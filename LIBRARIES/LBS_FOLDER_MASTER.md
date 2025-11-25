# LBS Folder Master Reference

**Document Type:** Master Reference  
**Entity:** LIBRARIES  
**Created:** 2025-12-26  
**Last Updated:** 2025-12-26  
**Purpose:** Complete reference for all LIBRARIES folders using LBS_XXX_Name convention

---

## Overview

This document provides a complete reference for all LIBRARIES folders using the `LBS_XXX_Name` naming convention. Each folder is numbered sequentially and follows a consistent structure.

---

## Folder Master List

| ID | Folder Name | Display Name | Entity Type | ISO Code | File Count | Status |
|----|-------------|--------------|-------------|----------|------------|--------|
| **LBS_001** | `Responsibilities/Actions` | Actions | Actions | ACT | 429 | Proposed |
| **LBS_002** | `Responsibilities/Objects` | Objects | Objects | OBJ | 110 | Proposed |
| **LBS_003** | `LBS_003_Tools` | Tools | Tools | TOL | 164 | Proposed |
| **LBS_004** | `../TALENTS/Skills` | Skills | Skills | SKL | 29 | Proposed |
| **LBS_005** | `LBS_005_Professions` | Professions | Professions | PRF | 17 | Proposed |
| **LBS_006** | `LBS_006_Departments` | Departments | Departments | DPT | 9 | Proposed |
| **LBS_007** | `Responsibilities/Parameters` | Parameters | Parameters | PRM | 200 | Proposed |
| **LBS_008** | `Taxonomy` | Taxonomy | Taxonomy | TAX | 10 | Proposed |
| **LBS_009** | `Archive` | Archive | Archive | ARC | 0 | Proposed |

**Total:** 9 folders, 968 entities

---

## Detailed Folder Structure

### Responsibilities/Actions

**Purpose:** Standardized action verbs for task naming  
**Old Path:** `LIBRARIES/Responsibilities/Actions/`  
**New Path:** `LIBRARIES/Responsibilities/Actions/`  
**ISO Code:** ACT

**Subfolders:**
- `Master/` - Master action files (actions_master.json, etc.)
- `By_Domain/` - Domain-specific actions (video_generation_actions.json)
- `Data_Operations/` - Data operation actions (13 files)
- `Archive/` - Archived action files

**Key Files:**
- `Master/actions_master.json` - Complete catalog (429 actions)
- `Master/actions_command_verbs.json` - Command verbs subset
- `Master/actions_process_verbs.json` - Process verbs subset
- `Master/actions_result_verbs.json` - Result verbs subset

---

### Responsibilities/Objects

**Purpose:** Business objects and deliverables  
**Old Path:** `LIBRARIES/Responsibilities/Objects/`  
**New Path:** `LIBRARIES/Responsibilities/Objects/`  
**ISO Code:** OBJ

**Subfolders:**
- `Master/` - Master object files
- `By_Domain/` - Objects organized by domain:
  - `AI_Objects/` - AI-related objects
  - `Development_Objects/` - Development objects
  - `Design_Objects/` - Design deliverables
  - `Video_Objects/` - Video production objects
  - `Marketing_Objects/` - Marketing deliverables
  - `HR_Objects/` - HR/Recruitment objects
  - `Lead_Generation_Objects/` - Lead generation objects
  - `General_Objects/` - General document objects
- `Metadata/` - Object metadata (object_types.json, etc.)

**Key Files:**
- `Master/objects_master.json` - Complete catalog
- `Metadata/object_types.json` - Object type classifications

---

### LBS_003_Tools

**Purpose:** Software, platforms, and services  
**Old Path:** `LIBRARIES/LBS_003_LBS_003_Tools/`  
**New Path:** `LIBRARIES/LBS_003_LBS_003_Tools/`  
**ISO Code:** TOL

