# PMT-032: Daily Report Collection v2.1

**Prompt ID:** PMT-032
**Version:** 2.1
**Department:** Cross-Department Utility
**Category:** Report Automation
**Date:** 2025-11-19
**Status:** Active

---

## Purpose

Automate collection of daily activities from department prompt logs and generate comprehensive department-specific reports with TASK_MANAGERS entity integration using token-efficient format.

**Key Updates (v2.1):**
- ✅ TASK_MANAGERS entity integration
- ✅ Token-efficient format: `TST-###_Name`
- ✅ 10-section report schema (streamlined from 14)
- ✅ Entity validation
- ✅ Project/milestone tracking
- ✅ Cross-department coordination
- ✅ Forward planning (Next Day Plans, Research, Improvements)

---

## Pre-Execution Setup

### Step 0: Load TASK_MANAGERS Entity Data

**Before processing any department logs**, load entity master files:

```
ENTITIES/TASK_MANAGERS/Project_Templates/Project_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Step_Templates/Taxonomy/Step_Templates_Master_List.csv
```

**Purpose:** Enable entity mapping for all department activities

**Validation:**
- ✅ Verify all CSV files exist
- ✅ Confirm columns: New_ID, Name, Description, Department, Status
- ✅ Load into memory for fast lookups

---

## Instructions for AI Assistant

### Step 1: Read All Department Prompt Logs

Read the following department prompt log files to collect today's activities:

**Active Departments:**
1. `Dropbox/Nov25/AI/AI prompt log.md` (AID)
2. `Dropbox/Nov25/Design/Design prompt log.md` (DGN)
3. `Dropbox/Nov25/Dev/Dev prompt log.md` (DEV)
4. `Dropbox/Nov25/LG/LG prompt log.md` (LGN)
5. `Dropbox/Nov25/Video/Video prompt log.md` (VID)
6. `Dropbox/Nov25/HR/HR prompt log.md` (HRM)
7. `Dropbox/Nov25/Finance/Finance prompt log.md` (FIN)
8. `Dropbox/Nov25/Sales/Sales prompt log.md` (SLS)
9. `Dropbox/Nov25/SMM/SMM prompt log.md` (SMM)
10. `Dropbox/Nov25/Content/Content prompt log.md` (CNT)

**Note:** MKT (Marketing) deprecated - not included

---

### Step 2: Determine Current Date

Use the system date to determine the day number (e.g., 19 for November 19, 2025).

**Format:** Two-digit day number (01, 02, 03... 30, 31)

---

### Step 3: Create Folder Structure

For each department, ensure the following folder structure exists:

```
/Nov25/{DEPARTMENT}/Reports/{DAY}/
```

**Example for day 19:**
- `/Nov25/AI/Reports/19/`
- `/Nov25/Design/Reports/19/`
- `/Nov25/Dev/Reports/19/`
- `/Nov25/LG/Reports/19/`
- `/Nov25/Video/Reports/19/`
- `/Nov25/HR/Reports/19/`
- `/Nov25/Finance/Reports/19/`
- `/Nov25/Sales/Reports/19/`
- `/Nov25/SMM/Reports/19/`
- `/Nov25/Content/Reports/19/`

---

### Step 4: Process Activities with Entity Mapping

**For each activity in department prompt logs:**

#### 4A: Extract Activity Details
- Title/description
- Actions taken
- Time spent
- Status (Completed/In Progress/Blocked)
- Results/deliverables

#### 4B: Map to TASK_MANAGERS Entities

**Invoke PMT-070** (Daily Report Entity Mapping) for each activity:

```python
# For each activity
entity_mapping = map_activity_to_entities(
    activity_desc=activity.description,
    department=department_code,  # AID, HRM, DEV, etc.
    date=current_date
)

# Output format: TST-###_Name → MLT-###_Name → PRT-###_Name
```

**Entity Format:** Token-efficient `{ISO-###}_{Name}`

**Examples:**
- `TST-055_Process_Department_Task_Files → MLT-002_Data_Inventory → PRT-007_System_Analysis`
- `TST-015_Extract_Taxonomy_Tutorial_Videos → MLT-001_Content_Analysis → PRT-001_AI_Tutorial_Research`

#### 4C: Handle Special Cases

**Operational/Maintenance Work:**
```markdown
**Entity:** Operational/Maintenance (No project mapping)
**Category:** Administrative Operations
```

**Cross-Department Projects:**
```markdown
**Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
**Role:** Lead | Support | Contributor
**Departments:** AID (Lead), DEV (Support)
```

