---
PMT_ID: PMT-075
Title: Integrate Refactored Components into VideoQueuePage
Category: CORE
Department: Dev
Version: 1.0
Status: Draft
Created: 2025-12-10
Last_Updated: 2025-12-10
Author: AI & Automation Team
Tags: [integration, component-reuse, react, video-queue, refactoring]
Dependencies: [PMT-074]
Referenced_Entities: []
---

# Integrate Refactored Components into VideoQueuePage

## Purpose
Integrate all newly extracted components from `InteractiveVideoPlayer.jsx` refactoring into `VideoQueuePage.jsx` to achieve visual consistency and code reusability, while **preserving VideoQueuePage's existing data source and API calls**.

## Context

**Source Components (from PMT-074):**
- `VideoPlayerContainer.jsx` - Video player with glow effect, loading, controls, layers
- `VideoMetadata.jsx` - Title, author, action buttons (Like, Share, Save)
- `VideoDescription.jsx` - Tags and description display
- `VideoTimestamps.jsx` - Timestamps list with click-to-seek
- `CommentsSection.jsx` - Full comments system (filter, input, list, replies, likes)
- `RecommendationsSection.jsx` - Recommendations list wrapper
- `TranscriptsSection.jsx` - Transcripts wrapper
- `DeleteCommentModal.jsx` - Comment deletion confirmation
- `commentUtils.js` - Utility functions (getAvatarColor, formatTimeAgo)

**Current VideoQueuePage State:**
- File: `upload_crms/client/src/pages/VideoQueuePage.jsx`
- Size: ~540 lines
- **Data Source:** Uses `fetchVideoDetail`, `fetchVideoList`, `syncVideoQueue` from `../services/videoQueue`
- **Data Structure:** `detail` object from video queue API with fields:
  - `queueId`, `title`, `videoUrl`, `channelName`, `publishDate`, `duration`
  - `status`, `priorityScore`, `topicCategory`, `researchSource`
  - `transcriptData` (array of segments with `start`, `end`, `text`)
- Current implementation:
  - Simple `VideoPlayer` component (no container, no glow, no controls)
  - Inline video metadata (title, author, buttons) - basic HTML
  - Inline tags display - simple divs
  - Inline timestamps - basic list
  - Simple comments system - basic input + list (no replies, likes, filters)
  - Simple recommendations - mock data display
  - Uses `TranscriptPanel` directly (not wrapped in TranscriptsSection)

**Target State:**
- **PRESERVE existing data source:** Keep `fetchVideoDetail`, `fetchVideoList`, `syncVideoQueue` calls
- **PRESERVE existing data structure:** Continue using `detail` object from video queue API
- **USE same components:** Replace inline implementations with components from `InteractiveVideoPlayer.jsx`
- **CREATE data adapters:** Transform video queue data format to match component prop expectations
- **MAINTAIN functionality:** Keep all existing features (localStorage comments, search, breadcrumbs)
- **ADD new features:** Enable replies, likes, filters in comments (same as InteractiveVideoPlayer)
- **ACHIEVE visual consistency:** Use exact same design and layout as InteractiveVideoPlayer

---

## Critical Requirements

### ⚠️ Data Source Preservation
**DO NOT CHANGE:**
- Keep `fetchVideoDetail`, `fetchVideoList`, `syncVideoQueue` API calls
- Keep `detail` object structure from video queue API
- Keep `loadList()`, `loadDetail()` functions as-is
- Keep localStorage persistence logic for comments
- Keep search and breadcrumb functionality

**ONLY CHANGE:**
- Replace inline UI components with extracted components
- Add data transformation/adaptation layer
- Add state management for new features (comments, video controls)

### Data Transformation Strategy

**Video Queue Data → Component Props:**
- `detail.videoUrl` → `asset.url` for VideoPlayerContainer
- `detail.title` → `video.title` for VideoMetadata
- `detail.channelName` → `video.createdBy` for VideoMetadata
- `detail.publishDate` → `video.createdAt` for VideoMetadata
- `detail.transcriptData` → `segments` array for VideoPlayerContainer/TranscriptsSection
- `detail.transcriptData` → `displayTranscription` array for VideoTimestamps
- `detail.status`, `detail.priorityScore`, `detail.topicCategory` → `video.tags` array for VideoDescription
- `localStorage comments` → `allComments` array for CommentsSection

---

## Integration Plan

### Phase 1: Video Player Integration

**Component:** `VideoPlayerContainer.jsx`

