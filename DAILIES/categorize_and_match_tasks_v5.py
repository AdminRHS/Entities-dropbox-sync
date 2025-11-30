"""
Day 28 Task Categorization & Matching v5.0

Features:
1. Filter out metadata/template fields (What I worked on, etc.)
2. Classify by verb tense: Tasks (active) vs Reports (completed) vs Problems
3. Rename: TSK-### (tasks), RPT-### (reports), PRB-### (problems)
4. Match against TST-### task templates
5. Sort matched vs unmatched
"""

import os
import json
import re
from collections import defaultdict
import glob

# Configuration
TASK_TEMPLATES_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-003_Task_Templates'
RESULTS_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities\Actions\Archive\Results_Archived\Results_Master.json'
ACTIONS_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities\Actions\Master\actions_master.json'
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_v2.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'

print('=' * 80)
print('DAY 28 TASK CATEGORIZATION & MATCHING v5.0')
print('=' * 80)
print()

# Load result verbs (completed forms)
print('[STEP 1] Loading verb forms from Actions library...')
with open(RESULTS_FILE, 'r', encoding='utf-8-sig') as f:
    results_data = json.load(f)

result_verbs = set()
for item in results_data['results']:
    result_verbs.add(item['result'].lower())

print(f'  Loaded {len(result_verbs)} result verbs (completed forms)')

# Load action verbs (process forms)
with open(ACTIONS_FILE, 'r', encoding='utf-8-sig') as f:
    actions_data = json.load(f)

process_verbs = set()
base_verbs = set()
for action in actions_data['actions']:
    base_verbs.add(action['action'].lower())
    # Add process forms (verb-ing)
    if 'forms' in action and 'processes' in action['forms']:
        for form in action['forms']['processes']:
            process_verbs.add(form.lower())

print(f'  Loaded {len(base_verbs)} base action verbs')
print(f'  Loaded {len(process_verbs)} process verbs (active forms)')
print()

# Load task templates
print('[STEP 2] Loading Task Manager templates...')
task_templates = {}

pattern = os.path.join(TASK_TEMPLATES_DIR, '**', 'TST-*.json')
template_files = glob.glob(pattern, recursive=True)

for template_file in template_files:
    try:
        with open(template_file, 'r', encoding='utf-8-sig') as f:
            template_data = json.load(f)

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
        pass

print(f'  Loaded {len(task_templates)} task templates')
print()

# Load extracted tasks
print('[STEP 3] Loading extracted tasks from v2.0...')
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    extracted_tasks = json.load(f)

print(f'  Loaded {len(extracted_tasks)} extracted items')
print()

# Define metadata/template field patterns to filter out
# These patterns match field labels with or without values
# Pattern explanation: ^\*+ matches start with one or more asterisks
METADATA_PATTERNS = [
    r'^\*+[A-Za-z\s]+\*+:?\s*$',  # Field labels like *What I worked on:*, *Priority:** (empty)
    r'^\*What I worked on\*+:?',
    r'^\*Whisper [Ff]low.*\*+:?',
    r'^\*Success Criteria\*+:?',
    r'^\*Definition of Done\*+:?',
    r'^\*Priority\*+:?',
    r'^\*Status\*+:?',
    r'^\*Depends On\*+:?',
    r'^\*Assigned To\*+:?',
    r'^\*Estimated Time\*+:?',
    r'^\*Common Support Requests',
    r'^\*Taxonomy Code\*+:?',
    r'^\*Project\*+:?',
    r'^\*Blocks\*+:?',
    r'^\*Category\*+:?',
    r'^\*Tags\*+:?',
    r'^\*Time\*+:?',
    r'^\*Challenge \d+:',
    r'^\*Key Technical Points\*+:?',
    r'^\*HIGH PRIORITY\*+:?',
    r'^\*Development\*+:?',
    r'^\*Documentation\*+:?',
    r'^\*Project Management\*+:?',
    r'^\*Infrastructure\*+:?',
    # Additional common field labels
    r'Whisper Flow (ON|Transcript)',
    r'^Instructions:',
    r'^Include:',
    r'^What:',
]

