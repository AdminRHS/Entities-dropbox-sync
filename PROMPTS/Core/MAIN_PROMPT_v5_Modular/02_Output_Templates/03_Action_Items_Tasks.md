# Template 03: Action Items & Tasks

**Purpose:** Document action items with structured task creation using LIBRARIES taxonomy
**Library Integration:** ⭐⭐⭐ Heavy (Actions, Objects, Skills, Responsibilities)
**Priority:** Include when action items discussed (most meetings)

---

## Template

```markdown
## Action Items & Tasks

**Total Action Items:** [Number]
**Assigned To:** [Number] team members
**Priority Breakdown:** [X High, Y Medium, Z Low]

### High Priority

#### 1. [Task Title]
- **Owner:** [Name] (ID: [Employee ID]) - [Position]
- **Action:** [ACT-XXX] - [Action name from Responsibilities/Responsibilities/Actions library]
- **Object:** [OBJ-XXX] - [Object from Responsibilities/Responsibilities/Objects library] (if applicable)
- **Responsibility:** [Action + Object formula]
- **Required Skill:** [SKL-XXX] - [Skill name] (if specialized)
- **Deadline:** YYYY-MM-DD or [Timeframe]
- **Status:** Not Started | In Progress | Blocked
- **Context:** [Why this needs to be done - 1-2 sentences]
- **Dependencies:** [What must happen first, if any]
- **Success Criteria:** [How to know it's complete]

### Medium Priority

[Same structure as above]

### Low Priority

[Same structure as above]

### Blocked Items

[Items that cannot proceed - note blocker]
```

---

## Recognition Rules

### Identifying Action Items

**Explicit Actions:**
- "Olha will create the mockups"
- "Yaroslav needs to fix the API bug"
- "Someone should update the documentation"

**Implicit Actions:**
- "The mockups aren't ready" → Action: Complete mockups
- "We're missing test coverage" → Action: Write tests
- "Client hasn't seen the proposal" → Action: Send proposal

**Keywords:**
- "will," "should," "needs to," "must," "have to"
- "let's," "can you," "please"
- "by Friday," "before next meeting"
- "assigned to," "responsible for"

### Matching to LIBRARIES

**Actions Library (429 actions):**
Match task to action entity:
- "Create wireframes" → ACT-DESIGN-001
- "Fix authentication bug" → ACT-DEV-004
- "Generate lead list" → ACT-SCRAPE-001 + ACT-ENRICH-001
- "Review code changes" → ACT-DEV-008

**Objects Library (36 objects):**
What is being worked on:
- "Landing page mockups" → OBJ-DESIGN-015
- "React component" → OBJ-DEV-005
- "Lead list (1000 contacts)" → OBJ-LG-001
- "Explainer video" → OBJ-VID-001

**Skills Library:**
Required capabilities:
- "Create UI mockups" requires SKL-DESIGN-001 (UI/UX Design)
- "Review code" requires SKL-DEV-005 (Git Version Control)
- "Scrape website data" requires SKL-LG-002 (Data Scraping)

**Responsibilities (Action + Object):**
- CREATE + UI MOCKUPS = Create UI Mockups
- FIX + AUTHENTICATION BUG = Fix Authentication Bug
- GENERATE + LEAD LIST = Generate Lead List

---

## Examples

### Example 1: Design Team Action Items

