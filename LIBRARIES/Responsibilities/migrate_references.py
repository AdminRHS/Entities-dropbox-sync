"""
Migrate all path references from old structure to new Responsibilities ecosystem
Updates Task_Templates, Step_Templates, Workflows, and project_instance.json files
Uses relative paths from Dropbox\ENTITIES\ directory
"""
import json
import os
from pathlib import Path
import re
import time

# Base directory - find Dropbox\ENTITIES\ dynamically
SCRIPT_DIR = Path(__file__).resolve().parent
ENTITIES_DIR = SCRIPT_DIR.parent.parent  # Go up to ENTITIES from LIBRARIES/Responsibilities

# Path mappings using relative paths from ENTITIES
PATH_MAPPINGS = {
    # Backslash paths
    r"LIBRARIES\Actions": r"LIBRARIES\Responsibilities\Actions",
    r"LIBRARIES\Objects": r"LIBRARIES\Responsibilities\Objects",
    r"LIBRARIES\Parameters": r"LIBRARIES\Responsibilities\Parameters",
    r"LIBRARIES\Responsibilities\responsibilities_master.json": r"LIBRARIES\Responsibilities\Core\responsibilities_master.json",
    r"LIBRARIES\Responsibilities\phrase_matching_index.json": r"LIBRARIES\Responsibilities\Core\phrase_matching_index.json",
    r"LIBRARIES\Responsibilities\action_variants_map.json": r"LIBRARIES\Responsibilities\Core\action_variants_map.json",
    r"LIBRARIES\Responsibilities\object_variants_map.json": r"LIBRARIES\Responsibilities\Core\object_variants_map.json",
    r"LIBRARIES\Responsibilities\By_Department": r"LIBRARIES\Responsibilities\Core\By_Department",

    # Forward slash paths
    r"LIBRARIES/Actions": r"LIBRARIES/Responsibilities/Actions",
    r"LIBRARIES/Objects": r"LIBRARIES/Responsibilities/Objects",
    r"LIBRARIES/Parameters": r"LIBRARIES/Responsibilities/Parameters",
    r"LIBRARIES/Responsibilities/responsibilities_master.json": r"LIBRARIES/Responsibilities/Core/responsibilities_master.json",
    r"LIBRARIES/Responsibilities/phrase_matching_index.json": r"LIBRARIES/Responsibilities/Core/phrase_matching_index.json",
    r"LIBRARIES/Responsibilities/action_variants_map.json": r"LIBRARIES/Responsibilities/Core/action_variants_map.json",
    r"LIBRARIES/Responsibilities/object_variants_map.json": r"LIBRARIES/Responsibilities/Core/object_variants_map.json",
    r"LIBRARIES/Responsibilities/By_Department": r"LIBRARIES/Responsibilities/Core/By_Department",

    # Also handle absolute paths for completeness
    str(ENTITIES_DIR / "LIBRARIES" / "Actions").replace("\\", "\\\\"): str(ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Actions").replace("\\", "\\\\"),
    str(ENTITIES_DIR / "LIBRARIES" / "Objects").replace("\\", "\\\\"): str(ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Objects").replace("\\", "\\\\"),
    str(ENTITIES_DIR / "LIBRARIES" / "Parameters").replace("\\", "\\\\"): str(ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "Parameters").replace("\\", "\\\\"),
}

# Directories to scan (relative to ENTITIES)
SCAN_DIRECTORIES = [
    "TASK_MANAGERS\\Task_Templates",
    "TASK_MANAGERS\\Step_Templates",
    "TASK_MANAGERS\\Workflows",
]

def replace_paths_in_string(content):
    """Replace all old paths with new paths in a string"""
    modified = False
    for old_path, new_path in PATH_MAPPINGS.items():
        if old_path in content:
            content = content.replace(old_path, new_path)
            modified = True
    return content, modified

def update_json_file(file_path, max_retries=3):
    """Update paths in a JSON file"""
    for attempt in range(max_retries):
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace paths
            new_content, modified = replace_paths_in_string(content)

            if not modified:
                return "unchanged"

            # Validate JSON
            try:
                json.loads(new_content)
            except json.JSONDecodeError as e:
                print(f"[ERROR] JSON validation failed for {Path(file_path).name}: {e}")
                return "error"

            # Write back
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)

            return "updated"

        except PermissionError:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                return "locked"
        except Exception as e:
            print(f"[ERROR] Error updating {Path(file_path).name}: {e}")
            return "error"

    return "error"

def update_yaml_file(file_path, max_retries=3):
    """Update paths in a YAML file"""
    for attempt in range(max_retries):
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace paths
            new_content, modified = replace_paths_in_string(content)

            if not modified:
                return "unchanged"

            # Write back
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)

            return "updated"

        except PermissionError:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                return "locked"
        except Exception as e:
            print(f"[ERROR] Error updating {Path(file_path).name}: {e}")
            return "error"

    return "error"

