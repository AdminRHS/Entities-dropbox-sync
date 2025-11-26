# MLT-006: Task Assignment Planning

**Milestone ID:** MLT-006
**Milestone Name:** Task Assignment Planning
**Duration:** 45 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 6 of 9

---

## Overview

Assign all 87 extracted tasks to appropriate employees using the multi-factor scoring algorithm. Balance workload across departments while matching skills, professions, and department affinity.

---

## What You'll Do

### 1. Load Assignment Algorithm

**Algorithm Location:**
```
/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files/Task_Assignment_Rules.json
```

**Multi-Factor Scoring System (100 points total):**

| Factor | Weight | Max Points |
|--------|--------|------------|
| **Profession Match** | 40% | 40 points |
| **Department Match** | 20% | 20 points |
| **Skill Level Match** | 20% | 20 points |
| **Workload Balance** | 20% | 20 points |

---

### 2. Scoring Breakdown

#### Factor 1: Profession Match (40 points)

| Match Type | Points | Example |
|------------|--------|---------|
| **Perfect Match** | 40 | Designer task → Designer employee |
| **Partial Match** | 30 | UI/UX task → Graphic Designer |
| **Transferable** | 20 | Project Management → Team Lead |
| **No Match** | 0 | Developer task → Designer |

**Examples:**

**Task:** Create_UI_Design_Figma (requires PRF-DGN: Designer)

| Employee | Profession | Score |
|----------|------------|-------|
| Bogun Polina | UI/UX Designer | 40 (Perfect) |
| Shelep Olha | Graphic Designer | 30 (Partial) |
| Artemchuk Nikolay | Project Manager | 0 (No Match) |

#### Factor 2: Department Match (20 points)

| Match Type | Points | Example |
|------------|--------|---------|
| **Same Department** | 20 | Design task → Design employee |
| **Related Department** | 10 | Video task → Design employee |
| **Unrelated Department** | 0 | LG task → Video employee |

**Department Relationships:**

Related departments:
- Design ↔ Video
- AI ↔ Development
- Sales ↔ Lead Generation

#### Factor 3: Skill Level Match (20 points)

| Match Type | Points | Example |
|------------|--------|---------|
| **Skill Exact Match** | 20 | Has "UI design via Figma" |
| **Close Match** | 10 | Has "Figma" but not UI design |
| **Mismatch** | -10 | Missing required skill (penalty) |

**Check employee skills:**
- Employee profile: `/ENTITIES/TALENTS/Employees/profiles/{Dept}/{Employee}.md`
- Look at "Skills" section
- Match against task's `skills_required`

#### Factor 4: Workload Balance (20 points)

| Current Workload | Points | Example |
|------------------|--------|---------|
| **0-2 tasks** | 20 | Lightly loaded |
| **3-5 tasks** | 15 | Normal load |
| **6-8 tasks** | 10 | Heavy load |
| **9-10 tasks** | 5 | Maximum capacity |
| **>10 tasks** | Excluded | Overloaded |

**Workload Limits:**
- Maximum: 10 tasks/employee/day
- Preferred: 5 tasks/employee/day
- Target variance: <20% across department

---

## Assignment Process

### Step 1: Load Employee Profiles

**Profile Location:**
```
/ENTITIES/TALENTS/Employees/profiles/Work/{Department}/{Employee}.md
```

**Extract for each employee:**
- Name
- Profession
- Department
- Skills (comma-separated list)
- Tools (comma-separated list)
- Nov25 Folder path

**Example Profile Data:**

```json
{
  "name": "Artemchuk Nikolay",
  "profession": "project manager",
  "profession_code": "PRF-PRJ",
  "department": "AI",
  "department_code": "AID",
  "skills": [
    "Account Management",
    "Agile",
    "Data Processing",
    "Kanban",
    "project management",
    "SCRUM",
    "Waterfall"
  ],
  "tools": [
    "Asana",
    "Jira",
    "Monday",
    "Notion",
    "Slack",
    "Trello"
  ],
  "nov25_folder": "/Dropbox/Nov25/AI/Artemchuk Nikolay",
  "current_workload": 0
}
```

