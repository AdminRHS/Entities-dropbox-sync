# PROMPT: Video Queue Module

**Purpose:** Generate Video Queue module with full functionality

---

## TASK

Create Video Queue module for RESEARCHES 2 with the following components and functionality.

**Design:** Follow the style of https://adminrhs.github.io/Video-catalog/
**Design System:** https://adminrhs.github.io/Design-system/
**Module Color:** `--color-video: #147857` (Developers - Forest Green from Design System)

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

### VideoQueueDashboard.tsx

```tsx
import React from 'react';
import { VideoCard } from './VideoCard';
import { AddVideoModal } from './AddVideoModal';
import { VideoQueueStats } from './VideoQueueStats';

interface Video {
  vq_id: string;
  youtube_url: string;
  title: string;
  channel: string;
  duration: string;
  views: number;
  upload_date: string;
  topic: string;
  source: string;
  employee: string;
  priority: number;
  status: 'Queued' | 'Selected' | 'In_Progress' | 'Completed';
  date_added: string;
  notes?: string;
  thumbnail: string;
}

export function VideoQueueDashboard() {
  const [videos, setVideos] = React.useState<Video[]>([]);
  const [isAddModalOpen, setIsAddModalOpen] = React.useState(false);
  const [viewMode, setViewMode] = React.useState<'grid' | 'list'>('grid');

  // Filters
  const [statusFilter, setStatusFilter] = React.useState('All');
  const [priorityFilter, setPriorityFilter] = React.useState('All');
  const [sortBy, setSortBy] = React.useState('priority');

  return (
    <div className="container mx-auto p-8">
      {/* Header */}
      <header className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-[var(--text-primary)] mb-2">
            Video Queue
          </h1>
          <p className="text-sm text-[var(--text-secondary)]">
            Manage and prioritize video processing queue
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button className="btn-secondary">
            📤 Export
          </button>
          <button
            onClick={() => setIsAddModalOpen(true)}
            className="btn-primary flex items-center gap-2"
          >
            <span>➕</span>
            <span>Add Video Manually</span>
          </button>
        </div>
      </header>

      {/* Stats */}
      <VideoQueueStats />

      {/* Filters & Controls */}
      <div className="flex items-center justify-between mb-6">
        <div className="filter-group">
          <button
            className={`filter-button ${statusFilter === 'All' ? 'active department-video' : ''}`}
            onClick={() => setStatusFilter('All')}
          >
            All
          </button>
          <button
            className={`filter-button ${statusFilter === 'Queued' ? 'active department-video' : ''}`}
            onClick={() => setStatusFilter('Queued')}
          >
            Queued
          </button>
          <button
            className={`filter-button ${statusFilter === 'In_Progress' ? 'active department-video' : ''}`}
            onClick={() => setStatusFilter('In_Progress')}
          >
            In Progress
          </button>
          <button
            className={`filter-button ${statusFilter === 'Completed' ? 'active department-video' : ''}`}
            onClick={() => setStatusFilter('Completed')}
          >
            Completed
          </button>
        </div>

        <div className="flex items-center gap-3">
          {/* Sort */}
          <select
            className="select"
            value={sortBy}
            onChange={e => setSortBy(e.target.value)}
          >
            <option value="priority">By Priority (High to Low)</option>
            <option value="date">By Date Added (Newest)</option>
            <option value="views">By Views</option>
          </select>

          {/* View Mode */}
          <div className="flex items-center gap-1 border border-[var(--border-color)] rounded-lg p-1">
            <button
              className={`btn-icon btn-sm ${viewMode === 'grid' ? 'bg-[var(--bg-tertiary)]' : ''}`}
              onClick={() => setViewMode('grid')}
            >
              ⊞
            </button>
            <button
              className={`btn-icon btn-sm ${viewMode === 'list' ? 'bg-[var(--bg-tertiary)]' : ''}`}
              onClick={() => setViewMode('list')}
            >
              ☰
            </button>
          </div>
        </div>
      </div>

      {/* Videos Grid/List */}
      <div className={viewMode === 'grid' ? 'grid gap-6' : 'flex flex-col gap-4'}>
        {videos.map(video => (
          <VideoCard
            key={video.vq_id}
            video={video}
            viewMode={viewMode}
            onMoveToPhase1={handleMoveToPhase1}
            onEdit={handleEditVideo}
            onDelete={handleDeleteVideo}
          />
        ))}
      </div>

      {/* Add Video Modal */}
      <AddVideoModal
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        onAdd={handleAddVideo}
      />
    </div>
  );
}
```

