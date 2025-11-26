# Daily Updates Entity Identification System
## Version 1.1 - Markdown Output Only + Accurate Library Paths

---

## PURPOSE

This prompt guides the systematic extraction and structuring of taxonomy entities from daily work logs following a hierarchical methodology:

**Actions → Objects → Responsibilities → Tools → Skills → Tasks → Milestones**

The output integrates with the existing LIBRARIES taxonomy (429 Actions, 193 Responsibilities, 200+ Tools, 28 Skills) and generates structured outputs for entity management, analytics, and workflow automation.

**Key Feature**: Includes **Gap Analysis** to identify missing entities and enhancement opportunities for existing library entries.

---

## CORE METHODOLOGY

### 7-Step Processing Pipeline with Gap Analysis

1. **Action Word Tagging** - Extract verbs, match to 429 actions library, categorize into 7 types (A-G), **identify missing actions**
2. **Object Probability Marking** - Identify likely objects using 209 phrase patterns with probability scores, **check object library gaps**
3. **Responsibility Formation** - Combine action+object pairs, match to 193 existing responsibilities, **mark new ones**
4. **Tool Identification** - Extract mentioned tools from 200+ catalog, **flag tools not in catalog**
5. **Skill Recognition** - Apply formula: Responsibility + Tool = Skill, **identify new skills**
6. **Task Clustering** - Group related responsibilities into ACTION+OBJECT+CONTEXT format
7. **Milestone Formation** - Cluster related tasks into deliverable sequences

### Skills Formation Formula

```
Skill = Responsibility + Tool

Example:
- Responsibility: "record screen share"
- Tool: "OCam"
- Skill: "screen recording with OCam"
```

### Hierarchical Structure

```
MILESTONE (MLS-###) - Deliverable cluster
├── TASK (TSK-###) - ACTION + OBJECT + CONTEXT
│   ├── STEP (STP-###) - Atomic action
│   │   ├── ACTION (ACT-###) - Verb from 429 library
│   │   ├── OBJECT (OBJ-###) - Target of action
│   │   ├── TOOL (TOL-###) - Instrument used
│   │   └── RESPONSIBILITY (RSP-###) - Action+Object pair
│   └── SKILL (SKL-###) - Responsibility + Tool
└── PROFESSION (PRF-###) - Role performing milestone
```

---

## INPUT FORMAT

### Daily Note Structure

Daily notes typically contain:
- **Time-stamped activities** (Morning/Afternoon/Evening sections)
- **"What I worked on"** - High-level description
- **Whisper Flow Transcripts** - Detailed bilingual (Russian/Ukrainian + English) conversation logs
- **Outcomes** - Results and deliverables
- **Notes** - Follow-up items and observations

### Example Input Pattern

```markdown
### [09:00 - 11:00] - [Activity Name]
**What I worked on:**
- Creating lessons in the Online Academy platform
- Using AI to generate HTML/CSS code for course content
- Working with flip cards and animations

**Whisper Flow Transcript:**
[Bilingual transcript with detailed workflow description]

**Outcomes:**
- Created lesson structure in Lesson Library
- Generated code using AI for interactive elements
- Successfully deployed content to platform
```

---

## OUTPUT FORMAT

**REQUIRED FORMAT: Markdown (.md) ONLY**

❌ **DO NOT** output CSV files, JSON, or plain text
✅ **REQUIRED**: Complete structured markdown document with 17 sections below

Generate a comprehensive markdown report with the following sections:

---

## SECTION 1: METADATA

```markdown
## METADATA

**DAILY_NOTE_ID**: daily_[employee_number]_[LastName]_[FirstName]
**PERSON**: [Full Name]
**DEPARTMENT**: [Primary Department ISO Code]
**DATE**: [YYYY-MM-DD format]
**SOURCE_FILE**: [Full file path]
**EXTRACTION_DATE**: [YYYY-MM-DD HH:MM:SS]
**EXTRACTOR_VERSION**: Daily_Updates_v1.1
**PROCESSING_STATUS**: [Complete/Partial/In Progress]
```

---

## SECTION 2: EXECUTIVE SUMMARY

Provide 3-5 bullet points summarizing:
- Main milestones accomplished
- Key skills demonstrated
- Tools utilized
- Department contributions
- **Gap Analysis Highlights** (new entities identified)

**Example:**
```markdown
## EXECUTIVE SUMMARY

- **Milestone Achieved**: Completed Online Academy content development pipeline including AI-assisted code generation, lesson structuring, and platform deployment
- **Skills Demonstrated**: Lesson creation with Online Academy (SKL-015), AI-assisted HTML/CSS code generation with ChatGPT (SKL-023), GitHub repository management (SKL-031)
- **Tools Utilized**: Online Academy platform (TOL-030), ChatGPT (TOL-008), VS Code (TOL-019), GitHub (TOL-025), Live Server plugin (TOL-042)
- **Department Impact**: Design (DGN) - Created reusable educational content templates; Development (DEV) - Documented AI code generation workflows
- **Entity Extraction**: 3 Milestones, 8 Tasks, 24 Steps, 15 unique Actions, 18 Objects, 12 Responsibilities, 8 Tools, 6 Skills identified
- **Gap Analysis**: 4 new Responsibilities, 2 new Tools, 3 new Skills, 10 new Objects require library addition
```

---

## SECTION 3: GAP ANALYSIS - LIBRARIES CHECK

**Purpose**: Systematically compare extracted entities against existing LIBRARIES to identify what exists (and needs enhancement) vs. what is missing (and needs creation).

### Library Locations to Check

**ACTUAL CURRENT STRUCTURE** (Updated 2025-11-19):

```
ENTITIES/LIBRARIES/
├── Responsibilities/
│   ├── Core/
│   │   ├── responsibilities_master.json (193 responsibilities)
│   │   ├── phrase_matching_index.json (209 action+object patterns)
│   │   ├── action_variants_map.json (57 action synonyms)
│   │   └── object_variants_map.json (169 object variants)
│   ├── Actions/
│   │   ├── Actions_Master.json (429 actions)
│   │   ├── Actions_Master_Command_Verbs.json
│   │   ├── Actions_Master_Process_Verbs.json
│   │   ├── Actions_Master_Result_Verbs.json
│   │   ├── Video_Generation_Actions.json
│   │   └── Data_Operations/ (11 specialized action files)
│   ├── Objects/
│   │   ├── object_types.json
│   │   ├── Design_Deliverables.json
│   │   ├── Documents.json
│   │   ├── Video_Deliverables.json
│   │   └── [10 other domain-specific object files]
│   └── Parameters/
│       ├── parameters.json (7,321+ mappings)
│       ├── organized_by_profession/
│       └── organized_by_department/
├── Tools/
│   ├── AI_Tools/ (15+ tools including Claude, ChatGPT, Midjourney, etc.)
│   ├── Development_Tools/ (Cursor, Apify, etc.)
│   ├── Data_Tools/ (Anymailfinder, Bright_Data, etc.)
│   ├── Business_Tools/ (Apollo_io, LinkedIn_Sales_Navigator, etc.)
│   ├── Automation_Tools/ (Vayne, AmpleLeads, etc.)
│   ├── Integration_Tools/ (MCP connectors, etc.)
│   └── [70+ individual tool JSON files - NO master catalog]
├── Professions/
│   ├── professions.json (master list with department mapping)
│   └── [18 individual profession JSON files]
├── DEPARTMENTS/
│   ├── departments.json
│   └── By_Department/ (AI/, SMM/, etc.)
└── Archive/
    └── Legacy_Root_Files/ (archived old versions)
```

**IMPORTANT NOTES**:
- **Actions**: Located in `Responsibilities/Actions/`, NOT at root
- **Objects**: Located in `Responsibilities/Objects/`, NOT at root
- **Tools**: NO master catalog file - organized by category in individual folders
- **Skills**: Location TBD (not found in current structure - verify before using)
- **Responsibilities Core**: All core files in `Responsibilities/Core/` subdirectory

### Format

