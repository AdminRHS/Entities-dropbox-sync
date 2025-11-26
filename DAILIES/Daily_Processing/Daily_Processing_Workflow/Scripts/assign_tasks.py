#!/usr/bin/env python3
"""
assign_tasks.py - Task Assignment Script

Purpose: Assign extracted tasks to employees using multi-factor scoring algorithm.
         Balances workload while matching skills, professions, and departments.

Milestone: MLT-006 (Task Assignment Planning)
Time Savings: 45 min manual → 10 min automated (35 min saved)

Usage:
    python3 assign_tasks.py [--date YYYY-MM-DD] [--max-tasks N]

Examples:
    python3 assign_tasks.py
    python3 assign_tasks.py --date 2025-11-25
    python3 assign_tasks.py --max-tasks 8
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

# ============================================================================
# Configuration
# ============================================================================

DROPBOX_ROOT = Path.home() / "Library/CloudStorage/Dropbox"
WORKSPACE_ROOT = DROPBOX_ROOT / "ENTITIES/DAILIES/Daily_Processing"
PROFILES_ROOT = DROPBOX_ROOT / "ENTITIES/TALENTS/Employees/profiles"
SUPPORT_FILES_ROOT = DROPBOX_ROOT / "ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files"

# Assignment constraints
DEFAULT_MAX_TASKS_PER_EMPLOYEE = 10
DEFAULT_PREFERRED_TASKS_PER_EMPLOYEE = 5
TARGET_VARIANCE_PERCENT = 20  # <20% variance across department

# Scoring weights (100 points total)
PROFESSION_WEIGHT = 40
DEPARTMENT_WEIGHT = 20
SKILL_WEIGHT = 20
WORKLOAD_WEIGHT = 20

# ============================================================================
# Employee Profile Loading
# ============================================================================

def load_employee_profiles():
    """Load all employee profiles from Work folders."""
    profiles = []

    work_dir = PROFILES_ROOT / "Work"
    if not work_dir.exists():
        return profiles

    # Scan all department folders
    for dept_folder in work_dir.iterdir():
        if not dept_folder.is_dir():
            continue

        for profile_file in dept_folder.glob("Profile*.md"):
            profile = parse_profile(profile_file)
            if profile:
                profiles.append(profile)

    return profiles

def parse_profile(profile_path):
    """Parse employee profile markdown file."""
    try:
        content = profile_path.read_text()

        profile = {
            'file_path': str(profile_path),
            'name': extract_field(content, 'Name'),
            'profession': extract_field(content, 'Profession'),
            'department': profile_path.parent.name,
            'skills': [],
            'tools': [],
            'nov25_folder': extract_field(content, 'Nov25 Folder'),
            'current_workload': 0
        }

        # Extract skills
        skills_match = re.search(r'## Skills\s*\n\s*\n(.+?)(?:\n\n|\n##|$)', content, re.DOTALL)
        if skills_match:
            skills_text = skills_match.group(1).strip()
            profile['skills'] = [s.strip() for s in skills_text.split(',')]

        # Extract tools
        tools_match = re.search(r'## Tools\s*\n\s*\n(.+?)(?:\n\n|\n##|$)', content, re.DOTALL)
        if tools_match:
            tools_text = tools_match.group(1).strip()
            profile['tools'] = [t.strip() for t in tools_text.split(',')]

        return profile

    except Exception as e:
        print(f"  ⚠️  Error parsing {profile_path.name}: {e}")
        return None

def extract_field(content, field_name):
    """Extract field value from markdown."""
    pattern = rf'\*\*{field_name}:\*\*\s*(.+?)(?:\n|$)'
    match = re.search(pattern, content)
    return match.group(1).strip() if match else None

# ============================================================================
# Scoring Functions
# ============================================================================

def calculate_profession_score(task_profession, employee_profession):
    """Calculate profession match score (0-40 points)."""
    if not task_profession or not employee_profession:
        return 0

    task_prof_lower = task_profession.lower()
    emp_prof_lower = employee_profession.lower()

    # Perfect match
    if task_prof_lower == emp_prof_lower:
        return 40

    # Partial match (contains keywords)
    task_keywords = set(task_prof_lower.split())
    emp_keywords = set(emp_prof_lower.split())

    if task_keywords & emp_keywords:
        return 30

    # Transferable (manager can do planning, designer can do graphics)
    transferable_map = {
        'manager': ['lead', 'coordinator', 'organizer'],
        'designer': ['graphic', 'visual', 'creative'],
        'developer': ['programmer', 'engineer', 'coder'],
        'generator': ['researcher', 'analyst', 'prospector']
    }

    for base, related in transferable_map.items():
        if base in task_prof_lower:
            if any(r in emp_prof_lower for r in related):
                return 20

    return 0

def calculate_department_score(task_dept, employee_dept):
    """Calculate department match score (0-20 points)."""
    if not task_dept or not employee_dept:
        return 0

    task_dept_upper = task_dept.upper()
    emp_dept_upper = employee_dept.upper()

    # Same department
    if task_dept_upper == emp_dept_upper:
        return 20

    # Related departments
    related = {
        'DESIGN': ['VIDEO'],
        'VIDEO': ['DESIGN'],
        'AI': ['DEV'],
        'DEV': ['AI'],
        'SALES': ['LG'],
        'LG': ['SALES']
    }

    if emp_dept_upper in related.get(task_dept_upper, []):
        return 10

    return 0

def calculate_skill_score(task_skills, employee_skills, task_tool):
    """Calculate skill level match score (-10 to 20 points)."""
    if not task_skills and not task_tool:
        return 0

    # Check for exact skill match
    task_skills_lower = [s.lower() for s in task_skills]
    emp_skills_lower = [s.lower() for s in employee_skills]

    exact_match = any(ts in emp_skills_lower for ts in task_skills_lower)
    if exact_match:
        return 20

    # Check for tool match
    emp_tools_lower = [t.lower() for t in employee_skills]  # Skills often include tools
    if task_tool and task_tool.lower() in ' '.join(emp_tools_lower):
        return 10

    # Missing required skill (penalty)
    if task_skills and not any(ts in emp_skills_lower for ts in task_skills_lower):
        return -10

    return 0

def calculate_workload_score(current_workload, max_tasks=DEFAULT_MAX_TASKS_PER_EMPLOYEE):
    """Calculate workload balance score (0-20 points, or exclude if >max)."""
    if current_workload >= max_tasks:
        return None  # Exclude employee

    if current_workload <= 2:
        return 20
    elif current_workload <= 5:
        return 15
    elif current_workload <= 8:
        return 10
    else:  # 9-10
        return 5

def score_employee_for_task(task, employee, current_workloads):
    """Calculate total score for employee-task pair."""
    # Get current workload
    workload = current_workloads.get(employee['name'], 0)

    # Calculate workload score (may exclude)
    workload_score = calculate_workload_score(workload)
    if workload_score is None:
        return None  # Employee excluded (overloaded)

    # Calculate other scores
    profession_score = calculate_profession_score(
        task.get('profession', {}).get('name'),
        employee['profession']
    )

    department_score = calculate_department_score(
        task.get('department', {}).get('name'),
        employee['department']
    )

    skill_score = calculate_skill_score(
        task.get('skills', []),
        employee['skills'],
        task.get('tool', {}).get('name')
    )

    # Total score
    total = profession_score + department_score + skill_score + workload_score

    return {
        'total': total,
        'profession': profession_score,
        'department': department_score,
        'skill': skill_score,
        'workload': workload_score,
        'current_tasks': workload
    }

# ============================================================================
# Assignment Algorithm
# ============================================================================

def assign_tasks(date_str=None, max_tasks=DEFAULT_MAX_TASKS_PER_EMPLOYEE, dry_run=False):
    """
    Assign all extracted tasks to employees using scoring algorithm.

    Args:
        date_str: Date string in YYYY-MM-DD format
        max_tasks: Maximum tasks per employee
        dry_run: If True, only print what would be done

    Returns:
        dict: Assignment results
    """
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    print(f"{'[DRY RUN] ' if dry_run else ''}Task Assignment Planning")
    print(f"Date: {date_str}")
    print(f"Max Tasks per Employee: {max_tasks}")
    print("=" * 60)

    # Load workspace
    workspace = WORKSPACE_ROOT / f"{date_str}_Collection"
    extraction_dir = workspace / "02_Extracted_Tasks"
    assignment_dir = workspace / "05_Distribution_Plan"

    if not extraction_dir.exists():
        print(f"❌ Extraction directory not found: {extraction_dir}")
        print("   Run extract_tasks_batch.py first!")
        return None

    # Load employee profiles
    print("\n📋 Loading employee profiles...")
    employees = load_employee_profiles()
    print(f"   Loaded {len(employees)} employee profiles")

    # Load extracted tasks
    print("\n📋 Loading extracted tasks...")
    all_tasks = []
    extraction_files = list(extraction_dir.glob("*_extracted.json"))

    for extract_file in extraction_files:
        try:
            with open(extract_file) as f:
                data = json.load(f)
                tasks = data.get('tasks', [])
                for task in tasks:
                    task['source_file'] = extract_file.name
                    task['source_employee'] = data.get('employee')
                all_tasks.extend(tasks)
        except Exception as e:
            print(f"  ⚠️  Error loading {extract_file.name}: {e}")

    print(f"   Loaded {len(all_tasks)} tasks from {len(extraction_files)} files")

    if not all_tasks:
        print("\n❌ No tasks to assign!")
        return None

    # Assignment tracking
    assignments = {}  # employee_name -> [tasks]
    current_workloads = {}  # employee_name -> count
    unassigned_tasks = []

    # Assign each task
    print(f"\n📊 Assigning {len(all_tasks)} tasks...\n")

    for i, task in enumerate(all_tasks, 1):
        task_name = task.get('task_name', f'Task_{i}')

        # Score all employees
        scores = []
        for employee in employees:
            score_result = score_employee_for_task(task, employee, current_workloads)
            if score_result:  # Not excluded
                scores.append({
                    'employee': employee,
                    'score': score_result
                })

        if not scores:
            print(f"  ⚠️  No eligible employees for: {task_name}")
            unassigned_tasks.append(task)
            continue

        # Sort by total score (highest first)
        scores.sort(key=lambda x: x['score']['total'], reverse=True)

        # Assign to highest scoring employee
        winner = scores[0]
        employee_name = winner['employee']['name']

        if employee_name not in assignments:
            assignments[employee_name] = []

        assignments[employee_name].append({
            'task': task,
            'score': winner['score']['total']
        })

        current_workloads[employee_name] = current_workloads.get(employee_name, 0) + 1

        if i <= 5 or i % 20 == 0:  # Show first 5 and every 20th
            print(f"  [{i}/{len(all_tasks)}] {task_name} → {employee_name} (score: {winner['score']['total']})")

    # Calculate statistics
    stats = calculate_assignment_stats(assignments, employees, unassigned_tasks)

    # Summary
    print("\n" + "=" * 60)
    print(f"{'[DRY RUN] ' if dry_run else ''}ASSIGNMENT COMPLETE")
    print(f"Total Tasks: {len(all_tasks)}")
    print(f"Tasks Assigned: {len(all_tasks) - len(unassigned_tasks)}")
    print(f"Unassigned: {len(unassigned_tasks)}")
    print(f"Employees with Tasks: {len(assignments)}")
    print(f"Overall Workload Variance: {stats['overall_variance']:.1f}%")

    if not dry_run:
        # Create assignment directory
        assignment_dir.mkdir(exist_ok=True)

        # Save assignment plan
        save_assignment_plan(assignment_dir, date_str, assignments, stats, unassigned_tasks)

        print(f"\nAssignment plan saved to: {assignment_dir}")

    return {
        'assignments': assignments,
        'stats': stats,
        'unassigned': unassigned_tasks
    }

def calculate_assignment_stats(assignments, employees, unassigned):
    """Calculate assignment statistics and workload balance."""
    dept_stats = defaultdict(lambda: {'employees': 0, 'tasks': 0, 'max_tasks': 0})

    for emp_name, tasks in assignments.items():
        # Find employee dept
        employee = next((e for e in employees if e['name'] == emp_name), None)
        if not employee:
            continue

        dept = employee['department']
        task_count = len(tasks)

        dept_stats[dept]['employees'] += 1
        dept_stats[dept]['tasks'] += task_count
        dept_stats[dept]['max_tasks'] = max(dept_stats[dept]['max_tasks'], task_count)

    # Calculate variance per department
    for dept, stats in dept_stats.items():
        if stats['employees'] > 0:
            avg = stats['tasks'] / stats['employees']
            if avg > 0:
                variance = ((stats['max_tasks'] - avg) / avg) * 100
                stats['variance'] = variance
            else:
                stats['variance'] = 0

    # Overall stats
    total_tasks = sum(len(tasks) for tasks in assignments.values())
    total_employees = len(assignments)
    avg_overall = total_tasks / total_employees if total_employees > 0 else 0
    max_overall = max((len(tasks) for tasks in assignments.values()), default=0)
    variance_overall = ((max_overall - avg_overall) / avg_overall * 100) if avg_overall > 0 else 0

    return {
        'department_stats': dict(dept_stats),
        'total_tasks': total_tasks,
        'total_employees': total_employees,
        'avg_tasks_per_employee': avg_overall,
        'max_tasks_single_employee': max_overall,
        'overall_variance': variance_overall,
        'unassigned_count': len(unassigned)
    }

def save_assignment_plan(assignment_dir, date_str, assignments, stats, unassigned):
    """Save assignment plan as markdown."""
    plan_file = assignment_dir / f"assignment_plan_{date_str}.md"

    content = f"""# Task Assignment Plan - {date_str}