**Low Confidence (<70%):**
```markdown
**Entity:** Pending Manual Review
**Best Guess:** TST-### (65%)
**Recommendation:** Review Task_Templates_Master_List.csv
```

---

### Step 5: Generate Department Reports (14-Section v2.1 Schema)

**File Name:** `Daily_Activity_Report_Nov{DAY}_2025.md`

**Report Structure:**

#### Section 1: Executive Summary
- Report period (date)
- Department name and code
- Total activities count
- Team size
- Overall status (On Track/At Risk/Blocked)
- Key achievements (3-5 bullet points)
- Project contributions summary

**Example:**
```markdown
# Daily Activity Report - AI Department (AID)
**Date:** November 19, 2025

## 1. Executive Summary

- **Department:** AI & Automation (AID)
- **Team Size:** 5
- **Activities Completed:** 8
- **Overall Status:** On Track ✅
- **Key Achievements:**
  - Completed entity mapping system v2.1
  - Processed 47 department task files
  - Integrated TASK_MANAGERS with daily reports

**Project Contributions:**
- PRT-001_AI_Tutorial_Research: 2 tasks completed
- PRT-007_System_Analysis: 3 tasks in progress
- Operational/Maintenance: 3 activities
```

---

#### Section 2: Project Contributions (NEW in v2.1)

Track activities by project template:

```markdown
## 2. Project Contributions

### PRT-001_AI_Tutorial_Research
- **Role:** Lead
- **Status:** In Progress
- **Activities Today:**
  - TST-015_Extract_Taxonomy_Tutorial_Videos: 3 hours (Completed)
  - MLT-001_Content_Analysis: 40% complete
- **Next Steps:** Continue taxonomy extraction from remaining 12 videos

### PRT-007_System_Analysis
- **Role:** Lead
- **Status:** Active
- **Activities Today:**
  - TST-055_Process_Department_Task_Files: 2.5 hours (Completed)
  - TST-058_Extract_Tasks_Daily_Files: 1.5 hours (In Progress)
  - MLT-002_Data_Inventory: 65% complete
- **Next Steps:** Validate extracted data against schema

### Operational/Maintenance
- **Activities:** 3 tasks (0.5 hours total)
- **Type:** Administrative operations, routine tasks
```

---

#### Section 3: Milestone Progress (NEW in v2.1)

Track progress on active milestones:

```markdown
## 3. Milestone Progress

### MLT-001_Content_Analysis (PRT-001)
- **Progress:** 40% → 52% (+12%)
- **Tasks Completed Today:** TST-015 (Extract Taxonomy)
- **Tasks In Progress:** TST-016 (Categorize Topics)
- **Blockers:** None
- **Timeline:** On track for Nov 25 completion

### MLT-002_Data_Inventory (PRT-007)
- **Progress:** 60% → 65% (+5%)
- **Tasks Completed Today:** TST-055 (Process Task Files)
- **Tasks In Progress:** TST-058 (Extract Daily Files)
- **Blockers:** Waiting on schema validation
- **Timeline:** On track for Nov 22 completion

### MLT-010_CV_Screening_Setup (PRT-003) [Cross-Dept Support]
- **Progress:** 30% → 35% (+5%)
- **Our Role:** Support (Development assistance for HR)
- **Activities Today:** TST-042 configuration support (1 hour)
- **Timeline:** On track for Dec 1 completion
```

---

#### Section 4: Task Sequences and Entity Mapping

Detailed breakdown of each activity with entity mappings:

```markdown
## 4. Task Sequences and Entity Mapping

### Activity 1: Process AI department task files
- **Entity:** TST-055_Process_Department_Task_Files → MLT-002_Data_Inventory → PRT-007_System_Analysis
- **Time:** 2.5 hours
- **Status:** Completed ✅
- **Confidence:** 95%
- **Priority:** High
- **Objective:** Process and validate task files from folders 04-11
- **Actions Taken:**
  - Extracted 47 task files
  - Validated against schema
  - Generated summary report
  - Updated task tracking database
- **Results:**
  - ✅ 47 files processed successfully
  - ✅ 0 validation errors
  - ✅ Database updated
  - ✅ Summary report created
- **Impact:** Improved task tracking accuracy by 25%

### Activity 2: Extract taxonomy from tutorial videos
- **Entity:** TST-015_Extract_Taxonomy_Tutorial_Videos → MLT-001_Content_Analysis → PRT-001_AI_Tutorial_Research
- **Time:** 3 hours
- **Status:** Completed ✅
- **Confidence:** 92%
- **Priority:** High
- **Objective:** Extract structured taxonomy from 8 tutorial videos
- **Actions Taken:**
  - Processed 8 videos with AI extraction
  - Categorized 124 topics
  - Validated taxonomy structure
  - Exported to CSV format
- **Results:**
  - ✅ 124 topics extracted
  - ✅ 8 videos completed
  - ✅ Taxonomy validated
  - ✅ CSV export ready
- **Impact:** Accelerated content analysis pipeline by 40%

### Activity 3: Daily administrative tasks
- **Entity:** Operational/Maintenance
- **Time:** 0.5 hours
- **Status:** Completed ✅
- **Category:** Administrative Operations
- **Actions Taken:**
  - Reviewed daily emails
  - Updated task status in tracking system
  - Team standup meeting
- **Impact:** Routine operations maintained
```

