# PMT-033: AI Department - Daily Report v2.1

**Prompt ID:** PMT-033
**Version:** 2.1
**Department:** AI & Automation (AID)
**Category:** Daily Report Generation
**Date:** 2025-11-19
**Status:** Active

---

## Purpose

Generate comprehensive daily activity reports for the **AI Department** with TASK_MANAGERS entity integration, using token-efficient format and forward planning.

**v2.1 Updates:**
- ✅ TASK_MANAGERS entity integration
- ✅ Token-efficient format: `TST-###_Name`
- ✅ 10-section report schema
- ✅ Entity validation via PMT-070
- ✅ Project/milestone tracking
- ✅ Next day plans, research, improvements

---

## Department Context: AI (Artificial Intelligence)

### Department Overview
- **Code:** AID
- **Mission:** LLM integration, automation, prompt engineering, AI-first operations
- **Team Size:** 2 employees
- **Key Responsibilities:**
  - Prompt engineering and optimization
  - AI tool integration and automation
  - Framework development and maintenance
  - Technical infrastructure management
  - AI workflow automation

### AI Department Employees

**Artemchuk Nikolay** (ID: 37226)
- Role: Project manager, Lead generator
- Location: Ukraine
- Telegram: @twinklelilsta
- Email: artemchuknn@gmail.com
- Status: Work

**Perederii Vladislav** (ID: 86246)
- Role: Prompt engineer
- Location: Ukraine
- Telegram: @WeAllWillDie
- Email: vladyslav.perederii@nure.ua
- Status: Available

~~**Zasiadko Matvii** (ID: 86981)~~
- Role: Prompt engineer
- Location: Ukraine
- Telegram: @matviy04
- Email: matvey.z.2004@icloud.com
- Status: Left

---

## AI-Specific Projects (TASK_MANAGERS)

### Common Projects
- **PRT-001_AI_Tutorial_Research** - AI tutorial content analysis and taxonomy
- **PRT-006_Research_Taxonomy_Pipeline** - Taxonomy extraction and processing
- **PRT-007_System_Analysis** - Infrastructure and system improvements
- **PRT-002_MCP_Automation_Stack** - MCP server integrations

### Common Tasks
- **TST-015_Extract_Taxonomy_Tutorial_Videos** - Video content processing
- **TST-055_Process_Department_Task_Files** - Task file processing
- **TST-058_Extract_Tasks_Daily_Files** - Daily file extraction
- **TST-001_AI_Powered_HTML_Parsing** - HTML parsing automation
- **TST-018_Populate_Knowledge_Library** - Knowledge base management

### Activity Patterns
- **Infrastructure:** Operational/Maintenance (config, setup, tool integration)
- **Prompt Engineering:** PRT-001 or PRT-006 (taxonomy, framework development)
- **System Analysis:** PRT-007 (task processing, data inventory)
- **Framework Development:** Operational or PRT-specific depending on scope
- **Tool Integration:** Map to relevant TST or Operational

---

## AI-Specific Tools

### Large Language Models
- **ChatGPT** (OpenAI) - https://chat.openai.com/
- **Claude** (Anthropic) - https://claude.ai/
- **Gemini** (Google) - https://gemini.google.com/
- **Grok** (X/Twitter) - https://grok.com/
- **Minimax** - https://chat.minimax.io/

### AI Research & Analysis
- **NotebookLM** (Google) - Document analysis and knowledge base
- **Perplexity AI** - AI-powered search
- **Genspark** - AI search engine

### AI Development Tools
- **Replit** - Cloud IDE with AI capabilities
- **Google AI Studio** - Prompt testing and model comparison
- **Smithery** - AI coding assistant
- **Cursor** - AI code editor
- **Windsurf** - AI development tool
- **Claude Desktop** - Desktop AI assistant

### Communication & Documentation
- Discord, Gmail, Google Workspace, Notion
- GitHub (RAC knowledge base)

---

## Data Sources

### Input Files
1. **AI Prompt Log:** `Dropbox/Nov25/AI Nov25/AI prompt log.md`
2. **Employee Daily Files:** `Dropbox/Nov25/AI Nov25/{Employee}/Week_{N}/{DAY}/daily.md`
3. **TASK_MANAGERS CSVs:** (Loaded via PMT-032)
   - Project_Templates_Master_List.csv
   - Milestone_Templates_Master_List.csv
   - Task_Templates_Master_List.csv

