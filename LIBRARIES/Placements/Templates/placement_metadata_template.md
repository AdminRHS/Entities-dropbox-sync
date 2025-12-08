# Placement Metadata Template

## Purpose
This template provides standardized placement metadata for all documentation files.

## When to Use
- All README.md files
- All task files (TASK-###)
- All execution files (EXC-###)
- All significant documentation files
- All system component files

## Template Format

```markdown
## Placement Metadata

📍 **Current Placement:** {full_relative_path_to_this_file}
📍 **Parent Placement:** {parent_folder_path}
📍 **Related Placements:**
- {related_file_1}
- {related_file_2}
- {related_file_3}

**Placement Type:** {absolute|relative|pattern}
**Placement Category:** {root|entity|system|task|execution|report|input|day|data}
**Symbol:** {appropriate_category_symbol}
```

## Example 1: Task File

```markdown
## Placement Metadata

📍 **Current Placement:** TASKS/TASK-001_AI_Voice_Agent.md
📍 **Parent Placement:** TASKS/
📍 **Related Placements:**
- CLARIFICATIONS/README.md (Q004 questions)
- AI_EXECUTIONS/EXC-004_Voice_Interface_Spec.md
- ENTITIES/Video/ (integration point)

**Placement Type:** relative
**Placement Category:** task
**Symbol:** 📌
```

## Example 2: System Component

```markdown
## Placement Metadata

📍 **Current Placement:** System/Workflows/SESSION_LIFECYCLE.md
📍 **Parent Placement:** System/Workflows/
📍 **Related Placements:**
- System/Workflows/CHECKLIST_SESSION_OPEN.md
- System/Workflows/CHECKLIST_SESSION_CLOSE.md
- SESSION_HANDOFF.md
- Reports/Daily/

**Placement Type:** relative
**Placement Category:** system
**Symbol:** ⚙️
**System ID:** SYS.60
```

## Example 3: Entity README

```markdown
## Placement Metadata

📍 **Current Placement:** ENTITIES/Libraries/Placements/README.md
📍 **Parent Placement:** ENTITIES/Libraries/Placements/
📍 **Related Placements:**
- Core/placement_master.json
- By_Type/ (all categorized placements)
- Integration/placement_mapping.json
- Symbols/placement_symbols.json
- Templates/placement_metadata_template.md

**Placement Type:** relative
**Placement Category:** entity
**Symbol:** 📚
**Entity Code:** LBS
**Entity ID:** ENT.LBS
```

## Example 4: Execution File

```markdown
## Placement Metadata

📍 **Current Placement:** AI_EXECUTIONS/EXC-012_Cleanup_Day_07_Files.md
📍 **Parent Placement:** AI_EXECUTIONS/
📍 **Related Placements:**
- Week_01/07/ (target folder)
- Week_01/07/output/ (cleanup target)
- TASKS/TASK-010_Internal_Companies_Ecosystem.md (parent task)

**Placement Type:** relative
**Placement Category:** execution
**Symbol:** 🔧
**Input Placement:** Week_01/07/output/
**Output Placement:** Week_01/07/output/ (cleaned files)
```

## Example 5: Report File

```markdown
## Placement Metadata

📍 **Current Placement:** Reports/Daily/2025-12-08_session_1_report.md
📍 **Parent Placement:** Reports/Daily/
📍 **Related Placements:**
- SESSION_HANDOFF.md
- Execution/chat_log.md
- Week_01/08/output/

**Placement Type:** relative
**Placement Category:** report
**Symbol:** 📊
**Report Date:** 2025-12-08
**Session Number:** 1
```

## Field Definitions

### Required Fields

| Field | Description | Format |
|-------|-------------|--------|
| Current Placement | Full relative path to this file | `folder/subfolder/file.ext` |
| Parent Placement | Parent folder path | `folder/subfolder/` |
| Related Placements | List of related files/folders | Bulleted list with descriptions |
| Placement Type | Type classification | `absolute`, `relative`, or `pattern` |
| Placement Category | Category classification | See categories below |
| Symbol | Visual indicator | Emoji symbol |

### Optional Fields

| Field | Description | When to Use |
|-------|-------------|-------------|
| System ID | System component ID | For System/ files (SYS.30, SYS.40, etc.) |
| Entity Code | Entity code | For ENTITIES/ files (LBS, VID, HR, etc.) |
| Entity ID | Full entity ID | For ENTITIES/ files (ENT.LBS, etc.) |
| Input Placement | Input data location | For executions that read data |
| Output Placement | Output data location | For tasks/executions that create files |
| Report Date | Report date | For Reports/ files (YYYY-MM-DD) |
| Session Number | Session number | For session reports (1, 2, 3...) |

### Placement Categories

- `root` - Top-level system placements
- `entity` - ENTITIES/ hierarchy
- `system` - System/ hierarchy
- `task` - TASKS/ files
- `execution` - AI_EXECUTIONS/ files
- `report` - Reports/ files
- `input` - USER_INPUTS/, CLARIFICATIONS/ files
- `day` - Week_##/##/ files
- `data` - Data storage files
- `tracking` - Session tracking files

### Placement Types

- `absolute` - Full system path (C:\Users\Dell\Dropbox\...)
- `relative` - Path relative to root (ENTITIES/Libraries/...)
- `pattern` - Template pattern (Week_{week}/{day}/)

## Integration with Tools

### automation-agent
The automation-agent can:
- Auto-detect placement metadata from file paths
- Suggest appropriate symbols based on category
- Validate metadata completeness
- Generate metadata sections automatically

### File Monitor (SKL.04)
When implemented, file monitor will:
- Detect when placement metadata is missing
- Suggest corrections for incorrect placements
- Track file movements and update references

## Best Practices

1. **Always include placement metadata** in README files and significant documentation
2. **Keep related placements updated** when file relationships change
3. **Use correct symbols** based on placement category
4. **Be specific with descriptions** in related placements (don't just list the filename)
5. **Include optional fields** when relevant (System ID, Entity Code, Input/Output placements)
6. **Use relative placements** unless absolute path is required
7. **Follow date format** YYYY-MM-DD for all dates
8. **Update metadata** when files are moved or reorganized

## Validation Checklist

- [ ] Current Placement matches actual file location
- [ ] Parent Placement is correct parent folder
- [ ] Related Placements includes all key dependencies
- [ ] Placement Type is accurate (absolute/relative/pattern)
- [ ] Placement Category matches folder hierarchy
- [ ] Symbol is appropriate for category
- [ ] Optional fields included where relevant
- [ ] All paths use forward slashes (/) not backslashes
- [ ] Relative paths are from Dropbox root

## Common Mistakes to Avoid

❌ **Don't use backslashes:**
```
Current Placement: ENTITIES\Libraries\Placements\README.md
```

✅ **Use forward slashes:**
```
Current Placement: ENTITIES/Libraries/Placements/README.md
```

❌ **Don't use absolute paths without reason:**
```
Current Placement: C:\Users\Dell\Dropbox\ENTITIES\Libraries\Placements\README.md
```

✅ **Use relative paths from root:**
```
Current Placement: ENTITIES/Libraries/Placements/README.md
```

❌ **Don't omit placement descriptions:**
```
Related Placements:
- placement_master.json
- placement_types.json
```

✅ **Include descriptions:**
```
Related Placements:
- Core/placement_master.json (master catalog)
- Core/placement_types.json (type definitions)
```
