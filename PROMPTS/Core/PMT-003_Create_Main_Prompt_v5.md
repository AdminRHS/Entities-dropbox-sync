# META-PROMPT: Create MAIN_PROMPT v5 with Enhanced Modular Architecture

**Purpose:** This prompt guides AI through creating MAIN_PROMPT v5 by systematically building a modular folder structure and updating architecture and data details for each module based on the comprehensive LIBRARIES system.

**Target Output:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts\Core\MAIN_PROMPT_v5_Modular\`

**Source Reference:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts\Core\MAIN_PROMPT_v4.md`

**Library Location:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\`

---

## OVERVIEW: What You Will Create

You will create MAIN_PROMPT v5 as a modular system consisting of approximately 50 individual markdown files organized into 5 main folders. Each module will be enhanced with detailed integration to the 12 LIBRARIES entities, updated statistics, and improved cross-referencing.

### Key Improvements in v5:
- **Granular Modularity:** 21 output templates as individual files (vs. 2 large files in v4)
- **Library-Specific Modules:** 12 dedicated integration files (one per library entity)
- **Enhanced Data:** Current statistics from actual library files (429 actions, 10,596 parameters, etc.)
- **Better Maintainability:** Smaller, focused files that can be updated independently
- **Assembly System:** Scripts to generate monolithic version when needed

---

## PHASE 1: FOLDER STRUCTURE CREATION

### Step 1.1: Create Root Folder and README

**Action:** Create the main modular folder with overview documentation

**Location:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts\Core\MAIN_PROMPT_v5_Modular\`

**Files to Create:**
1. `README.md` - Overview, folder structure, assembly instructions
2. `.gitkeep` files in each subfolder

**Content for README.md:**
```markdown
# MAIN_PROMPT v5 - Modular Architecture

## Overview
MAIN_PROMPT v5 is the master prompt for AI-assisted call organization, meeting analysis, and taxonomy-driven documentation at Remote Helpers.

**Version:** 5.0
**Last Updated:** [Current Date]
**Modular Files:** ~50 files across 5 folders
**Total Libraries Integrated:** 12

## Folder Structure

### 00_Core/
Company context, employee directory, project directory, and core AI instructions.
- 5 files
- Updates: Monthly (employees), Weekly (projects)

### 01_Library_Integration/
Individual integration modules for each of the 12 LIBRARIES entities.
- 13 files (12 libraries + README)
- Contains recognition patterns, matching rules, cross-references

### 02_Output_Templates/
21 individual section templates for meeting output.
- 22 files (21 templates + README)
- Each template includes relevant library integrations

### 03_Processing_Rules/
Entity recognition patterns and processing guidelines.
- 6 files
- Language handling, participant ID, project recognition

### 04_Usage/
Usage instructions, examples, tips, and maintenance guides.
- 6 files
- Includes version history and changelog

## Assembly Instructions

### To Create Monolithic Version:
```bash
python assemble_full_prompt.py
```

### To Create Department-Specific Version:
```bash
python assemble_department.py --dept AI
```

## Library Statistics (Current)
- **Actions:** 429 actions
- **Objects:** 36 objects (4 collections)
- **Processes:** 428 processes
- **Results:** 432 results
- **Skills:** 12+ skills
- **Responsibilities:** Multiple across departments
- **Products:** 39 products
- **Services:** 7 categories
- **Parameters:** 10,596+ parameters
- **Professions:** 12+ professions
- **Tools:** 75+ tools
- **Prompts:** Multiple categories

## Quick Start
1. Read files in numerical order (00, 01, 02, etc.)
2. Start with Core files to understand context
3. Review Library Integration for entity recognition
4. Reference Output Templates for formatting
5. Use Processing Rules for recognition patterns

## Maintenance
- Update employee directory monthly
- Update project directory weekly
- Sync library statistics when LIBRARIES are updated
- Update version history in `04_Usage/06_CHANGELOG.md`

