"""
Analyze Day 28 Tasks to Extract Vocabulary for Clustering

This script analyzes the actual extracted tasks to identify:
1. Common verbs (active vs completed)
2. Common objects/subjects
3. Patterns for clustering
4. Natural groupings
"""

import os
import json
import re
from collections import defaultdict, Counter

# Configuration
INPUT_FILE = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28\Day28_Tasks_v2.json'
OUTPUT_DIR = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\28'

print('=' * 80)
print('TASK VOCABULARY ANALYSIS')
print('=' * 80)
print()

# Load tasks
print('[STEP 1] Loading extracted tasks...')
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

print(f'  Loaded {len(tasks)} items')
print()

# Extract verbs (first word of description)
print('[STEP 2] Extracting verbs and patterns...')

first_words = []
verb_patterns = defaultdict(list)
field_labels = []
section_headers = []
time_stamped = []
questions = []
deliverables = defaultdict(list)

for task in tasks:
    desc = task['description'].strip()

    # Check for field labels (*Field:**)
    if re.match(r'^\*[A-Za-z\s]+\*+:.*', desc):
        field_labels.append(desc)
        continue

    # Check for time stamps
    if re.match(r'^\*\*\d{1,2}:\d{2}', desc):
        time_stamped.append(desc)
        continue

    # Check for questions
    if desc.startswith('"') and '?' in desc:
        questions.append(desc)
        continue

    # Get first word (verb)
    words = re.findall(r'\b\w+\b', desc.lower())
    if words:
        first_word = words[0]
        first_words.append(first_word)
        verb_patterns[first_word].append(desc)

        # Check for deliverable patterns
        # Pattern: "X mascot", "Y document", etc.
        if len(words) >= 2:
            if 'mascot' in words:
                deliverables['mascot'].append(desc)
            elif 'document' in words or 'guide' in words:
                deliverables['documentation'].append(desc)
            elif 'script' in words or 'code' in words:
                deliverables['code'].append(desc)
            elif 'design' in words or 'graphic' in words:
                deliverables['design'].append(desc)

print(f'  First words (verbs): {len(set(first_words))} unique')
print(f'  Field labels found: {len(field_labels)}')
print(f'  Time-stamped entries: {len(time_stamped)}')
print(f'  Questions: {len(questions)}')
print(f'  Deliverable patterns: {sum(len(v) for v in deliverables.values())}')
print()

# Count verb frequency
print('[STEP 3] Analyzing verb frequency...')
verb_counts = Counter(first_words)
top_verbs = verb_counts.most_common(50)

print('  Top 30 verbs:')
for verb, count in top_verbs[:30]:
    try:
        print(f'    {verb}: {count}')
    except UnicodeEncodeError:
        print(f'    [Non-ASCII]: {count}')
print()

# Identify metadata patterns
print('[STEP 4] Identifying metadata patterns...')

metadata_patterns = defaultdict(int)
for desc in field_labels:
    # Extract field name
    match = re.match(r'^\*([A-Za-z\s]+)\*+:', desc)
    if match:
        field_name = match.group(1).strip()
        metadata_patterns[field_name] += 1

print('  Common field labels:')
for field, count in sorted(metadata_patterns.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f'    *{field}**: {count}')
print()

# Find clustering patterns
print('[STEP 5] Finding clustering patterns...')

# Group by employee + section
employee_sections = defaultdict(lambda: defaultdict(list))
for task in tasks:
    emp = task['employee']
    section = task.get('section', 'Unknown')
    employee_sections[emp][section].append(task['description'])

# Find sections with multiple items (potential clusters)
multi_item_sections = []
for emp, sections in employee_sections.items():
    for section, items in sections.items():
        if len(items) > 5:  # More than 5 items in same section
            multi_item_sections.append({
                'employee': emp,
                'section': section,
                'count': len(items),
                'samples': items[:3]
            })

print(f'  Sections with 5+ items (potential clusters): {len(multi_item_sections)}')
for cluster in sorted(multi_item_sections, key=lambda x: x['count'], reverse=True)[:10]:
    try:
        print(f'    {cluster["employee"]} - {cluster["section"]}: {cluster["count"]} items')
    except UnicodeEncodeError:
        print(f'    [Cluster]: {cluster["count"]} items')
print()

# Analyze deliverable patterns
print('[STEP 6] Analyzing deliverable patterns...')
for category, items in sorted(deliverables.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'  {category.capitalize()}: {len(items)} items')
    # Skip printing individual items to avoid encoding issues
print()

# Generate vocabulary file
print('[STEP 7] Generating vocabulary file...')

