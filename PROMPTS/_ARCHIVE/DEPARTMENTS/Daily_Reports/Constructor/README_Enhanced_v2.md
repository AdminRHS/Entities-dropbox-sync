# Prompt Parts Constructor - Enhanced v2.0 Documentation

## Overview

This folder contains the **enhanced system** for constructing department-specific daily report prompts with comprehensive organizational context integration. The system now includes intelligent participant/project matching, standardized task frameworks, and department-optimized configurations.

**Enhancement Version**: 2.0 (November 7, 2025)
**Based on**: Comprehensive organizational context from SummariesOct knowledge base
**Previous Version**: v1.0 (November 25, 2025) - see `README.md` for original documentation

---

## What's New in v2.0

### Major Enhancements

✅ **Intelligent Participant Identification**
- Auto-match against 32-employee directory
- Confidence level system (High/Medium/Low)
- 5 identification strategies
- Multi-lingual name recognition
- Unmatched participant flagging

✅ **Intelligent Project Matching**
- Auto-match against 31+ project directory
- Resource references (Figma, Google Drive)
- 6 recognition strategies
- Multi-lingual project names
- Abbreviation support

✅ **Standardized Task Framework**
- ACTION + OBJECT + CONTEXT structure
- Complete task metadata
- RACI accountability matrix
- Step and checklist templates
- Quality validation built-in

✅ **21-Section Framework Integration**
- Comprehensive report structure
- Flexible section selection by call type
- Department-specific sections (16-20)
- Cross-referencing capabilities

✅ **Enhanced Vocabulary**
- Standardized terminology
- Action verbs with 3 forms
- Department-specific object libraries
- 636+ profession variations
- Multi-language support

✅ **Department Optimization**
- Focus areas for each of 7 departments
- Department-specific metrics and KPIs
- Typical activities and workflows
- Cross-department collaboration patterns

✅ **Comprehensive Documentation**
- 6 detailed guidance documents
- Complete variable mapping guide
- Enhanced prompt template
- Quality checklists and success metrics

---

## File Structure

```
constructor/
├── README.md                                    # Original v1.0 documentation
├── README_Enhanced_v2.md                        # This file - v2.0 documentation
├── classification_summary.md                    # Enhanced classification with context integration
├── prompt_parts_structure.json                 # Original JSON structure (v1.0)
├── TEMPLATE_Enhanced_Department_Prompt.md       # ⭐ NEW: Enhanced prompt template
├── TEMPLATE_VARIABLE_MAPPING.md                # ⭐ NEW: Variable population guide
└── docs/                                        # ⭐ NEW: Comprehensive guidance documentation
    ├── README.md                                # Documentation overview
    ├── 01_employee_directory_guidance.md        # 32 employees, 5 identification strategies
    ├── 02_project_directory_guidance.md         # 31+ projects, 6 recognition strategies
    ├── 03_vocabulary_standards.md               # Standardized terminology framework
    ├── 04_task_object_framework.md              # ACTION + OBJECT + CONTEXT structure
    ├── 05_21_section_framework.md               # Comprehensive report structure
    └── 06_department_specific_patterns.md       # 7 department configurations
```

---

## Quick Start Guide

### Option 1: Use Enhanced Template (Recommended)

1. **Open Template**: `TEMPLATE_Enhanced_Department_Prompt.md`
2. **Open Mapping Guide**: `TEMPLATE_VARIABLE_MAPPING.md`
3. **Select Department**: Choose from HR, AI, Video, Sales, Design, Dev, or LG
4. **Find Configuration**: Look up department in mapping guide
5. **Replace Variables**: Use find-replace for all `{VARIABLE}` placeholders
6. **Validate**: Check against quality checklist
7. **Save**: As `PROMPT_{Department}_Daily_Report_Enhanced.md`

### Option 2: Reference Documentation

