# Execution Flow - Building 10 Screen Apps with Lovable

**Last Updated:** 2025-11-28
**Total Screens:** 10
**Estimated Total Time:** 2-4 hours

---

## 📋 Overview

This execution flow guides you through building all 10 screen components for the Research Management Application using Lovable AI. Each screen can be built independently in 10-30 minutes.

---

## 🎯 Pre-Build Setup

### Step 1: Prepare Lovable Environment
1. Create a new Lovable project (or use existing)
2. Name: "Research App Screens"
3. **CRITICAL:** Paste custom instructions FIRST

### Step 2: Add Custom Instructions to Lovable
Open and paste these files into Lovable's custom instructions:

```
📂 custom_instructions/01_project_setup.md
📂 custom_instructions/02_design_system_reference.md
```

**What to paste:**
- Project setup (tech stack, dependencies, standards)
- Design system (colors, icons, patterns)

### Step 3: Organize Your Prompts
You have two options:

**Option A (Recommended):** Use consolidated file
- Open: `ALL_REMAINING_PROMPTS.md`
- Copy each screen section as you build

**Option B:** Split into individual files
- Extract each prompt to its folder's `prompt.md`
- Build from individual files

---

## 🚀 Build Order (Recommended Sequence)

Build in this order for logical progression and dependency management:

### Phase 1: Foundation Screens (Easiest - Start Here)
**Goal:** Build UI components with mock data, no complex interactions

| Order | Screen | Complexity | Time | Why This Order |
|-------|--------|------------|------|----------------|
| 1 | `04_dashboard_stats` | ⭐ Easy | 10 min | Simple cards, no forms - confidence builder |
| 2 | `09_cost_tracker_widget` | ⭐ Easy | 10 min | Similar to dashboard, practice with data display |
| 3 | `08_progress_tracker_widget` | ⭐⭐ Medium | 15 min | Visual timeline, introduces phase concepts |

### Phase 2: Data Entry & Interaction
**Goal:** Add forms, validation, user input handling

| Order | Screen | Complexity | Time | Why This Order |
|-------|--------|------------|------|----------------|
| 4 | `03_filter_panel` | ⭐ Easy | 10 min | Reusable component, checkbox interactions |
| 5 | `02_search_queue_screen` | ⭐⭐ Medium | 15 min | Table + basic CRUD, already completed |
| 6 | `01_video_queue_screen` | ⭐⭐ Medium | 20 min | Similar to search queue, full forms |
| 7 | `05_upload_transcription_screen` | ⭐⭐ Medium | 20 min | File upload, validation, dropzone |

### Phase 3: Advanced Components
**Goal:** Complex data visualization and comparison

| Order | Screen | Complexity | Time | Why This Order |
|-------|--------|------------|------|----------------|
| 8 | `06_entity_extraction_viewer` | ⭐⭐ Medium | 20 min | Tabbed interface, entity cards |
| 9 | `07_gap_analysis_screen` | ⭐⭐⭐ Complex | 25 min | Side-by-side comparison, approval workflow |
| 10 | `10_knowledge_map_viewer` | ⭐⭐⭐ Complex | 30 min | React Flow graph, most complex |

**Total Estimated Time:** ~2 hours 45 minutes

---

## 📝 Build Template (Use for Each Screen)

### Before Starting Each Screen

1. **Read the prompt** - Understand features and requirements
2. **Review mock data** - Know what test data looks like
3. **Check dependencies** - Note required libraries (React Dropzone, React Flow, etc.)
4. **Clear Lovable context** - Start fresh conversation for each screen (optional but recommended)

### Building Process

