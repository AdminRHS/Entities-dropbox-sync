# MLT-002: Collection

**Milestone ID:** MLT-002
**Milestone Name:** Collection
**Duration:** 30 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 2 of 9

---

## Overview

Copy **ALL** files from every employee's today folder (DD folder) to the workspace. This includes daily.md, plans.md, tasks.md, notes.md, and any other .md files. Process approximately 60+ employees across all departments.

---

## What You'll Do

### 1. Identify Employee Folders

**Folder Structure Pattern:**
```
/Nov25/{Department}/{Employee Name}/Week_{X}/{DD}/
```

**Example Paths:**
- `/Nov25/AI/Artemchuk Nikolay/Week_3/25/`
- `/Nov25/Design/Bogun Polina/Week_3/25/`
- `/Nov25/LG/Bessarab Valeriia/Week_3/25/`
- `/Nov25/Video/Podolskyi Sviatoslav/Week_3/25/`
- `/Nov25/Sales/Kovalska Anastasiya/Week_3/25/`

### 2. Departments to Process

| Dept Code | Department Name | Employees | Location |
|-----------|----------------|-----------|----------|
| **AID** | AI & Automation | ~10 | `/Nov25/AI/` |
| **DGN** | Design | ~15 | `/Nov25/Design/` |
| **LGN** | Lead Generation | ~20 | `/Nov25/LG/` |
| **VID** | Video Production | ~8 | `/Nov25/Video/` |
| **SLS** | Sales | ~5 | `/Nov25/Sales/` |
| **DEV** | Development | ~3 | `/Nov25/Dev/` |
| **HRM** | Human Resources | ~2 | `/Nov25/HR/` |

**Total:** ~60-65 employees

---

### 3. Files to Collect

**Copy ALL .md files from each employee's DD folder:**

| File Type | Typical Name | Contains |
|-----------|--------------|----------|
| Daily log | `daily.md` | Daily notes, accomplishments, blockers |
| Plans | `plans.md` | Plans for today/tomorrow, goals |
| Tasks | `tasks.md` | Task lists, assignments |
| Notes | `notes.md` | Meeting notes, research notes |
| Other | `*.md` | Any other markdown files |

**⚠️ Important:** Don't filter - collect **ALL** .md files!

---

### 4. Copy to Workspace

**Destination:**
```
/ENTITIES/DAILIES/Daily_Processing/YYYY-MM-DD_Collection/01_Collected_Files/
```

**Naming Convention:**
```
{Department}_{Employee_Name}_{Filename}
```

**Examples:**
```
AI_Artemchuk_Nikolay_daily.md
AI_Artemchuk_Nikolay_plans.md
AI_Artemchuk_Nikolay_tasks.md
Design_Bogun_Polina_daily.md
Design_Bogun_Polina_notes.md
LG_Bessarab_Valeriia_daily.md
Video_Podolskyi_Sviatoslav_daily.md
Sales_Kovalska_Anastasiya_daily.md
```

---

## Employee Profile Examples

Use employee profiles to understand who you're collecting from:

### Example: AI Department

