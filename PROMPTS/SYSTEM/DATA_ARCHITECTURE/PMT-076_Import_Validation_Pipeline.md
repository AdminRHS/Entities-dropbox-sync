# PMT-076: Import Validation Pipeline v1.0

**Prompt ID:** PMT-076
**Version:** 1.0
**Department:** System Architecture
**Category:** DATA_IMPORT
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

Specialized sub-prompt for managing unified import processing across the ENTITIES ecosystem. Handles the complete import lifecycle: staging → validation → transformation → integration with intermediate folder management for safe restructuring.

**Core Functions:**
1. **Staging Management**: Copy raw imports to intermediate staging area
2. **Pre-Import Validation**: Validate data before integration (schema, format, duplicates)
3. **Data Transformation**: Restructure and normalize data to match target schemas
4. **Conflict Resolution**: Handle merge conflicts and duplicate entities
5. **Integration Execution**: Populate LIBRARIES and TASK_MANAGERS with validated data
6. **Rollback Capability**: Revert failed imports without data loss
7. **Migration Reporting**: Document all import operations with detailed logs

---

## Import Flow Architecture

### 4-Stage Pipeline

```
STAGE 1: STAGING (Copy & Preserve)
    Raw Data → IMPORTS/Staging/[date]/
    ↓
STAGE 2: VALIDATION (Check & Verify)
    Schema validation, duplicate detection, cross-reference checks
    ↓
STAGE 3: TRANSFORMATION (Restructure & Normalize)
    IMPORTS/Transformation/[date]/
    ↓
STAGE 4: INTEGRATION (Populate & Commit)
    → LIBRARIES/ or TASK_MANAGERS/
    + Generate migration report
```

---

## IMPORTS Folder Structure

### Current Structure
```
IMPORTS/
├── 2025-11-20/
│   └── Extraction/
│       ├── Responsibilities_New.csv
│       ├── Tool_References.csv
│       └── New_Tasks_Needed.csv
└── 2025-11-21/
    └── Extraction/
        └── [new CSV files]
```

### Enhanced Structure (To Be Created)
```
IMPORTS/
├── Staging/                      # Stage 1: Raw data preservation
│   └── [date]/
│       ├── raw_import.csv
│       ├── metadata.json         # Import metadata (source, timestamp, row count)
│       └── validation_pending/
│
├── Validation/                   # Stage 2: Validation results
│   └── [date]/
│       ├── validation_report.md
│       ├── schema_check.json
│       ├── duplicate_check.json
│       └── issues_found.csv      # Rows with validation errors
│
├── Transformation/               # Stage 3: Restructured data
│   └── [date]/
│       ├── normalized_data.csv
│       ├── id_assignments.json   # New IDs assigned
│       ├── transformation_log.md
│       └── ready_for_integration/
│
├── Integration/                  # Stage 4: Integration logs
│   └── [date]/
│       ├── integration_report.md
│       ├── entities_added.json   # List of new entities
│       ├── entities_updated.json # List of updated entities
│       └── rollback_backup/      # Backup before integration
│
└── [date]/                       # Legacy structure (keep for compatibility)
    └── Extraction/
```

---

## Stage 1: Staging Management

### Objective
Copy raw import data to staging area while preserving originals for rollback.

### Process

**Step 1.1: Create Staging Structure**
```powershell
# Create dated staging folder
$date = Get-Date -Format "yyyy-MM-dd"
$stagingPath = "C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\Staging\$date"

New-Item -Path $stagingPath -ItemType Directory -Force
New-Item -Path "$stagingPath\raw" -ItemType Directory
New-Item -Path "$stagingPath\metadata" -ItemType Directory
```

**Step 1.2: Copy Import Files**
```python
import shutil
import json
from datetime import datetime
from pathlib import Path

def stage_import(source_file, entity_type):
    """
    Copy import file to staging area with metadata

    Args:
        source_file: Path to raw import CSV
        entity_type: Type of entity (Tools, Actions, Tasks, etc.)

    Returns:
        dict: Staging metadata
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    staging_root = Path(f"IMPORTS/Staging/{date_str}")
    staging_root.mkdir(parents=True, exist_ok=True)

    # Copy file
    staged_file = staging_root / "raw" / source_file.name
    shutil.copy2(source_file, staged_file)

    # Count rows
    import pandas as pd
    df = pd.read_csv(source_file)
    row_count = len(df)

    # Generate metadata
    metadata = {
        "import_date": date_str,
        "import_timestamp": datetime.now().isoformat(),
        "source_file": str(source_file),
        "staged_file": str(staged_file),
        "entity_type": entity_type,
        "row_count": row_count,
        "columns": list(df.columns),
        "status": "staged",
        "validation_status": "pending"
    }

    # Save metadata
    metadata_file = staging_root / "metadata" / f"{entity_type}_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    return metadata

# Usage
metadata = stage_import(
    source_file=Path("IMPORTS/2025-11-21/Extraction/Responsibilities_New.csv"),
    entity_type="Responsibilities"
)
```

