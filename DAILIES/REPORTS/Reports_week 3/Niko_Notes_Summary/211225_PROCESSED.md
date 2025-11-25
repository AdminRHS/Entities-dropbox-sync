# 211225 - Working Session Transcriptions (Processed via PMT-073)
**Date:** 2025-11-21 | **Type:** Multiple Working Sessions | **Processor:** MAIN_PROMPT_v6
**Language:** Russian (Transcribed) | **Status:** Entity-Tagged | **Format:** Conversation → Tasks

---

## DOCUMENT OVERVIEW 📋

**Content Type:** Audio/Video Transcriptions of Working Sessions
**Participants:** Multiple (Identified below)
**Topics:** Google Maps Scraping, HR Dashboard, Video Processing, AI Tools Management, Employee Onboarding
**Duration:** Full day sessions (multiple conversations)
**Primary Language:** Russian

---

## 1. IDENTIFIED PARTICIPANTS 👥

| Name | Role/Department | Mentioned Context |
|------|----------------|-------------------|
| **Стас (Stas)** | Lead/Manager | Google scraping, job sites, leading discussions |
| **Коля (Kolya/Nikolay)** | Developer | HR Dashboard development, Vercel deployment |
| **Вильгельм (Vilhelm)** | Developer/New | Learning video parsing, VS Code setup, onboarding |
| **Юля (Yulya)** | Team Member | Dashboard work, design tasks |
| **Оля (Olya)** | Team Member | Sales/CRM tasks delegation |
| **Настя (Nastya/Anastasiya Bykova)** | HR/Designer | Client interviews, poor work examples noted |
| **Ксения (Kseniya)** | Lead Gen | Junior entry position targeting |
| **Даниэль (Daniel)** | Designer | Mentioned in interviews |
| **Эленора (Eleanor)** | Designer | UI Kit work mentioned |
| **Димa Торзок (Dima Torzok)** | Technical | Subtitles, transcription work |
| **Реководoлд (Rekvold)** | Team Member | Mentioned in previous notes |

**Profile Entities:** PRF-### (to be assigned per employee)

---

## 2. MAJOR PROJECTS IDENTIFIED 🏗️

### PRT-011: Google Maps Scraping System
**Owner:** Stas + LGN Department
**Priority:** CRITICAL
**Status:** Development → Testing

#### Context (Translated Summary):
- Rethinking scraping approach after last conversation
- Latest batch targeted Junior Entry Positions only
- Filtering by company professions offered
- System needs better filtering for results
- Need to test if better filtering improves outcomes

#### Components Discussed:

**A. Search Query Optimization**
- **Issue:** Query formation needs AI optimization
- **Solution:** Create long, detailed prompt for Column H (Google request formation)
- **Historical Data:** Search queries file on Google Drive (thousands of LinkedIn queries)
- **Action:** Reformat existing queries for Google Maps

**B. Scraper Workflow**
- Currently manual process:
  1. Enter Google Maps
  2. Write AI-generated request
  3. Run scraper
  4. Process results

**C. URL Analysis & Data Extraction**
- Extract Google Maps URL structure
- Parse: `vr+business+sales+...`
- Need to cut/clone column, trim URL
- Extract variables after `/maps/`
- Analyze `/place/` structure (e.g., `/place/Georgia_state`)
- Company name extraction working
- Website link extraction (where available)

**D. CRM Integration**
- Automation exists for job sites
- Same automation can work for different table
- Check CRM for duplicates before adding

#### Milestones:

| ID | Milestone | Tasks | Owner |
|----|-----------|-------|-------|
| **MLT-029** | Search Query System | Column H prompt architecture, AI query optimization | Stas + AID |
| **MLT-030** | Scraper Automation | Manual → Semi-automated workflow | Stas + DEV |
| **MLT-031** | Data Processing | URL parsing, company extraction, deduplication | DEV |
| **MLT-032** | CRM Integration | Connect to existing automation, duplicate checking | DEV + LGN |
| **MLT-033** | Testing & Analytics | Track results, build analytics on collected data | LGN + AID |

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-106** | Find historical search queries file on Google Drive | OBJ-### (Document) | LGN | HIGH |
| **TSK-107** | Reformat LinkedIn queries for Google Maps | ACT-###, PMT-066 | LGN + AID | HIGH |
| **TSK-108** | Create detailed prompt for query generation (Column H) | PMT-### | AID | CRITICAL |
| **TSK-109** | Build URL parsing script | TOL-###, ACT-### | DEV | HIGH |
| **TSK-110** | Extract company name from URLs | ACT-###, OBJ-### | DEV | MEDIUM |
| **TSK-111** | Connect scraper to CRM automation | TOL-###, ACT-### | DEV | HIGH |
| **TSK-112** | Implement duplicate checking against CRM | ACT-###, OBJ-### | DEV | HIGH |
| **TSK-113** | Test scraping with 3-4 videos about Google Maps scraping | PMT-004, ACT-### | Vilhelm + VID | HIGH |
| **TSK-114** | Allocate 5 lead generators, 1-2 hours/day for Google Maps | PRF-###, RSP-### | LGN | HIGH |
| **TSK-115** | Create attractive offer for leads (20 Google vs 5 LinkedIn) | ACT-###, OBJ-### | LGN | MEDIUM |

**Prompts:** PMT-004 (Video Transcription), PMT-039 (LG), PMT-066 (Automation)

---

### PRT-012: Reviews Scraping & Analysis System
**Owner:** Stas + LGN + AID
**Priority:** HIGH
**Status:** System Ready → Pending Launch

#### System Overview (Translated):

**Stage 1: Company Scraping**
- Collect companies
- Clean data
- Connect to second script

**Stage 2: Reviews Collection**
- Go to each company from Stage 1
- Scrape reviews from Google listing
- Format: Company Name, Review Text, Review Date
- Filter: 4 stars and below, up to 50 max per company
- Logic: Prioritize newest low-rating reviews (3-5 stars and below)

**Stage 3: Semantic Analysis**
- Analyze reviews with AI
- Anchor: Specific profession + specific problem
- Link problems to professions
- Generate Problem Score

**Stage 4: Final Table Output**

