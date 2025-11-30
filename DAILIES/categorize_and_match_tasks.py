"""
Day 28 Task Categorization & Matching v4.0

Features:
1. Separate tasks from problems
2. Rename TST-### to TSK-### (extracted tasks)
3. Match against TST-### task templates
4. Sort matched vs unmatched
"""

import os
import json
import re
from collections import defaultdict
import glob

# Configuration
TASK_TEMPLATES_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-003_Task_Templates'
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_v2.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'

print('=' * 80)
print('DAY 28 TASK CATEGORIZATION & MATCHING v4.0')
print('=' * 80)
print()

# Load task templates
print('[STEP 1] Loading Task Manager templates...')
task_templates = {}

# Find all TST-*.json files
pattern = os.path.join(TASK_TEMPLATES_DIR, '**', 'TST-*.json')
template_files = glob.glob(pattern, recursive=True)

for template_file in template_files:
    try:
        with open(template_file, 'r', encoding='utf-8-sig') as f:
            template_data = json.load(f)

            # Extract TST-### from filename
            filename = os.path.basename(template_file)
            tst_match = re.match(r'(TST-\d+)', filename)
            if tst_match:
                tst_id = tst_match.group(1)
                task_templates[tst_id] = {
                    'id': tst_id,
                    'file': template_file,
                    'name': template_data.get('task_name', filename),
                    'description': template_data.get('description', ''),
                    'action': template_data.get('action', ''),
                    'object': template_data.get('object', '')
                }
    except Exception as e:
        pass  # Skip files that can't be parsed

print(f'  Loaded {len(task_templates)} task templates (TST-001 to TST-{max([int(k.split("-")[1]) for k in task_templates.keys()]):03d})')
print()

# Load extracted tasks
print('[STEP 2] Loading extracted tasks from v2.0...')
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    extracted_tasks = json.load(f)

print(f'  Loaded {len(extracted_tasks)} extracted tasks')
print()

# Categorize: Tasks vs Problems
print('[STEP 3] Categorizing tasks vs problems...')

tasks = []
problems = []

# Problem indicators
PROBLEM_KEYWORDS = [
    'error', 'bug', 'issue', 'problem', 'broken', 'not working',
    'failed', 'fail', 'crash', 'помилка', 'проблема', 'не працює',
    'fix', 'repair', 'troubleshoot', 'debug'
]

for item in extracted_tasks:
    desc_lower = item['description'].lower()

    # Check if it's a problem
    is_problem = any(keyword in desc_lower for keyword in PROBLEM_KEYWORDS)

    # Check if status indicates problem
    if 'blocked' in item.get('task_status', ''):
        is_problem = True

    if is_problem:
        problems.append(item)
    else:
        tasks.append(item)

print(f'  Tasks: {len(tasks)}')
print(f'  Problems: {len(problems)}')
print()

# Rename IDs: TST-### → TSK-### for extracted tasks
print('[STEP 4] Renaming task IDs (TST -> TSK)...')

for i, task in enumerate(tasks, 1):
    task['original_id'] = task['id']  # Keep original
    task['id'] = f'TSK-{i:03d}'  # Rename to TSK

for i, problem in enumerate(problems, 1):
    problem['original_id'] = problem['id']
    problem['id'] = f'PRB-{i:03d}'  # Problems get PRB-###

print(f'  Renamed {len(tasks)} tasks to TSK-###')
print(f'  Renamed {len(problems)} problems to PRB-###')
print()

# Match tasks to templates
print('[STEP 5] Matching tasks to Task Manager templates...')

matched_tasks = []
unmatched_tasks = []

def match_task_to_template(task_desc, templates):
    """Find best matching template for a task"""
    best_match = None
    best_score = 0

    desc_lower = task_desc.lower()
    desc_words = set(re.findall(r'\w+', desc_lower))

    for tst_id, template in templates.items():
        # Build template word set
        template_text = f"{template['name']} {template['description']} {template.get('action', '')} {template.get('object', '')}"
        template_words = set(re.findall(r'\w+', template_text.lower()))

        # Calculate overlap
        common_words = desc_words & template_words
        if len(common_words) > 0:
            # Weighted score: more common words = better match
            score = len(common_words) / max(len(desc_words), 1)

            if score > best_score and score > 0.2:  # At least 20% overlap
                best_score = score
                best_match = {
                    'template_id': tst_id,
                    'template_name': template['name'],
                    'match_score': round(score * 100, 1)
                }

    return best_match

