# Milestone Registry (MLT-###)

**Purpose:** Central registry of all milestone IDs used across TSM-007_GUIDES workflows

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active

---

## What is a Milestone?

Per MAIN_PROMPT_v6.md (line 42), **MLT-###** represents a "Milestone Template" - a defined stage or checkpoint within a larger workflow or process.

**Format:** MLT-### (3-digit number, zero-padded)

**Usage:**
- Each milestone represents a discrete phase of work with clear inputs, outputs, and success criteria
- Milestones are sequential within a workflow
- Each workflow (guide) is assigned a block of milestone IDs

---

## Registry

### GDS-001: Daily Task Processing Instructions

**Milestone Range:** MLT-001 through MLT-009 (9 milestones)

**Workflow:** Daily processing of all employee files, task extraction, gap analysis, and distribution

| ID | Name | Duration | Description |
|---|---|---|---|
| MLT-001 | Setup | 10 min | Create daily workspace folder structure |
| MLT-002 | Collection | 30 min | Collect ALL files from ~60 employee folders |
| MLT-003 | Entity Extraction | 60 min | Extract tasks from ALL collected files using MAIN_PROMPT_v6.md |
| MLT-004 | Gap Analysis | 45 min | Perform RESEARCHES gap analysis (EXISTS/LIBRARY_ONLY/NEW) |
| MLT-005 | Template Creation | 30 min | Create new TST-### templates for identified gaps |
| MLT-006 | Task Assignment Planning | 45 min | Apply multi-factor assignment algorithm |
| MLT-007 | Task Distribution | 30 min | Distribute tasks to employee folders (DD+1) |
| MLT-008 | Quality Assurance | 20 min | Verify assignments, check balance, validate templates |
| MLT-009 | Archival & Reporting | 10 min | Generate reports, update metrics, archive workspace |

**Total Time:** 3-4 hours (target: 1-2 hours with automation)

---

### GDS-002: Video Transcript Processing Instructions

**Milestone Range:** MLT-010 through MLT-015 (6 milestones)

**Workflow:** Video transcript processing through RESEARCHES methodology

| ID | Name | Duration | Description |
|---|---|---|---|
| MLT-010 | Search Queue | 2-3h/week | Assign video search tasks to researchers |
| MLT-011 | Video Queue | 30min/week | Prioritize and queue videos for processing |
| MLT-012 | Transcriptions | 40-60min/video | Process video through PMT-004 v3.2 (14 sections) |
| MLT-013 | Analysis & Gap Analysis | 20-30min/video | Extract entities, identify library gaps |
| MLT-014 | Integration | 10-20min/video | Create JSON entities for tools, tasks, skills |
| MLT-015 | Library Mapping | 10min/video | Final documentation and library integration |

**Total Time per Video:** 50-100 minutes (90-95% time savings vs pre-v3.2)

---

## Reserved Ranges

### In Use
- **MLT-001 to MLT-009:** GDS-001 Daily Processing (9 milestones)
- **MLT-010 to MLT-015:** GDS-002 Video Processing (6 milestones)

### Available
- **MLT-016 to MLT-999:** Available for future guides

---

## Future Guides (Planned)

### GDS-003: Employee Onboarding Process
**Reserved Range:** MLT-016 to MLT-025 (tentative)

### GDS-004: Weekly Reporting & Analytics
**Reserved Range:** MLT-026 to MLT-035 (tentative)

### GDS-005: Task Template Maintenance
**Reserved Range:** MLT-036 to MLT-045 (tentative)

### GDS-006: Library Management & Cleanup
**Reserved Range:** MLT-046 to MLT-055 (tentative)

---

## Naming Conventions

### Milestone Names

**Format:** `[Action Verb] + [Object/Context]`

**Examples:**
- Setup (MLT-001)
- Collection (MLT-002)
- Entity Extraction (MLT-003)
- Gap Analysis (MLT-004)
- Task Assignment Planning (MLT-006)

### Milestone Descriptions

Each milestone must include:
1. **Duration estimate** - Typical time required
2. **Input** - What's needed to start
3. **Process** - Key activities
4. **Output** - Deliverables/artifacts created
5. **Success criteria** - How to verify completion

---

## Integration with System Taxonomy

**Milestone Template (MLT-###)** is part of the broader entity taxonomy:

- **TST-###:** Task Template
- **STP-###:** Step Template
- **MLT-###:** Milestone Template
- **ACT-###:** Action
- **OBJ-###:** Object
- **TOL-###:** Tool
- **SKL-###:** Skill

**Reference:** MAIN_PROMPT_v6.md (line 42)

---

## Usage Guidelines

### When to Create a New Milestone

Create a new milestone when:
1. The work represents a distinct phase with clear boundaries
2. The phase has unique inputs, processes, and outputs
3. The phase can be completed independently (though may depend on previous phases)
4. The phase duration is significant enough to track (typically >10 minutes)

### When NOT to Create a Milestone

Don't create milestones for:
1. Individual steps within a larger phase (use STP-### instead)
2. Very brief activities (<5 minutes)
3. Parallel sub-tasks of a single milestone
4. Ad-hoc or one-time activities

### Assigning Milestone IDs

1. **Reserve in blocks:** Allocate 10-20 IDs per guide to allow growth
2. **Sequential within guide:** Number milestones in execution order
3. **Document immediately:** Add to registry when assigned
4. **Never reuse:** Once assigned, never reassign an MLT-### ID

---

## Milestone vs Phase vs Step

**Phase (deprecated):**
- Old terminology, replaced by "Milestone"
- No longer used in system

**Milestone (MLT-###):**
- Major stage in a workflow
- Multiple steps combined
- Duration: typically 10-60 minutes
- Clear deliverable or state change

**Step (STP-###):**
- Individual action within a milestone
- Duration: typically 1-10 minutes
- Part of a task template

**Example Hierarchy:**
```
Workflow: Daily Processing (GDS-001)
├─ Milestone MLT-002: Collection
│  ├─ Step: Navigate to employee folder
│  ├─ Step: Copy all .md files
│  └─ Step: Verify file count
├─ Milestone MLT-003: Entity Extraction
│  ├─ Step: Load MAIN_PROMPT_v6.md
│  ├─ Step: Process each file
│  └─ Step: Save extracted entities
└─ Milestone MLT-004: Gap Analysis
   ├─ Step: Load Task Templates Master
   ├─ Step: Compare extracted vs existing
   └─ Step: Generate gap report
```

---

## Maintenance

### Review Schedule
- **Weekly:** Check for new milestone assignments
- **Monthly:** Verify all in-use IDs are documented
- **Quarterly:** Review reserved ranges, adjust as needed

### Change Process
1. Never delete or modify existing milestone IDs
2. Add new entries to registry immediately upon creation
3. Update guide documentation when milestones change
4. Notify stakeholders if milestone ranges shift

---

## Version History

**Version 1.0** (2025-11-25)
- Initial registry creation
- MLT-001 through MLT-009: GDS-001 Daily Processing
- MLT-010 through MLT-015: GDS-002 Video Processing
- Reserved MLT-016+ for future guides

---

**Document Maintained By:** AI & Automation Team
**Last Updated:** 2025-11-25
**Status:** Active
**Next Review:** 2025-12-25 (1 month)
**Related Documents:**
- MAIN_PROMPT_v6.md (system taxonomy)
- GDS-001 (Daily Processing)
- GDS-002 (Video Processing)
