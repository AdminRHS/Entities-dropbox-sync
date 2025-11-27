---
category: ARCHIVE
subcategory: 04_INFLUENCER_DATA
type: analysis
source_id: README
title: README
date: 2025-11-21
status: archived
owner: unknown
related: []
links: []
---

# README

## Summary
- TODO

## Context
- TODO

## Data / Content
# AI Tutorial Influencer & Creator Tracking

**Purpose**: Track YouTube channels and multi-platform influencers who create AI tutorial content for content discovery, collaboration opportunities, and trend monitoring.

**Location**: `LIBRARIES/Researches/AI_Tutorials/Influencer_Tracking/`

**Last Updated**: 2025-11-13

---

## Overview

This directory contains databases and tracking systems for AI tutorial creators and influencers discovered through:
- Video transcriptions (from `../../Videos/`)
- Perplexity research sessions (from `../Weekly_Searches/`)
- External discovery and recommendations

**Integration with Research Workflow**:
```
Perplexity Research → Discover Videos → Identify Creators →
Add to Database → Monitor Content → Transcribe Priority Videos → Repeat
```

**Total Influencers Tracked**: 6
**Primary Platform**: YouTube (expandable to Instagram, TikTok, Twitter, LinkedIn)

---

## Database Files

### 1. Influencer_Database.json
**Primary database** tracking all influencers across platforms.

**Structure**:
- Influencer profiles with unique IDs (INF-AI-XXX)
- Multi-platform presence tracking
- Content classification and topics
- Engagement metrics and tier classification
- Collaboration potential assessment
- Monitoring priorities and schedules

**Key Fields**:
- `influencer_id`: Unique identifier
- `name`: Creator/channel name
- `platforms`: Multi-platform presence (YouTube, Instagram, TikTok, etc.)
- `content_classification`: Topics, categories, formats
- `engagement_metrics`: Tier, quality ratings, engagement rates
- `collaboration_potential`: Contact status, partnership types
- `tracking`: Monitoring priority, tags, last updated

### 2. YouTube_Channels.json
**YouTube-specific tracking** with detailed channel metrics.

**Structure**:
- Channel-specific metrics (subscribers, views, upload frequency)
- Videos transcribed in taxonomy
- Content analysis (focus, types, quality)
- Monitoring schedule and frequency

**Key Fields**:
- `channel_id`: YouTube-specific ID (YT-AI-XXX)
- `influencer_id`: Links to Influencer_Database
- `metrics`: Subscriber count, views, video count, frequency
- `videos_in_taxonomy`: List of transcribed videos
- `tracking`: Check frequency, priority, notes

### 3. Platform_Coverage.json (To be created)
**Future**: Track influencer presence across multiple platforms for cross-platform strategies.

---

## Influencer Tiers

Classification based on follower/subscriber count:

| Tier | Followers/Subscribers | Characteristics |
|------|----------------------|-----------------|
| **Mega** | 1M+ | Celebrity-level reach, very expensive |
| **Macro** | 500K-1M | High reach, expensive, brand deals |
| **Mid** | 100K-500K | Balanced reach and cost, professional |
| **Micro** | 10K-100K | High engagement, affordable, niche experts |
| **Nano** | 1K-10K | Highest engagement, very affordable, personal |

**Current Distribution**:
- Mid: 1 (Matthew Berman or Matt Wolfe)
- Micro: 2 (Cole, Nick Saraev/Leftclick)
- Nano-Micro: 2 (Darren Wiener, D-Squared)

---

## Content Categories

**Current Influencers by Category**:

1. **AI Models & Reviews** (1): Matthew Berman
   - Focus: Frontier models, benchmarks, comparisons

2. **AI Tools & Tutorials** (1): Matt Wolfe
   - Focus: Tool demos, weekly roundups, productivity

3. **AI Development & Tech Stacks** (1): Cole
   - Focus: Developer tools, infrastructure, RAG systems

