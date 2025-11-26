# TASK_MANAGERS Import Guide Master v1.0

**Document Type:** Import Guide Master
**Version:** 1.0
**Department:** System Architecture
**Date:** 2025-11-21
**Status:** Active
**Integration:** PMT-074, PMT-075, PMT-076

---

## Purpose

Comprehensive guide for importing new entities into the TASK_MANAGERS ecosystem using the Data Architect prompt system (PMT-074 through PMT-080). This master guide covers the complete import workflow from initial data preparation through validation and integration.

**What This Guide Covers:**
- Complete 4-stage import pipeline (Staging → Validation → Transformation → Integration)
- Import guides for all TSM entities (Projects, Milestones, Tasks, Steps, Checklists, Workflows)
- Data validation and error handling
- Relationship mapping and hierarchy enforcement
- Token-efficient data formatting
- Rollback and recovery procedures

---

## TASK_MANAGERS Ecosystem Overview

### Entity Structure

```
TASK_MANAGERS/
├── TSM-001_Project_Templates/          # PRT-### (Projects)
│   ├── Project_Templates_Master_List.csv
│   └── Project-Template-###_[Name].json
├── TSM-002_Milestone_Templates/        # MLT-### (Milestones)
│   ├── Milestone_Templates_Master_List.csv
│   └── Milestone-Template-###_[Name].json
├── TSM-003_Task_Templates/             # TSK-### (Tasks) [DEPRECATED: Use TST-###]
│   ├── Task_Templates_Master_List.csv
│   └── Task-Template-###_[Name].json
├── TSM-004_Step_Templates/             # STT-### (Steps)
│   ├── Step_Templates_Master_List.csv
│   └── Step-Template-###_[Name].json
├── TSM-005_Checklist_Items/            # CHT-### templates, CHK-### items
│   ├── Checklist_Items_Master_List.csv
│   └── CHT-###_Item_###_to_Item_###.json
├── TSM-006_Daily_Workflows/            # DWK-### (Daily Workflows)
│   ├── Daily_Workflows_Master_List.csv
│   └── Daily-Workflow-###_[Name].json
└── TSM-007_Weekly_Workflows/           # WWK-### (Weekly Workflows)
    ├── Weekly_Workflows_Master_List.csv
    └── Weekly-Workflow-###_[Name].json
```

### Hierarchy Relationships

```
Project (PRT-###)
    └── contains → Milestone (MLT-###)
            └── contains → Task (TSK-### or TST-###)
                    └── contains → Step (STT-###)
                            └── references → ChecklistTemplate (CHT-###)
                                    └── contains → ChecklistItem (CHK-###)
```

**Critical Rules:**
1. **Child → Parent References**: Tasks MUST reference valid Milestone IDs, Milestones MUST reference valid Project IDs
2. **ID Uniqueness**: All IDs must be unique across the entity type
3. **Status Values**: Active, Deprecated, Draft, Archived
4. **Department Codes**: Must match approved department list (AID, DEV, HRM, LGN, VID, DGN, etc.)

---

## Import Pipeline Overview

### 4-Stage Workflow (PMT-076)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Stage 1: STAGING                                                    │
│ Copy files → Preserve originals → Initial structure check          │
│ Location: IMPORTS/Staging/[date]/TASK_MANAGERS/                    │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Stage 2: VALIDATION (PMT-075)                                       │
│ Schema check → Cross-ref validation → Duplicate detection          │
│ Location: IMPORTS/Validation/[date]/TASK_MANAGERS/                 │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Stage 3: TRANSFORMATION                                             │
│ Normalize IDs → Format fields → Enrich metadata → Token optimize   │
│ Location: IMPORTS/Transformation/[date]/TASK_MANAGERS/             │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Stage 4: INTEGRATION                                                │
│ Merge to master → Update cross-refs → Generate reports             │
│ Location: ENTITIES/TASK_MANAGERS/                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start Import

### Example: Import New Task Template

```python
# Step 1: Prepare import data
new_task = {
    "New_ID": "TST-999",
    "Entity_Type": "Task_Template",
    "Current_ID": "Task-Template-999",
    "Name": "Configure_Email_Automation",
    "Description": "Setup automated email workflows using n8n and Gmail API",
    "Department": "AID",
    "milestone_template_id": "MLT-010",  # Must exist!
    "File_Path": "ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task-Template-999_Configure_Email_Automation.json",
    "Status": "Active"
}

# Step 2: Stage the import
python import_manager.py stage --entity-type Task --data new_task.json

# Step 3: Validate
python import_manager.py validate --entity-type Task --import-id 20251121_001

# Step 4: Review validation report
# Check: IMPORTS/Validation/20251121_001/validation_report.json

# Step 5: Transform (if validation passed)
python import_manager.py transform --import-id 20251121_001

# Step 6: Integrate (final commit)
python import_manager.py integrate --import-id 20251121_001 --commit
```

