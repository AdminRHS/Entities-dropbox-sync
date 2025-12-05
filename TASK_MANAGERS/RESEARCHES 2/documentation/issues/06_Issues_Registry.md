# Issues Registry: RESEARCHES System

**Document ID:** DOC-RES-006
**Version:** 1.0
**Date:** 2025-12-03
**Status:** ✅ Active Registry
**Last Updated:** 2025-12-03

---

## Purpose

This registry documents all identified issues, problems, and improvement opportunities for the RESEARCHES system. Each issue receives a unique `ISS-RES-XXX` identifier and includes priority, impact assessment, proposed solutions, and tracking information.

---

## Issue ID Format: ISS-RES-XXX

**Components:**
- `ISS` = Issue
- `RES` = RESEARCHES module
- `XXX` = Sequential number (001-999)

**Example:** `ISS-RES-011`

---

## Priority Categories

| Priority | Criteria | Response Time |
|----------|----------|---------------|
| **CRITICAL** | Blocks system operation, data loss risk | Immediate (within hours) |
| **HIGH** | Significantly affects efficiency, productivity impact | 1-2 weeks |
| **MEDIUM** | Desirable to fix, quality improvement | 1-2 months |
| **LOW** | Nice to have, minor enhancement | Future release |

---

## Status Values

- **OPEN** - Issue identified, not yet addressed
- **IN_PROGRESS** - Solution being implemented
- **RESOLVED** - Solution implemented, awaiting verification
- **VERIFIED** - Solution confirmed working
- **CLOSED** - Issue fully closed
- **WONTFIX** - Decided not to fix
- **DUPLICATE** - Duplicate of another issue

---

## Identified Issues

### ISS-RES-001: VIDEO_PROGRESS_TRACKER Desynchronization

**Priority:** HIGH
**Status:** OPEN
**Identified:** 2025-11-24
**Category:** Data Integrity

**Description:**
All 22 videos in VIDEO_PROGRESS_TRACKER.csv show status "Phase_1" (Transcribed), but Master_Video_Status_Overview_2025-11-24.md confirms all 22 videos are actually fully integrated (Complete status). This represents a critical desynchronization between tracking system and actual state.

**Impact:**
- Cannot track actual video processing progress
- Inaccurate reporting to management
- Confusion for team members about video status
- Metrics and dashboards show incorrect data
- Difficult to identify which videos need work

**Root Cause:**
- VIDEO_PROGRESS_TRACKER.csv not updated after manual integration
- Scripts may have been bypassed during integration
- No automated sync mechanism between tracker and actual state

**Evidence:**
- `REPORTS/Master_Video_Status_Overview_2025-11-24.md`: Documents 22/22 videos integrated
- `VIDEO_PROGRESS_TRACKER.csv`: Shows all videos at Phase_1
- `03_ANALYSIS/Library_Mapping/`: Contains mapping reports for all 22 videos

**Proposed Solution:**
1. Create verification script to check for Library_Mapping_Report existence
2. Run batch update: `update_video_progress.py batch-update --from-mapping-reports`
3. Validate CSV after update (all 22 should show "Complete")
4. Generate change report documenting updates
5. Create backup before any modifications

**Related Files:**
- `VIDEO_PROGRESS_TRACKER.csv`
- `scripts/update_video_progress.py`
- `scripts/verify_manual_integration.py`
- `REPORTS/Master_Video_Status_Overview_2025-11-24.md`
- `03_ANALYSIS/Library_Mapping/*.md`

**Related Tasks:**
- TASK-001: Update VIDEO_PROGRESS_TRACKER.csv (PHS-RES-001)
- TASK-003: Create backup of all CSV before changes (PHS-RES-001)

**Effort Estimate:** 2-3 hours
**Assigned To:** System Administrator
**Target Resolution:** PHS-RES-001 (Stabilization phase)

---

### ISS-RES-002: Missing Video_015

**Priority:** LOW
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Data Completeness

**Description:**
The video sequence shows a gap at Video_015. The sequence goes: Video_014 → Video_016 (skips 015). This creates an inconsistency in the sequential numbering system.

**Impact:**
- Breaks sequential numbering pattern
- May confuse users expecting continuous sequence
- Potential issues with automated scripts expecting no gaps
- Historical record incomplete

**Possible Reasons:**
1. Video_015 was processed but later deleted
2. Video_015 was skipped intentionally for quality reasons
3. Processing error occurred and video was abandoned
4. Video_015 was merged with another video

**Proposed Solution:**
Option A: Document the gap
- Add note in `02_TRANSCRIPTIONS/README.md` explaining Video_015
- Update `Video_Queue_Tracker.md` with explanation
- Add to FAQ: "Why is Video_015 missing?"

Option B: Fill the gap
- If video source still available, process as Video_015
- Maintain sequential integrity

Option C: Accept and continue
- Allow gaps in sequence
- Update documentation to note gaps are acceptable

**Related Files:**
- `02_TRANSCRIPTIONS/` (all Video_XXX.md files)
- `02_TRANSCRIPTIONS/README.md`
- `01_VIDEO_QUEUE/Video_Queue_Tracker.md`

**Related Tasks:**
- TASK-005: Document Video_015 (PHS-RES-001)

**Effort Estimate:** 30 minutes (documentation) or 2-3 hours (processing if available)
**Assigned To:** Research Lead
**Target Resolution:** PHS-RES-001 (Stabilization phase)

---

### ISS-RES-003: Conflicting Files

**Priority:** MEDIUM
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** File Management

**Description:**
Conflicting file detected: `PMT-051_YouTube_AI_Design_Tools_Workflows_CONFLICT_2025-11-21.md`. This indicates a merge conflict or duplicate file that was not properly resolved.

