---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_Discovery_Pipeline
title: Video Discovery Pipeline
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video Discovery Pipeline

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video Discovery Pipeline

**Entity Type:** LIBRARIES
**Sub-Entity:** Researches/Videos
**Purpose:** Systematic pipeline for discovering, prioritizing, and processing high-value AI tutorial videos for taxonomy extraction
**Created:** November 14, 2025
**Status:** Active

---

## Overview

The Video Discovery Pipeline is a systematic workflow for continuous taxonomy growth through strategic video content identification, evaluation, and extraction. This pipeline ensures the taxonomy stays current with emerging AI tools, workflows, and best practices.

**Goal:** Sustainable, scalable process for adding 2-4 high-value videos per month to the taxonomy library.

---

## Pipeline Architecture

```
┌─────────────────┐
│  1. Discovery   │ → Weekly scanning of AI content sources
└────────┬────────┘
         ↓
┌─────────────────┐
│  2. Evaluation  │ → Scoring system (0-100 points)
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. Priorit      │ → Queue management (High/Med/Low)
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. Transcribe   │ → Automated transcription + analysis
└────────┬────────┘
         ↓
┌─────────────────┐
│  5. Extract     │ → v3.2 prompt (90%+ automated)
└────────┬────────┘
         ↓
┌─────────────────┐
│  6. Integrate   │ → Update indexes + cross-references
└─────────────────┘
```

---

## Phase 1: Discovery Sources

### Primary Sources (Weekly Monitoring)

**YouTube Channels:**
- **Matthew Berman** (AI news, model comparisons, benchmarks)
- **Cole** (Engineering, tech stacks, RAG systems)
- **Matt Wolfe** (AI tools, product demos, workflow automation)
- **Nick Saraev** (Business automation, lead generation, growth)
- **Darren Wiener** (Claude Code, business OS, AI systems)
- **D-Squared** (Claude integration, MCP connectors, no-code)
- **Liam Otley** (AI agency, automation, business systems)
- **AI Jason** (AI tools, productivity, automation)
- **WorldofAI** (AI news aggregation, tool reviews)
- **TheAIGRID** (Deep dives, technical tutorials)

**Tracking Method:**
- Reference: [Influencer_Tracking/YouTube_Channels.json](../AI_Tutorials/Influencer_Tracking/YouTube_Channels.json)
- Reference: [Influencer_Tracking/Influencer_Database.json](../AI_Tutorials/Influencer_Tracking/Influencer_Database.json)

**Secondary Sources:**
- **Reddit:** r/LocalLLaMA, r/MachineLearning, r/ArtificialIntelligence
- **Twitter/X:** Key AI researchers and practitioners
- **Perplexity Research Sessions:** Weekly AI tools/trends queries
- **Product Hunt:** New AI tool launches
- **GitHub Trending:** AI/ML repositories

### Discovery Frequency

| Source Type | Check Frequency | Time Investment | Expected Yield |
|-------------|----------------|-----------------|----------------|
| **Top 5 YouTube Channels** | 2x per week | 30 min | 3-5 candidates |
| **Extended YouTube Channels** | 1x per week | 20 min | 1-2 candidates |
| **Reddit/Twitter** | 1x per week | 15 min | 1-3 candidates |
| **Perplexity Research** | 1x per month | 30 min | 2-4 candidates |
| **Product Hunt** | 1x per week | 10 min | 0-2 candidates |
| **Total** | **Weekly** | **1.5-2 hours** | **7-16 candidates** |

---

## Phase 2: Evaluation System

### Scoring Matrix (0-100 Points)

**A. Content Quality (0-30 points)**
- **Technical Depth** (0-10): Superficial overview (0-3), Practical tutorial (4-7), Deep technical dive (8-10)
- **Demonstrated Workflows** (0-10): No workflows (0), 1-3 workflows (5), 4+ workflows (10)
- **Tool Coverage** (0-10): 0-2 tools (0-3), 3-5 tools (4-7), 6+ tools (8-10)

**B. Taxonomy Value (0-40 points)**
- **New Tools** (0-15): Known tools only (0-5), 1-2 new tools (6-10), 3+ new tools (11-15)
- **New Workflows** (0-15): Generic workflows (0-5), 2-3 unique workflows (6-10), 4+ unique workflows (11-15)
- **Integration Patterns** (0-10): No integration (0-3), 1-2 patterns (4-7), 3+ patterns (8-10)

**C. Strategic Fit (0-20 points)**
- **Coverage Gap** (0-10): Overlaps existing (0-3), Partial gap fill (4-7), Major gap fill (8-10)
- **Trend Relevance** (0-10): Declining tech (0-3), Current tech (4-7), Emerging trend (8-10)

