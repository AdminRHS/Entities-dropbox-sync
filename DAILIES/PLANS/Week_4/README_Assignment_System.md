# Employee Task Assignment System - Quick Start Guide

**Created:** November 28, 2025
**Purpose:** Extract tasks from Week 4 Executive reports and assign to employees
**Status:** Ready to execute

---

## 📁 What's Been Created

### 1. AI Prompt for Task Extraction
**File:** [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md)

**What it does:**
- Reads all 5 Executive reports (Nov 24-28)
- Extracts 100-200 tasks
- Assigns tasks to employees
- Creates individual `plans.md` files for each employee in `Week_4/28/` folder
- Generates Master CSV tracker
- Creates process logs

**How to use:**
Copy the entire prompt and give it to an AI assistant (Claude/GPT) with access to your files.

---

### 2. Master CSV Tracker Template
**File:** [Master_Employee_Assignment_Tracker_TEMPLATE.csv](./Master_Employee_Assignment_Tracker_TEMPLATE.csv)

**What it contains:**
Columns for tracking all task assignments:
- Employee_ID, Employee_Name, Department, Department_Code
- Task_ID, Task_Title, Priority, Status
- Source_Date, Deadline, Deliverables_Count
- Has_Dependencies, Blocking_Other_Tasks
- Assigned_By, File_Location, Notes

**Why CSV:**
✅ Easy to view in Excel/Google Sheets
✅ Filter by employee, department, priority, deadline
✅ Sort and analyze workload distribution
✅ Quick updates and bulk editing

---

### 3. Complete Workflow Guide
**File:** [Assignment_Workflow_Plan.md](./Assignment_Workflow_Plan.md)

**What it includes:**
- 4-step workflow (Data Collection → Master CSV → Individual plans.md → Distribution)
- Decision trees for task assignment
- CSV-first strategy (your preference!)
- Time estimates: 75 min (AI) vs 9 hours (manual)
- FAQ with common scenarios
- Quality assurance checklists

---

## 🎯 Quick Start: How to Execute

### Option A: AI-Assisted (Recommended - 75 minutes)

**STEP 1:** Open [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md)

**STEP 2:** Copy the entire prompt

**STEP 3:** Give to AI assistant (Claude/GPT) with this instruction:
```
Read all 5 Executive reports from:
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\Executives\

Read employee directory from:
C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\Employees_Public_Nov25.md

Execute the prompt to:
1. Extract all tasks
2. Create Master CSV tracker
3. Generate individual plans.md files
4. Create process logs
```

**STEP 4:** Review the generated files:
- Master CSV in Excel/Sheets
- Check workload balance
- Verify assignments make sense
- Adjust any misassignments

**STEP 5:** Notify employees via Discord

---

### Option B: Manual (3-5 hours)

Follow the detailed steps in [Assignment_Workflow_Plan.md](./Assignment_Workflow_Plan.md)

---

## 📂 File Locations

### Source Data
```
ENTITIES\DAILIES\REPORTS\Week_4\Executives\
├── 241125_Analysis_COMPREHENSIVE.md
├── 251125_Analysis_COMPREHENSIVE.md
├── 261125_Analysis_COMPREHENSIVE.md
├── 271125_Analysis_v7.1_COMPREHENSIVE.md
└── 281125.md (Friday Executive Plan)

Nov25\Fin Nov25\Public\
└── Employees_Public_Nov25.md (Employee directory)
```

### Output Files
```
ENTITIES\DAILIES\PLANS\Week_4\
├── Master_Employee_Assignment_Tracker.csv (MAIN TRACKER)
├── Unassigned_Tasks.csv (Tasks needing manual assignment)
└── Assignment_Working_Files\ (Intermediate files)

Nov25\[Department] Nov25\[Employee Name]\Week_4\28\
└── plans.md (Individual employee plans)

ENTITIES\DAILIES\LOG\Week_4\
├── 281125_Assignment_Process_Log.md
├── 281125_Extraction_Log.txt
├── 281125_Assignment_Decisions.csv
└── 281125_Errors_And_Issues.txt
```

---

## 📊 Expected Results

After execution, you'll have:

✅ **100-200 tasks** extracted from 5 Executive reports
✅ **20-50 employees** with task assignments
✅ **Master CSV file** - Easy to view, filter, sort in Excel
✅ **Individual plans.md files** - Each employee sees their own tasks
✅ **Process logs** - Complete audit trail of decisions
✅ **Unassigned tasks list** - For manual review and assignment
✅ **Workload analysis** - See distribution across departments

---

## 🔑 Key Features

### Master CSV Advantages
- **Visibility:** See all 100-200 tasks in one spreadsheet
- **Filtering:** Show only HIGH priority, or only Friday deadlines, or only one department
- **Sorting:** Order by employee, priority, deadline, department
- **Analysis:** Create pivot tables for workload distribution
- **Editing:** Bulk update statuses, reassign tasks, change priorities
- **Sharing:** Send to executives or import into project management tools

