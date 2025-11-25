## Prompt_Metadata
- prompt_id: RES-PR-YT-AI-TOOLS-001
- version: v2
- owner: AI Research / Architecture
- target_departments: [AI, DEV, LG, DESIGN, SALES]
- intended_runner: Perplexity or Claude (web + YouTube access)

## Topic_Context
- Business objective:  
  Discover newly released AI tools, features, and workflows from YouTube tutorials and map them into `LIBRARIES` and `TASK_MANAGERS` so they can be used in onboarding, workflows, and automation projects.

- Departments / professions (Libraries alignment):  
  - Departments: managers (HR), developers, designers, marketers (LG/SMM), sales  
  - Professions (examples): lead generator, recruiter, sales manager, UI/UX designer, frontend developer, backend developer, AI engineer, automation specialist

- Related oa-y courses (learning context):  
  - `Getting-Started-with-ChatGPT-2025.md` (AI & Tools)  
  - `Getting-Started-with-Claude-AI-2025.md` (AI & Tools)  
  - `Getting-Started-with-Gemini-AI.md` (AI & Tools)  
  - `Mastering-Notebook-LM.md` / `Create-Notebook-LM.md` (AI & Tools)  
  - `Cursor-Fundamentals.md` (Development)  
  - `Onboarding-for-AI.md` (AI & Tools, general)

## Source_Scope
- Platforms:
  - Primary: YouTube
  - Secondary (optional): blog posts and official docs linked from video descriptions

- Time window:
  - Default: videos published in the **last 30 days**
  - If too few results: extend to **last 60 days**, but clearly mark older content

- Content types:
  - Tutorials, how-to guides, live coding sessions, case studies, workshop replays
  - Exclude: purely marketing/announcement videos with no concrete workflows

- Language / region:
  - Primary: English-language content
  - Secondary: optionally include high-signal non‑English tutorials; clearly tag language

## Extraction_Targets
- Tools:
  - Identify AI tools and services that are:
    - New to our taxonomy (not yet in `LIBRARIES/Tools/*`)
    - Existing tools with **new capabilities or usage patterns**

- Objects:
  - New deliverables or entities introduced by tools (e.g., “agentic workflows”, “RAG graphs”, “AI dashboards”, “multi-agent projects”).

- Actions / Processes / Results:
  - Standardized verbs and processes that describe how tools are used (aligned with `Actions`, `Processes`, `Results` libraries).

- Responsibilities:
  - New or refined Action+Object responsibilities for professions (e.g., “orchestrating AI agents”, “configuring MCP connectors”).

- Workflows:
  - Task and workflow patterns (step-by-step sequences) that could become:
    - Project templates.
    - Task/Step templates.
    - Workflows under `Processes/Workflows/`.

- Parameters:
  - Important configuration parameters (API limits, model choices, prompt structures, automation thresholds) that belong in `LIBRARIES/Parameters`.

## Output_Entities
- Libraries_updates:
  - Candidate entries for:
    - `Tools/*` (new tools, or additions to existing tool JSON).
    - `Objects/*` (new object types).
    - `Responsibilities` (new responsibilities built from Actions + Objects).
    - `Processes/Workflows/*` (named workflow patterns).
    - `Parameters/*` (per-tool or per-department parameters).

- Task_managers_updates:
  - Suggestions for:
    - New Task Templates (Action + Object + Context) based on discovered workflows.
    - New Step Templates (fine-grained actions with tools and success criteria).
    - New or updated Project Templates (multi-phase AI adoption or automation projects).
    - New or updated Workflows in `TASK_MANAGERS/Workflows/`.

- Research_reports:
  - A schema-compliant report under `TASK_MANAGERS/RESEARCHES/Research Reports/` summarizing:
    - Tools discovered/updated.
    - Workflows discovered.
    - Gaps and recommendations.

## Research_Tasks_and_Steps
1. **Discovery**
   - Search YouTube for newly published AI tool tutorials and overviews using combinations of:
     - “AI tools tutorial”, “AI workflow”, “agentic AI”, “automation with [tool]”, “MCP connectors”, “AI coding tools”, “RAG tutorial”, etc.
   - Filter to the configured time window (30–60 days).

