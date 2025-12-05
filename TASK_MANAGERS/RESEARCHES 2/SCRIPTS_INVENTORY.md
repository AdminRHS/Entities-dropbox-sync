# RESEARCHES Scripts Inventory

**Last Updated:** 2025-11-24
**Total Scripts:** 14
**Categories:** Search Queue, Video Queue, Progress Tracking, Utilities

---

## Scripts by Category

### 🔍 Search Queue Scripts (00_SEARCH_QUEUE/scripts/)

#### 1. assign_search.py
**Purpose:** Assign new video search tasks to employees

**Usage:**
```bash
python 00_SEARCH_QUEUE/scripts/assign_search.py <employee> <department> <topic> [search_query] [notes]
```

**Example:**
```bash
python assign_search.py "John Doe" "AI" "Claude tutorials" "claude tutorial" "Focus on 2024-2025"
```

**Functionality:**
- Generates unique SEARCH-XXX IDs
- Tracks employee assignments
- Records department and topic
- Sets initial status to "Assigned"
- Updates Search_Queue_Master.csv

---

#### 2. complete_search.py
**Purpose:** Mark search tasks as completed and record results

**Usage:**
```bash
python 00_SEARCH_QUEUE/scripts/complete_search.py <search_id> <videos_found> [notes]
```

**Example:**
```bash
python complete_search.py SEARCH-001 15 "Found excellent tutorials"
```

**Functionality:**
- Updates search status to "Completed"
- Records number of videos found
- Adds completion date
- Updates notes if provided

---

### 📹 Video Queue Scripts (01_VIDEO_QUEUE/scripts/)

#### 3. add_video_to_queue.py
**Purpose:** Add videos to the processing queue with full metadata

**Usage:**
```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py <youtube_url> <employee> <topic> <source> [notes]
```

**Example:**
```bash
python add_video_to_queue.py "https://youtube.com/watch?v=abc123" "John Doe" "Claude AI" "Perplexity" "Important tutorial"
```

**Functionality:**
- Generates unique VQ-XXX IDs
- Extracts video metadata from YouTube
- Calculates priority score
- Sets initial status to "Queued"
- Updates Video_Queue_Master.csv

---

#### 4. add_video_to_queue_simple.py
**Purpose:** Simplified version for quick video additions

**Usage:**
```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py <youtube_url>
```

**Example:**
```bash
python add_video_to_queue_simple.py "https://youtube.com/watch?v=abc123"
```

**Functionality:**
- Minimal input required
- Uses default employee/source
- Faster for batch additions

---

#### 5. update_queue_status.py
**Purpose:** Update video status in queue

**Usage:**
```bash
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update <video_id> <new_status> [employee]
```

**Example:**
```bash
python update_queue_status.py update VQ-001 Selected "John Doe"
python update_queue_status.py update VQ-001 Parsed
```

**Statuses:**
- Queued
- Selected
- Transcribing
- Parsed
- Completed
- Skipped

**Functionality:**
- Updates video status
- Records employee who made change
- Adds timestamp
- Updates processing notes

---

#### 6. calculate_priority.py
**Purpose:** Calculate and update priority scores for queued videos

**Usage:**
```bash
python 01_VIDEO_QUEUE/scripts/calculate_priority.py [video_id]
```

**Example:**
```bash
python calculate_priority.py VQ-001  # Calculate for one video
python calculate_priority.py         # Calculate for all
```

**Priority Factors:**
- Date added (older = higher priority)
- Source credibility
- Topic relevance
- Department needs
- Employee requests

**Functionality:**
- Recalculates priority scores
- Updates queue ordering
- Helps identify next videos to process

---

#### 7. export_queue.py
**Purpose:** Export queue to various formats

**Usage:**
```bash
python 01_VIDEO_QUEUE/scripts/export_queue.py <format>
```

**Formats:**
- `csv` - Export as CSV
- `json` - Export as JSON
- `markdown` - Export as Markdown table
- `all` - Export to all formats

**Example:**
```bash
python export_queue.py all
python export_queue.py json
```

**Functionality:**
- Exports current queue state
- Filters by status
- Generates reports
- Creates backups

---

#### 8. video_queue_manager.py
**Purpose:** Main queue management interface

**Usage:**
```bash
python 01_VIDEO_QUEUE/video_queue_manager.py
```

**Functionality:**
- Interactive CLI menu
- View queue statistics
- Manage video entries
- Batch operations
- Generate reports

---

### 📊 Progress Tracking Scripts (scripts/)

#### 9. update_video_progress.py
**Purpose:** Track video processing progress through all phases

**Usage:**
```bash
# Add video to tracker
python scripts/update_video_progress.py add <video_number> <title> <youtube_url> <employee>

# Update phase
python scripts/update_video_progress.py update <video_number> <phase_name> [notes]

# View progress
python scripts/update_video_progress.py view [video_number]
```

**Examples:**
```bash
# Add new video
python update_video_progress.py add 22 "Claude AI Tutorial" "https://youtube.com/..." "John Doe"

# Update to transcribed
python update_video_progress.py update 22 Phase_1_Transcribed "Used PMT-004"

# Update to extraction phase
python update_video_progress.py update 22 Phase_2_Extraction "Extracted 37 entities"

# View specific video
python update_video_progress.py view 22

# View all videos
python update_video_progress.py view
```

