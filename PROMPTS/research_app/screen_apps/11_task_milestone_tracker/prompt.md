# Screen 11: Task & Milestone Tracker

Build a comprehensive Task and Milestone tracking dashboard that extracts actionable work items from video transcriptions.

---

## Tech Stack
- React 18 + TypeScript + Vite
- Supabase (database + real-time subscriptions)
- shadcn/ui components
- TanStack Table v8
- Lucide React icons
- Tailwind CSS

---

## Design System

Use the **AdminRHS-AI-Catalog Design System**:

### Colors
```typescript
const COLORS = {
  // Primary
  accentBlue: '#428eb4',

  // Phase Colors
  phase0: '#9CA3AF',  // Gray - Research
  phase1: '#60A5FA',  // Blue - Transcription
  phase2: '#34D399',  // Green - Entity Extraction
  phase3: '#FBBF24',  // Yellow - Gap Analysis
  phase4: '#F97316',  // Orange - Integration
  phase5: '#A78BFA',  // Purple - Knowledge Mapping
  complete: '#10B981', // Emerald - Complete

  // Task Status
  pending: '#9CA3AF',    // Gray
  in_progress: '#60A5FA', // Blue
  completed: '#10B981',   // Green
  blocked: '#EF4444',     // Red

  // Priority
  low: '#9CA3AF',      // Gray
  medium: '#FBBF24',   // Yellow
  high: '#F97316',     // Orange
  critical: '#EF4444'  // Red
}
```

### Typography
- **Headings**: font-bold, tracking-tight
- **Body**: font-normal, leading-relaxed
- **Monospace**: font-mono for IDs (MLS-001, TSK-001)

---

## Database Schema

### Table: `milestones`
```sql
CREATE TABLE milestones (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  milestone_id TEXT UNIQUE NOT NULL, -- e.g., "MLS-001"
  milestone_name TEXT NOT NULL,
  objective TEXT NOT NULL,
  video_id UUID REFERENCES video_queue(id),
  duration TEXT, -- e.g., "20-30 minutes"
  complexity TEXT, -- Low, Medium, Medium-High, High
  department TEXT, -- AID, DEV, SEC, QA, etc.
  status TEXT DEFAULT 'pending', -- pending, in_progress, completed, blocked
  progress INTEGER DEFAULT 0, -- 0-100
  related_tasks TEXT[], -- Array of TSK-IDs
  related_skills TEXT[], -- Array of SKL-IDs
  related_responsibilities TEXT[], -- Array of RSP-IDs
  related_professions TEXT[], -- Array of PRF-IDs
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

CREATE INDEX idx_milestones_video ON milestones(video_id);
CREATE INDEX idx_milestones_status ON milestones(status);
CREATE INDEX idx_milestones_department ON milestones(department);
```

### Table: `tasks`
```sql
CREATE TABLE tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id TEXT UNIQUE NOT NULL, -- e.g., "TSK-001"
  task_name TEXT NOT NULL,
  description TEXT,
  milestone_id UUID REFERENCES milestones(id),
  video_id UUID REFERENCES video_queue(id),
  status TEXT DEFAULT 'pending', -- pending, in_progress, completed, blocked
  priority TEXT DEFAULT 'medium', -- low, medium, high, critical
  assignee TEXT, -- Email or name
  department TEXT,
  estimated_duration TEXT, -- e.g., "15 minutes"
  complexity TEXT, -- Low, Medium, High
  dependencies TEXT[], -- Array of other TSK-IDs
  related_skills TEXT[],
  related_tools TEXT[],
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

CREATE INDEX idx_tasks_milestone ON tasks(milestone_id);
CREATE INDEX idx_tasks_video ON tasks(video_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_priority ON tasks(priority);
CREATE INDEX idx_tasks_assignee ON tasks(assignee);
```

---

## Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Header: Task & Milestone Tracker                    [Phase]│
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │  📊 Stats   │ │  🎯 Active  │ │  ✅ Done    │          │
│  │  24 Total   │ │  12 Tasks   │ │  8 Tasks    │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
├─────────────────────────────────────────────────────────────┤
│  [Tabs: 🎯 Milestones | ✅ Tasks | 📊 Gantt View]          │
├─────────────────────────────────────────────────────────────┤
│  Filters: [Status ▼] [Dept ▼] [Priority ▼] [🔍 Search]    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MILESTONE VIEW (Kanban-style columns):                    │
│                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │  📋 Pending │ │ 🔄 Progress │ │ ✅ Complete │          │
│  ├─────────────┤ ├─────────────┤ ├─────────────┤          │
│  │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │          │
│  │ │ MLS-001 │ │ │ │ MLS-002 │ │ │ │ MLS-004 │ │          │
│  │ │ Prepare │ │ │ │ Config  │ │ │ │ Test    │ │          │
│  │ │ Baseline│ │ │ │ ScaleKit│ │ │ │ OAuth   │ │          │
│  │ │         │ │ │ │ [60%]   │ │ │ │ [100%]  │ │          │
│  │ │ 3 tasks │ │ │ │ 2/3 ✓   │ │ │ │ 3/3 ✓   │ │          │
│  │ │ AID     │ │ │ │ SEC/AID │ │ │ │ QA/AID  │ │          │
│  │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │          │
│  └─────────────┘ └─────────────┘ └─────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Features