# Problem indicators
PROBLEM_KEYWORDS = [
    'error', 'bug', 'issue', 'problem', 'broken', 'not working',
    'failed', 'fail', 'crash', 'помилка', 'проблема', 'не працює',
    'fix', 'repair', 'troubleshoot', 'debug'
]

def is_metadata_field(text):
    """Check if text is a metadata field label"""
    text_stripped = text.strip()
    for pattern in METADATA_PATTERNS:
        if re.match(pattern, text_stripped, re.IGNORECASE):
            return True
    return False

def get_first_verb(text):
    """Extract first verb from text"""
    # Get first few words
    words = text.lower().split()[:5]

    for word in words:
        # Remove punctuation
        clean_word = re.sub(r'[^\w]', '', word)

        # Check if it's a result verb (completed)
        if clean_word in result_verbs:
            return ('result', clean_word)

        # Check if it's a process verb (active)
        if clean_word in process_verbs:
            return ('process', clean_word)

        # Check if it's a base verb
        if clean_word in base_verbs:
            return ('base', clean_word)

    return (None, None)

def is_problem(text):
    """Check if text describes a problem"""
    desc_lower = text.lower()
    return any(keyword in desc_lower for keyword in PROBLEM_KEYWORDS)

# Categorize: Tasks vs Reports vs Problems
print('[STEP 4] Categorizing by verb tense and content type...')

tasks = []  # Active verbs
reports = []  # Completed verbs
problems = []  # Issues/bugs
filtered_metadata = []  # Metadata fields

for item in extracted_tasks:
    desc = item['description']

    # Filter metadata fields
    if is_metadata_field(desc):
        filtered_metadata.append(item)
        continue

    # Check if it's a problem
    if is_problem(desc):
        problems.append(item)
        continue

    # Check if status indicates problem
    if 'blocked' in item.get('task_status', ''):
        problems.append(item)
        continue

    # Classify by verb tense
    verb_type, verb = get_first_verb(desc)

    if verb_type == 'result':
        # Completed verb = Report
        item['verb_form'] = 'result'
        item['detected_verb'] = verb
        reports.append(item)
    elif verb_type in ['process', 'base']:
        # Active/base verb = Task
        item['verb_form'] = verb_type
        item['detected_verb'] = verb
        tasks.append(item)
    else:
        # No recognized verb - treat as task by default
        item['verb_form'] = 'unknown'
        item['detected_verb'] = None
        tasks.append(item)

print(f'  Tasks (active verbs): {len(tasks)}')
print(f'  Reports (completed verbs): {len(reports)}')
print(f'  Problems: {len(problems)}')
print(f'  Filtered metadata: {len(filtered_metadata)}')
print()

# Rename IDs
print('[STEP 5] Assigning new IDs...')

for i, task in enumerate(tasks, 1):
    task['original_id'] = task['id']
    task['id'] = f'TSK-{i:03d}'

for i, report in enumerate(reports, 1):
    report['original_id'] = report['id']
    report['id'] = f'RPT-{i:03d}'

for i, problem in enumerate(problems, 1):
    problem['original_id'] = problem['id']
    problem['id'] = f'PRB-{i:03d}'

print(f'  Renamed {len(tasks)} tasks to TSK-###')
print(f'  Renamed {len(reports)} reports to RPT-###')
print(f'  Renamed {len(problems)} problems to PRB-###')
print()

# Match tasks and reports to templates
print('[STEP 6] Matching tasks/reports to Task Manager templates...')

def match_to_template(item_desc, templates):
    """Find best matching template"""
    best_match = None
    best_score = 0

    desc_words = set(re.findall(r'\w+', item_desc.lower()))

    for tst_id, template in templates.items():
        template_text = f"{template['name']} {template['description']} {template.get('action', '')} {template.get('object', '')}"
        template_words = set(re.findall(r'\w+', template_text.lower()))

        common_words = desc_words & template_words
        if len(common_words) > 0:
            score = len(common_words) / max(len(desc_words), 1)

            if score > best_score and score > 0.2:  # At least 20% overlap
                best_score = score
                best_match = {
                    'template_id': tst_id,
                    'template_name': template['name'],
                    'match_score': round(score * 100, 1)
                }

    return best_match

