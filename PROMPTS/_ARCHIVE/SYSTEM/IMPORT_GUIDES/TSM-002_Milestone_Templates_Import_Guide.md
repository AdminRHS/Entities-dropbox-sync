# TSM-002: Milestone Templates Import Guide v1.0

**Entity Type:** Milestone_Template
**ID Pattern:** MLT-###
**Parent Guide:** [TASK_MANAGERS_Import_Guide_Master.md](TASK_MANAGERS_Import_Guide_Master.md)
**Version:** 1.0
**Date:** 2025-11-21
**Status:** Active

---

## Purpose

Detailed guide for importing new Milestone Templates into TSM-002_Milestone_Templates. Milestones are the second level in the task management hierarchy - they represent phases or major deliverables within projects and contain tasks.

**What You'll Learn:**
- How to structure milestone template data
- Required and optional fields for milestones
- How to link milestones to projects and tasks
- Validation rules for milestone templates
- Parallel vs sequential milestone execution
- Common import errors and solutions

---

## Milestone Template Overview

### What is a Milestone Template?

A **Milestone Template** is a reusable phase or deliverable within a project. It defines:
- Milestone objectives and deliverables
- Associated tasks (references to task templates)
- Estimated effort and timeline
- Dependencies on other milestones
- Whether tasks can run in parallel
- Expected reports and outputs

### Current Milestones

**Active Milestones (9+):**
- MLT-001: Content Analysis (AID)
- MLT-002: Data Inventory (AID)
- MLT-003: Relationship Validation (AID)
- MLT-004: Schema Naming Validation (AID)
- MLT-005: Synthesis Recommendations (AID)
- MLT-006: VIDEO-001 Research Complete (VID)
- MLT-007: VIDEO-002 Processing Complete (VID)
- MLT-008: VIDEO-003 Library Population Complete (VID)
- MLT-009: Behance Project Publishing Workflow (DGN)
- ...and more

**Next Available ID:** MLT-050+ (check current max)

---

## File Structure

```
TSM-002_Milestone_Templates/
├── Milestone_Templates_Master_List.csv        # Master catalog (CSV)
├── MLT-###_[ShortName].json                   # Milestone detail files (JSON)
├── Milestone_Templates_Listing.md             # Human-readable listing
├── Milestone_Templates_Hierarchy_Tree.md      # Visual hierarchy
├── Milestone_Templates_Department_Distribution.md
├── Milestone_Templates_ISO_Code_Registry.md
├── Milestone_Templates_Migration_Map.json     # ID migrations
├── Milestone_Template_Schema.md               # Schema documentation
└── README.md                                  # Folder documentation
```

**Key Files:**
- **CSV Master List**: Primary source of truth for all milestones
- **JSON Detail Files**: Rich milestone metadata, task references, dependencies
- **Schema Documentation**: Field definitions and validation rules

---

## Required Fields

### Master CSV Fields

| Field | Type | Required | Pattern/Enum | Description |
|-------|------|----------|--------------|-------------|
| `New_ID` | string | ✅ Yes | `MLT-\d{3}` | Unique milestone ID (MLT-001 to MLT-999) |
| `Entity_Type` | string | ✅ Yes | "Milestone_Template" | Fixed value |
| `Current_ID` | string | ✅ Yes | `Milestone-Template-###` | Internal reference ID |
| `Name` | string | ✅ Yes | 3-100 chars | Milestone template name |
| `Description` | string | ✅ Yes | 10-500 chars | Detailed milestone description |
| `Department` | string | ✅ Yes | AID\|DEV\|HRM\|LGN\|VID\|DGN\|FIN\|SAL | Department code |
| `File_Path` | string | ✅ Yes | Path pattern | Path to JSON detail file |
| `Status` | string | ✅ Yes | Active\|Deprecated\|Draft\|Archived | Milestone status |

### JSON Detail File Fields

