# Task Manager Entity Filling Prompt (Updated 2025-11-12)

## Objective
Extract all tasks from department consolidated task files (November 2025) and create individual task files in the TASK_MANAGERS structure with complete entity field population. This process transforms unstructured department task lists into structured, taxonomy-compliant task entities with full metadata, ownership, dependencies, steps, and source tracking.

---

## Current State (As of 2025-11-12)

### Task Extraction Status
**Total Tasks Extracted:** 316 tasks from 5 departments

| Department | Tasks Extracted | Task ID Range | Source File |
|------------|----------------|---------------|-------------|
| AI | 10 | AI-001 to AI-010 | AI Department Tasks - November 2025.md |
| Design | 95 | DESIGN-001 to DESIGN-095 | Design Department Tasks - November 2025.md |
| Dev | 11 | DEV-001 to DEV-011 | Dev Department Tasks - November 2025.md |
| LG | 142 | LG-001 to LG-142 | LG Department Tasks - November 2025.md |
| Video | 58 | VIDEO-001 to VIDEO-058 | Video Department Tasks - November 2025.md |

**Status:** Initial extraction completed. All tasks converted to individual files in `/Entities/TASK_MANAGERS/Tasks/`

**Priority:** Complete entity field population, validate data quality, and enrich with taxonomy references.

---

## Source Files Structure

### Primary Source: Department Consolidated Task Files
**Location:** `Dropbox/Nov25/{Department}/{Department} Department Tasks - November 2025.md`

**Files:**
1. `Nov25/AI/AI Department Tasks - November 2025.md`
2. `Nov25/Design/Design Department Tasks - November 2025.md`
3. `Nov25/Dev/Dev Department Tasks - November 2025.md`
4. `Nov25/LG/LG Department Tasks - November 2025.md`
5. `Nov25/Video/Video Department Tasks - November 2025.md`

### Source File Format

**Structure Pattern:**
```markdown
# {Department} Department Tasks - November 2025

**Department:** {Department} Nov25
**Document Type:** Department-Wide Task Consolidation
**Date Range:** November 1-30, 2025
**Last Updated:** {Date}

---

## By Priority Level

### CRITICAL (Immediate - 1-2 days)

#### 1. Task Title Here
- **Owner:** Employee Name
- **Priority:** CRITICAL
- **Status:** Not Started
- **Timeline:** {Timeline description}
- **Department:** {Department} or {Department1, Department2}
- **Profession:** {Profession name}
- **Related Project:** {Project name}
- **Tools:** {Tool list}

**Context:** {Context description}

**Steps:**
1. Step description
2. Step description
...

**Resources:**
- Resource item
...

**Instructions:**
{Additional instructions}

---
```

### Task Identification Patterns

**Task Header Format:**
- Pattern: `#### {number}. {Task Title}`
- Examples: `#### 1. Monitor Power Outage Impact`, `#### 7. Verify Marta Vereteno's Format Conversion Quality`

**Metadata Fields (in task section):**
- `**Owner:**` - Employee name(s), may include multiple names
- `**Priority:**` - CRITICAL, HIGH, MEDIUM, LOW
- `**Status:**` - Not Started, In Progress, Completed, Done, Waiting, Pending, Open
- `**Timeline:**` - Free-text timeline description
- `**Department:**` - Single department or comma-separated list
- `**Profession:**` - Profession name (optional)
- `**Related Project:**` - Project name (optional)
- `**Tools:**` - Tool list (optional)
- `**Dependencies:**` - Dependency description (optional)

**Content Sections:**
- `**Context:**` - Background and context information
- `**Steps:**` - Numbered list of steps
- `**Resources:**` - List of resources (optional)
- `**Instructions:**` - Additional instructions (optional)

---

## Target Entity Structure

### Output Location
**Path:** `Dropbox/Entities/TASK_MANAGERS/Tasks/`

**File Naming Convention:**
- Pattern: `{DEPT}-{NUM}_{Title_Slug}.md`
- Examples:
  - `AI-001_Research_Lead_Generation_Strategies_&_Performance_.md`
  - `DESIGN-007_Verify_Marta_Vereteno's_Format_Conversion_Quality.md`
  - `LG-142_Networks_and_Messages.md`

