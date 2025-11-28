# Queue Management Web App - Complete Implementation Prompt

## Overview

Build a **Queue Management Web Application** for managing research video queues and search queries. This is Part 1 of a 2-app Research Management System. The app provides a centralized dashboard for team collaboration, video prioritization, and search queue management.

**Technology Stack:**
- React 18 + TypeScript
- Vite (build tool)
- Supabase (PostgreSQL database + real-time subscriptions)
- shadcn/ui (component library)
- TanStack Query (data fetching)
- TanStack Table (data grids)
- Recharts (charts/visualizations)
- Tailwind CSS (styling)

**Database:** Uses the Supabase PostgreSQL schema from `01_Supabase_Database_Schema_Prompt.md`

---

## 🎨 Design System Integration

### Using Existing RHS Design Assets

This app uses the **AdminRHS-AI-Catalog** design system created by the Design Department. The design system provides a complete UI toolkit with a friendly, educational aesthetic optimized for catalog/dashboard applications

### Available SVG Icons (Inline - Ready to Use)
- ✅ `search.svg` - Search functionality
- ✅ `filter.svg` - Filter panels
- ✅ `upload.svg` - File upload areas
- ✅ `edit.svg` - Edit buttons
- ✅ `create.svg` - Create new items
- ✅ `ai.svg` - AI-related features
- ✅ `lightning.svg` - Priority/quick actions
- ✅ `diamond.svg` - Premium features
- ✅ `moon.svg` / `sun.svg` - Dark/light mode toggle
- ✅ `lock.svg` - Permissions/security

**Icon Code Example**:
```typescript
// Use existing SVG icons from AdminRHS-AI-Catalog
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <path d="M11 18C14.866 18 18 14.866 18 11C18 7.13401 14.866 4 11 4C7.13401 4 4 7.13401 4 11C4 14.866 7.13401 18 11 18Z" stroke="#6A8EA9" stroke-width="2"/>
  <path d="M20 20L17 17" stroke="#6A8EA9" stroke-width="2" stroke-linecap="round"/>
</svg>
```

### Color Palette (From AdminRHS-AI-Catalog)

**Light Mode**:
```css
--background: #f5f5f5;
--foreground: #2d465d;          /* Soft cool black */
--card: #ffffff;
--card-foreground: #2a4054;
--border: rgba(0, 0, 0, 0.08);
--muted-foreground: #3d5268;    /* Secondary text */
--destructive: #d4183d;
--accent-blue: #428eb4;
--accent-blue-hover: #28749b;
--accent-blue-light: #83CBFF;
```

**Dark Mode**:
```css
--background: #1a1a1a;
--foreground: #e0e0e0;
--card: #2d2d2d;
--card-foreground: #e0e0e0;
--border: rgba(248, 62, 62, 0.1);
--muted-foreground: #b0b0b0;
```

### UI Patterns to Reuse

1. **Filter Panel** (From AdminRHS-AI-Catalog)
   - Left-side collapsible panel
   - Multi-select pill buttons
   - Active filters display with removable tags
   - "Clear All" button (enabled only when filters active)

2. **Search Bar** (From AdminRHS-AI-Catalog)
   - Expands on hover/focus
   - Search icon on left
   - Smooth transitions (0.2-0.3s ease)

3. **Card Layout** (From AdminRHS-AI-Catalog)
   - Expandable cards (click title to expand)
   - "+N more" button for additional items
   - Blue shadow on hover
   - Consistent spacing and alignment

### Implementation Strategy

Build using the AdminRHS-AI-Catalog design patterns described above:

1. **Filter Panel:** Left-side collapsible with pill buttons for Status (Pending/Selected/Completed), Department (VID/AID/DEV/ALL), Priority (High/Medium/Low)
2. **Search Bar:** Expandable input with search icon, filters video titles and channels
3. **Card Layout:** Display queue items as cards with hover effects (blue shadow), expandable details
4. **Icons:** Use inline SVG code provided above for all UI elements

---

## 📋 Research Workflow Context

### Video Transcript Processing Pipeline

This Queue Management App is **Part 1** of a larger video research workflow used by Remote Helpers to extract development tools and workflows from video content.

**Complete 7-Phase Workflow:**

| Phase | Name | Description | Handled By |
|-------|------|-------------|------------|
| **Phase 0** | Search & Selection | Identify relevant videos based on daily work tasks | **This App** (Queue Management) |
| **Phase 1** | Transcription | Upload video transcriptions | Video Processing App |
| **Phase 2** | Entity Extraction | AI extracts tools, workflows, actions | Video Processing App |
| **Phase 3** | Gap Analysis | Identify missing information | Video Processing App |
| **Phase 4** | Integration | Integrate with knowledge base | Video Processing App |
| **Phase 5** | Mapping | Create knowledge maps | Video Processing App |
| **Complete** | Final Review | Human review and approval | Video Processing App |

**Phase 0 Details** (handled by this app):

1. **Process Daily Reports** - Extract tasks and processes from team daily.md files
2. **Create Search Prompts** - Generate Perplexity AI prompts for tool discovery
3. **Search Fresh Videos** - Find relevant YouTube videos (last 30 days, popular content)
4. **Collect & Prioritize** - Add videos to queue, assign priority scores

**Tools Used in Phase 0:**
- Perplexity AI (video search with specific settings: Creativity 0.5, Structure mode)
- YouTube (source platform)
- This Queue Management App (tracking and prioritization)