1. **Read docs/README.md**: Understand documentation structure
2. **Review docs/06**: Find your department configuration
3. **Reference docs/01**: Get employee list for department
4. **Reference docs/02**: Get project list for department
5. **Reference docs/03**: Get vocabulary and terminology
6. **Reference docs/04**: Understand task framework
7. **Reference docs/05**: Review 21-section structure
8. **Build Prompt**: Construct using all context

### Option 3: Study Example

1. **Open Existing Prompt**: e.g., `PROMPT_Design_Daily_Report.md`
2. **Compare with Template**: See what's enhanced in v2.0
3. **Review Mapping Guide**: Understand variable sources
4. **Generate New Version**: Create enhanced version for your department

---

## Core Files Explained

### TEMPLATE_Enhanced_Department_Prompt.md ⭐

**Purpose**: Master template for all department prompts with v2.0 enhancements

**Features**:
- Intelligent participant identification section
- Intelligent project matching section
- Comprehensive vocabulary and terminology
- Enhanced task extraction with complete metadata
- 21-section framework integration
- Department-specific metrics and KPIs
- Quality standards and validation
- Multi-lingual support

**Variables** (50+ total):
- Department: name, mission, team size, focus areas
- Employees: full list with identification strategies
- Projects: full list with resources and abbreviations
- Tools: AI tools, traditional tools, communication tools
- Vocabulary: categories, terms, objects, actions
- Metrics: KPIs, formulas, targets
- Collaboration: patterns and details

**Usage**: Replace all `{VARIABLE}` placeholders using `TEMPLATE_VARIABLE_MAPPING.md`

---

### TEMPLATE_VARIABLE_MAPPING.md ⭐

**Purpose**: Complete guide for populating template variables

**Contents**:
- Variable reference table (50+ variables)
- Department configurations (all 7 departments)
- Employee list formats
- Project list formats
- Section emphasis details
- Metrics and KPIs
- Vocabulary and terminology
- Collaboration patterns
- Usage instructions

**How to Use**:
1. Find your department section
2. Copy provided values
3. Replace corresponding variables in template
4. Validate completeness

---

### docs/ Folder ⭐

**Purpose**: Comprehensive guidance documentation extracted from SummariesOct

#### docs/01_employee_directory_guidance.md
- **32 employees** across 7 departments
- **5 identification strategies**: Direct match, contextual clues, communication handles, voice/speech patterns, multi-lingual matching
- **Confidence levels**: High/Medium/Low with reasoning
- **Integration guidelines**: How to embed in prompts

#### docs/02_project_directory_guidance.md
- **31+ active projects** with full details
- **6 recognition strategies**: Direct name, abbreviation, keyword, multi-lingual, contextual, resource-based
- **Project categories**: Service platforms, internal systems, client projects, etc.
- **Resource references**: Figma links, Google Drive folders
- **Integration guidelines**: How to enable matching

#### docs/03_vocabulary_standards.md
- **Company-specific vocabulary**: LG, Sales, AI, Design, Dev, Video, HR
- **ACTION + OBJECT framework**: Complete structure
- **636+ profession variations**: All recognized job titles
- **Multi-language support**: Russian, Ukrainian, English, Polish
- **Standard values**: Status, priority, complexity
- **Integration guidelines**: Terminology consistency

#### docs/04_task_object_framework.md
- **ACTION + OBJECT + CONTEXT** structure
- **Standard actions library**: With 3 forms (action/process/result)
- **Standard objects library**: By department/profession
- **Step Templates**: Procedure format
- **Checklist templates**: Verification format
- **RACI matrix**: Accountability definitions
- **Integration guidelines**: Task extraction rules

#### docs/05_21_section_framework.md
- **21 comprehensive sections**: Complete structure
- **Section specifications**: Purpose, format, requirements
- **Call type guidance**: Project planning, technical review, QA, client, department meetings
- **Department sections**: 16-20 (LG, Sales, Design, Dev, HR)
- **Quality standards**: Per section criteria
- **Integration guidelines**: Section selection rules

