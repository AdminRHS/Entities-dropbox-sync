# LIBRARIES Folder Structure - Quick Reference

**Last Updated:** 2025-12-26

---

## Proposed Folder Structure (Simplified)

```
LIBRARIES/
├── Responsibilities/Actions/              # All action verbs
│   ├── Master/
│   ├── By_Domain/
│   └── Data_Operations/
│
├── Responsibilities/Objects/              # All business objects/deliverables
│   ├── Master/
│   ├── By_Domain/
│   └── Metadata/
│
├── LBS_003_LBS_003_Tools/                # All tools/software/platforms
│   ├── Master/
│   └── By_Category/
│       ├── AI/
│       ├── Development/
│       ├── Automation/
│       ├── Design/
│       ├── Video_Editing/
│       ├── Social_Media/
│       ├── Business/
│       └── Integrations/
│
├── LBS_004_../TALENTS/Skills/               # Skills (responsibility + tool)
│   ├── Master/
│   ├── By_Department/
│   ├── By_Profession/
│   ├── By_Difficulty/
│   ├── By_Tool/
│   ├── Mappings/
│   └── Templates/
│
├── LBS_005_LBS_005_Professions/          # Job roles
│   ├── Master/
│   └── Individual/
│
├── LBS_006_Departments/          # Organizational units
│   ├── Master/
│   └── By_Department/
│
├── Responsibilities/Parameters/           # Configuration parameters
│   ├── Master/
│   ├── By_Profession/
│   └── By_Department/
│
├── LBS_008_Taxonomy/             # Documentation & master lists
│   ├── Master_Lists/
│   ├── Documentation/
│   ├── Scripts/
│   └── Migrations/
│
└── LBS_009_Archive/              # Archived/legacy files
    ├── Legacy_Root_Files/
    ├── Backups/
    └── Deprecated/
```

---

## Naming Convention Rules

1. **Root folders:** `LBS_XXX_Name` format where:
   - `LBS` = LIBRARIES prefix
   - `XXX` = Sequential number (001, 002, 003, etc.)
   - `Name` = Folder name in Title Case

2. **Subfolders:** Title Case with underscores
   - ✅ `By_Department/` (not `by_department/`)
   - ✅ `Master/` (not `master/`)
   - ✅ `AI_LBS_003_Tools/` (not `ai_tools/`)
   - ✅ `Video_Generation/` (not `video_generation/`)

3. **Consistent patterns:**
   - `By_*` for organization by attribute (By_Department, By_Profession, By_Difficulty)
   - `Master/` for master/collection files
   - `Individual/` for individual entity files
   - `Metadata/` for supporting data files

---

## Key Mappings

| Current Location | Proposed Location |
|-----------------|-------------------|
| `LBS_003_LBS_003_Tools/By_Category/AI/` | `LBS_003_LBS_003_Tools/By_Category/AI/` |
| `LBS_003_LBS_003_Tools/By_Category/Development/` | `LBS_003_LBS_003_Tools/By_Category/Development/` |
| `LBS_003_Tools/Databases/` | `LBS_003_LBS_003_Tools/By_Category/Development/Databases/` |
| `LBS_003_LBS_003_Tools/By_Category/Social_Media/` | `LBS_003_LBS_003_Tools/By_Category/Social_Media/` |
| `Responsibilities/Actions/` | `Responsibilities/Actions/` |
| `Responsibilities/Objects/` | `Responsibilities/Objects/` |
| `Responsibilities/Parameters/` | `Responsibilities/Parameters/` |
| `LBS_004_../TALENTS/Skills/Master/` | `LBS_004_LBS_004_../TALENTS/Skills/Master/` |
| `LBS_004_../TALENTS/Skills/By_Department/` | `LBS_004_LBS_004_../TALENTS/Skills/By_Department/` |
| `LBS_005_Professions/` | `LBS_005_LBS_005_Professions/Individual/` |
| `LBS_006_Departments/` | `LBS_006_Departments/` |
| `Taxonomy/` | `LBS_008_Taxonomy/` |

---

## Benefits

✅ **Consistent:** All root folders use `LBS_XXX_Name` format  
✅ **Clear:** Numbered prefixes provide easy identification and ordering  
✅ **Scalable:** Easy to add new categories following the same pattern  
✅ **Maintainable:** Predictable structure with Title Case subfolders  
✅ **Professional:** Numbered system looks organized and systematic  

---

**See:** `FOLDER_NAMING_PROPOSAL.md` for detailed proposal

