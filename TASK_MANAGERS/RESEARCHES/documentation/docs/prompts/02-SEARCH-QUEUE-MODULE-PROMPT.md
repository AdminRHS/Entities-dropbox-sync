# PROMPT: Search Queue Module

**Purpose:** Generate Search Queue module with full functionality

---

## TASK

Create Search Queue module for RESEARCHES 2 with the following components and functionality.

**Design:** Follow the style of https://adminrhs.github.io/Video-catalog/
**Design System:** https://adminrhs.github.io/Design-system/
**Module Color:** `--color-search: #6D28D9` (Designers - Deep Purple from Design System)

**Important:** Use exact values from the design system:
- **Typography:** Roboto (weights: 300, 400, 500, 600, 700)
- **Colors:** Exact hex codes from Design System
- **Spacing:** 4px base unit (xs/sm/md/lg/xl/2xl/3xl)
- **Border Radius:** 8px (buttons), 12px (cards)
- **Shadows:** light/card/medium/heavy from Design System
- **Transitions:** 150ms (fast), 300ms (normal), 500ms (slow)
- **Z-Index:** Use layers from Design System (dropdown: 1000, modal: 1050)

---

## 1. COMPONENTS

### SearchQueueDashboard.tsx

```tsx
import React from 'react';
import { SearchTaskCard } from './SearchTaskCard';
import { CreateSearchTaskModal } from './CreateSearchTaskModal';
import { SearchResultsModal } from './SearchResultsModal';

interface SearchTask {
  search_id: string;
  employee: string;
  department: string;
  topic: string;
  search_query?: string;
  status: 'Assigned' | 'In_Progress' | 'Completed';
  date_assigned: string;
  videos_found: number;
  date_completed?: string;
  notes?: string;
}

export function SearchQueueDashboard() {
  const [tasks, setTasks] = React.useState<SearchTask[]>([]);
  const [isCreateModalOpen, setIsCreateModalOpen] = React.useState(false);
  const [resultsModalData, setResultsModalData] = React.useState(null);

  // Filters
  const [statusFilter, setStatusFilter] = React.useState('All');
  const [departmentFilter, setDepartmentFilter] = React.useState('All');

  return (
    <div className="container mx-auto p-8">
      {/* Header */}
      <header className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-[var(--text-primary)] mb-2">
            Search Queue
          </h1>
          <p className="text-sm text-[var(--text-secondary)]">
            Manage video search tasks and assignments
          </p>
        </div>
        <button
          onClick={() => setIsCreateModalOpen(true)}
          className="btn-primary flex items-center gap-2"
        >
          <span>➕</span>
          <span>New Search Task</span>
        </button>
      </header>

      {/* Filters */}
      <div className="flex items-center gap-3 mb-6">
        <div className="filter-group">
          <button
            className={`filter-button ${statusFilter === 'All' ? 'active department-search' : ''}`}
            onClick={() => setStatusFilter('All')}
          >
            All
          </button>
          <button
            className={`filter-button ${statusFilter === 'Assigned' ? 'active department-search' : ''}`}
            onClick={() => setStatusFilter('Assigned')}
          >
            Assigned
          </button>
          <button
            className={`filter-button ${statusFilter === 'In_Progress' ? 'active department-search' : ''}`}
            onClick={() => setStatusFilter('In_Progress')}
          >
            In Progress
          </button>
          <button
            className={`filter-button ${statusFilter === 'Completed' ? 'active department-search' : ''}`}
            onClick={() => setStatusFilter('Completed')}
          >
            Completed
          </button>
        </div>
      </div>

      {/* Tasks Grid */}
      <div className="grid gap-6">
        {tasks.map(task => (
          <SearchTaskCard
            key={task.search_id}
            task={task}
            onExecute={handleExecuteSearch}
            onComplete={handleCompleteTask}
          />
        ))}
      </div>

      {/* Modals */}
      <CreateSearchTaskModal
        isOpen={isCreateModalOpen}
        onClose={() => setIsCreateModalOpen(false)}
        onCreate={handleCreateTask}
      />

      {resultsModalData && (
        <SearchResultsModal
          data={resultsModalData}
          onClose={() => setResultsModalData(null)}
          onAddToQueue={handleAddToVideoQueue}
        />
      )}
    </div>
  );
}
```