**Distribution Date:** {get_next_day(date_str)} (tomorrow)
**Tasks Assigned:** {stats['total_tasks']}
**Employees Assigned:** {stats['total_employees']}
**Unassigned Tasks:** {stats['unassigned_count']}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Overall Statistics

- **Total Tasks:** {stats['total_tasks']}
- **Employees with Tasks:** {stats['total_employees']}
- **Avg Tasks per Employee:** {stats['avg_tasks_per_employee']:.1f}
- **Max Tasks (Single Employee):** {stats['max_tasks_single_employee']}
- **Overall Workload Variance:** {stats['overall_variance']:.1f}% {'✅' if stats['overall_variance'] < TARGET_VARIANCE_PERCENT else '⚠️'}

---

## Department Statistics

"""

    for dept, dept_stats in stats['department_stats'].items():
        variance_status = '✅' if dept_stats.get('variance', 0) < TARGET_VARIANCE_PERCENT else '⚠️'
        content += f"""### {dept}
- Employees: {dept_stats['employees']}
- Tasks: {dept_stats['tasks']}
- Avg Tasks/Employee: {dept_stats['tasks'] / dept_stats['employees']:.1f}
- Max Tasks: {dept_stats['max_tasks']}
- Variance: {dept_stats.get('variance', 0):.1f}% {variance_status}

