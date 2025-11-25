# Video Transcription Custom Instructions - Taxonomy Analysis Focus

---

## 🔴 CRITICAL OUTPUT REQUIREMENT 🔴

**MUST OUTPUT COMPLETE STRUCTURED MARKDOWN DOCUMENT**

❌ **DO NOT** output JSON, plain text, or any other format
✅ **REQUIRED FORMAT:** Markdown (.md) with sections below
✅ **FILE EXTENSION:** .md (not .json, .txt)

---

**Purpose**: Transcribe videos with structured extraction of workflows, Task Templates, Step Templates, project structures, action verbs, skills, and responsibilities vocabulary for direct taxonomy integration.

**Version**: 3.2 - Phase 4-8 Integration (Task/Step/Project Templates + Skills Linkage)
**Date**: 2025-11-13
**Major Update**: Enables direct extraction of taxonomy-ready Task Templates, Step Templates, Project Templates, and skills with task linkage

---

## 🎯 What's New in v3.2

This version adds **FIVE MAJOR SECTIONS** for direct taxonomy extraction based on Phases 4-8 learnings:

**NEW SECTIONS:**
- **4B. Task Templates Extraction** - Direct ACTION_OBJECT_CONTEXT format
- **4C. Step Templates Extraction** - Reusable steps with parent task linkage
- **4D. Project Templates Extraction** - Phase → Milestone → Task → Step hierarchy
- **7B. Enhanced Skills Extraction** - "action via tool" format with task linkage
- **Taxonomy Naming Conventions** - Standardized naming rules

**KEY BENEFIT:** Reduces post-processing time from 2-4 hours to 10-20 minutes per video (90-95% time savings)

---

## TAXONOMY NAMING CONVENTIONS

**CRITICAL**: All extracted elements MUST follow these naming conventions for taxonomy integration.

### Task Template Names:
- **Format**: `ACTION_OBJECT_CONTEXT`
- **Rules**:
  - ALL_CAPS with underscores
  - ACTION: One verb from categories A-G (section 5)
  - OBJECT: Plural noun from Objects section (section 9)
  - CONTEXT: Distinguishing details (method, tool, source, purpose)
- **Examples**:
  - `ENRICH_LEADS_MULTI-SOURCE` (Action: Enrich, Object: Leads, Context: Multi-source)
  - `SCRAPE_COMPANIES_FROM_GOOGLE` (Action: Scrape, Object: Companies, Context: From Google)
  - `GENERATE_CONNECTOR_VIA_MCP-BUILDER` (Action: Generate, Object: Connector, Context: Via MCP-Builder)
  - `AUTOMATE_EMAILS_MORNING-DRAFTS` (Action: Automate, Object: Emails, Context: Morning-Drafts)

### Step Template Names:
- **Format**: `ACTION_OBJECT_SPECIFIC_DETAIL`
- **Rules**:
  - ALL_CAPS with underscores
  - Include tool/method in name for clarity
  - More specific than task names
- **Examples**:
  - `SCRAPE_COMPANY_DATA_FROM_AIRSCALE`
  - `EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW`
  - `UPLOAD_CSV_TO_ANYMAILFINDER`
  - `CONFIGURE_OAUTH_IN_GOOGLE_CLOUD`

### Skill Phrases:
- **Format**: `"[past tense action] [object] via [tool]"`
- **Rules**:
  - Lowercase, natural language
  - ALWAYS include tool name
  - Use past participle form of action verb
- **Examples**:
  - `"enriched emails via Anymailfinder"`
  - `"scraped lead lists via Apify"`
  - `"generated MCP connectors via Claude"`
  - `"deployed connectors via Cursor"`

### Project Template Names:
- **Format**: `Descriptive_Name_Campaign/System/Initiative`
- **Rules**: Title_Case with underscores
- **Examples**:
  - `Lead_Generation_Campaign`
  - `MCP_Automation_Stack_Setup`
  - `Enterprise_ABM_Campaign`

---

## Core Transcription Requirements

**Output complete structured markdown document** with the following format:

### Technical Requirements
- **Format:** Markdown (.md) only - NOT JSON, NOT plain text
- **Encoding:** UTF-8
- **Special Characters:** If $ or currency symbols cause corruption, write out full words ("five point six million")
- **Quality Check:** If text appears character-by-character (e.g., "h e l l o"), re-process that section

Transcribe the video content with the following structure in markdown format:

### 1. Metadata Section
- **Video Title**: [Extract exact title]
- **Channel/Creator**: [If available]
- **Video URL**: [Full URL if provided]
- **Duration**: [Video length if visible]
- **Publication Date**: [If available]

### 2. Description Section
- **Description**: [Full video description as provided]
- **Key Topics**: [List main topics covered]
- **Links Referenced**:
  - [Link 1 with description]
  - [Link 2 with description]

### 3. Word-for-Word Transcription

Transcribe exactly as spoken, including:
- **Timestamps**: Mark every 30-60 seconds or at topic changes
- **Speaker Labels**: If multiple speakers
- **Verbal Fillers**: Include "um", "uh", "you know" for accuracy
- **On-screen Text**: Capture in [TEXT: content]
- **Visual Descriptions**: Note in [VISUAL: description]

---

## TAXONOMY EXTRACTION REQUIREMENTS (Critical)

### 4. Workflows Identification

**Identify and extract all workflows/processes mentioned in the video:**

Format each workflow as:
```
WORKFLOW: [Workflow Name]
DEPARTMENT: [Primary department that performs this workflow]
CROSS_DEPT_PATTERN: [If cross-department, describe handoff pattern - OPTIONAL]
OBJECTIVE: [What the workflow achieves]
STEPS:
  1. [Action verb] + [object/deliverable]
  2. [Action verb] + [object/deliverable]
  3. [Continue...]
DURATION: [Time estimate if mentioned]
COMPLEXITY: [Low/Medium/High/Very High if mentioned]
TOOLS USED: [List all tools mentioned]
INPUT: [What you start with]
OUTPUT: [What you end with]
```

