# Content Export Prompt for oa-y-mcp-service

## Overview
This document provides step-by-step instructions for exporting all content from the oa-y-mcp-service API to local markdown files.

## API Configuration
```json
{
  "command": "npx",
  "args": ["github:AdminRHS/oa-y-mcp-service"],
  "env": {
    "APP_ENV": "prod",
    "API_TOKEN": "d383d4d1-5829-4aa1-80ce-0668d6869386",
    "API_TOKEN_LIBS": "sk_ksE_rARLjfvNSchxppLvgj6Svxvos1zuS4oZdQowOEo"
  }
}
```

## Content Statistics
- **Total Courses:** 53
- **Professions:** 65
- **Export Base Path:** `C:\Users\Dell\Dropbox\Nov25\Niko Nov25\oa-y_content`

## Folder Structure
```
oa-y_content/
├── Courses_Listing.md              # Index of all courses
├── Courses/                         # Individual course files
│   ├── {courseId}_{courseName}.md
│   └── ...
├── Lessons_Listing.md              # Index of all lessons
├── Lessons/                         # Individual lesson files
│   ├── {lessonId}_{lessonName}.md
│   └── ...
├── Modules_Listing.md              # Index of all modules
├── Modules/                         # Individual module files
│   ├── {moduleId}_{moduleName}.md
│   └── ...
├── Tests_Listing.md                # Index of all tests
├── Tests/                           # Individual test files
│   ├── {testId}_{testName}.md
│   └── ...
└── INDEX.md                         # Master index
```

## Step 1: Export All Courses

### Fetch All Courses
```typescript
const courses = await mcp_oa-y-mcp-service_get_courses({ all: true });
```

### For Each Course, Get Details
```typescript
for (const course of courses.data) {
  const details = await mcp_oa-y-mcp-service_get_course({ 
    courseId: course.id 
  });
  
  // Create file: Courses/{courseId}_{slug}.md
  // Include: title, description, professions, modules with lessons
}
```

### Course File Template
```markdown
# {Title}

**Course ID:** {id}
**Slug:** {slug}
**URL:** {url}

## Description
{description}

## Details
- **Image URL:** {image_url}
- **Video URL:** {video_url}
- **Professions:** {professions.map(p => p.name).join(', ')}

## Modules

### Module {n}: {module.title}
**Module ID:** {module.id}
**Slug:** {module.slug}
**URL:** {module.url}

#### Lessons:
1. **{lesson.title}**
   - ID: {lesson.id}
   - Slug: {lesson.slug}
   - URL: {lesson.url}
```

## Step 2: Export All Lessons

### Fetch All Lessons
```typescript
const lessons = await mcp_oa-y-mcp-service_get_lessons({ all: true });
```

### For Each Lesson, Get Details
```typescript
for (const lesson of lessons.data) {
  // Note: Lessons require courseId and moduleId
  // Get these from the course export data
  const details = await mcp_oa-y-mcp-service_get_lesson({
    courseId: lesson.courseId,
    moduleId: lesson.moduleId,
    lessonId: lesson.id
  });
  
  // Create file: Lessons/{lessonId}_{slug}.md
}
```

### Lesson File Template
```markdown
# {Title}

**Lesson ID:** {id}
**Slug:** {slug}
**Type:** {type}
**Content Type:** {contentType}
**Duration:** {duration} minutes

## Description
{description}

## Content
{content or contentBlocks}

## Resources
{resources}

## Practice Exercises
{practiceExercises}

## Associated
- **Course:** {course.title} ({course.id})
- **Module:** {module.title} ({module.id})
```

## Step 3: Export All Modules

### Fetch All Modules
```typescript
const modules = await mcp_oa-y-mcp-service_get_modules({ 
  limit: 1000 // Or iterate through pages
});
```

### For Each Module, Get Details
```typescript
for (const module of modules.data) {
  const details = await mcp_oa-y-mcp-service_get_module({
    moduleId: module.id
  });
  
  // Create file: Modules/{moduleId}_{slug}.md
}
```

### Module File Template
```markdown
# {Title}

**Module ID:** {id}
**Slug:** {slug}

## Description
{description}

## Content
{content}

## Lessons
{lessons.map(l => `- ${l.title} (${l.id})`).join('\n')}

## Details
- **Preview Image:** {previewImage}
- **Video URL:** {videoUrl}
- **Draft Status:** {isDraft}
```

## Step 4: Export All Tests

### Fetch All Tests
```typescript
const tests = await mcp_oa-y-mcp-service_get_tests({ 
  limit: 1000
});
```

### For Each Test, Get Details
```typescript
for (const test of tests.data) {
  const details = await mcp_oa-y-mcp-service_get_test({
    testId: test.id
  });
  
  // Create file: Tests/{testId}_{slug}.md
}
```

### Test File Template
```markdown
# {Title}

**Test ID:** {id}
**Slug:** {slug}
**Lesson ID:** {lesson}

## Description
{description}

## Settings
- **Time Limit:** {timeLimit} minutes
- **Passing Score:** {passingScore}%

## Questions

### Question {n}: {question.question}
**Type:** {question.type}
**Points:** {question.points}

{Options or correct answer based on type}
```

## Step 5: Create Master Index

Create `INDEX.md` with:
- Total counts for each content type
- Links to all listing files
- Export date and statistics
- Quick navigation

## Automation Script (Pseudocode)

```javascript
async function exportAllContent() {
  // 1. Export Courses
  const courses = await getCourses({ all: true });
  for (const course of courses.data) {
    const details = await getCourse(course.id);
    await writeFile(`Courses/${course.id}_${sanitize(course.slug)}.md`, 
                    formatCourse(details));
  }
  await writeFile('Courses_Listing.md', createCourseListing(courses));
  
  // 2. Export Lessons
  const lessons = await getLessons({ all: true });
  // ... similar pattern
  
  // 3. Export Modules
  const modules = await getModules({ limit: 1000 });
  // ... similar pattern
  
  // 4. Export Tests
  const tests = await getTests({ limit: 1000 });
  // ... similar pattern
  
  // 5. Create Master Index
  await createMasterIndex();
}
```

## Current Export Status

### ✅ Completed
- Folder structure created
- Courses_Listing.md with all 53 courses
- First 10 course detail files

### ⏳ Remaining
- 43 more course detail files
- All lessons (listing + details)
- All modules (listing + details)
- All tests (listing + details)
- Master INDEX.md

## Next Steps

To complete the export, either:
1. **Manual:** Continue calling `get_course` for each of the remaining 43 courses
2. **Automated:** Use the script structure above in a Node.js environment
3. **Batch:** Process in groups of 10-20 courses at a time

The manual approach requires approximately **200+ API calls** to complete the full export.