```markdown
## GAP ANALYSIS - LIBRARIES CHECK

### ACTIONS GAP ANALYSIS (429 existing)

**✅ EXISTS (Matched from Responsibilities/Actions/Actions_Master.json)**:

- **ACT-044: create** ✓
  - Process form: "creating"
  - Result form: "created"
  - Category: A (Creation)
  - Mentions: 12 times in daily note
  - Status: Active in library
  - No changes needed

- **ACT-089: generate** ✓
  - Process form: "generating"
  - Result form: "generated"
  - Category: A (Creation)
  - Mentions: 5 times in daily note
  - Status: Active in library
  - No changes needed

- **ACT-156: edit** ✓
  - Process form: "editing"
  - Result form: "edited"
  - Category: B (Modification)
  - Mentions: 8 times in daily note
  - Status: Active in library
  - No changes needed

[Continue for all matched actions...]

---

**❌ MISSING (Not found in Responsibilities/Actions/Actions_Master.json)**:

Priority: CRITICAL
  - None identified (all actions matched to existing 429)

Priority: HIGH
  - None identified

Priority: MEDIUM
  - None identified

---

### OBJECTS GAP ANALYSIS (Check Objects library)

**Location to check**: `ENTITIES/LIBRARIES/Responsibilities/Objects/`

**✅ EXISTS (Found in Objects library - Enhancement Opportunities)**:

In Design_Deliverables.json:
  - **OBJ-XXX: presentations** ✓
    - Current types: "Client pitch", "Internal presentation"
    - **ENHANCEMENT NEEDED**: ADD new type "Educational content presentation"
    - **ENHANCEMENT NEEDED**: ADD tool "Online Academy" (TOL-030)
    - **ENHANCEMENT NEEDED**: UPDATE use case "Academy lesson presentation blocks"
    - Priority: Medium
    - Suggested file: Design_Deliverables.json

[Check other existing objects...]

---

**CHECK IF EXISTS (Verify in library)**:

  - **lesson structure** → VERIFY in Design_Deliverables.json or Documents.json
    - If exists: ADD new tools (Online Academy, ChatGPT)
    - If exists: ADD new workflows (AI-assisted lesson creation)
    - If exists: UPDATE professions (Instructional Designer)
    - If NOT exists: CREATE as NEW object (see MISSING section)

  - **interactive elements** → VERIFY in Design_Deliverables.json
    - If exists: ADD new types (flip cards, hover animations, keyboard combinations)
    - If exists: ADD tools (ChatGPT for code generation)
    - If NOT exists: CREATE as NEW object (see MISSING section)

[Continue for uncertain objects...]

---

**❌ MISSING (Create new entries)**

Priority: CRITICAL
  - **lesson structure** (if not found in library)
    - Category: Design Deliverables or Documents
    - Types: "Educational content framework", "Online Academy lesson", "Course structure"
    - Tools: TOL-030 (Online Academy), TOL-008 (ChatGPT)
    - Professions: Instructional Designer (PRF-008), Content Creator
    - Time estimate: 30-60 minutes
    - Complexity: Low to Medium
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json
    - **CREATE FULL ENTRY** (use template from Objects_Library_Extraction_Prompt.md)

Priority: HIGH
  - **interactive elements** (if not found in library)
    - Category: Design Deliverables
    - Types: "Flip cards", "Hover animations", "Keyboard combinations", "Toggle elements"
    - Tools: TOL-008 (ChatGPT - code generation), TOL-019 (VS Code - editing), TOL-030 (Online Academy - deployment)
    - Professions: Instructional Designer (PRF-008), Web Developer (PRF-015)
    - Time estimate: 15-45 minutes per element
    - Complexity: Medium
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json

  - **redesigned covers** (if not found)
    - Category: Design Deliverables
    - Types: "Course cover", "1280x720 cover", "Educational content thumbnail"
    - Tools: Design software (implied), Google Drive (TOL-XXX - storage)
    - Professions: Graphic Designer (PRF-XXX)
    - Dimensions: "1280x720px"
    - Time estimate: 1-2 hours per cover
    - Complexity: Medium
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json

  - **catalog documentation** (if not found)
    - Category: Documents
    - Types: "Icon catalog", "Design documentation", "Asset catalog"
    - Tools: TOL-025 (GitHub - icon library), TOL-XXX (Dropbox), TOL-XXX (Catalog system)
    - Professions: Documentation Specialist (PRF-XXX), Graphic Designer (PRF-XXX)
    - Time estimate: Variable (depends on catalog size)
    - Complexity: Medium
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Objects/Documents.json

Priority: MEDIUM
  - **screen share recordings** (if not found)
    - Category: Media
    - Types: "Knowledge transfer recording", "Training session recording", "Masterclass recording"
    - Tools: TOL-051 (OCam), TOL-018 (Loom), TOL-XXX (Discord)
    - Professions: Videographer (PRF-XXX), Trainer (PRF-XXX)
    - Duration: Variable (minutes to hours)
    - Format: MP4, MOV
    - Complexity: Low
    - Suggested file: ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables.json

[Continue for all missing objects identified...]

---

### RESPONSIBILITIES GAP ANALYSIS (193 existing in phrase_matching_index.json)

**✅ EXISTS (Matched from phrase_matching_index.json)**:

- **RSP-089: create lesson structure** ✓
  - Action: ACT-044 (create)
  - Object: lesson structure
  - Definition: Form educational content framework
  - Department: DGN
  - Source: phrase_matching_index.json
  - Status: Active
  - Mentions: 6 times in daily note
  - No changes needed

- **RSP-156: edit HTML/CSS code** ✓
  - Action: ACT-156 (edit)
  - Object: HTML/CSS code
  - Definition: Modify web styling and structure code
  - Department: DEV
  - Source: phrase_matching_index.json
  - Status: Active
  - Mentions: 8 times in daily note
  - No changes needed

[Continue for all matched responsibilities...]

---

**❌ MISSING (Not found in phrase_matching_index.json - Create new)**

Priority: CRITICAL
  - **RSP-NEW-001: generate interactive elements**
    - Action: ACT-089 (generate)
    - Object: OBJ-067 (interactive elements)
    - Definition: Create user-interactive components for web content
    - Evidence: "Successfully generated code using AI for interactive elements (flip cards, animations)"
    - Department: DGN
    - Tools: TOL-008 (ChatGPT)
    - Skills formed: SKL-NEW-XXX (AI-assisted interactive element generation)
    - Suggested path: LIBRARIES/Responsibilities/Design/interactive_element_generation.json
    - **ADD TO PHRASE MATCHING INDEX**: "generate interactive elements" → RSP-NEW-001

Priority: HIGH
  - **RSP-NEW-002: translate lesson content**
    - Action: ACT-378 (translate)
    - Object: OBJ-201 (lesson content)
    - Definition: Convert educational material between languages
    - Evidence: "Translating lesson content to English using AI"
    - Department: DGN
    - Tools: TOL-008 (ChatGPT)
    - Skills formed: SKL-NEW-001 (AI-assisted content translation)
    - Suggested path: LIBRARIES/Responsibilities/Design/content_translation.json
    - **ADD TO PHRASE MATCHING INDEX**: "translate lesson content" → RSP-NEW-002

  - **RSP-NEW-003: upload redesigned covers**
    - Action: ACT-201 (upload)
    - Object: OBJ-234 (redesigned covers)
    - Definition: Deploy updated visual assets to platform
    - Evidence: "Successfully uploaded all redesigned course covers (1280x720 format)"
    - Department: DGN
    - Tools: TOL-030 (Online Academy)
    - Skills formed: SKL-XXX (platform content deployment)
    - Suggested path: LIBRARIES/Responsibilities/Design/asset_deployment.json
    - **ADD TO PHRASE MATCHING INDEX**: "upload redesigned covers" → RSP-NEW-003

Priority: MEDIUM
  - **RSP-NEW-004: identify missing icons**
    - Action: ACT-412 (identify)
    - Object: OBJ-XXX (missing icons)
    - Definition: Recognize absent visual assets in documentation
    - Evidence: "Identify all missing icons (mark locations where icons should be)"
    - Department: DGN
    - Tools: TOL-XXX (Catalog system), TOL-025 (GitHub)
    - Skills formed: SKL-XXX (documentation quality control)
    - Suggested path: LIBRARIES/Responsibilities/Design/asset_identification.json
    - **ADD TO PHRASE MATCHING INDEX**: "identify missing icons" → RSP-NEW-004

[Continue for all new responsibilities...]

---

### TOOLS GAP ANALYSIS (200+ existing in tools_master_catalog.json, 21 categories)

**✅ EXISTS (Matched from tools_master_catalog.json)**:

- **TOL-030: Online Academy** ✓
  - Category: Learning Management Systems
  - Description: Platform for creating and delivering educational content
  - Mentions: 8 times in daily note
  - Context: "Creating lessons in the Online Academy platform", "Full HTML content type", "Lesson Library"
  - Status: Active in catalog
  - **ENHANCEMENT**: Consider adding "Game Academy" as variant/instance

- **TOL-008: ChatGPT** ✓
  - Category: AI Assistants
  - Description: Conversational AI for code generation and content creation
  - Mentions: 12 times in daily note
  - Context: "Using AI to generate HTML/CSS code", "Translating content with AI"
  - Status: Active in catalog
  - No changes needed

- **TOL-019: VS Code** ✓
  - Category: Code Editors
  - Description: Visual Studio Code - integrated development environment
  - Mentions: 3 times in daily note
  - Context: "Editing code in VS Code", "Review code structure"
  - Status: Active in catalog
  - No changes needed

- **TOL-025: GitHub** ✓
  - Category: Version Control
  - Description: Git-based repository hosting and collaboration platform
  - Mentions: 15 times in daily note
  - Context: "GitHub repository setup", "Creating repositories", "Editing files"
  - Status: Active in catalog
  - No changes needed

- **TOL-042: Live Server** ✓
  - Category: Development Tools
  - Description: VS Code plugin for live HTML preview
  - Mentions: 2 times in daily note
  - Context: "Setting up Live Server plugin for HTML preview"
  - Status: Active in catalog
  - No changes needed

- **TOL-018: Loom** ✓
  - Category: Screen Recording
  - Description: Video messaging and screen recording tool
  - Mentions: 4 times in daily note
  - Context: "Recording tutorials in Loom"
  - Status: Active in catalog
  - No changes needed

- **TOL-051: OCam** ✓
  - Category: Screen Recording
  - Description: Screen capture and recording software
  - Mentions: 2 times in daily note
  - Context: "Recorded screen share using OCam"
  - Status: Active in catalog
  - No changes needed

[Continue for all matched tools...]

---

**❌ MISSING (Not found in tools_master_catalog.json - Create new)**

Priority: HIGH
  - **TOL-NEW-001: Time Tracker**
    - Category: Productivity Tools
    - Description: Platform for tracking work hours and submitting reports
    - Mentions: 6 times in daily note
    - Context: "Time tracker technical issues", "Timer wouldn't stop", "Couldn't submit reports"
    - Evidence: Mentioned as critical blocker affecting all employees
    - Department: ALL (used across all departments)
    - Use cases: Work hour tracking, Report submission, Productivity monitoring
    - Related tools: None identified
    - Suggested catalog path: LIBRARIES/Tools/Productivity/time_tracking_platforms.json
    - **CREATE FULL ENTRY** with fields: tool_id, name, category, description, use_cases, departments, integrations, features, pricing_model

  - **TOL-NEW-002: Whisper Flow**
    - Category: Transcription Tools
    - Description: Audio transcription and meeting documentation tool
    - Mentions: Throughout daily note structure (embedded in format)
    - Context: "Whisper Flow transcripts from all meetings/calls", "Whisper Flow ON during all activities"
    - Evidence: Core tool for daily documentation workflow
    - Department: ALL (documentation standard)
    - Use cases: Meeting transcription, Daily note capture, Conversation logging
    - Output format: Bilingual transcripts (Russian/Ukrainian + English)
    - Suggested catalog path: LIBRARIES/Tools/Productivity/transcription_tools.json
    - **CREATE FULL ENTRY** with transcription accuracy, language support, integration capabilities

Priority: MEDIUM
  - **TOL-NEW-003: Discord** (if not cataloged)
    - Category: Communication Tools
    - Description: Team communication and screen sharing platform
    - Mentions: 3 times
    - Context: "Join Discord screen share session", "Staying in Discord window during recording"
    - Use cases: Screen sharing, Video calls, Team communication, Knowledge transfer sessions
    - Department: ALL
    - Suggested catalog path: LIBRARIES/Tools/Communication/team_collaboration.json

  - **TOL-NEW-004: Google Drive** (if not cataloged)
    - Category: Cloud Storage
    - Description: Cloud storage and file sharing service
    - Mentions: 4 times
    - Context: "Upload to Google Drive folder", "Secured all tutorial videos in Google Drive"
    - Use cases: Video storage, Asset sharing, Collaborative file management
    - Department: ALL
    - Suggested catalog path: LIBRARIES/Tools/Productivity/cloud_storage.json

[Continue for all missing tools...]

---

### SKILLS GAP ANALYSIS (28 existing in skills_master.json)

**✅ EXISTS (Matched from skills_master.json)**:

- **SKL-015: lesson creation with Online Academy** ✓
  - Responsibility: RSP-089 (create lesson structure)
  - Tool: TOL-030 (Online Academy)
  - Definition: Create educational content using LMS platform
  - Evidence: "Creating lessons in the Online Academy platform", "Created lesson structure in Lesson Library"
  - Department: DGN
  - Proficiency level: Intermediate (based on successful deployment)
  - Status: Active in library
  - No changes needed

- **SKL-023: AI-assisted HTML/CSS code generation with ChatGPT** ✓
  - Responsibility: RSP-156 (edit HTML/CSS code) + RSP-NEW-001 (generate interactive elements)
  - Tool: TOL-008 (ChatGPT)
  - Definition: Use conversational AI to create and modify web code
  - Evidence: "Using AI to generate and modify HTML/CSS code for course content"
  - Department: DGN, DEV
  - Proficiency level: Intermediate (iterative refinement capability)
  - Status: Active in library
  - No changes needed

- **SKL-031: GitHub repository management** ✓
  - Responsibility: RSP-187 (organize repositories) + RSP-044 (create repository)
  - Tool: TOL-025 (GitHub)
  - Definition: Manage version control repositories including creation, editing, and deletion
  - Evidence: "GitHub repository creation and management"
  - Department: DEV
  - Proficiency level: Beginner (learning phase)
  - Status: Active in library
  - No changes needed

[Continue for all matched skills...]

---

**❌ MISSING (Not found in skills_master.json - Create new using formula)**

Priority: CRITICAL
  - **SKL-NEW-001: AI-assisted content translation**
    - Formula: RSP-NEW-002 (translate lesson content) + TOL-008 (ChatGPT) = Skill
    - Definition: Use AI to convert educational content between languages
    - Evidence: "Translating lesson content to English using AI"
    - Department: DGN
    - Proficiency level: Beginner
    - Required responsibilities: RSP-NEW-002 (translate lesson content)
    - Required tools: TOL-008 (ChatGPT)
    - Time to proficiency: 2-4 weeks (basic), 2-3 months (advanced)
    - Use cases: Course localization, Multilingual content creation, Documentation translation
    - Related skills: SKL-023 (AI-assisted code generation), SKL-XXX (content writing)
    - Suggested library path: LIBRARIES/Skills/Design/ai_translation.json
    - **CREATE FULL ENTRY** following skills_master.json format

Priority: HIGH
  - **SKL-NEW-002: screen recording with OCam**
    - Formula: RSP-089 (record screen share) + TOL-051 (OCam) = Skill
    - Definition: Capture screen activity using OCam software
    - Evidence: "I recorded her shared screen using OCam", "Recorded screen share via OCam"
    - Department: VID
    - Proficiency level: Intermediate
    - Required responsibilities: RSP-089 (record screen share)
    - Required tools: TOL-051 (OCam)
    - Time to proficiency: 1-2 weeks (basic), 1-2 months (advanced)
    - Use cases: Knowledge transfer recording, Tutorial creation, Bug documentation
    - Related skills: SKL-NEW-003 (video tutorial creation with Loom)
    - Suggested library path: LIBRARIES/Skills/Video/screen_capture.json

  - **SKL-NEW-003: video tutorial creation with Loom**
    - Formula: RSP-044 (create video tutorials) + TOL-018 (Loom) = Skill
    - Definition: Produce instructional video content using Loom platform
    - Evidence: "She recorded video instructions for us... recording them in Loom"
    - Department: VID
    - Proficiency level: Advanced
    - Required responsibilities: RSP-044 (create video tutorials), RSP-092 (document processes)
    - Required tools: TOL-018 (Loom)
    - Time to proficiency: 2-3 weeks (basic), 2-4 months (advanced)
    - Use cases: Team training, Process documentation, Client onboarding
    - Related skills: SKL-NEW-002 (screen recording with OCam)
    - Suggested library path: LIBRARIES/Skills/Video/tutorial_production.json

Priority: MEDIUM
  - **SKL-NEW-004: platform content deployment**
    - Formula: RSP-NEW-003 (upload redesigned covers) + TOL-030 (Online Academy) = Skill
    - Definition: Deploy visual and content assets to online platforms
    - Evidence: "Successfully uploaded all redesigned course covers (1280x720 format) to Game Academy platform"
    - Department: DGN
    - Proficiency level: Intermediate
    - Required responsibilities: RSP-NEW-003 (upload redesigned covers), RSP-201 (deploy content)
    - Required tools: TOL-030 (Online Academy), TOL-XXX (Google Drive)
    - Time to proficiency: 1-2 weeks (basic), 1-2 months (advanced with optimization)
    - Use cases: Course cover deployment, Content publishing, Asset updates
    - Related skills: SKL-015 (lesson creation with Online Academy)
    - Suggested library path: LIBRARIES/Skills/Design/platform_deployment.json

[Continue for all new skills identified...]

---

### PROFESSIONS GAP ANALYSIS (Check professions_master.json)

**✅ EXISTS (Matched from professions_master.json)**:

- **PRF-008: Instructional Designer** ✓
  - Definition: Professional who designs, develops, and delivers educational content
  - Skills demonstrated: SKL-015 (lesson creation), SKL-023 (AI code generation), SKL-NEW-001 (AI translation)
  - Responsibilities: RSP-089 (create lesson structure), RSP-NEW-001 (generate interactive elements), RSP-156 (edit HTML/CSS)
  - Tools used: TOL-030 (Online Academy), TOL-008 (ChatGPT), TOL-019 (VS Code)
  - Employee match: Kucherenko, Iuliia
  - Department: DGN
  - Status: Active
  - No changes needed

- **PRF-015: Web Developer** ✓
  - Definition: Professional who creates and maintains websites and web applications
  - Skills demonstrated: SKL-031 (GitHub management), SKL-023 (AI code generation)
  - Responsibilities: RSP-044 (create repository), RSP-187 (organize repositories), RSP-156 (edit code)
  - Tools used: TOL-025 (GitHub), TOL-042 (Live Server), TOL-019 (VS Code)
  - Employee match: Kucherenko, Iuliia (secondary role)
  - Department: DEV
  - Status: Active
  - No changes needed

[Continue for matched professions...]

---

**❌ MISSING (Not found in professions_master.json - Create new)**

Priority: HIGH
  - **PRF-NEW-001: Videographer** (if not in library)
    - Definition: Professional who captures, records, and produces video content
    - Skills required: SKL-NEW-002 (screen recording with OCam), SKL-NEW-003 (video tutorial creation with Loom)
    - Responsibilities: RSP-089 (record screen share), RSP-092 (document content), RSP-187 (organize videos)
    - Tools used: TOL-051 (OCam), TOL-018 (Loom), TOL-XXX (Discord), TOL-XXX (Google Drive)
    - Employee match: Skrypkar, Vilhelm
    - Department: VID
    - Suggested library path: LIBRARIES/Professions/professions_master.json
    - **CREATE FULL ENTRY** with required skills, typical responsibilities, tools, career path

  - **PRF-NEW-002: Documentation Specialist** (if not in library)
    - Definition: Professional who creates, maintains, and improves documentation quality
    - Skills required: SKL-XXX (documentation quality control), SKL-XXX (icon library management)
    - Responsibilities: RSP-298 (review documentation), RSP-412 (identify missing icons), RSP-089 (create asset lists)
    - Tools used: TOL-XXX (Catalog system), TOL-025 (GitHub), TOL-XXX (Dropbox)
    - Employee match: Kucherenko, Iuliia (task-based)
    - Department: DGN, ALL
    - Suggested library path: LIBRARIES/Professions/professions_master.json

[Continue for all missing professions...]

---

### GAP ANALYSIS SUMMARY

**ENTITIES TO ADD TO LIBRARIES**:

| Entity Type | Existing (Matched) | Missing (New) | Enhancement Needed | Total |
|------------|-------------------|--------------|-------------------|-------|
| Actions (ACT) | 14 | 0 | 0 | 14 |
| Objects (OBJ) | 0-2 (verify) | 8-10 (create) | 1-2 (enhance) | 10 |
| Responsibilities (RSP) | 7 | 4-6 | 0 | 11-13 |
| Tools (TOL) | 7 | 2-4 | 1 (enhance) | 9-11 |
| Skills (SKL) | 3 | 3-4 | 0 | 6-7 |
| Professions (PRF) | 2 | 0-2 (verify) | 0 | 2-4 |
| **TOTAL** | **33-35** | **17-26** | **2-3** | **52-60** |

**PRIORITY ACTIONS**:
1. **CRITICAL**: Create 4-6 new Responsibilities + add to phrase_matching_index.json
2. **HIGH**: Create 8-10 new Objects + add to appropriate category files
3. **HIGH**: Create 2-4 new Tools + add to tools_master_catalog.json
4. **HIGH**: Create 3-4 new Skills + add to skills_master.json
5. **MEDIUM**: Enhance 1-2 existing Objects with new tools/types/workflows
6. **MEDIUM**: Verify and create 0-2 Professions if missing from library

**FILES TO UPDATE**:
- `LIBRARIES/Responsibilities/Actions/Actions_Master.json` - No updates needed (all actions matched)
- `LIBRARIES/Responsibilities/Core/phrase_matching_index.json` - ADD 4-6 new action+object patterns
- `LIBRARIES/Responsibilities/Core/responsibilities_master.json` - ADD 4-6 new responsibility definitions
- `LIBRARIES/Responsibilities/Objects/Design_Deliverables.json` - ADD 5-7 new objects + ENHANCE 1-2 existing
- `LIBRARIES/Responsibilities/Objects/Documents.json` - ADD 1-2 new objects
- `LIBRARIES/Responsibilities/Objects/Video_Deliverables.json` - ADD 1-2 new objects
- `LIBRARIES/Tools/[Category_Folder]/[Tool_Name].json` - ADD 2-4 new tools (NO master catalog - add to appropriate category folder)
- `LIBRARIES/Skills/skills_master.json` - ADD 3-4 new skills
- `LIBRARIES/Professions/professions_master.json` - VERIFY + ADD 0-2 professions if missing
```

