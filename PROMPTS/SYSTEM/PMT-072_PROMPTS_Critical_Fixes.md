---
PMT_ID: PMT-072
Title: PROMPTS Entity - Critical Fixes Workflow
Category: SYSTEM
Department: AID
Version: 1.0
Status: Active
Created: 2025-11-19
Last_Updated: 2025-11-19
Author: AI & Automation Team
Tags: [fixes, validation, data-quality, system-maintenance]
Dependencies: [PMT-028]
Referenced_Entities: [PROMPTS, REPORTS]
---

# PROMPTS Entity - Critical Fixes Workflow

## Purpose
Execute critical fixes identified in the PROMPTS Entity Analysis Report to resolve breaking issues and establish data consistency.

## Context
Following the PROMPTS reorganization on 2025-11-19, several critical issues were identified that require immediate resolution to ensure system stability and data integrity. This prompt guides the systematic resolution of all Priority 0 (P0) critical issues.

## Input Requirements
- PROMPTS Entity Analysis Report (C:\Users\Dell\Dropbox\ENTITIES\REPORTS\System_Analysis\PROMPTS_Entity_Analysis_2025-11-19.md)
- PMT_Master_List.csv (C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DATA_FIELDS\PMT_Master_List.csv)
- Access to PROMPTS folder structure

## Expected Output
- All critical issues resolved
- Updated master CSV with corrected paths
- Validated file structure with zero broken references
- Updated ISO Code Registry documentation
- Validation report confirming fixes

---

## Instructions

### Phase 1: Resolve PMT-013 Missing File

**Objective:** Locate or recreate the missing PMT-013 file.

#### Step 1: Search for File
```bash
# Search for file with various naming patterns
cd "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
find . -iname "*merge*transcr*" -type f
find . -iname "*PMT-013*" -type f
find . -iname "*transcribation*" -type f
```

#### Step 2: Check Backup Locations
Search in:
- Recycle Bin / Trash
- Git history (if versioned): `git log --all --full-history -- "*PMT-013*"`
- Backup folders: `_ARCHIVE/`, `WORKFLOWS/`
- Previous session temp files

#### Step 3: Decision Matrix

**If file is found:**
1. Move to correct location: `PROMPTS/Workflows/PMT-013_Merge_Transcriptions_Research.md`
2. Update master CSV path
3. Validate file content
4. Mark as resolved

**If file is NOT found:**
1. **Option A - Recreate from purpose:**
   - Review description: "Merge video transcriptions with research integration"
   - Check related prompts: PMT-004 (Video Transcription), PMT-051 (Research Integration)
   - Recreate logical workflow combining both

2. **Option B - Mark as deprecated:**
   - Update master CSV: Status = "Missing"
   - Add note: "File lost during reorganization 2025-11-19"
   - Consider creating replacement with new PMT ID

3. **Option C - Reassign PMT-013:**
   - If creating entirely new prompt, reassign PMT-013 to new content
   - Document in version history

**Recommended Action:** Recreate from purpose (Option A)

#### Step 4: Create Placeholder (If Recreating)
```markdown
---
PMT_ID: PMT-013
Title: Merge Transcriptions Research
Category: VIDEO
Department: VID
Version: 1.0
Status: Active
Created: 2025-11-19 (Recreated)
Last_Updated: 2025-11-19
Author: AI & Automation Team
Tags: [video, research, integration, workflow]
Dependencies: [PMT-004, PMT-051]
Referenced_Entities: [TASK_MANAGERS, LIBRARIES]
---

# Merge Video Transcriptions with Research Integration

## Purpose
Combine video transcription entity extraction (TASK_MANAGERS) with research findings integration to create comprehensive knowledge base entries.

## Workflow
1. Extract entities from video transcriptions using PMT-004
2. Gather related research using PMT-051
3. Cross-reference and merge findings
4. Generate integrated knowledge entries
5. Update taxonomy references

## Input
- Video transcription output (with MLS-###, TSK-###, STP-### entities)
- Research documents related to video topic

## Output
- Merged document with:
  - Extracted TASK_MANAGERS entities
  - Integrated research context
  - Cross-referenced LIBRARIES entities
  - Taxonomy mappings
```

