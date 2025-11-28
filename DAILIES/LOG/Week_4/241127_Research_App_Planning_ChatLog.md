# Research App Planning Session - Chat Log
**Date:** 2025-11-27
**Session:** Research Management App - Platform Selection & Prompt Generation
**Plan File:** `C:\Users\Dell\.claude\plans\rippling-marinating-raccoon.md`

---

## Session Summary

### Initial Request
User requested creation of prompts for building a Research App based on the existing RESEARCHES system at `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES`.

### Key Decisions Made

#### 1. Platform Evolution
- **Initial Preference:** Desktop application (Windows)
- **Final Decision:** Web application (React + Supabase)
- **Rationale:** Easier installation, cross-platform, shareable, compatible with AI builders (Lovable, v0, Cursor)

#### 2. Database Selection
- **Initial Consideration:** Airtable (non-conventional)
- **Final Decision:** PostgreSQL via Supabase
- **Features:**
  - Relational database with JSONB support
  - pgvector extension for semantic search
  - Real-time subscriptions
  - Auto-generated REST API
  - Built-in authentication

#### 3. Architecture
- **2 Separate Web Apps:**
  1. Queue Management App (search + video queues)
  2. Video Processing App (multi-agent AI orchestration)

#### 4. AI Integration
- **Primary:** OpenRouter API (unified access to 100+ models)
- **Fallbacks:** Claude API, GPT API, Gemini API

---

## Conversation Flow

### Phase 1: Initial Exploration
**User:** "Create Prompt For Building Research App based on C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES"

**Assistant Actions:**
- Launched Explore agent to analyze RESEARCHES directory structure
- Discovered comprehensive system:
  - 7-phase research workflow (Phase 0 → Complete)
  - 23+ video transcriptions
  - 50+ processing prompts
  - 14 automation scripts
  - 4 master CSV tracking files
  - Existing comprehensive documentation (2230 lines)

**Key Findings:**
- Search Queue Master (7 columns)
- Video Queue Master (21 columns)
- Progress tracking across phases
- Entity extraction system (Tools, Workflows, Actions, Objects)
- Integration with ENTITIES ecosystem

### Phase 2: Requirements Clarification
**User Inputs:**
1. "I want it in React"
2. "I would prefer desktop application, but for Windows"
3. "Can you make me a comparison between those options?"
4. "Split the prompt into multiple apps"
5. "One will be for the queue management, the other one will be video processing"
6. "Transcription research will be made manually placed inside Gemini or Perplexity or Grok"
7. "No database now. Maybe we can use non-conventional like Airtable"
8. "Can also be GPT API, Gemini API"
9. "Add OpenRouter"

**Assistant Response:**
- Created initial plan for Desktop app (Electron)
- Outlined Airtable database schema
- Proposed modular architecture with 4 prompts

### Phase 3: Platform Pivot
**User:** "Now if we are talking, it will be easier for us to install a web version first. Let's go for a web demo version and yes, split into two apps. Let's go for the React and database, like SQL database, or the best would be any possible vector database. If the AI, like Lovable, can create and work with it, but usually it is working with Postgres super base."

**Critical Decision:** Platform changed from Desktop (Electron) to Web (React + Supabase)

**Assistant Actions:**
- Updated plan completely for web architecture
- Switched database from Airtable to PostgreSQL (Supabase)
- Added pgvector extension for semantic search
- Designed 8-table database schema
- Created AI builder-compatible approach

---

## Final Architecture

### Technology Stack

**App 1: Queue Management Web App**
```
Frontend:
- React 18 + TypeScript
- Vite (build tool)
- shadcn/ui + Tailwind CSS
- TanStack Table (data grids)
- TanStack Query (React Query)
- Recharts (visualizations)

Backend:
- Supabase (PostgreSQL)
  - Built-in auth
  - Real-time subscriptions
  - Row-level security
  - Auto-generated REST API
  - Storage for file uploads

Deployment:
- Vercel (free tier)
```

**App 2: Video Processing Web App**
```
Frontend:
- React 18 + TypeScript
- Vite
- shadcn/ui + Tailwind CSS
- React Flow (agent visualization)
- Markdown editor/viewer

Backend:
- Supabase (PostgreSQL)
  - JSONB for flexible data
  - pgvector for embeddings

AI Integration:
- OpenRouter API (primary)
- Claude API (fallback)
- GPT API (fallback)
- Gemini API (fallback)

Deployment:
- Vercel (free tier)
```

