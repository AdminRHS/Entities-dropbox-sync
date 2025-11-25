## oa-y / Libraries / Task Managers – Research Data Flow Notes

**Purpose:** Internal mapping note describing how `oa-y` learning content, `LIBRARIES`, and `TASK_MANAGERS` research assets connect today. This is a support document for the gap analysis and schema design work, not a user-facing guide.

---

## 1. High-level data flows

- **Flow A – Video / tutorial research → Libraries → Task Managers**
  - Source: YouTube / AI tutorials researched via prompts in `PROMPTS/Research Prompts/` and Perplexity workflows documented in `TASK_MANAGERS/RESEARCHES/README_Library.md`.
  - Processing:
    - Raw research sessions logged as JSON in `TASK_MANAGERS/RESEARCHES/RESEARCH_INDEX.json` and `AI_Tutorials` (now folded into `RESEARCHES` + `Videos/`).
    - Selected videos moved into `TASK_MANAGERS/RESEARCHES/Videos/*.md` with mapping reports under `TASK_MANAGERS/RESEARCHES/Research Reports/` and `LIBRARIES/LIBRARIES_Import_Index.md`.
    - Tools, objects, workflows, skills, professions created or updated in `LIBRARIES` (`Tools/`, `Objects/`, `Responsibilities/`, `Processes/Workflows/`, `Professions/`, `Skills/`).
  - Outputs:
    - Library entries become the canonical source for **Actions / Objects / Tools / Processes / Responsibilities / Parameters / Professions**.
    - Task and project templates in `TASK_MANAGERS` reference these libraries via taxonomy fields defined in `TASK_MANAGERS/TAXONOMY_GUIDELINES.md`.

- **Flow B – oa-y courses → Libraries → Task Managers**
  - Source: Courses, modules, lessons, tests under `ASSETS/oa-y/` described in `FILE_MAP.md`, `Courses_Listing.md`, `Lessons_Listing.md`, `Modules_Listing.md`, `Tests_Listing.md`.
  - Processing:
    - Courses describe onboarding and tool usage (AI tools, IDEs, CRM, Notion, Dropbox, etc.).
    - `FILE_MAP.md` and `Courses_Listing.md` provide the primary mapping from human course names → API IDs → professions / departments.
  - Outputs (today, partially implicit):
    - Tools and workflows mentioned in oa-y courses should map to existing entries in `LIBRARIES` (e.g., `Tools/AI_Tools`, `Tools/Development_Tools`, `Tools/Automation_Tools`, `Tools/Social_Media_Platforms`).
    - Responsibilities implied by courses (e.g., “Create Job Posting”, “Send Cold Email”) should correspond to responsibilities and task templates defined in `LIBRARIES/Responsibilities/` and `TASK_MANAGERS/Task_Templates/`.

- **Flow C – Research prompts → Research reports → Library updates / Task templates**
  - Source: Department- or topic-specific research prompts in `PROMPTS/Research Prompts/` (YouTube AI tools, HR automation, SMM, Sales, VSCode Agent HQ, etc.).
  - Processing:
    - Prompts are run against external sources (mostly YouTube), creating structured notes and mapping reports.
    - Reports live under `TASK_MANAGERS/RESEARCHES/Research Reports/` and `LIBRARIES/Prompts/*.md` (Video_006/008 mapping reports, tool validation reports, gap analyses).
  - Outputs:
    - Tools and workflows validated or discovered in reports are integrated into `LIBRARIES` (Tools, Objects, Workflows, Skills, Professions).
    - Task Manager templates (Projects, Milestones, Tasks, Steps) are planned in `LIBRARIES_Import_Index.md` Phase 4–9 and implemented in `TASK_MANAGERS` using taxonomy fields.

---

## 2. Key schema anchors used across entities

- **Libraries (authoritative taxonomy)**
  - `LIBRARIES/README.md` and `CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md` define the **DEPARTMENTS → RESPONSIBILITIES → (ACTIONS + OBJECTS) → TASKS** stack.
  - Core files:
    - `Actions/actions.json` + `Processes` + `Results`
    - `Objects/objects.json` + category files (e.g., `Lead_Generation_Objects.json`, `AI_Automation_Objects.json`)
    - `Tools/` (AI_Tools, Development_Tools, Automation_Tools, etc.)
    - `Professions/professions.json`
    - `Responsibilities/responsibilities.json`
    - `Parameters/parameters.json` and organized-by-profession/department views.
  - Video-driven imports are orchestrated via `LIBRARIES_Import_Index.md` and `Taxonomy_Gap_Analysis.md` (e.g., Video_002/005/006/008 extractions).

