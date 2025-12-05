# VS Code Agent HQ Announcement Research Prompt

**Category:** Research / AI Tool Launch Tracking  
**Location:** `LIBRARIES/Prompts/Research/`  
**Purpose:** Guide any external AI researcher to collect structured, ingestion-ready knowledge about the newly announced **VS Code Agent HQ** feature inside Visual Studio Code.  
**Last Updated:** 2025-11-14  
**Maintainer:** Taxonomy Team

---

## 1. When to Use This Prompt
- The VS Code team ("VS Code" or Microsoft) publishes a new **Agent HQ** experience and we need immediate research on the launch that happened **today** (use the actual calendar date in ISO format).
- We must understand how Agent HQ changes developer workflows so we can update LIBRARIES (Actions, Tools, Processes, Skills, Task Managers) and Task Manager templates.
- The researcher does **not** have access to this repository and needs full context, structure, and formatting instructions.

**Primary Research Question**  
> Tell me more about the feature announced today by the VS Code / Agent HQ team inside VS Code. Capture announcement details, workflows, adoption steps, risks, and taxonomy mapping so Remote Helpers can operationalize it immediately.

---

## 2. Remote Helpers Context (Share with Researcher)
1. Remote Helpers standardizes work through `TASK = ACTION + OBJECT + TOOL + CONTEXT` and `SKILL = RESULT + OBJECT + ("via/using/in") + TOOL`.
2. LIBRARIES store actions, processes, results, tools, objects, professions, skills, templates, and researches that fuel TASK_MANAGERS, JOBS, and TALENTS.
3. We monitor AI tool releases so we can add workflows, responsibilities, and onboarding steps the same day they are announced.
4. Research output must map findings back to those primitives (actions, objects, tools) and identify which entity or template should be updated.

---

## 3. Research Scope & Deliverables
- **Announcement Verification:** Confirm the exact release date/time, official naming, roll-out stage (preview, beta, GA), and the communication channel (blog, VS Code release notes, GitHub post, livestream, X post, etc.).
- **Feature Deep Dive:** Identify everything Agent HQ enables (agent management UI, preset agents, marketplace integration, workspace context sharing, debugging agents, etc.).
- **Workflow Mapping:** Translate each capability into actionable workflows using ACTION + OBJECT language and specify supporting tools (VS Code, GitHub Copilot, Azure AI, extensions, API endpoints).
- **Adoption Playbook:** Provide sequential steps for Remote Helpers teams to evaluate, enable, configure, integrate, and train on Agent HQ.
- **Risks & Unknowns:** Document licensing, security, telemetry, known limitations, geographic availability, or unanswered questions.
- **Source Appendix:** Minimum of 3 credible sources with timestamps, emphasizing official Microsoft content first; note any speculative coverage separately.

Required metadata for each finding:
1. Announcement title, author, channel, and permalink.
2. Release date/time (ISO + timezone if provided) and stage (Insiders, Stable, Preview, GA, Public Beta).
3. Dependencies (VS Code version, GitHub Copilot subscription, Azure OpenAI access, extension IDs, OS requirements).
4. Pricing/licensing statements (free, requires Copilot Individual/Business, or enterprise SKU).
5. Feature list with short descriptions and targeted personas (developers, prompt engineers, automation builders).
6. Tooling references (models, endpoints, VS Code commands, CLI flags, settings sync behaviour).
7. Suggested KPIs (onboarding time, tasks automated, debugging turnaround, etc.).

---

## 4. Research Workflow for the AI Researcher
1. **Anchor Date:** Treat "today" as the research date (record `research_date = YYYY-MM-DD`). Cross-check every source to confirm it references the same-day announcement or note if it is a preview/leak.
2. **Source Priority:**
   - Tier 1: Official VS Code blog, Microsoft Dev Blogs, Visual Studio release notes, GitHub repository announcements, Agent HQ documentation, Microsoft Build / Ignite keynotes.
   - Tier 2: Verified journalist or developer tools publications (e.g., The Verge, TechCrunch, dev.to) referencing the release.
   - Tier 3: Social posts from VS Code engineers or product managers. Use only for corroboration; mark as such.
3. **Evidence Logging:** For each source capture `source_name`, `source_type`, `url`, `publish_time`, `reliability_score (High/Medium/Low)`, and `why_it_matters`.
4. **Extraction:** For every capability or quote, map it to ACTION + OBJECT + TOOL, note prerequisites, and identify impacted departments (Developers, AI Team, Automation Specialists, QA).
5. **Validation:** Cross-reference at least two sources for any critical claim (release date, availability, pricing). Flag contradictions in the Risks section.
6. **Output Assembly:** Follow the markdown structure below exactly. Use tables when specified. All times/dates in ISO (UTC when possible).

