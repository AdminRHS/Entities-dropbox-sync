---
PMT_ID: PMT-074
Title: Refactor InteractiveVideoPlayer.jsx into Modular Components
Category: CORE
Department: Dev
Version: 1.0
Status: Draft
Created: 2025-12-10
Last_Updated: 2025-12-10
Author: AI & Automation Team
Tags: [refactoring, component-extraction, react, modular-architecture, code-organization]
Dependencies: []
Referenced_Entities: []
---

# Refactor InteractiveVideoPlayer.jsx into Modular Components

## Purpose
Break down the monolithic `InteractiveVideoPlayer.jsx` component (~2542 lines) into smaller, reusable, maintainable components following React best practices and modular architecture principles.

## Context
**Current State:**
- Single file: `upload_crms/client/src/components/InteractiveVideo/InteractiveVideoPlayer.jsx`
- Size: ~2542 lines
- Contains: Main component + RecommendationCard component + all UI sections inline
- Issues:
  - Difficult to maintain and test
  - Hard to reuse sections in other components
  - Complex state management in one place
  - Poor code organization and readability

**Target State:**
- Main component: `InteractiveVideoPlayer.jsx` (~200-300 lines) - orchestration only
- Extracted components: 8-10 focused, reusable components
- Better separation of concerns
- Easier testing and maintenance
- Reusable components for other pages

---

## Design Philosophy

### Core Principles

**1. Single Responsibility**
- Each component handles one UI section or feature
- Clear props interface
- Minimal dependencies

**2. Reusability**
- Components can be used in VideoQueuePage, AssetDetailPage, etc.
- Generic props, not tightly coupled to InteractiveVideoPlayer

**3. Maintainability**
- Smaller files easier to understand and modify
- Clear component boundaries
- Self-contained logic

**4. Performance**
- Use React.memo where appropriate
- Optimize re-renders with proper dependencies
- Preserve existing optimizations

---

## Component Extraction Plan

### Current Structure Analysis

**Main Sections Identified:**
1. **RecommendationCard** (lines 22-620) - Already separate but inside file
2. **Video Player Container** (lines 1594-1704) - Video + loading + controls + layers
3. **Video Title & Metadata** (lines 1706-1790) - Title, author, action buttons
4. **Video Description** (lines 1793-1823) - Tags, description text
5. **Timestamps Section** (lines 1826-1973) - Transcript timestamps list
6. **Comments Section** (lines 1975-2467) - Comments list, input, filters, replies
7. **Right Sidebar: Transcripts** (lines 2470-2484) - Collapsible transcripts
8. **Right Sidebar: Recommendations** (lines 2486-2500) - Recommendations list
9. **Delete Comment Modal** (lines 2504-2536) - Confirmation dialog

**State Management:**
- Video state: `currentTime`, `videoDuration`, `isPlaying`, `volume`, `isFullscreen`, `videoLoading`, `videoLoadProgress`
- Interaction state: `segments`, `interactions`, `activeSegmentId`, `commentText`
- UI state: `isLiked`, `isSaved`, `likeCount`, `isTranscriptsExpanded`
- Comments state: `commentLikes`, `commentDislikes`, `commentReplies`, `replyingTo`, `editingCommentId`, etc.

---

## Extracted Components Structure

### Component 1: VideoPlayerContainer
**File:** `components/InteractiveVideo/VideoPlayerContainer.jsx`
**Lines:** ~110 (1594-1704)

**Props:**
```typescript
{
  videoRef: RefObject<HTMLVideoElement>
  videoContainerRef: RefObject<HTMLDivElement>
  videoUrl: string
  videoColors: { glow: string }
  videoLoading: boolean
  videoLoadProgress: number
  videoDuration: number
  currentTime: number
  isPlaying: boolean
  volume: number
  isFullscreen: boolean
  segments: Segment[]
  reactions: Reaction[]
  comments: Comment[]
  commentText: string
  onTimeUpdate: () => void
  onPlay: () => void
  onPause: () => void
  onVolumeChange: (volume: number) => void
  onSeek: (time: number) => void
  onFullscreen: () => void
  onCommentTextChange: (text: string) => void
  onAddComment: () => void
  onAddReaction: (emoji: string) => void
}
```

**Contains:**
- Video player with glow effect
- Loading skeleton
- CustomVideoControls
- ReactionAnimationsLayer
- DynamicCommentsLayer

