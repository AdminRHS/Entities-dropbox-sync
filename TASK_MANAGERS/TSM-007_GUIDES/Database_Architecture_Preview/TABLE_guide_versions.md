# TABLE: guide_versions

**Purpose:** Complete audit trail of guide changes over time
**Relationships:** Child of `guides` table

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `version` | VARCHAR(20) | NOT NULL | Version number (semantic versioning) |
| `changes` | TEXT | NOT NULL | Description of changes in this version |
| `change_type` | ENUM | NOT NULL | Type of change |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When version was created |
| `created_by` | SMALLINT | NULL | User ID who made the change |

### Enum Values

**change_type:**
- `created` - Initial version
- `content_update` - Content modifications
- `format_added` - New format added
- `template_link` - Template cross-reference added/removed
- `minor_fix` - Typos, formatting fixes
- `major_revision` - Significant rewrite

---

## Sample Data

| id | guide_id | version | changes | change_type | created_at | created_by |
|----|----------|---------|---------|-------------|------------|------------|
| 1 | 10 | 1.0 | Initial creation of Quick Start Guide for PMT-032 v2.1 | created | 2025-11-22T09:00:00 | 1 |
| 2 | 10 | 1.1 | Added video tutorial format, clarified Whisper Flow setup | format_added | 2025-11-22T10:30:00 | 1 |
| 3 | 10 | 1.2 | Fixed typos in section 3, updated screenshot | minor_fix | 2025-11-22T14:00:00 | 1 |
| 4 | 11 | 1.0 | Initial creation of Entity Mapping Tutorial | created | 2025-11-22T09:30:00 | 1 |
| 5 | 11 | 1.1 | Added Miro board for visual hierarchy, linked to TST-067 | format_added | 2025-11-22T12:00:00 | 1 |
| 6 | 12 | 1.0 | Initial creation of Template Cross-Reference Guide | created | 2025-11-22T10:00:00 | 1 |
| 7 | 1 | 1.0 | Initial CRM Entities LLM Taxonomy Guide | created | 2025-11-15T10:30:00 | 1 |
| 8 | 1 | 1.1 | Updated entity classification rules, added 5 new entity types | content_update | 2025-11-18T09:00:00 | 1 |
| 9 | 1 | 1.2 | Major revision: Restructured taxonomy hierarchy, added LLM prompt examples | major_revision | 2025-11-20T11:00:00 | 1 |
| 10 | 1 | 2.0 | Complete rewrite for v2.0 framework compatibility | major_revision | 2025-11-21T10:00:00 | 1 |

---

## Version History Example: GDS-001

```
GDS-001: CRM Entities LLM Taxonomy Guide
  ├── v1.0 (2025-11-15) - Initial creation
  ├── v1.1 (2025-11-18) - Content update: Added 5 entity types
  ├── v1.2 (2025-11-20) - Major revision: Restructured hierarchy
  └── v2.0 (2025-11-21) - Major revision: v2.0 framework compatibility
      ↑ Current version
```

---

## Version History Example: GDS-010

```
GDS-010: Quick Start Guide - PMT-032 v2.1
  ├── v1.0 (2025-11-22 09:00) - Initial creation
  ├── v1.1 (2025-11-22 10:30) - Format added: Video tutorial
  └── v1.2 (2025-11-22 14:00) - Minor fix: Typos and screenshot
      ↑ Current version
```

---

## Change Type Distribution

| Change Type | Count | Percentage | Use Case |
|-------------|-------|------------|----------|
| created | 3 | 30% | Initial guide creation |
| format_added | 2 | 20% | New format versions |
| content_update | 1 | 10% | Content modifications |
| major_revision | 3 | 30% | Significant rewrites |
| minor_fix | 1 | 10% | Typos and formatting |
| template_link | 0 | 0% | Template cross-reference changes |

---

## Version Numbering Strategy

**Semantic Versioning: MAJOR.MINOR.PATCH**

- **MAJOR (x.0.0):** Complete rewrite, framework changes, breaking changes
  - Example: v1.0 → v2.0 (framework compatibility update)
- **MINOR (1.x.0):** New content sections, format additions, template links
  - Example: v1.0 → v1.1 (added video tutorial)
- **PATCH (1.0.x):** Typos, minor fixes, screenshot updates
  - Example: v1.1 → v1.2 (fixed typos)

---

## Query Examples

### Example 1: Get version history for a guide
```markdown
Filter: guide_id = 1
Order by: version ASC
Result: 4 versions (1.0, 1.1, 1.2, 2.0)
```

### Example 2: Find all major revisions
```markdown
Filter: change_type = 'major_revision'
Result: GDS-001 v1.2, GDS-001 v2.0, [others]
```

### Example 3: Track who made changes
```markdown
Filter: created_by = 1
Group by: guide_id
Result: User 1 created all current guide versions
```

### Example 4: Find recent changes (last 7 days)
```markdown
Filter: created_at >= (NOW() - INTERVAL 7 DAY)
Order by: created_at DESC
Result: All GDS-010, GDS-011, GDS-012 versions
```

---

## Rollback Strategy

**To rollback to previous version:**

1. Query version history: `SELECT * FROM guide_versions WHERE guide_id = X ORDER BY version DESC`
2. Identify target version
3. Restore content from that version record
4. Create new version entry documenting the rollback

**Example:**
```
Current: GDS-001 v2.0 (broken)
Rollback to: GDS-001 v1.2 (stable)
New entry: GDS-001 v2.1 (rollback to v1.2, reverted breaking changes)
```

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_versions.md`
**Related Files:**
- [TABLE_guides.md](./TABLE_guides.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