---

#### Section 5: Cross-Department Coordination (NEW in v2.1)

Track inter-department handoffs and dependencies:

```markdown
## 5. Cross-Department Coordination

### PRT-003_HR_Automation (Support Role)
- **Lead Department:** HRM (HR & Recruitment)
- **Supporting Departments:** DEV (Development), AID (AI & Automation)
- **Our Contribution Today:**
  - TST-042_Configure_ATS_Integration: Configuration support (1 hour)
  - Provided technical guidance on API integration
- **Status:** On track
- **Next Handoff:** Dev team to complete API testing by Nov 20

### Design Assets Request (Outgoing)
- **To Department:** DGN (Design)
- **Request:** Thumbnails for 8 tutorial videos (Activity 2)
- **Priority:** Medium
- **Deadline:** Nov 22
- **Status:** Request submitted, awaiting design queue

### Data Validation (Incoming)
- **From Department:** DEV (Development)
- **Request:** Validate extracted task data schema
- **Priority:** High
- **Timeline:** Nov 20
- **Status:** In progress (Activity 1 completed, validation pending)
```

---

#### Section 6: Department-Specific Content

**AI Department Example:**

```markdown
## 6. Infrastructure and Technical Achievements

### System Configurations
- Updated entity mapping system to v2.1
- Integrated token-efficient format across all prompts
- Configured CSV data loaders for TASK_MANAGERS

### Framework Enhancements
- Enhanced PMT-070 entity mapping algorithm
- Improved confidence scoring (now 92% average)
- Added department-specific pattern matching

### Tool Integrations
- Connected daily reports to TASK_MANAGERS hierarchy
- Automated entity validation pipeline
- Integrated project/milestone tracking

### Documentation Updates
- Created REPORT_OUTPUT_SCHEMA_v2.1.md
- Updated ENTITY_MAPPING_GUIDE_v2.1.md
- Published IMPLEMENTATION_PLAN_v2.1.md
```

**Design Department Example:**

```markdown
## 6. Creative Deliverables and Design Systems

### Design Deliverables
- Created 12 social media graphics for SMM campaign
- Designed 3 logo concepts for client project DGN-CLIENT-042
- Updated brand style guide v3.2

### Design System Development
- Enhanced component library (TST-009_Design_System_Development)
- Added 8 new UI components
- Updated design tokens for dark mode

### Video Production Support
- Created 15 video thumbnails for tutorial series
- Designed motion graphics templates
- Updated video branding assets

### Client Projects
- DGN-CLIENT-042: Brand identity (3 logo concepts delivered)
- DGN-CLIENT-038: Website redesign (wireframes in progress)
```

---

#### Section 7: Entity Activity Summary

```markdown
## 7. Entity Activity Summary

### Projects Active Today
1. **PRT-001_AI_Tutorial_Research** - 3 hours (2 tasks)
2. **PRT-007_System_Analysis** - 4 hours (2 tasks)
3. **PRT-003_HR_Automation** - 1 hour (1 task, support role)

**Total Project Time:** 8 hours
**Operational Time:** 0.5 hours

### Milestones Progressed Today
1. **MLT-001_Content_Analysis** - +12% progress
2. **MLT-002_Data_Inventory** - +5% progress
3. **MLT-010_CV_Screening_Setup** - +5% progress (support)

### Tasks Completed Today
1. **TST-015_Extract_Taxonomy_Tutorial_Videos** ✅
2. **TST-055_Process_Department_Task_Files** ✅
3. **TST-042_Configure_ATS_Integration** ✅ (support)

### Tasks In Progress
1. **TST-058_Extract_Tasks_Daily_Files** (60% complete)
2. **TST-016_Categorize_Topics** (40% complete)
```

