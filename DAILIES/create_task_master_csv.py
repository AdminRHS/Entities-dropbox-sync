"""
Create Day 28 Task Master CSV for Review
Generates a comprehensive CSV with all 681 tasks for validation
"""

import json
import csv
import re

# Load tasks
tasks_file = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_With_Projects.json'
output_csv = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Task_Master_Review.csv'

with open(tasks_file, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'Loaded {len(tasks)} tasks')

# Function to create short task name from description
def create_task_name(description, max_length=60):
    """Create a concise task name from description"""
    # Remove markdown formatting
    clean = re.sub(r'\*\*|\*|`', '', description)

    # Remove special prefixes
    clean = re.sub(r'^\*[^*]+\*\*:\s*', '', clean)

    # Clean up
    clean = clean.strip()

    # Truncate if too long
    if len(clean) > max_length:
        clean = clean[:max_length] + '...'

    # If empty, use first few words
    if not clean or len(clean) < 5:
        words = description.split()[:5]
        clean = ' '.join(words)
        if len(clean) > max_length:
            clean = clean[:max_length] + '...'

    return clean

# Create CSV
with open(output_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    # Header
    writer.writerow([
        'Task_ID',
        'Task_Name',
        'Employee',
        'Department',
        'Employee_Status',
        'Task_Status',
        'Project',
        'Section',
        'Time',
        'Date',
        'Description_Full'
    ])

    # Write all tasks
    for task in tasks:
        task_name = create_task_name(task['description'])

        writer.writerow([
            task['id'],
            task_name,
            task['employee'],
            task['department'],
            task['status'],
            task['task_status'],
            task['project'],
            task['section'],
            task.get('time', ''),
            task['date'],
            task['description']
        ])

print(f'Created: {output_csv}')
print(f'Total rows: {len(tasks) + 1} (including header)')
print('')
print('CSV Columns:')
print('  1. Task_ID - TST-### identifier')
print('  2. Task_Name - Short descriptive name')
print('  3. Employee - Employee name')
print('  4. Department - AI/Design/Dev/Fin/LG')
print('  5. Employee_Status - Work/Available')
print('  6. Task_Status - completed/in_progress/new/blocked')
print('  7. Project - PRT-### mapped project')
print('  8. Section - Section from daily.md')
print('  9. Time - Time stamp if available')
print(' 10. Date - November 28, 2025')
print(' 11. Description_Full - Complete task description')
print('')
print('[SUCCESS] CSV ready for review and validation')
