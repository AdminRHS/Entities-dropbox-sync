# PMT-094: Weekly Report Gap Analysis Prompt

**Prompt ID:** PMT-094
**Version:** 1.0
**Created:** 2025-11-21
**Category:** Research Analysis
**Purpose:** Extract knowledge gaps from weekly department reports for research prioritization

---

## Prompt Overview

This prompt guides the Phase 0 analysis process: extracting research needs, improvement opportunities, and knowledge gaps from department daily reports.

**Input:** Last 7 days of department reports from `Dropbox/ENTITIES/REPORTS/`
**Output:** Weekly Gap Analysis document with prioritized research tasks

---

## Analysis Instructions

### Step 1: Report Collection

**Collect reports from:**
- `Dropbox/ENTITIES/REPORTS/2025-[MM]-[DD]/Departments/`
- Last 7 days (or available days)
- All 8 departments:
  1. AI_Department_Report_[date].md
  2. Design_Department_Report_[date].md
  3. Dev_Department_Report_[date].md
  4. Finance_Department_Report_[date].md
  5. HR_Department_Report_[date].md
  6. LG_Department_Report_[date].md
  7. Sales_Department_Report_[date].md
  8. Video_Department_Report_[date].md

---

### Step 2: Extract from Section 8 (Primary Source)

**Section 8: "RESEARCH NEEDED"**

For each department report, extract:

**Format in report:**
```markdown
## 8. RESEARCH NEEDED

### High Priority
- **[Topic]**
  - [Description]
  - [Context/Why needed]
  - Timeline: [timeframe]

### Medium Priority
- **[Topic]**
  ...

### Low Priority
- **[Topic]**
  ...
```

**What to capture:**
- Research topic/title
- Priority level (High/Medium/Low)
- Description/context
- Timeline if specified
- Date of report
- Department

**Scoring:**
- Mentioned in Section 8 = **+3 points** (explicit request)
- Tagged "High Priority" in report = **+3 additional points**
- Tagged "Medium Priority" = **+1 additional point**

---

### Step 3: Extract from Section 9 (Secondary Source)

**Section 9: "IMPROVEMENTS NEEDED"**

For each department report, extract:

**Format in report:**
```markdown
## 9. IMPROVEMENTS NEEDED

### Process Improvements
- [Improvement description]
- Timeline: [timeframe]

### Technical Improvements
- [Improvement description]

### Tool Integrations
- [Tool/integration needed]
```

**What to capture:**
- Improvement topic
- Type (Process/Technical/Tool)
- Description
- Timeline if specified
- Date of report
- Department

**Scoring:**
- Mentioned in Section 9 = **+1 point** (improvement opportunity)
- Blocks current work = **+3 additional points**
- Process automation opportunity = **+1 additional point**

---

### Step 4: Scan Section 6 (Tool Discovery)

**Section 6: "INFRASTRUCTURE AND TECHNICAL ACHIEVEMENTS"**

**What to look for:**
- Tools mentioned by name
- New tools being adopted
- Tool integration projects
- Technology stack mentions

**Action:**
1. List all tools mentioned
2. Check if tool exists in `Dropbox/ENTITIES/LIBRARIES/Tools/`
3. If NOT in LIBRARIES → Flag as "Tool Gap" = **+1 point**

**Examples:**
- "Implemented Cursor for development" → Check if Cursor in LIBRARIES
- "Using Vercel for deployment" → Check if Vercel documented
- "Testing Antigravity IDE" → Check if Antigravity cataloged

---

### Step 5: Scan All Sections (Implicit Gaps)

**Keywords indicating implicit research needs:**

Search all sections for phrases like:
- "Need to research..."
- "Unclear how to..."
- "Blocked by..."
- "Waiting on..."
- "Not sure about..."
- "Should investigate..."
- "Looking into..."
- "Exploring options for..."

**Scoring:**
- Explicit blocker phrase = **+3 points**
- Research intention phrase = **+2 points**
- Exploratory phrase = **+1 point**

**Context clues:**
- If mentioned in Section 3 (Milestone Progress) → Blocks milestone = **+3 points**
- If mentioned in Section 4 (Task Sequences) → Active work item = **+2 points**
- If mentioned in Section 7 (Next Day Plans) → Immediate need = **+2 points**

---

### Step 6: Identify Cross-Department Patterns

**Look for:**
1. **Same tool mentioned by 2+ departments**
   - Example: "Cursor" mentioned by AI, Dev, Design
   - Indicates company-wide interest = **+2 points**

2. **Similar challenges across departments**
   - Example: "Performance optimization" in Dev and AI
   - Indicates systemic issue = **+2 points**

3. **Knowledge sharing opportunities**
   - Department A struggling with X, Department B already solved X
   - Flag for internal knowledge sharing

