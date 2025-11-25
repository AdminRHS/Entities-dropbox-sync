# PROMPTS Hierarchy Tree

## Overview
This document visualizes the categorical organization of all 62 prompts in the TASK_MANAGERS/PROMPTS system. Prompts are organized by functional category and workflow integration.

---

## Complete Hierarchy

```
PROMPTS (PRM) - 62 Total
│
├── Video_Transcription (4 prompts)
│   ├── PRM-001: Video Transcription Custom Instructions
│   ├── PRM-002: Video Naming Business Alternatives
│   ├── PRM-003: Video Analysis Prompt
│   └── PRM-004: Objects Library Extraction Prompt
│
├── Taxonomy_Integration (1 prompt)
│   └── PRM-005: Taxonomy Analysis and Updates Prompt
│
├── Library_Processing (3 prompts)
│   ├── PRM-006: Tools Collection and Matching Prompt
│   ├── PRM-007: Products Integration Prompt
│   └── PRM-008: Task Manager Entity Filling Prompt
│
├── Research_Prompts (6 prompts)
│   ├── PRM-009: VSCode Agent HQ Research Prompt
│   ├── PRM-010: YouTube AI HR Tutorials Research Prompt
│   ├── PRM-011: YouTube AI Tools Daily Research Prompt
│   ├── PRM-012: YouTube HR Automation Research Prompt
│   ├── PRM-013: Sales Department Research Prompt
│   └── PRM-014: YouTube Video Research RemoteHelpers Nov2025
│
├── HR_Operations (5 prompts)
│   ├── PRM-015: CV Parser v1
│   ├── PRM-016: Communication Templates Prompt
│   ├── PRM-017: CRM Data Entry Prompt
│   ├── PRM-018: Interview Conductor Prompt
│   └── PRM-019: Job Sites Deep Research Prompt
│
├── Operational_Workflows (1 prompt)
│   └── PRM-020: Document Finished Project
│
├── Daily_Reports (13 prompts)
│   ├── Department Reports (11 prompts)
│   │   ├── PRM-021: AI Daily Report
│   │   ├── PRM-022: Development Daily Report
│   │   ├── PRM-023: Design Daily Report
│   │   ├── PRM-024: HR Daily Report
│   │   ├── PRM-025: Lead Generation Daily Report
│   │   ├── PRM-026: Marketing Daily Report
│   │   ├── PRM-027: Sales Daily Report
│   │   ├── PRM-028: Social Media Daily Report
│   │   ├── PRM-029: Video Daily Report
│   │   ├── PRM-030: Finance Daily Report
│   │   └── PRM-031: Content Daily Report
│   │
│   ├── Aggregation (1 prompt)
│   │   └── PRM-032: Daily Report Collection
│   │
│   └── Templates (1 prompt)
│       └── PRM-033: Enhanced Department Prompt Template
│
├── Core (7 prompts)
│   ├── Production Versions (2 prompts)
│   │   ├── PRM-036: Main Prompt v4 [Active]
│   │   └── PRM-037: Main Prompt v5 [Active]
│   │
│   ├── Development Versions (1 prompt)
│   │   └── PRM-038: Main Prompt v6 Draft [Draft]
│   │
│   ├── Deprecated Versions (2 prompts)
│   │   ├── PRM-034: Main Prompt v2 [Deprecated]
│   │   └── PRM-035: Main Prompt v3 [Deprecated]
│   │
│   └── Documentation (2 prompts)
│       ├── PRM-039: Create Main Prompt v5
│       └── PRM-040: Reverse Prompt Engineering Analysis
│
├── Taxonomy (9 prompts)
│   ├── System Building (4 prompts)
│   │   ├── PRM-041: Build Taxonomy ID System
│   │   ├── PRM-044: Build LIBRARIES Taxonomy
│   │   ├── PRM-045: LIBRARIES Taxonomy Initial ID List
│   │   └── PRM-048: Taxonomy Entities Collection
│   │
│   ├── Employee Management (2 prompts)
│   │   ├── PRM-042: Build Employee Profile Schema Workflow
│   │   └── PRM-043: Restructure Employee Profile to Task Managers
│   │
│   ├── Optimization (1 prompt)
│   │   └── PRM-046: Optimize Video Transcription Instructions
│   │
│   ├── Standards (1 prompt)
│   │   └── PRM-047: Prompts ISO Code Registry
│   │
│   └── Deprecated (1 prompt)
│       └── PRM-049: ENTITIES Data Synchronization Architecture [Deprecated]
│
├── Account_Management (3 prompts)
│   ├── PRM-050: Account Creation Validation
│   ├── PRM-051: Account Security Audit
│   └── PRM-052: Subscription Renewal Alert
│
├── Automation (1 prompt)
│   └── PRM-053: Create Script Copy Dailies
│
├── System (8 prompts)
│   ├── Integration (4 prompts)
│   │   ├── PRM-054: Data Consistency and Knowledge Integration
│   │   ├── PRM-055: Department Researches Integration
│   │   ├── PRM-056: Folder Reorganization
│   │   └── PRM-057: Merge Transcriptions and Research Integration
│   │
│   ├── Monitoring (1 prompt)
│   │   └── PRM-058: System Health Review Prompt
│   │
│   ├── Architecture (2 prompts)
│   │   ├── PRM-059: Architecture Merge Planning Prompt
│   │   └── PRM-061: Architecture Learning Guide
│   │
│   └── Research (1 prompt)
│       └── PRM-060: VSCode AI Extensions Research
│
└── Analysis (1 prompt)
    └── PRM-062: Prompt Analysis and Improvements
```

