# Phase 0: Master Context Document
## ENTITIES System Rebuild - Multi-Agent Execution Plan

**Created**: 2025-11-22
**Owner**: Niko Kar
**Status**: Active
**Execution Model**: Multi-phase, multi-agent simultaneous execution

---

## 📋 Overview

This master document indexes the complete multi-phase rebuild of the ENTITIES system. Each phase has a dedicated context document that provides detailed instructions, file paths, schemas, and prompts for AI agents to execute simultaneously.

---

## 🎯 Objectives

1. **Clean up system** - Remove duplicates, nested backups, invalid data
2. **Populate missing data** - Fill 298 empty prospect folders (when CRM data ready)
3. **Restructure RESEARCHES** - Organize scattered research files and video queue
4. **Build Deep Research system** - Task templates, employee dashboards, video queue accumulation
5. **Sync master lists** - Update all 10 CSV master lists with changes
6. **Document everything** - READMEs, migration logs, validation reports

---

## 📂 Phase Context Documents

### Phase 1: Data Cleanup & Consolidation
**File**: [Phase_1_Context_Cleanup.md](./Phase_1_Context_Cleanup.md)
**Agents**: 3 simultaneous
**Focus**: Backup cleanup, duplicate ID resolution, empty folder analysis
**Priority**: P1-HIGH

### Phase 2: PROSPECTS Population
**File**: [Phase_2_Context_Prospects.md](./Phase_2_Context_Prospects.md)
**Agents**: 2 simultaneous
**Focus**: Schema validation, master list update
**Priority**: P2-MEDIUM
**Status**: ⏸️ POSTPONED - Blocked on CRM data from Kolya/Olya

### Phase 3: RESEARCHES Restructuring + Video Queue
**File**: [Phase_3_Context_Research.md](./Phase_3_Context_Research.md)
**Agents**: 3 simultaneous
**Focus**: Research consolidation, video queue system, import flow documentation
**Priority**: P0-CRITICAL (per Russian transcript discussion)

### Phase 4: Deep Research Task Manager + Employee Dashboards
**File**: [Phase_4_Context_DeepResearch.md](./Phase_4_Context_DeepResearch.md)
**Agents**: 4 simultaneous
**Focus**: Deep research tasks, employee dashboards, Online Academy gap analysis, portfolio diversity tracker
**Priority**: P0-CRITICAL (solves "goat problem" + video research workflow)

### Phase 5: Master Lists Sync + Validation
**File**: [Phase_5_Context_Integration.md](./Phase_5_Context_Integration.md)
**Agents**: 4 simultaneous
**Focus**: CSV sync, JSON validation, taxonomy update, cross-reference validation
**Priority**: P1-HIGH

### Phase 6: Documentation + Integration
**File**: [Phase_6_Context_Documentation.md](./Phase_6_Context_Documentation.md)
**Agents**: 2 simultaneous
**Focus**: README generation, migration documentation
**Priority**: P2-MEDIUM

---

## 🔄 Execution Flow

```
Phase 0: Context Creation (THIS PHASE)
    ↓
    [YOU ARE HERE - Creating context documents]
    ↓
Phase 1: Cleanup (3 agents)
    ↓
    [VALIDATION GATE - Manual review of cleanup reports]
    ↓
Phase 3 + Phase 4 (7 agents total, run in parallel)
    ↓
    [VALIDATION GATE - Test video queue + review sample dashboard]
    ↓
Phase 5: Integration (4 agents)
    ↓
    [VALIDATION GATE - Review validation reports]
    ↓
Phase 6: Documentation (2 agents)
    ↓
    [FINAL REVIEW]
```

**Note**: Phase 2 executes independently when CRM data becomes available.

---

## 🗂️ System Structure Reference

### Base Path
```
C:\Users\Dell\Dropbox\ENTITIES\
```

### Critical Entities (17 total)
```
ENTITIES/
├── ACCOUNTS/
├── ARCHIVE/
├── ASSETS/
├── BUSINESSES/          ← Phase 2
├── DAILIES/             ← Phase 4 (dashboard data source)
├── IMPORTS/
├── JOBS/
├── LIBRARIES/           ← Phase 1 (cleanup)
├── LOG/
├── PLANS/
│   └── System_Rebuild_2025-11/  ← YOU ARE HERE
├── PROMPTS/             ← Referenced by all phases
├── REPORTS/             ← Phase 5 (validation output)
├── RESEARCHES/          ← Phase 3
├── Scripts/
├── SETTINGS/
├── TALENTS/             ← Phase 4 (employee dashboards)
├── TASK_MANAGERS/       ← Phase 1 & 4
└── TAXONOMY/            ← Phase 5
```

