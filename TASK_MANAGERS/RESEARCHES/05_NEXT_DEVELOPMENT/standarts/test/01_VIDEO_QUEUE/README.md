---
category: 01_VIDEO_QUEUE
subcategory: root
type: log
source_id: README
title: README
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# README

## Summary
- TODO

## Context
- TODO

## Data / Content
# TSM-008: Video Queue System

## Purpose

The Video Queue System accumulates up to 20 videos from Deep Research before requiring manual review, preventing loss of research results and enabling batch processing.

## Problem Solved

**Before**: Employees do Deep Research, find 20 videos, manually select 1 video (taking 10-15 min), and those 20 videos get lost.

**After**: All 20 videos accumulate in a persistent queue with metadata, allowing employees to review all at once (2-3 min) and batch-parse selected videos.

---

## Quick Start

### 1. Add a Video to Queue

```bash
python scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=VIDEO_ID" \
    "Your Name" \
    "Research Topic" \
    "Research Source" \
    "Optional notes"
```

### 2. View Queue Dashboard

Open `Video_Queue_Dashboard.html` in your web browser to see all queued videos.

### 3. Update Video Status

```bash
# Mark as selected for parsing
python scripts/update_queue_status.py update VQ-001 Selected "Your Name"

# Mark as parsed after processing
python scripts/update_queue_status.py update VQ-001 Parsed
```

### 4. Export Queue

```bash
# Export to all formats (CSV, JSON, Markdown)
python scripts/export_queue.py all
```

---

## Directory Structure

```
RESEARCHES/Video_Queue/
├── Video_Queue_Master.csv          # Main queue database
├── Video_Queue_Dashboard.html       # Web-based dashboard
├── scripts/                         # Python management scripts
│   ├── add_video_to_queue.py       # Add videos to queue
│   ├── update_queue_status.py      # Update video status
│   ├── export_queue.py             # Export to CSV/JSON/MD
│   └── calculate_priority.py       # Priority scoring algorithm
├── docs/                            # Documentation
│   ├── Queue_Integration_Guide.md  # Integration workflow guide
│   ├── API_Documentation.md         # (Future: API docs)
│   └── Workflow_Diagram.md          # (Future: Visual workflows)
├── exports/                         # Generated exports
│   ├── queue_export_YYYY-MM-DD.csv
│   ├── queue_export_YYYY-MM-DD.json
│   └── queue_export_YYYY-MM-DD.md
├── archive/                         # Archived queues
│   └── queue_archive_YYYY-MM.csv
└── README.md                        # This file
```

---

## Queue CSV Schema

| Field | Type | Description |
|-------|------|-------------|
| Queue_ID | String | Unique ID (VQ-001, VQ-002, ...) |
| Video_ID | String | YouTube video ID (11 chars) |
| Video_Title | String | Video title |
| Channel_Name | String | YouTube channel name |
| Channel_URL | String | Channel URL |
| Video_URL | String | Full YouTube video URL |
| Views | Integer | View count |
| Likes | Integer | Like count |
| Comments | Integer | Comment count |
| Publish_Date | Date | Publication date (YYYY-MM-DD) |
| Duration | Time | Video duration (HH:MM:SS) |
| Added_By | String | Employee who added video |
| Added_Date | Date | Date added to queue (YYYY-MM-DD) |
| Status | Enum | Pending, Selected, Parsing, Parsed, Rejected |
| Selected_By | String | Employee who selected for parsing |
| Selected_Date | Date | Date selected (YYYY-MM-DD) |
| Parsed_Date | Date | Date parsing completed (YYYY-MM-DD) |
| Topic_Category | String | Research topic |
| Research_Source | String | Tool used (Perplexity, Gemini, GPT, DeepSeek, YouTube) |
| Priority_Score | Float | 0-100 priority score (auto-calculated) |
| Notes | String | Free text notes |

---

## Priority Scoring

Videos are automatically scored 0-100 based on:

- **Views** (30%): 1M views = max 30 points
- **Likes** (20%): 50K likes = max 20 points
- **Recency** (30%): Brand new = 30 points, decreasing over 365 days
- **Engagement** (20%): Likes/Views ratio, 1% engagement = 20 points

**High Priority** (70-100): Viral, recent, high engagement
**Medium Priority** (40-69): Good performance, moderate recency
**Low Priority** (0-39): Older or lower performing

---

## Status Workflow

```
Pending → Selected → Parsing → Parsed
    ↓
Rejected
```

- **Pending**: Newly added to queue, awaiting review
- **Selected**: Marked for parsing by employee
- **Parsing**: Currently being parsed
- **Parsed**: Parsing complete, transcript available
- **Rejected**: Not relevant, excluded from parsing

---

## Manual Approval Philosophy

The queue requires **manual approval** ("мануально") at two points:

1. **Video Selection**: Employee chooses which videos to parse from queue
2. **Final Review**: Employee reviews parsed results

**Why Manual?**
- Maintains quality control
- Keeps employees engaged in decision-making
- Prevents automation from removing human judgment
- Provides learning opportunities

