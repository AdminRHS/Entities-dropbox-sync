# TASK_MANAGERS Taxonomy Hierarchy Tree

**Generated:** 2025-11-18
**Last Updated:** 2025-11-20
**System:** TASK_MANAGERS Entity Taxonomy
**Total Entities:** 752+ catalogued entities (including 8 TSM meta-categories)

---

## Hierarchical Structure Overview

This document shows parent-child relationships between **Meta-Level Categories (TSM)**, Project Templates, Milestone Templates, Task Templates, Step Templates, Checklist Items, Workflows, Guides, Prompts, and Research entities.

### TSM Meta-Layer Structure

```
TASK_MANAGERS Root
│
├── TSM-001: Project Templates Category (9 PRT instances)
│   └── Contains: PRJ-001 through PRJ-009
│
├── TSM-002: Milestone Templates Category (28 MLT instances)
│   └── Contains: MLS-001 through MLS-028
│
├── TSM-003: Task Templates Category (71 TST instances)
│   └── Contains: TSK-001 through TSK-071
│
├── TSM-004: Step Templates Category (379 STT instances)
│   └── Contains: All step templates organized by department
│
├── TSM-005: Checklist Templates Category (98 CHT instances)
│   └── Contains: All checklist items
│
├── TSM-006: Workflows Category (20 WRF instances)
│   └── Contains: WRF-001 through WRF-020
│
├── TSM-007: Guides Category (8+ GDS instances)
│   └── Contains: GDS-001 through GDS-008+
│
└── TSM-008: Research Category (24+ RSR instances)
    └── Contains: RSR-001 through RSR-024+
    └── Path: ENTITIES/TASK_MANAGERS/RESEARCHES/
    └── Structure:
        ├── 00_SEARCH_QUEUE/ (Search assignment & tracking)
        ├── 01_VIDEO_QUEUE/ (Video accumulation & prioritization)
        ├── 02_TRANSCRIPTIONS/ (23 video transcriptions)
        ├── 03_ANALYSIS/ (Extractions, Gap Analysis, Library Mapping)
        ├── 04_INTEGRATION/ (Integration tracking)
        ├── PROMPTS/ (26 research prompts)
        ├── DATA/ (Research data & metadata)
        ├── REPORTS/ (Research reports)
        └── ARCHIVE/ (Archived content)
```

---

## PROJECT TEMPLATES → MILESTONES → TASKS → STEPS 

### PRJ-001: AI Tutorial Research to Taxonomy Integration

```
PRJ-001 (AI Tutorial Research to Taxonomy Integration)
│
├── MLS-001 (Tutorial Sources Identified - Phase 0-1)
│   ├── TSK-046 (Research AI Platforms)
│   │   └── [Multiple Step Templates - Platform evaluation]
│   └── TSK-048 (Research Other Tools)
│       └── [Multiple Step Templates - Tool discovery]
│
├── MLS-002 (Videos Transcribed - Phase 2)
│   └── TSK-057 (Transcribe Video)
│       ├── STP-001 to STP-010 (Transcription workflow steps)
│       └── [Video processing steps]
│
└── MLS-003 (Taxonomy Enriched - Phase 3-9)
    ├── TSK-049 (Perform Initial Video Analysis)
    │   └── [Analysis step templates]
    ├── TSK-052 (Extract Taxonomy)
    │   └── [Extraction step templates]
    ├── TSK-053 (Validate Taxonomy)
    │   └── [Validation step templates]
    ├── TSK-054 (Validate Tools)
    │   └── [Tool validation steps]
    ├── TSK-055 (Update Mappings)
    │   └── [Mapping update steps]
    ├── TSK-056 (Gap Analysis)
    │   └── [Gap analysis steps]
    └── TSK-058 (Create/Update Tool Entries)
        └── [Tool entry creation steps]
```

---

### PRJ-002: Complete MCP Automation Stack Setup

