"""
ENTITIES Master List Generator
Creates a comprehensive CSV inventory of all folders and files in the ENTITIES directory.
"""

import os
import csv
from datetime import datetime
from pathlib import Path
import re

def extract_date_from_path(path_str):
    """Extract date reference from path or filename if present."""
    # Pattern for YYYY-MM-DD format
    date_pattern = r'(\d{4}-\d{2}-\d{2})'
    match = re.search(date_pattern, path_str)
    if match:
        return match.group(1)
    return ""

def is_master_file(name):
    """Check if file is a master reference file."""
    master_indicators = [
        '_Master', '_MASTER', 'Master_', 'MASTER_',
        'master_list', 'Master_List', 'MASTER_LIST',
        'FOLDER_MASTER', 'master.json', 'master.csv'
    ]
    return any(indicator in name for indicator in master_indicators)

def get_category(relative_path):
    """Extract top-level category from relative path."""
    parts = Path(relative_path).parts
    if len(parts) > 0:
        return parts[0]
    return "ROOT"

def scan_directory(root_path):
    """
    Recursively scan directory and collect metadata for all items.

    Returns:
        list of dict: Each dict contains metadata for one file/folder
    """
    items = []
    root_path = Path(root_path).resolve()

    print(f"Scanning directory: {root_path}")
    print("This may take a few moments for large directories...")

    # Counter for progress
    count = 0

    for dirpath, dirnames, filenames in os.walk(root_path):
        current_dir = Path(dirpath)

        # Process directories
        for dirname in dirnames:
            dir_path = current_dir / dirname
            relative_path = dir_path.relative_to(root_path)
            depth = len(relative_path.parts)

            try:
                stat_info = dir_path.stat()
                last_modified = datetime.fromtimestamp(stat_info.st_mtime).isoformat()
            except Exception as e:
                last_modified = ""

            # Check if directory has subdirectories
            has_children = any(dir_path.iterdir()) if dir_path.exists() else False

            items.append({
                'Path': str(dir_path),
                'Relative_Path': str(relative_path),
                'Name': dirname,
                'Type': 'Directory',
                'Extension': '',
                'Parent_Directory': current_dir.name,
                'Depth_Level': depth,
                'Category': get_category(relative_path),
                'Size_Bytes': 0,
                'Last_Modified': last_modified,
                'Is_Master_File': False,
                'Is_Documentation': False,
                'Date_Reference': extract_date_from_path(str(relative_path)),
                'Has_Children': has_children
            })

            count += 1
            if count % 100 == 0:
                print(f"Processed {count} items...")

        # Process files
        for filename in filenames:
            file_path = current_dir / filename
            relative_path = file_path.relative_to(root_path)
            depth = len(relative_path.parts)
            extension = file_path.suffix

            try:
                stat_info = file_path.stat()
                size_bytes = stat_info.st_size
                last_modified = datetime.fromtimestamp(stat_info.st_mtime).isoformat()
            except Exception as e:
                size_bytes = 0
                last_modified = ""

            items.append({
                'Path': str(file_path),
                'Relative_Path': str(relative_path),
                'Name': filename,
                'Type': 'File',
                'Extension': extension,
                'Parent_Directory': current_dir.name,
                'Depth_Level': depth,
                'Category': get_category(relative_path),
                'Size_Bytes': size_bytes,
                'Last_Modified': last_modified,
                'Is_Master_File': is_master_file(filename),
                'Is_Documentation': extension.lower() == '.md',
                'Date_Reference': extract_date_from_path(str(relative_path)),
                'Has_Children': False
            })

            count += 1
            if count % 100 == 0:
                print(f"Processed {count} items...")

    print(f"\nTotal items processed: {count}")
    return items