### Step 2: Score Each Task-Employee Pair

For each of 87 tasks, score against all ~60 employees:

**Task Example:** TST-072: Export_Contacts_CSV_LinkedIn

| Employee | Profession (40) | Department (20) | Skill (20) | Workload (20) | **Total** |
|----------|----------------|----------------|------------|---------------|-----------|
| Bessarab Valeriia | 40 (Lead Gen) | 20 (LG) | 20 (LinkedIn) | 20 (0 tasks) | **100** ✅ |
| Kovalska Anastasiya | 30 (Sales Mgr) | 10 (Sales/LG) | 10 (has LinkedIn) | 20 (1 task) | **70** |
| Artemchuk Nikolay | 0 (PM) | 0 (AI) | 0 (no LG skills) | 20 (0 tasks) | **20** |

**Winner:** Bessarab Valeriia (100 points) → Assign task

### Step 3: Apply Constraints

**Hard Constraints:**
- ❌ Never assign >10 tasks to one employee
- ❌ Never assign task requiring missing skill
- ❌ Never assign cross-department unless related

**Soft Constraints:**
- ⚠️ Prefer <5 tasks per employee
- ⚠️ Prefer employees with <8 tasks
- ⚠️ Keep department variance <20%

### Step 4: Balance Workload

After initial assignment, check variance:

```
Department workload variance = (Max - Min) / Average * 100%
```

**Example:**
- Design: 10 employees, 52 tasks → 5.2 tasks/employee
- If one employee has 10 tasks and another has 1 task:
  - Variance = (10 - 1) / 5.2 * 100% = 173% ❌
  - **Action:** Redistribute tasks

**Target:** <20% variance per department

---

## Output Format

**Save to:**
```
/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/05_Distribution_Plan/assignment_plan_2025-11-25.md
```

**Structure:**

```markdown
# Task Assignment Plan - 2025-11-25

**Distribution Date:** 2025-11-26 (tomorrow)
**Tasks Assigned:** 87
**Employees Assigned:** 58
**Planner:** [Your Name]

---

## Assignment Summary by Department

### AI & Automation (AID)
- **Employees:** 10
- **Tasks Assigned:** 18
- **Avg Tasks/Employee:** 1.8
- **Max Tasks (Single Employee):** 4 (Artemchuk Nikolay)
- **Workload Variance:** 15% ✅

### Design (DGN)
- **Employees:** 15
- **Tasks Assigned:** 22
- **Avg Tasks/Employee:** 1.5
- **Max Tasks (Single Employee):** 3 (Bogun Polina)
- **Workload Variance:** 12% ✅

### Lead Generation (LGN)
- **Employees:** 20
- **Tasks Assigned:** 25
- **Avg Tasks/Employee:** 1.25
- **Max Tasks (Single Employee):** 5 (Bessarab Valeriia)
- **Workload Variance:** 18% ✅

[...continue for all departments]

---

## Detailed Task Assignments

### Artemchuk Nikolay (AI & Automation)
**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Work/AI/Profile Project manager, Lead generator Artemchuk Nikolay.md`
**Profession:** Project Manager (PRF-PRJ)
**Department:** AI & Automation (AID)
**Nov25 Folder:** `/Nov25/AI/Artemchuk Nikolay/Week_3/26/`

**Tasks Assigned: 4**

#### Task 1: TST-075 - Update_Project_Status_Notion
**Score:** 95 points
- Profession: 40 (Perfect - PM task)
- Department: 20 (AI dept)
- Skill: 20 (Has Notion skill)
- Workload: 15 (3 tasks already)
**Priority:** High
**Estimated Duration:** 20 minutes

#### Task 2: TST-076 - Generate_Weekly_Report_Google_Sheets
**Score:** 90 points
- Profession: 40 (Perfect - PM task)
- Department: 20 (AI dept)
- Skill: 15 (Has Data Processing)
- Workload: 15 (3 tasks already)
**Priority:** High
**Estimated Duration:** 30 minutes

[...list all 4 tasks]

---

