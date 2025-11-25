# `TASK_MANAGERS/RESEARCHES/` Overview

**Purpose:** Central home for all migrated research assets (AI tutorials, influencer tracking, SMM reports, video studies, and research ToDo queues). Everything that used to live in `LIBRARIES/Researches/` now lives here so research sits closer to task managers and operational workflows.

---

## Folder Layout

```none
TASK_MANAGERS/RESEARCHES/
├── README.md                                # this file
├── README_Library.md                        # AI Tutorial Research playbook (full guide)
├── RESEARCH_INDEX.json                      # master catalog of research sessions
├── RESEARCH_TEMPLATE.json                   # JSON template for new sessions
├── EXAMPLE_*.json                           # sample completed sessions
├── Videos/                                  # video research + transcriptions (Video_001-013, reports, queue)
├── SMM/                                     # social media marketing research sessions and analyses
├── Influencer_Tracking/                     # influencer databases and channel trackers
├── ToDo/                                    # queued research work (AI Platforms, Video Tools, Dev Tools, Other Tools)
├── Transcribations/                         # (optional) legacy pointer kept in README_Library
├── common_index.json                        # shared metrics roll-up
├── routing_matrix.json                      # cross-team dependency tracker
├── oa-y_Research_Data_Flow_Notes.md         # mapping between oa-y, Libraries, Task Managers, and research assets
├── oa-y_Libraries_TaskManagers_Gap_Analysis.md   # oa-y-driven gap analysis and recommendations
├── Research_Prompt_Schema.md                # unified schema for research prompts
├── Research_Report_Schema.md                # unified schema for research reports
└── Research_Prompts_Schema_Aligned/         # schema-aligned v2 research prompts (per topic/department)
```

Each subfolder mirrors the structure that existed under `LIBRARIES/Researches/` so paths in historical documentation still make sense.

---

## Operating Principles

1. **Canonical Storage**  
   - Treat `TASK_MANAGERS/RESEARCHES/` as the master source for all research artefacts.  
   - `common_index.json` aggregates metrics across everything stored here.

2. **Link Back to Libraries**  
   - Research files still reference department libraries via relative paths such as `../../LIBRARIES/tools.json` or `../tasks_listing.json`.  
   - Scripts that previously wrote to `LIBRARIES/Researches/` should now target these folders directly.

3. **Consistency**  
   - Keep README + template files up to date so future migrations remain predictable.  
   - Use the JSON templates when logging new sessions or ToDo queues.

4. **Cross-Team Awareness**  
   - Use `routing_matrix.json` to flag when a finding in one area (e.g., AI tutorials) triggers work in another (e.g., Video, SMM).  
   - Update `common_index.json` when new sessions or ToDo items are added.
5. **Schema Alignment (oa-y / Libraries / Task Managers)**  
   - Use `Research_Prompt_Schema.md` when designing new research prompts so they clearly specify topic context, source scope, extraction targets, and output entities.  
   - Use `Research_Report_Schema.md` for new reports in `Research Reports/` so they can be consumed by Libraries and Task Managers.  
   - Prefer creating new prompt versions under `Research_Prompts_Schema_Aligned/` when upgrading existing prompts to the unified schema.

---

## Next Actions

1. Ensure all scripts/prompts reference `TASK_MANAGERS/RESEARCHES/` instead of the retired `LIBRARIES/Researches/` or `LIBRARIES/DEPARTMENTS/RESEARCHES/` paths.  
2. Populate `common_index.json` and `routing_matrix.json` as research resumes so reporting stays accurate.  
3. Keep the ToDo queue current—new backlog items should be saved in `ToDo/` using the provided template.  
4. Continue storing new video findings under `Videos/`, SMM research under `SMM/`, and influencer data under `Influencer_Tracking/`.

For questions, contact the Taxonomy Automation Team or check `MIGRATED_TO_DEPARTMENTS.md` for rollback details.
