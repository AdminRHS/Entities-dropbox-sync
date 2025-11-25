# ⚠️ Research Assets - MIGRATED TO DEPARTMENTS

**Entity Type:** LIBRARIES (DEPRECATED)
**Library:** Researches (MIGRATED)
**New Location:** `TASK_MANAGERS/RESEARCHES/` (centralized research library)
**Migration Date:** November 25, 2025

---

## Migration Notice

This research library has been **migrated to TASK_MANAGERS/RESEARCHES/** with task manager integration on November 25, 2025.

**All research content is now located in:**
```
/Users/anastasia/Library/CloudStorage/Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/
```

---

## New Directory Structure

### AI Tutorial & Influencer Tracking
- **Location:** `TASK_MANAGERS/RESEARCHES/Influencer_Tracking/`
- **Files:** `Influencer_Database.json`, `YouTube_Channels.json`, `README.md`

### SMM Research
- **Location:** `TASK_MANAGERS/RESEARCHES/SMM/`
- **Files:** 11 social-media research sessions, taxonomy analyses, and integration reports

### Video Research & Transcriptions
- **Location:** `TASK_MANAGERS/RESEARCHES/Videos/`
- **Files:** `Video_001.md` through `Video_013.md`, discovery pipeline, queue tracker, and library mapping/gap analysis reports (under `Videos/Reports/`)

### Research ToDo Items
- **Location:** `TASK_MANAGERS/RESEARCHES/ToDo/`
- **Files:** AI Platforms, AI Video Tools, Development Tools, and Other Tools research queues

### Project Logs
- **Location:** `TASK_MANAGERS/RESEARCHES/PROJECT_LOG_2025-11-13.md`
- **Purpose:** Documentation of the original migration workflow and findings

---

## Migration Summary

**Total Files Migrated:** 20 files
**Total Size Migrated:** ~447 KB
**Migration Date:** January 16, 2025
**Backup Location:** `LIBRARIES/Researches_BACKUP_2025-11-16_020031/`

---

## Why This Migration?

### Previous Structure (LIBRARIES-based)
```
LIBRARIES/Researches/
├── AI_Tutorials/
├── SMM/
└── Videos/
```

### New Structure (Task Manager Integrated Research Hub)
```
TASK_MANAGERS/RESEARCHES/
├── README*.md / templates / indexes
├── Videos/                    (video findings + transcriptions)
├── SMM/                       (social media research)
├── Influencer_Tracking/       (creator databases)
├── ToDo/                      (research backlogs)
└── common_index.json, routing_matrix.json
```

**Benefits:**
1. **Single Source:** One location for every research artefact
2. **Simpler Automation:** Scripts can target a consistent path
3. **Easier Discovery:** No need to inspect individual department folders
4. **Future-Proof:** Additional research areas can be added as sibling folders
5. **Rollback Ready:** Backup retained under `LIBRARIES/Researches_BACKUP_*`

---

## Finding Your Research

### If You're Looking For...

**AI Tutorials & Influencer Tracking:**
→ `TASK_MANAGERS/RESEARCHES/Influencer_Tracking/`

**Social Media Research:**
→ `TASK_MANAGERS/RESEARCHES/SMM/`

**Video Transcriptions (Video_001-013):**
→ `TASK_MANAGERS/RESEARCHES/Videos/`

**Video Workflow Tools:**
→ `TASK_MANAGERS/RESEARCHES/Videos/` (Discovery Pipeline and Queue Tracker)

**Research ToDo Items:**
→ `TASK_MANAGERS/RESEARCHES/ToDo/`

**Session Logs:**
→ Check appropriate department's `sessions/` folder

---

## Rollback Procedure

If you need to restore the original LIBRARIES structure:

### Step 1: Locate Backup
```
C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches_BACKUP_2025-11-16_020031\
```

### Step 2: Restore (PowerShell)
```powershell
$backup = "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches_BACKUP_2025-11-16_020031"
$target = "C:\Users\Dell\Dropbox\Entities\LIBRARIES\Researches"

# Remove current directory
Remove-Item -Path $target -Recurse -Force

# Restore from backup
Copy-Item -Path $backup -Destination $target -Recurse
```

### Step 3: Verify
Check that all original files are restored.

**Note:** Rollback will not remove files from TASK_MANAGERS/RESEARCHES - you'll need to do that manually if desired.

---

## Related Documentation

- **Migration Plan:** `Research_Migration_Plan.md`
- **Phase 1 Verification:** `Research_Migration_Phase1_Verification_Report.md`
- **TASK_MANAGERS/RESEARCHES README:** `TASK_MANAGERS/RESEARCHES/README.md`
- **TASK_MANAGERS/RESEARCHES Index:** `TASK_MANAGERS/RESEARCHES/RESEARCH_INDEX.json`

---

## Migration Technical Details

**Migration Method:** Copy (not move) - originals preserved in backup
**Verification:** File count and size validation at each phase
**Phases Executed:**
1. ✅ Verification & Comparison
2. ✅ Backup Creation (36 files, 1186 KB)
3. ✅ AI Migration (3 files)
4. ✅ SMM Migration (11 files)
5. ✅ VIDEO Migration (4 files)
6. ✅ Root-level Migration (2 files)
7. ✅ Documentation Update
8. ✅ Validation

---

## Questions?

For questions about the migration or to request updates to this documentation, refer to:
- Migration reports in Dropbox root
- TASK_MANAGERS/RESEARCHES/README.md for structure details
- Individual department READMEs for specific research content

---

**Migration Completed:** January 16, 2025
**Migrated By:** Claude AI Assistant (Sonnet 4.5)
**Next Review:** After 2 weeks of use (January 30, 2025)

---

*This directory is now deprecated. All future research should be added to TASK_MANAGERS/RESEARCHES/ in the appropriate folder.*
