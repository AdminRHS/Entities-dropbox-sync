# TASK_MANAGERS Entity Index
**Version:** 2.1
**Last Updated:** 2025-11-15
**Major Update:** First Project Instance Created (PROJ-AI-NMP-001 - Next Main Prompt v5)

---

## 📋 Quick Navigation

| Resource | Count | Location |
|----------|-------|----------|
| **Task Templates** | 22 | [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md) |
| **Project Templates** | 3 | [Project_Templates/Project_Templates_Checklist-Item-003.md](./Project_Templates/Project_Templates_Checklist-Item-003.md) |
| **Project Instances** | 1 | [Projects/](./Projects/) |
| **Milestone Instances** | 8 | In PROJ-AI-NMP-001/Milestones/ |
| **Milestone Templates** | 16 | Embedded in Project Templates |
| **Step Templates** | 141 (Phase 4) | [Task_Templates/Step_Templates/PHASE4_STEPS_INDEX.md](./Task_Templates/Step_Templates/PHASE4_STEPS_INDEX.md) |
| **Task Instances** | 0 (ready) | [Tasks/](./Tasks/) |
| **Step Instances** | 0 (ready) | [Steps/](./Steps/) |
| **Workflows** | 2 | [Workflows_Checklist-Item-003.md](./Workflows_Checklist-Item-003.md) |
| **Milestone Tracking** | 0 | Milestone_Tracking/ (to be created) |
| **Performance Metrics** | 0 | Performance_Metrics/ (to be created) |

---

## 📁 Folder Structure

```
TASK_MANAGERS/
├── README.md                          # Entity documentation
├── INDEX.md                           # This file - master index
├── Task_Templates.md                   # Complete Task Template details
├── Task_Templates_Checklist-Item-003.md          # Task Template ID and name index
├── Project_Templates_Checklist-Item-003.md       # Project Template ID and name index
├── Milestone_Templates_Checklist-Item-003.md     # Milestone Template ID and name index
├── Step_Templates_Checklist-Item-003.md          # Step Template ID and name index
├── Projects_Checklist-Item-003.md                # All projects with IDs
├── Workflows_Checklist-Item-003.md               # All workflows with IDs
│
├── Task_Templates/                    # Task Template files
│   ├── Task-Template-007.json (TASK-TEMPLATE-001)
│   └── Task-Template-021.json (TASK-TEMPLATE-002)
│
├── Project_Templates/                  # Project Template files
│   └── README.md                       # Directory documentation
│
├── Milestone_Templates/                # Milestone Template files
│   └── README.md                       # Directory documentation
│
├── Step_Templates/                     # Step Template files
│   └── README.md                       # Directory documentation
│
├── Projects/                          # Project instance files
│   └── PROJ-AI-NMP-001_Next_Main_Prompt_Version/
│       ├── project_instance.json
│       ├── README.md
│       ├── Milestones/ (8 milestone files)
│       └── Logs/ (6 log files)
│
├── Tasks/                             # Task instance files (centralized)
│   └── (empty - ready for task instances)
│
├── Steps/                             # Step instance files (centralized)
│   └── (empty - ready for step instances)
│
└── Workflows/                         # Workflow definition files
    ├── Old_Client_Reengagement_Workflow.yaml (WF-LIN-001)
    └── Lead_Enrichment_Workflow.yaml (WF-PAR-001)
│
├── Milestone_Tracking/               # (To be created)
│   ├── Project_Milestones/
│   └── Sprint_Goals/
│
└── Performance_Metrics/               # (To be created)
    ├── Department_Dashboards/
    ├── Individual_Performance/
    └── Team_Velocity/
```

---

## 🆔 ID Reference

### Task Template IDs

| ID | Name | File |
|----|------|------|
| TASK-TEMPLATE-001 | Create Job Posting | Task_Templates/Task-Template-007.json |
| TASK-TEMPLATE-002 | Send Follow-up Email to Old Clients | Task_Templates/Task-Template-021.json |

### Project Template IDs

| ID | Name | File |
|----|------|------|
| TEMPLATE-PROJ-LG-001 | Complete Lead Generation to Customer Conversion Campaign | Project_Templates/TEMPLATE-PROJ-LG-001.json |
| TEMPLATE-PROJ-DEV-001 | Complete MCP Automation Stack Setup | Project_Templates/TEMPLATE-PROJ-DEV-001.json |
| TEMPLATE-PROJ-LG-002 | Enterprise Account-Based Marketing (ABM) Campaign | Project_Templates/TEMPLATE-PROJ-LG-002.json |

### Milestone Template IDs

| ID | Name | Parent Project Template | File |
|----|------|------------------------|------|
| *(No Milestone Templates yet)* | | | |

### Step Template IDs

| ID | Name | Parent Task | File |
|----|------|-------------|------|
| STEP-HR-003-01 | Edit Video Interview Footage | TASK-TEMPLATE-HR-003 | Step_Templates/Edit_Video_Interview_Footage_TASK-TEMPLATE-HR-003_Template.json |
| STEP-HR-003-02 | Archive Edited Video to Drive | TASK-TEMPLATE-HR-003 | Step_Templates/Archive_Edited_Video_to_Drive_TASK-TEMPLATE-HR-003_Template.json |
| STEP-HR-003-03 | Publish Video Interview on YouTube | TASK-TEMPLATE-HR-003 | Step_Templates/Publish_Video_Interview_on_YouTube_TASK-TEMPLATE-HR-003_Template.json |
| STEP-HR-003-04 | Optimize YouTube Metadata | TASK-TEMPLATE-HR-003 | Step_Templates/Optimize_YouTube_Metadata_TASK-TEMPLATE-HR-003_Template.json |
| STEP-HR-003-05 | Add Interview Subtitles and Approve | TASK-TEMPLATE-HR-003 | Step_Templates/Add_Interview_Subtitles_and_Approve_TASK-TEMPLATE-HR-003_Template.json |

