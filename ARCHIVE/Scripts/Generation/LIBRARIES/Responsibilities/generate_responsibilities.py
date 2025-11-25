#!/usr/bin/env python3
"""
Generate responsibility records with array-based schema
Phase 2 of Responsibilities Architecture Merge
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities")
BY_DEPT_DIR = OUTPUT_DIR / "By_Department"

# Department code mapping
DEPT_CODES = {
    'AI': 'AI',
    'LG': 'LG',
    'Dev': 'DEV',
    'OPS': 'OPS',
    'HR': 'HR',
    'Sales': 'SAL',
    'Marketing': 'MKT',
    '': 'CNT'
    'Design': 'DES',
    'ADMIN': 'ADM',
    'E-commerce': 'ECM',
    'Research / AI': 'AI',
    'Research / AI / Design / Video': 'AI',
    'Research / AI / Video': 'AI',
    'Research / Dev': 'DEV'}

def get_dept_code(departments):
    """Get primary department code from list"""
    if not departments:
        return 'GEN'

    # Use first department
    primary = departments[0]
    return DEPT_CODES.get(primary, 'GEN')

def generate_responsibility_id(dept_code, number):
    """Generate responsibility ID"""
    return f"RESP-{dept_code}-{number:03d}"

def main():
    print("=" * 60)
    print("Phase 2: Generate Responsibility Records")
    print("=" * 60)

    # Load phrase combinations
    with open(OUTPUT_DIR / "phrase_combinations.json", 'r', encoding='utf-8') as f:
        combinations = json.load(f)

    print(f"\nLoaded {len(combinations)} phrase combinations")

    # Group by department
    by_department = defaultdict(list)
    for combo in combinations:
        dept_code = get_dept_code(combo['departments'])
        by_department[dept_code].append(combo)

    print(f"\nGrouped into {len(by_department)} departments:")
    for dept, combos in sorted(by_department.items()):
        print(f"  {dept}: {len(combos)} responsibilities")

    # Generate responsibility records
    all_responsibilities = []
    dept_counters = defaultdict(int)

    for dept_code, combos in sorted(by_department.items()):
        for combo in combos:
            dept_counters[dept_code] += 1
            resp_id = generate_responsibility_id(dept_code, dept_counters[dept_code])

            responsibility = {
                "id": resp_id,
                "primary_phrase": combo['primary_phrase'],
                "action_variants": combo['action_variants'],
                "object_variants": combo['object_variants'],
                "action_base": combo['action_base'],
                "object_base": combo['object_base'],
                "departments": combo['departments'],
                "primary_department": combo['departments'][0] if combo['departments'] else "Unknown",
                "typical_tools": [],  # To be populated later
                "object_types": [],   # To be populated later
                "description": f"{combo['action_base'].capitalize()} {combo['object_base']}",
                "frequency": combo['frequency'],
                "usage_examples": combo['examples'],
                "is_active": True,
                "created_at": datetime.now().isoformat(),
                "created_by": "system_migration",
                "version": "1.0"
            }

            all_responsibilities.append(responsibility)

    print(f"\nGenerated {len(all_responsibilities)} responsibility records")

    # Save master file
    master_file = OUTPUT_DIR / "responsibilities_master.json"
    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump(all_responsibilities, f, indent=2, ensure_ascii=False)
    print(f"Saved master file: {master_file}")

    # Create By_Department directory
    BY_DEPT_DIR.mkdir(exist_ok=True)

    # Save department-specific files
    dept_files = defaultdict(list)
    for resp in all_responsibilities:
        dept_code = resp['id'].split('-')[1]  # Extract from RESP-XXX-NNN
        dept_files[dept_code].append(resp)

    for dept_code, responsibilities in sorted(dept_files.items()):
        dept_file = BY_DEPT_DIR / f"{dept_code}_Responsibilities.json"
        with open(dept_file, 'w', encoding='utf-8') as f:
            json.dump(responsibilities, f, indent=2, ensure_ascii=False)
        print(f"Saved {dept_code}: {len(responsibilities)} responsibilities - {dept_file.name}")

    # Create phrase matching index for fast lookup
    phrase_index = {}
    for resp in all_responsibilities:
        # Index by all action+object combinations
        for action_var in resp['action_variants']:
            for object_var in resp['object_variants']:
                key = f"{action_var}+{object_var}".lower()
                phrase_index[key] = {
                    "responsibility_id": resp['id'],
                    "primary_phrase": resp['primary_phrase']
                }

    index_file = OUTPUT_DIR / "phrase_matching_index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(phrase_index, f, indent=2, ensure_ascii=False)
    print(f"\nSaved phrase matching index: {len(phrase_index)} phrase combinations - {index_file.name}")

    # Print statistics
    print("\n" + "=" * 60)
    print("Phase 2 Complete!")
    print("=" * 60)
    print(f"\nFiles created:")
    print(f"  - responsibilities_master.json ({len(all_responsibilities)} responsibilities)")
    print(f"  - phrase_matching_index.json ({len(phrase_index)} phrase lookups)")
    print(f"  - {len(dept_files)} department files in By_Department/")

    print(f"\nResponsibilities by department:")
    for dept_code in sorted(dept_files.keys()):
        count = len(dept_files[dept_code])
        print(f"  {dept_code}: {count:3d} responsibilities")

    # Show sample
    print(f"\nSample responsibilities (first 5):")
    for i, resp in enumerate(all_responsibilities[:5], 1):
        print(f"\n  {i}. {resp['id']}: {resp['primary_phrase']}")
        print(f"     Actions: {', '.join(resp['action_variants'][:3])}")
        print(f"     Objects: {', '.join(resp['object_variants'][:3])}")
        print(f"     Departments: {', '.join(resp['departments'])}")

if __name__ == "__main__":
    main()
