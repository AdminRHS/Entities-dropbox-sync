# Taxonomy Analysis and Updates Prompt
## Complete Video Transcription to Taxonomy Integration Workflow

**Purpose**: Full end-to-end process for analyzing video transcriptions and updating the entire taxonomy system (Tools, Actions, Objects, Processes, Professions, Skills, Responsibilities).

**Version**: 2.0 - Taxonomy Architecture Alignment
**Date**: 2025-11-25
**Status**: Active - Production Ready
**Last Updated**: 2025-11-25

---

## Overview

This prompt guides you through the complete process of:
1. Analyzing video transcriptions for taxonomy elements
2. Identifying gaps in existing libraries
3. Creating new library entries (Tools, Objects, Actions, etc.)
4. Updating existing library entries
5. Cross-referencing and linking all entities
6. Generating comprehensive analysis reports

---

## Phase 1: Initial Video Analysis (30-45 minutes)

### Step 1: Read and Inventory

**Input**: Video transcription file (`Video_XXX.md`)

**Task**: Create comprehensive inventory of all taxonomy elements

#### 1.1 Tools Inventory
Extract ALL tools and technologies mentioned:
```
TOOLS FOUND:
- [Tool Name 1] - [Category] - [First mention timestamp] - [Frequency count]
- [Tool Name 2] - [Category] - [First mention timestamp] - [Frequency count]
[Continue...]

TOOL CATEGORIES IDENTIFIED:
- AI/Video Generation: [Count]
- AI/Image Generation: [Count]
- AI/Audio Generation: [Count]
- AI/Workflow Automation: [Count]
- Research: [Count]
[Continue...]
```

#### 1.2 Objects Inventory
Extract ALL deliverables, outputs, and tangible items:
```
OBJECTS FOUND:
- thumbnails (Design Deliverable) - "YouTube thumbnails", "Mr. Beast style thumbnails"
- videos (Media) - "miniature documentaries", "TikTok videos", "social media content"
- scripts (Documents) - "documentary scripts", "voiceover scripts"
- images (Media) - "reference images", "concept art"
- voiceovers (Media) - "narration audio", "professional voice"
[Continue...]

OBJECT TYPES IDENTIFIED:
Design Deliverables:
  - Thumbnails [YouTube thumbnail, Social thumbnail, High-CTR thumbnail]
  - Videos [Documentary video, Social video, AI video]

Documents:
  - Scripts [Documentary script, Voiceover script, Video script]

Media:
  - Images [Reference image, Concept art, Generated image]
  - Audio [Voiceover, Narration, Background music]
[Continue...]
```

#### 1.3 Actions Inventory
Extract ALL action verbs categorized:
```
ACTIONS FOUND (By Category):

CREATION VERBS:
- create (15x) - [00:45], [02:30], [05:12]...
- generate (23x) - [01:20], [03:15], [06:45]...
- design (8x) - [02:34], [04:50]...
- build (5x) - [07:20], [09:15]...
- produce (7x) - [03:10], [08:25]...

MODIFICATION VERBS:
- optimize (12x) - [03:20], [05:40], [08:15]...
- refine (6x) - [04:10], [07:30]...
- customize (4x) - [06:00], [09:45]...
- enhance (3x) - [05:25], [10:10]...

ANALYSIS VERBS:
- research (8x) - [06:20], [08:50]...
- review (7x) - [04:25], [09:10]...
- analyze (5x) - [05:55], [11:30]...

ORGANIZATION VERBS:
- organize (3x) - [07:15], [12:05]...
- structure (2x) - [08:40]...
- schedule (1x) - [09:50]...

COMMUNICATION VERBS:
- publish (6x) - [08:45], [13:20]...
- share (4x) - [10:15]...
- export (5x) - [06:35], [11:25]...
```

#### 1.4 Processes/Workflows Inventory
```
WORKFLOWS IDENTIFIED:

1. WORKFLOW: Automated Miniature Documentary Creation
   OBJECTIVE: Generate 32-second historical documentary with research, visuals, narration
   STEPS:
     1. Research historical facts (Perplexity)
     2. Generate documentary script (AI)
     3. Create tilt-shift video (VAYU 2.2 + Seedream)
     4. Generate voiceover (Eleven Labs)
     5. Combine elements (GLIF automation)
     6. Review and publish
   DURATION: 10-20 minutes (automated)
   TOOLS: GLIF, Perplexity, VAYU, Seedream, Eleven Labs
   INPUT: Historical topic
   OUTPUT: 32-second documentary (MP4)
   OBJECT CREATED: videos [miniature documentary]

2. WORKFLOW: YouTube Thumbnail Creation (High CTR)
   OBJECTIVE: Generate YouTube thumbnail optimized for click-through rate
   STEPS:
     1. Define thumbnail concept
     2. Generate image (Nano Banana via GLIF)
     3. Refine prompt for style
     4. Select best variant
     5. Add text overlay
     6. Export final thumbnail
   DURATION: 15 minutes
   TOOLS: GLIF, Nano Banana
   INPUT: Video concept, style reference
   OUTPUT: YouTube thumbnail (PNG, 1920x1080)
   OBJECT CREATED: thumbnails [YouTube thumbnail, High-CTR thumbnail]

[Continue for all workflows...]
```

#### 1.5 Professions/Roles Inventory
```
PROFESSIONS MENTIONED:
- Content Creator - creates videos, thumbnails, social content
- Video Producer - orchestrates multi-tool workflows, documentary production
- YouTuber - creates thumbnails, optimizes CTR, builds audience
- Social Media Manager - optimizes content for platforms, manages calendar
- Prompt Engineer - refines AI prompts, optimizes outputs
- Marketer - creates promotional content, brand stories
- Documentary Producer - creates educational content, historical videos

RESPONSIBILITIES EXTRACTED:
Content Creator:
  - "creating thumbnails" [09:15]
  - "editing videos" [09:15]
  - "optimizing for social media" [09:15]
  - "managing content calendar" [09:15]
  - "automating workflows" [implied]

YouTuber:
  - "optimizing for CTR" [03:20]
  - "creating engaging thumbnails" [02:34]
  - "building audience" [12:10]

[Continue...]
```

