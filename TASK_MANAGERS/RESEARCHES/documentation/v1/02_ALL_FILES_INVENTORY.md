# RESEARCHES 2 - Complete Files Inventory

**Generated:** 2025-12-04
**Purpose:** Complete listing of every file in the system
**Total Files:** 163 (excluding ARCHIVE)
**Total Size:** 5.1 MB

---

## 📋 Complete File List

### Root Level Files (5 files)

```
README.md                                   6.4 KB      Main system documentation
SYSTEM_OVERVIEW.md                         21.0 KB      Complete system architecture
SCRIPTS_INVENTORY.md                       11.0 KB      Scripts reference guide
TSM_TAXONOMY_INTEGRATION_SUMMARY.md         8.5 KB      Integration summary
RESEARCHES_Master_List.csv                  2.5 KB      25 RSR entities tracked
VIDEO_PROGRESS_TRACKER.csv                  3.2 KB      Video processing status
```

**Purpose:** Core system documentation and master tracking files

**Key Files:**
- **README.md** - Start here for system overview
- **SYSTEM_OVERVIEW.md** - Complete 7-phase workflow architecture
- **RESEARCHES_Master_List.csv** - Tracks all 25 RSR entities

---

### 00_SEARCH_QUEUE/ (5 files)

```
00_SEARCH_QUEUE/
├── README.md                               4.2 KB      Search queue documentation
├── Search_Queue_Master.csv                 0.5 KB      Empty/initialized tracker
│
├── scripts/
│   ├── assign_search.py                    3.8 KB      Assign search task
│   └── complete_search.py                  2.9 KB      Complete search task
│
├── Active_Searches/                        (empty)     Current searches
├── Completed_Searches/                     (empty)     Finished searches
└── Search_Prompts/                         (empty)     Search prompts
```

**Purpose:** Phase 0 - Video search assignment and tracking

**Key Files:**
- **assign_search.py** - Create new search assignment
- **complete_search.py** - Mark search as complete
- **Search_Queue_Master.csv** - Track search tasks

**CSV Columns:**
```
Search_ID, Topic, Assigned_To, Status, Date_Assigned, Videos_Found, Date_Completed
```

---

### 01_VIDEO_QUEUE/ (10 files)

```
01_VIDEO_QUEUE/
├── README.md                               5.8 KB      Queue documentation
├── Video_Queue_Master.csv                  1.8 KB      5 videos in queue
├── Video_Queue_Dashboard.html              12.5 KB     Visual dashboard
├── Priority_Scoring_Guide.md               3.2 KB      Priority calculation
│
└── scripts/
    ├── add_video_to_queue.py               6.4 KB      Add video with full metadata
    ├── add_video_to_queue_simple.py        3.2 KB      Quick add video
    ├── calculate_priority.py               4.8 KB      Calculate priority score
    ├── export_queue.py                     2.9 KB      Export queue data
    ├── update_queue_status.py              3.5 KB      Update video status
    └── video_queue_manager.py              8.2 KB      Master queue manager
```

**Purpose:** Phase 0→1 - Video accumulation, prioritization, and selection

**Key Files:**
- **Video_Queue_Master.csv** - Main queue with 5 videos
  - Columns: Queue_ID, Video_URL, Title, Channel, Duration, Priority_Score, Status, Added_Date, Assigned_To
  - Statuses: Queued, Selected, In_Progress, Completed

- **Video_Queue_Dashboard.html** - Interactive dashboard
  - Sort by priority, status, date
  - Visual priority indicators
  - Quick status updates

- **add_video_to_queue.py** - Full featured add
  - Fetches metadata from YouTube
  - Calculates priority score
  - Validates URL format

- **add_video_to_queue_simple.py** - Quick add
  - Manual metadata entry
  - Fast workflow
  - No API calls

**Priority Scoring (0-100):**
```
Date Score (30 points):       Recent = higher (30 days window)
Source Score (25 points):     Channel credibility 0-25
Topic Score (25 points):      Relevance to needs 0-25
Engagement Score (20 points): Views, likes, comments
```

---

### 02_TRANSCRIPTIONS/ (30+ files)

```
02_TRANSCRIPTIONS/
├── Video_001.md                           85.3 KB      Figma AI Tutorial
├── Video_002.md                           92.1 KB      ChatGPT Automation
├── Video_003.md                           78.5 KB      Midjourney Workflows
├── Video_004.md                           65.8 KB      Claude API Guide
├── Video_005.md                           71.2 KB      NotebookLM Deep Dive
├── Video_006.md                           88.9 KB      Perplexity Research
├── Video_007.md                           95.4 KB      Cursor AI Coding
├── Video_008.md                           82.6 KB      V0 Design Systems
├── Video_009.md                           76.3 KB      Lovable App Builder
├── Video_010.md                           69.7 KB      Bolt.new Workflows
├── Video_011.md                           73.8 KB      GitHub Copilot Guide
├── Video_012.md                           81.5 KB      Replit AI Features
├── Video_013.md                           87.2 KB      Gemini 2.0 Features
├── Video_014.md                           79.6 KB      Sora Video Generation
├── Video_015.md                           84.1 KB      Kling AI Videos
├── Video_016.md                           90.8 KB      Runway Gen-3
├── Video_017.md                           75.9 KB      Pika Art Workflows
├── Video_018.md                           83.4 KB      HeyGen Avatars
├── Video_019.md                           77.2 KB      Descript Editing
├── Video_020.md                           86.5 KB      CapCut AI Features
├── Video_021.md                           91.3 KB      Canva AI Tools
├── Video_022.md                           80.7 KB      Adobe Firefly
├── Video_023.md                           74.6 KB      Framer AI Design
├── Video_024.md                           88.2 KB      Webflow Workflows
├── Video_025.md                           82.9 KB      Make.com Automation
├── Video_026.md                           76.4 KB      Zapier AI Actions
├── Video_027.md                           85.7 KB      Airtable Automation
├── Video_028.md                           79.3 KB      Notion AI Features
│
├── Transcription_Index.md                  8.5 KB      Index of all videos
├── Video_Metadata_Summary.json            15.2 KB      Aggregated metadata
└── Entity_Extraction_Index.md             12.8 KB      Cross-reference index
```

