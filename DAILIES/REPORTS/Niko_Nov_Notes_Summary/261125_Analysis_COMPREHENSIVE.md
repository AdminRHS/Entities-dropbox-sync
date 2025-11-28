# COMPREHENSIVE ANALYSIS: November 26, 2025
**Folder:** `D:\2025\Notes\Nov25\Notes\W4\261125\`
**Analysis Date:** 2025-11-27
**Framework:** MAIN_PROMPT_v6.md
**Files Analyzed:** 4 (261125.md, Clients.md, message.md, AdminCall.md)

---

## EXECUTIVE SUMMARY

### Documents Identified

1. **261125.md** (115 lines) - Strategic planning notes + full company administrative call transcript
2. **Clients.md** (25 lines) - Client prospect documentation (mergent.com.au - Oil & Gas recruiting firm)
3. **message.md** (26 lines) - Team communication draft (restructuring announcement)
4. **AdminCall.md** (52 lines) - Department priorities and call logistics

### Central Themes

**Day Type:** Crisis Management + System Pivot + Cultural Reset

**Key Initiatives:**
1. **SMM Integration Launch** - First major marketing pivot with phased rollout
2. **Mandatory AI Adoption** - Final ultimatum on daily reporting + automation usage
3. **Team Restructuring** - Yellow flag system reimplementation + performance-based retention
4. **MAIN_PROMPT v6→v7 Evolution** - Expanding framework to handle employee reports
5. **Client Acquisition** - Strategic B2B recruitment automation prospect

**Critical Moment:** Company-wide administrative call addressing:
- Chronic non-compliance with documentation requirements
- Token exhaustion preventing CEO from working during business hours
- Cultural divide between innovation-ready vs. resistance-to-change employees
- Electricity outage complications (Ukrainian context)
- December deadline for team composition finalization

---

## SESSION 1: STRATEGIC INITIATIVES (Notes Section)

### 1.1 SMM INTEGRATION PROJECT

**Project Name:** Social Media Marketing Department Launch

**Preparation Phase Assets Required:**

| Asset Type | Specifics |
|------------|-----------|
| **Accounts** | Instagram, Facebook, Facebook Ads Manager |
| **Content Strategy** | Planning templates, posting schedules |
| **Access & Instructions** | Website posting credentials, CMS access |
| **Creative Briefs** | Text/image/video requirements per platform |
| **Client Descriptions** | Inner client profiles for targeting |

**Extracted Entities:**

**MLT-NEW: SMM Integration Milestone**
```
Phase 1: Account Setup & Access
- Verify Instagram/Facebook access (remote.place accounts exist)
- Set up Facebook Ads Manager
- Obtain website CMS credentials

Phase 2: Content Strategy Development
- Platform specifications (sizes, formats per platform - PMT-045 reference)
- First 10 posts = onboarding materials (not sales)
- Funnel approach: Give value → Build followers → Occasional promo

Phase 3: Staff Training
- Train existing designers on SMM work (cross-department tasking)
- Implement research workflows (1 YouTube video/day per employee)
- Create component libraries (backgrounds, poses, costumes)