### Bogun Polina (Design)
**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Part_Project___Part_Time/Design/Profile UI UX designer Bogun Polina.md`
**Profession:** UI/UX Designer (PRF-DGN)
**Department:** Design (DGN)
**Nov25 Folder:** `/Nov25/Design/Bogun Polina/Week_3/26/`

**Tasks Assigned: 3**

#### Task 1: TST-074 - Create_Social_Media_Post_Instagram
**Score:** 100 points
- Profession: 40 (Perfect - Design task)
- Department: 20 (Design dept)
- Skill: 20 (Has design layout, mobile design)
- Workload: 20 (0 tasks)
**Priority:** High
**Estimated Duration:** 45 minutes

#### Task 2: TST-077 - Design_Email_Newsletter_Figma
**Score:** 100 points
- Profession: 40 (Perfect - Design task)
- Department: 20 (Design dept)
- Skill: 20 (Has Figma, design skills)
- Workload: 20 (0 tasks)
**Priority:** Medium
**Estimated Duration:** 60 minutes

[...list all 3 tasks]

---

### Bessarab Valeriia (Lead Generation)
**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Work/Sales/Profile Lead generator Bessarab Valeriia.md`
**Profession:** Lead Generator (PRF-LDG)
**Department:** Sales/LG (LGN)
**Nov25 Folder:** `/Nov25/LG/Bessarab Valeriia/Week_3/26/`

**Tasks Assigned: 5**

#### Task 1: TST-072 - Export_Contacts_CSV_LinkedIn
**Score:** 100 points
- Profession: 40 (Perfect - LG task)
- Department: 20 (LG dept)
- Skill: 20 (Has LinkedIn)
- Workload: 20 (0 tasks)
**Priority:** High
**Estimated Duration:** 15 minutes

#### Task 2: TST-090 - Generate_Leads_Via_Hunter_IO
**Score:** 95 points
- Profession: 40 (Perfect - LG task)
- Department: 20 (LG dept)
- Skill: 15 (Lead gen skill, new tool)
- Workload: 20 (1 task)
**Priority:** High
**Estimated Duration:** 30 minutes

[...list all 5 tasks]

---

## Workload Balance Analysis

### Department Distribution

| Department | Employees | Tasks | Avg/Employee | Max | Variance |
|------------|-----------|-------|--------------|-----|----------|
| AI (AID) | 10 | 18 | 1.8 | 4 | 15% ✅ |
| Design (DGN) | 15 | 22 | 1.5 | 3 | 12% ✅ |
| LG (LGN) | 20 | 25 | 1.25 | 5 | 18% ✅ |
| Video (VID) | 8 | 12 | 1.5 | 3 | 14% ✅ |
| Sales (SLS) | 3 | 6 | 2.0 | 3 | 10% ✅ |
| Dev (DEV) | 2 | 3 | 1.5 | 2 | 8% ✅ |
| HR (HRM) | 1 | 1 | 1.0 | 1 | 0% ✅ |
| **TOTAL** | **59** | **87** | **1.47** | **5** | **16%** ✅ |

### Top 10 Employees by Workload

| Employee | Department | Profession | Tasks | Status |
|----------|------------|------------|-------|--------|
| Bessarab Valeriia | LG | Lead Generator | 5 | ✅ Normal |
| Artemchuk Nikolay | AI | Project Manager | 4 | ✅ Normal |
| Bogun Polina | Design | UI/UX Designer | 3 | ✅ Normal |
| Shelep Olha | Design | Graphic Designer | 3 | ✅ Normal |
| Podolskyi Sviatoslav | Video | Video Editor | 3 | ✅ Normal |
[...continue]

---

## Quality Checks

- [x] All 87 tasks assigned
- [x] No employee has >10 tasks
- [x] Department variance <20%
- [x] All assignments match profession/skills
- [x] Workload balanced across departments
- [x] High-priority tasks assigned to experienced employees
- [x] Related tasks grouped to same employee (when possible)

---

## Exceptions & Manual Overrides

### Exception 1: HR Department (1 employee)
**Issue:** Only 1 HR employee available
**Resolution:** Assigned all HR tasks (1 task) to HR employee
**Impact:** No variance calculation possible

