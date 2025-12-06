## Prompt_Metadata
- prompt_id: RES-PR-DEV-MCP-001
- version: v2
- owner: Dev / AI Research
- target_departments: [DEV, AI]
- intended_runner: Perplexity or Claude (web + YouTube + GitHub/docs access)

## Topic_Context
- Business objective:  
  Research developer tools and MCP-related workflows (VS Code, Cursor, Agent HQ, MCP connectors) to design Task Manager templates and Libraries entries that support AI-augmented development and integration work.

- Departments / professions:
  - Departments: Development, AI.
  - Professions: frontend developer, backend developer, full stack developer, AI engineer, automation engineer, DevOps engineer.

- Related oa-y courses:
  - `VS-Code-Fundamentals.md`
  - `VS-Code-Launchpad.md`
  - `Cursor-Fundamentals.md`
  - `How-to-Install-Claude-Code-on-Linux.md`
  - `Browser-Extension-Development-Mastery.md`
  - `Integrating-AI-with-the-Model-Context-Protocol-(MCP).md`

## Source_Scope
- Platforms:
  - YouTube developer tutorials and conference talks.
  - GitHub repositories and documentation for MCP, Agent frameworks, and dev tool integrations.
  - Official docs and blogs from tool vendors.

- Time window:
  - Default: last **6–12 months** (developer ecosystem content evolves slightly slower than AI tools news).

- Content types:
  - Live coding sessions, step-by-step tutorials, integration guides, architecture deep dives.
  - Exclude: purely marketing/feature announcements with no code.

## Extraction_Targets
- Tools:
  - VS Code extensions, Cursor, Agent HQ, MCP servers and clients, CLI tools used in workflows.

- Objects:
  - Repositories, services, connectors, dashboards, pipelines, “agent sessions”, dev environments.

- Actions / Processes / Results:
  - Actions: scaffold, generate, refactor, test, debug, deploy, monitor.
  - Processes: “agent-assisted development loop”, “MCP connector lifecycle”, “CI/CD-integrated agent workflows”.

- Responsibilities:
  - Responsibilities for developers and AI engineers around:
    - Maintaining AI-enabled development environments.
    - Designing, implementing, and operating MCP connectors.
    - Ensuring quality and security of agent-driven changes.

- Workflows:
  - End-to-end flows such as:
    - “From idea to deployed microservice with agents.”
    - “Adding tests via agents and MCP.”
    - “Agent-assisted browser extension development.”

- Parameters:
  - MCP configuration parameters, agent resource limits, safety rails, environment variables.

## Output_Entities
- Libraries_updates:
  - Add or update entries in:
    - `LIBRARIES/Tools/Development_Tools/`
    - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`
    - `Processes/Workflows/` for developer/agent workflows.

- Task_managers_updates:
  - Propose:
    - Task/Step templates for key developer/agent workflows.
    - Project templates for “Developer AI onboarding”, “MCP connector implementation”, “Agentic refactor campaign”.

- Research_reports:
  - A developer/MCP-focused mapping report under `TASK_MANAGERS/RESEARCHES/Research Reports/` aligned with `Research_Report_Schema.md`.

## Research_Tasks_and_Steps
1. **Discovery**
   - Search for tutorials on:
     - “VSCode Agent HQ”, “Cursor + Claude”, “MCP connector tutorial”, “AI agents for refactoring”, “agentic coding pipelines”.

2. **Filtering**
   - Prefer:
     - Tutorials with public repos and reproducible steps.
     - Content that shows complete flows from setup to deployment.

3. **Extraction**
   - For each high-quality source:
     - List tools, services, and extensions.
     - Outline steps in the workflow (3–10 steps).
     - Identify where agents change developer responsibilities.

4. **Mapping to Libraries**
   - Map tools and workflows to existing Libraries entries or propose new ones.
   - Identify missing objects and responsibilities for agentic engineering.

5. **Mapping to Task Managers**
   - Propose concrete Task/Step/Project templates:
     - Include action, object, tool, profession, department, and success criteria.

6. **Synthesis**
   - Group findings into categories:
     - Agent-assisted coding, testing, refactoring, documentation, deployment, MCP integration.

## Response_Format

Return:

1. **Narrative summary** grouped by workflow category.
2. **Structured payload**:

```json
{
  "tools": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "task_templates": [ { "...": "..." } ],
  "project_templates": [ { "...": "..." } ]
}
```

## Quality_Constraints_and_Filters
- Focus on:
  - Mature tools with active maintenance.
  - Workflows that can run in realistic team environments.
- Avoid:
  - Overly experimental, single-person hacks without clear value.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/VSCode_Agent_HQ_Research_Prompt.md`

- Research reports:
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_013_Library_Mapping_Report.md`
  - `TASK_MANAGERS/RESEARCHES/Research Reports/Video_013_Gap_Analysis.md`

- Libraries:
  - `LIBRARIES/Tools/Development_Tools/`
  - `LIBRARIES/Objects/Agentic_Engineering_Objects.json`
  - `LIBRARIES/Processes/Workflows/*`

- Task templates / workflows:
  - Developer/AI templates in `Task_Templates_Checklist-Item-003.md` and `Workflows_Checklist-Item-003.md`.


