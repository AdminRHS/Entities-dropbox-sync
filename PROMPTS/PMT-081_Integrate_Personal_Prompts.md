# Integrate Personal Prompts into ENTITIES/PROMPTS Ecosystem

**Purpose**: Step-by-step guide for integrating personal prompts from individual employee folders into the standardized ENTITIES/PROMPTS ecosystem following PMT taxonomy and naming conventions.

**Version**: 1.0  
**Date**: 2025-11-21  
**Status**: Active  
**Related Prompts**: `PMT-001_Main_Prompt_v4.md`, `PMT-072_PROMPTS_Critical_Fixes.md`, `Entity_Integration_Prompts.md`

---

## Overview

This prompt guides you through the complete process of integrating your personal prompts (stored in department folders like `Design Nov25\Skrypkar Vilhelm\Prompts.md`) into the centralized `ENTITIES/PROMPTS` ecosystem. The integration ensures:

- **Standardized naming**: All prompts follow `PMT-###` ID system
- **Proper categorization**: Prompts are organized by function (RESEARCH, WORKFLOW, CREATIVES, etc.)
- **Department mapping**: Each prompt is linked to the correct department code
- **Master list tracking**: All prompts are registered in `PMT_Master_List.csv`
- **Metadata consistency**: All prompts include required headers and documentation

---

## Prerequisites

Before starting integration, ensure you have:

1. ✅ Access to `ENTITIES/PROMPTS/` directory
2. ✅ Your personal prompts file (e.g., `Design Nov25\Skrypkar Vilhelm\Prompts.md`)
3. ✅ Understanding of your prompts' purposes and use cases
4. ✅ Knowledge of which department(s) your prompts serve

---

## Phase 1: Analysis & Inventory

### Step 1.1: Read Your Personal Prompts File

**Action**: Open your personal prompts file and create an inventory list.

**Example Location**: `Design Nov25\Skrypkar Vilhelm\Prompts.md`

**Task**: List each distinct prompt with:
- **Prompt Title/Description** (what it does)
- **Primary Use Case** (when/why you use it)
- **Target AI Platform** (Gemini, ChatGPT, Perplexity, Cursor, etc.)
- **Department Scope** (DGN, AID, Multi, etc.)
- **Dependencies** (references other prompts/files/tools)

**Example Inventory Entry**:
```markdown
### Prompt 1: Course Creation via Deep Research
- **Title**: Creating courses on advanced prompting in different AIs
- **Use Case**: Generate comprehensive course lessons on AI platforms
- **Platform**: Gemini (deep research capability)
- **Department**: AID (AI & Automation) or Multi
- **Dependencies**: None
- **Category**: RESEARCH (research-based content creation)
```

### Step 1.2: Identify Prompt Categories

**Action**: Map each prompt to one of the PROMPTS categories:

| Category Code | Category Name | Description | Example Use Cases |
|--------------|---------------|-------------|-------------------|
| **CORE** | Core System | Main system prompts | MAIN_PROMPT versions |
| **VIDEO** | Video Processing | Video transcription, analysis | Video workflows |
| **REPORTS** | Daily Reports | Department reporting | Daily report generation |
| **TAXONOMY** | Taxonomy | ID systems, schemas | Building taxonomy structures |
| **RESEARCH** | Research | Research processing | YouTube research, deep research |
| **HR** | HR Operations | Human resources workflows | CV parsing, interviews |
| **WORKFLOW** | Operational Workflows | Business process automation | Call organization, project docs |
| **AUTOMATION** | Automation | Workflow automation | Version control, scripts |
| **UTILITIES** | Utilities | General-purpose tools | Entity identification, updates |
| **SYSTEM** | System Architecture | System analysis, architecture | Data integrity, health reviews |
| **DATA_ARCHITECTURE** | Data Architecture | Data management | Schema validation, optimization |
| **CREATIVES** | Creative Workflows | Design, image generation | Mascot prompts, graphics creation |

**Task**: For each prompt, assign the most appropriate category. If a prompt fits multiple categories, choose the **primary** function.

