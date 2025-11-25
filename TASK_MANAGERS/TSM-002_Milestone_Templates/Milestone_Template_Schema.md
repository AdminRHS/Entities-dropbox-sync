# Milestone Template Schema (TASK_MANAGERS)

**Purpose:** Define the standard JSON structure for Milestone Templates stored in `ENTITIES/TASK_MANAGERS/Milestone_Templates`.

This schema is inferred from existing files such as `Milestone-Template-001.json` and the `README.md` in this directory.

---

## File Format

- **Format:** JSON
- **Location:** `ENTITIES/TASK_MANAGERS/Milestone_Templates/`
- **Naming Convention:** `Milestone-Template-{NUM}_{Description}.json`
  - Sequential numbering: 001-008 (as of 2025-11-17)
  - No department codes in filenames
  - Example: `Milestone-Template-001_Content_Analysis.json`
  - Example: `Milestone-Template-006_VIDEO-001_Research_Complete.json`

---

## Core Fields

- **`milestone_template_id`** *(string, required)*
  - Unique identifier for the Milestone Template using standardized format.
  - Format: `Milestone-Template-{NUM}` where NUM is 3-digit sequential (001-008)
  - Example: `"Milestone-Template-001"`, `"Milestone-Template-006"`
  - Note: This field matches the filename prefix for consistency.

- **`name`** *(string, required)*
  - Human-readable milestone name.
  - Example: `"Content Analysis"`.

- **`category`** *(string, optional)*
  - High-level category or type of milestone.
  - Example: `"Analysis"`.

- **`department`** *(string, optional)*
  - Department primarily responsible for this milestone.
  - Example: `"OPS"`.

- **`description`** *(string, optional but recommended)*
  - Short description of the milestone scope.

- **`estimated_hours`** *(number, optional)*
  - Estimated effort to complete the milestone.

- **`phase`** *(number or string, optional)*
  - Project phase index or label corresponding to this milestone.

- **`can_run_parallel`** *(boolean, optional)*
  - Whether this milestone can run in parallel with others.

- **`dependencies`** *(array, optional)*
  - List of other milestone IDs or prerequisites that must be completed before this milestone.
  - Example: `[]` or `["MIL-TEMPL-002"]`.

---

## Task Template Links

- **`task_templates`** *(array, optional but recommended)*
  - List of Task Templates that constitute this milestone.
  - Each item:
    - `task_template_id` *(string)* – ID of the Task Template (e.g. `"TASK-TEMPLATE-ANALYSIS-007"`).
    - `task_template_name` *(string)* – Human-readable Task Template name.

Example:

```json
"task_templates": [
  {
    "task_template_id": "TASK-TEMPLATE-ANALYSIS-007",
    "task_template_name": "Duplicate Content Detection"
  },
  {
    "task_template_id": "TASK-TEMPLATE-ANALYSIS-008",
    "task_template_name": "Terminology Extraction"
  }
]
```

---

## Expected Reports

- **`expected_reports`** *(array, optional)*
  - Reports or artifacts expected as outputs of this milestone.
  - Each item:
    - `report_id` *(string)* – Report identifier, e.g. `"REP-004"`.
    - `report_name` *(string)* – Descriptive report name or filename.

Example:

```json
"expected_reports": [
  {
    "report_id": "REP-004",
    "report_name": "Duplicate Content Report"
  },
  {
    "report_id": "REP-005",
    "report_name": "Terminology Extraction Report"
  }
]
```

---

## Metadata

- **`version`** *(string, optional but recommended)*
  - Semantic version of the template (e.g. `"1.0"`).

- **Additional metadata (may appear in other templates):**
  - `status` – template status (Active/Deprecated).
  - `source` / `source_workflow_file` – traceability back to original workflows.
  - `parent_project_template_id` – link to the owning Project Template.

---

## Relationship to Other Entities

- A **Project Template** typically references multiple **Milestone Templates** by ID.
- Each **Milestone Template** references one or more **Task Templates** via the `task_templates` array.

Hierarchy:

```text
Project Template
  └── Milestone Template 1
      ├── Task Template 1
      └── Task Template 2
  └── Milestone Template 2
      └── Task Template 3
```

Use this document as the canonical reference when creating or migrating Milestone Templates.
