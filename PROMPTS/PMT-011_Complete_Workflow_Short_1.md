# Complete Video Workflow - Short Version

**Version**: 3.0 Quick Reference
**Date**: November 17, 2025
**Purpose**: Condensed guide for video processing workflow

---

## Overview

Transform videos into actionable knowledge through 3 stages:
1. **Research** - Find relevant videos (2-3 hours/week)
2. **Processing** - Transcribe & extract data (40-80 min/video)
3. **Population** - Integrate into libraries (10-20 min/video)

**Time Savings**: 90-95% reduction vs manual processing

---

## STAGE 1: Research & Discovery

### Search Platforms
- **Primary**: Perplexity AI (Creativity: 0.5, Structure mode ON)
- **Secondary**: YouTube Direct Search
- **Filters**: Last 30-60 days, 10-40 minutes duration

### Scoring System (0-100 points)

**Strategic Alignment (0-40 pts)**
- 40 pts: Critical Priority Topics (file automation, video generation, lead gen)
- 30 pts: High Priority Topics (AI agents, Discord automation, project mgmt)
- 20 pts: Tangentially related
- 10 pts: General relevance
- 0 pts: No alignment

**Tool/Tech Relevance (0-30 pts)**
- 30 pts: 3+ tools from our stack
- 20 pts: 1-2 tools from our stack
- 10 pts: Compatible/integrable tools
- 0 pts: Unrelated tools

**Actionable Value (0-30 pts)**
- 30 pts: Step-by-step tutorial with code
- 20 pts: Clear implementation path
- 10 pts: Conceptual with some practical tips
- 0 pts: Pure theory/hype

### Selection Criteria
- **Minimum score**: 70/100
- **Weekly target**: 3-5 videos
- **Priority**: Score 80+ (Critical Priority topics)

---

## STAGE 2: Transcription & Extraction

### Tool
**Primary**: Google AI Studio (videos <100 MB)
**Alternative**: Transcribe AI (larger videos)

### Required Output Format
**⚠️ CRITICAL**: Markdown (.md) ONLY - NOT JSON

### Document Structure

#### 1. Metadata
```
- Video Title
- Channel/Creator
- Video URL
- Duration
- Publication Date
- Transcription Date
```

#### 2. Video Description
- Full description
- Key topics covered
- Links referenced

#### 3. Word-for-Word Transcription
- Timestamps every 30-60 seconds
- [TEXT: ...] for on-screen text
- [VISUAL: ...] for demonstrations

#### 4. Workflows Identification
For each workflow:
- Department
- Objective
- Steps (numbered list)
- Duration
- Complexity (Low/Medium/High/Very High)
- Tools used
- Input/Output
- Timestamp

#### 4B. Task Templates (v3.2)
**Format**: `ACTION_OBJECT_CONTEXT` (ALL_CAPS)
**Example**: `ENRICH_LEADS_MULTI-SOURCE`

For each task:
- Department
- Action verb
- Object (plural)
- Context
- Complexity & time estimate
- Steps used
- Skills required
- Tools
- Success criteria
- Reusability contexts

#### 4C. Step Templates (v3.2)
**Format**: `ACTION_OBJECT_SPECIFIC_DETAIL` (ALL_CAPS)
**Example**: `SCRAPE_COMPANY_DATA_FROM_AIRSCALE`

For each step:
- Parent task
- Action & object
- Tool/platform
- Instructions (clear, actionable)
- Prerequisites
- Validation
- Troubleshooting
- Time estimate

### Naming Conventions

**Task Templates**: `ACTION_OBJECT_CONTEXT`
- ✅ `ENRICH_LEADS_MULTI-SOURCE`
- ❌ `enrich_leads` (not ALL_CAPS)

**Step Templates**: `ACTION_OBJECT_SPECIFIC_DETAIL`
- ✅ `UPLOAD_CSV_TO_ANYMAILFINDER`
- ❌ `UPLOAD_DATA` (too generic)

**Skills**: `"[action] [object] via [tool]"` (lowercase)
- ✅ `"enriched emails via Anymailfinder"`
- ❌ `"enrich emails"` (missing tool)

---

## STAGE 3: Library Population

### Process

1. **Collect Tools from Transcript**
   - Extract all tools mentioned
   - Check against existing libraries
   - Identify new vs existing

2. **Create/Enrich Tool Entries**
   - Use JSON schema for new tools
   - Enrich existing tools with new data
   - Add tasks, workflows, integrations

3. **Categorize Tools**
   - Primary category (main function)
   - Secondary categories
   - Use standard taxonomy

