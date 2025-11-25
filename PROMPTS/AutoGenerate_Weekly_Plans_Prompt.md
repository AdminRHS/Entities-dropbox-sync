# MASTER PROMPT: Automatic Weekly Planning Generation System
**Version:** 1.0
**Created:** 2025-11-21
**Purpose:** Automated generation of weekly plans for all departments and employees

---

## OVERVIEW

This prompt enables AI to automatically generate comprehensive weekly planning packages for the next week, including:
1. Department-level weekly plans (Plan_Week_X.md)
2. Individual employee weekly plans (EmployeeName_WeekX_Plan.md)

The system analyzes previous week's performance, ongoing tasks, and strategic priorities to create actionable, measurable plans.

---

## A. TASK EXTRACTION

### 1. Data Sources to Analyze

**For Previous Week Summary:**
- Read all Summary_Week_X.md files from team lead folders in each department
- Location pattern: `C:\Users\victo\Dropbox\[Department Name]\[Team Lead Name]\Summary_Week_X.md`

**For Daily Reports:**
- Read department reports from: `C:\Users\victo\Dropbox\ENTITIES\REPORTS\[Date]\Departments\`
- Read master reports from: `C:\Users\victo\Dropbox\ENTITIES\REPORTS\[Date]\MASTER_REPORT_[Date].md`
- Focus on most recent 2-3 days for current context

**For Employee Individual Files:**
- Read from employee folders: `C:\Users\victo\Dropbox\[Department Name]\[Employee Name]\`
- Check files: daily.md, plans.md, tasks.md, Week_X folders
- Review README.md and Profile files for role context

**For Department Context:**
- Read DEP_README.md and DEPARTMENT_GUIDE.md files
- Check Projects.md and department-level task files
- Review previous week's Plan_Week_X.md if exists

### 2. Task Extraction Logic

**Extract tasks from:**
1. **Completed Tasks section** of previous week summary
   - Identify tasks marked as "in progress" or incomplete
   - Extract blockers preventing completion
   - Note dependencies still pending

2. **In Progress Tasks section**
   - All tasks in this section move to new week
   - Assess completion percentage if documented
   - Identify required support or resources

3. **Blockers section**
   - Convert unresolved blockers to high-priority tasks
   - Identify dependencies on other departments
   - Note required support or escalation

4. **Recommendations section**
   - Convert recommendations to medium-priority tasks
   - Assess which are actionable vs aspirational
   - Prioritize based on impact and feasibility

5. **Issues section**
   - Convert recurring issues to process improvement tasks
   - Identify systemic problems requiring attention
   - Note workarounds that should be formalized

6. **Daily Reports**
   - Extract tasks mentioned as "planned for tomorrow"
   - Note recurring activities that should continue
   - Identify new tasks that emerged during week

---

## B. TASK MIGRATION LOGIC

### 1. Task Categorization Rules

**MOVE TO NEXT WEEK (High Priority) if:**
- Task was "in progress" previous week
- Task has explicit deadline in next week
- Task blocks other work or departments
- Task is critical business function
- Task was repeatedly mentioned across multiple days

**STAY IN BACKLOG (Medium/Low Priority) if:**
- Task is improvement or optimization (not blocking)
- Task is research or exploration
- Task is nice-to-have enhancement
- Task has flexible timeline
- Task is strategic long-term initiative

**REQUIRE ESCALATION (Flag for Management) if:**
- Task blocked for 2+ weeks
- Task requires resources not available
- Task has cross-department dependencies unresolved
- Task has unclear ownership or priority
- Task affects multiple departments

**BECOME REMINDERS (Track but don't schedule) if:**
- Task is waiting on external response
- Task is seasonal or event-driven
- Task is dependent on other task completion
- Task has uncertain timeline

### 2. Priority Assignment Logic

**High Priority:**
- Blockers from previous week
- Tasks with explicit deadlines this week
- Core business functions (daily activities)
- Client deliverables
- Tasks blocking other departments

**Medium Priority:**
- Process improvements
- Documentation and knowledge sharing
- Training and skill development
- Tool optimization
- Cross-department coordination

**Low Priority:**
- Exploratory research
- Long-term strategic initiatives
- Nice-to-have enhancements
- Optional optimizations
- Archive organization

### 3. Task Completion Estimation

For each task, estimate:
- **Time required:** Based on similar tasks from previous weeks
- **Complexity:** Simple (< 2 hours), Medium (2-4 hours), Complex (> 4 hours)
- **Dependencies:** List required inputs or support
- **Deadline:** Specific date within week when applicable

---

## C. DEPARTMENT-LEVEL GENERATION

### 1. Plan_Week_X.md Structure

Use this exact structure for all department-level plans:

```markdown
# [Department Name] - Week X Plan
**Planning Period:** Week X ([Start Date] to [End Date])
**Department:** [Department Name]
**Team Size:** [Number] active members