#### 1.6 Skills Inventory
```
SKILLS IDENTIFIED:
- Prompt engineering - [01:45] "crafting effective AI prompts"
- Video editing - [05:30] "traditional editing skills augmented by AI"
- Thumbnail design - [03:15] "creating high-CTR thumbnails"
- Content strategy - [12:10] "planning content for audience building"
- Workflow automation - [08:50] "setting up agent-based pipelines"
- Style optimization - [03:20] "understanding visual aesthetics for engagement"
- Research skills - [06:25] "fact-checking historical content"
- Social media optimization - [09:15] "optimizing for platforms"

SKILL CATEGORIES:
Technical Skills:
  - Prompt engineering
  - Workflow automation
  - Video editing

Creative Skills:
  - Thumbnail design
  - Style optimization
  - Visual storytelling

Strategic Skills:
  - Content strategy
  - Social media optimization
  - Audience building
```

---

## Phase 2: Gap Analysis (20-30 minutes)

### Step 2: Check Existing Taxonomy

For EACH element extracted, check if it exists in the taxonomy:

#### 2.1 Tools Gap Analysis

**Check**: `ENTITIES/LIBRARIES/Tools/AI_Tools/*.json`

```
TOOLS GAP ANALYSIS:

✅ EXISTS (Enhance):
- ElevenLabs.json → ADD: GLIF integration, miniature documentary workflow
- Perplexity.json → ADD: documentary research use case, fact-checking workflow
- Midjourney.json → ADD: thumbnail generation workflow, CTR optimization

❌ MISSING (Create):
Priority: CRITICAL
- GLIF.json → AI Workflow Automation platform (mentioned 30+ times, core tool)
- Sora.json → OpenAI video generation (mentioned 15+ times)
- Kling.json → Fast video generation (mentioned 12+ times)

Priority: HIGH
- Nano_Banana.json → YouTube thumbnail specialist (mentioned 8 times)
- VAYU.json → Miniature documentary video (mentioned 10 times)
- Seedream.json → Tilt-shift effects (pairs with VAYU, 8 mentions)

Priority: MEDIUM
- Cdans.json → Animation tool (mentioned 2 times)

COVERAGE METRICS:
Total Tools Mentioned: 10
Existing in Taxonomy: 3 (30%)
Missing from Taxonomy: 7 (70%)
TARGET: 100% coverage
```

#### 2.2 Objects Gap Analysis

**Check**: `ENTITIES/LIBRARIES/Responsibilities/Objects/*.json`

```
OBJECTS GAP ANALYSIS:

✅ EXISTS (Verify & Enhance):
Check Design_Deliverables.json:
  - Banners ✓ (exists)
  - Logos ✓ (exists)
  - Illustrations ✓ (exists)
  - UI Mockups ✓ (exists)
  - Presentations ✓ (exists)

Check if exists:
  - Thumbnails → Need to ADD if missing
  - Videos → Need to ADD if missing
  - Scripts → Check Documents.json
  - Voiceovers → Need to ADD if missing
  - Documentaries → Need to ADD if missing

❌ MISSING (Create or Add to Existing):

For Design_Deliverables.json:
  ADD object_types to "Thumbnails" (if exists):
    - YouTube thumbnail
    - Social media thumbnail
    - High-CTR thumbnail
    - Mr. Beast style thumbnail

  If "Thumbnails" missing, CREATE new object entry:
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "category": "Design Deliverables",
      "object_types": ["YouTube thumbnail", "Social thumbnail", "High-CTR thumbnail"],
      "professions": ["Content Creator", "Graphic Designer", "YouTuber"],
      "profession_ids": ["PRF-###", "PRF-###", "PRF-###"],
      "tools": ["Nano Banana", "GLIF", "Photoshop", "Midjourney"],
      "tool_ids": ["TOL-###", "TOL-###", "TOL-###", "TOL-###"],
      "skills": ["SKL-###"],
      "department": "VID;DGN",
      "complexity": "Low to Medium",
      "time_estimate": "15-30 minutes",
      "common_actions": ["Create", "Generate", "Optimize", "Design"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"],
      "platforms_used": ["YouTube", "Social Media"],
      "ai_tools_used": [
        {
          "tool_id": "TOL-###",
          "tool_name": "Nano Banana",
          "usage": "via GLIF"
        },
        {
          "tool_id": "TOL-###",
          "tool_name": "Midjourney",
          "usage": "concept exploration"
        }
      ]
    }

For Media Objects (create new file or add to existing):
  CREATE "Videos" object:
    object_types: ["Miniature documentary", "TikTok video", "Social video", "AI video"]

  CREATE "Voiceovers" object:
    object_types: ["Documentary narration", "Educational voiceover", "AI voiceover"]

  CREATE "Scripts" object (or add to Documents.json):
    object_types: ["Documentary script", "Voiceover script", "Video script"]

CROSS-REFERENCE REQUIREMENT:
Each object must link to:
  - Tools used to create it (with TOL-### IDs)
  - Actions performed on it (with ACT-### IDs)
  - Professions that work with it (with PRF-### IDs)
  - Skills that involve it (with SKL-### IDs)
  - Workflows that produce it (with WRF-### IDs)
  - Department codes (ISO format: AID, DEV, HRM, LGN, DGN, VID, SLS, SMM, FIN)
```