### Output Location
```
Dropbox/Nov25/AI Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
```

---

## Report Generation Instructions

### Step 1: Load Entity Data
**Before processing**, ensure TASK_MANAGERS CSV files loaded (handled by PMT-032)

### Step 2: Read AI Prompt Log
Read: `Dropbox/Nov25/AI Nov25/AI prompt log.md`

Extract all activities for the target date.

### Step 3: Map Activities to Entities
**For each activity**, invoke PMT-070 entity mapping:

```python
entity_mapping = map_activity_to_entities(
    activity_desc=activity.description,
    department="AID",
    date=current_date
)
```

**AI-Specific Mapping Guidelines:**
- **Infrastructure configs** → Operational/Maintenance (unless part of project)
- **Tool integrations** → Map to TST if specific, or Operational if general
- **Prompt engineering** → PRT-001_AI_Tutorial_Research or PRT-006_Research_Taxonomy_Pipeline
- **Framework development** → PRT-007_System_Analysis or Operational
- **Task processing** → TST-055_Process_Department_Task_Files or TST-058_Extract_Tasks_Daily_Files
- **Documentation** → Related to parent project/task

### Step 4: Generate 10-Section Report
Follow REPORT_OUTPUT_SCHEMA_v2.1.md structure with AI-specific customization.

---

## 10-Section Report Template

### SECTION 1: EXECUTIVE SUMMARY

```markdown
# Daily Activity Report - AI Department (AID)
**Date:** November {DAY}, 2025

## 1. EXECUTIVE SUMMARY

- **Report Date:** 2025-11-{DAY}
- **Department:** AI & Automation (AID)
- **Team Size:** 3 members
- **Total Activities:** [COUNT]
- **Projects Active:** [COUNT] ([PRT-IDs])
- **Tasks Completed:** [COUNT]
- **Tasks In Progress:** [COUNT]
- **Overall Status:** [On Track/At Risk/Blocked] ✅/⚠️/🚫
- **Key Achievements:**
  - [Achievement 1 with impact]
  - [Achievement 2 with impact]
  - [Achievement 3 with impact]
```

**AI-Specific Focus:**
- Infrastructure improvements
- Tool integrations completed
- Framework enhancements
- Prompt engineering milestones

---

### SECTION 2: PROJECT CONTRIBUTIONS

```markdown
## 2. PROJECT CONTRIBUTIONS

### PRT-001_AI_Tutorial_Research
- **Role:** Lead
- **Status:** Active
- **Progress Today:** MLT-001_Content_Analysis (X% → Y%)
- **Tasks Completed:**
  - TST-015_Extract_Taxonomy_Tutorial_Videos (X hours)
  - TST-018_Populate_Knowledge_Library (X hours)
- **Next Milestone:** MLT-003_Relationship_Validation (starts [DATE])

### PRT-007_System_Analysis
- **Role:** Lead
- **Status:** Active
- **Progress Today:** MLT-002_Data_Inventory (X% → Y%)
- **Tasks Completed:**
  - TST-055_Process_Department_Task_Files (X hours)
  - TST-058_Extract_Tasks_Daily_Files (X hours)
- **Cross-Dept Coordination:** [If applicable]

### Operational/Maintenance
- **Activities:** [COUNT] tasks ([HOURS] hours)
- **Type:** Infrastructure configs, tool setup, admin tasks
```

**AI-Specific Projects to Track:**
- PRT-001_AI_Tutorial_Research
- PRT-006_Research_Taxonomy_Pipeline
- PRT-007_System_Analysis
- PRT-002_MCP_Automation_Stack
- Cross-department support (PRT-003_HR_Automation, etc.)

---

### SECTION 3: MILESTONE PROGRESS