**D. Production Quality (0-10 points)**
- **Clarity** (0-5): Poor audio/unclear (0-2), Good clarity (3-4), Excellent (5)
- **Transcribability** (0-5): Heavy jargon/accents (0-2), Standard speech (3-4), Clear structured (5)

**Scoring Thresholds:**
- **90-100:** Must process (Exceptional value)
- **75-89:** High priority (Process within 1 week)
- **60-74:** Medium priority (Process within 1 month)
- **45-59:** Low priority (Backlog, revisit quarterly)
- **0-44:** Skip (Insufficient value)

---

## Phase 3: Prioritization Queue

### Queue Management

**High Priority Queue** (Score 75-100):
- Target: Process 2-4 videos per month
- Max queue size: 10 videos
- Review frequency: Weekly

**Medium Priority Queue** (Score 60-74):
- Target: Process 1-2 videos per month (if bandwidth available)
- Max queue size: 20 videos
- Review frequency: Monthly

**Low Priority Backlog** (Score 45-59):
- Quarterly review for potential promotion
- No processing unless strategic need identified

### Priority Boosters (Add +10 points each)

1. **Frontier Model Release:** New GPT/Claude/Gemini/DeepSeek model
2. **Ecosystem Shift:** Major API/platform change (e.g., OpenAI agents, Anthropic MCPs)
3. **Coverage Critical:** Addresses identified taxonomy gap
4. **Time-Sensitive:** Tool/technique with short relevance window
5. **Creator Authority:** Known expert in specific domain

### Example Scored Videos

| Video | Quality | Taxonomy | Strategic | Production | **Total** | Priority |
|-------|---------|----------|-----------|------------|-----------|----------|
| Video_005 (Cole - Tech Stack) | 28 | 38 | 18 | 9 | **93** | Must Process |
| Video_003 (Kimi K2 Thinking) | 25 | 35 | 17 | 10 | **87** | High |
| Video_006 (Lead Gen) | 22 | 32 | 14 | 8 | **76** | High |
| Video_008 (Claude MCP) | 20 | 30 | 16 | 9 | **75** | High |

---

## Phase 4: Transcription Process

### Automated Transcription

**Tools:**
- **Primary:** Claude Code with Whisper API integration
- **Fallback:** YouTube auto-captions + cleanup
- **Quality Check:** Manual review of first 2 minutes

**Process:**
1. Extract YouTube URL
2. Download audio using yt-dlp
3. Transcribe with Whisper Large v3
4. Apply v3.2 Video Transcription prompt
5. Generate embedded taxonomy analysis
6. Save to `Video_XXX.md`

**Time Investment:**
- Automated: 5-10 minutes per video
- Manual cleanup: 10-15 minutes per video
- Total: **15-25 minutes**

---

## Phase 5: Extraction Workflow

### v3.2 Prompt Automation (90-95% Automated)

**What v3.2 Provides:**
- ✅ Workflows identified and structured
- ✅ Action verbs categorized (7 categories)
- ✅ Tools matrix generated
- ✅ Objects/deliverables listed
- ✅ Integration patterns documented
- ✅ Business concepts extracted
- ✅ Optimization techniques noted
- ✅ Task chains mapped

**Manual Work (5-10% of effort):**
- Create individual tool JSON files (10-20 min for 5-10 tools)
- Create workflow collection JSONs (5-10 min)
- Create object collection JSONs (5-10 min)
- Update cross-references (5 min)

**Time Investment:**
- With embedded analysis: **25-40 minutes** total
- vs Old process: 2-4 hours (85-90% time savings)

---

## Phase 6: Integration & Updates

### Required Updates Per Video

**Files to Update:**
1. **VIDEOS_INDEX.md** - Add video entry, update statistics
2. **LIBRARIES_Import_Index.md** - Update entity counts, add video summary
3. **Cross_Reference_Mapping.json** - Link new entities to existing ones
4. **Actions_Master.json** - Verify new actions exist or add them
5. **Tool category indexes** - If new tool categories created

**Time Investment:** 15-20 minutes per video

---

## Pipeline Metrics & KPIs

### Success Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| **Videos Processed/Month** | 2-4 | TBD | - |
| **Discovery → Extraction Time** | <7 days | TBD | - |
| **Extraction Time Per Video** | <1 hour | 25-40 min | ✅ Ahead |
| **Tools Added/Month** | 10-20 | TBD | - |
| **Workflows Added/Month** | 8-15 | TBD | - |
| **Coverage Gap Closure/Quarter** | 20-30% | TBD | - |

### Pipeline Health Indicators

