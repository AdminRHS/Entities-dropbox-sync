# Prompt: Reorganize Prompts Folder to Match Ecosystem Standards

## Purpose
Reorganize the `Taxonomy\Entities\LIBRARIES\Prompts` folder structure to align with Remote Helpers ecosystem standards, ensuring consistency, discoverability, and proper entity-based organization.

---

## Current State Analysis

### Current Structure Issues
1. **Duplication:** `Daily_Reports/` and `PROMPT_Daily_Report_Collection/` contain overlapping content
2. **Inconsistent Naming:** Mixed conventions (spaces, underscores, PascalCase)
3. **Scattered Main Prompts:** MAIN PROMPT files at root level mixed with other content
4. **Unorganized Files:** Root level contains session logs, integration plans, and various reports
5. **Missing Categories:** Some prompt types lack proper categorization
6. **Inconsistent Metadata:** Not all prompts follow standard metadata format

---

## Target Structure (Ecosystem Standards)

### Folder Organization Principles
1. **Entity-Based Organization:** Group by WHAT (prompt type/function) not WHERE (source)
2. **Hierarchical Structure:** Clear parent-child relationships
3. **Consistent Naming:** Use underscores for folders, PascalCase for files
4. **Version Management:** Separate current from archived versions
5. **Documentation:** README.md in each major folder
6. **Index Files:** JSON indexes for programmatic access

---

## Target Folder Structure

```
Prompts/
├── README.md                                          [Master documentation]
├── PROMPTS_INDEX.json                                 [Master catalog - update]
│
├── Core/                                              [Main system prompts]
│   ├── README.md
│   ├── MAIN_PROMPT_v2.md
│   ├── MAIN_PROMPT_v3.md
│   ├── MAIN_PROMPT_v4.md
│   └── MAIN_PROMPT_v4_Modular/                       [Modular version]
│       ├── README.md
│       ├── 00_Purpose_and_Company_Context.md
│       ├── 01_Employee_Directory.md
│       ├── 02_Project_Directory.md
│       ├── 03_Instructions_for_AI.md
│       ├── 04_Section_Templates_1-11.md
│       ├── 05_Section_Templates_12-21.md
│       ├── 06_Section_22_Taxonomy_Framework.md
│       ├── 07_Section_23_LIBRARIES_Integration.md
│       ├── 08_Processing_Guidelines.md
│       ├── 09_Usage_Instructions.md
│       └── 10_Version_History.md
│
├── Daily_Reports/                                     [Consolidated daily reports]
│   ├── README.md
│   ├── PROMPT_Daily_Report_Collection.md             [Main collection prompt]
│   ├── Constructor/                                   [Template builder]
│   │   ├── README.md
│   │   ├── classification_summary.md
│   │   ├── IMPLEMENTATION_SUMMARY.md
│   │   ├── prompt_parts_structure.json
│   │   ├── README_Enhanced_v2.md
│   │   ├── TEMPLATE_Enhanced_Department_Prompt.md
│   │   ├── TEMPLATE_VARIABLE_MAPPING.md
│   │   └── docs/
│   │       ├── README.md
│   │       ├── 01_employee_directory_guidance.md
│   │       ├── 02_project_directory_guidance.md
│   │       ├── 03_vocabulary_standards.md
│   │       ├── 04_task_object_framework.md
│   │       ├── 05_21_section_framework.md
│   │       └── 06_department_specific_patterns.md
│   └── Department_Prompts/                            [Department-specific prompts]
│       ├── README.md
│       ├── PROMPT_Admin_Daily_Report.md
│       ├── PROMPT_AI_Daily_Report.md
│       ├── PROMPT_Content_Daily_Report.md
│       ├── PROMPT_Design_Daily_Report.md
│       ├── PROMPT_Dev_Daily_Report.md
│       ├── PROMPT_Finance_Daily_Report.md
│       ├── PROMPT_HR_Daily_Report.md
│       ├── PROMPT_LG_Daily_Report.md
│       ├── PROMPT_Marketing_Daily_Report.md
│       ├── PROMPT_Sales_Daily_Report.md
│       ├── PROMPT_SMM_Daily_Report.md
│       └── PROMPT_Video_Daily_Report.md
│
├── Video_Processing/                                  [Video transcription & analysis]
│   ├── README.md
│   ├── Transcription/
│   │   ├── Video_Transcription_Custom_Instructions.md
│   │   ├── Video_Transcription_Custom_Instructions_v3.2.md
│   │   └── Video_Naming_Business_Alternatives_Prompt.md
│   ├── Analysis/
│   │   ├── Video_Analysis_Prompt.md
│   │   └── Objects_Library_Extraction_Prompt.md
│   └── Taxonomy_Integration/
│       ├── Taxonomy_Analysis_and_Updates_Prompt.md
│       └── PROMPT_ANALYSIS_AND_IMPROVEMENTS.md
│
├── Library_Processing/                                [LIBRARIES entity maintenance]
│   ├── README.md
│   ├── Tools_Collection_and_Matching_Prompt.md
│   ├── Products_Integration_Prompt.md
│   └── Task_Manager_Entity_Filling_Prompt.md
│
├── Operational_Workflows/                             [Business process prompts]
│   ├── README.md
│   ├── Call_Organizer_v2.md
│   └── Call_Organizer_v3.md
│
├── Automation/                                        [Automation & version control]
│   ├── README.md
│   ├── Version_Control_Automation.md
│   ├── Rules_Automation.md
│   └── Version_Control_Main.md
│
├── Communication/                                     [Communication templates]
│   ├── README.md
│   └── DropBox_Migration_Announcement.md
│
├── Research/                                         [Research & analysis prompts]
│   ├── README.md
│   ├── SMM_Research_Document_Processing_Instructions.md
│   └── Reports/
│       ├── Video_006_Library_Mapping_Report.md
│       ├── Video_008_Library_Mapping_Report.md
│       └── Tool_Validation_Report_Video_006_008.md
│
└── LBS_009_Archive/                                          [Historical & deprecated]
    ├── README.md
    ├── Session_Logs/
    │   ├── SESSION_LOG_2025-11-12.md
    │   └── SESSION_LOG_2025-11-12_Session2.md
    ├── Integration_Plans/
    │   ├── INTEGRATION_CONTINUATION_PLAN.md
    │   ├── INTEGRATION_STATUS.md
    │   └── Phase_2_Complete_Summary_Report.md
    └── Legacy/
        └── Prompts_to_run/                           [Old folder structure]
            ├── DropBox Migration Announcement.md
            └── Rules automation.md
```

