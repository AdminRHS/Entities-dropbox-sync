# Daily Work Log Entity Extraction System
## PMT-070 Version 2.0 - Taxonomy-Aligned Architecture

**Version:** 2.0.0
**Created:** 2025-11-19
**Entity:** PROMPTS/UTILITIES/Daily_Updates
**Taxonomy Alignment:** TASK_MANAGERS Entity Hierarchy

---

## PURPOSE

Extract structured taxonomy entities from daily work logs using the proven TASK_MANAGERS hierarchical methodology:

**PROJECT → MILESTONE → TASK → STEP → ACTION/OBJECT/RESPONSIBILITY/TOOL**

Aligns with existing LIBRARIES taxonomy (429 Actions, 193 Responsibilities, 190+ Tools, 28 Skills) following ISO code standards.

---

## CORE TAXONOMY STRUCTURE

### Hierarchical Entity Model

```
PROJECT TEMPLATE (PRT-###) - Major initiative (multi-day/week)
│
├── MILESTONE TEMPLATE (MLT-###) - Phase deliverable
│   │
│   ├── TASK TEMPLATE (TST-###) - ACTION + OBJECT + CONTEXT
│   │   │
│   │   ├── STEP TEMPLATE (STT-###) - Atomic procedural action
│   │   │   │
│   │   │   ├── ACTION (ACT-###) - Verb from 429 library
│   │   │   ├── OBJECT (OBJ-###) - Target/deliverable
│   │   │   ├── TOOL (TOOL-{CAT}-###) - Instrument used
│   │   │   └── RESPONSIBILITY (RSP-###) - Action+Object pair
│   │   │
│   │   └── CHECKLIST (CHT-###) - Verification items
│   │
│   └── PROFESSION (PRF-###) - Role performing milestone
│
└── WORKFLOW (WRF-###) - Reusable process pattern
```

### ISO Code Registry (Aligned with TASK_MANAGERS)

**Entity Codes:**
- `PRT` - Project Template
- `MLT` - Milestone Template
- `TST` - Task Template
- `STT` - Step Template
- `CHT` - Checklist Template
- `WRF` - Workflow
- `ACT` - Action
- `OBJ` - Object
- `RSP` - Responsibility
- `PRF` - Profession

**Department Codes:**
- `AID` - AI & Automations (includes former OPS, ADM)
- `HRM` - Human Resources Management
- `DEV` - Development & Engineering
- `LGN` - Lead Generation
- `DGN` - Design & Creative
- `VID` - Video Production
- `SLS` - Sales & Client Relations
- `SMM` - Social Media Management
- `FIN` - Finance & Accounting

---

## EXTRACTION METHODOLOGY

### Phase 1: Initial Read & Clustering

**Goal:** Identify natural work clusters (projects/initiatives)

**Steps:**
1. Read entire daily log
2. Identify major work themes (1-3 per day typically)
3. Cluster related activities under themes
4. Look for multi-day continuations (ongoing projects)

**Output:** 1-3 project candidates with activity groups

---

### Phase 2: Project Template Formation

**Criteria for Project (PRT):**
- Spans multiple days/weeks
- Has clear end goal/deliverable
- Contains 2+ distinct phases (milestones)
- Involves multiple tasks/activities

**If NOT a Project:** Skip to Phase 3 (Milestone-level extraction)

**Format:**
```markdown
## PRT-### (Auto-increment or reference existing)

**Name:** [Verb] + [Deliverable/Goal]
**Department:** [Primary ISO codes]
**Duration:** [Timeframe estimate]
**Status:** [Not Started/In Progress/Completed/Blocked]
**Description:** [1-2 sentence summary]
```

**Example:**
```markdown
## PRT-009: Complete Employee Compliance System

**Name:** Complete Employee Compliance System
**Department:** HRM, AID
**Duration:** 2 weeks
**Status:** In Progress
**Description:** Build automated employee compliance auditing system with Dropbox monitoring, tool installation verification, and daily file tracking.
```

---

### Phase 3: Milestone Template Extraction

**Criteria for Milestone (MLT):**
- Represents a distinct phase/deliverable within project (or standalone if no project)
- Contains 2+ tasks
- Has clear completion criteria
- Can be marked as complete independently

