# Database Architecture Preview - Schema Overview

**Version:** 1.0
**Created:** 2025-11-22
**Purpose:** Markdown-based preview of proposed database schema for manual architecture review before technical implementation

---

## Architecture Philosophy

This preview simulates a relational database structure using markdown files to enable:
- **Human-reviewable architecture** before coding begins
- **Cross-reference validation** between guides and TASK_MANAGERS templates
- **Scalability assessment** for future content publishing
- **Relationship modeling** across 4-level template hierarchy

---

## Database Schema Visualization

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CORE SCHEMA                                  │
└─────────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│     guides       │ ◄──────────────────┐
│ ──────────────── │                    │
│ id (PK)          │                    │
│ guide_code       │                    │
│ name             │                    │
│ entity_id        │                    │
│ department_code  │                    │
│ category         │                    │
│ scope            │                    │
│ priority         │                    │
│ status           │                    │
│ version          │                    │
│ description      │                    │
│ est_read_time    │                    │
│ created_at       │                    │
│ created_by       │                    │
│ updated_at       │                    │
└──────────────────┘                    │
         │                              │
         │                              │
         ├──────────────────────────────┼────────────────────┐
         │                              │                    │
         ▼                              ▼                    ▼
┌──────────────────┐          ┌──────────────────┐  ┌──────────────────┐
│  guide_formats   │          │  guide_versions  │  │   guide_tags     │
│ ──────────────── │          │ ──────────────── │  │ ──────────────── │
│ id (PK)          │          │ id (PK)          │  │ id (PK)          │
│ guide_id (FK)    │          │ guide_id (FK)    │  │ guide_id (FK)    │
│ format_id (FK)   │          │ version          │  │ tag              │
│ link             │          │ changes          │  │ category         │
│ object_id        │          │ created_at       │  └──────────────────┘
│ description      │          │ created_by       │
│ is_primary       │          └──────────────────┘
│ format_version   │
└──────────────────┘
         │
         ▼
┌──────────────────┐
│     formats      │
│ ──────────────── │
│ id (PK)          │
│ name             │
│ file_extension   │
│ mime_type        │
└──────────────────┘


┌─────────────────────────────────────────────────────────────────────┐
│              TEMPLATE HIERARCHY RELATIONSHIPS                        │
└─────────────────────────────────────────────────────────────────────┘

         ┌──────────────────┐
         │     guides       │
         └──────────────────┘
                  │
                  │
      ┌───────────┼───────────┬───────────┬───────────┐
      │           │           │           │           │
      ▼           ▼           ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│  guide_  │ │  guide_  │ │  guide_  │ │  guide_  │ │  guide_  │
│ project_ │ │milestone_│ │  task_   │ │  step_   │ │  tools   │
│templates │ │templates │ │templates │ │templates │ │          │
├──────────┤ ├──────────┤ ├──────────┤ ├──────────┤ ├──────────┤
│guide_id  │ │guide_id  │ │guide_id  │ │guide_id  │ │guide_id  │
│prt_code  │ │mlt_code  │ │tst_code  │ │stp_code  │ │tool_id   │
│relevance │ │relevance │ │relevance │ │relevance │ │usage_ctx │
│context   │ │context   │ │context   │ │context   │ └──────────┘
│order     │ │order     │ │order     │ │order     │
└──────────┘ └──────────┘ └──────────┘ └──────────┘

         TASK_MANAGERS Template Hierarchy:
         TSM-001 (PRT) → TSM-002 (MLT) → TSM-003 (TST) → TSM-004 (STP)
