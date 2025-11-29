# AI Prompt: Extract Executive Analysis Data to Employee Task List

## Objective
Extract all task-related information from Week 4 Executive analysis reports and create a consolidated `employees.to-do` file organized by employee, with proper cross-referencing to milestone documentation.

---

## Instructions for AI Assistant

### Step 1: Read Source Files
Read and analyze all 5 comprehensive analysis reports from:
```
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\Executives\
```

**Files to process:**
1. `241125_Analysis_COMPREHENSIVE.md` (November 24, 2025)
2. `251125_Analysis_COMPREHENSIVE.md` (November 25, 2025)
3. `261125_Analysis_COMPREHENSIVE.md` (November 26, 2025)
4. `271125_Analysis_v7.1_COMPREHENSIVE.md` (November 27, 2025)
5. `281125.md` (November 28, 2025 - Friday Executive Plan)

### Step 2: Extract Task Information
For each file, extract the following data elements:

#### Required Fields:
- **Task ID:** Any identifier like TSK-###, MLT-### (Milestone), PRT-### (Project)
- **Task Title:** Brief descriptive title
- **Description:** Full task description or context
- **Employee Assignment:** Name of assigned employee(s)
- **Department:** Department responsible (AI, Design, Video, Dev, Finance, HR, etc.)
- **Priority:** HIGH, MEDIUM, LOW (infer from context if not explicit)
- **Status:** Not Started, In Progress, Completed, Blocked
- **Date:** Date from the analysis file (24, 25, 26, or 27 November 2025)
- **Task Steps:** Numbered action items or sub-tasks
- **Resources Needed:** Tools, files, access requirements mentioned
- **Dependencies:** Related tasks or milestones referenced
- **Deadline/Timeline:** Any time constraints mentioned

#### Data Extraction Rules:
1. **Employee Name Extraction:**
   - Look for explicit assignments (e.g., "Assigned to:", "Owner:", "@EmployeeName")
   - Check task descriptions for employee mentions
   - Extract from participant lists in meetings
   - If no employee assigned, mark as "Unassigned"

