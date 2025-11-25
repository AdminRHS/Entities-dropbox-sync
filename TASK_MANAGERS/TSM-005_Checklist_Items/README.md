# Checklist Items (TASK_MANAGERS)

**Purpose:** Checklist Items represent deliverables, outputs, and completion criteria for projects, milestones, and tasks.

**Created:** November 25, 2025  
**Migration Source:** Deliverables from Project Templates and Project Instances

---

## 📋 Overview

Checklist Items are trackable deliverables and substeps that can be:
- **At Project/Milestone Level:** Deliverables (outputs of milestones/projects)
- **At Step Level:** Substeps (detailed actions within steps)
- Marked as complete/incomplete
- Linked to specific phases, milestones, tasks, or steps
- Used for validation and quality control

### Hierarchy Position

Checklist Items exist in the TASK_MANAGERS hierarchy at multiple levels:

**Template Hierarchy:**
```
Project_Template
  └── Milestone_Template
      └── Task_Template
          └── Step_Template
              └── Checklist Item (substep) ← Can be here
      
Project_Template/Milestone_Template
  └── Checklist Item (deliverable) ← Or here
```

**Instance Hierarchy:**
```
Location: ENTITIES/ANALYTICS/

Project Instance
  └── Milestone Instance
      └── Task Instance
          └── Step Instance
              └── Checklist Item (substep) ← Can be here
      
Project Instance/Milestone Instance
  └── Checklist Item (deliverable) ← Or here
```

**Two Types:**
1. **Deliverables:** Associated with Projects/Milestones (what gets delivered)
2. **Substeps:** Associated with Steps (detailed actions within a step)

**Storage:**
- **Templates** → `ENTITIES/TASK_MANAGERS/` (blueprints)
- **Instances** → `ENTITIES/ANALYTICS/` (actual work with tracking)

**Both can reference Templates (blueprints) or Instances (actual work)**

---

## 📁 Structure

```
Checklist_Items/
├── README.md                    # This file
├── Checklist_Item_Schema.md     # Schema definition
├── Checklist-Item-003.json                 # Master listing of all Checklist Items
└── By_Project/                  # Checklist Items organized by project
    ├── PROJ-HR-002/
    ├── PROJ-AI-002/
    └── ...
```

---

## 🔄 Migration from Deliverables

**Source:** `deliverables` arrays in:
- Project Template milestones (`Project_Templates/*.json`)
- Project Instances (`PROJ-*/project_instance.json`)

**Target:** `Checklist_Items/` subEntity

**Migration Date:** November 25, 2025

---

## 📊 Schema

See `Checklist_Item_Schema.md` for complete schema definition.

**Key Fields:**
- `checklist_item_id` - Unique identifier (CHK-001, CHK-002, etc.)
- `item_name` - Name/description of the deliverable or substep
- `item_type` - Type (`deliverable`, `substep`, `output`, `validation`, `documentation`)
- `associated_project` - Project Template/instance ID (for deliverables)
- `associated_milestone` - Milestone ID (for deliverables)
- `associated_task` - Task ID (optional, for context)
- `associated_step` - Step ID (for substeps)
- `order` - Execution order (required for substeps)
- `phase` - Phase number (if applicable)
- `status` - Completion status
- `required` - Whether item is required for completion

---

## 🔗 Relationships

Checklist Items can be associated with entities at different hierarchy levels:

- **Projects** → Checklist Items (one-to-many) - Deliverables
- **Milestones** → Checklist Items (one-to-many) - Deliverables
- **Tasks** → Checklist Items (one-to-many, optional) - Task-level deliverables
- **Steps** → Checklist Items (one-to-many) - **Substeps** (detailed actions within steps)

**Key Distinction:**
- **Deliverables** (Project/Milestone level): Outputs that must be produced
- **Substeps** (Step level): Detailed actions that make up a step's execution

---

## 📝 Usage

Checklist Items replace the `deliverables` field in:
- Project Template milestones
- Project Instances

**Before (deliverables):**
```json
"deliverables": [
  "n8n workflow: Gmail → Gemini AI → Google Sheets",
  "CV Parser v1.1 optimized prompt"
]
```

**After (checklist_items reference):**
```json
"checklist_items": [
  "CHK-044",
  "CHK-045"
]
```

**Note:** Checklist Item IDs use the simple format `CHK-{ITEM_NUMBER}` (e.g., `CHK-001`, `CHK-044`) for consistency and simplicity.

### Using Checklist Items as Substeps

Checklist Items can also be used as substeps within Steps:

**In Step Instance:**
```json
{
  "step_id": "STEP-TASK-PROJ-HR-001-001-001",
  "name": "Edit Video Interview Footage",
  "checklist_items": [
    {"checklist_item_id": "CHK-099", "order": 1},
    {"checklist_item_id": "CHK-100", "order": 2},
    {"checklist_item_id": "Checklist-Item-001", "order": 3}
  ]
}
```

**Checklist Item (Substep):**
```json
{
  "checklist_item_id": "CHK-099",
  "item_name": "Import raw footage",
  "item_type": "substep",
  "associated_step": "STEP-TASK-PROJ-HR-001-001-001",
  "order": 1
}
```

See `HIERARCHY.md` for complete details on how Checklist Items work at different hierarchy levels.

---

**Last Updated:** November 25, 2025

