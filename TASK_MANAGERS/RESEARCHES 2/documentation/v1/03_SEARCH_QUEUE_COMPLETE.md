# 03_SEARCH_QUEUE_COMPLETE.md

**Complete Documentation of Phase 0: Video Search Assignment System**

**Last Updated:** 2025-12-04
**Location:** `00_SEARCH_QUEUE/`
**Purpose:** Assign and track video search tasks
**Scripts:** 2 (assign_search.py, complete_search.py)

---

## Table of Contents

1. [Overview](#overview)
2. [Phase 0 in Context](#phase-0-in-context)
3. [Search Queue Workflow](#search-queue-workflow)
4. [File Structure](#file-structure)
5. [Using the Scripts](#using-the-scripts)
6. [Search Strategies](#search-strategies)
7. [Best Practices](#best-practices)
8. [Examples](#examples)
9. [Troubleshooting](#troubleshooting)

---

## Overview

### Purpose

**Phase 0 (Search Queue)** is the initial phase where video search tasks are assigned to employees based on research needs, weekly reports, and departmental gaps.

### Key Objectives

1. **Identify Research Gaps**: Analyze what knowledge/tools are missing
2. **Create Search Assignments**: Generate targeted search tasks
3. **Track Search Progress**: Monitor assigned vs completed searches
4. **Measure Results**: Track videos found per search
5. **Feed Video Queue**: Discovered videos → Phase 0→1 (Video Queue)

### Why Phase 0 Matters

```
Without Phase 0:
- Random video selection
- No strategic focus
- Missed opportunities
- Duplicate research
- Poor ROI

With Phase 0:
- Targeted discovery
- Gap-driven research
- Systematic coverage
- Tracked assignments
- High-value videos
```

### Position in Workflow

```
Phase 0: SEARCH QUEUE ← YOU ARE HERE
│ Purpose: Assign video search tasks
│ Input: Research gaps, weekly reports, requests
│ Output: Search assignments (SEARCH-XXX)
│ Scripts: assign_search.py, complete_search.py
│ Time: 5-10 min per assignment
└──→

Phase 0→1: VIDEO QUEUE
│ Purpose: Collect and prioritize discovered videos
│ Input: Videos found from searches (SEARCH-XXX)
│ Output: Prioritized queue (VQ-XXX)
└──→

Phase 1: TRANSCRIPTION
[Continues to Phase 5...]
```

---

## Phase 0 in Context

### Integration Points

**Input Sources:**
- Weekly gap analysis reports
- Department research requests
- Tool/feature announcements
- Industry trends
- User feedback
- Strategic priorities

**Output Destinations:**
- Phase 0→1: Videos discovered → Video Queue
- Employee assignments
- Search completion tracking
- Research coverage metrics

### Success Metrics

| Metric | Target | Purpose |
|--------|--------|---------|
| Searches Assigned | 3-5/week | Systematic coverage |
| Completion Rate | >80% | Assignment effectiveness |
| Videos Per Search | 5-15 | Search quality |
| Queue Addition Rate | 10-25/week | Pipeline health |
| Search-to-Process | 15-20% | Prioritization accuracy |

---

## Search Queue Workflow

### Complete Workflow Diagram

```
┌─────────────────────────────────────┐
│ INPUTS (Research Needs)             │
├─────────────────────────────────────┤
│ • Weekly gap analysis reports       │
│ • Department requests               │
│ • New tool announcements            │
│ • Industry trends                   │
│ • Strategic priorities              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ STEP 1: Identify Search Topic       │
├─────────────────────────────────────┤
│ What: Specific research area needed │
│ Why: Gap to fill or trend to track  │
│ Who: Department/team needing it     │
│ Priority: Urgency level             │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ STEP 2: Create Search Assignment    │
├─────────────────────────────────────┤
│ Script: assign_search.py            │
│ Input:                              │
│   - Employee name                   │
│   - Department (DEV/DGN/AID/etc)    │
│   - Topic                           │
│   - Search query (optional)         │
│   - Notes (optional)                │
│ Output:                             │
│   - SEARCH-XXX ID generated         │
│   - CSV entry created               │
│   - Status: "Assigned"              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ STEP 3: Employee Executes Search    │
├─────────────────────────────────────┤
│ Employee:                           │
│ 1. Reviews search assignment        │
│ 2. Uses search query/develops own   │
│ 3. Searches YouTube, Perplexity     │
│ 4. Evaluates video relevance        │
│ 5. Notes promising videos           │
│ 6. Counts total found               │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ STEP 4: Add Videos to Queue         │
├─────────────────────────────────────┤
│ For each promising video:           │
│ Script: add_video_to_queue.py       │
│ Input:                              │
│   - YouTube URL                     │
│   - Employee name                   │
│   - Topic                           │
│   - Source: SEARCH-XXX              │
│ Output:                             │
│   - VQ-XXX ID generated             │
│   - Priority calculated             │
│   - Added to Video Queue            │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ STEP 5: Complete Search Assignment  │
├─────────────────────────────────────┤
│ Script: complete_search.py          │
│ Input:                              │
│   - SEARCH-XXX ID                   │
│   - Videos found count              │
│   - Completion notes                │
│ Output:                             │
│   - Status: "Completed"             │
│   - Date completed recorded         │
│   - Videos found tracked            │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ OUTPUTS (Discovered Videos)         │
├─────────────────────────────────────┤
│ • Videos in queue (VQ-XXX)          │
│ • Search completion tracking        │
│ • Coverage metrics                  │
│ • Research gap reduction            │
└─────────────────────────────────────┘
```

### Workflow Steps Detail

#### Step 1: Identify Search Topic (5 minutes)

**Questions to Answer:**
- What knowledge/tools are we missing?
- Which department needs this?
- How urgent is this research?
- What specific content should we find?

**Sources for Topics:**
- Weekly gap analysis: "We're missing X tool coverage"
- Department requests: "Sales needs lead gen tools"
- Announcements: "New Claude features released"
- Trends: "Agentic AI becoming popular"
- Strategy: "Focus on HR automation this quarter"

**Topic Examples:**
```
Good Topics (Specific):
✅ "Claude Sonnet 4.5 new features 2025"
✅ "Figma AI plugins for designers"
✅ "n8n automation workflows for HR"
✅ "Lead generation with AI tools"

Poor Topics (Too Broad):
❌ "AI tools"
❌ "Design software"
❌ "Automation"
❌ "New videos"
```

#### Step 2: Create Assignment (2 minutes)

**Using assign_search.py:**

```bash
# Basic assignment
python 00_SEARCH_QUEUE/scripts/assign_search.py \
  "John Doe" \
  "DEV" \
  "Claude Sonnet 4.5 new features"

# With search query
python 00_SEARCH_QUEUE/scripts/assign_search.py \
  "Jane Smith" \
  "DGN" \
  "Figma AI plugins" \
  "figma ai plugin 2025 tutorial"

# With notes
python 00_SEARCH_QUEUE/scripts/assign_search.py \
  "Mike Johnson" \
  "AID" \
  "n8n automation for HR" \
  "n8n hr onboarding workflow" \
  "Focus on practical examples, not theory"
```

**What Happens:**
1. Generates SEARCH-001 (or next sequential number)
2. Creates CSV entry with:
   - Search ID
   - Employee name
   - Department
   - Topic
   - Search query (if provided)
   - Status: "Assigned"
   - Date assigned
3. Employee is notified (manual or automated)

#### Step 3: Execute Search (30-60 minutes)

**Employee Process:**

1. **Review Assignment**
   - Read topic and notes
   - Understand what to find
   - Note any specific requirements

2. **Develop Search Strategy**
   - Use provided query or create own
   - Choose search platforms
   - Set filters (date, duration, etc.)

3. **Search Platforms**

   **YouTube Direct:**
   ```
   Search: "claude sonnet 4.5 features 2025"
   Filters:
   - Upload date: Last 30 days
   - Sort by: Relevance
   - Duration: 10-30 minutes
   ```

   **Perplexity AI:**
   ```
   Query: "Find YouTube videos about Claude Sonnet 4.5
          new features from last 30 days with practical
          examples and tutorials"
   ```

   **Google:**
   ```
   site:youtube.com "claude sonnet 4.5" "tutorial"
   after:2025-11-01
   ```

4. **Evaluate Videos**
   - Watch first 2-3 minutes
   - Check content quality
   - Verify relevance to topic
   - Note if worth processing

5. **Document Findings**
   - Keep list of promising videos
   - Note total videos found
   - Record search effectiveness

#### Step 4: Add to Video Queue (5-10 min per video)

**For Each Promising Video:**

```bash
# Add with full details
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
  "https://youtube.com/watch?v=abc123" \
  "John Doe" \
  "Claude AI" \
  "SEARCH-001" \
  "Excellent tutorial on new features"

# Quick add (batch mode)
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py \
  "https://youtube.com/watch?v=def456"
```

**Selection Criteria:**
- High-quality content (good production)
- Relevant to topic
- Practical/actionable
- Recent (unless evergreen)
- Good engagement (views/likes)
- Trusted source

#### Step 5: Complete Assignment (2 minutes)

```bash
# Mark search complete
python 00_SEARCH_QUEUE/scripts/complete_search.py \
  SEARCH-001 \
  12 \
  "Found 12 videos, added 4 high-priority to queue"

# If no videos found
python 00_SEARCH_QUEUE/scripts/complete_search.py \
  SEARCH-002 \
  0 \
  "Topic too narrow, no relevant content found. Suggest broader search."
```

---

## File Structure

### Folder Organization

```
00_SEARCH_QUEUE/
├── README.md                          # This documentation
├── Search_Queue_Master.csv            # Main tracking file
│
├── scripts/
│   ├── assign_search.py               # Assign new search
│   └── complete_search.py             # Mark search complete
│
├── Search_Prompts/                    # Generated search prompts
│   ├── DEV_Weekly_Searches.md
│   ├── DGN_Weekly_Searches.md
│   ├── AID_Weekly_Searches.md
│   └── [Department]_[Timeframe]_Searches.md
│
├── Active_Searches/                   # In-progress searches
│   ├── SEARCH-001_Details.md
│   ├── SEARCH-002_Details.md
│   └── [Optional tracking files]
│
└── Completed_Searches/                # Completed search reports
    ├── SEARCH-001_Report.md
    ├── 2025-Week-48_Summary.md
    └── [Historical records]
```

### Search_Queue_Master.csv Structure

```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
SEARCH-001,John Doe,DEV,Claude Sonnet 4.5 features,claude sonnet 4.5 2025,Completed,12,2025-12-01,2025-12-02,Found excellent tutorials
SEARCH-002,Jane Smith,DGN,Figma AI plugins,figma ai plugin tutorial,In Progress,0,2025-12-02,,Currently searching
SEARCH-003,Mike Johnson,AID,n8n HR automation,n8n onboarding workflow,Assigned,0,2025-12-03,,Assigned today
```

**Field Definitions:**

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Search_ID | String | Unique identifier | SEARCH-001 |
| Employee | String | Assigned employee | John Doe |
| Department | String | Department code | DEV, DGN, AID, HR, Sales |
| Topic | String | Search topic | "Claude Sonnet 4.5 features" |
| Search_Query | String | Specific search query | "claude sonnet 4.5 2025" |
| Status | Enum | Current status | Assigned, In Progress, Completed |
| Videos_Found | Integer | Total videos discovered | 12 |
| Date_Assigned | Date | Assignment date | 2025-12-01 |
| Date_Completed | Date | Completion date | 2025-12-02 |
| Notes | Text | Additional notes | "Found excellent tutorials" |

### Status Values

```
Assigned      → Initial state when search is assigned
In Progress   → Employee has started searching
Completed     → Search finished, videos added to queue
On Hold       → Temporarily paused
Cancelled     → Search cancelled (duplicate, no longer needed)
```

---

## Using the Scripts

### Script 1: assign_search.py

**Purpose:** Create new search assignment

**Full Documentation:** See [08_SCRIPTS_DETAILED.md](./08_SCRIPTS_DETAILED.md#1-assign_searchpy)

**Quick Reference:**

```bash
# Syntax
python 00_SEARCH_QUEUE/scripts/assign_search.py \
  <employee> \
  <department> \
  <topic> \
  [search_query] \
  [notes]

# Examples
python assign_search.py "John Doe" "DEV" "Claude AI tutorials"

python assign_search.py "Jane Smith" "DGN" "Figma plugins" "figma ai 2025"

python assign_search.py "Mike" "HR" "Onboarding automation" "hr onboarding ai" "Urgent"
```

**Output:**
```
✓ Search assigned: SEARCH-001
✓ Employee: John Doe
✓ Department: DEV
✓ Topic: Claude AI tutorials
✓ Status: Assigned
✓ Entry added to Search_Queue_Master.csv
```

---

### Script 2: complete_search.py

**Purpose:** Mark search as completed

**Full Documentation:** See [08_SCRIPTS_DETAILED.md](./08_SCRIPTS_DETAILED.md#2-complete_searchpy)

**Quick Reference:**

```bash
# Syntax
python 00_SEARCH_QUEUE/scripts/complete_search.py \
  <search_id> \
  <videos_found> \
  [notes]

# Examples
python complete_search.py SEARCH-001 12

python complete_search.py SEARCH-002 8 "Added 3 to high priority queue"

python complete_search.py SEARCH-003 0 "Topic too narrow, no results"
```

**Output:**
```
✓ Search completed: SEARCH-001
✓ Videos found: 12
✓ Status updated: Completed
✓ Completion date: 2025-12-02
✓ CSV updated
```

---

## Search Strategies

### Platform-Specific Strategies

#### YouTube Direct Search

**Advantages:**
- Direct access to all videos
- Advanced filters available
- Can see full metadata
- Real-time results

**Search Strategy:**

```
1. Basic Search:
   "claude sonnet 4.5"

2. Add Context:
   "claude sonnet 4.5 tutorial"

3. Add Timeframe:
   "claude sonnet 4.5 tutorial 2025"

4. Filters:
   - Upload date: Last 30 days
   - Duration: 10-30 minutes
   - Sort by: Relevance or Upload date

5. Evaluate:
   - Channel credibility
   - View count
   - Engagement (likes, comments)
   - Recency
```

**Example Searches:**

```
Technical Topics:
- "claude api integration python tutorial 2025"
- "figma auto layout plugin tutorial"
- "n8n workflow automation examples"

Tool Discovery:
- "new ai tools december 2025"
- "best ai design tools 2025"
- "ai automation tools for [department]"

Comparison/Analysis:
- "claude vs chatgpt comparison 2025"
- "best ai model for coding"
- "figma vs sketch ai features"
```

#### Perplexity AI Search

**Advantages:**
- AI-curated results
- Multiple sources
- Summarized content
- Quality filtering

**Search Strategy:**

```
1. Natural Language Query:
   "Find YouTube videos about Claude Sonnet 4.5 new features
    from last 30 days with practical examples"

2. Specify Quality:
   "Find high-quality YouTube tutorials on [topic] with code
    examples from verified channels"

3. Department-Specific:
   "Find YouTube videos for designers showing AI tools for
    UI design automation in 2025"

4. Review Results:
   - Perplexity provides summaries
   - Click through to videos
   - Verify relevance
```

**Example Queries:**

```
"Find recent YouTube tutorials on Claude Sonnet 4.5 API
 integration with practical code examples"

"Discover YouTube videos showing Figma AI plugins for
 designers, uploaded in last 60 days"

"Find YouTube channels teaching n8n automation for HR
 processes with step-by-step workflows"
```

#### Google Advanced Search

**Advantages:**
- Precise filtering
- Date ranges
- Site-specific
- Boolean operators

**Search Strategy:**

```
1. Site-Specific:
   site:youtube.com "claude sonnet 4.5"

2. Date Range:
   site:youtube.com "claude api" after:2025-11-01

3. Exact Phrase:
   site:youtube.com "claude sonnet 4.5" "tutorial"

4. Exclude Terms:
   site:youtube.com "figma plugin" -"paid promotion"

5. Multiple Terms:
   site:youtube.com ("claude" OR "anthropic") "api tutorial"
```

**Example Searches:**

```
site:youtube.com "claude sonnet 4.5" "new features" after:2025-11-01

site:youtube.com intitle:"figma automation" "ai plugin" after:2025-10-01

site:youtube.com "n8n" ("hr" OR "onboarding") "workflow"
```

### Search Quality Tips

**Do's ✅:**
- Use specific terms ("Claude Sonnet 4.5" not "AI")
- Add context ("tutorial", "guide", "how to")
- Filter by date (recent content)
- Check channel credibility
- Watch first 2-3 minutes
- Note engagement metrics
- Document search terms used

**Don'ts ❌:**
- Too broad ("AI tools")
- Too narrow ("Claude Sonnet 4.5 JSON mode batch API Python FastAPI deployment Azure")
- Ignore date filters
- Skip quality check
- Add low-quality videos
- Forget to document

### Topic Development

**Start Broad → Narrow Down:**

```
Level 1 (Too Broad):
"AI tools"
→ Too many results, low relevance

Level 2 (Better):
"AI automation tools 2025"
→ More focused, but still broad

Level 3 (Good):
"AI workflow automation tools for HR 2025"
→ Specific, targeted, actionable

Level 4 (Very Specific):
"n8n workflow automation for HR onboarding"
→ Precise, high-quality results
```

**Topic Refinement Process:**

```
1. Start: "Need HR automation content"

2. Identify: "Specifically onboarding automation"

3. Narrow: "Onboarding automation with n8n"

4. Search: "n8n onboarding workflow automation"

5. Refine if needed:
   - Too few results? Broaden: "n8n hr automation"
   - Too many results? Narrow: "n8n employee onboarding workflow tutorial"
```

---

## Best Practices

### Assignment Best Practices

**Clear Topics:**
```
✅ Good:
- "Claude Sonnet 4.5 vision capabilities tutorials"
- "Figma AI plugin for auto-layout generation"
- "n8n integration with HR systems"

❌ Poor:
- "AI stuff"
- "Design tools"
- "Automation"
```

**Appropriate Scope:**
```
✅ Right Size:
- Expected results: 5-20 videos
- Specific enough to find relevant content
- Broad enough to have options

❌ Too Narrow:
- Expected results: 0-2 videos
- Too specific, no content exists

❌ Too Broad:
- Expected results: 100+ videos
- Too general, can't evaluate all
```

**Strategic Timing:**
```
✅ Good Timing:
- Right after tool announcement
- Beginning of month/quarter
- After gap analysis report
- Before major project

❌ Poor Timing:
- Random assignment
- No strategic purpose
- Duplicate recent searches
```

### Execution Best Practices

**Time Management:**
```
Per Search:
- Planning: 5 minutes
- Searching: 20-30 minutes
- Evaluation: 15-20 minutes
- Adding to queue: 10-15 minutes
- Documentation: 5 minutes
Total: 55-75 minutes per search
```

**Quality Standards:**
```
Videos to Add:
✅ High production value
✅ Trusted source/channel
✅ Practical/actionable content
✅ Recent (unless evergreen)
✅ Good engagement
✅ Relevant to topic

Videos to Skip:
❌ Low quality production
❌ Unknown/untrusted source
❌ Theory only, no practice
❌ Outdated (unless historical)
❌ Low/no engagement
❌ Off-topic
```

**Documentation Standards:**
```
When Completing:
✅ Accurate video count
✅ Specific completion notes
✅ Note search effectiveness
✅ Flag any issues
✅ Suggest improvements

Example Good Notes:
"Found 12 videos total. Added 4 high-quality tutorials
 to queue. Topic has good coverage. Suggest follow-up
 search on advanced features in 2-3 weeks."

Example Poor Notes:
"Done"
```

### Tracking Best Practices

**Regular Reviews:**
```
Daily:
- Check assigned searches
- Update in-progress status
- Complete finished searches

Weekly:
- Review completion rate
- Analyze videos-per-search
- Identify successful topics
- Plan next week's searches

Monthly:
- Overall effectiveness
- Department coverage
- Employee performance
- Adjust strategy
```

**Metrics to Track:**
```
Efficiency:
- Searches assigned: X/week
- Searches completed: X/week
- Completion rate: X%
- Avg time per search: X hours

Quality:
- Videos found per search: X
- Videos added to queue: X
- Videos processed: X
- Search-to-process rate: X%

Coverage:
- Departments covered: X/7
- Topics researched: X
- Gaps filled: X
- Strategic alignment: X%
```

---

## Examples

### Example 1: Strategic Gap-Based Search

**Scenario:** Weekly gap analysis shows missing coverage of Claude Sonnet 4.5 features

**Step 1: Identify Need**
```
Gap: Claude Sonnet 4.5 coverage at 30%
Need: Video tutorials on new features
Priority: High (recent announcement)
Department: AID (AI & Automation)
```

**Step 2: Create Assignment**
```bash
python assign_search.py \
  "John Doe" \
  "AID" \
  "Claude Sonnet 4.5 new features and capabilities" \
  "claude sonnet 4.5 features tutorial 2025" \
  "Focus on practical examples, API integration, and vision capabilities"
```

Output:
```
✓ SEARCH-001 created
✓ Topic: Claude Sonnet 4.5 new features and capabilities
✓ Employee: John Doe
✓ Status: Assigned
```

**Step 3: Execute Search**

John searches:
- YouTube: "claude sonnet 4.5 tutorial 2025"
- Filters: Last 30 days, 10-30 min duration
- Finds: 15 videos total
- Evaluates: Watches first 2-3 min of each
- Selects: 5 high-quality tutorials

**Step 4: Add to Queue**
```bash
# Video 1
python ../01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
  "https://youtube.com/watch?v=abc123" \
  "John Doe" \
  "Claude AI" \
  "SEARCH-001" \
  "Excellent coverage of vision features"

# Videos 2-5
[Similar adds...]
```

**Step 5: Complete**
```bash
python complete_search.py \
  SEARCH-001 \
  15 \
  "Found 15 videos, added 5 high-quality tutorials to queue. Good coverage of new features including vision capabilities, improved context handling, and API updates. Recommend follow-up search on advanced use cases in 2 weeks."
```

**Result:**
- 5 videos in queue (VQ-001 through VQ-005)
- Coverage gap reduced: 30% → 55%
- High-priority content for processing

---

### Example 2: Department Request Search

**Scenario:** Design department requests content on AI plugins for Figma

**Step 1: Department Request**
```
From: Design Team Lead
Request: "Need tutorials on AI-powered Figma plugins for automated layout generation"
Urgency: Medium
Timeline: This week
```

**Step 2: Create Assignment**
```bash
python assign_search.py \
  "Jane Smith" \
  "DGN" \
  "AI-powered Figma plugins for layout automation" \
  "figma ai plugin auto layout 2025" \
  "Design team needs practical tutorials. Focus on plugins that automate component spacing and responsive layouts."
```

**Step 3: Execute Search**

Jane's approach:
1. YouTube: "figma ai plugin tutorial"
2. Perplexity: "Find Figma AI plugins for designers"
3. Google: site:youtube.com "figma" "ai plugin" "layout"
4. Finds: 8 videos
5. Adds: 3 most relevant

**Step 4: Complete**
```bash
python complete_search.py \
  SEARCH-002 \
  8 \
  "Found 8 videos on Figma AI plugins. Added 3 focused on layout automation to queue. Note: Limited content on this specific topic. May need broader search on Figma automation in general."
```

**Outcome:**
- 3 videos added (VQ-006, VQ-007, VQ-008)
- Design team informed
- Note: Consider broader follow-up search

---

### Example 3: Zero Results Search

**Scenario:** Search for very specific topic yields no results

**Step 1: Assignment**
```bash
python assign_search.py \
  "Mike Johnson" \
  "HR" \
  "AI automation for EU GDPR-compliant onboarding" \
  "ai hr onboarding gdpr compliance" \
  "HR needs GDPR-specific content"
```

**Step 2: Execute Search**

Mike's search:
- YouTube: "ai hr onboarding gdpr" → 0 relevant
- Try: "ai hr onboarding compliance" → 2 generic
- Try: "hr automation gdpr" → 1 legal video (not practical)
- Result: No suitable tutorial videos found

**Step 3: Document & Complete**
```bash
python complete_search.py \
  SEARCH-003 \
  0 \
  "No suitable videos found. Topic too specific (GDPR focus). Found 1 legal compliance video but not practical tutorial. RECOMMENDATION: Broaden to 'AI HR onboarding automation' and separately research GDPR compliance requirements."
```

**Follow-Up Action:**
- Create new broader search: "AI HR onboarding automation"
- Separate research: GDPR documentation (not video)
- Consider: Creating own content on this topic

---

## Troubleshooting

### Issue 1: Too Many Results

**Symptoms:**
- Search returns 50+ videos
- Can't evaluate all videos
- Taking too long

**Solutions:**
```
1. Narrow the topic:
   "AI tools" → "AI workflow automation tools for HR"

2. Add timeframe:
   "claude tutorial" → "claude sonnet 4.5 tutorial december 2025"

3. Add specificity:
   "figma plugin" → "figma ai auto-layout plugin tutorial"

4. Filter by quality:
   - Minimum views: 1,000+
   - Duration: 10-30 minutes
   - Channel subscribers: 5,000+
```

### Issue 2: Zero Results

**Symptoms:**
- No relevant videos found
- Topic too specific
- Wasted time

**Solutions:**
```
1. Broaden the topic:
   "n8n gdpr onboarding" → "n8n hr automation"

2. Remove constraints:
   "claude sonnet 4.5 vision api python fastapi" → "claude vision api tutorial"

3. Try alternative terms:
   "figma auto-layout" → "figma layout automation"

4. Consider if content exists:
   - Very new feature? Wait 1-2 weeks
   - Niche topic? May not have videos
   - Wrong platform? Try docs/blogs instead
```

### Issue 3: Low Quality Results

**Symptoms:**
- Videos found but low quality
- Outdated content
- Untrusted sources

**Solutions:**
```
1. Improve search query:
   Add "tutorial", "guide", "official"
   Filter by date (last 30-60 days)

2. Target better channels:
   Add channel names: "anthropic claude tutorial"
   Trusted creators: "[known creator] [topic]"

3. Adjust expectations:
   - Some topics have limited content
   - May need to wait for better content
   - Consider alternative sources

4. Document for team:
   "Limited quality content available. Monitoring for better tutorials."
```

### Issue 4: Duplicate Searches

**Symptoms:**
- Searching same topic again
- Videos already in queue
- Wasted effort

**Solutions:**
```
1. Check before assigning:
   # Search CSV for topic
   grep -i "claude sonnet" Search_Queue_Master.csv

2. Review queue:
   python ../01_VIDEO_QUEUE/video_queue_manager.py
   # Check existing videos on topic

3. Document previous searches:
   Keep history in Completed_Searches/

4. Coordinate with team:
   - Weekly search planning meeting
   - Shared search calendar
   - Check before new assignments
```

### Issue 5: Employee Not Completing

**Symptoms:**
- Searches assigned but not completed
- Status stuck on "Assigned"
- Low completion rate

**Solutions:**
```
1. Follow up:
   - Check with employee
   - Understand blockers
   - Offer help

2. Adjust workload:
   - Too many assignments?
   - Reduce to 1-2 per week
   - Prioritize critical searches

3. Improve clarity:
   - More specific topics
   - Better search queries
   - Clearer expectations

4. Track and address:
   - Monitor completion rates
   - Identify patterns
   - Training if needed
```

---

## Summary

### Phase 0 Checklist

```
Planning:
☐ Identify research gap or need
☐ Define specific topic
☐ Determine department
☐ Set priority level

Assignment:
☐ Run assign_search.py
☐ Verify SEARCH-XXX created
☐ Employee notified
☐ CSV entry confirmed

Execution:
☐ Employee reviews assignment
☐ Develops search strategy
☐ Searches multiple platforms
☐ Evaluates video quality
☐ Selects promising videos

Queue Addition:
☐ Add videos with add_video_to_queue.py
☐ Use SEARCH-XXX as source
☐ Include notes on relevance
☐ Verify VQ-XXX created

Completion:
☐ Run complete_search.py
☐ Record videos found count
☐ Add completion notes
☐ Status updated to "Completed"
☐ Ready for next search
```

### Success Criteria

**Per Search:**
- ✅ Assigned within 1 day of need identification
- ✅ Completed within 2-3 days
- ✅ 5-15 videos discovered
- ✅ 2-5 videos added to queue
- ✅ Clear completion notes

**Overall:**
- ✅ 3-5 searches per week
- ✅ 80%+ completion rate
- ✅ 10-25 videos added to queue per week
- ✅ Strategic coverage of departments
- ✅ Systematic gap reduction

### Key Takeaways

1. **Strategic Focus**: Phase 0 drives strategic video discovery
2. **Quality > Quantity**: 5 good videos > 20 mediocre videos
3. **Clear Topics**: Specific topics yield better results
4. **Document Everything**: Notes improve future searches
5. **Iterate**: Refine based on results

---

**Documentation Complete**

*Last Updated: 2025-12-04*
*Version: 2.0*
*Phase 0 Documentation Complete*

---