**Example Mapping**:
- "Creating courses via deep research" → **RESEARCH**
- "Generating brochure designs" → **CREATIVES** (or **WORKFLOW** if it's a multi-step process)
- "Processing daily reports" → **REPORTS** (or **WORKFLOW** if it includes multiple steps)
- "Redesigning cover images" → **CREATIVES**
- "Compiling daily plans and tasks" → **REPORTS** or **WORKFLOW**

### Step 1.3: Determine Department Codes

**Action**: Assign department code(s) for each prompt.

**Valid Department Codes**:
- **AID** - AI & Automation
- **HRM** - Human Resources
- **DEV** - Development
- **DGN** - Design
- **VID** - Video Production
- **LGN** - Lead Generation
- **SLS** - Sales
- **MKT** - Marketing
- **SMM** - Social Media Management
- **FNC** - Finance
- **CNT** - Content
- **Multi** - Multi-Department
- **OPS** - Operations

**Task**: Assign department code based on:
- Who primarily uses the prompt
- Which department's workflows it supports
- If used across multiple departments → use **Multi**

**Example Assignments**:
- Design-specific prompts → **DGN**
- AI research prompts → **AID** or **Multi**
- Course creation for all employees → **Multi**

---

## Phase 2: Categorization & Folder Placement

### Step 2.1: Determine Target Folder

**Action**: Based on category assignment, identify the target folder within `ENTITIES/PROMPTS/`.

**Folder Structure**:
```
ENTITIES/PROMPTS/
├── Core/                          # CORE category
├── Video_Processing/              # VIDEO category
│   ├── Transcription/
│   ├── Analysis/
│   ├── Taxonomy_Integration/
│   └── Workflows/
├── DEPARTMENTS/
│   ├── Daily_Reports/            # REPORTS category
│   └── HR_Operations/            # HR category
├── RESEARCH/                     # RESEARCH category
│   └── Research_Prompts/
├── SYSTEM/                       # SYSTEM, DATA_ARCHITECTURE categories
│   ├── System_Analysis/
│   ├── Architecture_Guides/
│   └── DATA_ARCHITECTURE/
├── WORKFLOWS/                    # WORKFLOW category
│   ├── Operational_Workflows/
│   ├── Account_Management/
│   └── Library_Processing/
├── CREATIVES/                    # CREATIVES category (if exists)
└── UTILITIES/                    # UTILITIES category
```

**Task**: For each prompt, identify the exact folder path where it should be placed.

**Example Placements**:
- Research prompts → `RESEARCH/Research_Prompts/`
- Design creative workflows → `CREATIVES/` (create if needed) or `WORKFLOWS/Operational_Workflows/`
- Report processing → `DEPARTMENTS/Daily_Reports/` or `WORKFLOWS/Operational_Workflows/`

### Step 2.2: Check for Existing Similar Prompts

**Action**: Search `ENTITIES/PROMPTS/` for prompts with similar functionality.

**Task**: 
1. Review `PMT_Master_List.csv` for similar prompts
2. Check category folders for related prompts
3. Determine if your prompt:
   - **Replaces** an existing prompt → Update existing PMT ID
   - **Extends** an existing prompt → Reference related PMT ID
   - **Is unique** → Assign new PMT ID

**Example Check**:
- If integrating "YouTube AI tutorials research" → Check `PMT-048_YouTube_AI_Tools_Daily.md`
- If similar exists → Consider if yours is a variant or replacement

---

## Phase 3: PMT ID Assignment

### Step 3.1: Find Next Available PMT ID

**Action**: Check `ENTITIES/PROMPTS/DATA_FIELDS/PMT_Master_List.csv` for the highest PMT ID.

**Task**:
1. Open `PMT_Master_List.csv`
2. Find the highest `PMT_ID` number (e.g., `PMT-080`)
3. Your first prompt gets the next sequential ID (e.g., `PMT-081`)
4. Assign sequential IDs to all your prompts (PMT-081, PMT-082, PMT-083, etc.)

**Important Rules**:
- ✅ IDs are **sequential** (no gaps)
- ✅ Each prompt gets **one unique ID**
- ✅ IDs are **permanent** (don't change after assignment)
- ❌ Don't skip numbers
- ❌ Don't reuse IDs

**Example**: If highest ID is `PMT-080`, your prompts get:
- Prompt 1 → `PMT-081`
- Prompt 2 → `PMT-082`
- Prompt 3 → `PMT-083`
- etc.

### Step 3.2: Create Descriptive Names

**Action**: Generate descriptive names for each prompt following the naming convention.

**Naming Format**: `PMT-{###}_{Descriptive_Name}.md`

**Naming Rules**:
- Use **underscores** not spaces: `PMT-081_Course_Creation_Research.md`
- Use **Title Case** for readability: `Course_Creation_Research` not `course_creation_research`
- Keep names **concise** but descriptive (max 5-6 words)
- Include **version** if applicable: `PMT-081_Course_Creation_Research_v1.md`

**Example Names**:
- "Creating courses on advanced prompting" → `PMT-081_Advanced_Prompting_Course_Creation.md`
- "Generating brochure for HoneyStone" → `PMT-082_Brochure_Design_Generation.md`
- "Deep research for photo editing AIs" → `PMT-083_Photo_Editing_AI_Research.md`
- "Redesigning cover images for Game Academy" → `PMT-084_Game_Academy_Cover_Redesign.md`

---

## Phase 4: File Creation with Metadata

### Step 4.1: Create Prompt File Structure

**Action**: Create a new markdown file for each prompt with proper metadata header.

**File Template**:
```markdown
# [Prompt Title]

**Purpose**: [One-sentence description of what this prompt does]
**Version**: 1.0
**Date**: [YYYY-MM-DD]
**Status**: Active
**Related Prompts**: [List related PMT-### IDs if applicable]

---

## Overview

[2-3 paragraph description of the prompt's purpose, use cases, and context]

---

## [Main Content Sections]

[Your actual prompt content, instructions, examples, etc.]

---

## Usage Guidelines

**When to Use**: [Specific scenarios]
**Input Requirements**: [What files/data are needed]
**Output Format**: [What the prompt produces]
**Best Practices**: [Tips for optimal results]

---

## Examples

[Include 1-2 example use cases with expected outputs]

---

## Version History

- v1.0 ([YYYY-MM-DD]): Initial integration from personal prompts
```

### Step 4.2: Transform Personal Prompt Content

**Action**: Convert your personal prompt text into the standardized format.

**Transformation Guidelines**:

1. **Extract Core Instructions**: Identify the main prompt text and any follow-up instructions
2. **Add Context**: Include when/why to use this prompt
3. **Document Dependencies**: List required files, tools, or other prompts
4. **Add Examples**: Include example inputs/outputs if not present
5. **Standardize Formatting**: Use consistent markdown formatting

**Example Transformation**:

**Original Personal Prompt**:
```
**For creating courses on advanced prompting in different AIs via deep research in Gemini:**
'Hey! I create a learning course for employees on advanced prompting in different AIs. Each lesson of the course must teach advanced prompting in another AI. Please conduct deep research on courses, tutorials, videos, etc around the internet and compile lessons on that AI. Make the theoretical part really short, and focus on possible use cases and details on how to tailor prompts and make that AI work. Now, compile a lesson "Advanced Pompting in [AI name]" '
```

**Transformed PMT Format**:
```markdown
# Advanced Prompting Course Creation via Deep Research

**Purpose**: Generate comprehensive course lessons on advanced prompting techniques for different AI platforms using Gemini's deep research capabilities.

**Version**: 1.0
**Date**: 2025-11-21
**Status**: Active
**Related Prompts**: None

---

## Overview

This prompt enables creation of structured course content focused on advanced prompting techniques across various AI platforms. It leverages Gemini's deep research capabilities to compile practical, use-case-focused lessons with minimal theoretical content.

**Primary Use Case**: Creating employee training courses on AI prompting
**Target Platform**: Gemini (for deep research functionality)
**Department**: Multi (all departments benefit from AI prompting skills)

---

## Prompt Instructions

### Base Prompt

```
Hey! I create a learning course for employees on advanced prompting in different AIs. Each lesson of the course must teach advanced prompting in another AI. Please conduct deep research on courses, tutorials, videos, etc around the internet and compile lessons on that AI. Make the theoretical part really short, and focus on possible use cases and details on how to tailor prompts and make that AI work. Now, compile a lesson "Advanced Prompting in [AI name]"
```

### Usage Instructions

1. **Replace `[AI name]`** with the target AI platform (e.g., "Claude", "ChatGPT", "Midjourney")
2. **Provide Context**: Optionally include specific use cases or department focus
3. **Review Output**: Verify research quality and practical focus

---

## Expected Output Structure

Each lesson should include:
- **Brief Introduction** (2-3 paragraphs max)
- **Use Cases** (specific, practical applications)
- **Prompt Tailoring Guide** (how to customize prompts for this AI)
- **Workflow Examples** (step-by-step processes)
- **Best Practices** (tips and common pitfalls)

---

## Examples

### Example 1: Claude AI Lesson
**Input**: "Advanced Prompting in Claude"
**Output**: Lesson covering Claude's strengths (long context, analysis), use cases (document analysis, code review), and prompt engineering techniques specific to Claude.

### Example 2: Midjourney Lesson
**Input**: "Advanced Prompting in Midjourney"
**Output**: Lesson covering Midjourney's image generation, prompt structure (parameters, weights), and design workflow integration.

---

## Version History

- v1.0 (2025-11-21): Initial integration from personal prompts collection
```

### Step 4.3: Save Files to Correct Locations

**Action**: Save each prompt file to its designated folder with the correct filename.

**Task**:
1. Navigate to target folder (e.g., `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/`)
2. Create file: `PMT-081_Advanced_Prompting_Course_Creation.md`
3. Verify file path matches your planned location
4. Repeat for all prompts

**File Path Format**: `ENTITIES/PROMPTS/{Category_Folder}/{Subfolder_if_applicable}/PMT-{###}_{Name}.md`

---

## Phase 5: Master List CSV Update

### Step 5.1: Prepare CSV Entries

**Action**: Create CSV entries for each integrated prompt.

**CSV Format** (from `PMT_Master_List.csv`):
```csv
PMT_ID,Entity_Type,Name,Description,Category,Department,File_Path,Status,Version,Last_Updated
```

**Field Definitions**:
- **PMT_ID**: `PMT-081`, `PMT-082`, etc.
- **Entity_Type**: Always `Prompt`
- **Name**: Short descriptive name (matches filename without PMT-###)
- **Description**: One-sentence purpose description
- **Category**: Category code (RESEARCH, CREATIVES, WORKFLOW, etc.)
- **Department**: Department code (DGN, AID, Multi, etc.)
- **File_Path**: Relative path from `ENTITIES/PROMPTS/` (e.g., `RESEARCH/Research_Prompts/PMT-081_Advanced_Prompting_Course_Creation.md`)
- **Status**: `Active`, `Utility`, or `Deprecated` (usually `Active` for new integrations)
- **Version**: `1.0` (semantic version)
- **Last_Updated**: `YYYY-MM-DD` format

**Example CSV Entry**:
```csv
PMT-081,Prompt,Advanced Prompting Course Creation,Generate comprehensive course lessons on advanced prompting techniques for different AI platforms using Gemini's deep research capabilities,RESEARCH,Multi,RESEARCH/Research_Prompts/PMT-081_Advanced_Prompting_Course_Creation.md,Active,1.0,2025-11-21
```

### Step 5.2: Update PMT_Master_List.csv

**Action**: Append your new entries to `ENTITIES/PROMPTS/DATA_FIELDS/PMT_Master_List.csv`.

**Task**:
1. Open `PMT_Master_List.csv` in a text editor or spreadsheet
2. **Append** new rows (don't insert in the middle)
3. Ensure CSV formatting is correct (commas, no extra spaces)
4. Verify all required fields are filled
5. Save the file

**Important**: 
- ✅ Maintain CSV structure (header row + data rows)
- ✅ Use commas as delimiters
- ✅ No trailing commas
- ✅ Consistent date format (YYYY-MM-DD)

**Example Batch Addition**:
```csv
PMT-081,Prompt,Advanced Prompting Course Creation,Generate comprehensive course lessons on advanced prompting techniques for different AI platforms using Gemini's deep research capabilities,RESEARCH,Multi,RESEARCH/Research_Prompts/PMT-081_Advanced_Prompting_Course_Creation.md,Active,1.0,2025-11-21
PMT-082,Prompt,Brochure Design Generation,Generate brochure designs for clients by analyzing website and existing materials,CREATIVES,DGN,CREATIVES/PMT-082_Brochure_Design_Generation.md,Active,1.0,2025-11-21
PMT-083,Prompt,Photo Editing AI Research,Research and compile tutorials on photo editing and retouching AI tools,RESEARCH,DGN,RESEARCH/Research_Prompts/PMT-083_Photo_Editing_AI_Research.md,Active,1.0,2025-11-21
```

---

## Phase 6: Validation & Verification

### Step 6.1: File Structure Validation

**Action**: Verify all files are created correctly.

**Checklist**:
- [ ] All prompt files exist in correct folders
- [ ] File names follow `PMT-{###}_{Name}.md` format
- [ ] All files have metadata headers (Purpose, Version, Date, Status)
- [ ] File paths match entries in `PMT_Master_List.csv`
- [ ] No duplicate PMT IDs

**Verification Command** (if using terminal):
```bash
# Check files exist
ls ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-081*.md

# Verify CSV entries
grep "PMT-081" ENTITIES/PROMPTS/DATA_FIELDS/PMT_Master_List.csv
```

### Step 6.2: Content Validation

**Action**: Review prompt content for completeness and quality.

**Checklist**:
- [ ] Each prompt has clear purpose statement
- [ ] Usage instructions are included
- [ ] Examples are provided (if applicable)
- [ ] Dependencies are documented
- [ ] Formatting is consistent
- [ ] No broken references to other files/prompts

### Step 6.3: Cross-Reference Validation

**Action**: Verify integration with ecosystem.

**Checklist**:
- [ ] PMT IDs are sequential (no gaps)
- [ ] Category assignments are appropriate
- [ ] Department codes are correct
- [ ] File paths are valid (folders exist)
- [ ] Related prompts are referenced (if applicable)

### Step 6.4: Documentation Update

**Action**: Update relevant documentation files.

**Optional Updates**:
- Update `ENTITIES/PROMPTS/README.md` if adding new category
- Update category-specific README files if applicable
- Document integration in department log (per workspace rules)

---

## Complete Integration Example

### Example: Integrating "Course Creation" Prompt

**Phase 1: Analysis**
- **Prompt**: Creating courses on advanced prompting in different AIs
- **Category**: RESEARCH
- **Department**: Multi
- **Platform**: Gemini

**Phase 2: Categorization**
- **Target Folder**: `RESEARCH/Research_Prompts/`

**Phase 3: ID Assignment**
- **PMT ID**: PMT-081
- **File Name**: `PMT-081_Advanced_Prompting_Course_Creation.md`

**Phase 4: File Creation**
- **Location**: `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-081_Advanced_Prompting_Course_Creation.md`
- **Content**: Transformed prompt with metadata header and structured sections

**Phase 5: Master List Update**
- **CSV Entry**: `PMT-081,Prompt,Advanced Prompting Course Creation,Generate comprehensive course lessons...,RESEARCH,Multi,RESEARCH/Research_Prompts/PMT-081_Advanced_Prompting_Course_Creation.md,Active,1.0,2025-11-21`

**Phase 6: Validation**
- ✅ File exists at correct path
- ✅ Metadata header complete
- ✅ CSV entry added
- ✅ No duplicate IDs
- ✅ Category and department codes correct

---

## Common Integration Scenarios

### Scenario 1: Multi-Step Workflow Prompt

**Example**: "Processing daily reports with MAIN PROMPT v4, then updating plans and tasks"

**Integration Steps**:
1. **Category**: WORKFLOW (multi-step process)
2. **Folder**: `WORKFLOWS/Operational_Workflows/`
3. **Structure**: Document each step clearly
4. **Dependencies**: Reference `PMT-001_Main_Prompt_v4.md`
5. **Name**: `PMT-082_Daily_Report_Processing_Workflow.md`

### Scenario 2: Creative Design Prompt

**Example**: "Generating social media graphics with mascot, UI kit, and design guidelines"

**Integration Steps**:
1. **Category**: CREATIVES (design generation)
2. **Folder**: `CREATIVES/` (create if needed) or `WORKFLOWS/Operational_Workflows/`
3. **Structure**: Include step-by-step instructions, file requirements
4. **Dependencies**: Document required files (mascot references, UI kit, guidelines)
5. **Name**: `PMT-083_Social_Media_Graphics_Generation.md`

### Scenario 3: Research Prompt with Iterations

**Example**: "Deep research prompt with follow-up refinement steps"

**Integration Steps**:
1. **Category**: RESEARCH
2. **Folder**: `RESEARCH/Research_Prompts/`
3. **Structure**: Document initial prompt + all iteration steps
4. **Format**: Use clear section separators for each iteration
5. **Name**: `PMT-084_Deep_Research_Workflow.md`

---

## Troubleshooting

### Issue: Category Doesn't Exist

**Solution**: 
- Use closest existing category
- Or create new category folder (update README.md)
- Document decision in prompt metadata

### Issue: Duplicate Functionality

**Solution**:
- Compare with existing prompts
- If yours is better → Replace existing (update PMT ID)
- If complementary → Keep both, reference each other
- Document relationship in "Related Prompts"

### Issue: Multi-Department Prompt

**Solution**:
- Use `Multi` as department code
- List primary departments in description
- Consider creating department-specific variants if needed

### Issue: Prompt References Personal Files

**Solution**:
- Update file paths to relative paths from workspace root
- Or use placeholders: `[Department]/[Employee]/[File]`
- Document path requirements in "Input Requirements"

---

## Best Practices

### ✅ DO:
- **Standardize formatting** across all prompts
- **Document dependencies** clearly
- **Include examples** for complex prompts
- **Reference related prompts** in metadata
- **Use consistent naming** conventions
- **Update master list immediately** after file creation
- **Test prompts** before marking as Active

### ❌ DON'T:
- **Skip metadata headers** (required for all prompts)
- **Create duplicate PMT IDs** (always check master list)
- **Use spaces in filenames** (use underscores)
- **Forget to update CSV** (master list must stay synchronized)
- **Mix categories** (one prompt = one primary category)
- **Leave broken references** (verify all file paths)

---

## Integration Checklist Summary

Use this checklist for each prompt you integrate:

**Pre-Integration**:
- [ ] Analyzed prompt purpose and use cases
- [ ] Identified category and department
- [ ] Checked for existing similar prompts
- [ ] Determined target folder location

**File Creation**:
- [ ] Assigned sequential PMT ID
- [ ] Created descriptive filename
- [ ] Added complete metadata header
- [ ] Transformed content to standard format
- [ ] Saved file to correct folder

**Master List**:
- [ ] Prepared CSV entry with all fields
- [ ] Added entry to PMT_Master_List.csv
- [ ] Verified CSV formatting

**Validation**:
- [ ] Verified file exists at correct path
- [ ] Checked metadata completeness
- [ ] Confirmed no duplicate IDs
- [ ] Validated category/department codes
- [ ] Tested prompt functionality (if possible)

---

## Next Steps After Integration

1. **Test the integrated prompts** with real use cases
2. **Share with team** if prompts are department-wide
3. **Update documentation** if creating new categories
4. **Monitor usage** and gather feedback
5. **Iterate** based on team needs

---

## Support & Questions

If you encounter issues during integration:

1. **Check existing prompts** for similar patterns
2. **Review** `ENTITIES/PROMPTS/README.md` for ecosystem structure
3. **Consult** `PMT_Master_List.csv` for ID assignments
4. **Reference** `Entity_Schema_Registry.json` for validation rules

---

## Version History

- v1.0 (2025-11-21): Initial creation - Comprehensive integration guide for personal prompts

---

**Last Updated**: 2025-11-21  
**Maintained By**: PROMPTS Entity Team  
**Status**: Active