## Migration from v4
See `04_Usage/07_Migration_Guide.md` for differences and upgrade path.
```

### Step 1.2: Create Folder Structure

**Action:** Create all 5 main folders and their subfolders

**Folders to Create:**
```
MAIN_PROMPT_v5_Modular/
├── 00_Core/
├── 01_Library_Integration/
├── 02_Output_Templates/
├── 03_Processing_Rules/
├── 04_Usage/
└── scripts/
```

---

## PHASE 2: CORE MODULES (Folder 00_Core/)

### Step 2.1: Purpose and Vision
**File:** `00_Core/01_Purpose_Vision.md`

**Action:** Extract and enhance purpose section from MAIN_PROMPT_v4.md

**Key Sections:**
1. AI-First Organization Vision
2. Role of AI as Call Organizer
3. Mission Statement
4. Core Principles
5. Integration Philosophy

**Enhancement:** Add vision for how 12 LIBRARIES work together

### Step 2.2: Company Context
**File:** `00_Core/02_Company_Context.md`

**Action:** Extract company context from MAIN_PROMPT_v4.md

**Key Data to Include:**
- 7 Departments (HR, AI, Video, Sales, Design, Dev, LG)
- 32 Employees
- Platforms used
- Operating systems
- Company structure
- Organizational hierarchy

### Step 2.3: Employee Directory
**File:** `00_Core/03_Employee_Directory.md`

**Action:** Extract full employee directory from MAIN_PROMPT_v4.md (Section 3)

**Format:**
```markdown
## Employee Directory (32 Employees)

### Department: HR (5 employees)
| ID | Name | Role | Platforms | OS | Projects |
|----|------|------|-----------|-----|----------|
| ALX | Alex | CEO | All | macOS | All |
...

### Department: AI (8 employees)
...
```

**Enhancement:** Add cross-reference to Professions library

### Step 2.4: Project Directory
**File:** `00_Core/04_Project_Directory.md`

**Action:** Extract project directory from MAIN_PROMPT_v4.md (Section 4)

**Format:**
```markdown
## Project Directory (31+ Active Projects)

### Project Categories:
1. AI & Automation Projects
2. Video Projects
3. Lead Generation Projects
4. Design Projects
5. Development Projects

### Full Project List:
| Abbreviation | Full Name | Keywords | Department | Status |
|--------------|-----------|----------|------------|--------|
| APIP | AI Prompt Improvement Project | prompts, AI, optimization | AI | Active |
...
```

**Enhancement:** Add status field, department mapping

### Step 2.5: Core AI Instructions
**File:** `00_Core/05_AI_Instructions.md`

**Action:** Create concise AI instruction set

**Key Content:**
- How to process meeting transcripts
- How to recognize entities from LIBRARIES
- How to apply taxonomy framework
- Priority order for processing
- Quality standards

---

## PHASE 3: LIBRARY INTEGRATION MODULES (Folder 01_Library_Integration/)

**Overview:** Create 12 individual files, one for each LIBRARIES entity, plus a README.

### Step 3.1: Library Integration README
**File:** `01_Library_Integration/README.md`

**Content:**
- Overview of 12 LIBRARIES
- Relationship diagram
- Integration philosophy
- How libraries work together
- ID format conventions

### Step 3.2-3.13: Individual Library Modules

For EACH of the 12 libraries, create a dedicated integration file following this template:

#### Template Structure for Each Library File:

```markdown
# [LIBRARY NAME] Library Integration

