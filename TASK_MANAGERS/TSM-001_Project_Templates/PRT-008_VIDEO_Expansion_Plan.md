# PRT-008 VIDEO Workflow Expansion Plan v2.0

**Project:** PRT-008 (VIDEO Production)
**Version:** 2.0 - Enhanced with Choice Points and Automation
**Date:** 2025-11-21
**Status:** Design Phase

---

## Overview

This document outlines enhancements to the existing PRT-008 VIDEO workflow to add:
1. **Multiple AI Research Options** (Perplexity, Gemini Deep Research, GPT, Grok)
2. **Flexible Transcription Choices** (Google AI Studio, TurboScribe, Whisper)
3. **Enhanced Video Metadata Capture** (channel, links, likes, timing)
4. **Automated Queue Management** (video processing pipeline)
5. **Human Review Checkpoints** (manual verification gates)
6. **Output Format Standardization** (structured video listings)

---

## Current Workflow (v1.0) Summary

```
Stage 1: Research → Stage 2: Transcription → Stage 3: Library Population
├─ TST-050: Search Videos (Perplexity only)
├─ TST-051: Select Videos
├─ TST-057: Transcribe (Google AI Studio only)
├─ TST-052: Extract Taxonomy
└─ TST-058: Populate Libraries
```

**Limitations:**
- ❌ Single AI platform for research (Perplexity only)
- ❌ Single transcription method (Google AI Studio)
- ❌ No structured video metadata capture
- ❌ No automated queue management
- ❌ No handling for videos >20 minutes
- ❌ Manual file organization
- ❌ No output format templates

---

## Expansion Plan: New Task Templates

### **STAGE 1A: Multi-Platform Video Research**

#### **TST-050A: Research Videos with Perplexity AI** (EXISTING - Enhanced)
- **Duration:** 1.5-2 hours
- **AI Platform:** Perplexity AI (Structure Mode, Creativity 0.5)
- **Output Format:** Structured markdown with video cards
- **New Features:**
  - Standardized video listing template
  - Channel information capture
  - Engagement metrics (likes, views, comments)
  - Export to JSON for queue system

**Enhanced Output Format:**
```markdown
## Video Research Results - YYYY-MM-DD

### Video 1: [Video Title]
- **Channel:** [Channel Name] ([Channel URL])
- **Video URL:** https://youtube.com/watch?v=...
- **Duration:** 15:30
- **Published:** 2025-11-15
- **Views:** 45.2K | **Likes:** 3.1K | **Comments:** 234
- **Score:** 85/100
  - Strategic Alignment: 35/40 (AI automation, matches PRT-002)
  - Tech Relevance: 28/30 (Claude, n8n, MCP - our stack)
  - Actionable Value: 22/30 (tutorial format, step-by-step)
- **Value Proposition:** Demonstrates MCP server setup for Claude automation
- **Department:** AID, DEV
- **Priority:** High
- **Processing Status:** Queued for transcription
```

#### **TST-050B: Research Videos with Gemini Deep Research** (NEW)
- **Duration:** 2-3 hours (deep analysis)
- **AI Platform:** Gemini 2.0 Flash Thinking / Deep Research
- **Best For:** Complex topics requiring multi-source synthesis
- **Unique Features:**
  - Deep dive into multiple videos on same topic
  - Comparative analysis across videos
  - Identifies best-in-class tutorials
  - Generates research reports with citations

**Workflow:**
1. Input research question: "Find best tutorials on MCP server development published in last 60 days"
2. Gemini performs deep research (5-15 minutes)
3. Returns comprehensive report with 10-15 video recommendations
4. Includes comparison matrix
5. Export structured results to queue

#### **TST-050C: Research Videos with ChatGPT Search** (NEW)
- **Duration:** 1-2 hours
- **AI Platform:** ChatGPT Plus (with web search)
- **Best For:** Recent videos (last 7-30 days), trending topics
- **Unique Features:**
  - Real-time search integration
  - Conversation-based refinement
  - Quick iteration on search criteria
  - Export to markdown or JSON

