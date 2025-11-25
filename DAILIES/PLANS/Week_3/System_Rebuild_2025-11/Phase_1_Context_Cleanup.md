# Phase 1 Context: Data Cleanup & Consolidation

**Phase**: 1 of 6
**Agents**: 3 simultaneous
**Priority**: P1-HIGH
**Dependencies**: None (executes after Phase 0)
**Estimated Complexity**: Medium

---

## 🎯 Phase Objectives

1. **Clean up nested backup folders** in LIBRARIES (8 levels deep)
2. **Resolve 23 duplicate IDs** in Task Templates and Tools
3. **Analyze 298 empty prospect folders** and recommend keep/delete

---

## 🤖 Agent Assignments

### Agent 1A: Backup Cleanup Agent
**Focus**: Remove redundant nested backups in LIBRARIES
**Working Directory**: `LIBRARIES/Archive/`
**Output**: Cleanup report + single consolidated archive

### Agent 1B: Duplicate ID Resolution Agent
**Focus**: Fix 23 duplicate IDs in Task Templates and Tools
**Working Directory**: `TASK_MANAGERS/` and `LIBRARIES/LBS_003_Tools/`
**Output**: Updated files + ID resolution report

### Agent 1C: Empty Folder Analysis Agent
**Focus**: Analyze 298 empty prospect folders
**Working Directory**: `BUSINESSES/Prospects/`
**Output**: Analysis report with recommendations

---

## 📋 Agent 1A: Backup Cleanup

### Problem Statement
Current state has nested backup folders 8 levels deep:
```
LIBRARIES/Archive/backup_20251119_055410/
  backup_20251119_055410/
    backup_20251119_055410/
      ... (8 levels total)
```

### Task Instructions

#### Step 1: Inventory Current Backups
Scan `LIBRARIES/Archive/` and catalog:
- All backup folders (name, date, depth level)
- Total size per backup
- Duplicate files across backups
- Output: `Backup_Inventory.csv`

#### Step 2: Identify Unique Files
For each nested backup level, identify:
- Files that exist ONLY in that backup (unique)
- Files that are duplicates of other levels
- Output: `Unique_Files_Per_Backup.csv`

#### Step 3: Consolidate to Single Archive
Create single archive folder:
```
ARCHIVE/Libraries_Backup_2025-11-22/
├── Original_Backups/
│   └── backup_20251119_055410/ (flattened, one level only)
├── Unique_Files/ (any files found only in nested levels)
└── Backup_Manifest.csv (index of all files)
```

#### Step 4: Delete Nested Backups from LIBRARIES
After consolidation, remove:
- `LIBRARIES/Archive/backup_20251119_055410/` (all nested levels)
- Any other nested backup folders found

#### Step 5: Update LIBRARIES README
Add section to `LIBRARIES/README.md`:
```markdown
## Archive History
- **2025-11-22**: Consolidated nested backups (8 levels) into single archive
- **Location**: `ARCHIVE/Libraries_Backup_2025-11-22/`
- **Original Backup Date**: 2025-11-19 05:54:10
- **Files Preserved**: [count] unique files
```

### Input Files
- `LIBRARIES/Archive/` (all nested folders)
- `LIBRARIES/README.md` (for update)

### Output Files
```
REPORTS/2025-11-22/System_Rebuild/
├── Phase_1A_Backup_Inventory.csv
├── Phase_1A_Unique_Files_Per_Backup.csv
├── Phase_1A_Cleanup_Report.md
└── Phase_1A_Deleted_Folders_Log.txt

ARCHIVE/Libraries_Backup_2025-11-22/
├── Original_Backups/
├── Unique_Files/
└── Backup_Manifest.csv

LIBRARIES/README.md (updated)
```

### Success Criteria
- [ ] Zero backup folders in `LIBRARIES/Archive/` nested deeper than 1 level
- [ ] All unique files preserved in `ARCHIVE/Libraries_Backup_2025-11-22/`
- [ ] Backup manifest CSV lists all archived files with source paths
- [ ] Cleanup report documents what was deleted and what was kept
- [ ] LIBRARIES README updated with archive history

### Risk Mitigation
**Risk**: Accidentally delete unique files
**Mitigation**:
1. Create consolidated archive FIRST
2. Verify all unique files copied successfully
3. Generate manifest CSV for verification
4. Only delete after manual review of manifest

---

## 📋 Agent 1B: Duplicate ID Resolution

### Problem Statement
23 duplicate IDs found across:
- Task Templates in `TASK_MANAGERS/TSM-003_Task_Templates/`
- Tools in `LIBRARIES/LBS_003_Tools/`

