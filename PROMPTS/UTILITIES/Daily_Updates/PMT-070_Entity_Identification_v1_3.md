# Daily Updates Entity Identification System
## Version 1.3 - Preparation Phase Integration

---

## PURPOSE

Extract and structure taxonomy entities from daily work logs following a hierarchical methodology:

**Actions → Objects → Responsibilities → Tools → Skills → Tasks → Milestones**

Integrates with existing LIBRARIES taxonomy (429 Actions, 193 Responsibilities, 190+ Tools, 28 Skills) and generates structured outputs for entity management.

**Key Feature**: **Library Enrichment** analysis to identify new entities and enhancement opportunities.

---

## CORE METHODOLOGY

### PHASE 0: PREPARATION - Markup Injection (NEW)

**Before extraction, inject markup tags directly into the source daily file to structure raw text.**

**Markup Symbols**:
- `<ACTION>` - Highlight action verbs
- `<OBJECT>` - Mark deliverables, outputs, targets
- `<TOOL>` - Identify mentioned tools/platforms
- `<DEPT>` - Department references (AID, DEV, SLS, HRM, VID, etc.)
- `<MILESTONE>` - Major deliverable clusters
- `<BLOCKER>` - Issues preventing progress
- `★` - High priority items
- `⚠️` - Warnings or risks
- `✅` - Completed items
- `[ ]` - Pending tasks

**Example Markup**:
```
Original: "Created GitHub repository for online academy setup"
Marked up: "<ACTION>Created</ACTION> <TOOL>GitHub</TOOL> <OBJECT>repository</OBJECT> for <MILESTONE>online academy setup</MILESTONE>"
```

**Process**:
1. Read the raw daily file
2. Inject markup tags inline throughout the text
3. Save marked-up version as `[filename]_marked.md` in same folder
4. Use marked-up file as input for extraction phases below

**Note**: This is human feedback simulation - teaching AI to recognize entity boundaries in unstructured text.

---

### 7-Step Processing Pipeline (Skills skipped for now - future enhancement)

1. **PHASE 0: Preparation** - Inject markup tags into raw daily file
2. **Action Word Tagging** - Extract verbs and categorize into 7 types (A-G)
3. **Object Probability Marking** - Identify objects with probability scores
4. **Responsibility Formation** - Combine action+object pairs
5. **Tool Identification** - Extract mentioned tools
6. **Task & Steps Clustering** - Group responsibilities into tasks with atomic steps
7. **Milestone Formation** - Cluster tasks into deliverable sequences

**Note**:
- Skill Recognition (Responsibility + Tool = Skill) deferred to Phase 2
- **Library Enrichment comparison** deferred to separate analysis after extraction

### Hierarchical Structure

```
MILESTONE (MLS-###) - Deliverable cluster
├── TASK (TSK-###) - ACTION + OBJECT + CONTEXT
│   ├── STEP (STP-###) - Atomic action
│   │   ├── ACTION (ACT-###) - Verb from 429 library
│   │   ├── OBJECT (OBJ-###) - Target of action
│   │   ├── TOOL (TOOL-{CATEGORY}-###) - Instrument used
│   │   └── RESPONSIBILITY (RSP-###) - Action+Object pair
│   └── SKILL (SKL-###) - Responsibility + Tool
└── PROFESSION (PRF-###) - Role performing milestone
```

---

## OUTPUT FORMAT

**REQUIRED FORMAT: Markdown (.md) ONLY**

❌ **DO NOT** output CSV files, JSON, or plain text
✅ **REQUIRED**: Structured markdown document with 15 sections (Skills section removed, Library Enrichment deferred)

---

## SECTION 1: METADATA

```markdown
## METADATA

**DAILY_NOTE_ID**: daily_[employee_number]_[LastName]_[FirstName]
**PERSON**: [Full Name]
**DEPARTMENT**: [Primary Department ISO Code]
**DATE**: [YYYY-MM-DD]
**SOURCE_FILE**: [Full file path]
**EXTRACTION_DATE**: [YYYY-MM-DD HH:MM:SS]
**EXTRACTOR_VERSION**: Daily_Updates_v1.2
**PROCESSING_STATUS**: [Complete/Partial/In Progress]
```

---

## SECTION 2: EXECUTIVE SUMMARY