```json
{
  "milestone_template_id": "Milestone-Template-###",  // Legacy ID (required)
  "name": "string",                                   // Milestone name (required)
  "category": "string",                               // Category (required)
  "department": "string",                             // Department (required)
  "description": "string",                            // Description (required)
  "estimated_hours": number,                          // Effort estimate (required)
  "phase": number,                                    // Execution phase/order (required)
  "can_run_parallel": boolean,                        // Parallel execution flag (required)
  "dependencies": ["MLT-###"],                        // Milestone dependencies (optional)
  "project_template_id": "PRT-###",                  // Parent project (REQUIRED for hierarchy)
  "task_templates": [                                 // Task references (required)
    {
      "task_template_id": "TASK-TEMPLATE-###",
      "task_template_name": "string"
    }
  ],
  "expected_reports": [                               // Expected outputs (optional)
    {
      "report_id": "REP-###",
      "report_name": "string"
    }
  ],
  "version": "1.0"                                    // Version (required)
}
```

**IMPORTANT:** The `project_template_id` field is **REQUIRED** for establishing parent-child relationships. Without it, the milestone is orphaned.

---

## Validation Rules

### Schema Validation (PMT-075 Operation 1)

**CSV Validation:**
```python
# Required field checks
assert pd.notna(row['New_ID']), "VAL-001: New_ID required"
assert re.match(r'^MLT-\d{3}$', row['New_ID']), "VAL-002: Invalid ID format"
assert row['Entity_Type'] == "Milestone_Template", "VAL-002: Wrong entity type"
assert len(row['Name']) >= 3, "VAL-001: Name too short"
assert len(row['Description']) >= 10, "VAL-001: Description too short"
assert row['Department'] in VALID_DEPARTMENTS, "VAL-006: Invalid department"
assert row['Status'] in ['Active', 'Deprecated', 'Draft', 'Archived'], "VAL-005: Invalid status"
```

**JSON Validation:**
```python
# JSON structure checks
assert 'milestone_template_id' in data, "VAL-001: Missing milestone_template_id"
assert 'name' in data, "VAL-001: Missing name"
assert 'project_template_id' in data, "VAL-001: Missing project_template_id (orphaned milestone)"
assert 'task_templates' in data, "VAL-001: Missing task_templates"
assert len(data['task_templates']) > 0, "VAL-003: No tasks defined"
assert 'estimated_hours' in data, "VAL-001: Missing estimated_hours"
assert 'phase' in data, "VAL-001: Missing phase"
assert 'can_run_parallel' in data, "VAL-001: Missing can_run_parallel"
assert data['version'] == "1.0", "VAL-010: Invalid version format"
```

### Cross-Reference Validation (PMT-075 Operation 2)

**Project Reference Validation:**
```python
# Check parent project exists
projects_csv = load_csv("Project_Templates_Master_List.csv")
project_id = milestone_json['project_template_id']
assert project_id in projects_csv['New_ID'].values, f"VAL-003: Project {project_id} not found"
```

**Task Reference Validation:**
```python
# Check all task references exist
tasks_csv = load_csv("Task_Templates_Master_List.csv")
for task in milestone_json['task_templates']:
    task_id = task['task_template_id']
    # Note: task_template_id may use legacy format (TASK-TEMPLATE-###)
    # Modern format is TST-###
    # Validation should handle both formats
    assert task_exists(task_id), f"VAL-003: Task {task_id} not found"
```

**Dependency Validation:**
```python
# Check dependency milestones exist
milestones_csv = load_csv("Milestone_Templates_Master_List.csv")
for dep_id in milestone_json.get('dependencies', []):
    assert dep_id in milestones_csv['New_ID'].values, f"VAL-003: Dependency {dep_id} not found"

# Check for circular dependencies
assert not has_circular_dependency(milestone_id, dependencies), "VAL-007: Circular dependency detected"
```

### Duplicate Detection (PMT-075 Operation 3)

**Check for Similar Milestones:**
```python
from difflib import SequenceMatcher

existing_milestones = load_csv("Milestone_Templates_Master_List.csv")
for existing in existing_milestones.itertuples():
    name_similarity = SequenceMatcher(None, new_milestone['Name'], existing.Name).ratio()
    if name_similarity >= 0.85:
        print(f"WARNING VAL-004: Similar milestone found: {existing.New_ID} - {existing.Name}")
        print(f"Similarity: {name_similarity:.2%}")
```

