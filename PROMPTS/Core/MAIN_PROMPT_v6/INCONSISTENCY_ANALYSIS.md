# MAIN_PROMPT_v6 vs Department Prompts - Inconsistency Analysis

**Analysis Date:** 2025-11-25
**Comparison:** MAIN_PROMPT_v6 modular files vs Department_Prompts (v2.1)
**Reference:** `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts\`

---

## EXECUTIVE SUMMARY

**Critical Finding:** MAIN_PROMPT_v6 and Department Prompts v2.1 have **significant structural and operational differences**. Department prompts are far more mature, detailed, and aligned with actual daily operations.

### Key Discrepancies Found:

| Area | MAIN_PROMPT_v6 | Department Prompts v2.1 | Gap Severity |
|------|----------------|------------------------|--------------|
| **Focus** | Generic task extraction | Detailed 10-section daily reports | 🔴 HIGH |
| **Entity Integration** | Basic mention | Full TASK_MANAGERS integration | 🔴 HIGH |
| **Data Sources** | Generic DAILIES folder | Specific prompt logs + employee dailies | 🔴 HIGH |
| **Report Structure** | Not defined | 10-section schema with templates | 🔴 HIGH |
| **Tool Coverage** | Basic TOL-### reference | Detailed tool lists per department | 🟡 MEDIUM |
| **Operational Detail** | Missing | Full operational/project classification | 🔴 HIGH |
| **Progress Tracking** | Conceptual | Implemented with metrics/deliverables | 🔴 HIGH |

---

## DETAILED INCONSISTENCY BREAKDOWN

### 1. DEPARTMENT STRUCTURE & CODES

#### MAIN_PROMPT_v6 (04_Department_Operations.md)
```
| Code | Department | Daily | Primary Prompts | Focus Areas |
| AID  | AI & Automation | PMT-033 | ... | Taxonomy, automation, system health |
| VID  | Video Production | PMT-043 | ... | Transcription, entity extraction |
| HRM  | Human Resources | PMT-038 | ... | CV parsing, recruitment |
| DEV  | Development | PMT-036 | ... | Version control, VSCode, APIs |
| LGN  | Lead Generation | PMT-039 | ... | Prospecting, outreach |
| DGN  | Design | PMT-035 | ... | UI/UX, graphics |
| MKT  | Marketing | PMT-040 | ... | Campaigns, content |
| SLS  | Sales | PMT-041 | ... | Pipeline management |
| SMM  | Social Media | PMT-042 | ... | Content, engagement |
| FIN  | Finance | PMT-037 | ... | Reporting, budgets |
```

#### Department Prompts v2.1 (Department_Prompts_Index.md)
```
### PMT-033: AI Department
- Team Size: 2 employees (was 3)
- Key Focus: Prompt engineering, AI tool integration, framework development
- **Employees:**
  - Artemchuk Nikolay (ID: 37226) - Project manager, Lead generator
  - Perederii Vladislav (ID: 86246) - Prompt engineer
  - ~~Zasiadko Matvii~~ (Left)
- **Data Sources:**
  - Prompt Log: Dropbox/Nov25/AI Nov25/AI prompt log.md
  - Employee Dailies: Dropbox/Nov25/AI Nov25/{Employee}/Week_{N}/{DAY}/daily.md
- **Output:** Dropbox/Nov25/AI Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md

### PMT-037: Finance Department
- Team Size: 2 employees
- Key Focus: Financial operations, invoice management, budget tracking
- **Employees:**
  - Shyiko Viktoriia (ID: 87598) - Accountant
  - [Additional Finance Staff]
- **Data Sources:**
  - Prompt Log: Dropbox/Nov25/Fin Nov25/Finance prompt log.md (if exists)
  - Employee Dailies: Dropbox/Nov25/Fin Nov25/{Employee}/Week_{N}/{DAY}/daily.md
