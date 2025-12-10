# COMPLETE APPLICATION GENERATION PROMPT
# Research Management System - Search & Video Queue Application

**Version:** 3.1
**Date:** 2025-12-09
**Purpose:** Complete prompt for generating a production-ready Search Queue and Video Queue management application
**Design System:** Game Academy Design System v1.0 (October 2025)
**UI Framework:** shadcn/ui + Tailwind CSS v4
**Data Storage:** Dropbox API (no database)

---

## 🎯 APPLICATION OVERVIEW

Build a **Research Management Web Application** for managing video research queues and search tasks. This application helps teams discover, prioritize, and process educational video content for knowledge extraction.

### Core Functionality

1. **Search Queue Module** - Manage search research tasks with AI-powered results
2. **Video Queue Module** - Manage video processing queue with intelligent prioritization
3. **Unified Dashboard** - Real-time statistics and progress tracking
4. **Processing Automation** - Automated entity extraction and gap analysis workflow

### Technology Stack

**ВАЖНО:** Backend и Frontend - **отдельные приложения** (разные репозитории)

```json
{
  "frontend": {
    "framework": "React 19 (latest)",
    "language": "TypeScript 5.0+",
    "buildTool": "Vite",
    "styling": "Tailwind CSS v4+",
    "uiComponents": "shadcn/ui (latest)",
    "stateManagement": "Zustand + React Context API",
    "dataFetching": "TanStack Query (React Query)",
    "forms": "React Hook Form + Zod",
    "tables": "TanStack Table",
    "charts": "Recharts",
    "http": "Axios"
  },
  "backend": {
    "runtime": "Node.js 20+",
    "framework": "Express.js 4.18+",
    "dataStorage": "Dropbox API (no database)",
    "validation": "Zod",
    "cors": "CORS middleware",
    "auth": "JWT (jsonwebtoken)",
    "apiDocs": "Swagger/OpenAPI"
  },
  "integrations": {
    "ai": ["OpenAI GPT-4", "Google Gemini"],
    "video": "YouTube Data API v3",
    "storage": "Dropbox API (primary data storage)",
    "search": "Perplexity AI"
  }
}
```

### Project Structure (2 Separate Apps)

```bash
research-management/
├── frontend/                 # React App
│   ├── src/
│   ├── package.json
│   ├── vite.config.ts
│   └── README.md
│
└── backend/                  # Express API
    ├── src/
    ├── package.json
    └── README.md
```

---

## 🎨 DESIGN SYSTEM INTEGRATION (CRITICAL)

### Single Source of Truth

**CRITICAL REQUIREMENT:** ALL styling MUST come from `design-system.json`

**Setup Instructions:**

1. Copy `design-system.json` to project: `src/design-system/design-system.json`
2. Import in EVERY component:
   ```typescript
   import designSystem from '@/design-system/design-system.json';
   const { colorPalette, typography, spacing, components, borderRadius, shadows } = designSystem.designSystem;
   ```

### Reference Files

- **Complete Specification:** `design-system.json` (2,500+ lines)
- **Integration Guide:** `DESIGN-SYSTEM-INTEGRATION-GUIDE.md`
- **Quick Reference:** `_DESIGN-SYSTEM-SNIPPET.md`
- **Analysis:** `design-system-analysis.md`

### Critical Design Values

```typescript
// DO's ✅
const primaryColor = colorPalette.systemColors.light.primary.default; // #2563EB
const sidebarBg = '#1F2937'; // Dark even in light theme
const scrollbarWidth = '6px'; // NOT 8px!
const buttonRadius = components.button.borderRadius; // 8px
const cardRadius = components.card.borderRadius; // 12px

// DON'Ts ❌
const primaryColor = '#2563EB'; // Never hardcode
const scrollbarWidth = '8px'; // Wrong value
```

### Color Palette

```typescript
// Department Colors (from design-system.json)
const departmentColors = {
  search: '#6D28D9',      // Designers - Deep Purple
  video: '#147857',       // Developers - Forest Green
  designers: '#6D28D9',   // Purple
  developers: '#147857',  // Green
  managers: '#DC2626',    // Red
  marketers: '#EC4899',   // Pink
  videographers: '#F97316' // Orange
};

// System Colors - Light Theme
const lightTheme = {
  primary: { default: '#2563EB', hover: '#3B82F6', active: '#1D4ED8' },
  secondary: { default: '#6B7280', hover: '#9CA3AF', active: '#4B5563' },
  background: { primary: '#f7fafc', secondary: '#ffffff', tertiary: '#edf2f7' },
  text: { primary: '#2d3748', secondary: '#718096', tertiary: '#a0aec0' },
  border: '#e2e8f0',
  sidebar: '#1F2937' // Always dark
};

// System Colors - Dark Theme
const darkTheme = {
  primary: { default: '#60A5FA', hover: '#93C5FD', active: '#3B82F6' },
  secondary: { default: '#9CA3AF', hover: '#D1D5DB', active: '#6B7280' },
  background: { primary: '#0f172a', secondary: '#1e293b', tertiary: '#334155' },
  text: { primary: '#f8fafc', secondary: '#cbd5e1', tertiary: '#94a3b8' },
  border: '#334155',
  sidebar: '#1F2937' // Same as light
};
```

### Typography System

```typescript
// Font Family (from design-system.json)
const fontFamily = {
  primary: ['Roboto', 'sans-serif'],
  weights: [300, 400, 500, 600, 700] // Light, Regular, Medium, SemiBold, Bold
};

// Typography Scale
const typography = {
  h1: { size: '48px', weight: 600, lineHeight: '58px' },
  h2: { size: '40px', weight: 600, lineHeight: '48px' },
  h3: { size: '32px', weight: 600, lineHeight: '38px' },
  h4: { size: '24px', weight: 600, lineHeight: '32px' },
  h5: { size: '20px', weight: 600, lineHeight: '28px' },
  h6: { size: '18px', weight: 600, lineHeight: '26px' },
  body: { size: '16px', weight: 400, lineHeight: '24px' },
  bodyLarge: { size: '18px', weight: 400, lineHeight: '28px' },
  bodySmall: { size: '14px', weight: 400, lineHeight: '20px' },
  caption: { size: '12px', weight: 400, lineHeight: '16px' }
};
```

### Spacing System

```typescript
// Base Unit: 4px (from design-system.json)
const spacing = {
  'space-0': '0px',
  'space-1': '4px',    // 1 unit
  'space-2': '8px',    // 2 units
  'space-3': '12px',   // 3 units
  'space-4': '16px',   // 4 units
  'space-5': '20px',   // 5 units
  'space-6': '24px',   // 6 units
  'space-8': '32px',   // 8 units
  'space-10': '40px',  // 10 units
  'space-12': '48px',  // 12 units
  'space-16': '64px',  // 16 units
  'space-20': '80px',  // 20 units
  'space-24': '96px'   // 24 units
};
```

### Component Specifications

```typescript
// Buttons (from design-system.json)
const button = {
  borderRadius: '8px',
  padding: { default: '12px 24px', small: '8px 16px', large: '16px 32px' },
  fontSize: { default: '16px', small: '14px', large: '18px' },
  fontWeight: 500,
  transition: '300ms ease',
  minHeight: '40px'
};

// Cards (from design-system.json)
const card = {
  borderRadius: '12px',
  padding: '24px',
  boxShadow: '0 2px 8px rgba(0, 0, 0, 0.10)',
  background: '#ffffff', // light theme
  border: '1px solid #e2e8f0'
};

// Inputs (from design-system.json)
const input = {
  borderRadius: '8px',
  padding: '12px 16px',
  fontSize: '16px',
  minHeight: '40px',
  border: '1px solid #e2e8f0',
  focusBorder: '2px solid #2563EB'
};

// Modals (from design-system.json)
const modal = {
  borderRadius: '12px',
  maxWidth: '600px',
  padding: '32px',
  boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
  zIndex: 1050,
  backdrop: 'rgba(0, 0, 0, 0.5)'
};

// Sidebar (from design-system.json)
const sidebar = {
  widthExpanded: '256px',
  widthCollapsed: '80px',
  background: '#1F2937', // Dark even in light theme!
  textColor: '#ffffff',
  transition: '300ms ease',
  zIndex: 100
};

// Scrollbar (from design-system.json)
const scrollbar = {
  width: '6px', // CRITICAL: NOT 8px!
  track: 'transparent',
  thumb: '#CBD5E0',
  thumbHover: '#A0AEC0'
};
```

### Priority System (5-Tier with Stars)

```typescript
// Priority Tiers (0-100 scale)
const priorityTiers = {
  critical: {
    range: [80, 100],
    stars: 5,
    color: '#DC2626',      // Red
    label: 'Critical',
    icon: '⭐⭐⭐⭐⭐'
  },
  high: {
    range: [60, 79],
    stars: 4,
    color: '#EA580C',      // Orange
    label: 'High',
    icon: '⭐⭐⭐⭐'
  },
  medium: {
    range: [40, 59],
    stars: 3,
    color: '#F59E0B',      // Yellow
    label: 'Medium',
    icon: '⭐⭐⭐'
  },
  low: {
    range: [20, 39],
    stars: 2,
    color: '#84CC16',      // Light Green
    label: 'Low',
    icon: '⭐⭐'
  },
  veryLow: {
    range: [0, 19],
    stars: 1,
    color: '#22C55E',      // Green
    label: 'Very Low',
    icon: '⭐'
  }
};

// Priority Badge Component
function PriorityBadge({ priority }: { priority: number }) {
  const tier = getPriorityTier(priority);
  return (
    <div
      className="priority-badge"
      style={{
        backgroundColor: tier.color,
        borderRadius: components.badge.borderRadius, // 9999px (fully rounded)
        padding: '4px 12px',
        color: '#ffffff',
        fontSize: '12px',
        fontWeight: 600,
        display: 'inline-flex',
        alignItems: 'center',
        gap: '4px'
      }}
    >
      <span>{tier.icon}</span>
      <span>{tier.label}</span>
      <span>({priority})</span>
    </div>
  );
}

function getPriorityTier(priority: number) {
  if (priority >= 80) return priorityTiers.critical;
  if (priority >= 60) return priorityTiers.high;
  if (priority >= 40) return priorityTiers.medium;
  if (priority >= 20) return priorityTiers.low;
  return priorityTiers.veryLow;
}
```

### shadcn/ui Setup

**CRITICAL:** Use shadcn/ui for ALL UI components. Do NOT create custom components when shadcn/ui equivalents exist.