**Green (Healthy):**
- High priority queue: 5-10 videos
- Processing rate: 2-4 videos/month
- Average score: 75+ points
- Backlog age: <3 months

**Yellow (Attention Needed):**
- High priority queue: 11-15 videos OR <3 videos
- Processing rate: 1 video/month
- Average score: 60-74 points
- Backlog age: 3-6 months

**Red (Action Required):**
- High priority queue: >15 videos OR 0 videos
- Processing rate: <1 video/month
- Average score: <60 points
- Backlog age: >6 months

---

## Automation Opportunities

### Level 1: Currently Automated (✅)
- YouTube subscription notifications
- Transcription with Whisper
- Taxonomy analysis with v3.2 prompt
- Embedded workflow/tool extraction

### Level 2: Partially Automated (⏳)
- Video discovery scanning (manual check → could use RSS)
- Scoring evaluation (manual → could use LLM-based scorer)
- JSON file generation (template-based → could be fully automated)

### Level 3: Future Automation (📋)
- **Auto-Discovery Bot:** Weekly scan of subscribed channels, auto-score new videos
- **Priority Notification:** Alert when high-value video (75+ score) detected
- **One-Click Processing:** URL → Transcribe → Extract → Integrate with single command
- **Quality Assurance:** Automated validation of taxonomy completeness
- **Trend Detection:** Identify emerging tool categories, suggest proactive research

### Automation ROI

**Current State:**
- Discovery: 1.5-2 hours/week
- Evaluation: 15-20 min/video
- Processing: 40-60 min/video
- **Total:** ~4-6 hours/week for 2-4 videos

**With Level 2+3 Automation:**
- Discovery: 15 min/week (auto-scan + review)
- Evaluation: 5 min/video (LLM scorer + review)
- Processing: 15-20 min/video (one-click pipeline)
- **Total:** ~1-2 hours/week for 2-4 videos
- **Time Savings:** 60-75%

---

## Coverage Strategy

### Current Taxonomy Gaps (Nov 2025)

**High Priority Gaps:**
1. **AI Voice/Audio Tools** - Speechify, ElevenLabs, Whisper, etc.
2. **AI Video Tools** - Runway, Pika, Sora (when available)
3. **AI Design Tools** - Midjourney deep dive, DALL-E 3, Ideogram
4. **Local AI Stack** - Ollama, LM Studio, Llamafile workflows
5. **AI Testing/QA** - Automated testing with AI, evaluation frameworks

**Medium Priority Gaps:**
1. Enterprise AI adoption workflows
2. AI compliance & governance tools
3. Multimodal agent architectures
4. AI cost optimization strategies
5. Prompt engineering frameworks

**Low Priority (Monitor):**
1. Gaming/Entertainment AI
2. Research-only tools (not production-ready)
3. Deprecated/sunset technologies

---

## Quality Gates

### Before Adding to Queue

**Minimum Requirements:**
- [ ] Video is publicly accessible
- [ ] Duration: 10-60 minutes (sweet spot)
- [ ] Published within last 12 months (or timeless content)
- [ ] Creator has 10K+ subscribers OR known domain authority
- [ ] English language (or high-quality subtitles available)

### Before Transcription

**Quality Checks:**
- [ ] Scored 60+ points
- [ ] Does not duplicate existing video content >80%
- [ ] Audio quality sufficient for transcription
- [ ] Practical content (not pure theory/news)

### Before Integration

**Completeness Checks:**
- [ ] At least 3 actionable workflows OR 5 tools identified
- [ ] Taxonomy analysis complete (all 12 sections)
- [ ] Cross-references identified
- [ ] No duplicate tool IDs
- [ ] Proper JSON formatting validated

---

## Workflow Templates

### Weekly Discovery Session (30-45 minutes)

**Monday Morning Routine:**

1. **Scan Top 5 Channels** (20 min)
   - Check last 7 days uploads
   - Quick evaluate titles/thumbnails
   - Add candidates to evaluation list

2. **Score Candidates** (15 min)
   - Watch first 2-3 minutes
   - Apply scoring matrix
   - Add to appropriate queue

3. **Update Queue Status** (5 min)
   - Review high priority queue
   - Select next video to process
   - Update pipeline dashboard

4. **Plan Week** (5 min)
   - Target: Process 1 video this week
   - Block 1-2 hour calendar slot
   - Prepare extraction checklist

### Monthly Pipeline Review (1 hour)

**First Friday of Month:**

1. **Metrics Review** (15 min)
   - Videos processed last month
   - Tools/workflows added
   - Coverage gaps addressed
   - Processing time trends

2. **Queue Grooming** (20 min)
   - Promote medium → high if needed
   - Archive low priority if stale (>6 months)
   - Reassess scores based on new context