**Output:** Curated list of videos ready for transcription (Phase 1)

**Workflow Summary:** This is a task-driven discovery process. Daily work reports identify current team challenges → Perplexity searches find videos demonstrating solutions → Videos are added to queue with priority scores based on relevance to active projects → Selected videos move to Phase 1 (Transcription) in the Video Processing app

---

## 🏗️ Entity Taxonomy Integration

### Task Manager System

This app integrates with Remote Helpers' **Entity Hierarchy** for tracking research activities:

```
PRT (Project Templates) - Multi-week research initiatives
  ├─→ MLT (Milestone Templates) - Research phases
       ├─→ TST (Task Templates) - Individual video processing tasks
            └─→ STT (Step Templates) - Granular actions (search, prioritize, assign)
```

**Entity ID Format:** `XXX-###` (e.g., TST-042, MLT-006, PRT-003)
- **XXX:** 3 consonants (PRT, MLT, TST, STT, TOL, GDS, PMT)
- **###:** 3 digits, zero-padded (001, 042, 153)

**Examples for Research Queue Management:**

| Entity Type | Example ID | Use Case |
|-------------|------------|----------|
| **PRT** | PRT-004 | Video Research Processing Project |
| **MLT** | MLT-010 | Video Discovery & Queue Management |
| **TST** | TST-055 | Search for AI development tools videos |
| **STT** | STT-127 | Create Perplexity search prompt |
| **TOL** | TOL-007 | Tools used (Perplexity, YouTube) |
| **GDS** | GDS-010 | Classification guides |
| **PMT** | PMT-004 to PMT-013 | Video processing prompts |

**Task Status Indicators:**
- ✅ **Completed** - Search completed, videos added to queue
- 🔄 **In Progress** - Actively searching/prioritizing
- 🆕 **New** - Just assigned, not started
- ⏸️ **Blocked** - Waiting on dependency

**Department Codes:**
- **VID** (Video Research) - Primary department for video discovery
- **AID** (AI Development) - AI-powered entity extraction
- **DEV** (Development) - Development tool research
- **ALL** (Cross-department) - Admin/multi-department research

---

## 🛠️ Development Tools Reference

### Tools Available for Research Workflow

The research team uses these tools (relevant to this Queue Management app):

**Primary AI Tools:**

| Tool | Vendor | Purpose | Cost |
|------|--------|---------|------|
| **Claude** | Anthropic | Analysis, automation, MCP integration | API-based |
| **Claude Desktop** | Anthropic | Local AI assistant with MCP connectors | Free app (requires API) |
| **Claude Projects** | Anthropic | Organize workflows with custom knowledge | Included in Pro ($20/month) |
| **Gemini** | Google | Large dataset processing, company research | Free tier + paid |
| **OpenAI GPT-5** | OpenAI | Parsing unstructured data | API-based |

**Automation & Integration:**

| Tool | Purpose | Use Case in Research |
|------|---------|---------------------|
| **n8n** | Workflow automation | Automate video queue processing, notifications |
| **MCP (Model Context Protocol)** | AI-to-app integration | Connect Claude to research databases |
| **Apify** | Web scraping platform | Scrape video metadata, channel info |

**Communication & Collaboration:**

| Tool | Purpose |
|------|---------|
| **Discord** | Team communication, bot notifications |
| **Google Cloud Console** | OAuth for Gmail/Calendar integration |

**Note:** These tools are already in use by Remote Helpers. The Queue Management app tracks which tools are being researched and helps prioritize videos about emerging tools (e.g., new AI models, updated frameworks, better automation platforms)

---

## Prerequisites

Before starting, ensure you have:

1. **Supabase Project:**
   - Created a Supabase project at https://supabase.com
   - Executed all SQL from `01_Supabase_Database_Schema_Prompt.md` in SQL Editor
   - Noted your Project URL and anon public key
   - Enabled real-time for tables: `video_queue`, `search_queue`, `video_progress`

2. **Development Environment:**
   - Node.js 18+ installed
   - Git installed
   - Code editor (VS Code recommended)
   - Modern browser (Chrome/Firefox/Edge)

---

## Project Setup

### 1. Initialize Vite + React + TypeScript Project

```bash
npm create vite@latest queue-management-app -- --template react-ts
cd queue-management-app
npm install
```

### 2. Install Core Dependencies

```bash
# Supabase client
npm install @supabase/supabase-js

# UI Components
npm install @radix-ui/react-slot @radix-ui/react-dialog @radix-ui/react-dropdown-menu @radix-ui/react-select @radix-ui/react-tabs @radix-ui/react-toast @radix-ui/react-label @radix-ui/react-checkbox @radix-ui/react-avatar

# Data fetching and state
npm install @tanstack/react-query @tanstack/react-table

# Charts
npm install recharts

# Utilities
npm install clsx tailwind-merge date-fns lucide-react

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
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
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
queue-management-app/
├── src/
│   ├── components/
│   │   ├── ui/              # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── input.tsx
│   │   │   ├── label.tsx
│   │   │   ├── select.tsx
│   │   │   ├── table.tsx
│   │   │   ├── tabs.tsx
│   │   │   └── toast.tsx
│   │   ├── layout/
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Header.tsx
│   │   │   └── Layout.tsx
│   │   ├── dashboard/
│   │   │   ├── KPICard.tsx
│   │   │   ├── QueueStatusChart.tsx
│   │   │   └── RecentActivity.tsx
│   │   ├── search-queue/
│   │   │   ├── SearchQueueTable.tsx
│   │   │   ├── AddSearchDialog.tsx
│   │   │   └── EditSearchDialog.tsx
│   │   ├── video-queue/
│   │   │   ├── VideoQueueTable.tsx
│   │   │   ├── AddVideoDialog.tsx
│   │   │   ├── EditVideoDialog.tsx
│   │   │   └── PriorityCalculator.tsx
│   │   └── employees/
│   │       ├── EmployeeTable.tsx
│   │       ├── AddEmployeeDialog.tsx
│   │       └── EditEmployeeDialog.tsx
│   ├── lib/
│   │   ├── supabase.ts      # Supabase client
│   │   ├── queries.ts       # React Query hooks
│   │   └── utils.ts         # Utility functions
│   ├── types/
│   │   └── database.ts      # TypeScript types
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── SearchQueue.tsx
│   │   ├── VideoQueue.tsx
│   │   ├── Employees.tsx
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
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-public-key
```

