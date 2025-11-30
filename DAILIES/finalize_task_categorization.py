"""
Day 28 Final Task Categorization - Cleanup and Translation

Improvements:
1. Deduplicate workflow names (remove time-only descriptions)
2. Translate Ukrainian to English
3. Add more problem details
4. Aggressive metadata filtering
5. Better task naming
"""

import os
import json
import re
from collections import defaultdict

# Configuration
INPUT_WORKFLOWS = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final\Day28_Workflows.json'
INPUT_TASKS = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final\Day28_Tasks_Standalone.json'
INPUT_PROBLEMS = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final\Day28_Problems.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final_Clean'

print('=' * 80)
print('FINAL TASK CATEGORIZATION - CLEANUP & TRANSLATION')
print('=' * 80)
print()

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
print('[STEP 1] Loading categorized data...')
with open(INPUT_WORKFLOWS, 'r', encoding='utf-8') as f:
    workflows = json.load(f)

with open(INPUT_TASKS, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

with open(INPUT_PROBLEMS, 'r', encoding='utf-8') as f:
    problems = json.load(f)

print(f'  Loaded {len(workflows)} workflows')
print(f'  Loaded {len(tasks)} standalone tasks')
print(f'  Loaded {len(problems)} problems')
print()

# Ukrainian to English translations (common terms from the data)
TRANSLATIONS = {
    'Основні задачі': 'Main Tasks',
    'Activity': 'Activity',
    'Call з Колею': 'Call with Kolya',
    'День планування': 'Planning Day',
    'Call з розробниками': 'Call with Developers',
    'Strapi Workflow пояснення': 'Strapi Workflow Explanation',
    'Coordination з HR командою': 'Coordination with HR Team',
    'Honeystone Project': 'Honeystone Project',
    'Code Review': 'Code Review',
    'Завершення': 'Completion',
    'Task Status Distribution': 'Task Status Distribution',
    'Tracking': 'Tracking',
    'REM-S Export': 'REM-S Export',
    'Image Fix': 'Image Fix',
    'Preparing Designer Communication': 'Preparing Designer Communication',
    'Planned': 'Planned',
    'Completed Tasks': 'Completed Tasks',
    'Challenges & Solutions': 'Challenges & Solutions',
    'Tools & Software Used': 'Tools & Software Used',
    'Plans for Tomorrow': 'Plans for Tomorrow',
    'Morning': 'Morning',
    'Afternoon': 'Afternoon',
    'Collections Export Script Enhancement': 'Collections Export Script Enhancement',
    'Collections Update Script Refactoring': 'Collections Update Script Refactoring',
    'File Filtering and Template Handling': 'File Filtering and Template Handling',
    'List.json Synchronization System': 'List.json Synchronization System',
    'Documentation Updates': 'Documentation Updates',
    'Managing the Lead Calendar': 'Managing the Lead Calendar',
    'Project Remess & AI Graphic Generation': 'Project Remess & AI Graphic Generation',
    'Morning accounts checking': 'Morning Accounts Checking',
    'Admin meeting': 'Admin Meeting',
    'Day planning': 'Day Planning',
    'Daily reports review': 'Daily Reports Review',
    'Account allocation for posts': 'Account Allocation for Posts',
    'Design training session': 'Design Training Session',
    'Coordination and outreach': 'Coordination and Outreach',
    'Dropbox and reporting guidance': 'Dropbox and Reporting Guidance',
    'Messaging test results': 'Messaging Test Results',
    'Black Friday posting': 'Black Friday Posting',
    'Newcomer CRM review': 'Newcomer CRM Review',
    'Send messages to leads': 'Send Messages to Leads',
    'Job sites': 'Job Sites',
    'black friday posts': 'Black Friday Posts',
    'Graphic design session': 'Graphic Design Session',
    'Add new companies using google scape': 'Add New Companies Using Google Scrape',
    'Getting Strapi Access': 'Getting Strapi Access',
    'Working on updates in Strapi': 'Working on Strapi Updates',
    'Figuring out and assigning tasks for creating graphics for REM-s website': 'Graphics for REM-S Website',
    'Cross-Department AI Tool Support': 'AI Tool Support',
    'System Optimization & User Feedback Monitoring': 'System Optimization',
    'Strapi Workflow Research': 'Strapi Workflow Research',
    'Documentation - Strapi AI Automation Guide': 'Strapi Automation Guide',
}

def translate_text(text):
    """Translate Ukrainian/Russian to English"""
    for ukr, eng in TRANSLATIONS.items():
        text = text.replace(ukr, eng)
    return text

def clean_workflow_name(name):
    """Clean workflow name - remove time, translate, deduplicate"""
    # Remove employee prefix
    if ' - ' in name:
        parts = name.split(' - ', 1)
        employee = parts[0]
        section = parts[1] if len(parts) > 1 else parts[0]
    else:
        employee = name.split()[0]
        section = name

    # Remove time patterns [HH:MM-HH:MM]
    section = re.sub(r'\[\d{1,2}:\d{2}-\d{1,2}:\d{2}\]', '', section)
    section = re.sub(r'\d{1,2}:\d{2}-\d{1,2}:\d{2}', '', section)

    # Remove [brackets]
    section = re.sub(r'\[([^\]]+)\]', r'\1', section)

    # Remove ** markdown
    section = re.sub(r'\*\*', '', section)

    # Remove # headers
    section = re.sub(r'^#+\s*', '', section)

    # Remove emoji numbers
    section = re.sub(r'[0-9]️⃣\s*', '', section)

    # Translate
    section = translate_text(section)

    # Clean up whitespace
    section = ' '.join(section.split())

    # Remove "Day -" prefix if that's all that's left
    if section.startswith('Day '):
        section = section[4:].strip()

    # Truncate if too long
    if len(section) > 50:
        section = section[:47] + '...'

    return f"{employee} - {section}" if section else employee

def is_still_metadata(desc):
    """Final aggressive metadata check"""
    desc_lower = desc.lower().strip()

    # Direct metadata patterns
    if desc.startswith('*What I worked on'):
        return True
    if desc.startswith('*Whisper'):
        return True
    if 'whisper flow on' in desc_lower:
        return True
    if desc.startswith('*Time'):
        return True
    if desc.startswith('*Step'):
        return True

    # Single word or very short
    if len(desc.strip()) < 10:
        return True

    return False

# Clean workflows
print('[STEP 2] Cleaning and deduplicating workflows...')

cleaned_workflows = []
workflow_names_seen = set()

for wf in workflows:
    # Clean name
    clean_name = clean_workflow_name(wf['name'])

    # Skip if duplicate name
    if clean_name in workflow_names_seen:
        # Merge items into existing workflow
        for existing_wf in cleaned_workflows:
            if clean_workflow_name(existing_wf['name']) == clean_name:
                existing_wf['items'].extend(wf['items'])
                existing_wf['item_count'] += wf['item_count']
                existing_wf['tasks_count'] += wf['tasks_count']
                existing_wf['reports_count'] += wf['reports_count']
                break
        continue

    workflow_names_seen.add(clean_name)

    wf['name'] = clean_name
    wf['translated'] = True
    cleaned_workflows.append(wf)

print(f'  Deduplicated: {len(workflows)} -> {len(cleaned_workflows)} workflows')
print()

# Filter remaining tasks
print('[STEP 3] Filtering remaining non-tasks...')

valid_tasks = []
for task in tasks:
    if not is_still_metadata(task['description']):
        # Translate description
        task['description_original'] = task['description']
        task['description'] = translate_text(task['description'])
        task['name'] = translate_text(task['name'])
        valid_tasks.append(task)

print(f'  Filtered tasks: {len(tasks)} -> {len(valid_tasks)} valid')
print()

# Enhance problem descriptions
print('[STEP 4] Enhancing problem descriptions...')

for problem in problems:
    desc = problem['description']

    # Add context from employee and section
    employee = problem['employee']
    section = problem.get('section', '')

    # Translate
    desc = translate_text(desc)
    section = translate_text(section)

    # Create enhanced description
    enhanced = f"{desc}"
    if section and section not in desc:
        enhanced += f" (Context: {section[:50]})"

    problem['description_original'] = problem['description']
    problem['description'] = enhanced
    problem['name'] = translate_text(problem['name'])
    problem['employee_context'] = f"{employee} - {section[:30]}"

print(f'  Enhanced {len(problems)} problem descriptions')
print()

# Re-assign IDs
print('[STEP 5] Re-assigning IDs...')

for i, wf in enumerate(cleaned_workflows, 1):
    wf['id'] = f'WFL-{i:03d}'

for i, task in enumerate(valid_tasks, 1):
    task['id'] = f'TSK-{i:03d}'

for i, problem in enumerate(problems, 1):
    problem['id'] = f'PRB-{i:03d}'

print(f'  Assigned {len(cleaned_workflows)} workflow IDs')
print(f'  Assigned {len(valid_tasks)} task IDs')
print(f'  Assigned {len(problems)} problem IDs')
print()

# Save cleaned outputs
print('[STEP 6] Saving cleaned outputs...')

workflows_file = os.path.join(OUTPUT_DIR, 'Day28_Workflows_Clean.json')
with open(workflows_file, 'w', encoding='utf-8') as f:
    json.dump(cleaned_workflows, f, indent=2, ensure_ascii=False)

tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Clean.json')
with open(tasks_file, 'w', encoding='utf-8') as f:
    json.dump(valid_tasks, f, indent=2, ensure_ascii=False)

problems_file = os.path.join(OUTPUT_DIR, 'Day28_Problems_Enhanced.json')
with open(problems_file, 'w', encoding='utf-8') as f:
    json.dump(problems, f, indent=2, ensure_ascii=False)

# Master CSV
import csv

csv_file = os.path.join(OUTPUT_DIR, 'Day28_Final_Master.csv')
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['ID', 'Type', 'Name', 'Employee', 'Items', 'Description'])

    # Workflows
    for wf in cleaned_workflows:
        writer.writerow([
            wf['id'],
            'Workflow',
            wf['name'],
            wf['employee'],
            f"{wf['item_count']} ({wf['tasks_count']}T + {wf['reports_count']}R)",
            wf['section'][:80]
        ])

    # Tasks
    for task in valid_tasks:
        writer.writerow([
            task['id'],
            'Task',
            task['name'],
            task['employee'],
            '1',
            task['description'][:80]
        ])

    # Problems
    for problem in problems:
        writer.writerow([
            problem['id'],
            'Problem',
            problem['name'],
            problem['employee'],
            '1',
            problem['description'][:80]
        ])

