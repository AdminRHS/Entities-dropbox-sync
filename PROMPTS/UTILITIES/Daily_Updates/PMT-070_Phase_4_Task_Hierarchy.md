# PMT-070 Phase 4: Task Hierarchy Formation & Granularity Classification
**Version:** 1.0
**Date:** 2025-11-20
**Purpose:** Transform Phase 3 responsibilities into hierarchical task structure with proper granularity classification

---

## OBJECTIVE

Classify Phase 3 responsibilities into three granularity tiers (Checklist/Step/Task) and organize them hierarchically using:
- **Bottom-Up Promotion:** Group 2+ related steps into tasks
- **Top-Down Decomposition:** Break down vague tasks into concrete steps

**Goal:** Create Task Manager-ready hierarchical templates with proper granularity classification

---

## INPUT FORMAT

### Phase 3 Responsibilities

You will receive Phase 3 structured JSON containing:

```json
{
  "responsibilities": [
    {
      "resp_id": "RESP-001",
      "signature": "create_repository_with_github",
      "action": "create",
      "objects": ["repository", "lesson"],
      "tools": ["github", "lesson_library"],
      "frequency": 11,
      "form_distribution": {"base": 2, "ing": 1, "ed": 8},
      "classification": "completed_work",
      "skill_level": "intermediate"
    }
  ]
}
```

---

## OUTPUT FORMAT

Generate Phase 4 JSON with three-tier hierarchy:

```json
{
  "metadata": {...},
  "checklist_items": [...],
  "step_templates": [...],
  "task_templates": [...],
  "task_decompositions": [...],
  "statistics": {...},
  "manual_review_required": {...}
}
```

---

## TIER 1: CHECKLIST ITEMS (Atomic Actions)

### Classification Criteria

**Duration:** < 2 minutes
**Complexity:** Single, atomic action
**Decision-Making:** None required
**Examples:** Click button, Open file, Save document, Login to system

### Atomic Verb Patterns

```
ATOMIC_VERBS = [
  'click', 'open', 'close', 'save', 'upload', 'download',
  'delete', 'select', 'copy', 'paste', 'login', 'logout',
  'import', 'export', 'enter', 'submit', 'cancel', 'refresh'
]
```

### Detection Rules