---

## Import Workflow

### Step-by-Step Import Process

#### Step 1: Prepare Milestone Data

**Create CSV Entry:**
```csv
New_ID,Entity_Type,Current_ID,Name,Description,Department,File_Path,Status
MLT-050,Milestone_Template,Milestone-Template-050,Onboarding Workflow Design,Design complete customer onboarding workflow including touchpoints and success metrics,SAL,ENTITIES/TASK_MANAGERS/TSM-002_Milestone_Templates/MLT-050_Onboarding_Workflow_Design.json,Active
```

**Create JSON Detail File:**
```json
{
  "milestone_template_id": "Milestone-Template-050",
  "name": "Onboarding Workflow Design",
  "category": "Design",
  "department": "Sales",
  "description": "Design complete customer onboarding workflow including touchpoints, automation triggers, and success metrics",
  "estimated_hours": 8,
  "phase": 1,
  "can_run_parallel": false,
  "dependencies": [],
  "project_template_id": "PRT-009",

  "task_templates": [
    {
      "task_template_id": "TST-500",
      "task_template_name": "Map Customer Journey"
    },
    {
      "task_template_id": "TST-501",
      "task_template_name": "Define Success Metrics"
    },
    {
      "task_template_id": "TST-502",
      "task_template_name": "Design Workflow Diagram"
    }
  ],

  "expected_reports": [
    {
      "report_id": "REP-050",
      "report_name": "Onboarding Workflow Diagram"
    },
    {
      "report_id": "REP-051",
      "report_name": "Customer Journey Map"
    }
  ],

  "version": "1.0"
}
```

#### Step 2: Stage Import

```bash
# Create staging directory
mkdir -p IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/

# Copy files to staging
cp milestone_data.csv IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/
cp MLT-050_Onboarding_Workflow_Design.json IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/

# Run staging operation
python import_manager.py stage \
  --entity-type Milestone \
  --import-id 20251121_001 \
  --source IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/
```

#### Step 3: Validate

```bash
# Run validation (PMT-075)
python import_manager.py validate \
  --entity-type Milestone \
  --import-id 20251121_001

# Review validation report
cat IMPORTS/Validation/20251121_001/validation_report.json
```

**Expected Validation Output:**
```json
{
  "import_id": "20251121_001",
  "entity_type": "Milestone",
  "timestamp": "2025-11-21T15:00:00",
  "validation_results": {
    "schema_validation": {
      "status": "PASS",
      "errors": []
    },
    "cross_reference_validation": {
      "status": "WARNING",
      "warnings": [
        "Task TST-500 not found (may need to import tasks first)",
        "Project PRT-009 found (parent exists - GOOD)"
      ]
    },
    "duplicate_detection": {
      "status": "PASS",
      "similar_entities": []
    },
    "dependency_validation": {
      "status": "PASS",
      "circular_dependencies": []
    }
  },
  "overall_status": "WARNING",
  "recommendation": "Import tasks before integrating milestone, or update task references"
}
```

#### Step 4: Handle Validation Results

**Scenario 1: Parent Project Missing (CRITICAL ERROR)**
```bash
# ERROR: VAL-003: Project PRT-009 not found
# MUST fix - milestone cannot be orphaned

# Option 1: Import project first
python import_manager.py stage --entity-type Project --data PRT-009.json
python import_manager.py integrate --import-id 20251121_project --commit

# Option 2: Update milestone to reference existing project
# Edit staged JSON: "project_template_id": "PRT-003" (existing)
vi IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/MLT-050_Onboarding_Workflow_Design.json

# Re-validate
python import_manager.py validate --import-id 20251121_001 --retry
```

**Scenario 2: Task References Missing (WARNING - Can Proceed)**
```bash
# WARNING: Tasks TST-500, TST-501, TST-502 not found
# Can integrate milestone first, then add tasks later (top-down approach)
# OR import tasks first (bottom-up approach - recommended)

# Bottom-up approach (recommended):
python import_manager.py stage --entity-type Task --data tasks_500_502.json
python import_manager.py integrate --import-id 20251121_tasks --commit
# Then integrate milestone
python import_manager.py integrate --import-id 20251121_001 --commit
```

