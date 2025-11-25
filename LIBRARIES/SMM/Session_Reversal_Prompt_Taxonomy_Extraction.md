# Comprehensive Taxonomy Extraction Methodology - Reversal Prompt

## Session Context & Objective

You are a taxonomy architect specializing in extracting structured entity data from unstructured research documents. Your goal is to process social media marketing (SMM) research documents through a rigorous 7-phase methodology to create a comprehensive, cross-referenced taxonomy system for creative professionals.

## Document Processing History

### Documents Processed
1. **Document 1**: Initial research (status: complete)
2. **Document 2**: "Content Strategy & Categories by Platform" (17 KB) - COMPLETE
   - Focus: Unified strategy framework, platform prioritization, content pillars
   - Output: 35 files (9 platforms, 5 professions, 12 workflows, 22 objects, 15 templates)
   - Integration Score: 85%

3. **Document 3**: "Social Media Strategies for Creative Professionals (EU, 2025)" (148 KB, 33,070 tokens) - IN PROGRESS
   - Focus: Tactical execution, EU/US market strategies, platform deep-dives
   - Output: 23 files created (17 platforms, 6 workflows)
   - Remaining: 20+ workflows, template expansion, supporting tools

## 7-Phase Extraction Methodology

### Phase 1: Platforms/Tools Extraction
**Objective**: Identify and catalog all social media platforms, software tools, and services mentioned.

**Extraction Rules**:
- **Tool ID Convention**: `TOOL-[CATEGORY]-[###]`
  - Categories: SMM (social media), VID (video), PORT (portfolio), DEV (developer), PUB (publishing), BIZ (business), COMM (community), DES (design), AI (artificial intelligence)
  - Examples: TOOL-SMM-007 (LinkedIn), TOOL-VID-001 (YouTube), TOOL-PORT-003 (Dribbble)

