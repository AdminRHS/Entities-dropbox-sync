# MAIN_PROMPT_v7

**Version:** 7.0
**Date:** 2025-11-26
**Status:** Production Ready

---

## What's New in v7

**Consolidated from 8 files to 5 files:**
- ✅ **62% less repetition** - Removed duplicate content
- ✅ **Running projects tracking** - New file 4 for active PRT-001 to PRT-009
- ✅ **Current month paths** - Nov25/, Finance 2025/ explicitly referenced
- ✅ **Streamlined workflow** - Combined identity + execution into file 1

---

## File Structure

```
MAIN_PROMPT_v7/
├── 01_Core_Workflow.md          # Role, workflow, examples (was files 1+3)
├── 02_Entity_Reference.md       # ID formats, taxonomy, decision tree (file 2)
├── 03_Department_Operations.md  # 10 depts + cross-dept projects (file 4)
├── 04_Running_Projects.md       # Active PRT tracking + progress (NEW!)
├── 05_Quick_Reference.md        # Paths, prompts, validation (was files 5+6+7)
└── README.md                    # This file
```

---

## Quick Start

**For daily task extraction:**

1. **Read file 1** (Core Workflow) - Understand your role and workflow
2. **Use file 2** (Entity Reference) - When classifying tasks/steps/milestones
3. **Check file 4** (Running Projects) - Map tasks to existing PRT-001 to PRT-009
4. **Reference file 5** (Quick Reference) - For paths, prompts, validation

**File 3** (Department Operations) - Use when working cross-department or research projects

---

## Key Changes from v6

| Aspect | v6 (8 files) | v7 (5 files) | Improvement |
|--------|--------------|--------------|-------------|
| **Files** | 8 | 5 | 38% reduction |
| **Repetition** | High (taxonomy repeated 3x) | Low (once per concept) | ~60% less duplicate content |
| **Project Context** | Scattered | Dedicated file 4 | Clearer tracking |
| **Current Paths** | Generic | Nov25/, Finance 2025/ | Ready to use |
| **Workflow** | Split across 2 files | Combined in file 1 | Faster onboarding |

---

## Daily Workflow (Quick)

```
1. Read employee submissions (Nov25/ or Finance 2025/)
2. Extract TST-### (tasks) - task-first approach
3. Check PRT-001 to PRT-009 (file 4) - map to existing project
4. Use GDS-011 for classification decisions
5. Link to TOL-### (tools) and GDS-### (guides)
6. Generate dept report (PMT-033 to PMT-043)
```

---

## Migration from v6

**What stayed the same:**
- Entity IDs (PRT, MLT, TST, STT, TOL, GDS, PMT)
- Master CSV locations (TSM-00X_[Category]/)
- Reusable templates (many-to-many)
- Task-first, bottom-up classification

**What changed:**
- 8 files → 5 files (consolidated)
- Added file 4 (Running Projects)
- Combined files 1+3 → new file 1
- Combined files 5+6+7 → new file 5
- Removed external modules (file 8) - replaced with this README

**No breaking changes** - All entity references, IDs, and workflows remain compatible.

---

## Support Files

**Guides (Classification Help):**
- [GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010) - Daily workflow
- [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011) - Decision tree
- [GDS-012](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012) - Cross-references

**Master CSVs:**
- PRT: `ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/Project_Templates_Master_List.csv`
- MLT: `ENTITIES/TASK_MANAGERS/TSM-002_Milestone_Templates/Milestones_Master_List.csv`
- TST: `ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`
- STT: `ENTITIES/TASK_MANAGERS/TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv`
- GDS: `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GUIDES_Master_List.csv`

---

## Next Steps

1. **Test with November reports** - Use with Nov25/ and Finance 2025/ data
2. **Update active projects** - Populate file 4 with actual PRT-001 to PRT-009 details
3. **Enhance guides** - Add more examples to GDS-010, GDS-011, GDS-012
4. **Gather feedback** - What works, what's still unclear
5. **Plan v8** - Further optimizations based on usage

---

**Last Updated:** 2025-11-26
**Status:** ✅ Production Ready
**Previous Version:** [MAIN_PROMPT_v6](../MAIN_PROMPT_v6/)