4. **B2B Marketing & Sales Automation** (1): Nick Saraev/Leftclick
   - Focus: Lead generation, web scraping, sales automation

5. **Claude Code & Business Automation** (1): Darren Wiener
   - Focus: Claude Code, skills, sub-agents, business OS

6. **Claude MCP & No-Code Automation** (1): D-Squared
   - Focus: MCP connectors, no-code automation, productivity

---

## Monitoring Priorities

### High Priority (Weekly checks)
- **INF-AI-001**: Matthew Berman - Frequent uploads, model news
- **INF-AI-002**: Matt Wolfe - Comprehensive tool coverage
- **INF-AI-004**: Nick Saraev/Leftclick - High-value B2B content

### Medium Priority (Bi-weekly to Monthly)
- **INF-AI-003**: Cole - Technical deep-dives
- **INF-AI-005**: Darren Wiener - Course-based content
- **INF-AI-006**: D-Squared - MCP specialist

---

## Workflow: Adding New Influencers

### Discovery
1. **Source Identification**:
   - Video transcription (creator name found in video)
   - Perplexity research (new tutorial discovered)
   - Recommendation or external discovery

2. **Initial Research**:
   - Find channel/profile URL
   - Estimate subscriber/follower count
   - Review recent content (3-5 videos)
   - Assess content quality and relevance

### Data Capture
3. **Create Database Entry** in `Influencer_Database.json`:
   ```json
   {
     "influencer_id": "INF-AI-XXX",
     "name": "Creator Name",
     "primary_platform": "YouTube",
     "platforms": { ... },
     "content_classification": { ... },
     "discovery": {
       "discovery_source": "Video_XXX or Research session",
       "discovery_date": "YYYY-MM-DD",
       "referenced_in": ["Video_XXX"],
       "discovery_notes": "..."
     },
     ...
   }
   ```

4. **Add YouTube Details** (if applicable) in `YouTube_Channels.json`:
   ```json
   {
     "channel_id": "YT-AI-XXX",
     "influencer_id": "INF-AI-XXX",
     "channel_name": "...",
     "metrics": { ... },
     "videos_in_taxonomy": [ ... ]
   }
   ```

### Integration
5. **Link to Research**:
   - Update `../../Videos/VIDEOS_INDEX.md` with creator info
   - Reference in research session that discovered them
   - Add to monitoring schedule based on priority

---

## Maintenance Schedule

### After Each Research Session (Weekly)
- [ ] Add newly discovered creators to database
- [ ] Update existing creator records with new videos found
- [ ] Check high-priority channels for new content
- [ ] Flag high-value videos for transcription

### Monthly Tasks
- [ ] Review all medium-priority channels
- [ ] Update subscriber/follower count estimates
- [ ] Assess content quality trends
- [ ] Identify inactive creators (no uploads in 60+ days)
- [ ] Generate monthly discovery report

### Quarterly Tasks
- [ ] Comprehensive database audit
- [ ] Update tier classifications
- [ ] Review collaboration potential
- [ ] Analyze content trend shifts
- [ ] Expand to new platforms (Instagram, TikTok, etc.)

---

## Collaboration Framework

### Contact Status Levels
- **Not contacted**: No outreach yet
- **Contacted**: Initial outreach sent
- **In discussion**: Active conversation
- **Negotiating**: Terms being discussed
- **Active partner**: Ongoing collaboration
- **Past partner**: Previous collaboration completed
- **Not interested**: Declined collaboration

### Partnership Types
1. **Content Exchange**: Cross-promotion, guest appearances
2. **Tool Promotion**: Sponsored demos, affiliate links
3. **Case Study**: Feature in tutorial, success story
4. **Course Collaboration**: Co-created educational content
5. **Affiliate**: Commission-based promotion
6. **Sponsored Content**: Paid promotion deals

---

## Quality Standards

### Minimum Criteria for Tracking
- ✅ **Content Focus**: AI tools, tutorials, or workflows
- ✅ **Content Quality**: Minimum "Medium" rating
- ✅ **Educational Value**: Minimum "Medium" rating
- ✅ **Active Status**: Uploaded within last 90 days
- ✅ **Discoverability**: Public channel, accessible content