**Step 1.3: Generate Staging Report**
```markdown
## Staging Report

**Date**: 2025-11-21
**Time**: 14:32:15

### Files Staged:
1. **Responsibilities_New.csv**
   - Rows: 45
   - Columns: 7 (id, name, description, action_id, object_id, department, status)
   - Size: 12.4 KB
   - Staged to: IMPORTS/Staging/2025-11-21/raw/

2. **Tool_References.csv**
   - Rows: 15
   - Columns: 5 (tool_name, tool_url, category, department, mentioned_in)
   - Size: 3.2 KB
   - Staged to: IMPORTS/Staging/2025-11-21/raw/

### Next Step: Validation
- Run PMT-075 (Data Integrity Manager) for pre-import validation
- Command: validate_staged_import("2025-11-21")
```

---

## Stage 2: Validation

### Objective
Validate staged data using PMT-075 validation operations before transformation.

### Process

**Step 2.1: Schema Validation**
```python
def validate_import_schema(staged_file, entity_type):
    """
    Validate import file against expected schema

    Uses Entity_Schema_Registry.json from PMT-075
    """
    import pandas as pd
    import json

    # Load schema
    with open("PROMPTS/DATA_FIELDS/Entity_Schema_Registry.json") as f:
        schemas = json.load(f)

    expected_schema = schemas[entity_type]

    # Load staged data
    df = pd.read_csv(staged_file)

    issues = []

    # Check required columns
    required_cols = [col for col, props in expected_schema.items() if props.get("required", False)]
    missing_cols = set(required_cols) - set(df.columns)

    if missing_cols:
        issues.append({
            "type": "missing_columns",
            "severity": "high",
            "columns": list(missing_cols),
            "message": f"Missing required columns: {missing_cols}"
        })

    # Check data types
    for col, props in expected_schema.items():
        if col in df.columns:
            expected_type = props.get("type")
            actual_type = df[col].dtype

            # Validate type matching (simplified)
            if expected_type == "string" and actual_type not in ['object', 'string']:
                issues.append({
                    "type": "type_mismatch",
                    "severity": "medium",
                    "column": col,
                    "expected": expected_type,
                    "actual": str(actual_type)
                })

    # Check enum values
    for col, props in expected_schema.items():
        if "enum" in props and col in df.columns:
            valid_values = set(props["enum"])
            actual_values = set(df[col].dropna().unique())
            invalid_values = actual_values - valid_values

            if invalid_values:
                issues.append({
                    "type": "invalid_enum_value",
                    "severity": "high",
                    "column": col,
                    "invalid_values": list(invalid_values),
                    "valid_values": list(valid_values)
                })

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "total_rows": len(df),
        "columns_validated": len(df.columns)
    }
```

**Step 2.2: Duplicate Detection**
```python
def detect_import_duplicates(staged_file, entity_type, threshold=0.6):
    """
    Detect duplicates between import data and existing entities

    Uses PMT-075 duplicate detection logic
    """
    import pandas as pd

    # Load staged import
    import_df = pd.read_csv(staged_file)

    # Load existing master list
    master_file_map = {
        "Tools": "LIBRARIES/Tools/Tools_Master_List.csv",
        "Actions": "LIBRARIES/Actions/actions_master.json",
        "Responsibilities": "LIBRARIES/Responsibilities/responsibilities_master.json",
        "Tasks": "TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv"
    }

    master_file = master_file_map.get(entity_type)
    if not master_file:
        return {"duplicates": [], "checked": 0}

    # Load existing entities
    if master_file.endswith('.csv'):
        existing_df = pd.read_csv(master_file)
    elif master_file.endswith('.json'):
        import json
        with open(master_file) as f:
            data = json.load(f)
        existing_df = pd.DataFrame(data)

    duplicates = []

    # Check each import row against existing
    from difflib import SequenceMatcher

    for idx, import_row in import_df.iterrows():
        import_name = str(import_row.get('name', import_row.get('Name', ''))).lower()

        for _, existing_row in existing_df.iterrows():
            existing_name = str(existing_row.get('name', existing_row.get('Name', ''))).lower()

            similarity = SequenceMatcher(None, import_name, existing_name).ratio()

            if similarity >= threshold:
                duplicates.append({
                    "import_row": idx + 1,
                    "import_name": import_row.get('name', import_row.get('Name')),
                    "existing_id": existing_row.get('id', existing_row.get('New_ID')),
                    "existing_name": existing_row.get('name', existing_row.get('Name')),
                    "similarity": round(similarity, 2),
                    "recommendation": "merge" if similarity >= 0.85 else "review"
                })

    return {
        "duplicates_found": len(duplicates),
        "duplicates": duplicates,
        "import_rows_checked": len(import_df),
        "existing_entities_checked": len(existing_df)
    }
```