for task in tasks:
    match = match_task_to_template(task['description'], task_templates)

    if match:
        task['template_match'] = match
        matched_tasks.append(task)
    else:
        task['template_match'] = None
        unmatched_tasks.append(task)

print(f'  Matched to templates: {len(matched_tasks)} ({len(matched_tasks)/len(tasks)*100:.1f}%)')
print(f'  Unmatched (new tasks): {len(unmatched_tasks)} ({len(unmatched_tasks)/len(tasks)*100:.1f}%)')
print()

# Generate reports
print('[STEP 6] Generating categorization reports...')

# Report 1: Matched Tasks
matched_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Matched.json')
with open(matched_file, 'w', encoding='utf-8') as f:
    json.dump(matched_tasks, f, indent=2, ensure_ascii=False)

# Report 2: Unmatched Tasks
unmatched_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Unmatched.json')
with open(unmatched_file, 'w', encoding='utf-8') as f:
    json.dump(unmatched_tasks, f, indent=2, ensure_ascii=False)

# Report 3: Problems
problems_file = os.path.join(OUTPUT_DIR, 'Day28_Problems.json')
with open(problems_file, 'w', encoding='utf-8') as f:
    json.dump(problems, f, indent=2, ensure_ascii=False)

# Report 4: Master CSV with new IDs
import csv

csv_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Categorized.csv')
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow([
        'New_ID',
        'Original_ID',
        'Category',
        'Task_Name',
        'Employee',
        'Department',
        'Status',
        'Template_Match',
        'Match_Score',
        'Description'
    ])

    # Write tasks
    for task in matched_tasks:
        match = task['template_match']
        writer.writerow([
            task['id'],
            task['original_id'],
            'Task (Matched)',
            task['description'][:60] + '...' if len(task['description']) > 60 else task['description'],
            task['employee'],
            task['department'],
            task['task_status'],
            match['template_id'],
            f"{match['match_score']}%",
            task['description']
        ])

    for task in unmatched_tasks:
        writer.writerow([
            task['id'],
            task['original_id'],
            'Task (New)',
            task['description'][:60] + '...' if len(task['description']) > 60 else task['description'],
            task['employee'],
            task['department'],
            task['task_status'],
            'N/A',
            '0%',
            task['description']
        ])

    # Write problems
    for problem in problems:
        writer.writerow([
            problem['id'],
            problem['original_id'],
            'Problem',
            problem['description'][:60] + '...' if len(problem['description']) > 60 else problem['description'],
            problem['employee'],
            problem['department'],
            problem.get('task_status', 'new'),
            'N/A',
            'N/A',
            problem['description']
        ])

