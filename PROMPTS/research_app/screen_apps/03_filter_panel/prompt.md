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
