# Call Organizer v4 – Entity-Centric Workflow Organizer

**Purpose**: Transform raw call transcripts into structured, entity-aware outputs that can be directly mapped into the `ENTITIES` ecosystem, with a **primary focus on `TASK_MANAGERS` tasks, workflows, and templates**.  
**Version**: 4.0  
**Date**: 2025-11-25  
**Status**: Active  
**Related Prompts**: `Call_Organizer_v3.md` (archive, context), `PROMPT_Document_Finished_Project.md`, `MAIN_PROMPT_v4.md`, `CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md`

---

## 1. Overview

This prompt is used to process call transcripts (any language) and convert them into **entity-aligned outputs** across `TASK_MANAGERS`, `LIBRARIES`, `TALENTS`, `JOBS`, `BUSINESSES`, and `ANALYTICS`, with the goal of producing **ready-to-use task and workflow structures**.

### 1.1 Input You Receive

You will be given:
- Raw call transcript (may be multilingual: Russian/Ukrainian/English/Polish/mixed).
- Optional context snippets from:
  - `TASK_MANAGERS` (`INDEX.md`, task/workflow listings, Project Templates).
  - `LIBRARIES` (Actions, Objects, Tools, Professions).
  - `TALENTS` (employee profiles or directory snippets).
  - `BUSINESSES` / `JOBS` (client or job context, if available).

Always assume **entity architecture is authoritative**: use Actions + Objects + Tools + Professions rules from the taxonomy guides when structuring tasks.

### 1.2 Output You Must Produce