**Dependencies:**
- VideoPlayer
- CustomVideoControls
- ReactionAnimationsLayer
- DynamicCommentsLayer
- useVideoColorAnalysis (hook)

---

### Component 2: VideoMetadata
**File:** `components/InteractiveVideo/VideoMetadata.jsx`
**Lines:** ~85 (1706-1790)

**Props:**
```typescript
{
  video: {
    title: string
    createdBy: string
    createdAt: string
    isPublic: boolean
  }
  isLiked: boolean
  isSaved: boolean
  likeCount: number
  onLike: () => void
  onShare: () => void
  onSave: () => void
  formatDateTime: (date: string) => string
}
```

**Contains:**
- Video title
- Author info with avatar
- Action buttons (Like, Share, Save)

**Dependencies:**
- MdThumbUp, MdShare, MdBookmark icons

---

### Component 3: VideoDescription
**File:** `components/InteractiveVideo/VideoDescription.jsx`
**Lines:** ~30 (1793-1823)

**Props:**
```typescript
{
  video: {
    location?: string
    duration?: string
    description?: string
  }
  formatDuration: (duration: string) => string
}
```

**Contains:**
- Metadata tags (location, duration, categories)
- Description text

---

### Component 4: VideoTimestamps
**File:** `components/InteractiveVideo/VideoTimestamps.jsx`
**Lines:** ~150 (1826-1973)

**Props:**
```typescript
{
  displayTranscription: Array<{ time: string, text: string }>
  showAllTimestamps: boolean
  onToggleShowAll: () => void
  currentTime: number
  videoRef: RefObject<HTMLVideoElement>
  segments: Segment[]
  onSeek: (time: number) => void
  formatTimeForDisplay: (time: string) => string
}
```

**Contains:**
- Timestamps list (first 10 or all)
- "Show more" / "collapse" button
- Click-to-seek functionality

**Note:** Already uses TranscriptPanel component, can be simplified further

---

### Component 5: CommentsSection
**File:** `components/InteractiveVideo/CommentsSection.jsx`
**Lines:** ~490 (1975-2467)

**Props:**
```typescript
{
  allComments: Comment[]
  commentSortOrder: 'newest' | 'oldest'
  showFilterMenu: boolean
  newCommentText: string
  commentLikes: Record<string, boolean>
  commentDislikes: Record<string, boolean>
  commentReplies: Record<string, Reply[]>
  replyingTo: string | null
  replyText: string
  editingCommentId: string | null
  editCommentText: string
  editingReplyId: { commentId: string, replyId: string } | null
  editReplyText: string
  hiddenReplies: Set<string>
  userDisplayName: string
  currentTime: number
  onSortOrderChange: (order: 'newest' | 'oldest') => void
  onFilterMenuToggle: () => void
  onNewCommentChange: (text: string) => void
  onAddComment: (text: string) => void
  onCommentLike: (commentId: string) => void
  onCommentDislike: (commentId: string) => void
  onReply: (commentId: string) => void
  onSubmitReply: (commentId: string, text: string) => void
  onEditReply: (commentId: string, replyId: string) => void
  onUpdateReply: (commentId: string, replyId: string, text: string) => void
  onDeleteReply: (commentId: string, replyId: string) => void
  onEditComment: (commentId: string) => void
  onUpdateComment: (commentId: string, text: string) => void
  onDeleteComment: (commentId: string) => void
  onToggleReplies: (commentId: string) => void
  formatTimeAgo: (time: string) => string
}
```

**Contains:**
- Comments header with filter
- New comment input
- Comments list with replies
- Reply input
- Edit/delete functionality

**Sub-components to extract:**
- CommentItem
- ReplyItem
- CommentInput
- CommentFilter

---

### Component 6: TranscriptsSection
**File:** `components/InteractiveVideo/TranscriptsSection.jsx`
**Lines:** ~15 (2470-2484)

**Props:**
```typescript
{
  segments: Segment[]
  activeSegmentId: string | null
  isExpanded: boolean
  onToggle: () => void
  onSegmentClick: (segment: Segment) => void
}
```

**Contains:**
- CollapsibleTranscripts wrapper
- SegmentList

**Dependencies:**
- CollapsibleTranscripts
- SegmentList

---

### Component 7: RecommendationsSection
**File:** `components/InteractiveVideo/RecommendationsSection.jsx`
**Lines:** ~15 (2486-2500)

**Props:**
```typescript
{
  recommendations: Recommendation[]
  onNavigate: (path: string) => void
  maxItems?: number
}
```

