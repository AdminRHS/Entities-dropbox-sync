# ANALYTICS Entity Index

**Entity Type:** ANALYTICS  
**Domain:** Operational Analytics  
**Last Updated:** November 17, 2025

---

## Quick Navigation

### 📊 Analytics Infrastructure

- **[Projects](./Projects/)** - Project instances and execution tracking
- **[Milestone_Templates](./Milestone_Templates/)** - Milestone template definitions
- **[Tasks](./Tasks/)** - Task instances and execution tracking
- **[Task_Templates](./Task_Templates/)** - Task template definitions
- **[Steps](./Steps/)** - Step instances and execution tracking
- **[Step_Templates](./Step_Templates/)** - Step template definitions

---

## Entity Structure

```
ANALYTICS/
├── Projects/                    # Project instances with execution data
│   ├── PROJ-AI-NMP-001_Next_Main_Prompt_Version/
│   │   ├── Milestones/         # Nested milestones within projects
│   │   └── Logs/               # Project execution logs
│   └── PROJ-OPS-001_ENTITIES_Ecosystem_Analysis/
├── Milestone_Templates/         # Milestone structure templates
├── Tasks/                       # Task execution instances
├── Task_Templates/             # Task template definitions
├── Steps/                       # Step execution instances
├── Step_Templates/             # Step template definitions
├── README.md                    # Entity documentation
└── INDEX.md                     # This file
```

---

## Related Entities

- **TASK_MANAGERS:** Contains workflow definitions, guides, and prompts
- **LIBRARIES:** Provides taxonomy and standards referenced by analytics
- **DEPARTMENTS:** Department-specific analytics and reports

---

## Migration History

**2025-11-17:** Created ANALYTICS entity by moving analytics infrastructure from TASK_MANAGERS

