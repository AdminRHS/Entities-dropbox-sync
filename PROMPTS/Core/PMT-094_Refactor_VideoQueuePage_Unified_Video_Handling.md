---
PMT_ID: PMT-094
Title: Refactor VideoQueuePage - Unified Video Handling with Transcription Integration
Category: DEVELOPMENT
Department: DEV
Version: 1.0
Status: Draft
Created: 2025-12-11
Last_Updated: 2025-12-11
Author: Artem Skichko (EMP-88853)
Tags: [refactoring, video-player, youtube-integration, database, unified-handling, transcriptions]
Dependencies: [PMT-074, PMT-075]
Referenced_Entities: [VideoQueueEntry, Video models, InteractiveVideoPlayer components, Video_XXX.md files]
---

# Refactor VideoQueuePage - Unified Video Handling with Transcription Integration

## Purpose

Refactor the `VideoQueuePage.jsx` component to create a unified video handling system that:
- **Eliminates separate component**: Remove the standalone `VideoQueuePage.jsx` component
- **Unifies video sources**: Treat YouTube and other external platform videos (not uploaded locally as assets) at the same level as locally uploaded videos
- **Database-driven**: All videos (local and external) are retrieved from the database
- **Transcription integration**: Integrate transcriptions from `Video_XXX.md` files (Video_001.md, Video_002.md, Video_003.md, etc.)
- **Single source of truth**: Database becomes the single source for all video data and metadata

**Key Goals:**
1. Remove code duplication between VideoQueuePage and other video components
2. Create unified API and data models for all video types
3. Integrate transcriptions from file system into database workflow
4. Simplify maintenance by consolidating video handling logic

---

## Context

### Current Architecture

**VideoQueuePage.jsx:**
- **Location:** `upload_crms/client/src/pages/VideoQueuePage.jsx`
- **Size:** 365+ lines
- **Purpose:** Displays video queue entries from database (primarily YouTube videos)
- **Data Source:** `VideoQueueEntry` model from database
- **Features:**
  - Video list with search
  - Video player with InteractiveVideoPlayer components
  - Comments (stored in localStorage)
  - Transcripts display
  - Video metadata

**Video Models:**
- **VideoQueueEntry** (`upload_crms/src/models/VideoQueueEntry.ts`):
  - Fields: `queueId`, `videoId`, `title`, `channelName`, `videoUrl`, `duration`, `views`, `likes`, `status`, etc.
  - Relationship: `OneToOne` with `VideoTranscript`
  - Used for: YouTube/external platform videos

- **Video** (implied, for local assets):
  - Currently handled separately
  - Stored as local files/assets
  - Different API endpoints

**Transcription Files:**
- **Location:** `Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`
- **Format:** Markdown or JSON structured format
- **Examples:**
  - `Video_001.md` - GLIF Tutorial (Markdown format)
  - `Video_002.md` - Dual video: GLIF + Gemini RAG (JSON format)
  - `Video_003.md` - Kimi K2 Thinking (Markdown format)
- **Content:**
  - Video metadata (title, description, timestamps)
  - Full transcription with timestamps
  - Taxonomy analysis (workflows, actions, tools, objects)
  - Links and references

**Current Issues:**
1. **Separate Components:** VideoQueuePage is isolated from other video handling
2. **Different Data Sources:** Local videos vs. database videos handled differently
3. **No Transcription Integration:** Transcriptions in files not linked to database videos
4. **Code Duplication:** Similar logic in VideoQueuePage and other video components
5. **Inconsistent API:** Different endpoints for different video types

---

## Requirements

### Functional Requirements

**FR1: Unified Video Source**
- All videos (local and external) must be retrieved from database
- Single API endpoint for all video types
- Unified data model that supports both local and external videos

**FR2: Transcription Integration**
- Videos and transcriptions must be loaded from `Video_XXX.md` files
- File path: `Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`
- Support multiple formats:
  - Markdown format (Video_001.md, Video_003.md)
  - JSON format (Video_002.md)
- Parse and extract:
  - Video metadata (title, description, timestamps)
  - Full transcription with timestamps
  - Taxonomy analysis data
  - Links and references

**FR3: Component Removal**
- Remove `VideoQueuePage.jsx` as separate component
- Integrate functionality into unified video player component
- Reuse existing InteractiveVideoPlayer components

