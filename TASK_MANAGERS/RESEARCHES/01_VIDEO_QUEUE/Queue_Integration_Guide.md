# Video Queue Integration Guide

## Overview

The Video Queue System accumulates up to 20 videos before requiring manual review, solving the problem of lost Deep Research results.

**Problem Solved**: Employees do Deep Research, find 20 videos, spend 10-15 minutes manually selecting 1 video, and those 20 videos get lost. Now they accumulate in a persistent queue.

## Workflow Integration

### Step 1: Employee Does Deep Research

Employee uses Deep Research tool (Perplexity, Gemini, GPT, DeepSeek, YouTube) to find videos on a topic.

### Step 2: Add Videos to Queue

For each video found, use the `add_video_to_queue.py` script:

```bash
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=VIDEO_ID" \
    "Employee Name" \
    "Topic Category" \
    "Research Source" \
    "Optional notes"
```

**Example**:
```bash
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=dQw4w9WgXcQ" \
    "Niko Kar" \
    "UI Design Trends" \
    "Perplexity" \
    "Found via deep research on 2025 design trends"
```

**Parameters**:
- `video_url`: Full YouTube URL
- `added_by`: Employee name
- `topic`: Research topic (e.g., "Design Research", "Video Editing", "AI Tools")
- `source`: Tool used (Perplexity, Gemini, GPT, DeepSeek, YouTube)
- `notes`: Optional notes about why this video is relevant

### Step 3: Queue Accumulation

Videos accumulate in `Video_Queue_Master.csv`. **No manual review required** until:
- 20 videos reached, OR
- Employee explicitly requests review

This allows employees to continue research without interruption.

### Step 4: Employee Reviews Queue

When ready to review, employee opens `Video_Queue_Dashboard.html` in a web browser:

```bash
# Open from file explorer, or
start TASK_MANAGERS/RESEARCHES/Video_Queue/Video_Queue_Dashboard.html
```

**Dashboard Features**:
- **Filter** by topic, status, source, or employee
- **Sort** by priority score, date added, views, or likes
- **Search** by title or channel name
- **View details** of each video
- **Export** to CSV, JSON, or Markdown

### Step 5: Select Videos for Parsing

Employee selects videos for parsing using the `update_queue_status.py` script:

```bash
# Mark video as selected
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-001 Selected "Niko Kar"

# Mark multiple videos as selected
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-002 Selected "Niko Kar"
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-003 Selected "Niko Kar"
```

Or reject videos that aren't relevant:

```bash
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-004 Rejected
```

### Step 6: Batch Parsing

All selected videos are parsed in batch (saves time vs. parsing one-by-one).

**Mark videos as parsing**:
```bash
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-001 Parsing
```

**After parsing completes**:
```bash
python TASK_MANAGERS/RESEARCHES/Video_Queue/scripts/update_queue_status.py update VQ-001 Parsed
```

Parsed videos move to `TASK_MANAGERS/RESEARCHES/VIDEO/Parsed/` (see Phase 3 Agent 3A for RESEARCHES structure).

### Step 7: Archive

Once parsed, videos can be archived or kept in queue for reference. Queue periodically archives old parsed videos to `archive/` folder.

---

## Integration Points

### With Deep Research (Phase 4)

- **Deep Research task template** includes "Add to video queue" step
- **Prompts** reference queue location
- **Employee dashboard** shows queue status (see Phase 4 Agent 4B)

**Integration Flow**:
```
Deep Research Task → Find 20 Videos → Add to Queue → Continue Research
                                           ↓
                          (Queue accumulates until 20 videos)
                                           ↓
                          Manual Review → Select Best Videos → Batch Parse
```

### With RESEARCHES Entity

- **Parsed videos** stored in `TASK_MANAGERS/RESEARCHES/VIDEO/Parsed/[DATE]/`
- **Analysis reports** in `TASK_MANAGERS/RESEARCHES/VIDEO/Analysis/`
- **Queue** references research topics from `TASK_MANAGERS/RESEARCHES/TAXONOMY/`

**Directory Integration**:
```
RESEARCHES/
├── VIDEO/
│   ├── Queue/ (links to RESEARCHES/Video_Queue)
│   ├── Parsed/ (parsed video transcripts)
│   └── Analysis/ (video analysis reports)
```

### With DAILIES

Daily reports can include:
- "Videos added to queue today: X"
- Prompts extract queue additions from daily activities
- Dashboard shows personal queue stats

### With TASK_MANAGERS

- **Queue system** lives in `TASK_MANAGERS/RESEARCHES/Video_Queue/`
- **Task templates** reference queue for video research tasks
- **Milestone templates** include "Video research phase" with queue target

---

## Manual Approval Gates

Per user requirement ("мануально" - manual review):

- Queue does **NOT** auto-parse videos
- Employee must **manually select** from queue
- Dashboard provides interface for selection
- Keeps employee **engaged in decision-making**