**Format:**
```markdown
### MLT-### (Phase Name) - [Project Reference if exists]

**Name:** [Deliverable/Outcome achieved]
**Department:** [ISO codes]
**Tasks:** [TST-### references]
**Timeline:** [Date range or duration]
**Status:** [Not Started/In Progress/Completed/Blocked]
**Deliverables:**
- [Concrete output 1]
- [Concrete output 2]
```

**Example:**
```markdown
### MLT-027: Employee Audit System Deployed - PRT-009 Phase 1

**Name:** Employee Audit System Deployed
**Department:** HRM, AID
**Tasks:** TST-072, TST-073, TST-074
**Timeline:** Week 1 (Nov 18-24)
**Status:** In Progress
**Deliverables:**
- Employee compliance audit checklist (98 items)
- Automated Dropbox folder scanner
- Installation verification script for VS Code/Cursor
- Daily file tracking dashboard
```

---

### Phase 4: Task Template Extraction

**Criteria for Task (TST):**
- Single actionable work item
- Formula: **ACTION + OBJECT + CONTEXT/TOOL**
- Takes 15 min to 4 hours typically
- Can be delegated to one person
- Has clear done/not-done state

**Format:**
```markdown
#### TST-### (Task Name) - [Milestone Reference]

**Name:** [Action] + [Object] + [Context]
**Milestone:** MLT-###
**Department:** [ISO codes]
**Status:** [Not Started/In Progress/Completed/Blocked]
**Steps:** [Count] steps
**Duration:** [Estimate]
**Tools:** [Tool names]
**Responsibilities:** [RSP-### references]
```

**Example:**
```markdown
#### TST-072: Audit Employee Dropbox Folders - MLT-027

**Name:** Audit Employee Dropbox Folders for Compliance
**Milestone:** MLT-027
**Department:** HRM, AID
**Status:** In Progress
**Steps:** 5 steps
**Duration:** 10-15 min/employee
**Tools:** Dropbox, Cursor, VS Code
**Responsibilities:** RSP-089 (audit employee folders), RSP-090 (verify installations)
```

---

### Phase 5: Step Template Extraction

**Criteria for Step (STT):**
- Atomic action (cannot be broken down further)
- Takes 1-15 minutes typically
- Clear procedural instruction
- Follows verb-noun pattern

**Format:**
```markdown
##### STT-###-## (Step Description)

**Action:** [Verb]
**Object:** [Noun/target]
**Tool:** [If specific tool used]
**Duration:** [Time estimate]
```

**Naming Convention:** `STT-{TaskID}-{SequenceNumber}`

**Example:**
```markdown
##### STT-072-01: Navigate to Employee Dropbox Folder

**Action:** Navigate
**Object:** Employee Dropbox folder (ENTITIES/Accounts/[ID])
**Tool:** Dropbox Desktop
**Duration:** 30 seconds

##### STT-072-02: Check for Daily/Plans/Tasks Files

**Action:** Verify
**Object:** Required file presence (daily.md, plans.md, tasks.md)
**Tool:** File Explorer / Finder
**Duration:** 1 minute

##### STT-072-03: Check File Last Modified Dates

**Action:** Check
**Object:** Last modified timestamps
**Tool:** File Explorer properties
**Duration:** 30 seconds
```

---

### Phase 6: Entity Extraction (Actions, Objects, Responsibilities)

#### 6A. Action Extraction

**Extract from verbs used in tasks/steps**

**Categories (7 types A-G):**

| Category | Description | Examples |
|----------|-------------|----------|
| **A. CREATION** | Bring into existence | create, build, generate, design, develop |
| **B. MODIFICATION** | Change existing | update, edit, refine, migrate, switch, modify |
| **C. ANALYSIS** | Examine/investigate | analyze, identify, parse, review, investigate |
| **D. ORGANIZATION** | Structure/arrange | organize, structure, filter, cluster, categorize |
| **E. COMMUNICATION** | Share/transfer | integrate, sync, export, share, present |
| **F. AUTOMATION** | System actions | automate, deploy, execute, schedule, trigger |
| **G. DATA OPS** | Manipulate data | extract, collect, match, transcribe, transform |