**Title Slug Rules:**
- Replace spaces with underscores
- Remove special characters except hyphens and ampersands
- Truncate to reasonable length (max 100 chars for filename)
- Preserve key words for identification

### Task File Structure

Each task file follows this structure:

```markdown
# {DEPT}-{NUM}: {Task Title}

**Department:** {Department}
**Status:** {Status}
**Priority:** {Priority}
**Assignee:** {Employee Name}
**Date Created:** {Date}
**Timeline:** {Timeline}

---

## Quick Info

- **Action:** {Action verb}
- **Object:** {Object name}
- **Tool:** {Tool name or TBD}
- **Related Projects:** {Project list}

---

## Description

{Task description/context}

## Full Template

```yaml
task_id: {DEPT}-{NUM}
task_name: {Task Title}
metadata:
  status: {Status}
  priority: {Priority}
  created_date: '{YYYY-MM-DD}'
  extraction_date: '{YYYY-MM-DD}'
ownership:
  department: {Department}
  assigned_to: {Employee Name}
  profession: {Profession}
taxonomy:
  action: {Action}
  object: {Object}
  object_type: Task
  context: {Department}-Department
dependencies:
  prerequisites: []
  related_tasks: []
  related_projects:
  - {Project names}
deliverables:
- Complete: {Task Title}
source_tracking:
  source_file: {Source file name}
  extraction_date: '{YYYY-MM-DD}'
  source_section: Task {number}
```

---

## Steps

1. **{Step title}**
   - Description: {Step description}
   - Status: Not Started

2. **{Step title}**
   - Description: {Step description}
   - Status: Not Started

...

## Tools Required

- {Tool list or TBD}

## Notes

{Additional notes/context}

---

**Source:** {Source file name}
**Date:** {YYYY-MM-DD}
```

---

## Extraction Process

### Phase 1: Task Identification and Parsing

**Step 1: Locate All Tasks**
- Scan source file for task headers matching pattern: `#### {number}. {Title}`
- Extract task number and title
- Track task position in file for source section reference

**Step 2: Extract Task Metadata**
- Parse metadata fields from task section:
  - Owner → `assigned_to`
  - Priority → `priority` (with mapping)
  - Status → `status` (with mapping)
  - Timeline → `timeline`
  - Department → `department` (with parsing logic)
  - Profession → `profession` (optional, may need inference)
  - Related Project → `related_projects`
  - Tools → `tools_required`

**Step 3: Extract Task Content**
- Extract `**Context:**` section → `description` and `notes`
- Extract `**Steps:**` numbered list → `steps` array
- Extract `**Resources:**` → `tools_required` (if not already populated)
- Extract `**Instructions:**` → append to `notes`

**Step 4: Parse Action and Object**
- Parse task title to extract Action (verb) and Object (noun phrase)
- Use action verb library for standardization
- Extract object from remaining title text
- Handle complex titles with multiple actions/objects

**Step 5: Generate Task ID**
- Format: `{DEPT}-{NUM}`
- Department abbreviation: AI, DESIGN, DEV, LG, VIDEO
- Number: Sequential from 001, zero-padded

**Step 6: Create Task File**
- Generate filename from task ID and title slug
- Create markdown file with complete structure
- Populate all sections with extracted data
- Add source tracking information

---

## Data Mapping Rules

### Department Detection

**Priority Order:**
1. **Explicit Department Field:** Use `**Department:**` field if present
   - Handle comma-separated: "Design, Operations" → take first department
   - Handle slash-separated: "AI / LG" → take first department
2. **File Path:** Extract from source file path
   - Pattern: `Nov25/{Department}/...`
   - Departments: AI, Design, Dev, LG, Video
3. **Inference:** If neither available, infer from:
   - Owner's typical department
   - Related project context
   - Task content keywords

**Department Abbreviations:**
- AI → AI
- Design → DESIGN
- Dev → DEV
- LG → LG
- Video → VIDEO

### Priority Mapping

