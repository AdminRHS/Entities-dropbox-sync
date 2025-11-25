# {DEPARTMENT_NAME} Department - Daily Report Collection Prompt (Enhanced v2.0)

## Purpose

This prompt is specifically designed for the **{DEPARTMENT_NAME} Department** to process call transcriptions and generate comprehensive daily activity reports. It integrates:
- Complete call organization framework with intelligent matching
- {DEPARTMENT_NAME}-specific context and employee directory
- Enhanced participant and project identification
- Standardized task extraction framework
- Department-optimized report generation

**Enhancement Version:** 2.0 (November 7, 2025)
**Based on:** Comprehensive organizational context from SummariesOct knowledge base

---

## Documentation References

This prompt is enhanced with comprehensive guidance from:
- **Employee Directory**: Automatic participant identification with confidence levels
- **Project Directory**: Intelligent project matching with multi-lingual support
- **Vocabulary Standards**: Standardized terminology and ACTION + OBJECT + CONTEXT framework
- **21-Section Framework**: Comprehensive report structure
- **Department Patterns**: {DEPARTMENT_NAME}-specific focus areas and metrics

> **Reference**: See [constructor/docs/](constructor/docs/) for detailed guidance documentation

---

## Department Context: {DEPARTMENT_NAME}

### Department Overview
**Mission:** {DEPARTMENT_MISSION}
**Team Size:** {TEAM_SIZE} employees ({TEAM_PERCENTAGE}% of company)
**Department Code:** {DEPT_CODE}

**Key Responsibilities:**
{KEY_RESPONSIBILITIES_LIST}

**Focus Areas ({FOCUS_AREAS_COUNT}):**
{FOCUS_AREAS_LIST}

---

### {DEPARTMENT_NAME} Department Employees

> **Intelligent Participant Identification Enabled**
> - Automatic matching against 32-employee directory
> - Confidence levels: High/Medium/Low
> - Multi-lingual name recognition (Russian, Ukrainian, English)
> - Contextual clue processing
> - Unmatched participants flagged for manual verification

{EMPLOYEE_LIST_WITH_FULL_DETAILS}

**Participant Identification Strategies:**
1. **Direct Name Match**: Match first/last name or full name (case-insensitive, handle variations)
2. **Contextual Clues**: Department context, project mentions, role descriptions, location references
3. **Communication Handles**: Telegram handles (@username), email addresses
4. **Professional Context**: Discussing department-specific tools, processes, or terminology
5. **Multi-lingual Matching**: Handle Russian/Ukrainian diminutives and transliterations

**Output Format for Participants:**
```
**Employee Name** (ID: xxxxx) - Role | Department | Confidence: High/Medium/Low
[Reason if Medium/Low confidence]
```

---

### {DEPARTMENT_NAME}-Specific Projects

> **Intelligent Project Identification Enabled**
> - Automatic matching against 31+ project directory
> - Abbreviation recognition
> - Multi-lingual project names supported
> - Resource references (Figma, Google Drive) included
> - Confidence levels assigned

{PROJECT_LIST_WITH_RESOURCES}

**Project Identification Strategies:**
1. **Direct Name Match**: Exact project names
2. **Abbreviation Match**: Recognize standard abbreviations (RH, DGN, l-gn, etc.)
3. **Keyword Match**: Descriptive keywords and themes
4. **Multi-lingual Names**: Russian/Ukrainian project names
5. **Resource Context**: When Figma files or Google Drive folders mentioned

**Project Abbreviations Quick Reference:**
{PROJECT_ABBREVIATIONS}

**Output Format for Projects:**
```
**Project Name** - Matched via [method] - Confidence: High/Medium/Low
Resources: [Figma link] [Google Drive link]
```

---

### {DEPARTMENT_NAME}-Specific Tools

**AI Tools & Platforms:**
{AI_TOOLS_LIST}

**Traditional/Core Tools:**
{TRADITIONAL_TOOLS_LIST}

**Communication & Documentation:**
{COMMUNICATION_TOOLS_LIST}

---

### {DEPARTMENT_NAME} Vocabulary & Terminology

> **Standardized Vocabulary Applied**
> - ACTION + OBJECT + CONTEXT format for all tasks
> - Standard status values: not_started, in_progress, blocked, completed
> - Standard priority values: critical, high, medium, low
> - Standard complexity values: beginner, intermediate, advanced, expert

**Department-Specific Terms:**

{VOCABULARY_CATEGORIES_WITH_TERMS}

**Common {DEPARTMENT_NAME} Objects:**
{COMMON_OBJECTS_LIST}

**Standard Actions (with 3 forms):**
{STANDARD_ACTIONS_WITH_FORMS}

---

## Base Context Integration