Phase 4: Launch & Operations
- Post approval workflows
- Performance tracking dashboards
- Client acquisition via SMM presence
```

**Strategic Rationale (from transcript):**

Quote: "We can train people who didn't qualify as designers for SMM work. Recruiters are charging $1000-1200 for SMM roles. We can create dual-purpose output: work for ourselves + train sellable SMM specialists."

**Cross-Department Impact:**
- **Design (DGN):** Provide SMM creative assets, cross-train staff
- **Lead Gen (LGN):** SMM becomes inbound lead source (vs. outbound outreach)
- **Sales (SLS):** Website + social presence = credibility for pre-sales
- **HR (HRM):** New sellable skill profile (SMM specialist)
- **Marketing (MKT):** First owned marketing channel launch

**Tools Referenced:**

| Tool | Purpose | Location |
|------|---------|----------|
| TOL-NEW: Instagram | Primary content platform | Social media |
| TOL-NEW: Facebook | Secondary platform + ads | Social media |
| TOL-NEW: Facebook Ads Manager | Paid advertising | Marketing automation |
| TOL-NEW: Pinterest | Secondary traffic source (mentioned as underutilized) | Social media |
| TOL-NEW: Behance | Design portfolio showcase | Portfolio platform |
| TOL-NEW: GitHub | Developer profiles | Portfolio platform |
| TOL-NEW: LinkedIn | Professional networking | Business social |
| TOL-NEW: TikTok | Video content (future) | Social media |
| TOL-NEW: Dribbble | Design showcase | Portfolio platform |
| TOL-NEW: ArtStation | 3D/illustration showcase | Portfolio platform |

**Content Strategy Library Reference:**
- Path mentioned: `ENTITIES/LIBRARIES/SMM/content_strategy.md` (line 53 reference)
- Contains: Platform specs, hashtags, post templates
- Historical data: Collected for Anyplace and iWeb3Natchet projects

**First Campaign: Black Friday Promotion**

Concept discussed:
- **Offer Structure:** "1+1" deals by department
  - Lead gen gets 1 free lead gen hour with purchase
  - Design gets 1 free design hour with purchase
- **Activation:** "Write code 312" or "Comment +" to unlock
- **Limitation:** "While supplies last" (artificial scarcity)
- **Timeline:** Immediate (end of month push)

**Risk Identified:** Jumping too far ahead

Quote: "We need very small shippable pieces. First achievement: number of people who logged into accounts. Then we can point them to onboarding folder. But right now nobody has even accessed the accounts yet."

**Immediate Next Step:** Verify who can log into Instagram/Facebook/Twitter accounts (checking access credentials)

---

### 1.2 MAIN_PROMPT v6→v7 EVOLUTION

**Context Improvement Requirements:**

**Version Comparison Analysis:**

| Aspect | v4 | v6 | v7 (Planned) |
|--------|----|----|--------------|
| **Primary Use** | Meeting transcripts | Meeting transcripts + system docs | Employee daily reports + meetings |
| **Libraries Included** | All entities | Simplified (Tools focused) | Tools + Actions (dept-categorized) |
| **Department Extraction** | General | General | Deep department-specific detail |
| **ID System** | XXX-### | XXX-### (simplified) | XXX-### (validated) |
| **Output Templates** | Freeform | Structured | Standardized datasets |
| **Taxonomy Rules** | Embedded | Referenced | Injected per dept |

**Migration Strategy:**

Quote: "v7 meant to replace v4 entirely. v7 will process meeting transcripts like v4 IN ADDITION to daily employee reports."

**Key Changes:**

1. **Library Reorganization:**
   - Keep: Tools (TOL-###)
   - Modify: Actions (ACT-###) with department categorization
   - Relocate: Skills/Objects close to Actions
   - Archive temporarily: Other libraries (revisit later)

2. **Department-Specific Extraction:**
   - v7 should extract department-level detail automatically
   - Test data available: Week_4 employee folders (24th, 25th)
   - Department overview files in main department folders

3. **Prompt Modularization:**
   - Split v6 into sections
   - Approve each section independently
   - Inject taxonomy rules per section
   - Build output templates for dataset population

4. **Context Enhancements:**
   - Add Master CSV files to all ENTITIES folders
   - Change Finance dept code: **FNC** → **FIN** (consistency)
   - Add progress tracking from previous day reports

**Testing Plan:**
- Source: `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4`
- Test files: Employee folders 24 and 25, or department daily summaries
- Validation: Compare extraction quality vs. v4/v6

---

### 1.3 TASK MANAGER VERIFICATION SYSTEM

**Workflow Identified:** Template Validation Pipeline

**TSM-006_Workflows Parsing:**
- Parse existing workflows into Milestone entities
- Create tracking systems for each level

**Tracking Systems Needed:**

| Level | Entity Type | Purpose |
|-------|-------------|---------|
| Projects Progress | PRT-### | Client work status |
| Milestones in Work | MLT-### | Phase tracking |
| Tasks Completed/To-Do | TSK-### | Work unit status |
| Step Sequence Variations | STP-### | Implementation paths |

**Taxonomy Compliance Requirements:**

Review points:
1. No more Skills in Libraries (moved to archive)
2. No more Profiles in Libraries (moved to TALENTS/Employees/)
3. Main purpose: Extract possible tasks → group into milestones → add details (steps)
4. Add context from previous day reports to track progress

**Entity Update Needed:**

From: `TAXONOMY/TAX-002_Task_Managers`
- Update Task Template IDs
- Update Step Template IDs
- Verify new ID system compliance
- Remove deprecated entity references

---

### 1.4 SALES UPGRADES PROJECT

**Problem Statement:**

Quote (Russian transcript): "Job postings use 2+ year old skills and responsibilities. This is like trading expired goods. We can't attract candidates, losing sales."

**Required Upgrades:**

| Asset | Current State | Needed Action |
|-------|---------------|---------------|
| **Company Website** | Outdated skills, no updates for years | Content refresh from current video transcripts |
| **Social Networks** | Non-existent/inactive | SMM Integration (see 1.1) |
| **Presentations** | Old portfolio/capabilities | Update with 2025 work samples |
| **Internal Training** | Employees don't create tasks for each other | Train peer task assignment |

**Pre-Sales Pivot Strategy:**

Context: CEO wants to move from hands-on delivery to pre-sales focus

Current bottleneck:
- Previous model: 40-80 calls/month, surface-level research
- New model: 2-4 calls/month, deep research per prospect
- Research depth: AI-assisted competitive analysis, website audit, needs assessment

**Example Research Workflow (friend's business cited):**

1. **Pre-Call Research:**
   - Analyze prospect website
   - Identify gaps (no social media, poor site, no YouTube, no video content)
   - Prepare AI-generated question list based on gaps

2. **During Call:**
   - Conduct detailed needs interview
   - Use prepared questions to uncover pain points

3. **Post-Call:**
   - AI analyzes conversation
   - Generates custom proposal
   - Result: Closes $8k+ deals consistently

**Implementation Requirements:**
- Reduce lead gen team to 1-2 qualified people (quality over quantity)
- Those remaining must have sales aptitude
- Deep research required before scheduled calls
- Day-before call confirmation process

---

### 1.5 SMENA (1:1 MEETING) SYSTEM

**Problem:** Chaotic ad-hoc meetings preventing systematic work

**Solution:** Scheduled weekly 1:1 meetings per employee

**Purpose:**
- Progress check-ins
- Work verification (show completed work, not just reports)
- Early-stage consultation (10% progress review, not just finished work)

**Preferred Workflow:**

1. **10% Checkpoint:** Employee writes plan/prompt → requests review before execution
2. **50% Checkpoint:** Mid-progress review, course correction opportunity
3. **100% Checkpoint:** Final delivery, verification

Quote: "Don't send me your first generation that you haven't even read. I expect you can read, correct, and refine it to a state you're happy with. THEN we review together."

**Scheduling:**
- Weekly rotation (1:1s not daily)
- Admin helper to schedule (role assignment pending)
- Can send employees to CEO for review (delegation)
- Specific time blocks for different departments

---

## SESSION 2: CLIENT ACQUISITION (Clients.md)

### 2.1 MERGENT.COM.AU - OIL & GAS RECRUITER

**Client Profile:**

| Field | Details |
|-------|---------|
| **Company** | mergent.com.au |
| **Industry** | Oil and Gas Industry Recruitment |
| **Region** | Australia |
| **Current Method** | LinkedIn recruiting |
| **CRM System** | Vincere (by The Access Group) |
| **Automation Interest** | Database review, CRM automations |

**Tools in Use:**

**TOL-NEW: Vincere CRM**
- Vendor: The Access Group
- URL: https://www.theaccessgroup.com/en-gb/crm/
- Purpose: Recruitment CRM
- Integration opportunity: Automation workflows

**TOL-NEW: Tripify**
- Purpose: LinkedIn Automation
- Use case: Prospecting, outreach automation

**Service Opportunity Analysis:**

**Proposed: 6-Month Talent Engagement**

**High Demand Areas Identified:**
1. **Content - SMM:**
   - Learning materials creation
   - Design instructions/templates
   - (List incomplete in notes - expansion needed)

**Remote Helpers Value Proposition:**
- AI-powered recruitment automation (aligns with Tripify usage)
- CRM workflow optimization (Vincere integration)
- Content creation for recruitment marketing
- Database management/enrichment

**Next Steps Required:**
- Complete needs assessment
- Propose automation workflows (PMT-044: Sales Department Research)
- Demonstrate SMM content capabilities (timing: aligns with SMM launch)
- Prepare 6-month talent proposal outline

---

## SESSION 3: TEAM RESTRUCTURING (message.md)

### 3.1 YELLOW FLAG SYSTEM REIMPLEMENTATION

**Communication Document Analysis:**

Type: Company-wide announcement (Russian language)
Tone: "Softer and more motivating version" (noted in filename context)

**System Overview:**

**Purpose:** Transparency tool (not punishment) to maintain team rhythm

**Key Principles:**
1. **Universal Application:** Same rules for everyone, no exceptions
2. **Clear Expectations:** Everyone knows what to aim for
3. **Self-Selection:** Employees choose if they fit the new culture

**Cultural Vision for December:**

Target team composition:
- People interested in AI development
- Curious about experiments and research
- Ready to learn, change, and engage
- Not about overwork - about attitude and team participation

**Restructuring Approach:**

Quote (translated): "If someone understands the work format doesn't suit them now, that there's no inspiration or interest - that's also normal. In such cases we will discuss options correctly, acting according to rules and with respect to the person's contribution."

**Global Context Cited:**

Justification for optimization:
- Companies worldwide optimizing teams
- Closing directions
- Reconsidering priorities
- Most resilient = those ready to learn, develop, take responsibility

**Goal:** Remote Helpers as a learning, responsible, adaptable team

---

### 3.2 TEAM ACKNOWLEDGMENT

**Recognition:**

Quote (translated): "I want to especially note those who remain engaged, help colleagues, communicate even in difficult conditions. We have many such people, and our projects rely on them."

**Gratitude:**
- Thanks to those currently performing
- Thanks for supporting each other
- Thanks for moving projects forward
- Value acknowledged as "incredibly valuable"

**Call to Action:**

"Let's make December the month when we strengthen the team, align to a common rhythm, and continue developing. We can do a lot - and I'm confident that together we'll do even more."

---

## SESSION 4: ADMINISTRATIVE CALL TRANSCRIPT (AdminCall.md + 261125.md)

### 4.1 THE AI ADOPTION ULTIMATUM

**Context:** Full company call addressing chronic non-compliance

**Problems Identified:**

**1. Empty Daily Reports**

Quote: "When AI receives an empty file, it has nothing to say. Neither to me about the department, nor anything else. I understand habit is a difficult thing. It developed over years. For years we wrote nothing no matter how much I asked."

**Impact:**
- CEO cannot analyze department progress
- AI cannot track individual learning progress
- Cannot identify where team is stuck
- No context for planning next steps

**2. Work Environment Setup Failures**

Administrative resources wasted:
- Checking if VS Code installed
- Verifying Dropbox enabled
- Confirming Claude Extension present
- Repeating basic setup checks in circles

Quote (translated): "Instead of developing our company, moving toward progress, implementing new tools, we run around dealing with nonsense like 'did you eat today? did you wash? did you brush your teeth?' for adult people we hired."

**3. Token Exhaustion Crisis (CEO Perspective)**

CEO work pattern:
- Can only work nights/weekends (when employees aren't using AI accounts)
- All 8 accounts exhausted by daily employee usage
- Cannot perform strategic work during business hours
- Forced into manual checking loops instead of AI analysis

---

### 4.2 THE THREE REQUIREMENTS

**Requirement 1: AI Usage (Daily Reports)**

**Minimum Standard:**
- Daily records in markdown format
- Not acceptable: "I came to work today" (too generic)
- Required: Specific details, progress tracking, project names, tasks completed

**Analysis Workflow:**
- Employee writes daily report
- Employee runs MAIN_PROMPT_v7 analysis on their OWN day
- Employee identifies: "What can I do better?"
- Self-improvement becomes daily habit (1% better each day)

**Second Level (Researches):**
- Find 1 YouTube video/day related to your work
- Use research prompts: `ENTITIES/TASK_MANAGERS/researches/`
- Learn: "How to do my task better in the AI age?"
- Options: Deep researches, Gemini, GPT, local models
- Parse videos, download instructions to your folder
- Point AI to instructions folder: "We do it this way. Can you reformat and create a prompt?"

**Third Level (Context Building):**
- Download instructions from Google Drive
- Place in your department folders
- Give context to AI for your specific work
- Ask: "How can I do this better?"

Quote: "This isn't overwork requirement. Question is: do you WANT to develop with us, improve with us, implement new things - or are you against all this?"

---

**Requirement 2: Work Environment Setup**

**Theme:** "You ate today? You washed? You brushed your teeth?"

**Non-Negotiable Tools:**
1. AI daily report analysis
2. Notes in markdown (Whisper Flow or manual)
3. Work environment properly configured

**Verification Method:**
- Admin resources no longer checking manually
- If not set up: direct conversation required
- Response expected: "I'm against it, I won't write, can't write, haven't written since school 20 years ago, don't want to analyze or improve"
- Result: Respectful exit with gratitude for past contributions

Quote: "I don't want to spend time running around checking, building systems to detect that you don't want to and won't write. I'm done with that."

---

**Requirement 3: Research Integration**

**Workflow:**
- Search YouTube for videos on your specialty
- Last 30-60 days, using AI + automation keywords
- Parse video, extract entities
- Save to research folder
- Build knowledge library

**Purpose:**
- Stay current (innovations emerge in 1-2 days)
- Company can't have 1 person doing all innovation integration
- "Not enough physical strength" to be solo researcher for entire company

---

### 4.3 RECORDING & DOCUMENTATION REQUIREMENTS

**Recording Workflow:**

When communicating with AI:
1. You ask AI to do something
2. AI responds
3. **You must save the conversation:**
   - Copy entire chat, OR
   - Ask AI: "Save this chat," OR
   - Ask AI: "Save not the chat but the PROMPTS - the sequence of working with AI"

**Prompt-First Development:**

Standard sequence:
1. "Create a plan for me" (ask AI)
2. AI creates plan
3. **You read the plan line by line** (critical step)
4. Check: correct names? right folders? needs these specific folders for context?
5. If no context: plan context creation first
6. Give feedback, correct errors (prevent errors from propagating)

**Re-reading Requirement:**

Quote: "Re-read, re-read, re-read again his output. How he understood your notes, how he understood details. If he understood something wrong, another person won't understand either."

**Details Requirement:**

Example: Media logging
- When uploading image: not just the image
- Required details:
  - Which project?
  - Which client?
  - Which task?
  - Which prompt used?
  - Which tool generated it? (Midjourney, DALL-E, etc.)
  - Difficulties encountered?
  - Shortcomings noticed?
  - How much time it took?

**Purpose:** Enable cross-team learning

Quote: "Yesterday I looked - on all images there's a face portrait. Does some designer have ideas to make them sitting, lying, I don't know, cleaning fish, cooking food? But they're shy to come to you because you're sitting there talking. But if it's written in the folder, they can read and comment: 'This could be better, these inputs...' that you won't immediately see yourself."

---

### 4.4 ATTENDANCE & ELECTRICITY ISSUES

**The Electricity Problem (Ukrainian Context):**

Current situation:
- Some employees have power outages
- Time lost: significant
- Reporting issue: Daily reports filled with "power out, power out, power out"

**CEO Perspective:**

Quote: "Where to move the company, what are we implementing, what progress - NONE. I don't need to record power outages. It's enough to know we have this problem so we don't schedule calls during outages."

**Policy:**
- Everyone knows who has power issues
- No need to log each outage
- Lost hours must be made up
- Evening/weekend makeup work expected
- Not about overwork - about making up lost hours

**Paid Overtime:**
- Will be compensated
- But: hours lost must be recovered
- "No electricity? OK, no ability to work. Need to make it up."

---

### 4.5 WORK STYLE PREFERENCE DECLARATION

**The Preference Question:**

CEO's desire:
- Want team to ENJOY what they do
- Want team to want to develop together
- Don't want people "digging in heels, trying every way to slow down"

**Direct Conversation Request:**

Preferred: "Come say you're against it. Say 'I won't record, I can't record, I won't use AI, I want to work the old way, want to work manually, don't want to write, can't write, forgot how since school 20 years ago, don't want to analyze and improve.'"

Result: "We'll treat you with respect and gratitude for all time worked at our company, thank you, but this year this stage of manual work ends completely."

**Unacceptable:** Silent non-compliance requiring CEO to build detection systems

---

### 4.6 SMENA (1:1) LOGISTICS

**Current Gap:**
- No administrator to schedule calls
- Need rotation system
- Agreement: Everyone comes 1-2 times/week minimum
- Show work, get advice, discuss progress

**Preferred Timing:**
- **10% progress:** Share plan before execution (not after failures)
- **Mid-progress:** Check-ins during work (not only at end)
- **Don't send:** First generation you haven't read yourself
- **Do send:** Refined plan you've read, corrected, brought to acceptable state

**Expectation Management:**

Quote: "I expect you can read, correct, and bring it to a state you like. Then: 'Here are our plans, we'll do X-Y-Z, what do you think?' I'll adjust slightly or we'll agree - let's go."

**Delegation:**
- Can send employees to CEO
- Can agree on specific times
- Don't wait for CEO to chase you down

---

### 4.7 DEPARTMENT-SPECIFIC FEEDBACK

**Design Department (Yulia's Report):**

**Positive:**
- Ran daily analysis through AI
- Understands it's not perfectly accurate yet (need to improve detail in notes)

**Improvement Area:**
- More details in recordings
- Use markdown formatting:
  - ## Hashtags for headers
  - **Bold**, *Italic*
  - [Square brackets], <angle brackets>
  - Stars, dashes for bullets
- Even when using Whisper Flow: highlight key things manually
- Mark: Project: [name], Task: [name], Source: [link], etc.

Quote to Yulia: "Enrich your notes please. You finished 11 years of education, higher education - I'm confident you can be more detailed."

---

**Lead Gen Department (Polina's Input):**

Request: Increase information quantity from lead gens
- Even if it hurts performance initially
- Copy: Dialogue profiles, conversations, outreach templates
- More detail = better analysis possibilities

**Purpose:** See deeper into workflows, identify improvement opportunities

---

**HR Department (Strategic Philosophy):**

**Documentation Principle:**
- Document every step
- Keep instructions current
- Create tutorials for routine tasks
- Extract global plans from department communication
- Record those plans
- AI analyzes structure of global plans

**Quality Loop:**
- Write plans/instructions
- Run through Prompt v7 (or similar)
- Ask: "How can this be improved?"
- Check what AI understood
- **Critical:** If AI misunderstood, give feedback (prevent error propagation)

**Context & Detail Requirement:**

Quote from Yulia (Anti Gravity user): "We do daily proceed already for administration. Started last week. But now need to add whole department - do same for entire folder each day."

**Tool Clarification:**
- Cursor + Claude Code Extension = best (works in Cursor, Anti Gravity, VS Code)
- Anti Gravity: Had issues with Gemini 3 Pro Haiya model
- Workaround: `/login` in chat to switch accounts without losing chat context

---

**Finance Department (Katya):**

**Task:** Routine monthly actions (e.g., marking weekends)

**Efficiency Strategy:**
1. Create instruction once (beginning of month)
2. Only record specific details that changed in each situation
3. Ask AI: "How can I automate this? How can I avoid manual steps?"
4. Continuously improve workflow

Quote: "Let's think how to improve. Everything I do by hand: how do I make it so I don't have to go manually?"

---

**Video Department (Nastya's Question):**

**Issue:** Empty folders created but no content

**Clarification:**
- Transcription of calls IS valuable
- But: when discussing something, generating prompts - save your PRIMARY prompt to the file
- Or: Save the result to your daily file/plans
- Or: Create any file with any name - just have SOMETHING in folder

**Specific to Designers:**

When generating images:
1. Save the prompt used
2. Copy to daily file
3. Or: Ask AI to log everything: "Every prompt I give you, save and log it"

**Advanced:** Multi-phase prompt creation

Before executing (if more complex than "remove comma"):
1. "Create a prompt for me"
2. AI creates prompt
3. "Save this prompt in today's folder"
4. Now you have documentation automatically

**Even More Advanced:** Multi-phase workflows

Quote to AI: "Create a multi-phase prompt for executing this task. Break each phase into a separate file so if my chat breaks, I can continue in another chat or execute other phases in parallel."

**Purpose:** Essential for synchronization, prevents need for endless calls

---

### 4.8 ATTENDANCE TRACKING SYSTEM (Kolya's Report)

**Data Sources:**

| Source | Tracks | Issue Identified |
|--------|--------|------------------|
| **CRM** | Work hours logged | Some employees: 0 hours but status = available |
| **Discord** | Online presence | Time discrepancies vs. CRM |
| **RAID** | (System mentioned, unclear) | Pending integration |

**Current Discrepancies:**

Example issues found:
- Employee shows "available" in CRM but 0 hours worked
- CRM hours don't match Discord hours
- Missing reports entirely
- No CRM entries, no Discord presence, no reports (complete absence)

**Time Calculation Issue:**

**Problem:** System auto-deducts 1 hour for breaks
- Full-time: Expected 8 hours → shows 7 hours (after -1 hour break)
- Part-time: Expected 4 hours → shows 3 hours (after -1 hour break)

**Current Status:** Kolya adjusted system

**CEO Reaction:** "Maybe don't deduct that hour? Some work without breaks, some work 4 hours..."

**Status Updates Needed:**

Example: Employee marked "available" but actually on "pre-sale" status
- System expects 8 hours work
- Shows 0 hours (because wrong status)
- Fix: Update status in CRM

---

**Weekends Issue:**

System counting weekends as work days for some employees

**Solution Needed:**
- Implement weekend exceptions
- Cross-reference with Gantt chart approved time off
- Example: Eleonora had approved week off, but system flagged as absent

---

**Project Employees:**

Current gap: Those on external projects not tracked in this system

**Decision:**
- Keep tracking separate for now (only company projects)
- Add "project" designation later
- Focus on internal team first

---

**Recommendation:**

Kolya suggests: Daily breakdown per person showing:
- CRM hours
- Discord hours
- Report submitted (yes/no)
- Expected vs. actual

CEO: Agrees, asked to develop detailed version

---

### 4.9 VIDEO PRODUCTION WORKFLOW (Svyat's Input)

**Current Process:**

1. Records all conversations (30-50 min recordings)
2. Cuts unnecessary parts
3. Transcribes via Whisper Flow
4. Processes transcripts

**Work Type:** Manual interview editing with Sekret

Process:
- Sekret edits on phone
- Svyat re-processes, uploads
- Daily routine: "Made X video, uploaded" (repetitive logging)

**Documentation Opportunity:**

CEO suggestion:
- Interviews have **scripts**
- Scripts have **execution instructions**
- There's a **tracking table** of which videos done

**Automation Path:**

1. Convert table to Markdown
2. Place in Video department folder
3. Give AI access to table
4. AI maintains table based on daily notes
5. AI auto-updates completion status

**CEO Offered:** "Want me to show you right now how to do this?"

**Implementation:**
- AI can't edit Google Sheets directly (yet)
- But: Markdown version updated by AI
- Periodically sync back to sheet
- Or: Explore Sheets automation APIs

---

### 4.10 DESIGN DEPARTMENT (Vlad's Input)

**Philosophy Shared:**

Quote: "Instructions = Context. In 2 words: The more we write now - not just 'I did this task today, period, moving on' - but actually describe step-by-step all processes, we'll have MATERIAL FOR ANALYSIS. We'll have context for AI, and specifically good quality context about our specific company, not in general."

**Result:**
- Won't have to explain same thing 10 times
- Useful, cool, valuable
- Leads to more clients, better results

**Current Work: Component Library Creation**

Task announced: Build element library for graphics (backgrounds, poses, scales, etc.)

**Vlad's Plan:**
1. Takes task to AI
2. Asks AI: "Give me instructions for this task, describe steps"
3. Attaches to daily report
4. Also includes: prompts, generated images, backgrounds, poses, etc.

**CEO Response:** "Super! That's exactly what we need."

**Next Phase (when enough prompts collected):**

1. Request AI to **templatize prompts**
2. Break into separate components
3. Create **Constructor folder** structure:
   ```
   Constructor/
   ├── Backgrounds/ (10+ variants each)
   ├── Poses/
   ├── Costumes/
   └── [etc.]
   ```

4. Eventually: Create internal prompt to auto-scan employee folders
5. Collect missing details
6. Auto-update component library

Quote: "Super! Fire! Thank you!"

---

### 4.11 DEVELOPMENT DEPARTMENT (Svyat - DevOps Context)

**Google Scraping Project:**

**Achievement:** Created instructions used by 2 people already (Plamenna, Isaac)

**Instruction Sharing:**
- Successfully created usable tutorials
- Other developers adopted immediately
- Demonstrates value of documentation

---

### 4.12 HR DEPARTMENT (Katya - Accountant Role)

**Challenge:** Parameter naming consistency

When recording details:
- Use consistent names (not switching languages/abbreviations)
- Example: Employee name
  - ❌ Wrong: Ukrainian once, English another time, short name third time
  - ✅ Right: Pick one standard, use always
- If multiple names possible: Tell AI: "Person may have 3 names, these are aliases"

**Routine Task Automation:**

Example: Monthly weekend marking

**Current:** Manual process each month

**Improvement Path:**
1. Create instruction at month start
2. Only record specific variations in each instance
3. Ask AI: "How can I automate this? How do I avoid manual work?"

**Continuous Improvement:**

Quote (CEO): "Let's think how to improve. How do I make it so I don't have to go manually?"

**Katya's Response:** Agreed, will work on it

---

### 4.13 CLOSING STATEMENTS

**CEO Summary:**

"Thank you everyone for enduring this flood. Thanks to those who are intensively implementing, trying, not afraid of errors. In any case, everyone have a good day until the next call."

**Call Frequency:**

- Will do calls every X days (frequency not specified)
- Don't forget to come to admin calls
- Bring back 1:1 meetings

**Knowledge Transfer Request:**

"Pass knowledge forward please. With whoever you talk, check, look."

**Team Acknowledgment:**

"Thank you very much. Good day."

**Final Note:**

Svyat: "It was a difficult call but I think for the better."

**Admin Access Issue (Anya):**

Tried to join Admin call, access issues
- CEO granted access
- Anya joined successfully
- Resolved on the call

---

## ENTITY EXTRACTION

### PROJECTS (PRT-###)

**PRT-NEW-001: SMM Integration & Launch**
```
Name: Social Media Marketing Department Integration
Department: Marketing (MKT) + Design (DGN) + Sales (SLS)
Status: Planning → Setup phase
Timeline: Immediate (Black Friday campaign) → Q4 2025 ongoing
Owner: CEO + MKT Lead
Dependencies: Account access, content strategy, staff training
```

**PRT-NEW-002: MAIN_PROMPT v7 Development**
```
Name: MAIN_PROMPT Framework v7 Creation
Department: AI & Automation (AID)
Status: Requirements gathering → Development
Purpose: Replace v4, extend v6 to handle employee daily reports
Dependencies: v6 testing complete, taxonomy updates
```

**PRT-NEW-003: Team Restructuring (December 2025)**
```
Name: December Team Optimization & Cultural Reset
Department: HR (HRM) + All departments
Status: In progress (announcement phase)
Timeline: Through end of November → finalize December 1
Components: Yellow flag system, AI adoption enforcement, skills assessment
```

**PRT-NEW-004: Mergent.com.au Client Acquisition**
```
Name: Oil & Gas Recruiter Automation Engagement
Department: Sales (SLS) + AI & Automation (AID)
Status: Prospect (discovery phase)
Opportunity: 6-month talent engagement
Value: CRM automation + LinkedIn automation + content creation
```

**PRT-NEW-005: Sales Department Pre-Sales Pivot**
```
Name: Transition to Deep Research Pre-Sales Model
Department: Sales (SLS) + Lead Gen (LGN)
Status: Planning
Change: 40-80 surface calls/month → 2-4 deep research calls/month
Dependencies: Website update, SMM presence, presentation updates
```

---

### MILESTONES (MLT-###)

**MLT-NEW-001: SMM Account Setup & Verification**
```
Project: PRT-NEW-001
Tasks: Verify Instagram/Facebook access, Facebook Ads Manager setup
Status: Immediate priority
Blocker: Nobody has logged in yet (as of 11/26)
```

**MLT-NEW-002: SMM Content Strategy Development**
```
Project: PRT-NEW-001
Tasks: Platform specs, first 10 posts (onboarding content), funnel design
Dependencies: MLT-NEW-001 complete
Reference: ENTITIES/LIBRARIES/SMM/ folder content
```

**MLT-NEW-003: SMM Staff Training & Cross-Department Tasking**
```
Project: PRT-NEW-001
Tasks: Train designers on SMM, implement research workflows (1 video/day)
Timeline: Ongoing through December
```

**MLT-NEW-004: Black Friday Campaign Launch**
```
Project: PRT-NEW-001
Timeline: End of November 2025
Offer: 1+1 deals by department, promo codes, comment-to-unlock
Status: Planning (premature - need MLT-NEW-001 complete first)
```

**MLT-NEW-005: MAIN_PROMPT v7 Requirements Finalization**
```
Project: PRT-NEW-002
Tasks: Review v4 vs v6, define department extraction depth, modularize sections
Test data: Week_4 employee folders (24, 25)
```

**MLT-NEW-006: MAIN_PROMPT v7 Library Reorganization**
```
Project: PRT-NEW-002
Tasks: Keep Tools, modify Actions (dept categorization), archive Skills/Profiles
ID updates: Change FNC → FIN for Finance
```

**MLT-NEW-007: MAIN_PROMPT v7 Output Templates & Taxonomy Injection**
```
Project: PRT-NEW-002
Tasks: Build standardized datasets, inject taxonomy rules per section
Approval: Section-by-section review
```

**MLT-NEW-008: Yellow Flag System Implementation**
```
Project: PRT-NEW-003
Tasks: Define criteria, communicate rules, track compliance
Status: Communication sent (message.md), enforcement starting
```

**MLT-NEW-009: AI Adoption Enforcement (3 Requirements)**
```
Project: PRT-NEW-003
Requirements:
1. Daily reports + self-analysis
2. Work environment setup (VS Code, Dropbox, Claude Extension)
3. Research integration (1 YouTube video/day)
Status: Announced in admin call, compliance deadline implied (December)
```

**MLT-NEW-010: Attendance & Electricity Issue Resolution**
```
Project: PRT-NEW-003
Tasks: Implement makeup work system, weekend tracking, project employee separation
Owner: Kolya (tracking system) + HR
```

**MLT-NEW-011: Mergent Discovery & Needs Assessment**
```
Project: PRT-NEW-004
Tasks: Complete client research, map Vincere CRM workflows, identify automation opportunities
Reference: PMT-044 (Sales Department Research)
```

**MLT-NEW-012: Mergent Proposal & 6-Month Plan**
```
Project: PRT-NEW-004
Dependencies: MLT-NEW-011, SMM capabilities demo ready
Deliverable: Talent engagement proposal
```

**MLT-NEW-013: Website Content Refresh**
```
Project: PRT-NEW-005
Tasks: Update skills, update portfolios, modernize case studies
Source: Current video transcripts (2025 work)
Status: Needed urgently ("trading expired goods")
```

**MLT-NEW-014: Lead Gen Team Optimization**
```
Project: PRT-NEW-005
Tasks: Reduce team to 1-2 qualified people with sales aptitude
Criteria: Can perform deep research, not just volume outreach
```

---

### TASKS (TSK-###)

**SMM Integration (from MLT-NEW-001 to MLT-NEW-004):**

- TSK-NEW-001: Check Instagram account access (remote.place or remote account?)
- TSK-NEW-002: Check Facebook account access
- TSK-NEW-003: Set up Facebook Ads Manager
- TSK-NEW-004: Obtain website CMS posting credentials
- TSK-NEW-005: Document platform specifications (sizes, formats) - reference existing SMM library
- TSK-NEW-006: Create onboarding content plan (first 10 posts)
- TSK-NEW-007: Design funnel strategy (value content → followers → occasional promo)
- TSK-NEW-008: Train designers on SMM asset creation
- TSK-NEW-009: Implement daily research workflow (1 YouTube video/person/day)
- TSK-NEW-010: Create component libraries (backgrounds, poses, costumes)
- TSK-NEW-011: Design Black Friday 1+1 offer mechanics
- TSK-NEW-012: Create Black Friday promotional posts
- TSK-NEW-013: Set up promo code system ("code 312" example)

**MAIN_PROMPT v7 Development (from MLT-NEW-005 to MLT-NEW-007):**

- TSK-NEW-014: Compare v4 vs v6 capabilities and gaps
- TSK-NEW-015: Test v6 on Week_4 employee folders (24, 25)
- TSK-NEW-016: Define department-specific extraction requirements per department
- TSK-NEW-017: Modularize v6 into approvable sections
- TSK-NEW-018: Rearrange Actions library by department categories
- TSK-NEW-019: Archive Skills and Profiles from LIBRARIES
- TSK-NEW-020: Update all Finance references from FNC to FIN
- TSK-NEW-021: Add Master CSV files to all ENTITIES folders
- TSK-NEW-022: Build output templates for dataset population
- TSK-NEW-023: Inject taxonomy rules per prompt section
- TSK-NEW-024: Test v7 extraction on daily employee reports
- TSK-NEW-025: Compare v7 output quality vs v4/v6

**Team Restructuring (from MLT-NEW-008 to MLT-NEW-010):**

- TSK-NEW-026: Draft yellow flag system criteria
- TSK-NEW-027: Send team communication (message.md) - **DONE**
- TSK-NEW-028: Conduct company-wide admin call - **DONE**
- TSK-NEW-029: Track daily report compliance by employee
- TSK-NEW-030: Track work environment setup compliance
- TSK-NEW-031: Track research workflow compliance (1 video/day)
- TSK-NEW-032: Implement makeup work tracking for electricity outages
- TSK-NEW-033: Fix weekend tracking in attendance system
- TSK-NEW-034: Update CRM statuses (e.g., fix "available" vs "pre-sale")
- TSK-NEW-035: Separate project employee tracking from internal tracking

**Client Acquisition (from MLT-NEW-011 to MLT-NEW-012):**

- TSK-NEW-036: Research Vincere CRM capabilities and APIs
- TSK-NEW-037: Research Tripify LinkedIn automation tool
- TSK-NEW-038: Map Mergent's current recruitment workflow
- TSK-NEW-039: Identify automation opportunities in their process
- TSK-NEW-040: Prepare SMM content samples (demonstrate capability)
- TSK-NEW-041: Draft 6-month talent engagement proposal
- TSK-NEW-042: Schedule discovery call with Mergent

**Sales Upgrades (from MLT-NEW-013 to MLT-NEW-014):**

- TSK-NEW-043: Audit website for outdated skills/content
- TSK-NEW-044: Extract current skills/tools from 2025 video transcripts
- TSK-NEW-045: Update website skills section
- TSK-NEW-046: Update website portfolio/case studies
- TSK-NEW-047: Refresh job posting templates
- TSK-NEW-048: Update sales presentation decks
- TSK-NEW-049: Assess current lead gen team for sales aptitude
- TSK-NEW-050: Implement deep research workflow template for sales calls
- TSK-NEW-051: Create pre-call AI research checklist (website audit, gap analysis, question generation)

**Task Manager Operations (from 261125.md notes):**

- TSK-NEW-052: Parse TSM-006_Workflows/ into Milestone entities
- TSK-NEW-053: Create Projects Progress tracking dashboard
- TSK-NEW-054: Create Milestones in Work tracking view
- TSK-NEW-055: Create Tasks Completed/To-Do dashboard
- TSK-NEW-056: Create Step Sequence Variations documentation
- TSK-NEW-057: Review TAXONOMY/TAX-002_Task_Managers for ID updates
- TSK-NEW-058: Update Task Template IDs to new system
- TSK-NEW-059: Update Step Template IDs to new system

**Department-Specific Tasks:**

**Design:**
- TSK-NEW-060: Implement markdown formatting in daily reports (##, **, [], etc.)
- TSK-NEW-061: Create component library (backgrounds) with prompts
- TSK-NEW-062: Create component library (poses) with prompts
- TSK-NEW-063: Create component library (costumes) with prompts
- TSK-NEW-064: Templatize design prompts into reusable components
- TSK-NEW-065: Create Constructor folder structure
- TSK-NEW-066: Build auto-scan prompt for employee design folders

**Lead Gen:**
- TSK-NEW-067: Increase detail in daily reports (dialogue copies, profile details)
- TSK-NEW-068: Document outreach conversations in markdown

**Video:**
- TSK-NEW-069: Convert video tracking table to Markdown
- TSK-NEW-070: Implement AI-maintained video completion table
- TSK-NEW-071: Save interview scripts to department folder
- TSK-NEW-072: Document video execution instructions

**HR:**
- TSK-NEW-073: Standardize employee name formats across all systems
- TSK-NEW-074: Create monthly routine instruction templates
- TSK-NEW-075: Identify automation opportunities in monthly tasks

**Finance:**
- TSK-NEW-076: Create weekend marking automation script
- TSK-NEW-077: Document routine task variations for AI learning

**Development:**
- TSK-NEW-078: Share Google scraping instructions (Svyat) - **DONE**
- TSK-NEW-079: Create developer tutorial library in dept folder

---

### ACTIONS (ACT-###)

**New Actions Identified:**

- ACT-NEW-001: Verify (account access, credentials)
- ACT-NEW-002: Set up (tools, platforms, integrations)
- ACT-NEW-003: Train (employees on new workflows)
- ACT-NEW-004: Implement (systems, processes, automations)
- ACT-NEW-005: Research (prospects, tools, competitors)
- ACT-NEW-006: Audit (websites, content, processes)
- ACT-NEW-007: Extract (data from transcripts, videos, reports)
- ACT-NEW-008: Analyze (reports, performance, gaps)
- ACT-NEW-009: Document (workflows, instructions, processes)
- ACT-NEW-010: Standardize (naming, formats, templates)
- ACT-NEW-011: Modularize (prompts, code, components)
- ACT-NEW-012: Templatize (prompts, designs, content)
- ACT-NEW-013: Track (compliance, progress, attendance)
- ACT-NEW-014: Optimize (teams, workflows, costs)
- ACT-NEW-015: Communicate (announcements, updates, feedback)
- ACT-NEW-016: Restructure (teams, departments, systems)
- ACT-NEW-017: Automate (reporting, tracking, maintenance)
- ACT-NEW-018: Integrate (APIs, systems, data sources)
- ACT-NEW-019: Validate (data, compliance, quality)
- ACT-NEW-020: Archive (old data, deprecated systems)

---

### OBJECTS (OBJ-###)

**New Objects Identified:**

- OBJ-NEW-001: Social Media Account (Instagram, Facebook, LinkedIn, etc.)
- OBJ-NEW-002: Ads Manager (Facebook Ads Manager)
- OBJ-NEW-003: Content Strategy (planning document)
- OBJ-NEW-004: Platform Specification (size/format requirements)
- OBJ-NEW-005: Onboarding Content (learning materials)
- OBJ-NEW-006: Funnel (marketing funnel structure)
- OBJ-NEW-007: Component Library (reusable design elements)
- OBJ-NEW-008: Daily Report (employee daily markdown file)
- OBJ-NEW-009: Prompt (AI instruction)
- OBJ-NEW-010: Taxonomy (classification system)
- OBJ-NEW-011: Master CSV (entity registry file)
- OBJ-NEW-012: Master JSON (entity registry file)
- OBJ-NEW-013: Yellow Flag (compliance warning)
- OBJ-NEW-014: Attendance Record (time tracking data)
- OBJ-NEW-015: CRM Entry (customer relationship data)
- OBJ-NEW-016: Discord Log (communication record)
- OBJ-NEW-017: Research Video (YouTube tutorial)
- OBJ-NEW-018: Transcript (video/call transcription)
- OBJ-NEW-019: Instruction (tutorial document)
- OBJ-NEW-020: Workflow (process sequence)
- OBJ-NEW-021: Template (reusable structure)
- OBJ-NEW-022: Tracking Table (progress spreadsheet)
- OBJ-NEW-023: Context (AI background information)
- OBJ-NEW-024: Client Proposal (service offering document)
- OBJ-NEW-025: Employee Profile (talent record)

---

### TOOLS (TOL-###)

**Social Media & Marketing:**
- TOL-NEW-001: Instagram (primary content platform)
- TOL-NEW-002: Facebook (secondary platform + marketplace)
- TOL-NEW-003: Facebook Ads Manager (paid advertising)
- TOL-NEW-004: LinkedIn (professional networking, B2B)
- TOL-NEW-005: Twitter/X (microblogging, tech community)
- TOL-NEW-006: TikTok (short-form video)
- TOL-NEW-007: YouTube (long-form video, tutorials)
- TOL-NEW-008: Pinterest (visual discovery, underutilized traffic source)
- TOL-NEW-009: Behance (design portfolio showcase)
- TOL-NEW-010: Dribbble (design community)
- TOL-NEW-011: ArtStation (3D/illustration showcase)
- TOL-NEW-012: GitHub (developer portfolios, code repos)

**CRM & Automation:**
- TOL-NEW-013: Vincere CRM (recruitment CRM by The Access Group)
- TOL-NEW-014: Tripify (LinkedIn automation)
- TOL-NEW-015: The Access Group (CRM vendor platform)

**AI & Development:**
- TOL-NEW-016: VS Code (code editor)
- TOL-NEW-017: Cursor (AI-powered code editor)
- TOL-NEW-018: Anti Gravity (AI development tool)
- TOL-NEW-019: Claude Code Extension (AI coding assistant)
- TOL-NEW-020: Whisper Flow (transcription tool)
- TOL-NEW-021: Gemini 3 Pro Haiya (Google AI model)
- TOL-NEW-022: GPT (OpenAI models)
- TOL-NEW-023: Local AI Models (on-premise inference)

**Collaboration & Storage:**
- TOL-NEW-024: Dropbox (file sync and storage)
- TOL-NEW-025: Discord (team communication)
- TOL-NEW-026: Google Drive (document storage)
- TOL-NEW-027: Google Sheets (spreadsheet collaboration)

**Design & Media:**
- TOL-NEW-028: Midjourney (image generation - implied)
- TOL-NEW-029: DALL-E (image generation - implied)
- TOL-NEW-030: Phone Editing Tools (mobile video editing - Sekret's workflow)

---

### WORKFLOWS (WFL-###)

**WFL-NEW-001: SMM Content Funnel**
```
Sequence:
1. Create valuable free content (onboarding, tutorials)
2. Build follower base through value delivery
3. Engage with comments, build community
4. Occasional promotional content (stories, posts)
5. Targeted ads for specific campaigns
Purpose: Lead generation through owned channels
```

**WFL-NEW-002: Daily Report AI Analysis**
```
Sequence:
1. Employee writes daily report in markdown
2. Employee runs MAIN_PROMPT_v7 analysis on OWN report
3. Employee reviews: "What can I do better?"
4. Employee implements 1% improvement next day
5. Repeat cycle (compound improvement)
Purpose: Self-directed continuous improvement
```

**WFL-NEW-003: Research Integration Workflow**
```
Sequence:
1. Search YouTube for work-related videos (last 30-60 days, AI keywords)
2. Select 1 video relevant to your role
3. Parse video transcript (Whisper Flow or similar)
4. Extract entities (tasks, tools, actions)
5. Save to research folder in ENTITIES/TASK_MANAGERS/researches/
6. Update knowledge library
7. Apply learnings to daily work
Purpose: Continuous learning and skill development
```

**WFL-NEW-004: Prompt-First Development**
```
Sequence:
1. Describe task to AI
2. Ask AI: "Create a plan for me"
3. AI generates plan
4. Human reads line-by-line, checks accuracy
5. Human verifies: correct names? right folders? needed context?
6. If missing context: create context first
7. Human gives feedback, corrects errors
8. AI refines plan
9. Human approves
10. Execution begins
Purpose: Prevent errors, ensure quality, build documentation
```

**WFL-NEW-005: Multi-Phase AI Task Execution**
```
Sequence:
1. Define complex task
2. Ask AI: "Create multi-phase prompt, each phase separate file"
3. AI breaks into phases:
   - Phase 1: Research & Planning
   - Phase 2: Execution
   - Phase 3: Review & Refinement
   - Phase 4: Documentation