---

## Workflow Integration View

### 7-Phase Video Processing Workflow
Complete video-to-taxonomy integration pipeline:

```
Phase 1: Transcription
└── PRM-001: Video Transcription Custom Instructions
    ├── Input: Video audio/captions
    ├── Output: Video_XXX.md with structured transcription
    └── Time: 30-60 minutes

Phase 2: Professional Naming (Optional)
└── PRM-002: Video Naming Business Alternatives
    ├── Input: Casual video title
    ├── Output: Professional title for documentation
    └── Time: 5-10 minutes

Phase 3: Initial Analysis
└── PRM-003: Video Analysis Prompt
    ├── Input: Video_XXX.md
    ├── Output: Taxonomy elements inventory
    └── Time: 45-60 minutes

Phase 4: Objects Extraction
└── PRM-004: Objects Library Extraction Prompt
    ├── Input: Video_XXX.md + Phase 3 results
    ├── Output: Complete object catalog with cross-references
    └── Time: 30-45 minutes

Phases 5-7: Taxonomy Integration
└── PRM-005: Taxonomy Analysis and Updates Prompt
    ├── Phase 5: Gap Analysis (30-45 min)
    ├── Phase 6: Taxonomy Updates (60-90 min)
    ├── Phase 7: Reporting (20-30 min)
    └── Output: Updated LIBRARIES + Video_XXX_Library_Mapping_Report.md
```
**Total Workflow Time**: 3.5-5.5 hours

---

### HR Recruitment Workflow
Complete candidate recruitment from search to onboarding:

```
Stages 1-5: Search & Pre-Screening
└── PRM-016: Communication Templates Prompt
    ├── Initial contact
    ├── 5 pre-screening questions
    ├── Company introduction
    └── Time: 30-45 minutes per candidate

Stages 6-9: Resume Processing & CRM Entry
├── PRM-015: CV Parser v1
│   ├── Extract 21 fields from resume
│   └── Generate TSV format
│
└── PRM-017: CRM Data Entry Prompt
    ├── Google Sheets buffer workflow
    ├── Browser extension usage
    ├── Video/test upload procedures
    └── Time: 20-30 minutes (15-20 min saved via automation)

Stages 10-12: Interview Planning & Execution
└── PRM-018: Interview Conductor Prompt
    ├── Schedule group interview
    ├── Conduct 5-phase interview
    ├── Evaluate candidates (4 criteria)
    └── Time: 60-90 minutes per interview group (2-4 candidates)

Stages 13-16: Contracts & Onboarding
└── PRM-018: Interview Conductor Prompt (cont.)
    ├── Send Regular contract (9-step process)
    ├── Collect documents
    ├── Onboard employee
    ├── Discord setup
    └── Time: 45-60 minutes per employee
```
**Total Workflow Time**: 2.5-3.5 hours per candidate
**Automation Savings**: 15-20 minutes per candidate

