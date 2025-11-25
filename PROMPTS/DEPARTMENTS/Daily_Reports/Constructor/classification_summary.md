# Prompt Parts Classification Summary

## Overview

This document provides a comprehensive summary of how prompt parts are classified and organized in the constructor system, enhanced with organizational context from Remote Helpers' comprehensive knowledge base.

## Documentation Resources

Detailed guidance documents are available in the [docs/](./docs/) folder:
- [Employee Directory Guidance](./docs/01_employee_directory_guidance.md) - 32 employees across 7 departments
- [Project Directory Guidance](./docs/02_project_directory_guidance.md) - 31+ active projects
- [Vocabulary Standards](./docs/03_vocabulary_standards.md) - Standardized terminology
- [Task + Object Framework](./docs/04_task_object_framework.md) - ACTION + OBJECT + CONTEXT structure
- [21-Section Framework](./docs/05_21_section_framework.md) - Comprehensive report structure
- [Department-Specific Patterns](./docs/06_department_specific_patterns.md) - Department configurations

---

## Classification Matrix

| Section ID | Section Name | Type | Category | Required | Order |
|------------|--------------|------|----------|----------|-------|
| purpose | Purpose | header | introduction | ✅ | 1 |
| department_context | Department Context | context | department_specific | ✅ | 2 |
| base_context_integration | Base Context Integration | reference | integration | ✅ | 3 |
| department_instructions | Department Instructions | instructions | department_specific | ✅ | 4 |
| department_vocabulary | Department Vocabulary | reference | department_specific | ✅ | 5 |
| project_matching | Project Matching | reference | department_specific | ✅ | 6 |
| quality_standards | Quality Standards | standards | standard | ✅ | 7 |
| example_usage | Example Usage | example | standard | ✅ | 8 |
| version_history | Version History | metadata | standard | ✅ | 9 |
| footer | Footer | metadata | standard | ✅ | 10 |

---

## Classification by Type

### Header (1 section)
- **purpose**: Introduction and purpose statement

### Context (2 sections)
- **department_context**: Department-specific information
- **base_context_integration**: References to base documents

### Instructions (1 section)
- **department_instructions**: Step-by-step instructions

### Reference (3 sections)
- **department_vocabulary**: Department-specific terms
- **project_matching**: Project identification rules
- *(base_context_integration also classified as reference)*

### Standards (1 section)
- **quality_standards**: Content and formatting requirements

### Example (1 section)
- **example_usage**: Usage examples and commands

### Metadata (2 sections)
- **version_history**: Version tracking
- **footer**: Document footer

---

## Classification by Category

### Introduction (1 section)
- **purpose**: Purpose statement

### Department Specific (4 sections)
- **department_context**: Custom department information
- **department_instructions**: Customized instructions
- **department_vocabulary**: Department terminology
- **project_matching**: Department projects

### Integration (1 section)
- **base_context_integration**: Base document references

### Standard (4 sections)
- **quality_standards**: Common quality rules
- **example_usage**: Standard usage examples
- **version_history**: Version tracking
- **footer**: Standard footer

---

## Section Hierarchy

```
Prompt Document
│
├── 1. Purpose (Header/Introduction)
│
├── 2. Department Context (Context/Department Specific)
│   ├── Department Overview
│   ├── Department Employees
│   ├── Department Projects
│   └── Department Tools
│
├── 3. Base Context Integration (Reference/Integration)
│
├── 4. Department Instructions (Instructions/Department Specific)
│   ├── Step 1: Read Prompt Log
│   ├── Step 2: Process Transcripts
│   └── Step 3: Generate Report
│
├── 5. Department Vocabulary (Reference/Department Specific)
│
├── 6. Project Matching (Reference/Department Specific)
│
├── 7. Quality Standards (Standards/Standard)
│   ├── Content Requirements
│   └── Formatting Requirements
│
├── 8. Example Usage (Example/Standard)
│
├── 9. Version History (Metadata/Standard)
│
└── 10. Footer (Metadata/Standard)
```

---

## Dependency Graph

