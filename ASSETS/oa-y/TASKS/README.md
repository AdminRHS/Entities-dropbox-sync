# TASKS: Onboarding Task Library

**System:** Remote Helpers Entity System  
**Purpose:** Structured onboarding task library with cross-references to Courses, Lessons, and Taxonomy  
**Created:** 2025-01-19  
**Status:** Active

---

## Overview

The TASKS folder contains structured onboarding tasks that guide new employees through their onboarding process. Each task includes:

- Unique ID (TASK-###)
- Step-by-step instructions
- Cross-references to Online Academy Courses (COURSE-###) and Lessons (LESSON-###)
- Taxonomy classification
- Dependencies and prerequisites
- Expected outcomes

---

## Folder Structure

```
TASKS/
├── README.md (this file)
├── PLANNING.md (system architecture and conventions)
├── TASK.md (current tasks and status)
├── FILES.md (codebase overview)
├── Tasks/
│   ├── TASK-001_*.md
│   ├── TASK-002_*.md
│   └── ...
├── Courses/
│   ├── COURSE-001_*.md
│   ├── COURSE-002_*.md
│   └── ...
└── Lessons/
    ├── LESSON-001_*.md
    ├── LESSON-002_*.md
    └── ...
```

---

## ID Conventions

- **Tasks:** TASK-001, TASK-002, TASK-003...
- **Courses:** COURSE-001, COURSE-002, COURSE-003...
- **Lessons:** LESSON-001, LESSON-002, LESSON-003...

---

## Cross-Reference System

Tasks reference:
- **Courses** from `ASSETS/oa-y/Courses/`
- **Lessons** from `ASSETS/oa-y/Lessons/`
- **Taxonomy** paths from `TAXONOMY/TASK_MANAGERS__Taxonomy/`

---

## Taxonomy Integration

Tasks are classified using taxonomy paths such as:
- `Onboarding/Tools/VSCode`
- `Onboarding/Accounts/Discord`
- `Onboarding/CRM/Basics`
- `Learning/Development/Basics`

---

## File Naming Convention

- Tasks: `TASK-{number}_{Title-Slug}.md`
- Courses: `COURSE-{number}_{Title-Slug}.md`
- Lessons: `LESSON-{number}_{Title-Slug}.md`

---

## Related Systems

- **ASSETS:** `ENTITIES/ASSETS/oa-y/` - Source courses and lessons
- **TAXONOMY:** `ENTITIES/TAXONOMY/` - Category definitions
- **TASK_MANAGERS:** `ENTITIES/TASK_MANAGERS/` - Task templates and workflows

---

**Last Updated:** 2025-01-19