- **Output:** Dropbox/Nov25/Fin Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
```

**🔴 CRITICAL GAP:**
- MAIN_PROMPT_v6 has NO employee details, team sizes, or actual data source paths
- Department Prompts have specific employees, IDs, contacts, team sizes, exact file paths
- Missing: Employee ID mapping, contact info, status tracking

---

### 2. DATA SOURCES & FILE LOCATIONS

#### MAIN_PROMPT_v6 (05_File_Operations.md)
```
### Daily Reports & Employee Data
ENTITIES/DAILIES/
└── Week{N}/{Day}/{Employee_Name}/Daily.md

ENTITIES/TALENTS/
├── Employees/profiles/
└── ANALYTICS_Employees_Attendance_*.csv
```

#### Department Prompts v2.1 (Actual Structure)
```
### Input Files (per PMT-037, PMT-033)
1. Department Prompt Log: Dropbox/Nov25/{DEPT} Nov25/{DEPT} prompt log.md
2. Employee Daily Files: Dropbox/Nov25/{DEPT} Nov25/{Employee}/Week_{N}/{DAY}/daily.md
3. TASK_MANAGERS CSVs: (Loaded via PMT-032)
   - Project_Templates_Master_List.csv
   - Milestone_Templates_Master_List.csv
   - Task_Templates_Master_List.csv

### Output Location
Dropbox/Nov25/{DEPT} Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
```

**🔴 CRITICAL GAP:**
1. **Different base paths:**
   - MAIN_PROMPT_v6: `ENTITIES/DAILIES/Week{N}/{Day}/`
   - Actual: `Dropbox/Nov25/{DEPT} Nov25/`

2. **Missing "Prompt Log" concept:**
   - MAIN_PROMPT_v6: Only mentions employee daily files
   - Actual: Each department has "{DEPT} prompt log.md" as primary data source

3. **Different output structure:**
   - MAIN_PROMPT_v6: `REPORTS/Daily_Reports/YYYY-MM-DD_{DEPT}.md`
   - Actual: `Dropbox/Nov25/{DEPT} Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

---

### 3. REPORT STRUCTURE & SCHEMA

#### MAIN_PROMPT_v6 (03_Workflow_Execution.md)
```markdown
**Daily Reports:**
Collection: PMT-032 aggregates all departments

Department Prompts:
| Dept | PMT | Use For |
| AI & Automation | PMT-033 | Taxonomy, automation, system work |
| Finance | PMT-037 | Financial reporting |
...
```
**NO report structure defined** - only mentions "Daily Ops Workflow" bash script

#### Department Prompts v2.1 (10-Section Schema)
```markdown
## 10-Section Report Template

### SECTION 1: EXECUTIVE SUMMARY
- Report Date, Department, Team Size
- Total Activities, Projects Active, Tasks Completed
- Overall Status, Key Achievements

### SECTION 2: PROJECT CONTRIBUTIONS
- Per-project status (PRT-###)
- Role (Lead/Support)
- Progress Today
- Tasks Completed
- Next Milestone

### SECTION 3: MILESTONE PROGRESS
- Progress tracking (X% → Y%)
- Tasks Completed Today
- Tasks In Progress
- Blockers
- Timeline status

### SECTION 4: TASK SEQUENCES AND ENTITY MAPPING
- Activity-by-activity breakdown
- Entity: TST-### → MLT-### → PRT-###
- Time, Status, Priority
- Objective, Actions Taken, Results, Impact

### SECTION 5: CROSS-DEPARTMENT COORDINATION
- Cross-project support roles
- Incoming/outgoing requests
- Deliverables shared
- Dependencies

### SECTION 6: [DEPARTMENT-SPECIFIC SECTION]
- **AI:** Infrastructure and Technical Achievements
- **Finance:** Financial Operations and Reporting

### SECTION 7: NEXT DAY PLANS
- Scheduled activities (High/Medium/Low priority)
- Time estimates
- Expected outcomes
- Dependencies

### SECTION 8: RESEARCH NEEDED
- High/Medium/Low priority research
- Research questions
- Resources needed
- Timeline, Owner, Expected Impact

### SECTION 9: IMPROVEMENTS NEEDED
- Process, Technical, Documentation, Infrastructure improvements
- Current Issue, Proposed Improvement
- Priority, Effort, Expected Benefit
- Owner, Implementation timeline

### SECTION 10: METRICS AND DELIVERABLES
- Time Allocation table
- Task Distribution by Status
- Project Time Breakdown
- Entity Mapping Confidence
- Files Created/Modified
- Key Deliverables Status
- Challenges Encountered
```