```
┌─────────────────┐
│  Data Sources   │
│  - Employees    │
│  - Projects     │
│  - Tools        │
│  - Vocabulary   │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ Department Context  │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Base Context        │
│ Integration         │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ Department          │
│ Instructions        │
└────────┬────────────┘
         │
         ├─────────────────┐
         ▼                 ▼
┌─────────────────┐  ┌──────────────┐
│ Vocabulary      │  │ Project      │
│                 │  │ Matching     │
└─────────────────┘  └──────────────┘
         │
         ▼
┌─────────────────┐
│ Quality         │
│ Standards       │
└─────────────────┘
```

---

## Section Characteristics

### Required vs Optional
- **All 10 sections are REQUIRED**
- No optional sections in current structure

### Customizable vs Standard
- **Customizable (4 sections)**:
  - Department Context
  - Department Instructions
  - Department Vocabulary
  - Project Matching

- **Standard (6 sections)**:
  - Purpose
  - Base Context Integration
  - Quality Standards
  - Example Usage
  - Version History
  - Footer

### Data-Driven vs Template-Driven
- **Data-Driven (3 sections)**:
  - Department Employees (from employee directory)
  - Department Projects (from project directory)
  - Department Tools (from tools library)

- **Template-Driven (7 sections)**:
  - All other sections use templates with variable substitution

---

## Variable Usage by Section

| Section | Variables Used |
|---------|----------------|
| purpose | `{department_name}` |
| department_context | `{department_name}`, `{team_size}`, employee data, project data, tool data |
| base_context_integration | `{department_folder}` |
| department_instructions | `{department_name}`, `{department_folder}`, `{DAY}`, section numbers |
| department_vocabulary | `{department_name}`, vocabulary terms |
| project_matching | `{department_name}`, project data |
| quality_standards | `{department_activities}`, `{tool_usage}`, `{deliverables}` |
| example_usage | `{department_name}`, `{department_folder}`, `{DAY}`, focus areas |
| version_history | `{department_name}` |
| footer | `{department_name}` |

---

## Department-Specific Variations

### Section Mappings (MAIN PROMPT sections to emphasize)

| Department | Section Numbers |
|------------|----------------|
| HR | 20, 16, 3 |
| AI | 8, 9, 11, 3 |
| Video | 18, 8, 3 |
| Sales | 17, 3 |
| Design | 18, 8, 3 |
| Dev | 19, 9, 3 |
| LG | 17, 3 |

### Focus Areas (Report emphasis)

Each department has 3-4 focus areas that guide what to highlight in the daily reports.

### Vocabulary Categories

| Department | Categories |
|------------|------------|
| HR | Recruitment Terms, Onboarding Terms, Employee Management Terms |
| AI | AI & LLM Terms, Framework Terms, Technical Terms |
| Video | Video Production Terms, AI Video Terms, Video Formats |
| Sales | Sales Terms, Pipeline Terms |
| Design | Design Terms, Design Process Terms |
| Dev | Development Terms, Technical Terms |
| LG | Lead Generation Terms, Data & Research Terms |

---

## Validation Rules Summary

### Section-Level Validation
- ✅ All 10 sections must be present
- ✅ Sections must be in correct order
- ✅ All variables must be substituted
- ✅ All dependencies must be resolved

### Content-Level Validation
- ✅ Minimum length requirements
- ✅ Maximum length requirements
- ✅ Required keywords present
- ✅ Format consistency

### Data-Level Validation
- ✅ Employee data accessible
- ✅ Project data accessible
- ✅ Tool data accessible
- ✅ Vocabulary data accessible

---

## Generation Flow

```
1. Load Department Configuration
   ↓
2. Fetch Data Sources
   ├── Employee Directory
   ├── Project Directory
   ├── Tools Library
   └── Vocabulary Library
   ↓
3. Apply Templates
   ├── Substitute Variables
   ├── Format Data
   └── Assemble Sections
   ↓
4. Validate Structure
   ├── Check Completeness
   ├── Verify Variables
   └── Validate Formatting
   ↓
5. Generate Markdown File
   └── Save to Location
```

