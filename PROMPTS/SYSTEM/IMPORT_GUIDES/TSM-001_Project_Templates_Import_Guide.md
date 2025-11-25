# TSM-001: Project Templates Import Guide v1.0

**Entity Type:** Project_Template
**ID Pattern:** PRT-###
**Parent Guide:** [TASK_MANAGERS_Import_Guide_Master.md](TASK_MANAGERS_Import_Guide_Master.md)
**Version:** 1.0
**Date:** 2025-11-21
**Status:** Active

---

## Purpose

Detailed guide for importing new Project Templates into TSM-001_Project_Templates. Projects are the top-level entities in the task management hierarchy and contain milestones, which in turn contain tasks, steps, and checklists.

**What You'll Learn:**
- How to structure project template data
- Required and optional fields for projects
- Validation rules for project templates
- How to link milestones to projects
- Best practices for project organization
- Common import errors and solutions

---

## Project Template Overview

### What is a Project Template?

A **Project Template** is a reusable blueprint for a complete project workflow. It defines:
- Project scope, objectives, and deliverables
- Associated milestones (phases) with references to milestone templates
- Department ownership and categorization
- Expected reports and outputs
- Execution prompts and instructions
- Estimated duration and complexity

### Current Projects

**Active Projects (8):**
- PRT-001: AI Tutorial Research to Taxonomy Integration (AID)
- PRT-002: Complete MCP Automation Stack Setup (DEV)
- PRT-003: Complete HR Automation Implementation (HRM)
- PRT-004: Complete Lead Generation to Customer Conversion (LGN)
- PRT-005: Enterprise Account-Based Marketing Campaign (LGN)
- PRT-006: Research to Taxonomy Integration Pipeline (AID)
- PRT-007: System Analysis (AID)
- PRT-008: VIDEO Production (VID)

**Next Available ID:** PRT-009

---

## File Structure

```
TSM-001_Project_Templates/
├── Project_Templates_Master_List.csv          # Master catalog (CSV)
├── PRT-###_[ShortName].json                   # Project detail files (JSON)
├── Project_Templates_Listing.md               # Human-readable listing
├── Project_Templates_Hierarchy_Tree.md        # Visual hierarchy
├── Project_Templates_Department_Distribution.md
├── Project_Templates_ISO_Code_Registry.md
├── Project_Templates_Migration_Map.json       # ID migrations
└── README.md                                  # Folder documentation
```

**Key Files:**
- **CSV Master List**: Primary source of truth for all projects
- **JSON Detail Files**: Rich project metadata, milestone references, reports
- **Documentation Files**: Human-readable overviews and distributions

---

## Required Fields

### Master CSV Fields

| Field | Type | Required | Pattern/Enum | Description |
|-------|------|----------|--------------|-------------|
| `New_ID` | string | ✅ Yes | `PRT-\d{3}` | Unique project ID (PRT-001 to PRT-999) |
| `Entity_Type` | string | ✅ Yes | "Project_Template" | Fixed value |
| `Current_ID` | string | ✅ Yes | `Project-Template-###` | Internal reference ID |
| `Name` | string | ✅ Yes | 3-100 chars | Project template name |
| `Description` | string | ✅ Yes | 10-500 chars | Detailed project description |
| `Department` | string | ✅ Yes | AID\|DEV\|HRM\|LGN\|VID\|DGN\|FIN\|SAL | Department code |
| `Meta_Category` | string | ✅ Yes | TSM-001 | Fixed value |
| `File_Path` | string | ✅ Yes | Path pattern | Path to JSON detail file |
| `Status` | string | ✅ Yes | Active\|Deprecated\|Draft\|Archived | Project status |

### JSON Detail File Fields