**Library Path:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\[Library]/`
**Total [Entities]:** [Current Count]
**ID Format:** `[PREFIX]-XXX`
**Last Updated:** [Date from library files]

---

## 1. PURPOSE

[What this library represents and why it's important]

---

## 2. LIBRARY STATISTICS

**Total Files:** [Count]
**Total [Entities]:** [Count]
**Categories:** [List categories if applicable]

### File Breakdown:
- `[File1.json]` - [Count] [entities]
- `[File2.json]` - [Count] [entities]
...

---

## 3. RECOGNITION RULES

### Primary Recognition Patterns:
1. **[Pattern Type 1]:** [Description and examples]
2. **[Pattern Type 2]:** [Description and examples]
3. **[Pattern Type 3]:** [Description and examples]

### Keywords to Match:
- [Keyword 1]
- [Keyword 2]
- [Keyword 3]
...

### Context Clues:
- [Context 1]
- [Context 2]
...

---

## 4. MATCHING EXAMPLES

### Example 1: High Confidence Match
**Transcript Phrase:** "[Example phrase]"
**Matched [Entity]:** `[ID]` - [Name]
**Confidence:** High
**Reasoning:** [Why this match was made]

### Example 2: Medium Confidence Match
**Transcript Phrase:** "[Example phrase]"
**Matched [Entity]:** `[ID]` - [Name]
**Confidence:** Medium
**Reasoning:** [Why this match was made]

### Example 3: Context-Based Match
**Transcript Phrase:** "[Example phrase]"
**Context:** [Department/Project/Employee]
**Matched [Entity]:** `[ID]` - [Name]
**Confidence:** High
**Reasoning:** [Why context helped]

---

## 5. CROSS-REFERENCES

### Relationships to Other Libraries:

**Primary Relationships:**
- **[Library 1]:** [How they connect]
- **[Library 2]:** [How they connect]

**Secondary Relationships:**
- **[Library 3]:** [How they connect]

### Integration Patterns:
1. [Pattern 1]: [Description]
2. [Pattern 2]: [Description]

---

## 6. OUTPUT INTEGRATION

### Sections That Use This Library:
1. **[Section Name]** - [How library is used]
2. **[Section Name]** - [How library is used]

### Output Format:
```markdown
**[Entity Type]:** `[ID]` - [Name]
- **Category:** [Category if applicable]
- **Related [Other Entity]:** `[ID]`
- **Context:** [Additional context]
```

---

## 7. VALIDATION CHECKLIST

When identifying [entities] from transcripts:
- [ ] Check for primary keywords
- [ ] Verify context matches
- [ ] Confirm department alignment
- [ ] Check for related entities
- [ ] Validate against project context
- [ ] Assign confidence level
- [ ] Add source reference

---

## 8. SAMPLE DATA

### Top 10 Most Common [Entities]:
1. `[ID-001]` - [Name] - [Description]
2. `[ID-002]` - [Name] - [Description]
...

### Department-Specific [Entities]:

#### [Department 1]:
- `[ID]` - [Name]
- `[ID]` - [Name]

#### [Department 2]:
- `[ID]` - [Name]
- `[ID]` - [Name]

---

## 9. USAGE NOTES

**Best Practices:**
- [Practice 1]
- [Practice 2]

**Common Pitfalls:**
- [Pitfall 1]: [How to avoid]
- [Pitfall 2]: [How to avoid]

**Update Frequency:**
- Check library for updates: [Frequency]
- Sync statistics: [When]
```

---

### Specific Instructions for Each Library:

#### 01_Actions_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions\`
- Total: 429 actions
- ID Format: `ACTION-XXX`
- Include Data_Operations breakdown (12 files)
- Reference Video_Generation_Actions.json
- Cross-reference: Processes, Results, Objects

#### 02_Objects_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects\`
- Total: 36 objects in 4 collections
- ID Format: `OBJ-XXX`
- Include all object categories (Agentic, AI, Design, Documents, etc.)
- Cross-reference: Actions (creates Action+Object=Task), Processes

#### 03_Processes_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Processes\`
- Total: 428 processes
- ID Format: `PROCESS-XXX`
- Include Workflows breakdown (27 workflows)
- Cross-reference: Actions, Results, Steps

#### 04_Results_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Results\`
- Total: 432 results
- ID Format: `RESULT-XXX`
- Cross-reference: Processes, Actions, Outcomes

#### 05_Skills_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Skills\`
- Total: 12+ skills
- ID Format: `SKL-XXX`
- Department-specific breakdown (AI, DEV, LG, AI)
- Cross-reference: Responsibilities, Professions, Actions

#### 06_Responsibilities_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities\`
- ID Format: `RESP-XXX`
- Formula: Responsibility = Action + Object
- Cross-reference: Actions, Objects, Professions, Skills

#### 07_Products_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\BUSINESSES\Products\`
- Total: 39 products
- ID Format: `PDT-XXXX`
- Include Products_Index structure
- Cross-reference: Services, Projects

#### 08_Services_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\BUSINESSES\Services\`
- Total: 7 categories
- ID Format: `SVC-XXX`
- Categories: Content, Design, Lead Gen, AI, SEO, Technical, Video
- Cross-reference: Products, Professions

#### 09_Parameters_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Parameters\`
- Total: 10,596+ parameters
- ID Format: `PARAM-XXX`
- Include organized_by_department structure
- Include organized_by_profession structure
- Cross-reference: All libraries (parameters are universal)

