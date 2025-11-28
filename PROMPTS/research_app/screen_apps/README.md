# Screen Apps - Incremental Building Strategy

**Build individual screens with Lovable, then merge into complete apps**

---

## Overview

Instead of building two massive applications at once, this folder contains **10 individual screen prompts**. Each screen can be built independently with Lovable AI, tested, and then merged together to create the complete Research Management System.

---

## Strategy

### 1. Build Screens Individually (10-20 min each)
- Copy a single screen prompt into Lovable
- Build that screen completely
- Test functionality
- Save the generated code

### 2. Merge Screens Into Apps
- Combine related screens into full applications
- Add routing/navigation between screens
- Integrate shared state management
- Deploy complete apps

---

## Screen Apps List

### Queue Management Screens (4 screens)

| # | Screen | Build Time | Complexity |
|---|--------|------------|------------|
| 01 | **Video Queue Table** | 15-20 min | ⭐⭐ Medium |
| 02 | **Search Queue Table** | 10-15 min | ⭐ Easy |
| 03 | **Filter Panel** | 15-20 min | ⭐⭐ Medium |
| 04 | **Dashboard Stats** | 10 min | ⭐ Easy |

**Merge Result:** Queue Management Web App

---

### Video Processing Screens (6 screens)

| # | Screen | Build Time | Complexity |
|---|--------|------------|------------|
| 05 | **Upload Transcription** | 15 min | ⭐⭐ Medium |
| 06 | **Entity Extraction Viewer** | 20-25 min | ⭐⭐⭐ Complex |
| 07 | **Gap Analysis Screen** | 20-25 min | ⭐⭐⭐ Complex |
| 08 | **Progress Tracker Widget** | 15 min | ⭐⭐ Medium |
| 09 | **Cost Tracker Widget** | 10 min | ⭐ Easy |
| 10 | **Knowledge Map Viewer** | 25-30 min | ⭐⭐⭐⭐ Very Complex |

**Merge Result:** Video Processing Web App

---

## Build Order

### Recommended Sequence

**Phase 1: Easy Wins (Get familiar with design system)**
1. ✅ Dashboard Stats (04) - Simplest, good starting point
2. ✅ Cost Tracker Widget (09) - Simple counter/display
3. ✅ Search Queue Table (02) - Basic CRUD table

**Phase 2: Core Functionality**
4. ✅ Video Queue Table (01) - Primary data display
5. ✅ Filter Panel (03) - Reusable component
6. ✅ Upload Transcription (05) - File upload UI

**Phase 3: Advanced Features**
7. ✅ Progress Tracker Widget (08) - Visual workflow
8. ✅ Entity Extraction Viewer (06) - Complex tables
9. ✅ Gap Analysis Screen (07) - Side-by-side comparison

**Phase 4: Complex Visualization**
10. ✅ Knowledge Map Viewer (10) - Graph with React Flow

---

## Each Screen Prompt Contains

1. **Complete Feature Spec** - Full functionality for that screen
2. **Tech Stack** - React + TypeScript + Supabase + shadcn/ui
3. **Database Queries** - Specific Supabase integration
4. **UI Design** - AdminRHS-AI-Catalog color system
5. **Validation & Error Handling** - Production-ready logic
6. **Lovable Initiation Phrase** - Copy/paste to start building

---

## Merging Strategy

### After Building All Screens

**Step 1: Group by App**
- Screens 01-04 → Queue Management App
- Screens 05-10 → Video Processing App

**Step 2: Add Navigation**
```typescript
// In merged app
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import VideoQueueScreen from './screens/VideoQueueScreen';
import SearchQueueScreen from './screens/SearchQueueScreen';
import FilterPanel from './components/FilterPanel';
import DashboardStats from './screens/DashboardStats';

function App() {
  return (
    <BrowserRouter>
      <div className="flex">
        <FilterPanel /> {/* Sidebar on all screens */}
        <Routes>
          <Route path="/" element={<DashboardStats />} />
          <Route path="/videos" element={<VideoQueueScreen />} />
          <Route path="/searches" element={<SearchQueueScreen />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
```

