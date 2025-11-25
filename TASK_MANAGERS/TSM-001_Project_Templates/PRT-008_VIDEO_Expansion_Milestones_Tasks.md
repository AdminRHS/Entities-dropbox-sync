# PRT-008 VIDEO Workflow - Expanded Milestones & Tasks

**Project:** PRT-008 (VIDEO Production)
**Version:** 2.0 - Expanded Structure
**Date:** 2025-11-21

---

## Milestone Structure

### **MLT-006: Research Complete - Videos Selected** (EXISTING - Enhanced)
**Phase:** 1 - Video Discovery & Research
**Department:** AI, Cross-functional
**Can Run Parallel:** false
**Dependencies:** []

**Task Templates:**
- **TST-050A**: Research Videos with Perplexity AI
- **TST-050B**: Research Videos with Gemini Deep Research (NEW)
- **TST-050C**: Research Videos with ChatGPT Search (NEW)
- **TST-050D**: Research Videos with Grok (NEW)
- **TST-050E**: Hybrid Multi-AI Research (NEW)
- **TST-051A**: Manual Video Review Checklist (Enhanced)
- **TST-051B**: Export to Video Processing Queue (NEW)

**Expected Deliverables:**
- Research results with 8-12 scored videos
- Complete video metadata (channel, URL, engagement metrics)
- Links from video descriptions
- Video processing queue JSON file
- Top 3-5 videos selected for transcription

---

### **MLT-007: Processing Complete - Taxonomy Extracted** (EXISTING - Enhanced)
**Phase:** 2 - Video Transcription & Taxonomy Extraction
**Department:** Cross-functional
**Can Run Parallel:** true (multiple videos simultaneously)
**Dependencies:** [MLT-006]

**Task Templates:**
- **TST-057A**: Auto-Select Transcription Method (NEW)
- **TST-057B**: Transcribe with Google AI Studio (EXISTING)
- **TST-057C**: Transcribe with TurboScribe (NEW)
- **TST-057D**: Transcribe with Local Whisper (NEW)
- **TST-057E**: Transcription Quality Check (NEW)
- **TST-057F**: Capture Complete Video Metadata (NEW)
- **TST-052**: Extract Taxonomy Data (EXISTING)
- **TST-053**: Validate Taxonomy (EXISTING)
- **TST-054**: Validate Tools (EXISTING)

**Expected Deliverables:**
- Word-for-word video transcriptions (.md format)
- Complete metadata JSON files
- Extracted workflows, tasks, steps, skills, tools
- Validated taxonomy documents

---

### **MLT-008: Library Population Complete** (EXISTING)
**Phase:** 3 - Library Population & Integration
**Department:** AI, Cross-functional
**Can Run Parallel:** false
**Dependencies:** [MLT-007]

**Task Templates:**
- **TST-055**: Update Mappings (EXISTING)
- **TST-056**: Gap Analysis (EXISTING)
- **TST-058**: Create/Update Tool Entries (EXISTING)
- **TST-059A**: Initialize Video Processing Queue (NEW)
- **TST-059B**: Add Video to Processing Queue (NEW)
- **TST-059C**: Process Video from Queue (NEW)
- **TST-059D**: Batch Process Queue (NEW)

**Expected Deliverables:**
- Updated LIBRARIES/Tools/ with new/enriched tools
- Updated tool_mapping.json
- Task-to-tool and skill-to-tool linkages
- Gap analysis reports
- Processing queue with status tracking

---

## Task Template Details

### **STAGE 1A: Multi-Platform Research**

#### **TST-050A: Research Videos with Perplexity AI** (EXISTING - Enhanced)
- **Action:** Research
- **Object:** Videos
- **Context:** Using Perplexity AI with 0-100 scoring
- **Department:** AI
- **Complexity:** Medium
- **Milestone:** MLT-006
- **Prerequisites:**
  - Strategic priorities reviewed
  - Department needs collected
  - Perplexity AI account
- **Outputs:**
  - 8-12 videos with complete metadata
  - Structured markdown with video cards
  - Channel information, URLs, engagement metrics
  - Links from descriptions captured
- **Enhanced Features:**
  - Standardized output format
  - Channel URL capture
  - Engagement metrics (likes, views, comments)
  - Export to JSON for queue system

#### **TST-050B: Research Videos with Gemini Deep Research** (NEW)
- **Action:** Research
- **Object:** Videos
- **Context:** Using Gemini 2.0 Flash Thinking for deep analysis
- **Department:** AI
- **Complexity:** High
- **Milestone:** MLT-006
- **Best For:** Complex topics requiring multi-source synthesis
- **Outputs:**
  - Deep research report with 10-15 video recommendations
  - Comparative analysis matrix
  - Multi-source citations
  - Best-in-class tutorial identification

