# GDS-012: Template Cross-Reference Guide

**Version:** 1.0
**Created:** 2025-11-22
**Department:** AI Department (AID)
**Category:** Reference
**Estimated Read Time:** 15 minutes
**Priority:** Medium - Recommended for understanding system architecture

---

## Overview

Understand how guides, templates, and workflows connect across the TASK_MANAGERS system. This reference guide explains cross-referencing patterns, navigation strategies, and best practices.

**What you'll learn:**
- How templates reference each other
- Guide-to-template relationships
- Navigation across the hierarchy
- Creating new cross-references
- Maintaining reference integrity

**Who needs this guide:**
- Template creators
- Documentation writers
- Team leads managing workflows
- Anyone curious about system architecture

---

## Table of Contents

1. [Cross-Reference Fundamentals](#cross-reference-fundamentals)
2. [Template Hierarchy Relationships](#template-hierarchy-relationships)
3. [Guide-to-Template Links](#guide-to-template-links)
4. [Navigation Patterns](#navigation-patterns)
5. [Creating Cross-References](#creating-cross-references)
6. [Validation & Maintenance](#validation--maintenance)
7. [Best Practices](#best-practices)
8. [Reference Tables](#reference-tables)

---

## Cross-Reference Fundamentals

### What is a Cross-Reference?

A cross-reference is a **link between two related entities** in our system:

```
Entity A ←→ Entity B
  (references)
```

**Types of cross-references:**
1. **Template ↔ Template** - Parent-child hierarchy
2. **Guide ↔ Template** - Documentation for templates
3. **Guide ↔ Guide** - Related documentation
4. **Template ↔ Tool** - Tools used in template
5. **Template ↔ Department** - Ownership and responsibility

### Why Cross-Reference?

**Benefits:**
- ✅ **Discoverability** - Find related content easily
- ✅ **Context** - Understand how pieces fit together
- ✅ **Navigation** - Move through hierarchy efficiently
- ✅ **Validation** - Verify relationships are correct
- ✅ **Documentation** - Self-documenting system

**Example:**
```
User viewing: TST-042 (Daily Report Submission)
    ↓
System shows:
    ↑ Parent: MLT-001 (Weekly Report Compilation)
    ↑ Grandparent: PRT-001 (Daily Report Collection)
    ↓ Children: STP-127, STP-128, STP-089, STP-090
    📖 Guides: GDS-010, GDS-011
    🛠 Tools: Whisper Flow, Claude, Gemini
```

---

## Template Hierarchy Relationships

### The 4-Level Structure

```
Level 1: PROJECT (PRT)
    │
    ├─→ Level 2: MILESTONE (MLT)
    │       │
    │       └─→ Level 3: TASK (TST)
    │               │
    │               └─→ Level 4: STEP (STP)
```

### Parent-Child References

**Every template should reference:**
- ⬆️ **Parent** (the level above it)
- ⬇️ **Children** (the level below it)

**Example Template File: TST-042**

```markdown
# TST-042: Daily Report Submission

## Parent Templates
- **Milestone:** MLT-001 (Weekly Report Compilation)
- **Project:** PRT-001 (Daily Report Collection)

## Child Templates (Steps)
1. STP-127: Whisper Flow Initialization
2. STP-128: Activity Logging Format
3. STP-089: Entity ID Assignment
4. STP-090: Entity Validation

## Related Tasks
- TST-043: Whisper Flow Recording (prerequisite)
- TST-044: Entity Mapping Validation (optional)
```

### Relationship Types

#### 1. Hierarchical (Parent-Child)

**Definition:** Strict hierarchy from Project → Milestone → Task → Step

**Rules:**
- Each child has ONE primary parent
- Parents can have MULTIPLE children
- Hierarchy must be maintained

**Example:**
```
PRT-001 (Daily Report Collection)
    ├── MLT-001 (Weekly Report Compilation)
    │   ├── TST-042 (Daily Report Submission)
    │   │   ├── STP-127 (Whisper Flow Init)
    │   │   ├── STP-128 (Activity Logging)
    │   │   └── STP-089 (Entity ID Assignment)
    │   └── TST-043 (Whisper Flow Recording)
    └── MLT-002 (Monthly Report Aggregation)
```

#### 2. Sequential (Order Dependencies)

**Definition:** Templates that must be done in order

**Notation:**
```
TST-001 → TST-002 → TST-003
(prerequisite) (next) (after)
```

**Example:**
```
TST-043 (Whisper Flow Recording)
    ↓ Must complete before
TST-042 (Daily Report Submission)
    ↓ Must complete before
TST-044 (Entity Mapping Validation)
```

#### 3. Related (Sibling References)

**Definition:** Templates at same level that are related

**Example:**
```
TST-101 (Social Media Post Creation)
    ↔ Related to
TST-102 (Content Template Application)
    ↔ Related to
TST-103 (Multi-Channel Posting)
```

#### 4. Optional Dependencies

**Definition:** Templates that can optionally reference each other

**Example:**
```
TST-042 (Daily Report Submission)
    ⤷ Optionally uses
TST-045 (Activity Time Tracking)
```

---

## Guide-to-Template Links

### How Guides Reference Templates

**Relevance Levels:**
- **Required** - Must read before using template
- **Recommended** - Should read for best practices
- **Optional** - Additional context available

### Cross-Reference Matrix

**Example: GDS-010 (Quick Start PMT-032)**

```
Template Level    Template Code    Relevance
──────────────────────────────────────────────
Project           PRT-001          Required
Milestone         MLT-001          Recommended
Milestone         MLT-002          Recommended
Task              TST-042          Required
Task              TST-043          Required
Task              TST-044          Recommended
Task              TST-045          Recommended
Step              STP-127          Required
Step              STP-128          Required
Step              STP-129          Recommended
Step              STP-130          Recommended
```

**Total:** 11 template links across all 4 hierarchy levels

### Multi-Level Coverage

**Pattern:** A single guide can provide value at multiple hierarchy levels

**Example: GDS-011 (Entity Mapping)**

```
Level 1 (Project):
    PRT-001 [Recommended]
    Context: "Entity mapping applies to all daily report activities"

Level 2 (Milestone):
    MLT-005 [Required]
    Context: "Task validation milestone - critical for entity mapping"

Level 3 (Task):
    TST-042, TST-044, TST-018 [Required/Recommended]
    Context: Specific entity mapping tasks

Level 4 (Step):
    STP-089, STP-090 [Required]
    Context: Granular entity ID assignment steps
```

**Benefit:** User sees guide at every relevant level with appropriate context

---

## Navigation Patterns

### Pattern 1: Top-Down (Project → Step)

**Use case:** Planning a new project

**Navigation flow:**
```
1. Start at PRT-001 (Daily Report Collection)
2. View milestones: MLT-001, MLT-002
3. Select milestone: MLT-001 (Weekly Report)
4. View tasks: TST-042, TST-043
5. Select task: TST-042 (Daily Report)
6. View steps: STP-127, STP-128, STP-089
```

**At each level, see:**
- Related guides (GDS-010, GDS-011)
- Required tools (Whisper Flow, Claude)
- Department ownership (AID)

---

### Pattern 2: Bottom-Up (Step → Project)

**Use case:** Understanding context of current work

**Navigation flow:**
```
1. Currently on: STP-089 (Entity ID Assignment)
2. View parent task: TST-042 (Daily Report Submission)
3. View parent milestone: MLT-001 (Weekly Report Compilation)
4. View parent project: PRT-001 (Daily Report Collection)
```

**At each level, see:**
- Why this work matters
- Broader context
- Related work at same level

---

### Pattern 3: Lateral (Sibling Navigation)

**Use case:** Exploring related tasks

**Navigation flow:**
```
Currently on: TST-042 (Daily Report Submission)
    ↓
See siblings under MLT-001:
    - TST-043 (Whisper Flow Recording)
    - TST-044 (Entity Mapping Validation)
    - TST-045 (Activity Time Tracking)
```

---

### Pattern 4: Guide-First Navigation

**Use case:** Learning new process

**Navigation flow:**
```
1. Search for: "How to submit daily reports"
2. Find guide: GDS-010 (Quick Start PMT-032)
3. Guide shows related templates:
    - PRT-001 [Required]
    - TST-042 [Required]
    - STP-127, STP-128 [Required]
4. Click template to see details
5. Template shows other guides
```

**Circular navigation enabled:**
```
Guide → Template → Guide → Template
```

---

## Creating Cross-References

### Adding Template References

**In a Task Template File:**

```markdown
# TST-XXX: Your Task Name

## Parent Templates
- **Milestone:** MLT-XXX (Milestone Name)
- **Project:** PRT-XXX (Project Name)

## Child Templates (Steps)
1. STP-XXX: Step Name
2. STP-YYY: Another Step

## Related Tasks
- TST-AAA: Related Task Name (prerequisite)
- TST-BBB: Another Related Task (optional)

## Related Guides
- GDS-XXX: Guide Name [Required/Recommended/Optional]
  Context: "How this guide helps with this task"
```

### Adding Guide References

**In a Guide File:**

```markdown
# GDS-XXX: Your Guide Name

## Related Templates

### Project Templates
- PRT-XXX: Project Name [Required]
  "Why this guide is required for this project"

### Task Templates
- TST-XXX: Task Name [Recommended]
  "How this guide helps with this task"

### Step Templates
- STP-XXX: Step Name [Optional]
  "Additional context for this step"
```

### Link Format Standards

**Markdown links:**
```markdown
<!-- Relative path from current file -->
[TST-042: Daily Report Submission](../TSM-003/TST-042_Daily_Report_Submission.md)

<!-- With display order -->
1. [STP-127: Whisper Flow Init](../TSM-004/STP-127_Whisper_Flow_Init.md)
2. [STP-128: Activity Logging](../TSM-004/STP-128_Activity_Logging.md)
```

**Code references:**
```markdown
<!-- Just the code -->
Parent: PRT-001

<!-- Code with name -->
Parent: PRT-001 (Daily Report Collection)

<!-- Code with link -->
Parent: [PRT-001: Daily Report Collection](../TSM-001/PRT-001.md)
```

---

## Validation & Maintenance

### Cross-Reference Validation Checklist

```
✅ Template References
   □ All parent references exist
   □ All child references exist
   □ No orphaned templates (templates with no parent)
   □ No circular references (A→B→C→A)

✅ Guide References
   □ All template codes in guide exist
   □ Relevance level specified (Required/Recommended/Optional)
   □ Context provided for each reference
   □ Display order logical

✅ Link Integrity
   □ All markdown links work
   □ Relative paths are correct
   □ No broken links (404s)
   □ Files exist at specified paths

✅ Consistency
   □ Naming conventions followed
   □ Format standards applied
   □ Metadata complete
   □ Bidirectional links (A→B and B→A)
```

### Common Validation Errors

| Error | Example | Fix |
|-------|---------|-----|
| Missing parent | TST-042 has no MLT reference | Add parent milestone |
| Wrong hierarchy | TST links directly to PRT | Link through MLT |
| Broken link | Path `../TSM-003/TST-999.md` doesn't exist | Update to correct path |
| Missing reciprocal | PRT-001 lists MLT-001, but MLT-001 doesn't list PRT-001 | Add reciprocal reference |
| Typo in code | TST-42 instead of TST-042 | Use correct format (3 digits) |

### Automated Validation

**Future database implementation:**
```sql
-- Check for orphaned tasks (no parent milestone)
SELECT * FROM task_templates
WHERE id NOT IN (
  SELECT task_id FROM milestone_task_links
);

-- Check for broken guide links
SELECT * FROM guide_task_templates
WHERE task_template_code NOT IN (
  SELECT template_code FROM task_templates
);
```

---

## Best Practices

### 1. Always Link Bidirectionally

**Bad:**
```
PRT-001 lists MLT-001 as child
MLT-001 doesn't mention PRT-001 as parent ❌
```

**Good:**
```
PRT-001 lists MLT-001 as child ✅
MLT-001 lists PRT-001 as parent ✅
```

### 2. Provide Context for Every Link

**Bad:**
```markdown
Related Guide: GDS-010
```

**Good:**
```markdown
Related Guide:
- GDS-010: Quick Start PMT-032 [Required]
  "Essential reading before submitting first daily report.
   Covers Whisper Flow setup and entity mapping basics."
```

### 3. Use Consistent Naming

**Template files:**
```
TSM-003/TST-042_Daily_Report_Submission.md ✅
TSM-003/DailyReportSubmission.md ❌
```

**References in text:**
```
TST-042: Daily Report Submission ✅
Task 42 (daily reports) ❌
```

### 4. Maintain Display Order

**Logical ordering:**
```markdown
## Steps (in execution order)
1. STP-127: Whisper Flow Initialization (do first)
2. STP-128: Activity Logging (do second)
3. STP-089: Entity ID Assignment (do third)
4. STP-090: Entity Validation (do last)
```

### 5. Update All References When Changing Templates

**When renaming TST-042 → TST-042A:**
1. Update the template file name
2. Update all parent templates listing TST-042
3. Update all child templates listing TST-042
4. Update all guides referencing TST-042
5. Update all cross-reference maps

### 6. Document Breaking Changes

**When removing a template:**
```markdown
## Deprecated Notice
**TST-999** has been deprecated as of 2025-11-20.
Please use **TST-042** instead.

All references updated in:
- PRT-001
- MLT-001
- GDS-010
```

---

## Reference Tables

### Template Cross-Reference Matrix

**See:** `Cross_Reference_Maps/XREF_Guides_to_Templates_Matrix.md`

**Quick lookup:**

| Guide | PRT-001 | MLT-001 | TST-042 | STP-127 |
|-------|---------|---------|---------|---------|
| GDS-010 | R | r | R | R |
| GDS-011 | r | - | r | R |
| GDS-012 | - | - | - | - |

**Legend:** R = Required, r = Recommended, - = Not linked

---

### Hierarchy Navigation Quick Reference

```
From PROJECT (PRT):
    ↓ Children: Milestones (MLT)
    → Siblings: Other projects
    📖 Guides: Project-level guides

From MILESTONE (MLT):
    ↑ Parent: Project (PRT)
    ↓ Children: Tasks (TST)
    → Siblings: Other milestones in same project
    📖 Guides: Milestone-level guides

From TASK (TST):
    ↑ Parent: Milestone (MLT)
    ↑ Grandparent: Project (PRT)
    ↓ Children: Steps (STP)
    → Siblings: Other tasks in same milestone
    📖 Guides: Task-level guides

From STEP (STP):
    ↑ Parent: Task (TST)
    ↑ Grandparent: Milestone (MLT)
    ↑ Great-grandparent: Project (PRT)
    → Siblings: Other steps in same task
    📖 Guides: Step-level guides
```

---

### Common File Paths

```
Templates:
    TSM-001/PRT-XXX_[Name].md (Projects)
    TSM-002/MLT-XXX_[Name].md (Milestones)
    TSM-003/TST-XXX_[Name].md (Tasks)
    TSM-004/STP-XXX_[Name].md (Steps)

Guides:
    TSM-007_GUIDES/GDS-XXX_[Name].md

Cross-Reference Maps:
    TSM-007_GUIDES/Cross_Reference_Maps/
        XREF_Guides_to_Templates_Matrix.md
        XREF_Template_Hierarchy_Integration.md
        XREF_Department_Guide_Coverage.md

Database Preview:
    TSM-007_GUIDES/Database_Architecture_Preview/
        TABLE_guide_task_templates.md
        TABLE_guide_project_templates.md
        [... other tables]
```

---

## Examples in Practice

### Example 1: Complete Task Template with References

```markdown
# TST-042: Daily Report Submission

## Overview
Submit your daily activity log to the reporting system.

## Parent Templates
- **Milestone:** [MLT-001: Weekly Report Compilation](../TSM-002/MLT-001.md)
- **Project:** [PRT-001: Daily Report Collection](../TSM-001/PRT-001.md)

## Child Templates (Steps)
1. [STP-127: Whisper Flow Initialization](../TSM-004/STP-127.md)
2. [STP-128: Activity Logging Format](../TSM-004/STP-128.md)
3. [STP-089: Entity ID Assignment](../TSM-004/STP-089.md)
4. [STP-090: Entity Validation](../TSM-004/STP-090.md)

## Related Tasks
- [TST-043: Whisper Flow Recording](../TSM-003/TST-043.md) (prerequisite)
- [TST-044: Entity Mapping Validation](../TSM-003/TST-044.md) (optional)
- [TST-045: Activity Time Tracking](../TSM-003/TST-045.md) (recommended)

## Related Guides
- **[GDS-010: Quick Start PMT-032](../TSM-007_GUIDES/GDS-010.md)** [Required]
  Essential reading before first submission. Covers Whisper Flow setup,
  entity mapping, and submission workflow.

- **[GDS-011: Entity Mapping Tutorial](../TSM-007_GUIDES/GDS-011.md)** [Recommended]
  Deep dive into entity code assignment for accurate reporting.

## Tools Required
- Whisper Flow (transcription)
- Claude or Gemini (optional assistance)

## Department
AI Department (AID)

[... rest of template content ...]
```

---

### Example 2: Guide with Multi-Level Template References

```markdown
# GDS-010: Quick Start Guide - PMT-032 v2.1

## Related Templates

### Project Level
- **PRT-001: Daily Report Collection** [Required]
  This guide is essential for the entire Daily Report Collection project.
  All employees must read before participating in daily reporting.

### Milestone Level
- **MLT-001: Weekly Report Compilation** [Recommended]
  Understand how your daily reports feed into weekly compilations.

- **MLT-002: Monthly Report Aggregation** [Recommended]
  See the bigger picture of how daily work rolls up monthly.

### Task Level
- **TST-042: Daily Report Submission** [Required]
  The primary task this guide supports. Read before first submission.

- **TST-043: Whisper Flow Recording** [Required]
  Learn proper recording techniques for accurate transcription.

- **TST-044: Entity Mapping Validation** [Recommended]
  Ensure your entity codes are correct.

### Step Level
- **STP-127: Whisper Flow Initialization** [Required]
  Detailed setup instructions for Whisper Flow.

- **STP-128: Activity Logging Format** [Required]
  Proper format for logging activities.

[... rest of guide content ...]
```

---

## Next Steps

### After Reading This Guide

1. **Explore** - Navigate through some template hierarchies
2. **Practice** - Create cross-references in your next template
3. **Validate** - Check existing templates for broken links
4. **Document** - Add missing cross-references you discover

### Additional Resources

- **GDS-010:** Quick Start PMT-032 - Daily reporting basics
- **GDS-011:** Entity Mapping Tutorial - Understanding entity codes
- **Cross_Reference_Maps/** - Visual matrices and coverage analysis
- **Database_Architecture_Preview/** - Future database structure

---

## Support

**Questions about cross-referencing?**
- AI Department for technical guidance
- Your team lead for workflow-specific questions
- Documentation repo for improvement suggestions

**Found a broken link?**
- Report to AI Department
- Create issue in documentation system
- Suggest fix if you know it

---

## Metadata

**Guide Code:** GDS-012
**Version:** 1.0
**Created:** 2025-11-22
**Department:** AI Department
**Category:** Reference
**Scope:** global
**Priority:** Medium
**Status:** Active

**Tags:** #advanced #reference #templates #cross_reference

**Related Templates:**
- PRT-002: Content Creation Pipeline [Recommended]
- PRT-003: Template Management [Optional]
- MLT-008: Template Review & Approval [Optional]
- TST-001: Template Creation Workflow [Optional]
- TST-015: Template Documentation Standards [Optional]
- TST-023: Cross-Reference Validation [Recommended]
- STP-150: Template Metadata Documentation [Optional]
- STP-151: Cross-Reference Creation [Optional]

**Available Formats:**
- 📄 Markdown (Primary) - This file
- 📊 Notion Page - [To be created - interactive database view]

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-012_Template_Cross_Reference_Guide.md`
**Maintained By:** AI Department
**Last Updated:** 2025-11-22
