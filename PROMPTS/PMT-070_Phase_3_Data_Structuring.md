# PMT-070 Phase 3: Data Structuring & Normalization
**Version:** 1.0
**Date:** 2025-11-19
**Purpose:** Transform Phase 2 markdown into compact, structured JSON for Task Manager integration

---

## OBJECTIVE

Extract structured data from Phase 2 processed files and generate compact JSON format optimized for:
- **Token efficiency** (target: 74% reduction from Phase 2)
- **Task Manager integration** (responsibilities, tasks, steps)
- **Machine processing** (valid JSON schema)
- **Audit traceability** (evidence preservation)

---

## INPUT FORMAT

### Phase 2 File Structure

You will receive a Phase 2 processed markdown file containing:

1. **Metadata section** with employee info, date, source file
2. **Tagged actions** with form and type attributes:
   ```markdown
   <ACT-A form="ed">[Created]</ACT-A> <OBJ-DIG>[repository]{0.95}</OBJ-DIG>
   ```
3. **Consolidation tables** for actions, objects, tools
4. **Statistics** and analysis sections
5. **Embedded Phase 1 output** (full tagged transcript)

### Example Input Snippet

```markdown
# Phase 2: Object Probability Marking - Daily 228

## Category A: CREATION

| Verb | Frequency | Objects Created | Tagged Instances | Library Match |
|------|-----------|----------------|------------------|---------------|
| create | 9x | repository (4x), lessons (2x), tutorials (3x) | Lines 21,25,36,45... | ACT-044 ✅ |

## Tagged Content Sample

- <ACT-A form="ed">[Created]</ACT-A> <OBJ-DIG>[GitHub repository]{0.95}</OBJ-DIG> for project
- <ACT-B form="ing">[Working]</ACT-B> on <OBJ-DAT>[catalog]{0.93}</OBJ-DAT> updates
- Need to <ACT-A form="base">[create]</ACT-A> <OBJ-DIG>[video tutorials]{0.92}</OBJ-DIG>
```

---

## OUTPUT FORMAT

### Primary Output: Structured JSON

Generate a **compact, normalized JSON object** with the following schema:

```json
{
  "metadata": {
    "phase": 3,
    "employee_id": "228_Kucherenko_Iuliia",
    "date": "2025-01-17",
    "source_file": "phase_2_objects_daily_228.md",
    "processed_date": "YYYY-MM-DD",
    "version": "PMT-070-P3 v1.0"
  },
  "actions": [ /* normalized action list */ ],
  "objects": [ /* deduplicated object library */ ],
  "responsibilities": [ /* action+object+tool triplets */ ],
  "tools": [ /* tool usage patterns */ ],
  "statistics": { /* compact metrics */ },
  "classifications": { /* form-based categories */ },
  "task_manager_ready": { /* TM integration data */ }
}
```

---

## SECTION 1: METADATA

Extract from Phase 2 file header and add processing info.

```json
{
  "metadata": {
    "phase": 3,
    "employee_id": "{ID}_{FirstName}_{LastName}",
    "date": "YYYY-MM-DD",
    "source_file": "phase_2_objects_daily_{id}.md",
    "processed_date": "YYYY-MM-DD",
    "version": "PMT-070-P3 v1.0",
    "department": "extracted from content or metadata"
  }
}
```

---

## SECTION 2: ACTIONS (Normalized)

Extract ALL action instances from tagged content.

### Extraction Pattern

```regex
<ACT-([A-G])(?:\s+form="(base|ing|ed)")?(?:\s+type="(learning)")?\>\[(.*?)\]</ACT-\1>
```

### Normalization Rules

1. **Assign unique action IDs**: `A-001`, `A-002`, etc.
2. **Standardize verb forms**: Convert to lowercase base form for `verb` field
3. **Preserve original form**: Keep as `form` attribute (base/ing/ed)
4. **Link to library**: Extract ACT-### ID from consolidation tables
5. **Extract context**: Get surrounding 50 characters for evidence

### Action Object Schema

