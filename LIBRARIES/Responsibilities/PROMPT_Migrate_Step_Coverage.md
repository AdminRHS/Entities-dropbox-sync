# Prompt: Migrate and Merge Step-Level Responsibility Coverage into Task Templates

## Objective
Increase step-level responsibility coverage from **83.3% (309/371 steps)** to **95%+** by migrating step-level responsibility mappings from Step_Templates and merging them into the corresponding Task_Templates.

---

## Current State Analysis

### Step Coverage Statistics
- **Total Steps:** 371 steps across all task templates
- **Steps with Responsibility ID:** 309 steps (83.3%)
- **Steps Missing Responsibility ID:** 62 steps (16.7%)
- **Target Coverage:** 95%+ (353+ steps)

### Data Sources
1. **Task Templates:** Located in `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\`
   - 59 task template JSON files
   - Contains `checklist` array with steps
   - Some steps have `responsibility_id`, many don't

2. **Step Templates:** Located in `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Step_Templates\`
   - 62 step template JSON files
   - Contains individual step definitions with actions, objects, and potentially responsibility IDs
   - May contain mappings that can enhance task template steps

3. **Migration Log:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Responsibilities\task_manager_migration_log.json`
   - Contains existing task-level and step-level responsibility mappings
   - Shows which steps have been mapped to responsibility IDs

---

## Migration Strategy

### Phase 1: Discovery & Analysis
1. **Scan all Task Templates:**
   - Identify steps missing `responsibility_id` in the `checklist` array
   - Extract step descriptions, actions, and objects
   - Categorize by department and task type

2. **Scan all Step Templates:**
   - Extract step definitions with actions and objects
   - Identify any existing responsibility_id mappings
   - Build lookup index: `{action + object} → responsibility_id`

3. **Load Responsibilities Master:**
   - Load `LIBRARIES/Responsibilities/Core/responsibilities_master.json`
   - Load `LIBRARIES/Responsibilities/Core/phrase_matching_index.json`
   - Load `LIBRARIES/Responsibilities/Core/action_variants_map.json`
   - Load `LIBRARIES/Responsibilities/Core/object_variants_map.json`
   - Build comprehensive lookup system for matching steps to responsibilities

### Phase 2: Mapping & Matching
1. **Match Steps to Responsibilities:**
   - For each step missing `responsibility_id`:
     - Extract action verb (e.g., "Configure", "Setup", "Test")
     - Extract object/target (e.g., "API", "Database", "Workflow")
     - Use phrase_matching_index to find matching responsibility
     - Apply action_variants and object_variants for fuzzy matching

2. **Validate Mappings:**
   - Ensure mapped responsibility exists in responsibilities_master.json
   - Verify responsibility belongs to correct department
   - Check responsibility action-object combination makes sense in context

3. **Handle Ambiguous Cases:**
   - If multiple responsibilities match: Choose most specific/contextual
   - If no exact match: Use closest variant from action_variants_map
   - If still no match: Flag for manual review with suggested alternatives

### Phase 3: Migration & Merge
1. **Update Task Templates:**
   - For each task template JSON file:
     - Iterate through `checklist` array
     - Add `responsibility_id` field to steps missing it
     - Preserve all existing fields (action, description, expected_output, etc.)
     - Maintain JSON structure and formatting

2. **Create Backup:**
   - Before modification, create timestamped backup of Task_Templates directory
   - Store in: `TASK_MANAGERS/Task_Templates_Backup_2025-11-17/`

3. **Write Updated Files:**
   - Write modified task templates back to original location
   - Ensure UTF-8 encoding (no BOM)
   - Validate JSON structure after writing

### Phase 4: Validation & Reporting
1. **Re-run Validation:**
   - Scan all updated task templates
   - Count steps with responsibility_id
   - Calculate new coverage percentage
   - Identify any remaining unmapped steps

