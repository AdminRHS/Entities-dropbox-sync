# Video Transcription Custom Instructions - Taxonomy Analysis Focus

---

## 🔴 CRITICAL OUTPUT REQUIREMENT 🔴

**MUST OUTPUT COMPLETE STRUCTURED MARKDOWN DOCUMENT**

❌ **DO NOT** output JSON, plain text, or any other format
✅ **REQUIRED FORMAT:** Markdown (.md) with sections below
✅ **FILE EXTENSION:** .md (not .json, .txt)

---

**Purpose**: Transcribe videos with structured extraction of TASK_MANAGERS entities (Milestones, Tasks, Steps) using LIBRARIES vocabulary for taxonomy mapping.

**Version**: 4.1-TASK_MANAGERS - TASK_MANAGERS Entity Extraction Focus (MLS, TSK, STP)
**Date**: 2025-11-19

---

## Core Transcription Requirements

**Output complete structured markdown document** with the following format:

### Technical Requirements
- **Format:** Markdown (.md) only - NOT JSON, NOT plain text
- **Encoding:** UTF-8
- **Special Characters:** If $ or currency symbols cause corruption, write out full words ("five point six million")
- **Quality Check:** If text appears character-by-character (e.g., "h e l l o"), re-process that section

Transcribe the video content with the following structure in markdown format:

### 1. Metadata Section
- **Video Title**: [Extract exact title]
- **Channel/Creator**: [If available]
- **Video URL**: [Full URL if provided]
- **Duration**: [Video length if visible]
- **Publication Date**: [If available]

### 2. Description Section
- **Description**: [Full video description as provided]
- **Key Topics**: [List main topics covered]
- **Links Referenced**:
  - [Link 1 with description]
  - [Link 2 with description]

### 3. Word-for-Word Transcription

Transcribe exactly as spoken, including:
- **Timestamps**: Mark every 30-60 seconds or at topic changes
- **Speaker Labels**: If multiple speakers
- **Verbal Fillers**: Include "um", "uh", "you know" for accuracy
- **On-screen Text**: Capture in [TEXT: content]
- **Visual Descriptions**: Note in [VISUAL: description]

---

## TAXONOMY EXTRACTION REQUIREMENTS (Critical)

### 4. Milestone Templates Identification

**Identify and extract all milestones (clusters of sequential tasks) mentioned in the video:**

Format each milestone as:
```
MILESTONE_ID: MLS-[next_sequential]
MILESTONE_NAME: [Cluster name]
OBJECTIVE: [What this milestone achieves]
TASKS:
  1. TSK-[next]: [Task name] - [Task description]
  2. TSK-[next]: [Task name] - [Task description]
  3. [Continue...]
DURATION: [Time estimate if mentioned]
COMPLEXITY: [Low/Medium/High if mentioned]
DEPARTMENT: [Primary department ISO code: AID, VID, MKT, LGN, DEV, DGN, SLS, SMM, HRM, FIN]
RELATED_ENTITIES:
  - Tasks: TSK-###, TSK-###, TSK-###
  - Skills: SKL-### (from LIBRARIES - required skills)
  - Responsibilities: RSP-### (from LIBRARIES - matched responsibility definitions)
  - Professions: PRF-### (from LIBRARIES - who executes)
```

**Examples:**
```
MILESTONE_ID: MLS-001
MILESTONE_NAME: Create YouTube Thumbnail
OBJECTIVE: Generate high-CTR thumbnail for video
TASKS:
  1. TSK-001: Define thumbnail concept - Establish visual style and composition
  2. TSK-002: Generate image with AI tool - Create thumbnail variants
  3. TSK-003: Refine and finalize - Select best variant and add text overlay
DURATION: 15-30 minutes
COMPLEXITY: Medium
DEPARTMENT: VID
RELATED_ENTITIES:
  - Tasks: TSK-001, TSK-002, TSK-003
  - Skills: SKL-025 (from LIBRARIES - Visual design)
  - Responsibilities: RSP-### (from LIBRARIES - Content creation)
  - Professions: PRF-008 (from LIBRARIES - Content Creator)
```

```
MILESTONE_ID: MLS-002
MILESTONE_NAME: Browser Automation Agent Workflow
OBJECTIVE: Automate web-based research and data collection using AI agent
TASKS:
  1. TSK-004: Initialize browser session - Open browser and navigate to target
  2. TSK-005: Execute search - Fill criteria and retrieve results
  3. TSK-006: Extract data - Parse and collect relevant information
  4. TSK-007: Export to spreadsheet - Migrate data and close session
DURATION: 2-5 minutes (automated)
COMPLEXITY: High
DEPARTMENT: AID
RELATED_ENTITIES:
  - Tasks: TSK-004, TSK-005, TSK-006, TSK-007
  - Skills: SKL-042 (from LIBRARIES - AI Agent Development)
  - Responsibilities: RSP-### (from LIBRARIES - Automation Engineering)
  - Professions: PRF-003 (from LIBRARIES - AI Engineer)
```

```
MILESTONE_ID: MLS-003
MILESTONE_NAME: Multi-Source Lead Enrichment Pipeline
OBJECTIVE: Generate enriched lead lists from multiple data sources with email validation
TASKS:
  1. TSK-008: Scrape company data - Extract company information from search platform
  2. TSK-009: Extract domains - Collect company domains from scraped data
  3. TSK-010: Enrich emails - Add nominative email patterns and validate deliverability
  4. TSK-011: Export verified list - Download enriched contacts with full data
DURATION: 10-15 minutes for 40 records, scalable to thousands
COMPLEXITY: Medium
DEPARTMENT: LGN
RELATED_ENTITIES:
  - Tasks: TSK-008, TSK-009, TSK-010, TSK-011
  - Skills: SKL-001 (from LIBRARIES - Lead Generation), SKL-002 (from LIBRARIES - Data Enrichment)
  - Responsibilities: RSP-### (from LIBRARIES - Lead Research)
  - Professions: PRF-001 (from LIBRARIES - Lead Generator)
```

### 5. Action Verbs & Operations

**Extract ALL action verbs and operations mentioned:**

Create categorized lists:

#### A. CREATION VERBS (Making new things)
- Create
- Generate
- Design
- Build
- Develop
- Draft
- Produce
- Craft
- Compose
- [Add others found]