**Purpose:** Phase 1 - Complete video transcriptions with 37+ entity extraction

**File Structure (each Video_XXX.md):**
```markdown
# Video Metadata (Header)
- Title: Full video title
- URL: YouTube URL
- Channel: Channel name
- Duration: MM:SS
- Upload Date: YYYY-MM-DD
- Processed Date: YYYY-MM-DD
- Processed By: Name
- Video ID: VID-XXX

# Video Summary
3-5 paragraph executive summary

# Pre-Categorized Entities (37+ minimum)

## WORKFLOWS (WRF-###)
1. [WRF-###] Workflow Name
   - Description
   - Steps: [list]
   - Tools: [TOL-### links]
   - Duration: X minutes

## TOOLS (TOL-###)
1. [TOL-###] Tool Name
   - Category: [Software/Platform/Plugin]
   - Purpose: Description
   - Features: [list]
   - Objects Created: [OBJ-### links]

## OBJECTS (OBJ-###)
1. [OBJ-###] Object Name
   - Type: [Digital artifact type]
   - Created By: [TOL-### link]
   - Used In: [WRF-### links]

## ACTIONS (Categories A-G)
### Category A: Interface Creation & Design
- [ACT-###] Action verb + context

### Category B: Content Generation
- [ACT-###] Action verb + context

### Category C: Design Refinement
- [ACT-###] Action verb + context

### Category D: Asset Management
- [ACT-###] Action verb + context

### Category E: Collaboration
- [ACT-###] Action verb + context

### Category F: Analysis & Research
- [ACT-###] Action verb + context

### Category G: Automation & Integration
- [ACT-###] Action verb + context

## PROFESSIONS & SKILLS
- [PRF-###] Profession Name
- [SKL-###] Skill Name

## DEPARTMENTS
- [DPT-###] Department Name

## INTEGRATION PATTERNS
Cross-references and relationships:
- Tool X → creates → Object Y
- Workflow A → uses → Tool B, Tool C
- Profession P → requires → Skill S1, S2

# Full Transcript
[00:00] Timestamped transcript text...
[00:15] More transcript...
[continued throughout video]

# Extraction Metadata
- Total Workflows: X
- Total Tools: Y
- Total Objects: Z
- Total Actions: A
- Total Entities: 37+
- Cross-References: B
```

**Key Prompts:**
- PMT-004: Video Transcription v4.1
  - Input: Video URL + raw transcript
  - Output: Structured Video_XXX.md with 37+ entities
  - Processing time: 1-2 hours with AI

**Supporting Files:**
- **Transcription_Index.md** - Quick reference table
  ```
  | ID  | Title                | Channel       | Duration | Entities | Status    |
  | --- | -------------------- | ------------- | -------- | -------- | --------- |
  | 001 | Figma AI Tutorial    | Design Master | 18:42    | 42       | Complete  |
  ```

- **Video_Metadata_Summary.json** - Aggregated data
  ```json
  {
    "total_videos": 28,
    "total_entities": 1247,
    "avg_entities_per_video": 44.5,
    "avg_duration": "16:23",
    "top_channels": ["Channel A", "Channel B"],
    "top_tools": ["TOL-001", "TOL-042", "TOL-089"]
  }
  ```

- **Entity_Extraction_Index.md** - Cross-reference
  ```
  TOL-042 (Figma) appears in: Video_001, Video_003, Video_021, Video_023
  WRF-158 (Design System Creation) appears in: Video_001, Video_008, Video_024
  ```

---

### 03_ANALYSIS/ (25+ files)