#### Step 5: Transform

```bash
# Transform validated data
python import_manager.py transform \
  --import-id 20251121_001 \
  --entity-type Milestone

# Review transformed data
cat IMPORTS/Transformation/20251121_001/TASK_MANAGERS/TSM-002_Milestone_Templates/MLT-050_Onboarding_Workflow_Design.json
```

**Transformation Operations:**
- Normalize field formats (dates, IDs, numbers)
- Enrich with metadata (creation timestamp, import source)
- Validate project_template_id exists
- Calculate total estimated hours for project
- Optimize for token efficiency
- Generate checksums for integrity

#### Step 6: Integrate

```bash
# Final integration to production
python import_manager.py integrate \
  --import-id 20251121_001 \
  --entity-type Milestone \
  --commit

# Verify integration
python import_manager.py status --import-id 20251121_001
```

**Integration Operations:**
1. Backup existing `Milestone_Templates_Master_List.csv`
2. Append new row(s) to CSV
3. Copy JSON file(s) to `TSM-002_Milestone_Templates/`
4. Update parent project's milestone references
5. Update cross-reference maps
6. Sync related prompts (PMT-079)
7. Generate integration report

---

## Common Import Patterns

### Pattern 1: Import Milestone for Existing Project (Top-Down)

**Use Case:** Add new milestone to active project

```bash
# Step 1: Verify parent project exists
python run_prompt.py PMT-078 --query "PRT-009" --entity-type Project
# Found: PRT-009 "Customer Onboarding Automation"

# Step 2: Prepare milestone data with project_template_id = PRT-009
# Step 3: Stage → Validate → Transform → Integrate
python import_manager.py stage --entity-type Milestone --data milestone.json
python import_manager.py validate --import-id 20251121_001
# Validation may warn about missing tasks - acceptable for top-down
python import_manager.py transform --import-id 20251121_001
python import_manager.py integrate --import-id 20251121_001 --commit

# Step 4: Import tasks for this milestone
python import_manager.py stage --entity-type Task --data tasks.json
# Ensure tasks reference milestone_template_id = MLT-050
python import_manager.py integrate --import-id 20251121_002 --commit
```

### Pattern 2: Import Milestone with Tasks (Bottom-Up)

**Use Case:** Import complete milestone with all tasks ready

```bash
# Step 1: Import tasks first
python import_manager.py stage --entity-type Task --data tasks_500_502.json
python import_manager.py validate --import-id 20251121_tasks
python import_manager.py integrate --import-id 20251121_tasks --commit

# Step 2: Import milestone referencing new tasks
python import_manager.py stage --entity-type Milestone --data milestone.json
python import_manager.py validate --import-id 20251121_milestone
# Validation PASS - all tasks exist, project exists
python import_manager.py integrate --import-id 20251121_milestone --commit
```

### Pattern 3: Import Milestone with Dependencies

**Use Case:** Sequential milestones where one depends on another

```bash
# Scenario: MLT-052 depends on MLT-051 completion

# Step 1: Import independent milestone first
python import_manager.py stage --entity-type Milestone --data MLT-051.json
# MLT-051 has "dependencies": []
python import_manager.py integrate --import-id 20251121_051 --commit

# Step 2: Import dependent milestone
python import_manager.py stage --entity-type Milestone --data MLT-052.json
# MLT-052 has "dependencies": ["MLT-051"]
python import_manager.py validate --import-id 20251121_052
# Validation checks: MLT-051 exists ✓, No circular dependencies ✓
python import_manager.py integrate --import-id 20251121_052 --commit
```

### Pattern 4: Import Parallel Milestones

**Use Case:** Multiple milestones that can run simultaneously

