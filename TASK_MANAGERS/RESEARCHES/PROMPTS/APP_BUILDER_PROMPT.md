# BUILD AN APPLICATION LIKE THE RESEARCH 2 SYSTEM

**This prompt explains WHAT the system does and WHY, focusing on business logic and workflows, not coding details.**

---

## COPY THIS COMPLETE PROMPT TO AI

```
Build me an application based on the RESEARCH 2 video processing system architecture. Focus on replicating the WORKFLOW LOGIC, DATA RELATIONSHIPS, and BUSINESS PROCESSES, not just the technical implementation.

## WHAT THE RESEARCH 2 SYSTEM DOES

The RESEARCH 2 system is a **7-phase pipeline that discovers, processes, and integrates research content from videos into a structured knowledge base**. It reduced manual processing time from 1.5-2 hours to 5-10 minutes per video (85-95% efficiency gain).

### The Big Picture

**Input**: YouTube videos about AI tools, workflows, and tutorials
**Output**: Structured entities (tools, workflows, actions, objects, skills) integrated into searchable libraries
**Processing**: 7 sequential phases with validation gates, progress tracking, and quality assurance

## THE 7-PHASE WORKFLOW (Main Business Logic)

### Phase 0: Search & Discovery Queue

**Purpose**: Assign video discovery tasks to team members

**What Happens**:
1. Manager assigns search task to employee with topic and department
2. Employee searches YouTube/Perplexity for relevant videos
3. Employee records how many videos found
4. System tracks: who searched, what topic, when assigned, when completed

**Data Tracked**:
- Search ID (SEARCH-001, SEARCH-002, etc.)
- Employee name
- Department (Video, AI Development, HR, etc.)
- Topic (e.g., "AI automation tools 2024")
- Search query used
- Status (Assigned → In Progress → Completed)
- Number of videos found
- Assignment and completion dates

**Business Rules**:
- Sequential search IDs auto-generated
- Cannot mark complete without recording videos found
- Tracks which employees are most productive at finding content

---

### Phase 0→1 Transition: Video Queue Management

**Purpose**: Queue discovered videos for processing with priority ranking

**What Happens**:
1. Employee adds video URL to queue
2. System extracts metadata (title, views, likes, duration, channel)
3. System calculates priority score (0-100) based on multiple factors
4. Videos automatically ranked by priority
5. System suggests best transcription method based on video characteristics

**Data Tracked**:
- Queue ID (VQ-001, VQ-002, etc.)
- Video ID (YouTube 11-character ID)
- Title, channel, URL
- View count, like count, comment count
- Publication date, duration
- Priority score (calculated)
- Status (Pending → Selected → Transcribing → Parsed → Completed)
- Who added it, when added
- Research source (which search found it)

**Priority Scoring Logic** (Business Rule):
- **30% weight**: View count (higher views = higher priority)
- **20% weight**: Like count (more likes = higher priority)
- **30% weight**: Recency (newer videos score higher, linear decay over 1 year)
- **20% weight**: Engagement ratio (likes/views - shows quality)
- **Result**: Videos with high views, recent publication, good engagement rank highest

**Transcription Method Selection** (Business Rule):
- IF duration ≤ 40 minutes AND file size ≤ 100MB → Use Google AI Studio (faster, cheaper)
- ELSE → Use TurboScribe (handles longer/larger videos)

**Why This Matters**: Ensures highest-value content gets processed first, optimizes transcription costs

---

### Phase 1: Transcription & Initial Analysis

**Purpose**: Convert video audio to text and extract initial entity lists

**What Happens**:
1. Video transcribed to text with timestamps
2. AI analyzes transcription using specialized prompt (PMT-004)
3. System extracts 6 types of entities mentioned in video:
   - **Workflows**: Multi-step processes shown (e.g., "Create AI agent with n8n and OpenAI")
   - **Tools**: Software/platforms mentioned (e.g., "VS Code", "ChatGPT", "Notion")
   - **Actions**: Verbs/operations (e.g., "create", "analyze", "export", "integrate")
   - **Objects**: Deliverables/outputs (e.g., "video", "document", "dashboard")
   - **Skills**: Capabilities needed (e.g., "prompt engineering", "Python coding")
   - **Professions**: Job roles (e.g., "AI Developer", "Content Creator")

**Data Structure**:
```
Video Transcription File:
├── Video metadata (ID, title, channel, duration)
├── Full transcription with timestamps
├── Taxonomy analysis
│   ├── Workflows found (list with descriptions)
│   ├── Tools matrix (tool name, category, purpose)
│   ├── Action verbs (categorized by type)
│   ├── Objects/deliverables
│   ├── Skills identified
│   └── Professions mentioned
└── Processing status (which phases completed)
```

**Business Rules**:
- Minimum quality: At least 1 workflow and 1 tool must be found
- Each entity gets preliminary categorization
- Timestamps preserved for future reference
- Provenance tracked (which video, when extracted, by whom)

**Why This Matters**: Converts unstructured video content into structured, searchable entities

---

### Phase 2: Entity Extraction & ID Scanning

**Purpose**: Prepare extracted entities for integration by scanning existing libraries

**What Happens**:
1. System scans all existing library directories to find highest IDs currently in use
2. For each entity type, determines next available ID:
   - Workflows: WRF-001, WRF-002, ... (finds current max, suggests next)
   - Tools: TOOL-AI-001, TOOL-DEV-002, ... (by category)
   - Actions: ACTION-001, ACTION-002, ...
   - Objects: OBJ-SMM-001, OBJ-VID-002, ... (by department)
   - Skills: SKL-001, SKL-002, ...
3. Creates entity inventory from transcription
4. Categorizes each entity by department/category

**ID Naming Conventions** (Business Rule):
- **Workflows**: WRF-###  (3 digits, sequential)
- **Tools**: TOOL-CATEGORY-### (category codes: AI, DEV, VID, SMM, CLOUD, DES, etc.)
- **Actions**: ACTION-### (sequential across all action types)
- **Objects**: OBJ-DEPT-### (department codes: SMM, VID, DEV, HRM, MKT, etc.)
- **Skills**: SKL-### (sequential)
- **Professions**: PROF-### (sequential)

**Why This Matters**: Ensures unique IDs, prevents duplicates, maintains consistent numbering across entire system

---

### Phase 3: Gap Analysis

**Purpose**: Compare extracted entities against existing libraries to identify new vs existing

**What Happens**:
1. System loads all existing entities from libraries
2. Compares extracted entities (from video) vs existing entities (in libraries)
3. Categorizes each extracted entity:
   - **NEW**: Entity doesn't exist in libraries → needs to be created
   - **EXISTS**: Entity already in libraries → skip or update
   - **NEEDS_UPDATE**: Entity exists but video shows new information → flag for review

**Gap Analysis Report Includes**:
- Count of new entities per type (e.g., "5 new tools, 2 new workflows")
- List of new entity names
- List of existing entities found (validation that extraction worked)
- Suggested next IDs for new entities
- Recommendations for updates

**Business Rules**:
- Match by name similarity (exact or fuzzy matching)
- Cross-reference: If tool mentioned in workflow, check if tool exists
- Flag potential duplicates (similar names)
- Estimate time savings: 30-45 minutes manual work → 2-3 minutes automated

**Why This Matters**: Prevents duplicate entities, identifies gaps in knowledge base, shows what's truly new

---

### Phase 4: JSON Creation & Integration

**Purpose**: Create structured JSON files for new entities and integrate into libraries

**What Happens**:
1. For each NEW entity from gap analysis:
   - Create JSON file with full metadata
   - Assign sequential ID (from Phase 2 scan)
   - Fill in all required fields
   - Add relationships to other entities
   - Record provenance (source video, date extracted)

2. JSON files created following templates:
   - **Workflow JSON**: Steps, tools required, inputs/outputs, skills needed
   - **Tool JSON**: Name, category, purpose, URL, pricing, related workflows
   - **Action JSON**: Verb, category, common contexts, related tools
   - **Object JSON**: Name, department, creation tools, related workflows
   - **Skill JSON**: Name, difficulty, related tools, professions using it

3. Files moved to appropriate library directories
4. Cross-references updated (bidirectional linking)

**JSON Structure Example** (Conceptual):
```
Tool JSON:
├── Tool ID (TOOL-AI-042)
├── Name ("ChatGPT")
├── Category ("AI Platform")
├── Department ("AI Development")
├── Description (full text)
├── URL (official website)
├── Pricing ("Free tier available, Plus $20/mo")
├── Relationships
│   ├── Used in workflows: [WRF-023, WRF-045, ...]
│   ├── Requires skills: [SKL-015 "Prompt Engineering"]
│   └── Used by professions: [PROF-002 "AI Developer"]
├── Provenance
│   ├── Source: Video_027
│   ├── Extraction date
│   ├── Validated: true/false
│   └── Last updated
└── Metadata (tags, version, etc.)
```

**Business Rules**:
- All new entities get unique IDs (never reuse)
- All relationships must reference existing IDs (validation)
- Provenance always recorded (traceability)
- JSON schema validated before saving
- Backup created before any file modification

**Why This Matters**: Creates permanent, structured records; enables cross-referencing; maintains data lineage

---

### Phase 5: Library Mapping & Cross-Referencing

**Purpose**: Update existing entities with new relationships discovered in video

**What Happens**:
1. For existing entities mentioned in video, update their JSON files:
   - Add new workflow references
   - Add new related tools
   - Update usage examples
   - Record that this video referenced them

2. Create bidirectional links:
   - If Workflow A uses Tool B → Update Tool B to show it's used in Workflow A
   - If Skill C needed for Workflow A → Update Skill C to show it's used in Workflow A

3. Update master indexes/registries:
   - Add new entries to ENTITIES_MASTER_LIST
   - Update tool_mapping.json (tracks all tools across system)
   - Update workflow categories

**Cross-Reference Example**:
```
Video shows: "Create automation with n8n and OpenAI"

