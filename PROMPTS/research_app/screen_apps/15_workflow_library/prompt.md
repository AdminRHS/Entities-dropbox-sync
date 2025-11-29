## Screen 15: Workflow Library

Build a comprehensive workflow library to browse, search, and manage all extracted workflows from video transcriptions with step-by-step details.

---

## Tech Stack
- React 18 + TypeScript + Vite
- Supabase (database + real-time subscriptions)
- shadcn/ui components
- TanStack Table v8
- Lucide React icons
- Tailwind CSS
- React Flow (optional, for visual workflow diagrams)

---

## Design System

Use the **AdminRHS-AI-Catalog Design System**:

### Colors
```typescript
const COLORS = {
  accentBlue: '#428eb4',
  workflowPrimary: '#F97316', // Orange
  // Complexity Colors
  low: '#34D399',      // Green
  medium: '#FBBF24',   // Yellow
  high: '#F97316',     // Orange
  veryHigh: '#EF4444'  // Red
}
```

---

## Database Schema

Create new `workflows` table for detailed workflow storage:

```sql
CREATE TABLE workflows (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_id TEXT UNIQUE NOT NULL, -- e.g., "WF-001"
  workflow_name TEXT NOT NULL,
  objective TEXT NOT NULL,
  video_id UUID REFERENCES video_queue(id),
  entity_id UUID REFERENCES extracted_entities(id), -- Link to entity if exists
  steps TEXT[] NOT NULL,
  duration TEXT,
  complexity TEXT, -- 'Low', 'Medium', 'High', 'Very High'
  department TEXT,
  tools_used TEXT[],
  input_description TEXT,
  output_description TEXT,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_workflows_complexity ON workflows(complexity);
CREATE INDEX idx_workflows_department ON workflows(department);
CREATE INDEX idx_workflows_video ON workflows(video_id);
```

---

## Layout Structure

```
┌──────────────────────────────────────────────────────────────┐
│  📊 Workflow Library                    [Export] [+ Add New] │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 📊 Total │ │ 🟢 Simple│ │ 🟡 Medium│ │ 🔴 Complex│       │
│  │ 156      │ │ 45       │ │ 78       │ │ 33        │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────────────────────┤
│  [Views: 📋 List | 🎴 Cards | 🔄 Flow Diagram]              │
├──────────────────────────────────────────────────────────────┤
│  Filters: [Complexity ▼] [Dept ▼] [Duration ▼] [🔍 Search] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  CARD VIEW:                                                  │
│  ┌──────────────────────┐ ┌──────────────────────┐         │
│  │ WF-001               │ │ WF-002               │         │
│  │ Email Automation     │ │ CV Screening         │         │
│  │ ────────────────────│ │ ────────────────────│         │
│  │ 🟢 Low Complexity   │ │ 🟡 Medium            │         │
│  │ ⏱ 5-10 min          │ │ ⏱ 10-15 min          │         │
│  │ 📌 5 steps          │ │ 📌 9 steps           │         │
│  │ 🔧 Gmail, Claude    │ │ 🔧 NotebookLM        │         │
│  │ [View Details]      │ │ [View Details]      │         │
│  └──────────────────────┘ └──────────────────────┘         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Features

### 1. Workflow Stats Cards

```tsx
interface WorkflowStats {
  total: number;
  byComplexity: {
    low: number;
    medium: number;
    high: number;
    veryHigh: number;
  };
  byDepartment: Record<string, number>;
  averageDuration: string;
}

