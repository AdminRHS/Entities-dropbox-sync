# PAGE 4: SCREEN 4 - Transcription Queue with YouTube Previews

**Show videos with embedded YouTube previews for selection**

---

## WHAT THIS SCREEN DOES

Display all queued videos with YouTube iframe embeds so user can:
- Preview videos before selecting for transcription
- Select videos to process
- See video metadata (title, duration, views)

---

## VISUAL LAYOUT

```
┌────────────────────────────────────────────────────────────┐
│  Transcription Queue                     [Filter: All ▼]   │
│  ══════════════════════                                    │
│                                                            │
│  15 videos ready for transcription                         │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │                                                      │ │
│  │  [YouTube Preview - Embedded iframe 16:9]           │ │
│  │  ▶ Play video inline                                │ │
│  │                                                      │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │ VIDEO-027: "Build AI Agent with n8n and OpenAI"     │ │
│  │                                                      │ │
│  │ Channel: AI Tutorials                               │ │
│  │ Duration: 11:30 | Views: 125K | Published: Nov 2024 │ │
│  │ Topic: AI Automation Tools 2024                     │ │
│  │                                                      │ │
│  │ [☐ Select] [▶ Watch Full] [View Details]           │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ [YouTube Preview - iframe]                           │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │ VIDEO-028: "Automate Everything with Make.com"      │ │
│  │ Channel: Tech Guide                                  │ │
│  │ Duration: 15:45 | Views: 89K                        │ │
│  │ [☐ Select] [▶ Watch Full] [View Details]           │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  [Show More]                                               │
│                                                            │
│  ── Selected: 3 videos ──────────────────────────────────  │
│  [Process Selected Videos →]                               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## DATA STRUCTURE

### Video Entry:

```
Video:
  - ID: "VIDEO-027"
  - Video ID: "ABC123DEF45" (YouTube 11-char ID)
  - YouTube URL: "https://youtube.com/watch?v=ABC123DEF45"
  - Title: "Build AI Agent with n8n and OpenAI" (optional - can fetch)
  - Channel: "AI Tutorials" (optional)
  - Duration: "11:30" (optional)
  - Views: 125000 (optional)
  - Published Date: "2024-11-15" (optional)
  - Topic ID: "TOPIC-001"
  - Status: "QUEUED"
  - Selected: false (for checkbox)
  - Date Added: "2025-12-05"
  - Thumbnail URL: auto-generated from video ID
```

### Auto-Generated URLs:

```javascript
// YouTube embed URL (for iframe)
embedUrl = `https://www.youtube.com/embed/${videoId}`

// YouTube thumbnail URL
thumbnailUrl = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`
// or medium quality:
thumbnailUrl = `https://img.youtube.com/vi/${videoId}/mqdefault.jpg`

// Full watch URL
watchUrl = `https://www.youtube.com/watch?v=${videoId}`
```

---

## YOUTUBE IFRAME EMBED

### Basic Embed Code:

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID_HERE"
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>
```

### Responsive Embed (16:9 ratio):

```html
<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/VIDEO_ID_HERE"
    frameborder="0"
    allowfullscreen>
  </iframe>
</div>
```

```css
.video-embed {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 ratio */
  height: 0;
  overflow: hidden;
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

---

## USER INTERACTIONS

### 1. View Queue
Load all videos with status "QUEUED", display with previews

### 2. Select Videos
Click checkboxes to select videos for processing

```
User checks VIDEO-027
→ Mark as selected
→ Update counter "Selected: 1 video"

User checks VIDEO-028
→ Mark as selected
→ Update counter "Selected: 2 videos"
```

### 3. Watch Full Video
Click "Watch Full" button or click iframe to watch inline

### 4. Process Selected
Click "Process Selected Videos" button
```
→ Get all videos where selected = true
→ Navigate to processing screen for first video
→ Change status from QUEUED to SELECTED
```

### 5. Filter Videos
Filter by topic, date added, etc.

---

## HTML STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transcription Queue</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="queue-container">
  <!-- Header -->
  <header>
    <h1>Transcription Queue</h1>
    <div class="filters">
      <select id="topicFilter" onchange="filterVideos()">
        <option value="">All Topics</option>
        <!-- Topics loaded dynamically -->
      </select>
    </div>
  </header>

  <!-- Video Count -->
  <p class="video-count" id="videoCount">Loading...</p>

  <!-- Video List -->
  <div id="videoList">
    <!-- Videos rendered here dynamically -->
  </div>

  <!-- Load More -->
  <button id="loadMore" onclick="loadMore()" style="display: none;">
    Show More
  </button>

  <!-- Selection Actions -->
  <div class="selection-footer" id="selectionFooter" style="display: none;">
    <p>Selected: <span id="selectedCount">0</span> videos</p>
    <button onclick="processSelected()" class="btn-process">
      Process Selected Videos →
    </button>
  </div>
</div>

<script src="queue.js"></script>
</body>
</html>
```

