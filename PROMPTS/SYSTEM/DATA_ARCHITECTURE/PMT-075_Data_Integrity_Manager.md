# PMT-075: Data Integrity Manager v1.0

**Prompt ID:** PMT-075
**Version:** 1.0
**Department:** System Architecture
**Category:** DATA_INTEGRITY
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

Specialized sub-prompt for maintaining internal data integrity across the ENTITIES ecosystem. Validates schemas, checks cross-references, detects duplicates, automates ID assignment, and ensures consistency across all 21 entities.

**Core Functions:**
1. **Schema Validation**: Verify structure of all master lists (JSON/CSV)
2. **Cross-Reference Checking**: Ensure hierarchical integrity (PRT→MLT→TSK→STT→Item)
3. **Duplicate Detection**: Find and resolve duplicate entities (similarity threshold: 0.6)
4. **ID Assignment Automation**: Generate next available IDs (TOL-###, ACT-###, TSK-###, etc.)
5. **Consistency Verification**: Check naming conventions, status values, department codes
6. **Cleanup Operations**: Remove redundancies, fix broken references, archive deprecated entities

---

## Scope of Operations

### Internal Data Management Only

This prompt focuses on **internal operations**:
- Data structure validation
- Master list integrity
- Cross-reference verification
- Schema compliance
- ID management
- Cleanup and optimization

**NOT included** (handled by other sub-prompts):
- External employee activity monitoring → PMT-077
- Import processing → PMT-076
- Cross-entity search → PMT-078
- Prompt synchronization → PMT-079
- Token optimization → PMT-080

---

## Entity Master List Registry

### Master Files to Validate

**LIBRARIES Entity**:
```
LIBRARIES/
├── Actions/actions_master.json                                    (429 entries)
├── Actions/action_variants_map.json                               (57 variations)
├── Objects/objects_master.json                                    (193+ entries)
├── Objects/object_variants_map.json                               (169 variations)
├── Tools/Tools_Master_List.csv                                    (177+ tools)
├── Responsibilities/responsibilities_master.json                  (209+ entries)
├── Responsibilities/phrase_matching_index.json                    (209 patterns)
└── Professions/professions_master.json                            (27+ entries)
```

**TASK_MANAGERS Entity**:
```
TASK_MANAGERS/
├── TSM-001_Project_Templates/Project_Templates_Master_List.csv
├── TSM-002_Milestone_Templates/Milestone_Templates_Master_List.csv
├── TSM-003_Task_Templates/Task_Templates_Master_List.csv           (71 tasks)
├── TSM-004_Step_Templates/Step_Templates_Master_List.csv
├── TSM-005_Checklist_Items/Checklist_Items_Master_List.csv
├── TSM-005_Checklist_Items/CHT-001_Item_101_to_Item_110.json
├── TSM-005_Checklist_Items/CHT-002_Item_111_to_Item_145.json
└── TSM-006_Workflows/ (workflow definitions)
```

**PROMPTS Entity**:
```
PROMPTS/DATA_FIELDS/
├── PMT_Master_List.csv                                             (73+ prompts)
└── Prompts_Index.json
```

---

## Validation Operations

### Operation 1: Schema Validation

**Objective**: Ensure all master lists comply with expected schemas

**Process**:
1. Load Entity_Schema_Registry.json (defines expected schemas)
2. For each master list:
   - Load file (JSON or CSV)
   - Parse structure
   - Validate against schema:
     * Required fields present?
     * Correct data types?
     * Valid enum values (Status, Department, etc.)?
     * ID format matches pattern?
     * No missing or extra fields?
3. Generate validation report
4. Flag errors for remediation

**Example Validation**:
```python
# Expected schema for Task Templates
task_schema = {
    "New_ID": "string (format: TSK-###)",
    "Entity_Type": "string (enum: Task)",
    "Current_ID": "string or null",
    "Name": "string (PascalCase with underscores)",
    "Description": "string",
    "Department": "string (enum: AID, HRM, DEV, ...)",
    "File_Path": "string (relative path)",
    "Status": "string (enum: Active, In Progress, Paused, Completed, Deprecated)",
    "milestone_template_id": "string (format: MLT-###)",
    "Last_Updated": "string (format: YYYY-MM-DD)"
}

# Validate each row
for task in tasks_csv:
    validate_field(task, "New_ID", pattern=r"^TSK-\d{3}$")
    validate_field(task, "Status", enum=["Active", "In Progress", "Paused", "Completed", "Deprecated"])
    validate_field(task, "Department", enum=["AID", "HRM", "DEV", "DGN", "VID", ...])
    validate_field(task, "milestone_template_id", pattern=r"^MLT-\d{3}$")
```

**Output Report**:
```markdown
## Schema Validation Report

**File**: Task_Templates_Master_List.csv
**Date**: 2025-11-21
**Total Rows**: 71

### Issues Found:
1. Row 15 (TSK-015): Missing "Last_Updated" field
2. Row 32 (TSK-032): Invalid Department "AI" (should be "AID")
3. Row 48 (TSK-048): Invalid Status "WIP" (should be "In Progress")
4. Row 55 (TSK-055): Invalid milestone_template_id format "MLT-2" (should be "MLT-002")

### Summary:
- ✅ Valid: 67/71 (94%)
- ❌ Errors: 4/71 (6%)
- 🔧 Action Required: Fix 4 rows
```

---

### Operation 2: Cross-Reference Validation

**Objective**: Verify hierarchical integrity and bidirectional references

**Hierarchies to Validate**:
```
1. PRT ← MLT ← TSK ← STT ← Item
2. RSP → ACT + OBJ
3. Tool References (in tasks, steps, responsibilities)
4. Prompt References (in other prompts, documentation)
```

**Process**:
1. Load all related master lists
2. Build relationship graph
3. Check forward references (child → parent):
   - TSK.milestone_template_id exists in Milestones?
   - MLT.project_template_id exists in Projects?
   - STT.task_template_id exists in Tasks?
   - Item.parent_id exists in Steps or Tasks?
4. Check backward references (parent → children):
   - Does PRT have at least one MLT?
   - Does MLT have at least one TSK?
   - Optional: TSK may have 0+ STT
   - Optional: STT may have 0+ Items
5. Check status consistency:
   - Completed PRT shouldn't have Active MLTs
   - Deprecated MLT shouldn't have Active TSKs
6. Generate orphan report

**Example Cross-Reference Check**:
```python
# Validate TSK → MLT → PRT chain
def validate_task_chain(task_id):
    # Load master lists
    tasks = load_csv("Task_Templates_Master_List.csv")
    milestones = load_csv("Milestone_Templates_Master_List.csv")
    projects = load_csv("Project_Templates_Master_List.csv")

    # Find task
    task = tasks[tasks['New_ID'] == task_id].iloc[0]
    milestone_id = task['milestone_template_id']

    # Validate milestone exists
    if milestone_id not in milestones['New_ID'].values:
        return {
            "valid": False,
            "error": f"Milestone {milestone_id} not found",
            "task_id": task_id
        }

    # Find milestone
    milestone = milestones[milestones['New_ID'] == milestone_id].iloc[0]
    project_id = milestone['project_template_id']

    # Validate project exists
    if project_id not in projects['New_ID'].values:
        return {
            "valid": False,
            "error": f"Project {project_id} not found",
            "milestone_id": milestone_id
        }

    # Check status consistency
    if task['Status'] == 'Active' and milestone['Status'] == 'Deprecated':
        return {
            "valid": False,
            "error": f"Active task linked to Deprecated milestone",
            "warning": "Status inconsistency"
        }

    return {
        "valid": True,
        "chain": f"{task_id} → {milestone_id} → {project_id}",
        "task": task['Name'],
        "milestone": milestone['Name'],
        "project": projects[projects['New_ID'] == project_id].iloc[0]['Name']
    }
```

**Output Report**:
```markdown
## Cross-Reference Validation Report

**Hierarchy**: TSK → MLT → PRT
**Date**: 2025-11-21
**Total Tasks Checked**: 71

### Broken References:
1. TSK-023 → MLT-008 (NOT FOUND)
   - Error: Milestone MLT-008 does not exist
   - Action: Update TSK-023.milestone_template_id or create MLT-008

2. TSK-041 → MLT-005 → PRT-015 (NOT FOUND)
   - Error: Project PRT-015 does not exist
   - Action: Update MLT-005.project_template_id

### Status Inconsistencies:
1. TSK-055 (Active) → MLT-002 (Deprecated)
   - Warning: Active task linked to Deprecated milestone
   - Recommendation: Update TSK-055 status to Deprecated or reactivate MLT-002

### Orphans:
1. MLT-007 has 0 tasks
   - Info: Milestone exists but no tasks reference it
   - Action: Add tasks or mark as empty milestone template

### Summary:
- ✅ Valid Chains: 67/71 (94%)
- ❌ Broken References: 2/71 (3%)
- ⚠️  Status Issues: 1/71 (1%)
- ℹ️  Orphans: 1 milestone
```

---

### Operation 3: Duplicate Detection

**Objective**: Find and resolve duplicate entities using similarity matching

**Similarity Threshold**: 0.6 (configurable in config.json)

**Process**:
1. Load master list (e.g., Actions, Tools, Responsibilities)
2. Extract key fields (Name, Description)
3. Compute similarity scores between all pairs:
   - Exact match: score = 1.0
   - Levenshtein distance for strings
   - Token overlap for descriptions
   - Semantic similarity (optional, using embeddings)
4. Flag pairs with score ≥ threshold
5. Group similar entities into clusters
6. Recommend merge or mark as intentional duplicates

**Similarity Calculation**:
```python
from difflib import SequenceMatcher

def calculate_similarity(entity1, entity2):
    # Name similarity (weighted 60%)
    name_sim = SequenceMatcher(None, entity1['Name'].lower(), entity2['Name'].lower()).ratio()

    # Description similarity (weighted 30%)
    desc_sim = SequenceMatcher(None, entity1['Description'].lower(), entity2['Description'].lower()).ratio()

    # Department match bonus (weighted 10%)
    dept_match = 1.0 if entity1.get('Department') == entity2.get('Department') else 0.0

    # Weighted score
    total_sim = (name_sim * 0.6) + (desc_sim * 0.3) + (dept_match * 0.1)

    return total_sim

def find_duplicates(entities, threshold=0.6):
    duplicates = []

    for i in range(len(entities)):
        for j in range(i+1, len(entities)):
            sim_score = calculate_similarity(entities[i], entities[j])

            if sim_score >= threshold:
                duplicates.append({
                    "entity1_id": entities[i]['New_ID'],
                    "entity1_name": entities[i]['Name'],
                    "entity2_id": entities[j]['New_ID'],
                    "entity2_name": entities[j]['Name'],
                    "similarity": round(sim_score, 2),
                    "recommendation": "merge" if sim_score >= 0.85 else "review"
                })

    return duplicates
```

**Output Report**:
```markdown
## Duplicate Detection Report

**Entity Type**: Tools
**Master List**: Tools_Master_List.csv
**Threshold**: 0.6
**Date**: 2025-11-21

### High Similarity (≥0.85) - Merge Recommended:
1. TOL-042 "Claude AI" ↔ TOL-089 "Claude" (similarity: 0.92)
   - Recommendation: Merge → Keep TOL-042, deprecate TOL-089
   - Update references: 15 files reference TOL-089

2. TOL-015 "n8n Automation" ↔ TOL-067 "n8n" (similarity: 0.87)
   - Recommendation: Merge → Keep TOL-015, deprecate TOL-067
   - Update references: 8 files reference TOL-067

### Medium Similarity (0.6-0.84) - Review Recommended:
1. TOL-001 "ChatGPT" ↔ TOL-034 "GPT-4" (similarity: 0.72)
   - Note: May be intentional (different versions)
   - Action: Review and confirm if separate entities are needed

2. ACT-012 "Extract" ↔ ACT-089 "Pull Out" (similarity: 0.68)
   - Note: Different action verbs with similar meaning
   - Action: Decide if both variants are needed or merge

### Summary:
- Total Entities: 177
- High Similarity Pairs: 2 (merge recommended)
- Medium Similarity Pairs: 2 (review needed)
- Estimated Deduplication Savings: ~4 entities
```

---

### Operation 4: ID Assignment Automation

**Objective**: Generate next available IDs for new entities

**ID Format Registry**:
| Entity Type | Pattern | Example | Max Tracking File |
|-------------|---------|---------|-------------------|
| Actions | ACT-### | ACT-429 | actions_master.json |
| Objects | OBJ-### | OBJ-193 | objects_master.json |
| Tools | TOL-### | TOL-177 | Tools_Master_List.csv |
| Responsibilities | RSP-### | RSP-209 | responsibilities_master.json |
| Professions | PRF-### | PRF-027 | professions_master.json |
| Projects | PRT-### | PRT-008 | Project_Templates_Master_List.csv |
| Milestones | MLT-### | MLT-010 | Milestone_Templates_Master_List.csv |
| Tasks | TSK-### | TSK-071 | Task_Templates_Master_List.csv |
| Steps | STT-### | STT-155 | Step_Templates_Master_List.csv |
| Checklists | CHT-### | CHT-004 | Checklist_Items_Master_List.csv |
| Items | Item_### | Item_145 | Checklist_Items_Master_List.csv |
| Workflows | WFL-### | WFL-### | Workflows/ |
| Prompts | PMT-### | PMT-073 | PMT_Master_List.csv |

**Process**:
1. Identify entity type
2. Load master list
3. Find max ID:
   - Parse all IDs (e.g., TSK-001, TSK-002, ..., TSK-071)
   - Extract numeric part
   - Find maximum
4. Generate next ID:
   - Max + 1
   - Format with leading zeros (e.g., TSK-072)
5. Validate uniqueness
6. Reserve ID (mark as pending until entity created)
7. Return new ID

**Implementation**:
```python
import re
import pandas as pd

def get_next_id(entity_type):
    """
    Get next available ID for entity type

    Args:
        entity_type: One of ["Actions", "Tools", "Tasks", "Milestones", etc.]

    Returns:
        str: Next available ID (e.g., "TSK-072")
    """

    # Entity type configuration
    config = {
        "Actions": {
            "prefix": "ACT",
            "file": "LIBRARIES/Actions/actions_master.json",
            "id_field": "id"
        },
        "Tools": {
            "prefix": "TOL",
            "file": "LIBRARIES/Tools/Tools_Master_List.csv",
            "id_field": "tool_id"
        },
        "Tasks": {
            "prefix": "TSK",
            "file": "TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv",
            "id_field": "New_ID"
        },
        "Prompts": {
            "prefix": "PMT",
            "file": "PROMPTS/DATA_FIELDS/PMT_Master_List.csv",
            "id_field": "PMT_ID"
        }
    }

    if entity_type not in config:
        raise ValueError(f"Unknown entity type: {entity_type}")

    entity_config = config[entity_type]
    prefix = entity_config["prefix"]
    file_path = entity_config["file"]
    id_field = entity_config["id_field"]

    # Load master list
    if file_path.endswith('.json'):
        import json
        with open(file_path, 'r') as f:
            data = json.load(f)
        ids = [item[id_field] for item in data]
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        ids = df[id_field].tolist()

    # Extract numeric parts
    pattern = rf"{prefix}-(\d{{3}})"
    numbers = []
    for id_str in ids:
        match = re.match(pattern, str(id_str))
        if match:
            numbers.append(int(match.group(1)))

    # Find max and generate next
    max_num = max(numbers) if numbers else 0
    next_num = max_num + 1
    next_id = f"{prefix}-{next_num:03d}"

    # Validate uniqueness
    if next_id in ids:
        raise ValueError(f"ID collision: {next_id} already exists")

    return {
        "entity_type": entity_type,
        "next_id": next_id,
        "current_max": f"{prefix}-{max_num:03d}",
        "total_entities": len(ids),
        "generated_at": "2025-11-21"
    }

# Usage
next_task_id = get_next_id("Tasks")
# Returns: {"next_id": "TSK-072", "current_max": "TSK-071", ...}
```

**Output Report**:
```markdown
## ID Assignment Report

**Date**: 2025-11-21

### Next Available IDs:

| Entity Type | Current Max | Next ID | Total Count |
|-------------|-------------|---------|-------------|
| Actions | ACT-429 | ACT-430 | 429 |
| Objects | OBJ-193 | OBJ-194 | 193 |
| Tools | TOL-177 | TOL-178 | 177 |
| Responsibilities | RSP-209 | RSP-210 | 209 |
| Tasks | TSK-071 | TSK-072 | 71 |
| Milestones | MLT-010 | MLT-011 | 10 |
| Projects | PRT-008 | PRT-009 | 8 |
| Steps | STT-155 | STT-156 | 155 |
| Checklist Items | Item_145 | Item_146 | 45 (Item_101-145) |
| Prompts | PMT-073 | PMT-074 | 73 |

### Reserved IDs (Pending Creation):
- TSK-072: Process AI Training Data (reserved 2025-11-21)
- TOL-178: Perplexity AI (reserved 2025-11-20)

### Warnings:
- ⚠️  Gap detected: TSK-034 missing (TSK-033 → TSK-035)
- ℹ️  Suggested action: Investigate or fill gap
```

---

### Operation 5: Consistency Verification

**Objective**: Check naming conventions, status values, department codes

**Validation Rules**:

**1. Naming Conventions**:
- PascalCase with underscores: `Process_Department_Task_Files` ✅
- No spaces in IDs: `TSK-055_Process_Department_Task_Files` ✅
- No special characters except underscores
- No leading/trailing spaces

**2. Status Values** (must be one of):
- Active
- In Progress
- Paused
- Completed
- Deprecated

**3. Department Codes** (must be one of):
- AID (AI & Automation)
- HRM (Human Resources)
- DEV (Development)
- DGN (Design)
- VID (Video Production)
- LGN (Lead Generation)
- SLS (Sales)
- MKT (Marketing)
- SMM (Social Media)
- FNC (Finance)
- CNT (Content)
- Multi (Multi-department)
- OPS (Operations)

**4. Date Formats**:
- YYYY-MM-DD (ISO 8601)

**5. File Paths**:
- Relative to ENTITIES/
- Use forward slashes: `LIBRARIES/Actions/`
- No absolute paths

**Process**:
```python
def verify_consistency(master_list_file, entity_type):
    df = pd.read_csv(master_list_file)
    issues = []

    # Check naming convention
    for idx, row in df.iterrows():
        name = row['Name']

        # Check for spaces
        if ' ' in name and entity_type != "Description":
            issues.append({
                "row": idx + 1,
                "id": row['New_ID'],
                "issue": "Name contains spaces (should use underscores)",
                "value": name,
                "severity": "medium"
            })

        # Check for special characters
        if not re.match(r'^[A-Za-z0-9_]+$', name):
            issues.append({
                "row": idx + 1,
                "id": row['New_ID'],
                "issue": "Name contains invalid characters",
                "value": name,
                "severity": "high"
            })

    # Check status values
    valid_statuses = ["Active", "In Progress", "Paused", "Completed", "Deprecated"]
    for idx, row in df.iterrows():
        status = row['Status']
        if status not in valid_statuses:
            issues.append({
                "row": idx + 1,
                "id": row['New_ID'],
                "issue": f"Invalid status '{status}'",
                "expected": valid_statuses,
                "severity": "high"
            })

    # Check department codes
    valid_depts = ["AID", "HRM", "DEV", "DGN", "VID", "LGN", "SLS", "MKT", "SMM", "FNC", "CNT", "Multi", "OPS"]
    for idx, row in df.iterrows():
        if 'Department' in row:
            dept = row['Department']
            if dept not in valid_depts:
                issues.append({
                    "row": idx + 1,
                    "id": row['New_ID'],
                    "issue": f"Invalid department code '{dept}'",
                    "expected": valid_depts,
                    "severity": "medium"
                })

    return issues
```

**Output Report**:
```markdown
## Consistency Verification Report

**File**: Task_Templates_Master_List.csv
**Date**: 2025-11-21
**Total Rows**: 71

### High Severity Issues (Must Fix):
1. Row 23 (TSK-023): Invalid status "WIP"
   - Expected: ["Active", "In Progress", "Paused", "Completed", "Deprecated"]
   - Action: Change to "In Progress"

2. Row 41 (TSK-041): Name contains invalid character "/"
   - Current: "Setup_API/Integration"
   - Action: Change to "Setup_API_Integration"

### Medium Severity Issues (Should Fix):
1. Row 15 (TSK-015): Name contains spaces
   - Current: "Extract Taxonomy Videos"
   - Action: Change to "Extract_Taxonomy_Videos"

2. Row 32 (TSK-032): Invalid department "AI"
   - Expected: "AID"
   - Action: Update department code

### Summary:
- ✅ Compliant: 67/71 (94%)
- ⚠️  Medium Issues: 2 (3%)
- ❌ High Issues: 2 (3%)
```

---

### Operation 6: Cleanup Operations

**Objective**: Remove redundancies, fix broken references, archive deprecated entities

**Cleanup Tasks**:

**A. Nested Backup Cleanup**:
```
Problem: 8+ levels of nested backups in LIBRARIES/backup_20251119_055410/
Impact: ~2GB wasted space

Action Plan:
1. Identify nested backup folders (depth > 2)
2. Calculate total size
3. Keep only top-level backup with clear date
4. Move to ARCHIVE/Backups/ with naming: LIBRARIES_backup_YYYYMMDD
5. Delete nested redundancies
6. Generate cleanup report
```

**B. Broken Reference Fix**:
```
Problem: TSK-023 → MLT-008 (MLT-008 not found)

Action Options:
1. Create missing MLT-008 (if intentional)
2. Update TSK-023.milestone_template_id to existing milestone
3. Mark TSK-023 as orphaned for manual review
4. Deprecate TSK-023 if no longer needed
```

**C. Deprecated Entity Archival**:
```
Process:
1. Find all entities with Status = "Deprecated"
2. Check if any Active entities reference them
3. If no active references:
   - Move to ARCHIVE/ folder
   - Update master list (mark as archived)
   - Generate migration report
4. If active references exist:
   - Flag for manual review (active entity referencing deprecated)
```

**D. Orphan Resolution**:
```
Orphan Types:
1. Milestones with 0 tasks
2. Projects with 0 milestones
3. Steps with invalid task_template_id
4. Checklist items with invalid parent_id

Action Plan:
1. Identify all orphans
2. Categorize by type
3. Options:
   - Add missing children (create tasks for empty milestones)
   - Remove orphan (if unintentional)
   - Mark as valid template (intentionally childless)
```

**Output Report**:
```markdown
## Cleanup Operations Report

**Date**: 2025-11-21

### Backup Cleanup:
- Nested folders found: LIBRARIES/backup_20251119_055410/ (8 levels deep)
- Total size: 2.3 GB
- Action: Moved to ARCHIVE/Backups/LIBRARIES_backup_20251119/
- Space recovered: 2.1 GB

### Broken References Fixed:
1. TSK-023 → MLT-008 (missing)
   - Action: Updated to MLT-002 (similar milestone)
   - Verified: MLT-002 exists and active

2. STT-089 → TSK-099 (missing)
   - Action: Deprecated STT-089 (task no longer exists)

### Deprecated Entities Archived:
- TOL-089 "Claude" (deprecated 2025-11-15, merged into TOL-042)
  - No active references found
  - Moved to ARCHIVE/Tools/TOL-089_Claude.json

### Orphans Resolved:
- MLT-007 (0 tasks)
  - Action: Marked as valid empty template (milestone for future use)
  - Added note: "Template for future feature development milestones"

### Summary:
- ✅ Backups cleaned: 2.1 GB recovered
- ✅ References fixed: 2
- ✅ Entities archived: 1
- ✅ Orphans resolved: 1
```

---

## Common Validation Workflows

### Workflow 1: Full System Validation

**Use Case**: Monthly data integrity audit

**Steps**:
1. Run Schema Validation on all master lists
2. Run Cross-Reference Validation for all hierarchies
3. Run Duplicate Detection (threshold: 0.6)
4. Run Consistency Verification
5. Generate comprehensive report
6. Prioritize issues by severity
7. Create remediation plan

**Estimated Time**: 30-45 minutes

---

### Workflow 2: Pre-Import Validation

**Use Case**: Before integrating new entities from IMPORTS/

**Steps**:
1. Load new entities from IMPORTS/[date]/Extraction/
2. Run Schema Validation on new data
3. Run Duplicate Detection (compare against existing entities)
4. Assign new IDs (if no duplicates found)
5. Validate cross-references (if hierarchical entities)
6. Generate import readiness report
7. If all valid → proceed to PMT-076 (Import Validation Pipeline)
8. If issues found → flag for manual review

**Estimated Time**: 10-15 minutes

---

### Workflow 3: Post-Migration Validation

**Use Case**: After major data restructuring or migrations

**Steps**:
1. Run Full System Validation (Workflow 1)
2. Compare counts (before vs after):
   - Total entities per type
   - Active vs Deprecated
   - Orphaned entities
3. Verify all cross-references still valid
4. Check for introduced duplicates
5. Validate file paths updated correctly
6. Generate migration validation report

**Estimated Time**: 45-60 minutes

---

### Workflow 4: Quick Health Check

**Use Case**: Daily/weekly routine check

**Steps**:
1. Check master list file integrity (files exist, parseable)
2. Count total entities per type
3. Find recent changes (Last_Updated in last 7 days)
4. Quick cross-reference spot check (sample 10 random entities)
5. Generate health status (Green/Yellow/Red)

**Estimated Time**: 5 minutes

---

## Best Practices

### DO:
- ✅ Run validation before major operations (imports, migrations)
- ✅ Generate reports with timestamps and detailed error messages
- ✅ Prioritize issues by severity (high/medium/low)
- ✅ Back up master lists before making bulk changes
- ✅ Use automated ID assignment (don't manually guess next ID)
- ✅ Log all validation runs for audit trail
- ✅ Fix high-severity issues immediately
- ✅ Schedule regular health checks (weekly/monthly)
- ✅ Document cleanup operations in migration reports

### DON'T:
- ❌ Skip validation steps to save time
- ❌ Manually edit master lists without validation
- ❌ Ignore warnings (they become errors later)
- ❌ Delete entities without checking references
- ❌ Create duplicate IDs
- ❌ Use invalid status values or department codes
- ❌ Modify files without backup
- ❌ Assume entity exists without verification

---

## Integration with Other Sub-Prompts

**PMT-076 (Import Validation Pipeline)**:
- Use PMT-075 for pre-import validation
- Validate new entities before staging
- Run duplicate detection before integration

**PMT-079 (Prompt Taxonomy Sync)**:
- Use PMT-075 to validate prompt references
- Check if referenced entity IDs exist
- Verify file paths are correct

**PMT-080 (Token Optimization Analyzer)**:
- Use PMT-075 to identify redundant data
- Find duplicate descriptions for compression
- Validate optimized data structure

---

## Error Codes & Messages

| Code | Severity | Message | Action |
|------|----------|---------|--------|
| VAL-001 | High | Missing required field | Add missing field |
| VAL-002 | High | Invalid ID format | Fix ID format (e.g., TSK-### not TSK-#) |
| VAL-003 | High | Broken cross-reference | Fix reference or create missing entity |
| VAL-004 | Medium | Invalid status value | Use valid status enum |
| VAL-005 | Medium | Invalid department code | Use valid department enum |
| VAL-006 | Medium | Name contains spaces | Replace spaces with underscores |
| VAL-007 | Low | Missing Last_Updated | Add update timestamp |
| VAL-008 | Low | Orphaned entity (no children) | Review if intentional |
| VAL-009 | Medium | Duplicate detected (≥0.6 similarity) | Review and merge if needed |
| VAL-010 | High | ID collision (duplicate ID) | Assign new unique ID |

---

## Version History

**v1.0** (2025-11-21)
- Initial version
- Schema validation for all master lists
- Cross-reference validation (PRT→MLT→TSK→STT→Item)
- Duplicate detection (similarity threshold: 0.6)
- Automated ID assignment for all entity types
- Consistency verification (naming, status, departments)
- Cleanup operations (backups, broken refs, deprecated entities)
- 4 validation workflows
- Error code system

---

## Related Documents

- [PMT-074_Data_Architect_Master.md](PMT-074_Data_Architect_Master.md) - Parent prompt
- [Entity_Schema_Registry.json](../../DATA_FIELDS/Entity_Schema_Registry.json) - Schema definitions
- [TASK_MANAGERS/README.md](../../TASK_MANAGERS/README.md) - Task hierarchy documentation
- [LIBRARIES/README.md](../../LIBRARIES/README.md) - Libraries structure
- [ARCHITECTURE_UPDATE_PLAN.md](../../ARCHITECTURE_UPDATE_PLAN.md) - System architecture

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Review Cycle:** Monthly
**Next Review:** 2025-12-21

---

**End of Prompt**