- **Task Managers (execution layer)**
  - `TASK_MANAGERS/TAXONOMY_GUIDELINES.md` explains how Actions/Objects/Tools/Professions/Departments from `LIBRARIES` are embedded into:
    - `Task_Templates/*.json`
    - `Step_Templates/*.json`
    - `Milestone_Templates/*.json`
    - `Project_Templates/*.json`
  - Relationships:
    - Task Templates reference Step Templates, Milestone Templates, Projects, and external entities (JOBS, BUSINESSES, TALENTS) via IDs and taxonomy fields.

- **oa-y (learning layer)**
  - `FILE_MAP.md` provides mapping between:
    - Human-readable course filenames
    - Course IDs, professions, departments, number of modules/lessons.
  - Listings for lessons/modules/tests give IDs + slugs but **do not yet explicitly reference Libraries or Task Manager templates**.

---

## 3. Where schema mismatches and gaps appear today

- **3.1 oa-y → Libraries**
  - The oa-y catalog heavily covers:
    - AI tools (Claude, ChatGPT, Gemini, NotebookLM, Cursor, etc.).
    - Developer environments (VS Code, Linux + Claude Code).
    - Productivity stack (Google Workspace, Dropbox, Notion, CRM).
    - Department-specific flows (Lead Generation series, Recruitment Operations, Sales Management).
  - Most of these tools already exist in `LIBRARIES/Tools/`, but:
    - Not all **course-specific workflows** (e.g., “Daily Google Drive File Tracker”) are represented as explicit workflows in `Processes/Workflows/`.
    - Some oa-y course modules encode responsibilities/tasks that are **not explicitly mirrored** in `Responsibilities` or `Task_Templates` (e.g., detailed lead-gen day workflows, onboarding bots, MCP integration flows).

- **3.2 oa-y → Task Managers**
  - `TASK_MANAGERS` contains a rich template ecosystem (Tasks, Projects, Steps), but:
    - There is no systematic **per-course mapping** from oa-y content to:
      - Which Task Templates a new hire should master.
      - Which Project Templates or Workflows implement the skills taught in each course.
    - Course difficulty and module structure are not currently reflected as **milestones or learning projects** in Task Managers.

- **3.3 Research prompts → Research reports / Libraries / Task Templates**
  - Existing research prompts have strong narrative descriptions (as documented in `PROMPTS/Research Prompts/README.md`) but:
    - They do not share a single, explicit **schema** for:
      - Inputs (source scope, time windows, platforms).
      - Expected outputs (tool lists, workflows, responsibilities, parameters).
      - Cross-references (which Libraries files and Task templates to update).
    - Mapping from a given research prompt → specific report type (`Research Reports`, `LIBRARIES_Import_Index` entries) is currently **implicit** and must be inferred from narrative docs.

---

## 4. Target direction for unified research schemas

- **Unified Research Prompt Schema (high-level goals)**
  - Make every research prompt explicitly specify:
    - **Topic_Context** (department, profession, oa-y courses it supports).
    - **Source_Scope** (platforms, time windows, content types).
    - **Extraction_Targets** (Tools, Objects, Workflows, Responsibilities, Parameters, Professions).
    - **Output_Entities** (which `LIBRARIES` sub-entities and `TASK_MANAGERS` templates should be produced or updated).
    - **Report_Type** (gap analysis, mapping report, validation report, trend analysis).
    - **Task_Manager_Links** (explicit IDs or filenames for projects/milestones/tasks/steps to reference or create).

- **Unified Research Report Schema (high-level goals)**
  - Make every report under `TASK_MANAGERS/RESEARCHES/Research Reports/` and `LIBRARIES/Prompts/*.md`:
    - Declare its **source prompt(s)** and **source videos/courses**.
    - Use a consistent structure for:
      - Coverage by topic/theme.
      - Library entities created/updated.
      - Task Manager templates created/updated.
      - Remaining gaps and open ToDo items (referencing `TASK_MANAGERS/RESEARCHES/ToDo/*.json`).

- **oa-y alignment**
  - For each major oa-y theme (AI tools, IDEs, CRM, Notion, Dropbox, Recruitment, Sales, LG, SMM, MCP), we want:
    - At least one **schema-aligned research prompt version** living under `TASK_MANAGERS/RESEARCHES/`.
    - Cross-references to:
      - Relevant oa-y courses (by ID + filename).
      - Relevant Libraries tools/responsibilities/parameters.
      - Relevant Task Manager Project/Task/Step templates (by ID + file path).

These notes are the working backbone for the dedicated gap analysis and the `Research_Prompt_Schema.md` / `Research_Report_Schema.md` definitions that follow.