**Current Implementation:**
```jsx
<div ref={videoContainerRef} className="..." style={{ boxShadow: ... }}>
  <VideoPlayer ref={videoRef} src={detail.videoUrl} controls />
</div>
```

**Required Changes:**
1. Import `VideoPlayerContainer` instead of `VideoPlayer`
2. **PRESERVE:** Keep `detail.videoUrl` from video queue API
3. Add video state management:
   - `videoLoading`, `videoLoadProgress`, `videoDuration`, `isPlaying`, `volume`, `isFullscreen`
   - Video event handlers: `onTimeUpdate`, `onPlay`, `onPause`, `onVolumeChange`, `onSeek`, `onFullscreen`
4. Add video loading/progress handlers: `onLoadStart`, `onLoadedMetadata`, `onProgress`, `onCanPlay`, `onError`
5. Transform `detail.transcriptData` to `segments` format (see Data Transformation section)
6. Add reactions, comments arrays (can be empty initially)
7. Add comment text state for video overlay comments
8. Add interactions and visibleComments for DynamicCommentsLayer
9. Pass all required props to `VideoPlayerContainer`

**Data Transformation:**
```jsx
// Transform detail.transcriptData to segments format
const segments = useMemo(() => {
  if (!detail?.transcriptData || !Array.isArray(detail.transcriptData)) return [];
  
  return detail.transcriptData.map((seg, index) => ({
    segmentId: `seg_${index}`,
    startTime: seg.start || '00:00',
    startTimeSeconds: parseTimeToSeconds(seg.start),
    endTime: seg.end || seg.start || '00:00',
    endTimeSeconds: parseTimeToSeconds(seg.end || seg.start),
    text: seg.text || ''
  }));
}, [detail?.transcriptData]);
```

**Props Mapping:**
```jsx
<VideoPlayerContainer
  videoRef={videoRef}
  videoContainerRef={videoContainerRef}
  asset={{ url: detail.videoUrl }} // PRESERVE: Use detail.videoUrl from API
  videoColors={videoColors}
  videoLoading={videoLoading}
  videoLoadProgress={videoLoadProgress}
  videoDuration={videoDuration}
  currentTime={currentTime}
  isPlaying={isPlaying}
  volume={volume}
  isFullscreen={isFullscreen}
  segments={segments} // Transformed from detail.transcriptData
  reactions={reactions} // Empty array initially
  comments={videoComments} // Empty array initially
  commentText={commentText}
  onTimeUpdate={handleTimeUpdate}
  onPlay={() => setIsPlaying(true)}
  onPause={() => setIsPlaying(false)}
  onVolumeChange={handleVolumeChange}
  onSeek={handleSeek}
  onFullscreen={handleFullscreen}
  onCommentTextChange={setCommentText}
  onAddComment={handleAddVideoComment}
  onAddReaction={handleAddReaction}
  onLoadStart={() => setVideoLoading(true)}
  onLoadedMetadata={(e) => {
    setVideoLoading(false);
    if (e.target.duration) {
      setVideoDuration(e.target.duration);
    }
    if (e.target.volume !== undefined) {
      setVolume(e.target.volume);
    }
  }}
  onProgress={(e) => {
    if (e.target.buffered.length > 0) {
      const buffered = e.target.buffered.end(e.target.buffered.length - 1);
      const duration = e.target.duration;
      if (duration > 0) {
        setVideoLoadProgress((buffered / duration) * 100);
        if (!videoDuration) {
          setVideoDuration(duration);
        }
      }
    }
  }}
  onCanPlay={(e) => {
    setVideoLoading(false);
    if (e.target.duration && !videoDuration) {
      setVideoDuration(e.target.duration);
    }
  }}
  onError={() => setVideoLoading(false)}
  onClick={handlePlayPause}
  interactions={interactions} // Empty array initially
  visibleComments={visibleComments} // Empty Set initially
/>
```

---

### Phase 2: Video Metadata Integration

**Component:** `VideoMetadata.jsx`

**Current Implementation:**
```jsx
<div className="flex flex-col gap-3">
  <h1>{detail.title}</h1>
  <div className="flex items-center gap-3">
    {/* Avatar, author, date, duration */}
  </div>
  <div className="flex flex-wrap items-center gap-2">
    {/* Like, Share, Save buttons */}
  </div>
</div>
```

**Required Changes:**
1. Import `VideoMetadata`
2. **PRESERVE:** Keep using `detail.title`, `detail.channelName`, `detail.publishDate` from video queue API
3. Add state: `isLiked`, `isSaved`, `likeCount`
4. Create data adapter to transform video queue data to VideoMetadata props
5. Replace inline JSX with `VideoMetadata` component

