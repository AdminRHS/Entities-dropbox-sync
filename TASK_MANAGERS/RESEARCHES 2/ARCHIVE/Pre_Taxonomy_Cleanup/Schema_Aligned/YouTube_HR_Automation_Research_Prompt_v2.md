## Prompt_Metadata
- prompt_id: RES-PR-YT-HR-AUTO-001
- version: v2
- owner: HR / AI Research
- target_departments: [HR, AI, OPS]
- intended_runner: Perplexity or Claude (web + YouTube access)

## Topic_Context
- Business objective:  
  Discover AI tools and workflows that automate HR processes (recruitment, onboarding, employee lifecycle management) and map them into Libraries and Task Managers for standardized HR automation projects.

- Departments / professions:
  - Departments: managers (HR), AI, operations
  - Professions: recruiter, HR manager, HR operations specialist, AI engineer (HR), automation specialist

- Related oa-y courses:
  - `Recruitment-Operations.md` (HR & Recruitment)
  - `Interview-Process.md` (HR & Recruitment)
  - `Employee-Anniversaries.md` (HR & Company Culture)
  - `General-Information.md` (Onboarding for all professions)

## Source_Scope
- Platforms:
  - Primary: YouTube
  - Secondary: vendor docs and case studies linked from video descriptions

- Time window:
  - Primary: last **60 days** of uploads.
  - Expand to 90 days only if HR-specific automation content is sparse; mark clearly when extended.

- Content types:
  - Tutorials, case studies, HR automation walkthroughs (ATS, CRM, onboarding flows, document workflows).
  - Exclude high-level “HR trends” videos without concrete workflows.

## Extraction_Targets
- Tools:
  - ATS, CRM, scheduling tools, document automation tools, HR analytics platforms, and AI agents specifically used for:
    - Sourcing, screening, interview scheduling, offer management, onboarding, performance tracking.

- Objects:
  - HR objects such as: vacancies, candidate pipelines, interview records, contracts, onboarding checklists, performance review documents.

- Actions / Processes / Results:
  - Common HR automation actions: schedule, remind, notify, generate, update, track, archive.
  - Processes like: “automating candidate screening”, “automated onboarding sequences”.

- Responsibilities:
  - Responsibilities for HR roles that combine Actions + Objects (e.g., “automating interview scheduling”, “maintaining candidate pipeline automations”).

- Workflows:
  - End-to-end HR workflows suitable for:
    - Lead-to-hire pipelines.
    - Onboarding projects.
    - Employee lifecycle automations (probation, anniversaries, evaluations).

- Parameters:
  - Configurable thresholds, SLAs, and policy-linked parameters (e.g., reminder frequencies, GDPR-related retention settings).

## Output_Entities
- Libraries_updates:
  - HR-specific tools and objects to create or enrich under:
    - `LIBRARIES/Tools/Business_Tools/`, `Automation_Tools/`, `AI_Tools/`.
    - `LIBRARIES/Objects/Recruitment_Objects.json`, `Objects/Documents.json`.
    - `Responsibilities/responsibilities.json` for HR roles.

- Task_managers_updates:
  - Candidate Project/Task/Step templates for:
    - “Automated candidate screening workflow”.
    - “Automated interview scheduling and follow-up”.
    - “Automated onboarding communications and checklists”.
    - “Anniversary and birthday automation for employees”.

- Research_reports:
  - A report under `TASK_MANAGERS/RESEARCHES/Research Reports/` summarizing:
    - Tools and workflows to adopt.
    - Gaps vs current Recruitment/HR Task Templates.

## Research_Tasks_and_Steps
1. **Discovery**
   - Search YouTube for HR automation tutorials using queries like:
     - “HR automation tutorial”, “AI recruitment workflow”, “automated onboarding with [tool]”, “ATS automation”, “HR chatbot onboarding”.

2. **Filtering**
   - Keep videos that:
     - Show concrete, step-by-step workflows.
     - Are relevant to small HR teams (1–3 people) and remote-first environments.
     - Include realistic HR artifacts (vacancies, candidate records, contracts).

3. **Extraction**
   - For each selected video, extract:
     - Tools used and their roles in the workflow.
     - HR objects manipulated at each step.
     - Key automation rules (e.g., triggers, conditions, schedules).
     - Any compliance / GDPR considerations mentioned.

4. **Mapping to Libraries**
   - Map tools to existing or new entries under Libraries.
   - Map HR objects to `Recruitment_Objects`, `Documents`, and related object libraries.
   - Propose responsibilities where new Action+Object pairs emerge (e.g., “automating reminder emails to candidates”).

5. **Mapping to Task Managers**
   - Propose Task / Step templates representing each major HR automation flow.
   - Identify where these align with or extend:
     - `Recruitment-Operations.md` processes.
     - HR Task templates referenced in `Task_Templates_Checklist-Item-003.md`.

6. **Synthesis**
   - Organize findings by HR process:
     - Sourcing, screening, interviews, offers, onboarding, anniversaries, performance.
   - Prioritize automations that:
     - Reduce repetitive administrative work.
     - Improve response times and candidate / employee experience.

## Response_Format

Return:

1. **Human-readable summary** organized by HR process (sourcing, screening, onboarding, etc.).

2. **Machine-structured section**:

```json
{
  "tools": [ { "...": "..." } ],
  "workflows": [ { "...": "..." } ],
  "responsibilities": [ { "...": "..." } ],
  "parameters": [ { "...": "..." } ],
  "hr_processes": [
    {
      "name": "Candidate Screening",
      "tools": ["..."],
      "objects": ["..."],
      "steps": ["..."],
      "automation_opportunities": ["..."]
    }
  ]
}
```

## Quality_Constraints_and_Filters
- Prefer content from:
  - Recognized HR tech vendors and practitioners.
  - Channels that show real system interfaces (ATS, CRM, HRIS).
- Exclude:
  - Purely conceptual “future of HR” talks without actionable workflows.
  - Content that obviously conflicts with GDPR/basic HR compliance practices.

## Cross_References
- Research prompts:
  - `PROMPTS/Research Prompts/YouTube_HR_Automation_Research_Prompt.md`
  - `PROMPTS/Research Prompts/YouTube_AI_HR_Tutorials_Research_Prompt.md`

- Research reports:
  - `TASK_MANAGERS/RESEARCHES/Research Reports/HR videos research.md`

- Libraries:
  - `LIBRARIES/Objects/Recruitment_Objects.json`
  - `LIBRARIES/Tools/*` for HR/ATS/automation tools.
  - `LIBRARIES/Responsibilities/responsibilities.json` (HR-related entries).

- Task templates / workflows:
  - HR templates in `Task_Templates_Checklist-Item-003.md`.
  - Recruitment workflows derived from `Recruitment-Operations.md` and `Interview-Process.md`.


