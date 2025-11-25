"""
Generate comprehensive progress reports for video research
"""
import csv
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

def get_progress_file():
    """Get path to progress tracker CSV"""
    base_path = Path(__file__).parent.parent
    return base_path / 'VIDEO_PROGRESS_TRACKER.csv'

def get_reports_dir():
    """Get path to reports directory"""
    base_path = Path(__file__).parent.parent
    reports_dir = base_path / 'REPORTS'
    reports_dir.mkdir(exist_ok=True)
    return reports_dir

def load_progress_data():
    """Load all progress data"""
    progress_file = get_progress_file()

    if not progress_file.exists():
        print("❌ No progress data found")
        return []

    with open(progress_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def generate_summary_report():
    """Generate overall summary report"""
    data = load_progress_data()

    if not data:
        return "No data available"

    report = []
    report.append("# VIDEO RESEARCH PROGRESS SUMMARY")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Total Videos:** {len(data)}")

    # Status breakdown
    status_counts = defaultdict(int)
    for row in data:
        status_counts[row['Status']] += 1

    report.append("\n## Status Overview\n")
    for status, count in status_counts.items():
        percentage = (count / len(data)) * 100
        report.append(f"- **{status}**: {count} ({percentage:.1f}%)")

    # Phase breakdown
    report.append("\n## Current Phase Distribution\n")
    phase_counts = defaultdict(int)
    for row in data:
        phase = row['Current_Phase'].replace('_', ' ')
        phase_counts[phase] += 1

    for phase, count in sorted(phase_counts.items()):
        report.append(f"- {phase}: {count}")

    # Employee breakdown
    report.append("\n## Processing by Employee\n")
    employee_counts = defaultdict(int)
    for row in data:
        if row['Employee']:
            employee_counts[row['Employee']] += 1

    for employee, count in sorted(employee_counts.items(), key=lambda x: x[1], reverse=True):
        report.append(f"- {employee}: {count} videos")

    # Completion stats
    completed = [r for r in data if r['Status'] == 'Complete']
    if completed:
        total_days = sum(int(r['Total_Days']) for r in completed if r['Total_Days'])
        avg_days = total_days / len(completed) if completed else 0

        report.append(f"\n## Completion Statistics\n")
        report.append(f"- Completed Videos: {len(completed)}")
        report.append(f"- Average Processing Time: {avg_days:.1f} days")

    # Recent activity
    report.append("\n## Recent Activity (Last 7 Days)\n")
    recent_cutoff = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    recent_videos = []
    for row in data:
        for phase in ['Phase_1_Transcribed', 'Phase_2_Extraction', 'Phase_4_Integration']:
            if row.get(phase, '') >= recent_cutoff:
                recent_videos.append((row['Video_Number'], row['Title'], phase, row[phase]))
                break

    if recent_videos:
        for vid_num, title, phase, date in recent_videos[:10]:
            phase_name = phase.replace('Phase_', 'P').replace('_', ' ')
            report.append(f"- Video {vid_num}: {title[:40]}... - {phase_name} ({date})")
    else:
        report.append("- No recent activity")

    return '\n'.join(report)

def generate_detailed_report():
    """Generate detailed report with all videos"""
    data = load_progress_data()

    if not data:
        return "No data available"

    report = []
    report.append("# VIDEO RESEARCH DETAILED PROGRESS REPORT")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"\n---\n")

    for row in sorted(data, key=lambda x: int(x['Video_Number'])):
        report.append(f"## Video {row['Video_Number']}: {row['Title']}\n")
        report.append(f"**Status:** {row['Status']}")
        report.append(f"**Current Phase:** {row['Current_Phase'].replace('_', ' ')}")
        report.append(f"**Employee:** {row['Employee']}")
        report.append(f"**Started:** {row['Date_Started']}")

        if row['Date_Completed']:
            report.append(f"**Completed:** {row['Date_Completed']}")
            report.append(f"**Total Days:** {row['Total_Days']}")

        if row['YouTube_URL']:
            report.append(f"**YouTube:** {row['YouTube_URL']}")

        # Phase checklist
        report.append(f"\n**Processing Phases:**")

        phases = [
            ('Phase_0_Queued', 'Queued'),
            ('Phase_1_Transcribed', 'Transcribed + Analysis (PMT-004)'),
            ('Phase_2_Extraction', 'Entity Extraction (PMT-007)'),
            ('Phase_3_Gap_Analysis', 'Gap Analysis (PMT-009 Part 1)'),
            ('Phase_4_Integration', 'Integration (PMT-009 Part 2)'),
            ('Phase_5_Mapping', 'Mapping (PMT-009 Part 3)'),
        ]

        for phase_key, phase_name in phases:
            date = row.get(phase_key, '')
            if date:
                report.append(f"- ✅ {phase_name}: {date}")
            else:
                report.append(f"- ⏳ {phase_name}: Pending")

        if row['Notes']:
            report.append(f"\n**Notes:** {row['Notes']}")

        report.append(f"\n---\n")

    return '\n'.join(report)

