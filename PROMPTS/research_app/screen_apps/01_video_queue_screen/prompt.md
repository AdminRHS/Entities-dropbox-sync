# Video Queue Table Screen

**Lovable Build Time:** 15-20 minutes | **Complexity:** ⭐⭐ Medium

---

## Lovable Initiation Phrase

```
Build a Video Queue Table screen with full CRUD operations.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Table

Features:
- Display videos with status badges (Pending, Selected, Transcribing, etc.)
- Filter by status and department
- Add/edit/delete videos with forms
- Real-time updates from Supabase
- AdminRHS-AI-Catalog design (blue theme, clean table)

Database: Supabase `video_queue` table

Follow complete spec below ⬇️
```

---

## Overview

Video Queue Table is the main screen for managing research videos:
- Browse all queued videos
- Filter by status, department, priority
- Add new videos to queue
- Edit video details
- Delete videos
- Track processing status

Used in **Queue Management App** for Phase 0 (Search & Selection).

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Table, Dialog, Form components)
- **TanStack Table** (data grid)
- **React Hook Form** (form handling)
- **Zod** (validation)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockVideoQueue.ts

export const MOCK_VIDEOS = [
  {
    id: '1',
    created_at: '2025-11-28T10:00:00Z',
    video_url: 'https://youtube.com/watch?v=abc123',
    video_title: 'Claude Desktop MCP Setup Tutorial',
    channel_name: 'AI Explained',
    duration_minutes: 15,
    priority: 'high',
    status: 'selected',
    department: 'DEV',
    assigned_to: 'alex@remotehelpers.com',
    added_by: 'maria@remotehelpers.com',
    notes: 'Great tutorial on MCP connectors',
    perplexity_search_id: 'search_123'
  },
  {
    id: '2',
    created_at: '2025-11-28T11:30:00Z',
    video_url: 'https://youtube.com/watch?v=xyz789',
    video_title: 'n8n Workflow Automation for Developers',
    channel_name: 'DevOps Weekly',
    duration_minutes: 22,
    priority: 'medium',
    status: 'transcribing',
    department: 'DEV',
    assigned_to: 'jordan@remotehelpers.com',
    added_by: 'alex@remotehelpers.com',
    notes: null,
    perplexity_search_id: 'search_124'
  },
  {
    id: '3',
    created_at: '2025-11-27T09:00:00Z',
    video_url: 'https://youtube.com/watch?v=def456',
    video_title: 'Social Media Caption AI Tools',
    channel_name: 'Marketing Pro',
    duration_minutes: 18,
    priority: 'low',
    status: 'pending',
    department: 'SMM',
    assigned_to: null,
    added_by: 'sam@remotehelpers.com',
    notes: 'Check if tools are free',
    perplexity_search_id: 'search_125'
  },
  // Add 10-15 more entries for realistic testing
];
```

---

## Database Schema

```sql
CREATE TABLE video_queue (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  video_url TEXT NOT NULL UNIQUE,
  video_title TEXT NOT NULL,
  channel_name TEXT,
  duration_minutes INTEGER,
  priority TEXT DEFAULT 'medium', -- 'low', 'medium', 'high'
  status TEXT DEFAULT 'pending', -- 'pending', 'selected', 'transcribing', 'transcribed', 'processing', 'complete', 'rejected'
  department TEXT NOT NULL, -- 'DEV', 'SMM', 'VID', 'AID', etc.
  assigned_to TEXT, -- employee email
  added_by TEXT NOT NULL, -- employee email
  notes TEXT,
  perplexity_search_id UUID REFERENCES search_queue(id)
);

CREATE INDEX idx_video_status ON video_queue(status);
CREATE INDEX idx_video_department ON video_queue(department);
```

---

## Component Structure with User Input

```typescript
// src/components/VideoQueueTable.tsx

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Input } from '@/components/ui/input';
import { Select } from '@/components/ui/select';
import { Textarea } from '@/components/ui/textarea';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