### Data Quality Requirements
- [ ] Influencer ID assigned (INF-AI-XXX format)
- [ ] Name and primary platform documented
- [ ] At least one platform profile URL captured
- [ ] Content category assigned
- [ ] Discovery source documented
- [ ] Monitoring priority set
- [ ] Tags added for searchability

---

## Usage Examples

### Example 1: Finding Creators by Topic
**Goal**: Find all influencers covering Claude Code

**Process**:
1. Open `Influencer_Database.json`
2. Search for "Claude" in `content_topics` or `tags`
3. Results: INF-AI-005 (Darren Wiener), INF-AI-006 (D-Squared)

### Example 2: Weekly Content Check
**Goal**: Check high-priority channels for new videos

**Process**:
1. Reference `monitoring_priorities.High` in database
2. Visit each channel (INF-AI-001, INF-AI-002, INF-AI-004)
3. Note new videos published since last check
4. Flag relevant videos for transcription
5. Update `last_content_check` dates

### Example 3: Collaboration Outreach
**Goal**: Reach out to micro-tier B2B influencer

**Process**:
1. Filter by `influencer_tier: "Micro"` and `content_classification.primary_category: "B2B"`
2. Result: INF-AI-004 (Nick Saraev/Leftclick)
3. Review `collaboration_potential` notes
4. Draft outreach based on `partnership_type_potential`
5. Update `contact_status` to "Contacted"

---

## Metrics & KPIs

### Discovery Metrics
- New influencers added per month: X
- Discovery sources breakdown: X% videos, X% research, X% external
- Platform distribution: X% YouTube, X% Instagram, etc.

### Engagement Metrics
- Average tier distribution across influencers
- Average content quality rating: X.X/5
- Average educational value rating: X.X/5

### Activity Metrics
- Active influencers (uploaded in last 30 days): X/6
- Videos transcribed per influencer: X average
- Collaboration partnerships: X active, X completed

---

## Cross-References

### Integration Points
- **Videos Library**: `../../Videos/VIDEOS_INDEX.md` - Creator names and channel URLs
- **Research Sessions**: `../Weekly_Searches/` - Discovery notes from Perplexity searches
- **Tools Discovered**: `../Tools_Discovered/` - Tools mentioned by influencers
- **Parent Research Library**: `../../README.md` - Overall Researches workflow

### Data Flow
```
Perplexity Search → Discover Video → Extract Creator Info →
Add to Influencer_Database → Update YouTube_Channels →
Link in VIDEOS_INDEX → Queue for Transcription →
Discover Tools → Update Tools Library
```

---

## Future Enhancements

### Platform Expansion
- [ ] Instagram influencer tracking
- [ ] TikTok creator database
- [ ] Twitter/X AI educators
- [ ] LinkedIn AI thought leaders

### Feature Additions
- [ ] Platform_Coverage.json for cross-platform analysis
- [ ] Collaboration_History.json for partnership tracking
- [ ] Content_Performance.json for video/post metrics
- [ ] Trend_Analysis.json for topic trending over time

### Automation Opportunities
- [ ] Automated subscriber count updates (YouTube API)
- [ ] New video alerts (RSS feeds or API)
- [ ] Engagement rate calculations
- [ ] Automated quality scoring based on views/likes

---

## Related Documentation

- [Researches Library README](../../README.md) - Parent library overview
- [Videos Library README](../../Videos/README.md) - Video transcription workflow
- [AI_Tutorials Research](../README.md) - Perplexity research methodology (to be created)
- [RESEARCH_INDEX.json](../../RESEARCH_INDEX.json) - Master research tracking

---

**Maintained By**: AI Research Team
**Status**: Active
**Version**: 1.0
**Last Updated**: 2025-11-13
**Total Influencers**: 6 (all from video transcriptions)

---

**End of README**


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
