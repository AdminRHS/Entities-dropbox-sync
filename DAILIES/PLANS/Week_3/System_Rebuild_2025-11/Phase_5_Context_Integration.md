# Phase 5 Context: Master Lists Sync + Validation

**Phase**: 5 of 6
**Agents**: 4 simultaneous
**Priority**: P1-HIGH
**Dependencies**: Phases 1, 3, 4 must complete (Phase 2 optional)
**Estimated Complexity**: Medium

---

## 🎯 Phase Objectives

1. **Sync all Master CSV Lists** - Update 10 master CSVs with Phase 1-4 changes
2. **Validate all JSON Files** - Fix invalid JSON, verify schema compliance
3. **Update TAXONOMY** - Regenerate TAX-001 through TAX-004
4. **Cross-Reference Validation** - Verify entity relationships across system

---

## 🤖 Agent Assignments

### Agent 5A: CSV Master List Sync Agent
**Focus**: Update all 10 master CSV files
**Working Directory**: Multiple (LIBRARIES, TASK_MANAGERS, PROMPTS, TAXONOMY, etc.)
**Output**: Updated CSVs + sync report

### Agent 5B: JSON Schema Validation Agent
**Focus**: Validate and fix all JSON files
**Working Directory**: Entire ENTITIES system
**Output**: Validation report + fixed JSON files

### Agent 5C: Taxonomy Update Agent
**Focus**: Regenerate taxonomy master lists
**Working Directory**: `TAXONOMY/TAX-001/` through `TAX-004/`
**Output**: Updated taxonomy files

### Agent 5D: Cross-Reference Validation Agent
**Focus**: Verify entity relationships
**Working Directory**: Entire ENTITIES system
**Output**: Cross-reference validation matrix

---

## 📋 Agent 5A: CSV Master List Sync

### Task Instructions

#### Update 10 Master CSV Lists

**Lists to Update**:
1. `LIBRARIES/Libraries_Master_List.csv` (78 entities → update with Phase 1 changes)
2. `LIBRARIES/LBS_003_Tools/Tools_Master_List.csv` (164 tools → remove 23 duplicates)
3. `PROMPTS/PROMPTS_Master_List.csv` (63 prompts → verify all cataloged)
4. `TASK_MANAGERS/Task_Templates_Master_List.csv` (50+ tasks → add DeepResearch-001)
5. `TASK_MANAGERS/TSM-002_Milestone_Templates/Milestone_Templates_Master_List.csv` (28 milestones)
6. `TASK_MANAGERS/TSM-004_Step_Templates/Step_Templates_Master_List.csv`
7. `TASK_MANAGERS/TSM-005_Checklist_Items/Checklist_Items_Master_List.csv`
8. `TASK_MANAGERS/TSM-006_Workflows/Workflows_Master_List.csv`
9. `TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv` (copy of #1)
10. `TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv` (copy of #2)

**For Each List**:
- Load current CSV
- Identify changes from Phases 1-4:
  - Phase 1B: 23 duplicate Tool/Task IDs removed/renumbered
  - Phase 3: RESEARCHES restructured
  - Phase 4: Deep Research task added
- Update counts, IDs, file paths
- Verify no duplicates
- Verify sequential IDs (or document intentional gaps)
- Regenerate CSV

**Output**: `Master_Lists_Sync_Report.md` showing before/after for each list

---

## 📋 Agent 5B: JSON Schema Validation

### Task Instructions

#### Scan All JSON Files

Scan entire ENTITIES system for `.json` files:
- Count total JSON files
- Validate JSON syntax (parse test)
- Identify invalid JSON (1 known in ANALYTICS/Projects)
- Categorize by entity type

**Output**: `JSON_Files_Inventory.csv`

#### Validate Against Schemas

For each JSON file, verify:
- Has required `entity_type` field
- Has required `entity_id` field
- ID format matches entity type (e.g., TOL-XXX for tools)
- Schema matches expected structure for entity type

**Output**: `JSON_Schema_Validation_Report.md`

#### Fix Invalid JSON

Fix the 1 known invalid JSON file + any others found:
- Attempt auto-fix (common issues: trailing commas, unescaped quotes)
- If auto-fix fails, flag for manual review
- Log all fixes

**Output**: `JSON_Fixes_Log.csv`

---

## 📋 Agent 5C: Taxonomy Update

### Task Instructions

#### Update TAX-001_Libraries

Regenerate:
- `Libraries_Master_List.csv` (sync with Agent 5A)
- `Tools_Master_List.csv` (sync with Agent 5A)
- Update counts, add any new library entities

#### Update TAX-002_Task_Managers

Regenerate:
- `Taxonomy_Master_List.csv`
- Add Deep Research task (Phase 4)
- Update video queue references (Phase 3)

#### Update TAX-003_Video_Processing

Update with Phase 3 video queue system:
- Add video queue workflow taxonomy
- Update video research categories

#### Update TAX-004_Entity_Integration

Update with all Phase 1-4 changes:
- New entity relationships
- Integration points documented

**Output**: Updated taxonomy files + `Taxonomy_Update_Report.md`

---

## 📋 Agent 5D: Cross-Reference Validation

### Task Instructions

#### Verify Key Relationships

**Validate**:
- Tasks → Prompts (all task prompt_references exist)
- Employees → Departments (all employees assigned to valid departments)
- Prospects → Industries (all industry_ids valid)
- Tools → Departments (all tools categorized)
- Research Topics → Taxonomy (all topics registered)

**Output**: `Cross_Reference_Validation_Matrix.csv`

Format:
```csv
Entity_Type_A,Entity_ID_A,Relationship,Entity_Type_B,Entity_ID_B,Status,Error_Message
Task,TASK-001,references,Prompt,PRM-042,VALID,
Task,TASK-015,references,Prompt,PRM-999,BROKEN,Prompt PRM-999 does not exist
```

#### Generate Orphan Report

Identify orphaned entities:
- Files not referenced in any master list
- Entities referenced but files missing
- Broken cross-references

**Output**: `Orphaned_Entities_Report.md`

---

## 🚦 Phase 5 Exit Criteria

**MUST COMPLETE:**
- [ ] All 10 master CSVs updated and synchronized
- [ ] All JSON files validated (invalid count: 1 → 0)
- [ ] Taxonomy TAX-001 through TAX-004 updated
- [ ] Cross-reference validation complete (broken links documented)

**METRICS UPDATED:**
- [ ] Master CSV count: 10 (unchanged)
- [ ] Master CSV accuracy: ~Unknown → 100% synced
- [ ] Invalid JSON files: 1 → 0
- [ ] Broken cross-references: Unknown → Documented

---

**END OF PHASE 5 CONTEXT**
