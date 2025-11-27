---
category: PROMPTS
subcategory: root
type: prompt
source_id: PMT-051_Department_Research_Integration
title: PMT-051 Department Research Integration
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# PMT-051 Department Research Integration

## Summary
- TODO

## Context
- TODO

## Data / Content
# Prompt: Department-Level Integration for `LIBRARIES/Researches`

**Created:** 2025-11-15  
**Author:** Taxonomy Automation Team  
**Purpose:** Relocate and integrate everything inside `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches\` into the department structure at `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\` so every department owns its research backlogs, findings, and action queues.  
**Status:** Planning & Execution Guide  
**Intended Operator:** AI assistant (Claude, ChatGPT, Cursor) with file-system access

---

## 1. Executive Summary

The centralized `LIBRARIES/Researches` directory (AI_Tutorials, Videos, SMM, Research_ToDo files, master index, templates) must be redistributed into the department folders created on 2025-11-13. Each department will gain a `TASK_MANAGERS/RESEARCHES/` sub-system (sibling to `LIBRARIES/`) containing:

1. **Raw Research Sessions** (JSON) scoped to that department  
2. **Research Queues / To-Do Pipelines** (what to investigate next)  
3. **Cross-links** to department tools, actions, tasks, and video assets  
4. **Metrics dashboards** that roll up into `_SHARED` indices

The goal is to make every department self-sufficient: research discoveries instantly enrich their libraries, feed their TASK_MANAGERS, and remain discoverable through `_SHARED` aggregate indexes.

---

## 2. Current vs Target State

| Aspect | Current (`LIBRARIES/Researches`) | Target (`LIBRARIES/DEPARTMENTS/<DEPT>/researches/`) |
|---|---|---|
| Ownership | Single cross-company location | Per-department ownership + `_SHARED` aggregate |
| Structure | AI_Tutorials/, Videos/, SMM/, ToDo JSONs, indexes, templates | `/researches/index.json`, `/researches/sessions/`, `/researches/queue/`, `/researches/reports/`, `/researches/templates/` stored alongside each department’s `LIBRARIES/` |
| Cross-refs | Manual links to Tools, Processes, Transcribations | Bidirectional references to department `LIBRARIES` (actions/objects/tools), `TASK_MANAGERS`, plus shared rollups |
| Consumption | Requires loading entire Research library | Load only the department you need (AI, VIDEO, SMM, etc.) |

---

## 3. Source Inventory Snapshot

- `AI_Tutorials/` → Weekly session JSON, influencer tracking, new tools logs  
- `Videos/` → Video_XXX.md assets + `VIDEOS_INDEX.md` (tightly coupled with Transcribations)  
- `SMM/` → AI and social content research guides  
- `Research_ToDo_2025-11-W47_*.json` → Backlog queues (AI Platforms, Video Tools, Development Tools, Other Tools)  
- `PROJECT_LOG_2025-11-13.md` → Narrative log of research activities  
- `RESEARCH_INDEX.json`, `RESEARCH_TEMPLATE.json`, `README.md`  
- `AI_Tutorials/Tools_Discovered/New_Tools_2025-11.json`, `Influencer_Database.json`, etc.

---

## 4. Department Mapping (Use this to split the assets)

| Research Segment | Primary Department(s) | Notes |
|---|---|---|
| AI_Tutorials (general) | AI, DEV | Feed AI & DEV libraries and their TASK_MANAGERS |
| AI_Tutorials → Influencer_Tracking | AI, AI, SMM | Influencers belong in AI + go-to-market teams |
| AI_Tutorials → Tools_Discovered | AI, DEV, AI | Tools mapped to `tools.json` per dept |
| Videos (video taxonomy extraction) | VIDEO, AI | Video dept owns production; AI owns taxonomy insights |
| Video transcription reports | VIDEO, AI, SMM | Should mirror `Transcribations` integration |
| SMM research patterns | SMM, AI | Social content research per channel |
| Research_ToDo_AI_Platforms | AI, AI | Platform/infrastructure backlog |
| Research_ToDo_AI_Video_Tools | VIDEO, AI, DESIGN | Visual generation workflows |
| Research_ToDo_Development_Tools | DEV, AI | Coding stack |
| Research_ToDo_Other_Tools | AI, AI, SALES (as needed) | Misc. findings distributed by metadata |

> ❗ **Rule:** If a research item spans multiple departments, duplicate only lightweight references (metadata + pointers), not the entire payload. Store the canonical JSON in the “primary” department and list it inside `TASK_MANAGERS/RESEARCHES/common_index.json`.

---

## 5. Target Folder Blueprint

For every department folder (`LIBRARIES/DEPARTMENTS/<DEPT>/`), create the following (if not already there):

```
LIBRARIES/
├── actions.json
├── ...