---

### Step 7: Priority Scoring Matrix

**Calculate total score for each gap:**

| Factor | Points | How to Identify |
|--------|--------|-----------------|
| Explicit in Section 8 | +3 | Mentioned in "Research Needed" |
| High Priority tag | +3 | Tagged "High Priority" in report |
| Blocks current work | +3 | Phrases: "blocked", "prevents", "stuck" |
| Mentioned 2+ times | +2 | Same gap in multiple reports/days |
| Cross-department | +2 | 2+ departments mention same gap |
| Active work item | +2 | Mentioned in current tasks/projects |
| Immediate need | +2 | In "Next Day Plans" or urgent timeline |
| Medium Priority tag | +1 | Tagged "Medium Priority" in report |
| Improvement opportunity | +1 | Mentioned in Section 9 |
| Tool not in LIBRARIES | +1 | Tool mentioned but not cataloged |
| Process automation | +1 | Could save time if automated |

**Priority Levels:**
- **High:** 6+ points (create research task immediately)
- **Medium:** 3-5 points (plan for next 2 weeks)
- **Low:** 1-2 points (backlog, review monthly)

---

### Step 8: Create Research Task Recommendations

**For each HIGH priority gap (6+ points):**

1. **Generate Assignment ID:**
   - Format: `RSH-{DEPT}-###`
   - Department codes: AI, DGN, DEV, FIN, HRM, LGN, SLS, SMM, VID
   - Check `LOGS/RESEARCH_ASSIGNMENT_LOG.md` for last ID used
   - Increment by 1

2. **Estimate Time:**
   - Simple tool research: 1-2 hours
   - Workflow analysis: 2-3 hours
   - Complex gap analysis: 3-4 hours
   - Market research: 3-5 hours

3. **Recommend Assignee:**
   - Check `LOGS/ACTIVE_EMPLOYEES_LIST.md`
   - Match department and skills
   - Prefer "Available" status employees
   - Suggest specific employee name

4. **Write Task Description:**
   - Clear, actionable title
   - Include context from report
   - Specify deliverable format

**Example:**
```markdown
**Gap:** Google Maps Query Optimization
- **Source:** AI Dept Report 2025-11-21, Section 8 (High Priority)
- **Quote:** "Need research on query syntax, filters, and targeting"
- **Score:** 9 points (Explicit +3, High Priority +3, Blocks work +3)
- **Priority:** High
- **Research Task:** RSH-AI-004: Research Google Maps API query optimization techniques
- **Estimated Time:** 2-3 hours
- **Recommended Assignee:** Perederii Vladislav (AI dept, Available status)
- **Deliverable:** Research report with query best practices, filter options, and targeting strategies
```

---

## Output Format

Create file: `Weekly_Gap_Analysis_[YYYY-MM-DD].md`

