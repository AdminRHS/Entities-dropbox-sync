# ID Master Registry - RESEARCHES System

**Document ID:** DOC-RES-017
**Version:** 1.0
**Date:** 2025-12-10
**Status:** ✅ Active Registry
**Last Updated:** 2025-12-10
**Purpose:** Complete registry of all ID namespaces and their current ranges

---

## Overview

This document serves as the **master registry** for all ID systems used across the RESEARCHES module and its integration with the ENTITIES taxonomy. It provides a single source of truth for:

- Current ID ranges in use
- Next available IDs for each namespace
- Cross-references between ID systems
- Integration points with ENTITIES taxonomy

---

## Quick Reference: Active ID Ranges

### RESEARCHES Module (Module-Specific)

| ID Type | Format | Current Range | Next Available | Status | Location |
|---------|--------|---------------|----------------|--------|----------|
| **Videos** | `Video_XXX` | 001-028 | Video_029 | ⚠️ Gap at 015 | `02_TRANSCRIPTIONS/` |
| **Video Queue** | `VQ-XXX` | 001-042 | VQ-043 | ✅ Active | `01_VIDEO_QUEUE/Video_Queue_Master.csv` |
| **Search Queue** | `SEARCH-XXX` | 001-015 | SEARCH-016 | ✅ Active | `00_SEARCH_QUEUE/Search_Queue_Master.csv` |
| **Documents** | `DOC-RES-XXX` | 001-017 | DOC-RES-018 | ✅ Active | `documentation/` |
| **Issues** | `ISS-RES-XXX` | 001-012 | ISS-RES-013 | ✅ Active | `documentation/issues/` |
| **Phases** | `PHS-RES-XXX` | 001-009 | N/A (Fixed) | ✅ Complete | `documentation/phases/` |
| **Changes** | `CHG-RES-YYYYMMDD-XXX` | Various by date | Daily reset | ✅ Active | `documentation/changelog/` |
| **Research Taxonomy** | `RSH-TAX-XXX` | 001 | RSH-TAX-002 | ✅ Active | `documentation/taxonomy/` |

### Global Namespaces (Cross-Module)

| ID Type | Format | Current Range | Next Available | Status | Location |
|---------|--------|---------------|----------------|--------|----------|
| **Tasks** | `TASK-XXX` | 001-042 | TASK-043 | ✅ Active | `documentation/phases/` |
| **Skills** | `SKL-XXX` | 001-066 | SKL-067 | ✅ Active | `ENTITIES/TALENTS/Skills/` |
| **Professions** | `PRF-XXX` | 001-015 | PRF-016 | ✅ Active | `ENTITIES/TALENTS/Professions/` |

### ENTITIES Libraries (Categorized)

| ID Type | Format | Current Range | Next Available | Status | Location |
|---------|--------|---------------|----------------|--------|----------|
| **Workflows** | `WRF-XXX` or `WRF-{CAT}-XXX` | 001-041 | WRF-042 | ✅ Active | `ENTITIES/TASK_MANAGERS/TSM-006_Workflows/` |
| **Tools (AI)** | `TOL-AI-XXX` | 001-224 | TOL-AI-225 | ✅ Active | `ENTITIES/LIBRARIES/LBS_003_Tools/` |
| **Tools (Video)** | `TOL-VID-XXX` | 001-042 | TOL-VID-043 | ✅ Active | `ENTITIES/LIBRARIES/LBS_003_Tools/` |
| **Objects (SMM)** | `OBJ-SMM-XXX` | 001-016 | OBJ-SMM-017 | ✅ Active | `ENTITIES/LIBRARIES/Responsibilities/Objects/` |
| **Research Entities** | `RSR-XXX` | 001-024 | RSR-025 | ✅ Active | `ENTITIES/TASK_MANAGERS/RESEARCHES/` |

---

## Detailed Registry by ID Type

### 1. Video IDs (`Video_XXX`)

**Format:** `Video_XXX`
**Range:** 001-999
**Separator:** Underscore `_` (legacy format)
**Zero-padding:** 3 digits

