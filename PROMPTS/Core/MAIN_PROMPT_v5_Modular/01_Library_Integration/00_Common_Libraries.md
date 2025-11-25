# Common Libraries - Universal Entities

**File:** 01_Library_Integration/00_Common_Libraries.md
**Last Updated:** 2025-11-15
**Version:** 5.0
**Loading:** ALWAYS included in all assemblies

---

## Purpose

This file contains library entities that are **common across all departments** at Remote Helpers. These libraries provide universal context needed for any meeting analysis, regardless of department.

**What's Included:**
- Professions Library (condensed reference)
- Prompts Library (core system prompts)
- Results Library (high-level overview)
- Responsibilities Formula (Action + Object = Responsibility)

**Why Common:**
- Every department needs to understand roles and professions
- Results apply cross-functionally to all outcomes
- Prompts are system-level automation templates
- Responsibilities formula is universal

---

## 1. Professions Library (Condensed)

**Total Professions:** 27 (across all departments)
**Source:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Professions\`

### Overview

The Professions library defines all job roles at Remote Helpers and in client companies. This condensed version provides quick reference; department-specific files contain detailed profession information.

### All 27 Professions (Alphabetical)

| ID | Profession | Department(s) | Common Variations |
|----|-----------|---------------|-------------------|
| PROF-001 | Account Executive | Sales | AE, Account Manager |
| PROF-002 | AI Engineer | AI | AI Specialist, ML Engineer |
| PROF-003 | Animator | Video | Motion Designer, 3D Animator |
| PROF-004 | Automation Engineer | AI | Automation Specialist |
| PROF-005 | Backend Developer | Dev | Server-side Developer |
| PROF-006 | Content Manager | LG | Content Strategist |
| PROF-007 | Customer Success Manager | Sales | CSM, Client Success |
| PROF-008 | Data Analyst | LG | Data Specialist |
| PROF-009 | Frontend Developer | Dev | UI Developer, Client-side Dev |
| PROF-010 | Fullstack Developer | Dev | Full-stack Engineer |
| PROF-011 | Graphic Designer | Design | Visual Designer |
| PROF-012 | Illustrator | Design | Digital Illustrator |
| PROF-013 | Lead Generator | LG | Lead Gen Specialist, Prospector |
| PROF-014 | Motion Designer | Video | Motion Graphics Designer |
| PROF-015 | Personal Assistant | LG, HR | PA, Executive Assistant |
| PROF-016 | Prompt Engineer | AI | Prompt Designer |
| PROF-017 | Project Manager | All | PM, Program Manager |
| PROF-018 | QA Engineer | Dev | Quality Assurance, Tester |
| PROF-019 | Recruiter | HR | Talent Acquisition, TA |
| PROF-020 | Sales Development Rep | Sales, LG | SDR, BDR |
| PROF-021 | Sales Manager | Sales | Sales Lead |
| PROF-022 | SMM Manager | Sales | Social Media Manager |
| PROF-023 | Translator | LG | Language Specialist |
| PROF-024 | 3D Designer | Design | 3D Artist, 3D Modeler |
| PROF-025 | UI/UX Designer | Design | UX Designer, Product Designer |
| PROF-026 | Video Editor | Video | Post-Production Editor |
| PROF-027 | Web Designer | Design | Web Developer (design-focused) |

### Recognition Patterns

**When identifying professions in transcripts:**

1. **Exact match:** "We need a UI/UX designer" → PROF-025
2. **Variation match:** "Looking for an AE" → PROF-001 (Account Executive)
3. **Context clues:** "Editing videos" + Video dept → PROF-026 (Video Editor)
4. **Multiple roles:** "Frontend developer who can design" → PROF-009 + PROF-027

### Department Distribution

| Department | Profession Count | Primary Professions |
|------------|------------------|---------------------|
| **Design** | 7 | UI/UX, Graphic, Illustrator, Web, 3D, Motion |
| **Dev** | 4 | Frontend, Backend, Fullstack, QA |
| **LG** | 5 | Lead Generator, SDR, Personal Assistant, Content Manager, Translator |
| **AI** | 3 | AI Engineer, Automation Engineer, Prompt Engineer |
| **Video** | 3 | Video Editor, Animator, Motion Designer |
| **Sales** | 4 | Sales Manager, Account Executive, CSM, SMM Manager |
| **HR** | 2 | Recruiter, Personal Assistant |
| **Cross-Dept** | 1 | Project Manager (all departments) |

---

## 2. Prompts Library (Core System Prompts)

**Source:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts\`

### Overview

The Prompts library contains AI automation templates used across Remote Helpers. This section includes **core/system-level prompts** used by all departments.

*Note: Department-specific prompts (e.g., technical prompts for Dev, creative prompts for Design) are included in respective department library files.*

### Core Prompts Categories

#### System Prompts (All Departments)

**PROMPT-CORE-001: Meeting Documentation (MAIN_PROMPT)**
- **Purpose:** Transform call transcripts into structured documentation
- **Used by:** All departments
- **Input:** Raw transcript (any language)
- **Output:** Structured meeting notes with action items
- **Location:** `Core/MAIN_PROMPT_v5_Modular/`

**PROMPT-CORE-002: Daily Report Generation**
- **Purpose:** Compile daily progress reports
- **Used by:** All departments
- **Input:** Activity logs, task updates
- **Output:** Structured daily report
- **Location:** `Core/Daily_Reports/`

**PROMPT-CORE-003: Weekly Summary**
- **Purpose:** Aggregate weekly achievements and blockers
- **Used by:** All departments (especially Project Managers)
- **Input:** Week's activity data
- **Output:** Executive summary for leadership

**PROMPT-CORE-004: Task Breakdown**
- **Purpose:** Break complex projects into actionable tasks
- **Used by:** Project Managers, Team Leads
- **Input:** Project requirements
- **Output:** Task list with estimates and owners

**PROMPT-CORE-005: Email Response Template**
- **Purpose:** Generate professional email responses
- **Used by:** All departments (client communication)
- **Input:** Incoming email + context
- **Output:** Draft response email

### Prompt Integration with Other Libraries

**Relationship to Actions:**
- Prompts often generate Action items (ACT-XXX)
- MAIN_PROMPT uses Responsibilities/Responsibilities/Actions library for task categorization

**Relationship to Processes:**
- Prompts automate Processes (PROC-XXX)
- Example: PROMPT-CORE-001 automates Process "Meeting Documentation"

**Relationship to Tools:**
- Prompts are executed via Tools (Claude, ChatGPT, etc.)
- Tool selection affects prompt format/structure

---

## 3. Results Library (High-Level Overview)

**Total Results:** 432
**Source:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Results\Results_Master.json`

