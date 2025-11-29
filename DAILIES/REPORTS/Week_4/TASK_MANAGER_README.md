# Week 4 Task Manager - Implementation Guide

**Created:** November 28, 2025
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\`

---

## What Was Built

A dedicated **Week 4 Task Manager system** based on comprehensive extractions from:

1. **Week 4 Reports Folder** - Contains all department reports, employee summaries, and status tracking
2. **Taxonomy Task Managers** - 71 TST task templates, 9 PRT project templates, 20 WRF workflows

---

## Core Components

### 1. Main Prompt File
**File:** [WEEK4_TASK_MANAGER_PROMPT.md](WEEK4_TASK_MANAGER_PROMPT.md)

**Size:** ~30KB comprehensive system prompt

**Purpose:**
- AI assistant configuration for Week 4 task management
- Complete context about departments, employees, and available data
- Task extraction and classification protocols
- Cross-department coordination guidelines

**Key Features:**
- ✅ 6 core functions (extraction, coordination, tracking, priority, workflow, reporting)
- ✅ Complete employee roster (20 active employees with data)
- ✅ 71 task templates (TST-###) from taxonomy system
- ✅ 8 department structures (3 complete, 5 pending)
- ✅ Usage scenarios with example interactions
- ✅ Critical issues tracking (compliance, coverage gaps)
- ✅ Success criteria and metrics

---

## Data Sources Integrated

### Completed Department Reports (3)
1. **Finance (FIN)** - 16 tasks extracted, 2 employees
   - Source: `FIN_Department_Nov24-25_Report.md` (44KB)
   - Coverage: Nov 24-25, 2025

2. **HR (HRM)** - 22 tasks, 77 steps, 3 employees
   - Source: `HRM_Department_Nov24-25_Report.md` (90KB)
   - High performer: 85% task detection accuracy

3. **Design (DGN)** - 50+ deliverables, 5 active employees
   - Source: `DGN_Department_Nov24-25_Report.md` (27KB)
   - Includes: 50+ LinkedIn posts, 16 AI-generated items, 5 videos

### Pending Department Reports (5)
4. **Development (DEV)** - 11 daily.md files from 7 developers
5. **AI & Automation (AID)** - Multiple dailies + special processing report
6. **Lead Generation (LGN)** - 20+ employee dailies
7. **Sales (SLS)** - 6+ employee dailies
8. **Video (VID)** - 2 employees with Nov 24-25 data

### Individual Employee Reports
- **Developers folder:** 9 summaries (Artem Skichko, Azar Imranov, Danylenko Liliia, etc.)
- **Managers folder:** 34 summaries (Lead Gen, HR, Sales managers)
- **Designers folder:** (To be processed)
- **Executives folder:** (Executive-level reports)

### Taxonomy System
**Source:** `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`

**Integrated Resources:**
- 71 Task Templates (TST-001 through TST-071)
- 9 Project Templates (PRT-001 through PRT-009)
- 28 Milestone Templates (MLT-001 through MLT-028)
- 20 Workflow Templates (WRF-001 through WRF-020)
- 8 Guides (GDS-001 through GDS-008)

---

## How to Use

### Step 1: Load the Prompt
```
Load WEEK4_TASK_MANAGER_PROMPT.md into your AI assistant
This provides complete context for Week 4 operations
```

### Step 2: Query Tasks
**Examples:**
- "Show me all tasks for Yelisieieva Daria on November 24"
- "What department reports still need creation?"
- "List all Lead Generation tasks from Week 4"
- "What's the priority for AI & Automation team tomorrow?"

### Step 3: Extract Tasks
```
Process employee daily.md files:
- Parse Nov25/[Department]/[Employee]/Week_4/{24,25}/daily.md
- Extract concrete actions and deliverables
- Classify using TST-### taxonomy codes
- Assign proper department codes
```

### Step 4: Generate Reports
**Available Report Types:**
- Department summary status
- Employee productivity metrics
- Task completion rates
- Cross-department dependencies
- Compliance tracking

### Step 5: Plan & Prioritize
```
Use built-in priority framework:
1. Critical: Client deliverables, system outages, compliance
2. High: Department reports, onboarding, automation fixes
3. Medium: Process improvements, documentation
4. Low: Long-term planning, optimization
```

---

## Task Taxonomy Quick Reference

### By Department

**Lead Generation (LGN) - 13 tasks:**
- TST-001: AI-Powered HTML Parsing
- TST-002: Airscale Employee Enrichment
- TST-014: Google SERP Lead Generation
- TST-018: LinkedIn Sales Navigator Lead Extraction
- [See full list in prompt]

**HR (HRM) - 6 tasks:**
- TST-007: Create Job Posting Template
- TST-039: Setup n8n for CV Screening
- TST-041: Build Notion ATS Database
- TST-042: Setup Interview Scheduling
- TST-044: Setup Onboarding Workflow

**Development (DEV) - 6 tasks:**
- TST-008: Create MCP Connector
- TST-010: Deploy MCP Connector Locally
- TST-059: Install MCP Server VS Code
- TST-061: Generate Project Instructions Copilot

**AI & Automation (AIA) - 30+ tasks:**
- TST-005: Automate Morning Email Drafting
- TST-023-038: System Analysis Tasks
- TST-052-056: Taxonomy Tasks
- TST-062-067: Advanced AI Tasks

**Video (VID) - 5 tasks:**
- TST-045: Research AI Video Tools
- TST-049: Perform Initial Video Analysis
- TST-057: Transcribe Video

**Design (DSN) - 2 tasks:**
- TST-064: Setup Company Voice Guide
- TST-068: Behance Step 01 Select and Prepare Project

**Sales (SAL) - 1 task:**
- TST-021: Send Old Client Email Template

---

## Key Metrics Tracked

### Department Coverage
- Total Departments: **8**
- Summaries Complete: **3** (37.5%)
- Summaries Needed: **5** (62.5%)
- Target: 100% completion

### Employee Participation
- Employees with Nov 24 dailies: **50+**
- Employees with Nov 25 dailies: **10-15** (sparse)
- Active employees with data: **20 confirmed**
- "Project" employees with empty logs: **16** (needs follow-up)

### Task Extraction Progress
- Finance: **16 tasks** extracted
- HR: **22 tasks, 77 steps** extracted
- Design: **50+ deliverables** documented
- Pending: ~**200+ tasks** from 60+ daily files

### Quality Benchmarks
- Task Detection Accuracy: **85%** (HR benchmark)
- Employee Coverage: Nov 24 (good), Nov 25 (needs improvement)
- Compliance: **1 critical issue** (Finance - Kateryna)

---

## Critical Issues Being Tracked

### 🚨 CRITICAL
**Finance Compliance Gap**
- Employee: Ponomarova Kateryna
- Issue: Empty daily.md files for 5 consecutive days
- Impact: Missing audit trail, financial records gap
- Action: Management escalation required

### ⚠️ HIGH
**Sparse Nov 25 Coverage**
- Issue: Only 10-15 employees submitted Nov 25 dailies (vs 50+ for Nov 24)
- Impact: Incomplete week coverage
- Action: Employee follow-up, investigate submission issues

### ⚠️ MEDIUM
**Pending Department Summaries**
- Status: 5 of 8 departments need summary creation
- Impact: Cannot extract 200+ tasks from 60+ daily files
- Action: Process DEV, AID, LGN, SLS, VID ASAP

### ⚠️ MEDIUM
**"Project" Status Employees Not Logging**
- Count: 16 employees with template-only files
- Impact: Cannot track project work
- Action: Clarify logging requirements

---

## Example Use Cases

### Use Case 1: Daily Standup Prep
**Goal:** Understand what each team member accomplished yesterday

**Query:**
```
"Show me all completed tasks for the Development team on November 24"
```

**Output:** List of tasks with employees, completion status, time spent

---

### Use Case 2: Weekly Planning
**Goal:** Plan next week's priorities based on Week 4 progress

**Query:**
```
"What tasks are incomplete from Week 4 that should roll to Week 5?"
```

**Output:** Incomplete tasks with dependencies, blockers, recommended priorities

---

### Use Case 3: Resource Allocation
**Goal:** Identify which department needs support

**Query:**
```
"Which department has the most pending tasks and fewest resources?"
```

**Output:** Department workload analysis with recommendations

---

### Use Case 4: Compliance Audit
**Goal:** Verify all employees submitted required daily reports

**Query:**
```
"Show me all employees with missing or incomplete daily.md files for Week 4"
```

**Output:** Compliance report with gaps highlighted

---

### Use Case 5: Cross-Team Dependencies
**Goal:** Coordinate work between Design and Video teams

**Query:**
```
"Show me all tasks that involve both Design and Video teams"
```

**Output:** Collaborative tasks with handoff status, blockers, next steps

---

## File Structure

```
ENTITIES/DAILIES/REPORTS/Week_4/
├── WEEK4_TASK_MANAGER_PROMPT.md          ⭐ Main prompt file (this is what you load)
├── TASK_MANAGER_README.md                📖 This guide
├── WEEK4_SUMMARY_STATUS.md               📊 Overall status report
├── Processing_Status_Report_20251128.md  📋 Processing details
│
├── Department Reports/
│   ├── FIN_Department_Nov24-25_Report.md   ✅ Complete (44KB)
│   ├── HRM_Department_Nov24-25_Report.md   ✅ Complete (90KB)
│   ├── DGN_Department_Nov24-25_Report.md   ✅ Complete (27KB)
│   ├── DEV_Department_Nov24-25_Report.md   🔄 Pending
│   ├── AID_Department_Nov24-25_Report.md   🔄 Pending
│   ├── LGN_Department_Nov24-25_Report.md   🔄 Pending
│   ├── SLS_Department_Nov24-25_Report.md   🔄 Pending
│   └── VID_Department_Nov24-25_Report.md   🔄 Pending
│
├── Individual Summaries/
│   ├── developers/
│   │   ├── Artem_Skichko_Employee_Summary_Week4.md
│   │   ├── Danylenko_Liliia_Employee_Summary_Week4.md
│   │   └── [9 total developer summaries]
│   ├── managers/
│   │   ├── Burda_Anna_Employee_Summary_Week4.md
│   │   ├── Nealova_Evgeniya_Employee_Summary_Week4.md
│   │   └── [34 total manager summaries]
│   ├── designers/ (to be processed)
│   ├── marketers/ (to be processed)
│   ├── videographers/ (to be processed)
│   └── Executives/ (to be processed)
│
├── Planning Documents/
│   ├── [Employee]_Week4_Plan.md          (individual planning for Week 5)
│   └── TODO.md files (folder 28)
│
└── Special Reports/
    └── Strapi_VSCode_Integration_Research.md
