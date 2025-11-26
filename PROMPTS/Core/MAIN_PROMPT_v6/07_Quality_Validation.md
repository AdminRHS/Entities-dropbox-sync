# 7. QUALITY VALIDATION

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## ENTITY CHECKLIST

**Before creating new entity:**

- [ ] **ID Format:** XXX-### (TST-042, not TSK-42 or TST-42)
- [ ] **Sequential:** Check master CSV for highest ID, use next (+1)
- [ ] **No duplicates:** ID doesn't exist in master CSV
- [ ] **References valid:** All linked entities exist (MLT-###, TOL-###, GDS-###)
- [ ] **Metadata complete:** Name, Description, Department filled

**Common Fixes:**

| Error | Fix |
|-------|-----|
| Duplicate ID | Use next available: max+1 |
| Wrong format (TSK) | Use TST for tasks, STT for steps |
| Missing reference | Link to TOL-### (tools) or GDS-### (guides) |

---

## VALIDATION WORKFLOW

1. Extract entities from daily reports (Nov25/, Finance 2025/)
2. Check against master CSVs in TSM-00X_[Category]/
3. Validate references: All PRT/MLT/TST/STT/TOL/GDS exist
4. Use [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011) for classification decisions
5. Update master CSVs with new entities
