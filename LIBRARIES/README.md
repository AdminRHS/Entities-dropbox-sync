# LIBRARIES Entity Documentation

**Entity Type:** LIBRARIES
**Domain:** Knowledge Base
**Purpose:** Centralized repository of reusable components and definitions
**Created:** November 1, 2025
**Last Updated:** November 17, 2025

> **🔄 Recent Migration (2025-11-17):**
> Actions and Objects have been consolidated under the **Responsibilities** ecosystem.
> See [ACTIONS_README.md](ACTIONS_README.md) and [OBJECTS_README.md](OBJECTS_README.md) for navigation.

---

## 📋 Overview

The LIBRARIES entity domain serves as the centralized repository of reusable components, definitions, and standards. It enforces naming consistency, enables AI-powered task recommendation, simplifies onboarding with standard vocabulary, supports cross-platform coordination, and facilitates automation and integration.

### 🌐 Microservice Access

**Live Microservice:** [https://libs.anyemp.com/](https://libs.anyemp.com/)

The LIBRARIES entity is available as a live microservice providing API access to all library data including Actions, Objects, Tools, Processes, Results, Skills, Professions, Products, Services, and more.

---

## 🗂️ Sub-Entities

### 1. Actions
**Purpose:** Standardized action verbs for task naming

> **📍 Location:** Now part of Responsibilities ecosystem
> **Path:** `LIBRARIES/Responsibilities/Actions/`
> **Quick Navigation:** See [ACTIONS_README.md](ACTIONS_README.md)

**Key Attributes:**
- Action (standardized action verb)
- Action_Type (Communication, Creation, Analysis, Management, etc.)
- Common objects it pairs with
- Tool requirements
- Example usage

**Action_Types:**
- **Communication:** Send, Notify, Contact, Respond, Follow-up
- **Creation:** Create, Generate, Build, Design, Develop
- **Analysis:** Analyze, Review, Evaluate, Assess, Research
- **Management:** Update, Manage, Organize, Coordinate, Track
- **Processing:** Process, Transform, Convert, Export, Import

**File Structure:**
```
Responsibilities/Actions/
├── Actions_Master.json                 # 429 actions - complete catalog
├── Actions_Master_Command_Verbs.json   # Command-oriented subset
├── Actions_Master_Process_Verbs.json   # Process-oriented subset
├── Actions_Master_Result_Verbs.json    # Result-oriented subset
├── Video_Generation_Actions.json       # Video-specific actions
└── README.md
```

**Legacy Note:** Previous root-level `actions.json` archived to `Archive/Legacy_Root_Files/`

---

### 2. Processes
**Purpose:** Verbs in gerund form that serve dual functions: tracking work status and defining responsibilities

**Dual Function:**
1. **Work Status**: Show what a person is currently or still working on (active work states)
2. **Responsibilities**: Define what a person can perform and knows how to perform (capabilities and competencies)

**Key Attributes:**
- Process name (gerund form: "creating", "analyzing", "communicating")
- Category (Communication, Creation, Analysis, Management, Processing, Verification, Storage, General)
- Description of the ongoing action
- Related actions that lead to this process
- Common departments that perform this process
- Common professions that perform this process
- Usage count (frequency in the system)
- Tags for searchability

**Usage:**
- **Work Tracking**: "Currently creating job posting" - shows active work status
- **Responsibilities**: "Can perform designing, creating, drafting" - shows capabilities
- **Skills Foundation**: Processes combined with objects and tools form skills

**Categories:**
- **Communication:** Communicating, Notifying, Responding, Sharing, Distributing
- **Creation:** Creating, Generating, Building, Designing, Developing, Drafting
- **Analysis:** Analyzing, Reviewing, Evaluating, Assessing, Researching, Comparing
- **Management:** Managing, Organizing, Coordinating, Tracking, Monitoring, Updating
- **Processing:** Processing, Transforming, Converting, Exporting, Importing, Formatting
- **Verification:** Verifying, Checking, Confirming, Validating, Testing, Auditing
- **Storage:** Storing, Archiving, Saving, Filing, Logging, Recording
- **General:** Other processes that don't fit into specific categories

**Relationship to Actions:**
Processes represent the ongoing state of an action. For example:
- Action: "Create" → Process: "Creating" → Result: "Created"
- Action: "Analyze" → Process: "Analyzing" → Result: "Analyzed"

**File Structure:**
```
Processes/
├── Communication_Processes.json
├── Creation_Processes.json
├── Analysis_Processes.json
├── Management_Processes.json
├── Processing_Processes.json
├── Verification_Processes.json
├── Storage_Processes.json
└── General_Processes.json
```

**Total:** 428 unique processes extracted from actions.json

---

### 3. Results
**Purpose:** Completed states or outcomes that represent finished work

**Key Attributes:**
- Result name (past participle form: "created", "analyzed", "communicated")
- Category (Communication, Creation, Analysis, Management, Processing, Verification, Storage, General)
- Description of the completed state
- Related actions that produce this result
- Common departments that achieve this result
- Common professions that achieve this result
- Usage count (frequency in the system)
- Tags for searchability

**Categories:**
- **Communication:** Sent, Notified, Contacted, Responded, Shared, Distributed, Communicated
- **Creation:** Created, Generated, Built, Designed, Developed, Drafted, Written
- **Analysis:** Analyzed, Reviewed, Evaluated, Assessed, Researched, Examined, Compared
- **Management:** Managed, Organized, Coordinated, Tracked, Monitored, Updated
- **Processing:** Processed, Transformed, Converted, Exported, Imported, Formatted, Refined
- **Verification:** Verified, Checked, Confirmed, Validated, Tested, Audited
- **Storage:** Stored, Archived, Saved, Filed, Logged, Recorded
- **General:** Other results that don't fit into specific categories

**Relationship to Actions:**
Results represent the completed state of an action. They are used to describe what has been accomplished:
- "The document has been created"
- "The analysis has been completed"
- "The email has been sent"

**File Structure:**
```
Results/
├── Communication_Results.json
├── Creation_Results.json
├── Analysis_Results.json
├── Management_Results.json
├── Processing_Results.json
├── Verification_Results.json
├── Storage_Results.json
└── General_Results.json
```

**Total:** 432 unique results extracted from actions.json

---

### 4. Objects
**Purpose:** Business objects that actions are performed on

> **📍 Location:** Now part of Responsibilities ecosystem
> **Path:** `LIBRARIES/Responsibilities/Objects/`
> **Quick Navigation:** See [OBJECTS_README.md](OBJECTS_README.md)

**Key Attributes:**
- Object name
- Category (Document, Communication, Data, Media, etc.)
- Attributes/fields
- Common actions performed
- Storage location patterns
- Related entities

**Categories:**
- **Documents:** Job Posting, Proposal, Report, Contract, Invoice
- **Communications:** Email, Message, Call, Meeting, Notification
- **Data:** Lead, Contact, Company, Project, Task
- **Media:** Video CV, Image, Design, Presentation, Audio

**File Structure:**
```
Responsibilities/Objects/
├── object_types.json                   # Object type classifications
├── Agentic_Engineering_Objects.json    # AI agent objects (13 objects)
├── AI_Automation_Objects.json          # Automation objects (10 objects)
├── Design_Deliverables.json            # Design outputs
├── Documents.json                      # Document objects
├── Lead_Generation_Objects.json        # LG objects (10 objects)
├── Portfolio_Deliverables.json         # Portfolio items
├── Publishing_Deliverables.json        # Publishing outputs
├── RAG_Objects.json                    # RAG system objects (6 objects)
├── Recruitment_Objects.json            # HR objects
├── Social_Media_Deliverables.json      # SMM outputs
├── Video_Deliverables.json             # Video outputs
├── Video_Generation_Objects.json       # Video production objects
└── README.md
```

**Total:** 36+ objects across 13 domain-specific collections

**Legacy Note:** Previous root-level `objects.json` archived to `Archive/Legacy_Root_Files/`

**Object Types:**
The `object_types.json` file contains detailed object type classifications organized by profession. Each object type includes:
- Object name (e.g., "candidates", "APIs", "mockups")
- Type modifiers (e.g., "needed", "applied", "found" for candidates)
- Descriptions for each type
- Profession and department mapping

**Source:** Extracted from `Guides/DATA_EXTRACTION_PROMPT.md` sections on profession-specific object types.

**Professions Covered:**
- HR/Recruiter (candidates, communications, contracts, interviews)
- Lead Generator (accounts, companies, leads, messages)
- Developer (APIs, databases, modules, code)
- Designer (mockups, logos, illustrations, UI Components)
- Video Editor (videos, assets)
- Marketer (ad campaigns, content, keywords, analytics, SEO Objects, social media)
- AI Engineer (models, prompts, training data)

---

### 5. Tools
**Purpose:** AI tools, software, and platform integrations

> **📍 Location:** `LIBRARIES/LBS_003_Tools/`

**Key Attributes:**
- Tool name and vendor
- Category (AI Tools, Development, Design, Marketing, Automation)
- Purpose and use cases
- Skill level required (Novice/Intermediate/Advanced/Expert)
- Cost structure
- Platform compatibility
- Integration capabilities
- Documentation links

**Current Tool Stack:**

**AI/LLM Services:**
- Claude (Anthropic) - Deep analysis, long-context
- ChatGPT (OpenAI) - Content generation, messaging
- Gemini (Google) - Research, large datasets
- Custom GPT - Specialized assistants

**AI Development Tools:**
- Cursor - AI code editor
- Claude Desktop - Local AI access

**Content Generation:**
- Midjourney - Image generation
- Leonardo.ai - Design assets
- ElevenLabs - Voice synthesis
- Gamma AI - Presentations

**Automation Platforms:**
- n8n - Workflow automation (primary)
- Make - Process integration
- Zapier - App connectivity

**Design Tools:**
- Figma - UI/UX design (primary)
- Adobe Suite - Graphics and video
- Canva - Quick content creation
- Blender - 3D modeling

**Development Tools:**
- VS Code - Code editing
- Docker - Containerization
- Git/GitHub - Version control
- PostgreSQL/MongoDB - Databases

**File Structure:**
```
LBS_003_Tools/
├── AI_Tools/                    # Original name kept
│   ├── Claude.json
│   ├── ChatGPT.json
│   ├── Gemini.json
│   └── ...
├── Development_Tools/            # Original name kept
│   ├── Cursor.json
│   ├── VS_Code.json
│   └── ...
├── Automation_Tools/            # Original name kept
│   ├── n8n.json
│   └── Make_com.json
├── Social_Media_Platforms/       # Original name kept
├── Business_Tools/              # Original name kept
├── MCP_Services/                # Original name kept
└── ... (other existing subfolders)
```

---

### 6. Skills
**Purpose:** Phrase-matched skills combining responsibilities (action + object) and tools

> **📍 Location:** `LIBRARIES/../TALENTS/Skills/`

**Key Attributes:**
- Skill ID (SKL-XXX format)
- Skill phrase (natural language description: responsibility + tool)
- Components:
  - **Responsibility**: Action + Object phrase (e.g., "screen candidates", "design UI mockups")
  - **Tool**: Tool used (e.g., "CRM", "Figma", "Gmail")
  - **Result**: Completed action (past participle form)
- Department mapping
- Professions that use this skill
- Difficulty level (beginner/intermediate/advanced/expert)
- Frequency of use
- Time estimate
- Automation potential
- Related skills
- Example tasks
- Training resources

**Formula:**
```
Skill = Responsibility + Tool
Where Responsibility = Action + Object (phrase-matched)

Examples:
- Responsibility: "send cold emails" + Tool: "via Gmail" = "send cold emails via Gmail"
- Responsibility: "design UI mockups" + Tool: "in Figma" = "design UI mockups in Figma"
- Responsibility: "analyze lead data" + Tool: "using Google Sheets" = "analyze lead data using Google Sheets"
- Responsibility: "screen candidates" + Tool: "via CRM" = "screen candidates via CRM"
```

**Use Cases:**
- Talent matching and skill-based employee search
- Resume parsing and automated skill tagging
- Training gap analysis
- AI assistant training for tool recommendations
- Performance reviews and skill growth tracking

**File Structure:**
```
../TALENTS/Skills/
├── Master/                        # Original name kept
│   ├── all_skills.json            # Complete skills catalog (28+ skills)
│   ├── skills_index.json          # Searchable index with keywords
│   └── skills_metadata.json      # Version control & statistics
├── By_Department/                 # Original name kept
│   ├── HR_skills.json
│   ├── LG_skills.json
│   └── ...
├── By_Profession/                 # Original name kept
│   └── ... (13 profession skill files)
├── By_Difficulty/                 # Original name kept
│   ├── beginner.json
│   ├── intermediate.json
│   └── advanced.json
├── By_Tool/                       # Original name kept
├── Mappings/                      # Original name kept
└── Templates/                     # Original name kept
```

**Total:** 28+ skills across 6 departments and 13+ professions

**Cross-References:**
- Skills ↔ Tools (tools used in skills)
- Skills ↔ Professions (who uses these skills)
- Skills ↔ Responsibilities (action + object components)
- Skills ↔ TALENTS (employee skill profiles)

---

### 7. Responsibilities
**Purpose:** Role-based responsibility definitions - what a person can perform and knows how to perform

**Relationship to Processes:**
- Responsibilities are defined by Processes (what can be performed)
- Processes represent capabilities and competencies that form responsibilities
- Example: A Recruiter's responsibilities include "screening", "interviewing", "evaluating" - all processes they can perform

**Key Attributes:**
- Responsibility name (typically Process + Object)
- Department mapping
- Role level (Junior/Mid/Senior/Expert)
- Required processes (what can be performed)
- Required skills (built from processes)
- Related tasks
- Success criteria

**File Structure:**
```
responsibilities.json
```

---

### 8. Parameters
**Purpose:** Configuration parameters and settings for tasks, workflows, and system operations

> **📍 Location:** `LIBRARIES/Responsibilities/Parameters/`

**Key Attributes:**
- Parameter name and value
- Type associations
- Profession mapping
- Department mapping
- Parameter categories
- Usage context

**Organization:**
- Organized by profession (sales manager, lead generator, back end developer, etc.)
- Organized by department (managers, developers, designers, marketers)
- General parameters for cross-functional use

**File Structure:**
```
Responsibilities/Parameters/
├── parameters.json                    # Master parameters file
├── By_Profession/                    # Original name (was organized_by_profession)
│   ├── sales_manager_parameters.json
│   ├── lead_generator_parameters.json
│   └── ...
└── By_Department/                    # Original name (was organized_by_department)
    ├── managers_parameters.json
    ├── developers_parameters.json
    └── ...
```

---

### 9. Professions
**Purpose:** Job roles and profession definitions with department mapping

> **📍 Location:** `LIBRARIES/LBS_005_Professions/`

**Key Attributes:**
- Profession name
- Department mapping
- Standardized profession titles

**File Structure:**
```
LBS_005_Professions/
├── Master/
│   └── professions.json              # Complete professions list with department mapping
└── Individual/                       # Original name kept
    ├── Account_Executive.json
    ├── AI_Engineer.json
    └── ... (15 more individual profession files)
```

---

### 10. Products
**Purpose:** AI-first customer-facing products and services catalog with intelligent pricing and automation

**AI-First Principle:**
All products MUST use AI-native tools OR AI-integrated software to increase efficiency, improve quality, enable scalability, and reduce costs.

**Key Attributes:**
- Product ID (PDT-XXXX format)
- Product name and description
- Category (SEO Services, Lead Generation, Design, Content, Marketing, Video, Technical)
- Pricing (minimum/maximum hours, estimated price range)
- AI Integration details:
  - AI tools used (specific tools with capabilities)
  - AI automation level (Manual/Semi-automated/Highly automated)
  - AI capabilities (what AI handles)
  - Manual components (what requires human expertise)
- Deliverables (what's produced)
- Cross-references (professions, skills, objects)
- Requirements (prerequisites, complexity, duration)
- Related products
- Tags for searchability

**Three-Tier Hierarchy:**
```
Service (Tier 1) > Product (Tier 2) > Responsibility (Tier 3)
```

**Pricing Formula:**
```
Price = ROUND($2000/160 × Hours)
Where:
- $2000 = Monthly FTE cost
- 160 = Billable hours per month
- Base rate = $12.50/hour
```

**Categories:**
1. **SEO Services** (6 products): Website Audit, Keyword Research, On-Page SEO, Content Strategy, Backlink Strategy, Technical SEO
2. **Lead Generation Services** (9 products): Market Analysis, Manual Lead Identification, Lead Qualification, Campaign Analysis, Data-Driven Strategy, Email Campaign Setup, Lead Engagement, Lead Identification, Lead Nurturing, LinkedIn Outreach
3. **Design Services** (3 products): 3D Models, 3D Animation, Brand Identity Design
4. **Content Services** (4 products): Blog & SEO Content, Content Creation, Content Strategy Development, How-To Guides
5. **Marketing Services** (8 products): A/B Testing, Email Marketing Campaigns, Optimization Implementation, PPC Campaign Management, SEO & Content Optimization, Social Media Branding, Social Media Management, Social Media Strategy
6. **Video Services** (5 products): Brand Highlight Reel, FAQ Videos, Product Demonstration, Testimonial Compilation, Tutorial Videos
7. **Technical Services** (4 products): CRM Customization, Website Redesign, Workflow Automation

**Note:** Products and Services have been moved to BUSINESSES entity. See:
- [BUSINESSES/Products/](../../BUSINESSES/Products/README.md) - Products library documentation
- [BUSINESSES/Services/](../../BUSINESSES/Services/README.md) - Services library documentation

**AI Tool Substitution Examples:**
- Traditional keyword research → ChatGPT + SEMrush AI + Ahrefs AI
- Manual content writing → ChatGPT, Claude, Jasper.ai with Surfer SEO
- Manual video editing → Descript + Runway + ElevenLabs
- Manual lead research → Apollo.io AI + Clay.com + LinkedIn Sales Navigator AI

**Total Products:** 39 AI-optimized products across 7 categories

**Cross-References:**
- Products ↔ Tools (AI tools used in delivery)
- Products ↔ Objects (deliverables created)
- Products ↔ Professions (who delivers the product)
- Products ↔ Skills (capabilities required)
- Products ↔ Workflows (how the product is delivered)

---

### 11. Services
**Note:** Services have been moved to BUSINESSES entity. See [BUSINESSES/Services/](../../BUSINESSES/Services/README.md) for complete documentation.

---

### 12. ~~Prompts~~ [MOVED]

> **📍 MOVED (2025-11-15):** The Prompts sub-entity has been relocated from `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/` to `LIBRARIES/DEPARTMENTS/_SHARED/PROMPTS/` as part of architectural reorganization to align with department-oriented resource structure.

**New Location:** `Entities/LIBRARIES/DEPARTMENTS/_SHARED/PROMPTS/`

**Archive Location:** `Entities/LIBRARIES/DEPARTMENTS/_SHARED/Archive/PROMPTS_Archive/`

**Purpose:** Centralized repository of AI prompts and custom instructions for taxonomy workflows

**Why Moved:**
- Aligns with department-oriented architecture
- Maintains centralized prompt governance while placing in shared resources
- Consolidates cross-department resources in LIBRARIES/DEPARTMENTS/_SHARED
- Separates active content from archive

**What Was Moved:**
- 146 files total (135 active + 11 archive)
- 9 prompt categories (Core, Video_Processing, HR_Operations, Library_Processing, Research, Daily_Reports, Operational_Workflows, Automation, Communication)
- 12 active prompts across 5 categories
- Complete documentation (PROMPTS_INDEX.json v1.2, README.md, category READMEs)

**For Current Documentation:**
- See: `LIBRARIES/DEPARTMENTS/_SHARED/PROMPTS/README.md` for complete prompts documentation
- See: `LIBRARIES/DEPARTMENTS/_SHARED/PROMPTS/PROMPTS_INDEX.json` for master catalog (v1.2)
- See: Migration report at `Taxonomy/Prompts_Migration_Report_2025-11-15.md` (if available)

**Cross-References (Updated Paths):**
- Prompts ↔ Transcribations (video processing workflow documentation)
- Prompts ↔ All LIBRARIES (integration methodologies for each entity type)
- Prompts ↔ Tools (extraction and cataloging methodologies)
- Prompts ↔ Products (AI-first optimization guidelines)
- Prompts ↔ Actions, Objects, Processes (extraction templates)

---

## 🔗 Relationships

### Primary Relationships

1. **LIBRARIES ↔ TASK_MANAGERS**
   - Tasks composed of Actions + Objects
   - Tasks track Processes (work status - what is currently being done)
   - Tasks produce Results (completed work)
   - Tasks require specific Tools
   - Tasks assigned based on Responsibilities (which are defined by Processes)

2. **LIBRARIES ↔ TALENTS**
   - Skills (SKL-XXX) define standardized skill catalog combining Responsibilities + Tools
   - Professions define required skills (reference SKL-XXX IDs from Skills catalog)
   - Employees have skill profiles referencing SKL-XXX IDs from Skills catalog
   - Employees have tool proficiency levels
   - Skills linked to employee profiles (show Responsibilities + Tools they can perform)
   - Responsibilities mapped to roles (action + object phrases - what can be performed)
   - Processes show both work status (current work) and capabilities (what can be done)

3. **LIBRARIES ↔ JOBS**
   - Jobs reference professions
   - Jobs require specific tools
   - Jobs use standard actions and objects
   - Jobs require specific skills from skills library (Responsibilities + Tools)

---

## 📊 Example Usage

### Action-Object Pairing
```
Action: "Create"
Object: "Job Posting"
Context: "for Frontend Developer"
Result: Task = "Create Job Posting for Frontend Developer"
```

### Action-Process-Result Flow
```
Action: "Create"
Process: "Creating" (ongoing work OR capability/responsibility)
Result: "Created" (completed work)

Example:
- Action: "Analyze Lead Quality"
- Process: "Analyzing Lead Quality" (in progress - work status)
- Result: "Analyzed Lead Quality" (completed)

Processes serve dual purpose:
1. Work Status: "Currently analyzing lead quality" (what is being done now)
2. Responsibility: "Can perform analyzing" (what can be done - capability)
```

### Tool Requirement Mapping
```
Task: "Generate Video CV"
Required Tools: ["Video Editing Software", "Camera", "Editing Computer"]
Tool Proficiency: "Intermediate" level required
```

### Profession-Skill Mapping
```
Profession: "Frontend Developer"
Required Skills: ["React", "TypeScript", "CSS", "HTML"]
Tool Proficiency: ["VS Code", "Git", "Figma"]
Department: "Dev"
```

---

## 📝 File Naming Convention

**Pattern:** `LIBRARIES_[Type]_[Name]_[Version].json`

**Examples:**
- `LIBRARIES_Action_Create_v1.json`
- `LIBRARIES_Object_Job_Posting_v1.json`
- `LIBRARIES_Tool_Claude_v1.json`
- `LIBRARIES_Profession_Frontend_Developer_v1.json`

---

## 📋 Metadata Template

### Action Template
```json
{
  "entity_type": "LIBRARIES",
  "Library": "Actions",
  "Action_Type": "Creation",
  "actions": [
    {
      "action_id": "ACT-CREATE-001",
      "Action": "Create",
      "description": "Generate or build a new item from scratch",
      "common_objects": ["Job Posting", "Proposal", "Report", "Document"],
      "tool_requirements": ["Notion", "Google Docs"],
      "examples": ["Create Job Posting for Frontend Developer"],
      "tags": ["creation", "generation", "building"]
    }
  ],
  "version": "1.0",
  "created": "2025-11-01",
  "last_updated": "2025-11-01"
}
```

### Object Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Object",
  "object_id": "OBJ-001",
  "name": "Job Posting",
  "category": "Document",
  "attributes": [
    "title",
    "description",
    "requirements",
    "compensation",
    "deadline"
  ],
  "common_actions": ["Create", "Update", "Publish", "Archive"],
  "storage_location": "Entities/JOBS/Job_Postings/",
  "related_entities": ["JOBS", "TALENTS"],
  "tags": ["document", "recruitment", "job"]
}
```

### Tool Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-001",
  "name": "Claude",
  "vendor": "Anthropic",
  "category": "AI/LLM Services",
  "purpose": "Deep analysis, long-context processing",
  "skill_level_required": "Intermediate",
  "cost_structure": "Usage-based pricing",
  "platform_compatibility": ["Web", "Desktop", "API"],
  "integration_capabilities": ["API", "n8n", "Custom integrations"],
  "documentation_url": "https://docs.anthropic.com",
  "tags": ["ai", "llm", "analysis", "long-context"]
}
```

### Process Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Processes",
  "process_id": "PROC-CREA-001",
  "process_name": "creating",
  "category": "Creation",
  "description": "The ongoing action of creating",
  "related_actions": ["Create", "Generate", "Build"],
  "common_departments": ["managers", "developers", "designers"],
  "common_professions": ["project manager", "frontend developer", "graphic designer"],
  "usage_count": 15,
  "tags": ["creation", "creating"]
}
```

### Result Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Results",
  "result_id": "RES-CREA-001",
  "result_name": "created",
  "category": "Creation",
  "description": "The completed state of having created",
  "related_actions": ["Create", "Generate", "Build"],
  "common_departments": ["managers", "developers", "designers"],
  "common_professions": ["project manager", "frontend developer", "graphic designer"],
  "usage_count": 15,
  "tags": ["creation", "created"]
}
```