---

## SECTION 4: ACTION VERB CATEGORIZATION

Categorize all extracted action verbs into 7 categories (A-G):

### A. CREATION VERBS
Actions that bring new entities into existence.

**Pattern**: Subject + CREATION_VERB + New_Object

**Examples from Actions Library**:
- create, generate, design, build, develop, draft, produce, compose, construct, establish, formulate, invent, make, model, originate, prepare, render, write

**Extracted from Daily Note**:
```markdown
- ACT-044: create (used 12 times) ✅ MATCHED
  - create lesson structure
  - create repository
  - create video tutorials

- ACT-089: generate (used 5 times) ✅ MATCHED
  - generate HTML/CSS code
  - generate interactive elements
```

### B. MODIFICATION VERBS
Actions that change existing entities.

**Pattern**: Subject + MODIFICATION_VERB + Existing_Object + (to improve/change aspect)

**Examples from Actions Library**:
- edit, refine, optimize, enhance, update, revise, modify, adjust, improve, customize, adapt, correct, fix, polish, streamline, tailor, transform, upgrade

**Extracted from Daily Note**:
```markdown
- ACT-156: edit (used 8 times) ✅ MATCHED
  - edit files in GitHub
  - edit HTML/CSS code

- ACT-401: update (used 4 times) ✅ MATCHED
  - update repositories
  - update catalog documentation
```

