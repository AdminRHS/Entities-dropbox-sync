# Department Prompts Documentation Session Log

**Date:** December 25, 2025  
**Session Type:** Documentation and Mapping  
**Duration:** ~30 minutes  
**Status:** Completed

---

## Session Overview

This session focused on identifying and documenting all department-specific daily report prompts, creating comprehensive index files, and mapping their locations and usage within the Nov25 department folder structure.

---

## Task Request

**Initial Request:**
1. Identify and put prompts in a file in `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts`
2. After updating department prompts, find a list of where those prompts are located inside department folders in `C:\Users\Dell\Dropbox\Nov25`

---

## Actions Taken

### 1. Exploration Phase
- Listed contents of Department_Prompts folder
- Identified 11 department prompt files (PMT-033 through PMT-043)
- Explored Nov25 folder structure
- Searched for prompt references across department folders

### 2. File Creation Phase

#### Created: `Department_Prompts_Index.md`
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts\Department_Prompts_Index.md`

**Contents:**
- Comprehensive index of all 11 department prompts
- Department overviews (mission, team size, key focus areas)
- Prompt log locations
- Report output paths
- Common structure documentation
- Integration points
- Usage workflow

**Prompts Documented:**
- PMT-033: AI Department Daily Report
- PMT-034: Content Department Daily Report
- PMT-035: Design Department Daily Report
- PMT-036: Dev Department Daily Report
- PMT-037: Finance Department Daily Report
- PMT-038: HR Department Daily Report
- PMT-039: LG Department Daily Report
- PMT-040: Marketing Department Daily Report
- PMT-041: Sales Department Daily Report
- PMT-042: SMM Department Daily Report
- PMT-043: Video Department Daily Report

#### Created: `Prompt_Locations_in_Nov25.md`
**Location:** `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\DEPARTMENTS\Daily_Reports\Department_Prompts\Prompt_Locations_in_Nov25.md`

**Contents:**
- Detailed mapping of prompt references by department
- Main prompt file locations (MAIN PROMPT v4.md)
- Prompt log file locations and references
- Generated reports locations
- Employee file references
- Workflow integration files
- Common integration patterns
- Missing or incomplete integrations

---

## Key Findings

### Department Prompt Integration Status

**Fully Integrated Departments:**
- ✅ **AI Nov25** - Complete integration with MAIN PROMPT v4.md, prompt log, and reports
- ✅ **Design Nov25** - Complete integration with extensive employee file references
- ✅ **Dev Nov25** - Complete integration with workflow files
- ✅ **Video Nov25** - Complete integration with team meeting processing
- ✅ **LG Nov25** - Complete integration with instruction files
- ✅ **HR Nov25** - Integration (uses MAIN PROMPT v2.md instead of v4.md)
- ✅ **Finance Nov25** - Basic integration with reports

**Partially Integrated Departments:**
- ⚠️ **Content Nov25** - No prompt log found
- ⚠️ **SMM Nov25** - No prompt log found

**Missing Departments:**
- ❌ **Marketing Nov25** - No Nov25 folder found

### Common Integration Points

1. **MAIN PROMPT v4.md Files**
   - Location Pattern: `Nov25/{DEPARTMENT} Nov25/MAIN PROMPT v4.md`
   - Present in: AI, Design, Dev, Video, LG, Finance
   - HR uses MAIN PROMPT v2.md instead

2. **Prompt Log Files**
   - Location Pattern: `Nov25/{DEPARTMENT} Nov25/{DEPARTMENT} prompt log.md`
   - Present in: AI, Design, Dev, Video, LG, HR

3. **Reports Folders**
   - Location Pattern: `Nov25/{DEPARTMENT} Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
   - Present in: AI, Design, Dev, Video, LG, HR, Finance, Sales

4. **Video Transcript Processing Workflow Files**
   - Location Pattern: `Nov25/{DEPARTMENT} Nov25/Video_Transcript_Processing_Workflow_{DEPARTMENT}.md`
   - Present in: AI, Design, Dev, Video, LG

5. **QUICKSTART.md Files**
   - Common reference: "Review daily report prompt in LIBRARIES/prompts.json"
   - Present in: Design, Dev, Video, LG, HR, Content, SMM

### Notable References Found

**AI Department:**
- Multiple references in AI prompt log.md (lines 548, 750, 886, 975-1016, 1041, 1326, 1458, 1494)
- References to PROMPT_Daily_Report_Collection.md template structure
- Task development for department-specific daily prompts

