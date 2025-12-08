# Placement Reference Template

## Purpose
This template shows how to reference placements in documentation, code comments, and task descriptions.

## Basic Reference Format

### Format 1: Simple Reference
```markdown
📍 {placement}
```

**Example:**
```markdown
📍 ENTITIES/Libraries/Placements/README.md
```

### Format 2: Labeled Reference
```markdown
📍 **{Label}:** {placement}
```

**Examples:**
```markdown
📍 **Placement:** ENTITIES/Libraries/Placements/README.md
📍 **Output Placement:** Reports/Daily/2025-12-08_session_1_report.md
📍 **Input Placement:** ACCOUNTS/Lead Accounts/
```

### Format 3: With Description
```markdown
📍 {placement} ({description})
```

**Examples:**
```markdown
📍 System/Workflows/SESSION_LIFECYCLE.md (5-phase workflow)
📍 CLARIFICATIONS/README.md (pending questions tracker)
📍 automation-agent/ (810 lines, needs testing)
```

### Format 4: Category Symbol + Placement
```markdown
{category_symbol} {placement}
```

**Examples:**
```markdown
⚙️ System/Workflows/SESSION_LIFECYCLE.md
📁 ENTITIES/Video/
📌 TASKS/TASK-001_AI_Voice_Agent.md
🔧 AI_EXECUTIONS/EXC-012_Cleanup_Day_07_Files.md
📊 Reports/Daily/2025-12-08_session_1_report.md
```

## In Task Lists

### With Reserved Words
```markdown
{RESERVED_WORD} at PLACEMENT: {placement}
```

**Examples:**
```markdown
CREATE file at PLACEMENT: System/Skills/SKL.05.md
EXECUTE script at PLACEMENT: automation-agent/test_agent.py
REVIEW document at PLACEMENT: Week_01/07/README.md
BUILD library at PLACEMENT: ENTITIES/Libraries/Placements/
MARK PLACEMENT as completed: TASKS/TASK-001_AI_Voice_Agent.md
```

### Action + Placement
```markdown
{action} → 📍 {placement}
```

**Examples:**
```markdown
Output → 📍 Reports/Daily/2025-12-08_integration_summary.md
Read from → 📍 ENTITIES/PROMPTS/Core/MAIN_PROMPT_v7.2.md
Write to → 📍 Week_01/08/output/LINES_159_174_ANALYSIS.md
Archive to → 📍 TASKS/_Archive/TASK-001_AI_Voice_Agent.md
```

## In Execution Files

### Input/Process/Output Format
```markdown
## Input
📍 **Input Placement:** {input_placement}
- Description of input data

## Process
1. Read from 📍 {input_placement}
2. Process data
3. Generate output

## Output
📍 **Output Placement:** {output_placement}
- Description of output
```

**Example:**
```markdown
## Input
📍 **Input Placement:** ACCOUNTS/Lead Accounts/
- LinkedIn export CSV files
- Contact data

## Process
1. Read from 📍 ACCOUNTS/Lead Accounts/Connections.csv
2. Parse and normalize data
3. Generate analysis report

## Output
📍 **Output Placement:** Week_01/08/output/linkedin_contacts_analysis.md
- Complete analysis with insights
- Contact categorization
- Next steps recommendations
```

## In Navigation Documents

### Directory Tree with Symbols
```markdown
📍 Root/
├── ⚙️ System/
│   ├── 📋 README.md
│   ├── Workflows/
│   │   └── SESSION_LIFECYCLE.md
│   └── Skills/
├── 📁 ENTITIES/
│   ├── 📚 Libraries/
│   │   ├── Placements/
│   │   └── Responsibilities/
│   └── 🎥 Video/
├── 📌 TASKS/
└── 📊 Reports/
```

### File Listings with Placements
```markdown
## Key Files

| Symbol | Placement | Description |
|--------|-----------|-------------|
| ⭐⚙️ | System/Workflows/SESSION_LIFECYCLE.md | 5-phase workflow (critical) |
| 📍 | SESSION_HANDOFF.md | Session bridge |
| 💬 | CLARIFICATIONS/README.md | Q&A tracker (16 questions) |
| 📌 | TASKS/TASK-010_Internal_Companies_Ecosystem.md | Internal companies (blocked) |
```

## In README Files

### Quick Start Section
```markdown
## 🎯 Quick Start - Where to Begin

**New to this folder?** Start here:

1. **📖 Read This First:** 📍 README.md ← You are here
2. **📋 What Happened:** 📍 output/FINAL_SUMMARY.md
3. **🗂️ See All Outputs:** 📍 output/INDEX.md
4. **📊 Execution Status:** 📍 output/SESSION_EXECUTION_SUMMARY.md
```

### File Organization Section
```markdown
## 📁 File Organization

### 📊 Summary Documents
- 📍 output/FINAL_SUMMARY.md - Complete day overview
- 📍 output/SESSION_EXECUTION_SUMMARY.md - Execution tracking
- 📍 output/INDEX.md - Complete file listing

### 📋 Cluster Documents
- 📍 output/cluster_01_libraries.md - Libraries discussion
- 📍 output/cluster_02_actions.md - Actions planning
- 📍 output/cluster_13_integration.md - Integration summary
```

