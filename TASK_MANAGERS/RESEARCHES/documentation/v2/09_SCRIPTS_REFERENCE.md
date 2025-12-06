# 09_SCRIPTS_REFERENCE.md

**Complete Reference for All 14 RESEARCHES 2 Automation Scripts**

**Last Updated:** 2025-12-04
**Total Scripts:** 14
**Categories:** Search Queue (2), Video Queue (6), Processing (6)

---

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Search Queue Scripts](#search-queue-scripts-2-scripts)
3. [Video Queue Scripts](#video-queue-scripts-6-scripts)
4. [Processing Scripts](#processing-scripts-6-scripts)
5. [Common Workflows](#common-workflows)
6. [Troubleshooting](#troubleshooting)
7. [Script Dependencies](#script-dependencies)

---

## Installation & Setup

### Prerequisites

**Python Version:** 3.8 or higher

### Install Required Dependencies

```bash
# Navigate to RESEARCHES 2 directory
cd "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2"

# Install dependencies
pip install pandas requests python-dateutil yt-dlp

# Verify installation
python --version
pip list | grep -E "pandas|requests|dateutil|yt-dlp"
```

### Required Python Packages

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | ≥1.5.0 | CSV/Excel data manipulation |
| requests | ≥2.28.0 | API calls and web requests |
| python-dateutil | ≥2.8.0 | Date/time handling |
| yt-dlp | ≥2023.3.0 | YouTube metadata extraction |

### Verify Installation

```bash
# Test script execution
python scripts/video_id_scanner.py

# Expected output: "Script initialized successfully"
```

### Directory Structure Required

```
RESEARCHES 2/
├── 00_SEARCH_QUEUE/
│   ├── scripts/
│   │   ├── assign_search.py
│   │   └── complete_search.py
│   └── Search_Queue_Master.csv
│
├── 01_VIDEO_QUEUE/
│   ├── scripts/
│   │   ├── add_video_to_queue.py
│   │   ├── add_video_to_queue_simple.py
│   │   ├── update_queue_status.py
│   │   ├── calculate_priority.py
│   │   └── export_queue.py
│   ├── video_queue_manager.py
│   └── Video_Queue_Master.csv
│
└── scripts/
    ├── process_video.py
    ├── video_gap_analyzer.py
    ├── video_json_updater.py
    ├── video_integration_reporter.py
    ├── update_video_progress.py
    ├── generate_progress_report.py
    ├── config.py
    ├── utils.py
    └── video_id_scanner.py
```

---

## Search Queue Scripts (2 Scripts)

### 1. assign_search.py

**Purpose:** Assign new video search tasks to employees

**Location:** `00_SEARCH_QUEUE/scripts/assign_search.py`

**Usage:**

```bash
python 00_SEARCH_QUEUE/scripts/assign_search.py <employee> <department> <topic> [search_query] [notes]
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| employee | Yes | String | Employee name | "John Doe" |
| department | Yes | String | Department code (AID, DEV, DGN, etc.) | "DEV" |
| topic | Yes | String | Search topic/category | "Claude AI tutorials" |
| search_query | No | String | Optional search query | "claude api tutorial 2025" |
| notes | No | String | Additional notes/instructions | "Focus on Sonnet 4.5" |

**Examples:**

```bash
# Basic search assignment
python 00_SEARCH_QUEUE/scripts/assign_search.py "John Doe" "DEV" "Claude AI tutorials"

# With search query
python 00_SEARCH_QUEUE/scripts/assign_search.py "Jane Smith" "DGN" "Figma AI plugins" "figma ai plugin 2025"

# With notes
python 00_SEARCH_QUEUE/scripts/assign_search.py "Mike Johnson" "AID" "ChatGPT automation" "chatgpt api examples" "Focus on workflow automation"
```

**Output:**

- Generates unique ID: `SEARCH-XXX` (e.g., SEARCH-001, SEARCH-042)
- Creates entry in `Search_Queue_Master.csv`:

```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Date_Assigned,Videos_Found,Date_Completed,Notes
SEARCH-001,John Doe,DEV,Claude AI tutorials,claude tutorial,Assigned,2025-12-04,0,,Focus on 2024-2025
```

**Functionality:**

1. ✅ Generates unique sequential SEARCH-XXX IDs
2. ✅ Tracks employee assignments
3. ✅ Records department and topic
4. ✅ Sets initial status to "Assigned"
5. ✅ Updates Search_Queue_Master.csv
6. ✅ Creates backup before modification

**Status Workflow:**

```
Assigned → In Progress → Completed
```

---

### 2. complete_search.py

**Purpose:** Mark search tasks as completed and record results

**Location:** `00_SEARCH_QUEUE/scripts/complete_search.py`

**Usage:**

```bash
python 00_SEARCH_QUEUE/scripts/complete_search.py <search_id> <videos_found> [notes]
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| search_id | Yes | String | SEARCH-XXX ID from assignment | "SEARCH-001" |
| videos_found | Yes | Integer | Number of videos discovered | 15 |
| notes | No | String | Completion notes | "Found excellent tutorials" |

**Examples:**

```bash
# Basic completion
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 15

# With notes
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-002 23 "Found excellent tutorials from Anthropic channel"

# No videos found
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-003 0 "Topic too narrow, need to broaden search"
```

**Output:**

Updates `Search_Queue_Master.csv`:

```csv
Search_ID,Employee,Department,Topic,Status,Date_Assigned,Videos_Found,Date_Completed,Notes
SEARCH-001,John Doe,DEV,Claude AI tutorials,Completed,2025-12-04,15,2025-12-04,Found excellent tutorials
```

**Functionality:**

1. ✅ Updates search status to "Completed"
2. ✅ Records number of videos found
3. ✅ Adds completion date (auto-generated)
4. ✅ Updates notes if provided
5. ✅ Validates SEARCH-XXX ID exists
6. ✅ Creates backup before modification

**Error Handling:**

```bash
# Invalid search ID
python complete_search.py SEARCH-999 10
# Error: SEARCH-999 not found in Search_Queue_Master.csv

# Already completed
python complete_search.py SEARCH-001 10
# Warning: SEARCH-001 already marked as Completed
```

---

## Video Queue Scripts (6 Scripts)

### 3. add_video_to_queue.py

**Purpose:** Add videos to the processing queue with full metadata extraction

**Location:** `01_VIDEO_QUEUE/scripts/add_video_to_queue.py`

**Usage:**

```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py <youtube_url> <employee> <topic> <source> [notes]
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| youtube_url | Yes | String | Full YouTube URL | "https://youtube.com/watch?v=abc123" |
| employee | Yes | String | Employee who found video | "John Doe" |
| topic | Yes | String | Video topic/category | "Claude AI" |
| source | Yes | String | Where video was found | "Perplexity", "Manual Search" |
| notes | No | String | Additional notes | "Important tutorial" |

**Examples:**

```bash
# Basic video addition
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
  "https://youtube.com/watch?v=abc123" \
  "John Doe" \
  "Claude AI" \
  "Perplexity"

# With notes
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
  "https://youtube.com/watch?v=def456" \
  "Jane Smith" \
  "Figma Automation" \
  "Manual Search" \
  "Covers advanced API integration"

# From search results
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
  "https://youtube.com/watch?v=ghi789" \
  "Mike Johnson" \
  "ChatGPT Workflows" \
  "SEARCH-001" \
  "Part of Claude AI tutorials search"
```

**Output:**

- Generates unique ID: `VQ-XXX` (e.g., VQ-001, VQ-042)
- Extracts metadata from YouTube:
  - Video title
  - Channel name
  - Duration
  - View count
  - Upload date
  - Description (first 200 chars)
- Calculates priority score (0-100)
- Creates entry in `Video_Queue_Master.csv`:

```csv
Video_ID,YouTube_URL,Title,Channel,Duration,Views,Upload_Date,Topic,Source,Employee,Priority,Status,Date_Added,Notes
VQ-001,https://youtube.com/watch?v=abc123,Claude API Tutorial,Anthropic,15:32,12500,2025-11-20,Claude AI,Perplexity,John Doe,85,Queued,2025-12-04,Important tutorial
```

**Priority Calculation:**

```python
priority_score = (
    date_recency_score * 0.30 +      # 30 points: Newer = higher
    source_credibility_score * 0.25 + # 25 points: Official > Community
    topic_relevance_score * 0.25 +    # 25 points: Core topics higher
    engagement_score * 0.20           # 20 points: Views, likes, comments
)
```

**Functionality:**

1. ✅ Generates unique VQ-XXX IDs
2. ✅ Validates YouTube URL format
3. ✅ Extracts video metadata via yt-dlp
4. ✅ Calculates priority score (0-100)
5. ✅ Sets initial status to "Queued"
6. ✅ Updates Video_Queue_Master.csv
7. ✅ Creates backup before modification
8. ✅ Handles rate limiting and API errors

**Error Handling:**

```bash
# Invalid URL
python add_video_to_queue.py "not-a-url" "John" "Topic" "Source"
# Error: Invalid YouTube URL format

# Video unavailable
python add_video_to_queue.py "https://youtube.com/watch?v=deleted123" "John" "Topic" "Source"
# Error: Video unavailable or private

# Duplicate video
python add_video_to_queue.py "https://youtube.com/watch?v=abc123" "John" "Topic" "Source"
# Warning: Video already in queue as VQ-001
```

---

### 4. add_video_to_queue_simple.py

**Purpose:** Simplified version for quick video additions without metadata extraction

**Location:** `01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py`

**Usage:**

```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py <youtube_url>
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| youtube_url | Yes | String | Full YouTube URL | "https://youtube.com/watch?v=abc123" |

**Examples:**

```bash
# Quick add single video
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py "https://youtube.com/watch?v=abc123"

# Batch add multiple videos
cat video_urls.txt | while read url; do
  python add_video_to_queue_simple.py "$url"
done
```

**Output:**

- Uses default values:
  - Employee: "System"
  - Source: "Quick Add"
  - Topic: "General"
  - Priority: 50 (medium)
- Skips metadata extraction (faster processing)
- Creates entry in `Video_Queue_Master.csv`

**Use Cases:**

- ✅ Batch importing videos from text file
- ✅ Quick additions during research
- ✅ Emergency high-priority additions
- ✅ When metadata not needed immediately

**Functionality:**

1. ✅ Minimal input required (just URL)
2. ✅ Faster processing (no API calls)
3. ✅ Default priority (50)
4. ✅ Status: "Queued"
5. ✅ Can update metadata later with calculate_priority.py

---

### 5. update_queue_status.py

**Purpose:** Update video status in queue and track processing progress

**Location:** `01_VIDEO_QUEUE/scripts/update_queue_status.py`

**Usage:**

```bash
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update <video_id> <new_status> [employee] [notes]
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_id | Yes | String | VQ-XXX ID | "VQ-001" |
| new_status | Yes | String | New status (see list below) | "Selected" |
| employee | No | String | Employee making change | "John Doe" |
| notes | No | String | Status change notes | "Starting transcription" |

**Valid Statuses:**

```
Queued         → Initial state when video added
Selected       → Video chosen for processing
In_Progress    → Currently being processed
Transcribing   → Transcription phase (Phase 1)
Transcribed    → Transcription complete
Extracting     → Extraction phase (Phase 2)
Extracted      → Extraction complete
Analyzing      → Gap analysis phase (Phase 3)
Integrating    → Integration phase (Phase 4)
Mapping        → Mapping phase (Phase 5)
Completed      → All phases finished
Skipped        → Video skipped (duplicate, irrelevant, etc.)
On_Hold        → Temporarily paused
```

**Examples:**

```bash
# Mark video as selected for processing
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Selected "John Doe"

# Update to transcribing
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Transcribing "John Doe" "Using PMT-004"

# Mark as completed
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Completed "John Doe" "All phases complete, 37 entities extracted"

# Skip video
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-042 Skipped "System" "Duplicate of VQ-023"
```

**Output:**

Updates `Video_Queue_Master.csv`:

```csv
Video_ID,Status,Last_Updated,Updated_By,Processing_Notes
VQ-001,Selected,2025-12-04 10:30:00,John Doe,Ready for Phase 1
VQ-001,Transcribing,2025-12-04 11:00:00,John Doe,Using PMT-004
VQ-001,Completed,2025-12-04 16:45:00,John Doe,All phases complete, 37 entities extracted
```

**Functionality:**

1. ✅ Updates video status
2. ✅ Records employee who made change
3. ✅ Adds timestamp (auto-generated)
4. ✅ Updates processing notes
5. ✅ Validates status transitions
6. ✅ Creates audit trail
7. ✅ Backup before modification

**Status Transition Validation:**

```python
# Valid transitions
Queued → Selected ✅
Selected → In_Progress ✅
In_Progress → Transcribing ✅
Transcribing → Transcribed ✅
# ... etc.

# Invalid transitions
Queued → Completed ❌ (must go through phases)
Completed → Queued ❌ (can't go backwards)
```

---

### 6. calculate_priority.py

**Purpose:** Calculate and update priority scores for queued videos

**Location:** `01_VIDEO_QUEUE/scripts/calculate_priority.py`

**Usage:**

```bash
# Calculate priority for specific video
python 01_VIDEO_QUEUE/scripts/calculate_priority.py <video_id>

# Recalculate priorities for all queued videos
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --all

# Calculate for specific status
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --status Queued
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_id | No* | String | VQ-XXX ID for single video | "VQ-001" |
| --all | No* | Flag | Calculate for all videos | |
| --status | No | String | Calculate for specific status | "Queued" |

*Either video_id or --all must be provided

**Examples:**

```bash
# Single video
python 01_VIDEO_QUEUE/scripts/calculate_priority.py VQ-001
# Output: VQ-001 priority updated: 65 → 82

# All queued videos
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --all
# Output: Updated 45 videos, average priority: 67.3

# Specific status
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --status Selected
# Output: Updated 5 videos with status 'Selected'
```

**Priority Calculation Factors:**

| Factor | Weight | Max Points | Calculation |
|--------|--------|------------|-------------|
| Date Added | 30% | 30 | Older videos = higher priority |
| Source Credibility | 25% | 25 | Official > Community > Unknown |
| Topic Relevance | 25% | 25 | Core topics > General topics |
| Engagement | 20% | 20 | Views, likes, comments ratio |

**Detailed Priority Formula:**

```python
# 1. Date Recency Score (30 points max)
days_in_queue = (today - date_added).days
date_score = min(30, days_in_queue * 2)  # 2 points per day, max 30

# 2. Source Credibility Score (25 points max)
source_scores = {
    "Official Channel": 25,      # Anthropic, OpenAI, etc.
    "Verified Expert": 22,       # Industry experts
    "Perplexity": 20,            # AI-curated
    "Manual Search": 18,         # Human-curated
    "Community": 15,             # User submissions
    "Quick Add": 10,             # Minimal vetting
    "Unknown": 5                 # No source info
}

# 3. Topic Relevance Score (25 points max)
topic_scores = {
    "Claude AI": 25,             # Core topic
    "ChatGPT": 23,               # Core topic
    "API Integration": 22,       # Important topic
    "Automation": 20,            # Important topic
    "Design Tools": 18,          # Relevant topic
    "General": 10                # General topic
}

# 4. Engagement Score (20 points max)
views_per_day = views / days_since_upload
engagement_score = min(20, log10(views_per_day) * 5)

# Total Priority
priority = date_score + source_score + topic_score + engagement_score
```

**Output:**

Updates `Video_Queue_Master.csv` with new priority scores:

```csv
Video_ID,Priority,Priority_Factors,Last_Calculated
VQ-001,82,"Date:28,Source:25,Topic:20,Engagement:9",2025-12-04
VQ-002,67,"Date:12,Source:20,Topic:18,Engagement:17",2025-12-04
```

**Functionality:**

1. ✅ Recalculates priority scores using latest data
2. ✅ Updates Video_Queue_Master.csv
3. ✅ Logs priority changes
4. ✅ Can process single video or batch
5. ✅ Shows before/after comparison
6. ✅ Creates backup before modification

**Use Cases:**

- ✅ Daily priority recalculation (automated cron job)
- ✅ After adding new videos (to reorder queue)
- ✅ When selecting next videos to process
- ✅ After changing topic priorities

---

### 7. export_queue.py

**Purpose:** Export queue to various formats for reporting and analysis

**Location:** `01_VIDEO_QUEUE/scripts/export_queue.py`

**Usage:**

```bash
python 01_VIDEO_QUEUE/scripts/export_queue.py <format> [--status STATUS] [--output PATH]
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| format | Yes | String | Export format (csv, json, markdown, html, all) | "json" |
| --status | No | String | Filter by status | "Queued" |
| --output | No | Path | Output file path | "./reports/queue.json" |

**Export Formats:**

1. **CSV** - Spreadsheet-compatible format
2. **JSON** - Structured data for APIs
3. **Markdown** - Human-readable documentation
4. **HTML** - Interactive dashboard
5. **All** - Export to all formats

**Examples:**

```bash
# Export all videos as JSON
python 01_VIDEO_QUEUE/scripts/export_queue.py json

# Export only queued videos as Markdown
python 01_VIDEO_QUEUE/scripts/export_queue.py markdown --status Queued

# Export to specific location
python 01_VIDEO_QUEUE/scripts/export_queue.py csv --output "./reports/weekly_queue.csv"

# Export all formats
python 01_VIDEO_QUEUE/scripts/export_queue.py all

# Filter by status and export
python 01_VIDEO_QUEUE/scripts/export_queue.py json --status Completed --output "./completed_videos.json"
```

**Output Examples:**

**CSV Format:**
```csv
Video_ID,Title,Channel,Duration,Priority,Status,Date_Added,Topic,Source
VQ-001,Claude API Tutorial,Anthropic,15:32,85,Queued,2025-12-04,Claude AI,Perplexity
VQ-002,ChatGPT Automation,OpenAI,22:15,78,Selected,2025-12-03,ChatGPT,Manual Search
```

**JSON Format:**
```json
{
  "export_date": "2025-12-04T10:30:00",
  "total_videos": 45,
  "filtered_videos": 12,
  "filter_status": "Queued",
  "videos": [
    {
      "video_id": "VQ-001",
      "youtube_url": "https://youtube.com/watch?v=abc123",
      "title": "Claude API Tutorial",
      "channel": "Anthropic",
      "duration": "15:32",
      "views": 12500,
      "upload_date": "2025-11-20",
      "topic": "Claude AI",
      "source": "Perplexity",
      "priority": 85,
      "status": "Queued",
      "date_added": "2025-12-04",
      "employee": "John Doe"
    }
  ]
}
```

**Markdown Format:**
```markdown
# Video Queue Export

**Export Date:** 2025-12-04
**Total Videos:** 45
**Status Filter:** Queued

## Queued Videos (12)

### VQ-001: Claude API Tutorial
- **Channel:** Anthropic
- **Duration:** 15:32
- **Priority:** 85
- **Topic:** Claude AI
- **Source:** Perplexity
- **Added:** 2025-12-04
- **URL:** https://youtube.com/watch?v=abc123
```

**HTML Format:**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Video Queue Dashboard</title>
  <style>/* Dashboard styles */</style>
</head>
<body>
  <h1>Video Queue Dashboard</h1>
  <div class="stats">
    <div class="stat">Total Videos: 45</div>
    <div class="stat">Queued: 12</div>
    <div class="stat">In Progress: 5</div>
    <div class="stat">Completed: 28</div>
  </div>
  <table>
    <thead>
      <tr><th>ID</th><th>Title</th><th>Priority</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr><td>VQ-001</td><td>Claude API Tutorial</td><td>85</td><td>Queued</td></tr>
      <!-- ... more rows ... -->
    </tbody>
  </table>
</body>
</html>
```

**Functionality:**

1. ✅ Export to multiple formats
2. ✅ Filter by status, date, priority
3. ✅ Sort by priority, date, status
4. ✅ Include statistics summary
5. ✅ Generate reports for specific timeframes
6. ✅ Create backups automatically

**Use Cases:**

- ✅ Weekly progress reports
- ✅ Team dashboards
- ✅ Priority planning meetings
- ✅ System backups
- ✅ API integrations

---

### 8. video_queue_manager.py

**Purpose:** Interactive CLI interface for queue management

**Location:** `01_VIDEO_QUEUE/video_queue_manager.py`

**Usage:**

```bash
python 01_VIDEO_QUEUE/video_queue_manager.py
```

**No parameters required** - Interactive menu-driven interface

**Main Menu:**

```
======================================
    VIDEO QUEUE MANAGER v2.0
======================================

1. View Queue Statistics
2. View All Videos
3. View Videos by Status
4. Add New Video
5. Update Video Status
6. Calculate Priorities
7. Export Queue
8. Search Videos
9. Generate Reports
0. Exit

Enter your choice:
```

**Features:**

**1. View Queue Statistics**
```
Queue Statistics
================
Total Videos: 45
By Status:
  Queued: 12
  Selected: 5
  In Progress: 3
  Completed: 28
  Skipped: 2

Average Priority: 67.3
Highest Priority: VQ-001 (85)
Oldest Video: VQ-023 (15 days)
```

**2. View All Videos**
```
All Videos (sorted by priority)
================================
ID      Title                      Priority  Status      Date Added
----------------------------------------------------------------------
VQ-001  Claude API Tutorial        85        Queued      2025-12-04
VQ-005  ChatGPT Automation Guide   82        Selected    2025-12-03
VQ-012  Figma Plugin Development   78        In Progress 2025-12-02
...
```

**3. View Videos by Status**
```
Enter status (Queued/Selected/In_Progress/Completed/Skipped): Queued

Videos with status: Queued (12 videos)
======================================
VQ-001: Claude API Tutorial (Priority: 85)
VQ-007: OpenAI API Integration (Priority: 79)
VQ-015: Automation Workflows (Priority: 72)
...
```

**4. Add New Video**
```
Add New Video
=============
YouTube URL: https://youtube.com/watch?v=abc123
Employee: John Doe
Topic: Claude AI
Source: Perplexity
Notes (optional): Important tutorial

Fetching video metadata...
✓ Title: Claude API Tutorial
✓ Channel: Anthropic
✓ Duration: 15:32

Calculating priority... Priority: 85
Video added successfully as VQ-001
```

**5. Update Video Status**
```
Update Video Status
===================
Video ID: VQ-001
Current Status: Queued

Available statuses:
1. Selected
2. In_Progress
3. Transcribing
4. Completed
5. Skipped

New Status: 2 (In_Progress)
Employee: John Doe
Notes (optional): Starting Phase 1

Status updated successfully
VQ-001: Queued → In_Progress
```

**6. Calculate Priorities**
```
Calculate Priorities
====================
1. Calculate for specific video
2. Recalculate all queued videos
3. Recalculate by status

Choice: 2

Recalculating priorities for all queued videos...
Progress: [████████████████████] 100% (12/12 videos)

Results:
- Updated: 12 videos
- Average priority: 67.3
- Highest: VQ-001 (85)
- Lowest: VQ-034 (42)
```

**7. Export Queue**
```
Export Queue
============
1. CSV
2. JSON
3. Markdown
4. HTML
5. All formats

Format: 2 (JSON)
Filter by status (leave blank for all): Queued
Output path (leave blank for default):

Exporting to: ./exports/queue_2025-12-04.json
✓ Export complete (12 videos exported)
```

**8. Search Videos**
```
Search Videos
=============
Search by:
1. Title
2. Channel
3. Topic
4. Employee

Choice: 1
Search term: Claude

Found 8 videos matching "Claude":
VQ-001: Claude API Tutorial (Anthropic)
VQ-015: Claude Prompt Engineering (AI Explained)
VQ-023: Getting Started with Claude (Official)
...
```

**9. Generate Reports**
```
Generate Reports
================
1. Weekly Summary
2. Monthly Summary
3. Employee Activity
4. Topic Analysis
5. Priority Distribution

Report Type: 1 (Weekly Summary)

Generating weekly summary...
✓ Report saved to: ./reports/weekly_summary_2025-12-04.md
```

**Functionality:**

1. ✅ Interactive menu system
2. ✅ Real-time statistics
3. ✅ Batch operations
4. ✅ Search and filter
5. ✅ Export and reporting
6. ✅ Error handling
7. ✅ User-friendly interface

**Keyboard Shortcuts:**

- `Ctrl+C` - Exit safely
- `0` - Return to main menu
- `q` - Quit application

---

## Processing Scripts (6 Scripts)

### 9. process_video.py

**Purpose:** Master orchestrator for complete video processing workflow (all 7 phases)

**Location:** `scripts/process_video.py`

**Usage:**

```bash
# Run all phases
python scripts/process_video.py <video_number> --all-phases

# Run specific phase
python scripts/process_video.py <video_number> --phase <phase_number>

# Run multiple phases
python scripts/process_video.py <video_number> --phases 1,2,3

# Dry run (show what would be done)
python scripts/process_video.py <video_number> --dry-run
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_number | Yes | Integer | Video number (e.g., 24 for Video_024) | 24 |
| --all-phases | No | Flag | Run all phases (1-5) | |
| --phase | No | Integer | Run specific phase (1-5) | 3 |
| --phases | No | List | Run multiple phases | "1,2,3" |
| --dry-run | No | Flag | Show actions without executing | |
| --employee | No | String | Employee name | "John Doe" |

**Examples:**

```bash
# Process entire video (all phases)
python scripts/process_video.py 24 --all-phases --employee "John Doe"

# Run just Phase 1 (Transcription)
python scripts/process_video.py 24 --phase 1

# Run Phases 2-3 (Extraction + Gap Analysis)
python scripts/process_video.py 24 --phases 2,3

# Dry run to preview actions
python scripts/process_video.py 24 --all-phases --dry-run

# Resume from specific phase
python scripts/process_video.py 24 --phase 4
```

**Output:**

```
Processing Video_024
====================
Employee: John Doe
Mode: All Phases (1-5)

Phase 0: Pre-checks
-------------------
✓ Video_024.md found in 02_TRANSCRIPTIONS/
✓ Video_024 exists in queue (VQ-024)
✓ Current status: Selected

Phase 1: Transcription
----------------------
✓ Transcript found (15,234 words)
✓ PMT-004 analysis complete
✓ 37 entities extracted
✓ Video_024.md updated
✓ Progress tracker updated

Phase 2: Extraction
-------------------
Running video entity extraction...
✓ Phase3_Analysis.md created (23 workflows, 18 tools)
✓ Phase4_Objects.md created (42 objects)
✓ Cross-references added (187 links)
✓ Progress tracker updated

Phase 3: Gap Analysis
---------------------
Running video_gap_analyzer.py...
Comparing against LIBRARIES/...
✓ Gap analysis complete
  - NEW: 28 entities
  - EXISTING: 94 entities
  - UPDATE: 5 entities
✓ Video_024_Gap_Analysis.md created
✓ Progress tracker updated

Phase 4: Integration
--------------------
Creating JSON files for NEW entities...
Progress: [████████████████████] 100% (28/28 entities)
✓ 28 JSON files created
✓ Cross-references validated (bidirectional)
✓ Integration_Log.csv updated
✓ Progress tracker updated

Phase 5: Mapping
----------------
Running video_integration_reporter.py...
✓ Comprehensive report generated
✓ Coverage: 51% → 96% (+45%)
✓ Business value analysis complete
✓ Video_024_Library_Mapping_Report.md created
✓ Progress tracker updated to "Complete"

Summary
=======
Video: Video_024
Status: Complete
Total Time: 2h 15m
Entities: 127 (28 NEW, 94 EXISTING, 5 UPDATE)
Coverage Improvement: +45%
Files Created: 5
JSON Files: 28

All phases completed successfully!
```

**Phase Breakdown:**

| Phase | Name | Script/Prompt | Time | Output |
|-------|------|---------------|------|--------|
| 1 | Transcription | PMT-004 | 1-2h | Video_024.md |
| 2 | Extraction | PMT-007 | 30-45m | Phase3_Analysis.md, Phase4_Objects.md |
| 3 | Gap Analysis | video_gap_analyzer.py | 2-3m | Video_024_Gap_Analysis.md |
| 4 | Integration | video_json_updater.py | 45-60m | 28 JSON files |
| 5 | Mapping | video_integration_reporter.py | 2-3m | Video_024_Library_Mapping_Report.md |

**Functionality:**

1. ✅ Orchestrates all 7 phases
2. ✅ Pre-checks (file existence, status validation)
3. ✅ Executes phases in order
4. ✅ Updates progress tracker after each phase
5. ✅ Error handling and rollback
6. ✅ Detailed logging
7. ✅ Can resume from any phase
8. ✅ Dry run mode for planning

**Error Handling:**

```bash
# Missing transcript
python process_video.py 99 --all-phases
# Error: Video_099.md not found in 02_TRANSCRIPTIONS/

# Invalid phase
python process_video.py 24 --phase 6
# Error: Phase 6 does not exist. Valid phases: 1-5

# Phase out of order
python process_video.py 24 --phase 4
# Warning: Phase 3 not completed. Run Phase 3 first?
```

---

### 10. video_gap_analyzer.py

**Purpose:** Automate Phase 3 gap analysis (compare extracted entities vs LIBRARIES)

**Location:** `scripts/video_gap_analyzer.py`

**Usage:**

```bash
# Analyze specific video
python scripts/video_gap_analyzer.py <video_number>

# Analyze with detailed output
python scripts/video_gap_analyzer.py <video_number> --verbose

# Generate JSON output
python scripts/video_gap_analyzer.py <video_number> --format json

# Analyze multiple videos
python scripts/video_gap_analyzer.py 24,25,26
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_number | Yes | Integer/List | Video number(s) | 24 or "24,25,26" |
| --verbose | No | Flag | Detailed output | |
| --format | No | String | Output format (markdown, json, both) | "json" |
| --output | No | Path | Custom output path | "./reports/" |

**Examples:**

```bash
# Basic gap analysis
python scripts/video_gap_analyzer.py 24

# Verbose output
python scripts/video_gap_analyzer.py 24 --verbose

# JSON format for API
python scripts/video_gap_analyzer.py 24 --format json

# Custom output location
python scripts/video_gap_analyzer.py 24 --output "./gap_reports/"

# Batch analysis
python scripts/video_gap_analyzer.py 24,25,26 --format both
```

**Output:**

**Console Output:**
```
Video Gap Analysis
==================
Video: Video_024
Title: Claude API Tutorial
Source: 02_TRANSCRIPTIONS/Video_024.md

Analyzing Entities
==================
Workflows: 23 extracted
  → Comparing against LIBRARIES/Workflows/...
  → NEW: 7 workflows
  → EXISTING: 14 workflows
  → UPDATE: 2 workflows

Tools: 18 extracted
  → Comparing against LIBRARIES/Tools/...
  → NEW: 5 tools
  → EXISTING: 12 tools
  → UPDATE: 1 tool

Objects: 42 extracted
  → Comparing against LIBRARIES/Objects/...
  → NEW: 16 objects
  → EXISTING: 24 objects
  → UPDATE: 2 objects

Actions: 28 extracted
  → Comparing against LIBRARIES/Actions/...
  → NEW: 0 actions (all existing)
  → EXISTING: 28 actions
  → UPDATE: 0 actions

Summary
=======
Total Entities: 127
  NEW: 28 (22.0%)
  EXISTING: 94 (74.0%)
  UPDATE: 5 (4.0%)

Library Coverage
================
Before: 51% (94/185 entities in library)
After: 96% (122/127 entities will be in library)
Improvement: +45%

Saved: 03_VIDEO_ENTITIES/Video_024_Gap_Analysis.md
Processing Time: 2m 34s
```

**Markdown Output (Video_024_Gap_Analysis.md):**
```markdown
# Gap Analysis: Video_024

**Video:** Video_024 - Claude API Tutorial
**Date:** 2025-12-04
**Analyzed By:** video_gap_analyzer.py v2.1

## Summary

| Category | Total | NEW | EXISTING | UPDATE |
|----------|-------|-----|----------|--------|
| Workflows | 23 | 7 (30%) | 14 (61%) | 2 (9%) |
| Tools | 18 | 5 (28%) | 12 (67%) | 1 (6%) |
| Objects | 42 | 16 (38%) | 24 (57%) | 2 (5%) |
| Actions | 28 | 0 (0%) | 28 (100%) | 0 (0%) |
| Professions | 8 | 0 (0%) | 8 (100%) | 0 (0%) |
| Skills | 6 | 0 (0%) | 6 (100%) | 0 (0%) |
| Departments | 2 | 0 (0%) | 2 (100%) | 0 (0%) |
| **TOTAL** | **127** | **28** | **94** | **5** |

## Library Coverage

- **Before:** 51% (94/185 entities)
- **After:** 96% (122/127 entities)
- **Improvement:** +45%

## NEW Entities (28)

### Workflows (7)

1. **WRF-412**: API Integration Workflow
   - **Description:** Connect Claude API to external services
   - **Steps:** 7 steps
   - **Complexity:** Medium
   - **Department:** DEV
   - **Action:** Create new JSON file

2. **WRF-413**: Prompt Template Management
   - **Description:** Organize and version control prompts
   - **Steps:** 5 steps
   - **Complexity:** Low
   - **Department:** AID
   - **Action:** Create new JSON file

...

### Tools (5)

1. **TOL-342**: Claude API (Sonnet 4.5)
   - **Category:** AI Platform
   - **Features:**
     - 200K context window
     - Vision capabilities
     - Function calling
   - **Pricing:** $3/$15 per million tokens
   - **Action:** Create new JSON file

...

### Objects (16)

1. **OBJ-289**: API Response JSON
   - **Type:** Data Structure
   - **Format:** JSON
   - **Size:** Variable
   - **Created By:** TOL-342 (Claude API)
   - **Used In:** WRF-412 (API Integration Workflow)
   - **Action:** Create new JSON file

...

## EXISTING Entities (94)

### Workflows (14)

1. **WRF-001**: Basic API Call Workflow
   - **Status:** In LIBRARIES/Workflows/WRF-001.json
   - **Action:** Cross-reference only

2. **WRF-008**: Design System Creation
   - **Status:** In LIBRARIES/Workflows/WRF-008.json
   - **Action:** Cross-reference only

...

## UPDATE Entities (5)

### Workflows (2)

1. **WRF-003**: Content Generation Workflow
   - **Current:** Basic content generation
   - **Enhancement:** Add Claude API integration steps
   - **Action:** Update JSON + add cross-references

...

## Recommendations

### Immediate Actions (Phase 4)

1. Create 28 NEW entity JSON files
2. Update 5 EXISTING entity JSON files
3. Add bidirectional cross-references (187 links)
4. Validate all JSON schemas

### Coverage Goals

- Target: 95%+ coverage
- Current: 51%
- After integration: 96%
- **Goal achieved:** Yes ✓

### Next Steps

1. Run Phase 4: `python scripts/video_json_updater.py Video_024`
2. Validate JSON files: `python scripts/validate_json_schema.py`
3. Run Phase 5: `python scripts/video_integration_reporter.py Video_024`
```

**JSON Output (Video_024_Gap_Analysis.json):**
```json
{
  "video_id": "Video_024",
  "title": "Claude API Tutorial",
  "analysis_date": "2025-12-04T10:30:00",
  "summary": {
    "total_entities": 127,
    "new_entities": 28,
    "existing_entities": 94,
    "update_entities": 5
  },
  "coverage": {
    "before": 51,
    "after": 96,
    "improvement": 45
  },
  "entities": {
    "workflows": {
      "total": 23,
      "new": [
        {
          "id": "WRF-412",
          "name": "API Integration Workflow",
          "description": "Connect Claude API to external services",
          "steps": 7,
          "complexity": "Medium",
          "department": "DEV"
        }
      ],
      "existing": ["WRF-001", "WRF-008", ...],
      "update": [
        {
          "id": "WRF-003",
          "current": "Basic content generation",
          "enhancement": "Add Claude API integration steps"
        }
      ]
    },
    "tools": { ... },
    "objects": { ... }
  },
  "recommendations": {
    "create_files": 28,
    "update_files": 5,
    "cross_references": 187
  }
}
```

**Functionality:**

1. ✅ Reads Video_XXX.md file
2. ✅ Extracts all entities (7 types)
3. ✅ Scans LIBRARIES/ for existing entities
4. ✅ Compares names, descriptions, attributes
5. ✅ Categorizes as NEW/EXISTING/UPDATE
6. ✅ Calculates coverage metrics
7. ✅ Generates detailed report
8. ✅ Saves to multiple formats

**Comparison Logic:**

```python
def compare_entity(video_entity, library_entities):
    # 1. Exact match (ID exists)
    if video_entity.id in library_entities:
        return "EXISTING"

    # 2. Name match (case-insensitive, fuzzy)
    for lib_entity in library_entities:
        similarity = fuzzy_match(video_entity.name, lib_entity.name)
        if similarity > 0.85:  # 85% similarity threshold
            return "EXISTING"

    # 3. Description match (semantic similarity)
    for lib_entity in library_entities:
        semantic_score = semantic_similarity(
            video_entity.description,
            lib_entity.description
        )
        if semantic_score > 0.75:  # 75% semantic similarity
            return "EXISTING"

    # 4. Attribute match (70%+ attributes same)
    for lib_entity in library_entities:
        attr_match = attribute_overlap(video_entity, lib_entity)
        if attr_match > 0.70:
            return "UPDATE"  # Similar but different

    # 5. No match found
    return "NEW"
```

---

### 11. video_json_updater.py

**Purpose:** Semi-automate Phase 4 JSON file creation and integration

**Location:** `scripts/video_json_updater.py`

**Usage:**

```bash
# Interactive mode (recommended)
python scripts/video_json_updater.py <video_number>

# Auto mode (create all NEW entities automatically)
python scripts/video_json_updater.py <video_number> --auto

# Specific entity types only
python scripts/video_json_updater.py <video_number> --types workflows,tools

# Dry run
python scripts/video_json_updater.py <video_number> --dry-run
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_number | Yes | Integer | Video number | 24 |
| --auto | No | Flag | Automatic JSON creation | |
| --types | No | List | Specific entity types | "workflows,tools" |
| --dry-run | No | Flag | Preview without creating | |
| --validate | No | Flag | Validate JSON schemas | |

**Examples:**

```bash
# Interactive mode (step-by-step)
python scripts/video_json_updater.py 24

# Automatic mode (no prompts)
python scripts/video_json_updater.py 24 --auto

# Only workflows and tools
python scripts/video_json_updater.py 24 --types workflows,tools

# Preview what would be created
python scripts/video_json_updater.py 24 --dry-run

# Create and validate
python scripts/video_json_updater.py 24 --auto --validate
```

**Interactive Mode Output:**

```
Video JSON Integration
======================
Video: Video_024
Gap Analysis: Found (28 NEW, 5 UPDATE)

Processing NEW Entities
=======================

Workflows (7 NEW)
-----------------

1/7: WRF-412 - API Integration Workflow

Proposed JSON:
{
  "entity_id": "WRF-412",
  "name": "API Integration Workflow",
  "type": "Workflow",
  "description": "Connect Claude API to external services",
  "steps": [
    "Configure API credentials",
    "Initialize client",
    "Create request payload",
    "Send API call",
    "Handle response",
    "Error handling",
    "Log transaction"
  ],
  "complexity": "Medium",
  "duration": "30-45 minutes",
  "required_skills": ["SKL-023", "SKL-034"],
  "uses_tools": ["TOL-342", "TOL-001"],
  "creates_objects": ["OBJ-289", "OBJ-290"],
  "department": "DEV",
  "metadata": {
    "source_video": "Video_024",
    "date_added": "2025-12-04",
    "status": "Active"
  }
}

Actions:
1. Create as shown
2. Edit before creating
3. Skip this entity
4. View template
5. Add cross-references

Choice: 1

✓ Created: LIBRARIES/Workflows/WRF-412.json
✓ Added cross-references:
  - TOL-342: Added to "used_in_workflows"
  - SKL-023: Added to "required_for_workflows"

2/7: WRF-413 - Prompt Template Management
...

Tools (5 NEW)
-------------

1/5: TOL-342 - Claude API (Sonnet 4.5)

Proposed JSON:
{
  "entity_id": "TOL-342",
  "name": "Claude API (Sonnet 4.5)",
  "type": "Tool",
  "category": "AI Platform",
  "subcategory": "Language Model",
  "features": [
    "200K context window",
    "Vision capabilities",
    "Function calling",
    "JSON mode",
    "Streaming responses"
  ],
  "pricing": {
    "input": "$3 per million tokens",
    "output": "$15 per million tokens"
  },
  "capabilities": [
    "Text generation",
    "Code generation",
    "Image analysis",
    "Function execution"
  ],
  "creates_objects": ["OBJ-289", "OBJ-290", "OBJ-291"],
  "used_in_workflows": ["WRF-412", "WRF-413", "WRF-414"],
  "requires_skills": ["SKL-023", "SKL-034"],
  "department": "AID",
  "metadata": {
    "source_video": "Video_024",
    "date_added": "2025-12-04",
    "status": "Active",
    "url": "https://docs.anthropic.com/claude/reference/"
  }
}

Actions:
1. Create as shown
2. Edit before creating
3. Skip this entity

Choice: 1

✓ Created: LIBRARIES/Tools/TOL-342.json
✓ Added cross-references:
  - WRF-412: Added to "uses_tools"
  - OBJ-289: Added to "created_by"

...

Processing UPDATE Entities (5)
================================

1/5: WRF-003 - Content Generation Workflow

Current JSON:
{
  "entity_id": "WRF-003",
  "name": "Content Generation Workflow",
  "description": "Basic content generation process",
  "steps": ["Research", "Outline", "Write", "Edit"]
}

Proposed Updates:
{
  "description": "Content generation with Claude API integration",
  "steps": [
    "Research topic",
    "Create prompt template",
    "Initialize Claude API",    ← NEW
    "Generate content",         ← NEW
    "Review output",
    "Edit and refine",
    "Finalize"
  ],
  "uses_tools": ["TOL-342", "TOL-001"],  ← NEW
  "creates_objects": ["OBJ-289"]         ← NEW
}

Actions:
1. Apply updates
2. Edit updates
3. Skip this entity

Choice: 1

✓ Updated: LIBRARIES/Workflows/WRF-003.json
✓ Added cross-references

...

Summary
=======
NEW Entities Created: 28
  - Workflows: 7
  - Tools: 5
  - Objects: 16

UPDATE Entities Modified: 5
  - Workflows: 2
  - Tools: 1
  - Objects: 2

Total Files Modified: 33
Cross-References Added: 187 (bidirectional)

Validation
==========
✓ All JSON schemas valid
✓ All IDs unique
✓ All cross-references bidirectional
✓ No orphaned references

Integration Log
===============
✓ Updated: LIBRARIES/Integration_Log.csv
✓ Video_024 marked as integrated

Processing Time: 12m 45s
```

**Auto Mode Output:**

```bash
python scripts/video_json_updater.py 24 --auto

Video JSON Integration (Auto Mode)
===================================
Video: Video_024
Gap Analysis: Found (28 NEW, 5 UPDATE)

Creating JSON files...
Progress: [████████████████████] 100% (28/28 entities)

✓ Created: 28 JSON files
✓ Updated: 5 JSON files
✓ Cross-references: 187 (bidirectional)
✓ Validation: All schemas valid
✓ Integration log updated

Processing Time: 2m 15s
```

**Functionality:**

1. ✅ Reads gap analysis report
2. ✅ Generates JSON from templates
3. ✅ Interactive or automatic mode
4. ✅ Validates JSON schemas
5. ✅ Adds bidirectional cross-references
6. ✅ Updates existing entities
7. ✅ Logs all changes
8. ✅ Creates backups

**JSON Templates Used:**

```python
TEMPLATES = {
    "Tool": {
        "entity_id": "",
        "name": "",
        "type": "Tool",
        "category": "",
        "features": [],
        "creates_objects": [],
        "used_in_workflows": [],
        "requires_skills": [],
        "metadata": {}
    },
    "Workflow": {
        "entity_id": "",
        "name": "",
        "type": "Workflow",
        "description": "",
        "steps": [],
        "complexity": "",
        "uses_tools": [],
        "creates_objects": [],
        "required_skills": [],
        "metadata": {}
    },
    # ... other templates
}
```

---

### 12. video_integration_reporter.py

**Purpose:** Automate Phase 5 comprehensive integration reporting

**Location:** `scripts/video_integration_reporter.py`

**Usage:**

```bash
# Generate standard report
python scripts/video_integration_reporter.py <video_number>

# Include detailed cross-references
python scripts/video_integration_reporter.py <video_number> --include-cross-refs

# Generate business value analysis
python scripts/video_integration_reporter.py <video_number> --business-value

# All options
python scripts/video_integration_reporter.py <video_number> --all
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| video_number | Yes | Integer | Video number | 24 |
| --include-cross-refs | No | Flag | Include cross-reference map | |
| --business-value | No | Flag | Include business analysis | |
| --all | No | Flag | Include all optional sections | |
| --format | No | String | Output format (markdown, pdf, both) | "both" |

**Examples:**

```bash
# Basic report
python scripts/video_integration_reporter.py 24

# Detailed report with cross-references
python scripts/video_integration_reporter.py 24 --include-cross-refs

# Business value analysis
python scripts/video_integration_reporter.py 24 --business-value

# Complete comprehensive report
python scripts/video_integration_reporter.py 24 --all

# Generate PDF
python scripts/video_integration_reporter.py 24 --all --format pdf
```

**Output:**

**Console Output:**
```
Video Integration Report
========================
Video: Video_024
Title: Claude API Tutorial

Generating report sections...
✓ Executive summary
✓ Coverage metrics
✓ Entity lists (NEW/EXISTING/UPDATE)
✓ Cross-reference map (187 links)
✓ Business value analysis
✓ Department impact
✓ Recommendations

Report saved: 04_INTEGRATION_LOGS/Video_024_Library_Mapping_Report.md
Processing Time: 2m 18s
```

**Report Contents (Video_024_Library_Mapping_Report.md):**

```markdown
# Library Mapping Report: Video_024

**Video:** Video_024 - Claude API Tutorial
**Channel:** Anthropic
**Duration:** 15:32
**Date Processed:** 2025-12-04
**Employee:** John Doe
**Report Generated:** 2025-12-04 16:45:00

---

## Executive Summary

Video_024 processing has been completed successfully across all 7 phases. The video contributed **28 NEW entities** to the LIBRARIES system, improving overall coverage by **45%** (from 51% to 96%). This video focused on Claude API integration, workflows, and automation patterns.

**Key Achievements:**
- ✅ 127 total entities identified
- ✅ 28 NEW entities created (22%)
- ✅ 94 EXISTING entities cross-referenced (74%)
- ✅ 5 entities enhanced with updates (4%)
- ✅ 187 bidirectional cross-references added
- ✅ Coverage improvement: +45%

---

## Coverage Metrics

### Overall Coverage

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Total Entities in LIBRARIES | 185 | 213 | +28 (+15%) |
| Coverage % | 51% | 96% | +45% |
| Workflows | 42 | 49 | +7 |
| Tools | 38 | 43 | +5 |
| Objects | 89 | 105 | +16 |
| Actions | 234 | 234 | 0 |
| Professions | 45 | 45 | 0 |
| Skills | 67 | 67 | 0 |
| Departments | 12 | 12 | 0 |

### Video Entity Breakdown

| Entity Type | Total | NEW | EXISTING | UPDATE |
|-------------|-------|-----|----------|--------|
| Workflows | 23 | 7 (30%) | 14 (61%) | 2 (9%) |
| Tools | 18 | 5 (28%) | 12 (67%) | 1 (6%) |
| Objects | 42 | 16 (38%) | 24 (57%) | 2 (5%) |
| Actions | 28 | 0 (0%) | 28 (100%) | 0 (0%) |
| Professions | 8 | 0 (0%) | 8 (100%) | 0 (0%) |
| Skills | 6 | 0 (0%) | 6 (100%) | 0 (0%) |
| Departments | 2 | 0 (0%) | 2 (100%) | 0 (0%) |
| **TOTAL** | **127** | **28** | **94** | **5** |

---

## NEW Entities (28)

### Workflows (7)

| ID | Name | Complexity | Department | JSON File |
|----|------|------------|------------|-----------|
| WRF-412 | API Integration Workflow | Medium | DEV | ✓ Created |
| WRF-413 | Prompt Template Management | Low | AID | ✓ Created |
| WRF-414 | Response Processing Pipeline | Medium | DEV | ✓ Created |
| WRF-415 | Error Handling Strategy | Low | DEV | ✓ Created |
| WRF-416 | Streaming Response Management | High | DEV | ✓ Created |
| WRF-417 | Function Calling Setup | Medium | DEV | ✓ Created |
| WRF-418 | Vision Analysis Workflow | Medium | AID | ✓ Created |

### Tools (5)

| ID | Name | Category | Department | JSON File |
|----|------|----------|------------|-----------|
| TOL-342 | Claude API (Sonnet 4.5) | AI Platform | AID | ✓ Created |
| TOL-343 | Claude SDK (Python) | Development Library | DEV | ✓ Created |
| TOL-344 | Anthropic Console | Management Platform | AID | ✓ Created |
| TOL-345 | Prompt Caching System | Optimization Tool | DEV | ✓ Created |
| TOL-346 | Token Counter | Utility Tool | DEV | ✓ Created |

### Objects (16)

| ID | Name | Type | Created By | JSON File |
|----|------|------|------------|-----------|
| OBJ-289 | API Response JSON | Data Structure | TOL-342 | ✓ Created |
| OBJ-290 | Prompt Template | Document | TOL-342 | ✓ Created |
| OBJ-291 | Function Definition | Code | TOL-343 | ✓ Created |
| OBJ-292 | Streaming Chunk | Data Structure | TOL-342 | ✓ Created |
| OBJ-293 | Error Log | Document | TOL-342 | ✓ Created |
| OBJ-294 | Token Usage Report | Report | TOL-346 | ✓ Created |
| OBJ-295 | API Credentials | Configuration | TOL-342 | ✓ Created |
| OBJ-296 | Request Payload | Data Structure | TOL-342 | ✓ Created |
| OBJ-297 | Vision Analysis Result | Data Structure | TOL-342 | ✓ Created |
| OBJ-298 | Cached Prompt | Data Structure | TOL-345 | ✓ Created |
| OBJ-299 | Function Response | Data Structure | TOL-342 | ✓ Created |
| OBJ-300 | System Prompt | Document | TOL-342 | ✓ Created |
| OBJ-301 | Conversation History | Data Structure | TOL-342 | ✓ Created |
| OBJ-302 | Rate Limit Status | Data Structure | TOL-342 | ✓ Created |
| OBJ-303 | Model Configuration | Configuration | TOL-342 | ✓ Created |
| OBJ-304 | API Key | Configuration | TOL-344 | ✓ Created |

---

## EXISTING Entities (94)

Successfully cross-referenced with existing LIBRARIES entities. Full list available in gap analysis report.

**Top Cross-Referenced Entities:**

1. **WRF-001**: Basic API Call Workflow (12 new cross-references)
2. **TOL-001**: ChatGPT API (8 new cross-references)
3. **SKL-023**: API Integration (15 new cross-references)
4. **ACT-042**: Generate text (23 new cross-references)
5. **DPT-DEV**: Development Department (28 new cross-references)

---

## UPDATE Entities (5)

| ID | Name | Enhancement | Status |
|----|------|-------------|--------|
| WRF-003 | Content Generation Workflow | Added Claude API integration steps | ✓ Updated |
| WRF-008 | Design System Creation | Added AI-assisted design steps | ✓ Updated |
| TOL-001 | ChatGPT API | Added comparison with Claude API | ✓ Updated |
| OBJ-023 | API Response | Enhanced with Claude-specific fields | ✓ Updated |
| OBJ-045 | Error Message | Added Claude error codes | ✓ Updated |

---

## Cross-Reference Map (187 Links)

### Tool → Workflow Relationships

**TOL-342 (Claude API)** used in:
- WRF-412: API Integration Workflow
- WRF-413: Prompt Template Management
- WRF-414: Response Processing Pipeline
- WRF-416: Streaming Response Management
- WRF-417: Function Calling Setup
- WRF-418: Vision Analysis Workflow
- WRF-003: Content Generation Workflow (updated)

**TOL-343 (Claude SDK)** used in:
- WRF-412: API Integration Workflow
- WRF-417: Function Calling Setup

### Tool → Object Relationships

**TOL-342 (Claude API)** creates:
- OBJ-289: API Response JSON
- OBJ-290: Prompt Template
- OBJ-292: Streaming Chunk
- OBJ-293: Error Log
- OBJ-296: Request Payload
- OBJ-297: Vision Analysis Result
- OBJ-299: Function Response
- OBJ-300: System Prompt
- OBJ-301: Conversation History
- OBJ-302: Rate Limit Status
- OBJ-303: Model Configuration

### Workflow → Skill Relationships

**WRF-412 (API Integration Workflow)** requires:
- SKL-023: API Integration
- SKL-034: Python Programming
- SKL-045: Error Handling
- SKL-056: JSON Processing

### Department Associations

**DPT-DEV (Development):**
- 15 workflows
- 8 tools
- 32 objects
- Primary focus: API integration, automation

**DPT-AID (AI Department):**
- 8 workflows
- 5 tools
- 18 objects
- Primary focus: AI implementation, prompt engineering

---

## Business Value Analysis

### Impact on Departments

| Department | New Workflows | New Tools | Coverage Gain | Business Impact |
|------------|---------------|-----------|---------------|-----------------|
| DEV | 5 | 3 | +42% | High - API integration patterns |
| AID | 2 | 2 | +38% | High - AI implementation guides |
| DGN | 0 | 0 | +5% | Low - Limited design content |
| SMM | 0 | 0 | +3% | Low - No social media focus |

### Value Propositions

**1. API Integration Capabilities (+$50K/year value)**
- NEW: 7 workflow patterns for Claude API integration
- Estimated time savings: 40 hours/month across dev team
- Reduction in API integration errors: 60%

**2. AI Implementation Knowledge (+$35K/year value)**
- NEW: 5 tools documented for AI development
- Faster onboarding for AI projects: 50% reduction
- Standardized prompt templates reduce rework: 30%

**3. Automation Patterns (+$25K/year value)**
- NEW: 16 objects for automation workflows
- Reusable components reduce development time: 25%
- Cross-references improve discoverability: 80%

**Total Estimated Annual Value: $110K**

### ROI Analysis

- **Investment:** 2h 15m processing time (1 employee)
- **Cost:** ~$85 (assuming $75/hour fully loaded)
- **Annual Value:** $110,000
- **ROI:** 129,300%
- **Payback Period:** <1 day

---

## Recommendations

### Immediate Actions (Complete)

- [x] Create 28 NEW entity JSON files
- [x] Update 5 EXISTING entity JSON files
- [x] Add 187 bidirectional cross-references
- [x] Validate all JSON schemas
- [x] Update Integration_Log.csv
- [x] Mark Video_024 as "Complete"

### Quality Validation

- [x] All JSON schemas valid
- [x] All IDs unique (WRF-412 through WRF-418, TOL-342 through TOL-346, OBJ-289 through OBJ-304)
- [x] All cross-references bidirectional
- [x] No orphaned references
- [x] Coverage target achieved (96% > 95%)

### Next Videos

Based on gap analysis, prioritize videos covering:

1. **Error Handling Patterns** - Current coverage: 42%
2. **Testing Strategies** - Current coverage: 38%
3. **Deployment Workflows** - Current coverage: 51%

Recommended queue:
- VQ-025: Testing Automation Tutorial (Priority: 82)
- VQ-027: Error Handling Best Practices (Priority: 79)
- VQ-031: CI/CD Pipeline Setup (Priority: 76)

---

## Processing Timeline

| Phase | Start | End | Duration | Status |
|-------|-------|-----|----------|--------|
| Phase 0: Search | 2025-12-02 09:00 | 2025-12-02 10:30 | 1h 30m | ✓ Complete |
| Phase 0→1: Queue | 2025-12-02 10:30 | 2025-12-02 10:45 | 15m | ✓ Complete |
| Phase 1: Transcription | 2025-12-03 14:00 | 2025-12-03 16:15 | 2h 15m | ✓ Complete |
| Phase 2: Extraction | 2025-12-04 09:00 | 2025-12-04 09:45 | 45m | ✓ Complete |
| Phase 3: Gap Analysis | 2025-12-04 10:00 | 2025-12-04 10:03 | 3m | ✓ Complete (automated) |
| Phase 4: Integration | 2025-12-04 10:30 | 2025-12-04 11:45 | 1h 15m | ✓ Complete |
| Phase 5: Mapping | 2025-12-04 14:00 | 2025-12-04 14:02 | 2m | ✓ Complete (automated) |
| **TOTAL** | | | **6h 20m** | ✓ Complete |

---

## Files Created

### Video Processing Files

1. `02_TRANSCRIPTIONS/Video_024.md` (15,234 words)
2. `03_VIDEO_ENTITIES/Video_024_Phase3_Analysis.md` (3,456 words)
3. `03_VIDEO_ENTITIES/Video_024_Phase4_Objects.md` (2,123 words)
4. `03_VIDEO_ENTITIES/Video_024_Gap_Analysis.md` (4,567 words)
5. `04_INTEGRATION_LOGS/Video_024_Library_Mapping_Report.md` (this file)

### Library JSON Files (28 NEW)

**Workflows (7):**
- LIBRARIES/Workflows/WRF-412.json
- LIBRARIES/Workflows/WRF-413.json
- LIBRARIES/Workflows/WRF-414.json
- LIBRARIES/Workflows/WRF-415.json
- LIBRARIES/Workflows/WRF-416.json
- LIBRARIES/Workflows/WRF-417.json
- LIBRARIES/Workflows/WRF-418.json

**Tools (5):**
- LIBRARIES/Tools/TOL-342.json
- LIBRARIES/Tools/TOL-343.json
- LIBRARIES/Tools/TOL-344.json
- LIBRARIES/Tools/TOL-345.json
- LIBRARIES/Tools/TOL-346.json

**Objects (16):**
- LIBRARIES/Objects/OBJ-289.json
- LIBRARIES/Objects/OBJ-290.json
- ... (OBJ-291 through OBJ-304)

### Updated Library JSON Files (5)

- LIBRARIES/Workflows/WRF-003.json
- LIBRARIES/Workflows/WRF-008.json
- LIBRARIES/Tools/TOL-001.json
- LIBRARIES/Objects/OBJ-023.json
- LIBRARIES/Objects/OBJ-045.json

---

## Conclusion

Video_024 processing represents a **highly successful integration** that significantly improved library coverage in API integration and AI implementation domains. The 45% coverage improvement and 187 new cross-references substantially enhance the discoverability and utility of the LIBRARIES system.

**Key Success Factors:**
- Comprehensive 7-phase workflow execution
- High-quality source material (Anthropic official)
- Effective gap analysis automation
- Thorough cross-referencing
- Detailed business value analysis

**Estimated Impact:**
- Annual value: $110,000
- ROI: 129,300%
- Department coverage: +40% (DEV), +38% (AID)
- Knowledge base completeness: 96%

**Status:** 🎉 **COMPLETE**

---

**Report Generated By:** video_integration_reporter.py v2.1
**Generated:** 2025-12-04 16:45:00
**Processing Time:** 2m 18s
```

**Functionality:**

1. ✅ Reads all phase outputs
2. ✅ Calculates comprehensive metrics
3. ✅ Maps all cross-references
4. ✅ Analyzes business value
5. ✅ Generates detailed report
6. ✅ Creates visualizations
7. ✅ Saves to multiple formats
8. ✅ Updates progress tracker to "Complete"

---

### 13. update_video_progress.py

**Purpose:** Track video processing progress through all phases

**Location:** `scripts/update_video_progress.py`

**Usage:**

```bash
# Add video to tracker
python scripts/update_video_progress.py add <video_number> <title> <youtube_url> <employee>

# Update phase
python scripts/update_video_progress.py update <video_number> <phase_name> [notes]

# View progress
python scripts/update_video_progress.py view [video_number]

# View statistics
python scripts/update_video_progress.py stats
```

**Parameters:**

| Command | Parameters | Description | Example |
|---------|------------|-------------|---------|
| add | video_number, title, url, employee | Add new video to tracker | add 24 "Claude Tutorial" "url" "John" |
| update | video_number, phase, notes | Update to next phase | update 24 Phase_1_Transcribed |
| view | video_number (optional) | View progress | view 24 |
| stats | - | View overall statistics | stats |

**Examples:**

```bash
# Add new video
python scripts/update_video_progress.py add 24 "Claude API Tutorial" "https://youtube.com/watch?v=abc123" "John Doe"

# Update to Phase 1
python scripts/update_video_progress.py update 24 Phase_1_Transcribed "Used PMT-004, extracted 37 entities"

# Update to Phase 2
python scripts/update_video_progress.py update 24 Phase_2_Extraction "Deep dive with PMT-007"

# Update to Phase 3
python scripts/update_video_progress.py update 24 Phase_3_Gap_Analysis "28 NEW, 94 EXISTING, 5 UPDATE"

# Update to Phase 4
python scripts/update_video_progress.py update 24 Phase_4_Integration "Created 28 JSON files"

# Update to Phase 5
python scripts/update_video_progress.py update 24 Phase_5_Mapping "Coverage: 51% → 96%"

# Mark complete
python scripts/update_video_progress.py update 24 Complete "All phases finished successfully"

# View specific video
python scripts/update_video_progress.py view 24

# View all videos
python scripts/update_video_progress.py view

# View statistics
python scripts/update_video_progress.py stats
```

**Output:**

**Add Video:**
```
Adding Video_024 to progress tracker...
✓ Video_024 added successfully
✓ Status: Phase_0_Queued
✓ Employee: John Doe
```

**Update Phase:**
```
Updating Video_024 progress...
✓ Phase updated: Phase_1_Transcribed
✓ Date: 2025-12-04 10:30:00
✓ Notes: Used PMT-004, extracted 37 entities
```

**View Progress:**
```
Video Progress: Video_024
==========================
Title: Claude API Tutorial
YouTube: https://youtube.com/watch?v=abc123
Employee: John Doe
Status: Phase_4_Integration (80% complete)

Phase Timeline:
---------------
✓ Phase_0_Queued        2025-12-02 09:00
✓ Phase_1_Transcribed   2025-12-03 14:00 (1 day 5h)
✓ Phase_2_Extraction    2025-12-04 09:00 (19h)
✓ Phase_3_Gap_Analysis  2025-12-04 10:00 (1h)
→ Phase_4_Integration   2025-12-04 10:30 (In Progress)
  Phase_5_Mapping       (Pending)
  Complete              (Pending)

Total Processing Time: 2 days 1h 30m
Estimated Completion: 2025-12-04 16:00
```

**View All Videos:**
```
Video Progress Tracker
======================
Total Videos: 28

Active Videos (5):
------------------
Video_024: Phase_4_Integration (80%) - John Doe
Video_025: Phase_2_Extraction (40%) - Jane Smith
Video_026: Phase_1_Transcribed (20%) - Mike Johnson

Recent Completions (3):
-----------------------
Video_023: Complete (2025-12-01) - 3 days processing
Video_022: Complete (2025-11-30) - 2 days processing
Video_021: Complete (2025-11-29) - 4 days processing

Pending Videos (20):
--------------------
Video_027 through Video_046 (Phase_0_Queued)
```

**Statistics:**
```
Progress Statistics
===================
Total Videos: 28
Completed: 23 (82%)
In Progress: 5 (18%)

Phase Distribution:
-------------------
Phase_0_Queued: 20 videos
Phase_1_Transcribed: 2 videos
Phase_2_Extraction: 1 video
Phase_3_Gap_Analysis: 0 videos
Phase_4_Integration: 1 video
Phase_5_Mapping: 1 video
Complete: 23 videos

Average Processing Time: 2.8 days
Fastest: Video_015 (1.2 days)
Slowest: Video_008 (5.4 days)

Employee Performance:
---------------------
John Doe: 12 videos (52% completion rate)
Jane Smith: 8 videos (45% completion rate)
Mike Johnson: 8 videos (38% completion rate)
```

**CSV File (VIDEO_PROGRESS_TRACKER.csv):**
```csv
Video_Number,Title,YouTube_URL,Employee,Status,Phase_0_Date,Phase_1_Date,Phase_2_Date,Phase_3_Date,Phase_4_Date,Phase_5_Date,Complete_Date,Total_Days,Notes
024,Claude API Tutorial,https://youtube.com/watch?v=abc123,John Doe,Phase_4_Integration,2025-12-02 09:00,2025-12-03 14:00,2025-12-04 09:00,2025-12-04 10:00,2025-12-04 10:30,,,2.1,"In progress"
023,ChatGPT Workflows,https://youtube.com/watch?v=def456,Jane Smith,Complete,2025-11-28 10:00,2025-11-29 14:00,2025-11-30 09:00,2025-11-30 10:00,2025-12-01 11:00,2025-12-01 14:00,2025-12-01 16:00,3.2,"Successfully completed"
```

**Functionality:**

1. ✅ Tracks videos through 7 phases
2. ✅ Records dates for each phase
3. ✅ Calculates total processing time
4. ✅ Tracks employee assignments
5. ✅ Stores notes for each phase
6. ✅ Shows completion percentage
7. ✅ Generates statistics

---

### 14. generate_progress_report.py

**Purpose:** Generate comprehensive progress reports

**Location:** `scripts/generate_progress_report.py`

**Usage:**

```bash
# Generate specific report
python scripts/generate_progress_report.py <type>

# Custom date range
python scripts/generate_progress_report.py <type> --from YYYY-MM-DD --to YYYY-MM-DD

# Export format
python scripts/generate_progress_report.py <type> --format <format>
```

**Parameters:**

| Parameter | Required | Type | Description | Example |
|-----------|----------|------|-------------|---------|
| type | Yes | String | Report type (summary, detailed, weekly, monthly, all) | "weekly" |
| --from | No | Date | Start date | "2025-12-01" |
| --to | No | Date | End date | "2025-12-04" |
| --format | No | String | Output format (markdown, pdf, html, json) | "pdf" |
| --output | No | Path | Output directory | "./reports/" |

**Report Types:**

1. **summary** - Overall summary with statistics
2. **detailed** - Detailed report for all videos
3. **weekly** - Weekly activity report
4. **monthly** - Monthly summary report
5. **all** - Generate all report types

**Examples:**

```bash
# Generate summary report
python scripts/generate_progress_report.py summary

# Generate weekly report
python scripts/generate_progress_report.py weekly

# Generate detailed report for date range
python scripts/generate_progress_report.py detailed --from 2025-12-01 --to 2025-12-04

# Generate all reports as PDF
python scripts/generate_progress_report.py all --format pdf

# Custom output location
python scripts/generate_progress_report.py monthly --output "./monthly_reports/"
```

**Output:**

**Summary Report:**
```markdown
# RESEARCHES 2 Progress Summary

**Report Date:** 2025-12-04
**Period:** All Time

## Overview

- **Total Videos:** 28
- **Completed:** 23 (82%)
- **In Progress:** 5 (18%)
- **Average Processing Time:** 2.8 days
- **Total Entities Created:** 487 NEW entities
- **Coverage Improvement:** +38% average

## Phase Distribution

| Phase | Count | % of Total |
|-------|-------|------------|
| Phase_0_Queued | 20 | 71% |
| Phase_1_Transcribed | 2 | 7% |
| Phase_2_Extraction | 1 | 4% |
| Phase_3_Gap_Analysis | 0 | 0% |
| Phase_4_Integration | 1 | 4% |
| Phase_5_Mapping | 1 | 4% |
| Complete | 23 | 82% |

## Employee Performance

| Employee | Videos | Completed | In Progress | Avg Time | Completion Rate |
|----------|--------|-----------|-------------|----------|-----------------|
| John Doe | 12 | 11 | 1 | 2.5 days | 92% |
| Jane Smith | 8 | 7 | 1 | 2.9 days | 88% |
| Mike Johnson | 8 | 5 | 3 | 3.2 days | 63% |

## Recent Activity (Last 7 Days)

- Videos Completed: 5
- Videos Started: 3
- Entities Created: 127 NEW
- Coverage Gain: +42%

## System Statistics

- Total Workflows: 89 (+23 this period)
- Total Tools: 67 (+12 this period)
- Total Objects: 234 (+78 this period)
- Total Cross-References: 1,247 (+187 this period)
```

**Weekly Report:**
```markdown
# Weekly Progress Report

**Week:** December 1-7, 2025
**Report Generated:** 2025-12-04

## Week Summary

- **Videos Completed:** 5
- **Videos Started:** 3
- **Videos In Progress:** 5
- **Total Processing Time:** 14.2 days
- **NEW Entities:** 127

## Completed Videos This Week

### Video_023: ChatGPT Workflows
- **Completed:** 2025-12-01
- **Duration:** 3.2 days
- **Employee:** Jane Smith
- **Entities:** 23 NEW, 87 EXISTING, 4 UPDATE
- **Coverage:** +38%

### Video_024: Claude API Tutorial
- **Completed:** 2025-12-04 (in progress)
- **Duration:** 2.1 days (so far)
- **Employee:** John Doe
- **Entities:** 28 NEW, 94 EXISTING, 5 UPDATE
- **Coverage:** +45%

...

## Daily Activity

### Monday, Dec 1
- Video_023 completed (Jane Smith)
- Video_025 started (Mike Johnson)

### Tuesday, Dec 2
- Video_024 started (John Doe)
- Video_026 started (Jane Smith)

### Wednesday, Dec 3
- Video_024 Phase 1 complete
- Video_025 Phase 2 complete

### Thursday, Dec 4
- Video_024 Phase 4 complete
- Video_027 started

## Metrics

### Processing Speed
- Average time per video: 2.8 days
- Fastest completion: Video_023 (3.2 days)
- Current capacity: 1.8 videos/week

### Entity Creation
- Workflows: +23
- Tools: +12
- Objects: +78
- Total: +127 NEW entities

### Coverage Improvement
- Week start: 58%
- Week end: 73%
- Improvement: +15%

## Upcoming Week Priorities

1. Complete Video_024 (Phase 5)
2. Complete Video_025 (Phases 3-5)
3. Start Video_028, Video_029, Video_030
4. Target: 3-4 completions next week
```

**Detailed Report:**
```markdown
# Detailed Video Processing Report

**Report Date:** 2025-12-04
**Videos Included:** All (28)

---

## Video_001: Introduction to AI Automation

**Status:** ✓ Complete
**Employee:** John Doe
**YouTube:** https://youtube.com/watch?v=...

### Timeline
- Phase_0_Queued: 2025-10-15 09:00
- Phase_1_Transcribed: 2025-10-16 14:00 (1 day 5h)
- Phase_2_Extraction: 2025-10-17 09:00 (19h)
- Phase_3_Gap_Analysis: 2025-10-17 10:00 (1h)
- Phase_4_Integration: 2025-10-17 14:00 (4h)
- Phase_5_Mapping: 2025-10-18 09:00 (19h)
- Complete: 2025-10-18 11:00 (2h)

**Total Time:** 3.1 days

### Entities
- Workflows: 5 NEW, 12 EXISTING, 1 UPDATE
- Tools: 3 NEW, 8 EXISTING, 0 UPDATE
- Objects: 12 NEW, 23 EXISTING, 2 UPDATE
- **Total:** 20 NEW, 43 EXISTING, 3 UPDATE

### Coverage Impact
- Before: 42%
- After: 67%
- Improvement: +25%

### Files Created
- Video_001.md
- Video_001_Gap_Analysis.md
- Video_001_Library_Mapping_Report.md
- 20 JSON files

### Notes
Successfully completed all phases. High-quality source material from official channel.

---

## Video_002: Advanced Prompt Engineering

[Similar detailed breakdown for each video...]

---

## Summary Statistics

- Total Videos: 28
- Completed: 23
- Average Time: 2.8 days
- Total Entities: 487 NEW
- Coverage: 42% → 87% (+45%)
```

**Functionality:**

1. ✅ Generates multiple report types
2. ✅ Customizable date ranges
3. ✅ Multiple output formats
4. ✅ Detailed statistics
5. ✅ Employee performance metrics
6. ✅ Coverage analysis
7. ✅ Saves to REPORTS/ folder

---

## Common Workflows

### Workflow 1: Complete Video Processing (7 Phases)

```bash
# Step 1: View queue and select video
python 01_VIDEO_QUEUE/video_queue_manager.py

# Step 2: Add to progress tracker
python scripts/update_video_progress.py add 24 "Claude Tutorial" "URL" "John Doe"

# Step 3: Update status to Selected
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-024 Selected "John Doe"

# Step 4: Phase 1 - Transcribe (manual with PMT-004)
# ... Use PMT-004 prompt with AI ...
python scripts/update_video_progress.py update 24 Phase_1_Transcribed "37 entities extracted"

# Step 5: Phase 2 - Extract (manual with PMT-007)
# ... Use PMT-007 prompt with AI ...
python scripts/update_video_progress.py update 24 Phase_2_Extraction "Deep extraction complete"

# Step 6: Phase 3 - Gap Analysis (automated)
python scripts/video_gap_analyzer.py 24
python scripts/update_video_progress.py update 24 Phase_3_Gap_Analysis "28 NEW, 94 EXISTING"

# Step 7: Phase 4 - Integration (semi-automated)
python scripts/video_json_updater.py 24 --auto
python scripts/update_video_progress.py update 24 Phase_4_Integration "28 JSON files created"

# Step 8: Phase 5 - Mapping (automated)
python scripts/video_integration_reporter.py 24 --all
python scripts/update_video_progress.py update 24 Phase_5_Mapping "Coverage +45%"

# Step 9: Mark complete
python scripts/update_video_progress.py update 24 Complete "All phases successful"
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-024 Completed "John Doe"

# Step 10: Generate report
python scripts/generate_progress_report.py weekly
```

### Workflow 2: Batch Video Addition

```bash
# Create file with video URLs
cat > video_urls.txt << EOF
https://youtube.com/watch?v=abc123
https://youtube.com/watch?v=def456
https://youtube.com/watch?v=ghi789
EOF

# Add all videos to queue
while read url; do
    python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py "$url" "John Doe" "Claude AI" "Batch Import"
done < video_urls.txt

# Recalculate priorities
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --all
```

### Workflow 3: Daily Queue Management

```bash
# Morning: View queue statistics
python 01_VIDEO_QUEUE/video_queue_manager.py
# Select option 1 (View Queue Statistics)

# Calculate/update priorities
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --status Queued

# Export daily report
python 01_VIDEO_QUEUE/scripts/export_queue.py markdown > daily_queue_$(date +%Y-%m-%d).md

# Review top priority videos
python 01_VIDEO_QUEUE/scripts/export_queue.py json --output "./priority_videos.json"
```

### Workflow 4: Weekly Reporting

```bash
# Generate all reports
python scripts/generate_progress_report.py weekly
python scripts/generate_progress_report.py summary

# Export queue status
python 01_VIDEO_QUEUE/scripts/export_queue.py all

# View progress statistics
python scripts/update_video_progress.py stats
```

---

## Troubleshooting

### Common Issues

**1. ImportError: No module named 'pandas'**
```bash
# Solution: Install dependencies
pip install pandas requests python-dateutil yt-dlp
```

**2. FileNotFoundError: Video_XXX.md not found**
```bash
# Solution: Verify file location
ls 02_TRANSCRIPTIONS/Video_024.md

# If missing, file was not created in Phase 1
# Re-run Phase 1 transcription with PMT-004
```

**3. KeyError: 'entity_id' in JSON file**
```bash
# Solution: Validate JSON schema
python scripts/validate_json_schema.py LIBRARIES/Tools/TOL-342.json

# Fix JSON structure using template
python scripts/fix_json_schema.py TOL-342
```

**4. DuplicateIDError: WRF-412 already exists**
```bash
# Solution: Check existing IDs
python scripts/video_id_scanner.py --check WRF-412

# Use next available ID
python scripts/get_next_id.py Workflows
# Returns: WRF-419
```

**5. CrossReferenceError: Broken bidirectional link**
```bash
# Solution: Validate cross-references
python scripts/validate_cross_refs.py

# Fix automatically
python scripts/fix_cross_refs.py --auto
```

**6. YouTube API rate limit**
```bash
# Solution: Use yt-dlp directly
yt-dlp --get-title --get-duration "https://youtube.com/watch?v=abc123"

# Or use simple add script (no metadata extraction)
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py "URL"
```

**7. Script hangs/freezes**
```bash
# Solution: Run with timeout
timeout 5m python scripts/video_gap_analyzer.py 24

# Or run with verbose output
python scripts/video_gap_analyzer.py 24 --verbose
```

### Error Log Locations

```
RESEARCHES 2/
└── scripts/
    └── logs/
        ├── assign_search.log
        ├── video_queue_manager.log
        ├── video_gap_analyzer.log
        ├── video_json_updater.log
        └── errors.log
```

### Debug Mode

```bash
# Run any script with debug flag
python scripts/process_video.py 24 --all-phases --debug

# View detailed logs
tail -f scripts/logs/process_video.log
```

---

## Script Dependencies

### Dependency Graph

```
┌─────────────────────────┐
│ config.py               │  ← Central configuration
└─────────────────────────┘
           ↓
┌─────────────────────────┐
│ utils.py                │  ← Utility functions
└─────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────┐
│                    All Other Scripts                 │
│ ─────────────────────────────────────────────────── │
│ • assign_search.py                                   │
│ • complete_search.py                                 │
│ • add_video_to_queue.py                             │
│ • video_gap_analyzer.py                             │
│ • video_json_updater.py                             │
│ • video_integration_reporter.py                     │
│ • update_video_progress.py                          │
│ • generate_progress_report.py                       │
└─────────────────────────────────────────────────────┘
```

### config.py Contents

```python
# File paths
BASE_DIR = "G:/Job/REMS/Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES 2"
SEARCH_QUEUE_CSV = f"{BASE_DIR}/00_SEARCH_QUEUE/Search_Queue_Master.csv"
VIDEO_QUEUE_CSV = f"{BASE_DIR}/01_VIDEO_QUEUE/Video_Queue_Master.csv"
TRANSCRIPTIONS_DIR = f"{BASE_DIR}/02_TRANSCRIPTIONS"
VIDEO_ENTITIES_DIR = f"{BASE_DIR}/03_VIDEO_ENTITIES"
INTEGRATION_LOGS_DIR = f"{BASE_DIR}/04_INTEGRATION_LOGS"
LIBRARIES_DIR = "G:/Job/REMS/Dropbox/ENTITIES/LIBRARIES"

# Default values
DEFAULT_EMPLOYEE = "System"
DEFAULT_SOURCE = "Quick Add"
DEFAULT_PRIORITY = 50

# Priority weights
PRIORITY_WEIGHTS = {
    "date": 0.30,
    "source": 0.25,
    "topic": 0.25,
    "engagement": 0.20
}

# Phase names
PHASES = [
    "Phase_0_Queued",
    "Phase_1_Transcribed",
    "Phase_2_Extraction",
    "Phase_3_Gap_Analysis",
    "Phase_4_Integration",
    "Phase_5_Mapping",
    "Complete"
]
```

### utils.py Functions

```python
def generate_id(prefix, existing_ids):
    """Generate next sequential ID (e.g., VQ-001)"""

def validate_youtube_url(url):
    """Validate YouTube URL format"""

def extract_video_id(url):
    """Extract video ID from YouTube URL"""

def format_date(date_obj):
    """Format date as YYYY-MM-DD HH:MM:SS"""

def load_csv(file_path):
    """Load CSV file with pandas"""

def save_csv(df, file_path):
    """Save CSV with backup"""

def fuzzy_match(str1, str2):
    """Calculate string similarity (0-1)"""

def semantic_similarity(text1, text2):
    """Calculate semantic similarity using embeddings"""
```

---

## Maintenance & Updates

### Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025-10-15 | Initial release (8 scripts) |
| v1.5 | 2025-11-01 | Added video_gap_analyzer.py |
| v2.0 | 2025-11-15 | Added video_json_updater.py, video_integration_reporter.py |
| v2.1 | 2025-12-04 | Updated all scripts with error handling |

### Backup Strategy

All scripts create backups before modifying CSV files:

```
RESEARCHES 2/
└── backups/
    ├── Search_Queue_Master_2025-12-04_10-30.csv
    ├── Video_Queue_Master_2025-12-04_11-15.csv
    └── VIDEO_PROGRESS_TRACKER_2025-12-04_14-00.csv
```

### Scheduled Tasks (Recommended)

**Daily (8:00 AM):**
```bash
# Recalculate queue priorities
python 01_VIDEO_QUEUE/scripts/calculate_priority.py --all

# Generate daily summary
python scripts/generate_progress_report.py summary --format html
```

**Weekly (Monday 9:00 AM):**
```bash
# Generate weekly report
python scripts/generate_progress_report.py weekly --format pdf

# Export queue backup
python 01_VIDEO_QUEUE/scripts/export_queue.py all
```

**Monthly (1st of month):**
```bash
# Generate monthly report
python scripts/generate_progress_report.py monthly

# Cleanup old backups (keep 90 days)
find backups/ -name "*.csv" -mtime +90 -delete
```

---

## Performance Optimization

### Automated vs Manual Processing Time

| Phase | Manual (PMT) | Automated (Script) | Time Savings |
|-------|--------------|-------------------|--------------|
| Phase 1 | 1-2 hours | N/A (requires human) | - |
| Phase 2 | 30-45 min | N/A (requires human) | - |
| Phase 3 | 20-30 min | 2-3 minutes | 90% faster |
| Phase 4 | 45-60 min | 2-3 minutes (auto mode) | 95% faster |
| Phase 5 | 30-45 min | 2-3 minutes | 93% faster |

**Total Automation Savings:** ~2 hours per video (phases 3-5)

### Batch Processing

```bash
# Process multiple videos in parallel (GNU parallel)
parallel python scripts/process_video.py {} --phases 3,4,5 ::: 24 25 26

# Or sequentially
for video in 24 25 26; do
    python scripts/process_video.py $video --phases 3,4,5
done
```

---

## Future Enhancements

### Planned Features

1. **AI-Assisted Phase 1-2** (Coming Q1 2026)
   - Automated transcription with Whisper API
   - Auto-extraction with Claude API
   - Reduce Phase 1-2 time by 50%

2. **Web Dashboard** (Coming Q2 2026)
   - Real-time queue monitoring
   - Interactive progress tracking
   - Visual analytics

3. **Quality Scoring** (Coming Q3 2026)
   - Automated quality checks
   - Entity relationship validation
   - Coverage optimization suggestions

4. **Integration APIs** (Coming Q4 2026)
   - REST API for all scripts
   - Webhook notifications
   - Third-party integrations

---

## Support & Documentation

### Additional Resources

- **Main Documentation:** [RESEARCHES 2/README.md](../README.md)
- **System Overview:** [SYSTEM_OVERVIEW.md](../SYSTEM_OVERVIEW.md)
- **Prompts Reference:** [08_PROMPTS_REFERENCE.md](./08_PROMPTS_REFERENCE.md)
- **Taxonomy Guide:** [07_TAXONOMY_BUILDING.md](./07_TAXONOMY_BUILDING.md)

### Getting Help

1. Check this reference guide
2. Review error logs in `scripts/logs/`
3. Run script with `--help` flag
4. Check GitHub issues (if applicable)

---

**Last Updated:** 2025-12-04
**Documentation Version:** 2.1
**Author:** RESEARCHES 2 System

---
