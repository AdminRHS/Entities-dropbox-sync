---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: oa-y_AI_Tools_Alignment_Research_Prompt_v2
title: oa-y AI Tools Alignment Research Prompt v2
date: 2025-11-24
status: archived
owner: unknown
related: []
links: []
---

# oa-y AI Tools Alignment Research Prompt v2

## Summary
- TODO

## Context
- TODO

## Data / Content
## Prompt_Metadata
- prompt_id: RES-PR-OAY-AI-TOOLS-ALIGN-001
- version: v2
- owner: AI Research / Architecture
- target_departments: [AI, DEV, LG, HR, SMM, SALES]
- intended_runner: Perplexity or Claude (web + YouTube + docs access)

## Topic_Context
- Business objective:  
  Align oa-y AI tools courses with `LIBRARIES` and `TASK_MANAGERS` by discovering missing workflows, responsibilities, and templates for each core AI tool in the stack.

- Departments / professions:
  - Departments: AI, Development, Lead Generation, HR, SMM, Sales.
  - Professions: lead generator, recruiter, HR manager, SMM manager, sales manager, frontend/backend developer, AI engineer, automation specialist.

- Related oa-y courses:
  - `Getting-Started-with-ChatGPT-2025.md`
  - `Getting-Started-with-Claude-AI-2025.md`
  - `Getting-Started-with-Gemini-AI.md`
  - `Onboarding-for-AI.md`
  - `Mastering-Notebook-LM.md`
  - `Create-Notebook-LM.md`
  - `Cursor-Fundamentals.md`

## Source_Scope
- Platforms:
  - Primary: YouTube tutorials and deep dives for each AI tool.
  - Secondary: official docs, blog posts, and changelogs linked from videos.

- Time window:
  - Default: last **90 days** for tutorials and feature updates.

- Content types:
  - Tutorials, “what’s new” feature overviews with demos, workflow breakdowns, case studies.
  - Exclude: purely marketing/announcement videos without concrete workflows.

## Extraction_Targets
- Tools:
  - ChatGPT, Claude, Gemini, NotebookLM, Cursor, and closely related tools used in oa-y courses.

- Objects:
  - AI outputs and artefacts such as: briefs, scripts, prompts, knowledge bases, notebooks, workspaces, multi-step workflows, automations.

- Actions / Processes / Results:
  - Actions: brainstorm, rewrite, summarize, generate, plan, refactor, debug, document.
  - Processes: “AI-assisted research loop”, “daily AI-assisted planning”, “AI pair-programming workflow”.

- Responsibilities:
  - Responsibilities per profession that leverage AI tools (e.g., “maintain AI research notebooks for LG”, “design AI-assisted recruitment workflows”).

- Workflows:
  - End-to-end flows where AI tools are core components, suitable for Task/Project templates (e.g., “AI-assisted candidate sourcing”, “AI-augmented content calendar creation”).

- Parameters:
  - Important prompt patterns, safety settings, model selection rules, context window strategies that should live in `LIBRARIES/Parameters`.

## Output_Entities
- Libraries_updates:
  - For each tool covered by oa-y:
    - Confirm presence in `LIBRARIES/Tools/AI_Tools/` or propose new entries.
    - Propose responsibilities, workflows, parameters that are missing today.

- Task_managers_updates:
  - For each key oa-y tool + department combination:
    - Candidate Task/Step templates that operationalize the workflows taught in courses.
    - Candidate Project templates for “AI onboarding” and “AI adoption” projects per department.

- Research_reports:
  - A schema-compliant alignment report under `TASK_MANAGERS/RESEARCHES/Research Reports/` summarizing per-tool gaps and recommended templates.

## Research_Tasks_and_Steps
1. **Course-Centric Inventory**
   - For each listed oa-y course, identify the core tools and workflows it teaches.

2. **External Research**
   - For each tool, search for recent tutorials and deep dives.
   - Prefer content that demonstrates end-to-end flows aligned with oa-y use cases.

3. **Extraction**
   - For each tool + source:
     - Extract workflows, responsibilities, parameters, and key artefacts.

4. **Mapping to Libraries**
   - Map findings to existing tool, object, responsibility, and parameter entries.
   - Flag missing or underspecified entities.

5. **Mapping to Task Managers**
   - Propose Task/Step/Project templates that reflect actual workflows from oa-y courses + external sources.

6. **Per-Tool Synthesis**
   - For each tool, summarize:
     - What oa-y teaches.
     - What the external ecosystem adds.
     - Concrete template and library changes needed.

## Response_Format

Return:

1. **Human-readable summary** organized by tool and department.
2. **Machine-structured block**:

```json
{
  "tools": [ { "...": "..." } ],
  "per_tool_alignment": [
    {
      "tool": "Claude",
      "oa_y_courses": ["Getting-Started-with-Claude-AI-2025.md"],
      "workflows": ["..."],
      "responsibilities": ["..."],
      "task_templates_suggested": ["..."],
      "project_templates_suggested": ["..."]
    }
  ]
}
```

## Quality_Constraints_and_Filters
- Focus on:
  - Workflows that a small remote team can realistically adopt.
  - Sources that show real interfaces and tangible outcomes.
- Normalize:
  - Terms to existing Libraries entities when possible.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/YouTube_AI_Tools_Daily_Research_Prompt.md`

- Research reports:
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_005_Library_Mapping_Report.md`
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_006_Library_Mapping_Report.md`
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_008_Library_Mapping_Report.md`

- Libraries:
  - `LIBRARIES/Tools/AI_Tools/`
  - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`
  - `LIBRARIES/Parameters/*`

- Task templates / workflows:
  - AI-related templates in `Task_Templates_Checklist-Item-003.md` and `Project_Templates_Checklist-Item-003.md`.




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
