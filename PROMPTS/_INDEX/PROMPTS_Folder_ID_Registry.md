# PROMPTS Folder/Sub-Entity ID Registry

**Generated:** 2025-11-19
**Entity Type:** PROMPTS Sub-Entities (Folders)
**ISO Code:** PMT-F (Prompt Folders)
**Total Folders:** 10 top-level + 17 sub-folders
**Status:** Active - Production Ready

---

## Overview

This document defines the ID system for all folder-level organizational structures within the PROMPTS entity. While individual prompt files use **PMT-###** IDs (PMT-001 through PMT-071), folders use **PMT-F##** IDs to distinguish organizational containers from content files.

**Purpose:**
- Provide stable identifiers for folder references in documentation
- Enable cross-referencing of folder collections in workflows
- Support automated folder structure validation
- Maintain hierarchical organization clarity

---

## ID Format Convention

### Top-Level Folders
```
PMT-F##
  PMT = Prompt entity ISO code
  F   = Folder indicator
  ##  = Sequential 2-digit number (01-10)
```

### Sub-Folders (Nested)
```
PMT-F##-X
  PMT-F## = Parent folder ID
  X       = Letter suffix (A, B, C, D...)
```

**Examples:**
- `PMT-F07` = SYSTEM folder
- `PMT-F07-D` = Taxonomy sub-folder within SYSTEM
- `PMT-F09-A` = Analysis sub-folder within Video_Processing

---

## Top-Level Folder Registry

| Folder ID | Folder Name | Description | File Count | Priority | Status |
|-----------|-------------|-------------|------------|----------|--------|
| **PMT-F01** | _INDEX | Documentation, master indexes, migration logs | 5+ | System | Active |
| **PMT-F02** | _ARCHIVE | Deprecated prompt versions and historical files | 10+ | System | Active |
| **PMT-F03** | Core | Main system prompts (v4, v6, modular versions) | 4 | CRITICAL | Active |
| **PMT-F04** | DATA_FIELDS | Structured data files (CSV, JSON master lists) | 3+ | CRITICAL | Active |
| **PMT-F05** | DEPARTMENTS | Department-specific prompts (2 sub-folders) | 16 | HIGH | Active |
| **PMT-F06** | RESEARCH | Research and analysis prompts (1 sub-folder) | 9 | MEDIUM | Active |
| **PMT-F07** | SYSTEM | System architecture, automation, taxonomy (4 sub-folders) | 13 | CRITICAL | Active |
| **PMT-F08** | UTILITIES | General-purpose utilities and communication (2 sub-folders) | 2 | MEDIUM | Active |
| **PMT-F09** | Video_Processing | Video content processing workflows (4 sub-folders) | 12 | HIGH | Active |
| **PMT-F10** | WORKFLOWS | Operational workflows and integrations (3 sub-folders) | 11 | HIGH | Active |

**Total:** 10 top-level folders containing 71+ prompt files

---

## Sub-Folder Hierarchy

### PMT-F01 - _INDEX (Documentation)
**Purpose:** System documentation and master catalogs
**Location:** `PROMPTS/_INDEX/`

| Sub-ID | File/Folder | Description |
|--------|-------------|-------------|
| - | README.md | Main PROMPTS entity documentation |
| - | MIGRATION_LOG.md | Change history and version tracking |
| - | PROMPTS_Folder_ID_Registry.md | This document |

---

### PMT-F02 - _ARCHIVE (Historical)
**Purpose:** Deprecated and superseded prompt versions
**Location:** `PROMPTS/_ARCHIVE/`

**Contents:** Older versions of PMT-001 through PMT-071, pre-migration files

---

### PMT-F03 - Core (System Prompts)
**Purpose:** Main system-wide AI instruction prompts
**Location:** `PROMPTS/Core/`
**Priority:** CRITICAL

| Prompt ID | File Name | Version | Status |
|-----------|-----------|---------|--------|
| PMT-001 | Main_Prompt_v4.md | v4.0 | Active |
| PMT-002 | Main_Prompt_v6_DRAFT.md | v6.0-draft | Draft |
| PMT-003 | Create_Main_Prompt_v5.md | v1.0 | Utility |
| PMT-073 | Create_Main_Prompt_v6.md | v1.0 | Utility |

