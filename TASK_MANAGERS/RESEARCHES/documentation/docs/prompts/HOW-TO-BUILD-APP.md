# HOW TO BUILD RESEARCHES 2 APPLICATION - STEP BY STEP

**Created:** 2025-12-08
**Purpose:** Complete guide to building the application using AI prompts
**Target:** Solo developer with Claude Code / Cursor / v0.dev

---

## 📋 OVERVIEW

This guide walks you through building the complete RESEARCHES 2 application using the AI-generation prompts in this directory. Follow these steps sequentially for best results.

---

## 🎯 PREREQUISITES

### Tools Required
- ✅ **AI Assistant**: Claude Code, Cursor, or v0.dev
- ✅ **Node.js**: v20+ installed
- ✅ **Git**: For version control
- ✅ **Code Editor**: VS Code recommended
- ✅ **Terminal**: Command line access

### Accounts Needed
- ✅ **GitHub**: For repository hosting
- ✅ **Vercel**: For frontend deployment (free tier)
- ✅ **Neon**: For PostgreSQL database (free tier)
- ✅ **Railway** (optional): For backend deployment
- ✅ **Dropbox API**: For file storage
- ✅ **OpenAI API**: For transcriptions/analysis

### Knowledge Level
- **Required**: Basic React/TypeScript knowledge
- **Helpful**: Next.js, Tailwind CSS, Prisma basics
- **Optional**: PostgreSQL, API design

---

## 🚀 BUILD PROCESS (3 APPROACHES)

You can build the application using one of three approaches:

### Approach 1: 🎨 Component-by-Component (Recommended for Learning)
**Time:** 3-4 weeks | **Control:** High | **Learning:** High

Build each module separately, test thoroughly, then integrate.

### Approach 2: ⚡ Full-App Generation (Recommended for Speed)
**Time:** 1-2 weeks | **Control:** Medium | **Learning:** Medium

Generate the entire app structure at once, then customize.

### Approach 3: 🔧 Hybrid (Recommended for Balance)
**Time:** 2-3 weeks | **Control:** High | **Learning:** High

Generate structure first, then build modules one by one.

---

## 📖 APPROACH 1: COMPONENT-BY-COMPONENT BUILD

### PHASE 0: SETUP (Day 1-2)

#### Step 1: Create Project Structure

```bash
# Create Next.js project with TypeScript
npx create-next-app@latest researches-2 --typescript --tailwind --app --src-dir

cd researches-2

# Install dependencies
npm install @tanstack/react-query zustand prisma @prisma/client
npm install @shadcn/ui lucide-react framer-motion recharts
npm install axios date-fns
npm install -D @types/node typescript eslint prettier
```

#### Step 2: Copy Design System

```bash
# Create design system directory
mkdir -p src/design-system

# Copy JSON file
cp [PATH_TO]/design-system.json src/design-system/

# Create types
touch src/design-system/types.ts
```

**In `src/design-system/types.ts`:**
```typescript
import designSystemData from './design-system.json';

export type DesignSystem = typeof designSystemData.designSystem;
export const designSystem = designSystemData.designSystem;
```

#### Step 3: Setup Tailwind with Design System

**Edit `tailwind.config.ts`:**
```typescript
import type { Config } from 'tailwindcss';
import { designSystem } from './src/design-system/types';

const { colorPalette, typography, spacing, borderRadius, shadows } = designSystem;

const config: Config = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: colorPalette.systemColors.light.primary.default,
          hover: colorPalette.systemColors.light.primary.hover,
          active: colorPalette.systemColors.light.primary.active,
        },
        // ... add more colors from design system
      },
      fontFamily: {
        sans: [typography.fontFamilies.primary],
      },
      fontSize: {
        xs: typography.fontSizes.xs.px,
        sm: typography.fontSizes.sm.px,
        base: typography.fontSizes.base.px,
        // ... add more sizes
      },
      spacing: spacing.values,
      borderRadius: borderRadius,
      boxShadow: {
        xs: shadows.xs.value,
        sm: shadows.sm.value,
        md: shadows.md.value,
        // ... add more shadows
      },
    },
  },
  plugins: [],
};

export default config;
```

#### Step 4: Setup Database (Neon PostgreSQL)

1. **Go to**: https://neon.tech
2. **Create account** (free tier)
3. **Create new project**: "researches-2"
4. **Copy connection string**

**Create `.env.local`:**
```env
# Database
DATABASE_URL="postgresql://username:password@host/database?sslmode=require"

# APIs (get later)
OPENAI_API_KEY="your-key-here"
DROPBOX_ACCESS_TOKEN="your-token-here"
YOUTUBE_API_KEY="your-key-here"
```

