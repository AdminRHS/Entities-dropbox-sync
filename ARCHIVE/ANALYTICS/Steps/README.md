# Steps Entity Documentation

**Entity Type:** TASK_MANAGERS  
**Sub-Entity:** Steps  
**Domain:** Task Management System  
**Purpose:** Actual step instances with tracking data, assignments, and completion status  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025

---

## 📋 Overview

**Steps** are actual work instances created from Step Templates. While Step Templates define reusable blueprints, Steps represent real work being executed with specific assignments, order within tasks, completion tracking, and checklist items.

**Key Characteristics:**
- **Instance-Based:** Created from Step Templates but with actual execution data
- **Task-Bound:** Belong to specific Tasks within Projects
- **Ordered:** Have execution order within their parent Task
- **Assigned:** Include actual assignee (user)
- **Tracked:** Monitor completion status and timestamps
- **Contextual:** Belong to specific entities and tasks

---

## 🔍 Definition

**Step:** An actual work instance created from a Step Template, with real execution data including order, assignment, completion status, and checklist items.

**Key Distinction:**
- **Step Template** = Reusable blueprint (structure only, no assignments/tracking)
- **Step** = Actual work instance (with assignments, order, status, completion tracking)

---

## 🆚 Steps vs. Step Templates

### Step Template (Blueprint)
- **Purpose:** Define reusable step structure
- **Contains:** Action, object, tool, description, planned hours
- **No Tracking:** No assignments, no completion status, no dates
- **Reusable:** One template creates many steps
- **Static:** Structure doesn't change during execution
- **Example:** "Edit Video Interview Footage Template" (blueprint)

### Step (Instance)
- **Purpose:** Execute actual work
- **Contains:** Real assignment, order, completion status, checklist items
- **Full Tracking:** Assignee, completion flag, completion timestamp
- **Unique:** Each step is a separate instance within a task
- **Dynamic:** Status and completion update during execution
- **Example:** "Edit Video Interview Footage" (actual step in Task PROJ-HR-001-001)

### Relationship

```
Step Template: "Edit Video Interview Footage"
    ↓ (instantiate within task)
Step Instance 1: (in Task PROJ-HR-001-001)
    - Order: 1
    - Assignee: Video Editor (user_id: 456)
    - Status: Completed
    - Completed At: 2025-01-15 14:30:00
    
Step Instance 2: (in Task PROJ-HR-001-002)
    - Order: 1
    - Assignee: Video Editor (user_id: 456)
    - Status: In Progress
    - Completed At: null
```

---

## 📐 Structure

### Step JSON Structure

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Step",
  "step_id": "STEP-{TASK_ID}-{NUMBER}",
  "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001",
  "name": "Edit Video Interview Footage",
  "metadata": {
    "order": 1,
    "is_completed": false,
    "completed_at": null,
    "created_at": "2025-01-15T10:00:00Z",
    "updated_at": "2025-01-15T10:00:00Z"
  },
  "assignment": {
    "assignee_id": 456,
    "assignee_name": "Video Editor",
    "assignee_role": "Video Editor"
  },
  "context": {
    "task_id": "TASK-PROJ-HR-001-001",
    "task_name": "Produce Employee Interview Video",
    "project_id": "PROJ-HR-001",
    "project_name": "Recruit Frontend Developer",
    "entity_id": 5,
    "entity_name": "HR Department"
  },
  "template_reference": {
    "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001",
    "step_template_name": "Edit Video Interview Footage",
    "action_id": 23,
    "action_name": "Edit",
    "object_id": 45,
    "object_name": "Video Interview",
    "tool_id": 12,
    "tool_name": "Video Editing Software",
    "hours_planned": "02:00:00"
  },
  "execution": {
    "actual_hours": null,
    "started_at": null,
    "completed_at": null,
    "notes": null
  },
  "checklist_items": [
    {
      "checklist_item_id": 1,
      "name": "Import raw footage",
      "is_completed": false,
      "is_correct": null,
      "order": 1
    },
    {
      "checklist_item_id": 2,
      "name": "Trim unnecessary sections",
      "is_completed": false,
      "is_correct": null,
      "order": 2
    },
    {
      "checklist_item_id": 3,
      "name": "Add transitions",
      "is_completed": false,
      "is_correct": null,
      "order": 3
    }
  ],
  "source_tracking": {
    "created_from_template": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001",
    "template_version": "1.0",
    "created_date": "2025-01-15"
  }
}
```

---

## 📂 File Organization

### Naming Convention

**File Format:** `STEP-{TASK_ID}-{NUMBER}.json` or `STEP-{TASK_ID}-{NUMBER}_{Step_Name}.json`

**Examples:**
- `STEP-TASK-PROJ-HR-001-001-001.json` - First step of first task in HR project
- `STEP-TASK-PROJ-HR-001-001-001_Edit_Video_Footage.json` - With descriptive name
- `STEP-TASK-PROJ-SALES-001-002-003.json` - Third step of second task in Sales project

### Directory Structure

```
Steps/
├── README.md                                    # This file
├── STEP-TASK-PROJ-HR-001-001-001.json         # Step instance
├── STEP-TASK-PROJ-HR-001-001-002.json         # Step instance
├── [Task_ID]/                                  # Optional: Organize by task
│   ├── STEP-TASK-PROJ-HR-001-001-001.json
│   └── STEP-TASK-PROJ-HR-001-001-002.json
└── [Project_ID]/                               # Optional: Organize by project
    └── [Task_ID]/
        └── STEP-*.json