---

#### Section 8: Metrics and Statistics

```markdown
## 8. Metrics and Statistics

### Time Allocation
| Category | Hours | Percentage |
|----------|-------|------------|
| Project Work | 8.0 | 94% |
| Operational | 0.5 | 6% |
| **Total** | **8.5** | **100%** |

### Task Distribution by Entity Type
| Entity Type | Count | Percentage |
|-------------|-------|------------|
| Tasks (TST) | 5 | 63% |
| Milestones (MLT) | 3 | 37% |
| Projects (PRT) | 3 | - |

### Project Contribution Breakdown
| Project | Hours | Tasks | Status |
|---------|-------|-------|--------|
| PRT-001_AI_Tutorial_Research | 3.0 | 2 | Active |
| PRT-007_System_Analysis | 4.0 | 2 | Active |
| PRT-003_HR_Automation | 1.0 | 1 | Support |
| Operational | 0.5 | 3 | - |

### Entity Mapping Confidence
| Confidence Level | Count | Percentage |
|------------------|-------|------------|
| High (>90%) | 4 | 80% |
| Medium (70-89%) | 1 | 20% |
| Low (<70%) | 0 | 0% |

**Average Confidence:** 92%
```

---

#### Section 9: Project Impact Assessment

```markdown
## 9. Project Impact Assessment

### PRT-001_AI_Tutorial_Research
- **Impact Level:** High
- **Today's Contribution:**
  - Extracted 124 taxonomy topics from 8 videos
  - Accelerated content analysis pipeline by 40%
  - Enabled structured content categorization
- **Project Health:** On Track ✅
- **Risk Factors:** None
- **Dependencies:** Design team (thumbnails requested)

### PRT-007_System_Analysis
- **Impact Level:** Critical
- **Today's Contribution:**
  - Processed 47 task files with 100% accuracy
  - Improved task tracking accuracy by 25%
  - Validated data integrity across 11 departments
- **Project Health:** On Track ✅
- **Risk Factors:** Pending schema validation from DEV
- **Dependencies:** Dev team validation (Nov 20)

### PRT-003_HR_Automation (Support)
- **Impact Level:** Medium (Support Role)
- **Today's Contribution:**
  - Configured ATS integration settings
  - Provided technical API guidance
  - Advanced milestone progress +5%
- **Project Health:** On Track ✅
- **Risk Factors:** None
- **Dependencies:** Dev team API testing (Nov 20)
```

---

#### Section 10: Key Deliverables

```markdown
## 10. Key Deliverables

### Files Created
1. `/ENTITIES/PROMPTS/UTILITIES/Daily_Updates/PMT-070_Daily_Report_Entity_Mapping_v2.1.md` (485 lines)
2. `/ENTITIES/PROMPTS/DEPARTMENTS/Daily_Reports/REPORT_OUTPUT_SCHEMA_v2.1.md` (672 lines)
3. `/ENTITIES/PROMPTS/DEPARTMENTS/Daily_Reports/ENTITY_MAPPING_GUIDE_v2.1.md` (449 lines)
4. `/Nov25/AI/Reports/19/Taxonomy_Extraction_Summary.csv` (124 rows)

**Total New Files:** 4
**Total Lines:** 1,806

### Files Modified
1. `/ENTITIES/TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv` (Added 3 new tasks)
2. `/ENTITIES/PROMPTS/PMT_Master_List.csv` (Updated PMT-070 to v2.1)

**Total Modified:** 2

### Major Outputs
- ✅ Entity mapping system v2.1 operational
- ✅ Token-efficient format implemented (60% token reduction)
- ✅ 47 task files processed and validated
- ✅ 124 taxonomy topics extracted and categorized
- ✅ Cross-department coordination established

### Status Summary
| Deliverable Type | Completed | In Progress | Pending |
|------------------|-----------|-------------|---------|
| Files Created | 4 | 0 | 0 |
| Files Modified | 2 | 0 | 0 |
| Documentation | 3 | 0 | 0 |
| System Integrations | 2 | 1 | 0 |
```

---

#### Section 11: Challenges and Solutions

