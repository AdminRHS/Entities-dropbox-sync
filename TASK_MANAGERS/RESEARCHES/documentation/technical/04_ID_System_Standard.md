# ID System Standard: RESEARCHES Module

**Document ID:** DOC-RES-004
**Version:** 1.0
**Date:** 2025-12-03
**Status:** ✅ Complete
**Priority:** HIGH
**Classification:** Technical Specification

---

## Purpose

This document establishes a **unified, standardized ID system** for all elements within the RESEARCHES module, including videos, queues, research entities, issues, phases, tasks, and changes. It addresses **ISS-RES-011** by providing comprehensive ID standards that enable tracking of relationships between documents, tasks, and system changes.

---

## Table of Contents

1. [Existing ID Systems](#1-existing-id-systems)
2. [New ID Systems](#2-new-id-systems-introduced-in-this-documentation)
3. [ID Formation Rules](#3-id-formation-rules)
4. [Integration with ENTITIES Taxonomy](#4-integration-with-entities-taxonomy)
5. [ID Generation Automation](#5-id-generation-automation)
6. [Validation Patterns](#6-validation-patterns)
7. [Cross-Reference Standards](#7-cross-reference-standards)
8. [Migration Guidelines](#8-migration-guidelines)

---

## 1. Existing ID Systems

### 1.1 Video IDs

**Format:** `Video_XXX`
**Range:** 001-999
**Example:** `Video_024`

**Purpose:** Unique identifier for each processed video
**Location:** `02_TRANSCRIPTIONS/Video_XXX.md`

**Current State:**
- 28 videos processed: Video_001 through Video_028
- Video_015 is missing (gap in sequence)
- No leading zeros in folder references, but used in file names

**Rules:**
- Sequential numbering starting from 001
- Three-digit zero-padded format
- Underscore separator
- No reuse of IDs (even if video deleted)

**Related Files:**
```
02_TRANSCRIPTIONS/Video_024.md
03_ANALYSIS/Library_Mapping/Video_024_Library_Mapping_Report.md
03_ANALYSIS/Gap_Analysis/Video_024_Gap_Analysis.md
```

### 1.2 Queue IDs

#### VQ (Video Queue)
**Format:** `VQ-XXX`
**Range:** 001-999
**Example:** `VQ-042`

**Purpose:** Unique identifier for videos in processing queue
**Location:** `01_VIDEO_QUEUE/Video_Queue_Master.csv`

**Rules:**
- Assigned when video added to queue
- Hyphen separator
- Three-digit zero-padded
- Persistent even after video processed

**CSV Schema:**
```csv
Queue_ID, Video_ID, Video_Title, Channel_Name, Video_URL, Views, Likes,
Duration, Added_By, Added_Date, Status, Priority_Score, Topic_Category
```

#### SEARCH (Search Queue)
**Format:** `SEARCH-XXX`
**Range:** 001-999
**Example:** `SEARCH-015`

**Purpose:** Unique identifier for search assignments
**Location:** `00_SEARCH_QUEUE/Search_Queue_Master.csv`

**Rules:**
- Assigned when search task created
- Hyphen separator
- Three-digit zero-padded
- Links to employee and department

**CSV Schema:**
```csv
Search_ID, Employee, Department, Topic, Search_Query, Assigned_Date,
Status, Videos_Found, Completed_Date, Notes
```

### 1.3 Entity IDs (ENTITIES Taxonomy)

#### WRF (Workflows)
**Format:** `WRF-XXX` or `WRF-{CAT}-XXX`
**Range:** 001-999 per category
**Example:** `WRF-025`, `WRF-SEC-014`

**Purpose:** Unique identifier for workflows
**Location:** `TASK_MANAGERS/TSM-006_Workflows/`

**Categories:**
- General: `WRF-XXX`
- Security: `WRF-SEC-XXX`
- Design: `WRF-DGN-XXX`
- Development: `WRF-DEV-XXX`

#### TOL (Tools)
**Format:** `TOL-{CAT}-XXX` or `TOOL-{CAT}-XXX`
**Range:** 001-999 per category
**Example:** `TOL-AI-223`, `TOOL-VID-042`

**Purpose:** Unique identifier for tools and technologies
**Location:** `LIBRARIES/LBS_003_Tools/`

**Categories:**
- AI: `TOL-AI-XXX`
- Video: `TOL-VID-XXX`
- Design: `TOL-DGN-XXX`
- Automation: `TOL-AUT-XXX`
- Development: `TOL-DEV-XXX`

#### OBJ (Objects)
**Format:** `OBJ-{CAT}-XXX`
**Range:** 001-999 per category
**Example:** `OBJ-SMM-015`, `OBJ-VID-008`

**Purpose:** Unique identifier for deliverables and outputs
**Location:** `LIBRARIES/Responsibilities/Objects/`

**Categories:**
- Social Media: `OBJ-SMM-XXX`
- Video: `OBJ-VID-XXX`
- Security: `OBJ-SEC-XXX`
- General: `OBJ-XXX`

#### SKL (Skills)
**Format:** `SKL-XXX`
**Range:** 001-999
**Example:** `SKL-042`, `SKL-065`

**Purpose:** Unique identifier for skills and competencies
**Location:** `TALENTS/Skills/Master/all_skills.json`

**Rules:**
- Sequential numbering
- Three-digit zero-padded
- Global namespace (not categorized)

#### PRF (Professions)
**Format:** `PRF-XXX`
**Range:** 001-999
**Example:** `PRF-003`, `PRF-015`

**Purpose:** Unique identifier for roles and professions
**Location:** `TALENTS/Professions/`

**Rules:**
- Sequential numbering
- Three-digit zero-padded
- Global namespace

#### RSR (Research Entities)
**Format:** `RSR-XXX`
**Range:** 001-999
**Example:** `RSR-001`, `RSR-024`

**Purpose:** Unique identifier for research-specific entities
**Location:** `TASK_MANAGERS/RESEARCHES/`

**Current State:**
- 24 RSR entities created (RSR-001 through RSR-024)
- Used for research-specific workflows, tools, or objects

---

## 2. New ID Systems (Introduced in This Documentation)

### 2.1 ISS (Issues)

**Format:** `ISS-RES-XXX`
**Range:** 001-999
**Example:** `ISS-RES-011`

**Purpose:** Unique identifier for identified issues and problems
**Location:** `documentation/issues/06_Issues_Registry.md`

**Components:**
- `ISS` = Issue
- `RES` = RESEARCHES module
- `XXX` = Sequential number (001-999)

**Rules:**
- Sequential numbering across all issues
- Module-specific prefix (RES for RESEARCHES)
- Hyphen separators
- Three-digit zero-padded

**Status Values:**
- `OPEN` - Issue identified, not resolved
- `IN_PROGRESS` - Work ongoing
- `RESOLVED` - Solution implemented
- `CLOSED` - Verified and closed
- `WONTFIX` - Decided not to fix

**Priority Values:**
- `CRITICAL` - Blocks system operation
- `HIGH` - Significantly affects efficiency
- `MEDIUM` - Desirable to fix
- `LOW` - Nice to have

**Example Entry:**
```markdown
### ISS-RES-011: Missing unified ID system for documentation elements
- **Priority:** HIGH
- **Status:** RESOLVED
- **Description:** No standardized ID system for issues, phases, tasks, changes
- **Impact:** Difficult to track relationships between documents
- **Solution:** Create 04_ID_System_Standard.md
- **Related Files:** documentation/technical/04_ID_System_Standard.md
- **Effort Estimate:** 3-4 hours
```

**Current Issues:**
- ISS-RES-001 through ISS-RES-012 (12 issues documented)

### 2.2 PHS (Phases)

**Format:** `PHS-RES-XXX`
**Range:** 001-009 (fixed, 9 phases planned)
**Example:** `PHS-RES-001`

**Purpose:** Unique identifier for development phases
**Location:** `documentation/phases/07_Development_Roadmap.md`

**Components:**
- `PHS` = Phase
- `RES` = RESEARCHES module
- `XXX` = Phase number (001-009)

**Rules:**
- Fixed range (9 phases total)
- Sequential numbering
- Hyphen separators
- Three-digit zero-padded

**Current Phases:**
- PHS-RES-001: Stabilization (v1.0)
- PHS-RES-002: Automation Enhancement (v1.0)
- PHS-RES-003: Monitoring & Dashboards (v1.0)
- PHS-RES-004: Quality Assurance (v2.0)
- PHS-RES-005: AI/ML Integration (v2.0)
- PHS-RES-006: Multi-Source Integration (v2.0)
- PHS-RES-007: Collaboration Features (v3.0)
- PHS-RES-008: Advanced Analytics (v3.0)
- PHS-RES-009: Documentation & Knowledge Base (v3.0)

**Version Mapping:**
- v1.0: PHS-RES-001 to PHS-RES-003
- v2.0: PHS-RES-004 to PHS-RES-006
- v3.0: PHS-RES-007 to PHS-RES-009

### 2.3 TASK (Tasks)

**Format:** `TASK-XXX`
**Range:** 001-999
**Example:** `TASK-001`

**Purpose:** Unique identifier for development tasks
**Location:** `documentation/phases/*.md`

**Components:**
- `TASK` = Task prefix
- `XXX` = Sequential number (001-999)

**Rules:**
- Sequential numbering across all tasks
- Global namespace (not module-specific)
- Hyphen separator
- Three-digit zero-padded

**Current Tasks:**
- TASK-001 through TASK-042 (42 tasks planned)
- TASK-001 to TASK-013: v1.0 tasks (detailed)
- TASK-014 to TASK-042: v2.0 and v3.0 tasks (conceptual)

**Example Entry:**
```markdown
### TASK-001: Update VIDEO_PROGRESS_TRACKER.csv
- **Phase:** PHS-RES-001 (Stabilization)
- **Issue:** ISS-RES-001
- **Description:** Batch update all 22 videos to correct status
- **Effort:** 2-3 hours
- **Dependencies:** None
- **Acceptance Criteria:**
  - [ ] All 22 videos have correct status
  - [ ] Backup created
  - [ ] CSV validates without errors
```

### 2.4 CHG (Changes)

**Format:** `CHG-RES-YYYYMMDD-XXX`
**Range:** 001-999 per day
**Example:** `CHG-RES-20251203-001`

**Purpose:** Unique identifier for system changes
**Location:** `documentation/changelog/14_Changelog_System.md`

**Components:**
- `CHG` = Change
- `RES` = RESEARCHES module
- `YYYYMMDD` = Date (ISO 8601)
- `XXX` = Daily sequential number (001-999)

**Rules:**
- Date-based grouping (YYYYMMDD format)
- Daily sequential numbering resets each day
- Hyphen separators
- Three-digit zero-padded for daily sequence

**Change Categories:**
- `FEATURE` - New functionality
- `BUGFIX` - Bug fix
- `IMPROVEMENT` - Enhancement of existing
- `DOCS` - Documentation changes
- `REFACTOR` - Code refactoring
- `DEPRECATED` - Deprecated functionality

**Example Entry:**
```markdown
#### CHG-RES-20251203-001 [DOCS]
**Type:** Documentation package creation
**Author:** AI Assistant
**Description:** Complete documentation package created (16 files)
**Files:**
- documentation/technical/*.md (NEW)
- documentation/diagrams/*.md (NEW)
- documentation/issues/*.md (NEW)
**Impact:** New employees can onboard in 1 day instead of 1 week
**Related Issues:** ISS-RES-011, ISS-RES-012
**Related Tasks:** N/A
```

**Current Changes:**
- CHG-RES-20251203-001 (this documentation package)
- CHG-RES-20251124-001 (phase restructure)
- CHG-RES-20251124-002 (status verification)

### 2.5 DOC (Documents)

**Format:** `DOC-RES-XXX`
**Range:** 001-999
**Example:** `DOC-RES-001`

**Purpose:** Unique identifier for documentation files
**Location:** All `documentation/` folder files

**Components:**
- `DOC` = Document
- `RES` = RESEARCHES module
- `XXX` = Sequential number (001-999)

**Rules:**
- Sequential numbering for all documents
- Module-specific prefix
- Hyphen separator
- Three-digit zero-padded

**Current Documents:**
- DOC-RES-001: 01_Executive_Summary.md
- DOC-RES-002: 02_Technical_Report.md
- DOC-RES-003: 03_System_Architecture.md
- DOC-RES-004: 04_ID_System_Standard.md (this document)
- DOC-RES-005: 05_Workflow_Diagrams.md
- DOC-RES-006: 06_Issues_Registry.md
- DOC-RES-007: 07_Development_Roadmap.md
- DOC-RES-008: 08_Phase_Prompts_V1.md
- DOC-RES-009: 09_Phase_Prompts_V2_V3.md
- DOC-RES-010: 10_Employee_Onboarding_Guide.md
- DOC-RES-011: 11_Day1_Quick_Start.md
- DOC-RES-012: 12_Week1_Practice.md
- DOC-RES-013: 13_Month1_Mastery.md
- DOC-RES-014: 14_Changelog_System.md
- DOC-RES-015: 15_Master_Index.md
- DOC-RES-016: README.md

---

## 3. ID Formation Rules

### 3.1 General Principles

1. **Uniqueness:** Every ID must be globally unique within its namespace
2. **Persistence:** IDs never change or get reused after deletion
3. **Readability:** IDs should be human-readable and self-documenting
4. **Consistency:** Follow established patterns across all systems
5. **Sortability:** IDs should sort naturally (alphabetically/numerically)

### 3.2 Component Structure

**Standard Format:**
```
[PREFIX]-[MODULE]-[CATEGORY]-[NUMBER]
```

**Examples:**
- `ISS-RES-011` (Issue in RESEARCHES module)
- `WRF-SEC-014` (Security workflow)
- `TOL-AI-223` (AI tool)
- `CHG-RES-20251203-001` (Change on 2025-12-03)

**Simplified Format (No Module/Category):**
```
[PREFIX]-[NUMBER]
```

**Examples:**
- `TASK-042` (Task, global namespace)
- `SKL-065` (Skill, global namespace)
- `PRF-015` (Profession, global namespace)

### 3.3 Separator Rules

- **Hyphen (-):** Primary separator for ID components
- **Underscore (_):** Used in legacy Video IDs (`Video_XXX`)
- **No spaces:** Never use spaces in IDs
- **Consistent case:** Use UPPERCASE for prefixes, lowercase for modules/categories

### 3.4 Numbering Rules

**Zero-Padding:**
- Always use 3-digit zero-padding: `001`, `042`, `999`
- Exception: Date-based IDs use YYYYMMDD format

**Sequential Assignment:**
- Assign IDs sequentially within namespace
- Never skip numbers intentionally
- Document gaps if they occur (e.g., Video_015)

**Range Limits:**
- Standard range: 001-999 (999 IDs per namespace)
- If exceeded, consider sub-categorization or namespace expansion

**No Reuse:**
- Never reuse an ID, even if entity deleted
- Maintain historical record of all assigned IDs

### 3.5 Prefix Standards

**Module Prefixes:**
- `RES` = RESEARCHES
- `LIB` = LIBRARIES
- `TSM` = TASK_MANAGERS
- `TAL` = TALENTS

**Entity Type Prefixes:**
- `ISS` = Issue
- `PHS` = Phase
- `TASK` = Task
- `CHG` = Change
- `DOC` = Document
- `WRF` = Workflow
- `TOL/TOOL` = Tool
- `OBJ` = Object
- `SKL` = Skill
- `PRF` = Profession
- `RSR` = Research Entity
- `VQ` = Video Queue
- `SEARCH` = Search Queue

---

## 4. Integration with ENTITIES Taxonomy

### 4.1 Namespace Hierarchy

```
ENTITIES (Global)
├── LIBRARIES
│   ├── LBS_003_Tools
│   │   └── TOL-{CAT}-XXX
│   └── Responsibilities
│       ├── Objects → OBJ-{CAT}-XXX
│       └── Actions → ACTION-XXX
├── TASK_MANAGERS
│   ├── RESEARCHES
│   │   ├── Video_XXX
│   │   ├── VQ-XXX
│   │   ├── SEARCH-XXX
│   │   ├── ISS-RES-XXX
│   │   ├── PHS-RES-XXX
│   │   ├── TASK-XXX
│   │   └── CHG-RES-YYYYMMDD-XXX
│   └── TSM-006_Workflows
│       └── WRF-{CAT}-XXX
└── TALENTS
    ├── Skills → SKL-XXX
    └── Professions → PRF-XXX
```

### 4.2 Cross-Module References

**Allowed References:**
- RESEARCHES → LIBRARIES (e.g., Video_024 creates TOL-AI-223)
- RESEARCHES → TASK_MANAGERS (e.g., Video_024 creates WRF-SEC-014)
- RESEARCHES → TALENTS (e.g., Video_024 references SKL-065)
- Issues → Any entity (e.g., ISS-RES-005 references scripts/)
- Tasks → Issues (e.g., TASK-006 resolves ISS-RES-005)
- Changes → Issues + Tasks (e.g., CHG-RES-20251203-001 addresses ISS-RES-011)

**Bidirectional Linking:**
All cross-references must be bidirectional:
- Video_024 creates TOL-AI-223 → TOL-AI-223 references Video_024
- TASK-001 resolves ISS-RES-001 → ISS-RES-001 references TASK-001

### 4.3 Department Codes

**Standard Codes:**
- `AID` = AI Development
- `VID` = Video Production
- `SMM` = Social Media Marketing
- `DGN` = Design
- `DEV` = Development
- `HRM` = Human Resources
- `MKT` = Marketing
- `SLS` = Sales
- `LGN` = Lead Generation
- `SEC` = Security
- `QA` = Quality Assurance

**Usage in IDs:**
- Optional category for tools: `TOL-AID-XXX`
- Optional category for workflows: `WRF-DGN-XXX`
- Optional category for objects: `OBJ-SMM-XXX`

---

## 5. ID Generation Automation

### 5.1 Existing Scripts

#### video_id_scanner.py
**Purpose:** Scan for next available IDs across all namespaces
**Usage:**
```bash
python scripts/video_id_scanner.py
```

**Output:**
```
Next available IDs:
- Video: Video_029
- WRF: WRF-041
- SKL: SKL-066
- TOL-AI: TOL-AI-224
- OBJ-SMM: OBJ-SMM-016
```

**Namespaces Scanned:**
- Video_XXX (02_TRANSCRIPTIONS/)
- WRF-XXX (TASK_MANAGERS/TSM-006_Workflows/)
- SKL-XXX (TALENTS/Skills/Master/)
- TOL-{CAT}-XXX (LIBRARIES/LBS_003_Tools/)
- OBJ-{CAT}-XXX (LIBRARIES/Responsibilities/Objects/)

### 5.2 Planned Scripts

#### id_generator.py (PLANNED)
**Purpose:** Generate IDs for new documentation system
**Usage:**
```bash
# Generate next issue ID
python scripts/id_generator.py issue

# Generate next task ID
python scripts/id_generator.py task

# Generate next change ID for today
python scripts/id_generator.py change

# Generate next phase ID
python scripts/id_generator.py phase
```

**Features:**
- Read existing IDs from documentation files
- Return next available ID in sequence
- Validate ID format before assignment
- Log all generated IDs to registry

**Implementation:**
```python
import re
from datetime import datetime
from pathlib import Path

class IDGenerator:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.patterns = {
            'issue': r'ISS-RES-(\d{3})',
            'task': r'TASK-(\d{3})',
            'change': r'CHG-RES-\d{8}-(\d{3})',
            'phase': r'PHS-RES-(\d{3})',
            'document': r'DOC-RES-(\d{3})'
        }

    def get_next_id(self, id_type: str) -> str:
        """Get next available ID for given type"""
        pattern = self.patterns.get(id_type)
        if not pattern:
            raise ValueError(f"Unknown ID type: {id_type}")

        # Scan files and extract existing IDs
        existing_ids = self._scan_existing_ids(id_type, pattern)

        # Find next available number
        if existing_ids:
            next_num = max(existing_ids) + 1
        else:
            next_num = 1

        # Format based on type
        if id_type == 'issue':
            return f"ISS-RES-{next_num:03d}"
        elif id_type == 'task':
            return f"TASK-{next_num:03d}"
        elif id_type == 'change':
            today = datetime.now().strftime("%Y%m%d")
            # Get today's sequence number
            today_nums = [n for n in existing_ids
                         if self._is_today_change(f"CHG-RES-{today}-{n:03d}")]
            next_today = max(today_nums, default=0) + 1
            return f"CHG-RES-{today}-{next_today:03d}"
        elif id_type == 'phase':
            return f"PHS-RES-{next_num:03d}"
        elif id_type == 'document':
            return f"DOC-RES-{next_num:03d}"

    def validate_id(self, id_string: str, id_type: str) -> bool:
        """Validate ID format"""
        pattern = self.patterns.get(id_type)
        return bool(re.match(f"^{pattern}$", id_string))
```

#### update_changelog.py (PLANNED)
**Purpose:** Automate changelog entry creation
**Usage:**
```bash
# Interactive entry
python scripts/update_changelog.py add

# Sync from git
python scripts/update_changelog.py sync-git

# Generate report
python scripts/update_changelog.py report --month 12 --year 2025
```

**Features:**
- Automatic CHG-RES-YYYYMMDD-XXX generation
- Template-based entry creation
- Git integration (parse commits)
- Monthly report generation

---

## 6. Validation Patterns

### 6.1 Regex Patterns

**Video ID:**
```regex
^Video_\d{3}$
```
**Examples:** `Video_001`, `Video_024`, `Video_999`

**Video Queue ID:**
```regex
^VQ-\d{3}$
```
**Examples:** `VQ-001`, `VQ-042`, `VQ-999`

**Search Queue ID:**
```regex
^SEARCH-\d{3}$
```
**Examples:** `SEARCH-001`, `SEARCH-015`, `SEARCH-999`

**Issue ID:**
```regex
^ISS-RES-\d{3}$
```
**Examples:** `ISS-RES-001`, `ISS-RES-011`, `ISS-RES-999`

**Phase ID:**
```regex
^PHS-RES-\d{3}$
```
**Examples:** `PHS-RES-001`, `PHS-RES-005`, `PHS-RES-009`

**Task ID:**
```regex
^TASK-\d{3}$
```
**Examples:** `TASK-001`, `TASK-042`, `TASK-999`

**Change ID:**
```regex
^CHG-RES-\d{8}-\d{3}$
```
**Examples:** `CHG-RES-20251203-001`, `CHG-RES-20251224-042`

**Document ID:**
```regex
^DOC-RES-\d{3}$
```
**Examples:** `DOC-RES-001`, `DOC-RES-016`, `DOC-RES-999`

**Workflow ID:**
```regex
^WRF-([A-Z]{3}-)?(\d{3})$
```
**Examples:** `WRF-025`, `WRF-SEC-014`, `WRF-DGN-042`

**Tool ID:**
```regex
^TOO?L-([A-Z]{2,3}-)?\d{3}$
```
**Examples:** `TOL-AI-223`, `TOOL-VID-042`, `TOL-005`

**Object ID:**
```regex
^OBJ-([A-Z]{3}-)?\d{3}$
```
**Examples:** `OBJ-SMM-015`, `OBJ-VID-008`, `OBJ-042`

**Skill ID:**
```regex
^SKL-\d{3}$
```
**Examples:** `SKL-001`, `SKL-065`, `SKL-999`

**Profession ID:**
```regex
^PRF-\d{3}$
```
**Examples:** `PRF-001`, `PRF-015`, `PRF-999`

**Research Entity ID:**
```regex
^RSR-\d{3}$
```
**Examples:** `RSR-001`, `RSR-024`, `RSR-999`

### 6.2 Validation Script

**validate_ids.py (PLANNED)**
```python
import re
from typing import Dict, List, Tuple

class IDValidator:
    PATTERNS = {
        'video': r'^Video_\d{3}$',
        'vq': r'^VQ-\d{3}$',
        'search': r'^SEARCH-\d{3}$',
        'issue': r'^ISS-RES-\d{3}$',
        'phase': r'^PHS-RES-\d{3}$',
        'task': r'^TASK-\d{3}$',
        'change': r'^CHG-RES-\d{8}-\d{3}$',
        'document': r'^DOC-RES-\d{3}$',
        'workflow': r'^WRF-([A-Z]{3}-)?\d{3}$',
        'tool': r'^TOO?L-([A-Z]{2,3}-)?\d{3}$',
        'object': r'^OBJ-([A-Z]{3}-)?\d{3}$',
        'skill': r'^SKL-\d{3}$',
        'profession': r'^PRF-\d{3}$',
        'research': r'^RSR-\d{3}$'
    }

    def validate(self, id_string: str) -> Tuple[bool, str]:
        """Validate ID against all patterns"""
        for id_type, pattern in self.PATTERNS.items():
            if re.match(pattern, id_string):
                return True, id_type
        return False, "unknown"

    def validate_file(self, file_path: str) -> Dict[str, List[str]]:
        """Validate all IDs in a file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        results = {'valid': [], 'invalid': []}

        # Find all potential IDs
        potential_ids = re.findall(
            r'\b[A-Z]{2,6}-[A-Z]{0,3}-?\d{3,8}-?\d{0,3}\b',
            content
        )

        for pid in potential_ids:
            is_valid, id_type = self.validate(pid)
            if is_valid:
                results['valid'].append((pid, id_type))
            else:
                results['invalid'].append(pid)

        return results
```

---

## 7. Cross-Reference Standards

### 7.1 Reference Format

**In Markdown:**
```markdown
See [Video_024](../../02_TRANSCRIPTIONS/Video_024.md)
Related to ISS-RES-011
References TASK-001
Implements WRF-SEC-014
Uses TOL-AI-223
```

**In JSON:**
```json
{
  "id": "TOL-AI-223",
  "name": "Browse AI",
  "related_videos": ["Video_024"],
  "workflows": ["WRF-025"],
  "issues_resolved": ["ISS-RES-008"],
  "tasks": ["TASK-008"]
}
```

**In CSV:**
```csv
Video_ID,Related_Issues,Related_Tasks,Entities_Created
Video_024,"ISS-RES-008,ISS-RES-009","TASK-008","TOL-AI-223,WRF-SEC-014"
```

### 7.2 Bidirectional Linking

**Requirements:**
- All references must be bidirectional
- Both sides must explicitly mention the relationship
- Update both entities when creating relationship

**Example:**
```markdown
# In Video_024.md
Created entities:
- TOL-AI-223 (Browse AI)
- WRF-SEC-014 (Secure OAuth)

# In TOL-AI-223 JSON
{
  "source_video": "Video_024",
  "documented_in": "DOC-RES-002"
}

# In WRF-SEC-014 JSON
{
  "source_video": "Video_024",
  "tools_used": ["TOL-AI-223"]
}
```

### 7.3 Reference Validation

**Checklist:**
- [ ] All entity IDs exist in target location
- [ ] All references are bidirectional
- [ ] No broken links
- [ ] Correct ID format used
- [ ] Relative paths correct

---

## 8. Migration Guidelines

### 8.1 Existing Systems

**No Migration Needed:**
- Video_XXX (keep as is)
- VQ-XXX (keep as is)
- SEARCH-XXX (keep as is)
- WRF-XXX, TOL-XXX, OBJ-XXX, SKL-XXX, PRF-XXX, RSR-XXX (ENTITIES taxonomy)

**New Systems Added:**
- ISS-RES-XXX (issues)
- PHS-RES-XXX (phases)
- TASK-XXX (tasks)
- CHG-RES-YYYYMMDD-XXX (changes)
- DOC-RES-XXX (documents)

### 8.2 Implementation Plan

**Phase 1: Documentation (Complete)**
- ✅ Create 04_ID_System_Standard.md
- ✅ Document all ID systems
- ✅ Define validation patterns

**Phase 2: Script Development (TASK-XXX)**
- [ ] Create id_generator.py
- [ ] Create update_changelog.py
- [ ] Create validate_ids.py
- [ ] Integrate with existing scripts

**Phase 3: Validation (TASK-XXX)**
- [ ] Validate all existing IDs
- [ ] Fix any format inconsistencies
- [ ] Generate ID registry

**Phase 4: Training (TASK-XXX)**
- [ ] Update onboarding materials
- [ ] Create ID usage examples
- [ ] Train team on new system

---

## 9. Summary

This ID system standard provides:

1. ✅ **Unified system** for all RESEARCHES entities
2. ✅ **Backward compatibility** with existing IDs
3. ✅ **Clear rules** for ID formation and validation
4. ✅ **Automation support** through scripts
5. ✅ **Cross-reference standards** for bidirectional linking
6. ✅ **Integration** with ENTITIES taxonomy
7. ✅ **Scalability** for future growth

**Key Benefits:**
- Tracking relationships between issues, tasks, changes
- Automated ID generation and validation
- Consistent naming across all systems
- Easy navigation through cross-references
- Historical tracking via changelog

**Resolved Issues:**
- ✅ ISS-RES-011 (Missing unified ID system)

**Related Documents:**
- [06_Issues_Registry.md](../issues/06_Issues_Registry.md) - Uses ISS-RES-XXX
- [07_Development_Roadmap.md](../phases/07_Development_Roadmap.md) - Uses PHS-RES-XXX and TASK-XXX
- [14_Changelog_System.md](../changelog/14_Changelog_System.md) - Uses CHG-RES-YYYYMMDD-XXX
- [ID_MASTER_REGISTRY.md](./ID_MASTER_REGISTRY.md) - Complete registry of all ID ranges

---

## 10. Unified ID Ecosystem

### 10.1 Ecosystem Overview

The RESEARCHES ID system is part of a **larger unified ecosystem** that integrates seamlessly with the ENTITIES taxonomy. This ecosystem provides:

1. **Hierarchical organization** - Clear parent-child relationships
2. **Cross-module references** - Links between different system components
3. **Consistent naming** - Standardized prefixes and formats across all modules
4. **Bidirectional traceability** - Track relationships in both directions
5. **Automated validation** - Scripts to ensure integrity

### 10.2 Complete Ecosystem Structure

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
│           ├── Phases → PHS-RES-XXX (9 phases)
│           ├── Tasks → TASK-XXX (42 tasks, global)
│           ├── Changes → CHG-RES-YYYYMMDD-XXX
│           └── Taxonomy → RSH-TAX-XXX (1 analysis)
│
└── TALENTS/
    ├── Skills → SKL-XXX (66 skills)
    └── Professions → PRF-XXX (15 professions)
```

### 10.3 ID Categories by Scope

#### Module-Specific IDs (RESEARCHES only)

These IDs are specific to the RESEARCHES module and use the `-RES-` component:

```
Format: [PREFIX]-RES-[NUMBER]
```

**Examples:**
- `ISS-RES-011` - Issue in RESEARCHES module
- `PHS-RES-001` - Phase in RESEARCHES development
- `CHG-RES-20251210-001` - Change in RESEARCHES system
- `DOC-RES-017` - Document in RESEARCHES documentation
- `RSH-TAX-001` - Research taxonomy analysis

**Usage:** These IDs cannot be used outside RESEARCHES module.

#### Global IDs (Cross-module)

These IDs are global and can be referenced from any module:

```
Format: [PREFIX]-[NUMBER]
```

**Examples:**
- `TASK-042` - Tasks can be in any module
- `SKL-065` - Skills are global
- `PRF-015` - Professions are global

**Usage:** Can be referenced from RESEARCHES, other modules, or ENTITIES libraries.

#### Categorized IDs (Domain-specific)

These IDs include a category component for organization within domains:

```
Format: [PREFIX]-[CATEGORY]-[NUMBER]
```

**Examples:**
- `WRF-SEC-014` - Security workflow
- `TOL-AI-223` - AI tool
- `OBJ-SMM-015` - Social media object

**Usage:** Category provides additional context and organization.

### 10.4 Integration Patterns

#### Pattern 1: Video → Entity Creation

```
Video_024 (Source)
    ↓ analyzed via
PMT-007 (Prompt)
    ↓ created
TOL-AI-223 (Tool: Browse AI)
WRF-SEC-014 (Workflow: Secure OAuth)
    ↓ stored in
ENTITIES/LIBRARIES/
```

**Bidirectional Links:**
- `Video_024.md` lists: Created TOL-AI-223, WRF-SEC-014
- `TOL-AI-223.json` contains: `source_video: "Video_024"`
- `WRF-SEC-014.json` contains: `source_video: "Video_024"`

#### Pattern 2: Issue → Task → Change → Document

```
ISS-RES-011 (Problem: Missing ID system)
    ↓ resolved by
TASK-XXX (Create ID documentation)
    ↓ implemented in
CHG-RES-20251203-001 (Documentation package)
    ↓ documented in
DOC-RES-004 (04_ID_System_Standard.md)
DOC-RES-017 (ID_MASTER_REGISTRY.md)
```

**Cross-references:**
- Issue lists resolving tasks
- Task references issue and change
- Change links to issue and resulting documents
- Documents reference originating issue

#### Pattern 3: Research → Taxonomy Integration

```
Video_024 (Research source)
    ↓ extracted entities
RSR-024 (Research entity wrapper)
    ↓ integrated to
ENTITIES/LIBRARIES/LBS_003_Tools/
    ↓ created
TOL-AI-223.json (Final entity)
```

### 10.5 Namespace Ownership

| Namespace | Owner Module | Scope | Who Can Create |
|-----------|--------------|-------|----------------|
| `Video_XXX` | RESEARCHES | Module | RESEARCHES team |
| `VQ-XXX` | RESEARCHES | Module | RESEARCHES team |
| `SEARCH-XXX` | RESEARCHES | Module | RESEARCHES team |
| `DOC-RES-XXX` | RESEARCHES | Module | Documentation team |
| `ISS-RES-XXX` | RESEARCHES | Module | QA team |
| `PHS-RES-XXX` | RESEARCHES | Module | Project managers (fixed set) |
| `TASK-XXX` | Global | Global | Any module |
| `CHG-RES-XXX` | RESEARCHES | Module | System administrators |
| `RSH-TAX-XXX` | RESEARCHES | Module | Taxonomy analysts |
| `WRF-XXX` | TASK_MANAGERS | Global | Workflow designers |
| `TOL-XXX` | LIBRARIES | Global | Tool curators |
| `OBJ-XXX` | LIBRARIES | Global | Object managers |
| `SKL-XXX` | TALENTS | Global | HR team |
| `PRF-XXX` | TALENTS | Global | HR team |
| `RSR-XXX` | RESEARCHES | Module | RESEARCHES team |

### 10.6 Ecosystem Benefits

#### 1. Traceability

Track any entity from source to final integration:
```
Video_024 → RSR-024 → TOL-AI-223 → Used in WRF-025
```

#### 2. Impact Analysis

Understand impact of changes:
```
CHG-RES-20251203-001 affects:
- DOC-RES-004 (modified)
- DOC-RES-017 (created)
- ISS-RES-011 (resolved)
- TASK-XXX (completed)
```

#### 3. Consistency

All IDs follow same patterns:
- Hyphen separators (except legacy `Video_XXX`)
- Three-digit zero-padding
- Uppercase prefixes
- Predictable formats

#### 4. Automation

Scripts can:
- Generate next available ID
- Validate format
- Check cross-references
- Update registries

#### 5. Documentation

Clear relationships documented:
- Parent-child hierarchies
- Cross-module references
- Dependency graphs
- Usage examples

### 10.7 Best Practices for Ecosystem

#### When Creating New IDs

1. **Check ID_MASTER_REGISTRY.md** for next available
2. **Use correct prefix** for your module/scope
3. **Follow format** exactly (case, separators, padding)
4. **Create bidirectional links** if referencing other IDs
5. **Update registry** after creation
6. **Document in changelog** if significant

#### When Referencing IDs

1. **Use full ID** including prefix (ISS-RES-011, not just 011)
2. **Create markdown links** when possible
3. **Verify target exists** before creating reference
4. **Update both sides** of relationship
5. **Use consistent format** across all files

#### When Integrating Modules

1. **Understand scope** (module-specific vs global)
2. **Check ownership** before creating IDs
3. **Follow namespace rules**
4. **Document integration points**
5. **Maintain bidirectional links**

### 10.8 Future Enhancements

#### Planned Improvements

1. **Automated Registry Sync**
   - Script scans all files
   - Updates ID_MASTER_REGISTRY.md automatically
   - Detects new IDs and gaps

2. **Cross-Reference Validator**
   - Checks all ID references
   - Verifies targets exist
   - Reports broken links
   - Suggests fixes

3. **ID Dashboard**
   - Visual representation of ecosystem
   - Interactive relationship graph
   - Usage statistics
   - Gap analysis

4. **Migration Tools**
   - Convert legacy formats
   - Bulk ID updates
   - Reference updates
   - Validation reports

5. **CI/CD Integration**
   - Automatic validation on commit
   - ID format checks
   - Duplicate detection
   - Registry updates

### 10.9 Ecosystem Maintenance

#### Daily Tasks
- Update CHG-RES-YYYYMMDD-XXX for changes
- Create new IDs as needed
- Maintain bidirectional links

#### Weekly Tasks
- Review ID_MASTER_REGISTRY.md
- Check for orphaned references
- Update documentation

#### Monthly Tasks
- Full ID audit
- Validate all cross-references
- Update ecosystem documentation
- Review automation scripts

#### Quarterly Tasks
- Evaluate ID system effectiveness
- Propose improvements
- Update standards
- Train new team members

---

**Document Owner:** Technical Architect
**Review Cycle:** Quarterly
**Next Review:** 2025-03-03
**Version History:**
- v1.0 (2025-12-03): Initial version, addresses ISS-RES-011
- v1.1 (2025-12-10): Added Section 10 - Unified ID Ecosystem

**Generated by:** Claude Code (Anthropic)
**Changelog Entry:** CHG-RES-20251203-001, CHG-RES-20251210-001
