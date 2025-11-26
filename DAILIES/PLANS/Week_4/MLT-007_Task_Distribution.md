# MLT-007: Task Distribution

**Milestone ID:** MLT-007
**Milestone Name:** Task Distribution
**Duration:** 30 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 7 of 9

---

## Overview

Create or update tasks.md files in each assigned employee's tomorrow folder (DD+1). Distribute all 87 tasks to ~58 employees across 7 departments.

---

## What You'll Do

### 1. Identify Tomorrow's Date Folders

**Today:** 2025-11-25 (DD = 25)
**Tomorrow:** 2025-11-26 (DD+1 = 26)

**Folder Pattern:**
```
/Nov25/{Department}/{Employee Name}/Week_{X}/{DD+1}/
```

**Examples:**
- `/Nov25/AI/Artemchuk Nikolay/Week_3/26/`
- `/Nov25/Design/Bogun Polina/Week_3/26/`
- `/Nov25/LG/Bessarab Valeriia/Week_3/26/`

---

### 2. Task File Format

**File Name:** `tasks.md`

**Location:** Inside each employee's DD+1 folder

**Structure:**

```markdown
# Tasks for 2025-11-26

**Assigned To:** {Employee Name}
**Department:** {Department}
**Profession:** {Profession}
**Date:** 2025-11-26

---

## Task 1: {Task Name}

**Template ID:** TST-{ID}
**Template Name:** {TASK_NAME}
**Priority:** {High/Medium/Low}
**Estimated Duration:** {X} minutes
**Department:** {Dept Code}
**Status:** Not Started

### Description
{Full task description}

### Required Tools
- {Tool 1}: {URL or location}
- {Tool 2}: {URL or location}

### Required Skills
- {Skill 1}
- {Skill 2}

### Steps
1. {Step 1 description} (X min)
2. {Step 2 description} (X min)
3. {Step 3 description} (X min)

### Checklist
- [ ] {Checklist item 1}
- [ ] {Checklist item 2}
- [ ] {Checklist item 3}

### Deliverables
- {Deliverable 1}: {Format} - {Location}

### Success Criteria
- {Criterion 1}
- {Criterion 2}

**Template Reference:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-{ID}_{Task_Name}.json`

---

## Task 2: {Next Task}
...
```

---

## Example Task Distribution

### Example 1: Artemchuk Nikolay (AI Department, 4 tasks)

**File:** `/Nov25/AI/Artemchuk Nikolay/Week_3/26/tasks.md`

```markdown
# Tasks for 2025-11-26

**Assigned To:** Artemchuk Nikolay
**Department:** AI & Automation (AID)
**Profession:** Project Manager (PRF-PRJ)
**Date:** 2025-11-26
**Total Tasks:** 4
**Estimated Total Time:** 120 minutes (2 hours)

---

## Task 1: Update Project Status in Notion

**Template ID:** TST-075
**Template Name:** Update_Project_Status_Notion
**Priority:** High
**Estimated Duration:** 20 minutes
**Department:** AID
**Status:** Not Started

### Description
Update the current status of all active AI projects in the Notion workspace. Review project progress, update completion percentages, add blockers, and set next milestones.

### Required Tools
- Notion: https://notion.so
- Access to AI Projects workspace

### Required Skills
- Project management
- Notion workspace management
- Status reporting

### Steps
1. Open Notion AI Projects database (5 min)
2. Review each active project's progress (10 min)
3. Update completion percentages and status (3 min)
4. Add any new blockers or notes (2 min)

### Checklist
- [ ] All active projects reviewed
- [ ] Completion % updated for each
- [ ] Blockers documented
- [ ] Next milestones set
- [ ] Team notified of updates

### Deliverables
- Updated Notion database: AI Projects workspace

### Success Criteria
- All projects have current status (updated today)
- Completion percentages accurate
- No missing information

**Template Reference:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-075_Update_Project_Status_Notion.json`

---

## Task 2: Generate Weekly Report in Google Sheets

**Template ID:** TST-076
**Template Name:** Generate_Weekly_Report_Google_Sheets
**Priority:** High
**Estimated Duration:** 30 minutes
**Department:** AID
**Status:** Not Started

### Description
Create the weekly metrics report for the AI & Automation team showing task completion, automation uptime, and key KPIs.

### Required Tools
- Google Sheets: https://sheets.google.com
- Access to AI Metrics dashboard
- Task tracking data

### Required Skills
- Data processing
- Google Sheets
- Reporting

### Steps
1. Open weekly report template in Google Sheets (2 min)
2. Export task completion data from Asana/Jira (10 min)
3. Calculate automation uptime metrics (8 min)
4. Update KPI dashboard with new data (5 min)
5. Generate summary and insights (5 min)

### Checklist
- [ ] Template opened and dated
- [ ] Task data imported
- [ ] Automation metrics calculated
- [ ] KPIs updated
- [ ] Summary written
- [ ] Report shared with team

### Deliverables
- Weekly Report: Google Sheets file
- Location: `/Shared/Reports/AI_Weekly_2025-11-26.xlsx`

### Success Criteria
- All sections complete
- Data accurate and up-to-date
- Shared with team by end of day

**Template Reference:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-076_Generate_Weekly_Report_Google_Sheets.json`

