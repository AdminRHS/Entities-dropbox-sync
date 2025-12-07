# PAGE 6: SCREEN 6 - Video Library Catalog

**Browse all completed videos with thumbnails and filters**

---

## WHAT THIS SCREEN DOES

Display final catalog of all COMPLETE videos:
- Grid/list view with YouTube thumbnails
- Filter by topic, channel, tools
- Search by title/keywords
- Click to view full details

---

## VISUAL LAYOUT

```
┌────────────────────────────────────────────────────────────┐
│  Video Library                                    🔍 Search │
│  ═════════════                                             │
│                                                            │
│  28 videos | Filters: [All Topics ▼] [All Channels ▼]     │
│  Sort by: [Date Added ▼]  View: [Grid] [List]            │
│                                                            │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────┐│
│  │[YouTube Thumb]  │ │[YouTube Thumb]  │ │[YouTube Thum]││
│  │                 │ │                 │ │              ││
│  │ VIDEO-027       │ │ VIDEO-028       │ │ VIDEO-029    ││
│  │ "Build AI       │ │ "Automate       │ │ "n8n for     ││
│  │  Agent..."      │ │  Everything..." │ │  Beginners"  ││
│  │                 │ │                 │ │              ││
│  │ AI Tutorials    │ │ Tech Guide      │ │ Workflow Pro ││
│  │ 11:30 | 125K    │ │ 15:45 | 89K     │ │ 8:20 | 45K   ││
│  │                 │ │                 │ │              ││
│  │ Tools: 4        │ │ Tools: 6        │ │ Tools: 3     ││
│  │ Workflows: 3    │ │ Workflows: 2    │ │ Workflows: 5 ││
│  │                 │ │                 │ │              ││
│  │ [View Details] ││ │ [View Details] ││ │ [View Detail]││
│  └─────────────────┘ └─────────────────┘ └──────────────┘│
│                                                            │
│  ┌─────────────────┐ ┌─────────────────┐ ┌──────────────┐│
│  │[YouTube Thumb]  │ │[YouTube Thumb]  │ │[YouTube Thum]││
│  │ ...             │ │ ...             │ │ ...          ││
│  └─────────────────┘ └─────────────────┘ └──────────────┘│
│                                                            │
│  [Load More Videos]                                        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## DATA STRUCTURE

### Complete Video Entry:

```
Video:
  - ID: "VIDEO-027"
  - video_id: "ABC123..."
  - title: "Build AI Agent with n8n and OpenAI"
  - channel: "AI Tutorials"
  - duration: "11:30"
  - views: 125000
  - published_date: "2024-11-15"
  - topic_id: "TOPIC-001"
  - status: "COMPLETE"

  - thumbnail_url: auto-generated
  - youtube_url: full URL

  - extracted_entities:
    - tools_count: 4
    - workflows_count: 3
    - actions_count: 12
    - skills_count: 5

  - transcription: full text
  - date_completed: "2025-12-07"
  - total_days: 6