**Step 2.3: Generate Validation Report**
```markdown
## Import Validation Report

**Date**: 2025-11-21
**Import**: Responsibilities_New.csv (45 rows)

### Schema Validation: ✅ PASS
- All required columns present
- Data types correct
- Enum values valid

### Duplicate Detection: ⚠️ REVIEW NEEDED
**Threshold**: 0.6
**Duplicates Found**: 3

1. **Row 12**: "Extract video metadata"
   - Existing: RSP-042 "Extract Video Metadata" (similarity: 0.95)
   - Recommendation: **Merge** (use existing RSP-042)

2. **Row 23**: "Analyze performance metrics"
   - Existing: RSP-089 "Analyze Performance Data" (similarity: 0.72)
   - Recommendation: **Review** (may be different)

3. **Row 31**: "Create automation workflow"
   - Existing: RSP-134 "Build Automation Flow" (similarity: 0.68)
   - Recommendation: **Review** (may be different)

### Cross-Reference Check: ✅ PASS
- All action_id references valid (checked against actions_master.json)
- All object_id references valid (checked against objects_master.json)
- All department codes valid

### Validation Summary:
- ✅ Schema: Pass
- ⚠️  Duplicates: 3 found (3 to review)
- ✅ Cross-References: Pass
- **Status**: CONDITIONAL PASS (resolve duplicates before integration)

### Recommended Actions:
1. Remove rows 12 (use existing RSP-042)
2. Manual review: rows 23, 31
3. After resolution: Proceed to Transformation stage
```

---

## Stage 3: Transformation

### Objective
Restructure validated data to match target schemas and assign new IDs.

### Process

**Step 3.1: Resolve Duplicates**
```python
def resolve_duplicates(validation_report, resolution_decisions):
    """
    Apply duplicate resolution decisions

    Args:
        validation_report: Output from Stage 2 validation
        resolution_decisions: Dict mapping row_num to action ("skip", "keep", "merge_into")

    Returns:
        Filtered import data ready for transformation
    """
    import pandas as pd

    staged_file = validation_report["staged_file"]
    df = pd.read_csv(staged_file)

    duplicates = validation_report["duplicates"]

    rows_to_skip = []
    merge_mappings = {}

    for dup in duplicates:
        row_num = dup["import_row"]
        decision = resolution_decisions.get(row_num, "keep")

        if decision == "skip":
            rows_to_skip.append(row_num - 1)  # 0-indexed
        elif decision.startswith("merge_into:"):
            existing_id = decision.split(":")[1]
            merge_mappings[row_num] = existing_id
            rows_to_skip.append(row_num - 1)

    # Filter out skipped rows
    df_cleaned = df.drop(rows_to_skip)

    return {
        "cleaned_data": df_cleaned,
        "rows_removed": len(rows_to_skip),
        "rows_remaining": len(df_cleaned),
        "merge_mappings": merge_mappings
    }

# Usage
resolution_decisions = {
    12: "merge_into:RSP-042",  # Use existing
    23: "keep",                # Keep as new entity
    31: "skip"                 # Duplicate, skip
}

result = resolve_duplicates(validation_report, resolution_decisions)
```