#### 10_Professions_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Professions\`
- Total: 12+ professions
- ID Format: `PROF-XXX`
- Include all profession files (Lead_Generator, SDR, Backend_Developer, etc.)
- Cross-reference: Skills, Responsibilities, Tools, Departments

#### 11_Tools_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Tools\`
- Total: 75+ tools
- ID Format: `TOOL-XXX`
- Categories: AI Tools (21), Development (18), Databases (7), Cloud (3), etc.
- Cross-reference: Professions, Skills, Processes

#### 12_Prompts_Library.md
**Source:** Read `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Prompts\`
- ID Format: `PROMPT-XXX`
- Categories: Core, Daily_Reports, Video_Processing, Library_Processing, etc.
- Cross-reference: Processes, Workflows, Tasks

#### 13_Taxonomy_Framework.md
**Action:** Extract Section 22 from MAIN_PROMPT_v4.md
- Overview of entire taxonomy system
- How all 12 libraries interconnect
- Master relationship diagram
- System architecture

---

## PHASE 4: OUTPUT TEMPLATES (Folder 02_Output_Templates/)

**Overview:** Create 21 individual template files (one for each output section) plus README.

### Step 4.1: Output Templates README
**File:** `02_Output_Templates/README.md`

**Content:**
- Overview of 21 sections
- Order of sections
- Which libraries integrate with which sections
- Output format standards

### Step 4.2-4.22: Individual Template Files

For EACH of the 21 output sections, create a template file:

#### Template Structure:

```markdown
# [SECTION NUMBER]. [SECTION NAME]

**Purpose:** [What this section captures]
**Integrated Libraries:** [List libraries used in this section]
**Output Format:** Markdown
**Priority:** [High/Medium/Low]

---

## SECTION OVERVIEW

