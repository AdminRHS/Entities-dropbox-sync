# Taxonomy Framework - System Architecture & Library Relationships

**File:** 01_Library_Integration/09_Taxonomy_Framework.md
**Last Updated:** 2025-11-15
**Version:** 5.0
**Purpose:** System architecture reference - How all 12 LIBRARIES interconnect

---

## Overview

The Remote Helpers taxonomy system consists of **12 interconnected LIBRARIES** that provide a comprehensive organizational framework. This file explains the system architecture, how libraries relate to each other, and the integration philosophy.

**Purpose:** This is a **reference document** explaining the system, not an operational file for entity matching. Load this when understanding overall system architecture is needed.

---

## The 12 LIBRARIES

### Core Entity Libraries

| # | Library | Count | Description | Primary Use |
|---|---------|-------|-------------|-------------|
| 1 | **Actions** | 429 | What needs to be done | Task creation, Action items |
| 2 | **Objects** | 36 | What's being worked on | Deliverables, Outputs |
| 3 | **Processes** | 428 | How work is done | Workflow documentation |
| 4 | **Results** | 432 | What's achieved | Outcomes, Success metrics |
| 5 | **Skills** | 12+ | Capabilities required | Team context, Training |
| 6 | **Responsibilities** | Formula | Role clarification | Team assignments |
| 7 | **Products** | 39 | What's offered | Service offerings |
| 8 | **Services** | 7 cats | Service categories | Sales, AI |
| 9 | **Parameters** | 10,596+ | Rules, Standards | Quality, Best practices |
| 10 | **Professions** | 27 | Job roles | Employee identification |
| 11 | **Tools** | 75+ | Technologies used | Technical architecture |
| 12 | **Prompts** | Varies | AI automation templates | Workflow automation |

---

## System Architecture

### Three-Layer Taxonomy Model

```
┌─────────────────────────────────────────────────────────┐
│                    LAYER 3: CONTEXT                      │
│  Professions | Parameters | Tools | Prompts | Services   │
│  (Who) (Rules) (How) (Automation) (Categories)          │
└─────────────────────────────────────────────────────────┘
                          ▲
                          │
┌─────────────────────────────────────────────────────────┐
│                  LAYER 2: EXECUTION                      │
│         Actions | Processes | Responsibilities           │
│         (Do) (How-to) (Who does what)                    │
└─────────────────────────────────────────────────────────┘
                          ▲
                          │
┌─────────────────────────────────────────────────────────┐
│                   LAYER 1: OUTCOMES                      │
│              Objects | Results | Skills                  │
│         (Deliverables) (Achievements) (Capabilities)     │
└─────────────────────────────────────────────────────────┘
```

**Layer 1 (Outcomes):** What we create and achieve
**Layer 2 (Execution):** How we do the work
**Layer 3 (Context):** Who does it, with what tools, following which rules

---

## Primary Library Relationships

### 1. The Core Workflow Chain

**Actions → Processes → Results**

This is the fundamental workflow lifecycle:

```
ACTION               PROCESS                  RESULT
(Create mockups) → (UI/UX Design Process) → (High-quality designs delivered)
(Generate leads) → (Lead List Building)   → (1000 qualified leads)
(Fix bug)        → (Bug Fix Workflow)      → (Bug resolved, deployed)
```

**Explanation:**
- **Actions** are individual tasks
- **Processes** combine actions into workflows
- **Results** are the outcomes achieved

---

### 2. The Responsibility Formula

**Responsibility = Action + Object**

Combining actions with objects defines clear responsibilities:

```
ACTION       OBJECT            RESPONSIBILITY
Create    +  UI Mockups     =  Create UI Mockups
Review    +  Code           =  Review Code
Generate  +  Sales Leads    =  Generate Sales Leads
Edit      +  AI Video =  Edit AI Video
```

**Usage:**
- Assign clear responsibilities to team members
- Define role requirements
- Create job descriptions

---

### 3. The Skill Development Path

**Responsibility + Tool = Skill**

Skills emerge from responsibilities performed with specific tools:

```
RESPONSIBILITY          TOOL        SKILL
Create UI Mockups    +  Figma    =  UI Design (Figma)
Review Code          +  GitHub   =  Code Review (GitHub PR)
Generate Leads       +  Apollo   =  Lead Generation (Apollo.io)
Edit Videos          +  Premiere =  Video Editing (Premiere Pro)
```