---

## Database Schema (PostgreSQL/Supabase)

### 8 Tables Created

1. **employees**
   - Employee management
   - Departments: VID, AID, HRM, FIN, MKT, ALL
   - Roles: Researcher, Analyst, Admin

2. **search_queue**
   - Search task assignments
   - Status tracking: Assigned → In Progress → Completed
   - Links to employees

3. **video_queue**
   - Video processing queue
   - Priority scoring (0-100)
   - Status: Pending → Selected → Transcribing → Parsed → Completed → Skipped
   - YouTube metadata (views, likes, comments, duration)

4. **video_progress**
   - Phase tracking (Phases 0-5)
   - Stores transcription text (TEXT or JSONB)
   - Extraction data, gap analysis, mapping reports

5. **extracted_entities**
   - Entity types: Tool, Workflow, Action, Object, Skill, Profession
   - Status: NEW, EXISTS, NEEDS_UPDATE
   - Priority: CRITICAL, HIGH, MEDIUM, LOW
   - Optional: embedding vector(1536) for semantic search

6. **ai_api_usage**
   - Track API costs per video
   - Token usage (prompt, completion, total)
   - Response times
   - Success/error tracking

7. **prompt_templates**
   - Store PMT-004, PMT-007, PMT-009 prompts
   - Configurable per phase
   - Model, temperature, max_tokens settings

8. **ai_provider_config**
   - API keys for OpenRouter, Claude, GPT, Gemini
   - Priority, cost, rate limits
   - Enable/disable providers

---

## Implementation Prompts Planned

### Prompt 1: Supabase Database Schema
**File:** `01_Supabase_Database_Schema_Prompt.md`
**Purpose:** Complete PostgreSQL schema setup
**Includes:**
- All 8 table CREATE statements
- Indexes for performance
- Row-Level Security policies
- Real-time subscription setup
- pgvector extension (optional)
- Seed data for testing

### Prompt 2: Queue Management Web App
**File:** `02_Queue_Management_Web_App_Prompt.md`
**Purpose:** Build App 1 with AI builder (Lovable/v0/Cursor)
**Features:**
- Dashboard (KPIs, charts)
- Search Queue table (CRUD)
- Video Queue table (CRUD, priority calculator)
- Employee management
- Settings page
- Real-time updates
- Dark/light mode toggle

### Prompt 3: Video Processing Web App
**File:** `03_Video_Processing_Web_App_Prompt.md`
**Purpose:** Build App 2 with AI builder
**Features:**
- Video selector
- Transcription uploader (markdown)
- Phase processing dashboard:
  - Phase 2: Extract Entities
  - Phase 3: Gap Analysis
  - Phase 4: Generate JSON
  - Phase 5: Create Mapping Report
- Real-time progress tracking
- Cost tracker (API usage)
- Report viewer with download

---

## AI Processing Pipeline (App 2)

```
1. User uploads Video_001.md (transcription)
2. Click "Start Processing" button
3. Phase 2: Call OpenRouter → Extract entities → Save to DB
4. Phase 3: Call OpenRouter → Gap analysis → Save results
5. Phase 4: Call OpenRouter → Generate JSON → Save files
6. Phase 5: Call OpenRouter → Library mapping → Generate report
7. Update video_progress table (track completion)
8. Display results in UI with download buttons
```

---

## Development Workflow

### Step 1: Setup Supabase
1. Create account at https://supabase.com
2. Create new project
3. Run SQL schema scripts
4. Enable pgvector (optional)
5. Configure RLS policies
6. Set up authentication
7. Get API keys

### Step 2: Build App 1 (Queue Management)
**Tools:** Lovable.dev / v0.dev / Cursor
**Timeline:** Estimated 1-2 weeks
**Deployment:** Vercel (automatic)

### Step 3: Build App 2 (Video Processing)
**Tools:** Lovable.dev / v0.dev / Cursor
**Timeline:** Estimated 2-3 weeks
**Deployment:** Vercel (automatic)

### Step 4: Data Migration (Optional)
- Import existing CSV data
- Upload existing transcriptions
- Import prompt templates

---

## Key Technical Decisions

