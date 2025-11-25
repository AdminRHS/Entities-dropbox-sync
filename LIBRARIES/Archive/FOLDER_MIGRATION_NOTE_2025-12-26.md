# LIBRARIES Folder Structure Migration

**Date:** 2025-12-26  
**Status:** Proposed - Awaiting Approval  
**Purpose:** Document folder structure changes from old naming to new `LBS_XXX_Name` format

---

## Migration Overview

The LIBRARIES folder structure is being updated to use a consistent `LBS_XXX_Name` naming convention for all root-level folders.

---

## Old vs New Folder Mapping

| Old Folder Name | New Folder Name | Notes |
|----------------|-----------------|-------|
| `Responsibilities/Actions/` | `Responsibilities/Actions/` | Actions split from Responsibilities |
| `Responsibilities/Objects/` | `Responsibilities/Objects/` | Objects split from Responsibilities |
| `LBS_003_Tools/` | `LBS_003_LBS_003_Tools/` | Tools folder renamed |
| `../TALENTS/Skills/` | `LBS_004_../TALENTS/Skills/` | Skills folder renamed |
| `LBS_005_Professions/` | `LBS_005_LBS_005_Professions/` | Professions folder renamed |
| `LBS_006_Departments/` | `LBS_006_Departments/` | Departments folder renamed |
| `Responsibilities/Parameters/` | `Responsibilities/Parameters/` | Parameters split from Responsibilities |
| `Taxonomy/` | `LBS_008_Taxonomy/` | Taxonomy folder renamed |
| `Archive/` | `LBS_009_Archive/` | Archive folder renamed |

---

## Subfolder Changes

### Actions
- `Responsibilities/Actions/` → `Responsibilities/Actions/`
- `Actions_Master.json` → `Master/actions_master.json`
- `Video_Generation_Actions.json` → `By_Domain/video_generation_actions.json`
- `Data_Operations/` → `Data_Operations/`

### Objects
- `Responsibilities/Objects/` → `Responsibilities/Objects/`
- Files organized under `By_Domain/` with subfolders by domain type

### Tools
- `LBS_003_LBS_003_Tools/By_Category/AI/` → `LBS_003_LBS_003_Tools/By_Category/AI/`
- `LBS_003_LBS_003_Tools/By_Category/Development/` → `LBS_003_LBS_003_Tools/By_Category/Development/`
- `LBS_003_Tools/Databases/` → `LBS_003_LBS_003_Tools/By_Category/Development/Databases/`
- `LBS_003_LBS_003_Tools/By_Category/Social_Media/` → `LBS_003_LBS_003_Tools/By_Category/Social_Media/`

### Skills
- `LBS_004_../TALENTS/Skills/Master/` → `LBS_004_LBS_004_../TALENTS/Skills/Master/`
- `LBS_004_../TALENTS/Skills/By_Department/` → `LBS_004_LBS_004_../TALENTS/Skills/By_Department/`
- `LBS_004_../TALENTS/Skills/By_Profession/` → `LBS_004_LBS_004_../TALENTS/Skills/By_Profession/`

### Professions
- `LBS_005_Professions/` → `LBS_005_LBS_005_Professions/`
- `professions.json` → `Master/professions.json`
- Individual files → `Individual/`

### Departments
- `LBS_006_Departments/` → `LBS_006_Departments/`
- `departments.json` → `Master/departments.json`
- `By_Department/` → `By_Department/`

### Parameters
- `Responsibilities/Parameters/` → `Responsibilities/Parameters/`
- `organized_by_profession/` → `By_Profession/`
- `organized_by_department/` → `By_Department/`

### Taxonomy
- `Taxonomy/` → `LBS_008_Taxonomy/`
- Files organized into `Master_Lists/`, `Documentation/`, `Scripts/`, `Migrations/`

---

## Files Requiring Updates

### Documentation Files
- [ ] `README.md` - Update all folder path references
- [ ] `ACTIONS_README.md` - Update path references
- [ ] `OBJECTS_README.md` - Update path references
- [ ] `ID_AND_NAME_CONVENTIONS.md` - Update folder naming examples
- [ ] `../TALENTS/Skills/README.md` - Update path references
- [ ] `LBS_003_Tools/README.md` - Update path references
- [ ] `LBS_005_Professions/README.md` - Update path references
- [ ] `LBS_006_Departments/README.md` - Update path references
- [ ] `Responsibilities/README.md` - Update or archive (split into 3 folders)

### Scripts
- [ ] `Taxonomy/generate_master_list.py` - Update all folder paths
- [ ] `Responsibilities/create_parameter_mapping.py` - Update paths
- [ ] `Responsibilities/validate_ecosystem.py` - Update paths
- [ ] `Responsibilities/migrate_references.py` - Update paths

### Configuration Files
- [ ] `Taxonomy/Libraries_Master_List.csv` - Update File_Path column
- [ ] `Taxonomy/Libraries_Migration_Map.json` - Update paths

---

## Migration Steps

1. **Create new folder structure** with `LBS_XXX_Name` format
2. **Move files** to new locations following the mapping table
3. **Update all documentation** with new paths
4. **Update scripts** to use new paths
5. **Update master lists** and indexes
6. **Test** all scripts and references
7. **Archive** old folder structure to `LBS_009_Archive/`

---

## Backward Compatibility

During migration period:
- Old folder structure will remain in `LBS_009_Archive/Old_Structure/`
- Documentation will reference both old and new paths temporarily
- Scripts will be updated to use new paths

---

## Status

- [x] Proposal created
- [ ] Proposal approved
- [ ] New folders created
- [ ] Files migrated
- [ ] Documentation updated
- [ ] Scripts updated
- [ ] Testing completed
- [ ] Old structure archived

---

**See:** `FOLDER_NAMING_PROPOSAL.md` for detailed proposal  
**See:** `FOLDER_STRUCTURE_QUICK_REFERENCE.md` for quick reference


