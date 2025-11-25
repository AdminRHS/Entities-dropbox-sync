# Templates vs Instances in TASK_MANAGERS

**Created:** November 25, 2025  
**Purpose:** Explain the difference between Templates and Instances

---

## 🎯 Key Concept

**Templates** = Reusable blueprints (definitions)  
**Instances** = Actual work being executed (with tracking data)

---

## 📋 Template vs Instance

### Template (Blueprint)

**What it is:**
- A reusable definition/blueprint
- Defines structure, steps, and requirements
- No tracking data (no assignments, no completion dates)
- Can be used to create multiple instances

**Characteristics:**
- ✅ Structure and definition
- ✅ Reusable across many projects/tasks
- ❌ No assignments
- ❌ No completion tracking
- ❌ No dates or status

**Example:**
```json
{
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "step_template_name": "Edit Video Interview Footage",
  "description": "Edit raw video footage for interview",
  "expected_duration": 120,
  "checklist_items": ["CHK-099", "CHK-100", "Checklist-Item-001"]
}
```

---

### Instance (Actual Work)

**What it is:**
- Actual work being executed
- Created from a template
- Has tracking data (assignments, completion status, dates)
- Unique to a specific project/task

**Characteristics:**
- ✅ Created from a template
- ✅ Has real assignments (who is doing it)
- ✅ Has completion tracking (is_completed, completed_at)
- ✅ Has dates (start_date, due_date)
- ✅ Has status (pending, in_progress, completed)
- ✅ Unique to specific project/task

**Example:**
```json
{
  "step_id": "STEP-TASK-PROJ-HR-001-001-001",
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "name": "Edit Video Interview Footage",
  "task_id": "TASK-PROJ-HR-001-001",
  "assignee_id": 456,
  "assignee_name": "Video Editor",
  "is_completed": true,
  "completed_at": "2025-01-15T14:30:00Z",
  "checklist_items": [
    {"checklist_item_id": "CHK-099", "order": 1, "is_completed": true},
    {"checklist_item_id": "CHK-100", "order": 2, "is_completed": true},
    {"checklist_item_id": "Checklist-Item-001", "order": 3, "is_completed": false}
  ]
}
```

---

## 🔄 How They Work Together

### The Process

1. **Create Template** (once)
   ```
   Step Template: "Edit Video Interview Footage"
   - Defines what needs to be done
   - Lists Checklist Items
   - Estimates duration
   ```

2. **Create Instance** (many times, from template)
   ```
   Step Instance 1: (in Task PROJ-HR-001-001)
   - Created from template
   - Assigned to Video Editor
   - Status: Completed
   
   Step Instance 2: (in Task PROJ-HR-001-002)
   - Created from same template
   - Assigned to Video Editor
   - Status: In Progress
   ```

---

## 📊 Hierarchy Examples

### Template Hierarchy (in TASK_MANAGERS)
```
Location: ENTITIES/TASK_MANAGERS/

Project_Template: "HR Automation"
  └── Milestone_Template: "CV Screening"
      └── Task_Template: "Process CVs"
          └── Step_Template: "Analyze CV"
              └── Checklist Item: "Import CV file"
```

**This is a blueprint** - defines structure, no tracking.  
**Stored in:** `ENTITIES/TASK_MANAGERS/Project_Templates/`, `Task_Templates/`, `Step_Templates/`

---

### Instance Hierarchy (in ANALYTICS)
```
Location: ENTITIES/ANALYTICS/

Project Instance: PROJ-HR-001
  └── Milestone Instance: MIL-PROJ-HR-001-001
      └── Task Instance: TASK-PROJ-HR-001-001
          └── Step Instance: STEP-TASK-PROJ-HR-001-001-001
              └── Checklist Item: "Import CV file" (completed ✓)
```

**This is actual work** - has assignments, dates, completion status.  
**Stored in:** `ENTITIES/ANALYTICS/Projects/`, `Tasks/`, `Steps/`

---

## 🎨 Visual Comparison

### Template (Blueprint)
```
┌─────────────────────────────────────┐
│ Step Template                        │
│ "Edit Video Interview Footage"       │
│                                      │
│ ✓ Structure defined                  │
│ ✓ Checklist Items listed             │
│ ✓ Duration estimated                 │
│                                      │
│ ✗ No assignee                        │
│ ✗ No completion date                 │
│ ✗ No status                          │
└─────────────────────────────────────┘
```

### Instance (Actual Work)
```
┌─────────────────────────────────────┐
│ Step Instance                        │
│ "Edit Video Interview Footage"       │
│                                      │
│ ✓ Created from template              │
│ ✓ Assigned to: Video Editor          │
│ ✓ Status: Completed                  │
│ ✓ Completed: 2025-01-15 14:30        │
│                                      │
│ Checklist Items:                     │
│   ✓ Import footage                   │
│   ✓ Trim sections                    │
│   ⏳ Add transitions                 │
└─────────────────────────────────────┘
```

---

## 📝 Checklist Items: Template vs Instance

### Checklist Item in Template
```json
{
  "checklist_item_id": "CHK-099",
  "item_name": "Import raw footage",
  "associated_step": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "item_type": "substep",
  "order": 1
}
```
**Purpose:** Defines what should be done (blueprint)

---

### Checklist Item in Instance
```json
{
  "checklist_item_id": "CHK-099",
  "item_name": "Import raw footage",
  "associated_step": "STEP-TASK-PROJ-HR-001-001-001",
  "item_type": "substep",
  "order": 1,
  "is_completed": true,
  "completed_at": "2025-01-15T10:00:00Z",
  "completed_by": 456
}
```
**Purpose:** Tracks actual completion (execution)

---

## 📁 Storage Locations

### Templates
**Location:** `ENTITIES/TASK_MANAGERS/`
- `Project_Templates/` - Project Template definitions
- `Task_Templates/` - Task Template definitions  
- `Step_Templates/` - Step Template definitions
- `Milestone_Templates/` - Milestone Template definitions

### Instances
**Location:** `ENTITIES/ANALYTICS/`
- `Projects/` - Project instances with execution data
- `Tasks/` - Task instances with execution data
- `Steps/` - Step instances with execution data
- `Milestones/` - Milestone instances with execution data

---

## ✅ Summary

| Aspect | Template | Instance |
|--------|----------|----------|
| **Purpose** | Define structure | Execute work |
| **Location** | `TASK_MANAGERS/` | `ANALYTICS/` |
| **Reusability** | Used many times | Unique to one project/task |
| **Assignments** | ❌ None | ✅ Real people assigned |
| **Completion** | ❌ Not tracked | ✅ Tracked (is_completed, dates) |
| **Status** | ❌ Static | ✅ Dynamic (changes over time) |
| **Dates** | ❌ None | ✅ Start date, due date, completion date |
| **ID Format** | `TEMPLATE-*` | `PROJ-*`, `TASK-*`, `STEP-*` |

**Think of it like:**
- **Template** = Recipe (how to make a cake) - stored in recipe book (`TASK_MANAGERS`)
- **Instance** = Actual cake being made (with specific ingredients, baker, completion time) - stored in kitchen log (`ANALYTICS`)

---

**Last Updated:** November 25, 2025

