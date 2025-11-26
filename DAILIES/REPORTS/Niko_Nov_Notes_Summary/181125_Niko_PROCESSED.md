# 181225 Niko - Taxonomy Architecture & Microservices (Processed via PMT-073)
**Date:** 2025-11-18 | **Author:** Niko Kar (AID Department Lead) | **Processor:** MAIN_PROMPT_v6
**Type:** Technical Architecture + Taxonomy Planning + Russian Discussions | **Status:** Entity-Tagged

---

## DOCUMENT OVERVIEW 📋

**Author:** Niko Kar (System Architect)
**Content:** Taxonomy architecture, microservice design, accounts management, n8n automation
**Focus:** Entity ID system, permissions, employee profile improvements, YouTube research workflow

---

## 1. PROJECT TEMPLATE: ASSETS 🗂️

**Reference File:** `\Nov25\Dev\Kizilova Olha\17\account-management-microservice-structure.plan.md`

**Template Structure:**
- "task_name" - Template
- "workflow_reference"

### Add Routes for AI Updates

**Context (Translated):**
> "Routes are called, yes, in general? You build separate routes. I wrote everything down. Then I should make routes for AI inside these folders that would transmit something like index file, yes, I have. For machine, this should work for AIs, yes, I understand. Good."

> "I've also started saving these schemas inside folders to understand what fields to write, what criteria, without returning to know about account."

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-331** | Create AI routes inside entity folders | ACT-###, OBJ-### | AID + DEV | HIGH |
| **TSK-332** | Build index files for machine/AI access | OBJ-###, ACT-### | DEV | HIGH |
| **TSK-333** | Save schemas inside folders with field definitions | OBJ-###, ACT-023 | AID | MEDIUM |

---

## 2. PROJECT: BACK FOR DROPBOX SUB-ENTITY 💾

### Task Manager - Sync Task Template

**Tool:** TOOL-DEV-020

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-334** | Sync Task Template to backend | TOL-###, ACT-### | DEV | HIGH |
| **TSK-335** | Create backend for DropBox SubEntity | TOL-###, ACT-### | DEV | HIGH |

---

### Accounts - Talents (Critical Alerts)

**Alert System:** Fired/Left Employees - Accesses to Change!

**Context (Translated):**
> "We need alerts for people who are fired, that we need to take accounts from them. Employees access to change - changing accesses. For example, now Pauline left, quite a lot of people already, we didn't change access, sometimes we change, sometimes we don't. We're talking about main emails, and there are just as many secondary ones. Same as job accounts and so on."

> "Girl worked 2 days as recruiter, got access to job accounts with everything, even not from her country."

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-336** | Build alert system for fired/left employees | ACT-###, OBJ-### | HRM + DEV | CRITICAL |
| **TSK-337** | Connect Accounts to Talents profiles | PRF-###, ACT-### | HRM + DEV | HIGH |
| **TSK-338** | Implement automatic access closure alerts | ACT-###, OBJ-### | HRM + DEV | CRITICAL |
| **TSK-339** | Track secondary accounts (not just main emails) | OBJ-###, ACT-### | HRM | HIGH |

**Prompts:** PMT-038 (HR Daily), PMT-066 (Automation)

---

### Accounts - Libraries

**Sub-Topics:**
- Job Accounts / Countries
- Team Lead Limit Accesses
- Accounts: Manager

**Context (Translated):**
> "Job accounts should be trained by countries, and countries should give access. But I have, for example, 1000 job accounts, I don't want to give access to all 1000. That is, if she can take, well, so conduct, how does this happen now."

> "Same as LinkedIn accounts, but there's no such obvious concept as countries. But how not to give access immediately to all LinkedIn accounts to person. Give him only to team lead, give him only 50 that he's responsible for or something."

**Permission System Design:**
- By country (for job accounts)
- By team lead responsibility
- By role/department
- Limit access to subset (not all 1000)

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-340** | Design country-based job account permissions | ACT-###, OBJ-### | LGN + DEV | HIGH |
| **TSK-341** | Implement team lead access limits | PRF-###, ACT-### | Management + DEV | HIGH |
| **TSK-342** | Build role-based account access system | ACT-###, OBJ-### | DEV | MEDIUM |
| **TSK-343** | Create account manager interface | TOL-###, ACT-### | DEV | MEDIUM |

