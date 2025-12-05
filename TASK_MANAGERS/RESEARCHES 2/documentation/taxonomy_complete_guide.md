# Complete Taxonomy System Documentation
## Video Taxonomy Generation, Usage, and Management Guide

**Document Version:** 1.0.0
**Created:** 2025-12-04
**Last Updated:** 2025-12-04
**Status:** Active - Comprehensive Guide
**Author:** System Analysis & Documentation Team

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [What is Taxonomy in REMS/Dropbox](#what-is-taxonomy)
3. [Taxonomy Architecture](#taxonomy-architecture)
4. [Video Taxonomy System](#video-taxonomy-system)
5. [How to Generate Taxonomy](#how-to-generate-taxonomy)
6. [How to Update Taxonomy](#how-to-update-taxonomy)
7. [Taxonomy Scripts and Tools](#taxonomy-scripts-and-tools)
8. [Prompts Library](#prompts-library)
9. [Information Captured by Taxonomy](#information-captured)
10. [Folder Structure](#folder-structure)
11. [Usage Examples](#usage-examples)
12. [Best Practices](#best-practices)
13. [Troubleshooting](#troubleshooting)

---

## Executive Summary

The REMS/Dropbox taxonomy system is a sophisticated, multi-layered classification framework that organizes **all knowledge, workflows, tools, and processes** across the organization. It enables:

- **Consistent classification** of entities across all departments
- **Automated workflow routing** based on taxonomy metadata
- **Cross-entity linking** for knowledge graphs
- **AI-friendly data processing** for intelligent automation
- **Video-to-taxonomy pipeline** for knowledge extraction from video content

**Key Statistics:**
- **2 primary taxonomies:** LIBRARIES (content/objects) and TASK_MANAGERS (workflows/templates)
- **752+ classified entities** across 10 entity types
- **421 task templates** aligned with taxonomy structure
- **80+ tags** for flexible README classification
- **40+ prompts** dedicated to taxonomy analysis and updates
- **Complete video processing pipeline** from transcription to taxonomy integration

---

## What is Taxonomy in REMS/Dropbox

### Core Concept

Taxonomy in REMS/Dropbox is a **standardized ID and classification system** that:

1. **Assigns unique identifiers** to all entities (tools, objects, actions, workflows, etc.)
2. **Creates hierarchical relationships** between entities
3. **Enables cross-referencing** across the entire system
4. **Supports AI-driven automation** through consistent structure
5. **Extracts knowledge** from unstructured sources (videos, documents, research)

### Three-Letter ISO Code System

All entities use a **consonant-only 3-letter ISO code** for identification:

**LIBRARIES Entity Codes:**
- **RSP** = Responsibilities (193 core items)
- **ACT** = Actions (429 verbs)
- **OBJ** = Objects (50+ deliverables)
- **PRM** = Parameters (200+)
- **TOL** = Tools (200+)
- **SKL** = Skills (28+)
- **PRF** = Professions (17)
- **DPT** = Departments (10)

**TASK_MANAGERS Entity Codes:**
- **PRT** = Project Templates (9)
- **MLT** = Milestone Templates (9)
- **TST** = Task Templates (71)
- **STT** = Step Templates (379)
- **CHT** = Checklist Templates (98)
- **WRF** = Workflows (20)
- **GDS** = Guides (8+)
- **PMT** = Prompts (100+)
- **RSR** = Research (50+)

**Department Codes (Shared Across All Entities):**
- **AIA** (or **AID**) = AI & Automation
- **DEV** = Development
- **HRM** = Human Resources
- **LGN** = Lead Generation
- **DGN** = Design
- **VID** = Video Production
- **SLS** = Sales
- **SMM** = Social Media Management
- **FIN** = Finance

### Why Consonant-Only?

- **Uniqueness:** Reduces collision risk
- **Memorability:** Easier to remember patterns
- **Consistency:** Standard across all taxonomies
- **AI-Friendly:** Predictable structure for automation

---

## Taxonomy Architecture

### 1. TAXONOMY Entity (Central Hub)

**Location:** `ENTITIES/TAXONOMY/`

**Purpose:** Central navigation hub and documentation layer for all taxonomy systems

**Sub-Entities:**

#### TAX-001: LIBRARIES Taxonomy
**Location:** `ENTITIES/TAXONOMY/TAX-001_Libraries/`

**Files:**
- `Libraries_Master_List.csv` - Master catalog of all library entities
- `Libraries_ISO_Code_Registry.md` - ISO code definitions and rules
- `Libraries_Hierarchy_Tree.md` - Hierarchical relationships
- `Libraries_Department_Distribution.md` - Statistics by department
- `Libraries_Migration_Map.json` - Legacy ID mappings
- `Tools_Master_List.csv` - Comprehensive tools inventory
- `Tools_Master_Priority.json` - Tool priority rankings

**Canonical Source:** `ENTITIES/LIBRARIES/Taxonomy/`

#### TAX-002: TASK_MANAGERS Taxonomy
**Location:** `ENTITIES/TAXONOMY/TAX-002_Task_Managers/`

**Files:**
- `Taxonomy_Master_List.csv` - Catalog of projects, milestones, tasks, workflows
- `Taxonomy_ISO_Code_Registry.md` - ISO codes and department codes
- `Taxonomy_Hierarchy_Tree.md` - Project → Milestone → Task hierarchy
- `Taxonomy_Department_Distribution.md` - Department statistics
- `Taxonomy_Migration_Map.json` - Migration mappings

**Canonical Source:** `ENTITIES/TASK_MANAGERS/Taxonomy/`

#### TAX-003: Video Processing Taxonomy
**Location:** `ENTITIES/TAXONOMY/TAX-003_Video_Processing/`

**File:**
- `PMT-009_Taxonomy_Integration.md` - Complete video transcription to taxonomy integration workflow

**Canonical Source:** `ENTITIES/PROMPTS/PROMPTS/Taxonomy_Integration/`

#### TAX-004: Entity Integration Taxonomy
**Location:** `ENTITIES/TAXONOMY/TAX-004_Entity_Integration/`

**File:**
- `Entity_Integration_Taxonomy.md` - Standard 6-step workflow for integrating new entities

**Purpose:** Define standard process for adding new entity types to the system

#### TAX-005: README Taxonomy (ENTITIES_2.0)
**Location:** `ENTITIES_2.0/SETTINGS/_Taxonomy/`

**Files:**
- `TAX-RDM-001_Types.md` - 12 README types across 4 categories
- `TAX-RDM-002_Categories.md` - 4 major categories for organizing READMEs
- `TAX-RDM-003_Tags.md` - 80 standardized tags for flexible categorization

**Purpose:** Classify and organize all documentation READMEs

### 2. LIBRARIES Ecosystem

**Purpose:** Content-focused classification (what you work with)

**Structure:**

```
ENTITIES/LIBRARIES/
├── Responsibilities/
│   ├── Actions/ (429 verbs)
│   ├── Objects/ (50+ deliverables)
│   └── Responsibilities_Master.json (193 core)
├── Tools/
│   ├── AI_Tools/ (80+ tools)
│   └── Tools_Master_List.csv
├── Skills/
│   ├── Master/all_skills.json (28+)
│   └── By_Department/
├── Professions/ (17 professions)
├── Departments/ (10 departments)
└── Taxonomy/
    └── (Canonical taxonomy files)
```

**Key Relationships:**
- **Tools** create **Objects** using **Actions**
- **Professions** perform **Responsibilities** using **Skills**
- **Skills** = Responsibility + Tool combination
- **Departments** own all of the above

### 3. TASK_MANAGERS Ecosystem

**Purpose:** Workflow-focused classification (how you work)

**Structure:**

```
ENTITIES/TASK_MANAGERS/
├── Project_Templates/ (9 projects)
├── Milestone_Templates/ (9 milestones)
├── Task_Templates/ (71 tasks)
├── Step_Templates/ (379 steps)
├── Checklist_Templates/ (98 checklists)
├── Workflows/ (20 automated flows)
├── Guides/ (8+ documentation)
├── PROMPTS/ (100+ prompts)
├── RESEARCHES/ (50+ research items)
└── Taxonomy/
    └── (Canonical taxonomy files)
```

**Key Relationships:**
- **Projects** contain **Milestones**
- **Milestones** contain **Tasks**
- **Tasks** contain **Steps** and **Checklists**
- **Workflows** automate **Task** sequences
- **Prompts** drive **Research** and **Taxonomy Updates**

### 4. README Taxonomy (ENTITIES_2.0)

**Purpose:** Documentation classification system

**12 README Types (4 Categories):**

**Core Documentation (3 types):**
- **FLD** = Folder Instructions
- **ENT** = Entity Documentation
- **SYS** = System Documentation

**AI Instructions (3 types):**
- **NAV** = Navigation Instructions
- **WRK** = Workflow Instructions
- **PRM** = Prompt Libraries

**Recommendations (3 types):**
- **BPR** = Best Practices
- **GDL** = Guidelines
- **STD** = Standards

**Mappings (3 types):**
- **MAP** = Data Mappings
- **MIG** = Migration Mappings
- **XRF** = Cross References

**80 Standard Tags (10 Categories):**
1. **Entity tags** (6): `entity-talents`, `entity-assets`, etc.
2. **Location tags** (9): `location-talents-work`, etc.
3. **Purpose tags** (9): `purpose-onboarding`, `purpose-migration`, etc.
4. **Audience tags** (6): `audience-ai`, `audience-developer`, etc.
5. **Phase tags** (8): `phase-1`, `phase-2`, etc.
6. **Status tags** (8): `status-work`, `status-project`, etc.
7. **Content tags** (10): `content-profiles`, `content-logs`, etc.
8. **Action tags** (10): `action-create`, `action-update`, etc.
9. **Technical tags** (9): `tech-csv`, `tech-markdown`, etc.
10. **Priority tags** (5): `priority-critical`, `priority-high`, etc.

---

## Video Taxonomy System

### Complete Pipeline Overview

The video taxonomy system extracts structured knowledge from video content and integrates it into the organizational taxonomy. This creates a **continuous knowledge capture loop**.

### Pipeline Stages

```
Video Source (YouTube, Loom, etc.)
    ↓
[1] Video Transcription (PMT-004)
    ↓
Transcription File (Video_XXX.md)
    ↓
[2] Video Analysis (PMT-006, PMT-008)
    ↓
Structured Extraction (Tools, Objects, Actions, Workflows, Skills, Professions)
    ↓
[3] Gap Analysis
    ↓
Missing Elements Identified
    ↓
[4] Taxonomy Integration (PMT-009)
    ↓
New JSON Files Created / Existing Files Updated
    ↓
[5] Cross-Reference Update
    ↓
Bidirectional Links Established
    ↓
[6] Documentation & Reports
    ↓
Video_XXX_Library_Mapping_Report.md
```

### Video Processing Prompts (14 Total)

**Core Prompts:**
1. **PMT-004: Video Transcription v4.1** - Transcription methodology
2. **PMT-005: Video Naming Alternatives** - Convert titles to taxonomy-friendly names
3. **PMT-006: Video Analysis** - Extract taxonomy elements from transcriptions
4. **PMT-008: Video Analysis Improvements** - Enhanced analysis techniques
5. **PMT-009: Taxonomy Integration** - End-to-end workflow (40+ prompts in category)
6. **PMT-015: Optimize Video Transcription** - Optimization guide
7. **PMT-090: YouTube Video Processing** - YouTube-specific processing

**Support Prompts:**
8-14. Additional prompts for specialized extraction (Objects, Actions, Skills, etc.)

### What Video Taxonomy Captures

From each video, the system extracts:

#### 1. Tools Mentioned
- Tool names and variants
- Tool categories (AI/Video Generation, AI/Image Generation, etc.)
- Frequency counts
- First mention timestamps
- Integration capabilities
- Use cases and workflows

**Example from Video:**
```
TOOLS FOUND:
- GLIF (AI Workflow Automation) - 30 mentions - [00:45]
- Nano Banana (AI Thumbnail Generator) - 8 mentions - [03:15]
- VAYU 2.2 (Miniature Documentary Video) - 10 mentions - [05:30]
- Sora (OpenAI Video Generation) - 15 mentions - [07:45]
```

#### 2. Objects/Deliverables
- Object names and types
- Object categories (Design Deliverables, Media, Documents)
- Creation methods
- Platforms used
- File formats
- Optimization metrics

**Example from Video:**
```
OBJECTS FOUND:
- thumbnails (Design Deliverable)
  Types: [YouTube thumbnail, High-CTR thumbnail, Mr. Beast style thumbnail]

- videos (Media)
  Types: [Miniature documentary, TikTok video, Social video, AI video]

- scripts (Documents)
  Types: [Documentary script, Voiceover script, Video script]
```

#### 3. Action Verbs (Categorized)
- **Creation verbs:** create, generate, design, build, produce
- **Modification verbs:** optimize, refine, customize, enhance
- **Analysis verbs:** research, review, analyze
- **Organization verbs:** organize, structure, schedule
- **Communication verbs:** publish, share, export

**Example from Video:**
```
ACTIONS FOUND:
CREATION VERBS:
- create (15x) - [00:45], [02:30], [05:12]...
- generate (23x) - [01:20], [03:15], [06:45]...
- design (8x) - [02:34], [04:50]...

MODIFICATION VERBS:
- optimize (12x) - [03:20], [05:40], [08:15]...
- refine (6x) - [04:10], [07:30]...
```

#### 4. Workflows/Processes
- Workflow names and objectives
- Step-by-step procedures
- Duration estimates
- Tools used in each step
- Input requirements
- Output deliverables
- Automation level
- Department assignment

**Example from Video:**
```
WORKFLOW: Automated Miniature Documentary Creation
OBJECTIVE: Generate 32-second historical documentary
STEPS:
  1. Research historical facts (Perplexity) - 2-3 min
  2. Generate documentary script (AI) - 1-2 min
  3. Create tilt-shift video (VAYU + Seedream) - 3-5 min
  4. Generate voiceover (Eleven Labs) - 1-2 min
  5. Combine elements (GLIF) - 1-2 min
  6. Review and publish - 2-5 min
DURATION: 10-20 minutes (mostly automated)
DEPARTMENT: VID;AID
```

#### 5. Professions/Roles
- Profession names
- Responsibilities performed
- Tools used
- Objects worked with
- Skills required
- Typical workflows

**Example from Video:**
```
PROFESSIONS MENTIONED:
- Content Creator
  Responsibilities: creating thumbnails, editing videos, automating workflows
  Tools: GLIF, Nano Banana, VAYU, Eleven Labs
  Objects: thumbnails, videos, scripts

- YouTuber
  Responsibilities: optimizing CTR, creating engaging thumbnails, building audience
  Tools: Nano Banana, GLIF, YouTube Studio
  Objects: YouTube thumbnails, videos
```

#### 6. Skills
- Skill names and definitions
- Skill phrases (action + tool pattern)
- Proficiency levels
- Applications and use cases
- Related tools and objects
- Department relevance

**Example from Video:**
```
SKILLS IDENTIFIED:
- Prompt Engineering
  Phrase: "refined AI video generation prompts"
  Proficiency: Intermediate
  Tools: GLIF, Nano Banana, VAYU, Sora

- Thumbnail Design
  Phrase: "designed thumbnails using Nano Banana"
  Proficiency: Intermediate
  Applications: CTR optimization, visual engagement
```

#### 7. Department Associations
- Which departments use the tools/objects/workflows
- Department-specific variations
- Cross-department collaborations

#### 8. Business Value Insights
- Time savings
- Cost reductions
- Efficiency gains
- Automation potential
- Strategic implications

---

## How to Generate Taxonomy

### Method 1: Manual Video Analysis (Using PMT-009)

**Time Required:** 2-4 hours per video
**Skill Level:** Intermediate
**Output:** Complete taxonomy integration

**Steps:**

#### Phase 1: Initial Video Analysis (30-45 minutes)

1. **Read Video Transcription File**
   - Location: `ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`
   - Open in editor

2. **Create Inventory of Taxonomy Elements**

   **Tools Inventory:**
   ```markdown
   TOOLS FOUND:
   - [Tool Name] - [Category] - [Timestamp] - [Frequency]
   - Example: GLIF - AI Workflow Automation - [00:45] - 30x
   ```

   **Objects Inventory:**
   ```markdown
   OBJECTS FOUND:
   - [Object Name] ([Category]) - [Description] - [Timestamp]
   - Example: thumbnails (Design Deliverable) - "YouTube thumbnails" - [03:15]
   ```

   **Actions Inventory:**
   ```markdown
   ACTIONS FOUND (By Category):
   CREATION VERBS:
   - create (15x) - [timestamps]
   - generate (23x) - [timestamps]
   ```

   **Workflows Inventory:**
   ```markdown
   WORKFLOW: [Name]
   OBJECTIVE: [Goal]
   STEPS: [Numbered steps]
   DURATION: [Time estimate]
   TOOLS: [Tool list]
   ```

   **Professions Inventory:**
   ```markdown
   PROFESSIONS MENTIONED:
   - [Profession Name] - [Responsibilities extracted]
   ```

   **Skills Inventory:**
   ```markdown
   SKILLS IDENTIFIED:
   - [Skill Name] - [Description] - [Applications]
   ```

#### Phase 2: Gap Analysis (20-30 minutes)

3. **Check Existing Taxonomy**

   **For Tools:**
   ```bash
   # Navigate to tools directory
   cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"

   # Check if tool exists
   ls *.json | grep -i "tool_name"
   ```

   **For Objects:**
   ```bash
   # Navigate to objects directory
   cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Responsibilities\Objects"

   # Check existing objects
   cat Design_Deliverables.json
   ```

4. **Document Gaps**

   Create gap analysis report:
   ```markdown
   TOOLS GAP ANALYSIS:
   ✅ EXISTS (Enhance):
   - ElevenLabs.json → ADD: GLIF integration workflow

   ❌ MISSING (Create):
   Priority: CRITICAL
   - GLIF.json → AI Workflow Automation platform
   - Sora.json → OpenAI video generation
   ```

#### Phase 3: Creation and Updates (60-90 minutes)

5. **Create New Tool Files**

   **Template:**
   ```json
   {
     "entity_type": "LIBRARIES",
     "sub_entity": "Tool",
     "tool_id": "TOL-###",
     "name": "[Tool Name]",
     "vendor": "[Vendor]",
     "category": "[Category]",
     "purpose": "[Purpose]",
     "description": "[Detailed description from video]",
     "skill_level_required": "[Level]",
     "cost_structure": "[Pricing]",
     "platform_compatibility": ["Web", "API"],
     "documentation_url": "[URL]",
     "actual_remote_helpers_usage": {
       "primary_use": "[From video]",
       "users": ["[Profession types]"],
       "use_cases": ["[Verb phrases]"],
       "typical_workflows": []
     },
     "strengths": ["[From video]"],
     "limitations": ["[From video]"],
     "tags": ["[Relevant tags]"]
   }
   ```

   **Save to:** `ENTITIES/LIBRARIES/Tools/AI_Tools/[Tool_Name].json`

6. **Create/Update Object Entries**

   **For Design Deliverables:**
   ```json
   {
     "object_id": "OBJ-###",
     "object_name": "thumbnails",
     "category": "Design Deliverables",
     "object_types": [
       "YouTube thumbnail",
       "Social media thumbnail",
       "High-CTR thumbnail"
     ],
     "professions": ["Content Creator", "Graphic Designer", "YouTuber"],
     "profession_ids": ["PRF-###", "PRF-###", "PRF-###"],
     "tools": ["Nano Banana", "GLIF", "Midjourney"],
     "tool_ids": ["TOL-###", "TOL-###", "TOL-###"],
     "department": "VID;DGN",
     "complexity": "Low to Medium",
     "time_estimate": "15-30 minutes",
     "common_actions": ["Create", "Generate", "Optimize", "Design"],
     "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"]
   }
   ```

   **Add to:** `ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json`

7. **Create/Update Workflow Entries**

   **Template:**
   ```json
   {
     "entity_type": "TASK_MANAGERS",
     "sub_entity": "Workflow",
     "workflow_id": "WRF-###",
     "workflow_name": "[Name]",
     "category": "Content Creation",
     "description": "[Description]",
     "objective": "[Goal]",
     "workflow_type": "Automated AI Pipeline",
     "duration": "[Time]",
     "complexity": "[Level]",
     "steps": [
       {
         "step_number": 1,
         "action": "[Action]",
         "description": "[Description]",
         "tool_id": "TOL-###",
         "tool_name": "[Tool]",
         "input": "[Input]",
         "output": "[Output]",
         "duration": "[Time]"
       }
     ],
     "tools_used": [{"tool_id": "TOL-###", "tool_name": "[Tool]", "role": "[Role]"}],
     "objects_created": [{"object_id": "OBJ-###", "object_name": "[Object]"}],
     "actions_performed": ["[Actions]"],
     "professions_involved": ["[Professions]"],
     "department": "VID;AID"
   }
   ```

   **Save to:** `ENTITIES/TASK_MANAGERS/Workflows/[Workflow_Name].json`

8. **Update Action Files**

   Open: `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`

   Add new contexts to existing actions:
   ```json
   {
     "action_id": "ACT-###",
     "action": "Generate",
     "category": "Creation",
     "contexts": [
       "generate images",
       "generate videos",  // NEW
       "generate thumbnails",  // NEW
       "generate scripts"  // NEW
     ],
     "tools_commonly_used": ["GLIF", "Nano Banana", "VAYU"],
     "tool_ids": ["TOL-###", "TOL-###", "TOL-###"]
   }
   ```

9. **Create/Update Profession Files**

   **For Content Creator:**
   ```json
   {
     "entity_type": "LIBRARIES",
     "sub_entity": "Profession",
     "profession_id": "PRF-###",
     "name": "Content Creator",
     "department": "VID;AID",
     "description": "Creates engaging digital content",
     "responsibilities": [
       "creating engaging thumbnails optimized for CTR",  // NEW
       "producing miniature documentaries",  // NEW
       "automating content workflows with AI agents"  // NEW
     ],
     "objects_worked_with": [
       {
         "object_id": "OBJ-###",
         "object_name": "thumbnails",
         "actions": ["Create", "Generate", "Optimize"]
       }
     ],
     "tools_used": [
       {
         "tool_id": "TOL-###",
         "tool_name": "GLIF",
         "purpose": "Workflow automation"
       }
     ],
     "workflows_performed": [
       {"workflow_id": "WRF-###", "workflow_name": "[Workflow]"}
     ],
     "skills_required": [
       {"skill_id": "SKL-###", "skill_name": "Prompt Engineering"}
     ]
   }
   ```

   **Save to:** `ENTITIES/LIBRARIES/Professions/Content_Creator.json`

10. **Create Skill Entries**

    **For New Skill:**
    ```json
    {
      "skill_id": "SKL-###",
      "skill_name": "Thumbnail Design",
      "skill_phrase": "designed thumbnails using Nano Banana",
      "definition": "Creating visually engaging thumbnail images optimized for CTR",
      "proficiency_levels": ["Beginner", "Intermediate", "Advanced"],
      "applications": ["YouTube thumbnails", "social media thumbnails"],
      "tools": ["Nano Banana", "Midjourney", "Photoshop"],
      "tool_ids": ["TOL-###", "TOL-###", "TOL-###"],
      "related_actions": ["create", "design", "optimize", "generate"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"],
      "related_objects": [{"object_id": "OBJ-###", "object_name": "thumbnails"}],
      "professions": ["Content Creator", "YouTuber", "Graphic Designer"],
      "profession_ids": ["PRF-###", "PRF-###", "PRF-###"],
      "department": "VID;DGN"
    }
    ```

    **Add to:** `ENTITIES/LIBRARIES/Skills/Master/all_skills.json`

#### Phase 4: Cross-Referencing (30-45 minutes)

11. **Establish Bidirectional Links**

    **Ensure:**
    - Tools reference objects they create
    - Objects reference tools that create them
    - Workflows reference all entities (tools, objects, actions, professions)
    - Professions reference all relevant entities

    **Example Cross-Reference Check:**
    ```
    GLIF.json should list:
      objects_created_via_workflows: ["thumbnails", "videos", "scripts"]

    Thumbnails object should list:
      tools: ["GLIF", "Nano Banana", "Midjourney"]
      ai_tools_used: [detailed tool usage]

    Content_Creator.json should list:
      tools_used: [GLIF with tool_id]
      objects_worked_with: [thumbnails with object_id]
      workflows_performed: [workflow with workflow_id]
    ```

#### Phase 5: Reporting (20-30 minutes)

12. **Generate Comprehensive Analysis Report**

    **Create:** `Video_XXX_Library_Mapping_Report.md`

    **Structure:**
    ```markdown
    # Video [XXX] Library Mapping Report
    ## Taxonomy Analysis and Integration

    **Video Title**: [Title]
    **Analysis Date**: [Date]
    **Video Duration**: [Duration]

    ## Executive Summary
    [Overview]

    **Key Metrics**:
    - Tools Analyzed: [Count]
    - Objects Identified: [Count]
    - Workflows Extracted: [Count]
    - Coverage Improvement: [Before%] → [After%]

    ## 1. Tools Analysis
    ### 1.1 Tools Identified
    [List all tools]

    ### 1.2 Tools Gap Analysis
    **Existing Tools (Enhanced):**
    [List]

    **New Tools Created:**
    [List]

    ## 2. Objects Analysis
    [Complete object analysis]

    ## 3. Actions Analysis
    [Complete action analysis]

    ## 4. Workflows Analysis
    [Complete workflow analysis]

    ## 5. Professions Analysis
    [Complete profession analysis]

    ## 6. Skills Analysis
    [Complete skill analysis]

    ## 7. Cross-Reference Summary
    [Validation of bidirectional links]

    ## 8. Business Value and Impact
    [Business insights]

    ## 9. Recommendations
    [Actionable recommendations]

    ## 10. Files Created/Modified
    ### Created Files:
    [List with paths]

    ### Modified Files:
    [List with changes]
    ```

    **Save to:** `ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Video_XXX_Library_Mapping_Report.md`

### Method 2: Assisted Video Analysis (Using AI Tools)

**Time Required:** 30-60 minutes per video
**Skill Level:** Beginner to Intermediate
**Output:** Structured extractions ready for manual review

**Steps:**

1. **Prepare Video Transcription**
   - Ensure transcription file exists in `02_TRANSCRIPTIONS/`

2. **Use PMT-009 Prompt with AI**
   - Open: `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`
   - Copy entire prompt
   - Paste into Claude or ChatGPT
   - Provide video transcription as input

3. **Review AI-Generated Extractions**
   - Verify tool names and categories
   - Validate object classifications
   - Check workflow step accuracy
   - Confirm profession assignments

4. **Manual Verification & Adjustment**
   - Cross-check timestamps
   - Verify context accuracy
   - Adjust categories if needed
   - Validate IDs assignment

5. **Save Extractions to JSON Files**
   - Follow Phase 3 steps from Method 1
   - Use AI-generated content as base
   - Add manual refinements

### Method 3: Automated Taxonomy Generation (Future)

**Status:** Partially implemented (scripts exist)
**Full automation:** In development

**Available Scripts:**
- `taxonomy_lookup.js` - Maps taxonomy data to application format
- Additional extraction scripts (planned)

---

## How to Update Taxonomy

### Scenario 1: Adding a New Tool

**When:** You discover a new AI tool that should be in the taxonomy

**Steps:**

1. **Check if Tool Already Exists**
   ```bash
   cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"
   ls *.json | grep -i "tool_name"
   ```

2. **Assign Tool ID**
   - Open: `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
   - Find last `TOL-###` ID
   - Assign next sequential number (e.g., if last is TOL-045, use TOL-046)

3. **Create Tool JSON File**
   - Use template from "How to Generate Taxonomy" section
   - Fill in all fields
   - Save as: `ENTITIES/LIBRARIES/Tools/AI_Tools/[Tool_Name].json`

4. **Update Master List**
   - Add row to: `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
   - Format: `TOL-046, Tool Name, Tool, [Department], [Category], [File Path], 1, Active`

5. **Update ISO Code Registry (if new category)**
   - Edit: `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`
   - Add new category code if needed

6. **Cross-Reference Updates**
   - If tool creates objects, update object files to reference new tool
   - If tool is used in workflows, update workflow files
   - If tool is used by professions, update profession files

### Scenario 2: Adding a New Object Type

**When:** A new deliverable or object type is identified

**Steps:**

1. **Identify Object Category**
   - Design Deliverables
   - Media Objects
   - Documents
   - Other

2. **Assign Object ID**
   - Find last `OBJ-###` ID in Master List
   - Assign next number

3. **Update or Create Object File**

   **If category file exists (e.g., Design_Deliverables.json):**
   - Open file
   - Add new object entry with assigned OBJ-### ID

   **If category file doesn't exist:**
   - Create new file: `ENTITIES/LIBRARIES/Responsibilities/Objects/[Category_Name].json`
   - Add object entry

4. **Update Master List**
   - Add row to: `Libraries_Master_List.csv`

5. **Cross-Reference Updates**
   - Update tools that create this object
   - Update professions that work with this object
   - Update actions that apply to this object
   - Update workflows that produce this object

### Scenario 3: Adding a New Workflow

**When:** A new process or workflow is discovered

**Steps:**

1. **Assign Workflow ID**
   - Find last `WRF-###` ID
   - Assign next number

2. **Create Workflow JSON File**
   - Use template from "How to Generate Taxonomy" section
   - Document all steps with tool IDs
   - Link to objects created (with OBJ-### IDs)
   - Link to actions performed (with ACT-### IDs)
   - Link to professions involved (with PRF-### IDs)
   - Save as: `ENTITIES/TASK_MANAGERS/Workflows/[Workflow_Name].json`

3. **Update Taxonomy Master List**
   - Add row to: `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`

4. **Cross-Reference Updates**
   - Update tool files to reference this workflow
   - Update object files to reference this workflow
   - Update profession files to reference this workflow

### Scenario 4: Adding a New Profession

**When:** A new job role or profession is identified

**Steps:**

1. **Assign Profession ID**
   - Find last `PRF-###` ID
   - Assign next number

2. **Create Profession JSON File**
   - Use template from "How to Generate Taxonomy" section
   - List all responsibilities
   - List all tools used (with TOL-### IDs)
   - List all objects worked with (with OBJ-### IDs)
   - List all workflows performed (with WRF-### IDs)
   - List all skills required (with SKL-### IDs)
   - Save as: `ENTITIES/LIBRARIES/Professions/[Profession_Name].json`

3. **Update Master List**
   - Add row to: `Libraries_Master_List.csv`

4. **Update ISO Code Registry**
   - Add profession code to: `Libraries_ISO_Code_Registry.md`
   - Format: `PRF-XXX | [Profession Name] | [Department] | 1`

5. **Cross-Reference Updates**
   - Update tool files to list this profession as user
   - Update object files to list this profession
   - Update workflow files to list this profession
   - Update skill files to list this profession

### Scenario 5: Bulk Update from Video Analysis

**When:** You've analyzed a video and have 10+ taxonomy updates

**Steps:**

1. **Complete Phase 1 & 2 (Analysis & Gap Identification)**
   - Follow steps in "Method 1: Manual Video Analysis"

2. **Prioritize Updates**
   - **Critical:** Tools mentioned 10+ times
   - **High:** Tools mentioned 5-9 times
   - **Medium:** Tools mentioned 2-4 times
   - **Low:** Tools mentioned once

3. **Batch Create Tool Files**
   - Create all CRITICAL and HIGH priority tools first
   - Use consistent naming and ID assignment

4. **Batch Update Object Files**
   - Group by category (Design Deliverables, Media, Documents)
   - Update all related objects in one session

5. **Batch Create Workflow Files**
   - Create workflows in order of complexity (simple → complex)
   - Ensure all referenced IDs are assigned

6. **Batch Update Profession Files**
   - Update all professions mentioned in video
   - Add new responsibilities, tools, objects, workflows

7. **Master List Updates**
   - Update both LIBRARIES and TASK_MANAGERS Master Lists in one session
   - Verify no duplicate IDs

8. **Generate Comprehensive Report**
   - Create `Video_XXX_Library_Mapping_Report.md`
   - Document all changes

---

## Taxonomy Scripts and Tools

### 1. taxonomy_lookup.js

**Location:** `Design Nov25/Safonova Eleonora/Safonova Eleonora/AdminRHS-AI-Catalog-4/scripts/taxonomy_lookup.js`

**Purpose:** Maps taxonomy data to application format for AI tools catalog

**Functions:**

#### lookupToolInTaxonomy(toolName, workspaceRoot)
**Purpose:** Searches for tool data in taxonomy folder structure

**Parameters:**
- `toolName` (string): Name of the tool to look up
- `workspaceRoot` (string): Root path of the workspace

**Returns:** Tool data from taxonomy or null if not found

**Example:**
```javascript
const toolData = lookupToolInTaxonomy('GLIF', 'G:\\Job\\REMS\\Dropbox');
// Returns: {entity_type: "LIBRARIES", name: "GLIF", ...}
```

#### convertTaxonomyToApp(taxonomyTool, defaults)
**Purpose:** Converts taxonomy format to app-compatible format

**Parameters:**
- `taxonomyTool` (object): Tool data from taxonomy
- `defaults` (object): Default values if taxonomy data is missing

**Returns:** Tool in app format

**Transformations:**
- Maps cost structure → subscription types (Free, Paid, Freemium)
- Maps departments (Dev→Developers, Design→Designers, Video→Videograph)
- Maps categories (Programming, AI Assistant, Design, Automation, Web Design, Productivity, Video)
- Maps use cases → responsibilities (Write Code, Debug Software, Design Websites, etc.)

**Example:**
```javascript
const appTool = convertTaxonomyToApp(taxonomyTool, {
  borderColor: '#28a745',
  account: 'team@example.com'
});
```

#### parseSubscription(costStructure)
**Purpose:** Maps cost structures to subscription types

**Parameters:**
- `costStructure` (string): Cost information from taxonomy

**Returns:** Array of subscription types

**Mapping Logic:**
- "free" + "tier" → ['Freemium']
- "free" only → ['Free']
- "paid" or "subscription" or "pro" → ['Paid']
- "free" + "paid" → ['Freemium']
- Default → ['Freemium']

#### parseCategory(categoryString)
**Purpose:** Maps tool categories to standardized categories

**Parameters:**
- `categoryString` (string): Category from taxonomy

**Returns:** Array of categories

**Category Mapping:**
- "code editor" or "programming" → ['Programming']
- "ai" or "llm" → ['AI Assistant']
- "design" → ['Design']
- "automation" → ['Automation']
- "web design" or "website" → ['Web Design']
- "productivity" → ['Productivity']
- "video" → ['Video']

#### mapUseCaseToResponsibility(useCase)
**Purpose:** Maps use cases to responsibility categories

**Parameters:**
- `useCase` (string): Use case description

**Returns:** Responsibility string

**Mapping Logic:**
- "code" or "generate" or "build" → 'Write Code'
- "debug" or "fix" or "refactor" → 'Debug Software'
- "design" or "component" or "ui" → 'Design Websites'
- "deploy" or "host" → 'Deploy Applications'
- "analyze" or "research" → 'Research Topics'
- "automate" or "workflow" → 'Automate Workflows'
- "manage" or "organize" → 'Manage Information'
- "presentation" or "content" → 'Create Presentations'
- "image" or "generate" → 'Generate Images'
- Default → 'Manage Information'

#### mapProfession(user)
**Purpose:** Normalizes profession names to standard format

**Parameters:**
- `user` (string): Profession name variant

**Returns:** Standardized profession name

**Mapping Logic:**
- "Frontend" or "Front-end" → 'Front-end Developer'
- "Backend" or "Back-end" → 'Back-end Developer'
- "Full Stack" or "Full-Stack" → 'Full Stack Developer'
- "UI/UX Designer" or "UI/UX" → 'UI/UX Designer'
- "Graphic Designer" → 'Graphic Designer'
- "Web Designer" → 'Web Designer'
- "All departments" or "All professionals" → 'All Professionals'

#### getTaxonomyFileName(toolName)
**Purpose:** Maps tool names to taxonomy file names

**Parameters:**
- `toolName` (string): Tool name

**Returns:** Filename string

**Name Map Examples:**
- 'Cursor' → 'Cursor.json'
- 'Claude' → 'Claude.json'
- 'GPT' → 'ChatGPT.json'
- 'MidJourney' or 'Midjourney' → 'Midjourney.json'
- 'Lovable' → 'Lovable_dev.json'
- 'ElevenLabs' → 'ElevenLabs.json'
- 'Adobe Firefly' → 'Adobe_Firefly.json'

**Usage Example:**
```javascript
const { getToolData } = require('./taxonomy_lookup.js');

const toolData = getToolData('GLIF', {
  borderColor: '#28a745',
  department: ['Developers']
}, 'G:\\Job\\REMS\\Dropbox');

console.log(toolData);
// Output: Complete tool object in app format
```

### 2. Future Scripts (Planned)

**Extraction Scripts:**
- `extract_tools.py` - Automated tool extraction from transcriptions
- `extract_objects.py` - Automated object extraction
- `extract_workflows.py` - Automated workflow extraction
- `validate_taxonomy.py` - Taxonomy validation and consistency checking

**Update Scripts:**
- `update_master_lists.py` - Automated master list updates
- `update_cross_references.py` - Automated bidirectional link updates
- `generate_reports.py` - Automated report generation

**Analysis Scripts:**
- `gap_analysis.py` - Automated gap detection
- `coverage_metrics.py` - Calculate taxonomy coverage
- `department_distribution.py` - Generate department statistics

---

## Prompts Library

### Core Video Processing Prompts

#### PMT-004: Video Transcription v4.1
**Location:** `ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md`

**Purpose:** Core transcription methodology for converting video audio to structured text

**Key Features:**
- Speaker identification
- Timestamp extraction
- Technical term preservation
- Action verb highlighting
- Tool name recognition

**Output Format:**
```markdown
# Video Transcription: [Title]

**Duration:** [HH:MM:SS]
**Speaker:** [Name/Role]
**Date:** [Date]

## [00:00] Introduction
[Transcription text...]

## [05:30] Main Content
[Transcription text...]

**Tools Mentioned:** [List]
**Key Concepts:** [List]
```

#### PMT-005: Video Naming Alternatives
**Location:** `ENTITIES/PROMPTS/PMT-005_Video_Naming_Alternatives.md`

**Purpose:** Convert video titles to professional taxonomy-friendly names

**Transformation Examples:**
- "10 INSANE AI Tools You NEED!" → "10 AI Tools for Content Creation"
- "This Changed EVERYTHING" → "AI Workflow Automation Best Practices"
- "STOP Using These Tools!" → "AI Tool Selection Guidelines"

**Output:** Clean, professional, descriptive names for taxonomy integration

#### PMT-006: Video Analysis
**Location:** `ENTITIES/PROMPTS/PMT-006_Video_Analysis.md`

**Purpose:** Extract taxonomy elements from video transcriptions

**Extraction Categories:**
1. Tools and Technologies
2. Objects and Deliverables
3. Action Verbs
4. Workflows and Processes
5. Skills and Competencies
6. Professions and Roles

**Output Format:**
```markdown
## Tools Identified
1. [Tool Name] - [Category] - [Frequency] - [First Mention]

## Objects Identified
1. [Object Name] - [Type] - [Context]

## Workflows Extracted
1. [Workflow Name]
   - Steps: [List]
   - Tools: [List]
   - Duration: [Time]
```

#### PMT-008: Video Analysis Improvements
**Location:** `ENTITIES/PROMPTS/PMT-008_Video_Analysis_Improvements.md`

**Purpose:** Enhanced video analysis with deeper context extraction

**Improvements Over PMT-006:**
- Business value identification
- ROI estimation
- Automation potential assessment
- Strategic insights extraction
- Competitive analysis

**Additional Outputs:**
- Efficiency metrics
- Cost-benefit analysis
- Implementation complexity
- Scalability assessment

#### PMT-009: Taxonomy Integration
**Location:** `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`

**Purpose:** Complete end-to-end workflow for video transcription to taxonomy integration

**Workflow Phases:**
1. **Initial Video Analysis** (30-45 minutes)
   - Tools inventory
   - Objects inventory
   - Actions inventory
   - Workflows inventory
   - Professions inventory
   - Skills inventory

2. **Gap Analysis** (20-30 minutes)
   - Tools gap analysis
   - Objects gap analysis
   - Actions gap analysis
   - Workflows gap analysis
   - Professions gap analysis
   - Skills gap analysis

3. **Creation and Updates** (60-90 minutes)
   - Create tool files
   - Create/update object entries
   - Update action files
   - Create workflow files
   - Create/update profession files
   - Create skill entries

4. **Cross-Referencing** (30-45 minutes)
   - Tool → Object links
   - Object → Tool links
   - Workflow → All entities links
   - Profession → All entities links

5. **Reporting** (20-30 minutes)
   - Generate comprehensive analysis report

**Total Time:** 2.5-4 hours per video

**Output:** Complete taxonomy integration with full documentation

### Support Prompts

#### PMT-007: Objects Library Extraction
**Location:** `ENTITIES/PROMPTS/PMT-007_Objects_Library_Extraction.md`

**Purpose:** Specialized extraction of objects and deliverables

**Object Categories:**
- Design Deliverables (banners, logos, thumbnails, etc.)
- Media Objects (videos, images, audio, etc.)
- Documents (scripts, reports, presentations, etc.)
- Technical Objects (code, APIs, databases, etc.)
- Marketing Objects (social posts, blog articles, etc.)

**Output:** Structured object definitions ready for integration

#### PMT-015: Optimize Video Transcription
**Location:** `ENTITIES/PROMPTS/PMT-015_Optimize_Video_Transcription.md` (likely location)

**Purpose:** Guidelines for improving transcription quality

**Optimization Areas:**
- Technical term recognition
- Timestamp accuracy
- Speaker identification
- Context preservation
- Action verb extraction

#### PMT-090: YouTube Video Processing
**Location:** `ENTITIES/PROMPTS/PMT-090_YouTube_Video_Processing.md` (likely location)

**Purpose:** YouTube-specific video processing

**YouTube-Specific Features:**
- Video ID extraction
- Channel information
- View count and metrics
- Comment analysis
- Description parsing
- Timestamp links

### Prompt Usage Workflow

**Standard Workflow:**

1. **Start with PMT-004 (Transcription)**
   ```
   Input: Video URL or audio file
   Output: Structured transcription with timestamps
   ```

2. **Apply PMT-005 (Title Normalization)**
   ```
   Input: Original video title
   Output: Professional, taxonomy-friendly title
   ```

3. **Use PMT-006 (Basic Analysis)**
   ```
   Input: Video transcription
   Output: Tools, objects, actions, workflows identified
   ```

4. **Apply PMT-008 (Deep Analysis)**
   ```
   Input: Basic analysis results
   Output: Business value, strategic insights, ROI
   ```

5. **Execute PMT-009 (Full Integration)**
   ```
   Input: All previous analysis
   Output: Complete taxonomy integration with JSON files
   ```

**Fast Track Workflow (for experienced users):**

1. **PMT-004 (Transcription)**
2. **PMT-009 (Direct to Integration)**
   - Skips PMT-005, PMT-006, PMT-008
   - Performs all steps in one workflow

---

## Information Captured by Taxonomy

### LIBRARIES Taxonomy Information

#### 1. Entity Metadata
- **Entity Type:** RSP, ACT, OBJ, PRM, TOL, SKL, PRF, DPT
- **Unique ID:** TOL-001, OBJ-042, PRF-015, etc.
- **Entity Name:** Human-readable name
- **ISO Code:** 3-letter consonant code
- **Department Association:** AIA, DEV, HRM, LGN, DGN, VID, SLS, SMM, FIN

#### 2. Tool Information
- **Tool Name:** Full name
- **Vendor:** Provider/company name
- **Category:** AI/Video Generation, AI/Image Generation, Development Tools, etc.
- **Purpose:** Primary function
- **Description:** Detailed description
- **Skill Level Required:** Beginner, Intermediate, Advanced
- **Cost Structure:** Free, Paid, Freemium, subscription details
- **Platform Compatibility:** Web, Desktop, Mobile, API
- **Documentation URL:** Official documentation link
- **Integration Capabilities:** APIs, webhooks, connectors
- **Actual Usage:** Real-world usage at organization
  - Primary use cases
  - User types (professions)
  - Typical workflows
  - Integration patterns
- **Strengths:** What the tool does well
- **Limitations:** Known constraints
- **Tags:** Searchable keywords

#### 3. Object Information
- **Object ID:** OBJ-###
- **Object Name:** Singular noun (thumbnails, videos, scripts)
- **Category:** Design Deliverables, Media, Documents, etc.
- **Object Types:** Variants (YouTube thumbnail, Social thumbnail, etc.)
- **Professions:** Who works with this object (with PRF-### IDs)
- **Tools:** Tools that create/modify this object (with TOL-### IDs)
- **Skills:** Skills needed to work with object (with SKL-### IDs)
- **Department:** Department ownership
- **Parameters:** Configuration options
- **Complexity:** Low, Medium, High
- **Time Estimate:** How long to create
- **Common Actions:** Actions performed on object (with ACT-### IDs)
- **Storage Pattern:** Where object files are stored
- **Platforms Used:** Where object is published/used
- **AI Tools Used:** AI tools specifically for this object
- **Optimization Metrics:** Success measurements (CTR, engagement, etc.)
- **Best Practices:** Guidelines for working with object
- **Related Workflows:** Workflows that produce this object (with WRF-### IDs)
- **Related Professions:** Professions that use this object

#### 4. Action Information
- **Action ID:** ACT-###
- **Action Verb:** Single verb (create, generate, optimize, etc.)
- **Category:** Creation, Modification, Analysis, Organization, Communication
- **Sub-Category:** ACT-CMD (command), ACT-PRC (process), ACT-RST (result)
- **Description:** What the action does
- **Contexts:** Usage examples ("create thumbnails", "generate videos")
- **Tools Commonly Used:** Tools for this action (with TOL-### IDs)
- **Objects Acted Upon:** Objects this action applies to (with OBJ-### IDs)
- **Professions Using:** Who performs this action (with PRF-### IDs)
- **Frequency:** How often action is performed

#### 5. Skill Information
- **Skill ID:** SKL-###
- **Skill Name:** Skill title
- **Skill Phrase:** Action + tool pattern ("designed thumbnails using Nano Banana")
- **Definition:** Clear skill description
- **Proficiency Levels:** Beginner, Intermediate, Advanced
- **Applications:** Use cases and scenarios
- **Tools:** Tools associated with skill (with TOL-### IDs)
- **Related Actions:** Actions that use this skill (with ACT-### IDs)
- **Related Objects:** Objects created with this skill (with OBJ-### IDs)
- **Professions:** Professions requiring this skill (with PRF-### IDs)
- **Department:** Department relevance
- **Related Workflows:** Workflows using this skill (with WRF-### IDs)

#### 6. Profession Information
- **Profession ID:** PRF-###
- **Profession Name:** Job title
- **Department:** Primary department
- **Description:** Role description
- **Responsibilities:** List of responsibilities (with RSP-### IDs if applicable)
- **Objects Worked With:** Objects used by profession (with OBJ-### IDs)
  - Object types
  - Actions performed
  - Action IDs
- **Tools Used:** Tools profession uses (with TOL-### IDs)
  - Tool purpose
  - Frequency of use
- **Workflows Performed:** Workflows profession executes (with WRF-### IDs)
- **Skills Required:** Skills needed for profession (with SKL-### IDs)
  - Skill name
  - Skill phrase
  - Proficiency level
  - Applications
- **Typical Day:** Sample daily activities

#### 7. Department Information
- **Department Code:** AIA, DEV, HRM, LGN, DGN, VID, SLS, SMM, FIN
- **Department Name:** Full name
- **Entity Count:** Number of entities in department
- **Professions:** Professions in department (with PRF-### IDs)
- **Tools:** Department-specific tools (with TOL-### IDs)
- **Objects:** Objects produced by department (with OBJ-### IDs)
- **Workflows:** Department workflows (with WRF-### IDs)

### TASK_MANAGERS Taxonomy Information

#### 1. Project Template Information
- **Project ID:** PRT-###
- **Project Name:** Project title
- **Description:** Project overview
- **Department:** Owning department
- **Milestones:** Contained milestones (with MLT-### IDs)
- **Total Duration:** Estimated project length
- **Priority:** Critical, High, Medium, Low
- **Status:** Active, Planned, Archived

#### 2. Milestone Template Information
- **Milestone ID:** MLT-###
- **Milestone Name:** Milestone title
- **Parent Project:** Project ID (PRT-###)
- **Description:** Milestone overview
- **Tasks:** Contained tasks (with TST-### IDs)
- **Deliverables:** Expected outputs
- **Duration:** Time estimate
- **Dependencies:** Prerequisite milestones

#### 3. Task Template Information
- **Task ID:** TST-###
- **Task Name:** Task title
- **Parent Milestone:** Milestone ID (MLT-###)
- **Description:** Task details
- **Formula:** Action + Object + Tool (if applicable)
- **Steps:** Contained steps (with STT-### IDs)
- **Checklists:** Verification items (with CHT-### IDs)
- **Department:** Responsible department
- **Priority:** High, Medium, Low
- **Complexity:** Low, Medium, High
- **Time Estimate:** Duration
- **Dependencies:** Prerequisite tasks
- **Blocking:** Tasks blocked by this task

#### 4. Step Template Information
- **Step ID:** STT-###
- **Step Description:** Step details
- **Parent Task:** Task ID (TST-###)
- **Order:** Step sequence number
- **Action:** Action performed (with ACT-### ID)
- **Tool:** Tool used (with TOL-### ID if applicable)
- **Input:** Required inputs
- **Output:** Expected outputs
- **Duration:** Time estimate
- **Department:** Performing department

#### 5. Checklist Template Information
- **Checklist ID:** CHT-###
- **Checklist Item:** Item description
- **Parent:** Task or Step ID
- **Type:** Deliverable, Verification, Quality Check
- **Completion Criteria:** How to verify completion

#### 6. Workflow Information
- **Workflow ID:** WRF-###
- **Workflow Name:** Workflow title
- **Category:** Content Creation, Development, Research, etc.
- **Description:** Workflow overview
- **Objective:** Goal of workflow
- **Workflow Type:** Manual, Semi-Automated, Fully Automated, AI Pipeline
- **Duration:** Total time
- **Complexity:** Low, Medium, High (for user), Setup complexity
- **Steps:** Detailed step-by-step process
  - Step number
  - Action
  - Description
  - Tool ID (TOL-###)
  - Tool name
  - Input
  - Output
  - Duration
- **Tools Used:** All tools in workflow (with TOL-### IDs and roles)
- **Objects Created:** Output objects (with OBJ-### IDs)
- **Objects Used:** Input objects (with OBJ-### IDs)
- **Actions Performed:** All actions (with ACT-### IDs)
- **Professions Involved:** Who executes workflow (with PRF-### IDs)
- **Skills Required:** Skills needed (with SKL-### IDs)
- **Department:** Owning department
- **Input Requirements:** What's needed to start
- **Output Deliverables:** What's produced
- **Automation Level:** Fully Automated, Semi-Automated, Manual
- **Business Value:** Impact and benefits
- **Use Cases:** Application scenarios
- **Platforms Served:** Where outputs are used
- **Optimization Tips:** Best practices
- **Related Workflows:** Connected workflows
- **Tags:** Searchable keywords

#### 7. Guide Information
- **Guide ID:** GDS-###
- **Guide Title:** Guide name
- **Purpose:** What guide explains
- **Content:** Guide body
- **Related Entities:** Referenced entities (with IDs)
- **Target Audience:** Who should read
- **Department:** Relevant department

#### 8. Research Information
- **Research ID:** RSR-###
- **Research Title:** Research name
- **Source:** Video, Document, Interview, etc.
- **Source URL:** Original content location
- **Date:** Research date
- **Analyst:** Who conducted research
- **Summary:** Executive summary
- **Key Findings:** Main discoveries
- **Tools Identified:** Tools found in research
- **Objects Identified:** Objects found
- **Workflows Identified:** Workflows found
- **Taxonomy Impact:** What was added/updated
- **Related Files:** Associated files

### README Taxonomy Information (ENTITIES_2.0)

#### 1. README Metadata
- **README ID:** RDM-[TYPE]-[###]
- **README Name:** Title
- **Type:** FLD, ENT, SYS, NAV, WRK, PRM, BPR, GDL, STD, MAP, MIG, XRF
- **Category:** Core Documentation, AI Instructions, Recommendations, Mappings
- **Tags:** Array of tags from 10 categories
- **Created Date:** Creation timestamp
- **Last Updated:** Last modification timestamp
- **Status:** Draft, Active, Archived
- **Version:** Semantic version
- **Author:** Creator
- **Target Audience:** Who should read

#### 2. Tag Information
- **Entity Tags:** Which entity (entity-talents, entity-assets, etc.)
- **Location Tags:** Where in system (location-talents-work, etc.)
- **Purpose Tags:** Why exists (purpose-onboarding, purpose-migration, etc.)
- **Audience Tags:** Who for (audience-ai, audience-developer, etc.)
- **Phase Tags:** When relevant (phase-1, phase-2, etc.)
- **Status Tags:** Which status (status-work, status-project, etc.)
- **Content Tags:** What contains (content-profiles, content-logs, etc.)
- **Action Tags:** What actions (action-create, action-update, etc.)
- **Technical Tags:** What tech (tech-csv, tech-markdown, etc.)
- **Priority Tags:** How important (priority-critical, priority-high, etc.)

### Cross-Reference Information

#### 1. Tool ↔ Object Relationships
- Which tools create which objects
- Which objects are created by which tools
- Tool-object usage patterns
- Alternative tool options for same object

#### 2. Workflow ↔ Entity Relationships
- Which tools are used in which workflows
- Which objects are produced by which workflows
- Which actions are performed in which workflows
- Which professions execute which workflows
- Which skills are required for which workflows

#### 3. Profession ↔ Entity Relationships
- Which professions use which tools
- Which professions work with which objects
- Which professions perform which actions
- Which professions execute which workflows
- Which professions require which skills

#### 4. Department ↔ Entity Relationships
- Which departments own which tools
- Which departments produce which objects
- Which departments perform which actions
- Which departments execute which workflows
- Which departments have which professions

### Hierarchical Information

#### 1. LIBRARIES Hierarchy
```
Departments
  ├── Professions
  │     ├── Responsibilities
  │     ├── Skills
  │     └── Tools
  │           └── Objects
  │                 └── Actions
  └── Parameters
```

#### 2. TASK_MANAGERS Hierarchy
```
Projects (PRT-###)
  └── Milestones (MLT-###)
        └── Tasks (TST-###)
              ├── Steps (STT-###)
              │     └── Checklists (CHT-###)
              └── Checklists (CHT-###)

Workflows (WRF-###)
  └── Tasks (sequence)

Guides (GDS-###)
  └── References to all entity types

Research (RSR-###)
  └── Extractions feeding back to all taxonomies
```

### Statistical Information

#### 1. Entity Counts
- Total entities by type (RSP: 193, ACT: 429, OBJ: 50+, etc.)
- Entities by department
- Entities by category
- Entity growth over time

#### 2. Coverage Metrics
- Tools coverage (% of tools in taxonomy vs. total tools used)
- Object coverage
- Workflow documentation coverage
- Profession-tool mapping completeness

#### 3. Cross-Reference Statistics
- Number of tool-object relationships
- Number of workflow-tool relationships
- Number of profession-tool relationships
- Average entities per department

#### 4. Usage Statistics
- Most referenced tools
- Most common objects
- Most performed actions
- Most executed workflows
- Most documented professions

### Migration Information

#### 1. Legacy Mappings
- Old ID → New ID mappings
- Old file paths → New file paths
- Deprecated entity codes
- Migration dates and reasons

#### 2. Version History
- Entity creation dates
- Entity update history
- Taxonomy version changes
- Schema evolution

---

## Folder Structure

### Complete Taxonomy Folder Hierarchy

```
G:\Job\REMS\Dropbox\
│
├── ENTITIES/
│   │
│   ├── TAXONOMY/ [CENTRAL HUB]
│   │   ├── README.md [Navigation hub for all taxonomy]
│   │   │
│   │   ├── TAX-001_Libraries/ [LIBRARIES Taxonomy]
│   │   │   ├── Libraries_Master_List.csv
│   │   │   ├── Libraries_ISO_Code_Registry.md
│   │   │   ├── Libraries_Hierarchy_Tree.md
│   │   │   ├── Libraries_Department_Distribution.md
│   │   │   ├── Libraries_Migration_Map.json
│   │   │   ├── Tools_Master_List.csv
│   │   │   └── Tools_Master_Priority.json
│   │   │
│   │   ├── TAX-002_Task_Managers/ [TASK_MANAGERS Taxonomy]
│   │   │   ├── Taxonomy_Master_List.csv
│   │   │   ├── Taxonomy_ISO_Code_Registry.md
│   │   │   ├── Taxonomy_Hierarchy_Tree.md
│   │   │   ├── Taxonomy_Department_Distribution.md
│   │   │   └── Taxonomy_Migration_Map.json
│   │   │
│   │   ├── TAX-003_Video_Processing/ [Video Taxonomy]
│   │   │   └── PMT-009_Taxonomy_Integration.md
│   │   │
│   │   └── TAX-004_Entity_Integration/ [Entity Integration]
│   │       └── Entity_Integration_Taxonomy.md
│   │
│   ├── LIBRARIES/ [CANONICAL SOURCE FOR LIBRARIES]
│   │   │
│   │   ├── Responsibilities/
│   │   │   ├── Actions/
│   │   │   │   ├── Actions_Master.json [429 verbs]
│   │   │   │   ├── ACT-CMD/ [Command verbs]
│   │   │   │   ├── ACT-PRC/ [Process verbs]
│   │   │   │   └── ACT-RST/ [Result verbs]
│   │   │   │
│   │   │   ├── Objects/
│   │   │   │   ├── Design_Deliverables.json
│   │   │   │   ├── Video_Deliverables.json
│   │   │   │   ├── Documents.json
│   │   │   │   ├── AI_Automation_Objects.json
│   │   │   │   └── [More object files by domain]
│   │   │   │
│   │   │   └── Responsibilities_Master.json [193 core responsibilities]
│   │   │
│   │   ├── Tools/
│   │   │   ├── AI_Tools/
│   │   │   │   ├── GLIF.json
│   │   │   │   ├── Claude.json
│   │   │   │   ├── ChatGPT.json
│   │   │   │   ├── Midjourney.json
│   │   │   │   ├── Nano_Banana.json
│   │   │   │   ├── VAYU.json
│   │   │   │   ├── Sora.json
│   │   │   │   └── [80+ AI tool files]
│   │   │   │
│   │   │   ├── Development_Tools/
│   │   │   ├── Database_Tools/
│   │   │   └── Tools_Master_List.csv
│   │   │
│   │   ├── Skills/
│   │   │   ├── Master/
│   │   │   │   └── all_skills.json [28+ skills]
│   │   │   │
│   │   │   └── By_Department/
│   │   │       ├── AIA_Skills.json
│   │   │       ├── DEV_Skills.json
│   │   │       ├── DGN_Skills.json
│   │   │       └── VID_Skills.json
│   │   │
│   │   ├── Professions/
│   │   │   ├── Content_Creator.json
│   │   │   ├── YouTuber.json
│   │   │   ├── Graphic_Designer.json
│   │   │   ├── Video_Producer.json
│   │   │   ├── Backend_Developer.json
│   │   │   └── [17 profession files]
│   │   │
│   │   ├── Departments/
│   │   │   └── [10 department definitions]
│   │   │
│   │   └── Taxonomy/ [Canonical taxonomy files]
│   │       ├── Libraries_Master_List.csv
│   │       ├── Libraries_ISO_Code_Registry.md
│   │       └── [Other taxonomy files]
│   │
│   ├── TASK_MANAGERS/ [CANONICAL SOURCE FOR TASK_MANAGERS]
│   │   │
│   │   ├── Project_Templates/
│   │   │   ├── PRT-001_AI_Tutorial_Research.json
│   │   │   └── [9 project template files]
│   │   │
│   │   ├── Milestone_Templates/
│   │   │   ├── MLT-001_Discovery.json
│   │   │   └── [9 milestone template files]
│   │   │
│   │   ├── Task_Templates/
│   │   │   ├── TST-001_AI_Powered_HTML_Parsing.json
│   │   │   ├── TST-042_Onboard_New_Employee.json
│   │   │   └── [71 task template files]
│   │   │
│   │   ├── Step_Templates/
│   │   │   ├── By_Department/
│   │   │   │   ├── AID_Steps/ [AI Department steps]
│   │   │   │   ├── DEV_Steps/ [Development steps]
│   │   │   │   ├── DGN_Steps/ [Design steps]
│   │   │   │   └── VID_Steps/ [Video steps]
│   │   │   │
│   │   │   └── [379 step template files]
│   │   │
│   │   ├── Checklist_Templates/
│   │   │   └── [98 checklist template files]
│   │   │
│   │   ├── Workflows/
│   │   │   ├── WRF-001_Lead_Enrichment.json
│   │   │   ├── WRF-002_Automated_Documentary_Creation.json
│   │   │   ├── WRF-003_YouTube_Thumbnail_Optimization.json
│   │   │   └── [20 workflow files]
│   │   │
│   │   ├── Guides/
│   │   │   ├── GDS-001_Taxonomy_Guide.md
│   │   │   ├── GDS-002_Workflow_Guide.md
│   │   │   └── [8+ guide files]
│   │   │
│   │   ├── PROMPTS/
│   │   │   ├── PMT-001_Main_Prompt.md
│   │   │   ├── PMT-004_Video_Transcription.md
│   │   │   ├── PMT-009_Taxonomy_Integration.md
│   │   │   └── [100+ prompt files]
│   │   │
│   │   ├── RESEARCHES/ [or RESEARCHES 2/]
│   │   │   ├── 00_SEARCH_QUEUE/ [Search assignments]
│   │   │   ├── 01_VIDEO_QUEUE/ [Video prioritization]
│   │   │   ├── 02_TRANSCRIPTIONS/ [23 video transcriptions]
│   │   │   │   ├── Video_001.md
│   │   │   │   ├── Video_002.md
│   │   │   │   └── [23 transcription files]
│   │   │   │
│   │   │   ├── 03_ANALYSIS/ [Extractions and reports]
│   │   │   │   ├── Video_001_Library_Mapping_Report.md
│   │   │   │   ├── Video_002_Gap_Analysis.md
│   │   │   │   └── [Analysis files]
│   │   │   │
│   │   │   ├── 04_INTEGRATION/ [Integration tracking]
│   │   │   │
│   │   │   ├── PROMPTS/ [26 research prompts]
│   │   │   │
│   │   │   ├── DATA/ [Research data & metadata]
│   │   │   │
│   │   │   ├── REPORTS/ [Research reports]
│   │   │   │
│   │   │   ├── documentation/ [Documentation]
│   │   │   │   ├── v1/
│   │   │   │   ├── v2/
│   │   │   │   └── taxonomy_complete_guide.md [THIS FILE]
│   │   │   │
│   │   │   └── ARCHIVE/ [Archived content]
│   │   │
│   │   └── Taxonomy/ [Canonical taxonomy files]
│   │       ├── Taxonomy_Master_List.csv
│   │       ├── Taxonomy_ISO_Code_Registry.md
│   │       └── [Other taxonomy files]
│   │
│   └── PROMPTS/ [CANONICAL SOURCE FOR PROMPTS]
│       ├── Core/
│       │   ├── PMT-001_Main_Prompt_v4.md
│       │   ├── PMT-002_Main_Prompt_v6_DRAFT.md
│       │   └── PMT-003_Create_Main_Prompt_v5.md
│       │
│       ├── PMT-004_Video_Transcription_v4.1.md
│       ├── PMT-005_Video_Naming_Alternatives.md
│       ├── PMT-006_Video_Analysis.md
│       ├── PMT-007_Objects_Library_Extraction.md
│       ├── PMT-008_Video_Analysis_Improvements.md
│       ├── PMT-009_Taxonomy_Integration.md
│       ├── PMT-015_Optimize_Video_Transcription.md
│       └── PMT-090_YouTube_Video_Processing.md
│
├── ENTITIES_2.0/ [NEW STRUCTURE]
│   │
│   └── SETTINGS/
│       └── _Taxonomy/ [README Taxonomy]
│           ├── TAX-RDM-001_Types.md [12 README types]
│           ├── TAX-RDM-002_Categories.md [4 categories]
│           └── TAX-RDM-003_Tags.md [80 tags]
│
└── Design Nov25/
    └── Safonova Eleonora/
        └── Safonova Eleonora/
            └── AdminRHS-AI-Catalog-4/
                └── scripts/
                    └── taxonomy_lookup.js [Taxonomy lookup script]
```

### Key Locations Reference

**Central Taxonomy Hub:**
- `ENTITIES/TAXONOMY/README.md`

**LIBRARIES Taxonomy (Canonical):**
- `ENTITIES/LIBRARIES/Taxonomy/`

**TASK_MANAGERS Taxonomy (Canonical):**
- `ENTITIES/TASK_MANAGERS/Taxonomy/`

**Video Processing:**
- Transcriptions: `ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/`
- Analysis: `ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/`
- Prompts: `ENTITIES/PROMPTS/`

**Tool Definitions:**
- AI Tools: `ENTITIES/LIBRARIES/Tools/AI_Tools/`
- Development Tools: `ENTITIES/LIBRARIES/Tools/Development_Tools/`

**Object Definitions:**
- `ENTITIES/LIBRARIES/Responsibilities/Objects/`

**Workflow Definitions:**
- `ENTITIES/TASK_MANAGERS/Workflows/`

**Scripts:**
- `Design Nov25/Safonova Eleonora/Safonova Eleonora/AdminRHS-AI-Catalog-4/scripts/`

**Documentation:**
- `ENTITIES/TASK_MANAGERS/RESEARCHES 2/documentation/`

---

## Usage Examples

### Example 1: Finding Tool Information

**Scenario:** You need to understand what GLIF is and how it's used

**Steps:**

1. **Navigate to Tool File**
   ```
   G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools\GLIF.json
   ```

2. **Read Tool Data**
   ```json
   {
     "entity_type": "LIBRARIES",
     "tool_id": "TOL-045",
     "name": "GLIF",
     "category": "AI/Workflow Automation",
     "purpose": "AI workflow automation platform",
     "actual_remote_helpers_usage": {
       "primary_use": "Orchestrating multiple AI tools",
       "users": ["Content Creator", "Video Producer"],
       "use_cases": [
         "Automated documentary creation",
         "Thumbnail generation workflows",
         "Content pipeline automation"
       ]
     }
   }
   ```

3. **Find Related Workflows**
   - Search: `ENTITIES/TASK_MANAGERS/Workflows/` for files containing "GLIF" or "TOL-045"
   - Find: `WRF-002_Automated_Documentary_Creation.json`

4. **Understand Complete Usage**
   - Tools used: GLIF orchestrates Perplexity, VAYU, Seedream, Eleven Labs
   - Objects created: miniature documentary videos
   - Professions: Content Creator, Video Producer
   - Department: VID;AID

### Example 2: Creating New Object from Video

**Scenario:** You watched a video about "interactive presentations" and need to add this to taxonomy

**Steps:**

1. **Identify Object Properties**
   - Object Name: "interactive presentations"
   - Category: Documents or Design Deliverables
   - Object Types: ["Clickable presentation", "Interactive slide deck", "Animated presentation"]
   - Tools Mentioned: Gamma, Canva, PowerPoint

2. **Assign Object ID**
   - Check: `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
   - Last OBJ-### is OBJ-042
   - Assign: OBJ-043

3. **Create Object Entry**
   - Open: `ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json`
   - Add:
   ```json
   {
     "object_id": "OBJ-043",
     "object_name": "interactive presentations",
     "category": "Design Deliverables",
     "object_types": [
       "Clickable presentation",
       "Interactive slide deck",
       "Animated presentation",
       "Web-based presentation"
     ],
     "professions": ["Graphic Designer", "Content Creator", "Marketer"],
     "profession_ids": ["PRF-005", "PRF-012", "PRF-008"],
     "tools": ["Gamma", "Canva", "PowerPoint", "Google Slides"],
     "tool_ids": ["TOL-030", "TOL-025", "TOL-010", "TOL-011"],
     "department": "DGN;MKT",
     "complexity": "Medium",
     "time_estimate": "1-3 hours",
     "common_actions": ["Create", "Design", "Animate", "Share"],
     "action_ids": ["ACT-001", "ACT-015", "ACT-042", "ACT-125"]
   }
   ```

4. **Update Master List**
   - Add row to: `Libraries_Master_List.csv`
   - `OBJ-043, interactive presentations, Object, DGN;MKT, Design Deliverables, ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json, 1, Active`

5. **Update Cross-References**
   - Open: `Gamma.json`, `Canva.json`, `PowerPoint.json`
   - Add "interactive presentations" to `objects_created` array
   - Add OBJ-043 to `object_ids` array

### Example 3: Discovering Workflows Using Specific Tool

**Scenario:** You want to know all workflows that use Eleven Labs

**Method 1: Manual Search**

1. **Search Workflow Files**
   ```bash
   cd "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\Workflows"
   grep -r "Eleven Labs" *.json
   ```

2. **Results:**
   - `WRF-002_Automated_Documentary_Creation.json`
   - `WRF-008_Podcast_Production.json`
   - `WRF-015_Educational_Video_Creation.json`

**Method 2: Using Taxonomy**

1. **Open Eleven Labs Tool File**
   - `ENTITIES/LIBRARIES/Tools/AI_Tools/ElevenLabs.json`

2. **Check `actual_remote_helpers_usage.typical_workflows`**
   ```json
   "typical_workflows": [
     {
       "workflow_id": "WRF-002",
       "task": "Automated Documentary Creation",
       "steps": [...]
     },
     {
       "workflow_id": "WRF-008",
       "task": "Podcast Production",
       "steps": [...]
     }
   ]
   ```

3. **Navigate to Specific Workflows**
   - Open workflow files using workflow IDs

### Example 4: Finding All Tools for Design Department

**Scenario:** You need a complete list of tools used by Design department

**Method 1: Using Master List**

1. **Open Tools Master List**
   - `ENTITIES/TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv`

2. **Filter by Department**
   - Look for rows with `DGN` in Department column
   - Results:
     - TOL-006: Midjourney (AI Image Generation)
     - TOL-025: Canva (Design Platform)
     - TOL-046: Nano Banana (Thumbnail Generator)
     - TOL-030: Gamma (Presentation Tool)
     - [More design tools]

**Method 2: Using Department Distribution**

1. **Open Department Distribution**
   - `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Department_Distribution.md`

2. **Navigate to Design Section**
   ```markdown
   ## Design Department (DGN)

   ### Tools (12 total)
   - Midjourney (TOL-006) - AI Image Generation
   - Canva (TOL-025) - Design Platform
   - Figma (TOL-027) - UI Design
   - [Complete list]
   ```

### Example 5: Understanding Profession Requirements

**Scenario:** You're hiring a Content Creator and need to know required skills and tools

**Steps:**

1. **Open Profession File**
   - `ENTITIES/LIBRARIES/Professions/Content_Creator.json`

2. **Review Complete Profile**
   ```json
   {
     "profession_id": "PRF-012",
     "name": "Content Creator",
     "department": "VID;AID",

     "responsibilities": [
       "creating engaging thumbnails optimized for CTR",
       "producing miniature documentaries",
       "automating content workflows with AI agents",
       "editing videos",
       "managing content calendar"
     ],

     "tools_used": [
       {
         "tool_id": "TOL-045",
         "tool_name": "GLIF",
         "purpose": "Workflow automation",
         "frequency": "Daily"
       },
       {
         "tool_id": "TOL-046",
         "tool_name": "Nano Banana",
         "purpose": "Thumbnail generation",
         "frequency": "Weekly"
       }
       // [More tools]
     ],

     "skills_required": [
       {
         "skill_id": "SKL-015",
         "skill_name": "Prompt Engineering",
         "proficiency": "Intermediate",
         "applications": ["AI tool optimization", "thumbnail generation"]
       },
       {
         "skill_id": "SKL-022",
         "skill_name": "Thumbnail Design",
         "proficiency": "Intermediate"
       }
       // [More skills]
     ],

     "workflows_performed": [
       {"workflow_id": "WRF-002", "workflow_name": "Automated Miniature Documentary Creation"},
       {"workflow_id": "WRF-003", "workflow_name": "YouTube Thumbnail Creation"}
     ]
   }
   ```

3. **Create Job Requirements Document**
   - List tools from `tools_used`
   - List skills from `skills_required`
   - List workflows from `workflows_performed`
   - Add responsibilities

### Example 6: Tracking Video Analysis Progress

**Scenario:** You're analyzing multiple videos and need to track progress

**Workflow:**

1. **Video Queue Management**
   - List videos in: `ENTITIES/TASK_MANAGERS/RESEARCHES/01_VIDEO_QUEUE/`
   - Prioritize by relevance, length, tool count

2. **Transcription Phase**
   - Create: `02_TRANSCRIPTIONS/Video_XXX.md` for each video
   - Status: Queued → In Progress → Completed

3. **Analysis Phase**
   - Create: `03_ANALYSIS/Video_XXX_Extraction.md`
   - Extract: Tools, Objects, Actions, Workflows, Professions, Skills

4. **Integration Phase**
   - Create JSON files in appropriate locations
   - Update master lists
   - Establish cross-references

5. **Completion Phase**
   - Create: `03_ANALYSIS/Video_XXX_Library_Mapping_Report.md`
   - Move: Video to `ARCHIVE/` if needed
   - Status: Completed

**Tracking File Example:**
```markdown
# Video Analysis Tracking

| Video ID | Title | Status | Transcription | Analysis | Integration | Report | Priority |
|----------|-------|--------|---------------|----------|-------------|--------|----------|
| 001 | AI Tools Overview | ✅ | ✅ | ✅ | ✅ | ✅ | High |
| 002 | Video Generation | ⏳ | ✅ | ⏳ | ⬜ | ⬜ | High |
| 003 | Thumbnail Design | 📋 | ⬜ | ⬜ | ⬜ | ⬜ | Medium |
| 004 | Workflow Automation | 📋 | ⬜ | ⬜ | ⬜ | ⬜ | Critical |

Legend:
✅ Completed
⏳ In Progress
⬜ Not Started
📋 Queued
```

### Example 7: Using taxonomy_lookup.js Script

**Scenario:** You're building an app and need tool data in app format

**Code Example:**

```javascript
const { getToolData } = require('./scripts/taxonomy_lookup.js');

// Get tool data with defaults
const glifData = getToolData('GLIF', {
  borderColor: '#28a745',
  account: 'team@example.com',
  lastUpdated: '2025-12-04',
  department: ['Developers', 'Videograph']
}, 'G:\\Job\\REMS\\Dropbox');

console.log(glifData);

// Output:
{
  name: 'GLIF',
  url: 'https://glif.app',
  category: ['AI Assistant', 'Automation'],
  description: 'AI workflow automation platform for orchestrating multiple AI tools',
  keyFeatures: [
    'Multi-tool orchestration',
    'Automated workflows',
    'Agent-based pipelines',
    'Integration capabilities',
    'No-code interface'
  ],
  subscription: ['Freemium'],
  account: 'team@example.com',
  lastUpdated: '2025-12-04',
  whatsNew: 'Enhanced VAYU and Seedream integration',
  profession: ['Content Creator', 'Video Producer', 'AI Engineer'],
  responsibility: [
    'Automate Workflows',
    'Manage Information',
    'Create Presentations'
  ],
  department: ['Developers', 'Videograph'],
  borderColor: '#28a745'
}
```

**Use Cases:**
- Building AI tools catalog
- Populating app databases
- Generating documentation
- Creating team dashboards

---

## Best Practices

### 1. ID Assignment Best Practices

**DO:**
✅ Always check Master List for last used ID before assigning new ID
✅ Assign sequential IDs (if last is TOL-045, use TOL-046)
✅ Use leading zeros for consistency (OBJ-001, not OBJ-1)
✅ Update Master List immediately after assigning ID
✅ Document ID in entity JSON file

**DON'T:**
❌ Skip numbers (don't jump from TOL-045 to TOL-050)
❌ Reuse deprecated IDs
❌ Assign IDs without checking Master List
❌ Use arbitrary numbers
❌ Mix ID formats (don't use both TOL-001 and TOOL-001)

### 2. Naming Conventions Best Practices

**DO:**
✅ Use singular nouns for objects (thumbnail, not thumbnails)
✅ Use verb infinitives for actions (create, not creates or creating)
✅ Use descriptive names (Content_Creator.json, not creator.json)
✅ Use consistent capitalization (PascalCase for multi-word names)
✅ Use underscores for file names (Video_Deliverables.json)
✅ Use hyphens for tags (audience-ai, not audience_ai)

**DON'T:**
❌ Use abbreviations unless standard (don't use Cont_Cr for Content_Creator)
❌ Use spaces in file names
❌ Use inconsistent casing
❌ Use special characters (#, @, etc.)
❌ Use overly long names (>50 characters)

### 3. Cross-Referencing Best Practices

**DO:**
✅ Always create bidirectional links (Tool → Object AND Object → Tool)
✅ Use entity IDs in cross-references (TOL-###, OBJ-###, etc.)
✅ Verify IDs exist before referencing
✅ Update all related entities when adding new relationships
✅ Document relationship type (creates, uses, requires, etc.)

**DON'T:**
❌ Create one-way links only
❌ Use entity names without IDs
❌ Reference non-existent IDs
❌ Leave broken references after deletions
❌ Forget to update related entities

### 4. Video Analysis Best Practices

**DO:**
✅ Watch video at normal speed first for context
✅ Take timestamps for tool mentions
✅ Note frequency of tool mentions (importance indicator)
✅ Capture exact tool names and spellings
✅ Document tool relationships (X integrates with Y)
✅ Extract business value and ROI insights
✅ Verify tool URLs before adding to taxonomy

**DON'T:**
❌ Rush through videos at 2x speed
❌ Miss context by skipping sections
❌ Guess tool names (verify correct spelling)
❌ Ignore tool relationships
❌ Skip business value insights
❌ Add tools without verification

### 5. Documentation Best Practices

**DO:**
✅ Create comprehensive mapping reports after video analysis
✅ Document all changes in report
✅ List files created and modified
✅ Include coverage metrics (before/after percentages)
✅ Add recommendations section
✅ Date all documentation
✅ Use consistent markdown formatting

**DON'T:**
❌ Skip report creation
❌ Document changes incompletely
❌ Forget to list modified files
❌ Omit metrics and statistics
❌ Leave undated documentation
❌ Use inconsistent formatting

### 6. JSON File Best Practices

**DO:**
✅ Validate JSON syntax before saving
✅ Use consistent indentation (2 or 4 spaces)
✅ Include all required fields
✅ Use arrays for multiple values
✅ Keep files under 1000 lines (split if larger)
✅ Add comments using special fields like "_comment"

**DON'T:**
❌ Save invalid JSON
❌ Mix tabs and spaces
❌ Omit required fields
❌ Use strings for multiple values (use arrays)
❌ Create massive files (hard to maintain)
❌ Use actual JSON comments (not supported in standard JSON)

### 7. Workflow Documentation Best Practices

**DO:**
✅ Document every step in detail
✅ Include tool IDs for all tools used
✅ Specify input and output for each step
✅ Estimate duration for each step
✅ Document automation level
✅ Include business value section
✅ List optimization tips

**DON'T:**
❌ Skip steps (document all, even obvious ones)
❌ Reference tools by name only (use IDs)
❌ Forget inputs/outputs
❌ Skip duration estimates
❌ Omit automation information
❌ Forget business impact
❌ Leave out optimization guidance

### 8. Master List Maintenance Best Practices

**DO:**
✅ Update master lists immediately after creating entities
✅ Keep master lists sorted by ID
✅ Verify no duplicate IDs before adding
✅ Include all metadata columns
✅ Mark deprecated entities clearly
✅ Back up master lists regularly

**DON'T:**
❌ Delay master list updates
❌ Leave master lists unsorted
❌ Skip duplicate checks
❌ Omit metadata
❌ Delete deprecated entities (mark instead)
❌ Work without backups

### 9. Taxonomy Version Control Best Practices

**DO:**
✅ Use git for version control
✅ Commit after each video analysis completion
✅ Write descriptive commit messages
✅ Tag major taxonomy updates
✅ Create branches for major changes
✅ Document changes in CHANGELOG.md

**DON'T:**
❌ Work without version control
❌ Batch multiple videos in one commit
❌ Use generic commit messages ("updated files")
❌ Skip tagging major versions
❌ Work directly on main branch for big changes
❌ Forget to document changes

### 10. Quality Assurance Best Practices

**DO:**
✅ Verify all tool names against official sources
✅ Check all URLs before adding to taxonomy
✅ Validate all cross-references
✅ Test workflows before documenting
✅ Proofread all documentation
✅ Run validation scripts (when available)

**DON'T:**
❌ Trust video names without verification
❌ Add URLs without checking (links break)
❌ Skip cross-reference validation
❌ Document untested workflows
❌ Skip proofreading
❌ Skip automated validation

---

## Troubleshooting

### Problem 1: Can't Find Tool in Taxonomy

**Symptoms:**
- Tool mentioned in video doesn't exist in `AI_Tools/` folder
- `taxonomy_lookup.js` returns null

**Solutions:**

1. **Check Alternative Names**
   - Tool might be filed under variant name
   - Examples: "GPT" → "ChatGPT.json", "MJ" → "Midjourney.json"
   - Search all files: `grep -r "tool_name" AI_Tools/`

2. **Check Other Tool Categories**
   - Tool might be in `Development_Tools/` or other categories
   - Search entire Tools folder: `grep -r "tool_name" Tools/`

3. **Tool Genuinely Missing**
   - Follow "How to Update Taxonomy → Scenario 1: Adding a New Tool"
   - Create new tool file
   - Update master lists

### Problem 2: Duplicate IDs Found

**Symptoms:**
- Two entities have same ID
- Master list shows duplicate entries
- Cross-references ambiguous

**Solutions:**

1. **Identify Duplicate**
   - Search master list for duplicate ID: `grep "TOL-045" Libraries_Master_List.csv`
   - Find both entities using this ID

2. **Determine Which is Correct**
   - Check creation dates
   - Check which is referenced more
   - Check which has more complete data

3. **Reassign ID to Duplicate**
   - Find next available ID
   - Update entity JSON file
   - Update all cross-references
   - Update master list

4. **Validate Fix**
   - Search entire codebase for old ID: `grep -r "TOL-045" .`
   - Verify no broken references

### Problem 3: Broken Cross-References

**Symptoms:**
- Tool references object that doesn't exist
- Object references tool that doesn't exist
- IDs don't match any entity

**Solutions:**

1. **Identify Broken Reference**
   - Look for referenced ID in master list
   - Example: Tool file references "OBJ-999" but OBJ-999 doesn't exist

2. **Determine Cause**
   - ID typo (OBJ-099 vs OBJ-999)
   - Entity deleted but reference not updated
   - Entity not created yet

3. **Fix Based on Cause**
   - **If typo:** Correct ID in reference
   - **If deleted:** Remove reference or replace with correct entity
   - **If not created:** Create entity with referenced ID

4. **Verify Bidirectional Links**
   - Ensure reverse link exists (if Tool → Object, then Object → Tool)
   - Update missing reverse links

### Problem 4: Master List Out of Sync

**Symptoms:**
- Entity JSON files exist but not in master list
- Master list shows entities that don't exist as files
- Count discrepancies

**Solutions:**

1. **Audit Files vs Master List**
   ```bash
   # Count actual files
   ls AI_Tools/*.json | wc -l

   # Count master list entries
   grep "^TOL-" Libraries_Master_List.csv | wc -l
   ```

2. **Find Missing Entries**
   - Compare file list to master list
   - Identify files without master list entries

3. **Add Missing Entries**
   - For each missing file, add row to master list
   - Include all metadata columns

4. **Remove Phantom Entries**
   - For master list entries without files, investigate
   - If file was deleted, remove or mark as "Archived" in master list

### Problem 5: Inconsistent Naming Conventions

**Symptoms:**
- Some files use spaces, some use underscores
- Some use camelCase, some use PascalCase
- Inconsistent tag formats

**Solutions:**

1. **Establish Standard**
   - Refer to "Best Practices → Naming Conventions"
   - PascalCase for multi-word file names
   - Underscores for separating words
   - Lowercase with hyphens for tags

2. **Rename Files**
   ```bash
   # Example: Rename space-separated files
   mv "Video Deliverables.json" "Video_Deliverables.json"
   ```

3. **Update References**
   - Search for old file name in all files
   - Update paths in cross-references
   - Update master lists

4. **Document Standard**
   - Add naming convention to README
   - Create checklist for new entities

### Problem 6: JSON Syntax Errors

**Symptoms:**
- JSON files won't parse
- Script errors when reading files
- Invalid JSON warnings

**Solutions:**

1. **Validate JSON**
   - Use online validator: jsonlint.com
   - Or command line: `jq . file.json`
   - Or VS Code: JSON validation built-in

2. **Common JSON Errors**
   - **Trailing commas:** Remove comma after last array/object item
   - **Unquoted keys:** Add quotes around all object keys
   - **Single quotes:** Use double quotes for strings
   - **Missing commas:** Add commas between array/object items
   - **Unclosed brackets:** Ensure all `{`, `[` have matching `}`, `]`

3. **Fix Errors**
   - Correct syntax based on error message
   - Re-validate after each fix

4. **Prevent Future Errors**
   - Use JSON-aware editor (VS Code, Sublime)
   - Enable JSON linting
   - Use formatter (Prettier)

### Problem 7: Can't Determine Correct Department

**Symptoms:**
- Tool could belong to multiple departments
- Unclear which department should own entity
- Cross-department collaboration unclear

**Solutions:**

1. **Check Department Codes**
   - Refer to: `Libraries_ISO_Code_Registry.md` or `Taxonomy_ISO_Code_Registry.md`
   - Department codes:
     - AIA/AID = AI & Automation
     - DEV = Development
     - DGN = Design
     - VID = Video
     - etc.

2. **Assign Primary Department**
   - Where is tool used most?
   - Which department initiated tool adoption?
   - Which department's budget pays for tool?

3. **Use Multiple Department Codes**
   - Format: `VID;AID` (Video primary, AI secondary)
   - Semicolon-separated list
   - Order by importance

4. **Document in Tool File**
   - List all departments in `departments_using` field
   - Explain usage per department in `actual_remote_helpers_usage`

### Problem 8: Overwhelmed by Video Complexity

**Symptoms:**
- Video mentions 20+ tools
- Can't keep track of all extractions
- Analysis taking too long

**Solutions:**

1. **Prioritize by Frequency**
   - Focus on tools mentioned 5+ times first
   - Mark critical tools (mentioned 10+ times)
   - Defer low-priority tools (mentioned 1-2 times)

2. **Break Into Phases**
   - **Phase 1:** Extract critical tools only (1 hour)
   - **Phase 2:** Extract high-priority tools (1 hour)
   - **Phase 3:** Extract remaining tools (1 hour)
   - **Phase 4:** Workflows and cross-references (1 hour)

3. **Use PMT-009 Structure**
   - Follow structured workflow
   - Complete one section at a time
   - Don't jump between sections

4. **Create Working Document**
   - Use checklist format:
   ```markdown
   ## Tools Extraction Progress
   - [✅] GLIF (30 mentions) - TOL-045 - DONE
   - [⏳] Nano Banana (8 mentions) - TOL-046 - IN PROGRESS
   - [⬜] VAYU (10 mentions) - Need to create
   - [⬜] Sora (15 mentions) - Need to create
   ```

### Problem 9: Unclear How to Structure Workflow

**Symptoms:**
- Workflow has many steps, unclear how to break down
- Uncertain which tool goes in which step
- Duration estimates unclear

**Solutions:**

1. **Watch Video Section Again**
   - Re-watch workflow demonstration
   - Note exact sequence of actions
   - Take timestamps for each step

2. **Map Tool to Action to Output**
   ```
   Step 1:
   - Action: Research
   - Tool: Perplexity
   - Input: Historical topic
   - Output: Verified facts
   - Duration: 2-3 minutes
   ```

3. **Use Template**
   ```json
   {
     "step_number": 1,
     "action": "[Action verb]",
     "description": "[What happens]",
     "tool_id": "TOL-###",
     "tool_name": "[Tool]",
     "input": "[What's needed]",
     "output": "[What's created]",
     "duration": "[Time estimate]"
   }
   ```

4. **Test Workflow**
   - If possible, actually execute workflow
   - Verify steps are correct and in right order
   - Adjust duration estimates based on reality

### Problem 10: Script Errors with taxonomy_lookup.js

**Symptoms:**
- Script can't find taxonomy folder
- Returns null for existing tools
- Mapping errors

**Solutions:**

1. **Check Workspace Path**
   ```javascript
   // Ensure correct path (Windows)
   const workspaceRoot = 'G:\\Job\\REMS\\Dropbox';

   // Or use forward slashes (works on Windows)
   const workspaceRoot = 'G:/Job/REMS/Dropbox';
   ```

2. **Verify Taxonomy Folder Structure**
   ```bash
   # Check if folders exist
   ls "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"
   ```

3. **Check Tool Name Mapping**
   - Look at `getTaxonomyFileName()` function
   - Add custom mapping if tool name doesn't match file name:
   ```javascript
   const nameMap = {
     'Your Tool': 'Your_Tool.json',
     // Add more mappings
   };
   ```

4. **Debug Script**
   ```javascript
   // Add console.log to see what's happening
   const toolData = lookupToolInTaxonomy('GLIF', workspaceRoot);
   console.log('Tool data:', toolData);
   console.log('Workspace root:', workspaceRoot);
   ```

---

## Appendix A: Quick Reference

### ISO Code Cheat Sheet

**LIBRARIES Codes:**
- RSP = Responsibilities
- ACT = Actions
- OBJ = Objects
- PRM = Parameters
- TOL = Tools
- SKL = Skills
- PRF = Professions
- DPT = Departments

**TASK_MANAGERS Codes:**
- PRT = Project Templates
- MLT = Milestone Templates
- TST = Task Templates
- STT = Step Templates
- CHT = Checklist Templates
- WRF = Workflows
- GDS = Guides
- PMT = Prompts
- RSR = Research

**Department Codes:**
- AIA/AID = AI & Automation
- DEV = Development
- HRM = Human Resources
- LGN = Lead Generation
- DGN = Design
- VID = Video Production
- SLS = Sales
- SMM = Social Media Management
- FIN = Finance

### File Location Cheat Sheet

| What | Where |
|------|-------|
| Central Taxonomy Hub | `ENTITIES/TAXONOMY/README.md` |
| Tool JSON Files | `ENTITIES/LIBRARIES/Tools/AI_Tools/` |
| Object Definitions | `ENTITIES/LIBRARIES/Responsibilities/Objects/` |
| Action Definitions | `ENTITIES/LIBRARIES/Responsibilities/Actions/` |
| Workflow Files | `ENTITIES/TASK_MANAGERS/Workflows/` |
| Profession Files | `ENTITIES/LIBRARIES/Professions/` |
| Skill Definitions | `ENTITIES/LIBRARIES/Skills/Master/` |
| Video Transcriptions | `ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/` |
| Analysis Reports | `ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/` |
| Video Prompts | `ENTITIES/PROMPTS/` |
| Master Lists | `ENTITIES/TAXONOMY/TAX-001_Libraries/` or `TAX-002_Task_Managers/` |
| Taxonomy Scripts | `Design Nov25/.../scripts/` |

### Prompt Cheat Sheet

| Prompt | Use When | Time Required |
|--------|----------|---------------|
| PMT-004 | Need to transcribe video | 30-60 min |
| PMT-005 | Need to normalize video title | 5 min |
| PMT-006 | Need basic video analysis | 30-45 min |
| PMT-008 | Need deep video analysis | 45-60 min |
| PMT-009 | Ready for full taxonomy integration | 2.5-4 hours |
| PMT-007 | Need focused object extraction | 30 min |
| PMT-015 | Need to improve transcription | 15-30 min |
| PMT-090 | Processing YouTube video | 30-60 min |

### Common Commands Cheat Sheet

**Search for tool:**
```bash
cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"
ls *.json | grep -i "tool_name"
```

**Find last ID:**
```bash
grep "^TOL-" Libraries_Master_List.csv | tail -1
```

**Validate JSON:**
```bash
jq . file.json
```

**Search all files for reference:**
```bash
grep -r "TOL-045" .
```

**Count entities:**
```bash
ls AI_Tools/*.json | wc -l
```

### Validation Checklist

Before considering taxonomy update complete:

- [ ] All new entities have assigned IDs
- [ ] Master lists updated
- [ ] All JSON files validated
- [ ] All cross-references bidirectional
- [ ] Tool files reference objects created
- [ ] Object files reference tools used
- [ ] Workflow files reference all entities with IDs
- [ ] Profession files reference all tools, objects, workflows with IDs
- [ ] All files saved in correct locations
- [ ] Analysis report created
- [ ] Changes committed to version control

---

## Appendix B: Template Library

### Tool JSON Template

```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOL-###",
  "name": "[Tool Name]",
  "vendor": "[Vendor/Company]",
  "category": "[Category - see ISO Code Registry]",
  "purpose": "[Brief purpose statement]",
  "description": "[Detailed description]",
  "skill_level_required": "[Beginner/Intermediate/Advanced]",
  "cost_structure": "[Free/Paid/Freemium - details]",
  "platform_compatibility": ["Web", "Desktop", "Mobile", "API"],
  "integration_capabilities": [
    "[Integration 1]",
    "[Integration 2]"
  ],
  "documentation_url": "[Official docs URL]",
  "actual_remote_helpers_usage": {
    "primary_use": "[How we use it]",
    "users": ["[Profession 1]", "[Profession 2]"],
    "use_cases": [
      "[Use case 1]",
      "[Use case 2]"
    ],
    "typical_workflows": [
      {
        "task": "[Workflow name]",
        "steps": ["[Step 1]", "[Step 2]"],
        "complexity": "[Low/Medium/High]",
        "time_estimate": "[Time]"
      }
    ],
    "integration_with_other_tools": ["[Tool 1]", "[Tool 2]"]
  },
  "strengths": [
    "[Strength 1]",
    "[Strength 2]"
  ],
  "limitations": [
    "[Limitation 1]",
    "[Limitation 2]"
  ],
  "tags": ["[tag1]", "[tag2]"]
}
```

### Object JSON Template

```json
{
  "object_id": "OBJ-###",
  "object_name": "[object name - singular]",
  "category": "[Category - see ISO Code Registry]",
  "object_types": [
    "[Type 1]",
    "[Type 2]"
  ],
  "professions": ["[Profession 1]", "[Profession 2]"],
  "profession_ids": ["PRF-###", "PRF-###"],
  "tools": ["[Tool 1]", "[Tool 2]"],
  "tool_ids": ["TOL-###", "TOL-###"],
  "skills": ["SKL-###"],
  "department": "[DPT codes - semicolon separated]",
  "parameters": ["[param1]", "[param2]"],
  "complexity": "[Low/Medium/High]",
  "time_estimate": "[Time range]",
  "common_actions": ["[Action 1]", "[Action 2]"],
  "action_ids": ["ACT-###", "ACT-###"],
  "storage_pattern": "[File path pattern]",
  "platforms_used": ["[Platform 1]", "[Platform 2]"],
  "ai_tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "[Tool]",
      "usage": "[How used]"
    }
  ],
  "optimization_metrics": ["[Metric 1]", "[Metric 2]"],
  "best_practices": [
    "[Practice 1]",
    "[Practice 2]"
  ],
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "[Workflow]"
    }
  ],
  "related_professions": ["[Profession 1]", "[Profession 2]"]
}
```

### Workflow JSON Template

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WRF-###",
  "workflow_name": "[Workflow Name]",
  "category": "[Category]",
  "description": "[Description]",
  "objective": "[Goal/Objective]",
  "workflow_type": "[Manual/Semi-Automated/Fully Automated/AI Pipeline]",
  "duration": "[Total time]",
  "complexity": "[Low/Medium/High (for user), Low/Medium/High (for setup)]",
  "steps": [
    {
      "step_number": 1,
      "action": "[Action]",
      "description": "[Description]",
      "tool_id": "TOL-###",
      "tool_name": "[Tool]",
      "input": "[Input]",
      "output": "[Output]",
      "duration": "[Time]"
    }
  ],
  "tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "[Tool]",
      "role": "[Role/Purpose]"
    }
  ],
  "objects_created": [
    {
      "object_id": "OBJ-###",
      "object_name": "[Object]",
      "object_type": "[Type]",
      "format": "[Format]",
      "duration": "[Duration if media]"
    }
  ],
  "objects_used": [
    {
      "object_id": "OBJ-###",
      "object_name": "[Object]",
      "object_type": "[Type]",
      "role": "[Role]"
    }
  ],
  "actions_performed": ["[Action 1]", "[Action 2]"],
  "action_ids": ["ACT-###", "ACT-###"],
  "professions_involved": ["[Profession 1]", "[Profession 2]"],
  "profession_ids": ["PRF-###", "PRF-###"],
  "skills_required": [
    {
      "skill_id": "SKL-###",
      "skill_phrase": "[phrase]"
    }
  ],
  "department": "[DPT codes]",
  "input_requirements": "[What's needed]",
  "output_deliverables": "[What's produced]",
  "automation_level": "[Fully Automated/Semi-Automated/Manual]",
  "business_value": [
    "[Value 1]",
    "[Value 2]"
  ],
  "use_cases": [
    "[Use case 1]",
    "[Use case 2]"
  ],
  "platforms_served": ["[Platform 1]", "[Platform 2]"],
  "optimization_tips": [
    "[Tip 1]",
    "[Tip 2]"
  ],
  "related_workflows": ["[Workflow 1]", "[Workflow 2]"],
  "tags": ["[tag1]", "[tag2]"]
}
```

### Profession JSON Template

```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_id": "PRF-###",
  "name": "[Profession Name]",
  "department": "[DPT codes]",
  "description": "[Description]",
  "responsibilities": [
    "[Responsibility 1]",
    "[Responsibility 2]"
  ],
  "objects_worked_with": [
    {
      "object_id": "OBJ-###",
      "object_name": "[Object]",
      "object_types": ["[Type 1]", "[Type 2]"],
      "actions": ["[Action 1]", "[Action 2]"],
      "action_ids": ["ACT-###", "ACT-###"]
    }
  ],
  "tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "[Tool]",
      "purpose": "[Purpose]",
      "frequency": "[Daily/Weekly/Monthly]"
    }
  ],
  "workflows_performed": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "[Workflow]"
    }
  ],
  "skills_required": [
    {
      "skill_id": "SKL-###",
      "skill_name": "[Skill]",
      "skill_phrase": "[phrase]",
      "proficiency": "[Beginner/Intermediate/Advanced]",
      "applications": ["[App 1]", "[App 2]"]
    }
  ],
  "typical_day": [
    "[Activity 1]",
    "[Activity 2]"
  ],
  "success_metrics": [
    "[Metric 1]",
    "[Metric 2]"
  ]
}
```

### Skill JSON Template

```json
{
  "skill_id": "SKL-###",
  "skill_name": "[Skill Name]",
  "skill_phrase": "[action] [object/topic] using [tool]",
  "definition": "[Clear description]",
  "proficiency_levels": ["Beginner", "Intermediate", "Advanced"],
  "applications": [
    "[Application 1]",
    "[Application 2]"
  ],
  "tools": ["[Tool 1]", "[Tool 2]"],
  "tool_ids": ["TOL-###", "TOL-###"],
  "related_actions": ["[action1]", "[action2]"],
  "action_ids": ["ACT-###", "ACT-###"],
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "[Object]"
    }
  ],
  "professions": ["[Profession 1]", "[Profession 2]"],
  "profession_ids": ["PRF-###", "PRF-###"],
  "department": "[DPT codes]",
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "[Workflow]"
    }
  ],
  "learning_resources": [
    "[Resource 1]",
    "[Resource 2]"
  ]
}
```

---

## Appendix C: Glossary

**Action (ACT):** A verb describing an activity performed on objects using tools. Examples: create, generate, optimize, analyze.

**Bidirectional Link:** Cross-reference that works both ways. If Tool references Object, Object should reference Tool.

**Canonical Source:** The authoritative, original location of data. Changes should be made to canonical source first.

**Consonant-Only Code:** ID system using only consonant letters (no vowels: A, E, I, O, U) for consistency and uniqueness.

**Cross-Reference:** Link between entities using IDs. Enables navigation and relationship tracking.

**Department Code:** 3-letter code identifying organizational department (AIA, DEV, DGN, VID, etc.).

**Entity:** Any classified item in taxonomy (tool, object, action, workflow, profession, etc.).

**Entity Type:** Top-level category of entities (LIBRARIES, TASK_MANAGERS, PROMPTS, etc.).

**Gap Analysis:** Process of identifying missing elements in taxonomy by comparing extracted data to existing taxonomy.

**Hierarchy:** Parent-child relationships between entities (Project → Milestone → Task → Step).

**ISO Code:** International Standards Organization-style 3-letter code for entity types (RSP, ACT, OBJ, TOL, etc.).

**JSON:** JavaScript Object Notation - file format used for structured data storage in taxonomy.

**Master List:** CSV file containing catalog of all entities of a specific type with metadata.

**Mirrored View:** Copy of canonical data placed in TAXONOMY entity for easy navigation (not authoritative).

**Object (OBJ):** Noun representing a deliverable, output, or tangible item. Examples: thumbnails, videos, scripts.

**Profession (PRF):** Job role or title with associated responsibilities, tools, objects, and workflows.

**Prompt (PMT):** Structured instruction set for AI or human to perform specific taxonomy-related task.

**Research (RSR):** Analysis of source material (video, document, interview) to extract taxonomy elements.

**Responsibility (RSP):** Core work responsibility or duty associated with profession or department.

**Skill (SKL):** Combination of responsibility and tool, representing competency. Format: "action + object using tool".

**Sub-Entity:** Specific type within entity type. Example: "Tool" is sub-entity of "LIBRARIES".

**Tag:** Metadata label enabling flexible search and filtering beyond type/category. Format: lowercase-with-hyphens.

**Taxonomy:** Standardized classification system for organizing and relating all knowledge, workflows, and entities.

**Tool (TOL):** Software, platform, service, or application used to perform work. Examples: GLIF, Claude, Midjourney.

**Transcription:** Written text version of video audio with timestamps and speaker identification.

**Workflow (WRF):** Sequence of steps using tools to transform inputs into outputs. Can be manual, semi-automated, or fully automated.

---

## Document Metadata

**Document Title:** Complete Taxonomy System Documentation - Video Taxonomy Generation, Usage, and Management Guide

**Document ID:** TAX-DOC-001

**Version:** 1.0.0

**Created:** 2025-12-04

**Last Updated:** 2025-12-04

**Status:** Active - Comprehensive Reference

**Author:** System Analysis & Documentation Team

**Purpose:** Provide complete guide to taxonomy system including video taxonomy generation, usage, scripts, prompts, and information captured.

**Target Audience:**
- Taxonomy maintainers
- Video analysts
- AI automation engineers
- Documentation specialists
- New team members learning the system

**Related Documents:**
- `ENTITIES/TAXONOMY/README.md` - Central taxonomy hub
- `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md` - LIBRARIES codes
- `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md` - TASK_MANAGERS codes
- `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md` - Video integration workflow
- `ENTITIES_2.0/SETTINGS/_Taxonomy/TAX-RDM-001_Types.md` - README taxonomy types

**Location:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\taxonomy_complete_guide.md`

**Total Pages:** ~100 (estimated when printed)

**Total Words:** ~25,000

**Total Characters:** ~175,000

---

**END OF DOCUMENTATION**