**Phases Tracked (6-Phase Workflow):**
- Phase_0_Queued - Video added to queue
- Phase_1_Transcribed - Full transcription + analysis (PMT-004)
- Phase_2_Extraction - Entity extraction & cross-referencing (PMT-007)
- Phase_3_Gap_Analysis - Library comparison & gap identification (PMT-009 Part 1)
- Phase_4_Integration - JSON creation & taxonomy integration (PMT-009 Part 2)
- Phase_5_Mapping - Final mapping & documentation (PMT-009 Part 3)
- Complete - All phases finished

**Functionality:**
- Creates VIDEO_PROGRESS_TRACKER.csv
- Tracks dates for each phase
- Calculates total processing time
- Records employee and notes
- Shows completion percentage

---

#### 10. generate_progress_report.py
**Purpose:** Generate comprehensive progress reports

**Usage:**
```bash
python scripts/generate_progress_report.py <type>
```

**Report Types:**
- `summary` - Overall summary with statistics
- `detailed` - Detailed report for all videos
- `weekly` - Weekly activity report
- `all` - Generate all report types

**Examples:**
```bash
# Generate summary report
python generate_progress_report.py summary

# Generate weekly report
python generate_progress_report.py weekly

# Generate all reports
python generate_progress_report.py all
```

**Reports Include:**
- Status overview (completed vs in progress)
- Phase distribution
- Employee productivity
- Average processing time
- Recent activity
- Weekly metrics

**Output Location:** `RESEARCHES/REPORTS/`

---

### 🛠️ Utility Scripts (scripts/)

#### 11. config.py
**Purpose:** Configuration management for RESEARCHES scripts

**Functionality:**
- Centralized configuration
- Path definitions
- Default settings
- API keys management

---

#### 12. utils.py
**Purpose:** Shared utility functions

**Functions:**
- `generate_id()` - Generate unique IDs
- `validate_youtube_url()` - Validate YouTube URLs
- `extract_video_id()` - Extract video ID from URL
- `format_date()` - Date formatting
- `load_csv()` - CSV file operations
- `save_csv()` - CSV file operations

---

#### 13. video_id_scanner.py
**Purpose:** Scan and validate video IDs across system

**Usage:**
```bash
python scripts/video_id_scanner.py
```

**Functionality:**
- Scans all video references
- Validates ID formats
- Checks for duplicates
- Generates validation report

---

## Script Dependencies

### Python Requirements
```
pandas
requests
youtube-dl (or yt-dlp)
python-dateutil
```

### Install Dependencies
```bash
pip install pandas requests yt-dlp python-dateutil
```

---

## Workflow Integration

### Search → Queue Workflow
```bash
# 1. Assign search
python 00_SEARCH_QUEUE/scripts/assign_search.py "Employee" "Dept" "Topic"

# 2. Complete search
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 10

# 3. Add videos found to queue
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py "URL" "Employee" "Topic" "Source"
```

### Complete Video Processing Workflow
```bash
# 1. View queue and select video
python 01_VIDEO_QUEUE/video_queue_manager.py

# 2. Add to progress tracker
python scripts/update_video_progress.py add 22 "Video Title" "URL" "Employee"

# 3. Update status to Selected
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Selected

# 4. Phase 1: Transcribe + Analyze (PMT-004)
# ... run transcription (includes title + analysis)
python scripts/update_video_progress.py update 22 Phase_1_Transcribed

# 5. Phase 2: Extract Entities (PMT-007)
# ... deep entity extraction & cross-referencing
python scripts/update_video_progress.py update 22 Phase_2_Extraction

# 6. Phase 3: Gap Analysis (PMT-009 Part 1)
# ... library comparison & gap identification
python scripts/update_video_progress.py update 22 Phase_3_Gap_Analysis

# 7. Phase 4: Integration (PMT-009 Part 2)
# ... create JSON files & integrate entities
python scripts/update_video_progress.py update 22 Phase_4_Integration

# 8. Phase 5: Mapping (PMT-009 Part 3)
# ... final mapping & documentation
python scripts/update_video_progress.py update 22 Phase_5_Mapping

# 9. Complete
python scripts/update_video_progress.py update 22 Complete
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Completed

# 10. Generate progress report
python scripts/generate_progress_report.py weekly
```

---

## Common Operations

### Quick Add Multiple Videos
```bash
for url in $(cat video_urls.txt); do
    python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py "$url"
done
```

### Export Weekly Report
```bash
python 01_VIDEO_QUEUE/scripts/export_queue.py markdown > weekly_queue_report.md
```

### Recalculate All Priorities
```bash
python 01_VIDEO_QUEUE/scripts/calculate_priority.py
```

---

## Script Locations

```
RESEARCHES/
├── 00_SEARCH_QUEUE/
│   └── scripts/
│       ├── assign_search.py
│       └── complete_search.py
│
├── 01_VIDEO_QUEUE/
│   ├── scripts/
│   │   ├── add_video_to_queue.py
│   │   ├── add_video_to_queue_simple.py
│   │   ├── calculate_priority.py
│   │   ├── export_queue.py
│   │   └── update_queue_status.py
│   └── video_queue_manager.py
│
└── scripts/
    ├── config.py
    ├── utils.py
    └── video_id_scanner.py
```

---

## Maintenance

### Script Updates
All scripts log to: `RESEARCHES/scripts/logs/`

### Error Handling
Scripts create backups before modifying CSV files

### Version Control
Track script versions in: `SCRIPTS_CHANGELOG.md`

---

**For detailed workflow documentation, see:** [RESEARCHES/README.md](README.md)
