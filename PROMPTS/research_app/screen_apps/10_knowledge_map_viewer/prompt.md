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