**Examples:**
```
WORKFLOW: Multi-Source Lead Enrichment Pipeline
DEPARTMENT: Sales / AI
OBJECTIVE: Generate enriched lead lists from multiple data sources with email validation
STEPS:
  1. Scrapes company data from search platform (location, size, keywords)
  2. Extracts company domains using automated workflow
  3. Exports to CSV format
  4. Imports CSV to email enrichment service
  5. Enriches with nominative email patterns (firstname@domain.com variations)
  6. Validates email deliverability
  7. Downloads enriched list with verified contacts
DURATION: 10-15 minutes for 40 records, scalable to thousands
COMPLEXITY: Medium
TOOLS USED: Airscale, Anymailfinder, LinkedIn Sales Navigator, Google Sheets
INPUT: Search criteria (industry, geography, company size, job titles)
OUTPUT: CSV with company data + verified decision-maker emails, names, LinkedIn URLs, roles
```

```
WORKFLOW: Stacked Connector Post-Meeting Automation
DEPARTMENT: Operations (Cross-department: Sales, Customer Success)
CROSS_DEPT_PATTERN:
  - Operations drops meeting transcript (trigger)
  - Claude extracts insights and attendees (Operations)
  - Gmail drafts follow-up email (Sales/CS collaboration)
  - CRM updates meeting notes and wins (Sales owns CRM)
OBJECTIVE: Automate all post-meeting follow-up tasks using stacked MCP connectors
STEPS:
  1. Drops meeting transcript into Claude Desktop
  2. Extracts action items, decisions, client wins, attendees
  3. Drafts personalized follow-up email
  4. Updates CRM with meeting notes and wins
  5. Sets calendar reminder for next action
DURATION: 1-4 minutes (automated), saves 15+ hours/week
COMPLEXITY: Very High
TOOLS USED: Claude Desktop, Gmail MCP, Calendar MCP, CRM connector
INPUT: Meeting transcript
OUTPUT: Follow-up email drafted, CRM updated, reminders set
```

---

### 4B. Task Templates Extraction ⭐ NEW IN V3.2

**For each workflow identified, extract reusable Task Templates:**

**PURPOSE:** Task Templates are reusable across projects. One Task Template can be used in multiple workflows and projects. They form the building blocks of your taxonomy.

**Format:**
```
TASK: [ACTION]_[OBJECT]_[CONTEXT]
TASK_ID: [TBD - will be assigned during taxonomy integration]
DEPARTMENT: [Primary department that performs this task]
ACTION: [Single verb from categories A-G in section 5]
OBJECT: [Deliverable/output - use from section 9]
CONTEXT: [Distinguishing details - method, source, tool, purpose]
COMPLEXITY: [Low/Medium/High/Very High]
TIME_ESTIMATE: [Typical duration from workflow data]
PARENT_PROJECT: [If part of larger project, name it - OPTIONAL]
STEPS_USED: [Reference Step Templates from section 4C]
SKILLS_REQUIRED: [Reference skills from section 7B]
TOOLS: [Primary tools used in this task]
INPUT: [What you start with]
OUTPUT: [What task produces]
SUCCESS_CRITERIA: [How to know task completed successfully]
REUSABLE_IN: [Other contexts where this Task Template could apply]
```

**Example 1:**
```
TASK: ENRICH_LEADS_MULTI-SOURCE
TASK_ID: TBD
DEPARTMENT: Sales / AI (Lead Generation)
ACTION: Enrich
OBJECT: Leads
CONTEXT: Multi-source with email validation
COMPLEXITY: Medium
TIME_ESTIMATE: 10-15 minutes for 40 records
PARENT_PROJECT: Lead_Generation_Campaign
STEPS_USED: [
  SCRAPE_COMPANY_DATA_FROM_AIRSCALE,
  EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW,
  EXPORT_DATA_TO_CSV,
  UPLOAD_CSV_TO_ANYMAILFINDER,
  EXECUTE_DECISION-MAKER_SEARCH,
  VALIDATE_EMAIL_DELIVERABILITY,
  DOWNLOAD_ENRICHED_RESULTS
]
SKILLS_REQUIRED: [
  "enriched emails via Anymailfinder",
  "scraped lead lists via Apify"
]
TOOLS: [Airscale, Anymailfinder, Google Sheets]
INPUT: Search criteria (industry, location, company size)
OUTPUT: CSV with verified decision-maker emails
SUCCESS_CRITERIA: 80%+ email enrichment rate, emails verified
REUSABLE_IN: [
  Enterprise prospecting campaigns,
  Local business outreach,
  Partnership development,
  Customer win-back campaigns,
  Event attendee outreach
]
```

**Example 2:**
```
TASK: GENERATE_CONNECTOR_VIA_MCP-BUILDER
TASK_ID: TBD
DEPARTMENT: Development / AI
ACTION: Generate
OBJECT: MCP Connector
CONTEXT: Via MCP-Builder skill
COMPLEXITY: Very High (automated by skill to 30-60 sec)
TIME_ESTIMATE: 30-60 seconds generation time
PARENT_PROJECT: MCP_Automation_Stack_Setup
STEPS_USED: [
  ENABLE_CLAUDE_SKILLS,
  WRITE_CONNECTOR_REQUIREMENTS,
  EXECUTE_MCP-BUILDER_GENERATION,
  REVIEW_GENERATED_CODE,
  SAVE_CONNECTOR_FILES
]
SKILLS_REQUIRED: [
  "generated MCP connectors via Claude",
  "configured OAuth for Google APIs"
]
TOOLS: [Claude Desktop, MCP Builder Skill]
INPUT: 2-sentence connector requirements prompt
OUTPUT: Complete MCP server code with OAuth, API handlers, error handling
SUCCESS_CRITERIA: Code generated successfully, 95%+ success rate
REUSABLE_IN: [
  Gmail connector generation,
  Calendar connector generation,
  CRM connector generation,
  Any Google API MCP connector,
  Custom app connectors
]
```

