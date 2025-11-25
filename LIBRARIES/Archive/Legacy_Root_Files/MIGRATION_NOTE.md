# Migration Note: Legacy Root Files

**Migration Date:** 2025-11-17
**Reason:** Architectural consolidation - Actions and Objects moved to Responsibilities ecosystem

---

## Files in This Directory

This directory contains legacy root-level library files that have been replaced by the organized Responsibilities ecosystem structure.

### Files Archived

1. **actions.json**
   - Legacy format: Simple array with Actions/Processes/Results
   - Replaced by: `LIBRARIES/LBS_001_Actions/Master/actions_master.json`
   - New location contains 429 actions in structured format

2. **objects.json**
   - Legacy format: Simple array with Objects/Object Types
   - Replaced by: `LIBRARIES/LBS_002_Objects/` (14 files)
   - New location contains 36+ objects organized by domain

3. **tools.json** (if present)
   - Legacy format: Simple tool listings
   - Replaced by: `LIBRARIES/LBS_003_LBS_003_Tools/` (75 tools across 13 categories)

---

## Why Were These Archived?

**Problem:**
- Duplicate data (root files vs organized structure)
- Format inconsistency (simple vs structured)
- Confusion about source of truth
- Difficult to maintain synchronization

**Solution:**
- Single source of truth: `LIBRARIES/Responsibilities/`
- Structured, organized format
- Clear navigation from root via README files
- Better integration with taxonomy framework

---

## New Locations

### For Actions:
**Current location:** `LIBRARIES/LBS_001_Actions/`

Files available:
- `Actions_Master.json` - Complete catalog (429 actions)
- `Actions_Master_Command_Verbs.json`
- `Actions_Master_Process_Verbs.json`
- `Actions_Master_Result_Verbs.json`
- `Video_Generation_Actions.json`

**Navigation:** See `LIBRARIES/ACTIONS_README.md`

### For Objects:
**Current location:** `LIBRARIES/LBS_002_Objects/`

Files available (14 files):
- `object_types.json`
- `Agentic_Engineering_Objects.json`
- `AI_Automation_Objects.json`
- `Design_Deliverables.json`
- And 10 more domain-specific collections

**Navigation:** See `LIBRARIES/OBJECTS_README.md`

---

## Migration Impact

**Files Updated:** 128+ files with path references
**Entities Updated:** LIBRARIES, TASK_MANAGERS/PROMPTS
**Documentation Updated:** All README files and PROMPTS_INDEX.json

---

## Rollback Instructions

If you need to restore these files to root:

```bash
cp "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\actions.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\actions.json"

cp "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\objects.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\objects.json"
```

**Note:** This is not recommended as it will create duplicate/conflicting data sources.

---

## Questions?

Refer to:
- [MIGRATION_PLAN_Actions_Objects.md](../../MIGRATION_PLAN_Actions_Objects.md)
- [Responsibilities README](../Responsibilities/README.md)
- [LIBRARIES README](../README.md)

---

**Archived:** 2025-11-17
**Status:** Safe to keep for historical reference
**Can be deleted:** After 6 months if no issues reported
