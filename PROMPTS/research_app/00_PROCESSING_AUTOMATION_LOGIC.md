# Video Processing Automation Logic

**Source:** `ENTITIES/TASK_MANAGERS/RESEARCHES/scripts/`
**Purpose:** Extract business logic from existing Python automation scripts for web app implementation

---

## Overview

The Research Management System currently uses Python scripts to automate video processing (Phases 2-5). This document extracts the core logic, validation rules, and workflows to implement in the web apps.

**Time Savings:** Automation reduced manual processing from **1.5-2 hours → 5-10 minutes per video**

---

## Processing Workflow (From process_video.py)

### Master Orchestrator Flow

```
User initiates video processing (Video_024)
    ↓
Phase 1: ID Scan
    - Scan all LIBRARIES directories
    - Discover next available entity IDs
    - Return: { workflows: "WRF-025", actions: "ACTION-433", skills: "SKL-065" }
    ↓
Phase 2: Gap Analysis
    - Parse Video_024.md transcription
    - Compare entities vs existing LIBRARIES
    - Classify as NEW/EXISTING/UPDATE
    - Generate gap analysis report
    ↓
Phase 3: JSON Update
    - Backup existing JSON files (timestamped)
    - Integrate NEW entities into LIBRARIES
    - Update master files and indexes
    - Validate all changes
    ↓
Phase 4: Report Generation
    - Create integration report (markdown + JSON)
    - Include statistics and summaries
    - Validate cross-references
    - Provide next step recommendations
    ↓
Result: Video fully processed, entities integrated
```

### Implementation in Web App

**Video Processing App should replicate this flow:**

1. **Upload Transcription** → Phase 1 complete
2. **Run Entity Extraction** → AI extracts entities → Phase 2 complete
3. **Gap Analysis** → Compare vs existing tools → Phase 3 complete
4. **Integration** → Merge with libraries → Phase 4 complete
5. **Knowledge Mapping** → Generate relationships → Phase 5 complete

---

## Entity ID Management (From video_id_scanner.py)

### Next ID Discovery Logic

**Problem:** When adding new entities, need to find next available sequential ID

**Solution:** Scan all JSON files, extract current IDs, calculate next

```typescript
// TypeScript equivalent of Python ID scanner

interface NextIDs {
  workflows: string;      // "WRF-025"
  actions: {
    command: string;      // "ACTION-433"
    master: string;       // "ACTION-439"
  };
  objects: {
    [department: string]: string;  // "OBJ-SMM-015", "OBJ-VID-022"
  };
  skills: string;         // "SKL-065"
  tools: {
    [category: string]: string;    // "TOOL-AI-223", "TOOL-VID-045"
  };
}

async function scanNextIDs(): Promise<NextIDs> {
  // 1. Scan workflows directory
  const workflowFiles = await glob('LIBRARIES/Workflows/*.json');
  const workflowIDs = workflowFiles.map(f => extractID(f, /WRF-(\d{3})/));
  const nextWorkflow = `WRF-${padZero(Math.max(...workflowIDs) + 1, 3)}`;

  // 2. Scan actions directory
  const actionFiles = await glob('LIBRARIES/Responsibilities/Actions/**/*.json');
  const actionIDs = actionFiles.map(f => extractID(f, /ACTION-(\d{3})/));
  const nextAction = `ACTION-${padZero(Math.max(...actionIDs) + 1, 3)}`;

  // 3. Scan objects by department
  const objectsByDept = {};
  for (const dept of ['SMM', 'VID', 'DEV', 'AID']) {
    const objFiles = await glob(`LIBRARIES/Responsibilities/Objects/${dept}*.json`);
    const objIDs = objFiles.map(f => extractID(f, /OBJ-${dept}-(\d{3})/));
    objectsByDept[dept] = `OBJ-${dept}-${padZero(Math.max(...objIDs) + 1, 3)}`;
  }

  // 4. Return next IDs
  return {
    workflows: nextWorkflow,
    actions: { command: nextAction, master: nextAction },
    objects: objectsByDept,
    skills: `SKL-${padZero(nextSkillID, 3)}`,
    tools: { AI: `TOOL-AI-${padZero(nextToolID, 3)}` }
  };
}

function padZero(num: number, width: number): string {
  return num.toString().padStart(width, '0');
}
```