**Sub-Folders:**
- `MAIN_PROMPT_v5_Modular/` - Modular architecture components

---

### PMT-F04 - DATA_FIELDS (Master Data)
**Purpose:** Structured catalog files for all prompts
**Location:** `PROMPTS/DATA_FIELDS/`
**Priority:** CRITICAL

| File | Format | Description |
|------|--------|-------------|
| PMT_Master_List.csv | CSV | Complete spreadsheet catalog of 71 prompts |
| Prompts_Index.json | JSON | Lightweight API-ready prompt index |
| PROMPTS_Migration_Map.json | JSON | Old → New ID mappings |

---

### PMT-F05 - DEPARTMENTS (Department-Specific)
**Purpose:** Department-owned and department-specific prompts
**Location:** `PROMPTS/DEPARTMENTS/`
**Priority:** HIGH

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F05-A** | Daily_Reports | 11 | Daily report templates for all departments |
| **PMT-F05-B** | HR_Operations | 5 | HR workflow and candidate processing |

**PMT-F05-A - Daily_Reports:**
- PMT-032 - Daily Report Collection (Master)
- PMT-033 to PMT-043 - Individual department reports

**PMT-F05-B - HR_Operations:**
- PMT-053 - CV Parser v1
- PMT-054 - CRM Data Entry
- PMT-055 - Communication Templates
- PMT-056 - Interview Conductor
- PMT-057 - Job Sites Research

---

### PMT-F06 - RESEARCH (Research Prompts)
**Purpose:** Research and analysis automation
**Location:** `PROMPTS/RESEARCH/`
**Priority:** MEDIUM

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F06-A** | Research_Prompts | 9 | YouTube research, VSCode analysis, department research |

**Prompts:**
- PMT-044 to PMT-052 - Department and tool research

---

### PMT-F07 - SYSTEM (System Architecture)
**Purpose:** System-level architecture, automation, and taxonomy
**Location:** `PROMPTS/SYSTEM/`
**Priority:** CRITICAL

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F07-A** | Architecture_Guides | 2 | Architecture learning and planning |
| **PMT-F07-B** | Automation | 4 | Git version control, automated updates |
| **PMT-F07-C** | System_Analysis | 6 | 6-milestone ecosystem analysis |
| **PMT-F07-D** | Taxonomy | 7 | Taxonomy building and optimization |

**PMT-F07-A - Architecture_Guides:**
- PMT-030 - Architecture Learning Guide
- PMT-031 - Architecture Merge Planning

**PMT-F07-B - Automation:**
- PMT-063 to PMT-066 - Git automation, version control

**PMT-F07-C - System_Analysis:**
- PMT-021 to PMT-026 - 6-milestone ecosystem analysis

**PMT-F07-D - Taxonomy:**
- PMT-014 - Build Taxonomy ID System
- PMT-015 - Optimize Video Transcription
- PMT-016 - Build LIBRARIES Taxonomy
- PMT-017 - Initial ID List
- PMT-018 - Employee Profile Schema
- PMT-019 - Restructure Employee Profile
- PMT-020 - Taxonomy Entities Collection

---

### PMT-F08 - UTILITIES (General Utilities)
**Purpose:** General-purpose utility prompts
**Location:** `PROMPTS/UTILITIES/`
**Priority:** MEDIUM

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F08-A** | Communication | 1 | Communication templates (PMT-055) |
| **PMT-F08-B** | Daily_Updates | 1 | Entity identification (PMT-070) |

---

### PMT-F09 - Video_Processing (Video Workflows)
**Purpose:** Complete video content processing pipeline
**Location:** `PROMPTS/Video_Processing/`
**Priority:** HIGH

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F09-A** | Analysis | 3 | Video analysis and extraction |
| **PMT-F09-B** | Taxonomy_Integration | 1 | Entity integration workflows |
| **PMT-F09-C** | Transcription | 2 | Transcription and naming |
| **PMT-F09-D** | Workflows | 3 | Complete video processing workflows |

**PMT-F09-A - Analysis:**
- PMT-006 - Video Analysis
- PMT-007 - Objects Library Extraction
- PMT-008 - Video Analysis Improvements
- PMT-071 - Actions Library Extraction

