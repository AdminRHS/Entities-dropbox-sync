#!/usr/bin/env python3
"""
TOOLS Library Restructuring Script
Purpose: Complete flat migration with TOL-### IDs and master CSV creation
Date: November 26, 2025
"""

import os
import json
import shutil
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

# Configuration
TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
ARCHIVE_DIR = TOOLS_ROOT / "_ARCHIVE" / "pre_migration_2025-11-26"
CSV_OUTPUT = TOOLS_ROOT / "Tools_Master_Inventory.csv"

# Files to exclude from migration
EXCLUDE_FILES = {
    "README.md",
    "MIGRATION_README.md",
    "migrate_tools_to_tol.py",
    "phase4_update_cross_references.py",
    "phase5_rollback_migration.py",
    "run_complete_migration.py",
    "restructure_tools.py",
    "tool_validation_log_2025-11-10.json",
    "Tools_Master_Inventory.csv"
}

# Directories to archive (not to process files from)
DIRECTORIES_TO_ARCHIVE = {
    "AI_Tools",
    "Authentication_Tools",
    "Cloud_Platforms",
    "Data_Tools",
    "Databases",
    "Developer_Platforms",
    "Developer_Tools",
    "File_Management",
    "Freelance_Platforms",
    "Infrastructure_Tools",
    "Integration_Tools",
    "Methodologies",
    "Payment_Tools",
    "Publishing_Platforms",
    "Security_Tools",
    "Web_Tools"
}


def get_all_json_files() -> List[Tuple[str, Path]]:
    """Get all JSON tool files and return alphabetically sorted list with assigned IDs."""
    print("=" * 80)
    print("PHASE 1: Collecting all JSON tool files...")
    print("=" * 80)

    tool_files = []

    # Get all .json files recursively
    for json_file in TOOLS_ROOT.rglob("*.json"):
        # Skip excluded files
        if json_file.name in EXCLUDE_FILES:
            print(f"  [SKIP] {json_file.name} (excluded)")
            continue

        # Skip archive directory
        if "_ARCHIVE" in json_file.parts:
            print(f"  [SKIP] {json_file.name} (in archive)")
            continue

        # Extract tool name from filename
        tool_name = json_file.stem

        # Remove old TOL- prefix if it exists
        if tool_name.startswith("TOL-"):
            parts = tool_name.split("_", 1)
            if len(parts) > 1:
                tool_name = parts[1]

        # Store relative path and name
        relative_path = json_file.relative_to(TOOLS_ROOT)
        tool_files.append((tool_name, json_file, relative_path))
        print(f"  [FOUND] {tool_name} ({relative_path})")

    # Sort alphabetically by tool name
    tool_files.sort(key=lambda x: x[0].lower())

    print(f"\n[OK] Found {len(tool_files)} tool files")
    print("=" * 80)

    return tool_files


def assign_tol_ids(tool_files: List[Tuple[str, Path, Path]]) -> List[Dict]:
    """Assign TOL-### IDs to all tools alphabetically."""
    print("\n" + "=" * 80)
    print("PHASE 2: Assigning TOL-### IDs alphabetically...")
    print("=" * 80)

    tool_mapping = []

    for idx, (tool_name, file_path, relative_path) in enumerate(tool_files, start=1):
        tol_id = f"TOL-{idx:03d}"

        # Determine category from path
        if len(file_path.parts) > len(TOOLS_ROOT.parts):
            parent_dir = file_path.parts[len(TOOLS_ROOT.parts)]
        else:
            parent_dir = "ROOT"

        # Read file to get old tool_id if exists
        old_tool_id = None
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                old_tool_id = data.get('tool_id', None)
        except Exception as e:
            print(f"  [WARNING] Could not read {file_path.name}: {e}")

        mapping = {
            'tol_id': tol_id,
            'tool_name': tool_name,
            'old_tool_id': old_tool_id,
            'old_path': str(relative_path),
            'old_location': parent_dir,
            'current_file_path': file_path,
            'new_filename': f"{tol_id}_{tool_name}.json"
        }

        tool_mapping.append(mapping)
        print(f"  {tol_id} -> {tool_name} (was in {parent_dir})")

    print(f"\n[OK] Assigned {len(tool_mapping)} TOL IDs")
    print("=" * 80)

    return tool_mapping