**Initialize Prisma:**
```bash
npx prisma init
```

#### Step 5: Setup Git & GitHub

```bash
git init
git add .
git commit -m "Initial setup with design system"

# Create repo on GitHub, then:
git remote add origin https://github.com/your-username/researches-2.git
git push -u origin main
```

---

### PHASE 1: BUILD CORE UI (Day 3-5)

#### Step 1: Generate Base Components with AI

**Prompt to Claude Code / Cursor:**
```
I'm building RESEARCHES 2 application. I need base UI components following the design system.

Design System: Use ./src/design-system/design-system.json as single source of truth
Reference: https://adminrhs.github.io/Video-catalog/

Please create the following components in src/components/ui/:

1. Button component (primary, secondary, outline, ghost variants + sm/md/lg sizes)
2. Input component (default, search variants)
3. Card component (default, elevated, video variants)
4. Modal component (with overlay, header, body, footer)
5. Badge component (priority, department variants)

Requirements:
- TypeScript with full type safety
- Import design tokens from design-system.json
- Support light + dark theme
- All states: default, hover, active, focus, disabled
- Follow exact specs from DESIGN-SYSTEM-INTEGRATION-GUIDE.md

Start with Button component, show me the code.
```

**Review and test each component before moving on.**

#### Step 2: Generate Layout Components

**Prompt:**
```
Now create layout components in src/components/layout/:

1. Sidebar component (expandable/collapsible, 256px/80px width)
   - Dark background (#1F2937) even in light theme
   - Nav items with icons (Lucide)
   - User profile section at bottom
   - Notification badge
   - Smooth transition (300ms ease-in-out)

2. Navbar component
   - Logo
   - Search bar (with voice button)
   - Dark mode toggle
   - Notifications panel (400px dropdown)

3. MainLayout component (combines Sidebar + Navbar + content area)

Use design tokens from design-system.json.
Reference: Components specs in DESIGN-SYSTEM-INTEGRATION-GUIDE.md
```

#### Step 3: Test Core UI

**Create test page** `src/app/test/page.tsx`:
```typescript
import { Button } from '@/components/ui/Button';
import { Input } from '@/components/ui/Input';
import { Card } from '@/components/ui/Card';

export default function TestPage() {
  return (
    <div className="p-8 space-y-8">
      <section>
        <h2 className="text-2xl font-semibold mb-4">Buttons</h2>
        <div className="flex gap-4">
          <Button variant="primary">Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="outline">Outline</Button>
          <Button variant="ghost">Ghost</Button>
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Inputs</h2>
        <Input placeholder="Enter text..." />
        <Input type="search" placeholder="Search..." />
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Cards</h2>
        <Card>Card content here</Card>
      </section>
    </div>
  );
}
```

**Run dev server:**
```bash
npm run dev
```

**Visit**: http://localhost:3000/test

✅ **Verify**: All components render correctly in light + dark mode

---

### PHASE 2: BUILD SEARCH QUEUE MODULE (Day 6-10)

#### Step 1: Generate Database Schema

**Prompt to AI:**
```
Create Prisma schema for Search Queue module based on 02-SEARCH-QUEUE-MODULE-PROMPT.md

Required models:
- SearchTask (search_id, employee, department, topic, status, date_assigned, videos_found, notes)
- SearchPrompt (prompt templates: PMT-048, PMT-089, etc.)

Add to prisma/schema.prisma
```

**After receiving schema:**
```bash
npx prisma generate
npx prisma db push
```

#### Step 2: Generate Search Queue Components

**Prompt:**
```
Generate Search Queue module components based on 02-SEARCH-QUEUE-MODULE-PROMPT.md

Create in src/app/search-queue/:
1. page.tsx (main dashboard)
2. components/SearchQueueDashboard.tsx
3. components/SearchTaskCard.tsx
4. components/CreateSearchTaskModal.tsx
5. components/SearchResultsModal.tsx

Module color: #6D28D9 (Designers Purple from design system)

Requirements:
- Use design-system.json for all styling
- TypeScript with full types
- Status filters: All, Assigned, In_Progress, Completed
- Execute search button (API integration)
- Results modal with video selection
- Add selected to Video Queue

Show me SearchQueueDashboard.tsx first.
```

#### Step 3: Generate API Routes

**Prompt:**
```
Create API routes for Search Queue in src/app/api/search-queue/:

1. route.ts - GET all tasks, POST create task
2. [id]/execute/route.ts - POST execute search
3. [id]/add-to-video-queue/route.ts - POST add videos
4. [id]/complete/route.ts - PUT complete task

Use Prisma for database operations.
Integrate with YouTube Data API v3 for video search.
```

