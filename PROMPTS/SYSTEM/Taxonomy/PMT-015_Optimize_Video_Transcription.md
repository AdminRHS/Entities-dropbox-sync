---
prompt_id: PRM-TAX-002
version: 1.0
purpose: Optimize Video Transcription Custom Instructions to align with LIBRARIES Taxonomy Architecture
target_file: Video_Transcription_Custom_Instructions.md
reference_architecture: LIBRARIES_Taxonomy_Initial_ID_List_Prompt.md
dependencies:
  - LIBRARIES_Taxonomy_Initial_ID_List_Prompt.md
  - departments.json
  - Video_Transcription_Custom_Instructions.md v3.1
created_date: 2025-11-18
output_version: Video_Transcription_Custom_Instructions.md v4.0
---

# PROMPT: Optimize Video Transcription Instructions for Taxonomy Architecture Alignment

## Context

Update `Video_Transcription_Custom_Instructions.md` (v3.1) to fully align with the standardized **LIBRARIES taxonomy architecture** defined in `LIBRARIES_Taxonomy_Initial_ID_List_Prompt.md`.

The current video transcription instructions successfully extract workflows, tools, actions, and responsibilities from videos. However, they lack integration with the new ID assignment system (XXX-###), CSV master list output, hierarchical relationship mapping, and standardized department codes required for seamless taxonomy integration.

**Target File**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS\PROMPTS\Transcription\Video_Transcription_Custom_Instructions.md`

**Current Version**: v3.1
**Target Version**: v4.0

---

## Objectives

1. **Integrate standardized ID assignment** (XXX-### format) into transcription workflow
2. **Add CSV master list generation** as required output format
3. **Align department codes** with official ISO registry (fix AID vs AIA inconsistency)
4. **Add hierarchical relationship tree generation** (ASCII format)
5. **Enhance entity metadata capture** to match LIBRARIES schema requirements
6. **Add department distribution summary** for quantitative analysis
7. **Clarify workflow entity type** (use WRF for workflows, not PROC)
8. **Implement simple ID format** (XXX-###, no sub-categorization like OBJ-MEDIA-100)

---

## Key Changes Required

### CHANGE 1: Fix Department Code Inconsistency

**Location**: Throughout document, particularly Section 2 (Metadata), Section 7 (Responsibilities Vocabulary)

**Current State**: References generic department names or inconsistent codes
**Required Change**: Use official 3-letter ISO codes from departments.json

**Official Department ISO Codes**:

| Department Code | Full Name | Description |
|----------------|-----------|-------------|
| **AID** | AI & Automations Department | AI, Automations, Admin (consolidated) |
| **HRM** | Human Resources Management | HR & Talent |
| **DEV** | Development & Engineering | Engineering & Dev |
| **LGN** | Lead Generation | Lead Generation |
| **DGN** | Design & Creative | Design & Creative |
| **VID** | Video Production | Video content & production |
| **SLS** | Sales & Client Relations | Sales & Client Relations |
| **SMM** | Social Media Management | Social media marketing and management |
| **FNC** | Finance & Accounting | Finance & Accounting |

**Action**:
- Replace any references to full department names with ISO codes
- Ensure consistency across all sections
- Use semicolon-separated codes for multi-department entities (e.g., "VID;AID;MKT")

---

### CHANGE 2: Standardize Entity Types with ISO Codes

**Location**: All taxonomy extraction sections (4-12)

**Entity Type ISO Codes** (from LIBRARIES architecture):

| Entity Type | ISO Code | ID Pattern | Description |
|-------------|----------|------------|-------------|
| Tools | **TOL** | TOL-001… | Individual tool definitions |
| Objects | **OBJ** | OBJ-001… | Domain objects/deliverables |
| Actions | **ACT** | ACT-001… | Data operations and actions |
| Workflows | **WRF** | WRF-001… | Process workflows |
| Skills | **SKL** | SKL-001… | Skill definitions |
| Professions | **PRF** | PRF-001… | Profession profiles |
| Cross-Refs | **XRF** | XRF-001… | Cross-reference files |
| Reports & Docs | **RPD** | RPD-001… | Documentation/reports |

**Critical Fix**: Use **WRF** for workflows (NOT PROC, WORKFLOW, or other variants)

**ID Format Rules**:
- Pattern: `{XXX}-{###}`
- XXX = 3-letter consonant-only ISO code
- ### = 3-digit sequential ID (001–999)
- **Simple format only** - no sub-categorization (e.g., avoid OBJ-MEDIA-100, use OBJ-100 instead)
- All codes uppercase
- Exactly 3 letters + hyphen + 3 digits

---

### CHANGE 3: Add Entity ID Assignment Section (NEW Section 13)

**Location**: Insert after Section 12 (Optimization & Best Practices), before FORMATTING STANDARDS

**New Section Title**: `### 13. Entity ID Assignment & Master List Generation`

**Content**:

```markdown
### 13. Entity ID Assignment & Master List Generation

**Assign standardized taxonomy IDs to all extracted entities and generate CSV master list output.**

#### ID Assignment Rules

For each extracted entity, assign IDs using the format `{XXX}-{###}`:

- **Tools**: TOL-[next_sequential] (e.g., TOL-042, TOL-043, TOL-044)
- **Workflows**: WRF-[next_sequential] (e.g., WRF-001, WRF-002)
- **Actions**: ACT-[next_sequential] (e.g., ACT-201, ACT-202)
- **Objects**: OBJ-[next_sequential] (e.g., OBJ-102, OBJ-103)
- **Skills**: SKL-[next_sequential] (e.g., SKL-015, SKL-016)
- **Professions**: PRF-[next_sequential] (e.g., PRF-005, PRF-006)

**Notes**:
- Use simple sequential numbering within each entity type
- Maintain a running count throughout the video transcription
- Mark all IDs with **[Pending_Review]** status (final ID assignment happens during taxonomy integration)
- Use placeholder "next" if you don't know the current max ID (e.g., TOL-[next])

#### CSV Master List Output

Generate a CSV-formatted table with all extracted entities:

**Required Columns**:
```
New_ID | Entity_Type | Name | Description | Department | Source | Status
```

**Example Output**:

```csv
New_ID,Entity_Type,Name,Description,Department,Source,Status
TOL-042,Tool,Google Veo 3.1,AI video generation with camera movement controls,VID;AID,Video_011,Pending_Review
TOL-043,Tool,OpenArt,Frame generation and image composition tool,VID;DGN,Video_011,Pending_Review
TOL-044,Tool,Nano Banana,Product image generation for commercial videos,VID;MKT,Video_011,Pending_Review
WRF-001,Workflow,Multi-Scene Product Commercial Creation,Create unlimited-length commercials by chaining scenes,VID;MKT,Video_011,Pending_Review
OBJ-102,Object,Product Commercial Video,Multi-scene commercial with chained animations,VID;MKT,Video_011,Pending_Review
OBJ-103,Object,Start Frame,Initial frame for video sequence,VID,Video_011,Pending_Review
OBJ-104,Object,End Frame,Final frame for scene transition,VID,Video_011,Pending_Review
ACT-201,Action,Animate,Convert static images to video with camera movements,VID,Video_011,Pending_Review
ACT-202,Action,Control Frames,Set start and end frames for video generation,VID,Video_011,Pending_Review
ACT-203,Action,Chain Scenes,Connect multiple video scenes for extended length,VID,Video_011,Pending_Review
SKL-015,Skill,Frame-based video generation,Ability to control video output using start/end frames,VID,Video_011,Pending_Review
PRF-005,Profession,Video Producer,Creates commercial and marketing videos using AI tools,VID;MKT,Video_011,Pending_Review
```

**Formatting Requirements**:
- CSV format with comma delimiters
- Header row included
- All text fields properly escaped (quotes for fields containing commas)
- One entity per row
- Sorted by Entity_Type, then by New_ID

#### Entity Metadata Capture

For each entity, capture the following metadata:

**Tools**:
- New_ID (TOL-###)
- Name (tool name as mentioned)
- Description (what it does)
- Department (ISO codes: VID, AID, MKT, etc.)
- Source (e.g., Video_011, Video_012)
- Status (always "Pending_Review" for new extractions)

**Workflows**:
- New_ID (WRF-###)
- Name (workflow name)
- Description (objective/purpose)
- Department (primary department codes)
- Source (video reference)
- Status (Pending_Review)

**Actions**:
- New_ID (ACT-###)
- Name (action verb)
- Description (what the action does)
- Department (where it's used)
- Source (video reference)
- Status (Pending_Review)

**Objects**:
- New_ID (OBJ-###)
- Name (object/deliverable name)
- Description (what it is)
- Department (who creates/uses it)
- Source (video reference)
- Status (Pending_Review)

**Skills**:
- New_ID (SKL-###)
- Name (skill phrase)
- Description (skill definition)
- Department (where it's used)
- Source (video reference)
- Status (Pending_Review)

**Professions**:
- New_ID (PRF-###)
- Name (profession title)
- Description (role description)
- Department (home department)
- Source (video reference)
- Status (Pending_Review)
```

---

### CHANGE 4: Add Hierarchical Relationship Trees Section (NEW Section 14)

**Location**: Insert after Section 13 (Entity ID Assignment)

**New Section Title**: `### 14. Hierarchical Relationship Trees`

**Content**:

```markdown
### 14. Hierarchical Relationship Trees

**Generate ASCII tree diagrams showing entity relationships and dependencies.**

#### Purpose

Visualize how tools, workflows, actions, objects, skills, and professions relate to each other within the video's content. This shows the complete stack from workflow down to individual tools and deliverables.

#### Format

Use ASCII tree structure with entity IDs:

```
WRF-### (Workflow Name)
├── TOL-### (Tool 1)
├── TOL-### (Tool 2)
├── TOL-### (Tool 3)
├── OBJ-### (Input Object)
│   ├── OBJ-### (Sub-object 1)
│   └── OBJ-### (Sub-object 2)
├── ACT-### (Action 1)
├── ACT-### (Action 2)
├── ACT-### (Action 3)
├── SKL-### (Required Skill 1)
├── SKL-### (Required Skill 2)
└── PRF-### (Profession who executes)
```

#### Example

**Video Production Workflow Tree**:

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

**Lead Generation Workflow Tree**:

```
WRF-002 (Google SERP Lead Generation)
├── TOL-015 (Apify Google SERP Scraper)
├── TOL-018 (Anymailfinder)
├── OBJ-001 (Lead List)
├── OBJ-003 (Decision-Maker Email)
├── ACT-015 (Scrape)
├── ACT-022 (Enrich)
├── ACT-028 (Validate)
├── SKL-001 (Scraped lead lists via Apify)
├── SKL-002 (Email enrichment via Anymailfinder)
└── PRF-001 (Lead Generator)
```

#### Relationship Types to Map

1. **Workflow → Tools** (which tools are used in this workflow)
2. **Workflow → Objects** (what inputs are required, what outputs are created)
3. **Workflow → Actions** (what actions are performed)
4. **Workflow → Skills** (what skills are needed to execute)
5. **Workflow → Professions** (who typically performs this workflow)
6. **Objects → Sub-objects** (hierarchical deliverables)
7. **Tools → Objects** (what tools create which objects)

#### Guidelines

- Create one tree per major workflow identified in the video
- Use entity IDs (not just names) for all references
- Show hierarchical relationships with proper indentation
- Include entity names in parentheses after IDs for readability
- Use ASCII tree characters: `├──`, `└──`, `│`
- If a workflow doesn't have all entity types, only show what's relevant
```

---

### CHANGE 5: Add Department Distribution Analysis Section (NEW Section 15)

**Location**: Insert after Section 14 (Hierarchical Relationship Trees)

**New Section Title**: `### 15. Department Distribution Analysis`

**Content**:

```markdown
### 15. Department Distribution Analysis

**Provide quantitative summary of entities extracted, organized by department and entity type.**

#### Purpose

Show the distribution of extracted taxonomy elements across departments to understand which departments benefit most from the video's content.

#### Format

Generate a table showing entity counts by department and type:

| Department | ISO | TOL | WRF | ACT | OBJ | SKL | PRF | Total |
|-----------|-----|-----|-----|-----|-----|-----|-----|-------|
| VID       | VID | X   | X   | X   | X   | X   | X   | XX    |
| AID       | AID | X   | X   | X   | X   | X   | X   | XX    |
| MKT       | MKT | X   | X   | X   | X   | X   | X   | XX    |
| LGN       | LGN | X   | X   | X   | X   | X   | X   | XX    |
| DEV       | DEV | X   | X   | X   | X   | X   | X   | XX    |
| DGN       | DGN | X   | X   | X   | X   | X   | X   | XX    |
| **TOTAL** |     | **XX** | **XX** | **XX** | **XX** | **XX** | **XX** | **XXX** |

**Column Definitions**:
- **Department**: Department full name
- **ISO**: 3-letter department code
- **TOL**: Tools count
- **WRF**: Workflows count
- **ACT**: Actions count
- **OBJ**: Objects count
- **SKL**: Skills count
- **PRF**: Professions count
- **Total**: Sum of all entity types for that department

#### Example (Video_011 - Multi-Scene Product Commercials)

| Department | ISO | TOL | WRF | ACT | OBJ | SKL | PRF | Total |
|-----------|-----|-----|-----|-----|-----|-----|-----|-------|
| Video Production | VID | 3   | 1   | 3   | 3   | 1   | 1   | 12    |
| AI & Automations | AID | 2   | 0   | 1   | 0   | 0   | 0   | 3     |
| Marketing | MKT | 1   | 1   | 0   | 1   | 0   | 1   | 4     |
| Design | DGN | 1   | 0   | 0   | 1   | 0   | 0   | 2     |
| **TOTAL** |     | **7** | **2** | **4** | **5** | **1** | **2** | **21** |

#### Notes

- Count each entity only once in its **primary department**
- If an entity maps to multiple departments (e.g., VID;MKT), assign to the most relevant primary department
- Multi-department mapping is captured in the CSV master list, not in this distribution table
- Use this table to identify which departments are most represented in the video content
```

---

### CHANGE 6: Add Video Source Metadata Section (NEW Section 16)

**Location**: Insert after Section 15 (Department Distribution Analysis)

**New Section Title**: `### 16. Video Source Metadata & Provenance`

**Content**:

```markdown
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
```

---

### CHANGE 7: Update Section 4 (Workflows Identification)

**Location**: Section 4 (Workflows Identification)

**Current**: Workflows have narrative format without IDs
**Required Change**: Add WRF-### ID assignment to workflow format

**Updated Workflow Format**:

```markdown
### 4. Workflows Identification

**Identify and extract all workflows/processes mentioned in the video:**

Format each workflow as:
```
WORKFLOW_ID: WRF-[next_sequential]
WORKFLOW: [Workflow Name]
OBJECTIVE: [What the workflow achieves]
STEPS:
  1. [Action verb] + [object/deliverable]
  2. [Action verb] + [object/deliverable]
  3. [Continue...]
DURATION: [Time estimate if mentioned]
COMPLEXITY: [Low/Medium/High if mentioned]
TOOLS_USED: [List all tools with TOL-### IDs if assigned]
INPUT: [What you start with]
OUTPUT: [What you end with]
DEPARTMENT: [Primary department ISO code]
RELATED_ENTITIES:
  - Tools: TOL-###, TOL-###, TOL-###
  - Objects: OBJ-###, OBJ-###
  - Actions: ACT-###, ACT-###
  - Skills: SKL-###
  - Professions: PRF-###
```

**Example**:
```
WORKFLOW_ID: WRF-001
WORKFLOW: Multi-Scene Product Commercial Creation
OBJECTIVE: Create unlimited-length product commercials by chaining video scenes
STEPS:
  1. Generate product images (Nano Banana)
  2. Set start frame for video sequence
  3. Generate first video scene with camera movement (Google Veo 3.1)
  4. Use end frame of Scene 1 as start frame of Scene 2
  5. Generate Scene 2 with continuation (Google Veo 3.1)
  6. Repeat chaining process for additional scenes
  7. Export final multi-scene commercial
DURATION: 20-30 minutes for 3-scene commercial
COMPLEXITY: High
TOOLS_USED: Google Veo 3.1 (TOL-042), OpenArt (TOL-043), Nano Banana (TOL-044)
INPUT: Product images, style references, camera movement descriptions
OUTPUT: Multi-scene product commercial video (MP4, unlimited length)
DEPARTMENT: VID
RELATED_ENTITIES:
  - Tools: TOL-042, TOL-043, TOL-044
  - Objects: OBJ-102, OBJ-103, OBJ-104
  - Actions: ACT-201, ACT-202, ACT-203
  - Skills: SKL-015
  - Professions: PRF-005
```
```

---

### CHANGE 8: Update Section 8 (Tools & Technologies Matrix)

**Location**: Section 8 (Tools & Technologies Matrix)

**Current**: Tools matrix without ID assignment
**Required Change**: Add Tool_ID column and department codes

**Updated Format**:

```markdown
### 8. Tools & Technologies Matrix

**Create a comprehensive tools matrix with ID assignment:**

| Tool_ID | Tool Name | Category | Purpose | Department | Source_Video | Related_Tools |
|---------|-----------|----------|---------|------------|--------------|---------------|
| TOL-042 | Google Veo 3.1 | AI Video Generation | Create videos with camera movement controls | VID;AID | Video_011 | TOL-043, TOL-044 |
| TOL-043 | OpenArt | Image Generation | Generate frames for video sequences | VID;DGN | Video_011 | TOL-042 |
| TOL-044 | Nano Banana | Product Image Generation | Create product images for commercials | VID;MKT | Video_011 | TOL-042 |
| [Continue...] | | | | | | |

**Column Definitions**:
- **Tool_ID**: Assigned TOL-### identifier (sequential)
- **Tool Name**: Tool name as mentioned in video
- **Category**: Tool category (AI Video Generation, Image Generation, Automation, etc.)
- **Purpose**: What the tool does (brief description)
- **Department**: Department ISO codes (semicolon-separated for multi-department)
- **Source_Video**: Video reference (e.g., Video_011)
- **Related_Tools**: Other tool IDs commonly used with this tool
```

---

### CHANGE 9: Update Section 10 (Integration Patterns)

**Location**: Section 10 (Integration Patterns)

**Current**: Integration patterns without entity IDs
**Required Change**: Add entity IDs and structured relationship mapping

**Updated Format**:

```markdown
### 10. Integration Patterns

**Document how tools/processes connect with entity ID references:**

Format:
```
INTEGRATION_ID: INT-[sequential]
INTEGRATION: [Tool A] + [Tool B] + [Tool C]
PURPOSE: [Why they're used together]
ENTITY_CHAIN: [TOL-###] → [WRF-###] → [OBJ-###]
FLOW: [Detailed data flow with IDs]
DEPARTMENT: [Primary department codes]
PROFESSIONS: [Who uses this integration]
```

**Example**:
```
INTEGRATION_ID: INT-VID-001
INTEGRATION: Google Veo 3.1 + OpenArt + Nano Banana
PURPOSE: Create multi-scene product commercials with frame chaining
ENTITY_CHAIN: TOL-044 → TOL-043 → TOL-042 → WRF-001 → OBJ-102
FLOW:
  1. [TOL-044] Generate product images (Nano Banana)
  2. [TOL-043] Create start/end frames (OpenArt)
  3. [ACT-202] Set frame controls
  4. [TOL-042] Animate with camera movements (Google Veo 3.1)
  5. [ACT-203] Chain scenes for unlimited length
  6. [OBJ-102] Output multi-scene commercial video
DEPARTMENT: VID, MKT
PROFESSIONS: Video Producer (PRF-005), Product Marketer (PRF-006)
```

**Integration Patterns to Capture**:
- Tool stacks (multiple tools working together)
- Workflow chains (output of one workflow feeds another)
- Department collaborations (cross-department integrations)
- Skill requirements (skills needed to execute integration)
```

---

### CHANGE 10: Update VALIDATION CHECKLIST

**Location**: Section titled "VALIDATION CHECKLIST"

**Current**: Format and content validation without taxonomy requirements
**Required Change**: Add taxonomy-specific validation rules

**Add New Validation Section**:

```markdown
### TAXONOMY INTEGRATION VALIDATION (NEW)
- [ ] **All entities have valid XXX-### IDs assigned**
  - [ ] Tools use TOL-### format
  - [ ] Workflows use WRF-### format (NOT PROC, WORKFLOW, or other variants)
  - [ ] Actions use ACT-### format
  - [ ] Objects use OBJ-### format
  - [ ] Skills use SKL-### format
  - [ ] Professions use PRF-### format
- [ ] **Department codes use 3-letter ISO format**
  - [ ] No full department names used (use AID, not "AI & Automations")
  - [ ] Multi-department entities use semicolon separation (e.g., VID;AID;MKT)
  - [ ] All department codes match official registry (AID, HRM, DEV, LGN, DGN, VID, SLS, SMM, FNC)
- [ ] **CSV master list generated** with all required columns:
  - [ ] New_ID, Entity_Type, Name, Description, Department, Source, Status
  - [ ] All entities included in CSV output
  - [ ] Proper CSV formatting (header row, comma delimiters, escaped fields)
- [ ] **Hierarchical relationship tree(s) included**
  - [ ] At least one tree per major workflow
  - [ ] Entity IDs used (not just names)
  - [ ] Proper ASCII tree formatting
- [ ] **Department distribution table included**
  - [ ] All departments represented
  - [ ] Entity counts accurate
  - [ ] Totals calculated correctly
- [ ] **Source video metadata section complete**
  - [ ] VIDEO_ID assigned (Video_XXX format)
  - [ ] Extraction date recorded
  - [ ] Entity count summary matches actual extractions
  - [ ] Primary/secondary departments identified
- [ ] **Entity counts match across all sections**
  - [ ] CSV master list count = Distribution table total
  - [ ] Entity breakdown in metadata matches actual extractions
  - [ ] No missing or duplicate entities
- [ ] **Simple ID format used (no sub-categorization)**
  - [ ] Use TOL-042, not TOOL-AI-042
  - [ ] Use OBJ-102, not OBJ-MEDIA-102
  - [ ] Use WRF-001, not PROC-VIDEO-001
```

---

### CHANGE 11: Update EXAMPLE OUTPUT STRUCTURE

**Location**: Section titled "EXAMPLE OUTPUT STRUCTURE"

**Required Change**: Add new sections to example output

**Add to Example**:

```markdown
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

### WORKFLOW 1: Multi-Scene Product Commercial Creation
**WORKFLOW_ID**: WRF-001
**OBJECTIVE**: Create unlimited-length product commercials
**STEPS**:
  1. Generate product images
  2. Set start/end frames
  3. Animate scenes
  4. Chain scenes together
**DURATION**: 20-30 min
**COMPLEXITY**: High
**TOOLS**: Google Veo 3.1 (TOL-042), OpenArt (TOL-043), Nano Banana (TOL-044)
**DEPARTMENT**: VID
**RELATED_ENTITIES**:
  - Tools: TOL-042, TOL-043, TOL-044
  - Objects: OBJ-102, OBJ-103, OBJ-104
  - Actions: ACT-201, ACT-202, ACT-203

[Continue for all workflows...]

## Action Verbs Extracted
[Existing sections A-G...]

## Task Chains
[Existing content...]

## Responsibilities Vocabulary
[Existing content...]

## Tools & Technologies Matrix

| Tool_ID | Tool Name | Category | Purpose | Department | Source_Video | Related_Tools |
|---------|-----------|----------|---------|------------|--------------|---------------|
| TOL-042 | Google Veo 3.1 | AI Video | Video generation | VID;AID | Video_011 | TOL-043, TOL-044 |
[Continue...]

## Objects & Deliverables
[Existing content...]

## Integration Patterns

**INT-VID-001**: Google Veo 3.1 + OpenArt + Nano Banana
- Purpose: Multi-scene commercial creation
- Entity Chain: TOL-044 → TOL-043 → TOL-042 → WRF-001 → OBJ-102
[Continue...]

---
# TAXONOMY INTEGRATION OUTPUTS (NEW)

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
[Existing content...]
```
```

---

## ISO Code Registry Reference

### Entity Type ISO Codes

| ISO Code | Entity Type | Derivation | ID Range |
|----------|-------------|------------|----------|
| **TOL** | Tools | **T**_oo**L**_s | TOL-001 to TOL-999 |
| **OBJ** | Objects | **OB**_**J**_ects | OBJ-001 to OBJ-999 |
| **ACT** | Actions | **AC**_**T**_ions | ACT-001 to ACT-999 |
| **WRF** | Workflows | **W**_o**R**_k**F**_lows | WRF-001 to WRF-999 |
| **SKL** | Skills | **SK**_i**L**_ls | SKL-001 to SKL-999 |
| **PRF** | Professions | **PR**_o**F**_essions | PRF-001 to PRF-999 |
| **XRF** | Cross-References | Cross Re**F**erence (ma**P**ping) | XRF-001 to XRF-999 |
| **RPD** | Reports & Docs | Re**P**orts & **D**ocumentation | RPD-001 to RPD-999 |

### Department ISO Codes

| ISO Code | Department | Full Name |
|----------|-----------|-----------|
| **AID** | AI & Automations | AI & Automations Department |
| **HRM** | Human Resources | Human Resources Management |
| **DEV** | Development | Development & Engineering |
| **LGN** | Lead Generation | Lead Generation |
| **DGN** | Design | Design & Creative |
| **VID** | Video Production | Video Production |
| **SLS** | Sales | Sales & Client Relations |
| **SMM** | Social Media | Social Media Management |
| **FNC** | Finance | Finance & Accounting |

---

## Implementation Guidelines

### Step 1: Review Current File
- Read `Video_Transcription_Custom_Instructions.md` v3.1 in full
- Understand existing structure and content
- Identify sections that will be modified vs. added

### Step 2: Make Department Code Updates
- Search for all department references
- Replace with 3-letter ISO codes
- Ensure consistency across all sections

### Step 3: Add Entity Type Standards
- Update Section 4 (Workflows) with WRF-### format
- Update Section 8 (Tools Matrix) with TOL-### column
- Add entity ID references throughout

### Step 4: Add New Sections
- Insert Section 13: Entity ID Assignment & Master List Generation
- Insert Section 14: Hierarchical Relationship Trees
- Insert Section 15: Department Distribution Analysis
- Insert Section 16: Video Source Metadata & Provenance

### Step 5: Update Existing Sections
- Section 4: Add WORKFLOW_ID field
- Section 8: Add Tool_ID column and department codes
- Section 10: Add INTEGRATION_ID and entity chain mapping
- Validation Checklist: Add taxonomy integration validation

### Step 6: Update Example Output
- Add all new sections to example structure
- Provide complete examples for new outputs
- Ensure consistency with real-world usage

### Step 7: Update Version & Metadata
- Change version from v3.1 to v4.0
- Update date to implementation date
- Add version history entry documenting all changes

---

## Success Criteria

✅ **Structural Alignment**:
- [ ] All entity types use standardized ISO codes (TOL, WRF, ACT, OBJ, SKL, PRF)
- [ ] Department codes align with official registry (AID, not "AI & Automations")
- [ ] Simple ID format enforced (TOL-042, not TOOL-AI-042)
- [ ] WRF used for workflows (not PROC or other variants)

✅ **Output Requirements**:
- [ ] CSV master list format specified with all required columns
- [ ] Hierarchical relationship trees section added with examples
- [ ] Department distribution table format defined
- [ ] Video source metadata section added with complete tracking fields

✅ **Section Updates**:
- [ ] Section 4 (Workflows) includes WORKFLOW_ID field
- [ ] Section 8 (Tools Matrix) includes Tool_ID column and department codes
- [ ] Section 10 (Integration Patterns) includes entity ID mapping
- [ ] Validation checklist includes taxonomy integration validation

✅ **Documentation**:
- [ ] ISO code registry included as reference
- [ ] Implementation guidelines provided
- [ ] Examples updated to show new format
- [ ] Version history updated to v4.0

✅ **Compatibility**:
- [ ] All existing sections preserved (additive changes only)
- [ ] No breaking changes to core transcription functionality
- [ ] Backward compatibility maintained for existing workflows
- [ ] Output can be directly imported into LIBRARIES taxonomy system

---

## Migration Notes

**Version**: v3.1 → v4.0
**Migration Type**: Additive (non-breaking)

**What's Preserved**:
- All existing transcription sections (1-12)
- Markdown format requirement
- Action verb categories (A-G)
- Workflow extraction format (enhanced, not replaced)
- Tools matrix structure (enhanced with ID column)
- Validation checklist (expanded, not replaced)

**What's New**:
- Section 13: Entity ID Assignment & Master List
- Section 14: Hierarchical Relationship Trees
- Section 15: Department Distribution Analysis
- Section 16: Video Source Metadata & Provenance
- Entity ID fields in workflows, tools, integrations
- Department ISO code standardization
- CSV output format specification
- Taxonomy integration validation rules

**Breaking Changes**: None (all changes are additive)

**Backward Compatibility**: Videos transcribed with v3.1 will need supplementary taxonomy integration phase to add IDs, CSV output, hierarchical trees, and department distribution. Future transcriptions using v4.0 will have this integrated from the start.

---

## Testing Recommendations

### Test 1: Video Production Content (Video_011)
- **Content**: Multi-scene product commercial creation with Google Veo 3.1
- **Expected Entities**: Tools (VID;AID), Workflows (VID;MKT), Actions (VID), Objects (VID;MKT)
- **Validation**:
  - WRF-### IDs assigned to workflows
  - CSV output with all columns
  - Hierarchical tree showing tool → workflow → object relationships
  - Department distribution showing VID, AID, MKT representation

### Test 2: Lead Generation Content (Video_006)
- **Content**: Google SERP scraping and email enrichment workflow
- **Expected Entities**: Tools (LGN), Workflows (LGN), Actions (Data Ops), Objects (LGN)
- **Validation**:
  - Data operations actions properly categorized (Category G)
  - Integration patterns showing tool chains
  - Department distribution showing LGN dominance

### Test 3: Browser Automation Content (Video_004)
- **Content**: Perplexity Comet browser automation
- **Expected Entities**: Tools (AID), Workflows (AID), Actions (Browser/Agentic)
- **Validation**:
  - Browser/agentic actions properly categorized (Category F)
  - Skills and professions extracted (AI Engineer)
  - Integration patterns showing agentic workflow chains

### Test 4: CSV Import Test
- Extract entities from test video
- Generate CSV master list output
- Import CSV into spreadsheet application
- Verify all columns populated correctly
- Confirm no formatting errors (escaped commas, proper quotes)

### Test 5: Cross-Section Consistency
- Count entities in CSV master list
- Count entities in department distribution table
- Count entities in metadata summary
- Verify all three counts match exactly

---

## Notes for Implementation

1. **Preserve Core Functionality**: The video transcription instructions (v3.1) are production-ready and highly effective. All changes should be additive only - do not remove or fundamentally alter existing sections.

2. **Entity ID Placeholders**: Since the transcription process doesn't know the current max ID in the LIBRARIES system, use placeholder format `TOL-[next]` or best-guess sequential IDs. Final ID assignment happens during taxonomy integration.

3. **Multi-Department Mapping**: Some entities (especially tools and workflows) serve multiple departments. Use semicolon-separated codes in CSV (e.g., "VID;AID;MKT") but assign to single primary department in distribution table.

4. **Status Field**: All newly extracted entities should have status "Pending_Review" since they require validation before full taxonomy integration.

5. **Source Attribution**: Always use format `Video_XXX` for source field to maintain consistency with existing LIBRARIES provenance tracking.

6. **Simple ID Format**: Despite some existing files using sub-categorized IDs (e.g., OBJ-MEDIA-100), the reference architecture specifies simple format (OBJ-100). Follow the reference architecture for new extractions.

7. **ASCII Tree Formatting**: Use standard ASCII tree characters (├── └── │) for hierarchical trees. Test rendering in markdown viewers to ensure proper display.

8. **CSV Escaping**: Ensure description fields containing commas are properly quoted. Follow RFC 4180 CSV standard.

---

## Approval & Sign-off

**Prepared By**: Taxonomy Architecture Team
**Review Required**: Yes
**Approver**: LIBRARIES Taxonomy Lead
**Implementation Target**: v4.0
**Estimated Effort**: 2-3 hours (careful review + systematic updates)

---

**END OF OPTIMIZATION PROMPT**
