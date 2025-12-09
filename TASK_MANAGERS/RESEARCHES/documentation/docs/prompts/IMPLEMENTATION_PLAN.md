# IMPLEMENTATION PLAN: Optimized Search + Video Queue App Prompt

**Date:** 2025-12-08
**Status:** 🔄 Ready for Approval
**Version:** 1.0

---

## 📋 OBJECTIVE

Create an optimized, production-ready prompt for generating a complete application with Search Queue and Video Queue functionality, properly integrated with design-system.json as single source of truth.

---

## 🎯 APPROACH

### Option 1: Create New Consolidated Prompt (RECOMMENDED)
**File:** `SEARCH-VIDEO-QUEUE-APP-GENERATION-PROMPT.md`

**Advantages:**
- ✅ Clean slate, no legacy code
- ✅ Properly structured from the start
- ✅ Easy to maintain
- ✅ Keeps existing prompts as reference

**Structure:**
```markdown
1. Design System Integration (reference JSON)
2. Tech Stack & Dependencies
3. Core Application Architecture
4. Shared Components (Header, Sidebar, Layout)
5. Search Queue Module (full specs)
6. Video Queue Module (full specs)
7. State Management (Zustand stores)
8. API Integration (OpenAI, YouTube, Dropbox)
9. Dark Mode Implementation
10. Error Handling & Loading States
11. Testing Strategy
12. Deployment Guide
```

### Option 2: Update Existing FULL-APP-GENERATION-PROMPT.md
**Advantages:**
- ✅ Maintains existing work
- ✅ Incremental improvement

**Disadvantages:**
- ⚠️ Need to remove 1,300+ lines of CSS variables
- ⚠️ Risk of conflicts with existing content
- ⚠️ More complex refactoring

---

## 📝 DETAILED IMPLEMENTATION PLAN

### Phase 1: Design System Integration (CRITICAL)

#### Task 1.1: Create Design System Header Section
**Location:** Top of new prompt file
**Content:**
```markdown
## 🎨 DESIGN SYSTEM - SINGLE SOURCE OF TRUTH

**CRITICAL REQUIREMENT:** All styling MUST come from `design-system.json`

### Setup Instructions
1. Copy `design-system.json` to project root: `src/design-system/`
2. Import in every component:
   ```typescript
   import designSystem from '@/design-system/design-system.json';
   const { colorPalette, typography, spacing, components } = designSystem.designSystem;
   ```

### Integration Reference
- **Complete Guide:** See `DESIGN-SYSTEM-INTEGRATION-GUIDE.md`
- **Quick Reference:** See `_DESIGN-SYSTEM-SNIPPET.md`
- **Analysis:** See `design-system-analysis.md`

### DO's and DON'Ts
✅ DO: `const color = colorPalette.systemColors.light.primary.default;`
❌ DON'T: `const color = '#2563EB';`

### Critical Design Details
- Sidebar: #1F2937 (dark even in light theme)
- Scrollbar: 6px width (not 8px!)
- Button radius: 8px
- Card/Input radius: 12px
- Voice Wave: 15 bars with staggered delays
```

#### Task 1.2: Add Tailwind Config Generation
**Content:** Complete tailwind.config.ts that reads from JSON
```typescript
import designSystem from './src/design-system/design-system.json';
const { colorPalette, typography, spacing, borderRadius, shadows } = designSystem.designSystem;

export default {
  theme: {
    extend: {
      colors: {
        primary: colorPalette.systemColors.light.primary,
        // ... all colors from JSON
      },
      fontFamily: {
        sans: typography.fontFamilies.primary,
      },
      // ... complete config
    }
  }
}
```

---

### Phase 2: Search Queue Module Specification

#### Task 2.1: Module Overview
```markdown
## 📊 SEARCH QUEUE MODULE

**Module Color:** #6D28D9 (Designers Purple)
**Department:** Designers
**Purpose:** Manage search research tasks with AI-powered results

### Key Features
1. Create search tasks with keywords, context, priority
2. AI-powered search using OpenAI API
3. Results organization and filtering
4. Status tracking (pending, in-progress, completed)
5. Priority management (5-tier system with stars)
```