### Skill Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Skills",
  "skill_id": "SKL-030",
  "skill_phrase": "developed features in React",
  "components": {
    "result": "developed",
    "action": "develop",
    "object": "features",
    "object_type": "UI features, functionality features",
    "tool": "React",
    "tool_category": "Development Framework"
  },
  "department": "Developers",
  "professions": ["frontend developer", "full stack developer"],
  "difficulty_level": "intermediate",
  "frequency": "daily",
  "time_estimate_minutes": 240,
  "automation_potential": "low",
  "related_skills": ["SKL-032", "SKL-033"],
  "example_tasks": [
    "Develop user authentication feature in React",
    "Create responsive navigation component"
  ],
  "training_resources": [],
  "tags": ["react", "frontend", "development", "javascript"]
}
```

### Profession Template
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_id": "PROF-001",
  "title": "Frontend Developer",
  "department": "Dev",
  "skill_requirements": {
    "technical": ["React", "TypeScript", "CSS", "HTML", "JavaScript"],
    "soft_skills": ["Problem Solving", "Communication", "Teamwork"]
  },
  "tool_proficiency": {
    "required": ["VS Code", "Git", "Figma"],
    "optional": ["Docker", "Jest", "Webpack"]
  },
  "typical_responsibilities": [
    "Develop user interfaces",
    "Implement responsive designs",
    "Collaborate with designers",
    "Write clean, maintainable code"
  ],
  "career_progression": {
    "junior": "0-2 years experience",
    "mid": "2-5 years experience",
    "senior": "5+ years experience",
    "expert": "7+ years, leadership role"
  },
  "salary_range": {
    "junior": "$1000-1500/month",
    "mid": "$1500-2500/month",
    "senior": "$2500-4000/month"
  },
  "tags": ["frontend", "react", "typescript", "web_development"]
}
```

---

## 🎯 Business Value

- **Naming Consistency:** Enforces standardized vocabulary across organization
- **AI Task Recommendation:** Enables AI to suggest appropriate tasks
- **Onboarding Simplification:** New employees learn standard vocabulary quickly
- **Cross-Platform Coordination:** Shared definitions enable seamless collaboration
- **Automation Support:** Structured data enables workflow automation

---

## 📚 Related Documents

- `../TASK_MANAGERS/` - Tasks using actions, objects, and tools
- `../TALENTS/` - Employees with profession and tool proficiency
- `../JOBS/` - Jobs requiring specific professions and tools
- `../ACCOUNTS/` - Configuration parameters for tools and processes

---

**Last Updated:** November 25, 2025

