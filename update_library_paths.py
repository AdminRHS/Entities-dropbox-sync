"""
Automated Path Update Script
Updates LIBRARIES path references from old structure to Responsibilities ecosystem
Created: 2025-11-17
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
ENTITIES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES")
TASK_MANAGERS = ENTITIES_DIR / "TASK_MANAGERS"

# Path replacement patterns
REPLACEMENTS = {
    # Legacy root files
    r'LIBRARIES/actions\.json': 'LIBRARIES/Responsibilities/Actions/Actions_Master.json',
    r'LIBRARIES/objects\.json': 'LIBRARIES/Responsibilities/Objects/object_types.json',
    r'LIBRARIES/tools\.json': 'LIBRARIES/Tools/tools_index.json',

    # Folder paths (without trailing slash patterns - more specific)
    r'LIBRARIES/Actions/([a-zA-Z_]+\.json)': r'LIBRARIES/Responsibilities/Actions/\1',
    r'LIBRARIES/Objects/([a-zA-Z_]+\.json)': r'LIBRARIES/Responsibilities/Objects/\1',

    # Generic folder references (with context)
    r'`LIBRARIES/Actions/`': '`LIBRARIES/Responsibilities/Actions/`',
    r'`LIBRARIES/Objects/`': '`LIBRARIES/Responsibilities/Objects/`',
    r'"LIBRARIES/Actions/"': '"LIBRARIES/Responsibilities/Actions/"',
    r'"LIBRARIES/Objects/"': '"LIBRARIES/Responsibilities/Objects/"',

    # Markdown links and documentation
    r'\[Actions library\]': '[Responsibilities/Actions library]',
    r'\[Objects library\]': '[Responsibilities/Objects library]',
    r'Actions library': 'Responsibilities/Actions library',
    r'Objects library': 'Responsibilities/Objects library',

    # Relative paths from TASK_MANAGERS
    r'\.\./\.\./LIBRARIES/Actions/': '../../LIBRARIES/Responsibilities/Actions/',
    r'\.\./\.\./LIBRARIES/Objects/': '../../LIBRARIES/Responsibilities/Objects/',
}

# Additional context-aware replacements (only in specific contexts)
CONTEXT_REPLACEMENTS = {
    'for Actions library': 'for Responsibilities/Actions library',
    'for Objects library': 'for Responsibilities/Objects library',
    'Extracts action verbs for Actions library': 'Extracts action verbs for Responsibilities/Actions library',
    'Identifies deliverables for Objects library': 'Identifies deliverables for Responsibilities/Objects library',
}

def update_file_paths(file_path: Path) -> Tuple[bool, List[str]]:
    """
    Update paths in a single file
    Returns: (changed, list_of_changes)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False, []

    original_content = content
    changes = []

    # Apply all standard replacements
    for old_pattern, new_path in REPLACEMENTS.items():
        matches = list(re.finditer(old_pattern, content))
        if matches:
            content = re.sub(old_pattern, new_path, content)
            changes.append(f"  {old_pattern} → {new_path} ({len(matches)} occurrences)")

    # Apply context-aware replacements
    for old_text, new_text in CONTEXT_REPLACEMENTS.items():
        if old_text in content:
            count = content.count(old_text)
            content = content.replace(old_text, new_text)
            changes.append(f"  '{old_text}' → '{new_text}' ({count} occurrences)")

    # Only write if changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes
        except Exception as e:
            print(f"Error writing {file_path}: {e}")
            return False, []

    return False, []

def scan_and_update(directory: Path, extensions: List[str] = ['.md', '.json']) -> Dict:
    """
    Scan directory and update all matching files
    Returns: statistics dictionary
    """
    stats = {
        'total_files': 0,
        'updated_files': 0,
        'skipped_files': 0,
        'errors': 0,
        'details': []
    }

    for root, dirs, files in os.walk(directory):
        # Skip certain directories
        if 'Archive' in Path(root).parts or 'Legacy' in Path(root).parts:
            continue

        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                stats['total_files'] += 1
                file_path = Path(root) / file

                changed, changes = update_file_paths(file_path)

                if changed:
                    stats['updated_files'] += 1
                    stats['details'].append({
                        'file': str(file_path.relative_to(ENTITIES_DIR)),
                        'changes': changes
                    })
                else:
                    stats['skipped_files'] += 1

    return stats

def validate_paths(directory: Path) -> Dict:
    """
    Validate that no old paths remain
    Returns: validation results
    """
    validation = {
        'old_patterns_found': [],
        'files_with_issues': []
    }

    old_patterns = [
        r'LIBRARIES/actions\.json',
        r'LIBRARIES/objects\.json',
        r'LIBRARIES/Actions/[a-zA-Z]',  # Not followed by README
        r'LIBRARIES/Objects/[a-zA-Z]',  # Not followed by README
    ]

    for root, dirs, files in os.walk(directory):
        # Skip Archive
        if 'Archive' in Path(root).parts:
            continue

        for file in files:
            if file.endswith(('.md', '.json')):
                file_path = Path(root) / file

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    for pattern in old_patterns:
                        if re.search(pattern, content):
                            validation['files_with_issues'].append(str(file_path.relative_to(ENTITIES_DIR)))
                            validation['old_patterns_found'].append(f"{pattern} in {file}")
                            break
                except:
                    pass

    return validation

def main():
    """Main execution function"""
    print("=" * 70)
    print("LIBRARIES Path Update Script")
    print("=" * 70)
    print()
    print("Starting path updates in TASK_MANAGERS...")
    print()

    # Update TASK_MANAGERS/PROMPTS
    stats = scan_and_update(TASK_MANAGERS / "PROMPTS")

    print(f"Scan Complete!")
    print(f"  Total files scanned: {stats['total_files']}")
    print(f"  Files updated: {stats['updated_files']}")
    print(f"  Files skipped (no changes needed): {stats['skipped_files']}")
    print(f"  Errors: {stats['errors']}")
    print()

    if stats['updated_files'] > 0:
        print("=" * 70)
        print("Updated Files Details:")
        print("=" * 70)
        for detail in stats['details']:
            print(f"\n[OK] {detail['file']}")
            for change in detail['changes']:
                print(change)

    print()
    print("=" * 70)
    print("Running Validation...")
    print("=" * 70)

    validation = validate_paths(TASK_MANAGERS / "PROMPTS")

    if validation['files_with_issues']:
        print(f"\n[WARNING] Found {len(validation['files_with_issues'])} files with old path patterns:")
        for file in validation['files_with_issues']:
            print(f"  - {file}")
        print("\nThese may need manual review.")
    else:
        print("\n[SUCCESS] No old path patterns found! All paths updated successfully.")

    print()
    print("=" * 70)
    print("Update Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
