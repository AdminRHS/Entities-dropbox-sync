# LIBRARIES Folder Migration Project Plan

**Project:** LIBRARIES Folder Structure Migration
**Created:** 2025-11-19
**Completed:** 2025-11-22
**Status:** ✅ **COMPLETE**
**Purpose:** Migrate LIBRARIES folder structure with Responsibilities as core layer and Skills moved to TALENTS

---

## Project Overview

### Objective
Reorganize the LIBRARIES folder structure to use a consistent `LBS_XXX_Name` naming convention, improving maintainability, clarity, and scalability.

### Background
The current LIBRARIES folder structure uses inconsistent naming:
- Mixed plural/singular: `Tools` vs `Professions` vs `Skills`
- Mixed case: `DEPARTMENTS` (all caps) vs `Tools` (Title Case)
- Mixed separators: `AI_Tools` (underscore) vs `Social Media Platforms` (spaces)
- Unclear organization: `Responsibilities` folder contains Actions, Objects, and Parameters

### Proposed Solution
Implement a numbered prefix system (`LBS_XXX_Name`) where:
- `LBS` = LIBRARIES prefix
- `XXX` = Sequential number (001-009)
- `Name` = Folder name (Title Case)

---

## Architecture

### Folder Structure

```
LIBRARIES/
├── Responsibilities/              # CORE LAYER (Actions + Objects + Parameters)
│   ├── Actions/                  # Standardized action verbs (429 actions)
│   ├── Objects/                  # Business objects and deliverables (50+)
│   ├── Parameters/               # Configuration parameters (200+)
│   ├── Core/                     # Master responsibilities (193)
│   ├── By_Department/            # Department-specific responsibilities
│   └── Integration/              # Cross-reference mappings
├── LBS_003_Tools/                # Software platforms and services (164 tools)
├── LBS_005_Professions/          # Job roles and profession definitions (17)
├── LBS_006_Departments/          # Organizational units (9)
├── Taxonomy/                     # Documentation and master lists
└── Archive/                      # Archived and legacy files

TALENTS/ (Skills migrated here on 2025-11-22)
└── Skills/                       # Responsibility + Tool combinations (28 skills)
    ├── Master/
    ├── By_Department/
    ├── By_Profession/
    ├── By_Difficulty/
    └── By_Tool/
```

### Path Mapping

| Old Path | New Path | Notes |
|----------|----------|-------|
| `LIBRARIES/LBS_001_Actions/` | `LIBRARIES/Responsibilities/Actions/` | ✅ Moved into Responsibilities |
| `LIBRARIES/LBS_002_Objects/` | `LIBRARIES/Responsibilities/Objects/` | ✅ Moved into Responsibilities |
| `LIBRARIES/LBS_003_Tools/` | `LIBRARIES/LBS_003_Tools/` | ✅ Unchanged |
| `LIBRARIES/LBS_004_Skills/` | `TALENTS/Skills/` | ✅ Migrated to TALENTS ecosystem |
| `LIBRARIES/LBS_005_Professions/` | `LIBRARIES/LBS_005_Professions/` | ✅ Unchanged |
| `LIBRARIES/LBS_006_Departments/` | `LIBRARIES/LBS_006_Departments/` | ✅ Unchanged |
| `LIBRARIES/LBS_007_Parameters/` | `LIBRARIES/Responsibilities/Parameters/` | ✅ Moved into Responsibilities |
| `LIBRARIES/LBS_008_Taxonomy/` | `LIBRARIES/Taxonomy/` | ✅ ID prefix removed |
| `LIBRARIES/LBS_009_Archive/` | `LIBRARIES/Archive/` | ✅ ID prefix removed |

---

## Implementation Strategy

### Phase 1: Preparation ✅
- [x] Create folder naming proposal document
- [x] Document current structure and issues
- [x] Define new folder structure
- [x] Create path mapping reference
- [x] Identify all files requiring updates

### Phase 2: Script Development ✅ (In Progress)
- [x] Create migration script (`migrate_folder_paths.py`)
- [ ] Test script on sample files
- [ ] Validate path mappings
- [ ] Create backup mechanism
- [ ] Add dry-run mode

### Phase 3: Reference Updates
- [ ] Run migration script in dry-run mode
- [ ] Review changes report
- [ ] Run migration script (live mode with backup)
- [ ] Verify all references updated
- [ ] Update master list generation script
- [ ] Update CSV master lists

