# Daily Processing Workflow - Milestones Index

**Workflow:** GDS-001 Daily Task Processing Instructions
**Total Milestones:** 9 (MLT-001 through MLT-009)
**Total Duration:** 3-4 hours (goal: 1-2 hours with automation)
**Frequency:** Daily (Monday-Friday)
**Version:** 1.0
**Date Created:** 2025-11-25

---

## Overview

This index provides quick access to all 9 milestones in the Daily Processing workflow. Each milestone is documented in a separate file with detailed instructions, examples, taxonomy references, and employee profile data.

**Purpose:** Process all employees' daily files, extract tasks, create templates, and distribute work assignments fairly across the organization.

---

## The 9 Milestones

### [MLT-001: Setup](MLT-001_Setup.md) ⏱️ 10 min

**What:** Create today's workspace folder structure

**Deliverables:**
- Workspace folder: `/ENTITIES/DAILIES/Daily_Processing/YYYY-MM-DD_Collection/`
- 5 subfolders created
- Processing log initialized

**Key Concepts:**
- Workspace organization
- ISO codes (MLT, TST, GDS)
- Department codes (AID, DGN, LGN, VID, SLS, DEV, HRM)

---

### [MLT-002: Collection](MLT-002_Collection.md) ⏱️ 30 min

**What:** Copy ALL files from every employee's today folder (DD)

**Deliverables:**
- 150-250 .md files collected
- Files renamed with {Dept}_{Employee}_{Filename} pattern
- Saved to `01_Collected_Files/`

**Key Data:**
- ~60 employees across 7 departments
- Employee profile examples (Artemchuk Nikolay, Bogun Polina, Bessarab Valeriia)
- Department ISO codes

---

### [MLT-003: Entity Extraction](MLT-003_Entity_Extraction.md) ⏱️ 60 min

**What:** Extract tasks, actions, objects, tools from all files using MAIN_PROMPT_v6.md

**Deliverables:**
- 60+ extraction files in `02_Extracted_Tasks/`
- 50-100 tasks identified
- All tasks tagged with ACT, OBJ, TOL, SKL, PRF, DPT codes

**Key Data:**
- MAIN_PROMPT_v6.md extraction format
- Actions taxonomy (429 actions)
- Objects taxonomy (50+ objects)
- Tools taxonomy (200+ tools)

---

### [MLT-004: Gap Analysis](MLT-004_Gap_Analysis.md) ⏱️ 45 min

**What:** Classify tasks as EXISTS/LIBRARY_ONLY/NEW using RESEARCHES methodology

**Deliverables:**
- Gap analysis report: `Gap_Analysis_YYYY-MM-DD.md`
- Coverage snapshot (EXISTS vs LIBRARY_ONLY vs NEW breakdown)
- Department-specific analysis

**Key Data:**
- RESEARCHES Gap Analysis methodology
- Current templates: TST-001 to TST-071
- Template ID assignment for new templates

---

### [MLT-005: Template Creation](MLT-005_Template_Creation.md) ⏱️ 30 min

**What:** Create new TST-### templates for LIBRARY_ONLY and NEW tasks

**Deliverables:**
- 28 LIBRARY_ONLY templates
- 14 NEW templates
- Total: 42 new templates (TST-072 to TST-113)
- Missing library entities created (8 tools, 3 objects, 2 skills)

**Key Data:**
- TST template JSON structure
- Template ID ranges by department
- Taxonomy Master List updates

---

### [MLT-006: Task Assignment Planning](MLT-006_Task_Assignment_Planning.md) ⏱️ 45 min

**What:** Assign tasks to employees using multi-factor scoring algorithm

**Deliverables:**
- Assignment plan: `assignment_plan_YYYY-MM-DD.md`
- All 87 tasks assigned to ~59 employees
- Workload balanced (<20% variance)

**Key Data:**
- Multi-factor algorithm (40% profession + 20% department + 20% skills + 20% workload)
- Employee profiles with skills/tools
- Scoring examples for real employees