---

## Task 3: Schedule Team Meeting in Calendly
[...continue with task 3]

## Task 4: Backup Project Files to Dropbox
[...continue with task 4]

---

**End of Tasks**
```

---

### Example 2: Bogun Polina (Design Department, 3 tasks)

**File:** `/Nov25/Design/Bogun Polina/Week_3/26/tasks.md`

```markdown
# Tasks for 2025-11-26

**Assigned To:** Bogun Polina
**Department:** Design (DGN)
**Profession:** UI/UX Designer (PRF-DGN)
**Date:** 2025-11-26
**Total Tasks:** 3
**Estimated Total Time:** 165 minutes (2.75 hours)

---

## Task 1: Create Social Media Post for Instagram

**Template ID:** TST-074
**Template Name:** Create_Social_Media_Post_Instagram
**Priority:** High
**Estimated Duration:** 45 minutes
**Department:** DGN
**Status:** Not Started

### Description
Design an engaging Instagram post for the company's social media campaign. Create visual graphics, write caption copy, and prepare for publication.

### Required Tools
- Figma: https://figma.com
- Photoshop (optional): Adobe Creative Cloud
- Instagram brand guidelines: `/Design/Brand/Instagram_Guidelines.pdf`

### Required Skills
- Mobile design
- Social media design
- Graphic design
- UX writing

### Steps
1. Review campaign brief and brand guidelines (10 min)
2. Create design mockup in Figma (20 min)
3. Write caption and hashtags (5 min)
4. Export graphics for Instagram (1080x1080) (5 min)
5. Review and make final adjustments (5 min)

### Checklist
- [ ] Design follows brand guidelines
- [ ] Image size correct (1080x1080)
- [ ] Caption written (max 150 chars)
- [ ] Hashtags included (5-10)
- [ ] File exported in PNG format
- [ ] Saved to shared folder
- [ ] Ready for scheduling

### Deliverables
- Instagram Post Design: PNG file (1080x1080)
- Caption text: .txt file
- Location: `/Design/Social_Media/Instagram/2025-11-26_Post.png`

### Success Criteria
- Design approved by marketing team
- Meets Instagram specifications
- On-brand and visually appealing

**Template Reference:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-074_Create_Social_Media_Post_Instagram.json`

---

## Task 2: Design Email Newsletter in Figma
[...continue with task 2]

## Task 3: Create Video Thumbnail in Photoshop
[...continue with task 3]

---

**End of Tasks**
```

---

### Example 3: Bessarab Valeriia (Lead Generation, 5 tasks)

**File:** `/Nov25/LG/Bessarab Valeriia/Week_3/26/tasks.md`

```markdown
# Tasks for 2025-11-26

**Assigned To:** Bessarab Valeriia
**Department:** Lead Generation (LGN)
**Profession:** Lead Generator (PRF-LDG)
**Date:** 2025-11-26
**Total Tasks:** 5
**Estimated Total Time:** 125 minutes (2 hours)

---

## Task 1: Export Contacts to CSV from LinkedIn

**Template ID:** TST-072
**Template Name:** Export_Contacts_CSV_LinkedIn
**Priority:** High
**Estimated Duration:** 15 minutes
**Department:** LGN
**Status:** Not Started

### Description
Export filtered contact list from LinkedIn Sales Navigator to CSV file for the lead database. Target: B2B SaaS companies in North America.

### Required Tools
- LinkedIn Sales Navigator: https://www.linkedin.com/sales/
- Chrome browser (for export extension)

### Required Skills
- Lead generation
- LinkedIn prospecting
- Data export

### Steps
1. Open LinkedIn Sales Navigator (1 min)
2. Apply search filters: B2B SaaS, North America, 50-200 employees (3 min)
3. Review and select all relevant contacts (up to 2,500) (5 min)
4. Click Export → CSV format (2 min)
5. Download and verify CSV file (4 min)

### Checklist
- [ ] Filters applied correctly
- [ ] Contact count matches expectation (aim for 500+)
- [ ] CSV file downloaded successfully
- [ ] All required fields present (name, title, company, email)
- [ ] No duplicate entries
- [ ] File saved to correct location

### Deliverables
- LinkedIn Contacts Export: CSV file
- Location: `/LG/Contact_Lists/LinkedIn_Export_2025-11-26.csv`

### Success Criteria
- CSV contains minimum 500 contacts
- All email fields populated
- No formatting errors
- Ready for import to CRM

**Template Reference:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-072_Export_Contacts_CSV_LinkedIn.json`