### SearchTaskCard.tsx

```tsx
interface SearchTaskCardProps {
  task: SearchTask;
  onExecute: (taskId: string) => void;
  onComplete: (taskId: string) => void;
}

export function SearchTaskCard({ task, onExecute, onComplete }: SearchTaskCardProps) {
  return (
    <div className="search-task-card group">
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <span className="text-sm font-bold text-[var(--color-search)]">
            {task.search_id}
          </span>
          <StatusBadge status={task.status} />
        </div>
        <button className="btn-icon opacity-0 group-hover:opacity-100">
          <span>⋮</span>
        </button>
      </div>

      {/* Content */}
      <h3 className="text-lg font-semibold text-[var(--text-primary)] mb-2">
        {task.topic}
      </h3>

      <div className="flex items-center gap-4 text-sm text-[var(--text-secondary)] mb-4">
        <span>👤 {task.employee}</span>
        <span>📁 {task.department}</span>
        <span>📅 {new Date(task.date_assigned).toLocaleDateString()}</span>
      </div>

      {/* Actions */}
      <div className="flex items-center gap-3">
        <button
          onClick={() => onExecute(task.search_id)}
          className="btn-primary btn-sm"
          disabled={task.status === 'Completed'}
        >
          🔍 Execute Search
        </button>
        <button className="btn-secondary btn-sm">
          👁️ View Details
        </button>
        {task.status !== 'Completed' && (
          <button
            onClick={() => onComplete(task.search_id)}
            className="btn-ghost btn-sm"
          >
            ✓ Complete
          </button>
        )}
      </div>
    </div>
  );
}
```

### CreateSearchTaskModal.tsx