This creates/updates:
- Workflow WRF-045: "n8n + OpenAI Automation"
  → References: TOOL-AI-015 (n8n), TOOL-AI-003 (OpenAI)

- Tool TOOL-AI-015 (n8n):
  → Add to "Used in workflows": WRF-045

- Tool TOOL-AI-003 (OpenAI):
  → Add to "Used in workflows": WRF-045
```

**Business Rules**:
- Always update BOTH sides of relationship (bidirectional)
- Validate all referenced IDs exist before creating links
- Detect circular references (workflow A → workflow B → workflow A)
- Track relationship strength (how many times entities appear together)

**Why This Matters**: Creates knowledge graph, enables "show me all workflows using this tool" queries, reveals patterns

---

### Phase 6-7: Completion & Reporting

**Purpose**: Mark video as fully processed and generate analytics

**What Happens**:
1. **Progress Tracking Update**:
   - Mark all phases complete with timestamps
   - Calculate total processing time (Phase 0 start → Phase 5 end)
   - Record employee who processed it
   - Update status to "Complete"

2. **Report Generation**:
   - Integration summary: How many entities created/updated
   - Breakdown by entity type (5 workflows, 12 tools, etc.)
   - Quality metrics (completeness, validation status)
   - Time saved vs manual processing
   - Employee productivity stats

**Weekly Progress Report Includes**:
- Videos completed this week
- Total entities added to libraries
- Completion rate (% of queued videos processed)
- Average processing time per video
- Bottlenecks (which phases take longest)
- Employee leaderboard (most productive)
- Queue health (how many videos waiting)

**Business Rules**:
- Cannot mark complete unless all phases done
- Total days calculated automatically (Phase 0 date → completion date)
- Reports generated automatically weekly
- Archive completed videos (maintain history)

**Why This Matters**: Tracks productivity, identifies bottlenecks, shows ROI of automation system

---

## DATA RELATIONSHIPS (How Everything Connects)

```
SEARCH QUEUE
    ↓ (finds videos)
