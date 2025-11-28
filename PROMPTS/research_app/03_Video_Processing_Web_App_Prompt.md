# Video Processing Web App - Complete Implementation Prompt

## Overview

Build a **Video Processing Web Application** for managing the 7-phase research workflow with AI-powered video transcription analysis. This is Part 2 of a 2-app Research Management System. The app handles Phases 0-5 of the research workflow, from transcription upload to final knowledge mapping.

**Technology Stack:**
- React 18 + TypeScript
- Vite (build tool)
- Supabase (PostgreSQL database + real-time subscriptions)
- shadcn/ui (component library)
- TanStack Query (data fetching)
- React Flow (workflow visualization)
- Recharts (charts/visualizations)
- OpenRouter API (multi-AI orchestration)
- Tailwind CSS (styling)

**Database:** Uses the Supabase PostgreSQL schema from `01_Supabase_Database_Schema_Prompt.md`

---

## 🎨 Design System Integration

### Using Existing RHS Design Assets

This app uses the **AdminRHS-AI-Catalog** design system created by the Design Department. The design system provides a complete UI toolkit with a friendly, educational aesthetic optimized for catalog/dashboard applications.

### Available SVG Icons (Inline - Ready to Use)

- ✅ `upload.svg` - Transcription file upload
- ✅ `ai.svg` - AI processing indicators
- ✅ `lightning.svg` - Phase processing actions
- ✅ `create.svg` - Generate reports
- ✅ `edit.svg` - Edit prompts/settings
- ✅ `filter.svg` - Filter videos by status
- ✅ `search.svg` - Search processed videos
- ✅ `moon.svg` / `sun.svg` - Dark/light mode

### Color Palette (From AdminRHS-AI-Catalog)

**Light Mode**:

```css
--background: #f5f5f5;
--foreground: #2d465d;
--card: #ffffff;
--accent-blue: #428eb4;
--accent-blue-hover: #28749b;
```

**Dark Mode**:

```css
--background: #1a1a1a;
--foreground: #e0e0e0;
--card: #2d2d2d;
```

### Phase Status Colors

```css
/* Phase 0-5 Color Coding */
--phase-0: #9CA3AF;  /* Gray - Search */
--phase-1: #60A5FA;  /* Blue - Transcription */
--phase-2: #34D399;  /* Green - Extraction */
--phase-3: #FBBF24;  /* Yellow - Gap Analysis */
--phase-4: #F97316;  /* Orange - Integration */
--phase-5: #A78BFA;  /* Purple - Mapping */
--complete: #10B981; /* Emerald - Complete */
```

### UI Component Patterns

1. **File Upload Zone** (Drag & Drop)
   - Use `upload.svg` icon
   - Dashed border on default state
   - Solid blue border on drag-over
   - Success state with checkmark

2. **Phase Progress Cards**
   - Card layout from AdminRHS-AI-Catalog
   - Color-coded by phase (see colors above)
   - Progress bar with percentage
   - Phase icon (use `ai.svg` or `lightning.svg`)

3. **Cost Tracker Widget**
   - Compact card design
   - Real-time token counter
   - Running cost display in USD
   - Color changes based on budget (green → yellow → red)

---

## 📋 Research Workflow Context

### Video Transcript Processing Pipeline (Phases 1-5)

This Video Processing App handles **Phases 1-5** of the research workflow, transforming raw video transcriptions into structured, searchable tool libraries.

**Complete Workflow Overview:**

| Phase | Name | AI Agent | Input | Output | Status Tracking |
|-------|------|----------|-------|--------|----------------|
| **Phase 0** | Search & Selection | Manual | Daily reports | Video queue | Queue Management App |
| **Phase 1** | Transcription | Manual upload | Video URLs | Raw transcripts | **This App** |
| **Phase 2** | Entity Extraction | Parser (GPT-4, Claude) | Transcripts | Structured entities | **This App** |
| **Phase 3** | Gap Analysis | Analyzer (Claude Opus) | Extracted data | Knowledge gaps | **This App** |
| **Phase 4** | Integration | Integrator (Gemini Pro) | Entities + KB | Integrated data | **This App** |
| **Phase 5** | Mapping | Mapper (GPT-4, Claude) | Integrated data | Knowledge maps | **This App** |
| **Complete** | Final Review | Manual | All phases | Approved output | **This App** |

**Detailed Phase Descriptions:**

### Phase 1: Transcription Upload
- **Input:** Video URL + transcription file (from Google AI Studio, Transcribe AI, or manual)
- **Process:** Upload raw transcript with timestamps and speaker annotations
- **Storage:** Saved in `Transcribations` folder, linked to video record
- **Output:** Transcript ready for AI processing

### Phase 2: Entity Extraction
- **AI Tools:** Claude Sonnet 4.5 (recommended), GPT-4
- **Focus Areas:**
  - Tools & Technologies (frameworks, libraries, APIs, services)
  - Workflows (development workflows, coding patterns)
  - Actions (development operations, technical actions)
  - Integration Patterns (how tools connect)
  - Use Cases (specific applications, examples)
- **Processing Approach:** AI reads the transcript and identifies every tool mentioned, extracting not just names but versions, use cases, strengths/limitations, and how they integrate with other tools
- **Output:** Structured extraction with taxonomy elements (Actions, Objects, Tools, Skills)

### Phase 3: Gap Analysis
- **AI Tools:** Claude Opus, GPT-4
- **Process:** Identify missing information, incomplete details, validation needs
- **Analysis:**
  - Missing tool specifications (versions, compatibility)
  - Incomplete workflow steps
  - Unclear integration patterns
  - Missing use case details
- **Output:** List of gaps with severity levels (Critical, Important, Nice-to-have)

### Phase 4: Knowledge Base Integration
- **AI Tools:** Claude Sonnet, Gemini Pro
- **Process:** Integrate extracted data with existing tool libraries
- **Integration Checks:**
  - Duplicate detection (tool already exists?)
  - Conflict resolution (different information about same tool)
  - Cross-referencing (link to related tools/workflows)
  - Category assignment (AI_Tools, Development_Tools, etc.)
- **Output:** Integration plan with merge/update/create actions

### Phase 5: Knowledge Mapping
- **AI Tools:** GPT-4, Claude Opus
- **Process:** Create visual knowledge maps and relationship graphs
- **Map Types:**
  - Tool relationship diagrams (which tools work together)
  - Workflow visualizations (step-by-step processes)
  - Technology stack maps (full development environments)
  - Integration pattern charts (data flow between tools)