| Source Priority | Target Priority | Notes |
|----------------|-----------------|-------|
| CRITICAL | High | Critical tasks mapped to High priority |
| HIGH | High | Direct mapping |
| MEDIUM | Medium | Direct mapping |
| LOW | Low | Direct mapping |
| (missing) | Medium | Default if not specified |

### Status Mapping

| Source Status | Target Status | Notes |
|--------------|--------------|-------|
| Not Started | Not Started | Direct mapping |
| In Progress | In Progress | Direct mapping |
| Completed | Done | Completed → Done |
| Done | Done | Direct mapping |
| Waiting | Waiting | Direct mapping |
| Pending | Pending | Direct mapping |
| Open | Open | Direct mapping |
| (missing) | Not Started | Default if not specified |

### Action/Object Parsing

**Action Extraction:**
- Common action verbs (longer phrases first):
  - "Schedule & Organize", "Complete Technical Setup", "Create Video Tutorial"
  - "Process Video Transcriptions", "Update Video Transcription"
  - "Review and Optimize", "Review and Organize", "Review and Test"
  - "Create or Update", "Create New", "Complete Remaining"
  - "Create", "Update", "Complete", "Review", "Implement", "Develop"
  - "Design", "Process", "Document", "Schedule", "Distribute"
  - "Test", "Fix", "Optimize", "Monitor", "Research", "Analyze"
  - "Build", "Setup", "Configure", "Install", "Train", "Organize"
  - "Separate", "Upload", "Export", "Import", "Verify", "Finalize"
  - "Troubleshoot", "Resolve", "Coordinate", "Prepare", "Send"
  - "Add", "Remove", "Delete", "Edit", "Modify", "Generate"
  - "Extract", "Write", "Formulate", "Identify", "Port"
  - "Standardize", "Address", "Explore", "Investigate"

**Parsing Logic:**
1. Try to match longer action phrases first (sorted by length, descending)
2. If match found, extract action and remaining text as object
3. Remove common prefixes from object: `:`, ` -`, ` - `
4. If no match, default action: "Complete"
5. Remaining title becomes object

**Object Extraction:**
- Everything after the action verb
- Clean up prefixes and formatting
- Preserve key nouns and context
- Examples:
  - "Create Job Posting" → Action: "Create", Object: "Job Posting"
  - "Schedule & Organize Weekly Department Calls" → Action: "Schedule & Organize", Object: "Weekly Department Calls"
  - "Verify Marta Vereteno's Format Conversion Quality" → Action: "Verify", Object: "Marta Vereteno's Format Conversion Quality"

### Profession Inference

**Priority Order:**
1. **Explicit Profession Field:** Use if present in task metadata
2. **Owner Analysis:** Infer from owner name patterns:
   - "Project manager" or "PM" in owner → "Project manager"
   - "Designer" in owner → "Designer"
   - "Developer" or "Dev" in owner → "Developer"
   - "Lead generator" or "LG" in owner → "Lead generator"
   - "Video Editor" or "Video" in owner → "Video Editor"
3. **Department Default:** If department known:
   - Design → "Designer"
   - Dev → "Developer"
   - LG → "Lead generator"
   - Video → "Video Editor"
   - AI → "Project manager" or "AI Engineer"
4. **Default:** "Team member" if cannot determine

### Related Projects Extraction

**Sources:**
1. `**Related Project:**` field (single project)
2. `**Related Projects:**` field (multiple projects, comma-separated)
3. Context analysis (project names mentioned in description)
4. Department default projects (if applicable)

**Format:**
- Array of project names
- Clean project names (remove extra spaces, standardize capitalization)
- Examples: ["Game Academy", "CRM", "Lead Generation"]

### Tools Extraction

**Sources:**
1. `**Tools:**` field in task metadata
2. `**Resources:**` section
3. Step descriptions (tool mentions)
4. Context analysis

**Format:**
- Array of tool names
- Default: ["TBD"] if no tools identified
- Normalize tool names (remove versions, standardize capitalization)
- Examples: ["VS Code", "Claude", "Google Drive", "Figma"]

---

## Field Population Guidelines

### Header Section