### Why Supabase?
- ✅ Open source (Firebase alternative)
- ✅ PostgreSQL (powerful + JSONB)
- ✅ Auto-generated REST API
- ✅ Real-time subscriptions
- ✅ Built-in authentication
- ✅ Free tier (500MB DB, 1GB storage)
- ✅ pgvector for AI/embeddings

### Why React + Vite?
- ✅ Modern build tool (faster than Create React App)
- ✅ TypeScript support
- ✅ HMR (Hot Module Replacement)
- ✅ Compatible with AI builders

### Why shadcn/ui?
- ✅ Copy-paste components (not NPM package)
- ✅ Full customization
- ✅ Tailwind CSS based
- ✅ Accessible (Radix UI primitives)
- ✅ Popular with AI builders

### Why OpenRouter?
- ✅ Unified API for 100+ models
- ✅ Cost optimization
- ✅ Automatic fallback
- ✅ Built-in usage tracking
- ✅ Higher rate limits

---

## Priority Scoring Algorithm

```javascript
function calculatePriority(views, likes, publish_date, topic_relevance) {
  const view_score = Math.min((views / 1000000) * 30, 30);
  const engagement_score = Math.min((likes / 10000) * 20, 20);

  const days_old = (today - publish_date).days;
  let recency_score;
  if (days_old <= 30) recency_score = 25;
  else if (days_old <= 90) recency_score = 20;
  else if (days_old <= 180) recency_score = 15;
  else recency_score = 10;

  const relevance_score = topic_relevance * 25; // 0-1 scale

  return view_score + engagement_score + recency_score + relevance_score;
}
```

---

## Multi-User Features

### Real-Time Collaboration
- Supabase Realtime subscriptions
- Live updates when employees make changes
- Toast notifications: "John just added a new video"
- Highlight new/updated rows

### Assignment Tracking
- "Added_By" and "Selected_By" fields
- Filter views: "My Videos", "My Searches", "All"
- Employee workload dashboard
- Leaderboard (most videos processed)

### Conflict Prevention
- Lock records during editing
- Show "John is currently editing" indicator
- Auto-save drafts to Supabase
- Last-write-wins with timestamps

---

## Future Enhancements

### Phase 3: Advanced File Storage
- Supabase Storage for transcriptions
- Supabase Storage for reports
- Replace local Dropbox (optional)

### Phase 4: AI-Powered Features
- Semantic search with pgvector
- Duplicate detection
- Automated priority scoring with embeddings
- Chat interface for querying research
- Recommendation system

---

## Files Referenced

### Explored During Planning
1. ✅ `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\App_Development_Prompt.md` (2230 lines)

### To Reference When Building
2. `README.md` - System overview
3. `SYSTEM_OVERVIEW.md` - Architecture details
4. `SCRIPTS_INVENTORY.md` - Automation scripts
5. `Search_Queue_Master.csv` - Schema reference
6. `Video_Queue_Master.csv` - Schema reference
7. `Video_001.md` - Transcription format example
8. `PMT-004`, `PMT-007`, `PMT-009` - Prompt templates

---

## Next Steps Options

**Option A:** Create all 3 implementation prompts
- 01_Supabase_Database_Schema_Prompt.md
- 02_Queue_Management_Web_App_Prompt.md
- 03_Video_Processing_Web_App_Prompt.md

**Option B:** Start with Supabase schema only

**Option C:** Jump to building App 1 with AI builder

---

## Session Artifacts

### Plan File
**Location:** `C:\Users\Dell\.claude\plans\rippling-marinating-raccoon.md`
**Lines:** ~1100
**Status:** Approved ✅

### Chat Log
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\LOG\241127_Research_App_Planning_ChatLog.md`
**Status:** Saved ✅

---

## Conclusion

This planning session successfully transformed an initial request for "prompts to build a research app" into a comprehensive architecture for two web applications:

1. **Queue Management App** - Manages search and video queues with priority scoring
2. **Video Processing App** - Multi-agent AI orchestration for entity extraction and analysis

The plan is AI builder-ready (Lovable/v0/Cursor) with complete database schema, technology stack, and implementation roadmap.

**Estimated Total Development Time:** 3-5 weeks for both apps

**Estimated Cost:** $0 (all free tiers - Supabase, Vercel, OpenRouter has free tier)

---

**End of Chat Log**
