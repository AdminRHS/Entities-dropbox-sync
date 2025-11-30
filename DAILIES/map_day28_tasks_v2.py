"""
Day 28 Task-to-Project Mapping Script
Maps extracted TST-### tasks to appropriate PRT-### projects
"""

import json
import os
import re
from collections import defaultdict

# Configuration
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'

# Project mapping rules by department and keywords
PROJECT_MAPPING = {
    'AI': {
        'default': 'PRT-001',  # AI Tutorial Research to Taxonomy Integration
        'keywords': {
            'PRT-001': ['tutorial', 'research', 'taxonomy', 'video', 'influencer', 'perplexity'],
            'PRT-006': ['research', 'pipeline', 'integration', 'processing'],
            'PRT-007': ['system', 'analysis', 'architecture', 'documentation'],
            'PRT-009': ['responsibility', 'ecosystem', 'governance', 'framework']
        }
    },
    'Dev': {
        'default': 'PRT-002',  # Complete MCP Automation Stack Setup
        'keywords': {
            'PRT-002': ['mcp', 'automation', 'email', 'calendar', 'claude', 'connector', 'api', 'backend', 'strapi', 'cms'],
            'PRT-007': ['system', 'analysis', 'architecture', 'documentation']
        }
    },
    'Design': {
        'default': 'PRT-008',  # VIDEO
        'keywords': {
            'PRT-008': ['video', 'graphics', 'visual', 'design', 'media', 'content', 'social'],
            'PRT-006': ['research', 'pipeline']
        }
    },
    'LG': {
        'default': 'PRT-004',  # Complete Lead Generation to Customer Conversion Campaign
        'keywords': {
            'PRT-004': ['lead', 'generation', 'google', 'serp', 'outreach', 'email', 'enrichment', 'company', 'contact', 'crm', 'linkedin', 'messaging'],
            'PRT-005': ['enterprise', 'abm', 'account', 'airscale', 'multi-contact', 'directory']
        }
    },
    'HR': {
        'default': 'PRT-003',  # Complete HR Automation Implementation
        'keywords': {
            'PRT-003': ['hr', 'recruitment', 'cv', 'screening', 'interview', 'onboarding', 'automation', 'hiring', 'candidate']
        }
    },
    'Fin': {
        'default': 'PRT-007',  # System Analysis (general business operations)
        'keywords': {
            'PRT-007': ['finance', 'accounting', 'budget', 'expense', 'revenue']
        }
    }
}

print('=' * 80)
print('DAY 28 TASK-TO-PROJECT MAPPING')
print('=' * 80)
print()

# Load extracted tasks
print('[STEP 1] Loading extracted tasks...')
tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_v2.json')

with open(tasks_file, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'  Loaded: {len(tasks)} tasks')
print()

# Map tasks to projects
print('[STEP 2] Mapping tasks to projects...')

def map_task_to_project(task):
    """Map a task to the most appropriate project"""
    dept = task['department']
    desc = task['description'].lower()
    section = task.get('section', '').lower()

    # Get department mapping rules
    if dept not in PROJECT_MAPPING:
        return 'PRT-007'  # Default to System Analysis for unknown departments

    dept_rules = PROJECT_MAPPING[dept]

    # Check keywords for each project
    best_match = dept_rules['default']
    best_score = 0

    for project_id, keywords in dept_rules.get('keywords', {}).items():
        score = 0
        for keyword in keywords:
            if keyword in desc or keyword in section:
                score += 1

        if score > best_score:
            best_score = score
            best_match = project_id

    return best_match

# Apply mapping
for task in tasks:
    task['project'] = map_task_to_project(task)

# Organize by project
by_project = defaultdict(list)
for task in tasks:
    by_project[task['project']].append(task)

print('  Task distribution by project:')
for project_id in sorted(by_project.keys()):
    project_tasks = by_project[project_id]
    completed = sum(1 for t in project_tasks if t['task_status'] == 'completed')
    in_prog = sum(1 for t in project_tasks if t['task_status'] == 'in_progress')
    new = sum(1 for t in project_tasks if t['task_status'] == 'new')
    print(f'    {project_id}: {len(project_tasks)} tasks (Done: {completed}, WIP: {in_prog}, New: {new})')
print()

# Generate project mapping report
print('[STEP 3] Generating project mapping report...')

# Project names
PROJECT_NAMES = {
    'PRT-001': 'AI Tutorial Research to Taxonomy Integration',
    'PRT-002': 'Complete MCP Automation Stack Setup',
    'PRT-003': 'Complete HR Automation Implementation',
    'PRT-004': 'Complete Lead Generation to Customer Conversion Campaign',
    'PRT-005': 'Enterprise Account-Based Marketing Campaign',
    'PRT-006': 'Research to Taxonomy Integration Pipeline',
    'PRT-007': 'System Analysis',
    'PRT-008': 'VIDEO',
    'PRT-009': 'Responsibilities Ecosystem'
}