**Output Format:**
```markdown
### ACT-### (Verb)

**Category:** [A-G letter]
**Frequency:** [Count in this daily log]
**Evidence:** "[Quote from log]"
**Library Status:** ✅ Matched / ❌ New
```

#### 6B. Object Extraction

**Extract from nouns (deliverables, outputs, targets)**

**Format:**
```markdown
### OBJ-### (Noun Phrase)

**Probability Score:** [0.0-1.0]
**Context:** "[Where mentioned]"
**Department:** [ISO code]
**Library Status:** ✅ Matched / ❌ New
```

**Probability Scoring:**
- **1.0** - Explicitly stated deliverable with clear name
- **0.8-0.9** - Strongly implied deliverable with context
- **0.5-0.7** - Mentioned target/goal, unclear if created
- **0.3-0.4** - Reference only, likely not deliverable
- **0.0-0.2** - Tangential mention

#### 6C. Responsibility Formation

**Formula:** `ACTION + OBJECT = RESPONSIBILITY`

**Format:**
```markdown
### RSP-### (Responsibility Phrase)

**Action:** ACT-###
**Object:** OBJ-###
**Full Phrase:** [action verb] + [object noun]
**Department:** [ISO code]
**Library Status:** ✅ Matched / ❌ New
```

**Example:**
```markdown
### RSP-089: Audit Employee Folders

**Action:** ACT-012 (audit)
**Object:** OBJ-234 (employee folders)
**Full Phrase:** audit employee folders
**Department:** HRM, AID
**Library Status:** ❌ New
```

---

### Phase 7: Tool & Profession Identification

#### 7A. Tool Extraction

**Explicit mentions only** - Do not infer tools

**Format:**
```markdown
### TOOL-{CAT}-### (Tool Name)

**Category:** [AI/AUTO/DESIGN/DEV/VIDEO/COMM/DATA/FILE/etc.]
**Frequency:** [Count]
**Context:** "[Usage context]"
**Department:** [Primary users]
**Library Status:** ✅ Matched / ❌ New
```

**Tool Categories:**
- `TOOL-AI-###` - AI/LLM tools (Claude, GPT, Gemini, Perplexity)
- `TOOL-AUTO-###` - Automation (n8n, Make, Zapier)
- `TOOL-DESIGN-###` - Design (Photoshop, Figma, Canva)
- `TOOL-DEV-###` - Development (VS Code, Cursor, Git, GitHub)
- `TOOL-VIDEO-###` - Video (Premiere, AI Studio, VAYU)
- `TOOL-COMM-###` - Communication (Slack, Gmail, Zoom)
- `TOOL-DATA-###` - Data (Excel, Sheets, Airtable)
- `TOOL-FILE-###` - File management (Dropbox, Drive)
- `TOOL-HR-###` - HR/Recruitment (Notion, ATS systems)

#### 7B. Profession Identification

**Inferred from work performed and responsibilities**

**Format:**
```markdown
### PRF-### (Profession Title)

**Responsibilities:** [RSP references]
**Tools Used:** [Tool references]
**Department:** [ISO code]
**Evidence:** "[Work performed quotes]"
**Library Status:** ✅ Matched / ❌ New
```

---

### Phase 8: Workflow Pattern Recognition

**Identify reusable process sequences**

**Criteria for Workflow (WRF):**
- Repeatable process (can be done multiple times)
- Clear start/end triggers
- 3+ steps in sequence
- Can be templated/automated

**Format:**
```markdown
### WRF-### (Workflow Name)

**Type:** [Linear/Parallel/Conditional]
**Trigger:** [What starts this workflow]
**Steps:** [High-level sequence]
**Output:** [End result]
**Department:** [ISO code]
**Frequency:** [How often repeated]
**Automation Potential:** [High/Medium/Low]
```

**Example:**
```markdown
### WRF-021: Employee Compliance Audit Workflow

**Type:** Linear
**Trigger:** New employee onboarding OR weekly audit schedule
**Steps:**
1. Navigate to employee Dropbox folder
2. Check required files presence (daily/plans/tasks)
3. Verify tool installations (Dropbox/VS Code/Cursor)
4. Check file update timestamps (last 7 days)
5. Document findings in audit spreadsheet
6. Schedule 1:1 if issues found

**Output:** Compliance audit report + action items
**Department:** HRM, AID
**Frequency:** Weekly (ongoing), per new hire
**Automation Potential:** High (50%+ can be scripted)
```