VIDEO QUEUE (prioritized)
    ↓ (transcribes)
VIDEO TRANSCRIPTION
    ↓ (extracts)
ENTITIES (Workflows, Tools, Actions, Objects, Skills, Professions)
    ↓ (integrates into)
LIBRARIES (permanent storage)
    ↓ (cross-references)
KNOWLEDGE GRAPH (interconnected entities)
    ↓ (enables)
QUERIES & REPORTS (insights)
```

### Entity Relationship Examples

1. **Workflow → Tools**: "Create AI chatbot" workflow uses [ChatGPT, Notion, Zapier]
2. **Workflow → Actions**: Workflow includes actions [create, configure, test, deploy]
3. **Workflow → Objects**: Workflow produces [chatbot, documentation, API]
4. **Workflow → Skills**: Workflow requires [prompt engineering, API integration]
5. **Tool → Professions**: ChatGPT used by [AI Developer, Content Writer, Marketer]
6. **Skill → Tools**: "Python coding" skill uses [VS Code, GitHub, Jupyter]

---

## PROGRESS TRACKING SYSTEM

### Video Progress Through Phases

Each video tracked in VIDEO_PROGRESS_TRACKER with:

| Video | Phase_0 | Phase_1 | Phase_2 | Phase_3 | Phase_4 | Phase_5 | Status | Employee | Days |
|-------|---------|---------|---------|---------|---------|---------|--------|----------|------|
| Video_027 | 2025-11-01 | 2025-11-02 | 2025-11-03 | 2025-11-04 | 2025-11-05 | 2025-11-06 | Complete | Alice | 5 |
| Video_028 | 2025-11-05 | 2025-11-06 | - | - | - | - | In Progress | Bob | 1 |

**Business Rules for Progress**:
- Must complete phases sequentially (cannot skip from Phase 1 to Phase 4)
- Each phase completion records timestamp
- Total days auto-calculated
- Status auto-updates based on last completed phase
- Employee assigned at Phase 0, can be reassigned mid-process

---

## PRIORITY & DECISION LOGIC

### Why Priority Matters

Videos with **high priority** (score 75-100):
- Get transcribed first (limited transcription budget)
- Likely to contain valuable/trending information
- Higher view counts = proven valuable to community
- Recent publication = current information
- Good engagement = quality content

Videos with **low priority** (score 0-25):
- Moved to bottom of queue
- May never get processed if queue grows
- Usually old videos with low views/engagement
- Content might be outdated

### Transcription Method Decision Logic

**Why it matters**: Cost and time optimization

- **Google AI Studio** (preferred for small videos):
  - Pros: Faster, cheaper, better for educational content
  - Cons: 40-minute limit, 100MB file size limit
  - Cost: ~$0.01 per video

- **TurboScribe** (for large videos):
  - Pros: No limits, handles 2+ hour videos
  - Cons: Slower, more expensive
  - Cost: ~$0.10 per video

**Decision rule**: If video fits Google limits → use Google (saves 90% cost)

---

## VALIDATION & QUALITY GATES

### What Gets Validated and Why

1. **Sequential Phase Progression**:
   - **Rule**: Cannot jump from Phase 1 to Phase 4
   - **Why**: Ensures no steps skipped, maintains data quality

2. **Minimum Entity Requirements**:
   - **Rule**: Each video must extract at least 1 workflow and 1 tool
   - **Why**: If nothing extracted, video wasn't about tools/workflows (wrong content)

3. **ID Uniqueness**:
   - **Rule**: No two entities can have same ID
   - **Why**: Prevents data corruption, enables reliable cross-references

4. **Cross-Reference Validity**:
   - **Rule**: All referenced IDs must exist in libraries
   - **Why**: Prevents broken links, maintains referential integrity

5. **Status Progression**:
   - **Rule**: Status must follow defined flow (Pending → In Progress → Complete)
   - **Why**: Clear process tracking, prevents confusion

6. **Backup Before Modification**:
   - **Rule**: Always backup CSV/JSON before changing
   - **Why**: Enables rollback if mistake made, maintains history

---

## KEY BUSINESS METRICS

### What The System Measures

1. **Efficiency Gains**:
   - Manual time: 1.5-2 hours per video
   - Automated time: 5-10 minutes per video
   - Time saved: 85-95% reduction

2. **Processing Volume**:
   - Videos processed: 28+ completed
   - Entities extracted: 200+ across all types
   - Cross-references created: 500+

3. **Queue Health**:
   - Videos pending: X in queue
   - Average wait time: Y days
   - Processing rate: Z videos per week

4. **Quality Metrics**:
   - Validation pass rate: % of entities that pass validation
   - Duplicate detection rate: % of duplicates caught
   - Cross-reference accuracy: % of valid references

5. **Employee Productivity**:
   - Videos per employee per week
   - Average processing time per employee
   - Quality score per employee (validation pass rate)

---

## BACKUP & RECOVERY STRATEGY

### Why Backups Matter

**Problem**: Mistakes happen - wrong data entered, file corrupted, accidental deletion

**Solution**: Automatic timestamped backups

### How It Works:

1. **Before Every Modification**:
   - System creates timestamped copy of file
   - Example: `master_data.csv` → `master_data_20251205_143022.csv`
   - Stored in `_backups/` directory

2. **Automatic Cleanup**:
   - Keeps 50 most recent backups
   - Deletes older backups automatically
   - Prevents disk space issues

3. **Recovery**:
   - If mistake made, copy backup file back
   - All historical states preserved for 50 changes
   - Can see exactly what changed and when

**Business Value**: Zero data loss, easy error recovery, audit trail

---

## REPORTING & INSIGHTS

### What Reports Are Generated

1. **Weekly Progress Report**:
   - Videos completed this week
   - Entities added to libraries
   - Employee productivity rankings
   - Bottleneck identification (which phases slow)

2. **Gap Analysis Report** (per video):
   - New entities found: 5 workflows, 12 tools, 8 actions
   - Existing entities mentioned: 20 tools, 3 workflows
   - Needs update: 2 tools (new features shown)
   - Recommendations: Create X, update Y

3. **Integration Summary** (per video):
   - Files created: 15 JSON files
   - Files updated: 8 JSON files
   - Cross-references added: 25 links
   - Processing time: 8 minutes
   - Manual equivalent: 1.5 hours

4. **Queue Status Report**:
   - Total videos in queue: 45
   - By status: 12 pending, 5 in progress, 28 complete
   - By priority: 8 high, 25 medium, 12 low
   - Estimated completion: 3 weeks at current rate

**Business Value**: Visibility into progress, data-driven decisions, proof of ROI

---

## APPLICATION YOU SHOULD BUILD

Based on the RESEARCH 2 system, build an application that:

1. **Manages a queue** of items (videos, tasks, documents, etc.)
2. **Calculates priority** using multiple weighted factors
3. **Tracks progress** through multiple sequential phases
4. **Validates transitions** (no skipping phases)
5. **Generates unique IDs** automatically (PREFIX-###)
6. **Creates backups** automatically before modifications
7. **Extracts entities** from content (or processes data)
8. **Performs gap analysis** (new vs existing)
9. **Integrates data** into structured storage
10. **Cross-references** entities (builds knowledge graph)
11. **Generates reports** (progress, analytics, insights)
12. **Tracks metrics** (time saved, productivity, quality)

### Customize For Your Domain

Replace these concepts:
- **Videos** → Your items (tasks, documents, leads, orders, etc.)
- **Transcription** → Your processing step
- **Entity extraction** → Your data extraction/analysis
- **Libraries** → Your database/knowledge base
- **7 phases** → Your workflow stages
- **Priority factors** → Your ranking criteria

### Keep These Patterns:
- ✅ Sequential ID generation
- ✅ Multi-phase pipeline with validation
- ✅ Automatic priority scoring
- ✅ Progress tracking through phases
- ✅ Gap analysis (new vs existing)
- ✅ Automatic backups
- ✅ Comprehensive reporting
- ✅ Cross-referencing/relationships
- ✅ Provenance tracking
- ✅ Employee/team assignment

---

## WHAT TO FOCUS ON IN YOUR BUILD

### Most Important Aspects:

1. **Business Logic** (not technical implementation):
   - What decisions are made and why
   - What workflows exist and their purpose
   - What data relationships matter
   - What metrics drive decisions

2. **Data Flow** (how information moves):
   - Input → Processing → Output
   - Phase transitions and validations
   - Entity extraction and integration
   - Cross-reference creation

3. **Automation Value** (what gets automated):
   - Manual task: 1.5 hours → Automated: 10 minutes
   - What manual steps eliminated
   - What quality checks automated
   - What reports auto-generated

4. **Knowledge Organization** (how data is structured):
   - Entity types and relationships
   - Hierarchies and categories
   - Cross-references and links
   - Searchability and queryability

### Less Important (Can Be Implemented Different Ways):

- Specific programming language (Python, JavaScript, etc.)
- Storage method (CSV vs database vs cloud)
- UI type (CLI vs web vs desktop)
- Specific libraries/frameworks

**Focus on WHAT the system does, not HOW it's coded.**

---

END OF PROMPT
```

## HOW TO USE THIS PROMPT

1. **Copy everything above** (the full text in the code block)
2. **Add your specific domain** at the end:

```
Customize for my use case:
- Instead of videos, I'm processing: [YOUR ITEMS]
- Instead of transcription, I'm doing: [YOUR PROCESSING]
- Instead of entity extraction, I need: [YOUR ANALYSIS]
- My phases are: [YOUR WORKFLOW STAGES]
- My priority factors are: [YOUR RANKING CRITERIA]
```

3. **Paste into ChatGPT/Claude**
4. **Ask for the application focused on business logic and workflow design first, technical implementation second**

This focuses on the LOGIC and PURPOSE, not code syntax!
