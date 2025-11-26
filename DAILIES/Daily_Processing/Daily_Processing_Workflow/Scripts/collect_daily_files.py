#!/usr/bin/env python3
"""
collect_daily_files.py - Daily File Collection Script

Purpose: Automatically collect ALL .md files from each employee's today folder (DD)
         and copy them to the workspace with standardized naming.

Milestone: MLT-002 (Collection)
Time Savings: 30 min manual → 2 min automated (28 min saved)

Usage:
    python3 collect_daily_files.py [--date YYYY-MM-DD] [--week N] [--day DD]

Examples:
    python3 collect_daily_files.py
    python3 collect_daily_files.py --date 2025-11-25
    python3 collect_daily_files.py --week 4 --day 25
"""

import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime
import json
import csv

# ============================================================================
# Configuration
# ============================================================================

# Base directories
DROPBOX_ROOT = Path.home() / "Library/CloudStorage/Dropbox"
NOV25_ROOT = DROPBOX_ROOT / "Nov25"
WORKSPACE_ROOT = DROPBOX_ROOT / "ENTITIES/DAILIES/Daily_Processing"

# Departments to process
DEPARTMENTS = [
    "AI",
    "Design",
    "LG",
    "Video",
    "Sales",
    "Dev",
    "HR",
    "Finance Nov25"
]

# Department ISO code mapping
DEPT_CODES = {
    "AI": "AID",
    "Design": "DGN",
    "LG": "LGN",
    "Video": "VID",
    "Sales": "SLS",
    "Dev": "DEV",
    "HR": "HRM",
    "Finance Nov25": "FIN"
}

# ============================================================================
# Helper Functions
# ============================================================================

