---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: README_Library
title: README Library
date: 2025-11-17
status: archived
owner: unknown
related: []
links: []
---

# README Library

## Summary
- TODO

## Context
- TODO

## Data / Content
# AI Tutorial Researches Library

**Purpose**: Run deep researches on Perplexity to find lists of newly published video tutorials by influencers about usage of AI and possible tasks that can be done.

**Location**: `TASK_MANAGERS/RESEARCHES/`

**Last Updated**: 2025-11-13

---

## Overview

This library contains research findings from systematic Perplexity searches focused on discovering:
- **Newly published video tutorials** about AI tools and workflows
- **Influencers and content creators** in the AI education space
- **Emerging AI tools and techniques** gaining traction
- **Practical use cases** and task demonstrations
- **Educational content** for AI adoption and implementation

**Key Characteristics**:
- **Research-driven**: Systematic Perplexity searches with structured queries
- **Recency-focused**: Only newly published content (typically last 7-30 days)
- **Influencer-tracked**: Monitoring key content creators and emerging voices
- **Educational**: Focus on tutorials and how-to content
- **Actionable**: Feeds directly into Transcriptions library workflow

**Integration with Taxonomy**:
- **AI_Tutorials**: Discovers new tutorial videos via Perplexity searches (weekly research sessions)
- **Videos**: Transcribes discovered videos and extracts taxonomy (tools, actions, processes)
- **Influencer_Tracking**: Monitors YouTube channels and creators for new content
- **Tools Library**: New tools discovered in videos get added to taxonomy
- **SMM**: Social media marketing research patterns and workflows
- **Complete Pipeline**: Perplexity Discovery → Video Transcription → Taxonomy Extraction → Library Updates

---

## File Structure

```
Researches/
├── README_Library.md (this file)
├── RESEARCH_INDEX.json (master log of all research sessions)
├── AI_Tutorials/
│   ├── Weekly_Searches/
│   │   ├── 2025-11-W46_AI_Tutorials_Research.json
│   │   ├── 2025-11-W45_AI_Tutorials_Research.json
│   │   └── ...
│   ├── Influencer_Tracking/
│   │   ├── Influencer_Database.json
│   │   ├── YouTube_Channels.json
│   │   └── README.md
│   └── Tools_Discovered/
│       ├── New_Tools_2025-11.json
│       └── Tool_Trends_Analysis.md
├── Videos/ (video transcription & taxonomy extraction)
│   ├── README.md
│   ├── VIDEOS_INDEX.md
│   ├── Video_001.md through Video_009.md
│   └── Reports/
│       ├── Video_001_Library_Mapping_Report.md
│       └── [other analysis reports]
└── SMM/ (social media marketing research)
```

### Naming Conventions

**Research Files**:
- Format: `YYYY-MM-WXX_[Category]_Research.json`
- Example: `2025-11-W46_AI_Tutorials_Research.json`
- Contains: Search queries, findings, metadata, next actions

**Tracking Files**:
- Format: `[Type]_[Period].json`
- Example: `New_Tools_2025-11.json`, `Influencer_Database.json`
- Contains: Aggregated data across multiple research sessions

**Analysis Reports**:
- Format: `[Type]_Trends_Analysis.md`
- Example: `Tool_Trends_Analysis.md`
- Contains: Monthly/quarterly trend analysis and insights

---

## Workflow: From Perplexity Search to Taxonomy Integration

### Phase 1: Search Execution
**Frequency**: Weekly (recommended)  
**Tool**: Perplexity  
**Duration**: 15-30 minutes per search session

**Search Query Templates**:
- `"newly published AI video tutorials [this week/month] 2025"`
- `"latest [AI tool name] tutorials by influencers"`
- `"how to use [AI tool] tutorial published [date range]"`
- `"[influencer name] new AI videos [month] 2025"`
- `"AI automation tutorials for [profession/use case]"`

**Query Strategies**:
- Use specific date ranges (e.g., "last 7 days", "November 2025")
- Include platform names when relevant (YouTube, TikTok)
- Combine tool names with "tutorial" or "how to"
- Target specific use cases or professions
- Track known influencers by name

**Output**: Raw Perplexity results with URLs, titles, dates

### Phase 2: Result Filtering
**Process**: Evaluate search results against quality criteria  
**Duration**: 20-40 minutes

**Filtering Criteria**:
- ✅ **Recency**: Published within target date range (typically 7-30 days)
- ✅ **Relevance**: Focuses on AI tool usage and practical tasks
- ✅ **Source**: From recognized AI influencers OR emerging credible creators
- ✅ **Quality**: Minimum engagement threshold (views, likes, comments)
- ✅ **Educational Value**: Tutorial/how-to format, not just news or opinion
- ✅ **Accessibility**: Video is public and accessible

**Filtering Process**:
1. Check publication date
2. Verify creator credibility (follower count, content history, expertise)
3. Assess video description and title for relevance
4. Check engagement metrics (views relative to channel size)
5. Verify video is tutorial/demonstration format

**Output**: Curated list of high-quality video tutorials meeting all criteria

### Phase 3: Data Extraction
**Process**: Capture comprehensive metadata for each video  
**Duration**: 5-10 minutes per video