def generate_weekly_report():
    """Generate weekly progress report"""
    data = load_progress_data()

    if not data:
        return "No data available"

    # Get activity from last 7 days
    week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

    report = []
    report.append("# WEEKLY VIDEO RESEARCH PROGRESS REPORT")
    report.append(f"\n**Week Ending:** {datetime.now().strftime('%Y-%m-%d')}")
    report.append(f"**Period:** Last 7 days")
    report.append(f"\n---\n")

    # Videos started this week
    started_this_week = [r for r in data if r['Date_Started'] >= week_ago]
    report.append(f"## Videos Started This Week: {len(started_this_week)}\n")

    for row in started_this_week:
        report.append(f"- Video {row['Video_Number']}: {row['Title']}")
        report.append(f"  - Started: {row['Date_Started']}")
        report.append(f"  - Employee: {row['Employee']}")
        report.append(f"  - Current: {row['Current_Phase'].replace('_', ' ')}")
        report.append("")

    # Videos completed this week
    completed_this_week = [r for r in data if r.get('Date_Completed', '') >= week_ago]
    report.append(f"## Videos Completed This Week: {len(completed_this_week)}\n")

    for row in completed_this_week:
        report.append(f"- Video {row['Video_Number']}: {row['Title']}")
        report.append(f"  - Completed: {row['Date_Completed']}")
        report.append(f"  - Processing Time: {row['Total_Days']} days")
        report.append("")

    # Active videos (in progress)
    in_progress = [r for r in data if r['Status'] == 'In Progress']
    report.append(f"## Currently In Progress: {len(in_progress)}\n")

    for row in in_progress[:10]:
        report.append(f"- Video {row['Video_Number']}: {row['Title'][:50]}...")
        report.append(f"  - Phase: {row['Current_Phase'].replace('_', ' ')}")
        report.append(f"  - Employee: {row['Employee']}")
        report.append("")

    # Productivity metrics
    if started_this_week or completed_this_week:
        report.append(f"## Weekly Metrics\n")
        report.append(f"- New Videos Started: {len(started_this_week)}")
        report.append(f"- Videos Completed: {len(completed_this_week)}")

        if completed_this_week:
            avg_days = sum(int(r['Total_Days']) for r in completed_this_week if r['Total_Days']) / len(completed_this_week)
            report.append(f"- Average Processing Time: {avg_days:.1f} days")

    report.append(f"\n---\n")

    return '\n'.join(report)

def save_report(content, filename):
    """Save report to file"""
    reports_dir = get_reports_dir()
    filepath = reports_dir / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Report saved: {filepath}")
    return filepath

def main():
    """Generate all reports"""
    import sys

    if len(sys.argv) < 2:
        print("Generate Progress Reports")
        print("\nUsage:")
        print("  python generate_progress_report.py <type>")
        print("\nReport Types:")
        print("  summary   - Overall summary report")
        print("  detailed  - Detailed report with all videos")
        print("  weekly    - Weekly activity report")
        print("  all       - Generate all reports")
        print("\nExamples:")
        print("  python generate_progress_report.py summary")
        print("  python generate_progress_report.py all")
        sys.exit(1)

    report_type = sys.argv[1]

    if report_type == 'summary':
        content = generate_summary_report()
        filename = f"Progress_Summary_{datetime.now().strftime('%Y-%m-%d')}.md"
        save_report(content, filename)

    elif report_type == 'detailed':
        content = generate_detailed_report()
        filename = f"Progress_Detailed_{datetime.now().strftime('%Y-%m-%d')}.md"
        save_report(content, filename)

    elif report_type == 'weekly':
        content = generate_weekly_report()
        filename = f"Progress_Weekly_{datetime.now().strftime('%Y-%m-%d')}.md"
        save_report(content, filename)

    elif report_type == 'all':
        # Generate all reports
        reports = [
            ('summary', generate_summary_report()),
            ('detailed', generate_detailed_report()),
            ('weekly', generate_weekly_report())
        ]

        for rtype, content in reports:
            filename = f"Progress_{rtype.capitalize()}_{datetime.now().strftime('%Y-%m-%d')}.md"
            save_report(content, filename)

        print("\n✅ All reports generated successfully")

    else:
        print(f"❌ Error: Unknown report type '{report_type}'")
        print("Valid types: summary, detailed, weekly, all")
        sys.exit(1)

if __name__ == '__main__':
    main()
