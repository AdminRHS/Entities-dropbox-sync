# TABLE: guide_formats

**Purpose:** Links guides to multiple format representations (Markdown, PDF, Video, Interactive, etc.)
**Relationships:** Child of `guides`, references `formats`

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | MEDIUMINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `guide_id` | MEDIUMINT UNSIGNED | FOREIGN KEY, NOT NULL | References guides.id |
| `format_id` | SMALLINT UNSIGNED | FOREIGN KEY, NOT NULL | References formats.id |
| `link` | VARCHAR(500) | NOT NULL | File path or URL to format |
| `object_id` | SMALLINT | NULL | Internal file system reference |
| `description` | VARCHAR(500) | NULL | Format-specific notes |
| `is_primary` | BOOLEAN | DEFAULT FALSE | Primary/default format flag |
| `format_version` | VARCHAR(20) | NULL | Format-specific version |
| `file_size_kb` | INT | NULL | File size in kilobytes |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When format was added |

---

## Sample Data

| id | guide_id | format_id | link | is_primary | format_version | file_size_kb | description |
|----|----------|-----------|------|------------|----------------|--------------|-------------|
| 1 | 1 | 1 | TSM-007_GUIDES/CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md | TRUE | 1.0 | 45 | Primary markdown source |
| 2 | 1 | 2 | TSM-007_GUIDES/exports/GDS-001_v1.0.pdf | FALSE | 1.0 | 320 | PDF export for printing |
| 3 | 2 | 1 | TSM-007_GUIDES/DATA_EXTRACTION_PROMPT.md | TRUE | 1.0 | 18 | Primary markdown source |
| 4 | 3 | 1 | TSM-007_GUIDES/Framework_Documentation/DESIGNER_INTEGRATION_SUMMARY.md | TRUE | 1.0 | 28 | Primary markdown source |
| 5 | 4 | 1 | TSM-007_GUIDES/Framework_Documentation/Framework_README.md | TRUE | 1.0 | 52 | Primary markdown source |
| 6 | 4 | 3 | https://internal-wiki.company.com/framework | FALSE | 1.0 | NULL | Interactive HTML version |
| 7 | 5 | 1 | TSM-007_GUIDES/Framework_Documentation/Implementation_Checklists.md | TRUE | 1.0 | 22 | Primary markdown source |
| 8 | 5 | 8 | TSM-007_GUIDES/exports/GDS-005_checklist.html | FALSE | 1.0 | 15 | Interactive checklist |
| 9 | 6 | 1 | TSM-007_GUIDES/Framework_Documentation/Knowledge_Library_Guide.md | TRUE | 1.0 | 38 | Primary markdown source |
| 10 | 7 | 1 | TSM-007_GUIDES/Framework_Documentation/Tool_Usage_Organizational_Proposals.md | TRUE | 1.0 | 62 | Primary markdown source |
| 11 | 8 | 1 | TSM-007_GUIDES/README_TAXONOMY_GUIDES.md | TRUE | 1.0 | 12 | Primary markdown source |
| 12 | 9 | 7 | TSM-007_GUIDES/Communication_Templates/GDS-009_SMM_Communication_Templates.json | TRUE | 1.0 | 8 | JSON template definitions |
| 13 | 10 | 1 | TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md | TRUE | 1.0 | 25 | Primary markdown tutorial |
| 14 | 10 | 2 | TSM-007_GUIDES/exports/GDS-010_Quick_Start_v1.0.pdf | FALSE | 1.0 | 180 | Printable PDF version |
| 15 | 10 | 4 | https://drive.google.com/drive/folders/VIDEO_ID_HERE | FALSE | 1.0 | 45000 | 5-minute video tutorial |
| 16 | 11 | 1 | TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md | TRUE | 1.0 | 32 | Primary markdown tutorial |
| 17 | 11 | 4 | https://drive.google.com/drive/folders/VIDEO_ID_HERE | FALSE | 1.0 | 78000 | 12-minute walkthrough video |
| 18 | 11 | 5 | https://miro.com/board/BOARD_ID_HERE | FALSE | 1.0 | NULL | Interactive entity hierarchy map |
| 19 | 12 | 1 | TSM-007_GUIDES/GDS-012_Template_Cross_Reference_Guide.md | TRUE | 1.0 | 28 | Primary markdown reference |
| 20 | 12 | 6 | https://notion.so/PAGE_ID_HERE | FALSE | 1.0 | NULL | Notion database view |

---

## Detailed Sample Entries

### Format Set 1: GDS-010 (Multi-Format Guide)

