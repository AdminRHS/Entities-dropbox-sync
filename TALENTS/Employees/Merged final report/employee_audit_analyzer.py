#!/usr/bin/env python3
"""
Employee Audit Analysis and Report Generator
Analyzes employee working hours from JSON audit data and generates Markdown report
"""

import json
import os
import re
import glob
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Any, Optional

# ===== CONFIGURATION =====
class Config:
    AUDIT_FILE_1 = "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TALENTS/Employees/merged final report/final_audit_2025-11-24.json"
    AUDIT_FILE_2 = "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TALENTS/Employees/merged final report/final_audit_2025-11-25.json"
    PROFILES_BASE_1 = "/Users/nikolay/Library/CloudStorage/Dropbox/Nov25"
    PROFILES_BASE_2 = "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TALENTS/Employees/profiles"
    OUTPUT_FILE = "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TALENTS/Employees/merged final report/employee_hours_analysis_report.md"
    SUMMARY_FILE = "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TALENTS/Employees/merged final report/under_performers_summary.md"

    TARGET_STATUSES = {'Available', 'Work'}  # Exclude Project statuses
    DISCREPANCY_THRESHOLD = 0.5  # hours
    COMPLIANCE_THRESHOLD = 0.9  # 90%

    # Thresholds for new focused report
    FULL_TIME_THRESHOLD = 8.0  # hours
    PART_TIME_THRESHOLD = 4.0  # hours


# ===== UTILITY FUNCTIONS =====
def safe_float_conversion(value: Any, field_name: str = "value", default: float = 0.0) -> float:
    """Safely convert string to float with error handling"""
    try:
        if value is None or value == '' or value == '-':
            return default
        return float(value)
    except (ValueError, TypeError) as e:
        print(f"  Warning: Invalid {field_name} value: {value}, using {default}")
        return default