#### docs/06_department_specific_patterns.md
- **7 department configurations**: Complete details
- **Team compositions**: With employee lists
- **Focus areas**: 3-4 key areas per department
- **Common objects**: Department-specific
- **Key metrics**: KPIs and formulas
- **Typical activities**: Workflows and processes
- **Collaboration patterns**: Cross-department
- **Integration guidelines**: Department optimization

#### docs/README.md
- **Documentation overview**: All files explained
- **Usage instructions**: How to use each document
- **Quality standards**: Validation criteria
- **Integration guidelines**: Step-by-step process
- **Key improvements**: What v2.0 enables

---

### classification_summary.md (Enhanced)

**Original Purpose**: Visual summary of prompt classification system

**v2.0 Enhancements**:
- Documentation resources section
- Context integration enhancements (6 areas)
- Enhanced generation flow diagram
- Quality enhancement checklist
- Implementation priorities (4 phases)
- Success metrics (accuracy, quality, efficiency)

**New Sections**:
- Intelligent Participant Identification
- Intelligent Project Identification
- Standardized Vocabulary Application
- Task Template Framework
- 21-Section Report Framework
- Department-Specific Customization

---

### prompt_parts_structure.json (v1.0)

**Purpose**: Original JSON structure for programmatic generation

**Status**: Original v1.0 structure maintained for compatibility

**Future Enhancement**: Will be updated to v2.0 with enhanced context integration for automated generation

**Current Use**: Reference for original 10-section structure and variable definitions

---

## How to Generate Enhanced Prompts

### Manual Method (Current)

**Step-by-Step Process:**

1. **Prepare Environment**
   ```
   - Open: TEMPLATE_Enhanced_Department_Prompt.md
   - Open: TEMPLATE_VARIABLE_MAPPING.md
   - Open: docs/06_department_specific_patterns.md
   ```

2. **Select Department**
   - Choose from: HR, AI, Video, Sales, Design, Dev, or LG
   - Find configuration in TEMPLATE_VARIABLE_MAPPING.md

3. **Gather Employee Data**
   - Open: docs/01_employee_directory_guidance.md
   - Filter employees by selected department
   - Copy formatted employee list

4. **Gather Project Data**
   - Open: docs/02_project_directory_guidance.md
   - Filter projects relevant to department
   - Copy project list with resources

5. **Gather Vocabulary**
   - Open: docs/03_vocabulary_standards.md
   - Find department-specific terms
   - Copy vocabulary categories

6. **Gather Metrics**
   - Refer to: docs/06_department_specific_patterns.md
   - Find department metrics section
   - Copy KPIs and formulas

7. **Replace Variables**
   - Use find-replace in template
   - Replace all `{VARIABLE}` placeholders
   - Use values from mapping guide

8. **Validate**
   - Check: All variables replaced
   - Check: All lists populated
   - Check: Formatting consistent
   - Check: Quality Checklist Items

9. **Save**
   - Filename: `PROMPT_{Department}_Daily_Report_Enhanced.md`
   - Location: Parent directory or designated location

10. **Test**
    - Review completeness
    - Validate against quality standards
    - Test with actual transcript if available

### Automated Method (Future)

**Planned Script**:
```python
def generate_enhanced_prompt(department):
    # Load configuration
    config = load_department_config(department)

    # Fetch data
    employees = fetch_employees(department)
    projects = fetch_projects(department)
    vocabulary = fetch_vocabulary(department)
    metrics = fetch_metrics(department)

    # Load template
    template = load_template('TEMPLATE_Enhanced_Department_Prompt.md')

    # Replace variables
    prompt = template
    for variable, value in config.items():
        prompt = prompt.replace(f'{{{variable}}}', value)

    # Validate
    if validate_prompt(prompt):
        save_prompt(prompt, department)
        return True
    return False
```

