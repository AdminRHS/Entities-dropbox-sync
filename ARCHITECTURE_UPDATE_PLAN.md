# Architecture Update Plan
## LIBRARIES Naming Conventions & TASK_MANAGERS/PROMPTS Alignment

**Date:** 2025-11-17
**Status:** Analysis Complete - Ready for Implementation
**Scope:** C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES and C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS

---

## Executive Summary

After comprehensive analysis of the LIBRARIES architecture and TASK_MANAGERS/PROMPTS structure, I've identified several naming convention inconsistencies and documentation misalignments that need to be addressed. This document provides a complete action plan for standardization.

---

## Part 1: Current State Analysis

### LIBRARIES Architecture (Current)

```
C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\
├── DEPARTMENTS/                    ✅ Correctly named
│   ├── departments.json
│   ├── By_Department/
│   ├── Archive/
│   └── README.md
│
├── Professions/                    ✅ Correctly named
│   ├── *.json (individual profession files)
│   ├── professions.json
│   └── README.md
│
├── Responsibilities/               ✅ Correctly organized (v2.0)
│   ├── Core/
│   │   ├── responsibilities_master.json (193 responsibilities)
│   │   ├── phrase_matching_index.json
│   │   ├── action_variants_map.json
│   │   ├── object_variants_map.json
│   │   └── By_Department/ (8 department views)
│   ├── Actions/ (27 files)
│   ├── Objects/ (13 files)
│   ├── Parameters/ (15 files)
│   └── README.md
│
├── Tools/                          ✅ Correctly organized
│   ├── AI_Tools/
│   ├── Development_Tools/
│   ├── Databases/
│   └── [13 categories total]
│
├── actions.json                    ⚠️ Root-level file (should reference Responsibilities/Actions/)
├── objects.json                    ⚠️ Root-level file (should reference Responsibilities/Objects/)
├── tools.json                      ⚠️ Root-level file (master index?)
├── README.md                       ✅ Main documentation
├── LIBRARIES_Import_Index.md       ✅ Import tracking
└── [Other documentation files]
```

### TASK_MANAGERS/PROMPTS Structure (Current)

```
C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS\
├── Core/                           ✅ Correctly named
├── Daily_Reports/                  ✅ Correctly named
├── Video_Processing/               ✅ Correctly named
├── Library_Processing/             ✅ Correctly named
├── HR_Operations/                  ✅ Correctly named
├── Operational_Workflows/          ✅ Correctly named
├── System_Analysis/                ✅ Correctly named
├── Automation/                     ✅ Correctly named
├── Communication/                  ✅ Correctly named
├── Research Prompts/               ⚠️ INCONSISTENT - Has space instead of underscore
├── README.md
├── PROMPTS_INDEX.json
└── [Various prompt files]
```

---

## Part 2: Issues Identified

### Issue 1: Root-Level Library Files vs. Organized Structure

**Problem:**
- `actions.json` exists at LIBRARIES root
- `objects.json` exists at LIBRARIES root
- `tools.json` exists at LIBRARIES root
- But actual organized data is in `Responsibilities/Actions/`, `Responsibilities/Objects/`, `Tools/`

**Impact:**
- Potential confusion about which is the source of truth
- Duplicate or outdated data risk
- TASK_MANAGERS/PROMPTS references may point to wrong location

**Recommendation:**
1. Verify if root-level files are master indexes or legacy duplicates
2. If indexes: Update with clear "See Responsibilities/" pointers
3. If legacy: Move to `LIBRARIES/Archive/` or delete
4. Update all TASK_MANAGERS/PROMPTS references to point to correct locations

### Issue 2: Folder Naming Inconsistency in TASK_MANAGERS/PROMPTS

**Problem:**
- Folder name: `Research Prompts` (has space)
- All other folders use underscores: `HR_Operations`, `Video_Processing`, etc.

**Impact:**
- File path complexity in scripts and code
- Inconsistent user experience
- Potential command-line/bash issues with spaces

**Recommendation:**
- Rename `Research Prompts/` → `Research_Prompts/`
- Update all references in documentation and PROMPTS_INDEX.json