class ErrorLogger:
    """Centralized error logging"""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def log_error(self, category: str, message: str, details: Optional[Dict] = None):
        self.errors.append({
            'category': category,
            'message': message,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
        print(f"  ERROR [{category}]: {message}")

    def log_warning(self, category: str, message: str, details: Optional[Dict] = None):
        self.warnings.append({
            'category': category,
            'message': message,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
        print(f"  Warning [{category}]: {message}")

    def generate_error_report(self) -> str:
        """Generate error summary for report appendix"""
        if not self.errors and not self.warnings:
            return ""

        report = "\n## Error and Warning Log\n\n"

        if self.errors:
            report += "### Errors\n"
            for error in self.errors:
                report += f"- **[{error['category']}]** {error['message']}\n"

        if self.warnings:
            report += "\n### Warnings\n"
            for warning in self.warnings:
                report += f"- [{warning['category']}] {warning['message']}\n"

        return report


# ===== PROFILE MANAGER =====
class ProfileManager:
    """Manages employee profile loading and matching"""

    def __init__(self, profiles_bases: List[str], error_logger: ErrorLogger):
        self.profiles_bases = profiles_bases if isinstance(profiles_bases, list) else [profiles_bases]
        self.error_logger = error_logger
        self.profile_index: Dict[str, Dict] = {}

    def discover_all_profiles(self) -> List[str]:
        """Recursively find all Profile*.md files from multiple base directories"""
        all_profiles = []
        for base in self.profiles_bases:
            if not os.path.exists(base):
                self.error_logger.log_warning('PROFILE_PATH', f"Profile base path does not exist: {base}")
                continue
            pattern = os.path.join(base, '**', 'Profile*.md')
            profiles = glob.glob(pattern, recursive=True)
            all_profiles.extend(profiles)
            print(f"    Found {len(profiles)} profiles in {os.path.basename(base)}")
        return all_profiles

    def extract_profile_data(self, file_path: str) -> Optional[Dict]:
        """Extract profile data from markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.error_logger.log_error('FILE_READ', f"Failed to read {file_path}: {e}")
            return None

        profile_data = {'file_path': file_path}

        # Extract Name
        name_match = re.search(r'\*\*Name:\*\*\s+(.+)', content)
        if name_match:
            profile_data['name'] = name_match.group(1).strip()
        else:
            self.error_logger.log_warning('PROFILE_PARSE', f"No name found in {file_path}")
            return None

        # Extract Rate
        rate_match = re.search(r'\*\*Rate:\*\*\s+([\d.]+)', content)
        if rate_match:
            profile_data['rate'] = float(rate_match.group(1))
        else:
            profile_data['rate'] = None
            self.error_logger.log_warning('PROFILE_PARSE', f"No rate found for {profile_data['name']}")

        # Extract Status
        status_match = re.search(r'\*\*Status:\*\*\s+(.+)', content)
        if status_match:
            profile_data['status'] = status_match.group(1).strip()

        # Extract Employee ID
        id_match = re.search(r'\*\*ID:\*\*\s+(\d+)', content)
        if id_match:
            profile_data['employee_id'] = id_match.group(1)

        # Extract Profession
        profession_match = re.search(r'\*\*Profession:\*\*\s+(.+)', content)
        if profession_match:
            profile_data['profession'] = profession_match.group(1).strip()

        # Extract Department from file path
        path_parts = file_path.split(os.sep)
        if 'Nov25' in path_parts:
            idx = path_parts.index('Nov25')
            if idx + 1 < len(path_parts):
                profile_data['department'] = path_parts[idx + 1]

        return profile_data

    def build_index(self) -> Dict[str, Dict]:
        """Build searchable index of all profiles"""
        print("  Discovering profile files...")
        profile_files = self.discover_all_profiles()
        print(f"  Found {len(profile_files)} profile files")

        print("  Parsing profile data...")
        for file_path in profile_files:
            profile_data = self.extract_profile_data(file_path)
            if profile_data and 'name' in profile_data:
                self.profile_index[profile_data['name']] = profile_data

        print(f"  Successfully indexed {len(self.profile_index)} profiles")
        return self.profile_index

    def fuzzy_match_name(self, audit_name: str, audit_employee_id: Optional[str] = None) -> Optional[str]:
        """Multi-level fuzzy matching algorithm including ID matching"""
        # Level 0: Match by Employee ID (most reliable)
        if audit_employee_id:
            for profile_name, profile_data in self.profile_index.items():
                if profile_data.get('employee_id') == audit_employee_id:
                    return profile_name

        # Level 1: Exact match
        if audit_name in self.profile_index:
            return audit_name

        # Level 2: Case-insensitive exact match
        audit_lower = audit_name.lower()
        for profile_name in self.profile_index.keys():
            if profile_name.lower() == audit_lower:
                return profile_name

        # Level 3: Prefix match (handles abbreviated last names)
        # "Liliia D" matches "Liliia Dmytrenko"
        parts = audit_name.split()
        if len(parts) >= 2:
            first_name = parts[0].lower()
            last_part = parts[-1].lower()

            # Check if last part is likely an abbreviation (<=3 chars)
            if len(last_part) <= 3:
                for profile_name in self.profile_index.keys():
                    profile_parts = profile_name.split()
                    if len(profile_parts) >= 2:
                        if (profile_parts[0].lower() == first_name and
                            profile_parts[-1].lower().startswith(last_part)):
                            return profile_name

        # No match found
        return None


# ===== AUDIT DATA PROCESSOR =====
class AuditDataProcessor:
    """Processes audit JSON data"""

    def __init__(self, error_logger: ErrorLogger):
        self.error_logger = error_logger

    def load_json_file(self, file_path: str) -> List[Dict]:
        """Load JSON audit file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except Exception as e:
            self.error_logger.log_error('FILE_LOAD', f"Failed to load {file_path}: {e}")
            return []

    def validate_audit_record(self, record: Dict) -> Dict:
        """Validate and fill missing fields in audit record"""
        required_fields = {
            'Employee Name': 'Unknown',
            'Current Status': 'Unknown',
            'CRM Time': '0',
            'Discord Time': '0',
            'Verdict': '❓ UNKNOWN',
            'Leave': 'No',
            'Department': 'Unknown',
            'Date': 'Unknown'
        }

        for field, default in required_fields.items():
            if field not in record or record[field] is None or record[field] == '':
                record[field] = default

        return record

    def load_both_files(self, file1: str, file2: str) -> Dict[str, List[Dict]]:
        """Load both audit files"""
        data = {}

        print(f"  Loading {os.path.basename(file1)}...")
        data['2025-11-24'] = self.load_json_file(file1)

        print(f"  Loading {os.path.basename(file2)}...")
        data['2025-11-25'] = self.load_json_file(file2)

        # Validate records
        for date in data:
            data[date] = [self.validate_audit_record(r) for r in data[date]]

        return data

    def filter_by_status(self, records: List[Dict], target_statuses: set) -> List[Dict]:
        """Filter records by status"""
        return [r for r in records if r['Current Status'] in target_statuses]

    def enrich_with_profile(self, record: Dict, profile_manager: ProfileManager) -> Dict:
        """Match audit record to profile and add Rate"""
        employee_name = record['Employee Name']
        employee_id = record.get('Employee ID')

        # Try to match (now includes ID matching)
        matched_name = profile_manager.fuzzy_match_name(employee_name, employee_id)

        if matched_name:
            profile = profile_manager.profile_index[matched_name]
            record['Rate'] = profile.get('rate', 1.0)
            record['Profile_Status'] = profile.get('status', 'Unknown')
            record['Matched'] = True
            record['Match_Method'] = 'ID' if employee_id and profile.get('employee_id') == employee_id else 'Name'
            record['_profile_data'] = profile  # Store full profile data for later use
            if matched_name != employee_name:
                record['Matched_Name'] = matched_name
        else:
            record['Rate'] = 1.0  # Default to full-time
            record['Matched'] = False
            record['Profile_Status'] = 'Unknown'
            record['_profile_data'] = {}  # Empty profile data
            self.error_logger.log_warning('MATCH_FAILED',
                f"No profile match for '{employee_name}' (ID: {employee_id}) on {record['Date']}")

        return record


# ===== METRICS CALCULATOR =====
class MetricsCalculator:
    """Calculates all required metrics"""

    def calculate_employee_metrics(self, record: Dict) -> Dict:
        """Calculate all required metrics for one employee record"""
        metrics = {}

        # Parse time values
        crm_time = safe_float_conversion(record.get('CRM Time'), 'CRM Time')
        discord_time = safe_float_conversion(record.get('Discord Time'), 'Discord Time')
        rate = record.get('Rate', 1.0) if record.get('Rate') is not None else 1.0

        # Expected hours
        expected_hours = rate * 8

        # Time comparisons
        metrics['crm_time'] = crm_time
        metrics['discord_time'] = discord_time
        metrics['expected_hours'] = expected_hours
        metrics['rate'] = rate

        # Discrepancy analysis
        metrics['crm_discord_diff'] = abs(crm_time - discord_time)
        metrics['crm_discord_ratio'] = (crm_time / discord_time) if discord_time > 0 else 0
        metrics['crm_discord_match'] = metrics['crm_discord_diff'] <= Config.DISCREPANCY_THRESHOLD

        # Expected vs actual
        metrics['actual_vs_expected_crm'] = crm_time - expected_hours
        metrics['actual_vs_expected_discord'] = discord_time - expected_hours
        metrics['meets_expected_crm'] = crm_time >= (expected_hours * Config.COMPLIANCE_THRESHOLD)
        metrics['meets_expected_discord'] = discord_time >= (expected_hours * Config.COMPLIANCE_THRESHOLD)

        # Overall assessment
        metrics['compliant'] = metrics['crm_discord_match'] and metrics['meets_expected_crm']

        return metrics

    def aggregate_statistics(self, enriched_data: Dict[str, List[Dict]]) -> Dict:
        """Calculate summary statistics across all employees"""
        stats = {
            'total_employees': 0,
            'by_status': defaultdict(int),
            'by_department': defaultdict(lambda: {'count': 0, 'total_crm': 0, 'total_discord': 0}),
            'by_verdict': defaultdict(int),
            'by_date': {},
            'time_stats': {},
            'compliance_stats': {},
            'discrepancy_stats': {}
        }

        all_records = []
        all_crm_times = []
        all_discord_times = []
        compliant_count = 0
        discrepancy_major = 0

        # Process by date
        for date, records in enriched_data.items():
            date_crm = []
            date_discord = []

            for record in records:
                all_records.append(record)

                # Status breakdown
                stats['by_status'][record['Current Status']] += 1

                # Verdict breakdown
                stats['by_verdict'][record['Verdict']] += 1

                # Department breakdown
                dept = record.get('Department', 'Unknown')
                crm = safe_float_conversion(record.get('CRM Time'))
                discord = safe_float_conversion(record.get('Discord Time'))

                stats['by_department'][dept]['count'] += 1
                stats['by_department'][dept]['total_crm'] += crm
                stats['by_department'][dept]['total_discord'] += discord

                # Time collection
                all_crm_times.append(crm)
                all_discord_times.append(discord)
                date_crm.append(crm)
                date_discord.append(discord)

                # Compliance
                metrics = record.get('_metrics', {})
                if metrics.get('compliant'):
                    compliant_count += 1

                # Discrepancies
                if abs(crm - discord) > 1.0:  # Major discrepancy > 1 hour
                    discrepancy_major += 1

            stats['by_date'][date] = {
                'count': len(records),
                'total_crm': sum(date_crm),
                'total_discord': sum(date_discord),
                'avg_crm': sum(date_crm) / len(date_crm) if date_crm else 0,
                'avg_discord': sum(date_discord) / len(date_discord) if date_discord else 0
            }

        stats['total_employees'] = len(all_records)

        # Time statistics
        stats['time_stats'] = {
            'total_crm_time': sum(all_crm_times),
            'total_discord_time': sum(all_discord_times),
            'avg_crm_time': sum(all_crm_times) / len(all_crm_times) if all_crm_times else 0,
            'avg_discord_time': sum(all_discord_times) / len(all_discord_times) if all_discord_times else 0,
            'min_crm_time': min(all_crm_times) if all_crm_times else 0,
            'max_crm_time': max(all_crm_times) if all_crm_times else 0,
            'min_discord_time': min(all_discord_times) if all_discord_times else 0,
            'max_discord_time': max(all_discord_times) if all_discord_times else 0
        }

        # Compliance statistics
        stats['compliance_stats'] = {
            'compliant_count': compliant_count,
            'compliance_rate': (compliant_count / len(all_records) * 100) if all_records else 0
        }

        # Discrepancy statistics
        stats['discrepancy_stats'] = {
            'major_discrepancies': discrepancy_major,
            'major_discrepancy_rate': (discrepancy_major / len(all_records) * 100) if all_records else 0
        }

        return stats


# ===== REPORT GENERATOR =====
class ReportGenerator:
    """Generates comprehensive Markdown report"""

    def __init__(self):
        pass

    def generate_executive_summary(self, stats: Dict, enriched_data: Dict) -> str:
        """Generate executive summary section"""
        total = stats['total_employees']
        avg_crm = stats['time_stats']['avg_crm_time']
        avg_discord = stats['time_stats']['avg_discord_time']
        compliance = stats['compliance_stats']['compliance_rate']

        # Count employees on leave
        leave_count = sum(1 for date_records in enriched_data.values()
                         for r in date_records if r.get('Leave') == 'Yes')

        # Count critical alerts
        major_disc = stats['discrepancy_stats']['major_discrepancies']

        summary = f"""# Employee Working Hours Analysis Report

**Analysis Period:** November 24-25, 2025
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Total Employee Records Analyzed:** {total}

---

## Executive Summary

### Key Findings
- **Total employee records monitored:** {total} (across 2 days)
- **Status breakdown:** {', '.join(f"{status} ({count})" for status, count in stats['by_status'].items())}
- **Average daily hours (CRM):** {avg_crm:.2f} hours
- **Average daily hours (Discord):** {avg_discord:.2f} hours
- **Overall compliance rate:** {compliance:.1f}%
- **Employees on leave:** {leave_count}

### Critical Alerts
- **{major_disc} employee records** with significant CRM/Discord discrepancies (>1 hour)
- **{stats['by_verdict'].get('⚠️ NO REPORT', 0)} records** with missing or insufficient reports
- **{sum(1 for d in enriched_data.values() for r in d if not r.get('_metrics', {}).get('meets_expected_crm', True))} employee records** below expected hours (>10% under)

---
"""
        return summary

    def generate_status_breakdown(self, stats: Dict) -> str:
        """Generate status breakdown section"""
        total = stats['total_employees']

        section = """## 1. Employee Status Breakdown

### 1.1 Distribution by Status
| Status | Count | Percentage |
|--------|-------|------------|
"""
        for status, count in sorted(stats['by_status'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total * 100) if total > 0 else 0
            section += f"| {status} | {count} | {percentage:.1f}% |\n"

        section += f"| **Total** | **{total}** | **100%** |\n\n"

        # Department breakdown
        section += """### 1.2 Distribution by Department
| Department | Count | Avg Hours (CRM) | Avg Hours (Discord) |
|------------|-------|-----------------|---------------------|
"""
        for dept, data in sorted(stats['by_department'].items()):
            avg_crm = data['total_crm'] / data['count'] if data['count'] > 0 else 0
            avg_discord = data['total_discord'] / data['count'] if data['count'] > 0 else 0
            section += f"| {dept} | {data['count']} | {avg_crm:.2f} | {avg_discord:.2f} |\n"

        section += "\n---\n\n"
        return section

    def generate_working_hours_stats(self, stats: Dict) -> str:
        """Generate working hours statistics section"""
        ts = stats['time_stats']
        by_date = stats['by_date']

        section = f"""## 2. Working Hours Statistics

### 2.1 Overall Time Analysis
```
Total CRM Hours (2 days):     {ts['total_crm_time']:.2f} hours
Total Discord Hours (2 days): {ts['total_discord_time']:.2f} hours
Average CRM per record:       {ts['avg_crm_time']:.2f} hours
Average Discord per record:   {ts['avg_discord_time']:.2f} hours
Range (CRM):                  {ts['min_crm_time']:.2f} - {ts['max_crm_time']:.2f} hours
Range (Discord):              {ts['min_discord_time']:.2f} - {ts['max_discord_time']:.2f} hours
```

### 2.2 Daily Breakdown
| Date | Records | Total CRM Hours | Total Discord Hours | Avg CRM | Avg Discord |
|------|---------|-----------------|---------------------|---------|-------------|
"""
        for date in sorted(by_date.keys()):
            data = by_date[date]
            section += f"| {date} | {data['count']} | {data['total_crm']:.2f} | {data['total_discord']:.2f} | {data['avg_crm']:.2f} | {data['avg_discord']:.2f} |\n"

        section += "\n---\n\n"
        return section

    def generate_discrepancy_analysis(self, enriched_data: Dict) -> str:
        """Generate CRM vs Discord discrepancy analysis"""
        # Collect all records with metrics
        all_records = []
        for date_records in enriched_data.values():
            all_records.extend(date_records)

        # Categorize discrepancies
        perfect = sum(1 for r in all_records if r.get('_metrics', {}).get('crm_discord_diff', 999) <= 0.25)
        minor = sum(1 for r in all_records if 0.25 < r.get('_metrics', {}).get('crm_discord_diff', 999) <= 0.5)
        moderate = sum(1 for r in all_records if 0.5 < r.get('_metrics', {}).get('crm_discord_diff', 999) <= 1.0)
        major = sum(1 for r in all_records if r.get('_metrics', {}).get('crm_discord_diff', 999) > 1.0)

        total = len(all_records)

        section = f"""## 3. CRM vs Discord Time Analysis

### 3.1 Discrepancy Summary
```
Perfect Match (±15 min):       {perfect} records ({perfect/total*100:.1f}%)
Minor Discrepancy (15-30 min): {minor} records ({minor/total*100:.1f}%)
Moderate Discrepancy (30-60 min): {moderate} records ({moderate/total*100:.1f}%)
Major Discrepancy (>60 min):   {major} records ({major/total*100:.1f}%)
```

### 3.2 Significant Discrepancies (>30 minutes)
| Employee | Department | Date | CRM Time | Discord Time | Difference | Status |
|----------|------------|------|----------|--------------|------------|--------|
"""
        # Find records with significant discrepancies
        significant = [r for r in all_records if r.get('_metrics', {}).get('crm_discord_diff', 0) > 0.5]
        significant.sort(key=lambda x: x.get('_metrics', {}).get('crm_discord_diff', 0), reverse=True)

        for record in significant[:20]:  # Top 20
            metrics = record.get('_metrics', {})
            diff = metrics.get('crm_discord_diff', 0)
            section += f"| {record['Employee Name']} | {record.get('Department', 'Unknown')} | {record['Date']} | {metrics.get('crm_time', 0):.2f} | {metrics.get('discord_time', 0):.2f} | ±{diff:.2f} | ⚠️ |\n"

        if not significant:
            section += "| - | - | - | - | - | - | ✅ No significant discrepancies |\n"

        section += "\n---\n\n"
        return section

    def generate_expected_hours_analysis(self, enriched_data: Dict) -> str:
        """Generate actual vs expected hours analysis"""
        all_records = []
        for date_records in enriched_data.values():
            all_records.extend(date_records)

        # Categorize compliance
        fully_compliant = sum(1 for r in all_records if r.get('_metrics', {}).get('meets_expected_crm', False))
        under = sum(1 for r in all_records if not r.get('_metrics', {}).get('meets_expected_crm', False) and r.get('_metrics', {}).get('crm_time', 0) < r.get('_metrics', {}).get('expected_hours', 0))
        over = sum(1 for r in all_records if r.get('_metrics', {}).get('crm_time', 0) > r.get('_metrics', {}).get('expected_hours', 0) * 1.1)

        total = len(all_records)

        section = f"""## 4. Actual vs Expected Hours Analysis

### 4.1 Compliance Overview
```
Fully Compliant (≥90% expected): {fully_compliant} records ({fully_compliant/total*100:.1f}%)
Under Expected (<90%):           {under} records ({under/total*100:.1f}%)
Over Expected (>110%):           {over} records ({over/total*100:.1f}%)
```

### 4.2 Under-Performing Records (<90% of expected)
| Employee | Department | Date | Rate | Expected | Actual (CRM) | Variance | Percentage |
|----------|------------|------|------|----------|--------------|----------|------------|
"""
        under_performers = [r for r in all_records if not r.get('_metrics', {}).get('meets_expected_crm', False)]
        under_performers.sort(key=lambda x: x.get('_metrics', {}).get('actual_vs_expected_crm', 0))

        for record in under_performers[:15]:  # Top 15
            metrics = record.get('_metrics', {})
            expected = metrics.get('expected_hours', 8)
            actual = metrics.get('crm_time', 0)
            variance = metrics.get('actual_vs_expected_crm', 0)
            percentage = (actual / expected * 100) if expected > 0 else 0
            section += f"| {record['Employee Name']} | {record.get('Department', 'Unknown')} | {record['Date']} | {metrics.get('rate', 1):.2f} | {expected:.2f} | {actual:.2f} | {variance:.2f} | {percentage:.0f}% |\n"

        if not under_performers:
            section += "| - | - | - | - | - | - | - | ✅ All records meeting expectations |\n"

        section += "\n### 4.3 Over-Performing Records (>110% of expected)\n"
        section += "| Employee | Department | Date | Rate | Expected | Actual (CRM) | Overtime | Percentage |\n"
        section += "|----------|------------|------|------|----------|--------------|----------|------------|\n"

        over_performers = [r for r in all_records if r.get('_metrics', {}).get('crm_time', 0) > r.get('_metrics', {}).get('expected_hours', 0) * 1.1]
        over_performers.sort(key=lambda x: x.get('_metrics', {}).get('actual_vs_expected_crm', 0), reverse=True)

        for record in over_performers[:15]:  # Top 15
            metrics = record.get('_metrics', {})
            expected = metrics.get('expected_hours', 8)
            actual = metrics.get('crm_time', 0)
            variance = metrics.get('actual_vs_expected_crm', 0)
            percentage = (actual / expected * 100) if expected > 0 else 0
            section += f"| {record['Employee Name']} | {record.get('Department', 'Unknown')} | {record['Date']} | {metrics.get('rate', 1):.2f} | {expected:.2f} | {actual:.2f} | +{variance:.2f} | {percentage:.0f}% |\n"

        if not over_performers:
            section += "| - | - | - | - | - | - | - | - |\n"

        section += "\n---\n\n"
        return section

    def generate_report_quality_metrics(self, stats: Dict) -> str:
        """Generate report quality metrics section"""
        total = stats['total_employees']

        section = """## 5. Report Quality Metrics

### 5.1 Verdict Distribution
| Verdict | Count | Percentage | Description |
|---------|-------|------------|-------------|
"""
        for verdict, count in sorted(stats['by_verdict'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total * 100) if total > 0 else 0
            descriptions = {
                '✅ OK': 'Complete report, adequate hours',
                '⚠️ NO REPORT': 'Missing or insufficient report',
                '📦 PROJECT': 'External project work',
                '🏖️ LEAVE': 'On leave',
                '🚨 CHECK CRM': 'CRM time discrepancy',
                '💤 Inactive': 'No activity detected'
            }
            desc = descriptions.get(verdict, 'Other status')
            section += f"| {verdict} | {count} | {percentage:.1f}% | {desc} |\n"

        ok_count = stats['by_verdict'].get('✅ OK', 0)
        quality_score = (ok_count / total * 100) if total > 0 else 0

        section += f"\n### 5.2 Overall Quality Score\n"
        section += f"```\n"
        section += f"Quality Score: {quality_score:.1f}%\n"
        section += f"Reports with ✅ OK: {ok_count} / {total}\n"
        section += f"```\n\n---\n\n"

        return section

    def generate_leave_section(self, enriched_data: Dict) -> str:
        """Generate employees on leave section"""
        section = """## 6. Employees on Leave

| Employee | Department | Date | Status | Leave Rate |
|----------|------------|------|--------|------------|
"""
        leave_records = []
        for date_records in enriched_data.values():
            leave_records.extend([r for r in date_records if r.get('Leave') == 'Yes'])

        for record in leave_records:
            section += f"| {record['Employee Name']} | {record.get('Department', 'Unknown')} | {record['Date']} | 🏖️ On Leave | {record.get('Leave Rate', '-')} |\n"

        if not leave_records:
            section += "| - | - | - | - | No employees on leave during this period |\n"

        section += "\n---\n\n"
        return section

    def generate_individual_details(self, enriched_data: Dict) -> str:
        """Generate individual employee details table"""
        section = """## 7. Individual Employee Details

### Complete Data Table
| Employee | Dept | Status | Date | Rate | Expected | CRM | Discord | Diff | Verdict | Match |
|----------|------|--------|------|------|----------|-----|---------|------|---------|-------|
"""
        all_records = []
        for date_records in enriched_data.values():
            all_records.extend(date_records)

        # Sort by employee name, then date
        all_records.sort(key=lambda x: (x['Employee Name'], x['Date']))

        for record in all_records:
            metrics = record.get('_metrics', {})
            name = record['Employee Name']
            dept = record.get('Department', 'Unknown')
            status = record['Current Status']
            date = record['Date']
            rate = metrics.get('rate', 1)
            expected = metrics.get('expected_hours', 8)
            crm = metrics.get('crm_time', 0)
            discord = metrics.get('discord_time', 0)
            diff = metrics.get('crm_discord_diff', 0)
            verdict = record.get('Verdict', '❓')
            matched = '✅' if record.get('Matched', False) else '⚠️'

            section += f"| {name} | {dept} | {status} | {date} | {rate:.2f} | {expected:.2f} | {crm:.2f} | {discord:.2f} | ±{diff:.2f} | {verdict} | {matched} |\n"

        section += "\n---\n\n"
        return section

    def generate_recommendations(self, enriched_data: Dict, stats: Dict) -> str:
        """Generate recommendations section"""
        all_records = []
        for date_records in enriched_data.values():
            all_records.extend(date_records)

        # Find issues
        major_discrepancies = [r for r in all_records if r.get('_metrics', {}).get('crm_discord_diff', 0) > 1.0]
        under_performers = [r for r in all_records if not r.get('_metrics', {}).get('meets_expected_crm', False)]
        no_report = [r for r in all_records if 'NO REPORT' in r.get('Verdict', '')]

        section = """## 8. Recommendations

### Immediate Actions Required
"""
        if major_discrepancies:
            section += f"\n1. **Follow up with {len(major_discrepancies)} employee records** showing major CRM/Discord discrepancies (>1 hour)\n"
            for record in major_discrepancies[:5]:
                diff = record.get('_metrics', {}).get('crm_discord_diff', 0)
                section += f"   - {record['Employee Name']} ({record['Date']}): {diff:.2f} hour difference\n"
            if len(major_discrepancies) > 5:
                section += f"   - ... and {len(major_discrepancies) - 5} more\n"

        if under_performers:
            section += f"\n2. **Address under-performance** for {len(under_performers)} employee records below 90% expected hours\n"
            for record in under_performers[:5]:
                metrics = record.get('_metrics', {})
                percentage = (metrics.get('crm_time', 0) / metrics.get('expected_hours', 1) * 100) if metrics.get('expected_hours', 1) > 0 else 0
                section += f"   - {record['Employee Name']} ({record['Date']}): Only {percentage:.0f}% of expected hours\n"
            if len(under_performers) > 5:
                section += f"   - ... and {len(under_performers) - 5} more\n"

        if no_report:
            section += f"\n3. **Collect missing reports** from {len(no_report)} employee records with 'NO REPORT' verdict\n"
            unique_employees = list(set(r['Employee Name'] for r in no_report))
            for name in unique_employees[:5]:
                section += f"   - {name}\n"
            if len(unique_employees) > 5:
                section += f"   - ... and {len(unique_employees) - 5} more\n"

        section += """
### Process Improvements
1. Implement automated CRM-Discord sync validation
2. Set up daily alerts for discrepancies >30 minutes
3. Create rate-based expected hours dashboard
4. Standardize report submission requirements
5. Review employee Rate settings for accuracy

### Positive Highlights
"""
        compliant = sum(1 for r in all_records if r.get('_metrics', {}).get('compliant', False))
        perfect_match = sum(1 for r in all_records if r.get('_metrics', {}).get('crm_discord_diff', 999) <= 0.25)

        section += f"- {compliant} employee records consistently meeting/exceeding expectations\n"
        section += f"- {perfect_match} employee records with excellent CRM-Discord alignment (±15 min)\n"
        section += f"- Average compliance rate of {stats['compliance_stats']['compliance_rate']:.1f}% shows strong overall performance\n"

        section += "\n---\n\n"
        return section

    def generate_appendix(self, enriched_data: Dict, error_logger: ErrorLogger) -> str:
        """Generate appendix section"""
        all_records = []
        for date_records in enriched_data.values():
            all_records.extend(date_records)

        matched = sum(1 for r in all_records if r.get('Matched', False))
        unmatched = [r for r in all_records if not r.get('Matched', False)]

        section = f"""## Appendix

### A. Profile Matching Status
```
Successfully Matched: {matched} / {len(all_records)} ({matched/len(all_records)*100:.1f}%)
Unmatched Records: {len(unmatched)}
```
"""
        if unmatched:
            section += "\n#### Unmatched Employee Records (requiring manual review)\n"
            section += "| Employee Name | Department | Date | Status |\n"
            section += "|---------------|------------|------|--------|\n"

            # Show unique unmatched employees
            unique_unmatched = {}
            for r in unmatched:
                name = r['Employee Name']
                if name not in unique_unmatched:
                    unique_unmatched[name] = r

            for name, record in unique_unmatched.items():
                section += f"| {name} | {record.get('Department', 'Unknown')} | {record['Date']} | No profile found (using Rate=1.0) |\n"

        section += f"""
### B. Data Sources
- Audit Data (Nov 24): `final_audit_2025-11-24.json` ({len(enriched_data.get('2025-11-24', []))} records)
- Audit Data (Nov 25): `final_audit_2025-11-25.json` ({len(enriched_data.get('2025-11-25', []))} records)
- Profile Data: Employee profile markdown files in `Nov25/` directory structure

### C. Calculation Methodology

**Expected Hours:**
- Calculated as: Rate × 8 hours
- Example: Rate 0.5 (part-time) → 4 hours expected
- Example: Rate 1 (full-time) → 8 hours expected

**CRM vs Discord Discrepancy:**
- Absolute difference between CRM Time and Discord Time
- Match threshold: ±{Config.DISCREPANCY_THRESHOLD} hours ({Config.DISCREPANCY_THRESHOLD * 60:.0f} minutes)

**Compliance:**
- Employee is compliant if actual hours ≥ {Config.COMPLIANCE_THRESHOLD * 100:.0f}% of expected hours
- Example: Full-time (8h expected) → must work ≥ {8 * Config.COMPLIANCE_THRESHOLD:.1f} hours

"""
        # Add error log
        section += error_logger.generate_error_report()

        section += f"""
---

**Report Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Analysis Tool:** Employee Audit Analyzer v1.0
"""
        return section

    def generate_full_report(self, enriched_data: Dict, stats: Dict, error_logger: ErrorLogger) -> str:
        """Generate complete Markdown report"""
        print("  Generating report sections...")

        report = ""
        report += self.generate_executive_summary(stats, enriched_data)
        report += self.generate_status_breakdown(stats)
        report += self.generate_working_hours_stats(stats)
        report += self.generate_discrepancy_analysis(enriched_data)
        report += self.generate_expected_hours_analysis(enriched_data)
        report += self.generate_report_quality_metrics(stats)
        report += self.generate_leave_section(enriched_data)
        report += self.generate_individual_details(enriched_data)
        report += self.generate_recommendations(enriched_data, stats)
        report += self.generate_appendix(enriched_data, error_logger)

        return report


# ===== MAIN EXECUTION =====
def generate_summary_report(enriched_data: Dict, stats: Dict, error_logger: ErrorLogger) -> str:
    """Generate simple summary report with employees working less than expected hours"""
    all_records = []
    for date_records in enriched_data.values():
        all_records.extend(date_records)

    # Filter for under-performers (not meeting expected hours)
    under_performers = [r for r in all_records if not r.get('_metrics', {}).get('meets_expected_crm', True)]

    # Group by unique employees
    unique_under_performers = {}
    for r in under_performers:
        name = r['Employee Name']
        if name not in unique_under_performers:
            unique_under_performers[name] = []
        unique_under_performers[name].append(r)

    # Sort by days under-performing (most days first), then by average hours (lowest first)
    sorted_employees = sorted(
        unique_under_performers.items(),
        key=lambda x: (len(x[1]), -sum(rec.get('_metrics', {}).get('crm_time', 0) for rec in x[1]) / len(x[1])),
        reverse=True
    )

    report = f"""# Employees Working Less Than Expected Hours

**Analysis Period:** November 24-25, 2025
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Total Employees:** {len(sorted_employees)}

---

## Summary List

| # | Employee Name | Profession | Department | Days Under | Avg CRM Hours | Expected Hours | Avg % | Status |
|---|---------------|------------|------------|------------|---------------|----------------|-------|--------|
"""

    for idx, (name, records) in enumerate(sorted_employees, 1):
        days_under = len(records)
        avg_crm = sum(r.get('_metrics', {}).get('crm_time', 0) for r in records) / len(records)
        avg_expected = sum(r.get('_metrics', {}).get('expected_hours', 8) for r in records) / len(records)
        avg_percentage = (avg_crm / avg_expected * 100) if avg_expected > 0 else 0
        dept = records[0].get('Department', 'Unknown')
        status = records[0].get('Current Status', 'Unknown')

        # Get profession from profile data
        profession = records[0].get('_profile_data', {}).get('profession', 'N/A')

        report += f"| {idx} | {name} | {profession} | {dept} | {days_under}/2 | {avg_crm:.1f}h | {avg_expected:.1f}h | {avg_percentage:.0f}% | {status} |\n"

    report += f"""

---

## Day-by-Day Details

"""

    for name, records in sorted_employees:
        report += f"\n### {name}\n\n"

        # Get profession from first record
        profession = records[0].get('_profile_data', {}).get('profession', 'N/A')
        dept = records[0].get('Department', 'Unknown')
        status = records[0].get('Current Status', 'Unknown')

        report += f"**Profession:** {profession} | **Department:** {dept} | **Status:** {status}\n\n"
        report += "| Date | Expected | CRM Hours | Discord Hours | Percentage | Shortfall | Verdict |\n"
        report += "|------|----------|-----------|---------------|------------|-----------|----------|\n"

        for r in sorted(records, key=lambda x: x['Date']):
            metrics = r.get('_metrics', {})
            expected = metrics.get('expected_hours', 8)
            crm_time = metrics.get('crm_time', 0)
            discord_time = metrics.get('discord_time', 0)
            percentage = (crm_time / expected * 100) if expected > 0 else 0
            shortfall = expected - crm_time
            verdict = r.get('Verdict', '?')

            report += f"| {r['Date']} | {expected:.1f}h | {crm_time:.1f}h | {discord_time:.1f}h | {percentage:.0f}% | -{shortfall:.1f}h | {verdict} |\n"

    report += """

---

**Report Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

    return report


def main():
    print("=" * 60)
    print("Employee Audit Analysis Tool")
    print("=" * 60)

    # Initialize
    error_logger = ErrorLogger()

    # Step 1: Load profiles from both locations
    print("\n[1/7] Loading employee profiles...")
    profile_bases = [Config.PROFILES_BASE_1, Config.PROFILES_BASE_2]
    profile_manager = ProfileManager(profile_bases, error_logger)
    profile_index = profile_manager.build_index()
    print(f"✓ Loaded {len(profile_index)} profiles")

    # Step 2: Load audit data
    print("\n[2/7] Loading audit data...")
    processor = AuditDataProcessor(error_logger)
    audit_data = processor.load_both_files(Config.AUDIT_FILE_1, Config.AUDIT_FILE_2)
    total_records = sum(len(v) for v in audit_data.values())
    print(f"✓ Loaded {total_records} total audit records")

    # Step 3: Filter and enrich
    print("\n[3/7] Filtering and enriching data...")
    enriched_data = {}

    for date, records in audit_data.items():
        # Filter by status
        filtered = processor.filter_by_status(records, Config.TARGET_STATUSES)
        print(f"  {date}: {len(filtered)} records match target statuses")

        # Enrich with profile data
        for record in filtered:
            processor.enrich_with_profile(record, profile_manager)

        enriched_data[date] = filtered

    total_filtered = sum(len(v) for v in enriched_data.values())
    matched_count = sum(1 for records in enriched_data.values() for r in records if r.get('Matched', False))
    print(f"✓ Processed {total_filtered} filtered records ({matched_count} matched to profiles)")

    # Step 4: Calculate metrics
    print("\n[4/7] Calculating metrics...")
    calculator = MetricsCalculator()

    for date, records in enriched_data.items():
        for record in records:
            metrics = calculator.calculate_employee_metrics(record)
            record['_metrics'] = metrics

    stats = calculator.aggregate_statistics(enriched_data)
    print(f"✓ Generated comprehensive metrics")

    # Step 5: Generate full report
    print("\n[5/7] Generating comprehensive Markdown report...")
    generator = ReportGenerator()
    report_content = generator.generate_full_report(enriched_data, stats, error_logger)

    # Step 6: Write full report
    print("\n[6/7] Writing comprehensive report to file...")
    with open(Config.OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"✓ Comprehensive report saved to: {Config.OUTPUT_FILE}")

    # Step 7: Generate and write summary report
    print("\n[7/7] Generating summary report (employees working less than expected)...")
    summary_content = generate_summary_report(enriched_data, stats, error_logger)
    with open(Config.SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"✓ Summary report saved to: {Config.SUMMARY_FILE}")

    # Summary
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Total Records Analyzed: {stats['total_employees']}")
    print(f"Profile Match Rate: {matched_count}/{total_filtered} ({matched_count/total_filtered*100:.1f}%)")
    print(f"Compliance Rate: {stats['compliance_stats']['compliance_rate']:.1f}%")

    under_count = sum(1 for records in enriched_data.values() for r in records
                     if not r.get('_metrics', {}).get('meets_expected_crm', True))
    print(f"Under-Performing Records: {under_count} ({under_count/total_filtered*100:.1f}%)")

    if error_logger.errors:
        print(f"\n⚠️  {len(error_logger.errors)} errors logged")
    if error_logger.warnings:
        print(f"⚠️  {len(error_logger.warnings)} warnings logged")
    print("=" * 60)
    print(f"\nReports available at:")
    print(f"  1. Comprehensive: {Config.OUTPUT_FILE}")
    print(f"  2. Summary: {Config.SUMMARY_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