#### 2.3 Actions Gap Analysis

**Check**: `ENTITIES/LIBRARIES/Responsibilities/Actions/*.json`

```
ACTIONS GAP ANALYSIS:

Check existing action files for:
- `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`
- Or category-specific files in Actions directory

For each action verb found in video:
  ✅ If EXISTS → Note frequency increase, add new contexts
  ❌ If MISSING → Add to appropriate category file

ACTIONS TO ADD/UPDATE:

Actions_Master.json (or appropriate category file):
  - "create" (ACT-###) → ADD context: "create thumbnails", "create documentaries"
  - "generate" (ACT-###) → ADD context: "generate videos", "generate scripts"
  - "design" (ACT-###) → ADD context: "design thumbnails for CTR"
  - "produce" (ACT-###) → ADD context: "produce miniature documentaries"
  - "optimize" (ACT-###) → ADD context: "optimize for CTR", "optimize thumbnails"
  - "refine" (ACT-###) → ADD context: "refine prompts", "refine style"

**Note**: All actions must include action_id (ACT-###) and link to objects with OBJ-### IDs

[Continue for all categories...]
```

#### 2.4 Workflows Gap Analysis

**Check**: `ENTITIES/TASK_MANAGERS/Workflows/*.json` or workflow references

**Note**: Workflows use WRF-### ID format (not PROC-###)

```
WORKFLOWS GAP ANALYSIS:

Check for existing workflow files:
- TASK_MANAGERS/Workflows/*.json
- Video processing workflow references

For each workflow extracted:
  ✅ Similar workflow exists → Enhance with new details
  ❌ New workflow → Create new workflow entry with WRF-### ID

WORKFLOWS TO ADD:

1. Automated Documentary Creation Workflow (WRF-###)
   - Check if exists in workflow library
   - If missing: ADD complete workflow structure
   - Link to Tools: GLIF (TOL-###), Perplexity (TOL-###), VAYU (TOL-###), Seedream (TOL-###), Eleven Labs (TOL-###)
   - Link to Objects: videos [miniature documentary] (OBJ-###)
   - Link to Actions: research (ACT-###), generate (ACT-###), create (ACT-###), combine (ACT-###), publish (ACT-###)
   - Link to Skills: SKL-### (if applicable)
   - Department: VID;AID

2. YouTube Thumbnail Optimization Workflow (WRF-###)
   - Check if exists in workflow library
   - If missing: ADD workflow
   - Link to Tools: GLIF (TOL-###), Nano Banana (TOL-###)
   - Link to Objects: thumbnails [YouTube thumbnail] (OBJ-###)
   - Link to Actions: define (ACT-###), generate (ACT-###), refine (ACT-###), select (ACT-###), export (ACT-###)
   - Link to Skills: SKL-### (if applicable)
   - Department: VID;DGN

[Continue for all workflows...]

CROSS-REFERENCE:
Each workflow must specify:
  - Workflow ID: WRF-### format
  - Tools used (by TOL-### IDs)
  - Objects created (by OBJ-### IDs)
  - Actions performed (by ACT-### IDs)
  - Professions involved (by PRF-### IDs)
  - Skills required (by SKL-### IDs)
  - Department codes (ISO format)
```

#### 2.5 Professions Gap Analysis

**Check**: `ENTITIES/LIBRARIES/Professions/*.json`

```
PROFESSIONS GAP ANALYSIS:

Check for existing profession files:
- Content_Creator.json
- Video_Producer.json
- Graphic_Designer.json
- Social_Media_Manager.json

For each profession mentioned:
  ✅ EXISTS → Update with new responsibilities, tools, objects
  ❌ MISSING → Create new profession file

PROFESSIONS TO UPDATE/CREATE:

Content_Creator.json:
  UPDATE responsibilities:
    - ADD: "creating thumbnails for high CTR"
    - ADD: "automating content workflows with AI agents"
    - ADD: "producing miniature documentaries"

  UPDATE tools_used:
    - ADD: GLIF (TOL-###) - workflow automation
    - ADD: Nano Banana (TOL-###) - thumbnails
    - ADD: VAYU (TOL-###), Seedream (TOL-###) - video generation

  UPDATE objects_worked_with:
    - ADD: thumbnails (OBJ-###) [YouTube thumbnail, High-CTR thumbnail]
    - ADD: videos (OBJ-###) [miniature documentary, social video]

  UPDATE workflows:
    - ADD: Automated Documentary Creation (WRF-###)
    - ADD: YouTube Thumbnail Optimization (WRF-###)

  UPDATE skills:
    - ADD: SKL-### (thumbnail design skills)
    - ADD: SKL-### (workflow automation skills)

YouTuber.json (if doesn't exist, CREATE):
  - Responsibilities: thumbnail creation, CTR optimization, audience building
  - Tools: GLIF, Nano Banana, video editing tools
  - Objects: thumbnails, videos, social content
  - Skills: thumbnail design, CTR optimization, content strategy

[Continue for all professions...]
```

#### 2.6 Skills Gap Analysis

**Check**: `ENTITIES/LIBRARIES/Skills/Master/all_skills.json` or `ENTITIES/LIBRARIES/Skills/By_Department/*.json`

**Note**: Skills are part of LIBRARIES ecosystem, use SKL-### ID format

