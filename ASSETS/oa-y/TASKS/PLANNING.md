# TASKS System Planning

**System:** Onboarding Task Library  
**Created:** 2025-01-19  
**Status:** Active

---

## Architecture Overview

The TASKS system is designed to:

1. **Structure onboarding content** into actionable tasks
2. **Cross-reference** with Online Academy Courses and Lessons
3. **Classify** using the Taxonomy system
4. **Track dependencies** between tasks
5. **Provide learning paths** for different roles

---

## Core Components

### 1. Tasks (TASK-###)

Each task represents a single onboarding activity with:
- Clear objective
- Step-by-step instructions
- Requirements (accounts, tools, prerequisites)
- Cross-references to courses/lessons
- Expected outcome

### 2. Courses (COURSE-###)

Courses are collections of lessons, mapped from `ASSETS/oa-y/Courses/`:
- Course description
- List of contained lessons
- Category classification

### 3. Lessons (LESSON-###)

Individual learning units, mapped from `ASSETS/oa-y/Lessons/`:
- Lesson summary
- Key content points
- Category classification

---

## Taxonomy Integration

### Taxonomy Path Structure

Tasks use hierarchical taxonomy paths:

```
Onboarding/
├── Tools/
│   ├── VSCode
│   ├── Chrome
│   └── Discord
├── Accounts/
│   ├── Discord
│   ├── Gmail
│   └── CRM
├── CRM/
│   ├── Basics
│   ├── Reports
│   └── Lead_Management
└── Learning/
    ├── Development/
    ├── Design/
    └── Sales/
```

### Mapping Rules

- If content comes from `oa-y/Courses` → Course entity
- If content comes from `oa-y/Lessons` → Lesson entity
- Tasks reference both Courses and Lessons
- Taxonomy paths come from `TAXONOMY/TASK_MANAGERS__Taxonomy/`

---

## ID Assignment Strategy

### Task IDs
- Sequential numbering: TASK-001, TASK-002...
- Assigned when task is created
- Never reused or renumbered

### Course IDs
- Mapped from Online Academy Course IDs
- Format: COURSE-001, COURSE-002...
- Cross-reference to original: `68c808b19b6cc171abd1454a` → `COURSE-001`

### Lesson IDs
- Mapped from Online Academy Lesson IDs
- Format: LESSON-001, LESSON-002...
- Cross-reference to original: `68b995d3432c23c0b668e41b` → `LESSON-001`

---

## Content Mapping Process

### From Course to Task

1. Identify course from `ASSETS/oa-y/Courses/`
2. Extract course modules and lessons
3. Create task(s) that reference the course
4. Map lessons to task steps
5. Assign taxonomy path based on course content

### From Lesson to Task

1. Identify lesson from `ASSETS/oa-y/Lessons/`
2. Determine if lesson is standalone or part of course
3. Create task referencing the lesson
4. Extract key learning points
5. Assign taxonomy path

---

## Dependency Management

Tasks can have:
- **Prerequisites:** Other tasks that must be completed first
- **Related Tasks:** Tasks that complement or extend this task
- **Required Lessons:** Lessons that must be completed before task
- **Required Courses:** Courses that provide foundational knowledge

---

## File Organization

### Task Files

Located in `TASKS/Tasks/`:
- One file per task
- Named: `TASK-{number}_{Title-Slug}.md`
- Contains full task specification

### Course Files

Located in `TASKS/Courses/`:
- One file per course
- Named: `COURSE-{number}_{Title-Slug}.md`
- Contains course structure and lesson references

### Lesson Files

Located in `TASKS/Lessons/`:
- One file per lesson
- Named: `LESSON-{number}_{Title-Slug}.md`
- Contains lesson content summary

---

## Validation Rules

1. **Every task must have:**
   - Unique ID
   - Title
   - Objective
   - Steps
   - Category (taxonomy path)
   - At least one cross-reference

2. **Every course must have:**
   - Unique ID
   - Title
   - Description
   - List of lessons
   - Category

3. **Every lesson must have:**
   - Unique ID
   - Title
   - Summary
   - Category

4. **Cross-references must:**
   - Use correct ID format (COURSE-###, LESSON-###)
   - Reference existing entities
   - Be bidirectional (task → course, course → task)

---

## Integration Points

### With ASSETS System
- Read courses from `ASSETS/oa-y/Courses/`
- Read lessons from `ASSETS/oa-y/Lessons/`
- Map original IDs to internal IDs
- Maintain sync with source content

### With TAXONOMY System
- Use taxonomy paths from `TAXONOMY/TASK_MANAGERS__Taxonomy/`
- Validate category assignments
- Ensure hierarchical consistency

### With TASK_MANAGERS System
- Reference task templates when applicable
- Align with workflow definitions
- Use department classifications

---

## Workflow

### Creating a New Task

1. Identify onboarding need
2. Search ASSETS for relevant courses/lessons
3. Determine taxonomy category
4. Assign next available TASK-ID
5. Create task file with all required sections
6. Add cross-references to courses/lessons
7. Update TASK.md with new task entry

### Mapping a Course

1. Read course file from `ASSETS/oa-y/Courses/`
2. Extract course metadata (ID, title, description)
3. Assign COURSE-ID
4. Map all lessons referenced in course
5. Create course file in `TASKS/Courses/`
6. Update cross-references in related tasks

### Mapping a Lesson

1. Read lesson file from `ASSETS/oa-y/Lessons/`
2. Extract lesson metadata (ID, title, content)
3. Assign LESSON-ID
4. Determine if lesson belongs to course
5. Create lesson file in `TASKS/Lessons/`
6. Update cross-references in related tasks/courses

---

## Best Practices

1. **Keep tasks focused:** One task = one clear objective
2. **Use clear language:** Steps should be actionable and simple
3. **Provide context:** Explain why each step matters
4. **Cross-reference liberally:** Link to all relevant courses/lessons
5. **Maintain taxonomy:** Always assign proper category paths
6. **Track dependencies:** Document prerequisites clearly
7. **Update regularly:** Keep content synchronized with ASSETS

---

**Last Updated:** 2025-01-19

