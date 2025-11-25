# Cross-Reference: Template Hierarchy Integration

**Purpose:** How guides integrate across the 4-level TASK_MANAGERS template hierarchy
**Last Updated:** 2025-11-22

---

## Template Hierarchy Overview

```
TASK_MANAGERS Hierarchy (4 Levels)
│
├── TSM-001: Project Templates (PRT-###)
│   │
│   ├── TSM-002: Milestone Templates (MLT-###)
│   │   │
│   │   ├── TSM-003: Task Templates (TST-###)
│   │   │   │
│   │   │   └── TSM-004: Step Templates (STP-###)
```

---

## Integration Pattern 1: Top-Down Guide Application

### Concept
A guide linked at a higher level (e.g., Project) applies to all child templates unless overridden.

### Example: GDS-010 → PRT-001

```
GDS-010 (Quick Start PMT-032) linked to PRT-001 [Required]
  │
  ├─→ Applies to ALL milestones under PRT-001
  │     ├── MLT-001 (Weekly Report Compilation)
  │     ├── MLT-002 (Monthly Report Aggregation)
  │     └── MLT-005 (Task Validation)
  │
  ├─→ Applies to ALL tasks under PRT-001
  │     ├── TST-042 (Daily Report Submission)
  │     ├── TST-043 (Whisper Flow Recording)
  │     ├── TST-044 (Entity Mapping Validation)
  │     └── TST-045 (Activity Time Tracking)
  │
  └─→ Applies to ALL steps under PRT-001 tasks
        ├── STP-127 (Whisper Flow Initialization)
        ├── STP-128 (Activity Logging Format)
        ├── STP-129 (Timestamp Documentation)
        └── STP-130 (Transcript Embedding)
```

**Use Case:** Organizational-wide process guides that apply to entire projects

---

## Integration Pattern 2: Bottom-Up Guide Specificity

### Concept
Guides linked at lower levels (e.g., Step) provide granular, specific instructions.

### Example: GDS-011 → STP-089

```
STP-089 (Entity ID Assignment) ← GDS-011 [Required]
  │
  ├─→ Specific to this step only
  │    "How to find and assign TST codes"
  │
  └─→ Parent task TST-044 also has GDS-011 [Required]
       "Broader entity mapping validation context"
```

**Use Case:** Detailed how-to guides for specific procedures

---

## Integration Pattern 3: Multi-Level Coverage

### Concept
A single guide provides value at multiple hierarchy levels with different contexts.

### Example: GDS-011 Multi-Level Integration

```
Level 1: PRT-001 (Daily Report Collection) [Recommended]
         Context: "Entity mapping applies to all daily report activities"

Level 2: MLT-005 (Task Validation) [Required]
         Context: "Task validation milestone - critical for entity mapping"

Level 3: TST-042, TST-044, TST-018, TST-067, TST-089 [Required/Recommended]
         Context: Specific tasks requiring entity mapping

Level 4: STP-089, STP-090, STP-091, STP-092 [Required/Recommended]
         Context: Granular steps for entity operations
```

**Result:** User sees GDS-011 at every relevant level with appropriate context

---

## Relevance Cascading Strategy

### Relevance Rules Across Levels

```
Project: Required
  └── Milestone: Inherits as Recommended
      └── Task: Inherits as Recommended
          └── Step: Inherits as Optional
```

**Example:**
```
GDS-010 → PRT-001 [Required]
  ├── MLT-001 [Recommended] (inherited)
  ├── TST-042 [Required] (explicit override)
  └── STP-127 [Required] (explicit override)
```

**Logic:** Explicit links override inherited relevance levels

---

## Hierarchy Navigation for Users

### Scenario 1: User Starts at Project Level

**User:** "I'm starting PRT-001 (Daily Report Collection)"

**System shows:**
```
Recommended Guides:
1. GDS-010 (Quick Start PMT-032) [Required]
   "Daily Report Collection project - essential for all employees"

2. GDS-011 (Entity Mapping Tutorial) [Recommended]
   "Entity mapping applies to all daily report activities"

Click to drill down:
→ View milestones under this project
→ View all tasks under this project
→ View task-specific guides
```

---

### Scenario 2: User Starts at Task Level

**User:** "I'm working on TST-042 (Daily Report Submission)"

**System shows:**
```
Task-Specific Guides:
1. GDS-010 (Quick Start PMT-032) [Required]
   "Daily report submission workflow"

2. GDS-011 (Entity Mapping Tutorial) [Recommended]
   "Entity ID assignment for daily tasks"

Parent Context:
↑ PRT-001 (Daily Report Collection) - See project-level guides
↑ MLT-001 (Weekly Report Compilation) - See milestone guides

Child Steps:
↓ STP-127 (Whisper Flow Init) - GDS-010 [Required]
↓ STP-128 (Activity Logging) - GDS-010 [Required]
↓ STP-089 (Entity ID Assignment) - GDS-011 [Required]
↓ STP-090 (Entity Validation) - GDS-011 [Required]
```

---

### Scenario 3: User Starts at Step Level

**User:** "I'm on step STP-127 (Whisper Flow Initialization)"

