"""
Day 28 Task Extraction Script
Extracts TST-### tasks from employee daily.md files
Follows MAIN_PROMPT_v7.2.md task extraction methodology
"""

import os
import re
import json
from datetime import datetime
from collections import defaultdict

# Configuration
BASE_PATH = r'C:\Users\Dell\Dropbox\Nov25'
EMPLOYEE_DIR = r'C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'
DAY = '28'
DATE = 'November 28, 2025'

print('=' * 80)
print('DAY 28 TASK EXTRACTION - TST-### ASSIGNMENT')
print('=' * 80)
print(f'Date: {DATE}')
print()

# Load employee status data
print('[STEP 1] Loading employee status data...')
work_employees = []
available_employees = []

work_file = os.path.join(EMPLOYEE_DIR, 'Nov 25 - Employees_Work.md')
if os.path.exists(work_file):
    with open(work_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line and not line.startswith('|---') and 'Employee ID' not in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 2 and parts[2] and parts[2] != 'Employee Name':
                    work_employees.append(parts[2])

avail_file = os.path.join(EMPLOYEE_DIR, 'Nov 25 - Employees_Available.md')
if os.path.exists(avail_file):
    with open(avail_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line and not line.startswith('|---') and 'Employee ID' not in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 2 and parts[2] and parts[2] != 'Employee Name':
                    available_employees.append(parts[2])

print(f'  Work: {len(work_employees)}, Available: {len(available_employees)}')
print()

# Find and filter Day 28 folders
print('[STEP 2] Scanning Day 28 employee folders...')
departments = ['AI Nov25', 'Design Nov25', 'Dev Nov25', 'Fin Nov25',
               'LG Nov25', 'Marketing Nov25', 'SMM Nov25', 'Video Nov25']

import glob

filtered_employees = []
for dept in departments:
    dept_path = os.path.join(BASE_PATH, dept)
    if os.path.exists(dept_path):
        pattern = os.path.join(dept_path, '**', 'Week_4', DAY)
        matches = glob.glob(pattern, recursive=True)
        for match in matches:
            parts = match.split(os.sep)
            employee_name = parts[-3]
            if employee_name in work_employees or employee_name in available_employees:
                status = 'Work' if employee_name in work_employees else 'Available'
                filtered_employees.append({
                    'department': dept.replace(' Nov25', ''),
                    'employee': employee_name,
                    'status': status,
                    'path': match
                })

print(f'  Filtered employees: {len(filtered_employees)}')
print()

# Extract tasks from daily.md files
print('[STEP 3] Extracting tasks from daily.md files...')

# Task status patterns
task_patterns = {
    'completed': r'[-*]\s*\[X\]|[-*]\s*\[x\]|✅|[Cc]ompleted|[Dd]one|[Ff]inished',
    'in_progress': r'🔄|[Ii]n [Pp]rogress|[Ww]orking on|[Cc]ontinuing',
    'new': r'🆕|[-*]\s*\[ \]|[Nn]ew|[Tt]o [Dd]o|[Pp]lanned',
    'blocked': r'⏸️|[Bb]locked|[Ww]aiting|[Pp]aused'
}

all_tasks = []
task_id_counter = 1

for emp in filtered_employees:
    daily_path = os.path.join(emp['path'], 'daily.md')

    if not os.path.exists(daily_path):
        continue

    with open(daily_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Split into lines for task detection
    lines = content.split('\n')

    current_section = 'General'
    current_time = None

    for i, line in enumerate(lines):
        # Detect section headers
        if line.startswith('###'):
            current_section = line.replace('###', '').strip()
            # Extract time if present (e.g., "### 9:00-11:00 - Activity")
            time_match = re.search(r'(\d{1,2}:\d{2}(?:\s*-\s*\d{1,2}:\d{2})?)', current_section)
            if time_match:
                current_time = time_match.group(1)

        # Detect task items (bullets with checkbox or status emoji)
        task_match = re.match(r'^\s*[-*]\s*(\[[ Xx]\])?\s*(.+)$', line)

        if task_match:
            task_text = task_match.group(2).strip()

            # Skip if too short or looks like a header
            if len(task_text) < 10 or task_text.endswith(':'):
                continue

            # Determine task status
            status = 'new'
            for status_type, pattern in task_patterns.items():
                if re.search(pattern, line):
                    status = status_type
                    break

            # Clean task text
            task_text = re.sub(r'[✅🔄🆕⏸️]', '', task_text).strip()
            task_text = re.sub(r'\[X\]|\[x\]|\[ \]', '', task_text).strip()

            # Create task object
            task_id = f'TST-{task_id_counter:03d}'
            task_id_counter += 1

            task = {
                'id': task_id,
                'employee': emp['employee'],
                'department': emp['department'],
                'status': emp['status'],
                'task_status': status,
                'description': task_text,
                'section': current_section,
                'time': current_time,
                'date': DATE
            }

            all_tasks.append(task)

print(f'  Tasks extracted: {len(all_tasks)}')
print()

# Organize tasks by department
print('[STEP 4] Organizing tasks by department...')
by_department = defaultdict(list)
for task in all_tasks:
    by_department[task['department']].append(task)

for dept in sorted(by_department.keys()):
    tasks = by_department[dept]
    completed = sum(1 for t in tasks if t['task_status'] == 'completed')
    in_prog = sum(1 for t in tasks if t['task_status'] == 'in_progress')
    new = sum(1 for t in tasks if t['task_status'] == 'new')
    print(f'  {dept}: {len(tasks)} tasks (Complete: {completed}, In Progress: {in_prog}, New: {new})')
print()

# Generate task extraction report
print('[STEP 5] Generating task extraction report...')

output_file = os.path.join(OUTPUT_DIR, 'Day28_Task_Extraction.md')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Task Extraction Report\n\n')
    f.write(f'**Date:** {DATE}\n')
    f.write(f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    f.write(f'**Total Tasks Extracted:** {len(all_tasks)}\n')
    f.write('\n---\n\n')

    f.write('## Task Summary by Department\n\n')
    f.write('| Department | Total | Completed | In Progress | New | Blocked |\n')
    f.write('|------------|-------|-----------|-------------|-----|----------|\n')

    total_complete = 0
    total_in_prog = 0
    total_new = 0
    total_blocked = 0

    for dept in sorted(by_department.keys()):
        tasks = by_department[dept]
        completed = sum(1 for t in tasks if t['task_status'] == 'completed')
        in_prog = sum(1 for t in tasks if t['task_status'] == 'in_progress')
        new = sum(1 for t in tasks if t['task_status'] == 'new')
        blocked = sum(1 for t in tasks if t['task_status'] == 'blocked')

        total_complete += completed
        total_in_prog += in_prog
        total_new += new
        total_blocked += blocked

        f.write(f'| {dept} | {len(tasks)} | {completed} | {in_prog} | {new} | {blocked} |\n')

    f.write(f'| **TOTAL** | **{len(all_tasks)}** | **{total_complete}** | **{total_in_prog}** | **{total_new}** | **{total_blocked}** |\n')
    f.write('\n---\n\n')

    # Task details by department
    f.write('## Detailed Task List\n\n')

    for dept in sorted(by_department.keys()):
        f.write(f'### {dept} Department\n\n')
        tasks = by_department[dept]

        # Group by employee
        by_employee = defaultdict(list)
        for task in tasks:
            by_employee[task['employee']].append(task)

        for emp_name in sorted(by_employee.keys()):
            emp_tasks = by_employee[emp_name]
            f.write(f'#### {emp_name} ({len(emp_tasks)} tasks)\n\n')

            for task in emp_tasks:
                status_emoji = {
                    'completed': '[DONE]',
                    'in_progress': '[WIP]',
                    'new': '[NEW]',
                    'blocked': '[BLOCKED]'
                }.get(task['task_status'], '[UNKNOWN]')

                f.write(f'- **{task["id"]}** {status_emoji} {task["description"]}\n')
                if task['time']:
                    f.write(f'  - Time: {task["time"]}\n')
                if task['section'] and task['section'] != 'General':
                    f.write(f'  - Section: {task["section"]}\n')

            f.write('\n')

        f.write('---\n\n')

    f.write('## Next Steps\n\n')
    f.write('1. **Project Mapping:** Map TST-### tasks to PRT-001 to PRT-009 projects\n')
    f.write('2. **Milestone Linking:** Link tasks to MLT-### milestones\n')
    f.write('3. **Tool/Guide Association:** Identify TOL-### tools and GDS-### guides used\n')
    f.write('4. **Department Reports:** Generate final reports using PMT-033 to PMT-043\n')
    f.write('5. **Aggregation:** Combine using PMT-032 for cross-department insights\n')

print(f'  Created: Day28_Task_Extraction.md')
print()

# Export tasks to JSON for further processing
json_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks.json')
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(all_tasks, f, indent=2, ensure_ascii=False)

print(f'  Created: Day28_Tasks.json ({len(all_tasks)} tasks)')
print()

print('=' * 80)
print('TASK EXTRACTION COMPLETE')
print('=' * 80)
print(f'Total tasks extracted: {len(all_tasks)}')
print(f'Departments processed: {len(by_department)}')
print(f'Output location: {OUTPUT_DIR}')
print()
print('[SUCCESS] Task extraction completed successfully!')
print('[SUCCESS] Ready for project mapping and final report generation')