```json
{
  "project_template_id": "PROJ-TEMPL-###",     // Legacy ID (required)
  "template_name": "string",                   // Project name (required)
  "template_version": "1.0",                   // Version (required)
  "department": "string",                      // Department (required)
  "category": "string",                        // Category (required)
  "created_date": "YYYY-MM-DD",               // Creation date (required)
  "description": "string",                     // Description (required)
  "when_to_use": ["string"],                   // Use cases (required)
  "estimated_duration": {                      // Duration estimates (optional)
    "total_hours": number,
    "total_days": number
  },
  "milestone_templates": [                     // Milestone references (required)
    {
      "milestone_template_id": "MIL-TEMPL-###",
      "milestone_template_name": "string",
      "reference": "path/to/milestone.json"
    }
  ],
  "expected_reports": [                        // Expected outputs (optional)
    {
      "report_id": "REP-###",
      "report_name": "string",
      "milestone": "MIL-TEMPL-###"
    }
  ],
  "execution_prompts": "path/to/prompts/",     // Prompt location (optional)
  "instantiation_instructions": ["string"],    // Setup instructions (optional)
  "version": "1.0",                            // Version (required)
  "last_updated": "YYYY-MM-DD"                 // Last update date (required)
}
```

---

## Validation Rules

### Schema Validation (PMT-075 Operation 1)

**CSV Validation:**
```python
# Required field checks
assert pd.notna(row['New_ID']), "VAL-001: New_ID required"
assert re.match(r'^PRT-\d{3}$', row['New_ID']), "VAL-002: Invalid ID format"
assert row['Entity_Type'] == "Project_Template", "VAL-002: Wrong entity type"
assert len(row['Name']) >= 3, "VAL-001: Name too short"
assert len(row['Description']) >= 10, "VAL-001: Description too short"
assert row['Department'] in VALID_DEPARTMENTS, "VAL-006: Invalid department"
assert row['Status'] in ['Active', 'Deprecated', 'Draft', 'Archived'], "VAL-005: Invalid status"
assert row['Meta_Category'] == "TSM-001", "VAL-002: Wrong meta category"
```

**JSON Validation:**
```python
# JSON structure checks
assert 'project_template_id' in data, "VAL-001: Missing project_template_id"
assert 'template_name' in data, "VAL-001: Missing template_name"
assert 'milestone_templates' in data, "VAL-001: Missing milestone_templates"
assert len(data['milestone_templates']) > 0, "VAL-003: No milestones defined"
assert data['version'] == "1.0", "VAL-010: Invalid version format"
```

### Cross-Reference Validation (PMT-075 Operation 2)

**Milestone Reference Validation:**
```python
# Check all milestone references exist
milestones_csv = load_csv("Milestone_Templates_Master_List.csv")
for milestone in project_json['milestone_templates']:
    milestone_id = milestone['milestone_template_id']
    # Note: milestone_template_id in JSON uses MIL-TEMPL-### format
    # But milestones CSV uses MLT-### format
    # Validation should check if referenced milestone exists in either format
    assert milestone_exists(milestone_id), f"VAL-003: Milestone {milestone_id} not found"
```

**Department Validation:**
```python
VALID_DEPARTMENTS = ['AID', 'DEV', 'HRM', 'LGN', 'VID', 'DGN', 'FIN', 'SAL', 'OPS', 'MKT']
assert row['Department'] in VALID_DEPARTMENTS, "VAL-006: Invalid department"
```

### Duplicate Detection (PMT-075 Operation 3)

**Check for Similar Projects:**
```python
from difflib import SequenceMatcher

existing_projects = load_csv("Project_Templates_Master_List.csv")
for existing in existing_projects.itertuples():
    name_similarity = SequenceMatcher(None, new_project['Name'], existing.Name).ratio()
    if name_similarity >= 0.85:
        print(f"WARNING VAL-004: Similar project found: {existing.New_ID} - {existing.Name}")
        print(f"Similarity: {name_similarity:.2%}")
```

---

## Import Workflow

### Step-by-Step Import Process

#### Step 1: Prepare Project Data

**Create CSV Entry:**
```csv
New_ID,Entity_Type,Current_ID,Name,Description,Department,Meta_Category,File_Path,Status
PRT-009,Project_Template,Project-Template-009,Customer Onboarding Automation,Complete customer onboarding workflow including welcome sequence CRM setup and success tracking,SAL,TSM-001,ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/PRT-009_Customer_Onboarding.json,Active
```

