# 201125 - Next Day Tasks + Interviews (Processed via PMT-073)
**Date:** 2025-11-20 | **Type:** Mixed (Tasks + Interview Transcriptions) | **Processor:** MAIN_PROMPT_v6
**Content:** Next Day Planning + 2 Interview Sessions + Candidate Evaluations
**Status:** Entity-Tagged

---

## DOCUMENT STRUCTURE 📋

This file contains three major sections:
1. **Next Day Tasks & Projects** - Strategic planning and TODO items
2. **Interview Session 1** - 4 Candidates (PPC/Marketing roles)
3. **Interview Session 2** - 3 Candidates (PPC/Marketing roles)
4. **Post-Interview Evaluation** - Candidate assessments (Russian)

---

# PART 1: NEXT DAY TASKS & PROJECTS 📝

## 1. PROJECT: RESEARCHES 🔬

### Task: Update Prompts for Departments Daily Analysis

**Tools:** Claude Code Extension in Cursor
**Status:** Files already split by department

**Requirements:**
- Create prompts for each department's daily analysis
- Reference to starting point needed
- Identify potential tasks
- Few iterations for better reports
- Create guides

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-233** | Create department-specific daily analysis prompts | PMT-033-043, ACT-### | AID | HIGH |
| **TSK-234** | Build starting point reference guides | OBJ-###, ACT-023 | AID | HIGH |
| **TSK-235** | Iterate prompts for better report quality | PMT-###, ACT-### | AID | MEDIUM |

**Prompts:** PMT-032-043 (Department Reports), PMT-073 (Prompt Creation)

---

## 2. PROJECT: TASK MANAGER DATA POPULATION 📊

### Process Tutorials and Guides in Department DropBox

**Instruction:**
> If doesn't exist, add to task list: "Find and Download in MarkDown format Google Drive Guides"

**Exports:** Process from OAY (Online Academy?)

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-236** | Process tutorials from Department DropBox | OBJ-###, ACT-### | All Depts | HIGH |
| **TSK-237** | Find and download Google Drive guides in Markdown | OBJ-###, ACT-### | All Depts | HIGH |
| **TSK-238** | Export and process from Online Academy | OBJ-###, ACT-### | AID | MEDIUM |

**Location:** Department DropBox folders

---

## 3. PROJECT: FILE SYSTEM IMPROVEMENT 🗂️

### Milestone Template: Create New Entity - REPORTS