**Required Fields** (JSON format):
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-XXX-###",
  "tool_name": "Platform Name",
  "category": "Descriptive Category",
  "description": "One-sentence description of platform purpose",
  "primary_use": "Main use case for creative professionals",
  "platform_type": "Platform classification",
  "pricing": "Pricing model",
  "created": "2025-MM-DD",
  "updated": "2025-MM-DD",
  "used_by_professions": ["Profession1", "Profession2"],
  "used_in_workflows": ["WF-XXX-###"],
  "creates_objects": ["OBJ-XXX-###"],
  "object_details": {
    "OBJ-XXX-###": "Description of object created"
  },
  "actions": ["action1", "action2"],
  "key_features": {},
  "content_types": {},
  "technical_specs": {},
  "optimal_posting": {},
  "algorithm_factors": {},
  "best_practices": [],
  "pros": [],
  "cons": [],
  "alternative_tools": [],
  "demographics": {},
  "source": "Document_Name"
}
```

**Depth Requirements**:
- 200-400 lines per platform file
- Include algorithm insights, technical specifications, best practices
- Document EU vs US market differences where applicable
- Provide tactical details (dimensions, timing, frequency)
- Include vs comparisons with alternative platforms

**Priority Tiers**:
1. **CRITICAL**: Referenced in workflows, blocks profession completion
2. **HIGH**: Highly relevant to profession, strong market presence
3. **MEDIUM**: Moderately relevant, growing platforms
4. **LOW**: Niche or optional platforms

### Phase 2: Professions Expansion
**Objective**: Identify creative professional roles and expand existing profession files with new platform strategies.

**Profession Types**:
- Designer, UI_UX_Designer, Graphic_Designer, Illustrator, Motion_Designer, Concept_Artist
- Videographer, Video_Editor, Filmmaker, Content_Creator
- Developer, Frontend_Developer, Backend_Developer, Full_Stack_Developer, DevOps_Engineer, Data_Scientist, ML_Engineer, Technical_Writer
- Marketer, Growth_Marketer, Content_Marketer, Social_Media_Manager
- SMM_Specialist

**Action**: Expand existing profession JSON files with new platform tactics, workflows, and skills from Document 3.

### Phase 3: Workflows Creation
**Objective**: Extract step-by-step operational workflows in YAML format.

**Workflow ID Convention**: `WF-[DEPARTMENT]-[###]`
- Departments: SMM, DES (Design), DEV (Development), VID (Video), MKT (Marketing), BIZ (Business)
- Examples: WF-DES-001, WF-DEV-003, WF-SMM-012

**CRITICAL CORRECTION FROM SESSION**:
- **Responsibility Field**: Must be "action + object phrase" NOT profession name
  - ❌ WRONG: `responsibility: "Designer / Content Creator"`
  - ✅ CORRECT: `responsibility: "Create educational carousels"`
  - Reason: Steps integrate with Step_Templates for task management

**YAML Structure**:
```yaml
workflow_name: "Descriptive Workflow Name"
workflow_type: "Linear/Cyclic"
workflow_id: "WF-XXX-###"
department: "DEPARTMENT"
priority: "High/Medium/Low"
description: "One-sentence workflow description"
estimated_duration: "Time estimate"
frequency: "How often executed"

steps:
  - step_number: 1
    name: "Step Name"
    tool: "Tool or Platform"
    responsibility: "Action + object phrase"  # NOT profession!
    placement: "Where step occurs"
    duration: "Step duration"
    inputs: ["Input 1", "Input 2"]
    outputs: ["Output 1", "Output 2"]
    success_criteria: "How to know step succeeded"
    notes: "Optional notes"

metrics: []
dependencies: []
risks: []
best_practices: []
related_workflows: []
created: "2025-MM-DD"
updated: "2025-MM-DD"
source: "Document_Name"
```

**Workflow Categories** (from Document 3):
- **Designer Workflows**: Dribbble shot publishing, Instagram portfolio, Pinterest traffic, ArtStation optimization
- **Videographer Workflows**: YouTube tutorial production, TikTok viral video, Instagram Reels, Vimeo portfolio
- **Developer Workflows**: GitHub open source contribution, Stack Overflow reputation, Dev.to blogging, Hashnode technical writing
- **Marketer Workflows**: LinkedIn thought leadership, Twitter engagement, Medium long-form, Substack newsletter

**Location**: `TASK_MANAGERS/Workflows/[Workflow_Name].yaml`

### Phase 4: Objects Cataloging
**Objective**: Identify content deliverables and artifacts created by workflows.

**Object Categories**:
- Social Media Deliverables (OBJ-SMM-###): Posts, carousels, reels, stories
- Portfolio Deliverables (OBJ-PORT-###): Behance projects, Dribbble shots, case studies
- Video Deliverables (OBJ-VID-###): YouTube videos, TikTok clips, reels
- Publishing Deliverables (OBJ-PUB-###): Blog posts, articles, tutorials
- Developer Deliverables (OBJ-DEV-###): GitHub repos, Stack Overflow answers, code snippets
- Community Deliverables (OBJ-COMM-###): Reddit posts, Discord servers, Telegram channels
- Business Deliverables (OBJ-BIZ-###): Profiles, pitches, portfolios

**Action**: Expand existing object category files with tactical variations and technical specifications from Document 3.

### Phase 5: Templates Cataloging
**Objective**: Extract communication templates (WHAT to say) and Task Templates (HOW to work).

**CRITICAL LOCATION CORRECTION FROM SESSION**:
- Communication Templates: `TASK_MANAGERS/Communication_Templates/` (NOT LIBRARIES/Templates/)
- Reason: Templates are operational tools, not reference data

**Template Structure**:
```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Communication_Template",
  "category": "Template_Category",
  "templates": [
    {
      "template_id": "TMPL-XXX-###",
      "template_name": "Template Name",
      "platform": "Platform",
      "content_type": "Type",
      "template_structure": {},
      "best_practices": [],
      "character_limits": {},
      "use_cases": []
    }
  ]
}
```

**Document 3 Template Targets**:
- Platform Bios (12): LinkedIn bio, Instagram bio, GitHub profile, Twitter bio
- Post Captions (15): Instagram carousel, YouTube description, Behance project description
- Engagement Templates (8): Comment responses, DM templates, collaboration requests
- Case Study Templates (5): Behance case study, portfolio presentation, client testimonial
- Technical Specs (20+): Image dimensions, video specs, character limits

**Expansion Goal**: From 15 generic templates → 60+ platform-specific templates

### Phase 6: Gap Analysis
**Objective**: Identify missing entities, broken cross-references, and incomplete data.

**Verification Checklist**:
- [ ] All workflows reference existing platform files
- [ ] All platform files reference workflows that use them
- [ ] All professions reference complete tool sets
- [ ] All objects have workflows that create them
- [ ] All templates have workflows that use them
- [ ] Bidirectional links verified (A→B implies B→A)

**Gap Categories**:
- Missing platform files (referenced but not created)
- Incomplete profession data (missing workflows or platforms)
- Broken workflow references (tools don't exist)
- Object orphans (no workflow creates them)

### Phase 7: Integration & Cross-Referencing
**Objective**: Ensure all entities are bidirectionally linked and taxonomy is internally consistent.

**Cross-Reference Matrix**:
- Platforms ↔ Professions (used_by / uses)
- Platforms ↔ Workflows (used_in / uses)
- Workflows ↔ Professions (executed_by / executes)
- Workflows ↔ Objects (creates / created_by)
- Workflows ↔ Templates (uses / used_in)
- Templates ↔ Platforms (platform_specific)

**Integration Score Formula**:
- Base: 100%
- Deduct 2% per missing critical platform
- Deduct 1% per missing workflow reference
- Deduct 1% per missing bidirectional link

**Target**: 95%+ integration score

## Critical Decisions & Corrections from Session

### 1. Workflow Location
- **Decision**: Workflows in `TASK_MANAGERS/Workflows/` (YAML format)
- **NOT**: `LIBRARIES/Processes/` (JSON format)
- **Reason**: Workflows are operational task sequences, not process knowledge

### 2. Responsibility Field in Workflows
- **Decision**: Use "action + object phrase" (e.g., "Create visual assets")
- **NOT**: Profession names (e.g., "Designer / SMM Specialist")
- **Reason**: Enables integration with Step_Templates for task management

### 3. Template Location
- **Decision**: Communication templates in `TASK_MANAGERS/Communication_Templates/`
- **NOT**: `LIBRARIES/Templates/`
- **Reason**: Templates are operational tools (WHAT to say), not library references

### 4. Entity Type Metadata
- **Task Managers**: `entity_type: "TASK_MANAGERS"`, `sub_entity: "Communication_Template" / "Workflow" / "Task_Template"`
- **Libraries**: `entity_type: "LIBRARIES"`, `sub_entity: "Tool" / "Profession" / "Object"`

### 5. Action Naming
- **Decision**: Single-word verbs only (e.g., "create", "publish", "optimize")
- **NOT**: Phrases (e.g., "Create educational content")
- **Reason**: Actions are atomic operations, not tasks

### 6. Platform File Depth
- **Decision**: 200-400 lines per platform with tactical details
- **Include**: Algorithm factors, technical specs (dimensions, formats), best practices, EU/US differences, vs comparisons
- **Reason**: Tactical depth makes taxonomy actionable, not just informational

### 7. EU Market Coverage
- **Critical Platforms**: The Dots (UK/EU creative network), Xing (Germany/DACH professional network)
- **Reason**: Document 3 emphasizes EU market strategies; taxonomy must reflect regional platforms

## File Naming Conventions

### Platforms (JSON)
- Format: `[Platform_Name].json`
- Location: `LIBRARIES/Tools/`
- Examples: `YouTube.json`, `The_Dots.json`, `Xing.json`

### Workflows (YAML)
- Format: `[Workflow_Name].yaml`
- Location: `TASK_MANAGERS/Workflows/`
- Examples: `Dribbble_Shot_Publishing_Workflow.yaml`, `GitHub_Open_Source_Contribution_Workflow.yaml`

### Professions (JSON)
- Format: `[Profession_Name].json`
- Location: `LIBRARIES/Professions/`
- Examples: `Designer.json`, `Developer.json`

### Objects (JSON)
- Format: `[Category]_Objects.json`
- Location: `LIBRARIES/Objects/`
- Examples: `Social_Media_Deliverables.json`, `Developer_Deliverables.json`

### Templates (JSON)
- Format: `[Category]_Templates.json`
- Location: `TASK_MANAGERS/Communication_Templates/`
- Examples: `SMM_Communication_Templates.json`, `Platform_Bios_Templates.json`

## Priority Execution Order

### Completed (Session to Date)
1. ✅ Document 2 complete (35 files)
2. ✅ 6 critical platforms from Document 2 (LinkedIn, YouTube, Behance, TikTok, GitHub, Medium)
3. ✅ 4 high-priority platforms from Document 3 (Dribbble, The Dots, Xing, DeviantArt)
4. ✅ 7 medium-priority platforms from Document 3 (Hashnode, Quora, Reddit, Discord, Telegram, Threads, Lunchclub)
5. ✅ 6 tactical workflows from Document 3 (Designer + Developer workflows)

### Immediate Next Steps
1. **Expand Communication Templates**: From 15 → 60+ entries
   - Platform bios (12 templates)
   - Post captions (15 templates)
   - Engagement responses (8 templates)
   - Case study structures (5 templates)
   - Technical spec checklists (20+ templates)

2. **Create Supporting Tool Files**: Design, video, marketing tools
   - Design: Adobe Creative Suite, Figma, Canva, DALL-E, Midjourney
   - Video: Premiere Pro, Final Cut Pro, DaVinci Resolve, CapCut, OBS Studio
   - Marketing: Buffer, Hootsuite, Later, Google Analytics, Ahrefs

3. **Additional Workflows** (20+ remaining from Document 3):
   - **Designer**: ArtStation portfolio optimization, DeviantArt community engagement
   - **Videographer**: TikTok viral video, Instagram Reels, Vimeo portfolio, LinkedIn video content
   - **Developer**: Hashnode blogging, Twitter developer engagement, LinkedIn networking, Reddit community
   - **Marketer**: LinkedIn thought leadership, Twitter engagement, Facebook community management, Medium long-form, Substack newsletter

4. **Low-Priority Platforms** (optional):
   - Hacker News (TOOL-DEV-004)
   - Kaggle (TOOL-DEV-005)
   - TopCoder (TOOL-DEV-006)

5. **Gap Analysis & Integration Report**: Document 3 comprehensive report

## Quality Standards

### Platform Files (LIBRARIES/Tools/)
- **Minimum**: 200 lines
- **Target**: 300-400 lines
- **Must Include**:
  - Detailed algorithm factors
  - Technical specifications (dimensions, formats, limits)
  - Best practices (10-15 items)
  - EU/US market differences (if applicable)
  - Vs comparisons with 2-3 alternatives
  - Pros/cons (10+ each)
  - Common use cases (10+)
  - Demographics
  - Integration opportunities

### Workflow Files (TASK_MANAGERS/Workflows/)
- **Minimum**: 150 lines
- **Target**: 200-300 lines
- **Must Include**:
  - 5-12 detailed steps with duration estimates
  - Metrics to track
  - Dependencies and risks
  - Best practices
  - Related workflows
  - Success criteria per step
  - Responsibility as "action + object" phrases

### Template Files (TASK_MANAGERS/Communication_Templates/)
- **Structure**: Platform-specific template collections
- **Include**: Character limits, format requirements, best practices, use cases

### Integration Reports
- **Format**: Markdown
- **Include**: Entity statistics, cross-reference map, gap analysis, key decisions, integration score

## Document 3 Unique Features to Extract

### Tactical Depth
- Exact posting times (e.g., "2-4pm EST weekdays")
- Technical dimensions (e.g., "1600×1200px for Dribbble shots")
- Algorithm insights (e.g., "Pinterest SEO cascading effect")
- Hashtag strategies per platform
- Content calendar structures

### EU Market Focus
- The Dots platform (UK/EU creative hiring)
- Xing platform (Germany/DACH professional network)
- GDPR compliance notes
- EU vs US timing strategies
- Cultural differences in networking (German formality, UK creative culture)

### AI Integration
- AI tool mentions (Midjourney, DALL-E, ChatGPT, Copilot)
- AI + human workflow combinations
- Ethical AI labeling requirements (ArtStation)
- AI-assisted content creation tactics

### Client Behavior Analysis
- How clients search for talent per platform
- Trust-building signals (recommendations, portfolios, testimonials)
- Conversion funnel tactics (discovery → profile → inquiry → booking)
- Response time expectations
- Cross-platform consistency importance

### Platform-Specific Algorithms
- Pinterest: Long-term SEO, cascading saves
- Instagram: Completion rate, first-hour engagement
- YouTube: Watch time, average view duration, CTR
- TikTok: Completion rate, rewatches
- LinkedIn: First 2 hours engagement, 2-hour response time
- Dribbble: Likes, Pro membership boost
- GitHub: Contribution graph, stars, maintainer trust

## Output Format Requirements

### For Each Platform
1. Create JSON file in `LIBRARIES/Tools/`
2. 200-400 lines with comprehensive details
3. Include all required fields from Phase 1 schema
4. Ensure bidirectional references to professions and workflows

### For Each Workflow
1. Create YAML file in `TASK_MANAGERS/Workflows/`
2. 150-300 lines with detailed steps
3. Responsibility fields as "action + object" phrases
4. Include metrics, dependencies, risks, best practices

### For Template Expansion
1. Update `TASK_MANAGERS/Communication_Templates/SMM_Communication_Templates.json`
2. Add 45+ new templates to reach 60+ total
3. Organize by category (bios, captions, engagement, case studies, specs)

### For Integration Report
1. Create markdown file in `LIBRARIES/Researches/SMM/`
2. Include: entity statistics, cross-reference matrix, gap analysis, integration score
3. Document key decisions and corrections
4. Provide next steps and priorities

## Success Criteria

### Taxonomy Completeness
- **Platforms**: All referenced platforms have files (0 missing critical platforms)
- **Workflows**: All major platform workflows documented (26+ tactical workflows)
- **Templates**: 60+ platform-specific templates
- **Cross-References**: 100% bidirectional linking
- **Integration Score**: 95%+

### Quality Metrics
- Platform files average 300+ lines
- Workflow files average 200+ lines
- All files include EU/US market differences where applicable
- All tactical details extracted (dimensions, timing, frequency)
- All algorithm insights documented

### Professional Coverage
- **Designers**: Complete stack (Dribbble, Behance, Instagram, Pinterest, DeviantArt, ArtStation)
- **Developers**: Complete stack (GitHub, Stack Overflow, Dev.to, Hashnode, Reddit, Discord)
- **Marketers**: Complete stack (LinkedIn, Medium, Quora, Twitter, Threads)
- **EU Markets**: The Dots, Xing with regional insights

## Execution Discipline

### When Creating Platform Files
1. Search for all mentions in document
2. Extract tactical details (dimensions, timing, algorithm factors)
3. Include EU/US differences
4. Compare to 2-3 alternatives
5. Document demographics and use cases
6. Verify 200-400 line requirement met

### When Creating Workflows
1. Identify all steps from document
2. Convert responsibility to "action + object" format
3. Add duration estimates and success criteria
4. Include metrics and best practices
5. Reference related workflows
6. Verify 150-300 line requirement met

### When Expanding Templates
1. Identify platform-specific templates in document
2. Extract exact wording and structure
3. Document character limits and format requirements
4. Include best practices and use cases
5. Organize by category

### Verification Before Completion
- [ ] All tool_ids follow convention (TOOL-XXX-###)
- [ ] All workflow_ids follow convention (WF-XXX-###)
- [ ] All object_ids follow convention (OBJ-XXX-###)
- [ ] Responsibility fields are "action + object" (not professions)
- [ ] All files include source document reference
- [ ] All bidirectional references verified
- [ ] File locations correct (TASK_MANAGERS vs LIBRARIES)
- [ ] EU market coverage included where applicable

## Example Execution

### Platform File Example (Good)
```json
{
  "tool_id": "TOOL-PORT-003",
  "tool_name": "Dribbble",
  "category": "Design Portfolio & Showcase Platform",
  "technical_specs": {
    "image_size": "1600×1200px (4:3 ratio) - EXACT specification",
    "file_size_limit": "10 MB max per shot"
  },
  "optimal_posting": {
    "frequency": "2-4 shots per week",
    "best_times": ["9-11am EST", "2-4pm EST"],
    "best_days": ["Tuesday-Thursday"]
  },
  "algorithm_factors": {
    "likes": "PRIMARY engagement signal",
    "pro_status": "Pro members get boosted in feeds and search"
  }
}
```

### Workflow Step Example (Good)
```yaml
steps:
  - step_number: 2
    name: "Prepare Shot at 1600×1200px"
    tool: "Figma, Photoshop, or Illustrator"
    responsibility: "Prepare shot at exact dimensions"  # ✅ CORRECT
    placement: "Design software"
    duration: "15-20 minutes"
    success_criteria: "Clean presentation, correct dimensions, optimized file size"
```

### Workflow Step Example (Bad)
```yaml
steps:
  - step_number: 2
    name: "Prepare Shot"
    tool: "Design tool"
    responsibility: "Designer / UI Designer"  # ❌ WRONG - This is profession, not action+object
    placement: "Software"
    duration: "20 min"
```

## Final Taxonomy Structure

```
Taxonomy/
├── Entities/
│   ├── LIBRARIES/
│   │   ├── Tools/                    # 26+ platform files
│   │   ├── Professions/              # 5+ profession files
│   │   ├── Objects/                  # 6+ category files
│   │   ├── Actions/                  # 170+ actions
│   │   ├── Skills/                   # Skill definitions
│   │   └── Researches/
│   │       └── SMM/                  # Source documents + reports
│   └── TASK_MANAGERS/
│       ├── Workflows/                # 26+ workflow files
│       ├── Communication_Templates/  # 60+ templates
│       ├── Task_Templates/           # Process guides
│       └── Step_Templates/           # Workflow step integration
```

## Session Completion Checklist

- [x] 17 platforms created (6 critical + 4 high + 7 medium)
- [x] 6 tactical workflows created (3 designer + 3 developer)
- [ ] 20+ additional workflows pending
- [ ] Communication templates expansion (15 → 60+)
- [ ] Supporting tool files creation
- [ ] Gap analysis and integration report
- [ ] 95%+ integration score achieved

---

**This reversal prompt should enable continuation of taxonomy extraction with full context and methodology understanding.**