### Issue 3: LIBRARIES Documentation References

**Problem:**
The LIBRARIES README.md (lines 462-495) references:
```
Previous Location: `LIBRARIES/DEPARTMENTS/_SHARED/Prompts/`
New Location: `LIBRARIES/DEPARTMENTS/PROMPTS/`
```

But actual current location is:
```
TASK_MANAGERS/PROMPTS/
```

**Impact:**
- Misleading documentation
- Users may search in wrong location
- Architecture understanding confusion

**Recommendation:**
- Update LIBRARIES README to clarify Prompts are in TASK_MANAGERS entity
- Add clear cross-reference section
- Remove outdated migration notes or move to Archive

### Issue 4: 128 Files with Potential Path References

**Problem:**
- 128 files in TASK_MANAGERS/PROMPTS reference "LIBRARIES", "Responsibilities", "Departments", "Professions"
- Many may have outdated path references
- Difficult to verify without checking each file

**Impact:**
- Broken links in documentation
- Incorrect file paths in prompts
- Integration issues

**Recommendation:**
- Systematic review of path references
- Update to standardized relative paths
- Create path validation script

---

## Part 3: Naming Convention Standards

### Standard 1: Folder Naming

**Rule:** All folder names use `PascalCase` or `Snake_Case` with underscores, NO SPACES

**Examples:**
- ✅ `Video_Processing`
- ✅ `HR_Operations`
- ✅ `Daily_Reports`
- ❌ `Research Prompts` (should be `Research_Prompts`)

### Standard 2: File Naming

**Pattern:** `{TYPE}_{Name}_{Optional_Version}.{ext}`

**Examples:**
- ✅ `PROMPT_Data_Consistency_and_Knowledge_Integration.md`
- ✅ `MAIN_PROMPT_v5_Modular`
- ✅ `responsibilities_master.json`
- ✅ `LIBRARIES_Import_Index.md`

### Standard 3: Path References

**Rule:** Use relative paths from ENTITIES root

**Standard Format:**
```
From TASK_MANAGERS/PROMPTS:
- ../../LIBRARIES/Responsibilities/Core/responsibilities_master.json
- ../../LIBRARIES/DEPARTMENTS/departments.json
- ../../LIBRARIES/Professions/professions.json
- ../../LIBRARIES/Tools/AI_Tools/

From LIBRARIES:
- ../TASK_MANAGERS/PROMPTS/Video_Processing/
- ../TASK_MANAGERS/Task_Templates/
```

### Standard 4: JSON Master Files

**Naming Pattern:** `{entity_type}_master.json` or `{entity_type}s.json`

**Examples:**
- ✅ `responsibilities_master.json`
- ✅ `departments.json`
- ✅ `professions.json`
- ✅ `Actions_Master.json`

---

## Part 4: Implementation Plan

### Phase 1: Verification & Analysis (Completed ✅)

**Tasks:**
- [x] List all LIBRARIES top-level folders
- [x] List all TASK_MANAGERS/PROMPTS folders
- [x] Read key documentation files
- [x] Identify all inconsistencies
- [x] Grep for reference patterns

### Phase 2: File & Folder Standardization

#### Task 2.1: Rename Inconsistent Folders

**Action:** Rename `Research Prompts` to `Research_Prompts`

```bash
mv "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS\Research Prompts" \
   "C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\PROMPTS\Research_Prompts"
```

**Files to Update After Rename:**
- PROMPTS_INDEX.json (category paths)
- README.md (category listings)
- Any files referencing "Research Prompts" folder

#### Task 2.2: Verify Root-Level Library Files

**Actions:**
1. Read `actions.json`, `objects.json`, `tools.json`
2. Compare with organized data in Responsibilities/ and Tools/
3. Determine: Are they indexes, duplicates, or legacy?
4. Decision:
   - If indexes → Update with clear references
   - If duplicates → Archive or delete
   - If legacy → Move to Archive/

#### Task 2.3: Update LIBRARIES README.md

**Changes Needed:**
- Remove Section 12 "Prompts [MOVED]" or update to correct location
- Add clear cross-reference: "See TASK_MANAGERS/PROMPTS for prompt library"
- Update all file structure diagrams
- Verify all sub-entity paths are current

