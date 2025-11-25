# Department Report Generation Workflow - Day 21 (2025-11-21)

**Date Created:** 2025-11-21
**Status:** Ready for Execution
**Estimated Time:** 4-6 hours for all 8 departments

---

## Overview

This document provides a step-by-step workflow for generating all 8 department reports for day 21 using the PMT-032 v2.1 framework with 10-section report schema.

---

## Prerequisites

### Data Sources Available
- ✅ **73 employee files** in `ENTITIES/DAILIES/21/`
- ✅ **Department prompts** (PMT-033 through PMT-043 v2.1)
- ✅ **Day 20 reports** as quality templates
- ✅ **TASK_MANAGERS CSVs** for entity mapping

### Tools Required
- AI Assistant (Claude, ChatGPT, or similar) for transcript analysis
- Access to ENTITIES folder structure
- Text editor for report generation

---

## Department Processing Order

Process in this order (easiest to most complex):

1. **Finance** (2 employees, 2 files) - 20-30 minutes
2. **HR** (2 employees, 6 files) - 30-40 minutes
3. **Video** (2 employees, 7 files) - 30-40 minutes
4. **AI** (2 employees, 4 files) - 30-40 minutes
5. **Dev** (3 employees, 3 files) - 30-40 minutes
6. **Sales** (2 employees, 6 files) - 30-40 minutes
7. **LG** (7 employees, 21 files) - 60-90 minutes
8. **Design** (8 employees, 24 files) - 60-90 minutes

---

## Step-by-Step Workflow (Per Department)

### Step 1: Prepare Department Context (5 minutes)

**Read Department Prompt:**
- Location: `ENTITIES/PROMPTS/DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-0##_*_Daily_Report_v2.1.md`
- Note: Department code, team size, common projects, tools

**Read Day 20 Report (Template):**
- Location: `ENTITIES/REPORTS/2025-11-20/Departments/*_Department_Report_2025-11-20.md`
- Study the structure and style

### Step 2: Collect Employee Data (5-10 minutes)

**For each employee in department:**

**AI Department Example:**
```
daily_Artemchuk_Nikolay.md
daily_report_2025-11-21_Artemchuk_Nikolay.md
plans_Artemchuk_Nikolay.md
tasks_Artemchuk_Nikolay.md
```

**Read files:**
- Daily files contain transcripts (Russian/Ukrainian)
- Plans files contain extracted action items
- Tasks files contain structured task breakdowns

### Step 3: Analyze Activities (10-15 minutes)

**For each employee's daily file:**

1. **Identify main activities** (typically 3-8 per person)
2. **Extract key information:**
   - Activity title/description
   - Time spent
   - Actions taken
   - Results/deliverables
   - Status (Completed/In Progress/Blocked)

3. **Map to entities** (use PMT-070 logic):
   - Operational/Maintenance (routine work)
   - PRT-###_Project_Name (project work)
   - TST-###_Task_Name (specific tasks)
   - MLT-###_Milestone_Name (milestones)

**Example Activity Analysis:**
```
Activity: Google Maps Scraping System Development
Time: 3 hours
Status: In Progress
Entity: PRT-007_System_Analysis → TST-055_Process_Department_Task_Files
Confidence: 85%
Actions:
- Developed Google Maps search query optimization
- Created URL structure analysis
- Designed city-based search formula
Results:
- Query optimization framework designed
- URL pattern documentation created
```

### Step 4: Generate 10-Section Report (30-45 minutes)

Using AI assistant, generate report following this structure:

#### Section 1: Executive Summary
```markdown
- Report Date: 2025-11-21
- Department: [Name] ([CODE])
- Team Size: X members
- Total Activities: X major activities
- Projects Active: X
- Tasks Completed: X
- Tasks In Progress: X
- Overall Status: On Track ✅ / At Risk ⚠️ / Blocked ❌
- Key Achievements: (3-5 bullet points)
```

#### Section 2: Project Contributions
```markdown
### [Project Name]
- Role: Lead | Support | Contributor
- Status: Active
- Progress Today: [Description] (X% complete)
- Tasks Completed: (list)
- Tasks In Progress: (list)
- Next Steps: (list)
```

#### Section 3: Milestone Progress
```markdown
### [Milestone Name]
- Progress: X% → Y% (+Z%)
- Tasks Completed Today: (list with ✅)
- Tasks In Progress: (list)
- Blockers: None | (description)
- Timeline: On track | Delayed | Ahead
- Impact: (description)
```

#### Section 4: Task Sequences and Entity Mapping
```markdown
### Activity 1: [Title]
- Entity: TST-###_Name → MLT-###_Name → PRT-###_Name
- Time: X hours
- Status: Completed ✅ | In Progress 🔄 | Blocked ❌
- Confidence: X%
- Priority: High | Medium | Low
- Employee: [Name]
- Objective: (description)
- Actions Taken: (bullet list)
- Results: (bullet list with ✅)
- Impact: (description)
```

#### Section 5: Cross-Department Coordination
```markdown
### [Initiative Name]
- From/To Department: XXX
- Request/Handoff: (description)
- Timeline: (date/status)
- Status: Completed | In Progress | Pending
- Next Steps: (description)
```

