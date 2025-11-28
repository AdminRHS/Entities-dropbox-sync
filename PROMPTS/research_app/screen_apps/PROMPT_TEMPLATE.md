# Screen Prompt Template

**Use this template to create the remaining 7 prompts**

---

## Template Structure

```markdown
# [Screen Name]

**Lovable Build Time:** [10-30] minutes | **Complexity:** ⭐/⭐⭐/⭐⭐⭐

---

## Lovable Initiation Phrase

```
Build a [Screen Name] for [purpose].

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + [additional libs]

Features:
- [Feature 1]
- [Feature 2]
- [Feature 3]
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `[table_name]` table

Follow complete spec below ⬇️
```

---

## Overview

[2-3 sentences describing what this screen does and where it's used]

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** ([specific components])
- **[Additional libraries if needed]**
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mock[ScreenName]Data.ts

export const MOCK_[DATA_NAME] = [
  {
    id: '1',
    // ... mock fields matching database schema
  },
  // ... more mock entries (5-10 examples)
];
```

---

## Database Schema

```sql
CREATE TABLE [table_name] (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  -- ... table fields
);
```

---

## Component Structure

```typescript
// src/components/[ComponentName].tsx

import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

interface [DataType] {
  id: string;
  // ... interface fields
}

export function [ComponentName]() {
  const [data, setData] = useState<[DataType][]>([]);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const { data } = await supabase
      .from('[table_name]')
      .select('*');

    if (data) setData(data);
  }

  return (
    <div>
      {/* Component JSX */}
    </div>
  );
}
```

---

## Features

1. **[Feature 1]** - Description
2. **[Feature 2]** - Description
3. **[Feature 3]** - Description

---

## Testing Checklist

- [ ] Component displays mock data correctly
- [ ] [Specific test 1]
- [ ] [Specific test 2]
- [ ] Real-time updates work (if applicable)
- [ ] Responsive on mobile

---

**Created:** 2025-11-28
**Complexity:** ⭐ [Easy/Medium/Complex]
**Build Time:** [10-30] minutes with Lovable
```

---

## Quick Reference for Each Screen

### 01_video_queue_screen
- **Similar to:** 02_search_queue_screen (copy that structure)
- **Table:** `video_queue`
- **Mock data:** 10-15 video entries with various statuses
- **Key features:** Status filter, department filter, CRUD operations

### 03_filter_panel
- **Type:** Reusable sidebar component
- **No database:** Pure UI component with props
- **Mock data:** Filter options array
- **Key features:** Collapsible, multi-select pills, clear all button

### 05_upload_transcription_screen
- **Library:** React Dropzone
- **Table:** `video_progress` (updates status after upload)
- **Mock data:** File upload simulation
- **Key features:** Drag & drop, file validation, progress bar

### 06_entity_extraction_viewer
- **Library:** TanStack Table with tabs
- **Table:** `extracted_entities`
- **Mock data:** Tools, workflows, actions arrays
- **Key features:** Tabbed interface, entity type filtering

### 07_gap_analysis_screen
- **Layout:** Two-column comparison
- **Table:** `extracted_entities` + existing libraries
- **Mock data:** NEW/EXISTING/UPDATE entities
- **Key features:** Side-by-side diff, approve/reject buttons

### 08_progress_tracker_widget
- **Visual:** Phase workflow diagram
- **Table:** `video_progress`
- **Mock data:** Phase completion states
- **Key features:** Color-coded phases, checkmarks, progress percentage

### 10_knowledge_map_viewer
- **Library:** React Flow
- **Table:** `extracted_entities` with relationships
- **Mock data:** Nodes and edges graph data
- **Key features:** Interactive graph, zoom/pan, node details

---

**Use the 3 completed prompts as your guide. Follow this template exactly!**
