---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: SMM_Research_Document_Processing_Instructions_v2
title: SMM Research Document Processing Instructions v2
date: 2025-11-24
status: archived
owner: unknown
related: []
links: []
---

# SMM Research Document Processing Instructions v2

## Summary
- TODO

## Context
- TODO

## Data / Content
## Prompt_Metadata
- prompt_id: RES-PR-SMM-RESEARCH-DOCS-001
- version: v2
- owner: SMM / AI Research
- target_departments: [SMM, MARKETING, DESIGN, AI]
- intended_runner: Claude or Perplexity with access to local / cloud documents

## Topic_Context
- Business objective:  
  Process existing and new SMM research documents (strategies, session logs, experiments) into structured updates for Libraries (tools, objects, responsibilities) and Task Managers (SMM workflows and tasks).

- Departments / professions:
  - Departments: SMM, marketing, design, AI.
  - Professions: SMM manager, content strategist, copywriter, designer, AI marketing specialist.

- Related existing assets:
  - `TASK_MANAGERS/RESEARCHES/SMM/*.md` (session prompts, strategy docs, integration reports).
  - `LIBRARIES/Objects/Design_Deliverables.json`, `Lead_Generation_Objects.json`.
  - `LIBRARIES/Tools/Social_Media_Platforms/` and SMM-related AI tools.

## Source_Scope
- Sources:
  - Existing SMM research markdown files under `TASK_MANAGERS/RESEARCHES/SMM/`.
  - New SMM research notes or exported documents provided to the model (as text or attachments).

- Content types:
  - Strategy docs, audits, experiments, reports, session prompts, and extraction outputs.

## Extraction_Targets
- Tools:
  - Social platforms, schedulers, analytics tools, AI content tools (image/video/copy).

- Objects:
  - SMM deliverables: posts, carousels, thumbnails, stories, campaigns, content plans, briefs.

- Actions / Processes / Results:
  - Actions like plan, schedule, publish, engage, test, optimize.
  - Processes such as “weekly content planning”, “campaign launch”, “A/B testing”.

- Responsibilities:
  - Responsibilities for SMM manager, designer, copywriter, etc. (e.g., “planning monthly content calendar”, “optimizing post performance reports”).

- Workflows:
  - Repeatable SMM processes that can be turned into Task and Project templates (e.g., “Instagram campaign workflow”, “LinkedIn content strategy for B2B”).

## Output_Entities
- Libraries_updates:
  - Updates to:
    - `Tools` for SMM and analytics tools.
    - `Objects` for SMM deliverables.
    - `Responsibilities` for SMM-related roles.

- Task_managers_updates:
  - Suggestions for:
    - SMM Task templates (per platform / per campaign).
    - SMM Project templates (e.g., “30-day campaign launch”).
    - Checklists and steps for content production workflows.

- Research_reports:
  - A structured summary of each processed document under `TASK_MANAGERS/RESEARCHES/SMM/` or `Research Reports/`, conforming to `Research_Report_Schema.md`.

## Research_Tasks_and_Steps
1. **Document Intake**
   - Read the provided SMM research document(s).
   - Identify their type: strategy, experiment, audit, instructions, or mixed.

2. **Concept Extraction**
   - Extract:
     - Tools and platforms mentioned.
     - Content types and deliverables.
     - Described workflows and sequences.
     - Role responsibilities and expectations.

3. **Mapping to Libraries**
   - Link tools to existing entries or suggest new ones.
   - Map deliverables to existing `Objects` or propose new SMM-specific object types.
   - Map responsibilities to the responsibility library (Action+Object phrases).

4. **Mapping to Task Managers**
   - Propose:
     - Task templates for recurring SMM activities (ideally tied to departments/professions).
     - Step templates where the document gives detailed step-by-step instructions.
     - Project templates for multi-week campaigns or recurring series.

5. **Synthesis**
   - For each processed document, produce:
     - A short human summary (1–3 paragraphs).
     - A machine-structured block listing tools, objects, workflows, responsibilities, and template suggestions.

## Response_Format

Return a **per-document** structure like:

```json
{
  "document_name": "Content Strategy & Categories by Platform.md",
  "summary": "...",
  "tools": [ { "...": "..." } ],
  "objects": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "responsibilities": [ { "...": "..." } ],
  "task_templates": [ { "...": "..." } ],
  "project_templates": [ { "...": "..." } ]
}
```

## Quality_Constraints_and_Filters
- Preserve:
  - Platform-specific nuances (what works on Instagram vs LinkedIn, etc.).
  - Attribution: where ideas came from (internal vs external sources).
- Normalize:
  - Terms to the nearest matching entries in Libraries when possible.
  - Role names to `Professions` definitions (e.g., “SMM manager”, “graphic designer”).

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/SMM_Research_Document_Processing_Instructions.md`

- Libraries:
  - `LIBRARIES/Objects/Design_Deliverables.json`
  - `LIBRARIES/Objects/Lead_Generation_Objects.json`
  - `LIBRARIES/Tools/Social_Media_Platforms/*`

- Task templates / workflows:
  - Any SMM/Marketing-related templates referenced in `Task_Templates_Checklist-Item-003.md`.
  - SMM research docs already in `TASK_MANAGERS/RESEARCHES/SMM/`.




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
