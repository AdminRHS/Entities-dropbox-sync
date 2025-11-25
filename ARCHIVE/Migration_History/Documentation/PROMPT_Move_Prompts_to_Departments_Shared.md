# PROMPT: Move and Integrate Prompts from LIBRARIES to LIBRARIES/DEPARTMENTS/_SHARED

**Date Created:** 2025-11-15
**Purpose:** Migrate the entire Prompts directory from LIBRARIES to LIBRARIES/DEPARTMENTS/_SHARED while maintaining all relationships, references, and documentation integrity
**Scope:** 146 files, 3.5MB, 51+ external references, complete archive integration

---

## EXECUTIVE SUMMARY

You are tasked with migrating the Prompts directory from its current location in LIBRARIES to a new centralized location in LIBRARIES/DEPARTMENTS/_SHARED. This migration involves:

- **Moving 146 files** organized in 20+ subdirectories
- **Updating 51+ external references** across TASK_MANAGERS, Transcribations, Research, and other entities
- **Integrating Archive content** into a new LIBRARIES/DEPARTMENTS/_SHARED/Archive structure
- **Updating comprehensive documentation** including master indexes and READMEs
- **Validating all cross-references** to ensure no broken links

This is a critical architectural shift that moves Prompts out of the LIBRARIES entity into the shared resources area of DEPARTMENTS, aligning with the taxonomy's philosophy of department-oriented resource management while maintaining centralized prompt governance.

---

## PART 1: UNDERSTANDING THE CURRENT STATE

### 1.1 Source Directory Structure

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`

**Complete Structure:**
```
LIBRARIES/DEPARTMENTS/_SHARED/Prompts/
├── Core/                                    [11 items]
│   ├── MAIN_PROMPT_v4_Modular/           [11 files]
│   ├── MAIN_PROMPT_v5_Modular/           [Complex structure, 5 subdirectories]
│   │   ├── 00_Core/                      [6 files]
│   │   ├── 01_Library_Integration/       [10 files]
│   │   ├── 02_Output_Templates/          [9 files]
│   │   ├── 03_Processing_Rules/          [README only]
│   │   ├── 04_Usage/                     [README only]
│   │   └── scripts/                      [README only]
│   ├── CREATE_MAIN_PROMPT_v5.md
│   ├── MAIN_PROMPT_v2.md
│   ├── MAIN_PROMPT_v3.md
│   ├── MAIN_PROMPT_v4.md
│   └── README.md
│
├── Daily_Reports/                          [36 items]
│   ├── Constructor/                       [14 files + docs/ subdirectory]
│   │   └── docs/                          [7 files]
│   ├── Department_Prompts/                [12 department-specific prompts]
│   ├── PROMPT_Daily_Report_Collection.md
│   └── README.md
│
├── Video_Processing/                       [24 items]
│   ├── Analysis/                          [3 files]
│   ├── Taxonomy_Integration/              [1 file - MASTER PROMPT]
│   ├── Transcription/                     [3 files]
│   ├── README.md
│   ├── README_MIGRATION.md
│   └── [Additional analysis and transcription files]
│
├── Library_Processing/                     [6 items]
│   ├── Products_Integration_Prompt.md
│   ├── PROMPT_Data_Consistency_and_Knowledge_Integration.md
│   ├── Task_Manager_Entity_Filling_Prompt.md
│   ├── Tools_Collection_and_Matching_Prompt.md
│   ├── README.md
│   └── README_MIGRATION.md
│
├── HR_Operations/                          [6 items]
│   ├── Communication_Templates_Prompt.md
│   ├── CRM_Data_Entry_Prompt.md
│   ├── CV_Parser_v1.md
│   ├── Interview_Conductor_Prompt.md
│   ├── Job_Sites_Deep_Research_Prompt.md
│   └── README.md
│
├── Operational_Workflows/                  [3 items]
│   ├── Call_Organizer_v2.md
│   ├── Call_Organizer_v3.md
│   └── README.md
│
├── Automation/                             [4 items]
│   ├── Rules_Automation.md
│   ├── Version_Control_Automation.md
│   ├── Version_Control_Main.md
│   └── README.md
│
├── Communication/                          [2 items]
│   ├── DropBox_Migration_Announcement.md
│   └── README.md
│
├── Research/                               [14 items]
│   ├── Reports/                           [6 files]
│   ├── SMM_Research_Document_Processing_Instructions.md
│   ├── VSCode_Agent_HQ_Research_Prompt.md
│   ├── YouTube_AI_HR_Tutorials_Research_Prompt.md
│   ├── YouTube_AI_Tools_Daily_Research_Prompt.md
│   ├── YouTube_HR_Automation_Research_Prompt.md
│   ├── YouTube_Video_Research_Prompt_RemoteHelpers_Nov2025.md
│   ├── README.md
│   └── README_MIGRATION.md
│
├── Archive/                                [11 items - TO BE MOVED SEPARATELY]
│   ├── Integration_Plans/                 [3 files]
│   ├── Legacy/                            [1 subdirectory - Prompts_to_run]
│   ├── Session_Logs/                      [2 files]
│   ├── PROMPT_Folder_Reorganization.md
│   └── README.md
│
├── [Root-level files]
├── Architecture_Merge_Planning_Prompt.md
├── PROMPTS_INDEX.json                     [CRITICAL - Master catalog, 693 lines]
├── PROMPT_Data_Consistency_and_Knowledge_Integration.md
├── PROMPT_Folder_Reorganization.md
├── PROMPT_Merge_Transcribations_and_Research_Integration.md
├── README.md                              [CRITICAL - 535 lines comprehensive documentation]
├── System_Health_Review_Prompt.md
└── vscode_ai_extensions_research.md
```

**Statistics:**
- **Total Files:** 146
- **Total Directories:** 20+
- **Total Size:** 3.5MB (active content) + 747.9MB (Archive)
- **File Types:**
  - Markdown (.md): 132+ files (primary format)
  - JSON (.json): 2 files (PROMPTS_INDEX.json is critical)

### 1.2 Critical Files to Preserve

**MUST PRESERVE EXACTLY:**
1. **PROMPTS_INDEX.json** (693 lines) - Master catalog with metadata for all 12 prompts
2. **README.md** (535 lines) - Comprehensive documentation of structure, workflows, relationships
3. All 9 category-level README.md files
4. All 12 active prompts referenced in PROMPTS_INDEX.json
5. Complete directory structure and hierarchy

### 1.3 Destination Directory Structure

**New Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`