```markdown
┌─────────────────────────────────────────┐
│ Step 1: Copy Lovable Initiation Phrase │
└─────────────────────────────────────────┘
↓
From the prompt.md, copy the text inside the code block under "Lovable Initiation Phrase"

┌─────────────────────────────────────────┐
│ Step 2: Paste into Lovable             │
└─────────────────────────────────────────┘
↓
Paste the initiation phrase into Lovable chat
Let Lovable generate initial structure

┌─────────────────────────────────────────┐
│ Step 3: Provide Full Specification     │
└─────────────────────────────────────────┘
↓
Tell Lovable: "Follow the complete specification below"
Paste the entire prompt content (all sections)

┌─────────────────────────────────────────┐
│ Step 4: Add Mock Data                  │
└─────────────────────────────────────────┘
↓
Copy the "Sample Data" section from prompt
Paste into Lovable: "Use this mock data for testing"

┌─────────────────────────────────────────┐
│ Step 5: Review & Test                  │
└─────────────────────────────────────────┘
↓
- Check UI matches AdminRHS-AI-Catalog design
- Test with mock data
- Verify all features from checklist
- Test user input and validation (if applicable)

┌─────────────────────────────────────────┐
│ Step 6: Export Code                    │
└─────────────────────────────────────────┘
↓
Download the built component
Save to local project folder
```

### Testing Checklist (Use for Each Screen)

After building each screen, verify:

- [ ] Component renders without errors
- [ ] Mock data displays correctly
- [ ] UI matches AdminRHS-AI-Catalog design (blue theme)
- [ ] Colors match design system (#428eb4 primary)
- [ ] All features from prompt work
- [ ] Forms validate correctly (if applicable)
- [ ] Responsive on mobile (test in Lovable preview)
- [ ] No console errors

---

## 🔥 Detailed Build Instructions by Screen

### 1. Dashboard Stats (`04_dashboard_stats`)

**What you're building:** Statistics cards showing total videos, completion rates, trends

**Key features:**
- 4 stat cards (total videos, in progress, completed, rate)
- Line chart showing 7-day trend
- Mock data: MOCK_STATS + MOCK_TREND_DATA

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase from prompt]
Lovable: [Generates initial structure]
You: "Use this mock data: [paste MOCK_STATS and MOCK_TREND_DATA]"
Lovable: [Implements with mock data]
You: "Add Recharts line chart for trend visualization"
```

**Common issues:**
- Missing Recharts dependency → Tell Lovable to add it
- Chart not displaying → Verify MOCK_TREND_DATA format

---

### 2. Cost Tracker Widget (`09_cost_tracker_widget`)

**What you're building:** AI API usage cost display with model breakdown

**Key features:**
- Cost summary card (total spent, budget remaining)
- Model usage breakdown table
- Mock data: MOCK_API_USAGE

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Use this API usage data: [paste MOCK_API_USAGE]"
You: "Show cost per model with color-coded status"
```

**Common issues:**
- Cost calculations wrong → Verify token pricing in mock data
- Table sorting not working → Request TanStack Table integration

---

### 3. Progress Tracker Widget (`08_progress_tracker_widget`)

**What you're building:** Visual timeline showing 7 processing phases

**Key features:**
- 7 color-coded phases (Gray → Blue → Green → Yellow → Orange → Purple → Emerald)
- Checkmarks for completed phases
- Progress percentage bar
- Mock data: MOCK_VIDEO_PROGRESS

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Use these phase colors exactly: [paste PHASE_COLORS from prompt]"
You: "Test with this progress data: [paste MOCK_VIDEO_PROGRESS]"
```

**Common issues:**
- Wrong phase colors → Copy exact hex codes from prompt
- Checkmarks not showing → Verify CheckCircle2 icon import from lucide-react

---

### 4. Filter Panel (`03_filter_panel`)

**What you're building:** Reusable sidebar filter with checkboxes and pills

**Key features:**
- Collapsible accordion sections
- Multi-select checkboxes
- Active filter pills (click to remove)
- Clear all button
- Mock data: FILTER_OPTIONS

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Make it a reusable component with onFilterChange prop"
You: "Use this filter data: [paste FILTER_OPTIONS]"
You: "Add active filter pills with × to remove"
```

