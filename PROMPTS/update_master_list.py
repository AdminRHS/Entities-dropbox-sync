import os
import csv
import re
from pathlib import Path

# Define paths
PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
MASTER_LIST_PATH = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"

# Files to exclude (documentation, templates, etc.)
EXCLUDE_PATTERNS = [
    r'README',
    r'INDEX',
    r'SUMMARY',
    r'TEMPLATE',
    r'IMPLEMENTATION',
    r'classification',
    r'REVERSE_PROMPT',
    r'SESSION_LOG',
    r'VARIABLE_MAPPING',
    r'docs[/\\]',
    r'Constructor[/\\].*(?:md|txt)$',
    r'[/\\]Core[/\\]',  # Exclude Core folder
]

# Department code mapping
DEPT_MAP = {
    'AI': 'AID',
    'HR': 'HRM',
    'Dev': 'DEV',
    'Development': 'DEV',
    'Sales': 'SLS',
    'Design': 'DGN',
    'Video': 'VID',
    'LG': 'LGN',
    'Lead': 'LGN',
    'Marketing': 'MKT',
    'Finance': 'FIN',
    'SMM': 'SMM',
    'Content': 'MKT',
    'Automation': 'AID',
    'Taxonomy': 'AID',
    'System': 'AID',
    'Research': 'AID',
    'Operational': 'OPS',
    'Account': 'AID',
    'Library': 'AID',
    'Workflow': 'OPS',
    'Daily_Report': 'OPS',
}

def should_exclude(file_path):
    """Check if file should be excluded based on patterns"""
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, file_path, re.IGNORECASE):
            return True
    return False

def extract_pmt_number(filename):
    """Extract PMT number from filename if present"""
    match = re.search(r'PMT-(\d+)', filename, re.IGNORECASE)
    return f"PMT-{match.group(1)}" if match else None

def infer_department(file_path):
    """Infer department from file path"""
    path_upper = file_path.upper()

    for key, dept in DEPT_MAP.items():
        if key.upper() in path_upper:
            return dept

    return 'AID'  # Default to AID

def extract_name_from_filename(filename):
    """Extract readable name from filename"""
    # Remove PMT number and version
    name = re.sub(r'PMT-\d+_', '', filename, flags=re.IGNORECASE)
    name = re.sub(r'_v\d+(\.\d+)?', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\.md$', '', name, flags=re.IGNORECASE)
    # Replace underscores with spaces
    name = name.replace('_', ' ')
    return name.strip()

def get_status_from_path(file_path):
    """Determine status based on file location"""
    if '_ARCHIVE' in file_path or 'Archive' in file_path or 'Deprecated' in file_path:
        return 'Deprecated'
    elif 'DRAFT' in file_path.upper() or 'WIP' in file_path.upper():
        return 'Draft'
    return 'Active'

def load_existing_entries():
    """Load existing entries from Master List"""
    existing = {}
    max_prm = 0

    with open(MASTER_LIST_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Track by file path to avoid duplicates
            file_path = row['File_Path'].strip()
            existing[file_path] = row

            # Track highest PRM number
            prm_match = re.search(r'PRM-(\d+)', row['New_ID'])
            if prm_match:
                max_prm = max(max_prm, int(prm_match.group(1)))

    return existing, max_prm

def find_all_prompt_files():
    """Find all prompt .md files excluding Core and documentation"""
    prompt_files = []

    for root, dirs, files in os.walk(PROMPTS_DIR):
        # Skip Core folder
        if 'Core' in dirs:
            dirs.remove('Core')

        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)

                # Check if should exclude
                if should_exclude(full_path):
                    continue

                # Store relative path from ENTITIES
                rel_path = full_path.replace(r'C:\Users\Dell\Dropbox\ENTITIES', 'ENTITIES')
                rel_path = rel_path.replace('\\', '/')

                prompt_files.append({
                    'full_path': full_path,
                    'rel_path': rel_path,
                    'filename': file
                })

    return prompt_files

def main():
    print("Loading existing Master List...")
    existing_entries, max_prm = load_existing_entries()
    print(f"Found {len(existing_entries)} existing entries")
    print(f"Highest PRM number: PRM-{max_prm:03d}")

    print("\nScanning for prompt files...")
    all_files = find_all_prompt_files()
    print(f"Found {len(all_files)} potential prompt files (excluding Core and docs)")

    # Identify new files
    new_entries = []
    next_prm = max_prm + 1

    for file_info in all_files:
        rel_path = file_info['rel_path']

        if rel_path not in existing_entries:
            pmt_num = extract_pmt_number(file_info['filename'])
            current_id = pmt_num if pmt_num else f"PRM-NEW-{next_prm:03d}"

            name = extract_name_from_filename(file_info['filename'])
            dept = infer_department(file_info['full_path'])
            status = get_status_from_path(file_info['full_path'])

            new_entry = {
                'New_ID': f"PRM-{next_prm:03d}",
                'Entity_Type': 'Prompt',
                'Current_ID': current_id,
                'Name': name,
                'Description': f"Prompt file: {name}",
                'Department': dept,
                'File_Path': rel_path,
                'Status': status
            }

            new_entries.append(new_entry)
            next_prm += 1

    print(f"\nFound {len(new_entries)} NEW entries to add")

    if new_entries:
        print("\nNew entries to be added:")
        for entry in new_entries[:10]:  # Show first 10
            print(f"  - {entry['New_ID']}: {entry['Name']} ({entry['Department']}) - {entry['File_Path']}")
        if len(new_entries) > 10:
            print(f"  ... and {len(new_entries) - 10} more")

        # Append to Master List
        print(f"\nAppending {len(new_entries)} new entries to Master List...")
        with open(MASTER_LIST_PATH, 'a', encoding='utf-8', newline='') as f:
            fieldnames = ['New_ID', 'Entity_Type', 'Current_ID', 'Name', 'Description', 'Department', 'File_Path', 'Status']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            for entry in new_entries:
                writer.writerow(entry)

        print(f"✓ Successfully added {len(new_entries)} new entries!")
        print(f"✓ Master List now has {len(existing_entries) + len(new_entries)} total entries")
    else:
        print("\n✓ No new entries to add. Master List is up to date!")

if __name__ == '__main__':
    main()