**Archive Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive\`

**Final Structure After Move:**
```
LIBRARIES/DEPARTMENTS/
├── _SHARED/
│   ├── Prompts/                          [Complete Prompts directory - MOVED HERE]
│   │   ├── Core/
│   │   ├── Daily_Reports/
│   │   ├── Video_Processing/
│   │   ├── Library_Processing/
│   │   ├── HR_Operations/
│   │   ├── Operational_Workflows/
│   │   ├── Automation/
│   │   ├── Communication/
│   │   ├── Research/
│   │   ├── PROMPTS_INDEX.json
│   │   ├── README.md
│   │   └── [all root-level files]
│   │
│   └── Archive/
│       └── Prompts_Archive/              [Archive content - MOVED HERE]
│           ├── Integration_Plans/
│           ├── Legacy/
│           ├── Session_Logs/
│           └── README.md
│
├── AI/
├── ADMIN/
├── [other departments...]
└── README.md                              [UPDATE with Prompts reference]
```

---

## PART 2: EXTERNAL DEPENDENCIES AND REFERENCES

### 2.1 Files That Reference Prompts Location (51+ files)

**Critical High-Priority References:**

#### A. TASK_MANAGERS (15+ files - HIGHEST PRIORITY)
```
C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Projects\PROJ-AI-NMP-001_Next_Main_Prompt_Version\
├── README.md
├── Milestones\MIL-003_Library_Integration_Modules.json
└── [Other project files]
```
**Update Required:** All references to `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` → `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`

#### B. LIBRARIES/Transcribations (2 files - CRITICAL)
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Transcribations\
├── README.md                              [References Video Processing prompts workflow]
├── VIDEOS_INDEX.md                        [References taxonomy integration prompts]
```
**Update Required:** Update workflow documentation to point to new prompt locations

#### C. LIBRARIES Index Files (2 files - CRITICAL)
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\
├── README.md                              [Section 12 references Prompts sub-entity]
├── LIBRARIES_Import_Index.md              [Catalogs Prompts as LIBRARIES sub-entity]
```
**Update Required:**
- Remove Prompts from LIBRARIES entity list
- Add reference to LIBRARIES/DEPARTMENTS/_SHARED/Prompts
- Update cross-reference matrix

#### D. LIBRARIES/Researches (3+ files - MEDIUM PRIORITY)
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches\
├── README.md
├── Videos\VIDEOS_INDEX.md
└── [Other research documentation]
```
**Update Required:** Update research prompt references

#### E. Additional References (29+ files - VARIOUS PRIORITIES)
- Department README files that reference prompts
- Task templates mentioning prompt workflows
- Project documentation with prompt dependencies
- Workflow definitions using prompts

### 2.2 Path Reference Patterns to Update

Search for and replace these patterns across all 51+ files:

| Old Pattern | New Pattern | Context |
|-------------|-------------|---------|
| `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Absolute paths |
| `../Prompts/` | `../../_SHARED/Prompts/` | Relative from LIBRARIES |
| `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Relative from deep paths |
| `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Full taxonomy paths |

### 2.3 PROMPTS_INDEX.json Internal Updates

**File:** `PROMPTS_INDEX.json` (693 lines)

**Current Structure:**
```json
{
  "metadata": {
    "version": "1.1",
    "last_updated": "2025-11-14",
    "total_prompts": 12
  },
  "prompts": [
    {
      "id": "PRM-VT-001",
      "file_path": "PROMPTS/Transcription/Video_Transcription_Custom_Instructions.md",
      ...
    }
  ]
}
```

**Required Updates:**
1. Update `metadata.last_updated` to migration date
2. Update `metadata.version` to "1.2" (migration version)
3. Add `metadata.migration_info` with old and new locations
4. Keep all `file_path` values as relative paths (no changes needed if using relative paths)
5. If using absolute paths, update all 12 prompt file_path entries

---

## PART 3: STEP-BY-STEP MIGRATION PROCEDURE

### Milestone 1: Pre-Migration Preparation

#### Step 1.1: Create Backup
```bash
# Create complete backup of Prompts directory before any changes
mkdir "C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15"
xcopy "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts" "C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Backup" /E /I /H /Y
```

**Verification:** Confirm backup contains 146 files

#### Step 1.2: Document Current State
```bash
# Generate file listing of current structure
dir /s /b "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts" > "C:\Users\Dell\Dropbox\Taxonomy\Prompts_FileListing_Before_Move.txt"
```

#### Step 1.3: Create Destination Directories
```bash
# Create _SHARED/Prompts directory structure
mkdir "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts"

# Create _SHARED/Archive directory structure
mkdir "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive"
```

**Verification:** Confirm both directories exist and are empty

---

### Milestone 2: Move Archive Content First

#### Step 2.1: Move Archive Directory
```bash
# Move Archive content separately to _SHARED/Archive/Prompts_Archive
xcopy "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Archive" "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive" /E /I /H /Y