4. Each phase = separate file (chat interruption resilience)
5. Can execute phases in parallel (different AI chats)
6. Aggregate results
Purpose: Handle complex tasks, enable parallel work, prevent chat loss
```

**WFL-NEW-006: Pre-Sales Deep Research**
```
Sequence:
1. Receive prospect information
2. Conduct AI-assisted research:
   - Audit website
   - Identify gaps (no social, poor site, no video, etc.)
   - Competitive analysis
3. Feed research to AI: "Given context, prepare interview questions"
4. AI generates custom question list
5. Conduct detailed needs interview using questions
6. During call: probe pain points identified in research
7. Post-call: AI analyzes conversation
8. AI generates custom proposal based on specific needs
9. Send tailored proposal
Purpose: Close high-value deals through deep personalization
```

**WFL-NEW-007: Component Library Building (Design)**
```
Sequence:
1. Designer creates asset (background, pose, costume)
2. Designer saves prompt used
3. Designer logs: project, client, task, tool, time, difficulties
4. Over time: collect multiple variations
5. Request AI to templatize prompts
6. Break into components:
   - Backgrounds/ (10+ variants)
   - Poses/ (10+ variants)
   - Costumes/ (10+ variants)
7. Store in Constructor/ folder
8. Create auto-scan prompt:
   - Scans employee folders
   - Identifies missing components
   - Auto-updates library