**Installation:**
```bash
# Initialize shadcn/ui with Tailwind CSS v4
npx shadcn@latest init

# Select options:
# - Style: new-york (default for new projects)
# - Base color: slate
# - CSS variables: yes
# - Tailwind CSS: v4
```

**Add Required Components:**
```bash
# Core components
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add input
npx shadcn@latest add label
npx shadcn@latest add select
npx shadcn@latest add textarea
npx shadcn@latest add badge
npx shadcn@latest add dropdown-menu
npx shadcn@latest add table
npx shadcn@latest add tabs
npx shadcn@latest add toast
npx shadcn@latest add sonner  # Replace deprecated toast
npx shadcn@latest add skeleton
npx shadcn@latest add separator
```

**Component Usage Pattern:**
```typescript
// ✅ CORRECT: Use shadcn/ui components
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';

// ❌ WRONG: Don't create custom button/card/modal components
// const CustomButton = () => <button>...</button>
```

### Tailwind CSS v4 Configuration

**IMPORTANT:** Tailwind CSS v4 uses new `@theme` directive instead of `theme.extend` in config.

```typescript
// tailwind.config.ts (v4 compatible)
import type { Config } from 'tailwindcss';
import designSystem from './src/design-system/design-system.json';

const { colorPalette, typography, spacing, borderRadius, shadows } = designSystem.designSystem;

const config: Config = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // System colors
        primary: colorPalette.systemColors.light.primary,
        secondary: colorPalette.systemColors.light.secondary,

        // Department colors
        'dept-search': '#6D28D9',
        'dept-video': '#147857',
        'dept-designers': '#6D28D9',
        'dept-developers': '#147857',
        'dept-managers': '#DC2626',
        'dept-marketers': '#EC4899',
        'dept-videographers': '#F97316',

        // Semantic colors
        success: colorPalette.systemColors.light.success,
        warning: colorPalette.systemColors.light.warning,
        error: colorPalette.systemColors.light.error,

        // Background
        'bg-primary': colorPalette.background.primary,
        'bg-secondary': colorPalette.background.secondary,
        'bg-tertiary': colorPalette.background.tertiary,

        // Text
        'text-primary': colorPalette.text.primary,
        'text-secondary': colorPalette.text.secondary,
        'text-tertiary': colorPalette.text.tertiary,

        // Sidebar
        'sidebar-bg': '#1F2937',
        'sidebar-text': '#ffffff'
      },
      fontFamily: {
        sans: typography.fontFamilies.primary
      },
      fontSize: {
        'h1': [typography.heading.h1.fontSize, { lineHeight: typography.heading.h1.lineHeight }],
        'h2': [typography.heading.h2.fontSize, { lineHeight: typography.heading.h2.lineHeight }],
        'h3': [typography.heading.h3.fontSize, { lineHeight: typography.heading.h3.lineHeight }],
        'h4': [typography.heading.h4.fontSize, { lineHeight: typography.heading.h4.lineHeight }],
        'h5': [typography.heading.h5.fontSize, { lineHeight: typography.heading.h5.lineHeight }],
        'h6': [typography.heading.h6.fontSize, { lineHeight: typography.heading.h6.lineHeight }],
        'body': [typography.body.default.fontSize, { lineHeight: typography.body.default.lineHeight }],
        'body-lg': [typography.body.large.fontSize, { lineHeight: typography.body.large.lineHeight }],
        'body-sm': [typography.body.small.fontSize, { lineHeight: typography.body.small.lineHeight }],
        'caption': [typography.caption.fontSize, { lineHeight: typography.caption.lineHeight }]
      },
      spacing: spacing,
      borderRadius: {
        'btn': borderRadius.button,      // 8px
        'card': borderRadius.card,        // 12px
        'input': borderRadius.input,      // 8px
        'modal': borderRadius.modal,      // 12px
        'badge': borderRadius.tag,        // 9999px
        'sm': borderRadius.small,         // 4px
        'md': borderRadius.medium,        // 8px
        'lg': borderRadius.large          // 12px
      },
      boxShadow: {
        'light': shadows.light,           // 0 1px 3px rgba(0,0,0,0.12)
        'card': shadows.card,             // 0 2px 8px rgba(0,0,0,0.10)
        'medium': shadows.medium,         // 0 4px 12px rgba(0,0,0,0.15)
        'heavy': shadows.heavy            // 0 8px 24px rgba(0,0,0,0.20)
      },
      transitionDuration: {
        'fast': '150ms',
        'normal': '300ms',
        'slow': '500ms'
      },
      zIndex: {
        'dropdown': '1000',
        'modal': '1050',
        'tooltip': '1100'
      }
    }
  },
  plugins: [require('tailwindcss-animate')]
};
```

**Alternative: Tailwind CSS v4 with @theme directive (Recommended)**

```css
/* src/styles/globals.css */
@import "tailwindcss";
@import "tailwindcss/theme" theme(reference);
@import "tailwindcss/preflight";
@import "tailwindcss/utilities";

@theme {
  /* Import design system values */
  --color-primary: #2563EB;
  --color-primary-hover: #3B82F6;
  --color-primary-active: #1D4ED8;
  
  --color-dept-search: #6D28D9;
  --color-dept-video: #147857;
  
  --radius-button: 8px;
  --radius-card: 12px;
  --radius-input: 8px;
  --radius-modal: 12px;
  --radius-badge: 9999px;
  
  --spacing-base: 4px;
  
  --font-family-sans: 'Roboto', sans-serif;
  
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.10);
  --shadow-medium: 0 4px 12px rgba(0, 0, 0, 0.15);
  --shadow-heavy: 0 8px 24px rgba(0, 0, 0, 0.20);
}
```

**Tailwind v4 Features:**
- ✅ New `@theme` directive for theme customization
- ✅ Improved color system (OKLCH support)
- ✅ Better performance
- ✅ CSS-first configuration
- ✅ Full compatibility with shadcn/ui

---

## 📊 SEARCH QUEUE MODULE

### Module Overview

**Purpose:** Manage search research tasks with AI-powered results
**Module Color:** `#6D28D9` (Designers - Deep Purple)
**Department:** Designers

### Key Features

1. Create search tasks with employee/department/topic assignment
2. Execute searches using OpenAI/Perplexity AI
3. View and organize search results
4. Add relevant videos to Video Queue
5. Track task status (Assigned → In_Progress → Completed)
6. Filter by status, department, priority
7. Display statistics (total tasks, completion rate, videos found)

### Data Model

```typescript
interface SearchTask {
  id: string;                    // Unique ID (cuid)
  search_id: string;             // Display ID (SRH-001, SRH-002, etc.)
  employee: string;              // Employee name
  department: string;            // Department code (VID, AID, DEV, etc.)
  topic: string;                 // Search topic/objective
  search_query?: string;         // AI-generated search query
  status: 'Assigned' | 'In_Progress' | 'Completed';
  priority: number;              // 0-100 priority score
  date_assigned: Date;
  date_completed?: Date;
  videos_found: number;          // Count of results
  results?: SearchResult[];      // Array of found videos
  notes?: string;
  createdAt: Date;
  updatedAt: Date;
}

interface SearchResult {
  title: string;
  url: string;
  channel: string;
  views: number;
  duration: string;
  upload_date: string;
  relevance_score: number;       // 0-100 calculated by AI
  thumbnail: string;
}
```

### Components

#### 1. SearchQueueDashboard.tsx

Main dashboard component with filters, statistics, and task grid.

```typescript
import React, { useState, useEffect } from 'react';
import { useSearchQueueStore } from '@/stores/searchQueueStore';
import { SearchTaskCard } from './SearchTaskCard';
import { CreateSearchTaskModal } from './CreateSearchTaskModal';
import { SearchResultsModal } from './SearchResultsModal';
import { SearchQueueStats } from './SearchQueueStats';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { useTheme } from '@/contexts/ThemeContext';

export function SearchQueueDashboard() {
  const { tasks, loading, error, fetchTasks, createTask, executeSearch } = useSearchQueueStore();

  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [resultsModalData, setResultsModalData] = useState<SearchTask | null>(null);
  const [statusFilter, setStatusFilter] = useState<string>('All');
  const [departmentFilter, setDepartmentFilter] = useState<string>('All');
  const [sortBy, setSortBy] = useState<string>('priority');

  useEffect(() => {
    fetchTasks();
  }, []);

  // Filter and sort tasks
  const filteredTasks = tasks
    .filter(task => {
      if (statusFilter !== 'All' && task.status !== statusFilter) return false;
      if (departmentFilter !== 'All' && task.department !== departmentFilter) return false;
      return true;
    })
    .sort((a, b) => {
      if (sortBy === 'priority') return b.priority - a.priority;
      if (sortBy === 'date') return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
      return 0;
    });

  const handleExecuteSearch = async (taskId: string) => {
    const task = tasks.find(t => t.id === taskId);
    if (!task) return;

    const results = await executeSearch(taskId, task.search_query || task.topic);
    setResultsModalData({ ...task, results });
  };

  return (
    <div className="min-h-screen bg-bg-primary p-8">
      {/* Header */}
      <header className="flex items-center justify-between mb-8">
        <div>
          <h1
            className="text-h1 font-semibold mb-2"
            style={{ color: colorPalette.text.primary }}
          >
            Search Queue
          </h1>
          <p
            className="text-body-sm"
            style={{ color: colorPalette.text.secondary }}
          >
            Manage video search tasks and assignments
          </p>
        </div>
        <Button
          onClick={() => setIsCreateModalOpen(true)}
          className="bg-[#6D28D9] hover:bg-[#5B21B6] text-white"
          size="default"
        >
          <span className="mr-2">➕</span>
          New Search Task
        </Button>
      </header>

      {/* Statistics */}
      <SearchQueueStats tasks={tasks} />

      {/* Filters */}
      <div className="flex items-center gap-4 mb-6">
        {/* Status Filter */}
        <div className="filter-group flex items-center gap-2">
          <span className="text-body-sm text-text-secondary">Status:</span>
          {['All', 'Assigned', 'In_Progress', 'Completed'].map(status => (
            <Button
              key={status}
              onClick={() => setStatusFilter(status)}
              variant={statusFilter === status ? 'default' : 'outline'}
              size="sm"
              className={statusFilter === status ? 'bg-[#6D28D9] hover:bg-[#5B21B6]' : ''}
            >
              {status.replace('_', ' ')}
            </Button>
          ))}
        </div>

        {/* Sort */}
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value)}
          className="h-9 rounded-md border border-input bg-background px-3 py-1 text-sm"
        >
          <option value="priority">Sort by Priority</option>
          <option value="date">Sort by Date</option>
        </select>
      </div>

      {/* Tasks Grid */}
      {loading ? (
        <div className="loading-state">Loading...</div>
      ) : error ? (
        <div className="error-state">{error}</div>
      ) : filteredTasks.length === 0 ? (
        <div className="empty-state">
          <p>No search tasks found.</p>
          <button onClick={() => setIsCreateModalOpen(true)}>Create First Task</button>
        </div>
      ) : (
        <div className="grid gap-6 grid-cols-1 lg:grid-cols-2 xl:grid-cols-3">
          {filteredTasks.map(task => (
            <SearchTaskCard
              key={task.id}
              task={task}
              onExecute={handleExecuteSearch}
              onViewResults={() => setResultsModalData(task)}
            />
          ))}
        </div>
      )}

      {/* Modals */}
      <CreateSearchTaskModal
        isOpen={isCreateModalOpen}
        onClose={() => setIsCreateModalOpen(false)}
        onCreate={createTask}
      />

      {resultsModalData && (
        <SearchResultsModal
          task={resultsModalData}
          onClose={() => setResultsModalData(null)}
        />
      )}
    </div>
  );
}
```

