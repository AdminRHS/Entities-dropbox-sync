# AI Prompt: Create Individual Employee Plans from Executive Reports

## Objective
Extract tasks from Week 4 Executive analysis reports (Nov 24-28) and create individual `plans.md` files for each employee in their `Week_4/28` folder.

---

## Task Overview

### Source Data
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\Executives\`

**Files to process:**
1. `241125_Analysis_COMPREHENSIVE.md` (November 24, 2025)
2. `251125_Analysis_COMPREHENSIVE.md` (November 25, 2025)
3. `261125_Analysis_COMPREHENSIVE.md` (November 26, 2025)
4. `271125_Analysis_v7.1_COMPREHENSIVE.md` (November 27, 2025)
5. `281125.md` (November 28, 2025 - Friday Executive Plan)

### Target Location
**Base Path:** `C:\Users\Dell\Dropbox\Nov25\[Department] Nov25\[Employee Name]\Week_4\28\`

**File to create:** `plans.md` (individual file for each employee)

### Employee Directory Structure Examples:
- `Nov25\Fin Nov25\Ponomarova Kateryna\Week_4\28\plans.md`
- `Nov25\AI Nov25\[Employee Name]\Week_4\28\plans.md`
- `Nov25\Design Nov25\[Employee Name]\Week_4\28\plans.md`
- `Nov25\Video Nov25\[Employee Name]\Week_4\28\plans.md`
- `Nov25\Dev Nov25\[Employee Name]\Week_4\28\plans.md`

---

## Step-by-Step Instructions

### STEP 1: Get Employee Directory List
First, identify all employees with "Work" status who should receive task assignments.

**Action:**
1. Read the employee directory from: `C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\Employees_Public_Nov25.md`
2. Filter employees by status: "Work" (active employees only)
3. Create a list of:
   - Employee Name
   - Employee ID
   - Department
   - Profession
   - Folder location pattern

**Output:** Master employee list for task assignment

---

### STEP 2: Read and Parse All Executive Reports
Read all 5 executive analysis files and extract task information.

**For each file, extract:**
- Task IDs (TSK-###, MLT-###, PRT-###, EXEC-###, HRM-###, DGN-###, etc.)
- Task titles and descriptions
- Employee assignments (explicit or inferred from department)
- Department assignments
- Priority levels (HIGH/MEDIUM/LOW)
- Status (New, In Progress, Completed, Blocked)
- Deadlines or timelines
- Task steps/deliverables
- Resources needed
- Dependencies

**Special attention to Nov 28 (281125.md):**
- Executive priorities (EXEC-PRIORITY-1, 2, 3, 4)
- Department-specific tasks (HRM-EXEC-1, DGN-EXEC-1, etc.)
- Strategic initiatives (INITIATIVE-1, 2, 3, 4)
- Friday priorities and Monday assignments

---

### STEP 3: Match Tasks to Employees

**Matching Logic:**

1. **Direct Assignment:** Task explicitly mentions employee name
   - Example: "Assignee: Niko" → Assign to Niko

2. **Department Assignment:** Task assigned to department code
   - Example: "Department: HRM" → Assign to all HR employees OR team lead
   - Example: "Department: DGN" → Assign to Design team

3. **Role-Based Assignment:** Task requires specific profession
   - Example: "Developer needed" → Assign to DEV department employees
   - Example: "Motion designer" → Assign to VID employees with that skill

4. **Team Lead Assignment:** Executive or strategic tasks
   - Niko → Executive/AI tasks
   - Olya → HR/Admin tasks
   - Kolya Artemchuk → Development/Executive tasks
   - Stas → Executive tasks
   - Department leads → Department planning tasks

5. **Unassigned Tasks:** If no clear employee match
   - Store in a separate "Unassigned_Tasks.csv" for manual review

---

### STEP 4: Create Individual Employee plans.md Files

For EACH employee with assigned tasks:

1. **Navigate to employee folder:**
   ```
   C:\Users\Dell\Dropbox\Nov25\[Department] Nov25\[Employee Name]\Week_4\28\
   ```

2. **Create `plans.md` file** using the template below

3. **Populate with assigned tasks** from all 5 executive reports

---

## TEMPLATE: Individual Employee plans.md

```markdown
# Week 4 Plans — November 28, 2025
**Employee:** [Full Name]
**Employee ID:** [ID Number]
**Department:** [Department Name]
**Total Tasks:** [COUNT]

---

## Task Summary