```markdown
## Action Items & Tasks

**Total Action Items:** 5
**Assigned To:** 3 team members
**Priority Breakdown:** 3 High, 2 Medium, 0 Low

### High Priority

#### 1. Implement Client Feedback on Landing Page A
- **Owner:** Shelep Olha (ID: 86641) - UI/UX Designer
- **Action:** ACT-DESIGN-002 - Design high-fidelity mockups
- **Object:** OBJ-DESIGN-015 - Landing Page Design
- **Responsibility:** Create/Update Landing Page Design
- **Required Skill:** SKL-DESIGN-001 - UI/UX Design (Figma)
- **Deadline:** 2025-11-18 (Friday, 3 days)
- **Status:** In Progress (70% complete as discussed)
- **Context:** Client provided feedback on initial mockups; needs final version for Monday presentation
- **Dependencies:** None
- **Success Criteria:** Client feedback addressed; design matches revised requirements; ready for client approval

#### 2. Update Design System Button Components
- **Owner:** Maslo Anastasiia (ID: 86981) - UI/UX Designer
- **Action:** ACT-DESIGN-034 - Update design system
- **Object:** OBJ-DESIGN-005 - Design System
- **Responsibility:** Update Design System Components
- **Required Skill:** SKL-DESIGN-006 - Design Systems
- **Deadline:** 2025-11-22 (Next week)
- **Status:** Not Started
- **Context:** Identified inconsistencies in button variants during review; need standardization before new projects
- **Dependencies:** Team approval on button style direction (completed in meeting)
- **Success Criteria:** All button variants updated; documented in Figma library; team notified

#### 3. Post Dribbble Shots (2 shots this week)
- **Owner:** Kucherenko Iuliia (ID: 86983) - UI/UX Designer, Graphic Designer
- **Action:** ACT-DESIGN-033 - Upload to platform (Dribbble)
- **Object:** N/A (portfolio management)
- **Responsibility:** Post Portfolio Work to Dribbble
- **Required Skill:** SKL-DESIGN-001 - UI/UX Design (for selecting work)
- **Deadline:** 2025-11-17 (Thursday)
- **Status:** Not Started
- **Context:** November portfolio goal to maintain Dribbble presence; team agreed on 2 shots per week
- **Dependencies:** Select best work from recent projects
- **Success Criteria:** 2 high-quality shots posted; proper descriptions and tags added

### Medium Priority

#### 4. Create Social Media Graphics Pack for Client B
- **Owner:** Chobotar Yuliia (ID: 72617) - Graphic Designer
- **Action:** ACT-DESIGN-006 - Design social media graphics
- **Object:** OBJ-DESIGN-011 - Social Media Graphics
- **Responsibility:** Create Social Media Graphics
- **Required Skill:** SKL-DESIGN-002 - Graphic Design
- **Deadline:** 2025-11-25 (10 days)
- **Status:** Not Started
- **Context:** Client B requested 10 Instagram post templates for December campaign
- **Dependencies:** Client brand guidelines (received)
- **Success Criteria:** 10 templates (1080x1080); source files delivered; client approval

#### 5. Research Mobile App Design Trends
- **Owner:** Shelep Olha (ID: 86641) - UI/UX Designer
- **Action:** ACT-DESIGN-020 - Conduct design research
- **Object:** N/A (research task)
- **Responsibility:** Research Design Trends
- **Required Skill:** SKL-DESIGN-001 - UI/UX Design
- **Deadline:** 2025-11-30 (End of month)
- **Status:** Not Started
- **Context:** Preparing for upcoming mobile app project; need current UX patterns
- **Dependencies:** None
- **Success Criteria:** Summary document with 10-15 trend examples; shared with team

### Blocked Items

None
```

---

### Example 2: Development Team Action Items