**PMT-F09-B - Taxonomy_Integration:**
- PMT-009 - Taxonomy Integration

**PMT-F09-C - Transcription:**
- PMT-004 - Video Transcription v4.1
- PMT-005 - Video Naming Alternatives

**PMT-F09-D - Workflows:**
- PMT-010 - Complete Workflow Full
- PMT-011 - Complete Workflow Short
- PMT-012 - Transcript Processing Workflow

---

### PMT-F10 - WORKFLOWS (Operational Workflows)
**Purpose:** Operational workflows and integration processes
**Location:** `PROMPTS/WORKFLOWS/`
**Priority:** HIGH

#### Sub-Folders

| Sub-ID | Folder Name | Prompt Count | Description |
|--------|-------------|--------------|-------------|
| **PMT-F10-A** | Account_Management | 3 | Account validation and security |
| **PMT-F10-B** | Library_Processing | 3 | LIBRARIES integration workflows |
| **PMT-F10-C** | Operational_Workflows | 5 | Project docs, call organizers, system maintenance |

**PMT-F10-A - Account_Management:**
- PMT-067 - Account Validation
- PMT-068 - Security Review
- PMT-069 - Account Sync

**PMT-F10-B - Library_Processing:**
- PMT-060 - Products Integration
- PMT-061 - Task Manager Entity Filling
- PMT-062 - Tools Collection Matching

**PMT-F10-C - Operational_Workflows:**
- PMT-027 - Data Consistency
- PMT-028 - Folder Reorganization
- PMT-029 - System Health Review
- PMT-058 - Call Organizer v4
- PMT-059 - Document Finished Project
- PMT-072 - PROMPTS Critical Fixes

---

## Folder Hierarchy Tree

```
PROMPTS/
├── PMT-F01 (_INDEX)
│   └── Documentation & Indexes
│
├── PMT-F02 (_ARCHIVE)
│   └── Historical Versions
│
├── PMT-F03 (Core)
│   ├── PMT-001, PMT-002, PMT-003, PMT-073
│   └── MAIN_PROMPT_v5_Modular/
│
├── PMT-F04 (DATA_FIELDS)
│   ├── PMT_Master_List.csv
│   ├── Prompts_Index.json
│   └── PROMPTS_Migration_Map.json
│
├── PMT-F05 (DEPARTMENTS)
│   ├── PMT-F05-A (Daily_Reports)
│   │   └── PMT-032 to PMT-043 (11 prompts)
│   └── PMT-F05-B (HR_Operations)
│       └── PMT-053 to PMT-057 (5 prompts)
│
├── PMT-F06 (RESEARCH)
│   └── PMT-F06-A (Research_Prompts)
│       └── PMT-044 to PMT-052 (9 prompts)
│
├── PMT-F07 (SYSTEM)
│   ├── PMT-F07-A (Architecture_Guides)
│   │   └── PMT-030, PMT-031
│   ├── PMT-F07-B (Automation)
│   │   └── PMT-063 to PMT-066
│   ├── PMT-F07-C (System_Analysis)
│   │   └── PMT-021 to PMT-026
│   └── PMT-F07-D (Taxonomy)
│       └── PMT-014 to PMT-020
│
├── PMT-F08 (UTILITIES)
│   ├── PMT-F08-A (Communication)
│   │   └── PMT-055
│   └── PMT-F08-B (Daily_Updates)
│       └── PMT-070
│
├── PMT-F09 (Video_Processing)
│   ├── PMT-F09-A (Analysis)
│   │   └── PMT-006, PMT-007, PMT-008, PMT-071
│   ├── PMT-F09-B (Taxonomy_Integration)
│   │   └── PMT-009
│   ├── PMT-F09-C (Transcription)
│   │   └── PMT-004, PMT-005
│   └── PMT-F09-D (Workflows)
│       └── PMT-010, PMT-011, PMT-012
│
└── PMT-F10 (WORKFLOWS)
    ├── PMT-F10-A (Account_Management)
    │   └── PMT-067, PMT-068, PMT-069
    ├── PMT-F10-B (Library_Processing)
    │   └── PMT-060, PMT-061, PMT-062
    └── PMT-F10-C (Operational_Workflows)
        └── PMT-027, PMT-028, PMT-029, PMT-058, PMT-059, PMT-072
```