**🔴 CRITICAL GAP:**
- MAIN_PROMPT_v6: **Zero detail** on report structure
- Department Prompts: **Comprehensive 10-section schema** with templates, examples, and quality standards
- Missing: Entire report generation framework, section-by-section guidance

---

### 4. ENTITY INTEGRATION (TASK_MANAGERS)

#### MAIN_PROMPT_v6 (01_Core_Identity.md)
```markdown
### 1. EXTRACT & ORGANIZE TASKS
- Extract tasks from daily reports, transcripts, calls
- Group tasks into logical milestones
- Add details by breaking tasks into steps
- Link entities to LIBRARIES
- Assign IDs using XXX-### format

### Example: TASK EXTRACTION FROM DAILY REPORT
**Processing:**
1. Check Previous Day
2. Extract Tasks
3. Link LIBRARIES
**Output:** Structured task list with IDs, status, and context
```

#### Department Prompts v2.1 (PMT-033, PMT-037)
```markdown
### Step 3: Map Activities to Entities
**For each activity**, invoke PMT-070 entity mapping:

entity_mapping = map_activity_to_entities(
    activity_desc=activity.description,
    department="AID",
    date=current_date
)

**AI-Specific Mapping Guidelines:**
- Infrastructure configs → Operational/Maintenance
- Tool integrations → Map to TST if specific
- Prompt engineering → PRT-001 or PRT-006
- Framework development → PRT-007 or Operational
- Task processing → TST-055 or TST-058

**Finance-Specific Mapping Guidelines:**
- Month-end closing → Operational/Routine
- Invoice processing → Operational/Routine
- System improvements → Project if significant, or Operational

**Expected Result:** 80-90% of activities will be Operational/Maintenance
```

**🔴 CRITICAL GAP:**
1. **PMT-070 Entity Mapping Tool:**
   - MAIN_PROMPT_v6: Not mentioned
   - Department Prompts: Core tool for activity → entity mapping

2. **Operational vs Project Classification:**
   - MAIN_PROMPT_v6: All tasks become MLT/TSK/STP
   - Department Prompts: Distinguishes "Operational/Maintenance" (80-90% of work) vs "Project work"

3. **Department-Specific Mapping Patterns:**
   - MAIN_PROMPT_v6: Generic task extraction
   - Department Prompts: Specific mapping rules per department (AI: infrastructure → Operational; Finance: month-end → Routine)

---

### 5. PROJECT & TASK EXAMPLES

#### MAIN_PROMPT_v6 (01_Core_Identity.md - Example)
```markdown
**Input:** Finance employee daily report
"Created n8n automation to sync Google Sheets employee data to Dropbox markdown.
Will continue testing the schedule trigger tomorrow."

**Output:**
- TSK-042: Create n8n automation (STATUS: ✅ Completed)
  - STP-001: Configure Google Sheets node (✅ Completed)
  - STP-002: Set up Dropbox upload (✅ Completed)
- TSK-043: Test schedule trigger (STATUS: 🔄 In Progress)
```

#### Department Prompts v2.1 (PMT-033 - AI Projects)
```markdown
## AI-Specific Projects (TASK_MANAGERS)

### Common Projects
- PRT-001_AI_Tutorial_Research - AI tutorial content analysis
- PRT-006_Research_Taxonomy_Pipeline - Taxonomy extraction
- PRT-007_System_Analysis - Infrastructure improvements
- PRT-002_MCP_Automation_Stack - MCP server integrations

### Common Tasks
- TST-015_Extract_Taxonomy_Tutorial_Videos
- TST-055_Process_Department_Task_Files
- TST-058_Extract_Tasks_Daily_Files
- TST-001_AI_Powered_HTML_Parsing
- TST-018_Populate_Knowledge_Library

### Activity Patterns
- Infrastructure → Operational/Maintenance
- Prompt Engineering → PRT-001 or PRT-006
- System Analysis → PRT-007
```