---

### Phase 2: Fix Path Inconsistencies in Master CSV

**Objective:** Ensure all file paths in PMT_Master_List.csv match physical file locations.

#### Step 1: Identify Affected Entries

Review analysis report for path mismatches:
- PMT-014 to PMT-020: `Taxonomy/` → `SYSTEM/Taxonomy/`
- PMT-058, PMT-059: Verify location in `WORKFLOWS/Operational_Workflows/`

#### Step 2: Update Taxonomy Paths
```bash
cd "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DATA_FIELDS"

# Update paths for Taxonomy folder
# Option 1: Using sed
sed -i 's|,Taxonomy/|,SYSTEM/Taxonomy/|g' PMT_Master_List.csv

# Option 2: Using Python
python << 'EOF'
import csv

# Read CSV
with open('PMT_Master_List.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Update paths
updated = []
for line in lines:
    if ',Taxonomy/' in line:
        line = line.replace(',Taxonomy/', ',SYSTEM/Taxonomy/')
    updated.append(line)

# Write back
with open('PMT_Master_List.csv', 'w', encoding='utf-8') as f:
    f.writelines(updated)

print("Updated Taxonomy paths")
EOF
```

#### Step 3: Verify File Existence
```python
import csv
from pathlib import Path

errors = []
base_path = Path('C:/Users/Dell/Dropbox/ENTITIES/PROMPTS')

with open('DATA_FIELDS/PMT_Master_List.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        file_path = base_path / row['File_Path']
        if not file_path.exists():
            errors.append(f"{row['PMT_ID']}: {row['File_Path']}")

if errors:
    print(f"❌ Found {len(errors)} missing files:")
    for error in errors:
        print(f"  - {error}")
else:
    print("✅ All file paths validated successfully")
```

#### Step 4: Update JSON Index
```bash
cd "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DATA_FIELDS"
python << 'EOF'
import csv
import json
from datetime import datetime

# Read CSV
with open('PMT_Master_List.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    prompts = list(reader)

# Create index
index = {
    'meta': {
        'entity': 'PROMPTS',
        'iso_code': 'PMT',
        'total_prompts': len(prompts),
        'last_updated': datetime.now().isoformat(),
        'version': '2.0'
    },
    'prompts': [
        {
            'id': p['PMT_ID'],
            'name': p['Name'],
            'category': p['Category'],
            'department': p['Department'],
            'path': p['File_Path'],
            'status': p['Status'],
            'version': p['Version']
        } for p in prompts
    ]
}

# Write JSON
with open('Prompts_Index.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2)

print(f"✅ Updated Prompts_Index.json with {len(prompts)} prompts")
EOF
```

---

### Phase 3: Update ISO Code Registry Documentation

**Objective:** Align Prompts_ISO_Code_Registry.md with the implemented simple PMT-### system.

#### Step 1: Read Current Registry
Location: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\SYSTEM\Taxonomy\Prompts_ISO_Code_Registry.md`

#### Step 2: Identify Outdated Sections
Remove/update references to:
- Hierarchical PMT-{CATEGORY}-{###} format
- Category-based sub-codes (PMT-COR-001, PMT-VID-018, etc.)
- Department-specific codes (PMT-DLY-AIA, etc.)

#### Step 3: Rewrite Key Sections

**Update Section: "Core Entity Type Code"**
```markdown
## Core Entity Type Code

### Primary Entity Type

| ISO Code | Entity Type | Consonant-Only | Description | Total Count |
|----------|-------------|----------------|-------------|-------------|
| **PMT** | Prompts | Yes | AI prompts and custom instructions | 71 cataloged |

**Format:** PMT-### (simple sequential)
- PMT-001, PMT-002, PMT-003... PMT-071
- No category prefixes
- No hierarchical sub-codes
- Sequential numbering without gaps
```

**Update Section: "ID Assignment Process"**
```markdown
## ID Assignment Process

### When Creating New Prompts

1. **Check Next Available ID**
   - Review PMT_Master_List.csv
   - Find highest PMT-### number
   - Assign next sequential number (e.g., if last is PMT-071, use PMT-072)