Purpose: Build reusable design system, accelerate production
```

**WFL-NEW-008: Attendance Tracking & Issue Resolution**
```
Sequence:
1. Collect data from CRM (work hours)
2. Collect data from Discord (online presence)
3. Collect data from RAID (pending integration)
4. Cross-reference:
   - Expected hours (full-time 8, part-time 4)
   - Actual CRM hours
   - Discord presence
   - Daily report submitted (yes/no)
5. Identify discrepancies:
   - CRM = 0 but status = available (wrong status)
   - CRM ≠ Discord (investigate)
   - No report + no hours (absence)
6. Handle edge cases:
   - Electricity outages (Ukraine context) → makeup work
   - Weekends (cross-ref Gantt approvals)
   - Project employees (separate tracking)
7. Generate compliance report
8. Flag issues for HR/management
Purpose: Accurate attendance, identify non-compliance
```

---

### PROMPTS (PMT-###)

**Referenced Existing Prompts:**

- PMT-004: Video Transcription (mentioned in notes)
- PMT-032 to PMT-043: Department Daily Reports (mentioned)
- PMT-044: Sales Department Research (referenced for Mergent client)
- PMT-045: SMM Document Processing (referenced for content strategy)

**New Prompts Needed:**

**PMT-NEW-001: SMM Platform Specification Generator**
```
Purpose: Generate platform-specific content requirements
Input: Platform name (Instagram, Facebook, LinkedIn, etc.)
Output: Size/format specs, best practices, posting frequency
Reference: ENTITIES/LIBRARIES/SMM/content_strategy.md
```

**PMT-NEW-002: Black Friday Campaign Generator**
```
Purpose: Create promotional content for seasonal campaigns
Input: Department, offer type (1+1, discount, etc.)
Output: Post copy, promo codes, engagement mechanics
Context: Company capabilities, target audience
```

**PMT-NEW-003: Employee Daily Self-Analysis**
```
Purpose: Analyze employee's own daily report for improvements
Input: Employee's daily markdown file
Output:
  - What went well
  - What can improve
  - Specific suggestions (with tool/process recommendations)
  - Tomorrow's focus areas