**Data Transformation:**
```jsx
// Transform video queue data to VideoMetadata format
const videoMetadataData = useMemo(() => ({
  title: detail?.title || '',
  createdBy: detail?.channelName || 'AI',
  createdAt: detail?.publishDate || new Date().toISOString(),
  description: detail?.description || '',
  isPublic: true // Default to public for video queue
}), [detail]);
```

**Props Mapping:**
```jsx
<VideoMetadata
  video={videoMetadataData} // Transformed from detail object
  isLiked={isLiked}
  isSaved={isSaved}
  likeCount={likeCount}
  onLike={() => {
    setIsLiked(!isLiked);
    setLikeCount(prev => isLiked ? prev - 1 : prev + 1);
  }}
  onShare={() => {
    if (navigator.share) {
      navigator.share({
        title: detail.title,
        text: detail.description,
        url: window.location.href
      }).catch(() => {});
    } else {
      navigator.clipboard.writeText(window.location.href);
    }
  }}
  onSave={() => setIsSaved(!isSaved)}
  formatDateTime={(date) => {
    // Format date from detail.publishDate
    try {
      return new Date(date).toLocaleString('uk-UA', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
    } catch {
      return new Date().toLocaleString('uk-UA');
    }
  }}
/>
```

---

### Phase 3: Video Description Integration

**Component:** `VideoDescription.jsx`

**Current Implementation:**
```jsx
<div className="flex flex-wrap gap-2 text-xs">
  <span>AI Tools Overview</span>
  <span>Статус: {detail.status}</span>
  <span>Пріоритет: {detail.priorityScore}</span>
</div>
```

**Required Changes:**
1. Import `VideoDescription`
2. **PRESERVE:** Keep using `detail.status`, `detail.priorityScore`, `detail.topicCategory`, `detail.researchSource` from video queue API
3. Create tags array from video queue data fields
4. Replace inline tags with `VideoDescription` component

**Data Transformation:**
```jsx
// Transform video queue data to VideoDescription format
const videoDescriptionData = useMemo(() => ({
  tags: [
    detail?.topicCategory || 'AI Tools Overview',
    `Статус: ${detail?.status || 'Pending'}`,
    `Пріоритет: ${detail?.priorityScore ?? '—'}`,
    detail?.researchSource ? `Джерело: ${detail.researchSource}` : null
  ].filter(Boolean),
  description: detail?.description || '',
  duration: detail?.duration || '00:00:00'
}), [detail]);
```

**Props Mapping:**
```jsx
<VideoDescription
  video={videoDescriptionData} // Transformed from detail object
  formatDuration={(duration) => {
    // PRESERVE: Use detail.duration from video queue API
    return detail?.duration || '00:00:00';
  }}
/>
```

---

### Phase 4: Video Timestamps Integration

**Component:** `VideoTimestamps.jsx`

**Current Implementation:**
```jsx
{detail.transcriptData && Array.isArray(detail.transcriptData) && (
  <div>
    <h3>TIMESTAMPS</h3>
    {detail.transcriptData.slice(0, 10).map((segment, index) => (
      <div onClick={() => { /* seek */ }}>
        {segment.start} — {segment.text}
      </div>
    ))}
  </div>
)}
```

**Required Changes:**
1. Import `VideoTimestamps`
2. **PRESERVE:** Keep using `detail.transcriptData` from video queue API
3. Transform `detail.transcriptData` to `displayTranscription` format (minimal transformation)
4. Add state: `showAllTimestamps`
5. Replace inline timestamps with `VideoTimestamps` component

**Data Transformation:**
```jsx
// Transform detail.transcriptData to displayTranscription format
const displayTranscription = useMemo(() => {
  if (!detail?.transcriptData || !Array.isArray(detail.transcriptData)) return [];
  // Minimal transformation - just map to expected format
  return detail.transcriptData.map(seg => ({
    start: seg.start || '00:00',
    text: seg.text || ''
  }));
}, [detail?.transcriptData]);
```

