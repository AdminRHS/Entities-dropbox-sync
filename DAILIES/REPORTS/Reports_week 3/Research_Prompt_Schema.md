## Research Prompt Schema (v1)

**Purpose:** Define a unified structure for all research prompts that operate across `oa-y`, `LIBRARIES`, and `TASK_MANAGERS`. This schema standardizes how we describe research goals, sources, extraction targets, and downstream entities to update.

---

## 1. Top-level sections

Every schema-compliant research prompt should contain the following sections (as markdown headings or clearly labeled blocks):

1. **Prompt_Metadata**
2. **Topic_Context**
3. **Source_Scope**
4. **Extraction_Targets**
5. **Output_Entities**
6. **Research_Tasks & Steps**
7. **Response_Format**
8. **Quality_Constraints & Filters**
9. **Cross_References**

---

## 2. Section definitions

### 2.1 Prompt_Metadata

- **Fields (conceptual):**
  - `prompt_id`: stable identifier for the **prompt version**, using `PRM-...` pattern (e.g., `PRM-YT-AI-TOOLS-001`).
  - `research_id`: stable identifier for the **research stream**, using `RES-...` pattern (e.g., `RES-YT-AI-TOOLS-001`).
  - `version`: semantic version (e.g., `v2`).
  - `DEP`: one or more department codes (`AI`, `DEV`, `LG`, `HR`, `SMM`, etc.).
  - `intended_runner`: where this will be used (e.g., `Perplexity`, `Claude`, `Cursor`).

### 2.2 Topic_Context

- Describes *why* the research is being done and how it ties into the ecosystem.
- **Required content:**
  - Business question / learning objective.
  - Relevant professions and departments (linkable to `LIBRARIES/Professions` and `DEPARTMENTS/departments.json`).
  - Relevant **oa-y** courses/lessons:
    - Course titles + IDs from `Courses_Listing.md` and/or `FILE_MAP.md`.
    - Optional modules/lessons when the research is supporting specific material.

### 2.3 Source_Scope

- Defines *where* and *what* we research.
- **Fields / content:**
  - Platforms and channels (YouTube, Perplexity, docs, blogs, vendor sites).
  - Time window (e.g., “last 30 days”, “2025-11 only”).
  - Content types: tutorials, deep dives, product updates, docs, benchmarks.
  - Language / region filters if relevant.

### 2.4 Extraction_Targets

- Explicit mapping to Libraries taxonomy.
- **Minimum fields:**
  - `tools`: which tools to identify/validate (links to `LIBRARIES/Tools/*.json`).
  - `objects`: any business objects to refine/add (links to `Objects/*.json`).
  - `actions` / `processes` / `results`: verbs, workflows, or work states to extract.
  - `responsibilities`: new responsibility phrases (Action+Object combinations).
  - `workflows`: high-level or detailed workflows suitable for `Processes/Workflows`.
  - `parameters`: config/parameter structures relevant to `Parameters/*`.

### 2.5 Output_Entities

- Specifies which **artifact types** must be produced or updated.
- **Typical fields:**
  - `libraries_updates`:
    - Tools (new entries / enrichments).
    - Objects, responsibilities, parameters, skills, professions.
  - `task_managers_updates`:
    - Project Templates.
    - Task Templates.
    - Step Templates.
    - Workflows.
  - `research_reports`:
    - Gap analyses.
    - Mapping reports.
    - Validation reports.

### 2.6 Research_Tasks & Steps

- Breaks the research work into steps the LLM (and human) should follow.
- **Recommended subsections:**
  - `Phase 1 – Discovery` (find candidate content).
  - `Phase 2 – Filtering` (apply quality and relevance filters).
  - `Phase 3 – Extraction` (structured extraction of tools, workflows, etc.).
  - `Phase 4 – Mapping` (map findings into Libraries + Task Managers).
  - `Phase 5 – Recommendations` (summaries + proposed actions).

### 2.7 Response_Format

- Defines the **shape** of the answer the LLM should return.
- **Requirements:**
  - Provide a **markdown** summary for humans.
  - Provide a **machine-friendly block** (JSON-like or markdown table) that can be used to:
    - Populate `Research Reports` under `TASK_MANAGERS/RESEARCHES/`.
    - Seed Library/tool updates and Task templates.
  - Always mark:
    - New entities.
    - Updates to existing entities.
    - Open questions / uncertainties.

### 2.8 Quality_Constraints & Filters

- Ensures we only keep high-quality, relevant findings.
- **Examples:**
  - Minimum engagement thresholds for videos.
  - Exclude marketing-only content without concrete workflows.
  - Prefer sources with reproducible, step-by-step demonstrations.
  - Require clear mapping to at least one **department + profession** combination.

### 2.9 Cross_References

- **Required references:**
  - Related research prompts (by `prompt_id` or filename).
  - Related research reports (e.g., `Video_006_Library_Mapping_Report.md`).
  - Related Libraries files (tools, objects, responsibilities).
  - Related Task Manager templates (IDs / filenames).

---

## 3. Minimal markdown skeleton

Schema-compliant prompts under `TASK_MANAGERS/RESEARCHES` should roughly follow this structure:

```markdown
## Prompt_Metadata
- prompt_id: RES-PR-...
- version: v2
- owner: ...
- target_departments: [...]
- intended_runner: ...

## Topic_Context
- Business objective: ...
- Departments / professions: ...
- Related oa-y courses:
  - [Course Title] (Course ID: ...)

## Source_Scope
- Platforms: ...
- Time window: ...
- Content types: ...

## Extraction_Targets
- Tools: ...
- Objects: ...
- Actions / Processes / Results: ...
- Responsibilities: ...
- Workflows: ...
- Parameters: ...

## Output_Entities
- Libraries_updates: ...
- Task_managers_updates: ...
- Research_reports: ...

## Research_Tasks_and_Steps
1. ...
2. ...

## Response_Format
- Human summary: ...
- Machine-structured block: ...

## Quality_Constraints_and_Filters
- ...

## Cross_References
- Research prompts: ...
- Research reports: ...
- Libraries: ...
- Task templates / workflows: ...
```

This schema is intentionally descriptive and will be instantiated by concrete prompts (v2 files) that inherit this shape while specializing the content.


