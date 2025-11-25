# PROMPT: Build LIBRARIES Taxonomy - Complete Knowledge Base ID System

## Objective
Create a comprehensive master taxonomy list of all LIBRARIES sub-entities with standardized consonant-only 3-letter ISO codes and sequential 3-digit IDs. LIBRARIES is the foundational knowledge base containing all reusable components across the ecosystem.

## ID Structure Format
```
{XXX}-{###}

XXX = 3-letter consonant-only ISO code (derived from entity type name)
### = 3-digit sequential ID (001-999)
```

## Entity Type Taxonomy

### Primary LIBRARIES Sub-Entities

| Entity Type | ISO Code | ID Range | Count | Description |
|-------------|----------|----------|-------|-------------|
| Departments | **DPT** | DPT-001 to DPT-010 | 10 | Organizational departments (AID, HRM, DVL, etc.) |
| Professions | **PRF** | PRF-001 to PRF-027 | 27 | Job roles and professional categories |
| Tools | **TLS** | TLS-001 to TLS-200+ | 150+ | Software, platforms, and methodologies |
| Actions | **ACT** | ACT-001 to ACT-429 | 429 | Verbs for task composition (command, process, result) |
| Objects | **OBJ** | OBJ-001 to OBJ-050+ | 36+ | Work objects and deliverables by department |
| Skills | **SKL** | SKL-001 onwards | TBD | Technical and soft skills organized by dept/profession/tool |
| Parameters | **PRM** | PRM-001 onwards | TBD | Configurable parameters by profession/department |
| Countries | **CNT** | CNT-001 onwards | TBD | Geographic locations and country codes |
| Currencies | **CRR** | CRR-001 onwards | TBD | Currency types and exchange systems |
| Statuses | **STS** | STS-001 onwards | TBD | Workflow and entity status indicators |

### ISO Code Derivation Rules

**Pattern**: Extract first 3 consonants from entity type name, removing vowels (A, E, I, O, U)

Examples:
- **D**_e**P**_ar**T**_ment → **DPT**
- **PR**_o**F**_ession → **PRF**
- **T**_oo**L**_**S** → **TLS**
- **ACT**_ion → **ACT**
- **OBJ**_ect → **OBJ**
- **SK**_i**L**_l → **SKL**
- **P**_a**R**_a**M**_eter → **PRM**
- **C**_ou**NT**_ry → **CNT**
- **C**_u**RR**_ency → **CRR**
- **ST**_atu**S** → **STS**

## LIBRARIES Directory Structure

```
LIBRARIES/
├── DEPARTMENTS/                    # DPT-001 to DPT-010
│   ├── departments.json           # Master department list
│   └── By_Department/
│       ├── AI/                    # AID - AI & Automations
│       │   ├── integration.json
│       │   ├── metrics.json
│       │   ├── objects_reference.json
│       │   ├── overview.json
│       │   ├── projects.json
│       │   ├── structure.json
│       │   ├── task_managers_reference.json
│       │   ├── team_composition.json
│       │   └── tools_reference.json
│       └── SMM/                   # Social Media Management
│
├── Professions/                   # PRF-001 to PRF-027
│   ├── professions.json          # Master professions list
│   ├── Account_Executive.json
│   ├── AI_Engineer.json
│   ├── Designer.json
│   ├── Lead_Generator.json
│   └── ... (27 total)
│
├── Tools/                         # TLS-001 to TLS-200+
│   ├── AI_Tools/                 # 60+ tools
│   │   ├── Claude.json
│   │   ├── ChatGPT.json
│   │   ├── Cursor.json
│   │   └── ...
│   ├── Automation_Tools/
│   │   ├── n8n.json
│   │   ├── Make.json
│   │   └── Zapier.json
│   ├── Development_Tools/
│   ├── Business_Tools/
│   ├── Video_Editing_Tools/
│   └── ... (20+ categories)
│
├── Responsibilities/              # Actions + Objects system
│   ├── Actions/                  # ACT-001 to ACT-429
│   │   ├── Actions_Master.json  # 429 actions
│   │   ├── Actions_Master_Command_Verbs.json
│   │   ├── Actions_Master_Process_Verbs.json
│   │   └── Actions_Master_Result_Verbs.json
│   ├── Objects/                  # OBJ-001 to OBJ-050+
│   │   ├── AI_Automation_Objects.json
│   │   ├── Design_Deliverables.json
│   │   ├── Lead_Generation_Objects.json
│   │   ├── RAG_Objects.json
│   │   └── ...
│   └── Parameters/               # PRM-001 onwards
│       ├── organized_by_profession/
│       └── organized_by_department/
│
├── Countries/                     # CNT-001 onwards
│   └── countries.json
│
├── Currencies/                    # CRR-001 onwards
│
└── Statuses/                      # STS-001 onwards
```