#### Step 4: Test Search Queue Module

1. **Seed test data:**
```bash
npx prisma studio
# Add test search tasks
```

2. **Visit**: http://localhost:3000/search-queue

3. **Test**:
   - ✅ Create new search task
   - ✅ Execute search
   - ✅ View results
   - ✅ Select videos
   - ✅ Add to video queue

---

### PHASE 3: BUILD VIDEO QUEUE MODULE (Day 11-15)

#### Step 1: Generate Database Schema

**Prompt:**
```
Add Video Queue models to prisma/schema.prisma based on 03-VIDEO-QUEUE-MODULE-PROMPT.md

Models:
- VideoQueue (vq_id, youtube_url, title, channel, duration, views, upload_date, topic, source, employee, priority, status, thumbnail, notes)

Priority calculation: 0-100 based on views, recency, duration
Status: Queued, Selected, In_Progress, Completed
```

#### Step 2: Generate Video Queue Components

**Prompt:**
```
Generate Video Queue module based on 03-VIDEO-QUEUE-MODULE-PROMPT.md

Create in src/app/video-queue/:
1. page.tsx (main dashboard)
2. components/VideoQueueDashboard.tsx
3. components/VideoCard.tsx (grid + list view)
4. components/AddVideoModal.tsx
5. components/VideoQueueStats.tsx
6. components/PriorityBadge.tsx

Module color: #147857 (Developers Green from design system)

Features:
- Grid/List view toggle
- Status filters (All, Queued, In_Progress, Completed)
- Priority filters
- Sort by: priority, date, views
- Add video manually (YouTube URL → fetch metadata)
- Move to Phase 1 (next stage)
- Priority badge with stars (⭐⭐⭐⭐⭐ to ⭐)

Show me VideoQueueDashboard.tsx first.
```

#### Step 3: Generate API Routes

**Prompt:**
```
Create API routes for Video Queue in src/app/api/video-queue/:

1. route.ts - GET all videos, POST add video
2. metadata/route.ts - GET fetch YouTube metadata
3. [id]/route.ts - GET, PUT, DELETE video
4. [id]/move-to-phase1/route.ts - POST move to next phase
5. calculate-priority/route.ts - POST calculate priority

Integrate YouTube Data API v3 for metadata.
Priority calculation formula:
- Views: 0-40 points (log scale)
- Recency: 0-40 points (last 30 days = max)
- Duration: 0-20 points (5-20 min = optimal)
```

#### Step 4: Test Video Queue Module

1. **Visit**: http://localhost:3000/video-queue

2. **Test**:
   - ✅ Add video manually (paste YouTube URL)
   - ✅ Fetch metadata automatically
   - ✅ Priority calculated correctly
   - ✅ Grid/List view toggle
   - ✅ Filter by status
   - ✅ Sort options work
   - ✅ Move to Phase 1
   - ✅ Stats update correctly

---

### PHASE 4: BUILD REMAINING MODULES (Day 16-20)

Continue same pattern for:
- **Transcriptions** (Phase 1)
- **Analysis** (Phase 2)
- **Integration** (Phase 3-5)
- **Taxonomy** (Phase 6)
- **Gap Analysis** (Phase 7)

**For each module:**
1. Generate Prisma schema
2. Generate components
3. Generate API routes
4. Test thoroughly

---

### PHASE 5: INTEGRATION & TESTING (Day 21-25)

#### Step 1: Connect All Modules

**Create dashboard** `src/app/page.tsx`:
```typescript
export default function DashboardPage() {
  return (
    <MainLayout>
      <div className="p-8">
        <h1 className="text-4xl font-bold mb-8">RESEARCHES 2 Dashboard</h1>

        <div className="grid grid-cols-3 gap-6">
          <ModuleCard
            title="Search Queue"
            color="#6D28D9"
            count={15}
            href="/search-queue"
          />
          <ModuleCard
            title="Video Queue"
            color="#147857"
            count={128}
            href="/video-queue"
          />
          {/* ... other modules */}
        </div>
      </div>
    </MainLayout>
  );
}
```

#### Step 2: End-to-End Testing

**Test complete workflow:**
1. ✅ Create search task → Execute → Select videos → Add to Video Queue
2. ✅ Video Queue → Move to Transcriptions → Process → Analyze
3. ✅ Analysis → Extract entities → Add to Taxonomy
4. ✅ Taxonomy → View entities → Run gap analysis
5. ✅ Dark mode toggle works everywhere
6. ✅ All filters and sorting work
7. ✅ All API endpoints respond correctly