```
03_ANALYSIS/
├── Extractions/                            # Phase 2: Deep entity extraction
│   ├── Video_001_Phase3_Analysis.md        15.2 KB     Deep analysis
│   ├── Video_001_Phase4_Objects.md         12.8 KB     Object extraction
│   ├── Video_024_Phase3_Analysis.md        16.5 KB     Deep analysis
│   ├── Video_024_Phase4_Objects.md         13.9 KB     Object extraction
│   └── [more extraction files]
│
├── Gap_Analysis/                           # Phase 3: Gap identification
│   ├── Video_001_Gap_Analysis.md           18.3 KB     Gap report
│   ├── Video_024_Gap_Analysis.md           19.7 KB     Gap report
│   └── [more gap analysis files]
│
├── Integration/                            # Integration tracking
│   ├── Integration_Status.md               8.5 KB      Overall status
│   └── Weekly_Integration_Summary.md       6.2 KB      Weekly summary
│
├── Library_Mapping/                        # Phase 5: Library mapping
│   ├── Video_001_Library_Mapping_Report.md 22.4 KB     Final report
│   ├── Video_024_Library_Mapping_Report.md 24.8 KB     Final report
│   ├── Video_025_Library_Mapping_Report.md 21.3 KB     Final report
│   ├── Video_026_Library_Mapping_Report.md 23.6 KB     Final report
│   ├── Video_027_Library_Mapping_Report.md 20.9 KB     Final report
│   ├── Video_028_Library_Mapping_Report.md 22.1 KB     Final report
│   └── [more mapping reports]
│
├── Phase_Reports/                          # Phase summaries
│   ├── Phase_2_Summary.md                  9.8 KB      Extraction summary
│   ├── Phase_3_Summary.md                  11.2 KB     Gap analysis summary
│   └── Phase_5_Summary.md                  10.6 KB     Mapping summary
│
└── Validation/                             # Quality validation
    ├── Entity_Validation.md                7.4 KB      Entity quality check
    └── Cross_Reference_Check.md            6.8 KB      Cross-ref validation
```

**Purpose:** Phases 2-3-5 analysis, gap identification, and mapping