---

## Extension Points

### Adding New Classification
1. Add to `classifications.by_type` or `classifications.by_category`
2. Update section definitions
3. Update this summary document

### Adding New Section Type
1. Define section in `sections` array
2. Assign classification
3. Define template and variables
4. Update dependencies
5. Add to required sections

### Adding New Department
1. Add to `department_configurations`
2. Define section mappings
3. Specify focus areas
4. Add vocabulary categories
5. Test generation

---

## Context Integration Enhancements

### Intelligent Participant Identification

**Purpose**: Automatically identify participants in call transcripts

**Implementation**:
- Embed relevant employee subset in **department_context** section
- Add identification strategies to **department_instructions** section
- Include confidence level assessment in output format
- Flag unmatched participants for manual review

**Reference**: [docs/01_employee_directory_guidance.md](./docs/01_employee_directory_guidance.md)

**Example Integration**:
```markdown
### Department Employees (from Employee Directory)
- **Shelep Olha** (ID: 86641) - UI/UX designer | Ukraine
- **Bogun Polina** (ID: 87537) - UI/UX designer | Austria
[... remaining Design team members ...]

**Participant Identification**:
- Match names using direct match, contextual clues, and communication handles
- Assign confidence levels (High/Medium/Low)
- Flag unidentified participants for manual verification
```

---

### Intelligent Project Identification

**Purpose**: Automatically identify projects mentioned in transcripts

**Implementation**:
- Include relevant project subset in **project_matching** section
- Add abbreviation recognition
- Enable multi-lingual project name matching
- Reference known resources (Figma, Google Drive)

**Reference**: [docs/02_project_directory_guidance.md](./docs/02_project_directory_guidance.md)

**Example Integration**:
```markdown
### Department Projects (from Project Directory)
- **DGN (Design Studio)** - Design services platform
  - Keywords: Design Studio, DGN, design services
  - Resources: Logo, Google Drive, Figma
- **MDL EU/UA** - Market-specific versions
  - Keywords: MDL, European market, Ukrainian market
  - Resources: Figma designs (old and new versions)
[... relevant projects for department ...]

**Project Identification**:
- Match via direct name, abbreviation, or keywords
- Handle multi-lingual names (Russian, Ukrainian, English)
- Reference known resources when project identified
```

---

### Standardized Vocabulary Application

**Purpose**: Ensure consistent terminology across all departments

**Implementation**:
- Apply standardized action verbs (with action/process/result forms)
- Use department-specific object libraries
- Implement standard status, priority, and complexity values
- Apply RACI matrix for accountability

**Reference**: [docs/03_vocabulary_standards.md](./docs/03_vocabulary_standards.md)

**Quality Standards**:
- All tasks use ACTION + OBJECT + CONTEXT format
- Status values: not_started, in_progress, blocked, completed
- Priority values: critical, high, medium, low
- Complexity values: beginner, intermediate, advanced, expert
- RACI defined: Responsible, Accountable, Consulted, Informed

---

### Task Template Framework

**Purpose**: Structure all task extraction consistently

**Implementation**:
- Apply ACTION + OBJECT + CONTEXT format to all tasks
- Include complete task metadata (owner, priority, timeline, dependencies, status)
- Use Step Templates for procedures
- Use checklist templates for verification
- Assign RACI for accountability

**Reference**: [docs/04_task_object_framework.md](./docs/04_task_object_framework.md)

**Example Task Structure**:
```json
{
  "task_name": "Create employee onboarding documentation",
  "format": "ACTION + OBJECT + CONTEXT",
  "action": "Create",
  "object": "employee onboarding documentation",
  "context": "for new employee registration system",
  "owner": {
    "name": "Shelep Olha",
    "department": "Design",
    "profession": "UI/UX designer"
  },
  "priority": "high",
  "status": "not_started",
  "complexity": "intermediate",
  "related_project": "LibDev / Talents Microservice",
  "raci": {
    "responsible": "Shelep Olha (Design)",
    "accountable": "Nealova Evgeniya (HR Manager)",
    "consulted": ["Development Team"],
    "informed": ["All Department Leads"]
  }
}
```