```
PRJ-002 (Complete MCP Automation Stack Setup)
│
├── MLS-004 (Claude Skills Enabled - Phase 1)
│   └── TSK-011 (Enable Claude Skills Feature)
│       ├── STP-011-01 (Navigate to Claude Desktop settings)
│       └── STP-011-02 (Enable skills toggle)
│
├── MLS-005 (Gmail & Calendar MCP Connectors Generated - Phase 2)
│   └── TSK-008 (Create MCP Connector)
│       ├── STP-008-01 (Open MCP Builder skill)
│       ├── STP-008-02 (Specify Gmail API requirements)
│       ├── STP-008-03 (Generate connector code)
│       ├── STP-008-04 (Specify Calendar API requirements)
│       └── STP-008-05 (Generate calendar connector)
│
├── MLS-006 (Both Connectors Deployed - Phase 3)
│   └── TSK-010 (Deploy MCP Connector Locally)
│       ├── STP-010-01 (Open Cursor AI/VS Code)
│       ├── STP-010-02 (Install dependencies)
│       ├── STP-010-03 (Configure environment variables)
│       ├── STP-010-04 (Test connector locally)
│       └── STP-010-05 (Verify in Claude Desktop)
│
└── MLS-007 (Automation Stack Live - Phase 4)
    ├── TSK-005 (Automate Morning Email Drafting)
    │   ├── STP-005-01 (Configure email response guidelines)
    │   ├── STP-005-02 (Setup morning workflow)
    │   ├── STP-005-03 (Test draft generation)
    │   └── STP-005-04 (Validate time savings)
    └── TSK-022 (Stacked Connector Post Meeting Automation)
        ├── STP-022-01 (Connect Calendar + Gmail)
        ├── STP-022-02 (Define meeting follow-up triggers)
        ├── STP-022-03 (Configure automated email templates)
        ├── STP-022-04 (Test end-to-end workflow)
        └── STP-022-05 (Monitor automation success rate)
```

---

### PRJ-003: Complete HR Automation Implementation

```
PRJ-003 (Complete HR Automation Implementation)
│
├── MLS-008 (CV Screening Automation Operational - Week 1)
│   ├── TSK-039 (Setup n8n for CV Screening)
│   │   ├── STP-039-01 (Create n8n Cloud account - EU datacenter)
│   │   ├── STP-039-02 (Connect Gmail trigger)
│   │   ├── STP-039-03 (Setup Google Sheets output)
│   │   └── STP-039-04 (Build workflow nodes)
│   └── TSK-040 (Configure Gemini AI Analysis)
│       ├── STP-040-01 (Obtain Gemini API key)
│       ├── STP-040-02 (Configure CV Parser v1 prompt)
│       ├── STP-040-03 (Optimize AI parameters)
│       └── STP-040-04 (Test with sample CVs)
│
├── MLS-009 (Complete Recruitment Pipeline - Week 2)
│   ├── TSK-041 (Build Notion ATS Database)
│   │   ├── STP-041-01 (Design database structure - 35 fields)
│   │   ├── STP-041-02 (Configure status pipeline - 9 stages)
│   │   ├── STP-041-03 (Create 7+ database views)
│   │   └── STP-041-04 (Design candidate card template)
│   └── TSK-042 (Setup Interview Scheduling)
│       ├── STP-042-01 (Configure Google Calendar automation)
│       ├── STP-042-02 (Setup calendar event creation)
│       ├── STP-042-03 (Add video meeting links)
│       └── STP-042-04 (Test scheduling workflow)
│
├── MLS-010 (Content Generation Operational - Week 3)
│   └── TSK-043 (Configure LinkedIn Automation)
│       ├── STP-043-01 (Setup Pabbly/Make.com account)
│       ├── STP-043-02 (Create Google Sheets job template)
│       ├── STP-043-03 (Configure AI content generation)
│       ├── STP-043-04 (Connect LinkedIn API)
│       └── STP-043-05 (Test job posting workflow)
│
└── MLS-011 (System Fully Operational - Week 4)
    └── TSK-044 (Setup Onboarding Workflow)
        ├── STP-044-01 (Build onboarding automation)
        ├── STP-044-02 (Configure welcome emails)
        ├── STP-044-03 (Setup Google Drive folder creation)
        ├── STP-044-04 (Create IT request automation)
        └── STP-044-05 (Implement compliance checks)
```

---

### PRJ-004: Complete Lead Generation to Customer Conversion Campaign