**Create JSON Detail File:**
```json
{
  "project_template_id": "PROJ-TEMPL-009",
  "template_name": "Customer Onboarding Automation",
  "template_version": "1.0",
  "department": "Sales",
  "category": "Automation",
  "created_date": "2025-11-21",

  "description": "Complete customer onboarding workflow including welcome sequence, CRM setup, and success tracking.",

  "when_to_use": [
    "Onboarding new customers after purchase",
    "Setting up automated welcome sequences",
    "Configuring CRM for new accounts",
    "Tracking customer success metrics"
  ],

  "estimated_duration": {
    "total_hours": 20,
    "total_days": 7
  },

  "milestone_templates": [
    {
      "milestone_template_id": "MIL-TEMPL-050",
      "milestone_template_name": "Onboarding Workflow Design",
      "reference": "Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone-Template-050.json"
    },
    {
      "milestone_template_id": "MIL-TEMPL-051",
      "milestone_template_name": "Email Sequence Setup",
      "reference": "Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone-Template-051.json"
    },
    {
      "milestone_template_id": "MIL-TEMPL-052",
      "milestone_template_name": "CRM Integration",
      "reference": "Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone-Template-052.json"
    }
  ],

  "expected_reports": [
    {
      "report_id": "REP-050",
      "report_name": "Onboarding Workflow Diagram",
      "milestone": "MIL-TEMPL-050"
    },
    {
      "report_id": "REP-051",
      "report_name": "Email Sequence Performance Report",
      "milestone": "MIL-TEMPL-051"
    }
  ],

  "execution_prompts": "Dropbox/ENTITIES/PROMPTS/Customer_Onboarding/",

  "instantiation_instructions": [
    "Create project folder: TASK_MANAGERS/Projects/PROJ-009_Customer_Onboarding/",
    "Create Milestones/ and Logs/ subfolders",
    "Setup CRM connection in INTEGRATIONS/",
    "Configure email templates in PROMPTS/Customer_Onboarding/"
  ],

  "version": "1.0",
  "last_updated": "2025-11-21"
}
```

#### Step 2: Stage Import

```bash
# Create staging directory
mkdir -p IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/

# Copy files to staging
cp project_data.csv IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/
cp PRT-009_Customer_Onboarding.json IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/

# Run staging operation
python import_manager.py stage \
  --entity-type Project \
  --import-id 20251121_001 \
  --source IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/
```

#### Step 3: Validate

```bash
# Run validation (PMT-075)
python import_manager.py validate \
  --entity-type Project \
  --import-id 20251121_001

# Review validation report
cat IMPORTS/Validation/20251121_001/validation_report.json
```

**Expected Validation Output:**
```json
{
  "import_id": "20251121_001",
  "entity_type": "Project",
  "timestamp": "2025-11-21T14:30:00",
  "validation_results": {
    "schema_validation": {
      "status": "PASS",
      "errors": []
    },
    "cross_reference_validation": {
      "status": "WARNING",
      "warnings": [
        "Milestone MIL-TEMPL-050 not found (may need to import milestones first)"
      ]
    },
    "duplicate_detection": {
      "status": "PASS",
      "similar_entities": []
    }
  },
  "overall_status": "WARNING",
  "recommendation": "Import milestones before integrating project"
}
```

#### Step 4: Handle Validation Results

**If validation FAILED:**
```bash
# Fix errors in staged files
vi IMPORTS/Staging/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/project_data.csv

# Re-validate
python import_manager.py validate --import-id 20251121_001 --retry
```

**If validation PASSED with WARNINGS:**
- Review warnings carefully
- If milestone references are missing, import milestones first (bottom-up approach)
- Or acknowledge warnings and proceed if acceptable

#### Step 5: Transform

```bash
# Transform validated data
python import_manager.py transform \
  --import-id 20251121_001 \
  --entity-type Project

# Review transformed data
cat IMPORTS/Transformation/20251121_001/TASK_MANAGERS/TSM-001_Project_Templates/PRT-009_Customer_Onboarding.json
```