**FR4: Database Integration**
- Store transcription references in database
- Link `VideoQueueEntry` to transcription files
- Cache transcription data in database for performance

### Technical Requirements

**TR1: API Changes**
- Create unified endpoint: `GET /api/videos/:id` (replaces separate endpoints)
- Create transcription endpoint: `GET /api/videos/:id/transcript`
- Support loading transcriptions from file system
- Cache transcriptions in database after first load

**TR2: Data Model Updates**
- Extend `VideoQueueEntry` model:
  - Add `transcriptionFilePath` field (optional)
  - Add `transcriptionFormat` field (markdown/json)
  - Add `transcriptionCached` boolean flag
  - Add `transcriptionCachedAt` timestamp
- Create `VideoTranscript` model extension:
  - Support metadata from Video_XXX.md files
  - Store taxonomy analysis data
  - Store timestamps and segments

**TR3: File Parsing**
- Create parser for Markdown format (Video_001.md, Video_003.md):
  - Extract video title, description
  - Parse timestamps: `[00:00] text`
  - Extract links and metadata
- Create parser for JSON format (Video_002.md):
  - Parse JSON structure
  - Extract video objects from array
  - Handle multiple videos in one file

**TR4: Component Architecture**
- Remove `VideoQueuePage.jsx`
- Integrate into unified video component (or existing InteractiveVideoPlayer)
- Reuse components from PMT-074 extraction:
  - `VideoPlayerContainer`
  - `VideoMetadata`
  - `VideoDescription`
  - `VideoTimestamps`
  - `TranscriptsSection`
  - `CommentsSection`

### Constraints

**C1: Backward Compatibility**
- Existing VideoQueueEntry records must continue to work
- Existing API consumers should not break
- Gradual migration path

**C2: File System Access**
- Transcription files are in Dropbox folder structure
- Must handle file path resolution correctly
- Support both relative and absolute paths

**C3: Performance**
- Transcription parsing should be cached
- Avoid reading files on every request
- Database caching for frequently accessed transcriptions

### Acceptance Criteria

**AC1: Unified Video Loading**
- ✅ All videos (local and external) load from database
- ✅ Single API endpoint returns unified video data
- ✅ No distinction in frontend between video types

**AC2: Transcription Integration**
- ✅ Transcriptions load from Video_XXX.md files
- ✅ Both Markdown and JSON formats supported
- ✅ Transcription data displayed in video player
- ✅ Metadata from transcriptions shown in UI

**AC3: Component Removal**
- ✅ VideoQueuePage.jsx removed
- ✅ Functionality integrated into unified component
- ✅ No duplicate code between components

**AC4: Database Integration**
- ✅ Transcription references stored in database
- ✅ Transcription data cached after first load
- ✅ File system only accessed when cache miss

---

## Implementation Plan

### Phase 1: Data Model & API Updates (Days 1-2)

**Step 1.1: Extend VideoQueueEntry Model**
```typescript
// upload_crms/src/models/VideoQueueEntry.ts
@Column({ type: "varchar", length: 512, nullable: true })
transcriptionFilePath: string | null;

@Column({ type: "varchar", length: 32, nullable: true })
transcriptionFormat: "markdown" | "json" | null;

@Column({ type: "boolean", default: false })
transcriptionCached: boolean;

@Column({ type: "timestamp", nullable: true })
transcriptionCachedAt: Date | null;
```

**Step 1.2: Create Transcription Parser Service**
```typescript
// upload_crms/src/services/transcriptionParser.ts
export class TranscriptionParser {
  parseMarkdown(filePath: string): TranscriptionData
  parseJSON(filePath: string): TranscriptionData[]
  extractMetadata(content: string): VideoMetadata
  extractTimestamps(content: string): TimestampSegment[]
}
```

**Step 1.3: Update API Endpoints**
- Modify `GET /api/video-queue/:id` to include transcription data
- Create `GET /api/video-queue/:id/transcript` endpoint
- Add transcription loading logic with caching

**Step 1.4: Database Migration**
- Create migration to add new fields to VideoQueueEntry
- Backfill transcriptionFilePath for existing records (if applicable)

### Phase 2: Transcription File Integration (Days 2-3)