---

## CSS STYLING

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #f5f5f5;
  padding: 20px;
}

.queue-container {
  max-width: 900px;
  margin: 0 auto;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.filters select {
  padding: 8px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
}

.video-count {
  color: #666;
  margin-bottom: 20px;
}

/* Video Card */
.video-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.2s;
}

.video-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* YouTube Embed */
.video-embed {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 */
  height: 0;
  overflow: hidden;
  background: #000;
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}

/* Video Info */
.video-info {
  padding: 20px;
}

.video-info h3 {
  margin: 0 0 10px 0;
  font-size: 18px;
  color: #333;
}

.video-metadata {
  color: #666;
  font-size: 14px;
  margin: 8px 0;
}

.video-metadata span {
  margin-right: 15px;
}

.video-topic {
  display: inline-block;
  background: #e3f2fd;
  color: #1976d2;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  margin-top: 8px;
}

/* Actions */
.video-actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
  align-items: center;
}

.video-actions input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.video-actions label {
  cursor: pointer;
  margin-left: 5px;
  user-select: none;
}

.video-actions button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.video-actions button:hover {
  background: #f5f5f5;
  border-color: #999;
}

/* Selection Footer */
.selection-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #333;
  color: white;
  padding: 20px;
  text-align: center;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
}

.selection-footer p {
  margin: 0 0 10px 0;
}

.btn-process {
  background: #4caf50;
  color: white;
  border: none;
  padding: 12px 30px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-process:hover {
  background: #45a049;
}

/* Load More */
#loadMore {
  width: 100%;
  padding: 15px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  margin: 20px 0;
}

#loadMore:hover {
  background: #f5f5f5;
}
```

---

## JAVASCRIPT

```javascript
let videos = [];
let topics = [];
let selectedVideos = [];
let displayCount = 5; // Show 5 at a time

// Load data
window.onload = function() {
  loadData();
  displayVideos();
};

function loadData() {
  // Load videos from localStorage
  videos = JSON.parse(localStorage.getItem('videos') || '[]');
  topics = JSON.parse(localStorage.getItem('topics') || '[]');

  // Filter only QUEUED videos
  videos = videos.filter(v => v.status === 'QUEUED');

  // Update count
  document.getElementById('videoCount').textContent =
    `${videos.length} videos ready for transcription`;

  // Load topics into filter
  const topicFilter = document.getElementById('topicFilter');
  topics.forEach(topic => {
    const option = document.createElement('option');
    option.value = topic.id;
    option.textContent = topic.name;
    topicFilter.appendChild(option);
  });
}

function displayVideos() {
  const container = document.getElementById('videoList');
  container.innerHTML = '';

  // Show first N videos
  const videosToShow = videos.slice(0, displayCount);

  videosToShow.forEach(video => {
    const card = createVideoCard(video);
    container.appendChild(card);
  });

  // Show/hide "Load More" button
  const loadMoreBtn = document.getElementById('loadMore');
  if (videos.length > displayCount) {
    loadMoreBtn.style.display = 'block';
  } else {
    loadMoreBtn.style.display = 'none';
  }
}

function createVideoCard(video) {
  const card = document.createElement('div');
  card.className = 'video-card';

  // Get topic name
  const topic = topics.find(t => t.id === video.topic_id);
  const topicName = topic ? topic.name : 'Unknown Topic';

  // Build embed URL
  const embedUrl = `https://www.youtube.com/embed/${video.video_id}`;

  card.innerHTML = `
    <div class="video-embed">
      <iframe
        src="${embedUrl}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>

    <div class="video-info">
      <h3>${video.id}: ${video.title || 'YouTube Video'}</h3>

      <div class="video-metadata">
        ${video.channel ? `<span>📺 ${video.channel}</span>` : ''}
        ${video.duration ? `<span>⏱️ ${video.duration}</span>` : ''}
        ${video.views ? `<span>👁️ ${formatViews(video.views)}</span>` : ''}
        ${video.published_date ? `<span>📅 ${video.published_date}</span>` : ''}
      </div>

      <span class="video-topic">${topicName}</span>

      <div class="video-actions">
        <input
          type="checkbox"
          id="select-${video.id}"
          onchange="toggleSelection('${video.id}')"
          ${video.selected ? 'checked' : ''}
        >
        <label for="select-${video.id}">Select</label>

        <button onclick="watchFull('${video.video_id}')">▶ Watch Full</button>
        <button onclick="viewDetails('${video.id}')">View Details</button>
      </div>
    </div>
  `;

  return card;
}

