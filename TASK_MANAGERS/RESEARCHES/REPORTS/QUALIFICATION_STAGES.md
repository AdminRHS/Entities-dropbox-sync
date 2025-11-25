# Video Processing Qualification Stages

**Created:** 2025-11-22
**Location:** `TASK_MANAGERS/RESEARCHES/`
**Purpose:** Define qualification criteria for each processing phase, user input variation tracking, and quality thresholds
**Status:** Active

---

## Overview

This document establishes clear criteria for qualifying videos for each phase of processing (Phases 1-7), tracks different user input approaches and prompt variations, and defines quality thresholds to ensure consistent, high-value taxonomy integration.

---

## Table of Contents

1. [Phase Qualification Criteria](#phase-qualification-criteria)
2. [User Input Variation Tracking](#user-input-variation-tracking)
3. [Quality Thresholds](#quality-thresholds)
4. [Decision Trees](#decision-trees)
5. [Best Practices](#best-practices)

---

## Phase Qualification Criteria

### Phase 1: Transcription Readiness

**What qualifies a video for Phase 1:**

✅ **READY FOR TRANSCRIPTION if:**
- Video URL is accessible and valid
- Video duration is between 5-60 minutes (optimal)
- Audio quality is clear and understandable
- Content is relevant to business operations, AI, automation, or tools
- Creator/channel is identifiable
- Video is publicly available

❌ **NOT READY if:**
- Video is private or restricted
- Audio quality is poor (excessive background noise, unclear speech)
- Content is off-topic (entertainment, personal vlogs, etc.)
- Video duration is too short (<5 min) or too long (>90 min)
- Technical issues prevent playback

**Prerequisites:**
- None (Phase 1 is the entry point)

**Success Criteria:**
- Complete word-for-word transcription with timestamps
- Metadata section populated (title, creator, duration, date)
- Description section with key topics identified
- Embedded taxonomy (if using v3.0+ prompts)
- Action verb categorization (7 categories)
- Tools matrix created
- File size: typically 20-100KB depending on video length

**Output Files:**
- `Video_XXX.md` in `02_TRANSCRIPTIONS/` folder

**Estimated Time:** 15-25 minutes (with v3.2+ automation)

---

### Phase 2: Naming Readiness (Optional)

**What qualifies a video for Phase 2:**

✅ **NEEDS PROFESSIONAL NAMING if:**
- Original title is clickbait or casual ("This AI is INSANE!!!")
- Title contains excessive capitalization or emojis
- Multiple videos on same topic need differentiation
- Corporate documentation requires professional titles
- Title doesn't clearly describe content

✅ **SKIP PHASE 2 if:**
- Original title is already professional and descriptive
- Title clearly indicates content and value
- No business documentation needs

**Prerequisites:**
- Phase 1 complete (transcription exists)

**Success Criteria:**
- Professional, descriptive title generated
- Title accurately reflects video content
- Title follows naming convention (50-80 characters recommended)
- Alternative titles provided (3-5 options)

**Output:**
- Updated video title in VIDEOS_INDEX.md
- Professional naming documented

**Estimated Time:** 5-10 minutes

---

### Phase 3: Initial Analysis Readiness

**What qualifies a video for Phase 3:**

✅ **READY FOR ANALYSIS if:**
- Phase 1 complete (transcription exists)
- Video contains actionable workflows or tutorials
- Tools are mentioned or demonstrated
- Clear business processes are described
- Technical depth is sufficient for taxonomy extraction

❌ **NOT READY if:**
- Video is purely opinion/commentary with no workflows
- No tools or processes mentioned
- Content is too abstract or theoretical
- Transcription quality is poor

**Prerequisites:**
- Phase 1 complete
- Transcription quality verified (90%+ accuracy)

**Success Criteria:**
- Workflows extracted with structured format (OBJECTIVE, STEPS, TOOLS, etc.)
- Tools identified and categorized
- Action verbs cataloged across 7 categories:
  - A. CREATION & GENERATION
  - B. ANALYSIS & PROCESSING
  - C. MANAGEMENT & ORGANIZATION
  - D. COMMUNICATION & COLLABORATION
  - E. TRANSFORMATION & OPTIMIZATION
  - F. BROWSER/AGENTIC OPERATIONS (v3.0+)
  - G. DATA OPERATIONS (v3.1+)
- Integration patterns documented
- Processes identified

**Output Files:**
- Structured analysis embedded in `Video_XXX.md` OR
- Separate `Video_XXX_Analysis.md` file

**Estimated Time:** 30-45 minutes

---

### Phase 4: Objects Extraction Readiness

**What qualifies a video for Phase 4:**

✅ **READY FOR OBJECTS EXTRACTION if:**
- Phase 3 complete (initial analysis done)
- Video demonstrates creation of deliverables
- Clear inputs and outputs identified
- Tools produce tangible objects (documents, images, videos, data, etc.)

✅ **SKIP PHASE 4 if:**
- Video is purely conceptual with no deliverables
- No objects/outputs are created in workflows

**Prerequisites:**
- Phase 3 complete
- At least 3 workflows identified
- Tools matrix populated

**Success Criteria:**
- Objects categorized by type:
  - Design objects (mockups, prototypes, wireframes)
  - Media objects (videos, images, audio files)
  - Document objects (reports, specs, presentations)
  - Data objects (datasets, databases, spreadsheets)
  - Communication objects (emails, messages, notifications)
  - Code objects (scripts, applications, APIs)
- Bidirectional cross-references created:
  - Object → Tool (what creates it)
  - Object → Action (what verb describes its creation)
  - Tool → Object (what it produces)
- Input/Output relationships mapped

**Output Files:**
- Object inventory in analysis document OR
- Separate `Video_XXX_Objects.md` file

**Estimated Time:** 20-30 minutes

---

### Phase 5: Gap Analysis Readiness

**What qualifies a video for Phase 5:**

✅ **READY FOR GAP ANALYSIS if:**
- Phases 1-4 complete
- At least 5 tools identified OR 3 workflows documented
- Business value is High or Very High
- Clear department alignment exists
- Tools/workflows are NOT already fully documented in LIBRARIES
- Video adds significant new coverage to taxonomy

❌ **NOT READY if:**
- Fewer than 3 tools and 2 workflows identified
- All content already covered in LIBRARIES (>95% overlap)
- Business value is Low
- No clear integration path

**Prerequisites:**
- Phases 1-4 complete
- Quality score of 70%+ from Phase 3
- Department relevance identified

**Success Criteria:**
- Inventory of existing LIBRARIES entities reviewed
- New elements identified and categorized:
  - New tools (not in Tools.json)
  - New actions (not in Actions_Master.json)
  - New objects (not in Objects.json)
  - New workflows (not documented)
  - New integration patterns
- Updates to existing elements identified
- Coverage improvement percentage calculated
- Gap report structured with:
  - Executive summary
  - Existing coverage analysis
  - New elements list
  - Update recommendations
  - Coverage improvement metrics

**Output Files:**
- `Video_XXX_Gap_Analysis.md` in `03_ANALYSIS/Gap_Analysis/` folder

**Estimated Time:** 30-45 minutes

**Decision Point:**
- If gap analysis shows <10% new coverage → Consider archiving (low value)
- If gap analysis shows 10-30% new coverage → Proceed with caution
- If gap analysis shows >30% new coverage → High priority for Phase 6

---

### Phase 6: Taxonomy Updates Readiness

**What qualifies a video for Phase 6:**

✅ **READY FOR TAXONOMY UPDATES if:**
- Phase 5 complete (gap analysis exists)
- New coverage is >10%
- Gap analysis approved by stakeholder
- Integration path is clear
- No blockers exist (missing entity files, unclear categories, etc.)

❌ **SKIP PHASE 6 if:**
- Gap analysis shows <10% new coverage
- All elements already exist in LIBRARIES
- Video content is outdated or deprecated

**Prerequisites:**
- Phase 5 complete and approved
- Access to LIBRARIES entity files:
  - Tools.json (or equivalent)
  - Actions_Master.json
  - Objects.json
  - Processes.json
  - Skills.json
- Cross-reference files accessible

**Success Criteria:**
- New tools created with complete metadata:
  - Tool ID (TOOL-{CATEGORY}-###)
  - Name, description, category
  - Use cases, integration patterns
  - Related actions, objects, workflows
- New actions added to Actions_Master.json
- New objects created with cross-references
- New workflows documented
- Skills created (if applicable)
- Cross-references updated bidirectionally:
  - Tools ↔ Actions
  - Tools ↔ Objects
  - Tools ↔ Workflows
  - Actions ↔ Objects
- Version control maintained (backup before updates)

**Output Files:**
- Updated entity files in LIBRARIES
- Cross-reference updates documented
- `Video_XXX_Updates_Log.md` (optional)

**Estimated Time:** 45-60 minutes

---

### Phase 7: Reporting Readiness

**What qualifies a video for Phase 7:**

✅ **READY FOR REPORTING if:**
- Phase 6 complete (taxonomy updates made)
- All integration work finished
- Cross-references validated
- Quality assurance passed

**Prerequisites:**
- Phase 6 complete
- All entity files updated and saved
- Cross-references verified

**Success Criteria:**
- Library Mapping Report created with:
  - **Executive Summary**
    - Video overview
    - Processing dates
    - Key findings
  - **Extraction Results**
    - Tools created (count + list)
    - Workflows documented (count + list)
    - Objects identified (count + list)
    - Actions cataloged (count + list)
  - **Coverage Improvement Metrics**
    - Percentage increase in coverage
    - New categories added
    - Gaps filled
  - **Cross-Reference Map**
    - Visual or structured map of relationships
    - Entity connection diagram
  - **Integration Impact**
    - Department relevance
    - Business value assessment
    - Use cases enabled
  - **Next Steps/Recommendations**
    - Follow-up work needed
    - Related videos to process
    - Additional research suggested

**Output Files:**
- `Video_XXX_Library_Mapping_Report.md` in `03_ANALYSIS/Library_Mapping/` folder

**Estimated Time:** 20-30 minutes

---

## User Input Variation Tracking

### Purpose

Track different approaches, prompt versions, and processing methodologies to:
1. Understand which methods produce best results
2. Maintain consistency across video processing
3. Identify areas for prompt improvement
4. Document lessons learned for future processing

---

### Prompt Version History

#### v2.0 (Deprecated - November 2025)

**Used for:** Videos 001, 002, 003, 004, 005

**Characteristics:**
- JSON output format
- Basic workflow extraction
- 5 action verb categories (A-E)
- No embedded taxonomy
- Separate analysis files required

**Limitations:**
- JSON format difficult to read/edit
- Manual conversion to markdown needed
- Limited action verb coverage
- No browser/agentic operations category
- No data operations category

**Migration Path:**
- Convert JSON to v3.1 markdown format
- Add F. BROWSER/AGENTIC and G. DATA OPERATIONS categories
- Enhance cross-references

**Example Videos:**
- Video_001: GLIF Creative Workflows
- Video_002: GLIF + Gemini RAG
- Video_005: Agentic Engineering Tech Stack

---

#### v3.0 (Browser/Agentic Enhancement - November 2025)

**Used for:** Videos 007, 008

**Characteristics:**
- Markdown-only output
- Added **F. BROWSER/AGENTIC OPERATIONS** category
- Improved workflow structure
- Enhanced action verb categorization
- Embedded taxonomy option

**Enhancements over v2.0:**
- New action category: Takes over, Controls, Opens, Clicks, Navigates, Fills in, Submits, etc.
- Better handling of browser automation workflows
- Agentic AI pattern recognition
- Cleaner markdown format

**Informed by:** Video_004 (Perplexity Comet) analysis revealing browser control patterns

**Example Videos:**
- Video_007: Claude Code for Business (partial)
- Video_008: Claude MCP Connector Automation

**When to use:**
- Videos featuring browser automation
- Agentic AI workflows
- Tool-use patterns
- Multi-step autonomous processes

---

#### v3.1 (Data Operations Enhancement - November 2025)

**Used for:** Videos 006 (converted), 010 (JSON format)

**Characteristics:**
- Markdown preferred format
- Added **G. DATA OPERATIONS** category
- Enhanced ETL/data pipeline documentation
- Improved scraping/enrichment workflow extraction

**Enhancements over v3.0:**
- New action category: Scrape, Parse, Enrich, Validate, Deduplicate, Pump into, Dump into, Arbitrage, Extract patterns, etc.
- Better handling of lead generation workflows
- Data pipeline pattern recognition
- Web scraping workflow documentation

**Informed by:** Video_006 (Lead Generation Methods) revealing data operations patterns

**Example Videos:**
- Video_006: Lead Generation & Web Scraping (converted from JSON)
- Video_010: NotebookLM CV Screening (JSON format)

**When to use:**
- Videos featuring data pipelines
- Lead generation workflows
- Web scraping processes
- ETL operations
- Data enrichment workflows

---

#### v3.2 (Task Manager Integration - November 2025)

**Used for:** Videos 019, 021

**Characteristics:**
- Full task manager integration
- Milestones, Tasks, Steps extraction
- Enhanced department tagging
- Improved metadata structure
- Streamlined processing (90-95% time savings)

**Enhancements over v3.1:**
- Integrated taxonomy elements (Milestones, Tasks, Steps)
- Department tags (AID, LGN, SLS, DEV, etc.)
- Improved cross-referencing
- Quality score tracking
- Business value assessment

**Example Videos:**
- Video_019: Freelance & Remote Hiring Platforms
- Video_021: n8n Workflow Automation Fundamentals

**When to use:**
- All new video processing (recommended)
- Complex multi-step workflows
- Videos requiring department categorization
- High-value strategic content

**Time Savings:**
- Traditional processing: 2-4 hours per video
- v3.2 automation: 15-25 minutes per video
- Efficiency gain: 90-95%

---

#### v4.1 (Latest - Full Integration - November 2025)

**Status:** Documented in PMT-004_Video_Transcription_v4.1.md

**Characteristics:**
- Complete taxonomy integration
- All 7 action verb categories
- Full metadata structure
- Department alignment
- Priority ranking
- Quality metrics
- Research assignment tracking

**Enhancements over v3.2:**
- Priority queue integration
- Research assignment ID tracking
- Quality thresholds
- Department relevance scoring
- Comprehensive cross-referencing

**When to use:**
- All new videos (current standard)
- High-priority research videos
- Videos requiring formal research assignments
- Department-specific processing

**Recommended for:** All future video processing

---

### Processing Approach Variations

#### Embedded Taxonomy Analysis

**Used for:** Videos 003, 004, 017, 018, 020

**Approach:**
- Taxonomy elements (workflows, tools, actions) embedded directly in transcription file
- No separate analysis files created
- Faster initial processing
- Suitable for shorter videos or clear workflows

**Pros:**
- Single file to manage
- Faster processing (no separate files)
- Immediate visibility of taxonomy

**Cons:**
- Harder to update taxonomy separately
- Still requires formal Phase 5-7 for integration
- Less separation of concerns

**When to use:**
- Videos under 20 minutes
- Clear, straightforward workflows
- Quick initial extraction needed
- Low complexity content

**Example:**
```markdown
# Video_003: Kimi K2 Thinking AI Model

[Transcription...]

## TAXONOMY ANALYSIS

### WORKFLOWS
1. Analyze Healthcare Data and Create Dashboard
   - OBJECTIVE: ...
   - STEPS: ...
   - TOOLS: ...

### TOOLS MATRIX
| Tool | Category | Use Case |
|------|----------|----------|
| Kimi K2 | AI Model | Agentic reasoning |
```

---

#### Separate Analysis Files

**Used for:** Videos 001, 002, 005, 006, 008, 009, 019, 021

**Approach:**
- Dedicated files for each phase:
  - `Video_XXX_Gap_Analysis.md`
  - `Video_XXX_Library_Mapping_Report.md`
  - `Video_XXX_Extraction_Inventory.md`
- Clear separation of concerns
- Formal documentation
- Easier to update individual phases

**Pros:**
- Clear file organization
- Easier to update phases independently
- Better for complex videos
- Formal documentation trail
- Easier collaboration (multiple people can work on different phases)

**Cons:**
- More files to manage
- Slightly slower initial setup
- Requires file organization discipline

**When to use:**
- Videos over 20 minutes
- Complex workflows (5+ workflows)
- Multiple tools (10+ tools)
- High business value content
- Formal research assignments

**Example Structure:**
```
03_ANALYSIS/
├── Gap_Analysis/
│   └── Video_002_Gap_Analysis.md
├── Library_Mapping/
│   └── Video_002_Library_Mapping_Report.md
└── Extractions/
    └── Video_002_Extraction_Inventory.md
```

---

#### Hybrid Approach (Partial Completion)

**Used for:** Video_007 (6/20 workflows extracted)

**Approach:**
- Initial workflows extracted
- Remaining workflows pending
- Phased completion strategy

**Pros:**
- Captures high-value workflows immediately
- Allows incremental progress
- Can prioritize most important workflows

**Cons:**
- Incomplete processing
- Risk of never completing
- Harder to track what's remaining

**When to use:**
- Very long videos (30+ minutes)
- Time constraints
- High-value workflows identified early
- Phased research approach

**Completion Strategy:**
1. Extract top 20% of workflows (highest value)
2. Document remaining workflow count
3. Schedule dedicated session for completion
4. Update quality score as completion progresses

---

### User Input Prompt Customization

#### Standard Prompts (No Customization)

**Approach:** Use prompt exactly as documented in Video_Processing/

**When to use:**
- First-time video processing
- Standard tutorials and how-to videos
- Clear, straightforward content
- No special requirements

---

#### Customized Prompts (Department-Specific)

**Approach:** Modify prompts to emphasize specific department needs

**Examples:**

**Lead Generation Focus (Video_006):**
- Emphasize G. DATA OPERATIONS category
- Highlight scraping and enrichment workflows
- Focus on lead qualification processes
- Track conversion metrics

**AI & Automations Focus (Videos 003, 004, 005, 007, 008, 021):**
- Emphasize F. BROWSER/AGENTIC OPERATIONS
- Highlight multi-agent workflows
- Focus on integration patterns
- Track automation efficiency

**Sales Focus (Video_014):**
- Emphasize CRM workflows
- Highlight sales automation processes
- Focus on qualification and scoring
- Track sales velocity metrics

**HR Focus (Videos 010, 019):**
- Emphasize recruitment workflows
- Highlight screening and interview processes
- Focus on qualification criteria
- Track hiring efficiency

---

#### Iterative Refinement Approach

**Used for:** Prompt version evolution (v2.0 → v3.0 → v3.1 → v3.2 → v4.1)

**Process:**
1. Process video with current prompt version
2. Identify gaps or missing patterns (e.g., browser operations in Video_004)
3. Enhance prompt to capture new patterns
4. Document new category or enhancement
5. Apply to future videos
6. Optionally reprocess earlier videos with new prompt

**Example Evolution:**
- Video_004 revealed browser automation patterns → Created F. BROWSER/AGENTIC category (v3.0)
- Video_006 revealed data operations patterns → Created G. DATA OPERATIONS category (v3.1)
- Videos 019, 021 revealed task management needs → Integrated Milestones/Tasks/Steps (v3.2)

---

### Quality Assurance User Input

#### Manual Review Checkpoints

**Checkpoint 1: After Phase 1 (Transcription)**
- User validates transcription accuracy (90%+ required)
- User confirms key topics captured
- User verifies metadata (title, creator, duration)

**Checkpoint 2: After Phase 3 (Analysis)**
- User reviews extracted workflows for accuracy
- User validates tool identification
- User confirms action verb categorization

**Checkpoint 3: After Phase 5 (Gap Analysis)**
- User approves new elements for integration
- User confirms coverage improvement calculations
- User validates integration path

**Checkpoint 4: After Phase 6 (Updates)**
- User reviews updated entity files
- User validates cross-references
- User confirms quality standards met

---

#### Automated Quality Checks

**Phase 1 Checks:**
- Timestamp format validation
- Metadata completeness
- Minimum word count (typically 3000+ words for 15+ min video)
- Action verb categories populated (all 7 categories)

**Phase 3 Checks:**
- Minimum workflows (3+ workflows for standard video)
- Minimum tools (2+ tools identified)
- Workflow structure validation (OBJECTIVE, STEPS, TOOLS present)

**Phase 5 Checks:**
- Coverage improvement >10% (threshold for proceeding)
- Gap analysis sections complete (Executive Summary, New Elements, etc.)

**Phase 6 Checks:**
- Bidirectional cross-references created
- Entity IDs follow naming conventions
- No orphaned references

---

## Quality Thresholds

### Overall Quality Score Calculation

**Formula:**
```
Quality Score = (Transcription Accuracy × 0.2)
              + (Workflow Completeness × 0.3)
              + (Tool Identification × 0.2)
              + (Cross-Reference Quality × 0.15)
              + (Integration Readiness × 0.15)
```

**Component Definitions:**

1. **Transcription Accuracy (20%):**
   - 100% = Perfect transcription, no errors
   - 90% = Minor errors, key content accurate
   - 80% = Some errors, content mostly understandable
   - <80% = Significant errors, needs retranscription

2. **Workflow Completeness (30%):**
   - 100% = All workflows extracted with full structure (OBJECTIVE, STEPS, TOOLS, etc.)
   - 90% = Most workflows complete, minor gaps acceptable
   - 80% = Some workflows incomplete or missing steps
   - <80% = Significant workflow gaps

3. **Tool Identification (20%):**
   - 100% = All tools identified with metadata
   - 90% = Most tools identified, minor tools may be missing
   - 80% = Some tools missing or misidentified
   - <80% = Significant tool gaps

4. **Cross-Reference Quality (15%):**
   - 100% = All cross-references bidirectional and accurate
   - 90% = Most cross-references complete, minor gaps
   - 80% = Some cross-references missing
   - <80% = Significant cross-reference gaps

5. **Integration Readiness (15%):**
   - 100% = Ready for immediate Phase 5-7 processing
   - 90% = Ready with minor cleanup needed
   - 80% = Needs some preparation before Phase 5
   - <80% = Significant work needed before integration

---

### Phase-Specific Quality Thresholds

#### Phase 1: Transcription Quality

**Minimum Threshold:** 90% accuracy

**Evaluation Criteria:**
- [ ] Timestamps present for every segment
- [ ] Speaker identification (if multiple speakers)
- [ ] Technical terms spelled correctly
- [ ] Tool names capitalized and spelled correctly
- [ ] URLs captured accurately
- [ ] Code snippets formatted properly (if applicable)

**Quality Tiers:**
- **Excellent (95-100%):** Publish-ready, no errors
- **Good (90-94%):** Minor errors, acceptable
- **Fair (80-89%):** Needs revision
- **Poor (<80%):** Retranscription required

**User Input:** Manual spot-check of 10-15 random segments

---

#### Phase 3: Analysis Quality

**Minimum Threshold:** 80% workflow completeness

**Evaluation Criteria:**
- [ ] At least 3 workflows extracted
- [ ] Each workflow has OBJECTIVE, STEPS, TOOLS
- [ ] Action verbs categorized across 7 categories
- [ ] Tools matrix populated
- [ ] Integration patterns identified (if applicable)

**Quality Tiers:**
- **Excellent (95-100%):** All workflows complete, comprehensive extraction
- **Good (85-94%):** Most workflows complete, minor gaps
- **Fair (75-84%):** Some workflows incomplete
- **Poor (<75%):** Significant gaps, needs rework

**User Input:** Validate top 3 workflows for accuracy

---

#### Phase 5: Gap Analysis Quality

**Minimum Threshold:** 70% coverage improvement clarity

**Evaluation Criteria:**
- [ ] Existing coverage accurately assessed
- [ ] New elements clearly identified
- [ ] Coverage improvement percentage calculated
- [ ] Integration path defined
- [ ] Business value justified

**Quality Tiers:**
- **Excellent (90-100%):** Clear gap analysis, high confidence in integration
- **Good (80-89%):** Solid analysis, minor uncertainties
- **Fair (70-79%):** Basic analysis, some gaps in assessment
- **Poor (<70%):** Unclear analysis, needs rework

**Decision Thresholds:**
- **>30% new coverage:** HIGH PRIORITY - Proceed immediately
- **10-30% new coverage:** MEDIUM PRIORITY - Proceed with review
- **<10% new coverage:** LOW PRIORITY - Consider archiving

**User Input:** Stakeholder approval of gap analysis and coverage improvement

---

#### Phase 6: Integration Quality

**Minimum Threshold:** 95% cross-reference accuracy

**Evaluation Criteria:**
- [ ] All new tools have complete metadata
- [ ] Bidirectional cross-references created
- [ ] No orphaned references
- [ ] Entity IDs follow naming conventions
- [ ] Version control maintained (backup before updates)

**Quality Tiers:**
- **Excellent (98-100%):** Perfect integration, no errors
- **Good (95-97%):** Solid integration, minor cleanup needed
- **Fair (90-94%):** Integration complete but needs validation
- **Poor (<90%):** Integration errors, rework needed

**User Input:** Quality assurance review of updated entity files

---

#### Phase 7: Reporting Quality

**Minimum Threshold:** 85% report completeness

**Evaluation Criteria:**
- [ ] Executive summary clear and concise
- [ ] Extraction results quantified
- [ ] Coverage improvement metrics accurate
- [ ] Cross-reference map included
- [ ] Next steps defined

**Quality Tiers:**
- **Excellent (95-100%):** Comprehensive, publish-ready report
- **Good (85-94%):** Solid report, minor sections could be enhanced
- **Fair (75-84%):** Basic report, needs enhancement
- **Poor (<75%):** Incomplete report, needs rework

**User Input:** Stakeholder review and approval

---

### Business Value Thresholds

#### Business Value Assessment Criteria

**Very High Value:**
- Strategic department alignment (Lead Gen, Sales, AI & Automations)
- 10+ tools or 5+ workflows identified
- Addresses current business priority
- Enables new capabilities
- Coverage improvement >30%
- Clear ROI potential

**High Value:**
- Relevant department alignment
- 5-10 tools or 3-5 workflows identified
- Supports business operations
- Enhances existing capabilities
- Coverage improvement 15-30%
- Good value proposition

**Medium Value:**
- General relevance
- 2-5 tools or 2-3 workflows identified
- Useful but not critical
- Coverage improvement 10-15%
- Moderate value

**Low Value:**
- Limited relevance
- <2 tools or <2 workflows
- Nice to have
- Coverage improvement <10%
- Low priority

---

### Department Alignment Thresholds

**Primary Alignment (Direct Impact):**
- Video directly addresses department's core functions
- Tools and workflows immediately applicable
- High adoption likelihood
- Clear use cases identified

**Secondary Alignment (Indirect Impact):**
- Video relates to department but not core focus
- Tools and workflows potentially applicable
- Moderate adoption likelihood
- Some use cases identified

**Tertiary Alignment (Tangential Impact):**
- Video tangentially related to department
- Tools and workflows may have limited applicability
- Low adoption likelihood
- Few use cases identified

---

## Decision Trees

### Should I Process This Video?

```
START
  ↓
Is video URL accessible? → NO → STOP (Cannot process)
  ↓ YES
Is video 5-60 minutes long? → NO → REVIEW (Too short/long)
  ↓ YES
Is content business-relevant? → NO → ARCHIVE (Off-topic)
  ↓ YES
Is audio quality clear? → NO → STOP (Poor quality)
  ↓ YES
Are tools/workflows demonstrated? → NO → ARCHIVE (No actionable content)
  ↓ YES
PROCEED TO PHASE 1 (Transcription)
```

---

### Should I Continue to Phase 5?

```
START (After Phase 4)
  ↓
Quality Score ≥ 70%? → NO → REWORK PHASE 3-4
  ↓ YES
Tools identified ≥ 3? → NO → REVIEW (Low tool count)
  ↓ YES
Workflows identified ≥ 2? → NO → REVIEW (Low workflow count)
  ↓ YES
Business Value ≥ Medium? → NO → ARCHIVE (Low value)
  ↓ YES
Department alignment clear? → NO → REVIEW (Unclear fit)
  ↓ YES
PROCEED TO PHASE 5 (Gap Analysis)
```

---

### Should I Continue to Phase 6?

```
START (After Phase 5)
  ↓
Gap Analysis complete? → NO → COMPLETE PHASE 5
  ↓ YES
New coverage ≥ 10%? → NO → ARCHIVE (Too much overlap)
  ↓ YES
Integration path clear? → NO → REVIEW (Unclear integration)
  ↓ YES
Stakeholder approval? → NO → GET APPROVAL
  ↓ YES
No blockers exist? → NO → RESOLVE BLOCKERS
  ↓ YES
PROCEED TO PHASE 6 (Taxonomy Updates)
```

---

## Best Practices

### For Transcription (Phase 1)

1. **Use Latest Prompt Version**
   - Always use v3.2 or v4.1 prompts for new videos
   - Ensures consistent quality and format

2. **Verify Metadata Accuracy**
   - Double-check video title, creator, duration
   - Ensure publication date is accurate
   - Verify video URL is correct

3. **Spot-Check Transcription**
   - Manually review 10-15 random segments
   - Verify technical terms are spelled correctly
   - Confirm timestamps are accurate

4. **Categorize Action Verbs Thoroughly**
   - Use all 7 categories (A-G)
   - Include new categories F and G for browser/data operations
   - Avoid "Other" category unless truly unique

---

### For Analysis (Phase 3)

1. **Structure Workflows Consistently**
   - Always include: OBJECTIVE, STEPS, TOOLS, INPUT, OUTPUT
   - Optional: DURATION, COMPLEXITY, PREREQUISITES
   - Use clear, action-oriented language

2. **Identify Integration Patterns**
   - Document how tools work together
   - Identify multi-tool workflows
   - Note synergies and dependencies

3. **Prioritize High-Value Workflows**
   - Focus on workflows with clear business value
   - Extract complete workflows before partial ones
   - Document workflow variations if applicable

---

### For Gap Analysis (Phase 5)

1. **Be Conservative in Coverage Estimates**
   - Underestimate rather than overestimate coverage improvement
   - Validate against existing LIBRARIES entities
   - Cross-check with similar videos

2. **Identify Quick Wins**
   - Highlight tools/workflows that are easy to integrate
   - Note elements that fill critical gaps
   - Prioritize high-impact, low-effort additions

3. **Document Integration Challenges**
   - Note any ambiguities or unclear categorizations
   - Identify dependencies on other entities
   - Flag potential conflicts with existing documentation

---

### For Taxonomy Updates (Phase 6)

1. **Backup Before Updating**
   - Always create backup of entity files before editing
   - Use version control (git) if available
   - Document changes in update log

2. **Maintain Bidirectional Cross-References**
   - Every Tool → Action reference needs Action → Tool reference
   - Every Tool → Object reference needs Object → Tool reference
   - Validate cross-references after updates

3. **Follow Naming Conventions**
   - Tool IDs: TOOL-{CATEGORY}-###
   - Workflow IDs: WRF-###
   - Action IDs: ACT-###
   - Object IDs: OBJ-###

4. **Test Integration**
   - Verify updated files load correctly
   - Check cross-references work
   - Validate no orphaned references

---

### For Reporting (Phase 7)

1. **Quantify Everything**
   - Use specific numbers (X tools created, Y% improvement)
   - Provide metrics where possible
   - Avoid vague statements ("many tools")

2. **Highlight Business Value**
   - Connect findings to business priorities
   - Identify specific use cases
   - Note department relevance

3. **Provide Actionable Next Steps**
   - Recommend related videos to process
   - Suggest follow-up research
   - Identify additional integration opportunities

---

### For User Input Variations

1. **Document All Customizations**
   - Note any prompt modifications
   - Record reasons for customization
   - Track results vs. standard approach

2. **Share Learnings**
   - Document what worked well
   - Note what didn't work
   - Update prompt versions based on findings

3. **Iterate Based on Feedback**
   - Review quality scores across videos
   - Identify patterns in high-quality vs. low-quality processing
   - Refine prompts and approaches based on data

---

## Appendix: Prompt Version Quick Reference

| Version | Action Categories | Output Format | Key Features | Use Cases |
|---------|-------------------|---------------|--------------|-----------|
| v2.0 | A-E (5 categories) | JSON | Basic extraction | Deprecated |
| v3.0 | A-F (6 categories) | Markdown | Browser/Agentic ops | Browser automation |
| v3.1 | A-G (7 categories) | Markdown | Data operations | Lead gen, data pipelines |
| v3.2 | A-G (7 categories) | Markdown | Task manager integration | General use (recommended) |
| v4.1 | A-G (7 categories) | Markdown | Full integration | All new videos (standard) |

**Recommendation:** Use v4.1 for all new video processing as of November 2025.

---

**Next Review:** After processing 10 videos with v4.1 (assess effectiveness)
**Maintained By:** Video Research Team
**Status:** Active
