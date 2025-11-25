import json
from pathlib import Path

# Configuration
entities_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES')
output_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\Milestone_04_Relationship_Validation')

print("="*60)
print("MILESTONE 4: RELATIONSHIP VALIDATION")
print("="*60)

# TASK 1: Extract cross-references
print("\n[TASK 1] Extracting cross-references...")

references = {
    'tasks_to_steps': [],
    'milestones_to_tasks': [],
    'projects_to_milestones': []
}

reference_fields = {
    'Task_Templates': {'step_templates': 'tasks_to_steps'},
    'Milestone_Templates': {'task_templates': 'milestones_to_tasks'},
    'Project_Templates': {'milestone_templates': 'projects_to_milestones'}
}

for json_file in entities_path.rglob('*.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        entity_type = None
        for part in json_file.parts:
            if part in reference_fields:
                entity_type = part
                break

        if entity_type:
            for field, ref_type in reference_fields[entity_type].items():
                if field in data and isinstance(data[field], list):
                    for item in data[field]:
                        if isinstance(item, dict):
                            for key, value in item.items():
                                if '_template_id' in key or '_id' in key:
                                    references[ref_type].append({
                                        'source': str(json_file.relative_to(entities_path)),
                                        'target_id': value
                                    })
                                    break
                        elif isinstance(item, str):
                            references[ref_type].append({
                                'source': str(json_file.relative_to(entities_path)),
                                'target_id': item
                            })
    except Exception as e:
        pass

with open(output_path / 'reference_map.json', 'w') as f:
    json.dump(references, f, indent=2)

total_refs = sum(len(refs) for refs in references.values())
print(f"Cross-references: {total_refs}")
for ref_type, refs in references.items():
    print(f"  {ref_type}: {len(refs)}")

# TASK 2: Validate references
print("\n[TASK 2] Validating references...")

existing_ids = {'steps': set(), 'tasks': set(), 'milestones': set(), 'projects': set()}

for json_file in entities_path.rglob('*.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key, value in data.items():
            if isinstance(value, str) and key.endswith('_id'):
                if 'STEP' in value:
                    existing_ids['steps'].add(value)
                elif 'TASK' in value:
                    existing_ids['tasks'].add(value)
                elif 'MIL' in value:
                    existing_ids['milestones'].add(value)
                elif 'PROJ' in value:
                    existing_ids['projects'].add(value)
    except:
        pass

print(f"Indexed IDs:")
for id_type, ids in existing_ids.items():
    print(f"  {id_type}: {len(ids)}")

broken_references = []
ref_map = {'tasks_to_steps': 'steps', 'milestones_to_tasks': 'tasks', 'projects_to_milestones': 'milestones'}

for ref_type, refs in references.items():
    for ref in refs:
        if ref['target_id'] not in existing_ids[ref_map[ref_type]]:
            broken_references.append({
                'type': ref_type,
                'source': ref['source'],
                'target': ref['target_id'],
                'severity': 'critical'
            })

with open(output_path / 'broken_references.json', 'w') as f:
    json.dump(broken_references, f, indent=2)

print(f"Broken references: {len(broken_references)}")

# TASK 3: Index files
print("\n[TASK 3] Checking indexes...")

index_files = list(entities_path.rglob('INDEX.md')) + list(entities_path.rglob('*Listing*.md'))
print(f"Index files found: {len(index_files)}")

with open(output_path / 'index_files.json', 'w') as f:
    json.dump([str(f.relative_to(entities_path)) for f in index_files], f, indent=2)

summary = {
    'references': total_refs,
    'broken': len(broken_references),
    'indexes': len(index_files)
}

with open(output_path / 'milestone_04_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*60)
print("MILESTONE 4 COMPLETE")
print("="*60)
print("\nFiles created:")
print("  - reference_map.json")
print("  - broken_references.json")
print("  - index_files.json")
print("  - milestone_04_summary.json")