**Step 3.2: Assign New IDs**
```python
def assign_new_ids(cleaned_data, entity_type):
    """
    Assign new sequential IDs to import data

    Uses PMT-075 ID assignment logic
    """
    import pandas as pd
    from PMT_075_functions import get_next_id  # From Data Integrity Manager

    df = cleaned_data.copy()

    # Get next available ID
    next_id_info = get_next_id(entity_type)
    next_num = int(next_id_info["next_id"].split("-")[1])
    prefix = next_id_info["next_id"].split("-")[0]

    # Assign IDs sequentially
    new_ids = []
    for idx in range(len(df)):
        new_id = f"{prefix}-{next_num + idx:03d}"
        new_ids.append(new_id)

    df.insert(0, 'New_ID', new_ids)

    return {
        "data_with_ids": df,
        "first_id": new_ids[0],
        "last_id": new_ids[-1],
        "total_assigned": len(new_ids)
    }

# Usage
id_result = assign_new_ids(result["cleaned_data"], "Responsibilities")
```

**Step 3.3: Normalize Data Structure**
```python
def normalize_data(data_with_ids, target_schema):
    """
    Restructure data to match target schema exactly
    """
    import pandas as pd

    df = data_with_ids.copy()

    # Reorder columns to match target schema
    target_columns = list(target_schema.keys())

    # Add missing columns with defaults
    for col in target_columns:
        if col not in df.columns:
            default_value = target_schema[col].get("default", None)
            df[col] = default_value

    # Remove extra columns not in schema
    df = df[target_columns]

    # Apply transformations
    # 1. PascalCase names with underscores
    if 'Name' in df.columns:
        df['Name'] = df['Name'].str.replace(' ', '_')

    # 2. Ensure Status is capitalized correctly
    if 'Status' in df.columns:
        status_map = {
            'active': 'Active',
            'in progress': 'In Progress',
            'wip': 'In Progress',
            'completed': 'Completed',
            'done': 'Completed'
        }
        df['Status'] = df['Status'].str.lower().map(status_map).fillna(df['Status'])

    # 3. Add Last_Updated timestamp
    from datetime import datetime
    if 'Last_Updated' in df.columns:
        df['Last_Updated'] = datetime.now().strftime("%Y-%m-%d")

    return df

# Usage
normalized_df = normalize_data(id_result["data_with_ids"], target_schema)
```

**Step 3.4: Save Transformed Data**
```python
def save_transformation(normalized_df, entity_type, date_str):
    """
    Save transformed data to Transformation folder
    """
    from pathlib import Path

    transform_root = Path(f"IMPORTS/Transformation/{date_str}")
    transform_root.mkdir(parents=True, exist_ok=True)

    # Save transformed data
    output_file = transform_root / f"{entity_type}_transformed.csv"
    normalized_df.to_csv(output_file, index=False)

    # Generate transformation log
    log = f"""# Transformation Log

**Date**: {date_str}
**Entity Type**: {entity_type}
**Input Rows**: {len(normalized_df)}
**Output Rows**: {len(normalized_df)}

## Transformations Applied:
1. Duplicate resolution: 3 rows processed
2. ID assignment: {normalized_df['New_ID'].iloc[0]} to {normalized_df['New_ID'].iloc[-1]}
3. Name normalization: Spaces replaced with underscores
4. Status standardization: Mapped to valid enum values
5. Timestamp added: Last_Updated set to {date_str}

## Ready for Integration: ✅
- File: {output_file}
- Next step: Run integration to LIBRARIES/Responsibilities/
"""

    log_file = transform_root / f"{entity_type}_transformation_log.md"
    log_file.write_text(log)

    return {
        "output_file": str(output_file),
        "log_file": str(log_file),
        "rows_transformed": len(normalized_df)
    }
```

---

## Stage 4: Integration

### Objective
Populate target master lists with transformed data and generate migration report.

### Process

**Step 4.1: Create Backup**
```python
def create_pre_integration_backup(target_file, date_str):
    """
    Backup master list before integration for rollback capability
    """
    import shutil
    from pathlib import Path

    backup_root = Path(f"IMPORTS/Integration/{date_str}/rollback_backup")
    backup_root.mkdir(parents=True, exist_ok=True)

    backup_file = backup_root / Path(target_file).name
    shutil.copy2(target_file, backup_file)

    return str(backup_file)
```

