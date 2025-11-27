# 3. DEPARTMENT OPERATIONS

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## DEPARTMENTS (10)

| Code | Department | Daily Report | Focus Areas |
|------|-----------|--------------|-------------|
| **AID** | AI & Automation | PMT-033 | Taxonomy, automation, system health, prompt engineering |
| **VID** | Video Production | PMT-043 | Transcription, entity extraction, video workflows |
| **HRM** | Human Resources | PMT-038 | CV parsing, recruitment automation |
| **DEV** | Development | PMT-036 | Version control, VSCode, API integration |
| **LGN** | Lead Generation | PMT-039 | Lead scraping, prospecting, outreach |
| **DGN** | Design | PMT-035 | UI/UX, graphics, creative assets |
| **MKT** | Marketing | PMT-040 | Campaigns, content strategy |
| **SLS** | Sales | PMT-041 | Pipeline management, research |
| **SMM** | Social Media | PMT-042 | Content, engagement, community |
| **FIN** | Finance | PMT-037 | Reporting, compliance, budgets |

---

## EMPLOYEE DIRECTORY

**Source:** [Nov25/Fin Nov25/Public/Employees_Public_Nov25.md](Nov25/Fin Nov25/Public/Employees_Public_Nov25.md)

**Total Employees:** 79 across 5 departments
- **managers** (includes lead generators, recruiters, financial managers, sales managers, project managers)
- **designers** (graphic designers, ui ux designers, illustrators, web designers)
- **developers** (front end, back end, full stack)
- **marketers** (media buyers, copywriters, ppc specialists, social media managers, prompt engineers)
- **videographers** (video editors)
- **crm** (developers managing CRM systems)

**Active Employees (Status: Work):** 13 employees
- ID: 178, 299, 37226, 39412, 45810, 45405, 72754, 72889, 88105, 83953, 84138, 87157, 88972

**Key Fields:**
- Employee ID (unique identifier)
- Employee Name (first + last name)
- Status (Work, Project, Available, Left, Fired, Pending)
- Rate (work capacity/hours)
- Profession (role/title)
- Position (employee, team lead, head of)
- Department (managers, designers, developers, marketers, videographers, crm)
- Start date
- Shift (Day, Evening)

**Usage:** When processing meeting transcripts or daily reports, match employee names to this directory for identification and department classification.

---

## CLIENT PROJECTS

**Definition:** Projects where Remote Helpers employees work for client companies. Employee control is limited - they execute client-defined tasks rather than managing full project lifecycle.

**Key Distinction:**
- **Internal PRT-### Projects**: Remote Helpers initiatives (PRT-003 HR Automation, PRT-007 Lead Gen Pipeline)
- **Client Projects**: Employee assigned to work for external client (employee delivers services, client manages project)

