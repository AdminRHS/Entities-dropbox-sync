# Workflow Clustering Documentation

Welcome to the **Week 3 Workflow Clustering** documentation! This folder contains detailed flow analysis for all 50 workflow clusters extracted from Week 3 reports.

---

## Overview

The workflow clustering system organizes **501 tasks** into **50 logical workflows** based on:
- Project affinity (tasks belonging to the same project)
- Department grouping (tasks from the same department + category)
- Execution dependencies (sequential vs parallel execution)

---

## File Structure

### Source Files (in parent directory)

1. **[Workflow_Clustering.csv](../Workflow_Clustering.csv)**
   - Master workflow index with 50 clusters
   - Shows Task IDs but not task names
   - Original classification file

2. **[Workflow_Clustering_Enhanced.csv](../Workflow_Clustering_Enhanced.csv)**
   - **NEW!** Enhanced version with task names added
   - Includes `Task_Names` column for better understanding
   - Use this version for quick reference

3. **[Task_Template_Mapping.csv](../Task_Template_Mapping.csv)**
   - Complete task details (501 tasks)
   - Maps tasks to templates, departments, professions
   - Source of task names and metadata

### Documentation Files (this directory)

#### Planning Phase Workflows (10 files)

These are **project-based workflows** (WFC-001 through WFC-010) that represent strategic initiatives:

| File | Project | Tasks | Type | Hours |
|------|---------|-------|------|-------|
| [WFC-001_Develop_USER_Entities.md](WFC-001_Develop_USER_Entities.md) | PRT-005 | 1 | Parallel | 0.0h |
| [WFC-002_Prospects_Architecture_Improvement.md](WFC-002_Prospects_Architecture_Improvement.md) | PRT-009 | 6 | Sequential | 14.0h |
| [WFC-003_Populate_Business_Entity_from_Sales.md](WFC-003_Populate_Business_Entity_from_Sales.md) | PRT-010 | 1 | Parallel | 0.0h |
| [WFC-004_Find_historical_search_queries_file_on_Google_Drive.md](WFC-004_Find_historical_search_queries_file_on_Google_Drive.md) | PRT-011 | 15 | Sequential | 24.0h |
| [WFC-005_Document_scraping_system_(20%_checkpoint).md](WFC-005_Document_scraping_system_\(20%_checkpoint\).md) | PRT-012 | 13 | Sequential | 21.3h |
| [WFC-006_Create_Job_Sites_folder_in_ENTITIES_ACCOUNTS.md](WFC-006_Create_Job_Sites_folder_in_ENTITIES_ACCOUNTS.md) | PRT-013 | 5 | Sequential | 12.0h |
| [WFC-007_Deploy_v1.0_to_Vercel.md](WFC-007_Deploy_v1.0_to_Vercel.md) | PRT-014 | 12 | Parallel | 2.8h |
| [WFC-008_Teach_Vilhelm_video_parsing_workflow.md](WFC-008_Teach_Vilhelm_video_parsing_workflow.md) | PRT-015 | 10 | Parallel | 16.0h |
| [WFC-009_Document_current_AI_tools_tracking_system.md](WFC-009_Document_current_AI_tools_tracking_system.md) | PRT-016 | 7 | Parallel | 13.1h |
| [WFC-010_Design_single_task_page_layout.md](WFC-010_Design_single_task_page_layout.md) | PRT-017 | 6 | Parallel | 0.7h |

**Total:** 76 tasks, 83.9 hours

#### Execution Phase Workflow (1 summary file)

- **[Department_Workflows_Summary.md](Department_Workflows_Summary.md)**
  - Comprehensive overview of 40 execution workflows (WFC-011 through WFC-050)
  - Groups tasks by department and category
  - Shows quick wins, workload distribution, and execution recommendations
  - **Total:** 425+ tasks across 9 departments

---

## Understanding Workflow Types

### Sequential Workflows

Tasks must be completed **in order**, one after another:

```
Task 1 → Task 2 → Task 3 → Task 4
```

**Why sequential?**
- Each task depends on the output of the previous task
- Example: WFC-004 (Google Maps Scraping) - Must find queries → format them → build parser → test → deploy

