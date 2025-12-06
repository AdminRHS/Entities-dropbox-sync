# PAGE 3: SCREEN 2 - Research Prompt & Execution

**Show the research prompt and let user mark progress**

---

## WHAT THIS SCREEN DOES

When user clicks a topic from Screen 1, show:
1. The research prompt to copy
2. Button to mark "In Progress"
3. Form to submit research results (list of video URLs)

---

## VISUAL LAYOUT

```
┌──────────────────────────────────────────────────────┐
│  ← Back to Topics                                    │
│                                                      │
│  Research Topic: AI Automation Tools 2024            │
│  Status: Not Started                                 │
│  ════════════════════════════════════════════════   │
│                                                      │
│  RESEARCH PROMPT                                     │
│  ┌─────────────────────────────────────────────────┐│
│  │ Search YouTube and Perplexity for:              ││
│  │                                                 ││
│  │ - Videos about AI automation published in last  ││
│  │   6 months                                      ││
│  │ - Minimum 10K views                             ││
│  │ - Focus on tutorial/how-to content              ││
│  │ - Look for tools: n8n, Make, Zapier, AI agents  ││
│  │                                                 ││
│  │ Find at least 15-20 videos and return:          ││
│  │ - Video URL                                     ││
│  │ - Title (optional - we can extract it)          ││
│  │ - View count (optional)                         ││
│  │                                                 ││
│  │ Copy this prompt and go research. Come back     ││
│  │ with video URLs to process.                     ││
│  └─────────────────────────────────────────────────┘│
│                                                      │
│  [📋 Copy Prompt]  [🏁 Mark In Progress]            │
│                                                      │
│  ────────────────────────────────────────────────   │
│                                                      │
│  SUBMIT RESEARCH RESULTS                             │
│  Paste video URLs (one per line):                   │
│  ┌─────────────────────────────────────────────────┐│
│  │ https://youtube.com/watch?v=ABC123              ││
│  │ https://youtu.be/DEF456                         ││
│  │ https://youtube.com/watch?v=GHI789              ││
│  │                                                 ││
│  └─────────────────────────────────────────────────┘│
│                                                      │
│  [Process Videos →]                                  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## DATA FLOW

### When Screen Loads:

```
1. Get topic ID from navigation (passed from Screen 1)
2. Load topic data
3. Display:
   - Topic name
   - Current status
   - Research prompt
   - Submit form (if needed)
```

### When User Clicks "Copy Prompt":

```
1. Copy prompt text to clipboard
2. Show "Copied!" message
```

### When User Clicks "Mark In Progress":

```
1. Update topic status to "In Progress"
2. Update assigned_to (could prompt for name)
3. Save to data
4. Update display
```

### When User Submits URLs:

```
1. Get textarea content
2. Split by newlines
3. For each line:
   - Extract YouTube video ID
   - Create video entry in queue
4. Count videos added
5. Update topic:
   - Status = "Complete"
   - Videos_found = count
6. Navigate to Screen 4 (Transcription Queue)
```

---

## EXTRACT VIDEO ID FROM URL

### YouTube URL Formats:

```
https://youtube.com/watch?v=ABC123DEF456
https://youtu.be/ABC123DEF456
https://www.youtube.com/watch?v=ABC123DEF456
https://m.youtube.com/watch?v=ABC123DEF456

All extract to: ABC123DEF456 (11 characters)
```

### Extraction Logic:

```
Patterns to match:
1. youtube.com/watch?v=VIDEO_ID
2. youtu.be/VIDEO_ID
3. youtube.com/embed/VIDEO_ID

Extract: The 11-character alphanumeric ID
```

---

## PSEUDOCODE

```
DATA (from previous screen):
  CURRENT_TOPIC = {
    id: "TOPIC-001",
    name: "AI Automation Tools 2024",
    prompt: "Search YouTube for...",
    status: "Not Started"
  }

FUNCTION load_screen():
  # Get topic ID from URL parameter or localStorage
  topic_id = get_parameter("topic_id")

  # Load topic data
  CURRENT_TOPIC = find_topic_by_id(topic_id)

  # Display
  show_topic_name(CURRENT_TOPIC.name)
  show_status(CURRENT_TOPIC.status)
  show_prompt(CURRENT_TOPIC.prompt)

  # Show/hide sections based on status
  if CURRENT_TOPIC.status == "Not Started":
    show_mark_in_progress_button()
    hide_submit_form()

  if CURRENT_TOPIC.status == "In Progress":
    hide_mark_in_progress_button()
    show_submit_form()

  if CURRENT_TOPIC.status == "Complete":
    hide_both()
    show_completion_message()

FUNCTION copy_prompt():
  navigator.clipboard.writeText(CURRENT_TOPIC.prompt)
  show_toast("Prompt copied to clipboard!")