2. **Generate Migration Report:**
   - **Statistics:**
     - Steps before: 309 mapped, 62 unmapped (83.3%)
     - Steps after: X mapped, Y unmapped (Z%)
     - Improvement: +N steps mapped (+M% coverage)
   - **Department Breakdown:**
     - Coverage by department (AI, LG, DEV, HR, OPS, etc.)
   - **Unmapped Steps:**
     - List of steps that couldn't be automatically mapped
     - Suggested manual actions

3. **Update Migration Log:**
   - Append new mappings to task_manager_migration_log.json
   - Add metadata: migration_date, coverage_before, coverage_after
   - Include list of updated task template files

---

## Expected Deliverables

### Scripts
1. **migrate_step_coverage.py**
   - Main migration script
   - Functions:
     - `load_task_templates()` - Load all task templates
     - `load_step_templates()` - Load all step templates
     - `load_responsibilities()` - Load responsibilities ecosystem
     - `match_step_to_responsibility(step_text, action, object)` - Fuzzy matching logic
     - `update_task_template(template, mappings)` - Apply mappings to template
     - `validate_coverage()` - Calculate coverage statistics
     - `generate_report()` - Create migration report

2. **validate_step_coverage.py**
   - Validation script
   - Functions:
     - `scan_all_steps()` - Count total and mapped steps
     - `validate_responsibility_ids()` - Verify all IDs exist in master
     - `generate_coverage_report()` - Create detailed coverage analysis

### Reports
1. **step_migration_report.json**
   ```json
   {
     "migration_date": "2025-11-17",
     "coverage_before": {"total": 371, "mapped": 309, "percentage": 83.3},
     "coverage_after": {"total": 371, "mapped": 353, "percentage": 95.1},
     "improvements": {
       "steps_newly_mapped": 44,
       "coverage_increase": 11.8
     },
     "by_department": {
       "AI": {"total": 120, "mapped": 115, "percentage": 95.8},
       "LG": {"total": 95, "mapped": 92, "percentage": 96.8},
       "DEV": {"total": 78, "mapped": 74, "percentage": 94.9},
       "HR": {"total": 28, "mapped": 27, "percentage": 96.4},
       "OPS": {"total": 32, "mapped": 30, "percentage": 93.8},
       "MKT": {"total": 18, "mapped": 15, "percentage": 83.3}
     },
     "unmapped_steps": [
       {
         "task_template": "TEMPLATE-TASK-XYZ.json",
         "step_number": 5,
         "step_description": "Review and approve final deliverables",
         "suggested_responsibility": "RESP-OPS-001",
         "confidence": "medium"
       }
     ],
     "files_updated": ["TEMPLATE-TASK-001.json", "TEMPLATE-TASK-002.json", ...]
   }
   ```

2. **step_coverage_comparison.md**
   - Before/after visualization
   - Department-by-department breakdown
   - Recommendations for remaining unmapped steps

### Updated Files
- All task template JSON files with improved step coverage
- Updated task_manager_migration_log.json
- New validation_report.json with post-migration statistics

---

## Implementation Guidelines

### Matching Algorithm Priority
1. **Exact Match:**
   - `{action} + {object}` exactly matches a responsibility in phrase_matching_index
   - Example: "configure" + "api" → RESP-DEV-007

2. **Variant Match:**
   - Use action_variants_map to expand action synonyms
   - Example: "setup" → ["configure", "initialize", "establish"]
   - Try all variants against phrase_matching_index

3. **Object Variant Match:**
   - Use object_variants_map to expand object synonyms
   - Example: "database" → ["db", "data store", "database"]

4. **Department Context Match:**
   - If task is in AI_Tasks directory, prefer RESP-AI-* responsibilities
   - If task has `department: "LG"`, prefer RESP-LG-* responsibilities

5. **Fallback to Generic:**
   - If no specific match found, use generic responsibilities
   - Example: "execute" + any object → RESP-OPS-009 (execute operations)

### JSON Structure Preservation
When updating task templates, preserve:
- All existing fields (`action`, `description`, `expected_output`, `tools`, etc.)
- Array order in `checklist`
- Indentation (2 spaces)
- Field order within objects
- Unicode characters (use `ensure_ascii=False`)