**Execution:** Assign to one person or hand off between team members

### Parallel Workflows

Tasks can be completed **simultaneously** by different people:

```
Task 1 ─┐
Task 2 ─┼─→ All complete → Project done
Task 3 ─┘
```

**Why parallel?**
- Tasks are independent or loosely coupled
- Example: WFC-007 (Deploy Dashboard) - UI fixes, feature additions, and documentation can happen at the same time

**Execution:** Distribute across team members based on skills

---

## How to Use These Documents

### For Project Managers

1. **Start with Planning Phase workflows** (WFC-001 to WFC-010)
   - These represent your 10 strategic projects for Week 3
   - Each file shows the complete task flow for one project
   - Use these to track project progress milestone by milestone

2. **Review Department_Workflows_Summary.md**
   - See workload distribution across departments
   - Identify departments that are overloaded
   - Spot quick wins to build momentum

3. **Track completion**
   - Mark tasks as completed in each workflow document
   - Update project status when all tasks in a workflow are done

### For Department Heads

1. **Find your department in Department_Workflows_Summary.md**
   - See all workflows assigned to your department
   - Check task counts and estimated hours
   - Identify quick wins to prioritize

2. **Review specific workflows**
   - Each workflow section lists tasks with their IDs
   - Use Task IDs to look up full details in Task_Template_Mapping.csv
   - Assign tasks to team members based on skills and workload

### For Team Members

1. **Find tasks assigned to you**
   - Your department head will reference workflow IDs and task IDs
   - Look up the workflow document to see context
   - Check if the workflow is Sequential (wait for previous tasks) or Parallel (start immediately)

2. **Understand dependencies**
   - Sequential workflows: Complete tasks in order
   - Parallel workflows: Check for implicit dependencies before starting
   - Milestone dependencies: Some workflows are blocked until a milestone completes

---

## Quick Reference: Workflow Clusters

### Planning Phase (Project-Based)

| WFC ID | Project | Type | Key Focus |
|--------|---------|------|-----------|
| WFC-001 | PRT-005 | Parallel | USER entity development |
| WFC-002 | PRT-009 | Sequential | Prospects CRM improvement |
| WFC-003 | PRT-010 | Parallel | Business entity population |
| WFC-004 | PRT-011 | Sequential | Google Maps scraping system |
| WFC-005 | PRT-012 | Sequential | Reviews scraping & analysis |
| WFC-006 | PRT-013 | Sequential | Job Sites entity creation |
| WFC-007 | PRT-014 | Parallel | HR Attendance Dashboard v1.0 |
| WFC-008 | PRT-015 | Parallel | Vilhelm onboarding & training |
| WFC-009 | PRT-016 | Parallel | AI tools management system |
| WFC-010 | PRT-017 | Parallel | Task Manager dashboard UI |

### Execution Phase (Department + Category Based)

| Department | Workflows | Total Tasks | Total Hours |
|------------|-----------|-------------|-------------|
| AI | 9 workflows | 228 tasks | 19.1h |
| Design | 5 workflows | 62 tasks | 32.3h |
| Development | 5 workflows | 31 tasks | 39.0h |
| Finance | 4 workflows | 24 tasks | 56.0h |
| HR | 5 workflows | 84 tasks | 84.0h |
| Lead Generation | 1 workflow | 6 tasks | 3.0h |
| Sales | 5 workflows | 40 tasks | 112.7h |
| SMM | 2 workflows | 36 tasks | 36.0h |
| Video | 4 workflows | 11 tasks | 60.0h |

---

## Understanding Task Connections

### How Tasks Connect to Form Workflows

Tasks are grouped into workflows using three methods:

**1. Project Affinity**
- Tasks with the same `Related_Project_ID` are grouped together
- Example: All tasks for PRT-011 (Google Maps Scraping) form WFC-004
- Result: 10 project-based workflows (WFC-001 to WFC-010)

**2. Department + Category Grouping**
- Tasks from the same department doing the same type of work
- Example: All "AI - Development" tasks form WFC-012
- Result: 40 department-category workflows (WFC-011 to WFC-050)

