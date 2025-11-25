# Daily Report Prompt Constructor - Documentation

## Overview
This documentation folder contains comprehensive guidance materials extracted from [SummariesOct](../../../../../SummariesOct/) to refine and enhance the daily report prompt generation system.

---

## Documentation Files

### [01_employee_directory_guidance.md](./01_employee_directory_guidance.md)
**Purpose**: Automatic participant identification in call transcripts

**Contents**:
- Complete employee directory (32 employees across 7 departments)
- Participant identification strategies (5 methods)
- Confidence level assessment
- Multi-lingual name matching
- Output format specifications
- Integration guidelines for prompts

**Key Features**:
- Direct name matching with variations
- Contextual clue identification (department, project, role, location)
- Communication handle matching (Telegram, email)
- Voice/speech pattern recognition
- Department distribution statistics

**Use Case**: When generating department-specific prompts, integrate the relevant employee list and identification strategies to automatically match participants mentioned in transcripts.

---

### [02_project_directory_guidance.md](./02_project_directory_guidance.md)
**Purpose**: Automatic project identification in call transcripts

**Contents**:
- Complete project directory (31+ active projects)
- Project abbreviations quick reference
- Project recognition strategies (6 methods)
- Confidence level assessment
- Multi-lingual project name matching
- Resource references (Figma, Google Drive)
- Project categories and department alignment

**Key Features**:
- Direct name and abbreviation matching
- Keyword-based identification
- Multi-lingual support (Russian, Ukrainian, English)
- Resource-based identification
- Contextual clue matching

**Use Case**: When generating department-specific prompts, integrate the relevant project list to automatically identify and reference projects mentioned in transcripts.

---

### [03_vocabulary_standards.md](./03_vocabulary_standards.md)
**Purpose**: Standardized vocabulary and terminology for consistent reporting

**Contents**:
- Company-specific vocabulary across all domains:
  - Lead Generation & Sales terms (BANT, MQL, SQL, etc.)
  - AI & LLM terms (prompting techniques, AI concepts)
  - Design terms (Figma, UI/UX, AI design tools)
  - Development terms (roles, tools, architecture)
  - Video production terms
  - General business terms
- Action + Object framework foundations
- Multi-language support guidelines
- Profession recognition (636+ variations)
- Entity types (8 core types)

**Key Features**:
- Comprehensive terminology reference
- Standardized action verbs with three forms (action, process, result)
- Standard status and priority values
- RACI matrix definitions
- Multi-lingual term mappings

**Use Case**: Reference this document to ensure all generated prompts use consistent, standardized terminology across departments.

---

### [04_task_object_framework.md](./04_task_object_framework.md)
**Purpose**: Comprehensive task definition and management framework

**Contents**:
- Complete Task Template structure (JSON format)
- Standard Actions Library with three forms per action
- Standard Objects Library organized by department
- Step Template structure and format
- Checklist Template structure and format
- RACI Matrix definitions and examples
- Status, Priority, and Complexity value definitions
- Task extraction guidelines
- Quality standards and checks

**Key Features**:
- ACTION + OBJECT + CONTEXT format
- Profession-specific object libraries
- Structured step-by-step procedures
- Verification checklists
- Accountability assignment (RACI)
- Complete task metadata

**Use Case**: Use this framework to structure all task extraction in daily reports, ensuring consistency across departments and enabling template-driven operations.

---

### [05_21_section_framework.md](./05_21_section_framework.md)
**Purpose**: Comprehensive 21-section structure for organizing daily reports

**Contents**:
- Complete framework overview
- Detailed specifications for all 21 sections:
  1. Meeting Metadata
  2. Executive Summary
  3. Action Items & Tasks
  4. Projects & Features
  5. Workflows & Processes
  6. Rules & Best Practices
  7. Problems & Solutions
  8. Tools & Resources
  9. Technical Architecture
  10. Decisions Log
  11. Documentation & Knowledge Gaps
  12. Communication & Announcements
  13. Blockers & Dependencies
  14. Key Insights & Lessons
  15. Analogies & Frameworks
  16-20. Department-Specific Sections (LG, Sales, Design, Dev, HR)
  21. Follow-up Items
- Section selection guidelines by call type
- Integration guidelines
- Quality standards
- Prompt integration instructions

**Key Features**:
- Consistent structure across all reports
- Department-specific customization (sections 16-20)
- Flexible section selection based on call type
- Comprehensive information capture
- Cross-referencing capabilities

**Use Case**: Use this framework as the structural foundation for all daily report prompts, selecting appropriate sections based on department and call type.

---

### [06_department_specific_patterns.md](./06_department_specific_patterns.md)
**Purpose**: Department-specific guidance for targeted daily reports

**Contents**:
- Detailed configurations for all 7 departments:
  - **HR** (2 employees) - Recruitment, onboarding, employee management
  - **AI** (3 employees) - Prompt engineering, automation, RAC management
  - **Video** (3 employees) - Video production, content creation, AI tools
  - **Sales** (1 employee) - Client management, pipeline, SMM support
  - **Design** (9 employees) - UI/UX, graphic design, branding, AI design tools
  - **Dev** (3 employees) - Frontend, backend, system development, DevOps
  - **LG** (11 employees) - Prospecting, qualification, outreach, analytics

