## Screen 13: Main Dashboard (Home)

Build a comprehensive analytics dashboard that displays real-time statistics and insights from the Research Management System with proper data connections to Supabase.

---

## Tech Stack
- React 18 + TypeScript + Vite
- Supabase (real-time database queries)
- shadcn/ui components
- Recharts (for charts and graphs)
- Lucide React icons
- Tailwind CSS
- React Query (for data fetching)

---

## Design System

Use the **AdminRHS-AI-Catalog Design System**:

### Colors
```typescript
const COLORS = {
  accentBlue: '#428eb4',
  phase0: '#9CA3AF',
  phase1: '#60A5FA',
  phase2: '#34D399',
  phase3: '#FBBF24',
  phase4: '#F97316',
  phase5: '#A78BFA',
  complete: '#10B981'
}
```

---

## Database Queries (Real Data)

### Query 1: Video Statistics
```typescript
const { data: videoStats } = useQuery({
  queryKey: ['dashboard', 'videos'],
  queryFn: async () => {
    const { data, error } = await supabase
      .from('video_queue')
      .select('phase, priority, department, status', { count: 'exact' });

    if (error) throw error;

    return {
      total: data.length,
      byPhase: data.reduce((acc, v) => {
        acc[v.phase] = (acc[v.phase] || 0) + 1;
        return acc;
      }, {}),
      byPriority: data.reduce((acc, v) => {
        acc[v.priority] = (acc[v.priority] || 0) + 1;
        return acc;
      }, {}),
      byDepartment: data.reduce((acc, v) => {
        acc[v.department] = (acc[v.department] || 0) + 1;
        return acc;
      }, {})
    };
  }
});
```

### Query 2: Entity Counts
```typescript
const { data: entityCounts } = useQuery({
  queryKey: ['dashboard', 'entities'],
  queryFn: async () => {
    // Count extracted entities
    const { count: toolsCount } = await supabase
      .from('extracted_entities')
      .select('*', { count: 'exact', head: true })
      .eq('entity_type', 'TOOL');

    const { count: workflowsCount } = await supabase
      .from('extracted_entities')
      .select('*', { count: 'exact', head: true })
      .eq('entity_type', 'WORKFLOW');

    const { count: skillsCount } = await supabase
      .from('extracted_entities')
      .select('*', { count: 'exact', head: true })
      .eq('entity_type', 'SKILL');

    return {
      tools: toolsCount || 0,
      workflows: workflowsCount || 0,
      skills: skillsCount || 0,
      total: (toolsCount || 0) + (workflowsCount || 0) + (skillsCount || 0)
    };
  }
});
```

### Query 3: Task & Milestone Progress
```typescript
const { data: taskStats } = useQuery({
  queryKey: ['dashboard', 'tasks'],
  queryFn: async () => {
    const { data: milestones } = await supabase
      .from('milestones')
      .select('status');

    const { data: tasks } = await supabase
      .from('tasks')
      .select('status, priority');

    return {
      milestones: {
        total: milestones?.length || 0,
        pending: milestones?.filter(m => m.status === 'pending').length || 0,
        in_progress: milestones?.filter(m => m.status === 'in_progress').length || 0,
        completed: milestones?.filter(m => m.status === 'completed').length || 0
      },
      tasks: {
        total: tasks?.length || 0,
        byStatus: tasks?.reduce((acc, t) => {
          acc[t.status] = (acc[t.status] || 0) + 1;
          return acc;
        }, {}),
        byPriority: tasks?.reduce((acc, t) => {
          acc[t.priority] = (acc[t.priority] || 0) + 1;
          return acc;
        }, {})
      }
    };
  }
});
```

### Query 4: Recent Activity
```typescript
const { data: recentActivity } = useQuery({
  queryKey: ['dashboard', 'activity'],
  queryFn: async () => {
    const { data } = await supabase
      .from('video_queue')
      .select('id, video_title, phase, updated_at')
      .order('updated_at', { ascending: false })
      .limit(5);

    return data || [];
  }
});
```

---

## Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  🏠 Research Management Dashboard              [Refresh]    │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ 📹 Videos│ │ 🔧 Tools │ │ 📊 Flow  │ │ ✅ Tasks │      │
│  │ {count}  │ │ {count}  │ │ {count}  │ │ {count}  │      │
│  │ +12 ↑    │ │ +45 ↑    │ │ +23 ↑    │ │ 67% ✓    │      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────┐ ┌─────────────────────────┐ │
│  │ Phase Distribution        │ │ Department Breakdown    │ │
│  │ [Bar Chart]              │ │ [Pie Chart]             │ │
│  │                          │ │                         │ │
│  │ Phase 0: {count}         │ │ DEV: {count}            │ │
│  │ Phase 1: {count}         │ │ AID: {count}            │ │
│  │ Phase 2: {count}         │ │ MKT: {count}            │ │
│  └───────────────────────────┘ └─────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────┐ ┌─────────────────────────┐ │
│  │ Recent Activity           │ │ Priority Distribution   │ │
│  │                          │ │ [Donut Chart]           │ │
│  │ • Video_024 → Phase 2    │ │                         │ │
│  │ • Video_022 → Phase 1    │ │ Critical: {count}       │ │
│  │ • Video_019 → Complete   │ │ High: {count}           │ │
│  └───────────────────────────┘ └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. Stats Cards (Top Row)

