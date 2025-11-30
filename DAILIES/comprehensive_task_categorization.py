"""
Day 28 Comprehensive AI-Guided Task Categorization

Based on vocabulary analysis of actual data, this script:
1. Filters metadata (section headers like *What I worked on:*)
2. Classifies by verb tense (Tasks vs Reports vs Problems)
3. Clusters related items into workflows
4. Generates short task names
5. Marks Ukrainian text for translation
"""

import os
import json
import re
from collections import defaultdict

# Configuration
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_v2.json'
VOCAB_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Task_Vocabulary_Analysis.json'
CLUSTERING_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Clustering_Rules_From_Data.json'
RESULTS_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities\Actions\Archive\Results_Archived\Results_Master.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final'

print('=' * 80)
print('COMPREHENSIVE TASK CATEGORIZATION - VOCABULARY-GUIDED')
print('=' * 80)
print()

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
print('[STEP 1] Loading source data...')
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

with open(VOCAB_FILE, 'r', encoding='utf-8-sig') as f:
    vocab = json.load(f)

with open(CLUSTERING_FILE, 'r', encoding='utf-8-sig') as f:
    clustering_rules = json.load(f)

with open(RESULTS_FILE, 'r', encoding='utf-8-sig') as f:
    results_data = json.load(f)

result_verbs = set(r['result'].lower() for r in results_data['results'])

print(f'  Loaded {len(tasks)} extracted items')
print(f'  Loaded {len(result_verbs)} result verbs (completed forms)')
print()

# Build aggressive metadata filter based on vocabulary analysis
print('[STEP 2] Building metadata filters from vocabulary...')

# Top non-action words are section headers/metadata
metadata_indicators = ['what', 'whisper', 'time', 'challenge', 'step', 'project',
                       'status', 'template', 'technical']

metadata_patterns = [
    r'^\*What I worked on\*+:?',
    r'^\*Whisper [Ff]low.*\*+:?',
    r'Whisper Flow (ON|Transcript)',
    r'^\*Time\*+:?',
    r'^\*Challenge \d+:',
    r'^\*Step \d+:',
    r'^\*Project\*+:?',
    r'^\*Status\*+:?',
    r'^\*Priority\*+:?',
    r'^\*Taxonomy Code\*+:?',
    r'^\*\*Step \d+:',
    r'^\*Technical',
    r'^\*Key Technical Points',
    r'^\*Success Criteria',
    r'^\*Definition of Done',
    r'^\*Depends On\*+:?',
    r'^\*Assigned To\*+:?',
    r'^\*Estimated Time\*+:?',
    r'^\*Actual Time\*+:?',
    r'^\*Blocks\*+:?',
    r'^\*Common Support',
    r'^\*Development\*+:?',
    r'^\*Documentation\*+:?',
    r'^\*Project Management\*+:?',
    r'^\*Infrastructure\*+:?',
    r'^\*HIGH PRIORITY',
]

def is_metadata(text):
    """Check if text is metadata/section header"""
    text_lower = text.lower().strip()

    # Check patterns
    for pattern in metadata_patterns:
        if re.match(pattern, text, re.IGNORECASE):
            return True

    # Check if starts with metadata indicators
    words = text_lower.split()[:2]
    if words and words[0] in metadata_indicators:
        return True

    # Check for field labels pattern: *Field:** value
    if re.match(r'^\*[A-Z][A-Za-z\s]+\*\*:', text):
        return True

    return False

def has_ukrainian(text):
    """Check if text contains Ukrainian/Russian characters"""
    cyrillic = re.compile('[а-яА-ЯіїєґІЇЄҐ]')
    return bool(cyrillic.search(text))

def get_first_verb(text):
    """Extract first meaningful verb"""
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words[:5]:
        if word in result_verbs:
            return ('result', word)
        if word not in metadata_indicators and len(word) > 2:
            return ('active', word)
    return (None, None)