**🔴 CRITICAL GAP:**
- MAIN_PROMPT_v6: Generic example with made-up IDs (TSK-042, STP-001)
- Department Prompts: **Real project/task IDs** from TASK_MANAGERS master lists
- Missing: Actual project catalog, real task templates, activity pattern mapping

---

### 6. TOOLS & TECHNOLOGY

#### MAIN_PROMPT_v6 (01_Core_Identity.md)
```markdown
| **TOL** | Tool | TOL-### | LIBRARIES/Tools/*/*.json | Software, platforms, AI tools |
```
Generic reference only

#### Department Prompts v2.1 (PMT-033 - AI Tools)
```markdown
## AI-Specific Tools

### Large Language Models
- ChatGPT (OpenAI) - https://chat.openai.com/
- Claude (Anthropic) - https://claude.ai/
- Gemini (Google) - https://gemini.google.com/
- Grok (X/Twitter) - https://grok.com/
- Minimax - https://chat.minimax.io/

### AI Research & Analysis
- NotebookLM (Google) - Document analysis
- Perplexity AI - AI-powered search
- Genspark - AI search engine

### AI Development Tools
- Replit - Cloud IDE with AI
- Google AI Studio - Prompt testing
- Smithery, Cursor, Windsurf - AI code editors
- Claude Desktop - Desktop AI assistant
```

#### Department Prompts v2.1 (PMT-037 - Finance Tools)
```markdown
## Finance-Specific Tools

### Accounting Software
- QuickBooks - Primary accounting system
- Xero - Cloud accounting
- FreshBooks - Invoicing and expense tracking

### Banking & Payments
- Online Banking Platforms
- PayPal, Stripe - Payment processing
- Wire Transfer Systems

### Spreadsheets & Analysis
- Microsoft Excel
- Google Sheets
- Power BI / Tableau
```

**🟡 MEDIUM GAP:**
- MAIN_PROMPT_v6: Only references TOL-### generic
- Department Prompts: **Detailed tool lists** with URLs, categories, specific purposes per department
- Missing: Tool catalogs, department-specific tool mappings

---

### 7. WORKFLOW EXECUTION DETAILS

#### MAIN_PROMPT_v6 (03_Workflow_Execution.md)
```markdown
## DAILY REPORTS

**Daily Ops Workflow:**
```bash
# Run all department reports
for dept in AID DGN DEV FIN HRM LGN MKT SLS SMM VID; do
  execute_prompt "PMT-0XX_${dept}_Daily_Report" >> daily_reports/$(date +%Y-%m-%d)_${dept}.md
done

# Aggregate
execute_prompt "PMT-032" >> daily_reports/$(date +%Y-%m-%d)_COLLECTION.md
```
```

#### Department Prompts v2.1 (PMT-037 - Finance Workflow)
```markdown
## Report Generation Instructions

### Step 1: Load Entity Data
Before processing, ensure TASK_MANAGERS CSV files loaded (handled by PMT-032)

### Step 2: Read Finance Prompt Log
Read: `Dropbox/Nov25/Fin Nov25/Finance prompt log.md` or employee daily files

### Step 3: Map Activities to Entities
For each activity, invoke PMT-070 entity mapping:
- Month-end closing → Operational/Routine
- Invoice processing → Operational/Routine
- Bank reconciliation → Operational/Routine
- System improvements → Project if significant

Expected Result: 80-90% Operational/Maintenance

### Step 4: Generate 10-Section Report
Follow REPORT_OUTPUT_SCHEMA_v2.1.md with Finance customization

**Output Location:** Dropbox/Nov25/Fin Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
```

