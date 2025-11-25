# LIBRARIES ISO Code Registry

**Document Type:** Taxonomy Reference
**Entity:** LIBRARIES
**Last Updated:** 2025-11-18
**Purpose:** Standardized entity type codes and naming conventions

---

## Overview

This registry documents the ISO-style codes used to identify and categorize all entity types within the LIBRARIES ecosystem. These codes provide:
- **Unique identification** for each entity type
- **Consistent naming** across the system
- **Quick reference** for entity classification
- **Hierarchical organization** support

---

## Core Entity Type Codes

### Primary Entity Types

| ISO Code | Entity Type | Consonant-Only | Description | Count |
|----------|-------------|----------------|-------------|-------|
| **RSP** | Responsibilities | Yes | Core work responsibilities | 193 core |
| **ACT** | Actions | Yes | Verbs describing activities | 429 |
| **OBJ** | Objects | Yes | Nouns representing deliverables | 50+ |
| **PRM** | Parameters | Yes | Configuration variables | 200+ |
| **TOL** | Tools | Yes | Software/platforms/services | 200+ |
| **SKL** | Skills | Yes | Responsibility + Tool combinations | 28+ |
| **PRF** | Professions | Yes | Job roles and titles | 17 |
| **DPT** | Departments | Yes | Organizational units | 10 |

---

## Department ISO Codes

Standard 3-letter consonant codes for all departments:

| ISO Code | Department Name | Full Name | Entity Count |
|----------|-----------------|-----------|--------------|
| **AIA** | AI_Tasks | AI & Automation | 80 responsibilities |
| **DEV** | DEV_Tasks | Development | 34 responsibilities |
| **HRM** | HR_Tasks | Human Resources | 6 responsibilities |
| **LGN** | LG_Tasks | Lead Generation | 64 responsibilities |
| **DGN** | Design_Tasks | Design | - responsibilities |
| **VID** | Video_Tasks | Video Production | - responsibilities |
| **SLS** | Sales_Tasks | Sales | - responsibilities |
| **SMM** | SMM_Tasks | Social Media Management | - responsibilities |

---

## Action Verb Type Codes

Actions are subdivided into three verb types:

| Sub-Code | Verb Type | Description | Example Actions | Count |
|----------|-----------|-------------|-----------------|-------|
| **ACT-CMD** | Command Verbs | Imperative actions | Create, Update, Delete, Configure | 143 |
| **ACT-PRC** | Process Verbs | Transformation actions | Analyze, Validate, Transform, Integrate | 143 |
| **ACT-RST** | Result Verbs | Output-generating actions | Generate, Produce, Deliver, Publish | 143 |

### Command Verb Examples (ACT-CMD)
```
Create, Update, Delete, Add, Remove, Insert, Append
Configure, Set, Enable, Disable, Toggle, Adjust
Execute, Run, Launch, Start, Stop, Pause, Resume
Install, Deploy, Migrate, Move, Copy, Transfer
```

### Process Verb Examples (ACT-PRC)
```
Analyze, Review, Validate, Verify, Audit, Inspect
Transform, Convert, Migrate, Integrate, Merge
Monitor, Track, Measure, Calculate, Compute
Filter, Sort, Search, Find, Query, Extract
Optimize, Improve, Enhance, Refine, Streamline
```

### Result Verb Examples (ACT-RST)
```
Generate, Produce, Build, Compile, Construct
Deliver, Publish, Deploy, Release, Ship
Report, Document, Present, Communicate, Notify
Export, Download, Save, Store, Archive
```

---

## Object Domain Codes

Objects are organized by functional domain:

| Domain Code | Domain Name | Object Collections | Example Objects |
|-------------|-------------|-------------------|-----------------|
| **OBJ-AIA** | AI & Automation | 3 collections | AI Workflows, RAG Systems, Automation Scripts |
| **OBJ-VID** | Video Production | 2 collections | Video Scripts, Storyboards, Final Videos |
| **OBJ-LGN** | Lead Generation | 1 collection | Lead Lists, Lead Magnets, Lead Data |
| **OBJ-DGN** | Design | 4 collections | UI Designs, Graphics, Portfolios, Mascots |
| **OBJ-DEV** | Development | 1 collection | Code, APIs, Databases, Repositories |
| **OBJ-MKT** | Marketing | 3 collections | Social Posts, Blog Articles, Lesson Content |
| **OBJ-HRM** | Human Resources | 1 collection | Job Descriptions, Candidate Profiles |
| **OBJ-GEN** | General/Multi-Dept | 2 collections | Documents, Catalogs, Reports |

---

## Parameter Organization Codes

Parameters are organized by profession and department:

| Org Code | Organization Type | View Count | Description |
|----------|------------------|------------|-------------|
| **PRM-PRF** | By Profession | 8 files | Profession-specific parameter sets |
| **PRM-DPT** | By Department | 4 files | Department-grouped parameters |