### C. ANALYSIS VERBS
Actions that examine or investigate.

**Pattern**: Subject + ANALYSIS_VERB + Object + (to understand/evaluate aspect)

**Examples from Actions Library**:
- analyze, review, evaluate, research, assess, examine, investigate, study, explore, inspect, audit, benchmark, compare, diagnose, measure, test, validate, verify

**Extracted from Daily Note**:
```markdown
- ACT-298: review (used 6 times) ✅ MATCHED
  - review catalog documentation
  - review lesson content

- ACT-412: identify (used 3 times) ✅ MATCHED
  - identify missing icons
  - identify duplicate entries
```

### D. ORGANIZATION VERBS
Actions that structure or arrange.

**Pattern**: Subject + ORGANIZATION_VERB + Object + (by/according to criteria)

**Examples from Actions Library**:
- organize, structure, plan, coordinate, prioritize, arrange, categorize, classify, group, order, schedule, sequence, sort, standardize, systematize

**Extracted from Daily Note**:
```markdown
- ACT-187: organize (used 2 times) ✅ MATCHED
  - organize file locations
  - organize repositories

- ACT-265: plan (used 1 time) ✅ MATCHED
  - plan video tutorial series
```

### E. COMMUNICATION VERBS
Actions that share or transfer information.

**Pattern**: Subject + COMMUNICATION_VERB + Information + (to recipient/via channel)

**Examples from Actions Library**:
- present, share, publish, export, report, deliver, communicate, demonstrate, discuss, document, explain, inform, notify, submit, teach, translate

**Extracted from Daily Note**:
```markdown
- ACT-378: translate (used 4 times) ✅ MATCHED
  - translate lesson content to English
  - translate using AI

- ACT-092: document (used 3 times) ✅ MATCHED
  - document prompt templates
  - document file organization
```

### F. AGENTIC/AUTOMATION VERBS
Actions performed by systems or automated processes.

**Pattern**: System + AGENTIC_VERB + Process + (with parameters)

**Examples from Actions Library**:
- automate, execute, control, migrate, interact, process, run, trigger, deploy, integrate, synchronize, batch, schedule

**Extracted from Daily Note**:
```markdown
- ACT-123: deploy (used 2 times) ✅ MATCHED
  - deploy covers to platform
  - deploy content to Full HTML block

- ACT-201: upload (used 5 times) ✅ MATCHED
  - upload files to repositories
  - upload redesigned covers
```

### G. DATA OPERATIONS
Actions that manipulate or transform data.

**Pattern**: Subject + DATA_VERB + Dataset + (from source to target)

**Examples from Actions Library**:
- scrape, parse, extract, enrich, validate, transform, clean, merge, filter, aggregate, deduplicate, normalize, format, import, export

**Extracted from Daily Note**:
```markdown
- ACT-167: extract (used 1 time) ✅ MATCHED
  - extract action-object pairs

- ACT-289: insert (used 2 times) ✅ MATCHED
  - insert icons into locations
  - insert links to spreadsheet
```

---

## SECTION 5: OBJECT PROBABILITY MARKING

For each action verb identified, mark the probability of associated objects using the 209 phrase patterns from the phrase matching index.

### Probability Scoring System

- **HIGH (0.8-1.0)**: Object directly follows action in text, matches known phrase pattern
- **MEDIUM (0.5-0.79)**: Object appears in same sentence, contextually related to action
- **LOW (0.2-0.49)**: Object appears in same paragraph, possibly related to action
- **MINIMAL (0.0-0.19)**: Object mentioned but relationship unclear

### Format

```markdown
## OBJECT PROBABILITY MARKING

### ACT-044: create

**High Probability Objects (0.8-1.0)**:
- OBJ-103: lesson structure (0.95) ✅ MATCHED to phrase_matching_index
  - Pattern: "create lesson structure" (direct match)
  - Evidence: "Create lesson structure in Lesson Library"

- OBJ-087: repository (0.92) ✅ MATCHED to phrase_matching_index
  - Pattern: "create repository" (direct match)
  - Evidence: "Creating new repositories and deleting test repositories"

- OBJ-156: video tutorials (0.88) ❌ NEW OBJECT
  - Pattern: "create video tutorials" (phrase found, object not in library)
  - Evidence: "Need to create video tutorials for AI-assisted design work"
  - **GAP**: Object missing from library - requires creation

**Medium Probability Objects (0.5-0.79)**:
- OBJ-201: documentation (0.68) ✅ CHECK IF EXISTS
  - Context: "create... for documenting prompt templates"
  - Evidence: "Should document prompt templates and variations"
  - **GAP**: Verify if "documentation" exists in Objects/Documents.json

**Low Probability Objects (0.2-0.49)**:
- OBJ-178: module (0.35)
  - Mentioned in context but not direct object of "create"

---

### ACT-089: generate

**High Probability Objects (0.8-1.0)**:
- OBJ-045: HTML/CSS code (0.98) ✅ MATCHED to phrase_matching_index
  - Pattern: "generate HTML/CSS code" (direct match)
  - Evidence: "Using AI to generate and modify HTML/CSS code for course content"

- OBJ-067: interactive elements (0.91) ❌ NEW OBJECT
  - Pattern: "generate interactive elements" (phrase found, object not in library)
  - Evidence: "Successfully generated code using AI for interactive elements (flip cards, animations)"
  - **GAP**: Object missing from library - requires creation

- OBJ-123: code (0.85) ✅ MATCHED
  - Pattern: "generate code" (direct match)
  - Evidence: "Generate code using ChatGPT with specific prompts"
```

---

## SECTION 6: RESPONSIBILITY FORMATION

Combine action+object pairs to form responsibilities. Match against the 193 existing responsibilities in the phrase matching index.

### Format

```markdown
## RESPONSIBILITY FORMATION

### Matched to Existing Responsibilities (phrase_matching_index.json)

**RSP-089: create lesson structure** ✅ MATCHED
- **Action**: ACT-044 (create)
- **Object**: OBJ-103 (lesson structure)
- **Definition**: Form educational content framework
- **Source**: phrase_matching_index.json (existing)
- **Department**: DGN
- **Status**: Active
- **Evidence**: "Create lesson structure in Lesson Library"

**RSP-156: edit HTML/CSS code** ✅ MATCHED
- **Action**: ACT-156 (edit)
- **Object**: OBJ-045 (HTML/CSS code)
- **Definition**: Modify web styling and structure code
- **Source**: phrase_matching_index.json (existing)
- **Department**: DEV
- **Status**: Active
- **Evidence**: "Editing code in VS Code"

---

### New Responsibilities Identified (NOT in phrase_matching_index.json)

**RSP-NEW-001: generate interactive elements** ❌ NEW - CRITICAL PRIORITY
- **Action**: ACT-089 (generate)
- **Object**: OBJ-067 (interactive elements) - Also NEW
- **Definition**: Create user-interactive components for web content
- **Evidence**: "Successfully generated code using AI for interactive elements (flip cards, animations)"
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: DGN
- **Status**: Pending Addition to Library
- **Suggested Library Path**: LIBRARIES/Responsibilities/Design/interactive_element_generation.json
- **Add to phrase_matching_index**: "generate interactive elements" → RSP-NEW-001
- **Tools Used**: TOL-008 (ChatGPT)
- **Skills Formed**: SKL-NEW-XXX (AI-assisted interactive element generation)

**RSP-NEW-002: translate lesson content** ❌ NEW - HIGH PRIORITY
- **Action**: ACT-378 (translate)
- **Object**: OBJ-201 (lesson content) - Check if exists
- **Definition**: Convert educational material between languages
- **Evidence**: "Translating lesson content to English using AI"
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: DGN
- **Status**: Pending Addition to Library
- **Suggested Library Path**: LIBRARIES/Responsibilities/Design/content_translation.json
- **Add to phrase_matching_index**: "translate lesson content" → RSP-NEW-002
- **Tools Used**: TOL-008 (ChatGPT)
- **Skills Formed**: SKL-NEW-001 (AI-assisted content translation)

**RSP-NEW-003: upload redesigned covers** ❌ NEW - HIGH PRIORITY
- **Action**: ACT-201 (upload)
- **Object**: OBJ-234 (redesigned covers) - Also NEW
- **Definition**: Deploy updated visual assets to platform
- **Evidence**: "Successfully uploaded all redesigned course covers (1280x720 format) to Game Academy platform"
- **Source**: daily_333_Skrypkar_Vilhelm.md (new from daily note)
- **Department**: DGN
- **Status**: Pending Addition to Library
- **Suggested Library Path**: LIBRARIES/Responsibilities/Design/asset_deployment.json
- **Add to phrase_matching_index**: "upload redesigned covers" → RSP-NEW-003
- **Tools Used**: TOL-030 (Online Academy)
- **Skills Formed**: SKL-NEW-XXX (platform content deployment)

**RSP-NEW-004: identify missing icons** ❌ NEW - MEDIUM PRIORITY
- **Action**: ACT-412 (identify)
- **Object**: OBJ-XXX (missing icons) - Also NEW
- **Definition**: Recognize absent visual assets in documentation
- **Evidence**: "Identify all missing icons (mark locations where icons should be)"
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: DGN
- **Status**: Pending Addition to Library
- **Suggested Library Path**: LIBRARIES/Responsibilities/Design/asset_identification.json
- **Add to phrase_matching_index**: "identify missing icons" → RSP-NEW-004
- **Tools Used**: TOL-XXX (Catalog system), TOL-025 (GitHub)
- **Skills Formed**: SKL-XXX (documentation quality control)
```

