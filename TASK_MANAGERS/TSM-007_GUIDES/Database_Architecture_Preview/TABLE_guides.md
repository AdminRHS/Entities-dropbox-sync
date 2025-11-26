# TABLE: guides

**Purpose:** Core table storing all guide metadata and content information
**Relationships:** Parent to all other guide-related tables

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_code` | VARCHAR(20) | UNIQUE, NOT NULL | Standard code (GDS-###) |
| `name` | VARCHAR(100) | NOT NULL | Guide title |
| `entity_id` | TINYINT | NULL | CRM entity reference |
| `department_code` | CHAR(3) | NULL | Department (AID, DGN, DEV, etc.) |
| `category` | VARCHAR(50) | NULL | Category classification |
| `scope` | ENUM | DEFAULT 'global' | Usage scope (see below) |
| `priority` | ENUM | DEFAULT 'medium' | Importance level |
| `status` | ENUM | DEFAULT 'draft' | Lifecycle status |
| `version` | VARCHAR(20) | DEFAULT '1.0' | Current version number |
| `description` | TEXT | NULL | Detailed description |
| `estimated_read_time_min` | TINYINT | NULL | Reading time in minutes |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Creation timestamp |
| `created_by` | SMALLINT | NULL | User ID of creator |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Last update timestamp |

### Enum Values

**scope:**
- `global` - Applicable across entire organization
- `department` - Specific to one department
- `project_template` - Linked to specific project template(s)
- `milestone_template` - Linked to milestone template(s)
- `task_template` - Linked to task template(s)
- `step_template` - Linked to step template(s)
- `multi_template` - Linked to multiple template levels

**priority:**
- `critical` - Essential, blocking without it
- `high` - Very important, should read ASAP
- `medium` - Important for full understanding
- `low` - Nice to have, supplementary

**status:**
- `draft` - Being created, not ready
- `review` - Ready for review/approval
- `active` - Published and in use
- `deprecated` - Outdated, scheduled for removal

---

## Sample Data (Current Guides)

| id | guide_code | name | entity_id | dept | category | scope | priority | status | version | est_read_min |
|----|------------|------|-----------|------|----------|-------|----------|--------|---------|--------------|
| 1 | GDS-001 | CRM Entities LLM Taxonomy Guide | NULL | AID | Taxonomy | global | high | active | 1.0 | 15 |
| 2 | GDS-002 | Data Extraction Prompt Guide | NULL | AID | Extraction | global | medium | active | 1.0 | 8 |
| 3 | GDS-003 | Designer Integration Summary | NULL | DGN | Integration | department | medium | active | 1.0 | 12 |
| 4 | GDS-004 | Framework Documentation README | NULL | AID | Framework | global | high | active | 1.0 | 20 |
| 5 | GDS-005 | Implementation Checklists | NULL | AID | Implementation | global | high | active | 1.0 | 10 |
| 6 | GDS-006 | Knowledge Library Guide | NULL | AID | Library | global | medium | active | 1.0 | 18 |
| 7 | GDS-007 | Tool Usage Organizational Proposals | NULL | AID | Tools | global | low | active | 1.0 | 25 |
| 8 | GDS-008 | Taxonomy Guides README | NULL | AID | Taxonomy | global | medium | active | 1.0 | 5 |
| 9 | GDS-009 | SMM Communication Templates | NULL | AID | Templates | task_template | medium | active | 1.0 | 10 |
| 10 | GDS-010 | Quick Start Guide - PMT-032 v2.1 | NULL | AID | Tutorial | task_template | critical | active | 1.0 | 7 |
| 11 | GDS-011 | Entity Mapping Tutorial | NULL | AID | Tutorial | multi_template | high | active | 1.0 | 12 |
| 12 | GDS-012 | Template Cross-Reference Guide | NULL | AID | Reference | global | medium | active | 1.0 | 15 |

---

## Sample Data (Detailed View)

### Guide 1: GDS-001
```json
{
  "id": 1,
  "guide_code": "GDS-001",
  "name": "CRM Entities LLM Taxonomy Guide",
  "entity_id": null,
  "department_code": "AID",
  "category": "Taxonomy",
  "scope": "global",
  "priority": "high",
  "status": "active",
  "version": "1.0",
  "description": "Comprehensive taxonomy system for CRM entities with LLM integration patterns. Covers entity classification, naming conventions, relationship mapping, and AI-assisted data extraction.",
  "estimated_read_time_min": 15,
  "created_at": "2025-11-15T10:30:00",
  "created_by": 1,
  "updated_at": "2025-11-15T10:30:00"
}
```

### Guide 10: GDS-010 (New)
```json
{
  "id": 10,
  "guide_code": "GDS-010",
  "name": "Quick Start Guide - PMT-032 v2.1",
  "entity_id": null,
  "department_code": "AID",
  "category": "Tutorial",
  "scope": "task_template",
  "priority": "critical",
  "status": "active",
  "version": "1.0",
  "description": "Quick start tutorial for daily report submission using PMT-032 v2.1 framework. Covers Whisper Flow setup, activity logging, entity mapping, and report submission workflow. Essential for all employees.",
  "estimated_read_time_min": 7,
  "created_at": "2025-11-22T09:00:00",
  "created_by": 1,
  "updated_at": "2025-11-22T09:00:00"
}
```

### Guide 11: GDS-011 (New)
```json
{
  "id": 11,
  "guide_code": "GDS-011",
  "name": "Entity Mapping Tutorial",
  "entity_id": null,
  "department_code": "AID",
  "category": "Tutorial",
  "scope": "multi_template",
  "priority": "high",
  "status": "active",
  "version": "1.0",
  "description": "Step-by-step tutorial for mapping tasks to entity IDs (TST, MLT, PRT codes). Covers entity hierarchy, code lookup, validation rules, and common mapping scenarios across all template levels.",
  "estimated_read_time_min": 12,
  "created_at": "2025-11-22T09:30:00",
  "created_by": 1,
  "updated_at": "2025-11-22T09:30:00"
}
```

### Guide 12: GDS-012 (New)
```json
{
  "id": 12,
  "guide_code": "GDS-012",
  "name": "Template Cross-Reference Guide",
  "entity_id": null,
  "department_code": "AID",
  "category": "Reference",
  "scope": "global",
  "priority": "medium",
  "status": "active",
  "version": "1.0",
  "description": "Reference guide for understanding and creating cross-references between guides and TASK_MANAGERS templates. Covers hierarchy navigation, relevance levels, context documentation, and best practices for linking guides to templates.",
  "estimated_read_time_min": 15,
  "created_at": "2025-11-22T10:00:00",
  "created_by": 1,
  "updated_at": "2025-11-22T10:00:00"
}
```

---

## Department Distribution

| Department Code | Department Name | Guide Count | Percentage |
|-----------------|-----------------|-------------|------------|
| AID | AI Department | 11 | 91.7% |
| DGN | Design | 1 | 8.3% |
| DEV | Development | 0 | 0% |
| FIN | Finance | 0 | 0% |
| HRM | Human Resources | 0 | 0% |
| LGN | Lead Generation | 0 | 0% |
| SLS | Sales | 0 | 0% |
| VID | Video Production | 0 | 0% |

**Expansion Opportunities:** Create guides for DEV, FIN, HRM, LGN, SLS, VID departments.

---

## Category Distribution

| Category | Guide Count | Examples |
|----------|-------------|----------|
| Tutorial | 3 | GDS-010, GDS-011 |
| Taxonomy | 2 | GDS-001, GDS-008 |
| Framework | 1 | GDS-004 |
| Implementation | 1 | GDS-005 |
| Integration | 1 | GDS-003 |
| Library | 1 | GDS-006 |
| Tools | 1 | GDS-007 |
| Extraction | 1 | GDS-002 |
| Templates | 1 | GDS-009 |
| Reference | 1 | GDS-012 |

---

## Scope Distribution

| Scope | Guide Count | Use Case |
|-------|-------------|----------|
| global | 8 | Organization-wide applicability |
| department | 1 | Design-specific processes |
| task_template | 2 | Linked to specific tasks |
| multi_template | 1 | Spans multiple template levels |
| project_template | 0 | Reserved for project-level guides |
| milestone_template | 0 | Reserved for milestone guides |
| step_template | 0 | Reserved for granular step guides |

---

## Priority Distribution

| Priority | Guide Count | When to Use |
|----------|-------------|-------------|
| critical | 1 | Blocking workflow without it (GDS-010) |
| high | 3 | Very important for success |
| medium | 7 | Important for full understanding |
| low | 1 | Supplementary, nice to have |

---

## Status Lifecycle

```
draft → review → active → deprecated
  ↓       ↓        ↓          ↓
 (12)     (0)     (12)       (0)