#### Step 3: Performance Optimization

```bash
# Build production bundle
npm run build

# Analyze bundle size
npm install -D @next/bundle-analyzer
```

**Check:**
- ✅ Page load < 2s
- ✅ Bundle size optimized
- ✅ Images optimized
- ✅ No console errors

---

### PHASE 6: DEPLOYMENT (Day 26-28)

#### Step 1: Deploy Database (Neon)
Already done in Phase 0 ✅

#### Step 2: Deploy Frontend (Vercel)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Follow prompts:
# - Link to GitHub repo
# - Set environment variables
# - Deploy to production
```

**Set environment variables in Vercel dashboard:**
- `DATABASE_URL`
- `OPENAI_API_KEY`
- `DROPBOX_ACCESS_TOKEN`
- `YOUTUBE_API_KEY`

#### Step 3: Deploy Backend (Railway) - Optional

If you need separate backend:
```bash
# Create new Railway project
railway init

# Link to GitHub repo
railway link

# Deploy
railway up
```

#### Step 4: Setup Custom Domain (Optional)

1. Buy domain (Namecheap, Google Domains)
2. Add to Vercel
3. Configure DNS records

---

## ⚡ APPROACH 2: FULL-APP GENERATION

### Step 1: Use Main Prompt (Day 1-3)

**Prompt to Claude Code / Cursor:**
```
Generate complete RESEARCHES 2 application based on FULL-APP-GENERATION-PROMPT.md

Requirements:
- Use design-system.json for ALL styling (no hardcoded values)
- Follow DESIGN-SYSTEM-INTEGRATION-GUIDE.md for implementation
- Create all 7 modules (Search Queue, Video Queue, Transcriptions, Analysis, Integration, Taxonomy, Gap Analysis)
- Full TypeScript with strict mode
- Next.js 14 App Router
- Prisma + PostgreSQL (Neon)
- Tailwind CSS + ShadCN UI
- TanStack Query + Zustand
- Dark mode support

Tech stack:
- Frontend: React 19 + TypeScript + Next.js 14 + Tailwind CSS
- Backend: Node.js + Express + Prisma
- Database: PostgreSQL (Neon)
- APIs: OpenAI, YouTube Data API, Dropbox

Generate project structure first, then we'll build module by module.
```

### Step 2: Review Generated Structure (Day 4)

**Expected structure:**
```
researches-2/
├── src/
│   ├── app/
│   │   ├── (modules)/
│   │   │   ├── search-queue/
│   │   │   ├── video-queue/
│   │   │   ├── transcriptions/
│   │   │   ├── analysis/
│   │   │   ├── integration/
│   │   │   ├── taxonomy/
│   │   │   └── gap-analysis/
│   │   ├── api/
│   │   └── page.tsx
│   ├── components/
│   │   ├── ui/
│   │   └── layout/
│   ├── design-system/
│   ├── lib/
│   └── types/
├── prisma/
├── public/
└── ...config files
```

### Step 3: Test & Iterate (Day 5-10)

1. Test each module
2. Fix bugs
3. Refine UI
4. Add missing features
5. Optimize performance

### Step 4: Deploy (Day 11-12)

Follow deployment steps from Approach 1

---

## 🔧 APPROACH 3: HYBRID (RECOMMENDED)

### Phase 1: Generate Structure (Day 1-2)
Use full-app prompt to generate:
- Project structure
- Base components
- Layout
- Database schema
- API structure

### Phase 2: Build Modules (Day 3-20)
Use module-specific prompts:
- Day 3-7: Search Queue (02-SEARCH-QUEUE-MODULE-PROMPT.md)
- Day 8-12: Video Queue (03-VIDEO-QUEUE-MODULE-PROMPT.md)
- Day 13-20: Remaining modules

### Phase 3: Integration (Day 21-24)
Connect all modules and test workflow

### Phase 4: Deploy (Day 25-28)
Deploy to production

---

## 🎯 PIXEL-PERFECT CHECKLIST

After building, verify against this checklist:

### Design System Integration ✅
- [ ] `design-system.json` imported in all components
- [ ] No hardcoded colors, spacing, or typography
- [ ] Dark mode works everywhere
- [ ] All components match specifications

### Components ✅
- [ ] Button: 8px border-radius, correct padding (10px 20px for md)
- [ ] Input: 12px border-radius, correct padding (12px 16px)
- [ ] Card: 12px border-radius
- [ ] Sidebar: 256px/80px width, #1F2937 background, 300ms transition
- [ ] Scrollbar: 6px width
- [ ] All states implemented (hover, active, focus, disabled)

### Modules ✅
- [ ] Search Queue: #6D28D9 color
- [ ] Video Queue: #147857 color
- [ ] Priority colors: 5-tier system (Critical to Very Low)
- [ ] Priority badges: ⭐ to ⭐⭐⭐⭐⭐

### Performance ✅
- [ ] Page load < 2s
- [ ] Smooth animations (60fps)
- [ ] Optimized bundle size
- [ ] No console errors

### Functionality ✅
- [ ] All CRUD operations work
- [ ] Filters and sorting work
- [ ] API integration works
- [ ] File upload works (Dropbox)
- [ ] OpenAI integration works

---

## 🐛 TROUBLESHOOTING

### Common Issues

#### 1. "Design system not found"
```bash
# Ensure path is correct
import designSystem from '@/design-system/design-system.json';