FUNCTION mark_in_progress():
  # Optional: Ask for name
  name = prompt("Enter your name:")

  # Update topic
  CURRENT_TOPIC.status = "In Progress"
  CURRENT_TOPIC.assigned_to = name

  # Save
  save_topic(CURRENT_TOPIC)

  # Refresh display
  load_screen()

FUNCTION process_videos():
  # Get textarea content
  urls = document.getElementById("videoUrls").value

  # Split by lines
  url_list = urls.split("\n")

  # Process each URL
  videos_created = []

  for url in url_list:
    url = url.trim()

    if url == "":
      continue

    # Extract video ID
    video_id = extract_youtube_id(url)

    if video_id == null:
      continue

    # Create video entry
    video = create_video_entry(video_id, CURRENT_TOPIC.id)
    videos_created.push(video)

  # Update topic
  CURRENT_TOPIC.status = "Complete"
  CURRENT_TOPIC.videos_found = videos_created.length
  CURRENT_TOPIC.date_completed = today()

  # Save
  save_topic(CURRENT_TOPIC)
  save_videos(videos_created)

  # Navigate to queue
  navigate_to("transcription-queue.html")

FUNCTION extract_youtube_id(url):
  # Pattern 1: youtube.com/watch?v=VIDEO_ID
  if url contains "youtube.com/watch?v=":
    return extract_from_query_parameter(url, "v")

  # Pattern 2: youtu.be/VIDEO_ID
  if url contains "youtu.be/":
    return url.split("youtu.be/")[1].substring(0, 11)

  # Pattern 3: youtube.com/embed/VIDEO_ID
  if url contains "youtube.com/embed/":
    return url.split("/embed/")[1].substring(0, 11)

  return null

FUNCTION create_video_entry(video_id, topic_id):
  # Generate video entry ID
  next_id = get_next_video_number()

  return {
    id: "VIDEO-" + format_number(next_id, 3), // VIDEO-001
    video_id: video_id,
    youtube_url: "https://youtube.com/watch?v=" + video_id,
    topic_id: topic_id,
    status: "QUEUED",
    date_added: today(),
    selected: false
  }
```

---

## HTML STRUCTURE

```html
<div class="research-prompt-screen">
  <!-- Header -->
  <a href="topics.html" class="back-link">← Back to Topics</a>

  <h1 id="topicName">AI Automation Tools 2024</h1>
  <p class="status-badge" id="status">Not Started</p>

  <!-- Research Prompt Section -->
  <section class="prompt-section">
    <h2>Research Prompt</h2>
    <div class="prompt-box" id="promptBox">
      <!-- Prompt text loaded here -->
    </div>

    <button onclick="copyPrompt()" class="btn-copy">
      📋 Copy Prompt
    </button>

    <button onclick="markInProgress()" class="btn-start" id="btnStart">
      🏁 Mark In Progress
    </button>
  </section>

  <!-- Submit Results Section -->
  <section class="submit-section" id="submitSection" style="display: none;">
    <h2>Submit Research Results</h2>
    <p>Paste video URLs (one per line):</p>

    <textarea
      id="videoUrls"
      rows="10"
      placeholder="https://youtube.com/watch?v=ABC123&#10;https://youtu.be/DEF456&#10;https://youtube.com/watch?v=GHI789"
    ></textarea>

    <button onclick="processVideos()" class="btn-submit">
      Process Videos →
    </button>
  </section>

  <!-- Completion Message -->
  <section class="complete-section" id="completeSection" style="display: none;">
    <p>✓ Research complete! <span id="videoCount"></span> videos added to queue.</p>
    <a href="transcription-queue.html" class="btn-view-queue">View Queue →</a>
  </section>
</div>

<!-- Toast notification -->
<div id="toast" class="toast"></div>
```

---

## CSS STYLING

```css
.research-prompt-screen {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.back-link {
  color: #2196f3;
  text-decoration: none;
  margin-bottom: 20px;
  display: inline-block;
}

.status-badge {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 14px;
  background: #f5f5f5;
  color: #666;
}

.prompt-section {
  margin: 30px 0;
}

.prompt-box {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 15px 0;
  white-space: pre-wrap;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.6;
}

.btn-copy, .btn-start, .btn-submit {
  padding: 12px 24px;
  margin: 10px 10px 10px 0;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
}

.btn-copy {
  background: #2196f3;
  color: white;
}

.btn-start {
  background: #ff9800;
  color: white;
}

.btn-submit {
  background: #4caf50;
  color: white;
  width: 100%;
}

.submit-section textarea {
  width: 100%;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-family: monospace;
  font-size: 14px;
  margin: 10px 0;
}

.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #333;
  color: white;
  padding: 15px 25px;
  border-radius: 6px;
  display: none;
}

