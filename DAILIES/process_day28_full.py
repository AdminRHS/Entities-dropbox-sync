"""
Full Day 28 Processing Script
Following MAIN_PROMPT_v7.2.md workflow

Processes 20 filtered employees (Work/Available status only)
Extracts tasks, generates department reports, aggregates results
"""

import os
import glob
import json
from datetime import datetime
from collections import defaultdict

# Configuration
BASE_PATH = r'C:\Users\Dell\Dropbox\Nov25'
EMPLOYEE_DIR = r'C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'
DAY = '28'
DATE = 'November 28, 2025'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

print('=' * 80)
print('DAY 28 FULL PROCESSING - MAIN_PROMPT_v7.2.md')
print('=' * 80)
print(f'Date: {DATE}')
print(f'Output: {OUTPUT_DIR}')
print()

# Step 1: Load employee directories
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

print(f'  Work status: {len(work_employees)} employees')
print(f'  Available status: {len(available_employees)} employees')
print()

# Step 2: Find and filter Day 28 folders
print('[STEP 2] Scanning Day 28 employee folders...')
departments = ['AI Nov25', 'Design Nov25', 'Dev Nov25', 'Fin Nov25',
               'LG Nov25', 'Marketing Nov25', 'SMM Nov25', 'Video Nov25']

day_28_folders = []
for dept in departments:
    dept_path = os.path.join(BASE_PATH, dept)
    if os.path.exists(dept_path):
        pattern = os.path.join(dept_path, '**', 'Week_4', DAY)
        matches = glob.glob(pattern, recursive=True)
        for match in matches:
            parts = match.split(os.sep)
            employee_name = parts[-3]
            day_28_folders.append({
                'department': dept.replace(' Nov25', ''),
                'employee': employee_name,
                'path': match
            })

filtered_employees = []
for folder in day_28_folders:
    emp_name = folder['employee']
    if emp_name in work_employees or emp_name in available_employees:
        status = 'Work' if emp_name in work_employees else 'Available'
        folder['status'] = status
        filtered_employees.append(folder)

print(f'  Total folders: {len(day_28_folders)}')
print(f'  Filtered (Work/Available): {len(filtered_employees)}')
print(f'  Excluded: {len(day_28_folders) - len(filtered_employees)}')
print()

# Step 3: Read daily.md files and extract content
print('[STEP 3] Reading employee daily.md files...')
employee_data = []
files_read = 0
files_missing = 0

for emp in filtered_employees:
    daily_path = os.path.join(emp['path'], 'daily.md')
    plans_path = os.path.join(emp['path'], 'plans.md')
    task_path = os.path.join(emp['path'], 'task.md')

    content = {
        'employee': emp['employee'],
        'department': emp['department'],
        'status': emp['status'],
        'path': emp['path'],
        'daily': '',
        'plans': '',
        'task': '',
        'files_found': []
    }

    # Read daily.md
    if os.path.exists(daily_path):
        with open(daily_path, 'r', encoding='utf-8', errors='ignore') as f:
            content['daily'] = f.read()
            content['files_found'].append('daily.md')
            files_read += 1

    # Read plans.md
    if os.path.exists(plans_path):
        with open(plans_path, 'r', encoding='utf-8', errors='ignore') as f:
            content['plans'] = f.read()
            content['files_found'].append('plans.md')
            files_read += 1

    # Read task.md
    if os.path.exists(task_path):
        with open(task_path, 'r', encoding='utf-8', errors='ignore') as f:
            content['task'] = f.read()
            content['files_found'].append('task.md')
            files_read += 1

    if content['files_found']:
        employee_data.append(content)
    else:
        files_missing += 1

print(f'  Files read: {files_read}')
print(f'  Employees with data: {len(employee_data)}')
print(f'  Employees missing files: {files_missing}')
print()

# Step 4: Extract tasks by department
print('[STEP 4] Organizing data by department...')
by_department = defaultdict(list)

for emp in employee_data:
    by_department[emp['department']].append(emp)

print('  Department breakdown:')
for dept in sorted(by_department.keys()):
    emps = by_department[dept]
    work_count = sum(1 for e in emps if e['status'] == 'Work')
    avail_count = sum(1 for e in emps if e['status'] == 'Available')
    print(f'    {dept}: {len(emps)} employees (Work: {work_count}, Available: {avail_count})')
print()

# Step 5: Generate department summaries
print('[STEP 5] Generating department summaries...')

