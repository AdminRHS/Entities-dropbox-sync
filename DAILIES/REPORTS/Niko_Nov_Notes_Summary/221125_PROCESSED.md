# 221125 - Strategic Planning Session (Processed via PMT-073)
**Date:** 2025-11-22 | **Employee:** Niko Kar | **Processor:** MAIN_PROMPT_v6 | **Status:** Entity-Tagged

---

## 1. EMPLOYEE CONTEXT 👤

**Employee:** Niko Kar
**Discord ID:** [To be filled]
**Department:** AID (AI & Automation)
**Role:** System Architect / Automation Lead
**Profile Entity:** PRF-### (to be assigned)

---

## 2. ACTIVE RESEARCH PROCESSES 🔬

### Current Workflow Structure
```
PLANS → ToDo → REPORTS
    ↓
RESEARCHES → LOGS
```

**Active Location:** `Dropbox\ENTITIES\PLANS\Research_System_Activation`

**Entities Involved:**
- **MLT-###**: Research activation milestones
- **TST-###**: Todo task assignments
- **OBJ-028**: Reports objects
- **OBJ-###**: Log storage

---

## 3. PRIORITY PROJECTS & MILESTONES 🎯

### PRT-004: Single Sign-In Distribution System
**Owner:** AID + DEV
**Priority:** HIGH
**Timeline:** Start next day

