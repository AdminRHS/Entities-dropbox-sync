# Dashboard Stats Screen

**Lovable Build Time:** 10 minutes | **Complexity:** ⭐ Easy

---

## Lovable Initiation Phrase

```
Build a Dashboard Stats screen with overview statistics cards.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + Recharts

Features:
- 4 statistics cards (Total Videos, In Progress, Completed, Success Rate)
- Real-time data from Supabase
- Mini charts showing trends
- AdminRHS-AI-Catalog design (blue theme, gradient headers)

Database: Supabase `video_progress` table

Follow complete spec below ⬇️
```

---

## Overview

Dashboard stats screen displays key metrics for the Research Management System:
- Total videos in queue
- Videos currently being processed
- Completed videos
- Overall success/completion rate
- Trend indicators (↑ ↓)

This is the **landing page** for both Queue Management and Video Processing apps.

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Card, Badge components)
- **Recharts** (mini trend charts)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

Use this mock data to build and test the component before connecting to Supabase:

```typescript
// src/data/mockDashboardData.ts

export const MOCK_STATS = {
  totalVideos: 156,
  inProgress: 23,
  completed: 118,
  completionRate: 75.6
};

export const MOCK_TREND_DATA = [
  { date: '2025-11-22', videos_added: 18 },
  { date: '2025-11-23', videos_added: 22 },
  { date: '2025-11-24', videos_added: 15 },
  { date: '2025-11-25', videos_added: 28 },
  { date: '2025-11-26', videos_added: 31 },
  { date: '2025-11-27', videos_added: 24 },
  { date: '2025-11-28', videos_added: 18 }
];
```

**Usage in component:**
```typescript
// During development, use mock data
const [useMockData, setUseMockData] = useState(true);

useEffect(() => {
  if (useMockData) {
    setStats(MOCK_STATS);
    setTrendData(MOCK_TREND_DATA);
  } else {
    fetchStats(); // Real Supabase query
  }
}, [useMockData]);
```

---

## Database Tables

### Supabase Query

```sql
-- Get statistics from video_progress table
SELECT
  COUNT(*) as total_videos,
  COUNT(*) FILTER (WHERE status = 'in_progress') as in_progress_count,
  COUNT(*) FILTER (WHERE status = 'complete') as completed_count,
  ROUND(
    COUNT(*) FILTER (WHERE status = 'complete')::numeric /
    NULLIF(COUNT(*), 0) * 100,
    1
  ) as completion_rate
FROM video_progress;

-- Get trend data (last 7 days)
SELECT
  DATE(created_at) as date,
  COUNT(*) as videos_added
FROM video_progress
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY DATE(created_at)
ORDER BY date;
```

---

## UI Design (AdminRHS-AI-Catalog)

### Color System

```css
/* From AdminRHS-AI-Catalog */
:root {
  --background: #f5f5f5;
  --card: #ffffff;
  --accent-blue: #428eb4;
  --accent-blue-light: #83CBFF;
  --complete-green: #10B981;
  --in-progress-blue: #60A5FA;
}
```

### Layout

```
┌────────────────────────────────────────────────────────────┐
│  Dashboard Overview                                         │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  TOTAL   │  │ IN PROG  │  │ COMPLETE │  │  SUCCESS │  │
│  │  VIDEOS  │  │  VIDEOS  │  │  VIDEOS  │  │   RATE   │  │
│  │          │  │          │  │          │  │          │  │
│  │   156    │  │    23    │  │   118    │  │  75.6%   │  │
│  │          │  │          │  │          │  │          │  │
│  │  ▁▂▃▄▅▆  │  │  ▁▂▃▄▅▆  │  │  ▁▂▃▄▅▆  │  │  ▁▂▃▄▅▆  │  │
│  │  +12 ↑  │  │  +5 ↑   │  │  +8 ↑   │  │  +2.3% ↑ │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## Component Structure

```typescript
// src/components/DashboardStats.tsx

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { LineChart, Line, ResponsiveContainer } from 'recharts';

interface Stats {
  totalVideos: number;
  inProgress: number;
  completed: number;
  completionRate: number;
}

interface TrendData {
  date: string;
  videos_added: number;
}

