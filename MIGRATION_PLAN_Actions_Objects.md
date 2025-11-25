# Migration Plan: Actions & Objects to Responsibilities
## Consolidate LIBRARIES Structure

**Date:** 2025-11-17
**Status:** Ready for Execution
**Impact:** High - Affects 128+ files with path references

---

## Executive Summary

This plan consolidates the LIBRARIES architecture by:
1. **Moving** root-level `actions.json` and `objects.json` to Archive (legacy format)
2. **Establishing** `Responsibilities/` as the single source of truth for Actions and Objects
3. **Updating** all path references across TASK_MANAGERS and documentation
4. **Creating** clear navigation from root to organized structure

---

## Part 1: Current State Analysis

### What Exists Now

```
LIBRARIES/
├── actions.json                    📄 Legacy format (simple array)
├── objects.json                    📄 Legacy format (simple array)
│
└── Responsibilities/
    ├── Actions/                    📁 Organized format (6 files)
    │   ├── Actions_Master.json                 (95 KB - 429 actions)
    │   ├── Actions_Master_Command_Verbs.json   (32 KB)
    │   ├── Actions_Master_Process_Verbs.json   (62 KB)
    │   ├── Actions_Master_Result_Verbs.json    (61 KB)
    │   ├── Video_Generation_Actions.json       (24 KB)
    │   └── README.md
    │
    └── Objects/                    📁 Organized format (14 files)
        ├── Agentic_Engineering_Objects.json
        ├── AI_Automation_Objects.json
        ├── Design_Deliverables.json
        ├── Documents.json
        ├── Lead_Generation_Objects.json
        ├── object_types.json
        ├── Portfolio_Deliverables.json
        ├── Publishing_Deliverables.json
        ├── RAG_Objects.json
        ├── Recruitment_Objects.json
        ├── Social_Media_Deliverables.json
        ├── Video_Deliverables.json
        ├── Video_Generation_Objects.json
        └── README.md
```

### Format Comparison

**Root actions.json (Legacy):**
```json
[
  {
    "Actions": "access",
    "Processes": "accessing",
    "Results": "accessed",
    "Departments": "managers",
    "Professions": "recruiter"
  }
]
```

**Responsibilities/Actions/Actions_Master.json (Current):**
```json
{
  "action_id": "ACTION-001",
  "action": "abstract",
  "forms": {
    "processes": ["abstracting"],
    "results": ["abstracted"]
  },
  "departments": [...],
  "professions": [...]
}
```

**Root objects.json (Legacy):**
```json
[
  {
    "Objects": "candidates",
    "Object Types": "needed candidates, applied candidates, found candidates",
    "Professions": "recruiter",
    "Departments": "managers"
  }
]
```

**Responsibilities/Objects/[Domain]_Objects.json (Current):**
```json
{
  "object_id": "OBJ-AI-027",
  "name": "Evaluation System",
  "category": "Agentic_Engineering / Quality Assurance",
  "description": "Systematic evaluation mechanism...",
  "common_actions": ["Create", "Run", "Measure"],
  "business_value": "Enables systematic improvement",
  "source": "Video_013"
}
```

---

## Part 2: Decision - Archive vs. Delete

### Recommendation: ARCHIVE (Not Delete)

**Reasoning:**
1. Legacy files may have historical value
2. Some external scripts might still reference them
3. Safe rollback path if needed
4. Minimal storage cost

**Archive Location:**
```
LIBRARIES/Archive/Legacy_Root_Files/
├── actions.json
├── objects.json
├── tools.json (also found at root)
└── MIGRATION_NOTE.md
```

---

## Part 3: Migration Steps

### Phase 1: Preparation (5 minutes)

**Step 1.1: Create Archive Directory**
```bash
mkdir "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files"
```

**Step 1.2: Create Migration Note**
Create `MIGRATION_NOTE.md` in archive explaining the move.

**Step 1.3: Backup Current State**
```bash
# Create timestamped backup
mkdir "C:\Users\Dell\Dropbox\ENTITIES\BACKUPS\2025-11-17_PreMigration"
# Copy LIBRARIES and TASK_MANAGERS folders
```

---

### Phase 2: Move Legacy Files (5 minutes)