### Task Instructions

#### Step 1: Identify All Duplicate IDs
Scan the following files for duplicate IDs:
- `TASK_MANAGERS/TSM-003_Task_Templates/*.json` (all task template files)
- `TASK_MANAGERS/Task_Templates_Master_List.csv`
- `LIBRARIES/LBS_003_Tools/**/*.json` (all tool files recursively)
- `LIBRARIES/LBS_003_Tools/Tools_Master_List.csv`

Generate report listing:
- Duplicate ID
- Files containing this ID
- Entity names using this ID
- Suggested new ID for duplicates

Output: `Duplicate_IDs_Inventory.csv`

Format:
```csv
Duplicate_ID,File_1,File_2,Entity_Name_1,Entity_Name_2,Suggested_New_ID,Resolution_Strategy
TASK-015,Task-Template-015.json,Task-Template-015_v2.json,Design Research,Video Research,TASK-051,Renumber second file
TOL-042,Tool_Figma.json,Tool_FigJam.json,Figma,FigJam,TOL-165,Renumber FigJam
```

#### Step 2: Resolve Task Template Duplicates
For each duplicate in Task Templates:
1. Determine which instance is "canonical" (most referenced, newest, or explicitly marked)
2. Assign new sequential ID to duplicate(s)
3. Update JSON file with new ID
4. Update all references in other files
5. Log change in resolution report

**ID Numbering Strategy**:
- Existing Task Templates: TASK-001 to TASK-050
- New IDs start at: TASK-051
- Increment sequentially for each duplicate resolved

#### Step 3: Resolve Tool Duplicates
For each duplicate in Tools:
1. Check `Tools_Master_List.csv` for highest existing ID
2. Assign new sequential IDs starting after highest
3. Update JSON files
4. Update Tools_Master_List.csv
5. Update any references in Task Templates or Prompts

**ID Numbering Strategy**:
- Existing Tools: TOL-001 to TOL-164 (with duplicates)
- New IDs start after cleanup: TOL-165+
- Maintain ISO codes and categories

#### Step 4: Update Master Lists
Regenerate master lists with corrected IDs:
- `TASK_MANAGERS/Task_Templates_Master_List.csv`
- `LIBRARIES/LBS_003_Tools/Tools_Master_List.csv`
- `TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv` (copy)

Ensure:
- All IDs are unique
- IDs are sequential (no gaps unless intentional)
- Counts match file system (50 tasks = TASK-001 to TASK-050, etc.)

#### Step 5: Validate Cross-References
Scan these locations for references to old IDs that need updating:
- `PROMPTS/` (all subdirectories for tool/task references)
- `TASK_MANAGERS/TSM-002_Milestone_Templates/` (milestone may reference tasks)
- `DAILIES/` (recent dailies may reference tasks/tools)
- `TASK_MANAGERS/RESEARCHES/` (research reports may reference tools)

Update any files containing old duplicate IDs.

### Input Files
```
TASK_MANAGERS/TSM-003_Task_Templates/*.json
TASK_MANAGERS/Task_Templates_Master_List.csv
LIBRARIES/LBS_003_Tools/**/*.json
LIBRARIES/LBS_003_Tools/Tools_Master_List.csv
TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv
PROMPTS/**/* (for cross-reference validation)
```

### Output Files
```
REPORTS/2025-11-22/System_Rebuild/
├── Phase_1B_Duplicate_IDs_Inventory.csv
├── Phase_1B_ID_Resolution_Report.md
├── Phase_1B_Cross_Reference_Updates.csv
└── Phase_1B_Before_After_Comparison.csv

TASK_MANAGERS/Task_Templates_Master_List.csv (updated)
LIBRARIES/LBS_003_Tools/Tools_Master_List.csv (updated)
TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv (updated)
[Multiple JSON files updated with new IDs]
```

### Success Criteria
- [ ] Zero duplicate IDs in Task Templates
- [ ] Zero duplicate IDs in Tools
- [ ] All master lists regenerated with unique sequential IDs
- [ ] All cross-references updated (no broken links to old IDs)
- [ ] Before/after comparison shows exactly 23 ID changes
- [ ] Resolution report documents every ID change with rationale

### Reference Schema

**Task Template ID Format**:
```json
{
  "entity_type": "Task_Template",
  "entity_id": "TASK-XXX",
  "template_name": "ACTION_OBJECT_CONTEXT",
  ...
}
```