**Fields:**
- `# {DEPT}-{NUM}: {Task Title}` - Task ID and full title
- `**Department:**` - Department name (full name, not abbreviation)
- `**Status:**` - Mapped status value
- `**Priority:**` - Mapped priority value
- `**Assignee:**` - Owner name(s) from source
- `**Date Created:**` - Extraction date (YYYY-MM-DD format)
- `**Timeline:**` - Timeline description from source

### Quick Info Section

**Fields:**
- `**Action:**` - Parsed action verb
- `**Object:**` - Parsed object name
- `**Tool:**` - Primary tool or "TBD"
- `**Related Projects:**` - Comma-separated project list or "None"

### Description Section

**Content:**
- Primary source: `**Context:**` field from source
- Secondary: Task description from title and metadata
- Format: Plain text paragraph(s)
- Preserve important details and background

### Full Template (YAML)

**Metadata Section:**
```yaml
metadata:
  status: {mapped_status}
  priority: {mapped_priority}
  created_date: '{YYYY-MM-DD}'
  extraction_date: '{YYYY-MM-DD}'
```

**Ownership Section:**
```yaml
ownership:
  department: {Department}
  assigned_to: {Employee Name}
  profession: {Profession or inferred}
```

**Taxonomy Section:**
```yaml
taxonomy:
  action: {Action verb}
  object: {Object name}
  object_type: Task
  context: {Department}-Department
```

**Dependencies Section:**
```yaml
dependencies:
  prerequisites: []  # Extract from Dependencies field if present
  related_tasks: []   # Extract task references if mentioned
  related_projects:   # Array of project names
  - {Project 1}
  - {Project 2}
```

**Deliverables Section:**
```yaml
deliverables:
- Complete: {Task Title}
```

**Source Tracking Section:**
```yaml
source_tracking:
  source_file: {Source file name}
  extraction_date: '{YYYY-MM-DD}'
  source_section: Task {number}
```

### Steps Section

**Format:**
```markdown
1. **{Step title}**
   - Description: {Step description}
   - Status: Not Started
```

**Extraction:**
- Extract from `**Steps:**` numbered list
- Each numbered item becomes a step
- Step title: First sentence or key phrase
- Description: Full step text
- Status: Default to "Not Started" for all steps

**Step Title Extraction:**
- Use first sentence of step if clear
- Extract key action if step is long
- Preserve important context (names, tools, locations)

### Tools Required Section

**Content:**
- List of tools from extraction
- Format: Bullet list
- Default: "- TBD" if no tools identified
- Include tools from multiple sources (Tools field, Resources, context)

### Notes Section

**Content:**
- Additional context from `**Context:**` field
- Instructions from `**Instructions:**` field
- Important details not captured elsewhere
- Format: Plain text paragraph(s)

### Source Tracking (Footer)

**Fields:**
- `**Source:**` - Source file name
- `**Date:**` - Extraction date (YYYY-MM-DD)

---

## Validation Criteria

### Required Fields Check

**Must Have:**
- ✅ Task ID (DEPT-NUM format)
- ✅ Task Title
- ✅ Department
- ✅ Status
- ✅ Priority
- ✅ Assignee
- ✅ Date Created
- ✅ Action (from taxonomy)
- ✅ Object (from taxonomy)
- ✅ Source tracking

**Should Have:**
- ⚠️ Profession (can infer if missing)
- ⚠️ Related Projects (can be empty array)
- ⚠️ Tools (can be "TBD")
- ⚠️ Steps (can be empty if no steps in source)
- ⚠️ Description/Context

### Data Format Validation

**Task ID Format:**
- Pattern: `{DEPT}-{NUM}` where DEPT is 2-6 uppercase letters, NUM is 3-digit zero-padded
- Examples: `AI-001`, `DESIGN-007`, `LG-142`
- Validation: Regex `^[A-Z]{2,6}-\d{3}$`

**Date Format:**
- Pattern: `YYYY-MM-DD`
- Examples: `2025-11-12`
- Validation: Valid date, not future dates

**Status Values:**
- Valid: Not Started, In Progress, Done, Waiting, Pending, Open
- Case-sensitive: Must match exactly