---

## Entity-Specific Import Guides

### TSM-001: Project Templates
**Guide:** [TSM-001_Project_Templates_Import_Guide.md](TSM-001_Project_Templates_Import_Guide.md)
- Import new project templates
- Define project metadata, departments, milestones
- Validate project structure and deliverables
- Current Count: 8 projects (PRT-001 to PRT-008)

### TSM-002: Milestone Templates
**Guide:** [TSM-002_Milestone_Templates_Import_Guide.md](TSM-002_Milestone_Templates_Import_Guide.md)
- Import milestones linked to projects
- Define milestone objectives and task lists
- Validate parent-child relationships
- Current Count: 9+ milestones (MLT-001 to MLT-009+)

### TSM-003: Task Templates
**Guide:** [TSM-003_Task_Templates_Import_Guide.md](TSM-003_Task_Templates_Import_Guide.md)
- Import task templates with tool references
- Link tasks to milestones and projects
- Define steps, checklists, and dependencies
- Current Count: 71+ tasks (TST-001 to TST-071+)
- **Note**: New ID pattern is TST-### (not TSK-###)

### TSM-004: Step Templates
**Guide:** [TSM-004_Step_Templates_Import_Guide.md](TSM-004_Step_Templates_Import_Guide.md)
- Import granular step instructions
- Link steps to parent tasks
- Define inputs, outputs, and validation criteria
- ID Pattern: STT-###

