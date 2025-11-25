# Daily Report Processing Workflow

**Purpose**: Process daily reports, translate to English, and update plans and tasks files using Cursor/Claude code assistant.

**Version**: 1.0  
**Date**: 2025-11-21  
**Status**: Deprecated  
**Replaced By**: PMT-092_Daily_Report_Processing_v2.md  
**Related Prompts**: PMT-001_Main_Prompt_v4.md, PMT-092_Daily_Report_Processing_v2.md

---

## ⚠️ Deprecation Notice

**This prompt is deprecated.** Please use **PMT-092_Daily_Report_Processing_v2.md** instead, which integrates with MAIN PROMPT v4 and provides improved workflow patterns (v2/v3).

**Reason for Deprecation**: PMT-092 provides better integration with MAIN PROMPT v4 and includes versioned workflow patterns that are more robust and maintainable.

---

## Overview

This workflow processes daily report files (daily.md) by translating content to English, filling in structured sections, and generating/updating plans.md and tasks.md files accordingly.

**Primary Use Case**: Processing daily call transcripts and generating structured outputs  
**Target Platform**: Cursor/VS Code with Claude code assistant  
**Department**: DGN (Design)

---

## Prompt Instructions

### Base Workflow

```
In the daily.md file, the path to which I attached below, you will find the transcript of the call. I need to process this transcript. Translate it to English, fill in the rest of the daily.md file according to the structure specified in it. Also, generate plans and tasks and enter this information into the plans.md and tasks.md files and fill them accordingly to the structure specified within these files

[Attach daily.md file path]
[Attach plans.md file path]
[Attach tasks.md file path]
```

### File Path Format

**Example Paths**:
- Daily: `Design Nov25\Skrypkar Vilhelm\04\daily.md`
- Plans: `Design Nov25\Skrypkar Vilhelm\04\plans.md`
- Tasks: `Design Nov25\Skrypkar Vilhelm\04\task.md`

---

## Usage Workflow

### Step 1: Prepare Files
1. Ensure `daily.md` exists with transcript content
2. Ensure `plans.md` exists with structure template
3. Ensure `tasks.md` exists with structure template

### Step 2: Execute Prompt
1. Open Cursor/VS Code
2. Attach all three file paths
3. Run the processing prompt
4. AI processes and updates files

### Step 3: Review Output
1. Verify translation accuracy
2. Check daily.md structure completion
3. Validate plans.md content
4. Validate tasks.md content

---

## Expected Output Structure

### daily.md Processing
- **Translation**: All content translated to English
- **Structure Completion**: All sections filled according to template
- **Content Extraction**: Key information extracted from transcript

### plans.md Generation
- **Plans Created**: Based on transcript content
- **Structure Compliance**: Follows template format
- **Prioritization**: Plans organized by priority

### tasks.md Generation
- **Tasks Created**: Action items extracted from transcript
- **Structure Compliance**: Follows template format
- **Status Assignment**: Tasks marked with appropriate status

---

## Examples

### Example Input
**Files**:
- `Design Nov25\Skrypkar Vilhelm\04\daily.md` (contains Ukrainian/Russian transcript)
- `Design Nov25\Skrypkar Vilhelm\04\plans.md` (empty template)
- `Design Nov25\Skrypkar Vilhelm\04\task.md` (empty template)

### Example Output
**daily.md**: Translated and structured with all sections filled  
**plans.md**: Contains plans extracted from transcript  
**tasks.md**: Contains tasks with status assignments

---

## Best Practices

- ✅ Ensure file paths are correct and accessible
- ✅ Verify template structures exist in plans.md and tasks.md
- ✅ Review translations for accuracy
- ✅ Validate extracted plans and tasks
- ❌ Don't process without template structures
- ❌ Don't skip file path verification

---

## Version History

- v1.0 (2025-11-21): Initial integration from personal prompts collection
- v1.0 (2025-11-21): **Deprecated** - Replaced by PMT-092_Daily_Report_Processing_v2.md

