# PROMPTS Entity

**Entity Type:** PROMPTS
**ISO Code:** PMT
**Total Prompts:** 71 (PMT-001 through PMT-071)
**Status:** Active - Standalone Entity
**Last Updated:** 2025-11-19

---

## Overview

The PROMPTS entity contains all AI instruction templates, workflows, and custom instructions used across the organization. Each prompt is assigned a unique PMT-### identifier following the TASK_MANAGERS taxonomy pattern.

**Purpose:**
- Standardize AI interactions across departments
- Maintain version control for prompt templates
- Enable systematic prompt engineering and optimization
- Provide reusable instruction sets for common operations

---

## Folder Structure

```
PROMPTS/
├── _INDEX/                    # Documentation and master indexes
├── _ARCHIVE/                  # Deprecated prompt versions
├── Core/                      # Main system prompts (v4, v6 draft)
├── DATA_FIELDS/              # Structured data files (CSV, JSON)
├── DEPARTMENTS/              # Department-specific prompts
│   ├── Daily_Reports/        # Daily report templates (11 departments)
│   └── HR_Operations/        # HR workflow prompts
├── RESEARCH/                 # Research and analysis prompts
│   └── Research_Prompts/     # YouTube, VSCode, department research
├── SYSTEM/                   # System architecture and taxonomy
│   ├── Architecture_Guides/  # Architecture learning and planning
│   ├── Automation/          # Automation and version control
│   ├── System_Analysis/     # Ecosystem analysis milestones
│   └── Taxonomy/            # Taxonomy building and optimization
├── UTILITIES/               # General-purpose utilities
│   ├── Communication/       # Communication templates
│   └── Daily_Updates/       # Entity identification
├── Video_Processing/        # Video content processing
│   ├── Analysis/           # Video analysis and extraction
│   ├── Taxonomy_Integration/ # Entity integration
│   ├── Transcription/      # Transcription and naming
│   └── Workflows/          # Complete video workflows
└── WORKFLOWS/              # Operational workflows
    ├── Account_Management/ # Account validation and security
    ├── Library_Processing/ # LIBRARIES integration
    └── Operational_Workflows/ # Call organizer, project docs
```

---

## Quick Reference

### Core System Prompts
- **PMT-002** - Main Prompt v6 (Current Active) - Ultra-condensed, 73% reduction, <3s load
- **PMT-001** - Main Prompt v4 (Deprecated) - Will be archived after 90-day transition
- **PMT-003** - Create Main Prompt v5 (Utility)
- **PMT-073** - Create Main Prompt v6 (Generator) - Used to create v6

### Video Processing (12 prompts)
- **PMT-004** - Video Transcription v4.1 (TASK_MANAGERS extraction)
- **PMT-005** - Video Naming Alternatives
- **PMT-006** - Video Analysis
- **PMT-007** - Objects Library Extraction
- **PMT-008** - Video Analysis Improvements
- **PMT-009** - Taxonomy Integration
- **PMT-010** - Complete Workflow Full
- **PMT-011** - Complete Workflow Short
- **PMT-012** - Transcript Processing Workflow
- **PMT-071** - Actions Library Extraction

### Daily Reports (11 prompts)
- **PMT-032** - Daily Report Collection (Master)
- **PMT-033** - AI & Automation Daily Report
- **PMT-034** - Content/Marketing Daily Report
- **PMT-035** - Design Daily Report
- **PMT-036** - Development Daily Report
- **PMT-037** - Finance Daily Report
- **PMT-038** - HR Daily Report
- **PMT-039** - Lead Generation Daily Report
- **PMT-040** - Marketing Daily Report
- **PMT-041** - Sales Daily Report
- **PMT-042** - Social Media Daily Report
- **PMT-043** - Video Production Daily Report

### Taxonomy & System (13 prompts)
- **PMT-014** - Build Taxonomy ID System
- **PMT-015** - Optimize Video Transcription
- **PMT-016** - Build LIBRARIES Taxonomy
- **PMT-017** - Initial ID List
- **PMT-018** - Employee Profile Schema
- **PMT-019** - Restructure Employee Profile
- **PMT-020** - Taxonomy Entities Collection
- **PMT-021** - Ecosystem Analysis Overview
- **PMT-022** - Data Inventory
- **PMT-023** - Schema Validation
- **PMT-024** - Content Analysis
- **PMT-025** - Relationship Validation
- **PMT-026** - Synthesis Recommendations

### Research (9 prompts)
- **PMT-044** - Sales Department Research
- **PMT-045** - SMM Document Processing
- **PMT-046** - VSCode Agent HQ Research
- **PMT-047** - YouTube AI HR Tutorials
- **PMT-048** - YouTube AI Tools Daily
- **PMT-049** - YouTube HR Automation
- **PMT-050** - YouTube Remote Helpers
- **PMT-051** - Department Research Integration
- **PMT-052** - VSCode AI Extensions

### HR Operations (5 prompts)
- **PMT-053** - CV Parser v1
- **PMT-054** - CRM Data Entry
- **PMT-055** - Communication Templates
- **PMT-056** - Interview Conductor
- **PMT-057** - Job Sites Research

### Workflows (11 prompts)
- **PMT-027** - Data Consistency
- **PMT-028** - Folder Reorganization
- **PMT-029** - System Health Review
- **PMT-030** - Architecture Learning Guide
- **PMT-031** - Architecture Merge Planning
- **PMT-058** - Call Organizer v4
- **PMT-059** - Document Finished Project
- **PMT-060** - Products Integration
- **PMT-061** - Task Manager Entity Filling
- **PMT-062** - Tools Collection Matching
- **PMT-063 to PMT-069** - Account Management & Automation