```tsx
interface StatCard {
  title: string;
  value: number;
  change?: number;
  changeType?: 'increase' | 'decrease';
  icon: LucideIcon;
  color: string;
  linkTo?: string;
}

function StatCard({ stat }: { stat: StatCard }) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {stat.title}
        </CardTitle>
        <stat.icon className="h-4 w-4" style={{ color: stat.color }} />
      </CardHeader>
      <CardContent>
        <div className="text-3xl font-bold">{stat.value}</div>
        {stat.change !== undefined && (
          <p className="text-xs text-muted-foreground mt-1">
            {stat.changeType === 'increase' ? (
              <TrendingUp className="inline h-3 w-3 text-green-500" />
            ) : (
              <TrendingDown className="inline h-3 w-3 text-red-500" />
            )}
            <span className="ml-1">
              {stat.change > 0 ? '+' : ''}{stat.change} from last week
            </span>
          </p>
        )}
        {stat.linkTo && (
          <Link to={stat.linkTo} className="text-xs text-blue-500 hover:underline mt-2 block">
            View all →
          </Link>
        )}
      </CardContent>
    </Card>
  );
}

// Usage with REAL DATA
const stats: StatCard[] = [
  {
    title: 'Total Videos',
    value: videoStats?.total || 0,
    change: 12,
    changeType: 'increase',
    icon: PlayCircle,
    color: COLORS.accentBlue,
    linkTo: '/videos'
  },
  {
    title: 'Tools Extracted',
    value: entityCounts?.tools || 0,
    change: 45,
    changeType: 'increase',
    icon: Wrench,
    color: COLORS.phase2,
    linkTo: '/entities?type=tool'
  },
  {
    title: 'Workflows Identified',
    value: entityCounts?.workflows || 0,
    change: 23,
    changeType: 'increase',
    icon: GitBranch,
    color: COLORS.phase4,
    linkTo: '/entities?type=workflow'
  },
  {
    title: 'Tasks Completed',
    value: taskStats?.tasks?.byStatus?.completed || 0,
    change: Math.round(
      ((taskStats?.tasks?.byStatus?.completed || 0) / (taskStats?.tasks?.total || 1)) * 100
    ),
    icon: CheckCircle2,
    color: COLORS.complete,
    linkTo: '/tasks'
  }
];
```

### 2. Phase Distribution Bar Chart

```tsx
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function PhaseDistributionChart() {
  const chartData = useMemo(() => {
    if (!videoStats?.byPhase) return [];

    return [
      { phase: 'Phase 0', count: videoStats.byPhase[0] || 0, fill: COLORS.phase0 },
      { phase: 'Phase 1', count: videoStats.byPhase[1] || 0, fill: COLORS.phase1 },
      { phase: 'Phase 2', count: videoStats.byPhase[2] || 0, fill: COLORS.phase2 },
      { phase: 'Phase 3', count: videoStats.byPhase[3] || 0, fill: COLORS.phase3 },
      { phase: 'Phase 4', count: videoStats.byPhase[4] || 0, fill: COLORS.phase4 },
      { phase: 'Phase 5', count: videoStats.byPhase[5] || 0, fill: COLORS.phase5 },
      { phase: 'Complete', count: videoStats.byPhase[6] || 0, fill: COLORS.complete }
    ];
  }, [videoStats]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Phase Distribution</CardTitle>
        <CardDescription>Videos by processing phase</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="phase" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" fill="#428eb4" />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

### 3. Department Pie Chart

```tsx
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';