**Transformation Operations:**
- Normalize field formats (dates, IDs)
- Enrich with metadata (creation timestamp, import source)
- Optimize for token efficiency
- Validate file paths exist
- Generate checksums for integrity

#### Step 6: Integrate

```bash
# Final integration to production
python import_manager.py integrate \
  --import-id 20251121_001 \
  --entity-type Project \
  --commit

# Verify integration
python import_manager.py status --import-id 20251121_001
```

**Integration Operations:**
1. Backup existing `Project_Templates_Master_List.csv`
2. Append new row(s) to CSV
3. Copy JSON file(s) to `TSM-001_Project_Templates/`
4. Update cross-reference maps
5. Sync related prompts (PMT-079)
6. Generate integration report

---

## Common Import Patterns

### Pattern 1: Import Standalone Project (No New Milestones)

**Use Case:** Project references existing milestones

```bash
# Step 1: Verify milestones exist
python run_prompt.py PMT-078 --query "MLT-050 MLT-051 MLT-052" --entity-type Milestone

# Step 2: Prepare project data with existing milestone references
# Step 3: Stage → Validate → Transform → Integrate
python import_manager.py stage --entity-type Project --data project.json
python import_manager.py validate --import-id 20251121_001
python import_manager.py transform --import-id 20251121_001
python import_manager.py integrate --import-id 20251121_001 --commit
```

### Pattern 2: Import Project with New Milestones (Bottom-Up)

**Use Case:** Completely new project hierarchy

```bash
# Step 1: Import milestones first
python import_manager.py stage --entity-type Milestone --data milestones.json
python import_manager.py validate --import-id 20251121_002
python import_manager.py integrate --import-id 20251121_002 --commit

# Step 2: Import project referencing new milestones
python import_manager.py stage --entity-type Project --data project.json
python import_manager.py validate --import-id 20251121_003
python import_manager.py integrate --import-id 20251121_003 --commit
```

### Pattern 3: Bulk Import Multiple Projects

**Use Case:** Migrating from external system (Asana, Jira)

```bash
# Step 1: Convert external format to ENTITIES format
python transform/asana_to_entities.py \
  --input asana_projects.csv \
  --output staging/ \
  --entity-type Project

# Step 2: Bulk stage
python import_manager.py batch-stage \
  --entity-type Project \
  --source staging/ \
  --import-id 20251121_bulk

# Step 3: Bulk validate
python import_manager.py batch-validate --import-id 20251121_bulk

# Step 4: Review consolidated report
cat IMPORTS/Validation/20251121_bulk/consolidated_report.json

# Step 5: Bulk integrate
python import_manager.py batch-integrate --import-id 20251121_bulk --commit
```

---

## Common Errors and Solutions

### Error 1: Missing Required Field

**Error Message:**
```
VAL-001: Missing required field 'New_ID' in project data
```

**Solution:**
```bash
# Add New_ID field to CSV
New_ID,Entity_Type,Current_ID,Name,Description,Department,Meta_Category,File_Path,Status
PRT-009,Project_Template,Project-Template-009,...
```

### Error 2: Invalid ID Format

**Error Message:**
```
VAL-002: Invalid ID format 'PROJ-009'. Expected pattern: PRT-\d{3}
```

**Solution:**
```bash
# Use correct ID pattern: PRT-### (not PROJ-###)
New_ID: PRT-009  # Correct
New_ID: PROJ-009 # Wrong
```

### Error 3: Department Code Invalid

**Error Message:**
```
VAL-006: Invalid department 'Sales'. Must be one of: AID, DEV, HRM, LGN, VID, DGN, FIN, SAL, OPS, MKT
```

**Solution:**
```bash
# Use department code, not full name
Department: SAL       # Correct
Department: Sales     # Wrong
```

### Error 4: Milestone Reference Not Found

**Error Message:**
```
VAL-003: Referenced milestone 'MIL-TEMPL-050' not found in Milestone_Templates_Master_List.csv
```

**Solution:**
```bash
# Option 1: Import milestone first (bottom-up)
python import_manager.py stage --entity-type Milestone --data milestone_050.json
python import_manager.py integrate --import-id 20251121_milestone

# Option 2: Update reference to existing milestone
# Change MIL-TEMPL-050 → MIL-010 (existing)
```