Provide 3-5 concise bullet points:
- Main milestones accomplished
- Key skills demonstrated
- Tools utilized (with counts)
- Library enrichment highlights (new entities)

**Example:**
```markdown
## EXECUTIVE SUMMARY

- **Milestone**: AI Workflow Infrastructure - Multi-model orchestration system
- **Tools**: Cursor, GPT-5.1, Perplexity, Gemini, Dropbox (5 tools)
- **Entities**: 3 Milestones, 8 Tasks, 24 Steps, 15 Actions, 12 Objects, 5 Tools, 8 Responsibilities
- **Professions**: AI Engineer, Backend Developer, Sales Researcher
```

---

## SECTION 3: ACTION VERB EXTRACTION

**Extract and categorize verbs into 7 types (A-G). List format only - no verbose explanations.**

```markdown
## ACTION EXTRACTION

### A. CREATION (bring into existence)
- ACT-044: create (12x) ✅
- ACT-089: generate (5x) ✅

### B. MODIFICATION (change existing)
- ACT-156: edit (8x) ✅
- ACT-401: update (4x) ✅

### C. ANALYSIS (examine/investigate)
- ACT-298: review (6x) ✅
- ACT-412: identify (3x) ✅

### D. ORGANIZATION (structure/arrange)
- ACT-187: organize (2x) ✅
- ACT-265: plan (1x) ✅

### E. COMMUNICATION (share/transfer)
- ACT-378: translate (4x) ✅
- ACT-092: document (3x) ✅

### F. AGENTIC/AUTOMATION (system actions)
- ACT-123: deploy (2x) ✅
- ACT-201: upload (5x) ✅

### G. DATA OPERATIONS (manipulate data)
- ACT-167: extract (1x) ✅
- ACT-289: insert (2x) ✅

**Summary**: 15 actions extracted, 15 matched (100%), 0 new
```

---

## SECTION 4: OBJECT PROBABILITY MARKING

**Compact format: Action → Objects with probability scores**

```markdown
## OBJECT PROBABILITY MARKING

### ACT-044: create

**HIGH (0.8-1.0)**:
- lesson structure (0.95) ✅ phrase_matching_index
- repository (0.92) ✅
- video tutorials (0.88) ❌ NEW

**MEDIUM (0.5-0.79)**:
- documentation (0.68) ⚠️ VERIFY

### ACT-089: generate

**HIGH**:
- HTML/CSS code (0.98) ✅
- interactive elements (0.91) ❌ NEW
- code (0.85) ✅

### ACT-156: edit

**HIGH**:
- files (0.94) ✅
- HTML/CSS code (0.91) ✅

[Continue for remaining actions...]
```

---

## SECTION 5: RESPONSIBILITY FORMATION

**Combine action+object pairs. Match to phrase_matching_index.json (193 existing).**

```markdown
## RESPONSIBILITY FORMATION

### Matched Responsibilities

- **RSP-089: create lesson structure** ✅
  - ACT-044 + lesson structure | DGN
  - Evidence: "Create lesson structure in Lesson Library"

- **RSP-156: edit HTML/CSS code** ✅
  - ACT-156 + HTML/CSS code | DEV
  - Evidence: "Editing code in VS Code"

### New Responsibilities

- **RSP-NEW-001: generate interactive elements** ❌ CRITICAL
  - ACT-089 + interactive elements | DGN
  - Tools: TOOL-AI-008
  - Evidence: "Generated AI code for flip cards, animations"
  - ADD TO: phrase_matching_index.json

- **RSP-NEW-002: translate lesson content** ❌ HIGH
  - ACT-378 + lesson content | DGN
  - Tools: TOOL-AI-008
  - Evidence: "Translating content to English using AI"
  - ADD TO: phrase_matching_index.json

[Continue for all new responsibilities...]
```

---

## SECTION 6: TOOL IDENTIFICATION

**Extract tools and match to Tools/ library (190+ in category folders).**

