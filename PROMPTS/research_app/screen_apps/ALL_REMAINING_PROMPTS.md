# All Remaining Screen Prompts (7)

**Instructions:** Copy each section below into its respective folder's `prompt.md` file

---

# 01_video_queue_screen/prompt.md

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

---
---

# 03_filter_panel/prompt.md

# Filter Panel Component

**Lovable Build Time:** 10-15 minutes | **Complexity:** ⭐ Easy

---

## Lovable Initiation Phrase

```
Build a reusable Filter Panel sidebar component.

Tech stack: React 18 + TypeScript + Vite + shadcn/ui

Features:
- Collapsible filter sections (Status, Department, Priority, Date Range)
- Multi-select pill badges
- Clear all filters button
- Filter count badge
- AdminRHS-AI-Catalog design (blue theme)

Pure UI component with props (no database needed)

Follow complete spec below ⬇️
```

---

## Overview

Filter Panel is a reusable sidebar component for filtering tables:
- Collapsible filter sections
- Multi-select with visual pills
- Clear all functionality
- Filter count display
- Used in Queue Management and Video Processing apps

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **shadcn/ui** (Accordion, Badge, Checkbox components)
- **Tailwind CSS** (styling)
- **No database** - Pure UI component

---

## Sample Data (Filter Options)

```typescript
// src/data/mockFilterOptions.ts

export const FILTER_OPTIONS = {
  status: [
    { value: 'pending', label: 'Pending', count: 24 },
    { value: 'selected', label: 'Selected', count: 18 },
    { value: 'transcribing', label: 'Transcribing', count: 8 },
    { value: 'transcribed', label: 'Transcribed', count: 32 },
    { value: 'processing', label: 'Processing', count: 12 },
    { value: 'complete', label: 'Complete', count: 118 },
    { value: 'rejected', label: 'Rejected', count: 6 }
  ],
  department: [
    { value: 'DEV', label: 'Development', count: 45 },
    { value: 'SMM', label: 'Social Media', count: 38 },
    { value: 'VID', label: 'Video', count: 22 },
    { value: 'AID', label: 'AI & Automation', count: 51 },
    { value: 'DGN', label: 'Design', count: 14 },
    { value: 'MKT', label: 'Marketing', count: 18 }
  ],
  priority: [
    { value: 'high', label: 'High Priority', count: 28 },
    { value: 'medium', label: 'Medium Priority', count: 102 },
    { value: 'low', label: 'Low Priority', count: 58 }
  ]
};
```

---

## Component Structure with User Input

```typescript
// src/components/FilterPanel.tsx

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Checkbox } from '@/components/ui/checkbox';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

interface FilterPanelProps {
  onFilterChange: (filters: FilterState) => void;
  initialFilters?: FilterState;
}

interface FilterState {
  status: string[];
  department: string[];
  priority: string[];
  dateRange?: {
    start: string;
    end: string;
  };
}

export function FilterPanel({ onFilterChange, initialFilters }: FilterPanelProps) {
  const [filters, setFilters] = useState<FilterState>(initialFilters || {
    status: [],
    department: [],
    priority: []
  });

  // Handle checkbox toggle
  function toggleFilter(category: keyof FilterState, value: string) {
    const currentValues = filters[category] as string[];
    const newValues = currentValues.includes(value)
      ? currentValues.filter(v => v !== value)
      : [...currentValues, value];

    const newFilters = { ...filters, [category]: newValues };
    setFilters(newFilters);
    onFilterChange(newFilters);
  }

  // Clear all filters
  function clearAll() {
    const emptyFilters = {
      status: [],
      department: [],
      priority: []
    };
    setFilters(emptyFilters);
    onFilterChange(emptyFilters);
  }

  // Count total active filters
  const activeFilterCount =
    filters.status.length +
    filters.department.length +
    filters.priority.length;

  return (
    <div className="w-64 border-r border-gray-200 p-4 space-y-4">
      {/* Header with Clear All */}
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-lg">
          Filters
          {activeFilterCount > 0 && (
            <Badge variant="secondary" className="ml-2">
              {activeFilterCount}
            </Badge>
          )}
        </h3>
        {activeFilterCount > 0 && (
          <Button
            variant="ghost"
            size="sm"
            onClick={clearAll}
          >
            Clear All
          </Button>
        )}
      </div>

      {/* Collapsible Filter Sections */}
      <Accordion type="multiple" defaultValue={['status', 'department', 'priority']}>
        {/* Status Filters */}
        <AccordionItem value="status">
          <AccordionTrigger>
            Status
            {filters.status.length > 0 && (
              <Badge variant="secondary" className="ml-2">
                {filters.status.length}
              </Badge>
            )}
          </AccordionTrigger>
          <AccordionContent>
            <div className="space-y-2">
              {FILTER_OPTIONS.status.map(option => (
                <label key={option.value} className="flex items-center gap-2 cursor-pointer">
                  <Checkbox
                    checked={filters.status.includes(option.value)}
                    onCheckedChange={() => toggleFilter('status', option.value)}
                  />
                  <span className="text-sm">{option.label}</span>
                  <span className="text-xs text-gray-500 ml-auto">
                    ({option.count})
                  </span>
                </label>
              ))}
            </div>
          </AccordionContent>
        </AccordionItem>

        {/* Department Filters */}
        <AccordionItem value="department">
          <AccordionTrigger>
            Department
            {filters.department.length > 0 && (
              <Badge variant="secondary" className="ml-2">
                {filters.department.length}
              </Badge>
            )}
          </AccordionTrigger>
          <AccordionContent>
            <div className="space-y-2">
              {FILTER_OPTIONS.department.map(option => (
                <label key={option.value} className="flex items-center gap-2 cursor-pointer">
                  <Checkbox
                    checked={filters.department.includes(option.value)}
                    onCheckedChange={() => toggleFilter('department', option.value)}
                  />
                  <span className="text-sm">{option.label}</span>
                  <span className="text-xs text-gray-500 ml-auto">
                    ({option.count})
                  </span>
                </label>
              ))}
            </div>
          </AccordionContent>
        </AccordionItem>

        {/* Priority Filters */}
        <AccordionItem value="priority">
          <AccordionTrigger>
            Priority
            {filters.priority.length > 0 && (
              <Badge variant="secondary" className="ml-2">
                {filters.priority.length}
              </Badge>
            )}
          </AccordionTrigger>
          <AccordionContent>
            <div className="space-y-2">
              {FILTER_OPTIONS.priority.map(option => (
                <label key={option.value} className="flex items-center gap-2 cursor-pointer">
                  <Checkbox
                    checked={filters.priority.includes(option.value)}
                    onCheckedChange={() => toggleFilter('priority', option.value)}
                  />
                  <span className="text-sm">{option.label}</span>
                  <span className="text-xs text-gray-500 ml-auto">
                    ({option.count})
                  </span>
                </label>
              ))}
            </div>
          </AccordionContent>
        </AccordionItem>
      </Accordion>

      {/* Active Filter Pills */}
      {activeFilterCount > 0 && (
        <div className="pt-4 border-t">
          <p className="text-xs text-gray-500 mb-2">Active Filters:</p>
          <div className="flex flex-wrap gap-2">
            {filters.status.map(status => (
              <Badge
                key={status}
                variant="default"
                className="cursor-pointer"
                onClick={() => toggleFilter('status', status)}
              >
                {status} ×
              </Badge>
            ))}
            {filters.department.map(dept => (
              <Badge
                key={dept}
                variant="default"
                className="cursor-pointer"
                onClick={() => toggleFilter('department', dept)}
              >
                {dept} ×
              </Badge>
            ))}
            {filters.priority.map(priority => (
              <Badge
                key={priority}
                variant="default"
                className="cursor-pointer"
                onClick={() => toggleFilter('priority', priority)}
              >
                {priority} ×
              </Badge>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
```