#### 2. SearchTaskCard.tsx

Individual task card component.

```typescript
import React from 'react';
import { SearchTask } from '@/types';
import { PriorityBadge } from '@/components/shared/PriorityBadge';
import { StatusBadge } from '@/components/shared/StatusBadge';
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

interface SearchTaskCardProps {
  task: SearchTask;
  onExecute: (taskId: string) => void;
  onViewResults: () => void;
}

export function SearchTaskCard({ task, onExecute, onViewResults }: SearchTaskCardProps) {
  return (
    <Card className="hover:shadow-md transition-all duration-300 hover:-translate-y-1 cursor-pointer">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <CardTitle className="text-lg font-semibold mb-1">
              {task.topic}
            </CardTitle>
            <p className="text-sm text-muted-foreground">
              {task.search_id} • {task.employee}
            </p>
          </div>
          <PriorityBadge priority={task.priority} />
        </div>
      </CardHeader>

      <CardContent>
        {/* Department & Status */}
        <div className="flex items-center gap-2 mb-4">
          <Badge className="bg-[#6D28D9] text-white">
            {task.department}
          </Badge>
          <StatusBadge status={task.status} />
        </div>

        {/* Search Query */}
        {task.search_query && (
          <div className="mb-4">
            <p className="text-xs text-muted-foreground mb-1">
              Search Query:
            </p>
            <p className="text-sm text-foreground">
              {task.search_query}
            </p>
          </div>
        )}

        {/* Stats */}
        <div className="flex items-center gap-4 mb-4">
          <div>
            <p className="text-xs text-muted-foreground">Videos Found</p>
            <p className="text-lg font-semibold text-[#6D28D9]">
              {task.videos_found}
            </p>
          </div>
          <div>
            <p className="text-xs text-muted-foreground">Assigned</p>
            <p className="text-sm text-foreground">
              {new Date(task.date_assigned).toLocaleDateString()}
            </p>
          </div>
        </div>
      </CardContent>

      <CardFooter>
        {/* Actions */}
        <div className="flex items-center gap-2 w-full">
          {task.status === 'Assigned' && (
            <Button
              onClick={() => onExecute(task.id)}
              className="flex-1 bg-[#6D28D9] hover:bg-[#5B21B6]"
              size="sm"
            >
              Execute Search
            </Button>
          )}
          {task.status === 'Completed' && (
            <Button
              onClick={onViewResults}
              variant="outline"
              className="flex-1 border-[#6D28D9] text-[#6D28D9] hover:bg-[#6D28D9] hover:text-white"
              size="sm"
            >
              View Results ({task.videos_found})
            </Button>
          )}
        </div>
      </CardFooter>
    </Card>
  );
}
```

#### 3. CreateSearchTaskModal.tsx

Modal for creating new search tasks.

```typescript
import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

const searchTaskSchema = z.object({
  employee: z.string().min(1, 'Employee name is required'),
  department: z.enum(['VID', 'AID', 'DEV', 'SMM', 'DGN']),
  topic: z.string().min(5, 'Topic must be at least 5 characters'),
  search_query: z.string().optional(),
  priority: z.number().min(0).max(100),
  notes: z.string().optional()
});

type SearchTaskFormData = z.infer<typeof searchTaskSchema>;

interface CreateSearchTaskModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCreate: (data: SearchTaskFormData) => Promise<void>;
}

export function CreateSearchTaskModal({ isOpen, onClose, onCreate }: CreateSearchTaskModalProps) {
  const { register, handleSubmit, formState: { errors }, reset, watch, setValue } = useForm<SearchTaskFormData>({
    resolver: zodResolver(searchTaskSchema),
    defaultValues: {
      priority: 50
    }
  });

  const onSubmit = async (data: SearchTaskFormData) => {
    await onCreate(data);
    reset();
    onClose();
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>Create Search Task</DialogTitle>
          <DialogDescription>
            Assign a new video search task to a team member
          </DialogDescription>
        </DialogHeader>

        {/* Form */}
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {/* Employee */}
          <div className="space-y-2">
            <Label htmlFor="employee">Employee Name *</Label>
            <Input
              id="employee"
              {...register('employee')}
              placeholder="Enter employee name"
              className={errors.employee ? 'border-destructive' : ''}
            />
            {errors.employee && (
              <p className="text-sm text-destructive mt-1">
                {errors.employee.message}
              </p>
            )}
          </div>

          {/* Department */}
          <div className="space-y-2">
            <Label htmlFor="department">Department *</Label>
            <Select
              value={watch('department') || ''}
              onValueChange={(value) => setValue('department', value as any, { shouldValidate: true })}
            >
              <SelectTrigger id="department">
                <SelectValue placeholder="Select department" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="VID">VID - Video Research</SelectItem>
                <SelectItem value="AID">AID - AI Development</SelectItem>
                <SelectItem value="DEV">DEV - Development</SelectItem>
                <SelectItem value="SMM">SMM - Social Media</SelectItem>
                <SelectItem value="DGN">DGN - Design</SelectItem>
              </SelectContent>
            </Select>
            {errors.department && (
              <p className="text-sm text-destructive mt-1">
                {errors.department.message}
              </p>
            )}
          </div>

          {/* Topic */}
          <div className="space-y-2">
            <Label htmlFor="topic">Search Topic *</Label>
            <Textarea
              id="topic"
              {...register('topic')}
              placeholder="Describe what to search for..."
              rows={3}
              className={errors.topic ? 'border-destructive' : ''}
            />
            {errors.topic && (
              <p className="text-sm text-destructive mt-1">
                {errors.topic.message}
              </p>
            )}
          </div>

          {/* Priority */}
          <div className="space-y-2">
            <Label htmlFor="priority">Priority (0-100)</Label>
            <Input
              id="priority"
              {...register('priority', { valueAsNumber: true })}
              type="number"
              min="0"
              max="100"
            />
          </div>

          {/* Actions */}
          <div className="flex items-center gap-3 justify-end pt-4">
            <Button
              type="button"
              onClick={onClose}
              variant="outline"
            >
              Cancel
            </Button>
            <Button
              type="submit"
              className="bg-[#6D28D9] hover:bg-[#5B21B6]"
            >
              Create Task
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
```

### State Management (Zustand Store)

```typescript
// stores/searchQueueStore.ts
import { create } from 'zustand';
import { SearchTask, SearchResult } from '@/types';

interface SearchQueueStore {
  tasks: SearchTask[];
  loading: boolean;
  error: string | null;

  // Actions
  fetchTasks: () => Promise<void>;
  createTask: (data: Partial<SearchTask>) => Promise<void>;
  executeSearch: (taskId: string, query: string) => Promise<SearchResult[]>;
  completeTask: (taskId: string) => Promise<void>;
  deleteTask: (taskId: string) => Promise<void>;
}

export const useSearchQueueStore = create<SearchQueueStore>((set, get) => ({
  tasks: [],
  loading: false,
  error: null,

  fetchTasks: async () => {
    set({ loading: true, error: null });
    try {
      const response = await fetch('/api/search-queue');
      const data = await response.json();
      set({ tasks: data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  createTask: async (data) => {
    set({ loading: true, error: null });
    try {
      const response = await fetch('/api/search-queue', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...data,
          status: 'Assigned',
          videos_found: 0,
          date_assigned: new Date().toISOString()
        })
      });
      const newTask = await response.json();
      set(state => ({
        tasks: [...state.tasks, newTask],
        loading: false
      }));
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  executeSearch: async (taskId, query) => {
    set({ loading: true, error: null });
    try {
      // Update status to In_Progress
      await fetch(`/api/search-queue/${taskId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'In_Progress' })
      });

      // Execute search with OpenAI/Perplexity
      const response = await fetch('/api/search-queue/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ taskId, query })
      });

      const { results } = await response.json();

      // Update task with results
      await fetch(`/api/search-queue/${taskId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          status: 'Completed',
          videos_found: results.length,
          results: JSON.stringify(results),
          date_completed: new Date().toISOString()
        })
      });

      // Refresh tasks
      await get().fetchTasks();

      set({ loading: false });
      return results;
    } catch (error) {
      set({ error: error.message, loading: false });
      return [];
    }
  },

  completeTask: async (taskId) => {
    try {
      await fetch(`/api/search-queue/${taskId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          status: 'Completed',
          date_completed: new Date().toISOString()
        })
      });
      await get().fetchTasks();
    } catch (error) {
      set({ error: error.message });
    }
  },

  deleteTask: async (taskId) => {
    try {
      await fetch(`/api/search-queue/${taskId}`, {
        method: 'DELETE'
      });
      await get().fetchTasks();
    } catch (error) {
      set({ error: error.message });
    }
  }
}));
```

---

## 🎬 VIDEO QUEUE MODULE

### Module Overview

**Purpose:** Manage video processing queue with intelligent prioritization
**Module Color:** `#147857` (Developers - Forest Green)
**Department:** Developers

### Key Features

1. Add videos from YouTube URLs
2. Automatic priority calculation (views, likes, recency, engagement)
3. Manual priority adjustment
4. Processing status tracking (Queued → Selected → In_Progress → Completed)
5. Video metadata extraction (title, channel, thumbnail, duration)
6. Grid and list view modes
7. Filter by status, priority, department
8. Sort by priority, date, views
9. Export to CSV
10. Bulk status updates