matched_tasks = []
unmatched_tasks = []

for task in tasks:
    match = match_to_template(task['description'], task_templates)
    if match:
        task['template_match'] = match
        matched_tasks.append(task)
    else:
        task['template_match'] = None
        unmatched_tasks.append(task)

matched_reports = []
unmatched_reports = []

for report in reports:
    match = match_to_template(report['description'], task_templates)
    if match:
        report['template_match'] = match
        matched_reports.append(report)
    else:
        report['template_match'] = None
        unmatched_reports.append(report)

print(f'  Tasks matched: {len(matched_tasks)} ({len(matched_tasks)/len(tasks)*100 if tasks else 0:.1f}%)')
print(f'  Tasks unmatched: {len(unmatched_tasks)} ({len(unmatched_tasks)/len(tasks)*100 if tasks else 0:.1f}%)')
print(f'  Reports matched: {len(matched_reports)} ({len(matched_reports)/len(reports)*100 if reports else 0:.1f}%)')
print(f'  Reports unmatched: {len(unmatched_reports)} ({len(unmatched_reports)/len(reports)*100 if reports else 0:.1f}%)')
print()

# Generate reports
print('[STEP 7] Generating categorization reports...')

# JSON outputs
matched_tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Matched.json')
with open(matched_tasks_file, 'w', encoding='utf-8') as f:
    json.dump(matched_tasks, f, indent=2, ensure_ascii=False)

unmatched_tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_Unmatched.json')
with open(unmatched_tasks_file, 'w', encoding='utf-8') as f:
    json.dump(unmatched_tasks, f, indent=2, ensure_ascii=False)

matched_reports_file = os.path.join(OUTPUT_DIR, 'Day28_Reports_Matched.json')
with open(matched_reports_file, 'w', encoding='utf-8') as f:
    json.dump(matched_reports, f, indent=2, ensure_ascii=False)

unmatched_reports_file = os.path.join(OUTPUT_DIR, 'Day28_Reports_Unmatched.json')
with open(unmatched_reports_file, 'w', encoding='utf-8') as f:
    json.dump(unmatched_reports, f, indent=2, ensure_ascii=False)

problems_file = os.path.join(OUTPUT_DIR, 'Day28_Problems.json')
with open(problems_file, 'w', encoding='utf-8') as f:
    json.dump(problems, f, indent=2, ensure_ascii=False)

filtered_file = os.path.join(OUTPUT_DIR, 'Day28_Filtered_Metadata.json')
with open(filtered_file, 'w', encoding='utf-8') as f:
    json.dump(filtered_metadata, f, indent=2, ensure_ascii=False)

# Master CSV
import csv