```
PRJ-004 (Complete Lead Generation to Customer Conversion)
│
├── MLS-012 (Lead List Generated - Phase 1)
│   └── TSK-014 (Google SERP Lead Generation)
│       ├── STP-014-01 (Define target search queries)
│       ├── STP-014-02 (Configure scraping parameters)
│       ├── STP-014-03 (Execute SERP extraction)
│       ├── STP-014-04 (Validate data quality)
│       └── STP-014-05 (Export to CSV)
│
├── MLS-013 (Emails Enriched - Phase 2)
│   └── TSK-003 (Anymailfinder Nominative Enrichment)
│       ├── STP-003-01 (Upload lead list)
│       ├── STP-003-02 (Configure enrichment settings)
│       ├── STP-003-03 (Execute batch enrichment)
│       ├── STP-003-04 (Verify email formats)
│       └── STP-003-05 (Download enriched data)
│
├── MLS-014 (Old Clients Re-engaged - Phase 3)
│   └── TSK-021 (Send Old Client Email Template)
│       ├── STP-021-01 (Identify dormant clients - 6+ months)
│       ├── STP-021-02 (Segment by previous project type)
│       ├── STP-021-03 (Create personalized templates)
│       ├── STP-021-04 (Execute email campaign)
│       └── STP-021-05 (Log activity in CRM)
│
└── MLS-015 (Automation Stack Live - Phase 4-5)
    └── [Links to TSK-005, TSK-022 from PRJ-002]
```

---

### PRJ-005: Enterprise Account-Based Marketing Campaign

```
PRJ-005 (Enterprise ABM Campaign)
│
├── MLS-016 (Enterprise Directory Unlocked - Phase 1)
│   └── TSK-002 (Airscale Employee Enrichment)
│       ├── STP-002-01 (Identify target company)
│       ├── STP-002-02 (Purchase Airscale credit)
│       ├── STP-002-03 (Unlock employee directory)
│       ├── STP-002-04 (Download employee data)
│       └── STP-002-05 (Identify key decision-makers)
│
├── MLS-017 (All Employees Email-Enriched - Phase 2)
│   └── TSK-003 (Anymailfinder Nominative Enrichment)
│       └── [Same steps as MLS-013]
│
├── MLS-018 (Arbitrage Strategy Executed - Phase 3)
│   └── TSK-012 (Enterprise Email Arbitrage)
│       ├── STP-012-01 (Calculate credit-to-email ratio)
│       ├── STP-012-02 (Execute 1:40 arbitrage strategy)
│       ├── STP-012-03 (Verify email quality)
│       ├── STP-012-04 (Expand contact database)
│       └── STP-012-05 (Generate ROI report)
│
├── MLS-019 (Multi-Contact Outreach Launched - Phase 4)
│   └── TSK-021 (Send Old Client Email Template - adapted for ABM)
│       ├── STP-021-01 (Segment by role: C-level, VP, Director, Manager)
│       ├── STP-021-02 (Create role-specific templates)
│       ├── STP-021-03 (Execute segmented campaigns)
│       ├── STP-021-04 (Track opens and replies)
│       └── STP-021-05 (Update CRM with multi-contact status)
│
└── MLS-020 (Automation Stack Operational - Phase 5)
    └── [Links to TSK-022 from PRJ-002]
```

---

### PRJ-006: Research to Taxonomy Integration Pipeline

```
PRJ-006 (Research to Taxonomy Integration Pipeline)
│
├── MLS-021 (Research Discovery Phase)
│   ├── TSK-046 (Research AI Platforms)
│   ├── TSK-047 (Research Development Tools)
│   └── TSK-048 (Research Other Tools)
│
├── MLS-022 (Video Transcription Phase)
│   ├── TSK-050 (Search Score Videos)
│   ├── TSK-051 (Select Videos)
│   └── TSK-057 (Transcribe Video)
│
├── MLS-023 (Analysis and Extraction Phase)
│   ├── TSK-049 (Perform Initial Video Analysis)
│   ├── TSK-052 (Extract Taxonomy)
│   └── TSK-056 (Gap Analysis)
│
├── MLS-024 (Taxonomy Integration Phase)
│   ├── TSK-053 (Validate Taxonomy)
│   ├── TSK-054 (Validate Tools)
│   ├── TSK-055 (Update Mappings)
│   └── TSK-058 (Create/Update Tool Entries)
│
└── MLS-025 (Reporting and Validation Phase)
    └── [Reporting tasks - documentation creation]
```

---

### PRJ-007: System Analysis