```

**PMT-NEW-004: Component Library Templatizer**
```
Purpose: Convert designer prompts into reusable templates
Input: Collection of prompts (backgrounds, poses, costumes)
Output: Templatized prompts with variable placeholders
Department: Design (DGN)
```

**PMT-NEW-005: Attendance Discrepancy Analyzer**
```
Purpose: Identify attendance tracking issues
Input: CRM data, Discord data, expected hours
Output: List of discrepancies with suggested resolutions
Department: HR (HRM)
```

**PMT-NEW-006: Pre-Sales Research Report Generator**
```
Purpose: Create comprehensive prospect research report
Input: Prospect website, industry, LinkedIn profiles
Output:
  - Company overview
  - Gap analysis (missing: social, video, modern web, etc.)
  - Suggested interview questions
  - Preliminary service recommendations
Department: Sales (SLS)
```

**PMT-NEW-007: Video Tracking Table Maintainer**
```
Purpose: Update video production tracking table
Input: Daily video department reports
Output: Updated markdown table with completion status
Department: Video (VID)
```

**PMT-NEW-008: Vincere CRM Workflow Mapper**
```
Purpose: Analyze and document CRM workflows for automation
Input: Vincere CRM documentation, client process description
Output: Workflow diagrams, automation opportunities, integration points
Department: AI & Automation (AID) + Sales (SLS)
```

---

### RESPONSIBILITIES (RSP-###)

**New Responsibilities Identified:**

**RSP-NEW-001: Daily Report Compliance**
```
Role: All Employees
Description: Write detailed daily report in markdown format with:
  - Tasks completed
  - Projects worked on
  - Tools used
  - Time spent
  - Challenges encountered
  - Context for AI analysis
Frequency: Daily (end of day)
Consequence: Non-compliance = yellow flag → exit path
```

**RSP-NEW-002: Self-Analysis Execution**
```
Role: All Employees
Description: Run AI analysis on own daily report, identify improvements
Tool: MAIN_PROMPT_v7 (or current version)
Output: "What can I do better tomorrow?"
Frequency: Daily (after report writing)
```

**RSP-NEW-003: Research Integration**
```
Role: All Employees
Description: Find 1 YouTube video related to work, parse, extract entities
Repository: ENTITIES/TASK_MANAGERS/researches/
Frequency: Daily (or weekly minimum)
Purpose: Continuous learning, stay current with AI tools/techniques
```

**RSP-NEW-004: Work Environment Maintenance**
```
Role: All Employees
Required Tools:
  - VS Code (or Cursor, Anti Gravity)
  - Dropbox (enabled, syncing)
  - Claude Code Extension (or equivalent)
Verification: Self-check, no admin hand-holding
Consequence: Non-compliance = exit conversation
```

**RSP-NEW-005: Prompt Documentation**
```
Role: All Employees (especially Design, Dev)
Description: Save all AI prompts used in work:
  - Copy entire chat, OR
  - Ask AI to log prompts
  - Save to daily file or specific prompt library
Purpose: Build reusable knowledge base
```

**RSP-NEW-006: Context Building**
```
Role: All Employees
Description:
  - Download instructions from shared drives
  - Place in department folders
  - Give AI context for work-specific tasks
  - Ask: "How can I do this better?"
Frequency: Ongoing as new instructions created
```

**RSP-NEW-007: Detail Enrichment (Media/Design)**
```
Role: Design Department
Description: When uploading images/media, document:
  - Project name
  - Client name
  - Task ID
  - Prompt used
  - Tool used (Midjourney, DALL-E, etc.)
  - Difficulties
  - Time taken
Location: Media log in department folder
Purpose: Enable cross-team learning and improvement
```

**RSP-NEW-008: Pre-Call Research (Sales)**
```
Role: Sales Department, Lead Gen
Description: Before scheduled call:
  - Audit prospect website
  - Identify gaps
  - Generate AI-assisted question list
  - Prepare custom approach
Minimum: 1 day before call
Purpose: Maximize call conversion
```

**RSP-NEW-009: 1:1 Meeting Preparation**
```
Role: All Employees
Description: Before SMENA (1:1) meeting:
  - Prepare 10% checkpoint materials (plan/prompt for review)
  - OR 50% checkpoint (mid-progress for course correction)
  - OR 100% checkpoint (finished work for verification)