- **Output:** JSON files for `LIBRARIES/Tools/` with complete metadata

**Pipeline Summary:** Raw video transcripts flow through 5 AI-powered phases, each extracting progressively deeper insights. Phase 2 identifies what tools are mentioned → Phase 3 finds missing details → Phase 4 merges with existing knowledge → Phase 5 creates relationship maps → Final output is structured JSON ready for the tool library. Each phase uses the best AI model for that task (Claude for extraction, Gemini for large context integration, GPT-4 for structured JSON generation)

---

## 🏗️ Entity Taxonomy & Libraries Framework

### Task Manager Integration

This app creates and tracks entities following Remote Helpers' taxonomy:

```
PRT (Project Templates) - Video research processing projects
  ├─→ MLT (Milestone Templates) - Processing milestones (transcription batch, extraction sprint)
       ├─→ TST (Task Templates) - Individual video processing tasks
            └─→ STT (Step Templates) - Granular actions (upload, extract, analyze)
```

**Entity Examples for Video Processing:**

| Entity Type | Example ID | Description | Phase |
|-------------|------------|-------------|-------|
| **TST** | TST-088 | Process "Claude Desktop Setup" video | All phases |
| **STT** | STT-201 | Upload transcription file | Phase 1 |
| **STT** | STT-202 | Run entity extraction prompt | Phase 2 |
| **STT** | STT-203 | Validate extracted tools | Phase 3 |
| **STT** | STT-204 | Merge with tool library | Phase 4 |
| **STT** | STT-205 | Generate knowledge map | Phase 5 |
| **TOL** | TOL-150 | Tool being documented (e.g., Claude Desktop) | Output |
| **PMT** | PMT-004 to PMT-013 | Video processing prompts | Processing |

**Libraries Framework: Actions + Objects + Tools = Skills**

The extraction process identifies these taxonomy elements:

### Actions by Department

**AI Actions** (extracted from videos):
- extract, analyze, build, configure, automate, coordinate
- establish, evaluate, grade, measure, plan, reflect

**Dev Actions** (common in tech videos):
- build, develop, configure, automate, test, extract
- deploy, edit, format, generate, compile, modify

**Example:** "automated workflows in n8n" → Action: automate, Object: workflows, Tool: n8n

### Objects by Department

**Dev Objects** (extracted from videos):
- APIs (REST, GraphQL, internal, external)
- Databases (PostgreSQL, MongoDB, MySQL)
- Modules (frontend, backend, shared)
- Code (functions, components, tests, scripts)

**Example:** "built REST APIs in Node.js" → Object: REST APIs, Tool: Node.js

### Skills Formula

**Skill = Action + Object + Tool**

Examples from video content:
- "deployed applications via GitHub Actions" = deploy + applications + GitHub Actions
- "tested components with Jest" = test + components + Jest
- "extracted data via Claude" = extract + data + Claude

**Storage Structure:**
- Extracted tools → `LIBRARIES/Tools/[Category]/[Tool].json`
- Categories: `AI_Tools/`, `Development_Tools/`, `Integration_Tools/`, `Frameworks/`, `APIs/`, `DevOps_Tools/`

**Libraries Framework Explanation:** This taxonomy captures how work gets done. An "Action" (verb like "deploy") combined with an "Object" (noun like "applications") using a "Tool" (software like "GitHub Actions") equals a "Skill" (capability the team has). By extracting these from videos, the system builds a searchable database of what tools can do and how they're actually used in real workflows

---

## 🤖 AI Orchestration with OpenRouter

### Multi-Model Processing Strategy

This app uses **OpenRouter API** to orchestrate multiple AI models for different phases:

**Phase 2: Entity Extraction**
- **Primary:** Claude Sonnet 4.5 (best for structured extraction)
- **Fallback:** GPT-4 Turbo (when Claude rate-limited)
- **Prompt Template:** `PMT-004` to `PMT-013` (video transcription prompts)

**Phase 3: Gap Analysis**
- **Primary:** Claude Opus (best for analytical reasoning)
- **Fallback:** GPT-4 (cost-effective alternative)

**Phase 4: Integration**
- **Primary:** Gemini Pro 1.5 (best for large context, library comparison)
- **Fallback:** Claude Sonnet (structured integration)

**Phase 5: Mapping**
- **Primary:** GPT-4 (best for structured JSON generation)
- **Fallback:** Claude Opus (detailed relationship mapping)

**OpenRouter Configuration:**

```typescript
// Example API call structure
const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${OPENROUTER_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'anthropic/claude-sonnet-4.5', // or other models
    messages: [
      { role: 'system', content: 'Extract development tools from transcript...' },
      { role: 'user', content: transcriptText }
    ],
    max_tokens: 4000,
    temperature: 0.2 // Low temperature for consistent extraction
  })
});
```

**Cost Tracking:**
- Track tokens used per phase
- Calculate cost per video processed
- Display running totals in `ai_api_usage` table
- Alert when daily budget exceeded

---

## 🛠️ Development Tools Reference

### Tools Used in Video Processing

**AI Models (via OpenRouter):**

| Model | Vendor | Best For | Cost (per 1M tokens) |
|-------|--------|----------|---------------------|
| **Claude Sonnet 4.5** | Anthropic | Entity extraction, structured output | ~$3 input, ~$15 output |
| **Claude Opus** | Anthropic | Gap analysis, reasoning | ~$15 input, ~$75 output |
| **GPT-4 Turbo** | OpenAI | JSON generation, mapping | ~$10 input, ~$30 output |
| **Gemini Pro 1.5** | Google | Large context, integration | ~$1.25 input, ~$5 output |

**Transcription Tools** (external, mentioned for context):

| Tool | Purpose | Max Video Length |
|------|---------|-----------------|
| **Google AI Studio** | Free transcription | ~1 hour videos |
| **Transcribe AI** | Paid transcription for large videos | Unlimited |
| **Claude Desktop** | Manual transcription with MCP | Any length |

**Automation & Integration:**

| Tool | Use Case in Video Processing |
|------|----------------------------|
| **n8n** | Automate phase triggers, notifications, library updates |
| **MCP Connectors** | Connect Claude to Supabase, file systems |
| **Supabase Realtime** | Live progress updates during AI processing |