```
PRJ-007 (System Analysis)
│
└── Analysis Tasks
    ├── TSK-023 (File Count Distribution)
    ├── TSK-024 (Folder Structure Mapping)
    ├── TSK-025 (File Size Analysis)
    ├── TSK-026 (Naming Convention Audit)
    ├── TSK-027 (JSON Schema Validation)
    ├── TSK-028 (Version Control Consistency)
    ├── TSK-029 (Duplicate Content Detection)
    ├── TSK-030 (Terminology Extraction)
    ├── TSK-031 (Documentation Completeness)
    ├── TSK-032 (Cross Reference Validation)
    ├── TSK-033 (Index Accuracy Check)
    ├── TSK-034 (Dependency Flow Mapping)
    ├── TSK-035 (Architecture Documentation)
    ├── TSK-036 (Terminology Consolidation)
    ├── TSK-037 (Recommendations Compilation)
    └── TSK-038 (Project Documentation Creation)
```

---

### PRJ-008: VIDEO Production

```
PRJ-008 (VIDEO Production)
│
├── MLS-026 (VIDEO-001 Research Complete)
│   └── TSK-045 (Research AI Video Tools)
│
├── MLS-027 (VIDEO-002 Processing Complete)
│   ├── TSK-050 (Search Score Videos)
│   └── TSK-057 (Transcribe Video)
│
└── MLS-028 (VIDEO-003 Library Population Complete)
    ├── TSK-058 (Create/Update Tool Entries)
    └── [Integration tasks]
```

---

## WORKFLOWS (Standalone Operational Processes)

### Sales & Lead Generation Workflows

```
WRF-001 (Old Client Re-Engagement Workflow)
└── Linked to: TSK-021, PRJ-004 Phase 3

WRF-002 (Lead Enrichment Workflow)
└── Linked to: TSK-003, PRJ-004 Phase 2, PRJ-005 Phase 2
```

### Video & Content Workflows

```
WRF-003 (Content Repurposing Pipeline)
└── Supports: PRJ-008, VID Department

WRF-004 (Cross-Platform Content Distribution)
└── Supports: PRJ-008, VID Department

WRF-005 (Instagram Content Strategy)
└── Supports: Social media content distribution

WRF-008 (YouTube Tutorial Production)
└── Linked to: PRJ-008, TSK-057

WRF-009 (Short-Form Video Production)
└── Supports: PRJ-008, VID Department
```

### Design Workflows

```
WRF-006 (Behance Project Publishing)
└── Linked to: TSK-068, MLS-009

WRF-007 (Dribbble Shot Posting)
└── Supports: DSN Department

WRF-015 (Dribbble Shot Publishing - duplicate variant)
└── Supports: DSN Department

WRF-016 (Instagram Designer Portfolio)
└── Supports: DSN Department
```

### Development Workflows

```
WRF-018 (GitHub Open Source Contribution)
└── Supports: DEV Department

WRF-019 (Stack Overflow Reputation Building)
└── Supports: DEV Department

WRF-020 (Dev.to Technical Blogging)
└── Supports: DEV Department
```

### Marketing & Social Media Workflows

```
WRF-010 (LinkedIn B2B Content Strategy)
└── Linked to: TSK-043, PRJ-003 Phase 3

WRF-011 (Medium Long-Form Publishing)
└── Supports: Content marketing

WRF-012 (Facebook Community Management)
└── Supports: Community engagement

WRF-013 (Twitter Real-Time Engagement)
└── Supports: Social media engagement

WRF-014 (Pinterest Discovery Strategy)
└── Supports: Visual content discovery

WRF-017 (Pinterest Traffic Generation)
└── Supports: Traffic generation
```

---

## GUIDES & DOCUMENTATION

```
GDS-001 (Knowledge Library Guide)
└── Supports: All taxonomy and research work

GDS-002 (Implementation Checklists)
└── Supports: All project implementations

GDS-003 (Designer Integration Summary)
└── Supports: DSN Department, PRJ-008

GDS-004 (Tool Usage Organizational Proposals)
└── Supports: AIA Department, tool management

GDS-005 (CRM Entities LLM Taxonomy Guide)
└── Supports: Taxonomy structure, AIA

GDS-006 (Data Extraction Prompt Guide)
└── Supports: Prompt engineering, AIA

GDS-007 (Framework README)
└── Root documentation for framework

GDS-008 (Taxonomy Guides README)
└── Root documentation for taxonomy system
```

---

## PROMPTS (AI Prompt Library)

```
PRM-001 (Version Control Automation)
└── Supports: AIA Department, automation workflows

PRM-002 (Rules Automation)
└── Supports: AIA Department, business rules

PRM-003 (CV Parser v1)
└── Linked to: TSK-040, PRJ-003 Phase 1

PRM-004 (VS Code Agent HQ Research)
└── Linked to: TSK-047, DEV Department research

PRM-005 (Build Taxonomy ID System)
└── This document's foundation prompt
```