**IMPORTANT:** Replace with your actual Supabase project credentials.

### TypeScript Configuration (`tsconfig.json`)

Update `tsconfig.json`:

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

### 2. Database Types (`src/types/database.ts`)

```typescript
export type Database = {
  public: {
    Tables: {
      employees: {
        Row: {
          id: string
          name: string
          email: string
          department: 'VID' | 'AID' | 'HRM' | 'FIN' | 'MKT' | 'ALL'
          role: 'Researcher' | 'Analyst' | 'Admin'
          active: boolean
          created_at: string
        }
        Insert: Omit<Database['public']['Tables']['employees']['Row'], 'id' | 'created_at'>
        Update: Partial<Database['public']['Tables']['employees']['Insert']>
      }
      search_queue: {
        Row: {
          id: string
          queue_id: string
          search_title: string
          research_topic: string
          department: 'VID' | 'AID' | 'HRM' | 'FIN' | 'MKT' | 'ALL'
          keywords: string[]
          added_by: string | null
          added_date: string
          status: 'Pending' | 'In Progress' | 'Completed' | 'On Hold'
          assigned_to: string | null
          started_date: string | null
          completed_date: string | null
          videos_found: number
          videos_selected: number
          search_notes: string | null
          priority: 'Low' | 'Medium' | 'High' | 'Urgent'
          created_at: string
          updated_at: string
        }
        Insert: Omit<Database['public']['Tables']['search_queue']['Row'], 'id' | 'created_at' | 'updated_at'>
        Update: Partial<Database['public']['Tables']['search_queue']['Insert']>
      }
      video_queue: {
        Row: {
          id: string
          queue_id: string
          video_id: string
          video_title: string
          channel_name: string
          channel_url: string | null
          video_url: string
          views: number
          likes: number
          comments: number
          publish_date: string | null
          duration: string | null
          added_by: string | null
          added_date: string
          status: 'Pending' | 'Selected' | 'Transcribing' | 'Parsed' | 'Completed' | 'Skipped'
          selected_by: string | null
          selected_date: string | null
          parsed_date: string | null
          topic_category: string | null
          research_source: string | null
          priority_score: number
          notes: string | null
          created_at: string
          updated_at: string
        }
        Insert: Omit<Database['public']['Tables']['video_queue']['Row'], 'id' | 'created_at' | 'updated_at'>
        Update: Partial<Database['public']['Tables']['video_queue']['Insert']>
      }
      video_progress: {
        Row: {
          id: string
          video_id: string
          phase: 0 | 1 | 2 | 3 | 4 | 5
          phase_status: 'Not Started' | 'In Progress' | 'Completed' | 'Failed'
          assigned_to: string | null
          started_at: string | null
          completed_at: string | null
          output_file: string | null
          ai_model_used: string | null
          ai_cost: number
          processing_time_seconds: number
          error_log: string | null
          retry_count: number
          created_at: string
          updated_at: string
        }
        Insert: Omit<Database['public']['Tables']['video_progress']['Row'], 'id' | 'created_at' | 'updated_at'>
        Update: Partial<Database['public']['Tables']['video_progress']['Insert']>
      }
    }
  }
}

export type Employee = Database['public']['Tables']['employees']['Row']
export type SearchQueue = Database['public']['Tables']['search_queue']['Row']
export type VideoQueue = Database['public']['Tables']['video_queue']['Row']
export type VideoProgress = Database['public']['Tables']['video_progress']['Row']
```

### 3. React Query Hooks (`src/lib/queries.ts`)

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { supabase } from './supabase'
import type { Employee, SearchQueue, VideoQueue } from '@/types/database'

// ==================== EMPLOYEES ====================

export function useEmployees() {
  return useQuery({
    queryKey: ['employees'],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('employees')
        .select('*')
        .order('name')

      if (error) throw error
      return data as Employee[]
    },
  })
}

export function useAddEmployee() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (employee: Omit<Employee, 'id' | 'created_at'>) => {
      const { data, error } = await supabase
        .from('employees')
        .insert([employee])
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['employees'] })
    },
  })
}

export function useUpdateEmployee() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async ({ id, updates }: { id: string; updates: Partial<Employee> }) => {
      const { data, error } = await supabase
        .from('employees')
        .update(updates)
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['employees'] })
    },
  })
}

export function useDeleteEmployee() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (id: string) => {
      const { error } = await supabase
        .from('employees')
        .delete()
        .eq('id', id)

      if (error) throw error
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['employees'] })
    },
  })
}