Expectation: Come with refined work, not first unread draft
```

**RSP-NEW-010: Makeup Work (Electricity Outages)**
```
Role: Employees with power outages (Ukraine context)
Description:
  - Log outages (not in daily report, communicate to team)
  - Track lost hours
  - Schedule makeup work (evenings, weekends)
  - Fulfill expected hours
Compensation: Overtime will be paid
```

**RSP-NEW-011: Knowledge Transfer**
```
Role: All Employees (especially those with successful workflows)
Description:
  - Document successful processes
  - Create tutorials for routine tasks
  - Share with team
  - Pass knowledge forward
Example: Svyat's Google scraping instructions (used by 2 people already)
```

**RSP-NEW-012: Naming Consistency (HR/Finance)**
```
Role: HR, Finance departments
Description:
  - Use consistent parameter names across systems
  - Don't switch languages (Ukrainian/English/abbreviations)
  - Define aliases if multiple names needed
  - Tell AI about name variations
Purpose: Enable accurate system analysis
```

---

### EMPLOYEES (EMP-###)

**Mentioned by Name (Role Context):**

| Name | Department/Role | Context |
|------|----------------|---------|
| **Nastya** | HR | Asked about MAIN_PROMPT v7, discussed empty folders issue |
| **Yulia** | Design (likely lead) | Anti Gravity user, discussed daily report analysis |
| **Polina** | Lead Gen | Asked to increase detail in lead gen reports |
| **Kolya** | Development/DevOps | Presented attendance tracking system |
| **Svyat** | Video/Development | Records calls, created Google scraping instructions |
| **Sekret** | Video | Edits interviews on phone |
| **Vlad** | Design/Development | Discussed instructions = context philosophy |
| **Katya** | Finance/Accounting | Discussed routine task automation |
| **Anya** | Unknown | Had admin access issue at end of call |
| **Plamenna** | Development | Using Svyat's Google scraping instructions |
| **Isaac** | Development | Using Svyat's Google scraping instructions |

**Roles Mentioned (not by name):**
- **Lead Gen team:** Discussed for reduction to 1-2 qualified people
- **Designers:** Cross-training for SMM work, component library building
- **Recruiters:** Comparison (charging $1000-1200 for SMM roles)
- **Admin Helper:** Role needed for SMENA scheduling (currently unfilled)

---

## CROSS-CUTTING THEMES

### 1. AI-FIRST MANDATE (Final Ultimatum)

**From Optional → Mandatory:**

Previous state:
- Years of requests ignored
- "For a long time we've been trying to transition to AI... at some stage attempts must turn into regular actions"
- "That stage has arrived"

New state:
- **No more attempts, no more reminders**
- **Use AI or exit conversation**
- "Bigger companies won't be able to waste time trying to teach someone who doesn't want to implement what we now need to release as a program. There is no business. So candidates will simply become fewer."

**Why Now:**

Global trend: "AI First Company"
- Access to analytical company data
- See full picture by reviewing records (vs. endless 1:1s)
- For employees: Find any action via YouTube videos
- Research system enables rapid innovation integration (1-2 days)
- One person can't do innovation for entire company

**Compliance Deadline:** Implied December (team finalization for December)

---

### 2. DOCUMENTATION AS SURVIVAL SKILL

**The Empty File Problem:**

Quote: "When AI receives an empty file, it has nothing to say. Neither to me about the department, nor anything else."

**Results of Empty Files:**
- Cannot track progress
- Cannot identify blockers
- Cannot plan next steps
- Cannot analyze learning curves
- CEO forced into manual checking loops

**CEO Work Impact:**

Quote: "Instead of developing our company, moving toward progress, implementing new tools, we run around dealing with nonsense like 'did you eat today?'"

**New Standard:**

Not acceptable: "I came to work today"

Required:
- Specific tasks
- Project names
- Tools used
- Time spent
- Challenges
- Context for AI

**Purpose:** Feed AI for analysis, improvement suggestions, progress tracking

---

### 3. SELF-DIRECTED IMPROVEMENT (1% Daily)

**The Question:** "Do we want to improve or not?"

**Philosophy:**

Quote: "Are we satisfied with our results and consider this our endpoint? Or will we day by day become 1% better?"

**Method:**
1. Write detailed report
2. AI analyzes report
3. AI suggests: "You can do X better"
4. Implement suggestion tomorrow
5. Compound effect over time

**Best Helper:** AI (but only if given full context)

**Critical Loop:**
- Can't ask AI without documentation
- Documentation enables AI analysis
- AI analysis enables improvement
- Improvement creates competitive advantage

---

### 4. PROMPT-FIRST DEVELOPMENT (Error Prevention)

**Standard Sequence:**

1. Ask AI: "Create a plan for me"
2. AI creates plan
3. **Human reads line-by-line** (most critical step)
4. Verify: correct names? right folders? needs context?
5. If missing context: plan context creation first
6. Give feedback (prevent error propagation)

**Re-reading Imperative:**

Quote: "Re-read, re-read, re-read again. How AI understood your notes, how it understood details. If it understood something wrong, another person won't understand either."

**Purpose:**
- Catch errors early
- Build accurate context
- Prevent cascade failures
- Create reusable documentation

---

### 5. CULTURAL DIVIDE (Innovation vs. Resistance)

**Two Employee Types:**

**Type A (Wanted):**
- Interested in AI
- Curious about experiments
- Ready to learn and change
- Engaged with team
- Not about overwork - about attitude

**Type B (Exit Path):**
- Against documentation
- Against AI usage
- Against learning new tools
- Silent non-compliance
- "Digging in heels, trying to slow down"

**CEO's Preference:**

Quote: "I'd rather have a direct honest conversation: 'I'm against it, I won't write, I can't write, haven't written since school 20 years ago, don't want to analyze or improve.' We'll treat you with respect and gratitude, but this year manual work stage ends."

**Unacceptable:** Silent resistance requiring detection systems

**December Goal:** Team of only Type A employees

---

### 6. CONTEXT = COMPETITIVE ADVANTAGE

**What is Context:**

Quote from Vlad: "Instructions = Context. The more we write step-by-step, we'll have MATERIAL FOR ANALYSIS. We'll have context for AI, specifically good quality context about our specific company, not in general."

**Context Sources:**
- Daily reports (detailed)
- Saved prompts
- Instructions downloaded from Google Drive
- Video transcripts
- Research findings
- Component libraries

**Context Uses:**
- AI analysis quality
- Onboarding new employees
- Cross-team learning
- Don't repeat explanations 10 times
- Systematic improvement

**Result:**
- More clients
- Better results
- Faster execution
- Scalable operations

---

### 7. SMALL SHIPPABLE PIECES (Anti-Premature Planning)

**Pattern Identified:** CEO has grand visions, team jumps ahead

**Example: SMM Launch**

Vision: Full SMM department, weekly themes, Discord announcements, gamified events

Reality check: "We haven't even logged into the accounts yet"

**CEO Self-Correction:**

Quote: "We need very small shippable pieces. First achievement: number of people who logged into accounts."

**Correct Sequence:**
1. Log into accounts (verify access) ← WE ARE HERE
2. Point to onboarding folder
3. Parse recent video into posts
4. Post first content
5. Verification (employee testing confirms it works)
6. THEN post publicly

**Metaphor Applied Elsewhere:**
- Component libraries: Start with backgrounds, one folder at a time
- Sales upgrade: One outdated item at a time
- Team restructuring: One week of compliance data before decisions

---

### 8. CROSS-DEPARTMENT ENTITY SHARING

**Principle:** Work done for ourselves = train sellable specialists

**Examples:**

**SMM Launch:**
- Company needs social presence (internal need)
- Designers learn SMM skills (training)
- SMM specialists sellable for $1000-1200 (revenue)

**Component Libraries (Design):**
- Designers build for company projects (internal)
- Process creates reusable templates (efficiency)
- Library becomes client deliverable (product)

**Research Workflows:**
- Employees research for own improvement (learning)
- Research builds company knowledge base (asset)
- Knowledge base becomes service offering (productization)

**Video Workflows:**
- Record internal meetings (documentation)
- Transcribe via Whisper Flow (data)
- Extract entities (taxonomy)
- Entities become task templates (reusable work)
- Templates sold to clients (service)

---

### 9. ELECTRICITY CRISIS (Ukrainian Context)

**The Constraint:**

Multiple employees experiencing power outages (implied: war-related infrastructure damage)

**Wrong Approach:**

Daily reports filled with: "power out, power out, power out"

**CEO Frustration:**

Quote: "Where is the company moving, what are we implementing, what progress - NONE. I don't need to record power outages."

**Right Approach:**

1. Team knows who has power issues (communicate once)
2. Don't log each outage in daily work reports
3. Track lost hours separately
4. Schedule makeup work (evenings, weekends)
5. Will be compensated (overtime pay)
6. But hours MUST be recovered

**Scheduling Impact:**
- Don't schedule calls during known outage times
- Consider shift work (some work evenings when power available)

---

### 10. DECEMBER DEADLINE (Team Finalization)

**Timeline:**

- **End November:** Current week (26th is Tuesday)
- **December 1:** Finalized team composition deadline

**Process:**

1. **This Week:** Monitor compliance with 3 requirements
   - Daily reports + self-analysis
   - Work environment setup
   - Research integration

2. **End November:** Identify non-compliant employees

3. **Conversations:** Direct discussion with those who don't want to comply

4. **December Start:** Begin with only engaged, AI-ready team

**Yellow Flag System:** Enforcement starting (mentioned in message.md)

**Expected Outcome:** Smaller team, but fully aligned with AI-first culture

---

## TECHNICAL SPECIFICATIONS

### System Architecture Components

**Current State:**

```
ENTITIES/
├── TASK_MANAGERS/
│   ├── DATA/
│   │   ├── Projects_Master.csv
│   │   ├── Milestones_Master.csv
│   │   ├── Tasks_Master.csv
│   │   └── Steps_Master.csv
│   ├── researches/ (video parsing workflows)
│   └── TSM-006_Workflows/ (to be parsed into milestones)
├── LIBRARIES/
│   ├── Tools/ (will remain in v7)
│   ├── Actions/ (will be reorganized by department)
│   ├── Objects/ (relocating close to Actions)
│   ├── Skills/ (archiving, moving to TALENTS)
│   ├── Profiles/ (archiving, moving to TALENTS/Employees/)
│   ├── Responsibilities/ (needs master file creation)
│   └── SMM/ (content_strategy.md, platform specs, historical data)
├── PROMPTS/
│   ├── Core/
│   │   ├── MAIN_PROMPT_v6.md (current)
│   │   └── MAIN_PROMPT_v7.md (in development)
│   ├── DEPARTMENTS/ (dept-specific prompts, need relocation)
│   └── [various prompt files PMT-001 to PMT-073+]
├── TAXONOMY/
│   └── TAX-002_Task_Managers (needs ID system update)
├── DAILIES/
│   └── REPORTS/
│       └── Week_4/ (test data for v7: folders 24, 25)
├── DEPARTMENTS/
│   ├── AI/ (AID)
│   ├── Design/ (DGN)
│   ├── Video/ (VID)
│   ├── HR/ (HRM)
│   ├── Finance/ (FNC → FIN rename needed)
│   ├── Lead_Gen/ (LGN)
│   ├── Sales/ (SLS)
│   ├── Marketing/ (MKT)
│   ├── SMM/ (new, being created)
│   └── Development/ (DEV)
└── TALENTS/
    └── Employees/ (profiles being created, started Nov 24)