```markdown
## TOOL IDENTIFICATION

### Matched Tools

- **TOOL-AI-028: GPT-5.1** ✅ (AI_Tools/OpenAI_GPT5.json)
  - Mentions: 12x | Context: Code generation, translation
- **TOOL-DEV-044: Cursor** ✅ (Development_Tools/Cursor.json)
  - Mentions: 25x | Context: AI-powered development
- **TOOL-AI-004: Perplexity** ✅ (AI_Tools/Perplexity.json)
  - Mentions: 8x | Context: Research, fact-checking
- **TOOL-FILE-006: Dropbox** ✅ (File_Management/Dropbox.json)
  - Mentions: 4x | Context: File storage

### New Tools

- **Whisper Flow** ❌ HIGH
  - Category: TOOL-AI-### or TOOL-DATA-###
  - Description: Audio transcription for meeting documentation
  - Context: Daily notes, meeting transcripts (bilingual)
  - Dept: ALL
  - ADD TO: Tools/AI_Tools/ or Tools/Data_Tools/

[Continue for remaining new tools...]
```

---

## SECTION 7: TASK & STEPS CLUSTERING

**Group responsibilities into tasks: ACTION + OBJECT + CONTEXT**

```markdown
## TASK CLUSTERING

### TSK-001: Create Online Academy Lessons with AI

**Format**: Create + Online Academy Lessons + with AI assistance

**Responsibilities**:
1. RSP-089: create lesson structure ✅
2. RSP-NEW-001: generate interactive elements ❌
3. RSP-156: edit HTML/CSS code ✅
4. RSP-201: deploy content ✅

**Tools**: TOOL-LMS-030, TOOL-AI-008, TOOL-DEV-019
**Skills**: SKL-015 ✅, SKL-023 ✅
**Steps**: 6 (Create structure → Generate code → Copy → Preview → Refine → Publish)
**Duration**: 3-4 hours | Dept: DGN | Status: Completed

### TSK-002: Manage Client Research System

**Format**: Build + Research System + for client analysis

**Responsibilities**:
1. RSP-NEW-003: research client background ❌
2. RSP-NEW-004: analyze patent information ❌
3. RSP-092: document findings ✅

**Tools**: TOOL-AI-004, TOOL-AI-028, TOOL-DATA-###
**Skills**: SKL-NEW-002 ✅
**Steps**: 8
**Duration**: 2-3 hours | Dept: SLS, AID | Status: Completed

[Continue for TSK-003 through TSK-008...]
```

---

## SECTION 8: MILESTONE FORMATION

**Cluster related tasks into deliverable sequences.**

```markdown
## MILESTONE FORMATION

### MLS-001: AI Workflow Infrastructure

**Tasks**: TSK-001 (Multi-model orchestration), TSK-002 (Cursor integration), TSK-003 (Workflow testing)
**Timeline**: Morning session (09:00-12:00)
**Professions**: AI Engineer (PRF-NEW) ✅, Backend Developer (PRF-015) ✅
**Deliverables**: Functional multi-model system, documented workflows, tested integrations
**Dept**: AID | Status: Completed

### MLS-002: Client Research System (Desert Greener)

**Tasks**: TSK-004 (Background research), TSK-005 (Patent analysis), TSK-006 (Documentation)
**Timeline**: Afternoon session (13:00-15:00)
**Professions**: Sales Research Specialist (PRF-NEW), AI Engineer (PRF-NEW)
**Deliverables**: Client profile, patent summary, contact information
**Dept**: SLS, AID | Status: Completed

### MLS-003: Employee Compliance Audit

**Tasks**: TSK-007 (Audit employee data), TSK-008 (Report generation)
**Timeline**: Late afternoon (15:30-17:00)
**Professions**: HR Compliance Coordinator (PRF-NEW)
**Deliverables**: Compliance report, issue identification
**Dept**: HRM | Status: Completed

[Continue for remaining milestones...]
```

---

## SECTION 9: PROFESSION IDENTIFICATION

**Identify professions based on skills/responsibilities demonstrated.**

```markdown
## PROFESSION IDENTIFICATION

### Matched Professions

- **PRF-015: Backend Developer** ✅
  - Skills: SKL-031 (GitHub management), SKL-023 (AI code gen)
  - Responsibilities: RSP-044, RSP-187, RSP-156

### New Professions

- **PRF-NEW-001: AI Engineer** ❌ HIGH
  - Skills: SKL-NEW-002 (multi-model orchestration), SKL-NEW-003 (prompt optimization)
  - Responsibilities: RSP-NEW-005, RSP-NEW-006, RSP-NEW-007
  - Tools: TOOL-AI-028, TOOL-AI-004, TOOL-DEV-044
  - Dept: AID

- **PRF-NEW-002: Sales Research Specialist** ❌ MEDIUM
  - Skills: SKL-NEW-004 (client research), SKL-NEW-005 (data enrichment)
  - Responsibilities: RSP-NEW-003, RSP-NEW-004
  - Tools: TOOL-AI-004, TOOL-DATA-###
  - Dept: SLS

[Continue for remaining professions...]
```

