# 2. ENTITY REFERENCE

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## ID FORMAT

**Pattern:** `XXX-###`
- **XXX:** 3 consonants (PRT, MLT, TST, STT, TOL, GDS, PMT)
- **###:** 3 digits, zero-padded (001, 042, 153)
- **Sequential:** No gaps, no category prefixes
- **Immutable:** IDs never change after assignment

**Examples:**
- ✅ CORRECT: MLT-001, TST-042, PMT-005, GDS-010, STT-127
- ❌ WRONG: MLT-1, TSK-VID-042, PMT-COR-005, GDS10, TST-42

---

## ENTITY TYPES

| Code | Entity | Use For | Master CSV |
|------|--------|---------|------------|
| **PRT** | Project Template | Multi-week initiatives, progress tracking | TSM-001_Project_Templates/Project_Templates_Master_List.csv |
| **MLT** | Milestone Template | Project phases, major checkpoints | TSM-002_Milestone_Templates/Milestones_Master_List.csv |
| **TST** | Task Template | Daily/weekly work units (most common) | TSM-003_Task_Templates/Task_Templates_Master_List.csv |
| **STT** | Step Template | 5-30 minute actions within tasks | TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv |
| **TOL** | Tool | Software, platforms, browser extensions | LIBRARIES/LBS_003_Tools/ |
| **GDS** | Guide | Classification help, decision trees | TSM-007_GUIDES/GUIDES_Master_List.csv |
| **PMT** | Prompt | Workflow automation prompts | PROMPTS/DATA_FIELDS/PMT_Master_List.csv |

---

## REUSABLE TEMPLATES (Many-to-Many)

Templates are **INDEPENDENT** and **REUSABLE**:
- Same STT-### can be used in multiple TST
- Same TST-### can be used in multiple MLT
- Same MLT-### can be used in multiple PRT

**No hard links** - Composition happens at runtime.

---

## DECISION TREE (from GDS-011)

**"Is this a complete work unit taking hours/days?"**
- ✅ YES → Create **TST-###** (Task Template)
- ❌ NO → Next question

**"Is this a 5-30 minute action within a larger task?"**
- ✅ YES → Create **STT-###** (Step Template)
- ❌ NO → Might be **MLT-###** (Milestone)

**"Does this span weeks with multiple milestones?"**
- ✅ YES → Create **PRT-###** (Project Template)
- ❌ NO → Check existing PRT-001 to PRT-009

---

## VALIDATION RULES

**Before creating new entity:**
1. Check master CSV for existing
2. Use next sequential ID (find highest, +1)
3. Fill all required metadata (Name, Description, Department)
4. Validate references (all linked PRT/MLT/TST/STT/TOL/GDS exist)
5. No duplicates

---

## LIBRARIES FRAMEWORK

### Actions by Department

**Actions** are standardized verbs used to describe work activities. From the original 438 actions library, we've organized key actions by department:

#### HR Actions (15 core actions)

- **assess** (candidates, skills, culture fit)
- **recruit** (talent, candidates, specialists)
- **contact** (candidates, applicants, references)
- **announce** (positions, policies, changes)
- **assign** (responsibilities, tasks, projects)
- **approve** (candidates, offers, contracts)
- **confirm** (interviews, start dates, onboarding)
- **begin** (onboarding, training, orientation)
- **congratulate** (new hires, promotions, milestones)
- **delegate** (tasks, responsibilities, authority)
- **empower** (employees, teams, decision-making)
- **list** (requirements, qualifications, responsibilities)
- **present** (offers, benefits, policies)
- **screen** (candidates, applications, resumes)
- **interview** (candidates, applicants, references)

#### AI Actions (12 core actions)

- **extract** (data, information, entities)
- **analyze** (data, patterns, trends)
- **build** (models, workflows, automations)
- **configure** (prompts, settings, parameters)
- **automate** (processes, workflows, tasks)
- **coordinate** (systems, integrations, data flows)
- **establish** (baselines, benchmarks, standards)
- **evaluate** (performance, accuracy, results)
- **grade** (quality, relevance, confidence)
- **measure** (metrics, KPIs, outcomes)
- **plan** (implementations, migrations, rollouts)
- **reflect** (on results, learnings, improvements)