def scan_and_update_directory(directory_rel):
    """Scan directory and update all JSON and YAML files"""
    stats = {
        "total": 0,
        "updated": 0,
        "unchanged": 0,
        "locked": 0,
        "error": 0
    }

    directory = ENTITIES_DIR / directory_rel
    if not directory.exists():
        print(f"[SKIP] Directory not found: {directory_rel}")
        return stats

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file

            # Process JSON files
            if file.endswith('.json'):
                stats["total"] += 1
                result = update_json_file(file_path)
                stats[result] += 1

                rel_path = file_path.relative_to(directory)
                if result == "updated":
                    print(f"[OK] Updated: {rel_path}")
                elif result == "error":
                    print(f"[FAIL] Error: {rel_path}")
                elif result == "locked":
                    print(f"[FAIL] Locked: {rel_path}")

            # Process YAML files
            elif file.endswith(('.yaml', '.yml')):
                stats["total"] += 1
                result = update_yaml_file(file_path)
                stats[result] += 1

                rel_path = file_path.relative_to(directory)
                if result == "updated":
                    print(f"[OK] Updated: {rel_path}")
                elif result == "error":
                    print(f"[FAIL] Error: {rel_path}")
                elif result == "locked":
                    print(f"[FAIL] Locked: {rel_path}")

    return stats

def main():
    print("=" * 70)
    print("Migrating Path References to New Responsibilities Ecosystem")
    print(f"ENTITIES Directory: {ENTITIES_DIR}")
    print("=" * 70)

    overall_stats = {
        "total": 0,
        "updated": 0,
        "unchanged": 0,
        "locked": 0,
        "error": 0
    }

    for directory_rel in SCAN_DIRECTORIES:
        print(f"\nScanning: {directory_rel}")
        print("-" * 70)

        stats = scan_and_update_directory(directory_rel)

        # Aggregate stats
        for key in overall_stats:
            overall_stats[key] += stats[key]

        print(f"\nDirectory Stats: {stats['updated']} updated, {stats['unchanged']} unchanged, "
              f"{stats['locked']} locked, {stats['error']} errors")

    print("\n" + "=" * 70)
    print(f"Overall Summary:")
    print(f"  Total files: {overall_stats['total']}")
    print(f"  Updated: {overall_stats['updated']}")
    print(f"  Unchanged: {overall_stats['unchanged']}")
    print(f"  Locked: {overall_stats['locked']}")
    print(f"  Errors: {overall_stats['error']}")
    print("=" * 70)

    # Save migration report
    report = {
        "migration_date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "entities_directory": str(ENTITIES_DIR),
        "path_mappings": {k: v for k, v in PATH_MAPPINGS.items() if not k.startswith("C:")},
        "directories_scanned": SCAN_DIRECTORIES,
        "statistics": overall_stats
    }

    report_path = ENTITIES_DIR / "LIBRARIES" / "Responsibilities" / "migration_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f"\nMigration report saved: migration_report.json")

if __name__ == "__main__":
    main()