**Impact:**
- Unclear which version is current/authoritative
- Risk of using outdated prompt
- Confusion for users selecting prompt to use
- Potential for inconsistent results if wrong version used

**Files Affected:**
- `PROMPTS/PMT-051_YouTube_AI_Design_Tools_Workflows.md` (original)
- `PROMPTS/PMT-051_YouTube_AI_Design_Tools_Workflows_CONFLICT_2025-11-21.md` (conflict)

**Proposed Solution:**
1. Compare both files to identify differences
2. Merge changes if both contain valid updates
3. Keep only the authoritative version
4. Rename old version with `_DEPRECATED_` prefix if needed for history
5. Update any documentation referencing PMT-051
6. Add to .gitignore: `*_CONFLICT_*` patterns

**Resolution Steps:**
```bash
# 1. Compare files
diff PROMPTS/PMT-051_YouTube_AI_Design_Tools_Workflows.md \
     PROMPTS/PMT-051_YouTube_AI_Design_Tools_Workflows_CONFLICT_2025-11-21.md

# 2. If conflict version has updates, merge manually

# 3. Rename old version
mv PROMPTS/PMT-051_YouTube_AI_Design_Tools_Workflows_CONFLICT_2025-11-21.md \
   PROMPTS/ARCHIVE/PMT-051_DEPRECATED_2025-11-21.md

# 4. Document in changelog
```

**Related Files:**
- `PROMPTS/PMT-051*.md`
- `PROMPTS/README_MIGRATION.md`

**Related Tasks:**
- TASK-002: Resolve PMT-051 conflict (PHS-RES-001)

**Effort Estimate:** 1 hour
**Assigned To:** Research Lead
**Target Resolution:** PHS-RES-001 (Stabilization phase)

---

### ISS-RES-004: Missing Progress Dashboard

**Priority:** MEDIUM
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Monitoring

**Description:**
While `Video_Queue_Dashboard.html` exists for queue management, there is no comprehensive dashboard showing progress across all phases (Phase 0 through Complete) for all videos. This makes it difficult to get a quick overview of system activity.

**Impact:**
- No single-page view of all video statuses
- Manual CSV inspection required to check progress
- Difficult to identify bottlenecks in workflow
- Management lacks visual progress reporting
- Cannot easily see which phase has most videos

**Current State:**
- ✅ Have: Video_Queue_Dashboard.html (queue-specific)
- ❌ Missing: Overall progress dashboard
- ❌ Missing: Phase distribution visualization
- ❌ Missing: Completion rate metrics
- ❌ Missing: Processing time trends

**Desired Features:**
1. **Overview Panel:**
   - Total videos processed
   - Videos by phase (bar chart)
   - Completion rate (percentage)
   - Average processing time

2. **Phase Distribution:**
   - Phase 0 (Search): X videos
   - Phase 1 (Transcribed): X videos
   - Phase 2 (Extracted): X videos
   - Phase 3 (Gap Analysis): X videos
   - Phase 4 (Integrated): X videos
   - Phase 5 (Mapped): X videos
   - Complete: X videos

3. **Recent Activity:**
   - Last 5 videos processed
   - Recent status changes
   - Time per phase statistics

4. **Bottleneck Identification:**
   - Phases with longest average duration
   - Videos stuck in a phase > 7 days
   - Alert indicators

**Proposed Solution:**
Create `Progress_Dashboard.html` based on VIDEO_PROGRESS_TRACKER.csv:

**Technical Approach:**
```html
<!-- Use same tech stack as Video_Queue_Dashboard.html -->
<!DOCTYPE html>
<html>
<head>
    <title>RESEARCHES Progress Dashboard</title>
    <!-- Chart.js for visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <!-- Read VIDEO_PROGRESS_TRACKER.csv -->
    <!-- Generate phase distribution chart -->
    <!-- Show completion metrics -->
    <!-- Display recent activity -->
</body>
</html>
```

**Data Source:**
- Primary: `VIDEO_PROGRESS_TRACKER.csv`
- Secondary: `Video_Queue_Master.csv`
- Tertiary: `REPORTS/*.md` files

**Related Files:**
- `01_VIDEO_QUEUE/Video_Queue_Dashboard.html` (template reference)
- `VIDEO_PROGRESS_TRACKER.csv` (data source)
- `scripts/generate_progress_report.py` (existing script for reports)

**Related Tasks:**
- TASK-010: Create Progress_Dashboard.html (PHS-RES-003)
- TASK-011: Add real-time updates to dashboards (PHS-RES-003)

**Effort Estimate:** 6-8 hours (development + testing)
**Assigned To:** Developer
**Target Resolution:** PHS-RES-003 (Monitoring & Dashboards phase)

---

### ISS-RES-005: Non-Automated Phase 2

**Priority:** HIGH
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Automation

**Description:**
Phase 2 (Extraction) using PMT-007 is executed manually, requiring 30-45 minutes of human work per video. This represents the largest automation gap in the system and the highest ROI improvement opportunity.

**Impact:**
- **Time cost:** 30-45 minutes manual work per video
- **Across 28 videos:** 14-21 hours of manual work
- **Annual (100 videos):** 50-75 hours of manual work
- **Consistency:** Human error risk
- **Scalability:** Bottleneck for high-volume processing
- **Employee satisfaction:** Repetitive manual work

**Current Process:**
1. Read `Video_XXX.md` transcription
2. Manually apply PMT-007 (Objects Library Extraction)
3. Extract all entity types:
   - Tools, Workflows, Actions, Objects
   - Processes, Professions, Skills, Results, Parameters