**Why Multiple AI Models?** Different AI models excel at different tasks. Claude Sonnet is best at structured extraction from messy text. Gemini Pro handles large context windows for comparing against existing libraries. GPT-4 generates the cleanest JSON output. The app automatically routes each phase to the optimal model, with fallbacks if the primary model is rate-limited. Cost tracking helps stay within budget (~$0.50-$2.00 per video depending on length and complexity)

---

## 🔄 Processing Automation Logic

### Existing Python Scripts (Reference for Implementation)

Remote Helpers currently uses Python scripts that automate Phases 2-5 processing, reducing manual work from **1.5-2 hours → 5-10 minutes per video**. The web app should replicate this automation logic.

**Key Automation Features to Implement:**

### 1. ID Scanner (Next Available Entity IDs)

When creating new entities (tools, workflows, actions), the app must find the next sequential ID:

**Logic:**
- Scan `extracted_entities` table for existing IDs
- Extract numeric part (e.g., "TOOL-AI-223" → 223)
- Calculate next ID (223 + 1 = 224)
- Format with zero-padding: "TOOL-AI-224"

**Entity ID Patterns:**
- Workflows: `WRF-###` (e.g., WRF-025)
- Actions: `ACTION-###` (e.g., ACTION-433)
- Tools: `TOOL-{CATEGORY}-###` (e.g., TOOL-AI-223, TOOL-VID-045)
- Objects: `OBJ-{DEPT}-###` (e.g., OBJ-SMM-015)
- Skills: `SKL-###` (e.g., SKL-065)

**UI Component:**
- Display "Next Available IDs" panel before processing
- Show for each entity type
- Auto-increment as entities are created

### 2. Gap Analysis (NEW vs EXISTING Detection)

Before integrating extracted entities, determine if they already exist:

**Classification Logic:**
```typescript
// For each extracted entity
if (entityExistsInDatabase(entity.name)) {
  if (hasConflictingInfo(entity, existingEntity)) {
    classify_as = "UPDATE";  // Same name, different info
  } else {
    classify_as = "EXISTING";  // Already documented, skip
  }
} else {
  classify_as = "NEW";  // Not in database, needs creation
}
```

**Gap Analysis Output:**
- **NEW:** Entities not in database (green badge, create action)
- **EXISTING:** Entities already documented (gray badge, skip)
- **UPDATE:** Entities with conflicting info (yellow badge, review needed)

**UI Component:**
- Gap analysis results table with color-coded badges
- Approve/reject checkboxes for NEW entities
- Side-by-side comparison for UPDATE entities
- Bulk actions (Approve All NEW, Skip All EXISTING)

### 3. Safe JSON Update with Backup

When integrating entities, prevent data loss:

**Update Process:**
1. **Backup** - Save current state to `_backups` table with timestamp
2. **Validate** - Check all required fields present, IDs formatted correctly
3. **Update** - Insert/update entities in Supabase
4. **Verify** - Confirm all operations succeeded
5. **Rollback** - If any step fails, restore from backup

**UI Components:**
- Progress bar showing: "Backing up → Validating → Updating → Verifying"
- Success/failure notifications
- "Undo Last Integration" button (restores from backup)

### 4. Progress Tracking

Track which phase each video is in:

**Phase Auto-Advancement:**
- Phase 1 complete → Auto-advance to Phase 2
- Phase 2 complete → Auto-advance to Phase 3
- Continue until Phase 5 complete → Mark as "Complete"

**Status Updates:**
```typescript
// Update video_progress table
UPDATE video_progress
SET
  phase_2_extraction_completed = NOW(),
  current_phase = 'phase_3_gap_analysis',
  status = 'in_progress'
WHERE video_id = 'Video_024';
```

**UI Components:**
- Visual workflow diagram showing current phase
- Phase completion checkmarks
- Estimated time remaining based on historical averages

### 5. Error Handling

Handle common processing errors gracefully:

**Error Scenarios:**
- Missing required fields → Show which fields are missing
- Invalid ID format → Highlight incorrect format, show example
- Duplicate entity → Display existing entity for comparison
- API rate limit → Queue for retry with exponential backoff
- Network failure → Save progress locally, resume when reconnected

**UI Components:**
- Toast notifications for non-critical errors
- Modal dialogs for critical errors requiring user action
- Error log viewer (filterable by video, phase, severity)

### 6. Batch Processing

Enable processing multiple videos simultaneously:

**Parallel Processing:**
- Queue up to 3 videos for concurrent processing
- Each video processes independently
- Real-time progress for each video in queue
- Pause/resume/cancel individual videos

**UI Components:**
- Processing queue panel (drag to reorder)
- Per-video progress bars
- Pause/Resume/Cancel buttons
- "Process All Pending" bulk action

---

## Prerequisites

Before starting, ensure you have:

1. **Supabase Project:**
   - Created a Supabase project at https://supabase.com
   - Executed all SQL from `01_Supabase_Database_Schema_Prompt.md` in SQL Editor
   - Noted your Project URL and anon public key
   - Enabled real-time for tables: `video_progress`, `extracted_entities`, `ai_api_usage`

2. **OpenRouter API Key:**
   - Sign up at https://openrouter.ai
   - Create API key
   - Fund account (pay-per-use, no subscription)

3. **Development Environment:**
   - Node.js 18+ installed
   - Git installed
   - Code editor (VS Code recommended)
   - Modern browser (Chrome/Firefox/Edge)

---

## 7-Phase Research Workflow

This app processes videos through these phases:

| Phase | Name | Description | AI Agent Role |
|-------|------|-------------|---------------|
| **Phase 0** | Search & Selection | Manual video search and selection | Manual (user via Queue Management app) |
| **Phase 1** | Transcription | Upload transcription from Claude/Perplexity/Grok | Manual upload (this app provides uploader) |
| **Phase 2** | Entity Extraction | Extract entities, concepts, frameworks | AI Agent: Parser (GPT-4, Claude Sonnet) |
| **Phase 3** | Gap Analysis | Identify knowledge gaps, missing info | AI Agent: Analyzer (Claude Opus, GPT-4) |
| **Phase 4** | Integration | Integrate with existing knowledge base | AI Agent: Integrator (Claude Sonnet, Gemini Pro) |
| **Phase 5** | Mapping | Create knowledge maps and relationships | AI Agent: Mapper (GPT-4, Claude Opus) |
| **Complete** | Final Review | Human review and approval | Manual review |

**This app handles Phases 1-5.**

