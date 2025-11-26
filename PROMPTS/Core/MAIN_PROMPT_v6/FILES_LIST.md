# MAIN_PROMPT_v6 - Complete File List

**Created:** 2025-11-25
**Version:** 6.1
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\MAIN_PROMPT_v6\`

---

## Core Modular Files (9 files)

### 1. 00_MASTER_INDEX.md
**Purpose:** Navigation hub and quick start guide
**Content:**
- Module overview and descriptions
- Quick start patterns (daily ops, video, taxonomy, full system)
- Compression metrics vs v4
- Version history

**Load When:** Starting point for all operations

---

### 2. 01_Core_Identity.md ⭐ UPDATED
**Purpose:** Core identity, primary functions, and task extraction
**Content:**
- WHO YOU ARE, WHAT YOU DO, HOW YOU OPERATE
- Available entities (PRT, MLT, TSK, STP, RSP, ACT, OBJ, PRM, TOL, PMT)
- Task extraction from daily reports with historical context
- Progress indicators (✅ ✔️ 🆕 ⏸️ 🔁)
- Real example: Finance employee daily processing

**Load When:** Processing employee dailies, extracting tasks, tracking progress

**Key Updates v6.1:**
- Removed deprecated SKL, PRF entities
- Added progress tracking section
- Added historical context loading
- Real example from DAILIES/Week3/20

---

### 3. 02_Entity_Taxonomy.md
**Purpose:** ID standards, relationships, validation rules
**Content:**
- XXX-### format specifications
- Entity relationship diagrams (PRT→MLT→TSK→STP)
- Cross-entity linking rules
- Validation before creating entities

**Load When:** Creating new entities, validating IDs

---

### 4. 03_Workflow_Execution.md
**Purpose:** Prompt-based workflows and execution chains
**Content:**
- Video processing (PMT-004 to PMT-013)
- Daily reports by department (PMT-032 to PMT-043)
- Research integration (PMT-044 to PMT-052)
- Task manager operations
- HR automation (PMT-053 to PMT-057)
- System maintenance (PMT-021 to PMT-031, PMT-072)

**Load When:** Executing specific workflows, running prompts

---

### 5. 04_Department_Operations.md
**Purpose:** Department structure, codes, and collaboration
**Content:**
- 10 departments (AID, VID, HRM, DEV, LGN, DGN, MKT, SLS, SMM, FIN)
- Department-specific prompts
- Daily workflow patterns
- Cross-department collaboration

**Load When:** Department-level reporting, understanding dept focus

---

### 6. 05_File_Operations.md ⭐ UPDATED
**Purpose:** Directory structure, file locations, data management
**Content:**
- Complete ENTITIES/ directory tree (current architecture)
- LIBRARIES structure (Responsibilities/Actions/Objects/Parameters/Tools)
- TASK_MANAGERS data locations
- DAILIES processing structure (Week/Day/Employee)
- TAXONOMY master file locations
- Naming conventions
- Validation checklist
- Daily processing workflow with code examples

**Load When:** Understanding file structure, locating data, processing dailies

**Key Updates v6.1:**
- Corrected LIBRARIES paths
- Added DAILIES folder structure
- Added daily processing workflow
- Removed references to deprecated entities

---

### 7. 06_Prompt_Reference.md
**Purpose:** Complete catalog of all 73 prompts
**Content:**
- Prompts by category (Core, Video, Reports, Taxonomy, System, Research, HR, Workflows, Automation, Utilities)
- Decision matrix (which prompt for which task)
- Common prompt chains
- Quick lookup by department and function

**Load When:** Selecting which prompt to use, understanding prompt relationships

---

### 8. 07_Quality_Validation.md
**Purpose:** Validation commands, checklists, error handling
**Content:**
- Auto-validation commands (bash scripts)
- Quality checklists (entity creation, prompt execution)
- Common errors and fixes
- Validation workflow

**Load When:** Before committing, validating entities, fixing errors

---

### 9. 08_External_Modules.md
**Purpose:** Optional on-demand modules for advanced use
**Content:**
- Video Processing Extended
- HR Automation Suite
- Advanced Taxonomy
- API Integration
- Module selection guide

**Load When:** Complex batch operations, schema migrations, API work

---

## Analysis & Documentation (2 files)

### 10. ANALYSIS_REPORT.md ⭐ NEW
**Purpose:** Comprehensive analysis from all requested perspectives
**Content:**
- Executive summary
- File structure overview
- **Daily Employee Operations Perspective**
  - Current workflow
  - Task extraction patterns (before/after)
  - Real example from Finance employee (Daria)
  - Progress indicators
- **Department Daily Overview Perspective**
  - Department structure table
  - Daily workflow (collection → aggregation → cross-dept)
  - Department report template (NEW)
- **Taxonomy Compliance Validation**
  - TAX-001 (LIBRARIES) compliance ✅
  - TAX-002 (TASK_MANAGERS) compliance ✅
  - TAX-003 (Video Processing) ✅
  - TAX-004 (Entity Integration) ✅
- Key improvements in v6.1
- Usage recommendations
- Compliance summary table
- Next steps

**Load When:** Understanding changes, validating compliance, learning workflows

---

### 11. FILES_LIST.md (This File)
**Purpose:** Complete file inventory with descriptions
**Content:**
- All 11 files with purposes and key content
- Load recommendations
- Quick reference guide

---

## Quick Reference Guide

### For Daily Operations
**Load:**
- `01_Core_Identity.md` - Task extraction
- `04_Department_Operations.md` - Dept codes
- `05_File_Operations.md` - DAILIES structure
- `06_Prompt_Reference.md` - PMT-032 to PMT-043

**Use Cases:**
- Processing employee daily reports
- Tracking progress across days
- Generating department summaries
- Creating collection reports

---

### For Taxonomy Work
**Load:**
- `02_Entity_Taxonomy.md` - ID standards
- `05_File_Operations.md` - Master file locations
- `07_Quality_Validation.md` - Validation rules
- `ANALYSIS_REPORT.md` - Compliance check

**Use Cases:**
- Creating new entities
- Validating IDs
- Understanding relationships
- Checking against TAXONOMY folder

---

### For Video Processing
**Load:**
- `01_Core_Identity.md` - Entity extraction
- `03_Workflow_Execution.md` - Video section
- `06_Prompt_Reference.md` - PMT-004 to PMT-013

**Use Cases:**
- Processing transcripts
- Extracting milestones/tasks
- Integrating to taxonomy

---

### For System Understanding
**Load:**
- `00_MASTER_INDEX.md` - Start here
- `ANALYSIS_REPORT.md` - Comprehensive overview
- `FILES_LIST.md` - This file

**Use Cases:**
- Onboarding
- Architecture review
- Understanding changes from v6.0 to v6.1

---

## File Locations

All files located in:
```
C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\MAIN_PROMPT_v6\
```

**Files:**
```
├── 00_MASTER_INDEX.md           (~100 lines)
├── 01_Core_Identity.md          (~180 lines) ⭐ UPDATED v6.1
├── 02_Entity_Taxonomy.md        (~60 lines)
├── 03_Workflow_Execution.md     (~120 lines)
├── 04_Department_Operations.md  (~50 lines)
├── 05_File_Operations.md        (~200 lines) ⭐ UPDATED v6.1
├── 06_Prompt_Reference.md       (~90 lines)
├── 07_Quality_Validation.md     (~70 lines)
├── 08_External_Modules.md       (~50 lines)
├── ANALYSIS_REPORT.md           (~450 lines) ⭐ NEW
└── FILES_LIST.md                (This file)
```

**Total:** ~1,370 lines across 11 files

---

## Key Changes from Original MAIN_PROMPT_v6.md

### What Changed
1. ✅ **Split** monolithic file into 9 modular components
2. ✅ **Removed** deprecated entities (SKL, PRF)
3. ✅ **Updated** LIBRARIES references (RSP, ACT, OBJ, PRM, TOL)
4. ✅ **Added** task extraction focus with progress tracking
5. ✅ **Added** historical context loading (previous days)
6. ✅ **Corrected** file architecture paths
7. ✅ **Added** DAILIES processing workflow
8. ✅ **Created** comprehensive analysis report
9. ✅ **Validated** against TAXONOMY folder structure

### What Stayed Same
1. ✅ Entity ID format (XXX-###)
2. ✅ 73 prompt catalog (PMT-001 to PMT-073)
3. ✅ Validation workflows
4. ✅ Department codes and structure
5. ✅ Workflow chains
6. ✅ Modular architecture concept

---

## Compliance Status

| Check | Status | File Reference |
|-------|--------|----------------|
| **LIBRARIES entities correct** | ✅ PASS | 01_Core_Identity.md, ANALYSIS_REPORT.md |
| **TASK_MANAGERS entities correct** | ✅ PASS | 01_Core_Identity.md |
| **File paths accurate** | ✅ PASS | 05_File_Operations.md |
| **TAXONOMY TAX-001 compliance** | ✅ PASS | ANALYSIS_REPORT.md |
| **TAXONOMY TAX-002 compliance** | ✅ PASS | ANALYSIS_REPORT.md |
| **Daily processing workflow** | ✅ PASS | 01_Core_Identity.md, 05_File_Operations.md |
| **Department structure** | ✅ PASS | 04_Department_Operations.md |
| **Progress tracking** | ✅ PASS | 01_Core_Identity.md, ANALYSIS_REPORT.md |

---

**Status:** All files created and validated ✅
**Version:** 6.1
**Date:** 2025-11-25