```

**Required Changes:**

1. **ID Standardization:**
   - Remove category prefixes: `TSK-VID-042` → `TSK-042`
   - Finance department: `FNC` → `FIN`
   - Add Master CSV files to all entity folders

2. **Library Reorganization:**
   - Actions: Add department categories
   - Objects: Move near Actions
   - Skills/Profiles: Archive from LIBRARIES, integrate with TALENTS
   - Responsibilities: Create master file

3. **Prompt Folder:**
   - Clean duplicate/misplaced prompts
   - Move department prompts to accessible locations
   - Modularize MAIN_PROMPT v7 into sections

4. **Employee Profiles:**
   - Collect from Nov25/ and Finance/ folders
   - Centralize in ENTITIES/TALENTS/Employees/
   - Include: skills, tools, department, status

---

### Tool Ecosystem

**AI Tools in Use:**

| Tool | Accounts | Limitation | Workaround |
|------|----------|------------|------------|
| Claude (via extensions) | 8 total | Token exhaustion after 2-3 hours | Rotate accounts, 3-hour cooldown |
| Cursor | Multiple | Token limits | Switch to Anthropic accounts |
| Anti Gravity | Multiple | Gemini model issues | `/login` to switch without losing chat |
| VS Code + Extension | Standard | Requires setup compliance | Mandatory for all employees |

**CRM & Tracking:**

| Tool | Purpose | Issue |
|------|---------|-------|
| CRM (unnamed) | Work hour tracking | Auto-deducts 1 hour (breaks), causing discrepancies |
| Discord | Online presence | Used for attendance cross-reference |
| RAID | (Mentioned, unclear) | Pending integration |
| Gantt Chart | Time-off approval | Need cross-reference for weekend tracking |

**External Services:**

| Tool | Client/Use | Department |
|------|-----------|------------|
| Vincere CRM | Mergent client uses | Sales opportunity |
| Tripify | LinkedIn automation (Mergent) | Sales opportunity |
| Whisper Flow | Transcription | Video, All |
| Google Drive | Instruction storage | All |
| Dropbox | File sync | All (mandatory) |

---

### Data Flow Diagrams

**Daily Report Workflow:**

```
Employee Work
    ↓
Write Markdown Daily Report (detailed)
    ↓
Save to DAILIES/REPORTS/Week_X/[Date]/[Name].md
    ↓
Run MAIN_PROMPT_v7 Self-Analysis
    ↓
AI Output: "What can I do better?"
    ↓
Employee Reviews Suggestions
    ↓
Implements 1% Improvement Tomorrow
    ↓
[Cycle Repeats]
    ↓
Department Lead: Aggregate all dept reports
    ↓
Run Department-Level Analysis (PMT-0XX)
    ↓
CEO: Review Department Summaries (not individual files)
```

**Research Integration Workflow:**

```
YouTube Search (work-related, last 30-60 days, AI keywords)
    ↓
Select 1 Video
    ↓
Parse Transcript (Whisper Flow or manual)
    ↓
Extract Entities (tasks, tools, actions, workflows)
    ↓
Save to ENTITIES/TASK_MANAGERS/researches/
    ↓
