## Workflows → Milestone_Templates Mapping

**Purpose:** Document how existing workflow definitions under `ENTITIES/TASK_MANAGERS/Workflows/` are migrated into Milestone Templates under `ENTITIES/TASK_MANAGERS/Milestone_Templates/` using a 1:1 mapping (one workflow file → one milestone template file).

---

## 1. ID and filename convention

- **Existing Milestone Templates:**
  - `Milestone-Template-001_Content_Analysis.json`
  - `Milestone-Template-002_Data_Inventory.json`
  - `Milestone-Template-003_Relationship_Validation.json`
  - `Milestone-Template-004_Schema_Naming_Validation.json`
  - `Milestone-Template-005_Synthesis_Recommendations.json`
  - `Milestone-Template-006_VIDEO-001_Research_Complete.json`
  - `Milestone-Template-007_VIDEO-002_Processing_Complete.json`
  - `Milestone-Template-008_VIDEO-003_Library_Population_Complete.json`

- **New Milestone Templates for Workflows:**
  - Use **sequential IDs starting at 009**, one per workflow file.
  - **Pattern:** `Milestone-Template-{NUM}_{Description}.json`
    - `{NUM}`: 3‑digit zero‑padded integer, continuing from `008`.
    - `{Description}`: derived from workflow name, e.g.:
      - `Lead Enrichment Automation` → `Lead_Enrichment_Automation`
      - `YouTube Tutorial Production` → `YouTube_Tutorial_Production`

Example:

- Workflow: `Workflows/Lead_Enrichment_Workflow.yaml`
- `workflow_name`: `"Lead Enrichment Automation"`
- New file: `Milestone-Template-009_Lead_Enrichment_Automation.json`
- `milestone_template_id`: `"Milestone-Template-009"`

---

## 2. Field mapping (workflow → milestone template)

Each workflow file is treated as the **source of truth** and mapped into a Milestone Template JSON using the schema in `Milestone_Template_Schema.md`, with these conventions:

- **Workflow-level fields → Milestone fields**
  - `workflow_name` → `name`
  - `workflow_id` → `workflow_id` (new metadata field)
  - `workflow_type` → part of `category` or `description`
  - `department` → `department`
  - `description` → `description` (first paragraph / summary)
  - `estimated_duration` → may inform `estimated_hours` (if reasonably interpretable; otherwise omitted)
  - `status` → may be reflected in `status` metadata if used

- **Traceability:**
  - `source_workflow_file`: relative path to the original workflow file, e.g.:
    - `"ENTITIES/TASK_MANAGERS/Workflows/Lead_Enrichment_Workflow.yaml"`
  - `source_workflow_metadata`: optional object with selected workflow fields (e.g., `priority`, `automation_details.platform`).

- **Steps:**
  - For this migration phase, we **do not fully expand every workflow step into Task Templates**.
  - Instead:
    - The milestone template may include a high‑level `notes` or `workflow_summary` field describing the step structure (e.g., “parallel enrichment tasks 2a–2c, then scoring”).
    - Detailed step definitions remain in the original YAML for now, referenced via `source_workflow_file`.
  - Future iterations may:
    - Add a `workflow_steps` array to the milestone template.
    - Or decompose steps into dedicated Task Templates and reference them via the `task_templates` array.

- **Task templates and expected reports:**
  - For migrated workflow milestones, `task_templates` and `expected_reports` **may initially be empty** until dedicated Task Templates and reporting structures are created.

---

## 3. Example mapping: `Lead_Enrichment_Workflow.yaml`

**Source:** `ENTITIES/TASK_MANAGERS/Workflows/Lead_Enrichment_Workflow.yaml`

Key fields:

- `workflow_name`: `"Lead Enrichment Automation"`
- `workflow_type`: `"Parallel Processing"`
- `workflow_id`: `"WF-PAR-001"`
- `department`: `"LG"`
- `description`: automated enrichment using n8n, AI tools, social/profile data

**Target milestone template (conceptual example):**

```json
{
  "milestone_template_id": "Milestone-Template-009",
  "name": "Lead Enrichment Automation",
  "category": "Workflow Migration",
  "department": "LG",
  "description": "Migrated from Workflows/Lead_Enrichment_Workflow.yaml. Automated lead enrichment workflow that processes multiple data sources in parallel to enrich lead information.",
  "estimated_hours": 0,
  "phase": "Lead Generation",
  "can_run_parallel": true,
  "dependencies": [],
  "task_templates": [],
  "expected_reports": [],
  "version": "1.0",
  "source_workflow_file": "ENTITIES/TASK_MANAGERS/Workflows/Lead_Enrichment_Workflow.yaml",
  "workflow_id": "WF-PAR-001"
}
```

---

## 4. Summary of migration rules

1. **1:1 mapping:** Each file in `Workflows/` gets exactly one new Milestone Template JSON in `Milestone_Templates/`.
2. **ID continuity:** Use `Milestone-Template-009` and up, with filename suffixes derived from workflow names.
3. **Minimal fields required:**
   - `milestone_template_id`
   - `name`
   - `department` (when known)
   - `description`
   - `version`
   - `source_workflow_file`
4. **Optional, but recommended:**
   - `category`, `phase`, `estimated_hours`, `workflow_id`.
5. **Steps stay in YAML for now:** high‑level behavior is documented in `description`/`workflow_summary`, with the YAML kept as the detailed technical definition.

Use this document alongside `Milestone_Template_Schema.md` when creating or reviewing workflow‑derived milestone templates.