```

---

## 🔗 Relationships

### Steps ↔ Step Templates

- **Many-to-One:** Multiple Steps can be created from one Step Template
- **Reference:** Steps reference their source template via `step_template_id`
- **Inheritance:** Steps inherit structure from templates but add execution data

```
Step Template (TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001)
    ↓
Step 1 (in Task PROJ-HR-001-001) - Jan 2025
Step 2 (in Task PROJ-HR-001-002) - Feb 2025
Step 3 (in Task PROJ-SALES-001-001) - Mar 2025
```

### Steps ↔ Tasks

- **Belongs To:** Steps belong to specific Tasks
- **Ordered:** Steps have order within their parent Task
- **Tracking:** Steps track completion within Task context

### Steps ↔ Users

- **Assigned To:** Steps have assigned users (assignees)
- **Completion:** Users mark steps as complete
- **Tracking:** Track who completed each step

### Steps ↔ Entities

- **Belongs To:** Steps belong to specific Entities (departments, clients)
- **Context:** Entity provides business context for step

### Steps ↔ Checklist Items

- **Has Many:** Steps contain checklist items
- **Tracking:** Checklist items track detailed completion within steps

---

## 🎯 Step Lifecycle

### Status Flow

```
Not Started (is_completed = false, completed_at = null)
    ↓ (start work)
In Progress (is_completed = false, assignee working)
    ↓ (complete)
Completed (is_completed = true, completed_at = timestamp)
```

### Completion Tracking

1. **Not Started**
   - `is_completed`: false
   - `completed_at`: null
   - Checklist items: All incomplete

2. **In Progress**
   - `is_completed`: false
   - `completed_at`: null
   - Checklist items: Some complete, some incomplete
   - Assignee actively working

3. **Completed**
   - `is_completed`: true
   - `completed_at`: timestamp
   - Checklist items: All complete (or marked as complete)

---

## 💡 Creating Steps from Templates

### Step-by-Step Process

1. **Select Template**
   - Choose appropriate Step Template
   - Verify template is Active (not Draft)

2. **Identify Parent Task**
   - Steps must belong to a Task
   - Get Task ID and context

3. **Set Order**
   - Determine step order within task
   - Consider dependencies from template

4. **Assign User**
   - Assign step to appropriate user
   - Set assignee_id

5. **Instantiate Structure**
   - Create Step from Step Template
   - Copy template structure (action, object, tool, description)
   - Initialize tracking fields

6. **Initialize Checklist**
   - Create checklist items from template (if applicable)
   - Set all items to incomplete

7. **Begin Execution**
   - Set status to "In Progress" (implicitly)
   - Start working on checklist items
   - Update progress

8. **Complete Step**
   - Complete all checklist items
   - Set `is_completed` to true
   - Set `completed_at` timestamp

### Example: Creating Step from Template

```json
// Step 1: Select Template
"step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001"

// Step 2: Identify Parent Task
"task_id": "TASK-PROJ-HR-001-001",
"task_name": "Produce Employee Interview Video"

// Step 3: Set Order
"order": 1

// Step 4: Assign User
"assignee_id": 456,
"assignee_name": "Video Editor"

// Step 5: Instantiate Structure
// (System automatically copies from template)

