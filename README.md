# ENTITIES - Knowledge and Operations Management System

> **Centralized ecosystem for managing knowledge, operations, talent, and business processes**

[![Sync Status](https://img.shields.io/badge/sync-automatic-green)](https://github.com/AdminRHS/Entities-dropbox-sync/actions)
[![Last Sync](https://img.shields.io/badge/last_sync-24h_ago-blue)]()
[![Total Entities](https://img.shields.io/badge/entities-5,321+-orange)]()

---

## 🎯 What Is This?

**ENTITIES** is a comprehensive knowledge and operations management system that unifies all aspects of organizational work into a single structured ecosystem. The system syncs from Dropbox to GitHub for version control and collaborative work.

### Key Features

- 📚 **Centralized Knowledge Base** — all definitions, standards, and libraries in one place
- 🔄 **Automated Workflows** — task, project, and process templates
- 👥 **Talent Management** — complete lifecycle from candidate to employee
- 🏢 **Client Management** — tracking business relationships and projects
- 🤖 **AI Integration** — prompts and automation for all processes
- 📊 **Analytics & Reporting** — performance tracking and metrics

---

## 🏗️ System Architecture

### Core Entities

The system consists of **8 core entities**, each responsible for its own domain:

```
ENTITIES/
├── 📚 LIBRARIES      → Knowledge base and standards
├── ⚙️  TASK_MANAGERS → Operational processes and templates
├── 👥 TALENTS        → Talent management
├── 🏢 BUSINESSES     → Client management
├── 💼 JOBS           → Job postings and recruitment
├── 🤖 PROMPTS        → AI prompts and instructions
├── ⚙️  SETTINGS       → System settings
└── 🏷️  TAXONOMY      → Classification and ID systems
```

---

## 📚 LIBRARIES — Knowledge Base

**Purpose:** Centralized repository of reusable components, definitions, and standards

**Contains:**
- **Actions (429)** — standardized action verbs (Create, Update, Analyze, Send...)
- **Objects (50+)** — business objects (Job Posting, Email, Report, Video CV...)
- **Tools (176+)** — tools and platforms (Claude, Figma, n8n, Cursor...)
- **Professions (17)** — job roles (Frontend Developer, AI Engineer, Designer...)
- **Responsibilities (377)** — role and department-based duties
- **Skills (28+)** — skills (combination of Responsibility + Tool)
- **Processes (428)** — processes in gerund form (creating, analyzing, managing...)
- **Results (432)** — results in past participle form (created, analyzed, managed...)

**Key Features:**
- 🌐 **Microservice:** [https://libs.anyemp.com/](https://libs.anyemp.com/) — live API access
- 🔗 **Relationships:** Actions + Objects = Tasks, Tools + Responsibilities = Skills
- 📊 **Statistics:** 1,000+ entities across 6 types

**Usage Example:**
```
Task = Action + Object + Context
"Create" + "Job Posting" + "for Frontend Developer"
```

**Structure:**
```
LIBRARIES/
├── Responsibilities/
│   ├── Actions/          # 429 actions
│   ├── Objects/          # 50+ objects
│   └── Parameters/       # Configuration parameters
├── LBS_003_Tools/        # 176+ tools
├── LBS_005_Professions/  # 17 professions
└── LBS_006_Departments/ # Departments
```

---

## ⚙️ TASK_MANAGERS — Operational Engine

**Purpose:** Orchestrates work execution through templates and processes

**Contains:**
- **Project Templates (3)** — project templates (Lead Generation, MCP Automation, ABM Campaign)
- **Milestone Templates (28)** — milestone templates (Content Analysis, Video Processing, Publishing...)
- **Task Templates (93)** — task templates (Create Job Posting, Send Email, Analyze Data...)
- **Step Templates (264)** — step templates (detailed instructions)
- **Workflows (31)** — automated processes (YAML definitions)
- **Guides (34)** — guides and documentation

**Hierarchy:**
```
Project Template
  └── Milestone Template
      └── Task Template
          └── Step Template
              └── Checklist Item
```

**Key Features:**
- 📋 **Template-Driven** — eliminates decision fatigue
- ⏱️ **Time Estimation** — historical data for accurate planning
- 📊 **Performance Tracking** — team and individual metrics
- 🔄 **Automation** — n8n integration for process automation

**Example:**
```json
{
  "task_name": "Create Job Posting for Frontend Developer",
  "action": "Create",
  "object": "Job Posting",
  "context": "for Frontend Developer",
  "estimated_duration": "2 hours",
  "tools_required": ["Notion", "Google Docs"]
}
```

---

## 👥 TALENTS — Talent Management

**Purpose:** Complete talent lifecycle from application to employment

**Contains:**
- **Employees (32)** — current employees by department
- **Candidates** — candidates in hiring pipeline
- **Job Applications** — job applications
- **Skills (28+)** — skills catalog for matching
- **Presales** — client presentation materials (Video CVs, portfolios)

**Departments:**
- **HR:** 2 employees
- **AI:** 3 employees
- **Video:** 3 employees
- **Sales:** 1 employee
- **Design:** 9 employees
- **Dev:** 3 employees
- **LG:** 11 employees

**Key Features:**
- 🎥 **Video-First Approach** — video CVs as competitive advantage
- 🎯 **Rapid Matching** — AI-powered talent-job matching
- 📈 **Skills Gap Analysis** — identifies training needs
- 📊 **Performance Tracking** — data-driven metrics

**Skills Structure:**
```
Skill = Responsibility + Tool
"send cold emails via Gmail" = "send cold emails" + "Gmail"
"design UI mockups in Figma" = "design UI mockups" + "Figma"
```

---

## 🏢 BUSINESSES — Client Management

**Purpose:** Manages client lifecycle and business relationships

**Contains:**
- **Clients (2,374+)** — active clients with full profiles
- **Prospects** — potential clients
- **Ex_Clients** — former clients
- **Products (39)** — AI-optimized products and services
- **Services** — services catalog

**Product Categories:**
- SEO Services (6 products)
- Lead Generation Services (9 products)
- Design Services (3 products)
- Content Services (4 products)
- Marketing Services (8 products)
- Video Services (5 products)
- Technical Services (4 products)

**Key Features:**
- 🤖 **AI-First Principle** — all products use AI tools
- 💰 **Intelligent Pricing** — formula based on hours and rate
- 📊 **Relationship Tracking** — complete interaction history
- 🎯 **Sales Automation** — integration with Lead Generation processes

---

## 💼 JOBS — Talent Marketplace

**Purpose:** Manages job postings, requirements, and talent matching

**Contains:**
- **Job Postings** — active job openings
- **Job Requirements** — structured skill requirements
- **Job Templates** — reusable job templates
- **Job Categories** — classification by categories

**Key Features:**
- 📋 **Standardization** — consistent job posting format
- 🤖 **AI Matching** — automated candidate matching
- 📊 **Pipeline Efficiency** — hiring funnel metrics
- 🌐 **Multi-Platform** — distribution across multiple platforms

---

## 🤖 PROMPTS — AI Instructions

**Purpose:** Centralized repository of AI prompts and instructions

**Contains:**
- **Core System Prompts (3)** — main system prompts (v4, v6)
- **Video Processing (12)** — video processing and transcription
- **Daily Reports (11)** — daily reports by department
- **Taxonomy & System (13)** — taxonomy building and system analysis
- **Research (9)** — research prompts
- **HR Operations (5)** — HR operations
- **Workflows (11)** — operational processes

**Total:** 71 prompts with unique IDs (PMT-001 through PMT-071)

**Key Features:**
- 🆔 **Unique IDs** — each prompt has PMT-### identifier
- 📝 **Version Control** — version tracking for all prompts
- 🔄 **Reusability** — standardized instructions
- 📊 **Cataloging** — complete catalog in CSV and JSON

---

## ⚙️ SETTINGS — System Settings

**Purpose:** Centralized management of settings and configurations

**Contains:**
- **Countries/Cities/Languages** — geographic and language references
- **Currencies/Rates** — currencies and exchange rates
- **Permissions** — access control system
- **Notifications** — notification settings
- **Calendar Configurations** — calendar settings

**Supported Languages:**
- English (primary business language)
- Russian
- Ukrainian
- Polish
- German

---

## 🏷️ TAXONOMY — Classification and ID Systems

**Purpose:** Central hub for IDs, hierarchies, and ISO codes

**Contains:**
- **LIBRARIES Taxonomy** — IDs for Actions, Objects, Tools, Professions (RSP, ACT, OBJ, TOL, PRF...)
- **TASK_MANAGERS Taxonomy** — IDs for Projects, Tasks, Workflows (PRT, MLT, TSK, WRF...)
- **Video Processing Integration** — video process integration with taxonomy
- **Entity Integration** — standard processes for integrating new entities

**ID Systems:**
- **LIBRARIES:** RSP-001, ACT-001, OBJ-001, TOL-001, PRF-001...
- **TASK_MANAGERS:** PRT-001, MLT-001, TSK-001, WRF-001...
- **PROMPTS:** PMT-001, PMT-002, PMT-003...

---

## 🔗 Entity Relationships

### Core Relationship Schema

```
┌─────────────┐
│  LIBRARIES  │ ← Knowledge center
└──────┬──────┘
       │
       ├──→ TASK_MANAGERS (Tasks = Actions + Objects)
       ├──→ TALENTS (Skills = Responsibilities + Tools)
       ├──→ JOBS (Requirements = Professions + Skills)
       └──→ BUSINESSES (Products reference Tools + Objects)
       
┌─────────────┐
│TASK_MANAGERS│ ← Operations
└──────┬──────┘
       │
       ├──→ TALENTS (Tasks assigned to Employees)
       ├──→ BUSINESSES (Client-related tasks)
       └──→ LIBRARIES (Tasks use Actions + Objects)

┌─────────────┐
│   TALENTS   │ ← People
└──────┬──────┘
       │
       ├──→ JOBS (Apply to jobs)
       ├──→ BUSINESSES (Assigned to clients)
       ├──→ TASK_MANAGERS (Assigned to tasks)
       └──→ LIBRARIES (Have Professions + Skills)

┌─────────────┐
│  BUSINESSES │ ← Clients
└──────┬──────┘
       │
       ├──→ TALENTS (Get assigned talent)
       ├──→ JOBS (Post jobs)
       └──→ TASK_MANAGERS (Client-related tasks)
```

### Detailed Relationships

#### 1. LIBRARIES ↔ TASK_MANAGERS
- **Tasks consist of:** Actions + Objects
- **Tasks require:** Tools
- **Tasks assigned based on:** Responsibilities
- **Example:** Task "Create Job Posting" = Action "Create" + Object "Job Posting" + Tool "Notion"

#### 2. LIBRARIES ↔ TALENTS
- **Skills defined as:** Responsibilities (Action + Object) + Tools
- **Professions define:** Required skills and tools
- **Employees have:** Skill profiles with tool proficiency levels
- **Example:** Skill "send cold emails via Gmail" = Responsibility "send cold emails" + Tool "Gmail"

#### 3. TALENTS ↔ TASK_MANAGERS
- **Employees assigned:** To tasks
- **Tasks require:** Specific profession capabilities
- **Performance tracked:** Through task completion
- **Example:** Employee "Artemchuk Nikolay" assigned to Task "Create Job Posting"

#### 4. TALENTS ↔ JOBS
- **Talents apply:** To jobs
- **Jobs require:** Specific talent skills
- **Matching uses:** Skills matrix
- **Example:** Job "Frontend Developer" requires Skills ["React", "TypeScript"] → Match with Talents having these skills

#### 5. BUSINESSES ↔ TALENTS
- **Talents assigned:** To client projects
- **Client feedback affects:** Talent performance metrics
- **Video-first presentation:** Competitive advantage
- **Example:** Client "ABC Corp" gets assigned Talent "Shelep Olha" for Design project

#### 6. PROMPTS ↔ All Entities
- **Prompts process:** Data from all entities
- **Prompts create:** New entities and update existing ones
- **Prompts integrate:** Video content into taxonomy
- **Example:** PMT-004 (Video Transcription) → Extracts Tasks → Updates TASK_MANAGERS

---

## 📊 System Statistics

### Overall Statistics
- **Total Items:** 5,321
- **Total Files:** 3,871
- **Total Directories:** 1,450
- **Total Size:** 78.81 MB
- **Master Files:** 1,049
- **Documentation (.md):** 1,534

### File Type Distribution
- **JSON:** 2,163 files
- **Markdown:** 1,534 files
- **Python:** 83 files
- **CSV:** 33 files
- **YAML:** 21 files

### Distribution by Entity
- **BUSINESSES:** 2,374 items
- **DAILIES:** 545 items
- **TASK_MANAGERS:** 525 items
- **LIBRARIES:** 482 items
- **PROMPTS:** 251 items
- **RESEARCHES:** 238 items
- **TALENTS:** 215 items
- **REPORTS:** 212 items

---

## 🔄 How The System Works

### Complete Cycle Example

**Scenario:** Creating a job posting and hiring an employee

1. **LIBRARIES** → Define requirements:
   - Profession: "Frontend Developer" (PRF-001)
   - Required Skills: ["React", "TypeScript"] (SKL-030, SKL-032)
   - Required Tools: ["VS Code", "Git"] (TOL-045, TOL-067)

2. **JOBS** → Create job posting:
   - Task: "Create Job Posting" (TSK-001)
   - Use template from TASK_MANAGERS
   - Action: "Create" + Object: "Job Posting"

3. **TALENTS** → Find candidates:
   - Search employees with Skills ["React", "TypeScript"]
   - Check Tool Proficiency ["VS Code", "Git"]
   - Match with Job Requirements

4. **TASK_MANAGERS** → Manage process:
   - Project: "Hiring Frontend Developer"
   - Milestones: Application Review → Technical Test → Interview → Offer
   - Tasks assigned to HR team

5. **BUSINESSES** → If for client:
   - Client gets assigned Talent
   - Project created in BUSINESSES
   - Tasks tracked in TASK_MANAGERS

6. **PROMPTS** → Automation:
   - PMT-053 (CV Parser) → Processes applications
   - PMT-056 (Interview Conductor) → Conducts interviews
   - PMT-032 (Daily Reports) → Tracks progress

---

## 🎯 Key Principles

### 1. Knowledge Centralization
All definitions, standards, and libraries are stored in **LIBRARIES**, ensuring consistency across the organization.

### 2. Template-Driven Approach
**TASK_MANAGERS** uses templates to eliminate the need to make decisions every time.

### 3. Entity Composition
Complex entities are built from simple ones:
- **Task** = Action + Object + Context
- **Skill** = Responsibility + Tool
- **Responsibility** = Process + Object

### 4. Versioning and Tracking
All changes are tracked through:
- Git version control
- Automatically generated changelog
- Migration maps for updates

### 5. AI-First Approach
- All products use AI tools
- Prompts are standardized and cataloged
- Automation through n8n workflows

---

## 📖 Quick Start

### For New Users

1. **Study the structure:**
   - Start with `LIBRARIES/README.md` — understanding basic components
   - Then `TASK_MANAGERS/README.md` — how processes work
   - `TALENTS/README.md` — managing people

2. **Use search:**
   - Search by ID (e.g., "ACT-001", "TSK-001")
   - Search by entity name
   - Use Master Lists for navigation

3. **Follow templates:**
   - Use existing task templates
   - Create new ones based on existing
   - Update documentation when making changes

### For Developers

1. **API Access:**
   - LIBRARIES: [https://libs.anyemp.com/](https://libs.anyemp.com/)
   - Use Master Lists (CSV/JSON) for integration

2. **ID Systems:**
   - Follow ISO codes from TAXONOMY
   - Use Master Lists to assign new IDs
   - Update registries when adding new entities

3. **Automation:**
   - Use PROMPTS for AI processing
   - Integrate with n8n through Workflows
   - Use scripts from `scripts/` for bulk operations

---

## 🔍 System Navigation

### Search by Entity Type

**Actions:**
- `LIBRARIES/Responsibilities/Actions/Actions_Master.json`
- 429 actions in 3 categories (Command, Process, Result)

**Objects:**
- `LIBRARIES/Responsibilities/Objects/`
- 50+ objects in 13 domain collections

**Tools:**
- `LIBRARIES/LBS_003_Tools/`
- 176+ tools by category

**Tasks:**
- `TASK_MANAGERS/TSM-003_Task_Templates/`
- 93 task templates

**Skills:**
- `TALENTS/Skills/Master/all_skills.json`
- 28+ skills by department and profession

### Search by Department

**AI & Automation:**
- LIBRARIES: 80 Responsibilities
- TASK_MANAGERS: 15+ Prompts
- TALENTS: 3 Employees

**Lead Generation:**
- LIBRARIES: 64 Responsibilities
- TASK_MANAGERS: 12 Task Templates, 82 Step Templates
- TALENTS: 11 Employees

**Design:**
- LIBRARIES: Design-specific Objects, Tools
- TASK_MANAGERS: Design workflows
- TALENTS: 9 Employees

---

## 🛠️ Technical Details

### Data Formats

**JSON** — primary format for structured data:
- Actions, Objects, Tools, Professions
- Task Templates, Project Templates
- Employee Profiles, Client Data

**Markdown** — documentation and descriptions:
- README files for each entity
- Guides and instructions
- Changelog and reports

**CSV** — Master Lists for cataloging:
- Libraries_Master_List.csv
- Taxonomy_Master_List.csv
- PMT_Master_List.csv

**YAML** — Workflow definitions:
- n8n workflow configurations
- Automation pipelines

### Naming Conventions

**Files:**
```
{ENTITY}_{Type}_{Name}_{Version}.{ext}
Examples:
- LIBRARIES_Action_Create_v1.json
- TASK_MANAGERS_Task_Task-Template-007.json
- TALENTS_Employee_Artemchuk_Nikolay_Profile.md
```

**ID Formats:**
```
{ISO_CODE}-{###}
Examples:
- ACT-001 (Action)
- TSK-001 (Task)
- PRF-001 (Profession)
- PMT-001 (Prompt)
```

---

## 📚 Additional Resources

### Entity Documentation
- [LIBRARIES/README.md](LIBRARIES/README.md) — Complete libraries documentation
- [TASK_MANAGERS/README.md](TASK_MANAGERS/README.md) — Operations documentation
- [TALENTS/README.md](TALENTS/README.md) — Talent documentation
- [PROMPTS/README.md](PROMPTS/README.md) — Prompts documentation
- [TAXONOMY/README.md](TAXONOMY/README.md) — Taxonomy documentation

### Indexes and Master Lists
- [ENTITIES_MASTER_LIST.csv](ENTITIES_MASTER_LIST.csv) — Complete catalog of all entities
- [TASK_MANAGERS/INDEX.md](TASK_MANAGERS/INDEX.md) — Index of all templates
- [LIBRARIES/LBS_FOLDER_MASTER.md](LIBRARIES/LBS_FOLDER_MASTER.md) — Libraries master list

### Migration and History
- [FINAL_MIGRATION_SUMMARY_2025-11-17.md](FINAL_MIGRATION_SUMMARY_2025-11-17.md) — Migration history
- [ARCHITECTURE_UPDATE_PLAN.md](ARCHITECTURE_UPDATE_PLAN.md) — Update plans

---

## 🔄 GitHub Sync

This repository automatically syncs from Dropbox every 24 hours.

**Schedule:** Daily at 2:00 AM UTC

**Process:**
1. GitHub Actions runs on schedule
2. Connects to Dropbox via API
3. Scans `/ENTITIES` folder
4. Compares with current git repository
5. Downloads new and modified files
6. Removes deleted files
7. Generates changelog
8. Commits and pushes changes

**Manual Trigger:** Can be triggered manually via GitHub Actions → "Run workflow"

---

## 🎓 Usage Examples

### Example 1: Creating a Task

**Task:** Create a job posting for Frontend Developer

1. **Find Action:** `LIBRARIES/Responsibilities/Actions/` → "Create"
2. **Find Object:** `LIBRARIES/Responsibilities/Objects/` → "Job Posting"
3. **Find Template:** `TASK_MANAGERS/TSM-003_Task_Templates/` → Task-Template-007.json
4. **Use Template:** Follow steps from Step Templates
5. **Create Job:** `JOBS/Job_Postings/` → New file with requirements

### Example 2: Finding Talent

**Task:** Find Frontend Developer with React skills

1. **Define Requirements:** 
   - Profession: "Frontend Developer" (PRF-001)
   - Skills: ["React"] (SKL-030)
   - Tools: ["VS Code"] (TOL-045)

2. **Search in TALENTS:**
   - `TALENTS/Employees/` → Filter by Profession
   - Check Skills in profiles
   - Check Tool Proficiency

3. **Match:**
   - Use Skills matrix for matching
   - Check Availability
   - Check Performance metrics

### Example 3: Video Processing

**Task:** Process video and extract tasks

1. **Use Prompt:** PMT-004 (Video Transcription)
2. **Process:** Video is transcribed
3. **Extract Entities:** Actions, Objects, Tasks from transcription
4. **Update LIBRARIES:** New Actions/Objects added
5. **Create Tasks:** In TASK_MANAGERS based on extracted data
6. **Update TAXONOMY:** New IDs assigned

---

## 🚀 Future Development

### Planned Improvements

- **PostgreSQL Integration** — migrate data to database
- **API Gateway** — single access point for all entities
- **Real-time Sync** — real-time synchronization
- **Advanced Analytics** — enhanced analytics and reporting
- **Mobile App** — mobile app for access

### Current Projects

- **Taxonomy Standardization** — standardizing all ID systems
- **Workflow Automation** — automation through n8n
- **Skills Development** — developing skills system
- **Client Integration** — integration with CRM systems

---

## 📞 Contact & Support

**System Owner:** AI & Automation Department  
**Architecture:** Framework Architecture Team  
**Issues:** Report to system administrators

---

## 📝 License & Status

**Status:** Active Development  
**Version:** 2.0  
**Last Updated:** November 2025

---

**🎉 Welcome to the ENTITIES World!**

This system is a living organism that constantly evolves and improves. Each entity is connected to others, creating a powerful ecosystem for knowledge and operations management.

**Start by exploring LIBRARIES** — this is the foundation of the entire system. Then move to TASK_MANAGERS to understand processes, and continue to other entities as needed.

**Happy exploring! 🚀**
