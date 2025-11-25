# Daily Reports v2.0 Upgrade - Implementation Plan

**Project:** Department Daily Reports Entity Integration
**Version:** 2.0
**Date:** 2025-11-19
**Status:** In Progress

---

## Objective

Upgrade all 11 department daily report prompts to integrate with TASK_MANAGERS entity hierarchy (PRT→MLT→TST→STP), enabling project/milestone tracking, task sequence clustering, and cross-department coordination visibility.

---

## Scope

### In Scope:
- Create standardized report output schema v2.0 (14 sections)
- Create entity mapping guide
- Update PMT-070 (Entity Identification) with enhanced mapping logic
- Update PMT-032 (Daily Report Collection) with entity validation
- Update all 11 department prompts (PMT-033 through PMT-043)
- Update supporting documentation

### Out of Scope (Future Phase):
- Executive report creation (PMT-074)
- Automated entity extraction from daily files
- Real-time project dashboard
- Cross-department dependency notifications

---

## Files to Create

1. ✅ **REPORT_OUTPUT_SCHEMA_v2.md** - Standardized 14-section schema specification (COMPLETE)
2. 🔄 **ENTITY_MAPPING_GUIDE.md** - Activity → entity mapping instructions (IN PROGRESS)
3. **IMPLEMENTATION_PLAN_v2_Upgrade.md** - This document

---

## Files to Modify

### Phase 1: Enhanced Entity Mapping
- [ ] **PMT-070_Entity_Identification_v1.md** - Add activity → TST → MLT → PRT mapping logic

### Phase 2: Report Collection Enhancement
- [ ] **PMT-032_Daily_Report_Collection.md** - Add entity data loading and validation

### Phase 3: Department Prompts (11 files)
- [ ] **PMT-033_AI_Daily_Report.md**
- [ ] **PMT-034_Content_Daily_Report.md**
- [ ] **PMT-035_Design_Daily_Report.md**
- [ ] **PMT-036_Dev_Daily_Report.md**
- [ ] **PMT-037_Finance_Daily_Report.md**
- [ ] **PMT-038_HR_Daily_Report.md**
- [ ] **PMT-039_LG_Daily_Report.md**
- [ ] **PMT-040_Marketing_Daily_Report.md**
- [ ] **PMT-041_Sales_Daily_Report.md**
- [ ] **PMT-042_SMM_Daily_Report.md**
- [ ] **PMT-043_Video_Daily_Report.md**

### Phase 4: Documentation
- [ ] **README.md** - Document v2 schema and entity integration
- [ ] **PMT_Master_List.csv** - Update prompt descriptions to note "v2.0"
- [ ] **Prompts_Index.json** - Update metadata
- [ ] **Constructor/TEMPLATE_Enhanced_Department_Prompt.md** - Update template

---

## Implementation Sequence

### Step 1: Foundation ✅
- [x] Create REPORT_OUTPUT_SCHEMA_v2.md (COMPLETE)
- [ ] Create ENTITY_MAPPING_GUIDE.md (IN PROGRESS)
- [x] Create IMPLEMENTATION_PLAN_v2_Upgrade.md (COMPLETE)

### Step 2: Enhanced Entity Mapping
**File:** PMT-070_Entity_Identification_v1.md