**Phase 2: Extractions/**
- **Video_XXX_Phase3_Analysis.md** - Deep analysis
  ```markdown
  # Video XXX - Phase 3 Deep Analysis

  ## Entity Expansion
  - Original entities: 42
  - Expanded entities: 68
  - New discoveries: 26

  ## Detailed Entity Analysis
  [Detailed breakdown of each entity]

  ## Cross-Reference Mapping
  [Complete relationship map]
  ```

- **Video_XXX_Phase4_Objects.md** - Object focus
  ```markdown
  # Video XXX - Phase 4 Objects Extraction

  ## Objects Identified: 35
  1. [OBJ-###] Object Name
     - Type: Digital artifact
     - Created by: [TOL-###]
     - Used in: [WRF-###, WRF-###]
     - Properties: [list]
  ```

**Phase 3: Gap_Analysis/**
- **Video_XXX_Gap_Analysis.md** - Gap identification
  ```markdown
  # Video XXX - Gap Analysis Report

  ## Summary
  - NEW Entities: 28 (need creation in LIBRARIES)
  - EXISTING Entities: 35 (already in system)
  - UPDATE Entities: 5 (need enhancement)

  ## Coverage Metrics
  - Before: 51% coverage
  - After: 96% coverage
  - Improvement: 45%

  ## NEW Entities Detail
  ### Tools (12 new)
  1. [TOL-###] Tool Name - Status: NEW
     - Why NEW: Not found in LIBRARIES/TOOLS/
     - Action: Create TOL-###.json
     - Priority: High

  ### Workflows (9 new)
  [Similar structure]

  ### Objects (7 new)
  [Similar structure]

  ## EXISTING Entities Detail
  [List of entities already in system]

  ## UPDATE Entities Detail
  [Entities needing enhancement]

  ## Recommendations
  1. Create 28 new JSON files
  2. Update 5 existing JSON files
  3. Add cross-references
  4. Validate bidirectional links
  ```

**Phase 5: Library_Mapping/**
- **Video_XXX_Library_Mapping_Report.md** - Final integration report
  ```markdown
  # Video XXX - Library Mapping Report

  ## Executive Summary
  - Video processed: [Title]
  - Total entities: 68
  - NEW created: 28 JSON files
  - EXISTING enhanced: 5 JSON files
  - Coverage improvement: 45%

  ## Integration Status
  ✅ All NEW entities created
  ✅ All UPDATE entities enhanced
  ✅ All cross-references added
  ✅ Bidirectional links validated

  ## Library Locations
  ### New Files Created (28)
  - LIBRARIES/TOOLS/TOL-159.json
  - LIBRARIES/TOOLS/TOL-160.json
  [full list]

  ### Files Updated (5)
  - LIBRARIES/WORKFLOWS/WRF-042.json
  [full list]

  ## Business Value
  - Departments benefited: 3 (Design, Development, Marketing)
  - Professions enabled: 5
  - Workflows enhanced: 12
  - Tools documented: 15

  ## Cross-Reference Map
  [Complete visual/text map of relationships]

  ## Quality Metrics
  - Cross-reference completeness: 100%
  - Bidirectional link validation: Passed
  - JSON schema validation: Passed
  - Entity uniqueness check: Passed
  ```

**Key Prompts:**
- PMT-007: Objects Library Extraction (Phase 2)
- PMT-009 Part 1: Gap Analysis (Phase 3)
- PMT-009 Part 3: Library Mapping (Phase 5)

**Key Scripts:**
```bash
# Phase 2-3: Run gap analysis
python scripts/video_gap_analyzer.py Video_024

# Phase 5: Generate final report
python scripts/video_integration_reporter.py Video_024 --include-cross-refs
```

---

### 04_INTEGRATION/ (3 files)

```
04_INTEGRATION/
├── Integration_Log.csv                     3.8 KB      Activity log
├── JSON_Creation_Tracker.md                5.2 KB      Tracks JSON files
└── Library_Update_History.md               4.6 KB      Update history
```

**Purpose:** Phase 4 - Track JSON file creation and library updates

**Integration_Log.csv:**
```csv
Log_ID, Video_ID, Entity_Type, Entity_ID, Action, File_Path, Date, Notes
LOG-001, Video_024, Tool, TOL-159, CREATE, LIBRARIES/TOOLS/TOL-159.json, 2025-12-01, New tool
LOG-002, Video_024, Workflow, WRF-042, UPDATE, LIBRARIES/WORKFLOWS/WRF-042.json, 2025-12-01, Enhanced
```

**JSON_Creation_Tracker.md:**
```markdown
# JSON Creation Tracker

## Video_024 Integration (2025-12-01)
### NEW Files Created: 28
- ✅ TOL-159.json - [Tool Name]
- ✅ TOL-160.json - [Tool Name]
- ✅ WRF-201.json - [Workflow Name]
[full list with checkboxes]

### Files Updated: 5
- ✅ WRF-042.json - Added new steps
- ✅ TOL-012.json - Enhanced features
[full list]

### Status: Complete
```

**Library_Update_History.md:**
```markdown
# Library Update History

## 2025-12-01: Video_024 Integration
- NEW: 28 entities
- UPDATE: 5 entities
- Total time: 45 minutes
- Coverage: +45%

## 2025-11-28: Video_023 Integration
[similar structure]
```

**Key Script:**
```bash
python scripts/video_json_updater.py Video_024
```

---

### DATA/ (2+ files)

```
DATA/
├── influencer_database.json               28.5 KB      Influencer data
├── video_metadata.json                    35.8 KB      Video metadata
└── research_datasets/                     (folder)     Additional datasets
```

**Purpose:** Research data and metadata storage

**influencer_database.json:**
```json
{
  "influencers": [
    {
      "influencer_id": "INF-001",
      "name": "Design Master",
      "platform": "YouTube",
      "channel_url": "https://youtube.com/@designmaster",
      "focus_areas": ["AI Design", "Figma", "UI/UX"],
      "subscriber_count": 250000,
      "video_count": 342,
      "avg_views": 15000,
      "credibility_score": 85,
      "last_checked": "2025-12-01",
      "notable_videos": ["VIDEO_URL_1", "VIDEO_URL_2"]
    }
  ]
}
```

**video_metadata.json:**
```json
{
  "videos": [
    {
      "video_id": "VID-001",
      "youtube_id": "dQw4w9WgXcQ",
      "title": "Video Title",
      "channel": "Channel Name",
      "duration": "18:42",
      "views": 45000,
      "likes": 2300,
      "upload_date": "2025-11-15",
      "tags": ["AI", "Design", "Tutorial"],
      "transcript_available": true,
      "processed": true,
      "entities_extracted": 42
    }
  ]
}
```

---

### PROMPTS/ (50+ files)

```
PROMPTS/
├── Transcription/
│   └── PMT-004_Video_Transcription_v4.1.md  25.8 KB    Main transcription prompt
│
├── PMT-007_Objects_Library_Extraction.md    18.5 KB    Deep extraction
├── PMT-009_Taxonomy_Integration_Part1.md    15.2 KB    Gap analysis
├── PMT-009_Taxonomy_Integration_Part2.md    16.8 KB    JSON creation
├── PMT-009_Taxonomy_Integration_Part3.md    14.3 KB    Library mapping
│
├── Research Prompts/
│   ├── PMT-048_YouTube_AI_Tools_Daily.md     8.5 KB    Daily AI search
│   ├── PMT-089_YouTube_AI_Tutorials_Research.md  9.2 KB    Tutorial search
│   ├── PMT-093_Design_AI_Video_Discovery.md  7.8 KB    Design focus
│   └── PMT-098_OpenAI_Automation_Examples.md 8.1 KB    Automation focus
│
├── Department Prompts/
│   ├── PMT-044_HR_Department.md              6.5 KB    HR research
│   ├── PMT-045_Sales_Department.md           6.8 KB    Sales research
│   ├── PMT-046_SMM_Department.md             7.2 KB    Social media
│   ├── PMT-047_Design_Department.md          7.5 KB    Design research
│   ├── PMT-048_Development_Department.md     7.8 KB    Dev research
│   ├── PMT-049_Marketing_Department.md       6.9 KB    Marketing research
│   ├── PMT-050_Operations_Department.md      6.6 KB    Ops research
│   ├── PMT-051_Finance_Department.md         6.3 KB    Finance research
│   └── PMT-052_Legal_Department.md           6.1 KB    Legal research
│
└── [40+ additional research and specialty prompts]
```

**Purpose:** Processing and research prompts for all phases

**Core Processing Prompts:**

1. **PMT-004: Video Transcription v4.1** (25.8 KB)
   - Phase: 1 (Transcription)
   - Purpose: Transform raw transcript → structured Video_XXX.md
   - Extracts: 37+ entities minimum
   - Categories: Workflows, Tools, Objects, Actions (A-G), Professions, Skills, Departments
   - Output: Fully structured markdown with cross-references
   - Processing time: 1-2 hours

2. **PMT-007: Objects Library Extraction** (18.5 KB)
   - Phase: 2 (Extraction)
   - Purpose: Deep dive into object entities
   - Focus: Digital artifacts, created objects, object properties
   - Output: Phase3_Analysis.md + Phase4_Objects.md
   - Processing time: 30-45 minutes

3. **PMT-009 Part 1: Gap Analysis** (15.2 KB)
   - Phase: 3 (Gap Analysis)
   - Purpose: Compare extracted entities vs LIBRARIES
   - Identifies: NEW (need creation), EXISTING, UPDATE (need enhancement)
   - Output: Gap_Analysis.md with coverage metrics
   - Processing time: 20-30 minutes

4. **PMT-009 Part 2: JSON Creation** (16.8 KB)
   - Phase: 4 (Integration)
   - Purpose: Create JSON files for NEW entities
   - Templates: Provides JSON structure for all entity types
   - Output: JSON files in LIBRARIES/
   - Processing time: 45-60 minutes

5. **PMT-009 Part 3: Library Mapping** (14.3 KB)
   - Phase: 5 (Mapping)
   - Purpose: Generate final integration report
   - Includes: Coverage metrics, business value, cross-references
   - Output: Library_Mapping_Report.md
   - Processing time: 30-45 minutes

**Research Prompts:**

- **PMT-048: YouTube AI Tools Daily** - Daily search for AI tool videos
- **PMT-089: YouTube AI Tutorials Research** - Tutorial-focused search
- **PMT-093: Design AI Video Discovery** - Design-specific search
- **PMT-098: OpenAI Automation Examples** - Automation-focused search

**Department-Specific Prompts (PMT-044 through PMT-052):**
Each prompt focuses research on specific department needs:
- HR: Recruitment, onboarding, performance tools
- Sales: CRM, outreach, proposal tools
- SMM: Social media management, content scheduling
- Design: Design tools, prototyping, collaboration
- Development: Coding tools, frameworks, APIs
- Marketing: Campaign management, analytics
- Operations: Process automation, project management
- Finance: Accounting, reporting, budgeting
- Legal: Contract management, compliance

---

### REPORTS/ (5+ files)

```
REPORTS/
├── Weekly_Progress_Reports/
│   ├── 2025-Week-48-Progress.md            8.5 KB     Week 48 summary
│   ├── 2025-Week-49-Progress.md            9.2 KB     Week 49 summary
│   └── [more weekly reports]
│
├── Monthly_Analytics/
│   ├── 2025-11-Analytics.md                15.8 KB    November analytics
│   └── 2025-12-Analytics.md                12.3 KB    December (partial)
│
├── Integration_Reports/
│   ├── Integration_Summary_2025-11.md      11.5 KB    November integration
│   └── Integration_Summary_2025-12.md      8.7 KB     December (partial)
│
└── System_Health_Reports/
    ├── System_Health_2025-12-01.md         7.2 KB     Health check
    └── System_Health_2025-12-04.md         7.5 KB     Current health
```

**Purpose:** System health, progress tracking, and analytics

**Weekly Progress Reports:**
```markdown
# Week 48 Progress Report (2025-11-25 to 2025-12-01)

## Videos Processed: 3
- Video_024: Webflow Workflows (Complete)
- Video_025: Make.com Automation (Complete)
- Video_026: Zapier AI Actions (In Progress)

## Entities Added: 82
- NEW Tools: 35
- NEW Workflows: 28
- NEW Objects: 19

## Coverage Improvement: +38%
- Webflow: 45% → 92%
- Make.com: 38% → 95%
- Zapier: 51% → 89%

## Time Metrics
- Average per video: 3.2 hours
- Total time: 9.6 hours
- Improvement from baseline: 62% faster

## Next Week Goals
- Complete Video_026
- Process Video_027, Video_028
- Target: 3 videos, 80+ entities
```

**Monthly Analytics:**
```markdown
# November 2025 Analytics

## Overview
- Videos processed: 8
- Total entities: 327
- Avg entities per video: 41
- Coverage improvement: +52%

## Performance Metrics
- Success rate: 97%
- Avg time per video: 3.5 hours
- Total processing time: 28 hours

## Top Categories
1. Tools: 142 entities
2. Workflows: 108 entities
3. Objects: 77 entities

## Department Impact
- Design: +35% coverage
- Development: +42% coverage
- Marketing: +28% coverage

## Trends
- Processing time decreasing: 4.2h → 3.5h
- Entity extraction improving: 38 → 41 avg
- Quality metrics stable: 95%+
```

**Report Generation:**
```bash
# Weekly report
python scripts/generate_progress_report.py weekly

# Monthly report
python scripts/generate_progress_report.py monthly

# System health
python scripts/generate_progress_report.py health
```

---

### RSR_DOCS/ (25 files)

```
RSR_DOCS/
├── RSR-001_Research_Topic.md               12.5 KB    Research doc 1
├── RSR-002_Research_Topic.md               11.8 KB    Research doc 2
├── RSR-003_Research_Topic.md               13.2 KB    Research doc 3
[... through RSR-025]
└── RSR-025_Research_Topic.md               10.9 KB    Research doc 25
```

**Purpose:** Research (RSR) entity documentation

**Tracked in:** RESEARCHES_Master_List.csv

**CSV Structure:**
```csv
RSR_ID, Topic, Date_Started, Status, Videos_Linked, Findings_Summary, Date_Completed
RSR-001, AI Design Tools, 2025-10-15, Complete, Video_001;Video_003;Video_021, [summary], 2025-11-01
```

**RSR Document Structure:**
```markdown
# RSR-001: [Research Topic]

## Metadata
- RSR ID: RSR-001
- Topic: [Topic Name]
- Date Started: YYYY-MM-DD
- Status: Complete/In Progress
- Researcher: Name

## Research Question
[Primary question being investigated]

## Methodology
- Video sources: 3
- Analysis method: [description]
- Tools used: [list]

## Findings
### Key Discovery 1
[Detailed findings]

### Key Discovery 2
[Detailed findings]

## Linked Videos
- Video_001: [Title] - [Key takeaways]
- Video_003: [Title] - [Key takeaways]

## Entities Extracted
- Tools: 15
- Workflows: 8
- Objects: 12

## Conclusions
[Summary and recommendations]

## Next Steps
[Future research directions]
```

---

### scripts/ (14 files)

```
scripts/
├── config.py                               4.8 KB     Central configuration
├── utils.py                                6.2 KB     Utility functions
├── video_id_scanner.py                     3.5 KB     Scan for video IDs
│
├── process_video.py                        15.8 KB    Master orchestrator
├── video_gap_analyzer.py                   12.3 KB    Gap analysis automation
├── video_json_updater.py                   14.6 KB    JSON file creation
├── video_integration_reporter.py           13.2 KB    Generate reports
├── update_video_progress.py                8.9 KB     Progress tracking
└── generate_progress_report.py             11.5 KB    Weekly/monthly reports
```

**Purpose:** Python automation for all workflow phases

**Configuration Files:**

1. **config.py** (4.8 KB)
```python
# Central configuration
BASE_PATH = "C:\\Users\\Dell\\Dropbox\\ENTITIES"
RESEARCHES_PATH = "TASK_MANAGERS/RESEARCHES 2"
LIBRARIES_PATH = "LIBRARIES"

# Validation rules
MIN_WORKFLOWS = 1
MIN_TOOLS = 1
MIN_ACTIONS = 3
MIN_ENTITIES = 37

# Department codes
DEPARTMENT_CODES = [
    "AID", "DEV", "VID", "SMM", "DGN",
    "MKT", "HRM", "SLS", "LG", "OPS",
    "FIN", "LGL"
]

# Priority scoring weights
PRIORITY_WEIGHTS = {
    "date": 30,
    "source": 25,
    "topic": 25,
    "engagement": 20
}
```

2. **utils.py** (6.2 KB)
```python
# Utility functions
def validate_entity_id(entity_id):
    """Validate entity ID format (e.g., TOL-001)"""

def scan_for_ids(text, entity_type):
    """Scan text for entity IDs"""

def calculate_coverage(before_count, after_count):
    """Calculate coverage improvement"""

def validate_json_structure(json_data, entity_type):
    """Validate JSON against schema"""
```

3. **video_id_scanner.py** (3.5 KB)
```python
# Scan files for video IDs
# Usage: python scripts/video_id_scanner.py
# Output: List of all video IDs found in system
```

**Processing Scripts:**

1. **process_video.py** (15.8 KB) - Master orchestrator
```bash
# Run complete workflow
python scripts/process_video.py Video_024 --all-phases

# Run specific phase
python scripts/process_video.py Video_024 --phase extraction
```

2. **video_gap_analyzer.py** (12.3 KB) - Phase 3 automation
```bash
# Run gap analysis
python scripts/video_gap_analyzer.py Video_024

# Output: 03_ANALYSIS/Gap_Analysis/Video_024_Gap_Analysis.md
```

3. **video_json_updater.py** (14.6 KB) - Phase 4 automation
```bash
# Create JSON files for NEW entities
python scripts/video_json_updater.py Video_024

# Interactive mode
python scripts/video_json_updater.py Video_024 --interactive

# Auto mode
python scripts/video_json_updater.py Video_024 --auto
```

4. **video_integration_reporter.py** (13.2 KB) - Phase 5 automation
```bash
# Generate integration report
python scripts/video_integration_reporter.py Video_024

# Include cross-references
python scripts/video_integration_reporter.py Video_024 --include-cross-refs

# Output: 03_ANALYSIS/Library_Mapping/Video_024_Library_Mapping_Report.md
```

5. **update_video_progress.py** (8.9 KB) - Progress tracking
```bash
# Add new video to tracker
python scripts/update_video_progress.py add 24 "Video Title" "URL" "Your Name"

# Update phase
python scripts/update_video_progress.py update 24 Phase_1_Transcribed "Notes"

# Mark complete
python scripts/update_video_progress.py update 24 Complete "Final notes"
```

6. **generate_progress_report.py** (11.5 KB) - Reporting
```bash
# Weekly report
python scripts/generate_progress_report.py weekly

# Monthly report
python scripts/generate_progress_report.py monthly

# System health
python scripts/generate_progress_report.py health
```

**Dependencies:**
```bash
pip install pandas requests python-dateutil yt-dlp
```

---

### TAXONOMY/ (3 files)

```
TAXONOMY/
├── Entity_Types.md                         8.5 KB     Entity definitions
├── ID_Format_Guide.md                      6.2 KB     ID assignment rules
└── Cross_Reference_Schema.md               7.8 KB     Relationship structure
```

**Purpose:** Define taxonomy structure, entity types, and cross-reference schema

**Entity_Types.md:**
```markdown
# Entity Types

## 1. TOOLS (TOL-###)
- Definition: Software, platforms, plugins, applications
- Examples: Figma, ChatGPT, Make.com
- ID Format: TOL-001, TOL-042, TOL-158

## 2. WORKFLOWS (WRF-###)
- Definition: Multi-step processes with clear start and end
- Examples: "Design System Creation", "API Integration Flow"
- ID Format: WRF-001, WRF-042, WRF-201

## 3. OBJECTS (OBJ-###)
- Definition: Digital artifacts created/manipulated
- Examples: Design file, API response, Video export
- ID Format: OBJ-001, OBJ-042, OBJ-158

## 4. ACTIONS (ACT-###)
- Definition: Atomic operations/verbs
- Categories: A (Interface), B (Content), C (Design), D (Asset), E (Collab), F (Analysis), G (Automation)
- Examples: "Create component", "Generate text", "Export file"
- ID Format: ACT-001, ACT-042, ACT-158

## 5. PROFESSIONS (PRF-###)
- Definition: Job roles/titles
- Examples: UI Designer, Full Stack Developer, Content Strategist
- ID Format: PRF-001, PRF-042

## 6. SKILLS (SKL-###)
- Definition: Competencies/abilities
- Examples: JavaScript Programming, Visual Design, Prompt Engineering
- ID Format: SKL-001, SKL-042

## 7. DEPARTMENTS (DPT-###)
- Definition: Organizational units
- Examples: Design (DGN), Development (DEV), Marketing (MKT)
- ID Format: DPT-DGN, DPT-DEV, DPT-MKT
```

**ID_Format_Guide.md:**
```markdown
# ID Format Guide

## Standard Format
[PREFIX]-[NUMBER]

PREFIX: 3 letters
NUMBER: 3 digits, zero-padded

## Examples
TOL-001  ✅ Correct
TOL-42   ❌ Wrong (needs zero-padding)
TOOL-001 ❌ Wrong (prefix too long)

## Assignment Rules
1. Sequential assignment within type
2. No gaps in numbering
3. Retired IDs not reused
4. Document all assignments

## ID Registry
Maintained in: LIBRARIES/[TYPE]/registry.json
```

**Cross_Reference_Schema.md:**
```markdown
# Cross-Reference Schema

## Bidirectional Linking
All relationships must be bidirectional:
- If Tool A creates Object B, then Object B must reference Tool A

## JSON Structure
```json
{
  "entity_id": "TOL-042",
  "name": "Figma",
  "type": "Tool",

  "creates_objects": ["OBJ-015", "OBJ-023", "OBJ-089"],
  "used_in_workflows": ["WRF-008", "WRF-042", "WRF-158"],
  "requires_skills": ["SKL-012", "SKL-034"],
  "relevant_professions": ["PRF-003", "PRF-015"],
  "relevant_departments": ["DPT-DGN", "DPT-DEV"]
}
```

## Validation
- All referenced IDs must exist
- Bidirectional links verified
- No orphaned entities
```

---

### templates/ (5+ files)

```
templates/
├── Video_Transcription_Template.md         6.5 KB     Transcription template
├── Gap_Analysis_Template.md                5.8 KB     Gap analysis template
├── Integration_Report_Template.md          7.2 KB     Integration template
│
└── JSON_Entity_Templates/
    ├── Tool_Template.json                  2.5 KB     Tool JSON structure
    ├── Workflow_Template.json              3.2 KB     Workflow JSON structure
    ├── Object_Template.json                2.8 KB     Object JSON structure
    ├── Action_Template.json                2.1 KB     Action JSON structure
    ├── Profession_Template.json            2.3 KB     Profession JSON structure
    └── Skill_Template.json                 2.0 KB     Skill JSON structure
```

**Purpose:** Templates for creating new content

**Video_Transcription_Template.md:**
```markdown
# Video_XXX: [Video Title]

## Video Metadata
- Title:
- URL:
- Channel:
- Duration:
- Upload Date:
- Processed Date:
- Processed By:
- Video ID: VID-XXX

## Video Summary
[3-5 paragraph summary]

## Pre-Categorized Entities

### WORKFLOWS (WRF-###)
1. [WRF-###] Workflow Name
   - Description:
   - Steps:
   - Tools:
   - Duration:

[Template continues...]
```

**Tool_Template.json:**
```json
{
  "entity_id": "TOL-XXX",
  "name": "Tool Name",
  "type": "Tool",
  "category": "Software|Platform|Plugin|Application",

  "description": "Detailed description of the tool",

  "features": [
    "Feature 1",
    "Feature 2"
  ],

  "use_cases": [
    "Use case 1",
    "Use case 2"
  ],

  "pricing": {
    "model": "Free|Freemium|Subscription|One-time",
    "tiers": []
  },

  "creates_objects": [],
  "used_in_workflows": [],
  "requires_skills": [],
  "relevant_professions": [],
  "relevant_departments": [],

  "metadata": {
    "source_video": "Video_XXX",
    "date_added": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "status": "Active|Deprecated"
  }
}
```

---

### documentation/ (20 files)

```
documentation/
├── v1/                                     # File-by-file analysis
│   ├── 00_MASTER_INDEX.md                 14.2 KB    Complete navigation
│   ├── 01_FOLDER_STRUCTURE.md             25.8 KB    This file
│   ├── 02_ALL_FILES_INVENTORY.md          [current file]
│   ├── 03_SEARCH_QUEUE_COMPLETE.md        (planned)
│   ├── 04_VIDEO_QUEUE_COMPLETE.md         (planned)
│   ├── 05_TRANSCRIPTIONS_COMPLETE.md      (planned)
│   ├── 06_ANALYSIS_COMPLETE.md            (planned)
│   ├── 07_INTEGRATION_COMPLETE.md         (planned)
│   ├── 08_SCRIPTS_DETAILED.md             (planned)
│   ├── 09_PROMPTS_CATALOG.md              (planned)
│   ├── 10_DATA_FILES.md                   (planned)
│   ├── 11_REPORTS_ARCHIVE.md              (planned)
│   ├── 12_QUICK_START.md                  13.5 KB    30-min guide
│   └── 13_TROUBLESHOOTING.md              (planned)
│
├── v2/                                     # Comprehensive guides
│   ├── README.md                          8.5 KB     v2 navigation
│   ├── 00_COMPLETE_SYSTEM_OVERVIEW.md     32.0 KB    System architecture
│   ├── 01_STEP_BY_STEP_WORKFLOWS.md       68.0 KB    ⭐ MAIN GUIDE
│   ├── 07_TAXONOMY_BUILDING.md            48.0 KB    Taxonomy guide
│   ├── 08_PROMPTS_REFERENCE.md            32.0 KB    All prompts
│   └── 09_SCRIPTS_REFERENCE.md            52.0 KB    All scripts
│
└── DOCUMENTATION_COMPLETE.md               12.3 KB    Documentation summary
```

**Purpose:** Complete system documentation

**v2 Documentation (230+ pages):**
- Comprehensive workflow guides
- Step-by-step instructions
- All prompts and scripts
- Taxonomy building
- Quick reference

**v1 Documentation (150+ pages planned):**
- File-by-file analysis
- Complete inventory
- Detailed breakdowns
- Troubleshooting
- Quick start

---

## 📊 File Statistics

### By Type

```
File Type             Count    Total Size    Avg Size    Purpose
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Markdown (.md)        131      3.2 MB        24.4 KB     Documentation
Python (.py)          21       0.15 MB       7.1 KB      Automation
JSON (.json)          13       0.08 MB       6.2 KB      Data storage
CSV (.csv)            3        0.008 MB      2.7 KB      Tracking
HTML (.html)          1        0.012 MB      12.5 KB     Dashboard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL                 169      3.5 MB        20.7 KB     (excluding video files)
```

### By Phase

```
Phase                 Files    Size        Primary Folder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 0: Search       5        0.05 MB     00_SEARCH_QUEUE/
Phase 0→1: Queue      10       0.12 MB     01_VIDEO_QUEUE/
Phase 1: Transcribe   30+      1.8 MB      02_TRANSCRIPTIONS/
Phase 2: Extract      5+       0.1 MB      03_ANALYSIS/Extractions/
Phase 3: Gap          5+       0.1 MB      03_ANALYSIS/Gap_Analysis/
Phase 4: Integrate    3        0.03 MB     04_INTEGRATION/
Phase 5: Map          8+       0.18 MB     03_ANALYSIS/Library_Mapping/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Support Files         100+     1.1 MB      PROMPTS, scripts, docs
```

### By Function

```
Function              Files    Purpose
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Processing            28+      Video transcriptions
Analysis              25+      Gap analysis, extraction, mapping
Automation            21       Python scripts
Prompts               50+      AI processing instructions
Documentation         20       System documentation
Tracking              6        CSV/JSON trackers
Data                  15+      Research data, metadata
Templates             5+       Content templates
Reports               5+       Progress and health reports
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL                 163      Complete system
```

---

## 🔍 File Finding Guide

### "I need to find..."

**"...a video transcription"**
→ Location: `02_TRANSCRIPTIONS/Video_XXX.md`
→ Index: `02_TRANSCRIPTIONS/Transcription_Index.md`

**"...a specific prompt"**
→ Location: `PROMPTS/PMT-XXX_Name.md`
→ Reference: `documentation/v2/08_PROMPTS_REFERENCE.md`

**"...a processing script"**
→ Location: `scripts/script_name.py`
→ Reference: `documentation/v2/09_SCRIPTS_REFERENCE.md`

**"...gap analysis for a video"**
→ Location: `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

**"...integration report for a video"**
→ Location: `03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md`

**"...video queue data"**
→ Location: `01_VIDEO_QUEUE/Video_Queue_Master.csv`
→ Dashboard: `01_VIDEO_QUEUE/Video_Queue_Dashboard.html`

**"...progress tracking"**
→ Location: `VIDEO_PROGRESS_TRACKER.csv` (root)
→ Reports: `REPORTS/Weekly_Progress_Reports/`

**"...research documents"**
→ Location: `RSR_DOCS/RSR-XXX_Topic.md`
→ Tracker: `RESEARCHES_Master_List.csv` (root)

**"...entity templates"**
→ Location: `templates/JSON_Entity_Templates/`

**"...system documentation"**
→ v2 (guides): `documentation/v2/`
→ v1 (detailed): `documentation/v1/`

---

## ✅ Files Inventory Summary

**Total Files Documented:** 163
**Total Size:** 5.1 MB
**File Types:** 5 (Markdown, Python, JSON, CSV, HTML)

**Coverage:**
- ✅ All root files
- ✅ All 15 main folders
- ✅ All subfolders
- ✅ All processing files
- ✅ All support files
- ✅ All documentation

**Documentation Status:**
- Complete file listing
- File purposes documented
- Sizes and locations recorded
- Relationships mapped
- Usage examples provided

---

*End of Complete Files Inventory*
