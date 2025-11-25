# LIBRARIES Folder Naming Proposal

**Document Type:** Architecture Proposal  
**Entity:** LIBRARIES  
**Created:** 2025-12-26  
**Purpose:** Propose renewed folder structure with consistent naming conventions

---

## Current Issues

1. **Inconsistent Naming:**
   - Mixed plural/singular: `Tools` vs `Professions` vs `Skills`
   - Mixed case: `DEPARTMENTS` (all caps) vs `Tools` (Title Case) vs `Skills` (Title Case)
   - Mixed separators: `AI_Tools` (underscore) vs `Social Media Platforms` (space in some contexts)

2. **Redundant Folders:**
   - `Developer_Platforms` vs `Development_Tools`
   - Multiple backup folders with dates

3. **Unclear Organization:**
   - `By_Department`, `By_Profession`, `By_Difficulty` - inconsistent patterns
   - Root-level tool files mixed with categorized folders

4. **Inconsistent Depth:**
   - Some categories have subfolders, others don't
   - `Video Generation` subfolder inside `AI_Tools`

---

## Proposed Naming Convention

### Core Principles

1. **Prefix format: `LBS_XXX_Name`** where:
   - `LBS` = LIBRARIES prefix
   - `XXX` = Sequential number (001, 002, 003, etc.)
   - `Name` = Folder name (Title Case)
2. **Consistent pluralization:** Use plural for collections (Tools, Skills, Professions)
3. **Clear hierarchy:** Maximum 3 levels deep
4. **Department codes:** Use ISO codes where applicable (AI, DEV, VID, SMM, etc.)
5. **Logical grouping:** Group by function, not by type
6. **Subfolders:** Use same prefix pattern or descriptive lowercase names

---

## Proposed Folder Structure

### Root Level

```
LIBRARIES/
├── Responsibilities/Actions/              # Actions (verbs)
├── Responsibilities/Objects/              # Objects (nouns/deliverables)
├── LBS_003_LBS_003_Tools/                # Tools (software/platforms)
├── LBS_004_../TALENTS/Skills/               # Skills (responsibility + tool combinations)
├── LBS_005_LBS_005_Professions/          # Professions (job roles)
├── LBS_006_Departments/          # Departments (organizational units)
├── Responsibilities/Parameters/           # Parameters (configuration variables)
├── LBS_008_Taxonomy/             # Taxonomy documentation and master lists
└── LBS_009_Archive/              # Archived/legacy files
```

**Changes:**
- `Responsibilities` → Split into `Responsibilities/Actions/`, `Responsibilities/Objects/`, `Responsibilities/Parameters/`
- `Tools` → `LBS_003_LBS_003_Tools/`
- `Professions` → `LBS_005_LBS_005_Professions/`
- `Skills` → `LBS_004_../TALENTS/Skills/`
- `DEPARTMENTS` → `LBS_006_Departments/`
- `Taxonomy` → `LBS_008_Taxonomy/`

---

## Detailed Folder Structure

### 1. Actions (`Responsibilities/Actions/`)

```
Responsibilities/Actions/
├── Master/
│   ├── actions_master.json
│   ├── actions_command_verbs.json
│   ├── actions_process_verbs.json
│   └── actions_result_verbs.json
├── By_Domain/
│   └── video_generation_actions.json
├── Data_Operations/
│   ├── data_operations_index.json
│   ├── arbitrage.json
│   ├── bill.json
│   ├── combine.json
│   └── ... (other data operations)
└── Archive/
    └── processes_archived/
```

**Changes:**
- `Responsibilities/Actions/` → `Responsibilities/Actions/`
- `Actions_Master.json` → `Master/actions_master.json`
- `Video_Generation_Actions.json` → `By_Domain/video_generation_actions.json`
- `Data_Operations/` → `Data_Operations/`

---

### 2. Objects (`Responsibilities/Objects/`)

