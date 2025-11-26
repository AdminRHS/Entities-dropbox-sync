"""
PROMPTS Folder Restructuring Script
- Moves all prompt files to Core folder organized by category
- Moves non-prompt files to _ARCHIVE
- Updates Master CSV with new paths
"""
import os
import shutil
import csv
from pathlib import Path

# Paths
PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
CORE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core"
ARCHIVE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\_ARCHIVE"
MASTER_LIST = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"
BACKUP_CSV = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List_BACKUP.csv"

# Core folder structure
CORE_STRUCTURE = {
    'VIDEO_PROCESSING': 'Video Processing Prompts',
    'HR_OPERATIONS': 'Human Resources Prompts',
    'DAILY_REPORTS': 'Daily Report Prompts',
    'TAXONOMY': 'Taxonomy & System Prompts',
    'WORKFLOWS': 'Workflow & Operations Prompts',
    'AUTOMATION': 'Automation Prompts',
    'RESEARCH': 'Research Prompts',
    'LIBRARY_PROCESSING': 'Library Processing Prompts',
    'CREATIVES': 'Creative & Design Prompts',
    'DATA_ARCHITECTURE': 'Data Architecture Prompts',
    'UTILITIES': 'Utility Prompts',
    'SYSTEM': 'System Prompts',
    'MAIN_PROMPTS': 'Main System Prompts (v4, v5, v6)',
}

# Files to exclude (not prompts)
NON_PROMPT_PATTERNS = [
    'README',
    'INDEX',
    'SUMMARY',
    'TEMPLATE',
    'IMPLEMENTATION',
    'classification',
    'REVERSE_PROMPT',
    'SESSION_LOG',
    'VARIABLE_MAPPING',
    'CHANGELOG',
    'ANALYSIS_REPORT',
    'INCONSISTENCY',
    'FILES_LIST',
    '.py',
    '.ps1',
    '.csv',
    '.json',
]

def is_prompt_file(filepath):
    """Determine if file is a prompt"""
    filename = os.path.basename(filepath).upper()

    # Exclude non-prompt patterns
    for pattern in NON_PROMPT_PATTERNS:
        if pattern in filename:
            return False

    # Must be .md file
    if not filepath.endswith('.md'):
        return False

    # PMT-numbered files are prompts
    if 'PMT-' in filename:
        return True

    # Files with PROMPT in name
    if 'PROMPT' in filename:
        return True

    # Main prompt files
    if 'MAIN_PROMPT' in filename:
        return True

    return True  # Default: .md files are prompts unless excluded

def categorize_prompt(filepath):
    """Determine which Core subfolder a prompt belongs to"""
    path_upper = filepath.upper()

    # MAIN_PROMPTS category
    if 'MAIN_PROMPT' in path_upper or 'CREATE_MAIN' in path_upper:
        return 'MAIN_PROMPTS'

    # Video processing
    if any(x in path_upper for x in ['VIDEO', 'TRANSCRIPTION', 'PMT-004', 'PMT-005', 'PMT-006']):
        return 'VIDEO_PROCESSING'

    # HR Operations
    if any(x in path_upper for x in ['HR_OPERATIONS', 'PMT-053', 'PMT-054', 'PMT-055', 'PMT-056', 'PMT-057', 'CV_PARSER', 'CRM_DATA']):
        return 'HR_OPERATIONS'

    # Daily Reports
    if any(x in path_upper for x in ['DAILY_REPORTS', 'PMT-032', 'PMT-033', 'PMT-034', 'PMT-035', 'PMT-036', 'PMT-037', 'PMT-038', 'PMT-039', 'PMT-040', 'PMT-041', 'PMT-042', 'PMT-043']):
        return 'DAILY_REPORTS'

    # Taxonomy
    if any(x in path_upper for x in ['TAXONOMY', 'PMT-014', 'PMT-015', 'PMT-016', 'PMT-017', 'PMT-018', 'PMT-019', 'PMT-020']):
        return 'TAXONOMY'

    # Data Architecture
    if any(x in path_upper for x in ['DATA_ARCHITECTURE', 'PMT-074', 'PMT-075', 'PMT-076', 'PMT-077', 'PMT-078', 'PMT-079', 'PMT-080']):
        return 'DATA_ARCHITECTURE'

    # Workflows
    if any(x in path_upper for x in ['WORKFLOW', 'PMT-058', 'PMT-059', 'PMT-063', 'PMT-064', 'PMT-065', 'CALL_ORGANIZER', 'DOCUMENT_FINISHED']):
        return 'WORKFLOWS'

    # Automation
    if any(x in path_upper for x in ['AUTOMATION', 'PMT-066', 'PMT-067', 'PMT-068', 'PMT-069', 'AUTOPLANNING']):
        return 'AUTOMATION'

    # Research
    if any(x in path_upper for x in ['RESEARCH', 'YOUTUBE']):
        return 'RESEARCH'

    # Library Processing
    if any(x in path_upper for x in ['LIBRARY_PROCESSING', 'PMT-060', 'PMT-061', 'PMT-062', 'TOOLS_COLLECTION', 'PRODUCTS_INTEGRATION']):
        return 'LIBRARY_PROCESSING'

    # Creatives
    if any(x in path_upper for x in ['CREATIVE', 'PMT-084', 'PMT-086', 'PMT-088', 'PMT-091', 'MASCOT', 'BROCHURE']):
        return 'CREATIVES'

    # Utilities
    if any(x in path_upper for x in ['UTILITIES', 'PMT-070', 'ENTITY_IDENTIFICATION', 'DAILY_UPDATE']):
        return 'UTILITIES'

    # System
    if any(x in path_upper for x in ['SYSTEM', 'PMT-021', 'PMT-022', 'PMT-023', 'PMT-024', 'PMT-025', 'PMT-026', 'PMT-027', 'PMT-028', 'PMT-029', 'PMT-030', 'PMT-031']):
        return 'SYSTEM'

    # Default
    return 'SYSTEM'