const videoSchema = z.object({
  video_url: z.string().url('Must be a valid URL'),
  video_title: z.string().min(3, 'Title must be at least 3 characters'),
  channel_name: z.string().optional(),
  duration_minutes: z.number().min(1).max(999),
  priority: z.enum(['low', 'medium', 'high']),
  department: z.enum(['DEV', 'SMM', 'VID', 'AID', 'DGN', 'MKT']),
  notes: z.string().optional()
});

type VideoFormData = z.infer<typeof videoSchema>;

export function VideoQueueTable() {
  const [isAddDialogOpen, setIsAddDialogOpen] = useState(false);
  const [isEditDialogOpen, setIsEditDialogOpen] = useState(false);
  const [selectedVideo, setSelectedVideo] = useState(null);

  const form = useForm<VideoFormData>({
    resolver: zodResolver(videoSchema),
    defaultValues: {
      priority: 'medium',
      department: 'DEV'
    }
  });

  async function onSubmit(data: VideoFormData) {
    // Add to Supabase
    const { error } = await supabase
      .from('video_queue')
      .insert([{
        ...data,
        added_by: 'current_user@example.com' // Get from auth
      }]);

    if (!error) {
      setIsAddDialogOpen(false);
      form.reset();
    }
  }

  return (
    <div className="space-y-4">
      {/* Add Video Button */}
      <Button onClick={() => setIsAddDialogOpen(true)}>
        + Add Video
      </Button>

      {/* Add/Edit Dialog */}
      <Dialog open={isAddDialogOpen} onOpenChange={setIsAddDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Add Video to Queue</DialogTitle>
          </DialogHeader>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
            <div>
              <label>Video URL *</label>
              <Input
                {...form.register('video_url')}
                placeholder="https://youtube.com/watch?v=..."
              />
              {form.formState.errors.video_url && (
                <p className="text-sm text-red-600">
                  {form.formState.errors.video_url.message}
                </p>
              )}
            </div>

            <div>
              <label>Video Title *</label>
              <Input
                {...form.register('video_title')}
                placeholder="Enter video title"
              />
            </div>

            <div>
              <label>Channel Name</label>
              <Input
                {...form.register('channel_name')}
                placeholder="Channel name"
              />
            </div>

            <div>
              <label>Duration (minutes) *</label>
              <Input
                type="number"
                {...form.register('duration_minutes', { valueAsNumber: true })}
                placeholder="15"
              />
            </div>

            <div>
              <label>Priority *</label>
              <Select {...form.register('priority')}>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </Select>
            </div>

            <div>
              <label>Department *</label>
              <Select {...form.register('department')}>
                <option value="DEV">Development</option>
                <option value="SMM">Social Media</option>
                <option value="VID">Video</option>
                <option value="AID">AI & Automation</option>
              </Select>
            </div>

            <div>
              <label>Notes</label>
              <Textarea
                {...form.register('notes')}
                placeholder="Any notes about this video..."
              />
            </div>

            <div className="flex gap-2">
              <Button type="submit">Add to Queue</Button>
              <Button
                type="button"
                variant="outline"
                onClick={() => setIsAddDialogOpen(false)}
              >
                Cancel
              </Button>
            </div>
          </form>
        </DialogContent>
      </Dialog>

      {/* Table (same as search queue example) */}
    </div>
  );
}
```

---

## Features

1. **Add Video Form** - Modal dialog with validation
2. **Edit Video** - Pre-filled form with existing data
3. **Delete Video** - Confirmation dialog
4. **Filter & Search** - By status, department, priority
5. **Real-Time Updates** - Auto-refresh when videos added/updated

---

## Testing Checklist

- [ ] Add video form validates required fields
- [ ] URL validation works correctly
- [ ] Edit pre-fills form with video data
- [ ] Delete shows confirmation dialog
- [ ] Filters work correctly
- [ ] Form resets after successful submission

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐ Medium
**Build Time:** 15-20 minutes with Lovable
