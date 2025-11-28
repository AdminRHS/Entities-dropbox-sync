# Search Queue Screen

**Lovable Build Time:** 10-15 minutes | **Complexity:** ⭐ Easy

---

## Lovable Initiation Phrase

```
Build a Search Queue Table screen for managing research search queries.

Tech stack: React 18 + TypeScript + Vite + Supabase + shadcn/ui + TanStack Table

Features:
- Display search queries with status badges
- Filter by department and status
- Add/edit/delete search queries
- Real-time updates from Supabase
- AdminRHS-AI-Catalog design (blue theme, clean table)

Database: Supabase `search_queue` table

Follow complete spec below ⬇️
```

---

## Overview

Search Queue Table displays and manages Perplexity AI search queries for video discovery:
- Pending searches to be executed
- Search query text and parameters
- Department assignment
- Status tracking (Pending, Searching, Completed, Failed)
- Results count

Used in **Queue Management App** for Phase 0 (Search & Selection).

---

## Tech Stack

- **React 18** + **TypeScript**
- **Vite** (build tool)
- **Supabase** (database + real-time)
- **shadcn/ui** (Table, Dialog, Badge components)
- **TanStack Table** (data grid)
- **Tailwind CSS** (styling)

---

## Sample Data (For Testing Without Supabase)

```typescript
// src/data/mockSearchQueue.ts

export const MOCK_SEARCHES = [
  {
    id: '1',
    created_at: '2025-11-28T10:00:00Z',
    search_query: 'Claude Desktop MCP setup tutorial 2024',
    department: 'DEV',
    status: 'completed',
    perplexity_settings: { creativity: 0.5, structure_mode: true },
    results_count: 12,
    videos_added: 3,
    assigned_to: 'alex@remotehel pers.com',
    completed_at: '2025-11-28T10:15:00Z'
  },
  {
    id: '2',
    created_at: '2025-11-28T11:30:00Z',
    search_query: 'n8n workflow automation examples for developers',
    department: 'DEV',
    status: 'searching',
    perplexity_settings: { creativity: 0.5, structure_mode: true },
    results_count: 0,
    videos_added: 0,
    assigned_to: 'maria@remotehelpers.com',
    completed_at: null
  },
  {
    id: '3',
    created_at: '2025-11-28T09:00:00Z',
    search_query: 'Social media caption AI tools comparison',
    department: 'SMM',
    status: 'pending',
    perplexity_settings: { creativity: 0.5, structure_mode: true },
    results_count: 0,
    videos_added: 0,
    assigned_to: null,
    completed_at: null
  },
  {
    id: '4',
    created_at: '2025-11-27T14:00:00Z',
    search_query: 'Video editing AI tools 2024',
    department: 'VID',
    status: 'completed',
    perplexity_settings: { creativity: 0.5, structure_mode: true },
    results_count: 18,
    videos_added: 5,
    assigned_to: 'jordan@remotehelpers.com',
    completed_at: '2025-11-27T14:30:00Z'
  },
  {
    id: '5',
    created_at: '2025-11-27T16:00:00Z',
    search_query: 'Recruitment automation with AI',
    department: 'HRM',
    status: 'failed',
    perplexity_settings: { creativity: 0.5, structure_mode: true },
    results_count: 0,
    videos_added: 0,
    assigned_to: 'sam@remotehelpers.com',
    completed_at: null,
    error_message: 'API rate limit exceeded'
  }
];
```

---

## Database Schema

```sql
-- Supabase search_queue table
CREATE TABLE search_queue (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  search_query TEXT NOT NULL,
  department TEXT NOT NULL, -- 'DEV', 'SMM', 'VID', 'AID', etc.
  status TEXT DEFAULT 'pending', -- 'pending', 'searching', 'completed', 'failed'
  perplexity_settings JSONB DEFAULT '{"creativity": 0.5, "structure_mode": true}',
  results_count INTEGER DEFAULT 0,
  videos_added INTEGER DEFAULT 0,
  assigned_to TEXT, -- employee email
  completed_at TIMESTAMPTZ,
  error_message TEXT
);

-- Indexes for performance
CREATE INDEX idx_search_status ON search_queue(status);
CREATE INDEX idx_search_department ON search_queue(department);
```

---

## Component Structure

