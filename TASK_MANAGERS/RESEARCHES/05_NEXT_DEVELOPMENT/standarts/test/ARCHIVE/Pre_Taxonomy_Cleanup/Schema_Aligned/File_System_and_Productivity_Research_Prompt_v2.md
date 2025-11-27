---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: File_System_and_Productivity_Research_Prompt_v2
title: File System and Productivity Research Prompt v2
date: 2025-11-24
status: archived
owner: unknown
related: []
links: []
---

# File System and Productivity Research Prompt v2

## Summary
- TODO

## Context
- TODO

## Data / Content
## Prompt_Metadata
- prompt_id: RES-PR-FS-PROD-001
- version: v2
- owner: Operations / AI Research
- target_departments: [OPS, DEV, DESIGN, LG, HR, SMM]
- intended_runner: Perplexity or Claude (web + YouTube + docs access)

## Topic_Context
- Business objective:  
  Use oa-y productivity and file-system courses plus fresh tutorials to design standardized workflows and Task templates for Chrome, Google Drive/Sheets, Dropbox, and Notion.

- Departments / professions:
  - Departments: Operations, Development, Lead Generation, HR, Design, SMM.
  - Professions: operations specialist, project manager, lead generator, recruiter, designer, content manager, developer.

- Related oa-y courses:
  - `Google-Chrome-Complete-Guide.md`
  - `Google-Basics-Drive-Sheets-The-Onboarding-Course.md`
  - `DropBox-Fundamentals.md`
  - `Unlocking-Productivity-with-Notion.md`

## Source_Scope
- Platforms:
  - YouTube tutorials focused on file management, workspace hygiene, and productivity workflows.
  - Official docs / guides from Google, Dropbox, and Notion.

- Time window:
  - Default: last **12 months** (file system patterns change slowly).

- Content types:
  - Long-form tutorials, walkthroughs of real setups, “how I organize X” videos.
  - Exclude: generic productivity motivation content without concrete structures.

## Extraction_Targets
- Tools:
  - Chrome, Google Drive, Google Sheets, Dropbox, Notion, and any glue tools (sync/backup utilities, automations).

- Objects:
  - Folders, documents, spreadsheets, shared drives, Notion databases, workspaces, tags.

- Actions / Processes / Results:
  - Actions: organize, archive, tag, share, sync, backup, document, track.
  - Processes: “weekly digital hygiene”, “project documentation workflow”, “client file intake”.

- Responsibilities:
  - Responsibilities for keeping team file systems clean and navigable (e.g., “maintain project folders”, “update documentation”).

- Workflows:
  - Repeatable flows suitable for templates:
    - “Client folder setup in Drive/Dropbox”.
    - “Project documentation in Notion”.
    - “Spreadsheet reporting for weekly metrics”.

- Parameters:
  - Naming conventions, folder patterns, access rules, retention policies.

## Output_Entities
- Libraries_updates:
  - Confirm/update tools and objects in:
    - `LIBRARIES/Tools/Productivity_Tools.json` (or equivalent).
    - `LIBRARIES/Objects/Documents.json`, `Objects/Knowledge_Base.json`, etc.

- Task_managers_updates:
  - Propose Task/Project templates for:
    - File hygiene rituals (weekly/monthly).
    - Standard client/project folder setups.
    - Building and maintaining Notion workspaces linked to oa-y learning.

- Research_reports:
  - A schema-compliant report under `TASK_MANAGERS/RESEARCHES/Research Reports/` that consolidates best practices and gaps.

## Research_Tasks_and_Steps
1. **Course Review**
   - Extract from each oa-y course the recommended patterns (folder structures, workflows).

2. **External Discovery**
   - Search for tutorials like:
     - “how I organize Google Drive”, “Dropbox for agencies”, “Notion workspace for teams”.

3. **Extraction**
   - For each source:
     - Capture folder structures, database schemas, checklists, and maintenance routines.

4. **Mapping to Libraries**
   - Map objects and parameters to existing Libraries entries or propose new ones.

5. **Mapping to Task Managers**
   - Translate best practices into:
     - Task templates (e.g., “Perform weekly file hygiene review”).
     - Project templates (e.g., “Set up client workspace”).

6. **Synthesis**
   - Summarize patterns that are compatible with current team tools and constraints.

## Response_Format

Return:

1. **Narrative summary** grouped by tool and workflow type.
2. **Structured payload**:

```json
{
  "tools": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "task_templates": [ { "...": "..." } ],
  "project_templates": [ { "...": "..." } ],
  "folder_patterns": [ { "...": "..." } ]
}
```

## Quality_Constraints_and_Filters
- Favor:
  - Approaches that scale to multi-client, multi-project environments.
  - Tutorials with clear visual examples of real workspaces.
- Normalize:
  - Naming conventions and structures to your existing folder architecture wherever possible.

## Cross_References
- Research prompts:
  - Any future v2 prompts that specialize per-tool, as needed.

- Libraries:
  - `LIBRARIES/Tools/` (Chrome, Dropbox, Google Drive/Sheets, Notion).
  - `LIBRARIES/Objects/Documents.json`

- Task templates / workflows:
  - File/knowledge management templates in `Task_Templates_Checklist-Item-003.md` and `Workflows_Checklist-Item-003.md`.




## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