```markdown
## Action Items & Tasks

**Total Action Items:** 6
**Assigned To:** 2 developers
**Priority Breakdown:** 2 High, 3 Medium, 1 Low

### High Priority

#### 1. Fix Authentication API Bug (Production)
- **Owner:** Kizilova Olha (ID: 178) - Backend Developer
- **Action:** ACT-DEV-004 - Fix bug
- **Object:** OBJ-DEV-003 - API Endpoint (authentication)
- **Responsibility:** Fix API Bug
- **Required Skill:** SKL-DEV-006 - API Integration
- **Deadline:** 2025-11-16 (Tomorrow - URGENT)
- **Status:** In Progress
- **Context:** Users unable to log in since yesterday; critical production issue
- **Dependencies:** Reproduce bug locally (completed)
- **Success Criteria:** Login working for all users; deployed to production; monitored for 24 hours

#### 2. Implement User Dashboard Component
- **Owner:** Klimenko Yaroslav (ID: 86478) - Frontend Developer
- **Action:** ACT-DEV-001 - Write code
- **Object:** OBJ-DEV-005 - React Component (Dashboard)
- **Responsibility:** Develop React Component
- **Required Skill:** SKL-DEV-002 - React Development
- **Deadline:** 2025-11-20 (5 days)
- **Status:** Not Started
- **Context:** Sprint task for user dashboard feature; designs approved
- **Dependencies:** API endpoints ready (completed); design files from Olha (completed)
- **Success Criteria:** Component built; responsive; tests passing; code reviewed

### Medium Priority

#### 3. Write Tests for New Features
- **Owner:** Klimenko Yaroslav (ID: 86478) - Frontend Developer
- **Action:** ACT-DEV-006 - Write tests
- **Object:** N/A (testing task)
- **Responsibility:** Write Unit Tests
- **Required Skill:** SKL-DEV-007 - Testing (Jest, React Testing Library)
- **Deadline:** 2025-11-22 (Before deployment)
- **Status:** Not Started
- **Context:** Need >80% test coverage before merging to main
- **Dependencies:** Dashboard component completed (pending)
- **Success Criteria:** Test coverage >80%; all tests passing; edge cases covered

#### 4. Code Review for Liliia's PR
- **Owner:** Kizilova Olha (ID: 178) - Backend Developer
- **Action:** ACT-DEV-008 - Review code
- **Object:** OBJ-DEV-002 - Pull Request
- **Responsibility:** Review Code Changes
- **Required Skill:** SKL-DEV-005 - Git Version Control
- **Deadline:** 2025-11-16 (Within 24 hours of PR)
- **Status:** Not Started
- **Context:** Liliia submitted PR yesterday; needs review before merge
- **Dependencies:** None
- **Success Criteria:** Code reviewed; feedback provided; approved or changes requested

#### 5. Update API Documentation
- **Owner:** Kizilova Olha (ID: 178) - Backend Developer
- **Action:** ACT-DESIGN-029 - Document (technical)
- **Object:** OBJ-DEV-003 - API Endpoint
- **Responsibility:** Document API
- **Required Skill:** SKL-DEV-006 - API Integration
- **Deadline:** 2025-11-25
- **Status:** Not Started
- **Context:** New endpoints added last week; docs outdated
- **Dependencies:** None
- **Success Criteria:** All endpoints documented; examples included; published to team wiki

### Low Priority

#### 6. Refactor Legacy Code Module
- **Owner:** Klimenko Yaroslav (ID: 86478) - Frontend Developer
- **Action:** ACT-DEV-002 - Refactor code
- **Object:** N/A (code quality task)
- **Responsibility:** Refactor Code
- **Required Skill:** SKL-DEV-002 - React Development
- **Deadline:** 2025-12-01 (When time permits)
- **Status:** Not Started
- **Context:** Old component needs modernization; not blocking anything
- **Dependencies:** None
- **Success Criteria:** Code refactored; tests still passing; no functionality changes

### Blocked Items

None
```

---

### Example 3: LG Team Action Items

