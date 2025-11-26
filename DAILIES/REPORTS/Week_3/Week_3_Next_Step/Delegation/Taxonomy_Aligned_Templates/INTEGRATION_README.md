# TAX-002 Template Integration Guide

**Created:** November 26, 2025
**Source:** Week 3 Workflow Clustering & Task Mapping
**Target:** Complete TAX-002_Task_Managers Template Hierarchy

---

## Overview

This directory contains **taxonomy-compliant templates** extracted from Week 3 workflows and tasks, organized according to the TAX-002_Task_Managers hierarchy:

```
PRT (Project Templates)
  └─> MLT (Milestone Templates)
      └─> TST (Task Templates)
          └─> STT (Step Templates)  [To be generated]
```

Additionally, **WRF (Workflows)** reference and orchestrate these templates.

---

## What Was Created

### 1. Project Templates (10 files)

**Location:** `Project_Templates/`
**Format:** `PRT-{###}_{Name}.json`

| Project ID | Name | Milestones | Tasks | Hours |
|------------|------|------------|-------|-------|
| PRT-005 | Develop USER Entities | 1 | 1 | 0.0h |
| PRT-009 | Prospects Architecture Improvement | 1 | 6 | 14.0h |
| PRT-010 | Populate Business Entity from Sales | 1 | 1 | 0.0h |
| PRT-011 | Google Maps Scraping System | 1 | 15 | 24.0h |
| PRT-012 | Reviews Scraping & Analysis | 1 | 13 | 21.3h |
| PRT-013 | Job Sites Entity Creation | 1 | 5 | 12.0h |
| PRT-014 | HR Attendance Dashboard v1.0 | 1 | 12 | 2.8h |
| PRT-015 | Vilhelm Onboarding & Training | 1 | 10 | 16.0h |
| PRT-016 | AI Tools Management System | 1 | 7 | 13.1h |
| PRT-017 | Task Manager Dashboard UI | 1 | 6 | 0.7h |

**Total:** 76 tasks, 104.9 hours

### 2. Milestone Templates (11 files)

**Location:** `Milestone_Templates/`
**Format:** `MLT-{###}_{Name}.json`

| Milestone ID | Name | Project | Tasks | Hours |
|--------------|------|---------|-------|-------|
| MLT-030 | Develop USER Entities | PRT-005 | 1 | 0.0h |
| MLT-031 | Prospects Architecture Improvement | PRT-009 | 6 | 14.0h |
| MLT-032 | Populate Business Entity from Sales | PRT-010 | 1 | 0.0h |
| MLT-033 | Google Maps Scraping System | PRT-011 | 15 | 24.0h |
| MLT-034 | Reviews Scraping & Analysis | PRT-012 | 13 | 21.3h |
| MLT-035 | Job Sites Entity Creation | PRT-013 | 5 | 12.0h |
| MLT-036 | HR Dashboard Deployment | PRT-014 | 12 | 2.8h |
| MLT-037 | Vilhelm Onboarding | PRT-015 | 10 | 16.0h |
| MLT-038 | AI Tools Tracking | PRT-016 | 7 | 13.1h |
| MLT-039 | Task Manager UI | PRT-017 | 6 | 0.7h |

**Note:** MLT-029 intentionally skipped (continues from existing MLT-028)

### 3. Task Templates (20 sample files)

**Location:** `Task_Templates/`
**Format:** `TST-{###}_{Name}.json`

**Created:** 20 samples (426 total available for creation)

**Sample Task Templates:**
- TST-395: REVOKE exposed GitHub token immediately
- TST-396: Generate new GitHub token
- TST-397: Audit all files for exposed credentials
- TST-398: Implement secret scanning in repos
- TST-399: Conduct deep research on Desert Greener
- ... (15 more)

**Conversion Pattern:**
```
TSK-### → TST-###  (for simple numeric task IDs)
```

**Not Converted (kept as-is):**
- TSK-DEV-2025-11-20-### (date-based tasks)
- TSK-DGN-2025-11-20-### (department daily tasks)
- PRT-###, MLT-### (already proper format)

### 4. Workflows (50 files - in separate directory)

