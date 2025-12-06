# PAGE 10: ADVANCED FEATURES & ENHANCEMENTS

**Add powerful features to enhance your video research system**

---

## OVERVIEW

Now that you have the core 8-screen system working, add these advanced features to make the app more powerful and user-friendly.

---

## FEATURE 1: BULK OPERATIONS

### What This Does:
- Select multiple videos at once
- Apply actions to all selected videos
- Move multiple videos through stages together

### Implementation:

Add checkboxes to video cards:

```javascript
// In transcription-queue.html
function createVideoCard(video) {
  const card = document.createElement('div');
  card.className = 'video-card';

  card.innerHTML = `
    <input type="checkbox"
           class="video-checkbox"
           data-video-id="${video.id}"
           onchange="updateBulkActions()">

    <div class="video-content">
      <!-- Existing video card content -->
    </div>
  `;

  return card;
}

// Bulk actions bar
let selectedVideos = [];

function updateBulkActions() {
  selectedVideos = Array.from(document.querySelectorAll('.video-checkbox:checked'))
    .map(cb => cb.dataset.videoId);

  const bulkBar = document.getElementById('bulkActionsBar');

  if (selectedVideos.length > 0) {
    bulkBar.style.display = 'flex';
    bulkBar.innerHTML = `
      <span>${selectedVideos.length} videos selected</span>
      <button onclick="bulkMarkSelected()">Mark All as Selected</button>
      <button onclick="bulkDelete()">Delete Selected</button>
      <button onclick="clearSelection()">Clear Selection</button>
    `;
  } else {
    bulkBar.style.display = 'none';
  }
}

function bulkMarkSelected() {
  const allVideos = JSON.parse(localStorage.getItem('videos') || '[]');

  selectedVideos.forEach(videoId => {
    const video = allVideos.find(v => v.id === videoId);
    if (video && video.status === 'QUEUED') {
      video.status = 'SELECTED';
      video.stage_dates = video.stage_dates || {};
      video.stage_dates.selected = new Date().toISOString().split('T')[0];
    }
  });

  localStorage.setItem('videos', JSON.stringify(allVideos));
  clearSelection();
  loadData();
}

function bulkDelete() {
  if (!confirm(`Delete ${selectedVideos.length} videos?`)) return;

  let allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  allVideos = allVideos.filter(v => !selectedVideos.includes(v.id));

  localStorage.setItem('videos', JSON.stringify(allVideos));
  clearSelection();
  loadData();
}

function clearSelection() {
  document.querySelectorAll('.video-checkbox').forEach(cb => cb.checked = false);
  selectedVideos = [];
  updateBulkActions();
}
```

---

## FEATURE 2: ADVANCED FILTERING

### What This Does:
- Filter by multiple criteria simultaneously
- Date range filtering
- Search within titles/channels
- Save filter presets

### Implementation:

```javascript
// Enhanced filter system
const filterState = {
  topics: [],
  channels: [],
  statuses: [],
  dateRange: { start: null, end: null },
  search: '',
  minViews: 0,
  maxDuration: null
};

function buildFilterUI() {
  return `
    <div class="advanced-filters">
      <div class="filter-section">
        <label>Search:</label>
        <input type="text"
               id="searchInput"
               placeholder="Search titles, channels..."
               oninput="applyFilters()">
      </div>

      <div class="filter-section">
        <label>Topics:</label>
        <select id="topicFilter" multiple onchange="applyFilters()">
          ${topics.map(t => `<option value="${t.id}">${t.name}</option>`).join('')}
        </select>
      </div>

      <div class="filter-section">
        <label>Status:</label>
        <div class="checkbox-group">
          <label><input type="checkbox" value="QUEUED" onchange="applyFilters()"> Queued</label>
          <label><input type="checkbox" value="SELECTED" onchange="applyFilters()"> Selected</label>
          <label><input type="checkbox" value="COMPLETE" onchange="applyFilters()"> Complete</label>
        </div>
      </div>

      <div class="filter-section">
        <label>Date Range:</label>
        <input type="date" id="dateStart" onchange="applyFilters()">
        <span>to</span>
        <input type="date" id="dateEnd" onchange="applyFilters()">
      </div>

      <div class="filter-section">
        <label>Min Views:</label>
        <input type="number"
               id="minViews"
               placeholder="0"
               onchange="applyFilters()">
      </div>

      <div class="filter-actions">
        <button onclick="saveFilterPreset()">Save Preset</button>
        <button onclick="clearAllFilters()">Clear All</button>
      </div>
    </div>
  `;
}

function applyFilters() {
  // Update filter state
  filterState.search = document.getElementById('searchInput').value.toLowerCase();
  filterState.topics = Array.from(document.getElementById('topicFilter').selectedOptions)
    .map(o => o.value);
  filterState.statuses = Array.from(document.querySelectorAll('.checkbox-group input:checked'))
    .map(cb => cb.value);
  filterState.dateRange.start = document.getElementById('dateStart').value;
  filterState.dateRange.end = document.getElementById('dateEnd').value;
  filterState.minViews = parseInt(document.getElementById('minViews').value) || 0;

  // Apply filters
  let filtered = [...allVideos];

  // Search filter
  if (filterState.search) {
    filtered = filtered.filter(v =>
      v.title?.toLowerCase().includes(filterState.search) ||
      v.channel?.toLowerCase().includes(filterState.search)
    );
  }

  // Topic filter
  if (filterState.topics.length > 0) {
    filtered = filtered.filter(v => filterState.topics.includes(v.topic_id));
  }

  // Status filter
  if (filterState.statuses.length > 0) {
    filtered = filtered.filter(v => filterState.statuses.includes(v.status));
  }

  // Date range filter
  if (filterState.dateRange.start) {
    filtered = filtered.filter(v => v.date_added >= filterState.dateRange.start);
  }
  if (filterState.dateRange.end) {
    filtered = filtered.filter(v => v.date_added <= filterState.dateRange.end);
  }

  // Views filter
  filtered = filtered.filter(v => (v.views || 0) >= filterState.minViews);

  displayVideos(filtered);
}

function saveFilterPreset() {
  const presetName = prompt('Enter preset name:');
  if (!presetName) return;

  const presets = JSON.parse(localStorage.getItem('filterPresets') || '{}');
  presets[presetName] = { ...filterState };

  localStorage.setItem('filterPresets', JSON.stringify(presets));
  alert('Filter preset saved!');
}
```

---

## FEATURE 3: EXPORT & REPORTING

### What This Does:
- Export data to CSV/JSON
- Generate summary reports
- Create entity lists (all tools, all workflows)
- Download transcriptions

### Implementation:

```javascript
// Export functionality
function exportToCSV() {
  const headers = ['ID', 'Title', 'Channel', 'Duration', 'Views', 'Status', 'Date Added', 'Topic'];

  const rows = allVideos.map(v => [
    v.id,
    `"${v.title || ''}"`,
    v.channel || '',
    v.duration || '',
    v.views || 0,
    v.status,
    v.date_added || '',
    v.topic_id || ''
  ]);

  let csv = headers.join(',') + '\n';
  csv += rows.map(row => row.join(',')).join('\n');

  downloadFile(csv, 'videos-export.csv', 'text/csv');
}

function exportToJSON() {
  const exportData = {
    exported_at: new Date().toISOString(),
    total_videos: allVideos.length,
    topics: topics,
    videos: allVideos
  };

  const json = JSON.stringify(exportData, null, 2);
  downloadFile(json, 'videos-export.json', 'application/json');
}

function generateReport() {
  const completed = allVideos.filter(v => v.status === 'COMPLETE');

  // Aggregate all entities
  const allTools = new Set();
  const allWorkflows = new Set();
  const allActions = new Set();
  const allSkills = new Set();

  completed.forEach(v => {
    if (v.extracted_entities) {
      v.extracted_entities.tools?.forEach(t => allTools.add(t.name));
      v.extracted_entities.workflows?.forEach(w => allWorkflows.add(w.name));
      v.extracted_entities.actions?.forEach(a => allActions.add(a));
      v.extracted_entities.skills?.forEach(s => allSkills.add(s));
    }
  });

  const report = `
# VIDEO RESEARCH REPORT
Generated: ${new Date().toLocaleDateString()}

## SUMMARY
- Total Videos: ${allVideos.length}
- Completed: ${completed.length}
- In Progress: ${allVideos.filter(v => v.status !== 'COMPLETE' && v.status !== 'QUEUED').length}
- Queued: ${allVideos.filter(v => v.status === 'QUEUED').length}

## RESEARCH TOPICS
${topics.map(t => `- ${t.name} (${t.videos_found} videos)`).join('\n')}

## ENTITIES EXTRACTED

### Tools Found (${allTools.size} unique)
${Array.from(allTools).sort().map(t => `- ${t}`).join('\n')}

### Workflows Identified (${allWorkflows.size} unique)
${Array.from(allWorkflows).sort().map(w => `- ${w}`).join('\n')}

### Actions Documented (${allActions.size} unique)
${Array.from(allActions).sort().join(', ')}