**Subfolders:**
- `Master/` - Master tool listing
- `By_Category/` - Tools organized by category:
  - `AI/` - AI tools (LLM_Services, Image_Generation, Video_Generation, Code_Assistance, AI_Frameworks)
  - `Development/` - Development tools (Code_Editors, Frameworks, Databases, Cloud_Platforms, DevOps)
  - `Automation/` - Automation platforms
  - `Design/` - Design tools
  - `Video_Editing/` - Video editing software
  - `Social_Media/` - Social media platforms
  - `Business/` - Business tools
  - `Integrations/` - Integration services (MCP_Services, Connectors)
- `Root_Files/` - Root-level tool files (to be categorized)

**Key Files:**
- `Master/tools_master_listing.json` - Complete AI tools catalog (80+ tools)

---

### ../TALENTS/Skills

**Purpose:** Skills combining responsibilities and tools  
**Old Path:** `LIBRARIES/LBS_004_../TALENTS/Skills/`  
**New Path:** `LIBRARIES/LBS_004_../TALENTS/Skills/`  
**ISO Code:** SKL

**Subfolders:**
- `Master/` - Master skills catalog (all_skills.json, skills_index.json, skills_metadata.json)
- `By_Department/` - Skills by department (7 files)
- `By_Profession/` - Skills by profession (13 files)
- `By_Difficulty/` - Skills by difficulty (beginner, intermediate, advanced)
- `By_Tool/` - Skills organized by tool
- `Mappings/` - Skill mapping files (skill_profession_map.json, skill_tool_map.json)
- `Templates/` - Skill templates (3 files)

**Key Files:**
- `Master/all_skills.json` - Complete skills catalog (28+ skills)

---

### LBS_005_Professions

**Purpose:** Job roles and profession definitions  
**Old Path:** `LIBRARIES/LBS_005_LBS_005_Professions/`  
**New Path:** `LIBRARIES/LBS_005_LBS_005_Professions/`  
**ISO Code:** PRF

**Subfolders:**
- `Master/` - Master professions file (professions.json)
- `Individual/` - Individual profession files (16 files)

**Key Files:**
- `Master/professions.json` - Complete professions list (17 professions)
- `Individual/ai_engineer.json` - AI Engineer profession
- `Individual/backend_developer.json` - Backend Developer profession
- `Individual/designer.json` - Designer profession
- ... (13 more individual profession files)

---

### LBS_006_Departments

**Purpose:** Organizational units and department definitions  
**Old Path:** `LIBRARIES/LBS_006_Departments/`  
**New Path:** `LIBRARIES/LBS_006_Departments/`  
**ISO Code:** DPT

**Subfolders:**
- `Master/` - Master departments file (departments.json)
- `By_Department/` - Department-specific data:
  - `AI/` - AI department data (9 files)
  - `SMM/` - SMM department data (2 files)
  - ... (other departments)

**Key Files:**
- `Master/departments.json` - Complete departments list (9 departments)

**Departments:**
- AIA - AI & Automation
- DEV - Development
- HRM - Human Resources
- LGN - Lead Generation
- DGN - Design
- VID - Video Production
- SLS - Sales
- SMM - Social Media Management
- FNC - Finance

---

### Responsibilities/Parameters

**Purpose:** Configuration parameters and settings  
**Old Path:** `LIBRARIES/Responsibilities/Parameters/`  
**New Path:** `LIBRARIES/Responsibilities/Parameters/`  
**ISO Code:** PRM

**Subfolders:**
- `Master/` - Master parameters file (parameters.json)
- `By_Profession/` - Parameters by profession (8 files)
- `By_Department/` - Parameters by department (4 files)

**Key Files:**
- `Master/parameters.json` - Master parameters file
- `By_Profession/graphic_designer_parameters.json` - Designer parameters (25)
- `By_Profession/backend_developer_parameters.json` - Developer parameters (30)
- `By_Profession/lead_generator_parameters.json` - Lead generator parameters (28)
- ... (5 more profession parameter files)

---

### Taxonomy

**Purpose:** Taxonomy documentation, master lists, and migration maps  
**Old Path:** `LIBRARIES/Taxonomy/`  
**New Path:** `LIBRARIES/Taxonomy/`  
**ISO Code:** TAX