// ==================== SEARCH QUEUE ====================

export function useSearchQueue() {
  return useQuery({
    queryKey: ['search-queue'],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('search_queue')
        .select(`
          *,
          added_by_employee:employees!search_queue_added_by_fkey(name),
          assigned_to_employee:employees!search_queue_assigned_to_fkey(name)
        `)
        .order('added_date', { ascending: false })

      if (error) throw error
      return data
    },
  })
}

export function useAddSearchQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (search: Omit<SearchQueue, 'id' | 'created_at' | 'updated_at'>) => {
      const { data, error } = await supabase
        .from('search_queue')
        .insert([search])
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['search-queue'] })
    },
  })
}

export function useUpdateSearchQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async ({ id, updates }: { id: string; updates: Partial<SearchQueue> }) => {
      const { data, error } = await supabase
        .from('search_queue')
        .update({ ...updates, updated_at: new Date().toISOString() })
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['search-queue'] })
    },
  })
}

export function useDeleteSearchQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (id: string) => {
      const { error } = await supabase
        .from('search_queue')
        .delete()
        .eq('id', id)

      if (error) throw error
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['search-queue'] })
    },
  })
}

// ==================== VIDEO QUEUE ====================

export function useVideoQueue() {
  return useQuery({
    queryKey: ['video-queue'],
    queryFn: async () => {
      const { data, error } = await supabase
        .from('video_queue')
        .select(`
          *,
          added_by_employee:employees!video_queue_added_by_fkey(name),
          selected_by_employee:employees!video_queue_selected_by_fkey(name)
        `)
        .order('priority_score', { ascending: false })

      if (error) throw error
      return data
    },
  })
}

export function useAddVideoQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (video: Omit<VideoQueue, 'id' | 'created_at' | 'updated_at'>) => {
      const { data, error } = await supabase
        .from('video_queue')
        .insert([video])
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['video-queue'] })
    },
  })
}

export function useUpdateVideoQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async ({ id, updates }: { id: string; updates: Partial<VideoQueue> }) => {
      const { data, error } = await supabase
        .from('video_queue')
        .update({ ...updates, updated_at: new Date().toISOString() })
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['video-queue'] })
    },
  })
}

export function useDeleteVideoQueue() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (id: string) => {
      const { error } = await supabase
        .from('video_queue')
        .delete()
        .eq('id', id)

      if (error) throw error
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['video-queue'] })
    },
  })
}

// ==================== REAL-TIME SUBSCRIPTIONS ====================

export function useRealtimeSearchQueue() {
  const queryClient = useQueryClient()

  useEffect(() => {
    const channel = supabase
      .channel('search-queue-changes')
      .on(
        'postgres_changes',
        { event: '*', schema: 'public', table: 'search_queue' },
        () => {
          queryClient.invalidateQueries({ queryKey: ['search-queue'] })
        }
      )
      .subscribe()

    return () => {
      supabase.removeChannel(channel)
    }
  }, [queryClient])
}

