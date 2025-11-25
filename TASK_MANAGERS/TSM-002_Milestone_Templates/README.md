# Milestone Templates Directory

**Purpose:** Store reusable Milestone Template definitions

---

## Overview

This directory contains Milestone Template JSON files. Milestone Templates define the structure, deliverables, and success criteria for major checkpoints within projects.

---

## File Naming Convention

**Pattern:** `MIL-TEMPLATE-PROJ-{DEPT}-{PROJ_NUMBER}-{MIL_NUMBER}.json`

**Examples:**
- `MIL-TEMPLATE-PROJ-HR-001-001.json` - First milestone of HR Project Template 001
- `MIL-TEMPLATE-PROJ-SALES-001-002.json` - Second milestone of Sales Project Template 001

---

## Milestone Template Structure

Each Milestone Template file contains:
- **Milestone Template ID** - Unique identifier
- **Milestone Template Name** - Descriptive name
- **Parent Project Template** - Link to the Project Template this milestone belongs to
- **Milestone Details** - Description, deliverables, success criteria
- **Taxonomy** - Action, object, context
- **Structure** - Task Templates and dependencies
- **Metadata** - Status, source tracking

---

## Key Concepts

### Template vs. Instance

- **Milestone Templates** (this directory) - Reusable blueprints without tracking data
- **Milestone Instances** (in actual Projects) - Have tracking (target_date, actual_completion_date, status, is_completed, start_date, end_date, expected_hours)

### Hierarchy

```
Project Template
  └── Milestone Template 1
      └── Task Template 1
      └── Task Template 2
  └── Milestone Template 2
      └── Task Template 3
```

---

## Related Documentation

- **[Milestone_Templates_Checklist-Item-003.md](../Milestone_Templates_Checklist-Item-003.md)** - Master index of all Milestone Templates
- **[Project_Templates_Checklist-Item-003.md](../Project_Templates_Checklist-Item-003.md)** - Parent Project Templates
- **[TAXONOMY_GUIDELINES.md](../TAXONOMY_GUIDELINES.md)** - Taxonomy usage guidelines
- **[INDEX.md](../INDEX.md)** - Master entity index

---

**Last Updated:** November 25, 2025