export function DashboardStats() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [trendData, setTrendData] = useState<TrendData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();

    // Real-time subscription
    const subscription = supabase
      .channel('video_progress_changes')
      .on('postgres_changes',
        { event: '*', schema: 'public', table: 'video_progress' },
        () => fetchStats()
      )
      .subscribe();

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  async function fetchStats() {
    // Fetch main stats
    const { data, error } = await supabase
      .rpc('get_dashboard_stats');

    if (data) setStats(data[0]);

    // Fetch trend data
    const { data: trends } = await supabase
      .rpc('get_trend_data');

    if (trends) setTrendData(trends);

    setLoading(false);
  }

  if (loading) return <div>Loading...</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6">
      {/* Total Videos Card */}
      <StatCard
        title="Total Videos"
        value={stats?.totalVideos || 0}
        trend="+12"
        trendUp={true}
        color="blue"
        data={trendData}
      />

      {/* In Progress Card */}
      <StatCard
        title="In Progress"
        value={stats?.inProgress || 0}
        trend="+5"
        trendUp={true}
        color="sky"
        data={trendData}
      />

      {/* Completed Card */}
      <StatCard
        title="Completed"
        value={stats?.completed || 0}
        trend="+8"
        trendUp={true}
        color="emerald"
        data={trendData}
      />

      {/* Success Rate Card */}
      <StatCard
        title="Success Rate"
        value={`${stats?.completionRate || 0}%`}
        trend="+2.3%"
        trendUp={true}
        color="violet"
        data={trendData}
      />
    </div>
  );
}

function StatCard({ title, value, trend, trendUp, color, data }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="text-3xl font-bold">{value}</div>

        {/* Mini Chart */}
        <ResponsiveContainer width="100%" height={40}>
          <LineChart data={data}>
            <Line
              type="monotone"
              dataKey="videos_added"
              stroke="#428eb4"
              strokeWidth={2}
              dot={false}
            />
          </LineChart>
        </ResponsiveContainer>

        {/* Trend Indicator */}
        <div className={`text-sm ${trendUp ? 'text-emerald-600' : 'text-red-600'}`}>
          {trend} {trendUp ? '↑' : '↓'}
        </div>
      </CardContent>
    </Card>
  );
}
```

---

## Supabase Functions

Create these functions in Supabase SQL Editor:

```sql
-- Function: get_dashboard_stats
CREATE OR REPLACE FUNCTION get_dashboard_stats()
RETURNS TABLE (
  total_videos BIGINT,
  in_progress BIGINT,
  completed BIGINT,
  completion_rate NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    COUNT(*)::BIGINT as total_videos,
    COUNT(*) FILTER (WHERE status = 'in_progress')::BIGINT as in_progress,
    COUNT(*) FILTER (WHERE status = 'complete')::BIGINT as completed,
    ROUND(
      COUNT(*) FILTER (WHERE status = 'complete')::numeric /
      NULLIF(COUNT(*), 0) * 100,
      1
    ) as completion_rate
  FROM video_progress;
END;
$$ LANGUAGE plpgsql;

-- Function: get_trend_data
CREATE OR REPLACE FUNCTION get_trend_data()
RETURNS TABLE (
  date DATE,
  videos_added BIGINT
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    DATE(created_at) as date,
    COUNT(*)::BIGINT as videos_added
  FROM video_progress
  WHERE created_at >= NOW() - INTERVAL '7 days'
  GROUP BY DATE(created_at)
  ORDER BY date;
END;
$$ LANGUAGE plpgsql;
```

---

## Features

### 1. Real-Time Updates
- Subscribes to `video_progress` table changes
- Auto-refreshes stats when new videos added
- No manual refresh needed

### 2. Trend Indicators
- Shows change from previous period
- Green ↑ for positive trends
- Red ↓ for negative trends

### 3. Mini Charts
- 7-day sparkline charts
- Visual trend representation
- Matches AdminRHS-AI-Catalog blue theme

### 4. Responsive Grid
- 4 columns on desktop
- 2 columns on tablet
- 1 column on mobile

---

## Styling

```css
/* Tailwind classes used */
.grid.grid-cols-1.md:grid-cols-2.lg:grid-cols-4 {
  /* Responsive grid */
}

.text-3xl.font-bold {
  /* Large stat numbers */
}

.text-emerald-600 {
  /* Positive trend color */
}

.text-red-600 {
  /* Negative trend color */
}
```

---

## Testing Checklist

- [ ] Stats display correctly from Supabase
- [ ] Real-time updates work when video_progress changes
- [ ] Trend indicators show correct direction
- [ ] Mini charts render properly
- [ ] Responsive layout works on all screen sizes
- [ ] Cards match AdminRHS-AI-Catalog design

---

## Next Steps After Building

1. **Merge with other screens** - Add to Queue Management App
2. **Add navigation** - Link to Video Queue Table, Search Queue
3. **Enhance charts** - Add tooltips, hover effects
4. **Add date filter** - Show stats for different time periods

---

**Created:** 2025-11-28
**Complexity:** ⭐ Easy
**Build Time:** 10 minutes with Lovable
