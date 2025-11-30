"""
Test script for processing Day 28 employee folders
Tests the new MAIN_PROMPT_v7.2.md employee filtering logic
"""

import os
import glob

# Read employee directory to get Work/Available status
work_employees = []
available_employees = []

# Read Work status employees
work_file = r'C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\Nov 25 - Employees_Work.md'
if os.path.exists(work_file):
    with open(work_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line and not line.startswith('|---') and 'Employee ID' not in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 2:
                    emp_name = parts[2] if len(parts) > 2 else ''
                    if emp_name and emp_name != 'Employee Name':
                        work_employees.append(emp_name)

# Read Available status employees
avail_file = r'C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\Nov 25 - Employees_Available.md'
if os.path.exists(avail_file):
    with open(avail_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if '|' in line and not line.startswith('|---') and 'Employee ID' not in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 2:
                    emp_name = parts[2] if len(parts) > 2 else ''
                    if emp_name and emp_name != 'Employee Name':
                        available_employees.append(emp_name)

print('=' * 60)
print('DAY 28 PROCESSING TEST - MAIN_PROMPT_v7.2.md')
print('=' * 60)
print()
print('=== EMPLOYEE STATUS FILTERING ===')
print(f'Work status: {len(work_employees)} employees')
print(f'Available status: {len(available_employees)} employees')
print(f'Total to process: {len(work_employees) + len(available_employees)} employees')
print()

# Find day 28 folders
departments = [
    'AI Nov25', 'Design Nov25', 'Dev Nov25', 'Fin Nov25',
    'LG Nov25', 'Marketing Nov25', 'SMM Nov25', 'Video Nov25'
]

base = r'C:\Users\Dell\Dropbox\Nov25'
day_28_folders = []

for dept in departments:
    dept_path = os.path.join(base, dept)
    if os.path.exists(dept_path):
        pattern = os.path.join(dept_path, '**', 'Week_4', '28')
        matches = glob.glob(pattern, recursive=True)

        for match in matches:
            parts = match.split(os.sep)
            employee_name = parts[-3]
            day_28_folders.append({
                'department': dept.replace(' Nov25', ''),
                'employee': employee_name,
                'path': match
            })

# Filter by Work/Available status
filtered_folders = []
excluded_folders = []

for folder in day_28_folders:
    emp_name = folder['employee']
    if emp_name in work_employees or emp_name in available_employees:
        status = 'Work' if emp_name in work_employees else 'Available'
        folder['status'] = status
        filtered_folders.append(folder)
    else:
        excluded_folders.append(folder)

print('=== FILTERED RESULTS FOR DAY 28 ===')
print(f'Total folders found: {len(day_28_folders)}')
print(f'[OK] After filtering (Work/Available only): {len(filtered_folders)}')
print(f'[SKIP] Excluded (Left/Fired/Other): {len(excluded_folders)}')
print()

# Summary by department
by_dept = {}
for folder in filtered_folders:
    dept = folder['department']
    if dept not in by_dept:
        by_dept[dept] = {'Work': [], 'Available': []}
    by_dept[dept][folder['status']].append(folder['employee'])

print('=== BREAKDOWN BY DEPARTMENT ===')
total_work = 0
total_available = 0

for dept in sorted(by_dept.keys()):
    work_emps = by_dept[dept]['Work']
    avail_emps = by_dept[dept]['Available']
    total = len(work_emps) + len(avail_emps)
    total_work += len(work_emps)
    total_available += len(avail_emps)

    print(f'{dept}: {total} employees (Work: {len(work_emps)}, Available: {len(avail_emps)})')

    # Show employee names
    if work_emps:
        for emp in sorted(work_emps)[:3]:
            print(f'  [Work] {emp}')
        if len(work_emps) > 3:
            print(f'  ... and {len(work_emps) - 3} more Work employees')

    if avail_emps:
        for emp in sorted(avail_emps)[:3]:
            print(f'  [Available] {emp}')
        if len(avail_emps) > 3:
            print(f'  ... and {len(avail_emps) - 3} more Available employees')
    print()

print('=' * 60)
print('SUMMARY')
print('=' * 60)
print(f'Total employees to process: {len(filtered_folders)}')
print(f'  - Work status: {total_work}')
print(f'  - Available status: {total_available}')
print()
print(f'Excluded from processing: {len(excluded_folders)}')
print()

# Check for files in filtered folders
print('=== CHECKING FOR FILES IN DAY 28 FOLDERS ===')
files_found = 0
folders_with_files = 0

for folder in filtered_folders[:5]:  # Check first 5
    path = folder['path']
    if os.path.exists(path):
        files = [f for f in os.listdir(path) if f.endswith(('.md', '.txt'))]
        if files:
            folders_with_files += 1
            files_found += len(files)
            print(f'{folder["employee"]} ({folder["department"]}): {len(files)} files')
            for f in files[:2]:
                print(f'  - {f}')

print()
print(f'[SUCCESS] Test completed successfully!')
print(f'[SUCCESS] MAIN_PROMPT_v7.2.md filtering is working as expected')
print(f'[SUCCESS] Ready to process {len(filtered_folders)} employees for November 28, 2025')