vocabulary = {
    'metadata': {
        'analysis_date': '2025-11-29',
        'source_file': 'Day28_Tasks_v2.json',
        'total_items': len(tasks),
        'unique_verbs': len(set(first_words)),
        'field_labels_found': len(field_labels),
        'time_stamped_entries': len(time_stamped)
    },
    'top_verbs': {
        'active_verbs': [],
        'completed_verbs': [],
        'frequency': {}
    },
    'field_labels': {},
    'deliverable_patterns': {},
    'clustering_opportunities': [],
    'section_based_clusters': []
}

# Classify verbs by likely tense
active_indicators = ['monitor', 'respond', 'help', 'guide', 'document', 'check', 'create',
                     'build', 'develop', 'design', 'analyze', 'investigate', 'research']
completed_indicators = ['monitored', 'responded', 'helped', 'guided', 'documented', 'checked',
                        'created', 'built', 'developed', 'designed', 'analyzed', 'investigated',
                        'implemented', 'added', 'updated', 'sent', 'completed', 'finished']

for verb, count in top_verbs:
    vocabulary['top_verbs']['frequency'][verb] = count

    if verb in active_indicators or not verb.endswith('ed'):
        vocabulary['top_verbs']['active_verbs'].append(verb)

    if verb.endswith('ed') or verb in completed_indicators:
        vocabulary['top_verbs']['completed_verbs'].append(verb)

# Add field labels
for field, count in metadata_patterns.items():
    vocabulary['field_labels'][field] = count

# Add deliverable patterns
for category, items in deliverables.items():
    vocabulary['deliverable_patterns'][category] = {
        'count': len(items),
        'samples': items[:10]
    }

# Add clustering opportunities
for cluster in sorted(multi_item_sections, key=lambda x: x['count'], reverse=True)[:20]:
    vocabulary['clustering_opportunities'].append({
        'employee': cluster['employee'],
        'section': cluster['section'],
        'item_count': cluster['count'],
        'cluster_potential': 'high' if cluster['count'] > 10 else 'medium'
    })

# Save vocabulary
vocab_file = os.path.join(OUTPUT_DIR, 'Task_Vocabulary_Analysis.json')
with open(vocab_file, 'w', encoding='utf-8') as f:
    json.dump(vocabulary, f, indent=2, ensure_ascii=False)

print(f'  Saved: Task_Vocabulary_Analysis.json')
print()

# Generate clustering rules based on actual data
print('[STEP 8] Generating clustering rules from actual data...')

clustering_rules = {
    'generated_from': 'Day28_Tasks_v2.json actual analysis',
    'date': '2025-11-29',
    'rules': {
        'metadata_filtering': {
            'field_labels': list(metadata_patterns.keys()),
            'action': 'FILTER - These are template fields, not tasks'
        },
        'deliverable_clustering': {
            'patterns': {},
            'action': 'CLUSTER - Group similar deliverables into single workflow task'
        },
        'time_based_clustering': {
            'pattern': 'Time-stamped entries (HH:MM format)',
            'count': len(time_stamped),
            'action': 'CLUSTER - Group sequential time entries into daily workflow'
        },
        'section_clustering': {
            'high_potential_sections': [c for c in vocabulary['clustering_opportunities'] if c['cluster_potential'] == 'high'],
            'action': 'CLUSTER - Group items from same employee/section into workflows'
        }
    },
    'task_naming_patterns': {
        'verb_object': 'Extract first verb + main object (e.g., "Monitor Discord" from "Monitor Discord #ai-support channel")',
        'deliverable': 'For deliverables, use category + type (e.g., "Create Mascot Designs" for multiple mascots)'
    }
}

# Add deliverable clustering patterns from actual data
for category, items in deliverables.items():
    if len(items) > 1:
        clustering_rules['rules']['deliverable_clustering']['patterns'][category] = {
            'count': len(items),
            'cluster_name': f'Create {category.capitalize()} Deliverables',
            'samples': items[:5]
        }

rules_file = os.path.join(OUTPUT_DIR, 'Clustering_Rules_From_Data.json')
with open(rules_file, 'w', encoding='utf-8') as f:
    json.dump(clustering_rules, f, indent=2, ensure_ascii=False)

print(f'  Saved: Clustering_Rules_From_Data.json')
print()

print('=' * 80)
print('VOCABULARY ANALYSIS COMPLETE')
print('=' * 80)
print()
print('Files generated:')
print('  1. Task_Vocabulary_Analysis.json - Comprehensive vocabulary from actual data')
print('  2. Clustering_Rules_From_Data.json - Clustering rules based on patterns found')
print()
print(f'Key Findings:')
print(f'  - {len(set(first_words))} unique verbs')
print(f'  - {len(metadata_patterns)} different field label types')
print(f'  - {len(deliverables)} deliverable categories with multiple items')
print(f'  - {len([c for c in multi_item_sections if c["count"] > 10])} high-potential clusters')