```tsx
interface CreateSearchTaskModalProps {
  isOpen: boolean;
  onClose: () => void;
  onCreate: (task: Partial<SearchTask>) => void;
}

export function CreateSearchTaskModal({ isOpen, onClose, onCreate }: CreateSearchTaskModalProps) {
  const [formData, setFormData] = React.useState({
    employee: '',
    department: '',
    topic: '',
    search_type: '',
    custom_query: '',
    notes: ''
  });

  const searchTypes = [
    { id: 'PMT-048', name: 'Daily AI Tools', description: 'New AI tool launches and updates' },
    { id: 'PMT-089', name: 'Weekly Tutorials', description: 'Comprehensive AI tutorial series' },
    { id: 'PMT-093', name: 'Design AI Tools', description: 'AI design tool videos' },
    { id: 'PMT-098', name: 'Automation Examples', description: 'AI automation workflows' },
    { id: 'CUSTOM', name: 'Custom Search', description: 'Enter your own search query' }
  ];

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal modal-md" onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className="modal-header">
          <h2 className="modal-title">Create New Search Task</h2>
          <button className="modal-close" onClick={onClose}>✕</button>
        </div>

        {/* Body */}
        <div className="modal-body">
          <form className="flex flex-col gap-4">
            {/* Employee */}
            <div>
              <label className="text-label mb-2 block">Employee *</label>
              <select
                className="select"
                value={formData.employee}
                onChange={e => setFormData({ ...formData, employee: e.target.value })}
              >
                <option value="">Select Employee</option>
                <option value="John Doe">John Doe</option>
                <option value="Jane Smith">Jane Smith</option>
              </select>
            </div>

            {/* Department */}
            <div>
              <label className="text-label mb-2 block">Department *</label>
              <select
                className="select"
                value={formData.department}
                onChange={e => setFormData({ ...formData, department: e.target.value })}
              >
                <option value="">Select Department</option>
                <option value="AI">AI Department</option>
                <option value="Design">Design</option>
                <option value="Development">Development</option>
              </select>
            </div>

            {/* Topic */}
            <div>
              <label className="text-label mb-2 block">Topic *</label>
              <input
                type="text"
                className="input"
                placeholder="e.g., AI Tools, Design Automation..."
                value={formData.topic}
                onChange={e => setFormData({ ...formData, topic: e.target.value })}
              />
            </div>

            {/* Search Type */}
            <div>
              <label className="text-label mb-2 block">Search Type *</label>
              <select
                className="select"
                value={formData.search_type}
                onChange={e => setFormData({ ...formData, search_type: e.target.value })}
              >
                <option value="">Select Search Type</option>
                {searchTypes.map(type => (
                  <option key={type.id} value={type.id}>
                    {type.name} - {type.description}
                  </option>
                ))}
              </select>
            </div>

            {/* Custom Query (if CUSTOM selected) */}
            {formData.search_type === 'CUSTOM' && (
              <div>
                <label className="text-label mb-2 block">Custom Search Query</label>
                <textarea
                  className="textarea"
                  placeholder="Enter your YouTube search query..."
                  value={formData.custom_query}
                  onChange={e => setFormData({ ...formData, custom_query: e.target.value })}
                />
              </div>
            )}

            {/* Notes */}
            <div>
              <label className="text-label mb-2 block">Notes (optional)</label>
              <textarea
                className="textarea"
                placeholder="Add any additional notes..."
                value={formData.notes}
                onChange={e => setFormData({ ...formData, notes: e.target.value })}
              />
            </div>
          </form>
        </div>

        {/* Footer */}
        <div className="modal-footer">
          <button className="btn-secondary" onClick={onClose}>
            Cancel
          </button>
          <button
            className="btn-primary"
            onClick={() => {
              onCreate(formData);
              onClose();
            }}
          >
            Create & Execute
          </button>
        </div>
      </div>
    </div>
  );
}
```

### SearchResultsModal.tsx

```tsx
interface SearchResultsModalProps {
  data: {
    search_id: string;
    videos: Array<{
      youtube_url: string;
      title: string;
      channel: string;
      duration: string;
      views: number;
      upload_date: string;
      thumbnail: string;
      priority: number;
    }>;
  };
  onClose: () => void;
  onAddToQueue: (searchId: string, videoUrls: string[]) => void;
}

export function SearchResultsModal({ data, onClose, onAddToQueue }: SearchResultsModalProps) {
  const [selectedVideos, setSelectedVideos] = React.useState<Set<string>>(new Set());

  const toggleVideo = (url: string) => {
    const newSelected = new Set(selectedVideos);
    if (newSelected.has(url)) {
      newSelected.delete(url);
    } else {
      newSelected.add(url);
    }
    setSelectedVideos(newSelected);
  };

  const toggleAll = () => {
    if (selectedVideos.size === data.videos.length) {
      setSelectedVideos(new Set());
    } else {
      setSelectedVideos(new Set(data.videos.map(v => v.youtube_url)));
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal modal-lg search-results-modal" onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className="search-results-header">
          <div>
            <h2 className="search-results-title">
              Search Results - {data.search_id}
            </h2>
            <p className="search-results-subtitle">
              Found {data.videos.length} videos
            </p>
          </div>
          <button className="modal-close" onClick={onClose}>✕</button>
        </div>

        {/* Actions */}
        <div className="search-results-actions">
          <button
            className="btn-secondary btn-sm"
            onClick={toggleAll}
          >
            {selectedVideos.size === data.videos.length ? 'Deselect All' : 'Select All'}
          </button>
        </div>

        {/* Body */}
        <div className="search-results-body">
          <div className="search-results-list">
            {data.videos.map(video => (
              <div
                key={video.youtube_url}
                className={`search-result-item ${selectedVideos.has(video.youtube_url) ? 'selected' : ''}`}
                onClick={() => toggleVideo(video.youtube_url)}
              >
                <input
                  type="checkbox"
                  className="search-result-checkbox"
                  checked={selectedVideos.has(video.youtube_url)}
                  onChange={() => toggleVideo(video.youtube_url)}
                />

                <img
                  src={video.thumbnail}
                  alt={video.title}
                  className="search-result-thumbnail"
                />

                <div className="search-result-content">
                  <h4 className="search-result-title">{video.title}</h4>
                  <p className="search-result-channel">📺 {video.channel}</p>
                  <div className="search-result-meta">
                    <span>⏱ {video.duration}</span>
                    <span>👁 {(video.views / 1000).toFixed(1)}K views</span>
                    <span>📅 {new Date(video.upload_date).toLocaleDateString()}</span>
                  </div>
                </div>

                <div className="search-result-priority">
                  <PriorityBadge priority={video.priority} />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Footer */}
        <div className="search-results-footer">
          <p className="search-results-selected-count">
            {selectedVideos.size} video{selectedVideos.size !== 1 ? 's' : ''} selected
          </p>
          <div className="flex gap-3">
            <button className="btn-secondary" onClick={onClose}>
              Cancel
            </button>
            <button
              className="btn-primary"
              disabled={selectedVideos.size === 0}
              onClick={() => {
                onAddToQueue(data.search_id, Array.from(selectedVideos));
                onClose();
              }}
            >
              Add Selected to Video Queue ({selectedVideos.size})
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## 2. API INTEGRATION

```typescript
// src/services/searchQueueApi.ts

