# PROMPTS ISO Code Registry

**Document Type:** Taxonomy Reference
**Entity:** PROMPTS
**Last Updated:** 2025-11-18
**Purpose:** Standardized entity type codes and naming conventions for PROMPTS

---

## Overview

This registry documents the ISO-style codes used to identify and categorize all prompt types within the PROMPTS entity. These codes provide:
- **Unique identification** for each prompt and prompt category
- **Consistent naming** across the system
- **Quick reference** for prompt classification
- **Hierarchical organization** support

---

## Core Entity Type Code

### Primary Entity Type

| ISO Code | Entity Type | Consonant-Only | Description | Total Count |
|----------|-------------|----------------|-------------|-------------|
| **PMT** | Prompts | Yes | AI prompts and custom instructions | 155 files, 48 cataloged |

**Note:** PMT (PromPTs) is used instead of PRM to avoid confusion with:
- **PRM** in LIBRARIES = Parameters
- **PRM** in TASK_MANAGERS legacy = Prompts

---

## Prompt Category Codes

Prompts are organized into 12 functional categories:

| Category Code | Category Name | Prompt Count | Primary Department |
|---------------|---------------|--------------|-------------------|
| **PMT-COR** | Core | 63 | Multi-Department |
| **PMT-DLY** | Daily Reports | 26 | Multi-Department |
| **PMT-VID** | Video Processing | 12 | Video Production |
| **PMT-LIB** | Library Processing | 4 | AI & Automation |
| **PMT-OPS** | Operational Workflows | 5 | Operations |
| **PMT-AUT** | Automation | 4 | AI & Automation |
| **PMT-HRM** | HR Operations | 6 | Human Resources |
| **PMT-RSR** | Research | 9 | Multi-Department |
| **PMT-SYS** | System Analysis | 7 | AI & Automation |
| **PMT-TAX** | Taxonomy | 7 | AI & Automation |
| **PMT-ACT** | Account Management | 3 | Operations |
| **PMT-COM** | Communication | 1 | Multi-Department |

---

## Department-Specific Prompt Codes

Daily Report prompts organized by department:

| Prompt Code | Department | Full Name | File Path |
|-------------|------------|-----------|-----------|
| **PMT-DLY-AIA** | AI & Automation | AI Daily Report | PROMPT_AI_Daily_Report.md |
| **PMT-DLY-MKT** | Marketing | Content Daily Report | PROMPT_Content_Daily_Report.md |
| **PMT-DLY-DGN** | Design | Design Daily Report | PROMPT_Design_Daily_Report.md |
| **PMT-DLY-DEV** | Development | Dev Daily Report | PROMPT_Dev_Daily_Report.md |
| **PMT-DLY-FIN** | Finance | Finance Daily Report | PROMPT_Finance_Daily_Report.md |
| **PMT-DLY-HRM** | Human Resources | HR Daily Report | PROMPT_HR_Daily_Report.md |
| **PMT-DLY-LGN** | Lead Generation | LG Daily Report | PROMPT_LG_Daily_Report.md |
| **PMT-DLY-MKT2** | Marketing | Marketing Daily Report | PROMPT_Marketing_Daily_Report.md |
| **PMT-DLY-SLS** | Sales | Sales Daily Report | PROMPT_Sales_Daily_Report.md |
| **PMT-DLY-SMM** | SMM | SMM Daily Report | PROMPT_SMM_Daily_Report.md |
| **PMT-DLY-VID** | Video Production | Video Daily Report | PROMPT_Video_Daily_Report.md |

**Department Codes:** AIA, DGN, DEV, HRM, LGN, MKT, SLS, SMM, VID, FIN

---

## Prompt Type Classifications

### By Functional Purpose