---

## Usage Guidelines

### Referencing Folders in Documentation
```markdown
See [PMT-F07-D](SYSTEM/Taxonomy/) for taxonomy-related prompts
Process uses prompts from [PMT-F09](Video_Processing/) workflow
```

### Cross-Referencing in Workflows
```yaml
workflow_dependencies:
  folder_id: "PMT-F09"
  sub_folder_id: "PMT-F09-D"
  prompts_used: ["PMT-010", "PMT-011", "PMT-012"]
```

### In Task Manager References
```json
{
  "step_id": "STT-045",
  "prompt_folder": "PMT-F09-C",
  "prompt_id": "PMT-004",
  "description": "Use transcription prompt from Video_Processing/Transcription"
}
```

---

## Folder Naming Conventions

### Top-Level Folders
- **Uppercase** for category names (SYSTEM, WORKFLOWS, RESEARCH)
- **PascalCase** for descriptive names (Video_Processing)
- **Underscore prefix** for special folders (_INDEX, _ARCHIVE)

### Sub-Folders
- **PascalCase** for multi-word names (Daily_Reports, Taxonomy_Integration)
- **Descriptive** and action-oriented (Analysis, Transcription)
- **Singular or plural** based on content type

---

## Validation Rules

1. **Uniqueness:** Each PMT-F## ID is globally unique
2. **Sequential:** Top-level IDs are sequential (F01-F10)
3. **Hierarchical:** Sub-folder IDs use letter suffixes (A, B, C...)
4. **Stable:** Folder IDs do not change even if folders are renamed
5. **No gaps:** IDs assigned without skipping numbers

---

## Cross-Entity Integration

### With TASK_MANAGERS
- Task steps reference specific prompt folders
- Workflows specify PMT-F## dependencies
- Checklists link to prompt collections

### With LIBRARIES
- Tools reference prompts via PMT-### IDs
- Actions specify required prompts by folder
- Objects link to creation prompts

### With DEPARTMENTS
- Each department has dedicated prompts in PMT-F05-A
- Department codes used in prompt metadata

---

## Maintenance & Updates

### Adding New Folders
1. Assign next available PMT-F## ID
2. Update this registry document
3. Update folder structure tree
4. Update README.md references
5. Document in MIGRATION_LOG.md

### Renaming Folders
1. **DO NOT** change PMT-F## ID
2. Update folder name on filesystem
3. Update this registry with new name
4. Document change in MIGRATION_LOG.md

### Archiving Folders
1. Move to PMT-F02 (_ARCHIVE)
2. Update Status to "Archived"
3. Maintain ID for historical reference
4. Document in MIGRATION_LOG.md

---

## Quick Reference Summary

| What | ID Format | Example |
|------|-----------|---------|
| Individual Prompts | PMT-### | PMT-001, PMT-045 |
| Top-Level Folders | PMT-F## | PMT-F07, PMT-F09 |
| Sub-Folders | PMT-F##-X | PMT-F07-D, PMT-F09-A |
| Archived Items | (preserved) | PMT-F02 contains all |

---

## Related Documentation

- [README.md](../README.md) - Main PROMPTS entity overview
- [PMT_Master_List.csv](../DATA_FIELDS/PMT_Master_List.csv) - Complete prompt catalog
- [Prompts_Index.json](../DATA_FIELDS/Prompts_Index.json) - API-ready index
- [PMT-014 Build Taxonomy ID System](../SYSTEM/Taxonomy/PMT-014_Build_Taxonomy_ID_System.md) - Taxonomy standards

---

## Changelog

### 2025-11-19
- Initial folder ID system created
- 10 top-level folders cataloged (PMT-F01 to PMT-F10)
- 17 sub-folders assigned letter suffixes
- Complete hierarchical tree documented
- Cross-reference integration defined

---

**Maintained By:** AI & Automation Department
**Entity Owner:** PROMPTS Entity Manager
**Last Updated:** 2025-11-19
**Status:** Active - Production Ready
**Review Schedule:** Quarterly or when structure changes