# Verify move
dir /s /b "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive" > Archive_Verification.txt
```

**Verification Steps:**
1. Confirm Archive/ directory contains all expected files:
   - Integration_Plans/ (3 files)
   - Legacy/ (subdirectory with Prompts_to_run)
   - Session_Logs/ (2 files)
   - PROMPT_Folder_Reorganization.md
   - README.md
2. Verify total file count matches original

#### Step 2.2: Delete Archive from Source
```bash
# Only after verification - delete Archive from source
rmdir /S /Q "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Archive"
```

**Important:** Do NOT proceed to Milestone 3 until Archive move is verified

---

### Milestone 3: Move Core Prompts Content

#### Step 3.1: Move All Non-Archive Content
```bash
# Move entire Prompts directory (minus Archive which was already moved)
xcopy "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts" "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts" /E /I /H /Y
```

**This moves:**
- Core/ (11 items)
- Daily_Reports/ (36 items)
- Video_Processing/ (24 items)
- Library_Processing/ (6 items)
- HR_Operations/ (6 items)
- Operational_Workflows/ (3 items)
- Automation/ (4 items)
- Communication/ (2 items)
- Research/ (14 items)
- All root-level files (PROMPTS_INDEX.json, README.md, etc.)

#### Step 3.2: Verify Complete Move
```bash
# Generate file listing of new location
dir /s /b "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts" > "C:\Users\Dell\Dropbox\Taxonomy\Prompts_FileListing_After_Move.txt"
```

**Verification Checklist:**
- [ ] 9 category directories present (Core through Research)
- [ ] PROMPTS_INDEX.json present at root
- [ ] README.md present at root (535 lines)
- [ ] All 9 category README.md files present
- [ ] Total file count: 135 files (146 original - 11 Archive files)
- [ ] Total size: ~3.5MB (excluding Archive)
- [ ] No Archive/ directory in new location (it's in _SHARED/Archive/Prompts_Archive instead)

#### Step 3.3: Verify Critical Files
Manually verify these critical files exist at new location:

**Critical Files Checklist:**
- [ ] `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\PROMPTS_INDEX.json` (693 lines)
- [ ] `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\README.md` (535 lines)
- [ ] `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\PROMPTS\Taxonomy_Integration\Taxonomy_Analysis_and_Updates_Prompt.md` (MASTER PROMPT)
- [ ] `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Core\MAIN_PROMPT_v5_Modular\` (complete directory structure)
- [ ] All 12 active prompts from PROMPTS_INDEX.json

---

### Milestone 4: Update Documentation and Indexes

#### Step 4.1: Update PROMPTS_INDEX.json

**File Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\PROMPTS_INDEX.json`

**Required Changes:**
```json
{
  "metadata": {
    "version": "1.2",
    "last_updated": "2025-11-15",
    "total_prompts": 12,
    "migration_info": {
      "migration_date": "2025-11-15",
      "previous_location": "Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/",
      "current_location": "Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/",
      "reason": "Architectural reorganization - moving to department-shared resources",
      "archive_location": "Entities/LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/"
    }
  },
  "prompts": [
    // Keep all prompt entries
    // If file_path values are relative: NO CHANGES NEEDED
    // If file_path values are absolute: UPDATE ALL PATHS
  ]
}
```

**Action:**
1. Open PROMPTS_INDEX.json
2. Update metadata section as shown above
3. If file paths are absolute, update all 12 file_path entries
4. Save and validate JSON syntax

#### Step 4.2: Update Main Prompts README.md

**File Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\README.md`

**Add Migration Notice at Top:**
```markdown
# Prompts Library - Comprehensive Documentation

> **LOCATION UPDATE (2025-11-15):** This Prompts library has been moved from `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` to `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` as part of architectural reorganization. All external references have been updated. Archive content is now located at `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/`.

## Overview
[Rest of existing content...]
```

**Update Archive References:**
- Find all mentions of `Archive/` in README
- Update to reference `../Archive/Prompts_Archive/` (relative path from Prompts/)
- Or reference `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/` (absolute taxonomy path)

#### Step 4.3: Update DEPARTMENTS README.md

**File Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\README.md`

**Add New Section for _SHARED/Prompts:**

Find the section documenting `_SHARED/` resources and add:

```markdown
### _SHARED Resources

The `_SHARED` directory contains resources used across multiple departments:

#### Prompts (`_SHARED/Prompts/`)

**Purpose:** Centralized AI prompt library for all departments

**Contents:**
- **12 active prompts** across 5 categories (Video Processing, HR Operations, Library Processing, Research, Taxonomy Integration)
- **9 prompt categories** with comprehensive documentation
- **Master catalog** (PROMPTS_INDEX.json) with metadata, dependencies, and workflow mappings
- **Complete documentation** including usage guidelines, version history, cross-references

**Categories:**
1. **Core/** - Main system prompts (MAIN_PROMPT v4 and v5 modular structures)
2. **Video_Processing/** - 4 prompts for video transcription, analysis, object extraction, taxonomy integration
3. **HR_Operations/** - 4 prompts for CV parsing, communication, CRM, interviews
4. **Library_Processing/** - 2 prompts for tools collection and products integration
5. **Research/** - Research prompts for VSCode agents, YouTube analysis, SMM research
6. **Daily_Reports/** - Constructor and department-specific daily report prompts
7. **Operational_Workflows/** - Call organizer prompts
8. **Automation/** - Rules and version control automation
9. **Communication/** - Communication templates and announcements

**Key Files:**
- `PROMPTS_INDEX.json` - Master catalog (v1.2, 12 prompts)
- `README.md` - Comprehensive 535-line documentation
- 9 category-level README files

**Related Resources:**
- **Archive:** `_SHARED/Archive/Prompts_Archive/` - Historical prompts, session logs, integration plans
- **TASK_MANAGERS:** Many task templates reference these prompts
- **LIBRARIES:** Video transcriptions, research outputs use these prompts

**Previous Location:** `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` (moved 2025-11-15)

**Usage:**
All departments can reference prompts from this shared location. Department-specific customizations can be created in individual department folders (see SMM/LIBRARIES/prompts.json as example), but core shared prompts remain here for consistency.
```

#### Step 4.4: Update LIBRARIES README.md

**File Location:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\README.md`

**Find Section 12 (or wherever Prompts is referenced) and Update:**

```markdown
### 12. ~~Prompts~~ [MOVED]

**Status:** MOVED to `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` as of 2025-11-15

**New Location:** `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`

