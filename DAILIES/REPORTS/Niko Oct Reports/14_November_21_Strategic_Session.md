# November 21, 2025 - Strategic Session & System Evolution
## Remote Helpers AI-First Organization - W3 Day 4

**Document Version:** 1.0
**Generated:** 2025-11-21
**Total Lines:** ~500

**Source File:**
- W3/211225/211225.md (Raw Whisper Flow transcription)

**Meeting Participants:**
- Niko (CEO/AI Department)
- Stas (AI/Lead Generation)
- Vilhelm (Design)
- Kolya (Development)
- Olya (HR)

**Related LIBRARIES:**
- **Actions:** Scrape, Analyze, Transcribe, Research, Automate, Deploy
- **Objects:** Dashboard, Reviews, Video, Research, Automation, Task
- **Tools:** Google Maps, AI Studio, Cursor, Claude Code, GitHub, Vercel
- **Processes:** Video processing, Review analysis, Research distribution

---

## Executive Summary

November 21st marked a critical strategic session where multiple parallel systems converged: Google Maps scraping evolution, YouTube video research infrastructure, HR dashboard deployment, and AI tools account management. The session demonstrated the maturation of Remote Helpers' AI-first operations with concrete deliverables and systematic approaches.

**Key Achievements:**
- Google Maps review scraping system operational
- HR Attendance Dashboard ready for deployment
- YouTube video research workflow established
- Multi-AI account management system
- Task Manager dashboard conceptualized

---

## 1. Google Maps Scraping Evolution

### 1.1 Strategy Shift

**Previous Approach:**
- Broad, untargeted scraping
- Manual request generation
- Low conversion rates

**New Approach (Nov 21):**
- **Targeted by Junior Entry Positions**
- Profession-specific filtering
- CRM matching automation
- Review-based lead scoring

### 1.2 Scraping Workflow

```
Google Maps Search
  ↓ (AI-generated queries)
Scraper Execution
  ↓
Company Data Extraction
  ├── Company name
  ├── Website
  ├── Google Maps URL
  ├── Category
  └── Review count
  ↓
CRM Matching Check
  ↓
Review Collection (if no match)
```

### 1.3 Search Query Optimization

**Key Insight:**
> "We need to parse the Google Maps URL structure. Extract the query variables and have AI generate optimized search terms based on sales call transcriptions."

**Implementation:**
1. Take existing LinkedIn search queries (thousands accumulated)
2. Feed to Claude/GPT with instruction: "Reformat for Google Maps"
3. Test query categories systematically
4. Analyze which categories yield best results
5. Build query formula: `[3 keywords] × [city] × [country]`

### 1.4 URL Structure Analysis

**Google Maps URL Pattern:**
```
https://maps.google.com/maps/place/[CompanyName]/...
```

**Variables to Extract:**
- Category (after `/place/`)
- Location (city, state)
- Business type identifiers

**AI Task:** Generate category variations programmatically

---

## 2. Review-Based Lead Scoring System

### 2.1 Review Collection Parameters

**Filtering Rules:**
- Maximum 50 reviews per company
- Focus on 4-star and below ratings
- Prioritize recent reviews (newest first)
- Stop at 50 even if more negative reviews exist

**Rationale:**
- Negative reviews indicate pain points
- Recent reviews show current problems
- 50 reviews provide sufficient sample size

### 2.2 Semantic Analysis Pipeline

**Process:**
```
Reviews Collected
  ↓
Semantic Analysis (AI)
  ├── Identify problems by profession
  ├── Map to RH services
  └── Calculate "Problem Score"
  ↓
Profession Matching
  ├── Developers
  ├── Designers
  ├── Video Editors
  └── [other professions]
  ↓
Recommendation Generation
```

### 2.3 Problem Score Calculation

**Formula:**
```
Problem Score = (Negative reviews mentioning profession-specific issues) / (Total reviews analyzed)
```