### Profession-Specific Codes
- **PRM-PRF-GRD** - Graphic Designer Parameters
- **PRM-PRF-BED** - Back-End Developer Parameters
- **PRM-PRF-LDG** - Lead Generator Parameters
- **PRM-PRF-RCR** - Recruiter Parameters
- **PRM-PRF-PRJ** - Project Manager Parameters
- **PRM-PRF-SLM** - Sales Manager Parameters
- **PRM-PRF-SEO** - SEO Manager Parameters
- **PRM-PRF-GEN** - General Parameters

---

## Tool Category Codes

Tools are categorized by function and platform type:

| Category Code | Category Name | Tool Count | Examples |
|---------------|---------------|------------|----------|
| **TOL-AIA** | AI Tools | 80+ | Claude, ChatGPT, Midjourney, Runway |
| **TOL-DEV** | Development Tools | 25 | VS Code, Git, Docker, npm |
| **TOL-DBS** | Databases | 7 | PostgreSQL, MongoDB, Redis |
| **TOL-CLD** | Cloud Platforms | 6 | AWS, Azure, GCP, Vercel |
| **TOL-SOC** | Social Media Platforms | 6 | LinkedIn, Twitter, Instagram |
| **TOL-AUT** | Automation Tools | 6 | Zapier, Make, n8n |
| **TOL-BIZ** | Business Tools | 4 | Notion, Airtable, Slack |
| **TOL-DAT** | Data Tools | 3 | Tableau, Power BI |
| **TOL-INT** | Integration Tools | 3 | APIs, Webhooks |
| **TOL-WEB** | Web Tools | 3 | Browsers, Analytics |
| **TOL-AUT** | Authentication | 1 | OAuth, SSO |
| **TOL-SEC** | Security Tools | 1 | Firewalls, Encryption |
| **TOL-PAY** | Payment Tools | 1 | Stripe, PayPal |
| **TOL-FIL** | File Management | 1 | Dropbox, Drive |
| **TOL-VED** | Video Editing | 1 | Premiere, Final Cut |

---

## Profession ISO Codes

Standardized codes for all professions:

| Profession Code | Profession Name | Department | Count |
|-----------------|-----------------|------------|-------|
| **PRF-AIE** | AI Engineer | AI & Automation | 1 |
| **PRF-ATE** | Automation Engineer | AI & Automation | 1 |
| **PRF-ATS** | Automation Specialist | AI & Automation | 1 |
| **PRF-BED** | Backend Developer | Development | 1 |
| **PRF-DEV** | Developer (General) | Development | 1 |
| **PRF-DGN** | Designer | Design | 1 |
| **PRF-LDG** | Lead Generator | Lead Generation | 1 |
| **PRF-MKT** | Marketer | Marketing | 1 |
| **PRF-RCR** | Recruiter | Human Resources | 1 |
| **PRF-ACE** | Account Executive | Sales | 1 |
| **PRF-CSM** | Customer Success Manager | Sales | 1 |
| **PRF-SDR** | Sales Development Rep | Sales | 1 |
| **PRF-EXA** | Executive Assistant | Management | 1 |
| **PRF-OPM** | Operations Manager | Management | 1 |
| **PRF-SMM** | SMM Specialist | Marketing/SMM | 1 |
| **PRF-VDG** | Videographer | Video Production | 1 |

---

## Naming Conventions

### General Rules

1. **Entity IDs**
   - Format: `{TYPE}-{NUMBER}`
   - Example: `RSP-001`, `ACT-042`, `OBJ-015`
   - Zero-padded to 3 digits

2. **File Names**
   - Use underscores for multi-word: `Actions_Master.json`
   - Department prefixes: `AI_Responsibilities.json`
   - Organized collections: `organized_by_profession/`

3. **Collection Names**
   - Descriptive, domain-specific
   - Examples: `Agentic_Engineering_Objects.json`, `Video_Generation_Actions.json`

4. **Master Files**
   - Use `_Master` suffix: `Actions_Master.json`
   - Use `_master` for core: `responsibilities_master.json`

### Consonant-Only Rule

Following TASK_MANAGERS convention, all ISO codes use **consonants only**:

✅ **Correct:**
- RSP (Responsibilities)
- ACT (Actions)
- OBJ (Objects)
- PRM (Parameters)
- TOL (Tools)
- PRF (Professions)
- DPT (Departments)

❌ **Incorrect:**
- RESP (contains vowel)
- ACTN (contains vowel)
- PARAM (contains vowel)

### Department Code Suffixes

When combining entity types with departments:

Format: `{ENTITY-TYPE}-{DEPT-CODE}-{NUMBER}`

Examples:
- `RSP-AIA-001` - AI Responsibility #1
- `OBJ-VID-042` - Video Production Object #42
- `PRM-DEV-015` - Development Parameter #15

---

## Hierarchical ID Structure

### Multi-Level Entity IDs

For nested entities:

```
Level 1: RSP-001 (Responsibility)
Level 2: RSP-001-ACT-042 (Associated Action)
Level 3: RSP-001-ACT-042-OBJ-015 (Associated Object)
Level 4: RSP-001-ACT-042-OBJ-015-PRM-003 (Associated Parameter)
```