This prompt integrates comprehensive organizational knowledge from:

### 1. MAIN PROMPT v3.md
- **Company Context**: Remote Helpers - AI-First, Human-Centered organization
- **Employee Directory**: 32 employees across 7 departments
  - HR (2), AI (3), Video (3), Sales (1), Design (9), Dev (3), LG (11)
- **Project Directory**: 31+ active projects with resources
- **21-Section Framework**: Comprehensive extraction structure
- **Intelligent Matching**: Auto-identify participants and projects
- **Template Operations**: Task, Step, Checklist templates with RACI
- **Multi-language Support**: Russian, Ukrainian, English, Polish

### 2. PROMPT_Daily_Report_Collection.md
- **Report Structure**: 14-section daily report template
- **Folder Organization**: `/Nov25/{DEPARTMENT_FOLDER}/Reports/{DAY}/`
- **Metrics Extraction**: Department-specific KPIs and statistics
- **Quality Standards**: Content and formatting requirements

### 3. Enhanced Context Documentation
- **Employee Directory Guidance**: 5 identification strategies with confidence levels
- **Project Directory Guidance**: 6 recognition strategies with resources
- **Vocabulary Standards**: Comprehensive terminology and framework
- **Task Framework**: ACTION + OBJECT + CONTEXT with complete metadata
- **21-Section Framework**: Flexible section selection by call type
- **Department Patterns**: {DEPARTMENT_NAME}-specific configurations

---

## {DEPARTMENT_NAME}-Specific Instructions

### Step 1: Read Department Prompt Log

Read the {DEPARTMENT_NAME} department prompt log file:
- **File**: `Dropbox/Nov25/{DEPARTMENT_FOLDER}/{DEPARTMENT_NAME} prompt log.md`
- **Purpose**: Collect all {DEPARTMENT_NAME} activities from the day
- **Action**: Extract prompts, tasks, and activities logged

---

### Step 2: Process Call Transcripts (if applicable)

When processing {DEPARTMENT_NAME}-related call transcripts, apply the 21-Section Framework with emphasis on:

**{DEPARTMENT_NAME}-Specific Sections to Emphasize:**

{SECTION_EMPHASIS_DETAILS}

**Section Selection by Call Type:**
- **Project Planning Calls**: Sections 1-4, 10, 13, 21
- **Technical Review Calls**: Sections 1, 7, 9, 10, 19, 21
- **QA/Testing Calls**: Sections 1, 3, 6, 7, 10, 21
- **Client Calls**: Sections 1, 2, 3, 10, 12, 17, 21
- **Department Meetings**: Sections 1, 2, 3, 11, 12, {DEPT_SPECIFIC_SECTION}, 21

**Extraction Focus:**
{EXTRACTION_FOCUS_POINTS}

**Task Extraction Requirements:**
- Use **ACTION + OBJECT + CONTEXT** format for all tasks
- Match task owner to Employee Directory (include ID, department, role)
- Assign priority (critical/high/medium/low)
- Set status (not_started/in_progress/blocked/completed)
- Assess complexity (beginner/intermediate/advanced/expert)
- Define success criteria
- Identify dependencies
- Match related project to Project Directory
- Assign RACI (Responsible, Accountable, Consulted, Informed)

**Task Structure Template:**
```markdown
### [ACTION] [OBJECT] [CONTEXT]
- **Description**: Full task description
- **Owner**: Employee Name (ID: xxxxx) - Role | Department
- **Priority**: critical/high/medium/low
- **Timeline**: Due date, Estimated duration
- **Dependencies**: Prerequisites or blocking items
- **Status**: not_started/in_progress/blocked/completed
- **Complexity**: beginner/intermediate/advanced/expert
- **Related Project**: Project Name (matched from directory)
- **Success Criteria**: How to know it's complete
- **RACI**:
  - Responsible: Person doing the work
  - Accountable: Person ultimately answerable (ONE person only)
  - Consulted: People providing input
  - Informed: People kept updated
```

---

### Step 3: Generate {DEPARTMENT_NAME} Daily Activity Report

**Output File Location:**
`/Nov25/{DEPARTMENT_FOLDER}/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**Report Structure (14 Sections):**

#### 1. Executive Summary
```markdown
**Report Period:** November {DAY}, 2025
**Department:** {DEPARTMENT_NAME}
**Team Size:** {TEAM_SIZE} employees
**Total Activities:** [count]
**Overall Status:** [summary]

[2-3 sentence executive summary highlighting key activities, decisions, and impact]
```

#### 2. {DEPARTMENT_NAME} Department Activities
```markdown
### {DEPARTMENT_ACTIVITY_CATEGORY_1}
{ACTIVITIES_DESCRIPTION}