---

### 21-Section Report Framework

**Purpose**: Provide comprehensive, consistent report structure

**Implementation**:
- Integrate full or partial 21-section framework based on call type
- Prioritize sections based on department (see section_mappings)
- Include department-specific sections (16-20)
- Enable cross-referencing across sections

**Reference**: [docs/05_21_section_framework.md](./docs/05_21_section_framework.md)

**Section Selection by Call Type**:
- **Project Planning**: Sections 1-4, 10, 13, 21
- **Technical Review**: Sections 1, 7, 9, 10, 19, 21
- **QA/Testing**: Sections 1, 3, 6, 7, 10, 21
- **Client Calls**: Sections 1, 2, 3, 10, 12, 17, 21
- **Department Meetings**: Sections 1, 2, 3, 11, 12, dept-specific (16-20), 21

---

### Department-Specific Customization

**Purpose**: Tailor prompts to department focus areas and workflows

**Implementation**:
- Apply section emphasis from department configurations
- Include department-specific focus areas (3-4 key areas)
- Reference common objects for the department
- Track department-specific key metrics
- Document typical activities and workflows

**Reference**: [docs/06_department_specific_patterns.md](./docs/06_department_specific_patterns.md)

**Department Section Mappings** (MAIN PROMPT sections to emphasize):

| Department | Primary Sections | Focus Areas Count | Team Size |
|------------|------------------|-------------------|-----------|
| HR | 20, 16, 3 | 4 | 2 |
| AI | 8, 9, 11, 3 | 4 | 3 |
| Video | 18, 8, 3 | 4 | 3 |
| Sales | 17, 3 | 4 | 1 |
| Design | 18, 8, 3 | 4 | 9 |
| Dev | 19, 9, 3 | 4 | 3 |
| LG | 16, 17, 3 | 4 | 11 |

**Example Department Customization** (Design):
```markdown
### Design Department Focus Areas
1. **UI/UX Design**: User interface design, wireframing, prototyping, user flows
2. **Graphic Design & Branding**: Logos, brand identity, marketing materials
3. **Project Execution**: Client projects, design reviews, asset organization
4. **AI Design Tools**: Midjourney, Leonardo.ai, Gamma AI, Figma plugins

### Common Design Objects
banners, headers, icons, illustrations, infographics, logos, presentations,
brandbooks, fonts, thumbnails, mockups, wireframes, prototypes, components

### Key Metrics
- Projects completed per week
- Revision rounds per project
- Client satisfaction scores
- Figma component library growth
- Design-to-development handoff quality
```

---

## Enhanced Generation Flow

```
1. Load Department Configuration (from docs/06)
   ├── Team composition (employees from docs/01)
   ├── Section emphasis (21-section framework from docs/05)
   ├── Focus areas (department-specific)
   └── Common objects and metrics
   ↓
2. Fetch Data Sources
   ├── Employee Directory (docs/01) → Participant matching
   ├── Project Directory (docs/02) → Project matching
   ├── Vocabulary Standards (docs/03) → Terminology
   └── Task Framework (docs/04) → Task structure
   ↓
3. Apply Templates with Enhanced Context
   ├── Substitute Variables
   ├── Embed Employee Subset
   ├── Embed Project Subset
   ├── Apply Vocabulary Standards
   ├── Structure with 21-Section Framework
   └── Customize for Department
   ↓
4. Validate Structure & Context
   ├── Check Completeness (all required sections)
   ├── Verify Employee Integration
   ├── Verify Project Integration
   ├── Validate Task Format (ACTION + OBJECT + CONTEXT)
   ├── Check Vocabulary Consistency
   └── Validate Department Customization
   ↓
5. Generate Enhanced Markdown File
   ├── Intelligent participant matching enabled
   ├── Intelligent project matching enabled
   ├── Standardized vocabulary applied
   ├── Task Templates structured
   ├── 21-section framework implemented
   └── Department patterns optimized
```