export function useRealtimeVideoQueue() {
  const queryClient = useQueryClient()

  useEffect(() => {
    const channel = supabase
      .channel('video-queue-changes')
      .on(
        'postgres_changes',
        { event: '*', schema: 'public', table: 'video_queue' },
        () => {
          queryClient.invalidateQueries({ queryKey: ['video-queue'] })
        }
      )
      .subscribe()

    return () => {
      supabase.removeChannel(channel)
    }
  }, [queryClient])
}
```

### 4. Utility Functions (`src/lib/utils.ts`)

```typescript
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatDate(date: string | Date): string {
  return new Date(date).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

export function formatNumber(num: number): string {
  if (num >= 1000000) {
    return `${(num / 1000000).toFixed(1)}M`
  }
  if (num >= 1000) {
    return `${(num / 1000).toFixed(1)}K`
  }
  return num.toString()
}

export function calculatePriorityScore(
  views: number,
  likes: number,
  publishDate: string,
  topicRelevance: number = 0.5
): number {
  const viewScore = Math.min((views / 1000000) * 30, 30)
  const engagementScore = Math.min((likes / 10000) * 20, 20)

  const daysOld = Math.floor(
    (Date.now() - new Date(publishDate).getTime()) / (1000 * 60 * 60 * 24)
  )

  let recencyScore = 10
  if (daysOld <= 30) recencyScore = 25
  else if (daysOld <= 90) recencyScore = 20
  else if (daysOld <= 180) recencyScore = 15

  const relevanceScore = topicRelevance * 25

  return Math.round(viewScore + engagementScore + recencyScore + relevanceScore)
}

export function getStatusColor(status: string): string {
  const colors: Record<string, string> = {
    Pending: 'bg-gray-100 text-gray-800',
    'In Progress': 'bg-blue-100 text-blue-800',
    Selected: 'bg-purple-100 text-purple-800',
    Transcribing: 'bg-yellow-100 text-yellow-800',
    Parsed: 'bg-indigo-100 text-indigo-800',
    Completed: 'bg-green-100 text-green-800',
    Skipped: 'bg-red-100 text-red-800',
    'On Hold': 'bg-orange-100 text-orange-800',
    Failed: 'bg-red-100 text-red-800',
  }
  return colors[status] || 'bg-gray-100 text-gray-800'
}

export function getPriorityColor(priority: string): string {
  const colors: Record<string, string> = {
    Low: 'bg-gray-100 text-gray-800',
    Medium: 'bg-blue-100 text-blue-800',
    High: 'bg-orange-100 text-orange-800',
    Urgent: 'bg-red-100 text-red-800',
  }
  return colors[priority] || 'bg-gray-100 text-gray-800'
}
```

---

## shadcn/ui Components

Install base components using the shadcn CLI (or manually copy from https://ui.shadcn.com):

```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add input
npx shadcn-ui@latest add label
npx shadcn-ui@latest add select
npx shadcn-ui@latest add table
npx shadcn-ui@latest add tabs
npx shadcn-ui@latest add toast
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add checkbox
npx shadcn-ui@latest add avatar
npx shadcn-ui@latest add badge
```

**Note:** If `shadcn-ui` CLI is unavailable, manually copy components from https://ui.shadcn.com/docs/components into `src/components/ui/`.

---

## Layout Components

### Sidebar (`src/components/layout/Sidebar.tsx`)

```typescript
import { Home, Search, Video, Users, Settings } from 'lucide-react'
import { Link, useLocation } from 'react-router-dom'
import { cn } from '@/lib/utils'

const navigation = [
  { name: 'Dashboard', href: '/', icon: Home },
  { name: 'Search Queue', href: '/search-queue', icon: Search },
  { name: 'Video Queue', href: '/video-queue', icon: Video },
  { name: 'Employees', href: '/employees', icon: Users },
  { name: 'Settings', href: '/settings', icon: Settings },
]

export function Sidebar() {
  const location = useLocation()

  return (
    <div className="flex h-screen w-64 flex-col bg-gray-900 text-white">
      <div className="flex h-16 items-center justify-center border-b border-gray-800">
        <h1 className="text-xl font-bold">Research Queue</h1>
      </div>

      <nav className="flex-1 space-y-1 px-3 py-4">
        {navigation.map((item) => {
          const isActive = location.pathname === item.href
          return (
            <Link
              key={item.name}
              to={item.href}
              className={cn(
                'flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-gray-800 text-white'
                  : 'text-gray-400 hover:bg-gray-800 hover:text-white'
              )}
            >
              <item.icon className="h-5 w-5" />
              {item.name}
            </Link>
          )
        })}
      </nav>

      <div className="border-t border-gray-800 p-4">
        <p className="text-xs text-gray-500">Queue Management v1.0</p>
      </div>
    </div>
  )
}
```

### Header (`src/components/layout/Header.tsx`)

```typescript
import { Bell, User } from 'lucide-react'
import { Button } from '@/components/ui/button'

export function Header() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-6">
      <div>
        <h2 className="text-2xl font-semibold text-gray-900">Dashboard</h2>
      </div>

      <div className="flex items-center gap-4">
        <Button variant="ghost" size="icon">
          <Bell className="h-5 w-5" />
        </Button>
        <Button variant="ghost" size="icon">
          <User className="h-5 w-5" />
        </Button>
      </div>
    </header>
  )
}
```

### Layout (`src/components/layout/Layout.tsx`)

```typescript
import { Sidebar } from './Sidebar'
import { Header } from './Header'

interface LayoutProps {
  children: React.ReactNode
}

export function Layout({ children }: LayoutProps) {
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex flex-1 flex-col overflow-hidden">
        <Header />
        <main className="flex-1 overflow-y-auto bg-gray-50 p-6">
          {children}
        </main>
      </div>
    </div>
  )
}
```

---

## Dashboard Page (`src/pages/Dashboard.tsx`)

```typescript
import { useSearchQueue, useVideoQueue } from '@/lib/queries'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { Search, Video, CheckCircle, Clock } from 'lucide-react'