#### Task 2.2: Component Specifications
- SearchQueueDashboard (main layout)
- SearchTaskCard (individual task)
- CreateSearchTaskModal (task creation)
- SearchResultsModal (view results)
- SearchFilters (filter by status/priority)
- SearchStats (statistics cards)

**Each component includes:**
- Complete TypeScript interface
- Props specification
- State management with Zustand
- Dark mode support from JSON
- Error/loading/empty states
- Accessibility (ARIA labels)

#### Task 2.3: API Integration
```typescript
// OpenAI API for search
POST /api/search/execute
{
  taskId: string;
  keywords: string[];
  context: string;
}

// Store results in database
POST /api/search/results
{
  taskId: string;
  results: SearchResult[];
}
```

---

### Phase 3: Video Queue Module Specification

#### Task 3.1: Module Overview
```markdown
## 🎬 VIDEO QUEUE MODULE

**Module Color:** #147857 (Developers Green)
**Department:** Developers
**Purpose:** Manage video processing queue with priority system

### Key Features
1. Add videos from YouTube URLs
2. Priority calculation algorithm
3. Processing status tracking
4. Video metadata extraction (YouTube Data API)
5. Thumbnail generation
6. Storage integration (Dropbox API)
```

#### Task 3.2: Priority Calculation Algorithm
```typescript
/**
 * Calculate video priority (0-100)
 * Based on: views, engagement rate, recency, manual boost
 */
function calculatePriority(video: Video): number {
  const viewScore = Math.min((video.views / 1000000) * 20, 30); // Max 30 points
  const engagementScore = (video.likes / video.views) * 100 * 0.3; // Max 30 points
  const recencyScore = calculateRecencyScore(video.publishedAt); // Max 20 points
  const manualBoost = video.manualPriority || 0; // Max 20 points

  return Math.min(Math.round(viewScore + engagementScore + recencyScore + manualBoost), 100);
}

/**
 * Priority tiers with visual representation
 */
const priorityTiers = {
  critical: { range: [80, 100], stars: 5, color: '#DC2626' },
  high: { range: [60, 79], stars: 4, color: '#EA580C' },
  medium: { range: [40, 59], stars: 3, color: '#F59E0B' },
  low: { range: [20, 39], stars: 2, color: '#84CC16' },
  veryLow: { range: [0, 19], stars: 1, color: '#22C55E' }
};
```

#### Task 3.3: Component Specifications
- VideoQueueDashboard (main layout)
- VideoCard (individual video with thumbnail)
- AddVideoModal (add from URL)
- VideoQueueStats (statistics)
- PriorityBadge (5-star system)
- VideoFilters (filter by priority/status/department)

---

### Phase 4: Shared Architecture

#### Task 4.1: Application Shell
```markdown
### Layout Components
1. **AppLayout** - Main layout wrapper
2. **Header** - Top navigation (256px height)
3. **Sidebar** - Navigation (256px expanded, 80px collapsed)
4. **MainContent** - Content area with responsive padding
```

#### Task 4.2: Theme Management
```typescript
// ThemeContext.tsx
import { createContext, useContext, useState, useEffect } from 'react';
import designSystem from '@/design-system/design-system.json';

type Theme = 'light' | 'dark';

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
  colors: typeof designSystem.designSystem.colorPalette;
}

export const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>('light');

  useEffect(() => {
    // Load from localStorage
    const saved = localStorage.getItem('theme') as Theme;
    if (saved) setTheme(saved);
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

#### Task 4.3: Error Handling
```typescript
// ErrorBoundary.tsx
import { Component, ErrorInfo, ReactNode } from 'react';

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
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="error-container">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
        </div>
      );
    }

    return this.props.children;
  }
}
```

#### Task 4.4: Loading States
```typescript
// LoadingSpinner.tsx
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
    <div className={`spinner ${sizeClasses[size]}`} style={{ borderColor: primaryColor }}>
      {/* Animated spinner */}
    </div>
  );
}