| Field | Source | Description |
|-------|--------|-------------|
| Company | Stage 1 | Company name |
| Website | Stage 1 | Company website |
| Category | Stage 1 | Business category |
| Review Count | Stage 1 | Total review count |
| Average Rating | Stage 1 | Average star rating |
| Review Velocity | Calculated | Reviews in last 90 days |
| Problem Score | Stage 3 | Count of issues per profession |
| Profession Match | Stage 3 | Developers, Designers, etc. |
| Summary | Stage 4 | AI recommendation letter |

**Stage 5: Recommendation Generation**
- If Problem Score exists: Generate recommendation based on reviews
- If no issues: Generate general recommendation
- Output: Recommendatory email/letter for outreach

#### Additional Features Discussed:

**Social Media Scraping**
- Scrape their social networks
- Check their website for social links (Instagram, Facebook, Twitter, YouTube)
- Find links (usually in footer)
- Collect social media URLs

#### Issues Raised:
> "How will we mark this as coming from Google Maps source?"
> "I thought you already launched it and had calls on these!"
> **Response:** No, just finished system implementation, wanted to show before launching

#### Feedback from Manager:
> "You should come at 20%, 40%, 60% stages, not at the end when everything needs redoing. At each stage, you should:
> - Do lots of research
> - Run research in 3-4-5 AI systems
> - Have a research plan
> - Document each stage with instructions
> - Gather world's accumulated knowledge on Google Maps scraping methodologies
> - Create guidelines for your direction"

#### Milestones:

| ID | Milestone | Status | Owner |
|----|-----------|--------|-------|
| **MLT-034** | Company & Reviews Data Collection | Complete | Stas |
| **MLT-035** | Semantic Analysis Setup | Complete | Stas + AID |
| **MLT-036** | Problem Score Algorithm | Complete | Stas + AID |
| **MLT-037** | Recommendation Engine | Complete | Stas + AID |
| **MLT-038** | Social Media Integration | Planned | DEV |
| **MLT-039** | Source Tracking & Documentation | Pending | AID |

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-116** | Document scraping system (20% checkpoint) | ACT-023, OBJ-028 | AID | CRITICAL |
| **TSK-117** | Research world methodologies on Google Maps scraping | PMT-051, ACT-### | AID + LGN | HIGH |
| **TSK-118** | Create guidelines for reviews scraping direction | OBJ-###, ACT-023 | AID | HIGH |
| **TSK-119** | Add source marking for Google Maps data | ACT-###, OBJ-### | DEV | HIGH |
| **TSK-120** | Implement social media scraping | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-121** | Test review system with live data | ACT-###, OBJ-### | LGN | HIGH |
| **TSK-122** | Launch system with LGN team | PRF-###, RSP-### | LGN | HIGH |

**Prompts:** PMT-039 (LG), PMT-051 (Research), PMT-066 (Automation)

---

### PRT-013: Job Sites Entity Creation
**Owner:** Stas + Vilhelm + AID
**Priority:** HIGH
**Status:** In Progress

#### Context:
- Create ENTITIES folder structure for job sites
- Job sites data exists in JSON format in Stas's folder
- Need to integrate into ENTITIES taxonomy
- Location: `ENTITIES/ACCOUNTS/Job_Sites/`

#### Workflow Discussed:

**Step 1:** Go to ENTITIES/Accounts
**Step 2:** Create Job Sites folder
**Step 3:** Look at taxonomy of other entities to understand structure
**Step 4:** Create proper entity structure (Master JSON, etc.)

#### AI Tools Used:
- **Claude Code Extension** in VS Code
- **Cursor** for development
- Discussion about tool limitations and token usage

#### Tasks:

| ID | Task | Entities | Assignee | Priority |
|----|------|----------|----------|----------|
| **TSK-123** | Create Job Sites folder in ENTITIES/ACCOUNTS | OBJ-012 (Directory) | Vilhelm | HIGH |
| **TSK-124** | Review other entities' taxonomy | ACT-###, OBJ-### | Vilhelm | HIGH |
| **TSK-125** | Build Job Sites entity structure | ACT-008, OBJ-### | Vilhelm + AI | HIGH |
| **TSK-126** | Create Master JSON for Job Sites | OBJ-###, ACT-### | Vilhelm | MEDIUM |
| **TSK-127** | Document Job Sites entity | ACT-023, OBJ-028 | Vilhelm | MEDIUM |

**File Path:** Already created at `ENTITIES/ACCOUNTS/Job_Sites/`
**Prompts:** PMT-016 (Taxonomy Creation), PMT-028 (Folder Reorganization)

---

### PRT-014: HR Attendance Dashboard
**Owner:** Kolya (Nikolay) + Design Team
**Priority:** CRITICAL
**Status:** Development → Deployment

#### Links:
- **GitHub:** https://github.com/AdminRHS/employees-attendance-dashboard
- **Vercel:** https://vercel.com/remote-helpers/hr-dashboard
- **Dropbox:** `Nov25/AI/Artemchuk Nikolay/Employees attendance`

#### Current Features (v1.0):

**Data Sources:**
- Discord time tracking
- CRM time tracking
- All employees (project & non-project)
- Workers visible
- Hours visible
- Reports visible
- Weekend/day-off status

**Display:**
- User attendance data
- Dates/feeds per user
- Time in Discord
- Time in CRM
- Report submissions

#### Requested Features:

