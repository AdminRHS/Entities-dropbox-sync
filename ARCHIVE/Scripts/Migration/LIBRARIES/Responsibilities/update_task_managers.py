#!/usr/bin/env python3
"""
Update Task Manager files with responsibility_id references
Phase 3 of Responsibilities Architecture Merge
"""

import json
from pathlib import Path
from collections import defaultdict

RESP_DIR = Path(r"C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities")
TASK_MANAGERS_ROOT = Path(r"C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS")

def load_phrase_index():
    """Load the phrase matching index"""
    with open(RESP_DIR / "phrase_matching_index.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def load_responsibilities():
    """Load all responsibilities for reference"""
    with open(RESP_DIR / "responsibilities_master.json", 'r', encoding='utf-8') as f:
        responsibilities = json.load(f)

    # Create lookup by ID
    return {r['id']: r for r in responsibilities}

def find_responsibility(action, obj, phrase_index):
    """Find responsibility ID for action+object pair"""
    action = action.lower().strip() if action else ""
    obj = obj.lower().strip() if obj else ""

    # Try exact match
    key = f"{action}+{obj}"
    if key in phrase_index:
        return phrase_index[key]

    # Try without object (for step-level actions that don't have explicit objects)
    if not obj:
        # Look for any responsibility with this action
        for phrase_key, resp_info in phrase_index.items():
            if phrase_key.startswith(action + "+"):
                return resp_info

    return None

def update_task_template(file_path, phrase_index, responsibilities):
    """Update a single task template file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        updated = False
        mapping_log = {
            'file': str(file_path),
            'task_id': data.get('template_id', data.get('task_id', 'Unknown')),
            'task_level_mapping': None,
            'step_mappings': []
        }

        # Update task-level action+object
        if 'action' in data and 'object' in data:
            resp_info = find_responsibility(data['action'], data['object'], phrase_index)
            if resp_info:
                # Add responsibility_id field
                data['responsibility_id'] = resp_info['responsibility_id']
                data['responsibility_name'] = resp_info['primary_phrase']

                # Keep original fields for now (validation)
                data['_original_action'] = data['action']
                data['_original_object'] = data['object']

                mapping_log['task_level_mapping'] = {
                    'action': data['action'],
                    'object': data['object'],
                    'responsibility_id': resp_info['responsibility_id'],
                    'responsibility_name': resp_info['primary_phrase']
                }
                updated = True

        # Update step-level actions
        if 'steps' in data and isinstance(data['steps'], list):
            for step in data['steps']:
                if isinstance(step, dict) and 'action' in step:
                    step_action = step['action']
                    step_object = step.get('object', step.get('name', ''))

                    resp_info = find_responsibility(step_action, step_object, phrase_index)
                    if resp_info:
                        step['responsibility_id'] = resp_info['responsibility_id']
                        step['responsibility_name'] = resp_info['primary_phrase']
                        step['_original_action'] = step_action

                        mapping_log['step_mappings'].append({
                            'step_number': step.get('step_number', '?'),
                            'action': step_action,
                            'responsibility_id': resp_info['responsibility_id']
                        })
                        updated = True

        if updated:
            # Save updated file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        return mapping_log if updated else None

    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return None

def find_task_template_files():
    """Find all task template JSON files"""
    template_files = []

    search_paths = [
        TASK_MANAGERS_ROOT / "Task_Templates",
        TASK_MANAGERS_ROOT / "Task_Templates" / "By_Department",
    ]

    for search_path in search_paths:
        if search_path.exists():
            for json_file in search_path.rglob("*.json"):
                if 'Listing.json' not in str(json_file) and 'DEPRECATED' not in str(json_file).upper():
                    template_files.append(json_file)

    return template_files

def main():
    print("=" * 60)
    print("Phase 3: Update Task Managers with responsibility_id")
    print("=" * 60)

    # Load phrase index and responsibilities
    print("\nLoading responsibilities...")
    phrase_index = load_phrase_index()
    responsibilities = load_responsibilities()
    print(f"Loaded {len(responsibilities)} responsibilities")
    print(f"Loaded {len(phrase_index)} phrase lookups")

    # Find task templates
    template_files = find_task_template_files()
    print(f"\nFound {len(template_files)} task template files")

    # Update all files
    all_mappings = []
    updated_count = 0
    error_count = 0

    for file_path in template_files:
        mapping_log = update_task_template(file_path, phrase_index, responsibilities)
        if mapping_log:
            all_mappings.append(mapping_log)
            updated_count += 1
            print(f"  Updated: {file_path.name}")
        else:
            error_count += 1

    # Save mapping log
    log_file = RESP_DIR / "task_manager_migration_log.json"
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(all_mappings, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("Phase 3 Complete!")
    print("=" * 60)
    print(f"\nResults:")
    print(f"  Files processed: {len(template_files)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files skipped: {error_count}")
    print(f"  Total mappings: {len(all_mappings)}")
    print(f"\nMigration log saved to: {log_file}")

    # Show sample mappings
    if all_mappings:
        print(f"\nSample mappings (first 5):")
        for i, mapping in enumerate(all_mappings[:5], 1):
            print(f"\n  {i}. {mapping['task_id']}")
            if mapping['task_level_mapping']:
                tlm = mapping['task_level_mapping']
                print(f"     Task: {tlm['action']} + {tlm['object']}")
                print(f"     --> {tlm['responsibility_id']}: {tlm['responsibility_name']}")
            if mapping['step_mappings']:
                print(f"     Steps: {len(mapping['step_mappings'])} updated")

if __name__ == "__main__":
    main()