```markdown
## 11. Challenges and Solutions

### Challenge 1: Entity Mapping Confidence Scoring
- **Problem:** Initial confidence scoring algorithm had 68% accuracy
- **Solution:** Enhanced keyword matching with department filtering and context analysis
- **Result:** Improved to 92% average confidence
- **Impact:** Reduced manual review requirements by 35%
- **Status:** Resolved ✅

### Challenge 2: CSV Path Inconsistencies
- **Problem:** Documentation referenced incorrect TASK_MANAGERS CSV paths
- **Solution:** Verified actual file locations and updated all references
- **Result:** All paths now point to correct locations
- **Impact:** Prevented future data loading errors
- **Status:** Resolved ✅

### Challenge 3: Cross-Department Project Visibility
- **Problem:** Support roles in multi-dept projects not clearly tracked
- **Solution:** Added Section 5 (Cross-Department Coordination) to schema
- **Result:** Clear handoff tracking and dependency management
- **Impact:** Improved inter-department collaboration awareness
- **Status:** Resolved ✅
```

---

#### Section 12: Recommendations for Follow-up

```markdown
## 12. Recommendations for Follow-up

### Immediate Actions (Next 24 Hours)
1. **Schema Validation:** Complete validation of extracted task data with DEV team
2. **Entity Review:** Review 1 medium-confidence entity mapping (TST-016, 85%)
3. **Design Request:** Follow up on thumbnail request for tutorial videos

### Short-term Improvements (This Week)
1. **Phase 4 Implementation:** Update all 11 department prompts to v2.1 schema
2. **Testing:** Generate test reports with new entity mapping system
3. **Documentation:** Update PMT_Master_List.csv with v2.1 versions
4. **Training:** Brief department heads on new entity integration features

### Long-term Enhancements (This Month)
1. **Executive Report:** Create executive aggregation from department reports
2. **Analytics Dashboard:** Build project/milestone progress visualization
3. **Automation:** Integrate entity mapping with report collection automation
4. **Optimization:** Further refine confidence scoring algorithm
```

---

#### Section 13: Entity Completion Tracking

```markdown
## 13. Entity Completion Tracking

### Tasks Completed Today
- ✅ **TST-015_Extract_Taxonomy_Tutorial_Videos** (3 hours)
  - Milestone: MLT-001_Content_Analysis (now 52% complete)
  - Project: PRT-001_AI_Tutorial_Research
- ✅ **TST-055_Process_Department_Task_Files** (2.5 hours)
  - Milestone: MLT-002_Data_Inventory (now 65% complete)
  - Project: PRT-007_System_Analysis
- ✅ **TST-042_Configure_ATS_Integration** (1 hour, support)
  - Milestone: MLT-010_CV_Screening_Setup (now 35% complete)
  - Project: PRT-003_HR_Automation

### Tasks In Progress
- 🔄 **TST-058_Extract_Tasks_Daily_Files** (60% complete, 1.5 hours today)
  - Milestone: MLT-002_Data_Inventory
  - Project: PRT-007_System_Analysis
  - Next Session: Continue extraction from remaining folders
- 🔄 **TST-016_Categorize_Topics** (40% complete, pending start)
  - Milestone: MLT-001_Content_Analysis
  - Project: PRT-001_AI_Tutorial_Research
  - Next Session: Begin categorization of 124 extracted topics

### Blocked Tasks
- None

### Milestone Completion Progress
| Milestone | Previous | Current | Change | Target Date |
|-----------|----------|---------|--------|-------------|
| MLT-001_Content_Analysis | 40% | 52% | +12% | Nov 25 |
| MLT-002_Data_Inventory | 60% | 65% | +5% | Nov 22 |
| MLT-010_CV_Screening_Setup | 30% | 35% | +5% | Dec 1 |
```

---

#### Section 14: Entity References Summary

```markdown
## 14. Entity References Summary

### All Entities Referenced Today

**Projects (3):**
1. PRT-001_AI_Tutorial_Research (Lead, Active)
2. PRT-007_System_Analysis (Lead, Active)
3. PRT-003_HR_Automation (Support, Active)

**Milestones (3):**
1. MLT-001_Content_Analysis → PRT-001
2. MLT-002_Data_Inventory → PRT-007
3. MLT-010_CV_Screening_Setup → PRT-003

**Tasks (5):**
1. TST-015_Extract_Taxonomy_Tutorial_Videos → MLT-001 → PRT-001 (Completed)
2. TST-055_Process_Department_Task_Files → MLT-002 → PRT-007 (Completed)
3. TST-042_Configure_ATS_Integration → MLT-010 → PRT-003 (Completed)
4. TST-058_Extract_Tasks_Daily_Files → MLT-002 → PRT-007 (In Progress)
5. TST-016_Categorize_Topics → MLT-001 → PRT-001 (In Progress)

**Operational Activities:** 3 (0.5 hours total)

### Entity Validation Status
- ✅ All entity IDs validated against master CSVs
- ✅ All hierarchy chains confirmed (TST → MLT → PRT)
- ✅ All entities Status = Active or In Progress
- ✅ Department alignment verified
- ✅ No orphaned entities
- ✅ Average confidence: 92%

### Department Alignment
| Entity | Entity Dept | Report Dept | Alignment |
|--------|-------------|-------------|-----------|
| TST-015 | AID | AID | ✅ Match |
| TST-055 | AID | AID | ✅ Match |
| TST-042 | HRM | AID | ✅ Cross-Dept Support |
| TST-058 | AID | AID | ✅ Match |
| TST-016 | AID | AID | ✅ Match |
```