**System shows:**
```
Step-Specific Guide:
1. GDS-010 (Quick Start PMT-032) [Required]
   Section: "Whisper Flow recording setup"
   Estimated: 2 min read
   Formats: [Markdown] [PDF] [Video 5min]

Context Chain:
↑ TST-042 (Daily Report Submission) - See task guides
↑ MLT-001 (Weekly Report Compilation) - See milestone guides
↑ PRT-001 (Daily Report Collection) - See project guides
```

---

## Cross-Level Guide Presentation

### Smart Guide Deduplication

**Problem:** GDS-010 appears at 4 levels (PRT, MLT, TST, STP). Don't show duplicates.

**Solution:** Show guide once with multi-level context

```
GDS-010 (Quick Start PMT-032)

Applies to:
  ├── PRT-001 (Daily Report Collection) [Required]
  ├── MLT-001, MLT-002 (Report Compilation) [Recommended]
  ├── TST-042, TST-043, TST-044, TST-045 (Report Tasks) [Required/Recommended]
  └── STP-127, STP-128, STP-129, STP-130 (Report Steps) [Required/Recommended]

Primary Format: Markdown (7 min read)
Also Available: PDF, Video (5 min)

[View Guide] [View for Current Level]
```

---

## Template Hierarchy Query Examples

### Query 1: Get all guides for a project and its children

```
Input: PRT-001
Output:
  Direct links: GDS-010 [R], GDS-011 [r]
  Via milestones: (none additional)
  Via tasks: (none additional - TST-042 has same guides)
  Via steps: (none additional - steps have same guides)

Result: 2 unique guides (GDS-010, GDS-011)
```

### Query 2: Get guides for a specific task including inherited

```
Input: TST-044 (Entity Mapping Validation)
Output:
  Direct task links: GDS-010 [r], GDS-011 [R]
  From parent MLT-005: GDS-011 [R] (duplicate, show highest relevance)
  From parent PRT-001: GDS-010 [R], GDS-011 [r]

Merged Result:
  - GDS-010 [Required] (from PRT-001)
  - GDS-011 [Required] (from TST-044, MLT-005)
```

### Query 3: Find all templates for a guide

```
Input: GDS-011
Output:
  Projects: PRT-001 [r]
  Milestones: MLT-005 [R], MLT-007 [r]
  Tasks: TST-042 [r], TST-044 [R], TST-018 [R], TST-067 [r], TST-089 [r]
  Steps: STP-089 [R], STP-090 [R], STP-091 [r], STP-092 [r]

Total: 11 template links across all 4 levels
```

---

## Implementation Examples

### Example 1: Project Template View

**File:** `TSM-001/PRT-001_Daily_Report_Collection.md`

```markdown
# PRT-001: Daily Report Collection

## Related Guides

### Required Reading
- [GDS-010: Quick Start Guide - PMT-032 v2.1](../../TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md)
  Essential for all employees. Daily Report Collection project overview.

### Recommended Reading
- [GDS-011: Entity Mapping Tutorial](../../TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md)
  Entity mapping applies to all daily report activities.

## Milestones
- [MLT-001: Weekly Report Compilation](../TSM-002/MLT-001_Weekly_Report_Compilation.md)
- [MLT-002: Monthly Report Aggregation](../TSM-002/MLT-002_Monthly_Report_Aggregation.md)
- [MLT-005: Task Validation](../TSM-002/MLT-005_Task_Validation.md)
```

---

### Example 2: Task Template View

**File:** `TSM-003/TST-042_Daily_Report_Submission.md`

```markdown
# TST-042: Daily Report Submission

## Required Guides
- [GDS-010: Quick Start PMT-032](../../TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md)
  **Section:** Daily report submission workflow
  **Formats:** [MD](link) | [PDF](link) | [Video 5min](link)

## Recommended Guides
- [GDS-011: Entity Mapping Tutorial](../../TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md)
  **Section:** Entity ID assignment for daily tasks

## Steps
1. [STP-127: Whisper Flow Initialization](../TSM-004/STP-127_Whisper_Flow_Init.md) → Guide: GDS-010 [R]
2. [STP-128: Activity Logging Format](../TSM-004/STP-128_Activity_Logging.md) → Guide: GDS-010 [R]
3. [STP-089: Entity ID Assignment](../TSM-004/STP-089_Entity_ID_Assignment.md) → Guide: GDS-011 [R]
4. [STP-090: Entity Validation](../TSM-004/STP-090_Entity_Validation.md) → Guide: GDS-011 [R]

## Parent Templates
- **Milestone:** [MLT-001: Weekly Report Compilation](../TSM-002/MLT-001.md)
- **Project:** [PRT-001: Daily Report Collection](../TSM-001/PRT-001.md)
```

---

## Benefits of Multi-Level Integration

### 1. Contextual Relevance
Users see guides appropriate to their current level in the hierarchy

### 2. Reduced Redundancy
Same guide referenced multiple times without duplication

### 3. Navigation Flexibility
Users can drill up or down to find related guides

### 4. Inheritance Clarity
Clear rules for how guides propagate through hierarchy

### 5. Maintenance Efficiency
Update guide link once at appropriate level, applies to children

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Cross_Reference_Maps/XREF_Template_Hierarchy_Integration.md`
**Related Files:**
- [XREF_Guides_to_Templates_Matrix.md](./XREF_Guides_to_Templates_Matrix.md)
- [Database_Architecture_Preview/SCHEMA_OVERVIEW.md](../Database_Architecture_Preview/SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
