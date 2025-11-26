You are an AI planning assistant. Your task is to generate a complete weekly planning package for Week 4 for all departments and all employees.  
Use the content from:
- Week 3 summaries
- Week 3 reports
- Employee individual files (plans, daily notes, week notes)
- Department folders
- Existing planning structure

Your output will have two main parts:

===========================================================
PART 1 — Department-Level Weekly Plans (Plan_Week_4.md)
===========================================================

For EACH department:

1. Create a file named: Plan_Week_4.md
2. Inside the file produce a structured weekly plan containing:

### 1. Key Tasks for the Week
List the main tasks that must be executed based on:
- Week 3 progress
- Department priorities
- Long-term goals

### 2. Priorities
Define High / Medium / Low priority items.

### 3. Deadlines and Milestones
Specify concrete deadlines for the week, broken down by day when possible.

### 4. Blockers
Identify:
- unresolved blockers from Week 3
- potential risks for Week 4
- dependencies on other departments

### 5. Control Points (Checkpoints)
Define 3–7 control points for the team lead to review during the week.

### 6. Recommendations for Week 4
Provide actionable suggestions based on Week 3 performance and patterns.

Save this file inside the department folder.

===========================================================
PART 2 — Individual Employee Weekly Plans
===========================================================

For EACH employee in every department:

1. Analyze:
- Their Week 3 summaries
- Daily reports
- Week 3 notes
- Personal goals
- Department context

2. Create an individual weekly plan using the structure:

File name: EmployeeName_Week4_Plan.md

### 1. Personal Goals for the Week
Based on Week 3 performance and department needs.

### 2. Key Tasks Assigned
Summarize all tasks from reports, plans, and summaries.

### 3. Priorities
High / Medium / Low + reasoning.

### 4. Deadlines
Exact dates inside Week 4.

### 5. Blockers & Required Support
List obstacles and specify support needed from team leads.

### 6. Skill Development / Improvements
Based on employee performance from Week 3.

### 7. Daily Checkpoints
Short checklist for each day of the week.

Save each individual file inside the employee’s subfolder.

===========================================================
PART 3 — Multi-Phase Prompt for Automated Weekly Planning
===========================================================

Create a master prompt called:  
“AutoGenerate_Weekly_Plans_Prompt.txt”

This prompt must allow the AI to automatically generate the next week's plan.

The prompt must include:

### A. Task Extraction
Automatically collect:
- Tasks from reports
- Tasks from previous week summaries
- Tasks from employee files

### B. Task Migration Logic
Rules to decide which tasks:
- Move to next week
- Stay in backlog
- Require escalation
- Become reminders

### C. Department-Level Generation
Instructions to generate:
- key priorities
- deadlines
- blockers
- checkpoints
- KPI targets

### D. Individual-Level Generation
Instructions to produce:
- personal task lists
- priorities
- daily plans
- improvements
- reminders from previous week

### E. Reminder Engine
Automatically detect:
- unfinished tasks from Week 3
- incomplete reports
- pending feedback
- overdue blockers

### F. Output Formatting
All output must be in clean Markdown files:
- Plan_Week_X.md (department)
- EmployeeName_WeekX_Plan.md (individual)

===========================================================

IMPORTANT:  
— Maintain consistent formatting  
— Do not mix departments  
— Do not merge files for different employees  
— Use business English  
— Output must be actionable, measurable, and organized  
— Follow all folder naming rules exactly  

After generating everything, save all created prompt files into:

C:\Users\victo\Dropbox\ENTITIES\PROMPTS

