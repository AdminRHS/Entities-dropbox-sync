"""
Generate Proper Task Names

Extract meaningful action-based task names from descriptions
Filter out remaining metadata and time-stamps
"""

import os
import json
import re

# Configuration
INPUT_TASKS = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final_Clean\Day28_Tasks_Clean.json'
OUTPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final_Clean\Day28_Tasks_Final.json'

print('Generating proper task names...\n')

# Load tasks
with open(INPUT_TASKS, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'Loaded {len(tasks)} tasks\n')

# Aggressive metadata/non-task patterns
SKIP_PATTERNS = [
    r'^\*+What',
    r'^\*+Status',
    r'^\*+Time',
    r'^\*+Step',
    r'^\*+Challenge',
    r'^\*+Priority',
    r'^\d{1,2}:\d{2}\s*(AM|PM|am|pm)',  # Time stamps
    r'^\*\*\d{1,2}:\d{2}',  # **HH:MM
    r'^What needs to be done',
    r'^Status:',
    r'^PENDING',
]

# Extract action verb + object for task name
def extract_task_name(description):
    """Extract meaningful task name from description"""

    # Remove markdown formatting
    clean = re.sub(r'\*+', '', description)
    clean = re.sub(r'\[.*?\]', '', clean)
    clean = clean.strip()

    # If description is a sentence, extract verb + object
    words = clean.split()

    # Remove Ukrainian articles and common words
    stop_words = ['the', 'a', 'an', 'to', 'for', 'of', 'in', 'on', 'at', 'with', 'від', 'до', 'на', 'в', 'з', 'для']

    # Get first 5 meaningful words
    meaningful_words = []
    for word in words:
        if word.lower() not in stop_words and len(word) > 2:
            meaningful_words.append(word)
        if len(meaningful_words) >= 5:
            break

    if not meaningful_words:
        return None

    name = ' '.join(meaningful_words)

    # Truncate if too long
    if len(name) > 60:
        name = name[:57] + '...'

    return name

# Process tasks
valid_tasks = []
filtered_count = 0

for task in tasks:
    desc = task['description']

    # Check if should be filtered
    should_filter = False
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, desc, re.IGNORECASE):
            should_filter = True
            print(f'  FILTERED: {desc[:60]}')
            filtered_count += 1
            break

    if should_filter:
        continue

    # Check if too short
    if len(desc.strip()) < 15:
        print(f'  FILTERED (too short): {desc[:60]}')
        filtered_count += 1
        continue

    # Generate proper name
    name = extract_task_name(desc)
    if not name:
        print(f'  FILTERED (no name): {desc[:60]}')
        filtered_count += 1
        continue

    # Update task
    task['name'] = name
    task['description_cleaned'] = desc
    valid_tasks.append(task)

print(f'\n{"-" * 80}')
print(f'Filtered: {filtered_count} non-tasks')
print(f'Valid tasks: {len(valid_tasks)}')
print(f'{"-" * 80}\n')

# Re-assign IDs
for i, task in enumerate(valid_tasks, 1):
    task['id'] = f'TSK-{i:03d}'

# Show sample names
print('Sample task names:\n')
for i, task in enumerate(valid_tasks[:15], 1):
    try:
        print(f'{i:2d}. {task["id"]} - {task["name"]}')
        print(f'    ({task["employee"]} - {task["department"]})')
    except UnicodeEncodeError:
        print(f'{i:2d}. {task["id"]} - [Non-ASCII name]')
        print(f'    ({task["employee"]} - {task["department"]})')

# Save
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(valid_tasks, f, indent=2, ensure_ascii=False)

print(f'\nSaved {len(valid_tasks)} valid tasks to: Day28_Tasks_Final.json')
