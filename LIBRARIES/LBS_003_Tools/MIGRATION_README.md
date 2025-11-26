# Tool ID Migration: Complete Guide

**Migration Date**: November 25, 2025
**Target**: Migrate from `TOOL-[CATEGORY]-###` to `TOL-###` format
**Status**: Ready for Execution

---

## 📋 Overview

This migration updates all tool files from the old `TOOL-[CATEGORY]-###` ID format to the new **Taxonomy `TOL-###`** format based on priority and mention frequency.

### What Changes
- **ID Format**: `TOOL-AI-029` → `TOL-002`
- **Filenames**: `Claude.json` → `TOL-002_Claude.json`
- **Directory Structure**: Flat structure (all files in root, subdirectories archived)
- **Duplicates**: Removed (keeping newest/most complete versions)

### What Stays the Same
- File content and metadata (preserved with `_migration` audit trail)
- Root-level social media files (remain in root)
- Archive directory structure (preserved)
- Backup (created automatically)

---

## 🚀 Quick Start

### Option 1: Complete Migration (All Phases)
```bash
cd "C:\Users\delir\Dropbox\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools"

# Dry run first (recommended)
python run_complete_migration.py --dry-run

# Review reports, then run actual migration
python run_complete_migration.py
```

### Option 2: Phase-by-Phase Execution
```bash
# Phase 1-3: Tool file migration
python migrate_tools_to_tol.py --dry-run
python migrate_tools_to_tol.py

# Phase 4: Cross-reference updates
python phase4_update_cross_references.py --dry-run
python phase4_update_cross_references.py

# Phase 5: Rollback (only if needed)
python phase5_rollback_migration.py --dry-run
python phase5_rollback_migration.py
```

---

## 📂 Migration Scripts

### 1. `migrate_tools_to_tol.py` (Phases 1-3)
**Main migration script** - Creates backup, maps IDs, migrates files, validates results

**Features**:
- ✅ Automatic backup with SHA256 verification
- ✅ Taxonomy CSV loading and validation
- ✅ Complete inventory and mapping generation
- ✅ Duplicate detection and resolution
- ✅ Pre-flight validation (6 checks)
- ✅ Dry run simulation
- ✅ Checkpoint-based execution (resumable)
- ✅ Post-migration validation (5 checks)
- ✅ Archive old files

**Usage**:
```bash
# Dry run (no changes)
python migrate_tools_to_tol.py --dry-run

# Actual migration
python migrate_tools_to_tol.py

# Skip backup (not recommended)
python migrate_tools_to_tol.py --skip-backup
```