---

### [MLT-007: Task Distribution](MLT-007_Task_Distribution.md) ⏱️ 30 min

**What:** Create/update tasks.md files in employees' tomorrow folders (DD+1)

**Deliverables:**
- ~59 tasks.md files created/updated
- All 87 tasks distributed
- Files in `/Nov25/{Dept}/{Employee}/Week_X/{DD+1}/tasks.md`

**Key Data:**
- Task file format and structure
- Real examples for 3 employees (Artemchuk, Bogun, Bessarab)
- Distribution verification checklist

---

### [MLT-008: Quality Assurance](MLT-008_Quality_Assurance.md) ⏱️ 20 min

**What:** Verify all tasks assigned correctly, workload balanced, templates created

**Deliverables:**
- QA checklist completed
- All 4 quality gates passed
- Issues documented and resolved

**Key Data:**
- Quality gates (Completeness, Correctness, Distribution, Documentation)
- Sample verification (10 templates, 10 distribution files)
- Success metrics tracking

---

### [MLT-009: Archival & Reporting](MLT-009_Archival_Reporting.md) ⏱️ 10 min

**What:** Archive workspace and update metrics tracking

**Deliverables:**
- Processing_Metrics.csv updated
- Daily_Processing_Master.csv updated
- Workspace archived to `/Archive/YYYY-MM-DD_Collection/`
- Daily summary report generated

**Key Data:**
- Metrics tracking (14 fields)
- Trend analysis (weekly comparison)
- Automation impact projection (81% time reduction potential)

---

## Quick Reference

### File Locations

**Milestone Files (this folder):**
```
/ENTITIES/DAILIES/PLANS/Week_4/
├── 00_Daily_Processing_Milestones_Index.md (this file)
├── MLT-001_Setup.md
├── MLT-002_Collection.md
├── MLT-003_Entity_Extraction.md
├── MLT-004_Gap_Analysis.md
├── MLT-005_Template_Creation.md
├── MLT-006_Task_Assignment_Planning.md
├── MLT-007_Task_Distribution.md
├── MLT-008_Quality_Assurance.md
├── MLT-009_Archival_Reporting.md
└── Daily_Processing_Workflow_Simple.md
```

**Main Workflow Documentation:**
```
/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/
├── Guides/
│   └── GDS-001_Daily_Task_Processing_Instructions.md
├── Support_Files/
│   ├── Task_Assignment_Rules.json
│   ├── Daily_Processing_Master.csv
│   └── Processing_Metrics.csv
└── README.md
```

**Workspace Location:**
```
/ENTITIES/DAILIES/Daily_Processing/
├── YYYY-MM-DD_Collection/          (active workspace)
│   ├── 01_Collected_Files/
│   ├── 02_Extracted_Tasks/
│   ├── 03_Gap_Analysis/
│   ├── 04_Task_Templates/
│   ├── 05_Distribution_Plan/
│   └── 06_Processing_Log.md
└── Archive/                         (completed workspaces)
    └── YYYY-MM-DD_Collection/
```

---

## Milestone Dependencies

```
MLT-001 (Setup)
    ↓
MLT-002 (Collection) ← Uses workspace from MLT-001
    ↓
MLT-003 (Entity Extraction) ← Processes files from MLT-002
    ↓
MLT-004 (Gap Analysis) ← Analyzes tasks from MLT-003
    ↓
MLT-005 (Template Creation) ← Creates templates based on MLT-004
    ↓
MLT-006 (Task Assignment) ← Assigns using templates from MLT-005
    ↓
MLT-007 (Task Distribution) ← Distributes based on plan from MLT-006
    ↓
MLT-008 (Quality Assurance) ← Verifies MLT-001 through MLT-007
    ↓
MLT-009 (Archival & Reporting) ← Archives all outputs
```

---

## Taxonomy Integration

### Entity Types Used

