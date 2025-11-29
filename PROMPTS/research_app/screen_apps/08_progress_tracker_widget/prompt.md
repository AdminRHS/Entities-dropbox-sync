# Progress Tracker Widget

**Lovable Build Time:** 15-20 minutes | **Complexity:** ⭐⭐ Medium

---

## Lovable Initiation Phrase

```
Build a Progress Tracker Widget with phase visualization.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui

Features:
- Visual phase workflow diagram (7 phases)
- Color-coded phase indicators (Gray, Blue, Green, Yellow, Orange, Purple, Emerald)
- Checkmarks for completed phases
- Progress percentage
- Current phase highlighting
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `video_progress` table

Follow complete spec below ⬇️
```

---

## Overview

Progress Tracker Widget displays video processing status:
- Show all 7 phases visually
- Highlight current phase
- Mark completed phases
- Display overall progress percentage
- Used in both Queue Management and Video Processing apps

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Card, Badge, Progress components)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockProgress.ts

export const PHASE_COLORS = {
  phase_0: '#9CA3AF',  // Gray - Search & Selection
  phase_1: '#60A5FA',  // Blue - Transcription Upload
  phase_2: '#34D399',  // Green - Entity Extraction
  phase_3: '#FBBF24',  // Yellow - Gap Analysis
  phase_4: '#F97316',  // Orange - Integration
  phase_5: '#A78BFA',  // Purple - Knowledge Mapping
  complete: '#10B981'  // Emerald - Complete
};

export const PHASES = [
  { id: 0, name: 'Search & Selection', color: PHASE_COLORS.phase_0 },
  { id: 1, name: 'Transcription Upload', color: PHASE_COLORS.phase_1 },
  { id: 2, name: 'Entity Extraction', color: PHASE_COLORS.phase_2 },
  { id: 3, name: 'Gap Analysis', color: PHASE_COLORS.phase_3 },
  { id: 4, name: 'Integration', color: PHASE_COLORS.phase_4 },
  { id: 5, name: 'Knowledge Mapping', color: PHASE_COLORS.phase_5 },
  { id: 6, name: 'Complete', color: PHASE_COLORS.complete }
];

