# Video Taxonomy: Complete Step-by-Step Tutorial

**Purpose:** Walk through the entire process of extracting taxonomy from a video with detailed examples
**Time Required:** 2-4 hours per video
**Difficulty:** Intermediate
**Version:** 1.0.0
**Date:** 2025-12-04

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step-by-Step Process](#step-by-step-process)
3. [Detailed Example: Analyzing a Video About AI Tools](#detailed-example)
4. [Common Pitfalls and Solutions](#common-pitfalls)
5. [Quality Checklist](#quality-checklist)

---

## Prerequisites

### What You Need

1. **Video transcription file** in `02_TRANSCRIPTIONS/Video_XXX.md`
2. **Text editor** (VS Code, Sublime, Notepad++)
3. **Access to folders:**
   - `ENTITIES/LIBRARIES/Tools/AI_Tools/`
   - `ENTITIES/LIBRARIES/Responsibilities/Objects/`
   - `ENTITIES/TASK_MANAGERS/Workflows/`
   - `ENTITIES/TAXONOMY/TAX-001_Libraries/`
   - `ENTITIES/TAXONOMY/TAX-002_Task_Managers/`

4. **Master list access:**
   - `Libraries_Master_List.csv`
   - `Taxonomy_Master_List.csv`

5. **Prompt file:**
   - `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`

### Skills Needed

- Basic text editing
- Understanding of JSON format
- Ability to follow structured workflows
- Attention to detail for cross-referencing

---

## Step-by-Step Process

### PHASE 1: Initial Video Analysis (30-45 minutes)

#### Step 1.1: Read Video Transcription

**Location:** `ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`

**What to do:**
1. Open the transcription file
2. Read through once at normal pace
3. Get familiar with:
   - Main topics discussed
   - Tools mentioned
   - Workflows described
   - Key terminology used

**Example opening:**
```markdown
# Video Transcription: 10 AI Tools for Content Creators

**Duration:** 15:30
**Speaker:** Tech Reviewer
**Date:** 2025-12-01

## [00:00] Introduction
Today I'm showing you 10 incredible AI tools that will
revolutionize your content creation workflow...

## [00:45] Tool #1: GLIF
GLIF is an amazing workflow automation platform...
```

#### Step 1.2: Create Tools Inventory

**Create a new working document:** `Video_XXX_Working_Notes.md`

**Extract tools with this format:**

```markdown
# TOOLS INVENTORY

## Tool 1: GLIF
- **Category:** AI/Workflow Automation
- **First Mention:** [00:45]
- **Total Mentions:** 8 times
- **Timestamps:** [00:45], [03:20], [05:10], [08:15], [10:30], [12:05], [13:40], [14:55]
- **Context Quotes:**
  - "GLIF orchestrates multiple AI tools together" [00:45]
  - "You can create automated workflows with GLIF" [03:20]
  - "GLIF integrates with Perplexity and VAYU" [05:10]
- **Use Cases Mentioned:**
  - Automated documentary creation
  - Thumbnail generation workflows
  - Multi-tool orchestration
- **Pricing Mentioned:** Freemium (free tier available, pro features paid)
- **URL Mentioned:** glif.app

## Tool 2: Nano Banana
- **Category:** AI/Image Generation (Thumbnails)
- **First Mention:** [02:30]
- **Total Mentions:** 5 times
- **Timestamps:** [02:30], [03:45], [06:20], [09:10], [13:25]
- **Context Quotes:**
  - "Nano Banana is specifically trained for YouTube thumbnails" [02:30]
  - "It creates high-CTR thumbnails in seconds" [03:45]
- **Use Cases Mentioned:**
  - YouTube thumbnail creation
  - Social media thumbnail optimization
  - Mr. Beast style thumbnails
- **Pricing Mentioned:** Access via GLIF
- **URL Mentioned:** Not directly mentioned

[Continue for all tools...]
```

**Tips:**
- Use video timestamps to find mentions quickly
- Copy exact quotes for accuracy
- Note if tool is integrated with another tool
- Record pricing information if mentioned
- Capture URLs/websites if mentioned

#### Step 1.3: Create Objects Inventory

**In same working document, add:**

```markdown
# OBJECTS INVENTORY

## Object 1: Thumbnails
- **Category:** Design Deliverables
- **First Mention:** [02:30]
- **Total Mentions:** 12 times
- **Object Types Identified:**
  - YouTube thumbnail [02:30], [03:45], [06:20]
  - Social media thumbnail [04:10]
  - High-CTR thumbnail [03:45], [09:10]
  - Mr. Beast style thumbnail [06:20]
- **Tools That Create It:**
  - Nano Banana (primary) [02:30]
  - GLIF (workflow automation) [05:10]
  - Midjourney (concept exploration) [07:45]
- **Professions Mentioned:**
  - Content Creator [02:30]
  - YouTuber [03:45]
  - Graphic Designer [04:10]
- **Creation Process:**
  1. Define thumbnail concept [02:30]
  2. Generate using Nano Banana via GLIF [05:10]
  3. Refine prompt for style [06:20]
  4. Select best variant [06:35]
  5. Add text overlay [06:50]
  6. Export final thumbnail [07:05]
- **Time Estimate:** 15 minutes (mentioned at [07:05])
- **Platforms Used:**
  - YouTube (primary) [02:30]
  - TikTok [04:10]
  - Instagram [04:15]

## Object 2: Videos (Miniature Documentary)
- **Category:** Media
- **First Mention:** [08:00]
- **Total Mentions:** 10 times
- **Object Types Identified:**
  - Miniature documentary [08:00]
  - 32-second documentary [08:15]
  - Historical documentary [08:30]
  - Educational video [09:45]
- **Tools That Create It:**
  - VAYU 2.2 (video generation) [08:45]
  - Seedream (tilt-shift effects) [09:00]
  - Perplexity (research) [08:00]
  - Eleven Labs (voiceover) [09:30]
  - GLIF (orchestration) [10:00]
- **Professions Mentioned:**
  - Content Creator [08:00]
  - Video Producer [08:15]
  - Documentary Producer [08:30]
- **Creation Process:**
  1. Research historical topic with Perplexity [08:00]
  2. Generate script with AI [08:30]
  3. Create tilt-shift video with VAYU + Seedream [08:45]
  4. Generate voiceover with Eleven Labs [09:30]
  5. Combine all elements with GLIF [10:00]
  6. Review and publish [10:15]
- **Time Estimate:** 10-20 minutes (mostly automated) [10:15]
- **Duration:** 32 seconds optimal [08:15]
- **Platforms Used:**
  - TikTok [10:30]
  - Instagram Reels [10:35]
  - YouTube Shorts [10:40]

[Continue for all objects...]
```

#### Step 1.4: Create Actions Inventory

```markdown
# ACTIONS INVENTORY

## CREATION VERBS

### "Create"
- **Total Occurrences:** 15
- **Timestamps:** [00:45], [01:20], [02:30], [03:15], [04:10], [05:20], [06:00], [07:15], [08:00], [08:30], [09:45], [11:20], [12:10], [13:30], [14:45]
- **Contexts:**
  - "create thumbnails" [02:30], [06:00]
  - "create videos" [08:00], [11:20]
  - "create documentaries" [08:30]
  - "create workflows" [00:45], [05:20]
  - "create content" [09:45], [12:10]
  - "create presentations" [13:30]
  - "create social media posts" [14:45]
- **Objects Acted Upon:** thumbnails, videos, documentaries, workflows, content, presentations, social media posts

### "Generate"
- **Total Occurrences:** 23
- **Timestamps:** [01:20], [02:30], [03:15], [03:45], [04:30], [05:10], [06:20], [06:45], [07:30], [08:15], [08:30], [09:00], [09:30], [10:00], [10:45], [11:30], [12:00], [12:45], [13:15], [13:50], [14:20], [14:40], [15:00]
- **Contexts:**
  - "generate thumbnails" [02:30], [03:45], [06:20]
  - "generate videos" [08:15], [09:00], [11:30]
  - "generate scripts" [08:30], [12:00]
  - "generate voiceovers" [09:30], [12:45]
  - "generate images" [06:45], [13:15]
  - "generate content" [10:00], [14:20]
- **Objects Acted Upon:** thumbnails, videos, scripts, voiceovers, images, content

[Continue for all action categories: MODIFICATION, ANALYSIS, ORGANIZATION, COMMUNICATION...]
```

#### Step 1.5: Create Workflows Inventory

```markdown
# WORKFLOWS INVENTORY

## Workflow 1: Automated Miniature Documentary Creation

### Overview
- **Name:** Automated Miniature Documentary Creation
- **Objective:** Generate 32-second historical documentary with research, visuals, and narration
- **First Mentioned:** [08:00]
- **Detailed At:** [08:00] - [10:30]
- **Duration:** 10-20 minutes (mostly automated)
- **Automation Level:** Fully Automated via GLIF
- **Department:** VID;AID

### Detailed Steps

**Step 1: Research Historical Facts**
- **Timestamp:** [08:00]
- **Action:** Research
- **Tool:** Perplexity
- **Description:** "Use Perplexity to research and fact-check historical information"
- **Input:** Historical topic name (e.g., "Ancient Rome")
- **Output:** Verified historical facts and context (3-5 paragraphs)
- **Duration:** 2-3 minutes (automated)
- **Quote:** "Perplexity does all the research and fact-checking for you" [08:00]

**Step 2: Generate Documentary Script**
- **Timestamp:** [08:30]
- **Action:** Generate
- **Tool:** ChatGPT (or AI within GLIF)
- **Description:** "AI generates a compelling 32-second documentary script from the research"
- **Input:** Historical facts from Perplexity
- **Output:** 32-second documentary script (80-100 words)
- **Duration:** 1-2 minutes (automated)
- **Quote:** "The AI writes a perfect 32-second script automatically" [08:30]

**Step 3: Create Tilt-Shift Video**
- **Timestamp:** [08:45]
- **Action:** Create
- **Tool:** VAYU 2.2 + Seedream
- **Description:** "VAYU generates miniature-style video, Seedream adds tilt-shift effects"
- **Input:** Documentary script + visual description
- **Output:** 32-second video with tilt-shift miniature look (no audio)
- **Duration:** 3-5 minutes (automated)
- **Quote:** "VAYU creates this amazing miniature world effect, and Seedream enhances it" [08:45]

**Step 4: Generate Voiceover Narration**
- **Timestamp:** [09:30]
- **Action:** Generate
- **Tool:** Eleven Labs
- **Description:** "Professional AI voice narrates the documentary script"
- **Input:** 32-second documentary script
- **Output:** Professional narration audio (32 seconds, MP3/WAV)
- **Duration:** 1-2 minutes (automated)
- **Quote:** "Eleven Labs makes it sound like a professional narrator" [09:30]

**Step 5: Combine Video and Audio**
- **Timestamp:** [10:00]
- **Action:** Combine
- **Tool:** GLIF (automation)
- **Description:** "GLIF automatically combines the video and audio"
- **Input:** Tilt-shift video + narration audio
- **Output:** Final 32-second documentary with narration (MP4)
- **Duration:** 1-2 minutes (automated)
- **Quote:** "GLIF handles all the combining automatically" [10:00]

**Step 6: Review and Publish**
- **Timestamp:** [10:15]
- **Action:** Review, Publish
- **Tool:** Manual (human review)
- **Description:** "Quick review of final video, then publish to platforms"
- **Input:** Final documentary video
- **Output:** Published content on TikTok, Instagram, YouTube
- **Duration:** 2-5 minutes (manual)
- **Quote:** "Just review it quickly and hit publish" [10:15]

### Workflow Summary
- **Total Duration:** 10-20 minutes
- **Automated Steps:** 5 out of 6 (83%)
- **Manual Steps:** 1 (review and publish)
- **Tools Used:** 5 (Perplexity, ChatGPT, VAYU, Seedream, Eleven Labs, GLIF)
- **Objects Created:** 1 primary (miniature documentary video)
- **Objects Used:** 2 intermediate (script, narration audio)
- **Business Value:** "10x faster than manual documentary production" [10:30]

### Related Information
- **Professions:** Content Creator, Video Producer, Documentary Producer
- **Skills Required:**
  - Prompt engineering (for AI tools)
  - Workflow automation (GLIF setup)
  - Content strategy (topic selection)
- **Use Cases:**
  - Educational social media content [10:30]
  - Historical storytelling for brands [10:35]
  - Online academy content [10:40]
- **Platforms:** TikTok, Instagram Reels, YouTube Shorts

[Continue for all workflows...]
```

#### Step 1.6: Create Professions Inventory

```markdown
# PROFESSIONS INVENTORY

## Profession 1: Content Creator

### Basic Information
- **First Mentioned:** [00:30]
- **Total Mentions:** 18 times
- **Context:** "This is perfect for content creators who want to automate their workflow" [00:30]

### Responsibilities Extracted
From video context:
1. "creating thumbnails" [02:30]
2. "editing videos" [03:45]
3. "optimizing for social media" [04:10]
4. "managing content calendar" [05:20]
5. "creating engaging content" [06:00]
6. "building audience" [12:30]
7. "automating workflows" [00:45]
8. "producing videos quickly" [08:00]
9. "A/B testing content" [06:20]

### Tools Mentioned for Content Creator
1. **GLIF** [00:45]
   - Purpose: "Automate entire content workflow"
   - Frequency: Used daily (implied)

2. **Nano Banana** [02:30]
   - Purpose: "Create YouTube thumbnails"
   - Frequency: Used weekly (implied)

3. **VAYU** [08:45]
   - Purpose: "Generate documentary videos"
   - Frequency: Used for specific content types

4. **Eleven Labs** [09:30]
   - Purpose: "Create voiceovers"
   - Frequency: Used regularly

5. **Midjourney** [07:45]
   - Purpose: "Create concept art and references"
   - Frequency: Used occasionally

### Objects Content Creator Works With
1. **Thumbnails** [02:30]
   - Actions: Create, Generate, Optimize, Design

2. **Videos** [08:00]
   - Types: Miniature documentary, TikTok video, Social video
   - Actions: Create, Produce, Generate, Edit, Publish

3. **Scripts** [08:30]
   - Types: Documentary script, Video script
   - Actions: Generate, Create, Refine

### Workflows Content Creator Performs
1. **Automated Miniature Documentary Creation** [08:00]
2. **YouTube Thumbnail Optimization** [02:30]
3. **Social Media Content Automation** [04:10]

### Skills Required
1. **Prompt Engineering** [01:20]
   - Application: "Refining AI video generation prompts"
   - Proficiency: Intermediate

2. **Thumbnail Design** [02:30]
   - Application: "Creating high-CTR thumbnails"
   - Proficiency: Intermediate

3. **Workflow Automation** [00:45]
   - Application: "Setting up GLIF agent-based pipelines"
   - Proficiency: Beginner to Intermediate

4. **Content Strategy** [12:30]
   - Application: "Planning content for audience building"
   - Proficiency: Intermediate

### Typical Day (Extracted)
From video context:
- Review content calendar [05:20]
- Set up automated workflows in GLIF [00:45]
- Generate thumbnail variants [02:30], [06:20]
- Review automated video outputs [10:15]
- Optimize content based on metrics [12:30]
- Plan next week's content [13:45]

[Continue for all professions: YouTuber, Video Producer, Graphic Designer, etc...]
```

#### Step 1.7: Create Skills Inventory

```markdown
# SKILLS INVENTORY

## Skill 1: Prompt Engineering

### Basic Information
- **First Mentioned:** [01:20]
- **Total Mentions:** 12 times
- **Context:** "You need good prompt engineering skills to get the best results" [01:20]

### Definition (Inferred from Video)
"The ability to craft effective prompts for AI tools to achieve desired outputs, particularly for video generation, thumbnail creation, and content optimization"

### Skill Phrase
"refined AI video generation prompts"

### Applications Mentioned
1. "Optimizing thumbnail generation prompts" [03:45]
2. "Refining video generation prompts" [08:45]
3. "Improving AI script generation" [08:30]
4. "Enhancing voiceover quality through prompts" [09:30]
5. "Getting better results from image AI" [07:45]

### Tools Associated
1. **GLIF** [01:20] - "Prompt engineering is crucial for GLIF workflows"
2. **Nano Banana** [03:45] - "Better prompts = better thumbnails"
3. **VAYU** [08:45] - "Detailed prompts create better miniature videos"
4. **Midjourney** [07:45] - "Prompt structure matters for concept art"

### Proficiency Levels
- **Beginner:** Basic prompts work but results vary
- **Intermediate:** Can refine prompts for consistent quality (mentioned as sufficient [01:20])
- **Advanced:** Optimize prompts for specific styles and outputs

### Professions Requiring This Skill
1. Content Creator [01:20]
2. Video Producer [08:00]
3. Graphic Designer [07:45]
4. AI Engineer [00:45]

### Related Objects
1. **Videos** [08:45] - Created with AI prompts
2. **Thumbnails** [03:45] - Generated with optimized prompts
3. **Scripts** [08:30] - AI-generated via prompts
4. **Images** [07:45] - Created through prompt engineering

### Related Actions
1. **Refine** [01:20], [03:45], [08:45]
2. **Optimize** [03:20], [09:10]
3. **Generate** [Multiple instances]
4. **Create** [Multiple instances]

### Learning Resources (If Mentioned)
- Not explicitly mentioned in this video

[Continue for all skills: Thumbnail Design, Workflow Automation, Video Editing, etc...]
```

---

### PHASE 2: Gap Analysis (20-30 minutes)

#### Step 2.1: Check Existing Tools

**For each tool in your inventory:**

1. **Navigate to tools folder:**
   ```
   G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools\
   ```

2. **Search for tool:**
   ```bash
   ls *.json | grep -i "glif"
   ```

3. **Document findings:**

```markdown
# TOOLS GAP ANALYSIS

## Tools Already in Taxonomy (TO ENHANCE)

### 1. Eleven Labs
- **File:** ElevenLabs.json
- **Status:** EXISTS
- **Action:** ENHANCE
- **What to Add:**
  - New use case: "Documentary narration creation" [09:30]
  - New workflow: Automated Miniature Documentary Creation (WRF-###)
  - Integration note: Works with GLIF for automated workflows [10:00]
  - Duration: 1-2 minutes for 32-second narration [09:30]

### 2. Midjourney
- **File:** Midjourney.json
- **Status:** EXISTS
- **Action:** ENHANCE
- **What to Add:**
  - New use case: "Thumbnail concept exploration" [07:45]
  - New workflow: YouTube Thumbnail Creation (WRF-###)
  - Alternative: Can be used instead of Nano Banana [07:45]

[Continue for all existing tools...]

## Tools NOT in Taxonomy (TO CREATE)

### Priority: CRITICAL (Mentioned 10+ times)

#### 1. GLIF
- **File to Create:** GLIF.json
- **Tool ID to Assign:** TOL-??? (check master list)
- **Category:** AI/Workflow Automation
- **Mentions:** 30 times
- **First Mention:** [00:45]
- **Key Timestamps:** [00:45], [03:20], [05:10], [08:15], [10:30], [12:05], [13:40], [14:55]
- **Why Critical:** Core orchestration tool, mentioned most frequently
- **Data to Capture:**
  - Vendor: GLIF (glif.app)
  - Purpose: "AI workflow automation platform for orchestrating multiple AI tools"
  - Integration capabilities: Perplexity, VAYU, Seedream, Eleven Labs, Nano Banana
  - Use cases: Automated documentary creation, thumbnail workflows, multi-tool orchestration
  - Cost: Freemium (free tier + pro features)
  - Skill level: Beginner to Intermediate

#### 2. Sora
- **File to Create:** Sora.json
- **Tool ID to Assign:** TOL-??? (check master list)
- **Category:** AI/Video Generation
- **Mentions:** 15 times
- **First Mention:** [11:00]
- **Why Critical:** OpenAI's video generation tool, frequently mentioned
- **Data to Capture:**
  - Vendor: OpenAI
  - Purpose: "Text-to-video AI generation"
  - Use cases: General video generation, marketing videos
  - Cost: Paid (OpenAI subscription required)

### Priority: HIGH (Mentioned 5-9 times)

#### 3. Nano Banana
- **File to Create:** Nano_Banana.json
- **Tool ID to Assign:** TOL-???
- **Category:** AI/Image Generation (Thumbnails)
- **Mentions:** 8 times
- **First Mention:** [02:30]
- **Why High:** Specialized thumbnail tool, specific use case
- **Data to Capture:**
  - Access: Via GLIF
  - Purpose: "YouTube thumbnail generation optimized for CTR"
  - Training: "Specifically trained on high-performing YouTube thumbnails" [02:30]
  - Use cases: YouTube thumbnails, social thumbnails, Mr. Beast style
  - Integration: GLIF workflow automation

#### 4. VAYU 2.2
- **File to Create:** VAYU.json
- **Tool ID to Assign:** TOL-???
- **Category:** AI/Video Generation (Miniature)
- **Mentions:** 10 times
- **First Mention:** [08:45]
- **Why High:** Unique miniature documentary style
- **Data to Capture:**
  - Purpose: "Miniature-style documentary video generation"
  - Visual style: "Tilt-shift, miniature world appearance" [08:45]
  - Integration: Works with Seedream for enhancement [09:00]
  - Output: 32-second optimal duration [08:15]
  - Use cases: Historical documentaries, educational videos

#### 5. Seedream
- **File to Create:** Seedream.json
- **Tool ID to Assign:** TOL-???
- **Category:** AI/Video Effects
- **Mentions:** 8 times
- **First Mention:** [09:00]
- **Why High:** Pairs with VAYU for tilt-shift
- **Data to Capture:**
  - Purpose: "Tilt-shift effects and miniature enhancement"
  - Integration: Works with VAYU 2.2 [09:00]
  - Effect: "Makes videos look like miniature worlds" [09:00]

### Priority: MEDIUM (Mentioned 2-4 times)

[Continue with medium priority tools...]

### Priority: LOW (Mentioned once)

[Continue with low priority tools...]

## Coverage Metrics

### Before Analysis:
- Tools mentioned in video: 10
- Tools in taxonomy: 2
- Coverage: 20%

### After Analysis (Projected):
- Tools mentioned: 10
- Tools existing: 2
- Tools to create: 8
- Projected coverage: 100%

### Gap:
- Missing: 8 tools (80% gap)
- Critical: 2 tools
- High: 3 tools
- Medium: 2 tools
- Low: 1 tool
```

#### Step 2.2: Check Existing Objects

```markdown
# OBJECTS GAP ANALYSIS

## Check Design Deliverables

**File:** `ENTITIES/LIBRARIES/Responsibilities/Objects/Design_Deliverables.json`

**Read file and check for:**
1. Thumbnails
2. Banners
3. Logos
4. Illustrations
5. UI Mockups

### Results:

✅ **EXISTS:** Banners, Logos, Illustrations, UI Mockups, Presentations

❌ **MISSING:** Thumbnails

## Thumbnails - MISSING (TO CREATE)

### Details:
- **Object ID to Assign:** OBJ-??? (check master list)
- **Object Name:** thumbnails (singular form)
- **Category:** Design Deliverables
- **Object Types to Add:**
  - YouTube thumbnail [02:30]
  - Social media thumbnail [04:10]
  - High-CTR thumbnail [03:45]
  - Mr. Beast style thumbnail [06:20]
  - Educational thumbnail [11:30]

### Tools That Create This Object:
1. Nano Banana (TOL-???) - Primary [02:30]
2. GLIF (TOL-???) - Workflow automation [05:10]
3. Midjourney (TOL-006) - Concept exploration [07:45]
4. Photoshop - Manual creation (not in video, but standard)
5. Canva - Manual creation (not in video, but standard)

### Professions That Use This Object:
1. Content Creator [02:30]
2. YouTuber [03:45]
3. Graphic Designer [04:10]
4. Social Media Manager [04:15]

### Actions Performed on This Object:
1. Create [02:30]
2. Generate [03:45]
3. Optimize [03:20]
4. Design [06:00]
5. Test (A/B testing) [06:20]
6. Export [07:05]

### Workflows That Produce This Object:
1. YouTube Thumbnail Creation (High CTR) - WRF-??? [02:30]
2. Social Media Thumbnail Optimization - WRF-??? [04:10]

### Additional Data:
- **Time Estimate:** 15-30 minutes (AI-assisted) [07:05]
- **Platforms:** YouTube, TikTok, Instagram, Facebook
- **Dimensions:** 1920x1080px (YouTube) [mentioned context]
- **Optimization Metrics:** CTR (click-through rate) [03:20]
- **Best Practices:**
  - High contrast for visibility [06:00]
  - Bold text area [06:00]
  - Clear focal point [06:00]
  - Mr. Beast style for viral appeal [06:20]
  - A/B test multiple variants [06:20]

## Check Media Objects

**Check if file exists:** `ENTITIES/LIBRARIES/Responsibilities/Objects/Video_Deliverables.json` or `Media_Objects.json`

**If file doesn't exist, need to create it.**

### Results:

❌ **FILE MISSING:** Need to create Video_Deliverables.json or Media_Objects.json

## Videos - MISSING (TO CREATE FILE + OBJECT)

### Details:
- **File to Create:** Video_Deliverables.json
- **Object ID to Assign:** OBJ-???
- **Object Name:** videos (singular form)
- **Category:** Media
- **Object Types to Add:**
  - Miniature documentary [08:00]
  - 32-second documentary [08:15]
  - TikTok video [10:30]
  - Social media video [04:10]
  - AI video [08:45]
  - Educational video [09:45]

### Complete structure needed (see Phase 3 for creation)

[Continue gap analysis for all objects...]
```

#### Step 2.3: Check Existing Actions

```markdown
# ACTIONS GAP ANALYSIS

**File:** `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`

## Read and Check

### Action: "Generate"
- **Status:** EXISTS (ACT-042 or similar)
- **Action:** ENHANCE
- **Current Contexts:**
  - "generate images"
  - "generate text"
  - "generate code"
- **Add New Contexts:**
  - "generate videos" [08:15]
  - "generate thumbnails" [03:45]
  - "generate scripts" [08:30]
  - "generate voiceovers" [09:30]
  - "generate documentaries" [08:00]

### Action: "Create"
- **Status:** EXISTS (ACT-001 or similar)
- **Action:** ENHANCE
- **Add New Contexts:**
  - "create thumbnails" [02:30]
  - "create documentaries" [08:00]
  - "create workflows" [00:45]

### Action: "Optimize"
- **Status:** EXISTS (ACT-??? check file)
- **Action:** ENHANCE
- **Add New Contexts:**
  - "optimize for CTR" [03:20]
  - "optimize thumbnails" [06:00]
  - "optimize social media content" [04:10]

[Continue for all actions...]

## Actions Potentially Missing

Check if these exist; if not, they may already be in master:
- "Orchestrate" (for GLIF workflows) [00:45]
- "Automate" (for workflow automation) [00:45]
- "Combine" (for merging video + audio) [10:00]
- "Narrate" (for voiceover) [09:30]

Most likely these are already in Actions_Master.json under different action IDs.
```

[Continue document with remaining phases...]