---

## Features

1. **Collapsible Sections** - Accordion UI for each filter category
2. **Multi-Select Checkboxes** - Select multiple filters per category
3. **Filter Count Badges** - Show number of active filters
4. **Active Filter Pills** - Visual pills with click-to-remove
5. **Clear All Button** - Reset all filters at once

---

## Testing Checklist

- [ ] Checkboxes toggle correctly
- [ ] Active filter count updates
- [ ] Clear all resets all filters
- [ ] Filter pills display and remove on click
- [ ] Accordion expands/collapses smoothly
- [ ] Parent component receives filter changes

---

**Created:** 2025-11-28
**Complexity:** ⭐ Easy
**Build Time:** 10-15 minutes with Lovable

---
---

# 05_upload_transcription_screen/prompt.md

# Upload Transcription Screen

**Lovable Build Time:** 15-20 minutes | **Complexity:** ⭐⭐ Medium

---

## Lovable Initiation Phrase

```
Build an Upload Transcription screen with drag & drop file upload.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + React Dropzone

Features:
- Drag & drop file upload area
- File type validation (.txt, .srt, .vtt only)
- File size validation (max 10MB)
- Upload progress bar
- Preview uploaded content
- Link transcription to video
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `video_progress` table (updates status)

Follow complete spec below ⬇️
```

---

## Overview

Upload Transcription Screen handles Phase 1 of video processing:
- Upload transcription files
- Validate file type and size
- Preview content before submission
- Link to video in queue
- Update video status to "transcribed"

Used in **Video Processing App** for Phase 1.

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + storage)
- **shadcn/ui** (Card, Button, Progress components)
- **React Dropzone** (file upload)
- **React Hook Form** (form handling)
- **Zod** (validation)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockTranscriptions.ts

export const MOCK_VIDEOS_FOR_UPLOAD = [
  {
    id: '1',
    video_title: 'Claude Desktop MCP Setup Tutorial',
    video_url: 'https://youtube.com/watch?v=abc123',
    status: 'selected',
    department: 'DEV'
  },
  {
    id: '2',
    video_title: 'n8n Workflow Automation for Developers',
    video_url: 'https://youtube.com/watch?v=xyz789',
    status: 'selected',
    department: 'DEV'
  },
  {
    id: '3',
    video_title: 'AI Caption Generator Tools Review',
    video_url: 'https://youtube.com/watch?v=def456',
    status: 'selected',
    department: 'SMM'
  }
];

export const MOCK_UPLOAD_RESULT = {
  success: true,
  file_path: '/transcriptions/video_1_transcript.txt',
  file_size_kb: 245,
  upload_time: '2025-11-28T14:30:00Z',
  preview: `00:00:00 Introduction to Claude Desktop
00:00:15 Installing MCP servers
00:00:45 Configuring the settings
00:01:20 Testing your first connection
00:02:00 Common troubleshooting tips...`
};
```

---

## Database Schema

```sql
-- Update existing video_progress table
UPDATE video_progress
SET
  status = 'transcribed',
  transcription_file_path = 'path/to/file.txt',
  transcription_uploaded_at = NOW(),
  phase_1_complete = TRUE
WHERE video_id = 'selected_video_id';
```

---

## Component Structure with User Input

```typescript
// src/components/UploadTranscriptionScreen.tsx

import { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

const uploadSchema = z.object({
  video_id: z.string().min(1, 'Please select a video'),
  file: z.instanceof(File)
    .refine(file => file.size <= 10 * 1024 * 1024, 'File must be less than 10MB')
    .refine(
      file => ['.txt', '.srt', '.vtt'].some(ext => file.name.endsWith(ext)),
      'Only .txt, .srt, or .vtt files allowed'
    )
});

type UploadFormData = z.infer<typeof uploadSchema>;

export function UploadTranscriptionScreen() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [preview, setPreview] = useState<string>('');
  const [isUploading, setIsUploading] = useState(false);

  const form = useForm<UploadFormData>({
    resolver: zodResolver(uploadSchema)
  });

  // Handle file drop
  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (file) {
      setSelectedFile(file);
      form.setValue('file', file);

      // Read file for preview
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target?.result as string;
        setPreview(text.slice(0, 500)); // First 500 chars
      };
      reader.readAsText(file);
    }
  }, [form]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/plain': ['.txt'],
      'text/vtt': ['.vtt'],
      'application/x-subrip': ['.srt']
    },
    maxFiles: 1,
    maxSize: 10 * 1024 * 1024 // 10MB
  });

  async function onSubmit(data: UploadFormData) {
    setIsUploading(true);

    // Simulate upload progress
    for (let i = 0; i <= 100; i += 10) {
      setUploadProgress(i);
      await new Promise(resolve => setTimeout(resolve, 200));
    }

    // Upload to Supabase Storage
    const { data: uploadData, error } = await supabase.storage
      .from('transcriptions')
      .upload(`video_${data.video_id}/${selectedFile!.name}`, selectedFile!);

    if (!error) {
      // Update video_progress status
      await supabase
        .from('video_progress')
        .update({
          status: 'transcribed',
          transcription_file_path: uploadData.path,
          transcription_uploaded_at: new Date().toISOString(),
          phase_1_complete: true
        })
        .eq('video_id', data.video_id);

      // Reset form
      setSelectedFile(null);
      setPreview('');
      setUploadProgress(0);
      form.reset();
    }

    setIsUploading(false);
  }

  return (
    <div className="max-w-2xl mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-bold">Upload Transcription</h1>
      <p className="text-gray-600">
        Upload transcription files for videos in Phase 1 (Transcription Upload)
      </p>

      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        {/* Video Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">
            Select Video *
          </label>
          <Select
            onValueChange={(value) => form.setValue('video_id', value)}
          >
            <SelectTrigger>
              <SelectValue placeholder="Choose a video..." />
            </SelectTrigger>
            <SelectContent>
              {MOCK_VIDEOS_FOR_UPLOAD.map(video => (
                <SelectItem key={video.id} value={video.id}>
                  {video.video_title} ({video.department})
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
          {form.formState.errors.video_id && (
            <p className="text-sm text-red-600 mt-1">
              {form.formState.errors.video_id.message}
            </p>
          )}
        </div>

        {/* File Upload Area */}
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
            isDragActive
              ? 'border-blue-500 bg-blue-50'
              : 'border-gray-300 hover:border-blue-400'
          }`}
        >
          <input {...getInputProps()} />

          {selectedFile ? (
            <div>
              <p className="text-lg font-semibold text-green-600">
                ✓ {selectedFile.name}
              </p>
              <p className="text-sm text-gray-500">
                {(selectedFile.size / 1024).toFixed(2)} KB
              </p>
              <Button
                type="button"
                variant="ghost"
                size="sm"
                onClick={(e) => {
                  e.stopPropagation();
                  setSelectedFile(null);
                  setPreview('');
                }}
                className="mt-2"
              >
                Remove File
              </Button>
            </div>
          ) : (
            <div>
              <p className="text-lg mb-2">
                {isDragActive
                  ? 'Drop the file here...'
                  : 'Drag & drop transcription file here'}
              </p>
              <p className="text-sm text-gray-500">
                or click to browse
              </p>
              <p className="text-xs text-gray-400 mt-2">
                Accepted: .txt, .srt, .vtt (max 10MB)
              </p>
            </div>
          )}
        </div>

        {form.formState.errors.file && (
          <p className="text-sm text-red-600">
            {form.formState.errors.file.message}
          </p>
        )}

        {/* Preview */}
        {preview && (
          <Card className="p-4">
            <h3 className="font-semibold mb-2">Preview:</h3>
            <pre className="text-xs bg-gray-50 p-3 rounded overflow-auto max-h-40">
              {preview}...
            </pre>
          </Card>
        )}

        {/* Upload Progress */}
        {isUploading && (
          <div>
            <Progress value={uploadProgress} className="mb-2" />
            <p className="text-sm text-center text-gray-600">
              Uploading... {uploadProgress}%
            </p>
          </div>
        )}

        {/* Submit Button */}
        <Button
          type="submit"
          disabled={!selectedFile || isUploading}
          className="w-full"
        >
          {isUploading ? 'Uploading...' : 'Upload Transcription'}
        </Button>
      </form>
    </div>
  );
}
```

---

## Features

1. **Drag & Drop Upload** - React Dropzone integration
2. **File Validation** - Type (.txt/.srt/.vtt) and size (10MB) checks
3. **Preview Content** - Show first 500 characters
4. **Upload Progress** - Visual progress bar
5. **Video Selection** - Dropdown of videos ready for transcription

---

## Testing Checklist

- [ ] Drag & drop works correctly
- [ ] File type validation rejects invalid files
- [ ] File size validation rejects files > 10MB
- [ ] Preview shows file content
- [ ] Progress bar animates during upload
- [ ] Video status updates to "transcribed"
- [ ] Form resets after successful upload

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐ Medium
**Build Time:** 15-20 minutes with Lovable

---
---

# 06_entity_extraction_viewer/prompt.md

# Entity Extraction Viewer

**Lovable Build Time:** 15-20 minutes | **Complexity:** ⭐⭐ Medium

---

## Lovable Initiation Phrase

```
Build an Entity Extraction Viewer with tabbed tables.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Table

Features:
- Tabbed interface (Tools, Workflows, Actions, Objects)
- Filterable tables for each entity type
- Entity detail cards
- Status badges (NEW, EXISTING, UPDATE)
- Export to JSON
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `extracted_entities` table

Follow complete spec below ⬇️
```

---

## Overview

Entity Extraction Viewer displays Phase 2 results:
- View extracted entities by type
- Filter and search entities
- See entity details and metadata
- Identify NEW vs EXISTING entities
- Export entities for review

Used in **Video Processing App** for Phase 2 (Entity Extraction).

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Tabs, Table, Card, Badge components)
- **TanStack Table** (data grid)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockExtractedEntities.ts

export const MOCK_EXTRACTED_TOOLS = [
  {
    id: '1',
    entity_type: 'TOOL',
    entity_name: 'Claude Desktop',
    entity_id: 'TOOL-AI-224',
    classification: 'NEW',
    category: 'AI',
    description: 'Desktop application for Claude AI with MCP server support',
    video_id: 'video_1',
    video_title: 'Claude Desktop MCP Setup Tutorial',
    extracted_at: '2025-11-28T10:00:00Z',
    confidence_score: 0.95,
    metadata: {
      pricing: 'Free + Pro ($20/mo)',
      platform: 'Desktop (Mac/Windows)',
      website: 'claude.ai'
    }
  },
  {
    id: '2',
    entity_type: 'TOOL',
    entity_name: 'n8n',
    entity_id: 'TOOL-AUTOMATION-112',
    classification: 'EXISTING',
    category: 'AUTOMATION',
    description: 'Workflow automation platform for developers',
    video_id: 'video_2',
    video_title: 'n8n Workflow Automation',
    extracted_at: '2025-11-28T11:00:00Z',
    confidence_score: 0.98,
    metadata: {
      pricing: 'Self-hosted free, Cloud from $20/mo',
      platform: 'Web/Self-hosted'
    }
  }
];

