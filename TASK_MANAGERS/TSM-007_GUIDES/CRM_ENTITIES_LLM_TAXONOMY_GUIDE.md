# CRM Entities & LLM Taxonomy - Complete Implementation Guide
**Version:** 1.0  
**Created:** November 9, 2025  
**Purpose:** Comprehensive explanation of CRM entity architecture, LLM taxonomy structure, and real-world Remote Helpers applications

---

## 📋 Table of Contents

1. [Executive Overview](#executive-overview)
2. [Taxonomy Structure](#taxonomy-structure)
3. [CRM Entity Architecture](#crm-entity-architecture)
4. [LLM Version Evolution](#llm-version-evolution)
5. [Real-World Examples](#real-world-examples)
6. [Task Manager System](#task-manager-system)
7. [Implementation Patterns](#implementation-patterns)

---

## 🎯 Executive Overview

### What This System Solves

Remote Helpers operates across **4 business platforms** with **32 employees** in **7 departments**. Without a structured system, this creates:

**Problems:**
- 🔴 Task naming chaos (everyone describes work differently)
- 🔴 Lost institutional knowledge (expertise locked in individual minds)
- 🔴 Inefficient onboarding (new hires struggle to understand processes)
- 🔴 Difficulty scaling (can't multiply success patterns)
- 🔴 AI agents can't help (unstructured data is invisible to automation)

**Solution:**
This framework provides a **Taxonomic Operating System** that normalizes how work is described, stored, and executed.

### Core Principle

Everything follows the formula:

```
DEPARTMENTS → RESPONSIBILITIES → (ACTIONS + OBJECTS) → TASKS
```

**Translation to Human Language:**
1. **Department** = Who does the work (HR, Design, Dev, LG, Sales, AI, Video)
2. **Responsibilities** = What outcomes they own
3. **Actions** = Verbs describing how work happens (Create, Send, Analyze, Update)
4. **Objects** = Nouns describing what is worked on (Job Posting, Email, Video CV)
5. **Tasks** = Specific work items combining Actions + Objects + Tools

---

## 🏛️ Taxonomy Structure

### Level 1: Departments

**Definition:** Organizational units with distinct functions

**Remote Helpers Departments:**

```
┌─────────────────────────────────────────────────┐
│              DEPARTMENTS                         │
├─────────────────────────────────────────────────┤
│                                                  │
│  👥 HR (Managers)          - Recruitment & People│
│  🤖 AI                     - Automation & LLMs   │
│  🎬 Video                  - Production & Editing│
│  💼 Sales                  - Client Relations    │
│  🎨 Design                 - Creative Services   │
│  💻 Dev (Developers)       - Engineering         │
│  📊 LG (Lead Generation)   - Prospecting         │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Example:** 
- HR Department owns all recruitment and employee management activities
- LG Department owns all lead generation and prospecting activities

---

### Level 2: Professions

**Definition:** Job roles within departments with specific skill requirements

**Structure:**
```json
{
  "Professions": "recruiter",
  "Departments": "managers"
}
```

**Remote Helpers Examples:**

| Department | Professions |
|------------|-------------|
| **Managers (HR)** | HR Manager, Recruiter |
| **Developers** | Frontend Developer, Backend Developer, Full Stack Developer, QA Engineer |
| **Marketers (LG)** | Lead Generator, SMM Manager |
| **Designers** | UI/UX Designer, Graphic Designer, 3D Designer, Animator |
| **Sales** | Sales Manager, Account Manager |
| **Video** | Video Editor, Motion Designer, Animator |
| **AI** | AI Engineer, Prompt Engineer, Automation Specialist |

**Real-World Example:**
- **Profession:** "Recruiter"
- **Department:** "Managers" (HR)
- **Responsibilities:** Finding, screening, and hiring talent

---

### Level 3: Responsibilities

**Definition:** High-level outcomes that professions are accountable for

**Formula:** `Responsibilities = Actions + Objects`

**Structure:**
```
Responsibilities:
├── Manage candidate pipeline
├── Conduct screening interviews
├── Negotiate salary offers
└── Onboard new hires
```

**Recruiter Responsibilities Example:**

```yaml
Profession: Recruiter
Department: Managers (HR)
Responsibilities:
  - Manage Candidate Pipeline:
      Actions: [Screen, Evaluate, Track, Update]
      Objects: [Candidates, Resumes, Applications, Interviews]
  
  - Conduct Hiring Process:
      Actions: [Schedule, Conduct, Record, Assess]
      Objects: [Interviews, Video Calls, Assessments, Feedback]
  
  - Negotiate Employment Terms:
      Actions: [Discuss, Propose, Adjust, Finalize]
      Objects: [Salary, Benefits, Contracts, Offers]
  
  - Onboard New Employees:
      Actions: [Send, Schedule, Guide, Track]
      Objects: [Onboarding Materials, Training, Access, Checklist]
```

**Real-World Scenario:**

**Without Taxonomy:**
- "I need to do some stuff with the new candidates"
- "Follow up on those people from last week"
- "Make sure the contracts are ready"

**With Taxonomy:**
- **Responsibility:** "Manage Candidate Pipeline"
- **Specific Tasks:**
  - Screen: Candidate Resumes
  - Conduct: Video Interview
  - Update: CRM Database
  - Send: Job Offer Email

---

### Level 4: Actions

**Definition:** Standardized verbs describing work activities

**Categories:**

#### Communication Actions
```json
{
  "Actions": "send",
  "Processes": "sending",
  "Results": "sent",
  "Departments": "managers",
  "Professions": "recruiter"
}
```

**Examples:**
- Send (sending → sent)
- Reply (replying → replied)
- Forward (forwarding → forwarded)
- Draft (drafting → drafted)
- Schedule (scheduling → scheduled)

#### Creation Actions
```json
{
  "Actions": "create",
  "Processes": "creating",
  "Results": "created",
  "Departments": "developers",
  "Professions": "frontend developer"
}
```

**Examples:**
- Create (creating → created)
- Generate (generating → generated)
- Develop (developing → developed)
- Design (designing → designed)
- Build (building → built)

#### Analysis Actions
```json
{
  "Actions": "analyze",
  "Processes": "analyzing",
  "Results": "analyzed",
  "Departments": "managers",
  "Professions": "lead generator"
}
```

**Examples:**
- Analyze (analyzing → analyzed)
- Review (reviewing → reviewed)
- Evaluate (evaluating → evaluated)
- Assess (assessing → assessed)
- Monitor (monitoring → monitored)

#### Management Actions
**Examples:**
- Update (updating → updated)
- Organize (organizing → organized)
- Archive (archiving → archived)
- Track (tracking → tracked)
- Coordinate (coordinating → coordinated)

---

### Level 5: Objects

**Definition:** Business entities that actions operate on

**Categories:**

#### Communications Objects
```json
{
  "Objects": "communications",
  "Object Types": "first connection, update, follow-up, feedback, faq, onboarding",
  "Professions": "recruiter",
  "Departments": "managers"
}
```

**Examples:**
- Email (Cold Email, Follow-up Email, Offer Email)
- Message (LinkedIn Message, Discord Message)
- Call (Phone Call, Video Call)
- Notification (Discord Chanel Alert, Direct Message Reminder)

#### Documents Objects
```json
{
  "Objects": "contracts",
  "Object Types": "employees contracts, presale contract, content creator agreement, clients agreements",
  "Professions": "recruiter",
  "Departments": "managers"
}
```

**Examples:**
- Contract (Employment Contract, Client Agreement)
- Resume (PDF Resume, Video CV)
- Report (Daily Report, Monthly Report)
- Proposal (Client Proposal, Project Proposal)

#### Data Objects
```json
{
  "Objects": "databases",
  "Object Types": "candidates database, employees database, presale database",
  "Professions": "recruiter",
  "Departments": "managers"
}
```

**Examples:**
- Database (CRM, Candidates DB, Clients DB)
- Record (Employee Record, Client Record)
- Profile (Talent Profile, Company Profile)
- Entry (Database Entry, Log Entry)

#### Design Deliverables
```json
{
  "Objects": "logo",
  "Object Types": "brand identity, icon set, favicon",
  "Professions": "graphic designer",
  "Departments": "designers"
}
```

**Examples:**
- Logo (Brand Logo, App Icon)
- UI Mockup (Web Mockup, Mobile Mockup)
- Presentation (Client Deck, Pitch Deck)
- Social Media Post (Instagram Post, LinkedIn Banner)

---

### Level 6: Tools

**Definition:** Software, platforms, and AI services used to complete tasks

**Categories:**

#### AI Tools
```json
{
  "Tools": "Claude",
  "Tool Type": "AI Assistant",
  "Responsibilities": "Content generation, code review, research",
  "Primary Users": "AI Department, Developers, Managers"
}
```

**Remote Helpers Stack:**
- **Claude** (Anthropic) - Primary AI assistant for all departments
- **ChatGPT** (OpenAI) - Alternative AI assistant
- **Midjourney** - AI image generation for designers
- **Leonardo.ai** - AI art generation
- **ElevenLabs** - AI voice generation for video team

#### Automation Tools
```json
{
  "Tools": "n8n",
  "Category": "Workflow Automation",
  "Time Saved": "4-5 hours/day per LG employee",
  "Primary Users": "Lead Generation Department"
}
```

#### Design Tools
```json
{
  "Tools": "Figma",
  "Category": "UI/UX Design",
  "Projects": "31+ active projects",
  "Primary Users": "Design Department (9 designers)"
}
```

**Remote Helpers Stack:**
- Figma - UI/UX design
- Adobe Photoshop - Image editing
- Adobe Illustrator - Vector graphics
- Canva - Quick design work
- Miro - Collaboration

#### Development Tools
```json
{
  "Tools": "Cursor",
  "Category": "AI-Powered IDE",
  "Primary Users": "Developers, Managers"
}
```

#### Communication Tools
```json
{
  "Tools": "Discord",
  "Category": "Team Communication",
  "Team Size": "32 members",
  "Primary Users": "All departments"
}
```

---

## 🏗️ CRM Entity Architecture

### The 8 Core Entities

```
┌─────────────────────────────────────────────────────────┐
│                    ENTITY UNIVERSE                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │   JOBS   │  │BUSINESSES│  │ TALENTS  │             │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘             │
│       │             │              │                    │
│       └─────────────┴──────────────┘                   │
│                     │                                   │
│              ┌──────▼──────┐                           │
│              │TASK_MANAGERS│                           │
│              └──────┬──────┘                           │
│                     │                                   │
│       ┌─────────────┼─────────────┐                   │
│       │             │             │                    │
│  ┌────▼────┐  ┌────▼────┐  ┌────▼────┐              │
│  │LIBRARIES│  │ SETTINGS│  │CATEGORIES│              │
│  └─────────┘  └─────────┘  └─────────┘              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Entity 1: JOBS (Talent Marketplace)

**Purpose:** Manage open positions, job requirements, and talent matching

**Sub-Entities:**
```
JOBS/
├── Job_Postings/           # Active job listings
│   ├── Active/             # Currently hiring
│   ├── Archived/           # Filled positions
│   └── Templates/          # Reusable job templates
│
├── Job_Requirements/       # Skill requirements
│   ├── Experience_Levels/  # Junior, Mid, Senior
│   └── Skills_Matrices/    # Required vs preferred skills
│
└── Job_Categories/         # Job classification
    ├── Design/             # Design roles
    ├── IT/                 # Developer roles
    ├── Marketing/          # LG & Sales roles
    └── Operations/         # HR & Admin roles
```

**Real-World Example:**

**Job Posting: Frontend Developer**
```yaml
Entity: JOBS
Sub-Entity: Job_Postings/Active/
File: Frontend_Developer_2025_11_09.json

Data Structure:
  position_title: "Frontend Developer"
  department: "Developers"
  profession: "Frontend Developer"
  experience_level: "Mid-Level (2-4 years)"
  
  required_skills:
    - React.js
    - TypeScript
    - CSS/SCSS
    - Git
  
  preferred_skills:
    - Next.js
    - Tailwind CSS
    - State management (Redux/Zustand)
  
  tools:
    - VS Code or Cursor IDE
    - Figma (for design handoff)
    - GitHub
  
  responsibilities:
    - Develop UI components
    - Implement responsive designs
    - Integrate APIs
    - Code reviews
  
  salary_range:
    currency: "USD"
    min: 2000
    max: 3500
    period: "monthly"
  
  work_arrangement: "Remote"
  timezone: "GMT+2 (overlap required)"
  
  application_process:
    1: "Submit resume via job board"
    2: "Complete technical assessment"
    3: "Video interview with HR"
    4: "Technical interview with Dev lead"
    5: "Offer negotiation"
```

**Generated Tasks from this Job Posting:**
```
1. Create: Job Posting (for Frontend Developer) [HR]
2. Post: Job Advertisement (on LinkedIn, DOU, Djinni) [HR]
3. Screen: Candidate Resumes (filter by React/TypeScript) [HR]
4. Schedule: Technical Interview (with Yaroslav Klimenko) [HR]
5. Assess: Coding Skills (via test project) [Dev]
6. Conduct: Video Interview (behavioral questions) [HR]
7. Prepare: Job Offer Letter (with salary details) [HR]
8. Send: Offer Email (to selected candidate) [HR]
```

---

### Entity 2: BUSINESSES (Client Lifecycle)

**Purpose:** Track business relationships from prospect to client

**Sub-Entities:**
```
BUSINESSES/
├── Prospects/              # Early-stage leads
│   ├── Pipeline_Stage_Early/
│   ├── Pipeline_Stage_Qualification/
│   └── Research_Notes/
│
├── Companies/              # All business entities
│   ├── Active_Clients/
│   └── Company_Profiles/
│
├── Clients/                # Active customers
│   ├── Active_Projects/
│   └── Contract_Documents/
│
└── Ex_Clients/             # Former customers
    ├── Historical_Projects/
    └── Reengagement_Queue/
        ├── High_Priority/
        ├── Medium_Priority/
        └── Low_Priority/
```

**Real-World Example:**

**Client Lifecycle: TechStartup Inc.**

```yaml
Entity: BUSINESSES
Lifecycle Stages:

# Stage 1: PROSPECT
File: Prospects/Pipeline_Stage_Early/TechStartup_Inc_2025_01_15.json
Status: "New Lead"
Source: "LinkedIn prospecting"
Company: "TechStartup Inc"
Industry: "SaaS"
Size: "50-100 employees"
Decision_Maker:
  name: "John Smith"
  title: "CTO"
  email: "john@techstartup.com"
Initial_Contact: "2025-01-15"
Lead_Score: 75/100
Next_Action: "Send initial connection request"

# Stage 2: QUALIFICATION (after response)
File: Prospects/Pipeline_Stage_Qualification/TechStartup_Inc_2025_01_20.json
Status: "Qualified Lead"
Budget_Range: "$5,000-10,000/month"
Timeline: "Q1 2025"
Pain_Point: "Need to scale development team quickly"
Solution_Fit: "High - we can provide Frontend + Backend devs"
Next_Action: "Schedule discovery call"

# Stage 3: ACTIVE CLIENT
File: Clients/Active_Clients/TechStartup_Inc_2025_02_01.json
Status: "Active Client"
Contract_Start: "2025-02-01"
Contract_Value: "$8,000/month"
Active_Projects:
  - Project_ID: "PROJ-2025-034"
  - Project_Name: "React Dashboard Development"
  - Assigned_Talents:
      - "Klimenko Yaroslav" (Frontend Developer)
      - "Kizilova Olha" (QA Engineer)
Monthly_Recurring_Revenue: "$8,000"
Satisfaction_Score: "9/10"
Next_Review: "2025-05-01"

# Stage 4: EX-CLIENT (if contract ends)
File: Ex_Clients/Reengagement_Queue/High_Priority/TechStartup_Inc_2025_08_01.json
Status: "Former Client"
Contract_End: "2025-07-31"
Reason_for_Exit: "Project completed successfully"
Total_Revenue_Generated: "$48,000"
Reengagement_Priority: "HIGH"
Reengagement_Opportunity: "New project phases, additional services"
Last_Contact: "2025-08-01"
Next_Touchpoint: "2025-11-01 (3-month check-in)"
Reengagement_Cost: "$100 (vs $3,000 new client acquisition)"
```

**Generated Tasks for Client Lifecycle:**

```
# PROSPECT STAGE
1. Search: Company Profiles (in LinkedIn) [LG]
2. Scrape: Contact Information (via automation) [LG]
3. Send: Cold Email (introduction) [LG/Sales]
4. Track: Email Open Rate (in CRM) [LG]
5. Send: Follow-up Message (after 3 days) [LG]

# QUALIFICATION STAGE
6. Schedule: Discovery Call (with CTO) [Sales]
7. Conduct: Needs Assessment (BANT framework) [Sales]
8. Create: Custom Proposal (for 2 developers) [Sales]
9. Send: Proposal Email (with pricing) [Sales]
10. Follow-up: Proposal Discussion (answer questions) [Sales]

# CLIENT STAGE
11. Finalize: Service Agreement (contract) [Sales/HR]
12. Assign: Development Team (2 talents) [HR]
13. Schedule: Kickoff Meeting (with client) [Sales/Dev]
14. Create: Project Brief (requirements doc) [Dev]
15. Set up: Communication Channel (Discord/Slack) [Dev]
16. Track: Project Milestones (in Task Manager) [Dev]
17. Send: Monthly Progress Report (to client) [Sales]

# EX-CLIENT STAGE
18. Send: Thank You Email (project completion) [Sales]
19. Request: Client Testimonial (for portfolio) [Sales]
20. Update: CRM Status (move to ex-clients) [Sales]
21. Schedule: 3-Month Check-in (calendar reminder) [Sales]
22. Send: Reengagement Email (new offerings) [Sales]
23. Offer: Referral Incentive (discount code) [Sales]
```

---

### Entity 3: TALENTS (Human Capital)

**Purpose:** Manage people from application through employment

**Sub-Entities:**
```
TALENTS/
├── Job_Applications/       # Submitted applications
│   ├── New_Applications/
│   ├── Under_Review/
│   └── Archived/
│
├── Candidates/             # In hiring pipeline
│   ├── Interview_Stage/
│   ├── Technical_Assessment/
│   └── Offers_Extended/
│
├── Employees/              # Hired team members (32 current)
│   ├── employees_rack_system.json
│   └── employees_tasks_profiles.json
│
└── Presales/               # Client-ready talent
    ├── Client_Ready_Profiles/
    ├── Portfolios/
    └── Video_CVs/
```

**Real-World Example:**

**Talent Lifecycle: Maria Ivanova (Designer)**

```yaml
Entity: TALENTS

# Stage 1: JOB APPLICATION
File: Job_Applications/New_Applications/Maria_Ivanova_2025_01_10.json
Application_Date: "2025-01-10"
Position_Applied: "UI/UX Designer"
Source: "Behance portfolio outreach"
Resume_Link: "drive.google.com/maria-resume"
Portfolio_Link: "behance.net/maria-ivanova"
Cover_Letter_Highlights:
  - "3 years experience in SaaS design"
  - "Proficient in Figma, Adobe XD"
  - "Case study: Mobile banking app redesign"
Initial_Screening_Score: 85/100
Next_Action: "Schedule screening call"

# Stage 2: CANDIDATE (in pipeline)
File: Candidates/Interview_Stage/Maria_Ivanova_2025_01_15.json
Status: "Interview Stage"
Screening_Call_Date: "2025-01-15"
Screening_Call_Notes:
  - "Strong portfolio, especially mobile design"
  - "Good communication skills"
  - "Available to start in 2 weeks"
  - "Salary expectation: $2,500/month"
Skills_Assessment:
  Figma: "Expert"
  Adobe Illustrator: "Advanced"
  User Research: "Intermediate"
  Prototyping: "Expert"
Technical_Test: "Assigned: Redesign landing page"
Technical_Test_Due: "2025-01-20"
Next_Action: "Review technical test, schedule final interview"

# Stage 3: EMPLOYEE (after hiring)
File: Employees/Active/Maria_Ivanova_2025_02_01.json
Employee_ID: "EMP-2025-033"
Full_Name: "Maria Ivanova"
Department: "Design"
Profession: "UI/UX Designer"
Start_Date: "2025-02-01"
Employment_Type: "Full-time"
Salary: "$2,500/month"
Tools_Access:
  - "Figma (Professional plan)"
  - "Adobe Creative Cloud"
  - "Discord (Team workspace)"
  - "Google Workspace"
  - "Miro (collaboration)"
Current_Projects:
  - Project_1: "DGN Platform redesign"
  - Project_2: "Client X mobile app"
Skills_Matrix:
  Primary: ["UI Design", "UX Design", "Figma"]
  Secondary: ["Illustration", "Branding", "User Research"]
Performance_Rating: "N/A (new hire)"
Mentor: "Shelep Olha (Lead Designer)"

# Stage 4: PRESALES (when ready for client presentation)
File: Presales/Client_Ready_Profiles/Maria_Ivanova_2025_03_01.json
Status: "Available for Presales"
Profile_Updated: "2025-03-01"
Video_CV_Link: "youtube.com/maria-cv"
Portfolio_Showcase: "behance.net/maria-rh-portfolio"
Case_Studies:
  - "E-commerce platform redesign (+35% conversion)"
  - "Mobile banking app (4.8★ app store rating)"
  - "SaaS dashboard optimization"
Client_Presentation_Materials:
  - "One-page designer profile"
  - "3-minute video introduction"
  - "Top 5 projects showcase"
Availability: "Can start new projects within 1 week"
Rate_for_Clients: "$35/hour"
Ideal_Client_Match:
  - "SaaS companies"
  - "Mobile app projects"
  - "E-commerce platforms"
```

**Generated Tasks for Talent Lifecycle:**

```
# APPLICATION STAGE
1. Receive: Job Application (via email) [HR]
2. Screen: Resume (check qualifications) [HR]
3. Review: Portfolio (assess design skills) [HR + Design Lead]
4. Schedule: Screening Call (with candidate) [HR]
5. Update: CRM Status (move to candidate stage) [HR]

# CANDIDATE STAGE
6. Conduct: Video Interview (behavioral questions) [HR]
7. Assign: Technical Test (redesign exercise) [Design Lead]
8. Review: Test Submission (evaluate design) [Design Lead]
9. Schedule: Final Interview (with team) [HR]
10. Discuss: Salary Offer (negotiate terms) [HR]
11. Send: Offer Letter (with contract) [HR]
12. Receive: Signed Contract (from candidate) [HR]

# EMPLOYEE STAGE
13. Create: Employee Account (in systems) [HR/IT]
14. Grant: Tool Access (Figma, Adobe, etc.) [IT]
15. Send: Welcome Email (with onboarding checklist) [HR]
16. Schedule: First Day Orientation (team intro) [HR]
17. Assign: Mentor (Olha Shelep) [Design Lead]
18. Create: Onboarding Tasks (in Task Manager) [HR]
19. Track: 30-60-90 Day Goals (performance) [HR + Design Lead]

# PRESALES STAGE
20. Create: Video CV (for client presentations) [Video Team]
21. Update: Portfolio (with RH projects) [Designer + Marketing]
22. Create: One-Page Profile (showcase sheet) [HR + Design]
23. Add: to Presales Database (client-ready talents) [HR]
24. Match: with Client Projects (based on skills) [Sales]
25. Send: Talent Profile (to prospective clients) [Sales]
```

---

### Entity 4: TASK_MANAGERS (Operational Engine)

**Purpose:** Orchestrate work execution and track performance

**Sub-Entities:**
```
TASK_MANAGERS/
├── Task_Templates/          # Reusable task configs
│   ├── By_Department/       # HR, Dev, LG, Design, etc.
│   ├── By_Action/           # Create, Send, Analyze, etc.
│   └── By_Object/           # Email, Video_CV, Report, etc.
│
├── Project_Workflows/       # Workflow definitions
│   └── Projects_List_2025.md
│
├── Milestone_Tracking/      # Project milestones
│   ├── Project_Milestones/
│   └── Sprint_Goals/
│
└── Performance_Metrics/     # KPIs and metrics
    ├── Department_Dashboards/
    ├── Individual_Performance/
    └── Team_Velocity/
```

**Task Structure Formula:**
```
Task = ACTION + OBJECT + [TOOL] + [CONTEXT]

Examples:
- Create + Job Posting + [Notion] + [for Frontend Developer]
- Send + Cold Email + [Gmail] + [to 50 prospects]
- Analyze + Lead Data + [Google Sheets] + [daily report]
- Design + UI Mockup + [Figma] + [for Client X]
- Update + CRM Database + [CRM] + [candidate status]
```

**Real-World Example:**

**Task Template: Send Cold Email (Lead Generation)**

```yaml
Entity: TASK_MANAGERS
Sub-Entity: Task_Templates/By_Department/LG_Tasks/

Template_Name: "Send_Cold_Email_Outreach"
Template_ID: "TASK-LG-001"

Structure:
  Action: "Send"
  Object: "Cold Email"
  Tool: "Gmail + n8n automation"
  Department: "Lead Generation"
  Profession: "Lead Generator"

Task_Variants:
  - "Send cold email to IT companies"
  - "Send cold email to design agencies"
  - "Send cold email to startup founders"

Prerequisites:
  - "Search: Company list (via LinkedIn)"
  - "Scrape: Contact emails (via Hunter.io)"
  - "Create: Email copy (with value proposition)"

Task_Steps:
  1. "Open Gmail"
  2. "Use email template from Google Docs"
  3. "Personalize: Company name, pain point"
  4. "Add: Value proposition (how RH can help)"
  5. "Include: CTA (schedule call link)"
  6. "Send email"
  7. "Log in CRM: Email sent date"
  8. "Schedule: Follow-up reminder (3 days)"

Success_Criteria:
  - "Email delivered (not bounced)"
  - "Logged in CRM"
  - "Follow-up reminder set"

Performance_Metrics:
  - "Emails sent per day: 50+ (minimum)"
  - "Open rate: >30%"
  - "Reply rate: >5%"
  - "Meeting booking rate: >2%"

Time_Estimate:
  - "2 minutes per email"
  - "50 emails = 100 minutes (~1.5 hours)"

Automation_Opportunity:
  - "Use n8n to bulk send with personalization"
  - "Auto-log sends to CRM"
  - "Auto-schedule follow-ups"
  - "Time saved: 4-5 hours/day"

Related_Tasks:
  - Parent: "Run lead generation campaign"
  - Child: "Track email open rates"
  - Child: "Send follow-up email (if no response)"
  - Child: "Schedule discovery call (if positive response)"
```

---

### Entity 5: LIBRARIES (Knowledge Base)

**Purpose:** Centralized repository of reusable components

**Sub-Entities:**
```
LIBRARIES/
├── Actions/                # Standardized verbs
│   └── actions.json
│
├── Objects/                # Business entities
│   ├── Communications/
│   ├── Data/
│   ├── Documents/
│   ├── Media/
│   └── objects.json
│
├── Tools/                  # Software catalog
│   ├── AI_Tools/
│   ├── Automation_Tools/
│   ├── Design_Tools/
│   └── Development_Tools/
│
├── Professions/            # Job roles
│   └── professions.json
│
└── Responsibilities/       # Role duties
    ├── By_Department/
    ├── By_Role/
    └── responsibilities_library.json
```

This entity provides the **building blocks** for all other entities.

---

## 🔄 LLM Version Evolution

### Why Multiple LLM Versions?

As your organization grows and learns, the taxonomy must evolve. Different versions represent:

1. **LLM 1.0** - Initial basic structure
2. **LLM 2.0** - Refined with real-world usage
3. **LLM 7.0** - Current production version (most complete)

### LLM 7 - Current Production Version

**Source Files:**
- `LIBRARIES/Actions/actions.json` (from LLM7)
- `LIBRARIES/Objects/objects.json` (from LLM7)
- `LIBRARIES/Tools/tools.json` (from LLM7)
- `LIBRARIES/Professions/professions.json` (from LLM7)
- `LIBRARIES/Responsibilities/responsibilities_library.json` (from LLM7)

**Improvements over Earlier Versions:**
- ✅ More granular action definitions
- ✅ Department-specific object types
- ✅ Tool-task mappings (which tools for which tasks)
- ✅ Real company usage data integrated

---

## 🌍 Real-World Examples from Remote Helpers

### Example 1: Complete Workflow - Old Client Reengagement

**Business Context:**
- Reengaging old clients costs $100 (vs $1,000-3,000 for new clients)
- High-priority revenue opportunity
- 50+ ex-clients in database

**Entity Involvement:**

```
BUSINESSES (Ex_Clients)
    ↓
TASK_MANAGERS (Workflow Template)
    ↓
LIBRARIES (Actions + Objects + Tools)
    ↓
TALENTS (Sales Team)
```

**Step-by-Step Execution:**

```yaml
Workflow_Name: "Old_Client_Reengagement_Campaign"
Owner: "Sales Department (Kovalska Anastasiya)"

Phase 1: RESEARCH (Preparation)
  Task_1:
    Action: "Export"
    Object: "Ex-Client List"
    Tool: "CRM"
    Output: "Google Sheets with 50 ex-clients"
  
  Task_2:
    Action: "Analyze"
    Object: "Client History"
    Tool: "CRM + Google Sheets"
    Criteria: "Last project date, revenue generated, satisfaction score"
    Output: "Prioritized list (High/Medium/Low)"
  
  Task_3:
    Action: "Research"
    Object: "Company Updates"
    Tool: "LinkedIn + Google"
    Goal: "Find trigger events (funding, expansion, new products)"
    Output: "Notes on potential needs"

Phase 2: OUTREACH (First Contact)
  Task_4:
    Action: "Draft"
    Object: "Personalized Email"
    Tool: "Gmail + Google Docs template"
    Content:
      - Greeting with personal touch
      - Reference to past successful project
      - Acknowledge trigger event
      - Soft ask about current needs
      - CTA: "Would love to catch up"
  
  Task_5:
    Action: "Send"
    Object: "Reengagement Email"
    Tool: "Gmail"
    Volume: "10 emails per day (manageable personalization)"
  
  Task_6:
    Action: "Log"
    Object: "Email Send Date"
    Tool: "CRM"
    Purpose: "Track for follow-up timing"

Phase 3: FOLLOW-UP (Persistence)
  Task_7:
    Action: "Monitor"
    Object: "Email Opens"
    Tool: "Email tracking (if enabled)"
    Trigger: "If opened but no reply after 3 days"
  
  Task_8:
    Action: "Send"
    Object: "Follow-up Email"
    Tool: "Gmail"
    Timing: "3 days after first email"
    Content: "Gentle reminder, add value (case study, insight)"
  
  Task_9:
    Action: "Try"
    Object: "Alternative Channel"
    Tool: "LinkedIn"
    Timing: "5 days after follow-up email"
    Content: "Connect request with personalized note"

Phase 4: CONVERSION (Closing)
  Task_10:
    Action: "Schedule"
    Object: "Discovery Call"
    Tool: "Google Calendar + Calendly"
    Condition: "If positive response"
  
  Task_11:
    Action: "Conduct"
    Object: "Needs Assessment"
    Tool: "Zoom + Google Docs (notes)"
    Framework: "BANT (Budget, Authority, Need, Timeline)"
  
  Task_12:
    Action: "Create"
    Object: "Custom Proposal"
    Tool: "Google Docs + Figma (design)"
    Include: "Specific solution, pricing, timeline, team"
  
  Task_13:
    Action: "Send"
    Object: "Proposal Email"
    Tool: "Gmail"
    Attachments: "PDF proposal, portfolio samples"
  
  Task_14:
    Action: "Follow-up"
    Object: "Proposal Discussion"
    Tool: "Email or Call"
    Timing: "2 days after proposal sent"
    Goal: "Answer questions, negotiate"
  
  Task_15:
    Action: "Finalize"
    Object: "Service Agreement"
    Tool: "DocuSign or Email"
    Result: "Signed contract"

Phase 5: REACTIVATION (Success)
  Task_16:
    Action: "Update"
    Object: "CRM Status"
    Tool: "CRM"
    Change: "Ex-Client → Active Client"
  
  Task_17:
    Action: "Assign"
    Object: "Project Team"
    Tool: "Task Manager"
    Involve: "HR (for talent allocation)"
  
  Task_18:
    Action: "Schedule"
    Object: "Kickoff Meeting"
    Tool: "Google Calendar"
    Attendees: "Client, Sales, Project lead, Assigned talents"

Performance_Metrics:
  - "Emails sent: 50"
  - "Open rate: 32%"
  - "Response rate: 8%"
  - "Meetings scheduled: 4"
  - "Proposals sent: 3"
  - "Deals closed: 1"
  - "Revenue generated: $8,000/month"
  - "Cost of campaign: $100 (time + tools)"
  - "ROI: 8,000% (vs $3,000 new client acquisition cost)"
```

---

### Example 2: Designer Daily Workflow

**Entity:** TALENTS (Employee: Shelep Olha - Lead Designer)

**Department:** Design  
**Profession:** UI/UX Designer  
**Tools:** Figma (primary), Adobe Illustrator, Miro

**Daily Task Sequence:**

```yaml
Morning_Routine:
  Task_1:
    Time: "9:00 AM"
    Action: "Check"
    Object: "Discord Messages"
    Tool: "Discord"
    Purpose: "Review overnight client feedback"
  
  Task_2:
    Time: "9:15 AM"
    Action: "Review"
    Object: "Task List"
    Tool: "Notion or CRM"
    Purpose: "Prioritize daily work"
  
  Task_3:
    Time: "9:30 AM"
    Action: "Read"
    Object: "Project Brief"
    Tool: "Google Docs"
    Purpose: "Understand new client requirements"

Active_Work_Block_1:
  Task_4:
    Time: "10:00 AM - 12:00 PM"
    Action: "Design"
    Object: "UI Mockup"
    Project: "Client X - Mobile App"
    Tool: "Figma"
    Deliverable: "3 screens: Login, Home, Profile"
  
  Task_5:
    Time: "Within work block"
    Action: "Create"
    Object: "Component Library"
    Tool: "Figma"
    Purpose: "Reusable UI elements for project"

Midday:
  Task_6:
    Time: "12:00 PM"
    Action: "Send"
    Object: "Design Preview"
    Tool: "Figma (share link) + Discord"
    Recipient: "Client X for feedback"
  
  Task_7:
    Time: "12:30 PM - 1:00 PM"
    Action: "Attend"
    Object: "Team Standup"
    Tool: "Discord Voice"
    Update: "Progress on Client X, blockers, plans"

Active_Work_Block_2:
  Task_8:
    Time: "1:00 PM - 3:00 PM"
    Action: "Design"
    Object: "Social Media Post"
    Project: "Internal - RH Instagram"
    Tool: "Canva"
    Quantity: "5 posts for the week"
  
  Task_9:
    Time: "Within work block"
    Action: "Generate"
    Object: "Background Graphics"
    Tool: "Midjourney AI"
    Purpose: "Speed up social media creation"

Feedback_&_Iteration:
  Task_10:
    Time: "3:00 PM"
    Action: "Review"
    Object: "Client Feedback"
    Tool: "Discord + Figma comments"
    Input: "Client X responded with change requests"
  
  Task_11:
    Time: "3:15 PM - 4:30 PM"
    Action: "Revise"
    Object: "UI Mockup"
    Tool: "Figma"
    Changes: "Update colors, adjust spacing, new icon"
  
  Task_12:
    Time: "4:30 PM"
    Action: "Send"
    Object: "Updated Design"
    Tool: "Figma + Discord"
    Message: "Revised per your feedback, ready for approval"

End_of_Day:
  Task_13:
    Time: "5:00 PM"
    Action: "Update"
    Object: "Task Status"
    Tool: "CRM or Notion"
    Status: "Mark completed tasks, note tomorrow's priorities"
  
  Task_14:
    Time: "5:15 PM"
    Action: "Export"
    Object: "Design Files"
    Tool: "Figma"
    Format: "PNG for client review, Figma file for dev handoff"
  
  Task_15:
    Time: "5:30 PM"
    Action: "Log"
    Object: "Work Hours"
    Tool: "Time tracking system"
    Purpose: "Record billable hours for Client X"

Daily_Metrics:
  - "Tasks completed: 15"
  - "Designs created: 8 (3 UI screens + 5 social posts)"
  - "Client interactions: 3 (preview, feedback, revision)"
  - "Tools used: 5 (Figma, Canva, Midjourney, Discord, Google Docs)"
  - "Billable hours: 6 (Client X project)"
  - "Internal hours: 2 (Social media, admin)"
```

**Taxonomy Breakdown:**

| Task # | Action | Object | Tool | Department | Profession |
|--------|---------|---------|------|------------|------------|
| 1 | Check | Discord Messages | Discord | Design | UI/UX Designer |
| 2 | Review | Task List | Notion | Design | UI/UX Designer |
| 3 | Read | Project Brief | Google Docs | Design | UI/UX Designer |
| 4 | Design | UI Mockup | Figma | Design | UI/UX Designer |
| 5 | Create | Component Library | Figma | Design | UI/UX Designer |
| 6 | Send | Design Preview | Figma + Discord | Design | UI/UX Designer |
| 7 | Attend | Team Standup | Discord | Design | UI/UX Designer |
| 8 | Design | Social Media Post | Canva | Design | Graphic Designer |
| 9 | Generate | Background Graphics | Midjourney | Design | Graphic Designer |
| 10 | Review | Client Feedback | Discord | Design | UI/UX Designer |
| 11 | Revise | UI Mockup | Figma | Design | UI/UX Designer |
| 12 | Send | Updated Design | Figma + Discord | Design | UI/UX Designer |
| 13 | Update | Task Status | Notion | Design | UI/UX Designer |
| 14 | Export | Design Files | Figma | Design | UI/UX Designer |
| 15 | Log | Work Hours | Time Tracker | Design | UI/UX Designer |

---

## 📋 Task Manager System

### Project Template Structure

**Definition:** A Project Template is a collection of related Task Templates organized by phases and dependencies.

**Example: Recruitment Project Template**

```yaml
Project_Template_Name: "Full_Cycle_Recruitment"
Project_Owner: "HR Department"
Estimated_Duration: "4-6 weeks"
Success_Metric: "Qualified candidate hired"

Phase_1_Job_Creation:
  Duration: "1 week"
  Tasks:
    - Task_1: "Create: Job Description"
    - Task_2: "Define: Required Skills"
    - Task_3: "Set: Salary Range"
    - Task_4: "Approve: Job Posting (with department lead)"
  Dependencies: None
  Output: "Approved job posting ready to publish"

Phase_2_Sourcing:
  Duration: "1-2 weeks"
  Tasks:
    - Task_5: "Post: Job Advertisement (LinkedIn, DOU, Djinni)"
    - Task_6: "Search: Active Candidates (portfolio sites)"
    - Task_7: "Scrape: Contact Information (if needed)"
    - Task_8: "Send: Outreach Messages (to passive candidates)"
  Dependencies: ["Phase_1 complete"]
  Output: "10+ qualified applications received"

Phase_3_Screening:
  Duration: "1 week"
  Tasks:
    - Task_9: "Screen: Resumes (filter by requirements)"
    - Task_10: "Review: Portfolios (assess quality)"
    - Task_11: "Conduct: Screening Calls (15 min each)"
    - Task_12: "Select: Top 3-5 Candidates (for interviews)"
  Dependencies: ["Phase_2 complete"]
  Output: "3-5 candidates ready for interviews"

Phase_4_Interviews:
  Duration: "1-2 weeks"
  Tasks:
    - Task_13: "Schedule: Video Interviews"
    - Task_14: "Conduct: Behavioral Interviews (HR)"
    - Task_15: "Conduct: Technical Interviews (dept lead)"
    - Task_16: "Assign: Test Project (if applicable)"
    - Task_17: "Review: Test Submissions"
  Dependencies: ["Phase_3 complete"]
  Output: "1-2 finalists selected"

Phase_5_Offer:
  Duration: "1 week"
  Tasks:
    - Task_18: "Discuss: Salary Expectations"
    - Task_19: "Prepare: Offer Letter"
    - Task_20: "Send: Job Offer (via email)"
    - Task_21: "Negotiate: Terms (if needed)"
    - Task_22: "Receive: Signed Contract"
  Dependencies: ["Phase_4 complete"]
  Output: "Accepted offer, start date confirmed"

Phase_6_Onboarding:
  Duration: "1 week"
  Tasks:
    - Task_23: "Create: Employee Account (systems)"
    - Task_24: "Grant: Tool Access (software licenses)"
    - Task_25: "Send: Welcome Email (with checklist)"
    - Task_26: "Schedule: First Day Orientation"
    - Task_27: "Assign: Mentor (team member)"
    - Task_28: "Set: 30-60-90 Day Goals"
  Dependencies: ["Phase_5 complete"]
  Output: "New hire successfully onboarded"

Project_Metrics:
  - "Time to hire: 4-6 weeks"
  - "Applications received: 50+"
  - "Screening calls conducted: 15"
  - "Interviews conducted: 6"
  - "Offers extended: 1-2"
  - "Acceptance rate: 80%"
  - "Cost per hire: $500"
```

### Task Template Structure

**Definition:** A Task Template is a reusable work unit with standard structure.

**Example: Task Template - Create Job Posting**

```json
{
  "template_id": "TASK-HR-001",
  "template_name": "Create Job Posting",
  "entity": "TASK_MANAGERS",
  "sub_entity": "Task_Templates/By_Department/HR_Tasks",
  
  "structure": {
    "action": "Create",
    "object": "Job Posting",
    "tool": "Notion + Google Docs"
  },
  
  "department": "HR (Managers)",
  "profession": "HR Manager or Recruiter",
  
  "inputs_required": [
    "Position title",
    "Department",
    "Required skills",
    "Experience level",
    "Salary range",
    "Work arrangement (remote/hybrid/office)"
  ],
  
  "steps": [
    {
      "step_number": 1,
      "action": "Open",
      "detail": "Job posting template in Google Docs"
    },
    {
      "step_number": 2,
      "action": "Fill in",
      "detail": "Position title and department"
    },
    {
      "step_number": 3,
      "action": "List",
      "detail": "Required skills and experience level"
    },
    {
      "step_number": 4,
      "action": "Define",
      "detail": "Responsibilities and key deliverables"
    },
    {
      "step_number": 5,
      "action": "Set",
      "detail": "Salary range based on market research"
    },
    {
      "step_number": 6,
      "action": "Specify",
      "detail": "Work arrangement and location"
    },
    {
      "step_number": 7,
      "action": "Add",
      "detail": "Company overview and culture highlights"
    },
    {
      "step_number": 8,
      "action": "Review",
      "detail": "Grammar, clarity, and completeness"
    },
    {
      "step_number": 9,
      "action": "Submit",
      "detail": "For approval by department lead"
    },
    {
      "step_number": 10,
      "action": "Publish",
      "detail": "Once approved, post on job boards"
    }
  ],
  
  "outputs": [
    "Completed job posting document",
    "Approved by department lead",
    "Ready for publication"
  ],
  
  "success_criteria": [
    "All required fields filled",
    "Clear and compelling job description",
    "Competitive salary range",
    "Approved by stakeholder"
  ],
  
  "time_estimate": {
    "min_minutes": 30,
    "max_minutes": 60,
    "average_minutes": 45
  },
  
  "dependencies": {
    "prerequisites": [
      "Department hiring need identified",
      "Budget approved for position"
    ],
    "follow_up_tasks": [
      "Post: Job Advertisement (on job boards)",
      "Share: Job Link (on social media)"
    ]
  },
  
  "related_entities": {
    "jobs": "Creates new Job_Posting entity",
    "libraries": "Uses Actions (Create), Objects (Job Posting), Tools (Notion, Google Docs)"
  },
  
  "automation_potential": "Medium - AI can draft initial posting from requirements",
  
  "real_world_example": {
    "scenario": "Hiring Frontend Developer",
    "inputs": {
      "position": "Frontend Developer",
      "department": "Developers",
      "required_skills": ["React.js", "TypeScript", "CSS"],
      "experience": "Mid-level (2-4 years)",
      "salary_range": "$2,000-3,500/month",
      "work_arrangement": "Remote"
    },
    "output": "Published job posting on LinkedIn, DOU, and Djinni"
  }
}
```

---

## 🔧 Implementation Patterns

### Pattern 1: Action + Object = Task Name

**Formula:**
```
Task Name = [Action Verb] + [Object Noun] + [Optional Context]
```

**Examples:**

| Action | Object | Context | Full Task Name |
|--------|---------|---------|----------------|
| Create | Job Posting | for Frontend Dev | Create Job Posting (for Frontend Developer) |
| Send | Cold Email | to 50 prospects | Send Cold Email (to 50 prospects) |
| Design | UI Mockup | for Client X | Design UI Mockup (for Client X) |
| Update | CRM Database | candidate status | Update CRM Database (candidate status) |
| Analyze | Lead Data | monthly report | Analyze Lead Data (monthly report) |
| Conduct | Video Interview | behavioral questions | Conduct Video Interview (behavioral questions) |
| Review | Portfolio | design quality | Review Portfolio (design quality) |
| Export | Design Files | for development | Export Design Files (for development) |

### Pattern 2: Department → Profession → Responsibilities → Tasks

**Example: HR Department**

```
Department: HR (Managers)
   ↓
Profession: Recruiter
   ↓
Responsibility: Manage Candidate Pipeline
   ↓
Tasks:
   - Screen: Candidate Resumes
   - Conduct: Video Interviews
   - Update: CRM Status
   - Send: Job Offers
```

### Pattern 3: Libraries as Building Blocks

**How to Construct Any Task:**

1. **Start with LIBRARIES/Actions** - Choose your verb
2. **Add LIBRARIES/Objects** - Choose your noun
3. **Specify LIBRARIES/Tools** - Choose your software
4. **Assign to TALENTS/Employees** - Choose who does it
5. **Link to BUSINESSES or JOBS** - Choose the context
6. **Store in TASK_MANAGERS** - Create the task record

**Example Construction:**

```yaml
# Step 1: Choose Action
Selected_Action: "Send" (from actions.json)

# Step 2: Choose Object
Selected_Object: "Cold Email" (from objects.json, type: Communications)

# Step 3: Choose Tool
Selected_Tool: "Gmail" (from tools.json, category: Communication)

# Step 4: Assign to Talent
Assigned_To: "Hanan Zaheur" (from employees, profession: Lead Generator)

# Step 5: Link to Entity
Linked_Entity: "BUSINESSES/Prospects" (outreach campaign)

# Step 6: Create Task
Task_Record:
  task_id: "TASK-LG-2025-001"
  task_name: "Send Cold Email (to IT companies)"
  action: "Send"
  object: "Cold Email"
  tool: "Gmail"
  assigned_to: "Hanan Zaheur"
  department: "Lead Generation"
  profession: "Lead Generator"
  related_entity: "BUSINESSES/Prospects"
  due_date: "2025-11-10"
  status: "In Progress"
  priority: "High"
```

### Pattern 4: Workflow Automation

**Linear Sequential Workflow:**

```
Task A (complete) → Task B (starts) → Task C (starts) → Task D (starts)
```

**Example: Old Client Reengagement**
```
1. Export Client List [HR/Sales]
   ↓ (when complete)
2. Research Company Updates [Sales]
   ↓ (when complete)
3. Draft Personalized Email [Sales]
   ↓ (when complete)
4. Send Reengagement Email [Sales]
   ↓ (when complete)
5. Log Email Send Date [Sales]
   ↓ (after 3 days)
6. Send Follow-up Email [Sales]
   ↓ (if positive response)
7. Schedule Discovery Call [Sales]
```

**Parallel Processing Workflow:**

```
Task A (complete) → [Task B, Task C, Task D] (all start simultaneously)
```

**Example: Lead Enrichment**
```
1. Find Company on LinkedIn [LG]
   ↓ (when complete, trigger 3 parallel tasks)
   ├→ 2. Scrape Contact Emails [LG with automation]
   ├→ 3. Research Company News [LG]
   └→ 4. Find Decision Makers [LG]
   ↓ (when all 3 complete)
5. Create Enriched Lead Profile [LG]
   ↓
6. Add to CRM [LG]
```

---

## 💡 Key Insights

### Why This System Works

1. **Standardization** - Everyone speaks the same language
2. **Scalability** - Templates multiply easily across departments
3. **Measurability** - Structured data enables analytics
4. **Automation** - AI can understand and execute tasks
5. **Onboarding** - New hires learn faster with clear structure
6. **Knowledge Preservation** - Expertise captured in templates
7. **Cross-Department Clarity** - Design knows what Dev needs, HR knows what Sales needs

### AI-First Benefits

**For LLM Agents:**
- Clear entity structure enables smart search
- Standardized naming allows pattern recognition
- Metadata supports context-aware responses
- Relationship mapping enables workflow automation

**For Human Users:**
- Reduced cognitive load (follow templates)
- Faster decision-making (clear options)
- Better collaboration (shared vocabulary)
- Easier training (documented processes)

---

## 📚 Related Documentation

- [INFRASTRUCTURE/ENTITIES/README.md](../INFRASTRUCTURE/ENTITIES/README.md) - Entity definitions
- [LIBRARIES/README.md](../LIBRARIES/README.md) - Library structure
- [Framework/PLANNING.md](../Framework/PLANNING.md) - Framework implementation plan
- [Documentation/ENTITY_TYPES.md](./ENTITY_TYPES.md) - Entity types overview
- [Documentation/ARCHITECTURE.md](./ARCHITECTURE.md) - System architecture

---

**Last Updated:** November 9, 2025  
**Maintained By:** Framework Architecture Team  
**Next Review:** Quarterly (February 2026)