---

## Project Setup

### 1. Initialize Vite + React + TypeScript Project

```bash
npm create vite@latest video-processing-app -- --template react-ts
cd video-processing-app
npm install
```

### 2. Install Core Dependencies

```bash
# Supabase client
npm install @supabase/supabase-js

# UI Components
npm install @radix-ui/react-slot @radix-ui/react-dialog @radix-ui/react-dropdown-menu @radix-ui/react-select @radix-ui/react-tabs @radix-ui/react-toast @radix-ui/react-label @radix-ui/react-checkbox @radix-ui/react-progress @radix-ui/react-accordion

# Data fetching and state
npm install @tanstack/react-query

# Workflow visualization
npm install reactflow

# Charts
npm install recharts

# File handling
npm install react-dropzone

# Utilities
npm install clsx tailwind-merge date-fns lucide-react axios

# Dev dependencies
npm install -D tailwindcss postcss autoprefixer
npm install -D @types/node
```

### 3. Initialize Tailwind CSS

```bash
npx tailwindcss init -p
```

Update `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [],
}
```

Update `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 221.2 83.2% 53.3%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 221.2 83.2% 53.3%;
    --radius: 0.5rem;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

---

## Project Structure

```
video-processing-app/
├── src/
│   ├── components/
│   │   ├── ui/                    # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── input.tsx
│   │   │   ├── progress.tsx
│   │   │   ├── tabs.tsx
│   │   │   ├── accordion.tsx
│   │   │   └── toast.tsx
│   │   ├── layout/
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Header.tsx
│   │   │   └── Layout.tsx
│   │   ├── dashboard/
│   │   │   ├── ProcessingStatsCard.tsx
│   │   │   ├── PhaseDistributionChart.tsx
│   │   │   ├── CostTrackingCard.tsx
│   │   │   └── ActiveVideos.tsx
│   │   ├── transcription/
│   │   │   ├── TranscriptionUploader.tsx
│   │   │   ├── DropzoneArea.tsx
│   │   │   └── UploadHistory.tsx
│   │   ├── processing/
│   │   │   ├── VideoList.tsx
│   │   │   ├── VideoCard.tsx
│   │   │   ├── PhaseProcessor.tsx
│   │   │   └── ProcessingLog.tsx
│   │   ├── workflow/
│   │   │   ├── WorkflowVisualization.tsx
│   │   │   ├── PhaseNode.tsx
│   │   │   └── ProgressIndicator.tsx
│   │   ├── ai-agents/
│   │   │   ├── AgentOrchestrator.tsx
│   │   │   ├── AgentConfig.tsx
│   │   │   ├── ModelSelector.tsx
│   │   │   └── PromptEditor.tsx
│   │   ├── reports/
│   │   │   ├── ReportGenerator.tsx
│   │   │   ├── EntityReport.tsx
│   │   │   ├── CostReport.tsx
│   │   │   └── ExportDialog.tsx
│   │   └── settings/
│   │       ├── AIProviderSettings.tsx
│   │       ├── APIKeyManager.tsx
│   │       └── PromptTemplateManager.tsx
│   ├── lib/
│   │   ├── supabase.ts           # Supabase client
│   │   ├── openrouter.ts         # OpenRouter API client
│   │   ├── queries.ts            # React Query hooks
│   │   ├── ai-agents.ts          # AI agent orchestration
│   │   └── utils.ts              # Utility functions
│   ├── types/
│   │   ├── database.ts           # TypeScript types
│   │   └── ai-agents.ts          # AI agent types
│   ├── prompts/
│   │   ├── phase2-extraction.ts  # Phase 2 prompt
│   │   ├── phase3-analysis.ts    # Phase 3 prompt
│   │   ├── phase4-integration.ts # Phase 4 prompt
│   │   └── phase5-mapping.ts     # Phase 5 prompt
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── TranscriptionUpload.tsx
│   │   ├── VideoProcessing.tsx
│   │   ├── WorkflowView.tsx
│   │   ├── Reports.tsx
│   │   └── Settings.tsx
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
├── .env.local
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

---

## Configuration Files

### Environment Variables (`.env.local`)

Create `.env.local` in project root:

```env
# Supabase
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-public-key

# OpenRouter API
VITE_OPENROUTER_API_KEY=sk-or-v1-...your-key
VITE_OPENROUTER_SITE_URL=https://your-app-name.vercel.app
VITE_OPENROUTER_SITE_NAME=Video Processing App
```

**IMPORTANT:** Replace with your actual credentials.

### TypeScript Configuration (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

### Vite Configuration (`vite.config.ts`)

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
```

---

## Core Implementation

### 1. Supabase Client (`src/lib/supabase.ts`)

```typescript
import { createClient } from '@supabase/supabase-js'
import { Database } from '@/types/database'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

if (!supabaseUrl || !supabaseAnonKey) {
  throw new Error('Missing Supabase environment variables')
}

export const supabase = createClient<Database>(supabaseUrl, supabaseAnonKey)
```

### 2. OpenRouter API Client (`src/lib/openrouter.ts`)

```typescript
import axios from 'axios'

const OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'

export interface OpenRouterMessage {
  role: 'system' | 'user' | 'assistant'
  content: string
}

export interface OpenRouterRequest {
  model: string
  messages: OpenRouterMessage[]
  temperature?: number
  max_tokens?: number
  top_p?: number
}

export interface OpenRouterResponse {
  id: string
  model: string
  choices: Array<{
    message: {
      role: string
      content: string
    }
    finish_reason: string
  }>
  usage: {
    prompt_tokens: number
    completion_tokens: number
    total_tokens: number
  }
}

export async function callOpenRouter(request: OpenRouterRequest): Promise<OpenRouterResponse> {
  const apiKey = import.meta.env.VITE_OPENROUTER_API_KEY
  const siteUrl = import.meta.env.VITE_OPENROUTER_SITE_URL
  const siteName = import.meta.env.VITE_OPENROUTER_SITE_NAME

  if (!apiKey) {
    throw new Error('Missing OpenRouter API key')
  }

  try {
    const response = await axios.post<OpenRouterResponse>(
      OPENROUTER_API_URL,
      request,
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'HTTP-Referer': siteUrl || 'https://localhost:5173',
          'X-Title': siteName || 'Video Processing App',
          'Content-Type': 'application/json',
        },
      }
    )

    return response.data
  } catch (error) {
    console.error('OpenRouter API Error:', error)
    throw error
  }
}