### Validation Patterns

```typescript
const ENTITY_PATTERNS = {
  workflow: /^WRF-\d{3}$/,
  action: /^ACTION-\d{3}$/,
  skill: /^SKL-\d{3}$/,
  object: /^OBJ-[A-Z]{3}-\d{3}$/,     // OBJ-SMM-015
  tool: /^TOOL-[A-Z]{2,5}-\d{3}$/     // TOOL-AI-223
};

function validateEntityID(id: string, type: string): boolean {
  return ENTITY_PATTERNS[type].test(id);
}
```

---

## Gap Analysis Logic (From video_gap_analyzer.py)

### Entity Classification

**Goal:** Determine if extracted entity is NEW, EXISTING, or needs UPDATE

```typescript
interface Entity {
  id: string;
  name: string;
  type: 'workflow' | 'action' | 'tool' | 'object' | 'skill';
  description: string;
  department: string[];
}

interface GapAnalysisResult {
  new: Entity[];         // Not in libraries, needs creation
  existing: Entity[];    // Already in libraries, skip
  update: Entity[];      // In libraries but different info, needs review
}

async function analyzeGaps(extractedEntities: Entity[]): Promise<GapAnalysisResult> {
  const result: GapAnalysisResult = { new: [], existing: [], update: [] };

  // Load existing libraries
  const existingTools = await loadJSON('LIBRARIES/Tools/AI_Tools/*.json');
  const existingWorkflows = await loadJSON('LIBRARIES/Workflows/*.json');

  for (const entity of extractedEntities) {
    if (entity.type === 'tool') {
      // Check if tool name exists
      const match = existingTools.find(t =>
        t.name.toLowerCase() === entity.name.toLowerCase()
      );

      if (!match) {
        result.new.push(entity);
      } else if (hasConflict(entity, match)) {
        result.update.push({ ...entity, conflictsWith: match.id });
      } else {
        result.existing.push(entity);
      }
    }

    // Similar logic for workflows, actions, etc.
  }

  return result;
}

function hasConflict(extracted: Entity, existing: Entity): boolean {
  // Check if descriptions differ significantly
  if (extracted.description !== existing.description) return true;

  // Check if departments differ
  const deptDiff = extracted.department.filter(d =>
    !existing.department.includes(d)
  );
  if (deptDiff.length > 0) return true;

  return false;
}
```

### Gap Analysis Output

```typescript
interface GapSummary {
  total_extracted: number;
  new_count: number;
  existing_count: number;
  update_count: number;
  by_type: {
    workflows: { new: number; existing: number; update: number; };
    actions: { new: number; existing: number; update: number; };
    tools: { new: number; existing: number; update: number; };
  };
}

// Example output
const gapSummary: GapSummary = {
  total_extracted: 25,
  new_count: 12,
  existing_count: 10,
  update_count: 3,
  by_type: {
    workflows: { new: 3, existing: 1, update: 0 },
    actions: { new: 8, existing: 5, update: 2 },
    tools: { new: 1, existing: 4, update: 1 }
  }
};
```

---

## JSON Update Logic (From video_json_updater.py)

### Safe Update Process