---

### Phase 9: Blocker & Dependency Tracking

#### 9A. Blockers

**Any impediment preventing progress**

**Format:**
```markdown
### BLOCKER-### (Issue Description)

**Severity:** [CRITICAL/HIGH/MEDIUM/LOW]
**Type:** [Technical/Resource/Process/External]
**Blocking:** [TST/MLT/PRT references]
**Description:** [Clear issue statement]
**Impact:** [What cannot proceed]
**Proposed Resolution:** [If known]
```

**Example:**
```markdown
### BLOCKER-001: 90% Empty Dropbox Files Blocking AI Processing

**Severity:** CRITICAL
**Type:** Process
**Blocking:** MLT-027, TST-072
**Description:** 90-95% of employee Dropbox files are empty placeholders, preventing AI-based analysis and automated compliance checking.
**Impact:** Cannot run batch AI processing on employee work logs; manual review required for all employees
**Proposed Resolution:** Immediate cleanup sprint - delete empty files, train employees on proper file usage
```

#### 9B. Dependencies

**Task/milestone prerequisites**

**Format:**
```markdown
### DEPENDENCY: [Task ID] depends on [Prerequisite IDs]

**Type:** [Hard Dependency/Soft Dependency/Data Dependency]
**Description:** [Why dependency exists]
```

---

## OUTPUT FORMAT

### Required Markdown Document Structure

**File Name:** `daily_processed_[DATE]_[EMPLOYEE-ID]_[LastName]_[FirstName].md`

**Sections (in order):**

1. **METADATA** - File info, person, date, version
2. **EXECUTIVE SUMMARY** - 3-5 bullet points (projects, milestones, tools, entities count)
3. **PROJECT TEMPLATES** - PRT entries (if multi-day work identified)
4. **MILESTONE TEMPLATES** - MLT entries grouped by project
5. **TASK TEMPLATES** - TST entries grouped by milestone
6. **STEP TEMPLATES** - STT entries grouped by task
7. **ACTIONS** - ACT entries by category (A-G)
8. **OBJECTS** - OBJ entries with probability scores
9. **RESPONSIBILITIES** - RSP entries with action+object
10. **TOOLS** - TOOL entries by category
11. **PROFESSIONS** - PRF entries
12. **WORKFLOWS** - WRF entries (if patterns identified)
13. **BLOCKERS** - BLOCKER entries by severity
14. **DEPENDENCIES** - Dependency mappings
15. **ENTITY COUNT SUMMARY** - Table with counts by type
16. **DEPARTMENT DISTRIBUTION** - Table showing work allocation
17. **LIBRARY ENRICHMENT NOTES** - New vs matched entities analysis

---

## METADATA SECTION TEMPLATE

```markdown
# Daily Work Log - Entity Extraction Report
## [Employee Name] - [Date]

---

## METADATA

**FILE_ID**: daily_processed_[YYYYMMDD]_[EMP-ID]_[LastName]_[FirstName]
**EMPLOYEE_ID**: [ID number]
**EMPLOYEE_NAME**: [Full Name]
**PRIMARY_DEPARTMENT**: [ISO code]
**CROSS_DEPARTMENTS**: [Additional ISO codes if applicable]
**DATE**: [YYYY-MM-DD]
**SOURCE_FILE**: [Full file path]
**EXTRACTION_DATE**: [YYYY-MM-DD HH:MM:SS]
**EXTRACTOR_VERSION**: PMT-070_v2.0
**PROCESSING_STATUS**: [Complete/Partial/Failed]
**TAXONOMY_ALIGNMENT**: TASK_MANAGERS v1.0
**ISO_CODE_COMPLIANCE**: ✅ Verified / ⚠️ Deviations noted
```

---

## EXECUTIVE SUMMARY TEMPLATE