```

---

## HTML STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video Library</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="library-container">
  <!-- Header -->
  <header>
    <h1>Video Library</h1>
    <div class="search-box">
      <input
        type="text"
        id="searchInput"
        placeholder="Search videos..."
        oninput="searchVideos()"
      >
      <span class="search-icon">🔍</span>
    </div>
  </header>

  <!-- Stats & Filters -->
  <div class="controls">
    <div class="stats">
      <span id="videoCount">28 videos</span>
    </div>

    <div class="filters">
      <label>Filters:</label>
      <select id="topicFilter" onchange="applyFilters()">
        <option value="">All Topics</option>
      </select>

      <select id="channelFilter" onchange="applyFilters()">
        <option value="">All Channels</option>
      </select>

      <label>Sort by:</label>
      <select id="sortBy" onchange="applyFilters()">
        <option value="date_desc">Date Added (Newest)</option>
        <option value="date_asc">Date Added (Oldest)</option>
        <option value="views_desc">Views (High to Low)</option>
        <option value="title_asc">Title (A-Z)</option>
      </select>

      <label>View:</label>
      <button onclick="setView('grid')" id="btnGrid" class="active">Grid</button>
      <button onclick="setView('list')" id="btnList">List</button>
    </div>
  </div>

  <!-- Video Grid/List -->
  <div id="videoGrid" class="video-grid">
    <!-- Videos rendered here -->
  </div>

  <!-- Load More -->
  <button id="loadMore" onclick="loadMore()" style="display: none;">
    Load More Videos
  </button>
</div>

<script src="library.js"></script>
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

.library-container {
  max-width: 1400px;
  margin: 0 auto;
}

/* Header */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.search-box {
  position: relative;
  width: 300px;
}

.search-box input {
  width: 100%;
  padding: 10px 40px 10px 15px;
  border: 1px solid #ddd;
  border-radius: 25px;
  font-size: 14px;
}

.search-icon {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: #999;
}

/* Controls */
.controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding: 15px;
  background: white;
  border-radius: 8px;
}

.stats {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.filters {
  display: flex;
  gap: 10px;
  align-items: center;
}

.filters label {
  font-size: 14px;
  color: #666;
}

.filters select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.filters button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.filters button.active {
  background: #2196f3;
  color: white;
  border-color: #2196f3;
}

/* Video Grid */
.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  margin-bottom: 30px;
}

.video-grid.list-view {
  grid-template-columns: 1fr;
}

/* Video Card */
.video-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.3s;
  cursor: pointer;
}

.video-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

/* Thumbnail */
.video-thumbnail {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
  background: #000;
  overflow: hidden;
}

.video-thumbnail img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.video-duration {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0,0,0,0.8);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

/* Video Info */
.video-card-info {
  padding: 15px;
}

.video-id {
  font-size: 11px;
  color: #999;
  margin-bottom: 5px;
}

.video-title {
  font-size: 16px;
  font-weight: bold;
  margin: 5px 0;
  color: #333;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.video-channel {
  font-size: 13px;
  color: #666;
  margin: 5px 0;
}

.video-stats {
  font-size: 12px;
  color: #999;
  margin: 8px 0;
}

.video-stats span {
  margin-right: 12px;
}

.video-entities {
  display: flex;
  gap: 10px;
  margin: 10px 0;
}

.entity-badge {
  background: #e3f2fd;
  color: #1976d2;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: bold;
}

.video-topic {
  display: inline-block;
  background: #fff3e0;
  color: #f57c00;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 11px;
  margin-top: 8px;
}

.btn-view-details {
  width: 100%;
  padding: 10px;
  margin-top: 12px;
  background: #2196f3;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.btn-view-details:hover {
  background: #1976d2;
}

/* List View */
.video-grid.list-view .video-card {
  display: flex;
  flex-direction: row;
}

.video-grid.list-view .video-thumbnail {
  width: 300px;
  padding-bottom: 0;
  height: 170px;
  flex-shrink: 0;
}

.video-grid.list-view .video-card-info {
  flex: 1;
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
  transition: all 0.2s;
}

#loadMore:hover {
  background: #f5f5f5;
}
```

---

## JAVASCRIPT