**Contains:**
- Recommendations list
- RecommendationCard components

**Dependencies:**
- RecommendationCard

---

### Component 8: DeleteCommentModal
**File:** `components/InteractiveVideo/DeleteCommentModal.jsx`
**Lines:** ~35 (2504-2536)

**Props:**
```typescript
{
  isOpen: boolean
  onClose: () => void
  onConfirm: () => void
}
```

**Contains:**
- Confirmation dialog
- Cancel/Delete buttons

---

### Component 9: RecommendationCard (Extract to separate file)
**File:** `components/InteractiveVideo/RecommendationCard.jsx`
**Lines:** ~600 (22-620)

**Props:**
```typescript
{
  recommendation: {
    id: string
    title: string
    thumbnailUrl?: string
    url: string
    duration?: string
    createdBy?: string
    createdAt?: string
    isPublic?: boolean
  }
  onNavigate: (path: string) => void
}
```

**Contains:**
- Thumbnail loading logic
- Video preview generation
- Card UI with duration badge

**Note:** Already separate component, just needs to be moved to own file

---

## Implementation Steps

### Phase 1: Extract Simple Components (Low Risk)
**Estimated Time:** 1-2 hours

1. **Extract RecommendationCard**
   - Move to `RecommendationCard.jsx`
   - Update imports in InteractiveVideoPlayer
   - Test: Recommendations display correctly

2. **Extract DeleteCommentModal**
   - Create `DeleteCommentModal.jsx`
   - Move modal JSX and logic
   - Test: Modal opens/closes, delete works

3. **Extract RecommendationsSection**
   - Create `RecommendationsSection.jsx`
   - Move recommendations list rendering
   - Test: Recommendations display

4. **Extract TranscriptsSection**
   - Create `TranscriptsSection.jsx`
   - Move CollapsibleTranscripts wrapper
   - Test: Transcripts expand/collapse, segments click

---

### Phase 2: Extract Medium Components (Medium Risk)
**Estimated Time:** 2-3 hours

5. **Extract VideoMetadata**
   - Create `VideoMetadata.jsx`
   - Move title, author, action buttons
   - Extract like/share/save handlers
   - Test: Buttons work, metadata displays

6. **Extract VideoDescription**
   - Create `VideoDescription.jsx`
   - Move tags and description
   - Test: Tags and description display

7. **Extract VideoTimestamps**
   - Create `VideoTimestamps.jsx`
   - Move timestamps list (already uses TranscriptPanel)
   - Test: Timestamps click-to-seek works

---

### Phase 3: Extract Complex Components (High Risk)
**Estimated Time:** 3-4 hours

8. **Extract CommentsSection**
   - Create `CommentsSection.jsx`
   - Move all comments logic
   - Extract sub-components:
     - `CommentItem.jsx`
     - `ReplyItem.jsx`
     - `CommentInput.jsx`
     - `CommentFilter.jsx`
   - Test: All comment features work (add, edit, delete, reply, like, filter)

9. **Extract VideoPlayerContainer**
   - Create `VideoPlayerContainer.jsx`
   - Move video player + controls + layers
   - Extract video event handlers
   - Test: Video plays, controls work, reactions/comments display

---

### Phase 4: Refactor Main Component (Final)
**Estimated Time:** 1-2 hours

10. **Refactor InteractiveVideoPlayer**
    - Keep only orchestration logic
    - Import all extracted components
    - Pass props to components
    - Remove extracted code
    - Test: All features work as before

---

## File Structure After Refactoring

```
components/InteractiveVideo/
├── InteractiveVideoPlayer.jsx          (~200-300 lines) - Main orchestration
├── VideoPlayerContainer.jsx            (~110 lines) - Video + controls
├── VideoMetadata.jsx                   (~85 lines) - Title, author, actions
├── VideoDescription.jsx                 (~30 lines) - Tags, description
├── VideoTimestamps.jsx                  (~150 lines) - Timestamps list
├── CommentsSection.jsx                  (~200 lines) - Comments container
│   ├── CommentItem.jsx                 (~150 lines) - Single comment
│   ├── ReplyItem.jsx                    (~100 lines) - Single reply
│   ├── CommentInput.jsx                 (~50 lines) - Comment input
│   └── CommentFilter.jsx                (~30 lines) - Filter dropdown
├── TranscriptsSection.jsx               (~15 lines) - Transcripts wrapper
├── RecommendationsSection.jsx          (~15 lines) - Recommendations wrapper
├── RecommendationCard.jsx             (~600 lines) - Recommendation card
├── DeleteCommentModal.jsx               (~35 lines) - Delete confirmation
├── VideoPlayer.jsx                      (existing)
├── SegmentList.jsx                      (existing)
├── CustomVideoControls.jsx              (existing)
├── DynamicCommentsLayer.jsx             (existing)
├── ReactionAnimationsLayer.jsx         (existing)
└── useVideoSegmentation.js              (existing)
```