### Data Model

```typescript
interface Video {
  id: string;                    // Unique ID (cuid)
  vq_id: string;                 // Display ID (VQ-001, VQ-002, etc.)
  youtube_url: string;           // Full YouTube URL
  video_id: string;              // YouTube video ID
  title: string;
  channel: string;
  thumbnail: string;             // Thumbnail URL
  duration: string;              // Format: "PT15M33S" or "15:33"
  views: number;
  likes: number;
  upload_date: Date;
  topic: string;
  source: 'Manual' | 'Search_Queue' | 'Dropbox';
  employee: string;
  department: string;
  priority: number;              // 0-100 calculated score
  manual_priority?: number;      // Manual boost (0-20)
  status: 'Queued' | 'Selected' | 'In_Progress' | 'Completed';
  processing_phase?: 'Phase_1_Transcribed' | 'Phase_2_Extraction' | 'Phase_3_Gap_Analysis' | 'Phase_4_Integration' | 'Phase_5_Mapping';
  date_added: Date;
  date_selected?: Date;
  date_completed?: Date;
  notes?: string;
  createdAt: Date;
  updatedAt: Date;
}
```

### Priority Calculation Algorithm

```typescript
/**
 * Calculate video priority (0-100)
 *
 * Formula:
 * - Views: 30% (max 30 points)
 * - Likes/Engagement: 20% (max 20 points)
 * - Recency: 30% (max 30 points)
 * - Manual Boost: 20% (max 20 points)
 *
 * Total: 0-100 scale
 */
function calculatePriority(video: {
  views: number;
  likes: number;
  publishedAt: Date;
  manualPriority?: number;
}): number {
  // 1. View Score (0-30 points)
  // 1M views = 30 points, linear scale
  const viewScore = Math.min((video.views / 1000000) * 30, 30);

  // 2. Engagement Score (0-20 points)
  // Like ratio: likes / views * 100
  // 10% like ratio = 20 points
  const engagementRate = (video.likes / video.views) * 100;
  const engagementScore = Math.min(engagementRate * 2, 20);

  // 3. Recency Score (0-30 points)
  const recencyScore = calculateRecencyScore(video.publishedAt);

  // 4. Manual Boost (0-20 points)
  const manualBoost = video.manualPriority || 0;

  // Total
  const total = viewScore + engagementScore + recencyScore + manualBoost;

  return Math.min(Math.round(total), 100);
}

function calculateRecencyScore(publishedAt: Date): number {
  const now = new Date();
  const daysOld = (now.getTime() - publishedAt.getTime()) / (1000 * 60 * 60 * 24);

  // Recency scoring:
  // 0-7 days: 30 points
  // 8-30 days: 20 points
  // 31-90 days: 10 points
  // 91+ days: 5 points

  if (daysOld <= 7) return 30;
  if (daysOld <= 30) return 20;
  if (daysOld <= 90) return 10;
  return 5;
}

// Example usage
const video = {
  views: 500000,        // 500K views
  likes: 25000,         // 25K likes
  publishedAt: new Date('2025-12-01'), // 8 days ago
  manualPriority: 10    // Manual boost
};

const priority = calculatePriority(video);
// viewScore: 15 (500K / 1M * 30)
// engagementScore: 10 ((25K / 500K * 100) * 2 = 5% * 2 = 10)
// recencyScore: 20 (8 days old)
// manualBoost: 10
// Total: 55 (Medium priority, 3 stars)
```

### Components

#### 1. VideoQueueDashboard.tsx

Main dashboard with grid/list views, filters, and statistics.

```typescript
import React, { useState, useEffect } from 'react';
import { useVideoQueueStore } from '@/stores/videoQueueStore';
import { VideoCard } from './VideoCard';
import { AddVideoModal } from './AddVideoModal';
import { VideoQueueStats } from './VideoQueueStats';
import { FilterPanel } from './FilterPanel';
import designSystem from '@/design-system/design-system.json';

const { colorPalette, spacing, typography } = designSystem.designSystem;

export function VideoQueueDashboard() {
  const { videos, loading, error, fetchVideos, addVideo, updateStatus } = useVideoQueueStore();

  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid');
  const [statusFilter, setStatusFilter] = useState<string>('All');
  const [priorityFilter, setPriorityFilter] = useState<string>('All');
  const [departmentFilter, setDepartmentFilter] = useState<string>('All');
  const [sortBy, setSortBy] = useState<string>('priority');

  useEffect(() => {
    fetchVideos();
  }, []);

  // Filter and sort videos
  const filteredVideos = videos
    .filter(video => {
      if (statusFilter !== 'All' && video.status !== statusFilter) return false;
      if (departmentFilter !== 'All' && video.department !== departmentFilter) return false;

      // Priority filter
      if (priorityFilter !== 'All') {
        const tier = getPriorityTier(video.priority);
        if (priorityFilter === 'High' && tier.stars < 4) return false;
        if (priorityFilter === 'Medium' && (tier.stars < 3 || tier.stars > 3)) return false;
        if (priorityFilter === 'Low' && tier.stars > 2) return false;
      }

      return true;
    })
    .sort((a, b) => {
      if (sortBy === 'priority') return b.priority - a.priority;
      if (sortBy === 'date') return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
      if (sortBy === 'views') return b.views - a.views;
      return 0;
    });

  const handleExport = async () => {
    const response = await fetch('/api/video-queue/export');
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `video-queue-${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
  };

  return (
    <div className="min-h-screen bg-bg-primary p-8">
      {/* Header */}
      <header className="flex items-center justify-between mb-8">
        <div>
          <h1
            className="text-h1 font-semibold mb-2"
            style={{ color: colorPalette.text.primary }}
          >
            Video Queue
          </h1>
          <p
            className="text-body-sm"
            style={{ color: colorPalette.text.secondary }}
          >
            Manage and prioritize video processing queue
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={handleExport}
            className="btn-secondary"
            style={{
              padding: `${spacing['space-3']} ${spacing['space-6']}`,
              borderRadius: designSystem.designSystem.borderRadius.button,
              border: `1px solid ${colorPalette.border.default}`,
              fontSize: typography.body.default.fontSize,
              fontWeight: 500,
              color: colorPalette.text.secondary
            }}
          >
            📤 Export CSV
          </button>
          <button
            onClick={() => setIsAddModalOpen(true)}
            className="btn-primary"
            style={{
              backgroundColor: '#147857', // Video module color
              color: '#ffffff',
              padding: `${spacing['space-3']} ${spacing['space-6']}`,
              borderRadius: designSystem.designSystem.borderRadius.button,
              fontSize: typography.body.default.fontSize,
              fontWeight: 500,
              display: 'flex',
              alignItems: 'center',
              gap: spacing['space-2']
            }}
          >
            <span>➕</span>
            <span>Add Video</span>
          </button>
        </div>
      </header>

      {/* Statistics */}
      <VideoQueueStats videos={videos} />

      {/* Filters & Controls */}
      <div className="flex items-center justify-between mb-6">
        {/* Filters */}
        <div className="flex items-center gap-4">
          {/* Status Filter */}
          <div className="filter-group flex items-center gap-2">
            <span className="text-body-sm text-text-secondary">Status:</span>
            {['All', 'Queued', 'Selected', 'In_Progress', 'Completed'].map(status => (
              <button
                key={status}
                onClick={() => setStatusFilter(status)}
                className={`filter-button ${statusFilter === status ? 'active' : ''}`}
                style={{
                  padding: `${spacing['space-2']} ${spacing['space-4']}`,
                  borderRadius: designSystem.designSystem.borderRadius.small,
                  fontSize: typography.body.small.fontSize,
                  fontWeight: 500,
                  backgroundColor: statusFilter === status ? '#147857' : 'transparent',
                  color: statusFilter === status ? '#ffffff' : colorPalette.text.secondary,
                  border: `1px solid ${statusFilter === status ? '#147857' : colorPalette.border.default}`,
                  transition: 'all 150ms ease'
                }}
              >
                {status.replace('_', ' ')}
              </button>
            ))}
          </div>

          {/* Priority Filter */}
          <div className="filter-group flex items-center gap-2">
            <span className="text-body-sm text-text-secondary">Priority:</span>
            {['All', 'High', 'Medium', 'Low'].map(priority => (
              <button
                key={priority}
                onClick={() => setPriorityFilter(priority)}
                className={`filter-button ${priorityFilter === priority ? 'active' : ''}`}
                style={{
                  padding: `${spacing['space-2']} ${spacing['space-4']}`,
                  borderRadius: designSystem.designSystem.borderRadius.small,
                  fontSize: typography.body.small.fontSize,
                  fontWeight: 500,
                  backgroundColor: priorityFilter === priority ? '#147857' : 'transparent',
                  color: priorityFilter === priority ? '#ffffff' : colorPalette.text.secondary,
                  border: `1px solid ${priorityFilter === priority ? '#147857' : colorPalette.border.default}`,
                  transition: 'all 150ms ease'
                }}
              >
                {priority}
              </button>
            ))}
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center gap-3">
          {/* Sort */}
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="select"
            style={{
              padding: `${spacing['space-2']} ${spacing['space-4']}`,
              borderRadius: designSystem.designSystem.borderRadius.input,
              border: `1px solid ${colorPalette.border.default}`,
              fontSize: typography.body.small.fontSize
            }}
          >
            <option value="priority">Sort by Priority</option>
            <option value="date">Sort by Date</option>
            <option value="views">Sort by Views</option>
          </select>

          {/* View Mode Toggle */}
          <div
            className="flex items-center gap-1 p-1"
            style={{
              border: `1px solid ${colorPalette.border.default}`,
              borderRadius: designSystem.designSystem.borderRadius.small
            }}
          >
            <button
              onClick={() => setViewMode('grid')}
              className={`btn-icon ${viewMode === 'grid' ? 'active' : ''}`}
              style={{
                padding: spacing['space-2'],
                borderRadius: designSystem.designSystem.borderRadius.small,
                backgroundColor: viewMode === 'grid' ? colorPalette.background.tertiary : 'transparent',
                color: colorPalette.text.primary
              }}
            >
              ⊞
            </button>
            <button
              onClick={() => setViewMode('list')}
              className={`btn-icon ${viewMode === 'list' ? 'active' : ''}`}
              style={{
                padding: spacing['space-2'],
                borderRadius: designSystem.designSystem.borderRadius.small,
                backgroundColor: viewMode === 'list' ? colorPalette.background.tertiary : 'transparent',
                color: colorPalette.text.primary
              }}
            >
              ☰
            </button>
          </div>
        </div>
      </div>

      {/* Videos Grid/List */}
      {loading ? (
        <div className="loading-state">Loading videos...</div>
      ) : error ? (
        <div className="error-state">{error}</div>
      ) : filteredVideos.length === 0 ? (
        <div className="empty-state">
          <p>No videos in queue.</p>
          <button onClick={() => setIsAddModalOpen(true)}>Add First Video</button>
        </div>
      ) : (
        <div
          className={viewMode === 'grid'
            ? 'grid gap-6 grid-cols-1 lg:grid-cols-2 xl:grid-cols-3'
            : 'flex flex-col gap-4'
          }
        >
          {filteredVideos.map(video => (
            <VideoCard
              key={video.id}
              video={video}
              viewMode={viewMode}
              onUpdateStatus={(status) => updateStatus(video.id, status)}
            />
          ))}
        </div>
      )}

      {/* Add Video Modal */}
      <AddVideoModal
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        onAdd={addVideo}
      />
    </div>
  );
}
```

### State Management (Zustand Store)

```typescript
// stores/videoQueueStore.ts
import { create } from 'zustand';
import { Video } from '@/types';
import { calculatePriority } from '@/lib/priority';