**For Each Department**:
- Team composition with full employee details
- Section emphasis (which of 21 sections to prioritize)
- Focus areas (3-4 key activity categories)
- Common objects specific to department
- Key metrics and KPIs
- Typical activities and workflows

**Additional Content**:
- Cross-department collaboration patterns
- Project alignment guidelines
- Integration instructions for prompt constructor

**Use Case**: Reference the relevant department section when creating department-specific prompts to ensure appropriate focus, terminology, and structure.

---

## How to Use This Documentation

### For Prompt Generation
1. **Start with** [06_department_specific_patterns.md](./06_department_specific_patterns.md) to understand department requirements
2. **Reference** [05_21_section_framework.md](./05_21_section_framework.md) for structural guidance
3. **Integrate** [01_employee_directory_guidance.md](./01_employee_directory_guidance.md) for participant matching
4. **Integrate** [02_project_directory_guidance.md](./02_project_directory_guidance.md) for project matching
5. **Apply** [03_vocabulary_standards.md](./03_vocabulary_standards.md) for consistent terminology
6. **Use** [04_task_object_framework.md](./04_task_object_framework.md) for task extraction structure

### For Prompt Refinement
1. **Review** existing prompt against quality standards in each document
2. **Enhance** participant identification using employee directory strategies
3. **Improve** project recognition using project directory patterns
4. **Standardize** terminology using vocabulary standards
5. **Structure** tasks using Action + Object + Context framework
6. **Align** with 21-section framework for comprehensive coverage
7. **Customize** using department-specific patterns

### For New Department Prompts
1. **Identify** department from [06_department_specific_patterns.md](./06_department_specific_patterns.md)
2. **Extract** section emphasis, focus areas, common objects, and key metrics
3. **Build** prompt structure using [05_21_section_framework.md](./05_21_section_framework.md)
4. **Add** employee identification from [01_employee_directory_guidance.md](./01_employee_directory_guidance.md)
5. **Add** project identification from [02_project_directory_guidance.md](./02_project_directory_guidance.md)
6. **Apply** vocabulary from [03_vocabulary_standards.md](./03_vocabulary_standards.md)
7. **Structure** tasks using [04_task_object_framework.md](./04_task_object_framework.md)

---

## Key Improvements Enabled

### 1. Intelligent Participant Matching
- Automatic identification of 32 employees
- Confidence level assignment
- Multi-lingual name recognition
- Contextual clue processing

### 2. Intelligent Project Matching
- Automatic identification of 31+ projects
- Abbreviation recognition
- Resource referencing (Figma, Google Drive)
- Multi-lingual project name support

### 3. Standardized Vocabulary
- Consistent terminology across departments
- Recognized profession titles (636+ variations)
- Standardized action verbs and objects
- Multi-language support

### 4. Template-Driven Task Management
- ACTION + OBJECT + CONTEXT format
- Complete task metadata
- RACI accountability
- Quality standards and verification

### 5. Comprehensive Information Capture
- 21-section framework coverage
- Department-specific focus
- Cross-referencing capabilities
- Structured follow-up tracking

### 6. Department-Specific Optimization
- Tailored section emphasis
- Relevant focus areas
- Department-specific metrics
- Common object recognition

---

## Quality Standards

All documentation includes:
- Clear purpose statements
- Comprehensive examples
- Integration guidelines
- Quality criteria
- Practical use cases

All generated prompts should:
- Match participants to Employee Directory with confidence levels
- Match projects to Project Directory with resource references
- Use standardized vocabulary from Vocabulary Standards
- Structure tasks using Task + Object Framework
- Follow 21-Section Framework structure
- Apply Department-Specific Patterns appropriately

---

## Source Context

This documentation was extracted and synthesized from:
- [C:\Users\Dell\Dropbox\SummariesOct\](../../../../../SummariesOct/)

Key source files:
- `Context/01-Company-Context.md`
- `Context/02-Employee-Directory.md`
- `Context/03-Project-Directory.md`
- `Resources/MAIN PROMPT v2.md`
- `INFRASTRUCTURE/TEMPLATES/task_template.json`
- `INFRASTRUCTURE/ENTITIES/LIBRARIES/Responsibilities/Actions/actions_library.json`
- `INFRASTRUCTURE/ENTITIES/LIBRARIES/Responsibilities/Objects/objects_library.json`
- `Summaries/241025-organized.md` (example structured report)
- `Documentation/ENTITY_TYPES.md`
- `Documentation/Skills_Assessment_Framework.md`

---

## Version History

**Version 1.0** (November 7, 2025)
- Initial documentation creation
- Extracted from SummariesOct comprehensive organizational knowledge base
- Created 6 core guidance documents
- Established integration framework for prompt constructor

---

## Next Steps

### Immediate
1. Integrate guidance into [classification_summary.md](../classification_summary.md)
2. Update prompt constructor to reference these documents
3. Generate department-specific prompts using this framework

### Future Enhancements
1. Add visual diagrams and flowcharts
2. Create quick-reference cheat sheets
3. Develop validation checklist for generated prompts
4. Build automated quality checking tools
5. Create example prompts for each department

---

*Last Updated: November 7, 2025*