# Or use absolute import
import designSystem from '../../../design-system/design-system.json';
```

#### 2. "Tailwind classes not working"
```bash
# Rebuild Tailwind
npm run dev

# Check tailwind.config.ts has correct paths
content: ['./src/**/*.{js,ts,jsx,tsx}']
```

#### 3. "Database connection error"
```bash
# Check .env.local has DATABASE_URL
# Re-run Prisma generate
npx prisma generate
npx prisma db push
```

#### 4. "API routes returning 404"
```bash
# Ensure route.ts naming is correct
# Check file is in src/app/api/[route]/route.ts
# Restart dev server
```

#### 5. "Dark mode not working"
```bash
# Ensure ThemeProvider is setup
# Check data-theme attribute on <html>
# Verify dark: classes in Tailwind
```

---

## 📚 HELPFUL RESOURCES

### Documentation
- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Prisma Docs](https://www.prisma.io/docs)
- [TanStack Query](https://tanstack.com/query/latest)
- [ShadCN UI](https://ui.shadcn.com/)

### AI Assistants
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh/)
- [v0.dev](https://v0.dev/)

### APIs
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [OpenAI API](https://platform.openai.com/docs)
- [Dropbox API](https://www.dropbox.com/developers)

---

## ✅ COMPLETION CHECKLIST

### Development ✅
- [ ] All modules built and tested
- [ ] Design system fully integrated
- [ ] Dark mode working
- [ ] All API endpoints functional
- [ ] Database schema complete
- [ ] Error handling implemented
- [ ] Loading states added
- [ ] Responsive design verified

### Quality ✅
- [ ] TypeScript strict mode (no errors)
- [ ] ESLint passing
- [ ] Prettier formatted
- [ ] No console errors/warnings
- [ ] Performance optimized
- [ ] Accessibility (WCAG 2.1 AA)

### Deployment ✅
- [ ] Environment variables set
- [ ] Database deployed (Neon)
- [ ] Frontend deployed (Vercel)
- [ ] Custom domain configured (optional)
- [ ] SSL certificate active
- [ ] Monitoring setup

### Documentation ✅
- [ ] README.md updated
- [ ] API documentation
- [ ] Component documentation
- [ ] Deployment guide
- [ ] User guide

---

## 🎉 SUCCESS!

After completing all steps, you'll have:
- ✅ Fully functional RESEARCHES 2 application
- ✅ Pixel-perfect UI matching design system
- ✅ All 7 modules operational
- ✅ Dark mode support
- ✅ Production deployment
- ✅ Complete documentation

**Estimated Timeline:**
- **Approach 1** (Component-by-Component): 3-4 weeks
- **Approach 2** (Full-App Generation): 1-2 weeks
- **Approach 3** (Hybrid): 2-3 weeks

**Next Steps:**
1. Choose your approach
2. Follow the step-by-step guide
3. Use AI assistants with provided prompts
4. Test thoroughly
5. Deploy to production
6. Celebrate! 🎉

---

**Version:** 1.0
**Last Updated:** 2025-12-08
**Status:** Ready to Build ✅

**Questions?** Review:
- [FULL-APP-GENERATION-PROMPT.md](./FULL-APP-GENERATION-PROMPT.md)
- [DESIGN-SYSTEM-INTEGRATION-GUIDE.md](./DESIGN-SYSTEM-INTEGRATION-GUIDE.md)
- [02-SEARCH-QUEUE-MODULE-PROMPT.md](./02-SEARCH-QUEUE-MODULE-PROMPT.md)
- [03-VIDEO-QUEUE-MODULE-PROMPT.md](./03-VIDEO-QUEUE-MODULE-PROMPT.md)