---

## 1. Key Tasks for the Week

### High Priority Tasks
[List 3-5 high priority tasks with brief descriptions]

### Medium Priority Tasks
[List 3-7 medium priority tasks with brief descriptions]

### Low Priority Tasks
[List 2-5 low priority tasks with brief descriptions]

---

## 2. Priorities

### High Priority
[Explain why these are high priority, business impact]

### Medium Priority
[Explain medium priority rationale]

### Low Priority
[Explain low priority rationale]

---

## 3. Deadlines and Milestones

### Monday, [Date]
[Key tasks and activities for Monday]

### Tuesday, [Date]
[Key tasks and activities for Tuesday]

### Wednesday, [Date]
[Key tasks and activities for Wednesday]

### Thursday, [Date]
[Key tasks and activities for Thursday]

### Friday, [Date]
[Key tasks and activities for Friday]

---

## 4. Blockers

### Unresolved Blockers from Week X-1
[List blockers carried over from previous week]

### Potential Risks for Week X
[List anticipated challenges or risks]

### Dependencies on Other Departments
[List cross-department dependencies]

---

## 5. Control Points (Checkpoints)

[List 5-7 checkpoints throughout the week to verify progress]

---

## 6. Recommendations for Week X

### Immediate Actions
[Actions to take at start of week]

### Process Improvements
[Process optimization opportunities]

### Quality Standards
[Quality and best practice recommendations]

### Knowledge Management
[Documentation and knowledge sharing]

### Team Development
[Skill development and training]

### Strategic Planning
[Long-term strategic considerations]

---

**Plan Status:** Active
**Review Date:** Friday, [End Date]
**Next Planning Cycle:** Week X+1 ([Next week dates])
```

### 2. Department Plan Generation Rules

**Key Tasks Section:**
- Extract from previous week's incomplete tasks, blockers, recommendations
- Prioritize based on business impact, deadlines, dependencies
- Limit high priority to 3-5 tasks (focus, not overwhelm)
- Medium priority 3-7 tasks (important but flexible)
- Low priority 2-5 tasks (if time permits)

**Priorities Section:**
- Explain WHY tasks are prioritized this way
- Connect to business impact, client needs, team goals
- Reference specific context from previous week

**Deadlines Section:**
- Distribute tasks across week logically
- Front-load high-priority items early in week
- Build in buffer for unexpected issues
- Consider dependencies (some tasks must complete before others)

**Blockers Section:**
- Copy unresolved blockers from previous week
- Assess which are still relevant
- Identify new potential risks based on task list
- List cross-department dependencies explicitly

**Control Points:**
- Create 5-7 checkpoints distributed through week
- At least one per day for daily operations departments
- Midweek checkpoint for longer tasks
- End-of-week review checkpoint always included

**Recommendations:**
- Convert previous week recommendations to concrete actions
- Add new recommendations based on patterns observed
- Organize by category (immediate, process, quality, knowledge, team, strategic)

---

## D. INDIVIDUAL-LEVEL GENERATION

### 1. EmployeeName_WeekX_Plan.md Structure

Use this exact structure for all individual employee plans:

```markdown
# Individual Weekly Plan - Week X
**Employee:** [Full Name]
**Department:** [Department Name]
**Position:** [Job Title]
**Planning Period:** Week X ([Start Date] to [End Date])

---

## 1. Personal Goals for the Week

### Professional Development
[3-4 specific professional development goals]

### Team Impact
[2-3 goals related to team contribution]

### Quality & Efficiency
[2-3 goals related to work quality and efficiency]

---

## 2. Key Tasks Assigned

### From Week X-1 Summary - Critical Items
[List high priority tasks from previous week with context]

### From Department Plan
[List tasks assigned from department-level plan]

---

## 3. Priorities

### High Priority
[List and explain high priority tasks]

### Medium Priority
[List and explain medium priority tasks]

### Low Priority
[List and explain low priority tasks]

---

## 4. Deadlines