```markdown
## 3. MILESTONE PROGRESS

### MLT-001_Content_Analysis (PRT-001_AI_Tutorial_Research)
- **Progress:** X% → Y% (+Z%)
- **Tasks Completed Today:**
  - TST-015_Extract_Taxonomy_Tutorial_Videos ✅
  - TST-018_Populate_Knowledge_Library ✅
- **Tasks In Progress:** TST-019_Validate_Relationships (X% complete)
- **Blockers:** [None or describe]
- **Timeline:** On track for [DATE] completion
- **Impact:** [Achievement description]

### MLT-002_Data_Inventory (PRT-007_System_Analysis)
- **Progress:** X% → Y% (+Z%)
- **Tasks Completed Today:**
  - TST-055_Process_Department_Task_Files ✅
- **Tasks In Progress:** [If applicable]
- **Blockers:** [None or describe]
- **Timeline:** On track for [DATE] completion
- **Impact:** [Achievement description]
```

**AI-Specific Milestones:**
- MLT-001_Content_Analysis (taxonomy extraction)
- MLT-002_Data_Inventory (system analysis)
- MLT-003_Relationship_Validation (data validation)

---

### SECTION 4: TASK SEQUENCES AND ENTITY MAPPING

```markdown
## 4. TASK SEQUENCES AND ENTITY MAPPING

### Activity 1: [Activity Title]
- **Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
- **Time:** X hours
- **Status:** Completed ✅ / In Progress 🔄 / Blocked 🚫
- **Confidence:** XX%
- **Priority:** High/Medium/Low
- **Objective:** [Clear objective statement]
- **Actions Taken:**
  - [Action 1]
  - [Action 2]
  - [Action 3]
- **Results:**
  - ✅ [Result 1]
  - ✅ [Result 2]
  - ✅ [Result 3]
- **Impact:** [Impact description]

### Activity 2: Infrastructure Configuration
- **Entity:** Operational/Maintenance
- **Time:** X hours
- **Status:** Completed ✅
- **Category:** Infrastructure Operations
- **Actions Taken:**
  - [Config 1]
  - [Config 2]
- **Impact:** [Infrastructure improvement]
```

**AI-Specific Activities to Track:**
- Prompt engineering work
- Tool integrations (MCP, n8n, automation)
- Framework enhancements
- Infrastructure configurations
- Task/data processing
- Documentation updates
- Research and testing

---

### SECTION 5: CROSS-DEPARTMENT COORDINATION

```markdown
## 5. CROSS-DEPARTMENT COORDINATION

### PRT-003_HR_Automation (Support Role)
- **Lead Department:** HRM (HR & Recruitment)
- **Supporting Departments:** AID (AI), DEV (Development)
- **Our Contribution Today:**
  - [Specific contribution 1]
  - [Specific contribution 2]
- **Deliverables Sent:**
  - [Deliverable 1 with filename]
  - [Deliverable 2 with filename]
- **Status:** [Current status]
- **Next Handoff:** [Department] to [action] by [date]
- **Dependencies:** [None or describe]

### [Outgoing Request Title] (Outgoing to [DEPT])
- **To Department:** [DEPT CODE] ([Department Name])
- **Request:** [Specific request]
- **Context:** [Why needed]
- **Priority:** High/Medium/Low
- **Deadline:** [DATE]
- **Files Shared:** [If applicable]
- **Status:** [Current status]

### [Incoming Request Title] (Incoming from [DEPT])
- **From Department:** [DEPT CODE] ([Department Name])
- **Request:** [What they need from us]
- **Timeline:** [DATE]
- **Status:** [Current status]
```

**AI-Specific Coordination:**
- Support for HRM (CV screening, automation)
- Support for DEV (API integrations, technical guidance)
- Support for DGN (asset requests for tutorials/content)
- Collaboration with all departments on automation

---

### SECTION 6: INFRASTRUCTURE AND TECHNICAL ACHIEVEMENTS

```markdown
## 6. INFRASTRUCTURE AND TECHNICAL ACHIEVEMENTS

### System Configurations
- [Configuration 1: Description and impact]
- [Configuration 2: Description and impact]
- [Configuration 3: Description and impact]

### Framework Enhancements
- [Enhancement 1: Description and impact]
- [Enhancement 2: Description and impact]
- [Enhancement 3: Description and impact]

### Tool Integrations
- [Integration 1: Tool name, purpose, status]
- [Integration 2: Tool name, purpose, status]
- [Integration 3: Tool name, purpose, status]

### Prompt Engineering
- [Prompt 1: Name, purpose, performance improvement]
- [Prompt 2: Name, purpose, performance improvement]

### Documentation Updates
- [Doc 1: Filename, lines, purpose]
- [Doc 2: Filename, lines, purpose]
- [Doc 3: Filename, lines, purpose]

### Testing & Validation
- [Test 1: What was tested, results]
- [Test 2: What was tested, results]
```

