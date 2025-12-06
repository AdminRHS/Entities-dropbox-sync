# PAGE 7: SCREEN 7 - Channel Catalog

**Browse videos grouped by YouTube channels**

---

## WHAT THIS SCREEN DOES

Show all YouTube channels that have been processed:
- List channels with logos/avatars
- Show video count per channel
- Show extracted entities count per channel
- Click to see all videos from that channel

---

## VISUAL LAYOUT

```
┌────────────────────────────────────────────────────────┐
│  YouTube Channels                                      │
│  ═══════════════════                                   │
│                                                        │
│  15 channels | 28 total videos                        │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │ [Channel Avatar]  AI Tutorials                 │   │
│  │                                                │   │
│  │ 📺 Videos processed: 8                         │   │
│  │ 🔧 Total tools found: 45                       │   │
│  │ ⚙️  Total workflows: 24                        │   │
│  │                                                │   │
│  │ Latest: "Build AI Agent with n8n" (Nov 2024)   │   │
│  │                                                │   │
│  │ [View All Videos from Channel →]               │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │ [Channel Avatar]  Tech Guide                   │   │
│  │                                                │   │
│  │ 📺 Videos processed: 5                         │   │
│  │ 🔧 Total tools found: 28                       │   │
│  │ ⚙️  Total workflows: 12                        │   │
│  │                                                │   │
│  │ Latest: "Automate Everything..." (Oct 2024)    │   │
│  │                                                │   │
│  │ [View All Videos from Channel →]               │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  [Show More Channels]                                  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## DATA STRUCTURE

### Channel Summary:

```
Channel:
  - name: "AI Tutorials"
  - video_count: 8
  - total_tools: 45
  - total_workflows: 24
  - total_actions: 96
  - total_skills: 32
  - latest_video: {
      id: "VIDEO-027",
      title: "Build AI Agent...",
      date: "2024-11-15"
    }
  - videos: ["VIDEO-027", "VIDEO-015", ...]
```

---

## HTML STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>YouTube Channels</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="channels-container">
  <!-- Header -->
  <header>
    <h1>YouTube Channels</h1>
    <a href="video-library.html" class="back-link">← Back to Library</a>
  </header>

  <!-- Stats -->
  <div class="stats">
    <span id="channelCount">Loading...</span>
  </div>

  <!-- Channel List -->
  <div id="channelList">
    <!-- Channels rendered here -->
  </div>

  <!-- Load More -->
  <button id="loadMore" onclick="loadMore()" style="display: none;">
    Show More Channels
  </button>
</div>

<script src="channels.js"></script>
</body>
</html>
```

---

## CSS STYLING

```css
.channels-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.back-link {
  color: #2196f3;
  text-decoration: none;
}

.stats {
  font-size: 16px;
  color: #666;
  margin-bottom: 25px;
}

/* Channel Card */
.channel-card {
  background: white;
  border-radius: 12px;
  padding: 25px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.3s;
}

.channel-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.channel-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.channel-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  font-weight: bold;
  color: white;
  margin-right: 20px;
}

.channel-info h2 {
  margin: 0 0 5px 0;
  font-size: 24px;
  color: #333;
}

.channel-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  margin: 15px 0;
}

.stat-item {
  text-align: center;
  padding: 12px;
  background: #f5f5f5;
  border-radius: 8px;
}

.stat-value {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  display: block;
}

.stat-label {
  font-size: 12px;
  color: #666;
  margin-top: 4px;
}

.channel-latest {
  margin: 15px 0;
  padding: 12px;
  background: #e3f2fd;
  border-radius: 8px;
}

.channel-latest-label {
  font-size: 12px;
  color: #666;
  font-weight: bold;
  margin-bottom: 5px;
}

.channel-latest-title {
  font-size: 14px;
  color: #333;
}

.btn-view-channel {
  width: 100%;
  padding: 12px;
  background: #2196f3;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.2s;
}

.btn-view-channel:hover {
  background: #1976d2;
}
```

---

## JAVASCRIPT