```

---

## Table Descriptions

### Core Tables

#### 1. **guides** (Core Entity)
Primary table storing all guide metadata and content references.

**Key Features:**
- Unique `guide_code` (GDS-###) for consistent referencing
- Department and category classification
- Scope indicator (global, department, template-specific, multi-template)
- Priority and status lifecycle management
- Version tracking
- Full-text searchable name and description

**Use Cases:**
- Central registry of all guides
- Quick lookup by code or category
- Filtering by department, priority, or status
- Version history tracking

#### 2. **guide_formats** (Multi-Format Support)
Links guides to multiple format representations (MD, PDF, Video, Interactive, etc.)

**Key Features:**
- One guide can have many formats
- Primary format designation
- Format-specific versioning
- External link storage (up to 500 chars)
- Object ID for internal file references

**Use Cases:**
- User selects preferred learning format
- Track format availability
- Manage format-specific updates
- Support diverse learning styles

#### 3. **formats** (Format Registry)
Master list of supported content formats.

**Current Formats:**
- Markdown (`.md`)
- PDF (`.pdf`)
- Interactive HTML (`.html`)
- Video Tutorial (`.mp4`, `.webm`)
- Miro Board (URL)
- Notion Page (URL)
- JSON Schema (`.json`)
- Interactive Checklist (`.html`)

#### 4. **guide_versions** (Version History)
Complete audit trail of guide changes over time.

**Key Features:**
- Maintains version number history
- Tracks what changed in each version
- Records who made changes and when
- Enables rollback if needed

#### 5. **guide_tags** (Flexible Categorization)
Tag-based organization system for guides.

**Tag Categories:**
- `skill_level`: beginner, intermediate, advanced, expert
- `task_type`: onboarding, troubleshooting, reference, tutorial, workflow
- `tool`: claude, gemini, lovable, firefly, runway, gamma
- `custom`: any project-specific tags

---

### Template Relationship Tables

#### 6. **guide_project_templates** (TSM-001 Integration)
Links guides to Project Templates (PRT-###).

**Example Relationships:**
- `GDS-010` (Quick Start PMT-032) → `PRT-001` (Daily Report Collection)
- `GDS-012` (Template Cross-Reference) → `PRT-002` (Content Creation Pipeline)

#### 7. **guide_milestone_templates** (TSM-002 Integration)
Links guides to Milestone Templates (MLT-###).

**Example Relationships:**
- `GDS-011` (Entity Mapping Tutorial) → `MLT-005` (Task Validation Milestone)

#### 8. **guide_task_templates** (TSM-003 Integration)
Links guides to Task Templates (TST-###).

**Example Relationships:**
- `GDS-010` → `TST-042` (Daily Report Submission)
- `GDS-001` (CRM Taxonomy) → `TST-018` (Entity Classification)

#### 9. **guide_step_templates** (TSM-004 Integration)
Links guides to Step Templates (STP-###).

**Example Relationships:**
- `GDS-010` → `STP-127` (Whisper Flow Recording)
- `GDS-011` → `STP-089` (Entity ID Assignment)

#### 10. **guide_tools** (Tool Integration)
Links guides to specific tools in the technology stack.

**Tool Registry:**
- Claude, Gemini, ChatGPT
- Lovable, Bolt, Replit
- Firefly, Runway, Midjourney
- Gamma, Canva, Figma
- Notion, Miro, Airtable

---

## Relationship Patterns

### 1. One-to-Many Relationships
```
guides (1) ──── (many) guide_formats
guides (1) ──── (many) guide_versions
guides (1) ──── (many) guide_tags
guides (1) ──── (many) guide_project_templates
guides (1) ──── (many) guide_milestone_templates
guides (1) ──── (many) guide_task_templates
guides (1) ──── (many) guide_step_templates
guides (1) ──── (many) guide_tools
```

### 2. Many-to-Many Relationships (via Junction Tables)
```
guides ←→ project_templates  (via guide_project_templates)
guides ←→ milestone_templates (via guide_milestone_templates)
guides ←→ task_templates     (via guide_task_templates)
guides ←→ step_templates     (via guide_step_templates)
guides ←→ tools              (via guide_tools)
```

### 3. Template Hierarchy Propagation
When a guide is linked to a Project Template, it can optionally cascade to:
- All Milestone Templates under that Project
- All Task Templates under those Milestones
- All Step Templates under those Tasks

**Relevance Levels:**
- `required`: Must read before using template
- `recommended`: Should read for best practices
- `optional`: Additional context available

---

## Data Flow Example

### Scenario: User needs help with Daily Report Submission

```
1. User searches: "daily report how to"
   ↓