---

### Library Maintenance Workflows

#### Tool Discovery & Validation
```
PRM-006: Tools Collection and Matching Prompt
├── Source Discovery
│   ├── TASK_MANAGERS analysis
│   ├── Video transcriptions
│   └── Documentation scanning
│
├── Validation Process
│   ├── Tool existence verification
│   ├── Usage context enrichment
│   └── Cross-referencing
│
└── Output
    ├── Validated tool JSON files
    ├── Tools library updates
    └── Time: 30-60 minutes per batch
```

#### Product Processing
```
PRM-007: Products Integration Prompt
├── Input
│   └── Raw product lists (ID, name, description, hours, price)
│
├── Processing
│   ├── AI-first tool substitution
│   ├── Optimization methodology
│   └── Cross-referencing with LIBRARIES
│
└── Output
    ├── Structured JSON with AI-first focus
    ├── Cross-references to tools/skills/professions/services
    └── Time: 15-30 minutes per product
```

---

## Department View

### AI Department (AID) - 39 Prompts
```
Video Processing & Taxonomy (5)
├── PRM-001: Video Transcription Custom Instructions
├── PRM-002: Video Naming Business Alternatives
├── PRM-003: Video Analysis Prompt
├── PRM-004: Objects Library Extraction Prompt
└── PRM-005: Taxonomy Analysis and Updates Prompt

Library Processing (3)
├── PRM-006: Tools Collection and Matching Prompt
├── PRM-007: Products Integration Prompt
└── PRM-008: Task Manager Entity Filling Prompt

Research (2)
├── PRM-009: VSCode Agent HQ Research Prompt
└── PRM-011: YouTube AI Tools Daily Research Prompt

Daily Reports (2)
├── PRM-021: AI Daily Report
└── PRM-030: Finance Daily Report

Core System (7)
├── PRM-032: Daily Report Collection
├── PRM-033: Enhanced Department Prompt Template
├── PRM-036: Main Prompt v4
├── PRM-037: Main Prompt v5
├── PRM-038: Main Prompt v6 Draft
├── PRM-039: Create Main Prompt v5
└── PRM-040: Reverse Prompt Engineering Analysis

Taxonomy System (8)
├── PRM-041: Build Taxonomy ID System
├── PRM-044: Build LIBRARIES Taxonomy
├── PRM-045: LIBRARIES Taxonomy Initial ID List
├── PRM-046: Optimize Video Transcription Instructions
├── PRM-047: Prompts ISO Code Registry
├── PRM-048: Taxonomy Entities Collection
├── PRM-050: Account Creation Validation
├── PRM-051: Account Security Audit

System Architecture (8)
├── PRM-052: Subscription Renewal Alert
├── PRM-053: Create Script Copy Dailies
├── PRM-054: Data Consistency and Knowledge Integration
├── PRM-055: Department Researches Integration
├── PRM-056: Folder Reorganization
├── PRM-057: Merge Transcriptions and Research Integration
├── PRM-058: System Health Review Prompt
├── PRM-059: Architecture Merge Planning Prompt
├── PRM-061: Architecture Learning Guide
└── PRM-062: Prompt Analysis and Improvements
```

