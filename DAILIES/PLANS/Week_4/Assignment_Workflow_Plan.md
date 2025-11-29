# Step-by-Step Employee Task Assignment Workflow

**Created:** November 28, 2025
**Purpose:** Guide for assigning tasks from Executive reports to individual employees
**Output:** Individual `plans.md` files + Master CSV tracker

---

## Overview: Why CSV Format?

**Your Preference:** CSV format for data visibility
**Benefits:**
- ✅ Easy to view and edit in Excel/Google Sheets/Numbers
- ✅ Quick filtering and sorting by any column
- ✅ Simple data analysis (counts, averages, pivot tables)
- ✅ Easy to share and collaborate
- ✅ Can import into any database or project management tool later
- ✅ Lightweight and portable

**Recommendation:** Use **CSV as the master tracking system** and generate individual markdown files from it.

---

## Workflow Architecture

```
┌─────────────────────────────────────────┐
│  STEP 1: Data Collection                │
│  ├─ Read 5 Executive Reports            │
│  └─ Read Employee Directory             │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  STEP 2: Create Master CSV              │
│  ├─ Extract all tasks                   │
│  ├─ Assign to employees                 │
│  └─ Populate CSV tracker                │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  STEP 3: Generate Individual plans.md   │
│  ├─ Filter CSV by employee              │
│  ├─ Format as markdown                  │
│  └─ Save to Week_4/28/plans.md          │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│  STEP 4: Review & Distribution          │
│  ├─ Executive reviews CSV               │
│  ├─ Assign unassigned tasks             │
│  └─ Notify employees                    │
└─────────────────────────────────────────┘
```

---

## STEP 1: Data Collection

### 1.1 Prepare Your Workspace

**Create working folder:**
```
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\PLANS\Week_4\Assignment_Working_Files\
```

**Files you'll create here:**
- `All_Tasks_Extracted.csv` - Raw task extraction
- `Employee_Directory_Active.csv` - Filtered employee list
- `Task_Assignment_Matrix.csv` - Task → Employee mapping

**Logs location:**
```
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\LOG\Week_4\
```

**Log files to create:**
- `281125_Assignment_Process_Log.md` - Detailed processing log with decisions made
- `281125_Extraction_Log.txt` - Raw extraction notes from each report
- `281125_Assignment_Decisions.csv` - Record of assignment decisions and reasoning
- `281125_Errors_And_Issues.txt` - Any problems encountered during processing

---

### 1.2 Read Executive Reports

**Source:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\Executives\`

**Files (in order):**
1. `241125_Analysis_COMPREHENSIVE.md` - Monday
2. `251125_Analysis_COMPREHENSIVE.md` - Tuesday
3. `261125_Analysis_COMPREHENSIVE.md` - Wednesday
4. `271125_Analysis_v7.1_COMPREHENSIVE.md` - Thursday
5. `281125.md` - Friday (Today - Executive Plan)

**For each file, create extraction notes:**

#### All_Tasks_Extracted.csv Structure:
```csv
Source_File,Date,Task_ID,Task_Title,Description,Department,Suggested_Employee,Priority,Status,Deadline,Type
241125,Nov 24,TSK-001,Example Task,Full description here,AID,Niko,HIGH,New,Friday,Task
241125,Nov 24,MLT-003,Entity Extraction,Milestone description,AID,Multiple,MEDIUM,In Progress,Week 5,Milestone
...
```

**Extraction Method:**
- Use AI assistant (Claude/GPT) with [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md)
- Manual extraction (open each file, copy task sections into CSV)
- Semi-automated: AI extracts, you verify and clean up

---

### 1.3 Get Active Employee List

**Source:** `C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\Employees_Public_Nov25.md`

**Filter criteria:**
- Status = "Work" (active employees only)
- Exclude: "Fired", "Left", "Pending"

#### Employee_Directory_Active.csv Structure:
```csv
Employee_ID,Employee_Name,Department,Department_Code,Profession,Position,Shift,Start_Date,Rate,Folder_Path
228,Ponomarova Kateryna,Finance,FIN,Financial Manager,Employee,Day,01/15/2023,25.00,Nov25\Fin Nov25\Ponomarova Kateryna
39412,Artemchuk Nikolay,Development,DEV,Full Stack Developer,Team Lead,Day,03/01/2022,35.00,Nov25\Dev Nov25\Artemchuk Nikolay
...
```

**Expected count:** 20-60 active employees

---

## STEP 2: Create Master CSV Assignment Tracker

### 2.1 Build the Master CSV

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker.csv`