---

## SECTION 7: TOOL IDENTIFICATION

Extract all tools mentioned in the daily note and match against the 200+ tools catalog across 21 categories.

### Format

```markdown
## TOOL IDENTIFICATION

### Matched to Existing Tools Catalog (tools_master_catalog.json)

**TOL-030: Online Academy** ✅ MATCHED
- **Category**: Learning Management Systems
- **Description**: Platform for creating and delivering educational content
- **Mentioned**: 8 times in daily note
- **Context**: "Creating lessons in the Online Academy platform", "Full HTML content type", "Lesson Library"
- **Source**: tools_master_catalog.json (existing)
- **Department**: DGN, AIA
- **Status**: Active
- **Enhancement Suggestion**: Consider adding "Game Academy" as variant/instance
- **Objects Created**: OBJ-103 (lesson structure), OBJ-XXX (lessons), OBJ-234 (course covers)

**TOL-008: ChatGPT** ✅ MATCHED
- **Category**: AI Assistants
- **Description**: Conversational AI for code generation and content creation
- **Mentioned**: 12 times in daily note
- **Context**: "Using AI to generate HTML/CSS code", "Translating content with AI", "Writing clear prompts"
- **Source**: tools_master_catalog.json (existing)
- **Department**: ALL
- **Status**: Active
- **No changes needed**
- **Objects Created**: OBJ-045 (HTML/CSS code), OBJ-067 (interactive elements), OBJ-201 (lesson content - translated)

[Continue for all matched tools: VS Code, GitHub, Live Server, Loom, OCam...]

---

### New Tools Identified (NOT in tools_master_catalog.json)

**TOL-NEW-001: Time Tracker** ❌ NEW - HIGH PRIORITY
- **Category**: Productivity Tools
- **Description**: Platform for tracking work hours and submitting reports
- **Mentioned**: 6 times in daily note
- **Context**: "Time tracker technical issues", "Timer wouldn't stop", "Couldn't submit reports"
- **Evidence**: "Discussing time tracker technical issues that occurred on Friday (timer wouldn't stop, couldn't submit reports)"
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: ALL (used across all departments)
- **Status**: Pending Addition to Catalog
- **Suggested Catalog Path**: LIBRARIES/Tools/Productivity/time_tracking_platforms.json
- **Use Cases**: Work hour tracking, Report submission, Productivity monitoring, Timesheet management
- **Related Tools**: None identified
- **Objects Created**: OBJ-XXX (time reports), OBJ-XXX (timesheets)
- **Skills Required**: SKL-XXX (time tracking and reporting)
- **Critical Issue**: Technical blocker affecting all employees - high priority to catalog

**TOL-NEW-002: Whisper Flow** ❌ NEW - HIGH PRIORITY
- **Category**: Transcription Tools
- **Description**: Audio transcription and meeting documentation tool
- **Mentioned**: Throughout daily note structure (embedded in format)
- **Context**: "Whisper Flow transcripts from all meetings/calls", "Whisper Flow ON during all activities"
- **Evidence**: Core tool for daily documentation workflow - appears in every daily note template
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: ALL (documentation standard for all employees)
- **Status**: Pending Addition to Catalog
- **Suggested Catalog Path**: LIBRARIES/Tools/Productivity/transcription_tools.json
- **Use Cases**: Meeting transcription, Daily note capture, Conversation logging, Bilingual documentation
- **Output Format**: Bilingual transcripts (Russian/Ukrainian + English)
- **Integration**: Embedded in Daily Notes workflow
- **Objects Created**: OBJ-XXX (transcripts), OBJ-XXX (meeting notes)
- **Skills Required**: SKL-XXX (meeting transcription and documentation)

**TOL-NEW-003: Discord** ❌ NEW (if not in catalog) - MEDIUM PRIORITY
- **Category**: Communication Tools
- **Description**: Team communication and screen sharing platform
- **Mentioned**: 3 times in daily note
- **Context**: "Join Discord screen share session", "Staying in Discord window during recording"
- **Evidence**: "Since I was recording the shared screen, I couldn't do anything else during this time so as not to leave the Discord window"
- **Source**: daily_333_Skrypkar_Vilhelm.md (new from daily note)
- **Department**: ALL
- **Status**: Pending Verification / Addition to Catalog
- **Suggested Catalog Path**: LIBRARIES/Tools/Communication/team_collaboration.json
- **Use Cases**: Screen sharing, Video calls, Team communication, Knowledge transfer sessions
- **Objects Created**: OBJ-XXX (screen shares), OBJ-XXX (voice calls)
- **Skills Required**: SKL-XXX (remote communication and collaboration)

[Continue for Google Drive, Google Sheets, Catalog system, etc. if not in catalog...]
```

---

## SECTION 8: SKILL RECOGNITION

Apply the formula: **Skill = Responsibility + Tool** to identify demonstrated skills.

### Format

