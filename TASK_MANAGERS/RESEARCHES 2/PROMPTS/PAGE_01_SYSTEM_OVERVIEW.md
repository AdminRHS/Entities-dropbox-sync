# PAGE 1: SYSTEM OVERVIEW - The Complete User Journey

**What we're building: A research video processing system with visual catalog**

---

## THE BIG PICTURE

A system with **2 major sections**:

### SECTION A: PROCESSING PIPELINE (Work Area)
Where videos move through stages until ready for catalog

### SECTION B: FINAL CATALOG (Library/Results)
Where finished videos are displayed with all details

---

## USER JOURNEY (Step-by-Step)

### SECTION A: PROCESSING PIPELINE

#### Screen 1: TOPICS FOR RESEARCH
**What**: List of research topics to investigate
**User sees**:
```
Research Topics
---------------
□ AI Automation Tools 2024
□ n8n Workflows for Beginners
□ OpenAI API Integration Examples
□ Video Editing with AI
+ Add New Topic
```

**User does**:
- Browse list of topics
- Choose a topic to research
- Click topic to see research prompt

---

#### Screen 2: RESEARCH PROMPT & EXECUTION
**What**: Show prompt for researching the chosen topic
**User sees**:
```
Topic: "AI Automation Tools 2024"

Research Prompt:
-----------------
Search YouTube and Perplexity for:
- Videos about AI automation published in last 6 months
- Minimum 10K views
- Focus on tutorial/how-to content
- Look for: n8n, Make, Zapier, AI agents

Please find at least 15-20 videos and return:
- Video URL
- Title
- Channel name
- View count
- Publication date

[Copy Prompt] [Mark as In Progress]
```

**User does**:
- Copies prompt
- Goes to YouTube/Perplexity
- Searches for videos
- Returns with raw data (URLs, titles, etc.)

---

#### Screen 3: RAW DATA ENTRY
**What**: Paste research results to create video listings
**User sees**:
```
Enter Research Results
----------------------

Paste video data here (one per line):
URL, Title, Channel, Views

[Paste Area]

Or add manually:
[+ Add Video URL]

[Process Data →]
```

**User does**:
- Pastes YouTube URLs or full data
- System extracts video IDs, titles, metadata
- Creates entries in TRANSCRIPTION QUEUE

---

#### Screen 4: TRANSCRIPTION QUEUE (with YouTube Previews)
**What**: List of videos ready to transcribe, WITH video previews
**User sees**:

```
Transcription Queue
-------------------

[YouTube Preview]    Video 027: "Build AI Agent with n8n"
                     Channel: AI Tutorials
                     11:30 duration
                     [Select for Transcription]

[YouTube Preview]    Video 028: "Automate Everything with OpenAI"
                     Channel: Tech Guide
                     15:45 duration
                     [Select for Transcription]

[YouTube Preview]    Video 029: "n8n Beginner Tutorial"
                     Channel: Workflow Master
                     8:20 duration
                     [Select for Transcription]
```

**YouTube Preview** = Embedded iframe showing video thumbnail/player

**User does**:
- Watches video previews
- Decides which videos to transcribe
- Selects videos to process

---

#### Screen 5: PROCESSING DETAILS
**What**: Single video detail page during processing
**User sees**:

```
Video 027: "Build AI Agent with n8n"
==========================================

[Full YouTube Player - Embedded]

Status: TRANSCRIBING
Progress:
  ✓ Queued (2025-12-01)
  ✓ Selected (2025-12-02)
  ⏳ Transcribing (in progress...)
  ⏹ Analyzed
  ⏹ Integrated
  ⏹ Complete

Actions:
[Upload Transcription File]
[Mark as Transcribed]
[Cancel]

Notes:
[Text area for notes]
```

**User does**:
- Monitors progress
- Uploads transcription when ready
- Moves to next stage

---

### SECTION B: FINAL CATALOG (The Library)

#### Screen 6: VIDEO LIBRARY (Catalog View)
**What**: Final catalog of ALL processed videos with details
**User sees**:

```
Video Library - 28 Completed Videos
====================================

Filters: [All Topics ▼] [All Channels ▼] [Sort by: Date ▼]

┌─────────────────────────────────────────────────────┐
│ [YouTube Thumbnail]  Video 027                      │
│                      "Build AI Agent with n8n"      │
│                                                     │
│ Channel: AI Tutorials                              │
│ Duration: 11:30 | Views: 125K | Date: 2024-11-15   │
│                                                     │
│ Tools Found: n8n, OpenAI, Make, Google Sheets      │
│ Workflows: 3 | Actions: 12 | Skills: 5             │
│                                                     │
│ [View Full Details] [Watch Video]                  │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ [YouTube Thumbnail]  Video 028                      │
│                      "Automate Everything..."        │
│ ...                                                 │
└─────────────────────────────────────────────────────┘

[Load More]
```

