# Screen 12: Video Catalog & Library

Build a comprehensive video library interface to view, search, filter, and manage all imported videos with phase tracking.

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
  phase0: '#9CA3AF',  // Gray - Phase 0: Search
  phase1: '#60A5FA',  // Blue - Phase 1: Transcription
  phase2: '#34D399',  // Green - Phase 2: Entity Extraction
  phase3: '#FBBF24',  // Yellow - Phase 3: Gap Analysis
  phase4: '#F97316',  // Orange - Phase 4: Integration
  phase5: '#A78BFA',  // Purple - Phase 5: Knowledge Mapping
  complete: '#10B981', // Emerald - Phase 6: Complete

  // Priority
  low: '#9CA3AF',
  medium: '#FBBF24',
  high: '#F97316',
  critical: '#EF4444'
}
```

---

## Database Schema

Uses existing `video_queue` table from Screen 01:

```sql
-- Reference: video_queue table structure
CREATE TABLE video_queue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_url TEXT NOT NULL,
  video_title TEXT NOT NULL,
  channel_name TEXT,
  duration_minutes INTEGER,
  priority TEXT DEFAULT 'medium', -- low, medium, high, critical
  department TEXT, -- DEV, SMM, VID, AID, DGN, MKT
  assigned_to TEXT,
  notes TEXT,
  status TEXT DEFAULT 'selected', -- selected, transcription_uploaded, entities_extracted, etc.
  phase INTEGER DEFAULT 0, -- 0-6
  transcription_id UUID REFERENCES transcriptions(id),
  perplexity_search_id TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add indexes for filtering
