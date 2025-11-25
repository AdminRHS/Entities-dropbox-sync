# TABLE: guide_project_templates

**Purpose:** Links guides to Project Templates (PRT-###) in the TASK_MANAGERS hierarchy (TSM-001)
**Relationships:** Junction table connecting `guides` to project templates

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `project_template_code` | VARCHAR(20) | NOT NULL | Project template code (PRT-###) |
| `relevance` | ENUM | DEFAULT 'recommended' | required/recommended/optional |
| `context` | VARCHAR(200) | NULL | Specific usage context |
| `display_order` | TINYINT | NULL | Order to present guides |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When link was created |

---

## Sample Data

| id | guide_id | project_template_code | relevance | context | display_order |
|----|----------|----------------------|-----------|---------|---------------|
| 1 | 10 | PRT-001 | required | Daily Report Collection project - essential for all employees | 1 |
| 2 | 11 | PRT-001 | recommended | Entity mapping applies to all daily report activities | 2 |
| 3 | 12 | PRT-002 | recommended | Template cross-referencing for content creation pipeline | 1 |
| 4 | 12 | PRT-003 | optional | Advanced template management for large projects | 2 |
| 5 | 4 | PRT-004 | required | Framework documentation for system architecture project | 1 |
| 6 | 9 | PRT-005 | required | Communication templates for social media management project | 1 |

---

## Project Template Coverage

| Project Code | Project Name (Example) | Guides Linked | Guide Codes |
|--------------|------------------------|---------------|-------------|
| PRT-001 | Daily Report Collection | 2 | GDS-010, GDS-011 |
| PRT-002 | Content Creation Pipeline | 1 | GDS-012 |
| PRT-003 | Template Management | 1 | GDS-012 |
| PRT-004 | System Architecture | 1 | GDS-004 |
| PRT-005 | Social Media Management | 1 | GDS-009 |

**5 project templates** have guide cross-references

---

## Hierarchical Propagation Example

```
Guide: GDS-010 linked to PRT-001 (Daily Report Collection)
  ↓
Propagates to child milestones:
  ├── MLT-001 (Weekly Report Compilation)
  ├── MLT-002 (Monthly Report Aggregation)
  └── MLT-005 (Task Validation)
      ↓
  Propagates to child tasks:
      ├── TST-042 (Daily Report Submission) ← Also has direct link
      ├── TST-043 (Whisper Flow Recording)
      └── TST-044 (Entity Mapping Validation)
```

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_project_templates.md`
**Related Files:**
- [TABLE_guides.md](./TABLE_guides.md)
- [TABLE_guide_milestone_templates.md](./TABLE_guide_milestone_templates.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