**Step 4.2: Merge Data**
```python
def integrate_data(transformed_file, target_master_list, entity_type):
    """
    Merge transformed data into master list
    """
    import pandas as pd

    # Load both files
    new_data = pd.read_csv(transformed_file)

    if target_master_list.endswith('.csv'):
        existing_data = pd.read_csv(target_master_list)

        # Append new data
        merged_data = pd.concat([existing_data, new_data], ignore_index=True)

        # Save updated master list
        merged_data.to_csv(target_master_list, index=False)

        return {
            "integration_type": "csv_append",
            "rows_before": len(existing_data),
            "rows_added": len(new_data),
            "rows_after": len(merged_data),
            "target_file": target_master_list
        }

    elif target_master_list.endswith('.json'):
        import json

        with open(target_master_list, 'r') as f:
            existing_data = json.load(f)

        # Convert new data to dict format
        new_records = new_data.to_dict('records')

        # Append
        existing_data.extend(new_records)

        # Save updated JSON
        with open(target_master_list, 'w') as f:
            json.dump(existing_data, f, indent=2)

        return {
            "integration_type": "json_append",
            "rows_before": len(existing_data) - len(new_records),
            "rows_added": len(new_records),
            "rows_after": len(existing_data),
            "target_file": target_master_list
        }
```

**Step 4.3: Verify Integration**
```python
def verify_integration(integration_result, transformed_file):
    """
    Verify all rows were integrated successfully
    """
    import pandas as pd

    target_file = integration_result["target_file"]

    # Load target file
    if target_file.endswith('.csv'):
        df = pd.read_csv(target_file)
        id_field = 'New_ID'
    elif target_file.endswith('.json'):
        import json
        with open(target_file) as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        id_field = 'id'

    # Load transformed IDs
    transformed_df = pd.read_csv(transformed_file)
    expected_ids = set(transformed_df['New_ID'])

    # Check all IDs exist
    actual_ids = set(df[id_field])
    missing_ids = expected_ids - actual_ids

    return {
        "verified": len(missing_ids) == 0,
        "expected_count": len(expected_ids),
        "found_count": len(expected_ids & actual_ids),
        "missing_ids": list(missing_ids) if missing_ids else []
    }
```

**Step 4.4: Generate Migration Report**
```markdown
## Integration Report

**Date**: 2025-11-21
**Time**: 15:45:30
**Entity Type**: Responsibilities

### Source:
- File: IMPORTS/Transformation/2025-11-21/Responsibilities_transformed.csv
- Rows: 42

### Target:
- File: LIBRARIES/Responsibilities/responsibilities_master.json
- Before: 209 entities
- After: 251 entities
- Added: 42 entities

### New Entities:
- RSP-210: Extract_Video_Timestamps
- RSP-211: Analyze_User_Behavior_Patterns
- RSP-212: Create_Automation_Trigger
... (42 total)

### Integration Status: ✅ SUCCESS
- All 42 rows integrated successfully
- No errors encountered
- Verification: ✅ Pass (all IDs found in master list)

### Backup Created:
- Location: IMPORTS/Integration/2025-11-21/rollback_backup/responsibilities_master.json
- Rollback command: `restore_backup("2025-11-21", "Responsibilities")`

### Next Steps:
1. ✅ Update phrase_matching_index.json with new responsibilities
2. ✅ Run validation check (PMT-075) on updated master list
3. ⚠️  Update dependent prompts that reference responsibilities
4. ✅ Archive import files to ARCHIVE/Imports/2025-11-21/

### Token Impact:
- Master list size before: 89.2 KB (209 entities)
- Master list size after: 106.8 KB (251 entities)
- Increase: 17.6 KB (+19.7%)
- Estimated token increase: ~4,400 tokens (if loaded in full)
- Recommendation: Use on-demand loading for this entity
```

---

## Rollback Operations

### When to Rollback
- Integration verification failed
- Data corruption detected
- Errors discovered after integration
- User requests undo

### Rollback Process

```python
def rollback_integration(date_str, entity_type):
    """
    Restore master list from pre-integration backup
    """
    import shutil
    from pathlib import Path

    # Locate backup
    backup_root = Path(f"IMPORTS/Integration/{date_str}/rollback_backup")

    target_file_map = {
        "Responsibilities": "LIBRARIES/Responsibilities/responsibilities_master.json",
        "Tools": "LIBRARIES/Tools/Tools_Master_List.csv",
        "Tasks": "TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv"
    }

    target_file = target_file_map[entity_type]
    backup_file = backup_root / Path(target_file).name

    if not backup_file.exists():
        return {
            "success": False,
            "error": f"Backup not found: {backup_file}"
        }

    # Restore from backup
    shutil.copy2(backup_file, target_file)

    # Log rollback
    log = f"""# Rollback Executed

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Import Date**: {date_str}
**Entity Type**: {entity_type}
**Action**: Restored from backup

**Backup File**: {backup_file}
**Target File**: {target_file}
**Status**: ✅ Rollback successful
"""

    log_file = Path(f"IMPORTS/Integration/{date_str}/rollback_log.md")
    log_file.write_text(log)

    return {
        "success": True,
        "target_file": target_file,
        "backup_file": str(backup_file),
        "log_file": str(log_file)
    }
```