### Project IDs

| ID | Name | File |
|----|------|------|
| *(No projects yet)* | | |

### Workflow IDs

| ID | Name | File |
|----|------|------|
| WF-LIN-001 | Old Client Re-Engagement Campaign | Workflows/Old_Client_Reengagement_Workflow.yaml |
| WF-PAR-001 | Lead Enrichment | Workflows/Lead_Enrichment_Workflow.yaml |

---

## 🔍 Quick Lookups

### Find Task Template by Department
- **HR:** [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md#hr-department)
- **Sales:** [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md#sales-department)

### Find Task Template by Action
- **Create:** [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md#create)
- **Send:** [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md#send)

### Find Project Template by Department
- See [Project_Templates_Checklist-Item-003.md](./Project_Templates_Checklist-Item-003.md) (no Project Templates yet)

### Find Milestone Template by Parent Project
- See [Milestone_Templates_Checklist-Item-003.md](./Milestone_Templates_Checklist-Item-003.md) (no Milestone Templates yet)

### Find Step Template by Parent Task
- See [Step_Templates_Checklist-Item-003.md](./Step_Templates_Checklist-Item-003.md) for HR video interview publishing workflow steps

### Find Project by Department
- See [Projects_Checklist-Item-003.md](./Projects_Checklist-Item-003.md) (no projects yet)

### Find Workflow by Type
- **Linear Sequential:** [Workflows_Checklist-Item-003.md](./Workflows_Checklist-Item-003.md#linear-sequential)
- **Parallel Processing:** [Workflows_Checklist-Item-003.md](./Workflows_Checklist-Item-003.md#parallel-processing)

---

## 📊 Statistics

**Current Status (Phase 4-7 Complete):**
- Task Templates: 22 active (20) + 2 deprecated
- Project Templates: 3 active
- Milestone Templates: 16 (embedded in Project Templates)
- Step Templates: 141 active (Phase 4)
- Projects: 0 (to be created)
- Workflows: 2 active
- Milestone Tracking: Not yet implemented
- Performance Metrics: Not yet implemented

**By Department:**
- LG (Lead Generation): 12 Task Templates, 2 Project Templates, 82 Step Templates
- OPS (Operations): 4 Task Templates, 21 Step Templates
- DEV (Development): 4 Task Templates, 1 Project Template, 20 Step Templates
- HR: 1 Task Template, 6 Step Templates
- SALES: 1 Task Template, 6 Step Templates
- MARKETING: 1 Task Template, 6 Step Templates

**Project Template Coverage:**
- All 3 Project Templates are cross-department
- 9 of 22 Task Templates incorporated into projects (41%)
- 60+ of 141 Step Templates referenced in projects (42%+)

**Key Metrics:**
- 100% of Phase 6 workflows converted to Project Templates
- 15-20+ hours/week time savings potential (automation projects)
- $0.0025-0.15 per lead cost range (lead generation projects)
- 1:40 ROI on arbitrage strategies (enterprise ABM)

---

## 🔗 Related Entities

- **LIBRARIES** - Actions, Objects, Tools used in templates
- **TALENTS** - Employees assigned to tasks
- **JOBS** - Job posting templates
- **BUSINESSES** - Client-related workflows

## 📖 Documentation

- **[TAXONOMY_GUIDELINES.md](./TAXONOMY_GUIDELINES.md)** - Complete taxonomy field usage and database mapping guidelines
- **[README.md](./README.md)** - Entity overview and documentation

---

## 📝 Adding New Items

### Adding a Task Template

1. Create template JSON file in `Task_Templates/`
2. Assign ID: `TASK-TEMPLATE-[NEXT_NUMBER]`
3. Add entry to `Task_Templates_Checklist-Item-003.md`
4. Update this INDEX.md

### Adding a Project Template

1. Create template JSON file in `Project_Templates/`
2. Assign ID: `TEMPLATE-PROJ-[DEPT]-[NEXT_NUMBER]`
3. Add entry to `Project_Templates_Checklist-Item-003.md`
4. Update this INDEX.md

### Adding a Milestone Template

1. Identify the parent Project Template (must exist first)
2. Create Milestone Template JSON file in `Milestone_Templates/`
3. Assign ID: `MIL-TEMPLATE-PROJ-[PARENT_PROJ_ID]-[NEXT_NUMBER]`
4. Link to parent Project Template in the JSON
5. Add entry to `Milestone_Templates_Checklist-Item-003.md`
6. Update this INDEX.md

**Important:** Milestone Templates must reference an existing Project Template. Create the Project Template first if it doesn't exist.

### Adding a Step Template

1. Create template JSON file in `Step_Templates/`
2. Assign ID: `TEMPLATE-STEP-[TASK_ID]-[NEXT_NUMBER]`
3. Link to parent Task Template
4. Add entry to `Step_Templates_Checklist-Item-003.md`
5. Update this INDEX.md

### Adding a Project

1. Create project file in `Projects/`
2. Assign ID: `PROJ-[DEPT]-[NEXT_NUMBER]`
3. Add entry to `Projects_Checklist-Item-003.md`
4. Update this INDEX.md

### Adding a Workflow

1. Create workflow YAML file in `Workflows/`
2. Assign ID: `WF-[TYPE]-[NEXT_NUMBER]`
3. Add entry to `Workflows_Checklist-Item-003.md`
4. Update this INDEX.md

---

**Last Updated:** November 25, 2025  
**Maintained By:** Framework Architecture Team