export const MOCK_EXTRACTED_WORKFLOWS = [
  {
    id: '3',
    entity_type: 'WORKFLOW',
    entity_name: 'MCP Server Setup Process',
    entity_id: 'WRF-026',
    classification: 'NEW',
    description: 'Complete workflow for setting up MCP servers in Claude Desktop',
    video_id: 'video_1',
    video_title: 'Claude Desktop MCP Setup Tutorial',
    extracted_at: '2025-11-28T10:00:00Z',
    steps_count: 8,
    estimated_time_minutes: 15
  }
];

export const MOCK_EXTRACTED_ACTIONS = [
  {
    id: '4',
    entity_type: 'ACTION',
    entity_name: 'Install MCP Server',
    entity_id: 'ACTION-434',
    classification: 'UPDATE',
    description: 'Install and configure MCP server for Claude Desktop',
    workflow_id: 'WRF-026',
    video_id: 'video_1',
    extracted_at: '2025-11-28T10:00:00Z',
    difficulty: 'Medium',
    time_estimate_minutes: 5
  }
];

export const MOCK_EXTRACTED_OBJECTS = [
  {
    id: '5',
    entity_type: 'OBJECT',
    entity_name: 'MCP Configuration File',
    entity_id: 'OBJ-AI-089',
    classification: 'NEW',
    description: 'JSON configuration file for MCP servers',
    video_id: 'video_1',
    extracted_at: '2025-11-28T10:00:00Z',
    file_type: '.json',
    example_provided: true
  }
];
```

---

## Database Schema

```sql
CREATE TABLE extracted_entities (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  entity_type TEXT NOT NULL, -- 'TOOL', 'WORKFLOW', 'ACTION', 'OBJECT'
  entity_name TEXT NOT NULL,
  entity_id TEXT, -- 'TOOL-AI-224', 'WRF-026', etc.
  classification TEXT, -- 'NEW', 'EXISTING', 'UPDATE'
  description TEXT,
  video_id UUID REFERENCES video_queue(id),
  video_title TEXT,
  extracted_at TIMESTAMPTZ,
  confidence_score DECIMAL,
  metadata JSONB,

  -- Entity-specific fields
  category TEXT, -- For tools
  steps_count INTEGER, -- For workflows
  workflow_id TEXT, -- For actions
  difficulty TEXT, -- For actions
  file_type TEXT -- For objects
);

CREATE INDEX idx_entity_type ON extracted_entities(entity_type);
CREATE INDEX idx_entity_classification ON extracted_entities(classification);
```

---

## Component Structure

```typescript
// src/components/EntityExtractionViewer.tsx

import { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import {
  useReactTable,
  getCoreRowModel,
  getFilteredRowModel,
  flexRender
} from '@tanstack/react-table';

export function EntityExtractionViewer() {
  const [activeTab, setActiveTab] = useState('tools');
  const [searchTerm, setSearchTerm] = useState('');

  // Classification badge color
  function getClassificationColor(classification: string) {
    switch (classification) {
      case 'NEW': return 'bg-green-500';
      case 'EXISTING': return 'bg-gray-500';
      case 'UPDATE': return 'bg-yellow-500';
      default: return 'bg-blue-500';
    }
  }

  // Export to JSON
  function exportToJSON(data: any[], type: string) {
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `extracted_${type}_${new Date().toISOString()}.json`;
    a.click();
  }

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Extracted Entities</h1>
          <p className="text-gray-600">
            Review entities extracted from video transcriptions (Phase 2)
          </p>
        </div>
      </div>

      {/* Search Bar */}
      <div className="flex gap-4">
        <Input
          placeholder="Search entities..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="max-w-md"
        />
      </div>

      {/* Tabbed Interface */}
      <Tabs value={activeTab} onValueChange={setActiveTab}>
        <TabsList>
          <TabsTrigger value="tools">
            Tools
            <Badge variant="secondary" className="ml-2">
              {MOCK_EXTRACTED_TOOLS.length}
            </Badge>
          </TabsTrigger>
          <TabsTrigger value="workflows">
            Workflows
            <Badge variant="secondary" className="ml-2">
              {MOCK_EXTRACTED_WORKFLOWS.length}
            </Badge>
          </TabsTrigger>
          <TabsTrigger value="actions">
            Actions
            <Badge variant="secondary" className="ml-2">
              {MOCK_EXTRACTED_ACTIONS.length}
            </Badge>
          </TabsTrigger>
          <TabsTrigger value="objects">
            Objects
            <Badge variant="secondary" className="ml-2">
              {MOCK_EXTRACTED_OBJECTS.length}
            </Badge>
          </TabsTrigger>
        </TabsList>

        {/* Tools Tab */}
        <TabsContent value="tools" className="space-y-4">
          <div className="flex justify-end">
            <Button
              variant="outline"
              onClick={() => exportToJSON(MOCK_EXTRACTED_TOOLS, 'tools')}
            >
              Export JSON
            </Button>
          </div>

          <div className="grid grid-cols-1 gap-4">
            {MOCK_EXTRACTED_TOOLS
              .filter(tool =>
                tool.entity_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                tool.description.toLowerCase().includes(searchTerm.toLowerCase())
              )
              .map(tool => (
                <Card key={tool.id} className="p-4">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <h3 className="font-semibold text-lg">
                          {tool.entity_name}
                        </h3>
                        <Badge className={getClassificationColor(tool.classification)}>
                          {tool.classification}
                        </Badge>
                        <Badge variant="outline">
                          {tool.entity_id}
                        </Badge>
                      </div>
                      <p className="text-sm text-gray-600 mb-3">
                        {tool.description}
                      </p>
                      <div className="flex flex-wrap gap-2 text-xs">
                        <Badge variant="secondary">
                          Category: {tool.category}
                        </Badge>
                        <Badge variant="secondary">
                          Confidence: {(tool.confidence_score * 100).toFixed(0)}%
                        </Badge>
                        <Badge variant="secondary">
                          From: {tool.video_title}
                        </Badge>
                      </div>
                      {tool.metadata && (
                        <div className="mt-3 p-2 bg-gray-50 rounded text-xs">
                          <strong>Metadata:</strong>
                          <pre className="mt-1">
                            {JSON.stringify(tool.metadata, null, 2)}
                          </pre>
                        </div>
                      )}
                    </div>
                  </div>
                </Card>
              ))}
          </div>
        </TabsContent>

        {/* Similar TabsContent for workflows, actions, objects */}
      </Tabs>
    </div>
  );
}
```

---

## Features

1. **Tabbed Interface** - Separate tabs for each entity type
2. **Entity Cards** - Rich display with metadata
3. **Classification Badges** - Visual NEW/EXISTING/UPDATE indicators
4. **Search & Filter** - Find specific entities
5. **Export to JSON** - Download entities for review

---

## Testing Checklist

- [ ] Tabs switch correctly
- [ ] Search filters entities
- [ ] Classification badges show correct colors
- [ ] Export JSON downloads file
- [ ] Entity counts update in tab badges
- [ ] Metadata displays correctly

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐ Medium
**Build Time:** 15-20 minutes with Lovable

---
---

# 07_gap_analysis_screen/prompt.md

# Gap Analysis Screen

**Lovable Build Time:** 20-25 minutes | **Complexity:** ⭐⭐⭐ Complex

---

## Lovable Initiation Phrase

```
Build a Gap Analysis Screen with side-by-side comparison.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui

Features:
- Two-column layout (NEW entities vs EXISTING library)
- Side-by-side diff comparison
- Approve/Reject/Update buttons for each entity
- Conflict highlighting
- Bulk actions (approve all NEW, reject duplicates)
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `extracted_entities` + `gap_analysis_results` tables

Follow complete spec below ⬇️
```

---

## Overview

Gap Analysis Screen handles Phase 3 processing:
- Compare extracted entities with existing knowledge
- Identify truly NEW entities
- Detect EXISTING duplicates
- Flag entities needing UPDATES
- User approval workflow
- Conflict resolution

Used in **Video Processing App** for Phase 3 (Gap Analysis).

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Card, Button, Badge, Dialog components)
- **React Hook Form** (approval forms)
- **Zod** (validation)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockGapAnalysis.ts

export const MOCK_GAP_ANALYSIS = [
  {
    id: '1',
    extracted_entity_id: '1',
    entity_name: 'Claude Desktop',
    entity_type: 'TOOL',
    classification: 'NEW',
    existing_match: null,
    confidence: 0.95,
    differences: [],
    recommendation: 'ADD_NEW',
    extracted_data: {
      name: 'Claude Desktop',
      category: 'AI',
      description: 'Desktop application for Claude AI with MCP server support',
      pricing: 'Free + Pro ($20/mo)',
      platform: 'Desktop (Mac/Windows)'
    },
    existing_data: null
  },
  {
    id: '2',
    extracted_entity_id: '2',
    entity_name: 'n8n',
    entity_type: 'TOOL',
    classification: 'EXISTING',
    existing_match: 'TOOL-AUTOMATION-112',
    confidence: 0.98,
    differences: [],
    recommendation: 'SKIP_DUPLICATE',
    extracted_data: {
      name: 'n8n',
      category: 'AUTOMATION',
      description: 'Workflow automation platform for developers',
      pricing: 'Self-hosted free, Cloud from $20/mo'
    },
    existing_data: {
      name: 'n8n',
      category: 'AUTOMATION',
      description: 'Workflow automation tool with visual editor',
      pricing: 'Free self-hosted'
    }
  },
  {
    id: '3',
    extracted_entity_id: '4',
    entity_name: 'Zapier',
    entity_type: 'TOOL',
    classification: 'UPDATE',
    existing_match: 'TOOL-AUTOMATION-005',
    confidence: 0.92,
    differences: [
      {
        field: 'pricing',
        existing_value: 'Starts at $20/mo',
        new_value: 'Free tier + paid from $29.99/mo'
      },
      {
        field: 'features',
        existing_value: '5,000+ integrations',
        new_value: '7,000+ integrations, AI-powered workflows'
      }
    ],
    recommendation: 'UPDATE_EXISTING',
    extracted_data: {
      name: 'Zapier',
      category: 'AUTOMATION',
      description: 'No-code automation platform with AI features',
      pricing: 'Free tier + paid from $29.99/mo',
      features: '7,000+ integrations, AI-powered workflows'
    },
    existing_data: {
      name: 'Zapier',
      category: 'AUTOMATION',
      description: 'No-code automation platform',
      pricing: 'Starts at $20/mo',
      features: '5,000+ integrations'
    }
  }
];

export type ApprovalAction = 'APPROVE_NEW' | 'SKIP_DUPLICATE' | 'APPROVE_UPDATE' | 'REJECT' | 'MANUAL_REVIEW';
```

---

## Database Schema

```sql
CREATE TABLE gap_analysis_results (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  extracted_entity_id UUID REFERENCES extracted_entities(id),
  entity_name TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  classification TEXT NOT NULL, -- 'NEW', 'EXISTING', 'UPDATE'
  existing_match TEXT, -- ID of matching entity in library
  confidence DECIMAL,
  differences JSONB, -- Array of field-level differences
  recommendation TEXT, -- 'ADD_NEW', 'SKIP_DUPLICATE', 'UPDATE_EXISTING'

  -- User approval
  user_action TEXT, -- 'APPROVE_NEW', 'SKIP_DUPLICATE', 'APPROVE_UPDATE', 'REJECT', 'MANUAL_REVIEW'
  approved_by TEXT, -- employee email
  approved_at TIMESTAMPTZ,
  notes TEXT,

  extracted_data JSONB,
  existing_data JSONB
);

CREATE INDEX idx_gap_classification ON gap_analysis_results(classification);
CREATE INDEX idx_gap_user_action ON gap_analysis_results(user_action);
```

---

## Component Structure with User Input