**Step 2.1: Move Root Files to Archive**
```bash
# Move legacy files
mv "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\actions.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\actions.json"

mv "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\objects.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\objects.json"

mv "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\tools.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\tools.json"
```

**Step 2.2: Verify Files Moved**
```bash
# Check archive
ls "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\"

# Verify root is clean
ls "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\" | grep -E "(actions|objects|tools).json"
# Should return nothing
```

---

### Phase 3: Create Navigation Helpers (10 minutes)

**Step 3.1: Create Actions Navigation File**

Create `LIBRARIES/ACTIONS_README.md`:
```markdown
# Actions Library - Navigation

> **Note:** Actions are now organized under the Responsibilities ecosystem.

## Current Location
All action definitions are located in:
```
LIBRARIES/Responsibilities/Actions/
```

## Files Available
- **Actions_Master.json** - Complete actions catalog (429 actions)
- **Actions_Master_Command_Verbs.json** - Command-oriented actions
- **Actions_Master_Process_Verbs.json** - Process-oriented actions
- **Actions_Master_Result_Verbs.json** - Result-oriented actions
- **Video_Generation_Actions.json** - Video-specific actions

## Quick Links
- [Actions README](Responsibilities/Actions/README.md)
- [Actions Master File](Responsibilities/Actions/Actions_Master.json)
- [Responsibilities Ecosystem](Responsibilities/README.md)

## Legacy Files
Previous root-level `actions.json` has been archived to:
```
LIBRARIES/Archive/Legacy_Root_Files/actions.json
```

**Last Updated:** 2025-11-17
```

**Step 3.2: Create Objects Navigation File**

Create `LIBRARIES/OBJECTS_README.md`:
```markdown
# Objects Library - Navigation

> **Note:** Objects are now organized under the Responsibilities ecosystem.

## Current Location
All object definitions are located in:
```
LIBRARIES/Responsibilities/Objects/
```

## Files Available (14 files)
- **object_types.json** - Object type classifications
- **Agentic_Engineering_Objects.json** - AI agent objects
- **AI_Automation_Objects.json** - Automation objects
- **Design_Deliverables.json** - Design outputs
- **Documents.json** - Document objects
- **Lead_Generation_Objects.json** - LG objects
- **Portfolio_Deliverables.json** - Portfolio items
- **Publishing_Deliverables.json** - Publishing outputs
- **RAG_Objects.json** - RAG system objects
- **Recruitment_Objects.json** - HR objects
- **Social_Media_Deliverables.json** - SMM outputs
- **Video_Deliverables.json** - Video outputs
- **Video_Generation_Objects.json** - Video production objects

## Quick Links
- [Objects README](Responsibilities/Objects/README.md)
- [Object Types](Responsibilities/Objects/object_types.json)
- [Responsibilities Ecosystem](Responsibilities/README.md)

## Legacy Files
Previous root-level `objects.json` has been archived to:
```
LIBRARIES/Archive/Legacy_Root_Files/objects.json
```

**Last Updated:** 2025-11-17
```

---

### Phase 4: Update LIBRARIES README (15 minutes)

**Step 4.1: Update Main README.md**

In `LIBRARIES/README.md`, update sections:

**Current (Lines 25-49 - Actions Section):**
```markdown
### 1. Actions
**Purpose:** Standardized action verbs for task naming

**File Structure:**
```
Actions/
├── Communication_Actions.json
├── Creative_Actions.json
├── Analysis_Actions.json
└── Management_Actions.json
```
```

**Update To:**
```markdown
### 1. Actions
**Purpose:** Standardized action verbs for task naming

> **Location:** Now part of Responsibilities ecosystem
> **Path:** `LIBRARIES/Responsibilities/Actions/`

**File Structure:**
```
Responsibilities/Actions/
├── Actions_Master.json                 # 429 actions complete catalog
├── Actions_Master_Command_Verbs.json   # Command-oriented subset
├── Actions_Master_Process_Verbs.json   # Process-oriented subset
├── Actions_Master_Result_Verbs.json    # Result-oriented subset
├── Video_Generation_Actions.json       # Video-specific actions
└── README.md
```

**Quick Navigation:** See [ACTIONS_README.md](ACTIONS_README.md)
```

