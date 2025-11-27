# MLT-003: Entity Extraction

**Milestone ID:** MLT-003
**Milestone Name:** Entity Extraction
**Duration:** 60 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 3 of 9

---

## Overview

Extract tasks, actions, objects, tools, and other entities from all collected employee files using MAIN_PROMPT_v7.md. Process ~150-250 files to identify 50-100 tasks for assignment.

---

## What You'll Do

### 1. Use MAIN_PROMPT_v7.md

**Prompt Location:**
```
/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v7.md
```

**Key Extraction Line (Line 42):**
```
Output Format: MLT-### (Milestones), TST-### (Task Templates),
STP-### (Step Templates), ACT-### (Actions), OBJ-### (Objects),
TOL-### (Tools), SKL-### (Skills)
```

**What to Extract:**
- Task names and descriptions
- Actions (verbs): Create, Update, Generate, Analyze, etc.
- Objects (nouns): Report, Design, Video, Lead List, etc.
- Tools used: Figma, Claude, LinkedIn, Asana, etc.
- Skills required: UI/UX design, coding, lead generation, etc.
- Professions: Designer, Developer, Project Manager, etc.
- Departments: AI, Design, LG, Video, Sales, etc.

---

### 2. Process Files by Department

**Input:**
```
/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/01_Collected_Files/
```

**Output:**
```
/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/02_Extracted_Tasks/
```

**Process Pattern:**

#### For Each Department:

**AI Department Example:**
- Read: `AI_Artemchuk_Nikolay_daily.md`
- Extract entities using MAIN_PROMPT_v7.md
- Save to: `AI_Artemchuk_Nikolay_extracted.md`

**Design Department Example:**
- Read: `Design_Bogun_Polina_daily.md`
- Extract entities using MAIN_PROMPT_v7.md
- Save to: `Design_Bogun_Polina_extracted.md`

---

### 3. Extraction Output Format

**Save each extraction as:**
```markdown
# Extracted Entities - {Department}_{Employee_Name}

**Source Files:** daily.md, plans.md, tasks.md
**Extraction Date:** 2025-11-25
**Extracted By:** [Your Name]

---

## Tasks Identified

### Task 1: {TASK_NAME}
**Task ID:** [TBD - assign in MLT-004]
**Action:** {ACTION_VERB}
**Object:** {DELIVERABLE_NOUN}
**Tool:** {TOOL_NAME}
**Profession Match:** {PROFESSION}
**Department:** {DEPARTMENT}
**Skill Required:** {SKILL}
**Priority:** {High/Medium/Low}
**Description:** {Full description from employee files}

### Task 2: {TASK_NAME}
...

---

## Entity Taxonomy Breakdown

### Actions (ACT)
- ACT-042: Create
- ACT-128: Generate
- ACT-067: Analyze

### Objects (OBJ)
- OBJ-015: Report
- OBJ-042: Video Script
- OBJ-021: UI Design

### Tools (TOL)
- TOL-DGN-015: Figma
- TOL-AIA-001: Claude
- TOL-LGN-025: LinkedIn Sales Navigator

### Skills (SKL)
- SKL-012: UI/UX design via Figma
- SKL-003: Lead generation via LinkedIn

### Professions (PRF)
- PRF-DGN: Designer
- PRF-LDG: Lead Generator
- PRF-AIE: AI Engineer
```

---

## Example Extraction

### Input File: AI_Artemchuk_Nikolay_daily.md
```markdown
# Daily Log - 2025-11-25

## Completed
- Updated project timeline in Asana
- Created weekly report for AI team
- Analyzed automation metrics

## Planned for Tomorrow
- Generate lead list using Hunter.io
- Review design mockups in Figma
- Write documentation for MCP connector
```

### Output File: AI_Artemchuk_Nikolay_extracted.md
```markdown
# Extracted Entities - AI_Artemchuk_Nikolay

**Source Files:** daily.md, plans.md
**Extraction Date:** 2025-11-25

---

## Tasks Identified

### Task 1: Update_Project_Timeline_Asana
**Action:** Update (ACT-015)
**Object:** Project Timeline (OBJ-032)
**Tool:** Asana (TOL-BIZ-004)
**Profession Match:** Project Manager (PRF-PRJ)
**Department:** AI & Automation (AID)
**Skill Required:** project management via Asana
**Priority:** Medium
**Status:** Completed
**Description:** Updated project timeline in Asana

### Task 2: Create_Weekly_Report_AI_Team
**Action:** Create (ACT-042)
**Object:** Weekly Report (OBJ-015)
**Tool:** Google Docs (TOL-BIZ-001)
**Profession Match:** Project Manager (PRF-PRJ)
**Department:** AI & Automation (AID)
**Skill Required:** reporting, documentation
**Priority:** High
**Status:** Completed
**Description:** Created weekly report for AI team

### Task 3: Generate_Lead_List_Hunter_IO
**Action:** Generate (ACT-128)
**Object:** Lead List (OBJ-LGN-005)
**Tool:** Hunter.io (TOL-LGN-042)
**Profession Match:** Lead Generator (PRF-LDG)
**Department:** Lead Generation (LGN)
**Skill Required:** lead generation via Hunter.io
**Priority:** High
**Status:** Planned
**Description:** Generate lead list using Hunter.io - NEW TASK for distribution
```