### Exception 2: Development Specialty Tasks
**Issue:** MCP connector task requires specific expertise
**Resolution:** Assigned to senior developer despite higher workload
**Impact:** Dev dept variance 8% (acceptable)

---

## Recommendations for MLT-007

1. **Distribute High-Priority First:** Create tasks.md files for high-priority assignments first
2. **Group Related Tasks:** If employee has multiple tasks from same project, group them
3. **Add Context:** Include task descriptions and template links in tasks.md
4. **Set Deadlines:** Recommend completion deadlines based on priority
```

---

## Employee Profile Examples

### Example 1: Project Manager Profile

**File:** `/ENTITIES/TALENTS/Employees/profiles/Work/AI/Profile Project manager, Lead generator Artemchuk Nikolay.md`

**Key Fields for Assignment:**
```
Profession: project manager → PRF-PRJ
Department: AI → AID
Skills: Agile, SCRUM, project management, Data Processing
Tools: Asana, Jira, Monday, Notion, Slack, Trello
```

**Best Fits:**
- Project management tasks (40 pts)
- AI department tasks (20 pts)
- Tasks using Asana/Jira/Notion (20 pts)

### Example 2: Designer Profile

**File:** `/ENTITIES/TALENTS/Employees/profiles/Part_Project___Part_Time/Design/Profile UI UX designer Bogun Polina.md`

**Key Fields:**
```
Profession: ui ux designer → PRF-DGN
Department: Design → DGN
Skills: UX/UI design, prototyping, usability testing, ux writing
Tools: Figma, Photoshop, Illustrator, HTML, CSS
```

**Best Fits:**
- Design tasks (40 pts)
- Design department (20 pts)
- Figma/UI/UX tasks (20 pts)

---

## Automation Opportunity

**Future Script:** `assign_tasks.py`

```python
# Pseudo-code
employees = load_profiles('/ENTITIES/TALENTS/Employees/profiles/Work/')
tasks = load('02_Extracted_Tasks/')
algorithm = load('Task_Assignment_Rules.json')

scores = {}
for task in tasks:
    for employee in employees:
        score = calculate_score(task, employee, algorithm)
        scores[(task.id, employee.name)] = score

assignments = optimize_assignments(scores, constraints={
    'max_tasks_per_employee': 10,
    'max_variance': 0.20,
    'prefer_tasks_per_employee': 5
})

save_plan('assignment_plan.md', assignments)
```

**Time Savings:** 45 min → 10 min (35 min saved)

---

## Checklist

- [ ] Load Task_Assignment_Rules.json algorithm
- [ ] Load all employee profiles from Work/ folders
- [ ] Extract employee data (profession, dept, skills, tools)
- [ ] Load all 87 extracted tasks from MLT-003
- [ ] Calculate profession match scores (40 pts) for all pairs
- [ ] Calculate department match scores (20 pts)
- [ ] Calculate skill match scores (20 pts)
- [ ] Calculate workload balance scores (20 pts)
- [ ] Assign tasks to highest-scoring employees
- [ ] Apply max 10 tasks/employee constraint
- [ ] Balance workload to <20% variance per department
- [ ] Create detailed assignment plan
- [ ] Verify all tasks assigned
- [ ] Save assignment_plan_2025-11-25.md
- [ ] Update processing log

---

## Expected Outcomes

✅ **Assignment Plan Created**
- **All 87 tasks assigned** to appropriate employees
- **Workload balanced:** <20% variance per department
- **Skills matched:** All assignments match profession + skills
- **Plan documented:** Complete assignment_plan.md with scores

✅ **Ready for MLT-007**
- Know which employee gets which task
- Have employee Nov25 folder paths
- Have tomorrow's date folder (DD+1) targets
- Assignment plan ready for execution

---

## Next Milestone

**→ [MLT-007: Task Distribution](MLT-007_Task_Distribution.md)** - Create/update tasks.md files in each employee's tomorrow folder (30 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Assignment Algorithm:** [Task_Assignment_Rules.json](../../Daily_Processing/Daily_Processing_Workflow/Support_Files/Task_Assignment_Rules.json)
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`
- **Profession Codes:** [TAX-001 Libraries ISO Registry](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md#profession-iso-codes)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