#### **TST-050C: Research Videos with ChatGPT Search** (NEW)
- **Action:** Research
- **Object:** Videos
- **Context:** Using ChatGPT Plus with real-time web search
- **Department:** AI
- **Complexity:** Medium
- **Milestone:** MLT-006
- **Best For:** Recent videos (last 7-30 days), trending topics
- **Outputs:**
  - Real-time search results
  - Conversation-based refinement
  - Markdown or JSON export

#### **TST-050D: Research Videos with Grok** (NEW)
- **Action:** Research
- **Object:** Videos
- **Context:** Using Grok (X.AI) with X (Twitter) integration
- **Department:** AI
- **Complexity:** Medium
- **Milestone:** MLT-006
- **Best For:** Tech news, developer community trends, viral content
- **Outputs:**
  - Trending videos in dev community
  - Social proof from X conversations
  - Developer reactions and quotes

#### **TST-050E: Hybrid Multi-AI Research** (NEW)
- **Action:** Research
- **Object:** Videos
- **Context:** Cross-validation across Perplexity + Gemini + ChatGPT
- **Department:** AI
- **Complexity:** High
- **Milestone:** MLT-006
- **Best For:** Critical decisions, large projects
- **Outputs:**
  - Consensus picks (all 3 AI platforms recommend)
  - Confidence scoring based on agreement
  - Unique finds from each platform
  - Consolidated research report

---

### **STAGE 1B: Video Selection & Queue Export**

#### **TST-051A: Manual Video Review Checklist** (EXISTING - Enhanced)
- **Action:** Review
- **Object:** Videos
- **Context:** Using enhanced criteria and metadata capture
- **Department:** Cross-functional
- **Complexity:** Low
- **Milestone:** MLT-006
- **Enhanced Criteria:**
  - Duration: 5-60 minutes (expanded range)
  - Published: Last 60 days (configurable)
  - Channel verified status
  - Engagement metrics analysis
  - Like ratio >90%
  - Comment quality assessment
- **Metadata Capture:**
  - Channel name + URL
  - Video URL
  - Views, likes, comments
  - Links from description
  - Video description text
  - Hashtags and tags
- **Outputs:**
  - Complete video metadata JSON
  - Manual review scores
  - Priority assignments

#### **TST-051B: Export to Video Processing Queue** (NEW)
- **Action:** Export
- **Object:** Video Metadata
- **Context:** To processing queue JSON format
- **Department:** AI
- **Complexity:** Low
- **Milestone:** MLT-006
- **Outputs:**
  - Queue JSON file with all selected videos
  - Auto-assigned video IDs (VIDEO_001, VIDEO_002...)
  - Processing status initialized to "queued"
  - Transcription method auto-selected

---

### **STAGE 2A: Intelligent Transcription Routing**

#### **TST-057A: Auto-Select Transcription Method** (NEW)
- **Action:** Select
- **Object:** Transcription Method
- **Context:** Based on video duration and file size
- **Department:** AI
- **Complexity:** Low (automated)
- **Milestone:** MLT-007
- **Decision Logic:**
  - ≤ 40 minutes AND ≤ 100MB → Google AI Studio
  - > 40 minutes OR > 100MB → TurboScribe
  - Poor audio quality → TurboScribe
  - Need speaker labels → TurboScribe
- **Outputs:**
  - Selected transcription method
  - Updated queue JSON with method assignment

#### **TST-057B: Transcribe with Google AI Studio** (EXISTING)
- **Action:** Transcribe
- **Object:** Video
- **Context:** Using Google AI Studio
- **Department:** Cross-functional
- **Complexity:** Medium
- **Milestone:** MLT-007
- **Best For:** Videos ≤ 40 minutes, ≤ 100MB
- **Outputs:**
  - Word-for-word transcription with timestamps
  - Markdown format (.md)
  - Metadata section completed

#### **TST-057C: Transcribe with TurboScribe** (NEW)
- **Action:** Transcribe
- **Object:** Video
- **Context:** Using TurboScribe for long videos
- **Department:** Cross-functional
- **Complexity:** Medium
- **Milestone:** MLT-007
- **Best For:** Videos > 40 minutes, large files, poor audio
- **Features:**
  - Speaker labels (auto-detect)
  - Precise timestamps (per word)
  - Multiple export formats (SRT, TXT)
  - Better handling of accents/noise
- **Outputs:**
  - SRT file with timestamps
  - Converted to markdown format
  - Speaker-labeled transcription

#### **TST-057D: Transcribe with Local Whisper** (NEW)
- **Action:** Transcribe
- **Object:** Video
- **Context:** Using OpenAI Whisper locally
- **Department:** Cross-functional
- **Complexity:** High
- **Milestone:** MLT-007
- **Best For:** Privacy-sensitive content, offline processing
- **Features:**
  - Fully local (no cloud)
  - State-of-the-art accuracy
  - Multiple model sizes
  - Timestamp support