interface VideoQueueStore {
  videos: Video[];
  loading: boolean;
  error: string | null;

  // Actions
  fetchVideos: () => Promise<void>;
  addVideo: (url: string, department: string) => Promise<void>;
  removeVideo: (videoId: string) => Promise<void>;
  updateStatus: (videoId: string, status: Video['status']) => Promise<void>;
  updatePriority: (videoId: string, manualPriority: number) => Promise<void>;
  exportToCSV: () => Promise<void>;
}

export const useVideoQueueStore = create<VideoQueueStore>((set, get) => ({
  videos: [],
  loading: false,
  error: null,

  fetchVideos: async () => {
    set({ loading: true, error: null });
    try {
      const response = await fetch('/api/video-queue');
      const data = await response.json();
      set({ videos: data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  addVideo: async (url, department) => {
    set({ loading: true, error: null });
    try {
      // Extract YouTube video ID
      const videoId = extractYouTubeId(url);

      // Fetch metadata from YouTube API
      const metadata = await fetchYouTubeMetadata(videoId);

      // Calculate priority
      const priority = calculatePriority({
        views: metadata.views,
        likes: metadata.likes,
        publishedAt: new Date(metadata.publishedAt),
        manualPriority: 0
      });

      // Create video record
      const response = await fetch('/api/video-queue', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          youtube_url: url,
          video_id: videoId,
          title: metadata.title,
          channel: metadata.channel,
          thumbnail: metadata.thumbnail,
          duration: metadata.duration,
          views: metadata.views,
          likes: metadata.likes,
          upload_date: metadata.publishedAt,
          department,
          priority,
          status: 'Queued',
          source: 'Manual',
          date_added: new Date().toISOString()
        })
      });

      const newVideo = await response.json();

      set(state => ({
        videos: [...state.videos, newVideo].sort((a, b) => b.priority - a.priority),
        loading: false
      }));
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  removeVideo: async (videoId) => {
    try {
      await fetch(`/api/video-queue/${videoId}`, {
        method: 'DELETE'
      });
      set(state => ({
        videos: state.videos.filter(v => v.id !== videoId)
      }));
    } catch (error) {
      set({ error: error.message });
    }
  },

  updateStatus: async (videoId, status) => {
    try {
      await fetch(`/api/video-queue/${videoId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
      });
      await get().fetchVideos();
    } catch (error) {
      set({ error: error.message });
    }
  },

  updatePriority: async (videoId, manualPriority) => {
    try {
      const video = get().videos.find(v => v.id === videoId);
      if (!video) return;

      // Recalculate priority with manual boost
      const newPriority = calculatePriority({
        views: video.views,
        likes: video.likes,
        publishedAt: video.upload_date,
        manualPriority
      });

      await fetch(`/api/video-queue/${videoId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          manual_priority: manualPriority,
          priority: newPriority
        })
      });

      await get().fetchVideos();
    } catch (error) {
      set({ error: error.message });
    }
  },

  exportToCSV: async () => {
    try {
      const response = await fetch('/api/video-queue/export');
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `video-queue-${new Date().toISOString().split('T')[0]}.csv`;
      a.click();
    } catch (error) {
      set({ error: error.message });
    }
  }
}));

// Helper functions
function extractYouTubeId(url: string): string {
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)/,
    /youtube\.com\/embed\/([^&\n?#]+)/
  ];

  for (const pattern of patterns) {
    const match = url.match(pattern);
    if (match) return match[1];
  }

  throw new Error('Invalid YouTube URL');
}

async function fetchYouTubeMetadata(videoId: string) {
  const response = await fetch(`/api/youtube/metadata?videoId=${videoId}`);
  return response.json();
}
```

---

## 📦 DATA STORAGE (Dropbox API)

**CRITICAL:** This application uses **Dropbox API** for all data storage. **NO DATABASE** is used.

### Data Storage Architecture

All data is stored as JSON files in Dropbox:
- **Search Tasks:** `/RESEARCHES/Search_Queue/Search_Queue_Master.json`
- **Video Queue:** `/RESEARCHES/Video_Queue/Video_Queue_Master.json`
- **Settings:** `/RESEARCHES/Settings/settings.json`

### Dropbox API Service

```typescript
// src/services/dropboxService.ts
import { Dropbox } from 'dropbox';

export class DropboxService {
  private dbx: Dropbox;
  private accessToken: string;

  constructor(accessToken: string) {
    this.accessToken = accessToken;
    this.dbx = new Dropbox({ accessToken });
  }

  // Read JSON file from Dropbox
  async readFile<T>(path: string): Promise<T> {
    try {
      const response = await this.dbx.filesDownload({ path });
      const content = (response.result as any).fileBinary;
      const text = content.toString('utf-8');
      return JSON.parse(text);
    } catch (error) {
      if (error.status === 409) {
        // File not found, return empty array/object
        return ([] as unknown) as T;
      }
      throw error;
    }
  }

  // Write JSON file to Dropbox
  async writeFile<T>(path: string, data: T): Promise<void> {
    const content = JSON.stringify(data, null, 2);
    await this.dbx.filesUpload({
      path,
      contents: content,
      mode: { '.tag': 'overwrite' },
      mute: true
    });
  }

  // Append to JSON array file
  async appendToFile<T>(path: string, item: T): Promise<void> {
    const data = await this.readFile<T[]>(path);
    data.push(item);
    await this.writeFile(path, data);
  }

  // Update item in JSON array file
  async updateItem<T extends { id: string }>(
    path: string,
    id: string,
    updates: Partial<T>
  ): Promise<void> {
    const data = await this.readFile<T[]>(path);
    const index = data.findIndex(item => item.id === id);
    if (index !== -1) {
      data[index] = { ...data[index], ...updates, updatedAt: new Date().toISOString() };
      await this.writeFile(path, data);
    }
  }

  // Delete item from JSON array file
  async deleteItem<T extends { id: string }>(path: string, id: string): Promise<void> {
    const data = await this.readFile<T[]>(path);
    const filtered = data.filter(item => item.id !== id);
    await this.writeFile(path, filtered);
  }

  // Get item by ID
  async getItemById<T extends { id: string }>(path: string, id: string): Promise<T | null> {
    const data = await this.readFile<T[]>(path);
    return data.find(item => item.id === id) || null;
  }

  // List all items with filters
  async listItems<T>(
    path: string,
    filters?: {
      status?: string;
      department?: string;
      priority?: { min?: number; max?: number };
    }
  ): Promise<T[]> {
    const data = await this.readFile<T[]>(path);
    
    if (!filters) return data;

    return data.filter(item => {
      if (filters.status && (item as any).status !== filters.status) return false;
      if (filters.department && (item as any).department !== filters.department) return false;
      if (filters.priority) {
        const priority = (item as any).priority || 0;
        if (filters.priority.min !== undefined && priority < filters.priority.min) return false;
        if (filters.priority.max !== undefined && priority > filters.priority.max) return false;
      }
      return true;
    });
  }
}
```

### Data Models (TypeScript Interfaces)

```typescript
// src/types/index.ts

export interface SearchTask {
  id: string;                    // Unique ID (cuid)
  search_id: string;             // Display ID (SRH-001, SRH-002, etc.)
  employee: string;              // Employee name
  department: string;            // Department code (VID, AID, DEV, etc.)
  topic: string;                 // Search topic/objective
  search_query?: string;         // AI-generated search query
  status: 'Assigned' | 'In_Progress' | 'Completed';
  priority: number;              // 0-100 priority score
  date_assigned: string;         // ISO date string
  date_completed?: string;       // ISO date string
  videos_found: number;          // Count of results
  results?: SearchResult[];      // Array of found videos
  notes?: string;
  createdAt: string;             // ISO date string
  updatedAt: string;             // ISO date string
}

export interface SearchResult {
  title: string;
  url: string;
  channel: string;
  views: number;
  duration: string;
  upload_date: string;
  relevance_score: number;       // 0-100 calculated by AI
  thumbnail: string;
}

export interface Video {
  id: string;                    // Unique ID (cuid)
  vq_id: string;                 // Display ID (VQ-001, VQ-002, etc.)
  youtube_url: string;           // Full YouTube URL
  video_id: string;              // YouTube video ID
  title: string;
  channel: string;
  thumbnail: string;             // Thumbnail URL
  duration: string;              // Format: "PT15M33S" or "15:33"
  views: number;
  likes: number;
  upload_date: string;          // ISO date string
  topic?: string;
  source: 'Manual' | 'Search_Queue' | 'Dropbox';
  employee: string;
  department: string;
  priority: number;              // 0-100 calculated score
  manual_priority?: number;      // Manual boost (0-20)
  status: 'Queued' | 'Selected' | 'In_Progress' | 'Completed';
  processing_phase?: 'Phase_1_Transcribed' | 'Phase_2_Extraction' | 'Phase_3_Gap_Analysis' | 'Phase_4_Integration' | 'Phase_5_Mapping';
  date_added: string;            // ISO date string
  date_selected?: string;        // ISO date string
  date_completed?: string;       // ISO date string
  notes?: string;
  createdAt: string;             // ISO date string
  updatedAt: string;             // ISO date string
}

export interface AppSettings {
  dropboxAccessToken: string;
  openaiApiKey?: string;
  youtubeApiKey?: string;
  perplexityApiKey?: string;
  updatedAt: string;
}
```

---

## 🖥️ BACKEND APPLICATION (Express.js)

### Backend Architecture

**Port:** 5000 (default)
**Base URL:** `http://localhost:5000/api`
**CORS:** Enabled for `http://localhost:3000` (Frontend)

### Project Structure

```bash
backend/
├── src/
│   ├── server.ts              # Express app entry point
│   ├── routes/
│   │   ├── search-queue.ts    # Search queue routes
│   │   ├── video-queue.ts     # Video queue routes
│   │   ├── youtube.ts         # YouTube API routes
│   │   ├── settings.ts        # Settings API routes
│   │   └── index.ts           # Route aggregator
│   ├── controllers/
│   │   ├── searchQueueController.ts
│   │   ├── videoQueueController.ts
│   │   ├── youtubeController.ts
│   │   └── settingsController.ts
│   ├── services/
│   │   ├── openaiService.ts   # OpenAI integration
│   │   ├── youtubeService.ts  # YouTube Data API
│   │   ├── dropboxService.ts  # Dropbox API (primary data storage)
│   │   └── priorityService.ts # Priority calculation
│   ├── middleware/
│   │   ├── errorHandler.ts
│   │   ├── validator.ts
│   │   └── cors.ts
│   └── types/
│       └── index.ts           # TypeScript types
├── package.json
├── tsconfig.json
└── .env
```

### Server Setup (server.ts)

```typescript
// src/server.ts
import express, { Express, Request, Response } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import dotenv from 'dotenv';
import routes from './routes';
import { errorHandler } from './middleware/errorHandler';

dotenv.config();

const app: Express = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(helmet()); // Security headers
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev')); // Logging

// Health check
app.get('/health', (req: Request, res: Response) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// API Routes
app.use('/api', routes);

// Error handling
app.use(errorHandler);

// Start server
app.listen(PORT, () => {
  console.log(`✅ Backend server running on http://localhost:${PORT}`);
  console.log(`📊 API endpoints: http://localhost:${PORT}/api`);
  console.log(`🔍 Health check: http://localhost:${PORT}/health`);
});