4. Create cross-references manually
5. Write extraction inventory manually
6. Save to `03_ANALYSIS/Extractions/Video_XXX_Extraction_Inventory.md`

**Automation Potential:**
- **Before:** 30-45 min (100% manual)
- **After:** 5-10 min (90% automated)
- **Time saved:** 90% (25-35 min per video)

**Proposed Solution:**
Create `video_extraction_automator.py` script:

**Features:**
1. **Parse Video_XXX.md:**
   - Read transcription
   - Extract existing taxonomy analysis
   - Identify mentioned entities

2. **AI-Assisted Extraction:**
   - Use PMT-007 prompt programmatically
   - Call Claude API or similar
   - Parse structured output

3. **Entity Classification:**
   - Classify each entity by type
   - Determine NEW/EXISTING status
   - Create cross-references automatically

4. **Generate Inventory:**
   - Create standardized markdown output
   - Include counts and statistics
   - Link to Video_XXX source

5. **Validation:**
   - Check entity ID formats
   - Verify cross-references exist
   - Flag inconsistencies for human review

**Implementation Approach:**
```python
# scripts/video_extraction_automator.py
import sys
from pathlib import Path
from markdown_parser import parse_video_transcription
from ai_client import call_claude_api
from entity_classifier import classify_entities
from inventory_generator import generate_inventory

def automate_phase2_extraction(video_id: str):
    """Automate Phase 2 extraction for a video"""

    # 1. Read transcription
    video_path = Path(f"02_TRANSCRIPTIONS/{video_id}.md")
    transcription = parse_video_transcription(video_path)

    # 2. Apply PMT-007 via AI
    prompt = load_prompt("PMT-007")
    extraction_result = call_claude_api(prompt, transcription)

    # 3. Classify entities
    entities = classify_entities(extraction_result)

    # 4. Generate inventory
    inventory = generate_inventory(video_id, entities)

    # 5. Save output
    output_path = Path(f"03_ANALYSIS/Extractions/{video_id}_Extraction_Inventory.md")
    output_path.write_text(inventory)

    print(f"✅ Extraction complete for {video_id}")
    print(f"   Entities extracted: {len(entities)}")
    print(f"   Output: {output_path}")
```

**Dependencies:**
- Claude API key (or alternative AI service)
- `markdown_parser.py` (parse Video_XXX.md)
- `ai_client.py` (call AI API)
- `entity_classifier.py` (classify entities)
- `inventory_generator.py` (generate markdown output)

**Testing Plan:**
1. Test on Video_001 (known good result)
2. Compare automated vs manual extraction
3. Validate accuracy (target: 95%+)
4. Test on 5 additional videos
5. Full rollout after validation

**Related Files:**
- `scripts/` (new automation script)
- `PROMPTS/PMT-007` (extraction prompt)
- `02_TRANSCRIPTIONS/Video_*.md` (input)
- `03_ANALYSIS/Extractions/` (output)

**Related Tasks:**
- TASK-006: Create video_extraction_automator.py (PHS-RES-002)

**Effort Estimate:** 2-3 days development + 1 day testing
**Assigned To:** Senior Developer
**Target Resolution:** PHS-RES-002 (Automation Enhancement phase)
**Expected Savings:** 25-35 minutes per video (14-21 hours across 28 videos)

---

### ISS-RES-006: Missing Batch Processing

**Priority:** MEDIUM
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Efficiency

**Description:**
The current `process_video.py` script processes only one video at a time. For bulk operations (e.g., processing 10-20 videos from queue), this is inefficient as it requires manual intervention between each video.

**Impact:**
- Cannot process multiple videos unattended
- Requires manual script re-runs
- Inefficient for bulk operations
- Longer time to process queue backlog
- Cannot leverage overnight/weekend processing

**Current Usage:**
```bash
# Must run separately for each video
python scripts/process_video.py Video_024
python scripts/process_video.py Video_025
python scripts/process_video.py Video_026
# ... repeat 20 times
```

**Desired Usage:**
```bash
# Option 1: Batch list
python scripts/process_video.py --batch Video_024 Video_025 Video_026

# Option 2: Range
python scripts/process_video.py --batch-range Video_024 Video_030

# Option 3: All pending
python scripts/process_video.py --batch-all-pending

# Option 4: Top N by priority
python scripts/process_video.py --batch-top 10
```

**Proposed Solution:**
Add `--batch` flag to `process_video.py`:

**Implementation:**
```python
# scripts/process_video.py (modified)
import argparse
from typing import List

def process_batch(video_ids: List[str], auto_approve: bool = False):
    """Process multiple videos in sequence"""
    results = []

    for video_id in video_ids:
        print(f"\n{'='*60}")
        print(f"Processing {video_id} ({video_ids.index(video_id)+1}/{len(video_ids)})")
        print(f"{'='*60}\n")

        try:
            result = process_single_video(video_id, auto_approve)
            results.append({'video': video_id, 'status': 'success', 'result': result})
        except Exception as e:
            results.append({'video': video_id, 'status': 'error', 'error': str(e)})
            print(f"❌ Error processing {video_id}: {e}")

            # Ask user if should continue
            if not auto_approve:
                continue_batch = input("Continue with remaining videos? (y/n): ")
                if continue_batch.lower() != 'y':
                    break

    # Generate batch report
    generate_batch_report(results)
    return results

def main():
    parser = argparse.ArgumentParser(description='Process RESEARCHES videos')
    parser.add_argument('video_id', nargs='?', help='Single video ID (e.g., Video_024)')
    parser.add_argument('--batch', nargs='+', help='Process multiple videos')
    parser.add_argument('--batch-range', nargs=2, help='Process range of videos')
    parser.add_argument('--batch-all-pending', action='store_true',
                       help='Process all pending videos')
    parser.add_argument('--batch-top', type=int, help='Process top N by priority')
    parser.add_argument('--auto-approve', action='store_true',
                       help='Auto-approve all prompts')

    args = parser.parse_args()

    # Determine video list
    if args.batch:
        video_ids = args.batch
    elif args.batch_range:
        video_ids = generate_range(args.batch_range[0], args.batch_range[1])
    elif args.batch_all_pending:
        video_ids = get_pending_videos()
    elif args.batch_top:
        video_ids = get_top_priority_videos(args.batch_top)
    elif args.video_id:
        video_ids = [args.video_id]
    else:
        parser.error("Must specify video_id or batch options")

    # Process
    if len(video_ids) > 1:
        process_batch(video_ids, args.auto_approve)
    else:
        process_single_video(video_ids[0], args.auto_approve)
```