- **Outputs:**
  - SRT file with timestamps
  - Converted to markdown format

#### **TST-057E: Transcription Quality Check** (NEW)
- **Action:** Validate
- **Object:** Transcription
- **Context:** Quality verification before extraction
- **Department:** Cross-functional
- **Complexity:** Low
- **Milestone:** MLT-007
- **Quality Checklist:**
  - No large gaps in transcription
  - Technical terms spelled correctly
  - Code snippets captured accurately
  - Timestamps align with video
  - Speaker labels accurate (if applicable)
  - Links from description included
  - On-screen text captured
- **Outputs:**
  - Quality validation report
  - Pass/Fail status
  - List of corrections needed (if any)

#### **TST-057F: Capture Complete Video Metadata** (NEW)
- **Action:** Capture
- **Object:** Video Metadata
- **Context:** Complete data capture before transcription
- **Department:** Cross-functional
- **Complexity:** Low
- **Milestone:** MLT-007
- **Metadata Captured:**
  - Video title, channel name, channel URL
  - Video URL (full and short forms)
  - Published date and timestamp
  - Duration (formatted and seconds)
  - Views, likes, comments, like ratio
  - Full description text
  - All links from description
  - Hashtags and video tags
  - On-screen tools/logos shown
  - Social media handles mentioned
- **Outputs:**
  - Complete metadata JSON file
  - Saved in ENTITIES/REPORTS/Videos/Metadata/

---

### **STAGE 3: Queue Management & Automation**

#### **TST-059A: Initialize Video Processing Queue** (NEW)
- **Action:** Initialize
- **Object:** Processing Queue
- **Context:** Set up queue system for batch processing
- **Department:** AI
- **Complexity:** Low
- **Milestone:** MLT-008
- **Outputs:**
  - Queue JSON file (QUEUE_YYYY-MM-DD.json)
  - Directory structure created
  - Statistics initialized (queued, in_progress, completed, failed)

#### **TST-059B: Add Video to Processing Queue** (NEW)
- **Action:** Add
- **Object:** Video
- **Context:** To processing queue (manual or automated)
- **Department:** AI
- **Complexity:** Low
- **Milestone:** MLT-008
- **Automated Features:**
  - Auto-assign video ID
  - Auto-parse duration to seconds
  - Auto-select transcription method
  - Set processing status to "queued"
- **Outputs:**
  - Updated queue JSON
  - Video added with complete metadata

#### **TST-059C: Process Video from Queue** (NEW)
- **Action:** Process
- **Object:** Video
- **Context:** From queue with automated routing
- **Department:** AI
- **Complexity:** Medium
- **Milestone:** MLT-008
- **Processing Steps:**
  - Find next queued video (by priority)
  - Update status to "in_progress"
  - Save metadata JSON file
  - Show transcription instructions
  - Wait for manual completion
- **Outputs:**
  - Processing instructions displayed
  - Status updated in queue
  - Ready for transcription

#### **TST-059D: Batch Process Queue** (NEW)
- **Action:** Process
- **Object:** Video Queue
- **Context:** Batch processing multiple videos
- **Department:** AI
- **Complexity:** Medium
- **Milestone:** MLT-008
- **Features:**
  - Process multiple videos sequentially
  - Configurable max videos limit
  - Error handling (mark as failed, continue)
  - Status tracking
- **Outputs:**
  - Batch processing report
  - All queued videos processed
  - Statistics updated

---

## Workflow Diagram (Enhanced)

