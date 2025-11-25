import json
import re
from pathlib import Path
from collections import Counter, defaultdict

# Configuration
entities_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES')
output_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\Milestone_02_Schema_Naming')

print("="*60)
print("MILESTONE 2: SCHEMA & NAMING VALIDATION")
print("="*60)

# TASK 1: Naming Convention Audit
print("\n[TASK 1] Auditing naming conventions...")

# Define expected naming patterns
patterns = {
    'step_templates': r'^STEP-[A-Z]+-\d{3}-\d{2}$',
    'task_templates': r'^TASK-TEMPLATE-[A-Z]+-\d{3}$',
    'milestone_templates': r'^MIL-TEMPL-\d{3}$',
    'project_templates': r'^PROJ-TEMPL-\d{3}$'
}

# Scan all JSON files for ID naming
naming_data = []
violations = []
json_count = 0

for json_file in entities_path.rglob('*.json'):
    json_count += 1
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract any ID fields
        for key, value in data.items():
            if isinstance(value, str) and '_template_id' in key:
                # Check pattern match
                matched = False
                for pattern_name, pattern in patterns.items():
                    if re.match(pattern, value):
                        matched = True
                        naming_data.append({
                            'file': str(json_file.relative_to(entities_path)),
                            'field': key,
                            'value': value,
                            'pattern': pattern_name,
                            'valid': True
                        })
                        break

                if not matched:
                    violations.append({
                        'file': str(json_file.relative_to(entities_path)),
                        'field': key,
                        'value': value,
                        'issue': 'Does not match standard template ID pattern',
                        'severity': 'high'
                    })
                    naming_data.append({
                        'file': str(json_file.relative_to(entities_path)),
                        'field': key,
                        'value': value,
                        'pattern': 'no_match',
                        'valid': False
                    })
    except Exception as e:
        pass

# Save naming patterns
with open(output_path / 'naming_patterns.json', 'w') as f:
    json.dump(naming_data, f, indent=2)

with open(output_path / 'naming_violations.json', 'w') as f:
    json.dump(violations, f, indent=2)

print(f"JSON files scanned: {json_count}")
print(f"Template IDs found: {len(naming_data)}")
print(f"Naming violations: {len(violations)}")

# TASK 2: JSON Schema Validation
print("\n[TASK 2] Validating JSON schemas...")

# Define required fields by template type
required_fields = {
    'Task_Templates': {
        'required': ['task_template_id', 'task_template_name'],
        'recommended': ['category', 'department', 'description']
    },
    'Milestone_Templates': {
        'required': ['milestone_template_id', 'name'],
        'recommended': ['task_templates', 'phase']
    },
    'Project_Templates': {
        'required': ['project_template_id', 'template_name'],
        'recommended': ['milestone_templates']
    },
    'Step_Templates': {
        'required': ['step_template_id', 'step_template_name'],
        'recommended': []
    }
}

schema_violations = []
field_usage = defaultdict(Counter)

for json_file in entities_path.rglob('*.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Determine template type from path
        template_type = None
        for part in json_file.parts:
            if part in required_fields:
                template_type = part
                break

        if template_type:
            # Track field usage
            for field in data.keys():
                field_usage[template_type][field] += 1

            # Check required fields
            req_fields = required_fields[template_type]['required']
            missing_required = set(req_fields) - set(data.keys())

            if missing_required:
                schema_violations.append({
                    'file': str(json_file.relative_to(entities_path)),
                    'type': template_type,
                    'missing_required': list(missing_required),
                    'severity': 'critical'
                })

            # Check recommended fields
            rec_fields = required_fields[template_type]['recommended']
            missing_recommended = set(rec_fields) - set(data.keys())

            if missing_recommended:
                schema_violations.append({
                    'file': str(json_file.relative_to(entities_path)),
                    'type': template_type,
                    'missing_recommended': list(missing_recommended),
                    'severity': 'medium'
                })
    except Exception as e:
        pass

# Save schema validation results
with open(output_path / 'schema_violations.json', 'w') as f:
    json.dump(schema_violations, f, indent=2)

# Save field usage stats
field_stats = {
    template_type: dict(fields.most_common())
    for template_type, fields in field_usage.items()
}

with open(output_path / 'field_usage_stats.json', 'w') as f:
    json.dump(field_stats, f, indent=2)

critical_violations = [v for v in schema_violations if v.get('severity') == 'critical']
print(f"Schema violations: {len(schema_violations)}")
print(f"  Critical (missing required fields): {len(critical_violations)}")
print(f"  Medium (missing recommended fields): {len(schema_violations) - len(critical_violations)}")

# TASK 3: Version Control Consistency
print("\n[TASK 3] Checking version control consistency...")

version_data = []
version_issues = []

for json_file in entities_path.rglob('*.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        version = data.get('version')
        last_updated = data.get('last_updated')
        created_date = data.get('created_date')

        if version or last_updated or created_date:
            version_data.append({
                'file': str(json_file.relative_to(entities_path)),
                'version': version,
                'last_updated': last_updated,
                'created_date': created_date,
                'has_version': version is not None,
                'has_dates': last_updated is not None or created_date is not None
            })

            # Validate version format (should be semantic: 1.0 or 1.0.0)
            if version and not re.match(r'^\d+\.\d+(\.\d+)?$', str(version)):
                version_issues.append({
                    'file': str(json_file.relative_to(entities_path)),
                    'issue': 'Invalid version format',
                    'version': version,
                    'expected': 'Semantic versioning (e.g., 1.0, 2.1.3)'
                })
    except Exception as e:
        pass

# Save version data
with open(output_path / 'version_inventory.json', 'w') as f:
    json.dump(version_data, f, indent=2)

with open(output_path / 'version_issues.json', 'w') as f:
    json.dump(version_issues, f, indent=2)

files_with_versions = len([v for v in version_data if v['has_version']])
print(f"Files with versioning: {len(version_data)}")
print(f"  With version field: {files_with_versions}")
print(f"  Version format issues: {len(version_issues)}")

# Save summary
summary = {
    'naming': {
        'total_json_files': json_count,
        'template_ids_found': len(naming_data),
        'violations': len(violations),
        'compliance_rate': round((1 - len(violations) / max(len(naming_data), 1)) * 100, 1) if naming_data else 100
    },
    'schema': {
        'total_violations': len(schema_violations),
        'critical_violations': len(critical_violations),
        'medium_violations': len(schema_violations) - len(critical_violations),
        'template_types_analyzed': list(field_usage.keys())
    },
    'versioning': {
        'files_with_versioning': len(version_data),
        'files_with_version_field': files_with_versions,
        'format_issues': len(version_issues)
    }
}

with open(output_path / 'milestone_02_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*60)
print("MILESTONE 2 COMPLETE")
print("="*60)
print(f"\nOutputs saved to: {output_path}")
print("Files created:")
print("  - naming_patterns.json")
print("  - naming_violations.json")
print("  - schema_violations.json")
print("  - field_usage_stats.json")
print("  - version_inventory.json")
print("  - version_issues.json")
print("  - milestone_02_summary.json")