function DepartmentPieChart() {
  const chartData = useMemo(() => {
    if (!videoStats?.byDepartment) return [];

    return Object.entries(videoStats.byDepartment).map(([dept, count]) => ({
      name: dept,
      value: count,
      fill: DEPARTMENT_COLORS[dept] || '#ccc'
    }));
  }, [videoStats]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Department Breakdown</CardTitle>
        <CardDescription>Videos by department</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={chartData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {chartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.fill} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

### 4. Recent Activity Feed

```tsx
function RecentActivityFeed() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Recent Activity</CardTitle>
        <CardDescription>Latest updates across the system</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {recentActivity?.map((item) => (
            <div key={item.id} className="flex items-center gap-3">
              <div
                className="w-2 h-2 rounded-full"
                style={{ backgroundColor: PHASE_COLORS[item.phase] }}
              />
              <div className="flex-1">
                <p className="text-sm font-medium">{item.video_title}</p>
                <p className="text-xs text-muted-foreground">
                  Moved to Phase {item.phase} • {formatDistanceToNow(new Date(item.updated_at))} ago
                </p>
              </div>
              <Button variant="ghost" size="sm" asChild>
                <Link to={`/videos/${item.id}`}>
                  <ExternalLink className="h-3 w-3" />
                </Link>
              </Button>
            </div>
          ))}
        </div>
      </CardContent>
      <CardFooter>
        <Button variant="outline" className="w-full" asChild>
          <Link to="/videos">View All Videos →</Link>
        </Button>
      </CardFooter>
    </Card>
  );
}
```

### 5. Priority Distribution Donut Chart

```tsx
function PriorityDonutChart() {
  const chartData = useMemo(() => {
    if (!videoStats?.byPriority) return [];

    return [
      { name: 'Critical', value: videoStats.byPriority.critical || 0, fill: '#EF4444' },
      { name: 'High', value: videoStats.byPriority.high || 0, fill: '#F97316' },
      { name: 'Medium', value: videoStats.byPriority.medium || 0, fill: '#FBBF24' },
      { name: 'Low', value: videoStats.byPriority.low || 0, fill: '#9CA3AF' }
    ];
  }, [videoStats]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Priority Distribution</CardTitle>
        <CardDescription>Videos by priority level</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={chartData}
              cx="50%"
              cy="50%"
              innerRadius={60}
              outerRadius={90}
              fill="#8884d8"
              paddingAngle={5}
              dataKey="value"
            >
              {chartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.fill} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
```

---

## Real-Time Updates

Subscribe to database changes:

```typescript
useEffect(() => {
  const channel = supabase
    .channel('dashboard-changes')
    .on(
      'postgres_changes',
      { event: '*', schema: 'public', table: 'video_queue' },
      () => {
        queryClient.invalidateQueries(['dashboard']);
      }
    )
    .on(
      'postgres_changes',
      { event: '*', schema: 'public', table: 'extracted_entities' },
      () => {
        queryClient.invalidateQueries(['dashboard']);
      }
    )
    .subscribe();

  return () => {
    supabase.removeChannel(channel);
  };
}, []);
```

---

## Quick Actions Panel

```tsx
function QuickActionsPanel() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Quick Actions</CardTitle>
      </CardHeader>
      <CardContent className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <Button asChild variant="outline" className="h-20 flex-col">
          <Link to="/videos/add">
            <Plus className="h-6 w-6 mb-2" />
            Add Video
          </Link>
        </Button>
        <Button asChild variant="outline" className="h-20 flex-col">
          <Link to="/videos/import">
            <Upload className="h-6 w-6 mb-2" />
            Bulk Import
          </Link>
        </Button>
        <Button asChild variant="outline" className="h-20 flex-col">
          <Link to="/entities/extract">
            <Database className="h-6 w-6 mb-2" />
            Extract Entities
          </Link>
        </Button>
        <Button asChild variant="outline" className="h-20 flex-col">
          <Link to="/tasks">
            <ListChecks className="h-6 w-6 mb-2" />
            View Tasks
          </Link>
        </Button>
      </CardContent>
    </Card>
  );
}
```

---

## Responsive Grid Layout

```tsx
<div className="grid gap-6 p-6">
  {/* Stats Cards Row */}
  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    {stats.map((stat, i) => (
      <StatCard key={i} stat={stat} />
    ))}
  </div>

  {/* Charts Row */}
  <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
    <PhaseDistributionChart />
    <DepartmentPieChart />
  </div>

  {/* Activity & Priority Row */}
  <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
    <RecentActivityFeed />
    <PriorityDonutChart />
  </div>

  {/* Quick Actions */}
  <QuickActionsPanel />
</div>
```

---

## Success Criteria

✅ Display real-time video counts from `video_queue` table
✅ Show entity counts from `extracted_entities` table
✅ Display task/milestone progress from `tasks` and `milestones` tables
✅ Phase distribution bar chart with accurate data
✅ Department breakdown pie chart
✅ Priority distribution donut chart
✅ Recent activity feed (last 5 updates)
✅ Real-time updates via Supabase subscriptions
✅ Quick action buttons to major features
✅ Responsive grid layout
✅ No hard-coded sample data - all connected to Supabase

---

**Created**: 2025-11-28
**Purpose**: Main dashboard with real-time analytics and statistics
**Phase**: Core Feature (Screen 13 of Research Management System)
**Priority**: Critical
**Department**: All Departments
