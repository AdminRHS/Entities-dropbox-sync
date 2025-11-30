"""
Day 28 AI-Powered Task Categorization

This script prepares extracted tasks for AI-powered categorization.
It creates batches that can be processed by Claude Code to:
1. Filter out metadata/template fields
2. Classify tasks vs reports vs problems
3. Match to task templates

Output: Batches ready for AI review
"""

import os
import json

# Configuration
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_v2.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\AI_Review'
BATCH_SIZE = 50  # Process 50 items at a time for AI review

print('=' * 80)
print('DAY 28 AI-POWERED CATEGORIZATION PREP')
print('=' * 80)
print()

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load extracted tasks
print('[STEP 1] Loading extracted items from v2.0...')
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    extracted_tasks = json.load(f)

print(f'  Loaded {len(extracted_tasks)} items')
print()

# Create batches
print(f'[STEP 2] Creating batches ({BATCH_SIZE} items each)...')

batches = []
for i in range(0, len(extracted_tasks), BATCH_SIZE):
    batch = extracted_tasks[i:i+BATCH_SIZE]
    batch_num = (i // BATCH_SIZE) + 1
    batches.append({
        'batch_number': batch_num,
        'items': batch,
        'start_index': i,
        'end_index': min(i + BATCH_SIZE, len(extracted_tasks)) - 1
    })

print(f'  Created {len(batches)} batches')
print()

# Save batches
print('[STEP 3] Saving batches for AI review...')

for batch_data in batches:
    batch_file = os.path.join(OUTPUT_DIR, f'Batch_{batch_data["batch_number"]:02d}.json')
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(batch_data['items'], f, indent=2, ensure_ascii=False)
    print(f'  Saved: Batch_{batch_data["batch_number"]:02d}.json ({len(batch_data["items"])} items)')

# Create review instructions
instructions_file = os.path.join(OUTPUT_DIR, 'AI_Review_Instructions.md')
with open(instructions_file, 'w', encoding='utf-8') as f:
    f.write('# AI Review Instructions for Day 28 Task Categorization\n\n')
    f.write('## Objective\n\n')
    f.write('Review extracted items and categorize them into:\n')
    f.write('1. **Tasks (TSK-###)** - Work to be done (active verbs)\n')
    f.write('2. **Reports (RPT-###)** - Work completed (completed verbs)\n')
    f.write('3. **Problems (PRB-###)** - Issues/bugs/blockers\n')
    f.write('4. **Metadata** - Template fields, section headers (to be filtered)\n\n')
    f.write('## Classification Rules\n\n')
    f.write('### Metadata (Filter Out)\n')
    f.write('- Field labels: *Priority:**, *Status:**, *Time:**, etc.\n')
    f.write('- Section headers: *What I worked on:**, *Success Criteria:**, etc.\n')
    f.write('- Template markers: *Whisper Flow Transcript:**, *Definition of Done:**, etc.\n')
    f.write('- Instructions/placeholders: "Instructions:", "[Time] - [Activity]"\n\n')
    f.write('### Tasks (Active Work)\n')
    f.write('- Start with action verbs in base/process form (do, doing, create, creating)\n')
    f.write('- Describe work that needs to be performed\n')
    f.write('- Examples: "Respond to messages", "Creating design mockups", "Update API"\n\n')
    f.write('### Reports (Completed Work)\n')
    f.write('- Start with completed verbs (created, developed, implemented, sent, updated)\n')
    f.write('- Describe work that was done\n')
    f.write('- Examples: "Created new feature", "Sent report", "Updated documentation"\n\n')
    f.write('### Problems\n')
    f.write('- Contain keywords: error, bug, issue, problem, broken, failed, fix, blocked\n')
    f.write('- Describe something not working or needing repair\n')
    f.write('- Examples: "API endpoint not working", "Fix authentication bug"\n\n')
    f.write('## Process\n\n')
    f.write(f'1. Process batches sequentially (Batch_01.json through Batch_{len(batches):02d}.json)\n')
    f.write('2. For each item, determine: Task, Report, Problem, or Metadata\n')
    f.write('3. Create categorized output with new IDs (TSK/RPT/PRB-###)\n')
    f.write('4. Match tasks/reports to existing task templates if possible\n\n')
    f.write('## Output Format\n\n')
    f.write('For each batch, create a categorized JSON file with structure:\n')
    f.write('```json\n')
    f.write('{\n')
    f.write('  "batch_number": 1,\n')
    f.write('  "tasks": [...],\n')
    f.write('  "reports": [...],\n')
    f.write('  "problems": [...],\n')
    f.write('  "metadata_filtered": [...]\n')
    f.write('}\n')
    f.write('```\n\n')
    f.write('## Key Insight\n\n')
    f.write('The extraction contains:\n')
    f.write('- Real tasks and outcomes from daily work\n')
    f.write('- Template field labels and section headers\n')
    f.write('- Instructional text and placeholders\n\n')
    f.write('Use context understanding to separate actual work items from template structure.\n')

print(f'  Created: AI_Review_Instructions.md')
print()

# Create summary
summary_file = os.path.join(OUTPUT_DIR, 'Batches_Summary.md')
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Task Categorization - Batch Summary\n\n')
    f.write(f'**Total Items:** {len(extracted_tasks)}\n')
    f.write(f'**Batch Size:** {BATCH_SIZE} items\n')
    f.write(f'**Total Batches:** {len(batches)}\n\n')
    f.write('## Batches\n\n')
    f.write('| Batch # | File | Items | Index Range |\n')
    f.write('|---------|------|-------|-------------|\n')
    for batch_data in batches:
        f.write(f'| {batch_data["batch_number"]:02d} | Batch_{batch_data["batch_number"]:02d}.json | {len(batch_data["items"])} | {batch_data["start_index"]}-{batch_data["end_index"]} |\n')

print(f'  Created: Batches_Summary.md')
print()

print('=' * 80)
print('BATCH PREPARATION COMPLETE')
print('=' * 80)
print()
print(f'Created {len(batches)} batches in: {OUTPUT_DIR}')
print()
print('Next steps:')
print('  1. Review AI_Review_Instructions.md')
print('  2. Process batches with Claude Code for categorization')
print('  3. Merge categorized batches into final output')