**Priority Values:**
- Valid: High, Medium, Low
- Case-sensitive: Must match exactly

**Department Names:**
- Valid: AI, Design, Dev, LG, Video
- Case-sensitive: Must match exactly

### Cross-Reference Validation

**Department Consistency:**
- Task ID department prefix matches ownership.department
- Department name matches file path department

**Profession Validation:**
- Profession should match department (if known)
- Profession should exist in LIBRARIES/Professions (if available)

**Tool Validation:**
- Tools should exist in LIBRARIES/Tools (if available)
- Tool names should be normalized

**Project Validation:**
- Projects should exist in TASK_MANAGERS/Projects (if available)
- Project names should be consistent

### Completeness Scoring

**Scoring Criteria:**
- **Complete (100%):** All required fields + all should-have fields + steps + tools + description
- **Good (80-99%):** All required fields + most should-have fields
- **Acceptable (60-79%):** All required fields + some should-have fields
- **Incomplete (<60%):** Missing required fields

**Field Weights:**
- Required fields: 10 points each (100 points total)
- Should-have fields: 5 points each (25 points total)
- Steps: 10 points (if present)
- Tools: 5 points (if not "TBD")
- Description: 10 points (if present)

---

## Output Format

### Individual Task Files

**Location:** `Entities/TASK_MANAGERS/Tasks/`

**File Structure:** See "Target Entity Structure" section above

**File Naming:** `{DEPT}-{NUM}_{Title_Slug}.md`

### Summary Report

**Location:** `Entities/TASK_MANAGERS/Tasks/EXTRACTION_SUMMARY.md`

**Content:**
- Total tasks extracted by department
- Task ID ranges
- Source file references
- Extraction date
- Status distribution
- Priority distribution
- Completeness statistics

---

## Quality Checklist

### Before Extraction

- [ ] Verify all source files exist and are accessible
- [ ] Review source file structure for consistency
- [ ] Confirm department abbreviations and naming conventions
- [ ] Prepare action verb library for parsing
- [ ] Set up output directory structure

### During Extraction

- [ ] Parse each task completely before moving to next
- [ ] Validate task ID format (DEPT-NUM)
- [ ] Verify department detection logic
- [ ] Check action/object parsing accuracy
- [ ] Ensure all metadata fields extracted
- [ ] Validate date formats
- [ ] Cross-reference department consistency

### After Extraction

- [ ] Review sample task files (5-10 per department)
- [ ] Validate YAML syntax in Full Template sections
- [ ] Check file naming consistency
- [ ] Verify source tracking accuracy
- [ ] Review completeness scores
- [ ] Generate extraction summary report
- [ ] Document any edge cases or issues encountered

### Validation Checklist

- [ ] All required fields present
- [ ] Task IDs are unique and sequential
- [ ] Department names consistent
- [ ] Status values valid
- [ ] Priority values valid
- [ ] Date formats correct
- [ ] YAML syntax valid
- [ ] File names follow convention
- [ ] Source tracking complete
- [ ] Steps extracted correctly
- [ ] Tools identified (or marked TBD)
- [ ] Related projects extracted

---

## Examples

### Example 1: Simple Task Extraction

**Source Task:**
```markdown
#### 7. Verify Marta Vereteno's Format Conversion Quality
- **Owner:** Skrypkar Vilhelm
- **Priority:** CRITICAL
- **Status:** Completed
- **Timeline:** Quality review completed
- **Related Project:** Game Academy Cover Production

**Context:** Marta completed 1280x720 format conversions. Quality review needed to verify all conversions meet specifications.

**Steps:**
1. Access Marta's completed 1280x720 conversions in Google Drive folder
2. Count total number of conversions completed vs. expected
3. Systematic quality review: dimensions, background extension, text space suitability
4. Create review summary with findings
5. If issues found, categorize by severity and determine fixes needed
6. Update project status and tracking documentation
```

