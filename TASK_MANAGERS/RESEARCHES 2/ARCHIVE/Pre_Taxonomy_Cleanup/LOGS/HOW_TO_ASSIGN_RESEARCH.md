# How to Assign Research Tasks - Step-by-Step Guide

**Created:** 2025-11-21
**Location:** `ENTITIES/TASK_MANAGERS/RESEARCHES/LOGS/`
**Purpose:** Practical walkthrough for manually assigning research tasks to employees

---

## Overview

This guide walks you through the complete process of assigning a research task from identification to employee notification. Follow these steps for every research assignment.

**Time Required:** 10-15 minutes per assignment

---

## Step-by-Step Process

### STEP 1: Identify Research Need

**Where to look:**
- [Department Gap Analysis](DEPARTMENT_GAP_ANALYSIS.md) - Systematic gaps across all departments
- [Video Processing Status Report](../RESEARCHES/PROCESSING_STATUS_REPORT.md) - Videos needing Phase 5-7
- Ad-hoc requests from department leads
- New tool discoveries requiring evaluation

**Action:**
1. Open [DEPARTMENT_GAP_ANALYSIS.md](DEPARTMENT_GAP_ANALYSIS.md)
2. Review current gaps by priority (High → Medium → Low)
3. Select ONE research task to assign

**Example:**
```
Selected: RSH-VID-001
Description: Video_006 Gap Analysis + Library Mapping (Lead Generation video)
Priority: High
Estimated Time: 1.5 hours
Department: Lead Generation / AI
```

---

### STEP 2: Determine Required Skills

**Questions to ask:**
- What department does this research serve? (AI, Design, Dev, LG, Video, HR, Sales, SMM)
- What specific skills are needed? (Check gap description in DEPARTMENT_GAP_ANALYSIS.md)
- What tools/knowledge required? (Video editing, AI tools, development, etc.)

**Action:**
1. Read the gap description carefully
2. Note required skills
3. Note if department expertise required

**Example:**
```
Task: RSH-VID-001 (Video_006 - Lead Generation)
Required Skills:
- Lead Generation knowledge (understand workflows and tools)
- OR AI/Video processing knowledge (understand Phase 5-7)
- Research and documentation skills
Preferred: Lead Gen department employee who knows the methods
```

---

### STEP 3: Find Available Employees

**Action:**
1. Open [ACTIVE_EMPLOYEES_LIST.md](ACTIVE_EMPLOYEES_LIST.md)
2. Go to "Employees by Status" section
3. Look at "AVAILABLE Status" employees first
4. Find employees matching required skills

**Decision Tree:**
```
Do any "Available" employees have matching department + skills?
├─ YES → Note their names → Go to Step 4
└─ NO → Check "Work" status employees
    ├─ Any "Work" employees with matching skills?
    │   ├─ YES → Note their names → Check they have capacity → Go to Step 4
    │   └─ NO → Look for close skill match (cross-training opportunity) → Go to Step 4
```

**Example:**
```
Task: RSH-VID-001 (Lead Gen research)

Checking AVAILABLE employees:
✅ Davlatmamadova Firuza (84059) - Lead Generator, Available
✅ Archibong Isaac (86453) - Lead Generator, Available
✅ Bindiak Dana (87396) - Lead Generator, Available

Best Match: Davlatmamadova Firuza (highest priority in assignment matrix)

Alternative (if Lead Gen not available):
✅ Perederii Vladislav (86246) - AI/Prompt Engineer, can handle video processing
```

---

### STEP 4: Check Employee History

**Action:**
1. Open [EMPLOYEE_RESEARCH_HISTORY.md](EMPLOYEE_RESEARCH_HISTORY.md)
2. Find the employee's section
3. Check:
   - Total research tasks completed
   - Average quality score
   - Similar research done before?
   - Average completion time

**Decision Logic:**
```
Has employee completed research before?
├─ YES → Check quality score
│   ├─ Score 7-10 → Great choice, proceed
│   ├─ Score 5-6 → OK choice, provide clear guidance
│   └─ Score 0-4 → Consider different employee OR plan for extra support
└─ NO (First time researcher)
    → OK to assign, but:
       - Start with simple research (avoid complex gap analysis)
       - Provide examples and templates
       - Allow extra time
       - Plan for quality review
```

**Example:**
```
Employee: Davlatmamadova Firuza (84059)
Research History: 0 completed tasks (new to research assignments)
Average Quality: N/A

Decision: OK to assign (Lead Gen is her department, 1.5 hour task is reasonable for first research)
Plan: Provide PMT-009 prompt, show example from Video_002 gap analysis
```

---

### STEP 5: Check Current Workload