**🔴 CRITICAL GAP:**
- MAIN_PROMPT_v6: Generic bash script concept
- Department Prompts: **4-step detailed workflow** with entity loading, prompt log reading, PMT-070 mapping, report generation
- Missing: PMT-032 orchestration details, PMT-070 invocation, REPORT_OUTPUT_SCHEMA_v2.1.md

---

### 8. QUALITY STANDARDS & VALIDATION

#### MAIN_PROMPT_v6 (07_Quality_Validation.md)
```markdown
## QUALITY CHECKLIST

**Entity Creation:**
- [ ] ID: Unique, sequential, zero-padded
- [ ] References: All entity IDs exist
- [ ] Metadata: Name, Description, Category, Department complete
- [ ] Files: Paths in CSV match physical locations
- [ ] Format: Consistent naming (XXX-###_Name.ext)
- [ ] Version: Semantic format
```

#### Department Prompts v2.1 (PMT-037 - Finance Quality)
```markdown
## Finance-Specific Quality Standards

### Content Requirements
- ✅ All 10 sections populated
- ✅ Operational excellence metrics included
- ✅ Financial accuracy documented (discrepancies, errors)
- ✅ Transaction volumes and values tracked
- ✅ Month-end/quarter-end progress noted
- ✅ Process improvements documented
- ✅ Mostly Operational/Maintenance entity classification

### Operational Excellence Focus
- ✅ Accuracy percentages (target: 100%)
- ✅ Processing time efficiency
- ✅ Zero discrepancies goal
- ✅ On-time completion tracking
- ✅ Process improvement initiatives

### Formatting Requirements
- ✅ Financial values formatted consistently ($X,XXX)
- ✅ Transaction counts clearly stated
- ✅ Accuracy metrics prominent
- ✅ Operational categories organized
```

**🔴 CRITICAL GAP:**
- MAIN_PROMPT_v6: Generic entity validation only
- Department Prompts: **Department-specific quality standards** (Finance: 100% accuracy, zero discrepancies; AI: entity confidence ≥70%)
- Missing: Operational metrics, domain-specific validation criteria

---

## MISSING COMPONENTS IN MAIN_PROMPT_v6

### 1. PMT-032: Daily Report Collection v2.1
**Status:** Referenced but NOT DEFINED in MAIN_PROMPT_v6

**What it does (from department prompts):**
- Orchestrates all department report generation
- Loads TASK_MANAGERS CSV files (Projects, Milestones, Tasks)
- Invokes each department prompt (PMT-033 to PMT-043)
- Aggregates results into collection report
- Manages version 2.1 schema enforcement

**Where defined:** `PMT-032_Daily_Report_Collection_v2.1.md` (not included in MAIN_PROMPT_v6)

---

### 2. PMT-070: Daily Report Entity Mapping v2.1
**Status:** NOT MENTIONED in MAIN_PROMPT_v6