# Report 5: Summary Markdown
summary_file = os.path.join(OUTPUT_DIR, 'Day28_Categorization_Summary.md')
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Task Categorization & Matching Summary\n\n')
    f.write(f'**Date:** November 28, 2025\n')
    f.write(f'**Total Items Processed:** {len(extracted_tasks)}\n\n')
    f.write('---\n\n')

    f.write('## Categorization Results\n\n')
    f.write('| Category | Count | % | ID Range | File |\n')
    f.write('|----------|-------|---|----------|------|\n')
    f.write(f'| Tasks (Matched) | {len(matched_tasks)} | {len(matched_tasks)/len(extracted_tasks)*100:.1f}% | TSK-001 to TSK-{len(matched_tasks):03d} | Day28_Tasks_Matched.json |\n')
    f.write(f'| Tasks (Unmatched) | {len(unmatched_tasks)} | {len(unmatched_tasks)/len(extracted_tasks)*100:.1f}% | TSK-{len(matched_tasks)+1:03d} to TSK-{len(tasks):03d} | Day28_Tasks_Unmatched.json |\n')
    f.write(f'| Problems | {len(problems)} | {len(problems)/len(extracted_tasks)*100:.1f}% | PRB-001 to PRB-{len(problems):03d} | Day28_Problems.json |\n')
    f.write(f'| **TOTAL** | **{len(extracted_tasks)}** | **100%** | | |\n\n')

    f.write('---\n\n')

    f.write('## Template Match Statistics\n\n')

    # Group matched tasks by template
    by_template = defaultdict(list)
    for task in matched_tasks:
        template_id = task['template_match']['template_id']
        by_template[template_id].append(task)

    f.write(f'**Templates Matched:** {len(by_template)} of {len(task_templates)} total\n')
    f.write(f'**Match Rate:** {len(matched_tasks)/len(tasks)*100:.1f}%\n\n')

    f.write('### Top Matched Templates\n\n')
    sorted_templates = sorted(by_template.items(), key=lambda x: len(x[1]), reverse=True)[:10]

    f.write('| Template | Name | Matches |\n')
    f.write('|----------|------|----------|\n')
    for template_id, task_list in sorted_templates:
        template_name = task_templates[template_id]['name']
        f.write(f'| {template_id} | {template_name} | {len(task_list)} |\n')

    f.write('\n---\n\n')

    f.write('## Sample Matched Tasks\n\n')
    f.write('**First 10 Matched Tasks:**\n\n')

    for i, task in enumerate(matched_tasks[:10], 1):
        match = task['template_match']
        f.write(f'{i}. **{task["id"]}** → {match["template_id"]} ({match["match_score"]}%)\n')
        f.write(f'   - Task: {task["description"][:80]}...\n')
        f.write(f'   - Template: {match["template_name"]}\n')
        f.write(f'   - Employee: {task["employee"]} ({task["department"]})\n\n')

    f.write('---\n\n')

    f.write('## Sample Unmatched Tasks (New)\n\n')
    f.write('**First 10 Unmatched Tasks:**\n\n')

    for i, task in enumerate(unmatched_tasks[:10], 1):
        f.write(f'{i}. **{task["id"]}** (New Task)\n')
        f.write(f'   - Description: {task["description"][:80]}...\n')
        f.write(f'   - Employee: {task["employee"]} ({task["department"]})\n')
        f.write(f'   - *Recommendation:* Create new task template\n\n')

    f.write('---\n\n')

    f.write('## Sample Problems\n\n')
    f.write('**First 10 Problems:**\n\n')

    for i, problem in enumerate(problems[:10], 1):
        f.write(f'{i}. **{problem["id"]}** (Problem/Issue)\n')
        f.write(f'   - Description: {problem["description"][:80]}...\n')
        f.write(f'   - Employee: {problem["employee"]} ({problem["department"]})\n')
        f.write(f'   - Status: {problem.get("task_status", "new")}\n\n')

    f.write('---\n\n')

    f.write('## Files Generated\n\n')
    f.write('1. **Day28_Tasks_Matched.json** - Tasks matched to templates\n')
    f.write('2. **Day28_Tasks_Unmatched.json** - New tasks (no template match)\n')
    f.write('3. **Day28_Problems.json** - Problems/issues/bugs\n')
    f.write('4. **Day28_Tasks_Categorized.csv** - Master CSV with all categories\n')
    f.write('5. **Day28_Categorization_Summary.md** - This summary\n\n')

    f.write('---\n\n')
    f.write('*Generated: 2025-11-29*\n')
    f.write('*System: Task Categorization v4.0*\n')

print(f'  Created: Day28_Tasks_Matched.json ({len(matched_tasks)} tasks)')
print(f'  Created: Day28_Tasks_Unmatched.json ({len(unmatched_tasks)} tasks)')
print(f'  Created: Day28_Problems.json ({len(problems)} problems)')
print(f'  Created: Day28_Tasks_Categorized.csv')
print(f'  Created: Day28_Categorization_Summary.md')
print()

print('=' * 80)
print('CATEGORIZATION & MATCHING COMPLETE')
print('=' * 80)
print()
print('Summary:')
print(f'  Tasks matched to templates: {len(matched_tasks)}')
print(f'  New tasks (unmatched): {len(unmatched_tasks)}')
print(f'  Problems identified: {len(problems)}')
print(f'  Match rate: {len(matched_tasks)/len(tasks)*100:.1f}%')
print()
print('[SUCCESS] Ready for review!')
print()
print('Next steps:')
print('  1. Review Day28_Tasks_Categorized.csv in Excel')
print('  2. Validate template matches')
print('  3. Create new templates for unmatched tasks')
print('  4. Triage problems (PRB-###)')