### Individual plans.md Files
- **Personalized:** Each employee sees only their tasks
- **Organized:** Sorted by priority (HIGH → MEDIUM → LOW)
- **Detailed:** Full task descriptions, steps, deliverables, resources
- **Contextual:** Links to related projects and executive initiatives
- **Actionable:** Clear deadlines and success criteria

---

## 🚀 Next Steps After Assignment

### For Employees:
1. Open your `Week_4/28/plans.md` file
2. Review all assigned tasks
3. Focus on HIGH priority tasks with Friday deadlines first
4. Update status as you work (Not Started → In Progress → Completed)
5. Ask questions if anything is unclear

### For Department Leads:
1. Review Master CSV filtered by your department
2. Check team workload distribution
3. Help with any blocked tasks
4. Monitor completion rates

### For Executives (Niko, Stas, Kolya, Olya):
1. Open Master CSV in Excel/Sheets
2. Review `Unassigned_Tasks.csv` and make assignments
3. Check Friday HIGH priority tasks are on track
4. Monitor overall progress
5. Adjust priorities as needed

---

## 📋 CSV Column Meanings

| Column | What It Means |
|--------|---------------|
| **Employee_ID** | Unique ID from employee directory (e.g., 228) |
| **Employee_Name** | Full name (e.g., Ponomarova Kateryna) |
| **Department** | Full name (e.g., Finance) |
| **Department_Code** | 3-letter code (FIN, AID, HRM, DGN, DEV, VID, LGN, MKT, SMM) |
| **Task_ID** | Identifier from report (TSK-###, MLT-###, PRT-###, EXEC-###) |
| **Task_Title** | Brief description |
| **Priority** | HIGH (urgent/critical), MEDIUM (important), LOW (nice-to-have) |
| **Status** | Not Started, In Progress, Completed, Blocked |
| **Source_Date** | Which report (241125, 251125, 261125, 271125, 281125) |
| **Deadline** | When due (Friday, Monday, Week 5, etc.) |
| **Deliverables_Count** | Number of outputs expected |
| **Has_Dependencies** | Yes if requires other tasks first |
| **Blocking_Other_Tasks** | Yes if other tasks wait on this |
| **Assigned_By** | Who made the assignment (usually Niko/Executive) |
| **File_Location** | Path to employee's plans.md |
| **Notes** | Additional context or instructions |

---

## 💡 Tips for Using the CSV

### Excel/Google Sheets Quick Actions:

**See all HIGH priority tasks:**
1. Click any cell in the table
2. Data → Filter (or Ctrl+Shift+L)
3. Click Priority dropdown
4. Check only "HIGH"

**See one employee's tasks:**
1. Filter by Employee_Name
2. Select the employee

**See Friday deadlines:**
1. Filter by Deadline
2. Select "Friday" or "Friday EOD"

**Count tasks by department:**
1. Insert → Pivot Table
2. Rows: Department
3. Values: Count of Task_ID

**Check workload balance:**
1. Pivot Table
2. Rows: Employee_Name
3. Values: Count of Task_ID
4. Sort descending to see who has most tasks

---

## ❓ Common Questions

**Q: What if an employee doesn't have a Week_4/28 folder?**
A: The AI or manual process should create it. If it doesn't exist, create it manually or note in the issues log.

**Q: Can I edit the CSV after it's generated?**
A: Yes! That's the point. Edit assignments, update statuses, change priorities as needed.

**Q: What if I use Google Sheets instead of CSV?**
A: Perfect! Upload the CSV to Google Sheets. You'll get real-time collaboration and easier sharing.

**Q: Should every employee get tasks?**
A: Only employees with status="Work" (active). Skip "Fired", "Left", "Pending".

**Q: What about tasks with no clear owner?**
A: They go in `Unassigned_Tasks.csv` for Niko to review and assign manually.

**Q: How do I track progress?**
A: Update the Status column in Master CSV as work progresses. Employees can also update their individual plans.md files.

---

## 🎯 Success Criteria

You'll know it worked when:

✅ Master CSV has 100-200 rows (one per task assignment)
✅ Each active employee has a `plans.md` file
✅ All HIGH priority Friday tasks are assigned
✅ Unassigned tasks list is reviewed
✅ Employees are notified
✅ Process logs document all decisions
✅ You can filter/sort the CSV easily

---

## 📞 Questions or Issues?

**For technical issues with the system:**
- Check the logs in `ENTITIES\DAILIES\LOG\Week_4\`
- Review [Assignment_Workflow_Plan.md](./Assignment_Workflow_Plan.md) for detailed guidance

**For task assignment questions:**
- Review `281125_Assignment_Decisions.csv` to see why assignments were made
- Check the executive reports to see original task context

**For workload concerns:**
- Open Master CSV and check task counts per employee
- Use pivot tables to analyze distribution
- Reassign tasks to balance workload

---

**Ready to start?**

Open [PROMPT_Create_Individual_Employee_Plans.md](./PROMPT_Create_Individual_Employee_Plans.md) and begin! 🚀

---

**Version:** 1.0
**Last Updated:** November 28, 2025
**Owner:** Niko (Executive/AID)