```markdown
## SKILL RECOGNITION

### Formula Application: Responsibility + Tool = Skill

**SKL-015: lesson creation with Online Academy** ✅ MATCHED to skills_master.json
- **Responsibility**: RSP-089 (create lesson structure)
- **Tool**: TOL-030 (Online Academy)
- **Definition**: Create educational content using LMS platform
- **Evidence from Daily Note**: "Creating lessons in the Online Academy platform", "Created lesson structure in Lesson Library", "Successfully deployed content to platform"
- **Source**: skills_master.json (existing)
- **Department**: DGN
- **Proficiency Level**: Intermediate (based on successful deployment and iterative refinement)
- **Status**: Active in Library
- **No changes needed**

**SKL-023: AI-assisted HTML/CSS code generation with ChatGPT** ✅ MATCHED to skills_master.json
- **Responsibility**: RSP-156 (edit HTML/CSS code) + RSP-NEW-001 (generate interactive elements)
- **Tool**: TOL-008 (ChatGPT)
- **Definition**: Use conversational AI to create and modify web code
- **Evidence from Daily Note**: "Using AI to generate and modify HTML/CSS code for course content", "Successfully generated code using AI for interactive elements (flip cards, animations)", "Learned to iterate on AI-generated code by providing specific design requirements"
- **Source**: skills_master.json (existing)
- **Department**: DGN, DEV
- **Proficiency Level**: Intermediate (iterative refinement capability demonstrated)
- **Status**: Active in Library
- **No changes needed**

**SKL-031: GitHub repository management** ✅ MATCHED to skills_master.json
- **Responsibility**: RSP-187 (organize repositories) + RSP-044 (create repository)
- **Tool**: TOL-025 (GitHub)
- **Definition**: Manage version control repositories including creation, editing, and deletion
- **Evidence from Daily Note**: "GitHub repository creation and management", "Learning how to edit files directly in GitHub", "Creating new repositories and deleting test repositories", "Understood the difference between repositories and projects"
- **Source**: skills_master.json (existing)
- **Department**: DEV
- **Proficiency Level**: Beginner (learning phase - explicit mention of "learning")
- **Status**: Active in Library
- **No changes needed**

---

### New Skills Identified (NOT in skills_master.json - Using Formula)

**SKL-NEW-001: AI-assisted content translation** ❌ NEW - CRITICAL PRIORITY
- **Formula**: RSP-NEW-002 (translate lesson content) + TOL-008 (ChatGPT) = Skill
- **Definition**: Use AI to convert educational content between languages while preserving meaning and context
- **Evidence from Daily Note**: "Translating lesson content to English using AI"
- **Source**: daily_228_Kucherenko_Iuliia.md (new from daily note)
- **Department**: DGN (primary), ALL (applicable across departments)
- **Proficiency Level**: Beginner (initial demonstration)
- **Required Responsibilities**: RSP-NEW-002 (translate lesson content)
- **Required Tools**: TOL-008 (ChatGPT)
- **Time to Proficiency**: 2-4 weeks (basic translation), 2-3 months (advanced with context preservation and quality control)
- **Use Cases**: Course localization, Multilingual content creation, Documentation translation, Client communication translation
- **Related Skills**: SKL-023 (AI-assisted code generation - similar AI interaction pattern), SKL-XXX (content writing), SKL-XXX (language proficiency)
- **Professions Using This Skill**: PRF-008 (Instructional Designer), PRF-XXX (Content Creator), PRF-XXX (Translator)
- **Status**: Pending Addition to Skills Library
- **Suggested Library Path**: LIBRARIES/Skills/Design/ai_translation.json
- **Best Practices**: Verify accuracy, maintain tone and voice, preserve formatting, review cultural context
- **CREATE FULL ENTRY** following skills_master.json format with learning path, proficiency indicators, common pitfalls

**SKL-NEW-002: screen recording with OCam** ❌ NEW - HIGH PRIORITY
- **Formula**: RSP-089 (record screen share) + TOL-051 (OCam) = Skill
- **Definition**: Capture screen activity using OCam software for knowledge transfer and documentation
- **Evidence from Daily Note**: "I recorded her shared screen using OCam", "Recorded screen share via OCam", "Set up OCam for backup recording"
- **Source**: daily_333_Skrypkar_Vilhelm.md (new from daily note)
- **Department**: VID (primary), DGN (secondary for self-service)
- **Proficiency Level**: Intermediate (successful backup recording strategy demonstrated)
- **Required Responsibilities**: RSP-089 (record screen share), RSP-187 (organize video files)
- **Required Tools**: TOL-051 (OCam), TOL-XXX (Discord - for screen share source)
- **Time to Proficiency**: 1-2 weeks (basic recording), 1-2 months (advanced with quality optimization and troubleshooting)
- **Use Cases**: Knowledge transfer recording, Tutorial creation, Bug documentation, Training session capture
- **Related Skills**: SKL-NEW-003 (video tutorial creation with Loom - complementary skill)
- **Professions Using This Skill**: PRF-NEW-001 (Videographer), PRF-XXX (Trainer), PRF-XXX (Support Specialist)
- **Status**: Pending Addition to Skills Library
- **Suggested Library Path**: LIBRARIES/Skills/Video/screen_capture.json
- **Best Practices**: Set correct audio source, optimize video quality settings, test recording before live session, organize output files
- **CREATE FULL ENTRY** with technical requirements, quality settings, file management

**SKL-NEW-003: video tutorial creation with Loom** ❌ NEW - HIGH PRIORITY
- **Formula**: RSP-044 (create video tutorials) + TOL-018 (Loom) = Skill
- **Definition**: Produce instructional video content using Loom platform for team training and knowledge sharing
- **Evidence from Daily Note**: "She recorded video instructions for us... recording them in Loom", "Provided Loom tutorial reference", "Based on one of the videos that Yuliia recorded for us in Loom, designers have already received an assignment to create a course"
- **Source**: daily_333_Skrypkar_Vilhelm.md (new from daily note)
- **Department**: VID (primary), DGN (secondary), ALL (training use case)
- **Proficiency Level**: Advanced (evidence of immediate actionable output - tutorials led to course assignments)
- **Required Responsibilities**: RSP-044 (create video tutorials), RSP-092 (document processes), RSP-298 (coordinate training)
- **Required Tools**: TOL-018 (Loom), TOL-XXX (Google Drive - for distribution)
- **Time to Proficiency**: 2-3 weeks (basic recording), 2-4 months (advanced with engagement optimization and structured workflows)
- **Use Cases**: Team training, Process documentation, Client onboarding, Knowledge transfer before employee departure
- **Related Skills**: SKL-NEW-002 (screen recording with OCam - complementary backup strategy)
- **Professions Using This Skill**: PRF-NEW-001 (Videographer), PRF-XXX (Trainer), PRF-008 (Instructional Designer)
- **Status**: Pending Addition to Skills Library
- **Suggested Library Path**: LIBRARIES/Skills/Video/tutorial_production.json
- **Best Practices**: Plan content structure before recording, use clear narration, include visual callouts, organize videos by topic, integrate with workflow documentation
- **CREATE FULL ENTRY** with content planning framework, narration techniques, distribution strategies

**SKL-NEW-004: platform content deployment** ❌ NEW - MEDIUM PRIORITY
- **Formula**: RSP-NEW-003 (upload redesigned covers) + TOL-030 (Online Academy) = Skill
- **Definition**: Deploy visual and content assets to online platforms with proper formatting and optimization
- **Evidence from Daily Note**: "Successfully uploaded all redesigned course covers (1280x720 format) to Game Academy platform", "New design now live with text overlay positioned on left side as planned"
- **Source**: daily_333_Skrypkar_Vilhelm.md (new from daily note)
- **Department**: DGN (primary)
- **Proficiency Level**: Intermediate (successful deployment with format specifications)
- **Required Responsibilities**: RSP-NEW-003 (upload redesigned covers), RSP-201 (deploy content), RSP-298 (verify quality)
- **Required Tools**: TOL-030 (Online Academy), TOL-XXX (Google Drive - asset source)
- **Time to Proficiency**: 1-2 weeks (basic upload), 1-2 months (advanced with optimization and quality assurance)
- **Use Cases**: Course cover deployment, Content publishing, Asset updates, Platform visual management
- **Related Skills**: SKL-015 (lesson creation with Online Academy - same platform knowledge)
- **Professions Using This Skill**: PRF-XXX (Graphic Designer), PRF-XXX (Platform Administrator), PRF-008 (Instructional Designer)
- **Status**: Pending Addition to Skills Library
- **Suggested Library Path**: LIBRARIES/Skills/Design/platform_deployment.json
- **Best Practices**: Verify dimensions before upload, check text overlay positioning, maintain backup of assets, document pending revisions
- **CREATE FULL ENTRY** with platform-specific requirements, quality checklists, rollback procedures
```

---

## SECTION 9: TASK CLUSTERING

Group related responsibilities into tasks following the **ACTION + OBJECT + CONTEXT** format.

### Format

```markdown
## TASK CLUSTERING

### TSK-001: Create Online Academy Lessons with AI

**Format**: ACTION + OBJECT + CONTEXT
- **ACTION**: Create
- **OBJECT**: Online Academy Lessons
- **CONTEXT**: with AI assistance (ChatGPT for code generation)

**Description**: Develop interactive educational content using ChatGPT to generate HTML/CSS code for flip cards, animations, and other elements, then deploy to Online Academy platform.

**Responsibilities Included**:
1. RSP-089: create lesson structure ✅ MATCHED
2. RSP-NEW-001: generate interactive elements ❌ NEW
3. RSP-156: edit HTML/CSS code ✅ MATCHED
4. RSP-201: deploy content to Full HTML block ✅ MATCHED
5. RSP-298: review and refine content ✅ MATCHED

**Tools Required**:
- TOL-030: Online Academy ✅ MATCHED
- TOL-008: ChatGPT ✅ MATCHED
- TOL-019: VS Code (for editing) ✅ MATCHED

**Skills Demonstrated**:
- SKL-015: lesson creation with Online Academy ✅ MATCHED
- SKL-023: AI-assisted HTML/CSS code generation with ChatGPT ✅ MATCHED

**Steps** (STP-###):
1. STP-001: Create lesson structure in Lesson Library
2. STP-002: Generate HTML/CSS code using ChatGPT with specific prompts
3. STP-003: Copy generated code to Full HTML block
4. STP-004: Preview and test interactive elements
5. STP-005: Refine code based on design requirements
6. STP-006: Save and publish lesson

**Duration**: ~3-4 hours per lesson
**Complexity**: Medium
**Department**: DGN
**Owner**: Kucherenko, Iuliia
**Status**: Completed
**Outcome**: "Successfully generated code using AI for interactive elements (flip cards, animations)"

**Gap Analysis Impact**:
- ❌ RSP-NEW-001 (generate interactive elements) must be added to phrase_matching_index.json
- ❌ OBJ-067 (interactive elements) must be added to Objects/Design_Deliverables.json
- ✅ All other entities exist in libraries

---

[Continue for TSK-002 through TSK-011 with similar format, marking ✅ MATCHED or ❌ NEW for each entity...]
```

---

## SECTION 10: MILESTONE FORMATION

Cluster related tasks into milestones representing deliverable sequences.

[Format remains same as before, but now includes Gap Analysis markers: ✅ MATCHED or ❌ NEW for each entity referenced]

---

## SECTION 11: PROFESSION IDENTIFICATION

Identify professions performing the milestones based on skills demonstrated and responsibilities fulfilled.

[Format remains same as before, with Gap Analysis verification]

---

## SECTION 12: WORKFLOW SEQUENCES

Document end-to-end workflows showing how tasks connect to achieve milestones.

[Format remains same as before]

---

## SECTION 13: DEPENDENCIES AND BLOCKERS

Identify dependencies between entities and any blockers encountered.

[Format remains same as before]

---

## SECTION 14: ENTITY ID ASSIGNMENT & MASTER LIST

Assign unique IDs to all extracted entities and generate comprehensive master list for library integration.

### ID Format Specifications

- **MLS-###**: Milestones (e.g., MLS-001, MLS-002)
- **TSK-###**: Tasks (e.g., TSK-001, TSK-042)
- **STP-###**: Steps (e.g., STP-001, STP-156)
- **ACT-###**: Actions (e.g., ACT-044, ACT-089) - Use existing IDs from actions_master
- **OBJ-###**: Objects (e.g., OBJ-103, OBJ-045)
- **RSP-###**: Responsibilities (e.g., RSP-089, RSP-NEW-001)
- **TOL-###**: Tools (e.g., TOL-030, TOL-008) - Use existing IDs from tools_master
- **SKL-###**: Skills (e.g., SKL-015, SKL-NEW-001)
- **PRF-###**: Professions (e.g., PRF-008, PRF-015) - Use existing IDs from professions_master
- **WF-###**: Workflows (e.g., WF-001, WF-002)

### Format

