# 2. ENTITY REFERENCE

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## ID FORMAT

**Pattern:** `XXX-###`
- **XXX:** 3 consonants (PRT, MLT, TST, STT, TOL, GDS, PMT)
- **###:** 3 digits, zero-padded (001, 042, 153)
- **Sequential:** No gaps, no category prefixes
- **Immutable:** IDs never change after assignment

**Examples:**
- ✅ CORRECT: MLT-001, TST-042, PMT-005, GDS-010, STT-127
- ❌ WRONG: MLT-1, TSK-VID-042, PMT-COR-005, GDS10, TST-42

---

## ENTITY TYPES

| Code | Entity | Use For | Master CSV |
|------|--------|---------|------------|
| **PRT** | Project Template | Multi-week initiatives, progress tracking | TSM-001_Project_Templates/Project_Templates_Master_List.csv |
| **MLT** | Milestone Template | Project phases, major checkpoints | TSM-002_Milestone_Templates/Milestones_Master_List.csv |
| **TST** | Task Template | Daily/weekly work units (most common) | TSM-003_Task_Templates/Task_Templates_Master_List.csv |
| **STT** | Step Template | 5-30 minute actions within tasks | TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv |
| **TOL** | Tool | Software, platforms, browser extensions | LIBRARIES/LBS_003_Tools/ |
| **GDS** | Guide | Classification help, decision trees | TSM-007_GUIDES/GUIDES_Master_List.csv |
| **PMT** | Prompt | Workflow automation prompts | PROMPTS/DATA_FIELDS/PMT_Master_List.csv |

---

## REUSABLE TEMPLATES (Many-to-Many)

Templates are **INDEPENDENT** and **REUSABLE**:
- Same STT-### can be used in multiple TST
- Same TST-### can be used in multiple MLT
- Same MLT-### can be used in multiple PRT

**No hard links** - Composition happens at runtime.

---

## DECISION TREE (from GDS-011)

**"Is this a complete work unit taking hours/days?"**
- ✅ YES → Create **TST-###** (Task Template)
- ❌ NO → Next question

**"Is this a 5-30 minute action within a larger task?"**
- ✅ YES → Create **STT-###** (Step Template)
- ❌ NO → Might be **MLT-###** (Milestone)

**"Does this span weeks with multiple milestones?"**
- ✅ YES → Create **PRT-###** (Project Template)
- ❌ NO → Check existing PRT-001 to PRT-009

---

## VALIDATION RULES

**Before creating new entity:**
1. Check master CSV for existing
2. Use next sequential ID (find highest, +1)
3. Fill all required metadata (Name, Description, Department)
4. Validate references (all linked PRT/MLT/TST/STT/TOL/GDS exist)
5. No duplicates

---

## PRACTICAL EXAMPLE

**Scenario:** "Set up n8n workflow to automate weekly reports"

**Classification:**
- Complete work unit? YES (takes hours) → **TST-###**
- Part of larger initiative? YES → Check projects
- Fits existing PRT-003 (HR Automation)? YES → Use MLT-006

**Breakdown:**
```
TST-055: Set up n8n weekly report automation
  ├─ STT-201: Create workflow canvas
  ├─ STT-202: Configure schedule trigger (every Monday 9am)
  ├─ STT-203: Add Google Sheets data source
  ├─ STT-204: Set up email notification node
  └─ STT-205: Test and deploy

Tools: TOL-007 (n8n), TOL-150 (Google Sheets), TOL-XXX (Gmail)
Guide: GDS-010
```

**Fits Into:**
```
PRT-003: Complete HR Automation Implementation
  └─ MLT-006: HR System Integration
      ├─ TST-042: Create n8n employee data sync ✅
      └─ TST-055: Set up n8n weekly report automation 🔄
```
