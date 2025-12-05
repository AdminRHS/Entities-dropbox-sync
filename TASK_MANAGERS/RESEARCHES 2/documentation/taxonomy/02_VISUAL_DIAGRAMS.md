# Taxonomy System: Visual Diagrams and Flowcharts

**Purpose:** Visual representation of taxonomy architecture, workflows, and relationships
**Version:** 1.0.0
**Date:** 2025-12-04

---

## Table of Contents

1. [System Architecture Diagrams](#system-architecture-diagrams)
2. [Video Processing Pipeline](#video-processing-pipeline)
3. [Entity Relationships](#entity-relationships)
4. [Workflow Diagrams](#workflow-diagrams)
5. [Folder Structure Trees](#folder-structure-trees)
6. [Data Flow Diagrams](#data-flow-diagrams)

---

## System Architecture Diagrams

### 1. Complete Taxonomy Ecosystem (High-Level)

```
┌────────────────────────────────────────────────────────────────────┐
│                      REMS/DROPBOX TAXONOMY SYSTEM                  │
│                                                                    │
│  ┌──────────────────────┐      ┌──────────────────────┐          │
│  │   ENTITIES/TAXONOMY   │      │   ENTITIES_2.0/      │          │
│  │   (Central Hub)       │◄────►│   SETTINGS/_Taxonomy │          │
│  │                       │      │   (README Taxonomy)  │          │
│  │  • Navigation         │      │                      │          │
│  │  • Documentation      │      │  • 12 Types          │          │
│  │  • Mirror Views       │      │  • 4 Categories      │          │
│  └───────────┬───────────┘      │  • 80 Tags           │          │
│              │                  └──────────────────────┘          │
│              │                                                     │
│              │                                                     │
│    ┌─────────┴─────────┐                                          │
│    │                   │                                          │
│    ▼                   ▼                                          │
│  ┌────────────────┐  ┌────────────────┐                          │
│  │   LIBRARIES    │  │ TASK_MANAGERS  │                          │
│  │  (CONTENT)     │  │  (WORKFLOW)    │                          │
│  │                │  │                │                          │
│  │  752+ Entities │  │  752+ Entities │                          │
│  └────────────────┘  └────────────────┘                          │
│                                                                    │
│  ┌────────────────────────────────────────────────┐               │
│  │              PROMPTS ENTITY                    │               │
│  │  • 155+ Prompt Files                           │               │
│  │  • 40+ Taxonomy Prompts                        │               │
│  │  • Video Processing Prompts (PMT-004 - PMT-090)│               │
│  └────────────────────────────────────────────────┘               │
└────────────────────────────────────────────────────────────────────┘
```

### 2. LIBRARIES Taxonomy Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIBRARIES ECOSYSTEM                          │
│                    (Content-Focused)                            │
│                                                                 │
│                         DEPARTMENTS                             │
│                              │                                  │
│              ┌───────────────┼───────────────┐                 │
│              │               │               │                 │
│              ▼               ▼               ▼                 │
│         ┌─────────┐    ┌─────────┐    ┌─────────┐             │
│         │  AIA    │    │   DEV   │    │   DGN   │  ...        │
│         │  (AI &  │    │  (Dev)  │    │(Design) │             │
│         │  Auto)  │    │         │    │         │             │
│         └────┬────┘    └────┬────┘    └────┬────┘             │
│              │              │              │                   │
│              └──────┬───────┴───────┬──────┘                   │
│                     │               │                          │
│                     ▼               ▼                          │
│              ┌────────────┐  ┌────────────┐                   │
│              │ PROFESSIONS│  │    TOOLS   │                   │
│              │  (17 PRF)  │  │  (200 TOL) │                   │
│              └─────┬──────┘  └─────┬──────┘                   │
│                    │               │                          │
│         ┌──────────┼───────────────┼──────────┐               │
│         │          │               │          │               │
│         ▼          ▼               ▼          ▼               │
│    ┌────────┐ ┌────────┐     ┌────────┐ ┌────────┐           │
│    │  RSP   │ │  SKL   │     │  OBJ   │ │  ACT   │           │
│    │  (193) │ │  (28+) │     │  (50+) │ │  (429) │           │
│    │Respons.│ │ Skills │     │Objects │ │Actions │           │
│    └────────┘ └────────┘     └────┬───┘ └────┬───┘           │
│                                    │          │               │
│                                    └────┬─────┘               │
│                                         │                     │
│                                         ▼                     │
│                                   ┌──────────┐                │
│                                   │   PRM    │                │
│                                   │  (200+)  │                │
│                                   │Parameters│                │
│                                   └──────────┘                │
│                                                               │
│  Legend:                                                      │
│  RSP = Responsibilities    SKL = Skills        PRM = Parameters│
│  ACT = Actions            OBJ = Objects        TOL = Tools     │
│  PRF = Professions        DPT = Departments                    │
└─────────────────────────────────────────────────────────────────┘
```

### 3. TASK_MANAGERS Taxonomy Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  TASK_MANAGERS ECOSYSTEM                        │
│                   (Workflow-Focused)                            │
│                                                                 │
│                       PROJECT TEMPLATES (PRT-001 to PRT-009)    │
│                                  │                              │
│                                  ▼                              │
│                       MILESTONE TEMPLATES (MLT-001 to MLT-009)  │
│                                  │                              │
│                                  ▼                              │
│                       TASK TEMPLATES (TST-001 to TST-071)       │
│                                  │                              │
│                       ┌──────────┼──────────┐                  │
│                       │          │          │                  │
│                       ▼          ▼          ▼                  │
│              STEP TEMPLATES  CHECKLIST TEMPLATES               │
│              (STT-001 to     (CHT-001 to CHT-098)              │
│               STT-379)                                         │
│                                                                │
│  ┌─────────────────────────────────────────────────────┐      │
│  │          PARALLEL STRUCTURES (Non-Hierarchical)      │      │
│  │                                                      │      │
│  │  WORKFLOWS (WRF-001 to WRF-020)                      │      │
│  │    • Automated process flows                         │      │
│  │    • Linear/Parallel types                           │      │
│  │    • References Task Templates                       │      │
│  │                                                      │      │
│  │  GUIDES (GDS-001+)                                   │      │
│  │    • Documentation guides                            │      │
│  │    • Framework references                            │      │
│  │                                                      │      │
│  │  PROMPTS (PMT-001+, 100+ prompts)                    │      │
│  │    • AI instruction sets                             │      │
│  │    • Taxonomy update drivers                         │      │
│  │                                                      │      │
│  │  RESEARCH (RSR-001+, 50+ items)                      │      │
│  │    • Video analyses                                  │      │
│  │    • Source extractions                              │      │
│  │    • Feeds back to LIBRARIES                         │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                                │
│  Legend:                                                       │
│  PRT = Project Templates    STT = Step Templates              │
│  MLT = Milestone Templates  CHT = Checklist Templates         │
│  TST = Task Templates       WRF = Workflows                   │
│  GDS = Guides              PMT = Prompts        RSR = Research│
└─────────────────────────────────────────────────────────────────┘
```

---

## Video Processing Pipeline

### 1. Complete Video-to-Taxonomy Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    VIDEO TO TAXONOMY PIPELINE                           │
└─────────────────────────────────────────────────────────────────────────┘

     VIDEO SOURCE (YouTube, Loom, etc.)
            │
            │  PMT-004: Video Transcription v4.1
            │  • Transcribe audio to text
            │  • Add timestamps
            │  • Identify speakers
            ▼
     ┌──────────────────────────┐
     │  TRANSCRIPTION FILE      │
     │  Video_XXX.md            │
     │  • Timestamped text      │
     │  • Speaker labels        │
     │  • Duration info         │
     └──────────┬───────────────┘
                │
                │  PMT-006/008: Video Analysis
                │  • Extract tools
                │  • Extract objects
                │  • Extract actions
                │  • Extract workflows
                │  • Extract professions/skills
                ▼
     ┌──────────────────────────┐
     │  STRUCTURED EXTRACTION   │
     │  • Tools list (30 min)   │
     │  • Objects list          │
     │  • Actions list          │
     │  • Workflows list        │
     │  • Professions list      │
     │  • Skills list           │
     └──────────┬───────────────┘
                │
                │  Gap Analysis
                │  • Compare with existing taxonomy
                │  • Identify missing tools (20 min)
                │  • Identify missing objects
                │  • Calculate coverage %
                ▼
     ┌──────────────────────────┐
     │  GAP REPORT              │
     │  ✅ Exists (3 tools)     │
     │  ❌ Missing (7 tools)    │
     │  Coverage: 30% → 100%    │
     └──────────┬───────────────┘
                │
                │  PMT-009: Taxonomy Integration
                │  • Create new JSON files (60-90 min)
                │  • Update existing files
                │  • Assign entity IDs
                ▼
     ┌──────────────────────────────────────────┐
     │  JSON FILES CREATED/UPDATED              │
     ├──────────────────────────────────────────┤
     │  LIBRARIES/Tools/AI_Tools/               │
     │    ├─ GLIF.json (NEW TOL-045)            │
     │    ├─ Sora.json (NEW TOL-046)            │
     │    └─ ElevenLabs.json (UPDATED)          │
     │                                          │
     │  LIBRARIES/Responsibilities/Objects/     │
     │    ├─ Design_Deliverables.json (UPDATED) │
     │    │   └─ Added: thumbnails (OBJ-043)    │
     │    └─ Video_Deliverables.json (NEW)      │
     │        └─ videos (OBJ-044)                │
     │                                          │
     │  TASK_MANAGERS/Workflows/                │
     │    └─ WRF-020_Automated_Documentary.json │
     │                                          │
     │  LIBRARIES/Professions/                  │
     │    ├─ Content_Creator.json (UPDATED)     │
     │    └─ YouTuber.json (NEW PRF-018)        │
     └──────────┬───────────────────────────────┘
                │
                │  Cross-Reference Update (30 min)
                │  • Tool → Object links
                │  • Object → Tool links
                │  • Workflow → All entities
                │  • Profession → All entities
                ▼
     ┌──────────────────────────┐
     │  BIDIRECTIONAL LINKS     │
     │  ESTABLISHED             │
     │                          │
     │  GLIF.json references:   │
     │    • OBJ-043 (thumbnails)│
     │    • OBJ-044 (videos)    │
     │                          │
     │  thumbnails references:  │
     │    • TOL-045 (GLIF)      │
     │    • TOL-046 (NanoBanana)│
     └──────────┬───────────────┘
                │
                │  Master List Update (15 min)
                │  • Add rows to CSV
                │  • Verify no duplicates
                ▼
     ┌──────────────────────────┐
     │  MASTER LISTS UPDATED    │
     │  • Libraries_Master_List │
     │  • Taxonomy_Master_List  │
     └──────────┬───────────────┘
                │
                │  Report Generation (20 min)
                ▼
     ┌──────────────────────────────────────┐
     │  MAPPING REPORT                      │
     │  Video_XXX_Library_Mapping_Report.md │
     │                                      │
     │  • Executive summary                 │
     │  • Tools analysis (before/after)     │
     │  • Objects analysis                  │
     │  • Workflows extracted               │
     │  • Cross-reference summary           │
     │  • Files created/modified list       │
     │  • Business value insights           │
     │  • Recommendations                   │
     └──────────────────────────────────────┘

                    TOTAL TIME: 2.5-4 hours
                    OUTPUT: Complete taxonomy integration
```

### 2. Video Analysis Decision Tree

```
                        START: Video Transcription File
                                      │
                                      ▼
                    ┌─────────────────────────────────┐
                    │  How many tools mentioned?      │
                    └────┬────────────────────────┬───┘
                         │                        │
                    ≤5 tools                  >5 tools
                         │                        │
                         ▼                        ▼
              ┌──────────────────┐    ┌──────────────────┐
              │  Use PMT-006     │    │  Use PMT-009     │
              │  (Quick Analysis)│    │  (Full Workflow) │
              │  30-45 minutes   │    │  2-4 hours       │
              └────┬─────────────┘    └────┬─────────────┘
                   │                       │
                   └───────┬───────────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │  Is this research-focused  │
              │  or integration-focused?   │
              └───┬────────────────────┬───┘
                  │                    │
             Research              Integration
                  │                    │
                  ▼                    ▼
       ┌──────────────────┐   ┌──────────────────┐
       │  Save extractions│   │  Create JSON     │
       │  to 03_ANALYSIS/ │   │  files in proper │
       │  for future use  │   │  taxonomy folders│
       └──────────────────┘   └──────────────────┘
                                       │
                                       ▼
                           ┌──────────────────────┐
                           │  Update master lists │
                           │  Create cross-refs   │
                           │  Generate report     │
                           └──────────────────────┘
```

### 3. ID Assignment Flowchart

```
                     START: Need to Assign New Entity ID
                                      │
                                      ▼
                     ┌────────────────────────────────┐
                     │  What entity type?             │
                     └─┬────┬────┬────┬────┬────┬────┘
                       │    │    │    │    │    │
                  Tool │Object│Action│Workflow│Profession│Skill
                       │    │    │    │    │    │
                       ▼    ▼    ▼    ▼    ▼    ▼
                     TOL  OBJ  ACT  WRF  PRF  SKL
                       │    │    │    │    │    │
                       │    │    │    │    │    │
                       └────┴────┴────┴────┴────┘
                                 │
                                 ▼
              ┌──────────────────────────────────────┐
              │  Open appropriate Master List CSV:   │
              │  • Tools → Libraries_Master_List.csv │
              │  • Workflows → Taxonomy_Master_List  │
              │  • etc.                              │
              └─────────────────┬────────────────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │  Find last ID for entity type:       │
              │  grep "^TOL-" Libraries_Master_List  │
              │  Result: TOL-045                     │
              └─────────────────┬────────────────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │  Assign next sequential ID:          │
              │  Last was TOL-045                    │
              │  Assign: TOL-046                     │
              └─────────────────┬────────────────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │  Create JSON file with assigned ID   │
              │  Example: GLIF.json with TOL-046     │
              └─────────────────┬────────────────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │  Add row to Master List:             │
              │  TOL-046, GLIF, Tool, AIA, ...       │
              └─────────────────┬────────────────────┘
                                │
                                ▼
              ┌──────────────────────────────────────┐
              │  Update ISO Code Registry (if new    │
              │  category or department code needed) │
              └─────────────────┬────────────────────┘
                                │
                                ▼
                              DONE
```

---

## Entity Relationships

### 1. Complete Entity Relationship Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│                     ENTITY RELATIONSHIPS                               │
└────────────────────────────────────────────────────────────────────────┘

                         DEPARTMENTS (DPT)
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                    ▼          ▼          ▼
              ┌─────────┐ ┌─────────┐ ┌─────────┐
              │  AIA    │ │  DEV    │ │  DGN    │  ...
              └────┬────┘ └────┬────┘ └────┬────┘
                   │           │           │
                   └─────┬─────┴─────┬─────┘
                         │           │
                         ▼           ▼
                   PROFESSIONS (PRF)
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  RESPONSIBILITIES   SKILLS (SKL)    TOOLS (TOL)
      (RSP)              │                │
                         │                │
                         └───────┬────────┘
                                 │
                      ┌──────────┼──────────┐
                      │          │          │
                      ▼          ▼          ▼
                 OBJECTS     ACTIONS    WORKFLOWS
                  (OBJ)       (ACT)       (WRF)
                      │          │          │
                      └──────────┼──────────┘
                                 │
                                 ▼
                           PARAMETERS (PRM)

RELATIONSHIP TYPES:
═══════════════════

Department → Profession:    "owns/contains"
Profession → Tools:         "uses"
Profession → Objects:       "works with"
Profession → Responsibilities: "performs"
Profession → Skills:        "requires"
Profession → Workflows:     "executes"

Tools → Objects:           "creates"
Objects → Tools:           "created by"

Actions → Objects:         "acts upon"
Objects → Actions:         "receives action"

Workflows → Tools:         "uses in steps"
Workflows → Objects:       "produces/consumes"
Workflows → Actions:       "performs"
Workflows → Professions:   "executed by"

Skills → Tools:            "involves using"
Skills → Actions:          "involves performing"
Skills → Objects:          "involves working with"

Parameters → Objects:      "configures"
```

### 2. Tool-Object-Action Triangle

```
                            TOOL (TOL)
                          (e.g., GLIF)
                               │
                               │ "uses"
                               │
                               ▼
        ┌──────────────────────────────────────┐
        │          performs ACTION             │
        │              (ACT)                   │
        │         (e.g., Generate)             │
        └──────────┬────────────────┬──────────┘
                   │                │
         "creates" │                │ "acts upon"
                   │                │
                   ▼                ▼
              OBJECT (OBJ)      OBJECT (OBJ)
            (e.g., videos)    (e.g., thumbnails)
                   │                │
                   └────────┬───────┘
                            │
                   "worked with by"
                            │
                            ▼
                    PROFESSION (PRF)
                  (e.g., Content Creator)

EXAMPLE CHAIN:
═════════════
GLIF (TOL-045)
  └─ generates (ACT-042)
       └─ videos (OBJ-044)
            └─ worked with by Content Creator (PRF-012)
                 └─ requires skill: Workflow Automation (SKL-022)
```

### 3. Workflow Entity Integration Map

```
                         WORKFLOW (WRF-002)
                "Automated Documentary Creation"
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                  │
           ▼                  ▼                  ▼
     USES TOOLS         PRODUCES OBJECTS    PERFORMED BY
           │                  │                  │
    ┌──────┴──────┐    ┌──────┴──────┐    ┌──────┴──────┐
    │             │    │             │    │             │
    ▼             ▼    ▼             ▼    ▼             ▼
  TOL-045      TOL-046  OBJ-044    OBJ-045  PRF-012   PRF-015
  (GLIF)       (VAYU)  (videos)   (scripts) (Creator) (Producer)
    │             │      │           │        │           │
    └─────┬───────┘      └─────┬─────┘        └─────┬─────┘
          │                    │                    │
          ▼                    ▼                    ▼
    INVOLVES ACTIONS    CONFIGURED BY         REQUIRES SKILLS
          │              PARAMETERS                 │
    ┌─────┴─────┐            │              ┌─────┴─────┐
    │           │            ▼              │           │
    ▼           ▼        PRM-001...     ▼           ▼
  ACT-042    ACT-051      (params)      SKL-022    SKL-025
  (Generate) (Combine)                  (Workflow) (Prompt Eng.)

BIDIRECTIONAL LINKS:
═══════════════════
WRF-002 → TOL-045 (uses)          TOL-045 → WRF-002 (used in)
WRF-002 → OBJ-044 (produces)      OBJ-044 → WRF-002 (produced by)
WRF-002 → PRF-012 (executed by)   PRF-012 → WRF-002 (executes)
WRF-002 → ACT-042 (performs)      ACT-042 → WRF-002 (performed in)
WRF-002 → SKL-022 (requires)      SKL-022 → WRF-002 (required by)
```

---

## Workflow Diagrams

### 1. Automated Documentary Creation Workflow (WRF-002)

```
┌────────────────────────────────────────────────────────────────────┐
│         Automated Miniature Documentary Creation Workflow          │
│                        (10-20 minutes)                             │
└────────────────────────────────────────────────────────────────────┘

INPUT: Historical topic name (e.g., "Ancient Rome")
   │
   │
   ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 1: Research Historical Facts                        │
│ Tool: Perplexity (TOL-###)                               │
│ Action: Research (ACT-###)                               │
│ Duration: 2-3 minutes (automated)                        │
│ Output: Verified historical facts (3-5 paragraphs)       │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 2: Generate Documentary Script                      │
│ Tool: ChatGPT / AI in GLIF (TOL-###)                     │
│ Action: Generate (ACT-042)                               │
│ Duration: 1-2 minutes (automated)                        │
│ Output: 32-second script (80-100 words)                  │
│ Object Created: scripts (OBJ-045)                        │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 3: Create Tilt-Shift Video                          │
│ Tool: VAYU 2.2 + Seedream (TOL-046, TOL-047)             │
│ Action: Create (ACT-001)                                 │
│ Duration: 3-5 minutes (automated)                        │
│ Output: 32-second tilt-shift video (no audio)            │
│ Object Created: videos [partial] (OBJ-044)               │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 4: Generate Voiceover Narration                     │
│ Tool: Eleven Labs (TOL-###)                              │
│ Action: Generate (ACT-042)                               │
│ Duration: 1-2 minutes (automated)                        │
│ Output: Professional narration (32 sec, MP3)             │
│ Object Created: voiceovers (OBJ-046)                     │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 5: Combine Video and Audio                          │
│ Tool: GLIF (TOL-045) - Automation                        │
│ Action: Combine (ACT-051)                                │
│ Duration: 1-2 minutes (automated)                        │
│ Output: Final documentary video (MP4, 32 sec)            │
│ Object Created: videos [complete] (OBJ-044)              │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 6: Review and Publish                               │
│ Tool: Manual (human review)                              │
│ Action: Review, Publish (ACT-###, ACT-###)               │
│ Duration: 2-5 minutes (manual)                           │
│ Output: Published content on platforms                   │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
           FINAL OUTPUT
   32-second miniature documentary
   Published on TikTok, Instagram, YouTube

═══════════════════════════════════════════════════════════
AUTOMATION: 83% (5 of 6 steps automated)
MANUAL: 17% (1 step - review and publish)
PROFESSIONS: Content Creator, Video Producer, Documentary Producer
DEPARTMENTS: VID;AID
BUSINESS VALUE: 10x faster than manual production
═══════════════════════════════════════════════════════════
```

### 2. YouTube Thumbnail Creation Workflow (WRF-003)

```
┌────────────────────────────────────────────────────────────────────┐
│            YouTube Thumbnail Creation (High CTR)                   │
│                        (15 minutes)                                │
└────────────────────────────────────────────────────────────────────┘

INPUT: Video concept, style reference
   │
   │
   ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 1: Define Thumbnail Concept                         │
│ Tool: Manual (brainstorming)                             │
│ Action: Define, Plan                                     │
│ Duration: 3-5 minutes (manual)                           │
│ Output: Concept description + style reference            │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 2: Generate Image                                   │
│ Tool: Nano Banana via GLIF (TOL-046, TOL-045)            │
│ Action: Generate (ACT-042)                               │
│ Duration: 2-3 minutes (automated)                        │
│ Output: 4-6 thumbnail variants (1920x1080)               │
│ Object Created: thumbnails [draft] (OBJ-043)             │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 3: Refine Prompt for Style                          │
│ Tool: Nano Banana (TOL-046)                              │
│ Action: Refine (ACT-###)                                 │
│ Duration: 3-5 minutes (semi-automated)                   │
│ Output: Refined thumbnails matching style                │
│ Skill Used: Prompt Engineering (SKL-022)                 │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 4: Select Best Variant                              │
│ Tool: Manual (human judgment)                            │
│ Action: Select, Review (ACT-###)                         │
│ Duration: 2-3 minutes (manual)                           │
│ Output: Best thumbnail selected                          │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 5: Add Text Overlay (Optional)                      │
│ Tool: Photo editor / Canva (TOL-025)                     │
│ Action: Add, Design (ACT-###)                            │
│ Duration: 2-4 minutes (manual)                           │
│ Output: Thumbnail with text                              │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ STEP 6: Export Final Thumbnail                           │
│ Tool: Image editor                                       │
│ Action: Export (ACT-###)                                 │
│ Duration: 1 minute (manual)                              │
│ Output: Final thumbnail (PNG, 1920x1080)                 │
│ Object Created: thumbnails [final] (OBJ-043)             │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
           FINAL OUTPUT
   YouTube thumbnail (1920x1080 PNG)
   Optimized for high CTR

═══════════════════════════════════════════════════════════
AUTOMATION: 33% (2 of 6 steps automated)
MANUAL: 67% (4 steps)
PROFESSIONS: Content Creator, YouTuber, Graphic Designer
DEPARTMENTS: VID;DGN
OPTIMIZATION METRICS: CTR (click-through rate), engagement
═══════════════════════════════════════════════════════════
```

---

## Folder Structure Trees

### 1. Complete Taxonomy Folder Tree

```
G:\Job\REMS\Dropbox\
│
├── ENTITIES/
│   │
│   ├── TAXONOMY/ ◄─── CENTRAL HUB
│   │   ├── README.md (navigation hub)
│   │   │
│   │   ├── TAX-001_Libraries/ (LIBRARIES taxonomy)
│   │   │   ├── Libraries_Master_List.csv ◄─── All LIBRARIES entities
│   │   │   ├── Libraries_ISO_Code_Registry.md ◄─── Code definitions
│   │   │   ├── Libraries_Hierarchy_Tree.md
│   │   │   ├── Libraries_Department_Distribution.md
│   │   │   ├── Libraries_Migration_Map.json
│   │   │   ├── Tools_Master_List.csv
│   │   │   └── Tools_Master_Priority.json
│   │   │
│   │   ├── TAX-002_Task_Managers/ (TASK_MANAGERS taxonomy)
│   │   │   ├── Taxonomy_Master_List.csv ◄─── All TASK_MANAGERS entities
│   │   │   ├── Taxonomy_ISO_Code_Registry.md ◄─── Code definitions
│   │   │   ├── Taxonomy_Hierarchy_Tree.md
│   │   │   ├── Taxonomy_Department_Distribution.md
│   │   │   └── Taxonomy_Migration_Map.json
│   │   │
│   │   ├── TAX-003_Video_Processing/
│   │   │   └── PMT-009_Taxonomy_Integration.md ◄─── Complete workflow
│   │   │
│   │   └── TAX-004_Entity_Integration/
│   │       └── Entity_Integration_Taxonomy.md ◄─── 6-step integration
│   │
│   ├── LIBRARIES/ ◄─── CANONICAL SOURCE (Content-focused)
│   │   │
│   │   ├── Responsibilities/
│   │   │   ├── Actions/
│   │   │   │   ├── Actions_Master.json ◄─── 429 verbs
│   │   │   │   ├── ACT-CMD/ (Command verbs: Create, Update, Delete)
│   │   │   │   ├── ACT-PRC/ (Process verbs: Analyze, Transform)
│   │   │   │   └── ACT-RST/ (Result verbs: Generate, Produce)
│   │   │   │
│   │   │   ├── Objects/
│   │   │   │   ├── Design_Deliverables.json ◄─── thumbnails, etc.
│   │   │   │   ├── Video_Deliverables.json ◄─── videos, etc.
│   │   │   │   ├── Documents.json
│   │   │   │   └── [More object files by domain]
│   │   │   │
│   │   │   └── Responsibilities_Master.json ◄─── 193 responsibilities
│   │   │
│   │   ├── Tools/
│   │   │   ├── AI_Tools/ ◄─── 80+ tool files
│   │   │   │   ├── GLIF.json (TOL-045)
│   │   │   │   ├── Claude.json
│   │   │   │   ├── ChatGPT.json
│   │   │   │   ├── Midjourney.json
│   │   │   │   ├── Nano_Banana.json (TOL-046)
│   │   │   │   ├── VAYU.json (TOL-047)
│   │   │   │   └── [80+ more tool files]
│   │   │   │
│   │   │   └── Tools_Master_List.csv
│   │   │
│   │   ├── Skills/
│   │   │   ├── Master/
│   │   │   │   └── all_skills.json ◄─── 28+ skills
│   │   │   │
│   │   │   └── By_Department/
│   │   │       ├── AIA_Skills.json
│   │   │       ├── DEV_Skills.json
│   │   │       ├── DGN_Skills.json
│   │   │       └── VID_Skills.json
│   │   │
│   │   ├── Professions/ ◄─── 17 profession files
│   │   │   ├── Content_Creator.json (PRF-012)
│   │   │   ├── YouTuber.json (PRF-018)
│   │   │   ├── Graphic_Designer.json
│   │   │   ├── Video_Producer.json
│   │   │   └── [13 more profession files]
│   │   │
│   │   └── Taxonomy/ ◄─── Canonical taxonomy files (mirror to TAX-001)
│   │       ├── Libraries_Master_List.csv
│   │       ├── Libraries_ISO_Code_Registry.md
│   │       └── [Other taxonomy files]
│   │
│   ├── TASK_MANAGERS/ ◄─── CANONICAL SOURCE (Workflow-focused)
│   │   │
│   │   ├── Project_Templates/ ◄─── 9 projects
│   │   │   ├── PRT-001_AI_Tutorial_Research.json
│   │   │   └── [8 more project files]
│   │   │
│   │   ├── Milestone_Templates/ ◄─── 9 milestones
│   │   │   ├── MLT-001_Discovery.json
│   │   │   └── [8 more milestone files]
│   │   │
│   │   ├── Task_Templates/ ◄─── 71 tasks
│   │   │   ├── TST-001_AI_Powered_HTML_Parsing.json
│   │   │   ├── TST-042_Onboard_New_Employee.json
│   │   │   └── [69 more task files]
│   │   │
│   │   ├── Step_Templates/ ◄─── 379 steps
│   │   │   └── By_Department/
│   │   │       ├── AID_Steps/
│   │   │       ├── DEV_Steps/
│   │   │       ├── DGN_Steps/
│   │   │       └── VID_Steps/
│   │   │
│   │   ├── Checklist_Templates/ ◄─── 98 checklists
│   │   │
│   │   ├── Workflows/ ◄─── 20 workflows
│   │   │   ├── WRF-001_Lead_Enrichment.json
│   │   │   ├── WRF-002_Automated_Documentary_Creation.json
│   │   │   ├── WRF-003_YouTube_Thumbnail_Optimization.json
│   │   │   └── [17 more workflow files]
│   │   │
│   │   ├── Guides/ ◄─── 8+ guides
│   │   │   ├── GDS-001_Taxonomy_Guide.md
│   │   │   └── [7+ more guide files]
│   │   │
│   │   ├── PROMPTS/ ◄─── 100+ prompts
│   │   │   ├── PMT-001_Main_Prompt.md
│   │   │   ├── PMT-004_Video_Transcription.md
│   │   │   ├── PMT-009_Taxonomy_Integration.md
│   │   │   └── [100+ more prompt files]
│   │   │
│   │   ├── RESEARCHES/ [or RESEARCHES 2/] ◄─── Video analysis
│   │   │   ├── 00_SEARCH_QUEUE/ (search assignments)
│   │   │   ├── 01_VIDEO_QUEUE/ (video prioritization)
│   │   │   ├── 02_TRANSCRIPTIONS/ ◄─── 23 video transcriptions
│   │   │   │   ├── Video_001.md
│   │   │   │   ├── Video_002.md
│   │   │   │   └── [21 more transcription files]
│   │   │   │
│   │   │   ├── 03_ANALYSIS/ ◄─── Extractions and reports
│   │   │   │   ├── Video_001_Library_Mapping_Report.md
│   │   │   │   ├── Video_002_Gap_Analysis.md
│   │   │   │   └── [Analysis files]
│   │   │   │
│   │   │   ├── 04_INTEGRATION/ (integration tracking)
│   │   │   ├── PROMPTS/ (26 research prompts)
│   │   │   ├── DATA/ (research data)
│   │   │   ├── REPORTS/ (research reports)
│   │   │   │
│   │   │   └── documentation/ ◄─── Documentation files
│   │   │       ├── v1/
│   │   │       ├── v2/
│   │   │       ├── taxonomy_complete_guide.md ◄─── Complete guide
│   │   │       ├── TAXONOMY_QUICK_START.md ◄─── Quick reference
│   │   │       └── taxonomy/ ◄─── Additional documentation
│   │   │           ├── 01_VIDEO_TAXONOMY_STEP_BY_STEP.md
│   │   │           ├── 02_VISUAL_DIAGRAMS.md (THIS FILE)
│   │   │           └── [More documentation files]
│   │   │
│   │   └── Taxonomy/ ◄─── Canonical taxonomy files (mirror to TAX-002)
│   │       ├── Taxonomy_Master_List.csv
│   │       ├── Taxonomy_ISO_Code_Registry.md
│   │       └── [Other taxonomy files]
│   │
│   └── PROMPTS/ ◄─── CANONICAL SOURCE FOR PROMPTS
│       ├── Core/
│       │   ├── PMT-001_Main_Prompt_v4.md
│       │   └── PMT-003_Create_Main_Prompt_v5.md
│       │
│       ├── PMT-004_Video_Transcription_v4.1.md ◄─── Transcription
│       ├── PMT-005_Video_Naming_Alternatives.md
│       ├── PMT-006_Video_Analysis.md ◄─── Analysis
│       ├── PMT-007_Objects_Library_Extraction.md
│       ├── PMT-008_Video_Analysis_Improvements.md
│       ├── PMT-009_Taxonomy_Integration.md ◄─── Complete workflow
│       ├── PMT-015_Optimize_Video_Transcription.md
│       └── PMT-090_YouTube_Video_Processing.md
│
├── ENTITIES_2.0/ (NEW STRUCTURE)
│   │
│   └── SETTINGS/
│       └── _Taxonomy/ ◄─── README Taxonomy
│           ├── TAX-RDM-001_Types.md ◄─── 12 README types
│           ├── TAX-RDM-002_Categories.md ◄─── 4 categories
│           └── TAX-RDM-003_Tags.md ◄─── 80 tags
│
└── Design Nov25/
    └── Safonova Eleonora/
        └── Safonova Eleonora/
            └── AdminRHS-AI-Catalog-4/
                └── scripts/
                    └── taxonomy_lookup.js ◄─── Taxonomy lookup script

═══════════════════════════════════════════════════════════════════
KEY:
  ◄─── = Important file/folder
  (###) = Quantity/ID format
  / = Folder
  .json, .md, .csv = File types
═══════════════════════════════════════════════════════════════════
```

---

## Data Flow Diagrams

### 1. Complete System Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA FLOW: COMPLETE SYSTEM                      │
└─────────────────────────────────────────────────────────────────────┘

                          EXTERNAL SOURCES
                    (Videos, Documents, Interviews)
                                  │
                                  │ [Raw Data]
                                  ▼
                     ╔════════════════════════╗
                     ║  RESEARCH & PROMPTS    ║
                     ║  TASK_MANAGERS/        ║
                     ║  RESEARCHES/           ║
                     ╚═══════════┬════════════╝
                                 │
                                 │ [Transcriptions]
                                 │ [Extractions]
                                 ▼
                     ╔════════════════════════╗
                     ║  TAXONOMY ENTITY       ║
                     ║  (Central Hub)         ║
                     ║  • Master Lists        ║
                     ║  • ISO Registries      ║
                     ╚═══════════┬════════════╝
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                    ▼            ▼            ▼
         ╔═══════════════╗ ╔═══════════════╗ ╔═══════════════╗
         ║   LIBRARIES   ║ ║TASK_MANAGERS  ║ ║   PROMPTS     ║
         ║  (Content)    ║ ║  (Workflow)   ║ ║(Instructions) ║
         ╚═══════╦═══════╝ ╚═══════╦═══════╝ ╚═══════╦═══════╝
                 │                 │                 │
                 │ [IDs, Data]     │ [Templates]     │ [Prompts]
                 │                 │                 │
                 └────────┬────────┴────────┬────────┘
                          │                 │
                          │ [Cross-Refs]    │
                          ▼                 ▼
                     ╔═══════════════════════════╗
                     ║  APPLICATIONS             ║
                     ║  • AI Tools Catalog       ║
                     ║  • Team Dashboards        ║
                     ║  • Workflow Automation    ║
                     ║  • Knowledge Graphs       ║
                     ╚═══════════════════════════╝
                                  │
                                  │ [Generated Content]
                                  │ [Automated Workflows]
                                  ▼
                          BUSINESS OUTPUTS
                    (Tools Usage, Content Creation)

DATA TYPES:
═══════════
→ Structured Data (JSON, CSV)
─ Unstructured Data (Markdown, Text)
═ Configuration/Metadata
╦ Hierarchical Relationships
```

### 2. Video Analysis Data Flow (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                VIDEO ANALYSIS DATA FLOW (DETAILED)                  │
└─────────────────────────────────────────────────────────────────────┘

                           VIDEO SOURCE
                        (YouTube, Loom, etc.)
                                │
                                │ [Audio/Video]
                                ▼
                    ┌───────────────────────┐
                    │  PMT-004:             │
                    │  Video Transcription  │
                    │  (30-60 min)          │
                    └───────────┬───────────┘
                                │
                                │ [Markdown File]
                                │ Video_XXX.md
                                ▼
                    ┌───────────────────────┐
                    │  02_TRANSCRIPTIONS/   │
                    │  Video_XXX.md         │
                    │  • Timestamps         │
                    │  • Speaker labels     │
                    │  • Full text          │
                    └───────────┬───────────┘
                                │
                                │ [Read file]
                                ▼
                    ┌───────────────────────┐
                    │  PMT-006/008/009:     │
                    │  Video Analysis       │
                    │  (30-90 min)          │
                    └───────────┬───────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
        ┌──────────────────┐    ┌──────────────────┐
        │ TOOLS EXTRACTION │    │OBJECTS EXTRACTION│
        │ • Tool names     │    │ • Object names   │
        │ • Categories     │    │ • Types          │
        │ • Timestamps     │    │ • Tools used     │
        │ • Use cases      │    │ • Professions    │
        └──────┬───────────┘    └──────┬───────────┘
               │                       │
               │                       │
               ▼                       ▼
    ┌──────────────────┐    ┌──────────────────┐
    │ACTIONS EXTRACTION│    │WORKFLOW EXTRACT. │
    │ • Verbs          │    │ • Steps          │
    │ • Categories     │    │ • Tools          │
    │ • Contexts       │    │ • Duration       │
    └──────┬───────────┘    └──────┬───────────┘
           │                       │
           │                       │
           ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│PROFESSION EXTRACT│    │  SKILL EXTRACT.  │
│ • Roles          │    │  • Skill names   │
│ • Responsibilities│   │  • Applications  │
│ • Tools used     │    │  • Proficiency   │
└──────┬───────────┘    └──────┬───────────┘
       │                       │
       └───────────┬───────────┘
                   │
                   │ [All Extractions]
                   ▼
       ┌───────────────────────┐
       │  03_ANALYSIS/         │
       │  Working_Notes.md     │
       │  • Complete inventory │
       │  • Gap analysis       │
       └───────────┬───────────┘
                   │
                   │ [Gap Report]
                   ▼
       ┌───────────────────────┐
       │  GAP ANALYSIS         │
       │  • Exists: 30%        │
       │  • Missing: 70%       │
       │  • Priority: Critical │
       └───────────┬───────────┘
                   │
                   │ [Create/Update]
                   ▼
       ╔═══════════════════════╗
       ║  JSON FILE CREATION   ║
       ╠═══════════════════════╣
       ║ LIBRARIES/Tools/      ║
       ║   GLIF.json (NEW)     ║
       ║   TOL-045             ║
       ║                       ║
       ║ LIBRARIES/Objects/    ║
       ║   thumbnails (ADD)    ║
       ║   OBJ-043             ║
       ║                       ║
       ║ TASK_MANAGERS/        ║
       ║ Workflows/            ║
       ║   WRF-002 (NEW)       ║
       ╚═══════════╦═══════════╝
                   │
                   │ [Cross-Reference]
                   ▼
       ┌───────────────────────┐
       │ BIDIRECTIONAL LINKING │
       │ Tool → Object         │
       │ Object → Tool         │
       │ Workflow → All        │
       │ Profession → All      │
       └───────────┬───────────┘
                   │
                   │ [Update Master Lists]
                   ▼
       ┌───────────────────────┐
       │ MASTER LIST UPDATES   │
       │ Libraries_Master_List │
       │ Taxonomy_Master_List  │
       └───────────┬───────────┘
                   │
                   │ [Generate Report]
                   ▼
       ┌───────────────────────┐
       │ 03_ANALYSIS/          │
       │ Video_XXX_Library_    │
       │ Mapping_Report.md     │
       │ • Summary             │
       │ • Files changed       │
       │ • Coverage metrics    │
       └───────────────────────┘

TOTAL TIME: 2.5-4 hours
OUTPUT FILES: 5-15 JSON files + 1 report
```

### 3. Cross-Reference Update Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                  CROSS-REFERENCE UPDATE FLOW                        │
└─────────────────────────────────────────────────────────────────────┘

                    NEW TOOL CREATED: GLIF (TOL-045)
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │ Tool File: GLIF.json     │
                    │ References:              │
                    │  • thumbnails (OBJ-043)  │
                    │  • videos (OBJ-044)      │
                    │  • scripts (OBJ-045)     │
                    └──────────┬───────────────┘
                               │
               ┌───────────────┼───────────────┐
               │               │               │
               ▼               ▼               ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────┐
    │UPDATE           │ │UPDATE       │ │UPDATE       │
    │thumbnails       │ │videos       │ │scripts      │
    │(OBJ-043)        │ │(OBJ-044)    │ │(OBJ-045)    │
    │                 │ │             │ │             │
    │Add to tools:    │ │Add to tools:│ │Add to tools:│
    │• GLIF (TOL-045) │ │• GLIF       │ │• GLIF       │
    │  "orchestration"│ │  "combine"  │ │  "generate" │
    └─────────┬───────┘ └──────┬──────┘ └──────┬──────┘
              │                │               │
              └────────┬───────┴───────┬───────┘
                       │               │
                       ▼               ▼
            ┌──────────────────────────────────┐
            │ PROFESSION FILES UPDATE          │
            │ Content_Creator.json             │
            │ Add to tools_used:               │
            │  • GLIF (TOL-045)                │
            │    Purpose: "Workflow automation"│
            │    Frequency: "Daily"            │
            │                                  │
            │ Add to workflows_performed:      │
            │  • WRF-002 (Automated Doc)       │
            └──────────────┬───────────────────┘
                           │
                           ▼
            ┌──────────────────────────────────┐
            │ WORKFLOW FILES UPDATE            │
            │ WRF-002_Automated_Documentary.json│
            │ Add to tools_used:               │
            │  • TOL-045 (GLIF)                │
            │    Role: "Orchestration"         │
            │                                  │
            │ Add to objects_created:          │
            │  • OBJ-044 (videos)              │
            └──────────────┬───────────────────┘
                           │
                           ▼
            ┌──────────────────────────────────┐
            │ VALIDATION                       │
            │ Check bidirectional links:       │
            │ ✓ GLIF → thumbnails             │
            │ ✓ thumbnails → GLIF             │
            │ ✓ GLIF → videos                 │
            │ ✓ videos → GLIF                 │
            │ ✓ Content_Creator → GLIF        │
            │ ✓ GLIF → workflows (via usage)  │
            │ ✓ WRF-002 → GLIF                │
            └──────────────────────────────────┘

RESULT: All entities properly cross-referenced
        Bidirectional navigation enabled
```

---

## Legend for All Diagrams

```
┌─────────────────────────────────────────────────────────────┐
│                    DIAGRAM SYMBOLS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BOXES:                                                     │
│  ┌─────┐  Standard box (process, entity, file)             │
│  │     │                                                    │
│  └─────┘                                                    │
│                                                             │
│  ╔═════╗  Important/emphasis box                           │
│  ║     ║                                                    │
│  ╚═════╝                                                    │
│                                                             │
│  ARROWS:                                                    │
│  →  Standard data flow                                     │
│  ▼  Downward flow                                          │
│  ◄  Backward reference                                     │
│  ═  Bidirectional flow                                     │
│  ├─ Branch/split                                           │
│  └─ Connection                                             │
│                                                             │
│  STATUS MARKERS:                                           │
│  ✓ or ✅  Completed/Exists                                 │
│  ✗ or ❌  Missing/To Create                                │
│  ⏳  In Progress                                           │
│  ⬜  Not Started                                           │
│  📋  Queued                                                │
│                                                             │
│  LABELS:                                                   │
│  (###)  Quantity or ID pattern                             │
│  [text] Description or data type                           │
│  "text" Quoted text or exact phrase                        │
│  ◄─── Important marker (points to key item)                │
│                                                             │
│  ENTITY CODES:                                             │
│  TOL-### Tool ID                                           │
│  OBJ-### Object ID                                         │
│  ACT-### Action ID                                         │
│  WRF-### Workflow ID                                       │
│  PRF-### Profession ID                                     │
│  SKL-### Skill ID                                          │
│  PRT-### Project Template ID                               │
│  MLT-### Milestone Template ID                             │
│  TST-### Task Template ID                                  │
│  PMT-### Prompt ID                                         │
│  RSR-### Research ID                                       │
│                                                             │
│  DEPARTMENT CODES:                                         │
│  AIA/AID AI & Automation                                   │
│  DEV     Development                                       │
│  DGN     Design                                            │
│  VID     Video Production                                  │
│  HRM     Human Resources                                   │
│  LGN     Lead Generation                                   │
│  SLS     Sales                                             │
│  SMM     Social Media Management                           │
│  FIN     Finance                                           │
└─────────────────────────────────────────────────────────────┘
```

---

**Document End**

**Created:** 2025-12-04
**Version:** 1.0.0
**Location:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\taxonomy\02_VISUAL_DIAGRAMS.md`
**Related:** `taxonomy_complete_guide.md`, `01_VIDEO_TAXONOMY_STEP_BY_STEP.md`