**Template Structure:**
```
=== Template: Create New Entity ===
Milestone: Create Entity Reports
Task: Create New Folder in ENTITIES "REPORTS"
- Add Taxonomy
- Integrate IDS system
- Import few examples
- Create classification
- Update Taxonomy
```

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-239** | Create REPORTS folder in ENTITIES | OBJ-012 (Directory) | AID | HIGH |
| **TSK-240** | Add taxonomy for REPORTS entity | ACT-###, OBJ-### | AID | HIGH |
| **TSK-241** | Integrate IDS system (RPT-###) | ACT-###, OBJ-### | AID | HIGH |
| **TSK-242** | Import example reports | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-243** | Create report classification system | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-244** | Update master taxonomy | PMT-014-020, ACT-### | AID | MEDIUM |

**New Entity Type:** RPT-### (Reports)
**Prompts:** PMT-016 (Taxonomy Creation), PMT-028 (Folder Organization)

---

### Task: Add to Next Day TODO File

**Dailies: Add Folders Tasks, Plans**
- Identification of Employees

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-245** | Create Tasks folder in Dailies | OBJ-012, ACT-### | AID | MEDIUM |
| **TSK-246** | Create Plans folder in Dailies | OBJ-012, ACT-### | AID | MEDIUM |
| **TSK-247** | Add employee identification system | PRF-###, ACT-### | HRM + AID | MEDIUM |

---

## 4. WISPR FLOW RECORDINGS (Russian Transcription)

### Context (Translated):

> "Tasks from onboarding that you described in detail. Maybe even cross-reference - in Task Manager there are guides. In guides, store link to Online Academy. All links to all pages of Online Academy are inside Entities Assets. Go to Online Academy folder and there are links to courses, lessons, modules."

> "If you organize them, put IDs, apply taxonomy to it, then you can cross-reference tasks with course information. For example, you say 'Install VS Code' and there you have steps inside - log in there, click here, click download, click install, etc."

> "If this is inside Task Manager, this is necessary - it's a starting point for the system to then, reading their reports, be able to identify progress on these tasks. It will insert task with ID - such-and-such template we're doing. This will be much easier for system to determine progress than just from Whisper Flow recordings."

### Extracted Requirements:

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-248** | Cross-reference Task Manager with Online Academy | TSK-###, OBJ-### | AID | HIGH |
| **TSK-249** | Store Online Academy links in guides | OBJ-###, ACT-### | AID | HIGH |
| **TSK-250** | Add IDs to Online Academy content | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-251** | Apply taxonomy to Academy structure | PMT-014-020, ACT-### | AID | MEDIUM |
| **TSK-252** | Create detailed onboarding tasks with steps | TSK-###, STP-### | HRM + AID | HIGH |
| **TSK-253** | Build progress tracking via task IDs in reports | ACT-###, OBJ-### | AID | MEDIUM |

**Location:** `ENTITIES/ASSETS/Online_Academy/`

---

## 5. NEW PROJECT TASKS 📋

### Create New Project: Clarify Data Flow

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-254** | Create data flow clarification project | PRT-###, MLT-### | AID | HIGH |
| **TSK-255** | Run methodologies skill-up project research | PMT-051, ACT-### | AID | MEDIUM |

---

### Tutorials for Instructions in VS Code

**Instruction:** When populating data, add logs to LOG folder

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-256** | Create VS Code instruction tutorials | OBJ-###, ACT-023 | AID + DEV | MEDIUM |
| **TSK-257** | Implement logging to LOG folder during data population | OBJ-###, ACT-### | AID | MEDIUM |

**Location:** `ENTITIES/LOG/`

---

## 6. TASK MANAGER TAXONOMY 📚

### Research and Prompt Creation

**Next Steps:**
- Data Import Flows description
- Structured / unstructured data
- Type of input (Research or Video Transcription)

**ID Implementation:**
> "I would like to implement Taxonomy, let's start from Task Manager Folder and give it ID TSM-###"
> "It would be TSM-001_Project_Template"

**Relevant Info:**
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS`
- `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers`

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-258** | Implement TSM-### ID system | ACT-###, OBJ-### | AID | HIGH |
| **TSK-259** | Create TSM-001_Project_Template | TSK-###, ACT-### | AID | HIGH |
| **TSK-260** | Document data import flows | ACT-023, OBJ-### | AID | HIGH |
| **TSK-261** | Define structured vs unstructured data handling | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-262** | Create input type taxonomy (Research, Video, etc.) | ACT-###, OBJ-### | AID | MEDIUM |

**New Entity Prefix:** TSM-### (Task Manager System files)
**Prompts:** PMT-016 (Taxonomy), PMT-061 (Task Manager)

---

## 7. EMPLOYEES NEXT DAY "TODO" FILE 📝

### Generate and Publish Learning Materials

**Rules:** Always ask to generate prompt first for:
- Write content
- Generate media
- Generate posts
- Web page creation
- Posting

> "Start every conversation with request to generate a prompt for you"

**Getting Acquainted with TAXONOMY: Entities**

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-263** | Create employee TODO file system | OBJ-###, ACT-### | AID | HIGH |
| **TSK-264** | Write learning materials generation guide | ACT-023, OBJ-### | AID | MEDIUM |
| **TSK-265** | Enforce "prompt-first" rule | PMT-073, ACT-### | AID | MEDIUM |
| **TSK-266** | Create taxonomy introduction materials | PMT-014-020, OBJ-### | AID | MEDIUM |

---

### Modifying Daily Review Prompt

**Locations:**
- `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts`
- Find prompts located inside department folders in `C:\Users\Dell\Dropbox\Nov25`

> "Yes, but after we update departments prompts, find me a list where those prompts are located inside departments folders"

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-267** | Update daily review prompts | PMT-032-043, ACT-### | AID | HIGH |
| **TSK-268** | Locate all department prompts in Nov25 folders | PMT-###, OBJ-### | AID | HIGH |
| **TSK-269** | Consolidate prompts to ENTITIES/PROMPTS | PMT-###, ACT-### | AID | MEDIUM |

---

### Data Processes Prompts and Scripts

**Data Import into Task Manager**

**Question:** Create Database in AirTable, for?

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-270** | Create data import scripts | TOL-###, ACT-### | DEV + AID | MEDIUM |
| **TSK-271** | Research AirTable integration options | TOL-###, ACT-### | DEV | LOW |

**Completed:** ✅ Save sessions in `\Dropbox\ENTITIES\LOG`

---

### Task Manager Choice System

**Status:** ⚠️ Warning/Pending

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-272** | Design Task Manager choice/selection system | ACT-###, OBJ-### | AID | LOW |

---

## 8. ACCOUNTS MANAGEMENT ⚠️

### Import Accounts

**Resources:**
- **Catalog:** https://adminrhs.github.io/AdminRHS-AI-Catalog-4/
- **JSON:** `C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\AI_list.json`

**Note:** "We want 1st micro example without job accounts or LinkedIn accounts"

### Russian Discussion (Translated):

> "You can ask AI to extract from your documentation separate accounts as a microservice. Let it first take all documents, everything that exists, and make only accounts file system. Those you put in dev docs, yes."

> "Accounts thinking, yes - API, tools from Libs. But users must also connect to accounts - who we gave what to, right?"

> "Good, we can make micro-microservice that for now will work only with gmails at the moment and bind gmails to tools, and immediately integrate this into catalog, like in this GitHub, and we immediately tie front and back, and literally within two days work on only this task, finish in two days."

> "Logging on microservice needed - user login with gmail box."

> "Can this box be copied to other microservices? All this environment? She attached database."

> "Old or want new ones immediately written? Yes, as needed. That is, we're talking about now developing these verifications first at the ends."

**Plans Started:** `C:\Users\Dell\Dropbox\ENTITIES\ACCOUNTS\Plans.md`

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-273** | Import accounts to ENTITIES | OBJ-###, ACT-### | AID + DEV | HIGH |
| **TSK-274** | Create accounts microservice | TOL-###, ACT-### | DEV | HIGH (Due: 2 days) |
| **TSK-275** | Bind gmails to tools | TOL-###, ACT-### | DEV | HIGH |
| **TSK-276** | Integrate accounts into AI Catalog | TOL-###, ACT-### | DEV | HIGH |
| **TSK-277** | Build user login system with gmail | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-278** | Set up database for accounts | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-279** | Create reusable microservice template | TOL-###, ACT-### | DEV | LOW |

**Links:**
- Catalog: https://adminrhs.github.io/AdminRHS-AI-Catalog-4/
- Plans: `ENTITIES/ACCOUNTS/Plans.md`

**Prompts:** PMT-036 (Dev), PMT-066 (Automation)

---

## 9. STRATEGIC ITEMS 🎯

### Departments Folders Architecture

**Issues:**
- **************** No Departments Info ****************
- Restore data processes pipelines
- Clear guidance on files locations
  - Prompts go there
  - Reports go there
  - Have summary updating script on progress count

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-280** | Document departments folder architecture | ACT-023, OBJ-### | AID | CRITICAL |
| **TSK-281** | Restore data processes pipelines | ACT-###, OBJ-### | AID | CRITICAL |
| **TSK-282** | Create clear file location guidance | OBJ-###, ACT-023 | AID | HIGH |
| **TSK-283** | Build progress count updating script | TOL-###, ACT-### | DEV + AID | MEDIUM |

**Prompts:** PMT-028 (Folder Organization), PMT-029 (System Health)

---

### Research: Tasks Import Guide

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-284** | Create tasks import guide | ACT-023, OBJ-### | AID | HIGH |

---

### Activity 3: Add Dates

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\PLANS` - Creating New Entity

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-285** | Add dates to Activity 3 | ACT-###, OBJ-### | AID | MEDIUM |

---

### LG Data Copied to DropBox

**Status:** DONE ✅

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-286** | Verify LG data in DropBox | OBJ-###, ACT-### | LGN + AID | LOW (Verification) |

---

### Import Actions Required

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\IMPORTS`

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-287** | Process items in IMPORTS folder | OBJ-###, ACT-### | AID | HIGH |

---

## 10. MISCELLANEOUS TASKS 📌

### Create Reserved Names List

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-288** | Create list of reserved names in ENTITIES | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-289** | Create list of videos to transcribe | OBJ-###, ACT-### | VID + AID | MEDIUM |
| **TSK-290** | Put video transcriptions into people tasks | TSK-###, ACT-### | AID | MEDIUM |
| **TSK-291** | Run prompts for video search | PMT-051, ACT-### | VID + AID | MEDIUM |

---

### Buy Gemini Ultra on Admin

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-292** | Purchase Gemini Ultra on Admin account | TOL-###, ACT-### | Management | HIGH |

---

### Transcription Execution Tracking

**Instructions:**
> "Add the list of transcriptions to run. That will be 1st on the list, give it ID and plan tracking of execution with proper guides on update control of execution through maybe reports folder and then what next milestone to trigger like Data Population"

**Video Link:** https://youtu.be/z1zddVjYrUI?si=VmTJUjXoIQAZ7PC6

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-293** | Create transcription execution list with IDs | OBJ-###, ACT-### | VID + AID | HIGH |
| **TSK-294** | Build execution tracking system | ACT-###, OBJ-### | AID | HIGH |
| **TSK-295** | Create execution update guides | ACT-023, OBJ-### | AID | MEDIUM |
| **TSK-296** | Define next milestone triggers (Data Population) | MLT-###, ACT-### | AID | MEDIUM |

---

### Other Items

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-297** | Create Content Entity | OBJ-###, ACT-### | AID | HIGH |
| **TSK-298** | Create Content Department | OBJ-###, ACT-### | Management | MEDIUM |
| **TSK-299** | Integrate shifts management | PRF-###, ACT-### | HRM | MEDIUM |
| **TSK-300** | Create shortcuts lesson/post | OBJ-###, ACT-### | AID | LOW |
| **TSK-301** | Prepare list of researches for Entity: Researches | OBJ-###, ACT-### | AID | MEDIUM |
| **TSK-302** | Research YouTube videos for transcription | PMT-051, ACT-### | VID + AID | MEDIUM |
| **TSK-303** | Build automation posting | TOL-###, ACT-### | DEV + SMM | LOW |
| **TSK-304** | Train AI to build research tasks for people | PMT-073, ACT-### | AID | LOW |
| **TSK-305** | List automations to learn or integrate | TOL-###, ACT-### | AID + DEV | MEDIUM |
| **TSK-306** | Task: Search for videos (template) | TSK-###, ACT-### | VID | ONGOING |
| **TSK-307** | Hosting in Vercel (Dev account) | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-308** | Automate library update | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-309** | Canva download/integration | TOL-###, ACT-### | DGN | LOW |

---

### Decision 10: Six Must-Have Files

**Designs Documents**

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-310** | Create six must-have files list | OBJ-###, ACT-### | Management | MEDIUM |
| **TSK-311** | Design core documents | OBJ-###, ACT-023 | AID | MEDIUM |

---

### Links & Resources

**PayRoll System:** https://paycifi.com (Intermediate)

**Music References:**
- Adele - "Is It Me You're Looking For"
- Lionel Richie - "Hello"

---

# PART 2: INTERVIEW SESSION 1 🎤

**Interviewer:** Zhenya (HR Manager - had electricity issues)
**Duration:** ~1 hour
**Focus:** PPC/Marketing roles, AI tool usage, Facebook Ads, Google Ads

---

## CANDIDATES - SESSION 1

### Candidate 1: Lyawe Stanley

**Profile:**
- **Age:** Not specified
- **Education:** Bachelor's in Radio Electronics, Master's in Computer Systems and Networks
- **Experience:** 30+ years remote work (Europe, U.S., Canada)
- **Specialization:** SEO Specialist, Google Business Profile (GMB)
- **Last 5-7 years:** Pure SEO and GMP
- **PPC Experience:** NO paid advertising experience

**AI Tools Used:**
- GPT for text generation, translation, information
- Government/bureaucracy questions
- Perplexity Chat (better than GPT for information)

**Work Example Shown:**
- SEO planning documentation
- Content optimization workflows
- Site-level optimization
- Computer analysis
- FAQ optimization from Google

**Technical Skills:**
- Google Tag Manager: Yes, very well
- Event tracking: Yes
- Speed Test: Slow during screen share

**Weaknesses:**
- **No paid advertising experience** (applied for Facebook Ads Manager role!)
- Last commercial work: 3 years ago (personal projects since)
- Cannot show advertising planning

**Interviewer Assessment:**
> "Not suitable for PPC role - no advertising experience"

**Status:** ❌ REJECTED

---

### Candidate 2: Ukandu Christopher

**Profile:**
- **Education:** Psychology major (Bachelor's), Google Digital Marketing, Cisco Cybersecurity
- **Experience:** Financial and Engineering sectors
- **Skills:**
  - WordPress development
  - High-impact graphic designs
  - AI tools user

**AI Tools Used:**
- ChatGPT: Marketing, text
- Veo3 (Google): Video content creation (6-8 seconds)
- Glow: Realistic image generation, clean texture
- Midjourney
- Many more depending on task

**Advertising Experience:**

**1. Pudge Bank (Financial Institution):**
- **Role:** Created website from scratch
- **Started:** Organic growth first
- **Then:** Paid ads
- **Budget:** $1,300 for 3 months (~$433/month)
- **Goal:** Brand awareness
- **Results:**
  - LinkedIn: 4k → 35k followers (still growing)
  - Created Instagram & Twitter platforms
  - 3-month project

**2. Salvation Ministries (Religious Organization):**
- Mentioned, no details provided

**3. FAIR (Crypto):**
- Created website
- Ran campaigns
- No specific details

**Content Creation:**
- Self-rated: 95/100
- Creates videos, images, content himself
- Manages social media platforms
- Uses Adobe (Photoshop, Illustrator) - practicing, not professional
- Published across platforms
- Nice visual page design

**Shown Work:**
- Instagram posts (format issue - content truncated due to format change)
- Videos mentioned but not shown in interview

**Issues:**
- More content creator/SMM than PPC specialist
- Limited deep PPC experience
- Budget handling relatively small

**Interviewer Assessment:**
> "Can keep for future as SMM specialist, creative guy for content generation. Doubt as advertising specialist. More like content manager/SMM."

**Status:** 🔶 PRE-SALE (Keep for future SMM roles)

---

### Candidate 3: Sekret Alona

**Profile:**
- **Location:** Portugal (was in Poland)
- **Experience:** 12 years in industry, last 3 years as influencer
- **Languages:** Russian, Ukrainian, Polish (A2), Portuguese (a little), English
- **Skills:** Targeting, Facebook Business, YouTube, Digital Marketing Ads

**AI Tools Used:**
- Perplexity Chat: Text generation, translation, better than GPT

**Facebook Ads Experience:**

**1. Hotel Owners Targeting:**
- **Goal:** Promote touristic places (not popular in Ukraine)
- **Strategy:** Target hotel owners/decision makers
- **Method:** Territorial targeting to conference locations (hotel business conferences)
- **Result:** 17 interested people

**2. Petroi Mazepa (Complex name - place in Ukraine):**
- **Target:** English speakers, Russian speakers located in other countries
- **Results:** Good customer collection

**Work Shown:**
- Amazon project
- **Role:** Digital project manager
- Managed team: designers, copywriters, targetologists
- Created technical tasks
- **When:** Last year

**Weaknesses:**
- Bad English (noted by interviewers)
- Managing creatives rather than hands-on PPC
- More project management than technical PPC

**Interviewer Assessment:**
> "Managing team, not hands-on PPC. Bad English."

**Status:** ❌ REJECTED (Language barrier)

---

### Candidate 4: Mihailo (Mikhail)

**Profile:**
- **Location:** Ukraine
- **Experience:** Junior PPC specialist from beginning of 2023
- **Projects:** USA, Europe, Australia, Britain, Ukraine local businesses
- **Platforms:** Mostly Google Ads, experience with Meta, a little TikTok

**AI Tools Used:**
- Not mentioned / no experience with AI tools for work
- Tried to make "something new" but no solid experience

**Advertising Experience:**

**1. Australia Case:**
- Budget: $5,000 AUD
- Half year work (February - end of May)

**2. British E-commerce (Cosmetics):**
- Budget: $6,000
- Popular brand in Britain
- Created technical tasks for redesign

**Campaign Structure:**
- E-commerce focused
- Remarketing campaigns
- LAL (Look-Alike) campaigns
- Product-specific campaigns
- Event-based campaigns (e.g., Father's Day)

**Work Shown:**
- CV with small screenshots (had to zoom in)
- Meta campaigns screens
- Technical task pages

**Weaknesses:**
- Bad English (noted)
- Could not articulate campaign strategy clearly
- Limited AI experience

**Interviewer Assessment:**
> "Bad English. Junior level."

**Status:** ❌ REJECTED (Language + Junior level)

---

# PART 3: INTERVIEW SESSION 2 🎤

**Interviewers:** Zhenya (HR) + Nikon (Company Owner)

---

## CANDIDATES - SESSION 2

### Candidate 5: Tarasova Valeriia

**Profile:**
- **Age:** 26
- **Location:** Netherlands
- **Education:** University degree in Marketing
- **Status:** Looking for remote work (Dutch companies require D2 Dutch level)
- **Passion:** Creating videos, photos with AI

**AI Tools Used:**

**Video:**
- Veo3: Video generation
- Cling AI: Short videos
- Video editors: **VN** (preferred), **CupCut**

**Audio:**
- 11Labs: Music and voices

**Images:**
- Neurostar: Image creation
- Midjourney
- ChatGPT for prompts

**Other:**
- Planning to try H&N (Heygen?) for AI avatar

**Workflow:**
1. Describe to ChatGPT (video context, effect, text, mindset)
2. ChatGPT generates prompt
3. Iterate until final version
4. Navigate AI shields/blocks to preserve faces

**Work:**
- Helping someone with YouTube videos:
  - Video cutting/editing
  - Creating preview photos
  - Managing content

**Weaknesses:**
- No Adobe experience (After Effects, etc.)
- Doesn't save prompts (stores in ChatGPT conversations)
- Takes notes in iPhone Notes app only
- No structured documentation
- **No computer-based work experience in any company**
- Last work: 1-2 months ago (agreement)

**Questions Asked:**
- Are you familiar with Adobe After Effects? NO
- Do you save your prompts? NO (only in ChatGPT)
- Do you take structured notes? NO (iPhone notes only)
- Company work experience? NONE

**Interviewer Assessment:**
> "No company work experience. No structured approach. Creative but not professional level."

**Status:** 🔶 MAYBE (1 year agreement, 1-2 month to start)

---

### Candidate 6: Akinyi Vanessa

**Profile:**
- **Role:** PPC Specialist + Executive Assistant Support
- **Experience:** Public and private organizations, individuals
- **Strengths:**
  - Project management
  - Media buying process
  - Creating ideas
  - Meeting management
  - Time/calendar management

**AI Tools Used:**

**Primary:** **Copilot** (Microsoft)
- Research purposes
- Clean up text
- Clean up communication
- Daily automation
- Work flow automation

**Clarification:**
- **NOT** GitHub Copilot in VS Code
- Uses web version like ChatGPT
- Automation via **Zapier**

**Advertising Experience:**

**Last Job:** UDSL (Data Science company)
- **Products:** SAS products, middle ticket courses
- **When:** November (last year) to August (this year)
- **Budget:** $200-$500 daily
- **Platforms:** Mostly Meta (Instagram, Facebook), some TikTok

**Campaign Structure:**
- **Confusion** when asked about campaign organization
- Could not clearly articulate:
  - How many campaigns running simultaneously
  - Campaign grouping strategy
  - Campaign categorization
  - Strategic approach

**Media Planning Process:**
- Campaign setup
- Budget allocation
- Setting targets
- "Entire media planning process"

**Tools:**
- Adobe Photoshop: Practicing, not professional
- Adobe Illustrator: Practicing

**Weaknesses:**
- Cannot explain campaign structure clearly
- Does not save prompts
- No structured note-taking system
- "More on the go" approach
- Self-described as "junior"

**Interviewer Assessment:**
> "Cannot articulate campaign strategy. Junior level. No structured approach."

**Status:** ❌ REJECTED (Cannot explain PPC structure)

---

### Candidate 7: Pokshynskyi Bohdan

**Profile:**
- **Age:** 21
- **Location:** Lviv, Ukraine
- **Languages:** Ukrainian, Russian, Polish (a little), English (not so good)
- **Experience:** Little experience, mostly learning
- **Tools:** Google Ads, Google Analytics, Google Sheets, Some Meta ads knowledge

**AI Tools Used:**
- **Mostly for fun** (no work)
- Gemini: Integrated into his home/form?
- ChatGPT: Created texts for **email advertising**
- Used for video before interview

**Prompting:**
- "I just write what I need. That's all."
- No special prompts
- Not using prompt engineering
- Knows about it but doesn't use it

**Advertising Experience:**

**Public Organization:**
- **Budget:** $200/day
- **Strategy:** Started with "basic semantics" and watched spend
- Hard because "not so much case I have"
- Could not clearly explain organization type or strategy

**Weaknesses:**
- **Very weak English**
- **No structured approach**
- **No prompting knowledge application**
- **Cannot articulate strategy**
- **Minimal real experience**

**Interviewer Feedback:**
> "If you know how to prompt, you get better results. Like skydiving - if you know how, you land well. If not, you'll almost land but hurt yourself or waste time."

**Interviewer Assessment:**
> "Weak English. No experience. Cannot explain approach."

**Status:** ❌ REJECTED

---

## INTERVIEW REQUIREMENTS EMPHASIZED 📋

### Key Points Stressed:

**1. Screen Sharing:**
- Basic requirement
- Test internet speed
- Work essential skill

**2. Work Examples:**
- Show reports
- Ad management system access
- Excel planning sheets
- Analytics
- Anything related to work

**3. Note-Taking & Learning:**
> "Because of fast evaluation of AI and the work, we need people to take notes and know how to find information. How do you learn? How fast do you learn?"

> "It wasn't enough that I told you now the type of campaigns that exist, you already took the notes and wrote it down, and you are able to implement it tomorrow in tomorrow's work, or I will need to remind you tomorrow to do that, and you won't recall what I am talking about."

**4. Organization:**
> "That's a tough approach that we have in our company for now about being organized and being able to learn fast. Since you will be learning, and we will be paying you for the learning, we have high demand and demands to our employees."

**5. AI Tools:**
- Company uses lots of AI tools
- Need people who want to use them
- Want to know more about tools
- Not just text generation, but image generation too

**6. Work Routine:**
- CRM system with Timelake
- Log in at 9:00 AM
- Clock in/out, pause for breaks
- 3 manual screenshots per day (not automatic)
- Discord: Main communication platform
  - Online during work hours
  - Cameras usually off
  - Can mute when not speaking
  - Convenient for collaboration

**7. Prompt Saving:**
- Expected to save prompts
- Structured documentation
- Campaign planning
- Content planning
- Budget tracking
- Last campaigns run

---

# PART 4: POST-INTERVIEW EVALUATION (Russian) 🔍

### Translated Discussion:

> **On African Candidates:**
> "Africans - no. I didn't like them either. Especially this Stanley. He applied, so you understand, for Facebook Ads Manager. Honestly he says: I have no experience with Facebook Ads. I didn't understand the point at all."

> **On Ukandu:**
> "Ukandu is more or less okay. He has a cool video, at least he tried somehow. He edited. But this Ukandu, yes, we can keep him for future as SMM specialist. That is, for Pre-Sale, start putting people, we'll generally transition to Pre-Sale."

**Instruction:**
> "As soon as we compile, or let them sign Pre-Sale contracts both? No, nothing! Now almost no calls, while I'm compiling. When there are applications, you'll already have a hot list. Sometimes you'll warm them up, saying yes yes yes, looking for project for you."

> "Such hot list of who we already interviewed who can be sold, but hold them - we definitely won't yet."

> **On Ukandu:** "Better to hear - he's creative guy for content generation. As advertising specialist, I doubt. He's such content manager, SMM specialist."

> "For SMM, he could fit in principle."

**Tomorrow Interview with Client:**
> "SMM interview? No, for client. Tomorrow interview for SMM."

> "We need today's candidates there. Borovik showed me most skilled in terms of Jack-of-all from all these."

**Remembered:** "The only one who showed his cases there."
**Response:** "Yes yes yes, remembered. Recalled. Yes, good. Sign contract with him and tomorrow to interview."

**Price Discussion:**
> "Tell him starting at $20, because Dubani is fool. But over time, not English, not low."

**On Ukandu Christopher:**
> "First, can beat down price. Second, take him to interview at least. Will show us from their side. These what, start two candidates? Let's go for last ones. Good."

**On Valeriia:**
> "I didn't understand - what, two months? Well, we agreed with her because she's now in Netherlands. Combat. And this moment like distance?"

> "We agreed with her 1 year agreement, 1-2 months to start."

---

## FINAL DECISIONS 🎯

| Candidate | Status | Reason | Action |
|-----------|--------|--------|--------|
| **Lyawe Stanley** | ❌ REJECTED | No PPC experience, applied for wrong role | None |
| **Ukandu Christopher** | 🔶 PRE-SALE | Creative, good for SMM, not PPC | Add to hot list, beat down price |
| **Sekret Alona** | ❌ REJECTED | Bad English, project manager not hands-on | None |
| **Mihailo** | ❌ REJECTED | Bad English, junior level | None |
| **Tarasova Valeriia** | 🟡 MAYBE | Creative but no company experience | 1-2 month trial, 1 year agreement |
| **Akinyi Vanessa** | ❌ REJECTED | Cannot explain PPC structure, junior | None |
| **Pokshynskyi Bohdan** | ❌ REJECTED | Weak English, no real experience | None |

### Pre-Sale Hot List:
1. Ukandu Christopher (SMM/Content)
2. Possibly Valeriia (Trial basis)

### Contract Signing:
- **Borovik** (mentioned as most skilled) - Sign contract for tomorrow's client interview
- Starting rate: $20

---

## EXTRACTED TASKS FROM INTERVIEWS 📝

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-312** | Create Pre-Sale candidate tracking system | PRF-###, OBJ-### | HRM | HIGH |
| **TSK-313** | Add Ukandu Christopher to Pre-Sale list | PRF-###, ACT-### | HRM | MEDIUM |
| **TSK-314** | Sign contract with Borovik for client interview | PRF-###, ACT-### | HRM | HIGH (Tomorrow) |
| **TSK-315** | Prepare Borovik for tomorrow's client interview | PRF-###, ACT-### | HRM | HIGH (Tomorrow) |
| **TSK-316** | Create candidate warming system for hot list | ACT-###, OBJ-### | HRM | MEDIUM |
| **TSK-317** | Document interview requirements checklist | ACT-023, OBJ-### | HRM | MEDIUM |
| **TSK-318** | Create interview scoring rubric | ACT-###, OBJ-### | HRM | MEDIUM |
| **TSK-319** | Follow up with Valeriia on trial terms | PRF-###, ACT-### | HRM | MEDIUM |

---

## HIRING CRITERIA IDENTIFIED ✅

### Must-Have Skills:
1. **Strong English** - Critical requirement
2. **PPC Experience** - Actual hands-on, not just theory
3. **Campaign Structure Knowledge** - Can articulate strategy
4. **Note-Taking** - Structured documentation
5. **Prompt Saving** - Organization of AI work
6. **Screen Sharing** - Basic remote work skill
7. **Fast Learning** - Take notes, implement immediately
8. **AI Tool Usage** - Beyond basics, multiple tools
9. **Work Examples** - Can show actual work

### Red Flags:
1. ❌ "I just write what I need" (no structure)
2. ❌ Cannot explain campaign organization
3. ❌ No prompt/note saving system
4. ❌ "More on the go" approach
5. ❌ Applied for wrong role (no matching experience)
6. ❌ Cannot show work examples
7. ❌ Slow internet during screen share
8. ❌ No company work experience
9. ❌ Weak English for client-facing role

---

## SUMMARY STATISTICS 📊

**Tasks Extracted (Part 1):** 319 total (TSK-233 to TSK-319, 87 new tasks)
**Projects Identified:** Multiple (Researches, Task Manager, File System, etc.)
**Interviews Conducted:** 2 sessions, 7 candidates
**Candidates Accepted:** 0 (immediate)
**Pre-Sale Candidates:** 2 (Ukandu, possibly Valeriia)
**Tomorrow Interview:** Borovik (contract + client interview)

**File Locations Mentioned:**
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS`
- `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers`
- `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts`
- `C:\Users\Dell\Dropbox\Nov25`
- `C:\Users\Dell\Dropbox\Nov25\Fin Nov25\Public\AI_list.json`
- `C:\Users\Dell\Dropbox\ENTITIES\PLANS`
- `C:\Users\Dell\Dropbox\ENTITIES\IMPORTS`
- `C:\Users\Dell\Dropbox\ENTITIES\LOG`
- `C:\Users\Dell\Dropbox\ENTITIES\ACCOUNTS\Plans.md`

**External Links:**
- AI Catalog: https://adminrhs.github.io/AdminRHS-AI-Catalog-4/
- PayCifi: https://paycifi.com
- YouTube Video: https://youtu.be/z1zddVjYrUI?si=VmTJUjXoIQAZ7PC6

**Priority Breakdown:**
- CRITICAL: 2 tasks
- HIGH: 40+ tasks
- MEDIUM: 35+ tasks
- LOW: 10+ tasks

---

## FILE METADATA

**Original:** [201125.md](D:\2025\Notes\Nov25\Notes\W3\201125\201125.md)
**Processed:** 201125_PROCESSED.md
**Processor:** MAIN_PROMPT_v6 (PMT-073)
**Date:** 2025-11-24
**Content Type:** Multi-part (Strategic Planning + Interview Transcriptions + Evaluations)
**Languages:** English + Russian
**Interviews:** 7 candidates evaluated
**Primary Focus:** Next day planning, PPC/Marketing hiring, AI tool proficiency assessment
**Status:** Ready for HR distribution and task execution

---

**END OF PROCESSED FILE**
