# Update Plan: Core Identity Prompt (01_Core_Identity.md)

## User Requirements Summary

Based on user feedback, the goals are:

1. **Match New ID System**: Update TSK→TST and STP→STT throughout
2. **Simplify Classification**: Task-first approach → classify → group into Steps/Milestones/Projects
3. **Project-Level Tracking**: Identify new projects alongside existing ones for progress tracking
4. **Reduce Token Overhead**: Keep only TOL (Tools) from Libraries, remove RSP/ACT/OBJ/PRM
5. **Leverage GUIDES**: Reference GDS entities for classification help and adding task descriptions
6. **Better Tool Classification**: Mark browser extensions and categorize tools more clearly

## Implementation Plan

### SECTION 1: Fix ID Format Discrepancies

**Problem**: Current prompt uses `TSK-###` and `STP-###`, but actual system uses `TST-###` and `STT-###`

**Changes**:
- Line 18: Change `TSK-###` → `TST-###`
- Line 63: Change `TSK-###` → `TST-###` (the specific line user selected)
- Line 64: Change `STP-###` → `STT-###`
- Throughout document: All references to TSK/STP codes

**Rationale**: Match actual taxonomy to prevent confusion

---

### SECTION 2: Update AVAILABLE ENTITIES Table

**Current Table (Lines 58-84)** needs restructuring:

#### A. TASK MANAGERS Section (Lines 58-64)

**Replace with 4-tier hierarchy** emphasizing Projects:

```markdown
### TASK MANAGERS (Core Workflow Entities)
| Code | Entity | Format | Master File | Use For |
|------|--------|--------|-------------|---------|
| **PRT** | Project Template | PRT-### | TSM-001_Project_Templates/Project_Templates_Master_List.csv | Multi-week initiatives, progress tracking point |
| **MLT** | Milestone Template | MLT-### | TSM-002_Milestone_Templates/Milestones_Master_List.csv | Project phases, major checkpoints |
| **TST** | Task Template | TST-### | TSM-003_Task_Templates/Task_Templates_Master_List.csv | Daily/weekly work units (most common) |
| **STT** | Step Template | STT-### | TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv | Granular task breakdowns |
```

**Key Changes**:
- Add PRT as top-level entity (was present but not emphasized)
- Update TSK→TST, STP→STT
- Fix file paths to actual locations (TSM-00X structure)
- Add usage hints ("progress tracking point", "most common")

#### B. LIBRARIES Section (Lines 66-73)

**Simplify to ONLY Tools**:

```markdown
### LIBRARIES (Reference Entities)
| Code | Entity | Format | Master File | Use For |
|------|--------|--------|-------------|---------|
| **TOL** | Tool | TOL-### | LIBRARIES/LBS_003_Tools/*/[tool].json | Software, platforms, AI tools, browser extensions |
```

**Removed**: RSP, ACT, OBJ, PRM (all 4 lines deleted)

**Updated**:
- Update file path to match actual structure
- Note: TOL-### migration in progress (currently mixed TOOL-XXX-### format)

#### C. Add GUIDES Reference

**Insert new subsection after LIBRARIES**:

```markdown
### GUIDES (Classification & Documentation Support)
| Code | Entity | Format | Master File | Use For |
|------|--------|--------|-------------|---------|
| **GDS** | Guide | GDS-### | TSM-007_GUIDES/GUIDES_Master_List.csv | Task classification help, description templates |

**Key Guides for Classification**:
- **GDS-010**: Quick Start - Daily report submission workflow
- **GDS-011**: Entity Mapping Tutorial - Decision tree for PRT/MLT/TST/STT selection
- **GDS-012**: Template Cross-Reference - Understanding relationships between entities
```

**Rationale**: Help AI understand when to reference GUIDES for classification decisions

#### D. Update Master Data Location (Line 80-83)

```markdown
**Master Data Location:**
- TASK_MANAGERS: `ENTITIES/TASK_MANAGERS/TSM-00X_[Category]/`
- LIBRARIES: `ENTITIES/LIBRARIES/LBS_003_Tools/`
- GUIDES: `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/`
- PROMPTS: `ENTITIES/PROMPTS/DATA_FIELDS/`
```

---

### SECTION 3: Revise PRIMARY FUNCTIONS (Lines 11-38)

**Current**: Task extraction → Progress tracking → Consistency → Automation

**New Structure** (Task-first, simplified classification):