#### B. MODIFICATION VERBS (Changing existing things)
- Edit
- Refine
- Optimize
- Enhance
- Update
- Revise
- Improve
- Adjust
- Customize
- [Add others found]

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- Analyze
- Review
- Evaluate
- Research
- Assess
- Examine
- Test
- Compare
- Verify
- [Add others found]

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Organize
- Structure
- Categorize
- Schedule
- Plan
- Coordinate
- Prioritize
- Arrange
- [Add others found]

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Present
- Share
- Publish
- Export
- Deliver
- Communicate
- Report
- Demonstrate
- [Add others found]

#### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)
- Takes over
- Controls
- Automates
- Executes
- Opens
- Clicks
- Closes
- Scrolls
- Navigates
- Fills in
- Hovers
- Submits
- Adds
- Imports
- Migrates
- Interacts
- [Add others found]

**Note**: This category captures action verbs specific to AI agents, browser automation tools, RPA systems, and agentic AI that takes control of digital interfaces.

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Scrape
- Parse
- Extract
- Feed
- Import
- Upload
- Download
- Export
- Enrich
- Validate
- Verify
- Deduplicate
- Sanitize
- Trim
- Filter
- Transform
- Convert
- Merge
- Split
- Combine
- Map
- Match
- Lookup
- [Add others found]

**Note**: This category captures verbs related to data acquisition, processing, and transformation - ETL (Extract, Transform, Load) operations, data enrichment, and data quality processes. Distinct from F (browser/agentic) which focuses on UI control; this focuses on data manipulation.

### 6. Task Templates Identification

**Extract individual tasks that are part of milestones or standalone tasks:**

Format each task as:
```
TASK_ID: TSK-[next_sequential]
TASK_NAME: [Task Name]
DESCRIPTION: [What this task accomplishes]
RESPONSIBILITY: RSP-### (from LIBRARIES - matched responsibility definition)
STEPS:
  1. STP-[next]: [Step description] - [ACT-### action]
  2. STP-[next]: [Step description] - [ACT-### action]
  3. [Continue...]
DURATION: [Time estimate if mentioned]
TOOLS_REQUIRED: [TOL-### references from LIBRARIES]
SKILLS_REQUIRED: [SKL-### references from LIBRARIES]
ASSIGNED_TO: [PRF-### profession from LIBRARIES]
PARENT_MILESTONE: [MLS-### if this task belongs to a milestone]
DEPARTMENT: [ISO code]
```

**Example:**
```
TASK_ID: TSK-001
TASK_NAME: Define thumbnail concept
DESCRIPTION: Establish visual style, composition, and text placement for YouTube thumbnail
RESPONSIBILITY: RSP-### (from LIBRARIES - Visual Content Planning)
STEPS:
  1. STP-001: Research competitor thumbnails - ACT-025 (Research)
  2. STP-002: Identify style elements - ACT-030 (Analyze)
  3. STP-003: Draft concept sketch - ACT-015 (Create)
DURATION: 10 minutes
TOOLS_REQUIRED: None
SKILLS_REQUIRED: SKL-025 (from LIBRARIES - Visual design)
ASSIGNED_TO: PRF-008 (from LIBRARIES - Content Creator)
PARENT_MILESTONE: MLS-001 (Create YouTube Thumbnail)
DEPARTMENT: VID
```

### 7. Step Templates Identification

**Extract atomic steps that make up tasks:**

Format each step as:
```
STEP_ID: STP-[next_sequential]
STEP_NAME: [Action verb + object]
ACTION: [ACT-### reference from LIBRARIES - REQUIRED]
OBJECT: [OBJ-### reference from LIBRARIES - if deliverable is produced]
PROBABILITY_SCORE: [0.0-1.0 - confidence that this object will be produced]
TOOL: [TOL-### if tool is used - reference from LIBRARIES]
INPUT: [What you start with]
OUTPUT: [What you produce]
DURATION: [Time estimate if mentioned]
PARENT_TASK: [TSK-### reference]
```

**Examples:**
```
STEP_ID: STP-001
STEP_NAME: Research competitor thumbnails
ACTION: ACT-025 (from LIBRARIES - Research)
OBJECT: OBJ-### (from LIBRARIES - Research Report)
PROBABILITY_SCORE: 0.85
TOOL: None
INPUT: YouTube channel URLs
OUTPUT: List of design patterns and styles
DURATION: 3 minutes
PARENT_TASK: TSK-001

STEP_ID: STP-002
STEP_NAME: Generate product images
ACTION: ACT-020 (from LIBRARIES - Generate)
OBJECT: OBJ-### (from LIBRARIES - Product Image)
PROBABILITY_SCORE: 0.95
TOOL: TOL-044 (from LIBRARIES - Nano Banana)
INPUT: Product concept, style references
OUTPUT: AI-generated product images (PNG)
DURATION: 5 minutes
PARENT_TASK: TSK-002
```

### 8. Task Chains

**Identify sequential task chains (tasks that feed into each other):**

Format:
```
TASK CHAIN: [Name]
TSK-### ([Task name]) → TSK-### ([Task name]) → TSK-### ([Task name]) → [Final output]

Example:
TASK CHAIN: Automated Documentary Creation
TSK-020 (Research topic) → TSK-021 (Generate script) → TSK-022 (Create video) → TSK-023 (Add voiceover) → Final Documentary
```

### 9. Action-Object-Tool Probability Mapping

**CRITICAL: This section documents the extraction sequence for identifying TASK_MANAGERS entities using LIBRARIES vocabulary.**

#### Extraction Sequence (Follow This Order)

**Phase 1: Tag Action Words**
- Identify all action verbs in the video transcript
- Match each action to ACT-### from LIBRARIES
- Mark actions that appear repeatedly (high frequency = high probability of task identification)

**Phase 2: Mark Object Probability**
- For each tagged action, identify what object/deliverable it produces
- Assign probability score (0.0-1.0) for each potential object
- Match to OBJ-### from LIBRARIES if confidence ≥ 0.7
- Example: "Generate thumbnail" → ACT-020 (Generate) → OBJ-### (Thumbnail) [Probability: 0.95]

**Phase 3: Search for Tools**
- Identify which tools are mentioned for each action-object pair
- Match to TOL-### from LIBRARIES
- Note tool integration patterns (which tools work together)

**Phase 4: Link to Responsibilities**
- Once action-object-tool triplets are identified, search LIBRARIES for matching responsibilities
- Match to RSP-### based on action pattern
- Example: "Generate thumbnail using Nano Banana" → RSP-### (Visual Content Creation)

**Phase 5: Identify Required Skills**
- Based on the action-object-tool-responsibility cluster, identify required skills
- Match to SKL-### from LIBRARIES
- Example: Visual design, Prompt engineering, etc.

