# PAGE 5: SCREEN 5 - Processing Detail View

**Process a single video through stages with progress tracking**

---

## WHAT THIS SCREEN DOES

Show full details for one video being processed:
- Embedded YouTube player (watch while working)
- Progress through stages
- Upload transcription file
- Move to next stage
- Add notes

---

## VISUAL LAYOUT

```
┌────────────────────────────────────────────────────────┐
│  ← Back to Queue                                       │
│                                                        │
│  VIDEO-027: "Build AI Agent with n8n and OpenAI"      │
│  ════════════════════════════════════════════════════  │
│                                                        │
│  [Full YouTube Player - 100% width]                    │
│  ▶ Video plays here                                    │
│                                                        │
│  ──────────────────────────────────────────────────── │
│                                                        │
│  PROGRESS TRACKER                                      │
│                                                        │
│  ✅ Queued          2025-12-01                        │
│  ✅ Selected        2025-12-02                        │
│  ⏳ Transcribing    In progress...                     │
│  ⏹ Analyzed        Not started                        │
│  ⏹ Integrated      Not started                        │
│  ⏹ Complete        Not started                        │
│                                                        │
│  ──────────────────────────────────────────────────── │
│                                                        │
│  CURRENT STAGE: TRANSCRIBING                           │
│                                                        │
│  Upload transcription file:                            │
│  [Choose File] No file chosen                          │
│                                                        │
│  Or paste transcription:                               │
│  ┌────────────────────────────────────────────────┐   │
│  │                                                │   │
│  │  (Text area for transcription)                 │   │
│  │                                                │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  [Mark as Transcribed →]                               │
│                                                        │
│  ──────────────────────────────────────────────────── │
│                                                        │
│  NOTES                                                 │
│  ┌────────────────────────────────────────────────┐   │
│  │  Add notes about this video...                 │   │
│  └────────────────────────────────────────────────┘   │
│  [Save Notes]                                          │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## STAGE PROGRESSION

### Stages (Sequential):

```
1. QUEUED      - Added to system
2. SELECTED    - Chosen for processing
3. TRANSCRIBING - Getting transcript
4. ANALYZED    - Entities extracted
5. INTEGRATED  - Added to library
6. COMPLETE    - Fully processed
```

### Rules:
- Must complete stages in order
- Cannot skip stages
- Each stage records completion date
- Current stage highlighted

---

## DATA STRUCTURE

### Video with Stage Tracking:

```
Video:
  - ID: "VIDEO-027"
  - video_id: "ABC123..."
  - title: "Build AI Agent..."
  - status: "TRANSCRIBING" (current stage)

  - stage_dates: {
      queued: "2025-12-01",
      selected: "2025-12-02",
      transcribing: null,    // In progress
      analyzed: null,
      integrated: null,
      complete: null
    }

  - transcription: "" (text content)
  - transcription_file: null (file path/URL)
  - notes: ""
  - date_started: "2025-12-01"
  - date_completed: null
  - total_days: null
```

---

## HTML STRUCTURE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Processing Video</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="processing-container">
  <!-- Header -->
  <a href="transcription-queue.html" class="back-link">← Back to Queue</a>

  <h1 id="videoTitle">Loading...</h1>

  <!-- YouTube Player -->
  <div class="video-player">
    <iframe
      id="youtubePlayer"
      width="100%"
      height="500"
      frameborder="0"
      allowfullscreen>
    </iframe>
  </div>

  <!-- Progress Tracker -->
  <section class="progress-section">
    <h2>Progress Tracker</h2>
    <div class="progress-list" id="progressList">
      <!-- Stages rendered here -->
    </div>
  </section>

  <!-- Current Stage Actions -->
  <section class="stage-actions" id="stageActions">
    <h2>Current Stage: <span id="currentStage"></span></h2>
    <div id="stageContent">
      <!-- Stage-specific content loaded here -->
    </div>
  </section>

  <!-- Notes -->
  <section class="notes-section">
    <h2>Notes</h2>
    <textarea
      id="notes"
      rows="5"
      placeholder="Add notes about this video..."
    ></textarea>
    <button onclick="saveNotes()" class="btn-save">Save Notes</button>
  </section>

</div>

<script src="processing.js"></script>
</body>
</html>
```

---

## CSS STYLING