### Phase 4: File Migration
- [ ] Create new folder structure
- [ ] Move files to new locations
- [ ] Verify file integrity
- [ ] Update file permissions if needed

### Phase 5: Documentation Updates
- [ ] Update README.md files
- [ ] Update ID_AND_NAME_CONVENTIONS.md
- [ ] Update all documentation references
- [ ] Update cross-references in other entities

### Phase 6: Archive & Cleanup
- [ ] Archive old folder structure to `LBS_009_Archive/Old_Structure/`
- [ ] Remove old references
- [ ] Final verification
- [ ] Update migration status

---

## Technical Details

### Migration Script Features

**Script:** `migrate_folder_paths.py`

**Capabilities:**
- Recursively processes all text files (`.md`, `.py`, `.json`, `.csv`, `.txt`, `.yaml`, etc.)
- Updates path references in content
- Handles multiple path formats (absolute, relative, with/without LIBRARIES prefix)
- Creates detailed migration report (JSON + Markdown)
- Supports dry-run mode for testing
- Creates backups before modification
- Skips binary files and system directories

**Path Patterns Handled:**
- Full paths: `LIBRARIES/LBS_003_Tools/`
- Relative paths: `LBS_003_Tools/`
- File-specific paths: `LBS_003_Tools/By_Category/AI/Claude.json`
- Subfolder paths: `TALENTS/Skills/Master/all_skills.json` (migrated to TALENTS)

### Files to Process

**Documentation Files:**
- `README.md` - Main documentation
- `ACTIONS_README.md` - Actions documentation
- `OBJECTS_README.md` - Objects documentation
- `ID_AND_NAME_CONVENTIONS.md` - Naming conventions
- All subfolder README files

**Scripts:**
- `Taxonomy/generate_master_list.py` - Master list generator
- `Responsibilities/create_parameter_mapping.py` - Parameter mapping
- `Responsibilities/validate_ecosystem.py` - Validation script
- `Responsibilities/migrate_references.py` - Reference migration

**Data Files:**
- `Taxonomy/Libraries_Master_List.csv` - Master list CSV
- `Taxonomy/Libraries_Master_List_2025-12-26.csv` - Dated master list
- `Taxonomy/Libraries_Migration_Map.json` - Migration map
- All JSON files with path references

---

## Risk Management

### Risks Identified

1. **Broken References**
   - Risk: Some references may not be caught by script
   - Mitigation: Comprehensive path mapping, manual review, testing

2. **File Corruption**
   - Risk: Script may corrupt files during update
   - Mitigation: Backup before modification, dry-run testing

3. **Incomplete Migration**
   - Risk: Some files may be missed
   - Mitigation: Recursive processing, comprehensive file extension list

4. **Script Errors**
   - Risk: Script may fail on certain file types
   - Mitigation: Error handling, logging, skip problematic files

### Rollback Plan

1. Restore from backup directory (created automatically)
2. Revert changes using Git (if version controlled)
3. Manual restoration from migration report

---

## Success Criteria

### Completion Criteria

- [ ] All path references updated in documentation
- [ ] All path references updated in scripts
- [ ] All path references updated in data files
- [ ] New folder structure created
- [ ] Files moved to new locations
- [ ] Master list generation script updated
- [ ] Master list CSV files updated
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Old structure archived

### Validation

- Run `generate_master_list.py` and verify paths are correct
- Search codebase for old path patterns (should find none)
- Verify all files accessible at new paths
- Check migration report for completeness

---

## Timeline

**Estimated Duration:** 2-3 days

- **Day 1:** Script development and testing
- **Day 2:** Reference updates and file migration
- **Day 3:** Documentation updates and verification

---

## Related Documents

- [FOLDER_NAMING_PROPOSAL.md](FOLDER_NAMING_PROPOSAL.md) - Detailed proposal
- [FOLDER_MIGRATION_NOTE_2025-12-26.md](FOLDER_MIGRATION_NOTE_2025-12-26.md) - Migration notes
- [FILES_TO_UPDATE.md](FILES_TO_UPDATE.md) - Files requiring updates
- [LBS_FOLDER_MASTER.csv](LBS_FOLDER_MASTER.csv) - Folder master list
- [ID_AND_NAME_CONVENTIONS.md](ID_AND_NAME_CONVENTIONS.md) - Naming conventions

---

**Last Updated:** 2025-12-26  
**Next Review:** After Phase 2 completion

