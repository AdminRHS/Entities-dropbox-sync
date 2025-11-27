import json
import os
from collections import defaultdict

# Valid department codes from TAX-002
VALID_DEPARTMENTS = ['AID', 'DGN', 'DEV', 'FIN', 'HRM', 'LGN', 'SLS', 'SMM', 'VID']

# Required fields for TAX-002 Task Template
REQUIRED_FIELDS = {
    'root': ['entity_type', 'sub_entity', 'template_id', 'task_template_id', 'metadata',
             'execution', 'assignment', 'steps', 'tags', 'version', 'created',
             'last_updated', 'migration_notes'],
    'metadata': ['task_name', 'description', 'department', 'category', 'priority',
                 'complexity', 'status', 'estimated_duration', 'created_date', 'version'],
    'execution': ['matched_template', 'quick_win', 'blocking_dependencies'],
    'assignment': ['assigned_to', 'queue_position'],
    'migration_notes': ['original_id', 'converted_from', 'conversion_date']
}

def validate_template(filepath):
    """Validate a single template against TAX-002 requirements"""
    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            template = json.load(f)
    except json.JSONDecodeError as e:
        return [f"JSON Parse Error: {e}"], []
    except Exception as e:
        return [f"File Read Error: {e}"], []

    # Check root fields
    for field in REQUIRED_FIELDS['root']:
        if field not in template:
            errors.append(f"Missing root field: {field}")

    # Check entity_type
    if template.get('entity_type') != 'TASK_MANAGERS':
        errors.append(f"Invalid entity_type: {template.get('entity_type')}, should be TASK_MANAGERS")

    # Check sub_entity
    if template.get('sub_entity') != 'Task_Template':
        errors.append(f"Invalid sub_entity: {template.get('sub_entity')}, should be Task_Template")

    # Check metadata fields
    metadata = template.get('metadata', {})
    for field in REQUIRED_FIELDS['metadata']:
        if field not in metadata:
            errors.append(f"Missing metadata field: {field}")

    # Validate department code
    dept = metadata.get('department')
    if dept and dept not in VALID_DEPARTMENTS:
        errors.append(f"Invalid department code: {dept}, valid codes: {', '.join(VALID_DEPARTMENTS)}")

    # Specifically check for AIA mistake
    if dept == 'AIA':
        errors.append("CRITICAL: Using AIA instead of AID for AI department")

    # Check execution fields
    execution = template.get('execution', {})
    for field in REQUIRED_FIELDS['execution']:
        if field not in execution:
            errors.append(f"Missing execution field: {field}")

    # Check assignment fields
    assignment = template.get('assignment', {})
    for field in REQUIRED_FIELDS['assignment']:
        if field not in assignment:
            errors.append(f"Missing assignment field: {field}")

    # Check migration_notes fields
    migration = template.get('migration_notes', {})
    for field in REQUIRED_FIELDS['migration_notes']:
        if field not in migration:
            errors.append(f"Missing migration_notes field: {field}")

    # Check ID consistency
    task_id = template.get('task_template_id', '')
    template_id = template.get('template_id', '')

    if task_id.startswith('TST-'):
        expected_template_id = f"Task-Template-{task_id[4:]}"
        if template_id != expected_template_id:
            warnings.append(f"template_id mismatch: {template_id} vs expected {expected_template_id}")

    # Check migration notes
    original_id = migration.get('original_id', '')
    if original_id.startswith('TSK-') and task_id.startswith('TST-'):
        if original_id[4:] != task_id[4:]:
            errors.append(f"ID conversion mismatch: {original_id} → {task_id}")

    # Check tags include department
    tags = template.get('tags', [])
    if dept:
        dept_tag = dept.lower()
        if dept_tag not in tags:
            warnings.append(f"Department tag '{dept_tag}' missing from tags: {tags}")

    # Check version consistency
    root_version = template.get('version')
    meta_version = metadata.get('version')
    if root_version != meta_version:
        warnings.append(f"Version mismatch: root={root_version}, metadata={meta_version}")

    # Check dates
    created = template.get('created')
    last_updated = template.get('last_updated')
    created_date = metadata.get('created_date')

    if created != created_date:
        warnings.append(f"Date mismatch: created={created}, created_date={created_date}")

    return errors, warnings