| Feature | Priority | Assignee | Status |
|---------|----------|----------|--------|
| Tool filtering (e.g., show only Cursor Pro accounts) | HIGH | Kolya | Planned v2 |
| User assignment tracking (who's logged in) | HIGH | Kolya | Planned v2 |
| Login session tracking (occupied status) | HIGH | Kolya | Planned v2 |
| Limit expiry dates | HIGH | Kolya | Added (incomplete) |
| UI Kit integration (from Eleanor's work) | MEDIUM | Design Team | Planned |
| LibDev catalog integration | LOW | Kolya | Planned v3 |
| API publication | LOW | Kolya | Planned v3 |

#### Deployment Plan:

**Monday Tasks:**
1. Publish v1.0 to all tools and developers
2. Share accounts dashboard access
3. Begin v2 development (user logging system)

**Tuesday/Next Week:**
- User integration with logging
- API development
- User assignment connections

#### Technical Stack:
- **Framework:** Next.js
- **Styling:** Tailwind CSS
- **Hosting:** Vercel (recommended over Netlify for Next.js)
- **Version Control:** GitHub
- **Local:** Running locally first, then deploy

#### Data Source:
- Google Sheets import from AI tab
- Future: Direct database integration

#### Design Notes:
- White text needs fixing
- Calendar addition needed
- Many employees need basic training
- Better to iterate quickly than perfect first version

#### Tasks:

| ID | Task | Entities | Department | Priority | Timeline |
|----|------|----------|------------|----------|----------|
| **TSK-128** | Deploy v1.0 to Vercel | TOL-### (Vercel) | DEV | CRITICAL | Monday |
| **TSK-129** | Share dashboard access with all departments | ACT-###, PRF-### | HRM + DEV | CRITICAL | Monday |
| **TSK-130** | Fix white text display | ACT-###, OBJ-### | DGN | MEDIUM | Monday |
| **TSK-131** | Add tool filtering feature | TOL-###, ACT-### | DEV | HIGH | v2 (Tuesday) |
| **TSK-132** | Implement user login tracking | TOL-###, ACT-### | DEV | HIGH | v2 |
| **TSK-133** | Create user assignment system | PRF-###, ACT-### | DEV | HIGH | v2 |
| **TSK-134** | Integrate UI Kit from Eleanor's work | OBJ-###, TOL-### | DGN | MEDIUM | v2 |
| **TSK-135** | Add calendar feature | TOL-###, ACT-### | DEV | MEDIUM | v2 |
| **TSK-136** | Build API for dashboard data | TOL-###, ACT-### | DEV | LOW | v3 |
| **TSK-137** | Integrate with LibDev catalog | TOL-###, OBJ-### | DEV | LOW | v3 |
| **TSK-138** | Document dashboard usage | ACT-023, OBJ-028 | HRM + AID | MEDIUM | Post-launch |
| **TSK-139** | Create employee training materials | ACT-###, OBJ-### | HRM | MEDIUM | Monday |

#### Meeting Notes:
> "It looks amazing! Much better than viewing Markdown. A bit of shading, colors... Now Vilhelm knows where things are located."

> "All our developments, everything we invested so much time in, can now come alive!"

**Prompts:** PMT-036 (Dev), PMT-038 (HR), PMT-066 (Automation)

---

### PRT-015: Vilhelm Onboarding & Video Processing Training
**Owner:** Stas + Kolya + Vilhelm
**Priority:** HIGH
**Status:** Active Training

#### Training Topics:

**1. Video Parsing Workflow**
- Find videos prompt
- Integrate video channels
- Influencer channels prompt
- Research and select 3-4 videos on Google Maps scraping
- Parse one video fully by end of session
- Goal: Minimum 1 video per day per employee

**2. VS Code / Cursor Setup**
- Install Claude Code Extension
- Login to dd@rh-s.com account
- Configure key bindings
- Set up workspace folders
- Learn to use Copy Path functionality

**3. Entity System Understanding**
- Introduced to ENTITIES folder structure
- PROMPTS ecosystem explanation
- Research prompts location
- File organization system

**4. AI Tools Training**
- **Claude Code:** For coding and entity work
- **Windsurf:** For personal folder work
- **Gravity:** Testing for development
- **Gemini & GPT:** For research

**5. Account Management**
- AI tools account limits documented
- Google Sheets with account tracking: Niko tab shows limits
- Vilhelm assigned accounts with expiry tracking
- Login tracking system explained

#### Key Instructions Given:

> **Kolyа to Vilhelm:** "Show Vlad how to do research on YouTube, how to import. We'll scrape 3-4 videos about parsing from Google Maps. It's time."

> **Stas:** "At least one video per day each person needs to parse, just to maintain fitness. Otherwise the system runs empty, spinning the same things. The system doesn't evolve."

> **On Research Process:** "First, gather a set of channels, review them, select first videos you like. This will be faster. Read, think, maybe 'last of the channel' - who wrote in last 30 days, put all in one file."

#### Workflow Steps for Vilhelm:

**1. YouTube Channel Research**
- Use research prompts
- Find channels related to assigned topics
- Gather list of potential videos (last 30 days)
- Select 3-4 videos to process

**2. Video Transcription**
- Use Google Studio for transcription
- Save transcription data
- Process with AI tools

**3. Entity Integration**
- Parse video content
- Extract: Milestones, Tasks, Steps
- Tag entities properly
- Integrate into ENTITIES system

**4. Documentation**
- Create ONE task called "Deep Research"
- Check Online Academy for Deep Research content
- If inadequate, add to New Academy/New Lessons folder
- Monday task: Upload content

#### Tasks:

| ID | Task | Entities | Assignee | Priority | Status |
|----|------|----------|----------|----------|--------|
| **TSK-140** | Teach Vilhelm video parsing workflow | PMT-004, ACT-### | Kolya | CRITICAL | In Progress |
| **TSK-141** | Set up Vilhelm's VS Code with Claude Extension | TOL-###, ACT-### | Kolya | CRITICAL | In Progress |
| **TSK-142** | Configure Vilhelm's key bindings | TOL-###, ACT-### | Vilhelm | HIGH | Pending |
| **TSK-143** | Introduce Vilhelm to ENTITIES structure | OBJ-###, ACT-### | Stas | HIGH | In Progress |
| **TSK-144** | Assign Vilhelm accounts with limits | PRF-###, TOL-### | Stas | HIGH | Done |
| **TSK-145** | Vilhelm: Research YouTube channels on Google Maps scraping | PMT-051, ACT-### | Vilhelm | HIGH | In Progress |
| **TSK-146** | Vilhelm: Parse 3-4 videos by Monday | PMT-004, ACT-### | Vilhelm | HIGH | Pending |
| **TSK-147** | Vilhelm: Create "Deep Research" task | TSK-###, ACT-### | Vilhelm | MEDIUM | Pending |
| **TSK-148** | Vilhelm: Check Online Academy for Deep Research content | OBJ-###, ACT-### | Vilhelm | MEDIUM | Pending |
| **TSK-149** | Vilhelm: Integrate prompts into ENTITIES ecosystem | PMT-###, ACT-### | Vilhelm | MEDIUM | In Progress |

**Prompts:** PMT-004 (Video Transcription), PMT-051 (Research Integration), PMT-073 (Prompt Creation)

---

### PRT-016: AI Tools & Accounts Management System
**Owner:** Stas + All Departments
**Priority:** HIGH
**Status:** Operational → Enhancement

#### Current System:

**Google Sheets Tracking:**
- Location: AI tab in shared sheets
- Niko tab: Shows limits highlighted in yellow
- Fields: Account, Tool, Limit Opens (expiry date), User Assignment

**Tools Managed:**
- Claude (multiple accounts)
- Cursor Pro
- Windsurf
- Gravity
- Gemini
- GPT
- VS Code extensions
- Perplexity
- Others

#### Issues Discussed:

**Token Limits:**
- Frequent exhaustion across accounts
- Need for more accounts
- Rotation system needed
- User assignment tracking critical

**Concurrent Usage:**
- 2 users can use one account if not aggressive
- But if one user is intensive, others shouldn't log in
- Need 1-2 hour session tracking
- "Toilet occupied" analogy - show who's logged in

**Current Update Frequency:**
- Stas: Updates 2x per hour
- Kolya: Updates 2x per hour
- Vilhelm: Joining
- Total: 4+ people, 4+ changes per hour
- Risk of conflicts/overwrites

#### Integration Plans:

**Dashboard Integration (v2-v3):**
- Add user assignment field (like Tools catalog)
- Show who's currently logged in
- Track session times
- Integrate with LibDev catalog
- Sync Tools library from Dropbox to libdev.com microservice

**Proposed Features:**
- User assignment naподобие (similar to) current table format
- Real-time login status
- Token usage tracking
- Automatic rotation suggestions
- Limit expiry alerts

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-150** | Document current AI tools tracking system | ACT-023, OBJ-### | AID | MEDIUM |
| **TSK-151** | Add user assignment field to accounts | PRF-###, ACT-### | DEV | HIGH |
| **TSK-152** | Implement login session tracking | TOL-###, ACT-### | DEV | HIGH |
| **TSK-153** | Create token usage alerts | ACT-###, OBJ-### | DEV | MEDIUM |
| **TSK-154** | Purchase additional AI tool accounts | TOL-###, ACT-### | Management | HIGH |
| **TSK-155** | Sync Dropbox Tools to libdev.com | TOL-###, ACT-### | DEV | HIGH (Due: Tuesday) |
| **TSK-156** | Build account rotation recommendations | ACT-###, OBJ-### | AID | LOW |

**Prompts:** PMT-060 (Integration), PMT-066 (Automation)

---

### PRT-017: Task Manager Dashboard (Single Task View)
**Owner:** Vilhelm + DEV Team
**Priority:** MEDIUM
**Status:** Concept → Planning

#### Context:
- Originally planned: Full task manager dashboard for all tasks
- Revised: Start with single task view (more realistic for weekend)
- Focus: Create web page for ONE task, ONE employee

#### Concept:

**Single Task Page Display:**
- Employee name
- Task details
- Steps breakdown
- Related entities
- Progress tracking

**Data Source:**
- ENTITIES/TASK_MANAGERS/
- Research folder
- Video transcription results

#### Workflow:

**1. Research Phase:**
- Topic selection
- Find videos/channels
- Use research prompts (PMT-051, etc.)

**2. Task Selection:**
- Choose one task: "Deep Research"
- Focus on narrow, clear theme
- Gather resources (Online Academy, Assets folder)

**3. Page Generation:**
- Take data and generate prompt for page creation
- Run through AI tools
- Extract tools from LIBRARIES
- Create HTML page output

**4. Testing:**
- One employee, one task test
- Validate workflow
- Improve process
- Then delegate to deep research designer

#### Tasks:

| ID | Task | Entities | Assignee | Priority |
|----|------|----------|----------|----------|
| **TSK-157** | Design single task page layout | ACT-###, OBJ-### | Vilhelm + DGN | MEDIUM |
| **TSK-158** | Create prompt for task page generation | PMT-###, ACT-### | Vilhelm | MEDIUM |
| **TSK-159** | Build HTML template for single task | TOL-###, ACT-### | Vilhelm | MEDIUM |
| **TSK-160** | Test with Deep Research task | TSK-###, ACT-### | Vilhelm | MEDIUM |
| **TSK-161** | Create research queue/line system | OBJ-###, ACT-### | AID + DEV | LOW |
| **TSK-162** | Integrate with TASK_MANAGERS data | OBJ-###, ACT-### | DEV | LOW |

**Prompts:** PMT-036 (Dev), PMT-061 (Task Manager), PMT-066 (Automation)

---

## 3. CONTENT ENTITY CREATION 📚

### New Entity: CONTENT
**Purpose:** Store and structure tutorials and guides
**Status:** Proposed

#### Context from Meeting:
> "Create Content Entity - Store and Structure Tutorials and Guides"

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-163** | Create CONTENT entity folder | OBJ-012 (Directory) | AID | HIGH |
| **TSK-164** | Define CONTENT entity taxonomy | ACT-###, OBJ-### | AID | HIGH |
| **TSK-165** | Create Master CSV for CONTENT | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-166** | Populate with existing tutorials | ACT-###, OBJ-### | AID + All | MEDIUM |

**Prompts:** PMT-016 (Taxonomy Creation), PMT-028 (Folder Organization)

---

## 4. VIDEO PROCESSING & RESEARCH 🎥

### Designers: Find Videos with Figma AI Tutorials
**Owner:** Design Team
**Priority:** HIGH

#### Requirements:
- Build video catalog app with YouTube links
- Check if timing in video can be clickable to restart YouTube frame from that time
- Goal: Minimum list of videos to parse

#### Tasks:

| ID | Task | Entities | Assignee | Priority |
|----|------|----------|----------|----------|
| **TSK-167** | Research Figma AI tutorial videos | PMT-051, ACT-### | DGN | HIGH |
| **TSK-168** | Build video catalog app | TOL-###, ACT-### | DEV + DGN | MEDIUM |
| **TSK-169** | Implement clickable timestamps | TOL-###, ACT-### | DEV | LOW |
| **TSK-170** | Create minimum parse list | OBJ-###, ACT-### | DGN | HIGH |

---

### Video Processing Taxonomy Upgrade
**Status:** Proposed

> "Video Processing Taxonomy upgrade"

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-171** | Review current video processing taxonomy | PMT-004-013, OBJ-### | AID + VID | MEDIUM |
| **TSK-172** | Identify taxonomy improvements | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-173** | Implement taxonomy upgrades | PMT-###, ACT-### | AID | LOW |

**Prompts:** PMT-004-013 (Video Processing), PMT-014-020 (Taxonomy)

---

### Video Editors: Storage Management
**Status:** TODO

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-174** | Document video editor processed works | ACT-023, OBJ-### | VID | MEDIUM |
| **TSK-175** | Define Google Drive storage locations | OBJ-###, ACT-### | VID | MEDIUM |

---

## 5. GRAVITY RESEARCH 🔬

### Task: Integrate Responsibilities into LBS Taxonomy
**Path:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities`
**Goal:** Integrate into LBS taxonomy and documentation

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-176** | Research Gravity AI tool capabilities | PMT-051, TOL-### | AID | MEDIUM |
| **TSK-177** | Integrate Responsibilities into LBS taxonomy | RSP-###, OBJ-### | AID | MEDIUM |
| **TSK-178** | Document Gravity integration | ACT-023, OBJ-028 | AID | LOW |

---

## 6. SMM DEPARTMENT PREPARATIONS 📱

### Sort Out Data for SMM Department
**Owner:** SMM + HRM
**Priority:** MEDIUM

#### Components:

**1. Shifts Management Preparations Across All Departments**
- Cross-department scheduling
- Workload distribution

**2. Schedules Management Techniques**
- Time management systems
- Employee availability tracking

**3. Connect Postings Based on Researches**
- Research-driven content
- Scheduled posting system

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-179** | Prepare shifts management system | PRF-###, ACT-### | HRM + SMM | MEDIUM |
| **TSK-180** | Document schedule management techniques | ACT-###, OBJ-### | HRM | MEDIUM |
| **TSK-181** | Connect research to posting schedule | OBJ-###, ACT-### | SMM + AID | MEDIUM |

---

## 7. BUSINESSES ENTITY CREATION 🏢

### Create Entity: BUSINESSES
**Path:** `Dropbox\ENTITIES\BUSINESSES`
**Owner:** Sales + AID
**Priority:** HIGH

#### Components:

**Sales Interviews with CLIENTS**
- Clients scheduled by Fridays
- Interview documentation
- Portfolio review process

**Context from Meeting (Translated):**
> "Yesterday whole day in interviews. About 13+ people. From them, selected some who go today on contract to CRM. They should have signed contract before going to interview."

> "Passed them to Nastya today. Nastya will explain in 15 minutes what happens with interviews."

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-182** | Create BUSINESSES entity folder | OBJ-012 (Directory) | AID | HIGH |
| **TSK-183** | Define BUSINESSES entity taxonomy | ACT-###, OBJ-### | AID | HIGH |
| **TSK-184** | Document client interview process | ACT-023, OBJ-### | HRM + SLS | HIGH |
| **TSK-185** | Track Friday client scheduling | OBJ-###, ACT-### | SLS | MEDIUM |
| **TSK-186** | Store interview recordings/notes | OBJ-###, ACT-### | HRM | MEDIUM |

---

## 8. PROFESSION PERSONAL ASSISTANTS 🤖

### Create Profession Personal Assistants
**Owner:** AID + All Departments
**Priority:** MEDIUM
**Status:** Concept

#### Concept:
- Personal AI assistants per profession
- Populated with tutorials and guidelines
- Role-specific knowledge bases

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-187** | Define profession categories | PRF-###, ACT-### | AID + HRM | MEDIUM |
| **TSK-188** | Populate tutorials per profession | OBJ-###, ACT-### | AID + All | MEDIUM |
| **TSK-189** | Create guidelines per profession | ACT-023, OBJ-### | AID + All | MEDIUM |
| **TSK-190** | Build AI assistant framework | TOL-###, ACT-### | DEV + AID | LOW |

---

## 9. INNER CLIENT SYSTEM 💼

### Add InnerClient: Any Employee
**Owner:** Management + HRM
**Priority:** LOW
**Status:** Concept

#### Description:
> "Do It Yourself Library or Hire An Employee for that specific task or per hour packages"

#### Concept:
- Internal marketplace
- DIY library access vs. hiring help
- Per-hour packages
- Buttons/interface
- Content split by profession profiles
- Human-curated AI work review
- Fast delivery guarantee

#### Example:
> "You pay X per hour, and can talk with any Human Curated Employee that reviews AI work and makes sure of fast delivery"

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-191** | Design InnerClient concept | ACT-###, OBJ-### | Management + HRM | LOW |
| **TSK-192** | Define pricing per profession | PRF-###, ACT-### | FNC + HRM | LOW |
| **TSK-193** | Create UI for InnerClient system | TOL-###, ACT-### | DEV + DGN | LOW |
| **TSK-194** | Set up human curation process | PRF-###, ACT-### | HRM | LOW |

---

## 10. DEVELOPERS PROJECT: Sync Data 🔄

### DevS Project: Sync Dropbox Tools to libdev.com
**Owner:** DEV Team
**Priority:** HIGH
**Due Date:** Tuesday

#### Components:

**1. Data Sync**
- Sync Tools library from Dropbox to libdev.com microservice
- Automate sync vs. manual updates
- Explore Dropbox API for synchronization

**2. Knowledge Gaps Focus**
- Always focus on identifying knowledge gaps
- General reminder to all employees: Read, Write, Save

#### Discussion Points:
> "Ideally, work out Dropbox synchronization with libdev library, not manual updating weekly. But try first, see what happens. If doesn't work out, this person who went on vacation for a week - if they return, here's a project for them. They said they're full-stack, so go ahead."

#### Tasks:

| ID | Task | Entities | Department | Priority | Due |
|----|------|----------|------------|----------|-----|
| **TSK-195** | Sync Dropbox Tools library to libdev.com | TOL-###, ACT-### | DEV | HIGH | Tuesday |
| **TSK-196** | Research Dropbox API synchronization | TOL-###, ACT-### | DEV | MEDIUM | This week |
| **TSK-197** | Build manual sync script (fallback) | TOL-###, ACT-### | DEV | MEDIUM | This week |
| **TSK-198** | Create knowledge gap identification process | ACT-###, OBJ-### | AID | MEDIUM | Ongoing |
| **TSK-199** | Implement Read/Write/Save reminder system | ACT-###, OBJ-### | AID | LOW | Next week |

**Prompts:** PMT-060 (Integration), PMT-066 (Automation), PMT-036 (Dev)

---

## 11. MONDAY PLANNING SESSION 📅

### Monday Call Details
**Time:** 9:00 AM
**Link:** https://meet.google.com/eqv-opgy-fff?authuser=0&hs=122&ijlm=1763740665475

### Monday Agenda:

**1. Dashboard Launch (Kolya)**
- Publish v1.0
- Share access
- Begin documentation
- Plan v2 features

**2. Vilhelm + Yulya: Designer Work Collection**
- Sit together and collect designer works
- Instruction from management:
  > "Now in Dropbox they save all their works, all screenshots of everything they do. They're showing old stuff made before working for us. Where's the work they're doing NOW? We can't find portfolios, but when you enter employee folder, you should see work they did - 3, 4, 5 per day minimum."

**3. End of Day Monday:**
- Log all documentation on completed stage
- Create plans for next stage considering today's discussion

#### Tasks:

| ID | Task | Entities | Assignee | Priority |
|----|------|----------|----------|----------|
| **TSK-200** | Monday call at 9 AM | ACT-###, PRF-### | All mentioned | CRITICAL |
| **TSK-201** | Vilhelm + Yulya: Collect designer works | PRF-###, OBJ-### | Vilhelm + Yulya | CRITICAL |
| **TSK-202** | Implement designer work storage in Dropbox | OBJ-###, ACT-### | DGN + HRM | HIGH |
| **TSK-203** | Document Monday progress | ACT-023, OBJ-028 | All | HIGH |
| **TSK-204** | Create plans for next stage | MLT-###, ACT-### | All | HIGH |

---

## 12. KEY INSTRUCTIONS & METHODOLOGIES 📖

### VS Code Key Bindings Setup

**Instruction to all:**
> "Release instruction to everyone: stuff custom shortcuts into VS Code and Cursor everywhere. Control+1 can paste Prompt 1, Control+2 = custom instruction, Control+3 = another template. You can have prepared templates behind one button press."

**Assignee:** Rekovald (from previous day's notes)
**Location:** [Key_Biddings_VS_code.md](D:\2025\Notes\Nov25\Notes\W3\221125\Key_Biddings_VS_code.md)

---

### Work Environment Changes

> "We need to change people's Work Environment somehow. Since VS Code it's been many years."

**Context:**
- Multiple AI tools now available
- Need for better integration
- Local AI tools for employees
- Cursor, Windsurf, Claude, Gravity, etc.

---

### Prompt Integration Workflow

**Key Instruction:**
> "Build me a prompt to integrate my own prompts into the Entities prompts ecosystem"

**Process:**
1. Always ask AI to create prompt first, not execute task
2. Store reusable prompts in ENTITIES/PROMPTS/
3. Cross-reference with existing prompt ecosystem
4. Use Copy Path (right-click) in VS Code
5. Two AI chats should run constantly
6. Enable "Plan Mode" (Shift+Tab 6 times) for approval workflow

---

### Multi-Agent Workflow Philosophy

> "You should have two running constantly. If needed, third one - Gravity on the right. This allows multiple accounts for development."

**Tools Setup:**
- **Left:** VS Code file system
- **Center:** Main AI chat (Cursor/Claude)
- **Right:** Secondary AI (Windsurf/Gravity)
- **Context:** Always point to ENTITIES folder

---

### Documentation at Every Stage

**Critical Feedback:**
> "You should come at 20%, 40%, 60% stages, not at the end when everything needs redoing! At each stage:
> - Do lots of research
> - Run research in 3-4-5 AI systems
> - Have a research plan
> - Document each stage
> - Gather world knowledge on the topic
> - Create guidelines for your direction"

**Application:** All new projects must follow this incremental documentation approach

---

### Research Methodology

**Deep Research Process:**
1. Topic selection with AI-generated prompt
2. Use Perplexity, Gemini, GPT, or Deep City
3. Manual approval mode (not auto-approve)
4. Multiple chats running in parallel
5. Compare results across AI systems
6. YouTube Premium (admin account) for video review

**Result Storage:**
- All found videos saved in queue
- Multi-queue line system
- Accumulated research accessible to all

---

### Daily Video Processing Goal

> "At least one video per day each person needs to parse, just to maintain fitness. Otherwise the system runs empty, spinning the same things. The system doesn't evolve."

**Mandatory:**
- 1 video per day per employee
- Transcription required
- Integration into ENTITIES required
- Knowledge gap filling priority

---

## 13. INTERVIEW NOTES: DESIGNER ISSUES 👨‍🎨

### Context: Client Interviews on Friday

**Findings (Translated):**

> "Yesterday whole day interviewing. About 13+ people. They all showed old works from before joining us. Almost nothing from current work. Very similar portfolios - everyone showing same 'goat' character. One made images, another made videos, but same character. Client says 'Oh I think I saw this already.'"

**Conclusion:**
> "Need to diversify portfolios. Main goal: Create as many case studies as possible for available people to increase chance client selects them. We don't need to chase promoting specific company themes, but rather build portfolios for these people."

**Problem:**
- Designers: Anastasiya Bykova - poor work examples, no AI works
- Daniel - (mentioned, no details)

**Solution Required:**
- Store ALL works in Dropbox employee folders
- Minimum 3-4-5 works per day visible
- Current work, not old pre-employment portfolio
- Screenshot everything created
- Build diverse case studies

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-205** | Review all designer portfolios | PRF-###, OBJ-### | HRM + DGN | CRITICAL |
| **TSK-206** | Mandate Dropbox work storage for designers | OBJ-###, ACT-### | DGN + HRM | CRITICAL |
| **TSK-207** | Create daily work documentation requirement | ACT-###, OBJ-### | HRM | HIGH |
| **TSK-208** | Diversify designer portfolios | ACT-###, OBJ-### | DGN | HIGH |
| **TSK-209** | Build case studies library | OBJ-###, ACT-### | DGN | HIGH |
| **TSK-210** | Train designers on AI tools | TOL-###, ACT-### | AID + DGN | MEDIUM |

---

## 14. ARCHITECTURE & MODIFICATIONS 🏗️

### Financial Framework
**Status:** Proposed
**Target:** Fin Dec 25

#### Components:

**Data Sets & Wiki:**
- Calculated data
- Sources documentation
- Take initial structure from Talents DB

**Public to Talents:**
- Collect profiles of employees in Talents folder
- Modified profiles for public view

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-211** | Design financial framework structure | OBJ-###, ACT-### | FNC + AID | MEDIUM |
| **TSK-212** | Create data sets for financial wiki | OBJ-###, ACT-### | FNC | MEDIUM |
| **TSK-213** | Document calculation sources | ACT-023, OBJ-### | FNC | MEDIUM |
| **TSK-214** | Collect employee profiles for Talents | PRF-###, ACT-### | HRM | MEDIUM |
| **TSK-215** | Create modified public profiles | PRF-###, ACT-### | HRM | LOW |

**Location:** `Dropbox\Nov25\Fin Nov25\Public`

---

### WindSurf Research & Methodology
**Status:** Researched
**Tool:** WindSurf (WS)

#### Instructions Given (Translated):

> "You can use the task managers folder inside entities, and maybe learn the taxonomy inside entities taxonomy task manager taxonomy. To match proper log files, rather than full documents storing, so we want short scenarios, easy tracking, easy following distribution system engine distribution engine for the among the employees inside no 25 folder and entities data source."

**Key Points:**
- Use TASK_MANAGERS folder in ENTITIES
- Learn taxonomy in ENTITIES/TAXONOMY/TASK_MANAGER_TAXONOMY
- Match proper log files (not full documents)
- Short scenarios preferred
- Easy tracking & following
- Distribution system for employees
- Source: Nov25 folder and ENTITIES data

> "While using templates from task manager for the heavy step-by-step. Here are here. And sorted data population processes as well as updating libraries. So it is kind of multi-agent flow."

**Multi-Agent Flow:**
- Researchers assigned across all departments
- Identify data gaps per department
- Break down into task quantities
- Assess information availability
- Research needs determination
- Send employees on research processes

> "I think we need to put logs inside every folder, at least in each entity folder. Let's put it inside the main researchers' log. We will be working with the employees that are in available or work status."

**Logging Strategy:**
- Logs in every folder
- At minimum: Each entity folder
- Main researchers' log
- Work with employees in "available" or "work" status

**Employee List:**
- Location: `Dropbox\Nov25\Fin Nov25\Public`
- Finance folder with employee list

> "No, the assignment will be manually, so we will need a lot of guidelines or structured guidelines and step-by-step documentation. No technical approach for now. No Python, no database, just Markdown listings."

**Methodology:**
- Manual assignment (no automation yet)
- Lots of structured guidelines needed
- Step-by-step documentation required
- **No technical approach for now**
- **No Python**
- **No database**
- **Just Markdown listings**

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-216** | Implement log files in every entity folder | OBJ-###, ACT-### | AID | HIGH |
| **TSK-217** | Create main researchers' log | OBJ-###, ACT-### | AID | HIGH |
| **TSK-218** | Build structured guidelines for manual assignment | ACT-023, OBJ-### | AID | HIGH |
| **TSK-219** | Create step-by-step documentation templates | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-220** | Identify department data gaps | ACT-###, OBJ-### | AID + All | HIGH |

---

## 15. FILL TODO FILE 📝

### TODO File Management
**Owner:** AID
**Priority:** MEDIUM

**Instruction (Translated):**
> "You don't distribute assignments by voice, just ask AI in the file for the next day to place tasks. For example, you have 10 videos - split between your employees, assign 2 each. Write 'TODO Kolya...'"

**Process:**
1. AI generates task distribution
2. Split work evenly among employees
3. Write in TODO file format
4. Each employee gets clear assignment

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-221** | Create TODO file system | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-222** | Build AI prompt for task distribution | PMT-###, ACT-### | AID | MEDIUM |
| **TSK-223** | Implement daily TODO generation | ACT-###, OBJ-### | AID | MEDIUM |

**Prompts:** PMT-073 (Prompt Creation), PMT-061 (Task Distribution)

---

## 16. TRANSCRIPT PROCESSING INSIGHTS 💡

### Current Issues with Dictation/Voice

**Problem Identified:**
> "My system completely failed with dictation recognition. For injections of these updates - types task manager and libraries."

**What Works:**
- Video transcriptions (structured information)
- Quality content parsing

**What Doesn't Work:**
- Dictated raw conversations
- Unstructured voice notes
- Meeting recordings without preparation

**Solutions Implemented:**
- Google Studio for video transcription
- Whisper flow for audio processing
- Structured parsing after transcription

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-224** | Document transcription best practices | ACT-023, OBJ-### | AID + VID | MEDIUM |
| **TSK-225** | Improve dictation-to-entity workflow | ACT-###, OBJ-### | AID | MEDIUM |

---

## 17. REPORTS SYSTEM 📊

### Daily Reports Generation
**Status:** Operational (Issues noted)

**Current Process:**
- Reports generated for Nov 20
- Location: `ENTITIES/REPORTS/`
- Import data prepared
- Create reports for system injections

**Issues:**
> "Sometimes saves in unpredictable places still."

**Success:**
> "Updated prompts by departments. Reports for 20th are viewable in entity reports, then by date, then department folders."

**New Feature:**
- Master report created from all November docs
- Located in ENTITIES/REPORTS/
- Surprisingly good quality

**Dashboard Features:**
- Project status separation
- Availability included in analytics
- Discord records presence
- Exclamation marks for attention needed (yellow card)
- Shows users with 8 hours + Discord + no records = flag for attention

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-226** | Fix unpredictable save locations | ACT-###, OBJ-### | AID | HIGH |
| **TSK-227** | Standardize report storage paths | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-228** | Document report generation process | ACT-023, OBJ-### | AID | MEDIUM |

**Location:** `ENTITIES/REPORTS/[Date]/Departments/`
**Prompts:** PMT-032-043 (Department Reports)

---

## 18. ASSET CREATION & DOCUMENTATION 📦

### HR Dashboard Asset Documentation

**Instruction:**
> "In assets, create documentation for it (dashboard). Create it as separate asset. Name it `attendance_dashboard`. Make README in it with description, all links, etc."

**Required Links:**
- Source code folder link
- Versions tracking
- v1.0 designation
- Future: Log design & developer updates

#### Tasks:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-229** | Create attendance_dashboard asset | OBJ-###, ACT-### | DEV + HRM | HIGH |
| **TSK-230** | Write README with all links | ACT-023, OBJ-### | DEV | HIGH |
| **TSK-231** | Set up version tracking | OBJ-###, ACT-### | DEV | MEDIUM |
| **TSK-232** | Document design updates log | ACT-###, OBJ-### | DGN | MEDIUM |

---

## 19. PHILOSOPHY & MOTIVATION 💪

### Key Quotes from Sessions:

**On Consistency:**
> "All our developments, everything we invested so much time in, can now come alive! Every day such progress, such big steps!"

**On Evolution:**
> "System doesn't evolve if we don't parse new content daily. We need fitness, not running empty."

**On Persistence:**
> "You're persistent, long-term oriented. Sometimes you drift, of course. I do too. But these old denials, resistances... I hear it myself. Enough already! How much longer? Just stop working already! But then it starts again. And you commit and begin."

**On False Rewards:**
> "When you give in to those persuasions and say 'okay I allow you 30 more minutes on phone' - all the advantages and enjoyment you imagined give opposite effect."

**On Systems:**
> "Now is the era of personal assistants. Real such possibilities. Not a chatterbox. How much of your conversations actually become action? Every day you're working..."

**On Hiring:**
> "What a big difference when you hire someone skilled in work vs. newbie you need to improve and teach everything."

**On Process:**
> "If we change methodology, you'll start moving manually like you were doing it yourself, then Vilhelm will understand basic principle. At least for first two steps - like when starting bicycle, someone holds it at first."

---

## 20. EXECUTION PRIORITY MATRIX

| Priority | Task IDs | Departments | Timeline | Notes |
|----------|----------|-------------|----------|-------|
| **CRITICAL** | TSK-106-115, 128-129, 140-141, 200-202, 205-207 | LGN, DEV, HRM, DGN, All | 24-48hrs | Google scraping, dashboard launch, Vilhelm training, Monday deliverables, designer issues |
| **HIGH** | TSK-116-122, 130-133, 142-149, 155, 182-186, 195, 203-204, 216-220 | All Depts | 1 week | System documentation, features, onboarding, entity creation, sync projects |
| **MEDIUM** | TSK-150-154, 157-166, 167-181, 187-199, 208-215, 221-232 | All Depts | 2 weeks | Enhancements, cataloging, SMM prep, concepts, documentation |
| **LOW** | TSK-156, 169, 173, 178, 190-194, 215 | AID, DEV, HRM | 3+ weeks | Nice-to-have features, long-term concepts |

---

## 21. SUMMARY STATISTICS 📈

**File Characteristics:**
- **Type:** Audio/Video transcriptions (Russian)
- **Sessions:** Multiple (estimated 5-7 conversations)
- **Duration:** Full working day(s)
- **Participants:** 10+ employees identified

**Entities Extracted:**
- **Projects (PRT):** 17 (PRT-011 to PRT-017, plus previous)
- **Milestones (MLT):** 39 (MLT-029 to MLT-039, plus subsets)
- **Tasks (TSK):** 232 (TSK-106 to TSK-232, 127 new tasks)
- **Profiles (PRF):** 10+ employees identified
- **External Links:** 2 (GitHub, Google Meet)

**Departments Involved:** ALL (LGN, DEV, HRM, DGN, VID, AID, SMM, SLS, FNC)

**Tools Discussed:**
- Claude Code, Cursor, Windsurf, Gravity
- Gemini, GPT, Perplexity, Deep City
- VS Code, Google Studio, Whisper
- Vercel, GitHub, Google Sheets, Dropbox

**Key Systems:**
- Google Maps Scraping
- Reviews Analysis
- HR Dashboard
- Video Processing
- AI Tools Management

**Priority Breakdown:**
- CRITICAL: 15 tasks
- HIGH: 40+ tasks
- MEDIUM: 50+ tasks
- LOW: 10+ tasks

---

## 22. VALIDATION CHECKLIST ✔️

Before execution:
- [ ] All employee profiles created (PRF-###)
- [ ] Google Maps scraping methodology documented
- [ ] HR Dashboard deployed to Vercel
- [ ] Vilhelm onboarding completed by Monday
- [ ] Designer work storage enforced
- [ ] Monday 9 AM call scheduled
- [ ] Account limits tracked in Google Sheets
- [ ] Video processing daily quota established (1/day/person)
- [ ] Entity folders created (Job Sites, Content, Businesses)
- [ ] Research methodology documented
- [ ] LibDev sync scheduled for Tuesday
- [ ] All GitHub/Vercel links accessible
- [ ] Prompts integrated into ENTITIES ecosystem

---

## 23. IMMEDIATE NEXT ACTIONS (Pre-Monday) ⚡

**For Stas:**
1. Finalize Google Maps scraping documentation
2. Prepare search queries file from Google Drive
3. Review Kolya's dashboard before deployment
4. Prepare Monday meeting agenda

**For Kolya:**
1. Complete HR Dashboard v1.0
2. Deploy to Vercel
3. Create README with links
4. Prepare v2 feature list
5. Set up LibDev sync for Tuesday

**For Vilhelm:**
1. Complete VS Code setup
2. Research 3-4 Google Maps scraping videos
3. Begin first video parsing
4. Integrate prompts into ENTITIES
5. Prepare for Monday training session

**For Yulya:**
1. Prepare to collect designer works on Monday
2. Review Dropbox storage requirements

**For Design Team:**
1. Prepare portfolio review
2. Begin storing ALL works in Dropbox
3. Daily work documentation (3-5 pieces minimum)
4. Diversify case studies

**For HRM (Nastya):**
1. Prepare client interview documentation
2. Friday scheduling system
3. Employee work monitoring process
4. Contract preparation for new hires

---

## FILE METADATA

**Original:** [211225.md](D:\2025\Notes\Nov25\Notes\W3\211225\211225.md)
**Processed:** 211225_PROCESSED.md
**Processor:** MAIN_PROMPT_v6 (PMT-073)
**Date:** 2025-11-24
**Session Type:** Full Day Working Sessions (Multiple Conversations)
**Primary Language:** Russian (Transcribed Audio/Video)
**Content Type:** Mixed (Technical Discussions, Training, Planning, Architecture)
**Participants:** 10+ employees across all departments
**Entities Extracted:** 17 PRT, 39 MLT, 127 TSK, 10+ PRF
**Key Focus:** Google Scraping, HR Dashboard, Vilhelm Onboarding, Video Processing
**Critical Deadline:** Monday 9 AM call
**Status:** Ready for department distribution and immediate action

---

**END OF PROCESSED FILE**

---

## TRANSLATION NOTES 📝

This document contains transcriptions of Russian-language working sessions. Key phrases and instructions have been translated to English while maintaining technical accuracy. Some colloquial expressions and context-dependent phrases may have cultural nuances not fully captured in translation. Where critical, original Russian context is noted.