**Additional Features:**
- Pause/resume capability
- Progress bar for batch
- Batch report generation
- Error handling and recovery
- Dry-run mode for batch

**Related Files:**
- `scripts/process_video.py` (modify)
- `scripts/config.py` (add batch settings)

**Related Tasks:**
- TASK-007: Add --batch to process_video.py (PHS-RES-002)

**Effort Estimate:** 1 day development + testing
**Assigned To:** Developer
**Target Resolution:** PHS-RES-002 (Automation Enhancement phase)

---

### ISS-RES-007: JSON Files Without Pretty Formatting

**Priority:** LOW
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Code Quality

**Description:**
Some JSON files in LIBRARIES and TASK_MANAGERS may not have consistent pretty-print formatting (indentation, line breaks). This makes manual editing and version control diffs more difficult.

**Impact:**
- Difficult to read JSON files manually
- Git diffs show entire file changed when only one field modified
- Harder to spot errors in JSON structure
- Inconsistent formatting across files
- Merge conflicts more likely

**Example (Bad):**
```json
{"tool_id":"TOL-AI-223","name":"Browse AI","category":"Automation/Web_Automation","features":["no-code","chrome-extension"]}
```

**Example (Good):**
```json
{
  "tool_id": "TOL-AI-223",
  "name": "Browse AI",
  "category": "Automation/Web_Automation",
  "features": [
    "no-code",
    "chrome-extension"
  ]
}
```

**Proposed Solution:**
Add formatting validation to `utils.py`:

**Implementation:**
```python
# scripts/utils.py (add function)
import json
from pathlib import Path
from typing import Any, Dict

def save_json_pretty(file_path: Path, data: Dict[str, Any],
                    indent: int = 2, sort_keys: bool = True) -> None:
    """Save JSON with pretty formatting"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, sort_keys=sort_keys,
                 ensure_ascii=False)
        f.write('\n')  # Add trailing newline

def validate_json_formatting(file_path: Path) -> bool:
    """Check if JSON file has proper formatting"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        data = json.loads(content)
        formatted = json.dumps(data, indent=2, sort_keys=True,
                             ensure_ascii=False) + '\n'
        return content == formatted
    except json.JSONDecodeError:
        return False

def reformat_all_json_files(directory: Path) -> List[Path]:
    """Reformat all JSON files in directory"""
    reformatted = []

    for json_file in directory.rglob('*.json'):
        if not validate_json_formatting(json_file):
            data = load_json(json_file)
            save_json_pretty(json_file, data)
            reformatted.append(json_file)

    return reformatted
```

**Script Usage:**
```bash
# Validate all JSON files
python scripts/validate_json_formatting.py --check

# Reformat all JSON files
python scripts/validate_json_formatting.py --fix

# Check specific directory
python scripts/validate_json_formatting.py --check LIBRARIES/LBS_003_Tools/
```

**Related Files:**
- `scripts/utils.py` (add functions)
- `scripts/validate_json_formatting.py` (new script)
- All `*.json` files in LIBRARIES/ and TASK_MANAGERS/

**Related Tasks:**
- TASK-004: Validate all JSON files (PHS-RES-001)

**Effort Estimate:** 2-3 hours
**Assigned To:** Developer
**Target Resolution:** PHS-RES-001 (Stabilization phase)

---

### ISS-RES-008: Missing YouTube API Integration

**Priority:** MEDIUM
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Automation

**Description:**
Video metadata (title, channel, views, likes, duration, description) is entered manually when adding videos to the queue. YouTube Data API v3 can automatically fetch all this information from a video URL, saving 5-10 minutes per video.

**Impact:**
- **Time cost:** 5-10 minutes manual data entry per video
- **Across 28 videos:** 2.3-4.7 hours of manual work
- **Annual (100 videos):** 8.3-16.7 hours of manual work
- **Errors:** Typos in titles, channel names
- **Incomplete data:** May miss important metadata
- **Effort:** Tedious manual copy-paste work

**Current Process:**
```bash
python scripts/add_video_to_queue_simple.py
# Enter URL: https://youtube.com/watch?v=xxx
# Enter Title: (copy-paste from browser)
# Enter Channel: (copy-paste from browser)
# Enter Duration: (copy-paste from browser)
# ... etc
```

**Desired Process:**
```bash
python scripts/add_video_to_queue_simple.py
# Enter URL: https://youtube.com/watch?v=xxx
# ✅ Fetching metadata from YouTube...
# ✅ Title: Retrieved automatically
# ✅ Channel: Retrieved automatically
# ✅ Duration: Retrieved automatically
# ✅ Views: Retrieved automatically
# ✅ Likes: Retrieved automatically
# Confirm? (y/n):
```

