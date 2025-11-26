#!/usr/bin/env python3
"""
Fix Duplicates and Create Better CSV
- Remove duplicate tool files
- Create improved master CSV with useful information
"""

import os
import json
import csv
import shutil
from pathlib import Path
from datetime import datetime

TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
CSV_OUTPUT = TOOLS_ROOT / "Tools_Master_Inventory.csv"
BACKUP_DIR = TOOLS_ROOT / "_ARCHIVE" / "removed_duplicates_2025-11-26"

# Duplicates to remove (keep the first, remove the second)
DUPLICATES_TO_REMOVE = [
    'TOL-020_Browse_AI.json',      # Keep TOL-019
    'TOL-069_Google_Sheets.json'   # Keep TOL-068
]


def backup_and_remove_duplicates():
    """Backup and remove duplicate files."""
    print("=" * 80)
    print("REMOVING DUPLICATE FILES")
    print("=" * 80)

    # Create backup directory
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created backup directory: {BACKUP_DIR}\n")

    removed = []
    for filename in DUPLICATES_TO_REMOVE:
        file_path = TOOLS_ROOT / filename
        if file_path.exists():
            # Backup first
            backup_path = BACKUP_DIR / filename
            shutil.copy2(file_path, backup_path)
            print(f"[BACKUP] {filename}")

            # Remove from root
            file_path.unlink()
            print(f"[REMOVE] {filename}")
            removed.append(filename)
        else:
            print(f"[SKIP] {filename} (not found)")

    print(f"\n[OK] Removed {len(removed)} duplicate files")
    print("=" * 80)
    return removed


def get_category_from_data(data):
    """Extract readable category from tool data."""
    category = data.get('category', '')

    # Map common categories to readable names
    category_map = {
        'AI Tools': 'AI Tools',
        'AI/LLM Services': 'AI Tools',
        'AI Tool': 'AI Tools',
        'Cloud Platforms': 'Cloud Infrastructure',
        'Cloud Platform': 'Cloud Infrastructure',
        'Database': 'Database',
        'Databases': 'Database',
        'Data Tools': 'Data & Analytics',
        'Web Tools': 'Web Services',
        'Social Media': 'Social Network',
        'Social Network': 'Social Network',
        'Freelance': 'Freelance Platform',
        'Freelance Platform': 'Freelance Platform',
        'Developer Tools': 'Development Tools',
        'Development': 'Development Tools',
        'Integration': 'Integration Tools',
        'Payment': 'Payment Processing',
        'Authentication': 'Authentication',
        'Security': 'Security',
        'Publishing': 'Publishing Platform',
        'Infrastructure': 'Infrastructure',
        'File Management': 'File Management',
        'Methodology': 'Methodology'
    }

    # Try to match
    for key, value in category_map.items():
        if key.lower() in category.lower():
            return value

    # If no match, return original or infer from vendor/purpose
    if category:
        return category

    # Infer from vendor or purpose
    vendor = data.get('vendor', '').lower()
    purpose = data.get('purpose', '').lower()

    if any(word in vendor or word in purpose for word in ['ai', 'llm', 'language model']):
        return 'AI Tools'
    elif any(word in vendor or word in purpose for word in ['social', 'network', 'community']):
        return 'Social Network'
    elif any(word in vendor or word in purpose for word in ['cloud', 'hosting', 'deploy']):
        return 'Cloud Infrastructure'
    elif any(word in vendor or word in purpose for word in ['database', 'db', 'storage']):
        return 'Database'

    return 'Other'


def create_improved_csv():
    """Create improved CSV with useful information."""
    print("\n" + "=" * 80)
    print("CREATING IMPROVED MASTER CSV")
    print("=" * 80)

    tools = []

    # Read all TOL files
    for file_path in sorted(TOOLS_ROOT.glob('TOL-*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Extract useful information
            tol_id = data.get('tool_id', '')
            name = data.get('name', '')
            vendor = data.get('vendor', 'N/A')
            category = get_category_from_data(data)
            purpose = data.get('purpose', 'N/A')
            description = data.get('description', 'N/A')

            # Get short description (first sentence or 150 chars)
            if description and description != 'N/A':
                short_desc = description.split('.')[0] + '.' if '.' in description else description
                if len(short_desc) > 150:
                    short_desc = short_desc[:147] + '...'
            else:
                short_desc = purpose if purpose != 'N/A' else 'No description available'

            # Cost info
            cost = data.get('cost_structure', 'N/A')

            # Platform compatibility
            platforms = data.get('platform_compatibility', [])
            if isinstance(platforms, list):
                platforms_str = ', '.join(platforms[:3])  # First 3 platforms
                if len(platforms) > 3:
                    platforms_str += f' (+{len(platforms)-3} more)'
            else:
                platforms_str = str(platforms) if platforms else 'N/A'

            # Tags
            tags = data.get('tags', [])
            if isinstance(tags, list):
                tags_str = ', '.join(tags[:5])  # First 5 tags
            else:
                tags_str = ''

            # Status
            status = data.get('status', 'active')

            # Documentation URL
            docs_url = data.get('documentation_url', '')

            tools.append({
                'TOL_ID': tol_id,
                'Name': name,
                'Vendor': vendor,
                'Category': category,
                'Description': short_desc,
                'Purpose': purpose,
                'Cost': cost,
                'Platforms': platforms_str,
                'Tags': tags_str,
                'Status': status.title(),
                'Documentation_URL': docs_url,
                'Filename': file_path.name
            })

            print(f"  [OK] {tol_id} - {name}")

        except Exception as e:
            print(f"  [ERROR] {file_path.name}: {e}")

    # Write to CSV
    headers = [
        'TOL_ID',
        'Name',
        'Vendor',
        'Category',
        'Description',
        'Purpose',
        'Cost',
        'Platforms',
        'Tags',
        'Status',
        'Documentation_URL',
        'Filename'
    ]

    try:
        with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(tools)

        print(f"\n[OK] Created improved CSV: {CSV_OUTPUT}")
        print(f"[OK] Total entries: {len(tools)}")
        print("=" * 80)

    except Exception as e:
        print(f"\n[ERROR] Failed to create CSV: {e}")
        print("=" * 80)

    return tools


def print_summary(removed_files, tools):
    """Print summary report."""
    print("\n" + "=" * 80)
    print("SUMMARY REPORT")
    print("=" * 80)

    print(f"\nDuplicates removed: {len(removed_files)}")
    for f in removed_files:
        print(f"  - {f}")

    print(f"\nTotal tools in inventory: {len(tools)}")
    print(f"CSV file: {CSV_OUTPUT}")
    print(f"Backup location: {BACKUP_DIR}")

    # Category breakdown
    print("\nTools by Category:")
    categories = {}
    for tool in tools:
        cat = tool['Category']
        categories[cat] = categories.get(cat, 0) + 1

    for cat in sorted(categories.keys()):
        print(f"  {cat}: {categories[cat]}")

    print("\n" + "=" * 80)
    print("[SUCCESS] Duplicate removal and CSV improvement complete!")
    print("=" * 80)


def main():
    print("\n" + "=" * 80)
    print(" FIX DUPLICATES AND CREATE BETTER CSV")
    print(" Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 80)

    # Step 1: Remove duplicates
    removed_files = backup_and_remove_duplicates()

    # Step 2: Create improved CSV
    tools = create_improved_csv()

    # Step 3: Print summary
    print_summary(removed_files, tools)


if __name__ == "__main__":
    main()