def migrate_files(tool_mapping: List[Dict]) -> List[Dict]:
    """Migrate all files to root with new naming and update internal tool_id."""
    print("\n" + "=" * 80)
    print("PHASE 3: Migrating files to root...")
    print("=" * 80)

    results = []

    for mapping in tool_mapping:
        old_path = mapping['current_file_path']
        new_filename = mapping['new_filename']
        new_path = TOOLS_ROOT / new_filename
        tol_id = mapping['tol_id']

        try:
            # Read the JSON file
            with open(old_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Update tool_id field
            old_id = data.get('tool_id')
            data['tool_id'] = tol_id

            # Add migration metadata
            data['_migration'] = {
                'date': datetime.now().isoformat(),
                'old_tool_id': old_id,
                'old_path': mapping['old_path'],
                'migrated_by': 'restructure_tools_v1'
            }

            # Write to new location
            with open(new_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # Get file stats
            stats = old_path.stat()

            result = {
                **mapping,
                'new_path': new_path,
                'status': 'SUCCESS',
                'file_size': stats.st_size,
                'modified_date': datetime.fromtimestamp(stats.st_mtime).isoformat()
            }

            results.append(result)
            print(f"  [OK] {tol_id} {mapping['tool_name']}")

        except Exception as e:
            result = {
                **mapping,
                'new_path': None,
                'status': 'FAILED',
                'error': str(e)
            }
            results.append(result)
            print(f"  [FAIL] {tol_id} {mapping['tool_name']} - ERROR: {e}")

    successful = sum(1 for r in results if r['status'] == 'SUCCESS')
    print(f"\n[OK] Migrated {successful}/{len(results)} files successfully")
    print("=" * 80)

    return results


def archive_old_directories():
    """Archive old subdirectories."""
    print("\n" + "=" * 80)
    print("PHASE 4: Archiving old subdirectories...")
    print("=" * 80)

    # Create archive directory
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"  Created archive directory: {ARCHIVE_DIR}")

    archived_count = 0
    for dir_name in DIRECTORIES_TO_ARCHIVE:
        source_dir = TOOLS_ROOT / dir_name
        if source_dir.exists() and source_dir.is_dir():
            dest_dir = ARCHIVE_DIR / dir_name
            try:
                shutil.copytree(source_dir, dest_dir)
                print(f"  [OK] Archived {dir_name}/")
                archived_count += 1
            except Exception as e:
                print(f"  [FAIL] Failed to archive {dir_name}/: {e}")

    print(f"\n[OK] Archived {archived_count} directories")
    print("=" * 80)


def delete_old_files_and_directories(results: List[Dict]):
    """Delete old files from subdirectories and remove empty directories."""
    print("\n" + "=" * 80)
    print("PHASE 5: Cleaning up old files and directories...")
    print("=" * 80)

    deleted_files = 0
    deleted_dirs = 0

    # Delete old files
    for result in results:
        if result['status'] == 'SUCCESS':
            old_file = result['current_file_path']
            try:
                if old_file.exists() and old_file != result['new_path']:
                    old_file.unlink()
                    print(f"  [OK] Deleted old file: {old_file.name}")
                    deleted_files += 1
            except Exception as e:
                print(f"  [FAIL] Failed to delete {old_file.name}: {e}")

    # Remove subdirectories
    for dir_name in DIRECTORIES_TO_ARCHIVE:
        dir_path = TOOLS_ROOT / dir_name
        if dir_path.exists() and dir_path.is_dir():
            try:
                shutil.rmtree(dir_path)
                print(f"  [OK] Removed directory: {dir_name}/")
                deleted_dirs += 1
            except Exception as e:
                print(f"  [FAIL] Failed to remove {dir_name}/: {e}")

    print(f"\n[OK] Deleted {deleted_files} old files and {deleted_dirs} directories")
    print("=" * 80)


def create_master_csv(results: List[Dict]):
    """Create master CSV inventory."""
    print("\n" + "=" * 80)
    print("PHASE 6: Creating master CSV inventory...")
    print("=" * 80)

    headers = [
        'TOL_ID',
        'Tool_Name',
        'Filename',
        'Category',
        'Old_Location',
        'Old_Tool_ID',
        'Old_Path',
        'File_Size_Bytes',
        'Modified_Date',
        'Status',
        'File_Path'
    ]

    try:
        with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for result in results:
                if result['status'] == 'SUCCESS':
                    row = {
                        'TOL_ID': result['tol_id'],
                        'Tool_Name': result['tool_name'],
                        'Filename': result['new_filename'],
                        'Category': result['old_location'],
                        'Old_Location': result['old_location'],
                        'Old_Tool_ID': result.get('old_tool_id', ''),
                        'Old_Path': result['old_path'],
                        'File_Size_Bytes': result.get('file_size', 0),
                        'Modified_Date': result.get('modified_date', ''),
                        'Status': 'Active',
                        'File_Path': str(result['new_path'])
                    }
                    writer.writerow(row)

        print(f"  [OK] Created CSV: {CSV_OUTPUT}")
        print(f"  [OK] Entries: {len([r for r in results if r['status'] == 'SUCCESS'])}")
        print("=" * 80)

    except Exception as e:
        print(f"  [FAIL] Failed to create CSV: {e}")
        print("=" * 80)


def generate_summary_report(results: List[Dict]):
    """Generate final summary report."""
    print("\n" + "=" * 80)
    print("MIGRATION SUMMARY REPORT")
    print("=" * 80)

    total = len(results)
    successful = sum(1 for r in results if r['status'] == 'SUCCESS')
    failed = total - successful

    print(f"Total files processed: {total}")
    print(f"Successfully migrated: {successful}")
    print(f"Failed: {failed}")
    print(f"\nAll files now in: {TOOLS_ROOT}")
    print(f"Master inventory: {CSV_OUTPUT}")
    print(f"Old files archived in: {ARCHIVE_DIR}")

    if failed > 0:
        print(f"\n[WARNING] FAILED FILES:")
        for result in results:
            if result['status'] == 'FAILED':
                print(f"  - {result['tool_name']}: {result.get('error', 'Unknown error')}")

    print("\n" + "=" * 80)
    print("[SUCCESS] MIGRATION COMPLETE!")
    print("=" * 80)


def main():
    """Main execution function."""
    print("\n" + "=" * 80)
    print(" TOOLS LIBRARY RESTRUCTURING")
    print(" Flat Migration with TOL-### IDs")
    print(" Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 80)

    # Phase 1: Collect all JSON files
    tool_files = get_all_json_files()

    # Phase 2: Assign TOL-### IDs
    tool_mapping = assign_tol_ids(tool_files)

    # Phase 3: Migrate files
    results = migrate_files(tool_mapping)

    # Phase 4: Archive old directories
    archive_old_directories()

    # Phase 5: Delete old files and directories
    delete_old_files_and_directories(results)

    # Phase 6: Create master CSV
    create_master_csv(results)

    # Phase 7: Generate summary
    generate_summary_report(results)


if __name__ == "__main__":
    main()
