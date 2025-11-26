# MLT-001: Setup

**Milestone ID:** MLT-001
**Milestone Name:** Setup
**Duration:** 10 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 1 of 9

---

## Overview

Create today's workspace folder with the required structure for processing all employee daily files. This milestone sets up the organized environment needed for the subsequent 8 milestones.

---

## What You'll Do

### 1. Create Today's Workspace Folder

**Location:**
```
/ENTITIES/DAILIES/Daily_Processing/YYYY-MM-DD_Collection/
```

**Example:** `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/`

---

### 2. Create Required Subfolders

Within the workspace folder, create these 6 subfolders:

```
2025-11-25_Collection/
├── 01_Collected_Files/
├── 02_Extracted_Tasks/
├── 03_Gap_Analysis/
├── 04_Task_Templates/
├── 05_Distribution_Plan/
└── 06_Processing_Log.md
```

**Subfolder Purpose:**

| Folder | Milestone | Purpose |
|--------|-----------|---------|
| `01_Collected_Files/` | MLT-002 | Store ALL copied employee .md files |
| `02_Extracted_Tasks/` | MLT-003 | Save entity extraction results per employee |
| `03_Gap_Analysis/` | MLT-004 | Store gap analysis reports (EXISTS/LIBRARY_ONLY/NEW) |
| `04_Task_Templates/` | MLT-005 | Save newly created TST-### templates |
| `05_Distribution_Plan/` | MLT-006 | Store task assignment planning documents |
| `06_Processing_Log.md` | MLT-009 | Log daily processing activities and metrics |

---

### 3. Initialize Processing Log

Create `06_Processing_Log.md` with this structure:

```markdown
# Daily Processing Log - 2025-11-25

**Processing Date:** 2025-11-25
**For Date (Distribution):** 2025-11-26
**Processor:** [Your Name]
**Start Time:** [HH:MM]

---

## Milestones Progress

- [ ] MLT-001: Setup (10 min)
- [ ] MLT-002: Collection (30 min)
- [ ] MLT-003: Entity Extraction (60 min)
- [ ] MLT-004: Gap Analysis (45 min)
- [ ] MLT-005: Template Creation (30 min)
- [ ] MLT-006: Task Assignment Planning (45 min)
- [ ] MLT-007: Task Distribution (30 min)
- [ ] MLT-008: Quality Assurance (20 min)
- [ ] MLT-009: Archival & Reporting (10 min)

---

## Notes

[Add processing notes, issues encountered, decisions made]

---

## Metrics Summary

| Metric | Count |
|--------|-------|
| Files Collected | 0 |
| Tasks Extracted | 0 |
| Employees Assigned | 0 |
| New Templates Created | 0 |
| Processing Duration | - |
| Status | In Progress |
```

---

## ISO Code References

### Entity Types Used
- **MLT** - Milestone Template (from TASK_MANAGERS taxonomy)
- **TST** - Task Template (from TASK_MANAGERS taxonomy)
- **GDS** - Guide (from TASK_MANAGERS taxonomy)

### Department Codes
Department codes you'll encounter in employee profiles:

| ISO Code | Department Name | Full Name |
|----------|-----------------|-----------|
| **AID** | AI_Tasks | AI & Automation |
| **DEV** | DEV_Tasks | Development |
| **HRM** | HR_Tasks | Human Resources |
| **LGN** | LG_Tasks | Lead Generation |
| **DGN** | Design_Tasks | Design |
| **VID** | Video_Tasks | Video Production |
| **SLS** | Sales_Tasks | Sales |

**Reference:** [TAX-002 ISO Code Registry](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md)

---

## Taxonomy Context

This milestone is part of the structured Daily Processing workflow documented in the TASK_MANAGERS taxonomy system.

**Hierarchical Position:**
```
TSM-007 (Guides Meta-Category)
└── GDS-001 (Daily Task Processing Instructions)
    └── MLT-001 (Setup - this milestone)
        └── Creates workspace for MLT-002 through MLT-009
```

**Related Taxonomy Files:**
- [Taxonomy Master List](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv)
- [ISO Code Registry](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md)
- [Hierarchy Tree](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_Hierarchy_Tree.md)

---

## Checklist

- [ ] Create workspace folder with today's date: `/ENTITIES/DAILIES/Daily_Processing/YYYY-MM-DD_Collection/`
- [ ] Create subfolder: `01_Collected_Files/`
- [ ] Create subfolder: `02_Extracted_Tasks/`
- [ ] Create subfolder: `03_Gap_Analysis/`
- [ ] Create subfolder: `04_Task_Templates/`
- [ ] Create subfolder: `05_Distribution_Plan/`
- [ ] Create file: `06_Processing_Log.md` with template structure
- [ ] Verify all folders are accessible
- [ ] Set start time in processing log

---

## Expected Outcomes

✅ **Workspace Structure Created**
- Date-stamped collection folder exists
- All 5 subfolders created and empty
- Processing log initialized with template

✅ **Ready for MLT-002**
- `01_Collected_Files/` ready to receive employee files
- Processing log tracking enabled

---

## Next Milestone

**→ [MLT-002: Collection](MLT-002_Collection.md)** - Copy ALL files from every employee's today folder (~60 employees, 30 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Simple Workflow:** [Daily_Processing_Workflow_Simple.md](Daily_Processing_Workflow_Simple.md)
- **Milestone Registry:** [MILESTONE_REGISTRY.md](../../../TASK_MANAGERS/TSM-007_GUIDES/MILESTONE_REGISTRY.md)
- **Workspace README:** [Daily_Processing README](../../Daily_Processing/README.md)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