// Available models on OpenRouter
export const AVAILABLE_MODELS = {
  // Claude models (Anthropic)
  'claude-opus': 'anthropic/claude-3-opus',
  'claude-sonnet': 'anthropic/claude-3.5-sonnet',
  'claude-haiku': 'anthropic/claude-3-haiku',

  // GPT models (OpenAI)
  'gpt-4-turbo': 'openai/gpt-4-turbo',
  'gpt-4': 'openai/gpt-4',
  'gpt-3.5-turbo': 'openai/gpt-3.5-turbo',

  // Gemini models (Google)
  'gemini-pro': 'google/gemini-pro-1.5',
  'gemini-flash': 'google/gemini-flash-1.5',

  // Other models
  'llama-3.1-70b': 'meta-llama/llama-3.1-70b-instruct',
  'mistral-large': 'mistralai/mistral-large',
}

export type ModelKey = keyof typeof AVAILABLE_MODELS
```

### 3. AI Agent Types (`src/types/ai-agents.ts`)

```typescript
export type PhaseNumber = 2 | 3 | 4 | 5

export interface AgentConfig {
  phase: PhaseNumber
  modelKey: string
  temperature: number
  maxTokens: number
  systemPrompt: string
}

export interface ProcessingJob {
  videoId: string
  videoTitle: string
  phase: PhaseNumber
  transcription?: string
  previousPhaseOutput?: string
  agentConfig: AgentConfig
}

export interface ProcessingResult {
  success: boolean
  output?: string
  error?: string
  tokensUsed?: number
  cost?: number
  processingTime?: number
  model?: string
}

export const DEFAULT_AGENT_CONFIGS: Record<PhaseNumber, AgentConfig> = {
  2: {
    phase: 2,
    modelKey: 'claude-sonnet',
    temperature: 0.3,
    maxTokens: 8000,
    systemPrompt: 'You are an expert entity extraction AI.',
  },
  3: {
    phase: 3,
    modelKey: 'gpt-4-turbo',
    temperature: 0.5,
    maxTokens: 6000,
    systemPrompt: 'You are an expert knowledge gap analyst.',
  },
  4: {
    phase: 4,
    modelKey: 'claude-opus',
    temperature: 0.4,
    maxTokens: 10000,
    systemPrompt: 'You are an expert knowledge integrator.',
  },
  5: {
    phase: 5,
    modelKey: 'gpt-4-turbo',
    temperature: 0.6,
    maxTokens: 8000,
    systemPrompt: 'You are an expert knowledge mapper.',
  },
}
```

### 4. AI Agent Orchestration (`src/lib/ai-agents.ts`)

```typescript
import { callOpenRouter, AVAILABLE_MODELS } from './openrouter'
import { supabase } from './supabase'
import { ProcessingJob, ProcessingResult, PhaseNumber } from '@/types/ai-agents'
import { PHASE_PROMPTS } from '@/prompts'