### Monday, [Date]
[Hour-by-hour or block schedule with specific tasks]

### Tuesday, [Date]
[Hour-by-hour or block schedule with specific tasks]

### Wednesday, [Date]
[Hour-by-hour or block schedule with specific tasks]

### Thursday, [Date]
[Hour-by-hour or block schedule with specific tasks]

### Friday, [Date]
[Hour-by-hour or block schedule with specific tasks]

---

## 5. Blockers & Required Support

### Current Blockers from Week X-1
[List blockers with action items and support needed]

### Anticipated Challenges
[List potential challenges with mitigation and support needed]

---

## 6. Skill Development / Improvements

### Based on Week X-1 Performance

**Strengths to Leverage:**
[List 3-4 strengths demonstrated previous week]

**Areas for Improvement:**
[List 2-3 specific improvement opportunities]

### Skill Development Goals for Week X
[List 3-4 specific, measurable skill development goals]

---

## 7. Daily Checkpoints

### Monday Checklist
[Bulleted checklist of tasks with checkboxes]

### Tuesday Checklist
[Bulleted checklist of tasks with checkboxes]

### Wednesday Checklist
[Bulleted checklist of tasks with checkboxes]

### Thursday Checklist
[Bulleted checklist of tasks with checkboxes]

### Friday Checklist
[Bulleted checklist of tasks with checkboxes]

---