**Example 3:**
```
TASK: AUTOMATE_EMAILS_MORNING-DRAFTS
TASK_ID: TBD
DEPARTMENT: Operations
ACTION: Automate
OBJECT: Emails
CONTEXT: Morning draft generation
COMPLEXITY: Medium
TIME_ESTIMATE: 15-20 minutes setup, then automated daily
PARENT_PROJECT: MCP_Automation_Stack_Setup
STEPS_USED: [
  CONFIGURE_GMAIL_MCP_CONNECTOR,
  DEFINE_AUTOMATION_RULES,
  TEST_DRAFT_GENERATION,
  SCHEDULE_MORNING_WORKFLOW
]
SKILLS_REQUIRED: [
  "automated emails via Gmail MCP",
  "deployed MCP connectors via Cursor"
]
TOOLS: [Claude Desktop, Gmail MCP Connector]
INPUT: Email response guidelines
OUTPUT: Automated morning email drafts (5-10 hrs/week saved)
SUCCESS_CRITERIA: 90%+ draft success rate, 5+ hours/week saved
REUSABLE_IN: [
  Executive assistant workflows,
  Sales team daily routines,
  Customer success operations,
  Newsletter management
]
```

**Extraction Guidelines:**
- Extract ONE Task Template per distinct workflow or major workflow phase
- Use ACTION_OBJECT_CONTEXT naming consistently
- If workflow has 5+ steps, consider if it should be multiple tasks
- Link to Step Templates (section 4C) and skills (section 7B)
- Always identify reusability contexts (where else could this be used?)

---

### 4C. Step Templates Extraction ⭐ NEW IN V3.2

**For each step within workflows/tasks, create standalone Step Templates:**

**PURPOSE:** Steps are reusable across multiple tasks. The same step (like "SCRAPE_COMPANY_DATA_FROM_AIRSCALE") might be used in 5 different Task Templates. Extracting them enables mixing and matching for new workflows.

**Format:**
```
STEP: [ACTION]_[OBJECT]_[SPECIFIC_DETAIL]
STEP_ID: [TBD - will be assigned during taxonomy integration]
ACTION: [Verb from A-G categories]
OBJECT: [What this step acts upon]
TOOL: [Primary tool used for this step]
PARENT_TASKS: [All tasks that use this step - reference section 4B]
COMPLEXITY: [Low/Medium/High]
TIME_ESTIMATE: [Time for this specific step]
INPUT: [What this step receives]
OUTPUT: [What this step produces]
PREREQUISITES: [What must be completed/configured before this step]
INSTRUCTIONS: [Brief how-to for this step - 3-8 bullet points]
REUSABLE_IN: [Other tasks/workflows where this step could be used]
```

**Example 1:**
```
STEP: SCRAPE_COMPANY_DATA_FROM_AIRSCALE
STEP_ID: TBD
ACTION: Scrape
OBJECT: Company Data
TOOL: Airscale
PARENT_TASKS: [
  ENRICH_LEADS_MULTI-SOURCE,
  GENERATE_ENTERPRISE_EMAIL_LISTS,
  BUILD_TAM_ANALYSIS
]
COMPLEXITY: Low
TIME_ESTIMATE: 2-3 minutes
INPUT: Search criteria (location, company size, keywords)
OUTPUT: Company list table with names, LinkedIn URLs
PREREQUISITES: [Airscale account configured, Search criteria defined]
INSTRUCTIONS:
  1. Navigate to Airscale platform
  2. Set location filter (e.g., "California")
  3. Set company size filter (e.g., "11-50 employees")
  4. Enter keywords in search (e.g., "AI agency")
  5. Click "Preview Companies" to verify results
  6. Click "Load all companies to table"
REUSABLE_IN: [
  Any task requiring company list generation,
  Market research projects,
  Competitive intelligence gathering,
  TAM (Total Addressable Market) analysis
]
```

**Example 2:**
```
STEP: UPLOAD_CSV_TO_ANYMAILFINDER
STEP_ID: TBD
ACTION: Upload
OBJECT: CSV File
TOOL: Anymailfinder
PARENT_TASKS: [
  ENRICH_LEADS_MULTI-SOURCE,
  ENRICH_LINKEDIN_EXPORT,
  VALIDATE_ENTERPRISE_EMAILS
]
COMPLEXITY: Low
TIME_ESTIMATE: 1-2 minutes
INPUT: CSV file with company domains
OUTPUT: Uploaded CSV ready for enrichment
PREREQUISITES: [
  CSV exported with correct columns (domain, company name),
  Anymailfinder account with credits
]
INSTRUCTIONS:
  1. Log into Anymailfinder
  2. Click "Bulk Enrichment"
  3. Click "Upload CSV"
  4. Select file from computer
  5. Map columns: "Company Domain" → Domain field
  6. Verify preview shows correct data
REUSABLE_IN: [
  Any email enrichment task,
  Bulk email verification,
  Decision-maker email discovery
]
```

**Example 3:**
```
STEP: CONFIGURE_OAUTH_IN_GOOGLE_CLOUD
STEP_ID: TBD
ACTION: Configure
OBJECT: OAuth Credentials
TOOL: Google Cloud Console
PARENT_TASKS: [
  GENERATE_CONNECTOR_VIA_MCP-BUILDER,
  DEPLOY_GMAIL_MCP_CONNECTOR,
  SETUP_CALENDAR_AUTOMATION
]
COMPLEXITY: Medium
TIME_ESTIMATE: 10-15 minutes (one-time setup)
INPUT: Google Cloud project name, API requirements
OUTPUT: OAuth 2.0 client ID and client secret
PREREQUISITES: [
  Google Cloud Console account,
  API enabled (Gmail API or Calendar API)
]
INSTRUCTIONS:
  1. Navigate to Google Cloud Console
  2. Create new project or select existing
  3. Enable required API (Gmail or Calendar)
  4. Go to "Credentials" section
  5. Click "Create Credentials" → "OAuth 2.0 Client ID"
  6. Configure consent screen (application name, scopes)
  7. Select application type: "Desktop app"
  8. Copy Client ID and Client Secret
REUSABLE_IN: [
  Any Google API MCP connector setup,
  Gmail automation,
  Calendar automation,
  Drive automation
]
```