### Utilities (2 prompts)
- **PMT-070** - Entity Identification v1

---

## Naming Conventions

### File Naming Format
```
PMT-{###}_{Descriptive_Name}.md
```

**Examples:**
- `PMT-001_Main_Prompt_v4.md`
- `PMT-004_Video_Transcription_v4.1.md`
- `PMT-058_Call_Organizer_v4.md`

### ID Assignment Rules
1. **Sequential numbering** - PMT-001, PMT-002, PMT-003...
2. **No category prefixes** - Use simple PMT-### (not PMT-VID-###)
3. **Unique IDs** - Each prompt gets one permanent ID
4. **No gaps** - IDs assigned sequentially without skipping

### Version Control
- Include version in filename: `_v{MAJOR}.{MINOR}`
- Active versions marked in master list
- Deprecated versions moved to `_ARCHIVE/`

---

## Department Codes

| Code | Department | Prompt Count |
|------|-----------|--------------|
| **AID** | AI & Automation | 15+ |
| **VID** | Video Production | 12 |
| **Multi** | Multi-Department | 8 |
| **HRM** | Human Resources | 7 |
| **DEV** | Development | 4 |
| **SLS** | Sales | 2 |
| **SMM** | Social Media | 2 |
| **LGN** | Lead Generation | 1 |
| **DGN** | Design | 1 |
| **FIN** | Finance | 1 |
| **MKT** | Marketing | 2 |
| **OPS** | Operations | 3 |

---

## Category Breakdown

| Category | Code | Count | Location |
|----------|------|-------|----------|
| Core System | CORE | 3 | Core/ |
| Video Processing | VIDEO | 12 | Video_Processing/ |
| Daily Reports | REPORTS | 11 | DEPARTMENTS/Daily_Reports/ |
| Taxonomy | TAXONOMY | 7 | SYSTEM/Taxonomy/ |
| System Analysis | SYSTEM | 9 | SYSTEM/ |
| Research | RESEARCH | 9 | RESEARCH/ |
| HR Operations | HR | 5 | DEPARTMENTS/HR_Operations/ |
| Workflows | WORKFLOW | 8 | WORKFLOWS/ |
| Automation | AUTOMATION | 4 | SYSTEM/Automation/ |
| Account Management | ACCOUNT | 3 | WORKFLOWS/Account_Management/ |
| Library Processing | LIBRARY | 3 | WORKFLOWS/Library_Processing/ |
| Updates | UPDATES | 1 | UTILITIES/Daily_Updates/ |

---

## Master Data Files

### PMT_Master_List.csv
**Location:** `DATA_FIELDS/PMT_Master_List.csv`

Complete catalog of all 71 prompts with:
- PMT_ID (unique identifier)
- Entity_Type (always "Prompt")
- Name (descriptive name)
- Description (purpose summary)
- Category (functional category)
- Department (owning department)
- File_Path (relative path from PROMPTS/)
- Status (Active/Draft/Deprecated)
- Version (semantic version)
- Last_Updated (YYYY-MM-DD)

### Prompts_Index.json
**Location:** `DATA_FIELDS/Prompts_Index.json`

Lightweight JSON index for quick lookups and API integration.

---

## Usage Guidelines

### For Developers
1. Reference prompts by PMT-### ID in code
2. Use master CSV for automated prompt loading
3. Check Status field before using (Active/Draft/Deprecated)
4. Always use latest version unless testing

### For Prompt Engineers
1. Create new prompts in appropriate category folder
2. Assign next available PMT-### ID
3. Follow naming convention: `PMT-{###}_{Name}.md`
4. Update `PMT_Master_List.csv` immediately
5. Include metadata header in prompt file

### For Departments
1. Daily reports: Use `DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-{###}_*`
2. Department-specific: Check category folders
3. Request new prompts: Contact AI & Automation team

---

## Version History

### v2.0 - 2025-11-19
- Complete folder reorganization (8 top-level categories)
- Renamed all 71 files with PMT-### IDs
- Created master CSV catalog
- Moved to simple sequential ID system (PMT-### vs PMT-CAT-###)
- Restructured Video Processing with Workflows subfolder
- Moved Daily Reports to DEPARTMENTS
- Consolidated category folders into logical groupings

### v1.0 - 2025-11-18
- Initial PROMPTS entity creation
- Established PMT ISO code
- Created category-based organization
- 70 prompts cataloged

---

## Related Documentation

- **[PMT_Master_List.csv](DATA_FIELDS/PMT_Master_List.csv)** - Complete prompt catalog
- **[Prompts_Index.json](DATA_FIELDS/Prompts_Index.json)** - Lightweight JSON index
- **[Prompts_ISO_Code_Registry.md](SYSTEM/Taxonomy/Prompts_ISO_Code_Registry.md)** - ISO code standards
- **[MIGRATION_LOG.md](_INDEX/MIGRATION_LOG.md)** - Change history

---

## Contact & Support

**Entity Owner:** AI & Automation Department
**Taxonomy Team:** TASK_MANAGERS Integration
**Issues:** Report to system administrators

---

**Document Status:** Active
**Maintenance:** Update when adding/modifying prompts
**Review Schedule:** Monthly audit of active prompts