**Phase 6: Identify Steps and Group into Tasks**
- Cluster action-object pairs that share the same responsibility into steps (STP-###)
- Group related steps into tasks (TSK-###)
- Each task should map to one RSP-### from LIBRARIES

**Phase 7: Cluster Tasks into Milestones**
- Identify sequential task chains
- Group tasks that work toward the same objective into milestones (MLS-###)
- Milestones represent complete workflows or project phases

#### Probability Scoring Guidelines

**Object Probability Scores:**
- **0.9-1.0**: Explicitly mentioned deliverable (e.g., "create a thumbnail")
- **0.7-0.89**: Strongly implied deliverable (e.g., "design the visual" → implies design file)
- **0.5-0.69**: Moderately implied (e.g., "improve the layout" → might produce new layout)
- **< 0.5**: Weakly implied (don't assign OBJ-### unless mentioned later)

**Task Identification Confidence:**
- **High**: Action + Object + Tool all mentioned explicitly
- **Medium**: Action + Object mentioned, tool implied
- **Low**: Only action mentioned, object/tool unclear

#### Example Mapping Flow

```
VIDEO STATEMENT: "I use Nano Banana to generate product thumbnails for my videos"

EXTRACTION FLOW:
1. TAG ACTION: "generate" → ACT-020 (Generate)
2. MARK OBJECT: "product thumbnails" → OBJ-### (Product Thumbnail) [Probability: 0.95]
3. SEARCH TOOL: "Nano Banana" → TOL-044 (Nano Banana)
4. LINK RESPONSIBILITY: Generate + Product Thumbnail + Nano Banana → RSP-### (Visual Content Creation)
5. IDENTIFY SKILLS: → SKL-025 (AI Image Generation), SKL-### (Prompt Engineering)
6. IDENTIFY STEP: STP-### "Generate product thumbnail using AI tool"
7. GROUP TO TASK: TSK-### "Create video thumbnail" (if other related steps exist)
8. CLUSTER TO MILESTONE: MLS-### "YouTube Video Production" (if part of larger workflow)
```

### 10. Responsibilities Vocabulary

**Extract all role-related terms and responsibilities:**

#### Professional Roles Mentioned:
- Content Creator
- Video Editor
- Graphic Designer
- [List all mentioned]

#### Responsibilities/Activities:
- "Creating thumbnails"
- "Editing videos"
- "Optimizing for CTR"
- "Managing social media content"
- [Extract all responsibility phrases]

#### Skills Mentioned:
- "Prompt engineering"
- "Video editing"
- "Style optimization"
- [Extract all skill references]

### 8. Tools & Technologies Matrix

**Create a comprehensive tools matrix with ID assignment:**

| Tool_ID | Tool Name | Category | Purpose | Department | Source_Video | Related_Tools |
|---------|-----------|----------|---------|------------|--------------|---------------|
| TOL-030 | GLIF | Workflow Automation | Orchestrate AI tools | AID;VID | Video_XXX | TOL-035, TOL-040, TOL-045 |
| TOL-044 | Nano Banana | Image Generation | Create thumbnails | VID;DGN | Video_XXX | TOL-062 |
| [Continue...] | | | | | | |

**Column Definitions**:
- **Tool_ID**: Assigned TOL-### identifier (sequential)
- **Tool Name**: Tool name as mentioned in video
- **Category**: Tool category (AI Video Generation, Image Generation, Automation, etc.)
- **Purpose**: What the tool does (brief description)
- **Department**: Department ISO codes (semicolon-separated for multi-department: AID, VID, MKT, LGN, DEV, DGN, SLS, SMM, HRM, FIN)
- **Source_Video**: Video reference (e.g., Video_011)
- **Related_Tools**: Other tool IDs commonly used with this tool

### 11. Objects & Deliverables (Reference Only - from LIBRARIES)

**IMPORTANT: Objects are NOT extracted as new entities. Reference existing OBJ-### from LIBRARIES only.**

**List all tangible outputs/deliverables mentioned and map to existing LIBRARIES objects:**

- Thumbnails → OBJ-### (from LIBRARIES)
- Videos (specify type: TikTok, documentary, etc.) → OBJ-### (from LIBRARIES)
- Scripts → OBJ-### (from LIBRARIES)
- Voiceovers → OBJ-### (from LIBRARIES)
- Images → OBJ-### (from LIBRARIES)
- Reports → OBJ-### (from LIBRARIES)
- Presentations → OBJ-### (from LIBRARIES)
- [Add all others] → Map to LIBRARIES OBJ-###

**Note**: This section helps identify which LIBRARIES objects are being produced by the TASK_MANAGERS entities (milestones, tasks, steps).

---

## TAXONOMY INTEGRATION OUTPUTS

### 12. Entity ID Assignment & Master List Generation

**Assign standardized taxonomy IDs to all extracted entities and generate CSV master list output.**

#### ID Assignment Rules

**CRITICAL: Only extract TASK_MANAGERS entities (MLS, TSK, STP). Reference LIBRARIES entities (ACT, OBJ, TOL, SKL, PRF, RSP) but do NOT create new ones.**

For each extracted TASK_MANAGERS entity, assign IDs using the format `{XXX}-{###}`:

- **Milestones**: MLS-[next_sequential] (e.g., MLS-001, MLS-002, MLS-003)
- **Tasks**: TSK-[next_sequential] (e.g., TSK-001, TSK-002, TSK-003)
- **Steps**: STP-[next_sequential] (e.g., STP-001, STP-002, STP-003)

**Notes**:
- Use simple sequential numbering within each entity type
- Maintain a running count throughout the video transcription
- Mark all IDs with **[Pending_Review]** status (final ID assignment happens during taxonomy integration)
- Use placeholder "next" if you don't know the current max ID (e.g., MLS-[next])
- **DO NOT assign new IDs to LIBRARIES entities** - only reference existing ACT-###, OBJ-###, TOL-###, SKL-###, PRF-###, RSP-### from LIBRARIES

#### CSV Master List Output

Generate a CSV-formatted table with **ONLY TASK_MANAGERS entities (MLS, TSK, STP)**:

**Required Columns**:
```
New_ID | Entity_Type | Name | Description | Department | Source | Status
```

**Example Output**:

```csv
New_ID,Entity_Type,Name,Description,Department,Source,Status
MLS-001,Milestone,Create YouTube Thumbnail,Generate high-CTR thumbnail for video,VID,Video_011,Pending_Review
MLS-002,Milestone,Browser Automation Agent Workflow,Automate web-based research and data collection using AI agent,AID,Video_011,Pending_Review
TSK-001,Task,Define thumbnail concept,Establish visual style and composition,VID,Video_011,Pending_Review
TSK-002,Task,Generate image with AI tool,Create thumbnail variants using AI,VID,Video_011,Pending_Review
TSK-003,Task,Refine and finalize,Select best variant and add text overlay,VID,Video_011,Pending_Review
STP-001,Step,Research competitor thumbnails,Research competitor thumbnails for design patterns,VID,Video_011,Pending_Review
STP-002,Step,Identify style elements,Analyze and identify key style elements,VID,Video_011,Pending_Review
STP-003,Step,Draft concept sketch,Create initial concept sketch,VID,Video_011,Pending_Review
```

**Formatting Requirements**:
- CSV format with comma delimiters
- Header row included
- All text fields properly escaped (quotes for fields containing commas)
- One entity per row
- **ONLY include MLS, TSK, STP** - NO Tools, Actions, Objects, Skills, Professions, or Responsibilities
- Sorted by Entity_Type, then by New_ID

### 13. Hierarchical Relationship Trees

**Generate ASCII tree diagrams showing TASK_MANAGERS hierarchy: Milestone → Task → Step.**

#### Purpose

Visualize the hierarchical structure of extracted TASK_MANAGERS entities and their relationships with LIBRARIES entities (actions, objects, tools, skills, responsibilities, professions).

#### Format

Use ASCII tree structure with entity IDs:

```
MLS-### (Milestone Name)
├── TSK-### (Task 1)
│   ├── STP-### (Step 1) - ACT-### (Action) → OBJ-### (Object) [TOL-###]
│   ├── STP-### (Step 2) - ACT-### (Action) → OBJ-### (Object) [TOL-###]
│   └── STP-### (Step 3) - ACT-### (Action) → OBJ-### (Object)
├── TSK-### (Task 2)
│   ├── STP-### (Step 4) - ACT-### (Action) → OBJ-### (Object) [TOL-###]
│   └── STP-### (Step 5) - ACT-### (Action) → OBJ-### (Object)
└── LIBRARIES References:
    ├── SKL-### (Skill - from LIBRARIES)
    ├── RSP-### (Responsibility - from LIBRARIES)
    └── PRF-### (Profession - from LIBRARIES)
```

#### Example

**YouTube Thumbnail Creation Milestone Tree**:

```
MLS-001 (Create YouTube Thumbnail)
├── TSK-001 (Define thumbnail concept)
│   ├── STP-001 (Research competitor thumbnails) - ACT-025 (Research) → OBJ-### (Research Report)
│   ├── STP-002 (Identify style elements) - ACT-030 (Analyze) → OBJ-### (Style Guide)
│   └── STP-003 (Draft concept sketch) - ACT-015 (Create) → OBJ-### (Concept Sketch)
├── TSK-002 (Generate image with AI tool)
│   ├── STP-004 (Generate product images) - ACT-020 (Generate) → OBJ-### (Product Image) [TOL-044 - Nano Banana]
│   └── STP-005 (Select best variant) - ACT-035 (Select) → OBJ-### (Selected Image)
├── TSK-003 (Refine and finalize)
│   ├── STP-006 (Add text overlay) - ACT-018 (Edit) → OBJ-### (Final Thumbnail) [TOL-062 - Photoshop]
│   └── STP-007 (Export for upload) - ACT-050 (Export) → OBJ-### (Thumbnail PNG)
└── LIBRARIES References:
    ├── SKL-025 (Visual Design - from LIBRARIES)
    ├── RSP-### (Visual Content Creation - from LIBRARIES)
    └── PRF-008 (Content Creator - from LIBRARIES)
```

**Browser Automation Workflow Milestone Tree**:

```
MLS-002 (Browser Automation Agent Workflow)
├── TSK-004 (Initialize browser session)
│   └── STP-008 (Open browser and navigate) - ACT-105 (Initialize) [TOL-026 - Browser Control API]
├── TSK-005 (Execute search)
│   ├── STP-009 (Fill search criteria) - ACT-108 (Fill) [TOL-025 - Perplexity Comet]
│   └── STP-010 (Retrieve results) - ACT-110 (Retrieve) → OBJ-### (Search Results)
├── TSK-006 (Extract data)
│   └── STP-011 (Parse and collect data) - ACT-112 (Parse) → OBJ-### (Extracted Data)
├── TSK-007 (Export to spreadsheet)
│   └── STP-012 (Migrate data and close) - ACT-115 (Export) → OBJ-### (Spreadsheet)
└── LIBRARIES References:
    ├── SKL-042 (AI Agent Development - from LIBRARIES)
    ├── RSP-### (Automation Engineering - from LIBRARIES)
    └── PRF-003 (AI Engineer - from LIBRARIES)
```

#### Relationship Types to Map

1. **Milestone → Tasks** (tasks that comprise the milestone)
2. **Task → Steps** (atomic steps that comprise each task)
3. **Step → Actions** (ACT-### from LIBRARIES - what action is performed)
4. **Step → Objects** (OBJ-### from LIBRARIES - what deliverable is produced)
5. **Step → Tools** (TOL-### from LIBRARIES - what tool is used, if any)
6. **Milestone → Skills** (SKL-### from LIBRARIES - skills needed for milestone)
7. **Milestone → Responsibilities** (RSP-### from LIBRARIES - responsibility mapping)
8. **Milestone → Professions** (PRF-### from LIBRARIES - who executes)

#### Guidelines

- Create one tree per major milestone identified in the video
- Use TASK_MANAGERS entity IDs (MLS, TSK, STP) - these are the entities being extracted
- Reference LIBRARIES entity IDs (ACT, OBJ, TOL, SKL, RSP, PRF) - these are existing entities being referenced
- Show hierarchical relationships with proper indentation
- Include entity names in parentheses after IDs for readability
- Use ASCII tree characters: `├──`, `└──`, `│`
- Format: `STP-### (Step Name) - ACT-### (Action) → OBJ-### (Object) [TOL-###]`

### 14. Department Distribution Analysis

**Provide quantitative summary of TASK_MANAGERS entities extracted (MLS, TSK, STP only).**

#### Purpose

Show the distribution of extracted TASK_MANAGERS entities across departments to understand which departments benefit most from the video's content.

#### Format

Generate a table showing TASK_MANAGERS entity counts by department:

| Department | ISO | MLS | TSK | STP | Total |
|-----------|-----|-----|-----|-----|-------|
| VID       | VID | X   | X   | X   | XX    |
| AID       | AID | X   | X   | X   | XX    |
| MKT       | MKT | X   | X   | X   | XX    |
| LGN       | LGN | X   | X   | X   | XX    |
| DEV       | DEV | X   | X   | X   | XX    |
| DGN       | DGN | X   | X   | X   | XX    |
| **TOTAL** |     | **XX** | **XX** | **XX** | **XXX** |

**Column Definitions**:
- **Department**: Department full name
- **ISO**: 3-letter department code
- **MLS**: Milestones count (TASK_MANAGERS entities extracted)
- **TSK**: Tasks count (TASK_MANAGERS entities extracted)
- **STP**: Steps count (TASK_MANAGERS entities extracted)
- **Total**: Sum of all TASK_MANAGERS entities for that department

#### Example (Video_011 - YouTube Thumbnail Creation)

| Department | ISO | MLS | TSK | STP | Total |
|-----------|-----|-----|-----|-----|-------|
| Video Production | VID | 1   | 3   | 7   | 11    |
| AI & Automations | AID | 1   | 4   | 4   | 9     |
| Marketing | MKT | 0   | 0   | 0   | 0     |
| Design | DGN | 0   | 0   | 0   | 0     |
| **TOTAL** |     | **2** | **7** | **11** | **20** |

#### Notes

- **ONLY count TASK_MANAGERS entities (MLS, TSK, STP)** - do NOT count LIBRARIES entities
- Count each entity only once in its **primary department**
- If an entity maps to multiple departments (e.g., VID;MKT), assign to the most relevant primary department
- Multi-department mapping is captured in the CSV master list, not in this distribution table
- Use this table to identify which departments have the most task/milestone/step activity in the video content

### 16. Video Source Metadata & Provenance

**Comprehensive source tracking for taxonomy integration and attribution.**

#### Purpose

Provide complete metadata about the source video to ensure full traceability of extracted entities back to their origin. This is critical for validation, updates, and maintaining data provenance in the LIBRARIES taxonomy system.

#### Required Metadata

**Video Identification**:
```
VIDEO_ID: Video_XXX
VIDEO_TITLE: [Full video title as published]
CHANNEL/CREATOR: [YouTube channel or creator name]
VIDEO_URL: [Full URL if available]
PUBLICATION_DATE: [YYYY-MM-DD or as available]
EXTRACTION_DATE: [YYYY-MM-DD - date of this transcription]
EXTRACTOR_VERSION: v4.0
```

**Extraction Summary**:
```
TOTAL_ENTITIES_EXTRACTED: XX

Entity Breakdown:
- Tools (TOL): X entities (TOL-042 to TOL-048)
- Workflows (WRF): X entities (WRF-001 to WRF-002)
- Actions (ACT): X entities (ACT-201 to ACT-208)
- Objects (OBJ): X entities (OBJ-102 to OBJ-110)
- Skills (SKL): X entities (SKL-015 to SKL-018)
- Professions (PRF): X entities (PRF-005 to PRF-006)
```

**Primary Departments**:
```
PRIMARY_DEPARTMENT: VID (Video Production)
SECONDARY_DEPARTMENTS: AID (AI & Automations), MKT (Marketing)
```

**Content Focus**:
```
MAIN_TOPICS:
- AI video generation
- Multi-scene commercial creation
- Frame chaining techniques

KEY_WORKFLOWS:
- Product commercial creation
- Frame-based animation

NOTABLE_TOOLS:
- Google Veo 3.1 (AI video generation)
- OpenArt (frame generation)
- Nano Banana (product images)
```

**Integration Status**:
```
TAXONOMY_STATUS: Pending_Review
READY_FOR_IMPORT: Yes/No
VALIDATION_REQUIRED: Yes (all new entities require review)
NOTES: [Any special considerations for taxonomy integration]
```

#### Example (Video_011)

```
VIDEO_ID: Video_011
VIDEO_TITLE: "Create Unlimited Length Product Commercials with Google Veo 3.1 Frame Chaining"
CHANNEL/CREATOR: AI Video Tools Channel
VIDEO_URL: https://youtube.com/watch?v=example123
PUBLICATION_DATE: 2025-11-10
EXTRACTION_DATE: 2025-11-18
EXTRACTOR_VERSION: v4.0

TOTAL_ENTITIES_EXTRACTED: 21

Entity Breakdown:
- Tools (TOL): 7 entities (TOL-042 to TOL-048)
- Workflows (WRF): 2 entities (WRF-001 to WRF-002)
- Actions (ACT): 4 entities (ACT-201 to ACT-204)
- Objects (OBJ): 5 entities (OBJ-102 to OBJ-106)
- Skills (SKL): 1 entity (SKL-015)
- Professions (PRF): 2 entities (PRF-005 to PRF-006)

PRIMARY_DEPARTMENT: VID (Video Production)
SECONDARY_DEPARTMENTS: AID (AI & Automations), MKT (Marketing), DGN (Design)

MAIN_TOPICS:
- AI video generation with camera movement controls
- Multi-scene product commercial creation
- Frame chaining for unlimited video length
- Start/end frame control techniques

KEY_WORKFLOWS:
- Multi-Scene Product Commercial Creation (WRF-001)
- Frame-based Animation Workflow (WRF-002)

NOTABLE_TOOLS:
- Google Veo 3.1 (AI video generation) - TOL-042
- OpenArt (frame generation) - TOL-043
- Nano Banana (product images) - TOL-044

TAXONOMY_STATUS: Pending_Review
READY_FOR_IMPORT: Yes
VALIDATION_REQUIRED: Yes (all new tool integrations require validation)
NOTES: Focus on video production + marketing integration patterns. Multiple tools work together in complex workflow.
```

---

## FORMATTING STANDARDS

### General Markdown Rules:
- Use `#` headers for major sections
- Use `##` for subsections
- **Bold** important terms
- `Code formatting` for tool names and technical terms
- Bullet points for lists
- Tables for structured data
- Timestamps in [MM:SS] format

### Taxonomy-Specific Formatting:
- ACTION VERBS: Always in CAPS when categorizing
- Tool names: Always capitalized consistently
- Workflows: Always use structured format above
- Task chains: Use → arrows between steps

---

## EXAMPLE OUTPUT STRUCTURE

```markdown
# Video Title
[Full title]

## Metadata
[Standard metadata...]

## Full Transcription
[Word-for-word with timestamps...]

---
# TAXONOMY ANALYSIS

## Workflows Identified

### WORKFLOW 1: Create YouTube Thumbnail
**OBJECTIVE**: Generate high-CTR thumbnail
**STEPS**:
  1. Define concept
  2. Generate with Nano Banana
  3. Add text overlay
**DURATION**: 15-30 min
**TOOLS**: Nano Banana, Photoshop
**INPUT**: Video concept
**OUTPUT**: PNG thumbnail

[Continue for all workflows...]

## Action Verbs Extracted

### Creation Verbs
- Create (mentioned 15 times)
- Generate (mentioned 23 times)
- Design (mentioned 8 times)
[Continue...]

### Modification Verbs
[List...]

## Task Chains

1. Research → Script → Video → Voiceover → Publish
2. Concept → Generate → Refine → Select → Export
[Continue...]

## Responsibilities Vocabulary

**Roles**: Content Creator, Designer, Video Editor
**Activities**:
- "creating engaging thumbnails" [02:34]
- "optimizing for social media" [05:12]
- "automating content workflows" [08:45]

**Skills**:
- Prompt engineering
- Video editing
- Style optimization

## Tools & Technologies Matrix

| Tool | Category | Purpose | Evidence |
|------|----------|---------|----------|
| GLIF | Automation | Orchestrate AI workflows | [01:20-15:30] |
| Nano Banana | Image Gen | Thumbnails | [03:15-05:40] |

## Objects & Deliverables

- YouTube thumbnails (PNG, 16:9)
- 32-second miniature documentaries (MP4)
- Social media videos (TikTok, Instagram Reels)
[Continue...]

## Integration Patterns

**Pattern 1**: Perplexity + AI + VAYU + Seedream + Eleven Labs
- Purpose: Automated documentary creation
- Flow: Research → Script → Video → Voice → Assembly

[Continue...]

## Business Concepts

- **ACP Funnel**: Audience → Community → Product [12:45]
- **10x Productivity**: Using AI agents [00:34]
- **CTR Optimization**: Thumbnail design techniques [03:20]

## Optimization Techniques

1. **Thumbnail CTR**: High contrast, bold text, Mr. Beast style [03:20]
2. **Video Length**: 32 seconds optimal for engagement [06:15]
3. **Workflow Speed**: Use GLIF agents to automate [01:45]

---

# TAXONOMY INTEGRATION OUTPUTS

## 13. Entity ID Assignment & Master List

**CSV Master List**:

```csv
New_ID,Entity_Type,Name,Description,Department,Source,Status
TOL-042,Tool,Google Veo 3.1,AI video generation with camera controls,VID;AID,Video_011,Pending_Review
WRF-001,Workflow,Multi-Scene Product Commercial Creation,Create unlimited commercials via frame chaining,VID;MKT,Video_011,Pending_Review
OBJ-102,Object,Product Commercial Video,Multi-scene commercial output,VID;MKT,Video_011,Pending_Review
ACT-201,Action,Animate,Convert images to video with camera movement,VID,Video_011,Pending_Review
SKL-015,Skill,Frame-based video generation,Control video via start/end frames,VID,Video_011,Pending_Review
PRF-005,Profession,Video Producer,Creates commercial videos with AI tools,VID;MKT,Video_011,Pending_Review
```

## 14. Hierarchical Relationship Trees

```
WRF-001 (Multi-Scene Product Commercial Creation)
├── TOL-042 (Google Veo 3.1)
├── TOL-043 (OpenArt)
├── TOL-044 (Nano Banana)
├── OBJ-102 (Product Commercial Video)
│   ├── OBJ-103 (Start Frame)
│   └── OBJ-104 (End Frame)
├── ACT-201 (Animate)
├── ACT-202 (Control Frames)
├── ACT-203 (Chain Scenes)
├── SKL-015 (Frame-based video generation)
└── PRF-005 (Video Producer)
```

## 15. Department Distribution Analysis

| Department | ISO | TOL | WRF | ACT | OBJ | SKL | PRF | Total |
|-----------|-----|-----|-----|-----|-----|-----|-----|-------|
| Video Production | VID | 3   | 1   | 3   | 3   | 1   | 1   | 12    |
| AI & Automations | AID | 2   | 0   | 1   | 0   | 0   | 0   | 3     |
| **TOTAL** |     | **5** | **1** | **4** | **3** | **1** | **1** | **15** |

## 16. Video Source Metadata & Provenance

```
VIDEO_ID: Video_011
VIDEO_TITLE: "Create Unlimited Length Product Commercials with Google Veo 3.1"
EXTRACTION_DATE: 2025-11-18
EXTRACTOR_VERSION: v4.0

TOTAL_ENTITIES_EXTRACTED: 15

Entity Breakdown:
- Tools (TOL): 5 entities (TOL-042 to TOL-046)
- Workflows (WRF): 1 entity (WRF-001)
- Actions (ACT): 4 entities (ACT-201 to ACT-204)
- Objects (OBJ): 3 entities (OBJ-102 to OBJ-104)
- Skills (SKL): 1 entity (SKL-015)
- Professions (PRF): 1 entity (PRF-005)

PRIMARY_DEPARTMENT: VID (Video Production)
SECONDARY_DEPARTMENTS: AID (AI & Automations), MKT (Marketing)

TAXONOMY_STATUS: Pending_Review
READY_FOR_IMPORT: Yes
```

---

## Key Takeaways for Taxonomy

**New Tools to Add**: [List]
**New Workflows**: [List]
**New Actions**: [List]
**New Responsibilities**: [List]
**Integration Opportunities**: [List]
```

---

## CRITICAL INSTRUCTIONS

1. **Never miss action verbs** - They map directly to taxonomy actions
2. **Capture exact workflow steps** - Essential for process documentation
3. **Note all tool combinations** - Shows integration patterns
4. **Extract responsibility phrases** - Maps to profession taxonomy
5. **Document time estimates** - Helps with workflow planning
6. **Preserve business context** - Shows value and ROI

## VALIDATION CHECKLIST

### FORMAT VALIDATION (CRITICAL - Check First!)
- [ ] **Output is markdown (.md)** - NOT JSON, NOT plain text
- [ ] **Document starts with # heading** - Proper markdown structure
- [ ] **File would save as .md extension** - Confirm format
- [ ] **No JSON curly braces `{}` at document start** - Must be markdown

### SECTION COMPLETENESS
- [ ] **All 3 main sections present:**
  - [ ] 1. Metadata Section
  - [ ] 2. Description Section
  - [ ] 3. Word-for-Word Transcription
- [ ] **TAXONOMY ANALYSIS section included** - This is NOT optional
- [ ] **All required taxonomy subsections present:**
  - [ ] Workflows Identified
  - [ ] Action Verbs & Operations (A-G categories)
  - [ ] Task Chains
  - [ ] Responsibilities Vocabulary
  - [ ] Tools & Technologies Matrix
  - [ ] Objects & Deliverables
  - [ ] Integration Patterns (if applicable)
  - [ ] Business Concepts & Strategy (if applicable)

### CONTENT QUALITY
- [ ] All workflows have structured format (OBJECTIVE, STEPS, DURATION, etc.)
- [ ] Action verbs categorized into 7 categories (A-G)
- [ ] Tools matrix in TABLE format (not JSON, not bulleted list)
- [ ] Task chains show clear flow with arrows (→)
- [ ] Responsibilities vocabulary extracted
- [ ] Integration patterns documented
- [ ] Timestamps provided for key concepts
- [ ] Business value captured
- [ ] No character-by-character text corruption

### TAXONOMY INTEGRATION VALIDATION (UPDATED - v4.1-TASK_MANAGERS)
- [ ] **TASK_MANAGERS entities have valid IDs assigned (MLS, TSK, STP only)**
  - [ ] Milestones use MLS-### format (e.g., MLS-001, MLS-002)
  - [ ] Tasks use TSK-### format (e.g., TSK-001, TSK-002)
  - [ ] Steps use STP-### format (e.g., STP-001, STP-002)
  - [ ] **NO new LIBRARIES entity IDs created** - only reference existing ACT-###, OBJ-###, TOL-###, SKL-###, PRF-###, RSP-###
- [ ] **NO fake entities present**
  - [ ] NO INTEGRATION_ID (Integration is not an entity)
  - [ ] NO PURPOSE field (Purpose is not an entity)
  - [ ] NO FLOW field (Flow is not an entity)
  - [ ] NO ENTITY_CHAIN field (Entity_Chain is not an entity)
  - [ ] NO WRF-### IDs (Workflows replaced by Milestones MLS-###)
- [ ] **Department codes use 3-letter ISO format**
  - [ ] No full department names used (use AID, not "AI & Automations")
  - [ ] Multi-department entities use semicolon separation (e.g., VID;AID;MKT)
  - [ ] All department codes match official registry (AID, HRM, DEV, LGN, DGN, VID, SLS, SMM, FIN, MKT)
- [ ] **CSV master list generated** (Section 12) with ONLY TASK_MANAGERS entities:
  - [ ] New_ID, Entity_Type, Name, Description, Department, Source, Status
  - [ ] **ONLY MLS, TSK, STP included** - NO TOL, ACT, OBJ, SKL, PRF, RSP
  - [ ] All TASK_MANAGERS entities included in CSV output
  - [ ] Proper CSV formatting (header row, comma delimiters, escaped fields)
- [ ] **Hierarchical relationship tree(s) included** (Section 13)
  - [ ] At least one tree per major milestone (MLS-###)
  - [ ] Tree shows Milestone → Task → Step hierarchy
  - [ ] Steps reference LIBRARIES entities (ACT-###, OBJ-###, TOL-###)
  - [ ] Proper ASCII tree formatting with ├── └── │ characters
- [ ] **Department distribution table included** (Section 14)
  - [ ] Columns: Department, ISO, MLS, TSK, STP, Total
  - [ ] **NO columns for TOL, WRF, ACT, OBJ, SKL, PRF** (LIBRARIES entities)
  - [ ] Entity counts accurate for TASK_MANAGERS entities only
  - [ ] Totals calculated correctly
- [ ] **Source video metadata section complete** (Section 15)
  - [ ] VIDEO_ID assigned (Video_XXX format)
  - [ ] Extraction date recorded
  - [ ] EXTRACTOR_VERSION: v4.1-TASK_MANAGERS
  - [ ] Entity count summary shows ONLY MLS, TSK, STP counts
  - [ ] Primary/secondary departments identified
- [ ] **Entity counts match across all sections**
  - [ ] CSV master list count = Distribution table total
  - [ ] Entity breakdown in metadata matches actual extractions
  - [ ] No missing or duplicate TASK_MANAGERS entities
- [ ] **Simple ID format used (no sub-categorization)**
  - [ ] Use MLS-001, not MLS-PROD-001
  - [ ] Use TSK-001, not TSK-VID-001
  - [ ] Use STP-001, not STP-CREATE-001
- [ ] **Action-Object-Tool Probability Mapping section included** (Section 9)
  - [ ] Extraction sequence documented (7 phases)
  - [ ] Probability scoring guidelines present
  - [ ] Example mapping flow provided

---

## Taxonomy Mapping Guide

### How Extracted Data Maps to Taxonomy:

| Extracted Element | Maps To Taxonomy | File Location |
|-------------------|------------------|---------------|
| **Workflows** | Creation_Processes.json | LIBRARIES/Processes/ |
| **Action Verbs** | Creative_Actions.json | LIBRARIES/Actions/ |
| **Tools** | Individual tool JSON files | LIBRARIES/Tools/AI_Tools/ |
| **Responsibilities** | Profession files | LIBRARIES/Professions/ |
| **Deliverables** | Design_Deliverables.json | LIBRARIES/Objects/ |
| **Skills** | Skills taxonomy | TALENTS/Skills/ |
| **Integration Patterns** | Tool integration_with_other_tools | Tool JSON files |

### Priority for Taxonomy Updates:

1. **High Priority**: New tools, workflows, action verbs
2. **Medium Priority**: Integration patterns, optimization techniques
3. **Low Priority**: Business concepts (for context only)

---

## Usage Notes

### For AI Transcription:
- Use this prompt as system instructions
- Process video audio/captions through this structure
- Output complete structured markdown

### For Manual Transcription:
- Follow structure systematically
- Use provided templates for each section
- Don't skip taxonomy extraction sections

### For Quality Assurance:
- Verify all timestamps are accurate
- Ensure action verbs are properly categorized
- Confirm workflows have all required fields
- Check that tools are correctly identified

---

## Version History

**v4.1-TASK_MANAGERS** (2025-11-19) - **TASK_MANAGERS ENTITY EXTRACTION FOCUS**
- **CRITICAL SHIFT:** Refocused from LIBRARIES entity extraction to TASK_MANAGERS entity extraction (MLS, TSK, STP)
- **REPLACED:** Workflows (WRF-###) → Milestones (MLS-###) - Milestones are clusters of sequential tasks
- **REMOVED:** Section 10 (Integration Patterns) - Eliminated fake entities (INTEGRATION_ID, PURPOSE, FLOW, ENTITY_CHAIN)
- **ADDED:** Section 9: Action-Object-Tool Probability Mapping
  - 7-phase extraction sequence (Tag Actions → Mark Objects → Find Tools → Link Responsibilities → Identify Skills → Group Tasks → Cluster Milestones)
  - Probability scoring guidelines (0.0-1.0 confidence scores for object production)
  - Example mapping flow showing LIBRARIES vocabulary usage to identify TASK_MANAGERS entities
- **UPDATED:** Section 4 (Milestones) - Changed from Projects/Workflows to Milestone Templates (MLS-###)
  - References LIBRARIES entities: Skills (SKL-###), Responsibilities (RSP-###), Professions (PRF-###)
  - Removed TOOLS_USED field - tools now referenced only in steps
- **UPDATED:** Section 6 (Tasks) - Added RESPONSIBILITY field, changed PARENT_PROJECT to PARENT_MILESTONE
  - Each task maps to RSP-### from LIBRARIES
- **UPDATED:** Section 7 (Steps) - Added OBJECT and PROBABILITY_SCORE fields
  - Each step MUST reference ACT-### from LIBRARIES
  - Steps optionally reference OBJ-### with probability score
- **UPDATED:** Section 11 (Objects & Deliverables) - Changed to reference-only (from LIBRARIES)
  - Objects are NOT extracted as new entities, only mapped to existing LIBRARIES OBJ-###
- **UPDATED:** Section 12 (CSV Master List) - Now outputs ONLY TASK_MANAGERS entities (MLS, TSK, STP)
  - Removed TOL, WRF, ACT, OBJ, SKL, PRF from CSV output
  - LIBRARIES entities are referenced but not extracted
- **UPDATED:** Section 13 (Hierarchical Trees) - Changed to Milestone → Task → Step hierarchy
  - Tree format: MLS-### → TSK-### → STP-### with LIBRARIES entity references (ACT, OBJ, TOL, SKL, RSP, PRF)
- **UPDATED:** Section 14 (Distribution Table) - Columns changed to MLS, TSK, STP (removed TOL, WRF, ACT, OBJ, SKL, PRF)
  - Only counts TASK_MANAGERS entities extracted from videos
- **UPDATED:** Validation Checklist - Added checks for NO fake entities, MLS/TSK/STP-only CSV, probability mapping section
- **ENTITY MODEL CLARIFICATION:**
  - **EXTRACT:** MLS-### (Milestones), TSK-### (Tasks), STP-### (Steps)
  - **REFERENCE ONLY:** ACT-### (Actions), OBJ-### (Objects), TOL-### (Tools), SKL-### (Skills), PRF-### (Professions), RSP-### (Responsibilities)
- Based on user feedback: Focus on TASK_MANAGERS extraction from videos using LIBRARIES vocabulary as references

**v4.0** (2025-11-18) - **TAXONOMY ARCHITECTURE ALIGNMENT**
- **CRITICAL:** Full integration with LIBRARIES taxonomy architecture
- **ADDED:** Section 13: Entity ID Assignment & Master List Generation
  - Standardized XXX-### ID format (TOL, WRF, ACT, OBJ, SKL, PRF)
  - CSV master list output with all required columns
  - Simple ID format (TOL-042, not TOOL-AI-042 or OBJ-MEDIA-100)
- **ADDED:** Section 14: Hierarchical Relationship Trees
  - ASCII tree diagrams showing entity relationships
  - Workflow → Tools → Objects → Actions → Skills → Professions mapping
- **ADDED:** Section 15: Department Distribution Analysis
  - Quantitative summary table by department and entity type
- **ADDED:** Section 16: Video Source Metadata & Provenance
  - Complete source tracking for taxonomy integration
  - Entity breakdown and integration status
- **UPDATED:** Section 4 (Workflows) - Added WORKFLOW_ID (WRF-###), DEPARTMENT, RELATED_ENTITIES fields
- **UPDATED:** Section 8 (Tools Matrix) - Added Tool_ID, Department, Source_Video, Related_Tools columns
- **UPDATED:** Section 10 (Integration Patterns) - Added INTEGRATION_ID, ENTITY_CHAIN, entity ID mapping
- **UPDATED:** Validation Checklist - Added Taxonomy Integration Validation section (4th tier)
- **UPDATED:** Example Output Structure - Includes all 4 new taxonomy integration sections
- **STANDARDIZED:** Department codes to ISO 3-letter format (AID, VID, MKT, LGN, DEV, DGN, SLS, SMM, HRM, FIN)
- **STANDARDIZED:** Workflow entity type to WRF (not PROC, WORKFLOW, or other variants)
- Based on LIBRARIES_Taxonomy_Initial_ID_List_Prompt.md architecture alignment requirements

**v3.1** (2025-11-12)
- **CRITICAL:** Strengthened markdown format requirement - moved to top with strong visual emphasis
- **ADDED:** G. DATA OPERATIONS action verb category (scraping, parsing, enrichment, ETL)
- **ADDED:** Format validation checklist section (prevent JSON/non-markdown outputs)
- **ADDED:** Character encoding guidance (prevent corruption)
- **ADDED:** Data workflow example (Multi-Source Lead Enrichment Pipeline)
- **ENHANCED:** Validation checklist with 3-tier structure (Format → Completeness → Quality)
- **ENHANCED:** Technical requirements section (UTF-8, quality checks)
- Based on analysis of Video_003, 004, 005, 006 - addresses format inconsistency and data workflow gaps

**v3.0** (2025-11-12)
- Added F. BROWSER/AGENTIC OPERATIONS action verb category
- Added browser automation workflow example
- Enhanced markdown output format specification
- Support for agentic AI, browser automation, and RPA scenarios
- Based on real-world usage analysis from Video_004.md (Perplexity Comet)

**v2.0** (2025-11-11)
- Added comprehensive taxonomy extraction requirements
- Added workflows, action verbs, task chains sections
- Added responsibilities vocabulary extraction
- Added integration patterns documentation
- Added business concepts and optimization sections
- Enhanced with validation checklist

**v1.0** (Initial)
- Basic word-for-word transcription format
- Metadata and description sections

---

**Maintained By**: Taxonomy Team
**Last Updated**: 2025-11-19
**Status**: Active - Production Ready
**Version**: 4.1-TASK_MANAGERS
