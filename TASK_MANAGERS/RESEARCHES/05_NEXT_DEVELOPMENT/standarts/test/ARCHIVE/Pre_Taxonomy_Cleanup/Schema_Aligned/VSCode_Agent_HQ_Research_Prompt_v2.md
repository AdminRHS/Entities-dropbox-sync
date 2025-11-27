---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: VSCode_Agent_HQ_Research_Prompt_v2
title: VSCode Agent HQ Research Prompt v2
date: 2025-11-17
status: archived
owner: unknown
related: []
links: []
---

# VSCode Agent HQ Research Prompt v2

## Summary
- TODO

## Context
- TODO

## Data / Content
## Prompt_Metadata
- prompt_id: RES-PR-VSC-AGENT-HQ-001
- version: v2
- owner: Dev / AI Research
- target_departments: [DEV, AI]
- intended_runner: Perplexity or Claude (web + YouTube/docs access)

## Topic_Context
- Business objective:  
  Research VS Code + agent frameworks (VSCode Agent HQ and adjacent tools) to design developer workflows, Task templates, and Libraries entries that support AI-powered development across the stack (frontend, backend, automation).

- Departments / professions:
  - Departments: Dev, AI
  - Professions: frontend developer, backend developer, full stack developer, AI engineer, prompt engineer, automation engineer.

- Related oa-y courses:
  - `VS-Code-Fundamentals.md`
  - `VS-Code-Launchpad.md`
  - `Cursor-Fundamentals.md`
  - `Browser-Extension-Development-Mastery.md`
  - `Integrating-AI-with-the-Model-Context-Protocol-(MCP).md`

## Source_Scope
- Platforms:
  - YouTube (tutorials, live coding sessions).
  - GitHub repositories and docs for Agent HQ and similar tools.
  - Blog posts / docs linked from videos.

- Time window:
  - Primary: last **90 days** for videos and articles.

- Content types:
  - Tool walkthroughs, sample projects, agent orchestration examples, MCP or extension integrations.
  - Exclude marketing-only launch videos without real code or examples.

## Extraction_Targets
- Tools:
  - VS Code extensions and agent frameworks (Agent HQ, Cursor integrations, AI copilots, MCP-related extensions).

- Objects:
  - Developer objects: repositories, branches, pull requests, issues, tests, pipelines, MCP connectors, browser extensions.

- Actions / Processes / Results:
  - Actions: generate, refactor, test, debug, review, scaffold, migrate.
  - Processes: “agent-assisted refactoring”, “test generation with agents”, “multi-repo orchestration”.

- Responsibilities:
  - Responsibilities for developers and AI engineers related to:
    - Maintaining AI-assisted dev environments.
    - Designing and iterating agent workflows.
    - Ensuring code quality and performance in an AI-heavy workflow.

- Workflows:
  - End-to-end patterns such as:
    - “From blank repo to deployed service using agents.”
    - “Adding tests and refactors via agents.”
    - “Agent workflows for MCP connector development and validation.”

- Parameters:
  - Configuration for agent workflows (model choices, context limits, safety rails, automation thresholds).

## Output_Entities
- Libraries_updates:
  - New or refined entries under:
    - `LIBRARIES/Tools/Development_Tools/` (agent frameworks, VS Code extensions).
    - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`.
    - `Processes/Workflows/` for agentic engineering flows.

- Task_managers_updates:
  - Proposed Task and Step templates for:
    - “AI-assisted feature development”.
    - “Agent-driven refactor + test cycle”.
    - “MCP connector creation & validation”.
    - “Extension-driven dev environment setup”.

- Research_reports:
  - A mapping report summarizing:
    - Which agent tools are most mature.
    - Which workflows are production-ready vs experimental.

## Research_Tasks_and_Steps
1. **Discovery**
   - Search for: “VSCode Agent HQ”, “AI agents in VS Code”, “agentic coding pipelines”, “MCP development in VS Code”.
   - Collect both video and repo/documentation links.

2. **Filtering**
   - Prefer:
     - Tutorials with working examples and source code.
     - Content showing **complete flows** (not just one-off tricks).
   - Exclude:
     - Early-stage tools without enough documentation or examples.

3. **Extraction**
   - For each high-quality source:
     - List tools involved (VS Code extension names, companion services).
     - Describe the overall workflow in 3–8 steps.
     - Identify where agents replace or augment manual developer tasks.

4. **Mapping to Libraries**
   - Map tools to `Development_Tools` and related categories.
   - Map workflows to `Processes/Workflows` as named flows (e.g., `WF-DEV-AGENT-REFactor-001`).
   - Identify any new objects (e.g., “agent-run logs”, “agent sessions”).

5. **Mapping to Task Managers**
   - Propose:
     - Task templates that wrap each major agent workflow.
     - Step templates that describe each key action (with tools and success criteria).
   - Suggest which templates belong under DEV vs AI departments.

6. **Synthesis**
   - Group findings into:
     - “Agent-assisted coding”.
     - “Agent-assisted testing”.
     - “Agent-assisted documentation & refactoring”.
     - “MCP/connector workflows”.

## Response_Format

Return:

1. **Narrative summary** (markdown) by workflow category.

2. **Structured payload**:

```json
{
  "tools": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "task_templates": [
    {
      "suggested_name": "Generate Tests with Agent in VS Code",
      "action": "generate",
      "object": "tests",
      "tool": "Agent HQ (VS Code extension)",
      "department": "DEV",
      "profession": "frontend developer",
      "steps_summary": ["..."]
    }
  ]
}
```

## Quality_Constraints_and_Filters
- Focus on:
  - Realistic, reproducible workflows that can be implemented by the current team.
  - Tools with active maintenance and documentation.
- Avoid:
  - Extremely experimental setups without clear value.
  - Workflows that require infrastructure the organization does not plan to adopt.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/VSCode_Agent_HQ_Research_Prompt.md`

- Libraries:
  - `LIBRARIES/Tools/Development_Tools/`
  - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`
  - `LIBRARIES/Processes/Workflows/*`

- Task templates / workflows:
  - Any DEV/AI Task templates referencing VS Code / Cursor / MCP in `Task_Templates_Checklist-Item-003.md`.




## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-17 standardization scaffold added