---

## SECTION 10: WORKFLOW SEQUENCES

**Document end-to-end workflows (concise format).**

```markdown
## WORKFLOW SEQUENCES

### WF-001: Multi-Model AI Orchestration

**Trigger**: Complex task requiring multiple AI models
**Steps**:
1. Analyze task requirements → Identify model strengths
2. Select primary model (GPT-5.1/Perplexity/Gemini) → Context-based choice
3. Execute via Cursor interface → Single workspace
4. Cross-verify results → Secondary model validation
5. Document outcomes → Knowledge base

**Duration**: 15-30 min/task | **Frequency**: 10-15x/day

### WF-002: Client Research & Enrichment

**Trigger**: New client prospect
**Steps**:
1. Initial search (Perplexity/GPT-5) → Background, patents, financials
2. Contact enrichment (Apollo.io implied) → Emails, decision-makers
3. Documentation (Markdown) → Structured client profile
4. Storage (Dropbox) → Centralized repository

**Duration**: 1-2 hours/client | **Frequency**: As needed

[Continue for remaining workflows...]
```

---

## SECTION 11: DEPENDENCIES AND BLOCKERS

**Identify dependencies and blockers (table format).**

```markdown
## DEPENDENCIES AND BLOCKERS

### Dependencies

| Task | Depends On | Type | Status |
|------|-----------|------|--------|
| TSK-001 | Cursor installed | Tool | ✅ Met |
| TSK-002 | GPT-5.1 access | Tool | ✅ Met |
| TSK-004 | Perplexity subscription | Tool | ✅ Met |

### Blockers

| Blocker | Severity | Impact | Resolution |
|---------|----------|--------|------------|
| Time Tracker down | HIGH | Report submission failed | Escalated to IT |
| Whisper Flow lag | MEDIUM | Transcript delays | Recorded locally as backup |
| (None other) | - | - | - |

**Blocking Summary**: 2 blockers (1 HIGH, 1 MEDIUM), both with workarounds implemented
```

---

## SECTION 12: ENTITY ID ASSIGNMENT & MASTER LIST

**Assign IDs to all entities. Markdown table with enrichment flags.**

### ID Format Specifications

- **MLS-###**: Milestones
- **TSK-###**: Tasks
- **STP-###**: Steps
- **ACT-###**: Actions (use existing from Actions_Master.json)
- **OBJ-###**: Objects
- **RSP-###**: Responsibilities (use existing from phrase_matching_index.json)
- **TOOL-{CATEGORY}-###**: Tools (e.g., TOOL-AI-028, TOOL-DEV-044)
- **SKL-###**: Skills
- **PRF-###**: Professions
- **WF-###**: Workflows