```markdown
## ENTITY ID ASSIGNMENT & MASTER LIST

### Master Entity List (Markdown Table)

| ID | Type | Name | Description | Dept | Source | Status | Gap Flag |
|----|------|------|-------------|------|--------|--------|----------|
| MLS-001 | Milestone | Online Academy Content Development | Establish AI-assisted educational content creation workflow | DGN | daily_228 | Completed | ✅ MATCHED |
| TSK-001 | Task | Create Online Academy Lessons with AI | Develop interactive educational content using ChatGPT | DGN | daily_228 | Completed | ✅ MATCHED |
| STP-001 | Step | Create lesson structure | Set up lesson framework in Lesson Library | DGN | daily_228 | Completed | ✅ MATCHED |
| ACT-044 | Action | create | Creation verb - bringing new entities into existence | ALL | actions_master | Active | ✅ MATCHED |
| OBJ-103 | Object | lesson structure | Framework for organizing educational content | DGN | daily_228 | New | ❌ NEW_CRITICAL |
| TOL-030 | Tool | Online Academy | Learning management platform | DGN | tools_master | Active | ✅ MATCHED |
| RSP-089 | Responsibility | create lesson structure | Form educational content framework | DGN | phrase_matching | Active | ✅ MATCHED |
| RSP-NEW-001 | Responsibility | generate interactive elements | Create user-interactive components for web content | DGN | daily_228 | New | ❌ NEW_CRITICAL |
| SKL-015 | Skill | lesson creation with Online Academy | Create educational content using LMS platform | DGN | skills_master | Active | ✅ MATCHED |
| SKL-NEW-001 | Skill | AI-assisted content translation | Use AI to convert content between languages | DGN | daily_228 | New | ❌ NEW_CRITICAL |
| PRF-008 | Profession | Instructional Designer | Professional who designs educational content | DGN | professions_master | Active | ✅ MATCHED |
| TOL-NEW-001 | Tool | Time Tracker | Platform for tracking work hours and reports | ALL | daily_228 | New | ❌ NEW_HIGH |
| OBJ-067 | Object | interactive elements | User-interactive web components | DGN | daily_228 | New | ❌ NEW_CRITICAL |

### Entity Count Summary with Gap Analysis

| Entity Type | Existing (✅ Matched) | New (❌ Missing) | Total |
|------------|----------------------|-----------------|-------|
| Milestones (MLS) | 0 | 4 | 4 |
| Tasks (TSK) | 0 | 11 | 11 |
| Steps (STP) | 0 | 34 | 34 |
| Actions (ACT) | 14 ✅ | 0 | 14 |
| Objects (OBJ) | 0-2 (verify) | 8-10 ❌ | 10 |
| Responsibilities (RSP) | 7 ✅ | 4 ❌ | 11 |
| Tools (TOL) | 7 ✅ | 2-4 ❌ | 9-11 |
| Skills (SKL) | 3 ✅ | 3-4 ❌ | 6-7 |
| Professions (PRF) | 2 ✅ | 0-2 (verify) | 2-4 |
| Workflows (WF) | 0 | 4 | 4 |
| **TOTAL** | **33-35** ✅ | **25-32** ❌ | **58-67** |

---

### New Entities Pending Addition to LIBRARIES (From Gap Analysis)

**CRITICAL PRIORITY (Immediate Addition Required)**:

**Responsibilities (4 new)**:
- RSP-NEW-001: generate interactive elements → LIBRARIES/Responsibilities/Design/interactive_element_generation.json
  - **Also add to**: phrase_matching_index.json
- RSP-NEW-002: translate lesson content → LIBRARIES/Responsibilities/Design/content_translation.json
  - **Also add to**: phrase_matching_index.json
- RSP-NEW-003: upload redesigned covers → LIBRARIES/Responsibilities/Design/asset_deployment.json
  - **Also add to**: phrase_matching_index.json
- RSP-NEW-004: identify missing icons → LIBRARIES/Responsibilities/Design/asset_identification.json
  - **Also add to**: phrase_matching_index.json

**Skills (3-4 new)**:
- SKL-NEW-001: AI-assisted content translation → LIBRARIES/Skills/Design/ai_translation.json
- SKL-NEW-002: screen recording with OCam → LIBRARIES/Skills/Video/screen_capture.json
- SKL-NEW-003: video tutorial creation with Loom → LIBRARIES/Skills/Video/tutorial_production.json
- SKL-NEW-004: platform content deployment → LIBRARIES/Skills/Design/platform_deployment.json

**HIGH PRIORITY (Add within 1 week)**:

**Objects (8-10 new)** - Pending verification:
- OBJ-103: lesson structure → LIBRARIES/Responsibilities/Objects/Design_Deliverables.json
  - If already exists: ENHANCE with new tools and workflows
- OBJ-067: interactive elements → LIBRARIES/Responsibilities/Objects/Design_Deliverables.json
  - Types: flip cards, hover animations, keyboard combinations
- OBJ-234: redesigned covers → LIBRARIES/Responsibilities/Objects/Design_Deliverables.json
  - Types: 1280x720 course covers, educational content thumbnails
- OBJ-XXX: catalog documentation → LIBRARIES/Responsibilities/Objects/Documents.json
- OBJ-XXX: screen share recordings → LIBRARIES/Responsibilities/Objects/Video_Deliverables.json
- [Continue for remaining objects...]

**Tools (2-4 new)**:
- TOL-NEW-001: Time Tracker → LIBRARIES/Tools/Productivity/time_tracking_platforms.json
  - **CRITICAL BLOCKER**: Technical issues affecting all employees
- TOL-NEW-002: Whisper Flow → LIBRARIES/Tools/Productivity/transcription_tools.json
  - **STANDARD TOOL**: Used in all daily notes
- TOL-NEW-003: Discord → LIBRARIES/Tools/Communication/team_collaboration.json (if not exists)
- TOL-NEW-004: Google Drive → LIBRARIES/Tools/Productivity/cloud_storage.json (if not exists)

**MEDIUM PRIORITY (Add within 2 weeks)**:

**Professions (0-2 new)** - Pending verification:
- PRF-NEW-001: Videographer → LIBRARIES/Professions/professions_master.json (if not exists)
- PRF-NEW-002: Documentation Specialist → LIBRARIES/Professions/professions_master.json (if not exists)
```

---

## SECTION 15: HIERARCHICAL RELATIONSHIP TREES (ASCII)

Visualize entity relationships using ASCII tree diagrams with Gap Analysis markers.

### Format

```markdown
## HIERARCHICAL RELATIONSHIP TREES

### MLS-001: Online Academy Content Development

```
MLS-001 (Online Academy Content Development) [DGN] ★ COMPLETED
│
├─── TASKS (2)
│    ├── TSK-001 (Create Online Academy Lessons with AI) [DGN] ★ COMPLETED
│    │    ├── STEPS (6)
│    │    │   ├── STP-001: Create lesson structure
│    │    │   ├── STP-002: Generate HTML/CSS code using ChatGPT
│    │    │   ├── STP-003: Copy code to Full HTML block
│    │    │   ├── STP-004: Preview and test interactive elements
│    │    │   ├── STP-005: Refine based on design requirements
│    │    │   └── STP-006: Save and publish lesson
│    │    ├── SKILLS (2)
│    │    │   ├── SKL-015: lesson creation with Online Academy ✅ MATCHED
│    │    │   └── SKL-023: AI-assisted HTML/CSS code generation ✅ MATCHED
│    │    ├── RESPONSIBILITIES (5)
│    │    │   ├── RSP-089: create lesson structure ✅ MATCHED
│    │    │   ├── RSP-NEW-001: generate interactive elements ❌ NEW_CRITICAL
│    │    │   ├── RSP-156: edit HTML/CSS code ✅ MATCHED
│    │    │   ├── RSP-201: deploy content to Full HTML block ✅ MATCHED
│    │    │   └── RSP-298: review and refine content ✅ MATCHED
│    │    ├── TOOLS (3)
│    │    │   ├── TOL-030: Online Academy ✅ MATCHED
│    │    │   ├── TOL-008: ChatGPT ✅ MATCHED
│    │    │   └── TOL-019: VS Code ✅ MATCHED
│    │    ├── OBJECTS (3)
│    │    │   ├── OBJ-103: lesson structure ❌ NEW_CRITICAL (verify if exists)
│    │    │   ├── OBJ-067: interactive elements ❌ NEW_CRITICAL
│    │    │   └── OBJ-045: HTML/CSS code ✅ MATCHED
│    │    └── ACTIONS (3)
│    │        ├── ACT-044: create ✅ MATCHED
│    │        ├── ACT-089: generate ✅ MATCHED
│    │        └── ACT-156: edit ✅ MATCHED
│    │
│    └── TSK-002 (Manage GitHub Repositories for Design Files) [DEV] ★ COMPLETED
│         [Similar structure with gap analysis markers...]
│
├─── PROFESSIONS (2)
│    ├── PRF-008: Instructional Designer ✅ MATCHED
│    └── PRF-015: Web Developer ✅ MATCHED
│
├─── WORKFLOWS (2)
│    ├── WF-001: AI-Assisted Educational Content Creation
│    └── WF-002: GitHub Repository Management for Design Projects
│
└─── DELIVERABLES (4)
     ├── Functional interactive lessons deployed to Online Academy
     ├── GitHub repositories with version-controlled HTML/CSS code
     ├── Documentation of AI prompt templates
     └── Planned video tutorial series

COMPLEXITY: High | DURATION: Full day (9:00-17:00) | DEPARTMENT: DGN (Primary), DEV (Secondary)
SOURCE: daily_228_Kucherenko_Iuliia.md | DATE: 2025-01-17

GAP ANALYSIS IMPACT:
  - ❌ CRITICAL: 2 new Responsibilities (RSP-NEW-001, RSP-NEW-002) require library addition
  - ❌ CRITICAL: 2-3 new Objects (OBJ-103, OBJ-067, OBJ-045 verify) require library addition
  - ✅ All Actions, Tools, Skills, Professions matched to existing libraries
```

[Continue for MLS-002, MLS-003, MLS-004 with gap analysis markers...]
```

---

## SECTION 16: DEPARTMENT DISTRIBUTION ANALYSIS

Quantify entity distribution across departments.

[Format remains same as before]

---

## SECTION 17: SOURCE METADATA & PROVENANCE

Track complete provenance and source information for traceability.

[Format remains same as before]

---

## VALIDATION CHECKLIST

Use this checklist to ensure output quality before submission.

### Tier 1: Format Validation

