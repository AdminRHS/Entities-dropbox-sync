# _SHARED / Archive

**Purpose:** Historical and deprecated shared resources
**Created:** 2025-11-15
**Last Updated:** 2025-11-15

---

## Overview

This archive contains historical content and deprecated resources from shared department resources. Content is preserved for:
- Historical context and reference
- Understanding design decisions
- Compliance and documentation requirements
- Version history tracking

**Note:** Archive content is read-only and not actively used in current workflows.

---

## Contents

### Prompts_Archive (`Prompts_LBS_009_Archive/`)

**Archived:** 2025-11-15 (moved with Prompts migration from LIBRARIES)

**Previous Location:** `LBS_006_Departments/PROMPTS/LBS_009_Archive/`

**Size:** ~747MB (includes large session logs)

**Contents:**

#### 1. Integration_Plans/ (3 files)
Historical integration planning documents for prompt development and taxonomy integration:
- Planning materials for merging different prompt workflows
- Integration strategies for combining Transcribations and Research
- Architecture planning for prompt organization

#### 2. Legacy/
Deprecated prompt structures and formats:
- **Prompts_to_run/** - Old prompt execution directory structure
- Superseded prompt versions
- Previous organizational schemas
- Deprecated workflows and methodologies

#### 3. Session_Logs/ (2 files, ~745MB)
Development session logs from prompt creation and refinement:
- Large log files documenting prompt development sessions
- Conversation histories with AI during prompt creation
- Iteration and refinement documentation
- Testing and validation logs

**Note:** Session logs are very large (~745MB total) and contain detailed conversation histories. Preserved for historical reference but not needed for current operations.

#### 4. Historical Documentation
- `PROMPT_Folder_Reorganization.md` - Documentation of previous reorganization efforts
- `README.md` - Archive-specific documentation (if exists)
- Other planning and architectural materials

---

## Archive Policy

### Purpose of Archive

**What Gets Archived:**
- Deprecated prompts or workflows
- Superseded documentation and methodologies
- Historical planning and integration materials
- Development logs and session notes
- Previous organizational structures

**What Does NOT Get Archived:**
- Active prompts (stay in `Prompts/`)
- Current documentation
- In-use workflows
- Recent session logs (less than 6 months old)

### Retention Policy

**Permanent Archive:**
- Integration plans (historical value)
- Major design decision documentation
- Significant architectural changes

**Temporary Archive (6-12 months):**
- Deprecated prompts (keep until no longer referenced)
- Session logs (review annually for deletion)
- Superseded documentation

**Review Schedule:**
- Annual review of archive contents
- Evaluate what can be permanently deleted
- Compress large files to save space
- Update archive documentation

---

## Accessing Archive Content

### If You Need to Reference Archived Content:

1. **Navigate** to `LBS_006_Departments/LBS_009_Archive/PROMPTS_LBS_009_Archive/`
2. **Review** the README in relevant subdirectory
3. **Read-Only** - Do not modify archived content
4. **Copy** if you need to resurrect archived content:
   - Copy to active location (`PROMPTS/`)
   - Update to current standards
   - Document in PROMPTS_INDEX.json

### Common Use Cases:

- **Understanding history:** Why was a prompt designed this way?
- **Recovering deprecated features:** Previous workflow had useful elements
- **Compliance:** Need to show historical versions for audit
- **Learning:** Study how prompts evolved over time

---

## Migration History

### 2025-11-15: Prompts Archive Migration

**Moved from:** `LBS_006_Departments/PROMPTS/LBS_009_Archive/`
**Moved to:** `LBS_006_Departments/LBS_009_Archive/PROMPTS_LBS_009_Archive/`

**Reason:** Consolidate all PROMPTS-related content in DEPARTMENTS structure

**What was moved:**
- Integration_Plans/ (3 files)
- Legacy/Prompts_to_run/
- Session_Logs/ (2 files, ~745MB)
- Historical documentation

**See also:**
- Main PROMPTS migration: `PROMPTS/README.md`
- Migration prompt: `LBS_008_Taxonomy/Entities/PROMPT_Move_Prompts_to_Departments_Shared.md`

---

## Archive Structure

```
LBS_009_Archive/
└── Prompts_LBS_009_Archive/                   [~747MB total]
    ├── Integration_Plans/             [3 files]
    │   ├── [Integration planning docs]
    │   └── [Architecture plans]
    ├── Legacy/                        [Deprecated structures]
    │   └── Prompts_to_run/            [Old execution directory]
    ├── Session_Logs/                  [2 files, ~745MB]
    │   ├── [Large session log 1]
    │   └── [Large session log 2]
    ├── PROMPT_Folder_Reorganization.md
    └── README.md (if exists)
```

---

## Maintenance

### For Archive Administrators:

**Adding to Archive:**
1. Move deprecated content from active locations
2. Update this README with what was added and why
3. Note archive date and previous location
4. Add to appropriate subdirectory (or create new one)

**Reviewing Archive:**
1. Annual review of all archive contents
2. Identify what can be permanently deleted
3. Compress large files if possible
4. Update retention dates
5. Document decisions in this README

**Restoring from Archive:**
1. Only if truly needed for active work
2. Copy (don't move) from archive to active location
3. Update to current standards and formats
4. Document resurrection in active location's README
5. Leave copy in archive for history

---

## For Questions

**Archive Management:**
- Contact: AI or ADMIN departments
- Review: Archive policy and retention guidelines
- Check: Migration documentation for context

**Content Questions:**
- Review subdirectory READMEs for specific content details
- Check session logs for prompt development history
- Consult integration plans for architectural context

---

**Last Updated:** 2025-11-15
**Next Review:** 2026-11-15
**Archive Size:** ~747MB
