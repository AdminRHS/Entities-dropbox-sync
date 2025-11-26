# 5. FILE OPERATIONS & DATA MANAGEMENT

**Version:** 6.2 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## MASTER DATA LOCATIONS

**TASK_MANAGERS (Templates):**
```
ENTITIES/TASK_MANAGERS/
├── TSM-001_Project_Templates/Project_Templates_Master_List.csv    # PRT-###
├── TSM-002_Milestone_Templates/Milestones_Master_List.csv         # MLT-###
├── TSM-003_Task_Templates/Task_Templates_Master_List.csv          # TST-###
├── TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv # STT-###
└── TSM-007_GUIDES/GUIDES_Master_List.csv                          # GDS-###
```

**LIBRARIES (Tools):**
```
ENTITIES/LIBRARIES/LBS_003_Tools/                                  # TOL-###
```

**PROMPTS:**
```
ENTITIES/PROMPTS/DATA_FIELDS/PMT_Master_List.csv                   # PMT-###
```

---

## DAILY DEPARTMENT REPORTS (November 2025)

**Current Month Locations:**
```
C:\Users\Dell\Dropbox\Nov25\           # November department dailies
C:\Users\Dell\Dropbox\Finance 2025\    # Finance department data
```

**Daily Workflow:**

1. **Read employee submissions** from Nov25/ or Finance 2025/ folders
2. **Extract entities**: TST-### (tasks), STT-### (steps), MLT-### (milestones), PRT-### (projects)
3. **Link references**: TOL-### (tools), GDS-### (guides)
4. **Validate against master CSVs** in TSM-00X_[Category]/
5. **Generate department reports** with progress tracking

**Entity Extraction Pattern:**

- Use [GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010) for daily workflow structure
- Use [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011) for classification decisions
- Task-first approach: Extract TST-### → Group into MLT-### → Link to PRT-###

---

## FILE NAMING

| Type | Pattern | Example |
|------|---------|---------|
| Templates | XXX-###_Name.ext | TST-042_Setup_OAuth.json |
| Reports | YYYY-MM-DD_{Dept}.md | 2025-11-25_Finance.md |
| Prompts | PMT-###_Name.md | PMT-033_AID_Daily_Report.md |
