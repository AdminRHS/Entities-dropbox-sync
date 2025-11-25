# Complete Video Transcript Workflow - Full Instructions
**Comprehensive End-to-End Guide with All Prompts Fully Expanded**

---

## Document Information

**Purpose**: Complete step-by-step instructions for the entire video processing workflow, from discovery to library population, with all prompts and methodologies fully detailed in one document.

**Version**: 3.0 - Complete Expanded Edition
**Date**: November 17, 2025
**Last Updated**: November 17, 2025
**Target Audience**: All Team Members (can be used by anyone)
**Format**: Comprehensive Single-Document Guide

**This document contains:**
- Full Research methodology (YouTube_Video_Research_Prompt)
- Complete Transcription instructions v3.2 (Video_Transcription_Custom_Instructions)
- Full Analysis methodology (Video_Analysis_Prompt)
- Complete Library Processing instructions (Tools_Collection_and_Matching_Prompt)

---

## Table of Contents

### Part 1: Overview & Chain
1. [Introduction](#introduction)
2. [Complete Workflow Chain Overview](#complete-workflow-chain-overview)
3. [Time Investment & ROI](#time-investment--roi)

### Part 2: Stage 1 - Research (FULL)
4. [STAGE 1: Video Discovery & Research - Complete Instructions](#stage-1-video-discovery--research---complete-instructions)
   - Research Focus & Strategic Priorities
   - Search Platforms & Configuration
   - Scoring System (0-100 points) - Full Details
   - Search Query Examples
   - Video Selection & Documentation
   - Output Templates

### Part 3: Stage 2 - Processing (FULL)
5. [STAGE 2: Video Transcription - Complete Instructions v3.2](#stage-2-video-transcription---complete-instructions-v32)
   - Core Transcription Requirements (Sections 1-3)
   - Taxonomy Extraction Requirements (Sections 4-14) - Full Details
   - All Naming Conventions
   - All Extraction Templates
   - Validation Checklist

6. [STAGE 2: Video Analysis - Complete Methodology](#stage-2-video-analysis---complete-methodology)
   - 3-Phase Analysis Workflow (Full Details)
   - All Extraction Techniques
   - Tool/Workflow/Action Templates
   - Coverage Calculation

### Part 4: Stage 3 - Population (FULL)
7. [STAGE 3: Library Processing - Complete Instructions](#stage-3-library-processing---complete-instructions)
   - Tool Collection & Validation (Full Process)
   - Tool JSON Schema & Examples
   - Categorization Guide (All Categories)
   - Tool ID Generation Rules
   - Mapping Updates
   - Gap Analysis

### Part 5: Integration & Execution
8. [Data Flow & Integration Points](#data-flow--integration-points)
9. [Weekly Workflow Schedule](#weekly-workflow-schedule)
10. [Quality Assurance & Metrics](#quality-assurance--metrics)
11. [Quick Start Guide](#quick-start-guide)

---

# PART 1: OVERVIEW & CHAIN

## Introduction

### What This Complete Workflow Does

This comprehensive workflow transforms strategic priorities into actionable knowledge through a systematic 3-stage process:

**Stage 1: Research** - Find relevant videos based on actual work priorities
**Stage 2: Processing** - Transcribe and extract structured taxonomy data
**Stage 3: Population** - Validate and integrate into libraries

### Why This Matters

**Knowledge Gain:**
- Continuous discovery of new tools, workflows, and best practices
- Structured, searchable knowledge base
- Always up-to-date with latest technologies

**Time Efficiency:**
- 90-95% reduction in processing time (4.5-9.5 hours → 50-100 minutes per video)
- Automated extraction eliminates manual data entry
- Reusable templates minimize rework

**Strategic Alignment:**
- Research driven by actual business priorities
- Department-specific relevance scoring
- Measurable ROI and coverage metrics

---

## Complete Workflow Chain Overview

```
┌─────────────────────────────────────────────────────┐
│  INPUT: Daily Reports & Strategic Priorities        │
└─────────────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────┐
│              STAGE 1: RESEARCH                      │
│         (Video Discovery & Scoring)                 │
│                                                     │
│  • Search platforms (Perplexity, YouTube)          │
│  • Score videos (0-100 relevance)                  │
│  • Select top 3-5 videos (score 80+)              │
└─────────────────────────────────────────────────────┘
                       ↓
        OUTPUT: Scored video list with URLs
                       ↓
┌─────────────────────────────────────────────────────┐
│           STAGE 2: PROCESSING                       │
│    (Transcription & Analysis)                       │
│                                                     │
│  • Transcribe video (Google AI Studio)            │
│  • Extract 14 taxonomy sections                    │
│  • Identify tools, workflows, tasks, steps         │
│  • Analyze and validate                            │
└─────────────────────────────────────────────────────┘
                       ↓
   OUTPUT: Structured markdown with taxonomy data
                       ↓
┌─────────────────────────────────────────────────────┐
│         STAGE 3: POPULATION                         │
│      (Library Integration)                          │
│                                                     │
│  • Validate tools (check existing)                 │
│  • Create/enrich tool entries                      │
│  • Integrate tasks, steps, skills                  │
│  • Update mappings                                 │
│  • Generate gap analysis                           │
└─────────────────────────────────────────────────────┘
                       ↓
        OUTPUT: Updated LIBRARIES
   ┌──────────────────────────────────────┐
   │ • Tools (new/enriched JSON files)    │
   │ • Task Templates (.md files)         │
   │ • Step Templates (.md files)         │
   │ • Skills (JSON files)                │
   │ • Mappings (tool_mapping.json)       │
   │ • Gap Analysis Report                │
   └──────────────────────────────────────┘
                       ↓
              FEEDBACK LOOP
   (Gap analysis → Next research cycle)
```

---

## Time Investment & ROI

### Time Per Stage

| Stage | Activity | Time Required | Frequency |
|-------|----------|---------------|-----------|
| **Stage 1** | Research & Scoring | 2-3 hours | Weekly |
| **Stage 2** | Transcription & Analysis | 40-80 min | Per video |
| **Stage 3** | Library Population | 10-20 min | Per video |
| **TOTAL** | Complete workflow | 8-12 hours | Weekly (3-5 videos) |

### ROI Calculation

**Before v3.2 (manual processing):**
- Transcription: 30-60 minutes
- Manual library mapping: 2-4 hours
- Task Template creation: 1-2 hours
- Step extraction: 1-2 hours
- **Total: 4.5-9.5 hours per video**

**After v3.2 (automated extraction):**
- Transcription with extraction: 40-60 minutes
- Direct taxonomy output: Included
- Library integration: 10-20 minutes
- **Total: 50-80 minutes per video**

**Time Savings: 90-95%**

**Weekly Output:**
- 3-5 videos fully processed
- 15-25 new tools discovered and integrated
- 10-20 Task Templates created
- 30-50 Step Templates created
- 15-25 skills identified

---

# PART 2: STAGE 1 - RESEARCH (FULL)

## STAGE 1: Video Discovery & Research - Complete Instructions

### Overview

**Goal**: Identify 8-12 relevant videos weekly based on strategic priorities

**Time**: 2-3 hours per week

**Output**: Research results document with scored videos (top 3-5 selected for processing)

---

### Step 1.1: Define Research Focus

#### Primary Research Sources

**1. Daily Reports Analysis**
- Location: Daily `.md` files from team members
- Extract: Tasks being worked on, problems encountered, tools in use, workflows followed
- Process with: MAIN PROMPT v4.md (if available)

**2. Strategic Initiative Documents**
- Current priorities for November 2025
- Department-specific requests
- Project challenges requiring solutions

**3. Department Needs**
- AI Team: Automation, LLM integration, prompt engineering
- Video Team: Video generation, editing automation
- Design Team: Design tools, creative workflows
- Dev Team: IDEs, development tools, CI/CD
- LG Team: Lead generation, prospecting, analytics
- Sales Team: CRM, outreach automation
- HR Team: Onboarding, documentation

---

### Critical Priority Topics (November 2025)

#### 🔥 CRITICAL PRIORITY (40 pts Strategic Alignment)

**1. File System & Workflow Automation**
- Meeting transcription workflows (Whisper, Claude, automated task generation)
- AI-assisted daily workflows reducing administrative overhead by 60-80%
- VS Code / Cursor IDE automation and extensions
- Claude Code integration and Claude Desktop applications
- Automated plan & task generation from transcripts

**Search Queries:**
```
"AI meeting transcription automation workflow 2025"
"Claude Code business applications"
"Cursor IDE automation techniques"
"VS Code automation extensions 2025"
"Automated task generation from transcripts"
```

**2. Natural Language Automation**
- Opal AI MiniApps (write automation in natural language vs complex workflow builders)
- Replacing traditional n8n/Make workflows with conversational automation
- No-code automation tools with AI interfaces

**Search Queries:**
```
"Opal AI MiniApps tutorial"
"Natural language workflow automation 2025"
"No-code automation with AI"
"Conversational automation tools"
```

**3. Open-Source Video Generation**
- WAN 2.2 video model (lighting, camera angles, scene composition controls)
- Runway Gen-3 updates and tutorials
- AI video generation for marketing and client content
- Synthesia, HeyGen, Hedra latest features

**Search Queries:**
```
"WAN 2.2 video generation tutorial"
"Runway Gen-3 2025 updates"
"Open source video generation AI"
"HeyGen tutorial 2025"
"Synthesia latest features"
```

**4. Real-Time Analytics & Dashboard Transformation**
- Shifting from monthly to daily/weekly analytics
- AI-powered analytics platforms (like Tendency)
- Data visualization and automated reporting
- Performance tracking dashboards

**Search Queries:**
```
"Daily analytics dashboard automation"
"Real-time analytics AI powered 2025"
"Tendency analytics tutorial"
"Automated reporting dashboards"
```

**5. Lead Generation Strategy & Optimization**
- Modern lead generation strategies (2025 best practices)
- AI-powered prospecting and qualification
- Appointment scheduling optimization
- Lead conversion analytics and tracking
- Alternative to data entry-focused LG workflows

**Search Queries:**
```
"Lead generation strategy 2025 AI powered"
"AI prospecting tools 2025"
"Modern lead gen best practices"
"Appointment scheduling automation"
```

---

#### 📊 HIGH-PRIORITY TOPICS (30 pts Strategic Alignment)

**6. AI Agents & Agentic Workflows**
- Claude with MCP (Model Context Protocol) integrations
- Browser automation agents (Perplexity Comet style)
- Multi-step AI workflows and tool chaining
- RAG (Retrieval Augmented Generation) systems
- AI agent frameworks and orchestration

**Search Queries:**
```
"Claude MCP integration tutorial"
"AI agents agentic workflows 2025"
"Browser automation AI agents"
"RAG systems implementation"
```

**7. Discord Server Automation**
- Discord bot development (ProBot, CarlBot alternatives)
- Advanced logging (voice events, member tracking, server analytics)
- Discord workflow automation
- Integration with AI tools

**Search Queries:**
```
"Discord bot automation advanced logging"
"Discord AI integration 2025"
"Discord server analytics automation"
```

**8. Project Management & Documentation**
- AI-assisted PM methodologies
- Automated documentation generation
- Knowledge base management (like RAC - Remote AI Context)
- Template-driven operations
- AI prompt compression techniques

**Search Queries:**
```
"AI project management documentation"
"Automated documentation generation 2025"
"Knowledge base AI automation"
```

**9. Business Process Automation**
- CRM automation and workflow optimization
- Email automation beyond basic campaigns
- Client onboarding automation
- Cross-department workflow coordination

**Search Queries:**
```
"CRM automation workflow 2025"
"Business process automation AI"
"Client onboarding automation"
```

**10. AI Development Tools & Coding Assistants**
- Cursor IDE advanced tutorials
- Windsurf AI coding features
- Claude Desktop for development
- AI code generation best practices
- GitHub integration workflows

**Search Queries:**
```
"Cursor IDE advanced features 2025"
"Windsurf AI coding assistant"
"Claude Desktop development workflow"
```

---

### Step 1.2: Search for Videos

#### Search Platforms

**Primary Platform: Perplexity AI** ⭐ RECOMMENDED

**Configuration:**
```
Settings:
- Creativity: 0.5
- Enable "Structure it out" mode
- Disable Google Search
- Enable specific search features below Google Search toggle
```

**Why Perplexity:**
- Best for finding recent videos (last 30-60 days)
- Structured output format
- Can filter by date, length, creator
- Provides relevance context

**Usage:**
1. Go to https://www.perplexity.ai/
2. Paste search query from lists above
3. Add filters: "YouTube videos published in last 30 days, 10-40 minutes length"
4. Review results with context
5. Extract video URLs, titles, creators

**Secondary Platform: YouTube Direct Search**

**Filters:**
```
Upload date: Last month
Duration: 10-40 minutes (preferred: 15-25 minutes)
Sort by: Relevance
```

**Usage:**
1. Use search queries from lists above
2. Apply filters
3. Check preferred creators first (see list below)
4. Note video metadata

**Alternative: ChatGPT / Claude with Web Search**

**Prompt Template:**
```
Find YouTube videos published in the last 30-60 days about [TOPIC].
Focus on:
- Tutorial videos (10-40 minutes)
- Practical demonstrations
- Step-by-step workflows
NOT news/hype videos.

Provide:
- Video title
- Creator
- URL
- Published date
- Duration
- Brief description
```

---

#### Search Criteria (Critical)

**Published Date:**
- **Last 30-60 days ONLY** (October 15 - December 15, 2025)
- Reason: Latest tools, features, best practices
- Exception: Foundational tutorials (can be up to 90 days old)

**Video Length:**
- **Preferred: 10-40 minutes**
- **Sweet spot: 15-25 minutes**
- Too short (<10 min): Often hype/announcements, insufficient depth
- Too long (>40 min): Time-consuming to process, often unfocused

**Quality Focus:**
```
✅ LOOK FOR:
- Practical tutorials with step-by-step workflows
- Tool demos with real business applications
- Case studies with measurable ROI/results
- "How to..." tutorials
- "Building..." demonstrations
- "Complete guide..." deep dives

❌ AVOID:
- Pure hype/news/announcements
- Tool release videos (unless showing usage)
- Theoretical discussions without examples
- Clickbait titles without substance
- Outdated content (>60 days)
```

**Technical Depth:**
```
✅ MUST HAVE:
- Actionable implementation steps
- Code examples or workflow screenshots
- Integration patterns and architecture
- Real-world use cases
- Actual tool demonstrations
```

---

#### Preferred Creators/Channels

**AI & Automation:**
- Matthew Berman (AI news, model benchmarks, tool reviews)
- Cole (agentic engineering, tech stacks, AI workflows)
- Matt Wolfe (AI tool demos, practical applications)
- Darren Wiener (Claude Code, business automation)
- D-Squared (Claude integrations, no-code)
- Liam Otley (AI automation, no-code workflows)
- AI Jason (AI workflows, automation)
- WorldofAI (AI news and tools)

**Lead Generation & Sales:**
- Nick Saraev / Leftclick (lead generation at scale)
- [Add your preferred LG creators]

**Development:**
- [Add your preferred dev tutorial creators]

**Why Preferred Creators:**
- Consistent quality
- Practical focus (not just theory)
- Regular uploads
- Business-oriented (not just tech demos)

---

### Step 1.3: Score & Prioritize Videos

#### Remote Helpers Relevance Score (0-100 Points)

**TOTAL SCORE = Strategic Alignment + Tool/Tech Relevance + Actionable Value**

---

#### Component 1: Strategic Alignment (0-40 points)

**40 points:**
- Directly addresses **Critical Priority Topics** (#1-5)
- Solves current blocker or decision point
- Example: Video about Opal AI MiniApps evaluation (Critical Priority #2)
- Example: Video about Claude Code file system automation (Critical Priority #1)

**30 points:**
- Strongly relates to **High-Priority Topics** (#6-10)
- Supports major initiative
- Example: Video about Claude MCP integration (High Priority #6)
- Example: Video about Discord automation (High Priority #7)

**20 points:**
- Tangentially related to our initiatives
- General improvement opportunity
- Example: Video about general project management (relates to Priority #8)

**10 points:**
- General relevance to AI/automation
- Nice-to-have, exploratory learning
- Example: Video about AI tool not in our stack

**0 points:**
- No strategic alignment
- Not relevant to current priorities

**Scoring Questions:**
1. Does this video address a Critical Priority Topic? → 40 pts
2. Does it help with current initiatives (November 2025)? → 30-40 pts
3. Will this solve a problem we're facing now? → 30-40 pts
4. Is it related to our strategic goals? → 20-30 pts
5. Is it just interesting but not strategic? → 0-10 pts

---

#### Component 2: Tool/Tech Relevance (0-30 points)

**30 points:**
- Features **3+ tools from our active stack**
- Example: Video using Claude + Cursor + GitHub (all in our stack)
- Example: Video showing n8n + ChatGPT + Notion integration

**20 points:**
- Features **1-2 tools from our active stack**
- Example: Video primarily about Figma (we use it)
- Example: Video showing Claude integration

**10 points:**
- **Compatible/integrable with our stack**
- Tool is not in our stack but can connect to our tools
- Example: New automation tool that integrates with n8n

**0 points:**
- **Unrelated tools**
- Tools we don't use and can't integrate
- Platform-specific tools for platforms we don't use

**Our Active Tech Stack (for reference):**

**AI & LLMs:**
- Claude (Anthropic), ChatGPT (GPT-4o), Perplexity AI, Gemini, Grok, Minimax, NotebookLM, Genspark

**Development:**
- Cursor (primary IDE), VS Code, Windsurf, Claude Desktop
- Replit, Google AI Studio, Smithery
- Lovable, v0 (Vercel), DeepSite, Bubble, Runner, OA-Y

**Video Production:**
- Runway (Gen-3), HeyGen, Synthesia, Hedra, Loom
- Maestra (transcription), WAN 2.2 (new focus)

**Design:**
- Leonardo.ai, Midjourney, Gamma (presentations), Manus

**Automation:**
- N8n (current), Make, Zapier
- Opal AI MiniApps (NEW - critical interest)

**Business & Analytics:**
- CRM systems, Discord (ProBot, CarlBot)
- Tendency analytics, Cove AI (sales intelligence)

**Data & Lead Generation:**
- Bright Data, Hunter.io, Instantly.ai, Apollo.io

**Scoring Questions:**
1. How many of our tools are featured? → Count them
2. Can we implement this immediately? → 20-30 pts
3. Would we need to add new tools? → 10 pts
4. Is it completely unrelated to our stack? → 0 pts

---

#### Component 3: Actionable Value (0-30 points)

**30 points: Immediately Implementable**
- **Step-by-step tutorial with code/workflows**
- Screen recordings showing exact steps
- Code examples provided (GitHub repo, description)
- Downloadable resources, templates
- Example: "Building a Claude MCP connector step-by-step with code"

**20 points: Clear Implementation Path**
- **Detailed demo with clear implementation guidance**
- Shows the full workflow
- Explains logic and decisions
- Some code shown but not complete
- Example: "How I automated my workflow with Claude" (shows process clearly)

**10 points: Conceptual with Some Practical Tips**
- **Conceptual overview with some actionable insights**
- General guidance, some tips
- Would need additional research to implement
- Example: "Overview of AI automation strategies" (useful concepts but not step-by-step)

**0 points: Pure Theory or Hype**
- **No practical implementation steps**
- Just announcements or news
- "This tool will change everything" (no how-to)
- Speculation without examples

**Scoring Questions:**
1. Can we implement this TODAY after watching? → 30 pts
2. Would we need only 1-2 hours more research? → 20 pts
3. Is it mostly concepts we'd need to figure out? → 10 pts
4. Is it just hype with no actionable steps? → 0 pts

---

#### Scoring Template

```markdown
### Video: [Full Title]

**Creator:** [Channel Name]
**URL:** [Full YouTube URL]
**Published:** [YYYY-MM-DD]
**Duration:** [MM:SS]

**Key Topics:**
- [Topic 1 - be specific]
- [Topic 2 - be specific]
- [Topic 3 - be specific]
- [Topic 4 if applicable]
- [Topic 5 if applicable]

**Relevance Score:** [XX]/100

**Breakdown:**
- **Strategic Alignment:** [XX]/40
  - Reason: [Why this score? Which priority topic? Current initiative?]
- **Tool/Tech Relevance:** [XX]/30
  - Reason: [Which tools featured? In our stack? How many?]
- **Actionable Value:** [XX]/30
  - Reason: [Tutorial? Demo? Conceptual? Code provided?]

**Department Relevance:** [Which departments benefit?]
- Primary: [Department Name]
- Secondary: [Department Name]
- Tertiary: [Department Name]

**Implementation Priority:** [Critical / High / Medium / Low]

**One-Sentence Value:**
[Why should we watch this video? What specific value will we gain?]

**Notes:**
- [Any additional context]
- [Concerns or considerations]
- [Prerequisites if any]
```

---

#### Scoring Examples

**Example 1: High-Scoring Video (92/100)**

```markdown
### Video: Building Production-Ready MCP Servers with Claude - Complete Tutorial

**Creator:** Darren Wiener
**URL:** https://youtube.com/watch?v=xyz123
**Published:** 2025-11-10
**Duration:** 24:35

**Key Topics:**
- MCP (Model Context Protocol) server development
- Claude Desktop integration
- OAuth 2.0 setup for Google APIs
- Production deployment with error handling
- Real workflow automation example (email drafts)

**Relevance Score:** 92/100

**Breakdown:**
- **Strategic Alignment:** 38/40
  - **Reason:** Directly addresses Critical Priority #1 (File System & Workflow Automation - Claude Code integration). Supports our Claude Desktop rollout initiative. Solves current need for MCP connector development.

- **Tool/Tech Relevance:** 28/30
  - **Reason:** Features Claude Desktop (we use), VS Code/Cursor (our primary IDE), Google APIs (we use Gmail). All tools in our active stack. Missing 2 pts because doesn't show n8n integration.

- **Actionable Value:** 26/30
  - **Reason:** Step-by-step tutorial with code examples. GitHub repo provided. Shows complete OAuth setup. Real workflow demonstrated. Missing 4 pts because deployment steps are summarized (not full detail).

**Department Relevance:**
- Primary: AI Team (MCP development)
- Secondary: Operations (workflow automation)
- Tertiary: Dev Team (deployment)

**Implementation Priority:** Critical

**One-Sentence Value:**
Provides complete step-by-step guide to building MCP servers that directly supports our Claude Desktop rollout and enables 15+ hours/week time savings through automated workflows.

**Notes:**
- GitHub repo: github.com/example/mcp-tutorial
- Prerequisites: Node.js, Claude Desktop installed
- Estimated implementation time: 2-3 hours
```

**Example 2: Medium-Scoring Video (65/100)**

```markdown
### Video: 10 AI Tools You Should Know in 2025

**Creator:** AI Trends Channel
**URL:** https://youtube.com/watch?v=abc456
**Published:** 2025-11-15
**Duration:** 18:20

**Key Topics:**
- Overview of 10 AI tools
- Brief demos of each tool
- Use case examples
- Pricing comparison

**Relevance Score:** 65/100

**Breakdown:**
- **Strategic Alignment:** 20/40
  - **Reason:** Tangentially related to our AI initiatives. Covers tools broadly but not focused on our specific priorities. General exploration, not addressing current blockers.

- **Tool/Tech Relevance:** 15/30
  - **Reason:** 2 tools featured are in our stack (ChatGPT, Midjourney). Other 8 tools are new or not in our stack. Some compatible/integrable.

- **Actionable Value:** 30/30
  - **Reason:** Clear demos of each tool. Shows exact steps to get started. Pricing info provided. Links in description. Immediately actionable for exploration.

**Department Relevance:**
- Primary: AI Team (tool discovery)
- Secondary: All teams (general awareness)

**Implementation Priority:** Medium

**One-Sentence Value:**
Provides quick overview of emerging AI tools with clear demos, useful for expanding our toolkit awareness but not addressing immediate priorities.

**Notes:**
- Good for general knowledge building
- Could spark ideas for future initiatives
- Would need additional research for actual implementation
```

---

### Step 1.4: Select & Document Videos

#### Selection Criteria

**Minimum Score: 70/100**
- Below 70: Not worth processing time
- 70-79: Watch if time permits (lower priority)
- 80-89: High priority, watch this week
- 90-100: Critical, watch immediately

**Priority Order:**

**1. Critical Priority + Score 90+** ⭐⭐⭐
- Watch immediately
- Process within 24 hours
- Share with relevant departments same day

**2. Critical Priority + Score 80-89** ⭐⭐
- Watch within 2-3 days
- Process within week
- Priority for Stage 2

**3. High Priority + Score 85+** ⭐⭐
- Watch this week
- Process within week
- Good candidates for Stage 2

**4. High Priority + Score 75-84** ⭐
- Watch if time permits
- Process if capacity available
- Keep in backlog

**5. Score 70-74** (any priority)
- Lower priority
- Process only if no higher-scored videos available
- May skip if time constrained

#### Weekly Target

**Select: 3-5 videos for processing**

**Ideal Mix:**
- 2 Critical Priority videos (scores 85+)
- 2 High Priority videos (scores 80+)
- 1 Exploratory video (score 75-79, interesting topic)

**Why This Mix:**
- Ensures strategic priorities covered
- Allows for discovery of new approaches
- Balances depth with breadth

---

#### Documentation Format

**File Name:**
```
Research_Results_YYYY-MM-DD_[Focus_Area].md
```

**Examples:**
```
Research_Results_2025-11-17_Opal_AI_Automation.md
Research_Results_2025-11-17_Video_Generation_Tools.md
Research_Results_2025-11-17_Weekly_Research.md
```

**File Template:**

```markdown
# Video Research Results - [Date]

**Research Date:** [YYYY-MM-DD]
**Researcher:** [Name]
**Focus Areas:** [List priority topics researched]
**Total Videos Found:** [Count]
**Videos Selected for Processing:** [Count]

---

## Summary

**Top Videos (Selected for Processing):**
1. [Video Title] - Score: XX/100
2. [Video Title] - Score: XX/100
3. [Video Title] - Score: XX/100
[Continue for all selected videos]

**Key Findings:**
- [Insight 1]
- [Insight 2]
- [Insight 3]

**Recommended Actions:**
- [Action item 1]
- [Action item 2]

---

## Video 1: [Title] ⭐ SELECTED

[Full scoring template from Step 1.3]

---

## Video 2: [Title] ⭐ SELECTED

[Full scoring template]

---

[Continue for all videos, mark selected ones]

---

## Videos Not Selected (For Reference)

### Video: [Title] - Score: 68/100
**Reason Not Selected:** Score below 70 threshold
**Brief Notes:** [Why scored low]

[Continue for other videos researched but not selected]

---

## Next Steps

**Assigned for Processing:**
- Video 1: [Assigned to Team Member Name] - Deadline: [Date]
- Video 2: [Assigned to Team Member Name] - Deadline: [Date]
- Video 3: [Assigned to Team Member Name] - Deadline: [Date]

**Timeline:**
- Stage 2 (Processing): [Start Date] - [End Date]
- Stage 3 (Population): [Start Date] - [End Date]
- Gap Analysis: [Date]

---

**Research Completed By:** [Name]
**Date:** [YYYY-MM-DD]
**Next Research Cycle:** [Next Monday]
```

---

### Stage 1 Checklist

**Before Starting Research:**
- [ ] Strategic priorities reviewed (current initiatives)
- [ ] Department needs collected
- [ ] Search platform configured (Perplexity settings)
- [ ] Preferred creators list reviewed

**During Research:**
- [ ] Search queries prepared (from priority topics)
- [ ] 8-12 videos identified
- [ ] All videos scored using 0-100 system
- [ ] Score breakdown documented (Strategic + Tech + Actionable)
- [ ] Department relevance identified for each video
- [ ] One-sentence value proposition written for each

**Video Selection:**
- [ ] Top 3-5 videos selected (minimum score 80/100)
- [ ] Selection reasoning documented
- [ ] Priority order assigned

**Documentation:**
- [ ] Research results document created
- [ ] All selected videos fully documented
- [ ] Video URLs collected and verified
- [ ] Research file saved with proper naming

**Handoff to Stage 2:**
- [ ] Videos assigned to team members (if applicable)
- [ ] Deadlines communicated
- [ ] Research results shared with team

---

### Stage 1 Output

**Primary Deliverable:**
`Research_Results_YYYY-MM-DD_[Focus_Area].md`

**Contents:**
- 8-12 scored videos with full breakdown
- Top 3-5 selected videos (scores 80+)
- Video metadata (URL, title, creator, date, duration)
- Relevance justification for each selected video
- Department assignments
- Implementation priorities

**Handoff to Stage 2:**
- Video URLs for top 3-5 videos
- Relevance scores and priority levels
- Key topics identified in each video
- Expected value/outcomes from processing

---

**Stage 1 Complete! Ready for Stage 2 Processing.**

---

# PART 3: STAGE 2 - PROCESSING (FULL)

## STAGE 2: Video Transcription - Complete Instructions v3.2

### Overview

**Goal**: Transform video content into structured, taxonomy-ready data

**Time**: 40-80 minutes per video (includes transcription + extraction)

**Output**: Complete markdown document with 14 taxonomy sections

**Version**: 3.2 (November 2025)

**Major Features:**
- Direct extraction of Task Templates, Step Templates, Project Templates
- Enhanced skills extraction with task linkage
- Reusability analysis
- Success metrics & performance data capture
- 90-95% time savings vs manual processing

---

### 🔴 CRITICAL OUTPUT REQUIREMENT

**MUST OUTPUT COMPLETE STRUCTURED MARKDOWN DOCUMENT**

❌ **DO NOT** output JSON, plain text, or any other format
✅ **REQUIRED FORMAT:** Markdown (.md) with sections below
✅ **FILE EXTENSION:** .md (not .json, .txt)

**Validation:**
- Document starts with `#` heading
- No JSON curly braces `{}` at document start
- All sections use markdown headers (`##`, `###`)
- Tables use markdown table format
- Lists use markdown bullet points

---

### Technical Requirements

**Format:** Markdown (.md) only - NOT JSON, NOT plain text
**Encoding:** UTF-8
**Special Characters:** If $ or currency symbols cause corruption, write out full words ("five point six million")
**Quality Check:** If text appears character-by-character (e.g., "h e l l o"), re-process that section

---

### Tools for Transcription

**Primary: Google AI Studio**
- Best for: Videos under ~100 MB
- Pros: Fast, accurate, handles multiple languages
- Cons: Size limitations
- URL: https://aistudio.google.com/

**Alternative: Transcribe AI**
- Best for: Larger videos exceeding Google AI Studio limits
- Pros: No size limit, good accuracy
- Cons: May be slower

**Local Alternative: Whisper**
- Best for: When cloud services unavailable
- Pros: Complete privacy, no limits
- Cons: Requires local setup, slower

---

## Core Transcription Structure

### Section 1: Metadata

```markdown
# Video Transcription: [Exact Video Title]

## Metadata

- **Video Title**: [Extract exact title from video]
- **Channel/Creator**: [Channel name]
- **Video URL**: [Full YouTube URL]
- **Duration**: [HH:MM:SS or MM:SS]
- **Publication Date**: [YYYY-MM-DD]
- **Transcription Date**: [YYYY-MM-DD]
- **Transcribed By**: [Tool used: Google AI Studio / Transcribe AI / Whisper]
- **Instructions Version**: v3.2
```

---

### Section 2: Description

```markdown
## Video Description

### Full Description
[Paste or extract the complete video description as provided by the creator]

### Key Topics Covered
- [Main topic 1]
- [Main topic 2]
- [Main topic 3]
- [Main topic 4]
- [Continue for all major topics]

### Links Referenced in Video
- [Link 1 with description of what it links to]
- [Link 2 with description]
- [Link 3 with description]
- [GitHub repos, tool URLs, documentation, etc.]
```

---

### Section 3: Word-for-Word Transcription

**Requirements:**
- Transcribe exactly as spoken
- Include verbal fillers ("um", "uh", "you know") for accuracy
- Mark timestamps every 30-60 seconds OR at topic changes
- Label speakers if multiple people
- Capture on-screen text in `[TEXT: content]` format
- Note visual demonstrations in `[VISUAL: description]` format

**Format:**

```markdown
## Word-for-Word Transcription

### [00:00 - 00:45] Introduction

[Speaker 1]: Hey everyone, welcome back to the channel. Today I'm going to show you how to automate your workflow using Claude and MCP connectors. [TEXT: "Building MCP Servers" shown on screen] This is going to be a complete step-by-step tutorial, and by the end, you'll have a working connector that can automate your email drafts.

[VISUAL: Screen shows VS Code with an empty project folder]

So let's jump right in. First thing you need is...

### [00:45 - 01:30] Prerequisites and Setup

[Speaker 1]: ...Node.js installed on your machine. I'm using version 18, but anything above 16 should work fine. You also need Claude Desktop installed. [VISUAL: Shows Claude Desktop application icon] If you don't have it yet, um, you can download it from anthropic.com.

[TEXT: "Prerequisites: Node.js 16+, Claude Desktop" appears on screen]

Next, we'll need to create a new project folder...

[Continue transcription with timestamps every 30-60 seconds or at topic changes]
```

**Important Notes:**
- Timestamps: Use [MM:SS] format for videos under 1 hour, [HH:MM:SS] for longer videos
- Speaker labels: Use [Speaker 1], [Speaker 2] or [Creator], [Guest] if names unknown
- On-screen text: Always capture in [TEXT: ...] format
- Visual cues: Important demonstrations in [VISUAL: ...] format
- Accuracy: Include verbal fillers for authenticity, but prioritize clarity

---

## TAXONOMY EXTRACTION REQUIREMENTS

**Purpose**: Extract structured data that maps directly to our taxonomy framework

**Critical**: These sections enable 90-95% time savings in post-processing

---

## TAXONOMY NAMING CONVENTIONS

**⚠️ CRITICAL: All extracted elements MUST follow these naming conventions**

### Task Template Names

**Format:** `ACTION_OBJECT_CONTEXT`

**Rules:**
- ALL_CAPS with underscores
- ACTION: One verb from categories A-G (see Section 5)
- OBJECT: Plural noun from Objects section (Section 9)
- CONTEXT: Distinguishing details (method, tool, source, purpose)

**Examples:**
```
✅ CORRECT:
- ENRICH_LEADS_MULTI-SOURCE
- SCRAPE_COMPANIES_FROM_GOOGLE
- GENERATE_CONNECTOR_VIA_MCP-BUILDER
- AUTOMATE_EMAILS_MORNING-DRAFTS
- BUILD_DASHBOARD_REAL-TIME-ANALYTICS

❌ INCORRECT:
- enrichLeadsMultiSource (not ALL_CAPS)
- ENRICH_LEAD (object should be plural)
- ENRICH (missing object and context)
- scrape companies (spaces, not underscores)
```

### Step Template Names

**Format:** `ACTION_OBJECT_SPECIFIC_DETAIL`

**Rules:**
- ALL_CAPS with underscores
- Include tool/method in name for clarity
- More specific than task names

**Examples:**
```
✅ CORRECT:
- SCRAPE_COMPANY_DATA_FROM_AIRSCALE
- EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW
- UPLOAD_CSV_TO_ANYMAILFINDER
- CONFIGURE_OAUTH_IN_GOOGLE_CLOUD
- INSTALL_DEPENDENCIES_VIA_NPM

❌ INCORRECT:
- SCRAPE_DATA (too generic, which data?)
- scrape_company_data (not ALL_CAPS)
- SCRAPE (missing object and detail)
```

### Skill Phrases

**Format:** `"[past tense action] [object] via [tool]"`

**Rules:**
- Lowercase, natural language
- ALWAYS include tool name
- Use past participle form of action verb

**Examples:**
```
✅ CORRECT:
- "enriched emails via Anymailfinder"
- "scraped lead lists via Apify"
- "generated MCP connectors via Claude"
- "deployed connectors via Cursor"
- "built automation workflows via n8n"

❌ INCORRECT:
- "Enriched Emails Via Anymailfinder" (capitalized)
- "enrich emails" (not past tense, missing tool)
- "enriched via Anymailfinder" (missing object)
- "enriched emails" (missing tool)
```

### Project Template Names

**Format:** `Descriptive_Name_Campaign/System/Initiative`

**Rules:**
- Title_Case with underscores
- Include project type suffix

**Examples:**
```
✅ CORRECT:
- Lead_Generation_Campaign
- MCP_Automation_Stack_Setup
- Enterprise_ABM_Campaign
- Video_Production_Pipeline_System

❌ INCORRECT:
- lead_generation_campaign (not Title_Case)
- LEAD_GENERATION_CAMPAIGN (not Title_Case, too caps)
- LeadGenerationCampaign (no underscores)
```

---

## Section 4: Workflows Identification

**Purpose**: Identify and extract all workflows/processes mentioned in video

**Format for Each Workflow:**

```markdown
## Workflows Identified

### WORKFLOW 1: [Workflow Name - Descriptive]

**DEPARTMENT:** [Primary department that performs this workflow]

**CROSS_DEPT_PATTERN:** [If cross-department, describe handoff pattern - OPTIONAL]
- [Department A] does [phase/task] then hands off to [Department B] via [method]
- Example: Sales generates leads, Operations configures automation, Sales runs campaigns

**OBJECTIVE:** [What this workflow achieves - one clear sentence]

**STEPS:**
1. [Action verb] + [object/deliverable] - [brief detail]
2. [Action verb] + [object/deliverable] - [brief detail]
3. [Action verb] + [object/deliverable] - [brief detail]
4. [Continue for all steps...]

**DURATION:** [Time estimate if mentioned in video]
- Example: "10-15 minutes for 40 records, scalable to thousands"
- Example: "2-3 hours one-time setup, then automated"

**COMPLEXITY:** [Low / Medium / High / Very High]

**TOOLS USED:** [List all tools mentioned in this workflow]
- [Tool 1]
- [Tool 2]
- [Tool 3]

**INPUT:** [What you start with]

**OUTPUT:** [What you end with - be specific]

**TIMESTAMP:** [Where this workflow is explained in video: MM:SS - MM:SS]
```

**Example 1:**

```markdown
### WORKFLOW 1: Multi-Source Lead Enrichment Pipeline

**DEPARTMENT:** Sales / AI (Lead Generation)

**OBJECTIVE:** Generate enriched lead lists from multiple data sources with email validation

**STEPS:**
1. Scrape company data from search platform (location, size, keywords)
2. Extract company domains using automated workflow
3. Export results to CSV format
4. Import CSV to email enrichment service
5. Enrich with nominative email patterns (firstname@domain.com variations)
6. Validate email deliverability
7. Download enriched list with verified contacts

**DURATION:** 10-15 minutes for 40 records, scalable to thousands

**COMPLEXITY:** Medium

**TOOLS USED:**
- Airscale
- Anymailfinder
- LinkedIn Sales Navigator
- Google Sheets

**INPUT:** Search criteria (industry, geography, company size, job titles)

**OUTPUT:** CSV with company data + verified decision-maker emails, names, LinkedIn URLs, roles

**TIMESTAMP:** [05:30 - 12:45]
```

**Example 2:**

```markdown
### WORKFLOW 2: Stacked Connector Post-Meeting Automation

**DEPARTMENT:** Operations (Cross-department: Sales, Customer Success)

**CROSS_DEPT_PATTERN:**
- Operations drops meeting transcript (trigger)
- Claude extracts insights and attendees (Operations)
- Gmail drafts follow-up email (Sales/CS collaboration)
- CRM updates meeting notes and wins (Sales owns CRM)

**OBJECTIVE:** Automate all post-meeting follow-up tasks using stacked MCP connectors

**STEPS:**
1. Drop meeting transcript into Claude Desktop
2. Extract action items, decisions, client wins, and attendees
3. Draft personalized follow-up email
4. Update CRM with meeting notes and wins
5. Set calendar reminder for next action

**DURATION:** 1-4 minutes (automated), saves 15+ hours/week

**COMPLEXITY:** Very High (but automated)

**TOOLS USED:**
- Claude Desktop
- Gmail MCP connector
- Calendar MCP connector
- CRM connector (HubSpot/Salesforce)

**INPUT:** Meeting transcript (text file or audio transcription)

**OUTPUT:** Follow-up email drafted, CRM updated, reminders set

**TIMESTAMP:** [18:20 - 24:50]
```

---

## Section 4B: Task Templates Extraction ⭐ NEW IN V3.2

**Purpose**: Extract reusable Task Templates that can be used across projects

**Key Concept**: Task Templates are building blocks. One Task Template can be used in multiple workflows and projects.

**When to Extract**: For each workflow identified in Section 4, extract 1-3 reusable Task Templates

**Format:**

```markdown
## Task Templates Extraction

### TASK 1: [ACTION]_[OBJECT]_[CONTEXT]

**TASK_ID:** TBD [Will be assigned during taxonomy integration]

**DEPARTMENT:** [Primary department that performs this task]

**ACTION:** [Single verb from categories A-G - see Section 5]

**OBJECT:** [Deliverable/output - use plural from Section 9]

**CONTEXT:** [Distinguishing details - method, source, tool, purpose]

**COMPLEXITY:** [Low / Medium / High / Very High]

**TIME_ESTIMATE:** [Typical duration from workflow data]

**PARENT_PROJECT:** [If part of larger project, name it - OPTIONAL]

**STEPS_USED:** [Reference Step Templates from Section 4C]
- [STEP_NAME_1]
- [STEP_NAME_2]
- [STEP_NAME_3]
- [Continue...]

**SKILLS_REQUIRED:** [Reference skills from Section 7B]
- "[skill phrase 1 via tool]"
- "[skill phrase 2 via tool]"
- [Continue...]

**TOOLS:** [Primary tools used in this task]
- [Tool 1]
- [Tool 2]

**INPUT:** [What you start with]

**OUTPUT:** [What task produces]

**SUCCESS_CRITERIA:** [How to know task completed successfully]

**REUSABLE_IN:** [Other contexts where this Task Template could apply]
- [Context 1]
- [Context 2]
- [Context 3]

**TIMESTAMP:** [Where demonstrated in video: MM:SS - MM:SS]
```

**Example 1:**

```markdown
### TASK 1: ENRICH_LEADS_MULTI-SOURCE

**TASK_ID:** TBD

**DEPARTMENT:** Sales / AI (Lead Generation)

**ACTION:** Enrich

**OBJECT:** Leads

**CONTEXT:** Multi-source with email validation

**COMPLEXITY:** Medium

**TIME_ESTIMATE:** 10-15 minutes for 40 records

**PARENT_PROJECT:** Lead_Generation_Campaign

**STEPS_USED:**
- SCRAPE_COMPANY_DATA_FROM_AIRSCALE
- EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW
- EXPORT_DATA_TO_CSV
- UPLOAD_CSV_TO_ANYMAILFINDER
- EXECUTE_DECISION-MAKER_SEARCH
- VALIDATE_EMAIL_DELIVERABILITY
- DOWNLOAD_ENRICHED_RESULTS

**SKILLS_REQUIRED:**
- "enriched emails via Anymailfinder"
- "scraped lead lists via Apify"

**TOOLS:**
- Airscale
- Anymailfinder
- Google Sheets

**INPUT:** Search criteria (industry, location, company size)

**OUTPUT:** CSV with verified decision-maker emails

**SUCCESS_CRITERIA:** 80%+ email enrichment rate, emails verified as deliverable

**REUSABLE_IN:**
- Enterprise prospecting campaigns
- Local business outreach
- Partnership development
- Customer win-back campaigns
- Event attendee outreach

**TIMESTAMP:** [05:30 - 12:45]
```

**Example 2:**

```markdown
### TASK 2: GENERATE_CONNECTOR_VIA_MCP-BUILDER

**TASK_ID:** TBD

**DEPARTMENT:** Development / AI

**ACTION:** Generate

**OBJECT:** MCP Connector

**CONTEXT:** Via MCP-Builder skill

**COMPLEXITY:** Very High (automated by skill to 30-60 sec)

**TIME_ESTIMATE:** 30-60 seconds generation time

**PARENT_PROJECT:** MCP_Automation_Stack_Setup

**STEPS_USED:**
- ENABLE_CLAUDE_SKILLS
- WRITE_CONNECTOR_REQUIREMENTS
- EXECUTE_MCP-BUILDER_GENERATION
- REVIEW_GENERATED_CODE
- SAVE_CONNECTOR_FILES

**SKILLS_REQUIRED:**
- "generated MCP connectors via Claude"
- "configured OAuth for Google APIs"

**TOOLS:**
- Claude Desktop
- MCP Builder Skill

**INPUT:** 2-sentence connector requirements prompt

**OUTPUT:** Complete MCP server code with OAuth, API handlers, error handling

**SUCCESS_CRITERIA:** Code generated successfully, 95%+ success rate, passes basic tests

**REUSABLE_IN:**
- Gmail connector generation
- Calendar connector generation
- CRM connector generation
- Any Google API MCP connector
- Custom app connectors

**TIMESTAMP:** [14:20 - 18:50]
```

**Extraction Guidelines:**
- Extract ONE Task Template per distinct workflow or major workflow phase
- Use ACTION_OBJECT_CONTEXT naming consistently (ALL_CAPS with underscores)
- If workflow has 5+ steps, consider if it should be multiple tasks
- Link to Step Templates (Section 4C) and skills (Section 7B)
- Always identify reusability contexts (where else could this be used?)

---

## Section 4C: Step Templates Extraction ⭐ NEW IN V3.2

**Purpose**: Extract reusable individual steps that can be used across multiple tasks

**Key Concept**: Steps are atomic actions. The same step (like "SCRAPE_COMPANY_DATA_FROM_AIRSCALE") might be used in 5 different Task Templates.

**When to Extract**: For each step within workflows/tasks, create standalone Step Template

**Format:**

```markdown
## Step Templates Extraction

### STEP 1: [ACTION]_[OBJECT]_[SPECIFIC_DETAIL]

**STEP_ID:** TBD [Will be assigned during taxonomy integration]

**ACTION:** [Verb from A-G categories]

**OBJECT:** [What this step acts upon]

**TOOL:** [Primary tool used for this step]

**PARENT_TASKS:** [All tasks that use this step - reference Section 4B]
- [TASK_NAME_1]
- [TASK_NAME_2]
- [Continue...]

**COMPLEXITY:** [Low / Medium / High]

**TIME_ESTIMATE:** [Time for this specific step]

**INPUT:** [What this step receives]

**OUTPUT:** [What this step produces]

**PREREQUISITES:** [What must be completed/configured before this step]
- [Prerequisite 1]
- [Prerequisite 2]

**INSTRUCTIONS:** [Brief how-to for this step - 3-8 bullet points]
1. [Instruction 1]
2. [Instruction 2]
3. [Instruction 3]
4. [Continue...]

**REUSABLE_IN:** [Other tasks/workflows where this step could be used]
- [Context 1]
- [Context 2]
- [Context 3]

**TIMESTAMP:** [Where demonstrated in video: MM:SS - MM:SS]
```

**Example 1:**

```markdown
### STEP 1: SCRAPE_COMPANY_DATA_FROM_AIRSCALE

**STEP_ID:** TBD

**ACTION:** Scrape

**OBJECT:** Company Data

**TOOL:** Airscale

**PARENT_TASKS:**
- ENRICH_LEADS_MULTI-SOURCE
- GENERATE_ENTERPRISE_EMAIL_LISTS
- BUILD_TAM_ANALYSIS

**COMPLEXITY:** Low

**TIME_ESTIMATE:** 2-3 minutes

**INPUT:** Search criteria (location, company size, keywords)

**OUTPUT:** Company list table with names, LinkedIn URLs

**PREREQUISITES:**
- Airscale account configured
- Search criteria defined
- Budget allocated for credits

**INSTRUCTIONS:**
1. Navigate to Airscale platform (airscale.ai)
2. Set location filter (e.g., "California")
3. Set company size filter (e.g., "11-50 employees")
4. Enter keywords in search (e.g., "AI agency")
5. Click "Preview Companies" to verify results match criteria
6. Review sample companies in preview
7. Click "Load all companies to table" to execute search

**REUSABLE_IN:**
- Any task requiring company list generation
- Market research projects
- Competitive intelligence gathering
- TAM (Total Addressable Market) analysis
- Partner identification

**TIMESTAMP:** [06:15 - 07:45]
```

**Example 2:**

```markdown
### STEP 2: CONFIGURE_OAUTH_IN_GOOGLE_CLOUD

**STEP_ID:** TBD

**ACTION:** Configure

**OBJECT:** OAuth Credentials

**TOOL:** Google Cloud Console

**PARENT_TASKS:**
- GENERATE_CONNECTOR_VIA_MCP-BUILDER
- DEPLOY_GMAIL_MCP_CONNECTOR
- SETUP_CALENDAR_AUTOMATION

**COMPLEXITY:** Medium

**TIME_ESTIMATE:** 10-15 minutes (one-time setup)

**INPUT:** Google Cloud project name, API requirements

**OUTPUT:** OAuth 2.0 client ID and client secret

**PREREQUISITES:**
- Google Cloud Console account
- API enabled (Gmail API or Calendar API)
- Project created in Google Cloud

**INSTRUCTIONS:**
1. Navigate to Google Cloud Console (console.cloud.google.com)
2. Create new project or select existing project
3. Enable required API (Gmail or Calendar) via API Library
4. Go to "Credentials" section in left sidebar
5. Click "Create Credentials" → "OAuth 2.0 Client ID"
6. Configure consent screen (application name, scopes) if first time
7. Select application type: "Desktop app"
8. Copy Client ID and Client Secret to secure location

**REUSABLE_IN:**
- Any Google API MCP connector setup
- Gmail automation workflows
- Calendar automation workflows
- Drive automation workflows
- Any OAuth-based Google integration

**TIMESTAMP:** [15:30 - 17:45]
```

**Extraction Guidelines:**
- Extract EVERY distinct step from workflows (typically 4-10 steps per workflow)
- Each step should be atomic (one clear action with one tool)
- Include tool name in step name for clarity
- Always document prerequisites (what's needed before this step)
- Link to parent tasks (which tasks use this step)
- Identify cross-task reusability

---

## Section 4D: Project Templates Extraction ⭐ NEW IN V3.2

**Purpose**: Extract hierarchical project structures when video describes multi-phase projects

**When to Extract**: ONLY if video shows:
- Multi-phase workflow spanning days/weeks
- Clear sequential phases with milestones
- Cross-department collaboration
- Complex campaigns with multiple outcomes

**Format:**

```markdown
## Project Templates Extraction

### PROJECT 1: [PROJECT_NAME]

**PROJECT_ID:** TBD [Will be assigned during taxonomy integration]

**DEPARTMENT:** [Primary department, note if cross-department]

**DESCRIPTION:** [What this project achieves end-to-end]

**DURATION:** [Total project timeline if mentioned]

**COMPLEXITY:** [Low / Medium / High / Very High]

**COST_ESTIMATE:** [If mentioned in video]

**ROI_ESTIMATE:** [If mentioned - time savings, revenue impact, cost savings]

---

#### PHASE 1: [Phase Name]

**DESCRIPTION:** [What this phase accomplishes]

**DURATION:** [Phase timeline]

**OUTPUT:** [What's delivered at phase end]

##### MILESTONE: [Milestone Name]

**DESCRIPTION:** [What this milestone achieves]

**DELIVERABLE:** [Specific output]

**TASKS:**
- **TASK:** [Task name from Section 4B] (TIME: [duration])
  - **STEPS:** [Step names from Section 4C]
    - [STEP_NAME_1]
    - [STEP_NAME_2]
    - [Continue...]

- **TASK:** [Next task]
  - **STEPS:** [Steps]

##### MILESTONE: [Next milestone]

[Continue for all milestones in phase]

---

#### PHASE 2: [Next Phase]

[Continue structure for all phases]

---

**CROSS_DEPARTMENT_COLLABORATION:**
- [Department A] does [phase/task] then hands off to [Department B] via [method]
- [Example: Sales generates leads, Operations configures automation, Sales runs campaigns]

**TIMESTAMP:** [Where project is described in video: MM:SS - MM:SS]
```

**Example:**

```markdown
### PROJECT 1: Lead_Generation_Campaign

**PROJECT_ID:** TBD

**DEPARTMENT:** Sales / AI (Cross-department with Operations for automation)

**DESCRIPTION:** Generate and enrich qualified lead lists for outbound sales campaigns with automated follow-up

**DURATION:** 1-2 weeks for setup, ongoing operation

**COMPLEXITY:** High

**COST_ESTIMATE:** $5-50 (email enrichment costs)

**ROI_ESTIMATE:** 15-20+ hours/week saved after automation setup

---

#### PHASE 1: Data Sourcing

**DESCRIPTION:** Identify and collect target company/contact information

**DURATION:** 1-3 days

**OUTPUT:** 2,000+ raw leads with company data

##### MILESTONE: Identify Target Companies

**DESCRIPTION:** Build list of companies matching ICP criteria

**DELIVERABLE:** Company list with 2,000+ entries

**TASKS:**
- **TASK:** SCRAPE_COMPANIES_FROM_GOOGLE (TIME: 20-30 min)
  - **STEPS:**
    - SCRAPE_COMPANY_DATA_FROM_AIRSCALE
    - EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW
    - EXPORT_DATA_TO_CSV

---

#### PHASE 2: Email Enrichment

**DESCRIPTION:** Find and validate email addresses for all leads

**DURATION:** 1-2 days

**OUTPUT:** Lead list with 80%+ emails verified

##### MILESTONE: Nominative Enrichment

**DESCRIPTION:** Generate emails using name + domain patterns

**DELIVERABLE:** CSV with decision-maker emails

**TASKS:**
- **TASK:** ENRICH_LEADS_MULTI-SOURCE (TIME: 10-15 min per batch)
  - **STEPS:**
    - UPLOAD_CSV_TO_ANYMAILFINDER
    - EXECUTE_DECISION-MAKER_SEARCH
    - VALIDATE_EMAIL_DELIVERABILITY
    - DOWNLOAD_ENRICHED_RESULTS

---

#### PHASE 3: Automation Setup

**DESCRIPTION:** Configure MCP automation for outreach and follow-up

**DURATION:** 3-4 hours (one-time setup)

**OUTPUT:** Automated email and meeting follow-up system

##### MILESTONE: Email Automation Operational

**DESCRIPTION:** Morning email drafts automated

**DELIVERABLE:** 5-10 hours/week saved

**TASKS:**
- **TASK:** GENERATE_CONNECTOR_VIA_MCP-BUILDER (TIME: 60 sec)
  - **STEPS:**
    - ENABLE_CLAUDE_SKILLS
    - WRITE_CONNECTOR_REQUIREMENTS
    - EXECUTE_MCP-BUILDER_GENERATION

- **TASK:** DEPLOY_GMAIL_MCP_CONNECTOR (TIME: 5 min)
  - **STEPS:**
    - CONFIGURE_OAUTH_IN_GOOGLE_CLOUD
    - INSTALL_CONNECTOR_LOCALLY
    - TEST_CONNECTION

- **TASK:** AUTOMATE_EMAILS_MORNING-DRAFTS (TIME: 15-20 min)
  - **STEPS:**
    - CONFIGURE_GMAIL_MCP_CONNECTOR
    - DEFINE_AUTOMATION_RULES
    - TEST_DRAFT_GENERATION

---

**CROSS_DEPARTMENT_COLLABORATION:**
- Sales/AI owns Phases 1-2 (sourcing and enrichment)
- Development assists Phase 3 (MCP connector setup)
- Operations owns Phase 3 ongoing (automation configuration and maintenance)
- Sales uses Phase 3 output (automated drafts) for daily operations

**TIMESTAMP:** [10:00 - 28:45] (spans most of video)
```

**Extraction Guidelines:**
- Only extract project structure if video shows clear multi-phase workflow
- Each phase should have 1-3 milestones
- Each milestone should have 1-5 tasks
- Reference Task Templates from Section 4B by name
- Reference Step Templates from Section 4C by name
- Document cross-department collaboration patterns explicitly
- Include ROI/cost estimates if mentioned in video

---

## Section 5: Action Verbs & Operations

**Purpose**: Extract and categorize ALL action verbs mentioned in video

**Why Important**: Action verbs map to taxonomy actions and are used in task naming

**Format:**

```markdown
## Action Verbs & Operations

### A. CREATION VERBS (Making new things)

**Verbs Found:**
- Create ([X] times) - [Timestamps where mentioned]
- Generate ([X] times) - [Timestamps]
- Design ([X] times) - [Timestamps]
- Build ([X] times) - [Timestamps]
- Develop ([X] times) - [Timestamps]
- Draft ([X] times) - [Timestamps]
- Produce ([X] times) - [Timestamps]
- Craft ([X] times) - [Timestamps]
- Compose ([X] times) - [Timestamps]
- [Add others found]

### B. MODIFICATION VERBS (Changing existing things)

**Verbs Found:**
- Edit ([X] times) - [Timestamps]
- Refine ([X] times) - [Timestamps]
- Optimize ([X] times) - [Timestamps]
- Enhance ([X] times) - [Timestamps]
- Update ([X] times) - [Timestamps]
- Revise ([X] times) - [Timestamps]
- Improve ([X] times) - [Timestamps]
- Adjust ([X] times) - [Timestamps]
- Customize ([X] times) - [Timestamps]
- [Add others found]

### C. ANALYSIS VERBS (Understanding/Evaluating)

**Verbs Found:**
- Analyze ([X] times) - [Timestamps]
- Review ([X] times) - [Timestamps]
- Evaluate ([X] times) - [Timestamps]
- Research ([X] times) - [Timestamps]
- Assess ([X] times) - [Timestamps]
- Examine ([X] times) - [Timestamps]
- Test ([X] times) - [Timestamps]
- Compare ([X] times) - [Timestamps]
- Verify ([X] times) - [Timestamps]
- [Add others found]

### D. ORGANIZATION VERBS (Structuring/Managing)

**Verbs Found:**
- Organize ([X] times) - [Timestamps]
- Structure ([X] times) - [Timestamps]
- Categorize ([X] times) - [Timestamps]
- Schedule ([X] times) - [Timestamps]
- Plan ([X] times) - [Timestamps]
- Coordinate ([X] times) - [Timestamps]
- Prioritize ([X] times) - [Timestamps]
- Arrange ([X] times) - [Timestamps]
- [Add others found]

### E. COMMUNICATION VERBS (Sharing/Presenting)

**Verbs Found:**
- Present ([X] times) - [Timestamps]
- Share ([X] times) - [Timestamps]
- Publish ([X] times) - [Timestamps]
- Export ([X] times) - [Timestamps]
- Deliver ([X] times) - [Timestamps]
- Communicate ([X] times) - [Timestamps]
- Report ([X] times) - [Timestamps]
- Demonstrate ([X] times) - [Timestamps]
- [Add others found]

### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)

**Verbs Found:**
- Take over ([X] times) - [Timestamps]
- Control ([X] times) - [Timestamps]
- Automate ([X] times) - [Timestamps]
- Execute ([X] times) - [Timestamps]
- Open ([X] times) - [Timestamps]
- Click ([X] times) - [Timestamps]
- Close ([X] times) - [Timestamps]
- Scroll ([X] times) - [Timestamps]
- Navigate ([X] times) - [Timestamps]
- Fill in ([X] times) - [Timestamps]
- Hover ([X] times) - [Timestamps]
- Submit ([X] times) - [Timestamps]
- Add ([X] times) - [Timestamps]
- Import ([X] times) - [Timestamps]
- Migrate ([X] times) - [Timestamps]
- Interact ([X] times) - [Timestamps]
- [Add others found]

**Note**: Captures action verbs specific to AI agents, browser automation tools, RPA systems.

### G. DATA OPERATIONS (Processing, Transforming, Moving Data)

**Verbs Found:**
- Scrape ([X] times) - [Timestamps]
- Parse ([X] times) - [Timestamps]
- Extract ([X] times) - [Timestamps]
- Feed ([X] times) - [Timestamps]
- Import ([X] times) - [Timestamps]
- Upload ([X] times) - [Timestamps]
- Download ([X] times) - [Timestamps]
- Export ([X] times) - [Timestamps]
- Enrich ([X] times) - [Timestamps]
- Validate ([X] times) - [Timestamps]
- Verify ([X] times) - [Timestamps]
- Deduplicate ([X] times) - [Timestamps]
- Sanitize ([X] times) - [Timestamps]
- Trim ([X] times) - [Timestamps]
- Filter ([X] times) - [Timestamps]
- Transform ([X] times) - [Timestamps]
- Convert ([X] times) - [Timestamps]
- Merge ([X] times) - [Timestamps]
- Split ([X] times) - [Timestamps]
- Combine ([X] times) - [Timestamps]
- Map ([X] times) - [Timestamps]
- Match ([X] times) - [Timestamps]
- Lookup ([X] times) - [Timestamps]
- [Add others found]

**Note**: ETL operations, data enrichment, data quality processes.
```

**Categorization Rules:**
- **Creation**: Brings something new into existence
- **Modification**: Changes something that already exists
- **Analysis**: Evaluates or understands something
- **Organization**: Arranges or structures information
- **Communication**: Shares or presents information
- **Browser/Agentic**: AI agent and automation specific actions
- **Data Operations**: Processing, moving, transforming data

---

## Section 6: Task Chains

**Purpose**: Identify sequential task chains (multi-step processes with clear flow)

**Format:**

```markdown
## Task Chains

### TASK CHAIN 1: [Name of Chain]

**SEQUENCE:**
[Step 1] → [Step 2] → [Step 3] → [Step 4] → [Output]

**PURPOSE:** [What this chain accomplishes]

**AUTOMATION LEVEL:** [Manual / Semi-automated / Fully automated]

**TIMESTAMP:** [Where mentioned: MM:SS - MM:SS]

**Example:**
TASK CHAIN 1: Automated Documentary Creation
**SEQUENCE:**
Research topic (Perplexity) → Generate script (AI) → Create video (VAYU+Seedream) → Add voiceover (Eleven Labs) → Review & publish

**PURPOSE:** End-to-end documentary production without manual video editing

**AUTOMATION LEVEL:** Fully automated (via GLIF agent)

**TIMESTAMP:** [06:15 - 08:45]
```

---

## Section 7: Responsibilities Vocabulary

### Section 7A: Professional Roles Mentioned

```markdown
## Professional Roles Mentioned

- [Role 1]: [Context from video - how role is described]
- [Role 2]: [Context]
- [Role 3]: [Context]
- [Continue for all roles mentioned]

**Example:**
- Content Creator: Creates videos, thumbnails, and social media content using AI tools
- Video Producer: Orchestrates multi-tool workflows for documentary production
- Social Media Manager: Optimizes content for platforms (TikTok, Instagram, YouTube)
- Prompt Engineer: Refines AI prompts for optimal output quality
```

---

### Section 7B: Skills Extraction (Responsibility + Tool Format) ⭐ ENHANCED IN V3.2

**Purpose**: Extract skills with task linkage to enable skill-based task assignment

**Key Concept**: Skills link people to tasks. When someone has "enriched emails via Anymailfinder" skill, they can execute ENRICH_LEADS_MULTI-SOURCE task.

**Format:**

```markdown
## Skills Extraction

### SKILL 1: [ACTION]_[OBJECT]_VIA_[TOOL]

**SKILL_ID:** TBD [Will be assigned during taxonomy integration]

**SKILL_PHRASE:** "[action in past tense] [object] via [tool]"

**DIFFICULTY:** [Beginner / Intermediate / Advanced / Expert]

**PROFESSIONS:** [Roles that use this skill]
- [Profession 1]
- [Profession 2]

**PARENT_TASKS:** [Tasks that require this skill - reference Section 4B]
- [TASK_NAME_1]
- [TASK_NAME_2]

**WORKFLOWS:** [Workflows where this skill is used - reference Section 4]
- [Workflow Name 1]
- [Workflow Name 2]

**TOOLS_REQUIRED:** [Tools needed for this skill]
- [Tool 1]
- [Tool 2]

**TIME_TO_LEARN:** [If mentioned or estimable]

**DESCRIPTION:** [Brief explanation of what this skill enables]

**TIMESTAMP:** [Where skill is demonstrated: MM:SS - MM:SS]
```

**Example 1:**

```markdown
### SKILL 1: ENRICH_EMAILS_VIA_ANYMAILFINDER

**SKILL_ID:** TBD

**SKILL_PHRASE:** "enriched emails via Anymailfinder"

**DIFFICULTY:** Beginner

**PROFESSIONS:**
- Lead Generator
- SDR (Sales Development Representative)
- Sales Development Representative

**PARENT_TASKS:**
- ENRICH_LEADS_MULTI-SOURCE
- GENERATE_ENTERPRISE_EMAIL_LISTS
- VALIDATE_LINKEDIN_EXPORTS

**WORKFLOWS:**
- Multi-Source Lead Enrichment Pipeline
- Enterprise Email Discovery
- LinkedIn Export Enhancement

**TOOLS_REQUIRED:**
- Anymailfinder
- CSV/spreadsheet tool (Excel, Google Sheets)

**TIME_TO_LEARN:** 15-30 minutes

**DESCRIPTION:** Ability to use Anymailfinder's nominative enrichment to find decision-maker emails from company domains and names. Includes bulk upload, decision-maker search configuration, and result download. Achieves 20-100% success rate depending on source quality at $0.0025 per valid email found.

**TIMESTAMP:** [07:30 - 10:15]
```

**Example 2:**

```markdown
### SKILL 2: GENERATE_MCP_CONNECTORS_VIA_CLAUDE

**SKILL_ID:** TBD

**SKILL_PHRASE:** "generated MCP connectors via Claude"

**DIFFICULTY:** Intermediate

**PROFESSIONS:**
- AI Engineer
- Backend Developer
- Automation Engineer

**PARENT_TASKS:**
- GENERATE_CONNECTOR_VIA_MCP-BUILDER
- BUILD_GMAIL_AUTOMATION
- CREATE_CALENDAR_INTEGRATION

**WORKFLOWS:**
- MCP Connector Generation
- Email Automation Setup
- Stacked Connector Configuration

**TOOLS_REQUIRED:**
- Claude Desktop
- MCP Builder Skill
- Node.js

**TIME_TO_LEARN:** 10-20 minutes (skill exists, just needs enabling)

**DESCRIPTION:** Ability to use Claude's MCP Builder skill to generate production-ready MCP connector code in 30-60 seconds with 2-sentence prompts. Revolutionary speed compared to 2-4 hours manual coding. Generates complete OAuth integration, API handlers, error handling. 95%+ success rate.

**TIMESTAMP:** [14:20 - 18:50]
```

**Extraction Guidelines:**
- Extract skills in "action via tool" format consistently (lowercase, natural language)
- Link skills to tasks (which tasks require this skill?)
- Link skills to workflows (where is this skill used?)
- Always include difficulty level (helps with training path planning)
- Include time-to-learn if mentioned or estimable
- Capture ROI metrics if mentioned (cost savings, time savings, success rates)

---

### Section 7C: Responsibilities/Activities

```markdown
## Responsibilities/Activities

- "[Activity phrase 1]" - [Timestamp]
- "[Activity phrase 2]" - [Timestamp]
- "[Activity phrase 3]" - [Timestamp]
- [Continue for all responsibility phrases - use exact wording from video]

**Example:**
- "creating engaging thumbnails" [02:34]
- "editing videos" [02:45]
- "optimizing for CTR" [03:20]
- "automating content workflows" [08:45]
- "generating miniature documentaries" [06:20]
- "managing social media content" [09:15]
- "researching historical facts" [06:25]
```

---

## Section 8: Tools & Technologies Matrix

**Purpose**: Create comprehensive matrix of ALL tools mentioned

**Format: TABLE (must be markdown table)**

```markdown
## Tools & Technologies Matrix

| Tool Name | Vendor | Category | Purpose | Used For in Video | Mentioned With (Integrations) | Timestamp |
|-----------|--------|----------|---------|-------------------|-------------------------------|-----------|
| [Tool 1] | [Company] | [Category] | [Purpose] | [How used] | [Other tools] | [MM:SS] |
| [Tool 2] | [Company] | [Category] | [Purpose] | [How used] | [Other tools] | [MM:SS] |
| [Continue for ALL tools mentioned] | | | | | | |

**Example:**

| Tool Name | Vendor | Category | Purpose | Used For in Video | Mentioned With | Timestamp |
|-----------|--------|----------|---------|-------------------|----------------|-----------|
| Claude Desktop | Anthropic | AI/LLM | AI assistant with MCP support | MCP connector orchestration, code generation | MCP Builder, Node.js, Gmail API | [00:30] |
| MCP Builder | Smithery | AI/Development | MCP connector generation tool | Generate connector code in 30-60 sec | Claude Desktop, OAuth | [14:20] |
| Google Cloud Console | Google | Cloud/Platform | Cloud platform management | OAuth credential setup | Gmail API, Calendar API | [15:30] |
| VS Code | Microsoft | Development/IDE | Code editor | Connector development environment | Node.js, Git | [05:15] |
| Anymailfinder | Anymailfinder | Data/Lead Gen | Email enrichment service | Find decision-maker emails | Airscale, CSV files | [07:30] |
```

**Important**: This MUST be a markdown table, not JSON, not a bulleted list.

---

## Section 9: Objects & Deliverables

**Purpose**: List ALL tangible outputs/deliverables mentioned

**Format:**

```markdown
## Objects & Deliverables

- [Object 1]
- [Object 2]
- [Object 3]
- [Continue for all objects mentioned]

**Example:**
- Thumbnails (YouTube thumbnails optimized for CTR)
- Videos (TikTok videos, documentaries, tutorials)
- Scripts (video scripts, documentary scripts)
- Voiceovers (AI-generated audio narration)
- Images (AI-generated images, graphics)
- Reports (analytics reports, gap analysis reports)
- Presentations (pitch decks, slide decks)
- Leads (enriched leads, validated leads, qualified leads)
- Connectors (MCP connectors, API connectors)
- Workflows (automated workflows, business workflows)
- Emails (drafted emails, follow-up emails)
- Dashboards (analytics dashboards, real-time dashboards)
- [Continue...]
```

---

## Section 10: Integration Patterns

**Purpose**: Document how tools/processes connect

**Format:**

```markdown
## Integration Patterns

### INTEGRATION 1: [Tool A] + [Tool B] + [Tool C]

**PURPOSE:** [Why these tools are used together]

**FLOW:**
[Tool A output] → [becomes] → [Tool B input] → [becomes] → [Tool C input]

**USE CASE:** [Specific application demonstrated in video]

**COMPLEXITY:** [Simple / Moderate / Complex]

**TIMESTAMP:** [Where explained: MM:SS - MM:SS]

**Example:**

### INTEGRATION 1: Perplexity + AI Script Generator + VAYU + Seedream + Eleven Labs

**PURPOSE:** Create factually accurate miniature documentaries with research, visuals, and narration

**FLOW:**
Historical facts (Perplexity) → Script generation (AI) → Tilt-shift video (VAYU + Seedream) → Voiceover (Eleven Labs) → Final documentary (GLIF assembly)

**USE CASE:** 32-second educational documentaries for social media

**COMPLEXITY:** Moderate (requires GLIF agent setup)

**TIMESTAMP:** [06:15 - 08:45]
```

---

## Section 11: Business Concepts & Strategy

**Purpose**: Extract business/strategy concepts mentioned

**Format:**

```markdown
## Business Concepts & Strategy

### Business Models
- [Business model 1]: [Description from video]
- [Business model 2]: [Description]

### Success Metrics
- [Metric 1]: [Definition, how measured]
- [Metric 2]: [Definition, how measured]

### Strategic Approaches
- [Approach 1]: [Description]
- [Approach 2]: [Description]

### Value Propositions
- [Value prop 1]: [Description]
- [Value prop 2]: [Description]

### Cost Optimization Strategies
- [Strategy 1]: [Description]
- [Strategy 2]: [Description]

**Example:**

### Business Models
- "ACP funnel": Audience → Conversion → Product funnel for content monetization
- "Arbitrage strategy": Using cheaper tool A to unlock access, then using expensive tool B for maximum value

### Success Metrics
- "CTR" (Click-Through Rate): Percentage of impressions that result in clicks
- "Enrichment rate": Percentage of leads successfully enriched with email data (target: 80%+)
- "Reply rate": Percentage of cold emails that receive responses (11.5% vs 1-3% industry average)
- "ROI ratio": 1:40 (1 credit yields 40 emails using Airscale arbitrage)

### Strategic Approaches
- "Build audience first": Grow engaged audience before monetizing
- "Arbitrage strategy": Exploit cost differences between tools for better ROI
- "Stacked automation": Chain multiple automations for compounding time savings

### Value Propositions
- "10x productivity": Claims of 10 times productivity improvement
- "15+ hours/week saved": Specific time savings from automation
- "$0.0025 per email": Cost per valid email found (vs $0.10-0.15 industry standard)

### Cost Optimization Strategies
- "1:40 credit-to-email ratio": Use one Airscale unlock to generate 40 emails via Anymailfinder company search
```

---

## Section 12: Optimization & Best Practices

**Purpose**: Document optimization tips and best practices mentioned

**Format:**

```markdown
## Optimization & Best Practices

### OPTIMIZATION 1: [Area being optimized]

**TECHNIQUE:** [How to optimize]

**REASON:** [Why this works]

**EVIDENCE/RESULT:** [Proof, data, or outcome mentioned]

**TIMESTAMP:** [Where mentioned: MM:SS]

**Example:**

### OPTIMIZATION 1: YouTube Thumbnail CTR

**TECHNIQUE:** Use high contrast, bold text area, Mr. Beast style aesthetics with faces showing emotion

**REASON:** Catches attention in crowded feeds where users scroll quickly, proven engagement pattern

**EVIDENCE/RESULT:** Creator claims "insane CTR" improvement after implementing this style

**TIMESTAMP:** [03:20]

---

### OPTIMIZATION 2: Email Enrichment Cost

**TECHNIQUE:** Use Airscale arbitrage - unlock company with 1 credit, then use Anymailfinder company search to get 40+ employees

**REASON:** 1:40 ratio vs standard 1:1 ratio, reduces cost per email from $0.10 to $0.0025

**EVIDENCE/RESULT:** 40x improvement in credit efficiency, documented in multiple use cases

**TIMESTAMP:** [08:45]
```

---

## Section 13: Reusability Analysis ⭐ NEW IN V3.2

**Purpose**: Identify reusability opportunities for extracted tasks and steps

**Format:**

```markdown
## Reusability Analysis

### Task Reusability

#### TASK: [Task name from Section 4B]

**REUSABLE_IN:**
- [Context 1 where task could be reused]
- [Context 2]
- [Context 3]
- [Continue...]

**VARIATIONS:**
- [Variation 1: different tool/method]
- [Variation 2: different context]

**Example:**

#### TASK: ENRICH_LEADS_MULTI-SOURCE

**REUSABLE_IN:**
- Partner recruitment campaigns
- Event attendee outreach
- Customer win-back campaigns
- Competitor analysis projects
- Market research initiatives
- Investor prospecting
- Supplier identification

**VARIATIONS:**
- ENRICH_LEADS_SINGLE-SOURCE (using only one enrichment tool for cost savings)
- ENRICH_LEADS_ENTERPRISE (focused on large companies with Airscale arbitrage)
- ENRICH_LEADS_LOCAL (geographic-specific with Google Maps data)

---

### Step Reusability

#### STEP: [Step name from Section 4C]

**REUSABLE_IN:**
- [Task 1 that could use this step]
- [Task 2]
- [Task 3]
- [Continue...]

**SIMILAR_STEPS:**
- [Step with similar function but different tool]

**Example:**

#### STEP: SCRAPE_COMPANY_DATA_FROM_AIRSCALE

**REUSABLE_IN:**
- Any task requiring company list generation
- Market research projects (TAM analysis)
- Competitive intelligence gathering
- Account-based marketing targeting
- Industry analysis projects
- Partner ecosystem mapping

**SIMILAR_STEPS:**
- SCRAPE_COMPANY_DATA_FROM_LINKEDIN (same action, different source)
- SCRAPE_COMPANY_DATA_FROM_APOLLO (could consolidate if Apollo returns)
- SCRAPE_COMPANY_DATA_FROM_GOOGLE-MAPS (for local businesses)
```

---

## Section 14: Success Metrics & Performance Data ⭐ NEW IN V3.2

**Purpose**: Extract quantitative performance data mentioned in video

**Format:**

```markdown
## Success Metrics & Performance Data

### METRIC 1: [Metric Name]

**WORKFLOW/TASK:** [Which workflow or task this metric applies to]

**VALUE:** [Actual value mentioned in video]

**CONTEXT:** [Conditions, timeframe, comparison, methodology]

**BENCHMARK:** [Industry standard if mentioned]

**TIMESTAMP:** [Where mentioned: MM:SS]

**Example:**

### METRIC 1: Enrichment Rate

**WORKFLOW/TASK:** Multi-Source Lead Enrichment Pipeline / ENRICH_LEADS_MULTI-SOURCE

**VALUE:** 80-100%

**CONTEXT:** When using LinkedIn Sales Navigator + Vayne + Anymailfinder combination for decision-maker search

**BENCHMARK:** Industry average 40-60% with standard tools

**TIMESTAMP:** [09:30]

---

### METRIC 2: Cost Per Email

**WORKFLOW/TASK:** Multi-Source Lead Enrichment Pipeline / ENRICH_LEADS_MULTI-SOURCE

**VALUE:** $0.0025 per email

**CONTEXT:** Using Anymailfinder nominative enrichment with company domain input

**BENCHMARK:** Apollo.io $0.10-0.15 per lead (80-95% cheaper)

**TIMESTAMP:** [10:15]

---

### METRIC 3: Time Savings

**WORKFLOW/TASK:** Stacked Connector Post-Meeting Automation / AUTOMATE_POST-MEETING_FOLLOW-UP

**VALUE:** 15+ hours per week

**CONTEXT:** After one-time 2-3 hour setup, automation handles all meeting follow-up tasks including email drafts, CRM updates, calendar reminders

**BENCHMARK:** Manual process takes 15-20 hours/week for heavy meeting schedules

**TIMESTAMP:** [22:45]

---

### METRIC 4: Connector Generation Speed

**WORKFLOW/TASK:** MCP Connector Generation / GENERATE_CONNECTOR_VIA_MCP-BUILDER

**VALUE:** 30-60 seconds

**CONTEXT:** Using Claude MCP Builder skill with 2-sentence requirement prompt

**BENCHMARK:** Manual coding takes 2-4 hours (99% faster)

**TIMESTAMP:** [16:20]

---

### METRIC 5: Reply Rate

**WORKFLOW/TASK:** Custom Niche Platform Scraper / BUILD_CUSTOM_NICHE_SCRAPER

**VALUE:** 11.5%

**CONTEXT:** Using custom n8n + AI HTML parsing for highly targeted niche scraping vs generic lead lists

**BENCHMARK:** Industry average 1-3% reply rate (4-11x better)

**TIMESTAMP:** [25:30]

---

### METRIC 6: ROI Ratio

**WORKFLOW/TASK:** Enterprise Email Arbitrage / EXECUTE_AIRSCALE_ARBITRAGE

**VALUE:** 1:40 (1 credit yields 40 emails)

**CONTEXT:** Using Anymailfinder company search on Airscale company unlock - search by company domain to find all employees

**BENCHMARK:** Standard enrichment 1:1 ratio (1 credit = 1 email)

**TIMESTAMP:** [08:45]
```

---

## FORMATTING STANDARDS

### General Markdown Rules

- Use `#` headers for major sections
- Use `##` for subsections
- Use `###` for sub-subsections
- **Bold** important terms with `**term**`
- `Code formatting` for tool names and technical terms with backticks
- Bullet points with `-` or `*` for lists
- Tables with markdown table syntax `| Column | Column |`
- Timestamps in `[MM:SS]` or `[HH:MM:SS]` format

### Taxonomy-Specific Formatting

- **ACTION VERBS**: Always in CAPS when categorizing (Section 5)
- **Tool names**: Always capitalized consistently (Section 8)
- **Workflows**: Always use structured format with CAPS fields (Section 4)
- **Task names**: `ACTION_OBJECT_CONTEXT` in ALL_CAPS (Section 4B)
- **Step names**: `ACTION_OBJECT_SPECIFIC_DETAIL` in ALL_CAPS (Section 4C)
- **Skill phrases**: `"action via tool"` in lowercase natural language (Section 7B)
- **Task chains**: Use → arrows between steps (Section 6)

---

## VALIDATION CHECKLIST

### FORMAT VALIDATION (CRITICAL - Check First!)

- [ ] **Output is markdown (.md)** - NOT JSON, NOT plain text
- [ ] **Document starts with # heading** - Proper markdown structure
- [ ] **File would save as .md extension** - Confirm format
- [ ] **No JSON curly braces `{}` at document start** - Must be markdown

### SECTION COMPLETENESS (V3.2 REQUIREMENTS)

**All 3 core sections present:**
- [ ] 1. Metadata Section
- [ ] 2. Description Section
- [ ] 3. Word-for-Word Transcription

**TAXONOMY ANALYSIS section included** - This is NOT optional

**All required taxonomy subsections present:**
- [ ] 4. Workflows Identified (with DEPARTMENT field)
- [ ] 4B. Task Templates Extraction (NEW - ACTION_OBJECT_CONTEXT format) ⭐
- [ ] 4C. Step Templates Extraction (NEW - with parent task linkage) ⭐
- [ ] 4D. Project Templates Extraction (NEW - if applicable) ⭐
- [ ] 5. Action Verbs & Operations (A-G categories)
- [ ] 6. Task Chains
- [ ] 7A. Professional Roles Mentioned
- [ ] 7B. Skills Extraction (NEW - "action via tool" format) ⭐
- [ ] 7C. Responsibilities/Activities
- [ ] 8. Tools & Technologies Matrix
- [ ] 9. Objects & Deliverables
- [ ] 10. Integration Patterns (if applicable)
- [ ] 11. Business Concepts & Strategy (if applicable)
- [ ] 12. Optimization & Best Practices (if applicable)
- [ ] 13. Reusability Analysis (NEW) ⭐
- [ ] 14. Success Metrics & Performance Data (NEW) ⭐

### CONTENT QUALITY (V3.2 STANDARDS)

- [ ] All workflows have DEPARTMENT field
- [ ] All workflows have structured format (OBJECTIVE, STEPS, DURATION, etc.)
- [ ] Task Templates follow ACTION_OBJECT_CONTEXT naming
- [ ] Step Templates follow ACTION_OBJECT_SPECIFIC_DETAIL naming
- [ ] Skills follow "action via tool" phrase format
- [ ] Task Templates link to Step Templates (STEPS_USED field)
- [ ] Skills link to tasks (PARENT_TASKS field)
- [ ] Reusability contexts identified for tasks and steps
- [ ] Success metrics extracted with values and context
- [ ] Action verbs categorized into 7 categories (A-G)
- [ ] Tools matrix in TABLE format (not JSON, not bulleted list)
- [ ] Task chains show clear flow with arrows (→)
- [ ] Timestamps provided for key concepts
- [ ] Business value captured
- [ ] No character-by-character text corruption

---

## Transcription Complete! Ready for Stage 2 Analysis.

---

# PART 3 (Continued): STAGE 2 - ANALYSIS (FULL)

## STAGE 2: Video Analysis - Complete Methodology

### Overview

**Goal**: Systematically analyze transcription to extract all taxonomy elements

**Time**: 30-45 minutes (after transcription complete)

**Input**: Complete transcription document from Stage 2 Part 1

**Output**: Analysis report with coverage metrics and gap analysis

---

### Analysis Workflow (3 Phases)

---

## Phase 1: Initial Review (15-20 minutes)

### Step 1: Read Full Transcription

**Process:**
1. Read transcription from beginning to end
2. Don't extract yet, just absorb content
3. Note overall themes and structure
4. Identify high-density sections (lots of tools/workflows mentioned)

**Notes to Take:**
- Main topics covered
- Speaker expertise areas
- Key demonstrations
- Sections worth re-reading

---

### Step 2: Create Inventory List

**Quick scan to list:**

**Tools/Technologies:**
```
Tool 1: [Name] - [What it does]
Tool 2: [Name] - [What it does]
Tool 3: [Name] - [What it does]
[Continue for all tools spotted]
```

**Workflows/Processes:**
```
Workflow 1: [Name] - [Brief description]
Workflow 2: [Name] - [Brief description]
[Continue...]
```

**Action Verbs:**
```
Category A (Creation): create, generate, build, design...
Category B (Modification): edit, optimize, enhance...
Category C (Analysis): analyze, review, evaluate...
[Continue for all categories]
```

**Business Concepts:**
```
- [Concept 1]
- [Concept 2]
- [Metric 1]
- [Strategy 1]
```

---

### Step 3: Timestamp Key Moments

**Mark timestamps where:**
- Tools are introduced or demonstrated
- Workflows are explained step-by-step
- Integration patterns are shown
- Optimization tips are shared
- Performance metrics are mentioned
- Success stories are shared

**Format:**
```
[MM:SS] - [What happens at this timestamp]
[MM:SS] - [What happens]
[Continue...]
```

---

## Phase 2: Deep Extraction (30-45 minutes)

### Step 4: Extract Tools & Technologies

**For each tool mentioned, use this template:**

```markdown
---
TOOL EXTRACTION: [Tool Name]
---
**Tool Name:** [Exact name as mentioned in video]
**Vendor:** [Company or creator - look for mentions in video]
**Category:** [AI/LLM, Automation, Development, etc. - see categorization guide in Stage 3]
**Purpose:** [Primary use case in 1 sentence]
**Version:** [If specific version mentioned]
**Timestamp:** [Where first introduced: MM:SS]
**Context:** [How it's used in this video]
**Integration:** [Other tools it connects with in video]
**Use Cases:** [Specific applications mentioned]
**Pricing:** [If mentioned]
**Links:** [URLs mentioned]
---
```

**Example from Video:**

```markdown
---
TOOL EXTRACTION: Claude Desktop
---
**Tool Name:** Claude Desktop
**Vendor:** Anthropic
**Category:** AI/LLM
**Purpose:** AI assistant with MCP (Model Context Protocol) support for tool integrations
**Version:** Latest (November 2025)
**Timestamp:** [00:30]
**Context:** Central platform for MCP connector orchestration and code generation workflows
**Integration:** MCP Builder, Gmail API, Calendar API, VS Code, Node.js
**Use Cases:** MCP connector generation, email draft automation, meeting follow-up automation, code generation
**Pricing:** Paid subscription (specific price not mentioned)
**Links:** anthropic.com (mentioned at 00:45)
---
```

**Repeat for ALL tools mentioned in video.**

---

### Step 5: Extract Workflows

**For each workflow described, use this template:**

```markdown
---
WORKFLOW EXTRACTION: [Workflow Name]
---
**WORKFLOW:** [Descriptive name]
**OBJECTIVE:** [What this workflow achieves in one sentence]
**STEPS:**
  1. [Action verb] + [object/deliverable] - [detail]
  2. [Action verb] + [object/deliverable] - [detail]
  3. [Continue for all steps]
**DURATION:** [Time estimate if mentioned]
**COMPLEXITY:** [Low/Medium/High/Very High - your assessment]
**TOOLS USED:** [List all tools in sequence]
**INPUT:** [What you start with]
**OUTPUT:** [What you produce]
**TIMESTAMP:** [Where explained in video: MM:SS - MM:SS]
**BUSINESS VALUE:** [Why this matters - ROI, time savings, cost savings]
---
```

**Example from Video:**

```markdown
---
WORKFLOW EXTRACTION: MCP Connector Generation
---
**WORKFLOW:** Create Production-Ready MCP Server in Under 1 Minute
**OBJECTIVE:** Generate a complete MCP connector with OAuth, API handlers, and error handling using Claude's MCP Builder skill
**STEPS:**
  1. Enable Claude Skills in Claude Desktop settings
  2. Write 2-sentence connector requirements (what API, what actions)
  3. Execute MCP Builder skill with requirements
  4. Review generated code (index.js, package.json, config)
  5. Save connector files to local directory
  6. Install dependencies (npm install)
  7. Test connector with Claude Desktop
**DURATION:** 30-60 seconds for generation, 5-10 minutes total with testing
**COMPLEXITY:** Very High (but automated to simple user experience)
**TOOLS USED:** Claude Desktop, MCP Builder Skill, VS Code, Node.js, npm
**INPUT:** 2-sentence connector requirements describing API and desired functionality
**OUTPUT:** Complete MCP server code with OAuth 2.0 setup, API handlers, error handling, 95%+ success rate
**TIMESTAMP:** [14:20 - 18:50]
**BUSINESS VALUE:** 99% time savings (30-60 sec vs 2-4 hours manual coding), enables rapid automation deployment, democratizes connector creation for non-developers
---
```

**Repeat for ALL workflows mentioned or demonstrated in video.**

---

### Step 6: Extract Action Verbs

**Scan entire transcription for action verbs and categorize:**

**Method:**
1. Read through transcription
2. Highlight every verb that describes an action
3. Count frequency of each verb
4. Note timestamps where used
5. Categorize into A-G categories

**Template:**

```markdown
ACTION VERB EXTRACTION

**A. CREATION VERBS:**
- create (15 times) - [00:45], [02:30], [05:12], [08:22], ...
- generate (23 times) - [01:20], [03:15], [06:45], [09:10], ...
- build (8 times) - [07:20], [09:15], [12:40], ...
- design (5 times) - [02:34], [04:50], [11:25], ...
- [Continue for all creation verbs found]

**B. MODIFICATION VERBS:**
- optimize (12 times) - [03:20], [05:40], [08:15], [10:22], ...
- refine (6 times) - [04:10], [07:30], [13:50], ...
- customize (4 times) - [06:00], [09:45], [14:20], ...
- [Continue for all modification verbs found]

**C. ANALYSIS VERBS:**
- [Continue same format]

**D. ORGANIZATION VERBS:**
- [Continue same format]

**E. COMMUNICATION VERBS:**
- [Continue same format]

**F. BROWSER/AGENTIC OPERATIONS:**
- [Continue same format]

**G. DATA OPERATIONS:**
- [Continue same format]
```

---

### Step 7: Extract Task Chains

**Identify multi-step sequences:**

**Template:**

```markdown
---
TASK CHAIN: [Name]
---
**SEQUENCE:** [Tool/Action 1] → [Tool/Action 2] → [Tool/Action 3] → [Final Output]

**PURPOSE:** [What this chain accomplishes]

**AUTOMATION LEVEL:** [Manual / Semi-automated / Fully automated]

**TIMESTAMP:** [Where mentioned: MM:SS - MM:SS]
---

**Example:**

---
TASK CHAIN: Automated Email Follow-Up
---
**SEQUENCE:** Meeting transcript → Claude extracts action items → Gmail drafts follow-up → CRM updates notes → Calendar sets reminder

**PURPOSE:** Complete post-meeting workflow automation without manual intervention

**AUTOMATION LEVEL:** Fully automated (via stacked MCP connectors)

**TIMESTAMP:** [20:15 - 24:30]
---
```

---

### Step 8: Extract Responsibilities Vocabulary

**Identify role-related terms:**

**Professional Roles:**
```markdown
PROFESSIONAL ROLES EXTRACTED:

- **Role 1:** [Role name]
  - Context: [How described in video]
  - Timestamp: [MM:SS]

- **Role 2:** [Role name]
  - Context: [How described]
  - Timestamp: [MM:SS]

[Continue for all roles]

**Example:**

- **AI Engineer:**
  - Context: Responsible for MCP connector development, automation setup, Claude integration
  - Timestamp: [14:00]

- **Operations Manager:**
  - Context: Configures and maintains automated workflows, handles cross-department coordination
  - Timestamp: [20:00]
```

**Responsibilities/Activities:**
```markdown
RESPONSIBILITIES EXTRACTED:

- "[Activity phrase 1]" - [Timestamp: MM:SS]
- "[Activity phrase 2]" - [Timestamp: MM:SS]
- [Continue with exact phrasing from video]

**Example:**

- "generating MCP connectors" - [14:20]
- "configuring OAuth for Google APIs" - [15:30]
- "automating email workflows" - [20:45]
- "orchestrating multi-tool integrations" - [22:15]
```

**Skills Mentioned:**
```markdown
SKILLS EXTRACTED:

- **"[skill phrase via tool]"**
  - Context: [What this skill enables]
  - Timestamp: [MM:SS]
  - Difficulty: [Beginner/Intermediate/Advanced/Expert]

**Example:**

- **"generated MCP connectors via Claude"**
  - Context: Using Claude's MCP Builder skill to create production-ready connector code in under 60 seconds
  - Timestamp: [14:20]
  - Difficulty: Intermediate (requires understanding of APIs and OAuth)

- **"enriched emails via Anymailfinder"**
  - Context: Finding decision-maker emails using nominative enrichment patterns
  - Timestamp: [07:30]
  - Difficulty: Beginner (15-minute learning curve)
```

---

### Step 9: Extract Integration Patterns

**Document tool connections:**

**Template:**

```markdown
---
INTEGRATION PATTERN: [Tool A] + [Tool B] + [Tool C]
---
**PURPOSE:** [Why these tools are used together]

**FLOW:**
  [Tool A output] → [description] → [Tool B input]
                 ↓
  [Tool B output] → [description] → [Tool C input]
                 ↓
  [Tool C output] → [Final result]

**USE CASE:** [Specific application from video]

**COMPLEXITY:** [Simple / Moderate / Complex]

**TIMESTAMP:** [Where explained: MM:SS - MM:SS]

**BENEFITS:**
- [Benefit 1]
- [Benefit 2]

**REQUIREMENTS:**
- [Requirement 1]
- [Requirement 2]
---

**Example:**

---
INTEGRATION PATTERN: Claude Desktop + Gmail MCP + Calendar MCP + CRM Connector
---
**PURPOSE:** Automate complete post-meeting workflow from transcript to follow-up

**FLOW:**
  Meeting transcript → Claude Desktop extracts:
    - Action items
    - Decisions made
    - Client wins
    - Attendee names/emails
                 ↓
  Extracted data → Gmail MCP drafts:
    - Personalized follow-up email
    - Thank you message
    - Next steps summary
                 ↓
  Email content → Calendar MCP:
    - Sets reminder for follow-up
    - Blocks time for action items
                 ↓
  All data → CRM Connector:
    - Updates meeting notes
    - Logs client wins
    - Updates deal stage

**USE CASE:** Sales and customer success teams handling 10+ meetings per week

**COMPLEXITY:** Complex (requires 4 MCP connectors configured) but then fully automated

**TIMESTAMP:** [18:20 - 24:50]

**BENEFITS:**
- 15+ hours/week saved (per person with heavy meeting load)
- Zero follow-ups missed
- CRM always up-to-date
- Consistent communication quality

**REQUIREMENTS:**
- Claude Desktop with Skills enabled
- 4 MCP connectors installed (Gmail, Calendar, CRM, custom extraction)
- OAuth configured for Gmail and Calendar
- CRM API credentials
---
```

---

## Phase 3: Taxonomy Mapping (20-30 minutes)

### Step 10: Check Existing Taxonomy

**For each extracted tool:**

**Process:**
1. Open `LIBRARIES/Tools/` directory
2. Search for tool by name (e.g., search for "Claude")
3. If found: Note file path and what exists
4. If not found: Mark as gap to fill

**Template:**

```markdown
TAXONOMY CHECK RESULTS

✅ **TOOLS THAT EXIST:**

1. **Claude Desktop**
   - Status: EXISTS
   - File: LIBRARIES/Tools/AI_Tools/Claude.json
   - Tool ID: TOOL-AI-009
   - Action: ENHANCE (add MCP Builder context, connector generation workflow)
   - Current description mentions: General AI assistant capabilities
   - Missing from current: MCP support, connector generation, Skills feature

2. **VS Code**
   - Status: EXISTS
   - File: LIBRARIES/Tools/Development_Tools/VS_Code.json
   - Tool ID: TOOL-DEV-015
   - Action: ENHANCE (add MCP connector development use case)

[Continue for all existing tools]

---

❌ **TOOLS THAT ARE MISSING (Critical Priority):**

1. **MCP Builder**
   - Status: MISSING
   - Suggested Category: AI_Tools or Development_Tools
   - Priority: CRITICAL (central to workflow in video)
   - Impact: Cannot document MCP connector generation workflow without this
   - Suggested Tool ID: TOOL-AI-039 or TOOL-DEV-065

2. **Anymailfinder**
   - Status: MISSING
   - Suggested Category: Data_Tools or Lead_Gen_Tools
   - Priority: HIGH (key tool for email enrichment)
   - Impact: Email enrichment workflows incomplete
   - Suggested Tool ID: TOOL-DATA-006

[Continue for all missing tools]

---

❌ **TOOLS THAT ARE MISSING (High Priority):**

[Continue listing]

---

❌ **TOOLS THAT ARE MISSING (Medium/Low Priority):**

[Continue listing]
```

---

### Step 11: Calculate Coverage Metrics

**Formula:**

```
Coverage % = (Existing items / Total items mentioned) × 100
```

**Template:**

```markdown
COVERAGE CALCULATION

### Tools Coverage

**Total Tools Mentioned in Video:** 10
- Claude Desktop
- MCP Builder
- VS Code
- Node.js
- Gmail API
- Google Cloud Console
- Anymailfinder
- Airscale
- LinkedIn Sales Navigator
- Google Sheets

**Existing in Taxonomy:** 5
- Claude Desktop (TOOL-AI-009) ✅
- VS Code (TOOL-DEV-015) ✅
- Node.js (TOOL-DEV-042) ✅
- Gmail API (TOOL-COMM-018) ✅
- Google Sheets (TOOL-COLLAB-005) ✅

**Missing from Taxonomy:** 5
- MCP Builder ❌
- Google Cloud Console ❌
- Anymailfinder ❌
- Airscale ❌
- LinkedIn Sales Navigator ❌

**BEFORE ANALYSIS: 50% coverage (5/10)**
**AFTER ANALYSIS: Target 100% coverage (10/10)** ← All gaps will be filled

**Gap Impact:** 5 new tool JSON files need to be created

**Enhancement Impact:** 5 existing files need to be enhanced with video context

---

### Workflows Coverage

**Total Workflows Mentioned:** 3
- MCP Connector Generation
- Email Enrichment Pipeline
- Post-Meeting Automation

**Existing in Taxonomy:** 0
- None of these workflows currently documented

**Missing from Taxonomy:** 3
- All workflows are new

**Coverage:** 0% → Target 100% after documentation

---

### Task Templates Coverage

**Total Task Templates Identified:** 5
- GENERATE_CONNECTOR_VIA_MCP-BUILDER
- ENRICH_LEADS_MULTI-SOURCE
- AUTOMATE_EMAILS_MORNING-DRAFTS
- [Continue...]

**Existing in Taxonomy:** [Count if any]

**Missing:** [Count]

**Coverage:** X% → Target 100%

---

### Skills Coverage

**Total Skills Identified:** 4
- "generated MCP connectors via Claude"
- "configured OAuth for Google APIs"
- "enriched emails via Anymailfinder"
- "scraped lead lists via Airscale"

**Existing in Taxonomy:** [Count if any]

**Missing:** [Count]

**Coverage:** X% → Target 100%
```

---

### Step 12: Create Gap Analysis Report

**Template:**

```markdown
# GAP ANALYSIS REPORT

## Video: [Video Title]
## Analysis Date: [YYYY-MM-DD]
## Analyzer: [Name]

---

## Executive Summary

**Total Gaps Identified:** [Count]
- **Critical Priority:** [Count] gaps
- **High Priority:** [Count] gaps
- **Medium Priority:** [Count] gaps
- **Low Priority:** [Count] gaps

**Coverage Metrics:**
- Tools: X% → Target 100% (+Y tools to add)
- Workflows: X% → Target 100% (+Y workflows to document)
- Tasks: X% → Target 100% (+Y Task Templates)
- Skills: X% → Target 100% (+Y skills)

**Estimated Work:**
- New tool entries to create: [Count]
- Existing tools to enhance: [Count]
- Task Templates to create: [Count]
- Step Templates to create: [Count]
- Skills to document: [Count]
- **Total estimated time:** [X hours]

---

## CRITICAL GAPS (Must create immediately)

### 1. [Tool/Concept Name]

**Type:** [Tool / Workflow / Task / Skill]

**Why Critical:**
- [Reason 1: e.g., Central to workflow, mentioned 30+ times]
- [Reason 2: e.g., Blocks understanding of integration patterns]
- [Reason 3: e.g., High strategic value - addresses Critical Priority Topic]

**Impact if Missing:**
- [Impact 1]
- [Impact 2]

**Recommendation:** Create immediately, assign to [Team/Person]

**Estimated Time:** [X minutes/hours]

**Priority Score:** 10/10

---

### 2. [Next critical gap]

[Continue same format]

---

## HIGH PRIORITY GAPS

[Continue same structure as Critical Gaps]

---

## MEDIUM PRIORITY GAPS

[Continue same structure]

---

## LOW PRIORITY GAPS

[Continue same structure]

---

## ENHANCEMENT OPPORTUNITIES

**Existing Tool/Resource to Enhance:**

### 1. [Existing Tool Name]

**Current File:** LIBRARIES/Tools/[Category]/[ToolName].json

**Current Status:** [Brief description of what exists]

**What to Add from Video:**
- [Enhancement 1: e.g., Add MCP Builder workflow]
- [Enhancement 2: e.g., Update use cases with connector generation]
- [Enhancement 3: e.g., Add integration_capabilities: MCP Builder, Gmail API]

**Value Added:**
- [Benefit 1]
- [Benefit 2]

**Estimated Time:** [X minutes]

---

## ACTION PLAN

### Immediate Actions (This Week):

1. **Create [Count] Critical Priority Tools**
   - [Tool 1]: Assign to [Person], Deadline: [Date]
   - [Tool 2]: Assign to [Person], Deadline: [Date]

2. **Enhance [Count] Existing Tools**
   - [Tool 1]: Assign to [Person], Deadline: [Date]

3. **Document [Count] Workflows**
   - [Workflow 1]: Assign to [Person], Deadline: [Date]

### Short-term Actions (Next 2 Weeks):

[Continue listing]

### Long-term Actions (Next Month):

[Continue listing]

---

## STATISTICS & INSIGHTS

### Tool Discovery Statistics:

- **Most Mentioned Tool:** [Tool Name] ([X] mentions)
- **Most Integrated Tool:** [Tool Name] (connects with [Y] other tools)
- **Highest Value Tool:** [Tool Name] ([ROI/Time savings mentioned])

### Workflow Statistics:

- **Most Complex Workflow:** [Workflow Name] (Complexity: Very High)
- **Highest ROI Workflow:** [Workflow Name] ([X hours/week saved])
- **Most Reusable Workflow:** [Workflow Name] ([Y] potential use cases)

### Category Distribution:

**Tools by Category:**
- AI/LLM: [Count]
- Development: [Count]
- Automation: [Count]
- Data/Lead Gen: [Count]
- [Continue...]

**Missing Tools by Category:**
- AI/LLM: [Count] missing
- Development: [Count] missing
- [Continue...]

---

## RECOMMENDATIONS

### Priority Recommendations:

1. **[Recommendation 1]**
   - Why: [Reason]
   - Impact: [Expected outcome]
   - Effort: [Low/Medium/High]
   - Timeline: [When to do]

2. **[Recommendation 2]**
   [Continue...]

### Process Improvements:

1. **[Process improvement 1]**
   - Current issue: [What's not working]
   - Proposed solution: [How to fix]
   - Expected benefit: [What improves]

---

## NEXT STEPS

**Assigned Tasks:**
- [ ] [Task 1] - Assigned to: [Person] - Due: [Date]
- [ ] [Task 2] - Assigned to: [Person] - Due: [Date]
- [ ] [Task 3] - Assigned to: [Person] - Due: [Date]

**Follow-up:**
- Schedule: [Date] - Review completion of critical gaps
- Metrics check: [Date] - Verify coverage improvement

---

**Gap Analysis Completed By:** [Name]
**Date:** [YYYY-MM-DD]
**Next Analysis:** [After Stage 3 Population complete]
```

---

## Extraction Techniques (Reference)

### Technique 1: Tool Identification

**Look for patterns:**
- "I use [Tool Name] to..."
- "This is created with [Tool Name]..."
- "You can get [Tool Name] at..."
- Tool names in on-screen text: `[TEXT: Tool Name]`
- URLs mentioned: "go to toolname.com"

**Validation:**
- Tool is mentioned multiple times → High confidence
- Tool is demonstrated on screen → Confirmed
- Tool version mentioned → Note version
- Tool URL provided → Capture for documentation_url field

### Technique 2: Workflow Extraction

**Trigger phrases:**
- "First I..., then I..., and finally..."
- "The process is..."
- "Here's how I create..."
- "My workflow for..."
- "Step one is..., step two is..."
- "The way this works is..."

**Structure workflow as:**
1. Clear objective statement (one sentence)
2. Sequential numbered steps (action verb + object)
3. Tools used at each step
4. Time estimate (if mentioned)
5. Input and output formats
6. Business value (why this matters)

### Technique 3: Integration Pattern Recognition

**Signals of integration:**
- "I combine [Tool A] with [Tool B]..."
- "The output from [Tool A] goes into [Tool B]..."
- "[Tool A] and [Tool B] work together to..."
- "After [Tool A], I use [Tool B] to..."
- "This connects to..." / "This integrates with..."

**Document:**
- Which tools connect (all tools in chain)
- Direction of data flow (A → B → C)
- Purpose of combination (why integrate?)
- Output enhancement achieved (what's better?)

### Technique 4: Action Verb Collection

**Method:**
1. Scan transcript for imperative verbs
2. Note verbs in workflow steps
3. Capture verbs from UI demonstrations
4. Count frequency of each verb
5. Note where used (contexts)

**Categorization rules:**
- **Creation**: Brings something new into existence (create, generate, build)
- **Modification**: Changes something that already exists (edit, optimize, enhance)
- **Analysis**: Evaluates or understands something (analyze, review, assess)
- **Organization**: Arranges or structures information (organize, categorize, plan)
- **Communication**: Shares or presents information (share, publish, present)
- **Browser/Agentic**: AI agent actions (automate, control, execute, click)
- **Data Operations**: Processing data (scrape, parse, extract, enrich, validate)

### Technique 5: Responsibilities Mining

**Look for:**
- Role titles: "As a [role]..." / "If you're a [role]..."
- Job functions: "People who do..."
- Skill mentions: "You need to know..." / "This requires..."
- Activity descriptions: "Creating [deliverable]..." / "Managing [process]..."
- Task ownership: "The [role] would..." / "[Role] is responsible for..."

**Extract:**
- Role names (exact titles mentioned)
- Activity phrases (use exact wording from video)
- Required skills (technical and soft skills)
- Tools associated with each role

---

## Analysis Complete! Ready for Stage 3 Population.

---

[Due to length constraints, I'll continue with STAGE 3 in the next response. Would you like me to continue with the full Stage 3 (Library Processing) content?]


# Complete Video Workflow - PART 2 (Continuation)
**Stage 3: Library Processing & Final Sections**

---

**NOTE**: This is Part 2 of the Complete Video Workflow Full Instructions. Part 1 contains Overview, Stage 1 (Research), and Stage 2 (Processing). This file contains Stage 3 (Library Processing), Integration sections, and Quick Start Guide.

---

# PART 4: STAGE 3 - LIBRARY PROCESSING (FULL)

## STAGE 3: Library Processing - Complete Instructions

### Overview

**Goal**: Validate, enrich, and integrate extracted taxonomy data into LIBRARIES structure

**Time**: 10-20 minutes per video

**Input**: Complete transcription document from Stage 2 with all 14 sections

**Output**: Updated LIBRARIES with new/enriched tool entries, Task Templates, Step Templates, skills

---

### Step 3.1: Load Extracted Data

**Input Files Required:**

1. **Video transcription document** from Stage 2 (.md format)
   - Location: Where you saved it after transcription
   - Contains: All 14 taxonomy sections

2. **Existing tool_mapping.json**
   - Location: `ENTITIES/TASK_MANAGERS/tool_mapping.json`
   - Contains: Tool name → Tool ID mappings

3. **Existing discovered_tools.json**
   - Location: `ENTITIES/TASK_MANAGERS/discovered_tools.json`
   - Contains: Recently discovered tools (253 as of 2025-11-10)

4. **Current LIBRARIES/Tools/*.json files**
   - Location: `ENTITIES/LIBRARIES/Tools/[Category]/`
   - Contains: Existing tool entries (254 tools across 15 categories)

**Data to Extract from Transcription:**

From your Stage 2 transcription document, collect:

- **Section 8**: Tools & Technologies Matrix → List of all tools
- **Section 4B**: Task Templates → Task Template names and details
- **Section 4C**: Step Templates → Step Template names and details
- **Section 7B**: Skills → Skill phrases and linkages
- **Section 4**: Workflows → Workflow descriptions
- **Section 5**: Action Verbs → Categorized verbs
- **Section 9**: Objects & Deliverables → Object names

---

### Step 3.2: Tool Collection & Validation

#### Process Overview

**For each tool from Section 8 (Tools Matrix):**

```
1. Check if tool exists in LIBRARIES/Tools
   ↓
2. Check tool_mapping.json for tool ID
   ↓
3. If exists: Enrich with video context
4. If missing: Create new tool entry with proper ID
   ↓
5. Update mappings
```

---

#### Substep 3.2.1: Check Existing Tools

**Process:**

1. Open tool_mapping.json
2. Search for tool by name (exact match or variation)
3. If found: Note tool_id and file path
4. If not found: Mark as new tool to create

**Example:**

```json
// tool_mapping.json excerpt
{
  "Claude Desktop": {
    "tool_id": "TOOL-AI-009",
    "category": "AI_Tools",
    "file_path": "/path/to/LIBRARIES/Tools/AI_Tools/Claude.json"
  },
  "Anymailfinder": {
    "tool_id": null,
    "category": null,
    "file_path": null
  }
}
```

**Result:**
- Claude Desktop: EXISTS (TOOL-AI-009) → Will ENHANCE
- Anymailfinder: MISSING → Will CREATE

---

#### Substep 3.2.2: Tool Categorization Guide

**When creating NEW tools, assign to correct category:**

### Category Decision Tree

**Is it AI-powered (LLM, AI model, AI service)?**
→ **AI_Tools**
- Examples: ChatGPT, Claude, Gemini, Perplexity, Midjourney, ElevenLabs
- Subcategories: AI/LLM, AI/Image Generation, AI/Video Generation, AI/Audio

**Does it automate workflows (no-code/low-code)?**
→ **Automation_Tools**
- Examples: n8n, Zapier, Make, IFTTT
- Subcategories: Automation/Workflow, Automation/RPA

**Is it for coding/development (IDE, version control, dev tools)?**
→ **Development_Tools**
- Examples: VS Code, Cursor, GitHub, Node.js, Python
- Subcategories: Development/IDE, Development/Version Control, Development/Runtime

**Is it for documentation (note-taking, markdown, wikis)?**
→ **Documentation_Tools**
- Examples: Obsidian, Notion, Markdown editors
- Subcategories: Documentation/Note-taking, Documentation/Wiki

**Is it for design (graphics, UI/UX, prototyping)?**
→ **Design_Tools**
- Examples: Figma, Photoshop, Sketch
- Subcategories: Design/UI-UX, Design/Graphics

**Is it for video/audio production?**
→ **Video_Tools**
- Examples: Premiere Pro, DaVinci Resolve, Maestra (transcription)
- Subcategories: Video/Editing, Video/Transcription, Video/Generation

**Is it for communication (email, CRM, messaging)?**
→ **Communication_Tools**
- Examples: Gmail, Outlook, Slack, HubSpot (CRM)
- Subcategories: Communication/Email, Communication/CRM, Communication/Messaging

**Is it for team collaboration (project management, real-time collab)?**
→ **Collaboration_Tools**
- Examples: Asana, Trello, Google Docs, Notion (PM)
- Subcategories: Collaboration/Project Management, Collaboration/Real-time

**Is it for file storage/management?**
→ **File_Management**
- Examples: Dropbox, Google Drive, OneDrive
- Subcategories: File/Cloud Storage

**Is it for analytics/reporting (dashboards, BI)?**
→ **Analytics_Tools**
- Examples: Tableau, Power BI, Google Analytics
- Subcategories: Analytics/Dashboard, Analytics/Business Intelligence

**Is it for data processing (ETL, enrichment, scraping)?**
→ **Data_Tools**
- Examples: Anymailfinder (enrichment), Apify (scraping)
- Subcategories: Data/Enrichment, Data/Scraping, Data/ETL

**Is it for testing (QA, test automation)?**
→ **Testing_Tools**
- Examples: Selenium, Jest, Cypress
- Subcategories: Testing/Unit, Testing/E2E

**Is it a cloud platform (AWS, Azure, GCP)?**
→ **Cloud_Services**
- Examples: AWS, Google Cloud, Azure
- Subcategories: Cloud/Infrastructure

**Is it for presentations?**
→ **Presentation_Tools**
- Examples: PowerPoint, Google Slides, Gamma
- Subcategories: Presentation/Slides

---

#### Substep 3.2.3: Tool ID Generation

**Format**: `TOOL-[CATEGORY]-###`

**Category Abbreviations (Actual from library):**

| Category | Abbreviation | Example | Next Available ID (Nov 2025) |
|----------|--------------|---------|------------------------------|
| AI_Tools | AI | TOOL-AI-027 | TOOL-AI-039 |
| Analytics_Tools | ANALYTICS | TOOL-ANALYTICS-022 | TOOL-ANALYTICS-023 |
| Automation_Tools | AUTO | TOOL-AUTO-191 | TOOL-AUTO-192 |
| Cloud_Services | CLOUD | TOOL-CLOUD-002 | TOOL-CLOUD-003 |
| Collaboration_Tools | COLLAB | TOOL-COLLAB-009 | TOOL-COLLAB-010 |
| Communication_Tools | COMM | TOOL-COMM-035 | TOOL-COMM-036 |
| Data_Tools | DATA | TOOL-DATA-005 | TOOL-DATA-006 |
| Design_Tools | DESIGN | TOOL-DESIGN-022 | TOOL-DESIGN-023 |
| Development_Tools | DEV | TOOL-DEV-064 | TOOL-DEV-065 |
| Documentation_Tools | DOC | TOOL-DOC-076 | TOOL-DOC-077 |
| File_Management | FILE | TOOL-FILE-005 | TOOL-FILE-006 |
| Presentation_Tools | PRES | TOOL-PRES-001 | TOOL-PRES-002 |
| Testing_Tools | TEST | TOOL-TEST-011 | TOOL-TEST-012 |
| Video_Tools | VIDEO | TOOL-VIDEO-014 | TOOL-VIDEO-015 |

**Process to Generate New ID:**

1. Determine category (use decision tree above)
2. Check latest ID in that category (look at existing tools or tool_mapping.json)
3. Increment by 1
4. Format as TOOL-[ABBREV]-###

**Example:**

```
Tool: Anymailfinder
Category: Data_Tools (email enrichment = data operation)
Abbreviation: DATA
Latest ID in Data_Tools: TOOL-DATA-005
Next ID: TOOL-DATA-006
Assign: TOOL-DATA-006
```

---

#### Substep 3.2.4: Tool JSON Schema & Creation

**Complete Tool JSON Structure:**

```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-CATEGORY-###",
  "name": "Tool Name",
  "vendor": "Vendor/Company Name",
  "category": "Category / Subcategory",
  "purpose": "One-sentence primary purpose",
  "description": "Detailed description with context from video. Include how it's used, what problems it solves, integration patterns. 2-4 sentences.",
  "skill_level_required": "Beginner|Intermediate|Advanced|Expert",
  "cost_structure": "Free|Freemium|Paid subscription ($X/mo)|Usage-based ($X per Y)|TBD",
  "platform_compatibility": ["Web", "Mobile", "Desktop", "API", "CLI"],
  "integration_capabilities": ["API", "Zapier", "n8n", "OAuth 2.0", "Webhooks", "MCP"],
  "documentation_url": "https://tool-website.com/docs",
  "actual_remote_helpers_usage": {
    "primary_use": "Main use case extracted from video",
    "users": ["Department 1", "Department 2", "Role 1"],
    "use_cases": [
      "Use case 1 from video",
      "Use case 2 from video",
      "Use case 3 from video"
    ],
    "workflows": [
      "Workflow 1 name from Section 4",
      "Workflow 2 name from Section 4"
    ]
  },
  "strengths": [
    "Strength 1 mentioned in video",
    "Strength 2 (e.g., time savings, cost efficiency)",
    "Strength 3 (e.g., ease of use, integration)"
  ],
  "limitations": [
    "Limitation 1 mentioned in video",
    "Limitation 2 (e.g., cost, learning curve)"
  ],
  "departments_using": ["Department 1", "Department 2"],
  "tags": ["tag1", "tag2", "tag3", "tag4"],
  "discovery_date": "2025-11-17",
  "discovery_source": "video_transcription",
  "status": "active"
}
```

**Field Requirements:**

| Field | Required? | Can be TBD? | Notes |
|-------|-----------|-------------|-------|
| tool_id | YES | NO | Must be unique, sequential |
| name | YES | NO | Exact tool name |
| vendor | YES | If unknown | Company/creator |
| category | YES | NO | Must match categories |
| purpose | YES | NO | One sentence |
| description | YES | NO | Extract from video |
| skill_level_required | YES | Can estimate | Based on video demo |
| cost_structure | YES | YES | "TBD" if not mentioned |
| platform_compatibility | YES | Can be partial | At least one platform |
| integration_capabilities | YES | Can be empty | Extract from video |
| documentation_url | NO | YES | "TBD" if not found |
| actual_remote_helpers_usage | YES | NO | Extract from video |
| strengths | YES | NO | At least 2 |
| limitations | NO | Can be empty | If mentioned |
| departments_using | YES | NO | Extract from video |
| tags | YES | NO | At least 3 |
| discovery_date | YES | NO | Today's date |
| discovery_source | YES | NO | "video_transcription" |
| status | YES | NO | "active" for new tools |

---

#### Substep 3.2.5: Create/Enhance Tool Entries

**For NEW tools (not in library):**

1. Create JSON file following schema above
2. Populate all fields from video transcription:
   - **name**: From Section 8 Tools Matrix
   - **vendor**: Look for mentions in transcript
   - **category**: Use categorization guide
   - **purpose**: Extract from how tool is described
   - **description**: Context from video (how used, why, with what)
   - **use_cases**: From Section 4 workflows and 4B Task Templates
   - **workflows**: From Section 4
   - **departments**: Infer from workflow context
   - **strengths**: Extract from video mentions
   - **tags**: Generate from purpose, category, features

3. Save file:
   - Location: `LIBRARIES/Tools/[Category]/[ToolName].json`
   - Example: `LIBRARIES/Tools/Data_Tools/Anymailfinder.json`

4. Add to tool_mapping.json:
   ```json
   "Anymailfinder": {
     "tool_id": "TOOL-DATA-006",
     "category": "Data_Tools",
     "file_path": "/path/to/LIBRARIES/Tools/Data_Tools/Anymailfinder.json"
   }
   ```

**For EXISTING tools (already in library):**

1. Open existing JSON file
2. Enhance with video context:
   - Add to **use_cases** array (new use cases from video)
   - Add to **workflows** array (new workflows from Section 4)
   - Update **description** (add video context)
   - Add to **integration_capabilities** (if video shows integrations)
   - Add to **strengths** (if video mentions benefits)
   - Update **departments_using** (if new departments mentioned)
3. Save updated file

**Example Enhancement:**

```json
// BEFORE (existing Claude.json):
{
  "tool_id": "TOOL-AI-009",
  "name": "Claude",
  "description": "AI assistant by Anthropic for conversation and content generation",
  "use_cases": [
    "content writing",
    "code generation",
    "analysis"
  ],
  "workflows": []
}

// AFTER (enhanced with video context):
{
  "tool_id": "TOOL-AI-009",
  "name": "Claude Desktop",
  "description": "AI assistant by Anthropic with MCP (Model Context Protocol) support enabling tool integrations. Can generate MCP connector code in 30-60 seconds using MCP Builder skill. Orchestrates multi-tool workflows through stacked connectors.",
  "use_cases": [
    "content writing",
    "code generation",
    "analysis",
    "MCP connector generation (NEW)",
    "email draft automation (NEW)",
    "meeting follow-up automation (NEW)"
  ],
  "workflows": [
    "MCP Connector Generation (NEW)",
    "Stacked Connector Post-Meeting Automation (NEW)"
  ],
  "integration_capabilities": [
    "API",
    "MCP (Model Context Protocol) (NEW)",
    "Gmail API (NEW)",
    "Calendar API (NEW)"
  ]
}
```

---

### Step 3.3: Task & Step Template Integration

**Purpose**: Create task and Step Template files in TASK_MANAGERS structure

---

#### Substep 3.3.1: Task Templates (from Section 4B)

**For each Task Template extracted in Section 4B:**

**Target Location**: `ENTITIES/TASK_MANAGERS/Task_Templates/[DEPARTMENT]/`

**File Format**: `[DEPT]-[###].md`

**ID Assignment**: Sequential within department (check existing task IDs)

**Process:**

1. **Determine Department**: From DEPARTMENT field in Section 4B
2. **Check Next Available ID**:
   - Look in `TASK_MANAGERS/Task_Templates/[DEPT]/`
   - Find highest number (e.g., AI-006.md exists)
   - Next ID: AI-007

3. **Create Task Template File**:

```markdown
# Task Template: [TASK_NAME_ACTION_OBJECT_CONTEXT]

## Metadata

- **Task ID**: [DEPT]-[###]
- **Task Name**: [ACTION_OBJECT_CONTEXT]
- **Department**: [Department Name]
- **Complexity**: [Low/Medium/High/Very High]
- **Time Estimate**: [Duration]
- **Discovery Source**: Video - [Video Title]
- **Discovery Date**: [YYYY-MM-DD]

## Task Description

**ACTION**: [Action verb from Section 5]
**OBJECT**: [Object from Section 9]
**CONTEXT**: [Context/method/tool/purpose]

**Objective**: [What this task achieves - from OBJECTIVE field]

## Task Details

**INPUT**: [What you start with]
**OUTPUT**: [What task produces]
**SUCCESS_CRITERIA**: [How to know complete]

## Steps

[List steps from STEPS_USED field in Section 4B - reference Step Template names]

1. [STEP_NAME_1] (Reference: [DEPT]-[###]-01_slug.md)
2. [STEP_NAME_2] (Reference: [DEPT]-[###]-02_slug.md)
3. [Continue...]

## Skills Required

[From SKILLS_REQUIRED field in Section 4B]

- "[skill phrase 1 via tool]" (Skill ID: TBD)
- "[skill phrase 2 via tool]" (Skill ID: TBD)

## Tools Used

[From TOOLS field in Section 4B]

- [Tool 1] (Tool ID: [TOOL-ID])
- [Tool 2] (Tool ID: [TOOL-ID])

## Reusability

**Can be reused in:**
[From REUSABLE_IN field in Section 4B]

- [Context 1]
- [Context 2]
- [Context 3]

## Workflows Using This Task

[From Section 4 - which workflows include this task]

- [Workflow 1]
- [Workflow 2]

## Video Reference

**Video**: [Video Title]
**Timestamp**: [MM:SS - MM:SS]
**URL**: [YouTube URL]

---

**Created**: [YYYY-MM-DD]
**Status**: Active
```

4. **Save file**: `TASK_MANAGERS/Task_Templates/[DEPT]/[DEPT]-[###].md`

---

#### Substep 3.3.2: Step Templates (from Section 4C)

**For each Step Template extracted in Section 4C:**

**Target Location**: `ENTITIES/TASK_MANAGERS/Step_Templates/[DEPARTMENT]/`

**File Format**: `[DEPT]-[TASK###]-[STEP##]_slug.md`

**ID Assignment**:
- TASK###: Parent task number
- STEP##: Sequential step number (01, 02, 03...)

**Process:**

1. **Identify Parent Task**: From PARENT_TASKS field in Section 4C
2. **Determine Step Number**: Sequential (01, 02, 03...)
3. **Generate Slug**: Lowercase version of step name with hyphens

**Example**:
- Step name: `SCRAPE_COMPANY_DATA_FROM_AIRSCALE`
- Parent task: AI-007 (ENRICH_LEADS_MULTI-SOURCE)
- Step number: 01 (first step)
- File: `AI-007-01_scrape-company-data-from-airscale.md`

4. **Create Step Template File**:

```markdown
# Step Template: [STEP_NAME_ACTION_OBJECT_SPECIFIC_DETAIL]

## Metadata

| Field | Value |
|-------|-------|
| Step ID | [DEPT]-[TASK###]-[STEP##] |
| Step Name | [ACTION_OBJECT_SPECIFIC_DETAIL] |
| Parent Task(s) | [TASK_NAME_1], [TASK_NAME_2] |
| Department | [Department] |
| Complexity | [Low/Medium/High] |
| Time Estimate | [Duration] |
| Tool | [Primary Tool] |

## Step Description

**ACTION**: [Verb]
**OBJECT**: [What step acts upon]
**TOOL**: [Primary tool used]

[Brief description from Section 4C]

## Prerequisites

[From PREREQUISITES field in Section 4C]

- [Prerequisite 1]
- [Prerequisite 2]

## Input/Output

**INPUT**: [What this step receives]
**OUTPUT**: [What this step produces]

## Instructions

[From INSTRUCTIONS field in Section 4C - 3-8 bullet points]

1. [Instruction 1]
2. [Instruction 2]
3. [Instruction 3]
4. [Continue...]

## Parent Tasks

This step is used in:

[From PARENT_TASKS field in Section 4C]

- [TASK_NAME_1] ([DEPT]-[###])
- [TASK_NAME_2] ([DEPT]-[###])

## Reusability

**Can be reused in:**

[From REUSABLE_IN field in Section 4C]

- [Context 1]
- [Context 2]

## Video Reference

**Video**: [Video Title]
**Timestamp**: [MM:SS - MM:SS]
**URL**: [YouTube URL]

---

**Created**: [YYYY-MM-DD]
**Status**: Active
```

5. **Save file**: `TASK_MANAGERS/Step_Templates/[DEPT]/[DEPT]-[TASK###]-[STEP##]_slug.md`

---

### Step 3.4: Skills Integration

**For each skill extracted in Section 7B:**

**Target Location**: `ENTITIES/TALENTS/Skills/`

**File Format**: `SKL-[###]_[skill_slug].json`

**ID Assignment**: Sequential (check highest SKL number)

**Process:**

1. **Check Next Available ID**:
   - Look in `TALENTS/Skills/`
   - Find highest SKL-### (e.g., SKL-042)
   - Next ID: SKL-043

2. **Generate File Slug**:
   - Take skill phrase: "enriched emails via Anymailfinder"
   - Convert to slug: `enriched_emails_via_anymailfinder`

3. **Create Skill JSON File**:

```json
{
  "entity_type": "TALENTS",
  "sub_entity": "Skill",
  "skill_id": "SKL-###",
  "skill_name": "ACTION_OBJECT_VIA_TOOL",
  "skill_phrase": "[action in past tense] [object] via [tool]",
  "difficulty": "Beginner|Intermediate|Advanced|Expert",
  "professions": [
    "Profession 1",
    "Profession 2"
  ],
  "parent_tasks": [
    "TASK_NAME_1",
    "TASK_NAME_2"
  ],
  "workflows": [
    "Workflow Name 1",
    "Workflow Name 2"
  ],
  "tools_required": [
    {
      "tool_name": "Tool 1",
      "tool_id": "TOOL-CATEGORY-###"
    },
    {
      "tool_name": "Tool 2",
      "tool_id": "TOOL-CATEGORY-###"
    }
  ],
  "time_to_learn": "X minutes/hours",
  "description": "Brief explanation of what this skill enables (from Section 7B)",
  "discovery_date": "2025-11-17",
  "discovery_source": "video_transcription",
  "video_reference": {
    "title": "Video Title",
    "url": "YouTube URL",
    "timestamp": "MM:SS"
  }
}
```

4. **Save file**: `TALENTS/Skills/SKL-###_skill_slug.json`

---

### Step 3.5: Update Mappings

#### Update tool_mapping.json

**For each NEW tool created:**

Add entry to `TASK_MANAGERS/tool_mapping.json`:

```json
{
  "Anymailfinder": {
    "tool_id": "TOOL-DATA-006",
    "category": "Data_Tools",
    "file_path": "/Users/nikolay/Library/CloudStorage/Dropbox/ENTITIES/LIBRARIES/Tools/Data_Tools/Anymailfinder.json"
  }
}
```

**Process:**

1. Open tool_mapping.json
2. Add new entry for each tool
3. Keep alphabetical order (optional but helpful)
4. Save file

---

#### Update discovered_tools.json

**For each NEW tool created:**

Add entry to `TASK_MANAGERS/discovered_tools.json`:

```json
{
  "tools": [
    {
      "name": "Anymailfinder",
      "tool_id": "TOOL-DATA-006",
      "category": "Data_Tools",
      "status": "active",
      "discovery_date": "2025-11-17",
      "discovery_source": "video_transcription",
      "video_reference": "Video Title"
    }
  ]
}
```

**Process:**

1. Open discovered_tools.json
2. Add to "tools" array
3. Set status to "active" (newly created tools are validated)
4. Save file

---

### Step 3.6: Coverage & Gap Analysis

#### Calculate Coverage Metrics

**Formula**:

```
Coverage % = (Existing items / Total items mentioned) × 100
```

**Before Video Processing**:
- Tools in library: X
- Task Templates: Y
- Step Templates: Z
- Skills: W

**After Video Processing**:
- Tools in library: X + N (N new tools added)
- Task Templates: Y + M
- Step Templates: Z + P
- Skills: W + Q

**Coverage Improvement**:
- Tools: Was X%, now (X+N)% → Improved by N%
- Tasks: Was Y%, now (Y+M)% → Improved by M%
- Steps: Was Z%, now (Z+P)% → Improved by P%
- Skills: Was W%, now (W+Q)% → Improved by Q%

---

#### Create Gap Analysis Report

**Template**:

```markdown
# Video Processing Gap Analysis Report

## Video Information

- **Video Title**: [Title]
- **Processing Date**: [YYYY-MM-DD]
- **Processed By**: [Name]
- **Video URL**: [YouTube URL]

---

## Summary

### Tools
- **Total mentioned in video**: [Count]
- **Existing in library before**: [Count]
- **New tools added**: [Count]
- **Existing tools enhanced**: [Count]
- **Coverage improvement**: X% → Y% (+Z%)

### Tasks
- **Task Templates extracted**: [Count]
- **Task Templates created**: [Count]

### Steps
- **Step Templates extracted**: [Count]
- **Step Templates created**: [Count]

### Skills
- **Skills identified**: [Count]
- **Skills created**: [Count]

---

## Actions Taken

### New Tool Entries Created

1. **[Tool Name]** (TOOL-ID: [TOOL-CATEGORY-###])
   - Category: [Category]
   - File: LIBRARIES/Tools/[Category]/[ToolName].json
   - Use cases: [Count] use cases from video

2. [Continue for all new tools]

### Existing Tool Entries Enhanced

1. **[Tool Name]** (TOOL-ID: [TOOL-ID])
   - Added [X] new use cases
   - Added [Y] workflows
   - Updated description with video context
   - Enhanced integration_capabilities

2. [Continue for all enhanced tools]

### Task Templates Created

1. **[TASK_NAME]** ([DEPT]-[###])
   - Department: [Department]
   - Complexity: [Level]
   - File: TASK_MANAGERS/Task_Templates/[DEPT]/[DEPT]-[###].md

2. [Continue for all tasks]

### Step Templates Created

1. **[STEP_NAME]** ([DEPT]-[TASK###]-[STEP##])
   - Parent Task: [TASK_NAME]
   - Tool: [Tool]
   - File: TASK_MANAGERS/Step_Templates/[DEPT]/[file].md

2. [Continue for all steps]

### Skills Created

1. **"[skill phrase via tool]"** (SKL-###)
   - Difficulty: [Level]
   - Parent Tasks: [Count] tasks
   - File: TALENTS/Skills/SKL-###_slug.json

2. [Continue for all skills]

---

## Coverage Metrics

### Before Video Processing

| Category | Count | Coverage % |
|----------|-------|------------|
| Tools | [X] | [%] |
| Task Templates | [Y] | [%] |
| Step Templates | [Z] | [%] |
| Skills | [W] | [%] |

### After Video Processing

| Category | Before | After | Added | Improvement |
|----------|--------|-------|-------|-------------|
| Tools | [X] | [X+N] | +[N] | +[%] |
| Task Templates | [Y] | [Y+M] | +[M] | +[%] |
| Step Templates | [Z] | [Z+P] | +[P] | +[%] |
| Skills | [W] | [W+Q] | +[Q] | +[%] |

---

## Recommendations

### High Priority

1. **[Recommendation 1]**
   - Reason: [Why important]
   - Action: [What to do]
   - Impact: [Expected benefit]

2. [Continue...]

### Medium Priority

[Continue...]

### Future Improvements

[Continue...]

---

## Next Steps

- [ ] Review new tool entries for completeness
- [ ] Test Task Templates in real workflows
- [ ] Validate Step Template instructions
- [ ] Update related documentation
- [ ] Share findings with [Departments]

---

**Report Generated**: [YYYY-MM-DD]
**Next Video Processing**: [Date]
```

---

### Stage 3 Checklist

**Before Starting:**
- [ ] Stage 2 transcription complete (all 14 sections)
- [ ] tool_mapping.json accessible
- [ ] discovered_tools.json accessible
- [ ] LIBRARIES/Tools structure accessible

**Tool Processing:**
- [ ] All tools from Section 8 checked against library
- [ ] New tools assigned proper IDs (sequential in category)
- [ ] New tool JSON files created with complete schema
- [ ] Existing tools enriched with video context
- [ ] tool_mapping.json updated

**Task & Step Integration:**
- [ ] Task Templates created (Section 4B)
- [ ] Task IDs assigned (sequential per department)
- [ ] Step Templates created (Section 4C)
- [ ] Step IDs linked to parent tasks
- [ ] All files saved in correct directories

**Skills Integration:**
- [ ] Skills extracted (Section 7B)
- [ ] Skill IDs assigned (sequential SKL-###)
- [ ] Skills linked to parent tasks
- [ ] Skills linked to tools
- [ ] Skill JSON files created

**Mappings:**
- [ ] tool_mapping.json updated with new tools
- [ ] discovered_tools.json updated
- [ ] Cross-references validated

**Gap Analysis:**
- [ ] Coverage metrics calculated
- [ ] Before/after comparison documented
- [ ] Gap analysis report created
- [ ] Recommendations documented

---

### Stage 3 Output

**Deliverables:**

1. **Updated LIBRARIES/Tools/**
   - New tool JSON files (e.g., Anymailfinder.json, MCP_Builder.json)
   - Enhanced existing tool files (e.g., Claude.json with MCP context)

2. **Updated tool_mapping.json**
   - New tool mappings added
   - Tool ID assignments documented

3. **Task Templates**
   - New .md files in TASK_MANAGERS/Task_Templates/[DEPT]/
   - Format: [DEPT]-[###].md

4. **Step Templates**
   - New .md files in TASK_MANAGERS/Step_Templates/[DEPT]/
   - Format: [DEPT]-[TASK###]-[STEP##]_slug.md

5. **Skills**
   - New JSON files in TALENTS/Skills/
   - Format: SKL-###_skill_slug.json

6. **Gap Analysis Report**
   - Coverage metrics (before/after)
   - Actions taken summary
   - Recommendations for future

---

**Stage 3 Complete! Video processing workflow finished.**

---

# PART 5: INTEGRATION & EXECUTION

## Data Flow & Integration Points

### Complete Data Flow Visualization

```
┌─────────────────────────────────────────────┐
│  STAGE 1 OUTPUT: Research Results          │
│  ─────────────────────────────────────────  │
│  File: Research_Results_2025-11-17.md      │
│  Contains:                                  │
│  • 8-12 scored videos                      │
│  • Top 3-5 selected (score 80+)           │
│  • Video URLs, metadata                    │
│  • Relevance justification                 │
└─────────────────────────────────────────────┘
              ↓ (Handoff: Video URLs)
┌─────────────────────────────────────────────┐
│  STAGE 2 INPUT: Video URLs                 │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  STAGE 2 PROCESSING                         │
│  ─────────────────────────────────────────  │
│  1. Transcribe video (Google AI Studio)    │
│  2. Extract 14 taxonomy sections           │
│  3. Analyze with 3-phase methodology       │
│  4. Quality validation                     │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  STAGE 2 OUTPUT: Transcription Document    │
│  ─────────────────────────────────────────  │
│  File: Video_[TITLE]_2025-11-17.md        │
│  Contains:                                  │
│  • Full transcription (Sections 1-3)      │
│  • 14 taxonomy sections:                   │
│    - Workflows (4)                         │
│    - Task Templates (4B)                   │
│    - Step Templates (4C)                   │
│    - Skills (7B)                           │
│    - Tools Matrix (8)                      │
│    - Success Metrics (14)                  │
│    - [All other sections]                  │
└─────────────────────────────────────────────┘
              ↓ (Handoff: Structured data)
┌─────────────────────────────────────────────┐
│  STAGE 3 INPUT: Transcription + Mappings   │
│  ─────────────────────────────────────────  │
│  • Transcription document                  │
│  • tool_mapping.json                       │
│  • discovered_tools.json                   │
│  • Existing LIBRARIES                      │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  STAGE 3 PROCESSING                         │
│  ─────────────────────────────────────────  │
│  1. Validate tools (check existing)        │
│  2. Create/enhance tool entries            │
│  3. Create Task Templates                  │
│  4. Create Step Templates                  │
│  5. Create skills                          │
│  6. Update mappings                        │
│  7. Generate gap analysis                  │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  STAGE 3 OUTPUT: Updated Libraries          │
│  ─────────────────────────────────────────  │
│  1. LIBRARIES/Tools/                       │
│     • New: Anymailfinder.json              │
│     • Enhanced: Claude.json                │
│                                            │
│  2. TASK_MANAGERS/Task_Templates/          │
│     • AI-007.md (new)                      │
│     • Sales-012.md (new)                   │
│                                            │
│  3. TASK_MANAGERS/Step_Templates/          │
│     • AI-007-01_scrape-data.md (new)       │
│     • AI-007-02_enrich-emails.md (new)     │
│                                            │
│  4. TALENTS/Skills/                        │
│     • SKL-043_enriched_emails.json (new)   │
│                                            │
│  5. Mappings:                              │
│     • tool_mapping.json (updated)          │
│     • discovered_tools.json (updated)      │
│                                            │
│  6. Gap Analysis Report                    │
│     • Coverage metrics                     │
│     • Recommendations                      │
└─────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────┐
│  FEEDBACK LOOP                              │
│  ─────────────────────────────────────────  │
│  Gap analysis → Informs next research      │
│  • Tool gaps → Search for tool tutorials  │
│  • Workflow gaps → Find workflow videos   │
│  • Metric needs → Prioritize ROI videos   │
└─────────────────────────────────────────────┘
```

---

## Weekly Workflow Schedule

### Monday: Research Day

**Time**: 2-3 hours

**Activities**:
1. Review daily reports and strategic priorities (30 min)
2. Run searches with research prompts (60 min)
   - Perplexity AI: 8-12 videos per focus area
   - YouTube: Validate findings
3. Score all videos using 0-100 system (60 min)
   - Strategic Alignment (0-40)
   - Tool/Tech Relevance (0-30)
   - Actionable Value (0-30)
4. Create research results document (30 min)

**Output**: `Research_Results_2025-11-XX.md` with scored videos

---

### Tuesday: Selection & Prioritization

**Time**: 1 hour

**Activities**:
1. Review Monday's research results (15 min)
2. Finalize video scores (15 min)
3. Select top 3-5 videos (scores 80+) (15 min)
4. Create watchlist with priorities (10 min)
5. Assign videos to team members if applicable (5 min)

**Output**: Prioritized video list, assignments

---

### Wednesday: Video Processing (Day 1)

**Time**: 2-3 hours

**Activities**:
1. Watch top video (15-25 min)
2. Transcribe using Google AI Studio (10-15 min)
3. Apply v3.2 custom instructions (40-60 min)
   - Sections 1-3: Core transcription
   - Sections 4-7: Workflows, tasks, steps, skills
4. Initial quality check (10 min)

**Output**: Partial transcriptions (sections 1-7 complete)

---

### Thursday: Video Processing (Day 2) & Analysis

**Time**: 2-3 hours

**Activities**:
1. Complete taxonomy extraction (60 min)
   - Sections 8-14: Tools, objects, integration patterns, metrics
2. Deep analysis (3-phase methodology) (60 min)
   - Phase 1: Initial review
   - Phase 2: Deep extraction
   - Phase 3: Taxonomy mapping
3. Quality validation (20 min)
4. Calculate coverage metrics (10 min)

**Output**: Complete transcription documents, analysis notes

---

### Friday: Library Population & Sharing

**Time**: 1-2 hours

**Activities**:
1. Tool validation and enrichment (30 min)
   - Check existing tools
   - Create new tool JSON files
   - Enhance existing tools
2. Create task/step/skill templates (30 min)
3. Update tool_mapping.json (10 min)
4. Generate gap analysis report (20 min)
5. Share findings with departments (10 min)

**Output**: Updated libraries, gap analysis, team communication

---

### Time Allocation Summary

| Day | Stage | Time | Cumulative | Output |
|-----|-------|------|------------|--------|
| **Monday** | Research | 2-3 hrs | 2-3 hrs | Research results |
| **Tuesday** | Selection | 1 hr | 3-4 hrs | Video list |
| **Wednesday** | Processing 1 | 2-3 hrs | 5-7 hrs | Partial transcripts |
| **Thursday** | Processing 2 | 2-3 hrs | 7-10 hrs | Complete transcripts |
| **Friday** | Population | 1-2 hrs | 8-12 hrs | Updated libraries |
| **TOTAL** | **All Stages** | **8-12 hrs** | **Week** | **3-5 videos processed** |

---

### Monthly Cycle

**Week 1: Critical Priority Topics**
- File System & Workflow Automation
- Natural Language Automation (Opal AI)

**Week 2: Video & Analytics**
- Open-Source Video Generation (WAN 2.2, Runway)
- Real-Time Analytics & Dashboards

**Week 3: Business Processes**
- Lead Generation Strategy
- AI Agents & Agentic Workflows (Claude MCP)

**Week 4: Department-Specific Needs**
- Discord Automation
- Project Management Tools
- Development Tools (Cursor, Windsurf)

---

## Quality Assurance & Metrics

### Stage-by-Stage Quality Criteria

**Stage 1 (Research) - Quality Checks:**
- [ ] 8-12 videos identified
- [ ] All videos scored using 0-100 system
- [ ] Score breakdown provided (Strategic + Tech + Actionable)
- [ ] Top 3-5 videos selected (minimum 80/100 score)
- [ ] Department relevance identified
- [ ] One-sentence value proposition written
- [ ] Research results documented

**Stage 2 (Processing) - Quality Checks:**
- [ ] Video transcribed with timestamps (every 30-60 sec)
- [ ] All 14 sections populated
- [ ] Task Templates use ACTION_OBJECT_CONTEXT naming
- [ ] Step Templates use ACTION_OBJECT_SPECIFIC_DETAIL naming
- [ ] Skills use "action via tool" format
- [ ] Tasks linked to steps (STEPS_USED field)
- [ ] Skills linked to tasks (PARENT_TASKS field)
- [ ] Tools matrix in table format
- [ ] Success metrics include values and context
- [ ] Output is markdown (.md), not JSON

**Stage 3 (Population) - Quality Checks:**
- [ ] All tools checked against library
- [ ] New tools assigned proper IDs (TOOL-CATEGORY-###)
- [ ] Tool JSON files follow complete schema
- [ ] Task Templates created with proper structure
- [ ] Step Templates linked to parent tasks
- [ ] Skills created with task/tool linkage
- [ ] tool_mapping.json updated
- [ ] discovered_tools.json updated
- [ ] Coverage metrics calculated
- [ ] Gap analysis report created

---

### Success Metrics

**Time Efficiency:**
- Stage 1: 2-3 hours/week → 8-12 videos researched
- Stage 2: 40-80 minutes/video → 90-95% time savings
- Stage 3: 10-20 minutes/video → 99% time savings vs manual
- **Total per video**: 50-100 minutes (vs 4.5-9.5 hours pre-v3.2)

**Quality Metrics:**
- **Video Relevance**: 80%+ of videos score 80+ relevance
- **Transcription Completeness**: 100% of 14 sections populated
- **Tool Coverage**: 90%+ of mentioned tools integrated
- **Task Extraction**: 3-5+ Task Templates per video
- **Step Extraction**: 5-10+ Step Templates per video
- **Skill Identification**: 3-5+ skills per video

**Library Impact (Track Monthly):**
- Tool Library Growth: +[N] tools/month
- Task Template Library Growth: +[M] tasks/month
- Step Template Library Growth: +[P] steps/month
- Skills Library Growth: +[Q] skills/month
- Coverage Improvement: Track before/after each video

---

### Validation Checkpoints

**After Research (Stage 1):**
```
Review Checklist:
✓ Videos aligned with strategic priorities?
✓ Scores accurately reflect relevance?
✓ Top videos actionable and tutorial-focused?
✓ Department relevance clear?

Approval: Team Lead or Research Coordinator
```

**After Processing (Stage 2):**
```
Review Checklist:
✓ Transcription complete with timestamps?
✓ All 14 taxonomy sections filled?
✓ Naming conventions match standards?
✓ Links between tasks/steps/skills present?

Approval: AI Team Lead or Taxonomy Coordinator
```

**After Population (Stage 3):**
```
Review Checklist:
✓ All new tools properly categorized?
✓ Tool IDs follow sequential format?
✓ Task/step/skill files created correctly?
✓ tool_mapping.json updated?
✓ Gap analysis shows improvement?

Approval: Library Maintainer or Taxonomy Lead
```

---

## Quick Start Guide

### For First-Time Users

**Step 1: Setup (30 minutes)**

1. **Read this complete document** (45-60 minutes)
   - Part 1: Overview
   - Part 2: Stage 1 (Research)
   - Part 3: Stage 2 (Processing)
   - Part 4: Stage 3 (Population)

2. **Review key prompt documents**:
   - `YouTube_Video_Research_Prompt_RemoteHelpers_Nov2025.md`
   - `Video_Transcription_Custom_Instructions_v3.2.md`
   - `Video_Analysis_Prompt.md`
   - `Tools_Collection_and_Matching_Prompt.md`

3. **Set up tools**:
   - Perplexity AI account (for research)
   - Google AI Studio account (for transcription)
   - Text editor for markdown (VS Code, etc.)
   - Access to LIBRARIES and TASK_MANAGERS directories

4. **Familiarize with directory structure**:
   ```
   ENTITIES/
   ├── LIBRARIES/Tools/[15 categories]/
   ├── TASK_MANAGERS/
   │   ├── Task_Templates/[DEPT]/
   │   ├── Step_Templates/[DEPT]/
   │   ├── tool_mapping.json
   │   └── discovered_tools.json
   └── TALENTS/Skills/
   ```

5. **Shadow experienced team member** (1 full video cycle)

---

### For Starting a New Week

**Monday Morning Routine:**
- [ ] Review strategic priorities for current week
- [ ] Check department requests
- [ ] Review previous week's gap analysis (what topics to prioritize)
- [ ] Run research (Stage 1) - 2-3 hours

**Tuesday Morning:**
- [ ] Review Monday's research results
- [ ] Select top 3-5 videos (scores 80+)
- [ ] Assign to team members or self

**Wed-Thu:**
- [ ] Process videos (Stage 2) - 40-80 min each
- [ ] Validate quality (checklists)

**Friday:**
- [ ] Populate libraries (Stage 3) - 10-20 min each
- [ ] Generate gap analysis
- [ ] Share findings with teams

---

### For Processing a Single Video

**Complete Workflow (90-100 minutes total):**

1. **Watch video** (15-25 min) - Take initial notes
2. **Transcribe** (10-15 min) - Google AI Studio
3. **Extract taxonomy** (40-60 min) - Apply v3.2 instructions
4. **Validate quality** (10 min) - Use checklists
5. **Integrate into libraries** (10-20 min) - Stage 3 process
6. **Generate gap analysis** (5 min) - Quick report

---

### You're Ready When You Can:

- [ ] Score videos using the 0-100 system confidently
- [ ] Apply v3.2 custom instructions to extract taxonomy
- [ ] Understand task/step/skill naming conventions
- [ ] Create tool JSON files with proper IDs
- [ ] Link tasks, steps, and skills correctly
- [ ] Generate gap analysis reports
- [ ] Complete full workflow in under 100 minutes

---

## Key Takeaways

### What Makes This Workflow Effective

**1. Strategic Alignment**
- Research driven by actual work priorities
- Relevance scoring ensures high-value content
- Department-specific focus

**2. Structured Extraction**
- v3.2 custom instructions enable direct taxonomy extraction
- 14 comprehensive sections capture all elements
- Naming conventions ensure consistency

**3. Library Integration**
- Tools validated and enriched (not just listed)
- Tasks, steps, skills linked together
- Coverage metrics track improvement

**4. Time Efficiency**
- 90-95% reduction in processing time
- Parallel processing possible (multiple team members)
- Reusable templates minimize rework

**5. Feedback Loop**
- Gap analysis informs next research cycle
- Library metrics guide strategic focus
- Continuous improvement of process

---

### Success Indicators

**✅ You're doing it right when:**
- Videos selected score 80+ relevance consistently
- All 14 taxonomy sections populated per video
- Task/step/skill templates created with proper naming
- Tool coverage improves with each video (track %)
- Processing time stays under 100 minutes per video
- Gap analysis shows library growth
- Departments use populated libraries for actual work

**❌ Red flags to watch for:**
- Videos selected have low scores (<70)
- Taxonomy sections incomplete or missing
- Naming conventions not followed
- Tasks not linked to steps
- Processing time exceeds 2 hours per video
- Tool coverage stagnant or declining
- Libraries not used by teams

---

### Remember

This workflow saves **90-95% time** vs manual processing.

**Follow the structure**, use the naming conventions, and link all elements together.

**The more videos you process, the richer your libraries become!**

---

## Version History

**Version 3.0** (November 17, 2025) - **Complete Expanded Edition**
- **ADDED**: Full expansion of all 4 prompts in one document
- **ADDED**: Complete Research methodology (Stage 1) with all scoring templates
- **ADDED**: Complete Transcription instructions v3.2 (Stage 2) with all 14 sections
- **ADDED**: Complete Analysis methodology (Stage 2) with 3-phase workflow
- **ADDED**: Complete Library Processing instructions (Stage 3) with all processes
- **ADDED**: Weekly workflow schedule with time allocations
- **ADDED**: Quality assurance checklists for all stages
- **ADDED**: Quick Start Guide for new users
- **FORMAT**: Single comprehensive document for complete workflow execution

---

**Maintained By**: Taxonomy Team / AI Team
**Last Updated**: November 17, 2025
**Status**: Active - Production Ready
**Next Review**: December 17, 2025

**For Questions or Improvements**: Contact AI Team Lead or Taxonomy Coordinator

---

**END OF COMPLETE VIDEO WORKFLOW FULL INSTRUCTIONS**

---

**USAGE NOTE**: This document is intentionally comprehensive. For specific stages, refer to individual prompt files. For complete end-to-end execution, this document contains everything you need.

---
