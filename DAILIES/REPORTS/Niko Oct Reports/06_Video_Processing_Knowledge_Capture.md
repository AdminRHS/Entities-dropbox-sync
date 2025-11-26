# Video Processing & Knowledge Capture
## Remote Helpers AI-First Organization - Week 2-3 (Nov 8-20, 2025)

**Document Version:** 1.0
**Generated:** 2025-11-20
**Total Lines:** ~400

**Source Files:**
- Video Instructions Transcribations.md (Processing workflows)
- 121125_structured_v2.md (Video pipeline, AI Studio)
- 171125_Niko.md (Token management, video parsing)
- 191225_Niko.md (YouTube research, tutorial extraction)
- MAIN_PROMPT_v5_Modular (Video transcription instructions)

**Related LIBRARIES:**
- **Actions:** Transcribe, Parse, Extract, Process, Analyze, Generate
- **Objects:** Video, Transcript, Milestone, Task, Tutorial
- **Tools:** AI Studio, Whisper Flow, Loom, YouTube
- **Processes:** Video transcription, Content parsing, Knowledge extraction

---

## Executive Summary

Video processing emerged as a critical knowledge capture mechanism during Week 2-3. The system transforms video content (meetings, tutorials, training) into structured TASK_MANAGERS entities using AI-powered transcription and extraction pipelines.

**Core Achievements:**
- AI Studio transcription workflow
- Token exhaustion management
- Milestone-based extraction methodology
- YouTube tutorial parsing system
- Overnight batch processing

---

## 1. Video Processing Pipeline

### 1.1 End-to-End Flow

```
Video Source
  ↓ Upload to AI Studio / Whisper Flow
  ↓ Transcription (auto/manual)
  ↓ Cleanup & formatting
  ↓ Entity extraction (MAIN_PROMPT v6)
  ↓ Milestone → Task → Step creation
  ↓ Storage in TASK_MANAGERS
  ↓ Integration with LIBRARIES
```

### 1.2 Supported Formats

**Meeting Recordings:**
- Google Meet exports
- Discord recordings
- Loom captures
- Zoom recordings

**Tutorial Content:**
- YouTube tutorials
- Internal training videos
- Screen recordings
- Webinars

### 1.3 Output Destinations