### Skills Required (${allSkills.size} unique)
${Array.from(allSkills).sort().join(', ')}

## TOP CHANNELS
${getTopChannels(5).map((c, i) => `${i+1}. ${c.name} (${c.count} videos)`).join('\n')}
  `;

  downloadFile(report, 'research-report.md', 'text/markdown');
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function getTopChannels(limit) {
  const channelCounts = {};

  allVideos.forEach(v => {
    const channel = v.channel || 'Unknown';
    channelCounts[channel] = (channelCounts[channel] || 0) + 1;
  });

  return Object.entries(channelCounts)
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => b.count - a.count)
    .slice(0, limit);
}
```

---

## FEATURE 4: STATISTICS DASHBOARD

### What This Does:
- Visual charts and graphs
- Processing time analytics
- Entity frequency analysis
- Channel performance metrics

### Implementation:

Create a new screen: `statistics.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Statistics Dashboard</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="stats-dashboard">
  <header>
    <h1>Statistics Dashboard</h1>
    <a href="video-library.html">← Back to Library</a>
  </header>

  <!-- Summary Cards -->
  <div class="summary-cards">
    <div class="stat-card">
      <h3 id="totalVideos">0</h3>
      <p>Total Videos</p>
    </div>
    <div class="stat-card">
      <h3 id="completedVideos">0</h3>
      <p>Completed</p>
    </div>
    <div class="stat-card">
      <h3 id="avgProcessingTime">0</h3>
      <p>Avg Days to Complete</p>
    </div>
    <div class="stat-card">
      <h3 id="totalTools">0</h3>
      <p>Unique Tools</p>
    </div>
  </div>

  <!-- Charts Section -->
  <section class="charts-section">
    <div class="chart-container">
      <h2>Videos by Status</h2>
      <div id="statusChart" class="bar-chart"></div>
    </div>

    <div class="chart-container">
      <h2>Top Channels</h2>
      <div id="channelChart" class="bar-chart"></div>
    </div>

    <div class="chart-container">
      <h2>Videos Added Over Time</h2>
      <div id="timelineChart" class="line-chart"></div>
    </div>

    <div class="chart-container">
      <h2>Most Common Tools</h2>
      <div id="toolsChart" class="bar-chart"></div>
    </div>
  </section>

  <!-- Detailed Tables -->
  <section class="tables-section">
    <h2>Processing Time Analysis</h2>
    <table id="processingTable">
      <thead>
        <tr>
          <th>Video</th>
          <th>Started</th>
          <th>Completed</th>
          <th>Days</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
  </section>
</div>

<script src="statistics.js"></script>
</body>
</html>
```

