# Entity Integration Taxonomy

## Overview
This document outlines the standard taxonomy and workflow for integrating new ENTITIES into the ecosystem. It ensures consistency across the file system and facilitates automation.

## Definitions
- **ENTITY:** A distinct functional unit or data category within the ecosystem (e.g., REPORTS, DEPARTMENTS, TASK_MANAGERS).
- **Ecosystem:** The collective directory structure and set of rules governing file organization.
- **Integration:** The process of establishing a new entity with proper structure, IDs, and documentation.
- **Action:** A tagging attribute (e.g., `#Action:Create`, `#Action:Update`) used to categorize the intent of a prompt or step. It is NOT a procedural step itself.

## Standard Workflow (Milestone Template)

### Milestone: Create Entity Reports
**Goal:** Fully integrate a new entity into the `ENTITIES` directory.

**Tasks:**
1. **Create New Folder:**
   - Location: `C:\Users\Dell\Dropbox\ENTITIES\[Entity_Name]`
   - Action: `#Action:Create`

2. **Add Taxonomy:**
   - Create a `TAXONOMY.md` file within the new entity folder.
   - Action: `#Action:Define`

3. **Integrate IDS System:**
   - Assign a unique 3-letter prefix.
   - Action: `#Action:Assign`

4. **Import Examples:**
   - Add representative files.
   - Action: `#Action:Import`

5. **Create Classification:**
   - Define types/categories.
   - Action: `#Action:Classify`

6. **Update Central Taxonomy:**
   - Register the new entity in `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\README.md`.
   - Action: `#Action:Update`

## Example: TASK_MANAGERS Full Cycle
To illustrate the integration, here is the `TASK_MANAGERS` entity structure:

1.  **Folder:** `ENTITIES\TASK_MANAGERS`
2.  **Taxonomy:**
    -   **Projects (PRT):** High-level objectives.
    -   **Milestones (MLT):** Key phases within a project.
    -   **Tasks (TST):** Actionable items.
3.  **IDS Integration:**
    -   `PRT-###`
    -   `MLT-###`
    -   `TST-###`
4.  **Hierarchy:**
    -   `PRT-001` -> `MLT-001` -> `TST-001`
    -   *Note:* Each child entity tags its parent (e.g., `TST-001` contains `#Parent:MLT-001`).

## Directory Structure
```
ENTITIES/
├── [Entity_Name]/
│   ├── DATA/           # Raw data, CSVs, JSONs
│   ├── DOCS/           # Documentation, guides
│   ├── ARCHIVE/        # Old or processed files
│   └── TAXONOMY.md     # Entity-specific taxonomy
```

## Naming Conventions
- **Directories:** UPPERCASE_WITH_UNDERSCORES (e.g., `DAILY_REPORTS`)
- **Files:** `[Prefix]-[ID]_[Description]_[Date].ext` (e.g., `RPT-001_Weekly_Summary_2025-11-19.md`)

---

## Registered Entities

### RESEARCHES (RSH)
**Added:** 2025-11-20
**Root Path:** `ENTITIES/TASK_MANAGERS/RESEARCHES/`

**Description:** Central repository for research artifacts, investigations, and knowledge synthesis across the ecosystem. Consolidates exploratory work, gap analyses, and structured findings.

**Sub-Entities:**
- **VIDEO_RESEARCHES (RSH-VID):** Video processing, influencer tracking, SMM research

**ID Patterns:**
- `RSH-{DEPT}-###` - General research (RSH-AI-001, RSH-DEV-001)
- `RSH-VID-###` - Video research

**Structure:**
```
RESEARCHES/
├── TAXONOMY/
├── INDEXES/
├── RESEARCHES/
│   ├── Video_Processing/         # Migrated from PROMPTS/Video_Processing
│   │   ├── Analysis/             # PMT-006, 007, 008, 071
│   │   ├── Transcription/        # PMT-004, 005
│   │   ├── Taxonomy_Integration/ # PMT-009
│   │   ├── Workflows/            # PMT-010, 011, 012, 090
│   │   └── Reports/              # Queue tracking
│   ├── PROMPTS/
│   ├── REPORTS/
│   ├── DATA/
│   └── MAPPINGS/
└── RESEARCH_PROMPTS/              # Migrated from PROMPTS/RESEARCH
    ├── Department_Integration/    # PMT-051
    ├── Sales/                     # PMT-044
    ├── Design/                    # PMT-051, 052, 085, 093
    ├── HR/                        # PMT-047, 049, 050, 052
    ├── AI_Tools/                  # PMT-048, 089
    ├── Development/               # PMT-046, 052
    ├── Course_Creation/           # PMT-082, 083
    └── SMM/                       # PMT-045
```

**Integration Points:**
- `PROMPTS/Video_Processing` → **MIGRATED** to `RESEARCHES/Video_Processing/`
- `PROMPTS/RESEARCH` → **MIGRATED** to `RESEARCH_PROMPTS/{Department}/`
- `REPORTS/Influencer_Tracking` - SMM data source (referenced)
- `REPORTS/Videos` - Video analysis outputs (referenced)

**PMT-IDs Managed:** 25+ prompts (PMT-004-012, PMT-044-052, PMT-071, PMT-082-093)