#### Section 6: Department-Specific Content

**Varies by department type:**
- **Technical (AI, Dev):** Infrastructure & Technical Achievements
- **Creative (Design, Video):** Creative Output & Assets Created
- **Operational (Finance, HR, Sales, LG):** Process Improvements & Operational Efficiency

#### Section 7: Next Day Plans
```markdown
### Planned Activity 1: [Title]
- Project/Entity: PRT-###_Name or Operational
- Priority: High | Medium | Low
- Estimated Time: X hours
- Objective: (description)
- Dependencies: None | (description)
- Assignee: [Name]
```

#### Section 8: Research Needed
```markdown
### Research Topic 1: [Title]
- Priority: High | Medium | Low
- Department: [CODE]
- Purpose: (description)
- Questions to Answer: (bullet list)
- Timeline: Immediate | This Week | This Month
- Assigned To: [Name]
```

#### Section 9: Improvements Needed
```markdown
### Improvement 1: [Title]
- Category: Process | Technical | Documentation | Training
- Priority: High | Medium | Low
- Current State: (description)
- Desired State: (description)
- Estimated Impact: (description)
- Owner: [Name]
```

#### Section 10: Metrics and Deliverables
```markdown
### Time Allocation
- Total Hours Tracked: X.X hours
- Project Work: X.X hours (X%)
- Operational/Maintenance: X.X hours (X%)
- Meetings/Coordination: X.X hours (X%)

### Deliverables Created Today
- X new files created (~XXX lines)
- X files updated (~XXX lines modified)
- X automations/scripts deployed
- X documentation pages created

### Task Status Breakdown
- Completed: X tasks
- In Progress: X tasks
- Blocked: X tasks
- Total: X tasks

### Entity Mapping Confidence
- Average Confidence: XX%
- High Confidence (>80%): X activities
- Medium Confidence (70-80%): X activities
- Low Confidence (<70%): X activities (require review)
```

### Step 5: Quality Check (5 minutes)

**Validation Checklist:**
- [ ] All 10 sections present
- [ ] Entity mappings have confidence scores
- [ ] Cross-department coordination documented
- [ ] Metrics calculated correctly
- [ ] Employee names spelled correctly
- [ ] Department code correct (AID, DGN, DEV, FNC, HRM, LGN, SLS, VID)
- [ ] File naming: `{DEPT}_Department_Report_2025-11-21.md`
- [ ] Saved to: `ENTITIES/REPORTS/2025-11-21/Departments/`

### Step 6: Save Report (1 minute)

**File Name Format:**
```
{Department}_Department_Report_2025-11-21.md
```

**Examples:**
- `AI_Department_Report_2025-11-21.md`
- `Design_Department_Report_2025-11-21.md`
- `Finance_Department_Report_2025-11-21.md`

**Save Location:**
```
C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-21\Departments\
```

---

## Department-Specific Notes

### AI Department (AID)
- **Employees:** Artemchuk Nikolay, Perederii Vladislav
- **Files:** 4 files
- **Focus:** Infrastructure, prompt engineering, automation
- **Common Projects:** PRT-001 (AI Tutorial Research), PRT-007 (System Analysis)
- **Key Activities:** Google scraping, automation setup, tool integration

### Design Department (DGN)
- **Employees:** 8 members
- **Files:** 24 files
- **Focus:** UI/UX design, creative assets, design systems
- **Common Projects:** Design system work, client projects
- **Key Activities:** Design mockups, prototypes, brand assets

### Dev Department (DEV)
- **Employees:** Artem Skichko, Azar Imranov, Klimenko Yaroslav
- **Files:** 3 files
- **Focus:** Software development, microservices, API development
- **Common Projects:** Account microservice, MCP integrations
- **Key Activities:** Coding, testing, deployment

### Finance Department (FNC)
- **Employees:** Ponomarova Kateryna, Yelisieieva Daria
- **Files:** 2 files
- **Focus:** Financial operations, reporting, expense tracking
- **Common Projects:** Operational/Maintenance
- **Key Activities:** Financial reporting, budget tracking, invoice processing

### HR Department (HRM)
- **Employees:** Nealova Evgeniya, Rekonvald Viktoriya
- **Files:** 6 files
- **Focus:** Recruitment, employee relations, onboarding
- **Common Projects:** Operational/Maintenance
- **Key Activities:** Recruitment, interviews, employee support

### LG Department (LGN - Lead Generation)
- **Employees:** 7 members
- **Files:** 21 files
- **Focus:** Lead research, outreach, CRM management
- **Common Projects:** Operational/Maintenance
- **Key Activities:** Lead research, data entry, outreach campaigns

### Sales Department (SLS)
- **Employees:** Bessarab Valeriia, Kovalska Anastasiya (dual role with LG)
- **Files:** 6 files (Sales-specific)
- **Focus:** Sales calls, client relationships, deal closing
- **Common Projects:** Operational/Maintenance
- **Key Activities:** Discovery calls, follow-ups, proposal writing