csv_file = os.path.join(OUTPUT_DIR, 'Day28_Categorized_v5.csv')
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow([
        'New_ID',
        'Original_ID',
        'Category',
        'Verb_Form',
        'Detected_Verb',
        'Task_Name',
        'Employee',
        'Department',
        'Status',
        'Template_Match',
        'Match_Score',
        'Description'
    ])

    # Write matched tasks
    for task in matched_tasks:
        match = task['template_match']
        writer.writerow([
            task['id'],
            task['original_id'],
            'Task (Matched)',
            task.get('verb_form', ''),
            task.get('detected_verb', ''),
            task['description'][:60] + '...' if len(task['description']) > 60 else task['description'],
            task['employee'],
            task['department'],
            task['task_status'],
            match['template_id'],
            f"{match['match_score']}%",
            task['description']
        ])

    # Write unmatched tasks
    for task in unmatched_tasks:
        writer.writerow([
            task['id'],
            task['original_id'],
            'Task (New)',
            task.get('verb_form', ''),
            task.get('detected_verb', ''),
            task['description'][:60] + '...' if len(task['description']) > 60 else task['description'],
            task['employee'],
            task['department'],
            task['task_status'],
            'N/A',
            '0%',
            task['description']
        ])

    # Write matched reports
    for report in matched_reports:
        match = report['template_match']
        writer.writerow([
            report['id'],
            report['original_id'],
            'Report (Matched)',
            report.get('verb_form', ''),
            report.get('detected_verb', ''),
            report['description'][:60] + '...' if len(report['description']) > 60 else report['description'],
            report['employee'],
            report['department'],
            report['task_status'],
            match['template_id'],
            f"{match['match_score']}%",
            report['description']
        ])

    # Write unmatched reports
    for report in unmatched_reports:
        writer.writerow([
            report['id'],
            report['original_id'],
            'Report (New)',
            report.get('verb_form', ''),
            report.get('detected_verb', ''),
            report['description'][:60] + '...' if len(report['description']) > 60 else report['description'],
            report['employee'],
            report['department'],
            report['task_status'],
            'N/A',
            '0%',
            report['description']
        ])

    # Write problems
    for problem in problems:
        writer.writerow([
            problem['id'],
            problem['original_id'],
            'Problem',
            '',
            '',
            problem['description'][:60] + '...' if len(problem['description']) > 60 else problem['description'],
            problem['employee'],
            problem['department'],
            problem.get('task_status', 'new'),
            'N/A',
            'N/A',
            problem['description']
        ])

