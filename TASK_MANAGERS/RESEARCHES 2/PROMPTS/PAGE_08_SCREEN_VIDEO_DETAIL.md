# PAGE 8: SCREEN 8 - Video Detail Page (Final View)

**Complete details for one processed video**

---

## WHAT THIS SCREEN DOES

Show EVERYTHING about one completed video:
- Full YouTube player embed
- All metadata
- Complete list of extracted entities (tools, workflows, actions, skills)
- Full transcription (expandable)
- Processing timeline
- Export options

---

## VISUAL LAYOUT

```
┌────────────────────────────────────────────────────────┐
│  ← Back to Library                                     │
│                                                        │
│  VIDEO-027: "Build AI Agent with n8n and OpenAI"      │
│  ══════════════════════════════════════════════════    │
│                                                        │
│  [Full YouTube Embedded Player - Large]                │
│  ▶ Watch full video                                    │
│                                                        │
│  ──────────────────────────────────────────────────    │
│                                                        │
│  METADATA                                              │
│  • Channel: AI Tutorials                              │
│  • Published: November 15, 2024                       │
│  • Duration: 11:30                                    │
│  • Views: 125,000 | Likes: 3,200                      │
│  • Topic: AI Automation Tools 2024                    │
│  • Processed: December 7, 2025 (6 days)               │
│                                                        │
│  ──────────────────────────────────────────────────    │
│                                                        │
│  EXTRACTED ENTITIES                                    │
│                                                        │
│  🔧 TOOLS (12)                                        │
│  • n8n - Workflow Automation                          │
│  • OpenAI API - AI Platform                           │
│  • Google Sheets - Spreadsheet                        │
│  • Gmail - Email                                      │
│  ... [show all]                                       │
│                                                        │
│  ⚙️ WORKFLOWS (3)                                     │
│  • WRF-045: n8n + OpenAI Automation                   │
│  • WRF-046: Google Sheets Integration                 │
│  • WRF-047: Email Notification System                 │
│                                                        │
│  ✏️ ACTIONS (12)                                      │
│  • Create, Configure, Connect, Test, Deploy...        │
│                                                        │
│  🎓 SKILLS (5)                                        │
│  • API Integration                                    │
│  • Workflow Design                                    │
│  • Prompt Engineering                                 │
│  ...                                                  │
│                                                        │
│  ──────────────────────────────────────────────────    │
│                                                        │
│  TRANSCRIPTION ▼ Click to expand                       │
│  [Full transcription text with timestamps]            │
│                                                        │
│  ──────────────────────────────────────────────────    │
│                                                        │
│  PROCESSING TIMELINE                                   │
│  ✅ Queued: 2025-12-01                                │
│  ✅ Selected: 2025-12-02                              │
│  ✅ Transcribed: 2025-12-03                           │
│  ✅ Analyzed: 2025-12-04                              │
│  ✅ Integrated: 2025-12-05                            │
│  ✅ Complete: 2025-12-07                              │
│  Total: 6 days                                        │
│                                                        │
│  ──────────────────────────────────────────────────    │
│                                                        │
│  [Download as JSON] [Edit Entities] [Delete Video]    │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## DATA STRUCTURE

### Complete Video Object:

```
Video (Complete):
  - ID: "VIDEO-027"
  - video_id: "ABC123..."
  - youtube_url: "https://..."
  - title: "Build AI Agent..."
  - channel: "AI Tutorials"
  - duration: "11:30"
  - views: 125000
  - likes: 3200
  - comments: 150
  - published_date: "2024-11-15"
  - topic_id: "TOPIC-001"

  - status: "COMPLETE"
  - date_added: "2025-12-01"
  - date_completed: "2025-12-07"
  - total_days: 6

  - stage_dates: {
      queued: "2025-12-01",
      selected: "2025-12-02",
      transcribing: "2025-12-03",
      analyzed: "2025-12-04",
      integrated: "2025-12-05",
      complete: "2025-12-07"
    }

  - transcription: "Full text..."

  - extracted_entities: {
      tools: [
        {name: "n8n", category: "Workflow Automation", id: "TOOL-AI-042"},
        {name: "OpenAI API", category: "AI Platform", id: "TOOL-AI-003"},
        ...
      ],
      workflows: [
        {id: "WRF-045", name: "n8n + OpenAI Automation", description: "..."},
        ...
      ],
      actions: ["Create", "Configure", "Connect", "Test", "Deploy", ...],
      skills: ["API Integration", "Workflow Design", ...]
    }

  - notes: "User notes..."