// EmptyState.tsx
export function EmptyState({
  icon,
  title,
  description,
  action
}: {
  icon: ReactNode;
  title: string;
  description: string;
  action?: ReactNode;
}) {
  return (
    <div className="empty-state">
      {icon}
      <h3>{title}</h3>
      <p>{description}</p>
      {action}
    </div>
  );
}
```

---

### Phase 5: State Management

#### Task 5.1: Search Queue Store
```typescript
// stores/searchQueueStore.ts
import { create } from 'zustand';

interface SearchTask {
  id: string;
  keywords: string[];
  context: string;
  priority: number;
  status: 'pending' | 'in-progress' | 'completed' | 'failed';
  results: SearchResult[];
  createdAt: Date;
  completedAt?: Date;
}

interface SearchQueueStore {
  tasks: SearchTask[];
  loading: boolean;
  error: string | null;

  // Actions
  createTask: (task: Omit<SearchTask, 'id' | 'createdAt'>) => Promise<void>;
  executeTask: (taskId: string) => Promise<void>;
  deleteTask: (taskId: string) => Promise<void>;
  updateTask: (taskId: string, updates: Partial<SearchTask>) => Promise<void>;
  fetchTasks: () => Promise<void>;
}

export const useSearchQueueStore = create<SearchQueueStore>((set, get) => ({
  tasks: [],
  loading: false,
  error: null,

  createTask: async (task) => {
    set({ loading: true, error: null });
    try {
      const response = await fetch('/api/search/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(task)
      });
      const newTask = await response.json();
      set(state => ({ tasks: [...state.tasks, newTask], loading: false }));
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },

  // ... other actions
}));
```

#### Task 5.2: Video Queue Store
```typescript
// stores/videoQueueStore.ts
import { create } from 'zustand';

interface Video {
  id: string;
  url: string;
  title: string;
  thumbnail: string;
  duration: number;
  views: number;
  likes: number;
  publishedAt: Date;
  priority: number;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  department: 'designers' | 'developers' | 'managers' | 'marketers' | 'videographers';
  createdAt: Date;
  processedAt?: Date;
}

interface VideoQueueStore {
  videos: Video[];
  loading: boolean;
  error: string | null;

  // Actions
  addVideo: (url: string, department: Video['department']) => Promise<void>;
  removeVideo: (videoId: string) => Promise<void>;
  updatePriority: (videoId: string, priority: number) => Promise<void>;
  processVideo: (videoId: string) => Promise<void>;
  fetchVideos: () => Promise<void>;
}