### {DEPARTMENT_ACTIVITY_CATEGORY_2}
{ACTIVITIES_DESCRIPTION}

[Continue for all department-specific activity categories]
```

**{DEPARTMENT_NAME} Activity Categories:**
{ACTIVITY_CATEGORIES_LIST}

#### 3. Tool Integration Activities
```markdown
### AI Tools Used
- **Tool Name** - Purpose - Activities - Results

### Traditional Tools Used
- **Tool Name** - Purpose - Activities - Results

### Tool Integration Highlights
[AI tool adoptions, new integrations, efficiency gains]
```

#### 4. Deliverables
```markdown
### Completed Deliverables
- [x] Deliverable 1 - Description - Owner - Project

### In-Progress Deliverables
- [ ] Deliverable 1 - Description - Owner - Project - % Complete

### Planned Deliverables
- [ ] Deliverable 1 - Description - Owner - Project - Timeline
```

#### 5. Metrics and Statistics

**{DEPARTMENT_NAME}-Specific Metrics:**
{KEY_METRICS_WITH_FORMULAS}

**Example Table Format:**
```markdown
| Metric | Target | Actual | Status | Trend |
|--------|--------|--------|--------|-------|
| {Metric 1} | {value} | {value} | ✅/⚠️/❌ | ↑/↓/→ |
```

#### 6. Key Deliverables (Summary)
High-level list of major accomplishments

#### 7. Department Impact Analysis
```markdown
**Impact Level:** High/Medium/Low
**Impact Categories:**
- Efficiency Improvements: [description]
- Quality Enhancements: [description]
- Process Optimizations: [description]
- Team Capabilities: [description]

**Quantifiable Benefits:**
- Time saved: [hours/percentage]
- Cost reduction: [amount/percentage]
- Quality improvement: [metrics]
```

#### 8. Technical Achievements
```markdown
### System Improvements
[Infrastructure, architecture, performance improvements]

### Tool Integrations
[New tools integrated, enhanced capabilities]

### Process Optimizations
[Workflow improvements, automation implementations]

### Innovation & Experimentation
[New approaches tested, R&D activities]
```

#### 9. Challenges and Solutions
```markdown
### Challenge 1: [Title]
- **Description**: [What the challenge was]
- **Impact**: [How it affected work]
- **Solution**: [How it was resolved]
- **Outcome**: [Result of solution]
- **Owner**: Employee Name (ID)

[Repeat for all challenges]
```

#### 10. Files Created/Modified Summary
```markdown
- `/path/to/file1.ext` - Created - Purpose
- `/path/to/file2.ext` - Modified - Changes made
```

#### 11. Recommendations for Follow-up
```markdown
### Immediate Actions (Next 24-48 hours)
- [ ] Action item 1 - Owner - Reason

### Short-term Actions (This week)
- [ ] Action item 1 - Owner - Reason