```markdown
## EXECUTIVE SUMMARY

**Projects Identified:** [Count] ([PRT IDs])
**Milestones Completed:** [Count] ([MLT IDs])
**Tasks Performed:** [Count] ([TST IDs])
**Steps Executed:** [Count] ([STT IDs])

**Key Achievements:**
- [Major accomplishment 1]
- [Major accomplishment 2]
- [Major accomplishment 3]

**Tools Utilized:** [Count] unique tools ([most frequent 3-5])
**Departments Involved:** [ISO codes with %]
**Blockers Encountered:** [Count] ([Severity breakdown])

**Library Enrichment:**
- ✅ [X] matched entities ([%])
- ❌ [Y] new entities requiring library addition ([%])

**Professions Demonstrated:** [List 2-3 primary roles]
```

---

## EXTRACTION QUALITY STANDARDS

### Mandatory Requirements

1. **ISO Code Compliance** - All department/entity codes must match registry
2. **Hierarchical Integrity** - Every entity must reference parent (Task → Milestone → Project)
3. **No Orphan Entities** - Every step/task/milestone must belong to a parent
4. **Consistent Naming** - Follow "Verb + Noun + Context" formula
5. **Evidence-Based** - Every entity must cite evidence from source log

### Quality Checks

**Before finalizing, verify:**

- [ ] All department codes are from approved list (AID, HRM, DEV, LGN, DGN, VID, SLS, SMM, FIN)
- [ ] No OPS or ADM codes used (deprecated → AID)
- [ ] All entity IDs follow format: `{CODE}-{###}` (3 letters, dash, 3 digits)
- [ ] Steps use naming pattern: `STT-{TaskID}-{Sequence}`
- [ ] Tools use category prefix: `TOOL-{CAT}-{###}`
- [ ] All tasks have at least 1 step
- [ ] All milestones have at least 1 task
- [ ] All blockers have severity + impact
- [ ] Entity count summary adds up correctly

---

## LIBRARY ENRICHMENT ANALYSIS

**At end of extraction, analyze:**

### New Entities Requiring Library Addition

```markdown
## LIBRARY ENRICHMENT NOTES

### New Actions (Add to Actions Library)
- ACT-### (verb) - Frequency: [X], Category: [A-G]
- [repeat for each new action]

### New Objects (Add to Objects Library)
- OBJ-### (noun phrase) - Probability: [score], Department: [ISO]
- [repeat for each new object]

### New Responsibilities (Add to Responsibilities Library)
- RSP-### (action+object) - Department: [ISO], Tools: [list]
- [repeat for each new responsibility]

### New Tools (Add to Tools Library)
- TOOL-{CAT}-### (name) - Category: [CAT], Department: [ISO]
- [repeat for each new tool]

### New Professions (Add to Professions Library)
- PRF-### (title) - Department: [ISO], Skills: [list]
- [repeat for each new profession]

### New Workflows (Add to Workflows Library)
- WRF-### (name) - Type: [Linear/Parallel], Automation: [potential]
- [repeat for each new workflow]
```

---

## EXAMPLE EXTRACTION (Partial)

