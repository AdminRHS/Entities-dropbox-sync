# GDS-011: Entity Mapping Tutorial

**Version:** 1.0
**Created:** 2025-11-22
**Department:** AI Department (AID)
**Category:** Tutorial
**Estimated Read Time:** 12 minutes
**Priority:** High - Recommended for all employees

---

## Overview

Master the art of entity mapping! This tutorial teaches you how to correctly assign entity codes (PRT, MLT, TST, STP) to your work activities.

**What you'll learn:**
- The 4-level template hierarchy
- How to find the right entity code
- When to use PRT vs MLT vs TST vs STP
- Validation techniques
- Common mapping scenarios

**Who needs this guide:**
- All employees (basic understanding)
- Team leads (advanced mapping)
- Project managers (full hierarchy)

---

## Table of Contents

1. [Understanding the Entity Hierarchy](#understanding-the-entity-hierarchy)
2. [The 4 Entity Types Explained](#the-4-entity-types-explained)
3. [How to Find Entity Codes](#how-to-find-entity-codes)
4. [Mapping Decision Tree](#mapping-decision-tree)
5. [Common Scenarios](#common-scenarios)
6. [Validation Checklist](#validation-checklist)
7. [Advanced Topics](#advanced-topics)
8. [Quick Reference](#quick-reference)

---

## Understanding the Entity Hierarchy

### The Big Picture

Think of entity codes as an organizational filing system with 4 levels:

```
ORGANIZATION
    │
    └── PROJECT (PRT-###)
            │
            └── MILESTONE (MLT-###)
                    │
                    └── TASK (TST-###)
                            │
                            └── STEP (STP-###)
```

### Real-World Analogy

```
Building a House (Project)
    │
    ├── Foundation Complete (Milestone)
    │       │
    │       └── Pour Concrete (Task)
    │               │
    │               └── Mix cement, Set forms, Pour, Level (Steps)
    │
    └── Framing Complete (Milestone)
            │
            └── Build Walls (Task)
                    │
                    └── Measure, Cut, Assemble, Secure (Steps)
```

### In Our Company

```
PRT-001: Daily Report Collection (Project)
    │
    ├── MLT-001: Weekly Report Compilation (Milestone)
    │       │
    │       └── TST-042: Daily Report Submission (Task)
    │               │
    │               ├── STP-127: Whisper Flow Initialization (Step)
    │               ├── STP-128: Activity Logging Format (Step)
    │               ├── STP-089: Entity ID Assignment (Step)
    │               └── STP-090: Entity Validation (Step)
    │
    └── MLT-002: Monthly Report Aggregation (Milestone)
```

---

## The 4 Entity Types Explained

### 1. PROJECT (PRT-###)

**What it is:** Large initiatives that span weeks or months

**Characteristics:**
- Has a clear start and end
- Multiple people involved
- Contains several milestones
- Strategic importance

**Examples:**
- PRT-001: Daily Report Collection
- PRT-002: Content Creation Pipeline
- PRT-003: Template Management System
- PRT-004: System Architecture Overhaul
- PRT-005: Social Media Management

**When to use PRT codes:**
- Planning a major initiative
- Setting quarterly goals
- Defining department-wide efforts
- Organizing cross-functional work

**Time scale:** Weeks to months

---

### 2. MILESTONE (MLT-###)

**What it is:** Major checkpoints within a project

**Characteristics:**
- Marks significant progress
- Contains multiple tasks
- Has deliverables
- Gates for project phases

**Examples:**
- MLT-001: Weekly Report Compilation
- MLT-002: Monthly Report Aggregation
- MLT-005: Task Validation
- MLT-007: Quality Assurance
- MLT-008: Template Review & Approval

**When to use MLT codes:**
- Tracking project phases
- Defining deliverables
- Setting checkpoints
- Measuring progress

**Time scale:** Days to weeks

---

### 3. TASK (TST-###)

**What it is:** Specific activities you do daily or weekly

**Characteristics:**
- Clear objective
- Can be completed in one session or day
- Assigned to one person (usually)
- Concrete deliverable

**Examples:**
- TST-042: Daily Report Submission
- TST-043: Whisper Flow Recording
- TST-044: Entity Mapping Validation
- TST-101: Social Media Post Creation
- TST-018: Entity Classification

**When to use TST codes:** ⭐ **MOST COMMON FOR DAILY LOGS**
- Logging daily work
- Assigning specific activities
- Tracking time on tasks
- Describing what you actually did

**Time scale:** Hours to 1-2 days

---

### 4. STEP (STP-###)

**What it is:** Granular sub-tasks within a task

**Characteristics:**
- Very specific action
- Part of a larger task
- Often sequential
- Quick to complete

**Examples:**
- STP-127: Whisper Flow Initialization
- STP-128: Activity Logging Format
- STP-089: Entity ID Assignment
- STP-090: Entity Validation Rules
- STP-150: Template Metadata Documentation

**When to use STP codes:**
- Breaking down complex tasks
- Creating checklists
- Documenting procedures
- Process optimization

**Time scale:** Minutes to 1 hour

---

## How to Find Entity Codes

### Method 1: Search by Name 🔍

**For Task codes (most common):**

1. Navigate to `ENTITIES/TASK_MANAGERS/TSM-003/`
2. Look for file matching your activity
3. Code is in filename: `TST-XXX_[Task_Name].md`

**Example:**
```
Looking for: "Daily report submission"
Find: TST-042_Daily_Report_Submission.md
Code: TST-042
```

### Method 2: Ask AI Assistant 🤖

**With Claude:**
```
User: "What is the task code for creating social media posts?"
Claude: "TST-101: Social Media Post Creation"
```

**With Gemini:**
```
User: "Entity code for video editing?"
Gemini: "TST-XXX: Video Editing Task (check TSM-003 for exact code)"
```

### Method 3: Browse by Department 📂

**Structure:**
```
TASK_MANAGERS/
├── TSM-001/  ← Project Templates (PRT-###)
├── TSM-002/  ← Milestone Templates (MLT-###)
├── TSM-003/  ← Task Templates (TST-###)
└── TSM-004/  ← Step Templates (STP-###)
```

**Find your department's tasks:**
1. Open `TSM-003/`
2. Filter files by department prefix in description
3. Or use file explorer search: "design" "video" "sales"

### Method 4: Check Common Codes List 📋

**Frequently Used Task Codes:**

**Daily Operations:**
- TST-042: Daily Report Submission
- TST-043: Whisper Flow Recording
- TST-044: Entity Mapping Validation
- TST-045: Activity Time Tracking

**Content Creation:**
- TST-101: Social Media Post Creation
- TST-102: Content Template Application
- TST-103: Multi-Channel Posting

**Entity Management:**
- TST-018: Entity Classification
- TST-019: Entity Relationship Mapping
- TST-067: Task-to-Milestone Linking
- TST-089: Template Hierarchy Navigation

**Template Management:**
- TST-001: Template Creation Workflow
- TST-015: Template Documentation Standards
- TST-023: Cross-Reference Validation

---

## Mapping Decision Tree

Use this flowchart to decide which entity type to use:

```
START: What are you mapping?
    │
    ├─→ A large multi-week initiative?
    │   └─→ YES → Use PRT-### (Project)
    │
    ├─→ A major checkpoint or phase?
    │   └─→ YES → Use MLT-### (Milestone)
    │
    ├─→ A specific task you're doing today/this week?
    │   └─→ YES → Use TST-### (Task) ⭐ MOST COMMON
    │
    └─→ A small sub-step within a task?
        └─→ YES → Use STP-### (Step)
```

### Quick Decision Guide

| Question | Answer | Use |
|----------|--------|-----|
| How long will this take? | Weeks-Months | PRT |
| How long will this take? | Days-Weeks | MLT |
| How long will this take? | Hours-Days | TST ⭐ |
| How long will this take? | Minutes-Hour | STP |
| | | |
| How many people involved? | Team/Department | PRT |
| How many people involved? | Small group | MLT |
| How many people involved? | Mostly just me | TST ⭐ |
| How many people involved? | Just me, one action | STP |
| | | |
| What's the scope? | Strategic initiative | PRT |
| What's the scope? | Major deliverable | MLT |
| What's the scope? | Specific activity | TST ⭐ |
| What's the scope? | Tiny action | STP |

---

## Common Scenarios

### Scenario 1: Daily Report Submission

**Your activity:** Filled out my daily log and submitted it

**Mapping decision:**
- ❌ Not a project (not multi-week)
- ❌ Not a milestone (not a major checkpoint)
- ✅ **Is a task** (specific daily activity)
- ❌ Not just a step (more than one small action)

**Correct code:** TST-042 (Daily Report Submission)

---

### Scenario 2: Video Course Creation

**Your activity:** Created a complete video course on Gemini

**Mapping decision:**
- ✅ Could be a project (if multi-week with team)
- ✅ Could be milestone (if part of larger content project)
- ✅ **Most likely a task** (if you completed in 1-3 days)

**Depends on context:**
- If part of "Q1 Course Library Project" → MLT-XXX (Course Creation Milestone)
- If standalone weekly task → TST-XXX (Course Creation Task)

**Best practice:** Map to the most specific level you know exists

---

### Scenario 3: Image Resizing

**Your activity:** Resized 5 course images using Firefly

**Mapping decision:**
- ❌ Not a project
- ❌ Not a milestone
- ✅ **Is a task** (specific work activity)
- ⚠️ Could be step if part of larger task

**Correct code:**
- If standalone activity → TST-XXX (Image Creation/Editing)
- If part of "Course Cover Creation" task → STP-XXX (Image Resize Step)

**For daily logs:** Use task-level (TST) unless you're tracking very detailed steps

---

### Scenario 4: Client Meeting

**Your activity:** 1-hour meeting with client to discuss requirements

**Mapping decision:**
- ✅ **Is a task** (specific meeting activity)
- Might be part of larger project, but log the task

**Correct code:** TST-XXX (Client Meeting) or TST-XXX (Requirements Gathering)

**Pro tip:** If unsure of exact code, describe clearly:
```
TST-TBD (Client Requirements Meeting - Project Alpha)
```

---

### Scenario 5: Multi-Day Project Work

**Your activity:** Worked on redesigning the homepage (day 2 of 4)

**How to map:**
- The overall "Homepage Redesign" → PRT-XXX or MLT-XXX
- Today's specific work → TST-XXX (UI Design Task)

**In your daily log:**
```
**Entity:** TST-XXX (Homepage UI Design)
**Part of:** MLT-XXX (Homepage Redesign Milestone)

**What I worked on today:**
- Designed navigation menu (continued from yesterday)
- Created 3 layout variations
- Presented to team for feedback
```

---

## Validation Checklist

### Before Submitting Your Daily Log

Use this checklist to validate your entity mappings:

```
✅ Entity Code Format
   □ Follows pattern: XXX-### (e.g., TST-042)
   □ Uses correct prefix (PRT/MLT/TST/STP)
   □ Number is 3 digits (001-999)

✅ Appropriate Level
   □ Using TST for most daily activities
   □ Using PRT/MLT only for actual projects/milestones
   □ STP used sparingly for very granular tracking

✅ Code Exists
   □ Code matches a real template file
   □ Or marked as TBD for validation

✅ Relationship Makes Sense
   □ Task belongs to appropriate milestone
   □ Milestone belongs to appropriate project
   □ Hierarchy is logical

✅ Description Clarity
   □ Activity description matches entity name
   □ Clear what you actually did
   □ Outcomes documented
```

### Common Validation Errors

| Error | Example | Fix |
|-------|---------|-----|
| Wrong level | Used PRT for daily activity | Change to TST |
| Typo in code | TST-42 (missing zero) | Use TST-042 |
| Non-existent code | TST-999 | Find correct code or use TST-TBD |
| Too granular | STP for normal task | Change to TST |
| Too broad | TST for multi-week project | Change to PRT or MLT |

---

## Advanced Topics

### Mapping Activities Across Multiple Entities

**Situation:** Your activity touches multiple projects or tasks

**Solution:** Choose the primary entity

**Example:**
```markdown
**Primary Entity:** TST-042 (Daily Report Submission)
**Related Entities:**
- TST-043 (Whisper Flow Recording)
- TST-044 (Entity Mapping Validation)

**What I worked on:**
- Submitted daily report (primary)
- Recorded activities with Whisper Flow (supporting)
- Validated entity codes (supporting)
```

### When Codes Don't Exist Yet

**Situation:** You're working on something new without a template

**Options:**

**Option 1: Use TBD**
```
TST-TBD (Homepage Redesign - Design Phase)
```

**Option 2: Use Closest Match**
```
TST-015 (Template Documentation) ← Close enough for website docs
```

**Option 3: Request New Code**
```
Submit to AI Department:
"Need task code for: Homepage Redesign Design Work"
```

### Hierarchical Mapping

**Understanding parent-child relationships:**

```
When you map to TST-042:
    ↓
System knows:
    ├── Parent: MLT-001 (Weekly Report Compilation)
    ├── Grandparent: PRT-001 (Daily Report Collection)
    └── Children: STP-127, STP-128, STP-089, STP-090
```

**You only need to specify one level** (usually TST), the system infers the rest.

---

## Quick Reference

### Entity Code Patterns

```
PRT-###  Projects        (Weeks-Months)
MLT-###  Milestones      (Days-Weeks)
TST-###  Tasks           (Hours-Days) ⭐ USE THIS FOR DAILY LOGS
STP-###  Steps           (Minutes-Hours)
```

### When in Doubt

```
1. Default to TST (Task level) for daily logs
2. Describe your work clearly
3. Mark as TST-TBD if unsure of exact code
4. AI Department will validate during processing
```

### Finding Codes

```
Location: ENTITIES/TASK_MANAGERS/
    ├── TSM-001/  PRT codes
    ├── TSM-002/  MLT codes
    ├── TSM-003/  TST codes ⭐ LOOK HERE FIRST
    └── TSM-004/  STP codes
```

### Most Common Codes (Memorize These!)

```
TST-042  Daily Report Submission
TST-043  Whisper Flow Recording
TST-044  Entity Mapping Validation
TST-101  Social Media Post Creation
TST-018  Entity Classification
```

---

## Practice Exercises

### Exercise 1: Map These Activities

Try mapping these activities. Answers at the bottom.

1. "Created 3 Instagram posts for product launch"
2. "Reviewed Q1 marketing strategy with team"
3. "Fixed a typo in the homepage header"
4. "Completed video editing for client testimonial"
5. "Attended daily standup meeting"

<details>
<summary>Click for answers</summary>

1. TST-101 (Social Media Post Creation)
2. MLT-XXX (Q1 Marketing Strategy) or PRT-XXX if entire initiative
3. STP-XXX (Header Text Edit) or TST-XXX (Website Maintenance)
4. TST-XXX (Video Editing Task)
5. TST-042 (Daily Report) or TST-XXX (Team Meeting)

Remember: Multiple valid answers depending on context!
</details>

---

## Next Steps

### After This Tutorial

1. **Practice** - Map your next 3 daily activities
2. **Reference** - Bookmark this guide for quick lookup
3. **Ask** - Reach out to AI Department with questions
4. **Review** - Check your department reports for mapping accuracy

### Additional Resources

- **GDS-010:** Quick Start PMT-032 - Daily reporting basics
- **GDS-012:** Template Cross-Reference Guide - Deep dive into template relationships
- **TSM-003:** All task template files - Browse available codes
- **CRM_ENTITIES_LLM_TAXONOMY_GUIDE:** Advanced entity classification

---

## Support

**Questions about entity mapping?**
- AI Department: [Contact info]
- Your Team Lead
- Daily report feedback

**Found an error in this guide?**
- Submit feedback to AI Department
- Suggest improvements via documentation repo

---

## Metadata

**Guide Code:** GDS-011
**Version:** 1.0
**Created:** 2025-11-22
**Department:** AI Department
**Category:** Tutorial
**Scope:** multi_template
**Priority:** High
**Status:** Active

**Tags:** #intermediate #tutorial #entity_mapping #taxonomy #miro

**Related Templates:**
- PRT-001: Daily Report Collection [Recommended]
- MLT-005: Task Validation [Required]
- MLT-007: Quality Assurance [Recommended]
- TST-042: Daily Report Submission [Recommended]
- TST-044: Entity Mapping Validation [Required]
- TST-018: Entity Classification [Required]
- TST-067: Task-to-Milestone Linking [Recommended]
- TST-089: Template Hierarchy Navigation [Recommended]
- STP-089: Entity ID Assignment [Required]
- STP-090: Entity Validation Rules [Required]

**Available Formats:**
- 📄 Markdown (Primary) - This file
- 🎥 Video Tutorial (12 min) - [To be created]
- 🎨 Interactive Miro Board - [To be created]

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md`
**Maintained By:** AI Department
**Last Updated:** 2025-11-22