**Application:**
- Training plans (which tools to learn)
- Skill assessments
- Hiring requirements

---

### 4. The Profession Mapping

**Professions have typical:**
- **Responsibilities** (What they do)
- **Skills** (How proficient they are)
- **Tools** (What they use)
- **Processes** (Workflows they follow)

```
UI/UX DESIGNER
├── Responsibilities: Create mockups, Design prototypes, Conduct user research
├── Skills: UI Design, UX Design, Figma proficiency, User research
├── Tools: Figma (primary), Adobe XD, FigJam, Miro
└── Processes: UI/UX Design Process, Design System Workflows
```

---

## Secondary Library Relationships

### Products → Services Categorization

**Products** (39 specific offerings) are categorized into **Services** (7 categories):

```
SERVICES (Categories)        PRODUCTS (Specific Offerings)
Design Services       →      Logo Design, Website Design, UI/UX Design, etc.
Video Services        →      Explainer Video, YouTube Editing, Social Media Videos
Lead Generation       →      Lead Lists, LinkedIn Campaigns, Email Outreach
Development Services  →      Web Development, API Integration, Automation
Content Services      →      Blog Posts, Social Media Content, Copywriting
AI Services    →      SMM Management, Paid Ads, Email AI
SEO Services          →      On-page SEO, Technical SEO, Link Building
```

**Usage:**
- Sales positioning
- Service catalog organization
- Pricing structure

---

### Tools → Professions → Departments Mapping

**Tools** are used by specific **Professions** in certain **Departments**:

```
TOOL                 PROFESSION           DEPARTMENT
Figma           →    UI/UX Designer   →   Design
VS Code         →    Frontend Developer → Dev
Apollo.io       →    Lead Generator    →  LG
Premiere Pro    →    Video Editor      →  Video
Claude Desktop  →    Prompt Engineer   →  AI
```

**Usage:**
- Tool provisioning
- Team onboarding
- Technology stack planning

---

### Parameters → All Libraries (Universal Applicability)

**Parameters** apply to all other libraries as quality/process standards:

```
PARAMETERS                    APPLIES TO
Design Quality (8/10 min) → Objects (Design deliverables)
Code Quality Standards     → Actions (Development actions)
Data Accuracy (>90%)       → Results (LG outcomes)
Response Time (<24h)       → Processes (Communication workflows)
Tool Proficiency           → Tools (All tool usage)
```

**Usage:**
- Quality assurance
- Performance evaluation
- Process improvement

---

## Library Integration Levels

### Heavy Integration (Core to Operations)

**Actions, Processes, Results:**
- Used in EVERY meeting analysis
- Core workflow documentation
- Essential for action item tracking

**Where:** All output templates, all department meetings

---

### Moderate Integration (Frequently Used)

**Tools, Professions, Skills:**
- Used in most technical/project meetings
- Important for context and assignments
- Critical for team meetings

**Where:** Technical discussions, team planning, resource allocation

---

### Light Integration (Contextual)

**Products, Services, Parameters:**
- Used in specific contexts (sales, quality discussions)
- Provide standards and references
- Important but not always active

**Where:** Sales meetings, quality reviews, strategic planning

---

### Reference Integration (As-Needed)

**Responsibilities, Prompts:**
- Derived/computed from other libraries
- Referenced when clarifying roles or automation
- Not actively searched in transcripts

**Where:** Organizational planning, role definition, automation design

---

## ID Format Conventions

### Standardized ID Formats Across Libraries

| Library | ID Format | Example | Notes |
|---------|-----------|---------|-------|
| Actions | ACT-XXX or ACT-CATEGORY-XXX | ACT-DESIGN-001 | Category prefix optional |
| Objects | OBJ-XXX or OBJ-CATEGORY-XXX | OBJ-VID-001 | Category for specialized |
| Processes | PROC-XXX or PROC-DEPT-XXX | PROC-LG-001 | Department prefix common |
| Results | RESULT-XXX or RES-XXX | RESULT-LG-001 | Both formats used |
| Skills | SKL-XXX or SKL-DEPT-XXX | SKL-DESIGN-001 | Department for specialized |
| Responsibilities | RESP-XXX or RESP-DEPT-XXX | RESP-HR-001 | Often department-specific |
| Products | PDT-XXX or PDT-TYPE-XXX | PDT-D-001 | Type: D=Design, V=Video, etc. |
| Services | SVC-XXX | SVC-002 | Simple numeric |
| Parameters | PARAM-XXX or PARAM-DEPT-XXX | PARAM-DEV-001 | Department-specific common |
| Professions | PROF-XXX | PROF-025 | Simple numeric |
| Tools | TOOL-XXX or TOOL-CATEGORY-XXX | TOOL-AI-001 | Category prefix common |
| Prompts | PROMPT-XXX or PROMPT-TYPE-XXX | PROMPT-CORE-001 | Type: CORE, AI, DEV, etc. |

