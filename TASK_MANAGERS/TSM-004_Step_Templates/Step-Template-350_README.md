# Step Templates Directory

**Purpose:** Store reusable Step Template JSON files that define standardized step structures for Task Templates.

---

## Overview

Step Templates define individual steps that belong to Task Templates. They specify:
- Step execution details (action, instructions, duration)
- Tool requirements
- Input/output specifications
- Dependencies and relationships with other steps
- Success criteria

---

## File Naming Convention

**Pattern:** `[Step_Name]_[Parent_Task_ID]_Template.json`

**Examples:**
- `Select_Job_Template_TASK-TEMPLATE-001_Template.json`
- `Fill_Position_Details_TASK-TEMPLATE-001_Template.json`
- `Review_Approval_TASK-TEMPLATE-001_Template.json`

---

## ID Format

**Pattern:** `TEMPLATE-STEP-[TASK_ID]-[NUMBER]`

**Examples:**
- `TEMPLATE-STEP-TASK-TEMPLATE-001-001` - First step of Task Template TASK-TEMPLATE-001
- `TEMPLATE-STEP-TASK-TEMPLATE-001-002` - Second step of Task Template TASK-TEMPLATE-001
- `TEMPLATE-STEP-TASK-TEMPLATE-002-001` - First step of Task Template TASK-TEMPLATE-002

**Important:** Step Templates must always reference a parent Task Template. The task ID in the step ID refers to the parent Task Template ID.

---

## Template Structure

Step Templates follow the structure defined in `DATA_EXTRACTION_PROMPT.md`. See [Step_Templates_Checklist-Item-003.md](../Step_Templates_Checklist-Item-003.md) for the complete JSON schema.

---

## Relationships

Step Templates are organized hierarchically:

```
Task Template (TASK-TEMPLATE-001)
  ├── Step Template 1 (TEMPLATE-STEP-TASK-TEMPLATE-001-001)
  ├── Step Template 2 (TEMPLATE-STEP-TASK-TEMPLATE-001-002)
  │   └── depends on Step Template 1
  └── Step Template 3 (TEMPLATE-STEP-TASK-TEMPLATE-001-003)
      └── parallel with Step Template 2
```

---

## Usage

1. Identify the parent Task Template (must exist first)
2. Create a new Step Template JSON file in this directory
3. Assign a unique ID following the pattern above
4. Link to parent Task Template in the JSON
5. Add entry to [Step_Templates_Checklist-Item-003.md](../Step_Templates_Checklist-Item-003.md)
6. Update [INDEX.md](../INDEX.md)

**Important:** Step Templates must reference an existing Task Template. Create the Task Template first if it doesn't exist.

---

## Example

For Task Template `TASK-TEMPLATE-001` (Create Job Posting), you might create:
- `TEMPLATE-STEP-TASK-TEMPLATE-001-001` - Select job template
- `TEMPLATE-STEP-TASK-TEMPLATE-001-002` - Fill in position details
- `TEMPLATE-STEP-TASK-TEMPLATE-001-003` - Define skills and requirements
- etc.

---

## Related Files

- [Step_Templates_Checklist-Item-003.md](../Step_Templates_Checklist-Item-003.md) - Index of all Step Templates
- [Task_Templates_Checklist-Item-003.md](../Task_Templates_Checklist-Item-003.md) - Index of parent Task Templates
- [INDEX.md](../INDEX.md) - Master index for TASK_MANAGERS entity

---

**Last Updated:** November 25, 2025  
**Maintained By:** Framework Architecture Team