output_file = os.path.join(OUTPUT_DIR, 'Day28_Project_Mapping_v2.md')
with open(output_file, 'w', encoding='utf-8') as f:
    from datetime import datetime

    f.write('# Day 28 Task-to-Project Mapping Report\n\n')
    f.write(f'**Date:** November 28, 2025\n')
    f.write(f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    f.write(f'**Total Tasks:** {len(tasks)}\n')
    f.write(f'**Projects Mapped:** {len(by_project)}\n')
    f.write('\n---\n\n')

    f.write('## Project Overview\n\n')
    f.write('| Project | Name | Tasks | Done | WIP | New |\n')
    f.write('|---------|------|-------|------|-----|-----|\n')

    total_done = 0
    total_wip = 0
    total_new = 0

    for project_id in sorted(by_project.keys()):
        project_tasks = by_project[project_id]
        project_name = PROJECT_NAMES.get(project_id, 'Unknown Project')

        completed = sum(1 for t in project_tasks if t['task_status'] == 'completed')
        in_prog = sum(1 for t in project_tasks if t['task_status'] == 'in_progress')
        new = sum(1 for t in project_tasks if t['task_status'] == 'new')

        total_done += completed
        total_wip += in_prog
        total_new += new

        f.write(f'| {project_id} | {project_name} | {len(project_tasks)} | {completed} | {in_prog} | {new} |\n')

    f.write(f'| **TOTAL** | | **{len(tasks)}** | **{total_done}** | **{total_wip}** | **{total_new}** |\n')
    f.write('\n---\n\n')

    # Detailed breakdown by project
    f.write('## Detailed Project Breakdown\n\n')

    for project_id in sorted(by_project.keys()):
        project_name = PROJECT_NAMES.get(project_id, 'Unknown Project')
        project_tasks = by_project[project_id]

        f.write(f'### {project_id}: {project_name}\n\n')
        f.write(f'**Total Tasks:** {len(project_tasks)}\n\n')

        # Group by department
        by_dept = defaultdict(list)
        for task in project_tasks:
            by_dept[task['department']].append(task)

        f.write('**Department Breakdown:**\n\n')
        for dept in sorted(by_dept.keys()):
            dept_tasks = by_dept[dept]
            f.write(f'- **{dept}:** {len(dept_tasks)} tasks\n')

        f.write('\n**Sample Tasks:**\n\n')

        # Show first 5 tasks as examples
        for i, task in enumerate(project_tasks[:5]):
            status_emoji = {
                'completed': '[DONE]',
                'in_progress': '[WIP]',
                'new': '[NEW]',
                'blocked': '[BLOCKED]'
            }.get(task['task_status'], '[UNKNOWN]')

            f.write(f'{i+1}. **{task["id"]}** {status_emoji} {task["description"][:100]}...\n')
            f.write(f'   - Employee: {task["employee"]} ({task["department"]})\n')

        if len(project_tasks) > 5:
            f.write(f'\n*... and {len(project_tasks) - 5} more tasks*\n')

        f.write('\n---\n\n')

    f.write('## Mapping Rules Applied\n\n')
    f.write('Tasks were mapped to projects based on:\n\n')
    f.write('1. **Department Default:** Each department has a primary project\n')
    f.write('2. **Keyword Matching:** Task descriptions matched against project keywords\n')
    f.write('3. **Section Context:** Task section headers analyzed for relevance\n\n')

    f.write('### Department-to-Project Defaults\n\n')
    f.write('| Department | Default Project |\n')
    f.write('|------------|------------------|\n')
    for dept, rules in sorted(PROJECT_MAPPING.items()):
        default_proj = rules['default']
        proj_name = PROJECT_NAMES.get(default_proj, 'Unknown')
        f.write(f'| {dept} | {default_proj}: {proj_name} |\n')

    f.write('\n---\n\n')

    f.write('## Next Steps\n\n')
    f.write('1. **Milestone Linking:** Map tasks to MLT-### milestones within projects\n')
    f.write('2. **Tool Association:** Identify TOL-### tools used in each task\n')
    f.write('3. **Guide References:** Link to GDS-### guides for task execution\n')
    f.write('4. **Department Reports:** Generate PMT-033 to PMT-043 reports with mapped data\n')
    f.write('5. **Aggregation:** Combine using PMT-032 for cross-project insights\n')

print(f'  Created: Day28_Project_Mapping_v2.md')
print()

# Save enhanced tasks with project mapping
enhanced_tasks_file = os.path.join(OUTPUT_DIR, 'Day28_Tasks_v2_With_Projects.json')
with open(enhanced_tasks_file, 'w', encoding='utf-8') as f:
    json.dump(tasks, f, indent=2, ensure_ascii=False)

print(f'  Created: Day28_Tasks_v2_With_Projects.json')
print()

# Generate project-specific task lists
print('[STEP 4] Generating project-specific task lists...')

for project_id in sorted(by_project.keys()):
    project_tasks = by_project[project_id]
    project_name = PROJECT_NAMES.get(project_id, 'Unknown')

    project_file = os.path.join(OUTPUT_DIR, f'{project_id}_Day28_Tasks_v2.json')
    with open(project_file, 'w', encoding='utf-8') as f:
        json.dump(project_tasks, f, indent=2, ensure_ascii=False)

    print(f'  Created: {project_id}_Day28_Tasks_v2.json ({len(project_tasks)} tasks)')

print()

print('=' * 80)
print('PROJECT MAPPING COMPLETE')
print('=' * 80)
print(f'Total tasks mapped: {len(tasks)}')
print(f'Projects with tasks: {len(by_project)}')
print(f'Output location: {OUTPUT_DIR}')
print()
print('[SUCCESS] Project mapping completed successfully!')
print('[SUCCESS] Ready for milestone linking and department reports')