- **TASK_MANAGERS/Milestone_Templates/** - Clustered workflows
- **TASK_MANAGERS/Task_Templates/** - Individual tasks
- **TASK_MANAGERS/Step_Templates/** - Atomic actions
- **LIBRARIES/** - Referenced entities (Actions, Tools, etc.)

---

## 2. AI Studio Workflow

### 2.1 Setup

**Location:** `ENTITIES/PROMPTS/PROMPTS/Transcription/`
**File:** `Video_Transcription_Custom_Instructions.md`

**Configuration:**
1. Upload video to Google AI Studio
2. Load custom instructions
3. Set output format
4. Run transcription
5. Export results

### 2.2 Custom Instructions Purpose

**What they define:**
- Entity types to extract (MLS, TSK, STP)
- ID format conventions
- Probability mapping for Action→Object
- Output structure
- Cross-reference requirements

### 2.3 Token Management

**Problem:** Large videos exhaust tokens quickly

**Solutions:**
1. Split into segments (10-15 min chunks)
2. Rotate between AI models
3. Overnight batch processing
4. Prioritize high-value content

---

## 3. Milestone-Based Extraction

### 3.1 Extraction Sequence

**Critical Order:**
1. **Tag Action Words** → Identify ACT-### verbs
2. **Mark Objects** → What OBJ-### follow actions
3. **Search for Tools** → What TOL-### are used
4. **Link Responsibilities** → Match to RSP-###
5. **Identify Skills** → What SKL-### required
6. **Cluster into Tasks** → Group related steps
7. **Form Milestones** → Cluster related tasks

### 3.2 Action→Object→Tool Probability

**For each action, map probable objects and tools:**

```yaml
ACTION: ACT-201 (Upload)
PROBABLE_OBJECTS:
  - OBJ-120 (Course Cover) - Probability: High
  - OBJ-045 (Design Asset) - Probability: High
PROBABLE_TOOLS:
  - TOL-089 (Admin Panel) - For: ACT-201 + OBJ-120
MATCHED_RESPONSIBILITY: RSP-045 ("Upload design assets")
REQUIRED_SKILLS: SKL-001 (File management)
```

### 3.3 Hierarchical Output

```
MLS-001 (Video Content Production)
├── TSK-001 (Record Tutorial)
│   ├── STP-001 (Prepare outline) - ACT-015
│   ├── STP-002 (Set up recording) - ACT-020 + TOL-044
│   └── STP-003 (Record content) - ACT-030
├── TSK-002 (Process Recording)
│   ├── STP-004 (Upload to AI Studio) - ACT-201
│   └── STP-005 (Run transcription) - ACT-025
├── RSP-085 ("Create video tutorials")
└── PRF-005 (Video Producer)
```

---

## 4. YouTube Tutorial Parsing

### 4.1 Research Workflow

**Goal:** Extract knowledge from latest tutorials

**Process:**
1. Search YouTube for topic (last 2 weeks)
2. Select relevant videos
3. Download/transcribe
4. Extract to TASK_MANAGERS
5. Link to LIBRARIES

### 4.2 Tutorial Selection Criteria

**High Priority:**
- Published within 2 weeks
- From trusted channels
- Relevant to current projects
- Step-by-step format

**Example Topics:**
- Claude Code tutorials
- MCP setup guides
- n8n automation workflows
- VS Code extensions

### 4.3 Content to Task Template

**Example Extraction:**

**Video:** "Claude Skills Tutorial" (15 min)

**Output:**
```yaml
Task Template: TSK-011
Name: Install Claude Skills MCP
Steps:
  - STP-001: Download MCP connector
  - STP-002: Configure settings
  - STP-003: Add API keys
  - STP-004: Test connection
Tools: Claude Code, VS Code
Skills: MCP configuration
```

---

## 5. Overnight Processing

### 5.1 Batch Processing Strategy

**Why Overnight:**
- Token limits reset
- No interruptions
- Large file processing
- Multiple videos queued

**Setup:**
1. Queue videos before end of day
2. Set processing order
3. Configure output locations
4. Review results next morning

### 5.2 Case Study (Nov 12)

**Scenario:** 3-hour training recording needed processing

**Approach:**
1. Split into 12 × 15-minute segments
2. Queue all segments
3. Run overnight
4. Consolidated output: 1 Milestone, 8 Tasks, 47 Steps

### 5.3 Token Exhaustion Tracking

**Monitor:**
- Tokens used per video
- Remaining daily quota
- Model rotation schedule
- Cost per video

---

## 6. Video Index System

### 6.1 Catalog Structure

**Location:** `ENTITIES/ASSETS/Video_Index/`

**Contains:**
- Video ID
- Title
- Duration
- Source (YouTube/Loom/Meet)
- Date processed
- Output location
- Entities extracted

### 6.2 Search & Retrieval

**Find videos by:**
- Topic/keyword
- Date range
- Source platform
- Department
- Extracted entities

### 6.3 Loom Data Export

**Project:** Export Loom library data

**Data Needed:**
- Titles
- Transcriptions
- Dates
- URLs

**Purpose:** Build searchable video knowledge base

---

## 7. Meeting Recording Best Practices

### 7.1 Recording Requirements

**Always Record:**
- Training sessions
- Client meetings
- Strategy discussions
- Technical walkthroughs

**Storage:**
- Department Loom folder
- Google Drive backup
- Link in meeting notes

### 7.2 Transcription Standards

**Format:**
- Speaker identification
- Timestamps
- Action items highlighted
- Decisions marked

**Processing:**
- Within 24 hours
- Extract to daily notes
- Link to TASK_MANAGERS

### 7.3 Third Recording Rule

> "If we've explained something three times, it must be recorded and documented. No more repeat explanations."

---

## 8. Whisper Flow Integration

### 8.1 Real-Time Transcription

**Use Case:** Capture conversations as they happen

**Setup:**
1. Install Whisper Flow
2. Start recording
3. Auto-transcribe
4. Save to daily notes

### 8.2 Benefits

- No post-processing needed
- Immediate documentation
- Context preserved
- Searchable instantly

### 8.3 File Naming

**Format:** `[Department]_[Topic]_[Date].md`
**Example:** `AI_Training_Session_191125.md`

---

## 9. Content Department Vision

### 9.1 New Entity: Content

**Purpose:** Centralized content production

**Includes:**
- Video processing
- Tutorial creation
- Documentation
- Knowledge extraction

### 9.2 Content Shifts

**Concept:** Multiple shifts working on content

**Shift 1:** Raw capture (recordings, notes)
**Shift 2:** Processing (transcription, extraction)
**Shift 3:** Integration (LIBRARIES, TASK_MANAGERS)

### 9.3 YouTube Channel Content

**Goal:** Create employee training videos for public channel

**Process:**
1. Record internal training
2. Edit for external audience
3. Add captions/graphics
4. Publish to REM-S channel
5. Track engagement

---

## 10. Implementation Checklist

### Completed
- [x] AI Studio custom instructions
- [x] Video transcription workflow
- [x] Milestone-based extraction design
- [x] Whisper Flow integration

### In Progress
- [ ] Video index system
- [ ] Loom data export
- [ ] YouTube parsing automation
- [ ] Token tracking dashboard

### Planned
- [ ] Automated video detection
- [ ] Smart segmentation
- [ ] Multi-language support
- [ ] Quality scoring

---

## Cross-References

**Related Export Files:**
- [02_RAG_Systems_Knowledge_Management.md](02_RAG_Systems_Knowledge_Management.md) - Data extraction
- [03_Team_Training_Development.md](03_Team_Training_Development.md) - Training recordings
- [07_Technical_Guides.md](07_Technical_Guides.md) - Setup guides

**Source Files:**
- [Video Instructions Transcribations.md](../Video%20Instructions%20Transcribations.md)
- [121125_structured_v2.md](../121125_structured_v2.md)
- [MAIN_PROMPT_v5_Modular](../../W3/MAIN_PROMPT_v5_Modular/)

---

## Metadata

**Extraction Date:** 2025-11-20
**Processing:** MAIN_PROMPT v5.0
**Confidence:** High (90%+)
**Line Count:** ~400

---

**Generated by MAIN_PROMPT v5.0 Export Process**
**Remote Helpers - AI-First Organization**
**November 2025**