**Step 3: Shared State**
```typescript
// Context for shared data
import { createContext } from 'react';

export const AppContext = createContext({
  filters: {},
  setFilters: () => {},
  selectedDepartment: 'ALL',
  setSelectedDepartment: () => {},
});
```

**Step 4: Testing**
- Test each screen individually
- Test navigation between screens
- Test shared state (filters applying across screens)
- Test Supabase real-time updates

---

## Example: Building Screen 01 (Video Queue Table)

### 1. Copy Lovable Initiation Phrase
```
Build a Video Queue Table screen with full CRUD operations.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Table

Features:
- Display videos with status badges
- Filter by status (Pending, Selected, Transcribing, etc.)
- Add/edit/delete videos
- Real-time updates from Supabase
- AdminRHS-AI-Catalog design (blue theme, friendly UI)

Database: Supabase `video_queue` table

Follow complete spec below ⬇️
```

### 2. Paste Complete Prompt
Copy entire contents of `01_video_queue_screen/prompt.md`

### 3. Build with Lovable
Lovable generates complete screen in ~15 minutes

### 4. Test & Save
- Test CRUD operations
- Verify Supabase connection
- Save generated code to your project

---

## Folder Structure

```
screen_apps/
├── README.md (this file)
├── 01_video_queue_screen/
│   └── prompt.md (200-300 lines)
├── 02_search_queue_screen/
│   └── prompt.md (150-250 lines)
├── 03_filter_panel/
│   └── prompt.md (200-250 lines)
├── 04_dashboard_stats/
│   └── prompt.md (150-200 lines)
├── 05_upload_transcription_screen/
│   └── prompt.md (200-250 lines)
├── 06_entity_extraction_viewer/
│   └── prompt.md (250-300 lines)
├── 07_gap_analysis_screen/
│   └── prompt.md (250-300 lines)
├── 08_progress_tracker_widget/
│   └── prompt.md (200-250 lines)
├── 09_cost_tracker_widget/
│   └── prompt.md (150-200 lines)
└── 10_knowledge_map_viewer/
    └── prompt.md (300-350 lines)
```

---

## Benefits of This Approach

✅ **Manageable Scope** - Build one screen in 10-20 minutes instead of full app in hours

✅ **Early Testing** - Validate design system and database integration incrementally

✅ **Easy Debugging** - Issues isolated to single screen, easier to fix

✅ **Flexible Timeline** - Build screens as needed, not all at once

✅ **Reusable Components** - Filter Panel, widgets can be shared across apps

✅ **Lower Risk** - If one screen fails, others are unaffected

---

## Time Estimates

| Task | Time |
|------|------|
| Build all 10 screens individually | 3-4 hours |
| Merge into Queue Management App | 30-45 min |
| Merge into Video Processing App | 45-60 min |
| **Total** | **5-6 hours** |

vs.

| Task | Time |
|------|------|
| Build full Queue Management App at once | 4-6 hours (with debugging) |
| Build full Video Processing App at once | 6-8 hours (with debugging) |
| **Total** | **10-14 hours** |

**Time Savings: ~50%** by building incrementally

---

## Support Files

All screen prompts reference:
- `DESIGN_ASSETS_REFERENCE.md` - Design system specs (inline in each prompt)
- `01_Supabase_Database_Schema_Prompt.md` - Database tables (inline in each prompt)
- `00_PROCESSING_AUTOMATION_LOGIC.md` - Business logic (inline in relevant prompts)

**No external file access needed** - Each prompt is self-contained

---

## Next Steps

1. **Start with easiest screen** - `04_dashboard_stats/prompt.md`
2. **Build and test** - Use Lovable AI builder
3. **Move to next screen** - Follow recommended build order
4. **Merge when ready** - Combine into full apps
5. **Deploy** - Ship complete Research Management System

---

**Created:** 2025-11-28
**Strategy:** Incremental building with Lovable AI
**Goal:** Faster, safer app development with easier debugging
