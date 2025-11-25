# TABLE: guide_milestone_templates

**Purpose:** Links guides to Milestone Templates (MLT-###) in the TASK_MANAGERS hierarchy (TSM-002)
**Relationships:** Junction table connecting `guides` to milestone templates

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `milestone_template_code` | VARCHAR(20) | NOT NULL | Milestone template code (MLT-###) |
| `relevance` | ENUM | DEFAULT 'recommended' | required/recommended/optional |
| `context` | VARCHAR(200) | NULL | Specific usage context |
| `display_order` | TINYINT | NULL | Order to present guides |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When link was created |

---

## Sample Data

| id | guide_id | milestone_template_code | relevance | context | display_order |
|----|----------|------------------------|-----------|---------|---------------|
| 1 | 10 | MLT-001 | recommended | Weekly report compilation milestone | 1 |
| 2 | 10 | MLT-002 | recommended | Monthly report aggregation milestone | 2 |
| 3 | 11 | MLT-005 | required | Task validation milestone - critical for entity mapping | 1 |
| 4 | 11 | MLT-007 | recommended | Quality assurance milestone for mappings | 2 |
| 5 | 12 | MLT-008 | optional | Template review and approval milestone | 1 |

---

## Milestone Coverage

| Milestone Code | Milestone Name (Example) | Guides Linked | Guide Codes |
|----------------|--------------------------|---------------|-------------|
| MLT-001 | Weekly Report Compilation | 1 | GDS-010 |
| MLT-002 | Monthly Report Aggregation | 1 | GDS-010 |
| MLT-005 | Task Validation | 1 | GDS-011 |
| MLT-007 | Quality Assurance | 1 | GDS-011 |
| MLT-008 | Template Review & Approval | 1 | GDS-012 |

**5 milestone templates** have guide cross-references

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_milestone_templates.md`
**Related Files:**
- [TABLE_guide_project_templates.md](./TABLE_guide_project_templates.md)
- [TABLE_guide_task_templates.md](./TABLE_guide_task_templates.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
