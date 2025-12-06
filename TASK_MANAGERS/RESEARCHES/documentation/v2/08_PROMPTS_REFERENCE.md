# RESEARCHES 2 - Prompts Reference

**Version:** 2.0
**Generated:** 2025-12-04
**Purpose:** Complete reference for all 50+ processing and research prompts
**Audience:** All users - researchers, integrators, content processors

---

## 📖 Table of Contents

1. [Core Processing Prompts](#core-processing-prompts)
2. [Research Prompts](#research-prompts)
3. [Department-Specific Prompts](#department-specific-prompts)
4. [How to Use Prompts](#how-to-use-prompts)
5. [Prompt Best Practices](#prompt-best-practices)

---

## Core Processing Prompts

These are the essential prompts used in the 7-phase video processing workflow.

---

### PMT-004: Video Transcription v4.1

**Phase:** 1 (Transcription)
**Location:** `PROMPTS/Transcription/PMT-004_Video_Transcription_v4.1.md`
**Processing Time:** 1-2 hours
**Automation Level:** 60% (AI-assisted)

#### Purpose

Transform raw video transcript into structured markdown file with comprehensive taxonomy analysis, extracting 37+ pre-categorized entities across all 7 entity types.

#### Input Requirements

**Required:**
- Video URL
- Video title
- Channel name
- Duration (MM:SS format)
- Upload date
- Raw transcript with timestamps

**Optional:**
- Video description
- Tags/keywords
- Thumbnail URL

#### Output Format

Generates `Video_XXX.md` file containing:

1. **Video Metadata Section:**
   - Title, URL, Channel, Duration, Dates
   - Processed by whom
   - Video ID

2. **Video Summary:**
   - 3-5 paragraph executive summary
   - Main topics covered
   - Target audience
   - Key takeaways

3. **Pre-Categorized Entities (37+ minimum):**
   - **Workflows (WRF-###):** Multi-step processes identified
   - **Tools (TOL-###):** Software, platforms, services used
   - **Objects (OBJ-###):** Digital artifacts created/manipulated
   - **Actions (7 categories A-G):** Atomic operations
   - **Professions:** Job roles mentioned
   - **Skills:** Capabilities required
   - **Departments:** Organizational units relevant

4. **Integration Patterns:**
   - Tool → Object relationships
   - Workflow → Tool chains
   - Profession → Skill mappings

5. **Full Transcript:**
   - Complete timestamped transcript
   - Formatted for readability

6. **Extraction Metadata:**
   - Entity counts by type
   - Total entities extracted
   - Processing time
   - Quality check status

#### How to Use

**Step 1: Prepare Input**
```
Video Information:
- Title: [Full video title]
- URL: https://youtube.com/watch?v=XXX
- Channel: [Channel name]
- Duration: 18:42
- Upload Date: 2025-11-28
- Video ID: VID-024

Raw Transcript:
[00:00] Welcome to this tutorial...
[00:15] In this video we'll cover...
[Full transcript with timestamps]
```

**Step 2: Open AI Assistant**
- Claude (recommended - 200K context)
- ChatGPT (GPT-4 - 128K context)
- Gemini (1M context, experimental)

**Step 3: Paste Prompt**
- Copy entire PMT-004 prompt
- Paste into AI assistant

**Step 4: Paste Video Info + Transcript**
- Paste prepared input after prompt
- Wait 2-5 minutes for AI processing

**Step 5: Save Output**
- Copy generated markdown
- Save as `02_TRANSCRIPTIONS/Video_XXX.md`
- Verify 37+ entities extracted

#### Quality Requirements

**Minimum Standards:**
- ✅ 37+ entities extracted (CRITICAL)
- ✅ All 7 entity categories present
- ✅ Actions across all 7 categories (A-G)
- ✅ Integration patterns documented
- ✅ Full transcript included
- ✅ Metadata section complete

**Typical Results:**
- Entity count: 40-60 entities
- Processing time: 1-2 hours
- Success rate: 95%+

#### Example Output Structure

```markdown
# Video_024: Claude API Complete Guide

## Video Metadata
- Title: Claude API Complete Guide - Build AI Apps
- URL: https://youtube.com/watch?v=dQw4w9WgXcQ
- Channel: AI Developer Academy
- Duration: 18:42
- Upload Date: 2025-11-28
- Processed Date: 2025-12-04
- Processed By: John Doe
- Video ID: VID-024

## Video Summary
This comprehensive tutorial covers the Claude API from basics to advanced...
[3-5 paragraphs]

## Pre-Categorized Entities

### WORKFLOWS (WRF-###)
1. [WRF-412] API Authentication Setup
   - Steps: [1. Create account, 2. Generate key, 3. Test connection]
   - Duration: 10 minutes
   - Complexity: Beginner

[10-15 workflows total]

### TOOLS (TOL-###)
1. [TOL-342] Claude API (Sonnet 4.5)
   - Category: AI Platform
   - Features: [200K context, streaming, function calling]
   - Pricing: $3/$15 per million tokens

[12-18 tools total]

### OBJECTS (OBJ-###)
1. [OBJ-289] API Response
   - Type: JSON Data Structure
   - Created by: TOL-342
   - Used in: WRF-413, WRF-414

[8-12 objects total]

### ACTIONS (7 Categories)

#### Category A: Interface Creation & Design
- [ACT-001] Create chat input field
- [ACT-002] Design message bubble

[3-5 actions per category]

### PROFESSIONS & SKILLS
- [PRF-012] Full Stack Developer
- [SKL-023] API Integration

### DEPARTMENTS
- [DPT-DEV] Development
- [DPT-AID] AI Department

### INTEGRATION PATTERNS
- Claude API (TOL-342) → creates → API Response (OBJ-289)
- Building Chat Interface (WRF-413) → uses → Claude API (TOL-342)

## Full Transcript
[00:00] Welcome to this complete guide...
[Complete timestamped transcript]

## Extraction Metadata
- Total Workflows: 12
- Total Tools: 15
- Total Objects: 10
- Total Actions: 45
- Total Entities: 106
- Processing Time: 1.5 hours
- Quality Check: ✅ PASSED
```

#### Tips for Success

**Maximize Entity Extraction:**
- Provide complete transcript (no truncation)
- Include video metadata for context
- Use Claude for longer videos (better context handling)
- If <37 entities, ask AI to extract more

**Common Issues:**
- "Only 25 entities extracted" → Re-run with emphasis on minimum 37
- "Transcript too long" → Use Claude (200K context) or split into segments
- "Missing categories" → Explicitly request all 7 categories

#### Version History

- **v4.1** (Current): 37+ entities minimum, 7 action categories
- **v4.0:** Added integration patterns, cross-references
- **v3.5:** Added professions and skills
- **v3.0:** Initial structured format

---

### PMT-007: Objects Library Extraction

**Phase:** 2 (Extraction)
**Location:** `PROMPTS/PMT-007_Objects_Library_Extraction.md`
**Processing Time:** 30-45 minutes
**Automation Level:** 50% (AI-assisted)

#### Purpose

Perform deep entity extraction with focus on objects and their relationships. Expands entity count from Phase 1 (typically 37 → 60-70 entities) and creates comprehensive cross-reference mapping.

#### Input Requirements

**Required:**
- Video_XXX.md from Phase 1
- Access to video for reference (optional but helpful)

#### Output Format

Generates two files:

1. **Video_XXX_Phase3_Analysis.md:**
   - Entity expansion summary
   - Complete entity breakdown
   - Detailed analysis of each entity
   - Cross-reference matrix

2. **Video_XXX_Phase4_Objects.md:**
   - Complete objects inventory
   - Object properties and structure
   - Object relationships
   - Object lifecycle flows

#### How to Use

**Step 1: Open AI Assistant**
- Continue from Phase 1 session if possible
- Or start new session with Claude/ChatGPT

**Step 2: Provide Context**
```
I have completed Phase 1 transcription of Video_024.
Now I need Phase 2 deep extraction using PMT-007.

Here is the Video_024.md file:
[Paste entire Video_024.md content]
```

**Step 3: Load PMT-007 Prompt**
- Copy entire PMT-007 prompt
- Paste into AI assistant
- AI will perform deep analysis

**Step 4: Save Outputs**
- Save Phase3_Analysis.md → `03_ANALYSIS/Extractions/`
- Save Phase4_Objects.md → `03_ANALYSIS/Extractions/`

#### What It Extracts

**Entity Expansion:**
- Discovers entities missed in Phase 1
- Expands entity properties
- Adds detailed descriptions
- Typical increase: 20-30 entities

**Object Deep Dive:**
- Every object analyzed in detail
- Properties and structure documented
- Creation tools identified
- Usage workflows mapped
- Lifecycle documented (creation → usage → deletion)

**Cross-Reference Mapping:**
- Tool → Object links
- Object → Workflow links
- Workflow → Tool chains
- Profession → Skill connections
- **All bidirectional**

#### Example Output Sections

**Phase3_Analysis.md:**
```markdown
# Video_024 - Phase 3 Deep Analysis

## Entity Expansion Summary
- Original entities (Phase 1): 106
- Expanded entities (Phase 2): 127
- New discoveries: 21
- Enhanced entities: 68

## Workflows (15 total)
[WRF-412] API Authentication Setup
  - Detailed steps: [8 steps with substeps]
  - Prerequisites: [Email, Payment method]
  - Duration: 10 minutes
  - Tools: [TOL-342, TOL-089, TOL-158]
  - Creates: [OBJ-295, OBJ-289]
  - Requires: [SKL-023, SKL-034]
```

**Phase4_Objects.md:**
```markdown
# Video_024 - Phase 4 Objects Focus

## Objects Inventory (22 total)

### [OBJ-289] API Response
- Type: JSON Data Structure
- Structure: {detailed JSON schema}
- Created by: TOL-342 (Claude API)
- Used in: WRF-413, WRF-414
- Properties: {size, encoding, format}
- Lifecycle: Request → Process → Response → Display
```

#### Quality Checks

**Verify:**
- [ ] Entity count increased from Phase 1
- [ ] All objects have detailed properties
- [ ] Cross-references are bidirectional
- [ ] No orphaned entities
- [ ] Both files generated and saved

---

### PMT-009 Part 1: Gap Analysis

**Phase:** 3 (Gap Analysis)
**Location:** `PROMPTS/PMT-009_Taxonomy_Integration_Part1.md`
**Processing Time:** 20-30 minutes manual, 2-3 min automated
**Automation Level:** 95% (script: video_gap_analyzer.py)

#### Purpose

Compare extracted entities against existing LIBRARIES to identify what's NEW (needs creation), EXISTING (already documented), or UPDATE (needs enhancement). Calculate coverage improvement metrics.

#### Input Requirements

**Required:**
- Video_XXX.md (Phase 1 output)
- Phase3_Analysis.md (Phase 2 output)
- Access to ENTITIES/LIBRARIES/ folder

**Optional:**
- Phase4_Objects.md for additional context

#### Output Format

Generates `Video_XXX_Gap_Analysis.md` containing:

1. **Executive Summary:**
   - Coverage metrics (before/after)
   - Entity breakdown (NEW/EXISTING/UPDATE)
   - Business value assessment

2. **NEW Entities (detailed list):**
   - Each NEW entity with priority
   - Action required (create JSON)
   - Business justification

3. **EXISTING Entities (list):**
   - Entities already in LIBRARIES
   - No action needed

4. **UPDATE Entities (list):**
   - Entities needing enhancement
   - What updates needed

5. **Coverage Analysis:**
   - By category breakdown
   - Improvement percentages

6. **Recommendations:**
   - Integration priority
   - Follow-up research topics

#### How to Use

**Automated Method (Recommended):**
```bash
python scripts/video_gap_analyzer.py Video_024
```

**Manual Method:**
1. Load PMT-009 Part 1 prompt
2. Provide Video_XXX.md + extraction files
3. Provide sample LIBRARIES structure
4. AI categorizes all entities
5. Save Gap_Analysis.md

#### Example Output

```markdown
# Video_024 - Gap Analysis Report

## Executive Summary
- Before Video: 51% coverage
- After Video: 96% coverage
- Improvement: +45%

## Entity Breakdown
- NEW: 28 (need JSON creation)
- EXISTING: 94 (already in libraries)
- UPDATE: 5 (need enhancement)

## NEW Entities (28 total)

### Tools (12 NEW)
1. [TOL-342] Claude API (Sonnet 4.5)
   - Status: NEW - Not in LIBRARIES/TOOLS/
   - Priority: HIGH
   - Action: Create TOL-342.json

[Full list of 28 NEW entities]

## Coverage Analysis
| Category | Before | After | Improvement |
|----------|--------|-------|-------------|
| Tools    | 45%    | 95%   | +50%        |
| Workflows| 38%    | 92%   | +54%        |
```

---

### PMT-009 Part 2: JSON Creation

**Phase:** 4 (Integration)
**Location:** `PROMPTS/PMT-009_Taxonomy_Integration_Part2.md`
**Processing Time:** 45-60 minutes
**Automation Level:** 40% (semi-automated: video_json_updater.py)

#### Purpose

Create JSON files for all NEW entities identified in gap analysis. Provides complete JSON templates for all 7 entity types with proper structure, cross-references, and metadata.

#### Input Requirements

**Required:**
- Gap_Analysis.md identifying NEW entities
- Extraction files for entity details
- JSON templates (provided in prompt)

#### Output Format

Creates JSON files in LIBRARIES/:
- LIBRARIES/TOOLS/TOL-XXX.json
- LIBRARIES/WORKFLOWS/WRF-XXX.json
- LIBRARIES/OBJECTS/OBJ-XXX.json
- LIBRARIES/ACTIONS/ACT-XXX.json
- LIBRARIES/SKILLS/SKL-XXX.json
- LIBRARIES/PROFESSIONS/PRF-XXX.json

#### How to Use

**Semi-Automated (Recommended):**
```bash
python scripts/video_json_updater.py Video_024 --auto
```

**Manual with AI:**
1. Load PMT-009 Part 2
2. For each NEW entity, request JSON generation
3. AI generates complete JSON structure
4. Save to appropriate LIBRARIES/ subfolder
5. Validate JSON syntax

#### JSON Templates Provided

The prompt includes complete templates for:
- Tool Template (full structure)
- Workflow Template (with steps)
- Object Template (with properties)
- Action Template (with category)
- Profession Template (with requirements)
- Skill Template (with levels)
- Department Template (with code)

#### Quality Requirements

**Each JSON file must have:**
- Valid JSON syntax
- entity_id matching filename
- All required fields filled
- At least 2 cross-references
- Complete metadata section
- No placeholder text

---

### PMT-009 Part 3: Library Mapping

**Phase:** 5 (Mapping)
**Location:** `PROMPTS/PMT-009_Taxonomy_Integration_Part3.md`
**Processing Time:** 30-45 minutes manual, 2-3 min automated
**Automation Level:** 95% (script: video_integration_reporter.py)

#### Purpose

Generate comprehensive integration report documenting the complete video processing journey, coverage improvements, business value, and quality metrics.

#### Input Requirements

**Required:**
- All Phase 1-4 outputs
- List of created JSON files
- Integration_Log.csv

#### Output Format

Generates `Video_XXX_Library_Mapping_Report.md` containing:

1. Executive Summary
2. Coverage Metrics
3. Library Locations (all files created/updated)
4. Business Value Analysis
5. Cross-Reference Map
6. Quality Metrics
7. Recommendations
8. Processing Summary

#### How to Use

**Automated (Recommended):**
```bash
python scripts/video_integration_reporter.py Video_024 --include-cross-refs
```

**Manual with AI:**
1. Load PMT-009 Part 3
2. Provide all Phase 1-4 outputs
3. Provide integration log
4. AI generates comprehensive report
5. Save Library_Mapping_Report.md

#### Report Sections

**Comprehensive documentation including:**
- Which files created (28 NEW)
- Which files updated (5 existing)
- Coverage improvement (+45%)
- Departments benefited (3)
- Professions enabled (5)
- Business impact analysis
- Quality validation (100% pass rate)
- Follow-up recommendations

---

## Research Prompts

These prompts are used for discovering videos in Phase 0 (Search).

---

### PMT-048: YouTube AI Tools Daily

**Purpose:** Daily search for new AI tool videos
**Location:** `PROMPTS/PMT-048_YouTube_AI_Tools_Daily.md`
**Frequency:** Daily
**Expected Output:** 10-15 video URLs

#### What It Searches

**Focus Areas:**
- New AI tools released
- AI tool updates and features
- Tool comparisons
- Getting started tutorials
- Advanced techniques

**Target Platforms:**
- Claude, ChatGPT, Gemini
- Midjourney, Stable Diffusion
- Runway, Pika, Sora
- Code AI tools (GitHub Copilot, Cursor)
- Design AI tools (Figma AI, Adobe Firefly)

#### Search Strategy

**Query Template:**
```
Find YouTube videos from the last 30 days about:
- New AI tool launches
- AI tool feature updates
- Step-by-step AI tool tutorials
- AI tool comparisons and reviews

Requirements:
- Videos 10-25 minutes long
- Channels with 10K+ subscribers
- High production quality
- Tutorial format (not just news)
- English language
```

#### How to Use

**Step 1: Run Daily Search**
- Use Perplexity AI or ChatGPT with browsing
- Use PMT-048 query template
- Get 10-15 video results

**Step 2: Filter Results**
- Verify video quality (watch first 2 min)
- Check transcript availability
- Confirm tutorial format

**Step 3: Add to Queue**
```bash
# Add discovered videos to queue
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py "URL" "Your Name" "AI Tools" "Daily Search"
```

#### Expected Results

**Daily yield:**
- 10-15 quality videos
- 5-8 immediately useful
- 2-3 high priority (score 80+)
- 1-2 critical (process immediately)

---

### PMT-089: YouTube AI Tutorials Research

**Purpose:** Weekly search for comprehensive AI tutorials
**Location:** `PROMPTS/PMT-089_YouTube_AI_Tutorials_Research.md`
**Frequency:** Weekly
**Expected Output:** 15-20 tutorial videos

#### What It Searches

**Focus Areas:**
- Complete beginner-to-advanced tutorials
- Step-by-step walkthroughs
- Project-based learning content
- Workflow demonstrations
- Best practices and tips

**Topics Covered:**
- AI API integrations
- Prompt engineering
- AI workflow automation
- AI for specific use cases (design, coding, writing)

#### Search Strategy

**Query Template:**
```
Find comprehensive YouTube tutorial series from the last 60 days:
- Complete guides (20-40 minutes)
- Step-by-step walkthroughs
- Project-based tutorials
- Beginner to intermediate level
- Clear explanations and demonstrations

Focus on:
- Claude API tutorials
- ChatGPT advanced usage
- AI automation workflows
- AI integration examples
```

#### Expected Results

**Weekly yield:**
- 15-20 tutorial videos
- 8-10 immediately useful
- 3-5 high priority
- Mix of beginner and intermediate content

---

### PMT-093: Design AI Video Discovery

**Purpose:** Weekly search for AI design tool videos
**Location:** `PROMPTS/PMT-093_Design_AI_Video_Discovery.md`
**Frequency:** Weekly
**Expected Output:** 10-15 design-focused videos

#### What It Searches

**Focus Areas:**
- Figma AI plugins and features
- Midjourney techniques
- Adobe Firefly workflows
- Design automation
- AI-assisted design processes
- UI/UX generation tools

**Target Audience:**
- UI/UX Designers
- Graphic Designers
- Product Designers
- Design Teams

#### Search Strategy

**Query Template:**
```
Find YouTube videos about AI design tools from the last 60 days:
- Figma AI plugins tutorials
- Midjourney design workflows
- AI for UI/UX design
- Design automation examples
- AI-generated assets

Requirements:
- Design-focused content
- Practical examples shown
- 15-30 minutes long
- Designer-created content preferred
```

#### Expected Results

**Weekly yield:**
- 10-15 design videos
- 5-7 Figma-related
- 3-4 Midjourney/image AI
- 2-3 design automation
- High relevance for design team

---

### PMT-098: OpenAI Automation Examples

**Purpose:** Weekly search for AI automation videos
**Location:** `PROMPTS/PMT-098_OpenAI_Automation_Examples.md`
**Frequency:** Weekly
**Expected Output:** 10-15 automation videos

#### What It Searches

**Focus Areas:**
- API automation workflows
- Make.com/Zapier AI integrations
- Custom AI automation scripts
- Workflow optimization
- Business process automation

**Use Cases:**
- Customer support automation
- Content generation pipelines
- Data processing automation
- Report generation
- Email automation

#### Expected Results

**Weekly yield:**
- 10-15 automation videos
- 5-8 practical workflows
- 3-4 advanced integrations
- 2-3 business use cases

---

## Department-Specific Prompts

These prompts focus research on specific department needs (PMT-044 through PMT-052).

---

### PMT-044: HR Department Research

**Focus:** HR tools, recruitment, onboarding, performance management
**Frequency:** Monthly
**Output:** 10-12 HR-focused videos

**Topics:**
- AI recruitment tools
- Candidate screening automation
- Onboarding workflows
- Performance review tools
- HR analytics

---

### PMT-045: Sales Department Research

**Focus:** CRM, sales automation, outreach tools
**Frequency:** Monthly
**Output:** 10-12 sales-focused videos

**Topics:**
- AI-powered CRM tools
- Sales email automation
- Lead generation
- Proposal generation
- Sales analytics

---

### PMT-046: SMM Department Research

**Focus:** Social media management, content scheduling, analytics
**Frequency:** Monthly
**Output:** 10-12 social media videos

**Topics:**
- Social media scheduling tools
- Content generation for social
- Analytics and reporting
- Community management
- Influencer research

---

### PMT-047: Design Department Research

**Focus:** Design tools, workflows, collaboration
**Frequency:** Weekly (high priority)
**Output:** 15-20 design videos

**Topics:**
- Design tools and plugins
- Design systems
- Prototyping tools
- Collaboration workflows
- Design handoff

---

### PMT-048: Development Department Research

**Focus:** Coding tools, APIs, frameworks
**Frequency:** Weekly (high priority)
**Output:** 15-20 development videos

**Topics:**
- AI coding assistants
- API integration tutorials
- Framework guides
- Development workflows
- Testing and deployment

---

### PMT-049: Marketing Department Research

**Focus:** Marketing automation, analytics, campaigns
**Frequency:** Monthly
**Output:** 10-12 marketing videos

**Topics:**
- Marketing automation platforms
- Email campaign tools
- SEO and content tools
- Analytics and reporting
- Campaign management

---

### PMT-050: Operations Department Research

**Focus:** Process automation, project management, operations tools
**Frequency:** Monthly
**Output:** 10-12 operations videos

**Topics:**
- Project management tools
- Process automation
- Resource planning
- Workflow optimization
- Operations analytics

---

### PMT-051: Finance Department Research

**Focus:** Financial tools, reporting, budgeting
**Frequency:** Quarterly
**Output:** 8-10 finance videos

**Topics:**
- Accounting automation
- Financial reporting tools
- Budgeting and forecasting
- Invoice management
- Expense tracking

---

### PMT-052: Legal Department Research

**Focus:** Legal tools, contract management, compliance
**Frequency:** Quarterly
**Output:** 8-10 legal videos

**Topics:**
- Contract management systems
- Legal research tools
- Compliance automation
- Document generation
- E-signature platforms

---

## How to Use Prompts

### General Workflow

**Step 1: Select Appropriate Prompt**
- Phase 1 → Use PMT-004
- Phase 2 → Use PMT-007
- Phase 3 → Use PMT-009 Part 1 (or script)
- Phase 4 → Use PMT-009 Part 2 (or script)
- Phase 5 → Use PMT-009 Part 3 (or script)
- Search → Use PMT-048, 089, 093, 098, or department-specific

**Step 2: Locate Prompt File**
```
PROMPTS/[prompt-name].md
OR
ENTITIES/PROMPTS/[prompt-name].md
```

**Step 3: Open in Text Editor**
- Read entire prompt
- Understand input requirements
- Note output expectations

**Step 4: Prepare Input Data**
- Gather required information
- Format according to prompt instructions
- Verify completeness

**Step 5: Execute with AI**
- Open AI assistant (Claude/ChatGPT/Gemini)
- Copy entire prompt
- Paste prompt + your input data
- Wait for AI processing

**Step 6: Save Output**
- Copy AI-generated content
- Save to appropriate location
- Verify quality and completeness

**Step 7: Update Tracking**
- Update progress tracker
- Log in appropriate CSV
- Mark phase complete

### Best Practices

**Prompt Selection:**
- Use correct prompt for each phase
- Don't skip prompts in workflow
- Follow prompts in order (PMT-004 → PMT-007 → PMT-009)

**Input Preparation:**
- Provide complete information
- Format correctly (timestamps, structure)
- Include all required fields

**AI Selection:**
- **Claude:** Best for long transcripts (200K context)
- **ChatGPT:** Good for standard videos (128K context)
- **Gemini:** Experimental, 1M context but less reliable

**Quality Verification:**
- Check output meets requirements
- Verify minimum standards (37+ entities for PMT-004)
- Validate all sections present

**Output Handling:**
- Save immediately (don't lose work)
- Use correct naming convention
- Store in correct folder

---

## Prompt Best Practices

### For Video Processing

**Phase 1 (PMT-004):**
- Provide complete transcript (no truncation)
- Include all video metadata
- Use Claude for videos >15 minutes
- Verify 37+ entities extracted
- Check all 7 categories present

**Phase 2 (PMT-007):**
- Continue same AI session if possible
- Provide Video_XXX.md from Phase 1
- Expect 20-30 additional entities
- Focus on object relationships
- Validate bidirectional links

**Phase 3 (PMT-009 Part 1):**
- Use automated script when possible
- Provide access to LIBRARIES folder
- Verify categorization (NEW/EXISTING/UPDATE)
- Check coverage calculations
- Review priorities assigned

**Phase 4 (PMT-009 Part 2):**
- Use templates provided in prompt
- Create one entity at a time (or use script)
- Validate JSON syntax immediately
- Check cross-references
- Verify metadata complete

**Phase 5 (PMT-009 Part 3):**
- Use automated script when possible
- Provide all previous outputs
- Verify report completeness
- Check all sections present
- Review recommendations

### For Research

**Search Prompts (PMT-048, 089, 093, 098):**
- Run on schedule (daily/weekly)
- Use Perplexity AI or ChatGPT with browsing
- Verify video quality before adding
- Check transcript availability
- Filter for tutorial format

**Department Prompts (PMT-044 through PMT-052):**
- Run monthly or quarterly
- Focus on department-specific needs
- Consult with department leads
- Prioritize high-impact topics
- Balance breadth and depth

### Quality Assurance

**Before Finalizing:**
- [ ] All required sections present
- [ ] Minimum standards met
- [ ] No placeholder text (TBD, etc.)
- [ ] Proper formatting
- [ ] Saved in correct location
- [ ] Progress tracker updated

**Common Issues:**
- "Output incomplete" → Re-run with same input
- "Below minimum entities" → Ask AI to extract more
- "Missing categories" → Explicitly request them
- "JSON invalid" → Validate with json.tool

### Efficiency Tips

**Save Time:**
- Reuse AI sessions (maintain context)
- Use automated scripts for Phases 3-5
- Batch similar prompts
- Keep prompt files easily accessible

**Improve Quality:**
- Review examples in LIBRARIES
- Study successful outputs
- Learn from errors
- Iterate on process

**Scale Up:**
- Process multiple videos in parallel
- Assign phases to different team members
- Use automation wherever possible
- Document learnings

---

## Summary

**Total Prompts:** 50+ prompts documented

**Core Processing:** 5 prompts (PMT-004, 007, 009 Parts 1-3)
**Research:** 4 main prompts (PMT-048, 089, 093, 098)
**Department-Specific:** 9 prompts (PMT-044 through PMT-052)
**Specialized:** 30+ additional prompts

**Key Takeaways:**
- PMT-004 is most critical (Phase 1)
- PMT-009 Parts 1-3 can be automated
- Research prompts run on schedule
- Department prompts focus specialized needs

**Success Metrics:**
- 37+ entities per video (PMT-004)
- 95%+ automation (Phases 3, 5)
- 100% JSON validation
- 90%+ coverage improvement

**Next Steps:**
- Review prompt files in PROMPTS/ folder
- Practice with PMT-004 on first video
- Use automation scripts for Phases 3-5
- Follow workflow guide: [01_STEP_BY_STEP_WORKFLOWS.md](./01_STEP_BY_STEP_WORKFLOWS.md)

---

*End of Prompts Reference Guide*
*For detailed workflow, see [01_STEP_BY_STEP_WORKFLOWS.md](./01_STEP_BY_STEP_WORKFLOWS.md)*
*For prompt files, see PROMPTS/ folder*