## In Session Reports

### Session Context Section
```markdown
## Session Context

**📍 Working Directory:** C:\Users\Dell\Dropbox\
**📍 Current Day:** Week_01/08/
**📍 Processing File:** Week_01/07/output/07_wspr.md
**📍 Current Line:** 174

### Key Placements Accessed
- 📍 SESSION_HANDOFF.md (session priorities)
- 📍 Execution/chat_log.md (session history)
- 📍 CLARIFICATIONS/README.md (16 pending questions)
- 📍 ENTITIES/PROMPTS/Core/MAIN_PROMPT_v7.2.md (integrated principles)
```

### Files Created Section
```markdown
## Files Created This Session

1. ⚙️ **System/Workflows/SESSION_LIFECYCLE.md**
   - 5-phase workflow definition
   - 1,000+ lines

2. 📚 **ENTITIES/Libraries/Placements/README.md**
   - Placements library documentation
   - 600+ lines

3. 📊 **Reports/Daily/2025-12-08_session_1_report.md**
   - Session summary and progress
```

## In Code Comments

### Python Example
```python
# Read input from placement
# 📍 Input Placement: ACCOUNTS/Lead Accounts/Connections.csv
input_file = "ACCOUNTS/Lead Accounts/Connections.csv"

# Process data

# Write output to placement
# 📍 Output Placement: Week_01/08/output/analysis.md
output_file = "Week_01/08/output/analysis.md"
```

### Markdown Example
```markdown
<!-- PLACEMENT REFERENCE -->
<!-- 📍 Related Document: System/Workflows/SESSION_LIFECYCLE.md -->
<!-- 📍 See Also: CLARIFICATIONS/README.md -->

## Section Title
Content here...
```

## In Clarifications

### Question Format with Placement Context
```markdown
### Q010-A: Company Identification

**Question:** What internal companies exist in the system?

**Context:**
- 📍 Mentioned in: USER_INPUTS/2025-12-08_dictation.md
- 📍 Related Task: TASKS/TASK-010_Internal_Companies_Ecosystem.md
- 📍 Possible Data: ACCOUNTS/, ENTITIES/

**Impact:** CRITICAL - Blocks entire TASK-010

**Answer:** [User to provide]
```

## In Handoff Documents

### Priorities Section
```markdown
## 🔥 IMMEDIATE PRIORITIES

**CRITICAL:**
1. Answer Q010-A (Company Identification)
   - 📍 Blocks: TASKS/TASK-010_Internal_Companies_Ecosystem.md
   - 📍 Context: CLARIFICATIONS/README.md

**HIGH:**
1. Execute Icon/Emoji System (3-4 hours)
   - 📍 EXC-001: AI_EXECUTIONS/EXC-001_Icon_Library.md
   - 📍 EXC-002: AI_EXECUTIONS/EXC-002_Reserved_Words_Emoji_Map.md
   - 📍 Output: ENTITIES/Libraries/Icons/
```

## Pattern References

### Using Pattern Variables
```markdown
📍 Week_01/{day}/output/ where {day} = 06, 07, or 08

**Concrete Examples:**
- 📍 Week_01/06/output/
- 📍 Week_01/07/output/
- 📍 Week_01/08/output/
```

### Multiple Pattern Instances
```markdown
📍 TASKS/TASK-###_{Name}.md pattern

**Current Instances:**
- 📍 TASKS/TASK-001_AI_Voice_Agent.md
- 📍 TASKS/TASK-002_Media_Library.md
- 📍 TASKS/TASK-010_Internal_Companies_Ecosystem.md
```

## Relative vs Absolute References

### When to Use Relative
✅ **Internal system references** (most common)
```markdown
📍 ENTITIES/Libraries/Placements/README.md
📍 System/Workflows/SESSION_LIFECYCLE.md
📍 TASKS/TASK-001_AI_Voice_Agent.md
```

### When to Use Absolute
✅ **External references or root-level context**
```markdown
📍 C:\Users\Dell\Dropbox\
📍 C:\Users\Dell\Dropbox\ACCOUNTS\Lead Accounts\
```

### Parent References
✅ **Navigating up the hierarchy**
```markdown
📍 ../System/ (one level up, then into System)
📍 ../../ENTITIES/ (two levels up, then into ENTITIES)
📍 ../../../Reports/ (three levels up, then into Reports)
```

## Best Practices Summary

1. **Always use 📍 symbol** for placement references
2. **Add category symbols** for additional context (⚙️📁📌🔧📊💬)
3. **Include descriptions** in parentheses when helpful
4. **Use relative paths** unless absolute is required
5. **Format consistently** across all documents
6. **Update references** when files move
7. **Be specific** with descriptions
8. **Use PLACEMENT** reserved word in task lists
9. **Include placement metadata** in all significant files
10. **Follow naming conventions** (forward slashes, ISO dates, underscores)
