# LIBRARIES/DEPARTMENTS/PROMPTS References Update Summary

**Generated:** 2025-11-16  
**Total References Found:** 50  
**Files Affected:** 24

## Priority Categories

### 🔴 HIGH PRIORITY - Active Files (Need Immediate Update)

#### 1. **PROMPTS_INDEX.json** (3 references)
- **Location:** `TASK_MANAGERS\PROMPTS\PROMPTS_INDEX.json`
- **Issue:** Metadata still references `LIBRARIES/DEPARTMENTS/PROMPTS`
- **Action:** Update `migration_info.current_location` and `entity_type`/`sub_entity` fields

#### 2. **LIBRARIES\README.md** (4 references)
- **Location:** `ENTITIES\LIBRARIES\README.md`
- **Issue:** Documentation still references `LIBRARIES/DEPARTMENTS/_SHARED/Prompts`
- **Action:** Update all path references to `TASK_MANAGERS/PROMPTS`

#### 3. **TASK_MANAGERS\Reports\Phase_9_Completion_Report.md** (4 references)
- **Location:** `TASK_MANAGERS\Reports\Phase_9_Completion_Report.md`
- **Issue:** Relative links point to old location
- **Action:** Update relative paths from `../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` to `../PROMPTS/`

#### 4. **Task Templates** (Multiple JSON files - 8 references total)
- **Locations:**
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-001.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-002.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-003.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-004.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-005.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-006.json`
  - `TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-RES-001.json`
- **Issue:** JSON files reference old prompt paths
- **Action:** Update prompt path references in JSON

#### 5. **Project Files** (Multiple files - 6 references)
- **Locations:**
  - `TASK_MANAGERS\Projects\PROJ-AI-NMP-001\README.md`
  - `TASK_MANAGERS\Projects\PROJ-AI-NMP-001\project_instance.json`
  - `TASK_MANAGERS\Projects\PROJ-AI-NMP-001\Milestones\*.json`
  - `TASK_MANAGERS\Projects\PROJ-AI-NMP-001\Logs\*.md`
- **Issue:** Project documentation references old paths
- **Action:** Update all project references

#### 6. **PROMPTS Internal Files** (3 references)
- **Locations:**
  - `TASK_MANAGERS\PROMPTS\System_Analysis\00_MAIN_Ecosystem_Analysis_Overview.md`
  - `TASK_MANAGERS\PROMPTS\System_Analysis\01_Milestone_Data_Inventory.md`
  - `TASK_MANAGERS\PROMPTS\System_Analysis\README.md`
  - `TASK_MANAGERS\PROMPTS\Operational_Workflows\PROMPT_Document_Finished_Project.md`
- **Issue:** Internal documentation references old location
- **Action:** Update internal references

### 🟡 MEDIUM PRIORITY - Documentation Files

#### 7. **LIBRARIES\DEPARTMENTS\README_SHARED_RESOURCES.md** (1 reference)
- **Location:** `ENTITIES\LIBRARIES\DEPARTMENTS\README_SHARED_RESOURCES.md`
- **Action:** Update documentation to reflect new location

#### 8. **ACCOUNTS\JobSites\JobSites_Processing_Prompt.md** (2 references)
- **Location:** `ENTITIES\ACCOUNTS\JobSites\JobSites_Processing_Prompt.md`
- **Action:** Update prompt path references

### 🟢 LOW PRIORITY - Archive/Historical Files (May Leave As-Is)

#### 9. **Archive Files** (6 references)
- **Locations:**
  - `LIBRARIES\DEPARTMENTS\Archive\README.md`
  - `LIBRARIES\DEPARTMENTS\Archive\Prompts_Archive\Integration_Plans\*.md`
  - `LIBRARIES\DEPARTMENTS\Archive\Prompts_Archive\Session_Logs\*.md`
- **Note:** These are historical/archive files. Consider leaving as-is for historical accuracy, or add a note about the migration.

### ⚪ INFORMATIONAL - Scripts (No Action Needed)

#### 10. **Migration Scripts** (12 references)
- **Locations:**
  - `Migrate_Prompts_Phase4-7_Helper.bat` (6 refs - these are intentional, scanning for old paths)
  - `Update_All_References.ps1` (6 refs - script comments/documentation)
- **Note:** These references are intentional - scripts are designed to find/update old paths.

## Recommended Update Pattern

### Path Replacements:
- `LIBRARIES/DEPARTMENTS/PROMPTS` → `TASK_MANAGERS/PROMPTS`
- `LIBRARIES/DEPARTMENTS/PROMPTS/` → `TASK_MANAGERS/PROMPTS/`
- `LIBRARIES\DEPARTMENTS\_SHARED\Prompts` → `TASK_MANAGERS\PROMPTS`
- `LIBRARIES/DEPARTMENTS/_SHARED/Prompts` → `TASK_MANAGERS/PROMPTS`
- `Entities/LIBRARIES/DEPARTMENTS/PROMPTS` → `Entities/TASK_MANAGERS/PROMPTS`
- `../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` → `../PROMPTS/` (relative paths)

### JSON Updates:
- `"current_location": "Entities/LIBRARIES/DEPARTMENTS/PROMPTS/"` → `"current_location": "Entities/TASK_MANAGERS/PROMPTS/"`
- `"entity_type": "DEPARTMENTS"` → `"entity_type": "TASK_MANAGERS"`
- `"sub_entity": "PROMPTS"` → Keep as-is (still correct)

## Next Steps

1. **Update PROMPTS_INDEX.json** - Critical metadata file
2. **Update LIBRARIES\README.md** - Main documentation
3. **Update Task Templates** - Active workflow files
4. **Update Project Files** - Active project references
5. **Update PROMPTS Internal Files** - Self-documentation
6. **Update Report Files** - Documentation accuracy

## Full Report

See `DEPARTMENTS_PROMPTS_References_Report.txt` for complete line-by-line details.