**Output Columns:**
- Company Name
- Website
- Category
- Review Count
- Average Rating
- Review Velocity (last 90 days)
- **Problem Score** (by profession)
- AI-generated recommendation

### 2.4 Recommendation Engine

**Input:** Company reviews + Problem Score + Profession needs
**Output:** Personalized outreach recommendation

**Example:**
```
Company: XYZ Digital Agency
Problem Score (Designers): 0.32
Issues Identified: "Design inconsistencies", "Missed deadlines", "Quality concerns"
Recommendation: Position RH design services emphasizing quality control and deadline reliability
```

---

## 3. YouTube Video Research Infrastructure

### 3.1 Research Distribution System

**Daily Assignment Goal:**
- Each employee: 1 video per day minimum
- Focus: Tools, automation, AI techniques
- Time commitment: 1-2 hours per person

**Concept:**
> "The system can't evolve if we're recycling the same knowledge. We need fresh inputs daily."

### 3.2 Video Discovery Prompt

**Location:** `ENTITIES/PROMPTS/Research_Prompts/YouTube_Video_Tutorial_Search.md`

**Criteria:**
- Published within last 30 days
- Related to employee's department tools
- Step-by-step tutorial format
- Focus on automation/AI integration

**AI Agents to Use:**
- Perplexity (with YouTube search)
- Gemini Deep Research
- GPT-5 (video metadata analysis)

### 3.3 Video Processing Workflow

```
1. DISCOVERY
   - AI finds relevant videos
   - Filters by criteria (date, topic, quality)
   - Generates list of candidates

2. SELECTION
   - Employee reviews list
   - Selects 1-2 videos
   - Loads into AI Studio

3. TRANSCRIPTION
   - Upload to Google AI Studio
   - Auto-transcribe
   - Export to markdown

4. EXTRACTION
   - Run MAIN_PROMPT v6
   - Extract: Milestones → Tasks → Steps
   - Identify: Tools, Actions, Skills

5. INTEGRATION
   - Store in TASK_MANAGERS
   - Update LIBRARIES
   - Create training materials

6. DISTRIBUTION
   - Assign to TODO lists
   - Share in Discord
   - Archive in ENTITIES/REPORTS/Videos
```

### 3.4 Channel Integration

**Concept:** Track influencer channels for systematic monitoring

**Prompt Needed:**
> "Find top YouTube channels for [department tools]. Monitor for new uploads. Create weekly digest."

**Implementation:**
- Subscribe to key channels
- Weekly video roundup
- Prioritize based on relevance
- Distribute to appropriate employees

---

## 4. HR Attendance Dashboard Deployment

### 4.1 Project Status