```markdown
## ENTITY MASTER LIST

| ID | Type | Name | Dept | Source | Status | Flag |
|----|------|------|------|--------|--------|------|
| MLS-001 | Milestone | AI Workflow Infrastructure | AID | daily_171125 | Completed | ✅ MATCHED |
| TSK-001 | Task | Multi-model orchestration setup | AID | daily_171125 | Completed | ✅ MATCHED |
| ACT-044 | Action | create | ALL | Actions_Master | Active | ✅ MATCHED |
| OBJ-103 | Object | lesson structure | DGN | daily_171125 | New | ❌ NEW_CRITICAL |
| TOOL-AI-028 | Tool | GPT-5.1 | AID | AI_Tools/ | Active | ✅ MATCHED |
| TOOL-DEV-044 | Tool | Cursor | DEV | Development_Tools/ | Active | ✅ MATCHED |
| RSP-NEW-001 | Responsibility | generate interactive elements | DGN | daily_171125 | New | ❌ NEW_CRITICAL |
| SKL-NEW-001 | Skill | AI-assisted translation | DGN | daily_171125 | New | ❌ NEW_CRITICAL |
| PRF-NEW-001 | Profession | AI Engineer | AID | daily_171125 | New | ❌ NEW_HIGH |

### Entity Count Summary

| Entity Type | Matched ✅ | New ❌ | Total |
|------------|-----------|--------|-------|
| Milestones (MLS) | 0 | 3 | 3 |
| Tasks (TSK) | 0 | 8 | 8 |
| Steps (STP) | 0 | 24 | 24 |
| Actions (ACT) | 15 | 0 | 15 |
| Objects (OBJ) | 2 | 8 | 10 |
| Responsibilities (RSP) | 7 | 4 | 11 |
| Tools (TOOL) | 7 | 2 | 9 |
| Skills (SKL) | 3 | 3 | 6 |
| Professions (PRF) | 2 | 2 | 4 |
| Workflows (WF) | 0 | 3 | 3 |
| **TOTAL** | **36** | **57** | **93** |

### New Entities for Library Addition

**CRITICAL (Immediate)**:
- RSP-NEW-001 through RSP-NEW-004 → phrase_matching_index.json
- SKL-NEW-001 through SKL-NEW-003 → skills_master.json
- OBJ-103, OBJ-067, OBJ-234 → Design_Deliverables.json

**HIGH (Within 1 week)**:
- TOOL-AI-### (Whisper Flow) → Tools/AI_Tools/ or Tools/Data_Tools/
- PRF-NEW-001, PRF-NEW-002 → professions.json

[Continue with detailed library paths for each new entity...]
```

---

## SECTION 13: HIERARCHICAL RELATIONSHIP TREES (ASCII)

**Visualize entity relationships with enrichment markers.**

```markdown
## HIERARCHICAL RELATIONSHIP TREES

### MLS-001: AI Workflow Infrastructure

```
MLS-001 (AI Workflow Infrastructure) [AID] ★ COMPLETED
│
├─── TASKS (3)
│    ├── TSK-001: Multi-model orchestration setup
│    │    ├── SKILLS (2)
│    │    │   ├── SKL-NEW-002: multi-model AI orchestration ❌ NEW_HIGH
│    │    │   └── SKL-023: AI-assisted code generation ✅ MATCHED
│    │    ├── RESPONSIBILITIES (3)
│    │    │   ├── RSP-NEW-005: configure multi-model system ❌ NEW_CRITICAL
│    │    │   ├── RSP-NEW-006: test model switching ❌ NEW_HIGH
│    │    │   └── RSP-156: edit configuration files ✅ MATCHED
│    │    ├── TOOLS (3)
│    │    │   ├── TOOL-AI-028: GPT-5.1 ✅ MATCHED
│    │    │   ├── TOOL-AI-004: Perplexity ✅ MATCHED
│    │    │   └── TOOL-DEV-044: Cursor ✅ MATCHED
│    │    └── ACTIONS (3)
│    │        ├── ACT-044: create ✅ MATCHED
│    │        ├── ACT-156: edit ✅ MATCHED
│    │        └── ACT-412: identify ✅ MATCHED
│    │
│    ├── TSK-002: Cursor IDE integration [...]
│    └── TSK-003: Workflow testing [...]
│
├─── PROFESSIONS (2)
│    ├── PRF-NEW-001: AI Engineer ❌ NEW_HIGH
│    └── PRF-015: Backend Developer ✅ MATCHED
│
├─── WORKFLOWS (2)
│    ├── WF-001: Multi-Model AI Orchestration
│    └── WF-002: Cursor-based Development
│
└─── DELIVERABLES
     ├── Functional multi-model system
     ├── Documented switching workflows
     └── Tested integrations

COMPLEXITY: High | DURATION: 3 hours | DEPT: AID
ENRICHMENT: 3 new Responsibilities, 1 new Skill, 1 new Profession
```

[Continue for MLS-002, MLS-003...]
```

---

## SECTION 14: DEPARTMENT DISTRIBUTION ANALYSIS

**Quantify entity distribution across departments (table format).**

```markdown
## DEPARTMENT DISTRIBUTION

| Department | Milestones | Tasks | Skills | Tools | Responsibilities |
|-----------|-----------|-------|--------|-------|-----------------|
| AID | 1 | 3 | 2 | 4 | 5 |
| SLS | 1 | 2 | 2 | 2 | 3 |
| HRM | 1 | 2 | 1 | 1 | 2 |
| DEV | 0 | 1 | 1 | 2 | 3 |
| **TOTAL** | **3** | **8** | **6** | **9** | **13** |

**Primary Department**: AID (33% of work)
**Cross-functional**: 2 milestones involve 2+ departments
```

