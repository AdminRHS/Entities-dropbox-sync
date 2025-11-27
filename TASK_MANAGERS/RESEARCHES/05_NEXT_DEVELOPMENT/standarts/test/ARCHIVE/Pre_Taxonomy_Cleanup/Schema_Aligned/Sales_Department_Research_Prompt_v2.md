---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: Sales_Department_Research_Prompt_v2
title: Sales Department Research Prompt v2
date: 2025-11-24
status: archived
owner: unknown
related: []
links: []
---

# Sales Department Research Prompt v2

## Summary
- TODO

## Context
- TODO

## Data / Content
## Prompt_Metadata
- prompt_id: RES-PR-SALES-DEPT-001
- version: v2
- owner: Sales / AI Research
- target_departments: [SALES, SMM, AI]
- intended_runner: Perplexity or Claude (web + YouTube + docs access)

## Topic_Context
- Business objective:  
  Extend and normalize Sales department research so findings become concrete Libraries updates and Task Manager templates for sales workflows, SMM support, and coordination tasks.

- Departments / professions:
  - Departments: Sales, SMM, AI.
  - Professions: sales manager, account manager, SDR/BDR, SMM manager, sales operations specialist, AI/sales automation engineer.

- Related oa-y courses:
  - `RH-Sales-Management-Basic-Course.md`
  - Lead Generation series (1–9) where relevant to sales coordination.
  - Any oa-y materials that cover CRM usage, pipelines, and outreach workflows.

## Source_Scope
- Platforms:
  - YouTube tutorials on sales workflows, CRMs, and AI-assisted selling.
  - Vendor docs and case studies (CRM, sales engagement tools, SMM tools used for sales).

- Time window:
  - Default: last **6 months**.

- Content types:
  - Tutorial and case study videos that show real CRM interfaces and SMM/sales coordination.
  - Exclude: purely conceptual “how to sell more” talks with no system walkthroughs.

## Extraction_Targets
- Tools:
  - CRMs, sales engagement platforms, email/SMM outreach tools, AI assistants for prospecting and follow-up.

- Objects:
  - Leads, opportunities, deals, pipelines, campaigns, sequences, playbooks.

- Actions / Processes / Results:
  - Actions: qualify, nurture, follow-up, propose, close, upsell.
  - Processes: “inbound lead handling”, “outbound campaign”, “renewal/expansion pipeline”.

- Responsibilities:
  - Responsibilities for sales and SMM roles that combine Actions + Objects, e.g., “design multi-channel outreach sequences”, “maintain opportunity pipeline hygiene”.

- Workflows:
  - Multi-channel workflows mixing CRM + SMM (e.g., LinkedIn + email + CRM updates).

- Parameters:
  - Cadence intervals, touchpoint limits, SLA thresholds, qualification criteria.

## Output_Entities
- Libraries_updates:
  - Validate/extend:
    - `LIBRARIES/Tools/Business_Tools/` (CRMs, outreach tools).
    - `LIBRARIES/Objects/Lead_Generation_Objects.json` and related sales objects.
    - `Responsibilities` entries for sales roles.

- Task_managers_updates:
  - Propose:
    - Task/Step templates for:
      - “Daily pipeline hygiene”.
      - “Outbound sequence execution”.
      - “Discovery call follow-up”.
    - Project templates for:
      - “New offer launch campaign”.
      - “Quarterly pipeline cleanup”.

- Research_reports:
  - A schema-compliant Sales department research report under `TASK_MANAGERS/RESEARCHES/Research Reports/` summarizing tools, workflows, and gaps.

## Research_Tasks_and_Steps
1. **Discovery**
   - Search YouTube and vendor resources for:
     - “AI for sales workflows”, “CRM automation tutorial”, “multi-channel sales sequences”.

2. **Filtering**
   - Keep:
     - Tutorials with real system walkthroughs and data structures.
     - Case studies that show clear before/after workflows.

3. **Extraction**
   - For each source, extract:
     - Tools and integrations.
     - Objects and data structures (pipelines, deals).
     - Step-by-step workflows for core processes.

4. **Mapping to Libraries**
   - Map tools/objects/responsibilities to existing Libraries entries or propose new ones.

5. **Mapping to Task Managers**
   - Design candidate Task/Step/Project templates with taxonomy fields populated (action, object, tool, department, profession).

6. **Synthesis**
   - Organize findings by sales process stage (prospecting, qualification, proposals, closing, expansion).

## Response_Format

Return:

1. **Narrative summary** by sales process stage.
2. **Structured payload**:

```json
{
  "tools": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "responsibilities": [ { "...": "..." } ],
  "task_templates": [ { "...": "..." } ],
  "project_templates": [ { "...": "..." } ]
}
```

## Quality_Constraints_and_Filters
- Favor:
  - Workflows suitable for small, remote-first teams.
  - Content with clear examples, metrics, or dashboards.
- Avoid:
  - Aggressive or non-compliant outreach strategies that do not fit existing policies.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/Sales_Department_Research_Prompt.md`

- Libraries:
  - `LIBRARIES/Objects/Lead_Generation_Objects.json`
  - `LIBRARIES/Tools/Business_Tools/*`
  - `LIBRARIES/Responsibilities/responsibilities.json`

- Task templates / workflows:
  - Lead-gen and sales templates in `Task_Templates_Checklist-Item-003.md` and `Workflows_Checklist-Item-003.md`.




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