| ISO Code | Entity Type | Usage in Workflow |
|----------|-------------|-------------------|
| **MLT** | Milestone Template | This workflow (MLT-001 to MLT-009) |
| **TST** | Task Template | Created in MLT-005 (TST-072 to TST-113) |
| **GDS** | Guide | Main workflow guide (GDS-001) |
| **ACT** | Actions | Referenced in MLT-003 extraction |
| **OBJ** | Objects | Referenced in MLT-003 extraction |
| **TOL** | Tools | Referenced in MLT-003 extraction |
| **SKL** | Skills | Referenced in MLT-006 assignment |
| **PRF** | Professions | Referenced in MLT-006 assignment |
| **DPT** | Departments | Used throughout for organization |

### Department Codes

| ISO Code | Department | Employees | Common Tasks |
|----------|------------|-----------|--------------|
| **AID** | AI & Automation | ~10 | Project mgmt, automation, reporting |
| **DGN** | Design | ~15 | UI/UX, graphics, branding |
| **LGN** | Lead Generation | ~20 | Prospecting, list building, outreach |
| **VID** | Video Production | ~8 | Video editing, thumbnails, scripts |
| **SLS** | Sales | ~5 | Client relations, follow-ups |
| **DEV** | Development | ~3 | Coding, MCP connectors, APIs |
| **HRM** | Human Resources | ~2 | Recruiting, onboarding |

---

## Employee Profile Examples

### Example 1: Project Manager (AI Dept)

**Profile:** [Artemchuk Nikolay](../../../TALENTS/Employees/profiles/Work/AI/Profile Project manager, Lead generator Artemchuk Nikolay.md)

- **Profession:** Project Manager (PRF-PRJ)
- **Department:** AI & Automation (AID)
- **Key Skills:** Agile, SCRUM, project management, Data Processing
- **Key Tools:** Asana, Jira, Monday, Notion
- **Typical Tasks:** Project updates, weekly reports, team scheduling

### Example 2: UI/UX Designer (Design Dept)

**Profile:** [Bogun Polina](../../../TALENTS/Employees/profiles/Part_Project___Part_Time/Design/Profile UI UX designer Bogun Polina.md)

- **Profession:** UI/UX Designer (PRF-DGN)
- **Department:** Design (DGN)
- **Key Skills:** UX/UI design, prototyping, usability testing, ux writing
- **Key Tools:** Figma, Photoshop, Illustrator
- **Typical Tasks:** Social media posts, email newsletters, UI mockups

### Example 3: Lead Generator (LG Dept)

**Profile:** [Bessarab Valeriia](../../../TALENTS/Employees/profiles/Work/Sales/Profile Lead generator Bessarab Valeriia.md)

- **Profession:** Lead Generator (PRF-LDG)
- **Department:** Lead Generation (LGN)
- **Key Skills:** Lead generation, prospecting
- **Key Tools:** LinkedIn Sales Navigator, CRM
- **Typical Tasks:** Contact exports, lead generation, list building

---

## Key Metrics & Targets

| Metric | Target | Typical Actual |
|--------|--------|----------------|
| **Processing Time** | <4 hours | 3h 20min |
| **Files Collected** | 150-200 | 187 |
| **Tasks Extracted** | 50-100 | 87 |
| **New Templates** | 2-5 | 5-10 (42 on high day) |
| **Employees Assigned** | ~60 | 59 |
| **Distribution Accuracy** | >95% | 100% |
| **Workload Variance** | <20% | 16% |
| **QA Pass Rate** | >90% | 100% |

---

## Automation Opportunities

### Current vs Automated Time

| Milestone | Current | With Scripts | Savings |
|-----------|---------|--------------|---------|
| MLT-002: Collection | 30 min | 2 min | 28 min |
| MLT-003: Extraction | 60 min | 10 min | 50 min |
| MLT-005: Templates | 30 min | 5 min | 25 min |
| MLT-006: Assignment | 45 min | 10 min | 35 min |
| MLT-007: Distribution | 30 min | 5 min | 25 min |
| **TOTAL** | **200 min** | **37 min** | **163 min** |

