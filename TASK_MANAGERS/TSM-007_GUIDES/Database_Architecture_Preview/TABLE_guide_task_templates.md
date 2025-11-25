# TABLE: guide_task_templates

**Purpose:** Links guides to Task Templates (TST-###) in the TASK_MANAGERS hierarchy
**Relationships:** Junction table connecting `guides` to task templates (TSM-003)

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `task_template_code` | VARCHAR(20) | NOT NULL | Task template code (TST-###) |
| `relevance` | ENUM | DEFAULT 'recommended' | How important is this guide |
| `context` | VARCHAR(200) | NULL | Specific usage context |
| `display_order` | TINYINT | NULL | Order to present guides |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When link was created |

### Enum Values

**relevance:**
- `required` - Must read before using this template (blocking)
- `recommended` - Should read for best practices and full understanding
- `optional` - Additional context available if needed

---

## Sample Data

| id | guide_id | task_template_code | relevance | context | display_order | created_at |
|----|----------|-------------------|-----------|---------|---------------|------------|
| 1 | 10 | TST-042 | required | Daily report submission workflow | 1 | 2025-11-22T09:00:00 |
| 2 | 10 | TST-043 | required | Whisper Flow recording setup | 2 | 2025-11-22T09:00:00 |
| 3 | 10 | TST-044 | recommended | Entity mapping validation | 3 | 2025-11-22T09:00:00 |
| 4 | 10 | TST-045 | recommended | Activity time tracking | 4 | 2025-11-22T09:00:00 |
| 5 | 11 | TST-042 | recommended | Entity ID assignment for daily tasks | 1 | 2025-11-22T09:30:00 |
| 6 | 11 | TST-044 | required | Entity mapping validation process | 2 | 2025-11-22T09:30:00 |
| 7 | 11 | TST-018 | required | Entity classification and tagging | 3 | 2025-11-22T09:30:00 |
| 8 | 11 | TST-067 | recommended | Task-to-milestone linking | 4 | 2025-11-22T09:30:00 |
| 9 | 11 | TST-089 | recommended | Template hierarchy navigation | 5 | 2025-11-22T09:30:00 |
| 10 | 12 | TST-001 | optional | Template creation workflow | 1 | 2025-11-22T10:00:00 |
| 11 | 12 | TST-015 | optional | Template documentation standards | 2 | 2025-11-22T10:00:00 |
| 12 | 12 | TST-023 | recommended | Cross-reference validation | 3 | 2025-11-22T10:00:00 |
| 13 | 1 | TST-018 | required | CRM entity classification | 1 | 2025-11-15T10:30:00 |
| 14 | 1 | TST-019 | recommended | Entity relationship mapping | 2 | 2025-11-15T10:30:00 |
| 15 | 9 | TST-101 | required | Social media post creation | 1 | 2025-11-18T14:00:00 |
| 16 | 9 | TST-102 | required | Content template application | 2 | 2025-11-18T14:00:00 |
| 17 | 9 | TST-103 | recommended | Multi-channel posting workflow | 3 | 2025-11-18T14:00:00 |

---

## Detailed Sample Entries

### Cross-Reference Set 1: GDS-010 → Task Templates

**Guide:** GDS-010 "Quick Start Guide - PMT-032 v2.1"

```json
[
  {
    "id": 1,
    "guide_id": 10,
    "task_template_code": "TST-042",
    "relevance": "required",
    "context": "Daily report submission workflow - comprehensive guide for completing and submitting daily logs using PMT-032 framework",
    "display_order": 1,
    "created_at": "2025-11-22T09:00:00"
  },
  {
    "id": 2,
    "guide_id": 10,
    "task_template_code": "TST-043",
    "relevance": "required",
    "context": "Whisper Flow recording setup - essential for capturing meeting transcripts and activity narration",
    "display_order": 2,
    "created_at": "2025-11-22T09:00:00"
  },
  {
    "id": 3,
    "guide_id": 10,
    "task_template_code": "TST-044",
    "relevance": "recommended",
    "context": "Entity mapping validation - ensures correct TST/MLT/PRT code assignment",
    "display_order": 3,
    "created_at": "2025-11-22T09:00:00"
  },
  {
    "id": 4,
    "guide_id": 10,
    "task_template_code": "TST-045",
    "relevance": "recommended",
    "context": "Activity time tracking - best practices for accurate hour estimation",
    "display_order": 4,
    "created_at": "2025-11-22T09:00:00"
  }
]
```

### Cross-Reference Set 2: GDS-011 → Task Templates

**Guide:** GDS-011 "Entity Mapping Tutorial"

```json
[
  {
    "id": 5,
    "guide_id": 11,
    "task_template_code": "TST-042",
    "relevance": "recommended",
    "context": "Entity ID assignment for daily tasks - demonstrates how to find and apply correct TST codes when logging daily activities",
    "display_order": 1,
    "created_at": "2025-11-22T09:30:00"
  },
  {
    "id": 6,
    "guide_id": 11,
    "task_template_code": "TST-044",
    "relevance": "required",
    "context": "Entity mapping validation process - step-by-step tutorial for verifying entity relationships",
    "display_order": 2,
    "created_at": "2025-11-22T09:30:00"
  },
  {
    "id": 7,
    "guide_id": 11,
    "task_template_code": "TST-018",
    "relevance": "required",
    "context": "Entity classification and tagging - comprehensive guide to CRM entity taxonomy application",
    "display_order": 3,
    "created_at": "2025-11-22T09:30:00"
  },
  {
    "id": 8,
    "guide_id": 11,
    "task_template_code": "TST-067",
    "relevance": "recommended",
    "context": "Task-to-milestone linking - understanding parent-child relationships in template hierarchy",
    "display_order": 4,
    "created_at": "2025-11-22T09:30:00"
  },
  {
    "id": 9,
    "guide_id": 11,
    "task_template_code": "TST-089",
    "relevance": "recommended",
    "context": "Template hierarchy navigation - how to traverse TSM-001 → TSM-002 → TSM-003 → TSM-004 relationships",
    "display_order": 5,
    "created_at": "2025-11-22T09:30:00"
  }
]
```

---

## Relevance Distribution

| Relevance Level | Link Count | Percentage | When to Use |
|-----------------|------------|------------|-------------|
| required | 7 | 41% | Guide is mandatory before using template |
| recommended | 9 | 53% | Guide significantly improves template usage |
| optional | 1 | 6% | Guide provides supplementary context |

**Total Links:** 17 cross-references

---

## Guide Coverage Analysis

| Guide Code | Guide Name | Task Templates Linked | Relevance Mix |
|------------|------------|----------------------|---------------|
| GDS-001 | CRM Taxonomy | 2 | 1 required, 1 recommended |
| GDS-009 | SMM Communication Templates | 3 | 2 required, 1 recommended |
| GDS-010 | Quick Start PMT-032 | 4 | 2 required, 2 recommended |
| GDS-011 | Entity Mapping Tutorial | 5 | 2 required, 3 recommended |
| GDS-012 | Template Cross-Reference | 3 | 0 required, 1 recommended, 2 optional |

**5 guides** have task template cross-references (42% of all guides)

---

## Task Template Coverage Analysis

### High-Usage Templates (3+ guides linked)

| Template Code | Template Name (Example) | Guides Linked | Notes |
|---------------|------------------------|---------------|-------|
| TST-042 | Daily Report Submission | 2 | GDS-010, GDS-011 |
| TST-044 | Entity Mapping Validation | 2 | GDS-010, GDS-011 |

### Medium-Usage Templates (1-2 guides linked)

| Template Code | Guides Linked | Guide Codes |
|---------------|---------------|-------------|
| TST-018 | 2 | GDS-001, GDS-011 |
| TST-043 | 1 | GDS-010 |
| TST-045 | 1 | GDS-010 |
| TST-067 | 1 | GDS-011 |
| TST-089 | 1 | GDS-011 |
| TST-001 | 1 | GDS-012 |
| TST-015 | 1 | GDS-012 |
| TST-023 | 1 | GDS-012 |
| TST-019 | 1 | GDS-001 |
| TST-101 | 1 | GDS-009 |
| TST-102 | 1 | GDS-009 |
| TST-103 | 1 | GDS-009 |

**14 unique task templates** have guide cross-references

---

## Task Template Categories (Inferred)

### Daily Operations
- TST-042: Daily Report Submission
- TST-043: Whisper Flow Recording
- TST-044: Entity Mapping Validation
- TST-045: Activity Time Tracking

### Entity Management
- TST-018: Entity Classification
- TST-019: Entity Relationship Mapping
- TST-067: Task-to-Milestone Linking
- TST-089: Template Hierarchy Navigation

### Content Creation
- TST-101: Social Media Post Creation
- TST-102: Content Template Application
- TST-103: Multi-Channel Posting

### Template Management
- TST-001: Template Creation Workflow
- TST-015: Template Documentation Standards
- TST-023: Cross-Reference Validation

---

## Display Order Strategy

**Purpose:** Control the sequence in which guides are presented to users

**Ordering Logic:**
1. **Required guides first** (relevance = 'required')
2. **Within same relevance, order by display_order** (ascending)
3. **Optional guides last** (relevance = 'optional')

**Example:** When viewing TST-042, guides appear in this order:
1. GDS-010 (required, display_order=1) - Quick Start Guide
2. GDS-011 (recommended, display_order=1) - Entity Mapping Tutorial

---

## Context Field Usage

**Purpose:** Provide specific information about how the guide relates to this particular template

**Best Practices:**
- Keep under 200 characters
- Explain the specific application to this template
- Highlight what the user will learn
- Use action-oriented language

**Examples:**
- ✅ Good: "Whisper Flow recording setup - essential for capturing meeting transcripts"
- ❌ Bad: "Guide about Whisper Flow"
- ✅ Good: "Entity mapping validation process - step-by-step tutorial for verifying relationships"
- ❌ Bad: "Validation guide"

---

## Query Examples

### Example 1: Find all guides for a task template
```markdown
Filter: task_template_code = 'TST-042'
Order by: relevance DESC, display_order ASC
Result:
1. GDS-010 (required, order 1) - Daily report submission workflow
2. GDS-011 (recommended, order 1) - Entity ID assignment for daily tasks
```

### Example 2: Find all required guides for a task
```markdown
Filter: task_template_code = 'TST-044' AND relevance = 'required'
Result: GDS-011 - Entity mapping validation process
```

### Example 3: Find all task templates for a guide
```markdown
Filter: guide_id = 11
Order by: display_order ASC
Result: TST-042, TST-044, TST-018, TST-067, TST-089 (5 templates)
```

### Example 4: Find guides with most task template coverage
```markdown
Group by: guide_id
Order by: COUNT(*) DESC
Result:
1. GDS-011 (5 templates)
2. GDS-010 (4 templates)
3. GDS-009, GDS-012 (3 templates each)
4. GDS-001 (2 templates)
```

### Example 5: Find task templates with no guides
```markdown
Query: All TST codes NOT IN (SELECT DISTINCT task_template_code FROM guide_task_templates)
Result: ~44 task templates without guides (assuming 58 total task templates)
Opportunity: Create guides for high-usage templates
```

---

## Relationship Chains

### Chain Example 1: User → Task → Guide
```
User starts task: TST-042 (Daily Report Submission)
  ↓
System queries: guide_task_templates WHERE task_template_code = 'TST-042'
  ↓
Returns guides: GDS-010, GDS-011
  ↓
User selects: GDS-010
  ↓
System queries: guide_formats WHERE guide_id = 10
  ↓
User chooses format: Video Tutorial
  ↓
System plays: 5-minute Quick Start video
```

### Chain Example 2: Guide → Templates → Steps
```
User views guide: GDS-011 (Entity Mapping Tutorial)
  ↓
Guide shows "Related Templates" section:
  ├── TST-042 (Daily Report Submission)
  ├── TST-044 (Entity Mapping Validation) ← Primary
  ├── TST-018 (Entity Classification)
  ├── TST-067 (Task-to-Milestone Linking)
  └── TST-089 (Template Hierarchy Navigation)
      ↓
User clicks: TST-044
      ↓
System queries: guide_step_templates WHERE linked via TST-044's steps
      ↓
Shows: Step-by-step breakdown with guide references
```

---

## Data Validation Rules

1. **task_template_code Format:** Must match pattern `TST-\d{3}` (e.g., TST-042)
2. **task_template_code Existence:** Must exist in TSM-003 templates registry
3. **Unique Combination:** (guide_id, task_template_code) must be unique
4. **display_order:** Must be positive integer (1-255)
5. **context Length:** 1-200 characters if provided
6. **At Least One Required:** Each task template should have at least one guide (aspirational)

---

## Future Enhancements

### Planned Additions
- `completion_required` - Must complete guide before task can start
- `quiz_id` - Link to comprehension quiz
- `estimated_impact_min` - Time saved by reading guide
- `user_rating` - Average user helpfulness rating
- `view_count` - Track guide usage per template
- `last_updated_at` - Track when cross-reference was last reviewed

### Bi-Directional Navigation
```
Task Template View:
  "Recommended Guides" section
  Shows: GDS-010, GDS-011 with relevance badges

Guide View:
  "Applicable Templates" section
  Shows: TST-042, TST-043, TST-044, TST-045
```

---

## Integration with Other Tables

### Sibling Tables (Same Pattern)
- `guide_project_templates` - Links to TSM-001 (PRT-###)
- `guide_milestone_templates` - Links to TSM-002 (MLT-###)
- `guide_step_templates` - Links to TSM-004 (STP-###)

### Hierarchical Propagation
When guide is linked to task template TST-042:
- Can optionally link to all step templates under TST-042
- Can link to parent milestone template (if specified)
- Can link to parent project template (if specified)

**Propagation Example:**
```
GDS-010 linked to TST-042
  ↓
Auto-suggest links:
  ├── STP-127 (Whisper Flow Recording) ← Step under TST-042
  ├── STP-128 (Activity Logging) ← Step under TST-042
  ├── MLT-005 (Task Validation) ← Parent milestone
  └── PRT-001 (Daily Report Collection) ← Parent project
```

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_task_templates.md`
**Related Files:**
- [TABLE_guides.md](./TABLE_guides.md)
- [TABLE_guide_project_templates.md](./TABLE_guide_project_templates.md)
- [TABLE_guide_milestone_templates.md](./TABLE_guide_milestone_templates.md)
- [TABLE_guide_step_templates.md](./TABLE_guide_step_templates.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