def generate_task_name(description, verb_type=None, verb=None):
    """Generate short task name from description"""
    # Remove asterisks and extra formatting
    clean = re.sub(r'\*+', '', description)
    clean = re.sub(r'\[.*?\]', '', clean)

    # Get first 5 words or until punctuation
    words = []
    for word in clean.split():
        if word in ['-', '—', ':', '**']:
            break
        words.append(word)
        if len(words) >= 5:
            break

    name = ' '.join(words)

    # Truncate if too long
    if len(name) > 50:
        name = name[:47] + '...'

    return name if name else description[:50]

print('  Built metadata filters')
print()

# Categorize items
print('[STEP 3] Categorizing items...')

tasks_list = []
reports_list = []
problems_list = []
metadata_filtered = []

problem_keywords = ['error', 'bug', 'issue', 'problem', 'broken', 'not working',
                    'failed', 'fail', 'crash', 'помилка', 'проблема', 'не працює',
                    'fix', 'repair', 'troubleshoot', 'debug']

for item in tasks:
    desc = item['description']

    # Filter metadata
    if is_metadata(desc):
        metadata_filtered.append({**item, 'filter_reason': 'metadata/section_header'})
        continue

    # Check for problems
    is_problem = any(kw in desc.lower() for kw in problem_keywords)
    if is_problem or 'blocked' in item.get('task_status', ''):
        item['category'] = 'problem'
        problems_list.append(item)
        continue

    # Get verb form
    verb_type, verb = get_first_verb(desc)
    item['verb_type'] = verb_type
    item['detected_verb'] = verb

    # Check for translation needs
    if has_ukrainian(desc):
        item['needs_translation'] = True

    # Classify by verb
    if verb_type == 'result':
        item['category'] = 'report'
        reports_list.append(item)
    else:
        item['category'] = 'task'
        tasks_list.append(item)

print(f'  Tasks: {len(tasks_list)}')
print(f'  Reports: {len(reports_list)}')
print(f'  Problems: {len(problems_list)}')
print(f'  Filtered metadata: {len(metadata_filtered)}')
print()

# Cluster by section (workflows)
print('[STEP 4] Clustering into workflows...')

# Group by employee + section
workflows = defaultdict(list)
for item in tasks_list + reports_list:
    emp = item['employee']
    section = item.get('section', 'Uncategorized')
    key = f"{emp}|||{section}"
    workflows[key].append(item)

# Identify high-value clusters (5+ items)
workflow_tasks = []
standalone_tasks = []
standalone_reports = []

workflow_id_counter = 1
task_id_counter = 1
report_id_counter = 1

for key, items in workflows.items():
    emp, section = key.split('|||')

    if len(items) >= 5:
        # Create workflow
        # Separate tasks from reports within workflow
        wf_tasks = [i for i in items if i['category'] == 'task']
        wf_reports = [i for i in items if i['category'] == 'report']

        workflow_name = generate_task_name(section)

        workflow_task = {
            'id': f'WFL-{workflow_id_counter:03d}',
            'name': f'{emp} - {workflow_name}',
            'employee': emp,
            'section': section,
            'type': 'workflow',
            'item_count': len(items),
            'tasks_count': len(wf_tasks),
            'reports_count': len(wf_reports),
            'items': items
        }
        workflow_tasks.append(workflow_task)
        workflow_id_counter += 1
    else:
        # Standalone items
        for item in items:
            if item['category'] == 'task':
                standalone_tasks.append(item)
            elif item['category'] == 'report':
                standalone_reports.append(item)

print(f'  Workflows created: {len(workflow_tasks)}')
print(f'  Standalone tasks: {len(standalone_tasks)}')
print(f'  Standalone reports: {len(standalone_reports)}')
print()

# Assign IDs and names
print('[STEP 5] Assigning IDs and task names...')

# Workflows already have IDs

# Standalone tasks
for task in standalone_tasks:
    task['id'] = f'TSK-{task_id_counter:03d}'
    task['name'] = generate_task_name(task['description'], task.get('verb_type'), task.get('detected_verb'))
    task_id_counter += 1