function toggleSelection(videoId) {
  const video = videos.find(v => v.id === videoId);
  if (video) {
    video.selected = !video.selected;

    // Update selected list
    if (video.selected) {
      selectedVideos.push(videoId);
    } else {
      selectedVideos = selectedVideos.filter(id => id !== videoId);
    }

    // Update UI
    updateSelectionFooter();

    // Save
    saveVideos();
  }
}

function updateSelectionFooter() {
  const footer = document.getElementById('selectionFooter');
  const count = document.getElementById('selectedCount');

  if (selectedVideos.length > 0) {
    footer.style.display = 'block';
    count.textContent = selectedVideos.length;
  } else {
    footer.style.display = 'none';
  }
}

function processSelected() {
  if (selectedVideos.length === 0) {
    alert('Please select at least one video');
    return;
  }

  // Update status to SELECTED
  videos.forEach(video => {
    if (video.selected) {
      video.status = 'SELECTED';
    }
  });

  // Save
  saveVideos();

  // Navigate to processing screen for first video
  const firstVideo = selectedVideos[0];
  localStorage.setItem('currentVideo', firstVideo);
  window.location.href = 'processing.html';
}

function watchFull(videoId) {
  // Open in new tab
  window.open(`https://www.youtube.com/watch?v=${videoId}`, '_blank');
}

function viewDetails(videoId) {
  localStorage.setItem('selectedVideo', videoId);
  window.location.href = 'video-detail.html';
}

function loadMore() {
  displayCount += 5;
  displayVideos();
}

function filterVideos() {
  const topicId = document.getElementById('topicFilter').value;

  if (topicId) {
    videos = videos.filter(v => v.topic_id === topicId);
  } else {
    // Reload all
    loadData();
  }

  displayCount = 5;
  displayVideos();
}

function formatViews(views) {
  if (views >= 1000000) {
    return (views / 1000000).toFixed(1) + 'M';
  } else if (views >= 1000) {
    return (views / 1000).toFixed(1) + 'K';
  }
  return views;
}

function saveVideos() {
  // Get all videos (not just queued)
  const allVideos = JSON.parse(localStorage.getItem('videos') || '[]');

  // Update only the ones we modified
  videos.forEach(v => {
    const index = allVideos.findIndex(av => av.id === v.id);
    if (index >= 0) {
      allVideos[index] = v;
    }
  });

  localStorage.setItem('videos', JSON.stringify(allVideos));
}
```

---

## OPTIONAL: FETCH VIDEO METADATA

If you want to automatically fetch title, duration, views from YouTube:

### Option 1: YouTube Data API (Requires API Key)

```javascript
async function fetchVideoMetadata(videoId) {
  const API_KEY = 'YOUR_YOUTUBE_API_KEY';
  const url = `https://www.googleapis.com/youtube/v3/videos?id=${videoId}&key=${API_KEY}&part=snippet,contentDetails,statistics`;

  const response = await fetch(url);
  const data = await response.json();

  if (data.items && data.items.length > 0) {
    const video = data.items[0];

    return {
      title: video.snippet.title,
      channel: video.snippet.channelTitle,
      published_date: video.snippet.publishedAt.split('T')[0],
      duration: parseDuration(video.contentDetails.duration),
      views: parseInt(video.statistics.viewCount),
      thumbnail: video.snippet.thumbnails.maxres?.url || video.snippet.thumbnails.high.url
    };
  }

  return null;
}

function parseDuration(duration) {
  // Convert PT11M30S to 11:30
  const match = duration.match(/PT(\d+H)?(\d+M)?(\d+S)?/);

  const hours = (match[1] || '').replace('H', '');
  const minutes = (match[2] || '0M').replace('M', '');
  const seconds = (match[3] || '0S').replace('S', '');

  if (hours) {
    return `${hours}:${minutes.padStart(2, '0')}:${seconds.padStart(2, '0')}`;
  }
  return `${minutes}:${seconds.padStart(2, '0')}`;
}
```

### Option 2: Manual Entry (Simpler)

User provides title/metadata when adding videos, or leave blank and just show video ID.

---

## SUCCESS CRITERIA

You've completed Screen 4 when:

✅ Displays list of QUEUED videos
✅ Shows YouTube iframe embed for each video
✅ Can play videos inline (in iframe)
✅ Can select videos with checkboxes
✅ Shows selection count in footer
✅ Can process selected videos
✅ Updates video status from QUEUED → SELECTED
✅ Navigates to processing screen
✅ Can filter by topic
✅ Can load more videos (pagination)

---

## NEXT STEP

**Go to Page 5: Screen 5 - Processing Detail View**

Build the screen for processing a single video through all stages.