#### Video Actions (12 core actions)

- **generate** (videos, scenes, assets)
- **load** (footage, assets, files)
- **configure** (settings, formats, export)
- **animate** (graphics, transitions, text)
- **build** (timelines, sequences, compositions)
- **capture** (footage, screen recordings, audio)
- **edit** (videos, clips, sequences)
- **film** (content, interviews, b-roll)
- **frame** (shots, compositions, scenes)
- **light** (scenes, subjects, environments)
- **perform** (voice-overs, narration, acting)
- **record** (audio, video, screen)

#### Sales Actions (12 core actions)

- **contact** (prospects, leads, clients)
- **reach out** (to prospects, to partners, to clients)
- **send** (proposals, quotes, follow-ups)
- **pitch** (solutions, services, value propositions)
- **close** (deals, contracts, agreements)
- **negotiate** (terms, pricing, contracts)
- **plan** (outreach, campaigns, strategies)
- **recommend** (solutions, services, next steps)
- **begin** (partnerships, contracts, projects)
- **follow up** (with prospects, after meetings, on proposals)
- **present** (solutions, demos, proposals)
- **brainstorm** (solutions, strategies, approaches)

#### Design Actions (12 core actions)

- **compose** (layouts, scenes, visuals)
- **create** (mockups, assets, components)
- **design** (interfaces, graphics, layouts)
- **develop** (concepts, styles, themes)
- **draft** (wireframes, sketches, prototypes)
- **redesign** (interfaces, layouts, components)
- **build** (components, prototypes, systems)
- **paint** (illustrations, graphics, icons)
- **frame** (layouts, compositions, grids)
- **animate** (UI elements, transitions, interactions)
- **arrange** (elements, layouts, hierarchies)
- **sketch** (ideas, concepts, wireframes)

#### Dev Actions (12 core actions)

- **build** (features, APIs, components)
- **develop** (applications, systems, modules)
- **configure** (environments, tools, settings)
- **automate** (testing, deployment, workflows)
- **test** (code, features, integrations)
- **extract** (data, APIs, services)
- **deploy** (applications, updates, fixes)
- **edit** (code, configs, files)
- **format** (code, data, output)
- **generate** (code, documentation, tests)
- **compile** (code, packages, builds)
- **modify** (code, features, configs)

#### LG Actions (12 core actions)

- **contact** (leads, prospects, companies)
- **reach out** (to leads, to prospects, to accounts)
- **send** (emails, messages, outreach)
- **analyze** (leads, companies, markets)
- **qualify** (leads, prospects, opportunities)
- **follow up** (with leads, after outreach, on responses)
- **extract** (leads, data, contacts)
- **scrape** (websites, directories, platforms)
- **parse** (data, lists, exports)
- **feed** (CRM, databases, lists)
- **sanitize** (data, lists, contacts)
- **combine** (lists, sources, datasets)

---

### Objects by Department

**Objects** are department-specific business entities that actions are performed on.

#### HR Objects

**Candidates:**
- needed (requisition opened)
- applied (application submitted)
- found (sourced proactively)
- interviewed (completed interview)
- offered (offer extended)
- hired (accepted and onboarded)

**Communications:**
- first connection (initial outreach)
- update (status update to candidate)
- follow-up (after interview/application)
- feedback (interview feedback, rejection)

**Contracts:**
- employee contract
- presale agreement
- NDA (non-disclosure agreement)

**Interviews:**
- video interview
- project interview (technical assessment)
- cultural fit interview

---

#### LG Objects

**Accounts:**
- new (recently created)
- in work (actively being used)
- sold (client acquired)
- banned (restricted/blocked)
- free (available for use)

**Companies:**
- lead (potential client)
- interested (engagement shown)
- client (active customer)
- updated (information refreshed)
- not relevant (disqualified)