**Tool ID Format**:
```json
{
  "entity_type": "Tool",
  "sub_entity": "AI|Development|Design|etc",
  "entity_id": "TOL-XXX",
  "iso_code": "XXX",
  ...
}
```

---

## 📋 Agent 1C: Empty Folder Analysis

### Problem Statement
298 prospect folders exist in `BUSINESSES/Prospects/` but are empty (no JSON files).
Only 33 prospects have actual JSON data.

Need to determine:
1. Why these folders exist (import artifacts? placeholders?)
2. Whether to keep (and populate later) or delete
3. If keeping, what data structure should populate them

### Task Instructions

#### Step 1: Inventory Empty Folders
Scan `BUSINESSES/Prospects/` and catalog:
- All folders (empty and populated)
- Folder names (company names)
- Creation dates if available
- Whether folder name matches any entity in BUSINESSES_Master.json
- Whether folder name appears in any other BUSINESSES sub-entities

Output: `Empty_Prospects_Inventory.csv`

Format:
```csv
Folder_Name,Has_JSON,Created_Date,In_Master_JSON,Found_In_Clients,Found_In_Leads,Recommendation
Acme_Corp,No,2025-11-21,No,No,No,DELETE - No data anywhere
Beta_Inc,No,2025-11-20,Yes,No,Yes,KEEP - Referenced in Master + Leads
...
```

#### Step 2: Cross-Reference with Other Entities
Check if empty prospect folders are referenced in:
- `BUSINESSES/BUSINESSES_Master.json` (40 entities)
- `BUSINESSES/CLIENTS/` (299 company folders)
- `BUSINESSES/Leads/` (if exists)
- `BUSINESSES/LeadSources/` (if exists)
- `IMPORTS/2025-11-21_Sales_Nov25/` (recent import data)
- `IMPORTS/2025-11-22_Sales_Import/` (latest import)

If folder name appears anywhere, mark as "KEEP - Has references".
If folder name appears nowhere, mark as "DELETE - No references".

#### Step 3: Analyze Populated Prospects
Examine the 33 prospects that DO have JSON files:
- Extract their schema structure
- Identify required fields
- Note which fields are consistently populated
- Compare to prospect database schema (from user notes)

Output: `Populated_Prospect_Schema_Analysis.md`

Include schema example:
```json
{
  "id": "MEDIUMINT",
  "name": "VARCHAR(100)",
  "position_id": "TINYINT",
  "status_id": "TINYINT",
  "notes": "VARCHAR(500)",
  "tool_id": "SMALLINT",
  "prospect_company": {
    "id": "MEDIUMINT",
    "name": "VARCHAR(100)",
    "website": "VARCHAR(255)",
    "city_id": "SMALLINT",
    "country_id": "TINYINT",
    "affiliate_id": "TINYINT",
    "tool_id": "SMALLINT",
    "manager_id": "SMALLINT",
    "created_by": "SMALLINT",
    "created_at": "DATETIME"
  },
  ...
}
```

#### Step 4: Generate Recommendations
Based on analysis, categorize all 298 empty folders:

**Category A: DELETE** - No references anywhere, likely import artifacts
**Category B: KEEP - Populate from Imports** - Referenced in recent imports
**Category C: KEEP - Populate from CRM** - Waiting on CRM data from Kolya/Olya
**Category D: KEEP - Placeholder** - Intentionally created for future use

For each category, provide:
- Count of folders
- Example folder names
- Recommended action
- Data source for population (if keeping)

Output: `Empty_Folders_Recommendation_Report.md`

#### Step 5: Create Population Template (for folders to keep)
For folders recommended to KEEP, create:
- JSON template file: `Prospect_Template_v2.json`
- CSV import template: `Prospect_Import_Template.csv`
- Mapping document: `Prospect_Field_Mapping.md` (maps import data fields to JSON schema)

These templates will be used in Phase 2 when populating.

### Input Files
```
BUSINESSES/Prospects/ (all 331 folders: 33 with JSON + 298 empty)
BUSINESSES/BUSINESSES_Master.json
BUSINESSES/CLIENTS/ (299 company folders)
BUSINESSES/schemas/ (if prospect schema exists)
IMPORTS/2025-11-21_Sales_Nov25/entities_extracted.csv
IMPORTS/2025-11-22_Sales_Import/
```