### Long-term Considerations
- [ ] Item 1 - Context - Timeline
```

#### 12. Success Indicators
```markdown
- [x] All planned {DEPARTMENT_NAME} activities completed
- [x] All {TOOL_CATEGORY} tools successfully used
- [x] All {DELIVERABLE_TYPE} deliverables produced
- [x] Quality standards met
- [x] Documentation updated
- [ ] [Any uncompleted items with explanation]
```

#### 13. Conclusion
```markdown
**Summary**: [1-2 sentence summary of the day's work]

**Key Achievements**:
- Achievement 1 (with impact)
- Achievement 2 (with impact)
- Achievement 3 (with impact)

**{DEPARTMENT_NAME} Department Impact**: [How this work contributes to department and company goals]

**Status**: Complete/Ongoing/Needs Follow-up
```

#### 14. Report Footer
```markdown
---
**Report Generated:** {DATE_TIME}
**Department:** {DEPARTMENT_NAME}
**Team Size:** {TEAM_SIZE}
**Report Status:** Complete
**Generated By:** AI Assistant with Enhanced Prompt v2.0

---

*Enhanced with comprehensive organizational context*
*Participant and project matching: Enabled*
*Task framework: ACTION + OBJECT + CONTEXT*
*Quality assurance: Validated*

---
*End of Report*
```

---

## Quality Standards & Validation

### Content Requirements
- [ ] All {DEPARTMENT_ACTIVITIES} documented with detail
- [ ] All participants matched to Employee Directory with confidence levels
- [ ] All projects matched to Project Directory with resources
- [ ] All tasks use ACTION + OBJECT + CONTEXT format
- [ ] All tasks have complete metadata (owner, priority, status, RACI, etc.)
- [ ] All {TOOL_CATEGORY} tool usage documented
- [ ] All {DELIVERABLE_TYPE} deliverables tracked
- [ ] All metrics calculated using standard formulas
- [ ] Impact analysis provided with quantifiable benefits
- [ ] Challenges documented with solutions
- [ ] Follow-up actions clearly defined with owners

### Formatting Requirements
- [ ] Markdown format with proper headers (##, ###, ####)
- [ ] Tables used for statistics and metrics
- [ ] Bullet lists for achievements and activities
- [ ] Checkboxes for completed items and success indicators
- [ ] Consistent section structure across all reports
- [ ] Code blocks for file paths and technical details
- [ ] Bold for emphasis on key terms
- [ ] Links formatted as [text](url)

### Vocabulary Consistency
- [ ] All action verbs from standardized list
- [ ] All objects from department-specific library
- [ ] Status values standardized (not_started, in_progress, blocked, completed)
- [ ] Priority values standardized (critical, high, medium, low)
- [ ] Complexity values standardized (beginner, intermediate, advanced, expert)
- [ ] RACI matrix properly applied

### Intelligent Matching Validation
- [ ] All participants matched with confidence levels
- [ ] Unidentified participants flagged for manual review
- [ ] All projects matched with confidence levels
- [ ] Project resources referenced when identified
- [ ] Multi-lingual names handled correctly

---

## Example Usage

### Command to AI Assistant:

```
Process {DEPARTMENT_NAME} department activities and create comprehensive daily activity report for November [DAY], 2025.

**Instructions:**
1. Read {DEPARTMENT_NAME} prompt log: Dropbox/Nov25/{DEPARTMENT_FOLDER}/{DEPARTMENT_NAME} prompt log.md
2. Process any {DEPARTMENT_NAME}-related call transcripts using MAIN PROMPT v3.md framework with enhanced matching
3. Apply intelligent participant identification (Employee Directory matching with confidence levels)
4. Apply intelligent project identification (Project Directory matching with resources)
5. Extract all tasks using ACTION + OBJECT + CONTEXT format with complete metadata
6. Create Reports/{DAY} folder in {DEPARTMENT_NAME} department
7. Generate detailed {DEPARTMENT_NAME} activity report following enhanced template

**{DEPARTMENT_NAME} Focus Areas:**
{FOCUS_AREAS_BULLET_LIST}

**Quality Requirements:**
- All participants matched to 32-employee directory
- All projects matched to 31+ project directory
- All tasks structured with ACTION + OBJECT + CONTEXT
- All metrics calculated per department standards
- Full RACI assignment for accountability
- Confidence levels assigned to all matches

**Enhancement Features:**
- Intelligent participant matching with 5 strategies
- Intelligent project matching with 6 strategies
- Standardized vocabulary and terminology
- Complete task metadata framework
- 21-section framework integration
- Department-specific optimization
```

---

## Department-Specific Metrics & KPIs

{KEY_METRICS_DETAILED_DESCRIPTIONS}

**Metric Calculation Formulas:**
{METRIC_FORMULAS}

**Performance Targets:**
{PERFORMANCE_TARGETS_TABLE}

---

## Cross-Department Collaboration

**{DEPARTMENT_NAME} Collaborates With:**
{COLLABORATION_PATTERNS}

**Common Collaboration Points:**
{COLLABORATION_DETAILS}

---

## Version History

**v2.0** - November 7, 2025
- Enhanced with comprehensive organizational context from SummariesOct
- Added intelligent participant identification (32-employee directory)
- Added intelligent project identification (31+ project directory)
- Implemented ACTION + OBJECT + CONTEXT task framework
- Added complete task metadata (RACI, complexity, dependencies)
- Integrated 21-section framework with flexible selection
- Added confidence level system for matching
- Enhanced with standardized vocabulary and terminology
- Added multi-lingual support (Russian, Ukrainian, English)
- Added department-specific focus areas and metrics
- Enhanced quality standards and validation

**v1.0** - November 25, 2025
- Initial {DEPARTMENT_NAME}-specific prompt creation
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added {DEPARTMENT_NAME}-specific employees and context
- Customized report template for {DEPARTMENT_NAME} department

---

**Documentation Reference**: See [constructor/docs/](constructor/docs/) for complete guidance
- [Employee Directory Guidance](constructor/docs/01_employee_directory_guidance.md)
- [Project Directory Guidance](constructor/docs/02_project_directory_guidance.md)
- [Vocabulary Standards](constructor/docs/03_vocabulary_standards.md)
- [Task + Object Framework](constructor/docs/04_task_object_framework.md)
- [21-Section Framework](constructor/docs/05_21_section_framework.md)
- [Department-Specific Patterns](constructor/docs/06_department_specific_patterns.md)

---

*Last Updated: November 7, 2025*
*Department: {DEPARTMENT_NAME}*
*Enhanced Version: 2.0*
*Quality Validated: ✅*