def generate_summary(items, output_path):
    """Generate a summary report of the scanned items."""

    # Statistics
    total_items = len(items)
    total_files = sum(1 for item in items if item['Type'] == 'File')
    total_dirs = sum(1 for item in items if item['Type'] == 'Directory')

    # Extension distribution
    extensions = {}
    for item in items:
        if item['Type'] == 'File':
            ext = item['Extension'] if item['Extension'] else '(no extension)'
            extensions[ext] = extensions.get(ext, 0) + 1

    # Category distribution
    categories = {}
    for item in items:
        cat = item['Category']
        categories[cat] = categories.get(cat, 0) + 1

    # Total size
    total_size = sum(item['Size_Bytes'] for item in items if item['Type'] == 'File')
    total_size_mb = total_size / (1024 * 1024)

    # Master files count
    master_files = sum(1 for item in items if item['Is_Master_File'])

    # Documentation files count
    doc_files = sum(1 for item in items if item['Is_Documentation'])

    # Create summary report
    summary = f"""# ENTITIES Master List Summary Report

Generated: {datetime.now().isoformat()}

## Overall Statistics

- **Total Items:** {total_items:,}
- **Total Files:** {total_files:,}
- **Total Directories:** {total_dirs:,}
- **Total Size:** {total_size_mb:.2f} MB ({total_size:,} bytes)
- **Master Reference Files:** {master_files}
- **Documentation Files (.md):** {doc_files}

## File Type Distribution

| Extension | Count |
|-----------|-------|
"""

    # Sort extensions by count (descending)
    sorted_extensions = sorted(extensions.items(), key=lambda x: x[1], reverse=True)
    for ext, count in sorted_extensions:
        summary += f"| {ext} | {count:,} |\n"

    summary += f"\n## Category Distribution (Top-Level Folders)\n\n"
    summary += "| Category | Count |\n"
    summary += "|----------|-------|\n"

    # Sort categories by count (descending)
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    for cat, count in sorted_categories:
        summary += f"| {cat} | {count:,} |\n"

    summary += f"\n## Master Reference Files Found\n\n"
    master_items = [item for item in items if item['Is_Master_File']]
    if master_items:
        for item in sorted(master_items, key=lambda x: x['Relative_Path']):
            summary += f"- [{item['Name']}]({item['Relative_Path']})\n"
    else:
        summary += "No master reference files found.\n"

    summary += f"\n## Output Files\n\n"
    summary += f"- CSV Master List: `ENTITIES_MASTER_LIST.csv`\n"
    summary += f"- This Summary: `ENTITIES_MASTER_LIST_SUMMARY.md`\n"

    # Write summary file
    summary_path = output_path.replace('.csv', '_SUMMARY.md')
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"\nSummary report saved to: {summary_path}")

    return summary

def main():
    """Main execution function."""

    # Define paths
    entities_path = Path(__file__).parent
    output_csv = entities_path / "ENTITIES_MASTER_LIST.csv"

    print("="*60)
    print("ENTITIES Master List Generator")
    print("="*60)
    print(f"\nScanning: {entities_path}")
    print(f"Output CSV: {output_csv}\n")

    # Scan directory
    items = scan_directory(entities_path)

    # Define CSV columns
    fieldnames = [
        'Path',
        'Relative_Path',
        'Name',
        'Type',
        'Extension',
        'Parent_Directory',
        'Depth_Level',
        'Category',
        'Size_Bytes',
        'Last_Modified',
        'Is_Master_File',
        'Is_Documentation',
        'Date_Reference',
        'Has_Children'
    ]

    # Write to CSV
    print(f"\nWriting CSV file...")
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

    print(f"CSV file saved: {output_csv}")
    print(f"Total rows written: {len(items):,}")

    # Generate summary report
    print(f"\nGenerating summary report...")
    summary = generate_summary(items, str(output_csv))

    print("\n" + "="*60)
    print("COMPLETED SUCCESSFULLY")
    print("="*60)
    print(f"\nOutputs created:")
    print(f"  1. {output_csv}")
    print(f"  2. {str(output_csv).replace('.csv', '_SUMMARY.md')}")
    print()

if __name__ == "__main__":
    main()
