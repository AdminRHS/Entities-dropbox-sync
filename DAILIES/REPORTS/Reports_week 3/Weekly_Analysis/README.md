# Phase 0: Weekly Report Gap Analysis

**Created:** 2025-11-21
**Location:** `ENTITIES/TASK_MANAGERS/REPORTS/Weekly_Analysis/`
**Purpose:** Analyze weekly daily reports to discover department knowledge gaps and research priorities

---

## Overview

Phase 0 is the **initial phase** in the research workflow that runs BEFORE assigning research tasks. It analyzes the previous week's daily department reports to identify:

- Explicit research needs (from report Section 8: "RESEARCH NEEDED")
- Improvement opportunities (from report Section 9: "IMPROVEMENTS NEEDED")
- Tool gaps (tools mentioned but not in LIBRARIES)
- Process gaps (workflows mentioned but not documented)
- Cross-department knowledge sharing opportunities

**Key Principle:** Research priorities should be evidence-based, derived from actual employee challenges and needs documented in daily reports.

---

## Weekly Schedule

**Run Phase 0 Analysis:** Every Monday morning (or Friday afternoon)

**Analysis Window:** Previous 7 days of department reports

**Example:**
- Analysis Date: Monday, November 25, 2025
- Report Window: November 18-24, 2025
- Output: `Weekly_Gap_Analysis_2025-11-25.md`

---

## Phase 0 Workflow

### Step 1: Collect Reports (5 minutes)

**Location:** `Dropbox/ENTITIES/REPORTS/`

**Collect:**
- Last 7 days of department reports
- Focus on these folders: `2025-11-19/`, `2025-11-20/`, `2025-11-21/`, etc.
- Include all 8 departments:
  - AI_Department_Report_[date].md
  - Design_Department_Report_[date].md
  - Dev_Department_Report_[date].md
  - Finance_Department_Report_[date].md
  - HR_Department_Report_[date].md
  - LG_Department_Report_[date].md
  - Sales_Department_Report_[date].md
  - Video_Department_Report_[date].md

---

### Step 2: Run Gap Analysis (30-45 minutes)

**Use Prompt:** `PMT-XXX_Weekly_Report_Gap_Analysis.md`

**Process:**
1. Read all department reports from last 7 days
2. Extract Section 8 (RESEARCH NEEDED) from each report
3. Extract Section 9 (IMPROVEMENTS NEEDED) from each report
4. Scan Section 6 (INFRASTRUCTURE) for tool mentions
5. Review challenges and blockers in all sections
6. Identify cross-department patterns

**Output:** `Weekly_Gap_Analysis_[date].md`

---

### Step 3: Prioritize Gaps (15 minutes)

**Scoring System:**

| Factor | Weight | Scoring |
|--------|--------|---------|
| Explicitly Requested | 3x | Mentioned in Section 8 "Research Needed" |
| Blocks Current Work | 3x | Prevents progress on active projects |
| Mentioned Multiple Times | 2x | Appears in 2+ reports or 2+ days |
| Cross-Department Impact | 2x | Affects multiple departments |
| Improvement Opportunity | 1x | Mentioned in Section 9 "Improvements Needed" |
| Tool/Process Gap | 1x | Tool mentioned but not in LIBRARIES |

**Priority Levels:**
- **High:** Score 6+ or blocks current work
- **Medium:** Score 3-5
- **Low:** Score 1-2

---

### Step 4: Update Research Logs (15 minutes)

**Update Files:**

1. **LOGS/DEPARTMENT_GAP_ANALYSIS.md**
   - Add newly discovered gaps
   - Add source citation: "Source: Weekly Report Analysis 2025-11-21"
   - Link to specific report: "Mentioned in AI Dept Report 2025-11-21, Section 8"

2. **LOGS/RESEARCH_ASSIGNMENT_LOG.md**
   - Create research tasks for high-priority gaps
   - Generate Assignment IDs: RSH-{DEPT}-###
   - Status: Pending
   - Source: Link to weekly analysis

---

### Step 5: Archive Analysis (5 minutes)

**Move completed analysis to:**
`ANALYSIS_HISTORY/Weekly_Gap_Analysis_[date].md`

**Purpose:** Track gap evolution over time

---

## Report Structure Reference

### Standard Daily Report Sections

From your daily report schema (10-section format):

**Section 1: EXECUTIVE SUMMARY**
- Key metrics overview
- Quick reference for time allocation

**Section 2: PROJECT CONTRIBUTIONS**
- Active projects and progress
- Which projects are mentioned repeatedly?

**Section 3: MILESTONE PROGRESS**
- Sprint/project milestones
- Blockers preventing milestone completion

**Section 4: TASK SEQUENCES AND ENTITY MAPPING**
- Detailed activities
- **SCAN FOR:** Workflows, processes, tools used

**Section 5: CROSS-DEPARTMENT COORDINATION**
- Incoming/outgoing requests
- **SCAN FOR:** Knowledge sharing opportunities

**Section 6: INFRASTRUCTURE AND TECHNICAL ACHIEVEMENTS**
- Systems/tools/process improvements
- **SCAN FOR:** Tools mentioned but not in LIBRARIES

**Section 7: NEXT DAY PLANS**
- Tomorrow's scheduled activities
- **SCAN FOR:** Upcoming needs, planned research

**Section 8: RESEARCH NEEDED** ⭐
- **PRIMARY SOURCE** for explicit research gaps
- Already prioritized by employees
- Often includes High/Medium/Low tags

**Section 9: IMPROVEMENTS NEEDED** ⭐
- **SECONDARY SOURCE** for process/technical gaps
- Process automation opportunities
- Tool integration needs