---

## Reorganization Steps

### Step 1: Create Target Folder Structure
1. Create all target folders following the structure above
2. Ensure proper nesting and hierarchy
3. Use consistent naming (underscores for folders, PascalCase for files)

### Step 2: Move Core Prompts
**Action:** Move MAIN PROMPT files to `Core/`
- `MAIN PROMPT v2.md` → `Core/MAIN_PROMPT_v2.md`
- `MAIN PROMPT v3.md` → `Core/MAIN_PROMPT_v3.md`
- `MAIN PROMPT v4.md` → `Core/MAIN_PROMPT_v4.md`
- `MAIN PROMPT v4 - Modular/` → `Core/MAIN_PROMPT_v4_Modular/`

**Rationale:** Core system prompts belong together, separate from specialized prompts

### Step 3: Consolidate Daily Reports
**Action:** Merge `Daily_Reports/` and `PROMPT_Daily_Report_Collection/` into single `Daily_Reports/` structure
- Move `PROMPT_Daily_Report_Collection/Daily_by_Department/*` → `Daily_Reports/Department_Prompts/`
- Move `PROMPT_Daily_Report_Collection/constructor/*` → `Daily_Reports/Constructor/`
- Move `PROMPT_Daily_Report_Collection/README.md` → `Daily_Reports/README.md` (merge with existing)
- Move `Daily_Reports/PROMPT_*.md` → `Daily_Reports/Department_Prompts/` (if not duplicates)
- Delete empty `PROMPT_Daily_Report_Collection/` folder

**Rationale:** Eliminate duplication, create single source of truth