### 1. Milestone Kanban Board
- **Columns**: Pending, In Progress, Completed, Blocked
- **Drag & Drop**: Move milestones between columns (update status)
- **Milestone Cards** show:
  - Milestone ID (MLS-XXX) with monospace font
  - Milestone Name
  - Progress bar (% complete based on tasks)
  - Task count (e.g., "3/5 tasks completed")
  - Department badge
  - Complexity indicator
  - Duration estimate
  - Related video link
- **Click card** → Open milestone detail modal

### 2. Task Table View
- **TanStack Table** with columns:
  - Task ID (TSK-XXX)
  - Task Name
  - Milestone (clickable link)
  - Status badge (color-coded)
  - Priority badge (color-coded)
  - Assignee (avatar + name)
  - Department
  - Duration estimate
  - Actions (Edit, Mark Complete, Delete)
- **Sortable** by any column
- **Filterable** by status, priority, department, assignee
- **Searchable** by task name or description
- **Bulk actions**: Select multiple tasks → Bulk assign, Bulk status update

### 3. Gantt Chart View (Optional, Phase 2)
- Timeline visualization of milestones
- Dependencies between tasks
- Critical path highlighting
- Resource allocation view

### 4. Stats Dashboard
- **Total Milestones**: Count by status
- **Total Tasks**: Count by status
- **Completion Rate**: % of completed vs total
- **Average Task Duration**: Calculated from completed tasks
- **Tasks by Department**: Pie chart breakdown
- **Tasks by Priority**: Bar chart
- **Blocked Tasks Alert**: Red badge if any blocked tasks exist

### 5. Milestone Detail Modal
When clicking a milestone card:
```
┌────────────────────────────────────────────────┐
│ MLS-002: Configure ScaleKit Authorization     │
│ ──────────────────────────────────────────────│
│ Objective:                                     │
│ Set up ScaleKit workspace, scopes, and MCP    │
│ server registration                            │
│                                                │
│ Status: [In Progress ▼]  Progress: [60%]      │
│ Department: SEC/AID      Complexity: Medium   │
│ Duration: 25-35 minutes                        │
│                                                │
│ Tasks (2/3 completed):                         │
│ ✅ TSK-004: Activate ScaleKit environments    │
│ ✅ TSK-005: Define OAuth scopes                │
│ ⏳ TSK-006: Register MCP identifier            │
│                                                │
│ Related Entities:                              │
│ Skills: SKL-078 (Identity & Access Mgmt)       │
│ Responsibilities: RSP-315 (OAuth Policy)       │
│ Professions: PRF-012 (Security Engineer)       │
│                                                │
│ Video Source:                                  │
│ 📹 Tutorial: Auth for Remote MCP Servers       │
│                                                │
│ [Update Milestone] [View All Tasks] [Close]   │
└────────────────────────────────────────────────┘
```

### 6. Task Detail Modal
When clicking a task:
```
┌────────────────────────────────────────────────┐
│ TSK-006: Register MCP Identifier               │
│ ──────────────────────────────────────────────│
│ Description:                                   │
│ Map localhost endpoint and enable dynamic     │
│ registration                                   │
│                                                │
│ Status: [Pending ▼]    Priority: [High ▼]     │
│ Assignee: [Select... ▼]                       │
│ Department: SEC        Complexity: Medium     │
│ Est. Duration: 10 minutes                      │
│                                                │
│ Parent Milestone:                              │
│ MLS-002: Configure ScaleKit Authorization     │
│                                                │
│ Dependencies:                                  │
│ ⬅ TSK-005 must be completed first             │
│                                                │
│ Related:                                       │
│ Skills: SKL-078                                │
│ Tools: ScaleKit, FastAPI                       │
│                                                │
│ Notes:                                         │
│ [Text area for additional notes...]           │
│                                                │
│ [Update Task] [Mark Complete] [Delete] [Close]│
└────────────────────────────────────────────────┘
```

### 7. Quick Actions
- **Add Milestone**: Manual creation form
- **Add Task**: Manual creation form (with milestone dropdown)
- **Import from Video**: Button to extract milestones/tasks from video transcription
  - Opens modal with video selector
  - Parse transcription for MILESTONE and TASK blocks
  - Batch import all extracted items