**Changes:**
- Add activity description → Task Template (TST-###) mapping logic
- Add keyword matching algorithm
- Add task → milestone rollup
- Add milestone → project rollup
- Include entity validation against TASK_MANAGERS CSVs
- Add examples from all 11 departments

**Estimated Time:** 2 hours

### Step 3: Report Collection Enhancement
**File:** PMT-032_Daily_Report_Collection.md

**Changes:**
- Add step to load TASK_MANAGERS entity data (Projects_Master.csv, Milestones_Master.csv, Tasks_Master.csv)
- Add entity validation step (verify all referenced entities exist)
- Update report naming to reflect v2.0
- Add instruction to use PMT-070 for entity mapping
- Prepare for future executive report aggregation

**Estimated Time:** 1.5 hours

### Step 4: Update Department Prompts (Parallel)
**Files:** PMT-033 through PMT-043 (11 files)

**Common Changes (All Departments):**
1. Add "Entity Integration Requirements" section
2. Update output format to 14-section schema v2.0
3. Add Section 2: Project Contributions (NEW)
4. Add Section 3: Milestone Progress (NEW)
5. Add Section 5: Cross-Department Coordination (NEW)
6. Enhance Section 4 with entity mapping instructions
7. Enhance Section 7 with entity activity summary
8. Enhance Section 9 with project impact table
9. Enhance Section 13 with entity completion tracking
10. Enhance Section 14 with entity references summary
11. Update examples with entity references
12. Add entity validation instructions

**Department-Specific Adaptations:**
- Maintain existing specialized content in Section 6
- Update examples to reflect department's typical projects
- Include department-relevant entity IDs

**Estimated Time:** 30 minutes per prompt × 11 = 5.5 hours

### Step 5: Documentation Updates
**Files:** README.md, PMT_Master_List.csv, Prompts_Index.json, Constructor template

**Changes:**
- Document v2.0 schema in README
- Add entity integration guidelines
- Update all 11 prompt descriptions in CSV (note "v2.0 with entity integration")
- Update JSON metadata
- Update Constructor template with v2.0 structure

**Estimated Time:** 1.5 hours

---

## Key Changes in v2.0

### New Sections (3 additions):
1. **Section 2: Project Contributions** - Shows department's work on PRT-### with progress tracking
2. **Section 3: Milestone Progress** - Tracks MLT-### completion with task sequences
3. **Section 5: Cross-Department Coordination** - Handoff tracking tables

### Enhanced Sections (5 upgrades):
1. **Section 4:** Activities mapped to TST → MLT → PRT hierarchy
2. **Section 7:** Entity activity summary added
3. **Section 9:** Project impact table added
4. **Section 13:** Entity completion tracking added
5. **Section 14:** Entity references summary added

### Total Structure:
- **v1.0:** 12 sections, activity-based
- **v2.0:** 14 sections, entity-integrated

---

## Entity Integration Approach

### Mapping Logic:

**Step 1: Activity → Task (TST-###)**
- Analyze activity description
- Extract keywords (action + object)
- Match to Task Templates in Tasks_Master.csv
- Use PMT-070 enhanced mapping algorithm

**Step 2: Task → Milestone (MLT-###)**
- Look up TST-### in Tasks_Master.csv
- Find parent milestone_template_id
- Retrieve milestone details from Milestones_Master.csv

**Step 3: Milestone → Project (PRT-###)**
- Look up MLT-### in Milestones_Master.csv
- Find parent project_template_id
- Retrieve project details from Projects_Master.csv

**Step 4: Validation**
- Verify all entity IDs exist in master CSVs
- Check entity status (Active/Paused/Blocked)
- Confirm department alignment
- Flag any invalid references

---

## Data Sources

### Primary:
- `ENTITIES/TASK_MANAGERS/DATA/Projects_Master.csv`
- `ENTITIES/TASK_MANAGERS/DATA/Milestones_Master.csv`
- `ENTITIES/TASK_MANAGERS/DATA/Tasks_Master.csv`

### Secondary:
- Department prompt logs (for activity extraction)
- Employee daily files (daily.md, task.md)
- Call transcripts (if applicable)

### Output:
- `Nov25/{Department} Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

---

## Success Criteria

### Deliverables:
- [ ] REPORT_OUTPUT_SCHEMA_v2.md created with complete 14-section specification
- [ ] ENTITY_MAPPING_GUIDE.md created with mapping instructions and examples
- [ ] PMT-070 updated with enhanced entity mapping logic
- [ ] PMT-032 updated with entity validation
- [ ] All 11 department prompts updated to v2.0 schema
- [ ] Documentation updated (README, CSV, JSON, Constructor)
- [ ] Test report generated successfully with entity references

### Quality Checks:
- [ ] All entity references valid (exist in TASK_MANAGERS CSVs)
- [ ] Activity → TST → MLT → PRT hierarchy correct
- [ ] Cross-department dependencies identified
- [ ] Project/milestone completion percentages accurate
- [ ] All 14 sections present in output
- [ ] Entity activity summary populated
- [ ] Markdown formatting clean and consistent

### Validation:
- [ ] Generate test report from each department prompt
- [ ] Verify entity IDs resolve correctly
- [ ] Check project/milestone progress tracking works
- [ ] Confirm cross-department handoff tables populate
- [ ] Validate metrics and statistics calculate correctly

---

## Timeline

**Total Estimated Time:** 10.5 hours

**Phase Breakdown:**
- Phase 1 (Foundation): 0.5 hours (COMPLETE except ENTITY_MAPPING_GUIDE.md - 30 min remaining)
- Phase 2 (PMT-070): 2 hours
- Phase 3 (PMT-032): 1.5 hours
- Phase 4 (11 Department Prompts): 5.5 hours
- Phase 5 (Documentation): 1.5 hours

**Recommended Schedule:**
- **Day 1 (Nov 19):** Complete Phase 1, start Phase 2 (3 hours)
- **Day 2 (Nov 20):** Complete Phase 2-3, start Phase 4 (4 hours)
- **Day 3 (Nov 21):** Complete Phase 4-5 (4 hours)

---

## Risk Mitigation

### Risk 1: Entity Mapping Inaccuracy
**Mitigation:**
- Use keyword matching algorithm with confidence scores
- Flag low-confidence matches for manual review
- Maintain "Operational/Maintenance" category for non-project activities

### Risk 2: Missing Entity Data
**Mitigation:**
- Validate entity IDs against master CSVs before including
- Provide clear error messages if entity not found
- Support manual entity specification in prompts

### Risk 3: Cross-Department Coordination Tracking
**Mitigation:**
- Use structured tables for handoff tracking
- Include status indicators (✅ ⏳ 🔄)
- Allow "None" or "N/A" for departments with no cross-dept work

### Risk 4: Department-Specific Variations
**Mitigation:**
- Maintain flexibility in Section 6 (Department-Specific)
- Allow departments to customize metrics in Section 7
- Provide template but don't enforce rigidity

---

## Testing Plan

### Test Case 1: AI Department Report
**Input:** AI department activities from Nov 19
**Expected Output:**
- Activities mapped to TST-055, TST-058, etc.
- Milestones: MLT-001, MLT-002
- Projects: PRT-001, PRT-007
- Cross-dept: Handoffs to HRM, DEV

### Test Case 2: Multi-Department Project
**Input:** HR department work on PRT-003 (HR Automation)
**Expected Output:**
- Project section shows "Support" role
- Cross-dept dependencies: waiting on DEV, providing to AID
- Handoff tables populated correctly

### Test Case 3: Operational Activities
**Input:** Finance department routine operations (invoices, reconciliation)
**Expected Output:**
- Activities marked as "Operational/Maintenance"
- Or mapped to ongoing operational projects if applicable
- No invalid entity references

---

## Rollback Plan

**If v2.0 has critical issues:**
1. Revert all 11 department prompts to v1.0 (backup copies in Git)
2. Keep REPORT_OUTPUT_SCHEMA_v2.md and ENTITY_MAPPING_GUIDE.md as reference docs
3. Iterate on fixes offline
4. Re-deploy when issues resolved

**Backup Strategy:**
- Git commit before any changes
- Keep v1.0 prompts in separate branch
- Document all changes in commit messages

---

## Future Enhancements (Post v2.0)

### Phase 6 (Future): Executive Report
- Create PMT-074 (Executive Daily Progress Report)
- Aggregate all 11 department reports
- Generate cross-department project dashboard
- Track organizational velocity and capacity

### Phase 7 (Future): Automation
- Automated entity extraction from daily files
- Real-time project progress updates
- Dependency blocker notifications
- Predictive milestone completion dates

### Phase 8 (Future): Visualization
- Project timeline Gantt charts
- Milestone completion dashboard
- Cross-department dependency graph
- Resource utilization heatmap

---

## Progress Tracking

### Current Status: Phase 1 (Foundation)
- [x] REPORT_OUTPUT_SCHEMA_v2.md ✅
- [ ] ENTITY_MAPPING_GUIDE.md (IN PROGRESS - 50% complete)
- [x] IMPLEMENTATION_PLAN_v2_Upgrade.md ✅

### Next Steps:
1. Complete ENTITY_MAPPING_GUIDE.md
2. Begin PMT-070 enhancement
3. Update PMT-032 with entity validation
4. Start department prompt updates (parallel)

---

## Notes

**Design Decisions:**
- Keep Section 6 flexible for department-specific content
- Use tables for clarity in cross-dept coordination
- Include examples from all departments in mapping guide
- Validate entities against master CSVs before output
- Support both project and operational activities

**Key Principles:**
- Maintain backward compatibility where possible
- Don't break existing workflows
- Provide clear error messages
- Make entity references optional but encouraged
- Focus on value: better visibility into project progress

---

**Document Status:** Active
**Maintained By:** AI & Automation Department
**Last Updated:** 2025-11-19
**Next Review:** Upon Phase 5 completion