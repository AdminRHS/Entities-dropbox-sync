# Cost Tracker Widget

**Lovable Build Time:** 10 minutes | **Complexity:** ⭐ Easy

---

## Lovable Initiation Phrase

```
Build a Cost Tracker Widget for tracking AI API usage and costs.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui

Features:
- Real-time token counter
- Running cost display in USD
- Budget progress bar
- Color changes based on budget (green → yellow → red)
- Daily/total cost breakdown

Database: Supabase `ai_api_usage` table

Follow complete spec below ⬇️
```

---

## Overview

Cost Tracker Widget displays real-time AI API costs for video processing:
- Tokens used (input + output)
- Current cost in USD
- Budget progress (% of daily limit)
- Color-coded warnings (approaching/exceeding budget)

This widget appears in the **Video Processing App** to help monitor AI spending.

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Card, Progress components)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

Use this mock data to build and test the component before connecting to Supabase:

```typescript
// src/data/mockCostData.ts

export const MOCK_API_USAGE = [
  {
    id: '1',
    created_at: new Date().toISOString(),
    video_id: 'Video_024',
    phase: 'phase_2_extraction',
    model: 'claude-sonnet-4.5',
    tokens_input: 45000,
    tokens_output: 12000,
    cost_usd: 2.25,
    processing_time_ms: 8500,
    status: 'success'
  },
  {
    id: '2',
    created_at: new Date().toISOString(),
    video_id: 'Video_025',
    phase: 'phase_3_gap_analysis',
    model: 'gpt-4-turbo',
    tokens_input: 32000,
    tokens_output: 8000,
    cost_usd: 1.84,
    processing_time_ms: 6200,
    status: 'success'
  },
  // Add more mock entries to reach ~$12.45 total
];

export const MOCK_COST_DATA = {
  todayCost: 12.45,
  todayTokens: 1234567,
  todayCalls: 156,
  totalCost: 342.18,
  budgetLimit: 50
};
```

---

## Database Tables

### Supabase Query

```sql
-- Get today's AI usage
SELECT
  SUM(tokens_input) as total_input_tokens,
  SUM(tokens_output) as total_output_tokens,
  SUM(cost_usd) as total_cost,
  COUNT(*) as api_calls
FROM ai_api_usage
WHERE DATE(created_at) = CURRENT_DATE;

-- Get all-time usage
SELECT
  SUM(tokens_input) as total_input_tokens,
  SUM(tokens_output) as total_output_tokens,
  SUM(cost_usd) as total_cost
FROM ai_api_usage;
```

---

## UI Design (AdminRHS-AI-Catalog)

### Color System

```css
/* From AdminRHS-AI-Catalog */
:root {
  --card: #ffffff;
  --accent-blue: #428eb4;
  --budget-safe: #10B981;      /* Green: Under 50% */
  --budget-warning: #FBBF24;   /* Yellow: 50-80% */
  --budget-danger: #EF4444;    /* Red: Over 80% */
}
```

### Layout

```
┌─────────────────────────────┐
│  💰 AI Cost Tracker          │
├─────────────────────────────┤
│                              │
│  Today's Cost                │
│  $12.45                      │
│                              │
│  Budget: $50/day             │
│  ████████░░░░░░░ 24.9%      │
│                              │
│  Tokens Used: 1.2M           │
│  API Calls: 156              │
│                              │
│  All-Time: $342.18           │
│                              │
└─────────────────────────────┘
```

---

## Component Structure

```typescript
// src/components/CostTrackerWidget.tsx

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';

interface CostData {
  todayCost: number;
  todayTokens: number;
  todayCalls: number;
  totalCost: number;
  budgetLimit: number; // $50 default
}

export function CostTrackerWidget() {
  const [costData, setCostData] = useState<CostData>({
    todayCost: 0,
    todayTokens: 0,
    todayCalls: 0,
    totalCost: 0,
    budgetLimit: 50
  });

  useEffect(() => {
    fetchCosts();

    // Real-time subscription
    const subscription = supabase
      .channel('ai_usage_changes')
      .on('postgres_changes',
        { event: 'INSERT', schema: 'public', table: 'ai_api_usage' },
        () => fetchCosts()
      )
      .subscribe();

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  async function fetchCosts() {
    // Today's costs
    const { data: today } = await supabase
      .from('ai_api_usage')
      .select('tokens_input, tokens_output, cost_usd')
      .gte('created_at', new Date().toISOString().split('T')[0]);

    const todayCost = today?.reduce((sum, row) => sum + row.cost_usd, 0) || 0;
    const todayTokens = today?.reduce((sum, row) =>
      sum + row.tokens_input + row.tokens_output, 0) || 0;

    // All-time costs
    const { data: total } = await supabase
      .from('ai_api_usage')
      .select('cost_usd');

    const totalCost = total?.reduce((sum, row) => sum + row.cost_usd, 0) || 0;

    setCostData({
      todayCost,
      todayTokens,
      todayCalls: today?.length || 0,
      totalCost,
      budgetLimit: 50
    });
  }

  const budgetPercent = (costData.todayCost / costData.budgetLimit) * 100;
  const budgetColor = getBudgetColor(budgetPercent);

  return (
    <Card className="w-80">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          💰 AI Cost Tracker
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Today's Cost */}
        <div>
          <p className="text-sm text-muted-foreground">Today's Cost</p>
          <p className="text-3xl font-bold">${costData.todayCost.toFixed(2)}</p>
        </div>

        {/* Budget Progress */}
        <div>
          <div className="flex justify-between text-sm mb-2">
            <span>Budget: ${costData.budgetLimit}/day</span>
            <span className={budgetColor}>
              {budgetPercent.toFixed(1)}%
            </span>
          </div>
          <Progress
            value={budgetPercent}
            className={`h-2 ${budgetColor}`}
          />
        </div>

        {/* Stats */}
        <div className="space-y-2 text-sm">
          <div className="flex justify-between">
            <span className="text-muted-foreground">Tokens Used</span>
            <span className="font-medium">
              {formatTokens(costData.todayTokens)}
            </span>
          </div>
          <div className="flex justify-between">
            <span className="text-muted-foreground">API Calls</span>
            <span className="font-medium">{costData.todayCalls}</span>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t pt-4">
          <div className="flex justify-between text-sm">
            <span className="text-muted-foreground">All-Time Cost</span>
            <span className="font-semibold">${costData.totalCost.toFixed(2)}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

function getBudgetColor(percent: number): string {
  if (percent < 50) return 'text-emerald-600';
  if (percent < 80) return 'text-yellow-600';
  return 'text-red-600';
}

function formatTokens(tokens: number): string {
  if (tokens >= 1_000_000) return `${(tokens / 1_000_000).toFixed(1)}M`;
  if (tokens >= 1_000) return `${(tokens / 1_000).toFixed(1)}K`;
  return tokens.toString();
}
```

