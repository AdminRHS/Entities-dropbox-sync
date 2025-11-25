# TASK_MANAGERS Entity Documentation

**Entity Type:** TASK_MANAGERS  
**Domain:** Operational Engine  
**Purpose:** Orchestrates work execution across departments and platforms  
**Created:** November 1, 2025  
**Last Updated:** November 17, 2025

> **📊 Migration Note (2025-11-17):** Analytics infrastructure (Projects, Tasks, Steps, and their templates) has been moved to the new **ANALYTICS** entity. TASK_MANAGERS now focuses on workflow definitions, guides, and prompts. See `ANALYTICS/README.md` for analytics-related resources.

---

## 📋 Overview

The TASK_MANAGERS entity domain orchestrates work execution across all departments and platforms. It eliminates decision fatigue through template-driven operations, enables accurate time estimation, supports capacity planning, tracks team velocity and productivity, and automates routine workflows.

---

## 🗂️ Sub-Entities

### 1. Project_Templates
**Purpose:** Template definitions for projects (project instances moved to ANALYTICS)

**Key Attributes:**
- Project Template structure
- Milestone definitions
- Task collections
- Department assignments

**Location:** `TASK_MANAGERS/Project_Templates/`

> **Note:** Project instances and execution tracking have been moved to `ANALYTICS/Projects/` (2025-11-17)

---

### 2. Milestone_Templates (workflow-derived)
**Purpose:** Milestone Template definitions that encode end-to-end workflows and automation rules in a template-friendly JSON format.

**Key Attributes:**
- Milestone name and description (often mapped from a prior workflow name).
- High-level workflow type (e.g., Linear, Parallel, Conditional, Event-Driven).
- Dependencies between milestones.
- Links to Task Templates and expected reports.
- Department assignment and success criteria.

**File Structure:**
```
Milestone_Templates/
├── Milestone-Template-001_Content_Analysis.json
├── Milestone-Template-002_Data_Inventory.json
├── Milestone-Template-003_Relationship_Validation.json
├── Milestone-Template-004_Schema_Naming_Validation.json
├── Milestone-Template-005_Synthesis_Recommendations.json
├── Milestone-Template-006_VIDEO-001_Research_Complete.json
├── Milestone-Template-007_VIDEO-002_Processing_Complete.json
├── Milestone-Template-008_VIDEO-003_Library_Population_Complete.json
├── Milestone-Template-009_Behance_Project_Publishing.json
├── Milestone-Template-010_Content_Repurposing_Pipeline.json
├── Milestone-Template-011_Cross_Platform_Content_Distribution.json
├── Milestone-Template-012_Dev_to_Technical_Blogging.json
├── Milestone-Template-013_Dribbble_Shot_Posting.json
├── Milestone-Template-014_Dribbble_Shot_Publishing.json
├── Milestone-Template-015_Facebook_Community_Management.json
├── Milestone-Template-016_GitHub_Open_Source_Contribution.json
├── Milestone-Template-017_Instagram_Content_Strategy.json
├── Milestone-Template-018_Instagram_Designer_Portfolio.json
├── Milestone-Template-019_Lead_Enrichment_Automation.json
├── Milestone-Template-020_LinkedIn_B2B_Content_Strategy.json
├── Milestone-Template-021_Medium_Long_Form_Publishing.json
├── Milestone-Template-022_Old_Client_Reengagement.json
├── Milestone-Template-023_Pinterest_Discovery_Strategy.json
├── Milestone-Template-024_Pinterest_Traffic_Generation.json
├── Milestone-Template-025_Short_Form_Video_Production.json
├── Milestone-Template-026_Stack_Overflow_Reputation_Building.json
├── Milestone-Template-027_Twitter_Real_Time_Engagement.json
└── Milestone-Template-028_YouTube_Tutorial_Production.json
```

---

### 3. Task_Templates (Reference)
**Purpose:** Task Template definitions (templates moved to ANALYTICS)

> **Note:** Task Templates and task instances have been moved to `ANALYTICS/Task_Templates/` and `ANALYTICS/Tasks/` respectively (2025-11-17). TASK_MANAGERS now contains workflow definitions and guides.

**Template Structure:**
```
Task Template = ACTION + OBJECT + CONTEXT
Example: "Create" + "Job Posting" + "for Frontend Developer"
```
    ├── Sales_Tasks/
    └── Dev_Tasks/