**Leads:**
- hot (high purchase intent, immediate opportunity)
- warm (moderate interest, nurturing needed)
- cold (low/no engagement, initial outreach)
- qualified (meets BANT/criteria)
- unqualified (doesn't meet criteria)

**Messages:**
- cold email (initial outreach)
- follow-up (subsequent touchpoint)
- response (reply from prospect)
- template (reusable message)

---

#### Dev Objects

**APIs:**
- REST (RESTful APIs)
- GraphQL (GraphQL APIs)
- internal (internal services)
- external (third-party APIs)

**Databases:**
- PostgreSQL
- MongoDB
- MySQL

**Modules:**
- frontend (UI components, pages)
- backend (server logic, APIs)
- shared (utilities, libraries)

**Code:**
- functions (JS/Python functions)
- components (React/Vue components)
- tests (unit/integration tests)
- scripts (automation scripts)

---

#### Design Objects

**Mockups:**
- wireframe (low-fidelity structure)
- high-fidelity (polished design)
- low-fidelity (basic sketch)

**Logos:**
- primary (main brand logo)
- secondary (alternative version)
- icon (favicon, app icon)

**Illustrations:**
- vector (SVG, scalable graphics)
- raster (PNG, JPG images)
- 3D (3D renders)

**UI Components:**
- buttons (CTA, navigation)
- forms (inputs, fields)
- cards (content containers)
- navigation (menus, breadcrumbs)

---

#### Video Objects

**Videos:**
- raw footage (unedited capture)
- edited (in-progress edit)
- final (completed, exported)
- draft (rough cut)

**Assets:**
- music (background tracks)
- sound effects (audio FX)
- graphics (motion graphics, overlays)
- transitions (scene transitions)

---

### Skills Formula

**Skill = Responsibility (Action + Object) + Tool**

A **Skill** is formed by combining an **Action** with an **Object** and the **Tool** used to perform it.

**Examples by Department:**

**HR:**
- **screened** candidates via **CRM** = screen + candidates + CRM
- **interviewed** candidates via **Zoom** = interview + candidates + Zoom
- **assessed** culture fit via **structured interview** = assess + culture fit + interview template

**LG:**
- **sent** cold emails via **Gmail** = send + cold emails + Gmail
- **qualified** leads via **BANT criteria** = qualify + leads + BANT framework
- **extracted** leads via **Apollo.io** = extract + leads + Apollo.io
- **scraped** companies via **Instantly.ai** = scrape + companies + Instantly.ai

**Dev:**
- **built** REST APIs in **Node.js** = build + REST APIs + Node.js
- **deployed** applications via **GitHub Actions** = deploy + applications + GitHub Actions
- **tested** components with **Jest** = test + components + Jest
- **configured** environments in **Docker** = configure + environments + Docker

**Design:**
- **designed** UI mockups in **Figma** = design + mockups + Figma
- **created** logos in **Adobe Illustrator** = create + logos + Adobe Illustrator
- **drafted** wireframes in **Miro** = draft + wireframes + Miro
- **animated** UI elements in **After Effects** = animate + UI elements + After Effects

**Video:**
- **edited** raw footage in **Premiere Pro** = edit + raw footage + Premiere Pro
- **generated** videos via **Runway** = generate + videos + Runway
- **captured** screen recordings in **OBS** = capture + screen recordings + OBS

**AI:**
- **extracted** data via **Claude** = extract + data + Claude
- **automated** workflows in **n8n** = automate + workflows + n8n
- **configured** prompts in **Claude Desktop** = configure + prompts + Claude Desktop

---

## PRACTICAL EXAMPLE

**Scenario:** "Set up n8n workflow to automate weekly reports"

**Classification:**
- Complete work unit? YES (takes hours) → **TST-###**
- Part of larger initiative? YES → Check projects
- Fits existing PRT-003 (HR Automation)? YES → Use MLT-006

**Breakdown:**
```
TST-055: Set up n8n weekly report automation
  ├─ STT-201: Create workflow canvas
  ├─ STT-202: Configure schedule trigger (every Monday 9am)
  ├─ STT-203: Add Google Sheets data source
  ├─ STT-204: Set up email notification node
  └─ STT-205: Test and deploy

Tools: TOL-007 (n8n), TOL-150 (Google Sheets), TOL-XXX (Gmail)
Guide: GDS-010
```

**Fits Into:**
```
PRT-003: Complete HR Automation Implementation
  └─ MLT-006: HR System Integration
      ├─ TST-042: Create n8n employee data sync ✅
      └─ TST-055: Set up n8n weekly report automation 🔄
```