---

### Report Footer

```markdown
---

## Report Metadata

**Report Generated:** November 19, 2025 18:00
**Department:** AI & Automation (AID)
**Team Size:** 5
**Report Version:** v2.1
**Schema Version:** 14-Section v2.1
**Entity Integration:** Enabled ✅
**Report Status:** Complete

---

## Summary Statistics

- **Total Activities:** 8 (5 project, 3 operational)
- **Total Time:** 8.5 hours
- **Projects Active:** 3 (2 lead, 1 support)
- **Milestones Progressed:** 3
- **Tasks Completed:** 3
- **Tasks In Progress:** 2
- **Deliverables Created:** 4 files (1,806 lines)
- **Average Entity Confidence:** 92%
- **Cross-Department Coordination:** 2 active

---

*End of Daily Activity Report*

**Next Report:** November 20, 2025
**Prepared By:** AI Assistant via PMT-032 v2.1
**Entity Mapping:** PMT-070 v2.1

---
```

---

## Department-Specific Extraction Patterns

### AI Department (AID)
**Focus Areas:**
- Infrastructure and system tasks
- Tool integrations (MCP, n8n, automation)
- Framework enhancements (prompts, workflows)
- Technical configurations
- Entity mapping and taxonomy work
- Documentation updates

**Common Projects:**
- PRT-001_AI_Tutorial_Research
- PRT-006_Research_Taxonomy_Pipeline
- PRT-007_System_Analysis

**Common Tasks:**
- TST-015_Extract_Taxonomy_Tutorial_Videos
- TST-055_Process_Department_Task_Files
- TST-058_Extract_Tasks_Daily_Files

---

### HR Department (HRM)
**Focus Areas:**
- Candidate sourcing and recruitment
- Interview scheduling and coordination
- CV screening and parsing
- Employee onboarding
- HR system automation

**Common Projects:**
- PRT-003_HR_Automation

**Common Tasks:**
- TST-039_Setup_n8n_CV_Screening
- TST-048_Create_Scoring_Algorithm
- TST-053_CV_Parser_Development

---

### Design Department (DGN)
**Focus Areas:**
- Client design deliverables
- Brand identity and style guides
- Video thumbnails and motion graphics
- UI/UX design work
- Design system development