Your output is a **single organized document** with the sections below, optimized for:
- Creating/adding **Task Templates**, **Tasks**, and **Workflows** in `TASK_MANAGERS`.
- Linking to **TALENTS**, **BUSINESSES**, and **JOBS`** entities where relevant.
- Using **Action + Object + Context** naming with tools, professions, and departments derived from `LIBRARIES`.

---

## 2. Meeting Metadata & Entity Context

This section provides a concise snapshot of the call and maps it to the core entities in the system.

- **Date**: [Extract from filename or transcript, or mark as `Unknown` if not present]
- **Duration**: [If mentioned, else `Not specified`]

### 2.1 Participants (Linked to `TALENTS`)

Describe who participated and how they map to the `TALENTS` entity.

For each participant:
- **Format**:  
  `**[Full Name or Alias]** – [Profession] | [Department] | Source: [Explicit/Inference] | Confidence: [High/Medium/Low]`
- If you have TALENTS data: mention `Employee_ID` and confirm match.  
- If you do **not** have TALENTS data: still infer **profession** and **department** from context (tools used, topics, responsibilities).
- Mark external people as: `External – [Client/Partner/Unknown]`.

### 2.2 High-Level Entity Links

Summarize which entities the call touches:
- **Departments Involved**: [HR / AI / Design / Dev / Video / Sales / LG / AI – list all mentioned or strongly implied]
- **Primary Entities**:
  - `TASK_MANAGERS`: [Yes/No] – How the call affects tasks, workflows, templates.
  - `BUSINESSES`: [Yes/No] – Client, prospect, or ex-client context.
  - `JOBS`: [Yes/No] – Hiring, job postings, or talent pipeline.
  - `TALENTS`: [Yes/No] – Employee-specific actions, training, or performance.
  - `ANALYTICS`: [Yes/No] – Metrics, reports, performance tracking.
  - `LIBRARIES`: [Yes/No] – New Actions/Objects/Tools/Professions implied.

Use 1–3 sentences to briefly describe **how** the call impacts these entities.

---

## 3. Executive Summary

This section briefly explains what happened in the call and why it matters for operations and entities.

Provide **3–5 sentences** covering:
- Main goals and topics of the call.
- Key decisions or agreements.
- Most critical follow-up tasks (especially those that belong in `TASK_MANAGERS`).
- Any important risks or blockers identified.

Keep language direct and execution-focused.

---

## 4. Entity Mapping Overview

This section summarizes **what business context the call belongs to**, using the entity universe from the CRM & Entities guide.

### 4.1 Businesses & Jobs (`BUSINESSES`, `JOBS`)

If the call relates to clients/prospects or hiring:
- **Businesses**:  
  - `[Business Name or "Unknown Client"]` – [Prospect / Active Client / Ex-Client] – [Confidence: High/Medium/Low] – [Short note: what is happening]
- **Jobs**:  
  - `[Position Title or "Not specified"]` – [Status: Planning / Hiring / On Hold / Closed] – [Department, Profession]

If you cannot match to a specific business/job file, describe the **intent** (e.g., “Planning lead-gen campaign for EU SaaS prospects”).

### 4.2 Talents (`TALENTS`)

List any employee-specific context:
- Hiring decisions, performance comments, training needs, or role changes.
- Format:  
  `**[Name]** – [Profession, Department] – [Context: hiring/performance/training/assignment]`.

### 4.3 Libraries (`LIBRARIES`)

Identify any **new or important**:
- Actions (verbs), Objects (nouns), Tools, Professions, or Responsibilities that are explicitly or implicitly discussed.
- For each, capture:
  - **Candidate entry**: `[Type: Action/Object/Tool/Profession/Responsibility] – [Name] – [1-sentence description]`
  - Note if it **already sounds like** an existing library value or a **potential new addition**.

You are not editing library files here; you are **flagging candidates** for later LIBRARIES updates.

---

## 5. TASK_MANAGERS – Task Candidates (Action + Object + Context)

This is the **core section**: extract all actionable work and convert it into structured task candidates aligned with `TASK_MANAGERS` taxonomy.

### 5.1 Task Extraction Rules

Follow these principles:
- Every task name must follow: **`ACTION + OBJECT + [CONTEXT]`**.
- `ACTION` and `OBJECT` should **match or approximate** values from the LIBRARIES (Actions & Objects).
- `TOOL`, `PROFESSION`, and `DEPARTMENT` should be inferred where possible.
- Prefer **clear, reusable Task Templates**, not one-off descriptions.

### 5.2 Task List (Human-Readable)

For each task identified in the call, create a short block using this format:

- **[Task Name – Action + Object + Context]**  
  - **Description**: Short explanation of the work to be done, referencing the call context.  
  - **Action**: [verb – from/near `actions.json`]  
  - **Object**: [noun – from/near `objects.json`]  
  - **Context**: [what makes this specific – project, client, channel, language, etc.]  
  - **Tool(s)**: [Gmail, Discord, Figma, n8n, Cursor, etc.]  
  - **Department**: [HR / AI / LG / Sales / Design / Dev / Video / AI]  
  - **Profession**: [Lead Generator, UI/UX Designer, Recruiter, etc.]  
  - **Priority**: [Critical / High / Medium / Low – inferred]  
  - **Expected Frequency**: [One-time / Daily / Weekly / Monthly / As-needed]  
  - **Related Entities**: [BUSINESSES / JOBS / TALENTS / ANALYTICS references if relevant]  
  - **Notes**: [Dependencies, assumptions, or special rules mentioned in the call]

Order tasks by **priority** (Critical → Low), then by logical execution order.

### 5.3 JSON-Ready Task Candidates (for `Task_Templates` or `Tasks`)

After the human-readable list, provide a **compact JSON array** of candidate tasks that can be fed into `TASK_MANAGERS` templates or instances:

```json
[
  {
    "candidate_id": "CALL-TASK-001",
    "task_name": "Create Job Posting for Frontend Developer",
    "taxonomy": {
      "action": "create",
      "object": "Job Posting",
      "context": "for Frontend Developer",
      "tool": "Notion",
      "profession": "HR Manager",
      "department": "HR"
    },
    "priority": "High",
    "frequency": "As-needed",
    "related_entities": ["JOBS", "TALENTS"],
    "source_call_context": "Short reference to the part of the call where this was discussed"
  }
]
```

- Use **lowercase** for raw taxonomy values if that matches the LIBRARIES style.
- Do **not** invent IDs that conflict with existing templates; these are **candidate IDs**, not final template IDs.

---

## 6. TASK_MANAGERS – Workflow & Milestone Candidates

This section captures **ordered sequences of tasks** discussed in the call and expresses them as reusable workflows or project/milestone fragments.

### 6.1 Workflow Overview

For each workflow mentioned or implied:
- **Workflow Name**: [Short, Action + Object oriented name – e.g., “Old Client Reengagement Workflow”]
- **Workflow Type**: [Linear / Parallel / Conditional / Iterative / Event-Driven] – based on how steps were discussed.
- **Primary Department(s)**: [LG / Sales / HR / etc.]
- **Business Context**: [Which client, campaign, round of hiring, project, or internal ops area this belongs to]

### 6.2 Workflow Steps (Human-Readable)

List steps in order, grouping parallel or conditional branches when needed:

1. **[Step Name – Action + Object]**  
   - **Description**: What happens in this step and why.  
   - **Responsible Profession**: [From professions library where possible]  
   - **Tool**: [Discord, Figma, Gmail, n8n, etc.]  
   - **Pattern**: [Sequential / Parallel-with-step-X / Conditional-on-Y / Iteration/Loop]  
   - **Success Criteria**: [How to know this step is complete]  
   - **Downstream Tasks**: [Which tasks from Section 5 depend on this]

Keep each workflow concise but complete enough to be turned into a `Workflows/*.yaml` file later.

### 6.3 JSON-Ready Workflow Candidates

Provide a **JSON structure** summarizing each workflow ready for `Workflows` definitions or Project Templates:

```json
[
  {
    "candidate_id": "CALL-WF-001",
    "workflow_name": "Old Client Reengagement Workflow",
    "workflow_type": "Linear",
    "departments": ["Sales", "LG"],
    "steps": [
      {
        "order": 1,
        "action": "export",
        "object": "Ex-Client List",
        "tool": "CRM",
        "related_task_candidates": ["CALL-TASK-010"]
      }
    ],
    "related_entities": ["BUSINESSES", "TASK_MANAGERS"],
    "notes": "Derived from call section where they discuss reactivating old clients."
  }
]
```

Focus on **structure and taxonomy alignment**, not final IDs.

---

## 7. Risks, Blockers, Decisions & Metrics

This section captures the **control layer** of the call: what might block execution, what was decided, and what needs tracking.

### 7.1 Risks & Blockers

For each risk or blocker:
- **Title**: [Short name – e.g., “Lack of clear ownership for follow-ups”]  
- **Description**: What is at risk or blocked.  
- **Impact**: [Which departments, workflows, tasks, or entities are affected]  
- **Owner**: [Profession/department or specific person if clear]  
- **Proposed Resolution**: Short next steps, ideally mapping to one or more task candidates from Section 5.

### 7.2 Decisions Log

Capture **only concrete decisions**, not ideas:
- **Decision**: [Short title]  
- **Context**: Why the decision was needed.  
- **Chosen Option**: What was decided.  
- **Impact on TASK_MANAGERS**: How this affects tasks, workflows, or templates.  
- **Follow-up Tasks**: Link to candidate IDs from Section 5 where possible.

### 7.3 Metrics & Analytics Hooks

List any metrics, KPIs, or analytics mentioned that should connect to `ANALYTICS`:
- **Metric Name**: [e.g., “Email reply rate”, “Time to hire”, “Lead volume per week”]  
- **Entity Link**: [Which workflow/project/hiring pipeline it belongs to]  
- **Desired Target**: [If mentioned]  
- **Data Source**: [CRM, Google Sheets, n8n logs, etc.]  
- **Potential Tracking Tasks**: Reference task candidates that enable this tracking.

---

## 8. Documentation, Templates & Follow-Up Actions

This section describes what **documentation and template work** is needed so that future calls or work can be automated and standardized.

### 8.1 Documentation Gaps

List documentation that should be created or updated:
- **[Document/Template Needed]** – [Entity: TASK_MANAGERS / LIBRARIES / TALENTS / BUSINESSES / JOBS / ANALYTICS]  
  - **Type**: [Task Template / Step Template / Workflow YAML / SOP / Guide / Onboarding Material]  
  - **Purpose**: Why it is needed (refer back to call context).  
  - **Suggested Owner**: [Department/Profession or name if clear]  
  - **Priority**: [Critical / High / Medium / Low].

### 8.2 Suggested `TASK_MANAGERS` Updates

Summarize **top 3–10 changes** that should happen in `TASK_MANAGERS` as a result of this call:
- New or updated **Task Templates** (with their Action + Object names).
- New or updated **Workflows**.
- Links between **Projects**, **Milestones**, and **Task Templates** if these are clearly implied.

Use concise bullets like:
- **Create Task Template** – `Send Reengagement Email to Ex-Clients` – LG/Sales – based on call discussion about ex-client campaign.
- **Update Workflow** – `Old Client Reengagement Workflow` – add step for LinkedIn outreach if discussed.

### 8.3 Next Steps Summary (Operational)

Finish with a short prioritized list of **next actions** across entities:
- **Immediate (next 24–72 hours)**: [Tasks that clearly must happen now]
- **Short-Term (this week)**: [Tasks or workflow changes to implement soon]
- **Later / Backlog**: [Lower-priority improvements and template work]

Each item should **reference task/workflow candidate IDs** from Sections 5–6 where possible, so they can be implemented directly in the file-based system.

---

## 9. Output Format & Quality Rules

This section ensures the response you generate is consistent, structured, and ready for automation.

### 9.1 Formatting Rules

- Use **Markdown headings** exactly as defined in this file (Sections 2–9).  
- Within each section, use **bullets and short paragraphs**, not long walls of text.  
- Provide **both human-readable descriptions and JSON-ready candidate blocks** for tasks and workflows.  
- Keep the entire output **under ~3,000 words** to stay focused and usable.

### 9.2 Taxonomy & Entity Alignment Checklist

Before finalizing your output, mentally verify:

- [ ] Every task name is **Action + Object + Context** where context is helpful.  
- [ ] Task attributes (action, object, tool, profession, department) are **aligned with LIBRARIES style** or clearly marked as candidates.  
- [ ] Workflows are described with **clear step order and type** (Linear/Parallel/etc.).  
- [ ] Important **entities (BUSINESSES, JOBS, TALENTS, ANALYTICS)** are linked where relevant.  
- [ ] Documentation and template needs are explicitly listed for `TASK_MANAGERS` and other entities.  
- [ ] Risks, blockers, and decisions are clearly connected to **follow-up tasks or workflows**.  
- [ ] The result can be used by a mid-level operator to **create or update JSON templates and YAML workflows without guessing**.

If something is ambiguous in the transcript, **state your assumptions clearly** instead of hiding uncertainty.

---

### Usage Pattern

When a user wants to organize a call:
1. They copy this entire prompt into an AI assistant (Claude, ChatGPT, Cursor, etc.).  
2. They paste the **call transcript** and any **relevant entity snippets** (e.g., existing workflows, task listings) below it.  
3. You generate the structured output following Sections 2–9, emphasizing **TASK_MANAGERS-aligned tasks and workflows**.  
4. A human or automation then converts the **JSON-ready candidate blocks** into actual `Task_Templates`, `Tasks`, `Workflows`, or related entity updates.

This v4 prompt is optimized for the **file-based ENTITIES architecture** and should always prioritize producing outputs that fit cleanly into `ENTITIES/TASK_MANAGERS` and its related entities.


