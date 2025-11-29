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