```

---

## HTML STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video Details</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="detail-container">
  <!-- Header -->
  <a href="video-library.html" class="back-link">← Back to Library</a>

  <h1 id="videoTitle"></h1>

  <!-- YouTube Player -->
  <div class="video-player-large">
    <iframe id="youtubePlayer" frameborder="0" allowfullscreen></iframe>
  </div>

  <!-- Metadata Section -->
  <section class="metadata-section">
    <h2>Metadata</h2>
    <div class="metadata-grid" id="metadata">
      <!-- Metadata loaded here -->
    </div>
  </section>

  <!-- Extracted Entities Section -->
  <section class="entities-section">
    <h2>Extracted Entities</h2>

    <div class="entity-category">
      <h3>🔧 Tools (<span id="toolsCount"></span>)</h3>
      <div id="toolsList" class="entity-list"></div>
    </div>

    <div class="entity-category">
      <h3>⚙️ Workflows (<span id="workflowsCount"></span>)</h3>
      <div id="workflowsList" class="entity-list"></div>
    </div>

    <div class="entity-category">
      <h3>✏️ Actions (<span id="actionsCount"></span>)</h3>
      <div id="actionsList" class="entity-list"></div>
    </div>

    <div class="entity-category">
      <h3>🎓 Skills (<span id="skillsCount"></span>)</h3>
      <div id="skillsList" class="entity-list"></div>
    </div>
  </section>

  <!-- Transcription Section -->
  <section class="transcription-section">
    <h2 onclick="toggleTranscription()" style="cursor: pointer;">
      Transcription <span id="transcriptionToggle">▼</span>
    </h2>
    <div id="transcriptionContent" class="transcription-content" style="display: none;">
      <!-- Transcription loaded here -->
    </div>
  </section>

  <!-- Timeline Section -->
  <section class="timeline-section">
    <h2>Processing Timeline</h2>
    <div id="timeline" class="timeline">
      <!-- Timeline loaded here -->
    </div>
    <p class="total-time">Total processing time: <strong id="totalDays"></strong></p>
  </section>

  <!-- Actions -->
  <section class="actions-section">
    <button onclick="downloadJSON()" class="btn-action">📥 Download as JSON</button>
    <button onclick="editVideo()" class="btn-action">✏️ Edit Entities</button>
    <button onclick="deleteVideo()" class="btn-danger">🗑️ Delete Video</button>
  </section>

</div>

<script src="video-detail.js"></script>
</body>
</html>
```

---

## CSS STYLING

```css
.detail-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.back-link {
  color: #2196f3;
  text-decoration: none;
  margin-bottom: 20px;
  display: inline-block;
}

h1 {
  margin: 20px 0;
  font-size: 28px;
}

/* Video Player */
.video-player-large {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  margin: 20px 0;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
}

.video-player-large iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Sections */
section {
  background: white;
  padding: 30px;
  margin: 20px 0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

section h2 {
  margin: 0 0 20px 0;
  padding-bottom: 10px;
  border-bottom: 2px solid #f5f5f5;
}

/* Metadata */
.metadata-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.metadata-item {
  padding: 12px;
  background: #f9f9f9;
  border-radius: 8px;
}

.metadata-label {
  font-size: 12px;
  color: #666;
  font-weight: bold;
  margin-bottom: 5px;
}

.metadata-value {
  font-size: 16px;
  color: #333;
}

/* Entities */
.entity-category {
  margin: 25px 0;
}

.entity-category h3 {
  margin: 0 0 15px 0;
  font-size: 18px;
}

.entity-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.entity-tag {
  background: #e3f2fd;
  color: #1976d2;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
}

.entity-item {
  background: #f5f5f5;
  padding: 15px;
  border-radius: 8px;
  margin: 10px 0;
  border-left: 4px solid #2196f3;
}

.entity-item h4 {
  margin: 0 0 8px 0;
  color: #333;
}

.entity-item p {
  margin: 0;
  color: #666;
  font-size: 14px;
}

/* Transcription */
.transcription-content {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  white-space: pre-wrap;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.8;
  max-height: 500px;
  overflow-y: auto;
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 40px;
}

.timeline-item {
  position: relative;
  padding: 15px 0;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -32px;
  top: 20px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #4caf50;
  border: 3px solid white;
  box-shadow: 0 0 0 2px #4caf50;
}

.timeline-item::after {
  content: '';
  position: absolute;
  left: -25px;
  top: 36px;
  width: 2px;
  height: calc(100% - 16px);
  background: #ddd;
}

.timeline-item:last-child::after {
  display: none;
}

.timeline-stage {
  font-weight: bold;
  color: #333;
  margin-bottom: 4px;
}

.timeline-date {
  color: #666;
  font-size: 14px;
}

.total-time {
  margin-top: 20px;
  font-size: 16px;
  color: #666;
}

/* Actions */
.actions-section {
  display: flex;
  gap: 15px;
  justify-content: center;
}

.btn-action {
  padding: 12px 24px;
  background: #2196f3;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.btn-action:hover {
  background: #1976d2;
}

.btn-danger {
  padding: 12px 24px;
  background: #f44336;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
}

.btn-danger:hover {
  background: #d32f2f;
}
```

