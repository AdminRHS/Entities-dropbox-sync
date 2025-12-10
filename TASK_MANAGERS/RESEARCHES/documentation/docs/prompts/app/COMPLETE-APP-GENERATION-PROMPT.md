# COMPLETE APPLICATION GENERATION PROMPT
# Research Management System - Search & Video Queue Application

**Version:** 2.0
**Date:** 2025-12-09
**Purpose:** Complete prompt for generating a production-ready Search Queue and Video Queue management application
**Design System:** Game Academy Design System v1.0 (October 2025)

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
    "framework": "React 19",
    "language": "TypeScript 5.0+",
    "buildTool": "Vite",
    "styling": "Tailwind CSS v4",
    "stateManagement": "Zustand",
    "dataFetching": "TanStack Query (React Query)",
    "forms": "React Hook Form + Zod",
    "tables": "TanStack Table",
    "charts": "Recharts",
    "http": "Axios"
  },
  "backend": {
    "runtime": "Node.js 20+",
    "framework": "Express.js 4.18+",
    "database": "PostgreSQL 15+ (Supabase/Neon)",
    "orm": "Prisma ORM",
    "validation": "Zod",
    "cors": "CORS middleware",
    "auth": "JWT (jsonwebtoken)",
    "apiDocs": "Swagger/OpenAPI"
  },
  "integrations": {
    "ai": ["OpenAI GPT-4", "Google Gemini"],
    "video": "YouTube Data API v3",
    "storage": "Dropbox API",
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
    ├── prisma/
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

### Tailwind Configuration

```typescript
// tailwind.config.ts
import designSystem from './src/design-system/design-system.json';

const { colorPalette, typography, spacing, borderRadius, shadows } = designSystem.designSystem;

export default {
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
  plugins: []
};
```

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
import designSystem from '@/design-system/design-system.json';

const { colorPalette, spacing, typography } = designSystem.designSystem;

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
        <button
          onClick={() => setIsCreateModalOpen(true)}
          className="btn-primary"
          style={{
            backgroundColor: '#6D28D9', // Search module color
            color: '#ffffff',
            padding: `${spacing['space-3']} ${spacing['space-6']}`,
            borderRadius: designSystem.designSystem.borderRadius.button,
            fontSize: typography.body.default.fontSize,
            fontWeight: 500,
            transition: 'all 300ms ease',
            display: 'flex',
            alignItems: 'center',
            gap: spacing['space-2']
          }}
        >
          <span>➕</span>
          <span>New Search Task</span>
        </button>
      </header>

      {/* Statistics */}
      <SearchQueueStats tasks={tasks} />

      {/* Filters */}
      <div className="flex items-center gap-4 mb-6">
        {/* Status Filter */}
        <div className="filter-group flex items-center gap-2">
          <span className="text-body-sm text-text-secondary">Status:</span>
          {['All', 'Assigned', 'In_Progress', 'Completed'].map(status => (
            <button
              key={status}
              onClick={() => setStatusFilter(status)}
              className={`filter-button ${statusFilter === status ? 'active' : ''}`}
              style={{
                padding: `${spacing['space-2']} ${spacing['space-4']}`,
                borderRadius: designSystem.designSystem.borderRadius.small,
                fontSize: typography.body.small.fontSize,
                fontWeight: 500,
                backgroundColor: statusFilter === status ? '#6D28D9' : 'transparent',
                color: statusFilter === status ? '#ffffff' : colorPalette.text.secondary,
                border: `1px solid ${statusFilter === status ? '#6D28D9' : colorPalette.border.default}`,
                transition: 'all 150ms ease'
              }}
            >
              {status.replace('_', ' ')}
            </button>
          ))}
        </div>

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
import designSystem from '@/design-system/design-system.json';

const { colorPalette, spacing, components } = designSystem.designSystem;

interface SearchTaskCardProps {
  task: SearchTask;
  onExecute: (taskId: string) => void;
  onViewResults: () => void;
}

export function SearchTaskCard({ task, onExecute, onViewResults }: SearchTaskCardProps) {
  return (
    <div
      className="search-task-card"
      style={{
        backgroundColor: colorPalette.background.secondary,
        borderRadius: components.card.borderRadius,
        padding: spacing['space-6'],
        boxShadow: components.card.boxShadow,
        border: `1px solid ${colorPalette.border.default}`,
        transition: 'all 300ms ease',
        cursor: 'pointer'
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.boxShadow = designSystem.designSystem.shadows.medium;
        e.currentTarget.style.transform = 'translateY(-2px)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.boxShadow = components.card.boxShadow;
        e.currentTarget.style.transform = 'translateY(0)';
      }}
    >
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h3
            className="text-h5 font-semibold mb-1"
            style={{ color: colorPalette.text.primary }}
          >
            {task.topic}
          </h3>
          <p
            className="text-body-sm"
            style={{ color: colorPalette.text.secondary }}
          >
            {task.search_id} • {task.employee}
          </p>
        </div>
        <PriorityBadge priority={task.priority} />
      </div>

      {/* Department & Status */}
      <div className="flex items-center gap-2 mb-4">
        <span
          className="department-badge"
          style={{
            padding: `${spacing['space-1']} ${spacing['space-3']}`,
            borderRadius: components.badge.borderRadius,
            backgroundColor: '#6D28D9',
            color: '#ffffff',
            fontSize: typography.caption.fontSize,
            fontWeight: 600
          }}
        >
          {task.department}
        </span>
        <StatusBadge status={task.status} />
      </div>

      {/* Search Query */}
      {task.search_query && (
        <div className="mb-4">
          <p
            className="text-caption mb-1"
            style={{ color: colorPalette.text.tertiary }}
          >
            Search Query:
          </p>
          <p
            className="text-body-sm"
            style={{ color: colorPalette.text.secondary }}
          >
            {task.search_query}
          </p>
        </div>
      )}

      {/* Stats */}
      <div className="flex items-center gap-4 mb-4">
        <div>
          <p className="text-caption" style={{ color: colorPalette.text.tertiary }}>
            Videos Found
          </p>
          <p className="text-h5 font-semibold" style={{ color: '#6D28D9' }}>
            {task.videos_found}
          </p>
        </div>
        <div>
          <p className="text-caption" style={{ color: colorPalette.text.tertiary }}>
            Assigned
          </p>
          <p className="text-body-sm" style={{ color: colorPalette.text.secondary }}>
            {new Date(task.date_assigned).toLocaleDateString()}
          </p>
        </div>
      </div>

      {/* Actions */}
      <div className="flex items-center gap-2">
        {task.status === 'Assigned' && (
          <button
            onClick={() => onExecute(task.id)}
            className="btn-primary flex-1"
            style={{
              backgroundColor: '#6D28D9',
              color: '#ffffff',
              padding: `${spacing['space-2']} ${spacing['space-4']}`,
              borderRadius: components.button.borderRadius,
              fontSize: typography.body.small.fontSize,
              fontWeight: 500
            }}
          >
            Execute Search
          </button>
        )}
        {task.status === 'Completed' && (
          <button
            onClick={onViewResults}
            className="btn-secondary flex-1"
            style={{
              backgroundColor: 'transparent',
              color: '#6D28D9',
              border: '1px solid #6D28D9',
              padding: `${spacing['space-2']} ${spacing['space-4']}`,
              borderRadius: components.button.borderRadius,
              fontSize: typography.body.small.fontSize,
              fontWeight: 500
            }}
          >
            View Results ({task.videos_found})
          </button>
        )}
      </div>
    </div>
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
import designSystem from '@/design-system/design-system.json';

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
  const { register, handleSubmit, formState: { errors }, reset } = useForm<SearchTaskFormData>({
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

  if (!isOpen) return null;

  const { colorPalette, spacing, components, typography } = designSystem.designSystem;

  return (
    <div
      className="modal-backdrop"
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        zIndex: components.modal.zIndex,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: spacing['space-4']
      }}
      onClick={onClose}
    >
      <div
        className="modal-content"
        style={{
          backgroundColor: colorPalette.background.secondary,
          borderRadius: components.modal.borderRadius,
          padding: spacing['space-8'],
          maxWidth: components.modal.maxWidth,
          width: '100%',
          boxShadow: designSystem.designSystem.shadows.heavy
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="mb-6">
          <h2
            className="text-h3 font-semibold mb-2"
            style={{ color: colorPalette.text.primary }}
          >
            Create Search Task
          </h2>
          <p
            className="text-body-sm"
            style={{ color: colorPalette.text.secondary }}
          >
            Assign a new video search task to a team member
          </p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit(onSubmit)}>
          {/* Employee */}
          <div className="form-group mb-4">
            <label
              className="text-body-sm font-medium mb-2 block"
              style={{ color: colorPalette.text.primary }}
            >
              Employee Name *
            </label>
            <input
              {...register('employee')}
              type="text"
              placeholder="Enter employee name"
              className="input"
              style={{
                width: '100%',
                padding: `${spacing['space-3']} ${spacing['space-4']}`,
                borderRadius: components.input.borderRadius,
                border: `1px solid ${errors.employee ? colorPalette.systemColors.light.error.default : colorPalette.border.default}`,
                fontSize: typography.body.default.fontSize
              }}
            />
            {errors.employee && (
              <p className="text-caption mt-1" style={{ color: colorPalette.systemColors.light.error.default }}>
                {errors.employee.message}
              </p>
            )}
          </div>

          {/* Department */}
          <div className="form-group mb-4">
            <label
              className="text-body-sm font-medium mb-2 block"
              style={{ color: colorPalette.text.primary }}
            >
              Department *
            </label>
            <select
              {...register('department')}
              className="input"
              style={{
                width: '100%',
                padding: `${spacing['space-3']} ${spacing['space-4']}`,
                borderRadius: components.input.borderRadius,
                border: `1px solid ${colorPalette.border.default}`,
                fontSize: typography.body.default.fontSize
              }}
            >
              <option value="VID">VID - Video Research</option>
              <option value="AID">AID - AI Development</option>
              <option value="DEV">DEV - Development</option>
              <option value="SMM">SMM - Social Media</option>
              <option value="DGN">DGN - Design</option>
            </select>
          </div>

          {/* Topic */}
          <div className="form-group mb-4">
            <label
              className="text-body-sm font-medium mb-2 block"
              style={{ color: colorPalette.text.primary }}
            >
              Search Topic *
            </label>
            <textarea
              {...register('topic')}
              placeholder="Describe what to search for..."
              rows={3}
              className="input"
              style={{
                width: '100%',
                padding: `${spacing['space-3']} ${spacing['space-4']}`,
                borderRadius: components.input.borderRadius,
                border: `1px solid ${errors.topic ? colorPalette.systemColors.light.error.default : colorPalette.border.default}`,
                fontSize: typography.body.default.fontSize,
                resize: 'vertical'
              }}
            />
            {errors.topic && (
              <p className="text-caption mt-1" style={{ color: colorPalette.systemColors.light.error.default }}>
                {errors.topic.message}
              </p>
            )}
          </div>

          {/* Priority */}
          <div className="form-group mb-6">
            <label
              className="text-body-sm font-medium mb-2 block"
              style={{ color: colorPalette.text.primary }}
            >
              Priority (0-100)
            </label>
            <input
              {...register('priority', { valueAsNumber: true })}
              type="number"
              min="0"
              max="100"
              className="input"
              style={{
                width: '100%',
                padding: `${spacing['space-3']} ${spacing['space-4']}`,
                borderRadius: components.input.borderRadius,
                border: `1px solid ${colorPalette.border.default}`,
                fontSize: typography.body.default.fontSize
              }}
            />
          </div>

          {/* Actions */}
          <div className="flex items-center gap-3 justify-end">
            <button
              type="button"
              onClick={onClose}
              className="btn-secondary"
              style={{
                padding: `${spacing['space-3']} ${spacing['space-6']}`,
                borderRadius: components.button.borderRadius,
                border: `1px solid ${colorPalette.border.default}`,
                fontSize: typography.body.default.fontSize,
                fontWeight: 500,
                color: colorPalette.text.secondary
              }}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
              style={{
                padding: `${spacing['space-3']} ${spacing['space-6']}`,
                borderRadius: components.button.borderRadius,
                backgroundColor: '#6D28D9',
                color: '#ffffff',
                fontSize: typography.body.default.fontSize,
                fontWeight: 500
              }}
            >
              Create Task
            </button>
          </div>
        </form>
      </div>
    </div>
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

## 🗄️ DATABASE SCHEMA (Prisma)

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// Search Queue Table
model SearchTask {
  id             String    @id @default(cuid())
  search_id      String    @unique // SRH-001, SRH-002
  employee       String
  department     String
  topic          String    @db.Text
  search_query   String?   @db.Text
  status         String    // Assigned, In_Progress, Completed
  priority       Int       @default(50) // 0-100
  date_assigned  DateTime  @default(now())
  date_completed DateTime?
  videos_found   Int       @default(0)
  results        Json?     // Array of SearchResult
  notes          String?   @db.Text
  createdAt      DateTime  @default(now())
  updatedAt      DateTime  @updatedAt

  @@index([status])
  @@index([department])
  @@index([priority])
  @@map("search_tasks")
}

// Video Queue Table
model Video {
  id                String    @id @default(cuid())
  vq_id             String    @unique // VQ-001, VQ-002
  youtube_url       String
  video_id          String    // YouTube video ID
  title             String
  channel           String
  thumbnail         String
  duration          String
  views             Int
  likes             Int
  upload_date       DateTime
  topic             String?
  source            String    // Manual, Search_Queue, Dropbox
  employee          String
  department        String
  priority          Int       // 0-100 calculated
  manual_priority   Int?      // 0-20 manual boost
  status            String    // Queued, Selected, In_Progress, Completed
  processing_phase  String?   // Phase_1_Transcribed, etc.
  date_added        DateTime  @default(now())
  date_selected     DateTime?
  date_completed    DateTime?
  notes             String?   @db.Text
  createdAt         DateTime  @default(now())
  updatedAt         DateTime  @updatedAt

  @@index([status])
  @@index([priority])
  @@index([department])
  @@index([processing_phase])
  @@map("videos")
}

// Video Processing Progress (for Phase tracking)
model VideoProgress {
  id                    String    @id @default(cuid())
  video_id              String    @unique
  video                 Video     @relation(fields: [video_id], references: [id], onDelete: Cascade)

  // Phase timestamps
  phase_0_queued        DateTime?
  phase_1_transcribed   DateTime?
  phase_2_extraction    DateTime?
  phase_3_gap_analysis  DateTime?
  phase_4_integration   DateTime?
  phase_5_mapping       DateTime?
  completed             DateTime?

  current_phase         String    // Phase_0_Queued, Phase_1_Transcribed, etc.
  processing_status     String    // Pending, In_Progress, Complete, Failed

  createdAt             DateTime  @default(now())
  updatedAt             DateTime  @updatedAt

  @@map("video_progress")
}

// Extracted Entities (from video transcriptions)
model ExtractedEntity {
  id            String    @id @default(cuid())
  video_id      String
  video         Video     @relation(fields: [video_id], references: [id], onDelete: Cascade)

  entity_type   String    // workflow, action, tool, object, skill
  entity_id     String?   // WRF-001, ACTION-042, TOOL-AI-223
  name          String
  description   String?   @db.Text
  category      String?
  department    String[]

  classification String   // NEW, EXISTING, UPDATE
  confidence    Float?    // 0.0-1.0 AI confidence score

  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  @@index([video_id])
  @@index([entity_type])
  @@index([classification])
  @@map("extracted_entities")
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
│   │   └── index.ts           # Route aggregator
│   ├── controllers/
│   │   ├── searchQueueController.ts
│   │   ├── videoQueueController.ts
│   │   └── youtubeController.ts
│   ├── services/
│   │   ├── openaiService.ts   # OpenAI integration
│   │   ├── youtubeService.ts  # YouTube Data API
│   │   ├── dropboxService.ts  # Dropbox API
│   │   └── priorityService.ts # Priority calculation
│   ├── middleware/
│   │   ├── errorHandler.ts
│   │   ├── validator.ts
│   │   └── cors.ts
│   ├── lib/
│   │   └── prisma.ts          # Prisma client
│   └── types/
│       └── index.ts           # TypeScript types
├── prisma/
│   ├── schema.prisma
│   └── migrations/
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

### Search Queue Controller

```typescript
// src/controllers/searchQueueController.ts
import { Request, Response } from 'express';
import { prisma } from '../lib/prisma';
import { executeOpenAISearch } from '../services/openaiService';

export async function getAllTasks(req: Request, res: Response) {
  try {
    const tasks = await prisma.searchTask.findMany({
      orderBy: [
        { status: 'asc' },
        { priority: 'desc' },
        { createdAt: 'desc' }
      ]
    });
    res.json(tasks);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function createTask(req: Request, res: Response) {
  try {
    const body = req.body;

    // Generate next search_id
    const lastTask = await prisma.searchTask.findFirst({
      orderBy: { search_id: 'desc' }
    });

    const nextId = lastTask
      ? `SRH-${String(parseInt(lastTask.search_id.split('-')[1]) + 1).padStart(3, '0')}`
      : 'SRH-001';

    const task = await prisma.searchTask.create({
      data: {
        search_id: nextId,
        employee: body.employee,
        department: body.department,
        topic: body.topic,
        search_query: body.search_query,
        priority: body.priority || 50,
        status: 'Assigned',
        videos_found: 0,
        date_assigned: new Date()
      }
    });

    return NextResponse.json(task, { status: 201 });
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// app/api/search-queue/execute/route.ts
import { OpenAI } from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function POST(request: NextRequest) {
  try {
    const { taskId, query } = await request.json();

    // Update status to In_Progress
    await prisma.searchTask.update({
      where: { id: taskId },
      data: { status: 'In_Progress' }
    });

    // Execute search with OpenAI
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        {
          role: 'system',
          content: 'You are a research assistant. Find relevant YouTube videos for the given topic. Return results in JSON format with title, url, channel, views, duration, upload_date, relevance_score (0-100).'
        },
        {
          role: 'user',
          content: `Find YouTube videos about: ${query}. Focus on recent videos (last 30 days) with high engagement.`
        }
      ],
      response_format: { type: 'json_object' }
    });

    const results = JSON.parse(response.choices[0].message.content);

    // Update task with results
    await prisma.searchTask.update({
      where: { id: taskId },
      data: {
        status: 'Completed',
        videos_found: results.videos?.length || 0,
        results: results.videos,
        date_completed: new Date()
      }
    });

    return NextResponse.json({ success: true, results: results.videos });
  } catch (error) {
    // Revert status on error
    await prisma.searchTask.update({
      where: { id: taskId },
      data: { status: 'Assigned' }
    });

    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

### Video Queue API

```typescript
// app/api/video-queue/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { google } from 'googleapis';
import { calculatePriority } from '@/lib/priority';

const youtube = google.youtube({
  version: 'v3',
  auth: process.env.YOUTUBE_API_KEY
});

export async function GET() {
  try {
    const videos = await prisma.video.findMany({
      orderBy: [
        { priority: 'desc' },
        { createdAt: 'desc' }
      ]
    });
    return NextResponse.json(videos);
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Extract YouTube video ID
    const videoId = extractYouTubeId(body.youtube_url);

    // Fetch metadata from YouTube
    const response = await youtube.videos.list({
      part: ['snippet', 'statistics', 'contentDetails'],
      id: [videoId]
    });

    if (!response.data.items || response.data.items.length === 0) {
      throw new Error('Video not found');
    }

    const videoData = response.data.items[0];
    const snippet = videoData.snippet!;
    const statistics = videoData.statistics!;
    const contentDetails = videoData.contentDetails!;

    // Calculate priority
    const priority = calculatePriority({
      views: parseInt(statistics.viewCount || '0'),
      likes: parseInt(statistics.likeCount || '0'),
      publishedAt: new Date(snippet.publishedAt!),
      manualPriority: body.manual_priority || 0
    });

    // Generate next vq_id
    const lastVideo = await prisma.video.findFirst({
      orderBy: { vq_id: 'desc' }
    });

    const nextId = lastVideo
      ? `VQ-${String(parseInt(lastVideo.vq_id.split('-')[1]) + 1).padStart(3, '0')}`
      : 'VQ-001';

    // Create video record
    const video = await prisma.video.create({
      data: {
        vq_id: nextId,
        youtube_url: body.youtube_url,
        video_id: videoId,
        title: snippet.title!,
        channel: snippet.channelTitle!,
        thumbnail: snippet.thumbnails?.high?.url || snippet.thumbnails?.default?.url!,
        duration: parseDuration(contentDetails.duration!),
        views: parseInt(statistics.viewCount || '0'),
        likes: parseInt(statistics.likeCount || '0'),
        upload_date: new Date(snippet.publishedAt!),
        topic: body.topic,
        source: body.source || 'Manual',
        employee: body.employee,
        department: body.department,
        priority,
        manual_priority: body.manual_priority,
        status: 'Queued',
        date_added: new Date(),
        notes: body.notes
      }
    });

    return NextResponse.json(video, { status: 201 });
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

// app/api/video-queue/export/route.ts
export async function GET() {
  try {
    const videos = await prisma.video.findMany({
      orderBy: { priority: 'desc' }
    });

    // Generate CSV
    const headers = ['VQ ID', 'Title', 'Channel', 'Priority', 'Status', 'Views', 'Department', 'Date Added', 'URL'];
    const rows = videos.map(v => [
      v.vq_id,
      v.title,
      v.channel,
      v.priority,
      v.status,
      v.views,
      v.department,
      new Date(v.date_added).toLocaleDateString(),
      v.youtube_url
    ]);

    const csv = [headers, ...rows].map(row => row.join(',')).join('\n');

    return new NextResponse(csv, {
      headers: {
        'Content-Type': 'text/csv',
        'Content-Disposition': `attachment; filename="video-queue-${new Date().toISOString().split('T')[0]}.csv"`
      }
    });
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}

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

function parseDuration(isoDuration: string): string {
  // Convert PT15M33S to "15:33"
  const match = isoDuration.match(/PT(\d+H)?(\d+M)?(\d+S)?/);
  if (!match) return '0:00';

  const hours = match[1] ? parseInt(match[1]) : 0;
  const minutes = match[2] ? parseInt(match[2]) : 0;
  const seconds = match[3] ? parseInt(match[3]) : 0;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  }
  return `${minutes}:${String(seconds).padStart(2, '0')}`;
}
```

---

## 🎨 SHARED COMPONENTS

### ThemeContext (Dark Mode Support)

```typescript
// contexts/ThemeContext.tsx
import React, { createContext, useContext, useState, useEffect } from 'react';
import designSystem from '@/design-system/design-system.json';

type Theme = 'light' | 'dark';

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
  colors: typeof designSystem.designSystem.colorPalette;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>('light');

  useEffect(() => {
    // Load from localStorage
    const saved = localStorage.getItem('theme') as Theme;
    if (saved) {
      setTheme(saved);
      document.documentElement.setAttribute('data-theme', saved);
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };

  return (
    <ThemeContext.Provider value={{
      theme,
      toggleTheme,
      colors: designSystem.designSystem.colorPalette
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
import { useTheme } from '@/contexts/ThemeContext';

export function LoadingSpinner({ size = 'md' }: { size?: 'sm' | 'md' | 'lg' }) {
  const { theme, colors } = useTheme();
  const primaryColor = colors.systemColors[theme].primary.default;

  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12'
  };

  return (
    <div
      className={`spinner ${sizeClasses[size]} border-4 border-t-transparent rounded-full animate-spin`}
      style={{ borderColor: primaryColor, borderTopColor: 'transparent' }}
    />
  );
}

// components/EmptyState.tsx
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
    <div className="empty-state text-center py-12">
      {icon && <div className="mb-4">{icon}</div>}
      <h3 className="text-h4 font-semibold mb-2">{title}</h3>
      <p className="text-body-sm text-text-secondary mb-6">{description}</p>
      {action}
    </div>
  );
}
```

---

## ⚙️ ENVIRONMENT VARIABLES

```bash
# .env.example

# Database
DATABASE_URL="postgresql://user:password@host:5432/researches_db"

# YouTube API
YOUTUBE_API_KEY="AIza..."

# OpenAI API
OPENAI_API_KEY="sk-..."

# Google AI (Gemini)
GOOGLE_AI_API_KEY="..."

# Dropbox API
DROPBOX_ACCESS_TOKEN="sl...."

# Application
NEXT_PUBLIC_APP_URL="https://your-app.vercel.app"
NODE_ENV="production"

# Optional: Analytics
NEXT_PUBLIC_ANALYTICS_ID="..."
```

---

## 📦 DEPLOYMENT

### Vercel Deployment

```json
// vercel.json
{
  "buildCommand": "prisma generate && npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "env": {
    "DATABASE_URL": "@database-url",
    "OPENAI_API_KEY": "@openai-api-key",
    "YOUTUBE_API_KEY": "@youtube-api-key",
    "GOOGLE_AI_API_KEY": "@google-ai-api-key",
    "DROPBOX_ACCESS_TOKEN": "@dropbox-access-token"
  }
}
```

### Database Setup (Neon/Supabase)

```bash
# Initialize Prisma
npx prisma init

# Create migration
npx prisma migrate dev --name init

# Generate Prisma Client
npx prisma generate

# Seed database (optional)
npx prisma db seed
```

---

## ✅ IMPLEMENTATION CHECKLIST

### Design System Integration
- [ ] design-system.json copied to `src/design-system/`
- [ ] Tailwind config imports from JSON
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
- [ ] Dark mode fully supported with ThemeContext

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
- [ ] Database schema (SearchTask model)

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
- [ ] Database schema (Video model)

### Shared Architecture
- [ ] AppLayout component
- [ ] Header component
- [ ] Sidebar component (256px/80px)
- [ ] ThemeContext (light/dark mode)
- [ ] ErrorBoundary component
- [ ] LoadingSpinner component
- [ ] EmptyState component
- [ ] PriorityBadge component (shared)
- [ ] StatusBadge component (shared)

### Database & API
- [ ] Prisma schema complete
- [ ] Database migrations run
- [ ] All API routes implemented
- [ ] Error handling in all routes
- [ ] Input validation with Zod
- [ ] TypeScript types for all models

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
# Create Next.js app
npx create-next-app@latest research-management --typescript --tailwind --app

cd research-management

# Install dependencies
npm install zustand @tanstack/react-query @tanstack/react-table
npm install react-hook-form zod @hookform/resolvers/zod
npm install recharts
npm install prisma @prisma/client
npm install openai googleapis dropbox

# Install dev dependencies
npm install -D @types/node typescript
```

### 2. Copy Design System

```bash
# Create directory
mkdir -p src/design-system

# Copy design-system.json to src/design-system/
```

### 3. Setup Database

```bash
# Initialize Prisma
npx prisma init

# Update DATABASE_URL in .env
# Copy schema from this prompt to prisma/schema.prisma

# Create migration
npx prisma migrate dev --name init

# Generate Prisma Client
npx prisma generate
```

### 4. Create File Structure

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
│   ├── search-queue/
│   │   ├── SearchQueueDashboard.tsx
│   │   ├── SearchTaskCard.tsx
│   │   ├── CreateSearchTaskModal.tsx
│   │   └── SearchResultsModal.tsx
│   ├── video-queue/
│   │   ├── VideoQueueDashboard.tsx
│   │   ├── VideoCard.tsx
│   │   └── AddVideoModal.tsx
│   └── shared/
│       ├── PriorityBadge.tsx
│       ├── StatusBadge.tsx
│       ├── LoadingSpinner.tsx
│       └── EmptyState.tsx
├── stores/
│   ├── searchQueueStore.ts
│   └── videoQueueStore.ts
├── contexts/
│   └── ThemeContext.tsx
├── lib/
│   ├── prisma.ts
│   ├── priority.ts
│   └── types.ts
├── design-system/
│   └── design-system.json
└── styles/
    └── globals.css
```

### 5. Start Development

#### Backend (Terminal 1)

```bash
cd backend
npm install
npx prisma generate
npx prisma migrate dev --name init
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
- **Prisma ORM:** https://www.prisma.io/docs
- **Express.js:** https://expressjs.com/
- **React:** https://react.dev/
- **Vite:** https://vitejs.dev/

---

## 🎯 SUCCESS CRITERIA

### Backend (Express.js)

✅ Separate Express.js application on port 5000
✅ All REST API endpoints functional (/api/search-queue, /api/video-queue)
✅ CORS properly configured for frontend origin
✅ Database schema complete with Prisma
✅ OpenAI integration for search execution
✅ YouTube Data API integration for video metadata
✅ Priority calculation algorithm implemented
✅ Error handling middleware
✅ Input validation with Zod
✅ TypeScript strict mode (no 'any' types)
✅ Deployment ready for Railway/Render/Heroku

### Frontend (React)

✅ Separate React application on port 3000
✅ 100% integration with design-system.json (no hardcoded values)
✅ Search Queue dashboard fully functional
✅ Video Queue dashboard fully functional
✅ Axios HTTP client configured for backend API
✅ Zustand stores for state management
✅ TanStack Query for data fetching
✅ Dark mode working throughout with ThemeContext
✅ All error/loading/empty states implemented
✅ Responsive on mobile/tablet/desktop
✅ TypeScript strict mode (no 'any' types)
✅ Deployment ready for Vercel/Netlify

### Integration

✅ Backend and Frontend communicate via REST API
✅ CORS configured correctly
✅ Environment variables properly configured
✅ Can run both apps locally in development
✅ Can deploy separately to production
✅ Database accessible from backend only
✅ API keys secure (backend only)

---

## 📦 DELIVERABLES

### 2 Separate Applications

1. **Backend (Express.js)**
   - Location: `backend/`
   - Package: Node.js + Express.js + Prisma
   - Port: 5000
   - Deploy: Railway/Render/Heroku

2. **Frontend (React)**
   - Location: `frontend/`
   - Package: React 19 + Vite + TypeScript
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
**Version:** 2.0 - Separated Backend & Frontend
**Architecture:** Express.js (Backend) + React (Frontend)
**Total Lines:** ~2,800
**Status:** ✅ Ready for Implementation