```

**Current State:** All 12 guides are in `active` status, none in draft or review.

---

## Query Examples

### Example 1: Find all critical guides
```markdown
Filter: priority = 'critical'
Result: GDS-010 (Quick Start Guide - PMT-032 v2.1)
```

### Example 2: Find all guides for AI Department
```markdown
Filter: department_code = 'AID'
Result: 11 guides (GDS-001, 002, 004, 005, 006, 007, 008, 009, 010, 011, 012)
```

### Example 3: Find all tutorial guides
```markdown
Filter: category = 'Tutorial'
Result: 3 guides (GDS-010, GDS-011, GDS-012)
```

### Example 4: Find guides linked to task templates
```markdown
Filter: scope IN ('task_template', 'multi_template')
Result: 3 guides (GDS-009, GDS-010, GDS-011)
```

### Example 5: Find guides under 10 minutes
```markdown
Filter: estimated_read_time_min <= 10
Result: 5 guides (GDS-002, GDS-005, GDS-008, GDS-009, GDS-010)
```

---

## Relationships to Other Tables

### Outgoing Relationships (guides is parent)
- `guides` → `guide_formats` (one-to-many)
- `guides` → `guide_versions` (one-to-many)
- `guides` → `guide_tags` (one-to-many)
- `guides` → `guide_project_templates` (one-to-many)
- `guides` → `guide_milestone_templates` (one-to-many)
- `guides` → `guide_task_templates` (one-to-many)
- `guides` → `guide_step_templates` (one-to-many)
- `guides` → `guide_tools` (one-to-many)

### Example Relationship Chain
```
GDS-010 (guides)
  ├── 3 formats (guide_formats): Markdown, PDF, Video
  ├── 2 versions (guide_versions): 1.0, 1.1
  ├── 5 tags (guide_tags): beginner, tutorial, daily_workflow, onboarding, required
  ├── 1 project link (guide_project_templates): PRT-001
  ├── 0 milestone links (guide_milestone_templates)
  ├── 4 task links (guide_task_templates): TST-042, TST-043, TST-044, TST-045
  ├── 8 step links (guide_step_templates): STP-127, STP-128, STP-089, etc.
  └── 3 tool links (guide_tools): Whisper Flow, Claude, Gemini
```

---

## Indexing Considerations (Future Database)

```sql
-- Primary and unique indexes
PRIMARY KEY (id)
UNIQUE INDEX idx_guide_code (guide_code)

-- Search performance
FULLTEXT INDEX idx_search (name, description)

-- Filter performance
INDEX idx_department_category (department_code, category)
INDEX idx_scope_priority (scope, priority)
INDEX idx_status (status)

-- Sort performance
INDEX idx_created_at (created_at DESC)
INDEX idx_updated_at (updated_at DESC)
```

---

## Data Validation Rules

1. **guide_code Format:** Must match pattern `GDS-\d{3}` (e.g., GDS-010)
2. **name Length:** 10-100 characters
3. **department_code:** Must exist in departments registry
4. **version Format:** Semantic versioning (e.g., 1.0, 1.1, 2.0)
5. **estimated_read_time_min:** 1-120 minutes (reasonable range)
6. **Uniqueness:** No duplicate guide_codes allowed

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guides.md`
**Related Files:**
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)
- [TABLE_guide_formats.md](./TABLE_guide_formats.md)
- [TABLE_guide_task_templates.md](./TABLE_guide_task_templates.md)

**Last Updated:** 2025-11-22