**Proposed Solution:**
Integrate YouTube Data API v3:

**Implementation:**
```python
# scripts/youtube_api.py (new)
import os
import requests
from typing import Dict, Optional

class YouTubeAPI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('YOUTUBE_API_KEY')
        if not self.api_key:
            raise ValueError("YouTube API key required")
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def get_video_metadata(self, video_url: str) -> Dict[str, any]:
        """Fetch video metadata from YouTube"""
        video_id = self._extract_video_id(video_url)

        # Call YouTube API
        response = requests.get(
            f"{self.base_url}/videos",
            params={
                'part': 'snippet,statistics,contentDetails',
                'id': video_id,
                'key': self.api_key
            }
        )

        if response.status_code != 200:
            raise Exception(f"YouTube API error: {response.status_code}")

        data = response.json()
        if not data.get('items'):
            raise Exception(f"Video not found: {video_id}")

        item = data['items'][0]

        return {
            'video_id': video_id,
            'title': item['snippet']['title'],
            'channel_name': item['snippet']['channelTitle'],
            'channel_id': item['snippet']['channelId'],
            'description': item['snippet']['description'],
            'published_at': item['snippet']['publishedAt'],
            'duration': self._parse_duration(item['contentDetails']['duration']),
            'views': int(item['statistics'].get('viewCount', 0)),
            'likes': int(item['statistics'].get('likeCount', 0)),
            'comments': int(item['statistics'].get('commentCount', 0)),
            'category_id': item['snippet']['categoryId'],
            'tags': item['snippet'].get('tags', []),
            'thumbnail_url': item['snippet']['thumbnails']['high']['url']
        }

    def _extract_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL"""
        import re
        patterns = [
            r'(?:v=|/)([0-9A-Za-z_-]{11}).*',
            r'(?:embed/)([0-9A-Za-z_-]{11})',
            r'^([0-9A-Za-z_-]{11})$'
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        raise ValueError(f"Could not extract video ID from: {url}")

    def _parse_duration(self, iso_duration: str) -> str:
        """Convert ISO 8601 duration to readable format"""
        import isodate
        duration = isodate.parse_duration(iso_duration)
        minutes = int(duration.total_seconds() // 60)
        seconds = int(duration.total_seconds() % 60)
        return f"{minutes}:{seconds:02d}"

# Modify add_video_to_queue_simple.py
from youtube_api import YouTubeAPI

def add_video_with_api(video_url: str):
    """Add video using YouTube API"""
    print(f"🔍 Fetching metadata from YouTube...")

    try:
        api = YouTubeAPI()
        metadata = api.get_video_metadata(video_url)

        print(f"✅ Title: {metadata['title']}")
        print(f"✅ Channel: {metadata['channel_name']}")
        print(f"✅ Duration: {metadata['duration']}")
        print(f"✅ Views: {metadata['views']:,}")
        print(f"✅ Likes: {metadata['likes']:,}")

        confirm = input("\nAdd to queue? (y/n): ")
        if confirm.lower() == 'y':
            add_to_queue(metadata)
            print("✅ Video added to queue")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Falling back to manual entry...")
        manual_entry(video_url)
```

**Setup Requirements:**
1. Get YouTube Data API v3 key from Google Cloud Console
2. Store key in environment variable: `YOUTUBE_API_KEY`
3. Install dependencies: `pip install isodate requests`
4. Update `add_video_to_queue_simple.py` to use API

**Fallback:**
If API unavailable, fall back to manual entry (current behavior)

**Related Files:**
- `scripts/youtube_api.py` (new)
- `scripts/add_video_to_queue_simple.py` (modify)
- `scripts/add_video_to_queue.py` (modify)

**Related Tasks:**
- TASK-008: Integrate YouTube API (PHS-RES-002)

**Effort Estimate:** 1 day development + API setup
**Assigned To:** Developer
**Target Resolution:** PHS-RES-002 (Automation Enhancement phase)
**Expected Savings:** 5-10 minutes per video

---

### ISS-RES-009: No ML for Prioritization

**Priority:** LOW
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Enhancement

**Description:**
Current priority calculation uses a simple formula (views×30% + likes×20% + recency×30% + engagement×20%). A machine learning model could provide smarter prioritization based on historical usefulness, topic relevance, and organizational needs.

**Impact:**
- Possibly suboptimal video selection
- Cannot learn from historical data
- Simple formula may miss important signals
- No personalization by department needs
- Cannot predict video usefulness before processing

**Current Formula:**
```python
def calculate_priority(views, likes, published_date, engagement_rate):
    views_score = min(views / 1_000_000 * 30, 30)
    likes_score = min(likes / 50_000 * 20, 20)
    recency_score = calculate_recency_score(published_date) * 30
    engagement_score = engagement_rate * 20
    return views_score + likes_score + recency_score + engagement_score
```

**Limitations:**
- Fixed weights (cannot adapt)
- Linear relationships (may not be accurate)
- No topic modeling
- No historical learning
- No department-specific needs

**Proposed ML Approach:**

**Features (Input):**
- Video metadata: views, likes, duration, channel subscribers
- Temporal: published date, days since published, trending velocity
- Content: title keywords, description, tags, category
- Channel: creator authority, channel focus, video count
- Historical: similar videos processed, their usefulness scores
- Context: department gaps, current priorities, topic trends

**Target (Output):**
- **Usefulness score** (0-100): How useful will this video be?
  - Based on historical data: which videos led to valuable entities
  - Department needs: gaps in current taxonomy
  - Topic relevance: aligns with strategic priorities

**Model Types to Consider:**
1. **Gradient Boosting (XGBoost):** Best for tabular data, interpretable
2. **Neural Network:** Can learn complex patterns
3. **Ensemble:** Combine multiple models for robustness