2. **No Category Prefixes**
   - ❌ WRONG: PMT-VID-012, PMT-TAX-005
   - ✅ CORRECT: PMT-012, PMT-005

3. **Format File Name**
   - Pattern: PMT-{###}_{Descriptive_Name}.md
   - Example: PMT-072_System_Validation.md

4. **Update Master CSV**
   - Add row with all metadata
   - Update Last_Updated field
   - Regenerate Prompts_Index.json
```

**Add Section: "Migration from v1.0 to v2.0"**
```markdown
## Migration Notes

### Version 1.0 → 2.0 Changes (2025-11-19)

**What Changed:**
- Moved from hierarchical PMT-{CAT}-{###} to simple PMT-###
- Removed category-based sub-codes
- Simplified to match TASK_MANAGERS taxonomy pattern

**Old Format (Deprecated):**
- PMT-COR-001 (Core category, prompt 1)
- PMT-VID-018 (Video category, prompt 18)
- PMT-DLY-AIA (Daily reports, AI & Automation)

**New Format (Current):**
- PMT-001 (Sequential)
- PMT-018 (Sequential)
- PMT-033 (Sequential)

**Why the Change:**
- Consistency with TASK_MANAGERS (MLT-001, TSK-001)
- Simpler ID management
- No category conflicts
- Easier automation
```

#### Step 4: Validate Updated Documentation
- Ensure all examples use PMT-### format
- Remove all PMT-CAT-### references
- Update version history to 2.0
- Add "Last Updated: 2025-11-19"

---

### Phase 4: Standardize Folder Structure

**Objective:** Move root-level files to appropriate subfolders for consistency.

#### Files to Move:

**1. WORKFLOWS folder:**
```bash
cd "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\WORKFLOWS"

# Verify current location
ls -la PMT-058_Call_Organizer_v4.md
ls -la PMT-059_Document_Finished_Project.md

# Move to Operational_Workflows (if not already there)
mv PMT-058_Call_Organizer_v4.md Operational_Workflows/
mv PMT-059_Document_Finished_Project.md Operational_Workflows/

# Update CSV paths
# WORKFLOWS/ → WORKFLOWS/Operational_Workflows/
```

**2. RESEARCH folder:**
```bash
cd "C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\RESEARCH"

# Check current structure
ls -la PMT-051*.md
ls -la PMT-052*.md

# Option A: Create Integration subfolder
mkdir -p Integration
mv PMT-051_Department_Research_Integration.md Integration/

# Option B: Move to Research_Prompts
mv PMT-052_VSCode_AI_Extensions.md Research_Prompts/
```

**3. Update Master CSV:**
```python
import csv

updates = {
    'PMT-058': 'WORKFLOWS/Operational_Workflows/PMT-058_Call_Organizer_v4.md',
    'PMT-059': 'WORKFLOWS/Operational_Workflows/PMT-059_Document_Finished_Project.md',
    'PMT-051': 'RESEARCH/Integration/PMT-051_Department_Research_Integration.md',
    'PMT-052': 'RESEARCH/Research_Prompts/PMT-052_VSCode_AI_Extensions.md'
}

# Read CSV
with open('PMT_Master_List.csv', 'r') as f:
    lines = f.readlines()

# Update paths
updated_lines = []
for line in lines:
    for pmt_id, new_path in updates.items():
        if line.startswith(pmt_id + ','):
            parts = line.split(',')
            parts[6] = new_path  # File_Path column
            line = ','.join(parts)
    updated_lines.append(line)

# Write back
with open('PMT_Master_List.csv', 'w') as f:
    f.writelines(updated_lines)

print("✅ Updated file paths in master CSV")
```

---

### Phase 5: Final Validation

#### Step 1: Run Comprehensive Validation
```python
#!/usr/bin/env python3
import csv
from pathlib import Path

def validate_prompts_entity():
    """Comprehensive validation of PROMPTS entity"""

    base_path = Path('C:/Users/Dell/Dropbox/ENTITIES/PROMPTS')
    csv_path = base_path / 'DATA_FIELDS/PMT_Master_List.csv'

    issues = []
    warnings = []

    # Load CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        prompts = list(reader)

    print(f"📊 Validating {len(prompts)} prompts...\n")

    # Validation 1: File existence
    print("1️⃣ Checking file existence...")
    for prompt in prompts:
        file_path = base_path / prompt['File_Path']
        if not file_path.exists():
            if prompt['Status'] == 'Missing':
                warnings.append(f"⚠️  {prompt['PMT_ID']}: Documented as missing - {prompt['File_Path']}")
            else:
                issues.append(f"❌ {prompt['PMT_ID']}: File not found - {prompt['File_Path']}")

    # Validation 2: Duplicate IDs
    print("2️⃣ Checking for duplicate IDs...")
    ids = [p['PMT_ID'] for p in prompts]
    duplicates = [id for id in ids if ids.count(id) > 1]
    if duplicates:
        issues.append(f"❌ Duplicate IDs found: {set(duplicates)}")

    # Validation 3: Sequential numbering
    print("3️⃣ Checking sequential numbering...")
    numbers = sorted([int(p['PMT_ID'].split('-')[1]) for p in prompts])
    expected = list(range(1, numbers[-1] + 1))
    gaps = [n for n in expected if n not in numbers]
    if gaps:
        warnings.append(f"⚠️  Gaps in numbering: PMT-{','.join(f'{n:03d}' for n in gaps)}")

    # Validation 4: Required metadata
    print("4️⃣ Checking required metadata...")
    for prompt in prompts:
        if not prompt['Description'] or len(prompt['Description']) < 20:
            warnings.append(f"⚠️  {prompt['PMT_ID']}: Short/missing description")
        if not prompt['Category']:
            issues.append(f"❌ {prompt['PMT_ID']}: Missing category")
        if not prompt['Department']:
            issues.append(f"❌ {prompt['PMT_ID']}: Missing department")

    # Validation 5: Version format
    print("5️⃣ Checking version format...")
    for prompt in prompts:
        if '.' not in prompt['Version']:
            warnings.append(f"⚠️  {prompt['PMT_ID']}: Version missing minor number - {prompt['Version']}")

    # Report
    print("\n" + "="*60)
    print("📋 VALIDATION REPORT")
    print("="*60)

    if not issues and not warnings:
        print("✅ All validations passed! PROMPTS entity is fully consistent.")
    else:
        if issues:
            print(f"\n❌ CRITICAL ISSUES ({len(issues)}):")
            for issue in issues:
                print(f"   {issue}")

        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for warning in warnings:
                print(f"   {warning}")

    print("\n" + "="*60)
    print(f"📊 Summary: {len(prompts)} prompts | {len(issues)} issues | {len(warnings)} warnings")
    print("="*60)

    return len(issues) == 0

if __name__ == '__main__':
    success = validate_prompts_entity()
    exit(0 if success else 1)
```

#### Step 2: Generate Validation Report
Save output to: `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\System_Analysis\PROMPTS_Validation_Report_2025-11-19.md`

---

## Success Criteria

✅ **Critical fixes completed when:**
1. PMT-013 file exists or is documented as recreated/missing
2. 100% of file paths in CSV match physical files
3. Zero broken references in master catalog
4. ISO Code Registry updated to reflect v2.0 system
5. All root-level files moved to subfolders
6. Validation script passes with 0 critical issues

## Deliverables

1. **Updated PMT_Master_List.csv** - All paths corrected
2. **Updated Prompts_Index.json** - Regenerated from corrected CSV
3. **Updated Prompts_ISO_Code_Registry.md** - Reflects simple PMT-### system
4. **PMT-013 file** - Recreated or documented
5. **Validation Report** - Confirms all fixes applied
6. **Migration Log** - Documents all changes made

## Related Prompts
- PMT-028 - Folder Reorganization
- PMT-029 - System Health Review
- PMT-022 - Data Inventory

## Version History

### v1.0 (2025-11-19)
**Changes:**
- Initial version created from PROMPTS Entity Analysis Report
- Covers all Priority 0 critical fixes
- Includes validation scripts and success criteria

**Author:** AI & Automation Team