**Data to Extract**:
- **Video Metadata**: Title, URL, platform, published date, duration
- **Creator Info**: Name, channel/profile URL, subscriber/follower count
- **Content Analysis**: Topics covered, AI tools mentioned, use cases demonstrated
- **Engagement**: View count, like count, comment count
- **Classification**: Category, relevance score, tutorial quality
- **Transcript Status**: Available/unavailable (for future transcription)

**Extraction Methods**:
- Manual review of video description and preview
- Platform metadata (YouTube API, if needed)
- Perplexity result details
- Quick video preview (first 2-3 minutes)

**Output**: Structured JSON records for each video finding

### Phase 4: Categorization & Analysis
**Process**: Organize findings and identify patterns  
**Duration**: 15-20 minutes

**Categories**:
- **AI Coding Tools**: Claude, Cursor, GitHub Copilot, Replit
- **AI Content Creation**: ChatGPT, Jasper, Copy.ai, content writing
- **AI Video/Image Generation**: Midjourney, Runway, Pika, DALL-E
- **AI Workflow Automation**: n8n, Make, Zapier with AI nodes
- **AI Data Analysis**: Data analysis, ChatGPT for analytics
- **Multi-tool Integrations**: Workflows combining multiple AI tools
- **AI for Specific Professions**: Marketing, design, development, etc.

**Analysis Tasks**:
- Assign primary and secondary categories
- Identify AI tools mentioned (new and existing)
- Note emerging trends (tool popularity, use case patterns)
- Assess tutorial quality and educational value
- Flag high-priority videos for transcription

**Output**: Categorized findings with analysis notes

### Phase 5: Taxonomy Integration & Gap Analysis
**Process**: Map findings to existing taxonomy and identify gaps  
**Duration**: 20-30 minutes

**Integration Steps**:
1. **Check Tools Library**:
   - Search for each AI tool mentioned in `../Tools/AI_Tools/`
   - Identify tools NOT in taxonomy (gaps)
   - Note new use cases for existing tools
2. **Check Influencer Tracking**:
   - Verify if influencer is in tracking database
   - Add new influencers with metadata
   - Update existing influencer records
3. **Cross-Reference Transcriptions**:
   - Check if video already transcribed in `../Transcribations/`
   - Avoid duplicates
   - Link to existing transcriptions if found
4. **Identify Workflows**:
   - Note multi-step workflows demonstrated
   - Check against `../Processes/` library
   - Flag new workflow patterns

**Gap Analysis**:
- **New Tools Count**: X tools not in taxonomy
- **New Influencers Count**: X creators not tracked
- **New Use Cases**: X use cases not documented
- **Transcription Candidates**: Top X videos for transcription priority

**Output**: Gap analysis report with prioritized action items

### Phase 6: Tracking & Trend Monitoring
**Process**: Aggregate data across research sessions to identify trends  
**Duration**: 15-20 minutes (monthly)

**Metrics to Track**:
- **Tool Popularity**: Which AI tools are most frequently tutorialized
- **Emerging Tools**: New tools appearing in recent weeks
- **Influencer Activity**: Most active creators in AI education space
- **Use Case Trends**: Which professions/tasks are getting most coverage
- **Tutorial Formats**: What teaching styles are most popular
- **Platform Trends**: Where AI tutorials are being published

**Trend Analysis**:
- Compare current week to previous weeks
- Calculate growth rates for tool mentions
- Identify breakout tools/influencers
- Spot emerging use case categories
- Detect shifts in educational content focus

**Output**: Monthly trend report highlighting key insights

### Phase 7: Workflow Continuation & Action Items
**Process**: Determine next steps and integrate with broader workflow  
**Duration**: 10-15 minutes

**Action Item Categories**:
1. **Transcription Queue**:
   - Add top-priority videos to `../Transcribations/` processing queue
   - Prioritize based on: tool novelty, use case relevance, tutorial quality
   - Assign transcription priority level (High/Medium/Low)
2. **Tools Library Updates**:
   - Create new tool entries for discovered tools
   - Update existing tools with new use cases
   - Add video references to tool documentation
3. **Influencer Follow-Up**:
   - Follow new influencers on relevant platforms
   - Add to monitoring list for future searches
   - Note content frequency and typical topics
4. **Search Refinement**:
   - Update search queries based on findings
   - Add new query templates for emerging categories
   - Schedule next research session
5. **Reporting**:
   - Document key findings in weekly summary
   - Share notable discoveries with relevant teams
   - Update metrics dashboard

**Output**: Prioritized action list with ownership and deadlines

---

## Data Structure & Fields

### Research Session Record

Each research session is saved as a JSON file with the following structure:

```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Research",
  "category": "AI_Tutorials",
  "research_session": {
    "research_id": "RSH-AI-001",
    "search_date": "2025-11-13",
    "search_week": "2025-W46",
    "search_tool": "Perplexity",
    "researcher": "AI Research Team",
    "session_duration_minutes": 60
  },
  "search_queries": [],
  "findings": [],
  "session_metadata": {},
  "discovery_summary": {},
  "gap_analysis": {},
  "next_research_session": {},
  "tags": [],
  "cross_references": {},
  "notes": ""
}
```

(...full field descriptions retained from the original README...)

---

*Remaining sections for Field Explanations, Quality Standards, Metrics, Examples, Best Practices, Maintenance Schedule, Support & Resources, and Quick Start Guide are identical to the original README and preserved or updated in this file to keep the research playbook centralized.*



## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-17 standardization scaffold added
