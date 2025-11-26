# PROMPTS Entity Documentation

**Entity Type:** Standalone Entity
**ISO Code:** PMT
**Location:** `ENTITIES/PROMPTS/`
**Purpose:** Centralized repository of AI prompts and custom instructions for all workflows

---

## Quick Navigation

- [Overview](#overview)
- [Entity Structure](#entity-structure)
- [Prompt Categories](#prompt-categories)
- [Quick Start Guide](#quick-start-guide)
- [Taxonomy Reference](#taxonomy-reference)
- [Usage Guidelines](#usage-guidelines)
- [Related Documentation](#related-documentation)

---

## Overview

PROMPTS is a **standalone entity** that serves as the centralized knowledge base for all AI instructions, custom prompts, and methodology guides used across the entire ENTITIES ecosystem.

### Key Facts

- **Total Prompts:** 155 files
- **Categories:** 12 functional categories
- **Departments Served:** All departments (AIA, DEV, HRM, LGN, DGN, VID, SLS, SMM, MKT, FIN)
- **Entity Status:** Active - Production Ready
- **ISO Code:** **PMT** (PromPTs)

### Primary Functions

1. **Video Processing** - Complete workflows for transcription, analysis, and taxonomy extraction
2. **Daily Reporting** - Automated department-specific report generation (11 departments)
3. **System Operations** - Core system prompts (MAIN_PROMPT v2-v6)
4. **Taxonomy Integration** - Gap analysis and entity synchronization
5. **Library Management** - Tools, products, and entity maintenance
6. **Research & Analysis** - Research processing and content extraction
7. **Automation** - Version control and workflow automation

---

## Entity Structure

```
PROMPTS/
├── README.md (this file)
├── MIGRATION_LOG.md
├── PROMPTS_INDEX.json
│
├── Taxonomy/                    [7 files] - ISO codes, master list, taxonomy docs
│
├── Core/                        [63 files] - System prompts, MAIN_PROMPT versions
│   ├── MAIN_PROMPT_v4.md (Active)
│   ├── MAIN_PROMPT_v5_Modular/ (46 files)
│   └── MAIN_PROMPT_v6_DRAFT.md
│
├── Daily_Reports/               [26 files] - Department-specific reporting
│   ├── Constructor/ (8 files)
│   └── Department_Prompts/ (11 files)
│
├── Video_Processing/            [12 files] - Video workflows
│   ├── Transcription/ (3 files)
│   ├── Analysis/ (3 files)
│   └── Taxonomy_Integration/ (1 file)
│
├── Library_Processing/          [4 files] - LIBRARIES integration
│
├── Operational_Workflows/       [5 files] - Business processes
│
├── Automation/                  [4 files] - Workflow automation
│
├── HR_Operations/               [6 files] - HR-specific prompts
│
├── Research_Prompts/            [9 files] - Research processing
│
├── System_Analysis/             [7 files] - System architecture
│
├── Account_Management/          [3 files] - Account operations
│
└── Communication/               [1 file] - Communication templates
```

**Total Files:** 155 markdown files across 12 categories

---

## Prompt Categories

### 1. Core System Prompts (PMT-COR)
**Location:** `PROMPTS/Core/` | **Files:** 63

The foundation of the system - contains all versions of MAIN_PROMPT and modular components.

**Key Prompts:**
- **MAIN_PROMPT_v4.md** - Current active system prompt
- **MAIN_PROMPT_v5_Modular/** - Next-gen modular architecture (46 files)
  - 00_Core/ (Company context, employee directory, AI instructions)
  - 01_Library_Integration/ (Department-specific libraries)
  - 02_Output_Templates/ (21 section templates)
  - 03_Processing_Rules/
  - 04_Usage/

**Status:** v4 = Active | v5 = In Development | v6 = Draft
**Use When:** Setting up AI system context, configuring main operations

---

### 2. Daily Reports (PMT-DLY)
**Location:** `PROMPTS/Daily_Reports/` | **Files:** 26

Automated daily report generation for every department in the organization.

**Department Prompts:** (11 total)
- PROMPT_AI_Daily_Report.md (AIA)
- PROMPT_Content_Daily_Report.md (MKT)
- PROMPT_Design_Daily_Report.md (DGN)
- PROMPT_Dev_Daily_Report.md (DEV)
- PROMPT_Finance_Daily_Report.md (FIN)
- PROMPT_HR_Daily_Report.md (HRM)
- PROMPT_LG_Daily_Report.md (LGN)
- PROMPT_Marketing_Daily_Report.md (MKT)
- PROMPT_Sales_Daily_Report.md (SLS)
- PROMPT_SMM_Daily_Report.md (SMM)
- PROMPT_Video_Daily_Report.md (VID)

**Constructor Tools:** (8 files)
- Template builders and prompt generators
- Variable mapping systems
- Classification frameworks

**Use When:** Generating daily departmental reports, tracking progress

---

### 3. Video Processing (PMT-VID)
**Location:** `PROMPTS/Video_Processing/` | **Files:** 12

Complete 7-phase video processing workflow for extracting taxonomy elements from video content.

**Workflow Phases:**

**Phase 1-2: Transcription** (`Transcription/`)
- Video_Transcription_Custom_Instructions_v3.2.md
- Video_Naming_Business_Alternatives_Prompt.md
- Video_Transcription_Custom_Instructions.md

**Phase 3-4: Analysis** (`Analysis/`)
- Video_Analysis_Prompt.md (Initial analysis)
- Objects_Library_Extraction_Prompt.md (Detailed extraction)
- PROMPT_ANALYSIS_AND_IMPROVEMENTS.md

**Phase 5-7: Integration** (`Taxonomy_Integration/`)
- Taxonomy_Analysis_and_Updates_Prompt.md (Master integration prompt)

**Complete Video Workflow:**
```
Video → Transcribe → Name → Analyze → Extract Objects →
Gap Analysis → Update Taxonomy → Generate Report
```

**Use When:** Processing tutorial videos, extracting workflows, building taxonomy

---

### 4. Library Processing (PMT-LIB)
**Location:** `PROMPTS/Library_Processing/` | **Files:** 4

Specialized prompts for maintaining and integrating LIBRARIES entities.

**Key Prompts:**
- **Tools_Collection_and_Matching_Prompt.md** - Tool discovery and validation
- **Products_Integration_Prompt.md** - Product processing with AI-first optimization
- **Task_Manager_Entity_Filling_Prompt.md** - Populate TASK_MANAGERS from LIBRARIES
- **PROMPT_Data_Consistency_and_Knowledge_Integration.md** - Data validation

**Use When:** Updating Tools library, integrating new products, syncing entities

---

### 5. Operational Workflows (PMT-OPS)
**Location:** `PROMPTS/Operational_Workflows/` | **Files:** 5

Business process automation and organizational prompts.

**Key Prompts:**
- **Call_Organizer_v4.md** (Active) - Meeting and call organization
- **PROMPT_Document_Finished_Project.md** - Project documentation
- Archive/ (v2, v3 deprecated versions)

**Use When:** Organizing meetings, documenting completed projects

---

### 6. Automation (PMT-AUT)
**Location:** `PROMPTS/Automation/` | **Files:** 4

Workflow automation and version control prompts.

**Key Prompts:**
- **Version_Control_Automation.md** - Automated version management
- **Version_Control_Main.md** - Main version control workflow
- **Rules_Automation.md** - Business rules automation

**Use When:** Setting up automation, managing versions, implementing rules

---

### 7. HR Operations (PMT-HRM)
**Location:** `PROMPTS/HR_Operations/` | **Files:** 6

Human resources specific prompts for recruitment and talent management.

**Key Prompts:**
- **CV_Parser_v1.md** - Extract candidate information from CVs
- **Interview_Conductor_Prompt.md** - Interview guidance
- **Job_Sites_Deep_Research_Prompt.md** - Job market research
- **Communication_Templates_Prompt.md** - HR communications
- **CRM_Data_Entry_Prompt.md** - Candidate data management

**Use When:** Screening candidates, conducting interviews, researching job markets

---

### 8. Research Prompts (PMT-RSR)
**Location:** `PROMPTS/Research_Prompts/` | **Files:** 9

Research processing and content analysis prompts.

**Key Prompts:**
- **SMM_Research_Document_Processing_Instructions.md** - Social media research
- **YouTube_AI_Tools_Daily_Research_Prompt.md** - AI tools research
- **YouTube_HR_Automation_Research_Prompt.md** - HR automation research
- **Sales_Department_Research_Prompt.md** - Sales research
- **VSCode_Agent_HQ_Research_Prompt.md** - Development tools research

**Use When:** Processing research documents, analyzing video content, extracting insights

---

### 9. System Analysis (PMT-SYS)
**Location:** `PROMPTS/System_Analysis/` | **Files:** 7

System architecture analysis and ecosystem validation prompts.

**Key Prompts:**
- **00_MAIN_Ecosystem_Analysis_Overview.md** - System-wide analysis
- **01_Milestone_Data_Inventory.md** - Data cataloging
- **02_Milestone_Schema_Naming_Validation.md** - Schema validation
- **03_Milestone_Content_Analysis.md** - Content analysis
- **04_Milestone_Relationship_Validation.md** - Relationship checking
- **05_Milestone_Synthesis_Recommendations.md** - Recommendations

**Use When:** Analyzing system architecture, validating schemas, ecosystem health checks

---

### 10. Taxonomy (PMT-TAX)
**Location:** `PROMPTS/Taxonomy/` | **Files:** 7

Taxonomy building, ID system creation, and structural optimization prompts.

**Key Prompts:**
- **PROMPT_Build_Taxonomy_ID_System.md** - ID system architecture
- **PROMPT_Build_LIBRARIES_Taxonomy.md** - LIBRARIES taxonomy creation
- **PROMPT_Build_Employee_Profile_Schema_Workflow.md** - Employee schema
- **PROMPT_Optimize_Video_Transcription_Instructions.md** - Transcription optimization
- **PROMPT_Restructure_Employee_Profile_to_Task_Managers.md** - Profile restructuring

**Taxonomy Files:**
- Prompts_Master_List.csv (48 entities cataloged)
- Prompts_ISO_Code_Registry.md (PMT code documentation)

**Use When:** Building taxonomy systems, creating ID structures, optimizing workflows

---

### 11. Account Management (PMT-ACT)
**Location:** `PROMPTS/Account_Management/` | **Files:** 3

Account operations, security, and subscription management.

**Key Prompts:**
- **PROMPT_Account_Creation_Validation.md** - Validate new accounts
- **PROMPT_Account_Security_Audit.md** - Security auditing
- **PROMPT_Subscription_Renewal_Alert.md** - Renewal notifications

**Use When:** Setting up accounts, conducting security audits, managing subscriptions

---

### 12. Communication (PMT-COM)
**Location:** `PROMPTS/Communication/` | **Files:** 1

Communication templates and announcements.

**Use When:** Creating announcements, communication planning

---

## Quick Start Guide

### For New Users

1. **Start with Core**
   - Read `Core/MAIN_PROMPT_v4.md` to understand system context
   - Review `Core/MAIN_PROMPT_v5_Modular/README.md` for modular architecture

2. **Choose Your Workflow**
   - **Video Processing?** → Start with `PROMPTS/Transcription/`
   - **Daily Reports?** → Check `Daily_Reports/Department_Prompts/`
   - **Library Updates?** → Use `Library_Processing/`
   - **Research?** → Browse `Research_Prompts/`

3. **Follow the Phase Order**
   - Video: Transcribe → Analyze → Extract → Integrate
   - Library: Collect → Validate → Integrate → Update
   - Research: Source → Process → Extract → Document

### For Video Processing

**Complete Workflow:**
```
1. Transcribe → Use Video_Transcription_Custom_Instructions_v3.2.md
2. Name → Use Video_Naming_Business_Alternatives_Prompt.md (optional)
3. Analyze → Use Video_Analysis_Prompt.md
4. Extract → Use Objects_Library_Extraction_Prompt.md
5. Integrate → Use Taxonomy_Analysis_and_Updates_Prompt.md
```

### For Daily Reports

**Department-Specific:**
```
1. Choose your department prompt from Daily_Reports/Department_Prompts/
2. Use Constructor/ tools to customize if needed
3. Generate report following template sections
```

### For Library Maintenance

**Tools/Products:**
```
1. Collect → Tools_Collection_and_Matching_Prompt.md
2. Process → Products_Integration_Prompt.md
3. Fill → Task_Manager_Entity_Filling_Prompt.md
4. Validate → PROMPT_Data_Consistency_and_Knowledge_Integration.md
```

---

## Taxonomy Reference

### ISO Code: PMT
**PMT** = **P**ro**M**p**T**s (Consonant-only naming)

**Why PMT instead of PRM?**
- **PRM** in LIBRARIES = Parameters
- **PRM** in TASK_MANAGERS (legacy) = Prompts
- **PMT** avoids confusion across entities

### Entity Categories

| Category Code | Name | Files | Primary Dept |
|--------------|------|-------|--------------|
| PMT-COR | Core | 63 | Multi-Department |
| PMT-DLY | Daily Reports | 26 | Multi-Department |
| PMT-VID | Video Processing | 12 | Video Production |
| PMT-LIB | Library Processing | 4 | AI & Automation |
| PMT-OPS | Operational Workflows | 5 | Operations |
| PMT-AUT | Automation | 4 | AI & Automation |
| PMT-HRM | HR Operations | 6 | Human Resources |
| PMT-RSR | Research | 9 | Multi-Department |
| PMT-SYS | System Analysis | 7 | AI & Automation |
| PMT-TAX | Taxonomy | 7 | AI & Automation |
| PMT-ACT | Account Management | 3 | Operations |
| PMT-COM | Communication | 1 | Multi-Department |

### Master Catalog
**Location:** `PROMPTS/Taxonomy/Prompts_Master_List.csv`
- 48 entities currently cataloged
- Full ISO code registry available
- Hierarchical organization documented

---

## Usage Guidelines

### Version Control

**Active Versions:**
- MAIN_PROMPT: **v4** (current production)
- Call_Organizer: **v4** (current)
- Video_Transcription: **v3.2** (current)

**In Development:**
- MAIN_PROMPT v5 (modular architecture)
- MAIN_PROMPT v6 (draft phase)

**Deprecated:**
- MAIN_PROMPT v2, v3
- Call_Organizer v2, v3

### Naming Conventions

**Files:**
- Use `PROMPT_` prefix for specific operational prompts
- Include version numbers: `_v1`, `_v2`, `_v3.2`
- Use underscores, not spaces: `Video_Analysis_Prompt.md`

**Versions:**
- Major version = Breaking changes (v4 → v5)
- Minor version = New features (v3.1 → v3.2)
- Always document changes in version history

### Best Practices

1. **Always read README first** - Each category has usage instructions
2. **Follow phase order** - Especially critical for Video Processing
3. **Use latest active version** - Check status before using
4. **Document customizations** - If you modify a prompt
5. **Test before production** - Validate with sample data
6. **Cross-reference entities** - Link to related LIBRARIES/TASK_MANAGERS

---

## File Organization

### Archive Strategy

Deprecated prompts are moved to category-specific Archive folders:
```
Operational_Workflows/Archive/
├── Call_Organizer_v2.md
└── Call_Organizer_v3.md

Taxonomy/Archive/
└── Depricated_PROMPT_ENTITIES_Data_Synchronization_Architecture.md
```

### Index Files

- **PROMPTS_INDEX.json** - Master catalog of all prompts
- **Taxonomy/Prompts_Master_List.csv** - Entity catalog (48 entries)
- **Taxonomy/Prompts_ISO_Code_Registry.md** - Code documentation

---

## Integration with Other Entities

### PROMPTS → LIBRARIES
- Tools discovery and validation
- Products integration and optimization
- Entity synchronization
- Parameter mapping

### PROMPTS → TASK_MANAGERS
- Task template creation
- Step template generation
- Project documentation
- Workflow automation

### PROMPTS → All Departments
- Daily report generation (11 departments)
- Department-specific workflows
- Taxonomy extraction
- Research processing

---

## Related Documentation

### Within PROMPTS
- [Taxonomy/Prompts_Master_List.csv](Taxonomy/Prompts_Master_List.csv) - Complete catalog
- [Taxonomy/Prompts_ISO_Code_Registry.md](Taxonomy/Prompts_ISO_Code_Registry.md) - ISO codes
- [MIGRATION_LOG.md](MIGRATION_LOG.md) - Migration history
- [PROMPTS_INDEX.json](PROMPTS_INDEX.json) - Master index

### Other Entities
- [LIBRARIES README](../LIBRARIES/README.md) - Library components
- [TASK_MANAGERS README](../TASK_MANAGERS/README.md) - Templates and workflows
- [LIBRARIES Taxonomy](../LIBRARIES/Taxonomy/) - LIBRARIES taxonomy docs
- [TASK_MANAGERS Taxonomy](../TASK_MANAGERS/Taxonomy/) - TM taxonomy docs

### Cross-Entity References
- [LIBRARIES ISO Registry](../LIBRARIES/Taxonomy/Libraries_ISO_Code_Registry.md) - PMT cross-reference
- [TASK_MANAGERS ISO Registry](../TASK_MANAGERS/Taxonomy/Taxonomy_ISO_Code_Registry.md) - PMT reference

---

## Entity History

### Location Changes
1. **2025-11-15:** `LIBRARIES/Prompts/` → `LIBRARIES/DEPARTMENTS/PROMPTS/`
2. **2025-11-15:** `LIBRARIES/DEPARTMENTS/PROMPTS/` → `TASK_MANAGERS/PROMPTS/`
3. **2025-11-18:** `TASK_MANAGERS/PROMPTS/` → `ENTITIES/PROMPTS/` ✓ Current

### Key Milestones
- **2025-11-12:** Initial PROMPTS library creation
- **2025-11-13:** Folder structure aligned with ecosystem standards
- **2025-11-15:** Moved to TASK_MANAGERS for consolidation
- **2025-11-16:** Enhanced with G. DATA OPERATIONS category
- **2025-11-18:** **Promoted to standalone entity** ← Current status
- **2025-11-18:** Taxonomy created (PMT code established)

---

## Statistics

### Entity Metrics
- **Total Prompts:** 155 markdown files
- **Categories:** 12 functional areas
- **Departments Served:** 11 (AIA, DEV, HRM, LGN, DGN, VID, SLS, SMM, MKT, FIN, Multi)
- **Active Versions:** 3 major prompt systems (MAIN v4, Call Org v4, Video Trans v3.2)
- **Cataloged Entities:** 48 in Master List (107 remaining to catalog)

### Category Distribution
- Largest: Core (63 files, 40.6%)
- Second: Daily Reports (26 files, 16.8%)
- Third: Video Processing (12 files, 7.7%)
- Others: 54 files (34.8%)

### Department Coverage
- Multi-Department prompts: 40%
- AI & Automation: 25%
- Video Production: 10%
- HR & Operations: 10%
- Lead Gen & Sales: 8%
- Design & Marketing: 7%

---

## Maintenance

### Regular Tasks
- **Weekly:** Review new prompt requests
- **Monthly:** Update version statuses
- **Quarterly:** Audit deprecated prompts
- **Annually:** Major version planning

### Update Process
1. Create new prompt in appropriate category
2. Add entry to Prompts_Master_List.csv
3. Update PROMPTS_INDEX.json
4. Document in category README
5. Test with sample data
6. Deploy to production

### Quality Standards
- All prompts must have metadata headers
- Version history required for all prompts
- Validation checklists mandatory
- Cross-references documented
- Example outputs provided

---

## Support & Contact

**Maintained By:** Taxonomy Team
**Entity Owner:** AI & Automation Department
**Status:** Active - Production Ready
**Last Major Update:** 2025-11-18 (Entity migration)
**Next Review:** 2025-12-01

### Getting Help
1. Check category-specific README files
2. Review Taxonomy documentation
3. Consult PROMPTS_INDEX.json
4. Contact Taxonomy Team

---

## Version Information

**README Version:** 2.0
**README Created:** 2025-11-12
**README Updated:** 2025-11-18
**Entity Status:** Active
**Entity ISO Code:** PMT
**Entity Location:** `ENTITIES/PROMPTS/`

---

**[⬆ Back to Top](#prompts-entity-documentation)**