function WorkflowStatsCards({ stats }: { stats: WorkflowStats }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Total Workflows</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold">{stats.total}</div>
          <p className="text-xs text-muted-foreground">Extracted from videos</p>
        </CardContent>
      </Card>
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Simple (Low)</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-green-500">
            {stats.byComplexity.low}
          </div>
          <p className="text-xs text-muted-foreground">Easy to implement</p>
        </CardContent>
      </Card>
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Medium</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-yellow-500">
            {stats.byComplexity.medium}
          </div>
          <p className="text-xs text-muted-foreground">Moderate complexity</p>
        </CardContent>
      </Card>
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Complex</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-red-500">
            {stats.byComplexity.high + stats.byComplexity.veryHigh}
          </div>
          <p className="text-xs text-muted-foreground">Advanced workflows</p>
        </CardContent>
      </Card>
    </div>
  );
}
```

### 2. Workflow Card

```tsx
function WorkflowCard({ workflow }: { workflow: Workflow }) {
  return (
    <Card className="hover:shadow-lg transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="space-y-1">
            <Badge variant="outline" className="font-mono text-xs">
              {workflow.workflow_id}
            </Badge>
            <CardTitle className="text-lg">{workflow.workflow_name}</CardTitle>
          </div>
          <Badge style={{ backgroundColor: COMPLEXITY_COLORS[workflow.complexity] }}>
            {workflow.complexity}
          </Badge>
        </div>
        <CardDescription className="line-clamp-2">
          {workflow.objective}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-3">
        <div className="flex items-center gap-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-1">
            <Clock className="h-4 w-4" />
            {workflow.duration || 'N/A'}
          </div>
          <div className="flex items-center gap-1">
            <ListChecks className="h-4 w-4" />
            {workflow.steps?.length || 0} steps
          </div>
        </div>

        {/* Tools Used */}
        {workflow.tools_used && workflow.tools_used.length > 0 && (
          <div>
            <p className="text-xs text-muted-foreground mb-2">Tools:</p>
            <div className="flex flex-wrap gap-1">
              {workflow.tools_used.slice(0, 3).map((tool, i) => (
                <Badge key={i} variant="secondary" className="text-xs">
                  {tool}
                </Badge>
              ))}
              {workflow.tools_used.length > 3 && (
                <Badge variant="outline" className="text-xs">
                  +{workflow.tools_used.length - 3}
                </Badge>
              )}
            </div>
          </div>
        )}

        {/* Department */}
        {workflow.department && (
          <div className="flex items-center gap-2">
            <DepartmentBadge dept={workflow.department} />
          </div>
        )}
      </CardContent>
      <CardFooter className="flex gap-2">
        <Button variant="outline" size="sm" className="flex-1" onClick={() => openWorkflowDetail(workflow)}>
          View Steps
        </Button>
        <Button variant="ghost" size="sm" asChild>
          <Link to={`/videos/${workflow.video_id}`}>
            <ExternalLink className="h-3 w-3" />
          </Link>
        </Button>
      </CardFooter>
    </Card>
  );
}
```

### 3. Workflow Detail Modal

```tsx
function WorkflowDetailModal({ workflow, open, onClose }: WorkflowDetailModalProps) {
  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="font-mono">{workflow.workflow_id}</Badge>
            <DialogTitle>{workflow.workflow_name}</DialogTitle>
          </div>
          <DialogDescription>{workflow.objective}</DialogDescription>
        </DialogHeader>

        <div className="space-y-6">
          {/* Metadata Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div>
              <Label>Complexity</Label>
              <div className="mt-1">
                <Badge style={{ backgroundColor: COMPLEXITY_COLORS[workflow.complexity] }}>
                  {workflow.complexity}
                </Badge>
              </div>
            </div>
            <div>
              <Label>Duration</Label>
              <p className="text-sm mt-1">{workflow.duration || 'Not specified'}</p>
            </div>
            <div>
              <Label>Department</Label>
              <div className="mt-1">
                {workflow.department && <DepartmentBadge dept={workflow.department} />}
              </div>
            </div>
            <div>
              <Label>Steps</Label>
              <p className="text-sm mt-1">{workflow.steps?.length || 0} steps</p>
            </div>
          </div>

          {/* Steps List */}
          <div>
            <Label className="text-base">Workflow Steps</Label>
            <ol className="mt-3 space-y-3">
              {workflow.steps.map((step, index) => (
                <li key={index} className="flex gap-3">
                  <div className="flex-shrink-0 w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-sm font-medium">
                    {index + 1}
                  </div>
                  <div className="flex-1 pt-1">
                    <p className="text-sm">{step}</p>
                  </div>
                </li>
              ))}
            </ol>
          </div>

          {/* Tools Used */}
          {workflow.tools_used && workflow.tools_used.length > 0 && (
            <div>
              <Label>Tools Used</Label>
              <div className="flex flex-wrap gap-2 mt-2">
                {workflow.tools_used.map((tool, i) => (
                  <Badge key={i} variant="secondary">{tool}</Badge>
                ))}
              </div>
            </div>
          )}

          {/* Input/Output */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {workflow.input_description && (
              <div>
                <Label>Input</Label>
                <p className="text-sm mt-1 text-muted-foreground">
                  {workflow.input_description}
                </p>
              </div>
            )}
            {workflow.output_description && (
              <div>
                <Label>Output</Label>
                <p className="text-sm mt-1 text-muted-foreground">
                  {workflow.output_description}
                </p>
              </div>
            )}
          </div>

          {/* Source Video */}
          <div>
            <Label>Source Video</Label>
            <Button variant="outline" size="sm" className="w-full mt-2" asChild>
              <Link to={`/videos/${workflow.video_id}`}>
                View Video Details →
              </Link>
            </Button>
          </div>
        </div>

        <DialogFooter className="flex gap-2">
          <Button variant="outline" onClick={onClose}>Close</Button>
          <Button variant="outline" onClick={() => exportWorkflow(workflow, 'json')}>
            <Download className="h-4 w-4 mr-2" />
            Export JSON
          </Button>
          <Button variant="outline" onClick={() => exportWorkflow(workflow, 'markdown')}>
            <FileText className="h-4 w-4 mr-2" />
            Export Markdown
          </Button>
          <Button onClick={() => createTasksFromWorkflow(workflow)}>
            <Plus className="h-4 w-4 mr-2" />
            Create Tasks
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
```

### 4. Filters

```typescript
interface WorkflowFilters {
  complexity: string | 'all';
  department: string | 'all';
  minSteps: number;
  maxSteps: number;
  toolsUsed: string[];
  search: string;
}

function FilterBar({ filters, onFilterChange }: FilterBarProps) {
  return (
    <div className="flex flex-wrap gap-4 mb-6">
      {/* Complexity Filter */}
      <Select
        value={filters.complexity}
        onValueChange={(v) => onFilterChange({ ...filters, complexity: v })}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="All Complexities" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Complexities</SelectItem>
          <SelectItem value="Low">🟢 Low</SelectItem>
          <SelectItem value="Medium">🟡 Medium</SelectItem>
          <SelectItem value="High">🟠 High</SelectItem>
          <SelectItem value="Very High">🔴 Very High</SelectItem>
        </SelectContent>
      </Select>

      {/* Department Filter */}
      <Select
        value={filters.department}
        onValueChange={(v) => onFilterChange({ ...filters, department: v })}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="All Departments" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Departments</SelectItem>
          <SelectItem value="DEV">DEV - Development</SelectItem>
          <SelectItem value="AID">AID - AI & Automation</SelectItem>
          <SelectItem value="MKT">MKT - Marketing</SelectItem>
          {/* ... more departments */}
        </SelectContent>
      </Select>

      {/* Steps Range */}
      <div className="flex items-center gap-2">
        <Label className="text-sm">Steps:</Label>
        <Input
          type="number"
          placeholder="Min"
          value={filters.minSteps}
          onChange={(e) => onFilterChange({ ...filters, minSteps: parseInt(e.target.value) })}
          className="w-20"
        />
        <span>-</span>
        <Input
          type="number"
          placeholder="Max"
          value={filters.maxSteps}
          onChange={(e) => onFilterChange({ ...filters, maxSteps: parseInt(e.target.value) })}
          className="w-20"
        />
      </div>

      {/* Search */}
      <div className="relative flex-1 min-w-[200px]">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input
          placeholder="Search workflows..."
          value={filters.search}
          onChange={(e) => onFilterChange({ ...filters, search: e.target.value })}
          className="pl-10"
        />
      </div>
    </div>
  );
}
```

### 5. List View (Table)

```typescript
const columns = [
  {
    accessorKey: 'workflow_id',
    header: 'ID',
    cell: ({ getValue }) => (
      <Badge variant="outline" className="font-mono text-xs">
        {getValue()}
      </Badge>
    )
  },
  {
    accessorKey: 'workflow_name',
    header: 'Name',
    cell: ({ row }) => (
      <div className="space-y-1">
        <div className="font-medium">{row.original.workflow_name}</div>
        <div className="text-xs text-muted-foreground line-clamp-1">
          {row.original.objective}
        </div>
      </div>
    )
  },
  {
    accessorKey: 'complexity',
    header: 'Complexity',
    cell: ({ getValue }) => (
      <Badge style={{ backgroundColor: COMPLEXITY_COLORS[getValue()] }}>
        {getValue()}
      </Badge>
    )
  },
  {
    accessorKey: 'duration',
    header: 'Duration',
    cell: ({ getValue }) => (
      <span className="text-sm">{getValue() || 'N/A'}</span>
    )
  },
  {
    accessorKey: 'steps',
    header: 'Steps',
    cell: ({ getValue }) => (
      <span className="text-sm">{(getValue() as string[])?.length || 0}</span>
    )
  },
  {
    id: 'actions',
    header: '',
    cell: ({ row }) => <WorkflowActions workflow={row.original} />
  }
];
```

### 6. Export Workflow

```typescript
function exportWorkflow(workflow: Workflow, format: 'json' | 'markdown') {
  if (format === 'json') {
    const json = JSON.stringify(workflow, null, 2);
    downloadFile(json, `${workflow.workflow_id}.json`, 'application/json');
  } else if (format === 'markdown') {
    const md = `# ${workflow.workflow_name}

**ID**: ${workflow.workflow_id}
**Objective**: ${workflow.objective}
**Complexity**: ${workflow.complexity}
**Duration**: ${workflow.duration}
**Department**: ${workflow.department}

## Steps

${workflow.steps.map((step, i) => `${i + 1}. ${step}`).join('\n')}

## Tools Used

${workflow.tools_used.map(tool => `- ${tool}`).join('\n')}

## Input

${workflow.input_description}

## Output

${workflow.output_description}
`;
    downloadFile(md, `${workflow.workflow_id}.md`, 'text/markdown');
  }
}
```

### 7. Create Tasks from Workflow

```typescript
async function createTasksFromWorkflow(workflow: Workflow) {
  // Create a milestone first
  const { data: milestone, error: milestoneError } = await supabase
    .from('milestones')
    .insert({
      milestone_id: `MLS-${Date.now()}`,
      milestone_name: workflow.workflow_name,
      objective: workflow.objective,
      video_id: workflow.video_id,
      duration: workflow.duration,
      complexity: workflow.complexity,
      department: workflow.department,
      related_tasks: []
    })
    .select()
    .single();

  if (milestoneError) {
    toast.error('Failed to create milestone');
    return;
  }

  // Create tasks for each step
  const tasks = workflow.steps.map((step, index) => ({
    task_id: `TSK-${Date.now()}-${index}`,
    task_name: step.substring(0, 100), // Truncate if too long
    description: step,
    milestone_id: milestone.id,
    video_id: workflow.video_id,
    status: 'pending',
    priority: 'medium',
    department: workflow.department
  }));

  const { error: tasksError } = await supabase
    .from('tasks')
    .insert(tasks);

  if (!tasksError) {
    toast.success(`Created milestone and ${tasks.length} tasks`);
    navigate('/tasks');
  }
}
```

---

## View Modes

```tsx
const [viewMode, setViewMode] = useState<'list' | 'cards'>('cards');

<div className="flex items-center gap-2">
  <Button
    variant={viewMode === 'list' ? 'default' : 'outline'}
    size="sm"
    onClick={() => setViewMode('list')}
  >
    <List className="h-4 w-4" />
  </Button>
  <Button
    variant={viewMode === 'cards' ? 'default' : 'outline'}
    size="sm"
    onClick={() => setViewMode('cards')}
  >
    <LayoutGrid className="h-4 w-4" />
  </Button>
</div>
```

---

## Success Criteria

✅ Display all workflows from `workflows` table
✅ Filter by complexity, department, steps, tools
✅ Search by workflow name or objective
✅ Toggle between list and card view
✅ Workflow detail modal with all steps
✅ Export workflow as JSON or Markdown
✅ Create tasks/milestones from workflow
✅ Real-time updates when workflows are added
✅ Link to source video
✅ Stats cards showing complexity breakdown
✅ Responsive grid layout

---

**Created**: 2025-11-28
**Purpose**: Browse and manage workflow library
**Phase**: Core Feature (Screen 15 of Research Management System)
**Priority**: High
**Department**: All Departments
