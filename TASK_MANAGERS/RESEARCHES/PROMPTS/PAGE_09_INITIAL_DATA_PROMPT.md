# PAGE 9: IMPORT REAL DATA FROM TRANSCRIPTIONS

**Convert your existing transcription files into app-ready data**

---

## WHAT THIS DOES

You already have 24 complete video transcriptions in `02_TRANSCRIPTIONS`. This prompt helps convert those real files into data the app can use.

---

## YOUR EXISTING DATA

Location: `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\02_TRANSCRIPTIONS`

**What you have:**
- 24 complete video transcriptions (Video_001.md through Video_028.md)
- VIDEOS_INDEX.md with metadata table
- 2 JSON format files (Video_027.json, Video_028.json)
- Timestamps, links, full transcriptions
- Topics and tool references (embedded in text)

**What's missing:**
- Channel names (mostly "Unknown" or empty)
- Publication dates (mostly empty)
- View counts, likes (not captured)
- Structured entity extraction (workflows, tools, actions)

---

## STEP 1: EXTRACT BASIC VIDEO DATA

### Prompt to Give AI:

```
I have video transcription files and need to convert them into structured JSON data for my app.

Here is the VIDEOS_INDEX.md content:
[PASTE THE ENTIRE VIDEOS_INDEX.MD TABLE HERE]

Extract this into a JSON array with this structure:

```javascript
[
  {
    "id": "VIDEO-001",
    "video_id": "",  // Leave empty if not found
    "youtube_url": "",  // Leave empty
    "title": "How To Use AI Agents to 10x Your Creative AI Game",
    "channel": "Unknown",  // Use creator column or "Unknown"
    "duration": "13:00",  // From VIDEOS_INDEX
    "views": 0,  // Not available
    "likes": 0,  // Not available
    "published_date": "",  // Not available
    "topic_id": "TOPIC-001",  // Assign based on topics
    "status": "COMPLETE",  // All are complete
    "date_added": "2024-11-20",  // Use today's date or extraction date
    "date_completed": "2024-11-25",  // Use today's date
    "total_days": 5,
    "stage_dates": {
      "queued": "2024-11-20",
      "selected": "2024-11-21",
      "transcribing": "2024-11-22",
      "analyzed": "2024-11-24",
      "integrated": "2024-11-25",
      "complete": "2024-11-25"
    },
    "transcription": "",  // Will add separately
    "extracted_entities": {
      "tools": [],  // Will extract from transcription
      "workflows": [],
      "actions": [],
      "skills": []
    },
    "topics_mentioned": ["AI agents", "GLIF", "creative workflows"]  // From VIDEOS_INDEX
  }
]
```

Only include videos marked as "✅ Complete" in VIDEOS_INDEX.

Output the complete JSON array ready to paste.
```

---

## STEP 2: ADD TRANSCRIPTION TEXT

For each video, you need to add the actual transcription content.

### Option A: Manual Copy-Paste

1. Open `Video_001.md`
2. Copy everything from `[00:00]` to the end
3. In your video JSON, set:
   ```javascript
   "transcription": "paste full transcription here..."
   ```

### Option B: AI-Assisted Extraction

```
I will give you a transcription file (Video_###.md). Extract just the transcription content (everything from [00:00] onwards, including timestamps).

Return it as a single text string, preserving line breaks.

Here is the file:
[PASTE FULL VIDEO_001.MD CONTENT]
```

Then add the output to the `transcription` field.

---

## STEP 3: EXTRACT ENTITIES FROM TRANSCRIPTIONS

### Prompt for AI:

```
Analyze this video transcription and extract structured entities:

**Transcription:**
[PASTE TRANSCRIPTION TEXT]

**Extract:**

1. **Tools** - Any software, platforms, APIs mentioned
   Format: [{"name": "Glif", "category": "AI Platform", "id": "TOOL-###"}]

2. **Workflows** - Complete processes or automations described
   Format: [{"id": "WRF-###", "name": "Mr Beast Thumbnail Generator", "description": "Creates viral YouTube thumbnails using AI agents"}]

3. **Actions** - Verb phrases describing what users do
   Format: ["Create", "Upload", "Generate", "Configure", "Test", "Deploy"]

4. **Skills** - Capabilities or knowledge required
   Format: ["Prompt Engineering", "Image Generation", "Workflow Design"]

**Return as JSON:**

```json
{
  "tools": [...],
  "workflows": [...],
  "actions": [...],
  "skills": [...]
}
```

Only extract entities that are explicitly mentioned or demonstrated in the video. Don't invent entities.
```

---

## STEP 4: CREATE RESEARCH TOPICS

Group your videos by theme.

### Prompt:

