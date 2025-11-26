# TSM-007_GUIDES: Processing & Workflow Guides

**Purpose:** Step-by-step instruction guides for employee task processing workflows

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active - Production Ready

---

## Available Guides

### GDS-001: Daily Task Processing Instructions

**File:** `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md`

**Note:** Daily Processing workflow files have been moved to ENTITIES/DAILIES for better organization.

**Purpose:** Process all employees' daily files, extract tasks, perform gap analysis, create templates, and distribute work assignments.

**Target Users:** 1-2 assigned employees (any profession)

**Frequency:** Daily (Monday-Friday)

**Time Required:** 3-4 hours initially, 1-2 hours with automation

**Key Features:**
- Collect ALL files from employee folders (daily.md, plans.md, tasks.md, etc.)
- Extract entities using MAIN_PROMPT_v6.md
- Perform gap analysis using RESEARCHES methodology
- Create new TST-### templates for identified gaps
- Assign tasks using multi-factor algorithm (profession 40%, department 20%, skills 20%, workload 20%)
- Distribute tasks to employee folders for tomorrow

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

**Supporting Files:**
- `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files/Task_Assignment_Rules.json` - Assignment algorithm rules
- `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files/Daily_Processing_Master.csv` - Processing history
- `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files/Processing_Metrics.csv` - Performance metrics

---

### GDS-002: Video Transcript Processing Instructions

**File:** [GDS-002_Video_Transcript_Processing_Instructions.md](GDS-002_Video_Transcript_Processing_Instructions.md)

**Purpose:** Process video transcripts through the complete RESEARCHES 7-phase workflow, from video search to library integration.

**Target Users:** Video processing team (AI, Video departments)

**Frequency:** Ongoing (3-5 videos per week)

**Time Required:** 50-100 minutes per video (90-95% time savings vs pre-v3.2)

**Key Features:**
- 7-phase systematic workflow
- PMT-004 v3.2 transcription with 14 taxonomy sections
- Gap analysis following RESEARCHES methodology
- Entity creation (tools, tasks, skills) with JSON files
- Library integration and mapping
- Automation scripts available

**Workflow:** 6 Milestones (MLT-010 through MLT-015)
1. MLT-010: Search Queue - Assign video searches (2-3h/week)
2. MLT-011: Video Queue - Prioritize videos (30min/week)
3. MLT-012: Transcriptions - PMT-004 processing (40-60min/video)
4. MLT-013: Analysis & Gap Analysis - Identify library gaps (20-30min/video)
5. MLT-014: Integration - Create JSON entities (10-20min/video)
6. MLT-015: Library Mapping - Final documentation (10min/video)

**Integration:** Routes video-related tasks from Daily Processing (GDS-001)

---

## Folder Structure

```
TSM-007_GUIDES/
├── GDS-002_Video_Transcript_Processing_Instructions.md
├── MILESTONE_REGISTRY.md
└── README.md (this file)
```

**Note:** GDS-001 Daily Processing workflow files have been moved to:
```
/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/
├── Guides/
│   └── GDS-001_Daily_Task_Processing_Instructions.md
├── Support_Files/
│   ├── Task_Assignment_Rules.json
│   ├── Daily_Processing_Master.csv
│   └── Processing_Metrics.csv
└── README.md
```

---

## Workspace Locations

### Daily Processing Workspace

**Location:** `/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/DAILIES/Daily_Processing/`

**Structure:**
```
Daily_Processing/
├── YYYY-MM-DD_Collection/
│   ├── 01_Collected_Files/
│   ├── 02_Extracted_Tasks/
│   ├── 03_Gap_Analysis/
│   ├── 04_Task_Templates/
│   ├── 05_Distribution_Plan/
│   └── 06_Processing_Log.md
└── Archive/
```

### Video Processing Workspace

**Location:** `/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/`

**Structure:**
```
RESEARCHES/
├── 00_SEARCH_QUEUE/
├── 01_VIDEO_QUEUE/
├── 02_TRANSCRIPTIONS/
├── 03_ANALYSIS/
│   ├── Extractions/
│   ├── Gap_Analysis/
│   └── Library_Mapping/
└── 04_INTEGRATION/
```

---

## Key Concepts

### Gap Analysis Methodology

Both workflows use the RESEARCHES Gap Analysis methodology to identify:

**EXISTS:**
- Already in TASK_MANAGERS
- All required tools/objects in LIBRARIES
- **Action:** Use existing template

**LIBRARY_ONLY:**
- Not in TASK_MANAGERS
- All tools/objects exist in LIBRARIES
- **Action:** Create task template only

**NEW:**
- Not in TASK_MANAGERS
- Some/all tools/objects missing from LIBRARIES
- **Action:** Create library entries + task template

### Entity Naming Conventions

**Task Templates:** `ACTION_OBJECT_CONTEXT` (all caps, underscores)
- Example: `GENERATE_LEADS_VIA_LINKEDIN_SALES_NAVIGATOR`

**Step Templates:** `ACTION_OBJECT_SPECIFIC_DETAIL` (all caps, underscores)
- Example: `EXPORT_CONTACTS_TO_CSV`

**Skills:** `"action via tool"` (lowercase, natural language)
- Example: `"generate leads via linkedin sales navigator"`

**Tool IDs:** `TOL-[CATEGORY]-###`
- Example: `TOL-LG-015` (LinkedIn Sales Navigator)

### Task Assignment Algorithm

**Multi-factor scoring (100 points total):**
1. **Profession Match:** 40 points
   - Perfect: 40, Partial: 30, Transferable: 20, No match: 0
