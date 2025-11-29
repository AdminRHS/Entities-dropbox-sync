## Screen 14: Entity Browser

Build a comprehensive entity browsing interface to explore all extracted tools, workflows, skills, and other entities from video transcriptions.

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
  accentBlue: '#428eb4',
  // Entity Type Colors
  tool: '#60A5FA',      // Blue
  workflow: '#F97316',  // Orange
  skill: '#34D399',     // Green
  responsibility: '#A78BFA', // Purple
  profession: '#FBBF24' // Yellow
}
```

---

## Database Schema

Uses existing `extracted_entities` table:

```sql
CREATE TABLE extracted_entities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  video_id UUID REFERENCES video_queue(id),
  entity_type TEXT NOT NULL, -- 'TOOL', 'WORKFLOW', 'SKILL', etc.
  entity_name TEXT NOT NULL,
  entity_id TEXT, -- e.g., 'TOOL-AI-224', 'SKL-042'
  classification TEXT, -- 'NEW', 'EXISTING', 'UPDATED'
  category TEXT,
  confidence_score DECIMAL,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Layout Structure

```
┌──────────────────────────────────────────────────────────────┐
│  🔍 Entity Browser                      [Export] [+ Add New] │
├──────────────────────────────────────────────────────────────┤
│  [Tabs: All | 🔧 Tools | 📊 Workflows | 💡 Skills | ...]    │
├──────────────────────────────────────────────────────────────┤
│  Filters: [Type ▼] [Classification ▼] [Category ▼] [🔍]     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  TABLE VIEW:                                                 │
│  ┌────┬──────────┬────────┬───────┬───────────┬──────────┐ │
│  │ ID │ Name     │ Type   │ Class │ Confidence│ Actions  │ │
│  ├────┼──────────┼────────┼───────┼───────────┼──────────┤ │
│  │TOOL│ Claude   │ Tool   │ NEW   │ 95%       │ [⋮]     │ │
│  │-001│ Code     │        │       │           │          │ │
│  ├────┼──────────┼────────┼───────┼───────────┼──────────┤ │
│  │WF- │ Email    │Workflow│EXISTING│ 88%      │ [⋮]     │ │
│  │023 │ Auto     │        │       │           │          │ │
│  └────┴──────────┴────────┴───────┴───────────┴──────────┘ │
│                                                              │
│  [← Prev] Page 1 of 12 [Next →]                             │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Features

### 1. Tabbed Navigation by Entity Type

```typescript
const entityTabs = [
  { value: 'all', label: 'All Entities', icon: Grid3x3, count: entityCounts?.total },
  { value: 'tool', label: 'Tools', icon: Wrench, count: entityCounts?.tools },
  { value: 'workflow', label: 'Workflows', icon: GitBranch, count: entityCounts?.workflows },
  { value: 'skill', label: 'Skills', icon: Lightbulb, count: entityCounts?.skills },
  { value: 'responsibility', label: 'Responsibilities', icon: ClipboardList, count: entityCounts?.responsibilities },
  { value: 'profession', label: 'Professions', icon: Briefcase, count: entityCounts?.professions }
];
```

### 2. Entity Table (TanStack Table)

```typescript
const columns = [
  {
    accessorKey: 'entity_id',
    header: 'ID',
    cell: ({ getValue }) => (
      <Badge variant="outline" className="font-mono text-xs">
        {getValue()}
      </Badge>
    )
  },
  {
    accessorKey: 'entity_name',
    header: 'Name',
    cell: ({ row }) => (
      <div className="space-y-1">
        <div className="font-medium">{row.original.entity_name}</div>
        {row.original.category && (
          <div className="text-xs text-muted-foreground">{row.original.category}</div>
        )}
      </div>
    )
  },
  {
    accessorKey: 'entity_type',
    header: 'Type',
    cell: ({ getValue }) => (
      <Badge style={{ backgroundColor: ENTITY_TYPE_COLORS[getValue()] }}>
        {getValue()}
      </Badge>
    )
  },
  {
    accessorKey: 'classification',
    header: 'Classification',
    cell: ({ getValue }) => (
      <Badge variant={
        getValue() === 'NEW' ? 'default' :
        getValue() === 'EXISTING' ? 'secondary' :
        'outline'
      }>
        {getValue()}
      </Badge>
    )
  },
  {
    accessorKey: 'confidence_score',
    header: 'Confidence',
    cell: ({ getValue }) => {
      const score = getValue() as number;
      return (
        <div className="flex items-center gap-2">
          <div className="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-green-500"
              style={{ width: `${score * 100}%` }}
            />
          </div>
          <span className="text-xs">{Math.round(score * 100)}%</span>
        </div>
      );
    }
  },
  {
    accessorKey: 'video_id',
    header: 'Source',
    cell: ({ row }) => (
      <Button variant="ghost" size="sm" asChild>
        <Link to={`/videos/${row.original.video_id}`}>
          <ExternalLink className="h-3 w-3" />
        </Link>
      </Button>
    )
  },
  {
    id: 'actions',
    header: '',
    cell: ({ row }) => <EntityActions entity={row.original} />
  }
];
```

### 3. Entity Detail Modal

```tsx
function EntityDetailModal({ entity, open, onClose }: EntityDetailModalProps) {
  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <div className="flex items-center gap-2">
            <Badge style={{ backgroundColor: ENTITY_TYPE_COLORS[entity.entity_type] }}>
              {entity.entity_type}
            </Badge>
            <DialogTitle>{entity.entity_name}</DialogTitle>
          </div>
          <DialogDescription>
            {entity.entity_id} • Confidence: {Math.round(entity.confidence_score * 100)}%
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-4">
          {/* Classification */}
          <div>
            <Label>Classification</Label>
            <div className="mt-1">
              <Badge>{entity.classification}</Badge>
            </div>
          </div>

          {/* Category */}
          {entity.category && (
            <div>
              <Label>Category</Label>
              <p className="text-sm mt-1">{entity.category}</p>
            </div>
          )}

          {/* Metadata */}
          {entity.metadata && (
            <div>
              <Label>Metadata</Label>
              <div className="mt-2 space-y-2">
                {Object.entries(entity.metadata).map(([key, value]) => (
                  <div key={key} className="flex justify-between text-sm">
                    <span className="text-muted-foreground capitalize">
                      {key.replace(/_/g, ' ')}:
                    </span>
                    <span className="font-medium">{String(value)}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Source Video */}
          <div>
            <Label>Source Video</Label>
            <Button variant="outline" size="sm" className="w-full mt-2" asChild>
              <Link to={`/videos/${entity.video_id}`}>
                View Video Details →
              </Link>
            </Button>
          </div>
        </div>

        <DialogFooter>
          <Button variant="outline" onClick={onClose}>Close</Button>
          <Button onClick={() => navigateToEdit(entity.id)}>
            <Edit className="h-4 w-4 mr-2" />
            Edit Entity
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
```

### 4. Filters

```typescript
interface EntityFilters {
  type: string | 'all';
  classification: string | 'all';
  category: string | 'all';
  videoSource: string | 'all';
  confidenceMin: number;
  search: string;
}

function FilterBar({ filters, onFilterChange }: FilterBarProps) {
  return (
    <div className="flex flex-wrap gap-4 mb-6">
      {/* Entity Type (handled by tabs) */}

      {/* Classification Filter */}
      <Select
        value={filters.classification}
        onValueChange={(v) => onFilterChange({ ...filters, classification: v })}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue placeholder="All Classifications" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Classifications</SelectItem>
          <SelectItem value="NEW">New</SelectItem>
          <SelectItem value="EXISTING">Existing</SelectItem>
          <SelectItem value="UPDATED">Updated</SelectItem>
        </SelectContent>
      </Select>

      {/* Category Filter (dynamic based on entity type) */}
      <Select
        value={filters.category}
        onValueChange={(v) => onFilterChange({ ...filters, category: v })}
      >
        <SelectTrigger className="w-[200px]">
          <SelectValue placeholder="All Categories" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">All Categories</SelectItem>
          {uniqueCategories.map(cat => (
            <SelectItem key={cat} value={cat}>{cat}</SelectItem>
          ))}
        </SelectContent>
      </Select>

      {/* Confidence Threshold */}
      <div className="flex items-center gap-2">
        <Label className="text-sm">Min Confidence:</Label>
        <Slider
          value={[filters.confidenceMin]}
          onValueChange={([v]) => onFilterChange({ ...filters, confidenceMin: v })}
          max={100}
          step={5}
          className="w-32"
        />
        <span className="text-sm text-muted-foreground w-12">
          {filters.confidenceMin}%
        </span>
      </div>

      {/* Search */}
      <div className="relative flex-1 min-w-[200px]">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
        <Input
          placeholder="Search entities..."
          value={filters.search}
          onChange={(e) => onFilterChange({ ...filters, search: e.target.value })}
          className="pl-10"
        />
      </div>
    </div>
  );
}
```

### 5. Export Functionality

```typescript
function exportEntities(entities: Entity[], format: 'csv' | 'json') {
  if (format === 'csv') {
    const csv = Papa.unparse(entities.map(e => ({
      'Entity ID': e.entity_id,
      'Name': e.entity_name,
      'Type': e.entity_type,
      'Classification': e.classification,
      'Category': e.category,
      'Confidence': Math.round(e.confidence_score * 100) + '%',
      'Metadata': JSON.stringify(e.metadata)
    })));
    downloadFile(csv, `entities_${new Date().toISOString()}.csv`, 'text/csv');
  } else {
    const json = JSON.stringify(entities, null, 2);
    downloadFile(json, `entities_${new Date().toISOString()}.json`, 'application/json');
  }
}
```

### 6. Card View (Alternative to Table)

```tsx
function EntityCard({ entity }: { entity: Entity }) {
  return (
    <Card className="hover:shadow-lg transition-shadow">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="space-y-1">
            <CardTitle className="text-lg">{entity.entity_name}</CardTitle>
            <CardDescription>{entity.entity_id}</CardDescription>
          </div>
          <Badge style={{ backgroundColor: ENTITY_TYPE_COLORS[entity.entity_type] }}>
            {entity.entity_type}
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-2">
        <div className="flex items-center justify-between text-sm">
          <span className="text-muted-foreground">Classification:</span>
          <Badge variant="outline">{entity.classification}</Badge>
        </div>
        {entity.category && (
          <div className="flex items-center justify-between text-sm">
            <span className="text-muted-foreground">Category:</span>
            <span>{entity.category}</span>
          </div>
        )}
        <div className="flex items-center justify-between text-sm">
          <span className="text-muted-foreground">Confidence:</span>
          <div className="flex items-center gap-2">
            <div className="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
              <div
                className="h-full bg-green-500"
                style={{ width: `${entity.confidence_score * 100}%` }}
              />
            </div>
            <span>{Math.round(entity.confidence_score * 100)}%</span>
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex gap-2">
        <Button variant="outline" size="sm" className="flex-1" onClick={() => openDetailModal(entity)}>
          View Details
        </Button>
        <Button variant="ghost" size="sm" asChild>
          <Link to={`/videos/${entity.video_id}`}>
            <ExternalLink className="h-3 w-3" />
          </Link>
        </Button>
      </CardFooter>
    </Card>
  );
}
```

---

## Real-Time Updates

```typescript
useEffect(() => {
  const channel = supabase
    .channel('entity-browser-changes')
    .on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'extracted_entities'
      },
      () => {
        queryClient.invalidateQueries(['entities']);
      }
    )
    .subscribe();

  return () => {
    supabase.removeChannel(channel);
  };
}, []);
```

---

## View Modes

### Toggle Between Table and Card View

```tsx
const [viewMode, setViewMode] = useState<'table' | 'cards'>('table');

<div className="flex items-center gap-2">
  <Button
    variant={viewMode === 'table' ? 'default' : 'outline'}
    size="sm"
    onClick={() => setViewMode('table')}
  >
    <Table2 className="h-4 w-4" />
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

## Entity Stats Panel

```tsx
function EntityStatsPanel() {
  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-6">
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Total Entities</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold">{entityCounts?.total}</div>
        </CardContent>
      </Card>
      <Card>
        <CardHeader className="pb-2">
          <CardTitle className="text-sm">Tools</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold">{entityCounts?.tools}</div>
        </CardContent>
      </Card>
      {/* ... more stat cards ... */}
    </div>
  );
}
```

---

## Success Criteria

✅ Display all extracted entities from `extracted_entities` table
✅ Filter by entity type, classification, category, confidence
✅ Search by entity name or ID
✅ Sortable columns in table view
✅ Toggle between table and card view
✅ Entity detail modal with full information
✅ Export entities as CSV or JSON
✅ Real-time updates when new entities are extracted
✅ Link to source video for each entity
✅ Stats panel showing entity counts by type
✅ Responsive grid layout

---

**Created**: 2025-11-28
**Purpose**: Browse and manage all extracted entities
**Phase**: Core Feature (Screen 14 of Research Management System)
**Priority**: High
**Department**: All Departments