2. **Filtering**
   - Include only videos that:
     - Demonstrate concrete workflows or step-by-step usage.
     - Use tools relevant for at least one of the target departments/professions.
     - Have meaningful engagement (views, likes, comments) relative to channel size.

3. **Extraction**
   - For each selected video, extract:
     - Tool(s) used (names + categories).
     - High-level workflow description.
     - Step-by-step tasks (human-readable).
     - Key parameters and settings.
     - Mentioned professions/departments / use cases.

4. **Mapping to Libraries**
   - For each tool / workflow:
     - Mark whether the tool is already present in `LIBRARIES/Tools`.
     - Propose new tools or updates where needed.
     - Propose new responsibilities and objects where gaps are found.

5. **Mapping to Task Managers**
   - For each high-value workflow:
     - Propose Task/Step templates with:
       - `action`, `object`, `tool`, `profession`, `department`.
       - Estimated duration and dependencies.
     - Suggest how these could become part of existing or new Project Templates (e.g., “AI stack rollout”, “agentic coding pipeline”).

6. **Synthesis**
   - Summarize per-topic (e.g., AI coding, RAG, automation, SMM tools).
   - Prioritize tools/workflows by impact and alignment with oa-y courses and current Libraries.

## Response_Format

The assistant should return:

1. **Human-readable summary (markdown)** with:
   - Overview by topic/theme.
   - Short descriptions of each new or important tool.
   - Short descriptions of each high-value workflow.

2. **Machine-structured block** (JSON-like, in fenced code) with this shape:

```json
{
  "tools": [
    {
      "name": "ExampleTool",
      "category": "AI_Tools | Development_Tools | Automation_Tools | ...",
      "status": "new | existing",
      "libraries_path": "relative/path/if_existing_or_suggested.json",
      "primary_departments": ["DEV", "AI"],
      "primary_professions": ["frontend developer", "ai engineer"],
      "use_cases": ["..."],
      "source_videos": ["YouTube URL 1", "YouTube URL 2"]
    }
  ],
  "workflows": [
    {
      "name": "Short descriptive name",
      "description": "...",
      "steps": ["Step 1 ...", "Step 2 ..."],
      "tools": ["ExampleTool"],
      "departments": ["DEV"],
      "professions": ["frontend developer"],
      "maps_to_task_templates": ["(optional existing template IDs)"]
    }
  ],
  "responsibilities": [
    {
      "phrase": "creating AI agent workflows",
      "actions": ["create"],
      "objects": ["AI agent workflow"],
      "departments": ["AI"],
      "professions": ["ai engineer"]
    }
  ],
  "parameters": [
    {
      "name": "max_concurrent_jobs",
      "tool": "ExampleTool",
      "description": "Maximum concurrent jobs for safe operation",
      "department": "AI",
      "profession": "automation engineer"
    }
  ]
}
```

## Quality_Constraints_and_Filters
- Prioritize tutorials and deep dives over short marketing snippets.
- Prefer videos with:
  - Clear narration and visuals.
  - Reproducible, step-by-step instructions.
  - Realistic examples, not toy demos only.
- Exclude tools and workflows that:
  - Are clearly deprecated or replaced.
  - Do not fit into any target department/profession.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/YouTube_AI_Tools_Daily_Research_Prompt.md` (original v1 prompt).

- Research reports:
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_005_Library_Mapping_Report.md`
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_006_Library_Mapping_Report.md`
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_008_Library_Mapping_Report.md`

- Libraries:
  - `LIBRARIES/Tools/` (AI_Tools, Development_Tools, Automation_Tools, Web_Tools, etc.).
  - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`
  - `LIBRARIES/Processes/Workflows/*.json`

- Task templates / workflows:
  - Existing AI-related Task and Project templates listed in `TASK_MANAGERS/INDEX.md` and `LIBRARIES_Import_Index.md` Phase 4–9 plan.