**Extracted Task File:**
```markdown
# DESIGN-007: Verify Marta Vereteno's Format Conversion Quality

**Department:** Design
**Status:** Done
**Priority:** High
**Assignee:** Skrypkar Vilhelm
**Date Created:** November 12, 2025
**Timeline:** Quality review completed

---

## Quick Info

- **Action:** Verify
- **Object:** Marta Vereteno's Format Conversion Quality
- **Tool:** TBD
- **Related Projects:** Game Academy

---

## Description

Marta completed 1280x720 format conversions. Quality review needed to verify all conversions meet specifications.

## Full Template

```yaml
task_id: DESIGN-007
task_name: Verify Marta Vereteno's Format Conversion Quality
metadata:
  status: Done
  priority: High
  created_date: '2025-11-12'
  extraction_date: '2025-11-12'
ownership:
  department: Design
  assigned_to: Skrypkar Vilhelm
  profession: Team member
taxonomy:
  action: Verify
  object: Marta Vereteno's Format Conversion Quality
  object_type: Task
  context: Design-Department
dependencies:
  prerequisites: []
  related_tasks: []
  related_projects:
  - Game Academy
deliverables:
- Complete: Verify Marta Vereteno's Format Conversion Quality
source_tracking:
  source_file: Design Department Tasks - November 2025.md
  extraction_date: '2025-11-12'
  source_section: Task 7
```

---

## Steps

1. **Access Marta's completed 1280x720 conversions in Google Drive folder**
   - Description: Access Marta's completed 1280x720 conversions in Google Drive folder
   - Status: Not Started

2. **Count total number of conversions completed vs. expected**
   - Description: Count total number of conversions completed vs. expected
   - Status: Not Started

3. **Systematic quality review: dimensions, background extension, text space suitability**
   - Description: Systematic quality review: dimensions, background extension, text space suitability
   - Status: Not Started

4. **Create review summary with findings**
   - Description: Create review summary with findings
   - Status: Not Started

5. **If issues found, categorize by severity and determine fixes needed**
   - Description: If issues found, categorize by severity and determine fixes needed
   - Status: Not Started

6. **Update project status and tracking documentation**
   - Description: Update project status and tracking documentation
   - Status: Not Started

## Tools Required

- TBD

## Notes

Marta completed 1280x720 format conversions. Quality review needed to verify all conversions meet specifications.

---

**Source:** Design Department Tasks - November 2025.md
**Date:** 2025-11-12
```

### Example 2: Complex Task with Multiple Departments

**Source Task:**
```markdown
#### 1. Complete Technical Setup for All Design Team Members
- **Owner:** Artemchuk Nikolay (Setup Support), Each Design Team Member (Individual Setup)
- **Department:** Design, AI
- **Profession:** All UI/UX Designers, Graphic Designers, Illustrators
- **Timeline:** Before end of week
- **Status:** In Progress (Yuliia completed ✓, Hlushko Mariia and others pending)
- **Dependencies:** AI account access for Claude authentication, Git Bash installation
- **Related Project:** Daily Workflow Automation
- **Tools:** VS Code, Claude Code extension, Cursor, Git Bash, Whisper Flow, AI Claude account

**Context:** Design call on November 4th successfully onboarded the team. Yuliia (Chobotar Yuliia) completed full setup during the call and tested the workflow. Remaining team members (Marta, Olena, Tatyana, and 5 others) need to complete their individual setups.

**Steps:**
1. Each designer downloads and installs VS Code or Cursor
2. Install Claude Code extension (official from Anthropic)
3. Coordinate with Kovalska Anastasiya for AI account 2FA access (via iPad)
...
```

**Extracted Task File:**
```markdown
# DESIGN-008: Complete Technical Setup for All Design Team Members

**Department:** Design
**Status:** In Progress
**Priority:** High
**Assignee:** Artemchuk Nikolay (Setup Support), Each Design Team Member (Individual Setup)
**Date Created:** November 12, 2025
**Timeline:** Before end of week

---

## Quick Info

- **Action:** Complete Technical Setup
- **Object:** All Design Team Members
- **Tool:** VS Code, Claude Code extension, Cursor, Git Bash, Whisper Flow
- **Related Projects:** Daily Workflow Automation

---

## Description

Design call on November 4th successfully onboarded the team. Yuliia (Chobotar Yuliia) completed full setup during the call and tested the workflow. Remaining team members (Marta, Olena, Tatyana, and 5 others) need to complete their individual setups.

## Full Template

```yaml
task_id: DESIGN-008
task_name: Complete Technical Setup for All Design Team Members
metadata:
  status: In Progress
  priority: High
  created_date: '2025-11-12'
  extraction_date: '2025-11-12'