**Props Mapping:**
```jsx
{displayTranscription.length > 0 && (
  <VideoTimestamps
    displayTranscription={displayTranscription} // Transformed from detail.transcriptData
    showAllTimestamps={showAllTimestamps}
    onToggleShowAll={() => setShowAllTimestamps(!showAllTimestamps)}
    currentTime={currentTime}
    videoRef={videoRef}
    segments={segments} // From Phase 1 transformation
    onSeek={(timeInSeconds) => {
      if (videoRef.current) {
        videoRef.current.currentTime = timeInSeconds;
        setCurrentTime(timeInSeconds);
      }
    }}
    setCurrentTime={setCurrentTime}
    setActiveSegmentId={setActiveSegmentId}
  />
)}
```

---

### Phase 5: Comments Section Integration

**Component:** `CommentsSection.jsx`

**Current Implementation:**
```jsx
<div className="bg-[#1f2937] border border-slate-800 rounded-xl p-4 space-y-3">
  <div>Comments ({comments.length})</div>
  <div className="flex items-center gap-2">
    <input value={commentText} onChange={...} />
    <button onClick={handleAddComment}>Send</button>
  </div>
  {comments.map(c => (
    <div key={c.id}>
      <div>{c.author}</div>
      <div>{c.text}</div>
    </div>
  ))}
</div>
```

**Required Changes:**
1. Import `CommentsSection`, `DeleteCommentModal`, `commentUtils`
2. **PRESERVE:** Keep localStorage comments system (`loadStoredComments`, `saveStoredComments`)
3. **PRESERVE:** Keep `comments` state from localStorage
4. Transform localStorage comments to `allComments` format (with time, author, etc.)
5. Add state for extended comments system:
   - `commentSortOrder`, `showFilterMenu`, `newCommentText`
   - `commentLikes`, `commentDislikes`, `commentReplies`
   - `replyingTo`, `replyText`, `editingCommentId`, `editCommentText`
   - `editingReplyId`, `editReplyText`, `hiddenReplies`
   - `commentToDelete`
6. Add `userDisplayName` (from auth or default)
7. Create handler functions for all comment operations
8. Replace inline comments with `CommentsSection` component
9. Add `DeleteCommentModal` component
10. **UPDATE:** Modify `saveStoredComments` to persist extended comment structure (replies, likes)

**Data Transformation:**
```jsx
// Transform localStorage comments to allComments format
const allComments = useMemo(() => {
  return comments.map(c => ({
    id: c.id,
    time: c.createdAt 
      ? formatSecondsToHHMMSS(Math.floor(new Date(c.createdAt).getTime() / 1000))
      : '00:00:00',
    author: c.author || userDisplayName,
    text: c.text,
    content: c.text,
    displayOnVideo: false,
    isEdited: c.isEdited || false
  }));
}, [comments, userDisplayName]);

// Create videoInfo object from video queue data
const videoInfo = useMemo(() => ({
  video: {
    title: detail?.title || '',
    createdBy: detail?.channelName || 'AI',
    createdAt: detail?.publishDate || new Date().toISOString()
  },
  formatDateTime: (date) => {
    try {
      return new Date(date).toLocaleString('uk-UA', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
    } catch {
      return new Date().toLocaleString('uk-UA');
    }
  }
}), [detail]);

<CommentsSection
  allComments={allComments}
  commentSortOrder={commentSortOrder}
  showFilterMenu={showFilterMenu}
  newCommentText={newCommentText}
  commentLikes={commentLikes}
  commentDislikes={commentDislikes}
  commentReplies={commentReplies}
  replyingTo={replyingTo}
  replyText={replyText}
  editingCommentId={editingCommentId}
  editCommentText={editCommentText}
  editingReplyId={editingReplyId}
  editReplyText={editReplyText}
  hiddenReplies={hiddenReplies}
  userDisplayName={userDisplayName}
  currentTime={currentTime}
  videoInfo={videoInfo}
  onSortOrderChange={setCommentSortOrder}
  onFilterMenuToggle={() => setShowFilterMenu(!showFilterMenu)}
  onNewCommentChange={setNewCommentText}
  onAddComment={(text) => {
    const newComment = {
      id: `sc_${Date.now()}`,
      time: formatSecondsToHHMMSS(currentTime),
      author: userDisplayName,
      text: text,
      createdAt: new Date()
    };
    setComments(prev => [...prev, newComment]);
    setNewCommentText('');
  }}
  onCommentLike={(commentId) => { /* ... */ }}
  onCommentDislike={(commentId) => { /* ... */ }}
  onReply={(commentId) => { /* ... */ }}
  onSubmitReply={(commentId, text) => { /* ... */ }}
  onEditReply={(commentId, replyId, text) => { /* ... */ }}
  onUpdateReply={(commentId, replyId, text) => { /* ... */ }}
  onDeleteReply={(commentId, replyId) => { /* ... */ }}
  onEditComment={(commentId, text) => { /* ... */ }}
  onUpdateComment={(commentId, text) => { /* ... */ }}
  onDeleteComment={(commentId) => {
    setCommentToDelete(commentId);
  }}
  onToggleReplies={(commentId) => { /* ... */ }}
  onReplyTextChange={setReplyText}
  onEditReplyTextChange={setEditReplyText}
  onEditCommentTextChange={setEditCommentText}
/>

<DeleteCommentModal
  isOpen={!!commentToDelete}
  onClose={() => setCommentToDelete(null)}
  onConfirm={() => {
    if (commentToDelete) {
      setComments(prev => prev.filter(c => c.id !== commentToDelete));
      setCommentToDelete(null);
    }
  }}
/>
```