**Repository:** https://github.com/AdminRHS/employees-attendance-dashboard
**Deployment:** Vercel (https://vercel.com/remote-helpers/hr-dashboard)
**Local Files:** `Nov25/AI/Artemchuk Nikolay/Employees attendance/`

**Version:** 1.0 (Ready for deployment)

### 4.2 Dashboard Features

**Data Sources:**
- CRM attendance logs
- Discord voice channel presence
- Manual time tracking records

**Visualizations:**
- Daily attendance heatmap
- Individual employee cards
- Department summaries
- Trend analysis (weekly/monthly)

**Key Metrics:**
- Clock in/out times
- Total hours worked
- Discord presence duration
- Status indicators (present/absent/late)

### 4.3 Yellow Card Integration

**Automated Alerts:**
- Missing daily files (3+ consecutive days)
- No CRM records despite 8+ hours Discord presence
- Incomplete reports
- Tool not installed after deadline

**Visual Indicators:**
- 🟢 Green: All good
- 🟡 Yellow: Warning (needs attention)
- 🔴 Red: Critical (immediate action)

### 4.4 Next Phase (v2.0)

**Planned Features:**
- User assignment tracking (who's logged into which AI account)
- Real-time status ("occupied" indicator)
- Token limit expiry alerts
- Cross-reference with ENTITIES/TALENTS data

---

## 5. AI Tools Account Management

### 5.1 Account Tracking Spreadsheet

**Location:** Google Sheets (AI tab, Niko's yellow-highlighted section)

**Columns:**
- Tool name (Cursor, Claude, Windsurf, etc.)
- Account email
- Limit expiration date
- User assignment
- Current status

### 5.2 Token Rotation Strategy

**Problem:** Frequent token exhaustion across team

**Current Approach:**
- Multiple accounts per tool
- Manual tracking in spreadsheet
- 2-4 hour rotation windows

**Proposed Solution:**
- Real-time occupancy tracking
- "Toilet occupied" concept - visual indicator
- Automated expiry alerts
- User assignment logging

### 5.3 Multi-Tool Stack

**Production Tools (Nov 21):**

| Tool | Accounts | Primary Use |
|------|----------|-------------|
| Cursor | 3-4 | Code development, file org |
| Claude Code | 2-3 | File operations, documentation |
| Windsurf | 2 | Alternative development |
| Gravity AI | Testing | Experimental features |
| VS Code + Extensions | Unlimited | Fallback option |

**Token Management:**
- Morning: Cursor (code)
- Midday: Claude Code (docs)
- Evening: Windsurf (experiments)
- Night: AI Studio (video processing)

### 5.4 Account Limit Tracking

**Example Entry:**
```
Tool: Claude Code
Account: dd@ai.remotehelpers.com
Limit Expires: Nov 21, 2:00 PM
Current User: Vilhelm
Status: 🔴 Occupied
Tokens Used: 85%
```

---

## 6. Task Manager Dashboard Concept

### 6.1 Vision

**Quote from session:**
> "Instead of making a dashboard for ALL tasks, maybe we should make a small dashboard for ONE task. More realistic to build over the weekend."

### 6.2 Single-Task Dashboard Features

**For One Task (e.g., "Video Transcription"):**
- Research queue (video links waiting)
- Assignment status (who's working on it)
- Progress tracker (discovery → transcription → extraction → integration)
- Output location
- Next actions

**Benefits:**
- Focused scope
- Faster development
- Proof of concept
- Replicable for other tasks

### 6.3 Proposed Structure

```
TASK DASHBOARD: Video Research & Transcription

┌─────────────────────────────────────┐
│ RESEARCH QUEUE                      │
│ ○ 3 videos pending                  │
│ ○ 2 videos in progress             │
│ ● 5 videos completed               │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ CURRENT ASSIGNMENTS                 │
│ Vilhelm: Figma AI Tutorial (80%)   │
│ Olya: HR Automation Video (45%)    │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ COMPLETED THIS WEEK                 │
│ • 12 videos transcribed            │
│ • 8 task templates created         │
│ • 45 new actions catalogued        │
└─────────────────────────────────────┘
```

---

## 7. Work Environment Upgrades

### 7.1 Vilhelm Onboarding

**Training Session (Nov 21):**
- VS Code + Claude Code Extension setup
- Cursor configuration
- ENTITIES folder structure navigation
- Prompt management system
- Plan Mode usage

**Key Learnings:**
- Copy path for AI context (`Copy Path → Paste in chat`)
- Plan Mode for complex tasks (`Shift+Tab`)
- Manual approval workflow ("Yes and manually approve")
- Extension management

### 7.2 Tool Configuration Standards

**Required Setup (All Employees):**

**VS Code:**
- Claude Code extension
- UTF-8 encoding
- LF line endings
- File watcher enabled

**Cursor:**
- Plan Mode enabled
- Composer for planning
- Chat for quick queries
- .cursorrules configured

**Account Access:**
- Logged into assigned AI accounts
- Name recorded in tracking sheet
- Token limits understood
- Rotation schedule known

### 7.3 Prompt Management

**Personal Prompts Location:**
- Each employee: Own folder for prompts
- Central repository: `ENTITIES/PROMPTS/`
- Integration task: Merge personal → central

**Integration Prompt:**
> "Build me a prompt to integrate my own prompts into the ENTITIES prompts ecosystem"

---

## 8. Content Creation Strategy

### 8.1 Designers: Figma AI Tutorial Videos

**Assignment (for Vilhelm & design team):**
- Find Figma AI tutorials (last 30 days)
- Transcribe and extract techniques
- Build video catalog app
- Features:
  - YouTube links embedded
  - Timestamps clickable
  - Restart video from specific time

**Use Case:**
- Training new designers
- Reference library
- Skill development tracking

### 8.2 Video Catalog App Requirements

**Technical Specs:**
- Next.js + Tailwind CSS
- YouTube iframe integration
- Timestamp parsing
- Click-to-play from timestamp
- Search/filter by topic

**Data Structure:**
```json
{
  "video_id": "V001",
  "title": "Figma AI Features 2025",
  "youtube_url": "https://youtube.com/...",
  "duration": "15:30",
  "timestamps": [
    {"time": "02:15", "topic": "AI text generation"},
    {"time": "08:40", "topic": "Auto-layout with AI"}
  ],
  "tools_mentioned": ["Figma AI", "Plugin X"],
  "extracted_tasks": ["TSK-045", "TSK-046"]
}
```

### 8.3 Work Portfolio Requirements

**New Policy (Nov 21):**
> "Designers must save ALL their work to Dropbox. We need to see what they're creating NOW, not old portfolios from before they joined."

**Implementation:**
- Daily screenshot requirement
- Save to: `Employee_Name/Work_Examples/[Date]/`
- Minimum 3-5 pieces per day
- Include: In-progress + completed work

---

## 9. Email Marketing Automation (Planning)

### 9.1 Concept

**Goal:** Automate follow-up sequences based on client interactions

**Example Flow:**
```
Client doesn't respond
  ↓ (After 3 days)
Auto-send follow-up email
  ↓ (Personalized by AI)
Client responds OR
  ↓ (After 7 days)
Second follow-up
```

### 9.2 Email Template Needs

**Templates to Develop:**
- Meeting reminders
- Daily task assignments
- Follow-up sequences (sales)
- Onboarding sequences (HR)
- Project update notifications

**Assignment:**
> "Give email template development to Vilhelm and design team for practice. Have them design the emails."

### 9.3 Integration Points

**Systems to Connect:**
- ZOHO (collect client emails)
- N8N (automation workflows)
- CRM (lead status tracking)
- Gmail (sending infrastructure)

---

## 10. Strategic Principles Reinforced

### 10.1 Manual First, Then Automate

**Quote:**
> "Manual is perfect for the first stage! You MUST have a plan for how to evolve. Nothing will appear if you don't do it manually first!"

**Progression:**
1. Manual execution (understand the process)
2. Document the workflow
3. Identify automation opportunities
4. Build semi-automated version
5. Full automation with oversight

### 10.2 Version-Based Development

**Philosophy:**
> "Because we'll move through versions, the approval process is less critical. We can fix and improve at any version. Now it's more important to SHIP than to perfect."

**Approach:**
- v1.0: Core functionality (ship fast)
- v2.0: User feedback integration
- v3.0: Advanced features
- v4.0: Optimization

### 10.3 Accumulation Over Replacement

**Quote:**
> "Our final experience is the accumulation of all that we've learned. We don't do things 'just because.' It should build one on another. You don't rebuild the first floor every time—you build the second floor on the foundation."

**Application:**
- Reuse existing search queries (LinkedIn → Google Maps)
- Build on existing transcriptions
- Expand current dashboards
- Integrate, don't replace

### 10.4 Daily Research Requirement

**Mandate:**
> "Everyone must parse at least one video per day. Otherwise the system runs empty—it's churning the same knowledge over and over."

**Implementation:**
- 1 video/day minimum
- Distributed across team
- Tracked in TODO lists
- Integrated into LIBRARIES

---

## 11. Technical Infrastructure Updates

### 11.1 GitHub + Vercel Workflow

**Standard Deployment:**
```
Local Development (Cursor/VS Code)
  ↓ (Git commit)
GitHub Repository
  ↓ (Auto-deploy)
Vercel Hosting
  ↓
Production URL
```

**Projects Deployed:**
- HR Attendance Dashboard
- (Future) Task Manager Dashboard
- (Future) Video Catalog App

### 11.2 Homebrew Installation Challenge

**Issue Encountered:** Installing GitHub CLI via Homebrew requires admin permissions

**Solutions Discussed:**
1. Direct browser download (GitHub CLI installer)
2. Test Gravity AI for installation tasks
3. Document common installation blockers

### 11.3 Extension Management

**VS Code Extensions Required:**
- Claude Code
- GitHub integration
- Markdown preview
- File watcher

**Testing Protocol:**
- Install → Test basic functions → Document issues → Share learnings

---

## 12. Action Items Assigned

### Immediate (Nov 21-22)

**Stas:**
- [ ] Optimize Google Maps search queries
- [ ] Configure review scraping filters
- [ ] Test CRM matching automation
- [ ] Document query formulas

**Kolya:**
- [ ] Deploy HR Dashboard to Vercel
- [ ] Create asset documentation for dashboard
- [ ] Begin Task Manager single-task dashboard
- [ ] Document GitHub → Vercel workflow

**Vilhelm:**
- [ ] Complete YouTube video research (Figma AI)
- [ ] Transcribe 2 videos via AI Studio
- [ ] Integrate personal prompts into ENTITIES
- [ ] Set up work portfolio folder structure

**Olya (HR):**
- [ ] Collect designer work examples
- [ ] Organize portfolio review session
- [ ] Update employee tracking sheet
- [ ] Implement daily screenshot policy

### Short-Term (Week 4)

- [ ] Launch video catalog app (MVP)
- [ ] Email marketing templates (first drafts)
- [ ] Task Manager dashboard v1.0
- [ ] Account management system (real-time tracking)

### Medium-Term (Month 2)

- [ ] Full email automation (N8N)
- [ ] Multi-task dashboard integration
- [ ] Advanced review analytics
- [ ] AI account optimization system

---

## 13. Quotes & Philosophy

**On Building Systems:**
> "It's much less effort to retain an employee than to replace them. The same applies to knowledge—it's less effort to capture it once than to explain it repeatedly."

**On Research:**
> "We worked with Google search queries for years. Give those queries to AI and say: reformat for Google Maps. You'll get your first 20 queries immediately."

**On Speed:**
> "Let's implement v1 on Monday. Then at end of day Monday, log all documentation on what we did, and create plans for the next phase considering today's discussion."

**On Work Evidence:**
> "When I go into an employee's folder, I should see the work they did today. Three, four, five pieces minimum per day."

**On Systematic Growth:**
> "The system can't evolve if we just recycle the same knowledge. Fresh inputs daily—at least one video per person."

---

## Cross-References

**Related Export Files:**
- [04_Automation_Integration.md](04_Automation_Integration.md) - Automation frameworks
- [06_Video_Processing_Knowledge_Capture.md](06_Video_Processing_Knowledge_Capture.md) - Video workflows
- [12_October_Microservices_Technical.md](12_October_Microservices_Technical.md) - Dashboard architecture

**Source Files:**
- [211225.md](../Nov25/Notes/W3/211225/211225.md) - Raw transcription
- [Architecture.md](../Nov25/Notes/W3/Architecture.md) - System design

**GitHub Repositories:**
- https://github.com/AdminRHS/employees-attendance-dashboard

---

## Metadata

**Meeting Date:** 2025-11-21
**Duration:** ~2 hours (estimated)
**Transcription:** Whisper Flow (raw)
**Processing:** MAIN_PROMPT v5.0
**Confidence:** High (85%+)
**Line Count:** ~500
**Language:** Mixed Russian/English

---

**Generated by MAIN_PROMPT v5.0 Export Process**
**Remote Helpers - AI-First Organization**
**November 2025 - Week 3 Day 4**