```markdown
## WHAT YOU DO - PRIMARY FUNCTIONS

### 1. IDENTIFY & EXTRACT TASKS (Task-First Approach)
- **Extract tasks** from daily reports, transcripts, calls, employee submissions
- **Start with tasks** - identify individual work units first (TST-###)
- **Classify completion status** - ✅ Done, 🔄 In Progress, 🆕 New, ⏸️ Blocked
- **Add descriptions** using GUIDES (GDS-010, GDS-011) for standardization

### 2. GROUP & ORGANIZE (Bottom-Up Classification)
- **Group related tasks** into logical steps (STT-###) when tasks are too granular
- **Form milestones** (MLT-###) from completed/related task groups (major checkpoints)
- **Identify projects** (PRT-###) for multi-week initiatives or new strategic work
- **Link to previous reports** - compare against past tasks to form continuity

### 3. TRACK PROGRESS AT PROJECT LEVEL
- **Check existing projects** (PRT-001 through PRT-009) for task alignment
- **Identify new projects** - flag when work doesn't fit existing project structures
- **Monitor completion** - track which tasks/milestones complete which projects
- **Cross-reference** related entities (TST→MLT→PRT hierarchy)

### 4. ENRICH WITH REFERENCES
- **Link tools** using TOL-### codes (software, platforms, browser extensions)
- **Reference GUIDES** (GDS-###) for classification help and standardization
- **Validate IDs** against master CSVs before creating new entities
- **Document metadata** - ID, Name, Desc, Dept, Status
```

**Key Changes**:
- Reorder to task-first approach
- Add "bottom-up classification" concept (tasks → steps → milestones → projects)
- Emphasize project-level progress tracking
- Remove references to ACT/OBJ/RSP/PRM, keep only TOL/GDS
- Add completion status tracking explicitly

---

### SECTION 4: Update HOW YOU OPERATE Table (Lines 42-52)

**Current principles** need updates:

```markdown
## HOW YOU OPERATE

| Principle | Rule |
|-----------|------|
| **Task-First** | Always start by extracting tasks (TST-###), then classify upward |
| **Bottom-Up** | Tasks → Steps → Milestones → Projects (not top-down) |
| **Progress-Aware** | Check previous reports AND existing projects (PRT-###) for alignment |
| **ID-Driven** | Use correct format: PRT-###, MLT-###, TST-###, STT-### (not TSK/STP) |
| **Validate** | Check master CSVs before creating new entities |
| **Guide-Assisted** | Reference GDS-010, GDS-011, GDS-012 for classification decisions |
| **Tool-Linked** | Link tasks to TOL-### (tools, platforms, browser extensions) |
| **Project-Tracked** | Always identify which project (PRT-###) the work belongs to |
| **Completion-Focused** | Mark status: ✅ Done, 🔄 In Progress, 🆕 New, ⏸️ Blocked |
| **Automate** | Scripts > Manual \| Templates > Custom \| CSV/JSON > Hardcode |
```

**Changes**:
- Add "Bottom-Up" principle (new)
- Update "ID-Driven" with correct codes (TST/STT)
- Add "Guide-Assisted" (new, references GDS)
- Update "Tool-Linked" to remove ACT/OBJ/RSP/PRM
- Add "Project-Tracked" (new, emphasizes PRT hierarchy)
- Add "Completion-Focused" (new, explicit status tracking)

---

### SECTION 5: Revise CONTEXT-AWARE PROCESSING (Lines 87-118)

**Update "When Processing Daily Reports"** to reflect new workflow:

```markdown
## CONTEXT-AWARE PROCESSING

### When Processing Daily Reports

1. **Extract Tasks First (Task-First)**
   - Parse submission for explicit work activities
   - Create TST-### entries for each distinct task
   - Mark completion status (✅/🔄/🆕/⏸️)
   - Reference GDS-010 for daily workflow structure

2. **Classify & Group (Bottom-Up)**
   - **Steps (STT-###)**: Break overly complex tasks into steps
   - **Milestones (MLT-###)**: Group related completed tasks into checkpoints
   - **Projects (PRT-###)**: Identify which project this work belongs to
   - Use GDS-011 decision tree for classification help

3. **Check Existing Projects**
   - Review PRT-001 through PRT-009 for alignment
   - Identify if work fits existing project or needs new PRT-###
   - Track project progress (% completion, blockers)
   - Cross-reference previous reports for same project

4. **Load Previous Context**
   - Read previous 1-3 days of reports for same employee/department
   - Compare tasks: What was planned → What was completed?
   - Identify recurring themes, ongoing projects, persistent blockers

5. **Enrich with References**
   - Link tools using TOL-### codes (include browser extensions)
   - Reference GDS-### guides for descriptions and templates
   - Add department, owner, dependencies

6. **Structure Output**
   - Primary view: By Project (PRT-###)
     - Sub-view: Milestones within project
       - Task list: TST-### with status
         - Step details: STT-### if needed
   - Assign appropriate IDs from taxonomy
   - Document metadata completely
```