**Extraction Guidelines:**
- Extract EVERY distinct step from workflows (typically 4-10 steps per workflow)
- Each step should be atomic (one clear action)
- Include tool name in step name for clarity
- Always document prerequisites (what's needed before this step)
- Link to parent tasks (which tasks use this step)
- Identify cross-task reusability

---

### 4D. Project Templates Extraction ⭐ NEW IN V3.2

**If video describes a multi-phase project or campaign, extract hierarchical structure:**

**PURPOSE:** Projects are collections of related tasks organized into phases and milestones. One Project Template can be instantiated multiple times (e.g., "Lead_Generation_Campaign" project could be run monthly). This structure enables project-level planning and reuse.

**WHEN TO EXTRACT:** If video shows:
- Multi-phase workflow spanning days/weeks
- Clear sequential phases with milestones
- Cross-department collaboration
- Complex campaigns with multiple outcomes

**Format:**
```
PROJECT: [PROJECT_NAME]
PROJECT_ID: [TBD - will be assigned during taxonomy integration]
DEPARTMENT: [Primary department, note if cross-department]
DESCRIPTION: [What this project achieves end-to-end]
DURATION: [Total project timeline if mentioned]
COMPLEXITY: [Low/Medium/High/Very High]
COST_ESTIMATE: [If mentioned]
ROI_ESTIMATE: [If mentioned - time savings, revenue impact, cost savings]

PHASE 1: [Phase Name]
  DESCRIPTION: [What this phase accomplishes]
  DURATION: [Phase timeline]
  OUTPUT: [What's delivered at phase end]

  MILESTONE: [Milestone Name]
    DESCRIPTION: [What this milestone achieves]
    DELIVERABLE: [Specific output]
    TASKS:
      - TASK: [Task name from section 4B] (TIME: [duration])
        STEPS: [Step names from section 4C]
      - TASK: [Next task]
        STEPS: [Steps]

  MILESTONE: [Next milestone]
    TASKS: ...

PHASE 2: [Next Phase]
  DESCRIPTION: ...
  MILESTONE: ...
    TASKS: ...

[Continue for all phases...]

CROSS_DEPARTMENT_COLLABORATION:
  - [Department A] does [phase/task] then hands off to [Department B] via [method]
  - [Example: Sales generates leads, Operations configures automation, Sales runs campaigns]
```

**Example:**
```
PROJECT: Lead_Generation_Campaign
PROJECT_ID: TBD
DEPARTMENT: Sales / AI (Cross-department with Operations for automation)
DESCRIPTION: Generate and enrich qualified lead lists for outbound sales campaigns with automated follow-up
DURATION: 1-2 weeks for setup, ongoing operation
COMPLEXITY: High
COST_ESTIMATE: $5-50 (email enrichment costs)
ROI_ESTIMATE: 15-20+ hours/week saved after automation setup

PHASE 1: Data Sourcing
  DESCRIPTION: Identify and collect target company/contact information
  DURATION: 1-3 days
  OUTPUT: 2,000+ raw leads with company data

  MILESTONE: Identify Target Companies
    DESCRIPTION: Build list of companies matching ICP criteria
    DELIVERABLE: Company list with 2,000+ entries
    TASKS:
      - TASK: SCRAPE_COMPANIES_FROM_GOOGLE (TIME: 20-30 min)
        STEPS: [
          SCRAPE_COMPANY_DATA_FROM_AIRSCALE,
          EXTRACT_DOMAINS_VIA_AIRSCALE_WORKFLOW,
          EXPORT_DATA_TO_CSV
        ]

PHASE 2: Email Enrichment
  DESCRIPTION: Find and validate email addresses for all leads
  DURATION: 1-2 days
  OUTPUT: Lead list with 80%+ emails verified

  MILESTONE: Nominative Enrichment
    DESCRIPTION: Generate emails using name + domain patterns
    DELIVERABLE: CSV with decision-maker emails
    TASKS:
      - TASK: ENRICH_LEADS_MULTI-SOURCE (TIME: 10-15 min per batch)
        STEPS: [
          UPLOAD_CSV_TO_ANYMAILFINDER,
          EXECUTE_DECISION-MAKER_SEARCH,
          VALIDATE_EMAIL_DELIVERABILITY,
          DOWNLOAD_ENRICHED_RESULTS
        ]

PHASE 3: Automation Setup
  DESCRIPTION: Configure MCP automation for outreach and follow-up
  DURATION: 3-4 hours (one-time setup)
  OUTPUT: Automated email and meeting follow-up system

  MILESTONE: Email Automation Operational
    DESCRIPTION: Morning email drafts automated
    DELIVERABLE: 5-10 hours/week saved
    TASKS:
      - TASK: GENERATE_CONNECTOR_VIA_MCP-BUILDER (TIME: 60 sec)
        STEPS: [
          ENABLE_CLAUDE_SKILLS,
          WRITE_CONNECTOR_REQUIREMENTS,
          EXECUTE_MCP-BUILDER_GENERATION
        ]
      - TASK: DEPLOY_GMAIL_MCP_CONNECTOR (TIME: 5 min)
        STEPS: [
          CONFIGURE_OAUTH_IN_GOOGLE_CLOUD,
          INSTALL_CONNECTOR_LOCALLY,
          TEST_CONNECTION
        ]
      - TASK: AUTOMATE_EMAILS_MORNING-DRAFTS (TIME: 15-20 min)
        STEPS: [
          CONFIGURE_GMAIL_MCP_CONNECTOR,
          DEFINE_AUTOMATION_RULES,
          TEST_DRAFT_GENERATION
        ]

CROSS_DEPARTMENT_COLLABORATION:
  - Sales/AI owns Phases 1-2 (sourcing and enrichment)
  - Development assists Phase 3 (MCP connector setup)
  - Operations owns Phase 3 ongoing (automation configuration and maintenance)
  - Sales uses Phase 3 output (automated drafts) for daily operations
```

**Extraction Guidelines:**
- Only extract project structure if video shows clear multi-phase workflow
- Each phase should have 1-3 milestones
- Each milestone should have 1-5 tasks
- Reference Task Templates from section 4B by name
- Reference Step Templates from section 4C by name
- Document cross-department collaboration patterns explicitly
- Include ROI/cost estimates if mentioned in video

---

### 5. Action Verbs & Operations

**Extract ALL action verbs and operations mentioned:**

Create categorized lists (SAME AS V3.1):

#### A. CREATION VERBS (Making new things)
- Create, Generate, Design, Build, Develop, Draft, Produce, Craft, Compose
- [Add others found]

#### B. MODIFICATION VERBS (Changing existing things)
- Edit, Refine, Optimize, Enhance, Update, Revise, Improve, Adjust, Customize
- [Add others found]

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- Analyze, Review, Evaluate, Research, Assess, Examine, Test, Compare, Verify
- [Add others found]

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Organize, Structure, Categorize, Schedule, Plan, Coordinate, Prioritize, Arrange
- [Add others found]

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Present, Share, Publish, Export, Deliver, Communicate, Report, Demonstrate
- [Add others found]

#### F. BROWSER/AGENTIC OPERATIONS (AI Agent & Automation Actions)
- Takes over, Controls, Automates, Executes, Opens, Clicks, Closes, Scrolls, Navigates, Fills in, Hovers, Submits, Adds, Imports, Migrates, Interacts
- [Add others found]

**Note**: Captures action verbs specific to AI agents, browser automation tools, RPA systems.

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Scrape, Parse, Extract, Feed, Import, Upload, Download, Export, Enrich, Validate, Verify, Deduplicate, Sanitize, Trim, Filter, Transform, Convert, Merge, Split, Combine, Map, Match, Lookup
- [Add others found]

**Note**: ETL operations, data enrichment, data quality processes.

---

### 6. Task Chains

**Identify sequential task chains (multi-step processes):**

Format:
```
TASK CHAIN: [Name]
[Step 1] → [Step 2] → [Step 3] → [Output]

Example:
TASK CHAIN: Automated Documentary Creation
Research topic (Perplexity) → Generate script (AI) → Create video (VAYU+Seedream) → Add voiceover (Eleven Labs) → Review & publish
```

---

### 7. Responsibilities Vocabulary

#### 7A. Professional Roles Mentioned:
- Content Creator
- Video Editor
- Graphic Designer
- [List all mentioned]

#### 7B. Skills Extraction (Responsibility + Tool Format) ⭐ ENHANCED IN V3.2

**Extract skills in standardized format with task linkage:**

**PURPOSE:** Skills link people to tasks. When you know someone has "enriched emails via Anymailfinder" skill, you know they can execute ENRICH_LEADS_MULTI-SOURCE task. This enables skill-based task assignment and training path development.

**Format:**
```
SKILL: [ACTION]_[OBJECT]_VIA_[TOOL]
SKILL_ID: [TBD - will be assigned during taxonomy integration]
SKILL_PHRASE: "[action in past tense] [object] via [tool]"
DIFFICULTY: [Beginner/Intermediate/Advanced/Expert]
PROFESSIONS: [Roles that use this skill]
PARENT_TASKS: [Tasks that require this skill - reference section 4B]
WORKFLOWS: [Workflows where this skill is used - reference section 4]
TOOLS_REQUIRED: [Tools needed for this skill]
TIME_TO_LEARN: [If mentioned or estimable]
DESCRIPTION: [Brief explanation of what this skill enables]
```

**Example 1:**
```
SKILL: ENRICH_EMAILS_VIA_ANYMAILFINDER
SKILL_ID: TBD
SKILL_PHRASE: "enriched emails via Anymailfinder"
DIFFICULTY: Beginner
PROFESSIONS: [Lead Generator, SDR, Sales Development Representative]
PARENT_TASKS: [
  ENRICH_LEADS_MULTI-SOURCE,
  GENERATE_ENTERPRISE_EMAIL_LISTS,
  VALIDATE_LINKEDIN_EXPORTS
]
WORKFLOWS: [
  Multi-Source Lead Enrichment Pipeline,
  Enterprise Email Discovery,
  LinkedIn Export Enhancement
]
TOOLS_REQUIRED: [Anymailfinder, CSV/spreadsheet tool]
TIME_TO_LEARN: 15-30 minutes
DESCRIPTION: Ability to use Anymailfinder's nominative enrichment to find decision-maker emails from company domains and names. Includes bulk upload, decision-maker search configuration, and result download. Achieves 20-100% success rate depending on source quality at $0.0025 per valid email found.
```

**Example 2:**
```
SKILL: GENERATE_MCP_CONNECTORS_VIA_CLAUDE
SKILL_ID: TBD
SKILL_PHRASE: "generated MCP connectors via Claude"
DIFFICULTY: Intermediate
PROFESSIONS: [AI Engineer, Backend Developer, Automation Engineer]
PARENT_TASKS: [
  GENERATE_CONNECTOR_VIA_MCP-BUILDER,
  BUILD_GMAIL_AUTOMATION,
  CREATE_CALENDAR_INTEGRATION
]
WORKFLOWS: [
  MCP Connector Generation,
  Email Automation Setup,
  Stacked Connector Configuration
]
TOOLS_REQUIRED: [Claude Desktop, MCP Builder Skill]
TIME_TO_LEARN: 10-20 minutes (skill exists, just needs enabling)
DESCRIPTION: Ability to use Claude's MCP Builder skill to generate production-ready MCP connector code in 30-60 seconds with 2-sentence prompts. Revolutionary speed compared to 2-4 hours manual coding. Generates complete OAuth integration, API handlers, error handling. 95%+ success rate.
```

**Example 3:**
```
SKILL: BUILD_N8N_WORKFLOWS
SKILL_ID: TBD
SKILL_PHRASE: "built enrichment pipelines via n8n"
DIFFICULTY: Advanced
PROFESSIONS: [Backend Developer, Automation Engineer, AI Engineer]
PARENT_TASKS: [
  AUTOMATE_HTML_PARSING_WORKFLOW,
  BUILD_CUSTOM_NICHE_SCRAPER,
  CREATE_MULTI-SOURCE_ENRICHMENT
]
WORKFLOWS: [
  Custom Niche Platform Scraper,
  AI-Powered HTML Parsing Pipeline
]
TOOLS_REQUIRED: [n8n, Apify, OpenAI GPT-5, HTTP request tools]
TIME_TO_LEARN: 4-8 hours
DESCRIPTION: Ability to design and implement automated data enrichment workflows in n8n, connecting HTTP requests, data parsing, AI extraction, and database storage. Creates custom scrapers for niche platforms where standard tools fail. Achieves 11.5% reply rate (vs 1-3% industry average) through highly targeted scraping.
```

**Extraction Guidelines:**
- Extract skills in "action via tool" format consistently
- Link skills to tasks (which tasks require this skill?)
- Link skills to workflows (where is this skill used?)
- Always include difficulty level (helps with training path planning)
- Include time-to-learn if mentioned or estimable
- Capture ROI metrics if mentioned (cost savings, time savings, success rates)

---

### 7C. Responsibilities/Activities:
- "Creating thumbnails"
- "Editing videos"
- "Optimizing for CTR"
- "Managing social media content"
- [Extract all responsibility phrases]

---

### 8. Tools & Technologies Matrix

**Create a comprehensive tools matrix:**

| Tool Name | Category | Purpose | Used For | Mentioned With |
|-----------|----------|---------|----------|----------------|
| GLIF | Workflow Automation | Orchestrate AI tools | Automating content creation | Sora, Kling, Eleven Labs |
| Nano Banana | Image Generation | Create thumbnails | YouTube thumbnail optimization | Photoshop |
| [Continue...] | | | | |

---

### 9. Objects & Deliverables

**List all tangible outputs/deliverables mentioned:**

- Thumbnails
- Videos (specify type: TikTok, documentary, etc.)
- Scripts
- Voiceovers
- Images
- Reports
- Presentations
- Leads (enriched, validated)
- Connectors (MCP, API)
- Workflows (automated)
- [Add all others]

---

### 10. Integration Patterns

**Document how tools/processes connect:**

Format:
```
INTEGRATION: [Tool A] + [Tool B]
PURPOSE: [Why they're used together]
FLOW: [Tool A output] → [becomes] → [Tool B input]

Example:
INTEGRATION: Perplexity + Seedream + Eleven Labs
PURPOSE: Create factually accurate miniature documentaries
FLOW: Historical facts (Perplexity) → Script → Video generation (Seedream) → Voiceover (Eleven Labs) → Final documentary
```

---

### 11. Business Concepts & Strategy

**Extract business/strategy concepts mentioned:**

- Business models mentioned (e.g., "ACP funnel")
- Success metrics (e.g., "CTR", "engagement", "enrichment rate", "reply rate", "ROI")
- Strategic approaches (e.g., "build audience first", "arbitrage strategy")
- Value propositions (e.g., "10x productivity", "15+ hours/week saved", "$0.0025 per email")
- Cost optimization strategies (e.g., "1:40 credit-to-email ratio")

---

### 12. Optimization & Best Practices

**Document any optimization tips or best practices:**

Format:
```
OPTIMIZATION: [Area being optimized]
TECHNIQUE: [How to optimize]
REASON: [Why this works]
EVIDENCE: [Timestamp where mentioned]

Example:
OPTIMIZATION: Thumbnail CTR
TECHNIQUE: Use high contrast, bold text area, Mr. Beast style
REASON: Catches attention in crowded feeds
EVIDENCE: [02:34 - 03:15]
```

---

### 13. Reusability Analysis ⭐ NEW IN V3.2

**For extracted tasks and steps, identify reusability opportunities:**

**Task Reusability:**
```
TASK: [Task name from section 4B]
REUSABLE_IN:
  - [Context 1 where task could be reused]
  - [Context 2]
  - [Context 3]
VARIATIONS:
  - [Variation 1: different tool/method]
  - [Variation 2: different context]
```

**Step Reusability:**
```
STEP: [Step name from section 4C]
REUSABLE_IN:
  - [Task 1 that could use this step]
  - [Task 2]
  - [Task 3]
SIMILAR_STEPS:
  - [Step with similar function but different tool]
```

**Example:**
```
TASK: ENRICH_LEADS_MULTI-SOURCE
REUSABLE_IN:
  - Partner recruitment campaigns
  - Event attendee outreach
  - Customer win-back campaigns
  - Competitor analysis projects
  - Market research initiatives
VARIATIONS:
  - ENRICH_LEADS_SINGLE-SOURCE (using only one enrichment tool for cost savings)
  - ENRICH_LEADS_ENTERPRISE (focused on large companies with Airscale arbitrage)
  - ENRICH_LEADS_LOCAL (geographic-specific with Google Maps data)

STEP: SCRAPE_COMPANY_DATA_FROM_AIRSCALE
REUSABLE_IN:
  - Any task requiring company list generation
  - Market research projects (TAM analysis)
  - Competitive intelligence gathering
  - Account-based marketing targeting
  - Industry analysis projects
SIMILAR_STEPS:
  - SCRAPE_COMPANY_DATA_FROM_LINKEDIN (same action, different source)
  - SCRAPE_COMPANY_DATA_FROM_APOLLO (could consolidate if Apollo returns)
  - SCRAPE_COMPANY_DATA_FROM_GOOGLE-MAPS (for local businesses)
```

---

### 14. Success Metrics & Performance Data ⭐ NEW IN V3.2

**Extract quantitative performance data mentioned:**

Format:
```
METRIC: [Metric name]
WORKFLOW/TASK: [Which workflow or task this metric applies to]
VALUE: [Actual value mentioned]
CONTEXT: [Conditions, timeframe, comparison]
BENCHMARK: [Industry standard if mentioned]
```

**Examples:**
```
METRIC: Enrichment Rate
WORKFLOW: Multi-Source Lead Enrichment Pipeline
TASK: ENRICH_LEADS_MULTI-SOURCE
VALUE: 80-100%
CONTEXT: When using LinkedIn Sales Navigator + Vayne + Anymailfinder combination
BENCHMARK: Industry average 40-60% with standard tools

METRIC: Cost Per Email
WORKFLOW: Multi-Source Lead Enrichment Pipeline
TASK: ENRICH_LEADS_MULTI-SOURCE
VALUE: $0.0025 per email
CONTEXT: Using Anymailfinder nominative enrichment
BENCHMARK: Apollo.io $0.10-0.15 per lead (80-95% cheaper)

METRIC: Time Savings
WORKFLOW: Stacked Connector Post-Meeting Automation
TASK: AUTOMATE_POST-MEETING_FOLLOW-UP
VALUE: 15+ hours per week
CONTEXT: After one-time 2-3 hour setup, automation handles all meeting follow-up
BENCHMARK: Manual process takes 15-20 hours/week for heavy meeting schedules

METRIC: Connector Generation Speed
WORKFLOW: MCP Connector Generation
TASK: GENERATE_CONNECTOR_VIA_MCP-BUILDER
VALUE: 30-60 seconds
CONTEXT: Using Claude MCP Builder skill with 2-sentence prompt
BENCHMARK: Manual coding takes 2-4 hours (99% faster)

METRIC: Reply Rate
WORKFLOW: Custom Niche Platform Scraper
TASK: BUILD_CUSTOM_NICHE_SCRAPER
VALUE: 11.5%
CONTEXT: Using custom n8n + AI HTML parsing for highly targeted niche scraping
BENCHMARK: Industry average 1-3% (4-11x better)

METRIC: ROI Ratio
WORKFLOW: Enterprise Email Arbitrage
TASK: EXECUTE_AIRSCALE_ARBITRAGE
VALUE: 1:40 (1 credit yields 40 emails)
CONTEXT: Using Anymailfinder company search on Airscale unlock
BENCHMARK: Standard enrichment 1:1 ratio
```

---

## FORMATTING STANDARDS

### General Markdown Rules:
- Use `#` headers for major sections
- Use `##` for subsections
- **Bold** important terms
- `Code formatting` for tool names and technical terms
- Bullet points for lists
- Tables for structured data
- Timestamps in [MM:SS] format

### Taxonomy-Specific Formatting:
- ACTION VERBS: Always in CAPS when categorizing
- Tool names: Always capitalized consistently
- Workflows: Always use structured format
- Task names: ACTION_OBJECT_CONTEXT in ALL_CAPS
- Step names: ACTION_OBJECT_SPECIFIC_DETAIL in ALL_CAPS
- Skill phrases: "action via tool" in lowercase natural language
- Task chains: Use → arrows between steps

---

## VALIDATION CHECKLIST

### FORMAT VALIDATION (CRITICAL - Check First!)
- [ ] **Output is markdown (.md)** - NOT JSON, NOT plain text
- [ ] **Document starts with # heading** - Proper markdown structure
- [ ] **File would save as .md extension** - Confirm format
- [ ] **No JSON curly braces `{}` at document start** - Must be markdown

### SECTION COMPLETENESS (V3.2 REQUIREMENTS)
- [ ] **All 3 core sections present:**
  - [ ] 1. Metadata Section
  - [ ] 2. Description Section
  - [ ] 3. Word-for-Word Transcription

- [ ] **TAXONOMY ANALYSIS section included** - This is NOT optional

- [ ] **All required taxonomy subsections present:**
  - [ ] 4. Workflows Identified (with DEPARTMENT field)
  - [ ] 4B. Task Templates Extraction (NEW - ACTION_OBJECT_CONTEXT format) ⭐
  - [ ] 4C. Step Templates Extraction (NEW - with parent task linkage) ⭐
  - [ ] 4D. Project Templates Extraction (NEW - if applicable) ⭐
  - [ ] 5. Action Verbs & Operations (A-G categories)
  - [ ] 6. Task Chains
  - [ ] 7A. Professional Roles Mentioned
  - [ ] 7B. Skills Extraction (NEW - "action via tool" format) ⭐
  - [ ] 7C. Responsibilities/Activities
  - [ ] 8. Tools & Technologies Matrix
  - [ ] 9. Objects & Deliverables
  - [ ] 10. Integration Patterns (if applicable)
  - [ ] 11. Business Concepts & Strategy (if applicable)
  - [ ] 12. Optimization & Best Practices (if applicable)
  - [ ] 13. Reusability Analysis (NEW) ⭐
  - [ ] 14. Success Metrics & Performance Data (NEW) ⭐

### CONTENT QUALITY (V3.2 STANDARDS)
- [ ] All workflows have DEPARTMENT field
- [ ] All workflows have structured format (OBJECTIVE, STEPS, DURATION, etc.)
- [ ] Task Templates follow ACTION_OBJECT_CONTEXT naming
- [ ] Step Templates follow ACTION_OBJECT_SPECIFIC_DETAIL naming
- [ ] Skills follow "action via tool" phrase format
- [ ] Task Templates link to Step Templates (STEPS_USED field)
- [ ] Skills link to tasks (PARENT_TASKS field)
- [ ] Reusability contexts identified for tasks and steps
- [ ] Success metrics extracted with values and context
- [ ] Action verbs categorized into 7 categories (A-G)
- [ ] Tools matrix in TABLE format (not JSON, not bulleted list)
- [ ] Task chains show clear flow with arrows (→)
- [ ] Timestamps provided for key concepts
- [ ] Business value captured
- [ ] No character-by-character text corruption

---

## Taxonomy Mapping Guide

### How V3.2 Extracted Data Maps to Taxonomy:

| Extracted Element | Maps To Taxonomy | File Location | Processing Required |
|-------------------|------------------|---------------|---------------------|
| **Task Templates (4B)** | Task_Templates/*.json | TASK_MANAGERS/Task_Templates/ | Assign TASK-TEMPLATE-XXX ID, create JSON |
| **Step Templates (4C)** | Step_Templates/*.md | TASK_MANAGERS/Step_Templates/ | Assign STEP-TASK-TEMPLATE-XXX-YY ID, create MD |
| **Project Templates (4D)** | Project_Templates/*.json | TASK_MANAGERS/Project_Templates/ | Assign TEMPLATE-PROJ-XXX-YYY ID, create JSON |
| **Skills (7B)** | Skills/*.json | TALENTS/Skills/ | Assign SKL-XXX ID, link to tasks |
| **Workflows (4)** | Workflows/*.yaml | Various | Convert to workflow format |
| **Action Verbs (5)** | Actions/*.json | LIBRARIES/Actions/ | Categorize and add |
| **Tools (8)** | Tools/*.json | LIBRARIES/Tools/ | Create individual tool files |
| **Objects (9)** | Objects/*.json | LIBRARIES/Objects/ | Categorize and add |
| **Responsibilities (7C)** | Professions/*.json | LIBRARIES/Professions/ | Map to professions |
| **Integration Patterns (10)** | Tool JSON integration_with fields | LIBRARIES/Tools/ | Add to tool files |

### V3.2 Time Savings:

**Before v3.2 (with v3.1):**
- Video transcription: 30-60 min
- Manual library mapping: 2-4 hours
- Task Template creation: 1-2 hours
- Step extraction: 1-2 hours
- Total: 4.5-9.5 hours per video

**After v3.2:**
- Video transcription: 30-60 min
- Direct extraction: Included in transcription
- Taxonomy integration: 10-20 min (assign IDs, create files)
- Total: 40-80 minutes per video

**Savings: 90-95% reduction in post-processing time**

---

## Priority for Taxonomy Updates:

1. **Highest Priority**: Task Templates (4B), Step Templates (4C), Skills (7B)
2. **High Priority**: Project Templates (4D), Workflows (4), Tools (8)
3. **Medium Priority**: Success metrics (14), Reusability analysis (13), Action verbs (5)
4. **Low Priority**: Business concepts (11), Integration patterns (10), Optimization tips (12)

---

## CRITICAL INSTRUCTIONS

1. **Never miss action verbs** - They map directly to taxonomy actions and task naming
2. **Extract every workflow step** - Each becomes a reusable Step Template
3. **Follow naming conventions** - ACTION_OBJECT_CONTEXT for tasks, "action via tool" for skills
4. **Link elements** - Tasks link to steps, steps link to tasks, skills link to tasks
5. **Identify reusability** - Where else could this task/step be used?
6. **Capture exact performance metrics** - ROI, time savings, success rates with context
7. **Document cross-department patterns** - How departments collaborate
8. **Extract project structure if present** - Phase → Milestone → Task → Step hierarchy

---

## Usage Notes

### For AI Transcription:
- Use this prompt as system instructions
- Process video audio/captions through this structure
- Output complete structured markdown
- **NEW**: Ensure sections 4B, 4C, 4D, 7B, 13, 14 are populated

### For Manual Transcription:
- Follow structure systematically
- Use provided templates for each section
- Don't skip NEW v3.2 sections (4B, 4C, 4D, 7B, 13, 14)
- Focus on linking elements (tasks to steps, skills to tasks)

### For Quality Assurance:
- Verify all timestamps are accurate
- Ensure action verbs are properly categorized
- Confirm task naming follows ACTION_OBJECT_CONTEXT
- Check that tasks link to steps via STEPS_USED field
- Check that skills link to tasks via PARENT_TASKS field
- Validate reusability contexts are identified
- Confirm success metrics have values and context

---

## Version History

**v3.2** (2025-11-13) - **MAJOR UPDATE**
- **ADDED:** Section 4B - Task Templates Extraction (ACTION_OBJECT_CONTEXT format)
- **ADDED:** Section 4C - Step Templates Extraction (with parent task linkage)
- **ADDED:** Section 4D - Project Templates Extraction (Phase → Milestone → Task → Step)
- **ENHANCED:** Section 7B - Skills Extraction (enriched with task linkage, "action via tool" format)
- **ADDED:** Section 13 - Reusability Analysis (identify cross-task/project reuse)
- **ADDED:** Section 14 - Success Metrics & Performance Data (quantitative extraction)
- **ADDED:** Taxonomy Naming Conventions section (standardize task/step/skill naming)
- **ADDED:** DEPARTMENT field to workflows (section 4)
- **ADDED:** CROSS_DEPT_PATTERN field to workflows (identify collaboration)
- **ENHANCED:** Validation checklist with v3.2 requirements
- **ENHANCED:** Taxonomy mapping guide with v3.2 elements
- **IMPACT:** Enables direct extraction of Phase 4-8 taxonomy elements
- **TIME SAVINGS:** Reduces post-processing from 2-4 hours to 10-20 minutes (90-95% savings)
- Based on Phases 4-8 learnings: 22 Task Templates, 141 Step Templates, 3 Project Templates, 12 skills with task linkage

**v3.1** (2025-11-12)
- **CRITICAL:** Strengthened markdown format requirement
- **ADDED:** G. DATA OPERATIONS action verb category
- **ADDED:** Format validation checklist section
- **ADDED:** Character encoding guidance
- **ADDED:** Data workflow example
- **ENHANCED:** Validation checklist with 3-tier structure
- **ENHANCED:** Technical requirements section

**v3.0** (2025-11-12)
- Added F. BROWSER/AGENTIC OPERATIONS action verb category
- Added browser automation workflow example
- Enhanced markdown output format specification
- Support for agentic AI, browser automation, and RPA scenarios

**v2.0** (2025-11-11)
- Added comprehensive taxonomy extraction requirements
- Added workflows, action verbs, task chains sections
- Added responsibilities vocabulary extraction
- Added integration patterns documentation
- Added business concepts and optimization sections
- Enhanced with validation checklist

**v1.0** (Initial)
- Basic word-for-word transcription format
- Metadata and description sections

---

**Maintained By**: Taxonomy Team
**Last Updated**: 2025-11-13
**Status**: Active - Production Ready
**Version**: 3.2
**Major Upgrade**: Phase 4-8 Integration - Direct Taxonomy Extraction Enabled
