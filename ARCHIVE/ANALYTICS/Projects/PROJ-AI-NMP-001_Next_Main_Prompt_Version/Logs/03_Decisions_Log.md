# Decisions Log - PROJ-AI-NMP-001: Next Main Prompt Version

**Project ID:** PROJ-AI-NMP-001
**Log Type:** Architecture & Design Decisions
**Created:** 2025-11-15
**Last Updated:** 2025-11-15

---

## Decision Summary

**Total Decisions:** 7
**Architecture Decisions:** 5
**Design Decisions:** 2
**Implementation Decisions:** 0

---

## Active Decisions

### DEC-001: Modular vs Monolithic Architecture

**Date:** 2025-11-15
**Decision Maker:** Claude + ALX (approval)
**Category:** Architecture
**Status:** Approved

#### Context
MAIN_PROMPT v4 is a single monolithic file (2,538 lines, ~119KB). Need to decide whether v5 should remain monolithic or become modular.

#### Options Considered
1. **Keep Monolithic:** Single large file like v4
2. **Full Modular:** Break into ~50 separate files
3. **Hybrid:** Maintain both versions

#### Decision
**Chosen: Option 3 - Hybrid Approach**

Create modular structure with ~50 files across 5 folders, AND maintain ability to generate monolithic version via assembly scripts.

#### Rationale
- **Maintainability:** Easier to update individual components
- **Scalability:** Can grow libraries without overwhelming single file
- **Flexibility:** Assembly scripts provide monolithic version when needed
- **Backward Compatibility:** Monolithic version preserves v4 usage pattern
- **Best of Both:** Modular for maintenance, monolithic for deployment

#### Implementation
- Modular version: `MAIN_PROMPT_v5_Modular/` (primary working version)
- Monolithic version: `MAIN_PROMPT_v5.md` (generated via scripts)
- Assembly scripts in `scripts/` folder

#### Consequences
- **Positive:** Better organization, easier updates, version control friendly
- **Negative:** Requires assembly step, more complex initial setup
- **Mitigation:** Automated assembly scripts reduce complexity

---

### DEC-002: Milestone Structure - Embedded vs Separate

**Date:** 2025-11-15
**Decision Maker:** Claude
**Category:** Architecture
**Status:** Implemented

#### Context
TASK_MANAGERS supports both embedded milestones (within project JSON) and separate milestone files. Need to choose approach.

#### Options Considered
1. **Embedded:** Milestones array within project_instance.json (like TEMPLATE-PROJ-LG-001)
2. **Separate Files:** Individual JSON files in Milestones/ subfolder
3. **Mixed:** Summary in project JSON, details in separate files

#### Decision
**Chosen: Option 2 - Separate Milestone Files**

Create individual JSON file for each milestone in `Milestones/` subfolder.

#### Rationale
- **Granularity:** Each milestone is complex enough to warrant separate file
- **Tracking:** Easier to update milestone status independently
- **Entity Separation:** Follows TASK_MANAGERS principle of separating entities
- **Documentation:** Milestone_Templates/README.md describes this approach
- **Scalability:** Can add milestone-specific artifacts (logs, reports)

#### Implementation
- 8 separate files: MIL-001 through MIL-008
- Project JSON references milestone IDs
- Milestone files contain full tracking data

#### Consequences
- **Positive:** Better tracking, easier updates, follows best practices
- **Negative:** More files to manage
- **Mitigation:** Clear naming convention, README documentation

---

### DEC-003: Task Instance Location

**Date:** 2025-11-15
**Decision Maker:** Claude
**Category:** Architecture
**Status:** Approved

#### Context
Task instances can be stored in project folder or in TASK_MANAGERS/Tasks/ central location. TASK_MANAGERS/Tasks/ is currently empty (0 files).

#### Options Considered
1. **Project Folder:** Tasks/ subfolder within project
2. **Central Location:** TASK_MANAGERS/Tasks/ (available empty entity)
3. **Both:** Reference in project, full details centrally

#### Decision
**Chosen: Option 2 - Central Location (TASK_MANAGERS/Tasks/)**