// Step 6: Initialize Checklist
"checklist_items": [
  {"name": "Import raw footage", "is_completed": false},
  {"name": "Trim sections", "is_completed": false},
  {"name": "Add transitions", "is_completed": false}
]

// Step 7: Begin Execution
// (Status implicitly "In Progress")

// Step 8: Complete Step
"is_completed": true,
"completed_at": "2025-01-15T14:30:00Z"
```

---

## 📊 Step Tracking

### Order Tracking

- **Order:** Position within parent Task (1, 2, 3, ...)
- **Dependencies:** Steps may depend on previous steps
- **Parallel Steps:** Multiple steps can execute in parallel

### Assignment Tracking

- **Assignee:** User assigned to complete the step
- **Assignment Date:** When step was assigned
- **Completion:** Who completed the step (via completed_at)

### Completion Tracking

- **Completion Flag:** `is_completed` boolean
- **Completion Timestamp:** `completed_at` timestamp
- **Checklist Progress:** Track completion via checklist items
- **Actual Hours:** Time spent (if tracked)

### Checklist Tracking

- **Checklist Items:** Detailed sub-tasks within step
- **Item Completion:** Each item can be marked complete
- **Item Validation:** Items can be marked as correct/incorrect
- **Order:** Checklist items have execution order

---

## 💡 Examples

### Example 1: Video Editing Step

**Created From:** TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001 (Edit Video Interview Footage)

```json
{
  "step_id": "STEP-TASK-PROJ-HR-001-001-001",
  "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001",
  "name": "Edit Video Interview Footage",
  "order": 1,
  "task_id": "TASK-PROJ-HR-001-001",
  "assignee_id": 456,
  "assignee_name": "Video Editor",
  "is_completed": true,
  "completed_at": "2025-01-15T14:30:00Z",
  "checklist_items": [
    {"name": "Import raw footage", "is_completed": true, "order": 1},
    {"name": "Trim unnecessary sections", "is_completed": true, "order": 2},
    {"name": "Add transitions", "is_completed": true, "order": 3}
  ]
}
```

### Example 2: Job Posting Step

**Created From:** TEMPLATE-STEP-TEMPLATE-TASK-001-001 (Select Job Template)

```json
{
  "step_id": "STEP-TASK-PROJ-HR-002-001-001",
  "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-001-001",
  "name": "Select Job Template",
  "order": 1,
  "task_id": "TASK-PROJ-HR-002-001",
  "assignee_id": 123,
  "assignee_name": "HR Manager",
  "is_completed": false,
  "completed_at": null,
  "checklist_items": [
    {"name": "Open CRM", "is_completed": true, "order": 1},
    {"name": "Navigate to Job Templates", "is_completed": true, "order": 2},
    {"name": "Select appropriate template", "is_completed": false, "order": 3}
  ]
}
```

### Example 3: Email Sending Step

**Created From:** TEMPLATE-STEP-TEMPLATE-TASK-002-001 (Draft Email)

```json
{
  "step_id": "STEP-TASK-PROJ-SALES-001-002-001",
  "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-002-001",
  "name": "Draft Follow-up Email",
  "order": 1,
  "task_id": "TASK-PROJ-SALES-001-002",
  "assignee_id": 234,
  "assignee_name": "Sales Manager",
  "is_completed": true,
  "completed_at": "2025-01-20T11:15:00Z",
  "checklist_items": [
    {"name": "Research client history", "is_completed": true, "order": 1},
    {"name": "Personalize email content", "is_completed": true, "order": 2},
    {"name": "Review and approve", "is_completed": true, "order": 3}
  ]
}
```

---

## 🔄 Integration with Other Entities

### Steps → Step Templates

Steps reference Step Templates:

```json
{
  "step_template_id": "TEMPLATE-STEP-TEMPLATE-TASK-HR-003-001",
  "template_reference": {
    "action_id": 23,
    "object_id": 45,
    "tool_id": 12,
    "hours_planned": "02:00:00"
  }
}
```

### Steps → Tasks

Steps belong to Tasks:

```json
{
  "task_id": "TASK-PROJ-HR-001-001",
  "task_name": "Produce Employee Interview Video",
  "order": 1
}
```

### Steps → Checklist Items

Steps contain Checklist Items:

```json
{
  "checklist_items": [
    {
      "checklist_item_id": 1,
      "name": "Import raw footage",
      "is_completed": true,
      "order": 1
    }
  ]
}
```

---

## 📈 Step Metrics and Reporting

### Key Metrics

1. **Completion Metrics**
   - Completion rate (completed vs. total)
   - Average time to complete
   - Checklist item completion rate

2. **Performance Metrics**
   - Actual vs. planned hours
   - Steps completed per day/week
   - Steps per task average

3. **Assignment Metrics**
   - Steps per assignee
   - Completion rate by assignee
   - Workload distribution

### Reporting

- **Step Dashboard:** Real-time step status
- **Completion Reports:** Step completion tracking
- **Performance Reports:** Actual vs. planned analysis
- **Assignee Reports:** Individual step contributions

---

## 🎯 Best Practices

### Step Creation

1. **Use Templates:** Always start from appropriate Step Template
2. **Set Correct Order:** Ensure step order matches dependencies
3. **Assign Appropriately:** Match assignee to step requirements
4. **Initialize Checklist:** Set up checklist items from template
5. **Document Context:** Include all relevant context

### Step Execution

1. **Follow Order:** Execute steps in order (unless parallel)
2. **Update Checklist:** Mark checklist items as you complete them
3. **Track Progress:** Update step status regularly
4. **Document Issues:** Note any problems or blockers
5. **Complete Thoroughly:** Ensure all checklist items done before marking complete

### Step Completion

1. **Verify Checklist:** Ensure all checklist items complete
2. **Set Completion Time:** Record accurate completion timestamp
3. **Update Status:** Set `is_completed` to true
4. **Document Results:** Note any outcomes or deliverables
5. **Move to Next:** Proceed to next step in task

---

## 🔍 Step Discovery

### Finding Steps

1. **By Task:** Find all steps for a specific task
2. **By Template:** Find all steps created from a template
3. **By Assignee:** Find all steps assigned to a user
4. **By Status:** Find steps by completion status
5. **By Project:** Find all steps within a project

### Step Search

- **By Name:** Search step names
- **By ID:** Find step by ID (STEP-XXX-###)
- **By Task:** Search by parent task ID
- **By Assignee:** Search by assignee name/ID
- **By Status:** Filter by completion status

---

## 📚 Related Documentation

### Internal References

- **Step Templates:** `../Step_Templates/README.md` - Template blueprints
- **Tasks:** `../Tasks/README.md` - Parent task instances
- **Task Templates:** `../Task_Templates/README.md` - Task template blueprints
- **Projects:** `../Projects/README.md` - Project instances

### External References

- **Task Manager Database Structure:** `SummariesOct/INFRASTRUCTURE/ENTITIES/TASK_MANAGERS/TASK_MANAGER_DATABASE_STRUCTURE.md`
- **TASK_MANAGERS Index:** `../INDEX.md`
- **Step Templates Listing:** `../Step_Templates_Listing.md`

---

## 🚀 Future Enhancements

### Planned Features

1. **Step Analytics:** Advanced analytics and reporting
2. **Time Tracking:** Automatic time tracking integration
3. **Dependency Management:** Visual dependency tracking
4. **Parallel Execution:** Enhanced parallel step support
5. **Step Templates:** AI-assisted step template suggestions

### Integration Opportunities

1. **Calendar Integration:** Sync step deadlines with calendars
2. **Notification Integration:** Step assignment and completion notifications
3. **Document Management:** Link steps to documents and deliverables
4. **Time Tracking:** Automatic time tracking for steps
5. **Reporting Integration:** Export to reporting systems

---

## 📝 Notes

- Steps are **instances**, not templates
- Steps track **actual execution**, not just structure
- Steps have **real assignments, order, and completion status**
- Steps can be created **manually** or **from templates**
- Steps should be **regularly updated** during execution
- Completed steps provide **data for template improvement**

---

## 🔗 Related Entities

- **Step Templates** (`../Step_Templates/`) - Blueprints used to create steps
- **Tasks** (`../Tasks/`) - Parent tasks that contain steps
- **Task Templates** (`../Task_Templates/`) - Task templates that reference step templates
- **Projects** (`../Projects/`) - Projects that contain tasks with steps
- **Users** (via assignments) - Team members assigned to steps
- **Entities** (`../../ENTITIES/`) - LIBRARIES/DEPARTMENTS/clients steps belong to

---

**Last Updated:** November 25, 2025  
**Document Version:** 1.0

