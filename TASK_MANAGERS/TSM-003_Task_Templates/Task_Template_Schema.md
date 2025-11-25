# Task Template Schema (TASK_MANAGERS)

**Purpose:** Define the standard JSON structure for Task Templates stored in `ENTITIES/TASK_MANAGERS/Task_Templates`.

This schema is inferred from existing files such as:
- `Task-Template-001.json`
- `Task-Template-044.json`

---

## File Format

- **Format:** JSON
- **Location:** `ENTITIES/TASK_MANAGERS/Task_Templates/`
- **Naming Convention:** `Task-Template-{NUM}_{Description}.json`
  - Sequential numbering: 001-058 (as of 2025-11-17)
  - No department codes in filenames
  - Example: `Task-Template-001_Task-Template-001.json`
  - Example: `Task-Template-039_Setup_n8n_for_CV_Screening.json`

---

## Identity & Taxonomy

- **`entity_type`** *(string, required)*
  - Always `"TASK_MANAGERS"` for this entity family.

- **`sub_entity`** *(string, required)*
  - Usually `"Task_Template"`.

- **`task_template_id`** *(string, required)*
  - Unique Task Template identifier using standardized format.
  - Format: `Task-Template-{NUM}` where NUM is 3-digit sequential (001-058)
  - Example: `"Task-Template-001"`, `"Task-Template-039"`
  - Note: This field matches the filename prefix for consistency.

- **`task_template_name`** *(string, required)*
  - Human-readable Task Template name.

- **`action`** *(string, recommended)*
  - Verb from taxonomy, e.g. `"Parse"`, `"Setup"`.

- **`object`** *(string, recommended)*
  - Object from taxonomy, e.g. `"HTML Data"`, `"Onboarding Automation Workflow"`.

- **`context`** *(string, optional but useful)*
  - Additional context, tools, or scenario.

- **`description`** *(string, recommended)*
  - Short description of what the task achieves.

- **`department`** *(string, optional)*
  - Department primarily responsible.

- **`profession`** *(string, optional)*
  - Typical role performing the task.

- **Priority & Status**
  - `priority` *(string, optional)* – e.g. `"Low" | "Medium" | "High"`.
  - `status` *(string, optional)* – e.g. `"Active"`, `"Template"`, `"Deprecated"`.

---

## Duration, Complexity & Performance

- **`estimated_duration`** *(string, optional)*
  - Example: `"60-90 minutes"`, `"2-3 hours"`.

- **`setup_duration`** *(string, optional)*
  - Time to configure or build the pipeline.

- **Other performance-related fields (may appear depending on template):**
  - `complexity` *(string)* – e.g. `"High"`.
  - `automation_potential` *(string)*.
  - `success_rate` *(string)*.
  - `best_for` *(string)*.
  - `performance_metrics` / `roi_metrics` *(object)* – structured performance information.

---

## Dependencies & Resources

- **`dependencies`** *(array, optional)*
  - Pre-conditions such as systems, access, or previous tasks.

- **`tools_required`** *(array, optional)*
  - List of tool names or tool IDs used.

- **`skills_required`** *(array, optional)*
  - Skills required to execute this task.

- **`objects_used`** *(array, optional)*
  - Related objects/entities used during execution.

- **Cross-references (optional fields used in some templates):**
  - `workflow_reference`
  - `related_workflows`
  - `related_tasks`
  - `related_projects`
  - `related_skills`
  - `related_professions`

---

 ## Steps Template (Execution Structure)

- **`steps_template`** *(array, recommended)*
  - Ordered list of **Step Template references** that describe how to perform the task.
  - Each item should reference a **Step Template** stored in `ENTITIES/TASK_MANAGERS/Step_Templates/` and typically includes:
    - `step_template_id` *(string, required)* – ID of the Step Template (e.g. `"STEP-HR-003-05"`).
    - `step_template_name` *(string, optional)* – human-readable Step Template name.
    - Optional local fields used by the Task Template (if needed):
      - `step_number` *(number, optional)* – display/order index within this task.
      - `notes` *(string, optional)* – task-specific notes or overrides.

  Full execution details (action, tool, inputs, outputs, success criteria, relationships) should be defined in the **Step Template JSON**. See `Step_Templates` README and listings for the canonical step schema.

Example (simplified):

```json
"steps_template": [
  {
    "step_template_id": "STEP-HR-003-05",
    "step_template_name": "Add Interview Subtitles and Approve",
    "step_number": 5
  }
]
```

---

## Checklist

- **`checklist`** *(array, optional but recommended)*
  - Validation items or preconditions that should be true for success.
  - Each item:
    - `item` *(string)* – description.
    - `guide` *(string, optional)* – explanation/details.
    - `required` *(boolean)* – whether this is mandatory.

---

## Guidance, Best Practices & Issues

These sections are optional but strongly recommended for richer templates.

- **Usage guidance:**
  - `when_to_use` *(array of strings)*
  - `when_not_to_use` *(array of strings)*

- **Prompting / AI support:**
  - `ai_parsing_prompt_examples` *(array)* or similar fields.

- **Best practices & examples:**
  - `best_practices` *(array of strings)*
  - `use_case_examples` *(array of objects)*

- **Issues & troubleshooting:**
  - `common_issues` *(array of objects)*
  - `troubleshooting` *(array of objects)*
  - `optimization_tips` *(array of strings)*

- **Additional domain-specific sections** may exist, such as:
  - `resources` *(array)* – external docs, videos, links.
  - `onboarding_checklist_template_detailed` *(array)* – structured checklists.
  - `future_enhancements` *(array)* – backlog of improvements.

---

## Tags & Classification

- **`tags`** *(array, optional)*
  - Freeform tags used for filtering and discovery.

---

## Metadata

- **`version`** *(string, recommended)*
  - Template version, e.g. `"1.0"`.

- **`created`** *(string, optional)*
  - Creation date (ISO 8601 or similar).

- **`last_updated`** *(string, optional)*
  - Last modification date.

- **`source`** *(string, optional)*
  - Provenance, e.g. research document, video, or workflow that inspired the template.

- **Other metadata (may appear):**
  - `compliance_notes`
  - `responsibility_id`, `responsibility_name`

---

## Relationship to Other Entities

- A **Milestone Template** references **Task Templates** by `task_template_id`.
- A **Project Template** references **Milestone Templates**, which in turn reference **Task Templates**.

Use this document as the canonical reference when creating or migrating Task Templates.