```json
{
  "action_id": "A-001",
  "verb": "create",
  "verb_original": "Created",
  "category": "A",
  "form": "ed",
  "type": null,
  "library_id": "ACT-044",
  "frequency": 9,
  "objects": ["O-001", "O-005", "O-012"],
  "tools": ["TOL-045"],
  "line_numbers": [21, 25, 36],
  "evidence_ref": "E-001",
  "context_snippet": "Created GitHub repository for..."
}
```

### Special Cases

**Learning Actions** (type="learning"):
```json
{
  "action_id": "A-045",
  "verb": "learn",
  "form": "ed",
  "type": "learning",
  "category": "C",
  "learning_subject": "Python data analysis",
  "nested_action": "A-046",
  "evidence_ref": "E-045"
}
```

---

## SECTION 3: OBJECTS (Deduplicated Library)

Create canonical object library by **deduplicating variants**.

### Deduplication Rules

1. **Identify variants**: "repository", "GitHub repository", "repo", "github repo"
2. **Select canonical form**: Most frequent or most specific variant
3. **Assign unique IDs**: `O-001`, `O-002`, etc.
4. **Calculate combined stats**: Total frequency, average probability

### Object Schema

```json
{
  "obj_id": "O-001",
  "canonical_name": "repository",
  "category": "DIG",
  "variants": ["GitHub repository", "repo", "github repo"],
  "variant_frequencies": {"repository": 5, "GitHub repository": 4, "repo": 3},
  "total_frequency": 12,
  "avg_probability": 0.93,
  "probability_range": [0.90, 0.95],
  "used_by_actions": ["A-001", "A-007", "A-012"],
  "used_by_tools": ["TOL-045"],
  "first_seen_line": 21
}
```

### Variant Detection Heuristics

- **Substring match**: "repository" matches "GitHub repository"
- **Common root**: "repo" → "repository"
- **Tool-prefixed**: "GitHub {object}" → "{object}"
- **Plural forms**: "repositories" → "repository"
- **Case insensitive**: "Repository" → "repository"

**Example Consolidation:**
```
Input variants:
- repository (4x, prob 0.93)
- GitHub repository (3x, prob 0.95)
- repo (2x, prob 0.90)
- github (5x, prob 0.92) ← separate tool, not variant

Output:
{
  "obj_id": "O-001",
  "canonical_name": "repository",
  "variants": ["GitHub repository", "repo"],
  "total_frequency": 9,
  "avg_probability": 0.93
}
```

---

## SECTION 4: RESPONSIBILITIES (Action+Object+Tool Triplets)

Form **responsibility signatures** by clustering related action-object-tool combinations.

### Formation Logic

1. **Group by action+objects**: Actions that operate on same objects
2. **Add tools**: Tools used to perform those actions
3. **Calculate frequency**: How often this combination appears
4. **Determine form distribution**: Breakdown by base/ing/ed
5. **Classify primary use**: Plan, ongoing responsibility, or completed work

### Responsibility Schema

```json
{
  "resp_id": "RESP-001",
  "signature": "create_repository_with_github",
  "action": "create",
  "action_ids": ["A-001", "A-007", "A-012"],
  "objects": ["repository", "lesson"],
  "object_ids": ["O-001", "O-005"],
  "tools": ["github", "lesson_library"],
  "tool_ids": ["TOL-045", "TOL-032"],
  "frequency": 11,
  "form_distribution": {
    "base": 2,
    "ing": 1,
    "ed": 8
  },
  "classification": "completed_work",
  "department": "DESIGN",
  "skill_level": "intermediate",
  "evidence_lines": [21, 25, 36, 45, 67, 89, 112, 134, 156, 178, 201]
}
```

### Signature Generation

Format: `{action}_{primary_object}_with_{primary_tool}`

Examples:
- `create_repository_with_github`
- `update_catalog_with_database`
- `analyze_data_with_python`

### Classification Rules

Based on `form_distribution`:

| Dominant Form | Classification | Skill Level Logic |
|---------------|----------------|-------------------|
| `ed` > 70% | `completed_work` | Frequency > 10 → advanced; 5-10 → intermediate; < 5 → beginner |
| `ing` > 50% | `ongoing_responsibility` | Current active skill |
| `base` > 50% | `planned_work` | Learning/growth area |
| Mixed | `mixed_activity` | Skill in development |