**Action:**
1. Open [WEEKLY_RESEARCH_PLAN.md](WEEKLY_RESEARCH_PLAN.md)
2. Check "Employee Workload This Week" table
3. Count tasks already assigned to this employee

**Workload Limits:**
- **Available (Rate 1.0):** Max 8 hours/week research
- **Work (Rate 1.25):** Max 6 hours/week research
- **Work (Rate 1.0):** Max 4 hours/week research
- **Work (Rate 0.5):** Max 0 hours/week (avoid assignments)

**Decision Logic:**
```
Current weekly hours for employee: ___ hours
This task requires: ___ hours
Total if assigned: ___ hours

Is total ≤ max hours for employee status?
├─ YES → Proceed to Step 6
└─ NO → Choose different employee OR defer task to next week
```

**Example:**
```
Employee: Davlatmamadova Firuza
Status: Available (max 8 hours/week)
Current assignments this week: 0 tasks, 0 hours
This task: 1.5 hours
Total if assigned: 1.5 hours

✅ APPROVED (well under 8 hour limit)
```

---

### STEP 6: Set Deadline

**Standard Timelines:**
- **Simple tool research (1-2 hours):** 3-5 days
- **Video Phase 5-7 (1-2 hours):** 3-5 days
- **Complex workflow/gap analysis (2-4 hours):** 5-7 days
- **Market research (3-5 hours):** 7-10 days

**Adjustments:**
- **First-time researcher:** +2 days
- **High priority:** -1 day (but realistic)
- **Employee requests more time:** +2-3 days (be flexible)

**Action:**
1. Calculate standard deadline based on research type
2. Apply adjustments if needed
3. Check it doesn't conflict with holidays/weekends
4. Set due date

**Example:**
```
Task: RSH-VID-001 (1.5 hours, Video Phase 5-7)
Standard timeline: 3-5 days
Adjustment: +2 days (first-time researcher)
Total: 5-7 days

Assigned Date: 2025-11-21 (Thursday)
Due Date: 2025-11-28 (Thursday, 7 days)
```

---

### STEP 7: Create Assignment ID

**Format:** `RSH-{DEPT}-###`

**Department Codes:**
- AI = Artificial Intelligence
- DGN = Design
- DEV = Development
- LGN = Lead Generation
- VID = Video
- HRM = HR
- SLS = Sales
- SMM = Social Media Marketing

**Numbering:**
- Check [RESEARCH_ASSIGNMENT_LOG.md](RESEARCH_ASSIGNMENT_LOG.md) for last ID used in department
- Increment by 1

**Example:**
```
Department: Lead Generation (LGN)
Last ID used: (none - first LGN research)
New ID: RSH-LGN-001

Alternative if this is Video-related:
Department: Video (VID)
Last ID used: RSH-VID-005
New ID: RSH-VID-006
```

---

### STEP 8: Update Research Assignment Log

**Action:**
1. Open [RESEARCH_ASSIGNMENT_LOG.md](RESEARCH_ASSIGNMENT_LOG.md)
2. Find the "Active Assignments" table
3. Add new row with assignment details