### Output Files
```
REPORTS/2025-11-22/System_Rebuild/
├── Phase_1C_Empty_Prospects_Inventory.csv
├── Phase_1C_Populated_Prospect_Schema_Analysis.md
├── Phase_1C_Empty_Folders_Recommendation_Report.md
└── Phase_1C_Cross_Reference_Matrix.csv

BUSINESSES/Prospects/
├── Prospect_Template_v2.json (for Phase 2 use)
├── Prospect_Import_Template.csv (for Phase 2 use)
└── Prospect_Field_Mapping.md (for Phase 2 use)
```

### Success Criteria
- [ ] All 298 empty folders inventoried with creation dates
- [ ] Cross-reference check complete across 5+ entity types
- [ ] Schema analysis covers all 33 populated prospects
- [ ] Clear recommendation (DELETE or KEEP) for each empty folder
- [ ] Categorization by data source (Imports/CRM/Placeholder)
- [ ] Templates created for Phase 2 population
- [ ] Report ready for manual review and decision

### Database Schema Reference (from user notes)
```sql
-- prospects table
prospects.id MEDIUMINT
prospects.name VARCHAR(100)
prospects.position_id TINYINT
prospects.status_id TINYINT
prospects.notes VARCHAR(500)
prospects.tool_id SMALLINT

-- prospect_companies table
prospect_companies.id MEDIUMINT
prospect_companies.name VARCHAR(100)
prospect_companies.website VARCHAR(255)
prospect_companies.city_id SMALLINT
prospect_companies.country_id TINYINT
prospect_companies.affiliate_id TINYINT
prospect_companies.tool_id SMALLINT
prospect_companies.manager_id SMALLINT
prospect_companies.created_by SMALLINT
prospect_companies.created_at DATETIME

-- junction tables
prospect_prospect_company (prospect_id, prospect_company_id)
prospect_company_industries (prospect_company_id, industry_id)
prospect_company_sub_industries (prospect_company_id, sub_industry_id)
prospect_company_contacts (prospect_company_id, contact_id)

-- communications
prospect_communications (id, prospect_id, prospect_company_id, user_id, account_id, created_at, is_followup, note)
prospect_communication_messages (prospect_communication_id, message_id)
```

Use this schema as reference when analyzing JSON structure vs expected database structure.

---

## 🔗 Cross-Agent Dependencies

### Agent 1A ← → Agent 1B
**No direct dependency** - Can run in parallel
- Agent 1A works on LIBRARIES/Archive/
- Agent 1B works on TASK_MANAGERS/ and LIBRARIES/LBS_003_Tools/
- No file overlap

### Agent 1A ← → Agent 1C
**No direct dependency** - Can run in parallel
- Agent 1A works on LIBRARIES/
- Agent 1C works on BUSINESSES/
- No file overlap

### Agent 1B ← → Agent 1C
**No direct dependency** - Can run in parallel
- Agent 1B works on TASK_MANAGERS/ and LIBRARIES/
- Agent 1C works on BUSINESSES/
- No file overlap

**Result**: All 3 agents can execute simultaneously without conflicts.

---

## 📊 Phase 1 Validation Checklist

After all 3 agents complete, manually review:

### Agent 1A Outputs
- [ ] Review `Phase_1A_Cleanup_Report.md` - verify backup strategy sound
- [ ] Check `Phase_1A_Backup_Inventory.csv` - confirm no unique files lost
- [ ] Verify `ARCHIVE/Libraries_Backup_2025-11-22/Backup_Manifest.csv` is complete
- [ ] Confirm LIBRARIES/Archive/ has zero nested folders deeper than 1 level
- [ ] Approve deletion of nested backups OR request rollback

### Agent 1B Outputs
- [ ] Review `Phase_1B_Duplicate_IDs_Inventory.csv` - verify all 23 duplicates found
- [ ] Check `Phase_1B_ID_Resolution_Report.md` - approve ID reassignments
- [ ] Verify `Phase_1B_Before_After_Comparison.csv` shows exactly 23 changes
- [ ] Spot-check 5 random Task Templates for correct new IDs
- [ ] Spot-check 5 random Tools for correct new IDs
- [ ] Verify cross-references updated (test a few prompt files)
- [ ] Approve ID changes OR request adjustments

### Agent 1C Outputs
- [ ] Review `Phase_1C_Empty_Folders_Recommendation_Report.md`
- [ ] Check categorization (DELETE vs KEEP) for reasonableness
- [ ] Verify cross-reference matrix is complete
- [ ] Review schema analysis against database schema (from user notes)
- [ ] Make decision: Which folders to DELETE? Which to KEEP?
- [ ] Review templates (Prospect_Template_v2.json) for Phase 2
- [ ] Approve recommendations OR request re-analysis

---