def main():
    templates_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates\Task_Templates'

    # Get all template files
    files = [f for f in os.listdir(templates_dir) if f.endswith('.json') and f.startswith('TST-')]

    print(f"Validating {len(files)} task templates...")
    print("="*60)

    # Track results
    results = {
        'total': len(files),
        'valid': 0,
        'with_errors': 0,
        'with_warnings': 0,
        'critical_errors': []
    }

    all_errors = defaultdict(int)
    all_warnings = defaultdict(int)
    files_with_errors = []
    files_with_warnings = []

    for filename in sorted(files):
        filepath = os.path.join(templates_dir, filename)
        errors, warnings = validate_template(filepath)

        if errors:
            results['with_errors'] += 1
            files_with_errors.append((filename, errors))
            for error in errors:
                all_errors[error] += 1
                if 'CRITICAL' in error or 'AIA' in error:
                    results['critical_errors'].append(f"{filename}: {error}")
        elif warnings:
            results['with_warnings'] += 1
            files_with_warnings.append((filename, warnings))
        else:
            results['valid'] += 1

        for warning in warnings:
            all_warnings[warning] += 1

    # Print summary
    print("\nVALIDATION SUMMARY")
    print("="*60)
    print(f"Total Templates: {results['total']}")
    print(f"Valid (no errors/warnings): {results['valid']}")
    print(f"With Errors: {results['with_errors']}")
    print(f"With Warnings Only: {results['with_warnings']}")
    print(f"Critical Errors: {len(results['critical_errors'])}")

    # Print critical errors
    if results['critical_errors']:
        print("\n" + "!"*60)
        print("CRITICAL ERRORS (MUST FIX)")
        print("!"*60)
        for error in results['critical_errors'][:10]:
            print(f"  {error}")
        if len(results['critical_errors']) > 10:
            print(f"  ... and {len(results['critical_errors']) - 10} more")

    # Print common errors
    if all_errors:
        print("\nCOMMON ERRORS")
        print("="*60)
        for error, count in sorted(all_errors.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  [{count}x] {error}")

    # Print common warnings
    if all_warnings:
        print("\nCOMMON WARNINGS")
        print("="*60)
        for warning, count in sorted(all_warnings.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  [{count}x] {warning}")

    # Show sample errors
    if files_with_errors:
        print("\nSAMPLE FILES WITH ERRORS")
        print("="*60)
        for filename, errors in files_with_errors[:5]:
            print(f"\n{filename}:")
            for error in errors[:3]:
                print(f"  - {error}")
            if len(errors) > 3:
                print(f"  ... and {len(errors) - 3} more")

    # Save detailed report
    report = {
        'summary': results,
        'error_counts': dict(all_errors),
        'warning_counts': dict(all_warnings),
        'files_with_errors': [
            {'file': f, 'errors': e} for f, e in files_with_errors
        ],
        'files_with_warnings': [
            {'file': f, 'warnings': w} for f, w in files_with_warnings
        ]
    }

    report_path = os.path.join(
        os.path.dirname(templates_dir),
        'VALIDATION_REPORT.json'
    )
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nDetailed report saved to: {report_path}")

    # Return exit code
    if results['critical_errors']:
        print("\nVALIDATION FAILED: Critical errors found!")
        return 1
    elif results['with_errors']:
        print("\nVALIDATION PASSED WITH ERRORS")
        return 0
    else:
        print("\nVALIDATION PASSED")
        return 0

if __name__ == "__main__":
    exit(main())