ownership:
  department: Design
  assigned_to: Artemchuk Nikolay (Setup Support), Each Design Team Member (Individual Setup)
  profession: Designer
taxonomy:
  action: Complete Technical Setup
  object: All Design Team Members
  object_type: Task
  context: Design-Department
dependencies:
  prerequisites:
  - AI account access for Claude authentication
  - Git Bash installation
  related_tasks: []
  related_projects:
  - Daily Workflow Automation
deliverables:
- Complete: Complete Technical Setup for All Design Team Members
source_tracking:
  source_file: Design Department Tasks - November 2025.md
  extraction_date: '2025-11-12'
  source_section: Task 1
```

---

## Steps

[Steps extracted from source...]

## Tools Required

- VS Code
- Claude Code extension
- Cursor
- Git Bash
- Whisper Flow
- AI Claude account

## Notes

Design call on November 4th successfully onboarded the team. Yuliia (Chobotar Yuliia) completed full setup during the call and tested the workflow. Remaining team members (Marta, Olena, Tatyana, and 5 others) need to complete their individual setups.

---

**Source:** Design Department Tasks - November 2025.md
**Date:** 2025-11-12
```

---

## Edge Cases and Special Handling

### Multiple Owners

**Source:** `- **Owner:** Name1, Name2, Name3`

**Handling:**
- Keep all names in `assigned_to` field
- Use first owner for profession inference if needed
- Note multiple owners in description if significant

### Multiple Departments

**Source:** `- **Department:** Design, Operations`

**Handling:**
- Take first department for primary assignment
- Note other departments in description or notes
- Use first department for task ID prefix

### Missing Metadata

**Handling:**
- Status: Default to "Not Started"
- Priority: Default to "Medium"
- Timeline: Use "TBD" or leave empty
- Profession: Infer from owner or department
- Tools: Use "TBD"

### Complex Action Phrases

**Examples:**
- "Schedule & Organize" → Keep as compound action
- "Review and Optimize" → Keep as compound action
- "Create or Update" → Keep as compound action

**Handling:**
- Match longer phrases first
- Preserve compound actions when they represent single logical action
- Split only if clearly two separate actions

### Special Characters in Titles

**Handling:**
- Preserve in task title
- Sanitize for filename slug (remove/replace special chars)
- Examples:
  - "Verify Marta Vereteno's Format Conversion Quality" → `Verify_Marta_Vereteno's_Format_Conversion_Quality`
  - "Research Lead Generation Strategies & Performance Analytics" → `Research_Lead_Generation_Strategies_&_Performance_Analytics`

### Empty Steps Section

**Handling:**
- If no steps in source, create empty Steps section
- Or omit Steps section entirely
- Note in description if task has no defined steps

### Tool Extraction from Context

**Patterns to Look For:**
- "using [Tool]"
- "with [Tool]"
- "via [Tool]"
- "in [Platform]"
- "on [Platform]"

**Handling:**
- Extract tool names from context descriptions
- Add to Tools Required section
- Normalize tool names

---

## Integration Points

### TASK_MANAGERS Entity Relationships

**Tasks → Task Templates:**
- Tasks may reference Task Templates if similar patterns exist
- Link tasks to templates for reusability tracking

**Tasks → Projects:**
- Link tasks to projects via `related_projects` field
- Projects defined in `TASK_MANAGERS/Projects/`

**Tasks → Steps:**
- Tasks contain steps (embedded in task file)
- Steps may reference Step Templates if patterns exist

**Tasks → LIBRARIES:**
- Actions from `LIBRARIES/Responsibilities/Actions/`
- Objects from `LIBRARIES/Responsibilities/Objects/`
- Tools from `LIBRARIES/Tools/`
- Professions from `LIBRARIES/Professions/`

### Taxonomy Compliance