```
Responsibilities/Objects/
├── Master/
│   └── objects_master.json
├── By_Domain/
│   ├── AI_Objects/
│   │   ├── agentic_engineering_objects.json
│   │   ├── ai_automation_objects.json
│   │   └── rag_objects.json
│   ├── Development_Objects/
│   │   └── development_objects.json
│   ├── Design_Objects/
│   │   ├── design_deliverables.json
│   │   ├── interactive_elements.json
│   │   ├── portfolio_deliverables.json
│   │   └── mascot_sets.json
│   ├── Video_Objects/
│   │   ├── video_deliverables.json
│   │   └── video_generation_objects.json
│   ├── Marketing_Objects/
│   │   ├── social_media_deliverables.json
│   │   ├── publishing_deliverables.json
│   │   └── online_academy_lessons.json
│   ├── HR_Objects/
│   │   └── recruitment_objects.json
│   ├── Lead_Generation_Objects/
│   │   └── lead_generation_objects.json
│   └── General_Objects/
│       ├── documents.json
│       └── catalog_documentation.json
└── Metadata/
    ├── object_types.json
    └── object_variants_map.json
```

**Changes:**
- `Responsibilities/Objects/` → `Responsibilities/Objects/`
- Group by domain with subfolders for clarity
- `Design_Deliverables.json` → `By_Domain/Design_Objects/design_deliverables.json`

---

### 3. Tools (`LBS_003_Tools/`)

```
LBS_003_Tools/
├── AI_Tools/                    # Keep original name
│   ├── Claude.json
│   ├── ChatGPT.json
│   ├── Gemini.json
│   └── ...
├── Development_Tools/           # Keep original name
│   ├── Cursor.json
│   ├── VS_Code.json
│   └── ...
├── Automation_Tools/            # Keep original name
│   ├── n8n.json
│   └── Make_com.json
├── Social_Media_Platforms/      # Keep original name
│   ├── LinkedIn.json
│   ├── Twitter.json
│   └── ...
├── Video_Editing_Tools/         # Keep original name
├── Business_Tools/              # Keep original name
├── MCP_Services/                # Keep original name
├── Databases/                   # Keep original name
├── Cloud_Platforms/             # Keep original name
└── ... (other existing subfolders)
```

**Changes:**
- `Tools/` → `LBS_003_Tools/` (root folder renamed only)
- **Internal structure unchanged** - all subfolders keep their original names

---

### 4. Skills (`LBS_004_../TALENTS/Skills/`)

```
LBS_004_../TALENTS/Skills/
├── Master/
│   ├── all_skills.json
│   ├── skills_index.json
│   └── skills_metadata.json
├── By_Department/
│   ├── ai_skills.json
│   ├── dev_skills.json
│   ├── design_skills.json
│   ├── hr_skills.json
│   ├── lg_skills.json
│   ├── sales_skills.json
│   └── video_skills.json
├── By_Profession/
│   ├── ai_engineer.json
│   ├── backend_developer.json
│   ├── designer.json
│   └── ...
├── By_Difficulty/
│   ├── beginner.json
│   ├── intermediate.json
│   └── advanced.json
├── By_Tool/
│   └── ... (tool-specific skill files)
├── Mappings/
│   ├── skill_profession_map.json
│   └── skill_tool_map.json
└── Templates/
    ├── talent_skill_profile.json
    ├── skill_assessment.json
    └── skill_development_plan.json
```

**Changes:**
- `LBS_004_../TALENTS/Skills/Master/` → `LBS_004_LBS_004_../TALENTS/Skills/Master/`
- `LBS_004_../TALENTS/Skills/By_Department/` → `LBS_004_LBS_004_../TALENTS/Skills/By_Department/`
- `LBS_004_../TALENTS/Skills/By_Profession/` → `LBS_004_LBS_004_../TALENTS/Skills/By_Profession/`
- `LBS_004_../TALENTS/Skills/By_Difficulty/` → `LBS_004_LBS_004_../TALENTS/Skills/By_Difficulty/`
- `../TALENTS/Skills/Mappings/` → `LBS_004_../TALENTS/Skills/Mappings/`
- `../TALENTS/Skills/Templates/` → `LBS_004_../TALENTS/Skills/Templates/`

---

### 5. Professions (`LBS_005_LBS_005_Professions/`)

```
LBS_005_LBS_005_Professions/
├── Master/
│   └── professions.json
└── Individual/
    ├── ai_engineer.json
    ├── automation_engineer.json
    ├── backend_developer.json
    ├── designer.json
    └── ...
```

**Changes:**
- `LBS_005_Professions/` → `LBS_005_LBS_005_Professions/`
- `professions.json` → `Master/professions.json`
- Individual profession files → `Individual/`

---