## 🚦 Phase 1 Exit Criteria

Before proceeding to Phase 3/4:

**MUST COMPLETE:**
- [ ] All 3 agents completed successfully
- [ ] All 3 validation checklists reviewed
- [ ] All reports saved to `REPORTS/2025-11-22/System_Rebuild/`
- [ ] Manual decisions made on:
  - [ ] Approve backup deletion (Agent 1A)
  - [ ] Approve ID changes (Agent 1B)
  - [ ] Approve folder DELETE list (Agent 1C)

**METRICS UPDATED:**
- [ ] Nested backup levels: 8 → 0
- [ ] Duplicate IDs: 23 → 0
- [ ] Empty prospect folders: 298 → [decision pending]

**READY FOR NEXT PHASE:**
- [ ] LIBRARIES cleaned and validated
- [ ] TASK_MANAGERS IDs unique and sequential
- [ ] BUSINESSES/Prospects/ ready for Phase 2 population (when data arrives)

---

## 🔑 Key File Paths Reference

### Agent 1A Paths
```
INPUT:
LIBRARIES/Archive/backup_20251119_055410/ (nested 8 levels)
LIBRARIES/README.md

OUTPUT:
ARCHIVE/Libraries_Backup_2025-11-22/
REPORTS/2025-11-22/System_Rebuild/Phase_1A_*.{csv,md,txt}
```

### Agent 1B Paths
```
INPUT:
TASK_MANAGERS/TSM-003_Task_Templates/*.json
TASK_MANAGERS/Task_Templates_Master_List.csv
LIBRARIES/LBS_003_Tools/**/*.json
LIBRARIES/LBS_003_Tools/Tools_Master_List.csv
TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv
PROMPTS/**/* (for cross-references)

OUTPUT:
[Updated JSON files with new IDs]
TASK_MANAGERS/Task_Templates_Master_List.csv (regenerated)
LIBRARIES/LBS_003_Tools/Tools_Master_List.csv (regenerated)
TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv (regenerated)
REPORTS/2025-11-22/System_Rebuild/Phase_1B_*.{csv,md}
```

### Agent 1C Paths
```
INPUT:
BUSINESSES/Prospects/ (331 folders total)
BUSINESSES/BUSINESSES_Master.json
BUSINESSES/CLIENTS/ (299 folders)
BUSINESSES/schemas/
IMPORTS/2025-11-21_Sales_Nov25/
IMPORTS/2025-11-22_Sales_Import/

OUTPUT:
BUSINESSES/Prospects/Prospect_Template_v2.json
BUSINESSES/Prospects/Prospect_Import_Template.csv
BUSINESSES/Prospects/Prospect_Field_Mapping.md
REPORTS/2025-11-22/System_Rebuild/Phase_1C_*.{csv,md}
```

---

## 📝 Prompts Reference

No specific prompts needed for Phase 1 (cleanup operations).

Phase 1 is primarily data analysis and file operations, not content generation.

Relevant prompts will be used in later phases:
- Phase 2: Prospect population prompts
- Phase 3: Research prompts
- Phase 4: Deep Research prompts

---

## 🎯 Success Metrics

| Metric | Before Phase 1 | After Phase 1 | Target |
|--------|----------------|---------------|--------|
| Nested backup levels | 8 | 0 | ✅ 0 |
| Duplicate IDs | 23 | 0 | ✅ 0 |
| Empty prospect folders | 298 | [TBD] | ⚠️ Decision pending |
| Invalid JSON files | 1 | 1 | ⏭️ Phase 5 |
| Backup storage size | ~[TBD] MB | ~[TBD] MB | ⬇️ Reduced |

---

## 🔄 Rollback Plan

If Phase 1 causes issues:

### Agent 1A Rollback
1. Restore from `ARCHIVE/Libraries_Backup_2025-11-22/Original_Backups/`
2. Copy back to `LIBRARIES/Archive/`
3. Verify file counts match Backup_Manifest.csv

### Agent 1B Rollback
1. Revert JSON files to git commit before Phase 1 (if version controlled)
2. Restore master CSVs from `REPORTS/2025-11-21/` (previous day's versions)
3. Re-run cross-reference scan to verify

### Agent 1C Rollback
No rollback needed - Agent 1C only generates reports, doesn't modify files.

---

**END OF PHASE 1 CONTEXT**

**Next Steps:**
1. Review this context document
2. Confirm agent instructions are clear
3. Execute 3 agents simultaneously
4. Review validation checklists
5. Proceed to Phase 3/4 after approval