```
Based on these video titles and topics:

[PASTE LIST OF VIDEO TITLES FROM VIDEOS_INDEX]

Create 3-5 research topic groups that organize these videos logically.

Format:

```javascript
[
  {
    "id": "TOPIC-001",
    "name": "AI Agents & Creative Workflows",
    "prompt": "Research videos covering AI agents, creative automation tools like Glif, and workflow optimization for content creators.",
    "status": "Complete",
    "assigned_to": "Research Team",
    "date_created": "2024-11-01",
    "date_completed": "2024-11-25",
    "videos_found": 8  // Count videos that fit this topic
  }
]
```

Group videos with similar themes together.
```

---

## STEP 5: GET YOUTUBE VIDEO IDs

For videos without YouTube IDs (most markdown files), you need to either:

### Option A: Extract from JSON files
- `Video_027.json` has: `"video_id": "yHPmIiXqH_U"`
- `Video_028.json` has: `"video_id": "9602Yzvd7ik"`

### Option B: Search YouTube
If you have the video title, search YouTube and extract the ID from the URL:
- URL: `https://www.youtube.com/watch?v=ABC123DEF45`
- Video ID: `ABC123DEF45`

### Option C: Leave Empty
For videos without IDs, the iframe won't work but the rest of the data is still useful.

---

## QUICK START: SIMPLIFIED IMPORT

If you want to get started quickly without all the entity extraction:

### 1. Use This Minimal Script:

```javascript
// PASTE INTO BROWSER CONSOLE

localStorage.clear();

// Create one topic
localStorage.setItem('topics', JSON.stringify([
  {
    "id": "TOPIC-001",
    "name": "AI Automation & Creative Tools",
    "prompt": "Research videos about AI agents, automation platforms, and creative AI workflows.",
    "status": "Complete",
    "assigned_to": "Research Team",
    "date_created": "2024-11-01",
    "date_completed": "2024-11-25",
    "videos_found": 24
  }
]));

// Add simplified videos (update with your actual data)
localStorage.setItem('videos', JSON.stringify([
  {
    "id": "VIDEO-001",
    "video_id": "",  // Add if you have it
    "title": "How To Use AI Agents to 10x Your Creative AI Game (GLIF TUTORIAL)",
    "channel": "Unknown",
    "duration": "13:00",
    "views": 0,
    "likes": 0,
    "published_date": "",
    "topic_id": "TOPIC-001",
    "status": "COMPLETE",
    "date_added": "2024-11-20",
    "date_completed": "2024-11-25",
    "total_days": 5,
    "stage_dates": {
      "queued": "2024-11-20",
      "selected": "2024-11-21",
      "transcribing": "2024-11-22",
      "analyzed": "2024-11-24",
      "integrated": "2024-11-25",
      "complete": "2024-11-25"
    },
    "transcription": "",  // Leave empty initially
    "extracted_entities": {
      "tools": [
        {"name": "Glif", "category": "AI Platform", "id": "TOOL-001"},
        {"name": "ChatGPT", "category": "AI Assistant", "id": "TOOL-002"}
      ],
      "workflows": [
        {"id": "WRF-001", "name": "YouTube Thumbnail Generator", "description": "AI agent workflow for creating viral thumbnails"}
      ],
      "actions": ["Create", "Generate", "Upload", "Configure"],
      "skills": ["Prompt Engineering", "AI Workflow Design"]
    },
    "topics_mentioned": ["AI agents", "GLIF", "creative workflows", "thumbnails", "TikTok automation"]
  },
  {
    "id": "VIDEO-002",
    "video_id": "",
    "title": "Building a Full Stack App",  // Replace with actual title
    "channel": "Unknown",
    "duration": "45:00",
    "topic_id": "TOPIC-001",
    "status": "COMPLETE",
    "date_added": "2024-11-21",
    "date_completed": "2024-11-26",
    "total_days": 5,
    "stage_dates": {
      "queued": "2024-11-21",
      "selected": "2024-11-22",
      "transcribing": "2024-11-23",
      "analyzed": "2024-11-25",
      "integrated": "2024-11-26",
      "complete": "2024-11-26"
    },
    "transcription": "",
    "extracted_entities": {
      "tools": [],
      "workflows": [],
      "actions": [],
      "skills": []
    },
    "topics_mentioned": []
  }
  // Add more videos...
]));

console.log('✅ Initial data loaded!');
console.log('📊 Topics: 1');
console.log('📹 Videos: 2 (update with all 24)');
console.log('');
console.log('Refresh the page to see your data.');
```

---

## RECOMMENDED WORKFLOW