### Error Handling
- **File Lock Errors:** Retry up to 3 times with 2-second delays
- **JSON Parse Errors:** Log error, skip file, continue with others
- **Missing Responsibility IDs:** Log warning, use best-guess mapping
- **Permission Errors:** Report to user, suggest manual intervention

---

## Success Criteria

### Quantitative
- [x] Step coverage increases from 83.3% to 95%+ (target: 353+ steps mapped)
- [x] All 59 task templates scanned and updated
- [x] Zero JSON validation errors in updated files
- [x] 100% of mappings point to valid responsibility IDs

### Qualitative
- [x] Mappings are contextually appropriate (action-object pairs make sense)
- [x] Department-specific responsibilities used when applicable
- [x] No existing mappings overwritten or lost
- [x] Migration process fully documented and reproducible

---

## Example Usage

```python
# Run migration
python migrate_step_coverage.py

# Expected output:
# ==============================================================
# Migrating Step-Level Responsibility Coverage
# ==============================================================
#
# [1] Loading resources...
#   - Task Templates: 59 files loaded
#   - Step Templates: 62 files loaded
#   - Responsibilities: 220 loaded from Core/
#
# [2] Analyzing current coverage...
#   - Total Steps: 371
#   - Mapped Steps: 309 (83.3%)
#   - Unmapped Steps: 62 (16.7%)
#
# [3] Matching unmapped steps to responsibilities...
#   - Exact matches: 38
#   - Variant matches: 18
#   - Context matches: 4
#   - Unmatched: 2
#
# [4] Updating task templates...
#   [OK] Updated: TEMPLATE-TASK-001.json (3 steps mapped)
#   [OK] Updated: TEMPLATE-TASK-015.json (2 steps mapped)
#   ...
#   [OK] Updated: TEMPLATE-TASK-RES-004.json (1 step mapped)
#
# [5] Validation...
#   - New Coverage: 367 / 371 (98.9%)
#   - Improvement: +58 steps (+15.6%)
#
# [6] Generating report...
#   - Report saved: step_migration_report.json
#   - Comparison saved: step_coverage_comparison.md
#
# ==============================================================
# Migration Complete!
# Coverage: 83.3% → 98.9% (+15.6%)
# ==============================================================
```

---

## Post-Migration Actions

1. **Review Unmapped Steps:**
   - Manually review steps that couldn't be automatically mapped
   - Determine if new responsibilities need to be created
   - Update responsibilities_master.json if needed

2. **Update Documentation:**
   - Update LIBRARIES/Responsibilities/README.md with new coverage stats
   - Document migration process in ECOSYSTEM_GUIDE.md
   - Add to project completion report

3. **Validate Task Execution:**
   - Test 5 random task templates end-to-end
   - Verify responsibility lookups work correctly
   - Ensure no breaking changes introduced

---

## Notes & Considerations

### Department-Specific Patterns
- **AI Tasks:** Often involve data processing, model training, analysis
  - Common patterns: "extract", "analyze", "train", "evaluate"
- **LG Tasks:** Often involve lead generation, enrichment, scraping
  - Common patterns: "scrape", "enrich", "export", "upload"
- **DEV Tasks:** Often involve building, configuring, deploying systems
  - Common patterns: "build", "configure", "deploy", "test"
- **HR Tasks:** Often involve recruiting, screening, onboarding
  - Common patterns: "screen", "interview", "onboard", "evaluate"

### Responsibilities Not to Overwrite
- Never overwrite existing `responsibility_id` fields
- Only add to steps where the field is missing or null
- Preserve manual mappings that may have been added

### Validation Checkpoints
1. Before migration: Generate baseline coverage report
2. After migration: Generate post-migration coverage report
3. Compare reports to verify improvement
4. Validate all JSON files parse correctly
5. Spot-check 10 random mappings for correctness

---

**End of Prompt**
