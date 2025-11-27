---
category: 01_VIDEO_QUEUE
subcategory: root
type: log
source_id: Queue_System_README
title: Queue System README
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# Queue System README

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video Processing Queue System

**Created:** 2025-11-21
**Status:** Active
**Location:** `TASK_MANAGERS/RESEARCHES/01_QUEUE/`

---

## Overview

The Queue System manages video discovery, prioritization, and processing tracking across all 7 phases.

**Components:**
1. **video_queue_manager.py** - Python script for automated queue management
2. **Video_Queue_Tracker.md** - Manual tracking and status updates
3. **Transcription_Queue.md** - Phase-specific transcription queue

---

## Queue Files

### 1. video_queue_manager.py
**Purpose:** Automated queue management and prioritization
**Language:** Python
**Location:** `01_QUEUE/video_queue_manager.py`

**Functions:**
- Add new videos to queue
- Update processing status
- Prioritize based on scoring matrix
- Track phase completion
- Generate status reports

**Usage:**
```bash
python video_queue_manager.py add "Video URL" "Title"
python video_queue_manager.py status
python video_queue_manager.py next
```

---

### 2. Video_Queue_Tracker.md
**Purpose:** Human-readable queue tracking
**Format:** Markdown table
**Location:** `01_QUEUE/Video_Queue_Tracker.md`

**Columns:**
- Video ID
- Title
- Priority Score (0-100)
- Current Phase
- Status
- Assignee
- Due Date

**Status Values:**
- 🔴 Pending
- 🟡 In Progress
- 🟢 Complete
- ⚫ Blocked

---

### 3. Transcription_Queue.md
**Purpose:** Phase 1 specific tracking
**Format:** Markdown
**Location:** `01_QUEUE/Transcription_Queue.md`

**Sections:**
- Queue table (pending transcriptions)
- Execution milestones
- Processing stages (Transcription, Analysis, Population)

---

## Priority Scoring Matrix

Videos scored 0-100 based on:

| Criterion | Weight | Max Points |
|-----------|--------|------------|
| Tool novelty | 30% | 30 |
| Workflow complexity | 25% | 25 |
| Department coverage | 20% | 20 |
| Creator authority | 15% | 15 |
| Recency | 10% | 10 |

**Priority Levels:**
- **High (80-100):** Process within 1 week
- **Medium (50-79):** Process within 2 weeks
- **Low (0-49):** Process within 1 month

---

## Queue Workflow

```
1. Discovery
   - Weekly scanning (see Video_Discovery_Pipeline.md)
   - Community recommendations
   - Influencer tracking
   ↓
2. Evaluation
   - Apply scoring matrix
   - Check for duplicates
   - Assess taxonomy value
   ↓
3. Queue Addition
   - Add to video_queue_manager.py
   - Update Video_Queue_Tracker.md
   - Assign to processor
   ↓
4. Processing
   - Execute Phase 1-7
   - Update status after each phase
   - Track completion
   ↓
5. Completion
   - Mark as complete
   - Update VIDEOS_INDEX.md
   - Archive queue entry
```

---

## Queue Management Rules

### Adding Videos
1. Run scoring matrix
2. Check for existing similar content
3. Verify video accessibility
4. Add with all metadata (URL, title, creator, duration)

### Prioritization
1. High-priority videos jump queue
2. Same priority = FIFO (First In First Out)
3. Blocked videos moved to separate list

### Status Updates
- Update after EACH phase completion
- Mark blockers immediately
- Note any quality issues

### Completion
- Verify all 7 phases complete
- Update VIDEOS_INDEX.md
- Move to archive section of queue

---

## Integration with Phase System

| Phase | Queue Update Required | Status Field |
|-------|----------------------|--------------|
| Phase 1 | ✅ Yes | "Phase 1 Complete" |
| Phase 2 | Optional | "Phase 2 Complete" |
| Phase 3 | ✅ Yes | "Phase 3 Complete" |
| Phase 4 | ✅ Yes | "Phase 4 Complete" |
| Phase 5 | ✅ Yes | "Phase 5 Complete" |
| Phase 6 | ✅ Yes | "Phase 6 Complete" |
| Phase 7 | ✅ Yes | "All Phases Complete" |

---

## Monthly Goals

**Target:** 2-4 high-value videos per month

**Breakdown:**
- Week 1: Discovery & queue population
- Week 2: Phase 1-3 (1-2 videos)
- Week 3: Phase 4-6 (1-2 videos)
- Week 4: Phase 7 + reporting

**Time Budget:** 8-16 hours/month total

---

## Queue Metrics

Track monthly:
- Videos added to queue
- Videos completed (all 7 phases)
- Average processing time
- Tools discovered
- Coverage improvement %

**Report Location:** `03_ANALYSIS/Phase_Reports/`

---

## Related Documentation

- [Video Discovery Pipeline](../02_TRANSCRIPTIONS/Video_Discovery_Pipeline.md)
- [Phase System Overview](../00_PHASES/Phase_System_Overview.md)
- [Videos Index](../02_TRANSCRIPTIONS/VIDEOS_INDEX.md)
- [Influencer Tracking](../04_INFLUENCER_DATA/)

---

*Queue system established: 2025-11-12*
*Consolidated: 2025-11-21*


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