```typescript
interface UpdateOperation {
  file: string;
  operation: 'create' | 'update' | 'append';
  entity: Entity;
}

async function updateLibraries(
  newEntities: Entity[],
  updateEntities: Entity[],
  dryRun: boolean = false
): Promise<UpdateResult> {

  const operations: UpdateOperation[] = [];

  // 1. Create backup before any modifications
  if (!dryRun) {
    await backupAllLibraries();
  }

  try {
    // 2. Process NEW entities
    for (const entity of newEntities) {
      const targetFile = getTargetFile(entity);

      if (dryRun) {
        console.log(`[DRY RUN] Would create: ${entity.id} in ${targetFile}`);
      } else {
        // Create new JSON file or append to master
        await createEntity(targetFile, entity);
        operations.push({ file: targetFile, operation: 'create', entity });
      }
    }

    // 3. Process UPDATE entities
    for (const entity of updateEntities) {
      const targetFile = getTargetFile(entity);

      if (dryRun) {
        console.log(`[DRY RUN] Would update: ${entity.id} in ${targetFile}`);
      } else {
        // Update existing entity with new info
        await updateEntity(targetFile, entity);
        operations.push({ file: targetFile, operation: 'update', entity });
      }
    }

    // 4. Update master indexes
    if (!dryRun) {
      await updateMasterIndexes(operations);
    }

    return { success: true, operations };

  } catch (error) {
    // Rollback on error (restore from backup)
    if (!dryRun) {
      await rollbackFromBackup();
    }
    throw error;
  }
}
```

### Backup System

```typescript
async function backupAllLibraries(): Promise<void> {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const backupDir = `_backups/${timestamp}`;

  // Backup all JSON files
  const files = await glob('LIBRARIES/**/*.json');
  for (const file of files) {
    const backupPath = `${backupDir}/${file}`;
    await copyFile(file, backupPath);
  }

  console.log(`Backup created: ${backupDir}`);
}

async function rollbackFromBackup(): Promise<void> {
  const latestBackup = await getLatestBackup();
  const files = await glob(`${latestBackup}/**/*.json`);

  for (const backupFile of files) {
    const originalPath = backupFile.replace(latestBackup, 'LIBRARIES');
    await copyFile(backupFile, originalPath);
  }

  console.log(`Rolled back from: ${latestBackup}`);
}
```

---

## Progress Tracking (From analyze_video_phases.py)

### Phase Completion Tracking

```typescript
interface VideoProgress {
  video_number: number;
  title: string;
  current_phase: Phase;
  status: 'Pending' | 'In Progress' | 'Complete' | 'Failed';
  phases: {
    Phase_0_Queued: Date | null;
    Phase_1_Transcribed: Date | null;
    Phase_2_Extraction: Date | null;
    Phase_3_Gap_Analysis: Date | null;
    Phase_4_Integration: Date | null;
    Phase_5_Mapping: Date | null;
    Complete: Date | null;
  };
}

async function updateVideoProgress(
  videoId: number,
  phase: Phase,
  status: 'start' | 'complete' | 'fail'
): Promise<void> {
  const progress = await getVideoProgress(videoId);

  if (status === 'complete') {
    progress.phases[phase] = new Date();

    // Auto-advance to next phase
    const nextPhase = getNextPhase(phase);
    if (nextPhase) {
      progress.current_phase = nextPhase;
    } else {
      progress.current_phase = 'Complete';
      progress.status = 'Complete';
    }
  }

  await saveVideoProgress(videoId, progress);
}

function getNextPhase(current: Phase): Phase | null {
  const phaseOrder: Phase[] = [
    'Phase_0_Queued',
    'Phase_1_Transcribed',
    'Phase_2_Extraction',
    'Phase_3_Gap_Analysis',
    'Phase_4_Integration',
    'Phase_5_Mapping',
    'Complete'
  ];

  const currentIndex = phaseOrder.indexOf(current);
  return phaseOrder[currentIndex + 1] || null;
}
```

### Dashboard Statistics

```typescript
interface DashboardStats {
  total_videos: number;
  by_phase: {
    [phase: string]: number;
  };
  completion_rate: number;
  avg_processing_time: string;
}

async function calculateDashboardStats(): Promise<DashboardStats> {
  const allVideos = await getAllVideos();

  const stats: DashboardStats = {
    total_videos: allVideos.length,
    by_phase: {},
    completion_rate: 0,
    avg_processing_time: '0h'
  };

  // Count videos in each phase
  for (const video of allVideos) {
    const phase = video.current_phase;
    stats.by_phase[phase] = (stats.by_phase[phase] || 0) + 1;
  }

  // Calculate completion rate
  const completed = stats.by_phase['Complete'] || 0;
  stats.completion_rate = (completed / stats.total_videos) * 100;

  return stats;
}
```