---

## 📊 Key Metrics (Current State)

| Metric | Count | Status |
|--------|-------|--------|
| Total Entities | 1,590 | ✅ Cataloged |
| Total Files | 621 | ✅ Indexed |
| Master CSV Lists | 10 | ⚠️ Needs sync |
| Departments | 9 | ✅ Organized |
| Employees | 32 | ✅ Profiled |
| Prompts | 63 | ✅ Cataloged |
| Tools | 164 | ⚠️ 23 duplicate IDs |
| Actions | 429 | ✅ Cataloged |
| Objects | 110 | ✅ Cataloged |
| Skills | 28 | ✅ Migrated |
| Professions | 17 | ✅ Organized |
| Clients | 5 | ✅ Active |
| Prospects (with data) | 33 | ⚠️ Partial |
| Prospects (empty folders) | 298 | ❌ Needs population |
| Milestone Templates | 28 | ✅ Organized |
| Task Templates | 50+ | ⚠️ 23 duplicate IDs |
| Duplicate IDs Found | 23 | ❌ Needs fixing |
| Nested Backup Levels | 8 | ❌ Needs cleanup |
| Invalid JSON Files | 1 | ❌ Needs fixing |

---

## 🎯 Success Criteria

### Phase 1 Success
- [ ] Zero nested backups deeper than 1 level
- [ ] All 23 duplicate IDs resolved
- [ ] Decision made on 298 empty folders (keep/delete)
- [ ] All reports reviewed manually

### Phase 3 Success
- [ ] Video queue accepts 20 videos before manual review
- [ ] Metadata captured: views, likes, publish_date, channel
- [ ] Research import flow documented
- [ ] Test with 5 sample videos passes

### Phase 4 Success
- [ ] Deep Research task template created
- [ ] Sample employee dashboard generated for Niko Kar
- [ ] Online Academy gap analysis complete
- [ ] Portfolio diversity tracker flags duplicate "goat" projects
- [ ] Manual approval tested with 1 designer

### Phase 5 Success
- [ ] All 10 master CSVs synchronized
- [ ] Invalid JSON fixed
- [ ] Taxonomy updated with new entities
- [ ] Cross-reference validation passes

### Phase 6 Success
- [ ] README.md in all major folders
- [ ] Migration log complete
- [ ] Rollback instructions documented

---

## 🔑 Key Design Decisions

### 1. Parallel Execution
**Decision**: Run 3-4 agents simultaneously per phase on independent folders
**Rationale**: Faster execution, no file conflicts if agents work on separate entities
**Risk**: Requires careful path separation in context docs

### 2. Manual Validation Gates
**Decision**: Human review between phases (not auto-approval)
**Rationale**: Per Russian transcript - "не на автоутверждение она мануально" - keeps humans engaged
**Implementation**: Each phase produces reports for manual review before next phase

### 3. Context-First Approach
**Decision**: Create all instruction docs in Phase 0 before agents execute
**Rationale**: Ensures agents have complete context, prompts, and paths
**Benefit**: Can review all plans before execution starts