**Current Status:**
- **Total Videos:** 28 (Video_001 through Video_028)
- **Gap:** Video_015 is missing
- **Next Available:** Video_029

**Active Videos:**
```
Video_001 ✅  Video_002 ✅  Video_003 ✅  Video_004 ✅  Video_005 ✅
Video_006 ✅  Video_007 ✅  Video_008 ✅  Video_009 ✅  Video_010 ✅
Video_011 ✅  Video_012 ✅  Video_013 ✅  Video_014 ✅  Video_015 ❌ MISSING
Video_016 ✅  Video_017 ✅  Video_018 ✅  Video_019 ✅  Video_020 ✅
Video_021 ✅  Video_022 ✅  Video_023 ✅  Video_024 ✅  Video_025 ✅
Video_026 ✅  Video_027 ✅  Video_028 ✅
```

**Migration Note:** New videos may use `Video-XXX` (hyphen) format for consistency with other IDs, but `Video_XXX` (underscore) remains the official format for backward compatibility.

**Related Files:**
- `02_TRANSCRIPTIONS/Video_XXX.md` (transcriptions)
- `03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md`
- `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`
- `VIDEO_PROGRESS_TRACKER.csv`

---

### 2. Video Queue IDs (`VQ-XXX`)

**Format:** `VQ-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Queue Items:** 42
- **Next Available:** VQ-043

**Active Range:** VQ-001 through VQ-042

**CSV Schema:**
```csv
Queue_ID, Video_ID, Video_Title, Channel_Name, Video_URL, Views, Likes,
Duration, Added_By, Added_Date, Status, Priority_Score, Topic_Category
```

**Related Files:**
- `01_VIDEO_QUEUE/Video_Queue_Master.csv`
- `01_VIDEO_QUEUE/Video_Queue_Dashboard.html`

---

### 3. Search Queue IDs (`SEARCH-XXX`)

**Format:** `SEARCH-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Search Tasks:** 15
- **Next Available:** SEARCH-016

**Active Range:** SEARCH-001 through SEARCH-015

**CSV Schema:**
```csv
Search_ID, Employee, Department, Topic, Search_Query, Assigned_Date,
Status, Videos_Found, Completed_Date, Notes
```

**Related Files:**
- `00_SEARCH_QUEUE/Search_Queue_Master.csv`

---

### 4. Document IDs (`DOC-RES-XXX`)

**Format:** `DOC-RES-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Documents:** 17 (including this document)
- **Next Available:** DOC-RES-018

**Active Documents:**
```
DOC-RES-001: 01_Executive_Summary.md
DOC-RES-002: 02_Technical_Report.md
DOC-RES-003: 03_System_Architecture.md
DOC-RES-004: 04_ID_System_Standard.md
DOC-RES-005: 05_Workflow_Diagrams.md
DOC-RES-006: 06_Issues_Registry.md
DOC-RES-007: 07_Development_Roadmap.md
DOC-RES-008: 08_Phase_Prompts_V1.md
DOC-RES-009: 09_Phase_Prompts_V2_V3.md
DOC-RES-010: 10_Employee_Onboarding_Guide.md
DOC-RES-011: 11_Day1_Quick_Start.md
DOC-RES-012: 12_Week1_Practice.md
DOC-RES-013: 13_Month1_Mastery.md
DOC-RES-014: 14_Changelog_System.md
DOC-RES-015: 15_Master_Index.md
DOC-RES-016: README.md
DOC-RES-017: ID_MASTER_REGISTRY.md (this document)
```

**Related Files:**
- All files in `documentation/` folder

---

### 5. Issue IDs (`ISS-RES-XXX`)

**Format:** `ISS-RES-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Issues:** 12
- **Next Available:** ISS-RES-013

**Status Breakdown:**
- **OPEN:** 10 issues
- **RESOLVED:** 2 issues (ISS-RES-011, ISS-RES-012)

**Priority Breakdown:**
- **HIGH:** 5 issues (ISS-RES-001, ISS-RES-005, ISS-RES-010, ISS-RES-011✅, ISS-RES-012✅)
- **MEDIUM:** 5 issues
- **LOW:** 2 issues