**Workflow:**
1. Use ChatGPT with search enabled
2. Prompt: "Search YouTube for videos published in last 30 days about [topic]"
3. Refine based on results
4. Request structured output
5. Copy to video queue

#### **TST-050D: Research Videos with Grok (X.AI)** (NEW)
- **Duration:** 1-1.5 hours
- **AI Platform:** Grok (X Premium+)
- **Best For:** Tech news, developer community trends
- **Unique Features:**
  - Real-time X (Twitter) integration
  - Developer community sentiment
  - Trending tech topics
  - Viral video detection

**Workflow:**
1. Ask Grok: "What YouTube videos about [topic] are trending in dev community?"
2. Grok analyzes X conversations + YouTube
3. Returns videos with social proof
4. Includes developer reactions/quotes
5. Export to queue

#### **TST-050E: Hybrid Multi-AI Research** (NEW)
- **Duration:** 3-4 hours
- **AI Platforms:** Perplexity + Gemini + ChatGPT (triangulation)
- **Best For:** Critical decisions, large projects
- **Unique Features:**
  - Cross-validates findings across 3 AI platforms
  - Identifies consensus picks (all 3 recommend)
  - Catches unique finds from each platform
  - Confidence scoring based on agreement

**Workflow:**
1. Run same search query on all 3 platforms
2. Collect all video recommendations
3. Identify overlaps (high confidence)
4. Review unique finds from each platform
5. Generate consolidated report
6. Export to queue with confidence scores

---

### **STAGE 1B: Human Review & Video Selection**

#### **TST-051A: Manual Video Review Checklist** (EXISTING - Enhanced)
- **Duration:** 30-60 minutes
- **New Features:** Enhanced checklist with more criteria

**Enhanced Review Criteria:**

**MUST HAVE (Blocking):**
- ✅ Duration: 5-60 minutes (NEW: expanded range)
- ✅ Published: Last 60 days (configurable)
- ✅ Language: English (or has English subtitles)
- ✅ Video Quality: 720p minimum
- ✅ Audio Quality: Clear, understandable
- ✅ Channel Verified: ✓ checkmark present

**SCORING FACTORS:**
- **Content Quality (40 points)**
  - Tutorial format (10 pts)
  - Step-by-step walkthrough (10 pts)
  - Shows real examples (10 pts)
  - Provides code/resources (10 pts)

- **Engagement Metrics (30 points)**
  - Likes ratio >90% (10 pts)
  - Comments with questions/discussion (10 pts)
  - View count relative to channel size (10 pts)

- **Strategic Fit (30 points)**
  - Aligns with current projects (15 pts)
  - Tools/tech we use (10 pts)
  - Immediately actionable (5 pts)

**NEW: Video Metadata Capture Form:**
```json
{
  "video_id": "VIDEO_001",
  "title": "",
  "channel_name": "",
  "channel_url": "",
  "video_url": "",
  "duration": "MM:SS",
  "published_date": "YYYY-MM-DD",
  "views": 0,
  "likes": 0,
  "comments": 0,
  "description_snippet": "",
  "links_in_description": [],
  "score": 0,
  "priority": "High|Medium|Low",
  "departments": [],
  "processing_status": "queued",
  "transcription_method": "auto_select",
  "notes": ""
}
```

#### **TST-051B: Export to Video Processing Queue** (NEW)
- **Duration:** 5-10 minutes
- **Output:** JSON file for queue system

**Queue File Structure:**
```
ENTITIES/TASK_MANAGERS/RESEARCHES/Video_Queue/
├── queue_YYYY-MM-DD.json
├── in_progress/
│   ├── VIDEO_001_metadata.json
│   └── VIDEO_002_metadata.json
├── completed/
│   ├── VIDEO_001_complete.json
│   └── VIDEO_001_transcript.md
└── failed/
    └── VIDEO_003_error.json
```