export const searchQueueApi = {
  // Get all tasks
  async getTasks() {
    const response = await fetch('/api/search-queue');
    return response.json();
  },

  // Create new task
  async createTask(data: Partial<SearchTask>) {
    const response = await fetch('/api/search-queue/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return response.json();
  },

  // Execute search
  async executeSearch(searchId: string) {
    const response = await fetch(`/api/search-queue/${searchId}/execute`, {
      method: 'POST'
    });
    return response.json();
  },

  // Add videos to queue
  async addToVideoQueue(searchId: string, videoUrls: string[]) {
    const response = await fetch(`/api/search-queue/${searchId}/add-to-video-queue`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ video_urls: videoUrls })
    });
    return response.json();
  },

  // Complete task
  async completeTask(searchId: string, data: any) {
    const response = await fetch(`/api/search-queue/${searchId}/complete`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return response.json();
  }
};
```

---

## 3. STYLING

Add to `src/styles/components.css`:

```css
/* Search Task Card */
.search-task-card {
  background: var(--bg-secondary);
  border-left: 4px solid var(--color-search);
  border-radius: 0.5rem;
  padding: var(--space-5);
  box-shadow: var(--shadow-sm);
  transition: all 300ms ease-in-out;
}

.search-task-card:hover {
  box-shadow: var(--shadow-md);
  border-left-width: 6px;
}

/* Search Results Modal */
.search-results-modal {
  width: 900px;
  max-height: 90vh;
}

.search-result-item {
  display: flex;
  gap: var(--space-4);
  padding: var(--space-4);
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  transition: all 200ms ease-in-out;
  cursor: pointer;
}

.search-result-item:hover {
  background: var(--bg-tertiary);
  border-color: var(--color-search);
  box-shadow: var(--shadow-md);
}

.search-result-item.selected {
  background: var(--color-search-bg);
  border-color: var(--color-search);
  border-width: 2px;
}
```

---

## RESULT

After applying this prompt, the Search Queue module will be ready with:

✅ Dashboard with task list
✅ Filters by status and department
✅ Create Task Modal with prompt selection
✅ Search Results Modal with video selection
✅ API integration
✅ Full styling in brand style
