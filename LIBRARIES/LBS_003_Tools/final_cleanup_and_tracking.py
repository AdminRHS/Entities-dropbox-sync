#!/usr/bin/env python3
"""
Final TOOLS Library Cleanup and Mentions Tracking System
- Clean up master CSV (remove Vendor, consolidate categories)
- Create category-based view
- Scan reports for tool mentions
- Generate usage tracking and analysis
"""

import os
import json
import csv
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

TOOLS_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools")
DAILIES_ROOT = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES")

# Output files
MASTER_CSV = TOOLS_ROOT / "Tools_Master_Inventory.csv"
CATEGORY_CSV = TOOLS_ROOT / "Tools_By_Category.csv"
MENTIONS_CSV = TOOLS_ROOT / "Tools_Mentions_Tracking.csv"
ANALYSIS_MD = TOOLS_ROOT / "Tools_Usage_Analysis.md"

# Category consolidation map
CATEGORY_MAP = {
    'AI Tools': 'AI Tools',
    'AI Tools - Video': 'AI Tools - Video',
    'AI Tools - Image': 'AI Tools - Image',
    'AI Tools - Code': 'AI Tools - Code',
    'AI Tools - Audio': 'AI Tools - Audio',

    # Social & Communication
    'Social Network': 'Social Network & Communication',
    'Messaging and Channel Platform': 'Social Network & Communication',
    'Question & Answer Platform': 'Social Network & Communication',

    # Cloud & Infrastructure
    'Cloud Infrastructure': 'Cloud & Infrastructure',
    'Infrastructure': 'Cloud & Infrastructure',

    # Database
    'Database': 'Database & Storage',

    # Development
    'Development Tools': 'Development Tools',
    'Developer Tools': 'Development Tools',

    # Data
    'Data & Analytics': 'Data & Analytics',
    'Web Services': 'Data & Analytics',

    # Design & Creative
    'Creative Portfolio': 'Design & Creative',
    'Design Resources': 'Design & Creative',
    'Visual Discovery Platform': 'Design & Creative',
    'Video Platform': 'Design & Creative',

    # Business
    'Freelance Platform': 'Business Tools',
    'Payment': 'Business Tools',
    'Integration Tools': 'Business Tools',
    'Security': 'Business Tools',
    'Publishing Platform': 'Business Tools',
    'Specialized Talent Platform / Marketing / HR Tools': 'Business Tools',
    'Specialized Talent Platform / RevOps / Offshore Hiring': 'Business Tools',

    # Other
    'Other': 'Other'
}


def consolidate_category(original_category):
    """Consolidate categories to simplified set."""
    for pattern, target in CATEGORY_MAP.items():
        if pattern.lower() in original_category.lower():
            return target
    return 'Other'