"""

    content += "\n---\n\n## Detailed Assignments\n\n"

    for emp_name, tasks in sorted(assignments.items()):
        task_count = len(tasks)
        content += f"""### {emp_name} ({task_count} tasks)

"""
        for i, assignment in enumerate(tasks, 1):
            task = assignment['task']
            score = assignment['score']
            content += f"""#### Task {i}: {task.get('task_name', 'Unnamed')}
- **Score:** {score}
- **Priority:** {task.get('priority', 'N/A')}
- **Estimated Duration:** {task.get('estimated_duration_minutes', 'N/A')} min
- **Description:** {task.get('description', 'N/A')}

"""

    # Unassigned tasks
    if unassigned:
        content += "\n---\n\n## Unassigned Tasks\n\n"
        for task in unassigned:
            content += f"- {task.get('task_name', 'Unnamed')}: {task.get('description', 'N/A')}\n"

    plan_file.write_text(content)

    # Also save as JSON
    json_file = assignment_dir / f"assignment_plan_{date_str}.json"
    json_data = {
        'date': date_str,
        'stats': stats,
        'assignments': {emp: [t['task'] for t in tasks] for emp, tasks in assignments.items()},
        'unassigned': unassigned
    }
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=2)

def get_next_day(date_str):
    """Get next day's date."""
    from datetime import datetime, timedelta
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_date = date + timedelta(days=1)
    return next_date.strftime('%Y-%m-%d')

# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Assign extracted tasks to employees',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--date',
        help='Date in YYYY-MM-DD format (default: today)',
        default=None
    )

    parser.add_argument(
        '--max-tasks',
        type=int,
        default=DEFAULT_MAX_TASKS_PER_EMPLOYEE,
        help=f'Maximum tasks per employee (default: {DEFAULT_MAX_TASKS_PER_EMPLOYEE})'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview assignments without saving'
    )

    args = parser.parse_args()

    result = assign_tasks(
        date_str=args.date,
        max_tasks=args.max_tasks,
        dry_run=args.dry_run
    )

    if result is None:
        return 1

    if result['stats']['unassigned_count'] > 0:
        print(f"\n⚠️  WARNING: {result['stats']['unassigned_count']} tasks could not be assigned!")

    return 0

if __name__ == "__main__":
    exit(main())
