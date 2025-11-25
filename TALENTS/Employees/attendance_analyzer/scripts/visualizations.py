#!/usr/bin/env python3
"""
Employee Attendance Visualization Module
Generate comprehensive visualizations for attendance analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from datetime import datetime, timedelta
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")


class AttendanceVisualizer:
    """Generate visualizations for employee attendance data"""

    def __init__(self, config_path='../config/analysis_config.json'):
        """Initialize visualizer with configuration"""
        self.script_dir = Path(__file__).parent
        self.config_path = self.script_dir / config_path
        self.load_config()
        self.df = None
        self.output_dir = None

    def load_config(self):
        """Load configuration from JSON file"""
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.output_dir = self.script_dir / self.config['output_paths']['charts_dir']
        self.fig_size = tuple(self.config['visualization_settings']['figure_size'])
        self.dpi = self.config['visualization_settings']['dpi']

        print(f"✓ Visualization configuration loaded")

    def load_data(self, dataframe=None, json_file=None):
        """Load data from dataframe or JSON file"""
        if dataframe is not None:
            self.df = dataframe
            print(f"✓ Loaded dataframe with {len(self.df)} records")
        elif json_file:
            json_path = self.script_dir / json_file
            self.df = pd.read_json(json_path)
            self._prepare_data()
            print(f"✓ Loaded data from {json_file}")
        else:
            # Load from default location
            json_file = self.script_dir / self.config['data_source']['json_file']
            self.df = pd.read_json(json_file)
            self._prepare_data()
            print(f"✓ Loaded data from {json_file}")

        return self.df

    def _prepare_data(self):
        """Prepare data for visualization (minimal processing)"""
        self.df['First Check In'] = pd.to_datetime(self.df['First Check In'], errors='coerce')
        self.df['Last Check Out'] = pd.to_datetime(self.df['Last Check Out'], errors='coerce')
        self.df['Has_Activity'] = self.df['Status'] == 'Active'

        # Calculate working hours if not present
        if 'Working_Hours' not in self.df.columns:
            break_hours = self.config['analysis_settings']['assumed_break_minutes'] / 60
            self.df['Working_Hours_Raw'] = (
                self.df['Last Check Out'] - self.df['First Check In']
            ).dt.total_seconds() / 3600
            self.df['Working_Hours'] = self.df['Working_Hours_Raw'] - break_hours
            self.df.loc[self.df['Working_Hours'] < 0, 'Working_Hours'] = 0

        if 'Check_In_Hour' not in self.df.columns:
            self.df['Check_In_Hour'] = self.df['First Check In'].dt.hour
            self.df['Check_Out_Hour'] = self.df['Last Check Out'].dt.hour

    def plot_working_hours_distribution(self, save=True):
        """Histogram of working hours distribution"""
        print("\nGenerating working hours distribution...")

        fig, axes = plt.subplots(2, 1, figsize=(12, 10))

        active_df = self.df[self.df['Has_Activity']].copy()

        # Histogram
        axes[0].hist(active_df['Working_Hours'].dropna(), bins=30,
                    color='skyblue', edgecolor='black', alpha=0.7)
        axes[0].axvline(active_df['Working_Hours'].mean(), color='red',
                       linestyle='--', linewidth=2, label=f'Mean: {active_df["Working_Hours"].mean():.2f}h')
        axes[0].axvline(active_df['Working_Hours'].median(), color='green',
                       linestyle='--', linewidth=2, label=f'Median: {active_df["Working_Hours"].median():.2f}h')
        axes[0].set_xlabel('Working Hours', fontsize=12)
        axes[0].set_ylabel('Number of Employees', fontsize=12)
        axes[0].set_title('Distribution of Working Hours', fontsize=14, fontweight='bold')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)

        # Box plot
        axes[1].boxplot(active_df['Working_Hours'].dropna(), vert=False, widths=0.5)
        axes[1].set_xlabel('Working Hours', fontsize=12)
        axes[1].set_title('Working Hours Box Plot (Outlier Detection)', fontsize=14, fontweight='bold')
        axes[1].grid(True, alpha=0.3)

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'working_hours_distribution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_heatmap_activity(self, save=True):
        """Heatmap of employee activity by hour"""
        print("\nGenerating activity heatmap...")

        active_df = self.df[self.df['Has_Activity']].copy()

        # Create hour bins
        check_in_hours = active_df['Check_In_Hour'].value_counts().sort_index()
        check_out_hours = active_df['Check_Out_Hour'].value_counts().sort_index()

        # Create matrix for heatmap
        hours = range(0, 24)
        data = pd.DataFrame({
            'Check-In': [check_in_hours.get(h, 0) for h in hours],
            'Check-Out': [check_out_hours.get(h, 0) for h in hours]
        }, index=hours)

        fig, ax = plt.subplots(figsize=(14, 6))

        sns.heatmap(data.T, annot=True, fmt='g', cmap='YlOrRd',
                   cbar_kws={'label': 'Number of Employees'}, ax=ax)

        ax.set_xlabel('Hour of Day', fontsize=12)
        ax.set_ylabel('Activity Type', fontsize=12)
        ax.set_title('Employee Activity Heatmap by Hour', fontsize=14, fontweight='bold')

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'activity_heatmap_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_gantt_timeline(self, save=True, max_employees=30):
        """Gantt-style timeline of employee presence"""
        print("\nGenerating timeline (Gantt chart)...")

        active_df = self.df[self.df['Has_Activity']].copy()
        active_df = active_df.dropna(subset=['First Check In', 'Last Check Out'])

        # Sort by check-in time and limit to top N
        active_df = active_df.sort_values('First Check In').head(max_employees)

        fig, ax = plt.subplots(figsize=(14, max(8, len(active_df) * 0.3)))

        colors = plt.cm.Set3(np.linspace(0, 1, len(active_df)))

        for idx, (_, row) in enumerate(active_df.iterrows()):
            start = row['First Check In']
            end = row['Last Check Out']

            # Convert to hours for plotting
            start_hour = start.hour + start.minute / 60
            end_hour = end.hour + end.minute / 60
            duration = end_hour - start_hour if end_hour > start_hour else (24 - start_hour) + end_hour

            ax.barh(idx, duration, left=start_hour, height=0.8,
                   color=colors[idx], edgecolor='black', alpha=0.7)

            # Add employee ID label
            emp_id = row['Employee ID']
            ax.text(start_hour - 0.5, idx, f'{emp_id}',
                   va='center', ha='right', fontsize=8)

        ax.set_xlabel('Hour of Day', fontsize=12)
        ax.set_ylabel('Employees', fontsize=12)
        ax.set_title(f'Employee Presence Timeline (Top {len(active_df)} Employees)',
                    fontsize=14, fontweight='bold')
        ax.set_xlim(0, 24)
        ax.set_xticks(range(0, 25, 2))
        ax.set_yticks([])
        ax.grid(True, axis='x', alpha=0.3)

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'timeline_gantt_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_arrival_departure_scatter(self, save=True):
        """Scatter plot of arrival vs departure times"""
        print("\nGenerating arrival vs departure scatter plot...")

        active_df = self.df[self.df['Has_Activity']].copy()
        active_df = active_df.dropna(subset=['Check_In_Hour', 'Check_Out_Hour'])

        fig, ax = plt.subplots(figsize=(12, 10))

        # Create scatter plot with working hours as color
        scatter = ax.scatter(active_df['Check_In_Hour'],
                           active_df['Check_Out_Hour'],
                           c=active_df['Working_Hours'],
                           s=100, alpha=0.6, cmap='viridis',
                           edgecolors='black', linewidth=0.5)

        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Working Hours', fontsize=11)

        # Add diagonal reference line (impossible region)
        ax.plot([0, 24], [0, 24], 'r--', alpha=0.3, linewidth=1, label='Same Time Line')

        ax.set_xlabel('Check-In Hour', fontsize=12)
        ax.set_ylabel('Check-Out Hour', fontsize=12)
        ax.set_title('Arrival vs Departure Time Pattern', fontsize=14, fontweight='bold')
        ax.set_xlim(0, 24)
        ax.set_ylim(0, 24)
        ax.grid(True, alpha=0.3)
        ax.legend()

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'arrival_departure_scatter_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_status_pie_chart(self, save=True):
        """Pie chart of employee statuses"""
        print("\nGenerating status pie chart...")

        status_counts = self.df['Status'].value_counts()

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Pie chart for Status
        colors_status = ['#90EE90', '#FFB6C6']
        axes[0].pie(status_counts, labels=status_counts.index, autopct='%1.1f%%',
                   colors=colors_status, startangle=90, textprops={'fontsize': 11})
        axes[0].set_title('Employee Status Distribution', fontsize=13, fontweight='bold')

        # Pie chart for Discord ID presence
        discord_counts = pd.Series({
            'Has Discord ID': self.df['Discord User ID'].notna().sum(),
            'No Discord ID': self.df['Discord User ID'].isna().sum()
        })
        colors_discord = ['#87CEEB', '#FFA07A']
        axes[1].pie(discord_counts, labels=discord_counts.index, autopct='%1.1f%%',
                   colors=colors_discord, startangle=90, textprops={'fontsize': 11})
        axes[1].set_title('Discord ID Registration', fontsize=13, fontweight='bold')

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'status_distribution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_anomalies_summary(self, save=True):
        """Bar chart of anomaly types"""
        print("\nGenerating anomalies summary...")

        if 'Total_Anomalies' not in self.df.columns:
            print("⚠ Anomaly detection not run. Skipping anomalies chart.")
            return

        anomaly_counts = {
            'Short Day': self.df['Anomaly_Short_Day'].sum(),
            'Long Day': self.df['Anomaly_Long_Day'].sum(),
            'Late Arrival': self.df['Anomaly_Late_Arrival'].sum(),
            'Early Departure': self.df['Anomaly_Early_Departure'].sum(),
            'Late Departure': self.df['Anomaly_Late_Departure'].sum(),
            'Missing Checkout': self.df['Missing_Checkout'].sum(),
        }

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Bar chart for anomaly types
        axes[0].bar(anomaly_counts.keys(), anomaly_counts.values(),
                   color='coral', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Anomaly Type', fontsize=11)
        axes[0].set_ylabel('Count', fontsize=11)
        axes[0].set_title('Anomalies Detected by Type', fontsize=13, fontweight='bold')
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].grid(True, axis='y', alpha=0.3)

        # Risk category distribution
        if 'Risk_Category' in self.df.columns:
            risk_counts = self.df['Risk_Category'].value_counts()
            colors_risk = {'High Risk': '#FF6B6B', 'Medium Risk': '#FFD93D',
                          'Normal': '#6BCF7F', 'Inactive': '#D3D3D3'}
            risk_colors = [colors_risk.get(cat, '#CCCCCC') for cat in risk_counts.index]

            axes[1].bar(risk_counts.index, risk_counts.values,
                       color=risk_colors, edgecolor='black', alpha=0.7)
            axes[1].set_xlabel('Risk Category', fontsize=11)
            axes[1].set_ylabel('Count', fontsize=11)
            axes[1].set_title('Employee Risk Distribution', fontsize=13, fontweight='bold')
            axes[1].grid(True, axis='y', alpha=0.3)

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'anomalies_summary_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_records_analysis(self, save=True):
        """Analyze records count distribution"""
        print("\nGenerating records count analysis...")

        active_df = self.df[self.df['Has_Activity']].copy()

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Histogram of records count
        axes[0].hist(active_df['Records Count'], bins=range(1, active_df['Records Count'].max() + 2),
                    color='lightblue', edgecolor='black', alpha=0.7)
        axes[0].set_xlabel('Number of Records', fontsize=11)
        axes[0].set_ylabel('Number of Employees', fontsize=11)
        axes[0].set_title('Distribution of Records Count', fontsize=13, fontweight='bold')
        axes[0].grid(True, alpha=0.3)

        # Scatter: records count vs working hours
        axes[1].scatter(active_df['Records Count'], active_df['Working_Hours'],
                       alpha=0.6, s=80, color='purple', edgecolors='black')
        axes[1].set_xlabel('Records Count', fontsize=11)
        axes[1].set_ylabel('Working Hours', fontsize=11)
        axes[1].set_title('Records Count vs Working Hours', fontsize=13, fontweight='bold')
        axes[1].grid(True, alpha=0.3)

        plt.tight_layout()

        if save:
            filename = self.output_dir / f'records_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def plot_comprehensive_dashboard(self, save=True):
        """Create a comprehensive dashboard with multiple metrics"""
        print("\nGenerating comprehensive dashboard...")

        active_df = self.df[self.df['Has_Activity']].copy()

        fig = plt.figure(figsize=(18, 12))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

        # 1. Working hours distribution
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.hist(active_df['Working_Hours'].dropna(), bins=20, color='skyblue', edgecolor='black')
        ax1.set_title('Working Hours Distribution', fontweight='bold')
        ax1.set_xlabel('Hours')
        ax1.set_ylabel('Count')

        # 2. Status pie chart
        ax2 = fig.add_subplot(gs[0, 1])
        status_counts = self.df['Status'].value_counts()
        ax2.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Status Distribution', fontweight='bold')

        # 3. Check-in hour distribution
        ax3 = fig.add_subplot(gs[0, 2])
        active_df['Check_In_Hour'].value_counts().sort_index().plot(kind='bar', ax=ax3, color='orange')
        ax3.set_title('Check-In Hour Distribution', fontweight='bold')
        ax3.set_xlabel('Hour')
        ax3.set_ylabel('Count')
        ax3.tick_params(axis='x', rotation=0)

        # 4. Check-out hour distribution
        ax4 = fig.add_subplot(gs[1, 0])
        active_df['Check_Out_Hour'].value_counts().sort_index().plot(kind='bar', ax=ax4, color='green')
        ax4.set_title('Check-Out Hour Distribution', fontweight='bold')
        ax4.set_xlabel('Hour')
        ax4.set_ylabel('Count')
        ax4.tick_params(axis='x', rotation=0)

        # 5. Working hours box plot
        ax5 = fig.add_subplot(gs[1, 1])
        ax5.boxplot(active_df['Working_Hours'].dropna(), vert=True)
        ax5.set_title('Working Hours Box Plot', fontweight='bold')
        ax5.set_ylabel('Hours')

        # 6. Records count distribution
        ax6 = fig.add_subplot(gs[1, 2])
        ax6.hist(active_df['Records Count'], bins=range(1, active_df['Records Count'].max() + 2),
                color='purple', edgecolor='black')
        ax6.set_title('Records Count Distribution', fontweight='bold')
        ax6.set_xlabel('Records')
        ax6.set_ylabel('Count')

        # 7. Arrival vs Departure scatter
        ax7 = fig.add_subplot(gs[2, :2])
        scatter = ax7.scatter(active_df['Check_In_Hour'], active_df['Check_Out_Hour'],
                            c=active_df['Working_Hours'], s=60, alpha=0.6, cmap='viridis')
        plt.colorbar(scatter, ax=ax7, label='Working Hours')
        ax7.set_title('Arrival vs Departure Time', fontweight='bold')
        ax7.set_xlabel('Check-In Hour')
        ax7.set_ylabel('Check-Out Hour')

        # 8. Statistics text box
        ax8 = fig.add_subplot(gs[2, 2])
        ax8.axis('off')
        stats_text = f"""
        STATISTICS SUMMARY

        Total: {len(self.df)}
        Active: {len(active_df)}
        Inactive: {len(self.df) - len(active_df)}

        Avg Hours: {active_df['Working_Hours'].mean():.2f}h
        Median Hours: {active_df['Working_Hours'].median():.2f}h
        Std Dev: {active_df['Working_Hours'].std():.2f}h

        Avg Check-In: {active_df['Check_In_Hour'].mean():.1f}:00
        Avg Check-Out: {active_df['Check_Out_Hour'].mean():.1f}:00
        """
        ax8.text(0.1, 0.5, stats_text, fontsize=11, family='monospace',
                verticalalignment='center')

        fig.suptitle('Employee Attendance Comprehensive Dashboard',
                    fontsize=16, fontweight='bold', y=0.995)

        if save:
            filename = self.output_dir / f'comprehensive_dashboard_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
            plt.savefig(filename, dpi=self.dpi, bbox_inches='tight')
            print(f"✓ Saved: {filename}")

        plt.close()

    def generate_all_visualizations(self, dataframe=None):
        """Generate all visualizations"""
        print("\n" + "="*80)
        print("GENERATING ALL VISUALIZATIONS")
        print("="*80)

        if dataframe is not None:
            self.load_data(dataframe=dataframe)
        elif self.df is None:
            self.load_data()

        # Generate all plots
        self.plot_working_hours_distribution()
        self.plot_heatmap_activity()
        self.plot_gantt_timeline()
        self.plot_arrival_departure_scatter()
        self.plot_status_pie_chart()
        self.plot_anomalies_summary()
        self.plot_records_analysis()
        self.plot_comprehensive_dashboard()

        print("\n" + "="*80)
        print("ALL VISUALIZATIONS GENERATED!")
        print("="*80)
        print(f"\nCharts saved to: {self.output_dir}")


def main():
    """Main execution function"""
    visualizer = AttendanceVisualizer()
    visualizer.generate_all_visualizations()
    return visualizer


if __name__ == "__main__":
    visualizer = main()