**Step 2.1: File System Service**
```typescript
// upload_crms/src/services/transcriptionFileService.ts
export class TranscriptionFileService {
  findTranscriptionFile(videoId: string): string | null
  readTranscriptionFile(filePath: string): string
  listAvailableTranscriptions(): string[]
  matchVideoToTranscription(video: VideoQueueEntry): string | null
}
```

**Step 2.2: Transcription Loading Logic**
- Implement file path resolution
- Parse transcription files based on format
- Cache parsed data in database
- Handle errors gracefully (file not found, parse errors)

**Step 2.3: API Integration**
- Update video detail endpoint to load transcriptions
- Add transcription endpoint that reads from file or cache
- Return transcription data in unified format

### Phase 3: Component Refactoring (Days 3-4)

**Step 3.1: Analyze VideoQueuePage Dependencies**
- Identify all functionality in VideoQueuePage.jsx
- Map to existing InteractiveVideoPlayer components
- Identify gaps that need new components

**Step 3.2: Create Unified Video Component**
- Create or extend existing video component
- Integrate VideoQueuePage functionality
- Use components from PMT-074 extraction
- Support both local and external videos

**Step 3.3: Update Routes**
- Remove VideoQueuePage route
- Update routes to use unified component
- Ensure backward compatibility

**Step 3.4: Migrate State Management**
- Move VideoQueuePage state to unified component
- Consolidate video loading logic
- Unify comment handling (currently in localStorage)

### Phase 4: Testing & Validation (Day 4-5)

**Step 4.1: Unit Tests**
- Test transcription parsers (Markdown and JSON)
- Test file system service
- Test API endpoints

**Step 4.2: Integration Tests**
- Test video loading from database
- Test transcription loading from files
- Test caching mechanism

**Step 4.3: Manual Testing**
- Test with Video_001.md (Markdown format)
- Test with Video_002.md (JSON format)
- Test with Video_003.md (Markdown format)
- Test with videos without transcriptions
- Test with local videos

**Step 4.4: Performance Testing**
- Measure transcription parsing time
- Test caching effectiveness
- Verify no performance regression

---

## Technical Specifications

### API Endpoints

**Unified Video Endpoint:**
```typescript
GET /api/videos/:id
Response: {
  id: string
  queueId: string
  videoId: string
  title: string
  videoUrl: string
  source: "local" | "youtube" | "external"
  transcription?: {
    filePath: string
    format: "markdown" | "json"
    cached: boolean
    data: TranscriptionData
  }
  // ... other fields
}
```

**Transcription Endpoint:**
```typescript
GET /api/videos/:id/transcript
Response: {
  videoId: string
  transcription: TranscriptionData
  cached: boolean
  cachedAt: Date | null
}
```

### Data Models

**Extended VideoQueueEntry:**
```typescript
@Entity()
export class VideoQueueEntry {
  // ... existing fields
  
  @Column({ type: "varchar", length: 512, nullable: true })
  transcriptionFilePath: string | null;
  
  @Column({ type: "varchar", length: 32, nullable: true })
  transcriptionFormat: "markdown" | "json" | null;
  
  @Column({ type: "boolean", default: false })
  transcriptionCached: boolean;
  
  @Column({ type: "timestamp", nullable: true })
  transcriptionCachedAt: Date | null;
}
```

**TranscriptionData Type:**
```typescript
interface TranscriptionData {
  videoTitle: string
  description: string
  timestamps: TimestampSegment[]
  links: Link[]
  metadata: {
    channel?: string
    duration?: string
    publishDate?: string
  }
  taxonomy?: {
    workflows?: Workflow[]
    actions?: Action[]
    tools?: Tool[]
    objects?: Object[]
  }
}

interface TimestampSegment {
  timestamp: string // "00:00"
  text: string
  line: string // full line with timestamp
}
```

### File Parsing

**Markdown Format Parser:**
```typescript
function parseMarkdownTranscription(content: string): TranscriptionData {
  // Extract video title: "Video Title: ..."
  // Extract description: "Video Description: ..."
  // Extract timestamps: "[00:00] text"
  // Extract links: "🔗 Links: ..."
  // Extract taxonomy analysis if present
}
```

**JSON Format Parser:**
```typescript
function parseJSONTranscription(content: string): TranscriptionData[] {
  // Parse JSON array
  // Extract video objects
  // Transform to TranscriptionData format
  // Handle multiple videos in one file
}
```

### Component Structure