```bash
# Milestones MLT-060, MLT-061, MLT-062 all have:
# "can_run_parallel": true
# "dependencies": []
# "project_template_id": "PRT-010"

# Can import all at once (batch)
python import_manager.py batch-stage \
  --entity-type Milestone \
  --data milestones_060_062.json

python import_manager.py batch-validate --import-id 20251121_batch
python import_manager.py batch-integrate --import-id 20251121_batch --commit
```

---

## Common Errors and Solutions

### Error 1: Missing project_template_id (Orphaned Milestone)

**Error Message:**
```
VAL-001: Missing required field 'project_template_id' in milestone JSON
This milestone would be orphaned - all milestones MUST belong to a project
```

**Solution:**
```json
// Add project_template_id to JSON
{
  "milestone_template_id": "Milestone-Template-050",
  "name": "Onboarding Workflow Design",
  "project_template_id": "PRT-009",  // <-- REQUIRED
  ...
}
```

### Error 2: Parent Project Not Found

**Error Message:**
```
VAL-003: Referenced project 'PRT-009' not found in Project_Templates_Master_List.csv
```

**Solution:**
```bash
# Option 1: Import project first (top-down from project)
python import_manager.py stage --entity-type Project --data PRT-009.json
python import_manager.py integrate --import-id 20251121_project --commit

# Option 2: Change to existing project
# Edit JSON: "project_template_id": "PRT-003" (existing)
```

### Error 3: Circular Dependency Detected

**Error Message:**
```
VAL-007: Circular dependency detected: MLT-050 → MLT-051 → MLT-052 → MLT-050
```

**Solution:**
```json
// Break the circular dependency
// MLT-050 dependencies: []
// MLT-051 dependencies: ["MLT-050"]
// MLT-052 dependencies: ["MLT-051"]  // Remove MLT-050 reference
```

### Error 4: Invalid Phase Number

**Error Message:**
```
VAL-002: Invalid phase value '0'. Phase must be positive integer (1, 2, 3, ...)
```

**Solution:**
```json
{
  "phase": 1,  // Start from 1, not 0
  ...
}
```

### Error 5: Missing can_run_parallel Flag

**Error Message:**
```
VAL-001: Missing required field 'can_run_parallel' in milestone JSON
```

**Solution:**
```json
{
  "can_run_parallel": false,  // or true - must be boolean
  ...
}
```

### Error 6: Task Reference Not Found

**Error Message:**
```
WARNING VAL-003: Referenced task 'TST-500' not found in Task_Templates_Master_List.csv
```

**Solution:**
```bash
# This is a WARNING, not blocking error
# Option 1: Import task first (bottom-up - recommended)
python import_manager.py stage --entity-type Task --data TST-500.json
python import_manager.py integrate --import-id 20251121_task --commit

# Option 2: Proceed anyway (top-down), import task later
# Milestone will integrate, task reference will be validated when task imports
```

### Error 7: Invalid ID Format

**Error Message:**
```
VAL-002: Invalid ID format 'MLS-050'. Expected pattern: MLT-\d{3}
```

**Solution:**
```bash
# Use correct ID pattern: MLT-### (not MLS-###, MIL-###, etc.)
New_ID: MLT-050  # Correct
New_ID: MLS-050  # Wrong
New_ID: MIL-050  # Wrong (this is legacy format used in JSON internally)
```

---

## Parallel vs Sequential Execution

### Understanding can_run_parallel

**Parallel Execution (can_run_parallel: true):**
```json
{
  "milestone_template_id": "Milestone-Template-060",
  "name": "Email Template Creation",
  "can_run_parallel": true,
  "dependencies": [],
  "phase": 2
}

{
  "milestone_template_id": "Milestone-Template-061",
  "name": "CRM Configuration",
  "can_run_parallel": true,
  "dependencies": [],
  "phase": 2
}
```
- Both milestones are **phase 2**
- Both have **no dependencies**
- Both marked **can_run_parallel: true**
- **Result:** Can be executed simultaneously

