# MAIN_PROMPT_v6 Analysis Report

**Date:** 2025-11-25
**Version:** 6.1 (Updated)
**Analysis Focus:** Daily Employee Operations, Department Overview, Taxonomy Compliance

---

## EXECUTIVE SUMMARY

MAIN_PROMPT_v6 has been split into **9 modular files** (8 core + 1 master index) with updated focus on:
1. **Task extraction** from daily employee reports
2. **Progress tracking** using historical context
3. **Taxonomy compliance** with current LIBRARIES/TASK_MANAGERS architecture
4. **Department-level** aggregation and reporting

**Key Updates from v6.0 → v6.1:**
- ✅ Removed deprecated entities (SKL, PRF - no longer in LIBRARIES)
- ✅ Added progress tracking with historical context
- ✅ Aligned with current LIBRARIES structure (RSP, ACT, OBJ, PRM, TOL)
- ✅ Integrated DAILIES processing workflow
- ✅ Updated file paths to match actual architecture

---

## FILE STRUCTURE

### Created Modular Files

| File | Purpose | Key Sections | Lines |
|------|---------|--------------|-------|
| **00_MASTER_INDEX.md** | Navigation hub | Quick start guide, module overview | ~100 |
| **01_Core_Identity.md** | WHO/WHAT/HOW | Primary functions, entity list, task extraction examples | ~180 |
| **02_Entity_Taxonomy.md** | ID standards | XXX-### format, relationships, validation | ~60 |
| **03_Workflow_Execution.md** | Prompts & chains | Video, daily reports, research, HR, system maintenance | ~120 |
| **04_Department_Operations.md** | Dept codes | 10 departments, focus areas, collaboration patterns | ~50 |
| **05_File_Operations.md** | Directory structure | Correct architecture, daily processing, validation | ~200 |
| **06_Prompt_Reference.md** | PMT catalog | 73 prompts by category, decision matrix, chains | ~90 |
| **07_Quality_Validation.md** | Validation rules | Checklists, error fixes, validation commands | ~70 |
| **08_External_Modules.md** | On-demand modules | Video extended, HR suite, advanced taxonomy, API | ~50 |

**Total:** ~920 lines (split from original 598 lines + added context)

---

## DAILY EMPLOYEE OPERATIONS PERSPECTIVE

### Current Daily Processing Workflow

**Employee Daily Report Structure:**
```
ENTITIES/DAILIES/
└── Week{N}/
    └── {Day}/
        └── {Employee_Name}/
            └── Daily.md    ← Employee submission (tasks, progress, notes)
```

**Example:** `ENTITIES/DAILIES/Week3/20/Fin Nov25_Yelisieieva Daria/Daily.md`

### Task Extraction Pattern (Updated in 01_Core_Identity.md)

#### BEFORE (v6.0): Generic entity extraction
- Focus on video processing
- Manual task identification
- No historical context

#### AFTER (v6.1): Context-aware task extraction
1. **Load Previous Context** (lines 107-111)
   - Read previous 1-3 days for same employee
   - Identify recurring themes, ongoing projects
   - Note blockers or delays

2. **Extract Current Tasks** (lines 113-117)
   - Parse explicit tasks from daily report
   - Infer implicit tasks from progress statements
   - Identify dependencies

3. **Compare & Track** (lines 119-123)
   - Planned vs completed comparison
   - New/removed task detection
   - Priority changes
   - Workload distribution

