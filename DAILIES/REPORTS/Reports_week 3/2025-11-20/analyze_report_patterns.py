"""
Analyze Department Report Patterns by Day of Week

This script analyzes processed department reports to identify patterns and
repetitions based on day of week, department, and activity types.

Usage:
    python analyze_report_patterns.py [--date-range START END] [--department DEPT_CODE]
"""

import json
import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
import argparse

def load_processed_reports(processed_dir):
    """Load all processed reports and their metadata."""
    reports = []
    mapping_file = processed_dir / "Department_Report_Mapping.json"
    
    if mapping_file.exists():
        with open(mapping_file, 'r', encoding='utf-8') as f:
            mapping_data = json.load(f)
            reports = mapping_data.get('processed_files', [])
    
    return reports

def extract_activities_from_report(report_path):
    """
    Extract activity patterns from a report file.
    
    Returns:
        dict with activity counts, task types, project mentions, etc.
    """
    if not report_path.exists():
        return None
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    activities = {
        'tasks_completed': 0,
        'tasks_in_progress': 0,
        'projects_active': 0,
        'key_achievements': 0,
        'mentions': defaultdict(int)
    }
    
    # Extract task counts
    tasks_completed_match = re.search(r'- \*\*Tasks Completed:\*\* (\d+)', content)
    if tasks_completed_match:
        activities['tasks_completed'] = int(tasks_completed_match.group(1))
    
    tasks_in_progress_match = re.search(r'- \*\*Tasks In Progress:\*\* (\d+)', content)
    if tasks_in_progress_match:
        activities['tasks_in_progress'] = int(tasks_in_progress_match.group(1))
    
    # Extract project count
    projects_match = re.search(r'- \*\*Projects Active:\*\* (\d+)', content)
    if projects_match:
        activities['projects_active'] = int(projects_match.group(1))
    
    # Count key achievements
    achievements_section = re.search(r'## 1\. EXECUTIVE SUMMARY.*?- \*\*Key Achievements:\*\*(.*?)(?=---|##)', content, re.DOTALL)
    if achievements_section:
        achievements_text = achievements_section.group(1)
        activities['key_achievements'] = len(re.findall(r'^\s*- ', achievements_text, re.MULTILINE))
    
    # Extract common keywords/patterns
    keywords = ['meeting', 'call', 'interview', 'training', 'bug', 'fix', 'deploy', 
                'design', 'client', 'automation', 'integration', 'review', 'approval']
    for keyword in keywords:
        count = len(re.findall(rf'\b{keyword}\b', content, re.IGNORECASE))
        if count > 0:
            activities['mentions'][keyword] = count
    
    return activities

def analyze_patterns_by_day(reports_data, processed_dir):
    """Analyze patterns grouped by day of week."""
    patterns = defaultdict(lambda: {
        'reports': [],
        'total_tasks_completed': 0,
        'total_tasks_in_progress': 0,
        'total_projects': 0,
        'departments': set(),
        'activities': defaultdict(int),
        'common_keywords': defaultdict(int)
    })
    
    for report_info in reports_data:
        day_name = report_info.get('day_of_week', {}).get('day_name', 'Unknown')
        if day_name == 'Unknown':
            continue
        
        pattern = patterns[day_name]
        pattern['reports'].append(report_info)
        pattern['departments'].add(report_info['dept_code'])
        
        # Load and analyze report content
        report_path = processed_dir / report_info['processed']
        activities = extract_activities_from_report(report_path)
        
        if activities:
            pattern['total_tasks_completed'] += activities['tasks_completed']
            pattern['total_tasks_in_progress'] += activities['tasks_in_progress']
            pattern['total_projects'] += activities['projects_active']
            
            for keyword, count in activities['mentions'].items():
                pattern['common_keywords'][keyword] += count
    
    # Convert sets to lists for JSON serialization
    for day_name in patterns:
        patterns[day_name]['departments'] = list(patterns[day_name]['departments'])
    
    return patterns

def analyze_department_patterns(reports_data, processed_dir):
    """Analyze patterns grouped by department."""
    dept_patterns = defaultdict(lambda: {
        'reports': [],
        'days_of_week': defaultdict(int),
        'total_tasks_completed': 0,
        'total_tasks_in_progress': 0,
        'avg_tasks_per_day': 0,
        'common_activities': defaultdict(int)
    })
    
    for report_info in reports_data:
        dept_code = report_info['dept_code']
        pattern = dept_patterns[dept_code]
        pattern['reports'].append(report_info)
        
        day_name = report_info.get('day_of_week', {}).get('day_name', 'Unknown')
        pattern['days_of_week'][day_name] += 1
        
        # Load and analyze report content
        report_path = processed_dir / report_info['processed']
        activities = extract_activities_from_report(report_path)
        
        if activities:
            pattern['total_tasks_completed'] += activities['tasks_completed']
            pattern['total_tasks_in_progress'] += activities['tasks_in_progress']
            
            for keyword, count in activities['mentions'].items():
                pattern['common_activities'][keyword] += count
    
    # Calculate averages
    for dept_code in dept_patterns:
        pattern = dept_patterns[dept_code]
        report_count = len(pattern['reports'])
        if report_count > 0:
            pattern['avg_tasks_per_day'] = pattern['total_tasks_completed'] / report_count
    
    return dept_patterns

