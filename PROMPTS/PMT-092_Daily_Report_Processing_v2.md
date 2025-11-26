# Daily Report Processing v2/v3 Workflow

**Purpose**: Process daily reports using MAIN PROMPT v4 and update plans/tasks files with processed output following versioned workflow patterns.

**Version**: 1.0  
**Date**: 2025-11-21  
**Status**: Active  
**Related Prompts**: PMT-001_Main_Prompt_v4.md  
**Replaces**: PMT-087_Daily_Report_Processing_Workflow.md (deprecated)

---

## Overview

This workflow processes daily report files using MAIN PROMPT v4, creates processed output files, and then updates plans.md and tasks.md files accordingly. The workflow has evolved through multiple versions (v2, v3) with refined processes.

**Primary Use Case**: Processing daily reports with MAIN PROMPT v4 integration  
**Target Platform**: Cursor/VS Code/Antigravity with Claude  
**Department**: DGN (Design)

---

## Prompt Instructions

### Version 2 Workflow

```
please process
[DAILY_FILE_PATH]
with
Design Nov25\MAIN PROMPT v4.md
then, after daily_processed file is created, update
[PLANS_FILE_PATH]
[TASKS_FILE_PATH]
with
[DAILY_PROCESSED_FILE_PATH]
```

### Version 3 Workflow

```
please process
[DAILY_FILE_PATH]
with
Design Nov25\MAIN PROMPT v4.md
then, after daily_processed file is created, update
[PLANS_FILE_PATH]
[TASKS_FILE_PATH]
with
daily_processed.md
```

**Note**: Version 3 uses relative path `daily_processed.md` instead of full path.

---

## Usage Workflow

### Step 1: Process Daily Report
1. Identify daily.md file path
2. Reference MAIN PROMPT v4 location
3. Execute processing prompt
4. Wait for `daily_processed.md` creation

### Step 2: Update Plans and Tasks
1. Verify `daily_processed.md` exists
2. Reference plans.md and tasks.md paths
3. Execute update prompt
4. Review updated files

---

## File Path Examples

### Version 2 Example
**Daily**: `Design Nov25\Skrypkar Vilhelm\17\daily.md`  
**MAIN PROMPT**: `Design Nov25\MAIN PROMPT v4.md`  
**Processed**: `Design Nov25\Skrypkar Vilhelm\17\daily_processed.md`  
**Plans**: `Design Nov25\Skrypkar Vilhelm\17\plans.md`  
**Tasks**: `Design Nov25\Skrypkar Vilhelm\17\task.md`

### Version 3 Example
**Daily**: `Design Nov25\Skrypkar Vilhelm\Week_3\20\daily.md`  
**MAIN PROMPT**: `Design Nov25\MAIN PROMPT v4.md`  
**Processed**: `daily_processed.md` (relative path)  
**Plans**: `Design Nov25\Skrypkar Vilhelm\Week_3\20\plans.md`  
**Tasks**: `Design Nov25\Skrypkar Vilhelm\Week_3\20\task.md`

---

## Expected Output Structure

### daily_processed.md
- **Content**: Processed daily report following MAIN PROMPT v4 structure
- **Format**: Structured sections as per MAIN PROMPT v4 template
- **Location**: Same folder as daily.md (or relative path in v3)

### plans.md Updates
- **Content**: Plans extracted from processed daily report
- **Structure**: Follows plans.md template format
- **Source**: Information from daily_processed.md

### tasks.md Updates
- **Content**: Tasks extracted from processed daily report
- **Structure**: Follows tasks.md template format
- **Source**: Information from daily_processed.md

---

## Version Differences

### Version 2
- Uses full path for daily_processed.md
- Explicit file path references

### Version 3
- Uses relative path `daily_processed.md`
- Assumes file in same directory
- More flexible for nested folder structures

---

## Best Practices

- ✅ Verify MAIN PROMPT v4 path is correct
- ✅ Ensure daily.md exists before processing
- ✅ Wait for daily_processed.md creation before updating plans/tasks
- ✅ Use version 3 format for nested folder structures
- ✅ Verify file paths are accessible
- ❌ Don't update plans/tasks before daily_processed.md exists
- ❌ Don't use wrong MAIN PROMPT version

---

## Dependencies

- **MAIN PROMPT v4**: Required for processing (PMT-001)
- **File Structure**: daily.md, plans.md, tasks.md must exist
- **Processing Tool**: Cursor/VS Code/Antigravity with Claude

---

## Version History

- v1.0 (2025-11-21): Initial integration from personal prompts collection
  - Includes both v2 and v3 workflow patterns