**Active Issues:**
```
ISS-RES-001: VIDEO_PROGRESS_TRACKER Desynchronization (HIGH, OPEN)
ISS-RES-002: Missing Video_015 (LOW, OPEN)
ISS-RES-003: Conflicting Files (MEDIUM, OPEN)
ISS-RES-004: Missing Progress Dashboard (MEDIUM, OPEN)
ISS-RES-005: Non-Automated Phase 2 (HIGH, OPEN)
ISS-RES-006: Missing Batch Processing (MEDIUM, OPEN)
ISS-RES-007: JSON Files Without Pretty Formatting (LOW, OPEN)
ISS-RES-008: Missing YouTube API Integration (MEDIUM, OPEN)
ISS-RES-009: No ML for Prioritization (MEDIUM, OPEN)
ISS-RES-010: Missing Tests (HIGH, OPEN)
ISS-RES-011: Missing Unified ID System (HIGH, RESOLVED) ✅
ISS-RES-012: Missing Changelog System (HIGH, RESOLVED) ✅
```

**Related Files:**
- `documentation/issues/06_Issues_Registry.md`

---

### 6. Phase IDs (`PHS-RES-XXX`)

**Format:** `PHS-RES-XXX`
**Range:** 001-009 (FIXED)
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Phases:** 9 (complete set, fixed range)
- **Next Available:** N/A (fixed set)

**Phase Structure:**

**Version 1.0 (Phases 1-3):**
```
PHS-RES-001: Stabilization
PHS-RES-002: Automation Enhancement
PHS-RES-003: Monitoring & Dashboards
```

**Version 2.0 (Phases 4-6):**
```
PHS-RES-004: Quality Assurance
PHS-RES-005: AI/ML Integration
PHS-RES-006: Multi-Source Integration
```

**Version 3.0 (Phases 7-9):**
```
PHS-RES-007: Collaboration Features
PHS-RES-008: Advanced Analytics
PHS-RES-009: Documentation & Knowledge Base
```

**Related Files:**
- `documentation/phases/07_Development_Roadmap.md`

---

### 7. Task IDs (`TASK-XXX`)