def scan_directory():
    """Scan PROMPTS directory and categorize all files"""
    prompt_files = []
    non_prompt_files = []

    for root, dirs, files in os.walk(PROMPTS_DIR):
        # Skip Core and _ARCHIVE directories for source files
        if 'Core' in root or '_ARCHIVE' in root or 'COMPILED_PROMPT_SYSTEM' in root:
            continue

        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, PROMPTS_DIR)

            if is_prompt_file(full_path):
                category = categorize_prompt(full_path)
                prompt_files.append({
                    'source': full_path,
                    'relative': rel_path,
                    'filename': file,
                    'category': category
                })
            else:
                non_prompt_files.append({
                    'source': full_path,
                    'relative': rel_path,
                    'filename': file
                })

    return prompt_files, non_prompt_files

def create_core_structure():
    """Create Core folder structure"""
    print("\nCreating Core folder structure...")

    for folder, description in CORE_STRUCTURE.items():
        folder_path = os.path.join(CORE_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Create README in each subfolder
        readme_path = os.path.join(folder_path, 'README.md')
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {description}\n\n")
                f.write(f"**Category:** {folder}\n\n")
                f.write(f"This folder contains {description.lower()}.\n\n")
                f.write("---\n\n")
                f.write("**Last Updated:** 2025-11-26\n")

    print(f"  Created {len(CORE_STRUCTURE)} category folders")

def move_prompt_files(prompt_files):
    """Move prompt files to Core folder"""
    print(f"\nMoving {len(prompt_files)} prompt files to Core...")
    moved_files = []

    for file_info in prompt_files:
        category = file_info['category']
        dest_folder = os.path.join(CORE_DIR, category)
        dest_path = os.path.join(dest_folder, file_info['filename'])

        # Handle duplicates
        counter = 1
        original_dest = dest_path
        while os.path.exists(dest_path):
            name, ext = os.path.splitext(file_info['filename'])
            dest_path = os.path.join(dest_folder, f"{name}_{counter}{ext}")
            counter += 1

        # Move file
        try:
            shutil.copy2(file_info['source'], dest_path)
            moved_files.append({
                'old_path': file_info['relative'],
                'new_path': os.path.relpath(dest_path, PROMPTS_DIR),
                'category': category
            })
            print(f"  Moved: {file_info['filename']} -> {category}/")
        except Exception as e:
            print(f"  ERROR moving {file_info['filename']}: {str(e)}")

    return moved_files

def move_non_prompt_files(non_prompt_files):
    """Move non-prompt files to _ARCHIVE"""
    print(f"\nMoving {len(non_prompt_files)} non-prompt files to _ARCHIVE...")

    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    for file_info in non_prompt_files:
        # Preserve directory structure in archive
        rel_dir = os.path.dirname(file_info['relative'])
        dest_folder = os.path.join(ARCHIVE_DIR, rel_dir)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, file_info['filename'])

        try:
            shutil.copy2(file_info['source'], dest_path)
            print(f"  Archived: {file_info['relative']}")
        except Exception as e:
            print(f"  ERROR archiving {file_info['filename']}: {str(e)}")

