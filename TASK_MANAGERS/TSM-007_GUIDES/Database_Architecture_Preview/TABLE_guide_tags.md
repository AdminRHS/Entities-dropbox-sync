# TABLE: guide_tags

**Purpose:** Flexible categorization system for guides using tags
**Relationships:** Child of `guides` table

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `tag` | VARCHAR(50) | NOT NULL | Tag value |
| `tag_category` | VARCHAR(30) | NULL | Tag category for organization |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When tag was added |

---

## Sample Data

| id | guide_id | tag | tag_category | created_at |
|----|----------|-----|--------------|------------|
| 1 | 10 | beginner | skill_level | 2025-11-22T09:00:00 |
| 2 | 10 | onboarding | task_type | 2025-11-22T09:00:00 |
| 3 | 10 | daily_workflow | task_type | 2025-11-22T09:00:00 |
| 4 | 10 | required | priority | 2025-11-22T09:00:00 |
| 5 | 10 | whisper_flow | tool | 2025-11-22T09:00:00 |
| 6 | 10 | claude | tool | 2025-11-22T09:00:00 |
| 7 | 11 | intermediate | skill_level | 2025-11-22T09:30:00 |
| 8 | 11 | tutorial | task_type | 2025-11-22T09:30:00 |
| 9 | 11 | entity_mapping | topic | 2025-11-22T09:30:00 |
| 10 | 11 | taxonomy | topic | 2025-11-22T09:30:00 |
| 11 | 11 | miro | tool | 2025-11-22T09:30:00 |
| 12 | 12 | advanced | skill_level | 2025-11-22T10:00:00 |
| 13 | 12 | reference | task_type | 2025-11-22T10:00:00 |
| 14 | 12 | templates | topic | 2025-11-22T10:00:00 |
| 15 | 12 | cross_reference | topic | 2025-11-22T10:00:00 |
| 16 | 1 | intermediate | skill_level | 2025-11-15T10:30:00 |
| 17 | 1 | reference | task_type | 2025-11-15T10:30:00 |
| 18 | 1 | crm | topic | 2025-11-15T10:30:00 |
| 19 | 1 | taxonomy | topic | 2025-11-15T10:30:00 |
| 20 | 1 | llm_integration | topic | 2025-11-15T10:30:00 |

---

## Tag Categories

### skill_level Tags
- `beginner` - New users, basic concepts
- `intermediate` - Some experience required
- `advanced` - Expert-level, complex topics
- `expert` - Deep technical knowledge needed

### task_type Tags
- `onboarding` - New employee guides
- `tutorial` - Step-by-step instructions
- `reference` - Lookup documentation
- `troubleshooting` - Problem-solving guides
- `workflow` - Process documentation
- `daily_workflow` - Recurring daily tasks

### tool Tags
- `claude`, `gemini`, `chatgpt` - AI tools
- `lovable`, `bolt`, `replit` - Development platforms
- `firefly`, `runway`, `midjourney` - Design/media tools
- `gamma`, `canva`, `figma` - Presentation/design
- `notion`, `miro`, `airtable` - Collaboration
- `whisper_flow` - Transcription tool

### topic Tags
- `entity_mapping`, `taxonomy`, `crm` - Data organization
- `templates`, `cross_reference` - Template system
- `llm_integration`, `ai_workflows` - AI topics
- `reporting`, `analytics` - Data/reporting

### priority Tags
- `required` - Must read
- `recommended` - Should read
- `optional` - Nice to have

---

## Tag Distribution by Category

| Tag Category | Unique Tags | Total Uses | Example Tags |
|--------------|-------------|------------|--------------|
| skill_level | 3 | 4 | beginner, intermediate, advanced |
| task_type | 4 | 5 | onboarding, tutorial, reference, daily_workflow |
| tool | 4 | 4 | whisper_flow, claude, miro |
| topic | 7 | 7 | entity_mapping, taxonomy, templates, crm, llm_integration, cross_reference |
| priority | 1 | 1 | required |