**AI-Specific Technical Content:**
- LLM integrations and configurations
- MCP server implementations
- n8n workflow automations
- Prompt optimization results
- Framework architecture updates
- API integrations
- Database/data pipeline improvements

---

### SECTION 7: NEXT DAY PLANS

```markdown
## 7. NEXT DAY PLANS

### Scheduled Activities (Nov {DAY+1}, 2025)

#### High Priority
1. **[Activity Title]**
   - **Project:** PRT-###_Name
   - **Milestone:** MLT-###_Name
   - **Objective:** [Clear objective]
   - **Time Estimate:** X hours
   - **Dependencies:** [None or describe]
   - **Expected Outcome:** [Specific outcome]

2. **[Activity Title]**
   - **Project:** PRT-###_Name
   - **Objective:** [Clear objective]
   - **Time Estimate:** X hours
   - **Dependencies:** [None or describe]
   - **Expected Outcome:** [Specific outcome]

#### Medium Priority
3. **[Activity Title]**
   - **Objective:** [Clear objective]
   - **Time Estimate:** X hours
   - **Expected Outcome:** [Specific outcome]

#### Low Priority / If Time Permits
4. **[Activity Title]**
   - **Objective:** [Clear objective]
   - **Time Estimate:** X hours

#### Meetings & Coordination
- Daily standup (9:00 AM, 15 min)
- [Meeting 1: Purpose, department, time]
- [Meeting 2: Purpose, department, time]

### Total Planned Time: X hours
```

**AI-Specific Planning:**
- Prioritize infrastructure improvements
- Schedule tool integration work
- Plan prompt engineering sessions
- Allocate time for testing and validation
- Coordinate cross-department handoffs

---

### SECTION 8: RESEARCH NEEDED

```markdown
## 8. RESEARCH NEEDED

### High Priority Research

#### 1. [Research Topic]
- **Context:** [Why this research is needed]
- **Research Questions:**
  - [Question 1]
  - [Question 2]
  - [Question 3]
- **Resources Needed:**
  - [Resource 1]
  - [Resource 2]
- **Timeline:** Research by [DATE], recommendations by [DATE]
- **Owner:** [Team member or "AID team"]
- **Expected Impact:** [Quantified if possible]

#### 2. [Research Topic]
- **Context:** [Why needed]
- **Research Questions:**
  - [Question 1]
  - [Question 2]
- **Resources Needed:**
  - [Resource 1]
- **Timeline:** Research by [DATE]
- **Owner:** [Owner]
- **Expected Impact:** [Impact description]

### Medium Priority Research

#### 3. [Research Topic]
- **Context:** [Background]
- **Research Questions:**
  - [Question 1]
- **Timeline:** Research by [DATE]
- **Owner:** [Owner]
- **Expected Impact:** [Impact]

### Low Priority Research

#### 4. [Research Topic]
- **Context:** [Background]
- **Timeline:** Research by [DATE]
- **Expected Impact:** [Impact]
```

**AI-Specific Research Areas:**
- New LLM models and capabilities
- Prompt engineering techniques
- Automation framework improvements
- Tool evaluation and comparison
- Integration patterns and best practices
- Performance optimization strategies
- AI workflow methodologies

---

### SECTION 9: IMPROVEMENTS NEEDED

