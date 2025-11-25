# Step Template Schema (TASK_MANAGERS)

**Purpose:** Define the standard JSON structure for Step Templates stored in `ENTITIES/TASK_MANAGERS/Step_Templates`.

This schema is inferred from:
- `Step_Templates/README.md`
- Example Step Templates such as `Add_Interview_Subtitles_and_Approve_TASK-TEMPLATE-HR-003_Template.json`
- Departmental listings like `Step_Templates/AI/Checklist-Item-003.json`

---

## File Format

- **Format:** JSON and Markdown
- **Location:** `ENTITIES/TASK_MANAGERS/Step_Templates/`
- **Naming Convention:** `Step-Template-{NUM}_{Description}.{json|md}`
  - Sequential numbering: 001-379 (as of 2025-11-17)
  - JSON files: 001-070 (complex steps with full metadata)
  - MD files: 071-379 (simple steps with basic structure)
  - No department codes in filenames
  - Example JSON: `Step-Template-001_Add_Interview_Subtitles_and_Approve_TEMPLATE-TASK-HR-003.json`
  - Example MD: `Step-Template-071_ADMIN-001-01_draft-rule-description-and-examples-eg-mon_prompts.md`

---

## Identity & Parent Task

- **`step_template_id`** *(string, required)*
  - Unique identifier for the Step Template using standardized format.
  - Format: `Step-Template-{NUM}` where NUM is 3-digit sequential (001-379)
  - Example: `"Step-Template-001"`, `"Step-Template-071"`
  - Note: This field matches the filename prefix for consistency.

- **`step_template_name`** *(string, required)*
  - Human-readable Step Template name.
  - Example: `"Add Interview Subtitles and Approve"`.

- **`metadata`** *(object, optional)*
  - High-level status / flags for the template.
  - Common fields:
    - `status` *(string)* – e.g. `"Active"`, `"Deprecated"`.

- **`parent_task`** *(object, required)*
  - Links the Step Template to its owning **Task Template**.
  - Fields:
    - `task_id` *(string)* – parent Task Template ID, e.g. `"TASK-TEMPLATE-HR-003"`.
    - `task_name` *(string)* – parent Task Template name, e.g. `"Conduct Video Interview with Candidate"`.

---

## Step Details (Step Template Core)

- **`step_template_details`** *(object, required)*
  - This object is the **core of the Step Template** – it describes the actual instruction.
  - In the minimal model, a Step Template is effectively:
    - `step_template_id` + `step_template_name` + `step_template_details`.
  - Typical fields:
    - `step_number` *(number)* – position of the step within the parent task workflow.
    - `order` *(number, optional)* – explicit ordering; can duplicate `step_number` when simple.
    - `action` *(string)* – action verb for the step, aligned with taxonomy, e.g. `"subtitle"`, `"review"`, `"draft"`.
    - `detail` *(string)* – detailed description of what is done in this step.
    - `expected_duration` *(number or string, optional)* – estimated effort (e.g. minutes, or descriptive string).

Example:

```json
"step_template_details": {
  "step_number": 5,
  "order": 5,
  "action": "subtitle",
  "detail": "Generate or upload captions, review accuracy, and approve once subtitles meet brand standards",
  "expected_duration": 35
}
```

---
> **Note:** Execution details (tools, inputs, outputs, success criteria) are intentionally **kept out of the minimal Step Template schema** for now. In future iterations, these may be modeled via dedicated checklist-style items or linked structures instead of an `execution` object.

---

## Relationships

- **`relationships`** *(object, optional but recommended)*
  - Describes how this step connects to other steps in the same Task Template.
  - Typical fields:
    - `dependencies` *(array of strings)* – IDs of Step Templates that must be completed first, e.g. `["STEP-HR-003-04"]`.
    - `next_steps` *(array of strings)* – IDs of Step Templates that typically follow this one.
    - `parallel_steps` *(array of strings)* – IDs of steps that may run in parallel.

Example:

```json
"relationships": {
  "dependencies": ["STEP-HR-003-04"],
  "next_steps": [],
  "parallel_steps": []
}
```

---

## Source Tracking

- **`source_tracking`** *(object, optional but recommended)*
  - Provides provenance/context for how this Step Template was derived.
  - Typical fields:
    - `source_file` *(string)* – path to source analysis or extraction file.
    - `extraction_date` *(string)* – date when this Step Template was created/extracted.

Example:

```json
"source_tracking": {
  "source_file": "AI Nov25/Niko AI/Employees/units/video_editing.json",
  "extraction_date": "2025-11-07"
}
```

---

## Relationship to Checklist-Item-003s & Task Templates

- Departmental listings (e.g. `Step_Templates/AI/Checklist-Item-003.json`) provide **indexes** of Step Templates with fields such as:
  - `id` – Step Template ID (links to `step_template_id`).
  - `parent_task_id` – parent Task Template ID.
  - `step_number`, `action`, `tool`, `description`, `location`, `created_date`.

- **Task Templates** reference Step Templates via `steps_template` entries (see `Task_Template_Schema.md`):

```json
"steps_template": [
  {
    "step_template_id": "STEP-HR-003-05",
    "step_template_name": "Add Interview Subtitles and Approve",
    "step_number": 5
  }
]
```

Hierarchical view:

```text
Task Template (TASK-TEMPLATE-XXX)
  ├── Step Template 1 (step_template_id)
  ├── Step Template 2 (depends on Step Template 1)
  └── Step Template 3 (parallel with Step Template 2)
```

Use this document as the canonical reference when creating or updating Step Templates in `Step_Templates/`. Align new Step Templates with this structure and ensure they are indexed in the appropriate departmental `Checklist-Item-003.json` and in `Step_Templates_Checklist-Item-003.md` / `INDEX.md` where applicable.