Create task instance files in central TASK_MANAGERS/Tasks/ folder.

#### Rationale
- **Leverages Empty Entity:** TASK_MANAGERS/Tasks/ has 0 files, perfect for instances
- **Centralized Tracking:** All task instances across all projects in one place
- **Follows Pattern:** Step instances will also go in TASK_MANAGERS/Steps/
- **Cross-Project Queries:** Easier to find all tasks system-wide
- **Separation of Concerns:** Templates separate from instances

#### Implementation
- Task instances: `TASK_MANAGERS/Tasks/TASK-NMP-XXX.json`
- Project references task IDs
- Naming: TASK-NMP-XXX (NMP = Next Main Prompt)

#### Consequences
- **Positive:** Centralized management, leverages empty entity
- **Negative:** Tasks not co-located with project
- **Mitigation:** Clear references in project and milestone files

---

### DEC-004: Library Integration Approach

**Date:** 2025-11-15
**Decision Maker:** Claude (based on meta-prompt)
**Category:** Design
**Status:** Approved

#### Context
Need to decide how to integrate 12 LIBRARIES entities into v5 structure.

#### Options Considered
1. **Single Integration File:** One file covering all 12 libraries
2. **Grouped Files:** 2-3 files grouping related libraries
3. **Individual Files:** One file per library (12 files)

#### Decision
**Chosen: Option 3 - Individual Library Files**

Create dedicated integration file for each of 12 libraries plus 1 taxonomy framework file (13 total).

#### Rationale
- **Modularity:** Each library is substantial enough for separate file
- **Statistics:** Easier to update individual library statistics
- **Clarity:** Focused documentation per library
- **Maintenance:** Can update one library without affecting others
- **Meta-Prompt Spec:** CREATE_MAIN_PROMPT_v5.md specifies this approach

#### Implementation
- 01_Library_Integration/ folder
- 13 files: 01_Actions through 12_Prompts + 13_Taxonomy_Framework
- Each file follows consistent template structure
- Statistics extracted from actual library files

#### Consequences
- **Positive:** Excellent modularity, easy to maintain
- **Negative:** More files to create (13 vs 1-3)
- **Mitigation:** Template-based approach speeds creation

---

### DEC-005: Output Template Granularity

**Date:** 2025-11-15
**Decision Maker:** Claude (based on meta-prompt)
**Category:** Design
**Status:** Approved

#### Context
MAIN_PROMPT v4 has 21 output sections. Currently split into 2 large files in v4 Modular. Need granularity for v5.

#### Options Considered
1. **Keep 2 Files:** Sections 1-11 and 12-21 (current v4 Modular approach)
2. **5 Files:** Group by category
3. **21 Files:** One file per section

#### Decision
**Chosen: Option 3 - One File Per Section (21 files)**

Create individual file for each of 21 output sections plus README (22 total).

#### Rationale
- **Maximum Modularity:** Smallest logical unit
- **Easier Updates:** Can modify one section without affecting others
- **Library Integration:** Each section has different library integration needs
- **File Size:** Current 55KB file is too large, splitting improves usability
- **Meta-Prompt Spec:** CREATE_MAIN_PROMPT_v5.md specifies this granularity

#### Implementation
- 02_Output_Templates/ folder
- 22 files: README + 01_Meeting_Metadata through 21_Follow_Up_Items
- Each file shows relevant library integration
- Templates include examples and validation checklists

#### Consequences
- **Positive:** Maximum flexibility, easy to maintain
- **Negative:** Many files to manage (22)
- **Mitigation:** Clear naming, README guide, assembly scripts

---

### DEC-006: ID Naming Conventions

**Date:** 2025-11-15
**Decision Maker:** Claude
**Category:** Implementation
**Status:** Implemented

#### Context
Need consistent ID format for project, milestones, tasks, and other entities.

#### Decision
**Chosen: Hierarchical ID System**

- **Project:** PROJ-AI-NMP-001
  - PROJ = Project instance
  - AI = Department
  - NMP = Project abbreviation (Next Main Prompt)
  - 001 = Instance number