# Summary Markdown
summary_file = os.path.join(OUTPUT_DIR, 'Day28_Categorization_v5_Summary.md')
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Task Categorization & Matching v5.0 Summary\n\n')
    f.write(f'**Date:** November 28, 2025\n')
    f.write(f'**Total Items Processed:** {len(extracted_tasks)}\n\n')
    f.write('---\n\n')

    f.write('## Categorization Results\n\n')
    f.write('| Category | Count | % | ID Range | File |\n')
    f.write('|----------|-------|---|----------|------|\n')
    f.write(f'| Tasks (Matched) | {len(matched_tasks)} | {len(matched_tasks)/len(extracted_tasks)*100:.1f}% | TSK-001 to TSK-{len(matched_tasks):03d} | Day28_Tasks_Matched.json |\n')
    f.write(f'| Tasks (Unmatched) | {len(unmatched_tasks)} | {len(unmatched_tasks)/len(extracted_tasks)*100:.1f}% | TSK-{len(matched_tasks)+1:03d} to TSK-{len(tasks):03d} | Day28_Tasks_Unmatched.json |\n')
    f.write(f'| Reports (Matched) | {len(matched_reports)} | {len(matched_reports)/len(extracted_tasks)*100:.1f}% | RPT-001 to RPT-{len(matched_reports):03d} | Day28_Reports_Matched.json |\n')
    f.write(f'| Reports (Unmatched) | {len(unmatched_reports)} | {len(unmatched_reports)/len(extracted_tasks)*100:.1f}% | RPT-{len(matched_reports)+1:03d} to RPT-{len(reports):03d} | Day28_Reports_Unmatched.json |\n')
    f.write(f'| Problems | {len(problems)} | {len(problems)/len(extracted_tasks)*100:.1f}% | PRB-001 to PRB-{len(problems):03d} | Day28_Problems.json |\n')
    f.write(f'| **Filtered Metadata** | **{len(filtered_metadata)}** | **{len(filtered_metadata)/len(extracted_tasks)*100:.1f}%** | | Day28_Filtered_Metadata.json |\n')
    f.write(f'| **TOTAL VALID** | **{len(tasks)+len(reports)+len(problems)}** | **{(len(tasks)+len(reports)+len(problems))/len(extracted_tasks)*100:.1f}%** | | |\n\n')

    f.write('---\n\n')

    f.write('## Verb Tense Classification\n\n')
    f.write(f'**Active Verbs (Tasks):** {len(tasks)} items with process/base verbs\n')
    f.write(f'**Completed Verbs (Reports):** {len(reports)} items with result verbs\n\n')

    # Show verb distribution
    verb_counts = defaultdict(int)
    for task in tasks:
        if task.get('detected_verb'):
            verb_counts[task['detected_verb']] += 1
    for report in reports:
        if report.get('detected_verb'):
            verb_counts[report['detected_verb']] += 1

    f.write('### Top 20 Detected Verbs\n\n')
    f.write('| Verb | Count |\n')
    f.write('|------|-------|\n')
    sorted_verbs = sorted(verb_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    for verb, count in sorted_verbs:
        f.write(f'| {verb} | {count} |\n')

    f.write('\n---\n\n')

    f.write('## Sample Tasks (Active Verbs)\n\n')
    for i, task in enumerate(matched_tasks[:10], 1):
        match = task['template_match']
        f.write(f'{i}. **{task["id"]}** ({task.get("detected_verb", "N/A")}) -> {match["template_id"]} ({match["match_score"]}%)\n')
        f.write(f'   - Task: {task["description"][:80]}...\n')
        f.write(f'   - Employee: {task["employee"]} ({task["department"]})\n\n')

    f.write('---\n\n')

    f.write('## Sample Reports (Completed Verbs)\n\n')
    for i, report in enumerate(matched_reports[:10], 1):
        match = report['template_match']
        f.write(f'{i}. **{report["id"]}** ({report.get("detected_verb", "N/A")}) -> {match["template_id"]} ({match["match_score"]}%)\n')
        f.write(f'   - Report: {report["description"][:80]}...\n')
        f.write(f'   - Employee: {report["employee"]} ({report["department"]})\n\n')

    f.write('---\n\n')

    f.write('## Files Generated\n\n')
    f.write('1. **Day28_Tasks_Matched.json** - Tasks matched to templates\n')
    f.write('2. **Day28_Tasks_Unmatched.json** - New tasks (no template match)\n')
    f.write('3. **Day28_Reports_Matched.json** - Reports matched to templates\n')
    f.write('4. **Day28_Reports_Unmatched.json** - New reports (no template match)\n')
    f.write('5. **Day28_Problems.json** - Problems/issues/bugs\n')
    f.write('6. **Day28_Filtered_Metadata.json** - Filtered metadata fields\n')
    f.write('7. **Day28_Categorized_v5.csv** - Master CSV with all categories\n')
    f.write('8. **Day28_Categorization_v5_Summary.md** - This summary\n\n')

    f.write('---\n\n')
    f.write('*Generated: 2025-11-29*\n')
    f.write('*System: Task Categorization v5.0*\n')

print(f'  Created: Day28_Tasks_Matched.json ({len(matched_tasks)} tasks)')
print(f'  Created: Day28_Tasks_Unmatched.json ({len(unmatched_tasks)} tasks)')
print(f'  Created: Day28_Reports_Matched.json ({len(matched_reports)} reports)')
print(f'  Created: Day28_Reports_Unmatched.json ({len(unmatched_reports)} reports)')
print(f'  Created: Day28_Problems.json ({len(problems)} problems)')
print(f'  Created: Day28_Filtered_Metadata.json ({len(filtered_metadata)} metadata fields)')
print(f'  Created: Day28_Categorized_v5.csv')
print(f'  Created: Day28_Categorization_v5_Summary.md')
print()

print('=' * 80)
print('CATEGORIZATION & MATCHING v5.0 COMPLETE')
print('=' * 80)
print()
print('Summary:')
print(f'  Tasks (active verbs): {len(tasks)} ({len(matched_tasks)} matched, {len(unmatched_tasks)} new)')
print(f'  Reports (completed verbs): {len(reports)} ({len(matched_reports)} matched, {len(unmatched_reports)} new)')
print(f'  Problems identified: {len(problems)}')
print(f'  Metadata filtered: {len(filtered_metadata)}')
print(f'  Total valid items: {len(tasks)+len(reports)+len(problems)} ({(len(tasks)+len(reports)+len(problems))/len(extracted_tasks)*100:.1f}%)')
print()
print('[SUCCESS] Ready for review!')