```

---

## Success Criteria

You'll know the system is working when you can:

1. ✅ Instantly locate any employee's Week 4 tasks
2. ✅ Extract and classify tasks using TST-### codes
3. ✅ Generate reports matching MAIN_PROMPT v7.1 standards
4. ✅ Identify cross-department dependencies
5. ✅ Prioritize work based on strategic value
6. ✅ Track completion with accurate metrics
7. ✅ Surface insights about patterns and bottlenecks
8. ✅ Maintain taxonomy consistency
9. ✅ Flag compliance and data quality issues
10. ✅ Support Week 5 planning with data-driven recommendations

---

## Next Steps

### Immediate Actions (Today)
1. ✅ Load WEEK4_TASK_MANAGER_PROMPT.md into AI assistant
2. 🔄 Create remaining 5 department summaries (DEV, AID, LGN, SLS, VID)
3. 🔄 Extract all tasks from completed reports
4. 🔄 Address Finance compliance issue (Kateryna)

### Short-term (This Week)
5. Process all 60+ daily.md files
6. Create Employee_Summary_Week4.md for all active employees
7. Build consolidated task database
8. Document lessons learned

### Medium-term (Next Week)
9. Implement automated task extraction
10. Create real-time status dashboard
11. Perform taxonomy gap analysis
12. Establish cross-department collaboration workflows

---

## Support & Documentation

**Primary Documentation:**
- Main Prompt: [WEEK4_TASK_MANAGER_PROMPT.md](WEEK4_TASK_MANAGER_PROMPT.md)
- Status Report: [WEEK4_SUMMARY_STATUS.md](WEEK4_SUMMARY_STATUS.md)
- Taxonomy Reference: `../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`

**Framework:**
- MAIN_PROMPT v7.1 (task-first extraction, bottom-up classification)

**Related Systems:**
- Employee Daily Reports (daily.md files in Nov25 folder)
- Department Report Templates (PMT-036, PMT-038, etc.)
- Taxonomy System (TAX-002)

---

## Version History

**v1.0 - November 28, 2025**
- Initial creation
- Integrated 3 completed department reports
- Mapped 5 pending departments
- Documented 20 active employees
- Referenced 71 task templates
- Identified 5 critical issues

---

**Questions or Issues?**
Refer to the main prompt file for detailed examples and interaction guidelines.

**Last Updated:** November 28, 2025