---

## SECTION 15: SOURCE METADATA & PROVENANCE

**Track source information for traceability.**

```markdown
## SOURCE METADATA

**Original File**: C:\Users\Dell\Dropbox\ENTITIES\DAILIES\17\171125_Niko.md
**File Size**: 245 lines
**Language**: Russian/Ukrainian (primary), English (secondary)
**Format**: Whisper Flow transcripts + structured notes
**Employee**: Niko (ID: 171125)
**Date**: 2025-11-25
**Processing Date**: 2025-11-19 [HH:MM:SS]
**Extractor Version**: Daily_Updates_v1.2
**Processing Time**: [X minutes]
**Total Entities Extracted**: 93 (36 matched, 57 new)
**Library Files to Update**: 5 (phrase_matching_index.json, skills_master.json, Design_Deliverables.json, AI_Tools/, professions.json)
```

---

## VALIDATION CHECKLIST

### Format
- [ ] Markdown output only (no CSV/JSON)
- [ ] All 17 sections present
- [ ] Master list is Markdown table with Flag column
- [ ] ASCII trees use correct characters (├── └── │)

### Content
- [ ] Actions categorized into 7 types (A-G)
- [ ] Objects have probability scores
- [ ] Responsibilities match action+object pattern
- [ ] Tools use TOOL-{CATEGORY}-### format
- [ ] Skills use formula: Responsibility + Tool = Skill
- [ ] Library enrichment complete for all entity types

### Integration
- [ ] All IDs follow XXX-### format
- [ ] Department codes valid (AID, DEV, SLS, etc.)
- [ ] Master list count matches tree count
- [ ] Enrichment flags correct (✅ ❌)
- [ ] Library paths provided for all new entities

---

## USAGE INSTRUCTIONS

1. **Read daily note** thoroughly
2. **Extract entities** (Actions, Objects, Responsibilities, Tools, Tasks, Steps, Milestones)
3. **Generate 15 sections** in order
4. **Draw ASCII trees**
5. **Calculate distributions**
6. **Document metadata**
7. **Validate** (checklist above)
8. **Save** as `daily_processed_[ID]_[LastName]_[FirstName].md`

**Note**: Library comparison (✅ ❌ markers) happens in separate analysis step AFTER extraction

---

## KEY CHANGES IN V1.2

**Streamlined Processing**:
- Removed Library Enrichment section (was Section 3)
- Removed Skills section (was Section 8)
- Actions section simplified (list format, no verbose examples)
- Compact object probability format
- Structured tables throughout

**Focus on Data Extraction**:
- Less prose, more structured lists
- Compact responsibility/skill/tool sections
- Table-based analysis (dependencies, departments, counts)
- Direct extraction without over-explanation

---

## VERSION HISTORY

**v1.3** (2025-11-19)
- **Added PHASE 0: PREPARATION** - Markup injection step before extraction
- Inject markup tags (`<ACTION>`, `<OBJECT>`, `<TOOL>`, etc.) directly into raw daily files
- Save marked-up version as `[filename]_marked.md` for enhanced extraction accuracy
- 7-step pipeline (was 6): Preparation → Actions → Objects → Responsibilities → Tools → Tasks/Steps → Milestones
- Human feedback simulation approach to teach AI entity boundary recognition

**v1.2** (2025-11-19)
- **Removed Library Enrichment section** - deferred to separate analysis step AFTER extraction
- **Removed Skills section** - deferred to Phase 2
- Compact list formats for Actions, Objects, Responsibilities, Tools
- Table-based analysis throughout
- Focus on data extraction vs. library comparison
- **15 sections** (was 17): removed Section 3 (Library Enrichment) and Section 8 (Skills)
- Reorganized flow: Extract → Form → Cluster → Analyze (no library matching during extraction)
- 6-step pipeline: Actions → Objects → Responsibilities → Tools → Tasks/Steps → Milestones

**v1.1** (2025-11-19)
- Markdown-only output
- Updated library paths to actual structure
- Corrected entity locations

**v1.0** (2025-11-19)
- Initial release with 17-section format

---

**END OF PROMPT**
