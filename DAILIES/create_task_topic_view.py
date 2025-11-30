"""
Create Task Topic View - Organize by themes/topics for better validation
"""

import json
import re
from collections import defaultdict

# Load tasks
tasks_file = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_With_Projects.json'
output_file = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_By_Topic.md'

with open(tasks_file, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'Loaded {len(tasks)} tasks')

# Function to create clean task name
def create_task_name(description):
    """Create concise task name"""
    clean = re.sub(r'\*\*|\*|`', '', description)
    clean = re.sub(r'^\*[^*]+\*\*:\s*', '', clean)
    clean = clean.strip()
    if len(clean) > 70:
        clean = clean[:67] + '...'
    if not clean or len(clean) < 5:
        words = description.split()[:6]
        clean = ' '.join(words)
    return clean

# Function to identify task topic/theme
def identify_topic(task):
    """Identify the main topic/theme of a task"""
    desc_lower = task['description'].lower()
    section_lower = task['section'].lower()

    # Check for specific topics
    if any(word in desc_lower for word in ['strapi', 'cms', 'content management']):
        return 'Strapi CMS Integration'
    elif any(word in desc_lower or word in section_lower for word in ['mascot', 'design', 'graphic']):
        return 'Mascot Design System'
    elif any(word in desc_lower for word in ['discord', 'support', 'help', 'ai tool']):
        return 'AI Tool Support'
    elif any(word in desc_lower for word in ['scraping', 'scrape', 'data collection', 'vacancy', 'vacancies']):
        return 'Data Scraping & Collection'
    elif any(word in desc_lower for word in ['lead', 'crm', 'linkedin', 'outreach', 'campaign']):
        return 'Lead Generation & CRM'
    elif any(word in desc_lower or word in section_lower for word in ['calendar', 'booking', 'scheduling']):
        return 'Calendar Management'
    elif any(word in desc_lower for word in ['optimization', 'performance', 'bottleneck', 'diagnostic']):
        return 'System Optimization'
    elif any(word in desc_lower for word in ['gem', 'chatgpt', 'prompt', 'template']):
        return 'AI Agent Development'
    elif any(word in desc_lower for word in ['export', 'script', 'automation', 'workflow']):
        return 'Script Automation'
    elif any(word in desc_lower for word in ['ui', 'ux', 'interface', 'responsive', 'design']):
        return 'UI/UX Improvements'
    elif any(word in desc_lower for word in ['black friday', 'messaging', 'message']):
        return 'Black Friday Campaign'
    elif desc_lower.startswith(('what:', 'what i worked', 'outcomes:', 'whisper flow', 'time stamp', 'include all')):
        return 'Template/Metadata (Remove)'
    elif desc_lower in ['priority:', 'description:', 'subtasks:', 'success criteria:', 'definition of done:']:
        return 'Field Labels (Remove)'
    elif 'format' in desc_lower or 'naming' in desc_lower or 'px' in desc_lower or 'mb' in desc_lower:
        return 'Technical Specifications'
    else:
        return 'General/Operational'

# Organize tasks by topic
by_topic = defaultdict(list)
for task in tasks:
    topic = identify_topic(task)
    by_topic[topic].append(task)

# Generate topic view
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('# Day 28 Tasks Organized by Topic/Milestone\n\n')
    f.write('**Purpose:** Review tasks grouped by theme for better validation\n')
    f.write('**Total Tasks:** 681\n')
    f.write(f'**Topics Identified:** {len(by_topic)}\n\n')
    f.write('---\n\n')

    f.write('## Topic Summary\n\n')
    f.write('| Topic | Tasks | Status Distribution |\n')
    f.write('|-------|-------|---------------------|\n')

    # Sort topics by task count (descending)
    sorted_topics = sorted(by_topic.items(), key=lambda x: len(x[1]), reverse=True)

    for topic, topic_tasks in sorted_topics:
        completed = sum(1 for t in topic_tasks if t['task_status'] == 'completed')
        new = sum(1 for t in topic_tasks if t['task_status'] == 'new')
        f.write(f'| {topic} | {len(topic_tasks)} | ✅ {completed}, 🆕 {new} |\n')

    f.write('\n---\n\n')

    # Detailed topic sections
    for topic, topic_tasks in sorted_topics:
        f.write(f'## Topic: {topic}\n\n')
        f.write(f'**Total Tasks:** {len(topic_tasks)}\n')

        # Departments involved
        depts = set(t['department'] for t in topic_tasks)
        f.write(f'**Departments:** {", ".join(sorted(depts))}\n')

        # Employees involved
        employees = set(t['employee'] for t in topic_tasks)
        f.write(f'**Employees:** {", ".join(sorted(employees))}\n')

        # Projects mapped
        projects = set(t['project'] for t in topic_tasks)
        f.write(f'**Projects:** {", ".join(sorted(projects))}\n\n')

        # Task list
        f.write('### Task List\n\n')

        for task in topic_tasks:
            task_name = create_task_name(task['description'])
            status_icon = {'completed': '✅', 'in_progress': '🔄', 'new': '🆕', 'blocked': '⏸️'}.get(task['task_status'], '❓')

            f.write(f'**{task["id"]}** | {status_icon} | {task_name}\n')
            f.write(f'└─ *Employee:* {task["employee"]} | *Project:* {task["project"]}\n\n')

        f.write('---\n\n')

    # Recommendations section
    f.write('## Validation Recommendations\n\n')

    f.write('### Topics to KEEP (Core Work)\n\n')
    keep_topics = [
        'Strapi CMS Integration',
        'Mascot Design System',
        'AI Tool Support',
        'Data Scraping & Collection',
        'Lead Generation & CRM',
        'Calendar Management',
        'System Optimization',
        'AI Agent Development',
        'Script Automation',
        'UI/UX Improvements',
        'Black Friday Campaign'
    ]

    for topic in keep_topics:
        if topic in [t[0] for t in sorted_topics]:
            count = len(by_topic[topic])
            f.write(f'- ✅ **{topic}** ({count} tasks) - Actual work items\n')

    f.write('\n### Topics to REVIEW/CLEAN\n\n')

    f.write('- ⚠️ **Template/Metadata (Remove)** - Template instructions, not tasks\n')
    f.write('- ⚠️ **Field Labels (Remove)** - Metadata field labels, not tasks\n')
    f.write('- ⚠️ **Technical Specifications** - Consider grouping into requirement docs\n')
    f.write('- ⚠️ **General/Operational** - Review individually for task validity\n')

    f.write('\n---\n\n')
    f.write('*Generated: 2025-11-29*\n')
    f.write('*Next: Review each topic, validate tasks, remove non-tasks*\n')

print(f'Created: {output_file}')
print('')
print('Topics identified:')
for topic, topic_tasks in sorted_topics:
    print(f'  {topic}: {len(topic_tasks)} tasks')
print('')
print('[SUCCESS] Topic view created for validation')