### Error 5: Duplicate Project Detected

**Error Message:**
```
VAL-004: Similar project detected: PRT-003 'Complete HR Automation Implementation'
Similarity: 92% with 'HR Automation Complete'
```

**Solution:**
```bash
# Option 1: Merge with existing project (if truly duplicate)
# Use PRT-003 instead of creating PRT-009

# Option 2: Differentiate clearly
# Rename: 'HR Automation Complete' → 'HR Performance Review Automation'
```

### Error 6: File Path Mismatch

**Error Message:**
```
VAL-008: File_Path 'ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/PRT-009.json'
does not match actual file 'PRT-009_Customer_Onboarding.json'
```

**Solution:**
```bash
# Ensure File_Path in CSV matches actual filename
File_Path: ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/PRT-009_Customer_Onboarding.json
```

### Error 7: Missing JSON Detail File

**Error Message:**
```
VAL-009: JSON detail file not found: PRT-009_Customer_Onboarding.json
```

**Solution:**
```bash
# Create JSON detail file matching CSV File_Path
# See "Create JSON Detail File" section above for structure
```

---

## Token Optimization

### Compact Project References

**Instead of:**
```json
{
  "milestone_templates": [
    {
      "milestone_template_id": "MIL-TEMPL-050",
      "milestone_template_name": "Onboarding Workflow Design",
      "reference": "Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone-Template-050.json",
      "description": "Design the complete onboarding workflow for new customers"
    }
  ]
}
```

**Use compact format (40% token reduction):**
```json
{
  "milestones": ["MLT-050", "MLT-051", "MLT-052"]
}
```

**Trade-off:**
- Compact format saves ~40% tokens
- Loses human-readable names and descriptions
- Requires cross-reference lookup for details
- **Recommendation:** Use compact format for production, verbose for documentation

---

## Integration with Data Architect Prompts

### Using PMT-074 (Data Architect Master)

```bash
# Route import request to appropriate sub-prompts
python run_prompt.py PMT-074 \
  --task "Import new project template" \
  --entity PRT-009 \
  --data project_data.json
```

**PMT-074 will:**
1. Route to PMT-076 (Import Pipeline) for 4-stage workflow
2. Call PMT-075 (Data Integrity) for validation
3. Call PMT-078 (Cross Entity Search) to check duplicates
4. Call PMT-079 (Prompt Taxonomy Sync) to update references

### Using PMT-075 (Data Integrity Manager)

```bash
# Run validation only
python run_prompt.py PMT-075 \
  --operation validate \
  --entity-type Project \
  --data IMPORTS/Staging/20251121_001/project_data.csv
```

### Using PMT-076 (Import Validation Pipeline)

```bash
# Run complete 4-stage import
python run_prompt.py PMT-076 \
  --source project_data.json \
  --entity-type Project \
  --auto-stage \
  --auto-commit
```

### Using PMT-078 (Cross Entity Search)

```bash
# Check if similar project exists
python run_prompt.py PMT-078 \
  --query "customer onboarding automation" \
  --entity-type Project \
  --similarity-threshold 0.8
```

---

## Best Practices

### DO:
- ✅ **Search First**: Use PMT-078 to check for similar projects before creating new ones
- ✅ **Import Milestones First**: Use bottom-up approach when creating new hierarchy
- ✅ **Use Standard Departments**: Stick to approved department codes (AID, DEV, HRM, etc.)
- ✅ **Follow Naming Conventions**: Use descriptive names with underscores (Customer_Onboarding_Automation)
- ✅ **Document When_To_Use**: Clearly define project use cases for reusability
- ✅ **Reference Existing Milestones**: Reuse milestones across projects when applicable
- ✅ **Validate Before Integrate**: Always run validation and review reports
- ✅ **Backup First**: Backups created automatically, but verify before bulk imports