```json
[
  {
    "id": 13,
    "guide_id": 10,
    "format_id": 1,
    "link": "TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md",
    "object_id": 10013,
    "description": "Primary markdown tutorial with step-by-step instructions",
    "is_primary": true,
    "format_version": "1.0",
    "file_size_kb": 25,
    "created_at": "2025-11-22T09:00:00"
  },
  {
    "id": 14,
    "guide_id": 10,
    "format_id": 2,
    "link": "TSM-007_GUIDES/exports/GDS-010_Quick_Start_v1.0.pdf",
    "object_id": 10014,
    "description": "Printable PDF version for offline reference",
    "is_primary": false,
    "format_version": "1.0",
    "file_size_kb": 180,
    "created_at": "2025-11-22T09:15:00"
  },
  {
    "id": 15,
    "guide_id": 10,
    "format_id": 4,
    "link": "https://drive.google.com/drive/folders/1ABC123XYZ_VIDEO",
    "object_id": null,
    "description": "5-minute video tutorial - ideal for visual learners",
    "is_primary": false,
    "format_version": "1.0",
    "file_size_kb": 45000,
    "created_at": "2025-11-22T10:30:00"
  }
]
```

### Format Set 2: GDS-011 (Tutorial + Interactive)

```json
[
  {
    "id": 16,
    "guide_id": 11,
    "format_id": 1,
    "link": "TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md",
    "object_id": 10016,
    "description": "Comprehensive markdown tutorial with examples",
    "is_primary": true,
    "format_version": "1.0",
    "file_size_kb": 32,
    "created_at": "2025-11-22T09:30:00"
  },
  {
    "id": 17,
    "guide_id": 11,
    "format_id": 4,
    "link": "https://drive.google.com/drive/folders/1DEF456UVW_VIDEO",
    "object_id": null,
    "description": "12-minute walkthrough video with real examples",
    "is_primary": false,
    "format_version": "1.0",
    "file_size_kb": 78000,
    "created_at": "2025-11-22T11:00:00"
  },
  {
    "id": 18,
    "guide_id": 11,
    "format_id": 5,
    "link": "https://miro.com/board/uXjVKMN1234567890",
    "object_id": null,
    "description": "Interactive entity hierarchy map on Miro - zoom and explore template relationships",
    "is_primary": false,
    "format_version": "1.0",
    "file_size_kb": null,
    "created_at": "2025-11-22T12:00:00"
  }
]
```

---

## Format Type Distribution

| Format ID | Format Name | Guide Count | Total Formats | Percentage |
|-----------|-------------|-------------|---------------|------------|
| 1 | Markdown | 12 | 12 | 60% |
| 2 | PDF | 2 | 2 | 10% |
| 3 | Interactive HTML | 1 | 1 | 5% |
| 4 | Video Tutorial | 2 | 2 | 10% |
| 5 | Miro Board | 1 | 1 | 5% |
| 6 | Notion Page | 1 | 1 | 5% |
| 7 | JSON Schema | 1 | 1 | 5% |
| 8 | Interactive Checklist | 1 | 1 | 5% |

**Total Formats:** 20 format instances across 12 guides (avg 1.67 formats per guide)

---

## Multi-Format Guides

| Guide Code | Guide Name | Format Count | Formats Available |
|------------|------------|--------------|-------------------|
| GDS-010 | Quick Start PMT-032 v2.1 | 3 | MD, PDF, Video |
| GDS-011 | Entity Mapping Tutorial | 3 | MD, Video, Miro |
| GDS-012 | Template Cross-Reference | 2 | MD, Notion |
| GDS-005 | Implementation Checklists | 2 | MD, Interactive HTML |
| GDS-004 | Framework README | 2 | MD, Interactive HTML |
| GDS-001 | CRM Taxonomy | 2 | MD, PDF |

**6 guides** have multiple formats (50% of all guides)

---

## Primary Format Strategy

**Rule:** Every guide MUST have exactly ONE primary format (is_primary = TRUE)

**Current Primary Formats:**
- **Markdown (11 guides):** Standard for most documentation
- **JSON (1 guide):** For template definitions (GDS-009)

**Best Practices:**
1. Primary format should be the source of truth
2. All other formats are derived/exported from primary
3. Updates should be made to primary, then exported to others
4. Primary format typically has best editability

---

## Format Use Cases

### 1. Markdown (format_id: 1)
**Use Case:** Primary documentation format
**Advantages:** Version control friendly, easy to edit, searchable
**Examples:** All guides (GDS-001 through GDS-012)

### 2. PDF (format_id: 2)
**Use Case:** Printable, shareable, offline reference
**Advantages:** Fixed formatting, professional appearance, widely compatible
**Examples:** GDS-001, GDS-010

### 3. Interactive HTML (format_id: 3)
**Use Case:** Web-based guides with navigation
**Advantages:** Click-through navigation, search, responsive design
**Examples:** GDS-004 framework documentation

### 4. Video Tutorial (format_id: 4)
**Use Case:** Visual learners, walkthroughs
**Advantages:** Shows actual process, easier for beginners
**Examples:** GDS-010 (5 min), GDS-011 (12 min)