2. **Department Match:** 20 points
   - Same: 20, Related: 10, Unrelated: 0
3. **Skill Level:** 20 points
   - Match: 20, Close: 10, Mismatch: -10
4. **Workload Balance:** 20 points
   - 0-2 tasks: 20, 3-5: 15, 6-8: 10, 9-10: 5, >10: excluded

**Workload Limits:**
- Maximum: 10 tasks/employee/day
- Preferred: 5 tasks/employee/day
- Target variance: <20% across department

---

## Success Metrics

### Daily Processing (GDS-001)

**Daily:**
- Processing time: <3 hours (target: <2h with automation)
- Files collected: ~60 (ALL files from each employee)
- Tasks extracted: 50-100
- New templates: 2-5 TST-###
- Distribution accuracy: >95%

**Weekly:**
- Tasks processed: 250-500
- Template growth: 10-25 TST-###
- Workload variance: <20%
- Processing consistency: 5 days/week

**Monthly:**
- Templates created: 40-100 TST-###
- Processing time trend: Decreasing
- Assignment accuracy: >90%

### Video Processing (GDS-002)

**Per Video:**
- Processing time: 50-100 minutes
- Transcription completeness: 100% (all 14 sections)
- Gap coverage: All missing entities identified
- Integration success: All entities created and mapped

**Weekly:**
- Videos processed: 3-5
- Library growth: 10-25 new entities
- Time efficiency: 90-95% improvement vs manual

**Monthly:**
- Total videos: 12-20
- New templates: 40-100 task templates
- Tool library growth: 20-50 new tools
- Coverage improvement: Tracked % increase

---

## Integration Between Workflows

### When Video Tasks Appear in Daily Processing

1. Daily processing (GDS-001) identifies video-related tasks
2. Route to RESEARCHES workflow (GDS-002)
3. Process through 6-milestone video workflow (MLT-010 through MLT-015)
4. New entities created become available for future daily processing
5. Report completion back to daily processing log

**Example:**
- Daily file mentions: "Process video transcript about Claude MCP"
- Route to Video Queue (GDS-002, Milestone MLT-011)
- Process video → Create TST-XXX templates
- Templates now available for assignment in future daily processing

---

## Getting Started

### For Daily Processing

1. Read GDS-001 at `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md` completely
2. Review support files in `/ENTITIES/DAILIES/Daily_Processing/Daily_Processing_Workflow/Support_Files/` folder
3. Load employee profiles from `/ENTITIES/TALENTS/Employees/profiles/Work/`
4. Review gap analysis examples in `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`
5. Create first workspace: `ENTITIES/DAILIES/Daily_Processing/2025-MM-DD_Collection/`
6. Follow 9-milestone workflow (MLT-001 through MLT-009)
7. Start with 5-10 employee pilot before full rollout

### For Video Processing

1. Read [GDS-002](GDS-002_Video_Transcript_Processing_Instructions.md) completely
2. Review existing RESEARCHES structure in `/ENTITIES/TASK_MANAGERS/RESEARCHES/`
3. Load PMT-004 and PMT-012 prompts
4. Review gap analysis examples
5. Start with Milestone MLT-010 (Search Queue) or MLT-011 (Video Queue) if videos ready
6. Process first video following all 6 milestones
7. Track progress using automation scripts

---

## Automation Opportunities

### Daily Processing

**Immediate scripts to create:**
1. `collect_daily_files.py` - Auto-scan and collect (saves 20 min)
2. `extract_tasks_batch.py` - Batch MAIN_PROMPT_v6 processing (saves 30 min)
3. `assign_tasks.py` - Apply assignment algorithm (saves 30 min)
4. `distribute_tasks.py` - Create tasks.md files (saves 20 min)
5. `generate_report.py` - Auto-generate reports (saves 10 min)

**Potential time savings:** 110 minutes/day (1.8 hours)

### Video Processing

**Already available scripts:**
- Search Queue: `assign_search.py`, `complete_search.py`
- Video Queue: `add_video_to_queue.py`, `update_queue_status.py`, `calculate_priority.py`
- Progress: `update_progress.py`, `generate_reports.py`

**Scripts location:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/[PHASE]/scripts/`

---

## Critical Files Reference

### For Daily Processing
- **MAIN_PROMPT_v6.md:** `/ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6.md`
- **Gap Analysis:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`
- **Task Templates:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/`
- **Employee Profiles:** `/ENTITIES/TALENTS/Employees/profiles/Work/`
- **LIBRARIES:** `/ENTITIES/LIBRARIES/` (Tools, Actions, Objects, Skills)

### For Video Processing
- **Workflow Overview:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/README.md`
- **Complete Workflow:** `/ENTITIES/PROMPTS/PMT-012_Transcript_Processing_Workflow.md`
- **Transcription:** `/ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md`
- **Gap Analysis:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`

---

## Version History

**Version 1.0** (2025-11-25)
- Initial release
- GDS-001: Daily Task Processing Instructions
- GDS-002: Video Transcript Processing Instructions
- Support files and workspace structures created
- Gap Analysis methodology integrated into both workflows

---

## Future Guides (Planned)

- **GDS-003:** Employee Onboarding Process
- **GDS-004:** Weekly Reporting & Analytics
- **GDS-005:** Task Template Maintenance
- **GDS-006:** Library Management & Cleanup

---

**Document Maintained By:** AI & Automation Team
**Last Updated:** 2025-11-25
**Status:** Active - Production Ready
**Next Review:** 2025-12-25 (1 month)