**Subfolders:**
- `Master_Lists/` - Master list CSV files
- `Documentation/` - Taxonomy documentation (4 markdown files)
- `Scripts/` - Taxonomy generation scripts (generate_master_list.py)
- `Migrations/` - Migration maps and logs

**Key Files:**
- `Master_Lists/libraries_master_list_2025-12-26.csv` - Latest master list (335 entities)
- `Documentation/libraries_iso_code_registry.md` - ISO code registry
- `Documentation/libraries_hierarchy_tree.md` - Hierarchy tree
- `Documentation/id_and_name_conventions.md` - ID and naming conventions
- `Scripts/generate_master_list.py` - Master list generation script

---

### Archive

**Purpose:** Archived and legacy files  
**Old Path:** `LIBRARIES/Archive/`  
**New Path:** `LIBRARIES/Archive/`  
**ISO Code:** ARC

**Subfolders:**
- `Legacy_Root_Files/` - Legacy root-level files (actions.json, objects.json, tools.json)
- `Backups/` - Backup folders with dates (actions_backup_20251118, objects_backup_20251118)
- `Deprecated/` - Deprecated files and folders
- `Old_Structure/` - Old folder structure after migration:
  - `Responsibilities/` - Old Responsibilities folder
  - `LBS_003_Tools/` - Old Tools folder
  - `../TALENTS/Skills/` - Old Skills folder
  - `LBS_005_Professions/` - Old Professions folder
  - `LBS_006_Departments/` - Old DEPARTMENTS folder
  - `Taxonomy/` - Old Taxonomy folder

---

## Path Mapping Reference

| Old Path | New Path | Notes |
|----------|----------|-------|
| `LIBRARIES/Responsibilities/Actions/` | `LIBRARIES/Responsibilities/Actions/` | Actions split from Responsibilities |
| `LIBRARIES/Responsibilities/Objects/` | `LIBRARIES/Responsibilities/Objects/` | Objects split from Responsibilities |
| `LIBRARIES/LBS_003_LBS_003_Tools/` | `LIBRARIES/LBS_003_LBS_003_Tools/` | Tools folder renamed |
| `LIBRARIES/LBS_004_../TALENTS/Skills/` | `LIBRARIES/LBS_004_../TALENTS/Skills/` | Skills folder renamed |
| `LIBRARIES/LBS_005_LBS_005_Professions/` | `LIBRARIES/LBS_005_LBS_005_Professions/` | Professions folder renamed |
| `LIBRARIES/LBS_006_Departments/` | `LIBRARIES/LBS_006_Departments/` | Departments folder renamed |
| `LIBRARIES/Responsibilities/Parameters/` | `LIBRARIES/Responsibilities/Parameters/` | Parameters split from Responsibilities |
| `LIBRARIES/Taxonomy/` | `LIBRARIES/Taxonomy/` | Taxonomy folder renamed |
| `LIBRARIES/Archive/` | `LIBRARIES/Archive/` | Archive folder renamed |

---

## Statistics

- **Total Folders:** 9
- **Total Entities:** 968
- **Breakdown:**
  - Actions: 429
  - Objects: 110
  - Tools: 164
  - Skills: 29
  - Professions: 17
  - Departments: 9
  - Parameters: 200
  - Taxonomy: 10

---

## Related Documents

- [FOLDER_NAMING_PROPOSAL.md](FOLDER_NAMING_PROPOSAL.md) - Detailed proposal
- [FOLDER_STRUCTURE_QUICK_REFERENCE.md](FOLDER_STRUCTURE_QUICK_REFERENCE.md) - Quick reference
- [FOLDER_MIGRATION_NOTE_2025-12-26.md](FOLDER_MIGRATION_NOTE_2025-12-26.md) - Migration notes
- [FILES_TO_UPDATE.md](FILES_TO_UPDATE.md) - Files requiring updates
- [LBS_FOLDER_MASTER.json](LBS_FOLDER_MASTER.json) - JSON master file
- [LBS_FOLDER_MASTER.csv](LBS_FOLDER_MASTER.csv) - CSV master file

---

**Status:** Active Reference  
**Last Updated:** 2025-12-26


