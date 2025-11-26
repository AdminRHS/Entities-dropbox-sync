# MLT-004: Gap Analysis

**Milestone ID:** MLT-004
**Milestone Name:** Gap Analysis
**Duration:** 45 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 4 of 9

---

## Overview

Classify all extracted tasks using the RESEARCHES Gap Analysis methodology. Determine which tasks have existing templates (EXISTS), which need templates only (LIBRARY_ONLY), or which need complete creation (NEW).

---

## What You'll Do

### 1. Learn Gap Analysis Methodology

**Reference Location:**
```
/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/
```

**Three-Tier Classification:**

#### EXISTS ✅
- Task template already exists in TASK_MANAGERS
- All required tools/objects exist in LIBRARIES
- **Action:** Use existing TST-### template

#### LIBRARY_ONLY ⚠️
- No task template in TASK_MANAGERS
- BUT all tools/objects exist in LIBRARIES
- **Action:** Create TST-### template only

#### NEW 🆕
- No task template in TASK_MANAGERS
- Some/all tools/objects missing from LIBRARIES
- **Action:** Create library entries (TOL/OBJ/ACT) + TST-### template

---

### 2. Check Against Existing Templates

**Compare extracted tasks against:**

**Task Templates:**
```
/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/
```
Current count: 71 templates (TST-001 to TST-071)

**Example Templates:**
- TST-045: Research_Video_Tools
- TST-067: Create_Presentation_PowerPoint
- TST-046: Automate_Version_Control
- TST-007: Create_Job_Posting

---

### 3. Check LIBRARIES Coverage

**Tools Library:**
```
/ENTITIES/LIBRARIES/Tools/
```
~200+ tools cataloged

**Actions Library:**
```
/ENTITIES/LIBRARIES/Actions/
```
429 actions cataloged

**Objects Library:**
```
/ENTITIES/LIBRARIES/Objects/
```
50+ objects cataloged

---

### 4. Perform Classification

For each extracted task:

**Step 1:** Check if TST-### template exists
- YES → Check if template is complete → EXISTS
- NO → Go to Step 2

**Step 2:** Check if all tools/objects exist in LIBRARIES
- YES → LIBRARY_ONLY
- NO → NEW

---

## Gap Analysis Output Format

**Save to:**
```
/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/03_Gap_Analysis/Gap_Analysis_2025-11-25.md
```

**Structure:**
```markdown
# Gap Analysis - 2025-11-25

**Analysis Date:** 2025-11-25
**Tasks Analyzed:** 87
**Analyst:** [Your Name]

---

## Coverage Snapshot

| Classification | Count | Percentage |
|----------------|-------|------------|
| **EXISTS** ✅ | 45 | 52% |
| **LIBRARY_ONLY** ⚠️ | 28 | 32% |
| **NEW** 🆕 | 14 | 16% |
| **TOTAL** | 87 | 100% |

---

## EXISTS (Use Existing Templates) - 45 tasks

### 1. Send_Email_Via_Gmail
**Existing Template:** TST-045
**Action:** ACT-089 (Send)
**Object:** OBJ-GEN-012 (Email)
**Tool:** TOL-BIZ-008 (Gmail)
**Status:** ✅ Complete - Use TST-045
**Assigned To:** [TBD in MLT-006]

### 2. Create_Presentation_PowerPoint
**Existing Template:** TST-067
**Action:** ACT-042 (Create)
**Object:** OBJ-GEN-015 (Presentation)
**Tool:** TOL-BIZ-020 (PowerPoint)
**Status:** ✅ Complete - Use TST-067
**Assigned To:** [TBD in MLT-006]

[...list all 45 EXISTS tasks]

---

## LIBRARY_ONLY (Create Template Only) - 28 tasks

### 1. Export_Contacts_CSV_LinkedIn
**Required Tools:** TOL-LGN-015 (LinkedIn Sales Navigator) ✅ Exists
**Required Actions:** ACT-067 (Export) ✅ Exists
**Required Objects:** OBJ-LGN-008 (Contact List) ✅ Exists
**Template Exists:** ❌ No TST-### template
**Action Required:** Create TST-072: Export_Contacts_CSV_LinkedIn
**Priority:** High
**Department:** Lead Generation (LGN)

### 2. Analyze_Video_Metrics_YouTube
**Required Tools:** TOL-VID-012 (YouTube Analytics) ✅ Exists
**Required Actions:** ACT-089 (Analyze) ✅ Exists
**Required Objects:** OBJ-VID-015 (Video Metrics) ✅ Exists
**Template Exists:** ❌ No TST-### template
**Action Required:** Create TST-073: Analyze_Video_Metrics_YouTube
**Priority:** Medium
**Department:** Video (VID)

[...list all 28 LIBRARY_ONLY tasks]

---

## NEW (Create Everything) - 14 tasks

### 1. Generate_Leads_Via_Hunter_IO
**Missing Entities:**
- ❌ Tool: Hunter.io (not in LIBRARIES/Tools/)
- ✅ Action: ACT-128 (Generate) exists
- ✅ Object: OBJ-LGN-005 (Lead List) exists
**Action Required:**
1. Create TOL-LGN-042: Hunter.io tool entry
2. Create WRF-015: Hunter.io lead generation workflow
3. Create TST-074: Generate_Leads_Via_Hunter_IO template
**Priority:** High
**Department:** Lead Generation (LGN)
**Assigned To:** [TBD in MLT-006]

### 2. Create_3D_Animation_Blender
**Missing Entities:**
- ❌ Tool: Blender (not in LIBRARIES/Tools/)
- ❌ Object: 3D Animation (not in LIBRARIES/Objects/)
- ✅ Action: ACT-042 (Create) exists
**Action Required:**
1. Create TOL-DGN-045: Blender tool entry
2. Create OBJ-DGN-025: 3D Animation object entry
3. Create SKL-025: "create 3D animation via Blender" skill
4. Create TST-075: Create_3D_Animation_Blender template
**Priority:** Medium
**Department:** Design (DGN)
**Assigned To:** [TBD in MLT-006]

[...list all 14 NEW tasks]

---

## Recommendations

### Immediate Actions (For MLT-005)
1. Create 28 TST-### templates for LIBRARY_ONLY tasks
2. Create 14 TST-### templates for NEW tasks
3. Create missing library entries for NEW tasks:
   - 8 new tools (TOL-###)
   - 3 new objects (OBJ-###)
   - 2 new skills (SKL-###)

### Library Expansion Priority
1. **High Priority** (7 tasks): Tools for lead generation and AI automation
2. **Medium Priority** (5 tasks): Design and video production tools
3. **Low Priority** (2 tasks): Specialty tools (rare use cases)

### Template Creation Order
1. LIBRARY_ONLY tasks (faster, no library work needed)
2. NEW high-priority tasks (critical for operations)
3. NEW medium/low-priority tasks

---

## Department-Specific Analysis

### AI & Automation (AID)
- Total Tasks: 18
- EXISTS: 10 (56%)
- LIBRARY_ONLY: 5 (28%)
- NEW: 3 (16%)
- **Gap:** AI automation tools need expansion

### Design (DGN)
- Total Tasks: 22
- EXISTS: 12 (55%)
- LIBRARY_ONLY: 7 (32%)
- NEW: 3 (13%)
- **Gap:** 3D tools and advanced design objects missing

### Lead Generation (LGN)
- Total Tasks: 25
- EXISTS: 10 (40%)
- LIBRARY_ONLY: 9 (36%)
- NEW: 6 (24%)
- **Gap:** Lead generation tools need significant expansion

### Video (VID)
- Total Tasks: 12
- EXISTS: 7 (58%)
- LIBRARY_ONLY: 4 (33%)
- NEW: 1 (9%)
- **Gap:** Minor - video production well-covered

### Sales (SLS)
- Total Tasks: 6
- EXISTS: 4 (67%)
- LIBRARY_ONLY: 2 (33%)
- NEW: 0 (0%)
- **Gap:** None - sales templates complete

### Development (DEV)
- Total Tasks: 3
- EXISTS: 2 (67%)
- LIBRARY_ONLY: 1 (33%)
- NEW: 1 (33%)
- **Gap:** Minor - one new MCP tool needed

### HR (HRM)
- Total Tasks: 1
- EXISTS: 0 (0%)
- LIBRARY_ONLY: 0 (0%)
- NEW: 1 (100%)
- **Gap:** HR templates need foundational work
```