### Phase 3: Path Reference Updates

#### Task 3.1: Update PROMPTS_INDEX.json

**Changes:**
- Update `file_path` for all prompts in "Research Prompts" → "Research_Prompts"
- Verify all paths are relative and accurate
- Update migration_info if needed

**Estimated Files to Update:** 1 file

#### Task 3.2: Update TASK_MANAGERS/PROMPTS README.md

**Changes:**
- Update folder structure diagram
- Fix any "Research Prompts" references
- Verify all cross-references to LIBRARIES paths

**Estimated Files to Update:** 1 file

#### Task 3.3: Systematic Path Reference Audit

**Process:**
1. Extract all LIBRARIES path references from 128 files
2. Categorize by reference type:
   - `LIBRARIES/Responsibilities/`
   - `LIBRARIES/DEPARTMENTS/`
   - `LIBRARIES/Professions/`
   - `LIBRARIES/Tools/`
3. Verify each path exists and is current
4. Create update script for batch path corrections

**Estimated Files to Update:** 20-40 files (est. 30% need updates)

### Phase 4: Documentation Updates

#### Task 4.1: Create LIBRARIES Cross-Reference Guide

**New File:** `LIBRARIES/CROSS_REFERENCE_GUIDE.md`

**Contents:**
- Current folder structure with descriptions
- How to reference from TASK_MANAGERS
- How to reference from other entities
- Common path patterns
- Migration history summary

#### Task 4.2: Update Architecture Documentation

**Files to Update:**
- `TASK_MANAGERS/PROMPTS/Architecture_Learning_Guide.md`
- `TASK_MANAGERS/PROMPTS/Architecture_Merge_Planning_Prompt.md`
- Any System_Analysis prompts referencing old structure

### Phase 5: Validation & Testing

#### Task 5.1: Path Validation Script

**Create:** `ENTITIES/validate_paths.py`

**Function:**
- Scan all .md and .json files
- Extract path references
- Verify paths exist
- Report broken links
- Generate correction suggestions

#### Task 5.2: Manual Verification

**Process:**
- Test 5-10 prompts end-to-end
- Verify they can locate referenced LIBRARIES files
- Check README accuracy
- Confirm no broken cross-references

---

## Part 5: Priority Recommendations

### High Priority (Do First) 🔴

1. **Rename `Research Prompts` → `Research_Prompts`**
   - Impact: Low risk, high consistency gain
   - Time: 5 minutes + update references
   - Blocker for: None

2. **Clarify root-level library files**
   - Impact: Prevents confusion, establishes source of truth
   - Time: 30-60 minutes analysis
   - Blocker for: Path reference decisions

3. **Update LIBRARIES README Section 12 (Prompts)**
   - Impact: Prevents misdirection
   - Time: 15 minutes
   - Blocker for: User navigation

### Medium Priority (Do Next) 🟡

4. **Update PROMPTS_INDEX.json paths**
   - Impact: Ensures catalog accuracy
   - Time: 10 minutes
   - Blocker for: Automated prompt loading

5. **Systematic path reference audit**
   - Impact: Fixes broken links
   - Time: 2-3 hours
   - Blocker for: System reliability

6. **Create Cross-Reference Guide**
   - Impact: Improves usability
   - Time: 1 hour
   - Blocker for: None

### Low Priority (Nice to Have) 🟢

7. **Path validation script**
   - Impact: Ongoing maintenance tool
   - Time: 2-4 hours development
   - Blocker for: None

8. **Architecture documentation updates**
   - Impact: Long-term accuracy
   - Time: 1-2 hours
   - Blocker for: None

---

## Part 6: Rollout Strategy

### Option A: Incremental Updates (Recommended)

**Approach:** Fix issues one by one with immediate testing

**Pros:**
- Lower risk of breaking changes
- Can validate each change
- Can pause/resume easily

**Cons:**
- Takes longer overall
- Multiple update sessions

**Timeline:** 3-5 work sessions over 1-2 days

### Option B: Batch Updates

**Approach:** Make all changes at once, then validate

**Pros:**
- Faster overall
- Single "update event"
- All changes synchronized

