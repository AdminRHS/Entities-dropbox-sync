# 8. EXTENSIONS & V7 ROADMAP

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## CURRENT SYSTEM (v6)

**What Works:**
- Task-first extraction (TST-### → MLT-### → PRT-###)
- Reusable templates (many-to-many relationships)
- Simplified libraries (TOL-### tools, GDS-### guides)
- Cross-department research tracking
- 10 departments with daily reports (PMT-033 to PMT-043)

**Current Locations:**
- Department dailies: `Nov25/`, `Finance 2025/`
- Master data: `ENTITIES/TASK_MANAGERS/TSM-00X_[Category]/`
- Guides: [GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010), [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011), [GDS-012](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012)

---

## ROADMAP TO V7

**Key Improvements Needed:**

1. **Reduce Repetition** - Consolidate overlapping content across 8 files
2. **Project Context** - Better tracking of active/running projects (PRT-001 to PRT-009+)
3. **Streamlined Workflow** - Single-file daily operations guide
4. **Real-time Updates** - Link to actual current month folders (dynamic paths)
5. **Clearer Guides** - Enhanced GDS-### with more examples

**V7 Structure (Proposed):**

```
MAIN_PROMPT_v7/
├── 01_Core_Workflow.md          # Combines identity + workflow execution
├── 02_Entity_Reference.md       # Simplified taxonomy + examples
├── 03_Department_Operations.md  # Dept codes + cross-dept projects
├── 04_Running_Projects.md       # Active PRT tracking + examples (NEW)
├── 05_Quick_Reference.md        # File paths + prompts + validation
```

**Migration Plan:**
- Consolidate 8 files → 5 files
- Remove ~60% duplicate content
- Add active project tracking
- Focus on operational value over theory