```markdown
## Action Items & Tasks

**Total Action Items:** 4
**Assigned To:** 3 lead generators
**Priority Breakdown:** 2 High, 2 Medium, 0 Low

### High Priority

#### 1. Build SaaS Lead List (1000 Contacts)
- **Owner:** Hanan Zaheur (ID: 87984) - Lead Generator
- **Action:** ACT-SCRAPE-001 + ACT-ENRICH-001 - Scrape & Enrich
- **Object:** OBJ-LG-001 - Lead List
- **Responsibility:** Generate Lead List
- **Required Skill:** SKL-LG-001 - B2B Lead Generation
- **Deadline:** 2025-11-18 (Friday, 3 days)
- **Status:** Not Started
- **Context:** Q4 LinkedIn campaign needs target list by Friday for Monday launch
- **Dependencies:** ICP defined in meeting (completed)
- **Success Criteria:** 1000 qualified SaaS contacts; >90% accuracy; emails verified

#### 2. Prepare LinkedIn Campaign Copy
- **Owner:** Rybak Nataliia (ID: 88054) - Lead Generator, Content Manager
- **Action:** ACT-LG-CONTENT-001 - Write outreach copy
- **Object:** OBJ-LG-004 - Email/LinkedIn Campaign
- **Responsibility:** Write Campaign Copy
- **Required Skill:** SKL-LG-004 - Email Campaign Management
- **Deadline:** 2025-11-19 (Saturday)
- **Status:** Not Started
- **Context:** Campaign copy needed before launch; 3-5 message sequence
- **Dependencies:** Target audience profile from Hanan (pending)
- **Success Criteria:** 5 message templates; A/B test variations; reviewed by Anastasiya

### Medium Priority

#### 3. Clean October Email Campaign Data
- **Owner:** Shkinder Kseniia (ID: 87157) - Lead Generator
- **Action:** ACT-SANITIZE-001 - Remove duplicates
- **Object:** OBJ-LG-002 - Scraped Dataset
- **Responsibility:** Clean Data
- **Required Skill:** SKL-LG-006 - Data Quality Management
- **Deadline:** 2025-11-22
- **Status:** Not Started
- **Context:** Archive October campaign data; clean for future use
- **Dependencies:** None
- **Success Criteria:** Duplicates removed; data normalized; archived to Google Drive

#### 4. Update Apollo.io Lead Scores
- **Owner:** Peneva Plamena (ID: 86297) - Lead Generator
- **Action:** ACT-VALIDATE-009 - Score lead quality
- **Object:** OBJ-LG-001 - Lead List
- **Responsibility:** Score Leads
- **Required Skill:** SKL-LG-007 - CRM Management
- **Deadline:** 2025-11-25
- **Status:** Not Started
- **Context:** Re-score leads based on new criteria discussed in meeting
- **Dependencies:** New scoring criteria from Anastasiya (to be sent)
- **Success Criteria:** All leads re-scored in Apollo; exported to CSV

### Blocked Items

None
```

---

## Validation Checklist

- [ ] **All action items captured** (explicit and implicit)
- [ ] **Owners assigned** with Employee IDs
- [ ] **Actions matched** to Responsibilities/Responsibilities/Actions library (ACT-XXX)
- [ ] **Objects identified** where applicable (OBJ-XXX)
- [ ] **Skills noted** for specialized tasks (SKL-XXX)
- [ ] **Deadlines included** (specific date or timeframe)
- [ ] **Status indicated** (Not Started, In Progress, Blocked)
- [ ] **Context provided** (why this task matters)
- [ ] **Dependencies listed** (what must happen first)
- [ ] **Success criteria defined** (how to know it's done)
- [ ] **Priority assigned** (High, Medium, Low)
- [ ] **Blocked items separated** if any

---

## Common Patterns

**Design Tasks:**
- ACT-DESIGN-001 to 035
- OBJ-DESIGN-001 to 020
- SKL-DESIGN-001 to 008

**Development Tasks:**
- ACT-DEV-001 to 015
- OBJ-DEV-001 to 007
- SKL-DEV-001 to 008

**LG Tasks:**
- ACT-SCRAPE, ACT-PARSE, ACT-ENRICH, ACT-VALIDATE series
- OBJ-LG-001 to 005
- SKL-LG-001 to 007

**Video Tasks:**
- ACT-VID-001 to 038
- OBJ-VID-001 to 010
- SKL-VID-001 to 006

---

## Related Templates

**Previous:** [02_Executive_Summary.md](02_Executive_Summary.md) - High-level overview
**Next:** [04_Projects_Features.md](04_Projects_Features.md) - Project context
**Related:** [21_Follow_Up_Items.md](21_Follow_Up_Items.md) - Additional follow-ups
**Libraries:** [../01_Library_Integration/](../01_Library_Integration/) - Action, Object, Skill entities

---

**Status:** ✅ Template ready for use