### Step 4: Organize Video Processing
**Action:** Consolidate all video-related prompts
- Move `Video_Transcription/*` → `PROMPTS/Transcription/`
- Create `PROMPTS/Analysis/` and move analysis prompts
- Move `Video_Transcription/Taxonomy_Integration/*` → `PROMPTS/Taxonomy_Integration/`
- Delete empty `Video_Transcription/` folder

**Rationale:** Group by workflow phase (Transcription → Analysis → Integration)

### Step 5: Organize Library Processing
**Action:** Move library maintenance prompts
- Move `Library_Processing/*` → `Library_Processing/` (already correct location)
- Ensure all prompts follow naming conventions

### Step 6: Organize Operational Workflows
**Action:** Move workflow prompts
- Move `Operational_Workflows/*` → `Operational_Workflows/` (already correct)
- Ensure consistent naming

### Step 7: Consolidate Automation
**Action:** Merge automation-related prompts
- Move `Automation/*` → `Automation/` (already correct)
- Move `Version Control/VC MAIN PROMPT.md` → `Automation/Version_Control_Main.md`
- Move `PROMPT_Version_Control_Automation.md` → `Automation/Version_Control_Automation.md`
- Delete empty `Version Control/` folder

**Rationale:** All automation and version control together

### Step 8: Organize Communication
**Action:** Move communication prompts
- Move `Communication/*` → `Communication/` (already correct)
- Move `Prompts to run/DropBox Migration Announcement.md` → `Communication/DropBox_Migration_Announcement.md`
- Move `Prompts to run/Rules automation.md` → `Automation/Rules_Automation.md` (if different from existing)

### Step 9: Create Research Category
**Action:** Organize research and reports
- Create `Research/` folder
- Move `SMM_Research/*` → `Research/SMM_Research_Document_Processing_Instructions.md`
- Create `Research/Reports/` subfolder
- Move `Video_006_Library_Mapping_Report.md` → `Research/Reports/`
- Move `Video_008_Library_Mapping_Report.md` → `Research/Reports/`
- Move `Tool_Validation_Report_Video_006_008.md` → `Research/Reports/`

**Rationale:** Separate research outputs from operational prompts

### Step 10: Archive Historical Files
**Action:** Move session logs and integration plans to Archive
- Create `LBS_009_Archive/Session_Logs/`
- Move `SESSION_LOG_*.md` → `LBS_009_Archive/Session_Logs/`
- Create `LBS_009_Archive/Integration_Plans/`
- Move `INTEGRATION_*.md` → `LBS_009_Archive/Integration_Plans/`
- Move `Phase_2_Complete_Summary_Report.md` → `LBS_009_Archive/Integration_Plans/`
- Move `Prompts to run/` → `LBS_009_Archive/Legacy/Prompts_to_run/` (if still needed)

**Rationale:** Keep active prompts separate from historical documentation

### Step 11: Standardize File Names
**Action:** Rename files to follow conventions
- Replace spaces with underscores in file names
- Use PascalCase for prompt files
- Ensure version numbers follow pattern: `_v2.md`, `_v3.md`, etc.
- Remove special characters except underscores and hyphens

**Examples:**
- `MAIN PROMPT v4.md` → `MAIN_PROMPT_v4.md`
- `DropBox Migration Announcement.md` → `DropBox_Migration_Announcement.md`
- `Video_Transcription_Custom_Instructions_v3.2.md` → `Video_Transcription_Custom_Instructions_v3_2.md` (or keep as is if version format is standard)

### Step 12: Create/Update README Files
**Action:** Add README.md to each major folder
- `Core/README.md` - Document main system prompts
- `Daily_Reports/README.md` - Document daily report system
- `Video_Processing/README.md` - Document video processing workflow
- `Library_Processing/README.md` - Document library maintenance
- `Operational_Workflows/README.md` - Document workflow prompts
- `Automation/README.md` - Document automation prompts
- `Communication/README.md` - Document communication templates
- `Research/README.md` - Document research prompts and reports
- `LBS_009_Archive/README.md` - Document archived content

**Each README should include:**
- Purpose of the category
- List of prompts with brief descriptions
- Usage guidelines
- Related prompts/categories
- Last updated date

### Step 13: Update PROMPTS_INDEX.json
**Action:** Regenerate index with new structure
- Update all file paths to reflect new locations
- Ensure all prompts are cataloged
- Add metadata (category, purpose, version, status)
- Include cross-references