researches/
├── README.md
├── index.json              # Dept catalog (mirrors RESEARCH_INDEX fields)
├── sessions/               # Historical research sessions
│   ├── 2025-11-W46_AI_Tutorials.json
│   └── ...
├── queue/                  # Active To-Do pipelines
│   ├── research_queue.json
│   └── backlog/
├── reports/                # Summaries, mapping reports, exports
├── templates/              # Dept-specific research prompt variants
└── integrations/
    ├── tools_crosswalk.json
    ├── tasks_linked.json
    └── status_tracker.json
```

Shared aggregation:

```
TASK_MANAGERS/RESEARCHES/
├── README.md
├── common_index.json           # references every dept index entry
├── routing_matrix.json         # mapping rules for multi-dept findings
└── influencers_global.json     # union of influencer databases
```

---

## 6. Data Transformation Rules

### 6.1 Session Files (`sessions/*.json`)
Reuse the structure from `RESEARCH_TEMPLATE.json`. Apply these adjustments before writing into each department:

- `entity_type` → `"DEPARTMENTS"`
- `department` → uppercase department code (e.g., `"AI"`)
- `library_reference` → relative path (e.g., `"../LIBRARIES/Responsibilities/Actions/Actions_Master.json"`)
- `cross_references.tools` → IDs from that dept’s `tools.json`
- `cross_references.tasks` → IDs from `TASK_MANAGERS/tasks_listing.json`
- `status.processing_stage` → `["queued","in-progress","analysis","integrated"]`

### 6.2 Queue Files (`queue/research_queue.json`)

```json
{
  "department": "VIDEO",
  "last_updated": "2025-11-15",
  "owner": "Research Pods",
  "pipeline": [
    {
      "queue_id": "VID-RSH-2025-W47-01",
      "source": "Research_ToDo_2025-11-W47_AI_Video_Tools.json",
      "topic": "Runway Gen-3 motion systems",
      "priority": "High",
      "status": "queued",
      "linked_tools": ["Runway", "Pika"],
      "linked_tasks": ["TASK-VIDEO-004"],
      "next_action": "Validate transcript availability",
      "due_date": "2025-11-18"
    }
  ]
}
```

### 6.3 Integrations Files

- `tools_crosswalk.json` → map `ai_tools_mentioned` to tool IDs per dept.  
- `tasks_linked.json` → list TASK IDs automatically generated or updated by findings.  
- `status_tracker.json` → aggregate stats (videos processed, tools added, influencers added, etc.) similar to `RESEARCH_INDEX.json`.

### 6.4 README Template

Include: purpose, research sources, how findings sync to libraries, cadence, KPIs. Reference the main README for naming conventions and methodology.

---

## 7. Step-by-Step Execution Plan

### Phase 0 – Preparation
1. Backup `LIBRARIES/Researches/` to `Taxonomy/Archive/Researches_Backup_2025-11-15/`  
2. Snapshot counts (files, JSON entries) for post-migration validation  
3. Confirm department folders exist for all target departments

### Phase 1 – Normalize Source Data
1. Run schema validation on `RESEARCH_TEMPLATE.json` and ensure every session matches it  
2. Tag each existing file with `department_targets` metadata (if missing, infer from filename/query)  
3. Standardize date formats (ISO) and week identifiers

### Phase 2 – Department Segmentation
1. For each file, decide **primary department** using table in Section 4  
2. Add `secondary_departments` array for additional consumers  
3. Store routing decisions inside `TASK_MANAGERS/RESEARCHES/routing_matrix.json`

### Phase 3 – Directory Creation
1. For each department, create the top-level `TASK_MANAGERS/RESEARCHES/` structure (Section 5)  
2. Copy `RESEARCH_TEMPLATE.json` → `templates/research_session_template.json`  
3. Generate dept-specific `README.md` describing scope, cadence, responsibilities

### Phase 4 – Data Migration
1. Move/copy session JSON into `<DEPT>/researches/sessions/` (rename to dept-friendly format)  
2. Split `Research_ToDo_*.json` into queue files per department priority  
3. Move SMM research markdown into `SMM/researches/reports/` (cross-link to AI if needed)  
4. Place Video reports inside both `VIDEO` and `AI` (canonical in VIDEO, reference in AI)  
5. Update references in `PROJECT_LOG_2025-11-13.md` to point to new locations (keep original file under `TASK_MANAGERS/RESEARCHES/reports/`)

### Phase 5 – Cross-References & Automation
1. Update each session’s `cross_references` to use department library paths (`../LIBRARIES/Tools/tools_index.json`, etc.)  
2. Write `tools_crosswalk.json` by matching `ai_tools_mentioned` to tool IDs  
3. Generate `tasks_linked.json` by mapping research outputs to `TASK_MANAGERS/templates/tasks/*.md`  
4. Create automation hooks (e.g., script configs) so future research saves directly to dept folders

### Phase 6 – Shared Index & Validation
1. Build `TASK_MANAGERS/RESEARCHES/common_index.json` by merging all dept `index.json` files  
2. Validate counts vs original snapshot (sessions, reports, influencers, queue items)  
3. Spot-check links (session → tool, session → task)  
4. Update `LIBRARIES/DEPARTMENTS/_VALIDATION_REPORT.md` with new checks specific to researches  
5. Remove or archive the old `LIBRARIES/Researches/` directory after confirmation

---

## 8. Integration with TASK_MANAGERS

1. **New Project Template**: `TASK_MANAGERS/Project_Templates/TEMPLATE-PROJ-RSH-001_Department_Research_Cycle.json`  
2. **Task Templates** (per dept):  
   - `Collect Weekly Research Inputs`  
   - `Prioritize Research Queue`  
   - `Integrate Findings into Libraries`  
   - `Sync Findings with Task Templates`  
3. **Step Templates**: Document how to run Perplexity searches, how to evaluate tools, how to update `tasks_linked.json`.  
4. **Workflows**: Extend existing Research→Transcription pipeline to include department split and status tracker updates.  
5. **Automation Hooks**: When a research session is marked `integrated`, auto-trigger relevant TASK templates or Step Templates.

---

## 9. KPIs & Reporting

- `sessions_processed` per department per week  
- `queue_items_completed` vs `queued`  
- `tools_discovered` (new vs existing)  
- `videos_flagged_for_transcription` and completion percent  
- `tasks_updated_from_research` (count + IDs)  
- `influencers_tracked` (active vs new)  
- `time_to_integrate` (avg hours from discovery to department library update)

Track KPIs inside each `status_tracker.json` and roll them up to `TASK_MANAGERS/RESEARCHES/common_index.json`.

---

## 10. Validation Checklist

- [ ] All department folders contain `/researches/` structure  
- [ ] `index.json` exists and matches template (includes counts, last_updated, maintainers)  
- [ ] No JSON schema violations (validate against template)  
- [ ] Queue files align with TASK priorities  
- [ ] Cross-reference IDs resolve to actual `tools.json`, `actions.json`, `TASK_MANAGERS` entries  
- [ ] `TASK_MANAGERS/RESEARCHES/common_index.json` total counts equal original library totals  
- [ ] `README.md` docs updated (department + shared)  
- [ ] Old `LIBRARIES/Researches/` content archived, not duplicated

---

## 11. Suggested Timeline

| Day | Focus |
|---|---|
| Day 1 | Backup + normalization + routing decisions |
| Day 2 | Build dept folder structures + migrate AI + VIDEO assets |
| Day 3 | Migrate SMM, AI, DEV research + create queues |
| Day 4 | Generate integrations files + TASK_MANAGERS hooks |
| Day 5 | Assemble shared index + validation + documentation cleanup |

---

## 12. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Loss of canonical session context | Medium | Archive original directory before move; track hashes |
| Broken cross-references | High | Automated validator to check every `tools_crosswalk` and `tasks_linked` entry |
| Duplicate processing between departments | Medium | Use `TASK_MANAGERS/RESEARCHES/routing_matrix.json` to ensure single source |
| Queue desynchronization | Medium | Enforce single writer per queue via status tracker |

---

## 13. Next Steps After Migration

1. Automate weekly script to drop new sessions straight into the right department folder  
2. Teach department leads to review `queue/research_queue.json` during weekly planning  
3. Extend `validate_departments.py` to include research integrity checks  
4. Keep `TASK_MANAGERS/RESEARCHES/common_index.json` updated for executive dashboards  
5. Align with `LIBRARIES/Taxonomy_Processing` roadmap (research → transcription → integration pipeline)

---

## Appendix A – Sample `index.json` (Per Department)

```json
{
  "department": "AI",
  "version": "1.0",
  "created": "2025-11-15",
  "last_updated": "2025-11-15",
  "total_sessions": 5,
  "aggregate_metrics": {
    "videos_discovered": 32,
    "videos_transcribed": 9,
    "tools_discovered": 6,
    "tools_added": 2,
    "influencers_tracked": 8,
    "queue_items_open": 4
  },
  "tracking_databases": {
    "sessions_path": "./sessions/",
    "queue_path": "./queue/research_queue.json",
    "reports_path": "./reports/",
    "templates_path": "./templates/"
  },
  "maintainers": ["AI Research Pod"],
  "related_resources": {
    "actions": "../LIBRARIES/Responsibilities/Actions/Actions_Master.json",
    "objects": "../LIBRARIES/Responsibilities/Objects/object_types.json",
    "tools": "../LIBRARIES/Tools/tools_index.json",
    "skills": "../LIBRARIES/skills.json",
    "tasks_listing": "../TASK_MANAGERS/tasks_listing.json"
  }
}
```

---

**End of Prompt**




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
