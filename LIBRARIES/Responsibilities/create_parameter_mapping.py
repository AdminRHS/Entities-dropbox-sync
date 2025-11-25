"""
Create parameter_object_mapping.json to map Parameters to Object Types
Links quality metrics from parameters.json to object types from object_types.json
"""
import json
from pathlib import Path
from collections import defaultdict

# Base directory
SCRIPT_DIR = Path(__file__).resolve().parent
ENTITIES_DIR = SCRIPT_DIR.parent.parent

# Load source files
def load_json(rel_path):
    """Load JSON file"""
    file_path = ENTITIES_DIR / rel_path
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def main():
    print("=" * 70)
    print("Creating Parameter-Object Type Mapping")
    print("=" * 70)

    # Load source data
    print("\n[1] Loading source files...")
    parameters_data = load_json("LIBRARIES/Responsibilities/Parameters/parameters.json")
    object_types_data = load_json("LIBRARIES/Responsibilities/Objects/object_types.json")

    print(f"  - Parameters: {parameters_data['metadata']['total_records']} records")
    print(f"  - Object Types: {len(object_types_data)} professions")

    # Build mapping structure
    print("\n[2] Building Parameter-Object Type mapping...")

    # Create index of all object types across all professions
    type_to_objects = defaultdict(list)

    for profession_data in object_types_data:
        profession = profession_data['profession']
        department = profession_data['department']

        for obj_group in profession_data['object_types']:
            obj_name = obj_group['object']

            for obj_type in obj_group['types']:
                type_to_objects[obj_type].append({
                    "profession": profession,
                    "department": department,
                    "object": obj_name,
                    "type": obj_type,
                    "description": obj_group['descriptions'].get(obj_type, "")
                })

    # Map parameters to object types
    parameter_mapping = []
    unmapped_params = []

    for param_entry in parameters_data['data']:
        # Handle potential key variations
        param_type = param_entry.get('Types') or param_entry.get('types') or param_entry.get('Type')
        param_name = param_entry.get('Parameters') or param_entry.get('parameters') or param_entry.get('Parameter')

        if not param_type or not param_name:
            print(f"  [SKIP] Invalid entry: {param_entry}")
            continue

        # Find matching object types
        if param_type in type_to_objects:
            for obj_match in type_to_objects[param_type]:
                parameter_mapping.append({
                    "parameter": param_name,
                    "parameter_type": param_type,
                    "object": obj_match['object'],
                    "object_type": obj_match['type'],
                    "profession": obj_match['profession'],
                    "department": obj_match['department'],
                    "object_type_description": obj_match['description']
                })
        else:
            unmapped_params.append({
                "parameter": param_name,
                "parameter_type": param_type
            })

    print(f"  - Mapped parameters: {len(parameter_mapping)}")
    print(f"  - Unmapped parameters: {len(unmapped_params)}")

    # Build summary statistics
    print("\n[3] Building summary statistics...")

    # Count by profession
    profession_counts = defaultdict(int)
    for mapping in parameter_mapping:
        profession_counts[mapping['profession']] += 1

    # Count by department
    dept_counts = defaultdict(int)
    for mapping in parameter_mapping:
        dept_counts[mapping['department']] += 1

    # Count by object
    object_counts = defaultdict(int)
    for mapping in parameter_mapping:
        object_counts[mapping['object']] += 1

    print(f"\n  Profession distribution:")
    for prof, count in sorted(profession_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"    - {prof}: {count}")

    print(f"\n  Department distribution:")
    for dept, count in sorted(dept_counts.items(), key=lambda x: -x[1]):
        print(f"    - {dept}: {count}")

    # Create output structure
    output = {
        "metadata": {
            "created_date": "2025-11-17",
            "source_files": {
                "parameters": "LIBRARIES/Responsibilities/Parameters/parameters.json",
                "object_types": "LIBRARIES/Responsibilities/Objects/object_types.json"
            },
            "total_mappings": len(parameter_mapping),
            "total_unmapped": len(unmapped_params)
        },
        "statistics": {
            "by_profession": dict(profession_counts),
            "by_department": dict(dept_counts),
            "by_object": dict(object_counts)
        },
        "mappings": parameter_mapping,
        "unmapped_parameters": unmapped_params
    }

    # Save output
    output_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "parameter_object_mapping.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n[4] Mapping saved: parameter_object_mapping.json")

    # Create simplified view by profession
    print("\n[5] Creating profession-specific views...")

    profession_views = defaultdict(lambda: defaultdict(list))

    for mapping in parameter_mapping:
        prof = mapping['profession']
        obj = mapping['object']
        profession_views[prof][obj].append({
            "parameter": mapping['parameter'],
            "type": mapping['object_type'],
            "description": mapping['object_type_description']
        })

    # Save profession views
    views_output = {
        "metadata": {
            "created_date": "2025-11-17",
            "description": "Parameter-Object mappings organized by profession"
        },
        "professions": {}
    }

    for prof, objects in profession_views.items():
        views_output["professions"][prof] = {
            "total_parameters": sum(len(params) for params in objects.values()),
            "objects": dict(objects)
        }

    views_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "parameter_views_by_profession.json"
    with open(views_path, 'w', encoding='utf-8') as f:
        json.dump(views_output, f, indent=2, ensure_ascii=False)

    print(f"  - Profession views saved: parameter_views_by_profession.json")

    print("\n" + "=" * 70)
    print("Parameter-Object Type Mapping Complete")
    print("=" * 70)

if __name__ == "__main__":
    main()