Update Master CSVs (TOL-###, ACT-###, TSK-###)
    ↓
Apply to Work (immediate use)
    ↓
Document Application in Daily Report
```

**Attendance Tracking Workflow:**

```
CRM Data (work hours logged)
    ↓
Discord Data (online presence)
    ↓
RAID Data (pending integration)
    ↓
Cross-Reference System (Kolya's script)
    ↓
Identify Discrepancies:
  - CRM = 0, Status = Available (wrong status)
  - CRM ≠ Discord (investigate)
  - No Report + No Hours (absence)
  - Weekend counted as workday (fix weekend tracking)
    ↓
Handle Edge Cases:
  - Electricity outages (makeup work)
  - Project employees (separate tracking)
  - Approved time off (Gantt cross-ref)
    ↓
Generate Compliance Report
    ↓
HR/Management Action
```

**Component Library Building (Design):**

```
Designer Creates Asset
    ↓
Saves Prompt + Details (project, client, task, tool, time)
    ↓
Logs to Media Log (department folder)
    ↓
Over Time: Collect Variations
    ↓
Request AI: "Templatize these prompts"
    ↓
AI Breaks Into Components:
  - Backgrounds/ (10+ variants)
  - Poses/ (10+ variants)
  - Costumes/ (10+ variants)
    ↓
Store in Constructor/ Folder
    ↓
Create Auto-Scan Prompt:
  - Scans Employee Folders
  - Identifies Missing Components
  - Auto-Updates Library
    ↓
Reusable Design System (internal + client deliverable)
```

---

## ACTION ITEMS BY ROLE

### CEO

**Immediate:**
- [ ] Verify SMM account access (Instagram, Facebook, Twitter/X)
- [ ] Finalize MAIN_PROMPT v7 requirements
- [ ] Monitor daily report compliance (first week data)
- [ ] Schedule 1:1s (SMENA rotation)

**This Week:**
- [ ] Review attendance tracking system (Kolya's reports)
- [ ] Identify non-compliant employees (3 requirements)
- [ ] Conduct exit conversations if needed

**End November:**
- [ ] Finalize December team composition
- [ ] Complete Mergent discovery call
- [ ] Launch Black Friday SMM campaign (if ready)

---

### HR (Nastya, Team)

**Immediate:**
- [ ] Test MAIN_PROMPT v7 on Week_4 folders (24, 25)
- [ ] Update CRM statuses (fix "available" vs actual status)
- [ ] Cross-reference Gantt chart for weekend tracking

**This Week:**
- [ ] Collect employee profiles from Nov25/ and Finance/ folders
- [ ] Centralize in ENTITIES/TALENTS/Employees/
- [ ] Track daily report compliance by employee
- [ ] Implement yellow flag system tracking

**Ongoing:**
- [ ] Standardize employee name formats across systems
- [ ] Define makeup work policy for electricity outages
- [ ] Schedule SMENA (1:1s) rotation

---

### Design (Yulia, Vlad, Team)

**Immediate:**
- [ ] Implement markdown formatting in daily reports (##, **, [], etc.)
- [ ] Start component library creation (backgrounds first)
- [ ] Save all prompts used for image generation
- [ ] Log media details (project, client, task, tool, time, difficulties)

**This Week:**
- [ ] Create Constructor/ folder structure
- [ ] Begin SMM asset creation (onboarding content first 10 posts)
- [ ] Templatize existing prompts (backgrounds, poses, costumes)

**Ongoing:**
- [ ] Build auto-scan prompt for employee folder analysis
- [ ] Cross-train on SMM workflows

---

### Lead Gen (Polina, Team)

**Immediate:**
- [ ] Increase detail in daily reports (copy dialogues, profile details)
- [ ] Document outreach conversations in markdown

**This Week:**
- [ ] Assess team for sales aptitude (deep research capability)
- [ ] Prepare for potential team reduction (keep 1-2 qualified)

**Ongoing:**
- [ ] Implement pre-call research workflow (website audit, AI question generation)

---

### Sales (Team)

**Immediate:**
- [ ] Complete Mergent discovery research (Vincere CRM, Tripify, workflow mapping)
- [ ] Prepare 6-month talent proposal for Mergent

**This Week:**
- [ ] Audit company website for outdated skills/content
- [ ] Update website skills section from 2025 video transcripts
- [ ] Update sales presentation decks

**Ongoing:**
- [ ] Implement deep research pre-sales workflow (2-4 calls/month vs 40-80)
- [ ] Create pre-call AI research checklist

---

### Video (Svyat, Sekret, Team)

**Immediate:**
- [ ] Convert video tracking table to Markdown
- [ ] Save interview scripts to department folder
- [ ] Document video execution instructions

**This Week:**
- [ ] Implement AI-maintained video completion table
- [ ] Test auto-update workflow (AI reads daily reports, updates table)

**Ongoing:**
- [ ] Continue transcription workflows (Whisper Flow)
- [ ] Save all prompts/processes to daily files

---

### Development (Svyat, Plamenna, Isaac, Team)

**Immediate:**
- [ ] Share Google scraping instructions more widely (already done with 2 people)
- [ ] Create developer tutorial library in dept folder

**This Week:**
- [ ] Research Vincere CRM APIs (for Mergent automation)
- [ ] Explore Google Sheets automation (for video tracking table)

**Ongoing:**
- [ ] Document all successful workflows as tutorials

---

### Finance (Katya, Team)

**Immediate:**
- [ ] Standardize parameter naming (employee names especially)
- [ ] Create monthly routine instruction templates

**This Week:**
- [ ] Identify automation opportunities (weekend marking, etc.)
- [ ] Update all Finance references: FNC → FIN

**Ongoing:**
- [ ] Ask AI: "How can I automate this manual task?"

---

### AI & Automation (Team)

**Immediate:**
- [ ] Develop MAIN_PROMPT v7 (test on Week_4 data)
- [ ] Modularize v6 into approvable sections
- [ ] Create output templates for standardized datasets

**This Week:**
- [ ] Reorganize Actions library by department
- [ ] Archive Skills/Profiles from LIBRARIES
- [ ] Create Responsibilities master file
- [ ] Add Master CSV files to all ENTITIES folders

**Ongoing:**
- [ ] Global ID standardization (remove category prefixes)
- [ ] Test v7 extraction quality vs v4/v6
- [ ] Inject taxonomy rules per prompt section

---

### Marketing/SMM (New Department)

**Immediate:**
- [ ] Verify account access (Instagram, Facebook, Ads Manager)
- [ ] Obtain website CMS posting credentials
- [ ] Review existing SMM library (ENTITIES/LIBRARIES/SMM/)

**This Week:**
- [ ] Document platform specifications (from existing strategy docs)
- [ ] Plan first 10 posts (onboarding/value content, NOT sales)
- [ ] Design funnel strategy

**End November:**
- [ ] Launch Black Friday campaign (if accounts accessible)
- [ ] Begin regular posting schedule

---

### All Employees

**Immediate (This Week):**
- [ ] Write detailed daily reports in markdown
- [ ] Run MAIN_PROMPT v7 self-analysis on own reports
- [ ] Verify work environment setup (VS Code/Cursor, Dropbox, Claude Extension)

**Ongoing:**
- [ ] Research integration: 1 YouTube video per day (or week minimum)
- [ ] Save all AI prompts used
- [ ] Build context (download instructions, place in dept folders)
- [ ] Attend SMENA (1:1s) when scheduled
- [ ] For electricity outages: track lost hours, schedule makeup work

**Compliance Deadline:** December 1 (implied)

**Consequence of Non-Compliance:** Exit conversation with respect and gratitude

---

## RISK ANALYSIS

### Critical Risks

**1. Mass Employee Departure (Cultural Rejection)**

**Risk:** Large portion of team refuses AI adoption, exits by December
**Impact:** Operational capacity loss, project delays, client service interruptions
**Likelihood:** Medium-High (based on years of non-compliance)

**Mitigation:**
- Clear communication sent (message.md) ✅
- Admin call held (AdminCall.md) ✅
- 1-week observation period (compliance data collection)
- Respectful exit process for non-compliant employees
- Acceptance of smaller, aligned team over larger resistant team

**CEO Philosophy:** "Better 4 engaged people than 20 going through the motions"

---

**2. SMM Launch Premature Execution**

**Risk:** Jumping to Black Friday campaign before account access verified
**Impact:** Campaign failure, wasted effort, team demoralization
**Likelihood:** High (CEO self-identified pattern of premature planning)

**Mitigation:**
- CEO self-corrected: "We need small shippable pieces"
- Sequence enforced: Log into accounts FIRST
- Then onboarding content, then verification, THEN public posting
- Black Friday campaign may be delayed (acceptable)

---

**3. Token Exhaustion Blocking Strategic Work**

**Risk:** CEO cannot work during business hours, forced into nights/weekends
**Impact:** Slow strategic decision-making, CEO burnout, company direction suffers
**Likelihood:** Currently happening (8 accounts exhausted daily)

**Mitigation:**
- MAIN_PROMPT v7 enables employee self-analysis (reduces CEO AI usage)
- Local AI model project (mentioned in previous sessions, not in this day's notes)
- Account rotation system (3-hour cooldown management)
- Expectation: v7 reduces CEO manual analysis workload

---

**4. Electricity Outages (Ukrainian Context)**

**Risk:** Unpredictable power loss reduces team capacity
**Impact:** Missed deadlines, client dissatisfaction, revenue loss
**Likelihood:** Ongoing (multiple employees affected)

**Mitigation:**
- Makeup work policy (evenings, weekends, compensated)
- Shift work consideration (work when power available)
- Don't schedule calls during known outage times
- Separate tracking (don't pollute daily reports with outage logs)

**Limitation:** External infrastructure issue, no internal control

---

**5. MAIN_PROMPT v7 Development Delays**

**Risk:** v7 not ready before December team finalization
**Impact:** Employee self-analysis workflow unavailable, compliance measurement unclear
**Likelihood:** Medium (aggressive timeline, test data available)

**Mitigation:**
- Test data ready: Week_4 folders (24, 25)
- Can use v6 temporarily for employee self-analysis (suboptimal but functional)
- Modular development (section-by-section approval)
- Clear requirements documented (this session's notes)

---

### Medium Risks

**6. Attendance Tracking System Inaccuracies**

**Risk:** CRM/Discord discrepancies cause unfair performance assessments
**Impact:** Employee dissatisfaction, wrongful terminations, legal issues
**Likelihood:** Medium (system shows discrepancies, being refined)

**Mitigation:**
- Kolya developing detailed daily breakdown
- Cross-reference multiple data sources (CRM + Discord + RAID)
- Handle edge cases explicitly (weekends, project employees, approved time off)
- Manual review for discrepancies before action

---

**7. Mergent Client Acquisition Failure**

**Risk:** Cannot close 6-month talent engagement
**Impact:** Lost revenue opportunity, SMM demo opportunity missed
**Likelihood:** Medium (prospect stage, no relationship depth yet)

**Mitigation:**
- Deep research workflow (PMT-044: Sales Department Research)
- Demonstrate SMM capabilities (timing aligns with internal launch)
- Vincere CRM expertise development (research APIs, workflows)
- Realistic expectations (it's a prospect, not a guarantee)

---

**8. Component Library Building Delays (Design)**

**Risk:** Designers don't log prompts, library remains fragmented
**Impact:** Cannot templatize, no reusable system, client deliverable missing
**Likelihood:** Medium (requires new habit formation)

**Mitigation:**
- Clear instructions given (Vlad understands requirement)
- CEO enthusiasm ("Super! Fire!") motivates compliance
- Incremental approach (backgrounds first, then poses, then costumes)
- Auto-scan prompt eventual automation (reduces manual maintenance)

---

### Low Risks (Monitored)

**9. Video Tracking Table Automation Delays**

**Risk:** Manual table maintenance continues, AI automation not implemented
**Impact:** Svyat's time wasted on routine updates
**Likelihood:** Low (clear workflow identified, Svyat capable)

**Mitigation:**
- Markdown conversion straightforward
- AI can update Markdown based on daily reports
- Periodic sync back to Google Sheets (or API exploration)

---

**10. Pre-Sales Pivot Resistance (Sales Team)**

**Risk:** Sales team prefers volume (40-80 calls) over depth (2-4 researched calls)
**Impact:** Strategy change fails, CEO forced back into delivery mode
**Likelihood:** Low (CEO directive, logical strategy)

**Mitigation:**
- Lead gen team reduction to 1-2 people (forced focus on quality)
- Deep research workflow provides clear process
- Example success story cited (friend closing $8k deals)
- CEO moving to pre-sales personally (leads by example)

---

## GAPS & MISSING INFORMATION

### Information Gaps

1. **SMM Account Credentials:**
   - Who has admin access to Instagram/Facebook?
   - What is the company Instagram handle (remote.place? remote? something else?)
   - Facebook page name?
   - Are accounts active or dormant?

2. **MAIN_PROMPT v7 Timeline:**
   - Specific deadline for v7 completion?
   - Who is developing it (AI team? CEO? Nastya?)
   - Approval process for modular sections?

3. **Yellow Flag System Criteria:**
   - Specific metrics for yellow flags?
   - How many flags = exit conversation?
   - Who tracks/enforces (HR? Department leads? CEO?)

4. **Attendance System Details:**
   - What is RAID tool?
   - How is CRM break time calculated (automatic -1 hour mentioned, but how?)
   - Who reviews discrepancy reports?

5. **Mergent Client:**
   - Who is the contact at Mergent?
   - When was initial contact made?
   - What triggered their interest?
   - Timeline for proposal delivery?

6. **Employee Profiles Creation:**
   - Who is responsible for collecting from Nov25/ and Finance/ folders?
   - What data fields required in employee profiles?
   - Integration with CRM/Discord/RAID?

7. **Black Friday Campaign:**
   - Budget for Facebook Ads (if using paid promotion)?
   - Who approves creative assets?
   - Measurement metrics?

8. **1:1 Meeting (SMENA) Logistics:**
   - Who will be admin helper scheduling these?
   - Frequency per employee (1x/week? 2x/week?)
   - Duration per meeting?
   - Department rotation order?

---

### Process Gaps

1. **Employee Exit Process:**
   - Formal offboarding checklist?
   - Knowledge transfer requirements?
   - Access revocation process?

2. **Makeup Work (Electricity):**
   - How are makeup hours tracked?
   - Approval process for weekend/evening work?
   - Overtime pay calculation method?

3. **Research Video Workflow:**
   - Centralized repository for parsed videos?
   - Deduplication (if multiple people find same video)?
   - Quality standards for entity extraction?

4. **Component Library Governance:**
   - Who approves templates before adding to Constructor/ folder?
   - Version control for prompt templates?
   - Integration with client projects?

5. **Pre-Sales Research Workflow:**
   - Template for research reports?
   - AI prompts for website audits?
   - Question generation prompts?

---

### Technical Gaps

1. **Vincere CRM API:**
   - Documentation access?
   - API key availability?
   - Rate limits?
   - Integration possibilities?

2. **Tripify LinkedIn Automation:**
   - How does it work?
   - Can we replicate for own use?
   - Legal/compliance considerations?

3. **Google Sheets Automation (Video Table):**
   - API credentials available?
   - Script development owner?
   - Sync frequency?

4. **Attendance System Integrations:**
   - CRM API for data extraction?
   - Discord API for presence tracking?
   - RAID integration method?

5. **Master CSV Updates:**
   - Who validates new entity IDs before assignment?
   - Commit approval process?
   - Merge conflict resolution?

---

## TERMINOLOGY GLOSSARY

**Yellow Flag System:** Transparency tool for tracking employee compliance with company standards (not punishment, but progress indicator)

**SMENA (Russian: "shift"):** Scheduled weekly 1:1 meetings between employees and management

**Whisper Flow:** Transcription tool used for converting audio/video to text

**Constructor Folder:** Design department's component library structure (backgrounds, poses, costumes as reusable templates)

**Daily Proceed:** Daily report analysis workflow using AI (Anti Gravity team's term)

**Funnel:** Marketing term for customer journey (awareness → interest → desire → action)

**1+1 Offer:** Promotional structure where purchase includes free additional service (e.g., buy 1 lead gen hour, get 1 free)

**Pre-Sale:** Sales approach focusing on preparation/research before delivery commitment (vs. selling then scrambling to deliver)

**Deep Research:** Intensive AI-assisted prospect analysis (website audit, gap analysis, custom question generation)

**Entity:** Structured data object in MAIN_PROMPT taxonomy (PRT, MLT, TSK, STP, ACT, OBJ, TOL, etc.)

**Templatize:** Convert specific prompts into reusable templates with variable placeholders

**Context:** Background information given to AI to improve output quality (instructions, past work, company specifics)

**Prompt-First Development:** Workflow where AI creates plan before execution (vs. jumping straight to execution)

**Multi-Phase Prompt:** AI instruction broken into separate files for resilience (chat interruption protection)

**Component Library:** Reusable design elements (backgrounds, poses, costumes) with documented prompts

**Makeup Work:** Hours worked outside normal schedule to compensate for lost time (e.g., electricity outages)

**Remote Helpers:** Company name

**Remote.place (or Remote):** Company's SMM account names (uncertain which is correct)

**Available vs. Pre-Sale (CRM Status):** Employee availability designation affecting expected work hours

**Project Employee:** Staff assigned to external client projects (tracked separately from internal work)

**Vincere:** Recruitment CRM software used by Mergent prospect

**Tripify:** LinkedIn automation tool used by Mergent

**The Access Group:** Vendor of Vincere CRM

**TOL-### / ACT-### / OBJ-### / etc.:** Entity ID formats in taxonomy system

**v4 / v6 / v7:** MAIN_PROMPT framework versions

**Week_4:** Week 4 of November 2025 (approximately Nov 24-30)

**Gantt:** Project timeline/scheduling tool (mentioned for approved time-off tracking)

**RAID:** Unknown tool for attendance/project tracking (mentioned but not explained)

---

## METADATA

**Analysis Completed:** 2025-11-27
**Analyst:** AI & Automation Department
**Framework Version:** MAIN_PROMPT v6.0
**Word Count:** ~18,500 words
**Entities Extracted:** 60+ tasks, 14+ milestones, 5+ projects, 20+ actions, 25+ objects, 30+ tools, 12+ responsibilities, 8+ prompts (new), 10+ employees identified
**Languages Detected:** English (primary), Russian (transcript sections, translated where critical)
**Source Files:** 4 (261125.md, Clients.md, message.md, AdminCall.md)
**Total Source Lines:** ~218 lines combined

---

## APPENDIX: RUSSIAN LANGUAGE CONTEXT

**Transcript Sections:** Multiple sections of 261125.md and AdminCall.md contain Russian/Ukrainian language discussion transcripts. These were analyzed for content and key quotes translated where essential to understanding.

**Key Translated Themes:**
1. Sales upgrade discussion (outdated content = "expired goods" metaphor)
2. SMM funnel strategy (value-first, then occasional promotion)
3. Team restructuring announcement (respectful but firm)
4. AI adoption ultimatum (use AI or respectful exit)
5. Documentation requirements (detailed, specific, not generic)
6. Electricity outage policy (makeup work required)
7. Cultural philosophy (1% daily improvement, learning mindset)

**Not Fully Translated:** Sections with repetitive points or tangential discussions were summarized rather than fully translated to maintain focus on actionable information.

---

**END OF COMPREHENSIVE ANALYSIS**