**Format:** `TASK-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits
**Namespace:** Global (not module-specific)

**Current Status:**
- **Total Tasks:** 42
- **Next Available:** TASK-043

**Version Distribution:**
- **v1.0 Tasks:** TASK-001 to TASK-013 (detailed)
- **v2.0 Tasks:** TASK-014 to TASK-030 (conceptual)
- **v3.0 Tasks:** TASK-031 to TASK-042 (conceptual)

**Sample Tasks:**
```
TASK-001: Update VIDEO_PROGRESS_TRACKER.csv (PHS-RES-001)
TASK-002: Resolve PMT-051 conflict (PHS-RES-001)
TASK-003: Create backup of all CSV (PHS-RES-001)
TASK-006: Create video_extraction_automator.py (PHS-RES-002)
TASK-010: Create Progress_Dashboard.html (PHS-RES-003)
...
TASK-042: Knowledge base integration (PHS-RES-009)
```

**Related Files:**
- `documentation/phases/07_Development_Roadmap.md`
- `documentation/phases/08_Phase_Prompts_V1.md`
- `documentation/phases/09_Phase_Prompts_V2_V3.md`

---

### 8. Change IDs (`CHG-RES-YYYYMMDD-XXX`)

**Format:** `CHG-RES-YYYYMMDD-XXX`
**Range:** 001-999 per day
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits for daily sequence
**Date Format:** YYYYMMDD (ISO 8601)

**Current Status:**
- **Latest Change:** CHG-RES-20251203-001
- **Next Available:** CHG-RES-20251210-001 (for today)

**Recent Changes:**
```
CHG-RES-20251203-001: Documentation package creation (16 files)
CHG-RES-20251124-002: Status verification
CHG-RES-20251124-001: Phase restructure
```

**Change Categories:**
- `FEATURE` - New functionality
- `BUGFIX` - Bug fix
- `IMPROVEMENT` - Enhancement
- `DOCS` - Documentation
- `REFACTOR` - Code refactoring
- `DEPRECATED` - Deprecated functionality

**Related Files:**
- `documentation/changelog/14_Changelog_System.md`

---

### 9. Research Taxonomy IDs (`RSH-TAX-XXX`)

**Format:** `RSH-TAX-XXX`
**Range:** 001-999
**Separator:** Hyphen `-`
**Zero-padding:** 3 digits

**Current Status:**
- **Total Taxonomy Analyses:** 1
- **Next Available:** RSH-TAX-002

**Active Documents:**
```
RSH-TAX-001: Complete Taxonomy Analysis
```

**Related Files:**
- `documentation/taxonomy/RSH-TAX-001_Complete_Taxonomy_Analysis.md`

---

## ENTITIES Integration

### Global Namespaces

#### Skills (`SKL-XXX`)

**Format:** `SKL-XXX`
**Range:** 001-999
**Current:** SKL-001 to SKL-066
**Next:** SKL-067

**Location:** `ENTITIES/TALENTS/Skills/Master/all_skills.json`

**Examples:**
- SKL-042: Video Editing
- SKL-065: AI Prompt Engineering
- SKL-063: HTML Parsing via OpenAI

---

#### Professions (`PRF-XXX`)

**Format:** `PRF-XXX`
**Range:** 001-999
**Current:** PRF-001 to PRF-015
**Next:** PRF-016

**Location:** `ENTITIES/TALENTS/Professions/`

**Examples:**
- PRF-003: Graphic Designer
- PRF-015: AI Engineer

---

#### Tasks (Global) (`TASK-XXX`)

**Format:** `TASK-XXX`
**Range:** 001-999
**Current:** TASK-001 to TASK-042
**Next:** TASK-043

**Note:** Tasks are global and can be used across all modules.

---

### Categorized Namespaces

#### Workflows (`WRF-{CAT}-XXX`)

**Format:** `WRF-XXX` or `WRF-{CAT}-XXX`
**Range:** 001-999 per category
**Current:** WRF-001 to WRF-041
**Next:** WRF-042

**Categories:**
- General: `WRF-XXX`
- Security: `WRF-SEC-XXX`
- Design: `WRF-DGN-XXX`
- Development: `WRF-DEV-XXX`

**Location:** `ENTITIES/TASK_MANAGERS/TSM-006_Workflows/`

**Examples:**
- WRF-025: Create Social Media Caption
- WRF-SEC-014: Secure OAuth Implementation

---

#### Tools (`TOL-{CAT}-XXX`)

**Format:** `TOL-{CAT}-XXX` or `TOOL-{CAT}-XXX`
**Range:** 001-999 per category
**Next:** TOL-AI-225, TOL-VID-043

**Categories:**
- AI: `TOL-AI-XXX` (current: TOL-AI-224)
- Video: `TOL-VID-XXX` (current: TOL-VID-042)
- Design: `TOL-DGN-XXX`
- Automation: `TOL-AUT-XXX`
- Development: `TOL-DEV-XXX`

**Location:** `ENTITIES/LIBRARIES/LBS_003_Tools/`

**Examples:**
- TOL-AI-223: Browse AI
- TOL-VID-042: Final Cut Pro

---

#### Objects (`OBJ-{CAT}-XXX`)

**Format:** `OBJ-{CAT}-XXX`
**Range:** 001-999 per category
**Next:** OBJ-SMM-017

**Categories:**
- Social Media: `OBJ-SMM-XXX` (current: OBJ-SMM-016)
- Video: `OBJ-VID-XXX`
- Security: `OBJ-SEC-XXX`
- General: `OBJ-XXX`

**Location:** `ENTITIES/LIBRARIES/Responsibilities/Objects/`

**Examples:**
- OBJ-SMM-015: Instagram Caption
- OBJ-VID-008: Video Thumbnail

---

#### Research Entities (`RSR-XXX`)

**Format:** `RSR-XXX`
**Range:** 001-999
**Current:** RSR-001 to RSR-024
**Next:** RSR-025

**Location:** `ENTITIES/TASK_MANAGERS/RESEARCHES/`

**Purpose:** Research-specific workflows, tools, or objects created from video analysis.

---

## ID Ecosystem Hierarchy

### Complete Structure

```
ENTITIES (Global Root)
│
├── LIBRARIES/
│   ├── LBS-001: Actions → ACT-XXX (429 actions)
│   ├── LBS-002: Objects → OBJ-{CAT}-XXX (110+ objects)
│   ├── LBS-003: Tools → TOL-{CAT}-XXX (164+ tools)
│   ├── LBS-004: Skills → SKL-XXX (66 skills)
│   ├── LBS-005: Professions → PRF-XXX (15 professions)
│   ├── LBS-006: Departments → DPT-XXX (9 departments)
│   └── LBS-007: Responsibilities → RESP-XXX (193 responsibilities)
│
├── TASK_MANAGERS/
│   ├── TSM-006: Workflows → WRF-{CAT}-XXX (41 workflows)
│   │
│   └── RESEARCHES/ (This module)
│       ├── Videos → Video_XXX (28 videos)
│       ├── Queues
│       │   ├── Video Queue → VQ-XXX (42 items)
│       │   └── Search Queue → SEARCH-XXX (15 items)
│       │
│       ├── Research Entities → RSR-XXX (24 entities)
│       │
│       └── documentation/
│           ├── Documents → DOC-RES-XXX (17 docs)
│           ├── Issues → ISS-RES-XXX (12 issues)
│           ├── Phases → PHS-RES-XXX (9 phases, fixed)
│           ├── Tasks → TASK-XXX (42 tasks, global)
│           ├── Changes → CHG-RES-YYYYMMDD-XXX (timestamped)
│           └── Taxonomy → RSH-TAX-XXX (1 analysis)
│
└── TALENTS/
    ├── Skills → SKL-XXX (66 skills)
    └── Professions → PRF-XXX (15 professions)