### VideoCard.tsx

```tsx
interface VideoCardProps {
  video: Video;
  viewMode: 'grid' | 'list';
  onMoveToPhase1: (vqId: string) => void;
  onEdit: (vqId: string) => void;
  onDelete: (vqId: string) => void;
}

export function VideoCard({ video, viewMode, onMoveToPhase1, onEdit, onDelete }: VideoCardProps) {
  if (viewMode === 'list') {
    return (
      <div className="video-card-list">
        {/* List view - horizontal layout */}
        <img src={video.thumbnail} alt={video.title} className="w-48 h-27 object-cover rounded" />
        <div className="flex-1">
          <div className="flex items-start justify-between mb-2">
            <div>
              <span className="text-xs font-bold text-[var(--color-video)]">{video.vq_id}</span>
              <h3 className="text-lg font-semibold">{video.title}</h3>
            </div>
            <PriorityBadge priority={video.priority} />
          </div>
          <p className="text-sm text-[var(--text-secondary)] mb-2">📺 {video.channel}</p>
          <div className="flex items-center gap-4 text-xs text-[var(--text-tertiary)]">
            <span>⏱ {video.duration}</span>
            <span>👁 {(video.views / 1000).toFixed(1)}K</span>
            <span>📅 {new Date(video.upload_date).toLocaleDateString()}</span>
          </div>
        </div>
        <div className="flex flex-col gap-2">
          <StatusBadge status={video.status} />
          <button className="btn-primary btn-sm" onClick={() => onMoveToPhase1(video.vq_id)}>
            Move to Phase 1
          </button>
        </div>
      </div>
    );
  }

  // Grid view (default)
  return (
    <div className="video-card group">
      {/* Thumbnail */}
      <div className="relative">
        <img
          src={video.thumbnail}
          alt={video.title}
          className="video-card-thumbnail"
        />
        <div className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity">
          <button className="btn-icon bg-white/90 hover:bg-white">
            ⋮
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="video-card-content">
        {/* Header */}
        <div className="flex items-start justify-between mb-2">
          <span className="text-xs font-bold text-[var(--color-video)]">
            {video.vq_id}
          </span>
          <PriorityBadge priority={video.priority} />
        </div>

        {/* Title */}
        <h3 className="video-card-title mb-2">{video.title}</h3>

        {/* Channel */}
        <p className="text-sm text-[var(--text-secondary)] mb-3">
          📺 {video.channel}
        </p>

        {/* Meta */}
        <div className="video-card-meta mb-3">
          <span>⏱ {video.duration}</span>
          <span>👁 {(video.views / 1000).toFixed(1)}K</span>
          <span>📅 {new Date(video.upload_date).toLocaleDateString()}</span>
        </div>

        {/* Tags */}
        <div className="flex items-center gap-2 mb-3">
          <span className="badge badge-video">{video.topic}</span>
          <StatusBadge status={video.status} />
        </div>

        {/* Employee */}
        <p className="text-xs text-[var(--text-tertiary)] mb-4">
          👤 {video.employee}
        </p>

        {/* Actions */}
        <div className="flex items-center gap-2">
          <button
            className="btn-secondary btn-sm flex-1"
            onClick={() => window.open(video.youtube_url, '_blank')}
          >
            👁️ View
          </button>
          <button
            className="btn-primary btn-sm flex-1"
            onClick={() => onMoveToPhase1(video.vq_id)}
          >
            ➡️ Phase 1
          </button>
        </div>
      </div>
    </div>
  );
}
```

### AddVideoModal.tsx