1. **Verb is atomic** (in ATOMIC_VERBS list)
2. **Simple object** (UI element, file, single data item)
3. **No nested actions** (not "save and commit" - that's 2 actions)
4. **Frequency = 1** (atomic actions typically appear once per context)

### Checklist Item Schema

```json
{
  "checklist_item_id": "CHK-DAY-{emp_num}-{seq}",
  "item_name": "{Action} {Object}",
  "item_type": "substep",
  "action": "atomic_verb",
  "object": "simple_object",
  "tool": "inferred_tool",
  "estimated_duration": "10 seconds to 2 minutes",
  "source_responsibility": "RESP-ID",
  "granularity_score": 0.9
}
```

### Duration Estimation

```python
DURATION_MAP = {
  'click': '10 seconds',
  'open': '30 seconds',
  'save': '15 seconds',
  'upload': '1-2 minutes',
  'download': '1-2 minutes',
  'login': '30 seconds',
  'delete': '20 seconds',
  'copy': '15 seconds'
}
```

---

## TIER 2: STEP TEMPLATES (Execution Units)

### Classification Criteria

**Duration:** 3-10 minutes
**Complexity:** Cohesive execution unit
**Contains:** 2-5 checklist items (substeps)
**Requires:** Specific tool/skill
**Has:** Clear inputs, outputs, success criteria

### Step Verb Patterns

```
STEP_VERBS = [
  'configure', 'setup', 'create', 'update', 'analyze', 'review',
  'process', 'execute', 'validate', 'test', 'design', 'implement',
  'organize', 'document', 'prepare', 'compile', 'generate'
]
```

### Detection Rules

1. **Verb is execution-level** (in STEP_VERBS list)
2. **Has tool requirement** (tools array not empty)
3. **Clear inputs/outputs** (operates on defined objects)
4. **Frequency 2-10** (recurring execution unit)
5. **Form mix** (not purely base or ed, shows actual work)

### Step Template Schema

```json
{
  "step_template_id": "STEP-DAY-{emp_num}-{seq}",
  "step_template_name": "{Action} {Object}",
  "action": "step_verb",
  "object": "primary_object",
  "tool": "primary_tool",
  "estimated_duration": "3-10 minutes",
  "source_responsibility": "RESP-ID",
  "granularity_score": 0.5,
  "checklist_items": ["CHK-ID-1", "CHK-ID-2"],
  "inputs": ["input_object_1", "input_object_2"],
  "outputs": ["output_object"],
  "success_criteria": "Clear completion definition",
  "classification": {
    "tier": "step_template",
    "method": "direct",
    "confidence": 0.95
  }
}
```

---

## TIER 3: TASK TEMPLATES (Work Packages)

### Classification Criteria

**Duration:** 30 minutes - 4 hours
**Complexity:** Complete deliverable
**Contains:** 2-8 step templates
**Requires:** Multiple tools (2+)
**Produces:** Tangible output/deliverable

### Task-Level Patterns

**Complex verbs:** manage, coordinate, develop, build, deploy, integrate
**Abstract objects:** system, workflow, process, framework, infrastructure

### Detection Rules

1. **Multiple steps identified** (2+ related steps)
2. **Multiple tools** (tools array length >= 2)
3. **High frequency** (frequency >= 5)
4. **Complex deliverable** (not single file/action)
5. **Skill level intermediate/advanced**

### Task Template Schema

```json
{
  "task_template_id": "TASK-DAY-{emp_num}-{seq}",
  "task_template_name": "{Action} {Object} {Context}",
  "action": "primary_action",
  "object": "primary_object",
  "context": "purpose or scope",
  "department": "inferred_dept",
  "estimated_duration": "30 min - 4 hours",
  "steps_template": [
    {"step_template_id": "STEP-ID-1", "step_number": 1},
    {"step_template_id": "STEP-ID-2", "step_number": 2}
  ],
  "tools_required": ["tool1", "tool2"],
  "objects_involved": ["obj1", "obj2"],
  "source_responsibilities": ["RESP-ID-1", "RESP-ID-2"],
  "classification": {
    "tier": "task_template",
    "method": "bottom_up",
    "grouped_count": 2,
    "confidence": 0.8
  },
  "requires_manual_review": false
}
```

---

## BOTTOM-UP PROMOTION

### Methodology: Accumulate Related Steps

**Goal:** Identify 2-4 related step templates that form a coherent task

### Step 1: Group Related Steps

**Similarity Criteria:**
1. **Same domain** - Similar object types (all file operations, all data operations)
2. **Sequential flow** - Natural progression (prepare → execute → validate)
3. **Shared tools** - At least 1 tool in common
4. **Common goal** - Produce same or related deliverable

**Similarity Score Formula:**
```python
similarity = (
  same_domain_score * 0.3 +
  sequential_flow_score * 0.3 +
  shared_tools_score * 0.2 +
  common_goal_score * 0.2
)
```

### Step 2: Promotion Criteria

**Minimum Requirements:**
- **Min 2 steps** in group (user confirmed)
- **Coherent sequence** OR **shared deliverable** (one is sufficient)
- **Tool variety preferred** but not required

**Promotion Formula:**
```python
should_promote = (
  len(step_group) >= 2 AND
  (has_coherent_sequence OR has_shared_deliverable)
)
```

### Step 3: Task Generation

**Task Name:** `{Primary_Action} {Primary_Object} {Context}`

**Example:**
- Steps: "Organize files", "Organize folders", "Document structure"
- Task: "Organize Project File Structure for better discoverability"

**Context Inference:**
- Files + folders → "for better discoverability"
- Data + analysis → "for insights"
- Code + testing → "for quality assurance"

---

## TOP-DOWN DECOMPOSITION

### Methodology: Break Down Vague Tasks

**Goal:** Detect vague/complex tasks and decompose into concrete steps

### Step 1: Vagueness Detection

**Vague Verbs:**
```python
VAGUE_VERBS = [
  'manage', 'handle', 'coordinate', 'oversee',
  'improve', 'optimize', 'maintain', 'support'
]
```

**Abstract Objects:**
```python
ABSTRACT_OBJECTS = [
  'workflow', 'process', 'system', 'framework',
  'infrastructure', 'platform', 'environment'
]
```

**Vagueness Score (Threshold: 0.6):**
```python
vagueness_score = (
  has_vague_verb * 0.3 +
  has_abstract_object * 0.2 +
  no_tools_specified * 0.2 +
  skill_level_high * 0.3
)

if vagueness_score >= 0.6:
  decompose_task()
```

### Step 2: Select Decomposition Pattern

**Pattern Mapping:**

| Action Verb | Pattern | Steps |
|-------------|---------|-------|
| create | create_pattern | research → design → implement → test → document |
| manage | manage_pattern | assess → plan → execute → monitor → adjust |
| integrate | integrate_pattern | review → configure → test → validate → troubleshoot |
| deploy | deploy_pattern | review → configure → execute → validate → document |
| develop | develop_pattern | design → implement → test → refine → deploy |
| setup | setup_pattern | plan → configure → test → document |

### Step 3: Generate Step Sequence

**Pattern Example: create_pattern**

```json
[
  {
    "step_name": "Research {object} requirements",
    "action": "research",
    "tool": "Documentation",
    "duration": "15 minutes"
  },
  {
    "step_name": "Design {object} structure",
    "action": "design",
    "tool": "Figma",
    "duration": "30 minutes"
  },
  {
    "step_name": "Implement {object}",
    "action": "implement",
    "tool": "VS Code",
    "duration": "45 minutes"
  },
  {
    "step_name": "Test {object}",
    "action": "test",
    "tool": "Testing Framework",
    "duration": "20 minutes"
  },
  {
    "step_name": "Document {object}",
    "action": "document",
    "tool": "Markdown Editor",
    "duration": "15 minutes"
  }
]
```

### Step 4: Pattern-Based Tool Inference

**Tool Mapping:**
```python
TOOL_PATTERNS = {
  'research': 'Documentation',
  'design': 'Figma',
  'implement': 'VS Code',
  'test': 'Testing Framework',
  'document': 'Markdown Editor',
  'configure': 'Settings Panel',
  'execute': 'CLI/Terminal',
  'validate': 'Review Tools',
  'monitor': 'Dashboard',
  'analyze': 'Analytics Tool',
  'review': 'Review Platform',
  'plan': 'Planning Tool',
  'assess': 'Assessment Tool'
}
```

**Fallback:** If no pattern match, use original responsibility tools or 'Manual Process'

---

## GRANULARITY SCORE CALCULATION

**Score Range:** 0.0 (most atomic) to 1.0 (most complex)

```python
def calculate_granularity_score(responsibility):
  score = 0.0

  # Verb complexity (0.0-0.4)
  if action in ATOMIC_VERBS:
    score += 0.0
  elif action in STEP_VERBS:
    score += 0.2
  else:
    score += 0.4

  # Object complexity (0.0-0.3)
  if len(objects) == 1 and is_simple_object(objects[0]):
    score += 0.0
  elif len(objects) <= 2:
    score += 0.15
  else:
    score += 0.3

  # Tool complexity (0.0-0.2)
  score += min(len(tools) * 0.1, 0.2)

  # Frequency impact (0.0-0.1)
  score += min(frequency * 0.01, 0.1)

  return min(score, 1.0)
```

**Classification Thresholds:**
- **0.0 - 0.3:** Checklist Item
- **0.3 - 0.7:** Step Template
- **0.7 - 1.0:** Task Template

---

## MANUAL REVIEW FLAGS

### Flag for Review When:

1. **High vagueness score** (>= 0.7) - Decomposition may need validation
2. **Low confidence** (< 0.7) - Classification uncertain
3. **No similar patterns** - Unique responsibility not matching known patterns
4. **Complex promotion** - More than 4 steps grouped together
5. **Tool inference failed** - Couldn't map tools from patterns

### Review Report Format

```json
{
  "manual_review_required": {
    "high_priority": ["TASK-DAY-228-002"],
    "decompositions": ["RESP-003"],
    "low_confidence": ["STEP-DAY-228-005"],
    "unusual_patterns": []
  }
}
```

---

## PROCESSING WORKFLOW

### 1. Load Phase 3 Data
Read `phase_3_structured_daily_{id}.json`

### 2. Classify Granularity
For each responsibility:
- Calculate granularity score
- Assign tier (checklist/step/task)
- Tag with confidence level

### 3. Bottom-Up Grouping
- Find step-tier responsibilities
- Calculate similarity between pairs
- Group by similarity threshold (>= 0.6)
- Check promotion criteria
- Generate task templates

### 4. Top-Down Decomposition
- Find task-tier responsibilities
- Calculate vagueness score
- If >= 0.6, select decomposition pattern
- Generate step sequence
- Infer tools for each step

### 5. Generate Checklist Items
- Find checklist-tier responsibilities
- Create substep items
- Estimate durations
- Link to parent steps (if any)

### 6. Validate & Flag
- Check hierarchy relationships
- Validate parent-child links
- Flag items requiring manual review
- Generate review report

### 7. Output Generation
- Compile all classifications
- Calculate statistics
- Generate manual review markdown
- Write Phase 4 JSON

---

## VALIDATION RULES

### Hierarchy Validation

1. **Parent-Child Links Valid**
   - All step_template_ids referenced in tasks exist
   - All checklist_item_ids referenced in steps exist

2. **No Circular References**
   - Task doesn't reference itself
   - Step doesn't reference parent task

3. **ID Uniqueness**
   - All CHK-IDs unique
   - All STEP-IDs unique
   - All TASK-IDs unique

4. **Duration Consistency**
   - Task duration >= sum of step durations
   - Step duration >= sum of checklist durations

### Classification Validation

1. **Tier Consistency**
   - Checklist: score 0.0-0.3
   - Step: score 0.3-0.7
   - Task: score 0.7-1.0

2. **Promotion Logic**
   - Tasks from bottom-up have >= 2 steps
   - Tasks from decomposition have >= 3 steps

3. **Tool Requirements**
   - Steps have at least 1 tool
   - Tasks have at least 1 tool (can be inherited from steps)
   - Checklists may have 0 tools (manual actions)

---

## TOKEN EFFICIENCY

**Target:** Add ~400 tokens to Phase 3 output (still 65% reduction vs Phase 2)

**Efficiency Strategies:**
1. Use compact IDs (CHK-DAY-228-001)
2. Reference not duplicate (use IDs not full objects)
3. Minimal metadata (only essential fields)
4. Separate review file (not in main JSON)

**Phase 4 Token Budget:**
- Checklist items: ~100 tokens
- Step templates: ~150 tokens
- Task templates: ~100 tokens
- Decompositions: ~50 tokens

**Total:** ~400 tokens → Combined Pipeline: 1,600 tokens (65% reduction)

---

## VERSION HISTORY

**v1.0** - 2025-11-20
- Initial Phase 4 prompt
- Three-tier classification system
- Bottom-up promotion (min 2 steps)
- Top-down decomposition (threshold 0.6)
- Pattern-based tool inference
- Manual review workflow

---

**END OF PMT-070 PHASE 4 PROMPT**