### Overview

The Results library defines **outcomes, achievements, and deliverables** across all departments. This is a high-level overview; specific results are detailed in department library files.

### Results Categories (Top Level)

#### Business Outcomes
- **Client acquisition** (new clients onboarded)
- **Revenue growth** (increased sales, upsells)
- **Client satisfaction** (positive feedback, renewals)
- **Market expansion** (new markets entered)

#### Operational Outcomes
- **Process improvement** (efficiency gains)
- **Quality enhancement** (reduced errors, higher standards)
- **Team productivity** (faster delivery, more output)
- **Cost reduction** (savings achieved)

#### Deliverable Outcomes
- **Projects completed** (on time, within budget)
- **Features launched** (new capabilities delivered)
- **Content published** (articles, videos, designs)
- **Systems deployed** (infrastructure, automation)

#### Growth Outcomes
- **Skills developed** (team training results)
- **Knowledge captured** (documentation created)
- **Partnerships formed** (collaborations established)
- **Innovation achieved** (new solutions, approaches)

### Common Result Patterns

**Pattern 1: Quantitative Results**
- Format: "[Metric] increased/decreased by [X]%"
- Example: "Conversion rate increased by 15%"
- Recognition: Look for numbers, percentages, metrics

**Pattern 2: Qualitative Results**
- Format: "[Quality aspect] improved/enhanced"
- Example: "Design quality improved significantly"
- Recognition: Look for quality descriptors, comparative language

**Pattern 3: Completion Results**
- Format: "[Deliverable] completed/launched/shipped"
- Example: "Landing page redesign completed"
- Recognition: Look for completion verbs, past tense