---

## Task 2: Generate Leads Via Hunter.io
[...continue with remaining 4 tasks]

---

**End of Tasks**
```

---

## Distribution Process

### Manual Distribution (30 minutes)

**For each employee in assignment plan:**

1. **Navigate to tomorrow folder:**
   ```
   /Nov25/{Dept}/{Employee}/Week_X/{DD+1}/
   ```

2. **Check if tasks.md exists:**
   - If YES → Open and append new tasks
   - If NO → Create new tasks.md file

3. **Write task content:**
   - Load task template: `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-{ID}_{Name}.json`
   - Convert JSON to markdown format
   - Add to tasks.md

4. **Verify and save:**
   - Check all required sections present
   - Verify links and references
   - Save file

5. **Repeat for next employee**

**Time:** ~30 seconds per task × 87 tasks = ~45 minutes (actual: 30 min with practice)

---

### Automated Distribution (Future)

**Script:** `distribute_tasks.py`

```python
# Pseudo-code
assignment_plan = load('assignment_plan_2025-11-25.md')
templates = load('/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/')

for employee, tasks in assignment_plan.items():
    folder = f'/Nov25/{employee.dept}/{employee.name}/Week_{week}/{dd+1}/'
    tasks_file = folder + 'tasks.md'

    # Create header
    content = create_header(employee, tasks)

    # Add each task
    for task in tasks:
        template = templates[task.template_id]
        task_md = convert_to_markdown(template)
        content += task_md

    # Save file
    save(tasks_file, content)
```

**Time Savings:** 30 min → 5 min (25 min saved)

---

## Departments to Process

| Department | Employees | Total Tasks | Avg Time/Employee |
|------------|-----------|-------------|-------------------|
| AI (AID) | 10 | 18 | ~3 min |
| Design (DGN) | 15 | 22 | ~3 min |
| LG (LGN) | 20 | 25 | ~4 min |
| Video (VID) | 8 | 12 | ~3 min |
| Sales (SLS) | 3 | 6 | ~3 min |
| Dev (DEV) | 2 | 3 | ~2 min |
| HR (HRM) | 1 | 1 | ~1 min |
| **TOTAL** | **59** | **87** | **30 min** |

---

## Checklist

- [ ] Load assignment_plan_2025-11-25.md
- [ ] Identify tomorrow's date (DD+1 = 26)
- [ ] Process AI department employees (10)
- [ ] Process Design department employees (15)
- [ ] Process Lead Generation employees (20)
- [ ] Process Video department employees (8)
- [ ] Process Sales employees (3)
- [ ] Process Development employees (2)
- [ ] Process HR employees (1)
- [ ] Verify all 87 tasks distributed
- [ ] Verify all tasks.md files saved correctly
- [ ] Check file formatting and links
- [ ] Update processing log with distribution metrics

---

## Expected Outcomes

✅ **Tasks Distributed**
- **Files Created/Updated:** ~59 tasks.md files
- **Tasks Written:** 87 task descriptions
- **Location:** Each employee's `/Nov25/{Dept}/{Name}/Week_X/26/tasks.md`

✅ **Ready for MLT-008**
- All employees have tomorrow's tasks
- Task files formatted correctly
- Template references included

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| DD+1 folder doesn't exist | Create Week_X/{DD+1}/ folder |
| tasks.md already exists | Append new tasks, don't overwrite |
| Employee folder not found | Check spelling, verify employee is active |
| Template JSON missing | Create basic task description, flag for review |
| Week number uncertainty | Check last active week folder |

---

## Verification

After distribution, verify:

```markdown
## Distribution Verification

- [x] All 87 tasks distributed (0 remaining)
- [x] 59 employees have tasks.md files
- [x] All files in correct DD+1 folders
- [x] Template references correct
- [x] No duplicate task assignments
- [x] Formatting consistent across all files
```

---

## Next Milestone

**→ [MLT-008: Quality Assurance](MLT-008_Quality_Assurance.md)** - Verify all tasks assigned correctly, workload balanced, templates created (20 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Assignment Plan:** [assignment_plan_2025-11-25.md](../../Daily_Processing/2025-11-25_Collection/05_Distribution_Plan/assignment_plan_2025-11-25.md)
- **Task Templates:** [TSM-003 Task Templates](../../../TASK_MANAGERS/TSM-003_Task_Templates/)
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
