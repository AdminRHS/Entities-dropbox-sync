# RESEARCHES System - Complete Overview

**Date:** 2025-11-24
**Status:** ✅ Active - Production Ready
**Workflow:** 7-Phase System (Restructured from 9 phases)

---

## Executive Summary

The RESEARCHES system is a complete video research and taxonomy integration pipeline that discovers, processes, and integrates video content into the ENTITIES ecosystem. It tracks videos from initial search through final library mapping across 7 distinct phases.

### Key Metrics
- **Total Videos Processed:** 23+ videos (Video_001 through Video_023)
- **Automation Scripts:** 14 Python scripts
- **Processing Phases:** 7 (Phase_0 through Phase_5, plus Complete)
- **Prompts Available:** 50+ research and processing prompts
- **Time Efficiency:** ~25% faster after 2025-11-24 restructure

---

## System Architecture

### 7-Phase Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 0: Search Queue (00_SEARCH_QUEUE)                    │
│ • Assign video search tasks based on weekly reports        │
│ • Track employee search assignments                        │
│ • Complete searches, add videos to queue                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 0→1 Transition: Video Queue (01_VIDEO_QUEUE)         │
│ • Accumulate and prioritize videos                         │
│ • Capture metadata (title, URL, source, employee)          │
│ • Select videos for transcription                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Transcribed (02_TRANSCRIPTIONS)                   │
│ • Full transcription + comprehensive taxonomy analysis     │
│ • PMT-004: Video Transcription v4.1                        │
│ • Output: 37+ entities pre-categorized                     │
│   - Workflows (WRF-###), Tools (TOL-###)                   │
│   - Action verbs (7 categories), Objects (OBJ-###)         │
│   - Integration patterns, Task chains                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 2: Extraction (03_ANALYSIS/Extractions/)             │
│ • Deep entity extraction & cross-referencing               │
│ • PMT-007: Objects Library Extraction                      │
│ • Extract ALL entity types + bidirectional links           │
│   - Objects, Tools, Actions, Workflows                     │
│   - Professions, Skills, Departments                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: Gap Analysis (03_ANALYSIS/Gap_Analysis/)          │
│ • Library comparison & gap identification                  │
│ • PMT-009 Part 1: Taxonomy Integration                     │
│ • Identify NEW vs EXISTING entities                        │
│ • Detect duplicates, prioritize integration                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 4: Integration (04_INTEGRATION/)                     │
│ • JSON creation & taxonomy integration                     │
│ • PMT-009 Part 2: Taxonomy Integration                     │
│ • Create JSON files for new entities                       │
│ • Update master registries, move files to LIBRARIES        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 5: Mapping (03_ANALYSIS/Library_Mapping/)            │
│ • Final mapping & documentation                            │
│ • PMT-009 Part 3: Taxonomy Integration                     │
│ • Generate library mapping reports                         │
│ • Document cross-references, verify bidirectional links    │
└─────────────────────────────────────────────────────────────┘
                            ↓
                     [Complete Status]
```

---

## Directory Structure

```
RESEARCHES/
├── 00_SEARCH_QUEUE/              # Video search assignment & tracking
│   ├── Active_Searches/          # In-progress search tasks
│   ├── Completed_Searches/       # Completed search reports
│   ├── Search_Prompts/           # Generated search queries
│   ├── scripts/                  # Search management (2 scripts)
│   │   ├── assign_search.py
│   │   └── complete_search.py
│   ├── Search_Queue_Master.csv
│   └── README.md
│
├── 01_VIDEO_QUEUE/               # Video accumulation & prioritization
│   ├── scripts/                  # Queue management (6 scripts)
│   │   ├── add_video_to_queue.py
│   │   ├── add_video_to_queue_simple.py
│   │   ├── update_queue_status.py
│   │   ├── calculate_priority.py
│   │   ├── export_queue.py
│   │   └── video_queue_manager.py (CLI interface)
│   ├── Video_Queue_Master.csv
│   ├── Video_Queue_Dashboard.html
│   └── README.md
│
├── 02_TRANSCRIPTIONS/            # Video transcriptions (23+ files)
│   ├── Video_001.md through Video_023.md
│   ├── Video_19_Taxonomy_Extraction.md
│   ├── Video_19_ExecutionFlow.md
│   ├── Video_19_Processing_Summary.md
│   ├── Video_16_Processing_Summary.md
│   ├── Video_Queue_Tracker.md
│   ├── Video_Discovery_Pipeline.md
│   └── README.md
│
├── 03_ANALYSIS/                  # Analysis outputs
│   ├── Extractions/              # Entity extraction reports
│   │   ├── Video_002_Extraction_Inventory.md
│   │   ├── Video_022_Phase3_Analysis.md
│   │   └── Video_022_Phase4_Objects.md
│   ├── Gap_Analysis/             # Gap identification
│   │   ├── Video_002_Gap_Analysis.md
│   │   ├── Video_009_Gap_Analysis.md
│   │   └── Video_022_Gap_Analysis.md
│   ├── Library_Mapping/          # Final mapping reports
│   │   ├── Video_001_Library_Mapping_Report.md
│   │   ├── Video_002_Library_Mapping_Report.md
│   │   ├── Video_005_Library_Mapping_Report.md
│   │   ├── Video_009_Library_Mapping_Report.md
│   │   ├── Video_017_Library_Mapping_Report.md
│   │   └── Video_018_Library_Mapping_Report.md
│   ├── Phase_Reports/            # Historical phase completion
│   │   ├── Phase_7_Completion_Report.md
│   │   └── Phase_9_Completion_Report.md
│   └── Validation/               # Tool validation
│       └── Tool_Validation_Report_Video_006_008.md
│
├── 04_INTEGRATION/               # Integration tracking (NEW)
│   └── [Integration reports and tracking files]
│
├── scripts/                      # Utility & tracking scripts (3 scripts)
│   ├── config.py                 # Configuration management
│   ├── utils.py                  # Shared utility functions
│   ├── video_id_scanner.py       # ID validation scanner
│   ├── update_video_progress.py  # Progress tracker (NEW)
│   └── generate_progress_report.py  # Report generator (NEW)
│
├── PROMPTS/                      # Research prompts (50+ files)
│   ├── PMT-044_Sales_Department_Research.md
│   ├── PMT-045_SMM_Document_Processing.md
│   ├── PMT-046_VSCode_Agent_HQ_Research.md
│   ├── PMT-047_YouTube_AI_HR_Tutorials.md
│   ├── PMT-048_YouTube_AI_Tools_Daily.md
│   ├── PMT-049_YouTube_HR_Automation.md
│   ├── PMT-050_YouTube_Remote_Helpers.md
│   ├── PMT-051_YouTube_AI_Design_Tools_Workflows.md
│   ├── PMT-052_*_various.md (Multiple variants)
│   ├── PMT-082_Advanced_Prompting_Course_Creation.md
│   ├── PMT-083_GenSpark_Course_Creation.md
│   ├── PMT-085_Photo_Editing_AI_Research.md
│   ├── PMT-089_YouTube_AI_Tutorials_Research.md
│   ├── PMT-093_Design_AI_Video_Discovery.md
│   ├── PMT-098_OpenAI_Automation_Examples.md
│   ├── Universal Research Prompt.md
│   └── README_MIGRATION.md
│
├── DATA/                         # Research data & metadata
│   └── Video_Search_Prompt_n8n_OpenAI_Google.md
│
├── REPORTS/                      # System reports
│   ├── VIDEO_RESEARCHES_Example_Report.md
│   ├── Video_Processing_README.md
│   ├── Phase_Redundancy_Analysis_2025-11-24.md
│   ├── Phase_Restructure_Plan_2025-11-24.md
│   └── Phase_Restructure_Summary_2025-11-24.md
│
├── ARCHIVE/                      # Historical content
│   ├── Pre_Taxonomy_Cleanup/    # Pre-2025-11-24 structure
│   ├── 04_INFLUENCER_DATA/      # Old influencer research
│   └── [Various archived reports and research]
│
├── README.md                     # Main system documentation
├── SCRIPTS_INVENTORY.md          # Complete script documentation
├── SYSTEM_OVERVIEW.md           # This file
└── VIDEO_PROGRESS_TRACKER.csv   # Automated progress tracking (NEW)
```

---

## Video Inventory

### Transcribed Videos (23 Total)

| Video | Title/Topic | Format | Status |
|-------|-------------|--------|--------|
| Video_001 | AI Agents for Creative AI (GLIF) | Basic | Transcribed |
| Video_002 | [Topic TBD] | [Format] | Transcribed |
| Video_003 | [Topic TBD] | [Format] | Transcribed |
| Video_004 | [Topic TBD] | [Format] | Transcribed |
| Video_005 | [Topic TBD] | [Format] | Transcribed |
| Video_006 | [Topic TBD] | [Format] | Transcribed |
| Video_007 | [Topic TBD] | [Format] | Transcribed |
| Video_008 | [Topic TBD] | [Format] | Transcribed |
| Video_009 | [Topic TBD] | [Format] | Transcribed |
| Video_010 | [Topic TBD] | [Format] | Transcribed |
| Video_011 | [Topic TBD] | [Format] | Transcribed |
| Video_012 | [Topic TBD] | [Format] | Transcribed |
| Video_013 | [Topic TBD] | [Format] | Transcribed |
| Video_014 | [Topic TBD] | [Format] | Transcribed |
| Video_016 | [Topic TBD] | [Format] | Transcribed + Summary |
| Video_017 | [Topic TBD] | [Format] | Transcribed |
| Video_018 | [Topic TBD] | [Format] | Transcribed |
| Video_019 | [Topic TBD] | Advanced | Transcribed + Taxonomy + Flow + Summary |
| Video_020 | [Topic TBD] | [Format] | Transcribed |
| Video_021 | n8n Quickstart: Workflow Fundamentals | Advanced | Transcribed with full taxonomy |
| Video_022 | [Topic TBD] | [Format] | Transcribed + Analysis + Objects + Gap |
| Video_023 | Google AI Studio Full Walkthrough | Latest v4.0 | Transcribed with 37 entities |

**Note:** Video_015 is missing (gap in numbering)

### Processing Stages Breakdown

- **Phase 1 Complete (Transcribed):** 23 videos
- **Phase 2 Complete (Extraction):** 3 videos (Video_002, Video_022, Video_023 implied)
- **Phase 3 Complete (Gap Analysis):** 3 videos (Video_002, Video_009, Video_022)
- **Phase 4 Complete (Integration):** Unknown (no tracking yet)
- **Phase 5 Complete (Mapping):** 6 videos (Video_001, 002, 005, 009, 017, 018)

---

## Automation Scripts (14 Total)

### 🔍 Search Queue Scripts (2)
1. **assign_search.py** - Assign video search tasks to employees
2. **complete_search.py** - Mark searches complete, record results

### 📹 Video Queue Scripts (6)
3. **add_video_to_queue.py** - Add videos with full metadata
4. **add_video_to_queue_simple.py** - Quick video addition
5. **update_queue_status.py** - Update video status in queue
6. **calculate_priority.py** - Calculate/update priority scores
7. **export_queue.py** - Export queue to CSV/JSON/Markdown
8. **video_queue_manager.py** - Interactive CLI queue manager

### 📊 Progress Tracking Scripts (2) ⭐ NEW
9. **update_video_progress.py** - Track video through 7 phases
10. **generate_progress_report.py** - Generate summary/detailed/weekly reports

### 🛠️ Utility Scripts (4)
11. **config.py** - Configuration management
12. **utils.py** - Shared utility functions
13. **video_id_scanner.py** - Validate video IDs across system
14. [Additional utility - TBD]

---

## Key Processing Prompts

### Core Video Processing
- **PMT-004:** Video Transcription v4.1 (Phase 1)
- **PMT-005:** Video Naming Alternatives (DEPRECATED - merged into PMT-004)
- **PMT-006:** Video Analysis (DEPRECATED - merged into PMT-004)
- **PMT-007:** Objects Library Extraction (Phase 2)
- **PMT-008:** Video Analysis Improvements
- **PMT-009:** Taxonomy Integration Parts 1-3 (Phases 3-5)
- **PMT-071:** Actions Library Extraction
- **PMT-090:** YouTube Video Processing

### Research & Discovery
- **PMT-048:** YouTube AI Tools Daily
- **PMT-089:** YouTube AI Tutorials Research
- **PMT-097:** YouTube AI Models Deep Research
- **PMT-093:** Design AI Video Discovery
- **PMT-098:** OpenAI Automation Examples

### Department-Specific Research
- **PMT-044:** Sales Department Research
- **PMT-045:** SMM Document Processing
- **PMT-046:** VSCode Agent HQ Research
- **PMT-047:** YouTube AI HR Tutorials
- **PMT-049:** YouTube HR Automation
- **PMT-050:** YouTube Remote Helpers
- **PMT-051:** YouTube AI Design Tools & Workflows
- **PMT-052:** Various (VSCode Extensions, Management, Leadership)
- **PMT-085:** Photo Editing AI Research

### Course Creation
- **PMT-082:** Advanced Prompting Course Creation
- **PMT-083:** GenSpark Course Creation

---

## Recent System Changes (2025-11-24)

### Phase Restructure: 9 → 7 Phases

**Eliminated:**
- ❌ **Phase_2_Named (PMT-005)** - Title already captured in PMT-004
- ❌ **Phase_3_Analyzed (PMT-006)** - Analysis already done in PMT-004

**Renamed:**
- **Phase_4_Objects → Phase_2_Extraction** - Reflects ALL entity extraction
- **Phase_7_Mapped → Phase_5_Mapping** - Active verb form

**New Numbering:**
```
OLD: Phase_0, 1, 2, 3, 4, 5, 6, 7, Complete (9 phases)
NEW: Phase_0, 1, 2, 3, 4, 5, Complete (7 phases)
```

**Benefits:**
- ⚡ 25% faster processing time
- 📝 Clearer phase naming
- 🎯 No duplication between phases
- 🧠 Simpler mental model

**Files Updated:**
- `scripts/update_video_progress.py`
- `scripts/generate_progress_report.py`
- `README.md`
- `SCRIPTS_INVENTORY.md`
- All phase documentation

---

## Integration with ENTITIES Ecosystem

### Outputs Flow To:

**PROMPTS:**
- All PMT-XXX files → `ENTITIES/PROMPTS/`

**LIBRARIES:**
- Tools → `ENTITIES/LIBRARIES/Tools/TOOL-{CATEGORY}-###.json`
- Actions → `ENTITIES/LIBRARIES/Actions/Actions_Master.json`
- Objects → `ENTITIES/LIBRARIES/Responsibilities/Objects/`
- Professions → `ENTITIES/LIBRARIES/Responsibilities/Professions/`
- Skills → `ENTITIES/LIBRARIES/Skills/`

**TASK_MANAGERS:**
- Workflows → `ENTITIES/TASK_MANAGERS/TSM-006_Workflows/WRF-###.json`

**REPORTS:**
- Weekly Analysis → `ENTITIES/REPORTS/Weekly_Analysis/`

**REGISTRIES:**
- Master List → `ENTITIES/ENTITIES_MASTER_LIST.csv`

---

## Usage Quick Reference

### Add Video to System
```bash
# 1. Assign search (if needed)
python 00_SEARCH_QUEUE/scripts/assign_search.py "Employee" "Department" "Topic"

# 2. Complete search & add videos
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 10
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py "URL" "Employee" "Topic" "Source"

# 3. Add to progress tracker
python scripts/update_video_progress.py add 24 "Video Title" "URL" "Employee"
```

### Process Video Through Phases
```bash
# Phase 1: Transcribe (PMT-004)
python scripts/update_video_progress.py update 24 Phase_1_Transcribed

# Phase 2: Extract entities (PMT-007)
python scripts/update_video_progress.py update 24 Phase_2_Extraction

# Phase 3: Gap analysis (PMT-009 Part 1)
python scripts/update_video_progress.py update 24 Phase_3_Gap_Analysis

# Phase 4: Integration (PMT-009 Part 2)
python scripts/update_video_progress.py update 24 Phase_4_Integration

# Phase 5: Mapping (PMT-009 Part 3)
python scripts/update_video_progress.py update 24 Phase_5_Mapping

# Mark complete
python scripts/update_video_progress.py update 24 Complete
```

### Generate Reports
```bash
# View progress
python scripts/update_video_progress.py view
python scripts/update_video_progress.py view 24

# Generate reports
python scripts/generate_progress_report.py summary
python scripts/generate_progress_report.py weekly
python scripts/generate_progress_report.py all
```

---

## System Health Metrics

### Processing Velocity
- **Average Time per Video:** ~7-14 days (varies by complexity)
- **Bottleneck Phase:** Phase 4 (Integration) - requires manual JSON creation
- **Fastest Phase:** Phase 1 (Transcription) - ~1-2 hours with PMT-004

### Quality Metrics
- **Entity Extraction Rate:** 37+ entities per video (PMT-004 v4.0+)
- **Cross-Reference Completeness:** Bidirectional linking in Phase 2
- **Gap Detection Accuracy:** High (based on library comparison)

### Automation Level
- **Fully Automated:** Phases 0-1 (Search, Queue, Transcription)
- **Semi-Automated:** Phases 2-5 (Require prompt execution)
- **Manual:** JSON creation, file moving, registry updates

---

## Future Enhancements

### Automation Opportunities
1. Auto-generate JSON files from extraction reports
2. Auto-update ENTITIES_MASTER_LIST.csv
3. Auto-move files to LIBRARIES/TASK_MANAGERS
4. Batch processing for multiple videos

### Process Improvements
1. Real-time progress dashboard
2. Automated duplicate detection
3. Entity relationship visualization
4. Quality scoring for transcriptions

### Integration Enhancements
1. Direct API integration with YouTube
2. Real-time search result feeds
3. Automated priority calculation based on department needs
4. Cross-video entity relationship mapping

---

## Maintenance & Support

### Log Files
- Script logs: `scripts/logs/`
- Error tracking: `ARCHIVE/LOGS/`

### Backup Strategy
- All CSV files backed up before modifications
- Archive folder contains pre-restructure snapshots
- Git version control (if applicable)

### Documentation Updates
- README.md - Main system documentation
- SCRIPTS_INVENTORY.md - Script reference
- SYSTEM_OVERVIEW.md - This file
- Individual phase READMEs in subdirectories

---

## Contact & Ownership

**Maintained By:** Taxonomy Team
**Last Major Update:** 2025-11-24 (Phase Restructure)
**Status:** ✅ Production Ready
**Version:** 2.0 (Post-Restructure)

---

**For detailed workflow documentation, see:** [README.md](README.md)
**For script usage, see:** [SCRIPTS_INVENTORY.md](SCRIPTS_INVENTORY.md)
**For restructure details, see:** [REPORTS/Phase_Restructure_Summary_2025-11-24.md](REPORTS/Phase_Restructure_Summary_2025-11-24.md)