**Common issues:**
- Props not typed → Request TypeScript interfaces for FilterPanelProps
- Accordion not opening → Verify shadcn/ui Accordion component installed

---

### 5. Search Queue Screen (`02_search_queue_screen`)

**Status:** Already completed ✅

**What's included:**
- TanStack Table with sorting/filtering
- Status badges
- Mock data: MOCK_SEARCHES

**If rebuilding:**
```
You: [Paste Lovable Initiation Phrase]
You: "Use TanStack Table for data grid"
You: "Test with: [paste MOCK_SEARCHES]"
```

---

### 6. Video Queue Screen (`01_video_queue_screen`)

**What you're building:** Main video queue table with full CRUD operations

**Key features:**
- Add video dialog with React Hook Form + Zod validation
- Edit video (pre-filled form)
- Delete confirmation
- Filter by status/department
- Mock data: MOCK_VIDEOS

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Add video form must use React Hook Form with this Zod schema: [paste videoSchema]"
You: "Include validation error messages for each field"
You: "Test with: [paste MOCK_VIDEOS]"
```

**Common issues:**
- Form validation not working → Verify zodResolver setup
- Errors not displaying → Check form.formState.errors mapping
- URL validation failing → Ensure Zod .url() validator used

**Critical validation requirements:**
- video_url: Valid URL format
- video_title: Min 3 characters
- duration_minutes: Number 1-999
- priority: Enum ['low', 'medium', 'high']
- department: Enum ['DEV', 'SMM', 'VID', 'AID', 'DGN', 'MKT']

---

### 7. Upload Transcription Screen (`05_upload_transcription_screen`)

**What you're building:** File upload screen with drag & drop

**Key features:**
- React Dropzone for drag & drop
- File validation (.txt, .srt, .vtt only, max 10MB)
- File preview (first 500 chars)
- Upload progress bar
- Mock data: MOCK_VIDEOS_FOR_UPLOAD

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Use React Dropzone with these accept types: [paste accept config]"
You: "Add Zod validation for file size (10MB max) and file type"
You: "Show file preview after selection"
You: "Test with: [paste MOCK_VIDEOS_FOR_UPLOAD]"
```

**Common issues:**
- Dropzone not accepting files → Check accept MIME types
- File preview not showing → Verify FileReader implementation
- Validation not triggering → Ensure Zod .refine() used correctly

**Critical validation:**
```typescript
file: z.instanceof(File)
  .refine(file => file.size <= 10 * 1024 * 1024, 'File must be less than 10MB')
  .refine(
    file => ['.txt', '.srt', '.vtt'].some(ext => file.name.endsWith(ext)),
    'Only .txt, .srt, or .vtt files allowed'
  )
```

---

### 8. Entity Extraction Viewer (`06_entity_extraction_viewer`)

**What you're building:** Tabbed interface showing extracted entities by type

**Key features:**
- 4 tabs: Tools, Workflows, Actions, Objects
- Entity cards with classification badges (NEW/EXISTING/UPDATE)
- Search filter
- Export to JSON
- Mock data: MOCK_EXTRACTED_TOOLS, MOCK_EXTRACTED_WORKFLOWS, etc.

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Create 4 tabs, each with its own mock data set"
You: "Use these classification colors: NEW=green, EXISTING=gray, UPDATE=yellow"
You: "Add export JSON functionality for each tab"
You: "Test with: [paste all MOCK_EXTRACTED_* arrays]"
```

**Common issues:**
- Tab switching not working → Verify shadcn/ui Tabs component
- Badge colors wrong → Use getClassificationColor() function from prompt
- Export not downloading → Check Blob + URL.createObjectURL setup

---

### 9. Gap Analysis Screen (`07_gap_analysis_screen`)

**What you're building:** Side-by-side comparison with approval workflow

**Key features:**
- Two-column comparison (Extracted vs Existing)
- Difference highlighting in yellow
- Approval dialog with 5 action types
- Notes textarea with React Hook Form
- Filter tabs (NEW/EXISTING/UPDATE)
- Mock data: MOCK_GAP_ANALYSIS

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Left column: Extracted data (green background)"
You: "Right column: Existing data (blue background) or 'No Match Found' (gray)"
You: "Highlight differences in yellow with strikethrough → arrow → new value"
You: "Approval dialog uses React Hook Form with Zod schema: [paste approvalSchema]"
You: "Test with: [paste MOCK_GAP_ANALYSIS]"
```