**Training Data:**
- Historical videos: 28 processed videos
- Usefulness labels:
  - High: Videos that created 10+ valuable entities
  - Medium: Videos that created 5-9 entities
  - Low: Videos that created <5 entities or duplicates
- Feature engineering from video metadata

**Implementation Steps:**
1. Collect historical data (28 videos)
2. Engineer features
3. Train model (start with XGBoost)
4. Validate on held-out set (80/20 split)
5. A/B test: ML vs formula
6. Measure improvement in average usefulness

**Success Criteria:**
- ML model outperforms formula by 15%+ on usefulness prediction
- Interpretable feature importance
- Can retrain as more data collected

**Proposed Solution:**
```python
# scripts/ml_prioritization.py (new)
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

class MLPrioritizer:
    def __init__(self):
        self.model = None
        self.feature_names = None

    def prepare_features(self, video_metadata):
        """Engineer features from metadata"""
        features = {
            # Popularity signals
            'log_views': np.log1p(video_metadata['views']),
            'log_likes': np.log1p(video_metadata['likes']),
            'engagement_rate': video_metadata['likes'] / max(video_metadata['views'], 1),

            # Temporal signals
            'days_since_published': (datetime.now() - video_metadata['published_at']).days,
            'is_recent': int(days_since_published <= 30),

            # Content signals
            'duration_minutes': video_metadata['duration'] / 60,
            'title_length': len(video_metadata['title']),
            'has_ai_keyword': int('AI' in video_metadata['title'].upper()),

            # Channel signals
            'channel_authority': self.get_channel_authority(video_metadata['channel_id']),

            # Historical signals
            'similar_videos_usefulness': self.get_similar_videos_score(video_metadata)
        }
        return pd.DataFrame([features])

    def train(self, historical_data):
        """Train ML model on historical videos"""
        X = pd.concat([self.prepare_features(v) for v in historical_data])
        y = [v['usefulness_score'] for v in historical_data]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        self.model = XGBRegressor(n_estimators=100, max_depth=5)
        self.model.fit(X_train, y_train)

        # Evaluate
        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)

        print(f"Train R²: {train_score:.3f}")
        print(f"Test R²: {test_score:.3f}")

        # Feature importance
        importance = pd.DataFrame({
            'feature': X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        print("\nFeature Importance:")
        print(importance)

    def predict_priority(self, video_metadata):
        """Predict usefulness score for new video"""
        if not self.model:
            raise ValueError("Model not trained")

        features = self.prepare_features(video_metadata)
        return self.model.predict(features)[0]
```

**Related Files:**
- `scripts/ml_prioritization.py` (new)
- `scripts/calculate_priority.py` (modify to add ML option)
- Historical data: All Video_XXX.md + usefulness labels

**Related Tasks:**
- TASK-019: Create ML model for priority scoring (PHS-RES-005)
- TASK-022: A/B testing ML vs rule-based (PHS-RES-005)

**Effort Estimate:** 1 week (data prep + modeling + validation)
**Assigned To:** Data Scientist / ML Engineer
**Target Resolution:** PHS-RES-005 (AI/ML Integration phase - v2.0)
**Expected Improvement:** 15-20% better usefulness prediction

---

### ISS-RES-010: Missing Tests

**Priority:** HIGH
**Status:** OPEN
**Identified:** 2025-12-03
**Category:** Quality Assurance

**Description:**
The system has 16 Python scripts but no automated unit tests. This creates risk of regressions when modifying code, makes maintenance difficult, and slows down development velocity.

**Impact:**
- **Regression risk:** Changes may break existing functionality
- **Slow development:** Must manually test after every change
- **Difficult maintenance:** Unclear if changes break anything
- **Low confidence:** Fear of modifying existing code
- **No CI/CD:** Cannot set up automated testing pipeline

**Current Scripts (No Tests):**
1. `process_video.py` - Main orchestrator
2. `video_id_scanner.py` - ID discovery
3. `video_gap_analyzer.py` - Gap analysis
4. `video_json_updater.py` - JSON updates
5. `video_integration_reporter.py` - Reporting
6. `markdown_parser.py` - MD parsing
7. `analyze_video_phases.py` - Phase analysis
8. `check_prompts_compliance.py` - Prompt validation
9. `update_video_progress.py` - Progress tracking
10. `generate_progress_report.py` - Report generation
11. `verify_manual_integration.py` - Integration verification
12. `validate_taxonomy.py` - Taxonomy validation
13. `config.py` - Configuration
14. `utils.py` - Utilities
15. `requirements.txt` - Dependencies
16. `add_video_to_queue*.py` - Queue scripts

**Proposed Solution:**
Create comprehensive test suite with pytest:

**Test Structure:**
```
scripts/
├── tests/
│   ├── __init__.py
│   ├── conftest.py (fixtures)
│   ├── test_process_video.py
│   ├── test_video_id_scanner.py
│   ├── test_video_gap_analyzer.py
│   ├── test_video_json_updater.py
│   ├── test_video_integration_reporter.py
│   ├── test_markdown_parser.py
│   ├── test_analyze_video_phases.py
│   ├── test_check_prompts_compliance.py
│   ├── test_update_video_progress.py
│   ├── test_generate_progress_report.py
│   ├── test_verify_manual_integration.py
│   ├── test_validate_taxonomy.py
│   ├── test_config.py
│   ├── test_utils.py
│   ├── fixtures/
│   │   ├── sample_video.md
│   │   ├── sample_queue.csv
│   │   ├── sample_tool.json
│   │   └── sample_workflow.json
│   └── integration/
│       └── test_full_workflow.py
├── pytest.ini
├── .coveragerc
└── requirements-dev.txt (add pytest, pytest-cov)
```