**Reason for Move:** Architectural reorganization to consolidate shared resources under DEPARTMENTS structure while maintaining centralized prompt governance.

**For prompt documentation, see:** `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/README.md`

**Archive Location:** `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/`

**Historical Context:** Prompts were originally part of LIBRARIES to maintain centralized knowledge management. Moving to LIBRARIES/DEPARTMENTS/_SHARED maintains centralization while aligning with department-oriented resource structure.
```

**Update Cross-Reference Matrix:**
If LIBRARIES README contains a cross-reference matrix mentioning Prompts, update all entries to point to new location.

#### Step 4.5: Update LIBRARIES_Import_Index.md

**File Location:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\LIBRARIES_Import_Index.md`

**Update Entry for Prompts:**

```markdown
## Sub-Entities Catalog

### Active Sub-Entities
1. Actions
2. Objects
3. Tools
4. Products
5. Professions
6. Responsibilities
7. Skills
8. Processes
9. JobSites
10. Researches
11. Transcribations
12. ~~Prompts~~ → **MOVED to LIBRARIES/DEPARTMENTS/_SHARED/Prompts/** (2025-11-15)

### Moved Sub-Entities

#### Prompts
- **Previous Location:** `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
- **New Location:** `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
- **Move Date:** 2025-11-15
- **Files:** 146 files (135 active + 11 archive)
- **Size:** 3.5MB active content
- **Reason:** Architectural reorganization - consolidating shared resources under DEPARTMENTS
- **Archive:** `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/`
- **Documentation:** See `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/README.md`
```

---

### Milestone 5: Update External References

#### Step 5.1: Update TASK_MANAGERS References

**Priority: CRITICAL - 15+ files**

**Search Pattern:** Find all files in TASK_MANAGERS containing "LIBRARIES/Prompts" or "Prompts/"

**Primary File to Update:**
```
C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Projects\PROJ-AI-NMP-001_Next_Main_Prompt_Version\README.md
```

**Update Strategy:**
1. Open each file
2. Find all references to:
   - `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
   - `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
   - Any relative path to Prompts from LIBRARIES
3. Replace with:
   - `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
   - `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
   - Adjusted relative paths

**Specific Files (search results):**
- All files in `PROJ-AI-NMP-001_Next_Main_Prompt_Version/`
- Task templates referencing prompt workflows
- Project milestones with prompt dependencies
- Workflow definitions using prompts

#### Step 5.2: Update Transcribations References

**Priority: CRITICAL - 2 files**

**Files to Update:**
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Transcribations\README.md
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Transcribations\VIDEOS_INDEX.md
```

**Update Focus:**
- 7-milestone video processing workflow references to prompts
- Links to Video_Processing prompts
- References to Taxonomy Integration master prompt

**Specific Updates:**
```markdown
OLD: See `../Prompts/Video_Processing/` for video processing prompts
NEW: See `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Video_Processing/` for video processing prompts

OLD: Workflow uses prompts from LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Video_Processing/
NEW: Workflow uses prompts from LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Video_Processing/
```

#### Step 5.3: Update Research References

**Priority: MEDIUM - 3+ files**

**Files to Update:**
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches\README.md
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches\Videos\VIDEOS_INDEX.md
[Other research documentation]
```

**Update Strategy:**
- Update research prompt references
- Update links to VSCode research prompts
- Update YouTube research prompt references

#### Step 5.4: Update All Other References (29+ files)

**Use Global Search and Replace:**

**Tools:**
- VS Code: Search in files (Ctrl+Shift+F)
- PowerShell: `Get-ChildItem -Recurse | Select-String "LIBRARIES/Prompts"`
- Find and Replace across all files in Taxonomy directory

**Search Terms:**
1. `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
2. `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`
3. `../Prompts/` (context-dependent)
4. `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`

**Replace With:**
1. `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
2. `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`
3. `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` (adjust based on context)
4. `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`

**Files to Check:**
- All department README files
- All task templates
- All project documentation
- All workflow definitions
- Any automation scripts
- Any configuration files

#### Step 5.5: Verification of Reference Updates

**Create Reference Check List:**
```bash
# Search for any remaining references to old location
cd "C:\Users\Dell\Dropbox\Taxonomy"
findstr /S /I /C:"LIBRARIES/Prompts" *.md *.json *.txt > Remaining_References_Check.txt
findstr /S /I /C:"LIBRARIES\Prompts" *.md *.json *.txt >> Remaining_References_Check.txt
```

**Review Results:**
- Any matches should be intentional (like migration documentation)
- No active workflow/task references should remain
- Update any missed references

---

### Milestone 6: Create _SHARED Documentation

#### Step 6.1: Create or Update _SHARED README

**File Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\README.md`

**If file doesn't exist, create it:**

```markdown
# DEPARTMENTS / _SHARED Resources

**Purpose:** Centralized shared resources accessible to all departments

**Last Updated:** 2025-11-15

---

## Overview

The `_SHARED` directory contains resources that are used across multiple departments. These resources are centralized here to:
- Maintain single source of truth
- Avoid duplication across departments
- Enable consistent cross-department workflows
- Facilitate easier maintenance and updates

---

## Contents

### 1. Prompts (`_SHARED/Prompts/`)

**Purpose:** Centralized AI prompt library for all departments

**Size:** 135 files, ~3.5MB

**Categories:** 9 prompt categories covering:
- Core system prompts
- Video processing workflows
- HR operations
- Library processing
- Research methodologies
- Daily reports
- Operational workflows
- Automation
- Communication templates

**Key Files:**
- `PROMPTS_INDEX.json` - Master catalog of all prompts (v1.2)
- `README.md` - Comprehensive 535-line documentation

**Documentation:** See `Prompts/README.md` for complete details

**Archive:** Historical content at `../Archive/Prompts_Archive/`

---

## Usage Guidelines

### For Departments

**Accessing Shared Prompts:**
- Reference prompts from `_SHARED/Prompts/` in your task templates
- Use relative paths: `../../_SHARED/Prompts/Category/PromptName.md`
- Do not duplicate shared prompts in your department