```
SKILLS GAP ANALYSIS:

For each skill identified:
  ✅ EXISTS → Add new contexts, applications, tools
  ❌ MISSING → Create new skill entry

SKILLS TO ADD/UPDATE:

"Prompt Engineering" (SKL-###):
  - ADD application: "refining AI video generation prompts"
  - ADD application: "optimizing thumbnail generation prompts"
  - ADD tools: GLIF (TOL-###), Nano Banana (TOL-###), VAYU (TOL-###), Sora (TOL-###)
  - ADD related_workflows: All automated AI workflows (WRF-###)
  - ADD related_objects: videos (OBJ-###), thumbnails (OBJ-###)

"Thumbnail Design" (SKL-###):
  - CREATE if missing
  - Skill ID: SKL-### (assign next sequential)
  - Skill phrase: "designed thumbnails using [Tool]"
  - Definition: Creating visually engaging thumbnail images optimized for CTR
  - Applications: YouTube thumbnails, social media thumbnails
  - Tools: Nano Banana (TOL-###), Midjourney (TOL-###), Photoshop (TOL-###)
  - Related actions: create (ACT-###), design (ACT-###), optimize (ACT-###), generate (ACT-###)
  - Related objects: thumbnails (OBJ-###)
  - Professions: Content Creator (PRF-###), YouTuber (PRF-###), Graphic Designer (PRF-###)
  - Department: VID;DGN

"Workflow Automation" (SKL-###):
  - CREATE if missing
  - Skill ID: SKL-### (assign next sequential)
  - Skill phrase: "automated workflows using [Tool]"
  - Definition: Setting up and managing agent-based AI pipelines
  - Tools: GLIF (TOL-###), n8n (TOL-###), Make (TOL-###), Zapier (TOL-###)
  - Applications: Content creation automation, documentary production
  - Related objects: videos (OBJ-###), scripts (OBJ-###)
  - Related workflows: Automated Documentary Creation (WRF-###)
  - Professions: Content Creator (PRF-###), AI Engineer (PRF-###), Video Producer (PRF-###)
  - Department: AID;VID

[Continue for all skills...]
```

---

## Phase 3: Creation and Updates (60-90 minutes)

### Step 3: Create New Library Entries

For EACH missing element, create proper JSON file:

#### 3.1 Creating Tool Files

**Template**: Use standard tool JSON structure