---

## Taxonomy Integration

### Task Template ID Assignment

Next available IDs for NEW templates:

| Current Last ID | Next Available | Count Needed | Range to Assign |
|-----------------|----------------|--------------|-----------------|
| TST-071 | TST-072 | 42 | TST-072 to TST-113 |

### Tool ID Assignment

Next available IDs for NEW tools:

| Category | Last ID | Next Available | Count Needed |
|----------|---------|----------------|--------------|
| TOL-LGN | TOL-LGN-041 | TOL-LGN-042 | 3 |
| TOL-DGN | TOL-DGN-044 | TOL-DGN-045 | 2 |
| TOL-AIA | TOL-AIA-080 | TOL-AIA-081 | 2 |
| TOL-DEV | TOL-DEV-025 | TOL-DEV-026 | 1 |

**Reference:** [TAX-001 Libraries Master List](../../../TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv)

---

## Checklist

- [ ] Load RESEARCHES Gap Analysis examples
- [ ] Review TSM-003 Task Templates (71 templates)
- [ ] Review LIBRARIES Tools (~200 tools)
- [ ] Review LIBRARIES Actions (429 actions)
- [ ] Review LIBRARIES Objects (50+ objects)
- [ ] Classify all 87 extracted tasks
- [ ] Create coverage snapshot table
- [ ] List all EXISTS tasks with TST IDs
- [ ] List all LIBRARY_ONLY tasks with requirements
- [ ] List all NEW tasks with missing entities
- [ ] Create department-specific analysis
- [ ] Generate recommendations for MLT-005
- [ ] Save Gap_Analysis_2025-11-25.md
- [ ] Update processing log with gap analysis metrics

---

## Expected Outcomes

✅ **Gap Analysis Complete**
- **Coverage Report:** EXISTS vs LIBRARY_ONLY vs NEW breakdown
- **Department Analysis:** Gap analysis per department
- **Action Plan:** Clear list of templates/entities to create in MLT-005

✅ **Ready for MLT-005**
- Know which templates to create (42 new TST-###)
- Know which library entries needed (8 tools, 3 objects, 2 skills)
- Prioritized creation order established

---

## Next Milestone

**→ [MLT-005: Template Creation](MLT-005_Template_Creation.md)** - Create 42 new TST-### templates for LIBRARY_ONLY and NEW tasks (30 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Gap Analysis Examples:** [RESEARCHES Gap Analysis](../../../TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/)
- **Task Templates:** [TSM-003 Task Templates](../../../TASK_MANAGERS/TSM-003_Task_Templates/)
- **Libraries Master List:** [TAX-001 Libraries Master List](../../../TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
