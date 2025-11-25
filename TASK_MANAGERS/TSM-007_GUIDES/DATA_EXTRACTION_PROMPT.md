# Data Extraction Prompt: RestructuredData → Taxonomy Templates
**Version:** 2.3
**Created:** November 25, 2025
**Last Updated:** November 10, 2025
**Purpose:** Comprehensive guide for extracting and organizing data from RestructuredData documents into taxonomy template listings with daily notes integration, skills collection, object type patterns, and priority management

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Source Data Structure](#source-data-structure)
3. [Extraction Targets](#extraction-targets)
4. [Taxonomy Mapping Rules](#taxonomy-mapping-rules)
5. [Skills Collection & Extraction](#skills-collection--extraction)
6. [Department-Specific Extraction Rules](#department-specific-extraction-rules)
7. [Object Library Definitions](#object-library-definitions)
8. [Object Type Patterns by Profession](#object-type-patterns-by-profession)
9. [Automation Potential by Object Type](#automation-potential-by-object-type)
10. [Compound Entities Explanation](#compound-entities-explanation)
11. [Template Structures](#template-structures)
12. [Output File Specifications](#output-file-specifications)
13. [Extraction Process](#extraction-process)
14. [Daily Notes Extraction Guidelines](#daily-notes-extraction-guidelines)
15. [Prioritization System](#prioritization-system)
16. [Top-10 Priority Management System](#top-10-priority-management-system)
17. [Validation Rules](#validation-rules)
18. [Examples](#examples)
19. [Quality Checklist](#quality-checklist)

---

## Overview

### Purpose
Extract structured data from documents in `C:\Users\Dell\Dropbox\Nov25\Taxonomy\RestructuredData\` and organize it into standardized template listings within the Taxonomy folder structure.

### Source Location
```
C:\Users\Dell\Dropbox\Nov25\Taxonomy\RestructuredData\
```

### Target Location
```
C:\Users\Dell\Dropbox\Nov25\Taxonomy\Templates\
```

### Expected Output Files
- `Tasks_Templates.md` - All extracted Task Templates
- `Step_Templates.md` - All extracted Step Templates
- `Project_Templates.md` - All extracted Project Templates
- `Milestone_Templates.md` - All extracted Milestone Templates
- `Action_Items_Templates.md` - All extracted action item templates
- `Workflow_Templates.md` - All extracted workflow templates

---

## Source Data Structure

### Document Types in RestructuredData

#### 1. Daily Summary Reports
**Files:** `Consolidated_Daily_Summary_Nov06_2025.md`, `Department_Operations_Nov05_2025.md`, etc.

**Structure:**
- Executive Summary
- Department-by-Department Summary
- Key Achievements (with tasks)
- Metrics
- Status indicators

**What to Extract:**
- Tasks (from "Key Achievements" sections)
- Department operations
- Completed activities
- Metrics and outcomes

#### 2. Project Reports
**Files:** `Projects_Milestones_Tasks_Nov05-07_2025.md`, `Projects_Deliverables_Nov05_2025.md`, etc.

**Structure:**
- Project Metadata (Status, Department, Owner, Timeline, Impact)
- Project Overview (Action + Object + Tool + Context)
- Phases (Phase 1, Phase 2, etc.)
- Milestones (Milestone 1.1, Milestone 1.2, etc.)
- Tasks (with taxonomy format: Action-Object using Tool in Context)
- Project Outcomes

**What to Extract:**
- Projects (with full metadata)
- Phases (within projects)
- Milestones (within phases)
- Tasks (with taxonomy breakdown)
- Dependencies and relationships

#### 3. Organized Call Notes
**Files:** `241025-organized.md`, `291025-organized.md`, etc.

**Structure:**
- Meeting Metadata (Date, Participants, Duration, Topics)
- Executive Summary
- Action Items & Tasks
- Decisions Made
- Next Steps

**What to Extract:**
- Action items (with owner, priority, timeline, status)
- Tasks (from action items)
- Decisions (for context)
- Follow-up items

#### 4. Comprehensive Reviews
**Files:** `OCTOBER_2025_COMPREHENSIVE_REVIEW.md`

**Structure:**
- Multi-period summaries
- Cross-project analysis
- Department performance
- Strategic initiatives

**What to Extract:**
- Recurring patterns (for template identification)
- Cross-project workflows
- Department-specific processes
- Best practices

---

## Extraction Targets

### 1. Tasks

#### Identification Pattern
Look for:
- Lines starting with `- ✅` or `- ⏳` or `- ❌` (completed, in-progress, failed)
- Lines containing "Action-Object using Tool in Context" format
- Task descriptions in bullet lists
- Sections titled "Tasks", "Activities", "Key Achievements"

#### Required Fields to Extract
```yaml
Task:
  id: "Auto-generated unique ID (TASK-[DEPT]-[NUMBER])"
  name: "Task name (Action + Object)"
  taxonomy:
    action: "Extracted "
    object: "libraries"
    tool: "Extracted from task description or libraries"
    department: "From context or metadata"
    profession: "From context or metadata"
  description: "Full task description"
  owner: "Owner/Assignee name"
  priority: "Critical | High | Medium | Low"
  status: "Completed | In Progress | Not Started | Failed"
  timeline:
    start_date: "YYYY-MM-DD"
    completed_date: "YYYY-MM-DD (if completed)"
    estimated_duration: "X minutes/hours"
  context: "Additional context from source"
  source_file: "Original file name"
  source_line: "Approximate line number"
```

#### Example Extraction
**Source:**
```markdown
- ✅ Create-Folder-Structure for Employee-Artemchuk-Nikolay using FileSystem in LG-Department-Context
  - Owner: Admin
  - Priority: High
  - Completed: Nov 5, 2025
```

**Extracted:**
```yaml
Task:
  id: "TASK-LG-001"
  name: "Create Folder Structure"
  taxonomy:
    action: "create"
    object: "folder_structure"
    tool: "filesystem"
    department: "LG"
    profession: "admin"
  description: "Create folder structure for Employee Artemchuk Nikolay"
  owner: "Admin"
  priority: "High"
  status: "Completed"
  timeline:
    completed_date: "2025-11-05"
  source_file: "Projects_Milestones_Tasks_Nov05-07_2025.md"
```

### 2. Steps

#### Identification Pattern
Look for:
- Numbered lists (1., 2., 3.)
- Steps within task descriptions
- "Step X:" headers
- Sequential actions in workflows

#### Required Fields to Extract
```yaml
Step:
  id: "Auto-generated (STEP-[TASK_ID]-[NUMBER])"
  task_id: "Parent task ID"
  step_number: "Integer (1, 2, 3...)"
  name: "Step name"
  action: "Action verb"
  detail: "Specific instruction"
  tool_used: "Tool name (if specified)"
  expected_duration: "X minutes"
  order: "Integer for sequencing"
  dependencies: "List of prerequisite step IDs"
  outputs: "What this step produces"
  source_file: "Original file name"
```

#### Example Extraction
**Source:**
```markdown
**Step 1: Identify the Task Pattern**
- Question_1: "Is this task repeated across multiple projects/people?"
- Question_2: "Can the task be broken into clear steps?"
```

**Extracted:**
```yaml
Step:
  id: "STEP-TASK-LG-001-01"
  task_id: "TASK-LG-001"
  step_number: 1
  name: "Identify the Task Pattern"
  action: "identify"
  detail: "Determine if task is repeated across multiple projects/people and can be broken into clear steps"
  expected_duration: "10 minutes"
  order: 1
```

### 3. Projects

#### Identification Pattern
Look for:
- Sections titled "PROJECT X:" or "## PROJECT"
- Project metadata blocks
- Project Overview sections
- Project Outcomes sections

#### Required Fields to Extract
```yaml
Project:
  id: "Auto-generated (PROJ-[DEPT]-[NUMBER])"
  name: "Project name"
  status: "Completed | In Progress | Planned | Cancelled"
  department: "Department name"
  primary_owner: "Owner name"
  timeline:
    start_date: "YYYY-MM-DD"
    end_date: "YYYY-MM-DD"
    duration_days: "Integer"
  impact: "Critical | High | Medium | Low"
  taxonomy:
    action: "From project overview"
    object: "From project overview"
    tool: "From project overview"
    context: "From project overview"
  description: "Project description"
  phases: "List of phase IDs"
  milestones: "List of milestone IDs"
  outcomes: "Project outcomes/metrics"
  source_file: "Original file name"
```

#### Example Extraction
**Source:**
```markdown
## PROJECT 1: LG Team Onboarding Solution ✅ COMPLETED

**Project Metadata:**
- **Status:** Completed
- **Department:** LG (Legal & Governance)
- **Primary Owner:** Artemchuk Nikolay
- **Timeline:** Nov 5-7, 2025
- **Impact:** High - Streamlined onboarding for 4 team members

### Project Overview
Action: **Implement** + Object: **Onboarding System** + Tool: **Automated Workflows** + Context: **LG Department**
```

**Extracted:**
```yaml
Project:
  id: "PROJ-LG-001"
  name: "LG Team Onboarding Solution"
  status: "Completed"
  department: "LG"
  primary_owner: "Artemchuk Nikolay"
  timeline:
    start_date: "2025-11-05"
    end_date: "2025-11-07"
    duration_days: 3
  impact: "High"
  taxonomy:
    action: "implement"
    object: "onboarding_system"
    tool: "automated_workflows"
    context: "LG Department"
  description: "Streamlined onboarding for 4 team members"
```

### 4. Milestones

#### Identification Pattern
Look for:
- "Milestone X.Y:" headers
- Milestone descriptions within phases
- Achievement markers

#### Required Fields to Extract
```yaml
Milestone:
  id: "Auto-generated (MIL-[PROJ_ID]-[NUMBER])"
  project_id: "Parent project ID"
  phase_id: "Parent phase ID (if applicable)"
  name: "Milestone name"
  description: "Milestone description"
  status: "Completed | In Progress | Not Started"
  target_date: "YYYY-MM-DD"
  completed_date: "YYYY-MM-DD (if completed)"
  tasks: "List of task IDs"
  success_criteria: "What defines completion"
  source_file: "Original file name"
```

### 5. Action Items

#### Identification Pattern
Look for:
- "### Action Items" sections
- "### ACTION ITEMS & TASKS" sections
- Items with Owner/Assignee, Priority, Timeline, Status

#### Required Fields to Extract
```yaml
ActionItem:
  id: "Auto-generated (ACT-[DEPT]-[NUMBER])"
  title: "Action item title"
  description: "Detailed description"
  owner: "Owner/Assignee"
  priority: "Critical | High | Medium | Low"
  status: "Not Started | In Progress | Completed | Blocked"
  timeline:
    created_date: "YYYY-MM-DD"
    due_date: "YYYY-MM-DD"
    completed_date: "YYYY-MM-DD (if completed)"
  dependencies: "List of dependencies"
  related_project: "Project ID (if applicable)"
  source_file: "Original file name"
```

---

## Taxonomy Mapping Rules

### Action Extraction
1. **From Task Name:** Extract the verb (first word before hyphen in "Action-Object" format)
   - Example: "Create-Folder-Structure" → action: "create"

2. **From Libraries:** Match extracted action to `Framework/Entities/LIBRARIES/actions.json`
   - Verify action exists in library
   - Use library entry if found, otherwise create new entry

3. **Normalization Rules:**
   - Convert to lowercase
   - Use base form (create, not creating/created)
   - Handle compound actions (e.g., "set-up" → "setup")

### Object Extraction
1. **From Task Name:** Extract the noun (after first hyphen in "Action-Object" format)
   - Example: "Create-Folder-Structure" → object: "folder_structure"

2. **From Libraries:** Match extracted object to `Framework/Entities/LIBRARIES/objects.json`
   - Verify object exists in library
   - Use library entry if found

3. **Normalization Rules:**
   - Convert to lowercase
   - Use snake_case for multi-word objects
   - Handle compound objects (e.g., "Folder-Structure" → "folder_structure")

### Tool Extraction
1. **From Task Description:** Look for "using [Tool]" pattern
   - Example: "using FileSystem" → tool: "filesystem"

2. **From Libraries:** Match extracted tool to `Framework/Entities/LIBRARIES/tools.json`
   - Verify tool exists in library

3. **Normalization Rules:**
   - Convert to lowercase
   - Use standard tool names from library

### Department Extraction
1. **From Metadata:** Use explicit department field if present
2. **From Context:** Extract from "in [Department]-Context" pattern
3. **From File Name:** Infer from file name patterns (e.g., "Department_Operations_Nov05_2025.md")
4. **From Owner:** Map owner to department if known

### Profession Extraction
1. **From Owner:** Map owner name to profession using known employee directory
2. **From Context:** Extract from task context
3. **From Libraries:** Match to `Framework/Entities/LIBRARIES/professions.json`

---

## Skills Collection & Extraction

### Skills Formula
Skills represent **demonstrated abilities** that result from completing tasks. The formula for extracting skills is:

```
SKILL = RESULT + OBJECT + "via/using/in" + TOOL
```

**Components:**
- **RESULT**: What outcome was achieved (verb in past participle form)
- **OBJECT**: What was worked on (noun or noun phrase)
- **TOOL**: What tool/platform was used (technology/platform name)

### Skill Extraction Process

#### Step 1: Identify Completed Tasks
Only extract skills from tasks with status `completed` or marked with ✅.

#### Step 2: Transform Action to Result
Convert the action verb to past participle form representing achievement:

| Action (Task) | Result (Skill) | Example |
|---------------|----------------|---------|
| Create | Created | Created API endpoint |
| Design | Designed | Designed landing page |
| Write | Written | Written documentation |
| Develop | Developed | Developed microservice |
| Analyze | Analyzed | Analyzed user data |
| Build | Built | Built dashboard |
| Implement | Implemented | Implemented feature |
| Fix | Fixed | Fixed bug |
| Optimize | Optimized | Optimized database query |
| Test | Tested | Tested integration |

#### Step 3: Construct Skill Phrase
Combine the components following the formula:

**Examples:**
- Task: "Create-API-Endpoint using FastAPI in Dev-Context"
  - Skill: "Created API endpoint using FastAPI"

- Task: "Design-Landing-Page using Figma in Design-Context"
  - Skill: "Designed landing page using Figma"

- Task: "Write-Documentation using VS Code in Dev-Context"
  - Skill: "Written technical documentation using VS Code"

#### Step 4: Categorize by Profession
Map skills to relevant professions based on the task context:

| Profession | Typical Skills | Common Tools |
|------------|----------------|--------------|
| **Backend Developer** | Created APIs, Developed microservices, Implemented databases, Fixed backend bugs | FastAPI, PostgreSQL, Docker, Python |
| **Frontend Developer** | Built UI components, Implemented responsive designs, Optimized frontend performance | React, TypeScript, CSS, Figma |
| **Full-Stack Developer** | Developed full-stack applications, Integrated APIs, Built end-to-end features | React, Node.js, PostgreSQL, Docker |
| **Designer** | Designed mockups, Created brand assets, Illustrated graphics, Built prototypes | Figma, Photoshop, Illustrator, Canva |
| **Lead Generator** | Generated leads, Sent cold outreach, Built prospect lists, Analyzed lead data | LinkedIn, CRM, Apollo, Perplexity |
| **Recruiter** | Sourced candidates, Conducted interviews, Managed hiring pipeline, Reviewed resumes | LinkedIn, ATS, VS Code |
| **Video Editor** | Edited videos, Created animations, Produced content, Optimized video quality | Premiere Pro, After Effects, CapCut |
| **AI Engineer** | Fine-tuned models, Developed prompts, Implemented ML pipelines, Analyzed training data | Python, Claude API, TensorFlow, Cursor |
| **SMM (Social Media Manager)** | Published social posts, Scheduled content, Engaged with audience, Analyzed social metrics | Hootsuite, Buffer, Meta Business Suite, Canva |
| **PPC Specialist** | Launched ad campaigns, Optimized bids, A/B tested creatives, Analyzed ad performance | Google Ads, Meta Ads Manager, Analytics |
| **SEO Specialist** | Optimized pages, Built backlinks, Researched keywords, Improved rankings | Ahrefs, SEMrush, Google Search Console, Screaming Frog |
| **Media Buyer** | Negotiated media buys, Managed budgets, Analyzed ROI, Purchased ad space | Ad platforms, Analytics tools, Media buying platforms |

### Skill Storage Structure

Each skill entry should be stored in:
```
C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\LIBRARIES\Skills\
```

**JSON Schema:**
```json
{
  "skill_id": "SKILL-[PROFESSION_CODE]-[NUMBER]",
  "skill_phrase": "Result + Object + via/using/in + Tool",
  "components": {
    "result": "Past participle verb",
    "object": "What was worked on",
    "tool": "Tool/platform used"
  },
  "profession": "Primary profession this skill relates to",
  "proficiency_level": "Beginner | Intermediate | Advanced | Expert",
  "frequency": "How often this skill was demonstrated (count)",
  "first_demonstrated": "YYYY-MM-DD (first task date)",
  "last_demonstrated": "YYYY-MM-DD (most recent task date)",
  "related_tasks": ["TASK-ID-1", "TASK-ID-2"],
  "department": "Department where skill was used",
  "tags": ["tag1", "tag2"]
}
```

**Example:**
```json
{
  "skill_id": "SKILL-DEV-047",
  "skill_phrase": "Created REST API endpoints using FastAPI",
  "components": {
    "result": "Created",
    "object": "REST API endpoints",
    "tool": "FastAPI"
  },
  "profession": "Backend Developer",
  "proficiency_level": "Advanced",
  "frequency": 12,
  "first_demonstrated": "2025-10-15",
  "last_demonstrated": "2025-11-07",
  "related_tasks": ["TASK-DEV-023", "TASK-DEV-089", "TASK-DEV-145"],
  "department": "Dev",
  "tags": ["backend", "api", "python", "fastapi", "microservices"]
}
```

### Skill Aggregation Rules

#### Frequency Tracking
- Increment `frequency` count each time a similar task is completed
- Update `last_demonstrated` date
- Add task ID to `related_tasks` array

#### Proficiency Level Assessment
Automatically determine proficiency based on frequency and complexity:

| Frequency | Complexity Level | Proficiency |
|-----------|------------------|-------------|
| 1-2 times | Simple tasks | Beginner |
| 3-5 times | Moderate tasks | Intermediate |
| 6-10 times | Complex tasks | Advanced |
| 10+ times | Complex + mentoring | Expert |

#### Skill Consolidation
Similar skills should be consolidated to avoid duplication:
- "Created API endpoint using FastAPI" + "Created REST API using FastAPI" → Merge to "Created REST API endpoints using FastAPI"
- Track both task IDs in consolidated skill
- Use the more comprehensive phrase

### Skills Quick Reference by Profession

This table helps identify which skills to prioritize extracting for each profession:

| Profession | Top 5 Skills to Track | Automation Potential |
|------------|----------------------|----------------------|
| **Backend Developer** | 1. Created APIs using FastAPI/Flask<br>2. Developed microservices using Docker<br>3. Implemented database schemas using PostgreSQL<br>4. Fixed backend bugs using debugging tools<br>5. Optimized queries using SQL | High (60-70%) |
| **Frontend Developer** | 1. Built UI components using React<br>2. Implemented responsive designs using CSS<br>3. Integrated APIs using JavaScript<br>4. Optimized performance using Chrome DevTools<br>5. Created animations using CSS/Framer | Medium (50-60%) |
| **Designer** | 1. Designed mockups using Figma<br>2. Created brand assets using Illustrator<br>3. Built prototypes using Figma<br>4. Illustrated graphics using Photoshop<br>5. Designed UI components using design systems | Low-Medium (40-50%) |
| **Lead Generator** | 1. Generated leads using LinkedIn Sales Navigator<br>2. Sent cold outreach using LinkedIn/Email<br>3. Analyzed lead data using CRM<br>4. Built prospect lists using Apollo<br>5. Researched companies using Perplexity | Very High (80-90%) |
| **Recruiter** | 1. Sourced candidates using LinkedIn<br>2. Conducted interviews using video tools<br>3. Reviewed resumes using ATS<br>4. Managed pipeline using CRM<br>5. Sent follow-ups using email automation | High (70-80%) |
| **SMM (Social Media Manager)** | 1. Published social posts using Hootsuite/Buffer<br>2. Scheduled content using content calendars<br>3. Engaged with audience using social platforms<br>4. Analyzed metrics using Meta Business Suite<br>5. Created visuals using Canva | High (65-75%) |
| **PPC Specialist** | 1. Launched ad campaigns using Google Ads/Meta Ads<br>2. Optimized bids using bid management tools<br>3. A/B tested ad creatives using platform testing<br>4. Analyzed performance using Analytics<br>5. Managed budgets using ad platforms | Very High (75-85%) |
| **SEO Specialist** | 1. Optimized pages using on-page SEO<br>2. Built backlinks using outreach strategies<br>3. Researched keywords using Ahrefs/SEMrush<br>4. Improved rankings using technical SEO<br>5. Analyzed traffic using Google Analytics | High (60-70%) |
| **Media Buyer** | 1. Negotiated rates using vendor relationships<br>2. Purchased ad space using media platforms<br>3. Managed budgets using financial tools<br>4. Analyzed ROI using performance data<br>5. Optimized placement using performance metrics | High (65-75%) |

### Daily Notes Skills Extraction

When processing daily notes, follow this workflow:

1. **Read Daily Report** → Extract all completed tasks (✅)
2. **Transform Actions to Results** → Convert verbs to past participle
3. **Build Skills Phrases** → Apply RESULT + OBJECT + via/using + TOOL formula
4. **Check for Existing Skills** → Search skills library for similar entries
5. **Update or Create** → Either increment frequency or create new skill entry
6. **Associate with Employee** → Link skill to TALENTS entity if employee is known

**Example from Daily Notes:**
```markdown
## Dev Department - Nov 07, 2025
- ✅ Create-API-Endpoint for Talents-Microservice using FastAPI in Dev-Context (Olha)
- ✅ Design-Database-Schema for Finance-Service using PostgreSQL in Dev-Context (Yaroslav)
- ✅ Implement-Authentication for Yellow-Card-Backend using JWT in Dev-Context (Olha)
```

**Extracted Skills:**
1. "Created API endpoint for microservices using FastAPI" → SKILL-DEV-047 (Olha)
2. "Designed database schema using PostgreSQL" → SKILL-DEV-089 (Yaroslav)
3. "Implemented authentication using JWT" → SKILL-DEV-102 (Olha)

---

## Department-Specific Extraction Rules

Each department has unique objects, tools, and workflows. Understanding these patterns improves extraction accuracy by 30-40%.

### HR Department
- **Common Objects:** Candidates, Job Postings, Interviews, Contracts, Reports, Databases
- **Common Tools:**
  - Documentation: VS Code (primary documentation tool)
  - AI Tools: Claude (deep analysis), Gemini (research), Perplexity (market intelligence)
  - Development: Cursor (if involved in HR tech)
  - Other: CRM, Gmail, Google Docs
- **Priority Keywords:** "screening", "interviewing", "hiring", "onboarding", "recruiting"
- **Success Metrics:** Time-to-hire, candidate quality, retention rate, applicants per posting

### LG (Lead Generation) Department
- **Common Objects:** Cold Emails, Lead Lists, Outreach Campaigns, Contact Data, Company Research
- **Common Tools:**
  - AI Tools: Gemini (primary - LinkedIn 2000+ account analysis), Perplexity (news search), Claude (deep analysis)
  - Automation: n8n (saves 4-5 hours/day per employee)
  - Research: Apollo, LinkedIn Sales Navigator, CRM
- **Priority Keywords:** "prospecting", "qualifying", "outreach", "nurturing", "enriching", "researching"
- **Success Metrics:** Emails sent, open rate (32%), reply rate (6%), meetings booked, deals closed, automation time saved

### Design Department
- **Common Objects:** UI Mockups, Brand Assets, Design Systems, Banners, Logos, Icons, Illustrations, Wireframes, Prototypes
- **Common Tools:**
  - Design: Figma (31+ active projects), Adobe Suite, Canva
  - AI Tools: Midjourney (image generation), Leonardo.ai (design assets), Claude (feedback and analysis)
  - Documentation: VS Code (design documentation)
- **Priority Keywords:** "designing", "prototyping", "iterating", "presenting", "creating", "visualizing"
- **Success Metrics:** Design iterations, client approval, time per mockup, assets delivered

### Dev Department
- **Common Objects:** Code, Pull Requests, Features, Bug Fixes, APIs, Databases, Microservices, Servers, Endpoints, Schemas
- **Common Tools:**
  - Development: Cursor (primary IDE with AI integration), VS Code, GitHub
  - AI Tools: Claude (via Cursor integration)
  - Version Control: GitHub (repositories, pull requests, issues, actions, project boards)
  - Databases: PostgreSQL, MongoDB
  - Other: Git, Terminal, Containers
- **Priority Keywords:** "developing", "testing", "deploying", "debugging", "refactoring", "implementing"
- **Success Metrics:** Lines of code, bugs resolved, deployment frequency, feature delivery time, code quality

### AI Department
- **Common Objects:** Prompts, AI Workflows, Automations, Knowledge Bases, Integration Scripts, Models
- **Common Tools:**
  - AI Tools: Claude (deep analysis), Gemini (large datasets), Perplexity (research), ChatGPT (content generation)
  - Development: Cursor (AI workflow development), VS Code
  - Automation: n8n (primary workflow automation platform)
- **Priority Keywords:** "automating", "optimizing", "training", "integrating", "processing", "synthesizing"
- **Success Metrics:** Automation coverage, time saved (4-5 hours/day), accuracy rate, workflows created, AI integrations

### Sales Department
- **Common Objects:** Proposals, Demos, Contracts, Follow-ups, Presentations, Client Communications
- **Common Tools:**
  - AI Tools: Claude (proposal analysis), Gemini (company research), Perplexity (market intelligence)
  - Documentation: VS Code (sales documentation), Google Slides
  - Other: CRM, DocuSign, Email platforms
- **Priority Keywords:** "presenting", "negotiating", "closing", "following-up", "proposing"
- **Success Metrics:** Deals closed, revenue generated, conversion rate, proposal quality, follow-up rate

### Video Department
- **Common Objects:** Video Scripts, Raw Footage, Edited Videos, Thumbnails, Animations, Storyboards
- **Common Tools:**
  - Video Editing: Premiere Pro, After Effects, CapCut
  - AI Tools: ElevenLabs (voice synthesis), Claude (script analysis and feedback)
  - Design: Canva (thumbnails and graphics), Adobe Suite
- **Priority Keywords:** "filming", "editing", "rendering", "publishing", "animating", "scripting"
- **Success Metrics:** Videos produced, view count, engagement rate, production time, quality score

### Marketers Department
- **Common Objects:** Ad Campaigns, Posts, Keywords, Landing Pages, Content, SEO Reports, Media Buys, Social Media Strategies, Analytics Dashboards
- **Marketers Tools:**
  - Advertising: Google Ads, Meta Ads Manager, LinkedIn Ads
  - Analytics: Google Analytics, Meta Business Suite, SEMrush, Ahrefs
  - Social Media: Hootsuite, Buffer, Sprout Social
  - SEO Tools: Ahrefs, SEMrush, Moz, Google Search Console
  - Content Management: WordPress, HubSpot, Webflow
  - AI Tools: Claude (content creation), Gemini (market research), Perplexity (competitor analysis), ChatGPT (copy writing)
  - Design: Canva (ad creatives), Figma (landing pages)
- **Priority Keywords:** "optimizing", "targeting", "analyzing", "publishing", "bidding", "ranking", "converting", "retargeting", "A/B testing"
- **Success Metrics:** ROI, CPC (cost per click), CTR (click-through rate), conversion rate, organic traffic, keyword rankings, engagement rate, ROAS (return on ad spend)
- **Professions:**
  - **SMM (Social Media Manager)**: Manages social media presence, creates content calendars, engages with audience, monitors brand mentions
  - **PPC Specialist**: Manages paid advertising campaigns, optimizes bids, A/B tests ad creatives, monitors ad performance
  - **SEO Specialist**: Optimizes website for search engines, conducts keyword research, builds backlinks, monitors rankings
  - **Media Buyer**: Purchases advertising space, negotiates rates, manages budgets, analyzes media performance

---

## Object Library Definitions

Objects are business artifacts that actions are performed on. They are organized by department for better classification and workflow understanding.

### Document Objects
**Department:** HR, Legal, Management
**Workflow Actions:** Create, Update, Review, Approve, Archive, Publish

| Object | Description | Storage Location |
|--------|-------------|------------------|
| Job Posting | Recruitment advertisement with requirements and compensation | `Entities/JOBS/Job_Postings/` |
| Proposal | Client project proposal with scope and pricing | `Entities/BUSINESSES/Proposals/` |
| Report | Status or analysis document (daily, monthly, project) | `Entities/TASK_MANAGERS/Reports/` |
| Contract | Legal agreement between parties | `Entities/BUSINESSES/Contracts/` |
| Invoice | Payment request document | `Entities/BUSINESSES/Invoices/` |

### Communication Objects
**Department:** All Departments
**Workflow Actions:** Send, Respond, Schedule, Follow-up, Archive

| Object | Description | Storage Location |
|--------|-------------|------------------|
| Email | Electronic mail communication | Email platforms, CRM |
| Message | Instant messaging communication | Discord, CRM, Chat platforms |
| Call | Voice or video communication session | Call logs, transcriptions |
| Meeting | Scheduled group communication session | Calendar, Meeting notes |
| Notification | System or manual alert/reminder | CRM, Project management tools |

### Development Objects
**Department:** Dev
**Workflow Actions:** Create, Update, Deploy, Debug, Optimize, Test

| Object | Description | Storage Location |
|--------|-------------|------------------|
| API | Application Programming Interface | Code repositories |
| Database | Structured data storage system | PostgreSQL, MongoDB servers |
| Server | Computing infrastructure | Cloud providers, Docker |
| Endpoint | API access point | API documentation, code |
| Schema | Database or API structure definition | Code repositories |
| Microservice | Independent service component | Docker containers, cloud |
| Code | Source code files | GitHub repositories |
| Pull Request | Code change proposal | GitHub |
| Feature | New functionality implementation | Project management tools |
| Bug Fix | Code correction | Issue tracking systems |

### Design Objects
**Department:** Design
**Workflow Actions:** Create, Design, Update, Review, Present, Iterate

| Object | Description | Storage Location |
|--------|-------------|------------------|
| Banner | Promotional or informational graphic | Design files, Marketing assets |
| Logo | Brand identity graphic | Brand assets folder |
| Icon | Small symbolic graphic | Design systems, Asset libraries |
| Mockup | Visual representation of interface | Figma, Design tools |
| Wireframe | Low-fidelity layout sketch | Figma, Design tools |
| Prototype | Interactive design demonstration | Figma, Prototype tools |
| Illustration | Custom artistic graphic | Design assets |
| UI Component | Reusable interface element | Design systems |
| Brand Asset | Company branding material | Brand guidelines folder |
| Presentation | Visual slide deck | Google Slides, PowerPoint |

### Marketers Objects
**Department:** Marketers
**Workflow Actions:** Create, Publish, Analyze, Optimize, Schedule, Target, Monitor, A/B Test

| Object | Description | Storage Location |
|--------|-------------|------------------|
| Ad | Paid promotional content | Ad platforms (Google, Meta) |
| Post | Social media content | Social platforms |
| Campaign | Coordinated marketing initiative | Marketing tools, CRM |
| Keyword | SEO search term | SEO tools |
| Content | Written or visual marketing material | CMS, Content library |
| Landing Page | Conversion-focused web page | Website, CMS |
| Ad Campaign | PPC advertising campaign | Google Ads, Meta Ads Manager |
| Social Media Strategy | Social media marketing plan | Marketing tools |
| SEO Report | Search engine optimization analysis | SEO tools, Analytics |
| Media Buy | Advertising space purchase | Media buying platforms |

### Management Objects
**Department:** Management, All Departments
**Workflow Actions:** Create, Update, Track, Assign, Complete, Review

| Object | Description | Storage Location |
|--------|-------------|------------------|
| Task | Specific work item | `Entities/TASK_MANAGERS/Tasks/` |
| Project | Collection of related tasks | `Entities/TASK_MANAGERS/Projects/` |
| Milestone | Project checkpoint | `Entities/TASK_MANAGERS/Milestones/` |
| Workflow | Process definition | `Framework/Entities/TASK_MANAGERS/Project_Workflows/` |
| Dashboard | Performance visualization | Analytics tools |
| Timeline | Schedule representation | Project management tools |

---

## Object Type Patterns by Profession

Beyond the general object categories above, objects can have **type modifiers** that provide more granular classification. These type patterns help with precise extraction and automation potential assessment.

### HR/Recruiter Object Types

**Candidates:**
- `needed` - Required positions to fill
- `applied` - Submitted applications
- `found` - Sourced/identified prospects
- `follow-up` - In active communication
- `interviewed` - Completed interview stage
- `offered` - Extended job offer
- `hired` - Successfully onboarded

**Communications:**
- `first connection` - Initial outreach
- `update` - Status or progress communication
- `follow-up` - Subsequent touchpoint
- `feedback` - Interview or application feedback

**Contracts:**
- `employee contracts` - Employment agreements
- `presale contract` - Pre-employment agreements
- `NDA` - Non-disclosure agreements

**Interviews:**
- `video interview` - Remote screening
- `project interview` - Technical/practical assessment
- `cultural fit` - Team alignment interview

### Lead Generator Object Types

**Accounts:**
- `new` - Recently created accounts
- `in work` - Active outreach/nurturing
- `sold` - Converted to client
- `banned` - Blocked/restricted
- `free` - Trial or free tier

**Companies:**
- `lead` - Potential client
- `interested` - Engaged prospect
- `client` - Active customer
- `updated` - Recently modified
- `not relevant` - Disqualified

**Leads:**
- `cold` - No prior contact
- `new` - Recently identified
- `active` - In conversation
- `client` - Converted
- `updated` - Information refreshed

**Messages:**
- `connection` - Initial LinkedIn/platform connection
- `cold` - First outreach
- `follow-up` - Subsequent message
- `presentation` - Product/service pitch

### Developer Object Types

**APIs:**
- `internal` - For internal systems only
- `external` - Third-party integrations
- `public` - Publicly accessible
- `private` - Authenticated access required
- `REST` - RESTful architecture
- `GraphQL` - GraphQL query language

**Databases:**
- `SQL` - Relational databases (PostgreSQL, MySQL)
- `NoSQL` - Document/key-value stores (MongoDB)
- `graph` - Graph databases (Neo4j)
- `time-series` - Time-series databases

**Modules:**
- `utility` - Helper/support functions
- `feature` - User-facing functionality
- `core` - Essential system components
- `integration` - Third-party connectors

**Code:**
- `frontend` - Client-side code
- `backend` - Server-side code
- `shared` - Common/library code
- `test` - Testing code

### Designer Object Types

**Mockups:**
- `website` - Web interface designs
- `app` - Mobile/desktop application designs
- `advertising` - Ad creative mockups
- `email` - Email template designs

**Logos:**
- `wordmark` - Text-based logo
- `lettermark` - Initial/letter-based
- `pictorial` - Icon/symbol-based
- `abstract` - Abstract mark
- `combination` - Text + symbol

**Illustrations:**
- `flat` - Flat design style
- `isometric` - Isometric perspective
- `vector` - Vector-based artwork
- `character` - Character illustrations
- `3D` - Three-dimensional renders

**UI Components:**
- `button` - Interactive buttons
- `form` - Input forms
- `card` - Content cards
- `modal` - Popup/overlay dialogs
- `navigation` - Menu/nav elements

### Video Editor Object Types

**Videos:**
- `raw footage` - Unedited recordings
- `draft` - Work-in-progress edit
- `final` - Completed video
- `short-form` - <60 seconds (TikTok, Reels)
- `long-form` - >3 minutes (YouTube)

**Assets:**
- `stock footage` - Licensed video clips
- `b-roll` - Supplemental footage
- `sound effects` - Audio FX
- `music` - Background tracks
- `voiceover` - Narration audio

### Marketers Object Types

**Ad Campaigns:**
- `PPC` - Pay-per-click advertising (Google Ads, Meta Ads)
- `display` - Banner and display ads
- `video` - Video advertising campaigns
- `retargeting` - Remarketing campaigns
- `search` - Search engine advertising
- `social` - Social media advertising

**Content:**
- `blog post` - Blog article content
- `email copy` - Email marketing content
- `ad copy` - Advertisement text
- `social copy` - Social media posts
- `landing page copy` - Conversion-focused content
- `video script` - Video content scripts

**Keywords:**
- `target` - Primary target keywords
- `long-tail` - Long-tail keyword phrases
- `competitor` - Competitor keywords
- `branded` - Brand-specific keywords
- `local` - Location-based keywords

**Analytics:**
- `traffic report` - Website traffic analysis
- `conversion report` - Conversion tracking data
- `SEO report` - Search ranking performance
- `ad performance` - Advertising metrics
- `social metrics` - Social media analytics

**SEO Objects:**
- `backlinks` - External links to website
- `meta tags` - SEO metadata
- `sitemap` - Website structure map
- `schema markup` - Structured data
- `robots.txt` - Crawler instructions

**Social Media:**
- `post` - Regular social media update
- `story` - Short-lived content (Instagram/Facebook Stories)
- `reel` - Short video content
- `carousel` - Multi-image posts
- `engagement` - Comments, likes, shares tracking

### AI Engineer Object Types

**Models:**
- `language model` - LLM (GPT, Claude, Gemini)
- `vision model` - Image processing
- `embedding model` - Vector embeddings
- `fine-tuned` - Customized models

**Prompts:**
- `system prompt` - Context/instructions
- `user prompt` - User input templates
- `few-shot` - Example-based prompts

**Training Data:**
- `raw` - Unprocessed data
- `cleaned` - Processed/validated
- `labeled` - Annotated for training
- `synthetic` - AI-generated data

---

## Automation Potential by Object Type

Different object types have varying automation potential. Use these rankings when prioritizing automation workflows:

| Automation Level | Definition | Object Type Examples | Automation % |
|-----------------|------------|---------------------|--------------|
| **Very High** | Fully automatable with existing tools | `leads: cold messages`, `reports: daily`, `emails: follow-up`, `candidates: sourcing`, `code: formatting` | >80% |
| **High** | Mostly automatable with minimal human review | `proposals: template-based`, `mockups: from wireframes`, `APIs: CRUD endpoints`, `interviews: scheduling` | 60-80% |
| **Medium** | Partial automation with human input required | `contracts: custom terms`, `logos: concept`, `databases: schema design`, `campaigns: strategy` | 40-60% |
| **Low** | Minimal automation, mostly manual | `creative illustrations`, `project interviews (cultural)`, `strategic planning`, `brand identity` | <40% |

**Priority for Library Population:**
1. Start with **Very High** automation objects - they provide immediate ROI
2. Focus on **High** automation objects that appear frequently in daily notes
3. Build templates for **Medium** automation to reduce manual effort
4. Document **Low** automation workflows for consistency

**Extraction Guideline:**
When extracting from daily notes, always capture the object type modifier when present:
- "Found 5 candidates on LinkedIn" → Object: `candidates`, Type: `found`, Count: 5
- "Sent cold outreach to 20 companies" → Object: `companies`, Type: `cold message sent`, Count: 20
- "Designed website mockup for client" → Object: `mockup`, Type: `website`, Status: completed

---

## Compound Entities Explanation

### What are Compound Entities?

In the taxonomy system, entities can be either **simple** or **compound**:

**Simple Entities:**
- Single-purpose, focused data structures
- Self-contained with minimal sub-components
- Examples: SETTINGS (configuration values), Accounts (variable fields)

**Compound Entities:**
- Multi-component compositions with interconnected sub-entities
- Act as centralized hubs connecting multiple related data types
- Enable complex relationships and cross-referencing
- Example: **LIBRARIES** (the primary compound entity)

### LIBRARIES as a Compound Entity

**LIBRARIES** is the flagship compound entity in the taxonomy system. It combines **5 distinct sub-entities** into a unified knowledge base:

```
LIBRARIES (Compound Entity)
├── Actions (Sub-entity 1)      → Standardized action verbs
├── Objects (Sub-entity 2)      → Business artifacts
├── Tools (Sub-entity 3)        → Software and platforms
├── Professions (Sub-entity 4)  → Job roles and titles
└── Responsibilities (Sub-entity 5) → Role-based duties
```

### Why LIBRARIES is Compound

**1. Multi-Component Composition**
- Contains 5 separate JSON libraries, each with its own schema
- Each sub-entity can exist independently but gains power when combined
- Total structure: 31 JSON files across multiple categories

**2. Interconnected Relationships**
- **Objects** define which **Actions** can be performed on them
- **Tools** are required to perform **Actions** on **Objects**
- **Professions** determine relevant **Actions**, **Objects**, and **Tools**
- **Responsibilities** map **Professions** to outcomes and **Actions**
- **Actions + Objects + Tools** compose **Tasks** in TASK_MANAGERS entity

**3. Cross-Entity Integration**
```
LIBRARIES connects to:
├── TASK_MANAGERS → Tasks = Actions + Objects (using Tools)
├── TALENTS → Employee professions determine skill requirements
├── JOBS → Job postings reference professions and required tools
├── BUSINESSES → Operations use standardized vocabulary
└── CATEGORIES → Taxonomy hierarchies built from LIBRARIES components
```

**4. Centralized Knowledge Hub**
- Single source of truth for organizational vocabulary
- Enforces naming consistency across all 32 team members
- Enables AI-powered task recommendation and automation
- Supports onboarding with 636+ standardized profession definitions

### Extraction Implications

When extracting data, recognizing LIBRARIES as a compound entity means:

**1. Validate Against All Sub-Entities:**
```yaml
Task Extraction:
  action: "send"           # Must exist in Actions sub-entity
  object: "cold_email"     # Must exist in Objects sub-entity
  tool: "gmail"            # Must exist in Tools sub-entity
  profession: "lead_generator" # Must exist in Professions sub-entity
```

**2. Track Cross-References:**
- When extracting a Task, link to parent Action, Object, and Tool IDs
- When finding new Actions/Objects/Tools, flag for library addition
- Maintain relationship integrity across all LIBRARIES components

**3. Leverage Compound Context:**
- Use profession to infer likely Actions and Objects
- Use department to filter relevant Tools
- Use Action-Object pairs to suggest appropriate Tools
- Use historical patterns to improve accuracy

### Other Compound Entities in the System

**TASK_MANAGERS** (Minor compound entity):
- Tasks + Projects + Milestones + Workflows
- Operational engine combining multiple work structures

**BUSINESSES** (Minor compound entity):
- Clients + Projects + Contracts + Communications
- Client lifecycle management across stages

**TALENTS** (Minor compound entity):
- Applications + Candidates + Employees + Presales
- Human capital tracking through talent pipeline

---

## Template Structures

Templates provide standardized formats for extracting and storing data. Each template type has a defined JSON schema.

### Task Template Structure

```json
{
  "template_type": "Task",
  "template_id": "TASK-{DEPT}-{NUMBER}",
  "template_name": "{Action} {Object}",

  "metadata": {
    "created_date": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "version": "1.0",
    "status": "Active | Archived | Deprecated"
  },

  "taxonomy": {
    "action": "string (from actions.json)",
    "object": "string (from objects.json)",
    "tool": "string (from tools.json)",
    "department": "string (HR|AI|Design|Dev|LG|Sales|Video)",
    "profession": "string (from professions.json)",
    "context": "string (where/why this task occurs)"
  },

  "task_details": {
    "name": "string (Action + Object format)",
    "description": "string (detailed explanation)",
    "purpose": "string (why this task exists)",
    "frequency": "One-time | Daily | Weekly | Monthly | As-needed",
    "complexity": "Beginner | Intermediate | Advanced | Expert"
  },

  "execution": {
    "inputs_required": ["string", "string"],
    "steps": ["STEP-{TASK_ID}-001", "STEP-{TASK_ID}-002"],
    "outputs_generated": ["string", "string"],
    "success_criteria": ["string", "string"]
  },

  "resources": {
    "tools_required": ["string", "string"],
    "skills_required": ["string", "string"],
    "documentation_links": ["URL", "URL"]
  },

  "timing": {
    "estimated_duration_min": "integer (minutes)",
    "estimated_duration_avg": "integer (minutes)",
    "estimated_duration_max": "integer (minutes)"
  },

  "relationships": {
    "parent_project": "PROJ-{DEPT}-{NUMBER} (optional)",
    "parent_milestone": "MIL-{PROJ_ID}-{NUMBER} (optional)",
    "dependencies": ["TASK-ID", "TASK-ID"],
    "follow_up_tasks": ["TASK-ID", "TASK-ID"],
    "related_entities": ["JOBS", "TALENTS", "BUSINESSES"]
  },

  "automation": {
    "automation_potential": "High | Medium | Low | None",
    "automation_notes": "string",
    "current_automation": "boolean",
    "automation_tool": "string (if automated)"
  },

  "priority": {
    "level": "Critical | High | Medium | Low",
    "inference_confidence": "0.0-1.0 (confidence in priority assignment)",
    "inference_reasoning": "string (how priority was determined)",
    "priority_score": "integer 0-100 (for Top-10 ranking)"
  },

  "accountability": {
    "raci": {
      "responsible": ["Person doing the work (can be multiple)"],
      "accountable": "Person ultimately answerable (ONLY ONE)",
      "consulted": ["People whose opinions are sought"],
      "informed": ["People kept up-to-date"]
    },
    "owner_confidence": "0.0-1.0 (confidence in owner assignment)",
    "status": "not_started | in_progress | blocked | completed",
    "blocked_by": "string (if status is blocked)"
  },

  "top_10": {
    "is_top_10": "boolean",
    "rank": "integer 1-10 (if in top 10)",
    "rank_date": "YYYY-MM-DD (when ranked)",
    "rank_reasoning": "string (why this is high priority)"
  },

  "quality": {
    "common_mistakes": ["string", "string"],
    "quality_checklist": ["string", "string"],
    "review_requirements": "boolean"
  },

  "source_tracking": {
    "source_file": "string (original file name)",
    "source_line": "integer (approximate)",
    "extraction_date": "YYYY-MM-DD",
    "confidence_score": "0.0-1.0 (overall extraction confidence)",
    "extraction_method": "explicit | inferred | hybrid",
    "inference_details": {
      "priority_inferred": "boolean",
      "owner_inferred": "boolean",
      "due_date_inferred": "boolean",
      "complexity_inferred": "boolean"
    }
  }
}
```

### Step Template Structure

```json
{
  "template_type": "Step",
  "step_id": "STEP-{TASK_ID}-{NUMBER}",
  "step_name": "string",

  "parent_task": {
    "task_id": "TASK-{DEPT}-{NUMBER}",
    "task_name": "string"
  },

  "step_details": {
    "step_number": "integer (1, 2, 3...)",
    "order": "integer (execution sequence)",
    "action": "string (verb describing step)",
    "detail": "string (specific instructions)",
    "expected_duration": "integer (minutes)"
  },

  "execution": {
    "tool_used": "string (specific tool)",
    "inputs": ["string", "string"],
    "outputs": ["string", "string"],
    "success_criteria": "string"
  },

  "relationships": {
    "dependencies": ["STEP-ID", "STEP-ID"],
    "next_steps": ["STEP-ID"],
    "parallel_steps": ["STEP-ID"]
  },

  "source_tracking": {
    "source_file": "string",
    "extraction_date": "YYYY-MM-DD"
  }
}
```

### Project Template Structure

```json
{
  "template_type": "Project",
  "project_id": "PROJ-{DEPT}-{NUMBER}",
  "project_name": "string",

  "metadata": {
    "status": "Planned | In Progress | Completed | Cancelled",
    "created_date": "YYYY-MM-DD",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "duration_days": "integer"
  },

  "ownership": {
    "department": "string",
    "primary_owner": "string",
    "team_members": ["string", "string"],
    "stakeholders": ["string", "string"]
  },

  "taxonomy": {
    "action": "string (high-level project action)",
    "object": "string (what is being built/delivered)",
    "tool": "string (primary tool or platform)",
    "context": "string (business context)"
  },

  "project_details": {
    "description": "string (detailed explanation)",
    "objectives": ["string", "string"],
    "deliverables": ["string", "string"],
    "impact": "Critical | High | Medium | Low",
    "budget": "number (if applicable)"
  },

  "structure": {
    "phases": ["PHASE-{PROJ_ID}-001", "PHASE-{PROJ_ID}-002"],
    "milestones": ["MIL-{PROJ_ID}-001", "MIL-{PROJ_ID}-002"],
    "tasks": ["TASK-ID", "TASK-ID"]
  },

  "outcomes": {
    "success_metrics": ["string", "string"],
    "achieved_results": "string (after completion)",
    "lessons_learned": ["string", "string"]
  },

  "source_tracking": {
    "source_file": "string",
    "extraction_date": "YYYY-MM-DD"
  }
}
```

### Workflow Template Structure

```json
{
  "template_type": "Workflow",
  "workflow_id": "WF-{DEPT}-{NUMBER}",
  "workflow_name": "string",

  "metadata": {
    "workflow_type": "Linear Sequential | Parallel Processing | Conditional Branching | Iterative Refinement | Event-Driven",
    "created_date": "YYYY-MM-DD",
    "version": "string",
    "status": "Active | Draft | Deprecated"
  },

  "workflow_details": {
    "description": "string",
    "purpose": "string",
    "trigger": "string (what initiates this workflow)",
    "frequency": "string (how often it runs)"
  },

  "steps": [
    {
      "step_id": "string",
      "step_number": "integer",
      "action": "string",
      "tool": "string",
      "duration": "integer (minutes)",
      "dependencies": ["step_id"],
      "parallel_with": ["step_id"],
      "conditional_logic": "string (if applicable)"
    }
  ],

  "automation": {
    "automated": "boolean",
    "automation_platform": "string (n8n, etc.)",
    "automation_level": "Fully Automated | Partially Automated | Manual"
  },

  "relationships": {
    "related_projects": ["PROJ-ID"],
    "related_tasks": ["TASK-ID"],
    "used_by_departments": ["string"],
    "used_by_professions": ["string"]
  },

  "performance": {
    "average_completion_time": "integer (minutes)",
    "success_rate": "number (0-100%)",
    "error_rate": "number (0-100%)",
    "time_saved_vs_manual": "integer (minutes or hours)"
  },

  "source_tracking": {
    "source_file": "string",
    "extraction_date": "YYYY-MM-DD"
  }
}
```

### Template Usage Guidelines

**When Extracting Data:**

1. **Identify Template Type:** Determine if source data represents a Task, Step, Project, or Workflow
2. **Map to Schema:** Extract fields according to the template structure above
3. **Generate IDs:** Use proper ID format (TASK-DEPT-NUMBER, STEP-TASK_ID-NUMBER, etc.)
4. **Validate Required Fields:** Ensure all required fields are populated
5. **Cross-Reference:** Link related templates (Steps to Tasks, Tasks to Projects)
6. **Track Source:** Always include source_tracking metadata

**Template Relationships:**
```
Project
  └── Phases
      └── Milestones
          └── Tasks
              └── Steps

Workflow
  └── Workflow Steps
      └── References Tasks (optional)
```

---

## Output File Specifications

### File Structure: Tasks_Templates.md

```markdown
# Task Templates Library
**Version:** 1.0  
**Last Updated:** [Date]  
**Total Templates:** [Count]

---

## Template Index

| ID | Name | Department | Action | Object | Tool | Status |
|----|------|------------|--------|--------|------|--------|
| TASK-LG-001 | Create Folder Structure | LG | create | folder_structure | filesystem | Active |
| TASK-AI-001 | Configure Logging System | AI | configure | logging_system | cursor | Active |

---

## Templates by Department

### LG Department

#### TASK-LG-001: Create Folder Structure

**Taxonomy:**
- **Action:** create
- **Object:** folder_structure
- **Tool:** filesystem
- **Department:** LG
- **Profession:** admin

**Description:**
Create folder structure for employee onboarding in LG department context.

**Inputs Required:**
- Employee name
- Department name
- Folder path

**Steps:**
1. [Step 1 ID] - Verify employee name
2. [Step 2 ID] - Create base folder structure
3. [Step 3 ID] - Set permissions

**Outputs:**
- Folder structure created
- Permissions configured

**Time Estimate:**
- Minimum: 5 minutes
- Average: 10 minutes
- Maximum: 15 minutes

**Success Criteria:**
- All required folders created
- Permissions set correctly
- Structure matches template

**Dependencies:**
- Prerequisites: Employee record exists
- Follow-up: Initialize documentation templates

**Related Entities:**
- Primary: TALENTS
- Interacts: LIBRARIES

**Automation:**
- Potential: High
- Notes: Can be fully automated with employee data

**Quality Checklist:**
- [ ] Folder structure matches template
- [ ] Permissions are correct
- [ ] Documentation initialized

**Common Mistakes:**
- Missing subfolders
- Incorrect permissions
- Wrong employee name

**Source:**
- File: Projects_Milestones_Tasks_Nov05-07_2025.md
- Line: ~75
- Date Extracted: 2025-11-25

---

[Continue with more templates...]
```

### File Structure: Step_Templates.md

```markdown
# Step Templates Library
**Version:** 1.0  
**Last Updated:** [Date]  
**Total Steps:** [Count]

---

## Step Index

| Step ID | Task ID | Step Number | Name | Action | Duration |
|---------|---------|-------------|------|--------|----------|
| STEP-TASK-LG-001-01 | TASK-LG-001 | 1 | Verify Employee Name | verify | 2 min |
| STEP-TASK-LG-001-02 | TASK-LG-001 | 2 | Create Base Folders | create | 5 min |

---

## Steps by Task

### TASK-LG-001: Create Folder Structure

#### STEP-TASK-LG-001-01: Verify Employee Name

**Parent Task:** TASK-LG-001  
**Step Number:** 1  
**Order:** 1

**Action:** verify  
**Detail:** Verify employee name and department assignment before creating folder structure

**Tool Used:** CRM System

**Expected Duration:** 2 minutes

**Dependencies:**
- None (first step)

**Outputs:**
- Verified employee name
- Confirmed department assignment

**Success Criteria:**
- Employee exists in system
- Department assignment confirmed

**Source:**
- File: Projects_Milestones_Tasks_Nov05-07_2025.md
- Date Extracted: 2025-11-25

---

[Continue with more steps...]
```

### File Structure: Project_Templates.md

```markdown
# Project Templates Library
**Version:** 1.0  
**Last Updated:** [Date]  
**Total Projects:** [Count]

---

## Project Index

| ID | Name | Department | Status | Impact | Duration |
|----|------|------------|--------|--------|----------|
| PROJ-LG-001 | LG Team Onboarding Solution | LG | Completed | High | 3 days |
| PROJ-AI-001 | Infrastructure Automation | AI | Completed | Critical | 5 days |

---

## Projects by Department

### LG Department

#### PROJ-LG-001: LG Team Onboarding Solution

**Status:** Completed  
**Department:** LG  
**Primary Owner:** Artemchuk Nikolay  
**Impact:** High

**Timeline:**
- Start Date: 2025-11-05
- End Date: 2025-11-07
- Duration: 3 days

**Taxonomy:**
- **Action:** implement
- **Object:** onboarding_system
- **Tool:** automated_workflows
- **Context:** LG Department

**Description:**
Successfully onboarded 4 new LG team members with comprehensive folder structure and documentation.

**Phases:**
1. Phase 1: Infrastructure Setup
2. Phase 2: Access & Permissions

**Milestones:**
- MIL-PROJ-LG-001-01: Employee Folder Creation
- MIL-PROJ-LG-001-02: Documentation Initialization

**Outcomes:**
- 4 team members onboarded
- Folder structures created
- Documentation initialized

**Source:**
- File: Projects_Milestones_Tasks_Nov05-07_2025.md
- Date Extracted: 2025-11-25

---

[Continue with more projects...]
```

---

## Extraction Process

### Phase 1: Preparation

1. **Scan Source Directory**
   ```bash
   List all files in: C:\Users\Dell\Dropbox\Nov25\Taxonomy\RestructuredData\
   ```

2. **Categorize Files**
   - Daily summaries
   - Project reports
   - Call notes
   - Comprehensive reviews

3. **Load Taxonomy Libraries**
   - Read `Framework/Entities/LIBRARIES/actions.json`
   - Read `Framework/Entities/LIBRARIES/objects.json`
   - Read `Framework/Entities/LIBRARIES/tools.json`
   - Read `Framework/Entities/LIBRARIES/professions.json`

### Phase 2: Extraction

#### For Each File:

1. **Parse Document Structure**
   - Identify sections (Projects, Tasks, Steps, etc.)
   - Extract metadata (dates, owners, departments)
   - Identify taxonomy patterns

2. **Extract Tasks**
   - Find all task patterns
   - Extract taxonomy components
   - Map to libraries
   - Generate unique IDs

3. **Extract Steps**
   - Find step patterns within tasks
   - Link to parent tasks
   - Extract step details

4. **Extract Projects**
   - Find project sections
   - Extract project metadata
   - Link to phases and milestones

5. **Extract Milestones**
   - Find milestone sections
   - Link to parent projects/phases
   - Extract milestone details

6. **Extract Action Items**
   - Find action item sections
   - Extract owner, priority, timeline
   - Link to related projects

### Phase 3: Organization

1. **Deduplicate**
   - Compare extracted items
   - Merge duplicates
   - Keep most complete version

2. **Validate Taxonomy**
   - Verify all actions in library
   - Verify all objects in library
   - Verify all tools in library
   - Flag missing entries for library update

3. **Generate IDs**
   - Tasks: TASK-[DEPT]-[NUMBER]
   - Steps: STEP-[TASK_ID]-[NUMBER]
   - Projects: PROJ-[DEPT]-[NUMBER]
   - Milestones: MIL-[PROJ_ID]-[NUMBER]
   - Action Items: ACT-[DEPT]-[NUMBER]

4. **Cross-Reference**
   - Link steps to tasks
   - Link tasks to projects
   - Link milestones to projects
   - Link action items to projects

### Phase 4: Output Generation

1. **Create Template Files**
   - Generate `Tasks_Templates.md`
   - Generate `Step_Templates.md`
   - Generate `Project_Templates.md`
   - Generate `Milestone_Templates.md`
   - Generate `Action_Items_Templates.md`
   - Generate `Workflow_Templates.md` (derived from project workflows)

2. **Format Output**
   - Use consistent markdown format
   - Include all required fields
   - Add source references
   - Include cross-references

3. **Generate Indexes**
   - Create index tables at top of each file
   - Sort by department, then by ID
   - Include quick lookup information

---

## Daily Notes Extraction Guidelines

### Overview

Daily notes, call transcripts, and operational logs are rich sources of real-world data for populating taxonomy libraries. This section provides systematic guidelines for extracting structured information from daily activities to continuously improve the knowledge base.

### 4-Step Daily Report Workflow

**Step 1: Read Department Prompt Logs**
- **Location:** `C:\Users\Dell\Dropbox\Nov25\{DEPT} Nov25\{DEPT} prompt log.md`
- **Purpose:** Capture today's context and activities
- **What to Extract:**
  - Current priorities and focus areas
  - Active projects and tasks
  - Team member assignments
  - Tools being used
  - Challenges encountered

**Step 2: Process Daily Notes/Transcripts**
- **Sources:**
  - Call transcripts (meetings, standups, 1-on-1s)
  - Daily activity reports
  - Project status updates
  - Chat logs (Discord, Slack)
  - Email communications
- **Processing Approach:**
  - Use department-specific section emphasis (see below)
  - Extract using 21-section framework mindset
  - Match participants to employee directory
  - Match projects to project directory
  - Identify implicit tasks and actions

**Step 3: Generate Structured Extraction**
- **Output Format:** Follow template structures defined in this document
- **Required Sections:**
  - Executive Summary (high-level overview)
  - Action Items & Tasks (structured with ACTION + OBJECT + CONTEXT)
  - Projects & Features (project updates)
  - Tools & Resources (tools mentioned)
  - Key Deliverables (what was produced)
  - Metrics & Statistics (quantifiable outcomes)
  - Challenges & Solutions (problems encountered)

**Step 4: Populate Libraries Systematically**
- **Actions Library:** Extract action verbs from completed tasks
- **Objects Library:** Identify deliverables and artifacts mentioned
- **Tools Library:** Document tools referenced in daily work
- **Professions Library:** Track role variations and terminology
- **Metrics Library:** Calculate department KPIs from daily data

### Department-Specific Section Emphasis

Each department should emphasize different aspects when extracting from daily notes:

#### HR Department
**Primary Sections:** Tasks, Team Context, Onboarding
- Focus on: Candidate screening, interview coordination, onboarding activities
- Extract: Job postings, candidate interactions, hiring metrics
- Tools emphasis: CRM usage, communication platforms, VS Code documentation
- Key metrics: Time-to-hire, candidates sourced, interview-to-offer ratio

#### LG (Lead Generation) Department
**Primary Sections:** Tasks, Lead Gen & Sales Context
- Focus on: Prospecting activities, lead enrichment, outreach campaigns
- Extract: Lead lists, email campaigns, meeting bookings, conversion data
- Tools emphasis: Gemini (LinkedIn analysis), Perplexity (news search), n8n (automation)
- Key metrics: Leads generated, response rate, meetings booked, deals closed

#### Design Department
**Primary Sections:** Tasks, Tools, Design & Creative Context
- Focus on: Design deliverables, client feedback, revision cycles
- Extract: Mockups, prototypes, design systems, client approvals
- Tools emphasis: Figma projects, Midjourney generations, Leonardo.ai assets
- Key metrics: Projects completed, revision rounds, client satisfaction

#### Dev Department
**Primary Sections:** Tasks, Technical Architecture, Dev Context
- Focus on: Code commits, feature implementations, bug fixes, deployments
- Extract: Pull requests, technical decisions, architecture changes
- Tools emphasis: Cursor IDE usage, Claude integration, GitHub activity
- Key metrics: Deployment frequency, bug resolution time, code quality

#### AI Department
**Primary Sections:** Tasks, Tools, Architecture, Documentation
- Focus on: Automation workflows, AI integrations, prompt engineering
- Extract: Prompts created, workflows automated, integrations built
- Tools emphasis: Claude/Gemini/Perplexity usage, n8n workflows, Cursor development
- Key metrics: Automation coverage, time saved, workflow efficiency, accuracy rate

#### Sales Department
**Primary Sections:** Tasks, Lead Gen & Sales Context
- Focus on: Proposal creation, client meetings, deal progression
- Extract: Proposals sent, demos conducted, contracts negotiated
- Tools emphasis: Claude (proposal analysis), Gemini (research), CRM usage
- Key metrics: Pipeline value, conversion rate, deal cycle length, win rate

#### Video Department
**Primary Sections:** Tasks, Tools, Design & Creative Context
- Focus on: Video production, editing, rendering, publishing
- Extract: Videos created, scripts written, footage processed
- Tools emphasis: Premiere Pro, After Effects, ElevenLabs, Claude (scripts)
- Key metrics: Videos produced, production time, engagement rate, client satisfaction

### Extraction Patterns from Daily Notes

#### Extract Implicit Tasks
**Pattern:** When problems or needs are discussed, extract the implied task

**Example:**
- **Transcript:** "We need to figure out why the LinkedIn scraper is timing out"
- **Extracted Task:**
  - Action: Debug
  - Object: LinkedIn scraper timeout issue
  - Tool: n8n, Chrome DevTools
  - Owner: AI Department
  - Priority: High
  - Status: not_started

#### Infer Priority from Context
**Priority Indicators:**

| Priority | Keywords | Context Clues |
|----------|----------|---------------|
| **Critical** | "blocking", "urgent", "ASAP", "emergency" | Stops other work, affects clients/revenue |
| **High** | "important", "soon", "this week", "deadline approaching" | Time-sensitive, affects multiple people |
| **Medium** | "should", "need to", "when possible" | Standard work, planned activities |
| **Low** | "nice to have", "someday", "consider", "maybe" | Can be deferred, nice-to-have improvements |

#### Match Participants with Confidence
**Matching Strategies:**

1. **Direct Name Match** (Confidence: High 0.9-1.0)
   - Exact name mentioned: "Olha said..."
   - Match to employee directory with ID

2. **Contextual Clues** (Confidence: Medium 0.6-0.8)
   - Department discussion: "The designer mentioned..." → likely Design dept employee
   - Tool reference: "The person using Figma..." → likely designer
   - Project association: "The person working on DGN..." → check project team

3. **Communication Handles** (Confidence: High 0.9-1.0)
   - Telegram @mention → match to employee Telegram handle
   - Email address → match to employee email

4. **Voice/Speech Patterns** (Confidence: Medium-Low 0.5-0.7)
   - Language, accent, terminology
   - Requires human verification

5. **Multi-lingual Matching** (Confidence: Medium 0.7-0.9)
   - Cyrillic transliteration: Николай → Nikolay/Nikolai/Mykola
   - Handle variations

**When Confidence is Low (<0.6):**
- Flag for manual review
- Document reasoning: "Likely Olha based on Figma discussion, but not explicitly named"
- Request clarification in follow-up

#### Auto-Populate Metadata
When a confident match is made, automatically populate:
- Employee ID
- Department
- Profession
- Contact information
- Project associations

**Example:**
- **Match:** "Olha" → Shelep Olha (ID: 86641)
- **Auto-populate:**
  - Department: Design
  - Profession: UI/UX Designer
  - Telegram: @olhashelep
  - Email: olha@remotehelpers.com
  - Active Projects: DGN, LibDev

### Library Population from Daily Notes

#### Actions Library Updates

**Extraction Rule:** Identify action verbs from completed tasks

**Pattern:**
```
Transcript: "I created the wireframes and sent them to the client"
Actions extracted:
- "create" (if not in library, add with definition)
- "send" (verify exists in library)

Add to actions.json:
{
  "action_id": "ACT-CREA-023",
  "verb": "Create",
  "category": "Creation",
  "complexity": "Intermediate",
  "common_objects": ["wireframes", "mockups", "designs"],
  "source": "Daily notes - Design dept - 2025-11-10"
}
```

#### Objects Library Updates

**Extraction Rule:** Identify deliverables and artifacts mentioned

**Pattern:**
```
Transcript: "We delivered the onboarding documentation and the API integration guide"
Objects extracted:
- "onboarding_documentation" (check if exists)
- "api_integration_guide" (check if exists)

Add to objects.json:
{
  "object_id": "OBJ-DOC-034",
  "name": "API Integration Guide",
  "category": "Documents",
  "description": "Technical documentation for API integration",
  "common_actions": ["Create", "Update", "Review"],
  "storage_location": "Entities/TASK_MANAGERS/Documentation/",
  "source": "Daily notes - Dev dept - 2025-11-10"
}
```

#### Tools Library Updates

**Extraction Rule:** Document tools mentioned in daily work

**Pattern:**
```
Transcript: "I used Leonardo.ai to generate the hero image"
Tool extracted: "Leonardo.ai"

Verify in tools.json:
- If exists: Increment usage counter
- If new: Add full tool definition
- Track: Which department, for what purpose, frequency

Update tools.json:
{
  "tool_id": "TOOL-AI-015",
  "name": "Leonardo.ai",
  "category": "AI/Image Generation",
  "departments_using": ["Design", "Marketing"],
  "use_cases": ["Hero images", "Product mockups", "Marketing visuals"],
  "usage_frequency": "Daily - 5-10 generations/day",
  "source": "Daily notes tracking - 2025-11-10"
}
```

#### Professions Library Updates

**Extraction Rule:** Track role variations and terminology

**Pattern:**
```
Transcript: "Our lead gen specialist processed 50 leads today"
Role variation: "lead gen specialist"

Check professions.json:
- Standard term: "Lead Generator"
- Variations: ["Lead Gen Specialist", "Lead Generation Specialist", "LG Specialist"]
- Add variation if new

Update professions.json to include all variations for better matching
```

#### Metrics Library Updates

**Extraction Rule:** Calculate department KPIs from daily data

**Pattern:**
```
From daily notes over one week:
- Monday: 3 designs completed
- Tuesday: 5 designs completed
- Wednesday: 4 designs completed
- Thursday: 6 designs completed
- Friday: 5 designs completed

Calculate:
- Weekly average: 4.6 designs/day
- Weekly total: 23 designs
- Revision rounds average: 2.8 (from notes)
- Client satisfaction: 4.7/5.0 (from feedback)

Update metrics library:
{
  "department": "Design",
  "metric": "Weekly Design Output",
  "value": 23,
  "average_daily": 4.6,
  "period": "2025-11-04 to 2025-11-08",
  "trend": "up 15% from previous week"
}
```

### Best Practices

1. **Consistency is Key**
   - Use standardized formats for all extractions
   - Follow ACTION + OBJECT + CONTEXT pattern
   - Apply same confidence scoring methodology

2. **Validate Before Committing**
   - Cross-reference with existing libraries
   - Check for duplicates
   - Verify formatting and structure

3. **Document Sources**
   - Always include source file reference
   - Note extraction date
   - Record confidence levels

4. **Iterate and Improve**
   - Review low-confidence extractions
   - Update matching rules based on failures
   - Refine extraction patterns over time

5. **Automate Where Possible**
   - Use scripts for repetitive extractions
   - Auto-populate known values
   - Flag only uncertain items for human review

---

## Prioritization System

### Overview

A robust prioritization system ensures that the most important and urgent tasks are always visible and actionable. This section defines a 4-level priority framework with clear inference rules, status tracking, complexity assessment, and RACI accountability matrices.

### 4-Level Priority Framework

| Level | Definition | When to Use | Expected Response Time |
|-------|------------|-------------|----------------------|
| **Critical** | Blocks other work, immediate action required | Production outage, client emergency, revenue-impacting issue | Within hours |
| **High** | Important and time-sensitive | Approaching deadline, affects multiple people/departments | Within 1-2 days |
| **Medium** | Standard priority | Planned work, normal operations | Within 1 week |
| **Low** | Nice to have, can be deferred | Improvements, optimizations, future enhancements | When capacity allows |

### Priority Inference Rules

When extracting tasks from unstructured data, use these rules to infer priority:

#### Rule 1: Urgency Keywords

**Critical Indicators:**
- "blocking", "blocked", "urgent", "ASAP", "emergency", "immediately", "critical", "production down", "client escalation"

**High Indicators:**
- "important", "soon", "this week", "deadline approaching", "time-sensitive", "high priority", "needs attention"

**Medium Indicators:**
- "should", "need to", "when possible", "upcoming", "planned", "scheduled"

**Low Indicators:**
- "nice to have", "someday", "consider", "maybe", "would be good", "enhancement", "optimization"

#### Rule 2: Business Impact Assessment

**Critical Impact:**
- Affects revenue or client relationships
- Stops other team members from working
- Security vulnerability or data breach
- Legal or compliance issue

**High Impact:**
- Affects multiple departments or projects
- Delays planned releases or deliverables
- Impacts team productivity significantly
- Important client request

**Medium Impact:**
- Affects single department or project
- Part of normal workflow
- Standard feature or improvement
- Internal tool or process

**Low Impact:**
- Affects single person
- Nice-to-have feature
- Internal optimization
- Future consideration

#### Rule 3: Deadline Proximity

- **Critical:** Due today or overdue
- **High:** Due within 1-3 days
- **Medium:** Due within 1 week
- **Low:** Due in 2+ weeks or no specific deadline

#### Rule 4: Dependency Analysis

- **Critical:** Blocks 3+ other tasks or people
- **High:** Blocks 1-2 other tasks or people
- **Medium:** Has dependencies but not blocking
- **Low:** No dependencies

### Confidence Scoring for Priority

When priority is inferred (not explicitly stated), assign a confidence score:

| Confidence | Range | Meaning | Action |
|------------|-------|---------|--------|
| **High** | 0.8-1.0 | Clear urgency indicators, explicit deadline | Accept inferred priority |
| **Medium** | 0.5-0.79 | Some indicators, contextual clues | Accept but flag for review |
| **Low** | 0.0-0.49 | Weak indicators, assumptions made | Flag for manual assignment |

**Example:**
```yaml
Task: "Debug the LinkedIn scraper timeout"
Priority: High
Confidence: 0.7 (Medium)
Reasoning: "timeout" suggests urgency, affects LG department operations, but no explicit "urgent" keyword
```

### Status Tracking System

Use a 4-state status model for clear progress visibility:

| Status | Definition | Indicators | Next Actions |
|--------|------------|------------|--------------|
| **not_started** | Task defined but work hasn't begun | Future tense: "will do", "need to" | Assign owner, set timeline |
| **in_progress** | Work actively happening | Present tense: "working on", "developing" | Monitor progress, check blockers |
| **blocked** | Cannot continue due to dependency/issue | "blocked by", "waiting for", "stuck" | Identify blocker, escalate |
| **completed** | Finished and verified | Past tense: "done", "finished", "delivered" | Archive, update metrics |

**Status Inference from Transcript:**

| Phrase | Inferred Status |
|--------|----------------|
| "I need to..." | not_started |
| "I'm working on..." | in_progress |
| "I'm stuck because..." | blocked |
| "I finished..." | completed |
| "Waiting for..." | blocked |
| "Will start next..." | not_started |

### Complexity Assessment

Assign complexity levels to estimate effort and required expertise:

| Level | Definition | Time Estimate | Skill Required |
|-------|------------|---------------|----------------|
| **Beginner** | Can be completed with basic training | < 2 hours | Entry-level knowledge |
| **Intermediate** | Requires some experience and familiarity | 2-8 hours | Working knowledge |
| **Advanced** | Requires significant expertise | 1-3 days | Deep expertise |
| **Expert** | Requires specialized knowledge or mastery | 3+ days | Subject matter expert |

**Complexity Inference Clues:**

- **Beginner:** "simple", "quick", "straightforward", "basic"
- **Intermediate:** "standard", "typical", "normal workflow"
- **Advanced:** "complex", "challenging", "requires careful thought"
- **Expert:** "highly specialized", "critical architecture decision", "deep expertise needed"

### RACI Matrix Integration

For every task, define clear accountability using the RACI framework:

**RACI Definitions:**

- **Responsible (R):** Person(s) doing the work (can be multiple)
- **Accountable (A):** Person ultimately answerable (**only ONE** per task)
- **Consulted (C):** People whose opinions are sought (two-way communication)
- **Informed (I):** People kept up-to-date on progress (one-way communication)

**RACI Assignment Rules:**

1. **Every task MUST have exactly ONE Accountable person**
2. **Responsible can be multiple people for collaborative work**
3. **Consulted should be limited to 2-3 key stakeholders**
4. **Informed can include broader groups (department leads, etc.)**

**Example Task with RACI:**

```yaml
Task: "Create employee onboarding documentation"
RACI:
  responsible: "Shelep Olha (Design) - creating the documentation"
  accountable: "Artemchuk Nikolay (AI - Project Manager) - ultimate owner"
  consulted: ["Nealova Evgeniya (HR Manager)", "Development Team Lead"]
  informed: ["All Department Leads", "CEO"]
```

**RACI Inference from Transcript:**

| Pattern | RACI Role |
|---------|-----------|
| "X is doing..." | Responsible: X |
| "X owns this..." | Accountable: X |
| "Check with X..." | Consulted: X |
| "Let X know..." | Informed: X |
| "X's project..." | Accountable: X |
| "X and Y are working on..." | Responsible: X, Y |

### Priority Matrix Visualization

Tasks can be visualized in a 2x2 priority matrix:

```
        Urgent
          |
    High  |  Critical
    ------+------
    Medium|  Low
          |
      Not Urgent
```

**Quadrants:**

1. **Critical (Urgent + High Impact):** Do immediately
2. **High (Urgent + Medium Impact):** Schedule soon
3. **Medium (Not Urgent + High Impact):** Plan carefully
4. **Low (Not Urgent + Medium/Low Impact):** Defer or delegate

---

## Top-10 Priority Management System

### Overview

The Top-10 system provides instant visibility into the most critical and time-sensitive tasks across all departments. This system automatically generates and maintains a prioritized list of the top 10 action items that need immediate attention.

### Automatic Top-10 Generation Algorithm

**Step-by-Step Process:**

**Step 1: Extract All Action Items**
- Gather all tasks from daily notes, call transcripts, project reports
- Include tasks from all departments and sources
- Ensure each task has required fields (action, object, priority, status)

**Step 2: Filter by Priority**
- **First Pass:** All **Critical** priority tasks
- **Second Pass:** All **High** priority tasks
- **Third Pass:** **Medium** priority tasks only if fewer than 10 items

**Step 3: Sort Within Priority Level**
- Primary sort: **Due date** (earliest first)
- Secondary sort: **Business impact** (revenue/client impact first)
- Tertiary sort: **Number of dependencies** (more blockers first)

**Step 4: Weight by Additional Factors**

Apply weighting scores (0-100 scale):

| Factor | Weight | Calculation |
|--------|--------|-------------|
| **Priority** | 40% | Critical=100, High=70, Medium=40, Low=10 |
| **Deadline** | 30% | Overdue=100, Today=90, This week=70, Next week=50, Later=30 |
| **Business Impact** | 20% | Client/Revenue=100, Multi-dept=70, Single dept=40, Internal=20 |
| **Dependencies** | 10% | Blocks 3+=100, Blocks 1-2=70, No blocking=30 |

**Formula:**
```
Priority_Score = (Priority × 0.4) + (Deadline × 0.3) + (Impact × 0.2) + (Dependencies × 0.1)
```

**Step 5: Generate Ranked Top-10 List**
- Select top 10 tasks by Priority_Score
- Rank from highest to lowest
- Include tie-breakers (complexity, department balance)

### Access Pattern for "At Reach" Items

Design the Top-10 display for instant visibility:

#### Dashboard Layout

```markdown
# 🔥 TOP 10 PRIORITIES

## Critical (Do Today)
1. 🔴 [TASK-LG-045] Debug LinkedIn scraper timeout - **Blocking 3 team members**
   - Owner: AI Dept | Due: Today | Score: 95
   - Status: 🟡 In Progress | Blocker: API rate limiting

2. 🔴 [TASK-DEV-102] Fix production database connection pool - **Client impact**
   - Owner: Dev Dept | Due: Overdue | Score: 93
   - Status: 🔴 Blocked | Blocker: Waiting for DB credentials

## High (This Week)
3. 🟠 [TASK-DESIGN-078] Complete DGN platform redesign mockups - **Client deadline**
   - Owner: Shelep Olha | Due: Nov 12 | Score: 85
   - Status: 🟢 On Track | Progress: 70%

4. 🟠 [TASK-HR-034] Finalize job postings for 3 developer roles - **Hiring goal**
   - Owner: HR Dept | Due: Nov 13 | Score: 82
   - Status: 🟡 In Progress | Progress: 50%

[... continues to #10]
```

#### Status Indicators

| Symbol | Meaning | CSS Class |
|--------|---------|-----------|
| 🔴 | Blocked / Overdue | `.status-blocked` |
| 🟡 | In Progress / At Risk | `.status-progress` |
| 🟢 | On Track / Completed | `.status-on-track` |
| ⚪ | Not Started | `.status-not-started` |

### Department KPI Integration

Each department tracks specific KPIs that inform prioritization:

#### HR Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Time-to-Hire | Days from posting to offer | ≤ 21 days | 18 days | 🟢 On Target |
| Candidates Sourced/Week | Weekly new candidates | 15-20 | 17 | 🟢 On Target |
| Interview-to-Offer Ratio | Offers / Interviews | ≥ 30% | 35% | 🟢 Above Target |
| Onboarding Completion | % completed within 1 week | 100% | 100% | 🟢 Perfect |

**Priority Impact:** If Time-to-Hire exceeds 21 days → Sourcing tasks become High priority

#### LG Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Leads Generated/Week | Weekly new leads | 100-150 | 142 | 🟢 On Target |
| Response Rate | Replies / Emails sent | ≥ 6% | 7.2% | 🟢 Above Target |
| Meetings Booked | Weekly meetings scheduled | 15-20 | 18 | 🟢 On Target |
| Deals Closed | Monthly deals won | 8-12 | 10 | 🟢 On Target |
| Automation Time Saved | Hours saved via n8n | 4-5 hrs/day | 4.8 hrs | 🟢 On Target |

**Priority Impact:** If Response Rate drops below 5% → Campaign optimization becomes Critical

#### Design Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Projects Completed/Week | Weekly deliveries | 5-7 | 6 | 🟢 On Target |
| Revision Rounds | Avg iterations per project | ≤ 3 | 2.8 | 🟢 On Target |
| Client Satisfaction | Survey score (1-5) | ≥ 4.5 | 4.7 | 🟢 Above Target |
| Figma Component Growth | New components/month | +10 | +12 | 🟢 Above Target |

**Priority Impact:** If Revision Rounds exceed 4 → Design quality review becomes High priority

#### Dev Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Deployment Frequency | Deployments per week | ≥ 3 | 4 | 🟢 Above Target |
| Bug Resolution Time | Avg hours to fix | ≤ 24 hrs | 18 hrs | 🟢 On Target |
| Code Quality Score | Automated analysis | ≥ 85% | 88% | 🟢 Above Target |
| Sprint Velocity | Story points/sprint | 40-50 | 45 | 🟢 On Target |

**Priority Impact:** If Bug Resolution Time exceeds 48hrs → Critical bugs escalate to Critical priority

#### AI Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Automation Coverage | % of processes automated | 60% | 67% | 🟢 Above Target |
| Time Saved | Daily hours saved | 4-5 hrs | 4.8 hrs | 🟢 On Target |
| Workflow Efficiency | Successful runs / Total | ≥ 95% | 97% | 🟢 Above Target |
| AI Tool Utilization | Active tools / Total tools | ≥ 80% | 85% | 🟢 Above Target |

**Priority Impact:** If Workflow Efficiency drops below 90% → Debugging becomes Critical

#### Sales Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Pipeline Value | Total deal value | €200k+ | €245k | 🟢 Above Target |
| Conversion Rate | Deals won / Total | ≥ 25% | 28% | 🟢 Above Target |
| Deal Cycle Length | Days from lead to close | ≤ 45 days | 42 days | 🟢 On Target |
| Win Rate | % of proposals won | ≥ 30% | 32% | 🟢 Above Target |

**Priority Impact:** If Conversion Rate drops below 20% → Proposal quality review becomes High priority

#### Video Department KPIs

| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Videos Completed/Week | Weekly deliveries | 3-5 | 4 | 🟢 On Target |
| Production Time | Avg hours per video | ≤ 8 hrs | 7.5 hrs | 🟢 On Target |
| Engagement Rate | Views / Subscribers | ≥ 15% | 17% | 🟢 Above Target |
| Client Satisfaction | Survey score (1-5) | ≥ 4.5 | 4.6 | 🟢 On Target |

**Priority Impact:** If Production Time exceeds 12hrs → Workflow optimization becomes High priority

### Top-10 Refresh Strategy

**Frequency:** Update daily at start of business day

**Process:**

1. **Morning Update (9:00 AM)**
   - Run Top-10 generation algorithm
   - Pull latest data from daily notes and overnight activity
   - Recalculate all priority scores
   - Generate fresh ranked list

2. **Archive Completed Items**
   - Move completed tasks to archive
   - Update completion metrics
   - Track average completion time

3. **Promote Next Items**
   - Fill vacated spots with next highest-priority tasks
   - Ensure department balance (not all from one dept)
   - Maintain mix of task types

4. **Alert on Newly Critical Items**
   - Email notifications for new Critical tasks
   - Slack/Discord alerts for department-specific Critical items
   - Dashboard red highlighting for attention

**Triggers for Immediate Refresh:**

- New Critical task created
- Task becomes Blocked
- Major deadline change
- Department KPI threshold breach

### Visualization Recommendations

#### 1. Priority Matrix Dashboard

```
┌─────────────────────────────────────┐
│  Urgent & Important  │  Not Urgent  │
│    [3 Critical]      │  & Important │
│    🔴 🔴 🔴          │  [2 High]    │
│                      │  🟠 🟠       │
├──────────────────────┼──────────────┤
│  Urgent & Less       │  Not Urgent  │
│   Important          │  & Less Imp  │
│   [3 High]           │  [2 Medium]  │
│   🟠 🟠 🟠          │  🟡 🟡       │
└──────────────────────┴──────────────┘
```

#### 2. Burndown Chart

```
Tasks
 10 │●
    │ ●
  8 │  ●
    │   ●
  6 │    ●
    │     ●
  4 │      ●
    │       ●
  2 │        ●
    │         ●
  0 └──────────────── Days
    Mon Tue Wed Thu Fri
```

#### 3. Status Distribution

```
🔴 Blocked:     2 tasks (20%)  ██
🟡 In Progress: 5 tasks (50%)  █████
🟢 On Track:    3 tasks (30%)  ███
```

#### 4. Top-10 Checklist

```markdown
## Top 10 Tasks - Week of Nov 10, 2025

- [ ] 🔴 #1 (95pts) Debug LinkedIn scraper - AI Dept
- [ ] 🔴 #2 (93pts) Fix DB connection pool - Dev Dept
- [x] 🟠 #3 (85pts) DGN redesign mockups - Design Dept [COMPLETED]
- [ ] 🟠 #4 (82pts) Developer job postings - HR Dept
- [ ] 🟠 #5 (78pts) Q4 sales proposal - Sales Dept
- [ ] 🟠 #6 (75pts) Video editing workflow - Video Dept
- [ ] 🟠 #7 (72pts) n8n lead enrichment - AI Dept
- [ ] 🟡 #8 (68pts) Employee onboarding docs - Design Dept
- [ ] 🟡 #9 (65pts) API documentation update - Dev Dept
- [ ] 🟡 #10 (62pts) Cold email campaign - LG Dept

Progress: 1/10 completed (10%) | 2 Blocked | 5 In Progress | 2 Not Started
```

### Department-Specific Top-10 Views

Each department can filter the global Top-10 to see only their tasks:

**Example: Design Department View**

```markdown
## 🎨 Design Top Priorities

1. 🟠 [TASK-DESIGN-078] DGN platform redesign mockups
   - Due: Nov 12 | Owner: Shelep Olha | Score: 85
   - Progress: 70% | Status: 🟢 On Track

2. 🟡 [TASK-DESIGN-091] Employee onboarding docs
   - Due: Nov 15 | Owner: Shelep Olha | Score: 68
   - Progress: 40% | Status: 🟡 In Progress

3. 🟡 [TASK-DESIGN-103] LibDev UI components
   - Due: Nov 18 | Owner: Design Team | Score: 55
   - Progress: 20% | Status: 🟡 In Progress
```

### Integration with Task Templates

Every task in the Top-10 should link to its full template:

```markdown
**Task #1:** Debug LinkedIn scraper timeout

[View Full Details](../Tasks/TASK-LG-045.md)

**Quick Summary:**
- Priority: Critical (Score: 95)
- Blocking: 3 team members (Lead Gen campaign halted)
- Owner: AI Department
- RACI: R=Perederii Vladislav | A=Artemchuk Nikolay | C=[LG Team] | I=[All Dept Leads]
- Complexity: Advanced
- Time Estimate: 4-6 hours
- Due: Today (Nov 10, 2025)
```

---

## Validation Rules

### Task Validation

✅ **Required Fields Present:**
- [ ] ID (unique, properly formatted)
- [ ] Name (non-empty)
- [ ] Taxonomy (action, object, tool, department)
- [ ] Description (non-empty)
- [ ] Status (valid value)

✅ **Taxonomy Validation:**
- [ ] Action exists in actions.json OR is valid new action
- [ ] Object exists in objects.json OR is valid new object
- [ ] Tool exists in tools.json OR is valid new tool
- [ ] Department is valid (AI, Design, Dev, HR, LG, Sales, Video)
- [ ] Profession exists in professions.json OR is valid

✅ **Data Quality:**
- [ ] Dates are valid (YYYY-MM-DD format)
- [ ] Priorities are valid (Critical, High, Medium, Low)
- [ ] Status values are valid
- [ ] No duplicate IDs

### Step Validation

✅ **Required Fields Present:**
- [ ] ID (unique, properly formatted)
- [ ] Task ID (references valid task)
- [ ] Step number (positive integer)
- [ ] Name (non-empty)
- [ ] Order (positive integer)

✅ **Relationship Validation:**
- [ ] Parent task exists
- [ ] Step number is unique within task
- [ ] Order matches step number (or is sequential)

### Project Validation

✅ **Required Fields Present:**
- [ ] ID (unique, properly formatted)
- [ ] Name (non-empty)
- [ ] Status (valid value)
- [ ] Department (valid)
- [ ] Taxonomy (action, object, tool, context)

✅ **Relationship Validation:**
- [ ] All referenced phases exist
- [ ] All referenced milestones exist
- [ ] Timeline dates are valid

### Cross-Reference Validation

✅ **Link Integrity:**
- [ ] All step task_ids reference valid tasks
- [ ] All milestone project_ids reference valid projects
- [ ] All action item project_ids reference valid projects
- [ ] No orphaned references

---

## Examples

### Example 1: Complete Task Extraction

**Source Text:**
```markdown
### Phase 1: Infrastructure Setup ✅
**Milestone 1.1: Employee Folder Creation**
- ✅ Create-Folder-Structure for Employee-Artemchuk-Nikolay using FileSystem in LG-Department-Context
  - Owner: Admin
  - Priority: High
  - Completed: Nov 5, 2025
```

**Extracted Task:**
```yaml
Task:
  id: "TASK-LG-001"
  name: "Create Folder Structure"
  taxonomy:
    action: "create"
    object: "folder_structure"
    tool: "filesystem"
    department: "LG"
    profession: "admin"
  description: "Create folder structure for Employee Artemchuk Nikolay in LG Department context"
  owner: "Admin"
  priority: "High"
  status: "Completed"
  timeline:
    completed_date: "2025-11-05"
  context: "LG Department onboarding"
  source_file: "Projects_Milestones_Tasks_Nov05-07_2025.md"
  source_line: 75
```

### Example 2: Complete Project Extraction

**Source Text:**
```markdown
## PROJECT 1: LG Team Onboarding Solution ✅ COMPLETED

**Project Metadata:**
- **Status:** Completed
- **Department:** LG (Legal & Governance)
- **Primary Owner:** Artemchuk Nikolay
- **Timeline:** Nov 5-7, 2025
- **Impact:** High - Streamlined onboarding for 4 team members

### Project Overview
Action: **Implement** + Object: **Onboarding System** + Tool: **Automated Workflows** + Context: **LG Department**

Successfully onboarded 4 new LG team members with comprehensive folder structure and documentation.
```

**Extracted Project:**
```yaml
Project:
  id: "PROJ-LG-001"
  name: "LG Team Onboarding Solution"
  status: "Completed"
  department: "LG"
  primary_owner: "Artemchuk Nikolay"
  timeline:
    start_date: "2025-11-05"
    end_date: "2025-11-07"
    duration_days: 3
  impact: "High"
  taxonomy:
    action: "implement"
    object: "onboarding_system"
    tool: "automated_workflows"
    context: "LG Department"
  description: "Successfully onboarded 4 new LG team members with comprehensive folder structure and documentation"
  outcomes: "4 team members onboarded, folder structures created, documentation initialized"
  source_file: "Projects_Milestones_Tasks_Nov05-07_2025.md"
```

### Example 3: Action Item Extraction

**Source Text:**
```markdown
### Implement Resume/Document Parser
- **Description:** Create parser functionality to automatically extract data from resumes in multiple formats (PDF, DOCX, RTF, images) and auto-populate applicant fields in the job application system
- **Owner/Assignee:** Development team
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** AI integration capability, field mapping defined
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice
```

**Extracted Action Item:**
```yaml
ActionItem:
  id: "ACT-DEV-001"
  title: "Implement Resume/Document Parser"
  description: "Create parser functionality to automatically extract data from resumes in multiple formats (PDF, DOCX, RTF, images) and auto-populate applicant fields in the job application system"
  owner: "Development team"
  priority: "Critical"
  status: "Not Started"
  timeline:
    created_date: "2025-10-24"
    due_date: null
  dependencies: ["AI integration capability", "field mapping defined"]
  related_project: "LibDev Talents Microservice"
  source_file: "241025-organized.md"
```

### Example 4: Complete Daily Notes Extraction with Skills

**Source Text (from Daily Activity Report):**
```markdown
## Dev Department - November 07, 2025

### Completed Tasks ✅
- Create-API-Endpoint for Talents-Microservice using FastAPI in Dev-Context
  - Owner: Kizilova Olha
  - Priority: Critical
  - Duration: 3 hours
  - Result: POST /talents endpoint implemented with validation

- Design-Database-Schema for Finance-Service using PostgreSQL in Dev-Context
  - Owner: Klimenko Yaroslav
  - Priority: High
  - Duration: 2 hours
  - Result: Normalized schema with 8 tables created

- Implement-Authentication for Yellow-Card-Backend using JWT in Dev-Context
  - Owner: Kizilova Olha
  - Priority: Critical
  - Duration: 4 hours
  - Result: Secure JWT-based auth with refresh tokens

### In Progress ⏳
- Test-Integration for Talents-Microservice using Pytest in Dev-Context
  - Owner: Klimenko Yaroslav
  - Priority: High
  - Est. Completion: Nov 08
```

**Extracted Data:**

**Tasks:**
```yaml
Task_1:
  id: "TASK-DEV-147"
  name: "Create API Endpoint"
  taxonomy:
    action: "create"
    object: "api_endpoint"
    tool: "fastapi"
    department: "Dev"
    profession: "backend_developer"
  description: "Create API endpoint for Talents Microservice"
  owner: "Kizilova Olha"
  priority: "Critical"
  status: "Completed"
  timeline:
    completed_date: "2025-11-07"
    estimated_duration: "3 hours"
  results: "POST /talents endpoint implemented with validation"
  related_project: "Talents Microservice"
  source_file: "Daily_Activity_Report_Nov07_2025.md"

Task_2:
  id: "TASK-DEV-148"
  name: "Design Database Schema"
  taxonomy:
    action: "design"
    object: "database_schema"
    tool: "postgresql"
    department: "Dev"
    profession: "backend_developer"
  description: "Design database schema for Finance Service"
  owner: "Klimenko Yaroslav"
  priority: "High"
  status: "Completed"
  timeline:
    completed_date: "2025-11-07"
    estimated_duration: "2 hours"
  results: "Normalized schema with 8 tables created"
  related_project: "Finance Service"
  source_file: "Daily_Activity_Report_Nov07_2025.md"

Task_3:
  id: "TASK-DEV-149"
  name: "Implement Authentication"
  taxonomy:
    action: "implement"
    object: "authentication"
    tool: "jwt"
    department: "Dev"
    profession: "backend_developer"
  description: "Implement authentication for Yellow Card Backend"
  owner: "Kizilova Olha"
  priority: "Critical"
  status: "Completed"
  timeline:
    completed_date: "2025-11-07"
    estimated_duration: "4 hours"
  results: "Secure JWT-based auth with refresh tokens"
  related_project: "Yellow Card Backend"
  source_file: "Daily_Activity_Report_Nov07_2025.md"
```

**Skills Extracted:**
```json
{
  "skill_id": "SKILL-DEV-047",
  "skill_phrase": "Created REST API endpoints using FastAPI",
  "components": {
    "result": "Created",
    "object": "REST API endpoints",
    "tool": "FastAPI"
  },
  "profession": "Backend Developer",
  "proficiency_level": "Advanced",
  "frequency": 13,
  "first_demonstrated": "2025-10-15",
  "last_demonstrated": "2025-11-07",
  "related_tasks": ["TASK-DEV-023", "TASK-DEV-089", "TASK-DEV-147"],
  "department": "Dev",
  "employee": "Kizilova Olha",
  "tags": ["backend", "api", "python", "fastapi", "microservices"]
}

{
  "skill_id": "SKILL-DEV-089",
  "skill_phrase": "Designed database schemas using PostgreSQL",
  "components": {
    "result": "Designed",
    "object": "database schemas",
    "tool": "PostgreSQL"
  },
  "profession": "Backend Developer",
  "proficiency_level": "Advanced",
  "frequency": 8,
  "first_demonstrated": "2025-10-20",
  "last_demonstrated": "2025-11-07",
  "related_tasks": ["TASK-DEV-045", "TASK-DEV-102", "TASK-DEV-148"],
  "department": "Dev",
  "employee": "Klimenko Yaroslav",
  "tags": ["backend", "database", "postgresql", "schema-design", "sql"]
}

{
  "skill_id": "SKILL-DEV-102",
  "skill_phrase": "Implemented authentication using JWT",
  "components": {
    "result": "Implemented",
    "object": "authentication",
    "tool": "JWT"
  },
  "profession": "Backend Developer",
  "proficiency_level": "Advanced",
  "frequency": 5,
  "first_demonstrated": "2025-10-28",
  "last_demonstrated": "2025-11-07",
  "related_tasks": ["TASK-DEV-078", "TASK-DEV-125", "TASK-DEV-149"],
  "department": "Dev",
  "employee": "Kizilova Olha",
  "tags": ["backend", "security", "authentication", "jwt", "auth"]
}
```

**Object Types Identified:**
- `api_endpoint` → Type: `REST`, Automation: Very High (80%)
- `database_schema` → Type: `SQL`, Automation: High (65%)
- `authentication` → Type: `JWT-based`, Automation: High (70%)

### Example 5: Lead Generator Task with Object Types

**Source Text:**
```markdown
## LG Department - November 06, 2025

### Completed ✅
- Generate-Leads for Tech-Startups using LinkedIn-Sales-Navigator in LG-Context
  - Owner: Artemchuk Nikolay
  - Result: 45 qualified leads found
  - Lead Types: 30 cold, 10 new, 5 active

- Send-Cold-Outreach to Companies using LinkedIn in LG-Context
  - Owner: Artemchuk Nikolay
  - Result: 25 connection requests sent
  - Message Type: Connection request with personalized intro
```

**Extracted with Object Types:**
```yaml
Task:
  id: "TASK-LG-089"
  name: "Generate Leads"
  taxonomy:
    action: "generate"
    object: "leads"
    object_types: ["cold", "new", "active"]
    tool: "linkedin_sales_navigator"
    department: "LG"
    profession: "lead_generator"
  description: "Generate leads for tech startups"
  owner: "Artemchuk Nikolay"
  priority: "High"
  status: "Completed"
  metrics:
    total_count: 45
    breakdown:
      cold: 30
      new: 10
      active: 5
  automation_potential: "Very High (85%)"
  source_file: "Daily_Activity_Report_Nov06_2025.md"

Skill:
  skill_id: "SKILL-LG-023"
  skill_phrase: "Generated qualified leads using LinkedIn Sales Navigator"
  components:
    result: "Generated"
    object: "qualified leads"
    tool: "LinkedIn Sales Navigator"
  profession: "Lead Generator"
  proficiency_level: "Expert"
  frequency: 25
  employee: "Artemchuk Nikolay"
```

### Example 6: Designer Task with Multiple Object Types

**Source Text:**
```markdown
## Design Department - November 05, 2025

### Completed ✅
- Design-Mockup for E-commerce-Website using Figma in Design-Context
  - Owner: Safonova Eleonora
  - Mockup Types: Homepage, Product Page, Checkout Flow
  - Components: Navigation bar, Product cards, Call-to-action buttons
  - Result: 12 screens with responsive layouts
```

**Extracted with Object Type Details:**
```yaml
Task:
  id: "TASK-DES-056"
  name: "Design Mockup"
  taxonomy:
    action: "design"
    object: "mockup"
    object_types: ["website", "e-commerce"]
    tool: "figma"
    department: "Design"
    profession: "ui_designer"
  description: "Design mockup for e-commerce website"
  owner: "Safonova Eleonora"
  priority: "High"
  status: "Completed"
  deliverables:
    screens: 12
    mockup_types: ["homepage", "product_page", "checkout_flow"]
    components_created: ["navigation_bar", "product_cards", "cta_buttons"]
    features: ["responsive_layout"]
  automation_potential: "Medium (45%)"
  source_file: "Daily_Activity_Report_Nov05_2025.md"

Skill:
  skill_id: "SKILL-DES-034"
  skill_phrase: "Designed website mockups using Figma"
  components:
    result: "Designed"
    object: "website mockups"
    tool: "Figma"
  profession: "UI Designer"
  proficiency_level: "Advanced"
  frequency: 18
  employee: "Safonova Eleonora"
  tags: ["ui-design", "figma", "mockups", "website", "e-commerce"]
```

---

## Quality Checklist

### Pre-Extraction Checklist
- [ ] All source files identified and listed
- [ ] Taxonomy libraries loaded and accessible
- [ ] Extraction patterns defined
- [ ] ID generation scheme established

### During Extraction Checklist
- [ ] Each task has unique ID
- [ ] Taxonomy components validated against libraries
- [ ] All required fields extracted
- [ ] Source references included
- [ ] Cross-references maintained

### Post-Extraction Checklist
- [ ] All templates validated
- [ ] No duplicate IDs
- [ ] All cross-references valid
- [ ] Output files formatted correctly
- [ ] Indexes generated
- [ ] Source tracking complete

### Final Review Checklist
- [ ] All files generated in correct location
- [ ] File structure matches specification
- [ ] Content is complete and accurate
- [ ] Markdown formatting is correct
- [ ] Ready for use in taxonomy system

---

## Troubleshooting

### Common Issues

#### Issue: Ambiguous Taxonomy Components
**Problem:** Cannot determine action/object/tool from task name

**Solution:**
1. Check task description for additional context
2. Look for "using [Tool]" or "in [Context]" patterns
3. Check similar tasks in same document
4. Use best guess and flag for manual review

#### Issue: Missing Department Information
**Problem:** Cannot determine department from task

**Solution:**
1. Check file name for department hints
2. Check owner name against employee directory
3. Check project context
4. Use "Unknown" and flag for manual assignment

#### Issue: Duplicate Tasks
**Problem:** Same task appears in multiple files

**Solution:**
1. Compare task details
2. Keep most complete version
3. Merge source references
4. Update cross-references

#### Issue: Invalid Taxonomy References
**Problem:** Action/Object/Tool not in libraries

**Solution:**
1. Flag for library update
2. Use closest match from library
3. Document new entry needed
4. Continue extraction with placeholder

---

## Next Steps After Extraction

1. **Review Generated Templates**
   - Manual review of extracted templates
   - Verify accuracy and completeness
   - Fix any extraction errors

2. **Update Libraries**
   - Add new actions to actions.json
   - Add new objects to objects.json
   - Add new tools to tools.json

3. **Create Template Index**
   - Generate master index file
   - Link all templates together
   - Create searchable reference

4. **Integration**
   - Import templates into taxonomy system
   - Link to CRM entities
   - Enable template usage in workflows

5. **Documentation**
   - Update README with new templates
   - Create usage guides
   - Train team on new templates

---

## Version History

**Version 2.3** (November 10, 2025)
- **Terminology Enhancement:** Improved Object Library Definitions section clarity
  - Changed "Category:" to "Department:" for all object sections
    - Document Objects: HR, Legal, Management
    - Communication Objects: All Departments
    - Development Objects: Dev
    - Design Objects: Design
    - Marketing Objects: Marketers (expanded)
    - Management Objects: Management, All Departments
  - Changed "Common Actions:" to "Workflow Actions:" throughout all sections
  - Updated intro text: "organized by department for better classification and workflow understanding"
- **Marketers Department Added** (Complete integration across all sections)
  - Added Marketers Department to Department-Specific Extraction Rules
    - Common Objects: Ad Campaigns, Posts, Keywords, Landing Pages, Content, SEO Reports, Media Buys, Social Media Strategies, Analytics Dashboards
    - Common Tools: Google Ads, Meta Ads Manager, Google Analytics, SEMrush, Ahrefs, Hootsuite, Buffer, WordPress, HubSpot
    - AI Tools: Claude (content creation), Gemini (market research), Perplexity (competitor analysis), ChatGPT (copywriting)
    - Priority Keywords: optimizing, targeting, analyzing, publishing, bidding, ranking, converting, retargeting, A/B testing
    - Success Metrics: ROI, CPC, CTR, conversion rate, organic traffic, keyword rankings, engagement rate, ROAS
    - **4 Professions Defined:**
      - SMM (Social Media Manager): Manages social media presence, content calendars, audience engagement
      - PPC Specialist: Manages paid advertising, optimizes bids, A/B tests ad creatives
      - SEO Specialist: Optimizes for search engines, keyword research, backlinks, rankings
      - Media Buyer: Purchases advertising space, negotiates rates, manages budgets
  - Enhanced Marketers Objects in Object Library Definitions
    - Added 4 new marketers-specific objects: Ad Campaign, Social Media Strategy, SEO Report, Media Buy
    - Enhanced Workflow Actions: Create, Publish, Analyze, Optimize, Schedule, Target, Monitor, A/B Test
  - Added Marketers Object Types by Profession section (45+ lines)
    - Ad Campaigns: 6 types (PPC, display, video, retargeting, search, social)
    - Content: 6 types (blog post, email copy, ad copy, social copy, landing page copy, video script)
    - Keywords: 5 types (target, long-tail, competitor, branded, local)
    - Analytics: 5 types (traffic report, conversion report, SEO report, ad performance, social metrics)
    - SEO Objects: 5 types (backlinks, meta tags, sitemap, schema markup, robots.txt)
    - Social Media: 5 types (post, story, reel, carousel, engagement)
  - Added Marketers professions to Skills Collection section
    - 4 new professions in Step 4 profession mapping table with typical skills and tools
    - Added to Skills Quick Reference by Profession with Top 5 skills each:
      - SMM: High automation (65-75%)
      - PPC Specialist: Very High automation (75-85%)
      - SEO Specialist: High automation (60-70%)
      - Media Buyer: High automation (65-75%)
- **Documentation Updates:**
  - Total additions: ~80+ lines of new marketers-specific content
  - Enhanced 4 professions count (8 → 12 professions now covered)
  - Improved terminology consistency across all 6 object sections
  - Department name: Marketing → Marketers (for consistency with other department names)

**Version 2.2** (November 10, 2025)
- **Major Enhancement:** Integrated AI_CONTEXT_PROMPT.md insights for skills collection and object type patterns
  - Added Skills Collection & Extraction section (170+ lines)
    - Skills formula: RESULT + OBJECT + "via/using/in" + TOOL
    - 4-step extraction process (Identify → Transform → Construct → Categorize)
    - Action-to-Result transformation table (10 common verbs)
    - Profession-based skills categorization (8 professions)
    - Skill storage structure with JSON schema
    - Skill aggregation rules (frequency tracking, proficiency assessment, consolidation)
    - Proficiency level assessment algorithm (Beginner/Intermediate/Advanced/Expert)
    - Skills Quick Reference by Profession (Top 5 skills for each profession)
    - Daily Notes Skills Extraction workflow (6-step process)
    - Integration with TALENTS entity for employee skills tracking
  - Added Object Type Patterns by Profession section (175+ lines)
    - HR/Recruiter object types: Candidates (7 types), Communications (4 types), Contracts (3 types), Interviews (3 types)
    - Lead Generator object types: Accounts (5 types), Companies (5 types), Leads (5 types), Messages (4 types)
    - Developer object types: APIs (6 types), Databases (4 types), Modules (4 types), Code (4 types)
    - Designer object types: Mockups (4 types), Logos (5 types), Illustrations (5 types), UI Components (5 types)
    - Video Editor object types: Videos (5 types), Assets (5 types)
    - AI Engineer object types: Models (4 types), Prompts (3 types), Training Data (4 types)
  - Added Automation Potential by Object Type section (30+ lines)
    - 4-level automation ranking (Very High >80%, High 60-80%, Medium 40-60%, Low <40%)
    - Prioritization guidelines for library population based on automation potential
    - Object type examples by automation level
    - Extraction guidelines for capturing object type modifiers from daily notes
  - Enhanced Examples section
    - Example 4: Complete Daily Notes Extraction with Skills (165+ lines)
      - Full Dev Department daily activity report extraction
      - 3 completed tasks with complete task structures
      - 3 skills extracted with full JSON schemas including frequency and proficiency
      - Object types identified with automation potential ratings
    - Example 5: Lead Generator Task with Object Types (55+ lines)
      - Lead generation task with object type breakdowns
      - Metrics and automation potential included
      - Skills extraction for lead generation
    - Example 6: Designer Task with Multiple Object Types (50+ lines)
      - Design mockup task with multiple deliverables
      - Component-level tracking
      - Skills extraction for UI design work
- **Tool Updates:**
  - Fixed GitHub references - kept GitHub with enhanced details (repositories, pull requests, issues, actions, project boards)
  - Moved GitHub to dedicated "Version Control" category in Dev Department
- **Documentation:**
  - Updated Table of Contents with 4 new sections (Skills Collection, Object Type Patterns, Automation Potential, Enhanced Examples)
  - Total additions: ~620+ lines of new content
  - Learning applied from AI_CONTEXT_PROMPT.md (200+ actions, 150+ objects, 100+ tools, profession-specific patterns)
  - Enhanced integration between taxonomy system (ACTION + OBJECT + TOOL) and skills collection (RESULT + OBJECT + via/using + TOOL)

**Version 2.1** (November 10, 2025)
- **Major Enhancement:** Integrated Niko AI Prompt methodologies for daily notes extraction
  - Added comprehensive Daily Notes Extraction Guidelines (320+ lines)
    - 4-step daily report workflow (Read logs → Process notes → Generate extraction → Populate libraries)
    - Department-specific section emphasis for 7 departments
    - Extraction patterns from implicit tasks and context
    - Participant matching with 5 strategies and confidence levels (High/Medium/Low 0.0-1.0)
    - Auto-population of metadata when matches found
    - Systematic library population from daily activities
  - Added Prioritization System (190+ lines)
    - 4-level priority framework (Critical/High/Medium/Low)
    - Priority inference rules with 4 rule types (Urgency, Impact, Deadline, Dependencies)
    - Status tracking system (not_started → in_progress → blocked → completed)
    - Complexity assessment (Beginner/Intermediate/Advanced/Expert)
    - RACI Matrix integration (Responsible/Accountable/Consulted/Informed)
    - Confidence scoring for priority assignments
    - Priority matrix visualization
  - Added Top-10 Priority Management System (300+ lines)
    - Automatic Top-10 generation algorithm with 5-step process
    - Priority scoring formula: (Priority×40%) + (Deadline×30%) + (Impact×20%) + (Dependencies×10%)
    - Access patterns for "at reach" items with dashboard layouts
    - Department KPI integration with 7 department-specific KPI tables
      - HR: Time-to-hire, candidates sourced, interview-to-offer ratio
      - LG: Leads/week, response rate, meetings booked, automation time saved
      - Design: Projects/week, revision rounds, client satisfaction
      - Dev: Deployment frequency, bug resolution time, code quality
      - AI: Automation coverage, workflow efficiency, time saved
      - Sales: Pipeline value, conversion rate, deal cycle length
      - Video: Videos/week, production time, engagement rate
    - Top-10 refresh strategy with daily updates and alert triggers
    - Visualization recommendations (priority matrix, burndown charts, status distribution)
    - Department-specific Top-10 views
    - Integration with Task Templates
  - Enhanced Task Template Structure
    - Added "priority" section with inference confidence and priority scoring
    - Added "accountability" section with full RACI matrix
    - Added "top_10" section for ranking metadata
    - Enhanced "source_tracking" with confidence scores and inference details
- **Tool Updates:**
  - Removed GitHub Copilot references (deprecated tool)
  - Retained focus on Cursor (primary IDE), Claude, Gemini, Perplexity
- **Documentation:**
  - Updated Table of Contents with 3 new major sections
  - Total additions: ~810+ lines of new content
  - Learning applied from Niko AI Prompts system (21-section framework, employee directory matching, project directory integration)

**Version 2.0** (November 10, 2025)
- Added department-specific extraction rules with AI tool mappings
  - HR: VS Code, Claude, Gemini, Perplexity, Cursor
  - LG: Gemini (primary), Perplexity, Claude, n8n
  - Design: Figma, Midjourney, Leonardo.ai, Claude
  - Dev: Cursor (primary IDE), Claude
  - AI: Claude, Gemini, Perplexity, ChatGPT, Cursor, n8n
  - Sales: Claude, Gemini, Perplexity, VS Code
  - Video: Premiere Pro, After Effects, ElevenLabs, Claude
- Added comprehensive object library definitions
  - Documents: Job Posting, Proposal, Report, Contract, Invoice
  - Communications: Email, Message, Call, Meeting, Notification
  - Development: API, Database, Server, Endpoint, Schema, Microservice
  - Design: Banner, Logo, Icon, Mockup, Wireframe, Prototype
  - Marketing: Ad, Post, Campaign, Keyword, Content
  - Management: Task, Project, Milestone, Workflow, Dashboard
- Added compound entities explanation
  - Explained LIBRARIES as flagship compound entity (5 sub-entities)
  - Clarified difference between simple and compound entities
  - Detailed interconnected relationships and extraction implications
- Added complete template structures with JSON schemas
  - Task Template Structure (comprehensive)
  - Step Template Structure
  - Project Template Structure
  - Workflow Template Structure
  - Template usage guidelines and relationships
- Removed outdated tool references (Zoom, Make.com)
- Updated library file paths to Framework/Entities/LIBRARIES/*

**Version 1.0** (November 25, 2025)
- Initial extraction prompt document created
- Defined extraction targets and processes
- Established validation rules
- Created output specifications

---

**Last Updated:** November 10, 2025
**Maintained By:** Taxonomy Extraction Team
**Inspired By:** Niko AI Prompt System (v3.0) - 21-section framework, participant matching, priority management
**Questions?** Refer to taxonomy guides or contact Framework Architecture Team

