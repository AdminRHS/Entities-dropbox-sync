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
