# Daily Reports v2.1 - Implementation Plan

**Version:** 2.1 | **Date:** 2025-11-19 | **Status:** In Progress

---

## Objective

Upgrade 11 department daily reports to v2.1 with TASK_MANAGERS entity integration using token-efficient format.

---

## Changes from v2.0

- ✅ Token-efficient format: `{ISO-###}_{Name}`
- ✅ Corrected STT (was STP)
- ✅ Updated CSV paths
- ✅ Removed deprecated MKT

---

## Files Created

1. ✅ REPORT_OUTPUT_SCHEMA_v2.1.md
2. ✅ ENTITY_MAPPING_GUIDE_v2.1.md
3. ✅ IMPLEMENTATION_PLAN_v2.1.md (this file)

---

## Files to Modify

### Phase 2: Enhanced Entity Mapping
- [ ] PMT-070_Entity_Identification_v1.md

### Phase 3: Report Collection
- [ ] PMT-032_Daily_Report_Collection.md

### Phase 4: Department Prompts (11 files)
- [ ] PMT-033_AI_Daily_Report.md
- [ ] PMT-034_Content_Daily_Report.md
- [ ] PMT-035_Design_Daily_Report.md
- [ ] PMT-036_Dev_Daily_Report.md
- [ ] PMT-037_Finance_Daily_Report.md
- [ ] PMT-038_HR_Daily_Report.md
- [ ] PMT-039_LG_Daily_Report.md
- [ ] PMT-040_Marketing_Daily_Report.md
- [ ] PMT-041_Sales_Daily_Report.md
- [ ] PMT-042_SMM_Daily_Report.md
- [ ] PMT-043_Video_Daily_Report.md

### Phase 5: Documentation
- [ ] README.md
- [ ] PMT_Master_List.csv
- [ ] Prompts_Index.json
- [ ] Constructor/TEMPLATE_Enhanced_Department_Prompt.md

---

## Implementation Sequence

### Phase 1: Foundation ✅ COMPLETE
- [x] REPORT_OUTPUT_SCHEMA_v2.1.md
- [x] ENTITY_MAPPING_GUIDE_v2.1.md
- [x] IMPLEMENTATION_PLAN_v2.1.md

### Phase 2: Enhanced Entity Mapping (2 hours)
**File:** PMT-070_Entity_Identification_v1.md

**Changes:**
- Use token-efficient format: `TST-###_{Name}`
- Update CSV paths
- Use STT (not STP)
- Add keyword matching algorithm
- Task → milestone → project rollup
- Examples from all 11 departments

### Phase 3: Report Collection (1.5 hours)
**File:** PMT-032_Daily_Report_Collection.md

**Changes:**
- Load TASK_MANAGERS CSVs (correct paths)
- Add entity validation
- Use token-efficient format
- Invoke PMT-070 for mapping
- Prepare for executive report aggregation

### Phase 4: Department Prompts (5.5 hours)
**Common Changes (All 11):**
1. Add "Entity Integration Requirements"
2. Update to 14-section schema v2.1
3. Section 2: Project Contributions (NEW)
4. Section 3: Milestone Progress (NEW)
5. Section 5: Cross-Department Coordination (NEW)
6. Section 4: Entity mapping with token-efficient format
7. Section 7: Entity activity summary
8. Section 9: Project impact table
9. Section 13: Entity completion tracking
10. Section 14: Entity references summary
11. Update all examples to token-efficient format
12. Use STT (not STP)

**Department-Specific:**
- Maintain specialized content in Section 6
- Update examples for dept's projects
- Use dept-relevant entity IDs

**Time:** 30 min/prompt × 11 = 5.5 hours

### Phase 5: Documentation (1.5 hours)
- Update README with v2.1 schema
- Add entity integration guidelines
- Update prompt descriptions in CSV (v2.1)
- Update JSON metadata
- Update Constructor template

---

## Token-Efficient Format

### Pattern
`{ISO-###}_{Name_With_Underscores}`

### Examples
```
PRT-001_AI_Tutorial_Research
MLT-002_Data_Inventory
TST-055_Process_Department_Task_Files
STT-155_Conduct_Client_Brand_Discovery
```

### Benefits
- 60% token reduction vs verbose
- Faster processing
- Cleaner reports
- Easier parsing

---

## CSV Paths (Correct)

```
ENTITIES/TASK_MANAGERS/Project_Templates/Project_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Step_Templates/Taxonomy/Step_Templates_Master_List.csv
```

---

## Department Codes (Active)

AID | HRM | DEV | LGN | DGN | VID | SLS | SMM | FNC | CNT

**Removed:** MKT (deprecated)

---

## Validation Checklist

### Per Department Prompt:
- [ ] All 14 sections present
- [ ] Token-efficient format used
- [ ] STT (not STP)
- [ ] CSV paths correct
- [ ] Project Contributions examples
- [ ] Milestone Progress examples
- [ ] Cross-Department Coordination
- [ ] Entity mapping shows hierarchy
- [ ] Department content preserved
- [ ] MKT removed

---

## Timeline

**Total:** 10.5 hours

**Breakdown:**
- Phase 1: ✅ Complete
- Phase 2: 2 hours
- Phase 3: 1.5 hours
- Phase 4: 5.5 hours
- Phase 5: 1.5 hours

**Schedule:**
- Day 1 (Nov 19): ✅ Phase 1 complete
- Day 2 (Nov 20): Phase 2-3 (3.5 hours)
- Day 3 (Nov 21): Phase 4-5 (7 hours)

---

## Success Criteria

- [ ] All 11 prompts updated to v2.1
- [ ] Token-efficient format throughout
- [ ] STT code correct
- [ ] CSV paths correct
- [ ] Entity mappings valid
- [ ] MKT removed
- [ ] Test reports generated successfully
- [ ] Documentation updated

---

## Progress Tracking

### Current: Phase 1 ✅ Complete
- [x] REPORT_OUTPUT_SCHEMA_v2.1.md
- [x] ENTITY_MAPPING_GUIDE_v2.1.md
- [x] IMPLEMENTATION_PLAN_v2.1.md

### Next: Phase 2 (PMT-070)

---

**Status:** Ready for Phase 2
**Maintained By:** AI & Automation
**Last Updated:** 2025-11-19