**Required Fields:**
- Assignment ID (from Step 7)
- Research Type (Video Phase 5-7, Tool Research, etc.)
- Task Description (brief summary)
- Assigned To (employee name)
- Employee ID (from ACTIVE_EMPLOYEES_LIST)
- Department (employee's department)
- Assigned Date (today's date)
- Due Date (from Step 6)
- Status (Pending)
- Priority (High/Medium/Low from DEPARTMENT_GAP_ANALYSIS)

**Example:**
```markdown
| RSH-VID-001 | Video Phase 5-7 | Video_006 Gap Analysis + Library Mapping | Davlatmamadova Firuza | 84059 | Lead Gen | 2025-11-21 | 2025-11-28 | Pending | High |
```

Save the file.

---

### STEP 9: Update Weekly Research Plan

**Action:**
1. Open [WEEKLY_RESEARCH_PLAN.md](WEEKLY_RESEARCH_PLAN.md)
2. Find current week section
3. Update "Employee Workload This Week" table

**Update:**
- Add task to employee's row
- Update total hours
- Update availability status if approaching limit

**Example:**
```markdown
| Davlatmamadova Firuza | Lead Gen | 1 task (RSH-VID-001) | 1.5 hours | Available - Good |
```

4. Also update "Weekly Priorities" section to mark task as "Assigned"

Save the file.

---

### STEP 10: Prepare Employee Brief

**Create a message for the employee with:**

1. **Assignment ID:** RSH-VID-001
2. **Task Title:** Video_006 Gap Analysis + Library Mapping
3. **Purpose:** Analyze Lead Generation video to identify tools/workflows and map to LIBRARIES
4. **Estimated Time:** 1.5 hours
5. **Due Date:** 2025-11-28
6. **Location of Materials:**
   - Video transcription: `TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_006.md`
   - Prompt to use: `PROMPTS/PROMPTS/Taxonomy_Integration/PMT-009...md`
   - Example output: `TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/Video_002_Gap_Analysis.md`
7. **What to deliver:**
   - Gap Analysis document (what tools/workflows are in video but not in LIBRARIES)
   - Updated LIBRARIES entries (if applicable)
   - Library Mapping Report (showing what was added)
8. **Questions?** Contact [your name/role]

**Template:**
```
Subject: Research Assignment RSH-VID-001 - Video_006 Gap Analysis

Hi [Employee Name],

I'd like to assign you a research task:

**Assignment ID:** RSH-VID-001
**Task:** Video_006 Gap Analysis + Library Mapping
**Department:** Lead Generation
**Estimated Time:** 1.5 hours
**Due Date:** Thursday, November 28, 2025

DESCRIPTION:
Review the Video_006 transcription (Lead Generation methods video) and:
1. Identify all tools, workflows, and methods mentioned
2. Check which ones are already in our LIBRARIES
3. Create Gap Analysis document showing what's missing
4. Add missing items to LIBRARIES
5. Create Library Mapping Report showing additions

MATERIALS:
- Video Transcription: RESEARCHES/02_TRANSCRIPTIONS/Video_006.md
- Prompt to use: PROMPTS/PROMPTS/Taxonomy_Integration/PMT-009...md
- Example: RESEARCHES/03_ANALYSIS/Gap_Analysis/Video_002_Gap_Analysis.md

This is your first research assignment, so I've included an example output to guide you. Please review the example before starting, and let me know if you have questions!

OUTPUT LOCATION:
- Gap Analysis: RESEARCHES/03_ANALYSIS/Gap_Analysis/Video_006_Gap_Analysis.md
- Library Mapping: RESEARCHES/03_ANALYSIS/Library_Mapping/Video_006_Library_Mapping_Report.md

Questions? Reply to this message or contact me directly.

Thanks!
[Your Name]
```

---

### STEP 11: Notify Employee

**Method:** (Outside this documentation system)
- Send email with employee brief
- Or: Direct message (Slack/Teams/etc.)
- Or: In-person conversation
- Or: Assignment management system

**Important:**
- Don't just assign - explain the context and importance
- Invite questions
- Provide examples for first-time researchers
- Set clear expectations for output

---

### STEP 12: Set Follow-Up Reminders

**Recommended Check-Ins:**

For 7-day assignment:
- **Day 2:** "Have you started? Any questions about the prompt or examples?"
- **Day 4:** "How's progress? Any blockers I can help with?"
- **Day 6:** "Reminder: Due in 2 days. Do you need an extension?"

For 3-5 day assignment:
- **Day 2:** "How's it going? Any questions?"
- **Day before due:** "Reminder: Due tomorrow. On track?"

**Action:**
- Add reminder to your calendar/todo list
- Note in WEEKLY_RESEARCH_PLAN.md when check-ins planned

---

## Quick Reference Checklist

Before finalizing assignment, verify:

- [ ] **Need Identified:** Research task clearly defined
- [ ] **Skills Matched:** Employee has required skills (or close with support)
- [ ] **Availability Confirmed:** Employee is "Available" OR "Work" with capacity
- [ ] **Workload Checked:** Employee not exceeding max hours for status
- [ ] **History Reviewed:** Checked past quality if applicable
- [ ] **Deadline Set:** Realistic timeline with appropriate adjustments
- [ ] **ID Created:** Assignment ID following RSH-{DEPT}-### format
- [ ] **Log Updated:** RESEARCH_ASSIGNMENT_LOG.md updated
- [ ] **Plan Updated:** WEEKLY_RESEARCH_PLAN.md updated
- [ ] **Brief Prepared:** Employee message with all details
- [ ] **Employee Notified:** Assignment sent to employee
- [ ] **Follow-Ups Scheduled:** Check-in reminders set

---

## Example: Complete Assignment Walkthrough

### Assignment: RSH-AI-001 (Gemini 2.0 Features Research)

**STEP 1: Identify Need**
- Source: DEPARTMENT_GAP_ANALYSIS.md → AI Department → Gap 1
- Task: Research Gemini 2.0 Features
- Priority: High
- Estimated: 2 hours

**STEP 2: Determine Skills**
- Department: AI
- Skills: AI Tools, Model Knowledge, Research
- Preferred: Someone who uses AI models daily

**STEP 3: Find Available Employees**
- Checked ACTIVE_EMPLOYEES_LIST.md
- Found: Perederii Vladislav (86246) - Available, Prompt Engineer
- Perfect match: AI tools expertise, Available status

**STEP 4: Check History**
- Checked EMPLOYEE_RESEARCH_HISTORY.md
- Perederii: 0 completed tasks (new to research)
- Plan: Provide examples, allow extra time

**STEP 5: Check Workload**
- Checked WEEKLY_RESEARCH_PLAN.md
- Current: 0 tasks, 0 hours
- This task: 2 hours
- Status: Available (max 8 hours)
- ✅ Approved (2 hours well under limit)

**STEP 6: Set Deadline**
- Standard: 3-5 days for 2-hour research
- Adjustment: +2 days (first-time)
- Total: 5-7 days
- Assigned: 2025-11-21
- Due: 2025-11-29 (8 days - Friday)

**STEP 7: Create ID**
- Department: AI
- Last AI ID: (none yet)
- New ID: RSH-AI-001

**STEP 8: Update Assignment Log**
```markdown
| RSH-AI-001 | AI Model Research | Research Gemini 2.0 Features | Perederii Vladislav | 86246 | AI | 2025-11-21 | 2025-11-29 | Pending | High |
```

**STEP 9: Update Weekly Plan**
```markdown
| Perederii Vladislav | AI | 1 task (RSH-AI-001) | 2 hours | Available - Good |
```

**STEP 10: Prepare Brief**
```
Subject: Research Assignment RSH-AI-001 - Gemini 2.0 Features

Hi Vladislav,

I'd like to assign you a research task on AI model features:

**Assignment ID:** RSH-AI-001
**Task:** Research Gemini 2.0 Features
**Estimated Time:** 2 hours
**Due Date:** Friday, November 29, 2025

DESCRIPTION:
Research the latest Gemini 2.0 model features and capabilities:
1. Find YouTube tutorials and documentation on Gemini 2.0
2. Identify new features vs. previous versions
3. Document key capabilities for automation use cases
4. Identify potential applications for our AI workflows
5. Create research report with findings and recommendations

FOCUS AREAS:
- Multimodal capabilities
- API features and integration options
- Use cases for automation and workflow enhancement
- Comparison with other frontier models (Claude, GPT-4)

OUTPUT:
Create a research report: RESEARCHES/AI_Research/RSH-AI-001_Gemini_2.0_Features_Report.md

This is your first research assignment. If you need examples of research reports or have questions about the format, let me know!

Questions? Reply here or message me directly.

Thanks!
[Your Name]
```

**STEP 11: Notify Employee**
- Email sent: 2025-11-21 10:00 AM

**STEP 12: Set Follow-Ups**
- Day 3 (Nov 24): Check-in on progress
- Day 6 (Nov 27): Reminder and offer support
- Day 8 (Nov 29): Due date

✅ Assignment Complete!

---

## Common Mistakes to Avoid

1. **Assigning without checking workload**
   - Result: Employee overloaded, quality suffers
   - Solution: Always check WEEKLY_RESEARCH_PLAN.md first

2. **Not providing examples to new researchers**
   - Result: Confusion, multiple revisions needed
   - Solution: Always include example outputs for first-time assignments

3. **Unrealistic deadlines**
   - Result: Rushed work, low quality, employee stress
   - Solution: Use standard timelines + adjustments for experience level

4. **Poor skill matching**
   - Result: Employee struggles, takes too long, poor quality
   - Solution: Follow decision tree in ASSIGNMENT_GUIDELINES.md

5. **No follow-up**
   - Result: Employee stuck with blocker, misses deadline
   - Solution: Set check-in reminders for midpoint and day before due

6. **Vague task description**
   - Result: Employee delivers wrong output
   - Solution: Use detailed employee brief template with clear deliverables

7. **Forgetting to update logs**
   - Result: Duplicate assignments, lost tracking
   - Solution: Make Step 8-9 (updating logs) mandatory before notifying employee

---

## Related Documentation

- [Assignment Guidelines](ASSIGNMENT_GUIDELINES.md) - Decision frameworks and rules
- [Active Employees List](ACTIVE_EMPLOYEES_LIST.md) - Who's available and their skills
- [Department Gap Analysis](DEPARTMENT_GAP_ANALYSIS.md) - What research is needed
- [Research Assignment Log](RESEARCH_ASSIGNMENT_LOG.md) - All assignments tracking
- [Weekly Research Plan](WEEKLY_RESEARCH_PLAN.md) - Current week priorities
- [Employee Research History](EMPLOYEE_RESEARCH_HISTORY.md) - Past performance

---

*Created: 2025-11-21*
*Last Updated: 2025-11-21*
*Use this guide for every research assignment*