**Pattern 4: Acquisition Results**
- Format: "[X] new [entities] acquired/onboarded"
- Example: "5 new clients onboarded"
- Recognition: Look for "new," counts, acquisition verbs

### Department-Specific Result Subsets

| Department | Primary Result Types |
|------------|---------------------|
| **Sales** | Client acquisition, revenue growth, deals closed |
| **Design** | Designs completed, client satisfaction, portfolio growth |
| **Dev** | Features launched, bugs fixed, systems deployed |
| **LG** | Leads generated, contacts enriched, databases built |
| **Video** | Videos produced, views achieved, engagement rates |
| **AI** | Automation implemented, prompts created, workflows optimized |
| **HR** | Candidates recruited, positions filled, onboarding completed |

*Note: Detailed results with IDs (RESULT-001, etc.) are in department-specific library files.*

---

## 4. Responsibilities Formula

**Formula:** Responsibility = Action + Object

### Concept

A **Responsibility** is a combination of an **Action** (what needs to be done) and an **Object** (what it's done to). This formula helps define clear role responsibilities.

### Examples

| Responsibility | Action | Object | Assigned To |
|----------------|--------|--------|-------------|
| Create UI mockups | Create | UI Mockups | UI/UX Designer |
| Review code changes | Review | Code | Senior Developer |
| Generate sales leads | Generate | Sales Leads | Lead Generator |
| Edit marketing video | Edit | AI Video | Video Editor |
| Write product description | Write | Product Description | Content Manager |
| Fix authentication bug | Fix | Authentication Bug | Backend Developer |

### How to Apply

**In meeting transcripts, listen for:**

1. **Action + Object mentions:**
   - "Olha will create the wireframes" → CREATE + WIREFRAMES
   - "Yaroslav needs to fix the API" → FIX + API

2. **Implied responsibilities:**
   - "The landing page needs updating" → UPDATE + LANDING PAGE
   - Discussion about who should own this responsibility

3. **Role clarifications:**
   - "Who's responsible for testing?" → Identify Action (TEST) + Object (FEATURE/SYSTEM)

**Output format:**
```markdown
## Responsibilities Identified
1. **Shelep Olha** (UI/UX Designer) - Create wireframes for dashboard redesign
   - Action: CREATE
   - Object: WIREFRAMES
   - Context: Dashboard redesign project

2. **Klimenko Yaroslav** (Frontend Dev) - Fix API authentication bug
   - Action: FIX
   - Object: AUTHENTICATION BUG
   - Context: Critical production issue
```

### Cross-Reference to Other Libraries

**Actions Library:**
- Contains all possible actions (429 actions)
- Department files list relevant action subsets
- Examples: Create, Update, Fix, Review, Generate, etc.

**Objects Library:**
- Contains all possible objects (36 objects in 4 collections)
- Department files focus on relevant objects
- Examples: UI Mockups, Code, Video, Landing Page, etc.

**Skills Library:**
- Skills are often: Responsibility + Tool
- Example: "Create UI mockups using Figma" = Skill

**Professions Library:**
- Professions have typical responsibilities
- Example: UI/UX Designer typically creates wireframes, mockups, prototypes

---

## Integration Guidelines

### When Processing Meeting Transcripts

**Always reference Common Libraries for:**

1. **Participant profession identification**
   - Use Professions Library to identify roles
   - Cross-reference with Employee Directory (00_Core/03_Employee_Directory.md)

2. **Result recognition**
   - Identify outcomes discussed in meeting
   - Categorize using Results Library patterns

3. **Responsibility assignment**
   - Apply Responsibility Formula (Action + Object)
   - Link to participant professions

4. **Prompt context**
   - Recognize when automation/prompts are discussed
   - Reference Core Prompts when applicable

### Loading Strategy

**Common Libraries + Department Libraries:**

For any meeting:
1. **Load Common Libraries** (this file) - provides universal context
2. **Load relevant Department Libraries** - provides specific entities
3. **Load Parameters Lightweight** - provides rules/standards overview

**Example:**
- Design team meeting: Common + Design + Parameters
- Cross-functional (AI + Dev): Common + AI + Dev + Parameters
- All-hands: Common + All Departments + Parameters

---

## Recognition Confidence Levels

When matching entities from these common libraries:

**High Confidence (90-100%):**
- Exact profession name mentioned: "We need a UI/UX designer"
- Exact prompt referenced: "Using MAIN_PROMPT for documentation"
- Clear result statement: "Completed 5 landing page designs"

**Medium Confidence (60-89%):**
- Profession implied by context: "Discussing wireframes" → likely UI/UX Designer
- Result inferred: "Much better conversion" → likely "Conversion rate increased"
- Responsibility partially stated: "Olha's handling the designs" → CREATE + DESIGNS

**Low Confidence (<60%):**
- Vague reference: "Someone needs to look at this"
- Unclear outcome: "Things improved"
- Ambiguous role: "The designer" (multiple designers in team)

**Flagging:**
- ⚠️ Flag low-confidence matches for manual verification
- ❓ Ask for clarification when critical to action items

---

## Statistics Summary

**Libraries Included in Common:**

| Library | Count | Coverage |
|---------|-------|----------|
| Professions | 27 | Condensed list (full in HR + dept files) |
| Prompts | 5 core | System-level only (dept-specific in dept files) |
| Results | 432 | High-level overview (detailed in dept files) |
| Responsibilities | Formula | Universal formula, examples |

**Total Common Content:** ~500-800 lines (lightweight, always loaded)

---

## Maintenance Notes

**Update Frequency:**
- **Monthly:** Verify profession list (new roles added?)
- **Quarterly:** Review core prompts (new system prompts?)
- **As-needed:** Update results categories when new outcome types emerge

**Update Process:**
1. Identify change (new profession, new core prompt, etc.)
2. Update this Common Libraries file
3. Update affected department files if needed
4. Re-run assembly scripts to generate updated versions

**Cross-File Dependencies:**
- When updating Professions, also update: HR_Libraries.md (full list), all dept files (subsets)
- When updating Core Prompts, also update: AI_Libraries.md, Dev_Libraries.md (technical prompts)
- When updating Results, also update: All dept files (specific results)

---

## Related Files

**Core Context:**
- [00_Core/02_Company_Context.md](../00_Core/02_Company_Context.md) - Department structure
- [00_Core/03_Employee_Directory.md](../00_Core/03_Employee_Directory.md) - 32 employees with professions

**Department Libraries:**
- [01_HR_Libraries.md](01_HR_Libraries.md) - Full Professions list with details
- [02_AI_Libraries.md](02_AI_Libraries.md) - Technical prompts
- [05_Design_Libraries.md](05_Design_Libraries.md) - Design professions details
- [All department files] - Specific results, responsibilities

**System Reference:**
- [09_Taxonomy_Framework.md](09_Taxonomy_Framework.md) - How all libraries interconnect
- [README.md](README.md) - Department-to-library mapping matrix

---

## Quick Reference

### Most Common Professions by Department

**Design (9 employees):**
- UI/UX Designer, Graphic Designer, Illustrator, Web Designer

**LG (11 employees):**
- Lead Generator, Content Manager, Translator

**Dev (3 employees):**
- Frontend, Backend, Fullstack Developer

**AI (3 employees):**
- Prompt Engineer, AI Engineer, Automation Engineer

**Video (3 employees):**
- Video Editor, Animator, Motion Designer

**Sales (1 employee):**
- Sales Manager, SMM Manager

**HR (2 employees):**
- Recruiter

### Core Prompts Quick List

1. PROMPT-CORE-001: Meeting Documentation (MAIN_PROMPT)
2. PROMPT-CORE-002: Daily Report Generation
3. PROMPT-CORE-003: Weekly Summary
4. PROMPT-CORE-004: Task Breakdown
5. PROMPT-CORE-005: Email Response Template

### Responsibility Formula

**Remember:** Responsibility = Action + Object

**Quick Examples:**
- "Create designs" = CREATE (action) + DESIGNS (object)
- "Fix bugs" = FIX (action) + BUGS (object)
- "Generate leads" = GENERATE (action) + LEADS (object)

---

**Status:** ✅ Complete - Universal libraries for all department meetings