```tsx
interface AddVideoModalProps {
  isOpen: boolean;
  onClose: () => void;
  onAdd: (video: Partial<Video>) => void;
}

export function AddVideoModal({ isOpen, onClose, onAdd }: AddVideoModalProps) {
  const [youtubeUrl, setYoutubeUrl] = React.useState('');
  const [metadata, setMetadata] = React.useState<any>(null);
  const [loading, setLoading] = React.useState(false);
  const [formData, setFormData] = React.useState({
    topic: '',
    employee: '',
    source: 'Manual',
    notes: ''
  });

  const fetchMetadata = async () => {
    setLoading(true);
    try {
      const response = await fetch(`/api/video-queue/metadata?url=${encodeURIComponent(youtubeUrl)}`);
      const data = await response.json();
      setMetadata(data);
    } catch (error) {
      console.error('Failed to fetch metadata:', error);
    } finally {
      setLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal modal-md" onClick={e => e.stopPropagation()}>
        {/* Header */}
        <div className="modal-header">
          <h2 className="modal-title">Add Video Manually</h2>
          <button className="modal-close" onClick={onClose}>✕</button>
        </div>

        {/* Body */}
        <div className="modal-body">
          <form className="flex flex-col gap-4">
            {/* YouTube URL */}
            <div>
              <label className="text-label mb-2 block">YouTube URL *</label>
              <div className="flex gap-2">
                <input
                  type="text"
                  className="input flex-1"
                  placeholder="https://youtube.com/watch?v=xxxxx"
                  value={youtubeUrl}
                  onChange={e => setYoutubeUrl(e.target.value)}
                />
                <button
                  type="button"
                  className="btn-primary"
                  onClick={fetchMetadata}
                  disabled={!youtubeUrl || loading}
                >
                  {loading ? '⏳' : '🔍'} Fetch Metadata
                </button>
              </div>
            </div>

            {/* Auto-filled metadata */}
            {metadata && (
              <div className="p-4 bg-[var(--bg-tertiary)] rounded-lg">
                <p className="text-sm font-medium mb-2">Auto-filled from YouTube:</p>
                <div className="space-y-1 text-sm text-[var(--text-secondary)]">
                  <p><strong>Title:</strong> {metadata.title}</p>
                  <p><strong>Channel:</strong> {metadata.channel}</p>
                  <p><strong>Duration:</strong> {metadata.duration}</p>
                  <p><strong>Views:</strong> {metadata.views.toLocaleString()}</p>
                  <p><strong>Upload Date:</strong> {new Date(metadata.upload_date).toLocaleDateString()}</p>
                </div>
                <div className="mt-3">
                  <img src={metadata.thumbnail} alt="Thumbnail" className="w-full rounded" />
                </div>
              </div>
            )}

            {/* Topic */}
            <div>
              <label className="text-label mb-2 block">Topic *</label>
              <input
                type="text"
                className="input"
                placeholder="e.g., AI Tools"
                value={formData.topic}
                onChange={e => setFormData({ ...formData, topic: e.target.value })}
              />
            </div>

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

            {/* Source */}
            <div>
              <label className="text-label mb-2 block">Source</label>
              <input
                type="text"
                className="input"
                placeholder="Manual"
                value={formData.source}
                onChange={e => setFormData({ ...formData, source: e.target.value })}
              />
            </div>

            {/* Auto-calculated Priority */}
            {metadata && (
              <div>
                <label className="text-label mb-2 block">Priority (auto-calculated)</label>
                <div className="flex items-center gap-2">
                  <PriorityBadge priority={metadata.priority || 50} />
                  <span className="text-sm text-[var(--text-secondary)]">
                    Calculated based on views, recency, and duration
                  </span>
                </div>
              </div>
            )}

            {/* Notes */}
            <div>
              <label className="text-label mb-2 block">Notes (optional)</label>
              <textarea
                className="textarea"
                placeholder="Add any notes..."
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
            disabled={!metadata || !formData.topic || !formData.employee}
            onClick={() => {
              onAdd({
                youtube_url: youtubeUrl,
                ...metadata,
                ...formData
              });
              onClose();
            }}
          >
            Add to Queue
          </button>
        </div>
      </div>
    </div>
  );
}
```

### VideoQueueStats.tsx