# Standalone reports
for report in standalone_reports:
    report['id'] = f'RPT-{report_id_counter:03d}'
    report['name'] = generate_task_name(report['description'], report.get('verb_type'), report.get('detected_verb'))
    report_id_counter += 1

# Problems
for i, problem in enumerate(problems_list, 1):
    problem['id'] = f'PRB-{i:03d}'
    problem['name'] = generate_task_name(problem['description'])

print(f'  Assigned {workflow_id_counter-1} workflow IDs (WFL-###)')
print(f'  Assigned {task_id_counter-1} task IDs (TSK-###)')
print(f'  Assigned {report_id_counter-1} report IDs (RPT-###)')
print(f'  Assigned {len(problems_list)} problem IDs (PRB-###)')
print()

# Save outputs
print('[STEP 6] Saving categorized outputs...')

# Workflows
workflows_file = os.path.join(OUTPUT_DIR, 'Day28_Workflows.json')
with open(workflows_file, 'w', encoding='utf-8') as f:
    json.dump(workflow_tasks, f, indent=2, ensure_ascii=False)

# Tasks
tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Standalone.json')
with open(tasks_file, 'w', encoding='utf-8') as f:
    json.dump(standalone_tasks, f, indent=2, ensure_ascii=False)

# Reports
reports_file = os.path.join(OUTPUT_DIR, 'Day28_Reports_Standalone.json')
with open(reports_file, 'w', encoding='utf-8') as f:
    json.dump(standalone_reports, f, indent=2, ensure_ascii=False)

# Problems
problems_file = os.path.join(OUTPUT_DIR, 'Day28_Problems.json')
with open(problems_file, 'w', encoding='utf-8') as f:
    json.dump(problems_list, f, indent=2, ensure_ascii=False)

# Metadata
metadata_file = os.path.join(OUTPUT_DIR, 'Day28_Metadata_Filtered.json')
with open(metadata_file, 'w', encoding='utf-8') as f:
    json.dump(metadata_filtered, f, indent=2, ensure_ascii=False)

# Master CSV
import csv

csv_file = os.path.join(OUTPUT_DIR, 'Day28_Master_Categorized.csv')
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['ID', 'Type', 'Name', 'Employee', 'Department', 'Category',
                     'Verb_Type', 'Needs_Translation', 'Item_Count', 'Description'])

    # Workflows
    for wf in workflow_tasks:
        writer.writerow([
            wf['id'],
            'Workflow',
            wf['name'],
            wf['employee'],
            wf['items'][0]['department'] if wf['items'] else '',
            f"{wf['tasks_count']}T + {wf['reports_count']}R",
            'mixed',
            '',
            wf['item_count'],
            wf['section'][:100]
        ])

    # Tasks
    for task in standalone_tasks:
        writer.writerow([
            task['id'],
            'Task',
            task['name'],
            task['employee'],
            task['department'],
            'task',
            task.get('verb_type', ''),
            'Yes' if task.get('needs_translation') else 'No',
            1,
            task['description'][:100]
        ])

    # Reports
    for report in standalone_reports:
        writer.writerow([
            report['id'],
            'Report',
            report['name'],
            report['employee'],
            report['department'],
            'report',
            report.get('verb_type', ''),
            'Yes' if report.get('needs_translation') else 'No',
            1,
            report['description'][:100]
        ])

    # Problems
    for problem in problems_list:
        writer.writerow([
            problem['id'],
            'Problem',
            problem['name'],
            problem['employee'],
            problem['department'],
            'problem',
            '',
            'Yes' if problem.get('needs_translation') else 'No',
            1,
            problem['description'][:100]
        ])

