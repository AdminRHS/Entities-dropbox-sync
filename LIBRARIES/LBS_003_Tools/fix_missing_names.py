#!/usr/bin/env python3
"""
Fix missing tool names in JSON files and regenerate CSV
"""

import json
import csv
from pathlib import Path

TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
CSV_OUTPUT = TOOLS_ROOT / "Tools_Master_Inventory.csv"


def infer_name_from_filename(filename):
    """Infer tool name from filename."""
    # Remove TOL-### prefix and .json extension
    name = filename.replace('.json', '')
    parts = name.split('_', 1)
    if len(parts) > 1:
        name = parts[1]

    # Convert underscores to spaces and title case
    name = name.replace('_', ' ')

    # Special cases
    special_cases = {
        'arXiv': 'arXiv',
        'GitHub': 'GitHub',
        'LinkedIn': 'LinkedIn',
        'YouTube': 'YouTube',
        'TikTok': 'TikTok',
        'DeviantArt': 'DeviantArt',
        'ArtStation': 'ArtStation',
        'Stack Overflow': 'Stack Overflow',
        'Dev to': 'Dev.to',
        'Dropbox Dash': 'Dropbox Dash',
        'Dropbox Protect and Control': 'Dropbox Protect & Control',
        'MCP Servers': 'MCP Servers',
        'LLM as Judge Evaluation Framework': 'LLM as Judge Evaluation Framework',
        'Product Management Decision Framework': 'Product Management Decision Framework',
        'Company Voice Guide': 'Company Voice Guide',
        'Custom Prompt Templates': 'Custom Prompt Templates',
        'AI Tools Master Listing': 'AI Tools Master Listing',
        'awesome copilot': 'Awesome Copilot'
    }

    # Check if name matches special case
    for key, value in special_cases.items():
        if name.lower() == key.lower():
            return value

    return name


def fix_missing_names():
    """Fix JSON files with missing names."""
    print("=" * 80)
    print("FIXING MISSING TOOL NAMES")
    print("=" * 80)

    fixed = 0

    for file_path in sorted(TOOLS_ROOT.glob('TOL-*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            name = data.get('name', '').strip()

            if not name:
                # Infer name from filename
                inferred_name = infer_name_from_filename(file_path.name)
                data['name'] = inferred_name

                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                print(f"  [FIXED] {data.get('tool_id')} -> {inferred_name}")
                fixed += 1

        except Exception as e:
            print(f"  [ERROR] {file_path.name}: {e}")

    print(f"\n[OK] Fixed {fixed} tools with missing names")
    print("=" * 80)


def get_category_from_data(data):
    """Extract readable category from tool data."""
    category = data.get('category', '')

    # Simplify categories
    if 'AI' in category or 'LLM' in category or 'llm' in category:
        if 'Video' in category:
            return 'AI Tools - Video'
        elif 'Image' in category or 'Generation' in category:
            return 'AI Tools - Image'
        elif 'Audio' in category:
            return 'AI Tools - Audio'
        elif 'Code' in category or 'Development' in category:
            return 'AI Tools - Code'
        else:
            return 'AI Tools'

    elif 'Cloud' in category:
        return 'Cloud Infrastructure'
    elif 'Database' in category or 'Storage' in category:
        return 'Database'
    elif 'Social' in category or 'Network' in category or 'Community' in category:
        return 'Social Network'
    elif 'Freelance' in category or 'Marketplace' in category:
        return 'Freelance Platform'
    elif 'Developer' in category or 'Development' in category or 'IDE' in category:
        return 'Development Tools'
    elif 'Web' in category or 'Scraping' in category or 'Crawl' in category:
        return 'Web Services'
    elif 'Data' in category or 'Analytics' in category:
        return 'Data & Analytics'
    elif 'Payment' in category:
        return 'Payment'
    elif 'Security' in category or 'Authentication' in category or 'Auth' in category:
        return 'Security'
    elif 'Video' in category and 'AI' not in category:
        return 'Video Platform'
    elif 'Portfolio' in category or 'Creative' in category:
        return 'Creative Portfolio'
    elif 'Publishing' in category or 'Blogging' in category:
        return 'Publishing Platform'
    elif 'Integration' in category:
        return 'Integration Tools'
    elif category:
        return category

    # Infer from purpose or vendor
    purpose = data.get('purpose', '').lower()
    vendor = data.get('vendor', '').lower()

    if any(word in purpose or word in vendor for word in ['ai', 'llm', 'language model']):
        return 'AI Tools'
    elif any(word in purpose or word in vendor for word in ['social', 'network']):
        return 'Social Network'
    elif any(word in purpose or word in vendor for word in ['cloud', 'hosting']):
        return 'Cloud Infrastructure'

    return 'Other'


def regenerate_csv():
    """Regenerate CSV with fixed names and better categories."""
    print("\n" + "=" * 80)
    print("REGENERATING MASTER CSV")
    print("=" * 80)

    tools = []

    for file_path in sorted(TOOLS_ROOT.glob('TOL-*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            tol_id = data.get('tool_id', '')
            name = data.get('name', 'Unknown')
            vendor = data.get('vendor', 'N/A')
            category = get_category_from_data(data)
            purpose = data.get('purpose', 'N/A')
            description = data.get('description', 'N/A')

            # Short description
            if description and description != 'N/A':
                if isinstance(description, dict):
                    short_desc = description.get('short', description.get('detailed', ''))
                else:
                    short_desc = description

                if isinstance(short_desc, str):
                    short_desc = short_desc.split('.')[0] + '.' if '.' in short_desc else short_desc
                    if len(short_desc) > 150:
                        short_desc = short_desc[:147] + '...'
                else:
                    short_desc = str(short_desc)[:150]
            else:
                short_desc = purpose if purpose != 'N/A' else 'No description'

            cost = data.get('cost_structure', 'N/A')

            platforms = data.get('platform_compatibility', [])
            if isinstance(platforms, list):
                platforms_str = ', '.join(platforms[:3])
                if len(platforms) > 3:
                    platforms_str += f' (+{len(platforms)-3})'
            else:
                platforms_str = str(platforms) if platforms else 'N/A'

            tags = data.get('tags', [])
            if isinstance(tags, list):
                tags_str = ', '.join(tags[:5])
            else:
                tags_str = ''

            status = data.get('status', 'active').replace('_', ' ').title()
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
                'Status': status,
                'Documentation_URL': docs_url,
                'Filename': file_path.name
            })

            print(f"  [OK] {tol_id} - {name} ({category})")

        except Exception as e:
            print(f"  [ERROR] {file_path.name}: {e}")

    # Write CSV
    headers = [
        'TOL_ID', 'Name', 'Vendor', 'Category', 'Description',
        'Purpose', 'Cost', 'Platforms', 'Tags', 'Status',
        'Documentation_URL', 'Filename'
    ]

    try:
        with open(CSV_OUTPUT, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(tools)

        print(f"\n[OK] CSV regenerated: {CSV_OUTPUT}")
        print(f"[OK] Total entries: {len(tools)}")
        print("=" * 80)

    except Exception as e:
        print(f"\n[ERROR] Failed to create CSV: {e}")
        print("=" * 80)


def main():
    print("\n" + "=" * 80)
    print(" FIX MISSING NAMES AND REGENERATE CSV")
    print("=" * 80)

    # Step 1: Fix missing names in JSON files
    fix_missing_names()

    # Step 2: Regenerate CSV with fixed data
    regenerate_csv()

    print("\n[SUCCESS] All tools now have names!")


if __name__ == "__main__":
    main()
