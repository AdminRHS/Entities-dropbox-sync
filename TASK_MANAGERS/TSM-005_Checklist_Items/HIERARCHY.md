# Checklist Items in TASK_MANAGERS Hierarchy

**Created:** November 25, 2025  
**Purpose:** Clarify where Checklist Items fit in the TASK_MANAGERS hierarchy

---

## 📊 Complete Hierarchy

### Template Hierarchy

```
Project_Template
  └── Milestone_Template
      └── Task_Template
          └── Step_Template
              └── Checklist Item (substep) ← Can be here
      
Project_Template/Milestone_Template Level
  └── Checklist Item (deliverable) ← Can be here
```

### Instance Hierarchy

```
Location: ENTITIES/ANALYTICS/

Project Instance
  └── Milestone Instance
      └── Task Instance
          └── Step Instance
              └── Checklist Item (substep) ← Can be here
      
Project Instance/Milestone Instance Level
  └── Checklist Item (deliverable) ← Can be here
```

**Note:** Checklist Items can be associated with either Templates (blueprints) or Instances (actual work), depending on whether they define reusable structure or track actual execution.

**Storage Locations:**
- **Templates** → `ENTITIES/TASK_MANAGERS/` (blueprints)
- **Instances** → `ENTITIES/ANALYTICS/` (actual work with tracking)

**What is an Instance?**
- **Template** = Reusable blueprint (defines structure, no tracking) - stored in `TASK_MANAGERS`
- **Instance** = Actual work being executed (has assignments, completion tracking, dates) - stored in `ANALYTICS`
- See `TEMPLATES_VS_INSTANCES.md` for detailed explanation

---

## 🎯 Two Types of Checklist Items

### 1. Deliverables (Project/Milestone Level)

**Purpose:** Track outputs that must be produced for a project or milestone

**Association:**
- `associated_project` - Required (Project Template ID or Project Instance ID)
- `associated_milestone` - Optional (Milestone Template ID or Milestone Instance ID)
- `associated_task` - Optional (Task Template ID or Task Instance ID)
- `associated_step` - Not used for deliverables

**Example (Template Level):**
```json
{
  "checklist_item_id": "CHK-044",
  "item_name": "n8n workflow: Gmail → Gemini AI → Google Sheets",
  "associated_project": "Project-Template-003",
  "associated_milestone": "MIL-TEMPLATE-PROJ-HR-002-001",
  "item_type": "deliverable"
}
```

**Usage in Milestone Template:**
```json
{
  "milestone_template_id": "MIL-TEMPLATE-PROJ-HR-002-001",
  "milestone_template_name": "CV Screening Automation",
  "checklist_items": ["CHK-044", "CHK-045", "CHK-046"]
}
```

**Usage in Milestone Instance:**
```json
{
  "milestone_id": "MIL-PROJ-HR-002-001",
  "milestone_template_id": "MIL-TEMPLATE-PROJ-HR-002-001",
  "checklist_items": ["CHK-044", "CHK-045", "CHK-046"]
}
```

---

### 2. Substeps (Step Level)

**Purpose:** Track detailed actions within a step's execution

**Association:**
- `associated_step` - Required (Step Template ID or Step Instance ID)
- `associated_task` - Optional (Task Template ID or Task Instance ID, for context)
- `associated_project` - Optional (Project Template ID or Project Instance ID, for context)
- `associated_milestone` - Optional (Milestone Template ID or Milestone Instance ID, for context)

**Example (Template Level):**
```json
{
  "checklist_item_id": "CHK-099",
  "item_name": "Import raw footage",
  "associated_step": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "associated_task": "TASK-TEMPLATE-HR-003",
  "item_type": "substep",
  "order": 1
}
```

**Usage in Step Template:**
```json
{
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "step_template_name": "Edit Video Interview Footage",
  "checklist_items": [
    {"checklist_item_id": "CHK-099", "order": 1},
    {"checklist_item_id": "CHK-100", "order": 2},
    {"checklist_item_id": "Checklist-Item-001", "order": 3}
  ]
}
```