---

## Quality Assurance

### Pre-Generation Checklist

- [ ] Department configuration reviewed in docs/06
- [ ] Employee list prepared from docs/01
- [ ] Project list prepared from docs/02
- [ ] Vocabulary gathered from docs/03
- [ ] Task framework understood from docs/04
- [ ] Section structure reviewed in docs/05
- [ ] Template variables mapped
- [ ] All data sources accessible

### Post-Generation Validation

#### Content Completeness
- [ ] All sections present (Purpose through Footer)
- [ ] All variables replaced (no `{VARIABLE}` remaining)
- [ ] Employee list complete with IDs and departments
- [ ] Project list includes resources
- [ ] Vocabulary categories populated
- [ ] Metrics and KPIs defined
- [ ] Focus areas documented

#### Context Integration
- [ ] Participant identification strategies included
- [ ] Project matching strategies included
- [ ] Task framework (ACTION + OBJECT + CONTEXT) explained
- [ ] RACI matrix defined
- [ ] 21-section framework referenced
- [ ] Department-specific sections emphasized
- [ ] Quality standards documented

#### Formatting Consistency
- [ ] Markdown headers properly structured
- [ ] Lists formatted correctly
- [ ] Tables formatted correctly
- [ ] Code blocks used appropriately
- [ ] Links functional
- [ ] Bold/italic used consistently

#### Department Optimization
- [ ] Focus areas match department (4 areas)
- [ ] Metrics relevant to department
- [ ] Section emphasis correct for department
- [ ] Common objects appropriate
- [ ] Collaboration patterns accurate

---

## Success Metrics

### v2.0 Enhancement Goals

**Accuracy Metrics**:
- Participant Identification Rate: >95% (vs ~70% in v1.0)
- Project Identification Rate: >90% (vs ~60% in v1.0)
- Vocabulary Consistency: >98% (vs ~80% in v1.0)
- Task Format Compliance: 100% (vs ~60% in v1.0)

**Quality Metrics**:
- Prompt Completeness: 100% (all sections present)
- Context Integration: 100% (employee/project directories embedded)
- Department Alignment: 100% (patterns matched)
- Documentation Coverage: >95% (adequate instructions)

**Efficiency Metrics**:
- Generation Time: <30 min manual, <5 min automated (future)
- Manual Refinement Required: <10% (vs ~40% in v1.0)
- User Satisfaction: >4.5/5
- Reusability: >70% template components

---

## Comparison: v1.0 vs v2.0

| Feature | v1.0 | v2.0 |
|---------|------|------|
| **Employee Matching** | Manual | Automatic with confidence levels |
| **Project Matching** | Manual | Automatic with resources |
| **Task Structure** | Free-form | ACTION + OBJECT + CONTEXT |
| **Task Metadata** | Minimal | Complete (RACI, dependencies, etc.) |
| **Report Structure** | 14 sections | 21-section framework (flexible) |
| **Vocabulary** | Informal | Standardized across all departments |
| **Documentation** | JSON + README | 6 guidance docs + mapping guide |
| **Multi-lingual** | Limited | Full support (RU, UK, EN, PL) |
| **Quality Validation** | Manual | Built-in checklists |
| **Department Config** | Basic | Comprehensive (focus, metrics, collaboration) |

---

## Implementation Phases

### Phase 1: Documentation (COMPLETED ✅)
- [x] Create comprehensive guidance documents in docs/
- [x] Document employee directory (docs/01)
- [x] Document project directory (docs/02)
- [x] Document vocabulary standards (docs/03)
- [x] Document task framework (docs/04)
- [x] Document 21-section framework (docs/05)
- [x] Document department patterns (docs/06)
- [x] Create docs/README.md
- [x] Create enhanced template
- [x] Create variable mapping guide
- [x] Update classification_summary.md

