# PROMPTS ISO Code Registry

## Overview
This document defines the ISO code system for Prompts in the TASK_MANAGERS taxonomy. The code `PRM` follows the standard 3-letter consonant-only convention and does NOT end with 'T' as prompts are not templates themselves (they guide template usage).

## ISO Code Definition

### Primary Code
- **Code**: `PRM`
- **Full Name**: Prompts
- **Entity Type**: Operational Guides
- **Description**: AI prompts and custom instructions for taxonomy workflows and operational processes
- **Template Status**: Non-template (no 'T' suffix)

### Code Structure
```
PRM-XXX
│   └── Sequential 3-digit number (001-999)
└── Prompts identifier
```

### Legacy Code Compatibility
Previous naming used category-based subcodes:
- `PRM-VT-XXX` (Video Transcription)
- `PRM-LP-XXX` (Library Processing)
- `PRM-HR-XXX` (HR Operations)
- `PRM-RE-XXX` (Research Prompts)
- `PRM-TI-XXX` (Taxonomy Integration)
- `PRM-OW-XXX` (Operational Workflows)
- `PRM-DR-XXX` (Daily Reports)
- `PRM-CR-XXX` (Core)
- `PRM-TX-XXX` (Taxonomy)
- `PRM-AM-XXX` (Account Management)
- `PRM-AT-XXX` (Automation)
- `PRM-SY-XXX` (System)
- `PRM-AN-XXX` (Analysis)

**Migration**: All legacy IDs preserved in `Current_ID` field of Master_List for backwards compatibility.

## Department Codes

Prompts are distributed across the following departments:

| Code | Department | Count | Description |
|------|------------|-------|-------------|
| **AID** | AI Department | 39 | Taxonomy, video processing, system architecture |
| **HRM** | Human Resources | 10 | Recruitment, CRM, employee management |
| **LGN** | Lead Generation | 4 | Daily reports, marketing content |
| **DEV** | Development | 2 | Development workflows, tools research |
| **DGN** | Design | 1 | Design department daily reports |
| **SLS** | Sales | 2 | Sales research and daily reports |
| **VID** | Video | 1 | Video production daily reports |

## Categorization Scheme

Prompts are organized into 13 functional categories:

### 1. Video_Transcription (VT)
**Prompts**: PRM-001 to PRM-004 (4 prompts)
- Video Transcription Custom Instructions
- Video Naming Business Alternatives
- Video Analysis Prompt
- Objects Library Extraction Prompt

**Purpose**: Process videos to extract taxonomy-relevant content (Phases 1-4)

### 2. Taxonomy_Integration (TI)
**Prompts**: PRM-005 (1 prompt)
- Taxonomy Analysis and Updates Prompt

**Purpose**: Complete taxonomy gap analysis and entity updates (Phases 5-7)

### 3. Library_Processing (LP)
**Prompts**: PRM-006 to PRM-008 (3 prompts)
- Tools Collection and Matching Prompt
- Products Integration Prompt
- Task Manager Entity Filling Prompt

**Purpose**: Specialized prompts for LIBRARIES maintenance and entity filling

### 4. Research_Prompts (RE)
**Prompts**: PRM-009 to PRM-014 (6 prompts)
- VSCode Agent HQ Research Prompt
- YouTube AI HR Tutorials Research Prompt
- YouTube AI Tools Daily Research Prompt
- YouTube HR Automation Research Prompt
- Sales Department Research Prompt
- YouTube Video Research RemoteHelpers Nov2025

**Purpose**: External research, launch tracking, intelligence gathering

### 5. HR_Operations (HR)
**Prompts**: PRM-015 to PRM-019 (5 prompts)
- CV Parser v1
- Communication Templates Prompt
- CRM Data Entry Prompt
- Interview Conductor Prompt
- Job Sites Deep Research Prompt

**Purpose**: HR recruitment workflow automation and candidate management

### 6. Operational_Workflows (OW)
**Prompts**: PRM-020 (1 prompt)
- Document Finished Project

**Purpose**: Cross-functional workflow prompts for project management and documentation

### 7. Daily_Reports (DR)
**Prompts**: PRM-021 to PRM-033 (13 prompts)
- 11 Department-specific daily report prompts (AI, Dev, Design, HR, LG, Marketing, Sales, SMM, Video, Finance, Content)
- Daily Report Collection aggregator
- Enhanced Department Prompt Template

**Purpose**: Daily operational reporting across all departments

### 8. Core (CR)
**Prompts**: PRM-034 to PRM-040 (7 prompts)
- Main Prompt v2 (Deprecated)
- Main Prompt v3 (Deprecated)
- Main Prompt v4 (Active - current production)
- Main Prompt v5 (Active - modular architecture)
- Main Prompt v6 Draft (Draft)
- Create Main Prompt v5
- Reverse Prompt Engineering Analysis

**Purpose**: Core system prompts and main prompt version management

### 9. Taxonomy (TX)
**Prompts**: PRM-041 to PRM-049 (9 prompts)
- Build Taxonomy ID System
- Build Employee Profile Schema Workflow
- Restructure Employee Profile to Task Managers
- Build LIBRARIES Taxonomy
- LIBRARIES Taxonomy Initial ID List
- Optimize Video Transcription Instructions
- Prompts ISO Code Registry
- Taxonomy Entities Collection
- ENTITIES Data Synchronization Architecture (Deprecated)