```tsx
export function VideoQueueStats() {
  const [stats, setStats] = React.useState({
    total: 128,
    queued: 15,
    in_progress: 3,
    completed: 28,
    priority_distribution: {
      '80-100': 15,
      '60-79': 45,
      '40-59': 50,
      '20-39': 15,
      '0-19': 3
    }
  });

  return (
    <div className="mb-8">
      {/* Stats Cards */}
      <div className="stats-grid mb-6">
        <div className="stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon video">📊</div>
          </div>
          <div className="stat-card-value">{stats.total}</div>
          <div className="stat-card-label">Total Videos</div>
        </div>

        <div className="stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon video">⏳</div>
          </div>
          <div className="stat-card-value">{stats.queued}</div>
          <div className="stat-card-label">Queued</div>
        </div>

        <div className="stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon video">▶️</div>
          </div>
          <div className="stat-card-value">{stats.in_progress}</div>
          <div className="stat-card-label">In Progress</div>
        </div>

        <div className="stat-card">
          <div className="stat-card-header">
            <div className="stat-card-icon video">✅</div>
          </div>
          <div className="stat-card-value">{stats.completed}</div>
          <div className="stat-card-label">Completed</div>
          <div className="stat-card-change positive">
            +12% this week
          </div>
        </div>
      </div>

      {/* Priority Distribution Bar */}
      <div className="card p-4">
        <h3 className="text-sm font-semibold mb-3">Priority Distribution</h3>
        <div className="flex gap-1 h-4 rounded overflow-hidden">
          <div
            className="bg-[var(--priority-critical)]"
            style={{ width: `${(stats.priority_distribution['80-100'] / stats.total) * 100}%` }}
            title="Critical: 15"
          />
          <div
            className="bg-[var(--priority-high)]"
            style={{ width: `${(stats.priority_distribution['60-79'] / stats.total) * 100}%` }}
            title="High: 45"
          />
          <div
            className="bg-[var(--priority-medium)]"
            style={{ width: `${(stats.priority_distribution['40-59'] / stats.total) * 100}%` }}
            title="Medium: 50"
          />
          <div
            className="bg-[var(--priority-low)]"
            style={{ width: `${(stats.priority_distribution['20-39'] / stats.total) * 100}%` }}
            title="Low: 15"
          />
          <div
            className="bg-[var(--priority-verylow)]"
            style={{ width: `${(stats.priority_distribution['0-19'] / stats.total) * 100}%` }}
            title="Very Low: 3"
          />
        </div>
        <div className="flex items-center justify-between mt-2 text-xs text-[var(--text-tertiary)]">
          <span>⭐⭐⭐⭐⭐ {stats.priority_distribution['80-100']}</span>
          <span>⭐⭐⭐⭐ {stats.priority_distribution['60-79']}</span>
          <span>⭐⭐⭐ {stats.priority_distribution['40-59']}</span>
          <span>⭐⭐ {stats.priority_distribution['20-39']}</span>
          <span>⭐ {stats.priority_distribution['0-19']}</span>
        </div>
      </div>
    </div>
  );
}
```

### PriorityBadge.tsx

```tsx
interface PriorityBadgeProps {
  priority: number;
}

export function PriorityBadge({ priority }: PriorityBadgeProps) {
  const getStars = (priority: number) => {
    if (priority >= 80) return '⭐⭐⭐⭐⭐';
    if (priority >= 60) return '⭐⭐⭐⭐';
    if (priority >= 40) return '⭐⭐⭐';
    if (priority >= 20) return '⭐⭐';
    return '⭐';
  };

  const getClass = (priority: number) => {
    if (priority >= 80) return 'badge-priority-critical';
    if (priority >= 60) return 'badge-priority-high';
    if (priority >= 40) return 'badge-priority-medium';
    if (priority >= 20) return 'badge-priority-low';
    return 'badge badge-priority-verylow';
  };

  return (
    <span className={`badge ${getClass(priority)}`}>
      {getStars(priority)} ({priority})
    </span>
  );
}
```

---

## 2. STYLING

Add to `src/styles/components.css`:

```css
/* Video Card */
.video-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: all 300ms ease-in-out;
  cursor: pointer;
}

.video-card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.video-card-thumbnail {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
  background: linear-gradient(135deg, #147857 0%, #10b981 100%);
}

/* Stats Card */
.stat-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: all 200ms ease-in-out;
}

.stat-card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.stat-card-icon.video {
  background: var(--color-video-bg);
  color: var(--color-video);
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.5rem;
  font-size: var(--text-xl);
}
```

---

## RESULT

After applying this prompt, the Video Queue module will be ready with:

✅ Dashboard with video cards (grid/list view)
✅ Stats cards with metrics
✅ Priority distribution bar
✅ Add Video Modal with YouTube API
✅ Priority Calculator (0-100)
✅ Filters & sorting
✅ Full styling