```
┌─────────────────────────────────────────────────────────────────┐
│ STAGE 1: MULTI-PLATFORM RESEARCH                                │
│ Milestone: MLT-006 (Research Complete)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ TST-050A     │  │ TST-050B     │  │ TST-050C     │         │
│  │ Perplexity   │  │ Gemini Deep  │  │ ChatGPT      │  ← Choose one or more
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐                           │
│  │ TST-050D     │  │ TST-050E     │                           │
│  │ Grok         │  │ Hybrid       │                           │
│  └──────────────┘  └──────────────┘                           │
│                          │                                      │
│                          ↓                                      │
│                ┌──────────────────┐                            │
│                │ TST-051A         │                            │
│                │ Manual Review    │                            │
│                │ + Metadata       │                            │
│                └──────────────────┘                            │
│                          │                                      │
│                          ↓                                      │
│                ┌──────────────────┐                            │
│                │ TST-051B         │                            │
│                │ Export to Queue  │                            │
│                └──────────────────┘                            │
│                                                                  │
│  Output: Queue JSON with 3-5 videos, complete metadata         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STAGE 2: INTELLIGENT TRANSCRIPTION                              │
│ Milestone: MLT-007 (Processing Complete)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────┐                                │
│  │ TST-057A                   │                                │
│  │ Auto-Select Method         │ ← 40 min threshold              │
│  │ (≤40min → Google, >40min → TurboScribe)                    │
│  └────────────────────────────┘                                │
│               │                                                  │
│               ├───────────────┬───────────────┬─────────────┐  │
│               ↓               ↓               ↓             ↓  │
│     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │  │
│     │ TST-057B     │ │ TST-057C     │ │ TST-057D     │   │  │
│     │ Google AI    │ │ TurboScribe  │ │ Local        │   │  │
│     │ Studio       │ │              │ │ Whisper      │   │  │
│     └──────────────┘ └──────────────┘ └──────────────┘   │  │
│               │               │               │             │  │
│               └───────────────┴───────────────┴─────────────┘  │
│                               │                                 │
│                               ↓                                 │
│                    ┌──────────────────┐                        │
│                    │ TST-057E         │                        │
│                    │ Quality Check    │                        │
│                    └──────────────────┘                        │
│                               │                                 │
│                               ↓                                 │
│                    ┌──────────────────┐                        │
│                    │ TST-057F         │                        │
│                    │ Capture Metadata │                        │
│                    └──────────────────┘                        │
│                               │                                 │
│                               ↓                                 │
│                    ┌──────────────────┐                        │
│                    │ TST-052          │                        │
│                    │ Extract Taxonomy │                        │
│                    └──────────────────┘                        │
│                               │                                 │
│                               ↓                                 │
│                    ┌──────────────────┐                        │
│                    │ TST-053          │                        │
│                    │ Validate         │                        │
│                    └──────────────────┘                        │
│                                                                  │
│  Output: Transcripts + Extracted taxonomy + Metadata           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STAGE 3: QUEUE MANAGEMENT & LIBRARY POPULATION                  │
│ Milestone: MLT-008 (Library Population Complete)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐                                           │
│  │ TST-059A         │                                           │
│  │ Initialize Queue │                                           │
│  └──────────────────┘                                           │
│           │                                                      │
│           ↓                                                      │
│  ┌──────────────────┐                                           │
│  │ TST-059B         │                                           │
│  │ Add to Queue     │ ← Repeatable for multiple videos          │
│  └──────────────────┘                                           │
│           │                                                      │
│           ↓                                                      │
│  ┌──────────────────┐     ┌──────────────────┐                │
│  │ TST-059C         │  or │ TST-059D         │                │
│  │ Process Single   │     │ Batch Process    │                │
│  └──────────────────┘     └──────────────────┘                │
│           │                         │                            │
│           └─────────────┬───────────┘                           │
│                         ↓                                        │
│              ┌──────────────────┐                               │
│              │ TST-054          │                               │
│              │ Validate Tools   │                               │
│              └──────────────────┘                               │
│                         │                                        │
│                         ↓                                        │
│              ┌──────────────────┐                               │
│              │ TST-058          │                               │
│              │ Update Tools     │                               │
│              └──────────────────┘                               │
│                         │                                        │
│                         ↓                                        │
│              ┌──────────────────┐                               │
│              │ TST-055          │                               │
│              │ Update Mappings  │                               │
│              └──────────────────┘                               │
│                         │                                        │
│                         ↓                                        │
│              ┌──────────────────┐                               │
│              │ TST-056          │                               │
│              │ Gap Analysis     │                               │
│              └──────────────────┘                               │
│                                                                  │
│  Output: Updated LIBRARIES + Mappings + Gap analysis            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Task Template Summary

### **Existing Tasks (8)**
- TST-050: Search and Score Videos (now TST-050A)
- TST-051: Select Videos (now TST-051A)
- TST-052: Extract Taxonomy
- TST-053: Validate Taxonomy
- TST-054: Validate Tools
- TST-055: Update Mappings
- TST-056: Gap Analysis
- TST-057: Transcribe Video (now TST-057B)
- TST-058: Create/Update Tool Entries

### **New Tasks (13)**
- TST-050B: Research with Gemini Deep Research
- TST-050C: Research with ChatGPT Search
- TST-050D: Research with Grok
- TST-050E: Hybrid Multi-AI Research
- TST-051B: Export to Queue
- TST-057A: Auto-Select Transcription Method
- TST-057C: Transcribe with TurboScribe
- TST-057D: Transcribe with Local Whisper
- TST-057E: Transcription Quality Check
- TST-057F: Capture Complete Metadata
- TST-059A: Initialize Queue
- TST-059B: Add to Queue
- TST-059C: Process from Queue
- TST-059D: Batch Process Queue

### **Total Tasks: 22**

---

**Status:** Ready for Implementation
**Next Step:** Create individual task template JSON files for new tasks

---

**End of Document**