### Phase 1: Get Basic Structure (30 minutes)
1. Run Step 1 prompt with VIDEOS_INDEX.md → Get all 24 video records
2. Run Step 4 prompt → Create 3-5 topic groups
3. Paste basic data into app → Verify it displays

### Phase 2: Add YouTube IDs (1-2 hours)
1. Check JSON files for existing video_ids
2. Search YouTube for titles → Extract IDs
3. Update video records with real YouTube IDs
4. Test iframe previews work

### Phase 3: Add Transcriptions (Optional)
1. For videos you want to analyze, copy transcription text
2. Add to `transcription` field
3. Now searchable in app

### Phase 4: Extract Entities (2-3 hours)
1. For important videos, run Step 3 prompt
2. Get structured tools, workflows, actions, skills
3. Add to `extracted_entities`
4. Browse catalog with rich data

---

## DATA QUALITY NOTES

**What's Real:**
✅ Video titles (from VIDEOS_INDEX)
✅ Durations (from VIDEOS_INDEX)
✅ Topics mentioned (from VIDEOS_INDEX)
✅ Full transcriptions with timestamps (in .md files)
✅ Tools and workflows (mentioned in transcriptions)

**What's Missing:**
❌ Channel names (mostly "Unknown" - need manual research)
❌ Publication dates (not captured)
❌ View counts, likes (not captured)
❌ Video IDs (need to search YouTube)

**Don't make up missing data.** Leave fields empty if you don't have the info. The app works fine with partial data.

---

## AUTOMATED IMPORT SCRIPT (Advanced)

If you want to automate this, create a Node.js script:

```javascript
// import-transcriptions.js
const fs = require('fs');
const path = require('path');

const transcriptionsDir = 'C:\\Users\\Dell\\Dropbox\\ENTITIES\\TASK_MANAGERS\\RESEARCHES\\02_TRANSCRIPTIONS';

// Read VIDEOS_INDEX.md
const indexContent = fs.readFileSync(
  path.join(transcriptionsDir, 'VIDEOS_INDEX.md'),
  'utf-8'
);

// Parse table rows
const videos = [];
const lines = indexContent.split('\n');

lines.forEach(line => {
  if (line.startsWith('| Video_')) {
    const parts = line.split('|').map(s => s.trim());

    const videoNum = parts[1].replace('Video_', '').padStart(3, '0');

    videos.push({
      id: `VIDEO-${videoNum}`,
      video_id: '',
      title: parts[2],
      channel: parts[3] === 'Unknown' ? 'Unknown' : parts[3],
      duration: parts[4],
      topics_mentioned: parts[6].split(',').map(s => s.trim()),
      status: 'COMPLETE',
      date_added: '2024-11-20',
      date_completed: '2024-11-25',
      total_days: 5,
      transcription: '',
      extracted_entities: {
        tools: [],
        workflows: [],
        actions: [],
        skills: []
      }
    });
  }
});

// Read transcription files
videos.forEach(video => {
  const mdFile = `Video_${video.id.replace('VIDEO-', '')}.md`;
  const mdPath = path.join(transcriptionsDir, mdFile);

  if (fs.existsSync(mdPath)) {
    const content = fs.readFileSync(mdPath, 'utf-8');

    // Extract transcription (everything from [00:00] onwards)
    const transcriptStart = content.indexOf('[00:00]');
    if (transcriptStart >= 0) {
      video.transcription = content.substring(transcriptStart);
    }
  }
});

// Output JSON
console.log(JSON.stringify(videos, null, 2));
```

Run: `node import-transcriptions.js > videos-data.json`

---

## SUCCESS CRITERIA

You've successfully imported real data when:

✅ All 24 videos from VIDEOS_INDEX appear in app
✅ Video titles match your transcription files
✅ Can view videos with YouTube IDs (iframes work)
✅ Can read full transcriptions for each video
✅ Topics group videos logically
✅ No fake/sample data - everything is real

---

## VISUAL FEATURE: QUEUE POSITION INDICATORS

Add red numbered dots to show where videos are in the processing queue.

### What This Shows:

For each status, display a red circle with the queue position number:
- QUEUED videos: Show position 1, 2, 3, etc.
- SELECTED videos: Show position 1, 2, 3, etc.
- TRANSCRIBING videos: Show position 1, 2, etc.

### Implementation:

```javascript
// Calculate queue positions
function addQueuePositions(videos) {
  const statusQueues = {
    'QUEUED': [],
    'SELECTED': [],
    'TRANSCRIBING': [],
    'ANALYZED': [],
    'INTEGRATED': []
  };

  // Group by status
  videos.forEach(video => {
    if (statusQueues[video.status]) {
      statusQueues[video.status].push(video);
    }
  });

  // Sort each queue by date_added (oldest first)
  Object.keys(statusQueues).forEach(status => {
    statusQueues[status].sort((a, b) =>
      new Date(a.date_added) - new Date(b.date_added)
    );

    // Add position number
    statusQueues[status].forEach((video, index) => {
      video.queue_position = index + 1;
    });
  });

  return videos;
}

// Call before displaying videos
videos = addQueuePositions(videos);
```

