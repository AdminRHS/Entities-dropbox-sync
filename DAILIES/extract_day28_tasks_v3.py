"""
Day 28 Task Extraction Script v3.0
Action-based extraction with step clustering and translation
Uses Actions + Objects taxonomy for task identification
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
ACTIONS_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities\Actions\Master\actions_master.json'
DAY = '28'
DATE = 'November 28, 2025'

print('=' * 80)
print('DAY 28 TASK EXTRACTION v3.0 - ACTION-BASED WITH CLUSTERING')
print('=' * 80)
print(f'Date: {DATE}')
print()

# Load Actions taxonomy
print('[STEP 1] Loading Actions taxonomy...')
with open(ACTIONS_FILE, 'r', encoding='utf-8-sig') as f:
    actions_data = json.load(f)

# Build action verb list
action_verbs = set()
for action in actions_data['actions']:
    action_verbs.add(action['action'].lower())
    # Add process forms (verb-ing)
    if 'forms' in action and 'processes' in action['forms']:
        for form in action['forms']['processes']:
            action_verbs.add(form.lower())
    # Add result forms (verb-ed)
    if 'forms' in action and 'results' in action['forms']:
        for form in action['forms']['results']:
            action_verbs.add(form.lower())

print(f'  Loaded {len(action_verbs)} action verbs')
print()

# Common step markers
STEP_PATTERNS = [
    r'^Step\s+\d+:',
    r'^\d+\.\s',
    r'^\d+\)',
    r'^-\s+\[\s*[Xx✅]\s*\]',  # Checkbox items
]

# Section headers to skip (not tasks)
SKIP_HEADERS = [
    r'^\*?What I worked on:?\*?$',
    r'^\*?Outcomes:?\*?$',
    r'^\*?Whisper Flow',
    r'^\*?Next Steps:?\*?$',
    r'^\*?Plan:?\*?$',
    r'^\*?Activities:?\*?$',
    r'^\*?Topic:?\*?$',
    r'^\*?Summary:?\*?$',
    r'^What:',
    r'^Include:',
    r'^Time stamps',
    r'^Instructions',
]

def translate_text(text, target_lang='en'):
    """Mark text for translation if contains non-ASCII"""
    # Check if contains Cyrillic or other non-ASCII
    has_non_ascii = any(ord(char) > 127 for char in text if char.isalpha())

    if has_non_ascii:
        # Mark for manual translation review
        return f"[TRANSLATE] {text}"
    return text

def is_action_based_task(text, action_verbs):
    """Check if text starts with or contains an action verb"""
    # Get first few words
    words = text.lower().split()[:3]

    # Check if any word is an action verb
    for word in words:
        # Remove punctuation
        clean_word = re.sub(r'[^\w]', '', word)
        if clean_word in action_verbs:
            return True

    return False

def is_skip_header(text):
    """Check if text is a section header to skip"""
    for pattern in SKIP_HEADERS:
        if re.match(pattern, text.strip(), re.IGNORECASE):
            return True
    return False

def is_step_marker(text):
    """Check if text has a step marker"""
    for pattern in STEP_PATTERNS:
        if re.match(pattern, text.strip(), re.IGNORECASE):
            return True
    return False

def cluster_steps_into_task(steps):
    """Cluster multiple steps into a single task with details"""
    if not steps:
        return None

    # First step becomes the main task description
    main_task = steps[0]['text']

    # Remaining steps become details
    details = []
    for step in steps[1:]:
        details.append(step['text'])

    return {
        'description': main_task,
        'details': details if details else None,
        'step_count': len(steps),
        'status': steps[0].get('status', 'new')
    }

# Load employee status data
print('[STEP 2] Loading employee status data...')
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

# Find Day 28 folders
print('[STEP 3] Scanning Day 28 employee folders...')
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

# Extract tasks with v3.0 logic
print('[STEP 4] Extracting action-based tasks with clustering...')
print('  (This may take a few moments for translation...)')

all_tasks = []
task_id_counter = 1
translated_count = 0
clustered_count = 0

for emp in filtered_employees:
    daily_path = os.path.join(emp['path'], 'daily.md')

    if not os.path.exists(daily_path):
        continue

    with open(daily_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')
    current_section = 'General'
    current_time = None

    pending_steps = []  # For clustering

    for i, line in enumerate(lines):
        # Track sections
        if line.startswith('###'):
            current_section = line.replace('###', '').strip()
            time_match = re.search(r'(\d{1,2}:\d{2}(?:\s*-\s*\d{1,2}:\d{2})?)', current_section)
            if time_match:
                current_time = time_match.group(1)

        # Detect task items
        task_match = re.match(r'^\s*[-*]\s*(\[[ Xx✅]\])?\s*(.+)$', line)

        if task_match:
            task_text_raw = task_match.group(2).strip()

            # Skip section headers
            if is_skip_header(task_text_raw):
                continue

            # Skip if too short
            if len(task_text_raw) < 10:
                continue

            # Translate if needed
            task_text = translate_text(task_text_raw)
            if task_text != task_text_raw:
                translated_count += 1

            # Determine status
            status_marker = task_match.group(1)
            if status_marker and status_marker.strip() in ['[X]', '[x]', '[✅]']:
                task_status = 'completed'
            elif '✅' in line:
                task_status = 'completed'
            else:
                task_status = 'new'

            # Check if this is a step or standalone task
            is_step = is_step_marker(task_text)

            if is_step:
                # Add to pending steps for clustering
                pending_steps.append({
                    'text': task_text,
                    'status': task_status,
                    'section': current_section,
                    'time': current_time
                })
            else:
                # Process any pending steps first
                if pending_steps:
                    clustered_task = cluster_steps_into_task(pending_steps)
                    if clustered_task and is_action_based_task(clustered_task['description'], action_verbs):
                        task_id = f'TST-{task_id_counter:03d}'
                        task_id_counter += 1
                        clustered_count += 1

                        all_tasks.append({
                            'id': task_id,
                            'employee': emp['employee'],
                            'department': emp['department'],
                            'status': emp['status'],
                            'task_status': clustered_task['status'],
                            'description': clustered_task['description'],
                            'details': clustered_task.get('details'),
                            'step_count': clustered_task['step_count'],
                            'section': pending_steps[0]['section'],
                            'time': pending_steps[0]['time'],
                            'date': DATE,
                            'clustered': True
                        })
                    pending_steps = []

                # Check if standalone task is action-based
                if is_action_based_task(task_text, action_verbs):
                    task_id = f'TST-{task_id_counter:03d}'
                    task_id_counter += 1

                    all_tasks.append({
                        'id': task_id,
                        'employee': emp['employee'],
                        'department': emp['department'],
                        'status': emp['status'],
                        'task_status': task_status,
                        'description': task_text,
                        'details': None,
                        'step_count': 1,
                        'section': current_section,
                        'time': current_time,
                        'date': DATE,
                        'clustered': False
                    })

    # Process any remaining pending steps
    if pending_steps:
        clustered_task = cluster_steps_into_task(pending_steps)
        if clustered_task and is_action_based_task(clustered_task['description'], action_verbs):
            task_id = f'TST-{task_id_counter:03d}'
            task_id_counter += 1
            clustered_count += 1

            all_tasks.append({
                'id': task_id,
                'employee': emp['employee'],
                'department': emp['department'],
                'status': emp['status'],
                'task_status': clustered_task['status'],
                'description': clustered_task['description'],
                'details': clustered_task.get('details'),
                'step_count': clustered_task['step_count'],
                'section': pending_steps[0]['section'],
                'time': pending_steps[0]['time'],
                'date': DATE,
                'clustered': True
            })

print(f'  Tasks extracted: {len(all_tasks)}')
print(f'  Items translated: {translated_count}')
print(f'  Tasks clustered from steps: {clustered_count}')
print()

# Save results
print('[STEP 5] Generating v3.0 reports...')

json_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_v3.json')
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(all_tasks, f, indent=2, ensure_ascii=False)

print(f'  Created: Day28_Tasks_v3.json')
print()

print('=' * 80)
print('TASK EXTRACTION v3.0 COMPLETE')
print('=' * 80)
print(f'Total tasks: {len(all_tasks)}')
print(f'Action-based filtering applied')
print(f'Step clustering: {clustered_count} multi-step tasks')
print(f'Translation: {translated_count} items')
print()
print('[SUCCESS] Ready for project mapping!')