---

## SECTION 5: TOOLS (Usage Patterns)

Extract tool usage from tagged content and consolidation tables.

### Tool Schema

```json
{
  "tool_id": "TOL-045",
  "name": "github",
  "category": "SYS",
  "frequency": 10,
  "actions_performed": ["create", "manage", "update", "delete"],
  "action_ids": ["A-001", "A-007", "A-012"],
  "objects_operated": ["repository", "issues", "pull_requests"],
  "object_ids": ["O-001", "O-003", "O-007"],
  "department": "DESIGN",
  "mastery_level": "advanced"
}
```

### Tool Extraction

1. **From tagged content**: `<TOOL-{CATEGORY}>[{name}]{prob}</TOOL-{CATEGORY}>`
2. **From consolidation tables**: "Tools Used" section
3. **From action context**: "with GitHub", "using Python", etc.

### Mastery Level

Based on frequency and action diversity:
- **Advanced**: freq > 10 AND actions > 3
- **Intermediate**: freq 5-10 OR actions 2-3
- **Beginner**: freq < 5 AND actions <= 1

---

## SECTION 6: STATISTICS (Compact)

Provide summary metrics in minimal format.

```json
{
  "statistics": {
    "total_actions": 85,
    "total_objects": 108,
    "unique_verbs": 25,
    "unique_canonical_objects": 49,
    "total_responsibilities": 42,
    "tools_used": 7,
    "action_categories": {
      "A": 16,
      "B": 14,
      "C": 23,
      "D": 2,
      "E": 16,
      "F": 4,
      "G": 10
    },
    "form_distribution": {
      "base": 23,
      "ing": 18,
      "ed": 38,
      "unknown": 6
    },
    "learning_activities": 15,
    "departments": {
      "DESIGN": 55,
      "DEV": 30
    }
  }
}
```

**NO prose descriptions. Only numbers and counts.**

---

## SECTION 7: CLASSIFICATIONS (Form-Based)

Integrate form-based classifications from verb forms.

### Work Plans (base form)

```json
{
  "work_plans": [
    {
      "plan_id": "PLAN-001",
      "action": "create",
      "action_id": "A-023",
      "objects": ["documentation", "tutorials"],
      "object_ids": ["O-015", "O-018"],
      "priority": "HIGH",
      "estimated_effort": "medium",
      "tools_needed": ["notion", "video_editor"]
    }
  ]
}
```

### Priority Calculation

Based on object probability and frequency:
- **HIGH**: avg_prob >= 0.90 OR freq > 3
- **MEDIUM**: avg_prob 0.70-0.89 OR freq 2-3
- **LOW**: avg_prob < 0.70 OR freq 1

### Ongoing Responsibilities (ing form)

```json
{
  "ongoing_responsibilities": [
    {
      "resp_id": "RESP-001",
      "action": "managing",
      "action_id": "A-008",
      "objects": ["repositories", "team_members"],
      "object_ids": ["O-001", "O-022"],
      "skill_level": "intermediate",
      "frequency": "daily",
      "tools": ["github", "slack"]
    }
  ]
}
```

### Completed Work (ed form)

```json
{
  "completed_work": [
    {
      "completion_id": "COMP-001",
      "action": "created",
      "action_id": "A-001",
      "objects": ["repository", "lesson_structure"],
      "object_ids": ["O-001", "O-009"],
      "impact": "high",
      "deliverable": "New project repository with lesson framework",
      "date": "2025-01-17",
      "tools_used": ["github", "lesson_library"]
    }
  ]
}
```

### Impact Assessment

- **High**: Creates new entity (repository, project, system)
- **Medium**: Updates existing entity significantly
- **Low**: Minor modifications or maintenance

### Learning Activities (type="learning")

```json
{
  "learning_activities": [
    {
      "learning_id": "LEARN-001",
      "action": "learned",
      "action_id": "A-045",
      "subjects": ["Python", "data analysis"],
      "status": "completed",
      "nested_action": "analyze_data",
      "nested_action_id": "A-046",
      "tools_learned": ["pandas", "matplotlib"],
      "skill_derived": "Python Data Analysis",
      "application": "analysis projects"
    }
  ]
}
```

