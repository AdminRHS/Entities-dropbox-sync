"""
Generate Proper Workflow Names

Analyze workflow items to create meaningful, descriptive names
"""

import os
import json
import re
from collections import Counter

# Configuration
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final_Clean\Day28_Workflows_Clean.json'
OUTPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Final_Clean\Day28_Workflows_Named.json'

print('=' * 80)
print('GENERATING PROPER WORKFLOW NAMES')
print('=' * 80)
print()

# Load workflows
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    workflows = json.load(f)

print(f'Loaded {len(workflows)} workflows\n')

# Ukrainian to English translations
TRANSLATIONS = {
    'Основні задачі': 'Main Tasks',
    'Зв\'язатися': 'Contact',
    'Обговорити': 'Discuss',
    'з Колею': 'with Kolya',
    'з розробниками': 'with Developers',
    'День планування': 'Planning Day',
    'Strapi Workflow пояснення': 'Strapi Workflow Explanation',
    'з HR командою': 'with HR Team',
    'Code Review': 'Code Review',
    'Завершення': 'Completion',
    'доработал': 'finalized',
    'інструкцію': 'instruction',
    'мастер-промт': 'master prompt',
    'графики': 'graphics',
}

def translate(text):
    """Translate Ukrainian to English"""
    for ukr, eng in TRANSLATIONS.items():
        text = text.replace(ukr, eng)
    return text

def extract_workflow_theme(items):
    """Extract main theme from workflow items"""

    # Collect all descriptions
    descriptions = [item.get('description', '') for item in items]

    # Extract key nouns/objects (common multi-word patterns)
    key_terms = []

    for desc in descriptions:
        # Clean
        desc = translate(desc)
        desc = re.sub(r'\*+', '', desc)

        # Extract significant phrases
        # Look for: "X script", "X system", "X workflow", etc.
        patterns = [
            r'(\w+\s+(?:script|system|workflow|guide|documentation|automation|export|import|update|sync))',
            r'(Strapi\s+\w+)',
            r'(Google\s+\w+)',
            r'(AI\s+\w+)',
            r'(\w+\s+support)',
            r'(\w+\s+design)',
            r'(\w+\s+review)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, desc, re.IGNORECASE)
            key_terms.extend(matches)

    # Count frequency
    if key_terms:
        term_counts = Counter([t.lower() for t in key_terms])
        most_common = term_counts.most_common(3)
        return [term for term, count in most_common]

    return []

def generate_workflow_name(workflow):
    """Generate descriptive workflow name"""

    employee = workflow['employee']
    section = workflow.get('section', '')
    items = workflow.get('items', [])

    # Get themes from items
    themes = extract_workflow_theme(items)

    # Clean section name
    section_clean = section
    section_clean = re.sub(r'#+ ', '', section_clean)
    section_clean = re.sub(r'\[\d{1,2}:\d{2}-\d{1,2}:\d{2}\]', '', section_clean)
    section_clean = re.sub(r'\d{1,2}:\d{2}-\d{1,2}:\d{2}', '', section_clean)
    section_clean = re.sub(r'\[|\]', '', section_clean)
    section_clean = re.sub(r'\*\*', '', section_clean)
    section_clean = re.sub(r'[0-9]️⃣\s*', '', section_clean)
    section_clean = translate(section_clean)
    section_clean = ' '.join(section_clean.split())

    # Build name
    name_parts = []

    # Add employee
    name_parts.append(employee)

    # Add theme if found
    if themes:
        # Use first theme
        theme = themes[0].title()
        name_parts.append(theme)
    elif section_clean and section_clean not in ['Morning', 'Afternoon', 'Day']:
        # Use section if meaningful
        name_parts.append(section_clean[:40])
    else:
        # Fallback: try to extract from first few items
        sample_items = items[:3]
        sample_text = ' '.join([item.get('description', '')[:50] for item in sample_items])

        # Look for key action verbs
        verbs = re.findall(r'\b(creat|build|develop|design|implement|updat|fix|review|document|analyz|optimiz|refactor|test|deploy|monitor)\w*\b',
                          sample_text, re.IGNORECASE)

        if verbs:
            action = verbs[0].title()
            name_parts.append(f"{action} Work")
        else:
            name_parts.append("Daily Work")

    name = ' - '.join(name_parts)

    # Truncate if too long
    if len(name) > 70:
        name = name[:67] + '...'

    return name

# Generate names
print('Generating workflow names...\n')

for i, workflow in enumerate(workflows, 1):
    old_name = workflow['name']
    new_name = generate_workflow_name(workflow)

    workflow['name'] = new_name
    workflow['name_original'] = old_name

    try:
        print(f'{i:2d}. {workflow["id"]}')
        print(f'    Old: {old_name[:60]}')
        print(f'    New: {new_name[:60]}')
    except UnicodeEncodeError:
        print(f'{i:2d}. {workflow["id"]} - [Updated]')
    print()

# Save
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(workflows, f, indent=2, ensure_ascii=False)

print('=' * 80)
print(f'Saved {len(workflows)} workflows with proper names')
print(f'Output: Day28_Workflows_Named.json')
print('=' * 80)