```

---

## ID Formatting Standards

### Prefix Conventions

**Module Prefixes:**
- `RES` = RESEARCHES module
- `LIB` = LIBRARIES module
- `TSM` = TASK_MANAGERS module
- `TAL` = TALENTS module

**Entity Type Prefixes:**
- `ISS` = Issue
- `PHS` = Phase
- `TASK` = Task (global)
- `CHG` = Change
- `DOC` = Document
- `WRF` = Workflow
- `TOL`/`TOOL` = Tool
- `OBJ` = Object
- `SKL` = Skill
- `PRF` = Profession
- `RSR` = Research Entity
- `RSH-TAX` = Research Taxonomy Analysis
- `VQ` = Video Queue
- `SEARCH` = Search Queue

### Separator Rules

- **Primary:** Hyphen `-` for all new IDs
- **Legacy:** Underscore `_` only for `Video_XXX` (backward compatibility)
- **Date format:** YYYYMMDD (ISO 8601) for timestamped IDs

### Numbering Rules

- **Zero-padding:** Always 3 digits (001, 042, 999)
- **Sequential:** Assign IDs sequentially within namespace
- **No reuse:** Never reuse IDs, even if entity deleted
- **Gaps allowed:** Document gaps but don't fill them

---

## Cross-Reference Map

### Issue → Task → Change → Document

```
ISS-RES-011 (Missing unified ID system)
    ↓ resolved by
TASK-XXX (Create ID system documentation)
    ↓ implemented in
CHG-RES-20251203-001 (Documentation package creation)
    ↓ documented in
DOC-RES-004 (04_ID_System_Standard.md)
DOC-RES-017 (ID_MASTER_REGISTRY.md)
```

### Video → Extraction → Integration → Entity Creation

```
Video_024
    ↓ extracted from
03_ANALYSIS/Extractions/Video_024_Extraction_Inventory.md
    ↓ integrated to
ENTITIES/LIBRARIES/
    ↓ created entities
