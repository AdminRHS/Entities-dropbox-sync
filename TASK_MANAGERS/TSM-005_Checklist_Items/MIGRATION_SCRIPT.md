# Deliverables to Checklist Items Migration Script

**Created:** November 25, 2025  
**Purpose:** Extract deliverables from Project Templates and Project Instances, convert to Checklist Items

---

## Migration Process

1. **Scan all Project Templates** for `deliverables` arrays in milestones
2. **Scan all Project Instances** for `deliverables` arrays
3. **Create Checklist Item files** for each deliverable
4. **Generate Checklist-Item-003.json** with all Checklist Items
5. **Update Project Templates** to reference checklist_items instead of deliverables

---

## Files to Process

### Project Templates:
- `Project-Template-003.json` (4 milestones, 24 deliverables)
- `Project-Template-001.json` (3 milestones, 12 deliverables)
- `Project-Template-002.json` (6 milestones, 12 deliverables)
- `Project-Template-004.json` (5 milestones, 10 deliverables)
- `Project-Template-005.json` (5 milestones, 10 deliverables)

### Project Instances:
- `PROJ-LIB-001_Responsibilities_Ecosystem/project_instance.json` (8 deliverables)

**Total Estimated:** ~76 deliverables to migrate

---

## Checklist Item ID Format

`CHK-{ITEM_NUMBER}` (sequential number, zero-padded to 3 digits)

Examples:
- `CHK-001` (First Checklist Item)
- `CHK-044` (44th Checklist Item)
- `CHK-098` (98th Checklist Item)

**Note:** The ID format was simplified from `CHK-{PROJECT_ID}-{MILESTONE_ID}-{ITEM_NUMBER}` to `CHK-{ITEM_NUMBER}` on November 25, 2025 for simplicity and consistency.

---

## Migration Status

- [x] Extract deliverables from all Project Templates
- [x] Create Checklist Item JSON files
- [x] Generate Checklist-Item-003.json
- [x] Update Project Templates to reference checklist_items
- [x] Validate all references
- [x] Create migration report

---

**Status:** ✅ Complete

**Completed:** November 25, 2025

**Summary:**
- 98 Checklist Items created from deliverables
- 5 Project Templates updated with checklist_items references
- 1 project instance updated
- All 98 references validated successfully
- Deliverables arrays kept for backward compatibility