| Type Code | Type Name | Description | Example |
|-----------|-----------|-------------|---------|
| **PMT-SYS** | System Prompts | Core AI system instructions | MAIN_PROMPT_v4 |
| **PMT-WKF** | Workflow Prompts | Multi-step process instructions | Video Processing Workflow |
| **PMT-RPT** | Report Prompts | Data extraction and reporting | Daily Report Collection |
| **PMT-INT** | Integration Prompts | Entity integration and synchronization | Taxonomy Integration |
| **PMT-VAL** | Validation Prompts | Data quality and consistency checks | Account Validation |
| **PMT-ANA** | Analysis Prompts | Content analysis and extraction | Video Analysis |
| **PMT-DOC** | Documentation Prompts | Documentation generation | Project Documentation |

### By Usage Pattern

| Usage Code | Usage Pattern | Description | Count |
|------------|---------------|-------------|-------|
| **PMT-ACT** | Active | Currently in production use | 40+ |
| **PMT-DEP** | Deprecated | Older versions kept for reference | 5 |
| **PMT-DRF** | Draft | Under development | 3 |
| **PMT-ARC** | Archived | Historical versions | 10+ |

---

## Version Naming Convention

### Core System Prompts
Format: `MAIN_PROMPT_v{MAJOR}.{MINOR}`