**Unified Video Component:**
```typescript
// upload_crms/client/src/components/Video/UnifiedVideoPlayer.jsx
import VideoPlayerContainer from '../InteractiveVideo/VideoPlayerContainer'
import VideoMetadata from '../InteractiveVideo/VideoMetadata'
import VideoDescription from '../InteractiveVideo/VideoDescription'
import VideoTimestamps from '../InteractiveVideo/VideoTimestamps'
import TranscriptsSection from '../InteractiveVideo/TranscriptsSection'
import CommentsSection from '../InteractiveVideo/CommentsSection'

const UnifiedVideoPlayer = ({ videoId, source }) => {
  // Load video from unified API
  // Load transcription if available
  // Render using extracted components
}
```

### Utilities

**Transcription File Service:**
```typescript
// upload_crms/src/services/transcriptionFileService.ts
export class TranscriptionFileService {
  private basePath = "Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS"
  
  findTranscriptionFile(videoId: string): string | null {
    // Try Video_XXX.md pattern
    // Match by videoId or title
  }
  
  readTranscriptionFile(filePath: string): string {
    // Read file from file system
    // Handle errors
  }
  
  parseTranscription(content: string, format: "markdown" | "json"): TranscriptionData {
    // Route to appropriate parser
  }
}
```

**Video Source Unifier:**
```typescript
// upload_crms/src/utils/videoSourceUnifier.ts
export function unifyVideoSource(video: VideoQueueEntry | LocalVideo): UnifiedVideo {
  // Normalize video data
  // Determine source type
  // Return unified format
}
```

---

## Success Criteria

### Functional Success

**✅ Unified Video Handling**
- All videos load from database regardless of source
- Single API endpoint works for all video types
- No distinction in UI between local and external videos

**✅ Transcription Integration**
- Transcriptions load from Video_XXX.md files
- Both Markdown and JSON formats work correctly
- Transcription data displays in video player
- Metadata from transcriptions shown correctly

**✅ Component Removal**
- VideoQueuePage.jsx successfully removed
- All functionality preserved in unified component
- No duplicate code

**✅ Database Integration**
- Transcription references stored correctly
- Caching works as expected
- File system accessed only when needed

### Technical Success

**✅ Performance**
- Transcription parsing < 500ms for typical files
- Caching reduces file system access by 90%+
- No performance regression in video loading

**✅ Code Quality**
- No code duplication
- Clear separation of concerns
- Proper error handling
- Type safety maintained

**✅ Testing**
- Unit tests cover parsers and services
- Integration tests cover API endpoints
- Manual testing confirms all features work

### Metrics

**Code Reduction:**
- VideoQueuePage.jsx: 365+ lines removed
- Duplicate code eliminated: ~200 lines
- Net reduction: ~150-200 lines

**Performance:**
- Transcription loading: < 500ms (first load)
- Transcription loading: < 50ms (cached)
- Video loading: No regression

**Maintainability:**
- Single source of truth for video handling
- Clear component boundaries
- Easier to add new video sources

---

## Deliverables

1. **Extended Data Models**
   - Updated `VideoQueueEntry` model with transcription fields
   - Database migration script

2. **Transcription Services**
   - `TranscriptionParser` service (Markdown and JSON)
   - `TranscriptionFileService` for file system access
   - Caching implementation

3. **API Updates**
   - Unified video endpoint
   - Transcription endpoint
   - Updated controllers

4. **Component Refactoring**
   - Removed `VideoQueuePage.jsx`
   - Unified video component
   - Updated routes

5. **Documentation**
   - API documentation updates
   - Component usage guide
   - Transcription file format documentation

6. **Tests**
   - Unit tests for parsers
   - Integration tests for API
   - Manual test checklist

---

## Related Prompts

- **PMT-074** - Refactor InteractiveVideoPlayer.jsx into Modular Components (component extraction)
- **PMT-075** - Integrate Components To VideoQueuePage (previous integration work)
- **PMT-004** - Video Transcription v4.1 (transcription processing)

---

## Version History

### v1.0 (2025-12-11)
**Changes:**
- Initial creation of PMT-094
- Defined unified video handling requirements
- Specified transcription integration from Video_XXX.md files
- Outlined component removal and refactoring plan

**Author:** Artem Skichko (EMP-88853)

---

**Next Step:** Execute this prompt to begin refactoring VideoQueuePage with transcription integration

