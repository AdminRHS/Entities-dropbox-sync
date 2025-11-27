# Daily_Processing Folder

**Purpose:** Complete workflow and support files for daily employee file processing

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active - Production Ready

---

## Folder Structure

```
Daily_Processing/
├── Guides/
│   └── GDS-001_Daily_Task_Processing_Instructions.md
├── Support_Files/
│   ├── Task_Assignment_Rules.json
│   ├── Daily_Processing_Master.csv
│   └── Processing_Metrics.csv
└── README.md (this file)
```

---

## Contents

### Guides/

**[GDS-001: Daily Task Processing Instructions](Guides/GDS-001_Daily_Task_Processing_Instructions.md)**

Complete step-by-step workflow for processing all employees' daily files.

**Workflow:** 9 Milestones (MLT-001 through MLT-009)
1. MLT-001: Setup (10 min)
2. MLT-002: Collection - ALL files (30 min)
3. MLT-003: Entity Extraction - from ALL files (60 min)
4. MLT-004: Gap Analysis - using RESEARCHES methodology (45 min)
5. MLT-005: Template Creation - based on gaps (30 min)
6. MLT-006: Task Assignment Planning (45 min)
7. MLT-007: Task Distribution (30 min)
8. MLT-008: Quality Assurance (20 min)
9. MLT-009: Archival & Reporting (10 min)

**Total Time:** 3-4 hours initially, 1-2 hours with automation

---

### Support_Files/

**Task_Assignment_Rules.json**
- Assignment algorithm configuration
- Scoring weights: Profession (40%), Department (20%), Skill (20%), Workload (20%)
- Override rules and profession mappings

**Daily_Processing_Master.csv**
- Historical tracking of daily processing runs
- Columns: Processing_Date, For_Date, Status, Files_Collected, Tasks_Extracted, Employees_Assigned, New_Templates_Created, Duration, Processor, Notes

**Processing_Metrics.csv**
- Performance metrics tracking
- Columns: Date, Files_Collected, Tasks_Extracted, New_Templates, Employees_Assigned, Avg_Tasks_Per_Employee, Max_Tasks_Single_Employee, Workload_Variance_Percent, Processing_Time, QA_Status, Processed_By, Gap_Analysis counts

---

## Key Concepts

### Milestone-Based Workflow

The daily processing follows a 9-milestone workflow (MLT-001 through MLT-009) aligned with the system's standard Milestone Template (MLT-###) taxonomy defined in MAIN_PROMPT_v7.md.

### Gap Analysis Methodology

Following RESEARCHES methodology to identify:
- **EXISTS:** Already in TASK_MANAGERS → Use existing
- **LIBRARY_ONLY:** In LIBRARIES but no template → Create template
- **NEW:** Missing from both → Create library entries + template

### Multi-Factor Assignment Algorithm

Tasks assigned using 100-point scoring system:
- Profession Match: 40 points
- Department Match: 20 points
- Skill Level Match: 20 points
- Workload Balance: 20 points

---

## Workspace Location

**Daily processing workspace:**
```
/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/Niko Nov25/Tasks/Daily_Processing/
```

**Structure:**
```
Daily_Processing/
├── YYYY-MM-DD_Collection/
│   ├── 01_Collected_Files/       # ALL employee files
│   ├── 02_Extracted_Tasks/       # Extracted entities
│   ├── 03_Gap_Analysis/          # Gap analysis reports
│   ├── 04_Task_Templates/        # New TST-### templates
│   ├── 05_Distribution_Plan/     # Assignment decisions
│   └── 06_Processing_Log.md      # Daily log
└── Archive/                       # Previous processing runs
```

---

## Getting Started

### Prerequisites

1. Read [GDS-001](Guides/GDS-001_Daily_Task_Processing_Instructions.md) completely
2. Review [Task_Assignment_Rules.json](Support_Files/Task_Assignment_Rules.json)
3. Load employee profiles from `/ENTITIES/TALENTS/Employees/profiles/Work/`
4. Review gap analysis examples in `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`

### First Run

1. Create workspace: `Nov25/Niko Nov25/Tasks/Daily_Processing/2025-MM-DD_Collection/`
2. Follow all 9 milestones in sequence
3. Start with 5-10 employee pilot before full rollout
4. Refine based on feedback

### Daily Routine

1. **Morning:** Create today's workspace folder
2. **Process:** Follow 9-milestone workflow
3. **Complete:** Archive workspace, generate summary report
4. **Track:** Update Processing_Metrics.csv

---

## Success Metrics

### Daily
- Processing time: <3 hours (target: <2h with automation)
- Files collected: ~60 (ALL files from each employee)
- Tasks extracted: 50-100
- New templates: 2-5 TST-###
- Distribution accuracy: >95%

### Weekly
- Tasks processed: 250-500
- Template growth: 10-25 TST-###
- Workload variance: <20%
- Processing consistency: 5 days/week

### Monthly
- Templates created: 40-100 TST-###
- Processing time trend: Decreasing
- Assignment accuracy: >90%

---

## Automation Opportunities

### Immediate Python Scripts (saves 2 hours/day)
1. `collect_daily_files.py` - Auto-scan and collect (saves 20 min)
2. `extract_tasks_batch.py` - Batch MAIN_PROMPT_v7 processing (saves 30 min)
3. `assign_tasks.py` - Apply assignment algorithm (saves 30 min)
4. `distribute_tasks.py` - Create tasks.md files (saves 20 min)
5. `generate_report.py` - Auto-generate reports (saves 10 min)

### Future Full Automation
- Claude API integration for entity extraction
- n8n/Make workflow triggered at 11 PM daily
- Complete overnight processing
- Morning dashboard with results
- **Potential:** Fully automated, 0 manual time required

---

## Critical Files Reference

### For Entity Extraction
- **MAIN_PROMPT_v7.md:** `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v7.md`

### For Gap Analysis
- **Gap Analysis Examples:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`
- **Task Templates Master:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`
- **LIBRARIES:** `/ENTITIES/LIBRARIES/` (Tools, Actions, Objects, Skills)

### For Employee Data
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`

---

## Integration with Other Workflows

### Video Processing (GDS-002)
When daily processing identifies video-related tasks, route to RESEARCHES workflow (Milestones MLT-010 through MLT-015).

### Task Management
New templates created (TST-###) are immediately available for future daily processing and task assignments across the organization.

---

## Version History

**Version 1.0** (2025-11-25)
- Initial release
- 9-milestone workflow (MLT-001 through MLT-009)
- Gap analysis methodology integrated
- Multi-factor assignment algorithm
- Support files and workspace structure

---

**Document Maintained By:** AI & Automation Team
**Last Updated:** 2025-11-25
**Status:** Active - Production Ready
**Next Review:** 2025-12-25 (1 month)
**Related Guides:** GDS-002 (Video Transcript Processing)