### TSM-005: Checklist Items
**Guide:** [TSM-005_Checklist_Items_Import_Guide.md](TSM-005_Checklist_Items_Import_Guide.md)
- Import checklist templates (CHT-###) and items (CHK-###)
- Types: deliverable, validation, process, documentation
- Link to tasks, milestones, projects
- Current Count: 49+ templates (CHT-001 to CHT-049+)

### TSM-006 & TSM-007: Workflow Templates
**Guide:** [TSM-006_007_Workflow_Templates_Import_Guide.md](TSM-006_007_Workflow_Templates_Import_Guide.md)
- Import daily and weekly workflow templates
- Define recurring task sequences
- ID Patterns: DWK-### (daily), WWK-### (weekly)

---

## Common Import Patterns

### Pattern 1: Bottom-Up Import (Recommended for New Hierarchies)

```
1. Import Steps (STT-###) first
2. Import Tasks (TST-###) referencing steps
3. Import Milestones (MLT-###) referencing tasks
4. Import Projects (PRT-###) referencing milestones
5. Import Checklists (CHT-###, CHK-###) referencing tasks
```

**Why Bottom-Up?**
- Ensures all child dependencies exist before parent creation
- Reduces validation errors
- Enables incremental testing

### Pattern 2: Top-Down Import (For Existing Hierarchy Extension)

```
1. Identify existing Project (PRT-###)
2. Import new Milestone (MLT-###) under existing project
3. Import Tasks (TST-###) under new milestone
4. Import Steps (STT-###) under new tasks
5. Import Checklists if needed
```

**When to Use:**
- Extending existing projects
- Adding milestones to active projects
- Incremental feature additions

### Pattern 3: Bulk Import (For Complete System Migrations)

```
1. Stage all entities in IMPORTS/Staging/[date]/
2. Run bulk validation (PMT-075)
3. Review consolidated error report
4. Fix validation errors in staging
5. Re-validate until clean
6. Bulk transform → Bulk integrate
```

**Use Cases:**
- Migration from external task managers (Asana, Jira, Monday.com)
- Initial system population
- Disaster recovery restores

---

## Data Validation Rules

### Schema Validation (PMT-075 Operation 1)

**Required Fields by Entity:**

**Projects (PRT-###):**
- `New_ID` (pattern: `PRT-\d{3}`)
- `Entity_Type` = "Project_Template"
- `Name` (string, 3-100 chars)
- `Description` (string, 10-500 chars)
- `Department` (valid department code)
- `Status` (Active|Deprecated|Draft|Archived)

**Milestones (MLT-###):**
- All project fields PLUS
- `project_template_id` (must exist in Projects)

**Tasks (TST-###):**
- All milestone fields PLUS
- `milestone_template_id` (must exist in Milestones)
- `tools_referenced` (array of TOL-### IDs, optional)

**Steps (STT-###):**
- `New_ID` (pattern: `STT-\d{3}`)
- `task_template_id` (must exist in Tasks)
- `Name`, `Description`, `Order` (numeric)

**Checklists (CHT-###, CHK-###):**
- CHT: Template metadata in CSV
- CHK: Individual items in JSON with `associated_task` references

### Cross-Reference Validation (PMT-075 Operation 2)

```python
# Validation checks performed:
1. milestone_template_id exists in Milestones CSV
2. project_template_id exists in Projects CSV
3. tools_referenced[] exist in Tools Master List
4. Department code exists in approved departments
5. Status value is valid enum
6. No circular dependencies (A→B→A)
```

### Duplicate Detection (PMT-075 Operation 3)

```python
# Similarity checks:
- Name similarity ≥ 0.85 → Warning (potential duplicate)
- Description similarity ≥ 0.90 → Warning
- Exact ID match → Error (blocking)
- Exact (Name + Department) match → Error
```

---

## Error Handling

### Validation Error Codes

**VAL-001**: Missing Required Field
- **Action**: Add missing field to staged data
- **Example**: `New_ID` missing from Task import

**VAL-002**: Invalid ID Format
- **Action**: Correct ID pattern (e.g., TST-### not TSK-###)
- **Example**: `TSK-999` → should be `TST-999`

**VAL-003**: Broken Cross-Reference
- **Action**: Ensure referenced entity exists first
- **Example**: Task references `MLT-999` but milestone doesn't exist

**VAL-004**: Duplicate Entity Detected
- **Action**: Review existing entity, merge or differentiate
- **Example**: Task name 90% similar to existing TST-042

**VAL-005**: Invalid Status Value
- **Action**: Use Active, Deprecated, Draft, or Archived
- **Example**: Status = "InProgress" → should be "Active"

**VAL-006**: Invalid Department Code
- **Action**: Use approved department (AID, DEV, HRM, LGN, VID, DGN, etc.)
- **Example**: Department = "AI" → should be "AID"

**VAL-007**: Circular Dependency Detected
- **Action**: Break dependency loop
- **Example**: Task A → Task B → Task A

**VAL-008**: File Path Mismatch
- **Action**: Ensure File_Path matches actual file location
- **Example**: Path references TSM-002 but file in TSM-003

**VAL-009**: Missing JSON Detail File
- **Action**: Create corresponding JSON file for CSV entry
- **Example**: TST-999 in CSV but no Task-Template-999_[Name].json

**VAL-010**: Schema Version Mismatch
- **Action**: Update data format to current schema version
- **Example**: Old format uses "task_id" instead of "New_ID"

---

## Token Optimization (PMT-080)

### Token-Efficient Import Format

**Instead of verbose JSON:**
```json
{
  "id": "TST-999",
  "entity_type": "Task_Template",
  "name": "Configure Email Automation Workflow",
  "description": "This task involves setting up an automated email workflow using n8n automation platform and Gmail API integration",
  "department": "AI Department",
  "tools": ["n8n", "Gmail API", "Claude AI"]
}
```

**Use compact format (60% token reduction):**
```json
{
  "id": "TST-999",
  "type": "Task",
  "name": "Configure_Email_Automation",
  "desc": "Setup automated email workflows using n8n and Gmail API",
  "dept": "AID",
  "tools": ["TOL-015", "TOL-092", "TOL-001"]
}
```

**Token Savings:**
- Abbreviated keys: `desc` vs `description` (50% reduction)
- Entity references: `TOL-015` vs "n8n Automation Platform" (70% reduction)
- Underscore naming: `Configure_Email_Automation` vs long descriptions (40% reduction)

---

## Rollback Procedures

### Rollback After Validation Failure

```bash
# Validation failed - no changes to production
# Simply fix staged data and re-validate
cd IMPORTS/Staging/20251121_001/
# Edit files
python import_manager.py validate --import-id 20251121_001 --retry
```

### Rollback After Integration

```bash
# Undo integration (within 24 hours)
python import_manager.py rollback --import-id 20251121_001

# Steps performed:
# 1. Restore master CSVs from backup
# 2. Remove integrated JSON files
# 3. Archive failed import in IMPORTS/Failed/
# 4. Generate rollback report
```

**Rollback Limitations:**
- Only available within 24 hours of integration
- Cannot rollback if downstream entities already created
- Requires backup files to exist

---

## Integration with Data Architect Prompts

### PMT-074: Data Architect Master
**Use:** Overall orchestration and routing
```bash
# Route import request to appropriate sub-prompt
python run_prompt.py PMT-074 --task "Import new task template" --entity TST-999
```

### PMT-075: Data Integrity Manager
**Use:** Validation operations
```bash
# Run full validation suite
python run_prompt.py PMT-075 --operation validate --import-id 20251121_001
```

### PMT-076: Import Validation Pipeline
**Use:** 4-stage import workflow
```bash
# Execute complete import pipeline
python run_prompt.py PMT-076 --source external_tasks.csv --auto-stage
```

### PMT-078: Cross Entity Search
**Use:** Find existing entities before import
```bash
# Search for similar tasks before creating new one
python run_prompt.py PMT-078 --query "email automation" --entity-type Task
```

### PMT-079: Prompt Taxonomy Sync
**Use:** Update prompts referencing imported entities
```bash
# After import, sync prompts with new entity IDs
python run_prompt.py PMT-079 --sync-entity TST-999
```

---

## Best Practices

### DO:
- ✅ **Search First**: Use PMT-078 to check if entity already exists
- ✅ **Bottom-Up**: Import child entities before parents when building new hierarchies
- ✅ **Validate Early**: Run validation after staging, before transformation
- ✅ **Use Compact IDs**: Reference entities by ID (TOL-015) not names ("n8n")
- ✅ **Batch Similar**: Import related entities together (all tasks for one milestone)
- ✅ **Document Sources**: Note where import data originated (Asana, Jira, manual)
- ✅ **Backup First**: Always create backups before bulk operations

### DON'T:
- ❌ **Skip Validation**: Never integrate without clean validation report
- ❌ **Duplicate IDs**: Check ID availability before assignment
- ❌ **Break Hierarchies**: Don't orphan entities (task without milestone)
- ❌ **Use Old Patterns**: Avoid deprecated ID patterns (TSK-### → use TST-###)
- ❌ **Manual Edits**: Don't edit production CSVs directly during import
- ❌ **Ignore Warnings**: Review similarity warnings even if validation passes
- ❌ **Rush Integration**: Take time to review transformation results

---

## Import Workflows by Use Case

### Use Case 1: Import From External Task Manager (Asana, Jira)

```bash
# Step 1: Export from external system
# Get CSV or JSON export from Asana/Jira

# Step 2: Transform to ENTITIES format
python transform/asana_to_entities.py --input asana_export.csv --output staging/

# Step 3: Stage import
python import_manager.py stage --source staging/ --entity-type Task

# Step 4: Validate
python import_manager.py validate --import-id 20251121_001

# Step 5: Review report and fix errors
vi IMPORTS/Validation/20251121_001/validation_report.json

# Step 6: Transform
python import_manager.py transform --import-id 20251121_001

# Step 7: Integrate
python import_manager.py integrate --import-id 20251121_001 --commit
```

### Use Case 2: Create New Project Hierarchy from Scratch

```bash
# Step 1: Define project structure
project:
  PRT-009: "Customer Onboarding Automation"
  milestones:
    MLT-050: "Onboarding Workflow Design"
    MLT-051: "Email Sequence Setup"
    MLT-052: "CRM Integration"
  tasks (under MLT-050):
    TST-500: "Map Customer Journey"
    TST-501: "Design Welcome Email"
    TST-502: "Create Onboarding Checklist"

# Step 2: Import bottom-up
python import_manager.py stage --entity-type Step --data steps.json
python import_manager.py stage --entity-type Task --data tasks.json
python import_manager.py stage --entity-type Milestone --data milestones.json
python import_manager.py stage --entity-type Project --data project.json

# Step 3: Validate all
python import_manager.py validate --import-id 20251121_002 --all

# Step 4: Integrate all
python import_manager.py integrate --import-id 20251121_002 --commit
```

### Use Case 3: Extend Existing Project with New Milestone

```bash
# Step 1: Find existing project
python run_prompt.py PMT-078 --query "HR Automation" --entity-type Project
# Found: PRT-003

# Step 2: Create new milestone data
new_milestone = {
  "New_ID": "MLT-053",
  "Name": "Performance Review Automation",
  "project_template_id": "PRT-003",
  "Department": "HRM",
  "Status": "Active"
}

# Step 3: Stage and validate
python import_manager.py stage --entity-type Milestone --data new_milestone.json
python import_manager.py validate --import-id 20251121_003

# Step 4: Integrate
python import_manager.py integrate --import-id 20251121_003 --commit

# Step 5: Sync prompts that reference PRT-003
python run_prompt.py PMT-079 --sync-entity PRT-003
```

---

## Monitoring and Reports

### Import Success Metrics

```markdown
## Import Session Report: 20251121_001

**Date**: 2025-11-21 14:30:00
**Import Type**: Task Templates (Bulk)
**Source**: Asana Migration

### Summary:
- ✅ Staged: 15 tasks
- ✅ Validated: 15 tasks (100% pass)
- ✅ Transformed: 15 tasks
- ✅ Integrated: 15 tasks
- ⏱️  Total Time: 8 minutes 32 seconds

### Entity Breakdown:
- Tasks: 15 (TST-500 to TST-514)
- New Milestones: 0
- New Projects: 0

### Validation Results:
- Schema Errors: 0
- Cross-Reference Errors: 0
- Duplicate Warnings: 2 (reviewed, approved)
- Token Optimization: 62% reduction achieved

### Integration Results:
- Master CSV Updated: Task_Templates_Master_List.csv (+15 rows)
- JSON Files Created: 15
- Cross-References Updated: 3 milestones, 1 project
- Prompts Synced: 2 (PMT-002, PMT-070)

### Next Steps:
- ✅ Import complete
- ✅ Validation passed
- ⏭️  Consider creating checklists for new tasks
- ⏭️  Update project documentation
```

---

## Appendix A: Entity Field Schemas

### Complete Field Definitions

See [Entity_Schema_Registry.json](C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DATA_FIELDS\Entity_Schema_Registry.json) for:
- All required and optional fields
- Field patterns and validation rules
- Enum values for Status, Department, etc.
- Cross-reference field mappings

---

## Appendix B: Common Validation Errors and Fixes

| Error Code | Description | Common Fix |
|------------|-------------|------------|
| VAL-001 | Missing `New_ID` | Add unique ID following pattern |
| VAL-002 | Invalid ID format | Use TST-### (not TSK-###) |
| VAL-003 | Milestone not found | Import milestone first |
| VAL-004 | Duplicate name | Differentiate or merge |
| VAL-005 | Invalid status | Use Active/Deprecated/Draft/Archived |
| VAL-006 | Invalid department | Use AID/DEV/HRM/LGN/VID/DGN |
| VAL-007 | Circular dependency | Break reference loop |
| VAL-008 | Path mismatch | Correct File_Path field |
| VAL-009 | Missing JSON | Create detail JSON file |
| VAL-010 | Schema mismatch | Update to current format |

---

## Appendix C: Import Command Reference

```bash
# Stage import
python import_manager.py stage --entity-type [Project|Milestone|Task|Step|Checklist] --data [file]

# Validate staged import
python import_manager.py validate --import-id [ID] [--retry]

# Transform validated data
python import_manager.py transform --import-id [ID]

# Integrate to production
python import_manager.py integrate --import-id [ID] --commit

# Rollback integration
python import_manager.py rollback --import-id [ID]

# Batch operations
python import_manager.py batch --operation [stage|validate|transform|integrate] --import-ids [ID1,ID2,ID3]

# Status check
python import_manager.py status --import-id [ID]
```

---

## Version History

**v1.0** (2025-11-21)
- Initial master guide
- 4-stage import pipeline documented
- Entity-specific guide structure
- Integration with PMT-074 through PMT-080
- Common patterns and use cases
- Error handling and rollback procedures

---

**Status:** Active
**Maintenance:** Update when new TSM entities added or import procedures change

---

**Related Guides:**
- [TSM-001_Project_Templates_Import_Guide.md](TSM-001_Project_Templates_Import_Guide.md)
- [TSM-002_Milestone_Templates_Import_Guide.md](TSM-002_Milestone_Templates_Import_Guide.md)
- [TSM-003_Task_Templates_Import_Guide.md](TSM-003_Task_Templates_Import_Guide.md)
- [TSM-004_Step_Templates_Import_Guide.md](TSM-004_Step_Templates_Import_Guide.md)
- [TSM-005_Checklist_Items_Import_Guide.md](TSM-005_Checklist_Items_Import_Guide.md)

---

**End of Document**
