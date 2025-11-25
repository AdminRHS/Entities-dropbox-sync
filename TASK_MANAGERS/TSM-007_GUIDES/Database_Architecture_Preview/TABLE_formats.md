# TABLE: formats

**Purpose:** Master registry of supported content formats for guides
**Relationships:** Referenced by `guide_formats`

---

## Table Schema

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | SMALLINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| `name` | VARCHAR(50) | UNIQUE, NOT NULL | Format name |
| `file_extension` | VARCHAR(10) | NULL | File extension (if applicable) |
| `mime_type` | VARCHAR(100) | NULL | MIME type for web delivery |
| `is_downloadable` | BOOLEAN | DEFAULT TRUE | Can be downloaded |
| `requires_internet` | BOOLEAN | DEFAULT FALSE | Requires online access |
| `description` | VARCHAR(200) | NULL | Format description |

---

## Sample Data

| id | name | file_extension | mime_type | is_downloadable | requires_internet | description |
|----|------|----------------|-----------|-----------------|-------------------|-------------|
| 1 | Markdown | .md | text/markdown | TRUE | FALSE | Plain text markdown format |
| 2 | PDF | .pdf | application/pdf | TRUE | FALSE | Portable Document Format |
| 3 | Interactive HTML | .html | text/html | TRUE | FALSE | Web-based interactive guide |
| 4 | Video Tutorial | .mp4 | video/mp4 | TRUE | FALSE | Video walkthrough |
| 5 | Miro Board | NULL | NULL | FALSE | TRUE | Interactive Miro whiteboard |
| 6 | Notion Page | NULL | NULL | FALSE | TRUE | Notion collaborative doc |
| 7 | JSON Schema | .json | application/json | TRUE | FALSE | Machine-readable template |
| 8 | Interactive Checklist | .html | text/html | TRUE | FALSE | Checkable task list |
| 9 | Google Slides | NULL | NULL | TRUE | TRUE | Presentation format |
| 10 | Figma Board | NULL | NULL | FALSE | TRUE | Design collaboration board |

---

## Format Categories

### Downloadable Formats (is_downloadable = TRUE)
- Markdown, PDF, Interactive HTML, Video, JSON, Interactive Checklist, Google Slides
- **7 formats** can be downloaded and used offline

### Online-Only Formats (requires_internet = TRUE)
- Miro Board, Notion Page, Google Slides, Figma Board
- **4 formats** require internet connection

---

## Usage Statistics

| Format ID | Format Name | Times Used | Percentage |
|-----------|-------------|------------|------------|
| 1 | Markdown | 12 | 60% |
| 2 | PDF | 2 | 10% |
| 4 | Video Tutorial | 2 | 10% |
| 3 | Interactive HTML | 1 | 5% |
| 5 | Miro Board | 1 | 5% |
| 6 | Notion Page | 1 | 5% |
| 7 | JSON Schema | 1 | 5% |
| 8 | Interactive Checklist | 1 | 5% |

**Total:** 20 format instances across 12 guides

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Database_Architecture_Preview/TABLE_formats.md`
**Related Files:** [TABLE_guide_formats.md](./TABLE_guide_formats.md)

**Last Updated:** 2025-11-22