**Potential Time Reduction:** 81% (from 3h 20min to 37 minutes)

### Priority Scripts to Create

1. **collect_daily_files.py** - Auto-collect from employee folders (saves 28 min)
2. **extract_tasks_batch.py** - Batch extraction with MAIN_PROMPT_v6.md (saves 50 min)
3. **assign_tasks.py** - Apply assignment algorithm (saves 35 min)
4. **distribute_tasks.py** - Auto-create tasks.md files (saves 25 min)

---

## Getting Started

### First Time Processing

**Step 1:** Read the main guide
- [GDS-001: Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)

**Step 2:** Review simple workflow
- [Daily_Processing_Workflow_Simple.md](Daily_Processing_Workflow_Simple.md)

**Step 3:** Read each milestone in order
- Start with MLT-001, proceed sequentially through MLT-009

**Step 4:** Prepare resources
- Load employee profiles: `/ENTITIES/TALENTS/Employees/profiles/Work/`
- Load MAIN_PROMPT_v6.md: `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6.md`
- Load assignment rules: [Task_Assignment_Rules.json](../../Daily_Processing/Daily_Processing_Workflow/Support_Files/Task_Assignment_Rules.json)

**Step 5:** Start with pilot
- Process 5-10 employees first (not all 60)
- Verify output quality
- Expand to full organization

### Daily Processing

**Every Morning:**
1. Start with [MLT-001: Setup](MLT-001_Setup.md)
2. Follow milestones sequentially
3. Update processing log after each milestone
4. Complete with [MLT-009: Archival & Reporting](MLT-009_Archival_Reporting.md)

---

## Success Criteria

### Daily

- ✅ All employee files collected
- ✅ All tasks extracted and assigned
- ✅ Workload balanced across departments
- ✅ All quality gates passed
- ✅ Tasks distributed to tomorrow's folders

### Weekly

- ✅ 5 days of successful processing
- ✅ Template library growing
- ✅ Processing time decreasing
- ✅ Assignment accuracy improving

### Monthly

- ✅ Significant template coverage increase
- ✅ Automation scripts implemented
- ✅ Processing time <2 hours consistently
- ✅ Employee satisfaction with task distribution

---

## Related Documentation

### Core Documents
- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Simple Workflow:** [Daily_Processing_Workflow_Simple.md](Daily_Processing_Workflow_Simple.md)
- **Workspace README:** [Daily_Processing README](../../Daily_Processing/README.md)

### Supporting Files
- **Assignment Rules:** [Task_Assignment_Rules.json](../../Daily_Processing/Daily_Processing_Workflow/Support_Files/Task_Assignment_Rules.json)
- **Processing History:** [Daily_Processing_Master.csv](../../Daily_Processing/Daily_Processing_Workflow/Support_Files/Daily_Processing_Master.csv)
- **Metrics Tracking:** [Processing_Metrics.csv](../../Daily_Processing/Daily_Processing_Workflow/Support_Files/Processing_Metrics.csv)

### Taxonomy
- **Milestone Registry:** [MILESTONE_REGISTRY.md](../../../TASK_MANAGERS/TSM-007_GUIDES/MILESTONE_REGISTRY.md)
- **Task Managers ISO Registry:** [TAX-002 ISO Registry](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md)
- **Libraries ISO Registry:** [TAX-001 ISO Registry](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md)

### Templates & Examples
- **Task Templates:** [TSM-003 Task Templates](../../../TASK_MANAGERS/TSM-003_Task_Templates/)
- **Gap Analysis Examples:** [RESEARCHES Gap Analysis](../../../TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/)
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-25 | Initial creation - all 9 milestones documented with taxonomy data and employee examples | AI Team |

---

## Maintenance

**Update this index when:**
- New milestones added to workflow
- Milestone durations change significantly
- File locations change
- New automation implemented
- Employee examples need updating

**Review Schedule:** Monthly

---

**Document Status:** Active
**Owner:** AI & Automation Team
**Last Updated:** 2025-11-25
**Next Review:** 2025-12-25