**Queue JSON Format:**
```json
{
  "queue_id": "QUEUE_2025-11-21",
  "created_date": "2025-11-21T14:30:00Z",
  "total_videos": 5,
  "videos": [
    {
      "video_id": "VIDEO_001",
      "title": "VS Code AI Features 2025",
      "channel_name": "James Montemagno",
      "channel_url": "https://youtube.com/@jamesmontemagno",
      "video_url": "https://youtube.com/watch?v=...",
      "duration": "10:56",
      "duration_seconds": 656,
      "published_date": "2025-11-15",
      "views": 45200,
      "likes": 3100,
      "like_ratio": 0.95,
      "comments": 234,
      "score": 85,
      "priority": "High",
      "departments": ["AID", "DEV"],
      "transcription_method": "google_ai_studio",
      "processing_status": "queued",
      "queued_at": "2025-11-21T14:30:00Z"
    }
  ]
}
```

---

### **STAGE 2A: Intelligent Transcription Routing**

#### **TST-057A: Auto-Select Transcription Method** (NEW)
- **Duration:** 1 minute (automated decision)
- **Logic:** Choose transcription method based on video properties

**Decision Tree:**
```
IF duration ≤ 40 minutes AND size ≤ 100MB:
    → Use Google AI Studio (fast, high quality)

ELIF duration > 40 minutes OR size > 100MB:
    → Use TurboScribe (handles long videos, advanced features)

ELIF audio quality poor OR heavy accent:
    → Use TurboScribe (better accuracy)

ELIF need timestamps with speaker labels:
    → Use TurboScribe (advanced features)

ELSE:
    → Default to Google AI Studio
```

**Output:** Updates queue JSON with selected method

#### **TST-057B: Transcribe with Google AI Studio** (EXISTING)
- **Best For:** Videos ≤ 40 minutes, ≤ 100MB
- **Quality:** Excellent for clear audio
- **Features:**
  - Word-for-word accuracy
  - Basic timestamps
  - Works with YouTube URLs

**Workflow:** (Existing, no changes)

#### **TST-057C: Transcribe with TurboScribe** (NEW)
- **Best For:** Videos > 40 minutes, large files, poor audio
- **Quality:** Excellent, handles accents/noise
- **Features:**
  - Speaker labels (auto-detect)
  - Precise timestamps (per word)
  - Multiple export formats
  - Batch processing