**Example Test:**
```python
# tests/test_utils.py
import pytest
from pathlib import Path
from utils import load_json, save_json, backup_file, validate_entity_id

class TestUtils:
    def test_load_json_valid(self, tmp_path):
        """Test loading valid JSON file"""
        json_file = tmp_path / "test.json"
        json_file.write_text('{"key": "value"}')

        result = load_json(json_file)
        assert result == {"key": "value"}

    def test_load_json_invalid(self, tmp_path):
        """Test loading invalid JSON file"""
        json_file = tmp_path / "test.json"
        json_file.write_text('invalid json')

        with pytest.raises(json.JSONDecodeError):
            load_json(json_file)

    def test_backup_file(self, tmp_path):
        """Test file backup creation"""
        original = tmp_path / "original.json"
        original.write_text('{"data": "original"}')

        backup_path = backup_file(original)

        assert backup_path.exists()
        assert backup_path.parent.name == "_backups"
        assert "original" in backup_path.name

    @pytest.mark.parametrize("entity_id,expected", [
        ("WRF-025", True),
        ("TOL-AI-223", True),
        ("OBJ-SMM-015", True),
        ("SKL-065", True),
        ("INVALID", False),
        ("WRF-", False),
        ("WRF-999999", False),
    ])
    def test_validate_entity_id(self, entity_id, expected):
        """Test entity ID validation"""
        assert validate_entity_id(entity_id) == expected

# tests/test_markdown_parser.py
import pytest
from markdown_parser import parse_video_transcription, extract_entities

class TestMarkdownParser:
    def test_parse_video_metadata(self, sample_video_file):
        """Test parsing video metadata"""
        result = parse_video_transcription(sample_video_file)

        assert result['title'] == "n8n Quickstart"
        assert result['channel'] == "Max Tkacz"
        assert result['duration'] == "14:38"

    def test_extract_workflows(self, sample_video_file):
        """Test extracting workflows from video"""
        entities = extract_entities(sample_video_file)

        assert len(entities['workflows']) > 0
        assert any('WRF' in w['id'] for w in entities['workflows'])

    def test_extract_tools(self, sample_video_file):
        """Test extracting tools from video"""
        entities = extract_entities(sample_video_file)

        assert len(entities['tools']) > 0
        assert any('TOL' in t['id'] for t in entities['tools'])

# tests/conftest.py
import pytest
from pathlib import Path

@pytest.fixture
def sample_video_file(tmp_path):
    """Create sample video markdown file"""
    content = """
    # Video Title: n8n Quickstart

    **Channel/Creator:** Max Tkacz
    **Duration:** 14:38
    **URL:** https://youtube.com/watch?v=xxx

    ## Workflows Identified

    ### WRF-025: Create Social Media Caption
    ...
    """

    video_file = tmp_path / "Video_024.md"
    video_file.write_text(content)
    return video_file

@pytest.fixture
def sample_tool_json(tmp_path):
    """Create sample tool JSON"""
    tool = {
        "tool_id": "TOL-AI-223",
        "name": "Browse AI",
        "category": "Automation"
    }

    tool_file = tmp_path / "TOL-AI-223.json"
    tool_file.write_text(json.dumps(tool, indent=2))
    return tool_file
```

**Testing Commands:**
```bash
# Install test dependencies
pip install pytest pytest-cov pytest-mock

# Run all tests
pytest scripts/tests/

# Run with coverage
pytest --cov=scripts scripts/tests/

# Run specific test file
pytest scripts/tests/test_utils.py

# Run with verbose output
pytest -v scripts/tests/

# Generate HTML coverage report
pytest --cov=scripts --cov-report=html scripts/tests/
```

**Coverage Target:**
- **Phase 1:** 60% coverage (core utilities)
- **Phase 2:** 80% coverage (all scripts)
- **Phase 3:** 90% coverage (including edge cases)

**CI/CD Integration:**
```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r scripts/requirements-dev.txt
      - name: Run tests
        run: pytest --cov=scripts scripts/tests/
      - name: Check coverage
        run: pytest --cov=scripts --cov-fail-under=80 scripts/tests/
```

**Related Files:**
- `scripts/tests/` (new directory)
- `scripts/pytest.ini` (new)
- `scripts/.coveragerc` (new)
- `scripts/requirements-dev.txt` (new)
- `.github/workflows/tests.yml` (new, if using GitHub)

**Related Tasks:**
- TASK-014: Create tests/ folder (PHS-RES-004)
- TASK-015: Unit tests for all scripts (PHS-RES-004)
- TASK-016: Integration tests for workflow (PHS-RES-004)
- TASK-017: CI/CD pipeline (PHS-RES-004)
- TASK-018: Code coverage > 80% (PHS-RES-004)

**Effort Estimate:** 1-2 weeks
**Assigned To:** QA Engineer + Developers
**Target Resolution:** PHS-RES-004 (Quality Assurance phase - v2.0)

---

### ISS-RES-011: Missing Unified ID System for Documentation Elements

**Priority:** HIGH
**Status:** ✅ RESOLVED
**Identified:** 2025-12-03
**Resolved:** 2025-12-03
**Category:** Documentation

**Description:**
There was no standardized ID system for issues, phases, tasks, and changes in the RESEARCHES documentation. This made it difficult to track relationships between documents, tasks, and system changes.

**Impact:**
- Cannot reference issues consistently
- No way to track which tasks resolve which issues
- Difficult to link changes to issues/tasks
- No standard for changelog entries
- Hard to maintain traceability