def generate_pattern_report(patterns_by_day, patterns_by_dept, output_file):
    """Generate a comprehensive pattern analysis report."""
    report_lines = [
        "# Department Report Pattern Analysis",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Overview",
        "",
        f"- **Total Days Analyzed:** {len(patterns_by_day)}",
        f"- **Total Departments:** {len(patterns_by_dept)}",
        "",
        "---",
        "",
        "## Patterns by Day of Week",
        ""
    ]
    
    # Sort days by weekday order
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sorted_days = sorted(patterns_by_day.keys(), key=lambda x: day_order.index(x) if x in day_order else 99)
    
    for day_name in sorted_days:
        pattern = patterns_by_day[day_name]
        report_lines.extend([
            f"### {day_name}",
            "",
            f"- **Reports:** {len(pattern['reports'])}",
            f"- **Departments Active:** {len(pattern['departments'])} ({', '.join(pattern['departments'])})",
            f"- **Total Tasks Completed:** {pattern['total_tasks_completed']}",
            f"- **Total Tasks In Progress:** {pattern['total_tasks_in_progress']}",
            f"- **Total Projects Active:** {pattern['total_projects']}",
            ""
        ])
        
        if pattern['common_keywords']:
            top_keywords = sorted(pattern['common_keywords'].items(), key=lambda x: x[1], reverse=True)[:5]
            report_lines.append("**Top Activities:**")
            for keyword, count in top_keywords:
                report_lines.append(f"- {keyword}: {count} mentions")
            report_lines.append("")
        
        report_lines.append("---")
        report_lines.append("")
    
    report_lines.extend([
        "## Patterns by Department",
        ""
    ])
    
    for dept_code in sorted(patterns_by_dept.keys()):
        pattern = patterns_by_dept[dept_code]
        report_lines.extend([
            f"### {dept_code}",
            "",
            f"- **Total Reports:** {len(pattern['reports'])}",
            f"- **Total Tasks Completed:** {pattern['total_tasks_completed']}",
            f"- **Average Tasks per Day:** {pattern['avg_tasks_per_day']:.1f}",
            ""
        ])
        
        if pattern['days_of_week']:
            report_lines.append("**Activity by Day:**")
            for day_name, count in sorted(pattern['days_of_week'].items(), key=lambda x: day_order.index(x[0]) if x[0] in day_order else 99):
                report_lines.append(f"- {day_name}: {count} reports")
            report_lines.append("")
        
        if pattern['common_activities']:
            top_activities = sorted(pattern['common_activities'].items(), key=lambda x: x[1], reverse=True)[:5]
            report_lines.append("**Top Activities:**")
            for activity, count in top_activities:
                report_lines.append(f"- {activity}: {count} mentions")
            report_lines.append("")
        
        report_lines.append("---")
        report_lines.append("")
    
    report_lines.extend([
        "## Key Insights",
        "",
        "### Day-of-Week Patterns",
        ""
    ])
    
    # Find busiest day
    busiest_day = max(patterns_by_day.items(), key=lambda x: x[1]['total_tasks_completed'])
    report_lines.append(f"- **Busiest Day:** {busiest_day[0]} ({busiest_day[1]['total_tasks_completed']} tasks completed)")
    
    # Find most active department
    most_active_dept = max(patterns_by_dept.items(), key=lambda x: x[1]['total_tasks_completed'])
    report_lines.append(f"- **Most Active Department:** {most_active_dept[0]} ({most_active_dept[1]['total_tasks_completed']} tasks completed)")
    
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Pattern analysis report generated: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Analyze department report patterns')
    parser.add_argument('--date-range', nargs=2, metavar=('START', 'END'),
                       help='Date range in YYYY-MM-DD format')
    parser.add_argument('--department', help='Filter by department code (e.g., AID, DGN)')
    parser.add_argument('--output', default='Pattern_Analysis_Report.md',
                       help='Output file name')
    
    args = parser.parse_args()
    
    # Set up paths
    script_dir = Path(__file__).parent
    processed_dir = script_dir / "Departments_Processed_TM"
    
    # Load reports
    reports_data = load_processed_reports(processed_dir)
    
    # Filter by date range if provided
    if args.date_range:
        start_date = datetime.strptime(args.date_range[0], '%Y-%m-%d')
        end_date = datetime.strptime(args.date_range[1], '%Y-%m-%d')
        reports_data = [
            r for r in reports_data
            if start_date <= datetime.strptime(r['date'], '%Y-%m-%d') <= end_date
        ]
    
    # Filter by department if provided
    if args.department:
        reports_data = [r for r in reports_data if r['dept_code'] == args.department.upper()]
    
    if not reports_data:
        print("No reports found matching the criteria.")
        return
    
    print(f"Analyzing {len(reports_data)} reports...")
    
    # Analyze patterns
    patterns_by_day = analyze_patterns_by_day(reports_data, processed_dir)
    patterns_by_dept = analyze_department_patterns(reports_data, processed_dir)
    
    # Generate report
    output_file = processed_dir / args.output
    generate_pattern_report(patterns_by_day, patterns_by_dept, output_file)
    
    # Also save JSON data for programmatic access
    json_output = processed_dir / "Pattern_Analysis_Data.json"
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'generated': datetime.now().isoformat(),
                'total_reports': len(reports_data),
                'date_range': args.date_range,
                'department_filter': args.department
            },
            'patterns_by_day': {k: {**v, 'departments': list(v['departments'])} for k, v in patterns_by_day.items()},
            'patterns_by_department': {k: {**v, 'days_of_week': dict(v['days_of_week'])} for k, v in patterns_by_dept.items()}
        }, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"Pattern analysis data saved: {json_output}")

if __name__ == "__main__":
    main()

