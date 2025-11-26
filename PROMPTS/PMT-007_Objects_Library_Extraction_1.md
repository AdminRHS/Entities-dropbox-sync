# Objects Library Extraction and Cross-Referencing Prompt
## Extracting Deliverables, Outputs, and Tangible Items from Video Transcriptions

**Purpose**: Systematic methodology for identifying, extracting, and cross-referencing Objects (deliverables, outputs, tangible items) from video transcriptions and integrating them into the LIBRARIES/Objects taxonomy.

**Version**: 2.1 - Tool ID Format Standardization & Terminology Update
**Date**: 2025-11-19
**Status**: Active - Production Ready
**Last Updated**: 2025-11-19

### Version History
- **v2.1** (2025-11-19): Tool ID format standardization (TOL-### → TOOL-{CATEGORY}-###), "Gap Analysis" → "Library Enrichment" terminology update
- **v2.0** (2025-11-25): Taxonomy Architecture Alignment

---

## Table of Contents

1. [Overview](#overview)
2. [Understanding Objects in Taxonomy](#understanding-objects-in-taxonomy)
3. [Object Identification Process](#object-identification-process)
4. [Object Type Extraction](#object-type-extraction)
5. [Cross-Referencing Methodology](#cross-referencing-methodology)
6. [Creating Object Entries](#creating-object-entries)
7. [Real Examples from Video_001](#real-examples-from-video_001)
8. [Quality Assurance](#quality-assurance)

---

## Overview

### What Are Objects?

In the taxonomy system, **Objects** are:
- **Plural, concrete nouns** representing tangible or slightly abstract entities
- **Deliverables** that professions create or work with
- **Outputs** from workflows and processes
- **Inputs** to other processes
- The **noun portion** of Task Templates (Action + Object = Task)

### Why Extract Objects from Videos?

Video transcriptions are rich sources of:
- **Design deliverables** mentioned (thumbnails, videos, mockups)
- **Documents** created (scripts, reports, proposals)
- **Media items** produced (images, audio, animations)
- **Data objects** managed (leads, contacts, projects)
- **Communication objects** (emails, messages, presentations)

Extracting and cataloging these objects:
1. Completes the taxonomy for "Action + Object = Task" structure
2. Enables cross-referencing between Tools → Objects → Workflows
3. Documents what deliverables can be produced with which tools
4. Maps profession-object relationships
5. Identifies object types and variations

---

## Understanding Objects in Taxonomy

### Object Structure

Each object has:

```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "object_types": ["YouTube thumbnail", "Social thumbnail", "High-CTR thumbnail"],
  "category": "Design Deliverables",
  "professions": ["Content Creator", "Graphic Designer"],
  "profession_ids": ["PRF-###"],
  "tools": ["Nano Banana", "Midjourney", "Photoshop"],
  "tool_ids": ["TOOL-AI-###", "TOOL-AI-###", "TOOL-DESIGN-###"],
  "skills": ["SKL-###"],
  "complexity": "Low to Medium",
  "time_estimate": "15-30 minutes",
  "common_actions": ["Create", "Generate", "Optimize", "Design"],
  "action_ids": ["ACT-###", "ACT-###"],
  "department": "VID;DGN",
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables/",
  "platforms_used": ["YouTube", "Social Media"]
}
```

### Object Categories

Objects are organized into categories:

1. **Design Deliverables**: Visual and interactive deliverables
   - Examples: Banners, Logos, Icons, Illustrations, Mockups, Wireframes, Prototypes

2. **Documents**: Text-based deliverables
   - Examples: Reports, Proposals, Contracts, Scripts, Job Postings

3. **Media**: Audio-visual content
   - Examples: Videos, Images, Audio, Animations, Presentations

4. **Data**: Structured information
   - Examples: Leads, Contacts, Projects, Tasks, Candidates

5. **Communication**: Interactive exchanges
   - Examples: Emails, Messages, Calls, Meetings, Notifications

### Object Types

Objects can have multiple **types** or **variations**:

**Example: Videos object**
- Types: "Miniature documentary", "TikTok video", "Social media video", "AI video"

**Example: Thumbnails object**
- Types: "YouTube thumbnail", "Social thumbnail", "High-CTR thumbnail", "Mr. Beast style thumbnail"

---

## Object Identification Process

### Phase 1: Read and Mark Objects (15-20 minutes)

#### Step 1: Scan Transcription for Nouns

Look for mentions of deliverables, outputs, and tangible items:

**Trigger phrases**:
- "create [noun]"
- "generate [noun]"
- "produce [noun]"
- "make [noun]"
- "design [noun]"
- "build [noun]"
- "the output is [noun]"
- "you get [noun]"
- "it produces [noun]"

#### Step 2: Identify Object Mentions

**From Video_001 example**:

> [02:34] "...for thumbnails, I use this Nano Banana agent..."
**Object identified**: thumbnails

> [06:20] "...it generates a 32-second miniature documentary..."
**Object identified**: documentaries (or videos)

> [06:25] "...Perplexity researches the topic and generates a script..."
**Object identified**: scripts

> [08:30] "...then Eleven Labs creates the voiceover..."
**Object identified**: voiceovers (or audio)

> [03:15] "...you can create YouTube thumbnails with high CTR..."
**Object identified**: thumbnails [YouTube thumbnail type]

#### Step 3: Create Initial Object Inventory

```
OBJECTS INVENTORY FROM VIDEO:

1. thumbnails
   - Mentioned: 12 times
   - Timestamps: [02:34], [03:15], [03:45], [05:20]...
   - Contexts: "YouTube thumbnails", "high-CTR thumbnails", "Mr. Beast style"
   - Types identified: YouTube thumbnail, High-CTR thumbnail, Mr. Beast style thumbnail

2. videos
   - Mentioned: 18 times
   - Timestamps: [06:20], [07:10], [08:45], [10:15]...
   - Contexts: "miniature documentaries", "32-second videos", "TikTok videos", "social content"
   - Types identified: Miniature documentary, TikTok video, Social media video

3. scripts
   - Mentioned: 6 times
   - Timestamps: [06:25], [07:30], [09:15]...
   - Contexts: "documentary scripts", "voiceover scripts", "AI-generated scripts"
   - Types identified: Documentary script, Voiceover script, Video script

4. voiceovers
   - Mentioned: 8 times
   - Timestamps: [08:30], [09:45], [11:20]...
   - Contexts: "professional narration", "documentary voiceover", "Eleven Labs voice"
   - Types identified: Documentary narration, Professional voiceover, AI-generated voice

5. images
   - Mentioned: 5 times
   - Timestamps: [04:10], [05:50]...
   - Contexts: "reference images", "generated images", "concept art"
   - Types identified: Reference image, Generated image, Concept art

[Continue for all objects...]
```

### Phase 2: Categorize Objects (10-15 minutes)

#### Step 4: Assign Objects to Categories

For each object, determine its category:

```
OBJECT CATEGORIZATION:

Design Deliverables:
  - thumbnails [YouTube thumbnail, Social thumbnail, High-CTR thumbnail]
  - mockups [if mentioned]
  - illustrations [if mentioned]

Media:
  - videos [Miniature documentary, TikTok video, Social media video]
  - images [Reference image, Concept art, Generated image]
  - voiceovers [Documentary narration, Professional voiceover]

Documents:
  - scripts [Documentary script, Voiceover script, Video script]
  - reports [if mentioned]
  - proposals [if mentioned]

Communication:
  - presentations [if mentioned]
  - messages [if mentioned]

Data:
  - projects [if mentioned]
  - leads [if mentioned]
```

#### Step 5: Check Existing Objects Library

**Check files**:
- `ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json`
- `ENTITIES/LIBRARIES/Responsibilities/Objects/Documents.json`
- `ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables.json`
- `ENTITIES/LIBRARIES/Responsibilities/Objects/object_types.json`
- `ENTITIES/LIBRARIES/Responsibilities/Objects/README.md`
- `ENTITIES/LIBRARIES/README.md` (for Objects section)

**For each identified object**:
- ✅ **EXISTS**: Note what needs enhancement (new types, tools, contexts)
- ❌ **MISSING**: Mark for creation with priority level

```
OBJECTS LIBRARY ENRICHMENT:

✅ EXISTS (Enhance):

In Design_Deliverables.json:
  - Banners ✓ (no changes needed for this video)
  - Logos ✓ (no changes needed)
  - Mockups ✓ (no changes needed)
  - Presentations ✓ (check if video-related use cases should be added)

CHECK IF EXISTS:
  - Thumbnails → VERIFY in Design_Deliverables.json
    - If exists: ADD new types (High-CTR, Mr. Beast style)
    - If exists: ADD tools (Nano Banana, GLIF)
    - If exists: UPDATE time estimates, workflows

❌ MISSING (Create):

Priority: CRITICAL
  - Videos (Media category)
    - Types: Miniature documentary, TikTok video, Social video
    - Tools: VAYU, Seedream, Sora, Kling, GLIF
    - Professions: Video Producer, Content Creator, Documentary Producer

Priority: HIGH
  - Voiceovers (Media category)
    - Types: Documentary narration, Professional voiceover, AI-generated voice
    - Tools: Eleven Labs, GLIF
    - Professions: Voice Actor, Content Creator, Video Producer

  - Scripts (Documents category)
    - Types: Documentary script, Voiceover script, Video script
    - Tools: ChatGPT, Claude, Perplexity (research input)
    - Professions: Scriptwriter, Content Creator, Documentary Producer

Priority: MEDIUM
  - If any other objects mentioned less frequently
```

---

## Object Type Extraction

### Step 6: Extract Object Types from Context

For each object, identify its **types** (variations, states, modifiers):

#### Method: Context Analysis

**Look for**:
- Adjectives describing the object: "miniature documentary", "high-CTR thumbnail"
- Purpose indicators: "for YouTube", "for TikTok", "for social media"
- Style descriptors: "Mr. Beast style", "tilt-shift", "professional"
- Format indicators: "32-second video", "1920x1080 thumbnail"

#### Example: Thumbnails Object Types

**From transcription**:
- [02:34] "...YouTube thumbnails..."
- [03:15] "...thumbnails with high CTR..."
- [03:20] "...Mr. Beast style thumbnail..."
- [05:30] "...social media thumbnails..."

**Extracted types**:
```json
"object_types": [
  "YouTube thumbnail",
  "Social media thumbnail",
  "High-CTR thumbnail",
  "Mr. Beast style thumbnail"
]
```

#### Example: Videos Object Types

**From transcription**:
- [06:20] "...32-second miniature documentary..."
- [07:40] "...TikTok videos..."
- [08:15] "...social media content..."
- [10:25] "...short-form videos..."
- [11:30] "...documentary-style videos..."

**Extracted types**:
```json
"object_types": [
  "Miniature documentary",
  "TikTok video",
  "Social media video",
  "Short-form video",
  "Documentary-style video",
  "32-second video"
]
```

### Step 7: Document Object Attributes

For each object, extract:

#### 7.1 Tools Used to Create Object

**Example: Thumbnails**
```json
"tools": [
  "Nano Banana (via GLIF)",
  "Midjourney",
  "Photoshop",
  "Canva"
],
"ai_tools_used": [
  "Nano Banana (primary for YouTube)",
  "Midjourney (concept exploration)",
  "GLIF (workflow automation)"
]
```

#### 7.2 Actions Performed on Object

**Example: Videos**
```json
"common_actions": [
  "Create",
  "Generate",
  "Produce",
  "Edit",
  "Optimize",
  "Publish",
  "Review"
]
```

#### 7.3 Professions That Work with Object

**Example: Scripts**
```json
"professions": [
  "Scriptwriter",
  "Content Creator",
  "Documentary Producer",
  "Video Producer",
  "Copywriter"
]
```

#### 7.4 Complexity and Time Estimates

**From video context**:
- [03:15] "...takes maybe 15 minutes total..." (for thumbnails)
- [06:30] "...10-20 minutes for a complete documentary..." (for videos)

```json
"complexity": "Low to Medium",
"time_estimate": "15-30 minutes (AI-assisted), 1-2 hours (manual)"
```

#### 7.5 Related Workflows

**Example: Videos (Miniature documentaries)**
```json
"related_workflows": [
  "Automated Miniature Documentary Creation",
  "Social Media Video Production",
  "TikTok Content Automation"
]
```

#### 7.6 Platforms and Use Cases

**Example: Thumbnails**
```json
"platforms_used": ["YouTube", "TikTok", "Instagram", "Facebook"],
"use_cases": [
  "YouTube video thumbnails for high CTR",
  "Social media post images",
  "AI campaign visuals",
  "Content preview images"
]
```

---

## Cross-Referencing Methodology

### Phase 3: Establish Bidirectional Links (20-30 minutes)

Cross-referencing ensures all entities in the taxonomy are interconnected.

#### Step 8: Object → Tool Links

For each object, link to tools that create it:

**In Object Entry** (Design_Deliverables.json - Thumbnails):
```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "tools": [
    "Nano Banana (via GLIF) - TOOL-AI-###",
    "Midjourney - TOOL-AI-###",
    "GLIF - TOOL-AUTO-###"
  ],
  "tool_ids": ["TOOL-AI-###", "TOOL-AI-###", "TOOL-AUTO-###"]
}
```

**In Tool Entry** (TOOL-AI-### - Nano_Banana.json):
```json
{
  "tool_id": "TOOL-AI-###",
  "name": "Nano Banana",
  "objects_created": [
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "object_types": ["YouTube thumbnail", "High-CTR thumbnail", "Social thumbnail"]
    }
  ]
}
```

#### Step 9: Object → Action Links

For each object, link to actions performed on it:

**In Object Entry**:
```json
{
  "object_name": "Videos",
  "common_actions": ["Create", "Generate", "Produce", "Edit", "Optimize", "Publish"]
}
```

**In Action Entry** (Actions_Master.json - "generate"):
```json
{
  "action_id": "ACT-###",
  "action": "Generate",
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
  ]
}
```

#### Step 10: Object → Workflow Links

For each object, link to workflows that produce it:

**In Object Entry**:
```json
{
  "object_id": "OBJ-###",
  "object_name": "videos",
  "object_types": ["Miniature documentary"],
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Automated Miniature Documentary Creation"
    }
  ]
}
```

**In Workflow Entry** (WRF-###):
```json
{
  "workflow_id": "WRF-###",
  "workflow_name": "Automated Miniature Documentary Creation",
  "objects_created": [
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "object_type": "miniature documentary",
      "format": "MP4",
      "duration": "32 seconds"
    }
  ]
}
```

#### Step 11: Object → Profession Links

For each object, link to professions that work with it:

**In Object Entry**:
```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "professions": ["Content Creator", "Graphic Designer", "YouTuber"],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###"]
}
```

**In Profession Entry** (professions.json):
```json
{
  "profession_id": "PRF-###",
  "name": "Content Creator",
  "objects_worked_with": [
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "object_types": ["YouTube thumbnail", "High-CTR thumbnail"],
      "actions": ["Create", "Generate", "Optimize", "Design"],
      "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###"]
    }
  ]
}
```

#### Step 12: Object → Object Links

Some objects relate to or depend on other objects:

**Example: Videos depend on Scripts and Voiceovers**:
```json
{
  "object_id": "OBJ-###",
  "object_name": "videos",
  "object_types": ["Miniature documentary"],
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "scripts",
      "relationship": "input",
      "description": "Documentary script provides content foundation"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "voiceovers",
      "relationship": "component",
      "description": "Voiceover narration is combined with video"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "images",
      "relationship": "reference",
      "description": "Reference images guide visual generation"
    }
  ]
}
```

#### Step 13: Object → Skills Links

Link objects to skills that involve working with them:

**In Object Entry**:
```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "skills": [
    {
      "skill_id": "SKL-###",
      "skill_phrase": "created UI mockups in Figma",
      "relationship": "design_thumbnails_via_tool"
    }
  ]
}
```

**In Skill Entry** (Skills/Master/all_skills.json):
```json
{
  "skill_id": "SKL-###",
  "skill_phrase": "designed thumbnails using Nano Banana",
  "components": {
    "action": "design",
    "object": "thumbnails",
    "tool": "Nano Banana"
  },
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails"
    }
  ]
}
```

---

## Creating Object Entries

### Step 13: Create New Object Entries

For MISSING objects, create entries in appropriate files:

#### Template: Design Deliverables Object

**File**: `ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json`

```json
{
  "object_id": "OBJ-###",
  "object_name": "thumbnails",
  "object_types": [
    "YouTube thumbnail",
    "Social media thumbnail",
    "High-CTR thumbnail",
    "Mr. Beast style thumbnail",
    "Educational thumbnail",
    "Gaming thumbnail"
  ],
  "category": "Design Deliverables",
  "professions": [
    "Content Creator",
    "Graphic Designer",
    "YouTuber",
    "Social Media Manager"
  ],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###"],
  "typical_dimensions": "1920x1080px (YouTube), 1200x628px (Facebook), 1080x1080px (Instagram)",
  "tools": [
    "Nano Banana (via GLIF)",
    "Midjourney",
    "Photoshop",
    "Canva",
    "Figma"
  ],
  "tool_ids": ["TOOL-AI-###", "TOOL-AI-###", "TOOL-DESIGN-###", "TOOL-DESIGN-###", "TOOL-DESIGN-###"],
  "skills": ["SKL-###"],
  "department": "VID;DGN",
  "parameters": [
    "style",
    "contrast",
    "text_area",
    "focal_point",
    "color_scheme",
    "CTA",
    "brand_elements"
  ],
  "complexity": "Low to Medium",
  "time_estimate": "15-30 minutes (AI-assisted), 1-2 hours (manual)",
  "common_actions": [
    "Create",
    "Generate",
    "Optimize",
    "Design",
    "Export",
    "Test",
    "Refine"
  ],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables/",
  "platforms_used": [
    "YouTube",
    "TikTok",
    "Instagram",
    "Facebook",
    "LinkedIn",
    "Twitter"
  ],
  "ai_tools_used": [
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Nano Banana",
      "usage": "primary for YouTube via GLIF"
    },
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Midjourney",
      "usage": "concept exploration"
    },
    {
      "tool_id": "TOOL-AUTO-###",
      "tool_name": "GLIF",
      "usage": "workflow automation"
    }
  ],
  "optimization_metrics": [
    "CTR (click-through rate)",
    "Engagement rate",
    "View retention",
    "A/B test performance"
  ],
  "best_practices": [
    "High contrast for visibility in feeds",
    "Bold text area for clear messaging",
    "Clear focal point (face or key element)",
    "Mr. Beast style: bold colors, expressive faces, large text",
    "A/B test multiple variants",
    "Platform-specific sizing",
    "Brand consistency"
  ],
  "related_workflows": [
    "YouTube Thumbnail Creation (High CTR)",
    "Social Media Thumbnail Optimization",
    "A/B Testing for Thumbnail Performance"
  ],
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "relationship": "preview",
      "description": "Thumbnail is preview image for video content"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "images",
      "relationship": "derived_from",
      "description": "May be derived from video screenshots or reference images"
    }
  ],
  "file_formats": ["PNG", "JPG", "WebP"],
  "deliverable_location": "Client presentation, Platform upload, AI assets"
}
```

#### Template: Media Object (Videos)

**File**: `ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables.json`

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
    "YouTube Shorts",
    "Instagram Reels",
    "Faceless content video"
  ],
  "professions": [
    "Video Producer",
    "Content Creator",
    "Documentary Producer",
    "Social Media Manager",
    "Video Editor"
  ],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###", "PRF-###"],
  "tools": [
    "VAYU 2.2 (miniature documentaries)",
    "Seedream (tilt-shift effects)",
    "Sora (general video generation)",
    "Kling (fast social media videos)",
    "Cdans (animation)",
    "GLIF (orchestration)",
    "Premiere Pro (editing)",
    "CapCut (social editing)"
  ],
  "tool_ids": ["TOOL-VIDEO-###", "TOOL-VIDEO-###", "TOOL-VIDEO-###", "TOOL-AI-###", "TOOL-AUTO-###", "TOOL-VIDEO-###", "TOOL-VIDEO-###", "TOOL-VIDEO-###"],
  "skills": ["SKL-###"],
  "department": "VID;AID",
  "duration_ranges": {
    "miniature_documentary": "30-60 seconds (optimal: 32 seconds)",
    "tiktok_video": "15-60 seconds",
    "instagram_reels": "15-90 seconds",
    "youtube_shorts": "15-60 seconds",
    "social_media_video": "15-90 seconds",
    "marketing_video": "30-120 seconds"
  },
  "complexity": "Medium to High",
  "time_estimate": {
    "automated_workflow": "10-30 minutes",
    "semi_automated": "1-3 hours",
    "manual_production": "2-8 hours",
    "professional_production": "1-5 days"
  },
  "common_actions": [
    "Create",
    "Generate",
    "Produce",
    "Edit",
    "Optimize",
    "Publish",
    "Review",
    "Export",
    "Render"
  ],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables/",
  "platforms_used": [
    "TikTok",
    "Instagram",
    "YouTube",
    "Facebook",
    "LinkedIn",
    "Twitter"
  ],
  "ai_tools_used": [
    {
      "tool_id": "TOOL-AUTO-###",
      "tool_name": "GLIF",
      "usage": "orchestration"
    },
    {
      "tool_id": "TOOL-VIDEO-###",
      "tool_name": "VAYU 2.2",
      "usage": "miniature style"
    },
    {
      "tool_id": "TOOL-VIDEO-###",
      "tool_name": "Seedream",
      "usage": "tilt-shift"
    },
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Sora",
      "usage": "OpenAI video generation"
    },
    {
      "tool_id": "TOOL-VIDEO-###",
      "tool_name": "Kling",
      "usage": "fast generation"
    },
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Eleven Labs",
      "usage": "voiceover"
    }
  ],
  "output_formats": ["MP4", "MOV", "WebM", "AVI"],
  "resolution_options": ["1920x1080 (Full HD)", "1080x1920 (Vertical)", "1080x1080 (Square)", "3840x2160 (4K)"],
  "visual_styles": {
    "miniature_documentary": "Tilt-shift, miniature world appearance, documentary narration",
    "social_video": "High-energy, fast-paced, attention-grabbing",
    "marketing_video": "Professional, brand-aligned, value-focused",
    "educational_video": "Clear, informative, step-by-step"
  },
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "scripts",
      "relationship": "input",
      "description": "Script provides content and structure for video"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "voiceovers",
      "relationship": "component",
      "description": "Voiceover narration is audio component of video"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "images",
      "relationship": "reference",
      "description": "Reference images guide visual generation"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "thumbnails",
      "relationship": "preview",
      "description": "Thumbnail serves as preview image for video"
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
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "YouTube Shorts Creation"
    }
  ],
  "optimization_metrics": [
    "View count",
    "Watch time / retention",
    "Engagement rate (likes, comments, shares)",
    "CTR from thumbnail",
    "Completion rate"
  ],
  "best_practices": [
    "Hook viewers in first 3 seconds",
    "Optimize for platform (vertical for TikTok/Reels, horizontal for YouTube)",
    "Add captions for accessibility and silent viewing",
    "Use platform-specific aspect ratios",
    "Optimize length for platform (TikTok favors 21-34 seconds)",
    "Test different styles and formats",
    "Include clear CTA"
  ]
}
```

#### Template: Document Object (Scripts)

**File**: `ENTITIES/LIBRARIES/Responsibilities/Objects/Documents.json`

```json
{
  "object_id": "OBJ-###",
  "object_name": "scripts",
  "category": "Documents",
  "object_types": [
    "Documentary script",
    "Voiceover script",
    "Video script",
    "AI script",
    "Educational script",
    "Social media script",
    "Presentation script"
  ],
  "professions": [
    "Scriptwriter",
    "Content Creator",
    "Documentary Producer",
    "Copywriter",
    "Video Producer"
  ],
  "profession_ids": ["PRF-###", "PRF-###", "PRF-###", "PRF-###", "PRF-###"],
  "tools": [
    "ChatGPT",
    "Claude",
    "Perplexity (research)",
    "Google Docs",
    "Microsoft Word",
    "Final Draft"
  ],
  "tool_ids": ["TOOL-AI-###", "TOOL-AI-###", "TOOL-AI-###", "TOOL-DATA-###", "TOOL-DATA-###", "TOOL-DATA-###"],
  "skills": ["SKL-###"],
  "department": "VID;AID",
  "typical_length": {
    "documentary_script": "100-200 words (32-second video)",
    "voiceover_script": "75-150 words per minute",
    "social_media_script": "50-100 words (30-second video)",
    "marketing_script": "150-300 words (60-90 second video)"
  },
  "complexity": "Low to Medium",
  "time_estimate": "15-30 minutes (AI-assisted), 1-3 hours (manual)",
  "common_actions": [
    "Create",
    "Generate",
    "Write",
    "Edit",
    "Refine",
    "Review",
    "Approve"
  ],
  "action_ids": ["ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###", "ACT-###"],
  "storage_pattern": "ENTITIES/LIBRARIES/Responsibilities/Objects/Documents/",
  "ai_tools_used": [
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "ChatGPT",
      "usage": "primary generation"
    },
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Perplexity",
      "usage": "fact-checking, research"
    },
    {
      "tool_id": "TOOL-AI-###",
      "tool_name": "Claude",
      "usage": "refinement"
    }
  ],
  "format": "Plain text, Markdown, DOCX, PDF",
  "related_objects": [
    {
      "object_id": "OBJ-###",
      "object_name": "videos",
      "relationship": "output",
      "description": "Script is input for video production"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "voiceovers",
      "relationship": "output",
      "description": "Script is read for voiceover narration"
    },
    {
      "object_id": "OBJ-###",
      "object_name": "presentations",
      "relationship": "output",
      "description": "Script may be basis for presentation content"
    }
  ],
  "related_workflows": [
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Automated Miniature Documentary Creation"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "Video Content Production"
    },
    {
      "workflow_id": "WRF-###",
      "workflow_name": "AI Video Creation"
    }
  ],
  "best_practices": [
    "Write for spoken delivery (conversational tone)",
    "Time script to target video length",
    "Include pauses and emphasis markers",
    "Fact-check with Perplexity",
    "Match brand voice and tone",
    "Include hook in first 10 seconds",
    "Clear CTA at end"
  ]
}
```

### Step 14: Update Existing Object Entries

If object EXISTS but needs enhancement:

**Example: Enhancing "Presentations" in Design_Deliverables.json**

**ADD**:
- New tools: Gamma AI, GLIF
- New use cases: Video content presentations, AI-generated presentations
- Updated time estimates: "30 minutes - 2 hours (Gamma AI)"
- Related workflows: Video content documentation, Client pitch decks

---

## Real Examples from Video_001

### Example 1: Complete Object Extraction - Thumbnails

**From Transcription**:
> [02:34] "So for thumbnails, I use this Nano Banana agent in GLIF."
> [03:15] "First, I define my concept—let's say I want a Mr. Beast style thumbnail with high contrast."
> [03:45] "Takes maybe 15 minutes total and the CTR is insane."
> [05:20] "These thumbnails work great for YouTube, TikTok, Instagram..."

**Extraction Process**:

**1. Object Identified**: thumbnails

**2. Object Types Extracted**:
- "YouTube thumbnail" (implied from YouTube mention)
- "Mr. Beast style thumbnail" (explicit)
- "High-CTR thumbnail" (from "CTR is insane")
- "Social media thumbnail" (from TikTok, Instagram mention)

**3. Tools Extracted**:
- Nano Banana (via GLIF) - PRIMARY
- Midjourney (mentioned earlier in video)

**4. Professions**:
- Content Creator (speaker role)
- YouTuber (context of use)
- Graphic Designer (implied)

**5. Time Estimate**: "15 minutes" (from [03:45])

**6. Platforms**: YouTube, TikTok, Instagram

**7. Optimization Metric**: CTR (click-through rate)

**8. Best Practices**: "high contrast", "Mr. Beast style"

**Created Object Entry**: See full template above in Step 13

---

### Example 2: Complete Object Extraction - Videos (Miniature Documentaries)

**From Transcription**:
> [06:20] "Here's the magic—I have a GLIF agent that does this all automatically. It takes a historical topic, researches it with Perplexity, writes a script, generates the video using VAYU and Seedream for that miniature effect, adds a voiceover with Eleven Labs, and boom—32-second documentary ready to post."
> [07:40] "These miniature documentaries work great on TikTok, Instagram Reels, YouTube Shorts..."
> [08:15] "The whole process takes 10-20 minutes, mostly automated."

**Extraction Process**:

**1. Object Identified**: videos (with specific type: miniature documentaries)

**2. Object Types Extracted**:
- "Miniature documentary" (explicit)
- "32-second video" (duration-based type)
- "TikTok video" (platform-specific)
- "Instagram Reels" (platform-specific)
- "YouTube Shorts" (platform-specific)
- "Documentary-style video" (style-based)

**3. Tools Extracted**:
- GLIF - orchestration
- Perplexity - research input
- VAYU - video generation
- Seedream - tilt-shift effects
- Eleven Labs - voiceover component

**4. Professions**:
- Documentary Producer
- Content Creator
- Video Producer

**5. Time Estimate**: "10-20 minutes (mostly automated)"

**6. Duration**: "32 seconds" (optimal length)

**7. Visual Style**: "miniature effect", "tilt-shift" (from Seedream)

**8. Platforms**: TikTok, Instagram Reels, YouTube Shorts

**9. Related Objects**:
- Input: scripts (documentary script)
- Component: voiceovers (narration)
- Output: Ready-to-publish video

**10. Workflow**: Automated Miniature Documentary Creation

**Created Object Entry**: See full template above in Step 13

---

### Example 3: Complete Object Extraction - Scripts

**From Transcription**:
> [06:25] "Perplexity researches the topic and generates a script..."
> [07:30] "The script is factually accurate because Perplexity does the research..."
> [09:15] "It creates a complete documentary script with narration..."

**Extraction Process**:

**1. Object Identified**: scripts

**2. Object Types Extracted**:
- "Documentary script" (explicit)
- "Voiceover script" (implied from narration use)
- "Video script" (general type)

**3. Tools Extracted**:
- Perplexity - research + generation
- ChatGPT / AI - script generation (implied)
- GLIF - workflow orchestration

**4. Professions**:
- Scriptwriter
- Content Creator
- Documentary Producer

**5. Time Estimate**: "2-3 minutes" (within 10-20 min automated workflow)

**6. Length**: ~100-200 words (for 32-second documentary)

**7. Quality Attribute**: "factually accurate" (Perplexity research)

**8. Related Objects**:
- Output: videos (script becomes video)
- Output: voiceovers (script is read for narration)

**9. Workflow**: Part of Automated Miniature Documentary Creation

**Created Object Entry**: See template above in Step 13

---

## Quality Assurance

### Validation Checklist

Before finalizing object entries:

#### Completeness
- [ ] All objects from video are identified
- [ ] All object types are documented
- [ ] Tools that create object are listed
- [ ] Professions that use object are listed
- [ ] Common actions are specified
- [ ] Time estimates provided (if mentioned)
- [ ] Related workflows documented

#### Accuracy
- [ ] Object names are plural, lowercase (e.g., "thumbnails", not "Thumbnail")
- [ ] Object IDs follow OBJ-### format
- [ ] Object types use exact phrases from video
- [ ] Tool references include TOOL-{CATEGORY}-### IDs
- [ ] Action references include ACT-### IDs
- [ ] Profession references include PRF-### IDs
- [ ] Skill references include SKL-### IDs
- [ ] Department codes use ISO format (AID, DEV, HRM, LGN, DGN, VID, SLS, SMM, FIN)
- [ ] Time estimates match video statements
- [ ] Platforms match video mentions
- [ ] Complexity levels are appropriate

#### Cross-References
- [ ] Object → Tools (bidirectional with TOOL-{CATEGORY}-### IDs)
- [ ] Object → Actions (bidirectional with ACT-### IDs)
- [ ] Object → Workflows (bidirectional with WRF-### IDs)
- [ ] Object → Professions (bidirectional with PRF-### IDs)
- [ ] Object → Skills (bidirectional with SKL-### IDs)
- [ ] Object → Object (related objects documented with OBJ-### IDs)

#### Structure
- [ ] JSON is valid (no syntax errors)
- [ ] All required fields populated
- [ ] Arrays properly formatted
- [ ] Consistent naming conventions
- [ ] Proper use of nested objects

---

## Summary Workflow

### Complete Object Extraction Process

1. **Read Transcription** (10 min)
   - Scan for deliverables, outputs, tangible items
   - Mark object mentions with timestamps

2. **Create Inventory** (15 min)
   - List all objects with frequency counts
   - Extract object types from context
   - Categorize objects (Design, Media, Documents, etc.)

3. **Library Enrichment** (10 min)
   - Check `ENTITIES/LIBRARIES/Responsibilities/Objects/` library for existing entries
   - Verify object IDs (OBJ-### format) in existing files
   - Mark objects as EXISTS (enhance) or MISSING (create)
   - Prioritize missing objects
   - Check for Skills (SKL-###) that involve these objects

4. **Extract Attributes** (20 min)
   - Tools used to create object
   - Actions performed on object
   - Professions that work with it
   - Time estimates, complexity levels
   - Related workflows

5. **Cross-Reference** (25 min)
   - Link Object → Tools (bidirectional with TOOL-{CATEGORY}-### IDs)
   - Link Object → Actions (bidirectional with ACT-### IDs)
   - Link Object → Workflows (bidirectional with WRF-### IDs)
   - Link Object → Professions (bidirectional with PRF-### IDs)
   - Link Object → Skills (bidirectional with SKL-### IDs)
   - Link Object → Related Objects (with OBJ-### IDs)

6. **Create/Update Entries** (30 min)
   - Create JSON entries for missing objects
   - Update existing objects with new info
   - Ensure all fields populated
   - Validate JSON syntax

7. **Validate** (10 min)
   - Run completeness checklist
   - Verify bidirectional links
   - Check JSON validity
   - Review accuracy

**Total Time**: ~120 minutes (2 hours)

---

## ID Assignment Standards

### Object IDs
- **Format**: `OBJ-###` (e.g., OBJ-001, OBJ-042, OBJ-125)
- **Sequential numbering** within entity type
- **Zero-padded** to 3 digits
- **Status**: Mark as `[Pending_Review]` until taxonomy integration

### Cross-Reference IDs
- **Tools**: `TOOL-{CATEGORY}-###` (e.g., TOOL-AI-027, TOOL-DESIGN-015, TOOL-DEV-044)
- **Actions**: `ACT-###`
- **Workflows**: `WRF-###` (not PROC-###)
- **Professions**: `PRF-###`
- **Skills**: `SKL-###`
- **Departments**: ISO codes (AID, DEV, HRM, LGN, DGN, VID, SLS, SMM, FIN)

#### Tool ID Category Examples

**Format**: `TOOL-{CATEGORY}-###`

**Common Categories:**
- **TOOL-AI-###**: AI/LLM tools (ChatGPT, Claude, Midjourney, Perplexity)
- **TOOL-AUTO-###**: Automation tools (GLIF, n8n, Make, Zapier)
- **TOOL-DESIGN-###**: Design tools (Photoshop, Figma, Canva)
- **TOOL-DEV-###**: Development tools (VS Code, Cursor, Git, Docker)
- **TOOL-VIDEO-###**: Video production tools (Premiere Pro, VAYU, Seedream)
- **TOOL-COMM-###**: Communication tools (Slack, Gmail, Zoom)
- **TOOL-DATA-###**: Data tools (Excel, Airtable, databases)
- **TOOL-FILE-###**: File management (Dropbox, Google Drive)

**From Video_001 Examples:**
- Nano Banana: `TOOL-AI-###` (AI image generation)
- GLIF: `TOOL-AUTO-###` (Workflow automation)
- Midjourney: `TOOL-AI-###` (AI image generation)
- Perplexity: `TOOL-AI-###` (AI research)
- Eleven Labs: `TOOL-AI-###` (AI voice synthesis)
- VAYU: `TOOL-VIDEO-###` (Video generation)
- Seedream: `TOOL-VIDEO-###` (Video effects)

### Department Codes
Use ISO 3-letter consonant codes:
- **AID** - AI & Automations (not AIA)
- **DEV** - Development
- **HRM** - Human Resources
- **LGN** - Lead Generation
- **DGN** - Design
- **VID** - Video Production
- **SLS** - Sales
- **SMM** - Social Media Management
- **FIN** - Finance

Multi-department objects use semicolon separation: `"VID;DGN"`

---

## Related Documentation

- [Video Transcription Custom Instructions](../Transcription/Video_Transcription_Custom_Instructions.md)
- [Video Analysis Prompt](./Video_Analysis_Prompt.md)
- [Taxonomy Analysis and Updates Prompt](../Taxonomy_Integration/Taxonomy_Analysis_and_Updates_Prompt.md)
- [Objects Library README](../../../LIBRARIES/Responsibilities/Objects/README.md)
- [LIBRARIES README](../../../LIBRARIES/README.md)
- [ISO Code Registry](../../../LIBRARIES/Taxonomy/Libraries_ISO_Code_Registry.md)
- [Skills Documentation](../../../LIBRARIES/Skills/README.md)

---

**Maintained By**: Taxonomy Team
**Version**: 2.0 - Taxonomy Architecture Alignment
**Last Updated**: 2025-11-25
**Status**: Active - Production Ready