**Important:** 
- **PRESERVE:** Keep existing `loadStoredComments` and `saveStoredComments` functions
- **UPDATE:** Modify `saveStoredComments` to persist extended comment structure (replies, likes, dislikes)
- **PRESERVE:** Keep `COMMENTS_KEY_PREFIX` and localStorage key structure
- Comments should still be stored per `queueId` (not `assetId`)

---

### Phase 6: Recommendations Section Integration

**Component:** `RecommendationsSection.jsx`

**Current Implementation:**
```jsx
<div className="bg-[#1f2937] shadow-lg shadow-black/30 rounded-xl p-4">
  <h3>Recommendations</h3>
  {[1, 2, 3].map((idx) => (
    <div key={idx}>
      {/* Mock recommendation */}
    </div>
  ))}
</div>
```

**Required Changes:**
1. Import `RecommendationsSection` and `useNavigate` hook
2. **PRESERVE:** Keep empty recommendations for now (video queue doesn't have recommendations API)
3. Replace mock recommendations with `RecommendationsSection` component
4. Pass empty array (can be populated later if video queue API adds recommendations)

**Props Mapping:**
```jsx
<RecommendationsSection
  recommendations={[]} // Empty - video queue API doesn't provide recommendations yet
  onNavigate={navigate} // From useNavigate hook
/>
```

**Note:** If video queue API adds recommendations in the future, transform them to match `RecommendationCard` expected format.

---

### Phase 7: Transcripts Section Integration

**Component:** `TranscriptsSection.jsx`

**Current Implementation:**
```jsx
<CollapsibleTranscripts title="Transcripts" ...>
  <TranscriptPanel transcripts={parsedTranscripts} ... />
</CollapsibleTranscripts>
```

**Required Changes:**
1. Import `TranscriptsSection`
2. **PRESERVE:** Keep using `detail.transcriptData` from video queue API
3. **USE:** Use `segments` from Phase 1 transformation (already transformed from `detail.transcriptData`)
4. Replace `CollapsibleTranscripts` + `TranscriptPanel` with `TranscriptsSection`
5. Pass segments and handlers

**Data Transformation:**
- Use `segments` from Phase 1 (already transformed from `detail.transcriptData`)

**Props Mapping:**
```jsx
<TranscriptsSection
  segments={segments} // From Phase 1 - transformed from detail.transcriptData
  activeSegmentId={activeSegmentId}
  onSegmentClick={(segment) => {
    if (videoRef.current) {
      videoRef.current.currentTime = segment.startTimeSeconds;
      setCurrentTime(segment.startTimeSeconds);
    }
  }}
  isExpanded={isTranscriptsExpanded}
  onToggle={setIsTranscriptsExpanded}
/>
```

---

## State Management Updates

### New State Variables Required

```jsx
// Video state
const [videoLoading, setVideoLoading] = useState(true);
const [videoLoadProgress, setVideoLoadProgress] = useState(0);
const [videoDuration, setVideoDuration] = useState(0);
const [isPlaying, setIsPlaying] = useState(false);
const [volume, setVolume] = useState(1);
const [isFullscreen, setIsFullscreen] = useState(false);

// Video metadata state
const [isLiked, setIsLiked] = useState(false);
const [isSaved, setIsSaved] = useState(false);
const [likeCount, setLikeCount] = useState(0);

// Segments state
const [segments, setSegments] = useState([]);
const [activeSegmentId, setActiveSegmentId] = useState(null);

// Comments state (extended)
const [commentSortOrder, setCommentSortOrder] = useState('newest');
const [showFilterMenu, setShowFilterMenu] = useState(false);
const [newCommentText, setNewCommentText] = useState('');
const [commentLikes, setCommentLikes] = useState({});
const [commentDislikes, setCommentDislikes] = useState({});
const [commentReplies, setCommentReplies] = useState({});
const [replyingTo, setReplyingTo] = useState(null);
const [replyText, setReplyText] = useState('');
const [editingCommentId, setEditingCommentId] = useState(null);
const [editCommentText, setEditCommentText] = useState('');
const [editingReplyId, setEditingReplyId] = useState(null);
const [editReplyText, setEditReplyText] = useState('');
const [hiddenReplies, setHiddenReplies] = useState(new Set());
const [commentToDelete, setCommentToDelete] = useState(null);

// Transcripts state
const [isTranscriptsExpanded, setIsTranscriptsExpanded] = useState(true);
const [showAllTimestamps, setShowAllTimestamps] = useState(false);

// Interactions (for video overlay)
const [interactions, setInteractions] = useState([]);
const [visibleComments, setVisibleComments] = useState(new Set());
const [commentText, setCommentText] = useState(''); // For video overlay
```

### Handler Functions Required

```jsx
// Video handlers
const handleTimeUpdate = () => { /* ... */ };
const handleSeek = (timeInSeconds) => { /* ... */ };
const handlePlayPause = () => { /* ... */ };
const handleVolumeChange = (newVolume) => { /* ... */ };
const handleFullscreen = () => { /* ... */ };
const handleAddVideoComment = (text) => { /* ... */ };
const handleAddReaction = (emoji) => { /* ... */ };

// Comment handlers (for CommentsSection)
const handleCommentLike = (commentId) => { /* ... */ };
const handleCommentDislike = (commentId) => { /* ... */ };
const handleReply = (commentId) => { /* ... */ };
const handleSubmitReply = (commentId, text) => { /* ... */ };
const handleEditReply = (commentId, replyId, text) => { /* ... */ };
const handleUpdateReply = (commentId, replyId, text) => { /* ... */ };
const handleDeleteReply = (commentId, replyId) => { /* ... */ };
const handleEditComment = (commentId, text) => { /* ... */ };
const handleUpdateComment = (commentId, text) => { /* ... */ };
const handleToggleReplies = (commentId) => { /* ... */ };
```

---

## Data Transformation Layer

### Overview
All data transformations should **preserve the original data source** (video queue API) and only adapt the format to match component prop expectations.

### Transformation 1: transcriptData → segments

**Source:** `detail.transcriptData` (from video queue API)
**Target:** `segments` array for VideoPlayerContainer and TranscriptsSection

```jsx
const segments = useMemo(() => {
  if (!detail?.transcriptData || !Array.isArray(detail.transcriptData)) return [];
  
  return detail.transcriptData.map((seg, index) => ({
    segmentId: `seg_${index}`,
    startTime: seg.start || '00:00',
    startTimeSeconds: parseTimeToSeconds(seg.start),
    endTime: seg.end || seg.start || '00:00',
    endTimeSeconds: parseTimeToSeconds(seg.end || seg.start),
    text: seg.text || ''
  }));
}, [detail?.transcriptData]);
```

### Transformation 2: transcriptData → displayTranscription

**Source:** `detail.transcriptData` (from video queue API)
**Target:** `displayTranscription` array for VideoTimestamps

```jsx
const displayTranscription = useMemo(() => {
  if (!detail?.transcriptData || !Array.isArray(detail.transcriptData)) return [];
  return detail.transcriptData.map(seg => ({
    start: seg.start || '00:00',
    text: seg.text || ''
  }));
}, [detail?.transcriptData]);
```

### Transformation 3: detail → videoMetadataData

**Source:** `detail` object (from video queue API)
**Target:** `video` object for VideoMetadata

```jsx
const videoMetadataData = useMemo(() => ({
  title: detail?.title || '',
  createdBy: detail?.channelName || 'AI',
  createdAt: detail?.publishDate || new Date().toISOString(),
  description: detail?.description || '',
  isPublic: true
}), [detail]);
```

### Transformation 4: detail → videoDescriptionData

**Source:** `detail` object (from video queue API)
**Target:** `video` object for VideoDescription

```jsx
const videoDescriptionData = useMemo(() => ({
  tags: [
    detail?.topicCategory || 'AI Tools Overview',
    `Статус: ${detail?.status || 'Pending'}`,
    `Пріоритет: ${detail?.priorityScore ?? '—'}`,
    detail?.researchSource ? `Джерело: ${detail.researchSource}` : null
  ].filter(Boolean),
  description: detail?.description || '',
  duration: detail?.duration || '00:00:00'
}), [detail]);
```

### Transformation 5: localStorage comments → allComments

**Source:** `comments` array (from localStorage)
**Target:** `allComments` array for CommentsSection

```jsx
const allComments = useMemo(() => {
  return comments.map(c => ({
    id: c.id,
    time: c.createdAt 
      ? formatSecondsToHHMMSS(Math.floor(new Date(c.createdAt).getTime() / 1000))
      : '00:00:00',
    author: c.author || userDisplayName,
    text: c.text,
    content: c.text,
    displayOnVideo: false,
    isEdited: c.isEdited || false
  }));
}, [comments, userDisplayName]);
```

### Transformation 6: detail → videoInfo

**Source:** `detail` object (from video queue API)
**Target:** `videoInfo` object for CommentsSection

```jsx
const videoInfo = useMemo(() => ({
  video: {
    title: detail?.title || '',
    createdBy: detail?.channelName || 'AI',
    createdAt: detail?.publishDate || new Date().toISOString()
  },
  formatDateTime: (date) => {
    try {
      return new Date(date).toLocaleString('uk-UA', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
    } catch {
      return new Date().toLocaleString('uk-UA');
    }
  },
  formatDuration: (duration) => {
    return detail?.duration || '00:00:00';
  },
  displayTranscription: displayTranscription, // From Transformation 2
  showAllTimestamps: showAllTimestamps,
  setShowAllTimestamps: setShowAllTimestamps
}), [detail, displayTranscription, showAllTimestamps]);
```

---

## Implementation Steps

### Step 1: Update Imports
- Add all component imports (VideoPlayerContainer, VideoMetadata, etc.)
- Add utility imports (`commentUtils`, `formatSecondsToHHMMSS`, etc.)
- Add `useNavigate` and `useAuth` hooks
- **PRESERVE:** Keep existing imports (`fetchVideoDetail`, `fetchVideoList`, `syncVideoQueue`)
- Remove unused imports (if any)

### Step 2: Add State Management
- Add all required state variables for video controls, comments, segments
- **PRESERVE:** Keep existing state (`videos`, `selectedId`, `detail`, `comments`, etc.)
- Initialize with appropriate default values

### Step 3: Create Data Transformation Layer
- Implement all data transformation useMemo hooks (see Data Transformation section)
- Transform `detail.transcriptData` → `segments`
- Transform `detail.transcriptData` → `displayTranscription`
- Transform `detail` → `videoMetadataData`
- Transform `detail` → `videoDescriptionData`
- Transform `comments` → `allComments`
- Transform `detail` → `videoInfo`

### Step 4: Add Handler Functions
- Implement all video handlers (handleTimeUpdate, handleSeek, etc.)
- Implement all comment handlers (handleCommentLike, handleReply, etc.)
- **PRESERVE:** Keep existing handlers (`loadList`, `loadDetail`, `handleAddComment`)
- **UPDATE:** Modify `saveStoredComments` to persist extended comment structure

### Step 5: Replace Video Player
- Replace `VideoPlayer` with `VideoPlayerContainer`
- Use `asset={{ url: detail.videoUrl }}` (preserve detail.videoUrl)
- Pass all required props including transformed `segments`
- Test video playback and controls

### Step 6: Replace Metadata Section
- Replace inline metadata with `VideoMetadata`
- Use transformed `videoMetadataData`
- Test like/share/save functionality

### Step 7: Replace Description Section
- Replace inline tags with `VideoDescription`
- Use transformed `videoDescriptionData`

### Step 8: Replace Timestamps Section
- Replace inline timestamps with `VideoTimestamps`
- Use transformed `displayTranscription`
- Test click-to-seek functionality

### Step 9: Replace Comments Section
- Replace inline comments with `CommentsSection`
- Use transformed `allComments` and `videoInfo`
- Implement all comment handlers
- Add `DeleteCommentModal`
- **UPDATE:** Modify `saveStoredComments` to persist replies, likes, dislikes

### Step 10: Replace Recommendations Section
- Replace mock recommendations with `RecommendationsSection`
- Pass empty array (video queue doesn't have recommendations API)

### Step 11: Replace Transcripts Section
- Replace `CollapsibleTranscripts` + `TranscriptPanel` with `TranscriptsSection`
- Use transformed `segments` from Step 3
- Pass segments and handlers

### Step 12: Testing
- **VERIFY:** Data source still uses video queue API (fetchVideoDetail, fetchVideoList)
- **VERIFY:** localStorage comments still persist per queueId
- Test all video functionality
- Test all comment features (add, edit, delete, reply, like, filter)
- Test timestamps click-to-seek
- Test localStorage persistence with extended comment structure
- Test visual consistency with InteractiveVideoPlayer
- Test search and breadcrumb functionality (should still work)

### Step 13: Cleanup
- Remove unused code (inline components, unused helpers)
- Remove unused state variables (if any)
- Optimize imports
- Update comments/documentation
- **VERIFY:** All video queue API calls still work

---

## Success Criteria

✅ **Integration is successful when:**
1. **Data Source Preserved:**
   - Video queue API calls still work (`fetchVideoDetail`, `fetchVideoList`, `syncVideoQueue`)
   - `detail` object still comes from video queue API
   - localStorage comments still persist per `queueId`
   - Search and breadcrumb functionality still works

2. **Components Integrated:**
   - All extracted components are integrated into VideoQueuePage
   - All components use transformed data from video queue API
   - Data transformation layer works correctly

3. **Functionality:**
   - All existing functionality is preserved
   - New features work (replies, likes, filters in comments)
   - Video playback and controls work correctly
   - Timestamps click-to-seek works
   - localStorage persistence works for extended comment structure

4. **Visual Consistency:**
   - Visual consistency achieved with InteractiveVideoPlayer
   - Same design, layout, and styling

5. **Code Quality:**
   - No console errors or warnings
   - All interactive elements respond correctly
   - Code is clean and maintainable
   - Data transformations are clear and documented

---

## Files to Modify

1. `upload_crms/client/src/pages/VideoQueuePage.jsx` - Main integration file

---

## Files to Reference

1. `upload_crms/client/src/components/InteractiveVideo/VideoPlayerContainer.jsx`
2. `upload_crms/client/src/components/InteractiveVideo/VideoMetadata.jsx`
3. `upload_crms/client/src/components/InteractiveVideo/VideoDescription.jsx`
4. `upload_crms/client/src/components/InteractiveVideo/VideoTimestamps.jsx`
5. `upload_crms/client/src/components/InteractiveVideo/CommentsSection.jsx`
6. `upload_crms/client/src/components/InteractiveVideo/RecommendationsSection.jsx`
7. `upload_crms/client/src/components/InteractiveVideo/TranscriptsSection.jsx`
8. `upload_crms/client/src/components/InteractiveVideo/DeleteCommentModal.jsx`
9. `upload_crms/client/src/utils/commentUtils.js`
10. `upload_crms/client/src/components/InteractiveVideo/InteractiveVideoPlayer.jsx` - Reference implementation

---

## Related Prompts

- PMT-074 - Refactor InteractiveVideoPlayer.jsx into Modular Components (source)
- PMT-073 - Create Main Prompt v6 (format reference)

---

## Key Differences from InteractiveVideoPlayer

### Data Source
- **InteractiveVideoPlayer:** Uses `asset` and `assetId` props, loads from asset API
- **VideoQueuePage:** Uses `detail` from video queue API (`fetchVideoDetail`, `fetchVideoList`)

### Comments Storage
- **InteractiveVideoPlayer:** Stores comments per `assetId` using `loadInteractions`, `saveInteractions`
- **VideoQueuePage:** Stores comments per `queueId` using `loadStoredComments`, `saveStoredComments`

### Recommendations
- **InteractiveVideoPlayer:** Receives `recommendations` as prop
- **VideoQueuePage:** Empty array (video queue API doesn't provide recommendations)

### Layout
- **InteractiveVideoPlayer:** Uses `lg:flex-row` layout with sticky positioning
- **VideoQueuePage:** Should use same layout structure for visual consistency

---

## Version History

### v2.0 (2025-12-10)
**Changes:**
- **CRITICAL UPDATE:** Clarified that video queue data source must be preserved
- Added explicit data transformation layer section
- Added "Key Differences from InteractiveVideoPlayer" section
- Updated all phases to emphasize data source preservation
- Added data transformation examples for each component
- Updated implementation steps to verify data source preservation
- Updated success criteria to include data source verification

### v1.0 (2025-12-10)
**Changes:**
- Initial creation of integration prompt
- Defined 7-phase integration plan
- Specified state management requirements
- Outlined data transformation needs
- Created step-by-step implementation guide

**Author:** AI & Automation Team

---

**Next Step:** Execute this prompt to integrate all components into VideoQueuePage.jsx while preserving video queue data source