def phase1_clean_master_csv():
    """Phase 1: Clean up master CSV - remove Vendor, consolidate categories."""
    print("=" * 80)
    print("PHASE 1: CLEANING UP MASTER CSV")
    print("=" * 80)

    tools = []

    # Read current CSV
    with open(MASTER_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Consolidate category
            original_cat = row['Category']
            new_cat = consolidate_category(original_cat)

            tools.append({
                'TOL_ID': row['TOL_ID'],
                'Category': new_cat,
                'Name': row['Name'],
                'Description': row['Description'],
                'Purpose': row['Purpose'],
                'Cost': row['Cost'],
                'Platforms': row['Platforms'],
                'Tags': row['Tags'],
                'Status': row['Status'],
                'Documentation_URL': row['Documentation_URL'],
                'Filename': row['Filename']
            })

            if original_cat != new_cat:
                print(f"  [REMAP] {row['TOL_ID']} {row['Name']}: {original_cat} -> {new_cat}")

    # Write cleaned CSV (removed Vendor, consolidated categories)
    headers = ['TOL_ID', 'Category', 'Name', 'Description', 'Purpose', 'Cost',
               'Platforms', 'Tags', 'Status', 'Documentation_URL', 'Filename']

    with open(MASTER_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(tools)

    # Print category summary
    cat_counts = Counter(t['Category'] for t in tools)
    print(f"\n[OK] Cleaned CSV: {len(tools)} tools")
    print(f"[OK] Categories consolidated: {len(CATEGORY_MAP)} -> {len(cat_counts)}")
    print("\nNew category distribution:")
    for cat, count in sorted(cat_counts.items()):
        print(f"  {cat}: {count}")

    print("=" * 80)
    return tools


def phase2_create_category_view(tools):
    """Phase 2: Create category-based view CSV."""
    print("\n" + "=" * 80)
    print("PHASE 2: CREATING CATEGORY-BASED VIEW")
    print("=" * 80)

    # Sort by category, then by name
    tools_sorted = sorted(tools, key=lambda x: (x['Category'], x['Name']))

    # Create category view
    category_tools = []
    for tool in tools_sorted:
        category_tools.append({
            'Category': tool['Category'],
            'TOL_ID': tool['TOL_ID'],
            'Name': tool['Name'],
            'Description': tool['Description'][:100] + '...' if len(tool['Description']) > 100 else tool['Description'],
            'Cost': tool['Cost'][:50] + '...' if len(tool['Cost']) > 50 else tool['Cost'],
            'Status': tool['Status']
        })

    headers = ['Category', 'TOL_ID', 'Name', 'Description', 'Cost', 'Status']

    with open(CATEGORY_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(category_tools)

    print(f"[OK] Created category view: {CATEGORY_CSV}")
    print(f"[OK] {len(category_tools)} tools organized by category")

    # Print summary
    current_cat = None
    for tool in category_tools:
        if tool['Category'] != current_cat:
            current_cat = tool['Category']
            count = sum(1 for t in category_tools if t['Category'] == current_cat)
            print(f"\n{current_cat} ({count} tools):")
        print(f"  {tool['TOL_ID']} - {tool['Name']}")

    print("=" * 80)
    return category_tools


def phase3_scan_reports_for_mentions(tools):
    """Phase 3: Scan reports for tool mentions."""
    print("\n" + "=" * 80)
    print("PHASE 3: SCANNING REPORTS FOR TOOL MENTIONS")
    print("=" * 80)

    # Build tool lookup
    tool_lookup = {}
    for tool in tools:
        tol_id = tool['TOL_ID']
        name = tool['Name'].lower()
        tool_lookup[tol_id] = {'name': tool['Name'], 'mentions': []}
        tool_lookup[name] = tol_id

    # Common tool names to search for
    tool_patterns = {}
    for tool in tools:
        name = tool['Name']
        tol_id = tool['TOL_ID']

        # Create regex patterns for tool name (case-insensitive, word boundary)
        if name and name != 'Unknown':
            # Escape special chars and create pattern
            escaped = re.escape(name)
            pattern = re.compile(rf'\b{escaped}\b', re.IGNORECASE)
            tool_patterns[tol_id] = {
                'name': name,
                'pattern': pattern,
                'tol_pattern': re.compile(rf'\b{tol_id}\b')
            }

    print(f"Searching for {len(tool_patterns)} tools in reports...")

    # Scan report directories
    report_dirs = [
        DAILIES_ROOT / "REPORTS",
        DAILIES_ROOT / "PLANS",
        DAILIES_ROOT / "LOG"
    ]

    mentions_data = defaultdict(lambda: {
        'count': 0,
        'reports': [],
        'dates': [],
        'contexts': [],
        'departments': set()
    })

    total_files = 0
    files_with_mentions = 0

    for report_dir in report_dirs:
        if not report_dir.exists():
            continue

        for md_file in report_dir.rglob("*.md"):
            total_files += 1
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                    file_has_mentions = False
                    relative_path = md_file.relative_to(DAILIES_ROOT)

                    # Extract date from path or filename
                    date_match = re.search(r'20\d{2}-\d{2}-\d{2}', str(md_file))
                    date = date_match.group(0) if date_match else 'Unknown'

                    # Extract department from path
                    dept_match = re.search(r'(AI|Dev|Design|Video|HR|Sales|LG|Finance)_Department', content, re.IGNORECASE)
                    department = dept_match.group(1) if dept_match else 'Unknown'

                    # Search for each tool
                    for tol_id, patterns in tool_patterns.items():
                        name = patterns['name']

                        # Search by TOL ID
                        tol_matches = patterns['tol_pattern'].findall(content)

                        # Search by tool name
                        name_matches = patterns['pattern'].findall(content)

                        total_matches = len(tol_matches) + len(name_matches)

                        if total_matches > 0:
                            file_has_mentions = True
                            mentions_data[tol_id]['count'] += total_matches
                            mentions_data[tol_id]['reports'].append(str(relative_path))
                            mentions_data[tol_id]['dates'].append(date)
                            mentions_data[tol_id]['departments'].add(department)

                            # Extract context (sentence containing the tool)
                            sentences = content.split('.')
                            for sentence in sentences:
                                if patterns['pattern'].search(sentence) or patterns['tol_pattern'].search(sentence):
                                    context = sentence.strip()[:100]
                                    mentions_data[tol_id]['contexts'].append(context)
                                    break

                    if file_has_mentions:
                        files_with_mentions += 1

            except Exception as e:
                print(f"  [ERROR] {md_file.name}: {e}")

        if total_files % 50 == 0 and total_files > 0:
            print(f"  Processed {total_files} files...")

    print(f"\n[OK] Scanned {total_files} report files")
    print(f"[OK] Found mentions in {files_with_mentions} files")
    print(f"[OK] Tools mentioned: {len([k for k, v in mentions_data.items() if v['count'] > 0])}")

    # Create mentions tracking CSV
    mentions_rows = []
    for tool in tools:
        tol_id = tool['TOL_ID']
        name = tool['Name']

        if tol_id in mentions_data:
            data = mentions_data[tol_id]
            mentions_rows.append({
                'TOL_ID': tol_id,
                'Tool_Name': name,
                'Mention_Count': data['count'],
                'Reports_Count': len(set(data['reports'])),
                'Last_Mentioned': max(data['dates']) if data['dates'] else 'Never',
                'Departments': ', '.join(sorted(data['departments'])) if data['departments'] else 'None',
                'Sample_Reports': '; '.join(list(set(data['reports']))[:3]),
                'Sample_Context': data['contexts'][0] if data['contexts'] else 'N/A'
            })
        else:
            mentions_rows.append({
                'TOL_ID': tol_id,
                'Tool_Name': name,
                'Mention_Count': 0,
                'Reports_Count': 0,
                'Last_Mentioned': 'Never',
                'Departments': 'None',
                'Sample_Reports': 'None',
                'Sample_Context': 'Not mentioned'
            })

    # Sort by mention count (descending)
    mentions_rows.sort(key=lambda x: x['Mention_Count'], reverse=True)

    headers = ['TOL_ID', 'Tool_Name', 'Mention_Count', 'Reports_Count', 'Last_Mentioned',
               'Departments', 'Sample_Reports', 'Sample_Context']

    with open(MENTIONS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(mentions_rows)

    print(f"\n[OK] Created mentions tracking: {MENTIONS_CSV}")

    # Print top mentions
    print("\nTop 10 most mentioned tools:")
    for row in mentions_rows[:10]:
        print(f"  {row['TOL_ID']} {row['Tool_Name']}: {row['Mention_Count']} mentions in {row['Reports_Count']} reports")

    print("=" * 80)
    return mentions_rows


def phase4_update_with_usage_tracking(tools, mentions_rows):
    """Phase 4: Update master CSV with usage tracking."""
    print("\n" + "=" * 80)
    print("PHASE 4: ADDING USAGE TRACKING TO MASTER CSV")
    print("=" * 80)

    # Create mention lookup
    mention_lookup = {row['TOL_ID']: row for row in mentions_rows}

    # Update tools with tracking data
    updated_tools = []
    for tool in tools:
        tol_id = tool['TOL_ID']
        mentions = mention_lookup.get(tol_id, {})

        count = mentions.get('Mention_Count', 0)
        last_used = mentions.get('Last_Mentioned', 'Never')

        # Determine testing status
        if count >= 5:
            testing_status = 'Actively Used'
            relevance = 'High'
        elif count >= 1:
            testing_status = 'Mentioned'
            relevance = 'Medium'
        else:
            testing_status = 'Testing Needed'
            relevance = 'Low'

        updated_tools.append({
            **tool,
            'Mention_Count': count,
            'Last_Used_Date': last_used,
            'Testing_Status': testing_status,
            'Relevance_Score': relevance
        })

    # Write updated CSV
    headers = ['TOL_ID', 'Category', 'Name', 'Description', 'Purpose', 'Cost',
               'Platforms', 'Tags', 'Status', 'Mention_Count', 'Last_Used_Date',
               'Testing_Status', 'Relevance_Score', 'Documentation_URL', 'Filename']

    with open(MASTER_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_tools)

    # Statistics
    actively_used = sum(1 for t in updated_tools if t['Testing_Status'] == 'Actively Used')
    mentioned = sum(1 for t in updated_tools if t['Testing_Status'] == 'Mentioned')
    testing_needed = sum(1 for t in updated_tools if t['Testing_Status'] == 'Testing Needed')

    print(f"[OK] Updated master CSV with usage tracking")
    print(f"\nUsage Statistics:")
    print(f"  Actively Used: {actively_used} tools (5+ mentions)")
    print(f"  Mentioned: {mentioned} tools (1-4 mentions)")
    print(f"  Testing Needed: {testing_needed} tools (0 mentions)")

    print("=" * 80)
    return updated_tools


def generate_usage_analysis(tools, mentions_rows, category_tools):
    """Generate comprehensive usage analysis report."""
    print("\n" + "=" * 80)
    print("GENERATING USAGE ANALYSIS REPORT")
    print("=" * 80)

    # Calculate statistics
    total_tools = len(tools)
    categories = Counter(t['Category'] for t in tools)

    actively_used = [t for t in tools if t.get('Testing_Status') == 'Actively Used']
    mentioned = [t for t in tools if t.get('Testing_Status') == 'Mentioned']
    testing_needed = [t for t in tools if t.get('Testing_Status') == 'Testing Needed']

    top_tools = sorted(mentions_rows, key=lambda x: x['Mention_Count'], reverse=True)[:20]
    never_mentioned = [t for t in tools if t.get('Mention_Count', 0) == 0]

    # Generate markdown report
    report = f"""# Tools Usage Analysis Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Tools:** {total_tools}

---

## Executive Summary

### Overall Statistics
- **Total Tools in Library:** {total_tools}
- **Categories:** {len(categories)}
- **Actively Used:** {len(actively_used)} tools (5+ mentions)
- **Mentioned:** {len(mentioned)} tools (1-4 mentions)
- **Testing Needed:** {len(testing_needed)} tools (no mentions)

### Usage Distribution
- **High Relevance:** {len([t for t in tools if t.get('Relevance_Score') == 'High'])} tools
- **Medium Relevance:** {len([t for t in tools if t.get('Relevance_Score') == 'Medium'])} tools
- **Low Relevance:** {len([t for t in tools if t.get('Relevance_Score') == 'Low'])} tools

---

## Category Breakdown

"""

    for cat, count in sorted(categories.items()):
        cat_tools = [t for t in tools if t['Category'] == cat]
        cat_actively_used = sum(1 for t in cat_tools if t.get('Testing_Status') == 'Actively Used')
        cat_mentioned = sum(1 for t in cat_tools if t.get('Testing_Status') == 'Mentioned')
        cat_testing = sum(1 for t in cat_tools if t.get('Testing_Status') == 'Testing Needed')

        report += f"""### {cat} ({count} tools)
- Actively Used: {cat_actively_used}
- Mentioned: {cat_mentioned}
- Testing Needed: {cat_testing}

"""

    report += f"""---

## Top 20 Most Used Tools

| Rank | TOL ID | Tool Name | Mentions | Reports | Departments |
|------|--------|-----------|----------|---------|-------------|
"""

    for i, tool in enumerate(top_tools, 1):
        report += f"| {i} | {tool['TOL_ID']} | {tool['Tool_Name']} | {tool['Mention_Count']} | {tool['Reports_Count']} | {tool['Departments']} |\n"

    report += f"""
---

## Tools Requiring Testing ({len(never_mentioned)} tools)

These tools have not been mentioned in any reports and may need evaluation:

"""

    for tool in never_mentioned[:30]:  # Show first 30
        report += f"- **{tool['TOL_ID']}**: {tool['Name']} ({tool['Category']})\n"

    if len(never_mentioned) > 30:
        report += f"\n... and {len(never_mentioned) - 30} more\n"

    report += f"""
---

## Recommendations

### High Priority (Actively Used Tools)
These {len(actively_used)} tools are actively used and should be:
- Maintained and updated regularly
- Documented thoroughly
- Monitored for licensing/costs
- Included in training materials

### Medium Priority (Mentioned Tools)
These {len(mentioned)} tools are mentioned occasionally:
- Evaluate for more frequent use
- Document use cases
- Consider expanding usage

### Low Priority (Testing Needed)
These {len(testing_needed)} tools need evaluation:
- Test functionality and relevance
- Determine if they should remain in library
- Archive or deprecate unused tools
- Update with clear use cases if valuable

---

## File References

- **Master Inventory:** `Tools_Master_Inventory.csv` ({total_tools} entries)
- **Category View:** `Tools_By_Category.csv` (organized by category)
- **Mentions Tracking:** `Tools_Mentions_Tracking.csv` (usage data)
- **This Report:** `Tools_Usage_Analysis.md`

---

*Report generated by final_cleanup_and_tracking.py*
"""

    with open(ANALYSIS_MD, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"[OK] Generated analysis report: {ANALYSIS_MD}")
    print("=" * 80)


def main():
    """Main execution."""
    print("\n" + "=" * 80)
    print(" TOOLS LIBRARY FINAL CLEANUP & TRACKING SYSTEM")
    print(" Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 80)

    # Phase 1: Clean up master CSV
    tools = phase1_clean_master_csv()

    # Phase 2: Create category-based view
    category_tools = phase2_create_category_view(tools)

    # Phase 3: Scan reports for mentions
    mentions_rows = phase3_scan_reports_for_mentions(tools)

    # Phase 4: Update with usage tracking
    updated_tools = phase4_update_with_usage_tracking(tools, mentions_rows)

    # Generate analysis report
    generate_usage_analysis(updated_tools, mentions_rows, category_tools)

    print("\n" + "=" * 80)
    print("[SUCCESS] ALL PHASES COMPLETE!")
    print("=" * 80)
    print("\nGenerated Files:")
    print(f"  1. {MASTER_CSV.name} (cleaned, with usage tracking)")
    print(f"  2. {CATEGORY_CSV.name} (organized by category)")
    print(f"  3. {MENTIONS_CSV.name} (detailed mentions tracking)")
    print(f"  4. {ANALYSIS_MD.name} (usage analysis report)")
    print("=" * 80)


if __name__ == "__main__":
    main()