**Creating Department-Specific Prompts:**
- If you need a highly customized version, create in your department's LIBRARIES
- Example: `SMM/LIBRARIES/prompts.json` (25 SMM-specific prompts)
- Reference shared prompts for general use, customize only when necessary

### For Task Managers

**Referencing in Tasks:**
- Link to specific prompts in task descriptions
- Include prompt version from PROMPTS_INDEX.json
- Note any prompt dependencies

### For Maintenance

**Updating Shared Prompts:**
- Update in `_SHARED/Prompts/` location only
- Update version in PROMPTS_INDEX.json
- Document changes in prompt README
- Notify affected departments if major changes

---

## Archive

**Location:** `_SHARED/Archive/`

Contains historical content and deprecated resources:

### Prompts_Archive (`Archive/Prompts_Archive/`)
- Integration plans
- Legacy prompts and structures
- Session logs from prompt development
- Historical documentation

**Note:** Archive content is preserved for reference but not actively used in workflows.

---

## Relationships

**Related to:**
- **All DEPARTMENTS** - Every department can access _SHARED resources
- **TASK_MANAGERS** - Tasks reference shared prompts
- **LIBRARIES** - Shared prompts support library processing workflows
- **Transcribations** - Video processing uses shared prompts

**Previously Located:**
- Prompts were in `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` until 2025-11-15
- Moved to `_SHARED` to align with department-oriented architecture

---

## Future Shared Resources

This directory may expand to include other shared resources such as:
- Common templates
- Shared documentation
- Cross-department workflows
- Shared tools or utilities

As needs arise, additional shared resources can be added here following the same organizational principles.
```

#### Step 6.2: Create _SHARED/Archive README (if needed)

**File Location:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\README.md`

**If file doesn't exist, create it:**

```markdown
# _SHARED / Archive

**Purpose:** Historical and deprecated shared resources

**Last Updated:** 2025-11-15

---

## Contents

### Prompts_Archive (`Prompts_Archive/`)

**Archived:** 2025-11-15 (moved with Prompts migration)

**Previous Location:** `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Archive/`

**Contents:**
- **Integration_Plans/** - Historical integration planning documents (3 files)
- **Legacy/** - Deprecated prompt structures and formats
  - `Prompts_to_run/` - Old prompt execution directory
- **Session_Logs/** - Development session logs from prompt creation (2 files)
- Historical documentation and planning materials

**Size:** ~747MB (includes large session logs)

**Note:** This archive is preserved for historical reference and may contain useful context for understanding prompt evolution, but content is not actively used in current workflows.

---

## Archive Policy

**Purpose of Archive:**
- Preserve historical context
- Maintain version history
- Reference for understanding design decisions
- Compliance and documentation requirements

**What Gets Archived:**
- Deprecated prompts or workflows
- Superseded documentation
- Historical planning and integration materials
- Development logs and session notes

**What Does NOT Get Archived:**
- Active prompts (stay in `_SHARED/Prompts/`)
- Current documentation
- In-use workflows

---

## Accessing Archive Content

**If you need to reference archive content:**
1. Navigate to `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/`
2. Review README in relevant subdirectory
3. Archived content is read-only - do not modify
4. If you need to resurrect archived content, copy to active location and update

**For Questions:**
- Check `Prompts_Archive/README.md` for archive-specific documentation
- Review session logs for context on why content was archived
- Consult with AI/ADMIN departments for archive management
```

---

### Milestone 7: Delete Old Location (After Full Verification)

**CRITICAL: Only proceed after ALL verifications pass**

#### Step 7.1: Final Verification Checklist

**Before deleting old Prompts directory, verify:**

- [ ] All 135 files successfully moved to `LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`
- [ ] All 11 archive files successfully moved to `LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive\`
- [ ] PROMPTS_INDEX.json updated with migration info
- [ ] Main Prompts README.md updated with location notice
- [ ] DEPARTMENTS README.md updated with _SHARED/Prompts documentation
- [ ] LIBRARIES README.md updated to show Prompts as moved
- [ ] LIBRARIES_Import_Index.md updated
- [ ] All TASK_MANAGERS references updated (15+ files)
- [ ] All Transcribations references updated (2 files)
- [ ] All Researches references updated (3+ files)
- [ ] All other references updated (29+ files)
- [ ] Global search shows no unexpected old path references
- [ ] _SHARED README created/updated
- [ ] Archive README created/updated
- [ ] Backup created and verified

#### Step 7.2: Test Critical Workflows

**Test these workflows to ensure nothing broke:**

1. **Video Processing Workflow:**
   - Check if workflow documentation correctly references new prompt locations
   - Verify all 7 milestones can access their prompts

2. **Task Template References:**
   - Open a task template that references prompts
   - Verify path resolves correctly

3. **PROMPTS_INDEX.json:**
   - Validate JSON syntax
   - Confirm all 12 prompts are accessible at new paths

#### Step 7.3: Delete Old Prompts Directory

**Only after all checks pass:**

```bash
# Final backup before delete
xcopy "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts" "C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Final_Backup" /E /I /H /Y

# Delete old directory
rmdir /S /Q "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts"
```

#### Step 7.4: Verify Deletion

```bash
# Confirm directory no longer exists
dir "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts"
# Should return "File Not Found"
```

---

### Phase 8: Post-Migration Documentation

#### Step 8.1: Create Migration Completion Report

**File Location:** `C:\Users\Dell\Dropbox\Taxonomy\Prompts_Migration_Report_2025-11-15.md`

**Create comprehensive report:**

```markdown
# Prompts Migration Completion Report

**Date:** 2025-11-15
**Migration:** LIBRARIES/Prompts → LIBRARIES/DEPARTMENTS/_SHARED/Prompts
**Status:** COMPLETED

---

## Summary

