import json
import re
import ast
from pathlib import Path
from collections import Counter, defaultdict

# Configuration
entities_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES')
output_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\Milestone_03_Content_Analysis')

print("="*60)
print("MILESTONE 3: CONTENT ANALYSIS & TERMINOLOGY EXTRACTION")
print("="*60)

# TASK 1: Extract JSON field names
print("\n[TASK 1] Extracting JSON field names...")

json_fields = Counter()
field_files = defaultdict(list)

def extract_fields_recursive(obj, prefix='', file_path=''):
    """Recursively extract all field names from nested JSON"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            full_key = f"{prefix}.{key}" if prefix else key
            json_fields[key] += 1
            field_files[key].append(file_path)
            extract_fields_recursive(value, full_key, file_path)
    elif isinstance(obj, list):
        for item in obj:
            extract_fields_recursive(item, prefix, file_path)

json_file_count = 0
for json_file in entities_path.rglob('*.json'):
    json_file_count += 1
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            extract_fields_recursive(data, file_path=str(json_file.relative_to(entities_path)))
    except Exception as e:
        pass

# Save JSON field data
with open(output_path / 'json_field_names.json', 'w') as f:
    json.dump({
        'total_unique_fields': len(json_fields),
        'total_json_files': json_file_count,
        'field_frequency': dict(json_fields.most_common(100)),  # Top 100
        'all_fields_sorted': sorted(json_fields.keys())
    }, f, indent=2)

print(f"JSON files analyzed: {json_file_count}")
print(f"Unique field names: {len(json_fields)}")
print(f"\nTop 10 most common fields:")
for field, count in json_fields.most_common(10):
    print(f"  {field:30} {count:5} occurrences")

# TASK 2: Extract Markdown headings
print("\n[TASK 2] Extracting Markdown headings...")

md_headings = defaultdict(list)
heading_pattern = r'^(#{1,6})\s+(.+)$'
md_file_count = 0

for md_file in entities_path.rglob('*.md'):
    md_file_count += 1
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                match = re.match(heading_pattern, line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    md_headings[f'h{level}'].append({
                        'file': str(md_file.relative_to(entities_path)),
                        'line': line_num,
                        'text': text
                    })
    except Exception as e:
        pass

# Save Markdown heading data
with open(output_path / 'markdown_headings.json', 'w') as f:
    json.dump({
        'total_md_files': md_file_count,
        'headings_by_level': {
            level: len(headings) for level, headings in md_headings.items()
        },
        'headings': dict(md_headings)
    }, f, indent=2)

total_headings = sum(len(h) for h in md_headings.values())
print(f"Markdown files analyzed: {md_file_count}")
print(f"Total headings extracted: {total_headings}")
for level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
    if level in md_headings:
        print(f"  {level}: {len(md_headings[level])}")

# TASK 3: Extract entity names from filenames
print("\n[TASK 3] Extracting entity identifiers from filenames...")

entity_patterns = {
    'step_ids': r'STEP-[A-Z]+-\d{3}-\d{2}',
    'task_ids': r'TASK-TEMPLATE-[A-Z]+-\d{3}',
    'milestone_ids': r'MIL-TEMPL-\d{3}',
    'project_ids': r'PROJ-TEMPL-\d{3}',
    'action_ids': r'ACTION-\d{3}'
}

extracted_entities = defaultdict(set)

for file_path in entities_path.rglob('*'):
    filename = file_path.name
    for entity_type, pattern in entity_patterns.items():
        matches = re.findall(pattern, filename)
        for match in matches:
            extracted_entities[entity_type].add(match)

# Convert sets to sorted lists
entity_data = {
    entity_type: sorted(list(ids))
    for entity_type, ids in extracted_entities.items()
}

# Save entity ID data
with open(output_path / 'extracted_entity_ids.json', 'w') as f:
    json.dump({
        'entity_counts': {k: len(v) for k, v in entity_data.items()},
        'entities': entity_data
    }, f, indent=2)

print("Entity IDs extracted from filenames:")
for entity_type, ids in entity_data.items():
    print(f"  {entity_type:20} {len(ids):5}")

# TASK 4: Extract Python script variables
print("\n[TASK 4] Extracting Python script variables...")

python_variables = set()
py_file_count = 0

for py_file in entities_path.rglob('*.py'):
    py_file_count += 1
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                python_variables.add(node.id)
            elif isinstance(node, ast.FunctionDef):
                python_variables.add(node.name)
            elif isinstance(node, ast.ClassDef):
                python_variables.add(node.name)
    except Exception as e:
        pass

# Save Python variable data
with open(output_path / 'python_variables.json', 'w') as f:
    json.dump({
        'python_files_analyzed': py_file_count,
        'unique_variables': len(python_variables),
        'variables': sorted(list(python_variables))
    }, f, indent=2)

print(f"Python files analyzed: {py_file_count}")
print(f"Unique variables/functions: {len(python_variables)}")

# TASK 5: Build comprehensive terminology dictionary
print("\n[TASK 5] Building terminology dictionary...")

# Collect all terms from all sources
all_terms = []

# From JSON fields
all_terms.extend(json_fields.keys())

# From Markdown headings
for level_headings in md_headings.values():
    all_terms.extend([h['text'] for h in level_headings])

# From Python variables
all_terms.extend(python_variables)

# From entity IDs
for ids in entity_data.values():
    all_terms.extend(ids)

# Normalize and find redundant terms
normalized_map = defaultdict(list)

for term in all_terms:
    # Normalize: lowercase, remove special chars
    normalized = re.sub(r'[_\-\s]', '', str(term).lower())
    normalized_map[normalized].append(term)

# Find redundant terms (same normalized form, multiple variations)
redundant_terms = {
    norm: variations
    for norm, variations in normalized_map.items()
    if len(set(variations)) > 1  # Multiple unique variations
}

# Categorize redundancies
redundancy_categories = {
    'case_variations': [],
    'separator_variations': [],
    'other_variations': []
}

for norm, variations in redundant_terms.items():
    unique_vars = list(set(variations))

    # Check if only case differs
    if len(set(v.lower() for v in unique_vars)) == 1:
        redundancy_categories['case_variations'].append(unique_vars)
    # Check if only separators differ
    elif all(re.sub(r'[_\-\s]', '', v.lower()) == norm for v in unique_vars):
        redundancy_categories['separator_variations'].append(unique_vars)
    else:
        redundancy_categories['other_variations'].append(unique_vars)

# Build final terminology dictionary
terminology_dictionary = {
    'metadata': {
        'generated_date': '2025-11-17',
        'total_unique_terms': len(set(all_terms)),
        'sources': {
            'json_fields': len(json_fields),
            'markdown_headings': total_headings,
            'python_variables': len(python_variables),
            'entity_ids': sum(len(ids) for ids in entity_data.values())
        }
    },
    'terminology_by_source': {
        'json_fields': sorted(list(json_fields.keys()))[:200],  # Top 200
        'markdown_heading_samples': [h['text'] for h in md_headings.get('h1', [])[:50]],
        'entity_ids': entity_data,
        'python_variables': sorted(list(python_variables))[:100]
    },
    'redundancy_analysis': {
        'total_redundant_patterns': len(redundant_terms),
        'case_variations_count': len(redundancy_categories['case_variations']),
        'separator_variations_count': len(redundancy_categories['separator_variations']),
        'other_variations_count': len(redundancy_categories['other_variations']),
        'examples': {
            'case_variations': redundancy_categories['case_variations'][:10],
            'separator_variations': redundancy_categories['separator_variations'][:10],
            'other_variations': redundancy_categories['other_variations'][:10]
        }
    },
    'standardization_recommendations': {
        'json_fields': 'Use snake_case (e.g., task_template_id)',
        'entity_ids': 'Use UPPERCASE-WITH-HYPHENS (e.g., STEP-HR-003-01)',
        'avoid_abbreviations': ['desc → description', 'dept → department', 'templ → template']
    }
}

# Save terminology dictionary
with open(output_path / 'terminology_dictionary.json', 'w') as f:
    json.dump(terminology_dictionary, f, indent=2)

# Save complete redundancy list
with open(output_path / 'redundant_terms_full.json', 'w') as f:
    json.dump({
        'case_variations': redundancy_categories['case_variations'],
        'separator_variations': redundancy_categories['separator_variations'],
        'other_variations': redundancy_categories['other_variations']
    }, f, indent=2)

print(f"Total unique terms: {len(set(all_terms))}")
print(f"Redundant patterns found: {len(redundant_terms)}")
print(f"  Case variations: {len(redundancy_categories['case_variations'])}")
print(f"  Separator variations: {len(redundancy_categories['separator_variations'])}")
print(f"  Other variations: {len(redundancy_categories['other_variations'])}")

# Save summary
summary = {
    'json_analysis': {
        'files': json_file_count,
        'unique_fields': len(json_fields)
    },
    'markdown_analysis': {
        'files': md_file_count,
        'total_headings': total_headings
    },
    'entity_extraction': {
        'total_entities': sum(len(ids) for ids in entity_data.items())
    },
    'python_analysis': {
        'files': py_file_count,
        'variables': len(python_variables)
    },
    'terminology': {
        'total_unique_terms': len(set(all_terms)),
        'redundant_patterns': len(redundant_terms),
        'standardization_needed': len(redundancy_categories['case_variations']) + len(redundancy_categories['separator_variations'])
    }
}

with open(output_path / 'milestone_03_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*60)
print("MILESTONE 3 COMPLETE")
print("="*60)
print(f"\nOutputs saved to: {output_path}")
print("Files created:")
print("  - json_field_names.json")
print("  - markdown_headings.json")
print("  - extracted_entity_ids.json")
print("  - python_variables.json")
print("  - terminology_dictionary.json ⭐ KEY DELIVERABLE")
print("  - redundant_terms_full.json")
print("  - milestone_03_summary.json")