### 5. Miro Board (format_id: 5)
**Use Case:** Interactive diagrams, mind maps
**Advantages:** Zoomable, collaborative, visual exploration
**Examples:** GDS-011 entity hierarchy map

### 6. Notion Page (format_id: 6)
**Use Case:** Living documentation, databases
**Advantages:** Interactive tables, filters, collaborative editing
**Examples:** GDS-012 template cross-reference database

### 7. JSON Schema (format_id: 7)
**Use Case:** Machine-readable templates
**Advantages:** Programmatic access, validation, automation
**Examples:** GDS-009 communication templates

### 8. Interactive Checklist (format_id: 8)
**Use Case:** Step-by-step task completion
**Advantages:** Track progress, check off items, mobile-friendly
**Examples:** GDS-005 implementation checklists

---

## Link Types and Patterns

### Internal File Paths (Relative to ENTITIES/)
```
TSM-007_GUIDES/[filename].md
TSM-007_GUIDES/exports/[guide_code]_[description].[ext]
TSM-007_GUIDES/Framework_Documentation/[filename].md
TSM-007_GUIDES/Communication_Templates/[filename].json
```

### External URLs
```
https://drive.google.com/drive/folders/[VIDEO_ID]
https://miro.com/board/[BOARD_ID]
https://notion.so/[PAGE_ID]
https://internal-wiki.company.com/[page]
```

---

## File Size Considerations

| Size Range | Description | Examples |
|------------|-------------|----------|
| 0-50 KB | Small text files | Most markdown guides (GDS-008: 12 KB) |
| 50-100 KB | Medium documents | Framework docs (GDS-004: 52 KB, GDS-007: 62 KB) |
| 100-500 KB | Large PDFs | PDF exports (GDS-010: 180 KB, GDS-001: 320 KB) |
| 5-50 MB | Short videos | GDS-010 video: 45 MB (5 min) |
| 50-100 MB | Long videos | GDS-011 video: 78 MB (12 min) |
| NULL | External links | Miro, Notion (hosted externally) |

**Storage Planning:**
- Current total: ~125 KB (markdown) + 500 KB (PDFs) + 123 MB (videos) ≈ **123.6 MB**
- Projected (100 guides): ~12.5 MB (markdown) + 50 MB (PDFs) + 10 GB (videos) ≈ **10 GB**

---

## Query Examples

### Example 1: Get all formats for a guide
```markdown
Filter: guide_id = 10
Result:
- Markdown: TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md
- PDF: TSM-007_GUIDES/exports/GDS-010_Quick_Start_v1.0.pdf
- Video: https://drive.google.com/drive/folders/VIDEO_ID
```

### Example 2: Find primary format for a guide
```markdown
Filter: guide_id = 11 AND is_primary = TRUE
Result: TSM-007_GUIDES/GDS-011_Entity_Mapping_Tutorial.md
```

### Example 3: Find all video tutorials
```markdown
Filter: format_id = 4
Result: 2 videos (GDS-010, GDS-011)
```

### Example 4: Find guides with multiple formats
```markdown
Group by guide_id, having count(*) > 1
Result: 6 guides (GDS-001, 004, 005, 010, 011, 012)
```

### Example 5: Find all PDF exports
```markdown
Filter: format_id = 2
Result: 2 PDFs (GDS-001, GDS-010)
```

---

## Relationships

### Parent Table
- `guides.id` ← `guide_formats.guide_id` (many-to-one)

### Referenced Table
- `formats.id` ← `guide_formats.format_id` (many-to-one)

### Relationship Chain Example
```
guides (id=10, guide_code='GDS-010')
  └── guide_formats
       ├── (id=13, format_id=1) → formats (name='Markdown')
       ├── (id=14, format_id=2) → formats (name='PDF')
       └── (id=15, format_id=4) → formats (name='Video Tutorial')
```

---

## Data Validation Rules

1. **Link Format:** Must be valid relative path or absolute URL
2. **is_primary Constraint:** Exactly one format per guide must have is_primary=TRUE
3. **Unique Combination:** (guide_id, format_id, link) must be unique
4. **File Size:** Must be positive integer or NULL
5. **Format Version:** Should match semantic versioning pattern

---

## Future Enhancements

### Planned Additions
- `download_count` - Track format popularity
- `last_accessed_at` - Analytics for format usage
- `encoding` - Specify character encoding
- `language` - Multi-language support (en, es, fr, etc.)
- `thumbnail_url` - Preview images for videos/boards

### Format Conversion Workflow
```
Primary (MD) → Export → PDF, HTML, DOCX
              ↓
         Record in guide_formats
              ↓
         Track versions separately
```

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_guide_formats.md`
**Related Files:**
- [TABLE_guides.md](./TABLE_guides.md)
- [TABLE_formats.md](./TABLE_formats.md)
- [SCHEMA_OVERVIEW.md](./SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