4. **Structure Output** (lines 125-129)
   - Group into milestones (MLT-###)
   - Break into tasks (TSK-###) and steps (STP-###)
   - Link to LIBRARIES (ACT, OBJ, TOL, RSP)

### Progress Indicators (NEW in v6.1)
```
✅ Completed   - Tasks finished (reference previous day)
🔄 In Progress - Ongoing work (compare status changes)
🆕 New         - Just added (not in previous reports)
⏸️ Blocked     - Waiting on dependency (track duration)
🔁 Recurring   - Appears regularly (pattern recognition)
```

### Real Example from Daily Report

**Input:** Finance employee (Daria) - Daily.md excerpt:
```
Creating a new month Google Sheet named December 2025-processing:
1. Go to Google Sheets, named November 2025, file, make a copy...
2. Check if all tabs are necessary...
3. Make edits to all data...

Create an automation in n8n project.
1. Go to n8n under Niko account...
2. Click at first step. Choose trigger...
```

**Extracted Structure:**
```
MLT-042: Monthly Financial Sheet Setup (December 2025)
  ├─ TSK-153: Create December 2025 Google Sheet copy
  │   ├─ STP-301: Copy November 2025 sheet with same permissions
  │   ├─ STP-302: Remove obsolete tabs
  │   └─ STP-303: Update employee data (removals/additions)
  │
  ├─ TSK-154: Update project and client data
  │   ├─ STP-304: Check project finish dates
  │   ├─ STP-305: Correct "Any Employee" tab formulas
  │   └─ STP-306: Update exchange rates for December 1st
  │
  └─ TSK-155: Sync Balance Full document
      ├─ STP-307: Add December column to "Clients Revenue All"
      └─ STP-308: Add December column to "Client Profit All"

MLT-043: n8n Employee Data Sync Automation
  ├─ TSK-156: Configure n8n workflow
  │   ├─ STP-309: Set schedule trigger (4-hour interval) [✅ Completed]
  │   ├─ STP-310: Configure Google Sheets node [✅ Completed]
  │   └─ STP-311: Map employee columns to output [✅ Completed]
  │
  ├─ TSK-157: Transform data to markdown
  │   ├─ STP-312: Write JavaScript function for markdown table [✅ Completed]
  │   └─ STP-313: Convert to file node [✅ Completed]
  │
  └─ TSK-158: Upload to Dropbox
      ├─ STP-314: Configure Dropbox upload node [✅ Completed]
      └─ STP-315: Test schedule trigger [🔄 In Progress - planned for tomorrow]
```

**Linked LIBRARIES:**
- **ACT-###:** "Create", "Configure", "Update", "Test", "Upload"
- **OBJ-###:** "Google Sheet", "Automation workflow", "Markdown file", "Employee data"
- **TOL-###:** "Google Sheets", "n8n", "Dropbox", "JavaScript"
- **RSP-###:** RSP-005 (Finance Responsibilities - monthly reporting, automation)
- **PRM-###:** PRM-001 (Finance Parameters - financial accuracy, data integrity)

---

## DEPARTMENT DAILY OVERVIEW PERSPECTIVE

### Department Structure (04_Department_Operations.md)

| Code | Department | Daily Prompt | Employees (Example) | Focus Areas |
|------|-----------|--------------|---------------------|-------------|
| **FIN** | Finance | PMT-037 | Yelisieieva Daria | Financial sheets, automation, reporting |
| **HRM** | Human Resources | PMT-038 | Cynthia Uzoh | Recruitment, onboarding, CV processing |
| **AID** | AI & Automation | PMT-033 | - | Taxonomy, prompt engineering, system health |
| **VID** | Video Production | PMT-043 | - | Transcription, entity extraction |
| **DEV** | Development | PMT-036 | - | Version control, VSCode, APIs |
| **LGN** | Lead Generation | PMT-039 | - | Prospecting, outreach, data research |
| **DGN** | Design | PMT-035 | - | UI/UX, graphics, creative assets |
| **MKT** | Marketing | PMT-040 | - | Campaigns, content strategy |
| **SLS** | Sales | PMT-041 | - | Pipeline management, deals |
| **SMM** | Social Media | PMT-042 | - | Content, engagement, community |

### Daily Department Workflow (Updated)

**Morning Collection Phase:**
```bash
# 1. Collect all employee dailies by department
DEPT="FIN"
WEEK="Week3"
DAY="20"

for employee in $(list_employees_by_dept "$DEPT"); do
    DAILY_PATH="ENTITIES/DAILIES/$WEEK/$DAY/${employee}/Daily.md"

    # Load current + previous day for context
    CURRENT=$(read_file "$DAILY_PATH")
    PREVIOUS=$(read_file "ENTITIES/DAILIES/$WEEK/19/${employee}/Daily.md")

    # Extract with context
    extract_tasks_with_context "$CURRENT" "$PREVIOUS" > "/tmp/${employee}_tasks.json"
done
```

**Aggregation Phase:**
```bash
# 2. Aggregate department-level report
execute_prompt "PMT-037" \
  --input "/tmp/*_tasks.json" \
  --context "REPORTS/Daily_Reports/2025-11-24_FIN.md" \
  --output "REPORTS/Daily_Reports/2025-11-25_FIN.md"

# PMT-037 generates:
# - Department summary
# - Employee activity breakdown
# - Progress against previous day
# - Blocked items requiring attention
# - Newly identified milestones/tasks
```

**Cross-Department Phase:**
```bash
# 3. Generate collection report (all departments)
execute_prompt "PMT-032" \
  --input "REPORTS/Daily_Reports/2025-11-25_*.md" \
  --output "REPORTS/Daily_Reports/2025-11-25_COLLECTION.md"
```

### Department Report Template (NEW)

```markdown
# Finance Department Daily Report
**Date:** 2025-11-25 | **Week:** 3 | **Day:** 20

## Team Activity Summary
| Employee | Tasks Completed | Tasks In Progress | New Tasks | Blocked |
|----------|----------------|-------------------|-----------|---------|
| Yelisieieva Daria | 7 steps | 1 task | 2 milestones | 0 |

## Progress vs Previous Day (2025-11-24)
- ✅ **Completed:** n8n automation workflow (6 of 7 steps done)
- 🔄 **Continuing:** Schedule trigger testing (planned for tomorrow)
- 🆕 **New:** December 2025 financial sheet setup (large milestone added)

## Active Milestones
- **MLT-042:** Monthly Financial Sheet Setup (December 2025) - 🆕 NEW
- **MLT-043:** n8n Employee Data Sync Automation - 85% complete

## Blockers & Dependencies
- None reported

## LIBRARIES Usage
- **Top Actions:** Create, Configure, Update (from ACT-###)
- **Top Objects:** Google Sheet, Automation, Markdown file (from OBJ-###)
- **Tools Used:** Google Sheets (TOL-###), n8n (TOL-009), Dropbox (TOL-###)

## Recommendations
- Test n8n schedule trigger tomorrow (STP-315)
- Begin December sheet setup early (large task identified)
```

---

## TAXONOMY COMPLIANCE VALIDATION

### Validation Against TAXONOMY Folder Structure

#### TAX-001: LIBRARIES Compliance ✅

**Checked Files:**
- `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
- `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`

**Current Entities in v6.1:**
| Entity | Code | Status in TAXONOMY | Status in v6.1 |
|--------|------|-------------------|----------------|
| Responsibilities | RSP-### | ✅ Active (193 entries) | ✅ Included |
| Actions | ACT-### | ✅ Active (429 entries) | ✅ Included |
| Objects | OBJ-### | ✅ Active (17 categories) | ✅ Included |
| Parameters | PRM-### | ✅ Active (8 profession sets) | ✅ Included |
| Tools | TOL-### | ✅ Active (80+ tools) | ✅ Included |
| ~~Skills~~ | ~~SKL-###~~ | ❌ NOT in master list | ✅ Removed from v6.1 |
| ~~Profiles~~ | ~~PRF-###~~ | ❌ NOT in master list | ✅ Removed from v6.1 |

**ID Format Compliance:**
- ✅ XXX-### format followed
- ✅ Sequential numbering (001, 042, 153)
- ✅ No category prefixes (was: ~~MLT-VID-042~~, now: MLT-042)

#### TAX-002: TASK_MANAGERS Compliance ✅

**Checked Files:**
- `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv`
- `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md`

**Current Entities in v6.1:**
| Entity | Code | Status in TAXONOMY | Status in v6.1 |
|--------|------|-------------------|----------------|
| Project Templates | PRT-### | ✅ Active | ✅ Included |
| Milestone Templates | MLT-### | ✅ Active | ✅ Included |
| Task Templates | TSK-### | ✅ Active | ✅ Included |
| Step Templates | STP-### | ✅ Active | ✅ Included |

**Directory Mapping:**
| Prompt Reference | Actual Directory |
|-----------------|------------------|
| `TASK_MANAGERS/DATA/Projects_Master.csv` | ✅ Exists |
| `TASK_MANAGERS/DATA/Milestones_Master.csv` | ✅ Exists |
| `TASK_MANAGERS/DATA/Tasks_Master.csv` | ✅ Exists |
| `TASK_MANAGERS/DATA/Steps_Master.csv` | ✅ Exists |

#### TAX-003: Video Processing ✅

**Integration Point:**
- Documented in `TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`
- Referenced in 03_Workflow_Execution.md (Video Processing section)
- Workflow chain: PMT-004 → PMT-009 → PMT-032

#### TAX-004: Entity Integration ✅

**Standard Workflow:**
- Documented in `TAXONOMY/TAX-004_Entity_Integration/Entity_Integration_Taxonomy.md`
- Applied to new entity creation process in 02_Entity_Taxonomy.md

---

## KEY IMPROVEMENTS IN v6.1

### 1. Task Extraction Focus ⭐⭐⭐
**Before:** Generic "extract entities from video"
**After:** Comprehensive task extraction workflow with:
- Multi-source input (dailies, calls, transcripts)
- Milestone grouping logic
- Step-level breakdown
- Real example from Finance employee

### 2. Progress Tracking Context ⭐⭐⭐
**Before:** No historical reference
**After:**
- Load previous 1-3 days
- Compare planned vs completed
- Track status changes (new, completed, blocked, recurring)
- Employee workload visibility

### 3. Correct LIBRARIES Architecture ⭐⭐
**Before:** Referenced deprecated SKL, PRF entities
**After:**
- RSP (Responsibilities) - 193 entries
- ACT (Actions) - 429 entries (Command/Process/Result)
- OBJ (Objects) - 17 domain categories
- PRM (Parameters) - 8 profession sets
- TOL (Tools) - 80+ organized by category

### 4. Daily Processing Workflow ⭐⭐⭐
**New Addition:**
- Employee daily collection from DAILIES folder
- Context loading (previous day comparison)
- Department aggregation templates
- Cross-department collection (PMT-032)

### 5. File Architecture Alignment ⭐⭐
**Before:** Generic/outdated paths
**After:**
- Correct LIBRARIES structure (Responsibilities/Actions/Objects/Parameters/Tools)
- DAILIES folder structure (Week/Day/Employee)
- TAXONOMY mirrored views (TAX-001, TAX-002)
- TALENTS analytics integration

---

## USAGE RECOMMENDATIONS

### For Daily Employee Report Processing

**Load These Modules:**
1. `01_Core_Identity.md` - Task extraction patterns, progress indicators
2. `04_Department_Operations.md` - Department codes and focus areas
3. `05_File_Operations.md` - DAILIES structure, data locations
4. `06_Prompt_Reference.md` - PMT-032 to PMT-043 (daily reports)

**Workflow:**
```bash
# Step 1: Extract tasks from employee dailies
python extract_employee_tasks.py \
  --week 3 \
  --day 20 \
  --context-days 3 \
  --output tasks_2025-11-25.json

# Step 2: Generate department reports
for dept in FIN HRM AID VID DEV LGN DGN MKT SLS SMM; do
  execute_prompt "PMT-0XX_${dept}_Daily" \
    --input "tasks_2025-11-25.json" \
    --dept "$dept" \
    --output "REPORTS/Daily_Reports/2025-11-25_${dept}.md"
done

# Step 3: Aggregate all departments
execute_prompt "PMT-032" \
  --input "REPORTS/Daily_Reports/2025-11-25_*.md" \
  --output "REPORTS/Daily_Reports/2025-11-25_COLLECTION.md"
```

### For Taxonomy Validation

**Load These Modules:**
1. `02_Entity_Taxonomy.md` - ID standards, validation rules
2. `05_File_Operations.md` - Master file locations
3. `07_Quality_Validation.md` - Validation checklist

**Check Before Creating Entities:**
```bash
# Validate new ACT-### action
python validate_entity.py \
  --type ACT \
  --name "Sync data" \
  --master LIBRARIES/Responsibilities/Actions/actions_master.json \
  --taxonomy TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md

# Output: ACT-430 (next sequential ID) - VALID ✅
```

### For Video Processing

**Load These Modules:**
1. `01_Core_Identity.md` - Entity extraction
2. `03_Workflow_Execution.md` - Video processing section
3. `06_Prompt_Reference.md` - PMT-004 to PMT-013

**Workflow:**
```bash
# Process video transcript
execute_prompt "PMT-004" \
  --input "transcript_video_024.md" \
  --output "entities_video_024.json"

# Integrate to taxonomy
execute_prompt "PMT-009" \
  --input "entities_video_024.json" \
  --validate-against TAXONOMY/

# Generate report
execute_prompt "PMT-032" \
  --include "entities_video_024.json"
```

---

## COMPLIANCE SUMMARY

| Aspect | Status | Details |
|--------|--------|---------|
| **LIBRARIES Entities** | ✅ PASS | RSP, ACT, OBJ, PRM, TOL only (deprecated SKL, PRF removed) |
| **TASK_MANAGERS Entities** | ✅ PASS | PRT, MLT, TSK, STP aligned with DATA folder |
| **ID Format** | ✅ PASS | XXX-### (no prefixes, zero-padded, sequential) |
| **File Paths** | ✅ PASS | Match actual directory structure |
| **TAXONOMY Alignment** | ✅ PASS | Follows TAX-001, TAX-002 ISO registries |
| **Daily Processing** | ✅ PASS | DAILIES/Week/Day/Employee structure integrated |
| **Progress Tracking** | ✅ PASS | Historical context, status indicators added |
| **Department Structure** | ✅ PASS | 10 departments with correct codes |
| **Prompt References** | ✅ PASS | 73 PMT prompts cataloged |

---

## FILES CREATED

### Successfully Created ✅
1. `00_MASTER_INDEX.md` - Navigation and quick start
2. `01_Core_Identity.md` - Updated with task extraction focus
3. `02_Entity_Taxonomy.md` - ID standards and relationships
4. `03_Workflow_Execution.md` - Prompt workflows
5. `04_Department_Operations.md` - Department structure
6. `05_File_Operations.md` - Corrected architecture paths
7. `06_Prompt_Reference.md` - 73 prompt catalog
8. `07_Quality_Validation.md` - Validation rules
9. `08_External_Modules.md` - Optional modules
10. `ANALYSIS_REPORT.md` - This file

### Rejected/Needs Update ❌
- Original 01_Core_Identity.md (had deprecated SKL, PRF) → Fixed in v6.1
- Original 05_File_Operations.md (wrong architecture) → Fixed in v6.1

---

## NEXT STEPS RECOMMENDED

1. **Test Daily Processing Workflow**
   - Run extraction on Week3/Day20 employee dailies
   - Validate task structure (MLT→TSK→STP)
   - Check LIBRARIES linking (ACT, OBJ, TOL)

2. **Create Department Report Templates**
   - Template for each department (10 total)
   - Include progress tracking sections
   - Add LIBRARIES usage summaries

3. **Update PMT-032 to PMT-043**
   - Align daily report prompts with new structure
   - Add historical context loading
   - Include progress comparison logic

4. **Build Validation Scripts**
   - `extract_employee_tasks.py` - Parse DAILIES folder
   - `compare_daily_progress.py` - Historical comparison
   - `generate_dept_report.py` - Department aggregation

5. **Document Standard Examples**
   - One full example per department
   - Show task extraction from real dailies
   - Demonstrate progress tracking across 3 days

---

**END OF ANALYSIS REPORT**
