#!/usr/bin/env python3
"""
Validate the Responsibilities architecture migration
Phase 4 of Responsibilities Architecture Merge
"""

import json
from pathlib import Path
from collections import defaultdict

RESP_DIR = Path(r"C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities")
TASK_MANAGERS_ROOT = Path(r"C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS")

def load_responsibilities():
    """Load all responsibilities"""
    with open(RESP_DIR / "responsibilities_master.json", 'r', encoding='utf-8') as f:
        responsibilities = json.load(f)
    return {r['id']: r for r in responsibilities}

def validate_task_template(file_path, responsibilities):
    """Validate a single task template"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        issues = []
        stats = {
            'has_responsibility_id': False,
            'responsibility_valid': False,
            'steps_with_responsibility': 0,
            'steps_total': 0
        }

        # Check task-level responsibility_id
        if 'responsibility_id' in data:
            stats['has_responsibility_id'] = True
            resp_id = data['responsibility_id']

            if resp_id in responsibilities:
                stats['responsibility_valid'] = True
            else:
                issues.append(f"Invalid responsibility_id: {resp_id}")

        # Check steps
        if 'steps' in data and isinstance(data['steps'], list):
            stats['steps_total'] = len(data['steps'])
            for step in data['steps']:
                if isinstance(step, dict) and 'responsibility_id' in step:
                    stats['steps_with_responsibility'] += 1
                    resp_id = step['responsibility_id']
                    if resp_id not in responsibilities:
                        issues.append(f"Invalid step responsibility_id: {resp_id}")

        return stats, issues

    except Exception as e:
        return None, [f"Error reading file: {e}"]

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
    print("Phase 4: Validation & Reporting")
    print("=" * 60)

    # Load responsibilities
    print("\nLoading responsibilities...")
    responsibilities = load_responsibilities()
    print(f"Loaded {len(responsibilities)} responsibilities")

    # Find and validate all templates
    template_files = find_task_template_files()
    print(f"Found {len(template_files)} task template files")

    # Validation statistics
    total_stats = {
        'files_processed': 0,
        'files_with_errors': 0,
        'files_with_responsibility': 0,
        'files_with_valid_responsibility': 0,
        'total_steps': 0,
        'steps_with_responsibility': 0
    }

    all_issues = []
    responsibility_usage = defaultdict(int)

    print("\nValidating files...")
    for file_path in template_files:
        stats, issues = validate_task_template(file_path, responsibilities)

        if stats is None:
            total_stats['files_with_errors'] += 1
            all_issues.append({
                'file': str(file_path),
                'issues': issues
            })
            continue

        total_stats['files_processed'] += 1

        if stats['has_responsibility_id']:
            total_stats['files_with_responsibility'] += 1

        if stats['responsibility_valid']:
            total_stats['files_with_valid_responsibility'] += 1

            # Track responsibility usage
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'responsibility_id' in data:
                        responsibility_usage[data['responsibility_id']] += 1
            except:
                pass

        total_stats['total_steps'] += stats['steps_total']
        total_stats['steps_with_responsibility'] += stats['steps_with_responsibility']

        if issues:
            all_issues.append({
                'file': str(file_path),
                'issues': issues
            })

    # Print validation report
    print("\n" + "=" * 60)
    print("VALIDATION REPORT")
    print("=" * 60)

    print(f"\nFile Statistics:")
    print(f"  Total files found: {len(template_files)}")
    print(f"  Files processed: {total_stats['files_processed']}")
    print(f"  Files with errors: {total_stats['files_with_errors']}")
    print(f"  Files with responsibility_id: {total_stats['files_with_responsibility']}")
    print(f"  Files with valid responsibility_id: {total_stats['files_with_valid_responsibility']}")

    print(f"\nStep Statistics:")
    print(f"  Total steps: {total_stats['total_steps']}")
    print(f"  Steps with responsibility_id: {total_stats['steps_with_responsibility']}")
    if total_stats['total_steps'] > 0:
        coverage = (total_stats['steps_with_responsibility'] / total_stats['total_steps']) * 100
        print(f"  Coverage: {coverage:.1f}%")

    print(f"\nResponsibility Usage:")
    print(f"  Total responsibilities: {len(responsibilities)}")
    print(f"  Responsibilities in use: {len(responsibility_usage)}")
    print(f"  Unused responsibilities: {len(responsibilities) - len(responsibility_usage)}")

    # Top 10 most used responsibilities
    print(f"\nTop 10 most used responsibilities:")
    for i, (resp_id, count) in enumerate(sorted(responsibility_usage.items(), key=lambda x: x[1], reverse=True)[:10], 1):
        resp = responsibilities[resp_id]
        print(f"  {i:2d}. {resp_id:15s} - {resp['primary_phrase']:30s} ({count:2d} uses)")

    # Issues summary
    if all_issues:
        print(f"\nIssues found: {len(all_issues)}")
        for issue in all_issues[:10]:  # Show first 10
            print(f"\n  File: {Path(issue['file']).name}")
            for issue_msg in issue['issues']:
                print(f"    - {issue_msg}")
    else:
        print(f"\nNo issues found! ✓")

    # Save validation report
    report = {
        'validation_date': '2025-11-16',
        'statistics': total_stats,
        'responsibility_usage': dict(responsibility_usage),
        'issues': all_issues
    }

    report_file = RESP_DIR / "validation_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nValidation report saved to: {report_file}")

    # Generate usage report
    usage_data = []
    for resp_id, resp in responsibilities.items():
        usage_data.append({
            'id': resp_id,
            'primary_phrase': resp['primary_phrase'],
            'department': resp['primary_department'],
            'usage_count': responsibility_usage.get(resp_id, 0),
            'is_used': resp_id in responsibility_usage
        })

    usage_data.sort(key=lambda x: x['usage_count'], reverse=True)

    usage_file = RESP_DIR / "responsibility_usage_report.json"
    with open(usage_file, 'w', encoding='utf-8') as f:
        json.dump(usage_data, f, indent=2, ensure_ascii=False)
    print(f"Usage report saved to: {usage_file}")

    print("\n" + "=" * 60)
    print("Phase 4 Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