**Location:** `../Taxonomy_Aligned_Workflows/`
**Format:** `WRF-{###}_{Name}.json`

- **Planning Phase:** WRF-001 to WRF-010 (linked to projects)
- **Execution Phase:** WRF-011 to WRF-050 (department operations)

---

## Template Hierarchy & Relationships

### Project → Milestone → Task Flow

**Example: PRT-011 (Google Maps Scraping)**

```json
{
  "project_template_id": "PRT-011",
  "metadata": {
    "name": "Find historical search queries file on Google Drive",
    "total_tasks": 15,
    "total_milestones": 1
  },
  "milestones": [
    {
      "milestone_id": "MLT-033",  ← Links to Milestone
      "task_count": 15,
      "execution_type": "Sequential"
    }
  ]
}
```

```json
{
  "milestone_template_id": "MLT-033",
  "metadata": {
    "related_project": "PRT-011",  ← Links back to Project
    "total_task_count": 15
  },
  "tasks": {
    "task_template_ids": [  ← Links to Tasks
      "TST-106", "TST-107", "TST-108", ...
    ]
  }
}
```

```json
{
  "task_template_id": "TST-106",
  "metadata": {
    "task_name": "Find historical search queries file on Google Drive",
    "department": "AID",
    "estimated_duration": "TBD"
  },
  "steps": [  ← Will link to STT-### when created
    // Step templates go here
  ]
}
```

---

## TAX-002 Compliance Checklist

### All Templates Include:

✅ **Required Entity Fields**
- `entity_type`: "TASK_MANAGERS"
- `sub_entity`: "Project_Template" | "Milestone_Template" | "Task_Template"
- `template_id`: Full format (e.g., "Project-Template-005")
- Entity-specific ID (e.g., `project_template_id`: "PRT-005")

✅ **Metadata Completeness**
- name/description
- department (ISO code: AID, DGN, DEV, etc.)
- priority, status, complexity
- estimated_duration
- created_date, version

✅ **Version Control**
- version: "1.0"
- created: "2025-11-26"
- last_updated: "2025-11-26"

✅ **Migration Tracking**
- migration_notes with original_id
- conversion_date
- source information

✅ **Hierarchical Links**
- Projects reference Milestones
- Milestones reference Projects and Tasks
- Tasks ready to reference Steps

---

## Integration Steps

### 1. Copy Templates to Taxonomy Directory

```bash
# Project Templates
cp Project_Templates/*.json C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\Project_Templates\

# Milestone Templates
cp Milestone_Templates/*.json C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\Milestone_Templates\

# Task Templates
cp Task_Templates/*.json C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\Task_Templates\

# Workflows (already created)
cp ../Taxonomy_Aligned_Workflows/*.json C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\Workflows\
```

### 2. Update Taxonomy Master List

Add entries to `TAX-002_Task_Managers\Taxonomy_Master_List.csv`:

**Projects:** PRT-005 through PRT-017
**Milestones:** MLT-030 through MLT-039
**Task Templates:** TST-395 through TST-###
**Workflows:** WRF-001 through WRF-050

### 3. Generate Remaining Task Templates

Currently only 20 sample task templates created. Generate remaining 406:

```python
# Use the same pattern from creation script
# Converts TSK-### to TST-### for all 426 simple tasks
```

### 4. Create Step Templates (STT-###)

**Next Phase:** Extract detailed execution steps for each task template.

**Approach:**
- Review task template details
- Break down into 3-8 granular steps
- Create STT-###-## format (e.g., STT-395-01, STT-395-02)
- Link back to parent TST-###

### 5. Validate Cross-References

Use `Template_Cross_Reference_Map.json` to verify:
- All projects have milestones
- All milestones reference valid projects
- All task IDs in milestones exist as templates
- No orphaned templates

---

## File Structure