**Plan Status:** Active
**Review Date:** Friday, [End Date] (17:00)
**Success Metrics:**
[3-5 specific, measurable success metrics for the week]
```

### 2. Individual Plan Generation Rules

**Personal Goals:**
- Derive from previous week's performance and areas for improvement
- Align with department goals and priorities
- Make specific, achievable, and relevant to role
- Balance development (learning) with delivery (doing)

**Key Tasks:**
- Start with incomplete tasks from previous week summary
- Add tasks from department plan applicable to this employee
- Consider employee's role, seniority, and capabilities
- Distribute workload realistically (don't overload)

**Priorities:**
- Align with department priorities
- Consider employee's specific blockers and challenges
- Reflect employee's role (leads have more coordination, ICs more execution)

**Deadlines:**
- Create realistic hour-by-hour or time-block schedules
- Consider employee's typical working hours (from reports)
- Build in breaks and buffer time
- Front-load high-priority work

**Blockers & Support:**
- Copy relevant blockers from previous week summary
- Add employee-specific anticipated challenges
- Be specific about required support (who, what, when)
- Include mitigation strategies

**Skill Development:**
- Reference specific achievements from previous week
- Identify concrete improvement areas from summary
- Set measurable skill goals for week
- Connect to career development

**Daily Checkpoints:**
- Create actionable checkbox items
- Specific enough to verify completion
- Distribute tasks logically across days
- Include both tasks and review/planning activities

---

## E. REMINDER ENGINE

### 1. Automatic Reminder Detection

**Scan for and create reminders for:**

**Unfinished Tasks from Previous Week:**
- Tasks marked "in progress" without completion
- Tasks mentioned in multiple daily reports but never completed
- Tasks in recommendations that weren't started

**Incomplete Reports:**
- Employees missing daily logs in previous week
- Departments without complete summaries
- Missing metrics or incomplete sections

**Pending Feedback:**
- Requests for feedback mentioned but not resolved
- Reviews or approvals pending
- Questions asked but not answered

**Overdue Blockers:**
- Blockers that persist 2+ weeks
- Dependencies on other departments unresolved > 1 week
- Resources requested but not received

**Follow-Up Items:**
- "Follow up with X" mentioned but not completed
- Scheduled check-ins or reviews
- Promised deliverables to other teams

### 2. Reminder Formatting

Include reminders in relevant sections of plans:

**In Department Plans:**
- Add to "Immediate Actions" in Recommendations section
- Flag in Blockers section if dependency-related
- Note in Control Points for checking completion

**In Individual Plans:**
- Add to "From Week X-1 Summary" in Key Tasks section
- Include in daily checklists on appropriate days
- Reference in Blockers & Support if applicable

**Reminder Format:**
```
**REMINDER - [Task Name]:** [Brief description of what was supposed to happen]
- **Original Timeline:** [When it should have been done]
- **Status:** [Why it wasn't completed]
- **Action:** [Specific action to complete this week]
- **Owner:** [Who is responsible]
```

---

## F. OUTPUT FORMATTING

### 1. File Naming Conventions

**Department Plans:**
- Format: `Plan_Week_X.md` where X is the week number
- Location: `C:\Users\victo\Dropbox\[Department Name]\Plan_Week_X.md`
- Example: `C:\Users\victo\Dropbox\AI Nov25\Plan_Week_4.md`

**Individual Plans:**
- Format: `[LastName]_[FirstName]_WeekX_Plan.md`
- Location: `C:\Users\victo\Dropbox\[Department Name]\[Employee Name]\[LastName]_[FirstName]_WeekX_Plan.md`
- Example: `C:\Users\victo\Dropbox\AI Nov25\Artemchuk Nikolay\Artemchuk_Nikolay_Week4_Plan.md`

**Department Folder Names:**
- AI Nov25
- Design Nov25
- Dev Nov25
- Finance Nov25
- HR Nov25
- LG Nov25
- Sales Nov25
- Video Nov25

### 2. Markdown Formatting Standards

**Headers:**
- Use # for document title
- Use ## for main sections (1. Key Tasks, 2. Priorities, etc.)
- Use ### for subsections (High Priority, Medium Priority, etc.)
- Use #### sparingly for sub-subsections

**Lists:**
- Use numbered lists for ordered steps or sequential items
- Use bulleted lists for unordered items or checkboxes
- Use checkbox format: `- [ ] Task description`

**Emphasis:**
- Use **bold** for important items, priorities, or emphasis
- Use *italics* sparingly for subtle emphasis
- Use `code formatting` for file paths, technical terms, tool names

**Tables:**
- Use markdown tables for structured data (rare in plans)
- Keep tables simple and readable

**Links:**
- Use absolute file paths, not relative paths
- Format: `C:\Users\victo\Dropbox\...`

### 3. Consistency Requirements

**Dates:**
- Format: "Monday, November 25" or "November 25-29, 2025"
- Always include year for planning period
- Use day of week for daily breakdowns

**Time:**
- Format: "9:00-11:00" for time blocks
- Format: "17:00" for specific times
- Use 24-hour format

**Metrics:**
- Be specific: "15-20 leads" not "some leads"
- Include units: "2 hours" not "2"
- Use ranges when appropriate: "50+ messages"

**Tone:**
- Professional, clear, actionable
- Avoid jargon unless standard to role
- Use active voice: "Complete task" not "Task should be completed"
- Be direct: "Fix bug" not "Consider fixing bug"

---

## G. EXECUTION WORKFLOW

### Step-by-Step Process for Generating Weekly Plans

**STEP 1: Data Collection (30-45 minutes)**
1. Identify the target week number (current week + 1)
2. Read all Summary_Week_X.md files from previous week
3. Read MASTER_REPORT files from previous week's last 2-3 days
4. Read department-level files (DEP_README, Projects, etc.)
5. Scan employee folders for additional context

**STEP 2: Task Extraction (20-30 minutes)**
1. Extract all incomplete tasks from summaries
2. Extract all blockers from summaries
3. Extract recommendations from summaries
4. Extract recurring activities from daily reports
5. Organize tasks by department and employee

**STEP 3: Task Prioritization (15-20 minutes)**
1. Apply task migration logic (move to week, backlog, escalate, remind)
2. Assign priority levels (high, medium, low)
3. Identify dependencies and blockers
4. Estimate time requirements
5. Set deadlines within target week

**STEP 4: Department Plan Generation (10-15 minutes per department)**
1. Create Plan_Week_X.md file in department folder
2. Populate all sections using structure template
3. Distribute tasks across week logically
4. Create meaningful control points
5. Write actionable recommendations
6. Review for completeness and consistency

**STEP 5: Individual Plan Generation (5-10 minutes per employee)**
1. Identify employees with Week X-1 summaries
2. Create [LastName]_[FirstName]_WeekX_Plan.md in employee folder
3. Populate all sections using structure template
4. Align with department plan tasks
5. Create realistic daily schedules
6. Add specific skill development goals
7. Review for completeness and consistency

**STEP 6: Reminder Integration (10-15 minutes)**
1. Scan for unfinished items from previous week
2. Identify follow-up items and pending feedback
3. Flag overdue blockers
4. Insert reminders in appropriate sections
5. Ensure all reminders have clear actions

**STEP 7: Quality Review (15-20 minutes)**
1. Verify all files created with correct naming
2. Check all dates accurate for target week
3. Ensure consistency across department and individual plans
4. Validate task distribution is realistic
5. Confirm all sections populated (no TBDs or blanks)

**STEP 8: Documentation (5-10 minutes)**
1. Create list of all files generated
2. Note any missing data or gaps
3. Flag any items requiring human review
4. Document generation timestamp

---

## H. QUALITY CHECKLIST

### Before finalizing plans, verify:

**Completeness:**
- [ ] All 7 department plans created
- [ ] All employee plans created (for employees with Week X-1 summaries)
- [ ] All sections populated in every plan
- [ ] No placeholder text (TBD, TODO, etc.)

**Accuracy:**
- [ ] Week numbers correct throughout
- [ ] Dates accurate for target week
- [ ] Day of week matches date
- [ ] File naming follows conventions exactly

**Consistency:**
- [ ] Department and individual plans aligned
- [ ] Tasks appear in relevant plans
- [ ] Priorities consistent across plans
- [ ] Formatting consistent across all files

**Actionability:**
- [ ] Tasks specific and measurable
- [ ] Deadlines clear and realistic
- [ ] Support requirements identified
- [ ] Success metrics defined

**Realism:**
- [ ] Workload distributed reasonably
- [ ] Time estimates realistic
- [ ] Dependencies acknowledged
- [ ] Blockers addressed

---

## I. EXAMPLE EXECUTION

### Sample Prompt for Week 5 Generation

```
You are an AI planning assistant. Generate a complete weekly planning package for Week 5 (December 2-6, 2025) for all departments and employees.

Use the following data sources:
- Week 4 summaries from: C:\Users\victo\Dropbox\[Department]\[TeamLead]\Summary_Week_4.md
- Week 4 reports from: C:\Users\victo\Dropbox\ENTITIES\REPORTS\[dates]
- Employee files from: C:\Users\victo\Dropbox\[Department]\[Employee]\

Follow the AutoGenerate_Weekly_Plans_Prompt.txt process:
1. Extract tasks from Week 4 summaries and reports
2. Apply task migration logic to categorize and prioritize
3. Generate department-level Plan_Week_5.md for each department
4. Generate individual WeekX_Plan.md for each employee with Week 4 summary
5. Integrate reminders for unfinished items
6. Format all output according to standards

Deliver:
- 7 department Plan_Week_5.md files
- Individual Week5_Plan.md files for all applicable employees
- Complete file list with paths

Follow all formatting, naming, and structure conventions exactly as specified in the master prompt.
```

---

## J. MAINTENANCE AND UPDATES

### Continuous Improvement

**After each planning cycle:**
1. Review plan accuracy vs actual execution
2. Identify tasks consistently over/under-estimated
3. Refine priority assignment rules
4. Update time estimates based on historical data
5. Improve reminder detection logic

**Monthly:**
1. Analyze task completion rates by priority
2. Review blocker resolution times
3. Assess workload distribution fairness
4. Evaluate skill development goal achievement
5. Update process documentation

**Quarterly:**
1. Major review of task categorization logic
2. Refinement of department-specific needs
3. Role-specific template customizations
4. Integration of new data sources
5. Automation enhancement opportunities

### Version Control

Track changes to this prompt:
- Version number (major.minor)
- Date of change
- What changed and why
- Who approved change
- Impact assessment

---

## K. TROUBLESHOOTING

### Common Issues and Solutions

**Issue: Missing Week X-1 Summary**
- **Solution:** Use daily reports from previous week as fallback
- **Action:** Generate plan based on reports, note data gap

**Issue: Incomplete Employee Data**
- **Solution:** Generate plan from department-level tasks only
- **Action:** Mark plan as "partial data" and recommend employee update

**Issue: Conflicting Priorities**
- **Solution:** Default to department plan priority
- **Action:** Flag conflict for human review

**Issue: Unrealistic Workload**
- **Solution:** Apply capacity constraint (8 hours/day max)
- **Action:** Move lower priority tasks to backlog

**Issue: Circular Dependencies**
- **Solution:** Break dependency chain, prioritize blocker resolution
- **Action:** Escalate to management in plan

**Issue: Outdated Department Structure**
- **Solution:** Use most recent organizational data available
- **Action:** Flag for verification in plan

---

**END OF MASTER PROMPT**

This prompt should be used as the definitive guide for automated weekly planning generation. All generated plans must follow these specifications exactly to ensure consistency, completeness, and actionability.

**Last Updated:** 2025-11-21
**Next Review:** 2025-12-21
**Maintained By:** AI Planning System
