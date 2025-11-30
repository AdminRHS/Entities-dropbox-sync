"""
Create Day 28 Task Master Summary
Organized by employee with clear task listings for review
"""

import json
import re
from collections import defaultdict

# Load tasks
tasks_file = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_With_Projects.json'
output_md = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Task_Master_Summary.md'

with open(tasks_file, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'Loaded {len(tasks)} tasks')

# Organize by department and employee
by_dept = defaultdict(lambda: defaultdict(list))
for task in tasks:
    by_dept[task['department']][task['employee']].append(task)

# Function to create task name
def create_task_name(description):
    """Create a concise task name"""
    clean = re.sub(r'\*\*|\*|`', '', description)
    clean = re.sub(r'^\*[^*]+\*\*:\s*', '', clean)
    clean = clean.strip()
    if len(clean) > 80:
        clean = clean[:77] + '...'
    if not clean or len(clean) < 5:
        words = description.split()[:8]
        clean = ' '.join(words)
        if len(clean) > 80:
            clean = clean[:77] + '...'
    return clean

# Generate markdown summary
with open(output_md, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Task Master Summary - Review & Validation\n\n')
    f.write('**Date:** November 28, 2025\n')
    f.write('**Total Tasks:** 681\n')
    f.write('**Employees:** 12\n')
    f.write('**Departments:** 5\n\n')
    f.write('---\n\n')

    f.write('## Quick Statistics\n\n')
    f.write('| Department | Employees | Total Tasks | Completed | In Progress | New |\n')
    f.write('|------------|-----------|-------------|-----------|-------------|-----|\n')

    total_tasks = 0
    total_complete = 0
    total_wip = 0
    total_new = 0

    for dept in sorted(by_dept.keys()):
        emp_tasks = by_dept[dept]
        dept_total = sum(len(tasks) for tasks in emp_tasks.values())
        dept_complete = sum(1 for emp_list in emp_tasks.values() for t in emp_list if t['task_status'] == 'completed')
        dept_wip = sum(1 for emp_list in emp_tasks.values() for t in emp_list if t['task_status'] == 'in_progress')
        dept_new = sum(1 for emp_list in emp_tasks.values() for t in emp_list if t['task_status'] == 'new')

        total_tasks += dept_total
        total_complete += dept_complete
        total_wip += dept_wip
        total_new += dept_new

        f.write(f'| {dept} | {len(emp_tasks)} | {dept_total} | {dept_complete} | {dept_wip} | {dept_new} |\n')

    f.write(f'| **TOTAL** | **12** | **{total_tasks}** | **{total_complete}** | **{total_wip}** | **{total_new}** |\n\n')

    f.write('---\n\n')
    f.write('## Task Listings by Employee\n\n')
    f.write('**Review Instructions:**\n')
    f.write('- ✅ = Task validated, keep as-is\n')
    f.write('- 🔄 = Task needs revision\n')
    f.write('- ❌ = Task should be removed\n')
    f.write('- 📝 = Add notes/comments in the margin\n\n')
    f.write('---\n\n')

    # Generate detailed task listings
    for dept in sorted(by_dept.keys()):
        f.write(f'## {dept} Department\n\n')

        emp_tasks = by_dept[dept]

        for emp_name in sorted(emp_tasks.keys()):
            emp_task_list = emp_tasks[emp_name]

            # Count statuses
            completed = sum(1 for t in emp_task_list if t['task_status'] == 'completed')
            wip = sum(1 for t in emp_task_list if t['task_status'] == 'in_progress')
            new = sum(1 for t in emp_task_list if t['task_status'] == 'new')

            f.write(f'### {emp_name}\n\n')
            f.write(f'**Employee Status:** {emp_task_list[0]["status"]}\n')
            f.write(f'**Tasks:** {len(emp_task_list)} total (✅ {completed} done, 🔄 {wip} in progress, 🆕 {new} new)\n')
            f.write(f'**Projects:** {", ".join(sorted(set(t["project"] for t in emp_task_list)))}\n')
            f.write(f'**Task Range:** {emp_task_list[0]["id"]} to {emp_task_list[-1]["id"]}\n\n')

            f.write('| # | Task ID | Status | Task Name | Project | Validate |\n')
            f.write('|---|---------|--------|-----------|---------|----------|\n')

            for i, task in enumerate(emp_task_list, 1):
                task_name = create_task_name(task['description'])
                status_icon = {
                    'completed': '✅',
                    'in_progress': '🔄',
                    'new': '🆕',
                    'blocked': '⏸️'
                }.get(task['task_status'], '❓')

                f.write(f'| {i} | {task["id"]} | {status_icon} | {task_name} | {task["project"]} | ⬜ |\n')

            f.write('\n')

            # Show sample full descriptions
            f.write('<details>\n')
            f.write('<summary>View Full Task Descriptions (Click to expand)</summary>\n\n')

            for i, task in enumerate(emp_task_list[:10], 1):  # Show first 10
                f.write(f'**{task["id"]}:** {task["description"]}\n\n')

            if len(emp_task_list) > 10:
                f.write(f'*...and {len(emp_task_list) - 10} more tasks. See CSV for complete list.*\n\n')

            f.write('</details>\n\n')

            f.write('---\n\n')

    f.write('## Validation Checklist\n\n')
    f.write('**Instructions:** Check each item after review\n\n')

    for dept in sorted(by_dept.keys()):
        f.write(f'### {dept} Department\n\n')
        emp_tasks = by_dept[dept]
        for emp_name in sorted(emp_tasks.keys()):
            emp_task_list = emp_tasks[emp_name]
            f.write(f'- [ ] {emp_name} ({len(emp_task_list)} tasks) - Reviewed\n')
        f.write('\n')

    f.write('---\n\n')
    f.write('## Files for Review\n\n')
    f.write('**CSV File (Full Data):**\n')
    f.write('- [Day28_Task_Master_Review.csv](Day28_Task_Master_Review.csv)\n')
    f.write('- Contains all 681 tasks with full descriptions\n')
    f.write('- Can be opened in Excel/Google Sheets for filtering and sorting\n\n')

    f.write('**JSON Files (Programmatic Access):**\n')
    f.write('- [Day28_Tasks_With_Projects.json](Day28_Tasks_With_Projects.json)\n')
    f.write('- Machine-readable format for scripts and automation\n\n')

    f.write('**Original Extraction Report:**\n')
    f.write('- [Day28_Task_Extraction.md](Day28_Task_Extraction.md)\n')
    f.write('- Detailed extraction with section context\n\n')

    f.write('---\n\n')
    f.write('*Generated: 2025-11-29*\n')
    f.write('*Purpose: Task validation and review before final processing*\n')

print(f'Created: {output_md}')
print('')
print('[SUCCESS] Task Master Summary ready for review')
print('')
print('Files created:')
print('  1. Day28_Task_Master_Review.csv (682 rows - all tasks)')
print('  2. Day28_Task_Master_Summary.md (organized by employee)')
print('')
print('Next steps:')
print('  1. Open CSV in Excel/Google Sheets')
print('  2. Review task names and descriptions')
print('  3. Mark validation status in Summary.md')
print('  4. Identify tasks to keep/revise/remove')
