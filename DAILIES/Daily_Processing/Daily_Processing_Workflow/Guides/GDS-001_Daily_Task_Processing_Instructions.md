# GDS-001: Daily Task Processing Instructions

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active
**Target Users:** Any assigned employee (profession-agnostic)

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Daily Workflow - 9 Milestones](#daily-workflow---8-milestones)
4. [Gap Analysis Methodology](#gap-analysis-methodology)
5. [Template Creation Process](#template-creation-process)
6. [Assignment Algorithm](#assignment-algorithm)
7. [Distribution Procedures](#distribution-procedures)
8. [Quality Checks](#quality-checks)
9. [Troubleshooting](#troubleshooting)
10. [Quick Reference](#quick-reference)

---

## Overview

### Purpose

This guide provides step-by-step instructions for processing all employees' daily files, extracting tasks, performing gap analysis, creating templates, and distributing work assignments.

### What You'll Do

1. Collect ALL files from ~60 employees' today's folders (daily.md, plans.md, tasks.md, etc.)
2. Extract tasks using MAIN_PROMPT_v6.md from all collected files
3. Perform gap analysis using RESEARCHES/Gap_Analysis methodology
4. Create new task templates (TST-###) for identified gaps
5. Assign tasks based on profession, department, skills, and workload
6. Distribute tasks to employee folders for tomorrow

### Time Commitment

- **Initial:** 3-4 hours per day
- **With automation:** 1-2 hours per day
- **Frequency:** Daily (Monday-Friday)

### Expected Output

- 50-100 tasks extracted daily
- Gap analysis report
- 2-5 new TST-### templates created
- Tasks distributed to ~30-40 employees
- Daily processing report

---

## Prerequisites

### Required Access

- [ ] Access to `/Users/nikolay/Library/CloudStorage/Dropbox/` directory
- [ ] Access to all department folders in `Nov25/`
- [ ] Access to `ENTITIES/` folder
- [ ] Permission to create files in employee folders

### Required Knowledge

- [ ] Familiarity with markdown format
- [ ] Understanding of entity taxonomy (MLT-###, TST-###, STP-###, etc.)
- [ ] Basic understanding of gap analysis methodology
- [ ] Ability to follow step-by-step instructions

### Files You'll Need

- **MAIN_PROMPT_v6.md:** `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6.md`
- **Gap Analysis Examples:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`
- **Task Templates Master List:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`
- **Assignment Rules:** `/ENTITIES/TASK_MANAGERS/DATA/Task_Assignment_Rules.json`
- **LIBRARIES:** `/ENTITIES/LIBRARIES/` (Tools, Actions, Objects, Skills)

### Tools You'll Use

- **Text editor** (for viewing/editing markdown and JSON files)
- **File manager** (for copying files)
- **Spreadsheet app** (for viewing CSV files)
- **AI assistant** (Claude, ChatGPT with MAIN_PROMPT_v6.md loaded)

---

## Daily Workflow - 9 Milestones

### Milestone MLT-001: Setup (10 minutes)

#### Goal
Prepare your workspace for today's processing

#### Steps

**1. Create Today's Workspace Folder**

Navigate to:
```
/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing/
```

Create folder structure:
```
2025-11-25_Collection/
├── 01_Collected_Files/
├── 02_Extracted_Tasks/
├── 03_Gap_Analysis/
├── 04_Task_Templates/
├── 05_Distribution_Plan/
└── 06_Processing_Log.md
```

Replace `2025-11-25` with today's date (YYYY-MM-DD format).

**2. Initialize Processing Log**

Create `06_Processing_Log.md` with this content:

```markdown
# Daily Processing Log - 2025-11-25

## Start Time: [HH:MM]

## Milestone MLT-001: Setup
- [ ] Workspace created
- [ ] Employee profiles loaded
- [ ] Assignment rules loaded
- [ ] Gap analysis examples reviewed
- [ ] Ready to begin

## Milestone MLT-002: Collection
- Files collected:
- Missing folders:
- Issues:

## Milestone MLT-003: Extraction
- Files processed:
- Tasks extracted:
- Issues:

## Milestone MLT-004: Gap Analysis
- Gaps identified:
- Coverage snapshot created:
- Issues:

[Continue for all milestones...]

## End Time: [HH:MM]
## Total Time: [Duration]
```

**3. Load Employee Profiles**

Open folder: `/ENTITIES/TALENTS/Employees/profiles/Work/`

Count active employees - should be ~60-62 profiles.

**4. Load Assignment Rules**

Open: `/ENTITIES/TASK_MANAGERS/DATA/Task_Assignment_Rules.json`

Review the scoring weights:
- Profession Match: 40%
- Department: 20%
- Skill Level: 20%
- Workload Balance: 20%

**5. Review Gap Analysis Methodology**

Open: `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`

Review 1-2 example gap analysis files to understand the format and methodology.

#### Checklist

- [ ] Today's workspace folder created
- [ ] Processing log initialized
- [ ] Employee profiles count verified (~60-62)
- [ ] Assignment rules reviewed
- [ ] Gap analysis examples reviewed
- [ ] Start time logged

---

### Milestone MLT-002: Collection (30 minutes)

#### Goal
Gather **ALL files** from today's date folder for each employee (not just daily.md)

**IMPORTANT:** You're collecting ALL files: daily.md, plans.md, tasks.md, notes.md, and any other .md or relevant files from today's folder.

#### Process Overview

For each department, scan all employee folders to find today's date folder and copy ALL its contents.

#### Departments to Scan

1. AI
2. Design
3. Dev (Development)
4. LG (Lead Generation)
5. Video
6. Finance
7. HR (Human Resources)
8. Sales
9. Marketing
10. SMM (Social Media Marketing)

#### Steps for Each Department

**1. Navigate to Department Folder**

```
/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/[DEPARTMENT]/
```

**2. For Each Employee Folder**

- Look for today's date folder: `Week_X/DD/`
- Example path: `Nov25/AI/Artemchuk Nikolay/Week_3/20/`

**3. Copy ALL Files from Today's Folder**

Create employee subfolder in collection:
```
2025-11-25_Collection/01_Collected_Files/[Dept]_[EmployeeName]/
```

Copy ALL files from `Week_X/DD/` to this folder:
- daily.md
- plans.md
- tasks.md
- notes.md
- Any other .md files
- Any relevant documents

Naming format for folder: `AI_Artemchuk_Nikolay/`

**4. Document Missing Folders**

If an employee doesn't have today's folder, note it in your Processing Log:

```markdown
## Milestone MLT-002: Collection
Missing folders:
- Design/Bogun Polina - No Week_4 folder
- LG/Hanan Zaheur - Week_4/25 folder empty
```

#### Collection Checklist by Department

```markdown
**AI Department:**
- [ ] Artemchuk Nikolay - Files: daily.md, plans.md
- [ ] Perederii Vladislav - Files: daily.md
- [ ] Zasiadko Matvii - Files: daily.md, tasks.md

**Design Department (~20 employees):**
- [ ] Shelep Olha - Files: daily.md, plans.md, notes.md
- [ ] Bogun Polina - Files: daily.md
- [ ] Kucherenko Iuliia - Files: daily.md, plans.md
- [ ] [Continue for all designers...]

[Continue for all departments...]
```

#### Expected Output

- **Employee folders created:** ~60 folders in `01_Collected_Files/`
- **File types collected:** daily.md, plans.md, tasks.md, notes.md, etc.
- **Naming format:** `[Dept]_[EmployeeName]/`
- **Missing folders documented** in Processing Log

#### Tips

- Start with smaller departments (AI, Video, Finance) to build momentum
- Use file manager to copy entire folder contents at once
- If you find multiple Week folders, use the highest Week number
- If you find multiple DD folders in a Week, use today's DD number (the highest/latest)
- Don't filter files - copy ALL files from today's folder

---

### Milestone MLT-003: Entity Extraction (60 minutes)

#### Goal
Extract tasks and entities from **ALL collected files** (not just daily.md) using MAIN_PROMPT_v6.md

**IMPORTANT:** Process daily.md, plans.md, tasks.md, and any other .md files found in each employee's folder.

#### What You're Extracting

- **MLT-###** (Milestones) - Project milestones mentioned
- **TST-###** (Tasks) - Work activities performed or planned
- **STP-###** (Steps) - Detailed action steps
- **ACT-###** (Actions/Verbs) - Action words used
- **OBJ-###** (Objects/Nouns) - Things worked on
- **TOL-###** (Tools) - Tools/software used
- **SKL-###** (Skills) - Skills demonstrated

#### Process

**1. Load MAIN_PROMPT_v6.md**

Open: `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6.md`

This is your reference for entity extraction logic.

**2. For Each Employee Folder**

Navigate to: `01_Collected_Files/[Dept]_[EmployeeName]/`

**3. Read ALL Files in the Folder**

Process each file found:
- daily.md (daily activities)
- plans.md (planned tasks - often in Russian with "Кто (Who)" assignments)
- tasks.md (task breakdowns with steps)
- notes.md (additional notes)
- Any other .md files

**4. Extract Entities from ALL Files Combined**

Apply MAIN_PROMPT_v6 logic to identify tasks from ALL files:

**From daily.md:**
- What tasks did the employee actually do?
- What tools did they use?
- What were they trying to accomplish?

**From plans.md:**
- What tasks are planned?
- Who are they assigned to ("Кто" field)?
- What's the priority?

**From tasks.md:**
- What are the detailed task breakdowns?
- What steps are involved?

**Combine all sources** to create comprehensive extraction.

**5. Extract Entities**

**Tasks (TST-###):**
- Format: ACTION + OBJECT + CONTEXT
- Example: "CREATE_JOB_POSTING_FOR_HR_MANAGER"
- Example: "ENRICH_EMAILS_VIA_ANYMAILFINDER"

**Steps (STP-###):**
- Format: Specific action within a task
- Example: "LOGIN_TO_LINKEDIN"
- Example: "EXPORT_CONTACTS_TO_CSV"

**Actions (ACT-###):**
- Verbs: Create, Send, Update, Analyze, Review, etc.

**Objects (OBJ-###):**
- Nouns: Job Posting, Email, Proposal, Report, etc.

**Tools (TOL-###):**
- Software: LinkedIn, Gmail, Figma, Claude, etc.

**Skills (SKL-###):**
- Competencies demonstrated

**6. Create Extracted File**

Save to: `02_Extracted_Tasks/[Dept]_[EmployeeName]_extracted.md`

**Format:**

```markdown
# Extracted Entities - [Employee Name]

**Employee:** [Name]
**Department:** [Department]
**Date:** 2025-11-25
**Source Files:** daily.md, plans.md, tasks.md

---

## Tasks Identified

### Task 1: [Task Name in ACTION_OBJECT_CONTEXT format]
- **Description:** [What the task involves]
- **Source:** daily.md (completed) / plans.md (planned) / tasks.md (in progress)
- **Department:** [Primary department]
- **Complexity:** [Low/Medium/High/Very High]
- **Estimated Time:** [Duration if mentioned]
- **Actions:** [ACT-XXX list]
- **Objects:** [OBJ-XXX list]
- **Tools:** [TOL-XXX list]
- **Skills Required:** [SKL-XXX list]

### Task 2: [Next task...]

---

## Steps Identified

### Step 1: [Step Name]
- **Parent Task:** Task 1 above
- **Action:** [ACT-XXX]
- **Tool:** [TOL-XXX]
- **Description:** [What this step does]

### Step 2: [Next step...]

---

## Actions Used
- ACT-XXX: [Action name] (Category: A-G)

## Objects Identified
- OBJ-XXX: [Object name]

## Tools Used
- TOL-XXX: [Tool name] - [Purpose]

## Skills Demonstrated
- SKL-XXX: [Skill description]

---

## Summary
- Total Tasks: X (Y from daily.md, Z from plans.md)
- Total Steps: X
- Complexity Level: [Average]
- Primary Department: [Dept]
```

**7. Repeat for All Employee Folders**

Process all ~60 folders in `01_Collected_Files/`

#### Example Extraction from Multiple Files

**Employee Folder:** `LG_Hanan_Zaheur/`

**File 1: daily.md**
```markdown
# Daily Log - 2025-11-25

## Activities

### 09:00 - LinkedIn Lead Generation
- Logged into LinkedIn Sales Navigator
- Searched for HR Managers
- Exported 50 contacts to CSV
```

**File 2: plans.md** (in Russian)
```markdown
## СРОЧНЫЕ ЗАДАЧИ

### 1. Enrich exported contacts
- **Кто (Who):** Hanan
- **Что (What):** Enrich 50 LinkedIn contacts with emails
- **Приоритет (Priority):** HIGH
```

**Combined Extraction:**

```markdown
# Extracted Entities - Hanan Zaheur

**Employee:** Hanan Zaheur
**Department:** LG
**Date:** 2025-11-25
**Source Files:** daily.md, plans.md

---

## Tasks Identified

### Task 1: GENERATE_LEADS_VIA_LINKEDIN_SALES_NAVIGATOR
- **Description:** Find and export HR Manager contacts from LinkedIn
- **Source:** daily.md (completed today)
- **Department:** LG
- **Complexity:** Medium
- **Estimated Time:** 2 hours
- **Actions:** [ACT-042 (Search), ACT-015 (Export)]
- **Objects:** [OBJ-025 (Contacts), OBJ-018 (CSV File)]
- **Tools:** [TOL-LG-015 (LinkedIn Sales Navigator)]
- **Skills Required:** [SKL-042 (LinkedIn prospecting)]

### Task 2: ENRICH_EMAILS_VIA_ANYMAILFINDER
- **Description:** Enrich 50 LinkedIn contacts with email addresses
- **Source:** plans.md (planned/urgent)
- **Department:** LG
- **Complexity:** Low
- **Estimated Time:** 30 minutes
- **Priority:** HIGH
- **Actions:** [ACT-025 (Enrich)]
- **Objects:** [OBJ-025 (Contacts), OBJ-008 (Email addresses)]
- **Tools:** [TOL-LG-003 (Anymailfinder)]
- **Skills Required:** [SKL-018 (Email enrichment)]

[Continue with steps...]
```

#### Quality Checks

For each extracted file, verify:

- [ ] ALL files in employee folder processed (daily.md, plans.md, tasks.md, etc.)
- [ ] All tasks have ACTION_OBJECT_CONTEXT naming
- [ ] Complexity level assigned
- [ ] Steps linked to parent tasks
- [ ] Entity IDs referenced
- [ ] Department identified
- [ ] Summary section complete
- [ ] Source file noted for each task

#### Tips

- Process similar departments together
- Use AI assistant (Claude/ChatGPT) with MAIN_PROMPT_v6.md loaded
- When extracting from plans.md, look for "Кто (Who)" to identify assignees
- From tasks.md, extract the detailed step breakdowns
- Combine information from all files for comprehensive understanding

#### Expected Output

- **Files created:** ~60 extracted.md files in `02_Extracted_Tasks/`
- **Format:** Structured markdown with all entity types
- **Total tasks extracted:** 50-100 tasks across all employees
- **Sources documented:** Clear indication from which file each task came

---

### Milestone MLT-004: Gap Analysis (45 minutes)

#### Goal
Perform gap analysis using RESEARCHES methodology to identify what exists in LIBRARIES vs TASK_MANAGERS

**IMPORTANT:** This is different from simple template matching. You're identifying:
1. What's already in TASK_MANAGERS (use as-is)
2. What's in LIBRARIES but not in TASK_MANAGERS (create template)
3. What's completely new (create template + library entries)

#### Gap Analysis Methodology

Based on: `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`

**Coverage Snapshot Format:**

| Entity Group | Total Identified | Already in Libraries? | Gaps / Notes | Priority |
|--------------|-----------------|------------------------|--------------|----------|
| Tools (TOL) | X | Y exist, Z missing | Need ... | HIGH/MED/LOW |
| Workflows (WRF) | X | Y exist, Z missing | Need ... | HIGH/MED/LOW |
| Tasks (TSK) | X | Y exist, Z missing | Need ... | HIGH/MED/LOW |
| Steps (STP) | X | Y exist, Z missing | Need ... | HIGH/MED/LOW |
| Objects (OBJ) | X | Y exist, Z missing | Need ... | HIGH/MED/LOW |
| Actions (ACT) | X | Covered | No action | LOW |
| Skills (SKL) | X | Y exist, Z missing | Need ... | MED |

#### Process

**1. Load Reference Files**

Open these for comparison:
- **TASK_MANAGERS:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`
- **LIBRARIES Tools:** `/ENTITIES/LIBRARIES/LBS_003_Tools/`
- **LIBRARIES Actions:** `/ENTITIES/LIBRARIES/LBS_001_Actions/`
- **LIBRARIES Objects:** `/ENTITIES/LIBRARIES/LBS_002_Objects/`
- **LIBRARIES Skills:** `/ENTITIES/LIBRARIES/LBS_004_Skills/`

**2. Create Gap Analysis Document**

Create: `03_Gap_Analysis/Gap_Analysis_2025-11-25.md`

**3. For Each Entity Type, Analyze Coverage**

**Tools (TOL) Analysis:**
```markdown
### Tools Library (LBS_003_Tools)

| Tool | Status | Required Actions | Priority |
|------|--------|------------------|----------|
| LinkedIn Sales Navigator (TOL-LG-015) | EXISTS in LIBRARIES | No action - already documented | LOW |
| Anymailfinder (TOL-LG-003) | EXISTS in LIBRARIES | No action - already documented | LOW |
| New_Tool_XYZ | MISSING from LIBRARIES | Create new tool file TOL-XXX-YYY | HIGH |
```

**Workflows/Tasks Analysis:**
```markdown
### Task Templates (TASK_MANAGERS)

| Task | In TASK_MANAGERS? | In LIBRARIES (Tools/Actions)? | Gap Type | Action |
|------|-------------------|------------------------------|----------|---------|
| GENERATE_LEADS_VIA_LINKEDIN | YES (TST-018) | Tools exist in LIBRARIES | EXISTS | Use TST-018 |
| PROCESS_DAILY_FILES_WITH_AI | NO | Tools exist in LIBRARIES | LIBRARY_ONLY | Create new TST-XXX |
| NEW_UNIQUE_TASK | NO | Some tools missing | NEW | Create TSK + missing TOL |
```

**Gap Classification:**

**EXISTS:**
- Task template already in TASK_MANAGERS
- All required tools/actions in LIBRARIES
- **Action:** Use existing template, no creation needed

**LIBRARY_ONLY:**
- No task template in TASK_MANAGERS
- BUT all required tools/actions exist in LIBRARIES
- **Action:** Create new task template (TST-XXX) referencing existing library entities

**NEW:**
- No task template in TASK_MANAGERS
- Some/all tools or objects missing from LIBRARIES
- **Action:** Create task template + create missing library entries

**4. Generate Coverage Snapshot**

Summary table for the day:

```markdown
## Coverage Snapshot - 2025-11-25

| Entity Group | Total Identified | Already Exist | Gaps | Priority |
|--------------|-----------------|---------------|------|----------|
| Tools (TOL) | 34 unique tools | 28 in LIBRARIES | 6 missing | HIGH |
| Task Templates (TSK) | 87 tasks | 65 match existing | 22 need creation | HIGH |
| Steps (STP) | 215 steps | Mostly covered | Link to new tasks | MED |
| Objects (OBJ) | 42 objects | 35 in LIBRARIES | 7 missing | MED |
| Actions (ACT) | Covered by A-G categories | All exist | None | LOW |
| Skills (SKL) | 28 skills | 25 in LIBRARIES | 3 missing | MED |
```

**5. Detailed Gaps & Recommendations**

For each gap category, document:

```markdown
## Detailed Gaps & Recommendations

### Tools Library Gaps
- **TOL-XXX:** New_Tool_Name - MISSING
  - **Action:** Create new tool file under appropriate category
  - **Priority:** HIGH
  - **Owner:** [Department]

### Task Template Gaps
- **TST-125:** PROCESS_DAILY_FILES_WITH_AI - LIBRARY_ONLY
  - **Action:** Create new task template, all tools exist
  - **Priority:** HIGH
  - **Type:** LIBRARY_ONLY

- **TST-126:** NEW_COMPLEX_WORKFLOW - NEW
  - **Action:** Create task template + missing tool TOL-XXX-YYY
  - **Priority:** HIGH
  - **Type:** NEW

### Object Library Gaps
- **OBJ-XXX:** New_Object_Type - MISSING
  - **Action:** Create new object entry
  - **Priority:** MED
```

**6. Risk Assessment**

```markdown
## Risks & Impact

| Risk | Impact | Mitigation |
|------|--------|------------|
| Missing tool documentation | Teams can't replicate workflows | Create tool entries before templates |
| Task templates without library support | Incomplete references | Ensure tools/objects exist first |
| Duplicate creation | Inconsistency | Thorough gap analysis prevents this |
```

**7. Next Steps**

```markdown
## Next Steps (Milestone MLT-005: Template Creation)

1. Create missing tool files (6 tools)
2. Create missing object entries (7 objects)
3. Create 22 new task templates:
   - 15 LIBRARY_ONLY type (quick - just reference existing)
   - 7 NEW type (requires new library entries first)
4. Update master CSVs
5. Log progress
```

#### Gap Analysis Document Format

Complete format:

```markdown
# Gap Analysis - Daily Processing 2025-11-25

**Date:** 2025-11-25
**Scope:** All employee files processed (~60 employees)
**Total Tasks Extracted:** 87
**Analyst:** [Your Name]

---

## 1. Coverage Snapshot

[Coverage table as shown above]

---

## 2. Detailed Gaps & Recommendations

### 2.1 Tools Library (LIBRARIES/LBS_003_Tools)
[Tools gap table]

### 2.2 Task Templates (TASK_MANAGERS/TSM-003_Task_Templates)
[Tasks gap table]

### 2.3 Objects Library (LIBRARIES/LBS_002_Objects)
[Objects gap table]

### 2.4 Skills Library (LIBRARIES/LBS_004_Skills)
[Skills gap table]

---

## 3. Gap Classification Summary

**EXISTS (Use as-is):** 65 tasks
- These match existing templates exactly
- No creation needed, just assign

**LIBRARY_ONLY (Create template only):** 15 tasks
- All tools/objects already in LIBRARIES
- Need task template creation
- Quick to implement

**NEW (Create template + library entries):** 7 tasks
- Require new tool/object entries first
- Then create task templates
- More work involved

---

## 4. Risks & Impact
[Risk table]

---

## 5. Next Steps
[Action list for Phase 4]

---

**Status:** Gap Analysis Complete - Ready for Phase 4
**Date:** 2025-11-25
```

#### Checklist

- [ ] All entity types analyzed (Tools, Tasks, Objects, Skills)
- [ ] Coverage snapshot created
- [ ] Each gap classified (EXISTS/LIBRARY_ONLY/NEW)
- [ ] Detailed recommendations documented
- [ ] Priorities assigned (HIGH/MED/LOW)
- [ ] Risk assessment completed
- [ ] Next steps outlined
- [ ] Gap_Analysis_2025-11-25.md saved

#### Expected Output

- **Document:** `03_Gap_Analysis/Gap_Analysis_2025-11-25.md`
- **EXISTS tasks:** ~65 (use existing templates)
- **LIBRARY_ONLY tasks:** ~15 (create templates)
- **NEW tasks:** ~7 (create templates + library entries)
- **Missing tools identified:** ~6
- **Missing objects identified:** ~7
- **Missing skills identified:** ~3

---

### Milestone MLT-005: Create Task Templates (30 minutes)

#### Goal
Create TST-### JSON files for tasks identified in Gap Analysis as LIBRARY_ONLY or NEW

**Note:** Only create templates for gaps, not for EXISTS tasks.

#### From Gap Analysis

From Phase 3, you identified:
- **EXISTS:** 65 tasks → Skip (use existing templates)
- **LIBRARY_ONLY:** 15 tasks → Create templates (this milestone)
- **NEW:** 7 tasks → Create library entries first, then templates

#### Process

**1. Create Missing Library Entries First (for NEW tasks)**

For tasks marked as NEW with missing tools/objects:

**Create Tool Entries:**
- Location: `/ENTITIES/LIBRARIES/LBS_003_Tools/[Category]/`
- Format: TOL-[CATEGORY]-###
- Follow existing tool JSON schema

**Create Object Entries:**
- Location: `/ENTITIES/LIBRARIES/LBS_002_Objects/`
- Format: OBJ-###
- Follow existing object JSON schema

**2. Get Next Template ID**

Open: `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`

Find the highest TST-### number. Add 1 for your first new template.

Example: If highest is TST-124, your new templates start at TST-125.

**3. For Each Template to Create (22 total: 15 LIBRARY_ONLY + 7 NEW)**

Create a JSON file following this schema:

**File Path:**
```
/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-XXX_[Task_Name].json
```

Also save copy to workspace:
```
04_Task_Templates/TST-XXX_[Task_Name].json
```

**JSON Schema:**

```json
{
  "entity_type": "Task_Template",
  "task_id": "TST-125",
  "name": "PROCESS_DAILY_FILES_WITH_AI",
  "description": "Process employee daily.md, plans.md, tasks.md files using AI to extract tasks and entities",
  "department": "AI",
  "profession": "AI Specialist",
  "complexity": "High",
  "time_estimate": "3-4 hours",
  "actions": [
    "ACT-014",
    "ACT-042"
  ],
  "objects": [
    "OBJ-025",
    "OBJ-018"
  ],
  "tools": [
    "TOL-AI-015"
  ],
  "skills_required": [
    "SKL-042",
    "SKL-038"
  ],
  "steps": [
    "STP-125-01",
    "STP-125-02",
    "STP-125-03"
  ],
  "dependencies": [
    "Access to all employee daily files",
    "MAIN_PROMPT_v6.md loaded",
    "Employee profiles available"
  ],
  "success_criteria": [
    "All daily files collected",
    "Entities extracted from each file",
    "Tasks assigned to employees",
    "Distribution complete"
  ],
  "gap_type": "LIBRARY_ONLY",
  "created_date": "2025-11-25",
  "created_by": "Daily Processing System",
  "status": "Active"
}
```

**Note the gap_type field** - use "LIBRARY_ONLY" or "NEW" based on Gap Analysis.

**4. Update Master List CSV**

Open: `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`

Add new rows for all 22 templates created:

```csv
TST-125,PROCESS_DAILY_FILES_WITH_AI,Process employee files using AI,AI,High,Active,2025-11-25
TST-126,UPDATE_CATALOG_FROM_SPREADSHEET,Update catalog from spreadsheet,Operations,Medium,Active,2025-11-25
[... continue for all 22 templates]
```

#### Validation Checklist

For each new template:

- [ ] Task ID sequential and unique
- [ ] Name in ACTION_OBJECT_CONTEXT format
- [ ] All required fields completed
- [ ] Entity references valid (ACT-XXX, OBJ-XXX, TOL-XXX, SKL-XXX)
- [ ] References only entities that exist (created missing ones first for NEW type)
- [ ] Complexity realistic
- [ ] Time estimate reasonable
- [ ] gap_type field included (LIBRARY_ONLY or NEW)
- [ ] JSON syntax valid
- [ ] File saved to both locations (permanent + workspace)
- [ ] Master CSV updated

#### Expected Output

- **New templates created:** 22 JSON files (15 LIBRARY_ONLY + 7 NEW)
- **New library entries:** ~6 tools, ~7 objects, ~3 skills (for NEW tasks)
- **Location:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-XXX_*.json`
- **Workspace copies:** `04_Task_Templates/TST-XXX_*.json`
- **Master CSV updated:** 22 new entries added

---

### Milestone MLT-006: Task Assignment Planning (45 minutes)

#### Goal
Determine which employee should receive each task tomorrow based on profession, department, skills, and workload

**Note:** You're assigning the 87 tasks extracted in Phase 2 (using existing templates for 65, new templates for 22).

[Assignment Algorithm section remains the same as in the original - using the 40/20/20/20 scoring system]

---

### Milestone MLT-007: Task Distribution (30 minutes)

[Distribution procedures remain the same as in the original]

---

### Milestone MLT-008: Quality Assurance (20 minutes)

#### QA Checklist

**Milestones MLT-001-002: Setup & Collection**

- [ ] Workspace folder structure created
- [ ] ~60 employee folders collected (not just daily.md files!)
- [ ] ALL files collected from each employee's today folder
- [ ] Missing folders documented in Processing Log
- [ ] All departments scanned

**Milestone MLT-003: Extraction**

- [ ] ~60 extracted.md files created
- [ ] ALL source files processed (daily.md, plans.md, tasks.md, etc.)
- [ ] All tasks have ACTION_OBJECT_CONTEXT naming
- [ ] Entities tagged (MLT-###, TST-###, STP-###, etc.)
- [ ] Source file noted for each task
- [ ] Complexity levels assigned
- [ ] Summary sections complete

**Milestone MLT-004: Gap Analysis**

- [ ] Gap_Analysis_2025-11-25.md created
- [ ] Coverage snapshot completed
- [ ] All tasks categorized (EXISTS/LIBRARY_ONLY/NEW)
- [ ] Missing tools identified
- [ ] Missing objects identified
- [ ] Priorities assigned
- [ ] Risk assessment completed
- [ ] Next steps documented

**Milestone MLT-005: Template Creation**

- [ ] Missing library entries created first (for NEW tasks)
- [ ] New TST-### templates created (22 expected)
- [ ] IDs sequential and unique
- [ ] gap_type field included
- [ ] All entity references valid
- [ ] JSON syntax valid
- [ ] Files saved to permanent location
- [ ] Workspace copies saved
- [ ] Master CSV updated

**Milestone MLT-006: Assignment Planning**

- [ ] assignment_plan.md created
- [ ] All 87 tasks assigned
- [ ] Scoring documented
- [ ] No employee >10 tasks
- [ ] Workload variance <20%

**Milestone MLT-007: Distribution**

- [ ] Correct date calculated (DD+1)
- [ ] Tomorrow's folders created
- [ ] All tasks.md files created (30-40 expected)
- [ ] Markdown formatting correct

[Continue with validation process as in original]

---

### Milestone MLT-009: Archival & Reporting (10 minutes)

[Archival and reporting procedures remain the same, but update the summary report to include:]

```markdown
# Daily Processing Summary - 2025-11-25

## Metrics

### Collection Phase
- **Employee Folders Collected:** 62 (out of 62 employees)
- **Total Files Collected:** 156 files
  - daily.md: 62
  - plans.md: 48
  - tasks.md: 32
  - notes.md: 14
- **Missing Folders:** 0

### Extraction Phase
- **Files Processed:** 156 total
- **Tasks Extracted:** 87 total
- **Sources:**
  - From daily.md: 45 tasks
  - From plans.md: 32 tasks
  - From tasks.md: 10 tasks

### Gap Analysis Phase
- **Total Entities Analyzed:** 87 tasks, 34 tools, 42 objects
- **Categorization:**
  - EXISTS: 65 tasks (use existing templates)
  - LIBRARY_ONLY: 15 tasks (create templates)
  - NEW: 7 tasks (create templates + library entries)
- **Library Gaps Identified:**
  - Missing Tools: 6
  - Missing Objects: 7
  - Missing Skills: 3

### Template Creation Phase
- **New Templates Created:** 22 (15 LIBRARY_ONLY + 7 NEW)
- **New Library Entries:** 16 (6 tools + 7 objects + 3 skills)
- **Template IDs:** TST-125 through TST-146

[Continue with rest of summary...]
```

---

## Gap Analysis Methodology

### Understanding Gap Analysis

Gap analysis identifies what's missing by comparing:
1. **Extracted entities** (from employee files)
2. **TASK_MANAGERS** (task templates, workflows, milestones)
3. **LIBRARIES** (tools, actions, objects, skills)

### The Three Gap Types

**1. EXISTS**
- Task pattern already in TASK_MANAGERS
- All required tools/objects in LIBRARIES
- **Action:** Use existing template
- **Example:** GENERATE_LEADS_VIA_LINKEDIN matches TST-018

**2. LIBRARY_ONLY**
- No task template in TASK_MANAGERS
- BUT all tools/actions/objects exist in LIBRARIES
- **Action:** Create new task template only
- **Example:** PROCESS_DAILY_FILES_WITH_AI - Claude exists in LIBRARIES, just need template

**3. NEW**
- No task template in TASK_MANAGERS
- Some/all required tools/objects missing from LIBRARIES
- **Action:** Create library entries first, then task template
- **Example:** USE_NEW_TOOL_XYZ - neither template nor tool exists

### How to Identify Gap Type

**Step 1: Check TASK_MANAGERS**
- Open Task_Templates_Master_List.csv
- Search for similar task names
- If exact match found → EXISTS
- If no match found → Continue to Step 2

**Step 2: Check LIBRARIES (for non-EXISTS tasks)**
- List all tools mentioned in task
- Check if each exists in LIBRARIES/LBS_003_Tools/
- List all objects mentioned
- Check if each exists in LIBRARIES/LBS_002_Objects/
- If ALL exist → LIBRARY_ONLY
- If ANY missing → NEW

**Example Process:**

**Task:** ENRICH_EMAILS_VIA_ANYMAILFINDER

**Step 1:** Check TASK_MANAGERS
- Found: TST-003 "ENRICH_EMAILS_VIA_ANYMAILFINDER"
- **Result:** EXISTS → Use TST-003

**Task:** CREATE_SOCIAL_MEDIA_CAMPAIGN_WITH_AI

**Step 1:** Check TASK_MANAGERS
- No match found
- **Continue to Step 2**

**Step 2:** Check LIBRARIES
- Tools needed: Claude (TOL-AI-015), Instagram (TOL-SMM-008)
- Claude: EXISTS ✓
- Instagram: EXISTS ✓
- Objects needed: Campaign (OBJ-042), Post (OBJ-015)
- Campaign: EXISTS ✓
- Post: EXISTS ✓
- **Result:** LIBRARY_ONLY → Create task template only

**Task:** ANALYZE_DATA_WITH_NEW_AI_TOOL_XYZ

**Step 1:** Check TASK_MANAGERS
- No match found
- **Continue to Step 2**

**Step 2:** Check LIBRARIES
- Tools needed: AI_Tool_XYZ
- AI_Tool_XYZ: MISSING ✗
- **Result:** NEW → Create tool entry first, then task template

### Gap Analysis Best Practices

1. **Be thorough** - Check every tool, object, skill mentioned
2. **Use exact matching** - "LinkedIn Sales Navigator" ≠ "LinkedIn"
3. **Document reasoning** - Note why you classified as EXISTS/LIBRARY_ONLY/NEW
4. **Prioritize** - NEW tasks take longer (create library entries first)
5. **Track coverage** - Use the snapshot table to show overall health

---

## Quick Reference

### Phase Checklist

```
[ ] Milestone MLT-001: Setup (10 min)
[ ] Milestone MLT-002: Collection - ALL files (30 min)
[ ] Milestone MLT-003: Extraction - from ALL files (60 min)
[ ] Milestone MLT-004: Gap Analysis - using RESEARCHES methodology (45 min)
[ ] Milestone MLT-005: Templates - create based on gaps (30 min)
[ ] Milestone MLT-006: Assignment (45 min)
[ ] Milestone MLT-007: Distribution (30 min)
[ ] Milestone MLT-008: QA (20 min)
[ ] Milestone MLT-009: Reporting (10 min)

Total: 3-4 hours
```

### Key Changes from Standard Process

**Collection (Phase 1):**
- ✅ Collect ALL files, not just daily.md
- ✅ Include plans.md, tasks.md, notes.md, etc.
- ✅ Copy entire today's folder contents

**Extraction (Phase 2):**
- ✅ Process ALL collected files
- ✅ Extract from daily.md, plans.md, tasks.md combined
- ✅ Note source file for each task

**Gap Analysis (Phase 3):**
- ✅ Use RESEARCHES/Gap_Analysis methodology
- ✅ Compare against both TASK_MANAGERS and LIBRARIES
- ✅ Classify as EXISTS/LIBRARY_ONLY/NEW
- ✅ Create coverage snapshot
- ✅ Identify missing library entries

**Template Creation (Phase 4):**
- ✅ Create missing library entries first (for NEW tasks)
- ✅ Create templates for LIBRARY_ONLY and NEW (not EXISTS)
- ✅ Include gap_type field in JSON

### Key File Paths

```
Workspace:
/ENTITIES/DAILIES/Daily_Processing/YYYY-MM-DD_Collection/

Employee Files (collect ALL from today's folder):
/Nov25/[Dept]/[Employee Name]/Week_X/DD/
  ├── daily.md
  ├── plans.md
  ├── tasks.md
  └── [other files]

Gap Analysis Reference:
/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/

Templates:
/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/

Libraries:
/ENTITIES/LIBRARIES/
  ├── LBS_001_Actions/
  ├── LBS_002_Objects/
  ├── LBS_003_Tools/
  └── LBS_004_Skills/

Main Prompt:
/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6.md
```

### Gap Type Quick Reference

```
EXISTS:
- In TASK_MANAGERS? YES
- In LIBRARIES? YES
- Action: Use existing template

LIBRARY_ONLY:
- In TASK_MANAGERS? NO
- In LIBRARIES? YES (all tools/objects exist)
- Action: Create task template only

NEW:
- In TASK_MANAGERS? NO
- In LIBRARIES? NO (some/all missing)
- Action: Create library entries + task template
```

---

**End of Guide**

---

**Document Maintained By:** AI & Automation Team
**Last Updated:** 2025-11-25
**Status:** Active - Production Ready
**Next Review:** 2025-12-25 (1 month)