---

## RESEARCH REPORTS

```
RSR-001 (Social Media Strategies for Creative Professionals)
└── Supports: VID Department, social media workflows

RSR-002 to RSR-010 (Video Research 001-009)
└── Linked to: PRJ-001, PRJ-006, TSK-049, TSK-052

RSR-011 (HR Videos Research)
└── Linked to: PRJ-003, HRM automation implementation
```

---

## CROSS-ENTITY RELATIONSHIPS

### Department Integration Patterns

**AI & Automations (AIA)**
- Projects: PRJ-001, PRJ-006, PRJ-007
- Tasks: TSK-005, TSK-022, TSK-023-038, TSK-040, TSK-046-048, TSK-052-056, TSK-058, TSK-062-067
- Workflows: WRF-001, WRF-002
- Guides: GDS-001, GDS-002, GDS-004-008
- Prompts: PRM-001, PRM-002, PRM-005

**Human Resources (HRM)**
- Projects: PRJ-003
- Tasks: TSK-007, TSK-039, TSK-041-042, TSK-044, TSK-071
- Prompts: PRM-003
- Research: RSR-011

**Development (DEV)**
- Projects: PRJ-002
- Tasks: TSK-008, TSK-010-011, TSK-047, TSK-059-061
- Workflows: WRF-018-020
- Prompts: PRM-004

**Lead Generation (LGN)**
- Projects: PRJ-004, PRJ-005
- Tasks: TSK-001-004, TSK-006, TSK-009, TSK-012-018, TSK-043
- Workflows: WRF-002, WRF-010

**Design (DSN)**
- Tasks: TSK-064, TSK-068
- Workflows: WRF-006-007, WRF-015-016
- Guides: GDS-003

**Video Production (VID)**
- Projects: PRJ-008
- Tasks: TSK-045, TSK-049-051, TSK-057
- Workflows: WRF-003-005, WRF-008-009, WRF-011-014, WRF-017
- Research: RSR-001-010

**Sales (SAL)**
- Tasks: TSK-021
- Workflows: WRF-001

---

## DEPENDENCY CHAINS

### Example: Complete Automation Stack Deployment

```
PRJ-002 (MCP Automation Stack)
    ↓
TSK-011 (Enable Claude Skills) → Required for connector generation
    ↓
TSK-008 (Create MCP Connector) → Generates Gmail & Calendar connectors
    ↓
TSK-010 (Deploy MCP Connector) → Deploys both connectors locally
    ↓
TSK-005 (Morning Email Automation) → Uses Gmail connector
    ↓
TSK-022 (Stacked Connector Automation) → Uses both Gmail + Calendar
```

### Example: HR Automation Full Pipeline

```
PRJ-003 (HR Automation)
    ↓
Week 1: TSK-039 (n8n Setup) + TSK-040 (Gemini Config)
    ↓
Week 2: TSK-041 (Notion ATS) + TSK-042 (Interview Scheduling)
    ↓
Week 3: TSK-043 (LinkedIn Automation)
    ↓
Week 4: TSK-044 (Onboarding Workflow) + Compliance & Documentation
```

### Example: Research to Taxonomy Pipeline

```
PRJ-006 (Research Pipeline)
    ↓
TSK-046/047/048 (Research Discovery)
    ↓
TSK-050 (Score Videos) → TSK-051 (Select Videos)
    ↓
TSK-057 (Transcribe Videos)
    ↓
TSK-049 (Initial Analysis) → TSK-052 (Extract Taxonomy)
    ↓
TSK-056 (Gap Analysis)
    ↓
TSK-053/054 (Validate) → TSK-055 (Update Mappings) → TSK-058 (Create Tool Entries)
```

---

## NOTES

1. **Step Templates (STP)**: Not fully enumerated in this tree due to volume (379 total). Each task contains 3-10 step templates following naming pattern: `STP-{TaskID}-{SequenceNumber}`

2. **Checklist Items (CHK)**: 98 checklist items distributed across milestones, organized in batches in 4 JSON files

3. **Deprecated Entities**: TSK-004 (Apollo IO) and TSK-019 (Make.com) marked as deprecated

4. **Department Migrations**: All OPS and ADM entities migrated to AIA per 2025-11-17 consolidation

5. **Hierarchical Depth**: Maximum depth is 5 levels (Project → Milestone → Task → Step → Sub-step)

---

**End of Hierarchy Tree**