**Common issues:**
- Comparison columns not aligned → Use CSS Grid with grid-cols-2
- Differences not highlighted → Check differences.some() logic
- Dialog not opening → Verify Dialog state management
- Form not submitting → Check form.handleSubmit() setup

**Critical approval actions:**
- APPROVE_NEW (for NEW entities)
- SKIP_DUPLICATE (for EXISTING entities)
- APPROVE_UPDATE (for UPDATE entities)
- REJECT
- MANUAL_REVIEW

---

### 10. Knowledge Map Viewer (`10_knowledge_map_viewer`)

**What you're building:** Interactive graph visualization with React Flow

**Key features:**
- Interactive node graph (zoom, pan, drag)
- 4 node types: tool, workflow, action, object (color-coded)
- Node detail sidebar on click
- Entity type filter checkboxes
- Relationship edges (uses, contains, requires)
- Mock data: MOCK_NODES, MOCK_EDGES

**Lovable conversation:**
```
You: [Paste Lovable Initiation Phrase]
Lovable: [Generates structure]
You: "Use React Flow with custom node types for each entity type"
You: "Node colors: tool=#428eb4, workflow=#34D399, action=#FBBF24, object=#A78BFA"
You: "Add node click handler to show detail sidebar"
You: "Test with: [paste MOCK_NODES and MOCK_EDGES]"
```

**Common issues:**
- Graph not rendering → Add 'reactflow/dist/style.css' import
- Nodes not draggable → Verify useNodesState/useEdgesState hooks
- Custom nodes not showing → Check nodeTypes prop configuration
- Sidebar not updating → Verify selectedNode state management

**Critical setup:**
```typescript
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState
} from 'reactflow';
import 'reactflow/dist/style.css';
```

---

## 🔄 Merge Strategy (After Building All 10)

Once all screens are built individually, merge them into 2 complete apps:

### App 1: Queue Management (Screens 1-4)
```
Queue Management App/
├── 01_video_queue_screen ──┐
├── 02_search_queue_screen ─┤
├── 03_filter_panel ────────┤ → Merge into single app
└── 04_dashboard_stats ─────┘
```

**Merge steps:**
1. Set up React Router
2. Create navigation sidebar
3. Add shared Context for filter state
4. Integrate FilterPanel into queue screens
5. Dashboard as home page

### App 2: Video Processing (Screens 5-10)
```
Video Processing App/
├── 05_upload_transcription_screen ──┐
├── 06_entity_extraction_viewer ─────┤
├── 07_gap_analysis_screen ──────────┤
├── 08_progress_tracker_widget ──────┤ → Merge into single app
├── 09_cost_tracker_widget ──────────┤
└── 10_knowledge_map_viewer ─────────┘
```

**Merge steps:**
1. Set up React Router with phase-based routes
2. Create phase navigation
3. Add ProgressTrackerWidget to all pages (shared component)
4. CostTrackerWidget in dashboard/header
5. Create multi-step flow: Upload → Extract → Analyze → Map

---

## 📊 Progress Tracking

Use this checklist to track your build progress:

### Foundation Screens
- [ ] 04_dashboard_stats (10 min)
- [ ] 09_cost_tracker_widget (10 min)
- [ ] 08_progress_tracker_widget (15 min)

### Data Entry & Interaction
- [ ] 03_filter_panel (10 min)
- [ ] 02_search_queue_screen (15 min) ✅ Already complete
- [ ] 01_video_queue_screen (20 min)
- [ ] 05_upload_transcription_screen (20 min)