**Tracking:**
- Client name
- Project scope/description
- Employee(s) assigned (reference Employee ID)
- Tools used (TOL-###)
- Status updates from daily reports

**Example:**
```
Client Project: Website Design for Acme Corp
- Employees: 228 (Kucherenko Iuliia), 80123 (Yarmachenko Kristina)
- Tools: TOL-### (Figma), TOL-### (Adobe Illustrator)
- Tasks extracted: TST-### (individual design tasks)
- NOT a full PRT-### (client manages milestones/deadlines)
```

---

## DEPARTMENT-SPECIFIC EXTRACTION RULES

### LG (Lead Generation) Extraction

**Extract These Elements:**

**Lead Types:**
- Inbound (prospect contacted us)
- Outbound (we contacted prospect)
- Hot (high intent, ready to engage)
- Warm (moderate interest, needs nurturing)
- Cold (initial outreach, no prior engagement)

**Qualification Criteria:**
- MQL (Marketing Qualified Lead): engagement shown, needs nurturing
- SQL (Sales Qualified Lead): ready for sales conversation
- BANT: Budget, Authority, Need, Timeline assessed

**Outreach Activities:**
- Cold email campaigns
- Social media outreach (LinkedIn, etc.)
- Follow-up sequences
- Response handling

**Tools to Track:**
- CRM systems (HubSpot, Salesforce, custom)
- Scraping/enrichment (Apollo.io, Instantly.ai, LeadIQ)
- Email automation (Gmail, Mailchimp, Sendgrid)
- Data management (Google Sheets, Airtable)

**KPIs to Extract:**
- Lead volume (# leads generated/qualified)
- Lead quality (MQL→SQL conversion rate)
- Outreach volume (emails sent, connections made)
- Response rate (% responses to outreach)
- Conversion rate (% leads to opportunities)

---

### Design Extraction

**Extract These Elements:**

**Project Types:**
- Banner (ad banners, promotional graphics)
- Logo (brand identity, icons)
- Website (full site design)
- Landing page (single-page design)
- UI/UX (interface design, user flows)
- 3D (3D modeling, rendering)
- Animation (motion graphics, transitions)

**Design Stages:**
- Brief (requirements gathering, client input)
- Wireframe (low-fidelity structure)
- Draft (initial design concepts)
- Review (client feedback, revisions)
- Refinement (incorporating feedback)
- Finalization (final deliverables)

**Tools to Track:**
- Design tools (Figma, Adobe Creative Suite, Canva, Sketch)
- Prototyping (InVision, Framer, ProtoPie)
- 3D tools (Blender, Cinema 4D)
- AI design (Midjourney, Leonardo.ai, DALL-E)

**Design Elements:**
- Typography (fonts, text hierarchy)
- Color palette (brand colors, schemes)
- Layout (grid, composition, spacing)
- Components (buttons, forms, cards)
- Imagery (photos, illustrations, icons)

**KPIs to Extract:**
- Turnaround time (design completion speed)
- Revision cycles (# iterations before approval)
- Client satisfaction (feedback sentiment)
- Asset output (# deliverables produced)

---

### Dev (Development) Extraction

**Extract These Elements:**

**Project Types:**
- Frontend (UI implementation, client-side)
- Backend (server-side, APIs, databases)
- Full-Stack (both frontend + backend)
- Mobile (iOS, Android, React Native)
- QA (testing, quality assurance)
- DevOps (deployment, infrastructure)

**Development Stages:**
- Planning (architecture, requirements)
- Development (coding, implementation)
- Testing (unit, integration, E2E tests)
- Deployment (production release)
- Maintenance (bug fixes, updates)

**Technical Challenges:**
- Bugs (errors, defects, issues)
- Architecture decisions (design patterns, structure)
- Performance optimization (speed, efficiency)
- Integration issues (API connectivity, third-party)
- Code quality (refactoring, technical debt)

**Tools to Track:**
- AI coding tools (Cursor, Windsurf, GitHub Copilot, Claude Desktop)
- AI development platforms (Lovable, v0, DeepSite, Bolt.new, Replit)
- Version control (Git, GitHub, GitLab)
- Frameworks (React, Vue, Node.js, Django, FastAPI)
- Databases (PostgreSQL, MongoDB, MySQL)
- Deployment (Vercel, Netlify, AWS, Docker)

**KPIs to Extract:**
- Sprint velocity (story points/week)
- Bug resolution time (avg time to fix)
- Deployment frequency (releases/week)
- Code review turnaround
- Test coverage (% code tested)

---

### HR/Training Extraction

**Extract These Elements:**

**Program Levels:**
- Day 1 (first day orientation)
- First Week (initial training, tool setups)
- Advanced (ongoing skill development)

**Training Topics:**
- AI basics (prompting, tool usage)
- Tool setups (installation, configuration)
- Workflows (processes, best practices)
- Department-specific skills (role training)

**Tools to Track:**
- AI tools (Cursor, Claude Desktop, ChatGPT)
- Communication (Discord, Telegram, Slack)
- Project management (Google Tasks, Trello, Notion)
- Training platforms (videos, documentation)

**Training Format:**
- Tutorial videos (5-7 seconds, screen recordings)
- Documentation (guides, SOPs)
- Live sessions (onboarding calls, Q&A)
- Hands-on practice (assignments, projects)

**Language Considerations:**
- Multilingual support (Russian, Ukrainian, English, Polish)
- Simplified language (for beginners)
- Visual aids (screenshots, diagrams)

**Progress Tracking:**
- Google Tasks integration
- Milestones (day 1, week 1, week 4)
- Skill assessments
- Completion status

**KPIs to Extract:**
- Onboarding time (days to productivity)
- Training completion rate (% finished modules)
- Skill assessment scores
- Retention rate (% employees staying)

---

## CROSS-DEPARTMENT PROJECTS

**Research Operations:**

Research is a **cross-department project**, not a standalone department. Multiple departments contribute:

| Research Type | Leading/Contributing Depts | Prompts |
|---------------|---------------------------|---------|
| **Video Processing** | VID (leads) | PMT-004 to PMT-013 |
| **Document Analysis** | SMM, HRM, SLS | PMT-045 |
| **Web Research** | SLS, LGN | PMT-044, PMT-051 |
| **Platform Research** | DEV, AID | PMT-046 to PMT-052 |

**Research Workflow:**
1. Input: Video, document, web page, platform data
2. Extract: TST-### (tasks), STT-### (steps) using task-first approach
3. Classify: Group into MLT-### and PRT-### using [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)
4. Enrich: Link to TOL-### (tools) and GDS-### (guides)
5. Output: Structured data reusable across departments

---

## COLLABORATION PATTERNS

**Shared Resources:**
- All depts use Tools (TOL-###) and Guides (GDS-###)
- Research outputs → AI validates → Marketing uses
- HR profiles → Sales uses → LG targets
- Dev tools → All depts reference
- Classification guides → All depts use ([GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010), [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011))

**Daily Workflow:**
1. Run dept report (PMT-033 to PMT-043)
2. Extract entities (TST-###, STT-###, MLT-###, PRT-###)
3. Link to TOL-### and GDS-###
4. Update master CSVs in `ENTITIES/TASK_MANAGERS/TSM-00X_[Category]/`
5. Archive to `ENTITIES/REPORTS/{Dept}/{Date}`