**Workflow:**
1. Open TurboScribe (https://turboscribe.ai)
2. Upload video file OR paste YouTube URL
3. Select settings:
   - Language: Auto-detect or English
   - Timestamps: Per sentence
   - Speaker labels: ON
   - Export format: SRT + TXT
4. Click "Transcribe" (processing: 2-5 minutes)
5. Download transcript
6. Convert to markdown format using template
7. Save as VIDEO_XXX.md

**TurboScribe Output Processing Script:**
```python
# convert_turboscribe_to_markdown.py
def convert_turboscribe_srt_to_markdown(srt_file, video_metadata):
    """
    Convert TurboScribe SRT output to standard VIDEO_XXX.md format
    """
    with open(srt_file, 'r') as f:
        srt_content = f.read()

    # Parse SRT format
    entries = parse_srt(srt_content)

    # Generate markdown
    markdown = generate_video_markdown_template(video_metadata)
    markdown += "\n### 3. Word-for-Word Transcription\n\n"

    for entry in entries:
        timestamp = format_timestamp(entry['start_time'])
        speaker = entry.get('speaker', 'Speaker')
        text = entry['text']
        markdown += f"**{speaker}**\n\n[{timestamp}] {text}\n\n"

    return markdown
```

#### **TST-057D: Transcribe with Local Whisper** (NEW)
- **Best For:** Privacy-sensitive content, offline processing
- **Quality:** Excellent, state-of-the-art
- **Features:**
  - Fully local (no cloud)
  - Multiple model sizes
  - High accuracy
  - Timestamp support

**Workflow:**
1. Install Whisper: `pip install openai-whisper`
2. Download video: `yt-dlp [VIDEO_URL]`
3. Run Whisper: `whisper video.mp4 --model large-v3 --output_format srt`
4. Convert output to markdown (same as TurboScribe)

#### **TST-057E: Transcription Quality Check** (NEW)
- **Purpose:** Verify transcription accuracy before extraction

**Quality Checklist:**
- ✅ No large gaps in transcription
- ✅ Technical terms spelled correctly
- ✅ Code snippets captured accurately
- ✅ Timestamps align with video
- ✅ Speaker labels accurate (if applicable)
- ✅ Links from description included
- ✅ On-screen text captured in [TEXT: ...] format

**If Quality Check FAILS:**
- Option 1: Re-transcribe with different method
- Option 2: Manual corrections in editor
- Option 3: Skip video (mark as "failed" in queue)

---

### **STAGE 2B: Enhanced Metadata Capture**

#### **TST-057F: Capture Complete Video Metadata** (NEW)
- **Purpose:** Ensure all video metadata is captured before transcription

**Metadata to Capture:**

**From YouTube Page:**
- Video title
- Channel name + URL
- Video URL
- Upload date
- View count
- Like count (use browser extension if hidden)
- Comment count
- Video description (FULL TEXT)
- All links in description
- Hashtags
- Video category
- Video tags (use View Page Source)

**From Video Content:**
- Actual duration (from playback)
- On-screen tools/logos shown
- Code repositories shown
- Social media handles mentioned

**Storage Location:**
```
ENTITIES/REPORTS/Videos/Metadata/VIDEO_XXX_metadata.json
```

**Metadata JSON Schema:**
```json
{
  "video_id": "VIDEO_015",
  "youtube_id": "0D__JqyaUYA",
  "title": "VS Code gets 6 NEW Game-Changing AI Features",
  "channel": {
    "name": "James Montemagno",
    "url": "https://youtube.com/@jamesmontemagno",
    "subscriber_count": "150K"
  },
  "urls": {
    "video": "https://youtu.be/0D__JqyaUYA",
    "embed": "https://youtube.com/embed/0D__JqyaUYA",
    "short": "https://youtu.be/0D__JqyaUYA?si=zQniZfhwystxTX54"
  },
  "published": {
    "date": "2025-11-15",
    "timestamp": "2025-11-15T10:00:00Z"
  },
  "duration": {
    "formatted": "10:56",
    "seconds": 656
  },
  "engagement": {
    "views": 45200,
    "likes": 3100,
    "comments": 234,
    "like_ratio": 0.95
  },
  "description": {
    "text": "Full description text here...",
    "links": [
      "https://github.com/awesome-copilot",
      "https://code.visualstudio.com/insider/mcp"
    ],
    "hashtags": ["VSCode", "AI", "Copilot"]
  },
  "content_analysis": {
    "tools_mentioned": ["VS Code", "GitHub Copilot", "MCP Servers"],
    "topics": ["AI", "Development", "Automation"],
    "tutorial_type": "Feature Demo",
    "skill_level": "Intermediate"
  },
  "processing": {
    "score": 85,
    "priority": "High",
    "departments": ["AID", "DEV"],
    "transcription_method": "google_ai_studio",
    "status": "completed",
    "transcribed_at": "2025-11-21T15:00:00Z",
    "extracted_at": "2025-11-21T15:30:00Z"
  }
}
```

---

### **STAGE 3: Queue Management & Automation**

#### **TST-059A: Initialize Video Processing Queue** (NEW)
- **Purpose:** Set up queue system for batch processing

**Queue Initialization Script:**
```python
# initialize_queue.py
import json
from datetime import datetime
from pathlib import Path

def initialize_queue(videos_list):
    """
    Create queue JSON from research results
    """
    queue_dir = Path("ENTITIES/TASK_MANAGERS/RESEARCHES/Video_Queue")
    queue_dir.mkdir(parents=True, exist_ok=True)

    queue_id = f"QUEUE_{datetime.now().strftime('%Y-%m-%d')}"

    queue = {
        "queue_id": queue_id,
        "created_date": datetime.now().isoformat(),
        "total_videos": len(videos_list),
        "status": "active",
        "videos": videos_list
    }

    queue_file = queue_dir / f"{queue_id}.json"
    with open(queue_file, 'w') as f:
        json.dump(queue, f, indent=2)

    print(f"✅ Queue initialized: {queue_file}")
    print(f"📊 Total videos: {len(videos_list)}")

    return queue_id

# Usage:
# python initialize_queue.py --input research_results.json
```

#### **TST-059B: Add Video to Processing Queue** (NEW)
- **Purpose:** Add single video to queue (manual or automated)

**Add to Queue Script:**
```python
# add_to_queue.py
def add_video_to_queue(queue_id, video_metadata):
    """
    Add single video to existing queue
    """
    queue_file = Path(f"ENTITIES/TASK_MANAGERS/RESEARCHES/Video_Queue/{queue_id}.json")

    with open(queue_file, 'r') as f:
        queue = json.load(f)

    # Auto-select transcription method
    video_metadata['transcription_method'] = auto_select_transcription_method(
        duration_seconds=video_metadata['duration_seconds']
    )

    video_metadata['processing_status'] = 'queued'
    video_metadata['queued_at'] = datetime.now().isoformat()

    queue['videos'].append(video_metadata)
    queue['total_videos'] = len(queue['videos'])

    with open(queue_file, 'w') as f:
        json.dump(queue, f, indent=2)

    print(f"✅ Added {video_metadata['title']} to queue")
    print(f"   Transcription method: {video_metadata['transcription_method']}")

def auto_select_transcription_method(duration_seconds):
    """
    Auto-select transcription method based on video duration
    """
    if duration_seconds <= 1200:  # 20 minutes
        return "google_ai_studio"
    else:
        return "turboscribe"

# Usage:
# python add_to_queue.py --queue QUEUE_2025-11-21 --video video_metadata.json
```

#### **TST-059C: Process Video from Queue** (NEW)
- **Purpose:** Automated processing of queued videos

**Queue Processing Script:**
```python
# process_queue.py
def process_next_video_in_queue(queue_id):
    """
    Process next video in queue (transcribe + extract)
    """
    queue_file = Path(f"ENTITIES/TASK_MANAGERS/RESEARCHES/Video_Queue/{queue_id}.json")

    with open(queue_file, 'r') as f:
        queue = json.load(f)

    # Find next queued video
    next_video = None
    for video in queue['videos']:
        if video['processing_status'] == 'queued':
            next_video = video
            break

    if not next_video:
        print("✅ Queue empty - all videos processed")
        return

    print(f"🎬 Processing: {next_video['title']}")
    print(f"   Method: {next_video['transcription_method']}")

    # Update status
    next_video['processing_status'] = 'in_progress'
    next_video['started_at'] = datetime.now().isoformat()
    save_queue(queue, queue_file)

    # Step 1: Transcribe
    if next_video['transcription_method'] == 'google_ai_studio':
        transcript = transcribe_google_ai_studio(next_video['video_url'])
    elif next_video['transcription_method'] == 'turboscribe':
        transcript = transcribe_turboscribe(next_video['video_url'])

    # Save transcript
    transcript_file = Path(f"ENTITIES/REPORTS/Videos/VIDEO_{next_video['video_id']}.md")
    transcript_file.write_text(transcript)

    # Step 2: Extract taxonomy (call existing TST-052)
    print("   Extracting taxonomy...")
    # (This would call Claude with extraction prompt)

    # Update status
    next_video['processing_status'] = 'completed'
    next_video['completed_at'] = datetime.now().isoformat()
    save_queue(queue, queue_file)

    print(f"✅ Completed: {next_video['title']}")

# Usage:
# python process_queue.py --queue QUEUE_2025-11-21
```

#### **TST-059D: Batch Process Queue** (NEW)
- **Purpose:** Process all queued videos automatically

**Batch Processing Script:**
```python
# batch_process_queue.py
def batch_process_queue(queue_id, max_videos=None):
    """
    Process multiple videos from queue in sequence
    """
    processed = 0
    while True:
        try:
            process_next_video_in_queue(queue_id)
            processed += 1

            if max_videos and processed >= max_videos:
                print(f"✅ Batch limit reached: {processed} videos processed")
                break

        except Exception as e:
            print(f"❌ Error processing video: {e}")
            # Mark as failed and continue
            mark_current_as_failed(queue_id, error=str(e))
            continue

# Usage:
# python batch_process_queue.py --queue QUEUE_2025-11-21 --max 5
# python batch_process_queue.py --queue QUEUE_2025-11-21  # Process all
```

---

## Updated Task Sequence

### **STAGE 1: Multi-Platform Research**
1. **TST-050A-E**: Choose AI research platform(s)
   - 050A: Perplexity (1.5-2h)
   - 050B: Gemini Deep Research (2-3h)
   - 050C: ChatGPT Search (1-2h)
   - 050D: Grok (1-1.5h)
   - 050E: Hybrid Multi-AI (3-4h)

2. **TST-051A**: Manual Review & Scoring (30-60 min)

3. **TST-051B**: Export to Queue (5-10 min)

### **STAGE 2: Intelligent Transcription**
4. **TST-057A**: Auto-Select Method (1 min)

5. **TST-057B-D**: Transcribe (Choose one)
   - 057B: Google AI Studio (20-40 min, ≤20 min videos)
   - 057C: TurboScribe (2-5 min, >20 min videos)
   - 057D: Local Whisper (10-30 min, privacy)

6. **TST-057E**: Quality Check (5-10 min)

7. **TST-057F**: Capture Metadata (5-10 min)

### **STAGE 3: Queue & Automation**
8. **TST-059A**: Initialize Queue (2 min)

9. **TST-059B**: Add to Queue (1 min per video)

10. **TST-059C**: Process from Queue (auto)

11. **TST-059D**: Batch Process (auto)

### **STAGE 4: Extraction & Population** (Existing)
12. **TST-052**: Extract Taxonomy (15-30 min)

13. **TST-053**: Validate Taxonomy (5-10 min)

14. **TST-058**: Populate Libraries (10-20 min)

---

## Implementation Priority

### **Phase 1: Core Enhancements**
- Enhanced review checklist with complete metadata capture
- Queue export format and initialization
- Auto-select transcription logic (40 min threshold)
- TurboScribe workflow documentation
- Metadata capture templates

### **Phase 2: Automation Scripts**
- Queue initialization script
- Add to queue script
- Single video processor
- Convert existing videos to new format

### **Phase 3: Multi-AI Research**
- Gemini Deep Research workflow
- ChatGPT Search workflow
- Grok workflow
- Hybrid multi-AI workflow

### **Phase 4: Advanced Features**
- Batch processing capabilities
- Local Whisper setup
- Dashboard for queue monitoring
- Automated library population pipeline

---

## Benefits of Expansion

### **Flexibility**
- ✅ Choose AI platform based on task (speed vs depth)
- ✅ Choose transcription method based on video length
- ✅ Manual checkpoints for quality control
- ✅ Automated batch processing when ready

### **Scalability**
- ✅ Queue system handles large video batches
- ✅ Parallel processing possible
- ✅ Batch operations for efficiency
- ✅ Clear status tracking

### **Quality**
- ✅ Multi-AI research catches more videos
- ✅ Better transcription for long videos
- ✅ Complete metadata capture (channel, links, likes)
- ✅ Quality checkpoints prevent bad data

### **Data Completeness**
- ✅ Channel URL always captured
- ✅ Video URL preserved separately
- ✅ Links from description included
- ✅ Engagement metrics tracked
- ✅ Processing history maintained

---

## Next Steps

1. Review expansion plan
2. Prioritize features based on immediate needs
3. Create new task templates (TST-050B through TST-059D)
4. Create new milestone templates for expanded stages
5. Build automation scripts for queue management
6. Test with pilot videos
7. Document learnings and refine workflows

---

**Status:** Ready for Implementation

---

**End of Expansion Plan**