**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Work/AI/Profile Project manager, Lead generator Artemchuk Nikolay.md`

```markdown
**Name:** Artemchuk Nikolay
**Profession:** project manager
**Department:** AI
**Skills:** Agile, project management, SCRUM, Data Processing
**Tools:** Asana, Jira, Monday, Notion, Slack, Trello
**Nov25 Folder:** /Dropbox/Nov25/AI/Artemchuk Nikolay
```

**Files to collect from:** `/Nov25/AI/Artemchuk Nikolay/Week_3/25/*.md`

### Example: Design Department

**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Part_Project___Part_Time/Design/Profile UI UX designer Bogun Polina.md`

```markdown
**Name:** Bogun Polina
**Profession:** ui ux designer
**Department:** Design
**Skills:** UX/UI design, prototyping, usability testing, ux writing
**Tools:** Figma, Photoshop, Illustrator, HTML, CSS
**Nov25 Folder:** /Dropbox/Nov25/Design/Bogun Polina
```

**Files to collect from:** `/Nov25/Design/Bogun Polina/Week_3/25/*.md`

### Example: Sales Department

**Profile:** `/ENTITIES/TALENTS/Employees/profiles/Work/Sales/Profile Lead generator Bessarab Valeriia.md`

```markdown
**Name:** Bessarab Valeriia
**Profession:** lead generator
**Department:** Sales (LG)
**Skills:** Lead generation, prospecting, outreach
**Tools:** LinkedIn, Sales Navigator, CRM
**Nov25 Folder:** /Dropbox/Nov25/LG/Bessarab Valeriia
```

**Files to collect from:** `/Nov25/LG/Bessarab Valeriia/Week_3/25/*.md`

---

## Collection Script (Automation Opportunity)

**Manual Process:**
1. Navigate to department folder
2. Open each employee subfolder
3. Navigate to Week_X/DD/
4. Copy all .md files
5. Rename with department_employee_filename pattern
6. Paste to `01_Collected_Files/`
7. Repeat for all employees

**Future Script:** `collect_daily_files.py`
```python
# Pseudo-code for automation
departments = ['AI', 'Design', 'LG', 'Video', 'Sales', 'Dev', 'HR']
date = '2025-11-25'
week = 'Week_3'
day = '25'

for dept in departments:
    for employee in get_employees(dept):
        source = f'/Nov25/{dept}/{employee}/{week}/{day}/*.md'
        dest = f'/ENTITIES/DAILIES/Daily_Processing/{date}_Collection/01_Collected_Files/'
        copy_and_rename(source, dest, f'{dept}_{employee}_')
```

**Time Savings:** From 30 min manual → ~2 min automated

---

## Tracking Progress

Update your `06_Processing_Log.md`:

```markdown
## MLT-002: Collection Progress

### Departments Completed
- [x] AI (10 employees, 35 files)
- [x] Design (15 employees, 52 files)
- [ ] Lead Generation (20 employees, ? files)
- [ ] Video (8 employees, ? files)
- [ ] Sales (5 employees, ? files)
- [ ] Development (3 employees, ? files)
- [ ] HR (2 employees, ? files)

### Total Files Collected: 87 / ~200
```

---

## ISO Code Context

### Department Codes in File Names

When naming collected files, use ISO department codes:

| File Prefix | ISO Code | Department |
|-------------|----------|------------|
| `AI_` | AID | AI & Automation |
| `Design_` | DGN | Design |
| `LG_` | LGN | Lead Generation |
| `Video_` | VID | Video Production |
| `Sales_` | SLS | Sales |
| `Dev_` | DEV | Development |
| `HR_` | HRM | Human Resources |

**Reference:** [TAX-001 Libraries ISO Code Registry](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md#department-iso-codes)

---

## Checklist

- [ ] Identify today's date folder (DD) across all employees
- [ ] Process AI department employees (~10)
- [ ] Process Design department employees (~15)
- [ ] Process Lead Generation employees (~20)
- [ ] Process Video department employees (~8)
- [ ] Process Sales department employees (~5)
- [ ] Process Development employees (~3)
- [ ] Process HR employees (~2)
- [ ] Verify all files copied to `01_Collected_Files/`
- [ ] Verify files renamed with {Dept}_{Employee}_{Filename} pattern
- [ ] Count total files collected
- [ ] Update processing log with collection metrics

---

## Expected Outcomes

✅ **Files Collected**
- **Target:** 150-250 .md files from ~60 employees
- **Location:** `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/01_Collected_Files/`
- **Format:** Department_EmployeeName_filename.md

✅ **Ready for MLT-003**
- All employee files available for entity extraction
- Clear file naming enables easy processing
- Processing log shows collection complete

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Employee has no DD folder | Note in log, skip employee, continue |
| DD folder is empty | Note in log, skip employee, continue |
| Files are not .md format | Collect only .md files, ignore others |
| Duplicate employee names | Add department prefix for clarity |
| Week number varies | Check last week folder with files |

---

## Next Milestone

**→ [MLT-003: Entity Extraction](MLT-003_Entity_Extraction.md)** - Extract tasks from ALL collected files using MAIN_PROMPT_v6.md (60 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Simple Workflow:** [Daily_Processing_Workflow_Simple.md](Daily_Processing_Workflow_Simple.md)
- **Employee Profiles Directory:** `/ENTITIES/TALENTS/Employees/profiles/`
- **Department ISO Codes:** [TAX-001 Libraries ISO Registry](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