- **Export**: Download tasks as CSV, JSON, or Markdown checklist

### 8. Filters & Search
```typescript
interface Filters {
  status: 'all' | 'pending' | 'in_progress' | 'completed' | 'blocked';
  priority: 'all' | 'low' | 'medium' | 'high' | 'critical';
  department: 'all' | 'AID' | 'DEV' | 'SEC' | 'QA' | 'MKT' | 'DGN' | 'VID' | 'SMM';
  assignee: 'all' | 'unassigned' | string; // email
  milestone: 'all' | string; // milestone_id
  videoSource: 'all' | string; // video_id
  search: string; // Free text search
}
```

Apply filters via dropdown selects and search input with debounce.

---

## Component Structure

```typescript
// Main screen
TaskMilestoneTracker.tsx
├── StatsCards.tsx           // Top 3 stat cards
├── TabNavigation.tsx        // Switch between views
├── FilterBar.tsx            // All filter dropdowns + search
├── MilestoneKanban.tsx      // Kanban board view
│   ├── KanbanColumn.tsx
│   └── MilestoneCard.tsx
├── TaskTable.tsx            // TanStack Table
│   └── TaskRow.tsx
├── GanttView.tsx            // (Phase 2)
├── MilestoneDetailModal.tsx
├── TaskDetailModal.tsx
├── AddMilestoneModal.tsx
├── AddTaskModal.tsx
└── ImportFromVideoModal.tsx
```

---

## State Management

Use React Query for server state:

```typescript
// Fetch milestones
const { data: milestones } = useQuery({
  queryKey: ['milestones', filters],
  queryFn: () => supabase
    .from('milestones')
    .select('*, tasks(count)')
    .match(filters)
});

// Fetch tasks
const { data: tasks } = useQuery({
  queryKey: ['tasks', filters],
  queryFn: () => supabase
    .from('tasks')
    .select('*, milestone:milestones(milestone_name)')
    .match(filters)
});

// Update milestone status
const updateMilestone = useMutation({
  mutationFn: (data) => supabase
    .from('milestones')
    .update(data)
    .eq('id', data.id),
  onSuccess: () => queryClient.invalidateQueries(['milestones'])
});
```

---

## Interactions

### Drag & Drop (Milestone Kanban)
Use `@dnd-kit/core` for drag-and-drop:
```typescript
import { DndContext, closestCenter, PointerSensor, useSensor } from '@dnd-kit/core';

<DndContext onDragEnd={handleDragEnd}>
  <KanbanColumn status="pending">
    {milestones.filter(m => m.status === 'pending').map(m => (
      <MilestoneCard key={m.id} milestone={m} />
    ))}
  </KanbanColumn>
  {/* ... other columns ... */}
</DndContext>
```

When dropped, update status and recalculate progress.

### Task Progress Calculation
```typescript
function calculateMilestoneProgress(milestone: Milestone): number {
  const tasks = milestone.related_tasks;
  if (!tasks || tasks.length === 0) return 0;

  const completedCount = tasks.filter(t => t.status === 'completed').length;
  return Math.round((completedCount / tasks.length) * 100);
}
```

Auto-update milestone status:
- All tasks completed → Milestone = "completed"
- Any task in progress → Milestone = "in_progress"
- Any task blocked → Milestone = "blocked" (optional)

### Mark Task Complete
```typescript
async function markTaskComplete(taskId: string) {
  await supabase
    .from('tasks')
    .update({
      status: 'completed',
      completed_at: new Date().toISOString()
    })
    .eq('id', taskId);

  // Recalculate parent milestone progress
  const task = tasks.find(t => t.id === taskId);
  if (task?.milestone_id) {
    updateMilestoneProgress(task.milestone_id);
  }
}
```

---

## Import from Video

**ImportFromVideoModal.tsx**:
1. User selects video from dropdown (load from `video_queue`)
2. Fetch video transcription content
3. Parse transcription for milestone/task blocks:

```typescript
interface ParsedMilestone {
  milestone_id: string;
  milestone_name: string;
  objective: string;
  duration: string;
  complexity: string;
  department: string;
  tasks: ParsedTask[];
  related_skills: string[];
  related_responsibilities: string[];
  related_professions: string[];
}

interface ParsedTask {
  task_id: string;
  task_name: string;
  description?: string;
}

// Parser regex
const MILESTONE_REGEX = /```\nMILESTONE_ID: (MLS-\d+)\nMILESTONE_NAME: (.+?)\nOBJECTIVE: (.+?)\nTASKS:\n([\s\S]+?)DURATION: (.+?)\nCOMPLEXITY: (.+?)\nDEPARTMENT: (.+?)\n/g;