```typescript
// src/components/GapAnalysisScreen.tsx

import { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

const approvalSchema = z.object({
  action: z.enum(['APPROVE_NEW', 'SKIP_DUPLICATE', 'APPROVE_UPDATE', 'REJECT', 'MANUAL_REVIEW']),
  notes: z.string().optional()
});

type ApprovalFormData = z.infer<typeof approvalSchema>;

export function GapAnalysisScreen() {
  const [selectedEntity, setSelectedEntity] = useState<any>(null);
  const [isApprovalDialogOpen, setIsApprovalDialogOpen] = useState(false);
  const [filter, setFilter] = useState<'all' | 'NEW' | 'EXISTING' | 'UPDATE'>('all');

  const form = useForm<ApprovalFormData>({
    resolver: zodResolver(approvalSchema)
  });

  async function onApprove(data: ApprovalFormData) {
    // Update gap_analysis_results
    const { error } = await supabase
      .from('gap_analysis_results')
      .update({
        user_action: data.action,
        approved_by: 'current_user@example.com',
        approved_at: new Date().toISOString(),
        notes: data.notes
      })
      .eq('id', selectedEntity.id);

    if (!error) {
      setIsApprovalDialogOpen(false);
      setSelectedEntity(null);
      form.reset();
    }
  }

  function openApprovalDialog(entity: any, suggestedAction: string) {
    setSelectedEntity(entity);
    form.setValue('action', suggestedAction as any);
    setIsApprovalDialogOpen(true);
  }

  // Get classification color
  function getClassificationColor(classification: string) {
    switch (classification) {
      case 'NEW': return 'bg-green-500';
      case 'EXISTING': return 'bg-gray-500';
      case 'UPDATE': return 'bg-yellow-500';
      default: return 'bg-blue-500';
    }
  }

  const filteredEntities = MOCK_GAP_ANALYSIS.filter(entity =>
    filter === 'all' || entity.classification === filter
  );

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Gap Analysis</h1>
          <p className="text-gray-600">
            Review extracted entities and approve changes (Phase 3)
          </p>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="flex gap-2">
        {['all', 'NEW', 'EXISTING', 'UPDATE'].map(f => (
          <Button
            key={f}
            variant={filter === f ? 'default' : 'outline'}
            onClick={() => setFilter(f as any)}
          >
            {f === 'all' ? 'All' : f}
            {f !== 'all' && (
              <Badge variant="secondary" className="ml-2">
                {MOCK_GAP_ANALYSIS.filter(e => e.classification === f).length}
              </Badge>
            )}
          </Button>
        ))}
      </div>

      {/* Entity Comparison Cards */}
      <div className="space-y-4">
        {filteredEntities.map(entity => (
          <Card key={entity.id} className="p-6">
            {/* Header */}
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <h3 className="text-lg font-semibold">{entity.entity_name}</h3>
                <Badge className={getClassificationColor(entity.classification)}>
                  {entity.classification}
                </Badge>
                <Badge variant="outline">{entity.entity_type}</Badge>
              </div>
              <Badge variant="secondary">
                Confidence: {(entity.confidence * 100).toFixed(0)}%
              </Badge>
            </div>

            {/* Two-Column Comparison */}
            <div className="grid grid-cols-2 gap-6">
              {/* Left: Extracted Data */}
              <div className="border rounded-lg p-4 bg-green-50">
                <h4 className="font-semibold mb-3 text-green-800">
                  Extracted from Video
                </h4>
                <dl className="space-y-2 text-sm">
                  {Object.entries(entity.extracted_data).map(([key, value]) => (
                    <div key={key}>
                      <dt className="font-medium text-gray-700">{key}:</dt>
                      <dd className="text-gray-900">{value as string}</dd>
                    </div>
                  ))}
                </dl>
              </div>

              {/* Right: Existing Data (if any) */}
              <div className={`border rounded-lg p-4 ${
                entity.existing_data ? 'bg-blue-50' : 'bg-gray-50'
              }`}>
                <h4 className="font-semibold mb-3 text-blue-800">
                  {entity.existing_data ? 'Existing in Library' : 'No Match Found'}
                </h4>
                {entity.existing_data ? (
                  <dl className="space-y-2 text-sm">
                    {Object.entries(entity.existing_data).map(([key, value]) => (
                      <div key={key}>
                        <dt className="font-medium text-gray-700">{key}:</dt>
                        <dd className={`${
                          entity.differences?.some((d: any) => d.field === key)
                            ? 'text-yellow-700 font-semibold'
                            : 'text-gray-900'
                        }`}>
                          {value as string}
                        </dd>
                      </div>
                    ))}
                  </dl>
                ) : (
                  <p className="text-sm text-gray-500">
                    This entity does not exist in the current library.
                  </p>
                )}
              </div>
            </div>

            {/* Differences Highlight */}
            {entity.differences && entity.differences.length > 0 && (
              <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded">
                <h5 className="font-semibold text-yellow-800 mb-2">
                  Detected Changes:
                </h5>
                <ul className="text-sm space-y-1">
                  {entity.differences.map((diff: any, idx: number) => (
                    <li key={idx}>
                      <strong>{diff.field}:</strong>{' '}
                      <span className="line-through text-gray-500">
                        {diff.existing_value}
                      </span>{' '}
                      → <span className="text-green-700">{diff.new_value}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Action Buttons */}
            <div className="mt-4 flex gap-2">
              {entity.classification === 'NEW' && (
                <Button
                  onClick={() => openApprovalDialog(entity, 'APPROVE_NEW')}
                  className="bg-green-600 hover:bg-green-700"
                >
                  Approve New
                </Button>
              )}
              {entity.classification === 'EXISTING' && (
                <Button
                  onClick={() => openApprovalDialog(entity, 'SKIP_DUPLICATE')}
                  variant="outline"
                >
                  Skip Duplicate
                </Button>
              )}
              {entity.classification === 'UPDATE' && (
                <Button
                  onClick={() => openApprovalDialog(entity, 'APPROVE_UPDATE')}
                  className="bg-yellow-600 hover:bg-yellow-700"
                >
                  Approve Update
                </Button>
              )}
              <Button
                onClick={() => openApprovalDialog(entity, 'REJECT')}
                variant="destructive"
              >
                Reject
              </Button>
              <Button
                onClick={() => openApprovalDialog(entity, 'MANUAL_REVIEW')}
                variant="outline"
              >
                Flag for Review
              </Button>
            </div>
          </Card>
        ))}
      </div>

      {/* Approval Dialog */}
      <Dialog open={isApprovalDialogOpen} onOpenChange={setIsApprovalDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Confirm Action</DialogTitle>
          </DialogHeader>
          <form onSubmit={form.handleSubmit(onApprove)} className="space-y-4">
            <div>
              <p className="text-sm mb-2">
                You are about to <strong>{form.watch('action')?.replace('_', ' ')}</strong> for:
              </p>
              <p className="font-semibold">{selectedEntity?.entity_name}</p>
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">
                Notes (optional)
              </label>
              <Textarea
                {...form.register('notes')}
                placeholder="Add any notes or comments..."
                rows={3}
              />
            </div>

            <div className="flex gap-2">
              <Button type="submit">Confirm</Button>
              <Button
                type="button"
                variant="outline"
                onClick={() => setIsApprovalDialogOpen(false)}
              >
                Cancel
              </Button>
            </div>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  );
}
```

---

## Features