```

---

### 4. Tasks
**Purpose:** Individual work items with tracking data, template references, and assignments

**Key Attributes:**
- Tracking data (status, priority, start date, due date, time spent)
- Task Template reference (template-based or freestyle)
- Freestyle task name (custom title)
- Assignment structure (executor and controller)
- Project and milestone linkage
- Steps and sub-tasks

**Structure Components:**
1. **Tracking Data** - Status, priority, dates, completion
2. **Task Template Reference** - Link to template (or NULL for freestyle)
3. **Freestyle Task Name** - Custom title field

**File Structure:**
```
Tasks/
├── README.md          # Tasks entity documentation
├── Tasks.json         # Complete structure definition
└── [Task Instances]/  # Individual task files (as needed)
```

**See:** `Tasks/Tasks.json` for complete structure definition

---

### 5. Milestone_Tracking
**Purpose:** Project milestone management and progress

**Key Attributes:**
- Milestone name and description
- Project association
- Target date
- Actual completion date
- Status (Planned/In Progress/Completed/Delayed)
- Dependencies
- Deliverables
- Success criteria

**File Structure:**
```
Milestone_Tracking/
├── Project_Milestones/    # Project-specific milestones
└── Sprint_Goals/          # Sprint-based milestones
```

---

### 6. Performance_Metrics
**Purpose:** Individual and team performance data

**Key Attributes:**
- Employee ID or team name
- Task completion rate
- Average completion time
- Quality scores
- On-time delivery rate
- Capacity utilization
- Velocity (story points or tasks per sprint)
- Department performance comparison

**File Structure:**
```
Performance_Metrics/
├── Department_Dashboards/    # Department-level metrics
├── Individual_Performance/   # Employee-level metrics
└── Team_Velocity/           # Team productivity metrics
```

---

## 🔗 Relationships

### Primary Relationships

1. **TASK_MANAGERS ↔ TALENTS**
   - Employees assigned to tasks
   - Tasks require specific profession capabilities
   - Performance tracked through task completion

2. **TASK_MANAGERS ↔ LIBRARIES**
   - Tasks composed of Actions + Objects
   - Tasks require specific Tools
   - Tasks assigned based on Responsibilities

3. **TASK_MANAGERS ↔ JOBS**
   - Job posting creation tasks
   - Hiring workflow tasks
   - Talent matching tasks

4. **TASK_MANAGERS ↔ BUSINESSES**
   - Client onboarding tasks
   - Sales pipeline tasks
   - Customer support tasks

---

## 📊 Task Template Structure

### Complete Task Template Format

**Name:** `ACTION + OBJECT + CONTEXT`

**Components:**
1. **ACTION** - Standardized verb from Actions Library
   - Examples: Create, Update, Send, Analyze, Review, Approve, Generate, Process, Archive, Delete

2. **OBJECT** - Business entity from Objects Library
   - Examples: Job Posting, Client Proposal, Email Outreach, LinkedIn Message, Financial Report, Video CV

3. **CONTEXT** - Specific details or parameters
   - Examples: "for Frontend Developer", "with pricing revisions", "to warm leads"

**Complete Examples:**
- `Create` + `Job Posting` + `for Frontend Developer`
- `Update` + `Client Proposal` + `with pricing revisions`
- `Send` + `Follow-up Email` + `to warm leads`
- `Analyze` + `Lead Quality` + `from LinkedIn campaign`
- `Generate` + `Video CV` + `for React Developer`

---

## 📊 Example Queries

### Get Tasks for Department Requiring Specific Tool
```sql
-- Get all tasks for Lead Generation department requiring LinkedIn
SELECT tm.task_name, tm.status, tm.assigned_to
FROM Task_Managers tm
JOIN Tools tool ON tm.tool_id = tool.id
WHERE tm.department = 'LG'
  AND tool.name = 'LinkedIn'
  AND tm.status = 'Not Started'
```

### Track Employee Task Performance
```sql
-- Get task completion statistics for an employee
SELECT 
  COUNT(*) as total_tasks,
  SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed,
  AVG(completion_time) as avg_time,
  AVG(quality_score) as avg_quality
FROM Task_Managers
WHERE assigned_to = [EMPLOYEE_ID]
  AND created_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