### DON'T:
- ❌ **Skip Validation**: Never integrate without clean validation report
- ❌ **Use Wrong ID Pattern**: Don't use PROJ-### or PROJECT-### (use PRT-###)
- ❌ **Create Duplicates**: Check for similar projects first
- ❌ **Reference Non-Existent Milestones**: Ensure all milestone references exist
- ❌ **Use Full Department Names**: Use codes (SAL) not names (Sales)
- ❌ **Edit Production Directly**: Always use import pipeline, never edit CSV manually
- ❌ **Ignore Warnings**: Review all validation warnings even if status is PASS

---

## Example: Complete Import Session

```bash
# === SCENARIO: Import "AI Content Generation Pipeline" project ===

# Step 1: Check if similar project exists
python run_prompt.py PMT-078 \
  --query "AI content generation pipeline" \
  --entity-type Project
# Result: No similar projects found

# Step 2: Verify required milestones exist
python run_prompt.py PMT-078 \
  --query "MLT-010 MLT-011 MLT-012" \
  --entity-type Milestone
# Result: MLT-010, MLT-011 exist, MLT-012 missing

# Step 3: Import missing milestone first
python import_manager.py stage \
  --entity-type Milestone \
  --data MLT-012_Content_Distribution.json
python import_manager.py validate --import-id 20251121_milestone
python import_manager.py integrate --import-id 20251121_milestone --commit

# Step 4: Prepare project data
cat > PRT-010_AI_Content_Pipeline.json <<EOF
{
  "project_template_id": "PROJ-TEMPL-010",
  "template_name": "AI Content Generation Pipeline",
  "template_version": "1.0",
  "department": "AI",
  "category": "Content",
  "created_date": "2025-11-21",
  "description": "End-to-end AI content generation pipeline from research to publishing",
  "when_to_use": [
    "Generating blog posts with AI",
    "Creating social media content at scale",
    "Automating content distribution"
  ],
  "milestone_templates": [
    {"milestone_template_id": "MIL-TEMPL-010", "milestone_template_name": "Research"},
    {"milestone_template_id": "MIL-TEMPL-011", "milestone_template_name": "Generation"},
    {"milestone_template_id": "MIL-TEMPL-012", "milestone_template_name": "Distribution"}
  ],
  "version": "1.0",
  "last_updated": "2025-11-21"
}
EOF

# Step 5: Stage project import
python import_manager.py stage \
  --entity-type Project \
  --data PRT-010_AI_Content_Pipeline.json

# Step 6: Validate
python import_manager.py validate --import-id 20251121_project
# Result: PASS (all milestones exist, no duplicates, schema valid)

# Step 7: Transform
python import_manager.py transform --import-id 20251121_project

# Step 8: Integrate
python import_manager.py integrate --import-id 20251121_project --commit

# Step 9: Verify
python run_prompt.py PMT-078 --query "PRT-010" --entity-type Project
# Result: PRT-010 found with 3 milestones

# Step 10: Update related prompts
python run_prompt.py PMT-079 --sync-entity PRT-010

# === IMPORT COMPLETE ===
```

---

## Related Guides

- **Master Guide:** [TASK_MANAGERS_Import_Guide_Master.md](TASK_MANAGERS_Import_Guide_Master.md)
- **Next Level:** [TSM-002_Milestone_Templates_Import_Guide.md](TSM-002_Milestone_Templates_Import_Guide.md)
- **Child Entities:** [TSM-003_Task_Templates_Import_Guide.md](TSM-003_Task_Templates_Import_Guide.md)

---

## Quick Reference

### File Naming
```
CSV Entry: PRT-###
JSON File: PRT-###_[ShortName].json
Example: PRT-009_Customer_Onboarding.json
```

### Required CSV Fields
```
New_ID, Entity_Type, Current_ID, Name, Description,
Department, Meta_Category, File_Path, Status
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
python import_manager.py stage --entity-type Project --data [file]

# Validate
python import_manager.py validate --import-id [ID]

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
- Initial guide for TSM-001 Project Templates
- Complete field documentation
- Validation rules and error handling
- Import patterns and examples
- Integration with PMT-074 through PMT-080

---

**Status:** Active

---

**End of Guide**