**Total:** 19 unique tags across 20 tag assignments

---

## Guide Tagging Examples

### GDS-010: Quick Start PMT-032
```
Tags (6):
- skill_level: beginner
- task_type: onboarding, daily_workflow
- priority: required
- tool: whisper_flow, claude
```

### GDS-011: Entity Mapping Tutorial
```
Tags (5):
- skill_level: intermediate
- task_type: tutorial
- topic: entity_mapping, taxonomy
- tool: miro
```

### GDS-012: Template Cross-Reference Guide
```
Tags (4):
- skill_level: advanced
- task_type: reference
- topic: templates, cross_reference
```

### GDS-001: CRM Entities LLM Taxonomy Guide
```
Tags (5):
- skill_level: intermediate
- task_type: reference
- topic: crm, taxonomy, llm_integration
```

---

## Query Examples

### Example 1: Find all beginner guides
```markdown
Filter: tag = 'beginner' AND tag_category = 'skill_level'
Result: GDS-010
```

### Example 2: Find all onboarding guides
```markdown
Filter: tag = 'onboarding'
Result: GDS-010
```

### Example 3: Find guides about taxonomy
```markdown
Filter: tag = 'taxonomy'
Result: GDS-001, GDS-011
```

### Example 4: Find guides using Miro
```markdown
Filter: tag = 'miro' AND tag_category = 'tool'
Result: GDS-011
```

### Example 5: Find all tutorial-type guides
```markdown
Filter: tag = 'tutorial' AND tag_category = 'task_type'
Result: GDS-011
```

---

## Tag Cloud (Frequency)

```
taxonomy ████ (2)
intermediate ████ (2)
reference ████ (2)
entity_mapping ██ (1)
templates ██ (1)
cross_reference ██ (1)
beginner ██ (1)
advanced ██ (1)
onboarding ██ (1)
daily_workflow ██ (1)
tutorial ██ (1)
required ██ (1)
whisper_flow ██ (1)
claude ██ (1)
miro ██ (1)
crm ██ (1)
llm_integration ██ (1)
```

---

## Multi-Tag Search Examples

### Search: "beginner + onboarding"
```markdown
Find guides tagged with BOTH 'beginner' AND 'onboarding'
Result: GDS-010 (Quick Start Guide)
Use case: New employee first-day reading
```

### Search: "intermediate + taxonomy"
```markdown
Find guides tagged with BOTH 'intermediate' AND 'taxonomy'
Result: GDS-001, GDS-011
Use case: Understanding entity classification system
```

### Search: "tool:miro OR tool:claude"
```markdown
Find guides about Miro OR Claude
Result: GDS-010 (Claude), GDS-011 (Miro)
Use case: Tool-specific training
```

---

## Tag Best Practices

1. **Use Consistent Naming:** Lowercase, underscore-separated (e.g., `entity_mapping`, not `Entity-Mapping`)
2. **Categorize Tags:** Always specify tag_category for organization
3. **Limit Tags:** 3-7 tags per guide (avoid over-tagging)
4. **Multi-Value Tags:** Use multiple tags instead of combined tags (e.g., `ai` + `workflow`, not `ai_workflow`)
5. **Avoid Duplication:** Don't tag what's already in guide metadata (e.g., department_code)

---

## Future Enhancements

### Planned Additions
- `tag_weight` - Importance of tag to this guide (1-10)
- `auto_generated` - Whether tag was auto-assigned
- `created_by` - User who added the tag
- `tag_synonyms` - Alias tags for search (e.g., "AI" = "artificial_intelligence")

### Tag Hierarchy
```
topic
  ├── entity_management
  │   ├── entity_mapping
  │   ├── taxonomy
  │   └── crm
  ├── template_system
  │   ├── templates
  │   └── cross_reference
  └── ai_topics
      ├── llm_integration
      └── ai_workflows
```

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_tags.md`
**Related Files:**
- [TABLE_guides.md](./TABLE_guides.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