### Step 14: Update Root README.md
**Action:** Update main README.md
- Reflect new folder structure
- Update quick reference table
- Update file paths in examples
- Update workflow diagrams if needed
- Add migration notes

### Step 15: Validation
**Action:** Verify reorganization
- [ ] All files moved to correct locations
- [ ] No duplicate files remain
- [ ] All folder names use underscores
- [ ] All file names follow PascalCase convention
- [ ] All README files created/updated
- [ ] PROMPTS_INDEX.json updated
- [ ] Root README.md updated
- [ ] No broken internal links
- [ ] Archive folder contains only historical files
- [ ] Active prompts easily discoverable

---

## Naming Conventions

### Folders
- Use underscores: `Daily_Reports`, `Video_Processing`
- PascalCase for subfolders: `Department_Prompts`, `Session_Logs`
- Descriptive names: `Taxonomy_Integration` not `TI`

### Files
- PascalCase: `PROMPT_AI_Daily_Report.md`
- Version format: `_v2.md`, `_v3.md`, `_v4.md`
- Descriptive: `Video_Transcription_Custom_Instructions.md`
- No spaces in filenames

### Exceptions
- Keep existing version formats if widely used (e.g., `v3.2.md`)
- Maintain backward compatibility for referenced files

---

## File Metadata Standards

### Required Header for Each Prompt
```markdown
# [Prompt Title]

**Purpose:** [One-line description]
**Category:** [Core | Daily_Reports | Video_Processing | Library_Processing | Operational_Workflows | Automation | Communication | Research]
**Version:** [Semantic version]
**Date:** [Last updated YYYY-MM-DD]
**Status:** [Active | Deprecated | Archive]
**Related Prompts:** [Links to related prompts]
**Dependencies:** [Required prompts/files]
```

---

## Migration Checklist

### Pre-Migration
- [ ] Backup current folder structure
- [ ] Document current file locations
- [ ] Identify all cross-references
- [ ] List all duplicate files

### During Migration
- [ ] Create target folder structure
- [ ] Move files systematically (one category at a time)
- [ ] Rename files to follow conventions
- [ ] Update internal links as you move files
- [ ] Create README files for each category

### Post-Migration
- [ ] Verify all files in correct locations
- [ ] Update PROMPTS_INDEX.json
- [ ] Update root README.md
- [ ] Test prompt references
- [ ] Update any external documentation
- [ ] Notify users of changes

---

## Rollback Plan

If issues arise:
1. Restore from backup
2. Document issues encountered
3. Revise reorganization plan
4. Re-attempt with corrections

---

## Success Criteria

### Structure Quality
- ✅ No duplicate prompts
- ✅ Clear category separation
- ✅ Consistent naming throughout
- ✅ Proper version management
- ✅ Historical files archived

### Documentation Quality
- ✅ README in each major folder
- ✅ Updated PROMPTS_INDEX.json
- ✅ Updated root README.md
- ✅ Clear usage guidelines

### Discoverability
- ✅ Easy to find prompts by category
- ✅ Clear workflow relationships
- ✅ Proper cross-references
- ✅ Logical folder hierarchy

---

## Notes

### Preserve Functionality
- Maintain all existing prompt functionality
- Keep version history intact
- Preserve cross-references
- Maintain backward compatibility where possible

### Future Considerations
- Consider adding prompt tags/metadata
- Consider prompt versioning system
- Consider prompt dependency mapping
- Consider usage analytics tracking

---

## Execution Instructions

1. **Read this prompt completely** before starting
2. **Create backup** of current folder structure
3. **Execute steps sequentially** (1-15)
4. **Validate after each major step** (Core, Daily_Reports, Video_Processing, etc.)
5. **Update documentation** as you go
6. **Test references** after completion
7. **Document any deviations** from plan

---

**Created:** 2025-11-13
**Purpose:** Reorganize Prompts folder to match ecosystem standards
**Status:** Ready for Execution
**Estimated Time:** 2-3 hours
**Risk Level:** Medium (file moves, requires careful execution)

---

*This prompt should be executed by an AI assistant with file system access and careful attention to preserving all functionality while improving organization.*