# Summary
summary_file = os.path.join(OUTPUT_DIR, 'Day28_Categorization_Summary.md')
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Comprehensive Task Categorization Summary\n\n')
    f.write('**Date:** November 28, 2025\n')
    f.write('**Method:** Vocabulary-Guided AI Categorization\n')
    f.write(f'**Total Items Processed:** {len(tasks)}\n\n')
    f.write('---\n\n')

    f.write('## Results\n\n')
    f.write('| Category | Count | % | ID Range |\n')
    f.write('|----------|-------|---|----------|\n')
    f.write(f'| Workflows | {len(workflow_tasks)} | {len(workflow_tasks)/len(tasks)*100:.1f}% | WFL-001 to WFL-{len(workflow_tasks):03d} |\n')
    f.write(f'| Standalone Tasks | {len(standalone_tasks)} | {len(standalone_tasks)/len(tasks)*100:.1f}% | TSK-001 to TSK-{len(standalone_tasks):03d} |\n')
    f.write(f'| Standalone Reports | {len(standalone_reports)} | {len(standalone_reports)/len(tasks)*100:.1f}% | RPT-001 to RPT-{len(standalone_reports):03d} |\n')
    f.write(f'| Problems | {len(problems_list)} | {len(problems_list)/len(tasks)*100:.1f}% | PRB-001 to PRB-{len(problems_list):03d} |\n')
    f.write(f'| **Filtered Metadata** | **{len(metadata_filtered)}** | **{len(metadata_filtered)/len(tasks)*100:.1f}%** | - |\n')

    total_valid = len(workflow_tasks) + len(standalone_tasks) + len(standalone_reports) + len(problems_list)
    total_items_in_workflows = sum(wf['item_count'] for wf in workflow_tasks)
    f.write(f'| **Total Valid** | **{total_valid}** ({total_items_in_workflows} items total) | **{total_valid/len(tasks)*100:.1f}%** | - |\n\n')

    f.write('---\n\n')

    f.write('## Top 10 Workflows\n\n')
    sorted_workflows = sorted(workflow_tasks, key=lambda x: x['item_count'], reverse=True)[:10]
    for i, wf in enumerate(sorted_workflows, 1):
        f.write(f'{i}. **{wf["id"]}** - {wf["name"]}\n')
        f.write(f'   - Items: {wf["item_count"]} ({wf["tasks_count"]} tasks, {wf["reports_count"]} reports)\n')
        f.write(f'   - Employee: {wf["employee"]}\n\n')

    f.write('---\n\n')
    f.write('## Files Generated\n\n')
    f.write('1. **Day28_Workflows.json** - Clustered workflows (5+ items)\n')
    f.write('2. **Day28_Tasks_Standalone.json** - Individual tasks\n')
    f.write('3. **Day28_Reports_Standalone.json** - Individual reports\n')
    f.write('4. **Day28_Problems.json** - Problems/issues\n')
    f.write('5. **Day28_Metadata_Filtered.json** - Filtered section headers\n')
    f.write('6. **Day28_Master_Categorized.csv** - Master CSV\n')
    f.write('7. **Day28_Categorization_Summary.md** - This summary\n')

print(f'  Saved: Day28_Workflows.json')
print(f'  Saved: Day28_Tasks_Standalone.json')
print(f'  Saved: Day28_Reports_Standalone.json')
print(f'  Saved: Day28_Problems.json')
print(f'  Saved: Day28_Metadata_Filtered.json')
print(f'  Saved: Day28_Master_Categorized.csv')
print(f'  Saved: Day28_Categorization_Summary.md')
print()

print('=' * 80)
print('CATEGORIZATION COMPLETE')
print('=' * 80)
print()
print(f'Workflows: {len(workflow_tasks)} ({total_items_in_workflows} items clustered)')
print(f'Standalone Tasks: {len(standalone_tasks)}')
print(f'Standalone Reports: {len(standalone_reports)}')
print(f'Problems: {len(problems_list)}')
print(f'Filtered: {len(metadata_filtered)}')
print(f'Total Valid: {total_valid} categories ({total_items_in_workflows + len(standalone_tasks) + len(standalone_reports) + len(problems_list)} items)')