Successfully migrated the entire Prompts directory from LIBRARIES to LIBRARIES/DEPARTMENTS/_SHARED, including:
- 135 active prompt files
- 11 archive files (moved to _SHARED/Archive/Prompts_Archive)
- Complete directory structure (9 categories, 20+ subdirectories)
- All documentation and indexes

---

## Files Moved

**Active Content:**
- Source: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`
- Destination: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`
- Files: 135 files, ~3.5MB

**Archive Content:**
- Source: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Archive\`
- Destination: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive\`
- Files: 11 files, ~747MB

---

## References Updated

Total external references updated: 51+ files

**By Category:**
- TASK_MANAGERS: 15+ files
- LIBRARIES/Transcribations: 2 files
- LIBRARIES index files: 2 files
- LIBRARIES/Researches: 3+ files
- Other references: 29+ files

**Key Files Updated:**
1. PROMPTS_INDEX.json (migration metadata added)
2. Prompts README.md (location notice added)
3. DEPARTMENTS README.md (Prompts documentation added)
4. LIBRARIES README.md (moved status documented)
5. LIBRARIES_Import_Index.md (catalog updated)
6. _SHARED README.md (created/updated)
7. _SHARED/Archive README.md (created/updated)
8. All TASK_MANAGERS project references
9. All workflow documentation
10. All task templates

---

## Verification Results

**File Counts:**
- Expected active files: 135 ✓
- Expected archive files: 11 ✓
- Total: 146 files ✓

**Critical Files:**
- PROMPTS_INDEX.json present ✓
- Main README.md present ✓
- All 9 category READMEs present ✓
- All 12 active prompts accessible ✓

**Reference Validation:**
- Global search for old paths: No unexpected references ✓
- Task workflow tests: All passing ✓
- PROMPTS_INDEX.json validation: Valid ✓

---

## Backup Locations

**Pre-migration backup:**
`C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Backup\`

**Final backup (before deletion):**
`C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Final_Backup\`

**File listings:**
- Before: `Prompts_FileListing_Before_Move.txt`
- After: `Prompts_FileListing_After_Move.txt`
- Reference check: `Remaining_References_Check.txt`

---

## Architectural Impact

**Before:**
```
LIBRARIES/
├── Actions
├── Objects
├── Tools
├── Prompts          ← Was here
└── [other entities]
```

**After:**
```
LIBRARIES/DEPARTMENTS/
├── _SHARED/
│   ├── Prompts/     ← Now here
│   └── Archive/
│       └── Prompts_Archive/
├── AI/
├── HR/
└── [other departments]

LIBRARIES/
├── Actions
├── Objects
├── Tools
└── [Prompts removed]
```

**Benefits of New Structure:**
- Aligns with department-oriented architecture
- Maintains centralized prompt governance
- Consolidates shared resources in _SHARED
- Separates active content from archive
- Improves discoverability for department users

---

## Post-Migration Tasks Completed

- [x] All files moved successfully
- [x] All references updated
- [x] Documentation updated (7+ files)
- [x] Verification tests passed
- [x] Old directory deleted
- [x] Backups created and verified
- [x] Migration report created

---

## Future Maintenance

**To add new prompts:**
1. Create prompt in `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/[Category]/`
2. Update PROMPTS_INDEX.json with new prompt entry
3. Update category README if needed
4. Reference in tasks as: `../../_SHARED/Prompts/Category/PromptName.md`

**To update existing prompts:**
1. Edit prompt in `_SHARED/Prompts/` location
2. Update version in PROMPTS_INDEX.json
3. Document changes in category README
4. Notify affected departments if major changes

**To archive deprecated prompts:**
1. Move to `_SHARED/Archive/Prompts_Archive/Legacy/`
2. Update PROMPTS_INDEX.json status to "Deprecated"
3. Document deprecation reason in Archive README

---

## Issues Encountered

[Document any issues encountered during migration]

- None reported

---

## Sign-off

**Completed by:** [Your Name/AI Assistant]
**Date:** 2025-11-15
**Verified by:** [Reviewer if applicable]
**Status:** COMPLETE ✓
```

#### Step 8.2: Update Taxonomy Change Log

**If taxonomy has a change log, add entry:**

```markdown
## 2025-11-15: Prompts Migration to LIBRARIES/DEPARTMENTS/_SHARED

**Change Type:** Structural reorganization
**Scope:** High - affects LIBRARIES, DEPARTMENTS, TASK_MANAGERS
**Files Affected:** 51+ files across multiple entities

**Changes:**
- Moved Prompts directory from `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` to `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
- Moved Prompts archive to `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/`
- Updated all external references (51+ files)
- Updated master documentation and indexes
- Created _SHARED resource documentation

**Rationale:** Align with department-oriented architecture while maintaining centralized prompt governance

**Impact:** All departments now access prompts from shared location; improves discoverability and maintains single source of truth

**Migration Report:** See `Prompts_Migration_Report_2025-11-15.md`
```

---

## PART 4: QUICK REFERENCE

### 4.1 Path Translation Quick Reference

| Old Path | New Path | Use Case |
|----------|----------|----------|
| `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Absolute taxonomy path |
| `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Archive/` | `LIBRARIES/DEPARTMENTS/_SHARED/Archive/Prompts_Archive/` | Archive location |
| `../Prompts/` (from LIBRARIES) | `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Relative from LIBRARIES |
| `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `../../LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Relative from deep paths |
| `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` | Full path from taxonomy root |

### 4.2 Critical Files Checklist

**Must Verify After Move:**

| File | Old Location | New Location | Size | Lines |
|------|--------------|--------------|------|-------|
| PROMPTS_INDEX.json | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/ | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/ | ~50KB | 693 |
| README.md | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/ | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/ | ~40KB | 535 |
| Taxonomy_Analysis_and_Updates_Prompt.md | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/PROMPTS/Taxonomy_Integration/ | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/PROMPTS/Taxonomy_Integration/ | ~15KB | - |
| Core/MAIN_PROMPT_v5_Modular/ | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Core/ | LIBRARIES/DEPARTMENTS/_SHARED/Prompts/Core/ | Directory | - |

### 4.3 External Reference Priority Matrix

| File/Directory | Priority | File Count | Impact |
|----------------|----------|------------|--------|
| TASK_MANAGERS | CRITICAL | 15+ | High - workflow dependencies |
| Transcribations | CRITICAL | 2 | High - video processing pipeline |
| LIBRARIES indexes | CRITICAL | 2 | High - structural documentation |
| Researches | MEDIUM | 3+ | Medium - research workflows |
| Other references | LOW-MEDIUM | 29+ | Varies - documentation, templates |

### 4.4 Verification Commands

**Windows Commands:**

```bash
# Count files in new location
dir /s /b "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts" | find /c /v ""