### 6. Departments (`LBS_006_Departments/`)

```
LBS_006_Departments/
├── Master/
│   └── departments.json
└── By_Department/
    ├── AI/
    │   ├── overview.json
    │   ├── structure.json
    │   ├── metrics.json
    │   └── ...
    └── SMM/
        └── ...
```

**Changes:**
- `LBS_006_Departments/` → `LBS_006_Departments/`
- `departments.json` → `Master/departments.json`
- `By_Department/` → `By_Department/`

---

### 7. Parameters (`Responsibilities/Parameters/`)

```
Responsibilities/Parameters/
├── Master/
│   └── parameters.json
├── By_Profession/
│   ├── graphic_designer_parameters.json
│   ├── backend_developer_parameters.json
│   ├── lead_generator_parameters.json
│   └── ...
└── By_Department/
    ├── designers_parameters.json
    ├── developers_parameters.json
    └── ...
```

**Changes:**
- `Responsibilities/Parameters/` → `Responsibilities/Parameters/`
- `organized_by_profession/` → `By_Profession/`
- `organized_by_department/` → `By_Department/`

---

### 8. Taxonomy (`LBS_008_Taxonomy/`)

```
LBS_008_Taxonomy/
├── Master_Lists/
│   ├── libraries_master_list.csv
│   └── libraries_master_list_2025-12-26.csv
├── Documentation/
│   ├── libraries_iso_code_registry.md
│   ├── libraries_hierarchy_tree.md
│   ├── libraries_department_distribution.md
│   └── id_and_name_conventions.md
├── Scripts/
│   └── generate_master_list.py
└── Migrations/
    └── libraries_migration_map.json
```

**Changes:**
- `Taxonomy/` → `LBS_008_Taxonomy/`
- Group master lists, documentation, scripts, and migrations

---

### 9. Archive (`LBS_009_Archive/`)

```
LBS_009_Archive/
├── Legacy_Root_Files/
│   ├── actions.json
│   ├── objects.json
│   └── tools.json
├── Backups/
│   ├── actions_backup_20251118/
│   └── objects_backup_20251118/
└── Deprecated/
    └── ...
```

**Changes:**
- Consolidate all archive/backup folders
- Use consistent naming with dates: `backup_YYYYMMDD/`

---

## Summary of Changes

### Naming Convention Applied

| Old Name | New Name | Reason |
|----------|----------|--------|
| `DEPARTMENTS` | `LBS_006_Departments` | Numbered prefix, Title Case |
| `Tools` | `LBS_003_Tools` | Numbered prefix, Title Case |
| `AI_Tools` | `LBS_003_LBS_003_Tools/By_Category/AI/` | Clearer hierarchy with prefix |
| `Development_Tools` | `LBS_003_LBS_003_Tools/By_Category/Development/` | Consistent structure |
| `By_Department` | `By_Department` | Title Case subfolder |
| `By_Profession` | `By_Profession` | Title Case subfolder |
| `Master` | `Master` | Title Case subfolder |
| `Responsibilities` | Split into `Responsibilities/Actions/`, `Responsibilities/Objects/`, `Responsibilities/Parameters/` | Clearer separation with numbered prefixes |

### Key Improvements

1. **Consistency:** All root folders use `LBS_XXX_Name` format with sequential numbering
2. **Clarity:** Clear hierarchy with maximum 3 levels, numbered prefixes for easy identification
3. **Organization:** Logical grouping by function/domain, Title Case for subfolders
4. **Maintainability:** Numbered prefixes make it easy to reference and order folders
5. **Scalability:** Structure supports growth, new folders follow the same pattern
6. **Professional:** Numbered system provides clear ordering and identification

---

## Migration Plan

1. **Phase 1:** Create new folder structure
2. **Phase 2:** Move files to new locations
3. **Phase 3:** Update all references in code/docs
4. **Phase 4:** Update master list generation script
5. **Phase 5:** Archive old structure

---

## Benefits

1. **Easier Navigation:** Consistent naming makes it easier to find files
2. **Better Organization:** Clear hierarchy reduces confusion
3. **Scalability:** Structure supports adding new categories
4. **Maintainability:** Consistent patterns make maintenance easier
5. **Professional:** Clean, organized structure looks more professional

---

**Status:** Proposal  
**Next Steps:** Review and approval before migration