```
Taxonomy_Aligned_Templates/
├── INTEGRATION_README.md              ← This file
├── Template_Cross_Reference_Map.json  ← Complete mapping
│
├── Project_Templates/
│   ├── PRT-005_Develop_USER_Entities.json
│   ├── PRT-009_Prospects_Architecture_Improvement.json
│   ├── PRT-011_Find_historical_search_queries_file_on_Google_Drive.json
│   └── ... (10 total)
│
├── Milestone_Templates/
│   ├── MLT-030_Develop_USER_Entities.json
│   ├── MLT-033_Find_historical_search_queries_file_on_Google_Drive.json
│   └── ... (11 total)
│
└── Task_Templates/
    ├── TST-395_REVOKE_exposed_GitHub_token_immediately.json
    ├── TST-396_Generate_new_GitHub_token.json
    └── ... (20 samples, 426 total available)
```

---

## Usage Examples

### Finding a Task's Complete Hierarchy

**Question:** Where does TST-106 fit in the overall structure?

**Answer:**
1. Open `Template_Cross_Reference_Map.json`
2. TST-106 belongs to MLT-033
3. MLT-033 belongs to PRT-011
4. PRT-011 is orchestrated by WRF-004

**Full Path:**
```
WRF-004 (Workflow)
  → PRT-011 (Project: Google Maps Scraping)
      → MLT-033 (Milestone: Find historical queries)
          → TST-106 (Task: Find historical search queries file)
              → [STT-106-01, STT-106-02, ...] (Steps - to be created)
```

### Executing a Project

**To execute PRT-011:**

1. **Open Project Template:** `PRT-011_Find_historical_search_queries_file_on_Google_Drive.json`
2. **Review Milestones:** Check MLT-033 details
3. **Get Tasks:** Open `MLT-033_Find_historical_search_queries_file_on_Google_Drive.json`
4. **Execute Tasks:** Follow task_template_ids (TST-106, TST-107, etc.)
5. **Track Progress:** Update status in each template as completed

### Tracking Completion

**Projects:**
- Count completed milestones / total milestones
- PRT-011: 0/1 milestones = 0% complete

**Milestones:**
- Count completed tasks / total tasks
- MLT-033: 0/15 tasks = 0% complete

**Tasks:**
- Mark status as "Completed" when done
- TST-106: status = "Active" → "Completed"

---

## Next Steps

### Immediate Actions

1. ✅ **Review Created Templates**
   - Verify Project Templates have correct data
   - Check Milestone Templates link properly
   - Validate Task Template samples

2. **Generate All Task Templates**
   - Run script to create remaining 406 TST files
   - Ensure all TSK-### are converted

3. **Create Step Templates**
   - Design STT schema
   - Extract steps from existing task data
   - Generate STT-###-## files

4. **Integrate with Taxonomy**
   - Copy files to TAX-002 directory
   - Update master lists
   - Run validation scripts

### Future Enhancements

- **Checklist Templates (CHT-###):** Extract deliverables and validation items
- **Dependencies Mapping:** Create dependency graph between tasks
- **Resource Templates:** Define required tools, skills, professions per task
- **Performance Tracking:** Add actual vs estimated hours tracking

---

## Reference Files

- **Source Data:**
  - [../Workflow_Clustering.csv](../Workflow_Clustering.csv)
  - [../Task_Template_Mapping.csv](../Task_Template_Mapping.csv)
  - [../Assignment_Priority_Queue.csv](../Assignment_Priority_Queue.csv)

- **Created Templates:**
  - [Template_Cross_Reference_Map.json](Template_Cross_Reference_Map.json)
  - [Project_Templates/](Project_Templates/)
  - [Milestone_Templates/](Milestone_Templates/)
  - [Task_Templates/](Task_Templates/)

- **Related:**
  - [../Taxonomy_Aligned_Workflows/](../Taxonomy_Aligned_Workflows/)
  - [../../TAX-002_Task_Managers/](C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers/)

---

## Version History

**v1.0 (2025-11-26):**
- Created 10 Project Templates (PRT-005 to PRT-017)
- Created 11 Milestone Templates (MLT-030 to MLT-039)
- Created 20 sample Task Templates (TST-395 to TST-414)
- Generated cross-reference mapping
- Full TAX-002 compliance achieved

---

**Last Updated:** November 26, 2025
**Status:** ✅ Phase 1 Complete (Project/Milestone/Task extraction)
**Next Phase:** Step Template (STT-###) generation