# Search for old references
cd "C:\Users\Dell\Dropbox\Taxonomy"
findstr /S /I /C:"LIBRARIES/Prompts" *.md *.json

# Verify directory deleted
dir "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts"

# Check file sizes
dir "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts"
dir "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive"
```

### 4.5 Rollback Procedure (Emergency Only)

**If migration fails and rollback is needed:**

```bash
# Step 1: Restore from backup
xcopy "C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Backup" "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts" /E /I /H /Y

# Step 2: Delete incomplete new location
rmdir /S /Q "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts"
rmdir /S /Q "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive"

# Step 3: Revert any documentation changes
# (Manual - restore from git if version controlled)

# Step 4: Document rollback reason
# Create Prompts_Migration_Rollback_Report.md
```

---

## PART 5: EXPECTED OUTCOMES

### 5.1 Final Directory Structure

**DEPARTMENTS Structure:**
```
LIBRARIES/DEPARTMENTS/
├── _SHARED/
│   ├── Prompts/                          [135 files, ~3.5MB]
│   │   ├── Core/                         [11 items]
│   │   ├── Daily_Reports/                [36 items]
│   │   ├── Video_Processing/             [24 items]
│   │   ├── Library_Processing/           [6 items]
│   │   ├── HR_Operations/                [6 items]
│   │   ├── Operational_Workflows/        [3 items]
│   │   ├── Automation/                   [4 items]
│   │   ├── Communication/                [2 items]
│   │   ├── Research/                     [14 items]
│   │   ├── PROMPTS_INDEX.json            [v1.2 with migration info]
│   │   ├── README.md                     [535 lines + migration notice]
│   │   └── [other root files]
│   │
│   ├── Archive/
│   │   └── Prompts_Archive/              [11 files, ~747MB]
│   │       ├── Integration_Plans/
│   │       ├── Legacy/
│   │       ├── Session_Logs/
│   │       └── README.md
│   │
│   └── README.md                          [Documents _SHARED resources]
│
├── AI/
├── ADMIN/
├── [other departments...]
└── README.md                              [Updated with Prompts reference]
```

**LIBRARIES Structure (Prompts removed):**
```
LIBRARIES/
├── Actions/
├── Objects/
├── Tools/
├── Products/
├── [other entities... NO MORE Prompts/]
├── README.md                              [Updated - Prompts marked as moved]
└── LIBRARIES_Import_Index.md              [Updated - Prompts listed as moved]
```

### 5.2 Success Criteria

**Migration is considered successful when:**

- [ ] All 146 files successfully moved (135 active + 11 archive)
- [ ] No files lost or corrupted
- [ ] All 51+ external references updated correctly
- [ ] No broken links in documentation
- [ ] PROMPTS_INDEX.json updated and valid
- [ ] All critical workflows still functional
- [ ] Documentation comprehensive and accurate
- [ ] Old location completely removed
- [ ] Backups created and verified
- [ ] Migration report completed

### 5.3 Quality Checks

**Run these final quality checks:**

1. **File Integrity:**
   - Compare file counts before and after
   - Verify file sizes match
   - Check no empty directories

2. **Reference Integrity:**
   - No broken links in markdown files
   - All workflow references resolve
   - Task templates can access prompts

3. **Documentation Quality:**
   - All READMEs updated
   - Migration notice clear
   - Archive documented

4. **Structural Integrity:**
   - Directory hierarchy preserved
   - All categories present
   - Critical files in correct locations

---

## PART 6: TROUBLESHOOTING

### 6.1 Common Issues and Solutions

#### Issue: File count mismatch after move

**Symptoms:** Number of files in new location doesn't match original

**Diagnosis:**
```bash
# Count original
dir /s /b "C:\Users\Dell\Dropbox\Taxonomy\BACKUP_2025-11-15\Prompts_Backup" | find /c /v ""

# Count new location
dir /s /b "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts" | find /c /v ""