.toast.show {
  display: block;
  animation: fadeIn 0.3s, fadeOut 0.3s 2.7s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
```

---

## JAVASCRIPT

```javascript
let currentTopic = null;

// Load screen
window.onload = function() {
  // Get topic ID from localStorage (set by previous screen)
  const topicId = localStorage.getItem('selectedTopic');

  // Load topics
  const topics = JSON.parse(localStorage.getItem('topics') || '[]');

  // Find current topic
  currentTopic = topics.find(t => t.id === topicId);

  if (!currentTopic) {
    alert('Topic not found');
    window.location.href = 'topics.html';
    return;
  }

  // Display topic info
  document.getElementById('topicName').textContent = currentTopic.name;
  document.getElementById('status').textContent = currentTopic.status;
  document.getElementById('promptBox').textContent = currentTopic.prompt;

  // Show/hide sections based on status
  if (currentTopic.status === 'Not Started') {
    document.getElementById('btnStart').style.display = 'inline-block';
    document.getElementById('submitSection').style.display = 'none';
    document.getElementById('completeSection').style.display = 'none';
  } else if (currentTopic.status === 'In Progress') {
    document.getElementById('btnStart').style.display = 'none';
    document.getElementById('submitSection').style.display = 'block';
    document.getElementById('completeSection').style.display = 'none';
  } else if (currentTopic.status === 'Complete') {
    document.getElementById('btnStart').style.display = 'none';
    document.getElementById('submitSection').style.display = 'none';
    document.getElementById('completeSection').style.display = 'block';
    document.getElementById('videoCount').textContent = currentTopic.videos_found;
  }
};

// Copy prompt to clipboard
function copyPrompt() {
  navigator.clipboard.writeText(currentTopic.prompt).then(() => {
    showToast('Prompt copied to clipboard!');
  });
}

// Show toast notification
function showToast(message) {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

// Mark topic as in progress
function markInProgress() {
  const name = prompt('Enter your name:') || 'Unknown';

  currentTopic.status = 'In Progress';
  currentTopic.assigned_to = name;

  // Save
  const topics = JSON.parse(localStorage.getItem('topics') || '[]');
  const index = topics.findIndex(t => t.id === currentTopic.id);
  topics[index] = currentTopic;
  localStorage.setItem('topics', JSON.stringify(topics));

  // Reload
  window.location.reload();
}

// Process submitted video URLs
function processVideos() {
  const urlsText = document.getElementById('videoUrls').value;
  const urls = urlsText.split('\n').map(u => u.trim()).filter(u => u.length > 0);

  if (urls.length === 0) {
    alert('Please enter at least one video URL');
    return;
  }

  // Load existing videos
  const videos = JSON.parse(localStorage.getItem('videos') || '[]');

  // Process each URL
  let addedCount = 0;

  urls.forEach(url => {
    const videoId = extractYouTubeId(url);

    if (videoId) {
      // Check if already exists
      if (!videos.find(v => v.video_id === videoId)) {
        const nextNumber = videos.length + 1;
        const newVideo = {
          id: `VIDEO-${String(nextNumber).padStart(3, '0')}`,
          video_id: videoId,
          youtube_url: `https://youtube.com/watch?v=${videoId}`,
          topic_id: currentTopic.id,
          status: 'QUEUED',
          date_added: new Date().toISOString().split('T')[0],
          selected: false
        };

        videos.push(newVideo);
        addedCount++;
      }
    }
  });

  // Save videos
  localStorage.setItem('videos', JSON.stringify(videos));

  // Update topic
  currentTopic.status = 'Complete';
  currentTopic.videos_found = addedCount;
  currentTopic.date_completed = new Date().toISOString().split('T')[0];

  const topics = JSON.parse(localStorage.getItem('topics') || '[]');
  const index = topics.findIndex(t => t.id === currentTopic.id);
  topics[index] = currentTopic;
  localStorage.setItem('topics', JSON.stringify(topics));

  // Navigate to queue
  showToast(`${addedCount} videos added!`);
  setTimeout(() => {
    window.location.href = 'transcription-queue.html';
  }, 1500);
}

// Extract YouTube video ID from URL
function extractYouTubeId(url) {
  // Pattern 1: youtube.com/watch?v=VIDEO_ID
  let match = url.match(/youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})/);
  if (match) return match[1];

  // Pattern 2: youtu.be/VIDEO_ID
  match = url.match(/youtu\.be\/([a-zA-Z0-9_-]{11})/);
  if (match) return match[1];

  // Pattern 3: youtube.com/embed/VIDEO_ID
  match = url.match(/youtube\.com\/embed\/([a-zA-Z0-9_-]{11})/);
  if (match) return match[1];

  return null;
}
```

---

## SUCCESS CRITERIA

You've completed Screen 2 when:

✅ Shows topic name and current status
✅ Displays research prompt
✅ Can copy prompt to clipboard
✅ Can mark topic as "In Progress"
✅ Can submit video URLs (one per line)
✅ Extracts YouTube video IDs from URLs
✅ Creates video entries in data storage
✅ Updates topic status to "Complete"
✅ Navigates to transcription queue after submission

---

## NEXT STEP

**Go to Page 4: Screen 4 - Transcription Queue with YouTube Previews**

Build the screen that shows all queued videos with embedded YouTube iframes for preview.
