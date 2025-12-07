# PAGE 2: SCREEN 1 - Research Topics List

**Build the first screen: List of research topics to investigate**

---

## WHAT THIS SCREEN DOES

Shows a list of research topics. User picks one to get a research prompt.

---

## VISUAL LAYOUT

```
┌──────────────────────────────────────────────────┐
│  Research Topics                                 │
│  ───────────────                                 │
│                                                  │
│  Select a topic to begin research:               │
│                                                  │
│  ┌─────────────────────────────────────────────┐│
│  │ □ AI Automation Tools 2024                  ││
│  │   Status: Not Started                       ││
│  │   [View Prompt]                             ││
│  └─────────────────────────────────────────────┘│
│                                                  │
│  ┌─────────────────────────────────────────────┐│
│  │ ✓ n8n Workflows for Beginners               ││
│  │   Status: Complete (15 videos found)        ││
│  │   [View Results]                            ││
│  └─────────────────────────────────────────────┘│
│                                                  │
│  ┌─────────────────────────────────────────────┐│
│  │ ⏳ OpenAI API Integration                   ││
│  │   Status: In Progress (Alice)               ││
│  │   [Continue Research]                       ││
│  └─────────────────────────────────────────────┘│
│                                                  │
│  [+ Add New Topic]                               │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## DATA FOR EACH TOPIC

### What to store:

```
Topic:
  - Topic ID (TOPIC-001, TOPIC-002, etc.)
  - Topic Name ("AI Automation Tools 2024")
  - Research Prompt (the text to copy)
  - Status (Not Started / In Progress / Complete)
  - Assigned To (person's name, optional)
  - Date Created
  - Date Completed (if complete)
  - Videos Found (count)
```

### Example:

```
TOPIC-001:
  Name: "AI Automation Tools 2024"
  Prompt: "Search YouTube for videos about..."
  Status: "Not Started"
  Assigned To: null
  Date Created: "2025-12-01"
  Date Completed: null
  Videos Found: 0
```

---

## USER INTERACTIONS

### 1. View Topic List
**What happens**: Load all topics from data, display as cards

```
Show topics in this order:
1. In Progress (top - active work)
2. Not Started (middle - ready to work)
3. Complete (bottom - archived)
```

### 2. Click Topic
**What happens**: Navigate to Screen 2 (Research Prompt page)

```
User clicks "AI Automation Tools 2024"
→ Go to research prompt screen
→ Show prompt for this topic
→ Give option to mark "In Progress"
```

### 3. Add New Topic
**What happens**: Show form to create new topic

```
Modal/Form appears:
┌─────────────────────────────────────┐
│ Add Research Topic                  │
│                                     │
│ Topic Name:                         │
│ [___________________________]       │
│                                     │
│ Research Prompt:                    │
│ [                                   ]│
│ [                                   ]│
│ [___________________________]       │
│                                     │
│ [Cancel]  [Create Topic]            │
└─────────────────────────────────────┘
```

**On "Create Topic"**:
- Generate new TOPIC-ID
- Save to data
- Add to list
- Close modal

---

## TOPIC STATUS INDICATORS

### Visual indicators:

```
□ Not Started
  - Gray checkbox
  - Gray text
  - "Not Started" label

⏳ In Progress
  - Yellow/orange indicator
  - Bold text
  - Person's name shown
  - "In Progress (Name)"

✓ Complete
  - Green checkmark
  - Normal text
  - Shows video count
  - "Complete (15 videos)"
```

---

## PSEUDOCODE

```
DATA:
  TOPICS = [
    {
      id: "TOPIC-001",
      name: "AI Automation Tools 2024",
      prompt: "Search YouTube for...",
      status: "Not Started",
      assigned_to: null,
      date_created: "2025-12-01",
      videos_found: 0
    },
    {
      id: "TOPIC-002",
      name: "n8n Workflows",
      prompt: "Find videos about...",
      status: "Complete",
      assigned_to: "Alice",
      date_created: "2025-11-25",
      date_completed: "2025-11-28",
      videos_found: 15
    }
  ]

FUNCTION display_topics():
  # Sort by status
  in_progress = filter TOPICS where status = "In Progress"
  not_started = filter TOPICS where status = "Not Started"
  complete = filter TOPICS where status = "Complete"

  # Display in order
  for topic in in_progress:
    render_topic_card(topic, "in-progress-style")

  for topic in not_started:
    render_topic_card(topic, "not-started-style")

  for topic in complete:
    render_topic_card(topic, "complete-style")

FUNCTION render_topic_card(topic, style):
  show card with:
    - Topic name (heading)
    - Status indicator (icon + text)
    - Button ("View Prompt" or "View Results")
    - Apply visual style

FUNCTION on_click_topic(topic_id):
  navigate to Screen 2 (Research Prompt)
  pass topic_id as parameter

FUNCTION on_add_new_topic():
  show modal with form:
    - Input: Topic Name
    - Textarea: Research Prompt
    - Buttons: Cancel, Create

FUNCTION on_create_topic(name, prompt):
  new_id = generate_next_id("TOPIC")

  new_topic = {
    id: new_id,
    name: name,
    prompt: prompt,
    status: "Not Started",
    assigned_to: null,
    date_created: today(),
    videos_found: 0
  }

  add new_topic to TOPICS
  save TOPICS
  close modal
  refresh display
```

---

## HTML STRUCTURE (Simple)

```html
<div class="topics-container">
  <h1>Research Topics</h1>
  <p>Select a topic to begin research:</p>

  <!-- In Progress Topics -->
  <div class="topic-card in-progress">
    <h3>OpenAI API Integration</h3>
    <p class="status">⏳ In Progress (Alice)</p>
    <button onclick="viewTopic('TOPIC-003')">Continue Research</button>
  </div>

  <!-- Not Started Topics -->
  <div class="topic-card not-started">
    <h3>AI Automation Tools 2024</h3>
    <p class="status">□ Not Started</p>
    <button onclick="viewTopic('TOPIC-001')">View Prompt</button>
  </div>

  <!-- Complete Topics -->
  <div class="topic-card complete">
    <h3>n8n Workflows for Beginners</h3>
    <p class="status">✓ Complete (15 videos found)</p>
    <button onclick="viewTopic('TOPIC-002')">View Results</button>
  </div>

  <!-- Add New Button -->
  <button class="add-topic-btn" onclick="showAddModal()">
    + Add New Topic
  </button>
</div>

<!-- Modal (hidden by default) -->
<div id="addTopicModal" class="modal" style="display: none;">
  <div class="modal-content">
    <h2>Add Research Topic</h2>

    <label>Topic Name:</label>
    <input type="text" id="topicName">

    <label>Research Prompt:</label>
    <textarea id="topicPrompt" rows="10"></textarea>

    <button onclick="createTopic()">Create Topic</button>
    <button onclick="closeModal()">Cancel</button>
  </div>
</div>
```

---

## CSS STYLING (Simple)

```css
.topics-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.topic-card {
  border: 1px solid #ddd;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
}

.topic-card.in-progress {
  border-left: 4px solid orange;
  background: #fff8e1;
}

.topic-card.not-started {
  border-left: 4px solid gray;
  background: #f5f5f5;
}

.topic-card.complete {
  border-left: 4px solid green;
  background: #e8f5e9;
}

.status {
  color: #666;
  font-size: 14px;
  margin: 10px 0;
}

.add-topic-btn {
  width: 100%;
  padding: 15px;
  background: #2196f3;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 500px;
}
```

---

## JAVASCRIPT (Simple)

```javascript
// Data storage (simplified - use localStorage or backend)
let topics = [
  {
    id: "TOPIC-001",
    name: "AI Automation Tools 2024",
    prompt: "Search YouTube and Perplexity for videos about AI automation...",
    status: "Not Started",
    assigned_to: null,
    date_created: "2025-12-01",
    videos_found: 0
  }
];

// Display topics
function displayTopics() {
  const container = document.querySelector('.topics-container');

  // Sort by status
  const inProgress = topics.filter(t => t.status === "In Progress");
  const notStarted = topics.filter(t => t.status === "Not Started");
  const complete = topics.filter(t => t.status === "Complete");

  // Clear existing cards (keep header and add button)
  const cards = container.querySelectorAll('.topic-card');
  cards.forEach(card => card.remove());

  // Render in order
  [...inProgress, ...notStarted, ...complete].forEach(topic => {
    renderTopicCard(topic);
  });
}

// Render single topic card
function renderTopicCard(topic) {
  const container = document.querySelector('.topics-container');
  const addButton = document.querySelector('.add-topic-btn');

  const card = document.createElement('div');
  card.className = `topic-card ${topic.status.toLowerCase().replace(' ', '-')}`;

  let statusIcon = '□';
  let buttonText = 'View Prompt';

  if (topic.status === 'In Progress') {
    statusIcon = '⏳';
    buttonText = 'Continue Research';
  } else if (topic.status === 'Complete') {
    statusIcon = '✓';
    buttonText = 'View Results';
  }

  card.innerHTML = `
    <h3>${topic.name}</h3>
    <p class="status">${statusIcon} ${topic.status}${topic.assigned_to ? ' (' + topic.assigned_to + ')' : ''}${topic.videos_found > 0 ? ' - ' + topic.videos_found + ' videos' : ''}</p>
    <button onclick="viewTopic('${topic.id}')">${buttonText}</button>
  `;

  container.insertBefore(card, addButton);
}

// Navigate to topic detail
function viewTopic(topicId) {
  // Store selected topic
  localStorage.setItem('selectedTopic', topicId);

  // Navigate to Screen 2
  window.location.href = 'research-prompt.html';
}

// Show add modal
function showAddModal() {
  document.getElementById('addTopicModal').style.display = 'flex';
}

// Close modal
function closeModal() {
  document.getElementById('addTopicModal').style.display = 'none';
  document.getElementById('topicName').value = '';
  document.getElementById('topicPrompt').value = '';
}

// Create new topic
function createTopic() {
  const name = document.getElementById('topicName').value;
  const prompt = document.getElementById('topicPrompt').value;

  if (!name || !prompt) {
    alert('Please fill in all fields');
    return;
  }

  // Generate ID
  const maxId = Math.max(...topics.map(t => parseInt(t.id.split('-')[1])), 0);
  const newId = `TOPIC-${String(maxId + 1).padStart(3, '0')}`;

  // Create topic
  const newTopic = {
    id: newId,
    name: name,
    prompt: prompt,
    status: 'Not Started',
    assigned_to: null,
    date_created: new Date().toISOString().split('T')[0],
    videos_found: 0
  };

  topics.push(newTopic);

  // Save (use localStorage for now)
  localStorage.setItem('topics', JSON.stringify(topics));

  closeModal();
  displayTopics();
}

// Load on page load
window.onload = function() {
  // Load from localStorage
  const saved = localStorage.getItem('topics');
  if (saved) {
    topics = JSON.parse(saved);
  }

  displayTopics();
};
```

---

## WHAT YOU NEED TO BUILD

### Minimum Version:

1. **Display Topics**
   - Load list of topics
   - Show as cards
   - Color code by status

2. **Click Topic**
   - Navigate to next screen
   - Pass topic ID

3. **Add New Topic**
   - Show modal/form
   - Create topic with ID
   - Save and refresh

### Data Storage Options:

**Option 1: localStorage** (simplest for now)
```javascript
localStorage.setItem('topics', JSON.stringify(topics));
const topics = JSON.parse(localStorage.getItem('topics'));
```

**Option 2: JSON file** (better for persistence)
```javascript
// Read from topics.json
// Write updates back to file
```

**Option 3: Backend** (best for multi-user)
```javascript
// API calls to server
// Server manages database
```

**Start with Option 1 (localStorage) for simplicity**

---

## SUCCESS CRITERIA

You've completed Screen 1 when:

✅ List of topics displays correctly
✅ Topics color-coded by status (gray/orange/green)
✅ Can click topic to navigate to next screen
✅ Can add new topic via modal
✅ New topics get unique IDs (TOPIC-001, etc.)
✅ Data persists (localStorage or file)

---

## NEXT STEP

**Go to Page 3: Screen 2 - Research Prompt**

Build the screen that shows the research prompt when user clicks a topic.