**Consistency Principle:** All IDs follow LIBRARY-CATEGORY-NUMBER format for easy recognition and filtering.

---

## Cross-Reference Patterns

### How Libraries Reference Each Other

**In Actions Library:**
```json
{
  "action_id": "ACT-DESIGN-001",
  "action_name": "Create UI mockups",
  "typical_object": "OBJ-DESIGN-002 (High-fidelity mockups)",
  "part_of_process": "PROC-DESIGN-001 (UI/UX Design Process)",
  "expected_result": "RESULT-001 (Designs completed)",
  "required_skill": "SKL-DESIGN-001 (UI/UX Design)",
  "primary_tool": "TOOL-DESIGN-001 (Figma)"
}
```

**In Processes Library:**
```json
{
  "process_id": "PROC-DEV-001",
  "process_name": "Feature Development Workflow",
  "actions_involved": ["ACT-DEV-001", "ACT-DEV-002", ...],
  "deliverable_objects": ["OBJ-DEV-005 (React Component)"],
  "expected_results": ["RESULT-DEV-001 (Feature deployed)"],
  "required_professions": ["PROF-009 (Frontend Developer)"],
  "tools_used": ["TOOL-DEV-001 (VS Code)", "TOOL-DEV-002 (GitHub)"],
  "quality_parameters": ["PARAM-DEV-008 (Test coverage >80%)"]
}
```

---

## Integration Philosophy

### Design Principles

**1. Modularity**
- Each library is independent
- Can be updated separately
- Department-specific subsets possible

**2. Interconnectedness**
- Libraries reference each other
- Relationships are bidirectional
- Cross-referencing maintains consistency

**3. Scalability**
- New entities can be added
- Libraries can grow independently
- System adapts to organizational changes

**4. Practical Use**
- Designed for real-world application
- Meeting transcript analysis
- Project planning and tracking

**5. AI-First**
- Optimized for AI processing
- Structured data formats
- Clear recognition patterns

---

## How MAIN_PROMPT Uses the Taxonomy

### Meeting Analysis Workflow

**Step 1: Identify Department** (Use Professions)
- Match participants to Employee Directory
- Determine which department library to load

**Step 2: Recognize Actions** (Use Actions Library)
- "We need to create mockups" → ACT-DESIGN-001
- "Fix the authentication bug" → ACT-DEV-004

**Step 3: Match Objects** (Use Objects Library)
- "The landing page design" → OBJ-DESIGN-015
- "Lead list for SaaS companies" → OBJ-LG-001

**Step 4: Identify Processes** (Use Processes Library)
- "Starting the design review phase" → PROC-DESIGN-001 (Step 4)
- "Deploying to production tomorrow" → PROC-DEV-001 (Step 7)

**Step 5: Map to Professions** (Use Professions Library)
- "Olha is handling the UI work" → PROF-025 (UI/UX Designer)
- "Yaroslav will code this" → PROF-009 (Frontend Developer)

**Step 6: Note Tools** (Use Tools Library)
- "Figma file is ready" → TOOL-DESIGN-001
- "Pushed to GitHub" → TOOL-DEV-002

**Step 7: Track Results** (Use Results Library)
- "Completed 5 landing pages this week" → RESULT-001
- "95% email deliverability achieved" → RESULT-LG-002

**Step 8: Apply Parameters** (Use Parameters Library)
- Check if quality standards met
- Verify process adherence
- Flag deviations

---

## Department-Specific Library Loading

### Selective Loading Strategy

**Instead of loading all 12 libraries for every meeting:**