### Phase 2: Manual Generation (IN PROGRESS)
- [ ] Generate enhanced Design prompt (example)
- [ ] Generate enhanced prompts for remaining 6 departments
- [ ] Validate all prompts against quality checklist
- [ ] Test prompts with actual transcripts
- [ ] Gather feedback and refine
- [ ] Update existing prompts to v2.0

### Phase 3: Automation (FUTURE)
- [ ] Create Python/Node.js generation script
- [ ] Implement variable replacement automation
- [ ] Add validation automation
- [ ] Create CLI tool for generation
- [ ] Add batch generation capability
- [ ] Integrate with existing workflows

### Phase 4: Enhancement (FUTURE)
- [ ] Add more metrics and KPIs
- [ ] Expand vocabulary library
- [ ] Add more identification patterns
- [ ] Create visual dashboard for metrics
- [ ] Build web interface for generation
- [ ] Add AI-assisted optimization

---

## Support & Resources

### Documentation
- **Enhanced Template**: `TEMPLATE_Enhanced_Department_Prompt.md`
- **Mapping Guide**: `TEMPLATE_VARIABLE_MAPPING.md`
- **Guidance Docs**: `docs/` folder (6 documents)
- **Original Docs**: `README.md`, `prompt_parts_structure.json`

### Reference Materials
- **SummariesOct**: Source organizational knowledge base
- **MAIN PROMPT v3.md**: Comprehensive call organization framework
- **PROMPT_Daily_Report_Collection.md**: Daily report automation template

### Examples
- Existing v1.0 prompts in parent directory:
  - `PROMPT_HR_Daily_Report.md`
  - `PROMPT_AI_Daily_Report.md`
  - `PROMPT_Video_Daily_Report.md`
  - `PROMPT_Sales_Daily_Report.md`
  - `PROMPT_Design_Daily_Report.md`
  - `PROMPT_Dev_Daily_Report.md`
  - `PROMPT_LG_Daily_Report.md`

---

## Troubleshooting

### Common Issues

**Issue**: Variables still showing as `{VARIABLE}`
- **Solution**: Use mapping guide to find correct replacement value
- **Check**: TEMPLATE_VARIABLE_MAPPING.md for exact format

**Issue**: Employee list incomplete
- **Solution**: Review docs/01, ensure all department members included
- **Check**: Employee count matches {TEAM_SIZE}

**Issue**: Projects not relevant to department
- **Solution**: Review docs/02, filter by department relevance
- **Check**: docs/06 for typical department projects

**Issue**: Metrics unclear
- **Solution**: Review docs/06 for department-specific KPIs
- **Check**: Formula definitions and target values

**Issue**: Section emphasis wrong
- **Solution**: Review docs/06 section mappings
- **Check**: Primary sections match department configuration

---

## Version History

**v2.0** - November 7, 2025
- Complete overhaul with comprehensive organizational context
- Added intelligent participant/project matching
- Implemented ACTION + OBJECT + CONTEXT task framework
- Integrated 21-section report framework
- Created 6 comprehensive guidance documents
- Added variable mapping guide
- Enhanced quality validation
- Added multi-lingual support
- Department optimization complete

**v1.0** - November 25, 2025
- Initial JSON structure creation
- Basic 10-section prompt structure
- 7 departments configured
- Simple classification system
- Basic formation rules
- Manual variable substitution

---

## Next Steps

1. **For New Users**: Start with `docs/README.md` to understand documentation structure

2. **To Generate Prompt**: Follow "Quick Start Guide" Option 1 above

3. **To Understand Context**: Read guidance docs in order (01 → 06)

4. **To Validate Quality**: Use checklists in this document

5. **To Provide Feedback**: Document issues and suggestions for future versions

---

*Last Updated: November 7, 2025*
*Version: 2.0*
*Status: Phase 1 Complete, Phase 2 In Progress*
*Documentation: Complete*
*Template: Ready for Use*