---

## SECTION 8: TASK MANAGER READY

Prepare structured data for Task Manager integration.

### Employee Profile

```json
{
  "task_manager_ready": {
    "employee_profile": {
      "id": "228_Kucherenko_Iuliia",
      "name": "Iuliia Kucherenko",
      "employee_number": "228",
      "department_allocation": {
        "DESIGN": 0.65,
        "DEV": 0.35
      },
      "top_responsibilities": ["RESP-001", "RESP-002", "RESP-005"],
      "tools_mastered": [
        {"tool": "github", "level": "advanced"},
        {"tool": "lesson_library", "level": "intermediate"}
      ],
      "skill_areas": [
        "Repository Management",
        "Lesson Creation",
        "Documentation"
      ],
      "work_patterns": {
        "primary_actions": ["create", "update", "manage"],
        "primary_objects": ["repository", "lessons", "documentation"]
      }
    }
  }
}
```

### Suggested Tasks

Cluster responsibilities into logical tasks.

```json
{
  "suggested_tasks": [
    {
      "task_id": "TASK-DESIGN-001",
      "title": "Manage GitHub repositories and lesson content",
      "description": "Create, update, and maintain GitHub repositories and educational lesson materials",
      "responsibilities": ["RESP-001", "RESP-003", "RESP-007"],
      "tools_required": ["github", "lesson_library", "vs_code"],
      "objects_involved": ["repository", "lessons", "tutorials"],
      "estimated_frequency": "daily",
      "complexity": "medium",
      "department": "DESIGN",
      "suggested_steps": [
        "Create new repository",
        "Set up lesson structure",
        "Upload content",
        "Review and validate"
      ]
    }
  ]
}
```

### Task Clustering Logic

1. **Group responsibilities** with overlapping objects and tools
2. **Calculate frequency**: Sum of responsibility frequencies
3. **Determine complexity**: Based on number of steps and tool diversity
4. **Generate title**: Action + primary objects
5. **Suggest steps**: Break down into subtasks (3-5 steps)

### Export Ready Flag

```json
{
  "export_ready": true,
  "export_format": "json",
  "tm_compatibility_version": "1.0",
  "validation_status": "passed"
}
```

---

## SECTION 9: EVIDENCE EXTRACTION

Create separate evidence file for audit trail.

### Evidence Object Schema

```json
{
  "evidence": {
    "A-001": {
      "action_id": "A-001",
      "full_context": "Created GitHub repository for new project with lesson structure and initial documentation",
      "tagged_line": "<ACT-A form=\"ed\">[Created]</ACT-A> <OBJ-DIG>[GitHub repository]{0.95}</OBJ-DIG> for new project",
      "line_number": 21,
      "phase_2_reference": "phase_2_objects_daily_228.md#L21",
      "phase_1_reference": "phase_1_actions_daily_228.md#L15",
      "transcript_snippet": "Original Ukrainian/Russian text if available",
      "surrounding_context": "Previous and next lines for context"
    }
  }
}
```

### Evidence References

In main JSON, use minimal references:

```json
{
  "action_id": "A-001",
  "evidence_ref": "E-001"  // Links to evidence file
}
```

---

## DATA EXTRACTION WORKFLOW

### Step 1: Parse Phase 2 Markdown

1. Extract metadata from header
2. Parse consolidation tables (actions, objects, tools)
3. Extract tagged content with regex
4. Identify line numbers for all entities

### Step 2: Normalize Objects

1. Collect all `<OBJ-{CATEGORY}>[{name}]{prob}</OBJ-{CATEGORY}>` tags
2. Group variants (substring match, root match, case insensitive)
3. Select canonical form (most frequent or specific)
4. Assign unique IDs (O-001, O-002, ...)
5. Calculate combined statistics

### Step 3: Build Actions List