**Action Standardization:**
- Map parsed actions to standard actions in Responsibilities/Responsibilities/Actions library
- Use exact action names from library when possible
- Document new actions if discovered

**Object Standardization:**
- Map parsed objects to standard objects in Responsibilities/Responsibilities/Objects library
- Use exact object names from library when possible
- Document new objects if discovered

**Tool Standardization:**
- Map tool names to tools in Tools library
- Use tool IDs when available
- Document new tools if discovered

---

## Execution Workflow

### Step-by-Step Process

**1. Prepare Environment**
```bash
# Set source directory
SOURCE_DIR="Dropbox/Nov25"

# Set output directory
OUTPUT_DIR="Dropbox/Entities/TASK_MANAGERS/Tasks"

# Load department files
DEPARTMENT_FILES=(
  "AI/AI Department Tasks - November 2025.md"
  "Design/Design Department Tasks - November 2025.md"
  "Dev/Dev Department Tasks - November 2025.md"
  "LG/LG Department Tasks - November 2025.md"
  "Video/Video Department Tasks - November 2025.md"
)
```

**2. For Each Department File:**
```bash
FOR each department_file in DEPARTMENT_FILES:
  - Read file content
  - Identify department from path
  - Extract all tasks (#### pattern)
  - Initialize task counter (001)
  
  FOR each task:
    - Extract metadata
    - Parse action/object
    - Extract steps
    - Extract tools
    - Generate task ID
    - Create task file
    - Increment task counter
```

**3. Generate Summary Report**
```bash
# Compile statistics
- Total tasks per department
- Task ID ranges
- Status distribution
- Priority distribution
- Completeness scores

# Create EXTRACTION_SUMMARY.md
```

**4. Validation Pass**
```bash
FOR each task_file in OUTPUT_DIR:
  - Validate required fields
  - Check YAML syntax
  - Verify task ID format
  - Validate cross-references
  - Calculate completeness score
  - Flag issues for review
```

**5. Quality Review**
```bash
# Review sample files (5-10 per department)
# Check edge cases
# Verify data accuracy
# Document any issues
```

---

## Output File Locations

### Primary Output
**Task Files:** `Dropbox/Entities/TASK_MANAGERS/Tasks/{DEPT}-{NUM}_{Title}.md`

### Supporting Files
**Extraction Summary:** `Dropbox/Entities/TASK_MANAGERS/Tasks/EXTRACTION_SUMMARY.md`
- Task counts by department
- Task ID ranges
- Source file references
- Extraction statistics

**Validation Log:** `Dropbox/Entities/TASK_MANAGERS/Tasks/VALIDATION_LOG_{DATE}.md` (optional)
- Validation results
- Issues found
- Completeness scores
- Recommendations

---

## Maintenance and Updates

### When to Re-run Extraction

**Triggers:**
- New department task files created
- Updates to existing department task files
- Changes to task structure requirements
- Taxonomy library updates requiring re-mapping

### Update Frequency

**Recommended:**
- Initial extraction: Complete all departments
- Incremental updates: As new tasks added to department files
- Full re-extraction: Monthly or when structure changes

### Version Control

**Tracking:**
- Document extraction date in each task file
- Maintain extraction summary with version info
- Track changes to extraction logic
- Document edge cases and special handling

---

## Notes

### Important Context

- **316 tasks** extracted from 5 department files (November 2025)
- Task files use markdown format with embedded YAML template
- All tasks include source tracking for traceability
- Action/Object parsing uses pattern matching with fallback defaults
- Department detection prioritizes explicit field over path inference

### Process Improvements

**Future Enhancements:**
- Automated tool matching to LIBRARIES/Tools
- Automated action/object matching to LIBRARIES/Actions and LIBRARIES/Objects
- Cross-reference validation against all entity libraries
- Automated completeness scoring
- Integration with Task Template matching

### Known Limitations

- Tool extraction may miss tools mentioned only in step descriptions
- Action/Object parsing may not handle all title variations
- Profession inference may be inaccurate for cross-department tasks
- Related tasks extraction requires manual review for accuracy

---

*Last Updated: 2025-11-12*
*Next Scheduled Run: As needed when new tasks added*