### Video Department (VID)
- **Employees:** Azanova Dar'ya, Podolskyi Sviatoslav
- **Files:** 7 files
- **Focus:** Video editing, content creation, tutorial processing
- **Common Projects:** PRT-001 (AI Tutorial Research)
- **Key Activities:** Video processing, transcript extraction, tutorial analysis

---

## Master Report Consolidation

### After All 8 Departments Complete

**Time Required:** 30-45 minutes

**Steps:**

1. **Read all 8 department reports**
2. **Extract key metrics:**
   - Total employees across all departments
   - Total hours tracked company-wide
   - Project vs operational breakdown
   - Cross-department initiatives
3. **Identify patterns:**
   - Common blockers
   - Cross-department dependencies
   - Resource bottlenecks
4. **Generate master report** following day 20 structure:
   - Executive summary (company-wide)
   - Department summaries (8 sections)
   - Cross-department coordination
   - Company-wide metrics
   - Entity mapping summary
   - Department report links

**Save as:** `MASTER_REPORT_2025-11-21.md`

---

## Tips for Efficient Processing

### Use AI Assistant Effectively
1. **Provide full context:** Give the AI the department prompt, day 20 template, and employee files
2. **Process in batches:** Do 2-3 employees at a time
3. **Review iteratively:** Check each section as it's generated
4. **Use templates:** Copy day 20 structure and replace content

### Handle Russian/Ukrainian Transcripts
1. **Use AI for translation:** Claude/ChatGPT can understand and summarize
2. **Focus on actions:** Look for verbs and project names
3. **Cross-reference tasks.md:** Structured task files are in English
4. **Ask for key points:** Request AI to extract main activities only

### Entity Mapping Guidelines
1. **Default to Operational:** When unsure, mark as Operational/Maintenance
2. **Use 70% threshold:** Only assign entities with 70%+ confidence
3. **Check day 20:** See how similar activities were mapped
4. **Document uncertainty:** Note low-confidence mappings for review

### Time Management
1. **Start with small departments:** Finance, HR build confidence
2. **Take breaks:** Every 2 departments, take 10-minute break
3. **Don't perfect:** 80% quality is sufficient, can iterate later
4. **Use copy-paste:** Reuse structure from day 20 reports

---

## Troubleshooting

### Issue: Transcript Too Long
**Solution:** Focus on tasks.md and plans.md files, use daily.md for context only

### Issue: Entity Mapping Unclear
**Solution:** Mark as Operational/Maintenance, add note for manual review

### Issue: Cross-Department Activity
**Solution:** Document in both department reports, note coordination

### Issue: Missing Employee Data
**Solution:** Note in report, mark as incomplete, continue with available data

---

## Progress Tracking

### Completion Checklist

- [ ] Finance Department Report
- [ ] HR Department Report
- [ ] Video Department Report
- [ ] AI Department Report
- [ ] Dev Department Report
- [ ] Sales Department Report
- [ ] LG Department Report
- [ ] Design Department Report
- [ ] Master Consolidated Report
- [ ] Update Processing_Summary_2025-11-21.md
- [ ] Update README.md

### Time Log Template

| Department | Start Time | End Time | Duration | Status |
|------------|-----------|----------|----------|--------|
| Finance | | | | |
| HR | | | | |
| Video | | | | |
| AI | | | | |
| Dev | | | | |
| Sales | | | | |
| LG | | | | |
| Design | | | | |
| Master | | | | |

---

## Final Quality Standards

### Each Department Report Must Have:
- ✅ All 10 sections completed
- ✅ 3-8 activities documented with entity mapping
- ✅ Confidence scores for all entities
- ✅ Time allocation metrics calculated
- ✅ Next day plans included (3-6 activities)
- ✅ Research topics identified (1-3)
- ✅ Improvements suggested (2-5)

### Master Report Must Have:
- ✅ Company-wide executive summary
- ✅ All 8 department summaries
- ✅ Cross-department coordination section
- ✅ Company-wide metrics (hours, tasks, entities)
- ✅ Links to all department reports

---

## References

### Department Prompts
- AI: `ENTITIES/PROMPTS/DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-033_AI_Daily_Report_v2.1.md`
- Design: `PMT-035_Design_Daily_Report_v2.1.md`
- Dev: `PMT-036_Dev_Daily_Report_v2.1.md`
- Finance: `PMT-037_Finance_Daily_Report_v2.1.md`
- HR: `PMT-038_HR_Daily_Report_v2.1.md`
- LG: `PMT-039_LG_Daily_Report_v2.1.md`
- Sales: `PMT-041_Sales_Daily_Report_v2.1.md`
- Video: `PMT-043_Video_Daily_Report_v2.1.md`

### Template Reports (Day 20)
- Location: `ENTITIES/REPORTS/2025-11-20/Departments/`
- All 8 departments available as reference

### Source Data
- Location: `ENTITIES/DAILIES/21/`
- 73 files total, organized by employee

---

**Document Version:** 1.0
**Last Updated:** 2025-11-21
**Author:** Automated Processing System
**Status:** Ready for Use
