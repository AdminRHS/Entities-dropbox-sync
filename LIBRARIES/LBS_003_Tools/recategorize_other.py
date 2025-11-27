#!/usr/bin/env python3
"""
Recategorize 'Other' tools with proper subcategories
"""

import csv
from pathlib import Path

TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
MASTER_CSV = TOOLS_ROOT / "Tools_Master_Inventory.csv"

# Detailed recategorization map
RECATEGORIZATION = {
    'TOL-001': 'Freelance & Talent - Design Services',
    'TOL-003': 'Documentation & Resources',
    'TOL-011': 'Portfolio & Creative Showcase',
    'TOL-012': 'Research & Academic',
    'TOL-013': 'Security & Authentication',
    'TOL-016': 'Portfolio & Creative Showcase',
    'TOL-018': 'Data Services & Marketplaces',
    'TOL-029': 'Freelance & Talent - Offshore/RevOps',
    'TOL-032': 'Documentation & Resources',
    'TOL-036': 'Integration & Connectors',
    'TOL-038': 'Documentation & Resources',
    'TOL-047': 'Productivity & Search',
    'TOL-048': 'Security & Authentication',
    'TOL-050': 'Design Assets & Resources',
    'TOL-053': 'Freelance & Talent - General',
    'TOL-056': 'Design Assets & Resources',
    'TOL-061': 'Development & Code Management',
    'TOL-064': 'Integration & Connectors',
    'TOL-066': 'Integration & Connectors',
    'TOL-085': 'Documentation & Resources',
    'TOL-091': 'Freelance & Talent - Marketing',
    'TOL-095': 'Publishing & Content',
    'TOL-114': 'Social & Discovery',
    'TOL-117': 'Documentation & Resources',
    'TOL-136': 'Payment & Financial',
    'TOL-137': 'Publishing & Content',
    'TOL-144': 'Social & Discovery',
    'TOL-147': 'Freelance & Talent - General',
    'TOL-152': 'Video & Media Hosting'
}


def recategorize_other_tools():
    """Recategorize tools from 'Other' to specific subcategories."""
    print("=" * 80)
    print("RECATEGORIZING 'OTHER' TOOLS")
    print("=" * 80)

    tools = []
    updated_count = 0

    # Read CSV
    with open(MASTER_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tol_id = row['TOL_ID']

            # Check if needs recategorization
            if tol_id in RECATEGORIZATION:
                old_cat = row['Category']
                new_cat = RECATEGORIZATION[tol_id]
                row['Category'] = new_cat
                updated_count += 1
                print(f"  [UPDATE] {tol_id} {row['Name']}")
                print(f"           {old_cat} -> {new_cat}")

            tools.append(row)

    # Write updated CSV
    headers = list(tools[0].keys())
    with open(MASTER_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(tools)

    print(f"\n[OK] Updated {updated_count} tools")
    print("=" * 80)

    # Print new category distribution
    from collections import Counter
    cat_counts = Counter(t['Category'] for t in tools)

    print("\nNew category distribution:")
    for cat, count in sorted(cat_counts.items()):
        print(f"  {cat}: {count}")

    return tools


def update_category_csv(tools):
    """Update the category-based CSV with new categories."""
    print("\n" + "=" * 80)
    print("UPDATING CATEGORY-BASED VIEW")
    print("=" * 80)

    CATEGORY_CSV = TOOLS_ROOT / "Tools_By_Category.csv"

    # Sort by category, then by name
    tools_sorted = sorted(tools, key=lambda x: (x['Category'], x['Name']))

    # Create category view
    category_tools = []
    for tool in tools_sorted:
        desc = tool['Description'][:100] + '...' if len(tool['Description']) > 100 else tool['Description']
        cost = tool['Cost'][:50] + '...' if len(tool['Cost']) > 50 else tool['Cost']

        category_tools.append({
            'Category': tool['Category'],
            'TOL_ID': tool['TOL_ID'],
            'Name': tool['Name'],
            'Description': desc,
            'Cost': cost,
            'Status': tool['Status']
        })

    headers = ['Category', 'TOL_ID', 'Name', 'Description', 'Cost', 'Status']

    with open(CATEGORY_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(category_tools)

    print(f"[OK] Updated category view: {CATEGORY_CSV}")
    print("=" * 80)


def main():
    """Main execution."""
    print("\n" + "=" * 80)
    print(" RECATEGORIZING 'OTHER' TOOLS")
    print("=" * 80)

    # Recategorize
    tools = recategorize_other_tools()

    # Update category CSV
    update_category_csv(tools)

    print("\n" + "=" * 80)
    print("[SUCCESS] RECATEGORIZATION COMPLETE!")
    print("=" * 80)

    print("\nNew Categories Added:")
    new_cats = set(RECATEGORIZATION.values())
    for cat in sorted(new_cats):
        count = sum(1 for t in tools if t['Category'] == cat)
        print(f"  - {cat} ({count} tools)")


if __name__ == "__main__":
    main()