### Human Resources (HRM) - 10 Prompts
```
HR Operations (5)
├── PRM-015: CV Parser v1
├── PRM-016: Communication Templates Prompt
├── PRM-017: CRM Data Entry Prompt
├── PRM-018: Interview Conductor Prompt
└── PRM-019: Job Sites Deep Research Prompt

Research (2)
├── PRM-010: YouTube AI HR Tutorials Research Prompt
└── PRM-012: YouTube HR Automation Research Prompt

Daily Reports (1)
└── PRM-024: HR Daily Report

Employee Management (2)
├── PRM-042: Build Employee Profile Schema Workflow
└── PRM-043: Restructure Employee Profile to Task Managers
```

### Lead Generation (LGN) - 4 Prompts
```
Daily Reports (4)
├── PRM-025: Lead Generation Daily Report
├── PRM-026: Marketing Daily Report
├── PRM-028: Social Media Daily Report
└── PRM-031: Content Daily Report
```

### Sales (SLS) - 2 Prompts
```
Research (1)
└── PRM-013: Sales Department Research Prompt

Daily Reports (1)
└── PRM-027: Sales Daily Report
```

### Development (DEV) - 2 Prompts
```
Daily Reports (1)
└── PRM-022: Development Daily Report

Research (1)
└── PRM-060: VSCode AI Extensions Research
```

### Design (DGN) - 1 Prompt
```
Daily Reports (1)
└── PRM-023: Design Daily Report
```

### Video (VID) - 1 Prompt
```
Daily Reports (1)
└── PRM-029: Video Daily Report
```

---

## Status Distribution

### Active Prompts (58)
Production-ready prompts currently in use across all workflows.

### Deprecated Prompts (2)
Superseded by newer versions but maintained for reference:
- PRM-034: Main Prompt v2
- PRM-035: Main Prompt v3
- PRM-049: ENTITIES Data Synchronization Architecture

### Draft Prompts (2)
Under development, not yet in production:
- PRM-038: Main Prompt v6 Draft

---

## Cross-Reference Mapping

### Prompts → Task Templates
```
PRM-015 (CV Parser) → TASK-TEMPLATE-HR-006
PRM-016 (Communication) → TASK-TEMPLATE-HR-002, HR-003, HR-016
PRM-017 (CRM Entry) → TASK-TEMPLATE-HR-006, HR-007, HR-008
PRM-018 (Interview) → TASK-TEMPLATE-HR-012, HR-013, HR-015
```

### Prompts → LIBRARIES
```
Video Processing Prompts (PRM-001 to PRM-005)
├── Actions → Responsibilities/Actions/Actions_Master.json
├── Objects → Responsibilities/Objects/Design_Deliverables.json, Documents.json
├── Tools → Tools/AI_Tools/[individual tool files]
├── Processes → Processes_Master.json
├── Professions → professions.json
└── Skills → skills_library.json

Library Processing Prompts (PRM-006 to PRM-008)
├── Tools → Tools library maintenance
├── Products → Products_Master.json optimization
└── Responsibilities → Action-object pairing derivation
```

---

## Usage Patterns

### High-Frequency Prompts
Daily or weekly usage:
- PRM-021 to PRM-031: Daily Reports (11 department prompts)
- PRM-015 to PRM-018: HR Operations (recruitment workflow)
- PRM-036, PRM-037: Core System Prompts (production)

### Medium-Frequency Prompts
Ad-hoc or monthly usage:
- PRM-001 to PRM-005: Video Processing (when new videos analyzed)
- PRM-006, PRM-007: Library Processing (maintenance cycles)
- PRM-009 to PRM-014: Research Prompts (research sessions)

### Low-Frequency Prompts
Infrequent or one-time usage:
- PRM-041 to PRM-048: Taxonomy Building (system development)
- PRM-050 to PRM-052: Account Management (as needed)
- PRM-054 to PRM-061: System Architecture (migrations, refactoring)

---

**Last Updated**: 2025-11-19
**Total Prompts**: 62
**Categories**: 13
**Departments**: 7
**Version**: 1.0