### Advanced Components
- [ ] 06_entity_extraction_viewer (20 min)
- [ ] 07_gap_analysis_screen (25 min)
- [ ] 10_knowledge_map_viewer (30 min)

### Integration
- [ ] Merge App 1: Queue Management
- [ ] Merge App 2: Video Processing
- [ ] Connect to Supabase (replace mock data)
- [ ] Final testing

---

## 🎨 Design Consistency Checklist

For every screen, ensure:

- [ ] Primary color: `#428eb4` (accent-blue)
- [ ] Hover color: `#28749b` (accent-blue-hover)
- [ ] Phase colors match: Gray, Blue, Green, Yellow, Orange, Purple, Emerald
- [ ] shadcn/ui components only (no MUI, Ant Design, etc.)
- [ ] Tailwind CSS for styling
- [ ] Responsive design (mobile-friendly)
- [ ] All icons from lucide-react (24x24px)

---

## 🐛 Common Issues & Solutions

### Issue: "Lovable doesn't understand the prompt"
**Solution:** Break it down:
1. Start with Lovable Initiation Phrase only
2. Let it generate structure
3. Then add mock data
4. Then add specific features one by one

### Issue: "Mock data not displaying"
**Solution:**
- Verify data structure matches interface
- Check array is exported correctly
- Ensure component imports mock data
- Add console.log to debug

### Issue: "Form validation not working"
**Solution:**
- Verify Zod schema matches form fields
- Check zodResolver is imported from @hookform/resolvers/zod
- Ensure form.formState.errors is checked
- Add error display components

### Issue: "Colors don't match design"
**Solution:**
- Copy exact hex codes from custom_instructions/02_design_system_reference.md
- Use style props for dynamic colors (phase colors)
- Verify Tailwind classes match

### Issue: "Dependencies missing"
**Solution:**
Tell Lovable: "Add these dependencies: [list]"
- React Hook Form: `npm i react-hook-form`
- Zod: `npm i zod @hookform/resolvers`
- React Dropzone: `npm i react-dropzone`
- React Flow: `npm i reactflow`
- Recharts: `npm i recharts`

---

## 💡 Pro Tips

### Speed Up Build Time
1. **Reuse patterns:** Once you build filter panel, copy pattern for other filters
2. **Template forms:** Video queue form → Template for other CRUD forms
3. **Batch similar screens:** Build all "easy" screens first for momentum

### Avoid Common Mistakes
1. **Don't skip mock data:** Always test with mock data first
2. **Don't customize too early:** Build to spec first, customize later
3. **Don't merge prematurely:** Get all 10 working individually first

### Quality Checks
1. **Test edge cases:** Empty states, loading states, error states
2. **Check responsiveness:** Test on mobile viewport
3. **Verify accessibility:** Keyboard navigation, ARIA labels
4. **Console clean:** No errors or warnings

---

## 📈 Next Steps After Completion

1. **Local Setup:**
   - Create Vite + React + TS project
   - Install all dependencies
   - Copy Lovable-generated code
   - Test locally

2. **Supabase Integration:**
   - Create Supabase project
   - Run database schemas from prompts
   - Replace mock data with Supabase queries
   - Add real-time subscriptions

3. **Deployment:**
   - Push to GitHub
   - Deploy to Vercel/Netlify
   - Configure environment variables
   - Test production build

---

## 🎯 Success Criteria

You're done when:

- ✅ All 10 screens build without errors
- ✅ Mock data displays correctly on all screens
- ✅ Forms validate user input properly
- ✅ Design matches AdminRHS-AI-Catalog
- ✅ All features from checklists work
- ✅ No console errors
- ✅ Responsive on mobile
- ✅ Ready to merge into 2 apps

---

**Estimated Total Time:** 2-4 hours (depending on experience)

**Ready to start?** Begin with `04_dashboard_stats` - the easiest screen! 🚀