CREATE INDEX idx_video_phase ON video_queue(phase);
CREATE INDEX idx_video_department ON video_queue(department);
CREATE INDEX idx_video_priority ON video_queue(priority);
CREATE INDEX idx_video_status ON video_queue(status);
CREATE INDEX idx_video_channel ON video_queue(channel_name);
```

### New: Video Metadata Table (for extended info)
```sql
CREATE TABLE video_metadata (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_id UUID REFERENCES video_queue(id) ON DELETE CASCADE,
  thumbnail_url TEXT,
  publication_date DATE,
  view_count INTEGER,
  tags TEXT[],
  key_topics TEXT[],
  tools_mentioned TEXT[],
  workflows_count INTEGER DEFAULT 0,
  entities_count INTEGER DEFAULT 0,
  milestones_count INTEGER DEFAULT 0,
  tasks_count INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Layout Structure

```
┌──────────────────────────────────────────────────────────────┐
│  🎬 Video Catalog                              [+ Add Video] │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 📊 Total │ │ 🔵 Phase1│ │ 🟢 Phase2│ │ ✅ Done  │       │
│  │ 42 videos│ │ 12 videos│ │ 8 videos │ │ 6 videos │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────────────────────┤
│  [Views: 📊 Table | 🎴 Cards | 📈 Timeline]                 │
├──────────────────────────────────────────────────────────────┤
│  Filters: [Phase ▼] [Dept ▼] [Priority ▼] [Status ▼] [🔍] │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  TABLE VIEW:                                                 │
│  ┌────┬─────────────┬────────┬───────┬───────┬──────────┐  │
│  │ #  │ Title       │ Channel│ Dept  │ Phase │ Actions  │  │
│  ├────┼─────────────┼────────┼───────┼───────┼──────────┤  │
│  │ 🔵 │ Claude Code │ CCGG   │ AID   │ [█░░] │ [⋮]     │  │
│  │    │ for Business│        │       │ 1/6   │          │  │
│  ├────┼─────────────┼────────┼───────┼───────┼──────────┤  │
│  │ 🟢 │ Lead Gen    │ Nick S │ MKT   │ [███]│ [⋮]     │  │
│  │    │ Masterclass │        │       │ 2/6   │          │  │
│  └────┴─────────────┴────────┴───────┴───────┴──────────┘  │
│                                                              │
│  [← Prev] Page 1 of 3 [Next →]                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## View Modes

### 1. Table View (Default)
TanStack Table with columns:

```typescript
const columns = [
  {
    id: 'phase_indicator',
    header: '',
    cell: ({ row }) => <PhaseIndicator phase={row.original.phase} />
  },
  {
    accessorKey: 'video_title',
    header: 'Title',
    cell: ({ row }) => (
      <div className="space-y-1">
        <div className="font-medium">{row.original.video_title}</div>
        <div className="text-sm text-muted-foreground">
          {row.original.duration_minutes} min • {row.original.channel_name}
        </div>
      </div>
    )
  },
  {
    accessorKey: 'department',
    header: 'Dept',
    cell: ({ getValue }) => <DepartmentBadge dept={getValue()} />
  },
  {
    accessorKey: 'priority',
    header: 'Priority',
    cell: ({ getValue }) => <PriorityBadge priority={getValue()} />
  },
  {
    accessorKey: 'phase',
    header: 'Progress',
    cell: ({ row }) => <PhaseProgress phase={row.original.phase} />
  },
  {
    accessorKey: 'assigned_to',
    header: 'Assignee',
    cell: ({ getValue }) => <UserAvatar email={getValue()} />
  },
  {
    id: 'actions',
    header: '',
    cell: ({ row }) => <VideoActions video={row.original} />
  }
];
```

**PhaseIndicator**: Colored dot/icon showing current phase
- Phase 0: Gray circle
- Phase 1: Blue circle
- Phase 2: Green circle
- Phase 3: Yellow circle
- Phase 4: Orange circle
- Phase 5: Purple circle
- Phase 6: Green checkmark

**PhaseProgress**: Visual progress bar
```typescript
function PhaseProgress({ phase }: { phase: number }) {
  const progress = (phase / 6) * 100;
  return (
    <div className="flex items-center gap-2">
      <div className="w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
        <div
          className="h-full transition-all"
          style={{
            width: `${progress}%`,
            backgroundColor: PHASE_COLORS[phase]
          }}
        />
      </div>
      <span className="text-sm text-muted-foreground">{phase}/6</span>
    </div>
  );
}
```

**VideoActions**: Dropdown menu
- View Details
- Upload Transcription
- Extract Entities
- View Milestones/Tasks
- Edit
- Delete

### 2. Card View
Grid layout with video cards:

```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
  {videos.map(video => (
    <VideoCard key={video.id} video={video} />
  ))}
</div>

// VideoCard component
function VideoCard({ video }: { video: Video }) {
  return (
    <Card className="overflow-hidden hover:shadow-lg transition-shadow">
      <div className="aspect-video bg-gray-100 relative">
        {video.thumbnail_url ? (
          <img src={video.thumbnail_url} alt={video.video_title} />
        ) : (
          <div className="flex items-center justify-center h-full">
            <PlayCircle className="w-12 h-12 text-gray-400" />
          </div>
        )}
        <Badge
          className="absolute top-2 right-2"
          style={{ backgroundColor: PHASE_COLORS[video.phase] }}
        >
          Phase {video.phase}
        </Badge>
      </div>
      <CardHeader>
        <CardTitle className="text-sm line-clamp-2">
          {video.video_title}
        </CardTitle>
        <CardDescription>
          {video.channel_name} • {video.duration_minutes} min
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-2">
        <div className="flex gap-2">
          <DepartmentBadge dept={video.department} />
          <PriorityBadge priority={video.priority} />
        </div>
        <PhaseProgress phase={video.phase} />
      </CardContent>
      <CardFooter>
        <Button variant="outline" size="sm" className="w-full">
          View Details
        </Button>
      </CardFooter>
    </Card>
  );
}
```

### 3. Timeline View
Horizontal timeline showing videos by date added or publication date:

```
Phase 0          Phase 1          Phase 2
────●────────────●────────────────●────────────────→
    │            │                │
 [Video A]   [Video B]        [Video C]
 Nov 25      Nov 26           Nov 27
```

Use a library like `vis-timeline` or build custom with CSS.

---

## Stats Cards

Top row showing aggregate statistics:

```typescript
interface StatsCard {
  label: string;
  value: number;
  icon: LucideIcon;
  color: string;
  description?: string;
}

const stats: StatsCard[] = [
  {
    label: 'Total Videos',
    value: videos.length,
    icon: PlayCircle,
    color: COLORS.accentBlue,
    description: 'In library'
  },
  {
    label: 'Phase 1 (Transcription)',
    value: videos.filter(v => v.phase === 1).length,
    icon: FileText,
    color: COLORS.phase1,
    description: 'Awaiting transcription'
  },
  {
    label: 'Phase 2 (Extraction)',
    value: videos.filter(v => v.phase === 2).length,
    icon: Database,
    color: COLORS.phase2,
    description: 'Processing entities'
  },
  {
    label: 'Completed',
    value: videos.filter(v => v.phase === 6).length,
    icon: CheckCircle2,
    color: COLORS.complete,
    description: 'Fully processed'
  }
];
```

Render as:
```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
  {stats.map((stat, i) => (
    <Card key={i}>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium">
          {stat.label}
        </CardTitle>
        <stat.icon className="h-4 w-4" style={{ color: stat.color }} />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{stat.value}</div>
        {stat.description && (
          <p className="text-xs text-muted-foreground">
            {stat.description}
          </p>
        )}
      </CardContent>
    </Card>
  ))}
</div>
```

---

## Filters & Search

```typescript
interface VideoFilters {
  phase: number | 'all';
  department: Department | 'all';
  priority: Priority | 'all';
  status: string | 'all';
  channel: string | 'all';
  assignee: string | 'all' | 'unassigned';
  dateRange: { from: Date; to: Date } | null;
  search: string;
}

function FilterBar({ filters, onFilterChange }: FilterBarProps) {
  return (
    <div className="flex flex-wrap gap-4 mb-6">
      {/* Phase Filter */}
      <Select
        value={filters.phase.toString()}
        onValueChange={(v) => onFilterChange({ ...filters, phase: v === 'all' ? 'all' : parseInt(v) })}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="All Phases" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Phases</SelectItem>
          <SelectItem value="0">Phase 0 - Search</SelectItem>
          <SelectItem value="1">Phase 1 - Transcription</SelectItem>
          <SelectItem value="2">Phase 2 - Extraction</SelectItem>
          <SelectItem value="3">Phase 3 - Gap Analysis</SelectItem>
          <SelectItem value="4">Phase 4 - Integration</SelectItem>
          <SelectItem value="5">Phase 5 - Mapping</SelectItem>
          <SelectItem value="6">Phase 6 - Complete</SelectItem>
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
          <SelectItem value="SMM">SMM - Social Media</SelectItem>
          <SelectItem value="VID">VID - Video Production</SelectItem>
          <SelectItem value="DGN">DGN - Design</SelectItem>
        </SelectContent>
      </Select>

      {/* Priority Filter */}
      <Select
        value={filters.priority}
        onValueChange={(v) => onFilterChange({ ...filters, priority: v })}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="All Priorities" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Priorities</SelectItem>
          <SelectItem value="low">Low</SelectItem>
          <SelectItem value="medium">Medium</SelectItem>
          <SelectItem value="high">High</SelectItem>
          <SelectItem value="critical">Critical</SelectItem>
        </SelectContent>
      </Select>

      {/* Channel Filter */}
      <Select
        value={filters.channel}
        onValueChange={(v) => onFilterChange({ ...filters, channel: v })}
      >
        <SelectTrigger className="w-[200px]">
          <SelectValue placeholder="All Channels" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Channels</SelectItem>
          {uniqueChannels.map(channel => (
            <SelectItem key={channel} value={channel}>
              {channel}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>

      {/* Search */}
      <div className="relative flex-1 min-w-[200px]">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input
          placeholder="Search videos..."
          value={filters.search}
          onChange={(e) => onFilterChange({ ...filters, search: e.target.value })}
          className="pl-10"
        />
      </div>

      {/* Clear Filters */}
      {Object.values(filters).some(v => v !== 'all' && v !== '') && (
        <Button
          variant="ghost"
          onClick={() => onFilterChange(DEFAULT_FILTERS)}
        >
          <X className="h-4 w-4 mr-2" />
          Clear Filters
        </Button>
      )}
    </div>
  );
}
```

---

## Video Detail Modal

Click "View Details" or click a row/card:

```tsx
function VideoDetailModal({ video, open, onClose }: VideoDetailModalProps) {
  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>{video.video_title}</DialogTitle>
          <DialogDescription>
            {video.channel_name} • {video.duration_minutes} minutes
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-6">
          {/* Video Thumbnail/Embed */}
          <div className="aspect-video bg-gray-100 rounded-lg overflow-hidden">
            {video.video_url && (
              <iframe
                src={getEmbedUrl(video.video_url)}
                className="w-full h-full"
                allowFullScreen
              />
            )}
          </div>

          {/* Metadata Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div>
              <Label>Phase</Label>
              <div className="flex items-center gap-2 mt-1">
                <PhaseIndicator phase={video.phase} />
                <span className="font-medium">Phase {video.phase}</span>
              </div>
            </div>
            <div>
              <Label>Department</Label>
              <div className="mt-1">
                <DepartmentBadge dept={video.department} />
              </div>
            </div>
            <div>
              <Label>Priority</Label>
              <div className="mt-1">
                <PriorityBadge priority={video.priority} />
              </div>
            </div>
            <div>
              <Label>Assignee</Label>
              <div className="mt-1">
                {video.assigned_to || <span className="text-muted-foreground">Unassigned</span>}
              </div>
            </div>
          </div>

          {/* Progress Tracker */}
          <div>
            <Label>Processing Progress</Label>
            <PhaseProgressBar video={video} />
          </div>

          {/* Key Topics */}
          {video.metadata?.key_topics && (
            <div>
              <Label>Key Topics</Label>
              <div className="flex flex-wrap gap-2 mt-2">
                {video.metadata.key_topics.map((topic, i) => (
                  <Badge key={i} variant="outline">{topic}</Badge>
                ))}
              </div>
            </div>
          )}

          {/* Tools Mentioned */}
          {video.metadata?.tools_mentioned && (
            <div>
              <Label>Tools Mentioned</Label>
              <div className="flex flex-wrap gap-2 mt-2">
                {video.metadata.tools_mentioned.map((tool, i) => (
                  <Badge key={i} variant="secondary">{tool}</Badge>
                ))}
              </div>
            </div>
          )}

          {/* Entity Counts */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-4 bg-muted rounded-lg">
            <div className="text-center">
              <div className="text-2xl font-bold">{video.metadata?.workflows_count || 0}</div>
              <div className="text-sm text-muted-foreground">Workflows</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold">{video.metadata?.entities_count || 0}</div>
              <div className="text-sm text-muted-foreground">Entities</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold">{video.metadata?.milestones_count || 0}</div>
              <div className="text-sm text-muted-foreground">Milestones</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold">{video.metadata?.tasks_count || 0}</div>
              <div className="text-sm text-muted-foreground">Tasks</div>
            </div>
          </div>

          {/* Notes */}
          {video.notes && (
            <div>
              <Label>Notes</Label>
              <p className="mt-1 text-sm text-muted-foreground">{video.notes}</p>
            </div>
          )}

          {/* Quick Actions */}
          <div className="flex gap-2">
            <Button asChild>
              <a href={video.video_url} target="_blank" rel="noopener noreferrer">
                <ExternalLink className="h-4 w-4 mr-2" />
                Watch on YouTube
              </a>
            </Button>
            {video.phase === 0 && (
              <Button variant="outline" onClick={() => navigateToTranscriptionUpload(video.id)}>
                <Upload className="h-4 w-4 mr-2" />
                Upload Transcription
              </Button>
            )}
            {video.phase === 1 && (
              <Button variant="outline" onClick={() => navigateToEntityExtraction(video.id)}>
                <Database className="h-4 w-4 mr-2" />
                Extract Entities
              </Button>
            )}
            {video.metadata?.milestones_count > 0 && (
              <Button variant="outline" onClick={() => navigateToMilestones(video.id)}>
                <ListChecks className="h-4 w-4 mr-2" />
                View Tasks ({video.metadata.milestones_count})
              </Button>
            )}
          </div>
        </div>

        <DialogFooter>
          <Button variant="outline" onClick={onClose}>Close</Button>
          <Button onClick={() => navigateToEdit(video.id)}>
            <Edit className="h-4 w-4 mr-2" />
            Edit Video
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
```

---

## Phase Progress Bar (Detailed)

Visual stepper showing all phases with completion status:

```tsx
function PhaseProgressBar({ video }: { video: Video }) {
  const phases = [
    { number: 0, label: 'Search', color: COLORS.phase0 },
    { number: 1, label: 'Transcription', color: COLORS.phase1 },
    { number: 2, label: 'Extraction', color: COLORS.phase2 },
    { number: 3, label: 'Gap Analysis', color: COLORS.phase3 },
    { number: 4, label: 'Integration', color: COLORS.phase4 },
    { number: 5, label: 'Mapping', color: COLORS.phase5 },
    { number: 6, label: 'Complete', color: COLORS.complete }
  ];

  return (
    <div className="flex items-center gap-2 mt-2">
      {phases.map((phase, index) => (
        <React.Fragment key={phase.number}>
          <div className="flex flex-col items-center">
            <div
              className={cn(
                "w-8 h-8 rounded-full flex items-center justify-center font-medium text-sm transition-all",
                video.phase >= phase.number
                  ? "ring-2 ring-offset-2"
                  : "bg-gray-200 text-gray-500"
              )}
              style={{
                backgroundColor: video.phase >= phase.number ? phase.color : undefined,
                color: video.phase >= phase.number ? 'white' : undefined,
                ringColor: video.phase === phase.number ? phase.color : undefined
              }}
            >
              {video.phase > phase.number ? (
                <Check className="h-4 w-4" />
              ) : (
                phase.number
              )}
            </div>
            <span className="text-xs mt-1 text-center">{phase.label}</span>
          </div>
          {index < phases.length - 1 && (
            <div
              className="flex-1 h-0.5 -mt-6"
              style={{
                backgroundColor: video.phase > phase.number ? phase.color : '#E5E7EB'
              }}
            />
          )}
        </React.Fragment>
      ))}
    </div>
  );
}
```

---

## Bulk Actions

Select multiple videos for batch operations:

```tsx
function BulkActionsBar({ selectedVideos, onAction }: BulkActionsBarProps) {
  if (selectedVideos.length === 0) return null;

  return (
    <div className="fixed bottom-4 left-1/2 -translate-x-1/2 bg-background border shadow-lg rounded-lg p-4 flex items-center gap-4 z-50">
      <span className="text-sm font-medium">
        {selectedVideos.length} video{selectedVideos.length > 1 ? 's' : ''} selected
      </span>
      <Separator orientation="vertical" className="h-6" />
      <Button
        variant="outline"
        size="sm"
        onClick={() => onAction('assign')}
      >
        <UserPlus className="h-4 w-4 mr-2" />
        Assign
      </Button>
      <Button
        variant="outline"
        size="sm"
        onClick={() => onAction('change-priority')}
      >
        <AlertCircle className="h-4 w-4 mr-2" />
        Change Priority
      </Button>
      <Button
        variant="outline"
        size="sm"
        onClick={() => onAction('change-department')}
      >
        <Building className="h-4 w-4 mr-2" />
        Change Department
      </Button>
      <Button
        variant="outline"
        size="sm"
        onClick={() => onAction('export')}
      >
        <Download className="h-4 w-4 mr-2" />
        Export
      </Button>
      <Separator orientation="vertical" className="h-6" />
      <Button
        variant="ghost"
        size="sm"
        onClick={() => onAction('clear')}
      >
        <X className="h-4 w-4" />
      </Button>
    </div>
  );
}
```

---

## Sorting & Pagination

```typescript
// TanStack Table state
const [sorting, setSorting] = useState<SortingState>([
  { id: 'created_at', desc: true } // Default: newest first
]);

const [pagination, setPagination] = useState({
  pageIndex: 0,
  pageSize: 20
});

// Apply to query
const { data, isLoading } = useQuery({
  queryKey: ['videos', filters, sorting, pagination],
  queryFn: async () => {
    let query = supabase
      .from('video_queue')
      .select('*, metadata:video_metadata(*)', { count: 'exact' });

    // Apply filters
    if (filters.phase !== 'all') query = query.eq('phase', filters.phase);
    if (filters.department !== 'all') query = query.eq('department', filters.department);
    // ... more filters

    // Apply sorting
    if (sorting.length > 0) {
      query = query.order(sorting[0].id, { ascending: !sorting[0].desc });
    }

    // Apply pagination
    const from = pagination.pageIndex * pagination.pageSize;
    const to = from + pagination.pageSize - 1;
    query = query.range(from, to);

    return query;
  }
});
```

---

## Real-time Updates

Subscribe to video_queue changes:

```typescript
useEffect(() => {
  const channel = supabase
    .channel('video-catalog-changes')
    .on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'video_queue'
      },
      (payload) => {
        queryClient.invalidateQueries(['videos']);

        toast({
          title: payload.eventType === 'INSERT' ? 'New video added' : 'Video updated',
          description: payload.new?.video_title
        });
      }
    )
    .subscribe();

  return () => {
    supabase.removeChannel(channel);
  };
}, []);
```

---

## Export Functionality

Export filtered/selected videos:

```typescript
async function exportVideos(videos: Video[], format: 'csv' | 'json' | 'markdown') {
  if (format === 'csv') {
    const csv = Papa.unparse(videos.map(v => ({
      'Video URL': v.video_url,
      'Title': v.video_title,
      'Channel': v.channel_name,
      'Duration (min)': v.duration_minutes,
      'Department': v.department,
      'Priority': v.priority,
      'Phase': v.phase,
      'Status': v.status,
      'Assignee': v.assigned_to,
      'Notes': v.notes
    })));
    downloadFile(csv, 'videos.csv', 'text/csv');
  } else if (format === 'json') {
    const json = JSON.stringify(videos, null, 2);
    downloadFile(json, 'videos.json', 'application/json');
  } else if (format === 'markdown') {
    const md = `# Video Catalog Export\n\n${videos.map(v =>
      `## ${v.video_title}\n- **Channel**: ${v.channel_name}\n- **URL**: ${v.video_url}\n- **Phase**: ${v.phase}/6\n- **Department**: ${v.department}\n\n`
    ).join('')}`;
    downloadFile(md, 'videos.md', 'text/markdown');
  }
}
```

---

## Responsive Design

- **Desktop** (>1024px): Full table with all columns
- **Tablet** (768-1024px): Condensed table, hide less important columns
- **Mobile** (<768px): Switch to card view automatically

---

## Success Criteria

✅ Display all videos in sortable/filterable table
✅ Switch between table, card, and timeline views
✅ Filter by phase, department, priority, status, channel
✅ Search by video title or channel name
✅ View detailed video information in modal
✅ Track phase progression visually (0-6)
✅ Bulk select and perform batch actions
✅ Export videos as CSV/JSON/Markdown
✅ Real-time updates when videos are added/updated
✅ Navigate to related screens (transcription upload, entity extraction, tasks)
✅ Embed YouTube videos in detail modal
✅ Display entity counts (workflows, milestones, tasks)

---

**Created**: 2025-11-28
**Purpose**: Comprehensive video library and catalog management
**Phase**: Core Feature (Screen 12 of Research Management System)
**Priority**: High
**Department**: All Departments