3. **Gap Analysis** (15 min)
   - Identify new coverage gaps
   - Research emerging tools/trends
   - Add targeted discovery goals

4. **Process Optimization** (10 min)
   - Review bottlenecks
   - Identify automation opportunities
   - Update pipeline documentation

---

## Tools & Resources

### Required Tools

| Tool | Purpose | Cost | Status |
|------|---------|------|--------|
| **YouTube Premium** | Ad-free viewing, offline | $12/mo | Optional |
| **yt-dlp** | Video/audio download | Free | Required |
| **Whisper Large v3** | Transcription | API cost | Required |
| **Claude Code** | Analysis automation | $20/mo | Required |
| **Perplexity Pro** | Trend research | $20/mo | Recommended |
| **Notion/Airtable** | Pipeline tracking | Free tier | Optional |

### Reference Documents

- [Video_Transcription_Custom_Instructions.md](../Prompts/Video_Transcription/Video_Transcription_Custom_Instructions.md) - v3.2 prompt
- [VIDEOS_INDEX.md](./VIDEOS_INDEX.md) - Master video catalog
- [Influencer_Tracking/](../AI_Tutorials/Influencer_Tracking/) - Creator database
- [LIBRARIES_Import_Index.md](../../LIBRARIES_Import_Index.md) - Entity statistics

---

## Success Stories

### Video_005: Agentic Engineering Stack
- **Score:** 93 points (Exceptional)
- **Processing Time:** 2.5 hours (phased approach)
- **Output:** 44 tools, 10 objects, 2 workflows, 5 integration patterns
- **Impact:** Largest single video extraction, +60-80% coverage for agentic engineering
- **Lesson:** High-scoring videos justify extended processing time

### Video_003: Kimi K2 Thinking
- **Score:** 87 points
- **Processing Time:** 25 minutes (embedded analysis + 1 tool)
- **Output:** 1 frontier model tool, 3 workflows, benchmark data
- **Impact:** First open-source model beating GPT-5 documented
- **Lesson:** Frontier model releases = immediate priority boost

### Video_006: Lead Generation
- **Score:** 76 points
- **Processing Time:** 1.5 hours (v3.1 prompt era)
- **Output:** 14 workflows, 12 tools, new action category
- **Impact:** G. DATA OPERATIONS category contribution
- **Lesson:** Business automation content = high workflow density

---

## Next Steps & Roadmap

### Immediate (Next 30 Days)
- [ ] Set up weekly discovery routine (Monday mornings)
- [ ] Create pipeline tracking spreadsheet/dashboard
- [ ] Process 2-3 high priority videos from current backlog
- [ ] Document first month metrics

### Short Term (Next 90 Days)
- [ ] Build Level 2 automation (LLM-based scorer)
- [ ] Establish monthly review cadence
- [ ] Achieve 2-4 videos/month processing rate
- [ ] Close 2-3 identified coverage gaps

### Long Term (Next 12 Months)
- [ ] Implement Level 3 automation (one-click pipeline)
- [ ] Expand creator network to 25+ channels
- [ ] Process 30-50 videos total
- [ ] Achieve 80%+ coverage of production-ready AI tools

---

## Appendix A: Video Scoring Worksheet

```markdown
## Video Evaluation: [Video Title]

**Metadata:**
- Creator: [Name]
- Duration: [MM:SS]
- Published: [Date]
- URL: [Link]

**A. Content Quality (0-30)**
- Technical Depth: [0-10] _____
- Demonstrated Workflows: [0-10] _____
- Tool Coverage: [0-10] _____
**Subtotal A:** _____

**B. Taxonomy Value (0-40)**
- New Tools: [0-15] _____
- New Workflows: [0-15] _____
- Integration Patterns: [0-10] _____
**Subtotal B:** _____

**C. Strategic Fit (0-20)**
- Coverage Gap: [0-10] _____
- Trend Relevance: [0-10] _____
**Subtotal C:** _____

**D. Production Quality (0-10)**
- Clarity: [0-5] _____
- Transcribability: [0-5] _____
**Subtotal D:** _____

**Priority Boosters (+10 each):**
- [ ] Frontier Model Release
- [ ] Ecosystem Shift
- [ ] Coverage Critical
- [ ] Time-Sensitive
- [ ] Creator Authority

**TOTAL SCORE:** _____ / 100

**PRIORITY:** [Must Process / High / Medium / Low / Skip]

**NOTES:**
[Additional observations, specific tools mentioned, unique value proposition]
```

---

**Maintained By:** Taxonomy Team
**Last Updated:** November 14, 2025
**Status:** Active - Ready for implementation
**Next Review:** December 14, 2025


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-21 standardization scaffold added