**User does**:
- Browse all completed videos
- Filter by channel, topic, tools
- Click to see full details

---

#### Screen 7: CHANNEL CATALOG
**What**: Browse by YouTube channels
**User sees**:

```
YouTube Channels
================

┌─────────────────────────────────────┐
│ [Channel Avatar] AI Tutorials        │
│                                     │
│ Videos processed: 8                 │
│ Total workflows extracted: 24       │
│ Total tools found: 45               │
│                                     │
│ Latest: "Build AI Agent with n8n"   │
│                                     │
│ [View All Videos from Channel]      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ [Channel Avatar] Tech Guide          │
│                                     │
│ Videos processed: 5                 │
│ ...                                 │
└─────────────────────────────────────┘
```

**User does**:
- Browse by favorite channels
- See which channels most productive
- Click channel to see all their videos

---

#### Screen 8: VIDEO DETAIL PAGE (Full Information)
**What**: Everything about one completed video
**User sees**:

```
Video 027: "Build AI Agent with n8n"
====================================

[Full YouTube Embedded Player]

Channel: AI Tutorials
Published: 2024-11-15
Duration: 11:30
Views: 125K | Likes: 3.2K

EXTRACTED ENTITIES
------------------

Workflows (3):
  • WRF-045: n8n + OpenAI Automation
  • WRF-046: Google Sheets Integration
  • WRF-047: Email Notification System

Tools (12):
  • n8n (Workflow Automation)
  • OpenAI API (AI Platform)
  • Google Sheets (Spreadsheet)
  • Gmail (Email)
  • Make (Alternative workflow tool)
  ... [show all]

Actions (12):
  • Create, Configure, Connect, Test, Deploy...

Skills Required (5):
  • API Integration
  • Workflow Design
  • Prompt Engineering
  ...

TRANSCRIPTION
-------------
[Expandable text with full transcription]

[Download as JSON] [Edit Entities] [Delete]
```

**User does**:
- Read full video details
- See what tools/workflows extracted
- Access transcription
- Export data

---

## THE TWO SECTIONS EXPLAINED

### SECTION A: PROCESSING PIPELINE (Screens 1-5)

**Purpose**: Move videos from research to completion

**Workflow**:
```
Topics → Research → Raw Data → Queue → Processing → Complete
```

**Key Features**:
- Task assignment (research topics)
- Data entry (paste URLs)
- YouTube previews (see videos before transcribing)
- Progress tracking (where is each video)
- Processing actions (transcribe, analyze, mark complete)

---

### SECTION B: FINAL CATALOG (Screens 6-8)

**Purpose**: Browse and explore completed videos

**What it shows**:
- Library of all videos (grid/list view)
- YouTube channel groupings
- Full video details
- Extracted entities (tools, workflows, etc.)
- Transcriptions
- Metadata

**Key Features**:
- Visual browsing (thumbnails, iframes)
- Filtering (by channel, topic, tools)
- Searching
- Detailed view (everything about one video)

---

## NAVIGATION FLOW

```
Main Menu
├── PROCESSING
│   ├── 1. Research Topics
│   ├── 2. Transcription Queue
│   └── 3. In Progress
│
└── LIBRARY
    ├── 4. Video Catalog
    ├── 5. Channels
    └── 6. Tools/Workflows (optional)
```

**User can switch between sections anytime**

---

## DATA THAT MOVES THROUGH SYSTEM

### Stage 1-3: Research Phase
```
Topic → Research URLs → Video Metadata
```

### Stage 4: Queue Phase
```
Video URL
Video ID (extracted from URL)
Title, Channel, Duration, Views (from YouTube API or manual)
Thumbnail URL
Status: QUEUED
```

### Stage 5: Processing Phase
```
All above +
Transcription file
Status: TRANSCRIBING → ANALYZED → INTEGRATED
```

### Stage 6-8: Library Phase
```
All above +
Extracted entities:
  - Workflows (with IDs)
  - Tools (with categories)
  - Actions, Skills, etc.
Status: COMPLETE
Display in catalog
```

---

## WHAT MAKES THIS DIFFERENT

### YouTube Integration
- **Preview videos** before processing (iframe embed)
- **Watch in catalog** (don't leave system)
- **Channel grouping** (see patterns by creator)
- **Thumbnail display** (visual browsing)

### Two-Mode System
- **Work mode** (Processing): Focus on getting videos through pipeline
- **Browse mode** (Library): Explore results, search, discover

### Progressive Detail
- **Queue view**: Just thumbnail + title (quick selection)
- **Catalog view**: Thumbnail + summary (browsing)
- **Detail view**: Everything (deep dive)

---

## NEXT STEPS

**Go to Page 2**: Build Screen 1 (Research Topics List)

We'll start building each screen step-by-step, beginning with the simplest: a list of research topics.
