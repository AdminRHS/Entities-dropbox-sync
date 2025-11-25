# TASKS System - Files Overview

**Created:** 2025-01-19  
**Purpose:** Codebase structure and file organization

---

## Root Files

- `README.md` - System overview and quick reference
- `PLANNING.md` - Architecture and design decisions
- `TASK.md` - Current tasks and status tracking
- `FILES.md` - This file, codebase overview

---

## Directory Structure

```
TASKS/
├── README.md
├── PLANNING.md
├── TASK.md
├── FILES.md
├── Tasks/          # Individual task files
├── Courses/        # Course mapping files
└── Lessons/        # Lesson mapping files
```

---

## File Types

### Task Files (`Tasks/TASK-###_*.md`)

Format: `TASK-{number}_{Title-Slug}.md`

Contains:
- Task ID and metadata
- Objective and steps
- Requirements and prerequisites
- Cross-references
- Expected outcome

### Course Files (`Courses/COURSE-###_*.md`)

Format: `COURSE-{number}_{Title-Slug}.md`

Contains:
- Course ID and metadata
- Description
- List of lessons (LESSON-### references)
- Category classification

### Lesson Files (`Lessons/LESSON-###_*.md`)

Format: `LESSON-{number}_{Title-Slug}.md`

Contains:
- Lesson ID and metadata
- Summary and content points
- Category classification

---

## File Naming Conventions

- Use kebab-case for slugs
- Include ID prefix (TASK-###, COURSE-###, LESSON-###)
- Keep titles concise but descriptive
- Example: `TASK-001_Setup-VSCode-Environment.md`

---

## Cross-Reference Patterns

### In Task Files

```markdown
## Cross References

- Related Course: COURSE-001 — CRM Onboarding
- Related Lesson: LESSON-001 — Login to CRM
```

### In Course Files

```markdown
## Contains Lessons

- LESSON-001
- LESSON-002
- LESSON-003
```

---

## Source File Mapping

### From ASSETS

- Courses: `ASSETS/oa-y/Courses/{id}_{slug}.md` → `TASKS/Courses/COURSE-###_{slug}.md`
- Lessons: `ASSETS/oa-y/Lessons/{id}_{slug}.md` → `TASKS/Lessons/LESSON-###_{slug}.md`

### ID Mapping

- Original Course ID: `68c808b19b6cc171abd1454a` → Internal: `COURSE-001`
- Original Lesson ID: `68b995d3432c23c0b668e41b` → Internal: `LESSON-001`

---

## File Size Guidelines

- Keep individual files under 500 lines
- Split large tasks into multiple smaller tasks
- Use cross-references instead of duplicating content

---

## Maintenance

- Update FILES.md when adding new file types
- Maintain consistent naming across all files
- Keep cross-references synchronized
- Document any structural changes in PLANNING.md

---

**Last Updated:** 2025-01-19

