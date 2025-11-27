# Daily Processing Workflow - Simple Explanation

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active
**Source:** [GDS-001 Daily Task Processing Instructions](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Guides/GDS-001_Daily_Task_Processing_Instructions.md)

---

## What It Does

Process all employees' daily files → extract tasks → create missing templates → assign tasks fairly → deliver to tomorrow's folders

---

## The 9 Steps (Milestones)

### MLT-001: Setup (10 min)
**What:** Create today's workspace folder

**Where:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/`

**Create these subfolders:**
```
01_Collected_Files/
02_Extracted_Tasks/
03_Gap_Analysis/
04_Task_Templates/
05_Distribution_Plan/
06_Processing_Log.md
```

---

### MLT-002: Collection (30 min)
**What:** Copy ALL files from every employee's today folder

**From where:**
- `/Nov25/AI/Artemchuk Nikolay/Week_3/25/` (all .md files)
- `/Nov25/Design/Shelep Olha/Week_3/25/` (all .md files)
- ... repeat for ~60 employees

**Copy to:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/01_Collected_Files/`

**Files you collect:**
- daily.md
- plans.md
- tasks.md
- notes.md
- Any other .md files

---

### MLT-003: Entity Extraction (60 min)
**What:** Read all collected files and extract task information

**Use this prompt:**
- `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v7.md`

**Save results to:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/02_Extracted_Tasks/`

**Create files like:**
- `AI_Artemchuk_Nikolay_extracted.md`
- `Design_Shelep_Olha_extracted.md`

---

### MLT-004: Gap Analysis (45 min)
**What:** Check if extracted tasks already have templates or need new ones

**Compare against:**
- `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/` (existing templates)
- `/ENTITIES/LIBRARIES/Tools/` (existing tools)
- `/ENTITIES/LIBRARIES/Actions/` (existing actions)
- `/ENTITIES/LIBRARIES/Objects/` (existing objects)

**Learn from examples:**
- `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/` (see how it's done)

**Save results to:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/03_Gap_Analysis/Gap_Analysis_2025-11-25.md`

**Three outcomes:**
1. **EXISTS** ✅ - Task template already exists → use it
2. **LIBRARY_ONLY** ⚠️ - Tools exist but no template → create template only
3. **NEW** 🆕 - Nothing exists → create tools + template

**Example Gap Analysis:**
```markdown
# Gap Analysis - 2025-11-25

## Coverage Snapshot
- Total tasks extracted: 87
- EXISTS: 45 (52%)
- LIBRARY_ONLY: 28 (32%)
- NEW: 14 (16%)

## EXISTS (Use existing templates)
1. Send_Email_Via_Gmail → TST-045
2. Create_Presentation_PowerPoint → TST-067

## LIBRARY_ONLY (Create template only)
1. Export_Contacts_CSV_LinkedIn
   - Tools exist: TOL-LG-015
   - Create: TST-XXX template

## NEW (Create everything)
1. Generate_Leads_Via_Hunter_IO
   - Missing: Tool Hunter.io
   - Create: TOL-XXX, WRF-XXX, TST-XXX
```

---

### MLT-005: Template Creation (30 min)
**What:** Create new TST-### templates for gaps found

**Save to:**
- `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-XXX_Task_Name.json`

**Also save copy to:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/04_Task_Templates/`

**Format:** JSON files with task details

---

### MLT-006: Task Assignment Planning (45 min)
**What:** Decide which employee gets which task

**Use this algorithm:**
- [Task_Assignment_Rules.json](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Task_Assignment_Rules.json)

**Read employee profiles:**
- `/ENTITIES/TALENTS/Employees/profiles/Work/[Employee_Name].md`

**Scoring (100 points total):**
- Profession match: 40 points
- Department match: 20 points
- Skill level: 20 points
- Workload balance: 20 points

**Save plan to:**
- `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/05_Distribution_Plan/assignment_plan_2025-11-25.md`

---

### MLT-007: Task Distribution (30 min)
**What:** Create/update tasks.md file in each employee's tomorrow folder

**Write to:**
- `/Nov25/AI/Artemchuk Nikolay/Week_3/26/tasks.md`
- `/Nov25/Design/Shelep Olha/Week_3/26/tasks.md`
- ... for all employees with assigned tasks

---

### MLT-008: Quality Assurance (20 min)
**What:** Double-check everything looks good

**Check:**
- All tasks assigned?
- Workload balanced? (<20% variance)
- No employee has >10 tasks?
- Templates created correctly?

---

### MLT-009: Archival & Reporting (10 min)
**What:** Record metrics and archive workspace

**Update these files:**
- [Daily_Processing_Master.csv](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Daily_Processing_Master.csv)
- [Processing_Metrics.csv](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Processing_Metrics.csv)

**Move workspace to:**
- `/ENTITIES/DAILIES/Daily_Processing/Archive/2025-11-25_Collection/`

---

## Key Reference Files

### Main Guide (Read First!)
📄 [GDS-001: Daily Task Processing Instructions](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Guides/GDS-001_Daily_Task_Processing_Instructions.md)

### Supporting Files
📄 [Task Assignment Rules](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Task_Assignment_Rules.json)
📄 [Processing History](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Daily_Processing_Master.csv)
📄 [Metrics Tracking](../../../TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Support_Files/Processing_Metrics.csv)

### Reference Documentation
📄 [Daily Processing Folder README](../Daily_Processing/README.md)
📄 [Milestone Registry](../../../TASK_MANAGERS/TSM-007_GUIDES/MILESTONE_REGISTRY.md)
📄 [TSM-007 Main README](../../../TASK_MANAGERS/TSM-007_GUIDES/README.md)

---

## Quick Summary

**In one sentence:** Collect everyone's today files → extract tasks → create missing templates → assign tasks fairly → deliver to tomorrow's folders.

**Total Time:** 3-4 hours (goal: 1-2 hours with automation)

**Frequency:** Daily (Monday-Friday)

**Target Users:** 1-2 assigned employees (any profession)

---

**Document Created:** 2025-11-25
**Based on:** GDS-001 v1.0
**Maintained By:** AI & Automation Team