**Sequential Execution (can_run_parallel: false):**
```json
{
  "milestone_template_id": "Milestone-Template-050",
  "name": "Workflow Design",
  "can_run_parallel": false,
  "dependencies": [],
  "phase": 1
}

{
  "milestone_template_id": "Milestone-Template-051",
  "name": "Workflow Implementation",
  "can_run_parallel": false,
  "dependencies": ["MLT-050"],
  "phase": 2
}
```
- MLT-051 **depends on MLT-050**
- MLT-051 must wait for MLT-050 completion
- **Result:** Sequential execution

### Phase Ordering

**Phase** defines execution order within a project:
```
Phase 1: Research & Planning
  - MLT-050: Workflow Design (can_run_parallel: false)

Phase 2: Implementation (parallel tasks)
  - MLT-060: Email Templates (can_run_parallel: true)
  - MLT-061: CRM Config (can_run_parallel: true)
  - MLT-062: Automation Setup (can_run_parallel: true)

Phase 3: Testing & Launch
  - MLT-063: Integration Testing (can_run_parallel: false, dependencies: [MLT-060, MLT-061, MLT-062])
```

**Best Practice:**
- Use **phase** for logical grouping
- Use **dependencies** for hard requirements
- Use **can_run_parallel** to optimize execution time

---

## Token Optimization

### Compact Milestone References

**Instead of verbose format:**
```json
{
  "task_templates": [
    {
      "task_template_id": "TASK-TEMPLATE-001",
      "task_template_name": "Map Customer Journey with Detailed Touchpoints"
    }
  ]
}
```

**Use compact format (55% token reduction):**
```json
{
  "tasks": ["TST-500", "TST-501", "TST-502"]
}
```

**Trade-off:**
- Compact: ~15 tokens
- Verbose: ~35 tokens per task
- **Savings:** 55% reduction
- **Loss:** Human-readable names (require lookup)

---

## Integration with Data Architect Prompts

### Using PMT-074 (Data Architect Master)

```bash
# Route import request
python run_prompt.py PMT-074 \
  --task "Import milestone template" \
  --entity MLT-050 \
  --data milestone_data.json
```

### Using PMT-075 (Data Integrity Manager)

```bash
# Validate milestone and dependencies
python run_prompt.py PMT-075 \
  --operation validate \
  --entity-type Milestone \
  --check-dependencies \
  --data IMPORTS/Staging/20251121_001/milestone.json
```

### Using PMT-076 (Import Validation Pipeline)

```bash
# Run complete 4-stage import
python run_prompt.py PMT-076 \
  --source milestone_data.json \
  --entity-type Milestone \
  --validate-hierarchy \
  --auto-commit
```

### Using PMT-078 (Cross Entity Search)

```bash
# Find milestones in same project
python run_prompt.py PMT-078 \
  --query "PRT-009" \
  --entity-type Milestone \
  --traverse-children
```

---

## Best Practices

### DO:
- ✅ **Always Set project_template_id**: Never create orphaned milestones
- ✅ **Import Bottom-Up When Possible**: Tasks → Milestones → Projects
- ✅ **Define Dependencies**: Clearly specify milestone dependencies
- ✅ **Use Parallel Flag**: Mark independent milestones as parallel
- ✅ **Estimate Accurately**: Provide realistic estimated_hours
- ✅ **Check for Duplicates**: Search similar milestones before creating
- ✅ **Validate Parent Project**: Ensure project exists before milestone import
- ✅ **Document Reports**: List all expected_reports for deliverables

### DON'T:
- ❌ **Skip project_template_id**: Results in orphaned milestone (validation error)
- ❌ **Create Circular Dependencies**: A → B → C → A (validation error)
- ❌ **Use Wrong ID Pattern**: Use MLT-### (not MLS-###, MIL-###)
- ❌ **Forget can_run_parallel**: This field is required (validation error)
- ❌ **Set Phase to 0**: Phase starts at 1
- ❌ **Reference Non-Existent Tasks**: Import tasks first or expect warnings
- ❌ **Duplicate Milestones**: Check existing before creating similar ones

---

## Example: Complete Import Session