1. **Side-by-Side Comparison** - Extracted vs Existing data
2. **Difference Highlighting** - Visual change indicators
3. **Approval Workflow** - Multiple action types with notes
4. **Filter by Classification** - NEW/EXISTING/UPDATE tabs
5. **Conflict Resolution** - User decision on each entity

---

## Testing Checklist

- [ ] Comparison displays correctly
- [ ] Differences highlighted in yellow
- [ ] Approval buttons trigger dialog
- [ ] Notes field saves correctly
- [ ] Filter tabs work
- [ ] User action updates database
- [ ] Confidence scores display

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐⭐ Complex
**Build Time:** 20-25 minutes with Lovable

---
---

# 08_progress_tracker_widget/prompt.md

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

---
---

# 10_knowledge_map_viewer/prompt.md

# Knowledge Map Viewer

**Lovable Build Time:** 25-30 minutes | **Complexity:** ⭐⭐⭐ Complex

---

## Lovable Initiation Phrase

```
Build a Knowledge Map Viewer with interactive graph visualization.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + React Flow

Features:
- Interactive node graph (Tools, Workflows, Actions, Objects)
- Zoom and pan controls
- Node detail panels on click
- Relationship edges (uses, contains, requires)
- Filter by entity type
- Export graph as PNG
- AdminRHS-AI-Catalog design (blue theme)

Database: Supabase `extracted_entities` + `entity_relationships` tables

Follow complete spec below ⬇️
```

---

## Overview

Knowledge Map Viewer displays Phase 5 results:
- Visualize entity relationships as graph
- Interactive exploration of knowledge structure
- Click nodes for details
- Filter and search entities
- Export visualization
- Used in **Video Processing App** for Phase 5 (Knowledge Mapping)

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Card, Button, Badge components)
- **React Flow** (graph visualization)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockKnowledgeGraph.ts

export const MOCK_NODES = [
  {
    id: 'TOOL-AI-224',
    type: 'tool',
    data: {
      label: 'Claude Desktop',
      category: 'AI',
      description: 'Desktop application for Claude AI'
    },
    position: { x: 250, y: 100 }
  },
  {
    id: 'WRF-026',
    type: 'workflow',
    data: {
      label: 'MCP Server Setup Process',
      steps: 8
    },
    position: { x: 250, y: 250 }
  },
  {
    id: 'ACTION-434',
    type: 'action',
    data: {
      label: 'Install MCP Server',
      difficulty: 'Medium'
    },
    position: { x: 100, y: 400 }
  },
  {
    id: 'ACTION-435',
    type: 'action',
    data: {
      label: 'Configure Settings',
      difficulty: 'Easy'
    },
    position: { x: 400, y: 400 }
  },
  {
    id: 'OBJ-AI-089',
    type: 'object',
    data: {
      label: 'MCP Configuration File',
      file_type: '.json'
    },
    position: { x: 250, y: 550 }
  },
  {
    id: 'TOOL-AUTOMATION-112',
    type: 'tool',
    data: {
      label: 'n8n',
      category: 'AUTOMATION'
    },
    position: { x: 600, y: 100 }
  },
  {
    id: 'WRF-027',
    type: 'workflow',
    data: {
      label: 'Automated Data Sync',
      steps: 5
    },
    position: { x: 600, y: 250 }
  }
];

export const MOCK_EDGES = [
  {
    id: 'e1',
    source: 'TOOL-AI-224',
    target: 'WRF-026',
    type: 'default',
    label: 'uses',
    animated: true
  },
  {
    id: 'e2',
    source: 'WRF-026',
    target: 'ACTION-434',
    type: 'default',
    label: 'contains'
  },
  {
    id: 'e3',
    source: 'WRF-026',
    target: 'ACTION-435',
    type: 'default',
    label: 'contains'
  },
  {
    id: 'e4',
    source: 'ACTION-435',
    target: 'OBJ-AI-089',
    type: 'default',
    label: 'requires'
  },
  {
    id: 'e5',
    source: 'TOOL-AUTOMATION-112',
    target: 'WRF-027',
    type: 'default',
    label: 'uses',
    animated: true
  }
];

export const NODE_COLORS = {
  tool: '#428eb4',      // Blue (tools)
  workflow: '#34D399',  // Green (workflows)
  action: '#FBBF24',    // Yellow (actions)
  object: '#A78BFA'     // Purple (objects)
};
```

---

## Database Schema

```sql
CREATE TABLE entity_relationships (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  source_entity_id TEXT NOT NULL,
  target_entity_id TEXT NOT NULL,
  relationship_type TEXT NOT NULL, -- 'uses', 'contains', 'requires', 'relates_to'
  video_id UUID REFERENCES video_queue(id),
  confidence_score DECIMAL,
  metadata JSONB
);

CREATE INDEX idx_entity_rel_source ON entity_relationships(source_entity_id);
CREATE INDEX idx_entity_rel_target ON entity_relationships(target_entity_id);
```

---

## Component Structure

```typescript
// src/components/KnowledgeMapViewer.tsx

import { useState, useCallback } from 'react';
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  Panel,
  Node,
  Edge
} from 'reactflow';
import 'reactflow/dist/style.css';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Download, Filter } from 'lucide-react';