```css
.processing-container {
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
}

/* Video Player */
.video-player {
  margin: 20px 0;
  background: #000;
  border-radius: 8px;
  overflow: hidden;
}

.video-player iframe {
  display: block;
  width: 100%;
}

/* Progress Section */
.progress-section {
  background: white;
  padding: 30px;
  border-radius: 12px;
  margin: 30px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.progress-list {
  margin-top: 20px;
}

.progress-item {
  display: flex;
  align-items: center;
  padding: 15px;
  margin: 10px 0;
  border-left: 4px solid #ddd;
  background: #f9f9f9;
  border-radius: 4px;
}

.progress-item.complete {
  border-left-color: #4caf50;
  background: #e8f5e9;
}

.progress-item.in-progress {
  border-left-color: #ff9800;
  background: #fff3e0;
}

.progress-item .icon {
  font-size: 24px;
  margin-right: 15px;
}

.progress-item .details {
  flex: 1;
}

.progress-item .stage-name {
  font-weight: bold;
  margin-bottom: 5px;
}

.progress-item .stage-date {
  color: #666;
  font-size: 14px;
}

/* Stage Actions */
.stage-actions {
  background: white;
  padding: 30px;
  border-radius: 12px;
  margin: 30px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

#currentStage {
  color: #ff9800;
  font-weight: bold;
}

.file-upload {
  margin: 20px 0;
}

.file-upload input[type="file"] {
  margin: 10px 0;
}

.transcription-input {
  width: 100%;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-family: monospace;
  font-size: 14px;
  margin: 10px 0;
}

.btn-next-stage {
  background: #4caf50;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 16px;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 20px;
}

.btn-next-stage:hover {
  background: #45a049;
}

.btn-next-stage:disabled {
  background: #ccc;
  cursor: not-allowed;
}

/* Notes */
.notes-section {
  background: white;
  padding: 30px;
  border-radius: 12px;
  margin: 30px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.notes-section textarea {
  width: 100%;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-family: inherit;
  margin: 10px 0;
}

.btn-save {
  background: #2196f3;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
}

.btn-save:hover {
  background: #1976d2;
}
```

---

## JAVASCRIPT

```javascript
const STAGES = [
  { key: 'queued', label: 'Queued' },
  { key: 'selected', label: 'Selected' },
  { key: 'transcribing', label: 'Transcribing' },
  { key: 'analyzed', label: 'Analyzed' },
  { key: 'integrated', label: 'Integrated' },
  { key: 'complete', label: 'Complete' }
];

let currentVideo = null;

// Load video
window.onload = function() {
  const videoId = localStorage.getItem('currentVideo');

  if (!videoId) {
    alert('No video selected');
    window.location.href = 'transcription-queue.html';
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

  // Display video info
  document.getElementById('videoTitle').textContent =
    `${currentVideo.id}: ${currentVideo.title || 'YouTube Video'}`;

  // Load YouTube player
  const embedUrl = `https://www.youtube.com/embed/${currentVideo.video_id}`;
  document.getElementById('youtubePlayer').src = embedUrl;

  // Display progress
  displayProgress();

  // Load stage actions
  displayStageActions();

  // Load notes
  document.getElementById('notes').value = currentVideo.notes || '';
}

function displayProgress() {
  const container = document.getElementById('progressList');
  container.innerHTML = '';

  // Find current stage index
  const currentStageIndex = getCurrentStageIndex();

  STAGES.forEach((stage, index) => {
    const item = document.createElement('div');

    let className = 'progress-item';
    let icon = '⏹';
    let status = 'Not started';

    if (index < currentStageIndex) {
      // Completed
      className += ' complete';
      icon = '✅';
      status = currentVideo.stage_dates?.[stage.key] || 'Completed';
    } else if (index === currentStageIndex) {
      // In progress
      className += ' in-progress';
      icon = '⏳';
      status = 'In progress...';
    }

    item.className = className;
    item.innerHTML = `
      <span class="icon">${icon}</span>
      <div class="details">
        <div class="stage-name">${stage.label}</div>
        <div class="stage-date">${status}</div>
      </div>
    `;

    container.appendChild(item);
  });
}

function getCurrentStageIndex() {
  // Find which stage video is currently at
  const status = currentVideo.status.toLowerCase();

  for (let i = 0; i < STAGES.length; i++) {
    if (STAGES[i].key === status) {
      return i;
    }
  }

  return 0;
}