---

## Validation Rules

### Department Codes

```typescript
const VALID_DEPARTMENTS = [
  'AID',  // AI & Automations
  'DEV',  // Development
  'VID',  // Video
  'SMM',  // Social Media Marketing
  'DGN',  // Design
  'MKT',  // Marketing
  'HRM',  // Human Resources
  'SLS',  // Sales
  'LGN'   // Lead Generation
];

function validateDepartment(code: string): boolean {
  return VALID_DEPARTMENTS.includes(code);
}
```

### Required Fields

```typescript
interface EntityValidation {
  workflow: string[];
  action: string[];
  tool: string[];
  object: string[];
  skill: string[];
}

const REQUIRED_FIELDS: EntityValidation = {
  workflow: ['id', 'name', 'objective', 'tasks', 'duration', 'complexity', 'department'],
  action: ['id', 'name', 'description', 'category'],
  tool: ['id', 'name', 'category', 'vendor', 'purpose'],
  object: ['id', 'name', 'department', 'description'],
  skill: ['id', 'name', 'action', 'object', 'tool']
};

function validateEntity(entity: Entity): ValidationResult {
  const requiredFields = REQUIRED_FIELDS[entity.type];
  const missing = requiredFields.filter(field => !entity[field]);

  return {
    valid: missing.length === 0,
    missing_fields: missing,
    errors: missing.map(f => `Missing required field: ${f}`)
  };
}
```

---

## Error Handling

### Common Error Scenarios

```typescript
enum ProcessingError {
  TRANSCRIPTION_NOT_FOUND = 'Transcription file not found',
  INVALID_ENTITY_ID = 'Invalid entity ID format',
  DUPLICATE_ENTITY = 'Entity already exists in libraries',
  MISSING_REQUIRED_FIELD = 'Missing required field in entity',
  JSON_PARSE_ERROR = 'Failed to parse JSON file',
  BACKUP_FAILED = 'Failed to create backup',
  PERMISSION_DENIED = 'Permission denied accessing file'
}

function handleProcessingError(error: Error, context: string): void {
  console.error(`Error in ${context}: ${error.message}`);

  // Log to file
  logError({
    timestamp: new Date(),
    context,
    error: error.message,
    stack: error.stack
  });

  // Attempt rollback if in update phase
  if (context.includes('update')) {
    rollbackFromBackup();
  }
}
```

---

## Performance Metrics

### Time Savings

**Manual Process (Before Automation):**
- Phase 2 (Extraction): 30-45 minutes
- Phase 3 (Gap Analysis): 30-45 minutes
- Phase 4 (Integration): 45-60 minutes
- Phase 5 (Reporting): 20-30 minutes
- **Total: 1.5-2 hours per video**

**Automated Process (With Scripts):**
- Full workflow: 5-10 minutes
- **Time saved: ~90% reduction**

**Goal for Web App:**
- Match or exceed script performance
- Add real-time progress updates
- Enable parallel processing of multiple videos
- Provide visual workflow tracking

---

## Implementation Guidelines for Lovable

### Video Processing App Features to Build

1. **ID Scanner Component**
   - Scan Supabase `extracted_entities` table
   - Calculate next available IDs
   - Display in UI before processing

2. **Gap Analysis Component**
   - Compare extracted entities vs existing tools
   - Visual diff showing NEW/EXISTING/UPDATE
   - Approve/reject interface

3. **Integration Component**
   - Batch update Supabase tables
   - Progress bar for multi-entity updates
   - Automatic backup before updates

4. **Progress Tracker**
   - Real-time phase completion
   - Dashboard showing videos by phase
   - Statistics and charts

5. **Error Handling**
   - Try/catch with rollback
   - User-friendly error messages
   - Detailed error logs in Supabase

---

**Created:** 2025-11-28
**Source:** Python automation scripts (process_video.py, video_gap_analyzer.py, video_json_updater.py)
**Purpose:** Extract business logic for React/TypeScript implementation
