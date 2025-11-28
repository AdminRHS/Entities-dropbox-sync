# Lovable Initiation Phrases

**Quick start prompts for building the Research Management System**

---

## Option 1: Queue Management App (Recommended First)

```
Build a Queue Management Web App for video research using the complete spec below.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Query + Recharts

Key features:
- Video queue dashboard with filters (Status, Department, Priority)
- Search queue management
- Real-time updates via Supabase
- AdminRHS-AI-Catalog design system (friendly blue theme)
- Filter panel, search bar, expandable cards

Database: Supabase with tables: video_queue, search_queue, video_progress, employees

Follow the complete implementation prompt below ⬇️
```

---

## Option 2: Video Processing App (More Complex)

```
Build a Video Processing Web App for AI-powered transcription analysis using the complete spec below.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Query + React Flow + OpenRouter API

Key features:
- 5-phase workflow (Transcription → Extraction → Gap Analysis → Integration → Mapping)
- Multi-AI orchestration (Claude Sonnet, GPT-4, Gemini Pro)
- Entity extraction with gap analysis (NEW/EXISTING/UPDATE detection)
- Automated ID scanning and safe JSON updates with backup/rollback
- Progress tracking with phase auto-advancement
- Cost tracking and batch processing

Database: Supabase with tables: video_progress, extracted_entities, knowledge_gaps, ai_api_usage

Follow the complete implementation prompt below ⬇️
```

---

## Option 3: Both Apps (Full System)

```
Build a 2-app Research Management System using the complete specs below.

App 1: Queue Management (Phase 0 - Search & Selection)
- Video discovery and prioritization
- Search queue management
- Team collaboration dashboard

App 2: Video Processing (Phases 1-5 - Transcription to Mapping)
- AI-powered entity extraction
- Gap analysis and integration
- Knowledge mapping with multi-model orchestration

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + OpenRouter API

Shared: AdminRHS-AI-Catalog design system, real-time Supabase updates

Build App 1 first, then App 2. Follow the complete implementation prompts below ⬇️
```

---

## Usage Instructions

1. **Copy** one of the initiation phrases above
2. **Paste** into Lovable chat
3. **Follow with** the complete prompt file:
   - For Queue Management: Copy entire `02_Queue_Management_Web_App_Prompt.md`
   - For Video Processing: Copy entire `03_Video_Processing_Web_App_Prompt.md`
   - For Both: Copy both prompts in sequence

---

## Pro Tips for Lovable

- **Start with Queue Management** - Simpler, no AI integration, good for testing design system
- **One feature at a time** - Don't try to build everything in one prompt
- **Reference design system** - "Use the AdminRHS-AI-Catalog colors and icons specified"
- **Iterate gradually** - Build core features first, add automation logic later
- **Test Supabase connection early** - Verify database schema is set up correctly

---

**Recommended Build Order:**

1. ✅ Queue Management App (1-2 days with Lovable)
   - Basic UI with design system
   - Supabase connection
   - Filter panel and search
   - Video queue table
   - Add/edit functionality

2. ✅ Video Processing App (3-5 days with Lovable)
   - Phase workflow UI
   - OpenRouter integration
   - Entity extraction interface
   - Gap analysis viewer
   - Progress tracking
   - Automation logic (ID scanner, safe updates)

---

**Created:** 2025-11-28
**Purpose:** Quick initiation for Lovable AI builder
