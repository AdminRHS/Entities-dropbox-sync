# RESEARCHES - Video Research & Taxonomy Integration System

## Overview

Complete workflow for discovering, processing, and integrating video content into the ENTITIES ecosystem.

---

## Workflow Phases

### Phase 0: Search Queue (00_SEARCH_QUEUE)
**Purpose**: Assign and track video search tasks based on weekly reports

**Process**:
1. Weekly report identifies research gaps
2. Search prompts generated for each department
3. Tasks assigned to employees
4. Employees execute searches
5. Videos added to Video Queue

**Key Files**:
- `Search_Queue_Master.csv` - Active search assignments
- `Search_Prompts/` - Generated search queries
- `scripts/assign_search.py` - Assign new search
- `scripts/complete_search.py` - Mark search complete

**Usage**:
```bash
# Assign a search
python 00_SEARCH_QUEUE/scripts/assign_search.py "Employee Name" "Department" "Topic"

# Complete search
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 15
```

---

### Phase 1: Video Queue (01_VIDEO_QUEUE)
**Purpose**: Accumulate and prioritize videos before processing

**Process**:
1. Videos from searches added to queue
2. Metadata captured (title, URL, source, employee)
3. Priority calculated
4. Videos selected for transcription
5. Batch processing enabled

**Key Files**:
- `Video_Queue_Master.csv` - Main queue with metadata
- `Video_Queue_Dashboard.html` - Visual queue manager
- `scripts/add_video_to_queue.py` - Add video
- `scripts/update_queue_status.py` - Update status

**Usage**:
```bash
# Add video to queue
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=VIDEO_ID" \
    "Your Name" \
    "Research Topic" \
    "Perplexity"

# Update status
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Selected
```

---

### Phase 2: Transcriptions (02_TRANSCRIPTIONS)
**Purpose**: Convert videos to structured markdown with full taxonomy analysis

**Process**: Use PMT-004 (Video Transcription v4.1)

**Outputs**: `Video_XXX.md` with:
- Full timestamped transcription
- Video metadata (title, description, duration)
- Embedded taxonomy analysis:
  - Workflows identified (WRF-###)
  - Action verbs (7 categories A-G)
  - Tools & Technologies Matrix (TOL-###)
  - Objects & Deliverables (OBJ-###)
  - Integration Patterns
  - Task Chains
  - 37+ entities pre-categorized

---

### Phase 3: Analysis (03_ANALYSIS)
**Purpose**: Deep entity extraction and library integration

**Subdirectories**:

- `Extractions/` - Entity extraction & cross-referencing (PMT-007)
- `Gap_Analysis/` - Library comparison & gap identification (PMT-009 Part 1)
- `Library_Mapping/` - Final mapping & documentation (PMT-009 Part 3)

**Process**:

- PMT-007: Entity Extraction & Cross-Referencing
- PMT-009 Part 1: Gap Analysis

---

### Phase 4: Integration (04_INTEGRATION)
**Purpose**: Create JSON entities and integrate

**Process**: PMT-009 Parts 2 & 3
- Create tool/workflow/task JSON files
- Integrate into LIBRARIES and TASK_MANAGERS
- Generate mapping reports
- Update registries

---

## Directory Structure

```
RESEARCHES/
├── 00_SEARCH_QUEUE/          # Search assignment & tracking
│   ├── Active_Searches/      # In-progress searches
│   ├── Completed_Searches/   # Completed search reports
│   ├── Search_Prompts/       # Generated search queries
│   ├── scripts/              # Management scripts
│   ├── Search_Queue_Master.csv
│   └── README.md
│
├── 01_VIDEO_QUEUE/           # Video accumulation & prioritization
│   ├── scripts/              # Queue management
│   ├── Video_Queue_Master.csv
│   ├── Video_Queue_Dashboard.html
│   └── README.md
│
├── 02_TRANSCRIPTIONS/        # Processed video transcriptions
├── 03_ANALYSIS/              # Analysis outputs
│   ├── Extractions/
│   ├── Gap_Analysis/
│   └── Library_Mapping/
│
├── 04_INTEGRATION/           # Integration tracking
├── PROMPTS/                  # All research prompts (PMT-XXX)
├── DATA/                     # Research data & metadata
├── REPORTS/                  # Research reports
└── ARCHIVE/                  # Archived content
```

---

## Prompts Reference

All prompts located in `PROMPTS/` or main `ENTITIES/PROMPTS/`:

**Video Processing**:
- PMT-004: Video Transcription v4.1
- PMT-005: Video Naming Alternatives
- PMT-006: Video Analysis
- PMT-007: Objects Library Extraction
- PMT-008: Video Analysis Improvements
- PMT-009: Taxonomy Integration (Parts 1-3)
- PMT-071: Actions Library Extraction
- PMT-090: YouTube Video Processing

**Search & Discovery**:
- PMT-048: YouTube AI Tools Daily
- PMT-089: YouTube AI Tutorials Research
- PMT-097: YouTube AI Models Deep Research

---

## Integration with Main ENTITIES

**PROMPTS**: All PMT-XXX files in `ENTITIES/PROMPTS/`
**REPORTS**: Weekly analysis in `ENTITIES/REPORTS/Weekly_Analysis/`
**WORKFLOWS**: WRF-VID-001 in `TASK_MANAGERS/TSM-006_Workflows/`

---

## Quick Start

### 1. Assign a Video Search
```bash
python 00_SEARCH_QUEUE/scripts/assign_search.py "John Doe" "AI" "Claude tutorials"
```

### 2. Complete Search & Add Videos
```bash
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 10
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py "https://youtube.com/..." "John" "Topic" "Perplexity"
```

### 3. Process Video (6-Phase Workflow)

1. Select from queue dashboard
2. **Phase 1**: Run transcription + analysis (PMT-004)
3. **Phase 2**: Extract entities & cross-references (PMT-007)
4. **Phase 3**: Gap analysis (PMT-009 Part 1)
5. **Phase 4**: Integration (PMT-009 Part 2)
6. **Phase 5**: Mapping (PMT-009 Part 3)

---

## Scripts & Automation

This system includes **14 Python scripts** for automation:

- **Search Queue**: 2 scripts (assign, complete)
- **Video Queue**: 6 scripts (add, update, export, priority, manager)
- **Progress Tracking**: 2 scripts (update progress, generate reports) ⭐ NEW
- **Utilities**: 3 scripts (config, utils, scanner)

**See:** [SCRIPTS_INVENTORY.md](SCRIPTS_INVENTORY.md) for complete documentation

**Progress Tracker**: `VIDEO_PROGRESS_TRACKER.csv` tracks all videos through **7 phases** (Phase_0 through Phase_5, plus Complete)

---

**Last Updated**: 2025-11-24
**Status**: Active - Production Ready
**Scripts**: 14 automation scripts available
**Workflow**: 7-phase system (9 phases → 7 phases restructure on 2025-11-24)
**Progress Tracking**: Automated phase tracking with weekly reports