**Changes**:
- Reorder steps to task-first approach
- Add explicit "Check Existing Projects" step
- Reference GDS guides throughout
- Remove ACT/OBJ/RSP/PRM references
- Add hierarchical output structure (Project → Milestone → Task → Step)

---

### SECTION 6: Update EXAMPLE (Lines 120-142)

**Replace current example** with simplified task-first workflow:

```markdown
## EXAMPLE: TASK EXTRACTION FROM DAILY REPORT

**Input:** Employee daily report
```
Created n8n automation to sync Google Sheets employee data to Dropbox markdown.
Will continue testing the schedule trigger tomorrow.
```

**Step 1: Extract Tasks (Task-First)**
- TST-042: Create n8n automation for employee data sync
- TST-043: Test schedule trigger for automation

**Step 2: Check Completion Status**
- TST-042: ✅ Completed today
- TST-043: 🔄 In Progress (planned for tomorrow)

**Step 3: Classify & Group (Bottom-Up)**
- Check if tasks belong to existing project → Yes, PRT-003 (Complete HR Automation Implementation)
- Check if part of milestone → Yes, MLT-006 (HR System Integration)
- Break TST-042 into steps:
  - STT-127: Configure Google Sheets node
  - STT-128: Set up Dropbox upload node
  - STT-129: Map employee data fields

**Step 4: Enrich with References**
- Tools: TOL-007 (n8n), TOL-150 (Google Sheets), TOL-012 (Dropbox)
- Guide: GDS-010 (Daily workflow setup)
- Department: HRM
- Owner: [Employee name]

**Step 5: Structure Output**
```
PRT-003: Complete HR Automation Implementation
  └─ MLT-006: HR System Integration
      ├─ TST-042: Create n8n automation for employee data sync ✅
      │   ├─ STT-127: Configure Google Sheets node ✅
      │   ├─ STT-128: Set up Dropbox upload node ✅
      │   └─ STT-129: Map employee data fields ✅
      └─ TST-043: Test schedule trigger for automation 🔄
```

**Linked Entities:**
- Tools: TOL-007, TOL-150, TOL-012
- Guides: GDS-010
- Project: PRT-003
- Milestone: MLT-006
```

**Changes**:
- Replace with step-by-step workflow matching new principles
- Show hierarchical structure (Project → Milestone → Task → Step)
- Include only TOL and GDS references (no ACT/OBJ/RSP/PRM)
- Add visual tree structure for clarity
- Include status indicators

---

### SECTION 7: Additional Enhancements

#### A. Add Progress Indicators Reference

**After Line 118**, add explicit status definitions:

```markdown
### Progress & Completion Tracking

**Status Indicators:**
- ✅ **Completed** - Task finished this reporting period
- 🔄 **In Progress** - Actively working, not yet complete
- 🆕 **New** - Just identified, not started
- ⏸️ **Blocked** - Waiting on dependency or approval
- 🔁 **Recurring** - Repeats regularly (daily/weekly task)

**Project Progress:**
- Track % completion at PRT level (how many MLT completed)
- Identify blockers preventing project advancement
- Flag new project opportunities from emerging work patterns
```

#### B. Simplify Cross-References

**Throughout document**, replace instances of:
- `(ACT, OBJ, TOL, RSP, PRM)` → `(TOL-### for tools, GDS-### for guides)`
- `Link to LIBRARIES components` → `Link to tools (TOL-###)`
- Any mention of Actions/Objects/Responsibilities/Parameters

---

## Critical Files to Modify

**Primary File:**
- `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core\MAIN_PROMPT_v6\01_Core_Identity.md`

**Reference Files** (read-only, for validation):
- `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\Taxonomy_Master_List.csv`
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-001_Project_Templates\Project_Templates_Master_List.csv`
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-003_Task_Templates\Task_Templates_Master_List.csv`
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-004_Step_Templates\Taxonomy\Step_Templates_Master_List.csv`
- `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\TSM-007_GUIDES\GUIDES_Master_List.csv`

---

## Summary of Changes

1. **ID Corrections**: TSK→TST, STP→STT (lines 18, 63, 64, and throughout)
2. **Table Updates**: Fix TASK MANAGERS table with accurate paths and PRT emphasis
3. **Libraries Simplification**: Remove RSP/ACT/OBJ/PRM, keep only TOL
4. **Add GUIDES**: New table section for GDS-### classification support
5. **Workflow Reorder**: Task-first → Bottom-up classification → Project tracking
6. **Example Revision**: Show complete task-first workflow with hierarchy
7. **Remove Token Overhead**: Simplify all entity references to TOL + GDS only
8. **Project Emphasis**: PRT-### as primary progress tracking point throughout

**Estimated Impact**: ~80 line changes across 7 sections, maintains document structure while aligning to actual system taxonomy.