Example versions:
- **MAIN_PROMPT_v2.md** - Deprecated
- **MAIN_PROMPT_v3.md** - Being phased out
- **MAIN_PROMPT_v4.md** - **Current/Active**
- **MAIN_PROMPT_v5_Modular/** - In development
- **MAIN_PROMPT_v6_DRAFT.md** - Future planning

### Operational Prompts
Format: `{PromptName}_v{VERSION}`

Examples:
- **Call_Organizer_v4.md** - Active
- **CV_Parser_v1.md** - Active
- **Video_Transcription_Custom_Instructions_v3.2.md** - Active

### Department Prompts
Format: `PROMPT_{Department}_Daily_Report.md`

Examples:
- PROMPT_AI_Daily_Report.md
- PROMPT_Dev_Daily_Report.md
- PROMPT_HR_Daily_Report.md

### Taxonomy Prompts
Format: `PROMPT_{Purpose}_Taxonomy.md`

Examples:
- PROMPT_Build_Taxonomy_ID_System.md
- PROMPT_Build_LIBRARIES_Taxonomy.md
- PROMPT_Optimize_Video_Transcription_Instructions.md

---

## Hierarchical ID Structure

### Multi-Level Prompt IDs

For nested prompt collections:

```
Level 1: PMT-001 (Core Category)
Level 2: PMT-001-002 (MAIN_PROMPT_v4)
Level 3: PMT-001-003 (MAIN_PROMPT_v5_Modular)
Level 4: PMT-001-003-001 (Module: Purpose and Context)
```

Example hierarchy:
```
PMT-017 = "Video Processing Prompts"
  └─ PMT-018 = "Video Transcription"
  └─ PMT-019 = "Video Analysis"
  └─ PMT-020 = "Objects Extraction"
  └─ PMT-021 = "Taxonomy Integration"
```

---

## File Naming Standards

### General Rules

1. **PROMPT_ Prefix**
   - Use for specific operational prompts
   - Format: `PROMPT_{Description}.md`
   - Example: `PROMPT_Account_Creation_Validation.md`

2. **Descriptive Names**
   - Use clear, action-oriented names
   - Format: `{Action}_{Object}_Prompt.md`
   - Example: `Objects_Library_Extraction_Prompt.md`

3. **Version Suffixes**
   - Include version for iterative prompts
   - Format: `{PromptName}_v{VERSION}.md`
   - Example: `Call_Organizer_v4.md`

4. **No Spaces**
   - Use underscores instead of spaces
   - ✅ `Video_Analysis_Prompt.md`
   - ❌ `Video Analysis Prompt.md`

---

## Consonant-Only Codes

Following TASK_MANAGERS and LIBRARIES convention:

✅ **Correct:**
- PMT (Prompts)
- COR (Core)
- DLY (Daily)
- VID (Video)
- LIB (Library)
- OPS (Operations)
- AUT (Automation)
- HRM (Human Resources)
- RSR (Research)
- SYS (System)
- TAX (Taxonomy)
- ACT (Account)
- COM (Communication)

❌ **Incorrect:**
- PRMT (extra consonant)
- PROM (contains O)
- CORE (contains O and E)

---

## Cross-Entity Code Consistency

### Department Codes (Shared Across All Entities)

| Code | Department | Used In |
|------|-----------|---------|
| **AIA** | AI & Automation | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **DEV** | Development | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **HRM** | Human Resources | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **LGN** | Lead Generation | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **DGN** | Design | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **VID** | Video Production | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **SLS** | Sales | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **SMM** | Social Media | TASK_MANAGERS, LIBRARIES, PROMPTS |
| **MKT** | Marketing | LIBRARIES, PROMPTS |
| **FIN** | Finance | PROMPTS |

---

## Entity Type Code Comparison

| Entity | Code | Full Name | Purpose |
|--------|------|-----------|---------|
| TASK_MANAGERS | PRM | Prompts (legacy) | Template instructions |
| LIBRARIES | PRM | Parameters | Configuration variables |
| **PROMPTS** | **PMT** | **Prompts** | **AI instructions and workflows** |

**Resolution:** PROMPTS uses **PMT** to avoid PRM conflicts.

---

## Validation Rules

### Code Format Validation

1. **Length:** 3 characters for entity type codes
2. **Characters:** Uppercase letters only
3. **Consonants:** No vowels (A, E, I, O, U) in primary codes
4. **Uniqueness:** Each code unique within PROMPTS entity

### File Naming Validation

1. **Extensions:** Always `.md` for prompts
2. **Structure:**
   - Category folders: Title Case (e.g., `Video_Processing/`)
   - Files: `PROMPT_` prefix or descriptive naming
3. **Versions:** Semantic versioning (v1, v2, v3.1, etc.)

---

## Code Assignment Process

### When Creating New Prompts

1. **Determine Category** - Which folder? (Core, Daily_Reports, Video_Processing, etc.)
2. **Check Registry** - Review this document for existing codes
3. **Assign Next ID** - Use next available sequential PMT number
4. **Format File Name** - Follow naming conventions
5. **Update Registry** - Add new prompt to this document
6. **Update Master CSV** - Add row to Prompts_Master_List.csv

### Example Process

```
New prompt: "Customer Onboarding Workflow" (HR department)

1. Category = HR_Operations (PMT-HRM)
2. Check: Last HR prompt = PMT-035
3. Assign: PMT-050 (next available in sequence)
4. File name: PROMPT_Customer_Onboarding_Workflow.md
5. Path: PROMPTS/HR_Operations/
6. Update: This registry + CSV
```

---

## Archive & Legacy Structure

### Deprecated Versions

Located in category-specific Archive folders:

```
PROMPTS/
├── Operational_Workflows/
│   └── Archive/
│       ├── Call_Organizer_v2.md (Deprecated)
│       └── Call_Organizer_v3.md (Deprecated)
│
└── Taxonomy/
    └── Archive/
        └── Depricated_PROMPT_ENTITIES_Data_Synchronization_Architecture.md
```

---

## Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | 2025-11-18 | Initial PROMPTS ISO Code Registry creation | Taxonomy Team |
| 1.0 | 2025-11-18 | Established PMT code to avoid PRM conflicts | Taxonomy Team |

---

## Related Documents

- [Prompts_Master_List.csv](./Prompts_Master_List.csv) - Complete prompt catalog
- [Prompts_Hierarchy_Tree.md](./Prompts_Hierarchy_Tree.md) - Visual hierarchy (to be created)
- [Prompts_Department_Distribution.md](./Prompts_Department_Distribution.md) - Statistics (to be created)
- [../README.md](../README.md) - PROMPTS entity documentation
- [../MIGRATION_LOG.md](../MIGRATION_LOG.md) - Migration history

---

**Document Status:** Active
**Maintenance Schedule:** Update whenever new prompt categories or codes are added
**Owner:** PROMPTS Taxonomy Team
**Contact:** Taxonomy Team

---

**ISO Code:** **PMT** (PromPTs)
**Entity Status:** Active - Standalone Entity
**Location:** `ENTITIES/PROMPTS/`