```

---

## 📝 File Naming Convention

**Pattern:** `TASK_MANAGERS_[Type]_[Name]_[Date].ext`

**Examples:**
- `TASK_MANAGERS_Workflow_Lead_Generation_Automation_v2.yaml`
- `TASK_MANAGERS_Task_Task-Template-007.json`
- `TASK_MANAGERS_Milestone_Project_Launch_2025_02_01.md`

---

## 🔄 Workflow Automation Patterns

### Pattern 1: Linear Sequential Workflow
Each step depends on previous step completion.

```
Step 1 → Step 2 → Step 3 → Step 4 → Complete
```

**Example:** Job application processing
1. Application received → 2. Initial screening → 3. Technical assessment → 4. Interview scheduling → 5. Hired/Rejected

---

### Pattern 2: Parallel Processing Workflow
Multiple steps execute simultaneously.

```
Step 1 → [Step 2a, Step 2b, Step 2c] → Step 3
```

**Example:** Lead enrichment
1. Lead captured → [2a. Company research, 2b. Contact verification, 2c. Social profile matching] → 3. Lead scoring

---

### Pattern 3: Conditional Branching Workflow
Next step determined by outcome of previous step.

```
Step 1 → Decision Point → [Path A, Path B, Path C]
```

**Example:** Client response handling
1. Send proposal → 2. Receive response → [Path A: Interested → Schedule call, Path B: Not interested → Nurture sequence, Path C: No response → Follow-up]

---

### Pattern 4: Iterative Refinement Workflow
Loop back to previous steps for refinement.

```
Step 1 → Step 2 → Step 3 → Review → [Approved → Complete | Revisions needed → Step 2]
```

**Example:** Design project
1. Brief → 2. Wireframe → 3. Design mockup → 4. Client review → [Approved → Development | Revisions → Mockup refinement]

---

### Pattern 5: Event-Driven Workflow
Triggered by external events or conditions.

```
Event Trigger → Automated Response → Conditional Next Steps
```

**Example:** LinkedIn account warning
Event: LinkedIn account restriction detected → Automated response: Pause account, rotate to backup → Conditional: If 3rd restriction → Remove from active pool

---

## 📋 Metadata Template

Every Task Template file should include:

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Task_Template",
  "task_id": "TASK-2025-001",
  "task_name": "Create Job Posting for Frontend Developer",
  "action": "Create",
  "object": "Job Posting",
  "context": "for Frontend Developer",
  "description": "Create a new job posting for a Frontend Developer position",
  "department": "HR",
  "profession": "HR Manager",
  "estimated_duration": "2 hours",
  "status": "Template",
  "dependencies": [],
  "tools_required": ["Notion", "Google Docs"],
  "success_criteria": [
    "Job posting published on 3+ platforms",
    "All required fields completed",
    "Approved by hiring manager"
  ],
  "steps": [
    {
      "step_number": 1,
      "name": "Select job template",
      "tool": "Notion",
      "duration": "5 minutes"
    }
  ],
  "tags": ["hr", "recruitment", "job_posting"]
}
```

---

## 🎯 Business Value

- **Eliminates Decision Fatigue:** Template-driven approach removes guesswork
- **Accurate Time Estimation:** Historical data enables better planning
- **Capacity Planning:** Supports team workload balancing
- **Performance Tracking:** Measures team velocity and productivity
- **Workflow Automation:** Enables n8n automation integration

---

## 📚 Related Documents

### Internal Indexes
- **[INDEX.md](./INDEX.md)** - Master index of all templates, projects, and milestone templates
- **[TAXONOMY_GUIDELINES.md](./TAXONOMY_GUIDELINES.md)** - Taxonomy field usage and database mapping guidelines
- **[Tasks/Tasks.json](./Tasks/Tasks.json)** - ⭐ NEW: Complete Tasks entity structure definition (tracking data, templates, assignments, controller, dates)
- **[Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md)** - Complete listing of all Task Templates with IDs
- **[Project_Templates_Checklist-Item-003.md](./Project_Templates_Checklist-Item-003.md)** - Complete listing of all Project Templates with IDs
- **[Step_Templates_Checklist-Item-003.md](../ANALYTICS/Step_Templates/)** - Step Templates moved to ANALYTICS (2025-11-17)
- **[Projects_Checklist-Item-003.md](./Projects_Checklist-Item-003.md)** - Complete listing of all projects with IDs
- **[Milestone_Templates_Checklist-Item-003.md](./Milestone_Templates_Checklist-Item-003.md)** - Complete listing of all milestone templates with IDs

### Related Entities
- `../LIBRARIES/Actions/` - Action verb definitions
- `../LIBRARIES/Objects/` - Business object definitions
- `../LIBRARIES/Tools/` - Tool requirements
- `../LIBRARIES/Professions/` - Profession definitions
- `../TALENTS/` - Employee assignments
- `../JOBS/` - Job-related tasks
- `../BUSINESSES/` - Client-related tasks

---

**Last Updated:** November 25, 2025

