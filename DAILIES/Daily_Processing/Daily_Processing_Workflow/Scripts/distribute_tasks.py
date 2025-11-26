#!/usr/bin/env python3
"""
distribute_tasks.py - Task Distribution Script

Purpose: Create/update tasks.md files in each employee's tomorrow folder (DD+1).
         Writes task descriptions with all details from templates.

Milestone: MLT-007 (Task Distribution)
Time Savings: 30 min manual → 5 min automated (25 min saved)

Usage:
    python3 distribute_tasks.py [--date YYYY-MM-DD] [--week N] [--day DD]

Examples:
    python3 distribute_tasks.py
    python3 distribute_tasks.py --date 2025-11-25
    python3 distribute_tasks.py --week 4 --day 26
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
import re

# ============================================================================
# Configuration
# ============================================================================

DROPBOX_ROOT = Path.home() / "Library/CloudStorage/Dropbox"
WORKSPACE_ROOT = DROPBOX_ROOT / "ENTITIES/DAILIES/Daily_Processing"
NOV25_ROOT = DROPBOX_ROOT / "Nov25"
PROFILES_ROOT = DROPBOX_ROOT / "ENTITIES/TALENTS/Employees/profiles"

# Department folder mapping
DEPT_FOLDERS = {
    'AI': 'AI',
    'AID': 'AI',
    'Design': 'Design',
    'DGN': 'Design',
    'LG': 'LG',
    'LGN': 'LG',
    'Video': 'Video',
    'VID': 'Video',
    'Sales': 'Sales',
    'SLS': 'Sales',
    'Dev': 'Dev',
    'DEV': 'Dev',
    'HR': 'HR',
    'HRM': 'HR',
    'Finance': 'Finance Nov25',
    'FIN': 'Finance Nov25'
}

# ============================================================================
# Helper Functions
# ============================================================================

def get_current_week():
    """Calculate current week number."""
    today = datetime.now()
    day_of_month = today.day
    week = ((day_of_month - 1) // 7) + 1
    return min(week, 5)

def get_tomorrow_info():
    """Get tomorrow's week and day."""
    tomorrow = datetime.now() + timedelta(days=1)
    day = tomorrow.day
    week = ((day - 1) // 7) + 1
    return min(week, 5), day

def find_employee_folder(employee_name, department):
    """Find employee's Nov25 folder."""
    # Map department code to folder name
    dept_folder_name = DEPT_FOLDERS.get(department, department)
    dept_path = NOV25_ROOT / dept_folder_name

    if not dept_path.exists():
        return None

    # Try exact match first
    employee_path = dept_path / employee_name
    if employee_path.exists():
        return employee_path

    # Try case-insensitive search
    for folder in dept_path.iterdir():
        if folder.is_dir() and folder.name.lower() == employee_name.lower():
            return folder

    return None

def create_tasks_md_header(employee_name, department, date_str, task_count, total_time):
    """Create tasks.md file header."""
    return f"""# Tasks for {date_str}

**Assigned To:** {employee_name}
**Department:** {department}
**Date:** {date_str}
**Total Tasks:** {task_count}
**Estimated Total Time:** {total_time} minutes ({total_time / 60:.1f} hours)

---

"""

def format_task_for_md(task, task_number):
    """Format a single task as markdown."""
    task_name = task.get('task_name', 'Unnamed Task')
    description = task.get('description', 'No description provided')
    priority = task.get('priority', 'medium').capitalize()
    duration = task.get('estimated_duration_minutes', 30)
    status = task.get('status', 'not_started').replace('_', ' ').title()

    # Tools
    tools = []
    if task.get('tool', {}).get('name'):
        tools.append(task['tool']['name'])

    # Skills
    skills = task.get('skills', [])

    # Action, Object
    action = task.get('action', {}).get('name', 'Action')
    obj = task.get('object', {}).get('name', 'Object')

    md = f"""## Task {task_number}: {task_name}

**Priority:** {priority}
**Estimated Duration:** {duration} minutes
**Status:** {status}

### Description
{description}

### Action & Object
- **Action:** {action}
- **Object:** {obj}

"""

    if tools:
        md += "### Required Tools\n"
        for tool in tools:
            md += f"- {tool}\n"
        md += "\n"

    if skills:
        md += "### Required Skills\n"
        for skill in skills:
            md += f"- {skill}\n"
        md += "\n"

    md += """### Checklist
- [ ] Task started
- [ ] Work completed
- [ ] Quality checked
- [ ] Deliverable saved
- [ ] Task marked complete

---

"""

    return md

# ============================================================================
# Main Distribution Function
# ============================================================================

def distribute_tasks(date_str=None, week=None, day=None, dry_run=False):
    """
    Distribute tasks to employee folders (DD+1).

    Args:
        date_str: Processing date (today)
        week: Week number for tomorrow (auto-calculate if None)
        day: Day number for tomorrow (auto-calculate if None)
        dry_run: Preview without writing files

    Returns:
        dict: Distribution statistics
    """
    # Determine dates
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Calculate tomorrow's date
    today = datetime.strptime(date_str, '%Y-%m-%d')
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')

    if not week or not day:
        week, day = get_tomorrow_info()

    print(f"{'[DRY RUN] ' if dry_run else ''}Task Distribution")
    print(f"Processing Date: {date_str}")
    print(f"Distribution Date: {tomorrow_str} (DD+1)")
    print(f"Target: Week_{week}/{day}/")
    print("=" * 60)

    # Load workspace
    workspace = WORKSPACE_ROOT / f"{date_str}_Collection"
    assignment_dir = workspace / "05_Distribution_Plan"

    if not assignment_dir.exists():
        print(f"❌ Assignment directory not found: {assignment_dir}")
        print("   Run assign_tasks.py first!")
        return None

    # Load assignment plan
    assignment_file = assignment_dir / f"assignment_plan_{date_str}.json"
    if not assignment_file.exists():
        print(f"❌ Assignment plan not found: {assignment_file}")
        return None

    with open(assignment_file) as f:
        assignment_data = json.load(f)

    assignments = assignment_data.get('assignments', {})
    stats_data = assignment_data.get('stats', {})

    print(f"\n📋 Loaded assignment plan")
    print(f"   Employees: {len(assignments)}")
    print(f"   Total Tasks: {stats_data.get('total_tasks', 0)}")

    # Load employee profiles (for department mapping)
    print("\n📋 Loading employee profiles...")
    profiles = load_employee_profiles()
    profile_map = {p['name']: p for p in profiles}
    print(f"   Loaded {len(profiles)} profiles")

    # Statistics
    stats = {
        'employees_processed': 0,
        'tasks_distributed': 0,
        'files_created': 0,
        'files_updated': 0,
        'errors': [],
        'distributions': []
    }

    # Distribute to each employee
    print(f"\n📤 Distributing to {len(assignments)} employees...\n")

    for i, (employee_name, tasks) in enumerate(assignments.items(), 1):
        print(f"[{i}/{len(assignments)}] {employee_name}: {len(tasks)} tasks")

        # Get employee profile
        profile = profile_map.get(employee_name)
        if not profile:
            print(f"  ⚠️  Profile not found, skipping")
            stats['errors'].append(f"Profile not found: {employee_name}")
            continue

        department = profile.get('department', 'Unknown')

        # Find employee folder
        employee_folder = find_employee_folder(employee_name, department)
        if not employee_folder:
            print(f"  ⚠️  Nov25 folder not found, skipping")
            stats['errors'].append(f"Nov25 folder not found: {employee_name}")
            continue

        # Create tomorrow's folder
        tomorrow_folder = employee_folder / f"Week_{week}" / str(day)

        if dry_run:
            print(f"  → Would create: {tomorrow_folder}")
            print(f"  → Would write {len(tasks)} tasks to tasks.md")
            stats['employees_processed'] += 1
            stats['tasks_distributed'] += len(tasks)
            continue

        # Create folder if needed
        tomorrow_folder.mkdir(parents=True, exist_ok=True)

        # Create tasks.md
        tasks_file = tomorrow_folder / "tasks.md"

        # Calculate total time
        total_time = sum(task.get('estimated_duration_minutes', 30) for task in tasks)

        # Create content
        content = create_tasks_md_header(
            employee_name,
            department,
            tomorrow_str,
            len(tasks),
            total_time
        )

        # Add each task
        for task_num, task in enumerate(tasks, 1):
            content += format_task_for_md(task, task_num)

        # Add footer
        content += f"""
---

**Generated by:** Daily Processing Automation
**Processing Date:** {date_str}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

        # Write file
        file_existed = tasks_file.exists()
        tasks_file.write_text(content)

        if file_existed:
            stats['files_updated'] += 1
            print(f"  ✅ Updated: {tasks_file}")
        else:
            stats['files_created'] += 1
            print(f"  ✅ Created: {tasks_file}")

        stats['employees_processed'] += 1
        stats['tasks_distributed'] += len(tasks)

        stats['distributions'].append({
            'employee': employee_name,
            'department': department,
            'task_count': len(tasks),
            'file': str(tasks_file)
        })

    # Summary
    print("\n" + "=" * 60)
    print(f"{'[DRY RUN] ' if dry_run else ''}DISTRIBUTION COMPLETE")
    print(f"Employees Processed: {stats['employees_processed']}/{len(assignments)}")
    print(f"Tasks Distributed: {stats['tasks_distributed']}")
    print(f"Files Created: {stats['files_created']}")
    print(f"Files Updated: {stats['files_updated']}")

    if stats['errors']:
        print(f"\n⚠️  Errors: {len(stats['errors'])}")
        for error in stats['errors'][:5]:  # Show first 5
            print(f"   - {error}")

    if not dry_run and stats['distributions']:
        # Save distribution manifest
        manifest_file = workspace / "05_Distribution_Plan" / f"distribution_manifest_{date_str}.json"
        with open(manifest_file, 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"\nManifest saved: {manifest_file}")

        # Update processing log
        log_file = workspace / "06_Processing_Log.md"
        if log_file.exists():
            update_log(log_file, stats)

    return stats

def load_employee_profiles():
    """Load employee profiles."""
    profiles = []
    work_dir = PROFILES_ROOT / "Work"

    if not work_dir.exists():
        return profiles

    for dept_folder in work_dir.iterdir():
        if not dept_folder.is_dir():
            continue

        for profile_file in dept_folder.glob("Profile*.md"):
            profile = parse_profile(profile_file, dept_folder.name)
            if profile:
                profiles.append(profile)

    return profiles

def parse_profile(profile_path, department):
    """Parse employee profile."""
    try:
        content = profile_path.read_text()

        name_match = re.search(r'\*\*Name:\*\*\s*(.+?)(?:\n|$)', content)
        name = name_match.group(1).strip() if name_match else None

        if not name:
            return None

        return {
            'name': name,
            'department': department
        }

    except Exception:
        return None

def update_log(log_file, stats):
    """Update processing log with distribution results."""
    content = log_file.read_text()

    update_text = f"""
## MLT-007: Task Distribution Progress

### Completed: {datetime.now().strftime('%H:%M')}

- **Employees Processed:** {stats['employees_processed']}
- **Tasks Distributed:** {stats['tasks_distributed']}
- **Files Created:** {stats['files_created']}
- **Files Updated:** {stats['files_updated']}
- **Errors:** {len(stats['errors'])}

"""

    content += update_text
    log_file.write_text(content)

# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Distribute tasks to employee folders',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Distribute tasks for today (to tomorrow's folders)
  python3 distribute_tasks.py

  # Distribute for specific date
  python3 distribute_tasks.py --date 2025-11-25

  # Specify tomorrow's week and day explicitly
  python3 distribute_tasks.py --week 4 --day 26

  # Dry run
  python3 distribute_tasks.py --dry-run
        """
    )

    parser.add_argument(
        '--date',
        help='Processing date in YYYY-MM-DD format (default: today)',
        default=None
    )

    parser.add_argument(
        '--week',
        type=int,
        help='Target week number for tomorrow (default: auto-calculate)',
        default=None
    )

    parser.add_argument(
        '--day',
        type=int,
        help='Target day number for tomorrow (default: auto-calculate)',
        default=None
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview distribution without creating files'
    )

    args = parser.parse_args()

    stats = distribute_tasks(
        date_str=args.date,
        week=args.week,
        day=args.day,
        dry_run=args.dry_run
    )

    if stats is None:
        return 1

    if stats['errors']:
        print(f"\n⚠️  WARNING: {len(stats['errors'])} errors occurred!")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