**Purpose**: Taxonomy system building, standardization, and entity management

### 10. Account_Management (AM)
**Prompts**: PRM-050 to PRM-052 (3 prompts)
- Account Creation Validation
- Account Security Audit
- Subscription Renewal Alert

**Purpose**: Account and subscription management workflows

### 11. Automation (AT)
**Prompts**: PRM-053 (1 prompt)
- Create Script Copy Dailies

**Purpose**: Automation scripts and workflow automation

### 12. System (SY)
**Prompts**: PRM-054 to PRM-061 (8 prompts)
- Data Consistency and Knowledge Integration
- Department Researches Integration
- Folder Reorganization
- Merge Transcriptions and Research Integration
- System Health Review Prompt
- Architecture Merge Planning Prompt
- VSCode AI Extensions Research
- Architecture Learning Guide

**Purpose**: System architecture, integration, and maintenance

### 13. Analysis (AN)
**Prompts**: PRM-062 (1 prompt)
- Prompt Analysis and Improvements

**Purpose**: Analysis and optimization of prompts and workflows

## ID Allocation

### Current Range
- **Allocated**: PRM-001 to PRM-062 (62 prompts)
- **Available**: PRM-063 to PRM-999 (937 IDs remaining)

### Reserved Ranges
- `PRM-001 to PRM-099`: General prompts (current usage)
- `PRM-100 to PRM-199`: Reserved for future department expansions
- `PRM-200 to PRM-299`: Reserved for workflow automation prompts
- `PRM-300 to PRM-399`: Reserved for research and intelligence
- `PRM-400 to PRM-999`: Available for future use

## Status Definitions

| Status | Description | Count |
|--------|-------------|-------|
| **Active** | Currently in production use | 58 |
| **Deprecated** | Superseded by newer versions | 2 |
| **Draft** | Under development, not yet in production | 2 |
| **Archived** | Historical reference only | 0 |

## Naming Conventions

### File Naming
Prompt files follow these naming patterns:
1. **Legacy Format**: `PROMPT_[Name].md`
2. **Category Format**: `[Category]_[Name]_Prompt.md`
3. **Version Format**: `[Name]_v[X].md` or `[Name]_vX.md`

### Standardization Rules
- Use underscores for multi-word names
- Include version numbers for versioned prompts
- Maintain descriptive, human-readable filenames
- Category folders organize related prompts

## Cross-References

### Integration with Other TASK_MANAGERS
Prompts integrate with:
- **Task_Templates (TST)**: Prompts guide task execution workflows
- **Step_Templates (STT)**: Prompts provide step-by-step instructions
- **Workflows (WRF)**: Prompts define workflow execution logic
- **GUIDES (GDS)**: Prompts complement operational guides

### Integration with LIBRARIES
Prompts reference and update:
- **Tools**: Tool discovery and validation (PRM-006)
- **Products**: Product optimization and AI-first alignment (PRM-007)
- **Responsibilities**: Action-object extraction from videos (PRM-001 to PRM-005)
- **Processes**: Workflow documentation and mapping (PRM-003, PRM-005)
- **Professions**: Role identification and skill mapping (PRM-003, PRM-005)

## Usage Guidelines

### When to Create New Prompts
1. New operational workflow requires AI guidance
2. Repetitive task needs standardization
3. Department requests custom daily report template
4. Research process requires structured output
5. System integration needs step-by-step instructions

### Prompt Development Lifecycle
1. **Draft**: Initial creation, testing, refinement
2. **Active**: Production use, maintained and updated
3. **Deprecated**: Superseded but kept for reference
4. **Archived**: Historical record, no longer maintained

### Version Management
- Major changes: Increment version number (v1 → v2)
- Minor updates: Update existing file, document in changelog
- Maintain deprecated versions for backwards compatibility
- Document rationale for version changes

## Quality Standards

### Required Elements
Every prompt must include:
1. **Purpose statement**: What the prompt accomplishes
2. **Input requirements**: What information is needed
3. **Output format**: Expected structure and format
4. **Usage context**: When and how to use the prompt
5. **Examples**: Real-world usage demonstrations
6. **Quality checklist**: Validation criteria

### Documentation Requirements
1. Update PROMPTS_INDEX.json with metadata
2. Add entry to PROMPTS_Master_List.csv
3. Document cross-references to related entities
4. Include version history and changelog
5. Specify workflow phase integration

## Maintenance

### Review Schedule
- **Quarterly**: Review all Active prompts for updates
- **Bi-annually**: Evaluate Deprecated prompts for archival
- **Annually**: Comprehensive taxonomy alignment review

### Update Triggers
1. Workflow changes requiring prompt modifications
2. User feedback indicating improvement opportunities
3. New taxonomy requirements
4. Cross-reference updates in LIBRARIES entities
5. Technology or tool updates

## Related Documentation
- `PROMPTS_Master_List.csv` - Complete prompt inventory
- `PROMPTS_Migration_Map.json` - Legacy ID mappings
- `PROMPTS_Hierarchy_Tree.md` - Categorical organization
- `PROMPTS_Department_Distribution.md` - Department statistics
- `ENTITIES/PROMPTS/PROMPTS_INDEX.json` - Source metadata index
- `ENTITIES/PROMPTS/README.md` - Comprehensive prompts documentation

---

**Last Updated**: 2025-11-19
**Version**: 1.0
**Maintained By**: Taxonomy Team
**Contact**: AI Department (AID)