**Current (Lines 150-178 - Objects Section):**
```markdown
### 4. Objects
**Purpose:** Business objects that actions are performed on

**File Structure:**
```
Objects/
├── object_types.json
├── objects.json
├── Documents.json
└── [Category folders]/
```
```

**Update To:**
```markdown
### 4. Objects
**Purpose:** Business objects that actions are performed on

> **Location:** Now part of Responsibilities ecosystem
> **Path:** `LIBRARIES/Responsibilities/Objects/`

**File Structure:**
```
Responsibilities/Objects/
├── object_types.json                   # Object type classifications
├── Agentic_Engineering_Objects.json
├── AI_Automation_Objects.json
├── Design_Deliverables.json
├── Documents.json
├── Lead_Generation_Objects.json
├── Portfolio_Deliverables.json
├── Publishing_Deliverables.json
├── RAG_Objects.json
├── Recruitment_Objects.json
├── Social_Media_Deliverables.json
├── Video_Deliverables.json
├── Video_Generation_Objects.json
└── README.md
```

**Quick Navigation:** See [OBJECTS_README.md](OBJECTS_README.md)

**Total:** 36+ objects across 13 domain-specific collections
```

**Step 4.2: Update File Structure Diagram**

Update the main file structure section (around line 567):

**Before:**
```markdown
**Pattern:** `LIBRARIES_[Type]_[Name]_[Version].json`

**Examples:**
- `LIBRARIES_Action_Create_v1.json`
- `LIBRARIES_Object_Job_Posting_v1.json`
```

**After:**
```markdown
**Pattern:** `LIBRARIES_[Type]_[Name]_[Version].json`

**Examples:**
- `Responsibilities/Actions/Actions_Master.json`
- `Responsibilities/Objects/Design_Deliverables.json`

**Note:** Actions and Objects are organized under `Responsibilities/` ecosystem.
```

---

### Phase 5: Update Path References (60-90 minutes)

**Step 5.1: Scan for References**

Search patterns to find:
```bash
# Find all references to old paths
grep -r "LIBRARIES/actions.json" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\"
grep -r "LIBRARIES/objects.json" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\"
grep -r "Actions/" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS\"
grep -r "Objects/" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS\"
```

**Step 5.2: Standard Path Replacements**

**Old Path → New Path Mapping:**

```
# Actions references
LIBRARIES/Actions/                    → LIBRARIES/Responsibilities/Actions/
LIBRARIES/actions.json                → LIBRARIES/Responsibilities/Actions/Actions_Master.json

# Objects references
LIBRARIES/Objects/                    → LIBRARIES/Responsibilities/Objects/
LIBRARIES/objects.json                → LIBRARIES/Responsibilities/Objects/object_types.json

# From TASK_MANAGERS perspective
../../LIBRARIES/Actions/              → ../../LIBRARIES/Responsibilities/Actions/
../../LIBRARIES/Objects/              → ../../LIBRARIES/Responsibilities/Objects/
```

**Step 5.3: Key Files to Update**

Based on grep results (128 files reference LIBRARIES), priority files:

1. **TASK_MANAGERS/PROMPTS/Architecture_Learning_Guide.md**
   - Lines referencing Actions_Master.json
   - Lines referencing Objects collections

2. **TASK_MANAGERS/PROMPTS/Architecture_Merge_Planning_Prompt.md**
   - Full architecture paths