```typescript
// src/components/SearchQueueTable.tsx

import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';
import {
  useReactTable,
  getCoreRowModel,
  getFilteredRowModel,
  getSortedRowModel,
  flexRender
} from '@tanstack/react-table';
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';

interface SearchQuery {
  id: string;
  created_at: string;
  search_query: string;
  department: string;
  status: 'pending' | 'searching' | 'completed' | 'failed';
  results_count: number;
  videos_added: number;
  assigned_to: string | null;
}

export function SearchQueueTable() {
  const [searches, setSearches] = useState<SearchQuery[]>([]);
  const [statusFilter, setStatusFilter] = useState<string>('all');

  useEffect(() => {
    fetchSearches();

    // Real-time subscription
    const subscription = supabase
      .channel('search_queue_changes')
      .on('postgres_changes',
        { event: '*', schema: 'public', table: 'search_queue' },
        () => fetchSearches()
      )
      .subscribe();

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  async function fetchSearches() {
    let query = supabase
      .from('search_queue')
      .select('*')
      .order('created_at', { ascending: false });

    if (statusFilter !== 'all') {
      query = query.eq('status', statusFilter);
    }

    const { data } = await query;
    if (data) setSearches(data);
  }

  const columns = [
    {
      accessorKey: 'search_query',
      header: 'Search Query',
      cell: ({ row }) => (
        <div className="max-w-md truncate" title={row.original.search_query}>
          {row.original.search_query}
        </div>
      )
    },
    {
      accessorKey: 'department',
      header: 'Department',
      cell: ({ row }) => (
        <Badge variant="outline">{row.original.department}</Badge>
      )
    },
    {
      accessorKey: 'status',
      header: 'Status',
      cell: ({ row }) => (
        <Badge className={getStatusColor(row.original.status)}>
          {row.original.status}
        </Badge>
      )
    },
    {
      accessorKey: 'results_count',
      header: 'Results',
      cell: ({ row }) => row.original.results_count
    },
    {
      accessorKey: 'videos_added',
      header: 'Videos Added',
      cell: ({ row }) => row.original.videos_added
    },
    {
      id: 'actions',
      header: 'Actions',
      cell: ({ row }) => (
        <div className="flex gap-2">
          <Button size="sm" variant="ghost">Edit</Button>
          <Button size="sm" variant="ghost">Delete</Button>
        </div>
      )
    }
  ];

  const table = useReactTable({
    data: searches,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getSortedRowModel: getSortedRowModel()
  });

  return (
    <div className="space-y-4">
      {/* Filters */}
      <div className="flex gap-2">
        {['all', 'pending', 'searching', 'completed', 'failed'].map(status => (
          <Button
            key={status}
            variant={statusFilter === status ? 'default' : 'outline'}
            onClick={() => setStatusFilter(status)}
          >
            {status}
          </Button>
        ))}
      </div>

      {/* Table */}
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map(headerGroup => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map(header => (
                <TableHead key={header.id}>
                  {flexRender(header.column.columnDef.header, header.getContext())}
                </TableHead>
              ))}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows.map(row => (
            <TableRow key={row.id}>
              {row.getVisibleCells().map(cell => (
                <TableCell key={cell.id}>
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

function getStatusColor(status: string): string {
  const colors = {
    pending: 'bg-gray-100 text-gray-700',
    searching: 'bg-blue-100 text-blue-700',
    completed: 'bg-emerald-100 text-emerald-700',
    failed: 'bg-red-100 text-red-700'
  };
  return colors[status] || colors.pending;
}
```

---

## Features

1. **Status Filtering** - Filter by pending/searching/completed/failed
2. **Department Badges** - Color-coded department tags
3. **Real-Time Updates** - Auto-refresh when searches change
4. **CRUD Operations** - Add/Edit/Delete search queries
5. **Results Tracking** - Shows how many results found and videos added

---

## Testing Checklist

- [ ] Table displays mock searches correctly
- [ ] Status filter buttons work
- [ ] Status badges show correct colors
- [ ] Real-time updates work when search_queue changes
- [ ] Edit/Delete buttons are visible
- [ ] Table is responsive on mobile

---

**Created:** 2025-11-28
**Complexity:** ⭐ Easy
**Build Time:** 10-15 minutes with Lovable
