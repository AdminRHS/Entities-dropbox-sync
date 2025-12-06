# Research Management System - App Development Prompt
**Version:** 1.0
**Date:** 2025-11-27
**Purpose:** Comprehensive specification for building a research management application

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Overview](#system-overview)
3. [Directory Structure](#directory-structure)
4. [Data Models & Schemas](#data-models--schemas)
5. [Core Features Required](#core-features-required)
6. [7-Phase Workflow Specifications](#7-phase-workflow-specifications)
7. [Entity Relationship Mapping](#entity-relationship-mapping)
8. [Technical Requirements](#technical-requirements)
9. [User Stories & Use Cases](#user-stories--use-cases)
10. [Development Guidelines](#development-guidelines)
11. [Integration Points](#integration-points)
12. [Success Criteria](#success-criteria)

---

## Executive Summary

The Research Management System is a sophisticated 7-phase workflow for discovering, processing, analyzing, and integrating research content (primarily video transcriptions) into a comprehensive entity library ecosystem. This app will automate and streamline the management of:

- **Search Queue**: Employee-assigned video searches
- **Video Queue**: Prioritized video processing pipeline
- **Progress Tracking**: Multi-phase status monitoring (Phase 0 → Complete)
- **Analysis Workflow**: Entity extraction, gap analysis, and library mapping
- **Library Integration**: Bidirectional entity linking and JSON file creation

**Current Scale:**
- 23+ videos processed
- 50+ processing prompts
- 14 automation scripts
- 4 master CSV tracking files
- 7 distinct processing phases
- 37+ entity types per video

**Problem Statement:** Manual CSV/file management is error-prone and time-consuming. An integrated app would provide visibility, automation, and workflow orchestration across all phases.

---

## System Overview

### Purpose
Transform raw research content (YouTube videos, articles, reports) into structured, cross-referenced entities integrated with a master library ecosystem.

### Current Workflow
```
Phase 0: Search Queue
  └─> Employee searches for videos based on research topics
      └─> Videos discovered and added to queue
          └─> Phase 0→1 Transition: Video Queue Accumulation
              └─> Videos prioritized and selected for processing
                  └─> Phase 1: Transcription (PMT-004)
                      └─> Phase 2: Entity Extraction (PMT-007)
                          └─> Phase 3: Gap Analysis (PMT-009 Part 1)
                              └─> Phase 4: Integration (PMT-009 Part 2)
                                  └─> Phase 5: Library Mapping (PMT-009 Part 3)
                                      └─> Complete Status
```

### Key Stakeholders
- **Employees**: Add searches, discover videos, process content
- **VID Department**: Video research and transcription
- **AID Department**: AI tools and automation research
- **HRM Department**: Human resources workflow research
- **System Admin**: Monitor overall progress, generate reports

---

## Directory Structure

```
C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\
│
├── 00_SEARCH_QUEUE/                    # Phase 0: Video Discovery
│   ├── Search_Queue_Master.csv         # Master search tracking
│   ├── Active_Searches/                # In-progress searches
│   ├── Completed_Searches/             # Finished searches
│   └── Search_Prompts/                 # Search query templates
│
├── 01_VIDEO_QUEUE/                     # Phase 0→1 Transition
│   ├── Video_Queue_Master.csv          # Master video queue
│   ├── Video_Queue_Dashboard.html      # Interactive dashboard
│   └── scripts/                        # 6 queue management scripts
│       ├── add_to_queue.py
│       ├── update_status.py
│       ├── calculate_priority.py
│       ├── select_for_processing.py
│       ├── generate_dashboard.py
│       └── validate_queue.py
│
├── 02_TRANSCRIPTIONS/                  # Phase 1: Processing
│   ├── Video_001.md                    # Transcribed videos (23+ files)
│   ├── Video_002.md
│   └── ...Video_023.md
│
├── 03_ANALYSIS/                        # Phases 2-5: Deep Analysis
│   ├── Extractions/                    # Phase 2: Entity Extraction
│   │   ├── Video_001_Extraction.md
│   │   └── ...
│   ├── Gap_Analysis/                   # Phase 3: Gap Identification
│   │   ├── Video_001_Gap_Analysis.md
│   │   └── ...
│   ├── Library_Mapping/                # Phase 5: Final Mapping
│   │   ├── Video_001_Library_Mapping_Report.md
│   │   └── ...
│   └── Validation/                     # Quality checks
│
├── 04_INTEGRATION/                     # Phase 4: JSON Creation
│   ├── Tools/                          # Tool JSON files
│   ├── Workflows/                      # Workflow JSON files
│   ├── Objects/                        # Object JSON files
│   └── Integration_Reports/
│
├── PROMPTS/                            # 50+ Processing Prompts
│   ├── PMT-004_Video_Transcription_v4.1.md
│   ├── PMT-007_Entity_Extraction.md
│   ├── PMT-009_Taxonomy_Integration_Part1.md
│   ├── PMT-009_Taxonomy_Integration_Part2.md
│   ├── PMT-009_Taxonomy_Integration_Part3.md
│   └── PMT-048_to_052_Department_Prompts.md
│
├── DATA/                               # Metadata & Configuration
│   ├── RESEARCHES_Master_List.csv      # All research entities
│   ├── VIDEO_PROGRESS_TRACKER.csv      # Phase tracking
│   └── config.json                     # System configuration
│
├── REPORTS/                            # Analysis Reports
│   ├── Weekly_Analysis/
│   ├── Phase_Completion/
│   └── KPI_Dashboards/
│
├── TAXONOMY/                           # Entity Reference
│   ├── Action_Verbs_7_Categories.md
│   ├── Tools_Categories.md
│   └── Workflow_Patterns.md
│
├── templates/                          # Document Templates
│   ├── transcription_template.md
│   ├── extraction_template.md
│   └── mapping_template.md
│
├── ARCHIVE/                            # Historical Content
│
└── scripts/                            # 14 Total Automation Scripts
    ├── search_queue_manager.py
    ├── progress_tracker.py
    └── utilities/
```

---

## Data Models & Schemas

### 1. Search_Queue_Master.csv

**Purpose:** Track employee-assigned video search tasks

**Schema:**
```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
```

**Field Definitions:**
- `Search_ID` (string, required): Unique identifier - Format: `SEARCH-001`, `SEARCH-002`, etc.
- `Employee` (string, required): Name of employee assigned to search
- `Department` (string, required): Department requesting search (VID, AID, HRM, etc.)
- `Topic` (string, required): Research topic/area
- `Search_Query` (string, required): Exact search query used
- `Status` (enum, required): `Assigned` | `In Progress` | `Completed`
- `Videos_Found` (integer): Count of videos discovered
- `Date_Assigned` (date, required): Format: `YYYY-MM-DD`
- `Date_Completed` (date): Format: `YYYY-MM-DD`
- `Notes` (string): Additional context, findings, insights

**Validation Rules:**
- Search_ID must be unique
- Status cannot skip states (Assigned → In Progress → Completed)
- Videos_Found must be ≥ 0
- Date_Completed must be ≥ Date_Assigned

**Example Entry:**
```csv
SEARCH-001,Alice,VID,AI Video Creation Tools,ai video generation automation 2024,Completed,5,2024-01-15,2024-01-16,Found GLIF tutorial and 4 related videos
```

---

### 2. Video_Queue_Master.csv

**Purpose:** Manage video processing queue with priority and metadata

**Schema:**
```csv
Queue_ID,Video_ID,Video_Title,Channel_Name,Channel_URL,Video_URL,Views,Likes,Comments,Publish_Date,Duration,Added_By,Added_Date,Status,Selected_By,Selected_Date,Topic_Category,Research_Source,Priority_Score,Notes
```

**Field Definitions:**
- `Queue_ID` (string, required): Unique identifier - Format: `VQ-001`, `VQ-002`, etc.
- `Video_ID` (string, required): YouTube video ID (11 characters)
- `Video_Title` (string, required): Full video title
- `Channel_Name` (string, required): YouTube channel name
- `Channel_URL` (string): Full channel URL
- `Video_URL` (string, required): Full video URL
- `Views` (integer): View count at time of addition
- `Likes` (integer): Like count at time of addition
- `Comments` (integer): Comment count at time of addition
- `Publish_Date` (date): Video publication date - Format: `YYYY-MM-DD`
- `Duration` (string): Video length - Format: `HH:MM:SS` or `MM:SS`
- `Added_By` (string, required): Employee who added video
- `Added_Date` (date, required): Date added to queue - Format: `YYYY-MM-DD`
- `Status` (enum, required): `Pending` | `Selected` | `Parsed` | `Completed`
- `Selected_By` (string): Employee who selected for processing
- `Selected_Date` (date): Date selected - Format: `YYYY-MM-DD`
- `Topic_Category` (string): Primary topic (AI Tools, Workflows, Automation, etc.)
- `Research_Source` (string): Source of discovery (Perplexity, YouTube, Gemini, Manual, etc.)
- `Priority_Score` (integer): Calculated priority 0-100
- `Notes` (string): Additional metadata, tags, context

**Validation Rules:**
- Queue_ID must be unique
- Video_ID must be 11 characters
- Status progression: Pending → Selected → Parsed → Completed
- Priority_Score range: 0-100
- Selected_Date must be ≥ Added_Date
- Video_URL must contain valid YouTube URL format

**Priority Calculation Formula:**
```
Priority_Score = (
    (Views / 1000000) * 30 +        # Max 30 points for views
    (Likes / 10000) * 20 +          # Max 20 points for engagement
    Recency_Score * 25 +             # Max 25 points for publish date
    Topic_Relevance * 25             # Max 25 points for topic match
)
```

**Example Entry:**
```csv
VQ-001,dQw4w9WgXcQ,How To Use AI Agents to 10x Your Creative AI Game,Tech Channel,https://youtube.com/@techchannel,https://youtube.com/watch?v=dQw4w9WgXcQ,150000,5200,340,2024-01-10,15:32,Alice,2024-01-16,Selected,Bob,2024-01-17,AI Automation,Perplexity,85,High priority - covers GLIF and multiple AI tools
```

---

### 3. VIDEO_PROGRESS_TRACKER.csv

**Purpose:** Track each video through all 7 processing phases

**Schema:**
```csv
Video_ID,Phase_0_Search,Phase_1_Transcribed,Phase_2_Extraction,Phase_3_Gap_Analysis,Phase_4_Integration,Phase_5_Mapping,Complete,Last_Updated,Notes
```

**Field Definitions:**
- `Video_ID` (integer, required): Numeric video identifier (1, 2, 3, etc.)
- `Phase_0_Search` (enum): `Not Started` | `In Progress` | `Complete`
- `Phase_1_Transcribed` (enum): `Not Started` | `In Progress` | `Complete`
- `Phase_2_Extraction` (enum): `Not Started` | `In Progress` | `Complete`
- `Phase_3_Gap_Analysis` (enum): `Not Started` | `In Progress` | `Complete`
- `Phase_4_Integration` (enum): `Not Started` | `In Progress` | `Complete`
- `Phase_5_Mapping` (enum): `Not Started` | `In Progress` | `Complete`
- `Complete` (boolean): `true` | `false`
- `Last_Updated` (datetime, required): Format: `YYYY-MM-DD HH:MM:SS`
- `Notes` (string): Current status, blockers, next steps

**Validation Rules:**
- Video_ID must match a Video_ID in Video_Queue_Master.csv
- Phases must progress sequentially (cannot skip phases)
- Complete = true only when all phases = Complete
- Last_Updated must update on any status change

**Example Entry:**
```csv
1,Complete,Complete,Complete,Complete,In Progress,Not Started,false,2024-01-20 14:30:00,Integration of 7 new tools in progress
```

---

### 4. RESEARCHES_Master_List.csv

**Purpose:** Central registry of all research entities

**Schema:**
```csv
RSR_ID,Name,Description,Department,Category,File_Path,Status
```

**Field Definitions:**
- `RSR_ID` (string, required): Unique identifier - Format: `RSR-001`, `RSR-002`, etc.
- `Name` (string, required): Descriptive title of research
- `Description` (string): Brief summary of content
- `Department` (string, required): Owning department (VID, AID, HRM, etc.)
- `Category` (enum, required): `Video_Transcription` | `Research_Report` | `Analysis` | `Documentation`
- `File_Path` (string, required): Relative path from RESEARCHES/ root
- `Status` (enum, required): `Active` | `Archive` | `In Progress`

**Validation Rules:**
- RSR_ID must be unique
- File_Path must point to existing file
- Sequential numbering (RSR-001, RSR-002, RSR-003...)

**Example Entry:**
```csv
RSR-001,GLIF AI Agents Tutorial,Video transcription covering GLIF platform and AI workflow automation,VID,Video_Transcription,02_TRANSCRIPTIONS/Video_001.md,Active
```

---

### 5. Transcription File Format (Video_XXX.md)

**Purpose:** Standardized markdown format for video transcriptions with pre-categorized entities

**Template Structure:**
```markdown
# Video Title

## Video Metadata
- **Video ID**: [YouTube ID]
- **Channel**: [Channel Name]
- **URL**: [Full URL]
- **Duration**: [HH:MM:SS]
- **Published**: [YYYY-MM-DD]
- **Transcribed By**: [Employee Name]
- **Transcription Date**: [YYYY-MM-DD]

## Video Description
[Full video description from YouTube]

## Links Referenced
- [Link 1]
- [Link 2]

## Timestamps
- 00:00 - Introduction
- 01:30 - Topic 1
- 05:45 - Topic 2
...

## Video Content Transcription
[Full verbatim or cleaned transcription]

## Taxonomy Analysis

### Tools & Technologies Identified
| Tool Name | Category | Context Used | Tool ID |
|-----------|----------|--------------|---------|
| GLIF | AI Workflow Platform | Create automated AI agent workflows | TOOL-AI-045 |
| Sora | Video Generation | Generate videos from text prompts | TOOL-NEW-001 |

### Actions/Verbs Identified
| Action | Category | Context |
|--------|----------|---------|
| Create | Creation | Create AI workflows |
| Generate | Generation | Generate video content |
| Automate | Automation | Automate content creation |

### Objects/Deliverables Identified
| Object | Category | Context |
|--------|----------|---------|
| Workflow | Digital Asset | AI agent workflow configuration |
| Thumbnail | Visual Asset | YouTube thumbnail image |

### Workflows Identified
| Workflow Name | Description | Steps | Workflow ID |
|---------------|-------------|-------|-------------|
| AI Thumbnail Generator | Automated thumbnail creation using AI | 1. Input prompt 2. Generate image 3. Apply style 4. Export | WRF-012 |

### Skills/Competencies Required
- Prompt Engineering
- Workflow Design
- AI Tool Selection

### Professions/Roles
- Content Creator
- AI Workflow Designer
- Digital Marketer

### Integration Patterns
- Multi-tool orchestration (GLIF → Sora → Output)
- Prompt chaining workflows
- Template-based generation

### Task Chains
1. Research topic → 2. Create prompt → 3. Generate with AI → 4. Refine output → 5. Export final

## Summary Statistics
- **Tools Identified**: 7
- **Workflows Extracted**: 3
- **Actions Categorized**: 15
- **Objects Documented**: 8
- **Integration Patterns**: 5
```

---

## Core Features Required

### Feature 1: Search Queue Management

**Purpose:** Enable employees to assign, track, and complete video search tasks

**Key Functions:**
1. Create new search assignment
2. View active searches (list/grid view)
3. Update search status
4. Record videos found
5. Mark search as complete
6. View search history

**UI Components:**
- Search assignment form (Employee, Department, Topic, Query)
- Active searches table (sortable, filterable)
- Search detail view
- Completion form (Videos found, Notes)

**Data Operations:**
- CREATE: New search entry in Search_Queue_Master.csv
- READ: Display searches filtered by status/employee/department
- UPDATE: Status transitions, video count, completion date
- DELETE: Archive completed searches (move to Completed_Searches/)

**Validation:**
- Required fields: Search_ID, Employee, Department, Topic, Search_Query, Status, Date_Assigned
- Search_ID uniqueness check
- Status progression enforcement
- Date validation (Completed ≥ Assigned)

---

### Feature 2: Video Queue Management

**Purpose:** Manage video pipeline from discovery to completion

**Key Functions:**
1. Add video to queue (manual or batch import)
2. View queue with priority sorting
3. Calculate/recalculate priority scores
4. Select videos for processing
5. Update video status
6. Track video metadata changes
7. Export queue data

**UI Components:**
- Add video form (URL, metadata fields)
- Queue table with columns: Queue_ID, Title, Channel, Priority, Status, Added Date
- Priority calculator widget
- Batch import interface (CSV upload)
- Video detail panel (metadata, status history, notes)
- Filter/search bar (by status, topic, date range)
- Interactive dashboard (HTML view with charts)

**Data Operations:**
- CREATE: New video entry with metadata
- READ: Queue display with sorting/filtering
- UPDATE: Status changes, priority recalculation, selection
- CALCULATE: Priority score based on formula
- EXPORT: Generate Video_Queue_Dashboard.html

**Validation:**
- YouTube URL validation
- Video_ID extraction and uniqueness check
- Priority score range (0-100)
- Status progression: Pending → Selected → Parsed → Completed
- Required fields enforcement

**Priority Calculation:**
```python
def calculate_priority(views, likes, publish_date, topic_relevance):
    view_score = min((views / 1000000) * 30, 30)
    engagement_score = min((likes / 10000) * 20, 20)

    days_old = (today - publish_date).days
    if days_old <= 30:
        recency_score = 25
    elif days_old <= 90:
        recency_score = 20
    elif days_old <= 180:
        recency_score = 15
    else:
        recency_score = 10

    relevance_score = topic_relevance * 25  # 0-1 scale

    return view_score + engagement_score + recency_score + relevance_score
```

---

### Feature 3: Progress Tracking Dashboard

**Purpose:** Real-time visibility into video processing across all phases

**Key Functions:**
1. View all videos and their phase status
2. Update phase completion
3. Identify bottlenecks
4. Generate progress reports
5. File integrity checking
6. Status history tracking

**UI Components:**
- Phase progression board (Kanban-style or table)
- Video detail modal (all phases, dates, notes)
- Phase status update form
- Progress charts (phase completion percentages, time in phase)
- Bottleneck alerts
- KPI cards (Total videos, Completed, In progress, Avg time per phase)

**Data Operations:**
- READ: VIDEO_PROGRESS_TRACKER.csv + Video_Queue_Master.csv (joined view)
- UPDATE: Phase status changes with timestamp
- VALIDATE: File existence checks (02_TRANSCRIPTIONS/Video_XXX.md)
- REPORT: Generate weekly progress summaries

**KPIs to Display:**
- Total videos processed
- Videos per phase (breakdown)
- Completion rate (%)
- Average time per phase
- Bottleneck identification (phase with most In Progress)
- Processing velocity (videos/week)

**Phase Transition Rules:**
- Phase 0 → Phase 1: Video selected from queue
- Phase 1 → Phase 2: Transcription file exists (Video_XXX.md)
- Phase 2 → Phase 3: Extraction report exists
- Phase 3 → Phase 4: Gap analysis complete
- Phase 4 → Phase 5: JSON files created
- Phase 5 → Complete: Library mapping report complete

---

### Feature 4: Analysis Workflow Automation

**Purpose:** Streamline entity extraction, gap analysis, and mapping

**Key Functions:**
1. Trigger extraction analysis (Phase 2)
2. Run gap analysis against existing libraries (Phase 3)
3. Generate library mapping reports (Phase 5)
4. Track analysis completeness
5. Export analysis results

**UI Components:**
- Analysis trigger panel (select video, select phase)
- Extraction results viewer (tables of entities found)
- Gap analysis dashboard (new vs existing entities)
- Priority assignment interface (CRITICAL, HIGH, MEDIUM, LOW)
- Mapping report generator

**Data Operations:**
- READ: Transcription files (Video_XXX.md)
- READ: Existing library files (ENTITIES/LIBRARIES/)
- WRITE: Analysis reports (03_ANALYSIS/Extractions/, Gap_Analysis/, Library_Mapping/)
- COMPARE: Extracted entities vs existing library entries
- GENERATE: Structured markdown reports

**Analysis Outputs:**

**Phase 2 - Extraction Report:**
```markdown
# Video_XXX_Extraction.md

## Executive Summary
- Total Entities Extracted: 47
- Tools: 12
- Workflows: 5
- Actions: 18
- Objects: 8
- Skills: 4

## Detailed Extraction

### Tools Extracted
| Tool Name | Category | Context | Existing in Library? |
|-----------|----------|---------|---------------------|
| GLIF | AI Platform | Workflow automation | No - NEW |
| Sora | Video Gen | Text-to-video | Yes - TOOL-AI-023 |

### Workflows Extracted
...

## Cross-References Identified
- GLIF integrates with Sora (TOOL-AI-023)
- Workflow WRF-012 uses GLIF + Sora combination
```

**Phase 3 - Gap Analysis:**
```markdown
# Video_XXX_Gap_Analysis.md

## Coverage Analysis
- Existing Coverage: 40%
- New Entities: 28 (60%)
- Enhanced Entities: 7 (existing entries to update)

## Priority Distribution
- CRITICAL: 5 (core tools, high impact)
- HIGH: 12 (important workflows)
- MEDIUM: 8 (supporting tools)
- LOW: 3 (minor objects)

## Library Gaps by Type
### Tools Gap
- Missing: 12 tools
- Priority: 5 CRITICAL, 4 HIGH, 3 MEDIUM

### Workflows Gap
- Missing: 5 workflows
- Priority: 2 CRITICAL, 2 HIGH, 1 MEDIUM

## Integration Requirements
- JSON files needed: 17
- Cross-references to create: 23
- Existing entries to enhance: 7
```

---

### Feature 5: Library Integration Engine

**Purpose:** Create and integrate new entities into ENTITIES ecosystem

**Key Functions:**
1. Generate JSON files for new entities
2. Update ENTITIES_MASTER_LIST.csv
3. Create bidirectional cross-references
4. Move files to ENTITIES/LIBRARIES/
5. Validate integration completeness
6. Generate mapping reports

**UI Components:**
- Entity creation form (Tool/Workflow/Object)
- JSON template editor
- Cross-reference mapper
- Integration validation dashboard
- File move/copy interface
- Mapping report viewer

**Data Operations:**
- CREATE: New JSON files in 04_INTEGRATION/
- MOVE: JSON files to ENTITIES/LIBRARIES/[category]/
- UPDATE: ENTITIES_MASTER_LIST.csv with new entries
- VALIDATE: Bidirectional link verification
- WRITE: Library_Mapping/ reports

**JSON File Template (Tool):**
```json
{
  "id": "TOOL-AI-045",
  "name": "GLIF",
  "category": "AI_Tools",
  "subcategory": "Workflow_Automation",
  "description": "AI-powered workflow automation platform for creating agent-based content generation pipelines",
  "use_cases": [
    "YouTube thumbnail generation",
    "Automated video creation",
    "Multi-tool orchestration"
  ],
  "integrations": [
    "TOOL-AI-023 (Sora)",
    "TOOL-AI-067 (Kling)"
  ],
  "workflows": [
    "WRF-012"
  ],
  "skills_required": [
    "Prompt Engineering",
    "Workflow Design"
  ],
  "url": "https://glif.app",
  "discovered_in": "RSR-001",
  "priority": "CRITICAL",
  "date_added": "2024-01-20"
}
```

**Integration Checklist:**
- [ ] JSON file created with all required fields
- [ ] Entity ID assigned (TOOL-XXX, WRF-XXX, OBJ-XXX)
- [ ] Cross-references added (bidirectional)
- [ ] File moved to correct ENTITIES/LIBRARIES/ subdirectory
- [ ] ENTITIES_MASTER_LIST.csv updated
- [ ] Mapping report generated
- [ ] Video progress updated to Phase 5 Complete

---

### Feature 6: Dashboard & Reporting

**Purpose:** Comprehensive visibility into system performance and progress

**Key Dashboards:**

**1. Overview Dashboard**
- KPI cards: Total videos, Completed, In progress, Processing velocity
- Phase distribution chart (pie/bar)
- Weekly progress trend (line chart)
- Recent activity feed
- Bottleneck alerts

**2. Search Queue Dashboard**
- Active searches table
- Searches by employee (bar chart)
- Videos discovered per search (stats)
- Completion rate by department

**3. Video Queue Dashboard**
- Queue size over time (line chart)
- Priority distribution (histogram)
- Status breakdown (pie chart)
- Top channels (bar chart)
- Topic category distribution

**4. Progress Tracking Dashboard**
- Phase progression board (Kanban)
- Time-in-phase analysis (box plot)
- Completion funnel (funnel chart)
- Phase-by-phase throughput

**5. Library Integration Dashboard**
- Entities added over time (line chart)
- Entity type distribution (pie chart)
- Coverage improvement tracking
- Integration completeness (%)

**Report Types:**
- Weekly progress report (PDF/MD)
- Phase completion report
- Library growth report
- Employee contribution report
- KPI summary report

---

## 7-Phase Workflow Specifications

### Phase 0: Search Queue

**Objective:** Discover and collect relevant video content

**Inputs:**
- Research topic from weekly reports
- Department requirements
- Search query templates

**Process:**
1. Employee receives search assignment
2. Conducts search using specified query
3. Evaluates video relevance
4. Adds qualifying videos to Video Queue
5. Records search completion

**Outputs:**
- Updated Search_Queue_Master.csv
- New entries in Video_Queue_Master.csv
- Search completion notes

**Success Criteria:**
- 3-10 videos found per search
- Videos match topic requirements
- Metadata captured completely

**Automation Opportunities:**
- Auto-generate search queries based on topics
- Batch video metadata scraping
- Duplicate detection

---

### Phase 0→1 Transition: Video Queue Accumulation

**Objective:** Accumulate and prioritize videos before processing

**Inputs:**
- Videos from multiple searches
- Video metadata (views, likes, date)
- Topic relevance scores

**Process:**
1. Videos enter queue with "Pending" status
2. Priority scores calculated automatically
3. Queue reviewed periodically
4. High-priority videos selected for processing
5. Status updated to "Selected"

**Outputs:**
- Prioritized Video_Queue_Master.csv
- Selected videos ready for Phase 1
- Video_Queue_Dashboard.html updated

**Success Criteria:**
- Priority scores accurate
- Queue size manageable (20-50 videos)
- High-value videos identified

**Selection Criteria:**
- Priority score > 70 = Auto-select
- Priority score 50-70 = Manual review
- Priority score < 50 = Backlog

---

### Phase 1: Transcription

**Objective:** Create full transcription with pre-categorized entities

**Inputs:**
- Selected video (Status = "Selected")
- Video URL and metadata
- PMT-004 prompt (Video Transcription v4.1)

**Process:**
1. Video selected from queue
2. PMT-004 prompt applied to video
3. Full transcription generated
4. Entities pre-categorized (37+ types)
5. Markdown file created (Video_XXX.md)
6. File saved to 02_TRANSCRIPTIONS/

**Outputs:**
- Video_XXX.md file (structured markdown)
- Taxonomy analysis tables
- Summary statistics

**Prompt Used:** PMT-004

**Quality Checks:**
- Transcription accuracy > 95%
- All metadata sections completed
- Minimum 10 entities identified
- Taxonomy tables formatted correctly

**Time Estimate:** 1-2 hours per video

**Automation:** Use AI transcription API + PMT-004 for entity extraction

---

### Phase 2: Entity Extraction

**Objective:** Deep entity extraction and cross-referencing

**Inputs:**
- Video_XXX.md transcription
- PMT-007 prompt (Entity Extraction & Cross-Referencing)
- Existing ENTITIES/LIBRARIES/ files

**Process:**
1. Read Video_XXX.md
2. Apply PMT-007 for deep extraction
3. Identify all entity types (Tools, Workflows, Actions, Objects, Skills, Professions)
4. Cross-reference against existing library
5. Tag new vs existing entities
6. Generate extraction report

**Outputs:**
- 03_ANALYSIS/Extractions/Video_XXX_Extraction.md
- Entity lists with existence status
- Cross-reference mappings

**Prompt Used:** PMT-007

**Quality Checks:**
- Minimum 20 entities extracted
- All 37+ entity types considered
- Cross-reference accuracy validated
- New entities clearly marked

**Time Estimate:** 2-3 hours per video

---

### Phase 3: Gap Analysis

**Objective:** Compare extracted entities against existing libraries and prioritize

**Inputs:**
- Video_XXX_Extraction.md
- ENTITIES/LIBRARIES/ (all existing JSON files)
- ENTITIES_MASTER_LIST.csv
- PMT-009 Part 1 prompt

**Process:**
1. Read extraction report
2. Load all existing library files
3. Compare extracted vs existing (entity matching)
4. Calculate coverage percentage
5. Assign priorities (CRITICAL, HIGH, MEDIUM, LOW)
6. Identify integration requirements
7. Generate gap analysis report

**Outputs:**
- 03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md
- Coverage statistics
- Priority assignments
- Integration checklist

**Prompt Used:** PMT-009 Part 1 (Taxonomy Integration - Gap Analysis)

**Priority Assignment Criteria:**
- **CRITICAL**: Core tools/workflows, high frequency, unique capability
- **HIGH**: Important supporting tools, commonly used workflows
- **MEDIUM**: Useful but not essential entities
- **LOW**: Minor objects, one-off mentions

**Quality Checks:**
- Coverage calculation accurate
- Priorities justified
- All new entities assigned priority
- Integration requirements complete

**Time Estimate:** 1-2 hours per video

---

### Phase 4: Integration

**Objective:** Create JSON files and integrate into ENTITIES ecosystem

**Inputs:**
- Video_XXX_Gap_Analysis.md
- Entity templates (JSON)
- PMT-009 Part 2 prompt
- ENTITIES/LIBRARIES/ directory structure

**Process:**
1. Read gap analysis report
2. For each CRITICAL/HIGH entity:
   a. Create JSON file from template
   b. Populate all required fields
   c. Add cross-references
   d. Validate JSON structure
3. Save to 04_INTEGRATION/[category]/
4. Update ENTITIES_MASTER_LIST.csv
5. Create bidirectional links

**Outputs:**
- New JSON files in 04_INTEGRATION/
- Updated ENTITIES_MASTER_LIST.csv
- Integration log

**Prompt Used:** PMT-009 Part 2 (Taxonomy Integration - JSON Creation)

**JSON Validation:**
- Required fields present
- ID format correct (TOOL-XXX, WRF-XXX, etc.)
- Cross-references valid
- No duplicate IDs

**Quality Checks:**
- All CRITICAL entities have JSON files
- Bidirectional links verified
- File naming conventions followed
- Master list updated correctly

**Time Estimate:** 3-4 hours per video (most time-consuming phase)

**Automation Opportunities:**
- JSON template auto-population
- Cross-reference auto-linking
- Duplicate ID detection

---

### Phase 5: Library Mapping

**Objective:** Move files to final locations and document integration

**Inputs:**
- JSON files from 04_INTEGRATION/
- PMT-009 Part 3 prompt
- ENTITIES/LIBRARIES/ target directories

**Process:**
1. Validate all JSON files ready for integration
2. Move files to ENTITIES/LIBRARIES/[category]/
3. Verify file placements
4. Update cross-references in existing files (bidirectional)
5. Generate library mapping report
6. Document coverage improvements

**Outputs:**
- JSON files in ENTITIES/LIBRARIES/
- 03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md
- Updated existing library files (cross-refs)

**Prompt Used:** PMT-009 Part 3 (Taxonomy Integration - Library Mapping)

**Mapping Report Contents:**
- Video overview
- Entities integrated (count by type)
- New library entries created (file paths)
- Existing entries enhanced
- Coverage improvements (before/after %)
- Cross-reference summary
- Integration completion confirmation

**Quality Checks:**
- All files moved correctly
- No broken links
- Coverage improvement documented
- Bidirectional links functional

**Time Estimate:** 1-2 hours per video

---

### Complete Status

**Criteria for Completion:**
- All phases 0-5 marked "Complete" in VIDEO_PROGRESS_TRACKER.csv
- All files exist and validated:
  - 02_TRANSCRIPTIONS/Video_XXX.md
  - 03_ANALYSIS/Extractions/Video_XXX_Extraction.md
  - 03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md
  - 03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md
  - 04_INTEGRATION/ files moved to ENTITIES/LIBRARIES/
- ENTITIES_MASTER_LIST.csv updated
- Video_Queue_Master.csv status = "Completed"

**Final Deliverables:**
- Complete research package (transcription + analysis)
- Integrated library entries (JSON files)
- Documentation (mapping report)
- Updated master lists

---

## Entity Relationship Mapping

### Core Entity Types

**1. Research Entity (RSR-###)**
```
RSR-001
  ├─ Has: Video transcription file (Video_001.md)
  ├─ Produces: Analysis files (Extraction, Gap, Mapping)
  ├─ Creates: Library entries (Tools, Workflows, Objects)
  ├─ Tracked in: RESEARCHES_Master_List.csv
  └─ Progress in: VIDEO_PROGRESS_TRACKER.csv
```

**2. Video Entity (VQ-###)**
```
VQ-001
  ├─ Sourced from: Search (SEARCH-001)
  ├─ Added by: Employee
  ├─ Has: Metadata (title, channel, views, priority)
  ├─ Status: Pending → Selected → Parsed → Completed
  ├─ Becomes: Video_001.md (transcription)
  └─ Tracked in: Video_Queue_Master.csv
```

**3. Search Entity (SEARCH-###)**
```
SEARCH-001
  ├─ Assigned to: Employee
  ├─ Requested by: Department
  ├─ Discovers: Videos (VQ-001, VQ-002, etc.)
  ├─ Status: Assigned → In Progress → Completed
  └─ Tracked in: Search_Queue_Master.csv
```

**4. Tool Entity (TOOL-XXX / TOL-XXX)**
```
TOOL-AI-045 (GLIF)
  ├─ Discovered in: RSR-001 (Video_001)
  ├─ Category: AI_Tools / Workflow_Automation
  ├─ Used in: Workflows (WRF-012)
  ├─ Integrates with: Other tools (TOOL-AI-023)
  ├─ Requires: Skills (Prompt Engineering)
  ├─ JSON file: ENTITIES/LIBRARIES/Tools/AI_Tools/GLIF.json
  └─ Listed in: ENTITIES_MASTER_LIST.csv
```

**5. Workflow Entity (WRF-###)**
```
WRF-012 (AI Thumbnail Generator)
  ├─ Discovered in: RSR-001
  ├─ Uses: Tools (TOOL-AI-045, TOOL-AI-023)
  ├─ Includes: Actions (Create, Generate, Automate)
  ├─ Produces: Objects (Thumbnails)
  ├─ Requires: Skills (Workflow Design)
  ├─ JSON file: ENTITIES/TASK_MANAGERS/TSM-006_Workflows/WRF-012.json
  └─ Listed in: ENTITIES_MASTER_LIST.csv
```

**6. Object Entity (OBJ-###)**
```
OBJ-015 (Thumbnail)
  ├─ Created by: Workflows (WRF-012)
  ├─ Uses: Tools (TOOL-AI-045)
  ├─ Category: Visual_Asset
  ├─ JSON file: ENTITIES/LIBRARIES/Responsibilities/Objects/Thumbnail.json
  └─ Listed in: ENTITIES_MASTER_LIST.csv
```

### Relationship Types

**1. Discovery Relationships**
```
Search (SEARCH-001)
  └─> discovers → Video (VQ-001)
      └─> becomes → Transcription (Video_001.md)
          └─> contains → Entities (Tools, Workflows, Objects)
              └─> integrated as → Library Files (JSON)
```

**2. Bidirectional Cross-References**
```
Tool (TOOL-AI-045)
  ├─> integrates_with → Tool (TOOL-AI-023)
  └─< integrated_by ─┘

Workflow (WRF-012)
  ├─> uses_tool → Tool (TOOL-AI-045)
  └─< used_in_workflow ─┘

Workflow (WRF-012)
  ├─> produces_object → Object (OBJ-015)
  └─< produced_by_workflow ─┘
```

**3. Hierarchical Relationships**
```
Department (VID)
  └─> requests → Search (SEARCH-001)
      └─> assigns_to → Employee
          └─> discovers → Videos
              └─> processes_into → Research (RSR-001)
                  └─> creates → Library Entries
```

**4. Progress Tracking Relationships**
```
Video (VQ-001)
  ├─> tracked_in → VIDEO_PROGRESS_TRACKER.csv (row 1)
  ├─> documented_in → RESEARCHES_Master_List.csv (RSR-001)
  └─> files:
      ├─ 02_TRANSCRIPTIONS/Video_001.md
      ├─ 03_ANALYSIS/Extractions/Video_001_Extraction.md
      ├─ 03_ANALYSIS/Gap_Analysis/Video_001_Gap_Analysis.md
      └─ 03_ANALYSIS/Library_Mapping/Video_001_Library_Mapping_Report.md
```

### Data Flow Diagram

```
┌─────────────────┐
│ Search Queue    │
│ (SEARCH-001)    │
└────────┬────────┘
         │ discovers
         ▼
┌─────────────────┐
│ Video Queue     │
│ (VQ-001)        │
└────────┬────────┘
         │ selected
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Phase 1         │─────>│ Video_001.md     │
│ Transcription   │      │ (02_TRANS...)    │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Phase 2         │─────>│ Extraction.md    │
│ Extraction      │      │ (03_ANALYSIS...) │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Phase 3         │─────>│ Gap_Analysis.md  │
│ Gap Analysis    │      │ (03_ANALYSIS...) │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Phase 4         │─────>│ JSON Files       │
│ Integration     │      │ (04_INTEGRAT...) │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Phase 5         │─────>│ LIBRARIES/       │
│ Library Mapping │      │ (ENTITIES/...)   │
└────────┬────────┘      └──────────────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Complete        │─────>│ Master Lists     │
│ Status          │      │ Updated          │
└─────────────────┘      └──────────────────┘
```

---

## Technical Requirements

### Tech Stack Recommendations

**Backend:**
- **Language**: Python 3.10+
- **Framework**: FastAPI or Flask (REST API)
- **Data Processing**: pandas (CSV), PyYAML (config), json (library files)
- **File Operations**: pathlib, os
- **Web Scraping**: yt-dlp (YouTube metadata), BeautifulSoup4
- **Task Queue**: Celery (for long-running processes)
- **Database**: SQLite (local) or PostgreSQL (production)

**Frontend:**
- **Framework**: React 18+ or Vue.js 3+
- **UI Library**: Material-UI or Ant Design
- **Data Grid**: AG-Grid or TanStack Table
- **Charts**: Chart.js or Recharts
- **File Upload**: react-dropzone
- **State Management**: Redux Toolkit or Zustand

**Desktop App (Optional):**
- **Electron**: Package as desktop app for Windows/Mac
- **Tauri**: Lightweight alternative to Electron

**DevOps:**
- **Version Control**: Git
- **Environment**: Docker (containerization)
- **CI/CD**: GitHub Actions
- **Testing**: pytest (backend), Jest (frontend)

---

### System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Frontend (React)                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │ Dashboard   │  │ Queue Mgmt  │  │ Progress    │ │
│  │ Component   │  │ Component   │  │ Tracker     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
└────────────────────────┬────────────────────────────┘
                         │ HTTP/REST
                         ▼
┌─────────────────────────────────────────────────────┐
│                  Backend API (FastAPI)               │
│  ┌──────────────────────────────────────────────┐  │
│  │           API Endpoints                       │  │
│  │  /search-queue  /video-queue  /progress      │  │
│  │  /analysis  /integration  /reports           │  │
│  └──────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────┐  │
│  │         Business Logic Layer                  │  │
│  │  - Queue Manager  - Progress Tracker         │  │
│  │  - Priority Calculator  - Validator          │  │
│  │  - Analysis Engine  - Report Generator       │  │
│  └──────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│              Data Access Layer (DAL)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │ CSV Handler  │  │ MD Handler   │  │ JSON      │ │
│  │              │  │              │  │ Handler   │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
└────────────────────────┬────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│                 File System                          │
│  C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\      │
│  RESEARCHES\                                         │
│    - Search_Queue_Master.csv                        │
│    - Video_Queue_Master.csv                         │
│    - VIDEO_PROGRESS_TRACKER.csv                     │
│    - 02_TRANSCRIPTIONS/                             │
│    - 03_ANALYSIS/                                   │
│    - etc.                                           │
└─────────────────────────────────────────────────────┘
```

---

### API Endpoints Specification

**Search Queue Endpoints:**
```
POST   /api/search-queue              # Create new search
GET    /api/search-queue              # List all searches
GET    /api/search-queue/{id}         # Get search details
PUT    /api/search-queue/{id}         # Update search
DELETE /api/search-queue/{id}         # Archive search
GET    /api/search-queue/stats        # Get statistics
```

**Video Queue Endpoints:**
```
POST   /api/video-queue               # Add video to queue
GET    /api/video-queue               # List all videos (with filters)
GET    /api/video-queue/{id}          # Get video details
PUT    /api/video-queue/{id}          # Update video
DELETE /api/video-queue/{id}          # Remove from queue
POST   /api/video-queue/{id}/select   # Select for processing
PUT    /api/video-queue/{id}/priority # Recalculate priority
POST   /api/video-queue/batch         # Batch import videos
GET    /api/video-queue/dashboard     # Generate dashboard HTML
```

**Progress Tracking Endpoints:**
```
GET    /api/progress                  # Get all video progress
GET    /api/progress/{video_id}       # Get specific video progress
PUT    /api/progress/{video_id}       # Update phase status
POST   /api/progress/{video_id}/phase # Advance to next phase
GET    /api/progress/stats            # Get KPIs and statistics
GET    /api/progress/bottlenecks      # Identify bottlenecks
```

**Analysis Endpoints:**
```
POST   /api/analysis/extract/{video_id}     # Trigger extraction (Phase 2)
POST   /api/analysis/gap/{video_id}         # Run gap analysis (Phase 3)
GET    /api/analysis/reports/{video_id}     # Get analysis reports
GET    /api/analysis/entities/{video_id}    # Get extracted entities
```

**Integration Endpoints:**
```
POST   /api/integration/create-json/{video_id}   # Create JSON files (Phase 4)
POST   /api/integration/map/{video_id}           # Library mapping (Phase 5)
GET    /api/integration/validate/{video_id}      # Validate integration
POST   /api/integration/move-files/{video_id}    # Move to ENTITIES/
```

**Report Endpoints:**
```
GET    /api/reports/weekly            # Generate weekly report
GET    /api/reports/phase/{phase_num} # Phase completion report
GET    /api/reports/library-growth    # Library growth report
GET    /api/reports/kpi               # KPI summary
POST   /api/reports/export            # Export report (PDF/CSV)
```

**Utility Endpoints:**
```
GET    /api/health                    # Health check
GET    /api/config                    # Get configuration
POST   /api/validate-files            # File integrity check
GET    /api/search-prompts            # Get search prompt templates
```

---

### File Operations Specifications

**CSV File Handling:**

**Read Operations:**
```python
import pandas as pd

def read_search_queue():
    """Read Search_Queue_Master.csv"""
    df = pd.read_csv('00_SEARCH_QUEUE/Search_Queue_Master.csv')
    return df.to_dict('records')

def read_video_queue(filters=None):
    """Read Video_Queue_Master.csv with optional filters"""
    df = pd.read_csv('01_VIDEO_QUEUE/Video_Queue_Master.csv')
    if filters:
        if 'status' in filters:
            df = df[df['Status'] == filters['status']]
        if 'priority_min' in filters:
            df = df[df['Priority_Score'] >= filters['priority_min']]
    return df.to_dict('records')
```

**Write Operations:**
```python
def add_video_to_queue(video_data):
    """Append new video to Video_Queue_Master.csv"""
    df = pd.read_csv('01_VIDEO_QUEUE/Video_Queue_Master.csv')
    new_id = generate_queue_id(df)  # VQ-XXX
    video_data['Queue_ID'] = new_id
    df = pd.concat([df, pd.DataFrame([video_data])], ignore_index=True)
    df.to_csv('01_VIDEO_QUEUE/Video_Queue_Master.csv', index=False)
    return new_id

def update_progress(video_id, phase, status):
    """Update VIDEO_PROGRESS_TRACKER.csv"""
    df = pd.read_csv('DATA/VIDEO_PROGRESS_TRACKER.csv')
    df.loc[df['Video_ID'] == video_id, f'Phase_{phase}_{phase_name}'] = status
    df.loc[df['Video_ID'] == video_id, 'Last_Updated'] = datetime.now()
    df.to_csv('DATA/VIDEO_PROGRESS_TRACKER.csv', index=False)
```

**Markdown File Handling:**

```python
def read_transcription(video_id):
    """Read Video_XXX.md file"""
    file_path = f'02_TRANSCRIPTIONS/Video_{video_id:03d}.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return parse_markdown(content)  # Parse sections

def create_transcription_file(video_id, content_dict):
    """Create Video_XXX.md from template"""
    template = load_template('templates/transcription_template.md')
    rendered = template.render(**content_dict)
    file_path = f'02_TRANSCRIPTIONS/Video_{video_id:03d}.md'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(rendered)
    return file_path
```

**JSON File Handling:**

```python
import json

def create_tool_json(tool_data):
    """Create tool JSON file"""
    file_name = f"{tool_data['id']}_{tool_data['name'].replace(' ', '_')}.json"
    file_path = f"04_INTEGRATION/Tools/{file_name}"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(tool_data, f, indent=2)

    return file_path

def move_to_library(source_path, entity_type):
    """Move JSON from 04_INTEGRATION to ENTITIES/LIBRARIES/"""
    import shutil
    target_dir = f"../../LIBRARIES/{entity_type}/"
    target_path = target_dir + os.path.basename(source_path)
    shutil.move(source_path, target_path)
    return target_path
```

---

### Configuration Management

**config.json Structure:**
```json
{
  "dropbox_root": "C:\\Users\\Dell\\Dropbox\\ENTITIES",
  "researches_root": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\TASK_MANAGERS\\RESEARCHES",
  "libraries_root": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\LIBRARIES",
  "departments": ["VID", "AID", "HRM", "FIN", "MKT"],
  "priority_weights": {
    "views": 30,
    "engagement": 20,
    "recency": 25,
    "relevance": 25
  },
  "phase_names": [
    "Search",
    "Transcribed",
    "Extraction",
    "Gap_Analysis",
    "Integration",
    "Mapping"
  ],
  "entity_types": [
    "Tools",
    "Workflows",
    "Actions",
    "Objects",
    "Skills",
    "Professions"
  ],
  "priority_levels": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
  "prompt_paths": {
    "transcription": "PROMPTS/PMT-004_Video_Transcription_v4.1.md",
    "extraction": "PROMPTS/PMT-007_Entity_Extraction.md",
    "gap_analysis": "PROMPTS/PMT-009_Taxonomy_Integration_Part1.md",
    "integration": "PROMPTS/PMT-009_Taxonomy_Integration_Part2.md",
    "mapping": "PROMPTS/PMT-009_Taxonomy_Integration_Part3.md"
  }
}
```

---

### Error Handling & Validation

**Validation Rules:**

**1. CSV Validation:**
```python
def validate_search_queue_entry(entry):
    """Validate search queue entry"""
    required_fields = ['Search_ID', 'Employee', 'Department', 'Topic',
                      'Search_Query', 'Status', 'Date_Assigned']

    # Check required fields
    for field in required_fields:
        if field not in entry or not entry[field]:
            raise ValueError(f"Missing required field: {field}")

    # Validate Search_ID format
    if not re.match(r'^SEARCH-\d{3}$', entry['Search_ID']):
        raise ValueError("Search_ID must be format: SEARCH-XXX")

    # Validate Status
    if entry['Status'] not in ['Assigned', 'In Progress', 'Completed']:
        raise ValueError("Invalid status")

    # Validate dates
    try:
        datetime.strptime(entry['Date_Assigned'], '%Y-%m-%d')
        if entry.get('Date_Completed'):
            datetime.strptime(entry['Date_Completed'], '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    return True
```

**2. File Integrity Checks:**
```python
def check_file_integrity(video_id):
    """Check all required files exist for a video"""
    issues = []

    # Check transcription
    trans_path = f'02_TRANSCRIPTIONS/Video_{video_id:03d}.md'
    if not os.path.exists(trans_path):
        issues.append(f"Missing transcription: {trans_path}")

    # Check progress tracker
    df = pd.read_csv('DATA/VIDEO_PROGRESS_TRACKER.csv')
    if video_id not in df['Video_ID'].values:
        issues.append(f"Video {video_id} not in progress tracker")

    # Check phase completion files
    progress = df[df['Video_ID'] == video_id].iloc[0]

    if progress['Phase_2_Extraction'] == 'Complete':
        ext_path = f'03_ANALYSIS/Extractions/Video_{video_id:03d}_Extraction.md'
        if not os.path.exists(ext_path):
            issues.append(f"Missing extraction: {ext_path}")

    return issues
```

**3. Progress Validation:**
```python
def validate_phase_transition(video_id, from_phase, to_phase):
    """Ensure phases are completed sequentially"""
    if to_phase != from_phase + 1:
        raise ValueError("Cannot skip phases")

    # Check previous phase is complete
    df = pd.read_csv('DATA/VIDEO_PROGRESS_TRACKER.csv')
    progress = df[df['Video_ID'] == video_id].iloc[0]

    phase_col = f'Phase_{from_phase}_'
    # Find the actual column name (varies by phase)
    phase_columns = [col for col in df.columns if col.startswith(phase_col)]

    if phase_columns:
        if progress[phase_columns[0]] != 'Complete':
            raise ValueError(f"Phase {from_phase} must be Complete before advancing")

    return True
```

---

## User Stories & Use Cases

### User Story 1: Adding Videos from Search

**As an** employee
**I want to** add videos discovered during a search to the processing queue
**So that** they can be transcribed and analyzed

**Acceptance Criteria:**
- Can paste YouTube URL and auto-fetch metadata
- Can manually enter metadata if auto-fetch fails
- Video is assigned unique Queue_ID (VQ-XXX)
- Priority score is calculated automatically
- Video appears in queue with "Pending" status
- Search_ID is linked to the video

**UI Flow:**
1. Click "Add Video" button
2. Paste YouTube URL or enter manually
3. Review auto-fetched metadata (title, channel, views, etc.)
4. Confirm or edit metadata
5. Video added to queue with confirmation message

---

### User Story 2: Selecting Videos for Processing

**As an** video department employee
**I want to** select high-priority videos from the queue for transcription
**So that** the most valuable content is processed first

**Acceptance Criteria:**
- Can view queue sorted by priority score
- Can filter by status, topic, date range
- Can manually select video or auto-select by priority threshold
- Selected video status changes to "Selected"
- Video appears in "Selected" view for processing

**UI Flow:**
1. View queue dashboard
2. Sort by Priority_Score descending
3. Review top videos
4. Click "Select for Processing" on chosen video
5. Confirmation dialog appears
6. Status updated, video moves to processing list

---

### User Story 3: Tracking Research Progress

**As a** department manager
**I want to** see the progress of all videos through processing phases
**So that** I can identify bottlenecks and monitor completion

**Acceptance Criteria:**
- Can view all videos in a phase progression board
- Can see time spent in each phase
- Can identify videos stuck in a phase
- Can filter by date range, employee, status
- Can drill into video details

**UI Flow:**
1. Navigate to Progress Dashboard
2. View Kanban board with 7 phases
3. See video cards in each phase column
4. Click on video card for details
5. View phase history and timestamps
6. Identify bottlenecks (phase with most videos)

---

### User Story 4: Generating Analysis Reports

**As a** researcher
**I want to** generate extraction and gap analysis reports automatically
**So that** I can identify new entities to integrate

**Acceptance Criteria:**
- Can trigger extraction analysis from video transcription
- Extraction report generated in structured format
- Gap analysis compares against existing libraries
- Priority assignments are suggested
- Reports saved to 03_ANALYSIS/ folders

**UI Flow:**
1. Navigate to video detail page
2. Click "Run Extraction" button (Phase 2)
3. AI processing indicator shown
4. Extraction report generated and displayed
5. Click "Run Gap Analysis" (Phase 3)
6. Gap analysis report shows new vs existing entities
7. Priority suggestions displayed
8. Reports saved automatically

---

### User Story 5: Creating Library Entries

**As a** library manager
**I want to** create JSON files for new entities
**So that** they can be integrated into the ENTITIES ecosystem

**Acceptance Criteria:**
- Can create JSON from gap analysis results
- Template auto-populated with extracted data
- Can edit fields before saving
- Cross-references auto-suggested
- File saved to 04_INTEGRATION/ initially
- Can move to ENTITIES/LIBRARIES/ when ready

**UI Flow:**
1. View gap analysis for video
2. Click "Create JSON" for a new entity
3. JSON template form appears with pre-filled data
4. Edit fields as needed
5. Add cross-references
6. Click "Save" - file created in 04_INTEGRATION/
7. Click "Move to Library" - file moved to ENTITIES/LIBRARIES/
8. ENTITIES_MASTER_LIST.csv updated

---

### User Story 6: Monitoring System KPIs

**As a** system administrator
**I want to** view KPIs and system health metrics
**So that** I can ensure the research system is operating efficiently

**Acceptance Criteria:**
- Dashboard shows: Total videos, Completed, In progress, Processing velocity
- Charts show phase distribution, completion trends
- Bottleneck alerts displayed
- Can export reports (PDF, CSV)

**UI Flow:**
1. Navigate to Dashboard
2. View KPI cards at top
3. Scroll to charts (phase distribution, trends)
4. Review bottleneck alerts
5. Click "Export Report" for PDF

---

### User Story 7: Batch Importing Videos

**As an** employee
**I want to** batch import multiple videos from a CSV
**So that** I can quickly add many videos at once

**Acceptance Criteria:**
- Can upload CSV file with video data
- Validation checks for required fields
- Duplicate detection
- Preview import before confirming
- Bulk import with progress indicator

**UI Flow:**
1. Click "Batch Import" button
2. Upload CSV file
3. System validates file
4. Preview table shows videos to import
5. Review and deselect any unwanted entries
6. Click "Import" - progress bar shown
7. Confirmation message with count imported

---

## Development Guidelines

### Code Organization

**Backend Structure:**
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app initialization
│   ├── config.py                # Configuration management
│   ├── models/                  # Data models
│   │   ├── __init__.py
│   │   ├── search_queue.py
│   │   ├── video_queue.py
│   │   ├── progress.py
│   │   └── entities.py
│   ├── routers/                 # API endpoints
│   │   ├── __init__.py
│   │   ├── search_queue.py
│   │   ├── video_queue.py
│   │   ├── progress.py
│   │   ├── analysis.py
│   │   ├── integration.py
│   │   └── reports.py
│   ├── services/                # Business logic
│   │   ├── __init__.py
│   │   ├── queue_manager.py
│   │   ├── priority_calculator.py
│   │   ├── progress_tracker.py
│   │   ├── analysis_engine.py
│   │   ├── integration_engine.py
│   │   └── report_generator.py
│   ├── dal/                     # Data access layer
│   │   ├── __init__.py
│   │   ├── csv_handler.py
│   │   ├── markdown_handler.py
│   │   └── json_handler.py
│   ├── utils/                   # Utilities
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   ├── file_utils.py
│   │   └── youtube_scraper.py
│   └── tests/                   # Unit tests
│       ├── test_queue_manager.py
│       ├── test_priority_calculator.py
│       └── test_validators.py
├── requirements.txt
└── README.md
```

**Frontend Structure:**
```
frontend/
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   ├── components/              # Reusable components
│   │   ├── Dashboard/
│   │   │   ├── KPICard.jsx
│   │   │   ├── PhaseChart.jsx
│   │   │   └── ActivityFeed.jsx
│   │   ├── Queue/
│   │   │   ├── QueueTable.jsx
│   │   │   ├── AddVideoForm.jsx
│   │   │   ├── VideoDetailModal.jsx
│   │   │   └── BatchImport.jsx
│   │   ├── Progress/
│   │   │   ├── ProgressBoard.jsx
│   │   │   ├── PhaseCard.jsx
│   │   │   └── VideoProgressModal.jsx
│   │   └── Common/
│   │       ├── Header.jsx
│   │       ├── Sidebar.jsx
│   │       └── LoadingSpinner.jsx
│   ├── pages/                   # Page components
│   │   ├── DashboardPage.jsx
│   │   ├── SearchQueuePage.jsx
│   │   ├── VideoQueuePage.jsx
│   │   ├── ProgressPage.jsx
│   │   ├── AnalysisPage.jsx
│   │   └── ReportsPage.jsx
│   ├── services/                # API calls
│   │   ├── api.js
│   │   ├── searchQueueService.js
│   │   ├── videoQueueService.js
│   │   └── progressService.js
│   ├── store/                   # State management
│   │   ├── store.js
│   │   ├── queueSlice.js
│   │   └── progressSlice.js
│   └── utils/
│       ├── formatters.js
│       └── validators.js
├── package.json
└── README.md
```

---

### Coding Standards

**Python (Backend):**
- Use PEP 8 style guide
- Type hints for all functions
- Docstrings for all public methods
- Use pathlib for file operations
- Exception handling for all file I/O
- Logging for all critical operations

**Example:**
```python
from pathlib import Path
from typing import List, Dict, Optional
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def read_video_queue(
    status_filter: Optional[str] = None,
    priority_min: Optional[int] = None
) -> List[Dict]:
    """
    Read Video_Queue_Master.csv with optional filters.

    Args:
        status_filter: Filter by status (Pending, Selected, etc.)
        priority_min: Minimum priority score

    Returns:
        List of video dictionaries

    Raises:
        FileNotFoundError: If queue file doesn't exist
        pd.errors.ParserError: If CSV is malformed
    """
    try:
        queue_path = Path('01_VIDEO_QUEUE/Video_Queue_Master.csv')
        df = pd.read_csv(queue_path)

        if status_filter:
            df = df[df['Status'] == status_filter]
        if priority_min:
            df = df[df['Priority_Score'] >= priority_min]

        logger.info(f"Read {len(df)} videos from queue")
        return df.to_dict('records')

    except Exception as e:
        logger.error(f"Error reading video queue: {e}")
        raise
```

**JavaScript/React (Frontend):**
- Use ESLint with Airbnb config
- Functional components with hooks
- PropTypes or TypeScript for type safety
- CSS modules or styled-components
- Error boundaries for error handling

**Example:**
```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { fetchVideoQueue } from '../services/videoQueueService';

const VideoQueueTable = ({ statusFilter, onVideoSelect }) => {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadVideos = async () => {
      try {
        setLoading(true);
        const data = await fetchVideoQueue({ status: statusFilter });
        setVideos(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadVideos();
  }, [statusFilter]);

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;

  return (
    <table className="video-queue-table">
      {/* Table implementation */}
    </table>
  );
};

VideoQueueTable.propTypes = {
  statusFilter: PropTypes.string,
  onVideoSelect: PropTypes.func.isRequired,
};

export default VideoQueueTable;
```

---

### Testing Requirements

**Unit Tests:**
- Test all business logic functions
- Test validators and utilities
- Test API endpoints (with mocked data)
- Target: 80%+ code coverage

**Integration Tests:**
- Test file I/O operations
- Test CSV read/write workflows
- Test phase transitions

**Example Test:**
```python
import pytest
from services.priority_calculator import calculate_priority

def test_priority_calculation():
    """Test priority score calculation"""
    priority = calculate_priority(
        views=1000000,
        likes=50000,
        publish_date='2024-01-01',
        topic_relevance=0.9
    )

    assert 70 <= priority <= 100, "High-value video should have high priority"

def test_priority_low_engagement():
    """Test priority for low engagement video"""
    priority = calculate_priority(
        views=1000,
        likes=10,
        publish_date='2020-01-01',
        topic_relevance=0.3
    )

    assert priority < 30, "Low engagement should result in low priority"
```

---

### Documentation Standards

**Code Documentation:**
- All functions must have docstrings
- API endpoints documented with OpenAPI/Swagger
- README with setup instructions
- Architecture diagram (Mermaid or draw.io)

**User Documentation:**
- User guide (PDF/web)
- Video tutorials for key workflows
- FAQ section
- Troubleshooting guide

---

## Integration Points

### Integration with ENTITIES Ecosystem

**Directory Mappings:**

**Research → Libraries:**
```
RESEARCHES/04_INTEGRATION/Tools/
  └─> ENTITIES/LIBRARIES/Tools/AI_Tools/
  └─> ENTITIES/LIBRARIES/Tools/Productivity/
  └─> etc.

RESEARCHES/04_INTEGRATION/Workflows/
  └─> ENTITIES/TASK_MANAGERS/TSM-006_Workflows/

RESEARCHES/04_INTEGRATION/Objects/
  └─> ENTITIES/LIBRARIES/Responsibilities/Objects/
```

**Master List Updates:**
```
RESEARCHES/DATA/RESEARCHES_Master_List.csv
  └─> Updates → ENTITIES/ENTITIES_MASTER_LIST.csv
```

**File Movement Logic:**
```python
def integrate_entity(json_path: str, entity_type: str) -> str:
    """
    Move entity JSON from RESEARCHES to ENTITIES ecosystem.

    Args:
        json_path: Path to JSON file in 04_INTEGRATION/
        entity_type: Type (Tools, Workflows, Objects)

    Returns:
        Final path in ENTITIES/LIBRARIES/
    """
    import shutil
    from pathlib import Path

    # Determine target directory
    if entity_type == 'Tools':
        # Read JSON to determine subcategory
        with open(json_path) as f:
            data = json.load(f)
        subcategory = data.get('subcategory', 'General')
        target_dir = Path(f'../../LIBRARIES/Tools/{subcategory}/')

    elif entity_type == 'Workflows':
        target_dir = Path('../../TASK_MANAGERS/TSM-006_Workflows/')

    elif entity_type == 'Objects':
        target_dir = Path('../../LIBRARIES/Responsibilities/Objects/')

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    # Move file
    target_path = target_dir / Path(json_path).name
    shutil.move(json_path, target_path)

    # Update master list
    update_entities_master_list(target_path, entity_type)

    return str(target_path)
```

---

### External APIs

**YouTube Data API (Optional):**
- Fetch video metadata automatically
- Get view counts, likes, comments
- Extract channel information

**AI Processing APIs (Optional):**
- OpenAI GPT-4 for transcription analysis
- Claude for entity extraction
- Gemini for cross-referencing

---

## Success Criteria

### Functional Success Criteria

✅ **Search Queue Management:**
- Can create, update, complete searches
- Validates all required fields
- Tracks videos discovered per search

✅ **Video Queue Management:**
- Can add videos (manual and batch)
- Priority calculation accurate
- Queue filtering and sorting functional
- Dashboard generation works

✅ **Progress Tracking:**
- All videos tracked through 7 phases
- Phase transitions validated
- Progress reports generated
- File integrity checks pass

✅ **Analysis Workflow:**
- Extraction reports generated from transcriptions
- Gap analysis compares against libraries
- Priority assignments logical

✅ **Library Integration:**
- JSON files created from templates
- Files moved to correct ENTITIES locations
- Master lists updated correctly
- Bidirectional links functional

✅ **Reporting:**
- KPIs calculated correctly
- Charts display accurate data
- Reports exportable (PDF, CSV)

---

### Non-Functional Success Criteria

✅ **Performance:**
- Queue operations < 1 second
- File operations < 3 seconds
- Dashboard load < 2 seconds
- Batch import of 50 videos < 30 seconds

✅ **Reliability:**
- File I/O error handling robust
- Data validation prevents corruption
- Backup/recovery mechanisms in place

✅ **Usability:**
- Intuitive UI requiring minimal training
- Clear error messages
- Responsive design (desktop-optimized)

✅ **Maintainability:**
- Code well-documented
- Modular architecture
- Easy to add new entity types
- Configuration-driven (not hardcoded)

---

## Appendix

### Prompt References

**Key Processing Prompts:**
- **PMT-004**: Video Transcription v4.1 (Phase 1)
- **PMT-007**: Entity Extraction & Cross-Referencing (Phase 2)
- **PMT-009 Part 1**: Taxonomy Integration - Gap Analysis (Phase 3)
- **PMT-009 Part 2**: Taxonomy Integration - JSON Creation (Phase 4)
- **PMT-009 Part 3**: Taxonomy Integration - Library Mapping (Phase 5)

**Location:** `RESEARCHES/PROMPTS/`

---

### Entity ID Formats

| Entity Type | ID Format | Example | Registry File |
|------------|-----------|---------|---------------|
| Research | RSR-XXX | RSR-001 | RESEARCHES_Master_List.csv |
| Search | SEARCH-XXX | SEARCH-001 | Search_Queue_Master.csv |
| Video Queue | VQ-XXX | VQ-001 | Video_Queue_Master.csv |
| Tool (AI) | TOOL-AI-XXX | TOOL-AI-045 | ENTITIES_MASTER_LIST.csv |
| Tool (General) | TOL-XXX | TOL-012 | ENTITIES_MASTER_LIST.csv |
| Workflow | WRF-XXX | WRF-012 | ENTITIES_MASTER_LIST.csv |
| Object | OBJ-XXX | OBJ-015 | ENTITIES_MASTER_LIST.csv |

---

### Glossary

- **Phase 0**: Search Queue - discovering videos
- **Phase 0→1 Transition**: Video Queue accumulation and prioritization
- **Phase 1**: Transcription - full content processing with PMT-004
- **Phase 2**: Extraction - deep entity extraction with PMT-007
- **Phase 3**: Gap Analysis - comparison against existing libraries
- **Phase 4**: Integration - JSON file creation
- **Phase 5**: Library Mapping - file movement and documentation
- **Complete**: All phases finished, fully integrated
- **Bidirectional Links**: Cross-references that work both ways (Tool → Workflow, Workflow → Tool)
- **Coverage**: Percentage of entities that exist in libraries vs extracted
- **Priority Score**: Calculated value (0-100) for video queue ranking

---

## Final Notes

This Research Management System represents a sophisticated multi-phase workflow for transforming raw content into structured, cross-referenced knowledge. The app should:

1. **Automate** where possible (priority calculation, file validation, progress tracking)
2. **Validate** rigorously (data integrity, phase progression, file existence)
3. **Visualize** effectively (dashboards, charts, progress boards)
4. **Integrate** seamlessly (with ENTITIES ecosystem, bidirectional links)
5. **Document** thoroughly (reports, mapping, completion summaries)

**Development Approach:**
- Start with core features (Search Queue, Video Queue, Progress Tracking)
- Build incrementally (add Analysis, Integration, Reporting)
- Test continuously (unit tests, integration tests, user acceptance)
- Deploy iteratively (MVP → Full System → Optimization)

**Success = 7-phase workflow fully automated, all entities integrated, complete visibility across the research pipeline.**

---

**End of Development Prompt**

**Version:** 1.0
**Document Path:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\App_Development_Prompt.md`
**Last Updated:** 2025-11-27