# Remember Archive moved separately - add those counts too
```

**Solution:**
- Check if Archive files were counted in original but moved separately
- Verify no hidden files missed
- Check for symbolic links or shortcuts that weren't copied
- Re-run move command with /H flag to include hidden files

#### Issue: Broken references after path updates

**Symptoms:** Links not resolving, 404-style errors in documentation

**Diagnosis:**
```bash
# Find all remaining old path references
findstr /S /I /C:"LIBRARIES/Prompts" *.md *.json
```

**Solution:**
- Check if relative paths need adjustment based on file location
- Verify path separator (/ vs \) consistent
- Ensure no trailing slashes causing issues
- Test links manually

#### Issue: PROMPTS_INDEX.json invalid after update

**Symptoms:** JSON parsing errors, syntax issues

**Diagnosis:**
- Open in JSON validator
- Check for missing commas, brackets
- Verify quotes and escape characters

**Solution:**
- Restore from backup
- Re-apply changes carefully
- Validate after each edit
- Use JSON linter

#### Issue: Archive files not accessible

**Symptoms:** Can't find archive content, directory empty

**Diagnosis:**
```bash
# Check Archive location
dir /s "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Archive\Prompts_Archive"
```

**Solution:**
- Verify Archive was moved in Milestone 2
- Check Archive wasn't included in main Prompts move (would create duplicate)
- Ensure Archive path is correct
- Restore from backup if needed

### 6.2 Validation Failures

**If any validation step fails:**

1. **STOP** - Do not proceed to next phase
2. **Document** - Note exactly what failed and error messages
3. **Diagnose** - Use troubleshooting section to identify issue
4. **Fix** - Apply solution
5. **Re-validate** - Repeat validation step
6. **Continue** - Only proceed when validation passes

**If multiple validations fail:**
- Consider rollback
- Review entire procedure
- Check for systemic issues (permissions, disk space, etc.)

### 6.3 Emergency Contacts and Resources

**Documentation Resources:**
- Original Prompts README: See backup
- PROMPTS_INDEX.json: See backup
- Taxonomy architecture docs: `ARCHITECTURE_ANALYSIS_2025-11-12.md`

**Backup Locations:**
- Primary: `BACKUP_2025-11-15\Prompts_Backup\`
- Final: `BACKUP_2025-11-15\Prompts_Final_Backup\`

**File Listings:**
- Before move: `Prompts_FileListing_Before_Move.txt`
- After move: `Prompts_FileListing_After_Move.txt`

---

## PART 7: COMPLETION CHECKLIST

Use this master checklist to track migration progress:

### Milestone 1: Pre-Migration Preparation
- [ ] Create backup of Prompts directory
- [ ] Verify backup contains 146 files
- [ ] Generate file listing of current structure
- [ ] Create destination directories (_SHARED/Prompts and _SHARED/Archive)
- [ ] Verify destination directories exist and are empty

### Milestone 2: Move Archive Content
- [ ] Move Archive to _SHARED/Archive/Prompts_Archive
- [ ] Verify Archive contains all expected files (11 files)
- [ ] Verify subdirectories (Integration_Plans, Legacy, Session_Logs)
- [ ] Delete Archive from source location
- [ ] Confirm Archive deleted from source

### Milestone 3: Move Core Prompts Content
- [ ] Move all non-Archive content to _SHARED/Prompts
- [ ] Generate file listing of new location
- [ ] Verify 9 category directories present
- [ ] Verify PROMPTS_INDEX.json present
- [ ] Verify main README.md present (535 lines)
- [ ] Verify all 9 category READMEs present
- [ ] Verify file count: 135 files
- [ ] Verify size: ~3.5MB
- [ ] Verify no Archive directory in new Prompts location
- [ ] Verify all 12 active prompts accessible

### Milestone 4: Update Documentation and Indexes
- [ ] Update PROMPTS_INDEX.json metadata
- [ ] Update PROMPTS_INDEX.json migration_info section
- [ ] Update file paths in PROMPTS_INDEX.json (if absolute)
- [ ] Validate PROMPTS_INDEX.json syntax
- [ ] Add migration notice to Prompts README.md
- [ ] Update Archive references in Prompts README.md
- [ ] Add Prompts section to DEPARTMENTS README.md
- [ ] Update LIBRARIES README.md (mark Prompts as moved)
- [ ] Update LIBRARIES_Import_Index.md
- [ ] Create/update _SHARED README.md
- [ ] Create/update _SHARED/Archive README.md

### Milestone 5: Update External References
- [ ] Update all TASK_MANAGERS references (15+ files)
- [ ] Update PROJ-AI-NMP-001 README and files
- [ ] Update other TASK_MANAGERS project files
- [ ] Update Transcribations README.md
- [ ] Update Transcribations VIDEOS_INDEX.md
- [ ] Update Researches README.md
- [ ] Update Researches VIDEOS_INDEX.md
- [ ] Update all other research documentation
- [ ] Run global search and replace for remaining references
- [ ] Update department README files if needed
- [ ] Update task templates
- [ ] Update workflow definitions
- [ ] Search for remaining old path references
- [ ] Review and update any unexpected old references

### Milestone 6: Create _SHARED Documentation
- [ ] Create/update _SHARED README.md with Prompts documentation
- [ ] Create/update _SHARED/Archive README.md
- [ ] Document usage guidelines
- [ ] Document future maintenance procedures

### Milestone 7: Delete Old Location
- [ ] Complete all verifications from Step 7.1
- [ ] Test critical workflows
- [ ] Test video processing workflow references
- [ ] Test task template references
- [ ] Validate PROMPTS_INDEX.json
- [ ] Create final backup before deletion
- [ ] Delete old LIBRARIES/Prompts directory
- [ ] Verify deletion (directory no longer exists)

### Phase 8: Post-Migration Documentation
- [ ] Create migration completion report
- [ ] Document all files moved
- [ ] Document all references updated
- [ ] Document verification results
- [ ] Document backup locations
- [ ] Document architectural impact
- [ ] Update taxonomy change log (if exists)
- [ ] Sign off on migration

### Final Verification
- [ ] All 146 files accounted for (135 active + 11 archive)
- [ ] No files lost or corrupted
- [ ] All references working correctly
- [ ] No broken links
- [ ] Documentation complete and accurate
- [ ] Old location removed
- [ ] Backups verified
- [ ] Migration report complete

---

## CONCLUSION

This prompt provides a comprehensive, step-by-step guide for migrating the Prompts directory from LIBRARIES to LIBRARIES/DEPARTMENTS/_SHARED. Follow each milestone sequentially, complete all verification steps, and do not proceed if any validation fails.

**Key Success Factors:**
1. **Thoroughness** - Complete every step, skip nothing
2. **Verification** - Validate after each milestone before proceeding
3. **Documentation** - Update all references and documentation
4. **Backup** - Maintain multiple backups throughout process
5. **Testing** - Test critical workflows before finalizing

**Estimated Time:** 2-4 hours for careful, thorough execution

**Final Note:** This migration represents a significant architectural shift in the taxonomy structure. Take time to ensure accuracy and completeness. The quality of this migration will impact all departments and workflows going forward.

---

**End of Migration Prompt**

**Document Version:** 1.0
**Created:** 2025-11-15
**For:** Prompts directory migration from LIBRARIES to LIBRARIES/DEPARTMENTS/_SHARED