export default app;
```

### Routes (routes/index.ts)

```typescript
// src/routes/index.ts
import { Router } from 'express';
import searchQueueRoutes from './search-queue';
import videoQueueRoutes from './video-queue';
import youtubeRoutes from './youtube';

const router = Router();

router.use('/search-queue', searchQueueRoutes);
router.use('/video-queue', videoQueueRoutes);
router.use('/youtube', youtubeRoutes);

export default router;
```

### Search Queue Routes

```typescript
// src/routes/search-queue.ts
import { Router } from 'express';
import {
  getAllTasks,
  createTask,
  updateTask,
  deleteTask,
  executeSearch
} from '../controllers/searchQueueController';
import { validateSearchTask } from '../middleware/validator';

const router = Router();

// GET /api/search-queue - Get all search tasks
router.get('/', getAllTasks);

// POST /api/search-queue - Create new search task
router.post('/', validateSearchTask, createTask);

// PATCH /api/search-queue/:id - Update search task
router.patch('/:id', updateTask);

// DELETE /api/search-queue/:id - Delete search task
router.delete('/:id', deleteTask);

// POST /api/search-queue/execute - Execute search with AI
router.post('/execute', executeSearch);

export default router;
```

### Search Queue Controller (Dropbox API)

```typescript
// src/controllers/searchQueueController.ts
import { Request, Response } from 'express';
import { DropboxService } from '../services/dropboxService';
import { executeOpenAISearch } from '../services/openaiService';
import { SearchTask } from '../types';
import { v4 as uuidv4 } from 'uuid';

const SEARCH_QUEUE_PATH = '/RESEARCHES/Search_Queue/Search_Queue_Master.json';

// Get Dropbox service instance (from settings)
function getDropboxService(req: Request): DropboxService {
  const accessToken = req.headers['x-dropbox-token'] as string || process.env.DROPBOX_ACCESS_TOKEN;
  if (!accessToken) {
    throw new Error('Dropbox access token not provided');
  }
  return new DropboxService(accessToken);
}