**Section 10: METRICS AND DELIVERABLES**
- Quantified results
- **SCAN FOR:** Performance gaps, efficiency issues

---

## Example: Extracting Gaps

### From AI Department Report (2025-11-21)

**Section 8: RESEARCH NEEDED**
```markdown
## 8. RESEARCH NEEDED

### High Priority
- **Google Maps search query optimization**
  - Current queries return low-quality leads
  - Need research on query syntax, filters, and targeting
  - Timeline: This week

### Medium Priority
- **Review sentiment analysis accuracy**
  - Validate sentiment detection algorithms
  - Compare tools/approaches
  - Timeline: Next 2 weeks
```

**Phase 0 Output:**
```markdown
### AI Department Gaps Discovered

1. **Gap:** Google Maps Search Query Optimization
   - **Source:** AI Dept Report 2025-11-21, Section 8 (High Priority)
   - **Impact:** Blocking current lead generation project
   - **Priority Score:** 9 (Explicit request 3x + Blocks work 3x + Current project 3x)
   - **Priority Level:** High
   - **Research Task:** RSH-AI-004: Research Google Maps API query optimization
   - **Estimated Time:** 2-3 hours
   - **Assignee:** Perederii Vladislav (AI, Available)

2. **Gap:** Review Sentiment Analysis Validation
   - **Source:** AI Dept Report 2025-11-21, Section 8 (Medium Priority)
   - **Impact:** Quality assurance for current system
   - **Priority Score:** 4 (Explicit request 3x + Improvement 1x)
   - **Priority Level:** Medium
   - **Research Task:** RSH-AI-005: Research sentiment analysis accuracy validation
   - **Estimated Time:** 2 hours
   - **Assignee:** TBD (defer to future week)
```

---

## Output Files

### Weekly_Gap_Analysis_[date].md Structure

```markdown
# Weekly Gap Analysis: [Date Range]

**Analysis Date:** [Monday date]
**Report Window:** [Start date] to [End date]
**Reports Analyzed:** [Number] reports from [Number] departments

## Executive Summary
- Total gaps discovered: [X]
- High priority: [X]
- Medium priority: [X]
- Low priority: [X]
- Research tasks created: [X]

## Gaps by Department

### AI Department
[Extracted gaps with sources and priorities]

### Design Department
[Extracted gaps with sources and priorities]

[...etc for all 8 departments]

## Cross-Department Patterns
[Tools/processes mentioned by multiple departments]

## Research Tasks Created
[List of RSH-XXX-### tasks generated]

## Next Steps
[Recommended assignments for upcoming week]
```

---

## Integration with Research System

### Phase 0 Feeds Into:

1. **LOGS/DEPARTMENT_GAP_ANALYSIS.md**
   - Updates with real employee-reported gaps
   - Adds evidence and citations
   - Tracks "Last Mentioned" dates

2. **LOGS/RESEARCH_ASSIGNMENT_LOG.md**
   - Populates with high-priority research tasks
   - Links to source reports
   - Ready for employee assignment

3. **LOGS/WEEKLY_RESEARCH_PLAN.md**
   - Informs weekly research priorities
   - Evidence-based planning

4. **LOGS/ACTIVE_EMPLOYEES_LIST.md**
   - Cross-reference: Which employees mentioned gaps?
   - Assign research to employees who reported the need

---

## Benefits of Phase 0

### Evidence-Based Research
- Research driven by actual employee needs
- Not guesswork or assumptions
- Direct link to business impact

### Automatic Discovery
- No manual brainstorming required
- Gaps surface naturally from daily work
- Real-time tracking of knowledge needs

### Priority Validation
- Employees themselves indicate urgency
- Blockers are clearly identified
- Time-sensitive needs are visible

### Accountability
- Clear source for every research task
- Can trace back to original request
- Employees see their needs addressed

### Evolution Tracking
- Archive shows how gaps change over time
- Identify recurring vs. one-time needs
- Measure research impact on gaps

---

## Weekly Checklist

**Every Monday (or Friday):**

- [ ] Collect last 7 days of department reports from `Dropbox/ENTITIES/REPORTS/`
- [ ] Run PMT-XXX_Weekly_Report_Gap_Analysis prompt
- [ ] Generate Weekly_Gap_Analysis_[date].md
- [ ] Score and prioritize discovered gaps (High/Medium/Low)
- [ ] Update LOGS/DEPARTMENT_GAP_ANALYSIS.md with new gaps + sources
- [ ] Create research tasks in LOGS/RESEARCH_ASSIGNMENT_LOG.md
- [ ] Archive analysis to ANALYSIS_HISTORY/
- [ ] Share findings with department leads (optional)

**Time Required:** 60-90 minutes per week

---

## Files in This Folder

- **README.md** (this file) - Phase 0 process documentation
- **PMT-XXX_Weekly_Report_Gap_Analysis.md** - Analysis prompt/template
- **Weekly_Gap_Analysis_[date].md** - Current week's analysis (moves to archive after review)
- **ANALYSIS_HISTORY/** - Archive of past weekly analyses

---

## Related Documentation

- [Department Gap Analysis](../LOGS/DEPARTMENT_GAP_ANALYSIS.md) - Master gap tracker
- [Research Assignment Log](../LOGS/RESEARCH_ASSIGNMENT_LOG.md) - Active research tasks
- [Weekly Research Plan](../LOGS/WEEKLY_RESEARCH_PLAN.md) - Weekly priorities
- [Daily Reports](../../REPORTS/) - Source data for analysis

---

*Run Phase 0 every Monday to keep research priorities aligned with actual employee needs*