```markdown
# Daily Work Log - Entity Extraction Report
## Nikolay Artemchuk - 2025-01-17

---

## METADATA

**FILE_ID**: daily_processed_20250117_37226_Artemchuk_Nikolay
**EMPLOYEE_ID**: 37226
**EMPLOYEE_NAME**: Nikolay Artemchuk
**PRIMARY_DEPARTMENT**: AID
**CROSS_DEPARTMENTS**: HRM, SLS, VID, DEV
**DATE**: 2025-01-17
**SOURCE_FILE**: C:\Users\Dell\Dropbox\ENTITIES\DAILIES\17\daily_37226_Artemchuk_Nikolay.md
**EXTRACTION_DATE**: 2025-11-19 16:30:00
**EXTRACTOR_VERSION**: PMT-070_v2.0
**PROCESSING_STATUS**: Complete
**TAXONOMY_ALIGNMENT**: TASK_MANAGERS v1.0
**ISO_CODE_COMPLIANCE**: ✅ Verified

---

## EXECUTIVE SUMMARY

**Projects Identified:** 1 (PRT-009)
**Milestones Completed:** 2 (MLT-027, MLT-028)
**Tasks Performed:** 5 (TST-072 to TST-076)
**Steps Executed:** 18 (STT-072-01 to STT-076-05)

**Key Achievements:**
- Deployed employee compliance audit system with 98-item checklist
- Identified critical blocker: 90% empty Dropbox files preventing AI processing
- Conducted sales team process assessment revealing gaps in client research workflow

**Tools Utilized:** 8 unique tools (Dropbox, VS Code, Cursor, Wispr Flow, Apollo.io, Perplexity, Claude, Gemini)
**Departments Involved:** AID (50%), HRM (25%), SLS (15%), VID (10%)
**Blockers Encountered:** 3 (1 CRITICAL, 2 HIGH)

**Library Enrichment:**
- ✅ 28 matched entities (62%)
- ❌ 17 new entities requiring library addition (38%)

**Professions Demonstrated:** HR Compliance Coordinator, Sales Process Auditor, AI Workflow Engineer

---

## PROJECT TEMPLATES

### PRT-009: Complete Employee Compliance System

**Name:** Complete Employee Compliance System
**Department:** HRM, AID
**Duration:** 2 weeks (Jan 17 - Jan 31)
**Status:** In Progress (Week 1 active)
**Description:** Build automated employee compliance auditing system with Dropbox monitoring, tool installation verification, and daily file tracking across all departments.

**Milestones:**
- MLT-027: Employee Audit System Deployed (Week 1)
- MLT-028: Training & Onboarding System Live (Week 2)
- MLT-029: Continuous Monitoring Automation Active (Week 3+)

---

## MILESTONE TEMPLATES

### MLT-027: Employee Audit System Deployed - PRT-009 Phase 1

**Name:** Employee Audit System Deployed
**Department:** HRM, AID
**Tasks:** TST-072, TST-073, TST-074
**Timeline:** Week 1 (Jan 17-24, 2025)
**Status:** In Progress
**Deliverables:**
- Employee compliance audit checklist (98 items)
- Automated Dropbox folder scanner script
- Installation verification script for VS Code/Cursor/Windsurf
- Daily file tracking dashboard
- Audit findings report template

---

## TASK TEMPLATES

#### TST-072: Audit Employee Dropbox Folders - MLT-027

**Name:** Audit Employee Dropbox Folders for Compliance
**Milestone:** MLT-027
**Department:** HRM, AID
**Status:** In Progress
**Steps:** 5 steps
**Duration:** 10-15 min/employee (scalable to 2-3 min with automation)
**Tools:** Dropbox, Cursor, VS Code
**Responsibilities:** RSP-089 (audit employee folders), RSP-090 (verify tool installations), RSP-091 (check file timestamps)

---

## STEP TEMPLATES

##### STT-072-01: Navigate to Employee Dropbox Folder

**Action:** Navigate
**Object:** Employee Dropbox folder (ENTITIES/Accounts/[EmployeeID])
**Tool:** Dropbox Desktop
**Duration:** 30 seconds

##### STT-072-02: Check Required Files Presence

**Action:** Verify
**Object:** Required file presence (daily.md, plans.md, tasks.md)
**Tool:** File Explorer / Finder
**Duration:** 1 minute
**Checklist:**
- [ ] daily.md exists
- [ ] plans.md exists
- [ ] tasks.md exists
- [ ] files are not empty (>100 bytes)

##### STT-072-03: Check File Last Modified Dates

**Action:** Check
**Object:** Last modified timestamps
**Tool:** File Explorer properties
**Duration:** 30 seconds
**Success Criteria:** All files modified within last 7 days

##### STT-072-04: Verify Tool Installations

**Action:** Check
**Object:** Development tool presence (Dropbox sync status, VS Code, Cursor, Windsurf)
**Tool:** System processes / Applications folder
**Duration:** 2 minutes
**Checklist:**
- [ ] Dropbox installed and syncing
- [ ] VS Code or Cursor installed
- [ ] Extensions configured (if applicable)

##### STT-072-05: Document Findings

**Action:** Record
**Object:** Audit findings in compliance spreadsheet
**Tool:** Google Sheets / Excel
**Duration:** 2 minutes
**Output:** 1 row per employee with compliance status (Pass/Fail + notes)

---

## BLOCKERS

### BLOCKER-001: 90% Empty Dropbox Files Blocking AI Processing

**Severity:** CRITICAL
**Type:** Process / Data Quality
**Blocking:** MLT-027 (employee audit), TSK-072 (folder audits), Future AI automation
**Description:** 90-95% of employee Dropbox files are empty placeholders (0-100 bytes), preventing:
- AI-based content analysis
- Automated compliance checking
- Batch processing workflows
- Entity extraction from daily logs

**Impact:**
- Cannot run automated compliance audits (requires manual review)
- AI tools refuse to process due to low information density
- Wastes storage and creates noise in file system
- Blocks implementation of advanced automation features

**Proposed Resolution:**
1. Immediate cleanup sprint (1-2 days): Delete all empty files
2. Employee training: Proper daily/plans/tasks file usage
3. Automated validation: Pre-commit hooks to reject empty file creation
4. Monitoring: Weekly empty file detection + alerts

**Dependencies:** Must resolve before implementing AI-based employee analytics

---

## ENTITY COUNT SUMMARY

| Entity Type | Total | Matched | New | Match Rate |
|-------------|-------|---------|-----|------------|
| Projects (PRT) | 1 | 0 | 1 | 0% |
| Milestones (MLT) | 2 | 0 | 2 | 0% |
| Tasks (TST) | 5 | 0 | 5 | 0% |
| Steps (STT) | 18 | 0 | 18 | 0% |
| Actions (ACT) | 28 | 28 | 0 | 100% |
| Objects (OBJ) | 35 | 0 | 35 | 0% |
| Responsibilities (RSP) | 14 | 6 | 8 | 43% |
| Tools (TOOL) | 13 | 8 | 5 | 62% |
| Professions (PRF) | 6 | 1 | 5 | 17% |
| Workflows (WRF) | 3 | 0 | 3 | 0% |
| **TOTAL** | **125** | **43** | **82** | **34%** |

---

## DEPARTMENT DISTRIBUTION

| Department | Projects | Milestones | Tasks | Steps | % of Work |
|------------|----------|------------|-------|-------|-----------|
| AID | 1 | 2 | 5 | 12 | 50% |
| HRM | 1 | 2 | 3 | 8 | 25% |
| SLS | 0 | 1 | 1 | 4 | 15% |
| VID | 0 | 1 | 1 | 3 | 10% |

---

**END OF EXAMPLE**
```