export const MOCK_VIDEO_PROGRESS = [
  {
    id: '1',
    video_id: 'video_1',
    video_title: 'Claude Desktop MCP Setup Tutorial',
    current_phase: 2, // Entity Extraction
    phase_0_complete: true,
    phase_1_complete: true,
    phase_2_complete: false,
    phase_3_complete: false,
    phase_4_complete: false,
    phase_5_complete: false,
    is_complete: false,
    progress_percentage: 28.6,
    updated_at: '2025-11-28T10:00:00Z'
  },
  {
    id: '2',
    video_id: 'video_2',
    video_title: 'n8n Workflow Automation',
    current_phase: 5, // Knowledge Mapping
    phase_0_complete: true,
    phase_1_complete: true,
    phase_2_complete: true,
    phase_3_complete: true,
    phase_4_complete: true,
    phase_5_complete: false,
    is_complete: false,
    progress_percentage: 85.7,
    updated_at: '2025-11-28T12:00:00Z'
  },
  {
    id: '3',
    video_id: 'video_3',
    video_title: 'Social Media Caption AI Tools',
    current_phase: 6, // Complete
    phase_0_complete: true,
    phase_1_complete: true,
    phase_2_complete: true,
    phase_3_complete: true,
    phase_4_complete: true,
    phase_5_complete: true,
    is_complete: true,
    progress_percentage: 100,
    updated_at: '2025-11-27T14:00:00Z'
  }
];
```

---

## Database Schema

```sql
CREATE TABLE video_progress (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  video_id UUID REFERENCES video_queue(id),
  video_title TEXT,
  current_phase INTEGER DEFAULT 0, -- 0-6

  -- Phase completion flags
  phase_0_complete BOOLEAN DEFAULT FALSE,
  phase_1_complete BOOLEAN DEFAULT FALSE,
  phase_2_complete BOOLEAN DEFAULT FALSE,
  phase_3_complete BOOLEAN DEFAULT FALSE,
  phase_4_complete BOOLEAN DEFAULT FALSE,
  phase_5_complete BOOLEAN DEFAULT FALSE,
  is_complete BOOLEAN DEFAULT FALSE,

  progress_percentage DECIMAL DEFAULT 0,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Component Structure

```typescript
// src/components/ProgressTrackerWidget.tsx

import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { CheckCircle2, Circle } from 'lucide-react';

interface ProgressTrackerProps {
  videoProgress: {
    video_title: string;
    current_phase: number;
    phase_0_complete: boolean;
    phase_1_complete: boolean;
    phase_2_complete: boolean;
    phase_3_complete: boolean;
    phase_4_complete: boolean;
    phase_5_complete: boolean;
    is_complete: boolean;
    progress_percentage: number;
  };
}

export function ProgressTrackerWidget({ videoProgress }: ProgressTrackerProps) {
  const phaseStatus = [
    videoProgress.phase_0_complete,
    videoProgress.phase_1_complete,
    videoProgress.phase_2_complete,
    videoProgress.phase_3_complete,
    videoProgress.phase_4_complete,
    videoProgress.phase_5_complete,
    videoProgress.is_complete
  ];

  function isPhaseActive(phaseId: number) {
    return videoProgress.current_phase === phaseId;
  }

  function isPhaseComplete(phaseId: number) {
    return phaseStatus[phaseId];
  }

  return (
    <Card className="p-6">
      {/* Header */}
      <div className="mb-4">
        <h3 className="font-semibold text-lg mb-1">
          {videoProgress.video_title}
        </h3>
        <div className="flex items-center gap-2">
          <Progress value={videoProgress.progress_percentage} className="flex-1" />
          <span className="text-sm font-medium">
            {videoProgress.progress_percentage.toFixed(0)}%
          </span>
        </div>
      </div>

      {/* Phase Timeline */}
      <div className="space-y-3">
        {PHASES.map((phase, index) => {
          const isActive = isPhaseActive(phase.id);
          const isComplete = isPhaseComplete(phase.id);

          return (
            <div key={phase.id} className="flex items-center gap-3">
              {/* Phase Icon */}
              <div
                className="flex-shrink-0"
                style={{ color: phase.color }}
              >
                {isComplete ? (
                  <CheckCircle2 className="w-6 h-6" />
                ) : (
                  <Circle
                    className="w-6 h-6"
                    fill={isActive ? phase.color : 'none'}
                  />
                )}
              </div>

              {/* Phase Name */}
              <div className="flex-1">
                <div className={`text-sm font-medium ${
                  isActive ? 'text-gray-900' : 'text-gray-600'
                }`}>
                  {phase.name}
                </div>
              </div>

              {/* Status Badge */}
              {isComplete && (
                <Badge
                  style={{
                    backgroundColor: phase.color,
                    color: 'white'
                  }}
                >
                  Complete
                </Badge>
              )}
              {isActive && !isComplete && (
                <Badge
                  variant="outline"
                  style={{ borderColor: phase.color, color: phase.color }}
                >
                  In Progress
                </Badge>
              )}
            </div>
          );
        })}
      </div>

      {/* Completion Message */}
      {videoProgress.is_complete && (
        <div className="mt-4 p-3 bg-green-50 border border-green-200 rounded-lg">
          <p className="text-sm font-medium text-green-800">
            ✓ All phases complete! Video processing finished.
          </p>
        </div>
      )}
    </Card>
  );
}
```

---

## Features

1. **Visual Phase Timeline** - 7 phases with color coding
2. **Checkmarks** - Completed phases marked
3. **Current Phase Highlight** - Active phase emphasized
4. **Progress Bar** - Overall completion percentage
5. **Status Badges** - "Complete" or "In Progress" per phase

---

## Testing Checklist

- [ ] Phase colors display correctly
- [ ] Checkmarks appear for completed phases
- [ ] Current phase highlighted
- [ ] Progress percentage accurate
- [ ] Completion message shows when done
- [ ] Component updates with real-time data

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐ Medium
**Build Time:** 15-20 minutes with Lovable