4. **Update Mappings**
   - Add to tool_mapping.json
   - Link tasks to tools
   - Link skills to tools

5. **Gap Analysis**
   - Tools mentioned but not in library
   - Missing integrations
   - Incomplete documentation

### Tool JSON Schema
```json
{
  "tool_id": "TOOL_XXX",
  "name": "Tool Name",
  "category": "Primary Category",
  "subcategories": ["Sub1", "Sub2"],
  "description": "Clear description",
  "key_features": ["Feature 1", "Feature 2"],
  "use_cases": ["Use case 1", "Use case 2"],
  "integrations": ["Tool A", "Tool B"],
  "pricing": "Free/Paid/Freemium",
  "url": "https://...",
  "tasks": ["TASK_ID_1", "TASK_ID_2"],
  "skills": ["skill phrase 1", "skill phrase 2"]
}
```

### Categories
- AI & LLMs
- Development
- Video Production
- Design
- Automation
- Business & Analytics
- Data & Lead Generation

---

## Weekly Schedule

**Monday**: Research cycle (2-3 hours)
- Review priorities
- Search videos
- Score & select 3-5 videos

**Tuesday-Thursday**: Processing (40-80 min/video)
- Transcribe videos
- Extract taxonomy data
- Generate task/Step Templates

**Friday**: Library population (10-20 min/video)
- Validate tools
- Update libraries
- Generate gap analysis

---

## Quick Start

1. **Start with Research**
   - Use current priorities from daily reports
   - Search on Perplexity AI
   - Score videos using 0-100 system
   - Select top 3-5 (score 80+)

2. **Process Videos**
   - Use Google AI Studio for transcription
   - Follow v3.2 extraction format
   - Output complete markdown document
   - Validate naming conventions

3. **Populate Libraries**
   - Extract all tools
   - Create/enrich tool entries
   - Update mappings
   - Run gap analysis

---

## Success Metrics

**Per Video Output**:
- 5-8 tools discovered
- 2-4 Task Templates
- 6-10 Step Templates
- 3-5 skills identified

**Weekly Output** (3-5 videos):
- 15-25 tools integrated
- 10-20 Task Templates
- 30-50 Step Templates
- 15-25 skills identified

**Time Investment**:
- Stage 1: 2-3 hours/week
- Stage 2: 40-80 min/video
- Stage 3: 10-20 min/video
- **Total**: 8-12 hours/week

---

## Critical Priorities (November 2025)

### 🔥 Critical (40 pts)
1. File system & workflow automation (Claude Code, Cursor IDE)
2. Natural language automation (Opal AI MiniApps)
3. Open-source video generation (WAN 2.2, Runway Gen-3)
4. Real-time analytics dashboards
5. Lead generation strategy optimization

### 📊 High Priority (30 pts)
6. AI agents & agentic workflows (MCP integration)
7. Discord server automation
8. Project management & documentation
9. Business process automation
10. AI development tools

---

## Key Action Verbs (for Task Templates)

**A. Create**: Generate, Build, Design, Compose, Draft, Develop
**B. Process**: Transform, Convert, Extract, Parse, Transcribe
**C. Organize**: Categorize, Sort, Structure, Tag, Index
**D. Enrich**: Enhance, Append, Augment, Validate, Verify
**E. Analyze**: Evaluate, Assess, Review, Compare, Calculate
**F. Automate**: Schedule, Trigger, Chain, Orchestrate
**G. Communicate**: Send, Notify, Alert, Report, Share

---

## Common Objects (for Templates)

**Data Types**: Leads, Contacts, Companies, Emails, Domains, Lists
**Content**: Videos, Documents, Transcripts, Reports, Summaries
**Workflows**: Campaigns, Automations, Pipelines, Processes
**Outputs**: Dashboards, Templates, Configs, Integrations

---

## Validation Checklist

### Stage 1 Complete
- ☐ 3-5 videos selected (score 80+)
- ☐ All videos documented with URLs
- ☐ Relevance scores justified

### Stage 2 Complete
- ☐ Markdown format (.md, not JSON)
- ☐ All 14 sections present
- ☐ Naming conventions followed
- ☐ Task Templates extracted
- ☐ Step Templates extracted
- ☐ Skills identified

### Stage 3 Complete
- ☐ All tools collected
- ☐ New tools added to libraries
- ☐ Existing tools enriched
- ☐ Mappings updated
- ☐ Gap analysis generated

---

**End of Short Version**

For full details, see: `Complete_Video_Workflow_Full_Instructions.md`