---

## Taxonomy Reference

### Actions (ACT) from LIBRARIES

Common action verbs you'll encounter:

| ACT Code | Action | Type | Example |
|----------|--------|------|---------|
| ACT-042 | Create | CMD | Create report, Create design |
| ACT-015 | Update | CMD | Update timeline, Update status |
| ACT-128 | Generate | RST | Generate leads, Generate content |
| ACT-067 | Analyze | PRC | Analyze metrics, Analyze data |
| ACT-089 | Review | PRC | Review designs, Review code |
| ACT-105 | Write | RST | Write documentation, Write email |

**Full List:** [TAX-001 Libraries ISO Registry - Actions](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md#action-verb-type-codes)

### Objects (OBJ) from LIBRARIES

Common deliverable objects:

| OBJ Domain | Objects | Examples |
|------------|---------|----------|
| OBJ-AIA | AI & Automation | AI Workflows, Reports, Scripts |
| OBJ-DGN | Design | UI Designs, Graphics, Mockups |
| OBJ-LGN | Lead Generation | Lead Lists, Lead Magnets |
| OBJ-VID | Video | Video Scripts, Storyboards |
| OBJ-GEN | General | Documents, Reports, Presentations |

### Tools (TOL) from LIBRARIES

Common tools by category:

| Tool Category | Examples | Dept |
|---------------|----------|------|
| TOL-AIA | Claude, ChatGPT, Midjourney | AI |
| TOL-DGN | Figma, Photoshop, Illustrator | Design |
| TOL-LGN | LinkedIn, Sales Navigator, Hunter.io | LG |
| TOL-VID | Premiere, After Effects, Runway | Video |
| TOL-BIZ | Asana, Notion, Slack, Trello | All |

**Full List:** [TAX-001 Libraries ISO Registry - Tools](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md#tool-category-codes)

---

## Batch Processing Strategy

### Option 1: Manual Sequential Processing
1. Open employee file
2. Read content
3. Apply MAIN_PROMPT_v7.md
4. Write extraction file
5. Repeat for next employee

**Time:** ~60 minutes for 60 employees (~1 min/employee)

### Option 2: Batch with Claude/ChatGPT
1. Load 10 employee files
2. Send batch to AI with MAIN_PROMPT_v7.md
3. Review and save 10 extractions
4. Repeat for next batch

**Time:** ~40 minutes (20 minutes saved)

### Option 3: Future Automation Script
**Script:** `extract_tasks_batch.py`

```python
# Pseudo-code
input_dir = '01_Collected_Files/'
output_dir = '02_Extracted_Tasks/'
prompt = load('MAIN_PROMPT_v7.md')

for file in input_dir:
    content = read(file)
    extraction = ai_extract(content, prompt)
    save(output_dir + file.replace('.md', '_extracted.md'), extraction)
```

**Time:** ~10 minutes (50 minutes saved)

---

## Checklist

- [ ] Load MAIN_PROMPT_v7.md prompt
- [ ] Process AI department files (~10 employees)
- [ ] Process Design department files (~15 employees)
- [ ] Process Lead Generation files (~20 employees)
- [ ] Process Video department files (~8 employees)
- [ ] Process Sales department files (~5 employees)
- [ ] Process Development files (~3 employees)
- [ ] Process HR files (~2 employees)
- [ ] Verify all extractions saved to `02_Extracted_Tasks/`
- [ ] Count total tasks extracted (target: 50-100 tasks)
- [ ] Update processing log with extraction metrics

---

## Expected Outcomes

✅ **Entities Extracted**
- **Files Created:** 60+ extraction files in `02_Extracted_Tasks/`
- **Tasks Identified:** 50-100 unique tasks
- **Taxonomy Tagged:** All tasks tagged with ACT, OBJ, TOL, SKL, PRF, DPT codes

✅ **Ready for MLT-004**
- All tasks have action/object/tool breakdown
- Profession and department identified for each task
- Clear descriptions enable gap analysis

---

## Metrics to Track

Update `06_Processing_Log.md`:

```markdown
## MLT-003: Entity Extraction Metrics

| Metric | Count |
|--------|-------|
| Files Processed | 63 |
| Tasks Extracted | 87 |
| Unique Actions | 25 |
| Unique Objects | 34 |
| Unique Tools | 42 |
| Departments | 7 |
| Professions | 12 |
```

---

## Next Milestone

**→ [MLT-004: Gap Analysis](MLT-004_Gap_Analysis.md)** - Classify tasks as EXISTS/LIBRARY_ONLY/NEW using RESEARCHES methodology (45 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Extraction Prompt:** [MAIN_PROMPT_v7.md](../../../PROMPTS/Core/MAIN_PROMPT_v7.md)
- **Action Taxonomy:** [TAX-001 Libraries ISO Registry](../../../TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md)
- **Task Template Format:** [TSM-003 Task Templates](../../../TASK_MANAGERS/TSM-003_Task_Templates/)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