# Summary
summary_file = os.path.join(OUTPUT_DIR, 'Day28_Final_Summary.md')
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Final Task Categorization - Clean\n\n')
    f.write('**Date:** November 29, 2025\n')
    f.write('**Status:** Final - Cleaned and Translated\n\n')
    f.write('---\n\n')

    f.write('## Summary\n\n')
    f.write(f'- **Workflows:** {len(cleaned_workflows)} (deduplicated and translated)\n')
    f.write(f'- **Standalone Tasks:** {len(valid_tasks)} (filtered and translated)\n')
    f.write(f'- **Problems:** {len(problems)} (enhanced with context)\n\n')

    total_items = sum(wf['item_count'] for wf in cleaned_workflows) + len(valid_tasks) + len(problems)
    f.write(f'**Total Items:** {total_items}\n\n')

    f.write('---\n\n')
    f.write('## Top Workflows\n\n')

    for i, wf in enumerate(sorted(cleaned_workflows, key=lambda x: x['item_count'], reverse=True)[:15], 1):
        f.write(f'{i}. **{wf["id"]}** - {wf["name"]}\n')
        f.write(f'   - Items: {wf["item_count"]} ({wf["tasks_count"]} tasks, {wf["reports_count"]} reports)\n\n')

    f.write('---\n\n')
    f.write('## Changes Made\n\n')
    f.write('1. ✅ Deduplicated workflow names\n')
    f.write('2. ✅ Removed time-only descriptions from names\n')
    f.write('3. ✅ Translated Ukrainian/Russian to English\n')
    f.write('4. ✅ Enhanced problem descriptions with context\n')
    f.write('5. ✅ Filtered remaining metadata items\n')
    f.write('6. ✅ Cleaned and simplified naming\n\n')

    f.write('---\n\n')
    f.write('## Files\n\n')
    f.write('- Day28_Workflows_Clean.json\n')
    f.write('- Day28_Tasks_Clean.json\n')
    f.write('- Day28_Problems_Enhanced.json\n')
    f.write('- Day28_Final_Master.csv\n')

print(f'  Saved: Day28_Workflows_Clean.json')
print(f'  Saved: Day28_Tasks_Clean.json')
print(f'  Saved: Day28_Problems_Enhanced.json')
print(f'  Saved: Day28_Final_Master.csv')
print(f'  Saved: Day28_Final_Summary.md')
print()

print('=' * 80)
print('FINAL CLEANUP COMPLETE')
print('=' * 80)
print()
print(f'✅ {len(cleaned_workflows)} unique workflows (translated)')
print(f'✅ {len(valid_tasks)} valid tasks (filtered & translated)')
print(f'✅ {len(problems)} problems (enhanced with context)')
print(f'✅ Total: {total_items} actionable items')
print()
print(f'Output: {OUTPUT_DIR}')