**Example: GLIF.json**
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOL-###",
  "name": "GLIF",
  "vendor": "GLIF (glif.app)",
  "category": "AI/Workflow Automation",
  "purpose": "AI workflow automation platform for orchestrating multiple AI tools",
  "description": "[Extract from video context]",
  "skill_level_required": "Beginner to Intermediate",
  "cost_structure": "[From video if mentioned]",
  "platform_compatibility": ["Web", "API"],
  "integration_capabilities": [
    "[List all tool integrations mentioned]"
  ],
  "documentation_url": "[From video]",
  "actual_remote_helpers_usage": {
    "primary_use": "[From video context]",
    "users": ["[User types mentioned]"],
    "use_cases": ["[Verb phrases from video]"],
    "typical_workflows": [
      {
        "task": "[Workflow name from video]",
        "steps": ["[Extracted steps]"],
        "complexity": "[From video]",
        "time_estimate": "[From video]"
      }
    ],
    "integration_with_other_tools": ["[Tools mentioned together]"]
  },
  "strengths": ["[From video]"],
  "limitations": ["[From video or inferred]"],
  "tags": ["[Relevant tags]"]
}
```

**Repeat for ALL missing tools**

#### 3.2 Creating/Updating Object Entries

**For Design_Deliverables.json:**

If "Thumbnails" object is MISSING, ADD:
```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "category": "Design Deliverables",
  "object_types": [
    "YouTube thumbnail",
    "Social media thumbnail",
    "High-CTR thumbnail",
    "Mr. Beast style thumbnail",
    "Educational thumbnail"
  ],
  "professions": ["Content Creator", "Graphic Designer", "YouTuber", "Social Media Manager"],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###"],
  "typical_dimensions": "1920x1080px (YouTube), 1200x628px (Facebook), 1080x1080px (Instagram)",
  "tools": [
    "Nano Banana (via GLIF)",
    "Midjourney",
    "Photoshop",
    "Canva"
  ],
  "tool_ids": ["TOL-###", "TOL-###", "TOL-###", "TOL-###"],
  "skills": ["SKL-###"],
  "department": "VID;DGN",
  "parameters": ["style", "contrast", "text_area", "focal_point", "color_scheme", "CTA"],
  "complexity": "Low to Medium",
  "time_estimate": "15-30 minutes (AI-assisted), 1-2 hours (manual)",
  "common_actions": ["Create", "Generate", "Optimize", "Design", "Export", "Test"],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables/",
  "platforms_used": ["YouTube", "TikTok", "Instagram", "Facebook", "LinkedIn"],
  "ai_tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "Nano Banana",
      "usage": "primary for YouTube"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Midjourney",
      "usage": "concept exploration"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "usage": "workflow automation"
    }
  ],
  "optimization_metrics": ["CTR (click-through rate)", "Engagement", "View retention"],
  "best_practices": [
    "High contrast for visibility",
    "Bold text area for messaging",
    "Clear focal point",
    "Mr. Beast style for viral appeal",
    "A/B testing multiple variants"
  ],
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "YouTube Thumbnail Creation (High CTR)"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Social Media Thumbnail Optimization"
    }
  ],
  "related_professions": ["Content Creator", "YouTuber", "Graphic Designer"]
}
```

**For Videos object (create Video_Deliverables.json if needed):**
```json
{
  "object_id": "OBJ-###",
  "object_name": "videos",
  "category": "Media",
  "object_types": [
    "Miniature documentary",
    "TikTok video",
    "Social media video",
    "AI video",
    "Educational video",
    "Product showcase video",
    "Documentary (32-second)",
    "Faceless content video"
  ],
  "professions": ["Video Producer", "Content Creator", "Documentary Producer", "Social Media Manager"],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###"],
  "tools": [
    "VAYU 2.2 (miniature documentaries)",
    "Seedream (tilt-shift effects)",
    "Sora (general video generation)",
    "Kling (fast social media videos)",
    "Cdans (animation)",
    "Premiere Pro (editing)",
    "CapCut (social editing)"
  ],
  "tool_ids": ["TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###"],
  "skills": ["SKL-###"],
  "department": "VID;AID",
  "duration_ranges": {
    "miniature_documentary": "30-60 seconds (optimal: 32 seconds)",
    "tiktok_video": "15-60 seconds",
    "social_media_video": "15-90 seconds",
    "marketing_video": "30-120 seconds"
  },
  "complexity": "Medium to High",
  "time_estimate": {
    "automated_workflow": "10-30 minutes",
    "manual_production": "2-8 hours"
  },
  "common_actions": ["Create", "Generate", "Produce", "Edit", "Optimize", "Publish"],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables/",
  "platforms_used": ["TikTok", "Instagram", "YouTube", "Facebook", "LinkedIn"],
  "ai_tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "usage": "orchestration"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "VAYU 2.2",
      "usage": "miniature style"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Seedream",
      "usage": "tilt-shift"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Sora",
      "usage": "OpenAI video"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Kling",
      "usage": "fast generation"
    }
  ],
  "output_formats": ["MP4", "MOV", "Various resolutions"],
  "visual_styles": {
    "miniature_documentary": "Tilt-shift, miniature world appearance",
    "social_video": "High-energy, fast-paced",
    "marketing_video": "Professional, brand-aligned"
  },
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "scripts",
      "relationship": "input"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "voiceovers",
      "relationship": "component"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "images",
      "relationship": "reference"
    }
  ],
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Automated Miniature Documentary Creation"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Social Media Video Production"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "TikTok Content Automation"
    }
  ]
}
```

**Repeat for ALL missing objects**

#### 3.3 Updating Action Files

For EACH action category file, ADD new contexts:

**Actions_Master.json** example update:
```json
{
  "action_id": "ACT-###",
  "action": "Generate",
  "category": "Creation",
  "description": "Produce content automatically using AI or automation",
  "contexts": [
    "generate images",
    "generate videos",
    "generate thumbnails",
    "generate scripts",
    "generate documentaries",
    "generate voiceovers",
    "generate social content"
  ],
  "tools_commonly_used": [
    "GLIF",
    "Nano Banana",
    "VAYU",
    "Sora",
    "Kling",
    "Midjourney",
    "ChatGPT"
  ],
  "tool_ids": ["TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###", "TOL-###"],
  "objects_acted_upon": [
    {
      "object_id": "OBJ-###",
      "object_name": "images"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "videos"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "scripts"
    }
  ],
  "professions_using": [
    "Content Creator",
    "Video Producer",
    "YouTuber",
    "Graphic Designer"
  ],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###"]
}
```

#### 3.4 Creating/Updating Workflow Entries

**Create new workflow entry:**

**File**: `ENTITIES/TASK_MANAGERS/Workflows/*.json` or workflow library

**Note**: Workflows use WRF-### ID format (not PROC-###)

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WRF-###",
  "workflow_name": "Automated Miniature Documentary Creation",
  "category": "Content Creation",
  "description": "End-to-end automated workflow for creating 32-second miniature-style historical documentaries using GLIF orchestration",
  "objective": "Generate engaging, fact-checked historical documentary with research, tilt-shift visuals, and professional narration",
  "workflow_type": "Automated AI Pipeline",
  "duration": "10-20 minutes (mostly automated)",
  "complexity": "Low (for user), High (for setup)",
  "steps": [
    {
      "step_number": 1,
      "action": "Research",
      "description": "Research historical facts and events using Perplexity AI",
      "tool_id": "TOL-###",
      "tool_name": "Perplexity",
      "input": "Historical topic or event name",
      "output": "Verified historical facts and context",
      "duration": "2-3 minutes (automated)"
    },
    {
      "step_number": 2,
      "action": "Generate",
      "description": "Generate documentary script from researched facts",
      "tool_id": "TOL-###",
      "tool_name": "ChatGPT",
      "input": "Historical facts from Perplexity",
      "output": "32-second documentary script",
      "duration": "1-2 minutes (automated)"
    },
    {
      "step_number": 3,
      "action": "Create",
      "description": "Create tilt-shift miniature video using VAYU 2.2 and Seedream",
      "tool_id": ["TOL-###", "TOL-###"],
      "tool_name": ["VAYU", "Seedream"],
      "input": "Documentary script and visual descriptions",
      "output": "32-second tilt-shift video (no audio)",
      "duration": "3-5 minutes (automated)"
    },
    {
      "step_number": 4,
      "action": "Generate",
      "description": "Generate professional voiceover narration",
      "tool_id": "TOL-###",
      "tool_name": "Eleven Labs",
      "input": "Documentary script",
      "output": "Professional narration audio",
      "duration": "1-2 minutes (automated)"
    },
    {
      "step_number": 5,
      "action": "Combine",
      "description": "Automatically combine video and audio via GLIF",
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "input": "Video (VAYU+Seedream) + Audio (Eleven Labs)",
      "output": "Final 32-second documentary with narration",
      "duration": "1-2 minutes (automated)"
    },
    {
      "step_number": 6,
      "action": "Review",
      "description": "Review final documentary and publish",
      "input": "Complete documentary video",
      "output": "Published content on social platforms",
      "duration": "2-5 minutes (manual)"
    }
  ],
  "tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "role": "Workflow orchestration and automation"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Perplexity",
      "role": "Historical research and fact-checking"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "VAYU",
      "role": "Miniature video generation"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Seedream",
      "role": "Tilt-shift effects enhancement"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Eleven Labs",
      "role": "Voiceover narration generation"
    }
  ],
  "objects_created": [
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "object_type": "miniature documentary",
      "format": "MP4",
      "duration": "32 seconds",
      "resolution": "1920x1080 (typical)"
    }
  ],
  "objects_used": [
    {
      "object_id": "OBJ-###",
      "object_name": "scripts",
      "object_type": "documentary script",
      "role": "Content foundation"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "images",
      "object_type": "reference image",
      "role": "Visual guidance"
    }
  ],
  "actions_performed": ["Research", "Generate", "Create", "Combine", "Review", "Publish"],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "professions_involved": [
    "Content Creator",
    "Documentary Producer",
    "Video Producer"
  ],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###"],
  "skills_required": [
    {
      "skill_id": "SKL-###",
      "skill_phrase": "automated workflows using GLIF"
    },
    {
      "skill_id": "SKL-###",
      "skill_phrase": "refined AI video generation prompts"
    },
    {
      "skill_id": "SKL-###",
      "skill_phrase": "developed content strategy"
    }
  ],
  "department": "VID;AID",
  "input_requirements": "Historical topic or event name",
  "output_deliverables": "32-second miniature documentary video (MP4) with narration",
  "automation_level": "Fully automated (via GLIF agent)",
  "business_value": [
    "10x faster than manual documentary production",
    "Consistent quality output",
    "Scalable content creation",
    "Unique visual style for engagement",
    "Fact-checked content for credibility"
  ],
  "use_cases": [
    "Educational social media content (TikTok, Instagram Reels, YouTube Shorts)",
    "Historical storytelling for brand content",
    "Engaging documentaries for online academies",
    "Visual history content for educational platforms"
  ],
  "platforms_served": [
    "TikTok",
    "Instagram Reels",
    "YouTube Shorts",
    "LinkedIn",
    "OAY (Online Academy)"
  ],
  "optimization_tips": [
    "Choose visually interesting historical topics",
    "Fact-check Perplexity output before finalizing",
    "Test different VAYU + Seedream combinations",
    "A/B test voiceover styles for audience preference",
    "Optimize video length (32 seconds is sweet spot)"
  ],
  "related_workflows": [
    "YouTube Thumbnail Creation",
    "Social Media Content Automation",
    "Educational Video Production"
  ],
  "tags": ["automated", "documentary", "miniature-video", "tilt-shift", "ai-workflow", "content-creation"]
}
```

**Repeat for ALL identified workflows**

#### 3.5 Creating/Updating Profession Files

**Update Content_Creator.json:**
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_id": "PRF-###",
  "name": "Content Creator",
  "department": "VID;AID",
  "description": "Creates engaging digital content including videos, thumbnails, and social media posts",

  "responsibilities": [
    "creating engaging thumbnails optimized for CTR",  // NEW
    "producing miniature documentaries",               // NEW
    "automating content workflows with AI agents",     // NEW
    "editing videos",
    "optimizing content for social media platforms",   // ENHANCED
    "managing content calendar",
    "building audience through consistent publishing",  // NEW
    "A/B testing content formats and styles"           // NEW
  ],

  "objects_worked_with": [
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "object_types": ["YouTube thumbnail", "High-CTR thumbnail", "Social thumbnail"],
      "actions": ["Create", "Generate", "Optimize", "Design"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"]
    },
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "object_types": ["miniature documentary", "social video", "TikTok video"],
      "actions": ["Create", "Produce", "Generate", "Edit", "Publish"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"]
    },
    {
      "object_id": "OBJ-###",
      "object_name": "scripts",
      "object_types": ["documentary script", "video script"],
      "actions": ["Generate", "Create", "Refine"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###"]
    }
  ],

  "tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "purpose": "Workflow automation and AI orchestration",  // NEW
      "frequency": "Daily"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Nano Banana",
      "purpose": "YouTube thumbnail generation",  // NEW
      "frequency": "Weekly"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "VAYU",
      "purpose": "Miniature documentary video creation",  // NEW
      "frequency": "Weekly"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "Eleven Labs",
      "purpose": "Voiceover generation",  // ENHANCED
      "frequency": "Weekly"
    }
  ],

  "workflows_performed": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Automated Miniature Documentary Creation"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "YouTube Thumbnail Creation (High CTR)"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Social Media Content Automation"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Video Editing and Publishing"
    }
  ],

  "skills_required": [
    {
      "skill_id": "SKL-###",
      "skill_name": "Prompt Engineering",
      "skill_phrase": "refined AI video generation prompts",
      "proficiency": "Intermediate",
      "applications": ["AI tool optimization", "thumbnail generation", "video creation"]
    },
    {
      "skill_id": "SKL-###",
      "skill_name": "Thumbnail Design",
      "skill_phrase": "designed thumbnails using Nano Banana",
      "proficiency": "Intermediate",
      "applications": ["CTR optimization", "visual engagement", "brand consistency"]
    },
    {
      "skill_id": "SKL-###",
      "skill_name": "Workflow Automation",
      "skill_phrase": "automated workflows using GLIF",
      "proficiency": "Beginner to Intermediate",
      "applications": ["GLIF agent setup", "automated pipelines", "efficiency optimization"]
    },
    {
      "skill_id": "SKL-###",
      "skill_name": "Content Strategy",
      "skill_phrase": "developed content strategy",
      "proficiency": "Intermediate",
      "applications": ["audience building", "platform optimization", "content planning"]
    }
  ],

  "typical_day": [
    "Review content calendar and upcoming topics",
    "Set up automated documentary creation via GLIF",  // NEW
    "Generate thumbnail variants for A/B testing",     // NEW
    "Review and publish automated content",            // NEW
    "Optimize existing content based on performance metrics",
    "Plan next week's content strategy"
  ]
}
```

**Create YouTuber.json if missing:**
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_id": "PRF-###",
  "name": "YouTuber",
  "department": "VID",
  "description": "Creates and publishes video content on YouTube, focused on building audience and optimizing for platform metrics",

  "responsibilities": [
    "creating high-CTR YouTube thumbnails",
    "optimizing video content for YouTube algorithm",
    "building and engaging audience",
    "analyzing performance metrics (CTR, watch time)",
    "A/B testing thumbnails and titles",
    "managing content upload schedule",
    "creating engaging video concepts",
    "responding to audience comments and feedback"
  ],

  "objects_worked_with": [
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "object_types": ["YouTube thumbnail", "High-CTR thumbnail", "Mr. Beast style thumbnail"],
      "actions": ["Create", "Generate", "Optimize", "Test"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"]
    },
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "object_types": ["YouTube video", "YouTube Shorts", "documentary"],
      "actions": ["Create", "Edit", "Upload", "Optimize"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"]
    }
  ],

  "tools_used": [
    {
      "tool_id": "TOL-###",
      "tool_name": "Nano Banana",
      "purpose": "YouTube thumbnail generation optimized for CTR"
    },
    {
      "tool_id": "TOL-###",
      "tool_name": "GLIF",
      "purpose": "Automating thumbnail and content creation workflows"
    },
    {
      "tool_name": "YouTube Studio",
      "purpose": "Video management and analytics"
    }
  ],

  "workflows_performed": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "YouTube Thumbnail Creation (High CTR)"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Video Upload and Optimization"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Audience Engagement Management"
    }
  ],

  "skills_required": [
    {
      "skill_id": "SKL-###",
      "skill_name": "Thumbnail Design",
      "skill_phrase": "designed thumbnails using Nano Banana",
      "proficiency": "Intermediate to Advanced",
      "applications": ["CTR optimization", "A/B testing", "viral appeal"]
    },
    {
      "skill_id": "SKL-###",
      "skill_name": "Content Strategy",
      "skill_phrase": "developed content strategy",
      "proficiency": "Advanced",
      "applications": ["audience building", "algorithm optimization", "retention"]
    },
    {
      "skill_id": "SKL-###",
      "skill_name": "Prompt Engineering",
      "skill_phrase": "refined AI thumbnail generation prompts",
      "proficiency": "Intermediate",
      "applications": ["AI thumbnail generation", "content ideation"]
    }
  ],

  "success_metrics": [
    "Click-through rate (CTR)",
    "Average view duration",
    "Subscriber growth",
    "Engagement rate (likes, comments)",
    "Video retention"
  ]
}
```

---

## Phase 4: Cross-Referencing (30-45 minutes)

### Step 4: Link All Entities

Ensure EVERY entity references related entities:

#### 4.1 Tool → Object Cross-Reference

For EACH tool file, ensure it lists objects it creates:

**Example: GLIF.json should reference:**
```json
{
  "objects_created_via_workflows": [
    "thumbnails [YouTube thumbnail, High-CTR thumbnail]",
    "videos [miniature documentary, social video]",
    "scripts [documentary script]",
    "voiceovers [documentary narration]"
  ]
}
```

#### 4.2 Object → Tool Cross-Reference

For EACH object in Responsibilities/Responsibilities/Objects library, ensure it lists tools:

**Example: Thumbnails object should reference:**
```json
{
  "tools": [
    "Nano Banana (via GLIF) - TOOL-AI-046",
    "Midjourney - TOOL-AI-006",
    "Photoshop",
    "GLIF - TOOL-AI-045"
  ],
  "ai_tools_used": [
    "Nano Banana (primary for YouTube)",
    "Midjourney (concept exploration)",
    "GLIF (workflow automation)"
  ]
}
```

#### 4.3 Workflow → All Entities Cross-Reference

For EACH workflow, ensure it references:
- Tools (by tool_id)
- Objects (by object_name and type)
- Actions (by action name)
- Professions (by profession name)
- Skills (by skill name)

#### 4.4 Profession → All Entities Cross-Reference

For EACH profession, ensure it references:
- Objects worked with
- Tools used (with tool_id)
- Workflows performed
- Skills required
- Actions commonly performed

---

## Phase 5: Reporting (20-30 minutes)

### Step 5: Generate Comprehensive Analysis Report

Create `Video_XXX_Library_Mapping_Report.md`

**Report Structure:**

```markdown
# Video [XXX] Library Mapping Report
## Taxonomy Analysis and Integration

**Video Title**: [Title]
**Analysis Date**: [Date]
**Analyst**: [Name/AI]
**Video Duration**: [Duration]
**Transcription File**: Video_XXX.md

---

## Executive Summary

[Brief overview of video content and taxonomy impact]

**Key Metrics**:
- Tools Analyzed: [Count]
- Objects Identified: [Count]
- Workflows Extracted: [Count]
- Actions Cataloged: [Count]
- Professions Updated: [Count]
- Coverage Improvement: [Before%] → [After%]

---

## 1. Tools Analysis

### 1.1 Tools Identified
Total tools mentioned: [Count]

[List all tools with frequency]

### 1.2 Tools Gap Analysis

**Existing Tools (Enhanced)**:
1. [Tool Name] - [Enhancements made]
2. [Continue...]

**New Tools Created**:
1. [Tool Name] - TOOL-AI-XXX - [Category] - [Priority]
2. [Continue...]

**Coverage Metrics**:
- Before Analysis: [X]% ([existing]/[total])
- After Analysis: [Y]% ([existing+new]/[total])
- Improvement: +[Y-X]%

### 1.3 Tool Integration Patterns

[Document how tools connect and work together]

---

## 2. Objects Analysis

### 2.1 Objects Identified
Total objects mentioned: [Count]

[List with object types]

### 2.2 Objects Gap Analysis

**Existing Objects (Enhanced)**:
- [Object name] → Added [N] new object_types
- [Continue...]

**New Objects Created**:
- [Object name] → [N] object_types → [File location]
- [Continue...]

### 2.3 Object Cross-References Created

For each object, documented:
- Tools that create it
- Actions performed on it
- Professions that use it
- Workflows that produce it

---

## 3. Actions Analysis

### 3.1 Action Verbs Cataloged
Total unique verbs: [Count]
Total verb instances: [Count]

**By Category**:
- Creation: [Count] verbs, [instances] total
- Modification: [Count] verbs, [instances] total
- Analysis: [Count] verbs, [instances] total
- Organization: [Count] verbs, [instances] total
- Communication: [Count] verbs, [instances] total

### 3.2 Actions Updated

[List action files updated with new contexts]

---

## 4. Workflows/Processes Analysis

### 4.1 Workflows Extracted
Total workflows: [Count]

[List each workflow with summary]

### 4.2 Workflows Created/Updated

**New Workflows**:
1. [Workflow Name] - PROC-XXX-XXX
   - Duration: [time]
   - Tools: [count]
   - Automation: [level]
   - Business Value: [summary]

**Workflow Integration Map**:
[Show how workflows relate to each other]

---

## 5. Professions Analysis

### 5.1 Professions Identified
Total professions mentioned: [Count]

[List professions with context]

### 5.2 Professions Updated

**Updated Professions**:
1. [Profession Name]
   - Added [N] responsibilities
   - Added [N] tools
   - Added [N] objects
   - Added [N] workflows

**New Professions Created**:
1. [Profession Name] - PROF-XXX-XXX
   - [Summary]

---

## 6. Skills Analysis

### 6.1 Skills Identified
Total skills mentioned: [Count]

[List skills with applications]

### 6.2 Skills Created/Updated

[Document skill additions/updates]

---

## 7. Cross-Reference Summary

### 7.1 Bidirectional Links Created

**Tools ↔ Objects**:
- [Count] tool-object relationships established

**Workflows ↔ Tools**:
- [Count] workflow-tool relationships established

**Professions ↔ All Entities**:
- [Count] profession relationships established

### 7.2 Cross-Reference Validation

✅ All tools reference objects they create
✅ All objects reference tools that create them
✅ All workflows reference complete entity chain
✅ All professions reference relevant entities

---

## 8. Business Value and Impact

### 8.1 Workflow Automation Potential

[Identify workflows that can be automated based on video insights]

### 8.2 Efficiency Gains

[Document time/cost savings from identified workflows]

### 8.3 Strategic Insights

[Business concepts, strategies, value propositions from video]

---

## 9. Recommendations

### 9.1 Immediate Actions
1. [Recommendation]
2. [Recommendation]

### 9.2 Future Enhancements
1. [Enhancement suggestion]
2. [Enhancement suggestion]

### 9.3 Additional Research Needed
1. [Topic to research]
2. [Topic to research]

---

## 10. Files Created/Modified

### Created Files:
1. [File path] - [Purpose]
2. [Continue...]

### Modified Files:
1. [File path] - [Changes summary]
2. [Continue...]

---

## Appendices

### Appendix A: Complete Tools List
[Full tool inventory with details]

### Appendix B: Complete Objects List
[Full object inventory with types]

### Appendix C: Complete Workflows
[Full workflow documentation]

### Appendix D: Timestamp Reference
[Key concepts with timestamps from video]

---

**Report Generated**: [Date and time]
**Status**: Complete
**Next Steps**: [Summary of what to do next]
```

---

## Quality Assurance Checklist

Before finalizing, verify:

### Completeness
- [ ] All tools from video are cataloged (100% coverage)
- [ ] All objects/deliverables are identified
- [ ] All workflows are extracted and documented
- [ ] All action verbs are categorized
- [ ] All professions are identified
- [ ] All skills are documented

### Accuracy
- [ ] Tool names spelled consistently
- [ ] URLs verified
- [ ] Timestamps accurate
- [ ] Workflow steps in logical order
- [ ] Action verb categories correct
- [ ] Object types properly classified

### Cross-References
- [ ] Tools reference objects they create
- [ ] Objects reference tools that create them
- [ ] Workflows reference all entities (tools, objects, actions, professions)
- [ ] Professions reference all relevant entities
- [ ] All references use proper IDs where applicable

### JSON Validity
- [ ] All JSON files are valid (no syntax errors)
- [ ] All required fields populated
- [ ] Consistent formatting across files
- [ ] Proper use of arrays and objects

### Documentation
- [ ] README files updated if needed
- [ ] Analysis report is comprehensive
- [ ] Examples are clear and accurate
- [ ] Recommendations are actionable

---

## Automation Opportunities

This workflow can be partially automated:

1. **Automated Inventory**: Script to extract tools, objects, actions from transcription
2. **Gap Detection**: Script to compare extracted items against existing taxonomy
3. **Template Generation**: Auto-generate JSON templates with extracted data
4. **Cross-Reference Validation**: Script to verify bidirectional links
5. **Report Generation**: Auto-generate mapping report from structured data

---

## Related Documentation

- [Video Transcription Custom Instructions](../Prompts/Video_Transcription_Custom_Instructions.md)
- [Video Analysis Prompt](./Video_Analysis_Prompt.md)
- [Transcribations README](./README.md)
- [Objects Library README](../Objects/README.md)
- [Tools Library README](../Tools/README.md)

---

**Maintained By**: Taxonomy Team
**Version**: 1.0
**Last Updated**: 2025-11-12
**Status**: Active - Production Ready
