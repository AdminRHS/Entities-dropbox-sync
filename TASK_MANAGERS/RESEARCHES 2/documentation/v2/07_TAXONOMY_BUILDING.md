# RESEARCHES 2 - Taxonomy Building Guide

**Version:** 2.0
**Generated:** 2025-12-04
**Purpose:** Complete guide to building and maintaining the taxonomy system
**Audience:** All users - taxonomy builders, integrators, developers

---

## 📖 Table of Contents

1. [Understanding Taxonomy](#understanding-taxonomy)
2. [The 7 Entity Types](#the-7-entity-types)
3. [ID Assignment System](#id-assignment-system)
4. [JSON File Templates](#json-file-templates)
5. [Cross-Referencing Guide](#cross-referencing-guide)
6. [Quality Standards](#quality-standards)
7. [Common Patterns](#common-patterns)
8. [Best Practices](#best-practices)

---

## Understanding Taxonomy

### What is Taxonomy?

**Taxonomy** is a systematic classification system that organizes knowledge into hierarchical categories with standardized naming, identification, and relationship structures.

In the RESEARCHES 2 system, taxonomy provides:
- **Standardized entity types** (7 core types)
- **Unique identification** (ID format system)
- **Relationship mapping** (cross-references)
- **Searchable structure** (JSON-based)
- **Scalable organization** (grows with knowledge)

### Why 7 Entity Types?

The 7 entity types cover all aspects of digital work:

1. **TOOLS** - What you use (software, platforms, services)
2. **WORKFLOWS** - How you do it (processes, procedures)
3. **OBJECTS** - What you create/manipulate (files, data, artifacts)
4. **ACTIONS** - What you do (operations, tasks, verbs)
5. **PROFESSIONS** - Who does it (roles, job titles)
6. **SKILLS** - What capabilities needed (competencies, expertise)
7. **DEPARTMENTS** - Where it happens (organizational units)

**These 7 types interconnect:**
```
DEPARTMENT employs → PROFESSION
PROFESSION requires → SKILL
SKILL enables → ACTION
ACTION uses → TOOL
TOOL creates → OBJECT
OBJECT used in → WORKFLOW
WORKFLOW performed by → PROFESSION
```

### How Entities Relate

**Example relationship chain:**
```
Development Department (DPT-DEV)
  └─ employs → Full Stack Developer (PRF-012)
      └─ requires → API Integration Skill (SKL-023)
          └─ enables → API Call Action (ACT-042)
              └─ uses → Claude API Tool (TOL-342)
                  └─ creates → API Response Object (OBJ-289)
                      └─ used in → Chat Interface Workflow (WRF-413)
                          └─ performed by → Full Stack Developer (PRF-012)
```

**This creates a knowledge graph** where:
- Every entity is connected
- Relationships are bidirectional
- Knowledge is discoverable
- Gaps are identifiable

---

## The 7 Entity Types

### 1. TOOLS (TOL-###)

**Definition:** Software, platforms, plugins, applications, services, or systems used to perform work.

**Characteristics:**
- Has a name (e.g., "Figma", "Claude API", "VS Code")
- Has a version or variant (e.g., "Figma v2024", "Claude Sonnet 4.5")
- Can be installed, accessed, or used
- Creates or manipulates objects
- Used within workflows

**Examples:**
- **TOL-042** - Claude API
- **TOL-089** - Postman (API testing tool)
- **TOL-158** - VS Code (code editor)
- **TOL-234** - Figma (design tool)
- **TOL-342** - GitHub Copilot (AI coding assistant)

**Subcategories:**
- **Software:** Desktop applications (Photoshop, Blender)
- **Platforms:** Web services (Notion, Airtable)
- **Plugins:** Extensions (VS Code extensions, Figma plugins)
- **APIs:** Web APIs (Claude API, OpenAI API)
- **Services:** Cloud services (AWS S3, Google Drive)
- **Frameworks:** Code frameworks (React, Django)
- **Libraries:** Code libraries (jQuery, TensorFlow)

**Key Properties:**
- Name
- Category/Subcategory
- Version
- Pricing model
- Features list
- Use cases
- Documentation URL
- Alternatives

**Relationships:**
- `creates_objects`: [OBJ-###, OBJ-###]
- `used_in_workflows`: [WRF-###, WRF-###]
- `requires_skills`: [SKL-###, SKL-###]
- `relevant_professions`: [PRF-###, PRF-###]
- `relevant_departments`: [DPT-###, DPT-###]
- `related_tools`: [TOL-###, TOL-###]
- `alternatives`: [TOL-###, TOL-###]

---

### 2. WORKFLOWS (WRF-###)

**Definition:** Multi-step processes with clear start and end points, involving multiple tools, actions, and objects.

**Characteristics:**
- Has sequential steps (Step 1 → Step 2 → Step 3)
- Has defined inputs and outputs
- Takes time to complete (duration)
- Can be repeated/reused
- Involves multiple tools and actions
- Creates or transforms objects

**Examples:**
- **WRF-008** - Design System Creation
- **WRF-042** - API Integration Flow
- **WRF-201** - Video Editing Workflow
- **WRF-412** - API Authentication Setup
- **WRF-413** - Building Chat Interface

**Subcategories:**
- **Creative:** Design, video editing, content creation
- **Technical:** Coding, API integration, deployment
- **Analytical:** Data analysis, research, testing
- **Administrative:** Project management, documentation
- **Collaborative:** Team workflows, review processes

**Key Properties:**
- Name
- Description
- Steps (numbered list)
- Duration estimate
- Complexity level (Beginner/Intermediate/Advanced)
- Prerequisites
- Expected outcome

**Relationships:**
- `uses_tools`: [TOL-###, TOL-###]
- `creates_objects`: [OBJ-###, OBJ-###]
- `includes_actions`: [ACT-###, ACT-###]
- `requires_skills`: [SKL-###, SKL-###]
- `performed_by`: [PRF-###, PRF-###]
- `relevant_departments`: [DPT-###, DPT-###]
- `prerequisite_workflows`: [WRF-###, WRF-###]
- `follow_up_workflows`: [WRF-###, WRF-###]

**Example Workflow Structure:**
```
WRF-413: Building Chat Interface

Steps:
1. Set up project structure (5 min)
2. Install Claude API SDK (5 min)
3. Configure authentication (10 min)
4. Create chat UI components (30 min)
5. Implement API integration (45 min)
6. Add streaming support (30 min)
7. Test and debug (20 min)

Duration: 2 hours 25 minutes
Complexity: Intermediate

Uses Tools:
- TOL-342 (Claude API)
- TOL-158 (VS Code)
- TOL-089 (Postman for testing)

Creates Objects:
- OBJ-289 (API Response)
- OBJ-290 (Chat Message)
- OBJ-345 (Chat Interface Component)

Requires Skills:
- SKL-023 (API Integration)
- SKL-034 (React/JavaScript)
- SKL-042 (Async Programming)
```

---

### 3. OBJECTS (OBJ-###)

**Definition:** Digital artifacts, files, data structures, or outputs that are created, manipulated, or consumed in workflows.

**Characteristics:**
- Has a format (JSON, PNG, PDF, etc.)
- Can be created by tools
- Can be stored/saved
- Has properties/metadata
- Used as input/output in workflows

**Examples:**
- **OBJ-015** - Design File (Figma file)
- **OBJ-023** - API Response (JSON)
- **OBJ-089** - Video Export (MP4)
- **OBJ-158** - Database Record
- **OBJ-289** - Chat Message Object

**Subcategories:**
- **Files:** Documents, images, videos, audio
- **Data Structures:** JSON, XML, database records
- **Code:** Source files, scripts, configurations
- **Artifacts:** Builds, packages, exports
- **Content:** Text, designs, graphics
- **Assets:** Images, icons, fonts

**Key Properties:**
- Name
- Type/Category
- File format
- Structure (if data)
- Properties/metadata
- Lifecycle (how created, modified, deleted)

**Relationships:**
- `created_by`: [TOL-###, TOL-###]
- `used_in`: [WRF-###, WRF-###]
- `consumed_by`: [TOL-###, WRF-###]
- `transforms_into`: [OBJ-###, OBJ-###]
- `contains`: [OBJ-###, OBJ-###]

**Example Object Structure:**
```
OBJ-289: API Response Object

Type: Data Structure
Format: JSON

Structure:
{
  "id": "msg_xxx",
  "type": "message",
  "role": "assistant",
  "content": [{"type": "text", "text": "..."}],
  "model": "claude-3-5-sonnet-20241022",
  "usage": {
    "input_tokens": 100,
    "output_tokens": 200
  }
}

Created By:
- TOL-342 (Claude API)

Used In:
- WRF-413 (Building Chat Interface)
- WRF-414 (Implementing Streaming)

Properties:
- id: Unique message identifier
- role: "assistant" or "user"
- content: Array of content blocks
- usage: Token consumption metrics

Lifecycle:
1. Request sent to Claude API
2. API processes request
3. Response generated (this object)
4. Response consumed by frontend
5. Logged for analytics (optional)
6. Temporary storage (not persisted)
```

---

### 4. ACTIONS (ACT-###)

**Definition:** Atomic operations, tasks, or verbs that describe what can be done. Actions are the smallest unit of work.

**Characteristics:**
- Single operation (not multi-step)
- Has a verb form ("Create", "Edit", "Delete", "Export")
- Can be performed by tools
- Part of larger workflows
- Categorized into 7 types

**7 Action Categories:**

**Category A: Interface Creation & Design**
- Creating UI components
- Designing layouts
- Building mockups
- Prototyping interfaces

Examples:
- ACT-001: Create input field
- ACT-002: Design button component
- ACT-003: Build navigation menu

**Category B: Content Generation**
- Generating text
- Creating images
- Producing videos
- Writing code

Examples:
- ACT-010: Generate API response
- ACT-011: Create blog post
- ACT-012: Write code snippet

**Category C: Design Refinement**
- Editing designs
- Adjusting layouts
- Refining styles
- Iterating on concepts

Examples:
- ACT-020: Adjust spacing
- ACT-021: Change color scheme
- ACT-022: Refine typography

**Category D: Asset Management**
- Organizing files
- Managing resources
- Storing assets
- Version control

Examples:
- ACT-030: Upload file
- ACT-031: Create folder
- ACT-032: Tag asset

**Category E: Collaboration**
- Sharing work
- Commenting
- Reviewing
- Communicating

Examples:
- ACT-040: Share design
- ACT-041: Add comment
- ACT-042: Request review

**Category F: Analysis & Research**
- Analyzing data
- Researching topics
- Testing features
- Evaluating options

Examples:
- ACT-050: Analyze metrics
- ACT-051: Research competitor
- ACT-052: Test API endpoint

**Category G: Automation & Integration**
- Automating tasks
- Integrating systems
- Connecting tools
- Streamlining processes

Examples:
- ACT-060: Automate deployment
- ACT-061: Integrate API
- ACT-062: Connect webhook

**Key Properties:**
- Name (verb + object)
- Category (A-G)
- Description
- Typical duration
- Complexity

**Relationships:**
- `performed_with`: [TOL-###, TOL-###]
- `part_of`: [WRF-###, WRF-###]
- `creates`: [OBJ-###, OBJ-###]
- `requires`: [SKL-###, SKL-###]

---

### 5. PROFESSIONS (PRF-###)

**Definition:** Job roles, titles, or positions that perform work using tools, workflows, and skills.

**Characteristics:**
- Has a job title
- Requires specific skills
- Uses specific tools
- Performs specific workflows
- Belongs to departments

**Examples:**
- **PRF-003** - UI Designer
- **PRF-008** - Backend Developer
- **PRF-012** - Full Stack Developer
- **PRF-015** - AI Integration Engineer
- **PRF-023** - DevOps Engineer

**Subcategories:**
- **Design:** UI Designer, Graphic Designer, UX Researcher
- **Development:** Frontend, Backend, Full Stack, Mobile
- **AI/ML:** ML Engineer, Data Scientist, AI Researcher
- **Operations:** DevOps, SysAdmin, Cloud Engineer
- **Product:** Product Manager, Product Designer
- **Content:** Content Writer, Video Editor, Copywriter
- **Marketing:** Marketing Manager, SEO Specialist
- **Management:** Team Lead, Project Manager, Director

**Key Properties:**
- Title
- Description
- Seniority level (Junior/Mid/Senior/Lead)
- Department
- Typical responsibilities

**Relationships:**
- `requires_skills`: [SKL-###, SKL-###]
- `uses_tools`: [TOL-###, TOL-###]
- `performs_workflows`: [WRF-###, WRF-###]
- `performs_actions`: [ACT-###, ACT-###]
- `belongs_to_department`: [DPT-###]
- `related_professions`: [PRF-###, PRF-###]

**Example:**
```
PRF-012: Full Stack Developer

Description: Develops both frontend and backend applications

Seniority: Mid to Senior level

Requires Skills:
- SKL-023 (API Integration)
- SKL-034 (JavaScript/TypeScript)
- SKL-042 (Async Programming)
- SKL-089 (React Framework)
- SKL-134 (Node.js)

Uses Tools:
- TOL-158 (VS Code)
- TOL-342 (GitHub Copilot)
- TOL-089 (Postman)
- TOL-234 (Git)

Performs Workflows:
- WRF-413 (Building Chat Interface)
- WRF-415 (Function Calling Setup)
- WRF-419 (Deploying to Production)

Belongs To:
- DPT-DEV (Development Department)

Related Professions:
- PRF-008 (Backend Developer)
- PRF-015 (AI Integration Engineer)
```

---

### 6. SKILLS (SKL-###)

**Definition:** Competencies, abilities, or expertise required to use tools, perform workflows, and execute actions.

**Characteristics:**
- Represents knowledge or ability
- Can be learned/acquired
- Has proficiency levels
- Required by professions
- Enables use of tools

**Examples:**
- **SKL-008** - Visual Design
- **SKL-012** - JavaScript Programming
- **SKL-023** - API Integration
- **SKL-034** - Prompt Engineering
- **SKL-042** - Async Programming

**Subcategories:**
- **Technical:** Programming, API integration, database design
- **Design:** Visual design, UX design, prototyping
- **Creative:** Video editing, content writing, illustration
- **Analytical:** Data analysis, research, testing
- **Soft:** Communication, leadership, time management
- **Domain:** AI/ML knowledge, cloud architecture, security

**Proficiency Levels:**
- **Beginner:** Basic understanding, can follow tutorials
- **Intermediate:** Can work independently on standard tasks
- **Advanced:** Can solve complex problems, optimize solutions
- **Expert:** Can teach others, innovate, architect systems

**Key Properties:**
- Name
- Description
- Category
- Typical learning time
- Prerequisites

**Relationships:**
- `required_by`: [PRF-###, PRF-###]
- `enables_use_of`: [TOL-###, TOL-###]
- `required_for`: [WRF-###, WRF-###]
- `prerequisite_skills`: [SKL-###, SKL-###]
- `related_skills`: [SKL-###, SKL-###]

**Example:**
```
SKL-023: API Integration

Description: Ability to integrate external APIs into applications

Category: Technical - Backend Development

Proficiency Levels:
- Beginner: Can call simple REST APIs
- Intermediate: Can handle authentication, error handling, rate limiting
- Advanced: Can design API abstractions, implement retry logic, optimize performance
- Expert: Can architect multi-API systems, handle complex integrations

Typical Learning Time: 2-4 weeks (intermediate level)

Prerequisites:
- SKL-034 (JavaScript/TypeScript)
- SKL-042 (Async Programming)
- SKL-089 (HTTP Protocol Understanding)

Required By:
- PRF-012 (Full Stack Developer)
- PRF-015 (AI Integration Engineer)
- PRF-008 (Backend Developer)

Enables Use Of:
- TOL-342 (Claude API)
- TOL-089 (Postman)
- TOL-234 (Axios HTTP client)

Required For:
- WRF-413 (Building Chat Interface)
- WRF-415 (Function Calling Setup)
```

---

### 7. DEPARTMENTS (DPT-###)

**Definition:** Organizational units, teams, or divisions within a company or organization.

**Characteristics:**
- Represents organizational structure
- Employs professions
- Has specific focus/goals
- Uses specific tools and workflows
- Has 3-letter code

**Standard Department Codes:**
- **AID** - AI Department
- **DEV** - Development
- **VID** - Video/Content Production
- **SMM** - Social Media Marketing
- **DGN** - Design
- **MKT** - Marketing
- **HRM** - Human Resources
- **SLS** - Sales
- **LG** - Legal (sometimes LGL)
- **OPS** - Operations
- **FIN** - Finance
- **LGL** - Legal

**Examples:**
- **DPT-DEV** - Development Department
- **DPT-DGN** - Design Department
- **DPT-AID** - AI Department
- **DPT-MKT** - Marketing Department

**Key Properties:**
- Name
- Code (3 letters)
- Description
- Typical size (team members)
- Primary focus

**Relationships:**
- `employs`: [PRF-###, PRF-###]
- `uses_tools`: [TOL-###, TOL-###]
- `performs_workflows`: [WRF-###, WRF-###]
- `collaborates_with`: [DPT-###, DPT-###]

**Example:**
```
DPT-DEV: Development Department

Code: DEV

Description: Responsible for building and maintaining software applications

Typical Size: 10-50 engineers

Primary Focus:
- Application development
- API integrations
- Code quality and testing
- Deployment and operations

Employs:
- PRF-012 (Full Stack Developer)
- PRF-008 (Backend Developer)
- PRF-015 (AI Integration Engineer)
- PRF-023 (DevOps Engineer)

Uses Tools:
- TOL-158 (VS Code)
- TOL-342 (Claude API)
- TOL-234 (Git)
- TOL-089 (Postman)

Performs Workflows:
- WRF-413 (Building Chat Interface)
- WRF-419 (Deploying to Production)
- WRF-089 (Code Review Process)

Collaborates With:
- DPT-DGN (Design - for UI/UX)
- DPT-AID (AI - for AI integrations)
- DPT-OPS (Operations - for deployment)
```

---

## ID Assignment System

### ID Format Rules

**Standard Format:**
```
[PREFIX]-[NUMBER]
```

**Components:**
- **PREFIX:** 3-letter code identifying entity type
- **SEPARATOR:** Hyphen (-)
- **NUMBER:** 3-digit sequential number, zero-padded

**Valid Examples:**
```
TOL-001  ✅ (Tool #1)
WRF-042  ✅ (Workflow #42)
OBJ-158  ✅ (Object #158)
ACT-234  ✅ (Action #234)
PRF-012  ✅ (Profession #12)
SKL-089  ✅ (Skill #89)
DPT-DEV  ✅ (Department with code)
```

**Invalid Examples:**
```
TOL-1    ❌ (number not zero-padded)
TOL001   ❌ (missing hyphen)
TOOL-001 ❌ (prefix too long)
TO-001   ❌ (prefix too short)
TOL-1234 ❌ (number too long)
tol-001  ❌ (lowercase prefix)
```

### Entity Type Prefixes

| Entity Type | Prefix | Example | Range |
|-------------|--------|---------|-------|
| Tools | TOL | TOL-042 | TOL-001 to TOL-999 |
| Workflows | WRF | WRF-158 | WRF-001 to WRF-999 |
| Objects | OBJ | OBJ-023 | OBJ-001 to OBJ-999 |
| Actions | ACT | ACT-089 | ACT-001 to ACT-999 |
| Professions | PRF | PRF-012 | PRF-001 to PRF-999 |
| Skills | SKL | SKL-034 | SKL-001 to SKL-999 |
| Departments | DPT | DPT-DEV | DPT-[CODE] |

**Note:** Departments use 3-letter codes instead of numbers (DPT-DEV, DPT-AID, etc.)

### ID Assignment Process

**Step 1: Determine Entity Type**
- Is it a tool? → TOL-###
- Is it a workflow? → WRF-###
- Is it an object? → OBJ-###
- Is it an action? → ACT-###
- Is it a profession? → PRF-###
- Is it a skill? → SKL-###
- Is it a department? → DPT-[CODE]

**Step 2: Find Next Available ID**

**Manual Method:**
```bash
# List existing IDs
ls ENTITIES/LIBRARIES/TOOLS/ | grep -o "TOL-[0-9]*" | sort | tail -1

# Output: TOL-341
# Next ID: TOL-342
```

**Script Method:**
```bash
# Use ID generator
python scripts/get_next_id.py TOL

# Output: TOL-342
```

**Step 3: Verify ID Uniqueness**
```bash
# Check if ID already exists
find ENTITIES/LIBRARIES/ -name "TOL-342.json"

# If no output: ID is available ✅
# If file found: ID taken, use next ❌
```

**Step 4: Assign ID**
- Use in filename: `TOL-342.json`
- Use in JSON: `"entity_id": "TOL-342"`
- **IMPORTANT:** Filename and entity_id MUST match

### ID Numbering Rules

**Sequential Assignment:**
- Always use next available number
- No gaps in numbering
- Start from 001, increment by 1

**Examples:**
```
Existing: TOL-001, TOL-002, TOL-003
Next: TOL-004 ✅

Existing: TOL-001, TOL-002, TOL-004
Next: TOL-005 ✅ (skip gap at 003)
```

**No Reuse:**
- Once assigned, never reuse
- Even if entity deleted/deprecated
- Maintain historical record

**Exception - Departments:**
- Use semantic codes (DPT-DEV, DPT-AID)
- Not sequential numbers
- Codes defined by organization

### ID Registry

**Maintain registry file:**
```
ENTITIES/LIBRARIES/[TYPE]/registry.json
```

**Example registry:**
```json
{
  "entity_type": "Tool",
  "prefix": "TOL",
  "last_assigned": "TOL-342",
  "next_available": "TOL-343",
  "total_count": 342,
  "retired_ids": ["TOL-089"],
  "last_updated": "2025-12-04"
}
```

---

## JSON File Templates

### Tool Template (TOL-###)

**File:** `ENTITIES/LIBRARIES/TOOLS/TOL-342.json`

```json
{
  "entity_id": "TOL-342",
  "name": "Claude API (Sonnet 4.5)",
  "type": "Tool",
  "category": "AI Platform",
  "subcategory": "Large Language Model API",

  "description": "Anthropic's Claude API with Sonnet 4.5 model - advanced language model for building AI applications with 400K context window",

  "features": [
    "400K context window for processing large documents",
    "Streaming responses for real-time output",
    "Function calling for tool integration",
    "Vision capabilities for image analysis",
    "JSON mode for structured output",
    "Extended thinking for complex reasoning"
  ],

  "use_cases": [
    "Building conversational AI chatbots",
    "Code generation and analysis",
    "Document processing and summarization",
    "Content creation and editing",
    "Research and data analysis",
    "Automated customer support"
  ],

  "pricing": {
    "model": "Pay-per-use",
    "tiers": [
      {
        "name": "Sonnet 4.5",
        "input_cost": "$3 per million tokens",
        "output_cost": "$15 per million tokens",
        "context_window": "400K tokens"
      }
    ],
    "free_tier": {
      "available": true,
      "credits": "$5 initial credit"
    }
  },

  "technical_specs": {
    "api_version": "2024-12-01",
    "rate_limits": {
      "requests_per_minute": 60,
      "tokens_per_minute": 100000
    },
    "supported_formats": ["text", "json", "markdown"],
    "authentication": "API Key"
  },

  "creates_objects": ["OBJ-289", "OBJ-290", "OBJ-291"],
  "used_in_workflows": ["WRF-412", "WRF-413", "WRF-414", "WRF-415"],
  "requires_skills": ["SKL-023", "SKL-034", "SKL-042", "SKL-089"],
  "relevant_professions": ["PRF-012", "PRF-015", "PRF-008"],
  "relevant_departments": ["DPT-DEV", "DPT-AID", "DPT-OPS"],

  "related_tools": ["TOL-042", "TOL-089", "TOL-134"],
  "alternatives": ["TOL-089", "TOL-199"],
  "integrations": ["TOL-158", "TOL-234"],

  "metadata": {
    "source_video": "Video_024",
    "date_added": "2025-12-04",
    "last_updated": "2025-12-04",
    "added_by": "John Doe",
    "status": "Active",
    "documentation_url": "https://docs.anthropic.com/claude/reference/",
    "version": "Sonnet 4.5",
    "provider": "Anthropic"
  },

  "tags": ["AI", "LLM", "API", "Claude", "Anthropic", "NLP", "Machine Learning", "Generative AI"]
}
```

---

### Workflow Template (WRF-###)

**File:** `ENTITIES/LIBRARIES/WORKFLOWS/WRF-413.json`

```json
{
  "entity_id": "WRF-413",
  "name": "Building Chat Interface with Claude API",
  "type": "Workflow",
  "category": "Development",
  "subcategory": "AI Integration",

  "description": "Complete workflow for building a conversational AI chat interface using Claude API with streaming support",

  "steps": [
    {
      "number": 1,
      "title": "Set up project structure",
      "description": "Initialize React project with TypeScript",
      "duration": "5 minutes",
      "tools_used": ["TOL-158"],
      "actions": ["ACT-001", "ACT-002"]
    },
    {
      "number": 2,
      "title": "Install Claude API SDK",
      "description": "Install @anthropic-ai/sdk package",
      "duration": "5 minutes",
      "tools_used": ["TOL-158"],
      "actions": ["ACT-010"]
    },
    {
      "number": 3,
      "title": "Configure authentication",
      "description": "Set up API key and environment variables",
      "duration": "10 minutes",
      "tools_used": ["TOL-342", "TOL-354"],
      "actions": ["ACT-020", "ACT-021"],
      "creates_objects": ["OBJ-295"]
    },
    {
      "number": 4,
      "title": "Create chat UI components",
      "description": "Build message bubbles, input field, and chat container",
      "duration": "30 minutes",
      "tools_used": ["TOL-158", "TOL-234"],
      "actions": ["ACT-001", "ACT-002", "ACT-003"],
      "creates_objects": ["OBJ-345"]
    },
    {
      "number": 5,
      "title": "Implement API integration",
      "description": "Connect to Claude API and handle responses",
      "duration": "45 minutes",
      "tools_used": ["TOL-342", "TOL-089"],
      "actions": ["ACT-061", "ACT-062"],
      "creates_objects": ["OBJ-289", "OBJ-290"]
    },
    {
      "number": 6,
      "title": "Add streaming support",
      "description": "Implement real-time streaming responses",
      "duration": "30 minutes",
      "tools_used": ["TOL-342", "TOL-353"],
      "actions": ["ACT-060", "ACT-061"],
      "creates_objects": ["OBJ-294"]
    },
    {
      "number": 7,
      "title": "Test and debug",
      "description": "Test all functionality and fix issues",
      "duration": "20 minutes",
      "tools_used": ["TOL-089", "TOL-158"],
      "actions": ["ACT-052", "ACT-053"]
    }
  ],

  "total_duration": "145 minutes",
  "complexity": "Intermediate",
  "difficulty_level": 3,

  "prerequisites": {
    "skills": ["SKL-023", "SKL-034", "SKL-042"],
    "tools": ["TOL-158", "TOL-342"],
    "workflows": ["WRF-412"],
    "knowledge": ["React basics", "API fundamentals", "Async programming"]
  },

  "expected_outcome": {
    "description": "Fully functional chat interface with Claude API integration and streaming support",
    "deliverables": ["Working chat application", "API integration code", "Test cases"],
    "quality_criteria": ["Messages display correctly", "Streaming works smoothly", "Error handling robust"]
  },

  "uses_tools": ["TOL-342", "TOL-158", "TOL-089", "TOL-234", "TOL-353", "TOL-354"],
  "creates_objects": ["OBJ-289", "OBJ-290", "OBJ-294", "OBJ-295", "OBJ-345"],
  "includes_actions": ["ACT-001", "ACT-002", "ACT-003", "ACT-010", "ACT-020", "ACT-021", "ACT-060", "ACT-061", "ACT-062", "ACT-052", "ACT-053"],
  "requires_skills": ["SKL-023", "SKL-034", "SKL-042", "SKL-089"],
  "performed_by": ["PRF-012", "PRF-015"],
  "relevant_departments": ["DPT-DEV", "DPT-AID"],

  "prerequisite_workflows": ["WRF-412"],
  "follow_up_workflows": ["WRF-414", "WRF-415", "WRF-419"],
  "related_workflows": ["WRF-201", "WRF-089"],

  "metadata": {
    "source_video": "Video_024",
    "date_added": "2025-12-04",
    "last_updated": "2025-12-04",
    "added_by": "John Doe",
    "status": "Active",
    "version": "1.0",
    "last_tested": "2025-12-04"
  },

  "tags": ["AI", "Chat", "Claude", "API Integration", "React", "Streaming", "Real-time"]
}
```

---

### Object Template (OBJ-###)

**File:** `ENTITIES/LIBRARIES/OBJECTS/OBJ-289.json`

```json
{
  "entity_id": "OBJ-289",
  "name": "Claude API Response",
  "type": "Object",
  "category": "Data Structure",
  "subcategory": "JSON Object",

  "description": "JSON response object returned by Claude API containing the assistant's message and metadata",

  "format": "JSON",
  "file_extension": null,
  "mime_type": "application/json",

  "structure": {
    "id": {
      "type": "string",
      "description": "Unique message identifier",
      "example": "msg_01XYZ123abc",
      "required": true
    },
    "type": {
      "type": "string",
      "description": "Always 'message' for message responses",
      "example": "message",
      "required": true
    },
    "role": {
      "type": "string",
      "description": "Role of the message sender",
      "example": "assistant",
      "enum": ["assistant", "user"],
      "required": true
    },
    "content": {
      "type": "array",
      "description": "Array of content blocks",
      "example": [{"type": "text", "text": "Hello! How can I help you?"}],
      "required": true
    },
    "model": {
      "type": "string",
      "description": "Model version used",
      "example": "claude-3-5-sonnet-20241022",
      "required": true
    },
    "usage": {
      "type": "object",
      "description": "Token usage metrics",
      "properties": {
        "input_tokens": "number",
        "output_tokens": "number"
      },
      "required": true
    }
  },

  "example": {
    "id": "msg_01XYZ123abc",
    "type": "message",
    "role": "assistant",
    "content": [
      {
        "type": "text",
        "text": "Hello! I'm Claude, an AI assistant. How can I help you today?"
      }
    ],
    "model": "claude-3-5-sonnet-20241022",
    "usage": {
      "input_tokens": 12,
      "output_tokens": 23
    },
    "stop_reason": "end_turn"
  },

  "properties": {
    "size_range": "500 bytes - 50 KB typical",
    "encoding": "UTF-8",
    "compression": "None",
    "persistence": "Temporary (not stored by API)",
    "mutability": "Immutable once created"
  },

  "lifecycle": {
    "creation": "Generated by Claude API on each request",
    "usage": "Consumed by frontend application for display",
    "storage": "Optional logging/analytics",
    "deletion": "Automatic (ephemeral)",
    "retention": "N/A (not persisted by API)"
  },

  "created_by": ["TOL-342"],
  "used_in": ["WRF-413", "WRF-414", "WRF-415"],
  "consumed_by": ["TOL-158", "TOL-234"],
  "transforms_into": ["OBJ-290"],
  "related_objects": ["OBJ-290", "OBJ-291", "OBJ-294"],

  "metadata": {
    "source_video": "Video_024",
    "date_added": "2025-12-04",
    "last_updated": "2025-12-04",
    "added_by": "John Doe",
    "status": "Active",
    "schema_version": "1.0"
  },

  "tags": ["API", "Response", "JSON", "Claude", "Data Structure", "Message"]
}
```

---

### Additional Templates

**Action Template, Profession Template, Skill Template, Department Template available in:**
```
ENTITIES/TASK_MANAGERS/RESEARCHES 2/templates/JSON_Entity_Templates/
```

Or see [v1/02_ALL_FILES_INVENTORY.md](../v1/02_ALL_FILES_INVENTORY.md) for complete template listing.

---

## Cross-Referencing Guide

### Bidirectional Linking Rules

**Core Principle:** If Entity A references Entity B, then Entity B MUST reference Entity A back.

**Example:**
```json
// In TOL-342.json (Claude API)
{
  "entity_id": "TOL-342",
  "creates_objects": ["OBJ-289"]  // Tool → Object
}

// In OBJ-289.json (API Response)
{
  "entity_id": "OBJ-289",
  "created_by": ["TOL-342"]  // Object → Tool (REQUIRED)
}
```

### Cross-Reference Field Mapping

**Tool ↔ Object:**
```
Tool: "creates_objects": ["OBJ-###"]
Object: "created_by": ["TOL-###"]
```

**Tool ↔ Workflow:**
```
Tool: "used_in_workflows": ["WRF-###"]
Workflow: "uses_tools": ["TOL-###"]
```

**Workflow ↔ Object:**
```
Workflow: "creates_objects": ["OBJ-###"]
Object: "used_in": ["WRF-###"]
```

**Profession ↔ Skill:**
```
Profession: "requires_skills": ["SKL-###"]
Skill: "required_by": ["PRF-###"]
```

**Profession ↔ Tool:**
```
Profession: "uses_tools": ["TOL-###"]
Tool: "relevant_professions": ["PRF-###"]
```

**Workflow ↔ Action:**
```
Workflow: "includes_actions": ["ACT-###"]
Action: "part_of": ["WRF-###"]
```

### Validation Checklist

Before finalizing any JSON file:

- [ ] All outbound references have inbound matches
- [ ] All inbound references have outbound matches
- [ ] No orphaned entities (referenced but not existing)
- [ ] No broken references (invalid IDs)
- [ ] Cross-reference arrays not empty (unless truly standalone)

### Cross-Reference Example

**Complete bidirectional chain:**

```
TOL-342 (Claude API)
  ↓ creates_objects
OBJ-289 (API Response)
  ↓ created_by (back to TOL-342) ✅
  ↓ used_in
WRF-413 (Building Chat Interface)
  ↓ uses_tools (back to TOL-342) ✅
  ↓ creates_objects (back to OBJ-289) ✅
  ↓ performed_by
PRF-012 (Full Stack Developer)
  ↓ uses_tools (back to TOL-342) ✅
  ↓ performs_workflows (back to WRF-413) ✅
  ↓ requires_skills
SKL-023 (API Integration)
  ↓ required_by (back to PRF-012) ✅
  ↓ enables_use_of (back to TOL-342) ✅
```

**All links bidirectional ✅**

---

## Quality Standards

### Minimum Requirements

**Per Video Processing:**
- Minimum 37 entities extracted
- All 7 entity categories represented
- At least 1 Tool
- At least 1 Workflow
- At least 3 Actions across categories

**Per JSON File:**
- Valid JSON syntax (no parse errors)
- entity_id matches filename
- All required fields present
- At least 1 cross-reference (unless truly standalone)
- Metadata section complete

**Per Entity:**
- Clear, descriptive name
- Complete description (not placeholder like "TBD")
- Appropriate category/subcategory
- Proper ID format
- At least 2 relationships documented

### Quality Checklist

**Before committing new entities:**

**Completeness:**
- [ ] Name is clear and specific
- [ ] Description is detailed (2+ sentences)
- [ ] Category correctly assigned
- [ ] All relevant properties filled
- [ ] No placeholder text (TBD, [description], etc.)

**Relationships:**
- [ ] At least 2 cross-references
- [ ] All references bidirectional
- [ ] All referenced IDs exist
- [ ] Relationships logical and accurate

**Metadata:**
- [ ] source_video documented
- [ ] date_added recorded
- [ ] added_by recorded
- [ ] status set ("Active")
- [ ] Tags present (3+ tags)

**Technical:**
- [ ] JSON syntax valid
- [ ] ID format correct
- [ ] Filename matches entity_id
- [ ] Saved in correct folder
- [ ] File permissions correct

### Quality Metrics

**Entity Quality Score (0-100):**

- **Name clarity:** 10 points
- **Description completeness:** 15 points
- **Properties filled:** 15 points
- **Cross-references:** 20 points (10 per direction)
- **Metadata complete:** 10 points
- **Tags present:** 5 points
- **Examples provided:** 10 points
- **Documentation links:** 5 points
- **Use cases listed:** 10 points

**Target Score:** 80+ (Excellent quality)

**Acceptable:** 60-79 (Good quality, minor improvements needed)

**Needs Work:** <60 (Incomplete, requires enhancement)

---

## Common Patterns

### Tool-Object-Workflow Pattern

**Most common pattern in system:**

```
Tool creates Object
Object used in Workflow
Workflow uses Tool

Example:
Figma (TOL-234)
  → creates → Design File (OBJ-015)
      → used in → Design System Creation (WRF-008)
          → uses → Figma (TOL-234)
```

### Profession-Skill-Tool Chain

**Employment and capability pattern:**

```
Profession requires Skill
Skill enables Tool
Tool used by Profession

Example:
Full Stack Developer (PRF-012)
  → requires → API Integration (SKL-023)
      → enables → Claude API (TOL-342)
          → used by → Full Stack Developer (PRF-012)
```

### Action Hierarchy Pattern

**Granular to comprehensive:**

```
Multiple Actions combine into Workflow

Example:
ACT-001 (Create input field)
ACT-002 (Create button)
ACT-003 (Create container)
  → combine into → WRF-413 (Building Chat Interface)
```

---

## Best Practices

### Naming Conventions

**Tools:**
- Use official product name: "Figma" not "figma"
- Include version if relevant: "Claude API (Sonnet 4.5)"
- Be specific: "VS Code" not "Code Editor"

**Workflows:**
- Use gerund form: "Building", "Creating", "Implementing"
- Be descriptive: "Building Chat Interface with Streaming" not "Chat Setup"
- Include key feature: "API Authentication Setup" not "Auth"

**Objects:**
- Use noun form: "API Response" not "Respond"
- Include type: "Chat Message Object" not "Message"
- Be specific: "Figma Design File" not "File"

**Actions:**
- Use verb+object: "Create component" not "Create"
- Be atomic: "Save file" not "Save and close file"
- Be clear: "Export to PDF" not "Export"

### Description Writing

**Good descriptions:**
- 2-3 sentences minimum
- Explain what, why, how
- Provide context
- Include typical use cases

**Example - Good:**
```
"Anthropic's Claude API with Sonnet 4.5 model provides advanced language
model capabilities for building AI applications. With a 400K context window
and streaming support, it's ideal for chatbots, document processing, and
code generation tasks. The API offers function calling, vision capabilities,
and JSON mode for structured output."
```

**Example - Bad:**
```
"AI API for building apps."
```

### Property Guidelines

**Fill all relevant properties:**
- Don't leave arrays empty unless truly no relationships
- Provide examples where helpful
- Include technical specs for tools
- Document typical durations for workflows
- List prerequisites clearly

**Use structured data:**
```json
// Good - structured pricing
"pricing": {
  "model": "Subscription",
  "tiers": [{"name": "Pro", "cost": "$20/month"}]
}

// Bad - unstructured
"pricing": "Twenty dollars per month for pro"
```

### Maintenance

**Regular updates:**
- Review entities quarterly
- Update when tool versions change
- Deprecate obsolete entities
- Add new relationships as discovered

**Version control:**
- Update `last_updated` field
- Document changes in commit message
- Keep old versions if major changes

**Deprecation process:**
```json
{
  "status": "Deprecated",
  "deprecated_date": "2025-12-01",
  "deprecated_reason": "Replaced by TOL-456",
  "replacement": "TOL-456"
}
```

---

## Summary

**Key Takeaways:**

1. **7 Entity Types** cover all aspects of work
2. **ID Format** (PREFIX-NUMBER) ensures uniqueness
3. **JSON Templates** provide structure and consistency
4. **Bidirectional Links** create knowledge graph
5. **Quality Standards** maintain high data quality

**Success Metrics:**
- 37+ entities per video minimum
- 100% bidirectional cross-references
- 100% JSON validation pass rate
- 90%+ coverage improvement per video

**Next Steps:**
- Review example entities in LIBRARIES/
- Practice creating entities from templates
- Validate cross-references
- Maintain quality standards

---

*End of Taxonomy Building Guide*
*For examples, see ENTITIES/LIBRARIES/ folders*
*For templates, see templates/JSON_Entity_Templates/*
