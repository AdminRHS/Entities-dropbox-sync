# 5. QUICK REFERENCE

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## CURRENT MONTH DATA (November 2025)

**Department Dailies:**
```
C:\Users\Dell\Dropbox\Nov25\           # November department reports
C:\Users\Dell\Dropbox\Finance 2025\    # Finance department data
```

**Master Data:**
```
ENTITIES/TASK_MANAGERS/
├── TSM-001_Project_Templates/Project_Templates_Master_List.csv    # PRT-###
├── TSM-002_Milestone_Templates/Milestones_Master_List.csv         # MLT-###
├── TSM-003_Task_Templates/Task_Templates_Master_List.csv          # TST-###
├── TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv # STT-###
└── TSM-007_GUIDES/GUIDES_Master_List.csv                          # GDS-###

ENTITIES/LIBRARIES/LBS_003_Tools/                                  # TOL-###
ENTITIES/PROMPTS/DATA_FIELDS/PMT_Master_List.csv                   # PMT-###
```

---

## KEY PROMPTS

**Daily Reports (by Department):**
- PMT-033 (AID), PMT-035 (DGN), PMT-036 (DEV), PMT-037 (FIN)
- PMT-038 (HRM), PMT-039 (LGN), PMT-040 (MKT), PMT-041 (SLS)
- PMT-042 (SMM), PMT-043 (VID)
- PMT-032 (Collection/Aggregation)

**Research (Cross-Department):**
- PMT-004 to PMT-013 (Video - VID leads)
- PMT-044, PMT-051 (Web/Sales - SLS, LGN)
- PMT-045 (Documents - SMM, HRM, SLS)
- PMT-046 to PMT-052 (Platforms - DEV, AID)

**Task Management:**
- PMT-061 (Project/milestone setup)
- PMT-062 (Tool & guide matching)

**System:**
- PMT-029 (System health)
- PMT-072 (Critical fixes)

---

## GUIDES (Classification Help)

- **[GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010)** - Daily workflow structure
- **[GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)** - PRT/MLT/TST/STT decision tree
- **[GDS-012](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012)** - Template cross-references

---

## VALIDATION CHECKLIST

**Before creating entity:**

- [ ] **ID Format:** XXX-### (TST-042, not TSK-42)
- [ ] **Sequential:** Check master CSV, use highest+1
- [ ] **No duplicates:** ID doesn't exist
- [ ] **Valid references:** All PRT/MLT/TST/STT/TOL/GDS exist
- [ ] **Metadata complete:** Name, Description, Department

**Common Errors:**

| Error | Fix |
|-------|-----|
| Duplicate ID | Use next available (max+1) |
| Wrong format (TSK) | Use TST for tasks, STT for steps |
| Missing reference | Link to TOL-### or GDS-### |

---

## QUICK WORKFLOW

**Daily Processing:**
1. Read: `Nov25/` or `Finance 2025/` employee submissions
2. Extract: TST-### (tasks), STT-### (steps)
3. Classify: Check PRT-001 to PRT-009, use [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)
4. Link: TOL-### (tools), GDS-### (guides)
5. Validate: Against master CSVs in TSM-00X_[Category]/
6. Generate: Department report (PMT-033 to PMT-043)
7. Archive: `ENTITIES/REPORTS/{Dept}/{Date}`

**Entity Extraction Pattern:**
- Task-first approach: Extract TST-### → Group into MLT-### → Link to PRT-###
- Bottom-up classification: Never top-down
- Reusable templates: Same template in multiple parents

---

## FILE NAMING

| Type | Pattern | Example |
|------|---------|---------|
| Templates | XXX-###_Name.ext | TST-042_Setup_OAuth.json |
| Reports | YYYY-MM-DD_{Dept}.md | 2025-11-25_Finance.md |
| Prompts | PMT-###_Name.md | PMT-033_AID_Daily.md |