export async function getAllTasks(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const tasks = await dbx.listItems<SearchTask>(SEARCH_QUEUE_PATH);
    
    // Sort tasks
    tasks.sort((a, b) => {
      if (a.status !== b.status) {
        const statusOrder = { 'Assigned': 0, 'In_Progress': 1, 'Completed': 2 };
        return statusOrder[a.status] - statusOrder[b.status];
      }
      if (b.priority !== a.priority) return b.priority - a.priority;
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    });
    
    res.json(tasks);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function createTask(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const body = req.body;

    // Get all tasks to generate next search_id
    const allTasks = await dbx.listItems<SearchTask>(SEARCH_QUEUE_PATH);
    const lastTask = allTasks
      .filter(t => t.search_id.startsWith('SRH-'))
      .sort((a, b) => {
        const numA = parseInt(a.search_id.split('-')[1]) || 0;
        const numB = parseInt(b.search_id.split('-')[1]) || 0;
        return numB - numA;
      })[0];

    const nextId = lastTask
      ? `SRH-${String(parseInt(lastTask.search_id.split('-')[1]) + 1).padStart(3, '0')}`
      : 'SRH-001';

    const now = new Date().toISOString();
    const task: SearchTask = {
      id: uuidv4(),
      search_id: nextId,
      employee: body.employee,
      department: body.department,
      topic: body.topic,
      search_query: body.search_query,
      priority: body.priority || 50,
      status: 'Assigned',
      videos_found: 0,
      date_assigned: now,
      createdAt: now,
      updatedAt: now
    };

    await dbx.appendToFile(SEARCH_QUEUE_PATH, task);
    res.status(201).json(task);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function updateTask(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const { id } = req.params;
    const updates = req.body;

    await dbx.updateItem<SearchTask>(SEARCH_QUEUE_PATH, id, updates);
    const updated = await dbx.getItemById<SearchTask>(SEARCH_QUEUE_PATH, id);
    res.json(updated);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function deleteTask(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const { id } = req.params;
    await dbx.deleteItem<SearchTask>(SEARCH_QUEUE_PATH, id);
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function executeSearch(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const { taskId, query } = req.body;

    // Update status to In_Progress
    await dbx.updateItem<SearchTask>(SEARCH_QUEUE_PATH, taskId, {
      status: 'In_Progress'
    });

    // Get OpenAI API key from settings
    const settings = await dbx.readFile<{ openaiApiKey?: string }>('/RESEARCHES/Settings/settings.json');
    const openaiApiKey = settings.openaiApiKey || process.env.OPENAI_API_KEY;

    if (!openaiApiKey) {
      throw new Error('OpenAI API key not configured');
    }

    // Execute search with OpenAI
    const results = await executeOpenAISearch(query, openaiApiKey);

    // Update task with results
    await dbx.updateItem<SearchTask>(SEARCH_QUEUE_PATH, taskId, {
      status: 'Completed',
      videos_found: results.length,
      results: results,
      date_completed: new Date().toISOString()
    });

    res.json({ success: true, results });
  } catch (error) {
    // Revert status on error
    try {
      const dbx = getDropboxService(req);
      await dbx.updateItem<SearchTask>(SEARCH_QUEUE_PATH, req.body.taskId, {
        status: 'Assigned'
      });
    } catch {}

    res.status(500).json({ error: error.message });
  }
}
```

### Video Queue Controller (Dropbox API)

```typescript
// src/controllers/videoQueueController.ts
import { Request, Response } from 'express';
import { DropboxService } from '../services/dropboxService';
import { Video } from '../types';
import { v4 as uuidv4 } from 'uuid';
import { calculatePriority } from '../services/priorityService';
import { fetchYouTubeMetadata } from '../services/youtubeService';

const VIDEO_QUEUE_PATH = '/RESEARCHES/Video_Queue/Video_Queue_Master.json';

function getDropboxService(req: Request): DropboxService {
  const accessToken = req.headers['x-dropbox-token'] as string || process.env.DROPBOX_ACCESS_TOKEN;
  if (!accessToken) {
    throw new Error('Dropbox access token not provided');
  }
  return new DropboxService(accessToken);
}

export async function getAllVideos(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const videos = await dbx.listItems<Video>(VIDEO_QUEUE_PATH);
    
    videos.sort((a, b) => {
      if (b.priority !== a.priority) return b.priority - a.priority;
      return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
    });
    
    res.json(videos);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function addVideo(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const body = req.body;

    // Extract YouTube video ID
    const videoId = extractYouTubeId(body.youtube_url);

    // Get YouTube API key from settings
    const settings = await dbx.readFile<{ youtubeApiKey?: string }>('/RESEARCHES/Settings/settings.json');
    const youtubeApiKey = settings.youtubeApiKey || process.env.YOUTUBE_API_KEY;

    if (!youtubeApiKey) {
      throw new Error('YouTube API key not configured');
    }

    // Fetch metadata from YouTube
    const metadata = await fetchYouTubeMetadata(videoId, youtubeApiKey);

    // Calculate priority
    const priority = calculatePriority({
      views: metadata.views,
      likes: metadata.likes,
      publishedAt: new Date(metadata.publishedAt),
      manualPriority: body.manual_priority || 0
    });

    // Generate next vq_id
    const allVideos = await dbx.listItems<Video>(VIDEO_QUEUE_PATH);
    const lastVideo = allVideos
      .filter(v => v.vq_id.startsWith('VQ-'))
      .sort((a, b) => {
        const numA = parseInt(a.vq_id.split('-')[1]) || 0;
        const numB = parseInt(b.vq_id.split('-')[1]) || 0;
        return numB - numA;
      })[0];

    const nextId = lastVideo
      ? `VQ-${String(parseInt(lastVideo.vq_id.split('-')[1]) + 1).padStart(3, '0')}`
      : 'VQ-001';

    const now = new Date().toISOString();
    const video: Video = {
      id: uuidv4(),
      vq_id: nextId,
      youtube_url: body.youtube_url,
      video_id: videoId,
      title: metadata.title,
      channel: metadata.channel,
      thumbnail: metadata.thumbnail,
      duration: metadata.duration,
      views: metadata.views,
      likes: metadata.likes,
      upload_date: metadata.publishedAt,
      topic: body.topic,
      source: body.source || 'Manual',
      employee: body.employee,
      department: body.department,
      priority,
      manual_priority: body.manual_priority,
      status: 'Queued',
      date_added: now,
      createdAt: now,
      updatedAt: now,
      notes: body.notes
    };

    await dbx.appendToFile(VIDEO_QUEUE_PATH, video);
    res.status(201).json(video);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function updateVideo(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const { id } = req.params;
    const updates = req.body;

    await dbx.updateItem<Video>(VIDEO_QUEUE_PATH, id, updates);
    const updated = await dbx.getItemById<Video>(VIDEO_QUEUE_PATH, id);
    res.json(updated);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function deleteVideo(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const { id } = req.params;
    await dbx.deleteItem<Video>(VIDEO_QUEUE_PATH, id);
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function exportToCSV(req: Request, res: Response) {
  try {
    const dbx = getDropboxService(req);
    const videos = await dbx.listItems<Video>(VIDEO_QUEUE_PATH);
    
    videos.sort((a, b) => b.priority - a.priority);

    const headers = ['VQ ID', 'Title', 'Channel', 'Priority', 'Status', 'Views', 'Department', 'Date Added', 'URL'];
    const rows = videos.map(v => [
      v.vq_id,
      v.title,
      v.channel,
      v.priority.toString(),
      v.status,
      v.views.toString(),
      v.department,
      new Date(v.date_added).toLocaleDateString(),
      v.youtube_url
    ]);

    const csv = [headers, ...rows].map(row => row.join(',')).join('\n');

    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', `attachment; filename="video-queue-${new Date().toISOString().split('T')[0]}.csv"`);
    res.send(csv);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

function extractYouTubeId(url: string): string {
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)/,
    /youtube\.com\/embed\/([^&\n?#]+)/
  ];

  for (const pattern of patterns) {
    const match = url.match(pattern);
    if (match) return match[1];
  }

  throw new Error('Invalid YouTube URL');
}
```

---

## 🎨 SHARED COMPONENTS

### ThemeContext (Dark Mode Support with shadcn/ui)

**CRITICAL:** Use shadcn/ui's built-in theme provider. shadcn/ui uses CSS variables for theming.

```typescript
// contexts/ThemeContext.tsx
import React, { createContext, useContext, useState, useEffect } from 'react';
import { useTheme as useShadcnTheme } from 'next-themes';

type Theme = 'light' | 'dark' | 'system';

interface ThemeContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  resolvedTheme: 'light' | 'dark' | undefined;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const { theme, setTheme, resolvedTheme } = useShadcnTheme();

  return (
    <ThemeContext.Provider value={{
      theme: theme as Theme,
      setTheme: setTheme as (theme: Theme) => void,
      resolvedTheme
    }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme must be used within ThemeProvider');
  return context;
};
```

**Setup next-themes:**
```bash
npm install next-themes
```

**App Layout Integration:**
```typescript
// app/layout.tsx or src/App.tsx
import { ThemeProvider as NextThemesProvider } from 'next-themes';
import { ThemeProvider } from '@/contexts/ThemeContext';

export function App() {
  return (
    <NextThemesProvider attribute="class" defaultTheme="light" enableSystem>
      <ThemeProvider>
        {/* Your app */}
      </ThemeProvider>
    </NextThemesProvider>
  );
}
```

**Theme Toggle Component (using shadcn/ui):**
```typescript
// components/ThemeToggle.tsx
import { Moon, Sun } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { useTheme } from '@/contexts/ThemeContext';

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <Button
      variant="outline"
      size="icon"
      onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
    >
      <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  );
}
```

### ErrorBoundary

```typescript
// components/ErrorBoundary.tsx
import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);

    // Log to error tracking service (Sentry, etc.)
    if (typeof window !== 'undefined' && window.analytics) {
      window.analytics.track('Error', {
        error: error.message,
        stack: error.stack,
        componentStack: errorInfo.componentStack
      });
    }
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="error-container p-8 text-center">
          <h2 className="text-h2 font-semibold mb-4">Something went wrong</h2>
          <p className="text-body mb-6">{this.state.error?.message}</p>
          <button
            onClick={() => window.location.reload()}
            className="btn-primary"
          >
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

### Loading & Empty States

```typescript
// components/LoadingSpinner.tsx
import { Loader2 } from 'lucide-react';
import { cn } from '@/lib/utils';

export function LoadingSpinner({ 
  size = 'md',
  className 
}: { 
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}) {
  const sizeClasses = {
    sm: 'h-4 w-4',
    md: 'h-8 w-8',
    lg: 'h-12 w-12'
  };

  return (
    <Loader2 className={cn('animate-spin text-primary', sizeClasses[size], className)} />
  );
}

// components/EmptyState.tsx
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export function EmptyState({
  icon,
  title,
  description,
  action
}: {
  icon?: React.ReactNode;
  title: string;
  description: string;
  action?: React.ReactNode;
}) {
  return (
    <Card className="border-dashed">
      <CardContent className="flex flex-col items-center justify-center py-12 text-center">
        {icon && <div className="mb-4 text-muted-foreground">{icon}</div>}
        <h3 className="text-lg font-semibold mb-2">{title}</h3>
        <p className="text-sm text-muted-foreground mb-6 max-w-sm">{description}</p>
        {action}
      </CardContent>
    </Card>
  );
}
```

---

## ⚙️ ENVIRONMENT VARIABLES

**Backend .env:**
```bash
# .env (Backend)

# Server
PORT=5000
FRONTEND_URL=http://localhost:3000
NODE_ENV=development

# Dropbox API (REQUIRED - can also be configured in Settings UI)
DROPBOX_ACCESS_TOKEN="sl.Bx..."

# Optional API Keys (can be configured in Settings UI)
OPENAI_API_KEY="sk-..."
YOUTUBE_API_KEY="AIza..."
PERPLEXITY_API_KEY="pplx-..."
```

**Frontend .env:**
```bash
# .env (Frontend)
VITE_API_URL=http://localhost:5000/api
VITE_APP_URL=http://localhost:3000
```

**Note:** API keys can be configured either:
1. In backend `.env` file (for development)
2. In Settings page UI (stored in Dropbox `/RESEARCHES/Settings/settings.json`)

Settings page takes precedence over `.env` file.

---

## 📦 DEPLOYMENT

### Vercel Deployment

```json
// vercel.json (Frontend)
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "vite",
  "env": {
    "VITE_API_URL": "@api-url",
    "VITE_APP_URL": "@app-url"
  }
}
```

**Backend Deployment (Railway/Render/Heroku):**
```bash
# Set environment variables:
DROPBOX_ACCESS_TOKEN=sl.Bx...
OPENAI_API_KEY=sk-... (optional)
YOUTUBE_API_KEY=AIza... (optional)
PERPLEXITY_API_KEY=pplx-... (optional)
FRONTEND_URL=https://your-frontend.vercel.app
```

### Dropbox API Setup

**CRITICAL:** No database setup required. All data is stored in Dropbox.

**Steps:**
1. Create Dropbox App at https://www.dropbox.com/developers/apps
2. Generate Access Token (with `files.content.read` and `files.content.write` permissions)
3. Configure token in Settings page (frontend) or set `DROPBOX_ACCESS_TOKEN` in backend `.env`

**Required Dropbox Permissions:**
- `files.content.read` - Read JSON files
- `files.content.write` - Write/update JSON files
- `files.metadata.read` - List files and folders

**Dropbox File Structure:**
```
/RESEARCHES/
├── Search_Queue/
│   └── Search_Queue_Master.json
├── Video_Queue/
│   └── Video_Queue_Master.json
└── Settings/
    └── settings.json
```

---

## ✅ IMPLEMENTATION CHECKLIST

### Design System Integration
- [ ] design-system.json copied to `src/design-system/`
- [ ] Tailwind CSS v4 configured with @theme directive
- [ ] shadcn/ui initialized with Tailwind v4
- [ ] All shadcn/ui components installed
- [ ] All components use shadcn/ui (Button, Card, Dialog, Input, etc.)
- [ ] No custom button/card/modal components (use shadcn/ui)
- [ ] Tailwind config imports from JSON (or uses @theme)
- [ ] All components use colorPalette from JSON (no hardcoded colors)
- [ ] Typography uses Roboto with correct weights (300, 400, 500, 600, 700)
- [ ] Spacing uses 4px base unit from JSON
- [ ] Border radius correct (buttons 8px, cards 12px, badges 9999px)
- [ ] Shadows use values from JSON
- [ ] Transitions use 150ms/300ms/500ms from JSON
- [ ] Sidebar #1F2937 (dark even in light theme)
- [ ] Scrollbar 6px width (NOT 8px!)
- [ ] Department colors correct (#6D28D9 Search, #147857 Video)
- [ ] Priority 5-tier system with stars implemented
- [ ] Dark mode fully supported with next-themes + ThemeContext
- [ ] lib/utils.ts created with cn() function

### Search Queue Module
- [ ] SearchQueueDashboard component
- [ ] SearchTaskCard component
- [ ] CreateSearchTaskModal component
- [ ] SearchResultsModal component
- [ ] SearchQueueStats component
- [ ] StatusBadge component
- [ ] PriorityBadge component
- [ ] Zustand store (searchQueueStore.ts)
- [ ] API routes (/api/search-queue)
- [ ] OpenAI integration for search execution
- [ ] Filters (status, department, priority)
- [ ] Sort (priority, date)
- [ ] Dropbox API integration for Search Queue storage

### Video Queue Module
- [ ] VideoQueueDashboard component
- [ ] VideoCard component (grid & list views)
- [ ] AddVideoModal component
- [ ] VideoQueueStats component
- [ ] FilterPanel component
- [ ] PriorityBadge component (reused)
- [ ] Zustand store (videoQueueStore.ts)
- [ ] API routes (/api/video-queue)
- [ ] YouTube Data API integration
- [ ] Priority calculation algorithm
- [ ] Grid/List view toggle
- [ ] Filters (status, priority, department)
- [ ] Sort (priority, date, views)
- [ ] CSV export functionality
- [ ] Dropbox API integration for Video Queue storage

### Settings Module
- [ ] SettingsPage component (frontend)
- [ ] Settings API routes (/api/settings)
- [ ] Dropbox Access Token configuration
- [ ] OpenAI API Key configuration
- [ ] YouTube API Key configuration
- [ ] Perplexity API Key configuration
- [ ] Settings stored in Dropbox (/RESEARCHES/Settings/settings.json)

### Shared Architecture
- [ ] AppLayout component
- [ ] Header component
- [ ] Sidebar component (256px/80px) - using shadcn/ui components
- [ ] ThemeContext (light/dark mode) - using next-themes
- [ ] ThemeToggle component - using shadcn/ui Button
- [ ] ErrorBoundary component
- [ ] LoadingSpinner component - using lucide-react Loader2
- [ ] EmptyState component - using shadcn/ui Card
- [ ] PriorityBadge component (shared) - using shadcn/ui Badge
- [ ] StatusBadge component (shared) - using shadcn/ui Badge
- [ ] lib/utils.ts with cn() function for className merging

### Dropbox API & Backend
- [ ] DropboxService implemented
- [ ] Dropbox API integration complete
- [ ] Settings API routes implemented
- [ ] All API routes implemented
- [ ] Error handling in all routes
- [ ] Input validation with Zod
- [ ] TypeScript types for all models
- [ ] Dropbox file structure created

### Code Quality
- [ ] TypeScript strict mode enabled
- [ ] No 'any' types
- [ ] All components have proper types
- [ ] Error handling throughout
- [ ] Loading states everywhere
- [ ] Empty states for lists
- [ ] Accessibility (ARIA labels)
- [ ] SEO meta tags
- [ ] Performance optimized

---

## 🚀 GETTING STARTED

### 1. Project Setup

```bash
# Create Vite + React app (NOT Next.js - separate frontend)
npm create vite@latest frontend -- --template react-ts

cd frontend

# Install dependencies
npm install

# Install Tailwind CSS v4
npm install -D tailwindcss@next postcss autoprefixer
npx tailwindcss init -p

# Install shadcn/ui
npx shadcn@latest init
# Select: new-york style, base color: slate, CSS variables: yes

# Install core dependencies
npm install zustand @tanstack/react-query @tanstack/react-table
npm install react-hook-form zod @hookform/resolvers/zod
npm install recharts axios
npm install next-themes  # For theme management
npm install lucide-react  # Icons for shadcn/ui
npm install clsx tailwind-merge  # Utility functions
npm install class-variance-authority  # For component variants

# Install shadcn/ui components
npx shadcn@latest add button card dialog input label select textarea badge dropdown-menu table tabs sonner skeleton separator

# Install dev dependencies
npm install -D @types/node @types/react @types/react-dom
```

### 2. Setup shadcn/ui Utilities

**CRITICAL:** Create `lib/utils.ts` file (required by shadcn/ui):

```typescript
// src/lib/utils.ts
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

This utility function is used throughout shadcn/ui components for merging className strings.

### 3. Copy Design System

```bash
# Create directory
mkdir -p src/design-system

# Copy design-system.json to src/design-system/
```

### 4. Setup Backend (Express.js)

```bash
# Create backend directory
mkdir backend
cd backend

# Initialize Node.js project
npm init -y

# Install dependencies
npm install express cors helmet morgan dotenv
npm install dropbox  # Dropbox API SDK
npm install openai googleapis  # AI and YouTube APIs
npm install zod uuid  # Validation and ID generation
npm install axios  # HTTP client

# Install dev dependencies
npm install -D typescript @types/node @types/express @types/cors ts-node nodemon

# Initialize TypeScript
npx tsc --init
```

**Backend .env file:**
```bash
# .env
PORT=5000
FRONTEND_URL=http://localhost:3000

# Dropbox API (REQUIRED)
DROPBOX_ACCESS_TOKEN=sl.Bx...

# Optional API Keys (can be configured in Settings UI)
OPENAI_API_KEY=sk-...
YOUTUBE_API_KEY=AIza...
PERPLEXITY_API_KEY=pplx-...
```

### 5. Setup Dropbox API

**Steps:**
1. Go to https://www.dropbox.com/developers/apps
2. Click "Create app"
3. Choose:
   - **API:** Dropbox API
   - **Access level:** Full Dropbox
   - **App name:** Research Management System
4. Generate Access Token (with `files.content.read` and `files.content.write` permissions)
5. Add token to backend `.env` file or configure in Settings page

**Create Dropbox folder structure:**
The application will automatically create the following structure on first use:
```
/RESEARCHES/
├── Search_Queue/
│   └── Search_Queue_Master.json  (empty array initially)
├── Video_Queue/
│   └── Video_Queue_Master.json   (empty array initially)
└── Settings/
    └── settings.json              (created on first settings save)
```

### 6. Create File Structure

```
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── search-queue/
│   │   └── page.tsx
│   ├── video-queue/
│   │   └── page.tsx
│   └── api/
│       ├── search-queue/
│       │   ├── route.ts
│       │   ├── [id]/route.ts
│       │   └── execute/route.ts
│       ├── video-queue/
│       │   ├── route.ts
│       │   ├── [id]/route.ts
│       │   └── export/route.ts
│       └── youtube/
│           └── metadata/route.ts
├── components/
│   ├── ui/                    # shadcn/ui components (auto-generated)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── input.tsx
│   │   ├── label.tsx
│   │   ├── select.tsx
│   │   ├── textarea.tsx
│   │   ├── badge.tsx
│   │   ├── table.tsx
│   │   ├── tabs.tsx
│   │   └── ...
│   ├── search-queue/
│   │   ├── SearchQueueDashboard.tsx
│   │   ├── SearchTaskCard.tsx
│   │   ├── CreateSearchTaskModal.tsx
│   │   └── SearchResultsModal.tsx
│   ├── video-queue/
│   │   ├── VideoQueueDashboard.tsx
│   │   ├── VideoCard.tsx
│   │   └── AddVideoModal.tsx
│   ├── settings/
│   │   └── SettingsPage.tsx
│   └── shared/
│       ├── PriorityBadge.tsx
│       ├── StatusBadge.tsx
│       ├── LoadingSpinner.tsx
│       ├── EmptyState.tsx
│       └── ThemeToggle.tsx
├── stores/
│   ├── searchQueueStore.ts
│   └── videoQueueStore.ts
├── contexts/
│   └── ThemeContext.tsx        # Wrapper for next-themes
├── lib/
│   ├── utils.ts                # cn() utility for className merging (REQUIRED for shadcn/ui)
│   ├── priority.ts
│   └── types.ts
├── design-system/
│   └── design-system.json
└── styles/
    └── globals.css
```

### 6. Start Development

#### Backend (Terminal 1)

```bash
cd backend
npm install
npm run dev
# ✅ Backend running on http://localhost:5000
```

#### Frontend (Terminal 2)

```bash
cd frontend
npm install
npm run dev
# ✅ Frontend running on http://localhost:3000
```

---

## 📚 ADDITIONAL RESOURCES

### Architecture

- `ARCHITECTURE-OVERVIEW.md` - Separated Backend/Frontend architecture guide

### Design System Files
- `design-system.json` - Complete design specification
- `DESIGN-SYSTEM-INTEGRATION-GUIDE.md` - Integration guide
- `_DESIGN-SYSTEM-SNIPPET.md` - Quick reference
- `design-system-analysis.md` - Detailed analysis

### Reference URLs
- **Video Catalog:** https://adminrhs.github.io/Video-catalog/
- **Design System:** https://adminrhs.github.io/Design-system/

### API Documentation

- **YouTube Data API:** https://developers.google.com/youtube/v3
- **OpenAI API:** https://platform.openai.com/docs
- **Dropbox API:** https://www.dropbox.com/developers/documentation
- **Express.js:** https://expressjs.com/
- **React:** https://react.dev/
- **Vite:** https://vitejs.dev/
- **shadcn/ui:** https://ui.shadcn.com/

---

## 🎯 SUCCESS CRITERIA

### Backend (Express.js)

✅ Separate Express.js application on port 5000
✅ All REST API endpoints functional (/api/search-queue, /api/video-queue, /api/settings)
✅ CORS properly configured for frontend origin
✅ Dropbox API integration complete (no database)
✅ Settings page for API key configuration
✅ OpenAI integration for search execution
✅ YouTube Data API integration for video metadata
✅ Priority calculation algorithm implemented
✅ Error handling middleware
✅ Input validation with Zod
✅ TypeScript strict mode (no 'any' types)
✅ Deployment ready for Railway/Render/Heroku

### Frontend (React)

✅ Separate React application on port 3000
✅ React 19 (latest version)
✅ Tailwind CSS v4+ configured
✅ shadcn/ui components integrated (all UI components from shadcn/ui)
✅ 100% integration with design-system.json (no hardcoded values)
✅ Search Queue dashboard fully functional
✅ Video Queue dashboard fully functional
✅ Axios HTTP client configured for backend API
✅ Zustand stores for state management + React Context API
✅ TanStack Query for data fetching
✅ Dark mode working throughout with next-themes + ThemeContext
✅ All error/loading/empty states implemented (using shadcn/ui)
✅ Responsive on mobile/tablet/desktop
✅ TypeScript strict mode (no 'any' types)
✅ Deployment ready for Vercel/Netlify

### Integration

✅ Backend and Frontend communicate via REST API
✅ CORS configured correctly
✅ Environment variables properly configured
✅ Dropbox API configured (via Settings or .env)
✅ Can run both apps locally in development
✅ Can deploy separately to production
✅ Data stored in Dropbox (no database required)
✅ API keys configurable via Settings UI (stored in Dropbox)

---

## 📦 DELIVERABLES

### 2 Separate Applications

1. **Backend (Express.js)**
   - Location: `backend/`
   - Package: Node.js + Express.js + Dropbox API
   - Port: 5000
   - Data Storage: Dropbox API (no database)
   - Deploy: Railway/Render/Heroku

2. **Frontend (React)**
   - Location: `frontend/`
   - Package: React 19 (latest) + Vite + TypeScript
   - UI: shadcn/ui + Tailwind CSS v4+
   - State: Zustand + React Context API
   - Port: 3000
   - Deploy: Vercel/Netlify

### Documentation

- ✅ `COMPLETE-APP-GENERATION-PROMPT.md` (this file)
- ✅ `ARCHITECTURE-OVERVIEW.md` (architecture guide)
- ✅ `design-system.json` (design specification)
- ✅ `DESIGN-SYSTEM-INTEGRATION-GUIDE.md`
- ✅ `FUNCTIONAL.md` (functional requirements)

---

**END OF PROMPT**

**Generated:** 2025-12-09
**Version:** 3.1 - React 19 + shadcn/ui + Tailwind CSS v4 + Dropbox API
**Architecture:** Express.js (Backend) + React 19 + shadcn/ui (Frontend)
**UI Framework:** shadcn/ui (latest) + Tailwind CSS v4+
**Data Storage:** Dropbox API (no database)
**State Management:** Zustand + React Context API
**Settings:** Configurable API keys via Settings UI
**Total Lines:** ~3,200
**Status:** ✅ Ready for Implementation