**What it does (from department prompts):**
- Maps activities to TASK_MANAGERS entities (PRT-###, MLT-###, TST-###)
- Distinguishes Operational/Maintenance vs Project work
- Returns entity ID, confidence score, category
- Department-specific mapping rules
- Token-efficient format: `TST-###_Name`

**Where defined:** `PMT-070_Daily_Report_Entity_Mapping_v2.1.md` (not included in MAIN_PROMPT_v6)

**Usage example:**
```python
entity_mapping = map_activity_to_entities(
    activity_desc="Reconciled 47 bank transactions",
    department="FIN",
    date="2025-11-19"
)
# Returns:
# {
#   "entity": "Operational/Maintenance",
#   "category": "Financial Operations - Bank Reconciliation",
#   "confidence": 95%,
#   "project": None
# }
```

---

### 3. REPORT_OUTPUT_SCHEMA_v2.1.md
**Status:** NOT DEFINED in MAIN_PROMPT_v6

**What it contains:**
- 10-section report structure specification
- Section-by-section templates
- Markdown formatting requirements
- Metrics and statistics guidelines
- Department customization rules

**Where defined:** `REPORT_OUTPUT_SCHEMA_v2.1.md` (not included in MAIN_PROMPT_v6)

---

### 4. ENTITY_MAPPING_GUIDE_v2.1.md
**Status:** NOT MENTIONED in MAIN_PROMPT_v6

**What it contains:**
- Activity → Entity mapping patterns
- Operational vs Project classification rules
- Confidence scoring methodology
- Department-specific examples
- Edge case handling

**Where defined:** `ENTITY_MAPPING_GUIDE_v2.1.md` (not included in MAIN_PROMPT_v6)

---

### 5. Department Prompt Logs
**Status:** NOT MENTIONED in MAIN_PROMPT_v6

**What they are:**
- Primary data source for each department
- Format: `{DEPT} prompt log.md`
- Contains timestamped activity logs from AI assistants
- Separate from employee daily.md files

**Location pattern:** `Dropbox/Nov25/{DEPT} Nov25/{DEPT} prompt log.md`

**Examples:**
- `Dropbox/Nov25/AI Nov25/AI prompt log.md`
- `Dropbox/Nov25/Fin Nov25/Finance prompt log.md`
- `Dropbox/Nov25/Design Nov25/Design prompt log.md`

---

## OPERATIONAL DIFFERENCES

### Task Classification Philosophy

#### MAIN_PROMPT_v6 Approach
```
ALL work → Extract tasks → Create entities (MLT/TSK/STP)
```
**Result:** Everything becomes a project/milestone/task

#### Department Prompts v2.1 Approach
```
Work → Classify:
  ├─ 80-90% → Operational/Maintenance (routine, recurring)
  └─ 10-20% → Project Work (PRT/MLT/TSK)
```
**Result:** Realistic separation of operational vs strategic work

### Examples:

**Finance:**
- Month-end closing → **Operational** (recurring monthly)
- Invoice processing → **Operational** (daily routine)
- Financial automation initiative → **Project** (PRT-###)

**AI:**
- Infrastructure configs → **Operational** (maintenance)
- Tool integration → **Operational** or TST-### (depends on scope)
- AI Tutorial Research → **Project** (PRT-001)

---

## FILE PATH DISCREPANCIES

### MAIN_PROMPT_v6 Paths
```
ENTITIES/
├── DAILIES/Week3/20/{Employee_Name}/Daily.md
├── REPORTS/Daily_Reports/YYYY-MM-DD_{DEPT}.md
├── TASK_MANAGERS/DATA/*.csv
└── LIBRARIES/{Type}/
```

### Actual Department Prompts Paths
```
Dropbox/
└── Nov25/
    ├── AI Nov25/
    │   ├── AI prompt log.md
    │   ├── {Employee}/Week_{N}/{DAY}/daily.md
    │   └── Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
    ├── Fin Nov25/
    │   ├── Finance prompt log.md
    │   ├── {Employee}/Week_{N}/{DAY}/daily.md
    │   └── Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
    └── [Other Departments]/
```

**🔴 CRITICAL ISSUE:** Completely different base paths and structure!

---

## RECOMMENDATIONS FOR MAIN_PROMPT_v7

### 1. Integrate Department Prompt Structure ⭐⭐⭐
**Add new module:** `09_Daily_Report_System.md`

**Content:**
- PMT-032: Daily Report Collection orchestration
- PMT-070: Entity Mapping tool specification
- 10-section report schema
- Operational vs Project classification
- Department-specific mapping rules

---

### 2. Update File Paths & Data Sources ⭐⭐⭐
**Update:** `05_File_Operations.md`

**Changes:**
```markdown
## DAILY PROCESSING DATA SOURCES (CURRENT)

### Department Prompt Logs (Primary Source)
Location: `Dropbox/Nov25/{DEPT} Nov25/{DEPT} prompt log.md`

Examples:
- AI: Dropbox/Nov25/AI Nov25/AI prompt log.md
- Finance: Dropbox/Nov25/Fin Nov25/Finance prompt log.md
- Design: Dropbox/Nov25/Design Nov25/Design prompt log.md

### Employee Daily Files (Secondary Source)
Location: `Dropbox/Nov25/{DEPT} Nov25/{Employee}/Week_{N}/{DAY}/daily.md`

### Report Outputs
Location: `Dropbox/Nov25/{DEPT} Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
```

---

### 3. Add Employee & Team Details ⭐⭐
**Update:** `04_Department_Operations.md`

**Add for each department:**
- Team Size
- Employee names, IDs, roles, contacts
- Status (Work/Available/Left)
- Specific prompt log locations
- Specific output paths

---

### 4. Document PMT-032 & PMT-070 ⭐⭐⭐
**Create:** `06A_PMT-032_Collection_Orchestration.md`
**Create:** `06B_PMT-070_Entity_Mapping_Tool.md`

**Content:**
- Complete specifications
- Usage examples
- Department-specific mapping rules
- Confidence scoring
- Operational classification

---

### 5. Define Report Schema ⭐⭐⭐
**Create:** `10_Report_Schema_v2.1.md`

**Content:**
- 10-section structure
- Section templates
- Department customization rules
- Quality standards per section
- Metrics and deliverables format

---

### 6. Add Real Project/Task Examples ⭐⭐
**Update:** `01_Core_Identity.md`

**Replace made-up examples with:**
- PRT-001_AI_Tutorial_Research
- PRT-007_System_Analysis
- TST-015_Extract_Taxonomy_Tutorial_Videos
- TST-055_Process_Department_Task_Files

---

### 7. Tool Catalogs by Department ⭐
**Create:** `11_Department_Tool_Catalogs.md`

**Content:**
- AI: LLMs, development tools, research tools
- Finance: Accounting software, banking, spreadsheets
- Design: Design software, asset tools, prototyping
- [etc. for all 10 departments]

---

## PRIORITY ACTION ITEMS

### Immediate (Before using MAIN_PROMPT_v6 for daily reports)

1. ✅ **Read actual department prompts** (PMT-033 to PMT-043 v2.1)
2. ✅ **Document PMT-032 orchestration** (collection process)
3. ✅ **Document PMT-070 entity mapping** (how it works, mapping rules)
4. ✅ **Define 10-section report schema** (templates, examples)
5. ✅ **Update file paths** to match actual Dropbox/Nov25/ structure

### Short-term (Within 1 week)

6. ⏳ **Add employee details** to each department
7. ⏳ **Create tool catalogs** for each department
8. ⏳ **Add real project/task examples** from TASK_MANAGERS
9. ⏳ **Document Operational vs Project classification**
10. ⏳ **Update workflow execution** with 4-step process

### Long-term (Within 1 month)

11. ⏳ **Unify path structure** (choose ENTITIES/ or Dropbox/Nov25/)
12. ⏳ **Create MAIN_PROMPT_v7** with all department prompt integration
13. ⏳ **Build validation tools** for 10-section reports
14. ⏳ **Standardize quality metrics** across departments

---

## CONCLUSION

**MAIN_PROMPT_v6** is currently a **high-level architectural document** that describes generic task extraction and entity management.

**Department Prompts v2.1** are **operational specifications** that detail exactly how daily reports are generated, with:
- Specific data sources (prompt logs + employee dailies)
- 10-section report structure
- PMT-070 entity mapping tool
- Operational vs Project classification
- Department-specific quality standards

**Gap Severity:** 🔴 **CRITICAL**

**Recommendation:** Either:
1. **Update MAIN_PROMPT_v6** to incorporate all department prompt details (becomes v7), OR
2. **Position MAIN_PROMPT_v6** as "System Architecture" and keep Department Prompts as "Operational Specifications"

**Current Status:** MAIN_PROMPT_v6 cannot be used alone for daily report generation without significant additions.

---

**End of Inconsistency Analysis**