```markdown
## 9. IMPROVEMENTS NEEDED

### Process Improvements

#### 1. [Improvement Title]
- **Current Issue:** [Describe problem and impact]
- **Proposed Improvement:** [Specific solution]
- **Priority:** High/Medium/Low
- **Effort:** Low/Medium/High (X hours)
- **Expected Benefit:** [Quantified benefit]
- **Owner:** [Team member]
- **Implementation:** [Start date or timeline]

#### 2. [Improvement Title]
- **Current Issue:** [Problem]
- **Proposed Improvement:** [Solution]
- **Priority:** High/Medium/Low
- **Effort:** X hours
- **Expected Benefit:** [Benefit]
- **Owner:** [Owner]
- **Implementation:** [Timeline]

### Technical Improvements

#### 3. [Technical Improvement]
- **Current Issue:** [Problem]
- **Proposed Improvement:** [Solution]
- **Priority:** High/Medium/Low
- **Effort:** X hours
- **Expected Benefit:** [Benefit]
- **Owner:** [Owner]
- **Implementation:** [Timeline]

### Documentation Improvements

#### 4. [Documentation Improvement]
- **Current Issue:** [Problem]
- **Proposed Improvement:** [Solution]
- **Priority:** Medium/Low
- **Effort:** X hours
- **Expected Benefit:** [Benefit]
- **Owner:** [Owner]
- **Implementation:** [Timeline]

### Infrastructure Improvements

#### 5. [Infrastructure Improvement]
- **Current Issue:** [Problem]
- **Proposed Improvement:** [Solution]
- **Priority:** High/Medium/Low
- **Effort:** X hours
- **Expected Benefit:** [Benefit]
- **Owner:** [Owner]
- **Implementation:** [Timeline]
```

**AI-Specific Improvement Areas:**
- Prompt template optimization
- Entity mapping accuracy improvement
- Tool integration streamlining
- Framework performance optimization
- Documentation enhancement
- Testing automation
- Workflow efficiency improvements

---

### SECTION 10: METRICS AND DELIVERABLES

```markdown
## 10. METRICS AND DELIVERABLES

### Time Allocation
| Category | Hours | Percentage |
|----------|-------|------------|
| Project Work | X.X | XX% |
| Operational | X.X | XX% |
| **Total** | **X.X** | **100%** |

### Task Distribution by Status
| Status | Count | Percentage |
|--------|-------|------------|
| Completed | X | XX% |
| In Progress | X | XX% |
| Blocked | X | XX% |
| Planned | X | XX% |

### Project Time Breakdown
| Project | Hours | Tasks | Percentage |
|---------|-------|-------|------------|
| PRT-001_AI_Tutorial_Research | X.X | X | XX% |
| PRT-007_System_Analysis | X.X | X | XX% |
| Operational | X.X | X | XX% |

### Entity Mapping Confidence
| Confidence Level | Count | Percentage |
|------------------|-------|------------|
| High (>90%) | X | XX% |
| Medium (70-89%) | X | XX% |
| Low (<70%) | X | XX% |

**Average Confidence:** XX%

### Files Created/Modified

#### New Files ([COUNT])
1. `[File path]` ([LINES] lines) - [Description]
2. `[File path]` ([LINES] lines) - [Description]
3. `[File path]` ([SIZE]) - [Description]

**Total New Files:** [COUNT] | **Total Lines:** [COUNT]

#### Modified Files ([COUNT])
1. `[File path]` - [Description of changes]
2. `[File path]` - [Description of changes]

### Key Deliverables Status
- ✅ [Deliverable 1] (Complete)
- ✅ [Deliverable 2] (Complete)
- 🔄 [Deliverable 3] (In Progress)
- ⏳ [Deliverable 4] (Pending)

### Challenges Encountered

#### Challenge 1: [Challenge Title]
- **Problem:** [Description]
- **Solution:** [What was done]
- **Result:** [Outcome]
- **Status:** Resolved ✅ / Ongoing 🔄

#### Challenge 2: [Challenge Title]
- **Problem:** [Description]
- **Solution:** [What was done]
- **Result:** [Outcome]
- **Status:** Resolved ✅ / Ongoing 🔄
```

---

## Report Footer

```markdown
---

## Report Metadata

**Report Generated:** November {DAY}, 2025 18:00
**Department:** AI & Automation (AID)
**Team Size:** 3
**Report Version:** v2.1
**Schema Version:** 10-Section Format
**Entity Integration:** Enabled ✅
**Report Status:** Complete

---

## Summary Statistics

- **Total Activities:** X (Y project, Z operational)
- **Total Time:** X.X hours
- **Projects Active:** X (Y lead, Z support)
- **Milestones Progressed:** X
- **Tasks Completed:** X
- **Tasks In Progress:** X
- **Deliverables Created:** X files (Y lines)
- **Average Entity Confidence:** XX%
- **Next Day Plans:** X activities (Y hours planned)
- **Research Items:** X (Y high priority)
- **Improvements Identified:** X (Y high priority)

---

*End of Daily Activity Report*

**Next Report:** November {DAY+1}, 2025
**Prepared By:** AI Assistant via PMT-032 v2.1
**Entity Mapping:** PMT-070 v2.1

---
```