3. **TASK_MANAGERS/PROMPTS/Video_Processing/*.md**
   - Object extraction prompts
   - Action categorization prompts

4. **TASK_MANAGERS/PROMPTS/Library_Processing/*.md**
   - Tools collection prompts
   - Integration prompts

5. **TASK_MANAGERS/PROMPTS/Core/MAIN_PROMPT_v5_Modular/01_Library_Integration/*.md**
   - All library integration modules

6. **TASK_MANAGERS/PROMPTS/PROMPTS_INDEX.json**
   - Cross-reference paths

**Step 5.4: Automated Replacement Script**

Create `ENTITIES/update_paths_actions_objects.py`:

```python
import os
import re
from pathlib import Path

# Paths to update
ENTITIES_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES")
TASK_MANAGERS = ENTITIES_DIR / "TASK_MANAGERS"

# Replacement patterns
REPLACEMENTS = {
    # Actions
    r'LIBRARIES/Actions/': 'LIBRARIES/Responsibilities/Actions/',
    r'LIBRARIES/actions\.json': 'LIBRARIES/Responsibilities/Actions/Actions_Master.json',

    # Objects
    r'LIBRARIES/Objects/': 'LIBRARIES/Responsibilities/Objects/',
    r'LIBRARIES/objects\.json': 'LIBRARIES/Responsibilities/Objects/object_types.json',

    # Relative paths from TASK_MANAGERS
    r'\.\./\.\./LIBRARIES/Actions/': '../../LIBRARIES/Responsibilities/Actions/',
    r'\.\./\.\./LIBRARIES/Objects/': '../../LIBRARIES/Responsibilities/Objects/',
}

def update_file_paths(file_path):
    """Update paths in a single file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Apply all replacements
    for old_pattern, new_path in REPLACEMENTS.items():
        content = re.sub(old_pattern, new_path, content)

    # Only write if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def scan_and_update(directory):
    """Scan directory and update all .md and .json files"""
    updated_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.json')):
                file_path = Path(root) / file
                if update_file_paths(file_path):
                    updated_files.append(str(file_path))

    return updated_files

if __name__ == "__main__":
    print("Scanning TASK_MANAGERS for path updates...")
    updated = scan_and_update(TASK_MANAGERS)

    print(f"\nUpdated {len(updated)} files:")
    for f in updated:
        print(f"  ✓ {f}")

    print("\nDone!")
```

---

### Phase 6: Update PROMPTS_INDEX.json (10 minutes)

**Step 6.1: Update Cross-References**

In `TASK_MANAGERS/PROMPTS/PROMPTS_INDEX.json`, update all prompts' `cross_references`:

**Find all occurrences of:**
```json
"actions": "Extracts action verbs for Actions library",
"objects": "Identifies deliverables for Objects library"
```

**Update to:**
```json
"actions": "Extracts action verbs for Responsibilities/Actions library",
"objects": "Identifies deliverables for Responsibilities/Objects library"
```

---

### Phase 7: Validation & Testing (30 minutes)

**Step 7.1: Path Existence Check**

```python
# Verify all new paths exist
import os
from pathlib import Path

LIBRARIES = Path(r"C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES")

paths_to_verify = [
    LIBRARIES / "Responsibilities/Actions/Actions_Master.json",
    LIBRARIES / "Responsibilities/Actions/README.md",
    LIBRARIES / "Responsibilities/Objects/object_types.json",
    LIBRARIES / "Responsibilities/Objects/README.md",
    LIBRARIES / "ACTIONS_README.md",
    LIBRARIES / "OBJECTS_README.md",
    LIBRARIES / "Archive/Legacy_Root_Files/actions.json",
    LIBRARIES / "Archive/Legacy_Root_Files/objects.json",
]

for path in paths_to_verify:
    if path.exists():
        print(f"✓ {path}")
    else:
        print(f"✗ MISSING: {path}")
```

**Step 7.2: Broken Link Check**

```bash
# Manually test key prompts
# Open these files and verify paths work:
# 1. TASK_MANAGERS/PROMPTS/Architecture_Learning_Guide.md
# 2. TASK_MANAGERS/PROMPTS/PROMPTS/Taxonomy_Integration/Taxonomy_Analysis_and_Updates_Prompt.md
# 3. TASK_MANAGERS/PROMPTS/README.md
```

**Step 7.3: Grep Verification**

```bash
# Should return 0 results (all updated)
grep -r "LIBRARIES/actions\.json" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\"
grep -r "LIBRARIES/objects\.json" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\"

# Should return results (properly updated)
grep -r "LIBRARIES/Responsibilities/Actions" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\" | wc -l
grep -r "LIBRARIES/Responsibilities/Objects" "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\" | wc -l
```

---

## Part 4: Post-Migration Structure

### Final LIBRARIES Structure

```
LIBRARIES/
├── DEPARTMENTS/                        # Department definitions
├── Professions/                        # Profession files
├── Responsibilities/                   # ✨ UNIFIED ECOSYSTEM
│   ├── Core/
│   │   ├── responsibilities_master.json
│   │   ├── phrase_matching_index.json
│   │   ├── action_variants_map.json
│   │   ├── object_variants_map.json
│   │   └── By_Department/ (8 files)
│   ├── Actions/                        # ← Organized Actions
│   │   ├── Actions_Master.json
│   │   ├── Actions_Master_Command_Verbs.json
│   │   ├── Actions_Master_Process_Verbs.json
│   │   ├── Actions_Master_Result_Verbs.json
│   │   ├── Video_Generation_Actions.json
│   │   └── README.md
│   ├── Objects/                        # ← Organized Objects
│   │   ├── object_types.json
│   │   ├── [13 domain-specific object files]
│   │   └── README.md
│   ├── Parameters/
│   └── README.md
├── Tools/                              # Tools library
├── Archive/
│   └── Legacy_Root_Files/              # ← Archived legacy files
│       ├── actions.json
│       ├── objects.json
│       ├── tools.json
│       └── MIGRATION_NOTE.md
├── ACTIONS_README.md                   # ← Navigation helper
├── OBJECTS_README.md                   # ← Navigation helper
├── README.md                           # Main documentation
└── LIBRARIES_Import_Index.md
```

---

## Part 5: Communication & Documentation

### Update Checklist

**Documentation Files to Update:**
- [x] LIBRARIES/README.md (Actions and Objects sections)
- [x] LIBRARIES/ACTIONS_README.md (create new)
- [x] LIBRARIES/OBJECTS_README.md (create new)
- [x] LIBRARIES/Responsibilities/README.md (verify paths)
- [x] LIBRARIES/Archive/Legacy_Root_Files/MIGRATION_NOTE.md (create)
- [x] TASK_MANAGERS/PROMPTS/README.md
- [x] TASK_MANAGERS/PROMPTS/PROMPTS_INDEX.json
- [x] ARCHITECTURE_UPDATE_PLAN.md (add migration completed note)

**Notify Users:**
Create announcement in `LIBRARIES/MIGRATION_ANNOUNCEMENT_2025-11-17.md`

---

## Part 6: Rollback Plan

### If Issues Arise

**Quick Rollback (5 minutes):**
```bash
# Restore from backup
cp -r "C:\Users\Dell\Dropbox\ENTITIES\BACKUPS\2025-11-17_PreMigration\LIBRARIES\" \
      "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\"

cp -r "C:\Users\Dell\Dropbox\ENTITIES\BACKUPS\2025-11-17_PreMigration\TASK_MANAGERS\" \
      "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\"
```

**Partial Rollback:**
```bash
# Just restore root files if needed
cp "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\actions.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\actions.json"

cp "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\Archive\Legacy_Root_Files\objects.json" \
   "C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\objects.json"
```

---

## Part 7: Success Criteria

**Migration Complete When:**
- [ ] Root actions.json and objects.json moved to Archive
- [ ] Navigation helpers created (ACTIONS_README.md, OBJECTS_README.md)
- [ ] LIBRARIES README updated with new paths
- [ ] All TASK_MANAGERS/PROMPTS references updated
- [ ] PROMPTS_INDEX.json cross-references updated
- [ ] Path validation script runs with 0 errors
- [ ] Manual testing of 5 key prompts successful
- [ ] Grep verification shows no old path references
- [ ] Documentation updated
- [ ] Migration announcement created

---

## Part 8: Timeline

**Estimated Total Time: 2-3 hours**

| Phase | Task | Time | Complexity |
|-------|------|------|------------|
| 1 | Preparation | 5 min | Low |
| 2 | Move files | 5 min | Low |
| 3 | Create navigation | 10 min | Low |
| 4 | Update LIBRARIES README | 15 min | Medium |
| 5 | Update path references | 60-90 min | High |
| 6 | Update PROMPTS_INDEX | 10 min | Medium |
| 7 | Validation & testing | 30 min | Medium |

---

## Part 9: Next Steps

**Ready to Begin?**

1. Review this plan
2. Confirm approach (archive vs delete)
3. Choose execution time
4. Execute phases in order
5. Test thoroughly
6. Update this document with results

---

**Migration Plan Created:** 2025-11-17
**Created By:** Claude AI Assistant
**Status:** Ready for Execution
**Approval Required:** Yes
**Estimated Impact:** 128+ files, 2-3 hours work