export async function processVideoPhase(job: ProcessingJob): Promise<ProcessingResult> {
  const startTime = Date.now()

  try {
    // Get prompt template for this phase
    const promptTemplate = PHASE_PROMPTS[job.phase]

    // Prepare input based on phase
    let inputContent = ''
    if (job.phase === 2) {
      // Phase 2: Use transcription
      inputContent = job.transcription || ''
    } else {
      // Phase 3-5: Use previous phase output
      inputContent = job.previousPhaseOutput || ''
    }

    if (!inputContent) {
      throw new Error(`Missing input for phase ${job.phase}`)
    }

    // Build prompt
    const userPrompt = promptTemplate.replace('{{INPUT}}', inputContent)

    // Call OpenRouter API
    const response = await callOpenRouter({
      model: AVAILABLE_MODELS[job.agentConfig.modelKey as keyof typeof AVAILABLE_MODELS],
      messages: [
        { role: 'system', content: job.agentConfig.systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      temperature: job.agentConfig.temperature,
      max_tokens: job.agentConfig.maxTokens,
    })

    const output = response.choices[0]?.message?.content || ''
    const tokensUsed = response.usage.total_tokens
    const processingTime = Math.round((Date.now() - startTime) / 1000)

    // Calculate cost (approximate pricing)
    const cost = calculateCost(response.model, tokensUsed)

    // Log AI usage to database
    await logAIUsage({
      videoId: job.videoId,
      phase: job.phase,
      model: response.model,
      tokensUsed,
      cost,
      processingTime,
    })

    // Update video_progress table
    await updateVideoProgress({
      videoId: job.videoId,
      phase: job.phase,
      status: 'Completed',
      output,
      model: response.model,
      cost,
      processingTime,
    })

    // For Phase 2, save extracted entities
    if (job.phase === 2) {
      await saveExtractedEntities(job.videoId, output)
    }

    return {
      success: true,
      output,
      tokensUsed,
      cost,
      processingTime,
      model: response.model,
    }
  } catch (error) {
    const processingTime = Math.round((Date.now() - startTime) / 1000)
    const errorMessage = error instanceof Error ? error.message : 'Unknown error'

    // Update video_progress with error
    await updateVideoProgress({
      videoId: job.videoId,
      phase: job.phase,
      status: 'Failed',
      error: errorMessage,
      processingTime,
    })

    return {
      success: false,
      error: errorMessage,
      processingTime,
    }
  }
}

async function logAIUsage(data: {
  videoId: string
  phase: PhaseNumber
  model: string
  tokensUsed: number
  cost: number
  processingTime: number
}) {
  await supabase.from('ai_api_usage').insert([{
    video_id: data.videoId,
    phase: data.phase,
    ai_provider: getProviderFromModel(data.model),
    model_name: data.model,
    tokens_used: data.tokensUsed,
    estimated_cost: data.cost,
    request_timestamp: new Date().toISOString(),
    response_time_ms: data.processingTime * 1000,
    status: 'success',
  }])
}

async function updateVideoProgress(data: {
  videoId: string
  phase: PhaseNumber
  status: 'Completed' | 'Failed'
  output?: string
  error?: string
  model?: string
  cost?: number
  processingTime?: number
}) {
  const updates: any = {
    phase_status: data.status,
    updated_at: new Date().toISOString(),
  }

  if (data.status === 'Completed') {
    updates.completed_at = new Date().toISOString()
    updates.output_file = data.output
    updates.ai_model_used = data.model
    updates.ai_cost = data.cost
    updates.processing_time_seconds = data.processingTime
  } else {
    updates.error_log = data.error
    updates.retry_count = supabase.rpc('increment', { x: 1 })
  }

  await supabase
    .from('video_progress')
    .update(updates)
    .eq('video_id', data.videoId)
    .eq('phase', data.phase)
}

async function saveExtractedEntities(videoId: string, output: string) {
  // Parse JSON output from Phase 2 (assumes structured JSON response)
  try {
    const entities = JSON.parse(output)

    // Insert each entity
    for (const entity of entities) {
      await supabase.from('extracted_entities').insert([{
        video_id: videoId,
        entity_type: entity.type,
        entity_name: entity.name,
        entity_value: entity.value,
        context_snippet: entity.context,
        confidence_score: entity.confidence || 0.8,
        source_timestamp: entity.timestamp,
      }])
    }
  } catch (error) {
    console.error('Failed to parse extracted entities:', error)
  }
}

function calculateCost(model: string, tokens: number): number {
  // Approximate pricing per 1M tokens
  const pricing: Record<string, { input: number; output: number }> = {
    'anthropic/claude-3-opus': { input: 15, output: 75 },
    'anthropic/claude-3.5-sonnet': { input: 3, output: 15 },
    'anthropic/claude-3-haiku': { input: 0.25, output: 1.25 },
    'openai/gpt-4-turbo': { input: 10, output: 30 },
    'openai/gpt-4': { input: 30, output: 60 },
    'openai/gpt-3.5-turbo': { input: 0.5, output: 1.5 },
    'google/gemini-pro-1.5': { input: 1.25, output: 5 },
    'google/gemini-flash-1.5': { input: 0.075, output: 0.3 },
  }

  const modelPricing = pricing[model] || { input: 1, output: 2 }
  // Assume 50/50 split for simplicity
  const avgPrice = (modelPricing.input + modelPricing.output) / 2
  return (tokens / 1000000) * avgPrice
}

function getProviderFromModel(model: string): string {
  if (model.includes('anthropic')) return 'Anthropic'
  if (model.includes('openai')) return 'OpenAI'
  if (model.includes('google')) return 'Google'
  if (model.includes('meta-llama')) return 'Meta'
  if (model.includes('mistral')) return 'Mistral'
  return 'Unknown'
}
```

### 5. Phase Prompts (`src/prompts/index.ts`)

```typescript
export const PHASE_PROMPTS: Record<number, string> = {
  2: `You are an expert entity extraction AI. Your task is to extract structured entities from video transcriptions.

TRANSCRIPTION:
{{INPUT}}

INSTRUCTIONS:
Extract the following entity types:
1. **People**: Names, roles, organizations
2. **Concepts**: Key ideas, theories, frameworks
3. **Tools/Technologies**: Software, platforms, methodologies
4. **Metrics**: Numbers, statistics, KPIs mentioned
5. **Dates/Events**: Important dates, events, milestones
6. **Actionable Insights**: Recommendations, best practices

OUTPUT FORMAT (JSON):
[
  {
    "type": "person|concept|tool|metric|date|insight",
    "name": "Entity name",
    "value": "Detailed value/description",
    "context": "Surrounding context from transcription",
    "timestamp": "00:00 (if available)",
    "confidence": 0.0-1.0
  }
]

Respond ONLY with valid JSON. Be thorough and accurate.`,

  3: `You are an expert knowledge gap analyst. Your task is to identify missing information and knowledge gaps.

EXTRACTED ENTITIES:
{{INPUT}}

INSTRUCTIONS:
Analyze the extracted entities and identify:
1. **Missing Context**: What background information is assumed but not explained?
2. **Unexplored Topics**: Related areas that were mentioned but not fully explored
3. **Contradictions**: Any conflicting statements or unclear points
4. **Follow-up Questions**: Questions a researcher should investigate further
5. **Source Validation**: Claims that need citation or verification

OUTPUT FORMAT (Markdown):
## Knowledge Gaps Analysis

### Missing Context
- [List gaps]

### Unexplored Topics
- [List topics]

### Contradictions
- [List issues]

### Follow-up Questions
1. [Question 1]
2. [Question 2]

### Source Validation Needed
- [List claims requiring verification]

Be critical and thorough. Highlight areas requiring deeper research.`,

  4: `You are an expert knowledge integrator. Your task is to integrate new knowledge with existing research.

GAP ANALYSIS:
{{INPUT}}

INSTRUCTIONS:
Based on the gap analysis, create an integration plan:
1. **Connections**: How does this knowledge connect to existing research?
2. **New Insights**: What novel insights emerge from this integration?
3. **Updated Frameworks**: How should existing frameworks be updated?
4. **Research Priorities**: What should be researched next?
5. **Action Items**: Concrete next steps for knowledge base updates

OUTPUT FORMAT (Markdown):
## Knowledge Integration Plan

### Connections to Existing Research
- [List connections]

### New Insights
- [List insights]

### Framework Updates
- [Framework 1]: [Updates needed]
- [Framework 2]: [Updates needed]

### Research Priorities
1. [Priority 1]
2. [Priority 2]

### Action Items
- [ ] [Action 1]
- [ ] [Action 2]

Provide actionable recommendations for knowledge base improvement.`,

  5: `You are an expert knowledge mapper. Your task is to create structured knowledge maps and relationship diagrams.

INTEGRATION PLAN:
{{INPUT}}

INSTRUCTIONS:
Create a comprehensive knowledge map:
1. **Concept Hierarchy**: Main concepts and subconcepts
2. **Relationships**: How concepts relate to each other
3. **Dependencies**: Prerequisites and dependencies
4. **Applications**: Where and how this knowledge applies
5. **Visual Map**: Mermaid diagram of knowledge structure

OUTPUT FORMAT (Markdown with Mermaid):
## Knowledge Map

### Concept Hierarchy
\`\`\`
- Main Concept 1
  - Subconcept 1.1
  - Subconcept 1.2
- Main Concept 2
  - Subconcept 2.1
\`\`\`

### Relationships
- [Concept A] → [influences] → [Concept B]
- [Concept C] ← [derived from] ← [Concept D]

### Dependencies
- To understand [X], must first know [Y]

### Applications
- **Industry**: [Application]
- **Research**: [Application]

### Visual Map (Mermaid)
\`\`\`mermaid
graph TD
    A[Main Concept] --> B[Subconcept 1]
    A --> C[Subconcept 2]
    B --> D[Application 1]
    C --> E[Application 2]
\`\`\`

Create a clear, structured map for easy knowledge navigation.`,
}
```

---

## Key Components

### 1. Transcription Uploader (`src/components/transcription/TranscriptionUploader.tsx`)

```typescript
import { useState } from 'react'
import { useDropzone } from 'react-dropzone'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Upload, FileText, CheckCircle } from 'lucide-react'
import { supabase } from '@/lib/supabase'
import { useVideoQueue } from '@/lib/queries'

export function TranscriptionUploader() {
  const [selectedVideoId, setSelectedVideoId] = useState('')
  const [transcriptionText, setTranscriptionText] = useState('')
  const [uploading, setUploading] = useState(false)
  const { data: videos } = useVideoQueue()

  const onDrop = async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0]
    if (!file) return

    const text = await file.text()
    setTranscriptionText(text)
  }

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'text/plain': ['.txt'], 'text/markdown': ['.md'] },
    multiple: false,
  })

  const handleUpload = async () => {
    if (!selectedVideoId || !transcriptionText) return

    setUploading(true)

    try {
      // Create video_progress entry for Phase 1
      await supabase.from('video_progress').insert([{
        video_id: selectedVideoId,
        phase: 1,
        phase_status: 'Completed',
        output_file: transcriptionText,
        completed_at: new Date().toISOString(),
      }])

      // Update video status
      await supabase
        .from('video_queue')
        .update({ status: 'Transcribing' })
        .eq('id', selectedVideoId)

      alert('Transcription uploaded successfully!')
      setTranscriptionText('')
      setSelectedVideoId('')
    } catch (error) {
      console.error('Upload error:', error)
      alert('Failed to upload transcription')
    } finally {
      setUploading(false)
    }
  }

  const selectedVideos = videos?.filter(v => v.status === 'Selected')

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Upload className="h-5 w-5" />
          Upload Transcription
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div>
          <Label htmlFor="video-select">Select Video</Label>
          <Select value={selectedVideoId} onValueChange={setSelectedVideoId}>
            <SelectTrigger>
              <SelectValue placeholder="Choose a video" />
            </SelectTrigger>
            <SelectContent>
              {selectedVideos?.map(video => (
                <SelectItem key={video.id} value={video.id}>
                  {video.video_title}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
            isDragActive ? 'border-primary bg-primary/10' : 'border-gray-300'
          }`}
        >
          <input {...getInputProps()} />
          <FileText className="mx-auto h-12 w-12 text-gray-400 mb-4" />
          {isDragActive ? (
            <p>Drop the transcription file here...</p>
          ) : (
            <div>
              <p className="font-medium">Drag & drop transcription file</p>
              <p className="text-sm text-gray-500">or click to browse (.txt, .md)</p>
            </div>
          )}
        </div>

        {transcriptionText && (
          <div className="rounded-lg bg-green-50 p-4 flex items-center gap-2">
            <CheckCircle className="h-5 w-5 text-green-600" />
            <span className="text-sm text-green-800">
              Transcription loaded ({transcriptionText.length} characters)
            </span>
          </div>
        )}

        <Button
          onClick={handleUpload}
          disabled={!selectedVideoId || !transcriptionText || uploading}
          className="w-full"
        >
          {uploading ? 'Uploading...' : 'Upload Transcription'}
        </Button>
      </CardContent>
    </Card>
  )
}
```

### 2. Video Processing Dashboard (`src/pages/VideoProcessing.tsx`)

```typescript
import { useState } from 'react'
import { useVideoQueue, useVideoProgress } from '@/lib/queries'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Play, Pause, SkipForward } from 'lucide-react'
import { processVideoPhase } from '@/lib/ai-agents'
import { DEFAULT_AGENT_CONFIGS } from '@/types/ai-agents'

export function VideoProcessing() {
  const { data: videos } = useVideoQueue()
  const [processing, setProcessing] = useState<Record<string, boolean>>({})

  const transcribedVideos = videos?.filter(v => v.status === 'Transcribing')

  const handleProcessPhase = async (videoId: string, phase: 2 | 3 | 4 | 5) => {
    setProcessing(prev => ({ ...prev, [videoId]: true }))

    try {
      // Get transcription or previous phase output
      const { data: progressData } = await supabase
        .from('video_progress')
        .select('output_file')
        .eq('video_id', videoId)
        .eq('phase', phase - 1)
        .single()

      const video = videos?.find(v => v.id === videoId)

      if (!progressData || !video) {
        throw new Error('Missing data')
      }

      const result = await processVideoPhase({
        videoId,
        videoTitle: video.video_title,
        phase,
        transcription: phase === 2 ? progressData.output_file : undefined,
        previousPhaseOutput: phase > 2 ? progressData.output_file : undefined,
        agentConfig: DEFAULT_AGENT_CONFIGS[phase],
      })

      if (result.success) {
        alert(`Phase ${phase} completed successfully!`)
      } else {
        alert(`Phase ${phase} failed: ${result.error}`)
      }
    } catch (error) {
      console.error('Processing error:', error)
      alert('Failed to process phase')
    } finally {
      setProcessing(prev => ({ ...prev, [videoId]: false }))
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Video Processing</h1>

      <div className="grid gap-6">
        {transcribedVideos?.map(video => (
          <Card key={video.id}>
            <CardHeader>
              <CardTitle>{video.video_title}</CardTitle>
              <p className="text-sm text-muted-foreground">{video.channel_name}</p>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="phase2">
                <TabsList className="grid w-full grid-cols-4">
                  <TabsTrigger value="phase2">Phase 2</TabsTrigger>
                  <TabsTrigger value="phase3">Phase 3</TabsTrigger>
                  <TabsTrigger value="phase4">Phase 4</TabsTrigger>
                  <TabsTrigger value="phase5">Phase 5</TabsTrigger>
                </TabsList>

                {([2, 3, 4, 5] as const).map(phase => (
                  <TabsContent key={phase} value={`phase${phase}`} className="space-y-4">
                    <div>
                      <h3 className="font-medium mb-2">
                        Phase {phase}: {getPhaseName(phase)}
                      </h3>
                      <Button
                        onClick={() => handleProcessPhase(video.id, phase)}
                        disabled={processing[video.id]}
                      >
                        <Play className="mr-2 h-4 w-4" />
                        {processing[video.id] ? 'Processing...' : `Start Phase ${phase}`}
                      </Button>
                    </div>
                  </TabsContent>
                ))}
              </Tabs>
            </CardContent>
          </Card>
        ))}

        {transcribedVideos?.length === 0 && (
          <Card>
            <CardContent className="py-12 text-center text-muted-foreground">
              No videos ready for processing. Upload transcriptions first.
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  )
}

function getPhaseName(phase: number): string {
  const names: Record<number, string> = {
    2: 'Entity Extraction',
    3: 'Gap Analysis',
    4: 'Integration',
    5: 'Knowledge Mapping',
  }
  return names[phase] || 'Unknown'
}
```

### 3. Workflow Visualization (`src/components/workflow/WorkflowVisualization.tsx`)

```typescript
import ReactFlow, { Node, Edge, Background, Controls } from 'reactflow'
import 'reactflow/dist/style.css'

const nodes: Node[] = [
  { id: '0', position: { x: 100, y: 0 }, data: { label: 'Phase 0: Search' }, type: 'input' },
  { id: '1', position: { x: 100, y: 100 }, data: { label: 'Phase 1: Transcription' } },
  { id: '2', position: { x: 100, y: 200 }, data: { label: 'Phase 2: Extraction' } },
  { id: '3', position: { x: 100, y: 300 }, data: { label: 'Phase 3: Gap Analysis' } },
  { id: '4', position: { x: 100, y: 400 }, data: { label: 'Phase 4: Integration' } },
  { id: '5', position: { x: 100, y: 500 }, data: { label: 'Phase 5: Mapping' } },
  { id: '6', position: { x: 100, y: 600 }, data: { label: 'Complete' }, type: 'output' },
]

const edges: Edge[] = [
  { id: 'e0-1', source: '0', target: '1', animated: true },
  { id: 'e1-2', source: '1', target: '2', animated: true },
  { id: 'e2-3', source: '2', target: '3', animated: true },
  { id: 'e3-4', source: '3', target: '4', animated: true },
  { id: 'e4-5', source: '4', target: '5', animated: true },
  { id: 'e5-6', source: '5', target: '6', animated: true },
]

export function WorkflowVisualization() {
  return (
    <div style={{ height: '600px' }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  )
}
```

---

## Features Checklist

### Core Features
- ✅ Transcription uploader (drag & drop .txt/.md files)
- ✅ OpenRouter API integration (multi-AI provider support)
- ✅ Phase 2-5 AI agent processing
- ✅ Real-time progress tracking
- ✅ Cost tracking and API usage logging
- ✅ Error handling and retry mechanism
- ✅ Agent configuration (model selection, temperature, tokens)
- ✅ Workflow visualization with React Flow
- ✅ Processing dashboard with status indicators
- ✅ Report generation and export

### Advanced Features
- 📊 Cost analytics and budget tracking
- 🔄 Batch processing (process multiple videos)
- 🎨 Customizable AI prompts per phase
- 📁 File download (processed outputs)
- 🔔 Progress notifications
- 📈 Performance metrics (processing time, token usage)
- 🧪 A/B testing (compare different models)
- 🔍 Semantic search on extracted entities

---

## Deployment to Vercel

Same as Queue Management app:

```bash
vercel
```

Add environment variables in Vercel dashboard:
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_OPENROUTER_API_KEY`
- `VITE_OPENROUTER_SITE_URL`
- `VITE_OPENROUTER_SITE_NAME`

Then deploy to production:

```bash
vercel --prod
```

---

## Testing Workflow

1. **Upload Transcription:**
   - Select video from Queue Management app (status: "Selected")
   - Upload .txt transcription file
   - Verify Phase 1 completed in `video_progress` table

2. **Process Phase 2 (Extraction):**
   - Start Phase 2 processing
   - Wait for AI response (30-60 seconds)
   - Check `extracted_entities` table for results
   - Verify `ai_api_usage` logged

3. **Process Phase 3-5:**
   - Process each phase sequentially
   - Verify outputs stored in `video_progress`
   - Check cost tracking

4. **Generate Report:**
   - View final knowledge map
   - Export Markdown report
   - Download all phase outputs

---

## Cost Management

OpenRouter pricing varies by model. Estimated costs per video:

| Phase | Model | Est. Tokens | Est. Cost |
|-------|-------|-------------|-----------|
| Phase 2 | Claude Sonnet | 8,000 | $0.14 |
| Phase 3 | GPT-4 Turbo | 6,000 | $0.24 |
| Phase 4 | Claude Opus | 10,000 | $0.45 |
| Phase 5 | GPT-4 Turbo | 8,000 | $0.32 |
| **Total** | | **32,000** | **~$1.15** |

**Budget recommendations:**
- Start with $10 credit (processes ~8 videos)
- Monitor `ai_api_usage` table regularly
- Set spending alerts in OpenRouter dashboard

---

## Troubleshooting

### Issue: "OpenRouter API Error 401"
**Solution:** Check `VITE_OPENROUTER_API_KEY` is correct and account has funds.

### Issue: "Rate limit exceeded"
**Solution:** OpenRouter has rate limits. Add delay between requests or upgrade plan.

### Issue: "Missing input for phase X"
**Solution:** Ensure previous phase completed successfully. Check `video_progress` table.

### Issue: Phase processing hangs
**Solution:** Check browser console for errors. Increase `max_tokens` if output truncated.

---

## Next Steps

1. **Add Batch Processing:**
   - Process multiple videos in parallel
   - Queue management system
   - Progress indicators for all videos

2. **Enhance Prompts:**
   - Create prompt template library
   - A/B test different prompts
   - User-editable system prompts

3. **Add Semantic Search:**
   - Generate embeddings for entities
   - Vector search UI
   - Related entity discovery

4. **Build Knowledge Graph:**
   - Visualize entity relationships
   - Interactive graph explorer
   - Export to Neo4j or similar

---

## Resources

- **OpenRouter Docs:** https://openrouter.ai/docs
- **React Flow:** https://reactflow.dev
- **Supabase Real-time:** https://supabase.com/docs/guides/realtime
- **shadcn/ui:** https://ui.shadcn.com

---

**End of Prompt 3: Video Processing Web App**

This prompt provides complete instructions for building the Video Processing application with AI agent orchestration, multi-phase workflow, cost tracking, and OpenRouter integration. Copy this entire prompt to an AI builder to generate the full application.