# Checklist Item Schema (TASK_MANAGERS)

**Purpose:** Define the standard JSON structure for Checklist Items stored in `ENTITIES/TASK_MANAGERS/Checklist_Items`.

**Created:** November 25, 2025  
**Migration Source:** Deliverables from Project Templates and Project Instances

**Hierarchy Position:** Checklist Items can exist at multiple levels:
- **Project/Milestone Level:** As deliverables (outputs of milestones/projects)
- **Step Level:** As substeps (detailed actions within steps)

**Template vs Instance:**
- Checklist Items can reference **Template IDs** (blueprints) or **Instance IDs** (actual work)
- **Templates** define reusable structure - stored in `ENTITIES/TASK_MANAGERS/`
- **Instances** track execution with completion status - stored in `ENTITIES/ANALYTICS/`

---

## File Format

- **Format:** JSON
- **Location:** `ENTITIES/TASK_MANAGERS/Checklist_Items/`
- **Naming Convention:** `Checklist-Item-{NUM}_{Description}.json`
  - Sequential numbering: 001-004 (as of 2025-11-17)
  - Organized in consolidated listing files
  - Example: `Checklist-Item-001_Item_101_to_Item_110.json`
  - Example: `Checklist-Item-003_Checklist-Item-003.json`

---

## Core Fields

### Required Fields

- **`checklist_item_id`** *(string, required)*
  - Unique identifier for the Checklist Item using standardized format
  - Format: `Checklist-Item-{NUM}` where NUM is 3-digit sequential (001-004)
  - Example: `"Checklist-Item-001"`, `"Checklist-Item-002"`
  - Note: This field matches the filename prefix for consistency

- **`item_name`** *(string, required)*
  - Name/description of the deliverable or Checklist Item
  - Example: `"n8n workflow: Gmail → Gemini AI → Google Sheets"`

- **`entity_type`** *(string, required)*
  - Always: `"TASK_MANAGERS"`

- **`sub_entity`** *(string, required)*
  - Always: `"Checklist_Item"`

### Association Fields

- **`associated_project`** *(string, required for deliverables, optional for substeps)*
  - Project Template ID or Project Instance ID
  - Template Example: `"Project-Template-003"` or `"TEMPLATE-PROJ-HR-002"`
  - Instance Example: `"PROJ-LIB-001"` or `"PROJ-HR-001"`
  - **Note:** Required for deliverables, optional for substeps (for context)

- **`associated_milestone`** *(string, optional)*
  - Milestone Template ID or Milestone Instance ID if item belongs to a milestone
  - Template Example: `"MIL-TEMPLATE-PROJ-HR-002-001"`
  - Instance Example: `"MIL-PROJ-HR-002-001"`

- **`associated_task`** *(string, optional)*
  - Task Template ID or Task Instance ID if item belongs to a task
  - Template Example: `"TASK-TEMPLATE-HR-003"`
  - Instance Example: `"TASK-PROJ-HR-002-001"`

- **`associated_step`** *(string, optional)*
  - Step Template ID or Step Instance ID if item belongs to a step (acts as substep)
  - Template Example: `"TEMPLATE-STEP-TASK-TEMPLATE-HR-003-001"`
  - Instance Example: `"STEP-TASK-PROJ-HR-001-001-001"`
  - **Note:** When associated with a step, the Checklist Item functions as a substep

- **`phase`** *(number or string, optional)*
  - Phase number or identifier
  - Example: `1` or `"Phase 1"`

### Status Fields

- **`status`** *(string, optional)*
  - Completion status: `"pending"`, `"in_progress"`, `"completed"`, `"blocked"`
  - Default: `"pending"`

- **`required`** *(boolean, optional)*
  - Whether this item is required for milestone/project completion
  - Default: `true`

- **`completed_date`** *(string, optional)*
  - ISO date format (YYYY-MM-DD) when item was completed
  - Example: `"2025-11-25"`

### Classification Fields

- **`item_type`** *(string, optional)*
  - Type of Checklist Item: `"deliverable"`, `"substep"`, `"output"`, `"validation"`, `"documentation"`, `"report"`, `"workflow"`, `"integration"`
  - Default: `"deliverable"` (for project/milestone level) or `"substep"` (for step level)

- **`order`** *(number, optional but recommended for substeps)*
  - Execution order within the parent step
  - Required when `item_type` is `"substep"`
  - Example: `1`, `2`, `3`

- **`category`** *(string, optional)*
  - Category for grouping: `"technical"`, `"documentation"`, `"testing"`, `"deployment"`, `"training"`