**Design Department:**
- Extensive documentation in Skrypkar Vilhelm's daily_processed.md files
- Complete workflow documentation: daily.md → daily_processed.md → plans.md + task.md
- References to Cursor AI processing prompts stored in Discord

**HR Department:**
- Discussion about prompt daily collection and department-specific prompts
- References to DailyReport finalization tasks
- AI-assisted daily planning system training references

**LG Department:**
- Multiple instruction files referencing daily workflows
- Team Performance Analysis Prompt.md for daily performance analyses
- Daily analytics dashboards and daily updates in team lead instructions

---

## Files Created

1. **Department_Prompts_Index.md** (242 lines)
   - Comprehensive index of all department prompts
   - Integration documentation
   - Usage workflow

2. **Prompt_Locations_in_Nov25.md** (441 lines)
   - Detailed location mapping
   - Reference tracking
   - Integration status

---

## Workflow Documentation

### Daily Report Generation Workflow

1. **Source Data:**
   - Department prompt logs (`{DEPARTMENT} prompt log.md`)
   - Employee daily files (`{EMPLOYEE}/{DAY}/daily.md`)
   - Call transcripts (processed via MAIN PROMPT v4.md)

2. **Processing:**
   - Use MAIN PROMPT v4.md framework
   - Apply department-specific prompt (PMT-033 through PMT-043)
   - Follow PROMPT_Daily_Report_Collection.md template structure

3. **Output:**
   - Generated reports in `Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`
   - Processed files: `daily_processed.md` → `plans.md` + `task.md`

---

## Technical Details

### Search Operations Performed
- Directory listings: Department_Prompts folder, Nov25 root, department folders
- Codebase searches: Daily report prompts, department prompt references
- Grep searches: Pattern matching for prompt references across departments
- File reads: Sample prompt files, MAIN PROMPT files, prompt logs

### Tools Used
- `list_dir` - Directory exploration
- `codebase_search` - Semantic search for prompt references
- `grep` - Pattern matching for specific references
- `read_file` - Reading prompt files and logs
- `glob_file_search` - Finding files by pattern
- `write` - Creating documentation files

---

## Issues Encountered

1. **Grep Error:** Encountered error with "nul" file in Nov25 directory during grep operation
   - **Resolution:** Used alternative search methods

2. **Missing Prompt Logs:** Content and SMM departments don't have prompt log files
   - **Status:** Documented as incomplete integrations

3. **Version Mismatch:** HR department uses MAIN PROMPT v2.md instead of v4.md
   - **Status:** Documented in integration mapping

---

## Recommendations

1. **Create Missing Prompt Logs:**
   - Content Nov25: Create `Content prompt log.md`
   - SMM Nov25: Create `SMM prompt log.md`

2. **Standardize MAIN PROMPT Versions:**
   - Update HR Nov25 to use MAIN PROMPT v4.md for consistency

3. **Create Marketing Department Folder:**
   - If Marketing department exists, create Nov25 folder structure

4. **Documentation Maintenance:**
   - Update index files when new prompts are added
   - Update location mapping when folder structures change

---

## Session Outcomes

✅ **Completed:**
- Created comprehensive index of all department prompts
- Mapped all prompt locations and references in Nov25 folders
- Documented integration status for all departments
- Identified missing or incomplete integrations
- Created reusable documentation for future reference

✅ **Deliverables:**
- Department_Prompts_Index.md
- Prompt_Locations_in_Nov25.md

---

## Next Steps (If Needed)

1. Review created documentation files
2. Address missing prompt logs for Content and SMM departments
3. Standardize MAIN PROMPT versions across all departments
4. Create Marketing department structure if needed
5. Update documentation as new prompts or integrations are added

---

## Session Metadata

**Files Read:** 15+ files
- Department prompt files (PMT-033 through PMT-043)
- MAIN PROMPT v4.md files
- Prompt log files
- Sample reports
- Workflow files

**Files Created:** 2 files
- Department_Prompts_Index.md
- Prompt_Locations_in_Nov25.md

**Searches Performed:** 10+ searches
- Directory listings
- Codebase searches
- Grep pattern matches
- Glob file searches

**Departments Analyzed:** 11 departments
- AI, Content, Design, Dev, Finance, HR, LG, Marketing, Sales, SMM, Video

---

**Session End Time:** December 25, 2025  
**Status:** Successfully Completed  
**Documentation Quality:** Comprehensive

---

*End of Session Log*