---

## Scripts Usage

### add_video_to_queue.py

**Purpose**: Add a video to the queue

**Usage**:
```bash
python scripts/add_video_to_queue.py <video_url> <added_by> <topic> <source> [notes]
```

**Example**:
```bash
python scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=dQw4w9WgXcQ" \
    "Niko Kar" \
    "UI Design Trends" \
    "Perplexity" \
    "Found via deep research on 2025 trends"
```

### update_queue_status.py

**Purpose**: Update video status or view queue summary

**Commands**:
```bash
# Update status
python scripts/update_queue_status.py update <queue_id> <status> [selected_by]

# View summary
python scripts/update_queue_status.py summary

# List by status
python scripts/update_queue_status.py list <status>
```

**Examples**:
```bash
python scripts/update_queue_status.py update VQ-001 Selected "Niko Kar"
python scripts/update_queue_status.py summary
python scripts/update_queue_status.py list Pending
```

### export_queue.py

**Purpose**: Export queue to various formats

**Usage**:
```bash
python scripts/export_queue.py <format> [status_filter]
```

**Formats**: csv, json, markdown, all

**Examples**:
```bash
python scripts/export_queue.py csv
python scripts/export_queue.py json Pending
python scripts/export_queue.py markdown Selected
python scripts/export_queue.py all
```

### calculate_priority.py

**Purpose**: Test priority scoring algorithm

**Usage**:
```bash
python scripts/calculate_priority.py <views> <likes> <publish_date>
```

**Example**:
```bash
python scripts/calculate_priority.py 1500000 45000 2025-10-15
```

---

## Integration

### With Deep Research (Phase 4)
- Deep Research task template includes "Add to video queue" step
- Employee dashboards show queue status
- See: [docs/Queue_Integration_Guide.md](docs/Queue_Integration_Guide.md)

### With RESEARCHES Entity
- Parsed videos → `TASK_MANAGERS/RESEARCHES/VIDEO/Parsed/`
- Analysis reports → `TASK_MANAGERS/RESEARCHES/VIDEO/Analysis/`
- Queue references → `TASK_MANAGERS/RESEARCHES/TAXONOMY/`

### With DAILIES
- Daily reports include "Videos added to queue today: X"
- Queue stats in employee daily summaries

---

## Expected Benefits

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Video selection time | 10-15 min | 2-3 min | ~80% faster |
| Videos lost | 19/20 (95%) | 0 (0%) | 100% retention |
| Batch size | 1 video | Up to 20 videos | 20x efficiency |
| Queue visibility | None | Full dashboard | ∞ improvement |

---

## Workflow Example

**Day 1: Research & Accumulation**
```
Employee does Deep Research on "UI Design Trends 2025"
→ Finds 20 videos
→ Adds all 20 to queue (5 min)
→ Continues working (no interruption)
```

**Day 2: More Research**
```
Employee researches "Video Editing Techniques"
→ Finds 15 more videos
→ Adds to queue (now 35 total)
→ Still no manual review needed
```

**Day 3: Review & Selection**
```
Employee opens dashboard
→ Filters by topic "UI Design Trends"
→ Sorts by priority score
→ Selects top 5 videos (2 min)
→ Marks as "Selected"
```

**Day 4: Batch Parsing**
```
Parsing team processes all 5 videos
→ Transcripts saved to RESEARCHES/VIDEO/Parsed/
→ Videos marked as "Parsed"
→ Employee reviews transcripts
→ Creates analysis report
```

---

## Troubleshooting

**Queue CSV not found**
- Run any script once to auto-create the CSV

**Dashboard not loading**
- Open `Video_Queue_Dashboard.html` by double-clicking
- Or serve via local web server: `python -m http.server 8000`

**Priority score is 0**
- Missing metadata (views, likes, publish_date)
- Update manually in CSV or wait for YouTube API integration

**Video already in queue**
- Duplicate detection prevents adding same video twice
- Existing Queue_ID is returned

---

## Future Enhancements

### Planned (Phase 5+)
- YouTube API integration for automatic metadata extraction
- Web UI for adding videos (form-based)
- Email notifications when queue reaches 20 videos
- Advanced analytics dashboard
- Multi-language support

---

## Related Documentation

- [Queue Integration Guide](docs/Queue_Integration_Guide.md) - Full integration workflow
- [Phase 3 Context](../../PLANS/System_Rebuild_2025-11/Phase_3_Context_Research.md) - System rebuild context
- [RESEARCHES Structure](../../RESEARCHES/README.md) - Research entity organization

---

## Version History

- **v1.0** (2025-11-24): Initial release - Phase 3B System Rebuild
  - Queue CSV schema
  - Python management scripts
  - HTML dashboard
  - Priority scoring algorithm
  - Integration documentation

---

**Created**: 2025-11-24
**Phase**: 3B (System Rebuild 2025-11)
**Status**: ✅ Production Ready
**Maintainer**: AI Department


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
