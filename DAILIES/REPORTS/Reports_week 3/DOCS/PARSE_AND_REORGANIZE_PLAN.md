# Reports Parsing and Reorganization Plan

**Created:** 2025-11-17  
**Purpose:** Plan for parsing and reorganizing Reports content into Analytics folder structure  
**Status:** Planning Phase

---

## 📋 Overview

This document outlines the plan to parse and reorganize content from `ANALYTICS/REPORTS/System_Analysis/` into the appropriate Analytics subfolders, maintaining consistency with existing structure and improving discoverability.

---

## 🎯 Objectives

1. **Organize Reports by Project/Milestone:** Link reports to their corresponding projects and milestones
2. **Consolidate Milestone Data:** Ensure all milestone JSON files are in `Milestones/` folder
3. **Preserve Project Context:** Maintain project instance data in `Projects/` folder
4. **Organize Scripts:** Create a dedicated location for analysis scripts
5. **Structure Data Files:** Organize JSON/CSV data files logically
6. **Maintain Traceability:** Keep clear links between reports, data, and milestones

---

## 📊 Current State Analysis

### Reports Structure (Source)
```
ANALYTICS/REPORTS/System_Analysis/
├── Milestone_01_Data_Inventory/
│   ├── file_distribution.csv
│   ├── file_distribution.json
│   ├── file_sizes.json
│   ├── folder_structure.json
│   ├── folder_structure.txt
│   ├── milestone_01_summary.json
│   └── REP-001_File_Inventory_Report.md
├── Milestone_02_Schema_Naming/
│   ├── field_usage_stats.json
│   ├── milestone_02_summary.json
│   ├── naming_patterns.json
│   ├── naming_violations.json
│   ├── REP-002_Naming_Convention_Audit.md
│   ├── schema_violations.json
│   ├── version_inventory.json
│   └── version_issues.json
├── Milestone_03_Content_Analysis/
│   ├── extracted_entity_ids.json
│   ├── json_field_names.json
│   ├── markdown_headings.json
│   ├── milestone_03_summary.json
│   ├── python_variables.json
│   ├── redundant_terms_full.json
│   ├── REP-006_terminology_standards.json
│   └── terminology_dictionary.json
├── Milestone_04_Relationship_Validation/
│   ├── broken_references.json
│   ├── index_files.json
│   ├── milestone_04_summary.json
│   ├── reference_map.json
│   └── (milestone_04_relationships.py - at parent level)
├── Milestone_05_Synthesis/
│   └── (empty)
├── milestone_01_inventory.py
├── milestone_02_schema_naming.py
├── milestone_03_terminology.py
├── milestone_04_relationships.py
├── Milestones_02_03_Summary.md
├── REP-003_Schema_Validation_Report.md
├── REP-007_Cross_Reference_Validation.md
├── REP-009_Architecture_Documentation.md
├── REP-010_Terminology_Consolidation.md
├── REP-011_Action_Items_Tracker.csv
└── REP-012_Executive_Summary.md
```

### Analytics Structure (Target)
```
ANALYTICS/
├── Milestones/              # Central milestone tracking (already exists)
│   ├── MIL-001_Data_Inventory.json
│   ├── MIL-002_Schema_Naming.json
│   ├── MIL-003_Content_Analysis.json
│   ├── MIL-004_Relationship_Validation.json
│   └── MIL-005_Synthesis.json
├── Projects/                # Project instances (already exists)
│   └── PROJ-001_ENTITIES_Analysis/
│       ├── README.md
│       ├── Session_Summary.md
│       └── Logs/
├── REPORTS/                 # Reports (to be reorganized)
├── Scripts/                 # Analysis scripts (NEW - to be created)
└── Data/                    # Analysis data files (NEW - to be created)
```

---

## 🔄 Reorganization Strategy

### Phase 1: Create New Folders

**Action:** Create supporting folder structure
- `ANALYTICS/Scripts/` - For Python analysis scripts
- `ANALYTICS/Data/` - For JSON/CSV data files organized by project/milestone
- `ANALYTICS/Data/PROJ-001/` - Project-specific data folder

**Rationale:** Separates scripts and data from reports, improving organization

---

### Phase 2: Move and Organize Scripts

**Source:** `REPORTS/System_Analysis/*.py`  
**Target:** `ANALYTICS/Scripts/PROJ-001/`

**Files to Move:**
- `milestone_01_inventory.py` → `Scripts/PROJ-001/milestone_01_inventory.py`
- `milestone_02_schema_naming.py` → `Scripts/PROJ-001/milestone_02_schema_naming.py`
- `milestone_03_terminology.py` → `Scripts/PROJ-001/milestone_03_terminology.py`
- `milestone_04_relationships.py` → `Scripts/PROJ-001/milestone_04_relationships.py`

