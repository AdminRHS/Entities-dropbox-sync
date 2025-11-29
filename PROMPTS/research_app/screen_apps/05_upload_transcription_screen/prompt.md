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