TOL-AI-223 (Browse AI)
WRF-SEC-014 (Secure OAuth)
```

---

## Validation Patterns (Regex)

### RESEARCHES Module

```regex
Video ID:       ^Video_\d{3}$
Video Queue:    ^VQ-\d{3}$
Search Queue:   ^SEARCH-\d{3}$
Document:       ^DOC-RES-\d{3}$
Issue:          ^ISS-RES-\d{3}$
Phase:          ^PHS-RES-\d{3}$
Task:           ^TASK-\d{3}$
Change:         ^CHG-RES-\d{8}-\d{3}$
Taxonomy:       ^RSH-TAX-\d{3}$
```

### ENTITIES Libraries

```regex
Workflow:       ^WRF-([A-Z]{3}-)?\d{3}$
Tool:           ^TOO?L-([A-Z]{2,3}-)?\d{3}$
Object:         ^OBJ-([A-Z]{3}-)?\d{3}$
Skill:          ^SKL-\d{3}$
Profession:     ^PRF-\d{3}$
Research:       ^RSR-\d{3}$
```

---

## Usage Guidelines

### When Creating New IDs

1. **Check this registry** for next available ID
2. **Follow formatting standards** (prefix-separator-number)
3. **Update this registry** after creating new ID
4. **Document in changelog** if significant (CHG-RES-YYYYMMDD-XXX)
5. **Create bidirectional links** if referencing other IDs

### When Referencing IDs

**In Markdown:**
```markdown
See [Video_024](../../02_TRANSCRIPTIONS/Video_024.md)
Related to ISS-RES-011
References TASK-001
```

**In JSON:**
```json
{
  "id": "TOL-AI-223",
  "related_videos": ["Video_024"],
  "resolves_issues": ["ISS-RES-008"]
}
```

**In CSV:**
```csv
Video_ID,Related_Issues,Related_Tasks
Video_024,"ISS-RES-008,ISS-RES-009","TASK-008"
```

---

## Maintenance Schedule

### Daily
- Update CHG-RES-YYYYMMDD-XXX for any system changes

### Weekly
- Review and update active ID ranges
- Check for orphaned references

### Monthly
- Full audit of all ID namespaces
- Validate cross-references
- Update this registry with new ID ranges

### Quarterly
- Review ID system effectiveness
- Propose improvements to standards
- Update documentation

---

## Automation Scripts

### Planned Scripts

1. **`scripts/id_generator.py`**
   - Generate next available ID for any namespace
   - Validate ID format before assignment
   - Update registry automatically

2. **`scripts/id_validator.py`**
   - Validate ID formats across all files
   - Check for duplicates
   - Verify cross-references

3. **`scripts/id_registry_sync.py`**
   - Scan all files for IDs
   - Update this registry automatically
   - Generate ID usage report

4. **`scripts/update_changelog.py`**
   - Add CHG-RES-YYYYMMDD-XXX entries
   - Link to issues and tasks
   - Generate monthly changelog reports

---

## Related Documents

- [04_ID_System_Standard.md](./04_ID_System_Standard.md) - Complete ID system specification
- [06_Issues_Registry.md](../issues/06_Issues_Registry.md) - Active issues using ISS-RES-XXX
- [07_Development_Roadmap.md](../phases/07_Development_Roadmap.md) - Tasks and phases
- [14_Changelog_System.md](../changelog/14_Changelog_System.md) - Change tracking system
- [RSH-TAX-001_Complete_Taxonomy_Analysis.md](../taxonomy/RSH-TAX-001_Complete_Taxonomy_Analysis.md) - ENTITIES taxonomy

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-12-10 | Initial registry creation | System Administrator |
| - | - | Documented all active ID ranges | - |
| - | - | Created cross-reference map | - |
| - | - | Added validation patterns | - |

---

**Registry Owner:** Technical Architect
**Review Cycle:** Monthly
**Next Review:** 2026-01-10

**Generated by:** Claude Code (Anthropic)
**Changelog Entry:** CHG-RES-20251210-001

---

**End of Document**