function displayStageActions() {
  const currentStageIndex = getCurrentStageIndex();
  const currentStage = STAGES[currentStageIndex];

  document.getElementById('currentStage').textContent = currentStage.label;

  const content = document.getElementById('stageContent');

  // Different content based on stage
  if (currentStage.key === 'transcribing') {
    content.innerHTML = `
      <div class="file-upload">
        <label>Upload transcription file:</label>
        <input type="file" id="transcriptionFile" accept=".txt,.json">
      </div>

      <div>
        <label>Or paste transcription:</label>
        <textarea
          id="transcriptionText"
          class="transcription-input"
          rows="10"
          placeholder="Paste transcription text here..."
        ></textarea>
      </div>

      <button onclick="markTranscribed()" class="btn-next-stage">
        Mark as Transcribed →
      </button>
    `;

    // Load existing transcription if any
    if (currentVideo.transcription) {
      document.getElementById('transcriptionText').value = currentVideo.transcription;
    }

  } else if (currentStage.key === 'analyzed') {
    content.innerHTML = `
      <p>Run entity extraction on the transcription.</p>
      <p>Use PMT-004 prompt to analyze and extract entities.</p>

      <button onclick="markAnalyzed()" class="btn-next-stage">
        Mark as Analyzed →
      </button>
    `;

  } else if (currentStage.key === 'integrated') {
    content.innerHTML = `
      <p>Integrate extracted entities into libraries.</p>

      <button onclick="markIntegrated()" class="btn-next-stage">
        Mark as Integrated →
      </button>
    `;

  } else {
    content.innerHTML = `
      <button onclick="moveToNextStage()" class="btn-next-stage">
        Move to Next Stage →
      </button>
    `;
  }
}

function markTranscribed() {
  // Get transcription
  const text = document.getElementById('transcriptionText').value;
  const file = document.getElementById('transcriptionFile').files[0];

  if (!text && !file) {
    alert('Please provide transcription text or file');
    return;
  }

  if (text) {
    currentVideo.transcription = text;
  }

  if (file) {
    // In real app, upload file to server
    currentVideo.transcription_file = file.name;
  }

  moveToNextStage();
}

function markAnalyzed() {
  // In real app, would run analysis here
  moveToNextStage();
}

function markIntegrated() {
  // In real app, would integrate entities here
  moveToNextStage();
}

function moveToNextStage() {
  const currentIndex = getCurrentStageIndex();

  if (currentIndex >= STAGES.length - 1) {
    alert('Video is already complete!');
    return;
  }

  const nextStage = STAGES[currentIndex + 1];

  // Update status
  currentVideo.status = nextStage.key.toUpperCase();

  // Record completion date for current stage
  if (!currentVideo.stage_dates) {
    currentVideo.stage_dates = {};
  }
  currentVideo.stage_dates[STAGES[currentIndex].key] = new Date().toISOString().split('T')[0];

  // If completing, calculate total days
  if (nextStage.key === 'complete') {
    currentVideo.date_completed = new Date().toISOString().split('T')[0];
    const start = new Date(currentVideo.date_started || currentVideo.stage_dates.queued);
    const end = new Date(currentVideo.date_completed);
    currentVideo.total_days = Math.ceil((end - start) / (1000 * 60 * 60 * 24));
  }

  // Save
  saveVideo();

  // Refresh display
  displayProgress();
  displayStageActions();

  // If complete, show success message
  if (nextStage.key === 'complete') {
    alert('Video processing complete! 🎉');
    setTimeout(() => {
      window.location.href = 'video-library.html';
    }, 1000);
  }
}

function saveNotes() {
  currentVideo.notes = document.getElementById('notes').value;
  saveVideo();
  alert('Notes saved!');
}

function saveVideo() {
  const allVideos = JSON.parse(localStorage.getItem('videos') || '[]');
  const index = allVideos.findIndex(v => v.id === currentVideo.id);

  if (index >= 0) {
    allVideos[index] = currentVideo;
  }

  localStorage.setItem('videos', JSON.stringify(allVideos));
}
```

---

## STAGE-SPECIFIC ACTIONS

### Stage 1: QUEUED
- Just added to system
- **Action**: Select for processing

### Stage 2: SELECTED
- Chosen for transcription
- **Action**: Begin transcription

### Stage 3: TRANSCRIBING
- Getting transcript
- **Actions**:
  - Upload transcription file (.txt, .json)
  - Paste transcription text
  - Mark as transcribed

### Stage 4: ANALYZED
- Extract entities
- **Actions**:
  - Run PMT-004 prompt
  - Extract workflows, tools, actions
  - Mark as analyzed

### Stage 5: INTEGRATED
- Add to libraries
- **Actions**:
  - Create JSON files for entities
  - Integrate into libraries
  - Mark as integrated

### Stage 6: COMPLETE
- Fully processed
- **Actions**:
  - View in catalog
  - Generate report

---

## SUCCESS CRITERIA

You've completed Screen 5 when:

✅ Displays video with YouTube player
✅ Shows progress through all stages
✅ Visual indicators (✅ ⏳ ⏹) for each stage
✅ Stage-specific actions displayed
✅ Can upload/paste transcription
✅ Can move to next stage
✅ Cannot skip stages (validation)
✅ Records completion dates
✅ Can add/save notes
✅ Updates video status in data
✅ Redirects to library when complete

---

## NEXT STEP

**Go to Page 6: Screen 6 - Video Library Catalog**

Build the final catalog/library view showing all completed videos.
