# Daily Processing Workspace

This folder contains daily task processing workspaces for employees.

## Structure

```
Daily_Processing/
├── YYYY-MM-DD_Collection/          # Daily workspace folders
│   ├── 01_Collected_Files/         # All employee files (daily.md, plans.md, etc.)
│   ├── 02_Extracted_Tasks/         # Extracted entities
│   ├── 03_Gap_Analysis/            # Gap analysis reports
│   ├── 04_Task_Templates/          # New TST-### templates
│   ├── 05_Distribution_Plan/       # Assignment decisions
│   └── 06_Processing_Log.md        # Daily processing log
├── Archive/                         # Previous processing runs
└── README.md                        # This file
```

## Usage

### Daily Processing

1. Create today's collection folder: `YYYY-MM-DD_Collection/`
2. Follow the workflow in GDS-001: Daily Task Processing Instructions
3. After completion, move folder to `Archive/`

### Example

Processing date: 2025-11-25

```
Daily_Processing/
├── 2025-11-25_Collection/          # Today's processing
│   ├── 01_Collected_Files/
│   │   ├── AI_Artemchuk_Nikolay/
│   │   │   ├── daily.md
│   │   │   └── plans.md
│   │   ├── Design_Shelep_Olha/
│   │   │   ├── daily.md
│   │   │   ├── plans.md
│   │   │   └── tasks.md
│   │   └── [... 60 employee folders]
│   ├── 02_Extracted_Tasks/
│   │   ├── AI_Artemchuk_Nikolay_extracted.md
│   │   ├── Design_Shelep_Olha_extracted.md
│   │   └── [... 60 extracted files]
│   ├── 03_Gap_Analysis/
│   │   └── Gap_Analysis_2025-11-25.md
│   ├── 04_Task_Templates/
│   │   ├── TST-125_Process_Daily_Files_AI.json
│   │   └── [... new templates]
│   ├── 05_Distribution_Plan/
│   │   └── assignment_plan_2025-11-25.md
│   └── 06_Processing_Log.md
└── Archive/
    ├── 2025-11-24_Collection/      # Previous day
    └── 2025-11-23_Collection/      # Day before
```

## Files Reference

**Guide:** `/ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-001_Daily_Task_Processing_Instructions.md`

**Support Files:**
- `/ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Task_Assignment_Rules.json`
- `/ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Daily_Processing_Master.csv`
- `/ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Daily_Processing/Processing_Metrics.csv`

## Workflow Summary

1. **Phase 0:** Setup (10 min) - Create workspace folders
2. **Phase 1:** Collection (30 min) - Collect ALL files from ~60 employees
3. **Phase 2:** Extraction (60 min) - Extract entities from all files
4. **Phase 3:** Gap Analysis (45 min) - Identify gaps using RESEARCHES methodology
5. **Phase 4:** Template Creation (30 min) - Create new TST-### templates
6. **Phase 5:** Assignment (45 min) - Assign tasks using algorithm
7. **Phase 6:** Distribution (30 min) - Create tasks.md for tomorrow
8. **Phase 7:** QA (20 min) - Quality checks
9. **Phase 8:** Reporting (10 min) - Generate summary and archive

**Total Time:** 3-4 hours initially, 1-2 hours with automation

## Notes

- Process daily (Monday-Friday)
- Collect ALL files, not just daily.md
- Use Gap Analysis methodology (EXISTS/LIBRARY_ONLY/NEW)
- Archive completed runs to Archive/ folder
- Track metrics in Processing_Metrics.csv

---

**Last Updated:** 2025-11-25
**Maintained By:** Daily Processing Team
