# Department Reports → Research Task Creation Integration Plan
**Plan Date:** 2025-11-23
**Plan Type:** System Integration
**Related System:** Research System Activation (Phase 1 Complete)
**Integration Target:** TASK_MANAGERS + RESEARCHES

---

## Executive Summary

This plan establishes the formal integration between **department daily reports** (Section 8 & 9) and the **Research System's weekly cycle**, creating standardized task creation workflows in TASK_MANAGERS.

**Key Outcome:** Department-reported research needs automatically flow into Monday Phase 0 analysis → Research assignments → LIBRARIES integration

**Files to Create:** 8 new files (3 YAML specs, 4 JSON templates, 1 YAML workflow)
**Estimated Time:** 3-4 hours
**Implementation Phase:** Phase 2 of Research System Activation

---

## 1. Current State Analysis

### What Already Exists ✅

**Research System Infrastructure (Phase 1 Complete)**
- `REPORTS/Weekly_Analysis/` - Monday engine with Phase_0_Template.md
- `RESEARCH_ASSIGNMENT_LOG.md` - RSH-{VIDEO#}-{PHASE#} tracking
- `Research_System_Weekly_Cycle_Workflow.yaml` - Complete 8-step workflow in TASK_MANAGERS
- `PMT-094_Weekly_Report_Gap_Analysis.md` - Prompt for extracting gaps from reports
- Quality review process (100-point rubric → 0-10 scale)
- LIBRARIES integration process with cross-referencing

**Department Reports Infrastructure**
- 8 departments submit daily reports to `REPORTS/[YYYY-MM-DD]/Departments/`
- 10-section standardized format
- **Section 8: RESEARCH NEEDED** - Explicit research requests
- **Section 9: IMPROVEMENTS NEEDED** - Process/tool improvements
- Reports accumulate daily Monday-Friday

**TASK_MANAGERS Structure**
- `TSM-006_Workflows/` - 26+ workflow YAML files
- `TSM-003_Task_Templates/` - 22 task templates (JSON)
- `TSM-007_GUIDES/` - Process documentation

### What's Missing ❌

**No Formal Input Specifications**
- Phase 0 analysis has no documented input spec in TASK_MANAGERS
- No template for "what data to extract from department reports"
- No standardized format for research task creation inputs

**No Task Templates for Research Activities**
- Phase 0 weekly analysis is manual (no task template)
- Department report review has no task template
- Research assignment creation is manual
- Quality review process has no task template

**No Automated Gap Extraction Workflow**
- PMT-094 prompt exists but not wrapped in workflow
- No automated trigger from report publishing → gap extraction
- Manual process to scan Section 8 & 9 across all departments

---

## 2. Integration Architecture

### The Complete Flow

```
┌─────────────────────────────────────────────────────────────┐
│ DAILY (Monday-Friday)                                       │
├─────────────────────────────────────────────────────────────┤
│ Employees → Daily Department Reports                        │
│   ↓                                                          │
│ Section 8: RESEARCH NEEDED (explicit requests)              │
│ Section 9: IMPROVEMENTS NEEDED (opportunities)              │
│ Section 6: INFRASTRUCTURE (tools not in LIBRARIES)          │
│   ↓                                                          │
│ REPORTS/[YYYY-MM-DD]/Departments/[Dept]_Report.md          │
│   ↓                                                          │
│ [Accumulates for 7 days]                                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ MONDAY 9:00-10:30 AM (THE ENGINE)                           │
├─────────────────────────────────────────────────────────────┤
│ Research Manager executes Phase 0 Analysis                  │
│   ↓                                                          │
│ INPUT (from TASK_MANAGERS/TSM-006_Workflows/INPUTS/)       │
│ ├── Last 7 days reports (all 8 departments)                │
│ ├── DEPARTMENT_GAP_ANALYSIS.md (existing gaps)             │
│ ├── ACTIVE_EMPLOYEES_LIST.md (16 employees)                │
│ └── RESEARCH_COMPLETION_TRACKER.md (last week data)        │
│   ↓                                                          │
│ PROCESS (PMT-094 + Gap Extraction Workflow)                │
│ ├── Extract Section 8 (explicit research)                  │
│ ├── Extract Section 9 (improvements)                       │
│ ├── Score gaps: (Urgency × 3) + (Impact × 2)              │
│ ├── Match employees to gaps                                │
│ └── Generate 2-4 research task recommendations             │
│   ↓                                                          │
│ OUTPUT (to REPORTS/Weekly_Analysis/)         │
│ └── November_2025_Week_3_Analysis.md                       │
│     ├── Gaps discovered (High/Medium/Low)                  │
│     ├── Research task recommendations (RSH-XXX-XX)         │
│     ├── Employee assignments                               │
│     └── Weekly goals                                       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ TUESDAY (Assignment Creation)                               │
├─────────────────────────────────────────────────────────────┤
│ RESEARCH_ASSIGNMENT_LOG.md updated:                         │
│ ├── RSH-006-05 → Davlatmamadova Firuza (due Nov 26)       │
│ └── RSH-008-05 → Perederii Vladislav (due Nov 26)         │
│   ↓                                                          │
│ Employees notified (24/ folder or Discord/Email)            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ TUESDAY-MONDAY (Research Execution + Review)                │
├─────────────────────────────────────────────────────────────┤
│ Employees research → Submit deliverables                    │
│   ↓                                                          │
│ Quality review (0-10 scale, 5.0+ to approve)               │
│   ↓                                                          │
│ LIBRARIES integration (Tools/, Workflows/)                  │
│   ↓                                                          │
│ Gap closure in DEPARTMENT_GAP_ANALYSIS.md                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ NEXT MONDAY (Cycle Repeats WITH DATA)                       │
├─────────────────────────────────────────────────────────────┤
│ Phase 0 runs again with:                                    │
│ ├── Last week's completion data                            │
│ ├── Quality scores                                         │
│ ├── LIBRARIES growth metrics                               │
│ └── Week-over-week comparison                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Priority Scoring System

### Research Trigger Types and Points

| Trigger Type | Points | Example from Reports |
|-------------|--------|---------------------|
| **Explicit in Section 8** | +3 | "RESEARCH NEEDED: Google Maps search optimization" |
| **High Priority tag** | +3 | "Priority: High - blocking current work" |
| **Blocks current work** | +3 | "Prevents progress on lead generation tasks" |
| **Mentioned 2+ times** | +2 | Same gap in multiple reports/days |
| **Cross-department** | +2 | AI + Lead Gen both need same research |
| **Medium Priority tag** | +1 | "Priority: Medium - quality assurance" |
| **Improvement opportunity** | +1 | Section 9 process improvement |
| **Tool not in LIBRARIES** | +1 | Section 6 tool mentioned but not cataloged |

### Priority Scoring Formula

**Priority Score = (Urgency × 3) + (Impact × 2)**

**Urgency (1-10):**
- 10 = Needed THIS WEEK (blocking work)
- 7-9 = Needed soon (next 2-3 weeks)
- 4-6 = Important but can wait
- 1-3 = Nice to have

**Impact (1-10):**
- 10 = Affects 10+ employees or critical business function
- 7-9 = Affects 5-9 employees or important function
- 4-6 = Affects 2-4 employees or secondary function
- 1-3 = Affects 1 employee or minor function

**Priority Levels:**
- **High (6+ points):** Create research task immediately (this week)
- **Medium (3-5 points):** Plan for next 2 weeks
- **Low (1-2 points):** Backlog, review monthly

---

## 4. Files to Create

### 4.1 TASK_MANAGERS Input Specifications (3 files)

#### File 1: `TASK_MANAGERS/TSM-006_Workflows/INPUTS/Phase_0_Analysis_Input_Spec.yaml`

**Purpose:** Defines what data Phase 0 weekly analysis needs and where to get it

**Content Structure:**
```yaml
input_spec_name: "Phase 0 Weekly Analysis Input Specification"
input_spec_id: "INPUT-SPEC-RSH-001"
workflow_reference: "WF-SEQ-RSH-001" # Research_System_Weekly_Cycle_Workflow
step_number: 1 # Phase 0: Weekly Analysis (MONDAY - THE ENGINE)

data_sources:
  - source_name: "Department Daily Reports (Last 7 Days)"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\REPORTS\\[YYYY-MM-DD]\\Departments\\"
    file_pattern: "*_Department_Report_*.md"
    departments:
      - AI
      - Lead_Generation
      - Development
      - Marketing
      - Operations
      - Finance
      - HR
      - Sales
    sections_to_extract:
      - section_8: "RESEARCH NEEDED"
      - section_9: "IMPROVEMENTS NEEDED"
      - section_6: "INFRASTRUCTURE" # Tools not in LIBRARIES
      - section_3: "MILESTONE PROGRESS" # Blockers
    date_range:
      calculation: "today - 7 days to today - 1 day"
      example: "2025-11-14 to 2025-11-20"

  - source_name: "Department Gap Analysis"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\DEPARTMENT_GAP_ANALYSIS.md"
    purpose: "Existing gaps to track (avoid duplicates)"
    format: "Markdown table with gap IDs, descriptions, status"

  - source_name: "Active Employees List"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\ACTIVE_EMPLOYEES_LIST.md"
    purpose: "Employee availability for matching"
    format: "Markdown table with employee ID, name, department, status"

  - source_name: "Research Completion Tracker"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\RESEARCH_COMPLETION_TRACKER.md"
    purpose: "Last week's completion data for comparison"
    format: "Markdown table with assignment ID, status, quality score"

input_parameters:
  - parameter_name: "analysis_week"
    type: "string"
    format: "[Month]_[Year]_Week_[#]"
    example: "November_2025_Week_3"
    calculation: "Current week number within month (max 5 weeks per month)"

  - parameter_name: "priority_threshold"
    type: "integer"
    range: "1-10"
    default: 6
    description: "Gaps scoring 6+ create immediate research tasks"

  - parameter_name: "max_assignments"
    type: "integer"
    range: "2-4"
    default: 3
    description: "Maximum research tasks to assign per week"

output_specification:
  - output_name: "Weekly Analysis Document"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\REPORTS\Weekly_Analysis\\[Month]_[Year]_Week_[#]_Analysis.md"
    template: "Phase_0_Template.md"
    sections:
      - "Last Week Review"
      - "Department Status (8 departments)"
      - "Gap Identification (new gaps discovered)"
      - "Priority Scoring (Urgency × 3 + Impact × 2)"
      - "Assignment Recommendations (2-4 tasks)"
      - "Employee Availability Check"
      - "Weekly Goals"

  - output_name: "Research Task Recommendations"
    format: "List of 2-4 research tasks"
    task_id_format: "RSH-{DEPT}-###"
    required_fields:
      - task_description
      - gap_addressed
      - recommended_employee
      - employee_department
      - estimated_time
      - suggested_deadline
      - priority_score

validation_rules:
  - "All 8 departments must be reviewed"
  - "Priority scores must be calculated for all gaps"
  - "Employee assignments must match department expertise"
  - "Deadlines must be 5-7 days from assignment date"
  - "Minimum 2, maximum 4 research tasks per week"
```

**Estimated Time:** 30 minutes

---

#### File 2: `TASK_MANAGERS/TSM-006_Workflows/INPUTS/Research_Task_Creation_Input.yaml`

**Purpose:** Template for creating research tasks from Phase 0 recommendations

**Content Structure:**
```yaml
input_spec_name: "Research Task Creation Input Specification"
input_spec_id: "INPUT-SPEC-RSH-002"
workflow_reference: "WF-SEQ-RSH-001"
step_number: 2 # Assignment Creation (TUESDAY)

input_source:
  - source_name: "Phase 0 Analysis Recommendations"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\REPORTS\Weekly_Analysis\\[Month]_[Year]_Week_[#]_Analysis.md"
    section: "Assignment Recommendations"
    format: "List of 2-4 recommended research tasks"

required_task_fields:
  - field_name: "assignment_id"
    format: "RSH-{DEPT}-###"
    examples:
      - "RSH-AI-004"
      - "RSH-LGN-012"
      - "RSH-DEV-007"
    validation: "Must be unique in RESEARCH_ASSIGNMENT_LOG.md"

  - field_name: "research_type"
    options:
      - "Video Phase 5-7" # Gap Analysis + Library Mapping + Extraction
      - "Department Gap Research" # New gap discovered in Phase 0
      - "Tool Investigation" # Tool mentioned but not in LIBRARIES
      - "Process Improvement" # Section 9 improvement opportunity
      - "Cross-Department Research" # 2+ departments need same research

  - field_name: "task_description"
    format: "Clear, actionable description"
    min_length: 20
    max_length: 150
    example: "Research Google Maps API for property search query optimization"

  - field_name: "assigned_to"
    source: "ACTIVE_EMPLOYEES_LIST.md"
    validation: "Employee must be in 'Available' status"
    must_include:
      - employee_full_name
      - employee_id
      - employee_department

  - field_name: "assigned_date"
    format: "YYYY-MM-DD"
    calculation: "Today's date (Tuesday)"

  - field_name: "due_date"
    format: "YYYY-MM-DD"
    calculation: "assigned_date + 5-7 days"
    typical: "Following Tuesday"

  - field_name: "status"
    initial_value: "Assigned"
    allowed_values:
      - "Assigned"
      - "In Progress"
      - "Under Review"
      - "Revision Requested"
      - "Completed"
      - "Archived"

  - field_name: "priority"
    source: "Phase 0 priority score"
    mapping:
      - "8-10 points = Very High"
      - "6-7 points = High"
      - "4-5 points = Medium"
      - "1-3 points = Low"

  - field_name: "estimated_hours"
    source: "Phase 0 recommendation"
    typical_ranges:
      - "Video Phase 5-7: 1-1.5 hours"
      - "Department Gap: 2-3 hours"
      - "Tool Investigation: 1-2 hours"
      - "Process Improvement: 2-4 hours"

output_specification:
  - output_name: "Research Assignment Log Entry"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\RESEARCH_ASSIGNMENT_LOG.md"
    format: "Markdown table row"
    action: "Append new row to assignment table"

  - output_name: "Weekly Research Plan Update"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\WEEKLY_RESEARCH_PLAN.md"
    action: "Add assignments to current week section"

  - output_name: "Employee Notification"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\24\\RSH-{DEPT}-###_{EmployeeName}.md"
    format: "Assignment notification document"
    includes:
      - Assignment ID and description
      - Gap addressed
      - Deliverables expected
      - Due date
      - Quality criteria

validation_rules:
  - "Assignment ID must not exist in RESEARCH_ASSIGNMENT_LOG.md"
  - "Employee must be 'Available' in ACTIVE_EMPLOYEES_LIST.md"
  - "Department match: Employee department = Gap department (preferred)"
  - "Due date must be 5-7 days from assignment date"
  - "All required fields must be populated"
```

**Estimated Time:** 30 minutes

---

#### File 3: `TASK_MANAGERS/TSM-006_Workflows/INPUTS/Department_Report_Gap_Extraction_Input.yaml`

**Purpose:** Specification for extracting research triggers from department reports

**Content Structure:**
```yaml
input_spec_name: "Department Report Gap Extraction Input Specification"
input_spec_id: "INPUT-SPEC-RSH-003"
workflow_reference: "WF-SEQ-RSH-002" # Department_Report_Gap_Extraction_Workflow (new)

input_source:
  - source_name: "Department Daily Reports"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\REPORTS\\[YYYY-MM-DD]\\Departments\\"
    file_pattern: "*_Department_Report_*.md"
    date_range: "Last 7 days"
    departments: 8 # All departments

extraction_targets:
  section_8_research_needed:
    section_name: "RESEARCH NEEDED"
    section_number: 8
    format: "Bulleted list with priority tags"
    extract_fields:
      - research_request: "Full text of research need"
      - priority_tag: "High/Medium/Low (if present)"
      - requestor: "Employee who submitted report"
      - date: "Report date"
      - department: "Department name"
      - context: "Business context/reason for request"
      - timeline: "When research is needed (if specified)"

    priority_scoring:
      explicit_high_priority: +3
      blocks_current_work: +3
      timeline_this_week: +3
      mentioned_multiple_days: +2
      cross_department: +2
      explicit_medium_priority: +1

  section_9_improvements_needed:
    section_name: "IMPROVEMENTS NEEDED"
    section_number: 9
    format: "Categorized list (Process/Technical/Tools/Automation)"
    extract_fields:
      - improvement_type: "Process/Technical/Tools/Automation"
      - improvement_description: "Full text"
      - benefit: "Expected improvement/benefit"
      - department: "Department name"
      - date: "Report date"

    priority_scoring:
      automation_opportunity: +2
      tool_integration: +2
      affects_multiple_employees: +2
      process_improvement: +1
      technical_improvement: +1

  section_6_infrastructure:
    section_name: "INFRASTRUCTURE"
    section_number: 6
    purpose: "Identify tools mentioned but not in LIBRARIES"
    extract_fields:
      - tool_name: "Name of tool/service"
      - tool_usage: "How it's being used"
      - department: "Department name"
      - in_libraries: "Check if exists in LIBRARIES/Tools/"

    research_trigger:
      condition: "tool_name NOT in LIBRARIES/Tools/"
      priority_score: +1
      task_type: "Tool Investigation"

  section_3_milestone_progress:
    section_name: "MILESTONE PROGRESS"
    section_number: 3
    purpose: "Identify blockers preventing milestone completion"
    extract_fields:
      - milestone_name: "Name of blocked milestone"
      - blocker_description: "What's blocking progress"
      - blocker_type: "Technical/Research/Tools/Knowledge"
      - department: "Department name"

    research_trigger:
      condition: "blocker_type = 'Research' OR 'Knowledge'"
      priority_score: +3 # Blockers are high priority

processing_rules:
  deduplication:
    - "Same research request in multiple reports = +2 priority"
    - "Track across all 8 departments to identify cross-department needs"
    - "Compare to DEPARTMENT_GAP_ANALYSIS.md to avoid duplicate gaps"

  priority_calculation:
    formula: "(Urgency × 3) + (Impact × 2)"
    urgency_signals:
      - "Priority: High tag" → Urgency 9-10
      - "Blocking current work" → Urgency 9-10
      - "Needed this week" → Urgency 8-9
      - "Needed soon" → Urgency 6-7
      - "Important but can wait" → Urgency 4-5
      - "Nice to have" → Urgency 1-3

    impact_signals:
      - "Affects 10+ employees" → Impact 10
      - "Affects 5-9 employees" → Impact 7-9
      - "Affects 2-4 employees" → Impact 4-6
      - "Affects 1 employee" → Impact 1-3
      - "Cross-department need" → Impact +2
      - "Critical business function" → Impact +3

output_specification:
  - output_name: "Weekly Gap Analysis"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\REPORTS\Weekly_Analysis\\Weekly_Gap_Analysis_[YYYY-MM-DD].md"
    format: "Markdown document"
    sections:
      - "Summary Statistics"
      - "High Priority Gaps (6+ points)"
      - "Medium Priority Gaps (3-5 points)"
      - "Low Priority Gaps (1-2 points)"
      - "Cross-Department Needs"
      - "Tools Not in LIBRARIES"
      - "Recommended Research Tasks (2-4 tasks)"

  - output_name: "Gap Inventory Update"
    location: "C:\\Users\\Dell\\Dropbox\\ENTITIES\\RESEARCHES\\LOGS\\DEPARTMENT_GAP_ANALYSIS.md"
    action: "Add new gaps discovered"
    gap_id_format: "{DEPT}-GAP-###"
    examples:
      - "LGN-GAP-001" # Lead Generation gap
      - "AI-GAP-002" # AI department gap

automation_potential:
  - "Run automatically every Monday morning before Phase 0 analysis"
  - "Triggered by: 'New week starts' OR 'Manual execution'"
  - "Outputs feed directly into Phase 0 analysis input"
  - "Saves 30-45 minutes of manual report scanning"
```

**Estimated Time:** 45 minutes

---

### 4.2 Task Templates for Research Activities (4 files)

#### File 4: `TASK_MANAGERS/TSM-003_Task_Templates/TASK-TEMPLATE-023_Phase_0_Weekly_Analysis.json`

**Purpose:** Template for Monday Phase 0 weekly analysis task

**Content Structure:**
```json
{
  "template_id": "TASK-TEMPLATE-023",
  "template_name": "Phase 0 Weekly Analysis",
  "template_version": "1.0",
  "category": "Research Management",
  "subcategory": "Weekly Analysis",
  "description": "Monday morning Phase 0 analysis to identify research priorities and make assignment recommendations",

  "task_details": {
    "task_name": "Phase 0 Weekly Analysis - [Month] [Year] Week [#]",
    "task_type": "Recurring",
    "frequency": "Weekly",
    "schedule": "Every Monday 9:00-10:30 AM",
    "duration_minutes": 90,
    "assigned_to": "Research Manager",
    "priority": "High",
    "tags": ["research", "weekly", "analysis", "phase-0"]
  },

  "input_requirements": {
    "input_spec": "INPUT-SPEC-RSH-001",
    "required_files": [
      "Department reports (last 7 days, all 8 departments)",
      "DEPARTMENT_GAP_ANALYSIS.md",
      "ACTIVE_EMPLOYEES_LIST.md",
      "RESEARCH_COMPLETION_TRACKER.md",
      "Weekly_Gap_Analysis_[date].md (from gap extraction workflow)"
    ],
    "prerequisites": [
      "All 8 departments submitted reports for last 7 days",
      "Gap extraction workflow completed",
      "Previous week's research assignments reviewed"
    ]
  },

  "steps": [
    {
      "step_number": 1,
      "step_name": "Last Week Review",
      "duration_minutes": 10,
      "description": "Review last week's research assignments and completion data",
      "checklist": [
        "Check RESEARCH_COMPLETION_TRACKER.md for completed assignments",
        "Note quality scores for completed research",
        "Identify any overdue or blocked assignments",
        "Calculate week-over-week completion rate"
      ]
    },
    {
      "step_number": 2,
      "step_name": "Department Status Review",
      "duration_minutes": 15,
      "description": "Review all 8 departments' reports from last week",
      "checklist": [
        "Review Weekly_Gap_Analysis_[date].md from gap extraction",
        "Scan Section 8 (RESEARCH NEEDED) from all departments",
        "Scan Section 9 (IMPROVEMENTS NEEDED) from all departments",
        "Note cross-department patterns",
        "Identify tools mentioned in Section 6 not in LIBRARIES"
      ]
    },
    {
      "step_number": 3,
      "step_name": "Gap Identification",
      "duration_minutes": 20,
      "description": "Identify and document new gaps discovered",
      "checklist": [
        "List all new gaps from department reports",
        "Check DEPARTMENT_GAP_ANALYSIS.md for duplicates",
        "Assign gap IDs: {DEPT}-GAP-###",
        "Document gap description, department, discovery source",
        "Note if gap blocks current work or milestones"
      ]
    },
    {
      "step_number": 4,
      "step_name": "Priority Scoring",
      "duration_minutes": 20,
      "description": "Score all gaps using objective priority formula",
      "checklist": [
        "Rate Urgency (1-10) for each gap",
        "Rate Impact (1-10) for each gap",
        "Calculate Priority Score: (Urgency × 3) + (Impact × 2)",
        "Rank gaps by priority score",
        "Identify High (6+), Medium (3-5), Low (1-2) priorities"
      ]
    },
    {
      "step_number": 5,
      "step_name": "Assignment Recommendations",
      "duration_minutes": 15,
      "description": "Generate 2-4 research task recommendations",
      "checklist": [
        "Select top 2-4 gaps (priority score 6+)",
        "Match gaps to employee expertise (check ACTIVE_EMPLOYEES_LIST.md)",
        "Verify employee availability",
        "Estimate research time (1-4 hours)",
        "Set suggested deadline (5-7 days)",
        "Document gap addressed and expected deliverables"
      ]
    },
    {
      "step_number": 6,
      "step_name": "Employee Availability Check",
      "duration_minutes": 5,
      "description": "Verify recommended employees are available",
      "checklist": [
        "Check ACTIVE_EMPLOYEES_LIST.md status",
        "Verify no conflicting assignments in RESEARCH_ASSIGNMENT_LOG.md",
        "Confirm department match (employee dept = gap dept preferred)",
        "Note any availability constraints"
      ]
    },
    {
      "step_number": 7,
      "step_name": "Weekly Goals Setting",
      "duration_minutes": 5,
      "description": "Set measurable weekly goals",
      "checklist": [
        "Set research completion goal (e.g., 2 assignments completed)",
        "Set LIBRARIES growth goal (e.g., 5+ new tools/workflows added)",
        "Set gap closure goal (e.g., 2 gaps closed this week)",
        "Document goals in weekly analysis file"
      ]
    }
  ],

  "deliverables": [
    {
      "deliverable_name": "Weekly Analysis Document",
      "file_location": "REPORTS/Weekly_Analysis/[Month]_[Year]_Week_[#]_Analysis.md",
      "template": "Phase_0_Template.md",
      "required_sections": [
        "Last Week Review",
        "Department Status (8 departments)",
        "Gap Identification",
        "Priority Scoring",
        "Assignment Recommendations (2-4 tasks)",
        "Employee Availability",
        "Weekly Goals"
      ]
    },
    {
      "deliverable_name": "Research Task Recommendations",
      "quantity": "2-4 tasks",
      "format": "List with task ID, description, employee, deadline, priority"
    }
  ],

  "quality_criteria": {
    "completeness": [
      "All 8 departments reviewed",
      "All gaps from Section 8 & 9 documented",
      "Priority scores calculated for all gaps",
      "2-4 research tasks recommended"
    ],
    "accuracy": [
      "Priority scores follow formula: (Urgency × 3) + (Impact × 2)",
      "Employee assignments match department expertise",
      "Deadlines are realistic (5-7 days)",
      "No duplicate gaps vs. DEPARTMENT_GAP_ANALYSIS.md"
    ],
    "timeliness": [
      "Completed by Monday 10:30 AM",
      "Within 90-minute time budget"
    ]
  },

  "next_steps": [
    "Tuesday: Create research assignments in RESEARCH_ASSIGNMENT_LOG.md",
    "Tuesday: Send employee notifications (24/ folder or Discord)",
    "Wednesday-Friday: Monitor assignment progress",
    "Following Monday: Review completed assignments in next Phase 0"
  ]
}
```

**Estimated Time:** 30 minutes

---

#### File 5: `TASK_MANAGERS/TSM-003_Task_Templates/TASK-TEMPLATE-024_Department_Report_Review.json`

**Purpose:** Template for daily department report review (optional for Research Manager)

**Content Structure:**
```json
{
  "template_id": "TASK-TEMPLATE-024",
  "template_name": "Department Report Review (Daily - Optional)",
  "template_version": "1.0",
  "category": "Research Management",
  "subcategory": "Daily Monitoring",
  "description": "Optional daily review of department reports to identify urgent research needs",

  "task_details": {
    "task_name": "Daily Department Report Review - [YYYY-MM-DD]",
    "task_type": "Recurring",
    "frequency": "Daily (Optional)",
    "schedule": "End of day (5:00-5:15 PM)",
    "duration_minutes": 15,
    "assigned_to": "Research Manager",
    "priority": "Low",
    "optional": true,
    "tags": ["research", "daily", "reports", "monitoring"]
  },

  "purpose": {
    "primary": "Catch urgent research needs that can't wait until Monday Phase 0",
    "secondary": "Build familiarity with department activities before Monday analysis",
    "trigger_urgent_assignment": "If High Priority + Blocking Work in Section 8"
  },

  "steps": [
    {
      "step_number": 1,
      "step_name": "Quick Scan Section 8",
      "duration_minutes": 10,
      "description": "Scan Section 8 (RESEARCH NEEDED) from today's reports",
      "checklist": [
        "Open REPORTS/[today]/Departments/ folder",
        "Quick scan Section 8 from all departments",
        "Look for 'High Priority' tags",
        "Look for 'Blocking work' indicators",
        "Note any urgent research requests"
      ]
    },
    {
      "step_number": 2,
      "step_name": "Urgency Assessment",
      "duration_minutes": 3,
      "description": "Assess if any research needs immediate action",
      "criteria": {
        "urgent_if": [
          "Tagged 'High Priority' AND 'Blocking current work'",
          "Prevents milestone completion this week",
          "Critical business impact (customer-facing issue)"
        ],
        "can_wait_if": [
          "Medium Priority",
          "No immediate blocker",
          "Can be addressed in Monday Phase 0"
        ]
      }
    },
    {
      "step_number": 3,
      "step_name": "Action Decision",
      "duration_minutes": 2,
      "description": "Decide: urgent assignment or wait for Monday",
      "decision_tree": {
        "if_urgent": "Create immediate research assignment (skip Phase 0)",
        "if_not_urgent": "Add to Monday Phase 0 analysis queue"
      }
    }
  ],

  "deliverables": [
    {
      "deliverable_name": "Urgent Research Assignment (if triggered)",
      "file_location": "RESEARCHES/LOGS/RESEARCH_ASSIGNMENT_LOG.md",
      "condition": "Only if urgent research need identified"
    },
    {
      "deliverable_name": "Note for Monday Phase 0",
      "format": "Quick note of patterns observed during week"
    }
  ],

  "notes": [
    "This task is OPTIONAL - Phase 0 Monday analysis is the primary process",
    "Only create urgent assignments if truly blocking work (rare)",
    "Most research needs can wait until Monday Phase 0",
    "Benefit: Research Manager builds context before Monday analysis"
  ]
}
```

**Estimated Time:** 20 minutes

---

#### File 6: `TASK_MANAGERS/TSM-003_Task_Templates/TASK-TEMPLATE-025_Research_Assignment_Creation.json`

**Purpose:** Template for Tuesday research assignment creation task

**Content Structure:**
```json
{
  "template_id": "TASK-TEMPLATE-025",
  "template_name": "Research Assignment Creation",
  "template_version": "1.0",
  "category": "Research Management",
  "subcategory": "Assignment Management",
  "description": "Tuesday task to create research assignments from Monday Phase 0 recommendations",

  "task_details": {
    "task_name": "Create Research Assignments - Week [#]",
    "task_type": "Recurring",
    "frequency": "Weekly",
    "schedule": "Every Tuesday morning (9:00-10:00 AM)",
    "duration_minutes": 60,
    "assigned_to": "Research Manager",
    "priority": "High",
    "tags": ["research", "weekly", "assignments", "phase-1"]
  },

  "input_requirements": {
    "input_spec": "INPUT-SPEC-RSH-002",
    "required_files": [
      "Monday's Phase 0 analysis (with 2-4 recommendations)",
      "RESEARCH_ASSIGNMENT_LOG.md",
      "ACTIVE_EMPLOYEES_LIST.md",
      "DEPARTMENT_GAP_ANALYSIS.md"
    ],
    "prerequisites": [
      "Phase 0 analysis completed Monday",
      "2-4 research tasks recommended",
      "Employees verified as available"
    ]
  },

  "steps": [
    {
      "step_number": 1,
      "step_name": "Review Phase 0 Recommendations",
      "duration_minutes": 10,
      "description": "Review Monday's Phase 0 analysis recommendations",
      "checklist": [
        "Open latest Phase 0 analysis file",
        "Read Assignment Recommendations section",
        "Verify 2-4 tasks recommended",
        "Note task descriptions, employees, deadlines",
        "Confirm priority scores"
      ]
    },
    {
      "step_number": 2,
      "step_name": "Generate Assignment IDs",
      "duration_minutes": 5,
      "description": "Create unique assignment IDs for each task",
      "checklist": [
        "Check RESEARCH_ASSIGNMENT_LOG.md for last used ID",
        "Generate IDs in format: RSH-{DEPT}-###",
        "Examples: RSH-AI-004, RSH-LGN-012, RSH-VID-006",
        "Ensure no duplicate IDs",
        "Document ID mapping to task description"
      ]
    },
    {
      "step_number": 3,
      "step_name": "Verify Employee Availability",
      "duration_minutes": 5,
      "description": "Double-check recommended employees are available",
      "checklist": [
        "Open ACTIVE_EMPLOYEES_LIST.md",
        "Verify each recommended employee status = 'Available'",
        "Check RESEARCH_ASSIGNMENT_LOG.md for conflicting assignments",
        "Confirm no employee has 2+ active assignments",
        "If unavailable, select alternative employee from same department"
      ]
    },
    {
      "step_number": 4,
      "step_name": "Create Assignment Log Entries",
      "duration_minutes": 15,
      "description": "Add new assignments to RESEARCH_ASSIGNMENT_LOG.md",
      "checklist": [
        "For each recommended task:",
        "- Add row to assignment table",
        "- Fill: Assignment ID, Research Type, Task Description",
        "- Fill: Assigned To, Employee ID, Department",
        "- Fill: Assigned Date (today), Due Date (5-7 days)",
        "- Fill: Status (Assigned), Priority (from Phase 0)",
        "- Fill: Estimated Hours",
        "Verify table formatting",
        "Save file"
      ]
    },
    {
      "step_number": 5,
      "step_name": "Update Weekly Research Plan",
      "duration_minutes": 5,
      "description": "Add assignments to WEEKLY_RESEARCH_PLAN.md",
      "checklist": [
        "Open WEEKLY_RESEARCH_PLAN.md",
        "Find current week section",
        "Update status: 'Assignments Made'",
        "Add each assignment with employee and due date",
        "Add gap addressed for each assignment",
        "Save file"
      ]
    },
    {
      "step_number": 6,
      "step_name": "Create Employee Notifications",
      "duration_minutes": 15,
      "description": "Create assignment notification files for employees",
      "checklist": [
        "For each assignment:",
        "- Create file: 24/RSH-{DEPT}-###_{EmployeeName}.md",
        "- Include: Assignment ID, description, gap addressed",
        "- Include: Deliverables expected (Gap Analysis + Library Mapping)",
        "- Include: Due date, estimated time",
        "- Include: Quality criteria (Completeness, Accuracy, Actionability)",
        "- Include: Submission location",
        "Optional: Send Discord/Email notification pointing to 24/ folder"
      ]
    },
    {
      "step_number": 7,
      "step_name": "Update Department Gap Analysis",
      "duration_minutes": 5,
      "description": "Mark gaps as 'Research In Progress'",
      "checklist": [
        "Open DEPARTMENT_GAP_ANALYSIS.md",
        "Find gaps addressed by new assignments",
        "Update status: 'Open' → 'Research In Progress'",
        "Add research assignment ID to gap entry",
        "Add assigned employee name",
        "Save file"
      ]
    }
  ],

  "deliverables": [
    {
      "deliverable_name": "Research Assignment Log Entries",
      "file_location": "RESEARCHES/LOGS/RESEARCH_ASSIGNMENT_LOG.md",
      "quantity": "2-4 new rows",
      "format": "Markdown table rows"
    },
    {
      "deliverable_name": "Employee Notifications",
      "file_location": "RESEARCHES/24/RSH-{DEPT}-###_{EmployeeName}.md",
      "quantity": "2-4 files (one per assignment)",
      "format": "Markdown document"
    },
    {
      "deliverable_name": "Weekly Research Plan Update",
      "file_location": "RESEARCHES/LOGS/WEEKLY_RESEARCH_PLAN.md",
      "action": "Current week updated with assignments"
    },
    {
      "deliverable_name": "Department Gap Analysis Update",
      "file_location": "RESEARCHES/LOGS/DEPARTMENT_GAP_ANALYSIS.md",
      "action": "Gaps marked 'Research In Progress'"
    }
  ],

  "quality_criteria": {
    "completeness": [
      "All Phase 0 recommendations converted to assignments",
      "All required fields populated in assignment log",
      "Employee notifications created for all assignments",
      "All tracking files updated"
    ],
    "accuracy": [
      "Assignment IDs unique and follow format",
      "Employee assignments match availability",
      "Deadlines calculated correctly (5-7 days)",
      "Gap IDs correctly referenced"
    ],
    "timeliness": [
      "Completed Tuesday morning (within 24 hours of Phase 0)",
      "Employees have full week to complete research"
    ]
  },

  "next_steps": [
    "Tuesday-Friday: Monitor assignment progress (optional check-ins)",
    "Following Tuesday: Review submitted deliverables",
    "Wednesday-Friday: Quality review of submissions",
    "Update RESEARCH_COMPLETION_TRACKER.md when assignments complete"
  ]
}
```

**Estimated Time:** 30 minutes

---

#### File 7: `TASK_MANAGERS/TSM-003_Task_Templates/TASK-TEMPLATE-026_Research_Quality_Review.json`

**Purpose:** Template for quality review of submitted research deliverables

**Content Structure:**
```json
{
  "template_id": "TASK-TEMPLATE-026",
  "template_name": "Research Quality Review",
  "template_version": "1.0",
  "category": "Research Management",
  "subcategory": "Quality Assurance",
  "description": "Review submitted research deliverables using 100-point rubric (0-10 scale)",

  "task_details": {
    "task_name": "Quality Review - [Assignment ID]",
    "task_type": "Ad-hoc",
    "frequency": "Per assignment submission",
    "schedule": "Wednesday-Friday (as submissions arrive)",
    "duration_minutes": 30,
    "assigned_to": "Research Manager",
    "priority": "High",
    "tags": ["research", "quality", "review", "approval"]
  },

  "input_requirements": {
    "required_deliverables": [
      "Gap Analysis document",
      "Library Mapping Report"
    ],
    "metadata": [
      "Assignment ID",
      "Employee name",
      "Due date",
      "Submission date",
      "Gap addressed"
    ]
  },

  "steps": [
    {
      "step_number": 1,
      "step_name": "Completeness Review (40 points)",
      "duration_minutes": 10,
      "description": "Assess if all required components are present",
      "scoring_criteria": {
        "gap_analysis_complete": {
          "points": 20,
          "requirements": [
            "Gap clearly defined (what's missing)",
            "Current state documented",
            "Desired state documented",
            "Impact analysis included",
            "Tools/workflows identified to close gap"
          ],
          "scoring": {
            "20_points": "All 5 requirements met",
            "15_points": "4 of 5 requirements met",
            "10_points": "3 of 5 requirements met",
            "5_points": "2 of 5 requirements met",
            "0_points": "0-1 requirements met"
          }
        },
        "library_mapping_complete": {
          "points": 20,
          "requirements": [
            "Tools mapped to LIBRARIES/Tools/ categories",
            "Workflows mapped to LIBRARIES/Workflows/ categories",
            "Cross-references provided (sources)",
            "Integration recommendations included",
            "Examples or use cases provided"
          ],
          "scoring": {
            "20_points": "All 5 requirements met",
            "15_points": "4 of 5 requirements met",
            "10_points": "3 of 5 requirements met",
            "5_points": "2 of 5 requirements met",
            "0_points": "0-1 requirements met"
          }
        }
      }
    },
    {
      "step_number": 2,
      "step_name": "Accuracy Review (30 points)",
      "duration_minutes": 10,
      "description": "Verify correctness of research findings",
      "scoring_criteria": {
        "tool_workflow_verification": {
          "points": 15,
          "requirements": [
            "Tools/workflows actually exist (not hallucinated)",
            "Descriptions are accurate",
            "Capabilities correctly stated",
            "Integration points verified"
          ],
          "scoring": {
            "15_points": "All verified, no errors",
            "10_points": "Minor errors (1-2), easily correctable",
            "5_points": "Moderate errors (3-4), need revision",
            "0_points": "Major errors or hallucinations"
          }
        },
        "cross_reference_accuracy": {
          "points": 15,
          "requirements": [
            "Sources cited correctly",
            "Gap ID correctly referenced",
            "Department correctly identified",
            "Assignment ID correctly used"
          ],
          "scoring": {
            "15_points": "All references accurate",
            "10_points": "1 reference error",
            "5_points": "2 reference errors",
            "0_points": "3+ reference errors"
          }
        }
      }
    },
    {
      "step_number": 3,
      "step_name": "Quality Review (20 points)",
      "duration_minutes": 5,
      "description": "Assess organization, clarity, depth",
      "scoring_criteria": {
        "organization_clarity": {
          "points": 10,
          "requirements": [
            "Well-structured document",
            "Clear headings and sections",
            "Easy to navigate",
            "Professional formatting"
          ],
          "scoring": {
            "10_points": "Excellent organization",
            "7_points": "Good organization, minor issues",
            "4_points": "Adequate, needs improvement",
            "0_points": "Poor organization, hard to follow"
          }
        },
        "depth_insight": {
          "points": 10,
          "requirements": [
            "Goes beyond surface-level",
            "Provides insights or analysis",
            "Identifies patterns or connections",
            "Shows understanding of business context"
          ],
          "scoring": {
            "10_points": "Excellent depth and insights",
            "7_points": "Good depth, some insights",
            "4_points": "Adequate, mostly descriptive",
            "0_points": "Superficial, no insights"
          }
        }
      }
    },
    {
      "step_number": 4,
      "step_name": "Actionability Review (10 points)",
      "duration_minutes": 3,
      "description": "Assess integration readiness",
      "scoring_criteria": {
        "integration_readiness": {
          "points": 10,
          "requirements": [
            "Clear integration recommendations",
            "LIBRARIES categories identified",
            "No additional research needed",
            "Ready to add to LIBRARIES immediately"
          ],
          "scoring": {
            "10_points": "Ready to integrate immediately",
            "7_points": "Minor clarifications needed",
            "4_points": "Moderate revision needed",
            "0_points": "Significant additional work needed"
          }
        }
      }
    },
    {
      "step_number": 5,
      "step_name": "Calculate Total Score",
      "duration_minutes": 1,
      "description": "Sum all points and convert to 0-10 scale",
      "formula": "Total Points ÷ 10 = Score (0-10 scale)",
      "example": "75 points ÷ 10 = 7.5 score"
    },
    {
      "step_number": 6,
      "step_name": "Make Decision",
      "duration_minutes": 1,
      "description": "Approve, request revision, or reject",
      "decision_matrix": {
        "approve": {
          "condition": "Score ≥ 5.0 (50+ points)",
          "action": "Mark assignment 'Completed', proceed to LIBRARIES integration"
        },
        "request_revision": {
          "condition": "Score 3.0-4.9 (30-49 points)",
          "action": "Mark assignment 'Revision Requested', provide feedback"
        },
        "reject": {
          "condition": "Score < 3.0 (< 30 points)",
          "action": "Mark assignment 'Rejected', reassign to different employee"
        }
      }
    }
  ],

  "deliverables": [
    {
      "deliverable_name": "Quality Score",
      "format": "0-10 scale (with 100-point breakdown)",
      "example": "7.5/10 (75/100 points)"
    },
    {
      "deliverable_name": "Review Feedback",
      "format": "Markdown document",
      "sections": [
        "Overall Score and Decision",
        "Completeness Feedback (what's missing or incomplete)",
        "Accuracy Feedback (errors to correct)",
        "Quality Feedback (organization/clarity suggestions)",
        "Actionability Feedback (integration readiness notes)"
      ]
    },
    {
      "deliverable_name": "Assignment Status Update",
      "file_location": "RESEARCHES/LOGS/RESEARCH_ASSIGNMENT_LOG.md",
      "update": "Status = 'Completed' or 'Revision Requested' or 'Rejected'"
    },
    {
      "deliverable_name": "Completion Tracker Update",
      "file_location": "RESEARCHES/LOGS/RESEARCH_COMPLETION_TRACKER.md",
      "update": "Add quality score, completion date, decision"
    }
  ],

  "quality_thresholds": {
    "acceptance_threshold": "5.0/10 (50/100 points)",
    "excellent_threshold": "8.0/10 (80/100 points)",
    "revision_threshold": "3.0-4.9/10 (30-49 points)",
    "rejection_threshold": "< 3.0/10 (< 30 points)"
  },

  "next_steps_after_approval": [
    "Integrate findings into LIBRARIES/Tools/ and LIBRARIES/Workflows/",
    "Update DEPARTMENT_GAP_ANALYSIS.md status: 'Research In Progress' → 'Closed'",
    "Add to RESEARCH_COMPLETION_TRACKER.md",
    "Notify employee of approval",
    "Add cross-reference to LIBRARIES entries: RSH-XXX-XX"
  ],

  "revision_process": {
    "if_revision_requested": [
      "Create detailed feedback document",
      "Highlight specific areas needing improvement",
      "Provide examples of what's expected",
      "Set revision deadline (2-3 days)",
      "Send feedback to employee (24/ folder or Discord)"
    ],
    "revision_timeline": "2-3 days",
    "re_review": "Same quality review process upon resubmission"
  }
}
```

**Estimated Time:** 45 minutes

---

### 4.3 Gap Extraction Workflow (1 file)

#### File 8: `TASK_MANAGERS/TSM-006_Workflows/Department_Report_Gap_Extraction_Workflow.yaml`

**Purpose:** Automated workflow for extracting research gaps from department reports

**Content Structure:**
```yaml
workflow_name: "Department Report Gap Extraction"
workflow_type: "Sequential + Automated"
workflow_id: "WF-SEQ-RSH-002"
department: "Research Management"
priority: "High"
estimated_duration: "30-45 minutes"
frequency: "Weekly (every Monday before Phase 0)"

description: |
  Automated workflow to extract research needs from department reports (Section 8, 9, 6, 3)
  and generate prioritized gap analysis for Phase 0 input.

  This workflow runs BEFORE Phase 0 analysis to prepare the input data.

trigger:
  type: "Scheduled OR Manual"
  schedule: "Every Monday 8:00 AM (1 hour before Phase 0)"
  manual: "Can be run on-demand by Research Manager"

input_specification:
  input_spec_id: "INPUT-SPEC-RSH-003"
  data_sources:
    - department_reports: "REPORTS/[last 7 days]/Departments/"
    - existing_gaps: "RESEARCHES/LOGS/DEPARTMENT_GAP_ANALYSIS.md"
    - libraries_tools: "LIBRARIES/Tools/" # For checking tool existence
    - libraries_workflows: "LIBRARIES/Workflows/" # For checking workflow existence

steps:
  - step_number: 1
    name: "Collect Department Reports"
    duration: "5 minutes"
    automation_potential: "High"
    description: "Gather all department reports from last 7 days"

    actions:
      - "Scan REPORTS/ directory for last 7 days"
      - "Collect all *_Department_Report_*.md files"
      - "Verify 8 departments × 7 days = ~56 reports (some may be missing)"
      - "Group reports by department"
      - "Sort by date (oldest to newest)"

    output:
      - "List of report files grouped by department and date"
      - "Missing report identification (if any departments skipped days)"

  - step_number: 2
    name: "Extract Section 8: RESEARCH NEEDED"
    duration: "10 minutes"
    automation_potential: "Very High"
    description: "Extract all explicit research requests from Section 8"

    prompt_reference: "PMT-094_Weekly_Report_Gap_Analysis.md (Section 8 extraction)"

    actions:
      - "For each report:"
      - "  - Locate Section 8: RESEARCH NEEDED"
      - "  - Extract all bulleted research items"
      - "  - Capture: request text, priority tag, requestor, date, department"
      - "  - Note if mentioned multiple days (track frequency)"
      - "Deduplicate: Same request from multiple days = +2 priority"
      - "Deduplicate: Same request from multiple departments = cross-department"

    extraction_fields:
      - research_request: "Full text of research need"
      - priority_tag: "High/Medium/Low (if present in report)"
      - requestor: "Employee who submitted report"
      - date: "Report date"
      - department: "Department name"
      - context: "Business context (why needed)"
      - timeline: "When needed (if specified)"
      - frequency: "Number of days mentioned"
      - cross_department: "Boolean (mentioned by 2+ departments)"

    output:
      - "Structured list of Section 8 research requests (all departments)"
      - "Deduplication notes (which requests repeated, how many times)"

  - step_number: 3
    name: "Extract Section 9: IMPROVEMENTS NEEDED"
    duration: "10 minutes"
    automation_potential: "Very High"
    description: "Extract improvement opportunities from Section 9"

    actions:
      - "For each report:"
      - "  - Locate Section 9: IMPROVEMENTS NEEDED"
      - "  - Extract Process improvements"
      - "  - Extract Technical improvements"
      - "  - Extract Tool integration needs"
      - "  - Extract Automation opportunities"
      - "Identify which improvements require research vs. implementation"

    extraction_fields:
      - improvement_type: "Process/Technical/Tools/Automation"
      - improvement_description: "Full text"
      - research_required: "Boolean (does this need research first?)"
      - benefit: "Expected improvement/benefit"
      - department: "Department name"
      - date: "Report date"

    research_trigger_criteria:
      - "Improvement requires new tool investigation"
      - "Improvement requires workflow research"
      - "Improvement requires knowledge gap closure"
      - "Improvement mentions 'need to research' or 'need to learn'"

    output:
      - "List of improvements requiring research (filtered)"
      - "List of improvements for implementation (not research)"

  - step_number: 4
    name: "Extract Section 6: INFRASTRUCTURE (Tool Gaps)"
    duration: "5 minutes"
    automation_potential: "Very High"
    description: "Identify tools mentioned but not in LIBRARIES"

    actions:
      - "For each report:"
      - "  - Locate Section 6: INFRASTRUCTURE"
      - "  - Extract all tool/service names"
      - "  - Check if tool exists in LIBRARIES/Tools/"
      - "  - If NOT in LIBRARIES: flag as research gap"
      - "Deduplicate: Same tool across multiple departments"

    extraction_fields:
      - tool_name: "Name of tool/service"
      - tool_usage: "How it's being used (from report)"
      - department: "Department using tool"
      - in_libraries: "Boolean (exists in LIBRARIES?)"

    research_trigger:
      condition: "in_libraries = False"
      priority_score: "+1 (Tool Investigation research type)"

    output:
      - "List of tools NOT in LIBRARIES (research needed)"
      - "List of tools IN LIBRARIES (no action needed)"

  - step_number: 5
    name: "Extract Section 3: MILESTONE PROGRESS (Blockers)"
    duration: "5 minutes"
    automation_potential: "High"
    description: "Identify research/knowledge blockers preventing milestone completion"

    actions:
      - "For each report:"
      - "  - Locate Section 3: MILESTONE PROGRESS"
      - "  - Scan for blocked milestones"
      - "  - Identify blocker type (Technical/Research/Tools/Knowledge)"
      - "  - If blocker type = Research or Knowledge: flag as research gap"

    extraction_fields:
      - milestone_name: "Name of blocked milestone"
      - blocker_description: "What's blocking progress"
      - blocker_type: "Technical/Research/Tools/Knowledge"
      - department: "Department name"

    research_trigger:
      condition: "blocker_type IN ['Research', 'Knowledge']"
      priority_score: "+3 (High priority - blocking current work)"

    output:
      - "List of research/knowledge blockers"
      - "Milestone impact assessment"

  - step_number: 6
    name: "Priority Scoring"
    duration: "10 minutes"
    automation_potential: "High"
    description: "Score all discovered gaps using priority formula"

    formula: "(Urgency × 3) + (Impact × 2) = Priority Score"

    urgency_signals:
      - name: "High Priority tag in Section 8"
        urgency_score: 9-10
      - name: "Blocking current work"
        urgency_score: 9-10
      - name: "Needed this week"
        urgency_score: 8-9
      - name: "Needed soon (2-3 weeks)"
        urgency_score: 6-7
      - name: "Medium Priority tag"
        urgency_score: 5-6
      - name: "Important but can wait"
        urgency_score: 4-5
      - name: "Nice to have"
        urgency_score: 1-3

    impact_signals:
      - name: "Affects 10+ employees"
        impact_score: 10
      - name: "Cross-department (2+ departments)"
        impact_score: 8-9
      - name: "Affects 5-9 employees"
        impact_score: 7-8
      - name: "Critical business function"
        impact_score: 9-10
      - name: "Affects 2-4 employees"
        impact_score: 4-6
      - name: "Affects 1 employee"
        impact_score: 1-3

    actions:
      - "For each gap discovered (from steps 2-5):"
      - "  - Rate Urgency (1-10) based on signals"
      - "  - Rate Impact (1-10) based on signals"
      - "  - Calculate: (Urgency × 3) + (Impact × 2)"
      - "  - Classify: High (6+), Medium (3-5), Low (1-2)"
      - "Sort gaps by priority score (highest first)"

    output:
      - "Scored and ranked gap list"
      - "High priority gaps (6+ points)"
      - "Medium priority gaps (3-5 points)"
      - "Low priority gaps (1-2 points)"

  - step_number: 7
    name: "Deduplication vs. Existing Gaps"
    duration: "5 minutes"
    automation_potential: "High"
    description: "Check discovered gaps against DEPARTMENT_GAP_ANALYSIS.md"

    actions:
      - "Open DEPARTMENT_GAP_ANALYSIS.md"
      - "For each discovered gap:"
      - "  - Check if similar gap already exists"
      - "  - If exists: note as 'reinforcement' (increases priority)"
      - "  - If new: flag as 'new gap'"
      - "Avoid creating duplicate gap entries"

    deduplication_logic:
      - "Exact match: Same gap description = reinforcement"
      - "Partial match: Related gap = note connection"
      - "No match: New gap = create new entry"

    output:
      - "List of NEW gaps (not in existing gap analysis)"
      - "List of REINFORCED gaps (already documented, now higher priority)"
      - "Deduplication report"

  - step_number: 8
    name: "Generate Weekly Gap Analysis Document"
    duration: "5 minutes"
    automation_potential: "Very High"
    description: "Create structured gap analysis document for Phase 0 input"

    output_file: "REPORTS/Weekly_Analysis/Weekly_Gap_Analysis_[YYYY-MM-DD].md"

    document_sections:
      - section_name: "Summary Statistics"
        content:
          - "Total gaps discovered: [#]"
          - "New gaps: [#]"
          - "Reinforced gaps: [#]"
          - "High priority (6+): [#]"
          - "Medium priority (3-5): [#]"
          - "Low priority (1-2): [#]"
          - "Cross-department needs: [#]"
          - "Tools not in LIBRARIES: [#]"

      - section_name: "High Priority Gaps (6+ points)"
        format: "Table with gap ID, description, department, priority score, urgency, impact"
        sort: "By priority score (highest first)"

      - section_name: "Medium Priority Gaps (3-5 points)"
        format: "Same table format"

      - section_name: "Low Priority Gaps (1-2 points)"
        format: "Same table format"

      - section_name: "Cross-Department Needs"
        content: "Gaps mentioned by 2+ departments (high impact)"

      - section_name: "Tools Not in LIBRARIES"
        content: "Tools discovered in Section 6 needing investigation"

      - section_name: "Recommended Research Tasks (2-4)"
        content:
          - "Top 2-4 gaps (priority 6+)"
          - "Preliminary employee matching (to be confirmed in Phase 0)"
          - "Estimated research time"
          - "Expected deliverables"

    output:
      - "Weekly_Gap_Analysis_[YYYY-MM-DD].md file created"
      - "Ready for Phase 0 analysis input"

deliverables:
  - deliverable_name: "Weekly Gap Analysis Document"
    location: "REPORTS/Weekly_Analysis/Weekly_Gap_Analysis_[YYYY-MM-DD].md"
    format: "Markdown with 6 sections"

  - deliverable_name: "Prioritized Gap List"
    content: "All gaps scored and ranked"

  - deliverable_name: "Research Task Recommendations (Preliminary)"
    content: "Top 2-4 gaps recommended for research assignment"

integration_with_phase_0:
  description: "This workflow FEEDS INTO Phase 0 analysis"
  timing: "Runs Monday 8:00 AM, completes by 8:45 AM"
  phase_0_starts: "Monday 9:00 AM (uses gap extraction output as input)"
  benefit: "Saves 30-45 minutes of manual report scanning in Phase 0"

automation_potential:
  current_state: "Manual (Research Manager executes PMT-094 prompt)"
  future_state: "Automated (script or AI agent runs weekly)"
  automation_steps:
    - "Schedule: Every Monday 8:00 AM"
    - "Trigger: Cron job or scheduled task"
    - "Input: Automatically collect last 7 days reports"
    - "Process: AI agent executes PMT-094 prompt"
    - "Output: Generate Weekly_Gap_Analysis_[date].md"
    - "Notify: Ping Research Manager when complete"

  time_savings: "30-45 minutes per week (78-117 hours per year)"

notes:
  - "This workflow is the 'prep work' for Phase 0 analysis"
  - "Outputs from this workflow = Inputs to Phase 0"
  - "Can be run manually if automation not yet implemented"
  - "PMT-094 prompt already exists and tested"
  - "Future: Fully automate with scheduled AI agent"
```

**Estimated Time:** 45 minutes

---

## 5. Implementation Timeline

### Week 1: TASK_MANAGERS Infrastructure (2.5 hours)
**Monday-Tuesday:**
- Create 3 input specification YAML files (1.75 hours)
- Create Department_Report_Gap_Extraction_Workflow.yaml (45 minutes)
- Test YAML syntax and structure

**Deliverables:** 4 YAML files in TASK_MANAGERS

---

### Week 2: Task Templates (2 hours)
**Wednesday-Thursday:**
- Create 4 task template JSON files (2 hours total)
  - TASK-TEMPLATE-023: Phase_0_Weekly_Analysis (30 min)
  - TASK-TEMPLATE-024: Department_Report_Review (20 min)
  - TASK-TEMPLATE-025: Research_Assignment_Creation (30 min)
  - TASK-TEMPLATE-026: Research_Quality_Review (45 min)
- Test JSON syntax and structure

**Deliverables:** 4 JSON files in TASK_MANAGERS

---

### Week 3: Testing & Documentation (30 minutes)
**Friday:**
- Test: Run gap extraction workflow manually with PMT-094
- Test: Use Phase 0 task template for Monday analysis
- Update: Research_System_Weekly_Cycle_Workflow.yaml to reference new input specs
- Document: Add notes to IMPLEMENTATION_LOG.md

**Deliverables:** Tested workflow, updated documentation

---

## 6. Success Metrics

### Immediate Success (Week 1-2)
- ✅ 8 new files created in TASK_MANAGERS
- ✅ Input specifications clearly define data sources
- ✅ Task templates provide step-by-step guidance
- ✅ Gap extraction workflow documented

### Short-term Success (Week 3-4)
- ✅ Gap extraction workflow used in Monday Phase 0
- ✅ Phase 0 task template used for weekly analysis
- ✅ Assignment creation follows task template
- ✅ Quality review uses standardized rubric

### Long-term Success (Month 2-3)
- ✅ 30-45 minutes saved per week (automated gap extraction)
- ✅ Consistent research assignment quality
- ✅ All 8 departments' research needs captured systematically
- ✅ Phase 0 analysis time reduced from 90 to 60 minutes

---

## 7. Integration Points

### How This Fits with Existing Research System

**Current State (Phase 1 Complete):**
```
Department Reports → Manual Phase 0 Analysis → Research Assignments
```

**New State (After Implementation):**
```
Department Reports → Gap Extraction Workflow → Weekly Gap Analysis Document
                                                        ↓
                                         Phase 0 Analysis (with structured input)
                                                        ↓
                                         Research Assignment Creation (with template)
                                                        ↓
                                         Quality Review (with rubric template)
```

**Key Improvements:**
1. **Structured Input:** Phase 0 has clear input specification (no guesswork)
2. **Automated Gap Extraction:** 30-45 minutes saved per week
3. **Consistent Process:** Task templates ensure same quality every week
4. **Quality Assurance:** Standardized 100-point rubric for all reviews
5. **Audit Trail:** TASK_MANAGERS has formal workflow definitions

---

## 8. Future Enhancements (Phase 3+)

### Automation Opportunities
1. **Automated Gap Extraction:** Schedule AI agent to run Monday 8:00 AM
2. **Auto-Assignment Matching:** AI suggests employee matches based on history
3. **Auto-Notification:** Trigger Discord/Email notifications when assignments created
4. **Dashboard:** Visual dashboard showing research pipeline status

### Integration Expansions
1. **TALENTS Integration:** Link employee research performance to TALENTS profiles
2. **Project Tracking:** Link research assignments to project milestones
3. **ROI Tracking:** Measure time saved by LIBRARIES growth from research
4. **Predictive Analysis:** Predict future research needs based on patterns

---

## Files Summary

| # | File Location | Type | Purpose | Est. Time |
|---|---------------|------|---------|-----------|
| 1 | TSM-006_Workflows/INPUTS/Phase_0_Analysis_Input_Spec.yaml | YAML | Phase 0 input definition | 30 min |
| 2 | TSM-006_Workflows/INPUTS/Research_Task_Creation_Input.yaml | YAML | Assignment creation spec | 30 min |
| 3 | TSM-006_Workflows/INPUTS/Department_Report_Gap_Extraction_Input.yaml | YAML | Gap extraction spec | 45 min |
| 4 | TSM-003_Task_Templates/TASK-TEMPLATE-023_Phase_0_Weekly_Analysis.json | JSON | Monday Phase 0 template | 30 min |
| 5 | TSM-003_Task_Templates/TASK-TEMPLATE-024_Department_Report_Review.json | JSON | Daily review template | 20 min |
| 6 | TSM-003_Task_Templates/TASK-TEMPLATE-025_Research_Assignment_Creation.json | JSON | Tuesday assignment template | 30 min |
| 7 | TSM-003_Task_Templates/TASK-TEMPLATE-026_Research_Quality_Review.json | JSON | Quality review template | 45 min |
| 8 | TSM-006_Workflows/Department_Report_Gap_Extraction_Workflow.yaml | YAML | Gap extraction workflow | 45 min |

**Total Estimated Time:** 3 hours 45 minutes

---

## Next Steps After Plan Approval

1. **Create INPUTS/ folder** in TASK_MANAGERS/TSM-006_Workflows/
2. **Create 3 input specification YAML files** (Files 1-3)
3. **Create 4 task template JSON files** (Files 4-7)
4. **Create gap extraction workflow YAML** (File 8)
5. **Test gap extraction workflow** with PMT-094 prompt
6. **Update IMPLEMENTATION_LOG.md** with Phase 2 progress
7. **Document integration** in Research_System_Weekly_Cycle_Workflow.yaml

---

**Plan Status:** Ready for Implementation
**Approval Required:** Yes
**Implementation Phase:** Phase 2 (Research System Activation)
**Dependencies:** Phase 1 Complete ✅
