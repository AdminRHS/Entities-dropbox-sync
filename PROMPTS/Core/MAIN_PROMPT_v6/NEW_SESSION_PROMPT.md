# Start Here: MAIN_PROMPT_v6 Update Continuation

Hi Claude! We're in the middle of updating the MAIN_PROMPT_v6 modular system. This is an 8-part prompt system for daily employee task extraction and progress tracking.

## Current Progress: 3 of 8 Files Complete

**Just Completed (File 3):** [03_Workflow_Execution.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/03_Workflow_Execution)

**Next Up (File 4):** [04_Department_Operations.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/04_Department_Operations)

## What We're Doing

We're systematically updating each file in the MAIN_PROMPT_v6 system to:

1. **Fix ID formats**: TSK→TST, STP→STT throughout
2. **Simplify libraries**: Remove RSP/ACT/OBJ/PRM, keep only TOL (Tools) + add GDS (Guides)
3. **Emphasize reusable templates**: Many-to-many relationships, no hard links
4. **Task-first workflow**: Bottom-up classification (TST → STT → MLT → PRT)
5. **Update file paths**: From `TASK_MANAGERS/DATA/` to `TSM-00X_[Category]/`
6. **Add GUIDES references**: GDS-010, GDS-011, GDS-012

## Key Changes Made So Far

### Global Pattern:
- ❌ **Removed**: RSP (Responsibility), ACT (Action), OBJ (Object), PRM (Parameter)
- ✅ **Kept**: TOL (Tool) - includes browser extensions
- ✅ **Added**: GDS (Guide) - for classification help

### ID Format Fixes:
- TSK-### → **TST-###** (Task Template)
- STP-### → **STT-###** (Step Template)
- MLS-### → **MLT-###** (Milestone Template)

### Core Principles:
1. **Task-First**: Extract TST-### first, classify upward
2. **Bottom-Up**: Tasks → Steps → Milestones → Projects
3. **Reusable Templates**: Same template can be used in multiple parents (many-to-many)
4. **No Hard Links**: Composition happens at runtime
5. **Project Tracking**: PRT-### as primary progress point

## Important Context

### Completed Files:
1. ✅ **01_Core_Identity.md** (v6.1→v6.2) - Core workflow definitions
2. ✅ **02_Entity_Taxonomy.md** (v6.0→v6.1) - ID standards, relationships, examples
3. ✅ **03_Workflow_Execution.md** (v6.0→v6.1) - Workflow prompts catalog

### Key GUIDES (Classification Help):
- **[GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010)**: Daily workflow structure
- **[GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)**: Decision tree for PRT/MLT/TST/STT selection
- **[GDS-012](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012)**: Template cross-references

### Reusable Template System:
Templates are INDEPENDENT and can be composed:
- Same **STT-###** can be part of multiple **TST**
- Same **TST-###** can be part of multiple **MLT**
- Same **MLT-###** can be part of multiple **PRT**

## Next File to Update: 04_Department_Operations.md

### Known Issues in File 4:
1. Department prompts need updating
2. "Video Processing" should be renamed to reflect it's one research type
3. Need to clarify: Research tracking includes video, documents, web research, etc.
4. Apply standard ID format fixes (TSK→TST, STP→STT)
5. Remove ACT/OBJ/RSP/PRM references, add GDS

### User's Request:
"We will have to update the department's prompts too. We do want to track researches that have been done while the video processing is the researchers, so it has been renamed to researchers, but it is just one of the possible."

## Your Task

Please:

1. **Read the progress tracking file** to understand what's been done:
   - [PROGRESS_TRACKING.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/PROGRESS_TRACKING)

2. **Review the next file** to update:
   - [04_Department_Operations.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/04_Department_Operations)

3. **Apply the same update pattern** as files 1-3:
   - Fix ID formats (TSK→TST, STP→STT)
   - Update version number and date
   - Remove ACT/OBJ/RSP/PRM references
   - Add GDS references where appropriate
   - Update file paths to TSM-00X structure
   - Add notes about reusable templates

4. **Address the research tracking clarification**:
   - Video processing is ONE type of research
   - Other research types exist (document analysis, web research, etc.)
   - Update naming/structure accordingly

## Reference Documentation

**Completed Changelogs:**
- [CHANGELOG_Core_Identity_v6.1_to_v6.2.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/CHANGELOG_Core_Identity_v6.1_to_v6.2)
- [CHANGELOG_Entity_Taxonomy_v6.0_to_v6.1.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/CHANGELOG_Entity_Taxonomy_v6.0_to_v6.1)

**Implementation Plan:**
- [IMPLEMENTATION_PLAN_Core_Identity_Update.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/IMPLEMENTATION_PLAN_Core_Identity_Update)

**Master Data Files:**
- Projects: `ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/Project_Templates_Master_List.csv`
- Tasks: `ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/Task_Templates_Master_List.csv`
- Steps: `ENTITIES/TASK_MANAGERS/TSM-004_Step_Templates/Taxonomy/Step_Templates_Master_List.csv`
- Guides: `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GUIDES_Master_List.csv`

## Working Directory

All paths are relative to: `C:\Users\Dell\Dropbox\`

## Success Criteria

For each file update:
1. ✅ Version number updated (increment minor version)
2. ✅ Date updated to current date
3. ✅ All ID formats corrected (TST, STT, MLT, PRT)
4. ✅ Library references simplified (TOL + GDS only)
5. ✅ File paths updated to TSM-00X structure
6. ✅ Reusable template notes added where relevant
7. ✅ Changelog created documenting all changes

## Let's Continue!

Please start by reading [04_Department_Operations.md](ENTITIES/PROMPTS/Core/MAIN_PROMPT_v6/04_Department_Operations) and let me know what updates it needs, following the same pattern we established for files 1-3.

Ready when you are! 🚀