def get_current_week():
    """Calculate current week number based on Nov 2025 calendar."""
    today = datetime.now()
    day_of_month = today.day

    # Week 1: Nov 1-7, Week 2: Nov 8-14, Week 3: Nov 15-21, Week 4: Nov 22-28, Week 5: Nov 29-30
    week = ((day_of_month - 1) // 7) + 1
    return min(week, 5)  # Max 5 weeks in November

def get_day_of_month():
    """Get current day of month (DD)."""
    return datetime.now().day

def sanitize_employee_name(name):
    """Sanitize employee name for filename (replace spaces with underscores)."""
    return name.replace(" ", "_")

def get_department_code(dept_name):
    """Get ISO department code."""
    return DEPT_CODES.get(dept_name, dept_name.upper()[:3])

def create_workspace(date_str):
    """Create workspace folder structure for today's processing."""
    workspace = WORKSPACE_ROOT / f"{date_str}_Collection"

    subfolders = [
        "01_Collected_Files",
        "02_Extracted_Tasks",
        "03_Gap_Analysis",
        "04_Task_Templates",
        "05_Distribution_Plan"
    ]

    workspace.mkdir(parents=True, exist_ok=True)

    for subfolder in subfolders:
        (workspace / subfolder).mkdir(exist_ok=True)

    # Create processing log
    log_file = workspace / "06_Processing_Log.md"
    if not log_file.exists():
        create_processing_log(log_file, date_str)

    return workspace

def create_processing_log(log_file, date_str):
    """Initialize processing log file."""
    content = f"""# Daily Processing Log - {date_str}

**Processing Date:** {date_str}
**For Date (Distribution):** {get_next_day(date_str)}
**Processor:** [Your Name]
**Start Time:** {datetime.now().strftime('%H:%M')}

---

## Milestones Progress

- [ ] MLT-001: Setup (10 min)
- [ ] MLT-002: Collection (30 min)
- [ ] MLT-003: Entity Extraction (60 min)
- [ ] MLT-004: Gap Analysis (45 min)
- [ ] MLT-005: Template Creation (30 min)
- [ ] MLT-006: Task Assignment Planning (45 min)
- [ ] MLT-007: Task Distribution (30 min)
- [ ] MLT-008: Quality Assurance (20 min)
- [ ] MLT-009: Archival & Reporting (10 min)

---

## MLT-002: Collection Progress

### Started: {datetime.now().strftime('%H:%M')}

"""
    log_file.write_text(content)

def get_next_day(date_str):
    """Get next day's date string."""
    from datetime import datetime, timedelta
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_date = date + timedelta(days=1)
    return next_date.strftime('%Y-%m-%d')

def update_processing_log(log_file, stats):
    """Update processing log with collection statistics."""
    content = log_file.read_text()

    stats_text = f"""
### Completed: {datetime.now().strftime('%H:%M')}

### Departments Completed
"""
    for dept, count in stats['departments'].items():
        files = stats['dept_files'].get(dept, 0)
        stats_text += f"- [x] {dept} ({count} employees, {files} files)\n"

    stats_text += f"""
### Total Statistics
- **Employees Processed:** {stats['total_employees']}
- **Files Collected:** {stats['total_files']}
- **Departments:** {len(stats['departments'])}

### Issues Encountered
"""
    if stats['errors']:
        for error in stats['errors']:
            stats_text += f"- {error}\n"
    else:
        stats_text += "- None - all collections successful ✅\n"

    content += stats_text
    log_file.write_text(content)

# ============================================================================
# Main Collection Function
# ============================================================================

def collect_daily_files(date_str=None, week=None, day=None, dry_run=False):
    """
    Collect all .md files from employee daily folders.

    Args:
        date_str: Date string in YYYY-MM-DD format (default: today)
        week: Week number (1-5) (default: auto-calculate)
        day: Day of month (1-31) (default: today)
        dry_run: If True, only print what would be done without copying

    Returns:
        dict: Collection statistics
    """
    # Determine date and week/day
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    if not week:
        week = get_current_week()

    if not day:
        day = get_day_of_month()

    print(f"{'[DRY RUN] ' if dry_run else ''}Daily File Collection")
    print(f"Date: {date_str}")
    print(f"Week: Week_{week}")
    print(f"Day: {day}")
    print("=" * 60)

    # Create workspace
    if not dry_run:
        workspace = create_workspace(date_str)
        collection_dir = workspace / "01_Collected_Files"
        log_file = workspace / "06_Processing_Log.md"
    else:
        collection_dir = None
        log_file = None

    # Statistics
    stats = {
        'total_employees': 0,
        'total_files': 0,
        'departments': {},
        'dept_files': {},
        'errors': [],
        'files_collected': []
    }

    # Process each department
    for dept_name in DEPARTMENTS:
        dept_path = NOV25_ROOT / dept_name

        if not dept_path.exists():
            print(f"⚠️  Department not found: {dept_name}")
            stats['errors'].append(f"Department folder missing: {dept_name}")
            continue

        dept_code = get_department_code(dept_name)
        dept_employee_count = 0
        dept_file_count = 0

        print(f"\n📁 Processing: {dept_name} ({dept_code})")

        # Find all employee folders
        for employee_path in dept_path.iterdir():
            if not employee_path.is_dir():
                continue

            # Skip special folders
            if employee_path.name in ['Left', 'Archive', '.DS_Store']:
                continue

            employee_name = employee_path.name
            employee_clean = sanitize_employee_name(employee_name)

            # Build path to daily folder
            daily_folder = employee_path / f"Week_{week}" / str(day)

            if not daily_folder.exists():
                # Try without Week prefix
                daily_folder = employee_path / f"{week}" / str(day)

            if not daily_folder.exists():
                continue  # Employee doesn't have today's folder yet

            # Collect all .md files
            md_files = list(daily_folder.glob("*.md"))

            if not md_files:
                continue  # No markdown files

            dept_employee_count += 1
            stats['total_employees'] += 1

            print(f"  👤 {employee_name}: {len(md_files)} files")

            for md_file in md_files:
                # Generate new filename: {Dept}_{Employee}_{Original}.md
                new_filename = f"{dept_code}_{employee_clean}_{md_file.name}"

                if dry_run:
                    print(f"     → Would copy: {md_file.name} → {new_filename}")
                else:
                    dest_path = collection_dir / new_filename
                    shutil.copy2(md_file, dest_path)
                    stats['files_collected'].append({
                        'source': str(md_file),
                        'dest': new_filename,
                        'employee': employee_name,
                        'department': dept_name
                    })

                dept_file_count += 1
                stats['total_files'] += 1

        stats['departments'][dept_name] = dept_employee_count
        stats['dept_files'][dept_name] = dept_file_count

        print(f"  ✅ {dept_name}: {dept_employee_count} employees, {dept_file_count} files")

    # Final summary
    print("\n" + "=" * 60)
    print(f"{'[DRY RUN] ' if dry_run else ''}COLLECTION COMPLETE")
    print(f"Total Employees Processed: {stats['total_employees']}")
    print(f"Total Files Collected: {stats['total_files']}")
    print(f"Departments: {len(stats['departments'])}")

    if not dry_run:
        print(f"Files saved to: {collection_dir}")

        # Update processing log
        update_processing_log(log_file, stats)
        print(f"Log updated: {log_file}")

        # Save collection manifest
        manifest_file = collection_dir / "_collection_manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"Manifest saved: {manifest_file}")

    return stats

# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Collect daily .md files from all employees',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Collect files for today (auto-detect week and day)
  python3 collect_daily_files.py

  # Collect for specific date
  python3 collect_daily_files.py --date 2025-11-25

  # Collect for specific week and day
  python3 collect_daily_files.py --week 4 --day 25

  # Dry run (see what would be collected without copying)
  python3 collect_daily_files.py --dry-run
        """
    )

    parser.add_argument(
        '--date',
        help='Date in YYYY-MM-DD format (default: today)',
        default=None
    )

    parser.add_argument(
        '--week',
        type=int,
        help='Week number 1-5 (default: auto-calculate)',
        default=None
    )

    parser.add_argument(
        '--day',
        type=int,
        help='Day of month 1-31 (default: today)',
        default=None
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview what would be collected without actually copying files'
    )

    args = parser.parse_args()

    # Run collection
    stats = collect_daily_files(
        date_str=args.date,
        week=args.week,
        day=args.day,
        dry_run=args.dry_run
    )

    # Exit with error code if no files collected
    if stats['total_files'] == 0:
        print("\n⚠️  WARNING: No files were collected!")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