### Display Queue Number Badge:

```html
<!-- In video card -->
<div class="video-card">
  <div class="card-header">
    <h3>Video Title</h3>

    <!-- Queue Position Badge (only for non-complete videos) -->
    {video.status !== 'COMPLETE' && (
      <div class="queue-badge">
        <span class="queue-number">{video.queue_position}</span>
      </div>
    )}
  </div>

  <!-- Rest of card -->
</div>
```

### CSS Styling:

```css
/* Queue Position Badge */
.queue-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  background: #EF4444;  /* Red */
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(239, 68, 68, 0.4);
  z-index: 10;
}

.queue-number {
  color: white;
  font-size: 14px;
  font-weight: 700;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* Pulse animation for position 1 (next in queue) */
.queue-badge.next-in-queue {
  animation: pulse-red 2s infinite;
}

@keyframes pulse-red {
  0%, 100% {
    box-shadow: 0 2px 8px rgba(239, 68, 68, 0.4);
  }
  50% {
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.8);
    transform: scale(1.1);
  }
}
```

### Enhanced Video Card with Queue Number:

```html
<div class="video-card" style="position: relative;">
  <!-- Queue Position Badge -->
  <div class="queue-badge ${video.queue_position === 1 ? 'next-in-queue' : ''}">
    <span class="queue-number">${video.queue_position}</span>
  </div>

  <!-- YouTube Iframe -->
  <div class="video-embed">
    <iframe src="https://www.youtube.com/embed/${video.video_id}"></iframe>
  </div>

  <!-- Card Content -->
  <div class="card-body">
    <h3>${video.title}</h3>
    <div class="flex items-center justify-between">
      <span class="status-badge">${video.status}</span>
      <span class="text-sm text-gray-500">${video.duration}</span>
    </div>
  </div>
</div>
```

### Queue Stats Display:

Show total count for each queue:

```html
<div class="queue-stats">
  <div class="stat-item">
    <span class="stat-label">Queued</span>
    <div class="flex items-center gap-2">
      <div class="queue-badge-small">
        <span>5</span>
      </div>
      <span class="text-sm text-gray-600">videos waiting</span>
    </div>
  </div>

  <div class="stat-item">
    <span class="stat-label">Selected</span>
    <div class="flex items-center gap-2">
      <div class="queue-badge-small">
        <span>3</span>
      </div>
      <span class="text-sm text-gray-600">ready to transcribe</span>
    </div>
  </div>

  <div class="stat-item">
    <span class="stat-label">Transcribing</span>
    <div class="flex items-center gap-2">
      <div class="queue-badge-small">
        <span>2</span>
      </div>
      <span class="text-sm text-gray-600">in progress</span>
    </div>
  </div>
</div>
```

```css
.queue-badge-small {
  width: 24px;
  height: 24px;
  background: #EF4444;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 12px;
  font-weight: 700;
}
```

### Visual Example:

```
┌────────────────────────────────────┐
│  ⭕1  [YouTube Video Preview]       │  ← First in queue (pulsing)
│                                    │
│  "Build AI Agent with n8n"         │
│  Status: QUEUED | 11:30            │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  ⭕2  [YouTube Video Preview]       │  ← Second in queue
│                                    │
│  "Complete Guide to Make.com"      │
│  Status: QUEUED | 15:45            │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  ⭕1  [YouTube Video Preview]       │  ← First in SELECTED queue
│                                    │
│  "Automate Everything with n8n"    │
│  Status: SELECTED | 22:10          │
└────────────────────────────────────┘
```

### Update Sample Data:

```javascript
// When loading videos, add queue positions
let videos = JSON.parse(localStorage.getItem('videos') || '[]');
videos = addQueuePositions(videos);

// Save back with positions
localStorage.setItem('videos', JSON.stringify(videos));
```

---

## WHAT TO DO NEXT

Once real data is imported:

1. **Test all screens** - Verify data displays correctly
2. **Add missing YouTube IDs** - Search YouTube for videos without IDs
3. **Extract entities** - Run entity extraction on key videos
4. **Verify transcriptions** - Check formatting and readability
5. **Check queue positions** - Red numbered dots show correctly
6. **Use the app** - Browse, search, analyze your real research data

Your app now becomes a **real video research library** with actual transcriptions, analysis, and visual queue indicators.