---

## JAVASCRIPT

```javascript
let currentVideo = null;

// Load video details
window.onload = function() {
  const videoId = localStorage.getItem('selectedVideo');

  if (!videoId) {
    alert('No video selected');
    window.location.href = 'video-library.html';
    return;
  }

  loadVideo(videoId);
};

function loadVideo(videoId) {
  const allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  currentVideo = allVideos.find(v => v.id === videoId);

  if (!currentVideo) {
    alert('Video not found');
    return;
  }

  // Display all sections
  displayTitle();
  displayPlayer();
  displayMetadata();
  displayEntities();
  displayTranscription();
  displayTimeline();
}

function displayTitle() {
  document.getElementById('videoTitle').textContent =
    `${currentVideo.id}: ${currentVideo.title || 'Untitled Video'}`;
}

function displayPlayer() {
  const embedUrl = `https://www.youtube.com/embed/${currentVideo.video_id}`;
  document.getElementById('youtubePlayer').src = embedUrl;
}

function displayMetadata() {
  const topics = JSON.parse(localStorage.getItem('topics') || '[]');
  const topic = topics.find(t => t.id === currentVideo.topic_id);

  const container = document.getElementById('metadata');
  container.innerHTML = `
    <div class="metadata-item">
      <div class="metadata-label">Channel</div>
      <div class="metadata-value">📺 ${currentVideo.channel || 'Unknown'}</div>
    </div>

    <div class="metadata-item">
      <div class="metadata-label">Published</div>
      <div class="metadata-value">📅 ${currentVideo.published_date || 'Unknown'}</div>
    </div>

    <div class="metadata-item">
      <div class="metadata-label">Duration</div>
      <div class="metadata-value">⏱️ ${currentVideo.duration || 'Unknown'}</div>
    </div>

    <div class="metadata-item">
      <div class="metadata-label">Views & Likes</div>
      <div class="metadata-value">👁️ ${formatNumber(currentVideo.views)} | ❤️ ${formatNumber(currentVideo.likes)}</div>
    </div>

    <div class="metadata-item">
      <div class="metadata-label">Topic</div>
      <div class="metadata-value">📂 ${topic ? topic.name : 'Unknown'}</div>
    </div>

    <div class="metadata-item">
      <div class="metadata-label">Processed</div>
      <div class="metadata-value">✅ ${currentVideo.date_completed} (${currentVideo.total_days} days)</div>
    </div>
  `;
}

function displayEntities() {
  const entities = currentVideo.extracted_entities || {};

  // Tools
  displayEntityList('tools', entities.tools || []);
  document.getElementById('toolsCount').textContent = (entities.tools || []).length;

  // Workflows
  displayWorkflows(entities.workflows || []);
  document.getElementById('workflowsCount').textContent = (entities.workflows || []).length;

  // Actions
  displaySimpleList('actions', entities.actions || []);
  document.getElementById('actionsCount').textContent = (entities.actions || []).length;

  // Skills
  displaySimpleList('skills', entities.skills || []);
  document.getElementById('skillsCount').textContent = (entities.skills || []).length;
}

function displayEntityList(type, items) {
  const container = document.getElementById(`${type}List`);
  container.innerHTML = '';

  if (items.length === 0) {
    container.innerHTML = '<p style="color: #999;">None found</p>';
    return;
  }

  items.forEach(item => {
    const div = document.createElement('div');
    div.className = 'entity-item';
    div.innerHTML = `
      <h4>${item.name}</h4>
      ${item.category ? `<p>${item.category}</p>` : ''}
      ${item.id ? `<p style="font-size: 12px; color: #999;">ID: ${item.id}</p>` : ''}
    `;
    container.appendChild(div);
  });
}