export const useVideoQueueStore = create<VideoQueueStore>((set, get) => ({
  videos: [],
  loading: false,
  error: null,

  addVideo: async (url, department) => {
    set({ loading: true, error: null });
    try {
      // Fetch YouTube metadata
      const metadata = await fetchYouTubeMetadata(url);

      // Calculate priority
      const priority = calculatePriority(metadata);

      // Save to database
      const response = await fetch('/api/videos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...metadata, priority, department, status: 'pending' })
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

  // ... other actions
}));
```

---

### Phase 6: API Routes

#### Task 6.1: Search API Routes
```typescript
// app/api/search/tasks/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';

export async function GET() {
  const tasks = await prisma.searchTask.findMany({
    orderBy: { createdAt: 'desc' }
  });
  return NextResponse.json(tasks);
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  const task = await prisma.searchTask.create({
    data: {
      keywords: body.keywords,
      context: body.context,
      priority: body.priority,
      status: 'pending'
    }
  });
  return NextResponse.json(task);
}

// app/api/search/execute/route.ts
import { OpenAI } from 'openai';

export async function POST(request: NextRequest) {
  const { taskId, keywords, context } = await request.json();

  const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

  try {
    // Update status
    await prisma.searchTask.update({
      where: { id: taskId },
      data: { status: 'in-progress' }
    });

    // Execute search with OpenAI
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a research assistant.' },
        { role: 'user', content: `Search for: ${keywords.join(', ')}. Context: ${context}` }
      ]
    });

    const results = parseSearchResults(response.choices[0].message.content);

    // Save results
    await prisma.searchTask.update({
      where: { id: taskId },
      data: {
        status: 'completed',
        results: JSON.stringify(results),
        completedAt: new Date()
      }
    });

    return NextResponse.json({ success: true, results });
  } catch (error) {
    await prisma.searchTask.update({
      where: { id: taskId },
      data: { status: 'failed' }
    });
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
```

#### Task 6.2: Video API Routes
```typescript
// app/api/videos/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { google } from 'googleapis';

const youtube = google.youtube({
  version: 'v3',
  auth: process.env.YOUTUBE_API_KEY
});

export async function POST(request: NextRequest) {
  const { url, department } = await request.json();

  // Extract video ID from URL
  const videoId = extractVideoId(url);

  // Fetch metadata from YouTube
  const response = await youtube.videos.list({
    part: ['snippet', 'statistics', 'contentDetails'],
    id: [videoId]
  });

  const videoData = response.data.items[0];

  // Calculate priority
  const priority = calculatePriority({
    views: parseInt(videoData.statistics.viewCount),
    likes: parseInt(videoData.statistics.likeCount),
    publishedAt: new Date(videoData.snippet.publishedAt)
  });

  // Save to database
  const video = await prisma.video.create({
    data: {
      url,
      title: videoData.snippet.title,
      thumbnail: videoData.snippet.thumbnails.high.url,
      duration: parseDuration(videoData.contentDetails.duration),
      views: parseInt(videoData.statistics.viewCount),
      likes: parseInt(videoData.statistics.likeCount),
      publishedAt: new Date(videoData.snippet.publishedAt),
      priority,
      department,
      status: 'pending'
    }
  });

  return NextResponse.json(video);
}
```

---

### Phase 7: Database Schema

#### Task 7.1: Prisma Schema
```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model SearchTask {
  id          String   @id @default(cuid())
  keywords    String[]
  context     String
  priority    Int
  status      String   // pending, in-progress, completed, failed
  results     Json?
  createdAt   DateTime @default(now())
  completedAt DateTime?

  @@map("search_tasks")
}

model Video {
  id          String   @id @default(cuid())
  url         String   @unique
  title       String
  thumbnail   String
  duration    Int
  views       Int
  likes       Int
  publishedAt DateTime
  priority    Int
  status      String   // pending, processing, completed, failed
  department  String   // designers, developers, managers, marketers, videographers
  createdAt   DateTime @default(now())
  processedAt DateTime?

  @@map("videos")
  @@index([priority])
  @@index([status])
  @@index([department])
}
```

---

### Phase 8: Testing Strategy

#### Task 8.1: Component Tests
```typescript
// __tests__/SearchTaskCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { SearchTaskCard } from '@/components/search/SearchTaskCard';

describe('SearchTaskCard', () => {
  it('renders task information correctly', () => {
    const task = {
      id: '1',
      keywords: ['React', 'TypeScript'],
      context: 'Best practices',
      priority: 85,
      status: 'pending'
    };

    render(<SearchTaskCard task={task} />);

    expect(screen.getByText('React')).toBeInTheDocument();
    expect(screen.getByText('TypeScript')).toBeInTheDocument();
    expect(screen.getByText('Best practices')).toBeInTheDocument();
  });

  it('displays correct priority stars', () => {
    const task = { priority: 85 }; // Should show 5 stars
    render(<SearchTaskCard task={task} />);
    expect(screen.getAllByText('⭐')).toHaveLength(5);
  });
});
```

---

### Phase 9: Deployment

#### Task 9.1: Environment Variables
```bash
# .env.example
DATABASE_URL="postgresql://user:password@host:5432/db"
OPENAI_API_KEY="sk-..."
YOUTUBE_API_KEY="AIza..."
DROPBOX_ACCESS_TOKEN="sl...."
NEXT_PUBLIC_APP_URL="https://your-app.vercel.app"
```

#### Task 9.2: Vercel Configuration
```json
// vercel.json
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "env": {
    "DATABASE_URL": "@database-url",
    "OPENAI_API_KEY": "@openai-api-key",
    "YOUTUBE_API_KEY": "@youtube-api-key"
  }
}
```

---

## 📊 IMPLEMENTATION CHECKLIST

### Critical Items (Must Have)
- [ ] Design system JSON properly integrated
- [ ] ThemeContext with light/dark mode
- [ ] ErrorBoundary for error handling
- [ ] Loading states for all async operations
- [ ] Empty states for all lists
- [ ] Search Queue complete functionality
- [ ] Video Queue complete functionality
- [ ] Priority calculation algorithm
- [ ] API routes for search and video
- [ ] Database schema with Prisma
- [ ] Proper TypeScript types throughout

### Design System Verification
- [ ] All colors from JSON (no hardcoded values)
- [ ] All typography from JSON
- [ ] All spacing from JSON
- [ ] Sidebar #1F2937 (dark in light theme)
- [ ] Scrollbar 6px width
- [ ] Button radius 8px
- [ ] Card/Input radius 12px
- [ ] Voice Wave 15 bars
- [ ] Priority 5-tier system with stars
- [ ] Department colors correct (#6D28D9, #147857)

### Functionality Verification
- [ ] Create search tasks
- [ ] Execute search with OpenAI
- [ ] Display search results
- [ ] Add videos from YouTube URL
- [ ] Calculate video priority
- [ ] Display priority badges
- [ ] Filter by status/priority/department
- [ ] Sort by priority/date
- [ ] Dark mode toggle works
- [ ] Responsive on mobile/tablet/desktop

### Code Quality
- [ ] TypeScript strict mode enabled
- [ ] No any types
- [ ] All components have proper types
- [ ] Error handling in all API routes
- [ ] Loading states everywhere
- [ ] Accessibility (ARIA labels)
- [ ] SEO meta tags
- [ ] Performance optimized

---

## 🎯 DELIVERABLE

**New File:** `SEARCH-VIDEO-QUEUE-APP-GENERATION-PROMPT.md`

**Size:** ~3,000-4,000 lines

**Structure:**
1. Design System Integration (300 lines)
2. Tech Stack & Setup (200 lines)
3. Application Architecture (300 lines)
4. Search Queue Module (800 lines)
5. Video Queue Module (800 lines)
6. Shared Components (600 lines)
7. State Management (400 lines)
8. API Integration (500 lines)
9. Testing & Deployment (300 lines)

**Quality Standards:**
- ✅ 100% references to design-system.json
- ✅ Complete TypeScript types
- ✅ Dark mode support
- ✅ Error/loading/empty states
- ✅ Priority calculation algorithm
- ✅ Real API integration code
- ✅ Database schema
- ✅ Testing examples
- ✅ Deployment guide

---

## ⏱️ ESTIMATED TIME

- **Phase 1-3:** 2 hours (core modules)
- **Phase 4-6:** 1.5 hours (architecture & API)
- **Phase 7-9:** 1 hour (database & deployment)
- **Testing & Polish:** 0.5 hours

**Total:** ~5 hours of focused work

---

## ✅ SUCCESS CRITERIA

1. Single prompt file that generates complete working app
2. 100% integration with design-system.json
3. Both Search Queue and Video Queue fully specified
4. No hardcoded design values
5. Complete dark mode support
6. All error/loading/empty states included
7. Priority calculation algorithm documented
8. Real API integration code
9. Database schema ready
10. Deployment instructions clear

---

**Ready for approval to proceed with implementation.**