**Solution Implemented:**
Created `04_ID_System_Standard.md` with comprehensive ID standards:

**New ID Systems:**
- **ISS-RES-XXX:** Issues (this registry)
- **PHS-RES-XXX:** Development phases
- **TASK-XXX:** Tasks
- **CHG-RES-YYYYMMDD-XXX:** Changes
- **DOC-RES-XXX:** Documentation files

**Benefits:**
- ✅ Consistent ID format across all documentation
- ✅ Easy cross-referencing between documents
- ✅ Traceability from issue → task → change
- ✅ Standard changelog format
- ✅ Validation patterns for all IDs

**Related Files:**
- `documentation/technical/04_ID_System_Standard.md` (NEW - complete specification)

**Related Changes:**
- CHG-RES-20251203-001: Documentation package creation (includes this solution)

**Effort Actual:** 3-4 hours
**Completed By:** Technical Architect
**Verification:** All documentation uses new ID system

---

### ISS-RES-012: Missing Changelog System

**Priority:** HIGH
**Status:** ✅ RESOLVED
**Identified:** 2025-12-03
**Resolved:** 2025-12-03
**Category:** Change Management

**Description:**
There was no unified system for tracking changes to the RESEARCHES system. This made it impossible to understand what changed, when, why, and by whom.

**Impact:**
- Cannot trace change history
- Unclear what modifications were made
- No record of why changes occurred
- Difficult to rollback changes
- No audit trail

**Solution Implemented:**
Created `14_Changelog_System.md` with comprehensive change tracking:

**Changelog Features:**
- **CHG-RES-YYYYMMDD-XXX ID format**
- **Change categories:** FEATURE, BUGFIX, IMPROVEMENT, DOCS, REFACTOR, DEPRECATED
- **Structured entries:** Type, Author, Description, Files, Impact, Related Issues/Tasks
- **Automation support:** Scripts for adding entries, syncing with git, generating reports
- **Git integration:** Commit message standards

**Benefits:**
- ✅ Complete change history
- ✅ Links changes to issues and tasks
- ✅ Automatic entry generation possible
- ✅ Monthly/yearly reports
- ✅ Audit trail for compliance

**Related Files:**
- `documentation/changelog/14_Changelog_System.md` (NEW - complete specification)
- `scripts/update_changelog.py` (PLANNED - automation)

**Related Changes:**
- CHG-RES-20251203-001: Documentation package creation (includes this solution)

**Effort Actual:** 2-3 hours
**Completed By:** Technical Architect
**Verification:** Changelog system documented with examples

---

## Summary Statistics

**Total Issues:** 12

**By Priority:**
- CRITICAL: 0
- HIGH: 5 (ISS-RES-001, ISS-RES-005, ISS-RES-010, ISS-RES-011 ✅, ISS-RES-012 ✅)
- MEDIUM: 5 (ISS-RES-003, ISS-RES-004, ISS-RES-006, ISS-RES-008, ISS-RES-009)
- LOW: 2 (ISS-RES-002, ISS-RES-007)

**By Status:**
- OPEN: 10
- RESOLVED: 2 (ISS-RES-011, ISS-RES-012)

**By Category:**
- Data Integrity: 1
- Data Completeness: 1
- File Management: 1
- Monitoring: 1
- Automation: 3
- Efficiency: 1
- Code Quality: 1
- Enhancement: 1
- Documentation: 1 ✅
- Change Management: 1 ✅

**Total Estimated Effort (Remaining):**
- HIGH priority: ~4-5 weeks
- MEDIUM priority: ~2-3 weeks
- LOW priority: ~1 week
- **Total:** ~7-9 weeks of development effort

---

## Issue Tracking Process

### Creating New Issues

1. **Identify issue** through monitoring, user feedback, or code review
2. **Assign ISS-RES-XXX ID** using next available number
3. **Document issue** using template below
4. **Set priority** based on impact and urgency
5. **Add to this registry** in appropriate section
6. **Link related files** and potential tasks
7. **Notify stakeholders** if HIGH or CRITICAL

### Issue Template

```markdown
### ISS-RES-XXX: Issue Title

**Priority:** CRITICAL/HIGH/MEDIUM/LOW
**Status:** OPEN
**Identified:** YYYY-MM-DD
**Category:** Category Name

**Description:**
[Detailed description of the issue]

**Impact:**
- [Impact point 1]
- [Impact point 2]

**Proposed Solution:**
[Solution description]

**Related Files:**
- [file1]
- [file2]

**Related Tasks:**
- TASK-XXX

**Effort Estimate:** [time]
**Assigned To:** [name]
**Target Resolution:** [phase]
```

### Resolving Issues

1. **Implement solution** and test thoroughly
2. **Update status** to RESOLVED
3. **Add resolution date** and details
4. **Link to implementing change** (CHG-RES-XXX)
5. **Document verification** process
6. **Close issue** after verification (status = CLOSED)

---

## Related Documents

- [04_ID_System_Standard.md](../technical/04_ID_System_Standard.md) - ID system specification
- [07_Development_Roadmap.md](../phases/07_Development_Roadmap.md) - Tasks that resolve issues
- [14_Changelog_System.md](../changelog/14_Changelog_System.md) - Changes that address issues
- [01_Executive_Summary.md](../technical/01_Executive_Summary.md) - High-level issue overview

---

**Registry Owner:** Quality Assurance Lead
**Review Cycle:** Weekly (for HIGH/CRITICAL), Monthly (for others)
**Next Review:** 2025-12-10

**Generated by:** Claude Code (Anthropic)
**Changelog Entry:** CHG-RES-20251203-001
