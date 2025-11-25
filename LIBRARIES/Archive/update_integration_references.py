#!/usr/bin/env python3
"""
Integration Reference Update Script
Updates all file paths and references after LBS restructuring
"""

import os
import re
import json
from pathlib import Path

# Base paths
LIBRARIES_PATH = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES")
TALENTS_PATH = Path(r"C:\Users\Dell\Dropbox\ENTITIES\TALENTS")

# Path mappings for the restructuring
PATH_MAPPINGS = {
    # Actions moved to Responsibilities/Actions
    r"Responsibilities/Actions": "Responsibilities/Actions",
    r"LIBRARIES/Responsibilities/Actions": "LIBRARIES/Responsibilities/Actions",
    r"ENTITIES/LIBRARIES/Responsibilities/Actions": "ENTITIES/LIBRARIES/Responsibilities/Actions",

    # Objects moved to Responsibilities/Objects
    r"Responsibilities/Objects": "Responsibilities/Objects",
    r"LIBRARIES/Responsibilities/Objects": "LIBRARIES/Responsibilities/Objects",
    r"ENTITIES/LIBRARIES/Responsibilities/Objects": "ENTITIES/LIBRARIES/Responsibilities/Objects",

    # Parameters moved to Responsibilities/Parameters
    r"Responsibilities/Parameters": "Responsibilities/Parameters",
    r"LIBRARIES/Responsibilities/Parameters": "LIBRARIES/Responsibilities/Parameters",
    r"ENTITIES/LIBRARIES/Responsibilities/Parameters": "ENTITIES/LIBRARIES/Responsibilities/Parameters",

    # Skills moved to TALENTS/Skills
    r"../TALENTS/Skills": "../TALENTS/Skills",
    r"LIBRARIES/../TALENTS/Skills": "../TALENTS/Skills",
    r"ENTITIES/LIBRARIES/../TALENTS/Skills": "ENTITIES/TALENTS/Skills",

    # Taxonomy ID removed
    r"Taxonomy": "Taxonomy",
    r"LIBRARIES/Taxonomy": "LIBRARIES/Taxonomy",
    r"ENTITIES/LIBRARIES/Taxonomy": "ENTITIES/LIBRARIES/Taxonomy",

    # Archive ID removed
    r"Archive": "Archive",
    r"LIBRARIES/Archive": "LIBRARIES/Archive",
    r"ENTITIES/LIBRARIES/Archive": "ENTITIES/LIBRARIES/Archive",
}

def update_file_content(file_path):
    """Update path references in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = []

        # Apply each path mapping
        for old_path, new_path in PATH_MAPPINGS.items():
            # Create regex pattern that matches the old path
            pattern = re.compile(re.escape(old_path), re.IGNORECASE)
            if pattern.search(content):
                content = pattern.sub(new_path, content)
                changes_made.append(f"{old_path} -> {new_path}")

        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made

        return False, []

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def find_files_to_update(root_path, extensions=['.json', '.py', '.md', '.csv']):
    """Find all files that might contain path references"""
    files_to_check = []

    for ext in extensions:
        files_to_check.extend(root_path.rglob(f'*{ext}'))

    return files_to_check

def main():
    """Main migration function"""
    print("=" * 70)
    print("LBS INTEGRATION REFERENCE UPDATE")
    print("=" * 70)
    print()

    # Track statistics
    stats = {
        'files_checked': 0,
        'files_updated': 0,
        'total_changes': 0,
        'errors': 0
    }

    update_log = []

    # Process LIBRARIES folder
    print("Processing LIBRARIES folder...")
    libraries_files = find_files_to_update(LIBRARIES_PATH)

    for file_path in libraries_files:
        # Skip backup directories
        if 'backup' in str(file_path).lower() or 'archive' in str(file_path).lower():
            continue

        stats['files_checked'] += 1
        updated, changes = update_file_content(file_path)

        if updated:
            stats['files_updated'] += 1
            stats['total_changes'] += len(changes)
            update_log.append({
                'file': str(file_path.relative_to(LIBRARIES_PATH)),
                'changes': changes
            })
            print(f"[+] Updated: {file_path.name} ({len(changes)} changes)")

    # Process TALENTS folder
    print("\nProcessing TALENTS folder...")
    if TALENTS_PATH.exists():
        talents_files = find_files_to_update(TALENTS_PATH)

        for file_path in talents_files:
            if 'backup' in str(file_path).lower():
                continue

            stats['files_checked'] += 1
            updated, changes = update_file_content(file_path)

            if updated:
                stats['files_updated'] += 1
                stats['total_changes'] += len(changes)
                update_log.append({
                    'file': str(file_path.relative_to(TALENTS_PATH)),
                    'changes': changes
                })
                print(f"[+] Updated: {file_path.name} ({len(changes)} changes)")

    # Print summary
    print("\n" + "=" * 70)
    print("MIGRATION SUMMARY")
    print("=" * 70)
    print(f"Files checked:    {stats['files_checked']}")
    print(f"Files updated:    {stats['files_updated']}")
    print(f"Total changes:    {stats['total_changes']}")
    print(f"Errors:           {stats['errors']}")
    print()

    # Save detailed log
    log_file = LIBRARIES_PATH / "integration_update_log.json"
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump({
            'statistics': stats,
            'updates': update_log,
            'mappings_applied': PATH_MAPPINGS
        }, f, indent=2)

    print(f"Detailed log saved to: {log_file}")
    print("\n[SUCCESS] Integration reference update complete!")

if __name__ == "__main__":
    main()