**3. Milestone Dependencies**
- Some workflows depend on completing specific milestones first
- Example: WFC-002 is blocked by MLT-022, WFC-004 blocked by MLT-033
- Check `Milestone_Dependencies` field before starting

### Task Hierarchy

```
PROJECT (PRT-###)
  ↓
MILESTONE (MLT-###) ← Dependency checkpoint
  ↓
WORKFLOW CLUSTER (WFC-###) ← This documentation level
  ↓
TASK (TSK-###) ← Individual work items
  ↓
STEP (STP-###) ← Execution instructions (in Task Templates)
```

---

## Completion Tracking

### How to Track Progress

1. **Individual Task Level**
   - Mark tasks as completed in Task_Template_Mapping.csv
   - Update status: Planned → In Progress → Completed

2. **Workflow Level**
   - Track completion percentage: `(Completed Tasks / Total Tasks) × 100`
   - Example: WFC-004 has 15 tasks. If 5 are done: 33% complete

3. **Project Level**
   - A project is complete when all its workflow clusters are done
   - Example: PRT-011 is complete when WFC-004 is 100% complete

4. **Department Level**
   - Use Department_Workflows_Summary.md to track department progress
   - Calculate: `(Completed Tasks / Total Department Tasks) × 100`

### Progress Indicators

- 🟢 **Green (0-25% complete):** Just started
- 🟡 **Yellow (26-75% complete):** In progress
- 🔴 **Red (76-99% complete):** Almost done, push to finish!
- ✅ **Done (100% complete):** Workflow complete, move to next

---

## Tips for Effective Workflow Execution

### 1. Start with Quick Wins
Look for tasks marked with ⚡ in Department_Workflows_Summary.md. These are high-impact tasks that take <1 hour.

### 2. Respect Sequential Dependencies
For Sequential workflows, **never skip ahead**. Each task builds on the previous one.

### 3. Maximize Parallel Efficiency
For Parallel workflows, distribute tasks across team members to complete the workflow faster.

### 4. Check Milestone Blockers
Before starting a workflow, check if it has `Milestone_Dependencies`. If yes, wait until that milestone is completed.

### 5. Cross-Department Coordination
Some workflows involve multiple departments (e.g., WFC-002: AI, Design, Development, Lead Generation, Sales). Set up coordination meetings.

---

## File Maintenance

### Updating Workflow Status

When tasks are completed:
1. Update Task_Template_Mapping.csv with new status
2. Regenerate Workflow_Clustering_Enhanced.csv (if task names change)
3. Update workflow documents with completion checkmarks
4. Recalculate hours remaining

### Adding New Workflows

If new tasks are extracted from Week 4:
1. Run the workflow clustering algorithm
2. Generate new WFC-### documents
3. Update this README with new workflow links
4. Merge with existing workflows if they're related

---

## Questions?

**Q: Why are some task IDs followed by "..."?**
A: This indicates the task list is truncated for readability. See the individual workflow document for the full list.

**Q: What if a task appears in multiple workflows?**
A: This shouldn't happen with the current clustering algorithm. Each task belongs to exactly one workflow. If you see duplicates, report it.

**Q: How do I know which workflow to start first?**
A: Start with Planning Phase workflows (WFC-001 to WFC-010) as they represent strategic projects. Within those, prioritize by:
   1. Milestone dependencies (complete blockers first)
   2. Sequential workflows (they take longer due to serial execution)
   3. Business priority (ask project manager)

**Q: Can I change a Sequential workflow to Parallel?**
A: Only if the task dependencies allow it. Review each task to ensure it doesn't depend on the output of the previous task. Consult with the project lead before making changes.

---

## Version History

- **v1.0 (2025-11-26):** Initial workflow clustering documentation
  - Created 10 Planning Phase workflow documents
  - Created Department_Workflows_Summary.md for Execution Phase
  - Added enhanced CSV with task names
  - Total: 50 workflows, 501 tasks documented

---

**Last Updated:** November 26, 2025
**Maintained by:** AI Task Classification System
**Related Files:** [Workflow_Clustering.csv](../Workflow_Clustering.csv), [Task_Template_Mapping.csv](../Task_Template_Mapping.csv)