```javascript
// statistics.js
let allVideos = [];
let topics = [];

window.onload = function() {
  loadData();
  calculateStats();
  renderCharts();
};

function loadData() {
  allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  topics = JSON.parse(localStorage.getItem('topics') || '[]');
}

function calculateStats() {
  const completed = allVideos.filter(v => v.status === 'COMPLETE');

  // Summary stats
  document.getElementById('totalVideos').textContent = allVideos.length;
  document.getElementById('completedVideos').textContent = completed.length;

  // Avg processing time
  const timesWithDays = completed.filter(v => v.total_days);
  const avgDays = timesWithDays.length > 0
    ? Math.round(timesWithDays.reduce((sum, v) => sum + v.total_days, 0) / timesWithDays.length)
    : 0;
  document.getElementById('avgProcessingTime').textContent = avgDays;

  // Unique tools
  const uniqueTools = new Set();
  completed.forEach(v => {
    v.extracted_entities?.tools?.forEach(t => uniqueTools.add(t.name));
  });
  document.getElementById('totalTools').textContent = uniqueTools.size;
}

function renderCharts() {
  renderStatusChart();
  renderChannelChart();
  renderTimelineChart();
  renderToolsChart();
  renderProcessingTable();
}

function renderStatusChart() {
  const statusCounts = {};
  allVideos.forEach(v => {
    statusCounts[v.status] = (statusCounts[v.status] || 0) + 1;
  });

  const container = document.getElementById('statusChart');
  const maxCount = Math.max(...Object.values(statusCounts));

  container.innerHTML = Object.entries(statusCounts)
    .map(([status, count]) => {
      const percentage = (count / maxCount) * 100;
      return `
        <div class="bar-item">
          <div class="bar-label">${status}</div>
          <div class="bar-wrapper">
            <div class="bar-fill" style="width: ${percentage}%"></div>
            <span class="bar-value">${count}</span>
          </div>
        </div>
      `;
    }).join('');
}

function renderChannelChart() {
  const channels = getTopChannels(10);
  const maxCount = channels[0]?.count || 1;

  const container = document.getElementById('channelChart');
  container.innerHTML = channels.map(channel => {
    const percentage = (channel.count / maxCount) * 100;
    return `
      <div class="bar-item">
        <div class="bar-label">${channel.name}</div>
        <div class="bar-wrapper">
          <div class="bar-fill" style="width: ${percentage}%"></div>
          <span class="bar-value">${channel.count}</span>
        </div>
      </div>
    `;
  }).join('');
}

function renderToolsChart() {
  const toolCounts = {};

  allVideos.filter(v => v.status === 'COMPLETE').forEach(v => {
    v.extracted_entities?.tools?.forEach(t => {
      toolCounts[t.name] = (toolCounts[t.name] || 0) + 1;
    });
  });

  const topTools = Object.entries(toolCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 15);

  const maxCount = topTools[0]?.[1] || 1;

  const container = document.getElementById('toolsChart');
  container.innerHTML = topTools.map(([tool, count]) => {
    const percentage = (count / maxCount) * 100;
    return `
      <div class="bar-item">
        <div class="bar-label">${tool}</div>
        <div class="bar-wrapper">
          <div class="bar-fill" style="width: ${percentage}%"></div>
          <span class="bar-value">${count}</span>
        </div>
      </div>
    `;
  }).join('');
}

function renderProcessingTable() {
  const completed = allVideos
    .filter(v => v.status === 'COMPLETE' && v.total_days)
    .sort((a, b) => b.total_days - a.total_days);

  const tbody = document.querySelector('#processingTable tbody');
  tbody.innerHTML = completed.map(v => `
    <tr>
      <td>${v.title || v.id}</td>
      <td>${v.date_added || 'N/A'}</td>
      <td>${v.date_completed || 'N/A'}</td>
      <td>${v.total_days} days</td>
    </tr>
  `).join('');
}
```

---

## FEATURE 5: KEYBOARD SHORTCUTS

### What This Does:
- Navigate with keyboard
- Quick actions with hotkeys
- Accessibility improvements

### Implementation:

```javascript
// Add to main.js or each screen
document.addEventListener('keydown', function(e) {
  // Ignore if typing in input
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
    return;
  }

  // Keyboard shortcuts
  switch(e.key) {
    case 'n':
      if (e.ctrlKey) {
        e.preventDefault();
        createNewTopic();
      }
      break;

    case 's':
      if (e.ctrlKey) {
        e.preventDefault();
        saveCurrentData();
      }
      break;

    case 'f':
      if (e.ctrlKey) {
        e.preventDefault();
        document.getElementById('searchInput')?.focus();
      }
      break;

    case 'Escape':
      clearSelection();
      closeModals();
      break;

    case 'ArrowLeft':
      if (e.ctrlKey) {
        navigateBack();
      }
      break;

    case 'ArrowRight':
      if (e.ctrlKey) {
        navigateForward();
      }
      break;
  }
});

// Show keyboard shortcuts help
function showKeyboardHelp() {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content">
      <h2>Keyboard Shortcuts</h2>
      <table class="shortcuts-table">
        <tr><td><kbd>Ctrl</kbd> + <kbd>N</kbd></td><td>New Topic</td></tr>
        <tr><td><kbd>Ctrl</kbd> + <kbd>S</kbd></td><td>Save</td></tr>
        <tr><td><kbd>Ctrl</kbd> + <kbd>F</kbd></td><td>Search</td></tr>
        <tr><td><kbd>Ctrl</kbd> + <kbd>←</kbd></td><td>Navigate Back</td></tr>
        <tr><td><kbd>Ctrl</kbd> + <kbd>→</kbd></td><td>Navigate Forward</td></tr>
        <tr><td><kbd>Esc</kbd></td><td>Clear/Close</td></tr>
      </table>
      <button onclick="this.closest('.modal').remove()">Close</button>
    </div>
  `;
  document.body.appendChild(modal);
}
```

---

## SUCCESS CRITERIA

You've added advanced features when:

✅ Bulk operations work for selecting/acting on multiple videos
✅ Advanced filtering with multiple criteria works
✅ Can export data to CSV/JSON formats
✅ Statistics dashboard shows visual analytics
✅ Reports can be generated with entity summaries
✅ Keyboard shortcuts improve navigation
✅ All features integrate smoothly with existing screens

---

## NEXT STEPS

**Go to PAGE_11: Integration & API Features**

Add external integrations like YouTube API, transcription services, and data sync.
