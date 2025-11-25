#!/usr/bin/env python3
"""
Extract Action+Object pairs from Task Manager files
Phase 1.1 of Responsibilities Architecture Merge
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Paths
TASK_MANAGERS_ROOT = Path(r"C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS")
OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities")

def normalize_text(text):
    """Normalize text for comparison"""
    if not text:
        return ""
    return text.lower().strip()

def extract_from_task_template(file_path):
    """Extract action+object pairs from a task template JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        pairs = []

        # Task-level action+object
        if 'action' in data and 'object' in data:
            pair = {
                'action': normalize_text(data['action']),
                'object': normalize_text(data['object']),
                'context': data.get('context', ''),
                'department': data.get('department', 'Unknown'),
                'task_id': data.get('template_id', data.get('task_id', 'Unknown')),
                'task_name': data.get('task_name', ''),
                'source_file': str(file_path),
                'level': 'task'
            }
            pairs.append(pair)

        # Step-level actions
        if 'steps' in data and isinstance(data['steps'], list):
            for step in data['steps']:
                if isinstance(step, dict) and 'action' in step:
                    step_pair = {
                        'action': normalize_text(step['action']),
                        'object': normalize_text(step.get('name', step.get('object', ''))),
                        'context': '',
                        'department': data.get('department', 'Unknown'),
                        'task_id': data.get('template_id', data.get('task_id', 'Unknown')),
                        'step_number': step.get('step_number', ''),
                        'source_file': str(file_path),
                        'level': 'step'
                    }
                    pairs.append(step_pair)

        return pairs

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def find_task_template_files():
    """Find all task template JSON files"""
    template_files = []

    # Check multiple locations
    search_paths = [
        TASK_MANAGERS_ROOT / "Task_Templates",
        TASK_MANAGERS_ROOT / "Task_Templates" / "By_Department",
    ]

    for search_path in search_paths:
        if search_path.exists():
            for json_file in search_path.rglob("*.json"):
                # Skip listing files and deprecated
                if 'Listing.json' not in str(json_file) and 'DEPRECATED' not in str(json_file).upper():
                    template_files.append(json_file)

    return template_files

def main():
    """Main extraction process"""
    print("=" * 60)
    print("Phase 1.1: Extracting Action+Object Pairs")
    print("=" * 60)

    # Find all task template files
    template_files = find_task_template_files()
    print(f"\nFound {len(template_files)} task template files")

    # Extract all pairs
    all_pairs = []
    for file_path in template_files:
        pairs = extract_from_task_template(file_path)
        all_pairs.extend(pairs)

    print(f"Extracted {len(all_pairs)} total action+object pairs")

    # Group by department
    by_department = defaultdict(list)
    for pair in all_pairs:
        by_department[pair['department']].append(pair)

    print(f"\nPairs by department:")
    for dept, pairs in sorted(by_department.items()):
        print(f"  {dept}: {len(pairs)} pairs")

    # Find unique combinations
    unique_combinations = defaultdict(lambda: {'count': 0, 'examples': []})
    for pair in all_pairs:
        key = f"{pair['action']} + {pair['object']}"
        unique_combinations[key]['count'] += 1
        unique_combinations[key]['examples'].append({
            'task_id': pair['task_id'],
            'department': pair['department'],
            'level': pair['level']
        })

    print(f"\nUnique action+object combinations: {len(unique_combinations)}")

    # Save all pairs
    output_file = OUTPUT_DIR / "extracted_pairs_raw.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_pairs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved all pairs to: {output_file}")

    # Save unique combinations with frequency
    unique_output = OUTPUT_DIR / "unique_combinations.json"
    unique_data = [
        {
            'combination': key,
            'action': key.split(' + ')[0],
            'object': key.split(' + ')[1],
            'frequency': data['count'],
            'examples': data['examples'][:5]  # Keep first 5 examples
        }
        for key, data in sorted(unique_combinations.items(), key=lambda x: x[1]['count'], reverse=True)
    ]

    with open(unique_output, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, indent=2, ensure_ascii=False)
    print(f"Saved unique combinations to: {unique_output}")

    # Print top 20 most frequent
    print("\nTop 20 most frequent combinations:")
    for i, item in enumerate(unique_data[:20], 1):
        print(f"  {i:2d}. {item['combination']:40s} ({item['frequency']:2d}x) - {item['examples'][0]['department']}")

    print("\n" + "=" * 60)
    print("Phase 1.1 Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