**Column Definitions:**

| Column Name | Description | Example Value |
|-------------|-------------|---------------|
| **Employee_ID** | Unique employee identifier | 228 |
| **Employee_Name** | Full name | Ponomarova Kateryna |
| **Department** | Full department name | Finance |
| **Department_Code** | 3-letter code | FIN |
| **Task_ID** | Task identifier | TSK-026 |
| **Task_Title** | Brief task name | Daily Report Processing Cycle |
| **Priority** | HIGH/MEDIUM/LOW | HIGH |
| **Status** | Not Started/In Progress/Completed/Blocked | Not Started |
| **Source_Date** | Which report date | 281125 |
| **Deadline** | When due | Friday EOD |
| **Deliverables_Count** | Number of outputs | 3 |
| **Has_Dependencies** | Yes/No | Yes |
| **Blocking_Other_Tasks** | Yes/No | Yes |
| **Assigned_By** | Who assigned | Niko (Executive) |
| **File_Location** | Path to plans.md | Nov25\Fin Nov25\Ponomarova Kateryna\Week_4\28\plans.md |
| **Notes** | Additional context | Critical for Monday task generation |

---

### 2.2 Task Assignment Decision Matrix

**How to decide who gets each task:**

#### Decision Tree:
```
Is employee explicitly named in task?
  ├─ YES → Assign to that employee
  └─ NO → Is department specified?
      ├─ YES → Is it a team-wide task?
      │   ├─ YES → Assign to ALL department members
      │   └─ NO → Assign to department Team Lead
      └─ NO → Is it an executive task?
          ├─ YES → Assign to executive team (Niko/Stas/Kolya/Olya)
          └─ NO → Mark as UNASSIGNED for manual review
```

#### Assignment Rules by Task Type:

**Executive Tasks (EXEC-PRIORITY-###, EXECUTIVE-###):**
- Niko: Strategic planning, AI, automation, prompts, taxonomy
- Stas: Executive oversight, strategic review
- Kolya Artemchuk: Development oversight, Research App
- Olya: HR, admin, employee management

**Department Tasks (DEPT-EXEC-###):**
- HRM-EXEC-### → Olya + HR team
- DGN-EXEC-### → Design team lead
- DEV-EXEC-### → Kolya + Dev team
- VID-EXEC-### → Video team lead
- LGN-EXEC-### → LG team leads (Anna Burda, Ksenia, Diana)
- MKT-EXEC-### → Marketing team lead
- SMM-EXEC-### → SMM team lead

**Project Tasks (PRT-NEW-###):**
- Check project description for assigned departments
- Distribute across relevant team members
- Large projects: assign to team leads for delegation

**Standard Tasks (TSK-###):**
- Check department code in task
- Match to employee profession/skills
- Consider workload balance (don't overload one person)

**Milestones (MLT-###):**
- Usually assigned to multiple employees
- Create one row per employee involved
- Mark as "Shared Milestone" in notes

---

### 2.3 Populate the Master CSV

**Methods (choose one):**

#### Option A: AI-Assisted (Fastest - Recommended)
1. Use the AI prompt from [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md)
2. Provide AI with:
   - All 5 executive report files
   - Employee directory CSV
   - Assignment decision matrix
3. AI generates complete Master CSV
4. You review and adjust assignments

**Time estimate:** 10-20 minutes

---

#### Option B: Semi-Manual (More Control)
1. Open `All_Tasks_Extracted.csv` (from Step 1.2)
2. Open `Employee_Directory_Active.csv` (from Step 1.3)
3. For each task row:
   - Look at "Suggested_Employee" or "Department"
   - Find matching employee(s) in directory
   - Add new row(s) to Master CSV
4. Use Excel formulas to auto-fill file paths

**Time estimate:** 2-4 hours

---

#### Option C: Fully Manual (Most Time-Consuming)
1. Read each executive report
2. Write down each task and who should do it
3. Type into CSV row by row
4. Double-check against employee directory

**Time estimate:** 3-5 hours

**Recommendation:** Use Option A (AI-Assisted) then spend 30 minutes reviewing

---

### 2.4 Handle Unassigned Tasks

**Create separate file:** `Unassigned_Tasks.csv`

**Same structure as Master CSV, but Employee_ID/Name are blank**

**Reasons for unassigned:**
- No clear department match
- Requires skills not in current team
- New hire needed
- Executive decision required
- Task description too vague

**Example:**
```csv
Employee_ID,Employee_Name,Department,Department_Code,Task_ID,Task_Title,Priority,Status,Source_Date,Deadline,Reason_Unassigned
,,,UNKNOWN,TSK-999,Unclear task description,MEDIUM,New,261125,Next week,No department specified and no employee mentioned
```

**Review process:**
1. Niko reviews `Unassigned_Tasks.csv`
2. Makes assignment decisions
3. Moves rows to Master CSV with employee assignment

---

## STEP 3: Generate Individual Employee plans.md Files

### 3.1 Automated Generation (Recommended)

**Script approach:**

```python
# Pseudo-code for automation
import pandas as pd
from pathlib import Path

# Load Master CSV
df = pd.read_csv('Master_Employee_Assignment_Tracker.csv')

# Group by employee
for employee_id, employee_tasks in df.groupby('Employee_ID'):
    employee_name = employee_tasks.iloc[0]['Employee_Name']
    department = employee_tasks.iloc[0]['Department']
    file_path = employee_tasks.iloc[0]['File_Location']

    # Generate markdown content
    markdown = generate_plans_md(employee_tasks)

    # Ensure directory exists
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    # Write plans.md
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
```

**Or use AI assistant:**
1. Provide Master CSV
2. Ask AI to generate each employee's plans.md
3. AI creates files in correct locations

---

### 3.2 Manual Generation (Per Employee)

**For each unique employee in Master CSV:**

1. **Filter the CSV** to show only that employee's rows
2. **Copy the template** from [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md)
3. **Fill in:**
   - Employee name, ID, department
   - Task summary statistics
   - HIGH priority tasks (filtered from CSV)
   - MEDIUM priority tasks
   - LOW priority tasks
4. **Save to:** `Nov25\[Department] Nov25\[Employee Name]\Week_4\28\plans.md`

**Time per employee:** 5-10 minutes
**Total time (40 employees):** 3-7 hours

**Recommendation:** Use automated approach to save time

---

### 3.3 Quality Check Each plans.md

**Checklist:**
- [ ] Employee name and ID match directory
- [ ] All tasks from Master CSV are included
- [ ] Tasks are sorted by priority (HIGH → MEDIUM → LOW)
- [ ] Each task has description, deliverables, steps
- [ ] File paths and resources are accurate
- [ ] Deadline information is clear
- [ ] File saved in correct Week_4/28 folder

---

## STEP 4: Review & Distribution

### 4.1 Executive Review of Master CSV

**Niko's review tasks:**

1. **Open Master CSV in Excel/Google Sheets**
2. **Check workload distribution:**
   - Sort by Employee_Name
   - Count tasks per employee
   - Look for imbalances (one person has 20 tasks, another has 2)
3. **Review priorities:**
   - Filter by Priority = HIGH
   - Verify Friday deadlines are realistic
   - Ensure critical tasks are assigned
4. **Check unassigned tasks:**
   - Review `Unassigned_Tasks.csv`
   - Make assignment decisions
   - Move to Master CSV
5. **Verify executive team assignments:**
   - Filter by Employee_Name IN (Niko, Stas, Kolya Artemchuk, Olya)
   - Confirm executive priorities are covered

---

### 4.2 Workload Balance Analysis

**Create pivot table in Excel:**

| Employee Name | HIGH | MEDIUM | LOW | Total | Avg Priority Score |
|---------------|------|--------|-----|-------|--------------------|
| Ponomarova Kateryna | 3 | 5 | 2 | 10 | 2.1 |
| Artemchuk Nikolay | 5 | 3 | 1 | 9 | 2.4 |
| ... | ... | ... | ... | ... | ... |

**Priority Score Formula:**
- HIGH = 3 points
- MEDIUM = 2 points
- LOW = 1 point
- Avg = (HIGH×3 + MEDIUM×2 + LOW×1) / Total

**Ideal distribution:**
- 15-25% of tasks are HIGH priority
- 50-60% are MEDIUM priority
- 20-30% are LOW priority
- No single employee has >80% HIGH priority tasks

**Rebalancing:**
- If someone is overloaded, move LOW priority tasks to colleagues
- If someone has too few tasks, assign from unassigned list
- Ensure skill match when redistributing

---

### 4.3 Department Summary Report

**Create:** `Department_Task_Summary.csv`

```csv
Department_Code,Department_Name,Total_Tasks,HIGH,MEDIUM,LOW,Employee_Count,Avg_Tasks_Per_Employee,Team_Lead
AID,Artificial Intelligence,25,8,12,5,3,8.3,Niko
HRM,Human Resources,15,5,7,3,4,3.8,Olya
DGN,Design,18,6,9,3,5,3.6,TBD
DEV,Development,22,9,10,3,4,5.5,Kolya Artemchuk
VID,Video,12,4,6,2,3,4.0,TBD
LGN,Lead Generation,10,2,6,2,3,3.3,"Anna Burda, Ksenia, Diana"
MKT,Marketing,8,2,4,2,2,4.0,TBD
SMM,Social Media Marketing,6,2,3,1,2,3.0,TBD
FIN,Finance,10,3,5,2,2,5.0,TBD
TOTAL,All Departments,126,41,62,23,28,4.5,-
```

**Analysis questions:**
- Which department has the most HIGH priority tasks?
- Are any departments understaffed for their workload?
- Do team lead assignments make sense?

---

### 4.4 Notify Employees

**Communication channels:**
1. **Discord announcement** (company-wide channel)
2. **Individual DMs** to employees with tasks
3. **Department channels** for team-specific tasks

**Discord Announcement Template:**
```
📋 **Week 4 Task Assignments Ready — November 28, 2025**

Your individual task plans for Week 4 (Nov 24-28) are now available!

**Where to find your tasks:**
📂 `Nov25\[Your Department] Nov25\[Your Name]\Week_4\28\plans.md`

**What's included:**
✅ All tasks assigned from Executive reports (Nov 24-28)
✅ Priority levels (HIGH/MEDIUM/LOW)
✅ Deadlines and deliverables
✅ Resources and dependencies
✅ Friday vs Monday task breakdown

**Important:**
🔴 **HIGH priority tasks** marked for **Friday (today)** - please review ASAP
🟡 **MEDIUM/LOW tasks** - can carry to Monday (Week 5)

**Questions?** Contact your department lead or @Niko

**Master tracker:** Executives can view all assignments at:
`ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker.csv`
```

---

### 4.5 Monitor Progress

**Daily check-ins:**
1. Employees update `Status` in their plans.md as they work
2. Department leads review team progress
3. Executive team checks Master CSV for completion rates

**Update Master CSV:**
- When employee completes a task, change Status to "Completed"
- If blocked, change to "Blocked" and add note
- If in progress, update to "In Progress"

**Friday EOD review:**
- Count completed HIGH priority tasks
- Identify blockers for Monday
- Celebrate wins

---

## STEP 5: Continuous Improvement

### 5.1 Lessons Learned (After Week 4)

**Create:** `Assignment_Process_Retrospective.md`

**Questions to answer:**
- What worked well in this assignment process?
- What was time-consuming or painful?
- How accurate were the initial assignments?
- How many tasks needed reassignment?
- What would make this easier next week?

---

### 5.2 Automation Opportunities

**Future improvements:**
1. **Daily Report Processing Cycle (TST-026):**
   - Automates reading yesterday's work
   - Generates tomorrow's tasks
   - Updates Master CSV automatically

2. **AI Task Extraction:**
   - Train AI to extract tasks from executive reports
   - Auto-assign based on learned patterns
   - Human review only for edge cases

3. **Dashboard:**
   - Real-time view of Master CSV
   - Visual charts (completion %, workload by dept)
   - Alerts for overdue HIGH priority tasks

---

### 5.3 Template Refinement

**After using this workflow:**
- Update [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md) with learnings
- Improve CSV column structure if needed
- Refine assignment decision matrix
- Add common edge cases to documentation

---

## FAQ: Common Questions

### Q: What if an employee doesn't have a Week_4/28 folder?
**A:** Create it automatically OR add to `Missing_Folders.csv` for manual creation.

### Q: Should team-wide tasks be duplicated for each team member?
**A:** It depends:
- If task requires collaboration: Assign to team lead, note "Delegate to team" in notes
- If each member does their own part: Create separate row per employee with specific sub-tasks

### Q: How to handle tasks assigned to "Executive Team" (multiple people)?
**A:** Create one row per executive (Niko, Stas, Kolya, Olya) with the same task ID, mark as "Shared Task" in notes.

### Q: What if priority is not clear from executive report?
**A:** Use inference:
- Has "Friday" deadline → HIGH
- Has "Monday" or "Week 5" → MEDIUM
- No deadline or "Future" → LOW
- When unsure → Mark as MEDIUM (can adjust later)

### Q: Should I include completed tasks from earlier in the week?
**A:** Yes, include with Status = "Completed" so employees can see their accomplishments and executives can track what was done.

### Q: How detailed should task descriptions be in CSV?
**A:** Brief summary in CSV (1-2 sentences), full details in plans.md file. CSV is for tracking/overview, markdown is for execution.

### Q: Can I use Google Sheets instead of CSV files?
**A:** Yes! Google Sheets is excellent for collaboration:
- Easier to share and edit together
- Real-time updates
- Can still export to CSV anytime
- Built-in charts and pivot tables

### Q: What if employee is on vacation or unavailable?
**A:** Mark status as "Blocked - Employee Unavailable" and reassign HIGH priority tasks to backup person.

---

## Tools & Resources

### Recommended Tools:

**For CSV editing:**
- Excel (Windows/Mac)
- Google Sheets (collaborative, online)
- LibreOffice Calc (free, open source)
- CSV Editor extensions for VS Code

**For automation:**
- Python + pandas library
- PowerShell scripts
- Claude/GPT for AI-assisted generation
- MCP (Model Context Protocol) tools

**For file management:**
- Total Commander (Windows)
- Finder (Mac)
- Python pathlib for batch operations

---

## File Locations Reference

**Planning documents:**
- This workflow plan: `ENTITIES\DAILIES\PLANS\Week_4\Assignment_Workflow_Plan.md`
- AI prompt: `ENTITIES\DAILIES\PLANS\Week_4\PROMPT_Create_Individual_Employee_Plans.md`
- CSV template: `ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker_TEMPLATE.csv`

**Source data:**
- Executive reports: `ENTITIES\DAILIES\REPORTS\Week_4\Executives\`
- Employee directory: `Nov25\Fin Nov25\Public\Employees_Public_Nov25.md`

**Output:**
- Master tracker: `ENTITIES\DAILIES\PLANS\Week_4\Master_Employee_Assignment_Tracker.csv`
- Individual plans: `Nov25\[Dept] Nov25\[Name]\Week_4\28\plans.md`
- Unassigned tasks: `ENTITIES\DAILIES\PLANS\Week_4\Unassigned_Tasks.csv`
- Working files: `ENTITIES\DAILIES\PLANS\Week_4\Assignment_Working_Files\`

**Logs:**
- Process logs: `ENTITIES\DAILIES\LOG\Week_4\`
- Assignment process log: `ENTITIES\DAILIES\LOG\Week_4\281125_Assignment_Process_Log.md`
- Extraction log: `ENTITIES\DAILIES\LOG\Week_4\281125_Extraction_Log.txt`
- Assignment decisions: `ENTITIES\DAILIES\LOG\Week_4\281125_Assignment_Decisions.csv`
- Errors and issues: `ENTITIES\DAILIES\LOG\Week_4\281125_Errors_And_Issues.txt`

---

## Timeline Estimate

**Full workflow completion:**

| Step | Time (AI-Assisted) | Time (Manual) |
|------|-------------------|---------------|
| Step 1: Data Collection | 15 min | 1 hour |
| Step 2: Create Master CSV | 20 min | 3 hours |
| Step 3: Generate plans.md | 10 min | 4 hours |
| Step 4: Review & Distribution | 30 min | 1 hour |
| **TOTAL** | **~75 min** | **~9 hours** |

**Recommendation:** Use AI-assisted approach and invest the saved time into quality review and workload balancing.

---

## Success Criteria

✅ **You'll know you're done when:**
1. Master CSV has 100-200 task rows
2. Every active employee has a plans.md file
3. All HIGH priority Friday tasks are assigned
4. Unassigned tasks list is reviewed and assignments made
5. Employees have been notified
6. Department leads know their team's priorities
7. Executive team can view complete picture in Master CSV

---

**Next:** After completing this workflow, move to implementing **TST-026: Daily Report Processing Cycle** to automate this process for future weeks.

---

**Version:** 1.0
**Created:** November 28, 2025
**Owner:** Niko (Executive/AID)
**Status:** Ready for execution