---

## 3. LEAD GENERATION 🎯

**Balkans: !No Region!**

**Note:** Balkans not configured as region yet

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-344** | Add Balkans as region in system | OBJ-###, ACT-### | LGN | MEDIUM |

---

## 4. SETTINGS ⚙️

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\SETTINGS\Auth User Service.md`

### Permission System Design

**Context (Translated):**
> "This is like permission. And to whom will it be only by employees? Will it be by employees or by professions, or what other options."

> "But it's not about machines, like who I allow to open. For example, opened dd, want to open for dd for designer, then I can choose designer."

**Options:**
- By employees (individual)
- By professions (role-based)
- By departments
- Hybrid approach

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-345** | Design permission system architecture | ACT-###, OBJ-### | DEV + Management | HIGH |
| **TSK-346** | Implement employee-based permissions | PRF-###, ACT-### | DEV | MEDIUM |
| **TSK-347** | Implement profession/role-based permissions | PRF-###, ACT-### | DEV | MEDIUM |
| **TSK-348** | Create Auth User Service documentation | ACT-023, OBJ-### | DEV | MEDIUM |

---

## 5. EXPENSES & COST CUTTING 💰

**Item:** Cut off GPT (reduce expenses)

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-349** | Review GPT usage and costs | OBJ-###, ACT-### | Management + FIN | MEDIUM |
| **TSK-350** | Identify cost-cutting opportunities | ACT-###, OBJ-### | Management | MEDIUM |

---

## 6. ENTITIES TAXONOMY 📚

### Create Taxonomy Prompt

**Objective:** Build Taxonomy Initial list of IDs in Eco System

**Tasks:**
1. List all Entities and sub-Entities
2. Define names and IDs structure
3. Add possible 3-letter ISO name

**Sub-Sections:**
- Task Manager Taxonomy
- Libraries Taxonomy

---

### Prompt: Taxonomy – Initial ID Inventory

**Full Prompt Specification:**

**Objective:** Produce a canonical list of IDs covering all Entities and their direct sub-entities across the Remote Helpers ecosystem.

**Instructions:**

**1. Scope:**
- Include every top-level Entity in `ENTITIES/` (e.g., TASK_MANAGERS, LIBRARIES, BUSINESSES, ANALYTICS, ACCOUNTS, etc.)
- For each Entity, list every immediate sub-entity folder or logical module
  - Example: TASK_MANAGERS → Task_Templates, Step_Templates, Project_Templates, Researches, Prompts, etc.
- Note any Entity or sub-entity already marked deprecated, archived, or migrated (include status in parentheses)

**2. Data to capture per item:**
```json
{
  "name": "",           // folder or logical label (plain text)
  "path": "",           // relative path from repo root
  "entity_type": "",    // "entity" for top-level, "sub_entity" for children
  "description": "",    // brief purpose summary if documented
  "status": "",         // active, deprecated, archived, or planned
  "notes": []          // related docs, schema files, migrations
}
```

**3. Output format:**
- JSON array with consistent casing
- No duplicate paths

**4. Validation / completeness checks:**
- Confirm every top-level Entity directory has corresponding entry
- Cross-check sub-entities against existing listings or README indices (e.g., Task_Templates_Listing.md)
- Highlight gaps (e.g., "No README found for …") inside notes

**5. Deliverable:**
- Return JSON plus short summary paragraph
- Call out total counts (entities vs sub-entities)
- List any discovered inconsistencies

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-351** | Create taxonomy initial ID inventory | PMT-014-020, ACT-### | AID | CRITICAL |
| **TSK-352** | Generate JSON with all entities and sub-entities | OBJ-###, ACT-### | AID | CRITICAL |
| **TSK-353** | Add 3-letter ISO codes to entities | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-354** | Cross-validate with existing listings | ACT-###, OBJ-### | AID | HIGH |
| **TSK-355** | Document deprecated/archived entities | ACT-023, OBJ-### | AID | MEDIUM |

**Prompts:** PMT-016 (Taxonomy Creation), PMT-073 (Prompt Generation)

---

### MLS* to MLST

**Note:** Switch milestone abbreviation from MLS to MLST

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-356** | Update milestone prefix from MLS-### to MLST-### | ACT-###, OBJ-### | AID | LOW |

---

## 7. PROJECT: ENTITIES ARCHITECTURE 🏗️

**Full Title:** PRJ-Entities Architecture-MLS-Create New Entity TSK: Create Plans

### Tasks:
- Filter Daily Notes by Taxonomy
- Build Parsing Extraction Taxonomy
- Identify repetitions

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-357** | Filter daily notes by taxonomy | PMT-032, ACT-### | AID | HIGH |
| **TSK-358** | Build parsing extraction taxonomy | PMT-014-020, ACT-### | AID | HIGH |
| **TSK-359** | Identify repetitions in daily notes | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-360** | Create PLANS entity folder | OBJ-012, ACT-### | AID | MEDIUM |

---

## 8. MILESTONE TEMPLATES: YOUTUBE RESEARCH 🎥

### Workflow:

**Task:** Create List of YouTube Channels

**Steps:**
1. Collect YT Channels
2. Parse List of Latest Videos
3. Analyze Per Relevancy

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-361** | Create YouTube channels list | OBJ-###, ACT-### | VID + AID | HIGH |
| **TSK-362** | Parse latest videos from channels | PMT-004, ACT-### | VID + AID | HIGH |
| **TSK-363** | Analyze video relevancy | ACT-###, OBJ-### | VID + AID | MEDIUM |
| **TSK-364** | Build YouTube research milestone template | MLT-###, ACT-### | AID | MEDIUM |

**Prompts:** PMT-051 (Research), PMT-004 (Video Transcription)

---

## 9. AUTOMATIONS 🤖

### Log Automations from n8n

**Source:** n8n.rh-s.com

### Talents / Voice Log

**Both Files:**
- Export from CRM
- Export from DropBox

**Context (Translated):**
> "Yes, no need! From this moment at least something will be. This is good. Mini-instruction. How simple is it to make this step? You create starting point, like pull clock, then pull Google Sheet, you separate individual Google Sheets, yes?"

> "So tomorrow morning log everything. That is, it's a project. Including bots. That is, bot is separate milestone, let's say, yes there. Create there and there."

> "We really need first hot, first fully ready projects. Milestone, as they say, so that in future next filling has at least ten examples under it. While I don't upload, it immediately floats because empty half year."

**n8n Workflow Ideas:**
- Google Sheets integration
- Bot creation as separate milestone
- Need 10+ example projects first
- AI agent analysis integration via GPT/OpenRouter

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-365** | Log all n8n automations | TOL-###, ACT-### | DEV | HIGH |
| **TSK-366** | Create n8n workflow documentation | ACT-023, OBJ-### | DEV | HIGH |
| **TSK-367** | Build Google Sheets integration workflow | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-368** | Create bot as separate milestone template | MLT-###, ACT-### | DEV | MEDIUM |
| **TSK-369** | Build AI agent for n8n analysis | TOL-###, ACT-### | DEV + AID | LOW |
| **TSK-370** | Generate n8n workflow from Claude | PMT-066, ACT-### | DEV | LOW |
| **TSK-371** | Create 10+ example n8n projects | OBJ-###, ACT-### | DEV | MEDIUM |

**Tools:** n8n, Google Sheets, GPT/OpenRouter, AI agents
**Prompts:** PMT-066 (Automation)

---

## 10. REMINDER: DAILY ANALYSIS PROMPT ⏰

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-372** | Implement daily analysis prompt reminder | PMT-032-043, ACT-### | AID | MEDIUM |

---

## 11. PROJECT: EMPLOYEES PROFILES (REQUIRES) 👥

### Continuous Improvement System

**Context (Translated):**
> "Together with attendance, together with employee profile and so on, we can plug in analysis of their records, then we can constantly improve employee profile."

### Data Injections in Employees Profiles

**Workflow:**
1. Collect daily records
2. Analyze employee records
3. Update attendance data
4. Continuously improve profile

**Method (Translated):**
> "We need to run their daily notes through scripts, saturate with injections. That is, finding action and there, and so on. You take this file, you inject it with all kinds of marks, and only then collect data."

**Process:**
1. Take employee daily file
2. Inject with markings (actions, objects, etc.)
3. Collect data from marked-up file
4. Update employee profile

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-373** | Build continuous employee profile improvement system | PRF-###, ACT-### | HRM + AID | HIGH |
| **TSK-374** | Integrate attendance with employee profiles | PRF-###, OBJ-### | HRM + DEV | HIGH |
| **TSK-375** | Analyze employee daily records | ACT-###, OBJ-### | AID | HIGH |
| **TSK-376** | Create data injection scripts for daily notes | TOL-###, ACT-### | DEV + AID | HIGH |
| **TSK-377** | Build action/object extraction from daily notes | ACT-###, OBJ-### | AID | MEDIUM |
| **TSK-378** | Update employee profiles automatically | PRF-###, ACT-### | HRM + AID | MEDIUM |

**Prompts:** PMT-038 (HR Daily), PMT-032 (Report Collection)

---

### Task Template Schema

**Reference:** Prompt 6

**Context (Translated):**
> "Then 6, but that is, 6 is more global like that, there by departments. Front end. You prompt, so daily reports, open tab. Cursor Code. Code. You're my beacon."

> "6 is already... let's go 5 minutes and we'll disperse. Here it is, not to folder Niko pointing, let him figure it out himself."

**Instructions for Prompt 6:**
- Refine daily library extraction
- Data from dailies profiles
- MLS folders
- Analyze files 17 and 18
- Filing new files
- Analyzing same
- Use symbol sequence
- Identifying actions first
- Then through connections of actions and objects
- Come up to possible tasks formations
- Extract daily matching data

**Links to Provide:**
- Actions in LIBRARIES
- Objects within responsibilities
- Task Manager → Task Template
- Taxonomy for LIBRARIES
- Taxonomy for Task Manager

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-379** | Update Prompt 6 for daily analysis | PMT-073, ACT-### | AID | HIGH |
| **TSK-380** | Create task template schema | TST-###, ACT-### | AID | MEDIUM |
| **TSK-381** | Link actions/objects to responsibilities | ACT-###, RSP-###, OBJ-### | AID | MEDIUM |
| **TSK-382** | Match research prompt naming conventions | PMT-051, ACT-### | AID | MEDIUM |

**Prompts:** PMT-006 (Main Prompt 6), PMT-032 (Daily Reports)

---

## 12. SOCIAL MEDIA POSTING AUTOMATION 📱

**Context (Translated):**
> "Return to life. Yes, on this network from several generations can move in direction, that is, master at least on LinkedIn accounts, yes, and very could be with ours if we parse videos that come out in last 2-3 weeks, last month, then we - this is excellent content for posting, right?"

> "List came especially if laid out, this reason to causes-consequences or step-by-step this, yes. Such video 40 minutes, and beer shots carousel like 10 screens total is made."

**Workflow:**
1. Parse recent videos (last 2-3 weeks / last month)
2. Break down into step-by-step or cause-consequence
3. Create carousel posts (10 screens from 40-min video)
4. Post to LinkedIn accounts

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-383** | Parse recent videos for LinkedIn content | PMT-004, ACT-### | VID + SMM | MEDIUM |
| **TSK-384** | Create carousel posts from video content | ACT-###, OBJ-### | SMM + DGN | MEDIUM |
| **TSK-385** | Build automated posting workflow | TOL-###, ACT-### | DEV + SMM | LOW |
| **TSK-386** | Design step-by-step content templates | ACT-###, OBJ-### | SMM | LOW |

**Prompts:** PMT-004 (Video Transcription), PMT-066 (Automation)

---

## 13. MICROSERVICE METHODOLOGY DISCUSSION 💻

**Context (Translated):**
> "We can test on some small entity. We can test on some small entity possibility of generating backend based on data that is, something of this type dynamic some Postgres based on data that is in one of Subentities, even. That is, immediately create backend based on git and dropbox."

> "But we in git just uploaded this data. That is, if connection easier through github, then there's branch, yes? And synchronized, and synchronized in this back data from this one to cells designer."

**Methodology:**
1. Test on small entity first
2. Generate backend dynamically based on existing data
3. Use GitHub for easier connection
4. Sync data from Dropbox to backend
5. Prove concept before scaling

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-387** | Design microservice methodology | ACT-###, OBJ-### | DEV + AID | HIGH |
| **TSK-388** | Test backend generation on small entity | TOL-###, ACT-### | DEV | HIGH |
| **TSK-389** | Build GitHub-Dropbox sync for backend | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-390** | Create dynamic Postgres generation | TOL-###, ACT-### | DEV | LOW |

**Prompts:** PMT-036 (Dev), PMT-060 (Integration)

---

## 14. TECHNICAL NOTES & OBSERVATIONS 📝

### API Tokens
- **Note:** Need to manage API tokens for integrations

### File Organization
- Taxonomy created inside TASK_MANAGERS (unexpected location)
- Hierarchy item created by AI
- Checklist items integrated into tasks
- Mouse cursor causing flickering issue identified

### Prompt Saving
- Saving prompts by copying to daily notes
- Research prompt integration
- Not just prompt, but research point to research

### Login Management
- Need to switch accounts frequently
- Token management across multiple tools

### Subtitles
- **Credit:** DimaTorzok handled subtitles

| ID | Task | Entities | Department | Priority |
|----|------|----------|------------|----------|
| **TSK-391** | Organize API tokens management | TOL-###, ACT-### | DEV | MEDIUM |
| **TSK-392** | Fix taxonomy location (move if needed) | ACT-###, OBJ-### | AID | LOW |
| **TSK-393** | Integrate checklist items into task system | TST-###, ACT-### | AID | LOW |
| **TSK-394** | Fix cursor flickering issue | TOL-###, ACT-### | DEV | LOW |

---

## 15. KEY COLLABORATION MOMENTS 👥

**People Mentioned:**
- Kizilova Olha (Dev - Account management microservice)
- DimaTorzok (Subtitles)
- dd@rh-s.com (Account reference)
- Pauline (Left company - access example)

**Tools Referenced:**
- n8n.rh-s.com
- Claude Code
- Cursor
- Whisper
- OpenRouter
- GPT
- Google Sheets

---

## EXECUTION PRIORITY MATRIX

| Priority | Task IDs | Focus Area | Timeline |
|----------|----------|------------|----------|
| **CRITICAL** | TSK-336-338, 351-352 | Employee access alerts, taxonomy inventory | 24-48hrs |
| **HIGH** | TSK-331-335, 340-341, 357-358, 361-362, 365-367, 373-377, 379, 387-388 | AI routes, permissions, YouTube research, employee profiles, microservices | 1 week |
| **MEDIUM** | TSK-339, 342-348, 353-355, 359-364, 368, 370-372, 378, 380-386, 389, 391 | Secondary systems, templates, automations, posting | 2 weeks |
| **LOW** | TSK-349-350, 356, 369, 385, 390, 392-394 | Cost cutting, naming changes, future features | 3+ weeks |

---

## FILE METADATA

**Original:** [181225_Niko.md](D:\2025\Notes\Nov25\Notes\W3\181215\181225_Niko.md)
**Processed:** 181225_Niko_PROCESSED.md
**Processor:** MAIN_PROMPT_v6 (PMT-073)
**Date:** 2025-11-24
**Author:** Niko Kar (AID Department Lead)
**Content Type:** Technical Architecture + Taxonomy Design + Russian Discussions
**Tasks Extracted:** 64 (TSK-331 to TSK-394)
**Focus:** Taxonomy ID system, permissions architecture, employee profile automation, n8n workflows
**Status:** Ready for technical implementation teams

---

**END OF PROCESSED FILE**