```bash
# === SCENARIO: Import 3 Milestones for PRT-009 "Customer Onboarding" ===

# Milestones to import:
# MLT-050: Workflow Design (phase 1, sequential)
# MLT-051: Email Sequence Setup (phase 2, parallel)
# MLT-052: CRM Integration (phase 2, parallel)

# Step 1: Verify parent project exists
python run_prompt.py PMT-078 --query "PRT-009" --entity-type Project
# Found: PRT-009 "Customer Onboarding Automation"

# Step 2: Check for similar milestones
python run_prompt.py PMT-078 \
  --query "workflow design email sequence CRM integration" \
  --entity-type Milestone \
  --similarity-threshold 0.8
# No similar milestones found

# Step 3: Prepare milestone data
cat > milestones_050_052.json <<EOF
[
  {
    "New_ID": "MLT-050",
    "Name": "Workflow Design",
    "project_template_id": "PRT-009",
    "phase": 1,
    "can_run_parallel": false,
    "dependencies": []
  },
  {
    "New_ID": "MLT-051",
    "Name": "Email Sequence Setup",
    "project_template_id": "PRT-009",
    "phase": 2,
    "can_run_parallel": true,
    "dependencies": ["MLT-050"]
  },
  {
    "New_ID": "MLT-052",
    "Name": "CRM Integration",
    "project_template_id": "PRT-009",
    "phase": 2,
    "can_run_parallel": true,
    "dependencies": ["MLT-050"]
  }
]
EOF

# Step 4: Batch stage all 3 milestones
python import_manager.py batch-stage \
  --entity-type Milestone \
  --data milestones_050_052.json

# Step 5: Batch validate
python import_manager.py batch-validate --import-id 20251121_batch
# Result: PASS (all projects exist, no circular deps, schemas valid)

# Step 6: Transform
python import_manager.py batch-transform --import-id 20251121_batch

# Step 7: Integrate
python import_manager.py batch-integrate --import-id 20251121_batch --commit

# Step 8: Verify integration
python run_prompt.py PMT-078 --query "PRT-009" --traverse-children
# Found: PRT-009 with 3 milestones (MLT-050, MLT-051, MLT-052)

# Step 9: Update project JSON to reference new milestones
python run_prompt.py PMT-079 --sync-entity PRT-009

# === IMPORT COMPLETE ===
```

---

## Related Guides

- **Master Guide:** [TASK_MANAGERS_Import_Guide_Master.md](TASK_MANAGERS_Import_Guide_Master.md)
- **Parent Entity:** [TSM-001_Project_Templates_Import_Guide.md](TSM-001_Project_Templates_Import_Guide.md)
- **Child Entities:** [TSM-003_Task_Templates_Import_Guide.md](TSM-003_Task_Templates_Import_Guide.md)

---

## Quick Reference

### File Naming
```
CSV Entry: MLT-###
JSON File: MLT-###_[ShortName].json
Example: MLT-050_Onboarding_Workflow_Design.json
```

### Required CSV Fields
```
New_ID, Entity_Type, Current_ID, Name, Description,
Department, File_Path, Status
```

### Required JSON Fields
```
milestone_template_id, name, category, department, description,
estimated_hours, phase, can_run_parallel, project_template_id,
task_templates (array), version
```

### Valid Departments
```
AID, DEV, HRM, LGN, VID, DGN, FIN, SAL, OPS, MKT
```

### Valid Statuses
```
Active, Deprecated, Draft, Archived
```

### Import Commands
```bash
# Stage
python import_manager.py stage --entity-type Milestone --data [file]

# Validate (checks parent project + dependencies)
python import_manager.py validate --import-id [ID] --check-dependencies

# Transform
python import_manager.py transform --import-id [ID]

# Integrate
python import_manager.py integrate --import-id [ID] --commit

# Rollback
python import_manager.py rollback --import-id [ID]
```

---

## Version History

**v1.0** (2025-11-21)
- Initial guide for TSM-002 Milestone Templates
- Complete field documentation including project_template_id
- Dependency and parallel execution guidance
- Validation rules and error handling
- Import patterns for top-down and bottom-up approaches
- Integration with PMT-074 through PMT-080

---

**Status:** Active

---

**End of Guide**
