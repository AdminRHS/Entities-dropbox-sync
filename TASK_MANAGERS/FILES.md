# TASK_MANAGERS – Files Overview

**Purpose**: Provide a concise overview of key files and directories in the `TASK_MANAGERS` entity, including prompts, templates, and workflows.  
**Last Updated**: 2025-11-25

---

## Core Documentation

- **`README.md`** – High-level description of the `TASK_MANAGERS` entity, sub-entities, relationships, and business value.
- **`INDEX.md`** – Master index of Task Templates, Project Templates, Step Templates, projects, and milestone templates.
- **`TAXONOMY_GUIDELINES.md`** – Rules for using Actions, Objects, Tools, Professions, and entity relationships in templates.
- **`TASK.md`** – Local task log for work related to `TASK_MANAGERS` (this project-level tasks list).

---

## Researches (`TASK_MANAGERS/RESEARCHES/`)

- **`TASK_MANAGERS/RESEARCHES/README.md`** – Overview of migrated research assets (AI tutorials, SMM, influencer tracking, ToDo queues) now colocated with Task Managers.
- **`TASK_MANAGERS/RESEARCHES/oa-y_Research_Data_Flow_Notes.md`** – Internal mapping note describing how `oa-y` content, `LIBRARIES`, and `TASK_MANAGERS` research assets connect.
- **`TASK_MANAGERS/RESEARCHES/oa-y_Libraries_TaskManagers_Gap_Analysis.md`** – Topic-by-topic gap analysis between oa-y courses, Libraries coverage, and Task Manager templates.
- **`TASK_MANAGERS/RESEARCHES/Research_Prompt_Schema.md`** – Unified schema for research prompts (inputs, extraction targets, outputs, cross-references).
- **`TASK_MANAGERS/RESEARCHES/Research_Report_Schema.md`** – Unified schema for research reports consumed by Libraries and Task Managers.
- **`TASK_MANAGERS/RESEARCHES/Research_Prompts_Schema_Aligned/*.md`** – v2 schema-aligned research prompts for key topics (YouTube AI tools, HR automation, SMM docs, VSCode Agent HQ, oa-y AI tools alignment, Dev/MCP, productivity, Sales).

---

## Prompts (`PROMPTS/`)

- **`PROMPTS/README.md`** – Overview of the prompts library (Core, Daily Reports, Video Processing, Operational Workflows, etc.).
- **`PROMPTS/Operational_Workflows/README.md`** – Index of operational workflow prompts.
- **`PROMPTS/Operational_Workflows/Call_Organizer_v4.md`** – **Active** entity-centric call organizer for mapping calls into `TASK_MANAGERS` tasks and workflows.
- **`PROMPTS/Operational_Workflows/Archive/Call_Organizer_v3.md`** – Archived call organizer with embedded employee and project directories (Remote Helpers–specific).
- **`PROMPTS/Operational_Workflows/Archive/Call_Organizer_v2.md`** – Legacy call organizer (deprecated, kept for historical reference).
- **`PROMPTS/Operational_Workflows/PROMPT_Document_Finished_Project.md`** – Prompt for creating standardized completion reports for finished projects.

---

## Templates & Instances (High-Level)

- **`Task_Templates/`** – JSON Task Templates (Action + Object + Context) organized by department; see `Task_Templates_Checklist-Item-003.md` for IDs and names.
- **`Project_Templates/`** – Project Template JSON files and `Project_Templates_Checklist-Item-003.md` for project IDs and names.
- **`RESEARCHES/Video_Queue/VIDEO-020_Task_Manager_App_ExecutionFlow.md`** – NEW condensed execution flow for the Codynn Task Manager tutorial (aliases Video_020) that maps phases to reusable tasks/steps/workflows.
- **`Milestone_Templates/`** – Milestone Template definitions (including templates migrated from legacy `Workflows/`) and README.
- **`Step_Templates/`** – Step Template definitions, grouped by department (HR, LG, DEV, DESIGN, etc.), with `PHASE4_STEPS_INDEX.md` and `STEPS_INDEX.md`.
- **`Projects/`** – Project instance folders (e.g., `PROJ-AI-NMP-001`), including milestones and logs.
- **`Tasks/`** – Central location for task instances (currently mainly prepared/empty for future population).
- **`Steps/`** – Central location for step instances (prepared for future use).

---

## How This Relates to Call_Organizer_v4

- **Input → Output**:  
  `Call_Organizer_v4` takes call transcripts and produces:
  - Human-readable task and workflow descriptions aligned with TAXONOMY guidelines.  
  - JSON-ready **task candidates** suitable for `Task_Templates` or `Tasks`.  
  - JSON-ready **workflow candidates** suitable for `Workflows/*.yaml` or for embedding into Project Templates.

- **Where to Save New Artifacts**:
  - New **Task Templates** → `Task_Templates/` (+ update `Task_Templates_Checklist-Item-003.md`, `INDEX.md`).  
  - New **workflows** → `Workflows/` (+ update `Workflows_Checklist-Item-003.md`, `INDEX.md`).  
  - New **Project Templates or milestones** implied by calls → `Project_Templates/` and `Milestone_Templates/` (with listing and index updates).

---

## Maintenance Notes

- Update this `FILES.md` when:
  - New core prompts are added or deprecated (especially under `PROMPTS/Operational_Workflows/`).  
  - New major template categories or directories are introduced.  
  - The primary call organizer prompt changes version or location.


