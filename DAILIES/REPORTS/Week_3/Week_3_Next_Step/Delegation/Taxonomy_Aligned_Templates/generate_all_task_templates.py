import csv
import json
import os
import re

# Department mapping (CRITICAL: Use AID not AIA)
DEPT_MAP = {
    'AI': 'AID',
    'Design': 'DGN',
    'Development': 'DEV',
    'Finance': 'FIN',
    'HR': 'HRM',
    'Lead Generation': 'LGN',
    'Sales': 'SLS',
    'SMM': 'SMM',
    'Video': 'VID'
}

def convert_department(dept_name):
    """Convert department name to ISO code"""
    return DEPT_MAP.get(dept_name, dept_name)

def is_simple_task_id(task_id):
    """Check if task ID is simple numeric TSK-### format"""
    if not task_id.startswith('TSK-'):
        return False
    suffix = task_id[4:]
    return suffix.isdigit()

def convert_task_id(task_id):
    """Convert TSK-### to TST-###"""
    if is_simple_task_id(task_id):
        return 'TST-' + task_id[4:]
    return task_id

def sanitize_filename(name):
    """Create safe filename from task name"""
    # Remove/replace invalid characters
    safe = re.sub(r'[<>:"/\\|?*]', '', name)
    safe = safe.replace(' ', '_')
    # Limit length
    if len(safe) > 100:
        safe = safe[:100]
    return safe

def create_task_template(task_data):
    """Create TAX-002 compliant task template"""
    task_id = task_data['Task_ID']
    tst_id = convert_task_id(task_id)

    # Extract numeric ID
    numeric_id = tst_id[4:] if tst_id.startswith('TST-') else task_id[4:]

    template = {
        "entity_type": "TASK_MANAGERS",
        "sub_entity": "Task_Template",
        "template_id": f"Task-Template-{numeric_id}",
        "task_template_id": tst_id,
        "metadata": {
            "task_name": task_data['Task_Name'],
            "description": task_data['Task_Name'],
            "department": convert_department(task_data['Reclassified_Department']),
            "category": task_data['Category'],
            "priority": task_data['Priority'],
            "complexity": task_data.get('Complexity_Score', 'Medium'),
            "status": "Active",
            "estimated_duration": task_data.get('Estimated_Duration', 'TBD'),
            "business_impact": task_data.get('Business_Impact', 'Medium'),
            "created_date": "2025-11-26",
            "version": "1.0"
        },
        "execution": {
            "matched_template": task_data.get('Matched_Template', 'CUSTOM'),
            "quick_win": task_data.get('Quick_Win_Flag', '').lower() == 'yes',
            "blocking_dependencies": task_data.get('Blocking_Dependencies', '').split(', ') if task_data.get('Blocking_Dependencies') else []
        },
        "assignment": {
            "assigned_to": task_data.get('Assigned_To', 'TBD'),
            "queue_position": task_data.get('Queue_Position', '')
        },
        "steps": [],
        "tags": [
            task_data['Category'].lower() if task_data['Category'] else 'task',
            convert_department(task_data['Reclassified_Department']).lower()
        ],
        "version": "1.0",
        "created": "2025-11-26",
        "last_updated": "2025-11-26",
        "migration_notes": {
            "original_id": task_id,
            "converted_from": "Task_Template_Mapping.csv",
            "conversion_date": "2025-11-26",
            "source": "Week 3 Task Mapping"
        }
    }

    return template

def main():
    # Paths
    input_csv = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Task_Template_Mapping.csv'
    output_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates\Task_Templates'

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read CSV
    print("Reading Task_Template_Mapping.csv...")
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        all_tasks = list(reader)

    print(f"Total tasks in CSV: {len(all_tasks)}")

    # Filter to simple numeric tasks only
    simple_tasks = [t for t in all_tasks if is_simple_task_id(t['Task_ID'])]
    print(f"Simple numeric TSK-### tasks: {len(simple_tasks)}")

    # Track excluded tasks
    excluded_tasks = [t for t in all_tasks if not is_simple_task_id(t['Task_ID'])]
    excluded_patterns = {}
    for task in excluded_tasks:
        task_id = task['Task_ID']
        if task_id.startswith('TSK-'):
            # Extract pattern (e.g., TSK-DEV-2025-11-20-001 -> DEV-date-based)
            parts = task_id.split('-')
            if len(parts) > 2:
                pattern = f"{parts[1]}-date-based"
            else:
                pattern = "Other"
        else:
            prefix = task_id.split('-')[0]
            pattern = f"{prefix} (already correct)"
        excluded_patterns[pattern] = excluded_patterns.get(pattern, 0) + 1

    print("\nExcluded task patterns:")
    for pattern, count in sorted(excluded_patterns.items()):
        print(f"  - {pattern}: {count} tasks")

    # Generate templates
    print(f"\nGenerating {len(simple_tasks)} task templates...")
    generated = 0
    errors = []

    for task in simple_tasks:
        try:
            # Create template
            template = create_task_template(task)
            tst_id = template['task_template_id']

            # Create filename
            safe_name = sanitize_filename(task['Task_Name'])
            filename = f"{tst_id}_{safe_name}.json"
            filepath = os.path.join(output_dir, filename)

            # Write JSON
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2, ensure_ascii=False)

            generated += 1

            if generated % 50 == 0:
                print(f"  Generated {generated}/{len(simple_tasks)} templates...")

        except Exception as e:
            errors.append(f"{task['Task_ID']}: {str(e)}")

    # Summary
    print("\n" + "="*60)
    print("GENERATION COMPLETE")
    print("="*60)
    print(f"Total tasks processed: {len(all_tasks)}")
    print(f"Simple numeric tasks: {len(simple_tasks)}")
    print(f"Templates generated: {generated}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\nErrors encountered:")
        for error in errors[:10]:  # Show first 10
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

    # Create summary file
    summary = {
        "generation_date": "2025-11-26",
        "total_tasks_in_csv": len(all_tasks),
        "simple_numeric_tasks": len(simple_tasks),
        "templates_generated": generated,
        "excluded_task_patterns": excluded_patterns,
        "errors": errors,
        "output_directory": output_dir,
        "department_mapping": DEPT_MAP,
        "conversion_pattern": "TSK-### -> TST-###"
    }

    summary_path = os.path.join(output_dir, '_GENERATION_SUMMARY.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\nSummary saved to: {summary_path}")
    print(f"Templates saved to: {output_dir}")

if __name__ == "__main__":
    main()
