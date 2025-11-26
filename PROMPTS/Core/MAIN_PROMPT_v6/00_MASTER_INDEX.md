# MAIN PROMPT v6 - MASTER INDEX

**Version:** 6.0 | **Date:** 2025-11-19 | **Status:** Production
**Replaces:** v4 | **Size:** ~700 lines | **Tokens:** ~5,000 | **Load:** <3s

---

## MODULAR FILE STRUCTURE

This is the master index for MAIN_PROMPT_v6. All sections have been split into modular files for easier maintenance and selective loading.

### Core Modules (Load All for Full Context)

1. **[01_Core_Identity.md](01_Core_Identity.md)**
   - WHO YOU ARE, WHAT YOU DO, HOW YOU OPERATE
   - Available entities (PRT, MLT, TSK, STP, ACT, OBJ, TOL, SKL, PRF, RSP, PMT)
   - Core operating principles

2. **[02_Entity_Taxonomy.md](02_Entity_Taxonomy.md)**
   - ID standards (XXX-### format)
   - Entity relationships
   - Cross-entity linking rules
   - Validation rules

3. **[03_Workflow_Execution.md](03_Workflow_Execution.md)**
   - Video processing workflows
   - Daily reports (PMT-032 to PMT-043)
   - Research integration (PMT-044 to PMT-052)
   - Task manager operations
   - HR automation (PMT-053 to PMT-057)
   - System maintenance

4. **[04_Department_Operations.md](04_Department_Operations.md)**
   - Department codes (AID, VID, HRM, DEV, LGN, DGN, MKT, SLS, SMM, FIN)
   - Department-specific prompts
   - Daily workflow patterns
   - Cross-department collaboration

5. **[05_File_Operations.md](05_File_Operations.md)**
   - Directory structure (ENTITIES/)
   - Naming conventions
   - Validation checklist
   - Auto-validation commands

6. **[06_Prompt_Reference.md](06_Prompt_Reference.md)**
   - All 73 prompts by category
   - Decision matrix (which prompt to use when)
   - Common prompt chains
   - Quick lookup by department/function

7. **[07_Quality_Validation.md](07_Quality_Validation.md)**
   - Auto-validation commands
   - Quality checklists
   - Common errors & fixes
   - Validation workflow

8. **[08_External_Modules.md](08_External_Modules.md)**
   - Optional modules (load on-demand)
   - Module selection guide
   - Loading syntax

---

## QUICK START GUIDE

### For Daily Operations
Load: `01_Core_Identity.md` + `04_Department_Operations.md` + `06_Prompt_Reference.md`

### For Video Processing
Load: `01_Core_Identity.md` + `03_Workflow_Execution.md` (Video section)

### For Taxonomy Work
Load: `02_Entity_Taxonomy.md` + `05_File_Operations.md` + `07_Quality_Validation.md`

### For New Entity Creation
Load: `02_Entity_Taxonomy.md` + `07_Quality_Validation.md`

### Full System Context
Load all modules (01-08)

---

## USAGE INSTRUCTIONS

**Loading This Prompt:**
```
Load: ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/00_MASTER_INDEX.md
Then: Load specific modules as needed
```

**Context Aware:**
- Automatically knows all entity types
- Understands PMT-### prompt system
- Can execute any workflow via prompt ID
- Validates data before operations

**Executing Workflows:**
1. Identify task → 2. Find prompt (Module 06) → 3. Execute → 4. Validate

---

## COMPRESSION METRICS

| Metric | v4 | v6 | Reduction |
|--------|----|----|-----------|
| **Lines** | ~2800 | ~750 | **73%** |
| **Tokens** | ~15,000 | ~5,200 | **65%** |
| **Sections** | 25+ | 8 | **68%** |
| **Tables** | 5 | 22 | **+340%** |
| **Load Time** | 8-10s | ~2.5s | **75%** faster |

---

## VERSION HISTORY

### v6.0 (2025-11-19)
**Changes:**
- Ultra-condensed from v4: 73% line reduction, 65% token reduction
- Restructured to 8 core sections (from 25+)
- Split into modular files for selective loading
- Replaced prose with 22 data tables
- Added modular architecture with on-demand loading
- Implemented prompt reference system (73 PMT prompts)
- Added comprehensive validation workflows
- Optimized for <3 second load time

**Author:** AI & Automation Team
**Generated via:** PMT-073

### v4.0 (2025-11-18)
- Comprehensive system prompt
- ~2800 lines, 25+ sections
- Embedded content (no modules)
- **Status:** Deprecated (transition period)

---

**END OF MASTER INDEX**