---

## VERSION HISTORY

**v2.0.0** (2025-11-19)
- Complete rewrite aligned with TASK_MANAGERS taxonomy
- Added Project Template (PRT) hierarchy level
- ISO code compliance with department registry
- Step template naming: `STT-{TaskID}-{Sequence}`
- Tool categorization: `TOOL-{CAT}-###`
- Blocker tracking with severity levels
- Dependency mapping
- Quality checklist integration
- Evidence-based extraction requirements

**v1.3** (2025-11-19)
- Added PHASE 0: Preparation with markup injection
- 7-step pipeline

**v1.2** (2025-11-19)
- Removed Library Enrichment section (separate phase)
- Removed Skills section
- 15 sections, 6-step pipeline

**v1.1** (2025-11-19)
- Markdown-only output
- Updated library paths

**v1.0** (2025-11-19)
- Initial release, 17 sections

---

## REFERENCES

- **TASK_MANAGERS Taxonomy Hierarchy**: `ENTITIES/TASK_MANAGERS/Taxonomy/Taxonomy_Hierarchy_Tree.md`
- **ISO Code Registry**: `ENTITIES/TASK_MANAGERS/Taxonomy/Taxonomy_ISO_Code_Registry.md`
- **Actions Library**: `ENTITIES/LIBRARIES/Actions/` (429 actions)
- **Responsibilities Library**: `ENTITIES/LIBRARIES/Responsibilities/` (193 responsibilities)
- **Tools Library**: `ENTITIES/LIBRARIES/Tools/` (190+ tools)
- **Professions Library**: `ENTITIES/LIBRARIES/Professions/` (profession taxonomy)
- **Department Definitions**: `ENTITIES/LIBRARIES/LBS_006_Departments/Master/departments.json`

---

**END OF PROMPT PMT-070 v2.0**