### Additional Metadata

- **`description`** *(string, optional)*
  - Detailed description of the item

- **`acceptance_criteria`** *(array, optional)*
  - List of criteria that must be met for completion
  - Example: `["All tests passing", "Documentation complete"]`

- **`dependencies`** *(array, optional)*
  - List of other Checklist Item IDs that must be completed first
  - Example: `["CHK-001", "CHK-044"]`

- **`related_files`** *(array, optional)*
  - File paths or references related to this item
  - Example: `["ENTITIES/TASK_MANAGERS/Workflows/WF-HR-AUTO-001.yaml"]`

- **`quality_criteria`** *(array, optional)*
  - Quality standards for this deliverable
  - Example: `["Accuracy >90%", "Documentation complete"]`

### Versioning & Tracking

- **`version`** *(string, optional)*
  - Version of the Checklist Item definition
  - Example: `"1.0"`

- **`created`** *(string, optional)*
  - ISO date format (YYYY-MM-DD) when item was created
  - Example: `"2025-11-25"`

- **`last_updated`** *(string, optional)*
  - ISO date format (YYYY-MM-DD) when item was last updated
  - Example: `"2025-11-25"`

- **`migrated_from`** *(object, optional)*
  - Reference to original deliverables data
  - Fields:
    - `source_type`: `"project_template"` or `"project_instance"`
    - `source_file`: Path to source file
    - `original_field`: `"deliverables"`
    - `migration_date`: ISO date format

---

## Example Structures

### Example 1: Deliverable (Project/Milestone Level)

```json
{
  "checklist_item_id": "CHK-044",
  "item_name": "n8n workflow: Gmail → Gemini AI → Google Sheets",
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Checklist_Item",
  "associated_project": "Project-Template-003",
  "associated_milestone": "MIL-PROJ-HR-002-001",
  "phase": 1,
  "status": "pending",
  "required": true,
  "item_type": "deliverable",
  "category": "technical",
  "description": "Complete n8n automation workflow connecting Gmail trigger to Gemini AI analysis and Google Sheets output",
  "acceptance_criteria": [
    "Workflow executes without errors",
    "Gmail trigger fires on new CV emails",
    "Gemini AI analysis produces valid output",
    "Google Sheets receives and displays data"
  ],
  "related_files": [
    "ENTITIES/TASK_MANAGERS/Workflows/WF-HR-AUTO-001.yaml"
  ],
  "quality_criteria": [
    "Processing time < 2 minutes per CV",
    "Accuracy >90%"
  ],
  "migrated_from": {
    "source_type": "project_template",
    "source_file": "ENTITIES/TASK_MANAGERS/Project_Templates/Project-Template-003.json",
    "original_field": "deliverables",
    "migration_date": "2025-11-25"
  },
  "version": "1.0",
  "created": "2025-11-25",
  "last_updated": "2025-11-25"
}
```

### Example 2: Substep (Step Level)

```json
{
  "checklist_item_id": "CHK-099",
  "item_name": "Import raw footage",
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Checklist_Item",
  "associated_step": "STEP-TASK-PROJ-HR-001-001-001",
  "associated_task": "TASK-PROJ-HR-001-001",
  "associated_project": "PROJ-HR-001",
  "status": "pending",
  "required": true,
  "item_type": "substep",
  "order": 1,
  "description": "Import raw video footage into editing software",
  "acceptance_criteria": [
    "All footage files imported",
    "Files organized in project structure",
    "No corrupted files"
  ],
  "version": "1.0",
  "created": "2025-11-25",
  "last_updated": "2025-11-25"
}
```

---

## Checklist-Item-003 File Structure

The `Checklist-Item-003.json` file contains a master index of all Checklist Items:

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Checklist_Items_Checklist-Item-003",
  "version": "1.0",
  "last_updated": "2025-11-25",
  "total_items": 150,
  "items": [
    {
      "checklist_item_id": "CHK-044",
      "item_name": "n8n workflow: Gmail → Gemini AI → Google Sheets",
      "associated_project": "Project-Template-003",
      "associated_milestone": "MIL-PROJ-HR-002-001",
      "status": "pending",
      "file_path": "ENTITIES/TASK_MANAGERS/Checklist_Items/By_Project/Project-Template-003/CHK-044.json"
    }
  ],
  "by_project": {
    "Project-Template-003": 6,
    "Project-Template-001": 12,
    "PROJ-LIB-001": 8
  },
  "by_status": {
    "pending": 120,
    "completed": 25,
    "in_progress": 5
  }
}
```

---

**Last Updated:** November 25, 2025