**Total:** ~1,500 lines distributed across 13+ focused components

---

## Component Props Interface Standards

### Naming Conventions
- Props use camelCase
- Event handlers: `on{Action}` (e.g., `onLike`, `onSeek`)
- State setters: `on{State}Change` (e.g., `onCommentTextChange`)
- Boolean flags: `is{State}` or `has{Feature}` (e.g., `isLiked`, `hasReplies`)

### Required vs Optional
- Mark optional props with `?` in TypeScript
- Provide default values where appropriate
- Document required props in JSDoc

### State Management
- Lift state up to InteractiveVideoPlayer when needed by multiple components
- Keep local state in components when isolated
- Use callbacks for parent-child communication

---

## Testing Strategy

### Unit Tests (Per Component)
- Test component renders with required props
- Test event handlers fire correctly
- Test conditional rendering
- Test edge cases (empty data, null values)

### Integration Tests
- Test component interactions
- Test data flow between components
- Test state synchronization

### Visual Regression
- Compare before/after screenshots
- Ensure no visual changes
- Verify responsive behavior

---

## Migration Checklist

### Pre-Refactoring
- [ ] Create backup branch
- [ ] Document current behavior
- [ ] List all props and state
- [ ] Identify dependencies

### During Refactoring
- [ ] Extract one component at a time
- [ ] Test after each extraction
- [ ] Update imports
- [ ] Verify no functionality lost

### Post-Refactoring
- [ ] All tests pass
- [ ] No console errors
- [ ] Visual regression check
- [ ] Performance check (no regressions)
- [ ] Code review
- [ ] Update documentation

---

## Success Criteria

✅ **Refactoring is successful when:**
1. **Size Reduction:** Main component < 300 lines (from 2542)
2. **Component Count:** 8-10 focused components created
3. **Functionality:** All features work identically
4. **Reusability:** Components can be used in VideoQueuePage
5. **Maintainability:** Each component < 200 lines
6. **Performance:** No performance regressions
7. **Tests:** All existing tests pass + new component tests added

---

## Risk Mitigation

### High-Risk Areas
1. **CommentsSection** - Complex state, many interactions
   - **Mitigation:** Extract sub-components first, test thoroughly
   
2. **VideoPlayerContainer** - Critical video functionality
   - **Mitigation:** Preserve all event handlers, test video playback

3. **State Management** - Many shared state variables
   - **Mitigation:** Document state flow, use TypeScript for type safety

### Rollback Plan
- Keep original file as `InteractiveVideoPlayer.old.jsx`
- Use feature flag to switch between old/new versions
- Gradual migration: extract one component, test, commit

---

## Deliverables

1. **Extracted Components** - 8-10 new component files
2. **Refactored Main Component** - Simplified InteractiveVideoPlayer.jsx
3. **Updated Imports** - All files importing InteractiveVideoPlayer updated
4. **Component Documentation** - JSDoc comments for each component
5. **Migration Guide** - How to use new components
6. **Test Suite** - Unit tests for each component

---

## Related Files

**Files to Update:**
- `upload_crms/client/src/pages/AssetDetailPage.jsx` (if uses InteractiveVideoPlayer)
- `upload_crms/client/src/pages/VideoQueuePage.jsx` (can reuse components)
- Any other files importing InteractiveVideoPlayer

**Dependencies:**
- Existing hooks: `useVideoSegmentation`, `useVideoColorAnalysis`
- Existing components: `VideoPlayer`, `SegmentList`, `CustomVideoControls`
- Existing utils: `time.js`, `throttle.js`, `persistence.js`

---

## Version History

### v1.0 (2025-12-10)
**Changes:**
- Initial creation of refactoring prompt
- Component extraction plan defined
- 8-10 components identified
- Implementation phases outlined

**Author:** AI & Automation Team

---

**Next Step:** Execute this prompt to refactor InteractiveVideoPlayer.jsx