```markdown
# Weekly Gap Analysis: [Date Range]

**Analysis Date:** [Today's date]
**Report Window:** [Start date] to [End date]
**Reports Analyzed:** [#] reports from [#] departments over [#] days

## Executive Summary

- **Total gaps discovered:** [#]
- **High priority (6+ points):** [#]
- **Medium priority (3-5 points):** [#]
- **Low priority (1-2 points):** [#]
- **Research tasks to create:** [#] (high priority only)
- **Cross-department patterns:** [#]

## Gaps by Department

### AI Department (DPT-001 - AID)

**Reports analyzed:** [# reports from # days]

#### Gap 1: [Gap Title]
- **Source:** AI Dept Report [YYYY-MM-DD], Section [#]
- **Quote:** "[Exact quote from report]"
- **Priority in Report:** [High/Medium/Low if specified]
- **Impact:** [How it affects work/blocks progress]
- **Score Breakdown:**
  - Explicit request (Section 8): +3
  - High priority tag: +3
  - Blocks current work: +3
  - **Total: 9 points**
- **Priority Level:** High
- **Recommended Research Task:**
  - **ID:** RSH-AI-###
  - **Title:** [Research task title]
  - **Description:** [What to research]
  - **Estimated Time:** [hours]
  - **Deliverable:** [What to produce]
  - **Best Assignee:** [Employee name] ([Department], [Status])
  - **Due Date:** [Suggested date based on urgency]

#### Gap 2: [Next gap]
[Same format...]

---

### Design Department (DPT-005 - DGN)
[Same structure for each department]

---

### Development Department (DPT-003 - DEV)
[Same structure...]

---

### Finance Department (DPT-009 - FIN)
[Same structure...]

---

### HR Department (DPT-002 - HRM)
[Same structure...]

---

### Lead Generation Department (DPT-004 - LGN)
[Same structure...]

---

### Sales Department (DPT-007 - SLS)
[Same structure...]

---

### Video Department (DPT-006 - VID)
[Same structure...]

---

## Cross-Department Patterns

### Pattern 1: [Pattern name]
- **Departments affected:** [List departments]
- **Common theme:** [Description]
- **Examples:**
  - [Department A]: [Specific mention]
  - [Department B]: [Specific mention]
- **Recommendation:** [Cross-department research or knowledge sharing]

### Pattern 2: [Next pattern]
[Same format...]

---

## Tools Mentioned (Not in LIBRARIES)

| Tool Name | Mentioned By | Frequency | Sections | Priority |
|-----------|--------------|-----------|----------|----------|
| [Tool] | [Dept(s)] | [# times] | [Sections] | [H/M/L] |

**Action Items:**
- Add to LIBRARIES: [List tools]
- Research further: [List tools needing research]

---

## Research Tasks to Create

**High Priority Tasks (Create This Week):**

| Assignment ID | Department | Task Title | Source | Est. Time | Assignee | Due Date |
|---------------|------------|------------|--------|-----------|----------|----------|
| RSH-AI-### | AI | [Task] | [Report date] | [hours] | [Name] | [Date] |
| RSH-LGN-### | Lead Gen | [Task] | [Report date] | [hours] | [Name] | [Date] |
[...]

**Total high-priority tasks:** [#] tasks, [#] hours total

**Medium Priority Tasks (Plan for Next 2 Weeks):**

| Assignment ID | Department | Task Title | Source | Est. Time |
|---------------|------------|------------|--------|-----------|
| RSH-DEV-### | Development | [Task] | [Report date] | [hours] |
[...]

**Total medium-priority tasks:** [#] tasks, [#] hours total

**Low Priority Tasks (Backlog):**
- [List low-priority items for future consideration]

---

## Implementation Next Steps

### Immediate Actions (This Week)
1. Create [#] high-priority research tasks in `LOGS/RESEARCH_ASSIGNMENT_LOG.md`
2. Update `LOGS/DEPARTMENT_GAP_ANALYSIS.md` with discovered gaps + sources
3. Assign specific tasks:
   - [Task ID] → [Employee name] (due [date])
   - [Task ID] → [Employee name] (due [date])
4. Add [#] tools to `LIBRARIES/Tools/`

### Short-term Actions (Next 2 Weeks)
1. Plan medium-priority research assignments
2. Monitor recurring gaps in next weekly analysis
3. Follow up on high-priority task completion

### Long-term Tracking
1. Archive this analysis to `ANALYSIS_HISTORY/`
2. Compare with next week's analysis to track gap evolution
3. Measure research impact on reported challenges

---

## Analysis Metadata

- **Analysis performed by:** [Your name/role]
- **Time invested:** [minutes/hours]
- **Departments with gaps:** [#]/8
- **Most gaps:** [Department name] ([#] gaps)
- **Fewest gaps:** [Department name] ([#] gaps)
- **Most common gap type:** [Research/Improvement/Tool]

---

*Analysis completed: [YYYY-MM-DD HH:MM]*
*Next analysis scheduled: [Next Monday date]*
```

---

## Quality Checklist

Before finalizing the analysis:

- [ ] Read ALL reports from all available days
- [ ] Extracted Section 8 from every report
- [ ] Extracted Section 9 from every report
- [ ] Scanned Section 6 for tools
- [ ] Searched all sections for blocker keywords
- [ ] Calculated priority scores for all gaps
- [ ] Generated Assignment IDs for high-priority tasks
- [ ] Recommended specific assignees from ACTIVE_EMPLOYEES_LIST
- [ ] Included exact quotes and sources for every gap
- [ ] Identified cross-department patterns
- [ ] Listed tools not in LIBRARIES
- [ ] Created actionable next steps

---

## Tips for Effective Analysis

### Be Thorough
- Don't skip any reports or sections
- Even "low activity" reports can have valuable gaps
- Check every department every time

### Maintain Evidence
- Always include exact quotes
- Always cite source (dept, date, section)
- Link to specific reports when possible

### Think Holistically
- Look for patterns across departments
- Identify knowledge sharing opportunities
- Consider cross-department research that benefits multiple teams

### Stay Objective
- Use the scoring system consistently
- Don't inflate scores based on assumptions
- Let employee-reported urgency guide priorities

### Be Actionable
- Every high-priority gap should become a research task
- Provide specific assignee recommendations
- Include realistic time estimates

---

## Version History

- **v1.0 (2025-11-21):** Initial prompt created
  - Established 7-step analysis process
  - Created priority scoring matrix
  - Defined output format

---

*Use this prompt every Monday to maintain evidence-based research priorities*