```javascript
let allVideos = [];
let filteredVideos = [];
let displayedVideos = [];
let topics = [];
let channels = [];
let displayCount = 12;
let currentView = 'grid';

// Load data
window.onload = function() {
  loadData();
  populateFilters();
  applyFilters();
};

function loadData() {
  // Load all videos
  allVideos = JSON.parse(localStorage.getItem('videos') || '[]');

  // Filter only COMPLETE videos
  allVideos = allVideos.filter(v => v.status === 'COMPLETE');

  // Load topics
  topics = JSON.parse(localStorage.getItem('topics') || '[]');

  // Extract unique channels
  channels = [...new Set(allVideos.map(v => v.channel).filter(c => c))];
}

function populateFilters() {
  // Populate topic filter
  const topicFilter = document.getElementById('topicFilter');
  topics.forEach(topic => {
    const option = document.createElement('option');
    option.value = topic.id;
    option.textContent = topic.name;
    topicFilter.appendChild(option);
  });

  // Populate channel filter
  const channelFilter = document.getElementById('channelFilter');
  channels.forEach(channel => {
    const option = document.createElement('option');
    option.value = channel;
    option.textContent = channel;
    channelFilter.appendChild(option);
  });
}

function applyFilters() {
  const topicId = document.getElementById('topicFilter').value;
  const channel = document.getElementById('channelFilter').value;
  const sortBy = document.getElementById('sortBy').value;
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();

  // Start with all videos
  filteredVideos = [...allVideos];

  // Apply topic filter
  if (topicId) {
    filteredVideos = filteredVideos.filter(v => v.topic_id === topicId);
  }

  // Apply channel filter
  if (channel) {
    filteredVideos = filteredVideos.filter(v => v.channel === channel);
  }

  // Apply search
  if (searchTerm) {
    filteredVideos = filteredVideos.filter(v =>
      (v.title || '').toLowerCase().includes(searchTerm) ||
      (v.channel || '').toLowerCase().includes(searchTerm) ||
      (v.id || '').toLowerCase().includes(searchTerm)
    );
  }

  // Apply sorting
  filteredVideos = sortVideos(filteredVideos, sortBy);

  // Update count
  document.getElementById('videoCount').textContent = `${filteredVideos.length} videos`;

  // Reset display count
  displayCount = 12;

  // Display
  displayVideos();
}

function sortVideos(videos, sortBy) {
  const sorted = [...videos];

  switch(sortBy) {
    case 'date_desc':
      return sorted.sort((a, b) => new Date(b.date_added) - new Date(a.date_added));
    case 'date_asc':
      return sorted.sort((a, b) => new Date(a.date_added) - new Date(b.date_added));
    case 'views_desc':
      return sorted.sort((a, b) => (b.views || 0) - (a.views || 0));
    case 'title_asc':
      return sorted.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
    default:
      return sorted;
  }
}

function displayVideos() {
  const container = document.getElementById('videoGrid');
  container.innerHTML = '';

  // Set view class
  container.className = currentView === 'list' ? 'video-grid list-view' : 'video-grid';

  // Show first N videos
  displayedVideos = filteredVideos.slice(0, displayCount);

  displayedVideos.forEach(video => {
    const card = createVideoCard(video);
    container.appendChild(card);
  });

  // Show/hide load more
  const loadMoreBtn = document.getElementById('loadMore');
  if (filteredVideos.length > displayCount) {
    loadMoreBtn.style.display = 'block';
  } else {
    loadMoreBtn.style.display = 'none';
  }
}

function createVideoCard(video) {
  const card = document.createElement('div');
  card.className = 'video-card';
  card.onclick = () => viewDetails(video.id);

  // Get topic
  const topic = topics.find(t => t.id === video.topic_id);
  const topicName = topic ? topic.name : '';

  // Thumbnail URL
  const thumbnailUrl = `https://img.youtube.com/vi/${video.video_id}/mqdefault.jpg`;

  card.innerHTML = `
    <div class="video-thumbnail">
      <img src="${thumbnailUrl}" alt="${video.title || 'Video'}">
      ${video.duration ? `<span class="video-duration">${video.duration}</span>` : ''}
    </div>

    <div class="video-card-info">
      <div class="video-id">${video.id}</div>
      <h3 class="video-title">${video.title || 'Untitled Video'}</h3>
      <div class="video-channel">📺 ${video.channel || 'Unknown Channel'}</div>

      <div class="video-stats">
        ${video.views ? `<span>👁️ ${formatViews(video.views)}</span>` : ''}
        ${video.published_date ? `<span>📅 ${video.published_date}</span>` : ''}
      </div>

      <div class="video-entities">
        ${video.extracted_entities?.tools_count ? `<span class="entity-badge">🔧 ${video.extracted_entities.tools_count} Tools</span>` : ''}
        ${video.extracted_entities?.workflows_count ? `<span class="entity-badge">⚙️ ${video.extracted_entities.workflows_count} Workflows</span>` : ''}
      </div>

      ${topicName ? `<span class="video-topic">${topicName}</span>` : ''}

      <button class="btn-view-details" onclick="event.stopPropagation(); viewDetails('${video.id}')">
        View Details
      </button>
    </div>
  `;

  return card;
}

function formatViews(views) {
  if (views >= 1000000) {
    return (views / 1000000).toFixed(1) + 'M';
  } else if (views >= 1000) {
    return (views / 1000).toFixed(1) + 'K';
  }
  return views.toString();
}

function searchVideos() {
  applyFilters();
}

function setView(view) {
  currentView = view;

  // Update buttons
  document.getElementById('btnGrid').classList.toggle('active', view === 'grid');
  document.getElementById('btnList').classList.toggle('active', view === 'list');

  // Redisplay
  displayVideos();
}

function loadMore() {
  displayCount += 12;
  displayVideos();
}

function viewDetails(videoId) {
  localStorage.setItem('selectedVideo', videoId);
  window.location.href = 'video-detail.html';
}
```

---

## SUCCESS CRITERIA

You've completed Screen 6 when:

✅ Displays all COMPLETE videos
✅ Shows YouTube thumbnails (auto-generated)
✅ Grid and list view toggle
✅ Filter by topic and channel
✅ Sort by date, views, title
✅ Search by title/channel/ID
✅ Shows entity counts (tools, workflows)
✅ Click card to view details
✅ Load more pagination
✅ Responsive layout

---

## NEXT STEP

**Go to Page 7: Screen 7 - Channel Catalog**

Build the channel browsing view to see all videos grouped by YouTube channel.
