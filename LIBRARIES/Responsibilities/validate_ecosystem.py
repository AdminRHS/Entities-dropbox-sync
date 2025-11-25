"""
Validate the Responsibilities Ecosystem structure
Checks all directories exist, files are accessible, and JSON files are valid
"""
import json
import os
from pathlib import Path

# Base directory
SCRIPT_DIR = Path(__file__).resolve().parent
ENTITIES_DIR = SCRIPT_DIR.parent.parent

# Expected structure
EXPECTED_STRUCTURE = {
    "LIBRARIES/Responsibilities": {
        "dirs": ["Actions", "Objects", "Parameters", "Core"],
        "files": ["README.md", "responsibilities.json"]
    },
    "LIBRARIES/Responsibilities/Core": {
        "dirs": ["By_Department"],
        "files": [
            "responsibilities_master.json",
            "phrase_matching_index.json",
            "action_variants_map.json",
            "object_variants_map.json"
        ]
    },
    "LIBRARIES/Responsibilities/Actions": {
        "files": ["action_variants.json"]
    },
    "LIBRARIES/Responsibilities/Objects": {
        "files": ["objects_taxonomy.json"]
    },
    "LIBRARIES/Responsibilities/Parameters": {
        "files": []  # Will check file count
    }
}

def check_directory_exists(rel_path):
    """Check if directory exists"""
    full_path = ENTITIES_DIR / rel_path
    exists = full_path.exists() and full_path.is_dir()
    return exists, full_path

def check_file_exists(rel_path):
    """Check if file exists and is readable"""
    full_path = ENTITIES_DIR / rel_path
    exists = full_path.exists() and full_path.is_file()
    return exists, full_path

def validate_json_file(file_path):
    """Validate JSON file can be parsed"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def count_files_in_directory(rel_path, extension=None):
    """Count files in directory"""
    full_path = ENTITIES_DIR / rel_path
    if not full_path.exists():
        return 0

    count = 0
    for root, dirs, files in os.walk(full_path):
        for file in files:
            if extension is None or file.endswith(extension):
                count += 1
    return count

def main():
    print("=" * 70)
    print("Validating Responsibilities Ecosystem Structure")
    print(f"ENTITIES Directory: {ENTITIES_DIR}")
    print("=" * 70)

    issues = []
    successes = []

    # Validate directory structure
    print("\n[1] Checking Directory Structure")
    print("-" * 70)

    for rel_dir, expected in EXPECTED_STRUCTURE.items():
        # Check main directory
        exists, full_path = check_directory_exists(rel_dir)
        if exists:
            print(f"[OK] {rel_dir}")
            successes.append(f"Directory exists: {rel_dir}")
        else:
            print(f"[FAIL] {rel_dir} - NOT FOUND")
            issues.append(f"Missing directory: {rel_dir}")
            continue

        # Check subdirectories
        for subdir in expected.get("dirs", []):
            sub_rel = f"{rel_dir}/{subdir}"
            exists, sub_full = check_directory_exists(sub_rel)
            if exists:
                print(f"  [OK] {subdir}/")
                successes.append(f"Subdirectory exists: {sub_rel}")
            else:
                print(f"  [FAIL] {subdir}/ - NOT FOUND")
                issues.append(f"Missing subdirectory: {sub_rel}")

        # Check files
        for file in expected.get("files", []):
            file_rel = f"{rel_dir}/{file}"
            exists, file_full = check_file_exists(file_rel)
            if exists:
                # Validate JSON files
                if file.endswith('.json'):
                    valid, error = validate_json_file(file_full)
                    if valid:
                        print(f"  [OK] {file}")
                        successes.append(f"File valid: {file_rel}")
                    else:
                        print(f"  [FAIL] {file} - JSON INVALID: {error}")
                        issues.append(f"Invalid JSON: {file_rel} - {error}")
                else:
                    print(f"  [OK] {file}")
                    successes.append(f"File exists: {file_rel}")
            else:
                print(f"  [FAIL] {file} - NOT FOUND")
                issues.append(f"Missing file: {file_rel}")

    # Count files in each directory
    print("\n[2] File Counts")
    print("-" * 70)

    actions_count = count_files_in_directory("LIBRARIES/Responsibilities/Actions", ".json")
    objects_count = count_files_in_directory("LIBRARIES/Responsibilities/Objects", ".json")
    parameters_count = count_files_in_directory("LIBRARIES/Responsibilities/Parameters", ".json")

    print(f"Actions: {actions_count} JSON files")
    print(f"Objects: {objects_count} JSON files")
    print(f"Parameters: {parameters_count} JSON files")

    if actions_count > 0:
        successes.append(f"Actions directory has {actions_count} files")
    else:
        issues.append("Actions directory is empty or missing JSON files")

    if objects_count > 0:
        successes.append(f"Objects directory has {objects_count} files")
    else:
        issues.append("Objects directory is empty or missing JSON files")

    if parameters_count > 0:
        successes.append(f"Parameters directory has {parameters_count} files")
    else:
        issues.append("Parameters directory is empty or missing JSON files")

    # Validate Core integration files
    print("\n[3] Validating Core Integration Files")
    print("-" * 70)

    core_files = [
        "responsibilities_master.json",
        "phrase_matching_index.json",
        "action_variants_map.json",
        "object_variants_map.json"
    ]

    for file in core_files:
        file_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Core" / file
        if file_path.exists():
            valid, error = validate_json_file(file_path)
            if valid:
                # Get file size
                size_kb = file_path.stat().st_size / 1024
                print(f"[OK] {file} ({size_kb:.1f} KB)")
                successes.append(f"Core file valid: {file}")
            else:
                print(f"[FAIL] {file} - JSON INVALID: {error}")
                issues.append(f"Invalid core file: {file} - {error}")
        else:
            print(f"[FAIL] {file} - NOT FOUND")
            issues.append(f"Missing core file: {file}")

    # Validate By_Department structure
    print("\n[4] Validating By_Department Structure")
    print("-" * 70)

    by_dept_dir = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Core" / "By_Department"
    if by_dept_dir.exists():
        dept_files = list(by_dept_dir.glob("*.json"))
        print(f"Found {len(dept_files)} department files")

        for dept_file in sorted(dept_files):
            valid, error = validate_json_file(dept_file)
            if valid:
                print(f"  [OK] {dept_file.name}")
                successes.append(f"Department file valid: {dept_file.name}")
            else:
                print(f"  [FAIL] {dept_file.name} - JSON INVALID: {error}")
                issues.append(f"Invalid department file: {dept_file.name} - {error}")
    else:
        print(f"[FAIL] By_Department directory not found")
        issues.append("Missing By_Department directory")

    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total Successes: {len(successes)}")
    print(f"Total Issues: {len(issues)}")

    if issues:
        print("\n[ISSUES FOUND]")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n[ALL CHECKS PASSED]")

    # Save validation report
    report = {
        "validation_date": Path(__file__).stat().st_mtime,
        "entities_directory": str(ENTITIES_DIR),
        "successes": successes,
        "issues": issues,
        "file_counts": {
            "actions": actions_count,
            "objects": objects_count,
            "parameters": parameters_count,
            "department_files": len(dept_files) if by_dept_dir.exists() else 0
        }
    }

    report_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "ecosystem_validation_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f"\nValidation report saved: ecosystem_validation_report.json")
    print("=" * 70)

    return len(issues) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