## Task Instructions

### Phase 1: Inventory LIBRARIES Entities

For each sub-entity type in LIBRARIES:

1. **Scan directory structure**:
   - Location: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\{EntityType}/`
   - Identify all JSON files and master lists
   - Extract current naming patterns and IDs

2. **Extract entity metadata**:
   - Current file name
   - Current ID (if exists)
   - Entity name/title
   - Description
   - Category/classification
   - Department association (if applicable)
   - Full file path

3. **Map to new ISO code system**:
   - Assign new ID: `{ISO}-{###}`
   - Maintain sequential numbering
   - Preserve relationships to other entities

### Phase 2: Generate Master Taxonomy List

Create structured lists for each sub-entity type:

#### 2.1 DEPARTMENTS (DPT-###)

| New_ID | Dept_Code | Name | Full_Name | Color | Description | Active | File_Path |
|--------|-----------|------|-----------|-------|-------------|--------|-----------|

**Example:**
```csv
New_ID,Dept_Code,Name,Full_Name,Color,Description,Active,File_Path
DPT-001,AID,AI & Automations,AI & Automations Department,rgb(61,183,124),Artificial intelligence automation and operations,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-002,HRM,Human Resources,Human Resources Management,rgb(255,99,71),Talent acquisition and management,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-003,DEV,Development,Development & Engineering,rgb(100,149,237),Software development and engineering,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-004,LGN,Lead Generation,Lead Generation,rgb(255,215,0),Lead generation and outreach,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-005,DGN,Design,Design & Creative,rgb(218,112,214),Design and creative production,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-006,VID,Video,Video Production,rgb(255,165,0),Video editing and production,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-007,SLS,Sales,Sales & Client Relations,rgb(50,205,50),Sales and client management,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-008,SMM,Social Media,Social Media Management,rgb(135,206,250),Social media marketing and management,true,LIBRARIES/DEPARTMENTS/departments.json
DPT-009,FNC,Finance,Finance & Accounting,rgb(144,238,144),Financial operations and accounting,true,LIBRARIES/DEPARTMENTS/departments.json
```

**Department 3-Letter Codes:**
- **AID** = AI & Automations (consolidates AI, ADM)
- **HRM** = Human Resource Management
- **DEV** = Development
- **LGN** = Lead Generation
- **DGN** = Design
- **VID** = Video
- **SLS** = Sales
- **SMM** = Social Media Management (keep existing)
- **FNC** = Finance

#### 2.2 PROFESSIONS (PRF-###)

| New_ID | Name | Description | Department | Seniority | File_Path |
|--------|------|-------------|------------|-----------|-----------|

**Example:**
```csv
New_ID,Name,Description,Department,Seniority,File_Path
PRF-001,AI Engineer,Develops AI systems and automation solutions,AID,Senior,LIBRARIES/Professions/AI_Engineer.json
PRF-002,Account Executive,Manages client accounts and relationships,SLS,Mid,LIBRARIES/Professions/Account_Executive.json
PRF-003,Designer,Creates visual designs and brand assets,DGN,Mid,LIBRARIES/Professions/Designer.json
PRF-004,Lead Generator,Generates and qualifies leads through outreach,LDG,Junior,LIBRARIES/Professions/Lead_Generator.json
```

#### 2.3 TOOLS (TLS-###)

| New_ID | Name | Category | Type | Department | Provider | File_Path |
|--------|------|----------|------|------------|----------|-----------|

**Example:**
```csv
New_ID,Name,Category,Type,Department,Provider,File_Path
TLS-001,Claude,AI_Tools,LLM,AID,Anthropic,LIBRARIES/Tools/AI_Tools/Claude.json
TLS-002,ChatGPT,AI_Tools,LLM,AID,OpenAI,LIBRARIES/Tools/AI_Tools/ChatGPT.json
TLS-003,Cursor,AI_Tools,IDE,DVL,Cursor,LIBRARIES/Tools/AI_Tools/Cursor.json
TLS-004,n8n,Automation_Tools,Workflow,AID,n8n,LIBRARIES/Tools/Automation_Tools/n8n.json
TLS-005,Make,Automation_Tools,Workflow,AID,Make,LIBRARIES/Tools/Automation_Tools/Make.json
TLS-006,Zapier,Automation_Tools,Workflow,AID,Zapier,LIBRARIES/Tools/Automation_Tools/Zapier.json
```

**Tool Categories (20+):**
- AI_Tools
- Automation_Tools
- Development_Tools
- Business_Tools
- Cloud_Platforms
- Databases
- Data_Tools
- Developer_Platforms
- File_Management
- Infrastructure_Tools
- Integration_Tools
- Methodologies
- Payment_Tools
- Publishing_Platforms
- Security_Tools
- Social_Media_Platforms
- Video_Editing_Tools
- Web_Tools
- Authentication_Tools

#### 2.4 ACTIONS (ACT-###)

| New_ID | Action | Type | Category | Use_Case | Example |
|--------|--------|------|----------|----------|---------|

**Example:**
```csv
New_ID,Action,Type,Category,Use_Case,Example
ACT-001,Create,Command,Core,Start new entity,Create job posting
ACT-002,Update,Command,Core,Modify existing,Update client record
ACT-003,Delete,Command,Core,Remove entity,Delete old campaign
ACT-004,Analyze,Process,Research,Examine data,Analyze market trends
ACT-005,Generate,Process,Production,Produce output,Generate report
ACT-006,Optimize,Process,Improvement,Enhance performance,Optimize workflow
ACT-007,Complete,Result,Completion,Finish task,Complete onboarding
ACT-008,Approve,Result,Validation,Confirm quality,Approve design
```

**Action Types:**
- **Command Verbs**: Direct actions (Create, Update, Delete, Send, etc.)
- **Process Verbs**: Transformational actions (Analyze, Generate, Optimize, etc.)
- **Result Verbs**: Outcome actions (Complete, Approve, Validate, etc.)

**Source**: `LIBRARIES/Responsibilities/Actions/Actions_Master.json` (429 actions total)

#### 2.5 OBJECTS (OBJ-###)

| New_ID | Object | Category | Department | Description | File_Path |
|--------|--------|----------|------------|-------------|-----------|

**Example:**
```csv
New_ID,Object,Category,Department,Description,File_Path
OBJ-001,Job Posting,Recruitment,HRM,Job opening advertisement,LIBRARIES/Responsibilities/Objects/Recruitment_Objects.json
OBJ-002,Email Campaign,Marketing,LDG,Email outreach campaign,LIBRARIES/Responsibilities/Objects/Lead_Generation_Objects.json
OBJ-003,Design Mockup,Deliverable,DGN,Visual design prototype,LIBRARIES/Responsibilities/Objects/Design_Deliverables.json
OBJ-004,AI Prompt,AI System,AID,Prompt template for AI models,LIBRARIES/Responsibilities/Objects/AI_Automation_Objects.json
OBJ-005,Vector Database,Data Structure,AID,RAG vector storage,LIBRARIES/Responsibilities/Objects/RAG_Objects.json
```

**Object Categories:**
- AI_Automation_Objects (10 objects)
- Agentic_Engineering_Objects (13 objects)
- Design_Deliverables
- Lead_Generation_Objects (10 objects)
- RAG_Objects (6 objects)
- Recruitment_Objects

#### 2.6 SKILLS (SKL-###)

| New_ID | Skill | Category | Department | Proficiency | Tools | File_Path |
|--------|-------|----------|------------|-------------|-------|-----------|

**Example:**
```csv
New_ID,Skill,Category,Department,Proficiency,Tools,File_Path
SKL-001,Python Programming,Technical,DVL,Advanced,VSCode|Cursor,LIBRARIES/Skills/By_Profession/Developer.json
SKL-002,Prompt Engineering,Technical,AID,Expert,Claude|ChatGPT,LIBRARIES/Skills/By_Profession/AI_Engineer.json
SKL-003,Adobe Photoshop,Technical,DGN,Advanced,Photoshop,LIBRARIES/Skills/By_Tool/Adobe_Suite.json
```

**Skill Organization:**
- `By_Department/` - Skills grouped by department
- `By_Profession/` - Skills grouped by profession
- `By_Tool/` - Skills grouped by tool
- `By_Difficulty/` - Skills grouped by difficulty level

#### 2.7 PARAMETERS (PRM-###)

| New_ID | Parameter | Type | Entity | Default | Options | File_Path |
|--------|-----------|------|--------|---------|---------|-----------|

**Example:**
```csv
New_ID,Parameter,Type,Entity,Default,Options,File_Path
PRM-001,Experience_Level,Enum,Profession,Mid,"Junior|Mid|Senior|Lead",LIBRARIES/Responsibilities/Parameters/organized_by_profession/
PRM-002,Priority,Enum,Task,Medium,"Low|Medium|High|Urgent",LIBRARIES/Responsibilities/Parameters/
```

#### 2.8 COUNTRIES (CNT-###)

| New_ID | Country_Code | Country_Name | Region | Currency | File_Path |
|--------|--------------|--------------|--------|----------|-----------|

**Example:**
```csv
New_ID,Country_Code,Country_Name,Region,Currency,File_Path
CNT-001,US,United States,North America,USD,LIBRARIES/Countries/countries.json
CNT-002,UK,United Kingdom,Europe,GBP,LIBRARIES/Countries/countries.json
```

#### 2.9 CURRENCIES (CRR-###)

| New_ID | Currency_Code | Currency_Name | Symbol | File_Path |
|--------|---------------|---------------|--------|-----------|

**Example:**
```csv
New_ID,Currency_Code,Currency_Name,Symbol,File_Path
CRR-001,USD,US Dollar,$,LIBRARIES/Currencies/
CRR-002,EUR,Euro,€,LIBRARIES/Currencies/
```

#### 2.10 STATUSES (STS-###)

| New_ID | Status | Entity_Type | Color | Description | File_Path |
|--------|--------|-------------|-------|-------------|-----------|

**Example:**
```csv
New_ID,Status,Entity_Type,Color,Description,File_Path
STS-001,Active,Universal,green,Entity is active and operational,LIBRARIES/Statuses/
STS-002,Pending,Task,yellow,Task awaiting action,LIBRARIES/Statuses/
```

### Phase 3: Create Hierarchical Relationships Map

Document relationships between LIBRARIES entities:

```
DPT-001 (AI & Automations)
  ├─ PROFESSIONS
  │  ├─ PRF-001 (AI Engineer)
  │  └─ PRF-012 (Automation Specialist)
  ├─ TOOLS
  │  ├─ TLS-001 (Claude)
  │  ├─ TLS-002 (ChatGPT)
  │  └─ TLS-004 (n8n)
  ├─ SKILLS
  │  ├─ SKL-002 (Prompt Engineering)
  │  └─ SKL-015 (Workflow Automation)
  └─ OBJECTS
     ├─ OBJ-004 (AI Prompt)
     └─ OBJ-005 (Vector Database)

TASK COMPOSITION FORMULA:
  ACT-001 (Create) + OBJ-001 (Job Posting) + TLS-XXX (Notion) = TASK
  [Action]       + [Object]           + [Tool]        = Task Template
```

### Phase 4: Cross-Entity Relationships

Map how LIBRARIES connects to other ENTITIES:

#### 4.1 LIBRARIES → TASK_MANAGERS
```
DPT-001 (AI & Automations) → PRJ-001 (AI Tutorial Research)
PRF-001 (AI Engineer) → TSK-021 (Discover AI Tutorial Content)
TLS-001 (Claude) → STP-001 (Configure Perplexity Search)
ACT-004 (Analyze) + OBJ-XXX (Video Content) → TSK-024 (Initial Video Analysis)
```

#### 4.2 LIBRARIES → TALENTS
```
PRF-001 (AI Engineer) → EMP-2024-001 (Employee profile)
SKL-002 (Prompt Engineering) → Employee skills matrix
DPT-001 (AI & Automations) → Team composition
```

#### 4.3 LIBRARIES → JOBS
```
PRF-001 (AI Engineer) → JOB-2024-001 (Job posting)
SKL-002 (Prompt Engineering) → Job requirements
TLS-001 (Claude) → Required tools
```

#### 4.4 LIBRARIES → BUSINESSES
```
DPT-007 (Sales) → Client relationship management
PRF-002 (Account Executive) → Client account owner
TLS-XXX (CRM) → Client management tools
```

### Phase 5: Generate Department Distribution

Break down entities by department:

| Department | ISO | Professions | Tools | Skills | Objects | Actions | Total |
|------------|-----|-------------|-------|--------|---------|---------|-------|
| AI & Automations | AID | 4 | 65 | 120 | 29 | 150 | 368 |
| Human Resources | HRM | 3 | 8 | 25 | 5 | 50 | 91 |
| Development | DVL | 5 | 35 | 80 | 12 | 100 | 232 |
| Lead Generation | LDG | 2 | 15 | 30 | 10 | 60 | 117 |
| Design | DGN | 3 | 20 | 40 | 15 | 40 | 118 |
| Video Production | VID | 2 | 12 | 25 | 8 | 30 | 77 |
| Sales | SLS | 3 | 10 | 20 | 6 | 45 | 84 |
| Social Media | SMM | 2 | 8 | 15 | 4 | 25 | 54 |
| Finance | FNC | 3 | 7 | 10 | 3 | 29 | 52 |

### Phase 6: Create Migration Mapping

Document current naming → new ID mappings:

```json
{
  "departments": {
    "AI": "DPT-001",
    "HR": "DPT-002",
    "DEV": "DPT-003",
    "LG": "DPT-004",
    "DESIGN": "DPT-005",
    "VIDEO": "DPT-006",
    "SALES": "DPT-007",
    "SMM": "DPT-008",
    "FIN": "DPT-009"
  },
  "professions": {
    "AI_Engineer": "PRF-001",
    "Account_Executive": "PRF-002",
    "Designer": "PRF-003",
    "Lead_Generator": "PRF-004"
  },
  "tools": {
    "Claude": "TLS-001",
    "ChatGPT": "TLS-002",
    "Cursor": "TLS-003",
    "n8n": "TLS-004"
  },
  "department_code_updates": {
    "AI": "AID",
    "HR": "HRM",
    "DEV": "DVL",
    "LG": "LDG",
    "DESIGN": "DGN",
    "VIDEO": "VDO",
    "SALES": "SLS",
    "SMM": "SMM",
    "FIN": "FNC"
  }
}
```

## Output Deliverables

Generate the following files in `ENTITIES/LIBRARIES/Taxonomy/`:

### 1. Master Taxonomy Lists (CSV format)

**Files:**
- `LIBRARIES_Taxonomy_Departments.csv` (10 departments)
- `LIBRARIES_Taxonomy_Professions.csv` (27 professions)
- `LIBRARIES_Taxonomy_Tools.csv` (150+ tools)
- `LIBRARIES_Taxonomy_Actions.csv` (429 actions)
- `LIBRARIES_Taxonomy_Objects.csv` (36+ objects)
- `LIBRARIES_Taxonomy_Skills.csv` (TBD skills)
- `LIBRARIES_Taxonomy_Parameters.csv` (TBD parameters)
- `LIBRARIES_Taxonomy_Countries.csv` (TBD countries)
- `LIBRARIES_Taxonomy_Currencies.csv` (TBD currencies)
- `LIBRARIES_Taxonomy_Statuses.csv` (TBD statuses)
- `LIBRARIES_Taxonomy_MASTER.csv` (combined view)

### 2. Hierarchical Relationship Tree
**File**: `LIBRARIES_Taxonomy_Hierarchy.md`
- Department → Profession → Skills → Tools relationships
- Action + Object + Tool = Task formula
- Cross-references to TASK_MANAGERS
- Dependency chains

### 3. Department Distribution Report
**File**: `LIBRARIES_Taxonomy_Department_Distribution.md`
- Entity counts by department
- Visual breakdown tables
- Coverage analysis
- Department-specific tool/skill mappings

### 4. Migration Mapping File
**File**: `LIBRARIES_Taxonomy_Migration_Map.json`
- Old names → New IDs mappings
- Department code updates (AI→AID, HR→HRM, etc.)
- Bidirectional lookup support
- Validation checksums

### 5. ISO Code Registry
**File**: `LIBRARIES_Taxonomy_ISO_Code_Registry.md`
- Complete list of all 3-letter codes
- Derivation rules and examples
- Reserved codes for future entities
- Department and entity type code reference

### 6. Cross-Entity Relationship Map
**File**: `LIBRARIES_Cross_Entity_Relationships.md`
- LIBRARIES → TASK_MANAGERS mappings
- LIBRARIES → TALENTS mappings
- LIBRARIES → JOBS mappings
- LIBRARIES → BUSINESSES mappings

## Validation Rules

1. **Uniqueness**: Each ISO-### code must be globally unique across all LIBRARIES sub-entities
2. **Sequential**: IDs within each type must be sequential (no gaps initially)
3. **Consonant-only**: All ISO codes use only consonants (B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z)
4. **Case**: Always uppercase for consistency
5. **Length**: Always 3 letters + 3 digits (e.g., DPT-001, PRF-027, TLS-150)
6. **Department codes**: Use updated 3-letter codes (AID, HRM, DVL, LDG, DGN, VDO, SLS, SMM, FNC)
7. **Relationships**: All entity relationships must be valid and bidirectional
8. **File references**: All file paths must exist and be accessible

## Active Department Codes (Updated)

| Department | Old Code | New Code | Full Name |
|------------|----------|----------|-----------|
| AI & Automations | AI | **AID** | AI, Automations, Administration |
| Human Resources | HR | **HRM** | Human Resource Management |
| Development | DEV | **DVL** | Development & Engineering |
| Lead Generation | LG | **LDG** | Lead Generation |
| Design | DESIGN | **DGN** | Design & Creative |
| Video Production | VIDEO | **VDO** | Video Production |
| Sales | SALES | **SLS** | Sales & Client Relations |
| Social Media | SMM | **SMM** | Social Media Management |
| Finance | FIN | **FNC** | Finance & Accounting |

## Expected Timeline

- **Phase 1** (Inventory): Scan all LIBRARIES subdirectories and extract metadata
- **Phase 2** (Master Lists): Generate CSV files for all 10 sub-entity types
- **Phase 3** (Relationships): Map hierarchical connections between entities
- **Phase 4** (Cross-Entity): Document relationships to TASK_MANAGERS, TALENTS, JOBS, BUSINESSES
- **Phase 5** (Distribution): Calculate department breakdowns for all entity types
- **Phase 6** (Migration): Create comprehensive old→new mappings

## Success Criteria

- ✓ All 700+ LIBRARIES entities catalogued with new ISO codes
- ✓ Zero duplicate IDs across entire LIBRARIES system
- ✓ Hierarchical relationships preserved (Dept → Profession → Skills → Tools)
- ✓ Action + Object composition formula documented
- ✓ Cross-entity relationships mapped to other ENTITIES
- ✓ Migration path documented for all naming changes
- ✓ All 10 deliverable files generated
- ✓ Validation rules passed 100%
- ✓ Department code consolidation completed (AI→AID, HR→HRM, etc.)

## Task Composition Formula (Core Principle)

**LIBRARIES enables task composition through:**

```
TASK = ACTION + OBJECT + TOOL + [CONTEXT]

Example:
  ACT-001 (Create)
  + OBJ-001 (Job Posting)
  + TLS-XXX (Notion)
  + [Context: Frontend Developer]
  = TSK-001 (Create Job Posting for Frontend Developer)

This formula connects:
- Actions (429 verbs from Actions_Master.json)
- Objects (36+ work products from department objects)
- Tools (150+ platforms and software)
- Context (from Professions, Departments, Skills)
```

## Notes

- **LIBRARIES is foundational** for all other entities - establishes shared vocabulary
- **Departments** organize all other sub-entities (professions, tools, skills, objects)
- **Actions + Objects** enable systematic task template generation
- **Tools** define technology stack across all departments
- **Professions** link to TALENTS (employees) and JOBS (openings)
- **Skills** connect professions, tools, and competencies
- System supports up to 999 entities per type before namespace expansion needed
- Maintain backward compatibility during migration period
- **Cross-entity relationships** are critical for ecosystem integrity
- LIBRARIES taxonomy enables automated task generation, skill matching, and workflow optimization