function displayWorkflows(workflows) {
  const container = document.getElementById('workflowsList');
  container.innerHTML = '';

  if (workflows.length === 0) {
    container.innerHTML = '<p style="color: #999;">None found</p>';
    return;
  }

  workflows.forEach(wf => {
    const div = document.createElement('div');
    div.className = 'entity-item';
    div.innerHTML = `
      <h4>${wf.id}: ${wf.name}</h4>
      ${wf.description ? `<p>${wf.description}</p>` : ''}
    `;
    container.appendChild(div);
  });
}

function displaySimpleList(type, items) {
  const container = document.getElementById(`${type}List`);
  container.innerHTML = '';

  if (items.length === 0) {
    container.innerHTML = '<p style="color: #999;">None found</p>';
    return;
  }

  items.forEach(item => {
    const tag = document.createElement('span');
    tag.className = 'entity-tag';
    tag.textContent = item;
    container.appendChild(tag);
  });
}

function displayTranscription() {
  const container = document.getElementById('transcriptionContent');
  container.textContent = currentVideo.transcription || 'No transcription available';
}

function toggleTranscription() {
  const content = document.getElementById('transcriptionContent');
  const toggle = document.getElementById('transcriptionToggle');

  if (content.style.display === 'none') {
    content.style.display = 'block';
    toggle.textContent = '▲';
  } else {
    content.style.display = 'none';
    toggle.textContent = '▼';
  }
}

function displayTimeline() {
  const container = document.getElementById('timeline');
  const stages = [
    { key: 'queued', label: 'Queued' },
    { key: 'selected', label: 'Selected' },
    { key: 'transcribing', label: 'Transcribed' },
    { key: 'analyzed', label: 'Analyzed' },
    { key: 'integrated', label: 'Integrated' },
    { key: 'complete', label: 'Complete' }
  ];

  container.innerHTML = '';

  stages.forEach(stage => {
    const date = currentVideo.stage_dates?.[stage.key];

    if (date) {
      const item = document.createElement('div');
      item.className = 'timeline-item';
      item.innerHTML = `
        <div class="timeline-stage">✅ ${stage.label}</div>
        <div class="timeline-date">${date}</div>
      `;
      container.appendChild(item);
    }
  });

  document.getElementById('totalDays').textContent =
    `${currentVideo.total_days || 0} days`;
}

function formatNumber(num) {
  if (!num) return '0';
  if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
  if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
  return num.toString();
}

// Actions
function downloadJSON() {
  const dataStr = JSON.stringify(currentVideo, null, 2);
  const blob = new Blob([dataStr], {type: 'application/json'});
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = `${currentVideo.id}.json`;
  a.click();

  URL.revokeObjectURL(url);
}

function editVideo() {
  alert('Edit functionality would go here');
  // Navigate to edit page or show modal
}

function deleteVideo() {
  if (!confirm('Are you sure you want to delete this video? This cannot be undone.')) {
    return;
  }

  const allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  const filtered = allVideos.filter(v => v.id !== currentVideo.id);

  localStorage.setItem('videos', JSON.stringify(filtered));

  alert('Video deleted');
  window.location.href = 'video-library.html';
}
```

---

## SUCCESS CRITERIA

You've completed Screen 8 when:

✅ Displays full video with large player
✅ Shows all metadata fields
✅ Lists all extracted entities (tools, workflows, actions, skills)
✅ Shows expandable transcription
✅ Displays processing timeline with dates
✅ Calculates total processing time
✅ Can download video data as JSON
✅ Can delete video
✅ Proper formatting and styling
✅ All data displayed accurately

---

## COMPLETE SYSTEM SUMMARY

You've now built all 8 screens:

1. ✅ **Research Topics** - Manage research tasks
2. ✅ **Research Prompt** - Execute research and submit URLs
3. ✅ **Transcription Queue** - Select videos with YouTube previews
4. ✅ **Processing View** - Move videos through stages
5. ✅ **Video Library** - Browse all completed videos
6. ✅ **Channel Catalog** - Browse by YouTube channels
7. ✅ **Video Detail** - View complete video information

**Your system is complete!**

The user can now:
- Create research topics
- Find videos
- Queue them for processing
- Watch previews
- Process through stages
- Browse final catalog
- View complete details

All with YouTube integration, no complex logging, and localStorage for simplicity.