**Action:** Create `Scripts/PROJ-001/` folder and move all Python scripts

**Rationale:** 
- Scripts are reusable analysis tools, not reports
- Grouping by project maintains context
- Enables version control and reuse

---

### Phase 3: Organize Data Files

**Source:** `REPORTS/System_Analysis/Milestone_*/`  
**Target:** `ANALYTICS/Data/PROJ-001/MIL-00X/`

**Structure:**
```
ANALYTICS/Data/PROJ-001/
├── MIL-001_Data_Inventory/
│   ├── file_distribution.csv
│   ├── file_distribution.json
│   ├── file_sizes.json
│   ├── folder_structure.json
│   ├── folder_structure.txt
│   └── milestone_01_summary.json
├── MIL-002_Schema_Naming/
│   ├── field_usage_stats.json
│   ├── naming_patterns.json
│   ├── naming_violations.json
│   ├── schema_violations.json
│   ├── version_inventory.json
│   ├── version_issues.json
│   └── milestone_02_summary.json
├── MIL-003_Content_Analysis/
│   ├── extracted_entity_ids.json
│   ├── json_field_names.json
│   ├── markdown_headings.json
│   ├── python_variables.json
│   ├── redundant_terms_full.json
│   ├── terminology_dictionary.json
│   └── milestone_03_summary.json
├── MIL-004_Relationship_Validation/
│   ├── broken_references.json
│   ├── index_files.json
│   ├── reference_map.json
│   └── milestone_04_summary.json
└── MIL-005_Synthesis/
    └── (empty - no data files)
```