export function KnowledgeMapViewer() {
  const [nodes, setNodes, onNodesChange] = useNodesState(MOCK_NODES);
  const [edges, setEdges, onEdgesChange] = useEdgesState(MOCK_EDGES);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [entityTypeFilter, setEntityTypeFilter] = useState<string[]>([]);

  // Handle node click
  const onNodeClick = useCallback((event: React.MouseEvent, node: Node) => {
    setSelectedNode(node);
  }, []);

  // Filter nodes by entity type
  const filteredNodes = nodes.filter(node => {
    if (entityTypeFilter.length === 0) return true;
    return entityTypeFilter.includes(node.type!);
  });

  // Filter edges based on visible nodes
  const filteredEdges = edges.filter(edge => {
    const sourceVisible = filteredNodes.some(n => n.id === edge.source);
    const targetVisible = filteredNodes.some(n => n.id === edge.target);
    return sourceVisible && targetVisible;
  });

  // Toggle entity type filter
  function toggleFilter(type: string) {
    setEntityTypeFilter(prev =>
      prev.includes(type)
        ? prev.filter(t => t !== type)
        : [...prev, type]
    );
  }

  // Export as PNG
  function exportGraph() {
    // Implementation using html-to-image or similar
    console.log('Exporting graph as PNG...');
  }

  // Custom node styling
  const nodeTypes = {
    tool: ({ data }: any) => (
      <div className="px-4 py-2 shadow-lg rounded-lg border-2" style={{
        backgroundColor: '#fff',
        borderColor: NODE_COLORS.tool
      }}>
        <div className="font-semibold text-sm">{data.label}</div>
        <div className="text-xs text-gray-500">{data.category}</div>
      </div>
    ),
    workflow: ({ data }: any) => (
      <div className="px-4 py-2 shadow-lg rounded-lg border-2" style={{
        backgroundColor: '#fff',
        borderColor: NODE_COLORS.workflow
      }}>
        <div className="font-semibold text-sm">{data.label}</div>
        <div className="text-xs text-gray-500">{data.steps} steps</div>
      </div>
    ),
    action: ({ data }: any) => (
      <div className="px-4 py-2 shadow-lg rounded-lg border-2" style={{
        backgroundColor: '#fff',
        borderColor: NODE_COLORS.action
      }}>
        <div className="font-semibold text-sm">{data.label}</div>
        <div className="text-xs text-gray-500">{data.difficulty}</div>
      </div>
    ),
    object: ({ data }: any) => (
      <div className="px-4 py-2 shadow-lg rounded-lg border-2" style={{
        backgroundColor: '#fff',
        borderColor: NODE_COLORS.object
      }}>
        <div className="font-semibold text-sm">{data.label}</div>
        <div className="text-xs text-gray-500">{data.file_type}</div>
      </div>
    )
  };

  return (
    <div className="h-screen flex">
      {/* Graph Canvas */}
      <div className="flex-1 relative">
        <ReactFlow
          nodes={filteredNodes}
          edges={filteredEdges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onNodeClick={onNodeClick}
          nodeTypes={nodeTypes}
          fitView
        >
          <Controls />
          <MiniMap
            nodeColor={(node) => NODE_COLORS[node.type as keyof typeof NODE_COLORS]}
          />
          <Background gap={12} size={1} />

          {/* Filter Panel */}
          <Panel position="top-left">
            <Card className="p-4 w-64">
              <h3 className="font-semibold mb-3 flex items-center gap-2">
                <Filter className="w-4 h-4" />
                Filter by Type
              </h3>
              <div className="space-y-2">
                {['tool', 'workflow', 'action', 'object'].map(type => (
                  <label key={type} className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={entityTypeFilter.length === 0 || entityTypeFilter.includes(type)}
                      onChange={() => toggleFilter(type)}
                    />
                    <span
                      className="w-4 h-4 rounded"
                      style={{ backgroundColor: NODE_COLORS[type as keyof typeof NODE_COLORS] }}
                    />
                    <span className="text-sm capitalize">{type}s</span>
                  </label>
                ))}
              </div>

              <Button
                variant="outline"
                size="sm"
                className="w-full mt-4"
                onClick={exportGraph}
              >
                <Download className="w-4 h-4 mr-2" />
                Export PNG
              </Button>
            </Card>
          </Panel>
        </ReactFlow>
      </div>

      {/* Node Detail Sidebar */}
      {selectedNode && (
        <div className="w-80 border-l bg-white p-6 overflow-y-auto">
          <h2 className="text-xl font-bold mb-4">Node Details</h2>

          <Badge
            className="mb-4"
            style={{ backgroundColor: NODE_COLORS[selectedNode.type as keyof typeof NODE_COLORS] }}
          >
            {selectedNode.type?.toUpperCase()}
          </Badge>

          <Card className="p-4">
            <h3 className="font-semibold text-lg mb-3">
              {selectedNode.data.label}
            </h3>

            <dl className="space-y-2 text-sm">
              <div>
                <dt className="font-medium text-gray-700">ID:</dt>
                <dd className="text-gray-900">{selectedNode.id}</dd>
              </div>

              {Object.entries(selectedNode.data).map(([key, value]) => {
                if (key === 'label') return null;
                return (
                  <div key={key}>
                    <dt className="font-medium text-gray-700 capitalize">
                      {key.replace(/_/g, ' ')}:
                    </dt>
                    <dd className="text-gray-900">{value as string}</dd>
                  </div>
                );
              })}
            </dl>
          </Card>

          {/* Connected Nodes */}
          <div className="mt-6">
            <h4 className="font-semibold mb-2">Connections</h4>
            <div className="space-y-2">
              {edges
                .filter(e => e.source === selectedNode.id || e.target === selectedNode.id)
                .map(edge => {
                  const otherNodeId = edge.source === selectedNode.id ? edge.target : edge.source;
                  const otherNode = nodes.find(n => n.id === otherNodeId);

                  return (
                    <Card key={edge.id} className="p-2">
                      <div className="text-xs text-gray-600">{edge.label}</div>
                      <div className="text-sm font-medium">{otherNode?.data.label}</div>
                    </Card>
                  );
                })}
            </div>
          </div>

          <Button
            variant="outline"
            className="w-full mt-6"
            onClick={() => setSelectedNode(null)}
          >
            Close
          </Button>
        </div>
      )}
    </div>
  );
}
```

---

## Features

1. **Interactive Graph** - Zoom, pan, drag nodes
2. **Custom Node Styling** - Color-coded by entity type
3. **Node Details Panel** - Click to view full information
4. **Relationship Edges** - Labeled connections (uses, contains, requires)
5. **Type Filtering** - Show/hide entity types
6. **Export Graph** - Download as PNG

---

## Testing Checklist

- [ ] Graph renders correctly
- [ ] Zoom and pan work smoothly
- [ ] Node click shows details
- [ ] Filters hide/show nodes correctly
- [ ] Edges connect properly
- [ ] Export PNG downloads file
- [ ] Mini-map displays graph overview

---

**Created:** 2025-11-28
**Complexity:** ⭐⭐⭐ Complex
**Build Time:** 25-30 minutes with Lovable

---
---

# All 7 Prompts Complete!

**Next Steps:**
1. Copy each section above into its respective folder's `prompt.md` file, OR
2. Keep this consolidated file and split later

**Total Screens:** 10 (3 previously completed + 7 new = 10/10 ✓)

**All prompts include:**
- ✅ Lovable initiation phrases
- ✅ Complete sample mock data
- ✅ Database schemas
- ✅ Component code with user input forms and validation
- ✅ Feature lists
- ✅ Testing checklists
- ✅ AdminRHS-AI-Catalog design integration

**Ready to build with Lovable AI!** 🚀