**Why Manual Approval**:
1. **Maintains quality control**: Employee reviews before committing parsing resources
2. **Prevents waste**: Only parse relevant videos, not all 20
3. **Employee engagement**: Keeps employees in the loop, not just automation
4. **Learning opportunity**: Reviewing metadata helps employees refine research skills

---

## Priority Scoring Algorithm

Videos are auto-scored 0-100 based on:

| Factor | Weight | Calculation |
|--------|--------|-------------|
| **Views** | 30% | 1M views = max 30 points |
| **Likes** | 20% | 50K likes = max 20 points |
| **Recency** | 30% | Brand new = 30 points, decreasing linearly over 365 days |
| **Engagement** | 20% | Likes/Views ratio, 1% engagement = 20 points |

**Example Scores**:
- **Viral recent video** (5M views, 200K likes, 7 days old): 95-100/100
- **High-performing video** (1.5M views, 45K likes, 30 days old): 75-85/100
- **Moderate older video** (500K views, 15K likes, 180 days old): 40-50/100
- **Low-performing video** (10K views, 200 likes, 60 days old): 5-10/100

**Usage**: Sort by priority to see best videos first in dashboard.

---

## Expected Benefits

### Time Savings
- **Before**: 10-15 min per video selection
- **After**: 2-3 min queue review for 20 videos
- **Savings**: ~80% reduction in selection time

### Quality Improvement
- **Metadata visibility**: Views, likes, recency guide decisions
- **Priority scoring**: Automated quality signals
- **Batch comparison**: See all 20 videos at once, not one-by-one

### Workflow Efficiency
- **No lost research**: All found videos preserved
- **Batch parsing**: Parse 20 videos at once vs. 1 at a time
- **Reduced context switching**: Add to queue and keep researching

### Portfolio Diversity
- Track video sources for varied portfolio content
- See which topics are over/under-researched
- Balance research across departments

---

## Queue Management Commands

### View Queue Summary
```bash
python scripts/update_queue_status.py summary
```

Output:
```
==============================================================
VIDEO QUEUE SUMMARY
==============================================================

Total videos in queue: 15

Status Breakdown:
  Pending     :  10 ( 66.7%)
  Selected    :   3 ( 20.0%)
  Parsed      :   2 ( 13.3%)

Top Topics:
  UI Design Trends                  :   5
  Video Editing Techniques          :   4
  AI Tools Overview                 :   3
```

### List Videos by Status
```bash
python scripts/update_queue_status.py list Pending
```

### Export Queue
```bash
# Export to CSV
python scripts/export_queue.py csv

# Export to JSON
python scripts/export_queue.py json

# Export to Markdown
python scripts/export_queue.py markdown

# Export all formats
python scripts/export_queue.py all

# Export filtered by status
python scripts/export_queue.py csv Pending
python scripts/export_queue.py markdown Selected
```

---

## Troubleshooting

### Queue CSV Not Found
**Error**: `Queue file not found`

**Solution**: Run any script once to auto-create the CSV:
```bash
python scripts/add_video_to_queue.py "https://youtube.com/watch?v=test" "Test User" "Test Topic" "YouTube"
```

### Video Already in Queue
**Warning**: `⚠️  Video already in queue: VQ-XXX`

**Explanation**: Duplicate detection prevents adding the same video twice. Existing Queue_ID is returned.

### Priority Score is 0
**Issue**: Video has 0 priority score

**Cause**: Missing metadata (views, likes, publish_date all at default values)

**Solution**: Update metadata manually in CSV or wait for metadata extraction feature (YouTube API integration planned).

### Dashboard Not Loading
**Error**: Dashboard shows "Error loading queue data"

**Cause**: Browser cannot read local CSV file due to security restrictions

**Solution**:
1. Open dashboard by double-clicking `Video_Queue_Dashboard.html`
2. Or serve via local web server:
   ```bash
   cd TASK_MANAGERS/RESEARCHES/Video_Queue
   python -m http.server 8000
   # Open http://localhost:8000/Video_Queue_Dashboard.html
   ```

---

## Future Enhancements

### Planned Features
1. **YouTube API Integration**: Auto-extract metadata (views, likes, publish date, duration)
2. **Web Interface for Adding Videos**: Form-based UI instead of command-line
3. **Automatic Status Updates**: Integration with parsing scripts to auto-update status
4. **Email Notifications**: Alert when queue reaches 20 videos
5. **Advanced Analytics**: Track which topics/sources yield best videos
6. **Multi-language Support**: Dashboard translations

### Integration Roadmap
1. **Phase 3 (Current)**: Basic queue system with manual metadata
2. **Phase 4**: Integration with Deep Research task template
3. **Phase 5**: YouTube API metadata extraction
4. **Phase 6**: Web UI for queue management
5. **Phase 7**: Analytics dashboard and reporting

---

## Support & Feedback

For issues or enhancement requests:
1. Check this guide for troubleshooting steps
2. Review script help messages (`python script.py` with no arguments)
3. Contact system administrator or AI Department

**Last Updated**: 2025-11-24
**Version**: 1.0
**Phase**: 3B (System Rebuild 2025-11)
