## Research Report Schema (v1)

**Purpose:** Define a consistent structure for research reports that summarize findings from research prompts and feed into `LIBRARIES` and `TASK_MANAGERS`. This schema is intended for documents under `TASK_MANAGERS/RESEARCHES/Research Reports/` and closely related paths.

---

## 1. Top-level sections

1. **Report_Metadata**
2. **Source_Prompts_and_Inputs**
3. **Scope_and_Methodology**
4. **Findings**
5. **Libraries_Updates**
6. **Task_Managers_Updates**
7. **Gap_Analysis**
8. **Recommendations_and_Next_Actions**
9. **Cross_References**

---

## 2. Section definitions

### 2.1 Report_Metadata

- **Fields (conceptual):**
  - `report_id`: e.g., `RES-REP-oa-y-ALIGN-001`.
  - `version`: e.g., `v1`.
  - `date`: ISO date.
  - `author`: human, AI, or team.
  - `status`: Draft / Final / Superseded.

### 2.2 Source_Prompts_and_Inputs

- List which research prompts and inputs produced this report.
- **Minimum content:**
  - `research_prompts`:
    - Filenames and/or `prompt_id`s of the prompts used.
  - `oa-y_sources`:
    - Course / module / lesson IDs and titles (for alignment reports).
  - `external_sources`:
    - Videos, transcripts, documentation links.

### 2.3 Scope_and_Methodology

- Clarify what the report covers and how the data was collected.
- **Examples:**
  - Time window of the research (e.g., last 30 days).
  - Platforms and search strategies used.
  - Inclusion / exclusion criteria.
  - Whether the report is focused on tools, workflows, responsibilities, or a mix.

### 2.4 Findings

- Main body of the report.
- **Recommended subsections:**
  - `By_Topic_or_Theme`: e.g., AI tools onboarding, MCP, CRM usage, lead-gen.
  - `By_Tool`: findings organized per tool.
  - `By_Workflow`: workflows and sequences discovered or validated.
  - `By_Profession_or_Department`: impact on specific departments.

### 2.5 Libraries_Updates

- A dedicated section that specifies **what should change** in `LIBRARIES`.
- **Examples:**
  - New tools to add (with minimal key fields).
  - New responsibilities (Action+Object phrases) to add.
  - Changes to existing objects, parameters, or skills.
- **Format recommendations:**
  - Provide summaries for humans.
  - Provide one or more machine-friendly tables or JSON-like blocks that can be used to update library files.

### 2.6 Task_Managers_Updates

- Specifies how Task Templates / Project Templates / Workflows should change or be added.
- **Examples:**
  - New Task Templates required, with:
    - Suggested `action`, `object`, `tool`, `profession`, `department`.
    - High-level description and dependencies.
  - Updates to existing templates (e.g., add steps, tweak taxonomy).
  - New Workflows (YAML or JSON structures) to be created in `TASK_MANAGERS/Workflows/`.

### 2.7 Gap_Analysis

- Explicitly list discrepancies between:
  - What oa-y courses and external tutorials teach.
  - What Libraries currently model.
  - What Task Manager templates currently implement.
- **Recommended structure:**
  - `Missing_entities` (tools, objects, responsibilities, workflows).
  - `Under_specified_entities` (existing entries that need more detail).
  - `Missing_templates` (tasks, steps, projects).
  - `Priority` per gap (Critical / High / Medium / Low).

### 2.8 Recommendations_and_Next_Actions

- Concrete, actionable instructions.
- **Subsections:**
  - `Immediate_actions` (next 1–2 weeks).
  - `Short_term` (next 30–90 days).
  - `Long_term` (beyond 3 months).
- Where possible, link each action to:
  - A specific Library file.
  - A specific Task template / workflow.
  - A specific oa-y course or lesson.

### 2.9 Cross_References

- **Required references:**
  - Related research prompts.
  - Related research reports (e.g., prior gap analyses, Video mapping reports).
  - Related Libraries files (paths and IDs).
  - Related Task Manager templates (IDs and filenames).
  - Related ToDo entries in `TASK_MANAGERS/RESEARCHES/ToDo`.

---

## 3. Minimal markdown skeleton

Schema-compliant reports should roughly follow this pattern:

```markdown
## Report_Metadata
- report_id: ...
- version: v1
- date: ...
- author: ...
- status: Draft | Final

## Source_Prompts_and_Inputs
- Research prompts: [...]
- oa-y sources: [...]
- External sources: [...]

## Scope_and_Methodology
- Scope: ...
- Methodology: ...

## Findings
### By_Topic_or_Theme
- ...

### By_Tool
- ...

### By_Workflow
- ...

## Libraries_Updates
- Summary: ...
- Proposed changes: ...

## Task_Managers_Updates
- Summary: ...
- Proposed changes: ...

## Gap_Analysis
- Missing_entities: ...
- Under_specified_entities: ...
- Missing_templates: ...
- Priority_summary: ...

## Recommendations_and_Next_Actions
- Immediate: ...
- Short_term: ...
- Long_term: ...

## Cross_References
- Research prompts: ...
- Research reports: ...
- Libraries: ...
- Task templates / workflows: ...
- ToDo entries: ...
```

This schema is designed to be compatible with existing mapping and gap analysis reports while providing enough structure for future automation.