**Requirements:**
- Build distribution center folder
- Log information distribution
- Files inside employee folders
- Integration with authentication (TOL-### - Auth systems)

**Milestones:**
- **MLT-019**: Design distribution architecture
- **MLT-020**: Implement logging system
- **MLT-021**: Employee folder integration
- **MLT-022**: Testing & rollout

**Prompts:** PMT-066 (Automation), PMT-036 (Dev workflow)

---

## 4. DEPARTMENT TASKS BREAKDOWN 📋

### HR Department (HRM)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-030** | Interviews Lists to MD Files | OBJ-###, ACT-023 | PMT-038, PMT-053 | HIGH | Convert HR video interviews |
| **TSK-031** | Clear Lists of Candidates Sources | OBJ-###, PRF-### | PMT-053 | MEDIUM | Source tracking |
| **TSK-032** | HR Onboarding preparation | MLT-###, TST-### | PMT-038, PMT-056 | HIGH | [Google Sheet](https://docs.google.com/spreadsheets/d/1yYUD9nfHXdRfBkKUIrq_0v0hyJbKO8WpsUBPxkCYsZA/edit?gid=0#gid=0) |
| **TSK-033** | Integrate Individual Employee Testing | PMT-056, PRF-### | PMT-038 | MEDIUM | Testing system |
| **TSK-034** | Discord Bot notifications | TOL-###, ACT-### | PMT-066 | LOW | To departments |

**Notes:**
- HR video interview conversion needed
- Employee testing system integration required
- Onboarding topics preparation in progress

---

### Lead Generation (LGN)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-035** | Expand Industries | OBJ-###, ACT-### | PMT-039 | HIGH | LG Team Leads |
| **TSK-036** | LG Message Templates | PMT-###, ACT-### | PMT-039 | HIGH | Outreach templates |
| **TSK-037** | Prospects Architecture Improvement | OBJ-###, MLT-### | PMT-044 | CRITICAL | See database schema below |
| **TSK-038** | Feed database: 300 new leads daily | OBJ-###, ACT-### | PMT-039, PMT-044 | CRITICAL | Goal target |
| **TSK-039** | Populate leads with classifications | OBJ-###, ACT-### | PMT-044 | HIGH | Industries & metadata |
| **TSK-040** | Target audience analysis | PMT-044, ACT-### | PMT-051 | HIGH | Research task |
| **TSK-041** | Extract/analyze LG conversations | ACT-###, OBJ-### | PMT-051 | MEDIUM | From accounts |
| **TSK-042** | Build look-alike auditory | ACT-###, OBJ-### | PMT-044 | MEDIUM | For campaigns |
| **TSK-043** | Testing Individual Scraping Techniques | TOL-###, ACT-### | PMT-039, PMT-066 | MEDIUM | Context doc needed |
| **TSK-044** | LG Department Core Principles Doc | OBJ-028, ACT-023 | PMT-039 | HIGH | Department context |
| **TSK-045** | Obligatory: Save 5 Templates + Screenshot | OBJ-###, ACT-### | PMT-039 | CRITICAL | CRM confirmation |

**Important Locations:**
- Research: `C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES`
- Video Queue: `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-008_Video_Queue`

**VS Code Key Binding TODO:**
- Assignee: Rekovald
- File: [Key_Biddings_VS_code.md](D:\2025\Notes\Nov25\Notes\W3\221125\Key_Biddings_VS_code.md)
- Completion: OBLIGATORY
- Confirmation: Screenshot in CRM with recognition

---

### Sales Department (SLS)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-046** | Sales Email Templates | PMT-###, ACT-### | PMT-041 | HIGH | Template creation |
| **TSK-047** | Connect to Google Calendar | TOL-###, ACT-### | PMT-066, PMT-036 | HIGH | Match transcripts to events |
| **TSK-048** | Scrape Event Metadata | ACT-###, OBJ-### | PMT-066 | MEDIUM | From calendar |
| **TSK-049** | Populate Business Entity from Sales | OBJ-###, ACT-### | PMT-041, PMT-044 | HIGH | Data extraction |
| **TSK-050** | Get CRM Data on Daily LeadGen Cards | TOL-###, OBJ-### | PMT-041 | HIGH | Delegate to Kolya & Olya |

**Test Tools:**
- [Relay.app Sales Demo Qualifier](https://www.relay.app/templates/sales-demo-request-qualifier)

---

### Development Department (DEV)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-051** | Learning Flow Step-by-Step Development | MLT-###, STP-### | PMT-036 | MEDIUM | Educational flow |
| **TSK-052** | Track Task Completions via Microservices | TOL-###, ACT-### | PMT-066, PMT-036 | HIGH | Sign up to Libs, manual tool add |
| **TSK-053** | Synchronize Libs with Online Academy | TOL-###, OBJ-### | PMT-036, PMT-060 | MEDIUM | Data sync |
| **TSK-054** | Connect Task Managers to Libs | TST-###, OBJ-### | PMT-061, PMT-062 | HIGH | Sync template variations |
| **TSK-055** | Task Manager Dashboard with Database | TOL-###, OBJ-### | PMT-036 | HIGH | Data export to DB |
| **TSK-056** | n8n Image Generation Guide | TOL-###, ACT-### | PMT-066, PMT-036 | MEDIUM | Dashboard integration |
| **TSK-057** | Frontend OAuth Implementation | TOL-###, ACT-### | PMT-036 | MEDIUM | Redirect URIs, /api/auth/google |
| **TSK-058** | Personal Task Manager Web Pages | TOL-###, ACT-### | PMT-036, PMT-066 | HIGH | HTML page generation |

**Required Materials:**
- Weekly Reports Data matched with TSM
- Focus on Task Manager export to dashboard

---

### AI & Automation Department (AID)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-059** | Add Rules for AI in Each Folder | PMT-###, OBJ-### | PMT-028 | HIGH | Folder-level AI rules |
| **TSK-060** | Log Entity Integration | OBJ-###, ACT-### | PMT-029 | MEDIUM | Example-based learning |
| **TSK-061** | Keep Logs Longer | OBJ-###, ACT-### | PMT-029 | LOW | Log retention |
| **TSK-062** | Develop USER Entities | OBJ-###, ACT-008 | PMT-016 | HIGH | New entity type |
| **TSK-063** | Review TALENTS match with Database | PRF-###, OBJ-### | PMT-038, PMT-029 | MEDIUM | Talent validation |
| **TSK-064** | Prepare DB EXPORT Folder: LIBRARIES | OBJ-###, ACT-### | PMT-060, PMT-036 | HIGH | Export to libs.amyemp.com |
| **TSK-065** | Text Researches Recognition & Import | ACT-###, TOL-### | PMT-051 | MEDIUM | Import system |
| **TSK-066** | Core System Taxonomy Architecture Review | PMT-014-020, MLT-### | PMT-029 | HIGH | REPETITIVE TODO |
| **TSK-067** | Prompt for Transcription Export | PMT-004, ACT-### | PMT-073 | MEDIUM | REPETITIVE TODO |
| **TSK-068** | Prompts for Weekly Analysis | PMT-032, ACT-### | PMT-073 | MEDIUM | REPETITIVE TODO |
| **TSK-069** | Prompts for Daily Analysis | PMT-032-043, ACT-### | PMT-073 | MEDIUM | REPETITIVE TODO |
| **TSK-070** | Researches Dashboard | TOL-###, OBJ-### | PMT-036, PMT-051 | HIGH | REPETITIVE TODO |
| **TSK-071** | Export Dailies Summaries to ToDo App | OBJ-###, ACT-### | PMT-032, PMT-066 | MEDIUM | REPETITIVE TODO |
| **TSK-072** | Tasks Templates Execution System | TST-###, STP-### | PMT-061 | HIGH | Multiple tasks allowed |
| **TSK-073** | Steps Confirmation System | STP-###, ACT-### | PMT-061 | HIGH | Choose matching deliverables |

---

### Design Department (DGN)

| ID | Task | Entities | PMT | Priority | Notes |
|----|------|----------|-----|----------|-------|
| **TSK-074** | Portfolio Diversification Strategy | OBJ-###, ACT-### | PMT-035 | CRITICAL | See meeting notes |
| **TSK-075** | Create More Case Studies | OBJ-###, ACT-023 | PMT-035 | HIGH | Available designers |
| **TSK-076** | Deep Research Designer Task | PMT-051, ACT-### | PMT-035 | MEDIUM | Web page design |
| **TSK-077** | Media Library Development | OBJ-###, ACT-### | PMT-035 | MEDIUM | Asset management |

**Critical Insight from Meeting:**
> Designers showed old work from before joining. Need to diversify portfolios with case studies. Goal: Create maximum examples for available designers to increase client selection chances. Focus on building portfolios vs. promoting specific company themes.

---

## 5. STRATEGIC INITIATIVES 🏗️

### PRT-005: GitHub Entities Repository Integration
**Owner:** AID + DEV
**Priority:** HIGH
**Status:** Planning

**Milestones:**
- **MLT-023**: Separate GitHub Repositories
  - Start from Researches
  - GPT connected to GitHub
- **MLT-024**: Restructure to Match Entities Taxonomy
  - Location: `C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES`
  - Taxonomy: `C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES\TAXONOMY`
  - Tool: Cursor (TOL-###)
- **MLT-025**: Integrate Users to GitHub
  - User entity development (TSK-062)

**Prompts:** PMT-068, PMT-069 (Version control)

---

### PRT-006: ID System for Services
**Owner:** AID
**Priority:** HIGH
**Status:** Planning

**Location:** `Dropbox\ENTITIES\BUSINESSES\Services`
**Requirement:** Create Master IDS CSV File

**Entities:**
- Master CSV format (similar to existing entity masters)
- Service ID format: SRV-### (new entity type)
- Integration with BUSINESSES folder

**Prompts:** PMT-016 (Taxonomy creation), PMT-029 (Validation)

---

### PRT-007: Research Integration with Google TODO
**Status:** POSTPONED (1 week)
**Owner:** AID
**Priority:** MEDIUM

**Tasks:**
- TSK-078: Google TODO API integration
- TSK-079: Research-to-TODO sync workflow

**Prompts:** PMT-066 (Automation)

---

### PRT-008: Researches Dashboard
**Owner:** AID + DEV
**Priority:** HIGH
**Status:** Planning

**Functionality:**
- Simplified research topic picking by employees
- Update employee assignments
- Develop assignment processes
- Create folders: Projects, Tasks, Milestones, Steps
- Cross-reference system
- Image support (nice to have)

**Entities:**
- **MLT-026**: Assignment Process Development
  - Create ASSIGNMENTS entity type
  - Folder structure for Projects/Tasks/Milestones/Steps
  - Cross-referencing logic
- **MLT-027**: Dashboard UI/UX
  - Topic selection interface
  - Employee assignment tracking
  - Progress visualization

**Prompts:** PMT-036 (Dev), PMT-051 (Research Integration), PMT-066 (Automation)

---

### PRT-009: PROSPECTS → Populate Data with AI Research
**Owner:** LGN + AID
**Priority:** CRITICAL
**Status:** Architecture Phase

**Big Project Components:**
- Import folder for next CRM
- Research additional data fields
- Businesses import
- Integrate job requests as HR communication channel
- Reports architecture → Checklists (Deliverables)

**Database Schema (Existing):**

#### Prospects Tables

| Table | Key Fields | Entity Mapping |
|-------|-----------|----------------|
| **prospects** | id, name, position_id, status_id, notes, tool_id | OBJ-### (Prospect), TOL-### (Tool) |
| **prospect_companies** | id, name, website, city_id, country_id, affiliate_id, tool_id, manager_id, created_by, created_at | OBJ-### (Company), PRF-### (Manager) |
| **prospect_contacts** | prospect_id, contact_id | OBJ-### (Contact) |
| **prospect_prospect_company** | prospect_id, prospect_company_id | Relationship table |
| **prospect_company_industries** | prospect_company_id, industry_id | OBJ-### (Industry) |
| **prospect_company_sub_industries** | prospect_company_id, sub_industry_id | OBJ-### (SubIndustry) |
| **prospect_company_contacts** | prospect_company_id, contact_id | Relationship table |
| **prospect_communications** | id, prospect_id, prospect_company_id, user_id, account_id, created_at, is_followup, note | OBJ-### (Communication), PRF-### (User) |
| **prospect_communication_messages** | prospect_communication_id, message_id | OBJ-### (Message) |

**Tasks:**
- TSK-037: Prospects Architecture Improvement
- TSK-038: Feed 300 new leads daily
- TSK-039: Populate with classifications
- TSK-040: Target audience analysis
- TSK-041: Extract/analyze conversations
- TSK-042: Build look-alike auditory

**Architecture Notes:**
> Missing details and structure. Need to build and confirm architecture and schemas before extraction. Don't change source folder, just track what's copied. Classify fields for tagging client interests and metadata.

**Prompts:** PMT-039 (LG), PMT-044 (Research), PMT-051 (Integration)

---

## 6. WORKFLOW & PROCESS DEFINITIONS 🔄

### Deep Research Workflow (Multi-Queue System)
**Owner:** AID + All Departments
**Status:** Design Phase

**Workflow Steps:**
1. **Topic Selection** (Research request arrives)
   - Context + Request → Generate prompt
   - Use research prompts folder (YouTube, various topics)
   - Can use Gemini, GPT, Perplexity, or Deep City

2. **Research Execution**
   - Employee chooses research direction in Task Manager
   - Categories in Task Manager: Videos, Research, Reading, etc.
   - Freedom for employee task selection

3. **Content Parsing**
   - Parse research content
   - Break down into tasks
   - Tag: Task, Step, Project, Milestone, Prompt

4. **Quality Analysis**
   - Analyze results
   - Channel names, views, likes, publish date
   - Format: Markdown, JSON, or similar
   - Save all found videos (create queue)

5. **Video Queue Management**
   - Previous attempts: 10-15 min to select 1 from 20 videos
   - Solution: Parse all 20 that pass minimum threshold
   - Accumulate queue (Polish: "kolejka")
   - Multi-queue line system

6. **Task Completion**
   - Goal: Parse one video fully by end of work session
   - Video integrated into system
   - Process ready to delegate to others

**Prompts Chain:**
```
PMT-051 (Research Integration) → PMT-004 (Video Transcription)
→ PMT-006 (Analysis) → PMT-009 (Taxonomy Integration)
→ PMT-032 (Report) → Update Queue
```

**Online Academy Integration:**
- Link to courses with Deep Research content
- If content inadequate, add to New Academy/New Lessons folder
- Task for Monday: Upload content

**Tools:**
- TOL-###: Gemini, GPT, Perplexity, Deep City
- TOL-###: Task Manager (personal dashboard)
- Location: Assets folder for reference materials

**Employee Benefits:**
- Track personal task queue/line
- Do deep research directly in GPT
- Save tokens on context
- Ideal for employees with Dropbox sync (e.g., video editors)

---

### Gap Analysis Workflow
**Owner:** AID
**Status:** Proposed

**Process:**
1. Analyze departments' knowledge from last week reports
2. Source: `C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-21`
3. Identify knowledge gaps
4. Create targeted research tasks
5. Assign to appropriate departments

**Entities:**
- **MLT-028**: Gap Analysis Milestone
  - STP-###: Review weekly reports
  - STP-###: Identify gaps
  - STP-###: Create research tasks
  - STP-###: Assign to departments

**Prompts:** PMT-029 (System Health), PMT-032 (Report Collection), PMT-051 (Research)

---

### Milestone Naming Convention (Clarification)
**Project Example:** Black Friday

**WRONG:**
- Milestone: Black Friday Design Preparation ❌

**CORRECT:**
- Milestone: Design Preparation ✅
  - Reusable across multiple projects
  - Universal naming
  - Includes: Finding references, preparing prompts, creating documentation

**Apply to:**
- All milestone creation (MLT-###)
- Task Manager integrations
- Project templates (PRT-###)

---

## 7. INTEGRATION & SYNC SYSTEMS 🔗

### PROMPTS into TASK MANAGER Integration
**Status:** TO DO
**Owner:** AID

**Action Required:**
- Add PROMPT Field to Task Manager entities
- Link TST-### to PMT-###
- Enable prompt-driven task execution

**Tasks:**
- TSK-080: Add PROMPT field to TASK_MANAGERS schema
- TSK-081: Update all existing TST-### with relevant PMT-###
- TSK-082: Create validation for PROMPT references

**Prompts:** PMT-061 (Entity Filling), PMT-029 (Validation)

---

### LIBRARIES Export to Database
**Status:** Planning
**Owner:** AID + DEV

**Target:** libs.amyemp.com
**Entities to Export:**
- ACT-### (Actions)
- OBJ-### (Objects)
- TOL-### (Tools)
- SKL-### (Skills)
- PRF-### (Profiles)
- RSP-### (Responsibilities)

**Tasks:**
- TSK-064: Prepare DB EXPORT Folder
- TSK-083: Create export scripts
- TSK-084: Test export/import pipeline
- TSK-085: Schedule automated sync

**Prompts:** PMT-060 (Integration), PMT-066 (Automation), PMT-036 (Dev)

---

### Connect Task Managers to LIBRARIES
**Status:** High Priority
**Owner:** AID

**Goal:** Sync more possible variations of templates

**Integration Points:**
- Link TST-### to ACT-###, OBJ-###
- Link MLT-### to SKL-###
- Link STP-### to TOL-###
- Enable fuzzy matching (PMT-062)

**Tasks:**
- TSK-054: Connect Task Managers to Libs
- TSK-086: Create sync workflow
- TSK-087: Test template variations

**Prompts:** PMT-061, PMT-062 (Library Match)

---

## 8. ARCHITECTURE UPDATES 🏛️

### Architecture Priorities

| ID | Update | Priority | Owner | Status |
|----|--------|----------|-------|--------|
| **ARC-001** | Add Employees Folders Relative Path | HIGH | AID | Planning |
| **ARC-002** | Expand Employees Profiles | HIGH | HRM + AID | Planning |
| **ARC-003** | Copy All Employees Profiles into Talents | MEDIUM | HRM | Planning |
| **ARC-004** | Consider Entities v2 Architecture | LOW | AID | Research |
| **ARC-005** | Integrate Log System | MEDIUM | AID | Planning |
| **ARC-006** | Block/Fields Sub System (Similarities) | LOW | AID | Research |

---

### Entities Simplification Strategy
**Status:** Planning
**Owner:** AID

**Goal:** Maintain only Master Lists
**New Entity Type:** "Departments" Entities

**Concept:**
- Go up from LIBRARY level
- Receive full functionality entity
- Include only relevant data per department
- Reduce redundancy

**Tasks:**
- TSK-088: Design Departments Entity structure
- TSK-089: Identify data filtering rules per department
- TSK-090: Create Department-specific master lists
- TSK-091: Test with one department (pilot)

**Prompts:** PMT-014-020 (Taxonomy), PMT-028 (Reorganization)

---

### Researches Architecture Cleanup
**Status:** CRITICAL
**Owner:** AID

**Issues Identified:**
- Architecture is scattered
- Clear guidance needed on import flow
- Inconsistent structure

**Tasks:**
- TSK-092: Document current research architecture
- TSK-093: Identify scattered components
- TSK-094: Design unified import flow
- TSK-095: Create clear guidance documentation
- TSK-096: Restructure research folders

**Prompts:** PMT-029 (System Health), PMT-072 (Critical Fixes), PMT-028 (Reorganization)

---

## 9. AFFILIATION & BUSINESS ENTITIES 💼

### PRT-010: Affiliation Department Creation
**Status:** Planning
**Owner:** Marketing + Dev

**Requirements:**
- Widgets upgrade
- Affiliation installation
- URL: https://rh-s.com/affiliate

**Tasks:**
- TSK-097: Create Affiliation Department entity
- TSK-098: Widgets upgrade
- TSK-099: Affiliation program installation
- TSK-100: Documentation

**Prompts:** PMT-036 (Dev), PMT-040 (Marketing)

---

### Business Entity Population
**Status:** Design Phase
**Owner:** SLS + AID

**Issue Noted:**
> Missing details and structure. Need to build and confirm architecture and schemas of business folder, then extract information in proper order.

**Requirements:**
- Don't change source folder
- Track what's copied
- Classify fields for tagging:
  - Client interests
  - Metadata
  - Other business info

**Process:**
1. Reverse changes to source
2. Build multi-file execution plan
3. Confirm architecture and schemas
4. Extract in proper order

**Tasks:**
- TSK-049: Populate Business Entity from Sales
- TSK-101: Define Business Entity schema
- TSK-102: Create business folder architecture
- TSK-103: Build extraction workflow
- TSK-104: Field classification system

**Prompts:** PMT-041 (Sales), PMT-044 (Research), PMT-016 (Taxonomy)

---

## 10. MEETING NOTES & DISCUSSIONS 🗣️

### Design Portfolio Strategy Meeting

**Context:** Designer interviews revealed portfolio issues

**Findings:**
- Designers showed old work (pre-employment)
- Little current work demonstrated
- Portfolios very similar (e.g., all showing same "goat" character)
  - One did images, another videos, but same character
  - Clients noticed repetition

**Conclusion:**
- Need portfolio diversification
- Goal: Create maximum case studies for available designers
- Increase client selection chances
- Focus: Build portfolios > promote company themes

**Action Items:**
- TSK-074: Portfolio diversification strategy
- TSK-075: Create more case studies
- Assignee: Design department (available designers)
- Priority: CRITICAL

---

### Task Manager Personal Dashboard Discussion

**Concept:** Personal task manager web pages

**Workflow:**
1. Take data and generate prompt for page generation
2. Run through tools
3. Extract tools from LIBRARIES
4. Build field/space for personal task manager
5. Employee-specific task view (one task or all tasks)

**Decision:** Start with single task view (one task, one employee)

**Deliverable:** HTML page (not full dashboard yet)

**Process:**
1. For test: Make one research
2. By end of work session: One video fully parsed and in system
3. Validate workflow works correctly
4. Improve process
5. Delegate to deep research designer
6. Point designer to research folder with video parsing content

**Logging:**
> "Ask to log your research progress to `C:\Users\Dell\Dropbox\ENTITIES\LOG`"

---

### Video Research Multi-Queue Discussion

**Problem Identified:**
- Previous attempts: 10-15 minutes to select 1 video from 20
- Only 1 video parsed per session
- Inefficient: Should parse all 20 that meet threshold

**Solution:** Multi-queue line system
- Accumulate queue (kolejka)
- Employee can track task queue/line
- Do deep research directly in GPT
- Save tokens on context
- Ideal for Dropbox sync users (e.g., video editors without computers)

**Implementation:**
- TSK-070: Build Researches Dashboard with queue
- Location: `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-008_Video_Queue`

---

### Markup & Tagging Discussion

**Instruction for Niko:**
> "Expand rows directly, cut, mark what's task, what's step, what belongs to what. Write annotations: 'task:', then content. 'This is project', 'this is milestone with many tasks', 'this is something else', 'this is prompt'. Make marks in your draft. Then you'll be ready to talk with the penguin [AI]."

**First Goal:**
- Not to make research
- Not to make task
- Just create ONE task called "Deep Research"

**Resources:**
- Assets folder
- Online Academy: Link to courses with Deep Research
- Check if Deep Research content exists
- If inadequate, add to New Academy/New Lessons folder
- Monday task: Upload content

**Approach:**
- Wide spectrum of material updates
- Concentrated on narrow, clear theme: Deep Research

---

## 11. NOTIFICATIONS & REMINDERS 🔔

### VS Code Key Binding
**Assignee:** Rekovald
**File:** [Key_Biddings_VS_code.md](D:\2025\Notes\Nov25\Notes\W3\221125\Key_Biddings_VS_code.md)
**Priority:** CRITICAL
**Department:** LGN (Lead Generation)
**Requirements:**
- Save at least 5 templates
- Send screenshot in CRM
- Screenshot received → Process recognition
- Confirm task done

**Task:** TSK-045 (created above)

---

### Taxonomy Basics
**Note:** Mentioned as notification topic
**Action:** Review taxonomy fundamentals
**Prompts:** PMT-014 to PMT-020

---

### GPT Connected to GitHub
**Note:** System is connected
**Action:** Separate GitHub repositories
**Task:** TST-### (under PRT-005)
**Start:** From Researches

---

### List of Tasks from Previous Day/Week
**Note:** Tracking required
**Action:** Create automated extraction
**Tasks:** TSK-008 (Extract tasks from daily reports)
**Prompts:** PMT-032 (Report Collection)

---

## 12. TODO & POSTPONED ITEMS 📝

### Postponed (1 Week)
- Research integration with Google TODO (PRT-007)

### Repetitive TODOs (Ongoing)
| ID | Task | Frequency | Owner |
|----|------|-----------|-------|
| **TSK-066** | Core System Taxonomy Architecture Review | Weekly | AID |
| **TSK-067** | Prompt for Transcription Export | As needed | AID |
| **TSK-068** | Prompts for Weekly Analysis | Weekly | AID |
| **TSK-069** | Prompts for Daily Analysis | Daily | AID |
| **TSK-070** | Researches Dashboard | Ongoing | AID + DEV |
| **TSK-071** | Export Dailies Summaries to ToDo App | Daily | AID |

---

## 13. ACHIEVEMENTS & PROGRESS ✅

### Completed: Master Activity Listing
**File:** `ENTITIES\REPORTS\2025-11-21\MASTER_ACTIVITY_LISTING_2025-11-21.csv`

**Conclusion:** Next TODO is Add Master Sheets in Entities

**Action Required:**
- Look for big lists with 500+ units
- Add categorization
- Apply data analysis for redundancy

---

### GPT Connected to GitHub Repositories
**Status:** ACTIVE

**Can Be Used For:**
- Build TODO initial list
- Build "ToDo" sub-entity in PLANS

**Action:** Build Tasks Connection (Entity)

---

## 14. TRACKS & MONITORING 📊

### Track Tasks and Projects Knowledge Coverage
**Location:** Task Manager
**Goal:** Monitor knowledge coverage per task/project

**Questions to Address:**
- What redirect URIs need registration?
- What parameters required for /api/auth/google endpoint?
- Frontend OAuth details

**Task:** TSK-105 (Knowledge coverage tracking system)

---

### Track by Micro Services
**Goal:** Task completion updates via microservices

**Examples:**
- Sign up into Libs
- Add one tool manually

**Task:** TSK-052 (already created above)

---

## 15. EXTERNAL RESOURCES & LINKS 🔗

### Google Sheets
1. **HR Onboarding:** https://docs.google.com/spreadsheets/d/1yYUD9nfHXdRfBkKUIrq_0v0hyJbKO8WpsUBPxkCYsZA/edit?gid=0#gid=0

### Test Tools
1. **Relay.app:** https://www.relay.app/templates/sales-demo-request-qualifier

### Websites
1. **Affiliation:** https://rh-s.com/affiliate
2. **Libraries Export:** libs.amyemp.com

---

## 16. KEY FILE PATHS 📂

| Purpose | Path |
|---------|------|
| **Researches** | C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES |
| **Taxonomy** | C:\Users\Dell\Dropbox\ENTITIES\RESEARCHES\TAXONOMY |
| **Video Queue** | C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-008_Video_Queue |
| **Reports (2025-11-21)** | C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-21 |
| **Departments Reports** | C:\Users\Dell\Dropbox\ENTITIES\REPORTS\2025-11-21\Departments |
| **Plans** | Dropbox\ENTITIES\PLANS\Research_System_Activation |
| **Businesses Services** | Dropbox\ENTITIES\BUSINESSES\Services |
| **Logs** | C:\Users\Dell\Dropbox\ENTITIES\LOG |

---

## 17. EXECUTION PRIORITY MATRIX

| Priority | Tasks | Department | Timeline |
|----------|-------|------------|----------|
| **CRITICAL** | TSK-037, 038, 045, 074, 092-096 | LGN, DGN, AID | 48hrs |
| **HIGH** | TSK-030, 032, 035, 036, 044, 050, 052, 054, 055, 058, 059, 062, 064, 066, 070, 072, 073, 080, 081 | All Depts | 1 week |
| **MEDIUM** | TSK-031, 033, 039-043, 046, 048, 049, 051, 053, 056, 060, 063, 065, 067-069, 071, 075, 076, 077 | All Depts | 2 weeks |
| **LOW** | TSK-034, 061 | HRM, AID | 3+ weeks |

---

## 18. SUMMARY STATISTICS 📈

**Entities Extracted:**
- **Projects (PRT):** 10 (PRT-004 to PRT-010, plus from previous)
- **Milestones (MLT):** 28 (MLT-019 to MLT-028, plus subsets)
- **Tasks (TSK):** 105 (TSK-030 to TSK-105, 76 new tasks)
- **Steps (STP):** Referenced in workflows
- **Architecture (ARC):** 6 (ARC-001 to ARC-006)

**Departments Involved:** ALL (HRM, LGN, SLS, DEV, AID, DGN, MKT)

**Prompts Referenced:**
- PMT-004 to PMT-073 (Video, Research, Reports, Automation, Taxonomy)

**Priority Breakdown:**
- CRITICAL: 7 tasks
- HIGH: 23 tasks
- MEDIUM: 33 tasks
- LOW: 2 tasks

**Database Tables Documented:** 9 (Prospects schema)

**Key Decisions Made:**
1. Portfolio diversification for designers
2. Multi-queue research system
3. Personal task manager web pages
4. Single sign-in distribution system
5. Milestone naming conventions

---

## 19. VALIDATION CHECKLIST ✔️

Before execution, ensure:
- [ ] All entity IDs exist in master CSVs/JSONs
- [ ] Database schema matches existing CRM structure
- [ ] File paths validated and accessible
- [ ] Employee assignments confirmed (Niko Kar, Rekovald, Kolya, Olya)
- [ ] External links tested and accessible
- [ ] GitHub integration verified
- [ ] Department capacity checked for task load
- [ ] Critical tasks (priority) resourced first
- [ ] Cross-references validated (TSK → MLT → PRT)
- [ ] Prompts exist in PMT_Master_List.csv

---

## 20. NEXT ACTIONS (Immediate) ⚡

**For Niko Kar (AID):**
1. Complete markup/tagging exercise (meeting instruction)
2. Create ONE task: Deep Research
3. Check Online Academy for Deep Research content
4. Add to New Academy/New Lessons if needed
5. Prepare for Monday content upload

**For Rekovald (LGN):**
1. Complete VS Code Key Binding task (CRITICAL)
2. Save 5 templates minimum
3. Submit screenshot in CRM
4. Await task confirmation

**For Kolya & Olya (Sales):**
1. Delegate CRM data on Daily LeadGen Cards (TSK-050)

**For Design Team:**
1. Begin portfolio diversification (TSK-074)
2. Create case studies (TSK-075)

**For AID Team:**
1. Fix scattered Researches architecture (TSK-092-096) - CRITICAL
2. Add rules for AI in folders (TSK-059)
3. Develop USER entities (TSK-062)

---

## FILE METADATA

**Original:** [221125.md](D:\2025\Notes\Nov25\Notes\W3\221125\221125.md)
**Processed:** 221125_PROCESSED.md
**Processor:** MAIN_PROMPT_v6 (PMT-073)
**Date:** 2025-11-24
**Session Type:** Strategic Planning Meeting + System Design
**Primary Attendee:** Niko Kar (AID Department)
**Content Type:** Mixed (Tasks, Architecture, Meeting Notes, Database Schema)
**Entities Extracted:** 10 PRT, 28 MLT, 76 TSK, 6 ARC
**Languages:** English + Russian (transcribed meeting)
**Status:** Ready for department distribution and action

---

**END OF PROCESSED FILE**
