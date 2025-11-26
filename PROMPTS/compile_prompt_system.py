"""
Prompt System Compiler
Extracts and compiles all prompts from the PROMPTS directory into a comprehensive system
"""
import os
import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
MASTER_LIST = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"
OUTPUT_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\COMPILED_PROMPT_SYSTEM"

# Categories based on directory structure
CATEGORIES = {
    'CORE': 'Core System Prompts',
    'VIDEO': 'Video Processing',
    'HR': 'Human Resources',
    'DAILY_REPORTS': 'Daily Reports',
    'TAXONOMY': 'Taxonomy & System',
    'WORKFLOWS': 'Workflows & Operations',
    'AUTOMATION': 'Automation',
    'RESEARCH': 'Research',
    'LIBRARIES': 'Library Processing',
    'CREATIVES': 'Creative & Design',
    'DATA_ARCHITECTURE': 'Data Architecture',
    'UTILITIES': 'Utilities',
}

def load_master_list():
    """Load the master list CSV"""
    entries = []
    with open(MASTER_LIST, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        entries = list(reader)
    return entries

def categorize_prompt(file_path, entry):
    """Categorize prompt based on file path and metadata"""
    path_upper = file_path.upper()

    if 'CORE' in path_upper or entry['Current_ID'].startswith('PRM-CR'):
        return 'CORE'
    elif 'VIDEO' in path_upper or 'VID' in entry['Department']:
        return 'VIDEO'
    elif 'HR_OPERATIONS' in path_upper or 'HRM' in entry['Department']:
        return 'HR'
    elif 'DAILY_REPORTS' in path_upper or entry['Current_ID'].startswith('PRM-DR'):
        return 'DAILY_REPORTS'
    elif 'TAXONOMY' in path_upper or 'SYSTEM' in path_upper:
        return 'TAXONOMY'
    elif 'WORKFLOW' in path_upper or 'OPS' in entry['Department']:
        return 'WORKFLOWS'
    elif 'AUTOMATION' in path_upper:
        return 'AUTOMATION'
    elif 'RESEARCH' in path_upper:
        return 'RESEARCH'
    elif 'LIBRARY_PROCESSING' in path_upper:
        return 'LIBRARIES'
    elif 'CREATIVE' in path_upper or 'DGN' in entry['Department']:
        return 'CREATIVES'
    elif 'DATA_ARCHITECTURE' in path_upper:
        return 'DATA_ARCHITECTURE'
    elif 'UTILITIES' in path_upper:
        return 'UTILITIES'
    else:
        return 'OTHER'

def read_prompt_content(file_path):
    """Read prompt file content"""
    try:
        full_path = file_path.replace('ENTITIES/', r'C:\Users\Dell\Dropbox\ENTITIES/')
        full_path = full_path.replace('/', '\\')

        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"[File not found: {full_path}]"
    except Exception as e:
        return f"[Error reading file: {str(e)}]"

def extract_description(content):
    """Extract description from prompt content"""
    lines = content.split('\n')[:50]  # First 50 lines

    # Look for common description patterns
    for i, line in enumerate(lines):
        if any(keyword in line.lower() for keyword in ['purpose:', 'description:', 'overview:', '## purpose', '## description']):
            # Get the next non-empty line
            for j in range(i+1, min(i+5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    return lines[j].strip()

    # Fallback: first paragraph
    for line in lines:
        if line.strip() and not line.startswith('#') and len(line.strip()) > 20:
            return line.strip()[:200]

    return "No description available"

def create_compiled_system():
    """Create comprehensive compiled prompt system"""
    print("=== PROMPT SYSTEM COMPILER ===\n")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load master list
    print("Loading Master List...")
    entries = load_master_list()
    print(f"Loaded {len(entries)} entries\n")

    # Categorize prompts
    print("Categorizing prompts...")
    categorized = defaultdict(list)

    for entry in entries:
        if entry['Status'] == 'Active':  # Only active prompts
            category = categorize_prompt(entry['File_Path'], entry)
            categorized[category].append(entry)

    print(f"Categorized into {len(categorized)} categories\n")

    # Create master index
    print("Creating Master Index...")
    create_master_index(categorized, entries)

    # Create category documents
    print("\nCreating category documents...")
    for category, prompts in categorized.items():
        create_category_document(category, prompts)

    # Create full compilation
    print("\nCreating full compilation...")
    create_full_compilation(categorized)

    # Create statistics
    print("\nCreating statistics...")
    create_statistics(categorized, entries)

    print(f"\n[SUCCESS] Compiled prompt system created in:")
    print(f"  {OUTPUT_DIR}")

def create_master_index(categorized, all_entries):
    """Create master index document"""
    content = f"""# COMPILED PROMPT SYSTEM - MASTER INDEX

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}
**Total Prompts:** {len(all_entries)}
**Active Prompts:** {sum(len(prompts) for prompts in categorized.values())}

---

## Overview

This is a comprehensive compilation of all prompts in the ENTITIES/PROMPTS system, organized by category and purpose.

---

## Categories

"""

    for category in sorted(categorized.keys()):
        prompts = categorized[category]
        category_name = CATEGORIES.get(category, category)
        content += f"### {category_name}\n"
        content += f"**Prompts:** {len(prompts)}  \n"
        content += f"**Document:** [{category}.md]({category}.md)\n\n"

    content += """
---

## Quick Reference

### By Department
"""

    # Group by department
    by_dept = defaultdict(int)
    for prompts in categorized.values():
        for p in prompts:
            by_dept[p['Department']] += 1

    for dept in sorted(by_dept.keys()):
        content += f"- **{dept}:** {by_dept[dept]} prompts\n"

    content += """
---

## Files in This Compilation

- `00_MASTER_INDEX.md` - This file
- `01_FULL_COMPILATION.md` - All prompts in one document
- `02_STATISTICS.md` - Detailed statistics
- `[CATEGORY].md` - Category-specific compilations

---

## Usage

1. **Quick lookup:** Use the Master Index (this file)
2. **Category browse:** Open specific category documents
3. **Full reference:** Use FULL_COMPILATION.md
4. **Statistics:** See STATISTICS.md for metrics

---

**Source:** ENTITIES/PROMPTS/PROMPTS_Master_List.csv
"""

    with open(os.path.join(OUTPUT_DIR, '00_MASTER_INDEX.md'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("  - Created 00_MASTER_INDEX.md")

def create_category_document(category, prompts):
    """Create document for specific category"""
    category_name = CATEGORIES.get(category, category)

    content = f"""# {category_name.upper()}

**Category:** {category}
**Total Prompts:** {len(prompts)}

---

## Prompts in This Category

"""

    for prompt in sorted(prompts, key=lambda x: x['New_ID']):
        content += f"""
### {prompt['New_ID']}: {prompt['Name']}

**Current ID:** {prompt['Current_ID']}
**Department:** {prompt['Department']}
**Status:** {prompt['Status']}
**File:** `{prompt['File_Path']}`

**Description:**
{prompt['Description']}

---
"""

    filename = f"{category}.md"
    with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  - Created {filename}")

def create_full_compilation(categorized):
    """Create full compilation of all prompts"""
    content = f"""# FULL PROMPT SYSTEM COMPILATION

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

This document contains ALL active prompts in the system, organized by category.

---

"""

    for category in sorted(categorized.keys()):
        prompts = categorized[category]
        category_name = CATEGORIES.get(category, category)

        content += f"""
# {category_name.upper()}

**Prompts in category:** {len(prompts)}

---

"""

        for prompt in sorted(prompts, key=lambda x: x['New_ID']):
            content += f"""
## {prompt['New_ID']}: {prompt['Name']}

**Current ID:** {prompt['Current_ID']}
**Department:** {prompt['Department']}
**File:** `{prompt['File_Path']}`

**Description:**
{prompt['Description']}

---

"""

    with open(os.path.join(OUTPUT_DIR, '01_FULL_COMPILATION.md'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("  - Created 01_FULL_COMPILATION.md")

def create_statistics(categorized, all_entries):
    """Create statistics document"""
    from collections import Counter

    active_count = sum(len(prompts) for prompts in categorized.values())

    # Department stats
    dept_counter = Counter()
    status_counter = Counter()

    for entry in all_entries:
        dept_counter[entry['Department']] += 1
        status_counter[entry['Status']] += 1

    content = f"""# PROMPT SYSTEM STATISTICS

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Overall Statistics

- **Total Prompts:** {len(all_entries)}
- **Active Prompts:** {active_count}
- **Deprecated Prompts:** {status_counter.get('Deprecated', 0)}
- **Draft Prompts:** {status_counter.get('Draft', 0)}
- **Categories:** {len(categorized)}

---

## By Category

"""

    for category in sorted(categorized.keys()):
        category_name = CATEGORIES.get(category, category)
        content += f"- **{category_name}:** {len(categorized[category])} prompts\n"

    content += """
---

## By Department

"""

    for dept, count in dept_counter.most_common():
        content += f"- **{dept}:** {count} prompts\n"

    content += """
---

## By Status

"""

    for status, count in status_counter.items():
        content += f"- **{status}:** {count} prompts\n"

    content += f"""
---

## PMT-Numbered Prompts

Total PMT-numbered prompts: {sum(1 for e in all_entries if e['Current_ID'].startswith('PMT-'))}

**PMT Range:** PMT-001 to PMT-092

---

## Growth Metrics

- **PRM Range:** PRM-001 to PRM-{all_entries[-1]['New_ID'].split('-')[1]}
- **Categories Covered:** {len(categorized)}
- **Departments Served:** {len(dept_counter)}

---
"""

    with open(os.path.join(OUTPUT_DIR, '02_STATISTICS.md'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("  - Created 02_STATISTICS.md")

if __name__ == '__main__':
    create_compiled_system()