```
HR Meeting:
- Load: Common + HR Libraries
- Includes: Professions (FULL), Recruitment Actions, HR Processes
- Skip: Tools (75+ dev tools not needed)

Design Meeting:
- Load: Common + Design Libraries
- Includes: Design Objects, Design Actions, Creative Tools
- Skip: Data_Operations (scraping not relevant)

Dev Meeting:
- Load: Common + Dev Libraries
- Includes: Tools (FULL), Dev Actions, Development Processes
- Skip: Services/Products (sales-focused)

LG Meeting:
- Load: Common + LG Libraries
- Includes: Data_Operations (FULL), LG Tools, Lead Gen Processes
- Skip: Design Objects (creative deliverables not relevant)
```

**Benefits:**
- 40-70% reduction in prompt weight
- Only relevant libraries loaded
- Faster processing
- Better context management

---

## Library Statistics (Baseline 2025-11-15)

### Entity Counts

| Library | Entities | Verification Status |
|---------|----------|---------------------|
| Actions | 429 | ✅ Verified (master + Data_Operations) |
| Objects | 36 | ✅ Verified (4 collections) |
| Processes | 428 | ✅ Verified (master + Workflows) |
| Results | 432 | ✅ Verified (master) |
| Skills | 12+ | ⚠️ Approximate (dept files) |
| Responsibilities | Formula | ✅ Verified (Action + Object) |
| Products | 39 | ✅ Verified (master + index) |
| Services | 7 | ✅ Verified (categories) |
| Parameters | 10,596+ | ✅ Verified (61,383 source lines) |
| Professions | 27 | ✅ Verified (all professions) |
| Tools | 75+ | ✅ Verified (categorized) |
| Prompts | Varies | ⚠️ Growing library |

**Total Entities:** ~12,000+ across all libraries

---

## Evolution & Maintenance

### How the Taxonomy Grows

**Adding New Entities:**
1. Identify gap (new action, tool, profession, etc.)
2. Assign ID following convention
3. Add to appropriate library file
4. Update cross-references
5. Update department library files if needed
6. Document in CHANGELOG

**Deprecating Entities:**
1. Mark as deprecated (don't delete immediately)
2. Note replacement entity
3. Update references
4. Archive after transition period

**Library Expansion:**
- New specialized files (e.g., Video_Generation_Objects.json)
- Department-specific subsets
- Integration with new tools/platforms

---

## Related Files

**Core Context:**
- [../00_Core/01_Purpose_Vision.md](../00_Core/01_Purpose_Vision.md) - How libraries work together
- [../00_Core/02_Company_Context.md](../00_Core/02_Company_Context.md) - Organizational structure

**Department Libraries (All Reference This Framework):**
- [00_Common_Libraries.md](00_Common_Libraries.md) - Universal libraries
- [01_HR_Libraries.md](01_HR_Libraries.md) through [07_LG_Libraries.md](07_LG_Libraries.md) - Dept-specific
- [08_Parameters_Lightweight.md](08_Parameters_Lightweight.md) - Standards overview

**Integration Guide:**
- [README.md](README.md) - Department-to-library mapping matrix
- [../04_Usage/01_Usage_Instructions.md](../04_Usage/01_Usage_Instructions.md) - How to use taxonomy

---

## Quick Reference

### Most Important Relationships

**For Action Items:**
- Actions + Objects = Responsibilities
- Actions + Professions = Task Assignments

**For Quality:**
- Parameters → All Libraries
- Quality standards apply universally

**For Workflows:**
- Actions → Processes → Results
- Complete lifecycle tracking

**For Team Context:**
- Professions → Skills → Tools
- Employee → Role → Capabilities → Technology

**For Sales:**
- Products → Services
- Specific offerings → Category

---

## Key Takeaways

**1. Interconnected System**
- 12 libraries work together
- Relationships are bidirectional
- Cross-referencing maintains consistency

**2. Department-Based Organization**
- Libraries organized by department need
- Selective loading reduces prompt weight
- Maintains completeness across all files

**3. Practical Application**
- Designed for meeting analysis
- Action item tracking
- Project documentation

**4. Scalable Architecture**
- Can add new entities
- Libraries grow independently
- Adapts to organizational changes

**5. AI-Optimized**
- Structured for AI processing
- Clear recognition patterns
- Efficient context management

---

**Status:** ✅ Complete - System architecture & library relationships reference
