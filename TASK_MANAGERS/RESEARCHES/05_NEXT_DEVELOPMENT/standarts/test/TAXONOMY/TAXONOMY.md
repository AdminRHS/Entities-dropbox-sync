---
category: TAXONOMY
subcategory: root
type: taxonomy
source_id: TAXONOMY
title: TAXONOMY
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# TAXONOMY

## Summary
- TODO

## Context
- TODO

## Data / Content
# RESEARCHES Entity Taxonomy

## 1. Entity Description

**Entity Name:** RESEARCHES
**Entity Code:** RSH
**Root Path:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\`
**Created:** 2025-11-20

### Purpose
RESEARCHES serves as the central repository for all research artifacts, investigations, and knowledge synthesis across the ENTITIES ecosystem. It consolidates exploratory work, gap analyses, and structured findings that inform decision-making.

### Department Coverage

| Code | Department | Description |
|------|------------|-------------|
| AI | Artificial Intelligence | AI/ML research, model evaluations, automation studies |
| LGN | Learning & Growth Notes | Learning research, knowledge synthesis, educational content |
| VID | Video | Video processing, influencer tracking, SMM research |
| DEV | Development | Tooling, architecture, technical research |

---

## 2. Sub-Entity: VIDEO_RESEARCHES

**Sub-Entity Name:** VIDEO_RESEARCHES
**Sub-Entity Code:** RSH-VID
**Path:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\`

### Scope
VIDEO_RESEARCHES consolidates all video-related research including:
- Video processing tools and workflow research
- SMM/Influencer tracking and performance studies
- Content analysis methodologies
- Transcription and caption research
- Platform-specific video optimization studies

### Typical Use Cases
1. Evaluating new video processing tools
2. Analyzing influencer performance trends
3. Optimizing video workflows
4. Researching platform algorithm changes
5. Conducting gap analyses for video capabilities

### Directory Structure
```
RESEARCHES/
├── 00_PHASES/               # Phase system documentation (NEW - 2025-11-21)
│   ├── Phase_System_Overview.md
│   └── Phase_1-7 documentation
├── 01_QUEUE/                # Unified queue system (CONSOLIDATED - 2025-11-21)
│   ├── video_queue_manager.py
│   ├── Video_Queue_Tracker.md
│   ├── Transcription_Queue.md
│   └── Queue_System_README.md
├── 02_TRANSCRIPTIONS/       # All video transcriptions (FROM REPORTS/Videos)
│   ├── Video_001 - Video_018.md (22 files)
│   ├── VIDEOS_INDEX.md
│   ├── Video_Discovery_Pipeline.md
│   └── README.md
├── 03_ANALYSIS/             # All analysis outputs (CONSOLIDATED)
│   ├── Library_Mapping/     # Phase 7 reports
│   ├── Gap_Analysis/        # Phase 5 outputs
│   ├── Extractions/         # Phase 4 outputs
│   ├── Phase_Reports/       # Completion reports
│   └── Validation/          # Validation reports
├── 04_INFLUENCER_DATA/      # SMM data (FROM REPORTS/Influencer_Tracking)
│   ├── Influencer_Database.json
│   ├── YouTube_Channels.json
│   └── README.md
├── Video_Processing/        # Methodology (Migrated from PROMPTS)
│   ├── Analysis/            # PMT-006, 007, 008, 071
│   ├── Transcription/       # PMT-004, 005
│   ├── Taxonomy_Integration/# PMT-009
│   └── Workflows/           # PMT-010, 011, 012, 090
├── PROMPTS/                 # Research-specific prompts
├── REPORTS/                 # Final research outputs
├── DATA/                    # Structured data (JSON, CSV)
├── MAPPINGS/                # Entity relationship mappings
└── ARCHIVE/                 # Outdated versions
```

---

## 2.2 Sub-Entity: RESEARCH_PROMPTS

**Sub-Entity Name:** RESEARCH_PROMPTS
**Path:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\RESEARCH_PROMPTS\`

### Scope
RESEARCH_PROMPTS consolidates department-specific research prompts including:
- YouTube research for AI tools, design, HR, and management
- Platform research (VSCode, development tools)
- Course creation and educational content research
- SMM and sales department research

### Department Organization
```
RESEARCH_PROMPTS/
├── Department_Integration/  # PMT-051 (cross-department integration)
├── Sales/                   # PMT-044 (sales research)
├── Design/                  # PMT-051, 052, 085, 093 (design AI research)
├── HR/                      # PMT-047, 049, 050, 052 (HR & management)
├── AI_Tools/                # PMT-048, 089 (daily AI research)
├── Development/             # PMT-046, 052 (VSCode, tools)
├── Course_Creation/         # PMT-082, 083 (courses)
└── SMM/                     # PMT-045 (SMM processing)
```

### PMT-ID Mapping

| Department | PMT IDs | Focus Area |
|------------|---------|------------|
| Department_Integration | PMT-051 | LIBRARIES/Researches integration |
| Sales | PMT-044 | Sales tools, CRM, SMM strategies |
| Design | PMT-051, 052, 085, 093 | Design AI tools, photo editing, video discovery |
| HR | PMT-047, 049, 050, 052 | HR automation, management, leadership workflows |
| AI_Tools | PMT-048, 089 | Daily AI tool discovery, tutorials |
| Development | PMT-046, 052 | VSCode extensions, Agent HQ |
| Course_Creation | PMT-082, 083 | Advanced prompting, GenSpark courses |
| SMM | PMT-045 | SMM document processing |

---

## 3. ID System & Naming Rules

### ID Prefixes

| Level | Prefix | Pattern | Example |
|-------|--------|---------|---------|
| Entity | RSH | RSH-{DEPT}-### | RSH-AI-001 |
| VIDEO_RESEARCHES | RSH-VID | RSH-VID-### | RSH-VID-001 |

### File Naming Conventions

**Prompts:**
```
RSH-VID-###_Research_Title.md
Example: RSH-VID-001_Video_Tool_Comparison.md
```

**Reports:**
```
RSH-VID-###_Report_Type_Description.md
Example: RSH-VID-002_Gap_Analysis_Transcription_Tools.md
```

**Data Files:**
```
RSH-VID-###_Data_Type_YYYY-MM-DD.{ext}
Example: RSH-VID-003_Influencer_Metrics_2025-11-20.csv
```

---

## 4. Entity References & Integration

### Source Integration Points

**VIDEO_RESEARCHES** integrated content from:

| Source Path | Content Type | Integration Status | New Location |
|-------------|--------------|-------------------|--------------|
| `PROMPTS/Video_Processing/` | Workflow prompts | **MIGRATED** | `RESEARCHES/Video_Processing/` |
| `REPORTS/Influencer_Tracking/` | SMM data & reports | Reference/Analyze | Referenced in DATA |
| `REPORTS/Videos/` | Video analysis outputs | Reference | Linked in MAPPINGS |

**RESEARCH_PROMPTS** integrated content from:

| Source Path | Content Type | Integration Status | New Location |
|-------------|--------------|-------------------|--------------|
| `PROMPTS/RESEARCH/` | Research prompts | **MIGRATED** | `RESEARCH_PROMPTS/{Department}/` |
| `PROMPTS/RESEARCH/Research_Prompts/` | Department prompts | **MIGRATED** | `RESEARCH_PROMPTS/{Department}/` |

### Cross-Entity Relationships

**REPORTS (RPT)**
- RESEARCHES provides raw material and analysis
- REPORTS contains finalized, published outputs
- Link via: `RPT-VID-###` references in research docs

**TASK_MANAGERS (TSK)**
- Research tasks tracked in TASK_MANAGERS
- Research findings inform task priorities
- Link via: Task IDs in report follow-up sections

**LIBRARIES (LIB)**
- Research identifies tools that become LIBRARIES entries
- Link via: `LIB/Tools/` references

**PROMPTS (PMT)**
- Research informs prompt design
- Prompts generate research outputs
- Link via: `PMT-VID-###` references

---

## 5. Quality Standards

### Research Document Requirements
- Clear objective statement
- Defined data sources
- Methodology description
- Structured findings
- Actionable recommendations
- Entity cross-references

### Naming Compliance
- All files must use RSH-{DEPT}-### prefix
- Dates in YYYY-MM-DD format
- Descriptive titles in Title_Case

---

*Taxonomy established: 2025-11-20*
*Updated with Video_Processing & RESEARCH_PROMPTS migration: 2025-11-21*


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