2. **Task Identification:**
   - Extract all formal task IDs (TSK-###, MLT-###, PRT-###)
   - Capture informal tasks mentioned in quotes or bullet points
   - Include action items from executive decisions
   - Include "TODO" items and follow-up actions

3. **Priority Inference:**
   - HIGH: Urgent, critical, blocking other work, deadline today/tomorrow
   - MEDIUM: Important, scheduled for this week, affects team workflow
   - LOW: Nice-to-have, planning, research, future considerations

4. **Status Determination:**
   - "Not Started": Tasks announced but not begun
   - "In Progress": Partially completed, actively worked on
   - "Completed": Finished, verified, or marked done
   - "Blocked": Waiting on dependencies, resources, or decisions

### Step 3: Organize Data Structure
Create a hierarchical organization:

```
├── By Date (November 24, 25, 26, 27)
│   ├── By Employee (Alphabetically)
│   │   ├── By Priority (HIGH → MEDIUM → LOW)
│   │   │   └── Individual Tasks
```

### Step 4: Generate Output File
Create the file at:
```
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\PLANS\Week_4\employees.to-do
```

**File Format:** Markdown with the following structure:

---

## OUTPUT TEMPLATE

```markdown
# Week 4 Employee Task Assignments
**Generated from:** Executive Analysis Reports (Nov 24-27, 2025)
**Source Location:** `ENTITIES/DAILIES/REPORTS/Week_4/Executives/`
**Total Employees:** [COUNT]
**Total Tasks:** [COUNT]
**Last Updated:** [TIMESTAMP]

---

## Table of Contents
- [Summary Statistics](#summary-statistics)
- [November 24 Tasks](#november-24-2025)
- [November 25 Tasks](#november-25-2025)
- [November 26 Tasks](#november-26-2025)
- [November 27 Tasks](#november-27-2025)
- [Unassigned Tasks](#unassigned-tasks)
- [Cross-Reference Index](#cross-reference-index)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Employees with Assignments | [NUMBER] |
| Total Tasks Extracted | [NUMBER] |
| High Priority Tasks | [NUMBER] |
| Medium Priority Tasks | [NUMBER] |
| Low Priority Tasks | [NUMBER] |
| Completed Tasks | [NUMBER] |
| In Progress Tasks | [NUMBER] |
| Not Started Tasks | [NUMBER] |
| Blocked Tasks | [NUMBER] |
| Unassigned Tasks | [NUMBER] |

### Department Breakdown
| Department | Task Count | Employees |
|------------|------------|-----------|
| AI | [NUMBER] | [NUMBER] |
| Design | [NUMBER] | [NUMBER] |
| Video | [NUMBER] | [NUMBER] |
| Development | [NUMBER] | [NUMBER] |
| Finance | [NUMBER] | [NUMBER] |
| HR | [NUMBER] | [NUMBER] |
| Lead Generation | [NUMBER] | [NUMBER] |
| Sales | [NUMBER] | [NUMBER] |
| Other | [NUMBER] | [NUMBER] |

---

## November 24, 2025

### [Employee Name 1] — [Department]
**Total Tasks:** [COUNT] | **High:** [COUNT] | **Medium:** [COUNT] | **Low:** [COUNT]

#### 🔴 HIGH PRIORITY

##### TSK-001: [Task Title]
- **Status:** [Not Started/In Progress/Completed/Blocked]
- **Department:** [Department Name]
- **Source:** `241125_Analysis_COMPREHENSIVE.md`
- **Description:**
  [Full task description or context from the analysis]

- **Task Steps:**
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]

- **Resources Needed:**
  - [Resource 1]
  - [Resource 2]

- **Dependencies:**
  - Related to: [MLT-### or TSK-###]
  - Requires: [Prerequisite task or resource]

- **Timeline:** [Deadline or time estimate]

---

##### MLT-003: [Milestone Title]
- **Status:** [Status]
- **Department:** [Department]
- **Source:** `241125_Analysis_COMPREHENSIVE.md`
- **Milestone Reference:** See [MLT-003_Entity_Extraction.md](./MLT-003_Entity_Extraction.md)
- **Description:**
  [Milestone description]

- **Deliverables:**
  - [Deliverable 1]
  - [Deliverable 2]

- **Success Criteria:**
  - [Criterion 1]
  - [Criterion 2]

---

#### 🟡 MEDIUM PRIORITY

##### TSK-002: [Task Title]
[Same structure as above]

---

#### 🟢 LOW PRIORITY

##### TSK-003: [Task Title]
[Same structure as above]

---

### [Employee Name 2] — [Department]
[Repeat structure for each employee]

---

## November 25, 2025

[Repeat entire date structure]

---

## November 26, 2025

[Repeat entire date structure]

---

## November 27, 2025

[Repeat entire date structure]

---

## Unassigned Tasks

### 🔴 HIGH PRIORITY
[List all high priority tasks without assigned employees]

### 🟡 MEDIUM PRIORITY
[List all medium priority tasks without assigned employees]

### 🟢 LOW PRIORITY
[List all low priority tasks without assigned employees]

---

## Cross-Reference Index

### Tasks by ID
| Task ID | Title | Employee | Department | Priority | Status | Date |
|---------|-------|----------|------------|----------|--------|------|
| TSK-001 | [Title] | [Name] | [Dept] | HIGH | [Status] | Nov 24 |
| TSK-002 | [Title] | [Name] | [Dept] | MEDIUM | [Status] | Nov 24 |
| MLT-003 | [Title] | [Name] | [Dept] | HIGH | [Status] | Nov 25 |
| ... | ... | ... | ... | ... | ... | ... |

### Tasks by Department
| Department | Total | HIGH | MEDIUM | LOW | Completed |
|------------|-------|------|--------|-----|-----------|
| AI | [#] | [#] | [#] | [#] | [#] |
| Design | [#] | [#] | [#] | [#] | [#] |
| Video | [#] | [#] | [#] | [#] | [#] |
| ... | ... | ... | ... | ... | ... |

### Milestone Cross-Reference
| Milestone ID | Title | Related Tasks | Assigned Employees |
|--------------|-------|---------------|-------------------|
| MLT-001 | Setup | TSK-001, TSK-005 | [Names] |
| MLT-002 | Collection | TSK-010, TSK-012 | [Names] |
| MLT-003 | Entity Extraction | TSK-020, TSK-021 | [Names] |
| MLT-004 | Gap Analysis | TSK-030 | [Names] |
| MLT-005 | Template Creation | TSK-040, TSK-041 | [Names] |
| MLT-006 | Task Assignment Planning | TSK-050 | [Names] |
| MLT-007 | Task Distribution | TSK-060 | [Names] |
| MLT-008 | Quality Assurance | TSK-070 | [Names] |
| MLT-009 | Archival & Reporting | TSK-080 | [Names] |

### Blocked Tasks Requiring Attention
| Task ID | Title | Employee | Blocking Issue | Date Blocked |
|---------|-------|----------|----------------|--------------|
| TSK-### | [Title] | [Name] | [Issue description] | Nov ## |

---

## Notes & Processing Details

### Extraction Methodology
- **Files Processed:** 4 comprehensive analysis reports
- **Date Range:** November 24-27, 2025
- **Extraction Date:** [Current timestamp]
- **Processing Version:** Manual/Automated [specify]

### Data Quality Notes
- **Ambiguous Assignments:** [List any tasks where employee assignment was unclear]
- **Missing Information:** [Note any tasks lacking priority, dates, or other key fields]
- **Assumptions Made:** [Document any inferences or assumptions during extraction]

### Related Documentation
- [Master Milestone Index](./00_Daily_Processing_Milestones_Index.md)
- [Task Assignment Planning](./MLT-006_Task_Assignment_Planning.md)
- [Task Distribution Process](./MLT-007_Task_Distribution.md)
- [Quality Assurance Checklist](./MLT-008_Quality_Assurance.md)

---

**End of Document**
```

---

## Step 5: Quality Assurance Checklist

Before finalizing the `employees.to-do` file, verify:

- [ ] All 4 Executive analysis files were read completely
- [ ] Task IDs are unique and properly formatted
- [ ] Employee names are spelled consistently
- [ ] All departments are standardized (AI, Design, Video, Dev, Finance, HR, LG, Sales)
- [ ] Priority levels are assigned to every task
- [ ] Status is determined for every task
- [ ] Dates match the source file dates (24, 25, 26, 27)
- [ ] Summary statistics are calculated correctly
- [ ] Cross-reference tables are complete and accurate
- [ ] Milestone references link to existing MLT-### files in the folder
- [ ] Unassigned tasks are captured in their own section
- [ ] Table of Contents links work correctly
- [ ] Markdown formatting is clean and consistent
- [ ] No duplicate tasks across dates (unless genuinely repeated)
- [ ] Related dependencies and resources are captured

---

## Step 6: Additional Context

### Employee Name Standardization
When extracting employee names, use full names as they appear in the analysis. Common formats:
- "Firstname Lastname" (e.g., "Artemchuk Nikolay")
- "Lastname Firstname" (e.g., "Ponomarova Kateryna")
- Keep consistent with how they appear in majority of mentions

### Department Code Mapping
| Full Name | Short Code |
|-----------|------------|
| Artificial Intelligence | AI / AID |
| Design | DGN / Design |
| Video Production | VID / Video |
| Development | DEV / Dev |
| Finance | FIN / Finance |
| Human Resources | HRM / HR |
| Lead Generation | LGN / LG |
| Sales | SLS / Sales |

### Task Type Recognition
- **TSK-###:** Individual actionable tasks
- **MLT-###:** Milestones (major process steps with multiple deliverables)
- **PRT-###:** Projects (multi-week initiatives with multiple tasks)

### Priority Context Clues
Look for these keywords in the analysis:
- **HIGH:** "urgent", "critical", "ASAP", "blocking", "must", "required immediately", "crisis", "emergency"
- **MEDIUM:** "should", "planned", "this week", "important", "necessary", "scheduled"
- **LOW:** "could", "optional", "future", "nice to have", "when possible", "eventually", "consider"

### Status Context Clues
- **Completed:** "done", "finished", "completed", "resolved", "implemented", "deployed"
- **In Progress:** "working on", "in process", "started", "currently", "ongoing"
- **Not Started:** "will", "need to", "plan to", "upcoming", "scheduled to start"
- **Blocked:** "waiting for", "blocked by", "pending", "requires", "cannot proceed", "stuck"

---

## Expected Output

**File:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\PLANS\Week_4\employees.to-do`

**Size Estimate:**
- 100-200 tasks total (based on 5 comprehensive analysis reports)
- 20-50 employees with assignments
- 150-400 KB file size

**Processing Time Estimate:**
- Manual: 3-5 hours
- AI-assisted: 10-20 minutes
- Fully automated: 2-5 minutes

---

## Usage Instructions

### To Execute This Prompt:
1. Copy this entire document
2. Provide it to an AI assistant (Claude, GPT-4, etc.)
3. Ensure the AI has access to read the 4 source files
4. Ensure the AI has permission to write to the target directory
5. Review the generated output for accuracy
6. Make manual corrections if needed

### Post-Generation Steps:
1. Validate employee name spellings against HR records
2. Cross-check task IDs with existing task tracking systems
3. Verify milestone references match actual MLT-### files
4. Distribute relevant sections to department heads
5. Update individual employee task folders in Nov25 structure

---

## Customization Options

If you need modifications to the output format, specify:

- **Different organization:** By department first? By priority first?
- **Additional fields:** Add skill requirements? Time estimates? Difficulty ratings?
- **Filtering:** Exclude completed tasks? Only include specific departments?
- **Export format:** Need JSON output? CSV table? Excel spreadsheet?
- **Integration:** Need to match specific task tracking software format?

---

**Version:** 1.0
**Created:** November 28, 2025
**Purpose:** Extract Executive analysis data to consolidated employee task list
**Output Location:** `ENTITIES/DAILIES/PLANS/Week_4/employees.to-do`
