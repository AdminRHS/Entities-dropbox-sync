# Actions Library Extraction and Cross-Referencing Prompt
## Extracting Action Verbs and Operations from Video Transcriptions

**Purpose**: Systematic methodology for identifying, extracting, normalizing, and cross-referencing Actions (standardized action verbs) from video transcriptions and integrating them into the LIBRARIES/Actions taxonomy.

**Version**: 1.1 - Tool ID Format Standardization & Terminology Update
**Date**: 2025-11-19
**Status**: Active - Production Ready
**Last Updated**: 2025-11-19

### Version History
- **v1.1** (2025-11-19): Tool ID format standardization (TOL-### → TOOL-{CATEGORY}-###), "Gap Analysis" → "Library Enrichment" terminology update
- **v1.0** (2025-11-19): Taxonomy Architecture Alignment

---

## Table of Contents

1. [Overview](#overview)
2. [Understanding Actions in Taxonomy](#understanding-actions-in-taxonomy)
3. [Action Identification Process](#action-identification-process)
4. [Action Type Categorization](#action-type-categorization)
5. [Cross-Referencing Methodology](#cross-referencing-methodology)
6. [Creating Action Entries](#creating-action-entries)
7. [Real Examples from Video_001](#real-examples-from-video_001)
8. [Quality Assurance](#quality-assurance)
9. [Summary Workflow](#summary-workflow)
10. [ID Assignment Standards](#id-assignment-standards)
11. [Related Documentation](#related-documentation)

---

## Overview

### What Are Actions?

In the taxonomy system, **Actions** are:
- **Standardized action verbs** in their base (infinitive) form
- **Operations** that professions perform on objects
- **The verb portion** of Task Templates (Action + Object = Task)
- **Normalized** to eliminate redundancy (e.g., "create", "created", "creating" → "create")
- **Categorized** by operational purpose (Communication, Creation, Analysis, etc.)

### Why Extract Actions from Videos?

Video transcriptions are rich sources of:
- **Workflow operations** mentioned ("I generate...", "you can send...", "to analyze...")
- **Task actions** performed ("create thumbnails", "edit videos", "export files")
- **Process verbs** described in demonstrations
- **Tool-enabled actions** (what actions become possible with specific tools)

Extracting and cataloging these actions:
1. Completes the taxonomy for "Action + Object = Task" structure
2. Enables action normalization across all task templates
3. Documents which tools enable which actions
4. Maps profession-action-object relationships
5. Identifies action types and operational categories
6. Supports automatic task naming conventions

### The Action + Object = Task Formula

```
Action (verb) + Object (noun) = Task Template

Examples:
- create + thumbnail = Create Thumbnail
- generate + script = Generate Script
- analyze + leads = Analyze Leads
- send + email = Send Email
- export + data = Export Data
```

---

## Understanding Actions in Taxonomy

### Action Structure

Each action has:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "action_type": "Creation",
  "verb_forms": {
    "base": "create",
    "past_tense": "created",
    "gerund": "creating",
    "past_participle": "created",
    "third_person": "creates"
  },
  "synonyms": ["make", "generate", "build", "produce"],
  "objects_acted_upon": ["OBJ-001", "OBJ-045", "OBJ-103"],
  "objects_list": ["thumbnails", "videos", "scripts", "designs", "presentations"],
  "tools_that_enable": ["TOL-008", "TOL-030", "TOL-019"],
  "tools_list": ["ChatGPT", "Midjourney", "Photoshop", "Canva"],
  "professions": ["PRF-008", "PRF-015", "PRF-022"],
  "professions_list": ["Content Creator", "Graphic Designer", "Video Producer"],
  "workflows": ["WRF-001", "WRF-012"],
  "skills": ["SKL-015", "SKL-023"],
  "example_usage": [
    "create thumbnails with high CTR",
    "create video scripts",
    "create mockups for client",
    "create social media content"
  ],
  "department": "ALL",
  "complexity": "Low to Medium",
  "common_contexts": ["content creation", "design workflows", "video production"],
  "related_actions": ["ACT-089", "ACT-156"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Actions/"
}
```

### Action Categories (Types)

Actions are organized into operational categories:

#### 1. **Communication Actions**
Purpose: Information exchange and interaction
- Examples: Send, Notify, Contact, Respond, Follow-up, Share, Present, Communicate, Discuss, Inform, Update (when informational)
- File: `Communication_Actions.json`
- Department: ALL (universal need)
- Typical objects: emails, messages, notifications, presentations, reports, calls

#### 2. **Creation Actions**
Purpose: Bringing new entities into existence
- Examples: Create, Generate, Build, Design, Develop, Produce, Compose, Draft, Make, Construct, Establish
- File: `Creative_Actions.json` (verify actual filename)
- Department: DGN, VID, DEV, ALL
- Typical objects: thumbnails, videos, scripts, designs, code, content, mockups, prototypes

#### 3. **Analysis Actions**
Purpose: Examination, evaluation, and insight generation
- Examples: Analyze, Review, Evaluate, Assess, Research, Examine, Investigate, Study, Inspect, Audit, Test, Validate
- File: `Analysis_Actions.json`
- Department: AI, DATA, HR, SALES
- Typical objects: data, reports, performance, leads, metrics, code, results

#### 4. **Management Actions**
Purpose: Organization, coordination, and oversight
- Examples: Update, Manage, Organize, Coordinate, Track, Plan, Schedule, Prioritize, Assign, Delegate, Monitor, Control
- File: `Management_Actions.json`
- Department: PM, HR, OPS, ALL
- Typical objects: projects, tasks, teams, resources, schedules, budgets, workflows

#### 5. **Processing Actions**
Purpose: Data manipulation, transformation, and formatting
- Examples: Process, Transform, Convert, Export, Import, Parse, Format, Normalize, Clean, Merge, Filter, Extract, Compile
- File: `Processing_Actions.json` (verify)
- Department: DATA, DEV, AI
- Typical objects: data, files, reports, leads, contacts, documents, datasets

#### 6. **Modification Actions**
Purpose: Changing existing entities
- Examples: Edit, Refine, Optimize, Enhance, Update (when modifying), Revise, Modify, Adjust, Improve, Customize, Adapt, Correct, Fix
- File: May be in Creative_Actions.json or separate
- Department: ALL
- Typical objects: videos, images, code, documents, designs, content

#### 7. **Organization Actions**
Purpose: Structuring and arranging
- Examples: Organize, Structure, Categorize, Classify, Group, Sort, Arrange, Order, Index, Tag, Label
- File: May overlap with Management_Actions.json
- Department: ALL
- Typical objects: files, folders, data, tasks, contacts, resources, content

### Action File Structure

Actions are stored in:
```
ENTITIES/LIBRARIES/Responsibilities/Actions/
├── Actions_Master.json (429 actions - master list with all action IDs)
├── Actions_Master_Command_Verbs.json (command-style actions)
├── Actions_Master_Process_Verbs.json (process-oriented actions)
├── Actions_Master_Result_Verbs.json (result-focused actions)
├── Communication_Actions.json (verified filename)
├── Creative_Actions.json (verify - may be Creation_Actions.json)
├── Analysis_Actions.json (verify)
├── Management_Actions.json (verify)
├── Processing_Actions.json (verify)
└── Data_Operations/ (11 specialized action files for data workflows)
```

**Note**: Verify actual category file names during implementation. Actions_Master.json is confirmed (429 actions).

---

## Action Identification Process

### Phase 1: Read and Mark Actions (15-20 minutes)

#### Step 1: Scan Transcription for Action Verbs

Look for mentions of operations, tasks, and processes:

**Trigger phrases**:
- "I [verb]" → "I create", "I send", "I analyze"
- "you can [verb]" → "you can generate", "you can export"
- "to [verb]" → "to process", "to convert", "to organize"
- "[verb] the [object]" → "edit the video", "send the email", "create the thumbnail"
- "it [verb]s" → "it generates", "it processes", "it transforms"
- "[verb]ing [object]" → "creating content", "analyzing data", "sending notifications"
- "you [verb]" → "you create", "you design", "you manage"

#### Step 2: Identify Action Mentions

**From Video_001 example**:

> [02:34] "...for thumbnails, I use this Nano Banana agent..."
**Action implied**: create (thumbnails are being created)

> [03:15] "...you can create YouTube thumbnails with high CTR..."
**Action identified**: create
**Verb forms found**: create, creates, creating

> [06:20] "...it generates a 32-second miniature documentary..."
**Action identified**: generate
**Verb forms found**: generates, generate, generating

> [06:25] "...Perplexity researches the topic and generates a script..."
**Actions identified**:
- research (researches)
- generate (generates)

> [08:30] "...then Eleven Labs creates the voiceover..."
**Action identified**: create (creates)

> [09:15] "...I export the final video..."
**Action identified**: export

> [10:20] "...you edit the clips together..."
**Action identified**: edit

> [04:10] "...it analyzes your prompt and optimizes the output..."
**Actions identified**:
- analyze (analyzes)
- optimize (optimizes)

#### Step 3: Extract All Verb Forms

For each action identified, capture all forms found in transcription:

```
ACTION VERB FORMS INVENTORY:

1. create
   - Forms found: "create" [base], "creates" [3rd person], "creating" [gerund], "created" [past]
   - Mentions: 15 times
   - Timestamps: [02:34], [03:15], [08:30], [11:45]...
   - Contexts: "create thumbnails", "creates the voiceover", "creating content", "created with AI"
   - Objects: thumbnails, videos, scripts, voiceovers, images

2. generate
   - Forms found: "generate" [base], "generates" [3rd person], "generating" [gerund], "generated" [past]
   - Mentions: 12 times
   - Timestamps: [06:20], [06:25], [07:10], [09:30]...
   - Contexts: "generates a documentary", "generate a script", "generating images", "generated by AI"
   - Objects: videos, scripts, images, ideas, content

3. research
   - Forms found: "research" [base], "researches" [3rd person], "researching" [gerund]
   - Mentions: 4 times
   - Timestamps: [06:25], [07:45]...
   - Contexts: "researches the topic", "research the subject", "researching information"
   - Objects: topics, subjects, information, data

4. edit
   - Forms found: "edit" [base], "edits" [3rd person], "editing" [gerund], "edited" [past]
   - Mentions: 8 times
   - Timestamps: [10:20], [11:30]...
   - Contexts: "edit the clips", "editing videos", "edited together"
   - Objects: videos, clips, images, content

5. export
   - Forms found: "export" [base], "exports" [3rd person], "exporting" [gerund]
   - Mentions: 3 times
   - Timestamps: [09:15]...
   - Contexts: "export the final video", "export as MP4"
   - Objects: videos, files, data

6. analyze
   - Forms found: "analyze" [base], "analyzes" [3rd person]
   - Mentions: 2 times
   - Timestamps: [04:10]...
   - Contexts: "analyzes your prompt", "analyze the output"
   - Objects: prompts, outputs, data, performance

7. optimize
   - Forms found: "optimize" [base], "optimizes" [3rd person], "optimizing" [gerund]
   - Mentions: 5 times
   - Timestamps: [04:10], [05:20]...
   - Contexts: "optimizes the output", "optimize for CTR", "optimizing thumbnails"
   - Objects: outputs, thumbnails, videos, content

[Continue for all actions found...]
```

#### Step 4: Normalize to Base Form

For each action, determine the **base form** (infinitive):

```
NORMALIZED ACTIONS:

create (from: create, creates, creating, created)
generate (from: generate, generates, generating, generated)
research (from: research, researches, researching, researched)
edit (from: edit, edits, editing, edited)
export (from: export, exports, exporting, exported)
analyze (from: analyze, analyzes, analyzing, analyzed)
optimize (from: optimize, optimizes, optimizing, optimized)
send (from: send, sends, sending, sent)
process (from: process, processes, processing, processed)
transform (from: transform, transforms, transforming, transformed)

[Continue for all...]
```

### Phase 2: Categorize Actions (10-15 minutes)

#### Step 5: Assign Actions to Categories

For each normalized action, determine its operational category:

```
ACTION CATEGORIZATION:

Communication Actions:
  - send (messages, emails, notifications)
  - notify (users, clients, team)
  - share (content, files, links)
  - present (results, findings, proposals)

Creation Actions:
  - create (thumbnails, videos, scripts, content)
  - generate (documentaries, images, ideas)
  - design (mockups, layouts, interfaces)
  - produce (videos, content, deliverables)
  - build (workflows, systems, prototypes)

Analysis Actions:
  - analyze (prompts, data, performance)
  - research (topics, subjects, information)
  - evaluate (results, quality, effectiveness)
  - review (content, code, deliverables)

Management Actions:
  - manage (projects, resources, workflows)
  - organize (files, content, tasks)
  - coordinate (teams, efforts, schedules)
  - track (progress, metrics, time)

Processing Actions:
  - process (data, files, inputs)
  - transform (content, formats, structures)
  - convert (files, formats, types)
  - export (videos, data, reports)
  - import (data, assets, files)

Modification Actions:
  - edit (videos, images, content)
  - optimize (thumbnails, content, performance)
  - refine (designs, outputs, results)
  - enhance (quality, features, capabilities)
  - update (information, content, status)
```

#### Step 6: Check Existing Actions Library

**Check files**:
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json` (429 actions - master list)
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Communication_Actions.json`
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Creative_Actions.json` (verify name)
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Analysis_Actions.json` (verify)
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Management_Actions.json` (verify)
- `ENTITIES/LIBRARIES/Responsibilities/Actions/README.md` (if exists)
- `ENTITIES/LIBRARIES/README.md` (for Actions section)

**For each identified action**:
- ✅ **EXISTS**: Note what needs enhancement (new objects, tools, contexts, synonyms)
- ❌ **MISSING**: Mark for creation with priority level

```
ACTIONS GAP ANALYSIS:

✅ EXISTS in Actions_Master.json (Enhance):

ACT-044: create ✓
  - Current objects: lesson structure, repository (from previous work)
  - **ENHANCEMENT**: ADD objects (thumbnails, videos, scripts, voiceovers, images, content)
  - **ENHANCEMENT**: ADD tools (Nano Banana, GLIF, Midjourney, Photoshop, ChatGPT)
  - **ENHANCEMENT**: ADD contexts (content creation, video production, AI-assisted design)
  - No changes needed to base action definition

ACT-089: generate ✓
  - Current objects: interactive elements, HTML/CSS code (from previous work)
  - **ENHANCEMENT**: ADD objects (documentaries, videos, scripts, images, ideas)
  - **ENHANCEMENT**: ADD tools (VAYU, Seedream, Sora, Perplexity, ChatGPT, GLIF)
  - **ENHANCEMENT**: ADD contexts (AI content generation, documentary creation, script writing)
  - No changes needed to base action definition

ACT-156: edit ✓
  - Current objects: files, code (from previous work)
  - **ENHANCEMENT**: ADD objects (videos, clips, images, thumbnails, audio)
  - **ENHANCEMENT**: ADD tools (Video editing software, Photoshop, Audio editors)
  - **ENHANCEMENT**: ADD contexts (video editing, image retouching, content refinement)

[Continue for all matched actions...]

CHECK IF EXISTS (Need verification):
  - research → VERIFY if exists with action_id
    - If exists: ADD tools (Perplexity, ChatGPT, Google)
    - If exists: ADD objects (topics, subjects, information, data)
    - If NOT exists: CREATE as NEW action (see MISSING section)

  - optimize → VERIFY if exists
    - If exists: ADD contexts (CTR optimization, thumbnail optimization, content optimization)
    - If exists: ADD tools (A/B testing tools, Analytics tools)
    - If NOT exists: CREATE as NEW action

  - export → VERIFY if exists
    - Likely exists (common data operation)
    - If exists: ADD contexts (video export, data export, file export)
    - If exists: ADD tools (Video editing software, Data tools, Export utilities)

❌ MISSING (Create new entries):

Priority: MEDIUM (Most actions likely exist in 429-action library)
  - [Action name] (if truly missing after verification)
    - Category: [Action Type]
    - Objects: [List objects this action applies to]
    - Tools: [List tools that enable this action]
    - Professions: [List professions that perform this action]
    - Example usage: [Phrases from video]
    - Synonyms: [Alternative verbs with same meaning]
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Actions/[Category]_Actions.json
    - **CREATE FULL ENTRY** (use template from Creating Action Entries section)

NOTE: With 429 existing actions, most video actions will be ✅ MATCHES or ✅ ENHANCEMENTS rather than ❌ NEW.
Focus on enriching existing entries with new objects, tools, contexts, and use cases.
```

---

## Action Type Categorization

### Step 7: Extract Action Contexts from Video

For each action, identify its **contexts** (how and when it's used):

#### Method: Context Analysis

**Look for**:
- Purpose phrases: "to create content", "for generating videos", "when analyzing data"
- Tool associations: "create with Midjourney", "generate using AI", "edit in Premiere"
- Object associations: "create thumbnails", "generate scripts", "edit videos"
- Workflow contexts: "during content creation", "in video production", "for lead generation"
- Quality modifiers: "quickly create", "professionally edit", "accurately analyze"

#### Example: Create Action Contexts

**From transcription**:
- [02:34] "...for thumbnails, I use this agent..."
  - **Context**: thumbnail creation
  - **Tool**: Nano Banana agent
  - **Purpose**: content creation

- [03:15] "...you can create YouTube thumbnails with high CTR..."
  - **Context**: YouTube thumbnail creation
  - **Purpose**: CTR optimization
  - **Quality**: high-converting

- [08:30] "...Eleven Labs creates the voiceover..."
  - **Context**: voiceover creation
  - **Tool**: Eleven Labs
  - **Purpose**: audio production

**Extracted contexts for "create"**:
1. Content creation workflows
2. AI-assisted design
3. Video production pipelines
4. Thumbnail generation
5. Audio/voiceover production
6. Script development
7. High-CTR asset creation

### Step 8: Map Actions to Tools

For each action, identify which **tools enable or perform** the action:

```
ACTION-TOOL MAPPING:

create:
  - TOL-XXX: Nano Banana (creates thumbnails)
  - TOL-XXX: GLIF (creates various content)
  - TOL-XXX: Midjourney (creates images)
  - TOL-XXX: Photoshop (creates designs)
  - TOL-008: ChatGPT (creates scripts, text)
  - TOL-XXX: Eleven Labs (creates voiceovers)

generate:
  - TOL-XXX: VAYU (generates videos)
  - TOL-XXX: Seedream (generates videos)
  - TOL-XXX: Sora (generates videos)
  - TOL-XXX: GLIF (generates content)
  - TOL-XXX: Perplexity (generates research)
  - TOL-008: ChatGPT (generates scripts)

edit:
  - TOL-XXX: Premiere Pro (edits videos)
  - TOL-XXX: Photoshop (edits images)
  - TOL-XXX: Final Cut (edits videos)
  - TOL-019: VSCode (edits code)

research:
  - TOL-XXX: Perplexity (researches topics)
  - TOL-008: ChatGPT (researches information)
  - TOL-XXX: Google (researches data)

optimize:
  - TOL-XXX: Analytics tools (optimize performance)
  - TOL-XXX: A/B testing tools (optimize CTR)
  - AI tools (optimize prompts, content)

export:
  - TOL-XXX: Video editing software (export videos)
  - TOL-XXX: Data tools (export data)
  - TOL-XXX: Design tools (export assets)

[Continue for all actions...]
```

### Step 9: Map Actions to Objects

For each action, list all **objects** it can be performed on:

```
ACTION-OBJECT MAPPING:

create:
  - OBJ-XXX: thumbnails (YouTube thumbnail, High-CTR thumbnail, Social thumbnail)
  - OBJ-XXX: videos (Miniature documentary, TikTok video, Social video)
  - OBJ-XXX: scripts (Documentary script, Voiceover script, Video script)
  - OBJ-XXX: voiceovers (Documentary narration, Professional voiceover)
  - OBJ-XXX: images (Reference image, Generated image, Concept art)
  - OBJ-XXX: designs (Mockups, Layouts, Interfaces)
  - OBJ-XXX: content (Social media content, Blog content)

generate:
  - OBJ-XXX: videos (AI-generated video, Documentary, Short-form video)
  - OBJ-XXX: scripts (AI-generated script, Research-based script)
  - OBJ-XXX: images (AI-generated images, Concept images)
  - OBJ-XXX: ideas (Concepts, Topics, Themes)
  - OBJ-XXX: research (Topic research, Subject analysis)

edit:
  - OBJ-XXX: videos (Final edit, Rough cut, Assembled clips)
  - OBJ-XXX: images (Retouched images, Adjusted photos)
  - OBJ-XXX: audio (Cleaned audio, Mixed audio)
  - OBJ-XXX: content (Refined content, Updated text)
  - OBJ-XXX: code (Modified code, Updated scripts)

research:
  - OBJ-XXX: topics (Subject areas, Themes, Concepts)
  - OBJ-XXX: information (Data, Facts, Statistics)
  - OBJ-XXX: subjects (Areas of study, Domains)
  - OBJ-XXX: data (Market data, User data, Performance data)

optimize:
  - OBJ-XXX: thumbnails (High-CTR thumbnails, Click-optimized thumbnails)
  - OBJ-XXX: content (SEO-optimized content, Engagement-optimized content)
  - OBJ-XXX: performance (Speed, Efficiency, Quality)
  - OBJ-XXX: prompts (AI prompts, Generation prompts)

export:
  - OBJ-XXX: videos (Final video, Rendered video, Exported file)
  - OBJ-XXX: data (Exported dataset, Report data)
  - OBJ-XXX: files (Export files, Archive files)

[Continue for all actions...]
```

---

## Cross-Referencing Methodology

### Phase 3: Cross-Reference Actions (15-20 minutes)

#### Step 10: Action → Object Cross-References

For each action, create complete object linkages:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "objects_acted_upon": [
    "OBJ-001",
    "OBJ-045",
    "OBJ-067",
    "OBJ-103",
    "OBJ-156",
    "OBJ-234"
  ],
  "objects_list": [
    "thumbnails",
    "videos",
    "scripts",
    "voiceovers",
    "images",
    "designs",
    "mockups",
    "presentations",
    "content",
    "lesson structure",
    "repository",
    "interactive elements"
  ],
  "object_categories": [
    "Design Deliverables",
    "Media",
    "Documents",
    "Data"
  ]
}
```

**Cross-reference validation**:
- ✅ Each object ID exists in Objects library
- ✅ Object names match official object_name in Objects entries
- ✅ Object categories align with Objects taxonomy structure

#### Step 11: Action → Tool Cross-References

For each action, link to enabling tools:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "tools_that_enable": [
    "TOL-008",
    "TOL-019",
    "TOL-030",
    "TOL-XXX",
    "TOL-XXX"
  ],
  "tools_list": [
    "ChatGPT",
    "VSCode",
    "Online Academy",
    "Nano Banana",
    "GLIF",
    "Midjourney",
    "Photoshop",
    "Canva",
    "Eleven Labs"
  ],
  "tool_categories": [
    "AI Assistants",
    "Development Tools",
    "Design Tools",
    "Content Creation Tools"
  ]
}
```

**Cross-reference validation**:
- ✅ Each tool ID exists in Tools library (or flagged as NEW)
- ✅ Tool names match official tool names
- ✅ Tool categories align with Tools taxonomy

#### Step 12: Action → Profession Cross-References

For each action, link to professions that perform it:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "professions": [
    "PRF-008",
    "PRF-015",
    "PRF-022",
    "PRF-XXX",
    "PRF-XXX"
  ],
  "professions_list": [
    "Content Creator",
    "Graphic Designer",
    "Video Producer",
    "Instructional Designer",
    "Web Developer",
    "Scriptwriter",
    "Documentary Producer"
  ],
  "profession_departments": [
    "VID",
    "DGN",
    "DEV",
    "AI"
  ]
}
```

**Cross-reference validation**:
- ✅ Each profession ID exists in Professions library (or flagged as NEW)
- ✅ Profession names match official profession names
- ✅ Departments align with Professions taxonomy

#### Step 13: Action → Workflow Cross-References

For each action, link to workflows that include it:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "workflows": [
    "WRF-001",
    "WRF-012",
    "WRF-XXX"
  ],
  "workflows_list": [
    "AI-Assisted Content Creation",
    "Video Production Pipeline",
    "Thumbnail Generation Workflow",
    "Documentary Creation Process"
  ],
  "workflow_stages": [
    "Content ideation",
    "Asset creation",
    "Production",
    "Design phase"
  ]
}
```

**Cross-reference validation**:
- ✅ Workflow IDs match Workflows library (when available)
- ✅ Workflow names are descriptive and consistent
- ✅ Stages align with typical workflow phases

#### Step 14: Action → Skill Cross-References

For each action, link to skills that include it:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "skills": [
    "SKL-015",
    "SKL-023",
    "SKL-NEW-001"
  ],
  "skills_list": [
    "lesson creation with Online Academy",
    "AI-assisted HTML/CSS code generation with ChatGPT",
    "thumbnail creation with Nano Banana",
    "video creation with AI tools"
  ],
  "skill_formula_examples": [
    "create lesson structure + Online Academy = lesson creation skill",
    "create code + ChatGPT = AI-assisted code generation skill",
    "create thumbnails + Nano Banana = thumbnail creation skill"
  ]
}
```

**Skill formula**: Skill = Action + Object + Tool

**Cross-reference validation**:
- ✅ Skills follow formula: Action (create) + Object + Tool = Skill
- ✅ Skill IDs exist in Skills library (or flagged as NEW)
- ✅ Skill descriptions are accurate and consistent

---

## Creating Action Entries

### Step 15: Build Complete Action Entry

Use this template for each new or enhanced action:

```json
{
  "action_id": "ACT-044",
  "action": "create",
  "action_type": "Creation",
  "definition": "Bring new entities, content, or deliverables into existence",

  "verb_forms": {
    "base": "create",
    "past_tense": "created",
    "gerund": "creating",
    "past_participle": "created",
    "third_person": "creates"
  },

  "synonyms": [
    "make",
    "generate",
    "build",
    "produce",
    "develop",
    "design",
    "construct",
    "compose"
  ],

  "objects_acted_upon": [
    "OBJ-001",
    "OBJ-045",
    "OBJ-067",
    "OBJ-103",
    "OBJ-156",
    "OBJ-234"
  ],

  "objects_list": [
    "thumbnails",
    "videos",
    "scripts",
    "voiceovers",
    "images",
    "designs",
    "mockups",
    "presentations",
    "content",
    "lesson structure",
    "repository",
    "interactive elements",
    "documentaries",
    "prototypes"
  ],

  "object_categories": [
    "Design Deliverables",
    "Media",
    "Documents",
    "Data",
    "Code"
  ],

  "tools_that_enable": [
    "TOL-008",
    "TOL-019",
    "TOL-030",
    "TOL-XXX",
    "TOL-XXX",
    "TOL-XXX"
  ],

  "tools_list": [
    "ChatGPT",
    "VSCode",
    "Online Academy",
    "Nano Banana",
    "GLIF",
    "Midjourney",
    "Photoshop",
    "Canva",
    "Eleven Labs",
    "VAYU",
    "Seedream",
    "Sora"
  ],

  "tool_categories": [
    "AI Assistants",
    "Development Tools",
    "Design Tools",
    "Content Creation Tools",
    "Video Generation Tools"
  ],

  "professions": [
    "PRF-008",
    "PRF-015",
    "PRF-022",
    "PRF-XXX",
    "PRF-XXX"
  ],

  "professions_list": [
    "Content Creator",
    "Graphic Designer",
    "Video Producer",
    "Instructional Designer",
    "Web Developer",
    "Scriptwriter",
    "Documentary Producer",
    "Audio Engineer"
  ],

  "workflows": [
    "WRF-001",
    "WRF-012",
    "WRF-XXX"
  ],

  "workflows_list": [
    "AI-Assisted Content Creation",
    "Video Production Pipeline",
    "Thumbnail Generation Workflow",
    "Documentary Creation Process",
    "Educational Content Development"
  ],

  "skills": [
    "SKL-015",
    "SKL-023",
    "SKL-NEW-001",
    "SKL-NEW-002"
  ],

  "skills_list": [
    "lesson creation with Online Academy",
    "AI-assisted HTML/CSS code generation with ChatGPT",
    "thumbnail creation with Nano Banana",
    "video creation with AI tools",
    "documentary creation with AI pipeline"
  ],

  "example_usage": [
    "create YouTube thumbnails with high CTR",
    "create a 32-second miniature documentary",
    "create video scripts with AI research",
    "create professional voiceovers using Eleven Labs",
    "create lesson structure in Online Academy",
    "create interactive elements for web content",
    "create mockups for client presentation",
    "create social media content at scale"
  ],

  "common_contexts": [
    "Content creation workflows",
    "Video production pipelines",
    "AI-assisted design",
    "Educational content development",
    "Social media content generation",
    "Documentary production",
    "Web development",
    "Graphic design projects"
  ],

  "department": "ALL",

  "complexity": "Low to Medium",

  "related_actions": [
    "ACT-089",
    "ACT-156",
    "ACT-201",
    "ACT-XXX"
  ],

  "related_actions_list": [
    "generate (similar creation process)",
    "edit (modification after creation)",
    "upload (deployment after creation)",
    "design (specialized creation)"
  ],

  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Actions/",

  "source_videos": [
    "Video_001",
    "daily_228_Kucherenko_Iuliia.md",
    "daily_171125_Niko.md"
  ],

  "extraction_date": "2025-11-19",

  "notes": [
    "Most universal creation action across all departments",
    "Applies to physical deliverables, digital content, and abstract concepts",
    "Often used interchangeably with 'generate' in AI contexts",
    "Base form for many specialized creation actions (design, build, develop)"
  ]
}
```

### Field Definitions

**Required Fields**:
- `action_id`: Unique identifier (ACT-###, 3-digit zero-padded)
- `action`: Standardized verb in base form
- `action_type`: Category (Communication, Creation, Analysis, Management, Processing, Modification, Organization)
- `verb_forms`: All conjugations of the verb
- `objects_acted_upon`: Array of object IDs this action applies to
- `tools_that_enable`: Array of tool IDs that enable this action
- `professions`: Array of profession IDs that perform this action

**Recommended Fields**:
- `definition`: Clear description of what the action means
- `synonyms`: Alternative verbs with similar meaning
- `objects_list`: Human-readable object names (mirrors objects_acted_upon)
- `tools_list`: Human-readable tool names (mirrors tools_that_enable)
- `professions_list`: Human-readable profession names (mirrors professions)
- `example_usage`: Real phrases from video transcriptions
- `common_contexts`: Typical use cases and workflow contexts
- `department`: Department codes (ISO format) or "ALL"

**Optional Fields**:
- `workflows`: Workflow IDs that include this action
- `skills`: Skill IDs that use this action
- `complexity`: Difficulty level
- `related_actions`: Similar or complementary actions
- `storage_pattern`: File path location
- `source_videos`: Videos where this action was extracted
- `extraction_date`: When the action was added/updated
- `notes`: Additional context or observations

---

## Real Examples from Video_001

### Example 1: "create" Action

**Evidence from Video_001**:

> [02:34] "...for thumbnails, I use this Nano Banana agent and I can create YouTube thumbnails..."

> [03:15] "...you can create YouTube thumbnails with high CTR using this prompt..."

> [08:30] "...then Eleven Labs creates the voiceover for the documentary..."

**Extraction Process**:

**Step 1: Identify action**
- Verb: "create"
- Forms found: create, creates
- Frequency: 15+ mentions

**Step 2: Normalize**
- Base form: create
- Past: created
- Gerund: creating
- 3rd person: creates

**Step 3: Categorize**
- Type: Creation
- Category file: Creative_Actions.json (verify)

**Step 4: Extract objects**
- thumbnails (YouTube thumbnails, High-CTR thumbnails)
- voiceovers (documentary narration)
- [From broader video context: videos, scripts, images, content]

**Step 5: Extract tools**
- Nano Banana (creates thumbnails)
- Eleven Labs (creates voiceovers)
- [From broader context: GLIF, Midjourney, ChatGPT, etc.]

**Step 6: Extract professions**
- Content Creator (implied from context)
- Video Producer (creates videos)
- Graphic Designer (creates thumbnails)

**Step 7: Build entry** → Use template above

---

### Example 2: "generate" Action

**Evidence from Video_001**:

> [06:20] "...it generates a 32-second miniature documentary about any topic..."

> [06:25] "...Perplexity researches the topic and generates a script..."

> [07:10] "...VAYU generates the tilt-shift video..."

**Extraction Process**:

**Step 1: Identify action**
- Verb: "generate"
- Forms found: generate, generates, generating
- Frequency: 12+ mentions

**Step 2: Normalize**
- Base form: generate
- Past: generated
- Gerund: generating
- 3rd person: generates

**Step 3: Categorize**
- Type: Creation
- Category file: Creative_Actions.json (verify)
- Note: Often AI-specific creation

**Step 4: Extract objects**
- documentaries (miniature documentary, 32-second documentary)
- scripts (documentary script, voiceover script)
- videos (tilt-shift video, AI-generated video)
- [From broader context: images, ideas, research]

**Step 5: Extract tools**
- VAYU (generates videos)
- Perplexity (generates scripts via research)
- [From broader context: Seedream, Sora, GLIF, ChatGPT]

**Step 6: Extract professions**
- Video Producer (generates videos)
- Content Creator (generates content)
- Documentary Producer (generates documentaries)
- Scriptwriter (generates scripts)

**Step 7: Build entry** → Use template structure

---

### Example 3: "research" Action

**Evidence from Video_001**:

> [06:25] "...Perplexity researches the topic and generates a script..."

> [07:45] "...it researches any subject you want..."

**Extraction Process**:

**Step 1: Identify action**
- Verb: "research"
- Forms found: research, researches, researching
- Frequency: 4 mentions

**Step 2: Normalize**
- Base form: research
- Past: researched
- Gerund: researching
- 3rd person: researches

**Step 3: Categorize**
- Type: Analysis
- Category file: Analysis_Actions.json (verify)

**Step 4: Extract objects**
- topics (subject topics, research topics)
- subjects (any subject, research subjects)
- information (research data, factual information)

**Step 5: Extract tools**
- Perplexity (primary research tool)
- [From broader context: ChatGPT, Google, Claude]

**Step 6: Extract professions**
- Content Creator (researches topics for content)
- Scriptwriter (researches for scripts)
- Video Producer (researches for documentaries)
- Research Analyst (if exists in taxonomy)

**Step 7: Build entry** → Use template structure

---

### Example 4: "edit" Action

**Evidence from Video_001**:

> [10:20] "...you can edit the clips together..."

> [11:30] "...after editing the video, export it as MP4..."

**Extraction Process**:

**Step 1: Identify action**
- Verb: "edit"
- Forms found: edit, editing, edited
- Frequency: 8 mentions

**Step 2: Normalize**
- Base form: edit
- Past: edited
- Gerund: editing
- 3rd person: edits

**Step 3: Categorize**
- Type: Modification
- Category file: Creative_Actions.json or Modification_Actions.json (verify)

**Step 4: Extract objects**
- videos (edited video, final cut)
- clips (video clips, assembled clips)
- images (retouched images)
- [From broader context: audio, content, code]

**Step 5: Extract tools**
- [Implied: Premiere Pro, Final Cut, video editing software]
- [From broader context: Photoshop (images), VSCode (code)]

**Step 6: Extract professions**
- Video Producer (edits videos)
- Content Creator (edits content)
- Video Editor (PRF-XXX - check if exists)

**Step 7: Build entry** → Use template structure

---

### Example 5: "export" Action

**Evidence from Video_001**:

> [09:15] "...I export the final video as MP4..."

> [11:45] "...export it in 1920x1080 resolution..."

**Extraction Process**:

**Step 1: Identify action**
- Verb: "export"
- Forms found: export, exports, exporting
- Frequency: 3 mentions

**Step 2: Normalize**
- Base form: export
- Past: exported
- Gerund: exporting
- 3rd person: exports

**Step 3: Categorize**
- Type: Processing
- Category file: Processing_Actions.json (verify)

**Step 4: Extract objects**
- videos (final video, rendered video, MP4 file)
- files (export files, output files)
- [From broader context: data, reports, assets]

**Step 5: Extract tools**
- Video editing software (export functionality)
- [From broader context: Data tools, Design tools with export features]

**Step 6: Extract professions**
- Video Producer (exports videos)
- Content Creator (exports content)
- [From broader context: Data Analyst (exports data)]

**Step 7: Build entry** → Use template structure

---

## Quality Assurance

### Completeness Checklist

#### Action Extraction Quality

- [ ] All action verbs identified from transcription (scan complete)
- [ ] All verb forms captured (base, past, gerund, past participle, 3rd person)
- [ ] Actions normalized to base form (infinitive)
- [ ] Action frequency counted (number of mentions)
- [ ] Timestamps recorded for each mention
- [ ] Contexts captured for each usage

#### Categorization Quality

- [ ] All actions assigned to correct category (Communication, Creation, Analysis, Management, Processing, Modification, Organization)
- [ ] Category assignments verified against category definitions
- [ ] Ambiguous actions flagged for review
- [ ] Related actions within same category identified

#### Cross-Reference Quality

- [ ] **Action → Object cross-references complete**
  - [ ] All objects this action applies to identified
  - [ ] Object IDs verified against Objects library
  - [ ] Object names match official taxonomy
  - [ ] Object categories aligned

- [ ] **Action → Tool cross-references complete**
  - [ ] All tools that enable this action identified
  - [ ] Tool IDs verified against Tools library (or flagged as NEW)
  - [ ] Tool names match official taxonomy
  - [ ] Tool categories aligned

- [ ] **Action → Profession cross-references complete**
  - [ ] All professions that perform this action identified
  - [ ] Profession IDs verified against Professions library
  - [ ] Profession names match official taxonomy
  - [ ] Departments aligned

- [ ] **Action → Workflow cross-references complete**
  - [ ] Workflows that include this action identified
  - [ ] Workflow stages/phases documented
  - [ ] Workflow IDs assigned (or TBD)

- [ ] **Action → Skill cross-references complete**
  - [ ] Skills that use this action identified
  - [ ] Skill formula applied (Action + Object + Tool = Skill)
  - [ ] Skill IDs verified against Skills library

#### Entry Structure Quality

- [ ] All required fields populated (action_id, action, action_type, verb_forms, objects_acted_upon, tools_that_enable, professions)
- [ ] All recommended fields populated (definition, synonyms, example_usage, common_contexts, department)
- [ ] Optional fields added where relevant (workflows, skills, complexity, related_actions)
- [ ] JSON structure valid (no syntax errors)
- [ ] Field values consistent with taxonomy standards

#### Library Enrichment Quality

- [ ] Existing actions library checked (Actions_Master.json - 429 actions)
- [ ] Each action marked as ✅ EXISTS, ✅ CHECK, or ❌ MISSING
- [ ] Enhancement needs documented for existing actions
- [ ] New actions flagged with priority level (CRITICAL, HIGH, MEDIUM, LOW)
- [ ] Suggested file locations provided for new actions
- [ ] Library update recommendations listed

### Accuracy Validation

#### Semantic Accuracy

- [ ] Action definitions are clear and accurate
- [ ] Synonyms are true equivalents (not just related verbs)
- [ ] Example usage reflects real transcription phrases
- [ ] Contexts are realistic and well-documented

#### Taxonomy Alignment

- [ ] Action types match taxonomy category definitions
- [ ] Departments use ISO codes (3-letter format)
- [ ] Object relationships make logical sense
- [ ] Tool relationships are technically accurate
- [ ] Profession relationships are realistic

#### ID Format Validation

- [ ] Action IDs follow ACT-### format (3-digit zero-padded)
- [ ] Object IDs follow OBJ-### format
- [ ] Tool IDs follow TOOL-{CATEGORY}-### format
- [ ] Profession IDs follow PRF-### format
- [ ] Workflow IDs follow WRF-### format
- [ ] Skill IDs follow SKL-### format
- [ ] All IDs are unique (no duplicates)

### Cross-Reference Verification

#### Bidirectional Links

For each action entry, verify:

- [ ] **Action ↔ Object**: Objects list matches object IDs
- [ ] **Action ↔ Tool**: Tools list matches tool IDs
- [ ] **Action ↔ Profession**: Professions list matches profession IDs
- [ ] **Action ↔ Workflow**: Workflows referenced are documented
- [ ] **Action ↔ Skill**: Skills referenced use correct formula

#### Library Consistency

- [ ] Object names match Objects library entries
- [ ] Tool names match Tools library entries
- [ ] Profession names match Professions library entries
- [ ] Workflow names are consistent with Workflows taxonomy (when available)
- [ ] Skill names follow standard formula format

### JSON Structure Validation

#### Syntax Check

- [ ] Valid JSON format (no syntax errors)
- [ ] All strings properly quoted
- [ ] All arrays properly formatted with []
- [ ] All objects properly formatted with {}
- [ ] No trailing commas
- [ ] Proper nesting and indentation

#### Schema Compliance

- [ ] All required fields present
- [ ] Field types correct (strings, arrays, objects as defined)
- [ ] Array contents consistent (all IDs or all names)
- [ ] No undefined or null values in required fields

---

## Summary Workflow

### End-to-End Process

**Phase 1: Identification (15-20 min)**
1. Scan transcription for action verbs
2. Extract all verb forms (base, past, gerund, etc.)
3. Normalize to base form
4. Count frequency and note timestamps

**Phase 2: Categorization (10-15 min)**
5. Assign actions to categories (Communication, Creation, Analysis, Management, Processing, Modification, Organization)
6. Check existing Actions library (Actions_Master.json - 429 actions)
7. Mark as ✅ EXISTS (enhance), ✅ CHECK (verify), or ❌ MISSING (create)

**Phase 3: Cross-Referencing (15-20 min)**
8. Map Action → Object relationships
9. Map Action → Tool relationships
10. Map Action → Profession relationships
11. Map Action → Workflow relationships
12. Map Action → Skill relationships

**Phase 4: Entry Creation (20-30 min)**
13. Build complete action entries using template
14. Populate all required fields
15. Add recommended and optional fields
16. Include cross-reference IDs and lists

**Phase 5: Quality Assurance (10-15 min)**
17. Run completeness checklist
18. Validate accuracy (definitions, synonyms, examples)
19. Verify cross-references (bidirectional links)
20. Check JSON structure and syntax
21. Align with taxonomy standards

**Total Time**: ~70-100 minutes per video (depending on action count and complexity)

### Output Deliverables

1. **Actions Inventory** (from Phase 1)
   - List of all actions identified
   - Verb forms and frequencies
   - Timestamps and contexts

2. **Action Categorization** (from Phase 2)
   - Actions organized by category
   - Gap analysis (✅ EXISTS, ✅ CHECK, ❌ MISSING)
   - Enhancement recommendations

3. **Cross-Reference Maps** (from Phase 3)
   - Action → Object mapping
   - Action → Tool mapping
   - Action → Profession mapping
   - Action → Workflow mapping
   - Action → Skill mapping

4. **Complete Action Entries** (from Phase 4)
   - JSON-formatted action entries
   - All required and recommended fields
   - Cross-reference IDs and lists
   - Example usage and contexts

5. **Quality Report** (from Phase 5)
   - Completeness checklist results
   - Validation findings
   - Taxonomy alignment confirmation
   - Suggested improvements

### Integration Points

**Update Actions Library**:
- Add new actions to `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`
- Update category files (Communication_Actions.json, Creative_Actions.json, etc.)
- Increment action count in README.md

**Update Cross-References**:
- Enhance Objects library with action cross-references
- Enhance Tools library with action cross-references
- Enhance Professions library with action cross-references
- Update Workflows library with action inclusions
- Update Skills library with action components

**Update Task Templates**:
- Create new Task Templates using Action + Object formula
- Update existing Task Templates with verified action IDs
- Align Task naming conventions with standardized actions

---

## ID Assignment Standards

### Action ID Format

**Format**: `ACT-###`
- Prefix: `ACT-` (all caps)
- Number: 3-digit zero-padded (001, 002, ..., 999)
- Examples: ACT-001, ACT-044, ACT-429

**ID Assignment Rules**:
1. Check Actions_Master.json for next available ID (current max: 429)
2. Assign sequential IDs to new actions (ACT-430, ACT-431, etc.)
3. Never reuse IDs (even if action is deprecated)
4. Maintain ID uniqueness across all action files

### Cross-Reference ID Formats

**Object IDs**: `OBJ-###`
- Example: OBJ-001, OBJ-103, OBJ-234
- Reference: Objects library

**Tool IDs**: `TOOL-{CATEGORY}-###`
- Example: TOOL-AI-008, TOOL-DESIGN-019, TOOL-DEV-030
- Reference: Tools library
- Common categories: AI, AUTO, DESIGN, DEV, VIDEO, COMM, DATA, FILE

**Profession IDs**: `PRF-###`
- Example: PRF-008, PRF-015, PRF-022
- Reference: Professions library

**Workflow IDs**: `WRF-###` or `WF-###` (verify standard)
- Example: WRF-001, WRF-012
- Reference: Workflows library (when available)

**Skill IDs**: `SKL-###`
- Example: SKL-015, SKL-023, SKL-NEW-001
- Reference: Skills library

**Department Codes**: ISO 3-letter format
- Examples: AI, VID, DGN, DEV, SMM, SALES, HR, OPS, ALL
- Reference: DEPARTMENTS taxonomy

### ID Cross-Reference Standards

**In Action Entries**:
- Use both ID arrays and name arrays
- Example:
  ```json
  "objects_acted_upon": ["OBJ-001", "OBJ-045", "OBJ-103"],
  "objects_list": ["thumbnails", "videos", "scripts"]
  ```

**Ordering**:
- IDs in numerical order
- Names in corresponding order (match ID positions)

**NEW Entities**:
- Use temporary ID format: `XXX-NEW-001`, `XXX-NEW-002`
- Replace with permanent IDs after library integration
- Flag as `❌ NEW` in gap analysis

---

## Related Documentation

### Primary References

1. **Objects Library Extraction Prompt**
   - Location: `ENTITIES/PROMPTS/PROMPTS/Analysis/Objects_Library_Extraction_Prompt.md`
   - Purpose: Parallel methodology for extracting Objects
   - Relationship: Actions and Objects combine to form Tasks

2. **Actions Library README**
   - Location: `ENTITIES/LIBRARIES/Responsibilities/Actions/README.md` (verify)
   - Purpose: Actions taxonomy structure and guidelines
   - Contains: Category definitions, file organization, ID standards

3. **LIBRARIES Master README**
   - Location: `ENTITIES/LIBRARIES/README.md`
   - Purpose: Overall taxonomy architecture
   - Contains: Actions section, cross-reference standards, taxonomy philosophy

4. **Actions_Master.json**
   - Location: `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`
   - Purpose: Master list of all 429 actions with IDs
   - Use: ID assignment, existence checking, enhancement planning

### Supporting References

5. **Skills Library README**
   - Location: `ENTITIES/LIBRARIES/Skills/README.md` (verify)
   - Purpose: Skill formation formula (Action + Object + Tool = Skill)
   - Relationship: Actions are components of Skills

6. **Task Templates Documentation**
   - Location: `ENTITIES/TASK_MANAGERS/README.md` (verify)
   - Purpose: Task naming conventions and structure
   - Relationship: Tasks follow Action + Object + Context formula

7. **Video Analysis Prompt**
   - Location: `ENTITIES/PROMPTS/PROMPTS/Analysis/Video_Analysis_Prompt.md` (verify)
   - Purpose: General video extraction methodology
   - Relationship: Provides context for action extraction

8. **Tools Library**
   - Location: `ENTITIES/LIBRARIES/Tools/`
   - Purpose: Tool taxonomy and cross-references
   - Relationship: Tools enable Actions on Objects

9. **Professions Library**
   - Location: `ENTITIES/LIBRARIES/Professions/professions_master.json` (verify)
   - Purpose: Profession definitions and relationships
   - Relationship: Professions perform Actions

10. **Workflows Library**
    - Location: `ENTITIES/LIBRARIES/Workflows/` or `ENTITIES/TASK_MANAGERS/Workflows/` (verify)
    - Purpose: Workflow definitions and sequences
    - Relationship: Workflows include multiple Actions in sequence

### Taxonomy Integration

**Action Position in Taxonomy Hierarchy**:

```
LIBRARIES
└── Responsibilities
    ├── Actions (THIS PROMPT)
    │   ├── Actions_Master.json (429 actions)
    │   ├── Communication_Actions.json
    │   ├── Creative_Actions.json
    │   ├── Analysis_Actions.json
    │   ├── Management_Actions.json
    │   ├── Processing_Actions.json
    │   └── Data_Operations/
    │
    ├── Objects (Objects_Library_Extraction_Prompt.md)
    │   ├── Design_Deliverables.json
    │   ├── Documents.json
    │   ├── Video_Deliverables.json
    │   └── [13 domain files]
    │
    └── Parameters (Future)

Skills = Actions + Objects + Tools
Tasks = Actions + Objects + Context
Workflows = Sequences of Tasks
```

**Cross-Reference Flow**:
1. Extract Actions from video (this prompt)
2. Extract Objects from video (Objects prompt)
3. Extract Tools from video (Tools prompt - if exists)
4. Cross-reference: Action → Object, Action → Tool, Action → Profession
5. Form Skills: Action + Object + Tool = Skill
6. Form Tasks: Action + Object + Context = Task Template
7. Form Workflows: Sequential Tasks = Workflow

---

## Version History

**v1.0** (2025-11-19)
- Initial release
- Mirrors Objects_Library_Extraction_Prompt.md structure
- Phase-based extraction methodology (Phases 1-3)
- Comprehensive cross-referencing (Actions → Objects, Tools, Professions, Workflows, Skills)
- Quality assurance checklists (Completeness, Accuracy, Cross-Reference, JSON validation)
- ID assignment standards (ACT-### format)
- Real examples from Video_001
- Integration with 429-action Actions_Master.json library
- Gap analysis methodology (✅ EXISTS, ✅ CHECK, ❌ MISSING)
- Template-driven entry creation
- Related documentation references

---

**END OF PROMPT**