```javascript
let allVideos = [];
let channels = [];
let displayCount = 10;

// Load data
window.onload = function() {
  loadData();
  analyzeChannels();
  displayChannels();
};

function loadData() {
  // Load completed videos
  allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  allVideos = allVideos.filter(v => v.status === 'COMPLETE');
}

function analyzeChannels() {
  const channelMap = {};

  // Group videos by channel
  allVideos.forEach(video => {
    const channelName = video.channel || 'Unknown Channel';

    if (!channelMap[channelName]) {
      channelMap[channelName] = {
        name: channelName,
        videos: [],
        total_tools: 0,
        total_workflows: 0,
        total_actions: 0,
        total_skills: 0
      };
    }

    channelMap[channelName].videos.push(video);

    // Aggregate entity counts
    if (video.extracted_entities) {
      channelMap[channelName].total_tools += video.extracted_entities.tools_count || 0;
      channelMap[channelName].total_workflows += video.extracted_entities.workflows_count || 0;
      channelMap[channelName].total_actions += video.extracted_entities.actions_count || 0;
      channelMap[channelName].total_skills += video.extracted_entities.skills_count || 0;
    }
  });

  // Convert to array and calculate stats
  channels = Object.values(channelMap).map(channel => {
    // Sort videos by date
    channel.videos.sort((a, b) => new Date(b.date_added) - new Date(a.date_added));

    return {
      name: channel.name,
      video_count: channel.videos.length,
      total_tools: channel.total_tools,
      total_workflows: channel.total_workflows,
      total_actions: channel.total_actions,
      total_skills: channel.total_skills,
      latest_video: channel.videos[0],
      videos: channel.videos
    };
  });

  // Sort by video count (most videos first)
  channels.sort((a, b) => b.video_count - a.video_count);

  // Update stats
  document.getElementById('channelCount').textContent =
    `${channels.length} channels | ${allVideos.length} total videos`;
}

function displayChannels() {
  const container = document.getElementById('channelList');
  container.innerHTML = '';

  // Show first N channels
  const channelsToShow = channels.slice(0, displayCount);

  channelsToShow.forEach(channel => {
    const card = createChannelCard(channel);
    container.appendChild(card);
  });

  // Show/hide load more
  const loadMoreBtn = document.getElementById('loadMore');
  if (channels.length > displayCount) {
    loadMoreBtn.style.display = 'block';
  } else {
    loadMoreBtn.style.display = 'none';
  }
}

function createChannelCard(channel) {
  const card = document.createElement('div');
  card.className = 'channel-card';

  // Get first letter for avatar
  const initial = channel.name.charAt(0).toUpperCase();

  card.innerHTML = `
    <div class="channel-header">
      <div class="channel-avatar">${initial}</div>
      <div class="channel-info">
        <h2>${channel.name}</h2>
      </div>
    </div>

    <div class="channel-stats">
      <div class="stat-item">
        <span class="stat-value">${channel.video_count}</span>
        <span class="stat-label">Videos</span>
      </div>
      <div class="stat-item">
        <span class="stat-value">${channel.total_tools}</span>
        <span class="stat-label">Tools</span>
      </div>
      <div class="stat-item">
        <span class="stat-value">${channel.total_workflows}</span>
        <span class="stat-label">Workflows</span>
      </div>
    </div>

    ${channel.latest_video ? `
      <div class="channel-latest">
        <div class="channel-latest-label">Latest Video:</div>
        <div class="channel-latest-title">
          "${channel.latest_video.title || 'Untitled'}"
          ${channel.latest_video.published_date ? `(${channel.latest_video.published_date})` : ''}
        </div>
      </div>
    ` : ''}

    <button onclick="viewChannel('${channel.name}')" class="btn-view-channel">
      View All Videos from Channel →
    </button>
  `;

  return card;
}

function viewChannel(channelName) {
  // Store channel name and navigate to library with filter
  localStorage.setItem('filterChannel', channelName);
  window.location.href = 'video-library.html';
}

function loadMore() {
  displayCount += 10;
  displayChannels();
}
```

---

## OPTIONAL: CHANNEL DETAIL PAGE

Create separate page showing all videos from one channel:

```html
<!-- channel-detail.html -->
<div class="channel-detail">
  <h1 id="channelName"></h1>
  <p id="channelStats"></p>

  <h2>All Videos</h2>
  <div id="channelVideos" class="video-grid">
    <!-- Videos from this channel -->
  </div>
</div>
```

---

## SUCCESS CRITERIA

You've completed Screen 7 when:

✅ Lists all unique channels
✅ Shows video count per channel
✅ Shows total entities per channel (tools, workflows)
✅ Shows latest video from each channel
✅ Sorted by video count (most productive first)
✅ Click to filter library by channel
✅ Pagination (load more)
✅ Channel avatar/initial display

---

## NEXT STEP

**Go to Page 8: Screen 8 - Video Detail Page**

Build the final detailed view showing everything about one completed video.