- **Milestones:** MIL-001 through MIL-008
  - Simple sequential within project
  - No department prefix (implied by project)

- **Tasks:** TASK-NMP-001 through TASK-NMP-040+
  - NMP links to project
  - Sequential numbering

- **Steps:** STEP-NMP-XXX-YY
  - NMP links to project
  - XXX = task number
  - YY = step number within task

- **Deliverables:** DEL-XXX-YY
  - XXX = milestone number
  - YY = deliverable number within milestone

#### Rationale
- **Consistency:** Follows TASK_MANAGERS conventions
- **Clarity:** Easy to identify entity type and parent
- **Scalability:** Can add more instances
- **Traceability:** Clear relationships between entities

#### Implementation
- Applied across all project files
- Documented in Setup Log
- Referenced in milestone and task files

---

### DEC-007: Logging System Structure

**Date:** 2025-11-15
**Decision Maker:** Claude
**Category:** Architecture
**Status:** Implemented

#### Context
Need comprehensive logging for project tracking. Multiple logging approaches possible.

#### Options Considered
1. **Single Log File:** One file for all logging
2. **Two Log Files:** Setup + Progress
3. **Six Specialized Logs:** Separate logs by purpose

#### Decision
**Chosen: Option 3 - Six Specialized Log Files**

Create 6 dedicated log files:
- 00_Setup_Log.md - Initial configuration
- 01_Progress_Log.md - Daily/weekly progress
- 02_Issues_Log.md - Problems and resolutions
- 03_Decisions_Log.md - Architecture/design decisions
- 04_Statistics_Log.md - Library statistics tracking
- 05_Completion_Report.md - Final summary

#### Rationale
- **Separation of Concerns:** Each log has specific purpose
- **Easier Navigation:** Find relevant information quickly
- **Comprehensive:** Covers all aspects of project lifecycle
- **Historical Record:** Maintains clear audit trail
- **Best Practice:** Follows software project logging patterns

#### Implementation
- All logs in `Logs/` subfolder
- Numbered prefix for ordering
- Markdown format for readability
- Regular updates throughout project

#### Consequences
- **Positive:** Excellent organization, comprehensive tracking
- **Negative:** More files to maintain
- **Mitigation:** Clear purpose for each, templates provided

---

## Decision Template

When logging new decisions, use this format:

```markdown
### DEC-XXX: [Decision Title]

**Date:** YYYY-MM-DD
**Decision Maker:** [Name/Role]
**Category:** Architecture / Design / Implementation
**Status:** Proposed / Approved / Implemented / Rejected

#### Context
[Background and why decision is needed]

#### Options Considered
1. **Option 1:** [Description]
2. **Option 2:** [Description]
3. **Option 3:** [Description]

#### Decision
**Chosen: [Selected Option]**

[Brief statement of decision]

#### Rationale
[Why this option was chosen]
- [Reason 1]
- [Reason 2]
- [Reason 3]

#### Implementation
[How this will be implemented]

#### Consequences
- **Positive:** [Benefits]
- **Negative:** [Drawbacks]
- **Mitigation:** [How negatives are addressed]

#### Related Decisions
[Links to related decisions if applicable]
```

---

## Decision Impact Matrix

| Decision | Milestone Impact | Risk Level | Reversibility |
|----------|------------------|------------|---------------|
| DEC-001 | All | Low | Medium (effort to change) |
| DEC-002 | All | Low | High (easy to change) |
| DEC-003 | MIL-001+ | Low | Medium |
| DEC-004 | MIL-003 | Low | Low (hard to change) |
| DEC-005 | MIL-004 | Low | Low (hard to change) |
| DEC-006 | All | Low | Medium |
| DEC-007 | All | Low | High (easy to change) |

---

## Notes

- All major architectural and design decisions are logged here
- Decisions are numbered sequentially (DEC-001, DEC-002, etc.)
- Each decision includes context, options, rationale, and consequences
- This log serves as project knowledge base and audit trail

---

**Last Updated:** 2025-11-15
**Next Review:** As new decisions are made