**What It Does**:
1. Creates timestamped backup with ZIP archive
2. Loads taxonomy mapping from `Tools_Master_List.csv`
3. Inventories all current tool files
4. Creates master mapping table (current ID → new TOL-### ID)
5. Identifies duplicates and unmapped tools
6. Runs pre-flight validation
7. Simulates migration (dry run)
8. **[User Approval Required]**
9. Executes migration with checkpoints
10. Validates all migrated files
11. Archives old files to `_ARCHIVE/pre_migration_YYYY-MM-DD/`

### 2. `phase4_update_cross_references.py` (Phase 4)
**Cross-reference updater** - Updates all old IDs in dependent systems

**What It Does**:
- Scans `TASK_MANAGERS/`, `LIBRARIES/` directories
- Finds all JSON files with old `TOOL-[CAT]-###` IDs
- Replaces with new `TOL-###` IDs
- Validates JSON after updates
- Generates detailed update log

**Usage**:
```bash
# Dry run
python phase4_update_cross_references.py --dry-run

# Actual update
python phase4_update_cross_references.py
```

**Scanned Locations**:
- `TASK_MANAGERS/Task_Templates/**/*.json`
- `TASK_MANAGERS/Workflows/**/*.json`
- `TASK_MANAGERS/Step_Templates/**/*.json`
- `LIBRARIES/Responsibilities/**/*.json`
- `LIBRARIES/Skills/**/*.json`

### 3. `phase5_rollback_migration.py` (Phase 5)
**Rollback script** - Restores system to pre-migration state if issues found

**What It Does**:
- Finds latest backup (ZIP or directory)
- Verifies backup integrity
- Deletes all `TOL-*.json` files
- Restores from backup
- Verifies restoration
- Cleans up migration artifacts

**Usage**:
```bash
# Dry run
python phase5_rollback_migration.py --dry-run

# Actual rollback
python phase5_rollback_migration.py --reason "Reason for rollback"
```

**⚠ WARNING**: Rollback deletes ALL migrated files. Requires typing 'ROLLBACK' to confirm.

### 4. `run_complete_migration.py` (All Phases)
**Orchestrator script** - Runs all phases sequentially

**Usage**:
```bash
# Dry run all phases
python run_complete_migration.py --dry-run

# Run complete migration
python run_complete_migration.py

# Skip Phase 4 (do cross-references manually later)
python run_complete_migration.py --skip-phase4
```

---

## 📊 Output Files

### Logs Directory
`C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\LOG\Week_4\`

| File | Description |
|------|-------------|
| `migration_log_YYYYMMDD_HHMMSS.txt` | Complete operation log with timestamps |
| `migration_checkpoint.json` | Progress tracking for resumability |
| `files_marked_for_deletion.txt` | List of old files to archive |
| `dry_run_log.txt` | Dry run simulation log |
| `references_updated_log_YYYYMMDD_HHMMSS.txt` | Cross-reference update log |
| `rollback_log_YYYYMMDD_HHMMSS.txt` | Rollback operation log |

### Reports Directory
`C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\`

| File | Description |
|------|-------------|
| `migration_mapping_table.csv` | Master ID mapping (old → new) |
| `pre_migration_inventory.csv` | Complete inventory of current files |
| `unmapped_tools_report.csv` | Tools not found in taxonomy |
| `duplicate_resolution_decisions.json` | Duplicate handling decisions |
| `preflight_validation_report.json` | Pre-flight check results |
| `dry_run_summary.json` | Dry run statistics |
| `post_migration_validation_report.json` | Validation results (PASS/FAIL) |
| `reference_update_summary.json` | Cross-reference update statistics |
| `rollback_report.json` | Rollback operation report |

---

## ✅ Pre-Migration Checklist

Before running migration:

- [ ] **Backup exists**: Automatic, but verify you have disk space
- [ ] **Python installed**: Version 3.7+ required
- [ ] **Taxonomy CSV exists**: `TAXONOMY/TAX-001_Libraries/Tools_Master_List.csv`
- [ ] **Close applications**: Close any tools that might lock files
- [ ] **Disk space**: At least 100MB free
- [ ] **Review plan**: Read `C:\Users\delir\.claude\plans\rippling-moseying-cookie.md`

---

## 📝 Execution Workflow

### Step 1: Dry Run
```bash
python migrate_tools_to_tol.py --dry-run
```

**Review These Files**:
1. `REPORTS/Week_4/migration_mapping_table.csv` - Check all ID mappings
2. `REPORTS/Week_4/unmapped_tools_report.csv` - Tools needing manual assignment
3. `REPORTS/Week_4/duplicate_resolution_decisions.json` - Duplicate handling
4. `REPORTS/Week_4/dry_run_summary.json` - Statistics
5. `LOG/Week_4/dry_run_log.txt` - Detailed simulation log

**Key Things to Check**:
- [ ] All tools correctly mapped to TOL-### IDs
- [ ] Duplicate resolution decisions are correct
- [ ] No unexpected unmapped tools
- [ ] File counts match expectations

### Step 2: Actual Migration
```bash
python migrate_tools_to_tol.py
```

**What Happens**:
1. Creates backup (10 min)
2. Loads taxonomy and inventory (5 min)
3. Creates mapping table (5 min)
4. Pre-flight validation (2 min)
5. **→ MANUAL CHECKPOINT: Approve execution**
6. Migrates files with checkpoints (20-30 min)
7. Validates migration (5 min)
8. Archives old files (5 min)

**Total Time**: ~50-60 minutes

### Step 3: Validate Results
Check validation report:
```bash
# View validation report
python -m json.tool "C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\post_migration_validation_report.json"
```

**All checks must PASS**:
- ✅ Count validation
- ✅ ID validation (filename matches internal tool_id)
- ✅ JSON validation
- ✅ Duplicate check
- ✅ Reference check

**If ANY check fails**: DO NOT proceed to Phase 4. Investigate or rollback.

### Step 4: Update Cross-References
```bash
python phase4_update_cross_references.py --dry-run
python phase4_update_cross_references.py
```

**What Happens**:
- Scans 5 directories for old TOOL-[CAT]-### IDs
- Replaces with new TOL-### IDs
- Validates JSON after each update
- Generates update log

**Total Time**: ~15-20 minutes

### Step 5: Manual Tasks
1. **Update README.md**:
   - Document new TOL-### ID system
   - Update directory tree example
   - Add migration completion date

2. **Spot-Check Files**:
   - Open 5-10 random `TOL-*.json` files
   - Verify tool_id matches filename
   - Check _migration metadata present
   - Confirm original data intact

3. **Test Integration**:
   - Run any scripts that use tool files
   - Verify no broken references
   - Check dependent systems still work

---

## 🔄 If Something Goes Wrong

### Scenario 1: Validation Failed
```bash
# Check validation report
cat "REPORTS/Week_4/post_migration_validation_report.json"

# If issues found, rollback
python phase5_rollback_migration.py --reason "Validation failed: [specific error]"
```

### Scenario 2: Process Interrupted
```bash
# Migration can resume from checkpoint
python migrate_tools_to_tol.py
# It will detect checkpoint and ask to resume
```

### Scenario 3: Cross-Reference Issues
```bash
# Rollback cross-references not supported
# Manually fix affected files or re-run from backup

# Restore backup of affected directories if needed
```

### Scenario 4: Critical Error
```bash
# Full rollback
python phase5_rollback_migration.py

# This will:
# 1. Delete all TOL-*.json files
# 2. Restore from latest backup
# 3. Verify restoration
# 4. Clean up artifacts
```

---

## 📈 Expected Results

### Before Migration
```
LBS_003_Tools/
├── AI_Tools/
│   ├── Claude.json (tool_id: "TOOL-AI-029")
│   ├── ChatGPT.json (tool_id: "TOOL-AI-002")
│   └── ... (98 files)
├── Cloud_Platforms/ (7 files)
├── Data_Tools/ (5 files)
├── Twitter.json (tool_id: "TOOL-SMM-006")
└── ... (25 root files)
```

### After Migration
```
LBS_003_Tools/
├── TOL-001_LinkedIn.json (tool_id: "TOL-001")
├── TOL-002_Claude.json (tool_id: "TOL-002")
├── TOL-070_Twitter.json (tool_id: "TOL-070")
├── ... (162 files total)
├── _ARCHIVE/
│   └── pre_migration_2025-11-25/
│       ├── AI_Tools/ (old files)
│       └── ... (all old structure)
└── README.md (updated)
```

### File Content Changes
```json
// BEFORE
{
  "tool_id": "TOOL-AI-029",
  "name": "Claude",
  "vendor": "Anthropic"
}

// AFTER
{
  "tool_id": "TOL-002",
  "name": "Claude",
  "vendor": "Anthropic",
  "_migration": {
    "date": "2025-11-25T14:30:00",
    "old_tool_id": "TOOL-AI-029",
    "old_path": "AI_Tools/Claude.json",
    "migrated_by": "tool_migration_script_v1"
  }
}
```

---

## 🎯 Success Criteria

Migration is successful when:

✅ All 162 tool files in root directory (flat structure)
✅ All filenames follow `TOL-###_ToolName.json` format
✅ All `tool_id` fields use `TOL-###` format
✅ Zero duplicate files
✅ All JSON files valid and parseable
✅ File count matches expected
✅ All validation checks PASS
✅ Cross-references updated in dependent systems
✅ Backup created and verified
✅ Old files archived (not deleted)
✅ README.md updated

---

## 📞 Support

**Migration Plan**: `C:\Users\delir\.claude\plans\rippling-moseying-cookie.md`
**Logs**: `C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\LOG\Week_4\`
**Reports**: `C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\`

**Rollback Available**: Yes - `python phase5_rollback_migration.py`

---

## 🔍 Troubleshooting

### Error: "Taxonomy CSV not found"
```bash
# Verify file exists
dir "C:\Users\delir\Dropbox\Dropbox\ENTITIES\TAXONOMY\TAX-001_Libraries\Tools_Master_List.csv"

# If missing, migration cannot proceed
```

### Error: "Python not found"
```bash
# Check Python installation
python --version

# Or try
py --version

# Install Python 3.7+ if needed
```

### Error: "Permission denied"
```bash
# Close any applications using the files
# Run Command Prompt as Administrator
# Ensure Dropbox is not syncing (pause sync temporarily)
```

### Error: "JSON validation failed"
```bash
# Check which file failed in logs
# Manually inspect the file
# May indicate corruption or format issue
# Consider rollback
```

---

**Last Updated**: November 25, 2025
**Script Version**: 1.0
**Python Required**: 3.7+