**Common Projects:**
- PRT-008_VIDEO_Production
- Client projects (DGN-CLIENT-###)

**Common Tasks:**
- TST-012_Create_Logo_Concepts
- TST-010_UI_UX_Design
- TST-009_Design_System_Development
- TST-007_Create_Video_Thumbnails

---

### Development Department (DEV)
**Focus Areas:**
- Feature development
- Bug fixes and maintenance
- API integrations
- Testing and QA
- Code reviews

**Common Projects:**
- PRT-002_MCP_Automation_Stack
- PRT-003_HR_Automation (Support)

**Common Tasks:**
- TST-001_AI_Powered_HTML_Parsing
- TST-042_Configure_ATS_Integration
- TST-045_Build_CV_Parser_Workflow

---

### Finance Department (FIN)
**Focus Areas:**
- Month-end closing processes
- Invoice processing and payment
- Bank reconciliation
- Financial reporting
- Budget tracking

**Note:** Most finance activities are Operational/Maintenance
**Occasional Projects:** Automation or system improvement initiatives

---

### Sales Department (SLS)
**Focus Areas:**
- Lead generation and qualification
- Client meetings and proposals
- Pipeline management
- Contract negotiations
- CRM updates

---

### Social Media Marketing (SMM)
**Focus Areas:**
- Content calendar planning
- Social media posts creation
- Engagement monitoring
- Campaign analytics
- Influencer coordination

---

### Content Department (CNT)
**Focus Areas:**
- Blog post writing
- Content strategy
- SEO optimization
- Editorial calendar
- Content distribution

---

### Video Department (VID)
**Focus Areas:**
- Video production and editing
- Script development
- Asset creation
- Publishing and distribution
- Performance analytics

**Common Projects:**
- PRT-008_VIDEO_Production

---

### Learning & Growth (LGN)
**Focus Areas:**
- Training material development
- Setup guides and documentation
- Onboarding processes
- Knowledge base updates
- Employee skill development

---

## Entity Mapping Integration

### Invoke PMT-070 for Each Activity

```python
# Pseudo-code for entity mapping integration

for department in active_departments:
    log_file = load_prompt_log(department)
    activities = extract_activities(log_file, current_date)

    for activity in activities:
        # Invoke PMT-070 entity mapping
        mapping = map_activity_to_entities(
            activity_desc=activity.description,
            department=department.code,
            date=current_date
        )

        # Add mapping to activity
        activity.entity = mapping.task
        activity.milestone = mapping.milestone
        activity.project = mapping.project
        activity.confidence = mapping.confidence
        activity.role = mapping.role  # Lead/Support/Contributor

        # Handle special cases
        if mapping.status == "low_confidence":
            activity.needs_review = True
        elif mapping.status == "operational":
            activity.entity = "Operational/Maintenance"
```

---

## Entity Validation Process

### Pre-Report Generation Validation

**Checklist for Each Entity Reference:**

1. **Format Validation**
   - ✅ Pattern matches: `{ISO-###}_{Name_With_Underscores}`
   - ✅ No colons, no spaces in format
   - ✅ No department letters in entity names

2. **Existence Validation**
   - ✅ Task ID exists in Task_Templates_Master_List.csv
   - ✅ Milestone ID exists in Milestone_Templates_Master_List.csv
   - ✅ Project ID exists in Project_Templates_Master_List.csv

3. **Hierarchy Validation**
   - ✅ Task belongs to Milestone (milestone_template_id correct)
   - ✅ Milestone belongs to Project (project_template_id correct)
   - ✅ No orphaned entities

4. **Status Validation**
   - ✅ All entities Status = Active or In Progress
   - ❌ Completed/Deprecated/Blocked entities flagged

5. **Department Alignment**
   - ✅ Task department matches report department OR
   - ✅ Cross-department role documented (Lead/Support)

**If Validation Fails:**
- Flag entity for manual review
- Include error message in report
- Suggest correction or alternative

---

## Report Quality Standards

### Content Requirements
- ✅ All 14 sections present and populated
- ✅ All activities from prompt logs included
- ✅ Entity mappings for all project work
- ✅ Confidence scores included
- ✅ Cross-department coordination documented
- ✅ Metrics and statistics calculated
- ✅ Impact analysis provided
- ✅ Challenges and solutions documented
- ✅ Files created/modified listed
- ✅ Recommendations for follow-up included

### Entity Integration Requirements
- ✅ All activities mapped to entities or marked Operational
- ✅ Token-efficient format used: `TST-###_Name`
- ✅ Entity validation passed
- ✅ Hierarchy chains complete (TST → MLT → PRT)
- ✅ Confidence scores ≥70% or flagged
- ✅ Cross-department roles documented
- ✅ Section 2, 3, 5, 7, 9, 13, 14 fully populated

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for statistics and metrics
- ✅ Bullet lists for achievements
- ✅ Checkboxes for completed items
- ✅ Consistent section structure (14 sections)
- ✅ Professional tone and language
- ✅ Clear, concise descriptions
- ✅ Entity format consistent throughout

### Technical Requirements
- ✅ File paths accurate and absolute
- ✅ Entity IDs validated against CSVs
- ✅ Department codes correct (AID, HRM, DEV, LGN, DGN, VID, SLS, SMM, FIN, CNT)
- ✅ Line counts included where applicable
- ✅ Tool names with URLs (if applicable)
- ✅ Employee names accurate
- ✅ Task counts verified
- ✅ Priority levels specified
- ✅ Time tracking accurate

---

## Execution Workflow

### Complete Automation Sequence

```
1. Load TASK_MANAGERS CSV files
   ↓
2. Read all department prompt logs
   ↓
3. Extract activities for current date
   ↓
4. For each activity:
   4a. Invoke PMT-070 entity mapping
   4b. Validate entity chain
   4c. Assign confidence score
   4d. Document cross-dept coordination
   ↓
5. Group activities by:
   - Project (Section 2)
   - Milestone (Section 3)
   - Task sequences (Section 4)
   ↓
6. Generate 14-section report
   ↓
7. Validate report quality
   ↓
8. Save to: /Nov25/{DEPT}/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
   ↓
9. Repeat for all active departments
```

---

## Example Command to AI Assistant

```
Generate comprehensive daily activity reports for November 19, 2025 with TASK_MANAGERS entity integration.

Use PMT-032 v2.1:

1. Load TASK_MANAGERS entity data from CSVs
2. Read all department prompt logs (AID, HRM, DEV, DGN, VID, LGN, SLS, SMM, FIN, CNT)
3. Map all activities to entities using PMT-070 v2.1
4. Generate 14-section reports with entity integration
5. Validate all entity references
6. Save reports to Nov25/{DEPARTMENT}/Reports/19/

Requirements:
- Token-efficient format: TST-###_Name
- All 14 sections populated
- Entity validation passed
- Cross-department coordination documented
- Confidence scores included
```

---

## Automation Schedule

### Recommended Timing
- **End of Day:** Generate reports at end of work day (18:00)
- **Next Morning:** Review reports before daily standup (09:00)
- **Weekly:** Compile weekly summary on Friday evening
- **Monthly:** Generate monthly executive report

### Trigger Conditions
Run this automation:
- At end of each work day (automatic)
- When explicitly requested
- Before important meetings
- For weekly/monthly reporting
- After major project milestones

---

## Troubleshooting

### Issue: Entity Mapping Failures
**Symptoms:** Activities not mapping to tasks
**Solutions:**
1. Verify TASK_MANAGERS CSV files loaded correctly
2. Check activity descriptions for clarity
3. Review PMT-070 confidence threshold settings
4. Consider operational/maintenance classification
5. Flag for manual review if needed

### Issue: Low Confidence Scores
**Symptoms:** Many entities below 70% confidence
**Solutions:**
1. Improve activity descriptions in prompt logs
2. Enhance keyword matching in PMT-070
3. Add department-specific patterns
4. Review and update Task_Templates_Master_List.csv
5. Provide more context in activity logs

### Issue: Missing Cross-Department Coordination
**Symptoms:** Section 5 empty or incomplete
**Solutions:**
1. Review prompt logs for multi-dept activities
2. Check for support roles in PRT-### projects
3. Verify handoff documentation in logs
4. Explicitly note cross-dept work in activity descriptions

### Issue: Invalid Entity Chains
**Symptoms:** Validation failures on TST → MLT → PRT hierarchy
**Solutions:**
1. Verify milestone_template_id and project_template_id in CSVs
2. Check for orphaned entities (no parent)
3. Confirm entity Status = Active
4. Report data integrity issues to system admin

### Issue: Report Sections Incomplete
**Symptoms:** Missing or empty sections 2, 3, 5, 7, 9, 13, 14
**Solutions:**
1. Ensure entity mapping completed for all activities
2. Verify project/milestone data populated
3. Check that operational work properly classified
4. Review department prompt log completeness

---

## Version History

**v2.1** - November 19, 2025
- ✅ Added TASK_MANAGERS entity integration
- ✅ Implemented token-efficient format
- ✅ Upgraded to 14-section schema
- ✅ Added PMT-070 entity mapping invocation
- ✅ Added Sections 2, 3, 5, 7, 9, 13, 14
- ✅ Enhanced validation and error handling
- ✅ Added cross-department coordination tracking
- ✅ Removed MKT (deprecated)

**v1.1** - November 16, 2025
- Removed deprecated AI department references
- Streamlined folder structure

**v1.0** - November 5, 2025
- Initial prompt creation
- Template structure defined
- All departments included

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Review Cycle:** Monthly
**Last Updated:** November 19, 2025

---

## Related Documents

- [PMT-070_Daily_Report_Entity_Mapping_v2.1.md](../UTILITIES/Daily_Updates/PMT-070_Daily_Report_Entity_Mapping_v2.1.md)
- [REPORT_OUTPUT_SCHEMA_v2.1.md](REPORT_OUTPUT_SCHEMA_v2.1.md)
- [ENTITY_MAPPING_GUIDE_v2.1.md](ENTITY_MAPPING_GUIDE_v2.1.md)
- [IMPLEMENTATION_PLAN_v2.1.md](IMPLEMENTATION_PLAN_v2.1.md)

---

*End of Prompt*