---

## Features

### 1. Real-Time Updates
- Subscribes to `ai_api_usage` table
- Auto-updates when new API calls logged
- No refresh needed

### 2. Budget Tracking
- Configurable daily budget ($50 default)
- Progress bar shows % of budget used
- Color changes warn when approaching limit:
  - **Green** (0-50%): Safe
  - **Yellow** (50-80%): Warning
  - **Red** (80%+): Danger

### 3. Token Formatting
- Displays large numbers cleanly:
  - 1,234,567 → "1.2M"
  - 45,678 → "45.7K"

### 4. Daily vs All-Time
- Top section: Today's costs
- Bottom section: Historical total

---

## Cost Calculation

### AI Model Pricing (Per 1M Tokens)

```typescript
const MODEL_COSTS = {
  'claude-sonnet-4.5': { input: 3, output: 15 },
  'claude-opus': { input: 15, output: 75 },
  'gpt-4-turbo': { input: 10, output: 30 },
  'gemini-pro-1.5': { input: 1.25, output: 5 }
};

function calculateCost(
  model: string,
  inputTokens: number,
  outputTokens: number
): number {
  const pricing = MODEL_COSTS[model];
  const inputCost = (inputTokens / 1_000_000) * pricing.input;
  const outputCost = (outputTokens / 1_000_000) * pricing.output;
  return inputCost + outputCost;
}
```

---

## Supabase Table Schema

```sql
-- ai_api_usage table
CREATE TABLE ai_api_usage (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  video_id TEXT NOT NULL,
  phase TEXT NOT NULL, -- 'phase_2_extraction', 'phase_3_gap_analysis', etc.
  model TEXT NOT NULL, -- 'claude-sonnet-4.5', 'gpt-4-turbo', etc.
  tokens_input INTEGER NOT NULL,
  tokens_output INTEGER NOT NULL,
  cost_usd DECIMAL(10, 4) NOT NULL, -- Calculated cost
  processing_time_ms INTEGER, -- How long the API call took
  status TEXT DEFAULT 'success' -- 'success', 'failed', 'rate_limited'
);

-- Index for fast daily queries
CREATE INDEX idx_ai_usage_date ON ai_api_usage(DATE(created_at));
```

---

## Budget Alert Logic

```typescript
// Optional: Alert when budget exceeded
useEffect(() => {
  if (budgetPercent > 100) {
    // Show notification
    toast({
      title: "Budget Exceeded!",
      description: `Daily budget of $${costData.budgetLimit} has been exceeded.`,
      variant: "destructive"
    });
  } else if (budgetPercent > 80) {
    // Warning notification
    toast({
      title: "Budget Warning",
      description: `You've used ${budgetPercent.toFixed(0)}% of your daily budget.`,
      variant: "warning"
    });
  }
}, [budgetPercent]);
```

---

## Styling

```css
/* Tailwind classes used */
.w-80 {
  width: 20rem; /* Fixed width widget */
}

.text-3xl.font-bold {
  /* Large cost display */
}

.text-emerald-600 {
  /* Safe budget color */
}

.text-yellow-600 {
  /* Warning budget color */
}

.text-red-600 {
  /* Danger budget color */
}
```

---

## Testing Checklist

- [ ] Widget displays today's cost correctly
- [ ] Budget progress bar shows correct percentage
- [ ] Colors change at 50% and 80% thresholds
- [ ] Real-time updates when new API calls logged
- [ ] Token formatting shows M/K correctly
- [ ] All-time cost displays cumulative total

---

## Next Steps After Building

1. **Add to Video Processing App** - Place in sidebar or header
2. **Make budget configurable** - Allow user to set daily limit
3. **Add cost breakdown by model** - Show which AI models cost most
4. **Add cost history chart** - Line graph of daily costs over time

---

**Created:** 2025-11-28
**Complexity:** ⭐ Easy
**Build Time:** 10 minutes with Lovable