- [ ] Output is in markdown format (not JSON, not CSV)
- [ ] Header hierarchy is correct (## for sections, ### for subsections)
- [ ] Master entity list is formatted as Markdown table with Gap_Analysis_Flag column
- [ ] ASCII trees use correct characters (├── └── │) with ✅ MATCHED / ❌ NEW markers
- [ ] All code blocks are properly fenced with triple backticks
- [ ] No syntax errors in markdown

### Tier 2: Section Completeness

- [ ] Section 1: Metadata (all 8 fields)
- [ ] Section 2: Executive Summary (3-5 bullets **including Gap Analysis Highlights**)
- [ ] **Section 3: Gap Analysis - Libraries Check (ALL 5 ENTITY TYPES: Actions, Objects, Responsibilities, Tools, Skills)**
- [ ] Section 4: Action Verb Categorization (all 7 categories A-G with ✅ MATCHED markers)
- [ ] Section 5: Object Probability Marking (with ✅ MATCHED / ❌ NEW markers)
- [ ] Section 6: Responsibility Formation (matched + new with library paths)
- [ ] Section 7: Tool Identification (matched + new with catalog paths)
- [ ] Section 8: Skill Recognition (using formula with library paths for new skills)
- [ ] Section 9: Task Clustering (ACTION+OBJECT+CONTEXT format with gap markers)
- [ ] Section 10: Milestone Formation (with boundaries and gap markers)
- [ ] Section 11: Profession Identification (with gap verification)
- [ ] Section 12: Workflow Sequences (with decision points)
- [ ] Section 13: Dependencies and Blockers
- [ ] Section 14: Entity ID Assignment & Master List (Markdown table with Gap_Analysis_Flag column)
- [ ] Section 15: Hierarchical Relationship Trees (ASCII with ✅ ❌ markers)
- [ ] Section 16: Department Distribution Analysis
- [ ] Section 17: Source Metadata & Provenance

### Tier 3: Content Quality

- [ ] Actions properly categorized into 7 types (A-G) **with existence verification**
- [ ] Objects have numeric probability scores **and library existence check**
- [ ] Responsibilities follow action+object pattern **with phrase_matching_index.json verification**
- [ ] Tools matched against tools_master_catalog.json **with new tools flagged**
- [ ] Skills use formula: Responsibility + Tool = Skill **with skills_master.json verification**
- [ ] Tasks follow ACTION+OBJECT+CONTEXT format
- [ ] Milestones have clear deliverable clusters
- [ ] Timestamps preserved from daily notes
- [ ] Outcomes clearly stated
- [ ] Workflows show decision points and flows
- [ ] Blockers have severity and resolution paths
- [ ] **Gap Analysis complete for ALL entity types (Actions, Objects, Responsibilities, Tools, Skills, Professions)**

### Tier 4: Integration Validation

- [ ] All entity IDs follow XXX-### format
- [ ] Department codes are valid 3-letter ISO (DGN, DEV, VID, etc.)
- [ ] Master entity list count matches tree count
- [ ] **Master entity list includes Gap_Analysis_Flag column (✅ MATCHED, ❌ NEW_CRITICAL, ❌ NEW_HIGH, ❌ NEW_MEDIUM)**
- [ ] No orphan entities (all linked to hierarchies)
- [ ] Source files properly referenced
- [ ] New entities flagged with "NEW" status **and priority level**
- [ ] Existing entities show library source (actions_master.json, phrase_matching_index.json, tools_master_catalog.json, skills_master.json)
- [ ] Library paths suggested for **ALL** new entities
- [ ] **Gap Analysis Summary table shows counts: Matched vs. Missing vs. Enhancement Needed**

### Tier 5: Gap Analysis Validation (NEW)

- [ ] **Section 3 (Gap Analysis) is complete and comprehensive**
- [ ] **All 5 entity types checked**: Actions, Objects, Responsibilities, Tools, Skills
- [ ] **(Optional) Professions checked** if relevant
- [ ] **For each entity type**:
  - [ ] ✅ EXISTS section lists matched entities with library sources
  - [ ] ❌ MISSING section lists new entities with priority (CRITICAL/HIGH/MEDIUM)
  - [ ] Enhancement opportunities identified for existing entities
- [ ] **For each NEW entity**:
  - [ ] Priority level assigned (CRITICAL/HIGH/MEDIUM)
  - [ ] Suggested library path provided
  - [ ] CREATE FULL ENTRY instruction included for high-priority items
  - [ ] Evidence from daily note cited
  - [ ] Related entities identified (tools, skills, professions, departments)
- [ ] **Gap Analysis Summary table present** showing counts (Matched / Missing / Enhancement)
- [ ] **Priority Actions list present** showing critical vs. high vs. medium priority additions
- [ ] **Files to Update list present** showing all library files requiring updates

---

## USAGE INSTRUCTIONS

1. **Read the daily note file** thoroughly
2. **Immediately perform Gap Analysis** (Section 3) by checking entities against existing libraries:
   - `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json` (429 actions)
   - `ENTITIES/LIBRARIES/Responsibilities/Core/phrase_matching_index.json` (209 patterns)
   - `ENTITIES/LIBRARIES/Responsibilities/Core/responsibilities_master.json` (193 responsibilities)
   - `ENTITIES/LIBRARIES/Responsibilities/Objects/` (Design_Deliverables.json, Documents.json, Video_Deliverables.json, etc.)
   - `ENTITIES/LIBRARIES/Tools/` (70+ tools organized by category - NO master catalog file)
   - `ENTITIES/LIBRARIES/Skills/` (location TBD - verify before using)
   - `ENTITIES/LIBRARIES/Professions/professions.json`
3. **Extract entities** following the 7-step methodology **with gap markers (✅ ❌)**
4. **Generate all 17 sections** in order (note: Section 3 is Gap Analysis)
5. **Draw ASCII trees** for each milestone **with ✅ MATCHED / ❌ NEW markers**
6. **Calculate department distribution**
7. **Document source metadata** completely
8. **Run validation checklist** (5 tiers including Gap Analysis tier)
9. **Save output** as `daily_processed_[employee_number]_[LastName]_[FirstName].md` (Markdown only)

---

## APPENDIX: INTEGRATION WITH EXISTING LIBRARIES

### Actions Library (429 actions)
- Location: `LIBRARIES/Responsibilities/Actions/Actions_Master.json`
- Additional files: `Actions_Master_Command_Verbs.json`, `Actions_Master_Process_Verbs.json`, `Actions_Master_Result_Verbs.json`
- Format: Process form, Result form, Category, Definition
- Integration: Match extracted verbs to existing actions, flag new ones (though all should match to 429 existing)

### Responsibilities Library (193 responsibilities, 209 phrase patterns)
- Core location: `LIBRARIES/Responsibilities/Core/`
- Key files:
  - `responsibilities_master.json` (193 responsibilities)
  - `phrase_matching_index.json` (209 action+object patterns)
  - `action_variants_map.json` (57 action synonyms)
  - `object_variants_map.json` (169 object variants)
- Format: Action+Object pairs with IDs
- Integration: Match formed responsibilities to existing 209 patterns, create RSP-NEW-### for additions
- **CRITICAL**: All new responsibilities must be added to phrase_matching_index.json for future matching

### Objects Library (36+ objects across 13 domain files)
- Location: `LIBRARIES/Responsibilities/Objects/`
- Files: `Design_Deliverables.json`, `Documents.json`, `Video_Deliverables.json`, `object_types.json`, plus 10 other domain files
- Format: See Objects_Library_Extraction_Prompt.md for full template
- Integration: Verify existence, enhance existing entries, create new entries with full attributes
- **Use template from**: Objects_Library_Extraction_Prompt.md (lines 641-1060)

### Tools Library (70+ individual tool files - NO master catalog)
- Location: `LIBRARIES/Tools/`
- **IMPORTANT**: Tools are organized by category folders, NOT in a single master file
- Categories: `AI_Tools/`, `Development_Tools/`, `Data_Tools/`, `Business_Tools/`, `Automation_Tools/`, `Integration_Tools/`
- Plus individual social media platform files at root level
- Integration: Match mentioned tools to existing category files, create new tool JSON files in appropriate category folder
- **NO tools_master_catalog.json** - each tool has its own JSON file

### Skills Library (28 skills)
- Location: `LIBRARIES/Skills/skills_master.json`
- Format: Skill name, Definition, Required responsibilities, Required tools
- Integration: Apply formula (Responsibility + Tool = Skill), match or create new
- **CRITICAL**: All new skills must include learning path, proficiency indicators, time to proficiency

### Professions Library
- Location: `LIBRARIES/Professions/professions_master.json`
- Format: Profession name, Skills required, Responsibilities, Departments
- Integration: Match demonstrated skills/responsibilities to professions, verify existence

---

## VERSION HISTORY

**v1.0** (2025-11-19)
- Initial release
- Incorporates methodologies from Video Transcription Custom Instructions v4.0
- **Incorporates Gap Analysis methodology from Objects_Library_Extraction_Prompt.md v2.0**
- 7-step processing pipeline with library verification
- 17-section output format (added Section 3: Gap Analysis)
- Markdown master list as primary output with Gap_Analysis_Flag column
- ASCII tree diagrams with ✅ MATCHED / ❌ NEW markers
- Department distribution analysis
- 5-tier validation system (added Tier 5: Gap Analysis Validation)
- 7-category action verb classification (A-G) with existence verification
- Source metadata and provenance tracking
- **Systematic library checking for all 5+ entity types (Actions, Objects, Responsibilities, Tools, Skills, Professions)**
- **Priority-based addition workflow (CRITICAL/HIGH/MEDIUM)**
- **Library file update recommendations**

**v1.1** (2025-11-19)
- **Changed output format to Markdown-only** (removed CSV requirements)
- **Updated all library paths to actual LIBRARIES taxonomy structure**
- Corrected Actions location: `Responsibilities/Actions/Actions_Master.json`
- Corrected Responsibilities location: `Responsibilities/Core/` subdirectory
- Corrected Objects location: `Responsibilities/Objects/` with domain-specific files
- Documented Tools organization: NO master catalog - 70+ individual files by category
- Updated all file path references throughout prompt
- Converted master entity list from CSV to Markdown table format
- Updated validation checklist to remove CSV-specific requirements

---

**END OF PROMPT**