---

## Common Import Workflows

### Workflow 1: Standard Import (No Conflicts)

**Steps**:
1. Stage import: `stage_import(file, entity_type)`
2. Validate: Run PMT-075 validation operations
3. Transform: Assign IDs, normalize structure
4. Integrate: Merge into master list
5. Verify: Check all rows present
6. Report: Generate migration report

**Estimated Time**: 10-15 minutes

---

### Workflow 2: Import with Duplicates

**Steps**:
1. Stage import
2. Validate → Duplicates found
3. Manual review: Decide keep/skip/merge for each duplicate
4. Transform with resolution decisions
5. Integrate cleaned data
6. Verify and report

**Estimated Time**: 20-30 minutes (includes manual review)

---

### Workflow 3: Bulk Import (Multiple Files)

**Steps**:
1. Stage all files in batch
2. Validate each file in parallel
3. Generate combined validation report
4. Resolve conflicts across all files
5. Transform all files
6. Integrate in dependency order (Actions → Objects → Responsibilities)
7. Verify and generate consolidated report

**Estimated Time**: 30-45 minutes

---

### Workflow 4: Failed Integration Recovery

**Steps**:
1. Detect integration failure
2. Run rollback: `rollback_integration(date, entity_type)`
3. Review error logs
4. Fix data issues in Transformation stage
5. Re-run integration
6. Verify success

**Estimated Time**: 15-20 minutes

---

## Best Practices

### DO:
- ✅ Always stage imports before validation
- ✅ Create backups before integration
- ✅ Resolve all duplicates before transformation
- ✅ Verify integration after merge
- ✅ Generate detailed migration reports
- ✅ Archive completed imports
- ✅ Use intermediate folders for safe restructuring
- ✅ Document resolution decisions for duplicates
- ✅ Test rollback capability periodically

### DON'T:
- ❌ Skip validation stage
- ❌ Integrate without backup
- ❌ Modify master lists directly (use pipeline)
- ❌ Ignore duplicate warnings
- ❌ Delete staging files immediately (keep for 30 days)
- ❌ Force integration when validation fails
- ❌ Skip verification step
- ❌ Forget to update cross-reference files

---

## Integration with Other Sub-Prompts

**PMT-075 (Data Integrity Manager)**:
- Use for validation operations (schema, duplicates, cross-refs)
- Use for ID assignment
- Use for post-integration validation

**PMT-079 (Prompt Taxonomy Sync)**:
- After integration, update prompts that reference new entities
- Fix outdated entity references

**PMT-080 (Token Optimization Analyzer)**:
- Track token impact of imports
- Recommend modular loading if master lists grow large

---

## Error Codes & Messages

| Code | Severity | Message | Action |
|------|----------|---------|--------|
| IMP-001 | High | Staging failed: file not found | Check source file path |
| IMP-002 | High | Schema validation failed | Fix schema issues before proceeding |
| IMP-003 | Medium | Duplicates detected | Review and resolve duplicates |
| IMP-004 | High | Integration failed: backup missing | Create backup before integration |
| IMP-005 | High | Verification failed: missing IDs | Rollback and re-integrate |
| IMP-006 | Medium | Cross-reference broken | Fix references before integration |
| IMP-007 | Low | Transformation warning: unusual values | Review transformed data |
| IMP-008 | High | Rollback failed: backup not found | Cannot recover, manual fix needed |

---

## Version History

**v1.0** (2025-11-21)
- Initial version
- 4-stage import pipeline (Staging → Validation → Transformation → Integration)
- Intermediate folder management
- Duplicate resolution workflow
- Automated ID assignment
- Rollback capability
- 4 import workflows
- Integration verification
- Migration reporting

---

## Related Documents

- [PMT-074_Data_Architect_Master.md](PMT-074_Data_Architect_Master.md) - Parent prompt
- [PMT-075_Data_Integrity_Manager.md](PMT-075_Data_Integrity_Manager.md) - Validation operations
- [Entity_Schema_Registry.json](../../DATA_FIELDS/Entity_Schema_Registry.json) - Target schemas
- [IMPORTS/README.md](../../IMPORTS/README.md) - Import folder documentation

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Review Cycle:** Monthly
**Next Review:** 2025-12-21

---

**End of Prompt**