| Priority | Count | Status Breakdown |
|----------|-------|------------------|
| 🔴 HIGH | [#] | Not Started: [#], In Progress: [#], Completed: [#] |
| 🟡 MEDIUM | [#] | Not Started: [#], In Progress: [#], Completed: [#] |
| 🟢 LOW | [#] | Not Started: [#], In Progress: [#], Completed: [#] |

**Total Tasks:** [#] | **Completed:** [#] | **In Progress:** [#] | **Not Started:** [#] | **Blocked:** [#]

---

## 🔴 HIGH PRIORITY TASKS

### TSK-### / MLT-### / PRT-###: [Task Title]
**Status:** [Not Started / In Progress / Completed / Blocked]
**Source:** [241125 / 251125 / 261125 / 271125 / 281125]
**Department:** [Department]
**Deadline:** [Date or "ASAP" or "Friday" etc.]

**Description:**
[Full task description from the executive report]

**Deliverables:**
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

**Task Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Resources Needed:**
- [Resource 1: Tool, file, access, etc.]
- [Resource 2]

**Dependencies:**
- Requires: [Task ID or resource]
- Blocks: [Task ID that depends on this]

**Success Criteria:**
- [How to know when complete]
- [Quality standards]

**Notes:**
[Any additional context or instructions]

---

### [Next High Priority Task...]

---

## 🟡 MEDIUM PRIORITY TASKS

### TSK-###: [Task Title]
[Same structure as above]

---

## 🟢 LOW PRIORITY TASKS

### TSK-###: [Task Title]
[Same structure as above]

---

## 📊 Task Context & Background

### Week 4 Overview (Nov 24-28)
**Strategic Focus:**
- [Key themes from this week's executive reports]
- [Major projects or initiatives]
- [Department priorities]

**Your Role This Week:**
[Explanation of how your tasks fit into larger strategic goals]

**Key Collaborators:**
- [Names of people you'll work with]
- [Department dependencies]

---

## 🔗 Related Resources

### Executive Plans
- [Link to relevant CLUSTER or INITIATIVE from 281125.md]
- [Link to project documentation: PRT-NEW-001, etc.]

### Department Documentation
- [Department-specific guides or templates]
- [Prompt templates: PMT-### from AI_PROMPT_For_Content_Generation.md]

### File Locations
- [Key file paths for your tasks]
- [Dropbox folders you'll need]
- [External links: websites, tools, etc.]

---

## ⚠️ Blockers & Issues

[List any blockers identified in executive reports]
[Note any missing resources or decisions needed]

---

## 📝 Notes for Monday (Dec 2, 2025)

**Carry Forward to Next Week:**
- [Tasks not completed this week]
- [Tasks marked for Monday start]

**Executive Decisions Needed:**
- [Any approvals or clarifications required]

**Questions for Team Lead:**
- [Items needing clarification]

---

**Generated:** November 28, 2025
**Source:** Week 4 Executive Analysis Reports (Nov 24-28)
**Next Update:** Monday, December 2, 2025 (Week 5 planning)
```

---

## STEP 5: Quality Assurance

Before finalizing each employee's `plans.md`:

### Checklist:
- [ ] Employee name, ID, and department are correct
- [ ] All tasks from 5 executive reports are included
- [ ] Tasks are properly prioritized (HIGH/MEDIUM/LOW)
- [ ] Each task has clear deliverables and steps
- [ ] Dependencies are identified
- [ ] Resources and file paths are accurate
- [ ] Task IDs are correct (TSK-###, MLT-###, etc.)
- [ ] Deadlines match executive report timelines
- [ ] Related executive initiatives are cross-referenced
- [ ] File is saved in correct location: `Week_4/28/plans.md`

---

## STEP 6: Create Process Logs

Document the entire assignment process for transparency and future reference.

**Log Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\LOG\Week_4\`

**Create the following log files:**

### 281125_Assignment_Process_Log.md
Complete narrative of the assignment process:
- Start time and end time
- Which reports were processed (all 5 files)
- How many tasks were extracted from each report
- How many employees received assignments
- Any decisions made during assignment process
- Issues encountered and how they were resolved
- Summary statistics

### 281125_Extraction_Log.txt
Raw extraction notes:
- List each task extracted with its source file
- Note any tasks that were unclear or ambiguous
- Record which tasks had explicit employee assignments vs. inferred

### 281125_Assignment_Decisions.csv
Record of all assignment decisions:
```csv
Task_ID,Task_Title,Decision_Type,Assigned_To,Reasoning,Alternative_Considered
TSK-026,Daily Report Cycle,Explicit,Niko,Named in 281125.md,None
HRM-EXEC-1,Send Onboarding Letters,Department,Olya,HR Executive tasks,Could assign to HR team
```

### 281125_Errors_And_Issues.txt
Document any problems:
- Tasks that couldn't be assigned
- Missing employee folders
- Ambiguous task descriptions
- Missing deadlines or priorities

---

## STEP 7: Create Master CSV Tracking File

After creating all individual `plans.md` files and logs, generate a master CSV for executive oversight.

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker.csv`

**CSV Columns:**
```
Employee_ID,Employee_Name,Department,Task_ID,Task_Title,Priority,Status,Source_Date,Deadline,Deliverables_Count,Dependencies,File_Location
```

**Example Row:**
```
228,Ponomarova Kateryna,Finance,TSK-026,Daily Report Processing Cycle,HIGH,Not Started,281125,Friday,3,TST-002,Nov25\Fin Nov25\Ponomarova Kateryna\Week_4\28\plans.md
```

**Purpose:**
- Executive dashboard of all assignments
- Quick filtering by employee, department, priority, status
- Track completion rates
- Identify workload distribution
- Easy sorting and analysis in Excel/Google Sheets

---

## Special Handling Instructions

### Department-Specific Considerations

#### Executive Team (Niko, Stas, Kolya, Olya)
- Include all EXEC-PRIORITY tasks
- Include strategic initiatives (INITIATIVE-1 through 4)
- Include cluster-level oversight tasks
- Include Friday executive meeting outcomes

#### HR (Olya + HR Team)
- Include HRM-EXEC-1, 2, 3 tasks
- Include 11 candidate onboarding tasks
- Include interview transcription processing
- Include website planning tasks

#### Design (DGN)
- Include terminology content tasks (TST-014, TST-016, TST-019)
- Include department documentation task (DGN-EXEC-2)
- Include planning tasks for Monday execution

#### Video (VID)
- Include 10-video series tasks (TST-015, VID-EXEC-1)
- Include Artlist.io research tasks
- Include production planning tasks

#### Development (DEV)
- Include Research App tasks (DEV-EXEC-1, TST-029)
- Include Prompts App tasks (DEV-EXEC-3)
- Include sitemap export tasks (TST-020)
- Include developer identification tasks (DEV-EXEC-2)

#### Lead Generation (LGN)
- Include website update tasks (LGN-EXEC-1)
- Include RH-S.com and REM-S.com planning
- Include sales trainee organization (LGN-EXEC-2)

#### Marketing (MKT)
- Include LinkedIn automation research (MKT-EXEC-1, TST-006)
- Include website content rewrite (TST-021)

#### Social Media Marketing (SMM)
- Include OAY content development (SMM-EXEC-1)
- Include Artlist.io video tutorials research (SMM-EXEC-2)

---

### Task Categorization by Date

**November 24 Tasks:**
- Extract from 241125_Analysis_COMPREHENSIVE.md
- Mark source date as "241125"

**November 25 Tasks:**
- Extract from 251125_Analysis_COMPREHENSIVE.md
- Mark source date as "251125"

**November 26 Tasks:**
- Extract from 261125_Analysis_COMPREHENSIVE.md
- Mark source date as "261125"

**November 27 Tasks:**
- Extract from 271125_Analysis_v7.1_COMPREHENSIVE.md
- Mark source date as "271125"

**November 28 Tasks (Friday Executive):**
- Extract from 281125.md
- Mark source date as "281125"
- **Special handling:** Many tasks marked "Friday implementation" or "Monday start"

---

### Friday vs Monday Task Distinction

**Friday Tasks (Complete Today - Nov 28):**
- Marked ⚡ CRITICAL or 🔴 HIGH PRIORITY with "Friday" deadline
- Executive priorities (EXEC-PRIORITY-1, 2, 3, 4)
- Daily report processing cycle (TST-026)
- 11 onboarding letters (HRM-EXEC-1)
- Executive department structure definition
- Week 4 summary creation

**Monday Tasks (Carry to Week 5 - Dec 2):**
- Planning tasks marked "Friday planning, Monday execution"
- Content creation tasks (design posts, videos)
- Website update implementation
- Development tasks (Research App, Prompts App)
- New employee onboarding (after letters sent)

**Mark clearly in each employee's plans.md which tasks are for Friday vs Monday**

---

## Employee Directory Reference

### Expected Department Folders:
- `Nov25\AI Nov25\` - Artificial Intelligence department
- `Nov25\Design Nov25\` - Design department
- `Nov25\Dev Nov25\` - Development department
- `Nov25\Fin Nov25\` - Finance/Administration department
- `Nov25\Video Nov25\` - Video production department
- `Nov25\LG Nov25\` - Lead Generation department (if exists)
- `Nov25\Marketing Nov25\` - Marketing department (if exists)
- `Nov25\HR Nov25\` - Human Resources (if exists)

### Employee Folder Structure:
```
[Department] Nov25\
  └── [Employee Name]\
      └── Week_4\
          └── 28\
              ├── plans.md       ← CREATE THIS FILE
              ├── daily.md       (may already exist)
              ├── task.md        (may already exist)
              └── reports.md     (may already exist)
```

---

## Priority Assignment Logic

### HIGH Priority Indicators:
- Marked ⚡ CRITICAL in source document
- Marked "URGENT" or "MUST complete Friday"
- Has "Friday" deadline
- Blocks other tasks
- Executive decision needed
- Affects company-wide operations
- Keywords: "critical", "urgent", "ASAP", "immediately", "blocking"

### MEDIUM Priority Indicators:
- Marked for "Week 5" start
- "Monday execution" tasks
- "Planning" tasks
- Important but not urgent
- Part of strategic initiatives
- Keywords: "should", "planned", "important", "this week", "next week"

### LOW Priority Indicators:
- Marked "Future" or "Week 5 strategic"
- Research tasks without immediate deadline
- "Nice to have" improvements
- Long-term planning
- Keywords: "could", "optional", "future", "when possible", "consider"

---

## Success Metrics

After completing this process, you should have:

1. ✅ **Individual plans.md files** created for all active "Work" status employees
2. ✅ **Master CSV tracker** with all assignments in one view
3. ✅ **100-200 tasks** distributed across employees
4. ✅ **Clear priorities** (HIGH/MEDIUM/LOW) for each task
5. ✅ **Source traceability** (which executive report each task came from)
6. ✅ **No orphan tasks** (all tasks assigned or marked as "Unassigned")
7. ✅ **Proper file structure** (all plans.md in correct Week_4/28 folders)

---

## Output Summary

### Files Created:
```
Nov25\[Department] Nov25\[Employee 1]\Week_4\28\plans.md
Nov25\[Department] Nov25\[Employee 2]\Week_4\28\plans.md
Nov25\[Department] Nov25\[Employee 3]\Week_4\28\plans.md
...
[20-50 individual plans.md files]

ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker.csv
ENTITIES\DAILIES\PLANS\Week_4\Unassigned_Tasks.csv (if applicable)
```

### Statistics to Report:
- Total employees with assignments: [#]
- Total tasks distributed: [#]
- Average tasks per employee: [#]
- High priority tasks: [#]
- Friday deadline tasks: [#]
- Monday start tasks: [#]
- Unassigned tasks needing review: [#]

---

## Error Handling

### If Employee Folder Doesn't Exist:
- Option 1: Create folder structure automatically
- Option 2: Add to "Missing_Employee_Folders.csv" for manual creation
- Option 3: Skip and note in summary report

### If Employee Not in Directory:
- Check for name variations (spelling, order)
- Check for nickname vs full name
- Add to "Unknown_Employees.csv" for executive review

### If Task Has No Clear Owner:
- Add to "Unassigned_Tasks.csv"
- Note which department it might belong to
- Flag for executive review and manual assignment

---

## Next Steps (After File Creation)

1. **Executive Review:**
   - Niko reviews Master_Employee_Assignment_Tracker.csv
   - Assign unassigned tasks
   - Verify workload distribution is balanced

2. **Communication:**
   - Notify employees via Discord that plans.md files are ready
   - Provide instructions on how to access Week_4/28 folder
   - Set expectations for Friday vs Monday tasks

3. **Tracking:**
   - Employees update status in their plans.md as work progresses
   - Daily report processing cycle (TST-026) reads plans.md to generate next day tasks
   - Weekly review of completion rates

---

**Version:** 1.0
**Created:** November 28, 2025
**Purpose:** Create individual employee plans.md files from Week 4 Executive reports
**Target:** All active employees with "Work" status
**Output Location:** `Nov25\[Department] Nov25\[Employee Name]\Week_4\28\plans.md`