export function Dashboard() {
  const { data: searchQueue } = useSearchQueue()
  const { data: videoQueue } = useVideoQueue()

  const searchStats = {
    total: searchQueue?.length || 0,
    pending: searchQueue?.filter(s => s.status === 'Pending').length || 0,
    inProgress: searchQueue?.filter(s => s.status === 'In Progress').length || 0,
    completed: searchQueue?.filter(s => s.status === 'Completed').length || 0,
  }

  const videoStats = {
    total: videoQueue?.length || 0,
    pending: videoQueue?.filter(v => v.status === 'Pending').length || 0,
    selected: videoQueue?.filter(v => v.status === 'Selected').length || 0,
    completed: videoQueue?.filter(v => v.status === 'Completed').length || 0,
  }

  const chartData = [
    { name: 'Pending', searches: searchStats.pending, videos: videoStats.pending },
    { name: 'In Progress', searches: searchStats.inProgress, videos: videoStats.selected },
    { name: 'Completed', searches: searchStats.completed, videos: videoStats.completed },
  ]

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Dashboard</h1>

      {/* KPI Cards */}
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Total Searches</CardTitle>
            <Search className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{searchStats.total}</div>
            <p className="text-xs text-muted-foreground">
              {searchStats.pending} pending
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Total Videos</CardTitle>
            <Video className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{videoStats.total}</div>
            <p className="text-xs text-muted-foreground">
              {videoStats.pending} pending
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">In Progress</CardTitle>
            <Clock className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{searchStats.inProgress}</div>
            <p className="text-xs text-muted-foreground">
              searches active
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium">Completed</CardTitle>
            <CheckCircle className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{videoStats.completed}</div>
            <p className="text-xs text-muted-foreground">
              videos processed
            </p>
          </CardContent>
        </Card>
      </div>

      {/* Status Chart */}
      <Card>
        <CardHeader>
          <CardTitle>Queue Status Overview</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="searches" fill="#3b82f6" name="Searches" />
              <Bar dataKey="videos" fill="#8b5cf6" name="Videos" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Recent Activity */}
      <Card>
        <CardHeader>
          <CardTitle>Recent Videos</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {videoQueue?.slice(0, 5).map((video) => (
              <div key={video.id} className="flex items-center justify-between border-b pb-2">
                <div className="flex-1">
                  <p className="font-medium">{video.video_title}</p>
                  <p className="text-sm text-muted-foreground">{video.channel_name}</p>
                </div>
                <div className="flex items-center gap-4">
                  <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${
                    video.status === 'Completed' ? 'bg-green-100 text-green-800' :
                    video.status === 'Pending' ? 'bg-gray-100 text-gray-800' :
                    'bg-blue-100 text-blue-800'
                  }`}>
                    {video.status}
                  </span>
                  <span className="text-sm font-medium">Priority: {video.priority_score}</span>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
```

---

## Search Queue Page (`src/pages/SearchQueue.tsx`)

```typescript
import { useState } from 'react'
import { useSearchQueue, useAddSearchQueue, useUpdateSearchQueue, useDeleteSearchQueue } from '@/lib/queries'
import { Button } from '@/components/ui/button'
import { Plus } from 'lucide-react'
import { SearchQueueTable } from '@/components/search-queue/SearchQueueTable'
import { AddSearchDialog } from '@/components/search-queue/AddSearchDialog'

export function SearchQueue() {
  const [isAddDialogOpen, setIsAddDialogOpen] = useState(false)
  const { data: searches, isLoading } = useSearchQueue()

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">Search Queue</h1>
        <Button onClick={() => setIsAddDialogOpen(true)}>
          <Plus className="mr-2 h-4 w-4" />
          Add Search
        </Button>
      </div>

      {isLoading ? (
        <div>Loading...</div>
      ) : (
        <SearchQueueTable data={searches || []} />
      )}

      <AddSearchDialog
        open={isAddDialogOpen}
        onOpenChange={setIsAddDialogOpen}
      />
    </div>
  )
}
```

### Search Queue Table (`src/components/search-queue/SearchQueueTable.tsx`)

```typescript
import { useState } from 'react'
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  getFilteredRowModel,
  flexRender,
  createColumnHelper,
} from '@tanstack/react-table'
import { SearchQueue } from '@/types/database'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { formatDate, getStatusColor, getPriorityColor } from '@/lib/utils'
import { Edit, Trash2 } from 'lucide-react'
import { useDeleteSearchQueue } from '@/lib/queries'

const columnHelper = createColumnHelper<SearchQueue>()

export function SearchQueueTable({ data }: { data: SearchQueue[] }) {
  const [globalFilter, setGlobalFilter] = useState('')
  const deleteSearchMutation = useDeleteSearchQueue()

  const columns = [
    columnHelper.accessor('queue_id', {
      header: 'Queue ID',
      cell: info => <span className="font-mono text-sm">{info.getValue()}</span>,
    }),
    columnHelper.accessor('search_title', {
      header: 'Search Title',
      cell: info => <span className="font-medium">{info.getValue()}</span>,
    }),
    columnHelper.accessor('research_topic', {
      header: 'Topic',
    }),
    columnHelper.accessor('department', {
      header: 'Department',
      cell: info => (
        <span className="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800">
          {info.getValue()}
        </span>
      ),
    }),
    columnHelper.accessor('priority', {
      header: 'Priority',
      cell: info => (
        <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${getPriorityColor(info.getValue())}`}>
          {info.getValue()}
        </span>
      ),
    }),
    columnHelper.accessor('status', {
      header: 'Status',
      cell: info => (
        <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${getStatusColor(info.getValue())}`}>
          {info.getValue()}
        </span>
      ),
    }),
    columnHelper.accessor('videos_found', {
      header: 'Videos Found',
      cell: info => <span className="text-center">{info.getValue()}</span>,
    }),
    columnHelper.accessor('videos_selected', {
      header: 'Selected',
      cell: info => <span className="text-center">{info.getValue()}</span>,
    }),
    columnHelper.accessor('added_date', {
      header: 'Added',
      cell: info => formatDate(info.getValue()),
    }),
    columnHelper.display({
      id: 'actions',
      header: 'Actions',
      cell: ({ row }) => (
        <div className="flex gap-2">
          <Button variant="ghost" size="icon">
            <Edit className="h-4 w-4" />
          </Button>
          <Button
            variant="ghost"
            size="icon"
            onClick={() => deleteSearchMutation.mutate(row.original.id)}
          >
            <Trash2 className="h-4 w-4 text-red-600" />
          </Button>
        </div>
      ),
    }),
  ]

  const table = useReactTable({
    data,
    columns,
    state: {
      globalFilter,
    },
    onGlobalFilterChange: setGlobalFilter,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
  })

  return (
    <div className="space-y-4">
      <Input
        placeholder="Search..."
        value={globalFilter}
        onChange={e => setGlobalFilter(e.target.value)}
        className="max-w-sm"
      />

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map(headerGroup => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map(header => (
                  <TableHead key={header.id}>
                    {flexRender(header.column.columnDef.header, header.getContext())}
                  </TableHead>
                ))}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows.map(row => (
              <TableRow key={row.id}>
                {row.getVisibleCells().map(cell => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}
```

### Add Search Dialog (`src/components/search-queue/AddSearchDialog.tsx`)

```typescript
import { useState } from 'react'
import { useAddSearchQueue, useEmployees } from '@/lib/queries'
import { Button } from '@/components/ui/button'
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

interface AddSearchDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
}

export function AddSearchDialog({ open, onOpenChange }: AddSearchDialogProps) {
  const { data: employees } = useEmployees()
  const addSearchMutation = useAddSearchQueue()

  const [formData, setFormData] = useState({
    queue_id: `SQ${Date.now()}`,
    search_title: '',
    research_topic: '',
    department: 'VID' as const,
    keywords: [] as string[],
    added_by: '',
    added_date: new Date().toISOString().split('T')[0],
    status: 'Pending' as const,
    assigned_to: null as string | null,
    started_date: null as string | null,
    completed_date: null as string | null,
    videos_found: 0,
    videos_selected: 0,
    search_notes: null as string | null,
    priority: 'Medium' as const,
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    addSearchMutation.mutate(formData, {
      onSuccess: () => {
        onOpenChange(false)
        setFormData({
          queue_id: `SQ${Date.now()}`,
          search_title: '',
          research_topic: '',
          department: 'VID',
          keywords: [],
          added_by: '',
          added_date: new Date().toISOString().split('T')[0],
          status: 'Pending',
          assigned_to: null,
          started_date: null,
          completed_date: null,
          videos_found: 0,
          videos_selected: 0,
          search_notes: null,
          priority: 'Medium',
        })
      },
    })
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>Add New Search</DialogTitle>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label htmlFor="search_title">Search Title</Label>
              <Input
                id="search_title"
                value={formData.search_title}
                onChange={e => setFormData({ ...formData, search_title: e.target.value })}
                required
              />
            </div>

            <div>
              <Label htmlFor="research_topic">Research Topic</Label>
              <Input
                id="research_topic"
                value={formData.research_topic}
                onChange={e => setFormData({ ...formData, research_topic: e.target.value })}
                required
              />
            </div>

            <div>
              <Label htmlFor="department">Department</Label>
              <Select
                value={formData.department}
                onValueChange={(value: any) => setFormData({ ...formData, department: value })}
              >
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="VID">VID</SelectItem>
                  <SelectItem value="AID">AID</SelectItem>
                  <SelectItem value="HRM">HRM</SelectItem>
                  <SelectItem value="FIN">FIN</SelectItem>
                  <SelectItem value="MKT">MKT</SelectItem>
                  <SelectItem value="ALL">ALL</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div>
              <Label htmlFor="priority">Priority</Label>
              <Select
                value={formData.priority}
                onValueChange={(value: any) => setFormData({ ...formData, priority: value })}
              >
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Low">Low</SelectItem>
                  <SelectItem value="Medium">Medium</SelectItem>
                  <SelectItem value="High">High</SelectItem>
                  <SelectItem value="Urgent">Urgent</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div>
              <Label htmlFor="added_by">Added By</Label>
              <Select
                value={formData.added_by}
                onValueChange={(value) => setFormData({ ...formData, added_by: value })}
              >
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {employees?.map(emp => (
                    <SelectItem key={emp.id} value={emp.id}>
                      {emp.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div>
              <Label htmlFor="keywords">Keywords (comma-separated)</Label>
              <Input
                id="keywords"
                placeholder="AI, research, video"
                onChange={e => setFormData({
                  ...formData,
                  keywords: e.target.value.split(',').map(k => k.trim())
                })}
              />
            </div>
          </div>

          <div className="flex justify-end gap-2">
            <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>
              Cancel
            </Button>
            <Button type="submit" disabled={addSearchMutation.isPending}>
              {addSearchMutation.isPending ? 'Adding...' : 'Add Search'}
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  )
}
```

---

## Video Queue Page Structure

Similar structure to Search Queue page. Create:

1. **`src/pages/VideoQueue.tsx`** - Main page with table and add button
2. **`src/components/video-queue/VideoQueueTable.tsx`** - TanStack Table with all 21 columns
3. **`src/components/video-queue/AddVideoDialog.tsx`** - Form with priority calculator
4. **`src/components/video-queue/PriorityCalculator.tsx`** - Interactive priority score calculator

The video queue table should include all 21 columns from the database schema, with special handling for:
- Priority score (color-coded badge)
- Status (color-coded badge)
- Video URL (clickable link)
- Views/Likes (formatted with K/M suffixes)
- Publish date (formatted date)

---

## Employees Page Structure

Create employee management page:

1. **`src/pages/Employees.tsx`** - Main page
2. **`src/components/employees/EmployeeTable.tsx`** - Table with CRUD
3. **`src/components/employees/AddEmployeeDialog.tsx`** - Add employee form
4. **`src/components/employees/EditEmployeeDialog.tsx`** - Edit employee form

---

## Main App Setup

### Router Setup (`src/App.tsx`)

```typescript
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Layout } from './components/layout/Layout'
import { Dashboard } from './pages/Dashboard'
import { SearchQueue } from './pages/SearchQueue'
import { VideoQueue } from './pages/VideoQueue'
import { Employees } from './pages/Employees'
import { Settings } from './pages/Settings'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/search-queue" element={<SearchQueue />} />
            <Route path="/video-queue" element={<VideoQueue />} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
```

### Entry Point (`src/main.tsx`)

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

---

## Real-Time Features

Add real-time subscriptions to pages:

```typescript
// In VideoQueue.tsx
import { useRealtimeVideoQueue } from '@/lib/queries'

export function VideoQueue() {
  useRealtimeVideoQueue() // Automatically updates when video_queue changes

  const { data: videos } = useVideoQueue()
  // ... rest of component
}
```

```typescript
// In SearchQueue.tsx
import { useRealtimeSearchQueue } from '@/lib/queries'

export function SearchQueue() {
  useRealtimeSearchQueue() // Automatically updates when search_queue changes

  const { data: searches } = useSearchQueue()
  // ... rest of component
}
```

---

## Development Workflow

### 1. Start Development Server

```bash
npm run dev
```

Access at `http://localhost:5173`

### 2. Build for Production

```bash
npm run build
```

Output in `dist/` folder.

### 3. Preview Production Build

```bash
npm run preview
```

---

## Deployment to Vercel

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Deploy

```bash
vercel
```

Follow the prompts:
- Set up and deploy? **Yes**
- Which scope? **Your account**
- Link to existing project? **No**
- Project name? **queue-management-app**
- In which directory is your code? **./
- Want to override settings? **No**

### 3. Add Environment Variables

In Vercel dashboard:
1. Go to project Settings → Environment Variables
2. Add:
   - `VITE_SUPABASE_URL` = your Supabase project URL
   - `VITE_SUPABASE_ANON_KEY` = your Supabase anon key

### 4. Redeploy

```bash
vercel --prod
```

---

## Features Checklist

### Core Features
- ✅ Dashboard with KPIs and charts
- ✅ Search Queue management (CRUD operations)
- ✅ Video Queue management (CRUD operations)
- ✅ Employee management (CRUD operations)
- ✅ Real-time updates via Supabase subscriptions
- ✅ Priority score calculator for videos
- ✅ Status tracking and color coding
- ✅ Department and role filtering
- ✅ Keyword tagging
- ✅ Search and filtering on all tables

### Advanced Features
- 📊 Data visualization with Recharts
- 🔍 Global search across all tables
- 📱 Responsive design (mobile-friendly)
- 🎨 Dark mode support (optional enhancement)
- 📤 Export to CSV functionality (optional enhancement)
- 🔔 Toast notifications for actions
- ⚡ Optimistic updates with React Query
- 🔄 Automatic refetching on window focus

---

## Testing

### Manual Testing Checklist

1. **Database Connection:**
   - [ ] App loads without errors
   - [ ] Data fetches from Supabase correctly
   - [ ] Real-time updates work when data changes

2. **Search Queue:**
   - [ ] Can add new search
   - [ ] Can edit existing search
   - [ ] Can delete search
   - [ ] Table sorting works
   - [ ] Table filtering works
   - [ ] Status badges show correct colors

3. **Video Queue:**
   - [ ] Can add new video
   - [ ] Priority score calculates correctly
   - [ ] Video URLs are clickable
   - [ ] Views/likes format correctly (K/M)
   - [ ] Can update video status
   - [ ] Can delete video

4. **Employees:**
   - [ ] Can add new employee
   - [ ] Can edit employee
   - [ ] Can deactivate employee
   - [ ] Department/role dropdowns work

5. **Dashboard:**
   - [ ] KPI cards show correct counts
   - [ ] Charts render correctly
   - [ ] Recent activity displays

---

## Troubleshooting

### Issue: "Missing Supabase environment variables"
**Solution:** Ensure `.env.local` exists with correct values and restart dev server.

### Issue: Real-time not working
**Solution:**
1. Check Supabase project → Database → Replication
2. Enable replication for `search_queue`, `video_queue`, `video_progress`
3. Verify real-time is enabled in Supabase dashboard

### Issue: RLS policies blocking data
**Solution:**
1. Temporarily disable RLS in Supabase for testing
2. Or add proper authentication and update RLS policies

### Issue: CORS errors
**Solution:** Supabase automatically handles CORS. Check project URL is correct.

---

## Next Steps

After completing this app:

1. **Add Authentication:**
   - Implement Supabase Auth
   - Add login/logout functionality
   - Protect routes with auth guards
   - Update RLS policies for multi-user access

2. **Enhance UI:**
   - Add dark mode toggle
   - Improve mobile responsiveness
   - Add loading skeletons
   - Add empty states

3. **Add Export Features:**
   - CSV export for all tables
   - PDF report generation
   - Data visualization exports

4. **Integration with Video Processing App:**
   - API endpoints for cross-app communication
   - Shared authentication
   - Unified navigation

---

## Resources

- **Supabase Docs:** https://supabase.com/docs
- **shadcn/ui Components:** https://ui.shadcn.com
- **TanStack Query:** https://tanstack.com/query/latest
- **TanStack Table:** https://tanstack.com/table/latest
- **Recharts:** https://recharts.org
- **Vite:** https://vitejs.dev

---

## Support

For issues:
1. Check browser console for errors
2. Check Supabase logs in dashboard
3. Verify environment variables are set
4. Review database schema matches expected types

---

**End of Prompt 2: Queue Management Web App**

This prompt provides complete instructions for building the Queue Management application with React, TypeScript, Supabase, and modern tooling. Copy this entire prompt to an AI builder (Lovable, v0, Cursor, etc.) to generate the full application.