**Action:** 
1. Create `Data/PROJ-001/` folder structure
2. Move all JSON/CSV/TXT files from milestone folders
3. Keep milestone summary JSON files here (they're data, not tracking)

**Rationale:**
- Data files are separate from milestone tracking files
- Organizing by project and milestone maintains context
- Makes data files discoverable and reusable

---

### Phase 4: Reorganize Reports

**Source:** `REPORTS/System_Analysis/`  
**Target:** `ANALYTICS/REPORTS/PROJ-001/`

**Structure:**
```
ANALYTICS/REPORTS/PROJ-001/
├── REP-001_File_Inventory_Report.md          (from Milestone_01/)
├── REP-002_Naming_Convention_Audit.md         (from Milestone_02/)
├── REP-003_Schema_Validation_Report.md        (from System_Analysis/)
├── REP-006_terminology_standards.json         (from Milestone_03/)
├── REP-007_Cross_Reference_Validation.md      (from System_Analysis/)
├── REP-009_Architecture_Documentation.md      (from System_Analysis/)
├── REP-010_Terminology_Consolidation.md       (from System_Analysis/)
├── REP-011_Action_Items_Tracker.csv           (from System_Analysis/)
├── REP-012_Executive_Summary.md               (from System_Analysis/)
└── Milestones_02_03_Summary.md                (from System_Analysis/)
```

**Action:**
1. Create `REPORTS/PROJ-001/` folder
2. Move all `.md` report files to this folder
3. Move `REP-011_Action_Items_Tracker.csv` to this folder
4. Flatten structure (remove milestone subfolders from reports)

**Rationale:**
- Reports are deliverables, not organized by milestone
- Grouping by project maintains context
- Easier to find all reports for a project
- Reports reference milestones via IDs, so folder structure not needed

---

### Phase 5: Verify Milestone Tracking Files

**Check:** Ensure milestone JSON files exist in `ANALYTICS/Milestones/`

**Files Expected:**
- `MIL-001_Data_Inventory.json` ✅ (exists)
- `MIL-002_Schema_Naming.json` ✅ (exists)
- `MIL-003_Content_Analysis.json` ✅ (exists)
- `MIL-004_Relationship_Validation.json` ✅ (exists)
- `MIL-005_Synthesis.json` ✅ (exists)

**Action:** Verify all milestone tracking files are present and up-to-date

**Rationale:** Milestone tracking files in `Milestones/` are the source of truth for milestone status

---

### Phase 6: Update Project Instance

**Target:** `ANALYTICS/Projects/PROJ-001_ENTITIES_Analysis/`

**Action:** 
1. Update `README.md` with new file locations
2. Add references to:
   - Scripts location: `Scripts/PROJ-001/`
   - Data location: `Data/PROJ-001/`
   - Reports location: `REPORTS/PROJ-001/`

**Rationale:** Maintains traceability and helps users find related files

---

## 📁 Final Structure

After reorganization:

```
ANALYTICS/
├── Milestones/                              # Milestone tracking (central)
│   ├── MIL-001_Data_Inventory.json
│   ├── MIL-002_Schema_Naming.json
│   ├── MIL-003_Content_Analysis.json
│   ├── MIL-004_Relationship_Validation.json
│   └── MIL-005_Synthesis.json
│
├── Projects/                                 # Project instances
│   └── PROJ-001_ENTITIES_Analysis/
│       ├── README.md                         # Updated with new paths
│       ├── Session_Summary.md
│       └── Logs/
│
├── Scripts/                                  # Analysis scripts (NEW)
│   └── PROJ-001/
│       ├── milestone_01_inventory.py
│       ├── milestone_02_schema_naming.py
│       ├── milestone_03_terminology.py
│       └── milestone_04_relationships.py
│
├── Data/                                     # Analysis data files (NEW)
│   └── PROJ-001/
│       ├── MIL-001_Data_Inventory/
│       │   ├── file_distribution.csv
│       │   ├── file_distribution.json
│       │   ├── file_sizes.json
│       │   ├── folder_structure.json
│       │   ├── folder_structure.txt
│       │   └── milestone_01_summary.json
│       ├── MIL-002_Schema_Naming/
│       │   ├── field_usage_stats.json
│       │   ├── naming_patterns.json
│       │   ├── naming_violations.json
│       │   ├── schema_violations.json
│       │   ├── version_inventory.json
│       │   ├── version_issues.json
│       │   └── milestone_02_summary.json
│       ├── MIL-003_Content_Analysis/
│       │   ├── extracted_entity_ids.json
│       │   ├── json_field_names.json
│       │   ├── markdown_headings.json
│       │   ├── python_variables.json
│       │   ├── redundant_terms_full.json
│       │   ├── terminology_dictionary.json
│       │   └── milestone_03_summary.json
│       └── MIL-004_Relationship_Validation/
│           ├── broken_references.json
│           ├── index_files.json
│           ├── reference_map.json
│           └── milestone_04_summary.json
│
└── REPORTS/                                  # Reports (reorganized)
    └── PROJ-001/
        ├── REP-001_File_Inventory_Report.md
        ├── REP-002_Naming_Convention_Audit.md
        ├── REP-003_Schema_Validation_Report.md
        ├── REP-006_terminology_standards.json
        ├── REP-007_Cross_Reference_Validation.md
        ├── REP-009_Architecture_Documentation.md
        ├── REP-010_Terminology_Consolidation.md
        ├── REP-011_Action_Items_Tracker.csv
        ├── REP-012_Executive_Summary.md
        └── Milestones_02_03_Summary.md
```

---

## 🔗 Cross-References and Links

### Reports → Milestones
Reports reference milestones by ID (e.g., "MIL-001", "MIL-002"). These links remain valid as milestone tracking files are in `Milestones/`.

### Reports → Data Files
Reports reference data files (e.g., "file_distribution.json", "schema_violations.json"). After reorganization, these will be in `Data/PROJ-001/MIL-00X/`. Reports may need path updates or we maintain relative paths.

### Project → All Related Files
The project README will contain links to:
- Scripts: `../../Scripts/PROJ-001/`
- Data: `../../Data/PROJ-001/`
- Reports: `../../REPORTS/PROJ-001/`
- Milestones: `../../Milestones/MIL-00X.json`

---

## ⚠️ Considerations

### 1. Path Updates in Reports
**Issue:** Reports may contain hardcoded paths to data files  
**Solution:** 
- Option A: Update paths in reports to new locations
- Option B: Use relative paths from report location
- Option C: Add a note at top of each report with new data location

**Recommendation:** Option C (add note) - preserves original context, minimal changes

### 2. Script Path Updates
**Issue:** Python scripts may reference data file paths  
**Solution:** Update script paths or add configuration file

**Recommendation:** Update scripts to use relative paths or environment variables

### 3. Empty Milestone Folder
**Issue:** `Milestone_05_Synthesis/` is empty  
**Solution:** Remove empty folder or add placeholder README

**Recommendation:** Remove empty folder (no data files generated for M5)

### 4. Duplicate Milestone Summaries
**Issue:** Milestone summary JSON files exist in both `Milestones/` (tracking) and `Data/` (data)  
**Solution:** Keep both - they serve different purposes:
- `Milestones/MIL-00X.json` - Tracking/status (lightweight)
- `Data/PROJ-001/MIL-00X/milestone_XX_summary.json` - Detailed data (comprehensive)

**Recommendation:** Keep both, document the difference

---

## ✅ Implementation Checklist

### Phase 1: Setup
- [ ] Create `ANALYTICS/Scripts/` folder
- [ ] Create `ANALYTICS/Scripts/PROJ-001/` folder
- [ ] Create `ANALYTICS/Data/` folder
- [ ] Create `ANALYTICS/Data/PROJ-001/` folder
- [ ] Create milestone subfolders in `Data/PROJ-001/`

### Phase 2: Move Scripts
- [ ] Move `milestone_01_inventory.py` → `Scripts/PROJ-001/`
- [ ] Move `milestone_02_schema_naming.py` → `Scripts/PROJ-001/`
- [ ] Move `milestone_03_terminology.py` → `Scripts/PROJ-001/`
- [ ] Move `milestone_04_relationships.py` → `Scripts/PROJ-001/`
- [ ] Create `Scripts/PROJ-001/README.md` documenting scripts

### Phase 3: Move Data Files
- [ ] Move `Milestone_01_Data_Inventory/*.{json,csv,txt}` → `Data/PROJ-001/MIL-001_Data_Inventory/`
- [ ] Move `Milestone_02_Schema_Naming/*.json` → `Data/PROJ-001/MIL-002_Schema_Naming/`
- [ ] Move `Milestone_03_Content_Analysis/*.json` → `Data/PROJ-001/MIL-003_Content_Analysis/`
- [ ] Move `Milestone_04_Relationship_Validation/*.json` → `Data/PROJ-001/MIL-004_Relationship_Validation/`
- [ ] Remove empty `Milestone_05_Synthesis/` folder

### Phase 4: Reorganize Reports
- [ ] Create `REPORTS/PROJ-001/` folder
- [ ] Move `Milestone_01_Data_Inventory/REP-001_File_Inventory_Report.md` → `REPORTS/PROJ-001/`
- [ ] Move `Milestone_02_Schema_Naming/REP-002_Naming_Convention_Audit.md` → `REPORTS/PROJ-001/`
- [ ] Move `Milestone_03_Content_Analysis/REP-006_terminology_standards.json` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-003_Schema_Validation_Report.md` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-007_Cross_Reference_Validation.md` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-009_Architecture_Documentation.md` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-010_Terminology_Consolidation.md` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-011_Action_Items_Tracker.csv` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/REP-012_Executive_Summary.md` → `REPORTS/PROJ-001/`
- [ ] Move `System_Analysis/Milestones_02_03_Summary.md` → `REPORTS/PROJ-001/`
- [ ] Remove empty `System_Analysis/` folder structure

### Phase 5: Update Documentation
- [ ] Update `Projects/PROJ-001_ENTITIES_Analysis/README.md` with new paths
- [ ] Create `Scripts/PROJ-001/README.md` documenting scripts
- [ ] Create `Data/PROJ-001/README.md` documenting data structure
- [ ] Create `REPORTS/PROJ-001/README.md` with report index
- [ ] Update `ANALYTICS/README.md` to document new structure
- [ ] Update `ANALYTICS/INDEX.md` with new folders

### Phase 6: Verification
- [ ] Verify all files moved successfully
- [ ] Verify no broken links in reports
- [ ] Verify milestone tracking files intact
- [ ] Verify project README updated
- [ ] Test script paths (if applicable)

---

## 📝 Notes

### File Naming Conventions
- **Milestones:** `MIL-00X_Milestone_Name.json` (in `Milestones/`)
- **Projects:** `PROJ-00X_Project_Name/` (folder in `Projects/`)
- **Reports:** `REP-00X_Report_Name.md` (in `REPORTS/PROJ-00X/`)
- **Scripts:** `milestone_XX_description.py` (in `Scripts/PROJ-00X/`)
- **Data:** Organized by milestone in `Data/PROJ-00X/MIL-00X/`

### Benefits of This Structure
1. **Clear Separation:** Scripts, data, reports, and tracking are separated
2. **Project Context:** All project-related files grouped by project ID
3. **Scalability:** Easy to add new projects following same pattern
4. **Discoverability:** Clear folder structure makes finding files easier
5. **Maintainability:** Changes to one type of file don't affect others

### Future Projects
When creating new projects, follow this structure:
- Create `Scripts/PROJ-XXX/` for project scripts
- Create `Data/PROJ-XXX/` for project data
- Create `REPORTS/PROJ-XXX/` for project reports
- Add milestone tracking files to `Milestones/`
- Create project instance in `Projects/PROJ-XXX/`

---

## 🚀 Next Steps

1. **Review this plan** with stakeholders
2. **Approve reorganization approach**
3. **Execute phases sequentially** (can be automated with script)
4. **Update documentation** as files are moved
5. **Verify integrity** after completion

---

**Plan Status:** Ready for Implementation  
**Estimated Time:** 1-2 hours for manual execution, 30 minutes if automated  
**Risk Level:** Low (files are moved, not modified)

---

*This plan maintains the existing Analytics structure while improving organization and discoverability of Reports content.*