### 4. Relative Paths Everywhere
**Decision**: All paths relative to `C:\Users\Dell\Dropbox\ENTITIES/`
**Rationale**: System portability, easier agent instructions
**Format**: `LIBRARIES/LBS_003_Tools/` not `C:\Users\Dell\...\LBS_003_Tools\`

### 5. No Database Build Yet
**Decision**: Everything in Markdown/CSV/JSON for manual review
**Rationale**: Per your note - "not planning to build a database for now... building a kind of database preview with markdown"
**Next Step**: Manual review of architecture before technical build

### 6. Priority: Research + Deep Research
**Decision**: Phase 3 & 4 are P0-CRITICAL
**Rationale**: Per Russian transcript - video research queue and Deep Research workflow are immediate needs
**Evidence**: "первая твоя цель на данный момент это не сделать research и не сделать task... тебе нужно только один task который будет называться deep research"

### 7. Portfolio Problem Solution
**Decision**: Phase 4 includes portfolio diversity tracker
**Rationale**: Solves "goat problem" - designers showing duplicate projects
**Implementation**: CSV tracking project diversity scores, flags duplicates across employees

---

## 📝 Master Prompts Reference

All phases reference prompts from `PROMPTS/` folder. Key prompts:

### Research Prompts
- `PROMPTS/DEPARTMENTS/Research/Deep_Research_Prompts/`
- `PROMPTS/WORKFLOWS/Research_Workflow_Prompts/`

### Video Processing Prompts
- `PROMPTS/DEPARTMENTS/Video/Video_Analysis_Prompts/`
- `PROMPTS/UTILITIES/Video_Metadata_Extraction/`

### Daily Report Prompts
- `PROMPTS/DEPARTMENTS/Daily_Reports/` (10 department templates)

### Task Manager Prompts
- `PROMPTS/WORKFLOWS/Task_Creation_Prompts/`

### Taxonomy Prompts
- `PROMPTS/SYSTEM/Taxonomy_Integration/`

---

## 🔍 Validation Reports Location

All validation reports and agent outputs will be saved to:

```
REPORTS/2025-11-22/System_Rebuild/
├── Phase_1_Cleanup_Report.md
├── Phase_1_Duplicate_IDs_Resolution.csv
├── Phase_1_Empty_Folders_Analysis.md
├── Phase_3_Video_Queue_Test_Results.md
├── Phase_4_Sample_Dashboard_Niko_Kar.html
├── Phase_4_Online_Academy_Gap_Analysis.md
├── Phase_4_Portfolio_Diversity_Report.csv
├── Phase_5_CSV_Sync_Report.md
├── Phase_5_JSON_Validation_Report.md
├── Phase_5_Cross_Reference_Validation.md
└── Phase_6_Migration_Log_2025-11-22.md
```

---

## 👥 Employee Context

**Primary User**: Niko Kar
**Department**: AI Department
**Role**: System Architecture & Research
**Discord ID**: [To be added]

**Related Employees** (will receive dashboards in Phase 4):
- 11 LG Team Leads (for expanded industries)
- 9 Designers (for portfolio diversity tracking)
- 3 Video editors (for video queue system)
- All 32 employees (for personal task dashboards)

---

## 🚀 Next Steps After Phase 0

1. **Review all 6 context documents** created in this phase
2. **Confirm agent instructions** are clear and complete
3. **Validate file paths** in each context doc
4. **Execute Phase 1** with 3 simultaneous agents
5. **Manual validation** of Phase 1 reports
6. **Proceed to Phase 3 + 4** (highest priority)

---

## 📅 Timeline Expectations

**Note**: No time estimates per your instruction - "planning without timelines". Focus on what needs to be done, not when.

**Phases ordered by dependency**, not duration:
1. Phase 0 → Phase 1 (sequential)
2. Phase 1 → Phase 3 + 4 (Phase 1 must complete first)
3. Phase 3/4 → Phase 5 (Phases 3/4 must complete first)
4. Phase 5 → Phase 6 (Phase 5 must complete first)

Phase 2 executes independently when unblocked.

---

## 🔗 Related Documents

- [ENTITIES System Analysis Report](../../analysis_report.md)
- [LIBRARIES README](../../LIBRARIES/README.md)
- [TASK_MANAGERS README](../../TASK_MANAGERS/README.md)
- [Migration History](../../ARCHIVE/MIGRATION_COMPLETED_2025-11-17.md)
- [Master Activity Listing](../../REPORTS/2025-11-21/MASTER_ACTIVITY_LISTING_2025-11-21.csv)

---

## 📞 Questions/Issues

If agents encounter issues during execution:
1. **Log to**: `LOG/System_Rebuild_2025-11-22_Session_[N].md`
2. **Flag in**: Validation reports (see structure above)
3. **Escalate**: Via Discord to Niko Kar

---

## ✅ Phase 0 Checklist

- [ ] Phase_0_Context_Master.md created (THIS FILE)
- [ ] Phase_1_Context_Cleanup.md created
- [ ] Phase_2_Context_Prospects.md created
- [ ] Phase_3_Context_Research.md created
- [ ] Phase_4_Context_DeepResearch.md created
- [ ] Phase_5_Context_Integration.md created
- [ ] Phase_6_Context_Documentation.md created
- [ ] All context docs reviewed by Niko Kar
- [ ] Validation reports folder created
- [ ] Ready to execute Phase 1

---

**END OF MASTER CONTEXT**
**Next**: Review this document, then proceed to Phase 1 context creation.