---

## 5. Required Output Structure (Markdown Only)
### 5.1 Executive Summary
- 4–6 bullets summarizing the announcement, most important capabilities, and immediate actions for Remote Helpers.

### 5.2 Announcement Snapshot Table
Provide a table with columns: `Field | Value`. Required rows: `Announcement Name`, `Official Channel`, `Publish Date/Time`, `Release Stage`, `Target Users`, `Dependency`, `Official Docs Link`, `Supporting Media (video/livestream)`, `Research Date`.

### 5.3 Feature Breakdown
For each capability (minimum 3):
```
CAPABILITY: <Name>
PROBLEM SOLVED: ...
HOW IT WORKS: ...
ACTION + OBJECT + TOOL: ...
DEPENDENCIES: ...
RELEASE STATUS: Preview | GA | TBD
NOTES: include models/agents involved
```

### 5.4 Workflow & Taxonomy Mapping
- Provide a table with columns `Workflow Candidate`, `Action + Object`, `Primary Tool(s)`, `Context/Trigger`, `Library Updates Needed` (Actions/Processes/Tools/Skills/Task_Manager templates). Include at least 4 workflows derived from Agent HQ usage (e.g., "Coordinating multi-agent debugging sessions inside VS Code").

### 5.5 Adoption Playbook
Break into phases:
1. **Evaluate** – discovery questions, documentation review, PoC scope.
2. **Enable** – prerequisites, VS Code settings, extension installs, feature flags.
3. **Integrate** – linking to repositories, Task Manager templates, automation hooks (n8n/GitHub Actions).
4. **Operationalize** – training, governance, KPIs, documentation tasks.

For each phase list:
- Responsible department/professions
- ACTION + OBJECT sentences
- Deliverables and tools
- Estimated effort (hours/days) if provided

### 5.6 Risk, Limitations & Open Questions
- Bullet list of technical risks, licensing limits, telemetry/privacy considerations, geographic availability, or missing info that requires follow-up.

### 5.7 Integration Opportunities
- Describe at least 3 specific Remote Helpers use cases. For each include: `Use Case Name`, `Trigger`, `Action + Object + Tool`, `Expected Result`, `Department`, `Libraries Impacted`.

### 5.8 Metrics & KPIs
- Provide suggested metrics to monitor Agent HQ adoption (time-to-configure, agent response latency, % of tasks automated, debugging turnaround). Indicate which PARAMETERS entity fields they would map to.

### 5.9 Source Appendix
- Table with `Source`, `Type`, `URL`, `Publish Date/Time`, `Key Insight`, `Reliability`. Ensure at least 3 entries and cite any quotes inline like `[Source #]`.

---

## 6. Reporting Standards & Formatting Rules
1. **Markdown Only:** No JSON. Use headings, tables, and fenced code blocks as instructed.
2. **Citations:** Use inline `[Source #]` referencing numbering from the Source Appendix.
3. **Timestamps:** Convert to ISO 8601; if only day is available, note `time = unknown`.
4. **Terminology:** Refer to the feature as "VS Code Agent HQ" unless an official variation is provided.
5. **Normalization:** Convert marketing taglines into actionable verbs/nouns (e.g., "coordinate agents" → `Coordinating multi-agent prompts using VS Code Command Palette`).
6. **Assumptions:** Clearly flag anything inferred and mark as `ASSUMPTION`.
7. **Comparisons:** If sources mention related features (e.g., GitHub Copilot Workspace, VS Code agents preview), briefly compare and note if they are separate or merged.

---

## 7. Quality Checklist (Researcher must confirm)
- [ ] Executive Summary present with 4–6 bullets.
- [ ] Announcement snapshot table includes research date and release stage.
- [ ] Minimum 3 capabilities documented with ACTION + OBJECT + TOOL mapping.
- [ ] Workflow table lists ≥4 entries referencing relevant LIBRARIES updates.
- [ ] Adoption Playbook covers Evaluate → Enable → Integrate → Operationalize with responsibilities.
- [ ] Risks/Unknowns section captures licensing, availability, and telemetry concerns.
- [ ] Integration opportunities detail 3 Remote Helpers use cases.
- [ ] Metrics/KPIs mapped to PARAMETERS suggestions.
- [ ] Source appendix with ≥3 credible links and inline citations used.
- [ ] All data ties back to the same-day announcement or is labelled otherwise.

---

## 8. Version History
- **v1.0 (2025-11-14):** Initial prompt to research the same-day VS Code Agent HQ announcement and translate findings into taxonomy-ready outputs.

Use this prompt verbatim when tasking Perplexity, Claude, or other AI researchers so their findings align with Remote Helpers' LIBRARIES ingestion standards.