---

## AI-Specific Vocabulary

### AI & LLM Terms
- **Prompting:** Task, Context, References, Evaluate, Iterate
- **Techniques:** Chain of Thought, Tree of Thought, Prompt Chaining, Meta Prompting
- **Concepts:** Persona, Multimodal prompting, Hallucinations, Biases
- **Workflows:** Human-in-the-loop, Agent Sim, Agent X

### Framework Terms
- **Task Template:** Action + Object format
- **Step Template:** Name, Tool, Responsibility
- **Checklist Items:** Name, Guide, Tools, Items, Formats, Placement
- **Entity-based organization**
- **Template-driven operations**

### Technical Terms
- **LLM integration**
- **API integration**
- **Workflow automation**
- **System architecture**
- **Technical infrastructure**

---

## AI-Specific Quality Standards

### Content Requirements
- ✅ All 10 sections populated
- ✅ All infrastructure tasks included
- ✅ All tool integrations documented
- ✅ All framework updates tracked
- ✅ All prompt engineering activities recorded
- ✅ Entity mappings complete (or Operational)
- ✅ Next day plans with time estimates
- ✅ Research needs identified
- ✅ Improvements documented

### Entity Integration Requirements
- ✅ Activities mapped to TST → MLT → PRT
- ✅ Token-efficient format: `TST-###_Name`
- ✅ Confidence scores ≥70% or flagged
- ✅ Operational work properly classified
- ✅ Cross-department roles documented

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for statistics and metrics
- ✅ Bullet lists for achievements
- ✅ Checkboxes for completed items
- ✅ Code blocks for technical content
- ✅ Consistent section structure (10 sections)

### Technical Requirements
- ✅ File paths accurate and absolute
- ✅ Line counts for code files
- ✅ Tool names with URLs where applicable
- ✅ Employee names accurate
- ✅ Time tracking accurate
- ✅ Priority levels specified

---

## Example Command

```
Generate AI department daily activity report for November 19, 2025.

Use PMT-033 v2.1:

1. Read AI prompt log: Dropbox/Nov25/AI Nov25/AI prompt log.md
2. Map all activities to TASK_MANAGERS entities using PMT-070 v2.1
3. Generate 10-section report with entity integration
4. Focus on:
   - Infrastructure and system tasks
   - Tool integrations (MCP, n8n, AI tools)
   - Framework enhancements
   - Prompt engineering activities
   - Technical configurations
   - Documentation updates
5. Include next day plans, research needs, improvements
6. Save to: Dropbox/Nov25/AI Nov25/Reports/19/Daily_Activity_Report_Nov19_2025.md
```

---

## Version History

**v2.1** (2025-11-19)
- ✅ Added TASK_MANAGERS entity integration
- ✅ Implemented 10-section schema (streamlined from 14)
- ✅ Added token-efficient format: `TST-###_Name`
- ✅ Added Section 7: Next Day Plans
- ✅ Added Section 8: Research Needed
- ✅ Added Section 9: Improvements Needed
- ✅ Removed redundant sections (7, 9, 13, 14 from v1.0)
- ✅ Enhanced AI-specific project/task patterns
- ✅ Updated quality standards

**v1.0** (2025-11-05)
- Initial AI-specific prompt creation
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added AI-specific employees and context
- Customized 14-section report template
- Included comprehensive AI tools directory

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Review Cycle:** Monthly
**Last Updated:** 2025-11-19

---

## Related Documents

- [PMT-032_Daily_Report_Collection_v2.1.md](../PMT-032_Daily_Report_Collection_v2.1.md)
- [PMT-070_Daily_Report_Entity_Mapping_v2.1.md](../../UTILITIES/Daily_Updates/PMT-070_Daily_Report_Entity_Mapping_v2.1.md)
- [REPORT_OUTPUT_SCHEMA_v2.1.md](../REPORT_OUTPUT_SCHEMA_v2.1.md)
- [ENTITY_MAPPING_GUIDE_v2.1.md](../ENTITY_MAPPING_GUIDE_v2.1.md)

---

*End of Prompt*
