#!/usr/bin/env python3
"""
Employee Attendance Analytics System
Comprehensive analysis of employee check-in/check-out data with anomaly detection
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


class EmployeeAnalytics:
    """Main class for employee attendance analysis"""

    def __init__(self, config_path='../config/analysis_config.json'):
        """Initialize analytics with configuration"""
        self.script_dir = Path(__file__).parent
        self.config_path = self.script_dir / config_path
        self.load_config()
        self.df = None
        self.stats = {}

    def load_config(self):
        """Load configuration from JSON file"""
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        print(f"✓ Configuration loaded from {self.config_path}")

    def load_data(self, json_file=None):
        """Load employee data from JSON file"""
        if json_file is None:
            json_file = self.script_dir / self.config['data_source']['json_file']
        else:
            json_file = Path(json_file)

        print(f"\nLoading data from: {json_file}")
        self.df = pd.read_json(json_file, encoding=self.config['data_source']['encoding'])
        print(f"✓ Loaded {len(self.df)} employee records")

        # Data cleaning and parsing
        self._clean_data()
        return self.df

    def _clean_data(self):
        """Clean and parse datetime columns"""
        print("\nCleaning and parsing data...")

        # Parse datetime columns
        self.df['First Check In'] = pd.to_datetime(
            self.df['First Check In'],
            errors='coerce'
        )
        self.df['Last Check Out'] = pd.to_datetime(
            self.df['Last Check Out'],
            errors='coerce'
        )

        # Create computed columns
        self.df['Has_Discord_ID'] = self.df['Discord User ID'].notna()
        self.df['Has_Activity'] = self.df['Status'] == 'Active'

        # Calculate working hours (raw, without break deduction)
        self.df['Working_Hours_Raw'] = (
            self.df['Last Check Out'] - self.df['First Check In']
        ).dt.total_seconds() / 3600

        # Calculate working hours with assumed break
        break_hours = self.config['analysis_settings']['assumed_break_minutes'] / 60
        self.df['Working_Hours'] = self.df['Working_Hours_Raw'] - break_hours
        self.df.loc[self.df['Working_Hours'] < 0, 'Working_Hours'] = 0

        # Extract time components
        self.df['Check_In_Hour'] = self.df['First Check In'].dt.hour
        self.df['Check_Out_Hour'] = self.df['Last Check Out'].dt.hour
        self.df['Check_In_Time'] = self.df['First Check In'].dt.time
        self.df['Check_Out_Time'] = self.df['Last Check Out'].dt.time

        print(f"✓ Data cleaned: {self.df['Has_Activity'].sum()} active employees")

    def detect_anomalies(self):
        """Detect anomalies in working hours and patterns"""
        print("\nDetecting anomalies...")

        thresholds = self.config['anomaly_thresholds']

        # Initialize anomaly flags
        self.df['Anomaly_Short_Day'] = False
        self.df['Anomaly_Long_Day'] = False
        self.df['Anomaly_Very_Short'] = False
        self.df['Anomaly_Late_Arrival'] = False
        self.df['Anomaly_Early_Departure'] = False
        self.df['Anomaly_Late_Departure'] = False
        self.df['Missing_Checkout'] = False

        # Only check active employees
        active_mask = self.df['Has_Activity']

        # Working hours anomalies
        self.df.loc[active_mask & (self.df['Working_Hours'] < thresholds['min_work_hours']),
                    'Anomaly_Short_Day'] = True
        self.df.loc[active_mask & (self.df['Working_Hours'] > thresholds['max_work_hours']),
                    'Anomaly_Long_Day'] = True
        self.df.loc[active_mask & (self.df['Working_Hours'] < thresholds['very_short_day_hours']),
                    'Anomaly_Very_Short'] = True

        # Time-based anomalies
        late_hour = int(thresholds['late_arrival_time'].split(':')[0])
        early_dept_hour = int(thresholds['early_departure_time'].split(':')[0])
        late_dept_hour = int(thresholds['late_departure_time'].split(':')[0])

        self.df.loc[active_mask & (self.df['Check_In_Hour'] >= late_hour),
                    'Anomaly_Late_Arrival'] = True
        self.df.loc[active_mask & (self.df['Check_Out_Hour'] <= early_dept_hour),
                    'Anomaly_Early_Departure'] = True
        self.df.loc[active_mask & (self.df['Check_Out_Hour'] >= late_dept_hour),
                    'Anomaly_Late_Departure'] = True

        # Missing checkout
        self.df.loc[active_mask & self.df['Last Check Out'].isna(),
                    'Missing_Checkout'] = True

        # Count total anomalies
        anomaly_cols = [col for col in self.df.columns if col.startswith('Anomaly_') or col == 'Missing_Checkout']
        self.df['Total_Anomalies'] = self.df[anomaly_cols].sum(axis=1)

        total_anomalies = (self.df['Total_Anomalies'] > 0).sum()
        print(f"✓ Detected {total_anomalies} employees with anomalies")

    def analyze_patterns(self):
        """Analyze work patterns and categorize employees"""
        print("\nAnalyzing work patterns...")

        # Categorize by arrival time
        def categorize_arrival(hour):
            if pd.isna(hour):
                return 'No Data'
            elif hour < 7:
                return 'Very Early Bird'
            elif hour < 9:
                return 'Early Bird'
            elif hour < 10:
                return 'On Time'
            else:
                return 'Late Arrival'

        self.df['Arrival_Category'] = self.df['Check_In_Hour'].apply(categorize_arrival)

        # Categorize by work duration
        def categorize_duration(hours):
            if pd.isna(hours) or hours == 0:
                return 'No Work'
            elif hours < 4:
                return 'Very Short'
            elif hours < 7:
                return 'Short Day'
            elif hours <= 9:
                return 'Standard'
            elif hours <= 11:
                return 'Overtime'
            else:
                return 'Excessive Hours'

        self.df['Duration_Category'] = self.df['Working_Hours'].apply(categorize_duration)

        # Employee risk category
        def risk_category(row):
            if not row['Has_Activity']:
                return 'Inactive'
            elif row['Total_Anomalies'] >= 3:
                return 'High Risk'
            elif row['Total_Anomalies'] >= 1:
                return 'Medium Risk'
            else:
                return 'Normal'

        self.df['Risk_Category'] = self.df.apply(risk_category, axis=1)

        print(f"✓ Patterns analyzed and employees categorized")

    def calculate_statistics(self):
        """Calculate comprehensive statistics"""
        print("\nCalculating statistics...")

        active_df = self.df[self.df['Has_Activity']].copy()

        self.stats = {
            'total_employees': len(self.df),
            'active_employees': len(active_df),
            'inactive_employees': len(self.df) - len(active_df),
            'with_discord_id': self.df['Has_Discord_ID'].sum(),
            'without_discord_id': (~self.df['Has_Discord_ID']).sum(),

            # Working hours statistics
            'avg_working_hours': active_df['Working_Hours'].mean(),
            'median_working_hours': active_df['Working_Hours'].median(),
            'std_working_hours': active_df['Working_Hours'].std(),
            'min_working_hours': active_df['Working_Hours'].min(),
            'max_working_hours': active_df['Working_Hours'].max(),

            # Records statistics
            'avg_records_count': active_df['Records Count'].mean(),
            'total_records': active_df['Records Count'].sum(),

            # Time statistics
            'avg_check_in_hour': active_df['Check_In_Hour'].mean(),
            'avg_check_out_hour': active_df['Check_Out_Hour'].mean(),

            # Anomalies
            'total_anomalies_detected': (self.df['Total_Anomalies'] > 0).sum(),
            'short_day_count': self.df['Anomaly_Short_Day'].sum(),
            'long_day_count': self.df['Anomaly_Long_Day'].sum(),
            'late_arrivals': self.df['Anomaly_Late_Arrival'].sum(),
            'missing_checkouts': self.df['Missing_Checkout'].sum(),

            # Risk categories
            'high_risk_employees': (self.df['Risk_Category'] == 'High Risk').sum(),
            'medium_risk_employees': (self.df['Risk_Category'] == 'Medium Risk').sum(),
            'normal_employees': (self.df['Risk_Category'] == 'Normal').sum(),
        }

        print(f"✓ Statistics calculated")
        return self.stats

    def generate_summary_report(self):
        """Generate text summary report"""
        print("\nGenerating summary report...")

        report = []
        report.append("=" * 80)
        report.append("EMPLOYEE ATTENDANCE ANALYSIS REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        report.append("")

        report.append("OVERVIEW")
        report.append("-" * 80)
        report.append(f"Total Employees: {self.stats['total_employees']}")
        report.append(f"Active Employees: {self.stats['active_employees']} ({self.stats['active_employees']/self.stats['total_employees']*100:.1f}%)")
        report.append(f"Inactive Employees: {self.stats['inactive_employees']} ({self.stats['inactive_employees']/self.stats['total_employees']*100:.1f}%)")
        report.append(f"With Discord ID: {self.stats['with_discord_id']}")
        report.append(f"Without Discord ID: {self.stats['without_discord_id']}")
        report.append("")

        report.append("WORKING HOURS ANALYSIS")
        report.append("-" * 80)
        report.append(f"Average Working Hours: {self.stats['avg_working_hours']:.2f}h")
        report.append(f"Median Working Hours: {self.stats['median_working_hours']:.2f}h")
        report.append(f"Standard Deviation: {self.stats['std_working_hours']:.2f}h")
        report.append(f"Min Working Hours: {self.stats['min_working_hours']:.2f}h")
        report.append(f"Max Working Hours: {self.stats['max_working_hours']:.2f}h")
        report.append("")

        report.append("CHECK-IN/OUT PATTERNS")
        report.append("-" * 80)
        report.append(f"Average Check-In Time: {self.stats['avg_check_in_hour']:.1f}:00")
        report.append(f"Average Check-Out Time: {self.stats['avg_check_out_hour']:.1f}:00")
        report.append("")

        # Arrival categories
        arrival_dist = self.df['Arrival_Category'].value_counts()
        report.append("Arrival Time Distribution:")
        for category, count in arrival_dist.items():
            report.append(f"  {category}: {count} ({count/len(self.df)*100:.1f}%)")
        report.append("")

        report.append("ANOMALIES DETECTED")
        report.append("-" * 80)
        report.append(f"Total Employees with Anomalies: {self.stats['total_anomalies_detected']}")
        report.append(f"Short Day (<4h): {self.stats['short_day_count']}")
        report.append(f"Long Day (>12h): {self.stats['long_day_count']}")
        report.append(f"Late Arrivals: {self.stats['late_arrivals']}")
        report.append(f"Missing Checkouts: {self.stats['missing_checkouts']}")
        report.append("")

        report.append("RISK ASSESSMENT")
        report.append("-" * 80)
        report.append(f"High Risk: {self.stats['high_risk_employees']} employees")
        report.append(f"Medium Risk: {self.stats['medium_risk_employees']} employees")
        report.append(f"Normal: {self.stats['normal_employees']} employees")
        report.append("")

        # Top issues
        report.append("TOP 10 EMPLOYEES WITH MOST ANOMALIES")
        report.append("-" * 80)
        top_anomalies = self.df.nlargest(10, 'Total_Anomalies')[
            ['Employee ID', 'Total_Anomalies', 'Risk_Category', 'Working_Hours']
        ]
        report.append(top_anomalies.to_string(index=False))
        report.append("")

        report.append("=" * 80)

        summary_text = "\n".join(report)

        # Save to file
        output_dir = self.script_dir / self.config['output_paths']['summaries_dir']
        output_file = output_dir / f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary_text)

        print(f"✓ Summary report saved to: {output_file}")
        print("\n" + summary_text)

        return summary_text

    def export_to_excel(self, filename=None):
        """Export detailed analysis to Excel with multiple sheets"""
        print("\nExporting to Excel...")

        if filename is None:
            output_dir = self.script_dir / self.config['output_paths']['reports_dir']
            filename = output_dir / f"attendance_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Sheet 1: Full data
            self.df.to_excel(writer, sheet_name='Full Data', index=False)

            # Sheet 2: Active employees only
            active_df = self.df[self.df['Has_Activity']].copy()
            active_df.to_excel(writer, sheet_name='Active Employees', index=False)

            # Sheet 3: Anomalies
            anomalies_df = self.df[self.df['Total_Anomalies'] > 0].copy()
            anomalies_cols = ['Employee ID', 'Discord User ID', 'Working_Hours', 'Total_Anomalies',
                             'Anomaly_Short_Day', 'Anomaly_Long_Day', 'Anomaly_Late_Arrival',
                             'Anomaly_Early_Departure', 'Missing_Checkout', 'Risk_Category']
            anomalies_df[anomalies_cols].to_excel(writer, sheet_name='Anomalies', index=False)

            # Sheet 4: Statistics summary
            stats_df = pd.DataFrame([self.stats]).T
            stats_df.columns = ['Value']
            stats_df.to_excel(writer, sheet_name='Statistics')

            # Sheet 5: Inactive employees
            inactive_df = self.df[~self.df['Has_Activity']].copy()
            inactive_df[['Employee ID', 'Discord User ID', 'Status']].to_excel(
                writer, sheet_name='Inactive Employees', index=False
            )

            # Sheet 6: Patterns summary
            patterns_summary = pd.DataFrame({
                'Arrival Category': self.df['Arrival_Category'].value_counts(),
                'Duration Category': self.df['Duration_Category'].value_counts(),
                'Risk Category': self.df['Risk_Category'].value_counts()
            })
            patterns_summary.to_excel(writer, sheet_name='Patterns Summary')

        print(f"✓ Excel report saved to: {filename}")
        return filename

    def export_to_csv(self):
        """Export main data to CSV"""
        output_dir = self.script_dir / self.config['output_paths']['reports_dir']
        csv_file = output_dir / f"attendance_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        self.df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"✓ CSV export saved to: {csv_file}")
        return csv_file

    def run_full_analysis(self, json_file=None):
        """Run complete analysis pipeline"""
        print("\n" + "="*80)
        print("STARTING FULL EMPLOYEE ATTENDANCE ANALYSIS")
        print("="*80)

        # Load and process data
        self.load_data(json_file)
        self.detect_anomalies()
        self.analyze_patterns()
        self.calculate_statistics()

        # Generate reports
        self.generate_summary_report()
        excel_file = self.export_to_excel()
        csv_file = self.export_to_csv()

        print("\n" + "="*80)
        print("ANALYSIS COMPLETE!")
        print("="*80)
        print(f"\nGenerated files:")
        print(f"  - Excel report: {excel_file}")
        print(f"  - CSV export: {csv_file}")
        print(f"\nNext step: Run visualizations.py to generate charts")

        return self.df, self.stats


def main():
    """Main execution function"""
    # Initialize and run analysis
    analyzer = EmployeeAnalytics()
    df, stats = analyzer.run_full_analysis()

    return analyzer


if __name__ == "__main__":
    analyzer = main()