1. Extract all action tags with form and type attributes
2. Assign unique IDs (A-001, A-002, ...)
3. Link to objects (replace object names with O-IDs)
4. Link to library (extract ACT-### from tables)
5. Extract context snippets (50 chars before/after)

### Step 4: Form Responsibilities

1. Group actions by verb+objects combination
2. Add tools from context or consolidation tables
3. Calculate frequency (count occurrences)
4. Determine form distribution (base/ing/ed counts)
5. Classify primary use (plan/ongoing/completed)
6. Generate signature (action_object_with_tool)
7. Assign IDs (RESP-001, RESP-002, ...)

### Step 5: Extract Tools

1. Parse `<TOOL-{CATEGORY}>[{name}]{prob}</TOOL-{CATEGORY}>` tags
2. Extract from "Tools Used" consolidation table
3. Find contextual mentions ("with GitHub", "using Python")
4. Assign IDs (TOL-001, TOL-002, ...)
5. Link to actions and objects
6. Calculate mastery level

### Step 6: Generate Classifications

1. **Work Plans**: Filter actions with form="base", create plan objects
2. **Ongoing**: Filter actions with form="ing", create responsibility objects
3. **Completed**: Filter actions with form="ed", create completion objects
4. **Learning**: Filter actions with type="learning", create learning objects

### Step 7: Prepare Task Manager Data

1. **Employee Profile**: Aggregate statistics and patterns
2. **Suggested Tasks**: Cluster responsibilities (3-5 per task)
3. **Tools Required**: List unique tools with mastery levels
4. **Department Allocation**: Calculate % by counting department tags

### Step 8: Generate Evidence File

1. For each action, extract full context
2. Save original tagged lines
3. Add line number references
4. Link to Phase 1 and Phase 2 sources
5. Include transcript snippets if available

---

## TOKEN REDUCTION STRATEGIES

### What to REMOVE from Phase 2

1. ✅ **Embedded Phase 1 output** (saves ~2,000 tokens)
2. ✅ **Verbose markdown tables** (convert to compact JSON arrays)
3. ✅ **Repeated consolidations** (one canonical object list)
4. ✅ **Statistical prose** (numbers only, no descriptions)
5. ✅ **Category descriptions** (already in config, don't repeat)
6. ✅ **Explanatory text** (move to documentation)

### What to KEEP (Essential Data)

1. ✅ Action-object pairs with form attributes
2. ✅ Object probabilities and frequencies
3. ✅ Tool mappings
4. ✅ Line number references
5. ✅ Form classifications
6. ✅ Responsibility signatures

### Compact Representation Examples

**Instead of:**
```markdown
| Verb | Frequency | Objects Modified | Tagged Instances | Library Match |
|------|-----------|-----------------|------------------|---------------|
| create | 9x | repository (4x), lessons (2x), tutorials (3x) | Throughout document | ACT-044 ✅ |
```

**Use:**
```json
{
  "action_id": "A-001",
  "verb": "create",
  "freq": 9,
  "objects": ["O-001:4", "O-005:2", "O-012:3"],
  "library_id": "ACT-044"
}
```

**Token reduction:** ~85%

---

## VALIDATION CHECKLIST

Before outputting, verify:

- ✅ Valid JSON (no syntax errors)
- ✅ All IDs unique and sequential
- ✅ All references valid (O-IDs, A-IDs, etc. exist)
- ✅ Object variants properly consolidated
- ✅ Responsibility signatures follow format
- ✅ Form distribution sums correctly
- ✅ Statistics calculated accurately
- ✅ Evidence references complete
- ✅ Task Manager export ready flag true

---

## OUTPUT FILE NAMING

Generate THREE files per employee daily:

1. **Main JSON:** `phase_3_structured_daily_{employee_id}.json`
2. **Summary MD:** `phase_3_summary_daily_{employee_id}.md`
3. **Evidence JSON:** `phase_3_evidence_daily_{employee_id}.json`

---

## VERSION HISTORY

**v1.0** - 2025-11-19
- Initial Phase 3 prompt creation
- JSON schema definition
- Object normalization rules
- Responsibility formation logic
- Task Manager export structure

---

**END OF PMT-070 PHASE 3 PROMPT**