---

## Quality Enhancement Checklist

### Employee Integration
- [ ] Relevant employees from Employee Directory embedded
- [ ] Participant identification strategies included
- [ ] Confidence level system explained
- [ ] Multi-lingual name matching enabled
- [ ] Unmatched participant flagging included

### Project Integration
- [ ] Relevant projects from Project Directory embedded
- [ ] Project abbreviations documented
- [ ] Multi-lingual project names supported
- [ ] Resource references included (Figma, Google Drive)
- [ ] Project identification strategies explained

### Vocabulary Standards
- [ ] Standardized action verbs used (with 3 forms)
- [ ] Department-specific objects referenced
- [ ] Status/Priority/Complexity values standardized
- [ ] RACI matrix explained and applied
- [ ] Multi-language support documented

### Task Framework
- [ ] ACTION + OBJECT + CONTEXT format enforced
- [ ] Complete task metadata template provided
- [ ] Step Template structure included
- [ ] Checklist template structure included
- [ ] Task extraction quality criteria defined

### 21-Section Framework
- [ ] Relevant sections selected based on call type
- [ ] Section templates provided
- [ ] Department-specific sections emphasized (16-20)
- [ ] Cross-referencing enabled
- [ ] Section quality standards defined

### Department Customization
- [ ] Section emphasis matches department configuration
- [ ] Focus areas documented (3-4 areas)
- [ ] Common objects listed
- [ ] Key metrics defined
- [ ] Typical activities described
- [ ] Cross-department collaboration noted

---

## Implementation Priorities

### Phase 1: Core Context Integration (COMPLETED)
✅ Create comprehensive documentation in docs/ folder
✅ Document employee directory with identification strategies
✅ Document project directory with matching patterns
✅ Document vocabulary standards
✅ Document task + object framework
✅ Document 21-section framework
✅ Document department-specific patterns

### Phase 2: Prompt Constructor Enhancement (NEXT)
- [ ] Update constructor to reference docs/ guidance
- [ ] Implement employee directory integration
- [ ] Implement project directory integration
- [ ] Apply vocabulary standardization
- [ ] Integrate task framework templates
- [ ] Apply 21-section framework structure
- [ ] Apply department-specific customization

### Phase 3: Validation & Testing
- [ ] Validate generated prompts against quality checklist
- [ ] Test participant matching accuracy
- [ ] Test project matching accuracy
- [ ] Verify vocabulary consistency
- [ ] Test task extraction with framework
- [ ] Validate 21-section coverage
- [ ] Verify department customization effectiveness

### Phase 4: Refinement & Optimization
- [ ] Gather feedback on generated prompts
- [ ] Optimize matching algorithms
- [ ] Refine templates based on usage
- [ ] Enhance documentation with examples
- [ ] Create quick-reference guides
- [ ] Build automated quality checking tools

---

## Success Metrics

### Accuracy Metrics
- **Participant Identification Rate**: % of participants correctly matched (Target: >95%)
- **Project Identification Rate**: % of projects correctly matched (Target: >90%)
- **Vocabulary Consistency**: % of terms matching standards (Target: >98%)
- **Task Format Compliance**: % of tasks following ACTION + OBJECT + CONTEXT (Target: 100%)

### Quality Metrics
- **Prompt Completeness**: % of required sections present (Target: 100%)
- **Context Integration**: % of prompts with employee/project directories (Target: 100%)
- **Department Alignment**: % of prompts matching department patterns (Target: 100%)
- **Documentation Coverage**: % of prompts with adequate instructions (Target: 95%)

### Efficiency Metrics
- **Generation Time**: Time to generate complete prompt (Target: <5 minutes)
- **Manual Refinement Required**: % of prompts needing manual editing (Target: <10%)
- **User Satisfaction**: Rating from prompt users (Target: >4.5/5)
- **Reusability**: % of template components reused across departments (Target: >70%)

---

*Last Updated: November 7, 2025*
*Enhanced with comprehensive organizational context from SummariesOct knowledge base*