**Usage in Step Instance:**
```json
{
  "step_id": "STEP-TASK-PROJ-HR-001-001-001",
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001",
  "name": "Edit Video Interview Footage",
  "checklist_items": [
    {"checklist_item_id": "CHK-099", "order": 1, "is_completed": true},
    {"checklist_item_id": "CHK-100", "order": 2, "is_completed": true},
    {"checklist_item_id": "Checklist-Item-001", "order": 3, "is_completed": false}
  ]
}
```

---

## 🔄 Relationship to Steps

### Step Instances Include Checklist Items

When a Step is instantiated from a Step Template, it can include Checklist Items as substeps:

```json
{
  "step_id": "STEP-TASK-PROJ-HR-002-001-001",
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-001-001",
  "name": "Select Job Template",
  "order": 1,
  "task_id": "TASK-PROJ-HR-002-001",
  "assignee_id": 123,
  "is_completed": false,
  "checklist_items": [
    {
      "checklist_item_id": "CHK-102",
      "name": "Open CRM",
      "is_completed": true,
      "order": 1
    },
    {
      "checklist_item_id": "CHK-103",
      "name": "Navigate to Job Templates",
      "is_completed": true,
      "order": 2
    },
    {
      "checklist_item_id": "CHK-104",
      "name": "Select appropriate template",
      "is_completed": false,
      "order": 3
    }
  ]
}
```

---

## 📝 Field Usage by Type

### Deliverable Checklist Items
- ✅ `associated_project` - Required
- ✅ `associated_milestone` - Usually present
- ❌ `associated_step` - Not used
- ✅ `item_type: "deliverable"`

### Substep Checklist Items
- ✅ `associated_step` - Required
- ✅ `associated_task` - Usually present (for context)
- ✅ `order` - Required (execution order within step)
- ✅ `item_type: "substep"`

---

## 🎨 Visual Representation

### Template Level
```
┌─────────────────────────────────────────────┐
│ Project_Template: HR Automation             │
│   └── Milestone_Template: CV Screening     │
│       └── Task_Template: Process CVs        │
│           └── Step_Template: Analyze CV     │
│               ├── CHK-099 (substep)         │
│               ├── CHK-100 (substep)         │
│               └── Checklist-Item-001 (substep)         │
│                                             │
│   └── Deliverables:                         │
│       ├── CHK-044 (deliverable)             │
│       └── CHK-045 (deliverable)             │
└─────────────────────────────────────────────┘
```

### Instance Level (in ANALYTICS)
```
Location: ENTITIES/ANALYTICS/

┌─────────────────────────────────────────────┐
│ Project Instance: PROJ-HR-001              │
│   └── Milestone Instance: MIL-PROJ-HR-001-001│
│       └── Task Instance: TASK-PROJ-HR-001-001│
│           └── Step Instance: STEP-...-001   │
│               ├── CHK-099 (substep) ✓       │
│               ├── CHK-100 (substep) ✓       │
│               └── Checklist-Item-001 (substep) ⏳      │
│                                             │
│   └── Deliverables:                         │
│       ├── CHK-044 (deliverable) ✓           │
│       └── CHK-045 (deliverable) ⏳           │
└─────────────────────────────────────────────┘
```

---

## ✅ Summary

**Checklist Items can be:**
1. **Deliverables** - Associated with Projects/Milestones (what gets delivered)
2. **Substeps** - Associated with Steps (detailed actions within steps)

**Both types can be associated with:**
- **Templates** (blueprints) - Define reusable structure - stored in `ENTITIES/TASK_MANAGERS/`
- **Instances** (actual work) - Track execution and completion - stored in `ENTITIES/ANALYTICS/`

**Both types:**
- Use the same `CHK-{ITEM_NUMBER}` ID format
- Can be tracked for completion
- Support status, required flags, and completion dates
- Are stored in the same Checklist_Items directory structure
- Can reference Template IDs or Instance IDs in association fields

**Key Differences:**
- **Deliverables** track **what** must be produced
- **Substeps** track **how** a step is executed
- **Templates** define structure (reusable blueprints)
- **Instances** track actual execution (with completion status)

---

**Last Updated:** November 25, 2025