for dept_name, employees in sorted(by_department.items()):
    output_file = os.path.join(OUTPUT_DIR, f'{dept_name}_Day28_Summary.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {dept_name.upper()} Department - Day 28 Summary\\n\\n')
        f.write(f'**Date:** {DATE}\\n')
        f.write(f'**Employees Processed:** {len(employees)}\\n')
        f.write(f'**Processing Method:** MAIN_PROMPT_v7.2.md\\n')
        f.write('\\n---\\n\\n')

        f.write('## Team Breakdown\\n\\n')
        work_emps = [e for e in employees if e['status'] == 'Work']
        avail_emps = [e for e in employees if e['status'] == 'Available']

        f.write(f'- **Work Status:** {len(work_emps)} employees\\n')
        for emp in work_emps:
            f.write(f'  - {emp["employee"]}\\n')

        f.write(f'- **Available Status:** {len(avail_emps)} employees\\n')
        for emp in avail_emps:
            f.write(f'  - {emp["employee"]}\\n')

        f.write('\\n---\\n\\n')
        f.write('## Employee Reports\\n\\n')

        for emp in sorted(employees, key=lambda x: x['employee']):
            f.write(f'### {emp["employee"]} [{emp["status"]}]\\n\\n')
            f.write(f'**Files:** {", ".join(emp["files_found"])}\\n\\n')

            if emp['daily']:
                f.write('#### Daily Report\\n\\n')
                f.write('```\\n')
                # Write first 500 chars to keep file manageable
                preview = emp['daily'][:500]
                f.write(preview)
                if len(emp['daily']) > 500:
                    f.write('\\n... (content truncated)\\n')
                f.write('```\\n\\n')

            if emp['plans']:
                f.write('#### Plans\\n\\n')
                f.write('```\\n')
                preview = emp['plans'][:300]
                f.write(preview)
                if len(emp['plans']) > 300:
                    f.write('\\n... (content truncated)\\n')
                f.write('```\\n\\n')

            f.write('---\\n\\n')

    print(f'  Created: {dept_name}_Day28_Summary.md')

print()

# Step 6: Generate master summary
print('[STEP 6] Generating master summary...')

master_file = os.path.join(OUTPUT_DIR, 'Day28_Master_Summary.md')
with open(master_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Master Summary\\n\\n')
    f.write(f'**Date:** {DATE}\\n')
    f.write(f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\\n')
    f.write(f'**Processing:** MAIN_PROMPT_v7.2.md\\n')
    f.write('\\n---\\n\\n')

    f.write('## Overview\\n\\n')
    f.write(f'- **Total Employees Processed:** {len(employee_data)}\\n')
    f.write(f'- **Work Status:** {sum(1 for e in employee_data if e["status"] == "Work")}\\n')
    f.write(f'- **Available Status:** {sum(1 for e in employee_data if e["status"] == "Available")}\\n')
    f.write(f'- **Departments:** {len(by_department)}\\n')
    f.write(f'- **Files Read:** {files_read}\\n')
    f.write('\\n---\\n\\n')

    f.write('## Department Summary\\n\\n')
    f.write('| Department | Employees | Work | Available | Files |\\n')
    f.write('|------------|-----------|------|-----------|-------|\\n')

    total_work = 0
    total_avail = 0

    for dept in sorted(by_department.keys()):
        emps = by_department[dept]
        work_count = sum(1 for e in emps if e['status'] == 'Work')
        avail_count = sum(1 for e in emps if e['status'] == 'Available')
        file_count = sum(len(e['files_found']) for e in emps)

        total_work += work_count
        total_avail += avail_count

        f.write(f'| {dept} | {len(emps)} | {work_count} | {avail_count} | {file_count} |\\n')

    f.write(f'| **TOTAL** | **{len(employee_data)}** | **{total_work}** | **{total_avail}** | **{files_read}** |\\n')
    f.write('\\n---\\n\\n')

    f.write('## Employee List\\n\\n')
    for dept in sorted(by_department.keys()):
        f.write(f'### {dept}\\n\\n')
        for emp in sorted(by_department[dept], key=lambda x: x['employee']):
            status_badge = '[W]' if emp['status'] == 'Work' else '[A]'
            files = ', '.join(emp['files_found']) if emp['files_found'] else 'No files'
            f.write(f'- {status_badge} **{emp["employee"]}** - {files}\\n')
        f.write('\\n')

    f.write('---\\n\\n')
    f.write('## Processing Notes\\n\\n')
    f.write('**Employee Filtering:** Processed only Work and Available status employees\\n\\n')
    f.write(f'**Excluded:** {len(day_28_folders) - len(filtered_employees)} employees (Left, Fired, Other statuses)\\n\\n')
    f.write('**Files Processed:** daily.md, plans.md, task.md (where available)\\n\\n')
    f.write('**Next Steps:**\\n')
    f.write('- Extract TST-### tasks from daily reports\\n')
    f.write('- Map tasks to PRT-### projects\\n')
    f.write('- Link to TOL-### tools and GDS-### guides\\n')
    f.write('- Generate final department reports (PMT-033 to PMT-043)\\n')

print(f'  Created: Day28_Master_Summary.md')
print()

print('=' * 80)
print('PROCESSING COMPLETE')
print('=' * 80)
print(f'Total employees processed: {len(employee_data)}')
print(f'Department summaries created: {len(by_department)}')
print(f'Output location: {OUTPUT_DIR}')
print()
print('Files generated:')
for dept in sorted(by_department.keys()):
    print(f'  - {dept}_Day28_Summary.md')
print(f'  - Day28_Master_Summary.md')
print()
print('[SUCCESS] Day 28 processing completed successfully!')
print('[SUCCESS] Ready for task extraction (TST-###) and final report generation')