2. Query matches guides table:
   - guide_code: GDS-010
   - name: "Quick Start Guide - PMT-032 v2.1"
   - scope: "task_template"
   ↓
3. System retrieves guide_formats:
   - Format 1: Markdown (primary)
   - Format 2: PDF
   - Format 3: Video Tutorial (5 min)
   ↓
4. User selects Video format
   ↓
5. System retrieves from guide_task_templates:
   - TST-042: Daily Report Submission
   - TST-043: Whisper Flow Setup
   - TST-044: Entity Mapping Validation
   ↓
6. System suggests related guides via guide_tags:
   - Tag "daily_workflow" matches:
     - GDS-011: Entity Mapping Tutorial
     - GDS-012: Template Cross-Reference Guide
```

---

## Scalability Considerations

### Current Scale (Preview Phase)
- **Guides**: 12 guides (GDS-001 to GDS-012)
- **Formats**: 8 format types
- **Template Links**: ~30-50 cross-references
- **Departments**: 8 departments (AID, DGN, DEV, HRM, LGN, SLS, VID, FNC)

### Projected Scale (Year 1)
- **Guides**: 50-100 guides
- **Formats**: 10-12 format types
- **Template Links**: 200-500 cross-references
- **Tags**: 50-100 unique tags

### Indexing Strategy (Future Database)
```sql
-- Primary indexes
PRIMARY KEY: guides.id, guides.guide_code
UNIQUE INDEX: guides.guide_code

-- Search indexes
FULLTEXT INDEX: guides.name, guides.description
INDEX: guides.department_code, guides.category, guides.scope

-- Foreign key indexes
INDEX: guide_formats.guide_id
INDEX: guide_task_templates.guide_id, guide_task_templates.tst_code
INDEX: guide_versions.guide_id, guide_versions.version
```

---

## Migration Path

### Phase 1: Markdown Preview (Current)
- ✅ Create simulated tables as markdown files
- ✅ Validate relationships manually
- ✅ Review with stakeholders
- ✅ Iterate on schema design

### Phase 2: Spreadsheet Prototype (Optional)
- Import markdown tables to Google Sheets or Airtable
- Test data entry workflows
- Validate cross-references with formulas
- Generate reports to verify completeness

### Phase 3: Database Implementation (Future)
- Convert schema to SQL (MySQL/PostgreSQL)
- Build migration scripts for existing guides
- Implement API layer
- Create admin interface

### Phase 4: Publishing Integration (Future)
- Connect to website CMS
- Enable format selection
- Implement search functionality
- Track usage analytics

---

## File Reference

All simulated tables are located in:
```
ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/
├── SCHEMA_OVERVIEW.md (this file)
├── TABLE_guides.md
├── TABLE_guide_formats.md
├── TABLE_guide_task_templates.md
├── TABLE_guide_project_templates.md
├── TABLE_guide_milestone_templates.md
├── TABLE_guide_step_templates.md
├── TABLE_guide_versions.md
├── TABLE_guide_tags.md
├── TABLE_formats.md
└── TABLE_guide_tools.md
```

Cross-reference maps are located in:
```
ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Cross_Reference_Maps/
├── XREF_Guides_to_Templates_Matrix.md
├── XREF_Template_Hierarchy_Integration.md
└── XREF_Department_Guide_Coverage.md
```

---

## Next Steps

1. ✅ Review this schema overview
2. ⏳ Examine individual table simulations
3. ⏳ Validate cross-reference mappings
4. ⏳ Test sample queries against markdown tables
5. ⏳ Iterate on schema design based on feedback
6. ⏳ Approve for technical implementation OR continue refining

---

**Maintained By:** AI Department
**Last Updated:** 2025-11-22
**Status:** Draft - Awaiting Review