const TASK_REGEX = /(\d+)\. (TSK-\d+): (.+?) - (.+)/g;
```

4. Display preview table showing all parsed milestones and tasks
5. User confirms → Batch insert to Supabase
6. Show success toast with count (e.g., "Imported 4 milestones and 12 tasks")

---

## Sample Mock Data

For initial development, use this mock data:

```typescript
const MOCK_MILESTONES = [
  {
    milestone_id: 'MLS-001',
    milestone_name: 'Prepare Baseline MCP Server',
    objective: 'Stand up the FastMCP-powered Tavilli server locally on HTTP transport',
    video_id: 'video-024-uuid',
    duration: '20-30 minutes',
    complexity: 'Low',
    department: 'AID',
    status: 'completed',
    progress: 100,
    related_tasks: ['TSK-001', 'TSK-002', 'TSK-003'],
    related_skills: ['SKL-042', 'SKL-006'],
    related_responsibilities: ['RSP-201'],
    related_professions: ['PRF-003']
  },
  {
    milestone_id: 'MLS-002',
    milestone_name: 'Configure ScaleKit Authorization Stack',
    objective: 'Set up ScaleKit workspace, scopes, and MCP server registration',
    video_id: 'video-024-uuid',
    duration: '25-35 minutes',
    complexity: 'Medium',
    department: 'SEC',
    status: 'in_progress',
    progress: 67,
    related_tasks: ['TSK-004', 'TSK-005', 'TSK-006']
  },
  {
    milestone_id: 'MLS-003',
    milestone_name: 'Implement OAuth Discovery & Middleware',
    objective: 'Add well-known endpoint plus middleware that enforces ScaleKit-issued JWTs',
    video_id: 'video-024-uuid',
    duration: '30-40 minutes',
    complexity: 'Medium-High',
    department: 'AID',
    status: 'pending',
    progress: 0,
    related_tasks: ['TSK-007', 'TSK-008', 'TSK-009']
  }
];

const MOCK_TASKS = [
  {
    task_id: 'TSK-001',
    task_name: 'Initialize FastMCP service',
    description: 'Scaffold Tavilli MCP server with FastAPI',
    milestone_id: 'milestone-001-uuid',
    status: 'completed',
    priority: 'medium',
    department: 'AID',
    estimated_duration: '10 minutes',
    complexity: 'Low',
    completed_at: '2025-11-27T10:30:00Z'
  },
  {
    task_id: 'TSK-006',
    task_name: 'Register MCP identifier',
    description: 'Map localhost endpoint and enable dynamic registration',
    milestone_id: 'milestone-002-uuid',
    status: 'in_progress',
    priority: 'high',
    department: 'SEC',
    assignee: 'alex@remotehelpers.com',
    estimated_duration: '10 minutes',
    complexity: 'Medium',
    dependencies: ['TSK-005']
  }
];
```

---

## Responsive Design

- **Desktop** (>1024px): 3-column Kanban, full table
- **Tablet** (768-1024px): 2-column Kanban, condensed table
- **Mobile** (<768px): 1-column list view, card-based tasks

---

## Accessibility

- Keyboard navigation for Kanban (arrow keys to move between cards)
- Screen reader labels for all interactive elements
- Focus indicators on drag handles
- ARIA labels for status badges
- Semantic HTML (use `<article>` for milestone cards)

---

## Success Criteria

✅ Display all milestones in Kanban board grouped by status
✅ Display all tasks in sortable/filterable table
✅ Drag milestone cards between columns to update status
✅ Auto-calculate milestone progress based on task completion
✅ Filter by status, priority, department, assignee
✅ Search by task/milestone name
✅ View milestone/task details in modal
✅ Manually add new milestones and tasks
✅ Import milestones/tasks from video transcription
✅ Mark tasks complete with one click
✅ Export tasks as CSV/JSON
✅ Real-time updates via Supabase subscriptions

---

## Future Enhancements (Phase 2)

- **Gantt Chart View**: Timeline visualization with dependencies
- **Time Tracking**: Log actual time spent on tasks
- **Notifications**: Email/push alerts when assigned tasks
- **Comments**: Discussion thread on tasks/milestones
- **Attachments**: Upload files to tasks
- **Templates**: Save milestone templates for reuse
- **Calendar Integration**: Sync tasks to Google Calendar
- **Slack Integration**: Post task updates to Slack channels

---

**Created**: 2025-11-28
**Purpose**: Track actionable milestones and tasks extracted from video transcriptions
**Phase**: Core Feature (Screen 11 of Research Management System)
**Priority**: High
**Department**: AID (AI & Automation) + All Departments