[Description of what this section should contain and why it's important]

---

## INTEGRATED LIBRARIES

### Primary Libraries:
1. **[Library 1]** (`[ID-FORMAT]`) - [How used]
2. **[Library 2]** (`[ID-FORMAT]`) - [How used]

### Secondary Libraries:
1. **[Library 3]** (`[ID-FORMAT]`) - [How used]

---

## OUTPUT TEMPLATE

```markdown
## [SECTION NUMBER]. [SECTION NAME]

[Section-specific template with placeholders for library entities]

### [Subsection 1]
**[Entity Type]:** `[ID]` - [Name]
- **[Attribute 1]:** [Value]
- **[Attribute 2]:** [Value]
- **Related [Other Entity]:** `[Related-ID]`

### [Subsection 2]
...
```

---

## RECOGNITION RULES

### What to Look For:
1. [Pattern 1]
2. [Pattern 2]
3. [Pattern 3]

### Keywords:
- [Keyword 1]
- [Keyword 2]

---

## EXAMPLES

### Example 1: [Scenario]
**Transcript Excerpt:**
"[Sample transcript text]"

**Generated Output:**
```markdown
## [SECTION]. [NAME]

[Filled template based on transcript]
```

**Entities Identified:**
- `[ID-001]` - [Entity Name] from [Library]
- `[ID-002]` - [Entity Name] from [Library]

---

## VALIDATION CHECKLIST

- [ ] All relevant [entities] identified
- [ ] Confidence levels assigned
- [ ] Cross-references added
- [ ] Context verified
- [ ] Format matches template
- [ ] IDs are valid

---

## NOTES

**Special Considerations:**
- [Note 1]
- [Note 2]

**Common Issues:**
- [Issue 1]: [Solution]
- [Issue 2]: [Solution]
```

---

### Specific Files to Create:

1. **01_Meeting_Metadata.md** - Participants, projects, departments (no library integration)
2. **02_Executive_Summary.md** - High-level overview (minimal library integration)
3. **03_Action_Items_Tasks.md** - **INTEGRATED:** Actions, Objects, Skills, Responsibilities
4. **04_Projects_Features.md** - **INTEGRATED:** Products, Services
5. **05_Workflows_Processes.md** - **INTEGRATED:** Processes, Results, Steps
6. **06_Rules_Best_Practices.md** - **INTEGRATED:** Parameters
7. **07_Problems_Solutions.md** - Minimal integration
8. **08_Tools_Resources.md** - **INTEGRATED:** Tools
9. **09_Technical_Architecture.md** - **INTEGRATED:** Tools, Processes
10. **10_Decisions_Log.md** - Minimal integration
11. **11_Documentation_Gaps.md** - Minimal integration
12. **12_Communication_Announcements.md** - Minimal integration
13. **13_Blockers_Dependencies.md** - **INTEGRATED:** Processes, Results
14. **14_Insights_Lessons.md** - Minimal integration
15. **15_Analogies_Frameworks.md** - Minimal integration
16. **16_Employee_Team_Context.md** - **INTEGRATED:** Professions, Skills, Responsibilities
17. **17_Lead_Gen_Sales_Context.md** - **INTEGRATED:** Services, Products, Processes (LG-specific)
18. **18_Design_Creative_Context.md** - **INTEGRATED:** Objects, Products, Tools (Design-specific)
19. **19_Development_Technical_Context.md** - **INTEGRATED:** Tools, Processes, Objects (Dev-specific)
20. **20_Onboarding_Training_Context.md** - **INTEGRATED:** Skills, Responsibilities, Professions
21. **21_Follow_Up_Items.md** - **INTEGRATED:** Actions, Tasks

---

## PHASE 5: PROCESSING RULES (Folder 03_Processing_Rules/)

**Overview:** Create 6 files for entity recognition and processing logic.

### Step 5.1: Processing Rules README
**File:** `03_Processing_Rules/README.md`

**Content:**
- Overview of processing workflow
- Order of operations
- Priority system
- Error handling

### Step 5.2: Participant Identification
**File:** `03_Processing_Rules/01_Participant_Identification.md`

**Action:** Extract from Section "Processing Guidelines" in MAIN_PROMPT_v4.md

**Content:**
- How to identify participants from transcripts
- Name variations handling
- Employee ID assignment
- Department detection
- Cross-reference with Employee Directory

### Step 5.3: Project Recognition
**File:** `03_Processing_Rules/02_Project_Recognition.md`

**Content:**
- Project keyword matching
- Abbreviation detection
- Project name variations
- Cross-reference with Project Directory
- Multi-project discussions

### Step 5.4: Entity Recognition Patterns
**File:** `03_Processing_Rules/03_Entity_Recognition.md`

**Content:**
- Master recognition workflow
- How to identify entities from all 12 libraries
- Confidence level assignment (High/Medium/Low)
- Context-based recognition
- Ambiguity resolution
- Entity validation

### Step 5.5: Language Handling
**File:** `03_Processing_Rules/04_Language_Handling.md`

**Content:**
- Multi-language support
- Translation rules
- Language detection
- Cultural context preservation

### Step 5.6: Vocabulary Recognition
**File:** `03_Processing_Rules/05_Vocabulary_Recognition.md`

**Content:**
- Industry-specific terminology
- Company-specific vocabulary
- Acronym expansion
- Synonym handling
- Domain-specific language patterns

### Step 5.7: Cross-Reference Rules
**File:** `03_Processing_Rules/06_Cross_Reference_Rules.md`

**Content:**
- How to create cross-references between entities
- Relationship validation
- Bidirectional linking
- Confidence scoring for relationships
- Reference format standards

---

## PHASE 6: USAGE & MAINTENANCE (Folder 04_Usage/)

**Overview:** Create 6 files for instructions, examples, and maintenance.

### Step 6.1: Usage Instructions
**File:** `04_Usage/01_Usage_Instructions.md`

**Action:** Extract and enhance from MAIN_PROMPT_v4.md

**Content:**
- Step-by-step workflow
- How to process a transcript
- How to generate output
- Quality checks
- Troubleshooting

### Step 6.2: Examples
**File:** `04_Usage/02_Examples.md`

**Content:**
- Full example: Transcript → Output
- Annotated examples showing entity recognition
- Multiple scenarios (AI meeting, Sales meeting, Design review, etc.)
- Edge cases

### Step 6.3: Tips and Best Practices
**File:** `04_Usage/03_Tips_Best_Practices.md`

**Action:** Extract from MAIN_PROMPT_v4.md

**Content:**
- Best practices for accuracy
- How to improve recognition
- Common mistakes to avoid
- Optimization tips

### Step 6.4: Advanced Features
**File:** `04_Usage/04_Advanced_Features.md`

**Content:**
- Multi-language processing
- Batch processing
- Custom library integration
- Advanced cross-referencing
- Department-specific configurations

### Step 6.5: Maintenance Guide
**File:** `04_Usage/05_Maintenance_Guide.md`

**Content:**
- How to update employee directory
- How to update project directory
- How to sync library statistics
- How to add new libraries
- Version control best practices
- Testing procedures

### Step 6.6: Changelog
**File:** `04_Usage/06_CHANGELOG.md`

**Content:**
```markdown
# MAIN_PROMPT Version History

## Version 5.0 (2025-XX-XX)

### Major Changes:
- **Modular Architecture:** Split into ~50 individual files across 5 folders
- **Library Integration:** 12 dedicated library integration modules
- **Granular Templates:** 21 individual output template files
- **Enhanced Statistics:** Current data from all libraries (429 actions, 10,596 parameters, etc.)

### New Files:
- Added 01_Library_Integration/ folder with 13 files
- Split 02_Output_Templates/ into 22 individual files
- Added 03_Processing_Rules/ folder with 6 files
- Created assembly system

### Improvements:
- Better maintainability with smaller, focused files
- Easier updates to individual components
- Enhanced cross-referencing between libraries
- Clearer separation of concerns

### Migration from v4:
- All v4 functionality preserved
- New modular structure for easier maintenance
- Can generate monolithic version for backward compatibility

## Version 4.0 (2025-01-27)

[Extract from MAIN_PROMPT_v4.md Version History]

## Version 3.0
...

## Version 2.0
...

## Version 1.0
...
```

### Step 6.7: Migration Guide
**File:** `04_Usage/07_Migration_Guide.md`

**Content:**
- Differences between v4 and v5
- How to migrate from v4 to v5
- Compatibility notes
- Feature mapping (v4 → v5)

---

## PHASE 7: ASSEMBLY SYSTEM (Folder scripts/)

**Overview:** Create Python scripts to assemble modular files into monolithic versions.

### Step 7.1: Full Assembly Script
**File:** `scripts/assemble_full_prompt.py`

**Purpose:** Combine all modular files into single `MAIN_PROMPT_v5.md`

**Functionality:**
- Read all files from 5 folders in order
- Combine into single markdown file
- Add table of contents
- Add navigation links
- Generate metadata (file count, total size, last updated)
- Output to `../MAIN_PROMPT_v5.md`

### Step 7.2: Department-Specific Assembly
**File:** `scripts/assemble_department.py`

**Purpose:** Create department-specific versions

**Functionality:**
- Accept `--dept` parameter (AI, Video, LG, Sales, Design, Dev, HR)
- Include only relevant libraries and templates
- Filter examples to department context
- Output to `../MAIN_PROMPT_v5_[DEPT].md`

### Step 7.3: Lightweight Assembly
**File:** `scripts/assemble_lightweight.py`

**Purpose:** Create minimal version without extensive examples

**Functionality:**
- Include core + templates only
- Exclude detailed examples
- Exclude full library statistics
- Smaller file for quick reference

### Step 7.4: Assembly README
**File:** `scripts/README.md`

**Content:**
- How to use assembly scripts
- Parameters and options
- Output locations
- Customization guide

---

## PHASE 8: FINAL ASSEMBLY & VALIDATION

### Step 8.1: Generate Monolithic Version
**Action:** Run assembly script to create `MAIN_PROMPT_v5.md`

**Output:** Single comprehensive file combining all modules

### Step 8.2: Statistics Update
**Action:** Scan all library files and update statistics throughout v5 files

**Update in:**
- Root README.md
- 01_Library_Integration/README.md
- Each library integration file
- CHANGELOG.md

### Step 8.3: Cross-Reference Validation
**Action:** Verify all cross-references between files are valid

**Check:**
- Library ID formats are consistent
- File paths are correct
- Section numbers match
- References to other modules are accurate

### Step 8.4: Example Generation
**Action:** Create comprehensive examples using actual library data

**For Each Output Template:**
- Generate at least 1 realistic example
- Show entity recognition process
- Display confidence levels
- Demonstrate cross-references

### Step 8.5: Quality Assurance
**Checklist:**
- [ ] All 5 folders created
- [ ] All ~50 files created
- [ ] All library statistics updated from actual files
- [ ] All cross-references validated
- [ ] All examples include real library entities
- [ ] Assembly scripts tested and working
- [ ] Monolithic version generated successfully
- [ ] README files complete and accurate
- [ ] CHANGELOG updated with v5 changes
- [ ] Migration guide complete

---

## DETAILED WORKFLOW: How to Execute This Meta-Prompt

### Iteration 1: Setup & Structure
1. Create root folder `MAIN_PROMPT_v5_Modular/`
2. Create 5 main folders
3. Create root README.md
4. Create folder-specific README files

### Iteration 2: Core Modules
5. Read MAIN_PROMPT_v4.md to understand structure
6. Create 5 files in `00_Core/`
7. Validate employee and project data

### Iteration 3-14: Library Integration (One Library Per Iteration)
**For EACH library (12 iterations):**
8. Read library folder: `C:\Users\Dell\Dropbox\Entities\LIBRARIES\[Library]/`
9. Count files and entities
10. Extract sample data
11. Create `01_Library_Integration/[XX]_[Library]_Library.md`
12. Fill template with actual library statistics
13. Add recognition patterns
14. Add examples using real entity IDs
15. Add cross-references to related libraries

### Iteration 15: Taxonomy Framework
16. Extract Section 22 from MAIN_PROMPT_v4.md
17. Enhance with updated library statistics
18. Create `01_Library_Integration/13_Taxonomy_Framework.md`

### Iteration 16-36: Output Templates (One Template Per Iteration)
**For EACH template (21 iterations):**
19. Extract relevant section from MAIN_PROMPT_v4.md
20. Identify which libraries integrate
21. Create template file in `02_Output_Templates/`
22. Add library integration details
23. Create realistic examples
24. Add validation checklist

### Iteration 37: Processing Rules
25. Extract processing guidelines from MAIN_PROMPT_v4.md
26. Create 6 files in `03_Processing_Rules/`
27. Enhance with library-specific rules

### Iteration 38: Usage & Maintenance
28. Extract usage instructions from MAIN_PROMPT_v4.md
29. Create 7 files in `04_Usage/`
30. Update CHANGELOG with v5 changes
31. Create migration guide

### Iteration 39: Assembly System
32. Create 4 Python scripts in `scripts/`
33. Test assembly scripts
34. Generate monolithic version

### Iteration 40: Validation & QA
35. Run statistics update across all files
36. Validate cross-references
37. Generate examples for all templates
38. Run full quality assurance checklist
39. Test monolithic version
40. Finalize documentation

---

## KEY PRINCIPLES FOR CREATING v5

### 1. Data Accuracy
- **ALWAYS** read actual library files to get current statistics
- **NEVER** guess entity counts
- **VERIFY** all IDs against library files
- **UPDATE** statistics as libraries grow

### 2. Modularity
- Each file should be self-contained
- Clear separation of concerns
- Minimal duplication
- Easy to update individual modules

### 3. Integration
- Show how libraries connect
- Demonstrate cross-referencing
- Provide clear relationship diagrams
- Include integration examples

### 4. Usability
- Clear instructions
- Realistic examples
- Troubleshooting guides
- Quick reference sections

### 5. Maintainability
- Regular update schedule
- Version control
- Change tracking
- Migration guides

---

## SUCCESS CRITERIA

v5 is complete when:
- [ ] All ~50 files created
- [ ] All library statistics accurate and current
- [ ] All cross-references validated
- [ ] Assembly scripts working
- [ ] Monolithic version generated
- [ ] Examples use real library data
- [ ] All README files complete
- [ ] CHANGELOG updated
- [ ] Migration guide created
- [ ] Quality assurance passed

---

## EXPECTED OUTPUT STRUCTURE

```
MAIN_PROMPT_v5_Modular/
│
├── README.md (Assembly overview)
│
├── 00_Core/
│   ├── 01_Purpose_Vision.md
│   ├── 02_Company_Context.md
│   ├── 03_Employee_Directory.md (32 employees)
│   ├── 04_Project_Directory.md (31+ projects)
│   └── 05_AI_Instructions.md
│
├── 01_Library_Integration/
│   ├── README.md
│   ├── 01_Actions_Library.md (429 actions)
│   ├── 02_Objects_Library.md (36 objects)
│   ├── 03_Processes_Library.md (428 processes)
│   ├── 04_Results_Library.md (432 results)
│   ├── 05_Skills_Library.md (12+ skills)
│   ├── 06_Responsibilities_Library.md
│   ├── 07_Products_Library.md (39 products)
│   ├── 08_Services_Library.md (7 categories)
│   ├── 09_Parameters_Library.md (10,596+ parameters)
│   ├── 10_Professions_Library.md (12+ professions)
│   ├── 11_Tools_Library.md (75+ tools)
│   ├── 12_Prompts_Library.md
│   └── 13_Taxonomy_Framework.md
│
├── 02_Output_Templates/
│   ├── README.md
│   ├── 01_Meeting_Metadata.md
│   ├── 02_Executive_Summary.md
│   ├── 03_Action_Items_Tasks.md ⭐ Integrated
│   ├── 04_Projects_Features.md ⭐ Integrated
│   ├── 05_Workflows_Processes.md ⭐ Integrated
│   ├── 06_Rules_Best_Practices.md ⭐ Integrated
│   ├── 07_Problems_Solutions.md
│   ├── 08_Tools_Resources.md ⭐ Integrated
│   ├── 09_Technical_Architecture.md ⭐ Integrated
│   ├── 10_Decisions_Log.md
│   ├── 11_Documentation_Gaps.md
│   ├── 12_Communication_Announcements.md
│   ├── 13_Blockers_Dependencies.md ⭐ Integrated
│   ├── 14_Insights_Lessons.md
│   ├── 15_Analogies_Frameworks.md
│   ├── 16_Employee_Team_Context.md ⭐ Integrated
│   ├── 17_Lead_Gen_Sales_Context.md ⭐ Integrated
│   ├── 18_Design_Creative_Context.md ⭐ Integrated
│   ├── 19_Development_Technical_Context.md ⭐ Integrated
│   ├── 20_Onboarding_Training_Context.md ⭐ Integrated
│   └── 21_Follow_Up_Items.md ⭐ Integrated
│
├── 03_Processing_Rules/
│   ├── README.md
│   ├── 01_Participant_Identification.md
│   ├── 02_Project_Recognition.md
│   ├── 03_Entity_Recognition.md
│   ├── 04_Language_Handling.md
│   ├── 05_Vocabulary_Recognition.md
│   └── 06_Cross_Reference_Rules.md
│
├── 04_Usage/
│   ├── 01_Usage_Instructions.md
│   ├── 02_Examples.md
│   ├── 03_Tips_Best_Practices.md
│   ├── 04_Advanced_Features.md
│   ├── 05_Maintenance_Guide.md
│   ├── 06_CHANGELOG.md
│   └── 07_Migration_Guide.md
│
└── scripts/
    ├── README.md
    ├── assemble_full_prompt.py
    ├── assemble_department.py
    └── assemble_lightweight.py
```

---

## NOTES FOR AI EXECUTING THIS META-PROMPT

### Work Iteratively
- Create one module at a time
- Validate each module before moving to next
- Update cross-references as you go

### Use Actual Data
- **CRITICAL:** Always read library files to get real statistics
- Don't use placeholder numbers
- Verify entity IDs exist in library files
- Update counts when libraries change

### Maintain Consistency
- Use same ID format conventions throughout
- Follow template structure for all similar files
- Keep naming conventions consistent
- Use same markdown formatting

### Document Everything
- Add comments in complex sections
- Explain recognition patterns clearly
- Provide context for decisions
- Include troubleshooting notes

### Test As You Go
- Validate cross-references after each module
- Check assembly scripts periodically
- Generate monolithic version to test integration
- Review examples for accuracy

---

## FINAL DELIVERABLES

1. **Modular Version:** Complete `MAIN_PROMPT_v5_Modular/` folder with ~50 files
2. **Monolithic Version:** Single `MAIN_PROMPT_v5.md` file
3. **Assembly Scripts:** Working Python scripts for generating variations
4. **Documentation:** Complete README files and guides
5. **Examples:** Realistic examples using actual library data
6. **Statistics:** Current, accurate counts for all libraries
7. **Changelog:** Complete version history
8. **Migration Guide:** v4 to v5 upgrade path

---

**END OF META-PROMPT**

When you execute this meta-prompt, you will create a comprehensive, modular, and highly maintainable MAIN_PROMPT v5 system that leverages the full power of the 12 LIBRARIES taxonomy framework.

Start with Phase 1 and work through each phase systematically, validating as you go.