**Cons:**
- Higher risk if issues arise
- Harder to isolate problems
- Requires dedicated time block

**Timeline:** 1 intensive 4-6 hour session

---

## Part 7: Risk Assessment

### Low Risk Changes ✅

- Renaming `Research Prompts` folder
- Updating README documentation
- Creating new guide documents

### Medium Risk Changes ⚠️

- Moving/archiving root-level library files
- Batch updating path references in prompts
- PROMPTS_INDEX.json structure changes

### High Risk Changes 🔴

- Restructuring LIBRARIES top-level organization
- Changing core file naming patterns
- Breaking changes to established paths

**Mitigation:**
- Create backup before changes
- Document all changes in CHANGELOG
- Test thoroughly after each change
- Have rollback plan ready

---

## Part 8: Success Criteria

### Phase Completion Checklist

**Phase 2 Success:**
- [ ] No folders with spaces in TASK_MANAGERS/PROMPTS
- [ ] Root-level library files clarified (index/archive/delete)
- [ ] LIBRARIES README accurately describes structure

**Phase 3 Success:**
- [ ] PROMPTS_INDEX.json paths all valid
- [ ] 0 broken path references in critical prompts
- [ ] Path audit complete with <5% broken links

**Phase 4 Success:**
- [ ] Cross-Reference Guide created
- [ ] Architecture docs updated
- [ ] All READMEs accurate

**Phase 5 Success:**
- [ ] Path validation script works
- [ ] Manual testing passes
- [ ] No reported navigation issues

---

## Part 9: Next Steps

### Immediate Actions (Today)

1. Get approval for this plan
2. Create backup of current state
3. Start Phase 2, Task 2.1 (rename folder)
4. Update PROMPTS_INDEX.json
5. Update TASK_MANAGERS/PROMPTS README.md

### This Week

1. Complete Phase 2 (Standardization)
2. Complete Phase 3 (Path References)
3. Create Cross-Reference Guide

### Next Week

1. Complete Phase 4 (Documentation)
2. Develop validation script
3. Full system test

---

## Part 10: Questions for Review

Before proceeding, please confirm:

1. **Folder Rename:** OK to rename `Research Prompts` → `Research_Prompts`?
2. **Root Files:** Should `actions.json`, `objects.json`, `tools.json` be:
   - Kept as master indexes with pointers?
   - Moved to Archive/?
   - Deleted as duplicates?
3. **Priority:** Should we follow Option A (Incremental) or Option B (Batch)?
4. **Scope:** Any other naming conventions or paths you want standardized?

---

## Appendix A: File Counts

### LIBRARIES Structure
- DEPARTMENTS/: Unknown (needs verification)
- Professions/: 17+ JSON files
- Responsibilities/: 193 responsibilities across 8 departments
- Tools/: 75 tools across 13 categories

### TASK_MANAGERS/PROMPTS Structure
- Total Categories: 10 folders
- Total Prompts (indexed): 13 prompts
- Total Files with LIBRARIES references: 128 files

---

## Appendix B: Path Reference Examples

### Current References Found (Sample)

**From Architecture_Learning_Guide.md:**
```markdown
Actions/Actions_Master.json
Objects/Agentic_Engineering_Objects.json
Responsibilities/Core/responsibilities_master.json
```

**From Video Processing Prompts:**
```markdown
LIBRARIES/Tools/
LIBRARIES/Objects/
LIBRARIES/Actions/
```

### Recommended Standard Format

**From TASK_MANAGERS/PROMPTS to LIBRARIES:**
```markdown
../../LIBRARIES/Responsibilities/Core/responsibilities_master.json
../../LIBRARIES/DEPARTMENTS/departments.json
../../LIBRARIES/Tools/AI_Tools/Claude.json
```

**From LIBRARIES to TASK_MANAGERS:**
```markdown
../TASK_MANAGERS/PROMPTS/Video_Processing/
../TASK_MANAGERS/Task_Templates/
```

---

**Document Created:** 2025-11-17
**Created By:** Claude AI Assistant
**Status:** Ready for Review and Approval
**Next Update:** After Phase 2 completion