Example:
```
RSP-025 = "Create AI-Generated Video Content"
  └─ ACT-128 = "Generate"
     └─ OBJ-042 = "Video Script"
        └─ PRM-067 = "Video Style"
        └─ PRM-068 = "Video Duration"
```

---

## Archive & Legacy Codes

Deprecated codes maintained for backward compatibility:

| Legacy Code | New Code | Migration Date | Reason |
|-------------|----------|----------------|---------|
| PCS | ACT-PRC | 2025-11-17 | Processes merged into Actions |
| RST | ACT-RST | 2025-11-17 | Results merged into Actions |
| SAL | SLS | 2025-11-18 | Department code standardization |
| DSN | DGN | 2025-11-18 | Consonant-only compliance |

---

## Validation Rules

### Code Format Validation

1. **Length:** All codes must be exactly 3 characters (except hierarchical IDs)
2. **Characters:** Uppercase letters only
3. **Consonants:** No vowels (A, E, I, O, U)
4. **Uniqueness:** Each code must be unique within its category

### File Naming Validation

1. **Extensions:**
   - Data files: `.json`
   - Documentation: `.md`
   - Data catalogs: `.csv`

2. **Structure:**
   - No spaces (use underscores)
   - PascalCase for types: `Video_Generation_Objects.json`
   - snake_case for scripts: `validate_ecosystem.py`

---

## Code Assignment Process

### When Creating New Entities

1. **Determine Entity Type** - Which category? (RSP, ACT, OBJ, etc.)
2. **Check Registry** - Review this document for existing codes
3. **Assign Next Number** - Use next available sequential number
4. **Format Consistently** - Follow {TYPE}-{NUM} pattern
5. **Update Registry** - Add new entity to this document
6. **Update Master CSV** - Add row to Libraries_Master_List.csv

### Example Process

```
New entity: "Email Newsletter" (Object, Marketing domain)

1. Type = OBJ (Objects)
2. Check: Last OBJ code = OBJ-017
3. Assign: OBJ-018
4. Format: OBJ-018
5. Full name: "Email Newsletter"
6. File: Social_Media_Deliverables.json (or create Marketing_Objects.json)
7. Update: Libraries_Master_List.csv
```

---

## Cross-Reference with Other Entities

### Entity Code Comparison Table

| Code | TASK_MANAGERS | LIBRARIES | PROMPTS | Notes |
|------|---------------|-----------|---------|-------|
| **PRT** | Project Templates | N/A | N/A | TM-specific |
| **MLT** | Milestone Templates | N/A | N/A | TM-specific |
| **TST** | Task Templates | N/A | N/A | TM-specific |
| **STT** | Step Templates | N/A | N/A | TM-specific |
| **CHT** | Checklist Templates | N/A | N/A | TM-specific |
| **WRF** | Workflows | N/A | N/A | TM-specific |
| **GDS** | Guides | N/A | N/A | TM-specific |
| **PRM** | (Legacy) | Parameters | N/A | LIBRARIES uses PRM for Parameters |
| **PMT** | Entity Reference | N/A | Prompts | PROMPTS standalone entity (155 files) |
| **RSR** | Research | N/A | N/A | TM-specific |
| **RSP** | N/A | Responsibilities | N/A | LIB-specific |
| **ACT** | N/A | Actions | N/A | LIB-specific |
| **OBJ** | N/A | Objects | N/A | LIB-specific |
| **TOL** | N/A | Tools | N/A | LIB-specific |
| **SKL** | N/A | Skills | N/A | LIB-specific |
| **PRF** | N/A | Professions | N/A | LIB-specific |
| **DPT** | N/A | Departments | N/A | LIB-specific |

### Shared Department Codes

TASK_MANAGERS, LIBRARIES, and PROMPTS all use the same department codes:
- **AIA** - AI & Automation
- **DEV** - Development
- **HRM** - Human Resources
- **LGN** - Lead Generation
- **DGN** - Design
- **VID** - Video Production
- **SLS** - Sales
- **SMM** - Social Media Management

---

## Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | 2025-11-18 | Initial registry creation | Taxonomy Team |
| 1.1 | 2025-11-18 | Added SAL→SLS, DSN→DGN updates | Taxonomy Team |

---

## Related Documents

- [Libraries_Master_List.csv](./Libraries_Master_List.csv) - Complete entity catalog
- [Libraries_Hierarchy_Tree.md](./Libraries_Hierarchy_Tree.md) - Visual hierarchy
- [Libraries_Department_Distribution.md](./Libraries_Department_Distribution.md) - Statistics
- [../TAXONOMY_UPDATE_LOG.md](../TAXONOMY_UPDATE_LOG.md) - Change log

---

**Document Status:** Active
**Maintenance Schedule:** Update whenever new entity types or codes are added
**Owner:** LIBRARIES Taxonomy Team
