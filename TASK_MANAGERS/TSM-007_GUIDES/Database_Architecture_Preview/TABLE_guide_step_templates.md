# TABLE: guide_step_templates

**Purpose:** Links guides to Step Templates (STP-###) in the TASK_MANAGERS hierarchy (TSM-004)
**Relationships:** Junction table connecting `guides` to step templates

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `step_template_code` | VARCHAR(20) | NOT NULL | Step template code (STP-###) |
| `relevance` | ENUM | DEFAULT 'recommended' | required/recommended/optional |
| `context` | VARCHAR(200) | NULL | Specific usage context |
| `display_order` | TINYINT | NULL | Order to present guides |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When link was created |

---

## Sample Data

| id | guide_id | step_template_code | relevance | context | display_order |
|----|----------|-------------------|-----------|---------|---------------|
| 1 | 10 | STP-127 | required | Whisper Flow recording initialization | 1 |
| 2 | 10 | STP-128 | required | Activity logging format | 2 |
| 3 | 10 | STP-129 | recommended | Timestamp documentation | 3 |
| 4 | 10 | STP-130 | recommended | Transcript embedding | 4 |
| 5 | 11 | STP-089 | required | Entity ID assignment step | 1 |
| 6 | 11 | STP-090 | required | Entity validation rules | 2 |
| 7 | 11 | STP-091 | recommended | Hierarchy navigation | 3 |
| 8 | 11 | STP-092 | recommended | Cross-reference verification | 4 |
| 9 | 12 | STP-150 | optional | Template metadata documentation | 1 |
| 10 | 12 | STP-151 | optional | Cross-reference creation | 2 |

---

## Step Template Coverage

| Step Code | Step Name (Example) | Guides Linked | Guide Codes |
|-----------|---------------------|---------------|-------------|
| STP-127 | Whisper Flow Initialization | 1 | GDS-010 |
| STP-128 | Activity Logging Format | 1 | GDS-010 |
| STP-129 | Timestamp Documentation | 1 | GDS-010 |
| STP-130 | Transcript Embedding | 1 | GDS-010 |
| STP-089 | Entity ID Assignment | 1 | GDS-011 |
| STP-090 | Entity Validation Rules | 1 | GDS-011 |
| STP-091 | Hierarchy Navigation | 1 | GDS-011 |
| STP-092 | Cross-Reference Verification | 1 | GDS-011 |
| STP-150 | Template Metadata Documentation | 1 | GDS-012 |
| STP-151 | Cross-Reference Creation | 1 | GDS-012 |

**10 step templates** have guide cross-references

---

## Granular Guide Application Example

```
Task: TST-042 (Daily Report Submission)
  ├── STP-127: Whisper Flow Initialization
  │   └── Guide: GDS-010 (required) - "How to set up Whisper Flow"
  ├── STP-128: Activity Logging Format
  │   └── Guide: GDS-010 (required) - "Activity section format"
  ├── STP-089: Entity ID Assignment
  │   └── Guide: GDS-011 (required) - "How to find TST codes"
  └── STP-090: Entity Validation
      └── Guide: GDS-011 (required) - "Validation checklist"
```

This granular linking allows users to see exactly which guide applies to which specific step within a task.

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_step_templates.md`
**Related Files:**
- [TABLE_guide_task_templates.md](./TABLE_guide_task_templates.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