def update_master_csv(moved_files):
    """Update Master CSV with new file paths"""
    print("\nUpdating Master CSV...")

    # Backup original
    shutil.copy2(MASTER_LIST, BACKUP_CSV)
    print(f"  Created backup: {os.path.basename(BACKUP_CSV)}")

    # Read current CSV
    entries = []
    with open(MASTER_LIST, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        entries = list(reader)

    # Create path mapping
    path_map = {}
    for moved in moved_files:
        old_path = f"ENTITIES/PROMPTS/{moved['old_path'].replace(os.sep, '/')}"
        new_path = f"ENTITIES/PROMPTS/{moved['new_path'].replace(os.sep, '/')}"
        path_map[old_path] = new_path

    # Update paths
    updated_count = 0
    for entry in entries:
        old_path = entry['File_Path']
        if old_path in path_map:
            entry['File_Path'] = path_map[old_path]
            updated_count += 1

    # Write updated CSV
    with open(MASTER_LIST, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['New_ID', 'Entity_Type', 'Current_ID', 'Name', 'Description', 'Department', 'File_Path', 'Status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    print(f"  Updated {updated_count} file paths in Master CSV")
    return updated_count

def generate_summary(prompt_files, non_prompt_files, moved_files):
    """Generate restructuring summary"""
    summary_path = os.path.join(PROMPTS_DIR, 'RESTRUCTURING_SUMMARY.md')

    # Count by category
    from collections import Counter
    category_counts = Counter([f['category'] for f in prompt_files])

    content = f"""# PROMPTS Folder Restructuring Summary

**Date:** 2025-11-26
**Total Files Processed:** {len(prompt_files) + len(non_prompt_files)}

---

## Summary

- **Prompt Files Moved to Core:** {len(prompt_files)}
- **Non-Prompt Files Archived:** {len(non_prompt_files)}
- **Categories Created:** {len(CORE_STRUCTURE)}
- **Master CSV Paths Updated:** {len(moved_files)}

---

## Prompts by Category

"""

    for category in sorted(category_counts.keys()):
        category_name = CORE_STRUCTURE.get(category, category)
        count = category_counts[category]
        content += f"- **{category_name}:** {count} files\n"

    content += f"""
---

## Core Folder Structure

```
Core/
├── MAIN_PROMPTS/           ({category_counts.get('MAIN_PROMPTS', 0)} files)
├── VIDEO_PROCESSING/       ({category_counts.get('VIDEO_PROCESSING', 0)} files)
├── HR_OPERATIONS/          ({category_counts.get('HR_OPERATIONS', 0)} files)
├── DAILY_REPORTS/          ({category_counts.get('DAILY_REPORTS', 0)} files)
├── TAXONOMY/               ({category_counts.get('TAXONOMY', 0)} files)
├── DATA_ARCHITECTURE/      ({category_counts.get('DATA_ARCHITECTURE', 0)} files)
├── WORKFLOWS/              ({category_counts.get('WORKFLOWS', 0)} files)
├── AUTOMATION/             ({category_counts.get('AUTOMATION', 0)} files)
├── RESEARCH/               ({category_counts.get('RESEARCH', 0)} files)
├── LIBRARY_PROCESSING/     ({category_counts.get('LIBRARY_PROCESSING', 0)} files)
├── CREATIVES/              ({category_counts.get('CREATIVES', 0)} files)
├── UTILITIES/              ({category_counts.get('UTILITIES', 0)} files)
└── SYSTEM/                 ({category_counts.get('SYSTEM', 0)} files)
```

---

## What Was Done

1. **Scanned** all files in PROMPTS directory (excluding Core and _ARCHIVE)
2. **Categorized** {len(prompt_files)} prompt files by function
3. **Created** {len(CORE_STRUCTURE)} category folders in Core/
4. **Moved** all prompt files to appropriate Core/ subfolders
5. **Archived** {len(non_prompt_files)} non-prompt files to _ARCHIVE/
6. **Updated** Master CSV with new file paths
7. **Preserved** original files (copy operation)

---

## Non-Prompt Files Archived

Files moved to _ARCHIVE/:
"""

    for file_info in sorted(non_prompt_files, key=lambda x: x['relative'])[:20]:
        content += f"- {file_info['relative']}\n"

    if len(non_prompt_files) > 20:
        content += f"- ... and {len(non_prompt_files) - 20} more files\n"

    content += """
---

## Next Steps

1. Review the new Core/ folder structure
2. Verify Master CSV paths are correct
3. Update any hardcoded references to old paths
4. Remove original files from old locations (currently preserved as copies)

---

## Backup

- **Master CSV Backup:** PROMPTS_Master_List_BACKUP.csv

---
"""

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n  Generated summary: {os.path.basename(summary_path)}")

def main():
    """Main restructuring process"""
    print("=" * 60)
    print("PROMPTS FOLDER RESTRUCTURING")
    print("=" * 60)

    # Scan directory
    print("\n[1/6] Scanning PROMPTS directory...")
    prompt_files, non_prompt_files = scan_directory()
    print(f"  Found {len(prompt_files)} prompt files")
    print(f"  Found {len(non_prompt_files)} non-prompt files")

    # Create Core structure
    print("\n[2/6] Creating Core folder structure...")
    create_core_structure()

    # Move prompt files
    print("\n[3/6] Moving prompt files to Core...")
    moved_files = move_prompt_files(prompt_files)

    # Move non-prompt files
    print("\n[4/6] Archiving non-prompt files...")
    move_non_prompt_files(non_prompt_files)

    # Update Master CSV
    print("\n[5/6] Updating Master CSV...")
    update_master_csv(moved_files)

    # Generate summary
    print("\n[6/6] Generating summary...")
    generate_summary(prompt_files, non_prompt_files, moved_files)

    print("\n" + "=" * 60)
    print("[SUCCESS] Restructuring complete!")
    print("=" * 60)
    print(f"\nCore folder: {CORE_DIR}")
    print(f"Archive folder: {ARCHIVE_DIR}")
    print(f"Master CSV updated: {MASTER_LIST}")
    print(f"Backup created: {BACKUP_CSV}")

if __name__ == '__main__':
    main()
