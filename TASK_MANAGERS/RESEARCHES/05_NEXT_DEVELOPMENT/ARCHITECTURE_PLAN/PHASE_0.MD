# PHASE 0: DROPBOX/CSV SOURCES & DATA FOUNDATIONS

**Phase ID:** RSH-ARCH-PHASE-0
**Status:** Planning
**Created:** 2025-11-26
**Dependencies:** None (Foundation Phase)

---

## 1. Overview

PHASE 0 establishes the foundation for the RESEARCHES dashboard by cataloging all current data sources, defining ID/token rules, and creating a comprehensive data source inventory. This phase focuses on understanding what data exists, where it lives, and how it's currently structured.

---

## 2. Current Data Source Inventory

### 2.1 Dropbox Structure

**Root Path:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\`

| Directory | Content Type | File Count | Data Format | Sync Status |
|-----------|-------------|------------|-------------|-------------|
| `00_SEARCH_QUEUE/` | Search management | ~10 | MD, CSV | Active |
| `01_VIDEO_QUEUE/` | Video pipeline | ~15 | MD, CSV, PY | Active |
| `02_TRANSCRIPTIONS/` | Video transcripts | ~50+ | MD | Active |
| `03_ANALYSIS/` | Analysis outputs | ~40+ | MD | Active |
| `04_INTEGRATION/` | Integration data | TBD | MD, JSON | Active |
| `ARCHIVE/` | Historical data | 100+ | MD, JSON, CSV | Archive |
| `DATA/` | Structured data | ~10 | JSON, CSV | Active |
| `PROMPTS/` | Research prompts | ~30 | MD | Active |
| `REPORTS/` | Final reports | ~20 | MD | Active |
| `TAXONOMY/` | Classification | ~5 | MD | Active |

**Total Estimated Files:** 300+
**Total Estimated Size:** TBD (needs audit)

---

### 2.2 CSV Data Sources

#### A. Queue Management CSVs

**File:** `DATA/00_SEARCH_QUEUE/Search_Queue_Master.csv`

| Column | Type | Description | Sample Values | Required |
|--------|------|-------------|--------------|----------|
| search_id | STRING | Unique search identifier | RSH-SRH-001 | YES |
| status | ENUM | Queue status | pending, active, completed | YES |
| department | STRING | Target department | AI, HR, Design, Dev | YES |
| created_date | DATE | Creation timestamp | 2025-11-26 | YES |
| priority | INTEGER | Priority level (1-5) | 1, 2, 3, 4, 5 | NO |
| assigned_to | STRING | Researcher ID | EMP-001 | NO |

**File:** `DATA/01_VIDEO_QUEUE/Video_Queue_Master.csv`

| Column | Type | Description | Sample Values | Required |
|--------|------|-------------|--------------|----------|
| video_id | STRING | Video identifier | Video_001 | YES |
| status | ENUM | Processing status | queued, transcribing, analyzing, completed | YES |
| source_url | URL | YouTube/source URL | https://youtube.com/watch?v=... | YES |
| duration | INTEGER | Video length (seconds) | 1200 | NO |
| transcript_path | PATH | Transcript file location | 02_TRANSCRIPTIONS/Video_001.md | NO |
| phase | INTEGER | Processing phase (1-7) | 1, 2, 3, 4, 5, 6, 7 | NO |

#### B. Research Master List

**File:** `DATA/RESEARCHES_Master_List.csv`

| Column | Type | Description | Sample Values | Required |
|--------|------|-------------|--------------|----------|
| research_id | STRING | Research identifier | RSH-VID-001 | YES |
| title | STRING | Research title | Video Tool Comparison | YES |
| department | STRING | Department code | VID, AI, HR, DEV | YES |
| status | ENUM | Research status | planning, active, completed, archived | YES |
| created_date | DATE | Creation date | 2025-11-26 | YES |
| researcher | STRING | Employee ID | EMP-001 | NO |
| output_path | PATH | Final report location | REPORTS/RSH-VID-001_Report.md | NO |
| related_videos | ARRAY | Related video IDs | [Video_001, Video_002] | NO |

---

### 2.3 JSON Data Sources

#### A. Influencer Database

**File:** `DATA/ARCHIVE/04_INFLUENCER_DATA/Influencer_Database.json`

```json
{
  "influencers": [
    {
      "id": "INF-001",
      "name": "Channel Name",
      "platform": "YouTube",
      "category": "AI Tools",
      "subscriber_count": 150000,
      "engagement_rate": 4.5,
      "last_updated": "2025-11-26",
      "videos_tracked": ["Video_001", "Video_005"]
    }
  ]
}
```

**Schema Fields:**

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| id | STRING | Influencer ID | YES |
| name | STRING | Channel/Creator name | YES |
| platform | ENUM | Social platform | YES |
| category | STRING | Content category | NO |
| subscriber_count | INTEGER | Follower count | NO |
| engagement_rate | FLOAT | Engagement % | NO |
| videos_tracked | ARRAY | Related video IDs | NO |

#### B. YouTube Channels Database

**File:** `DATA/ARCHIVE/04_INFLUENCER_DATA/YouTube_Channels.json`

```json
{
  "channels": [
    {
      "channel_id": "YT-CH-001",
      "name": "AI Tools Daily",
      "url": "https://youtube.com/@aitoolsdaily",
      "category": "AI",
      "videos_in_queue": 5,
      "last_scan_date": "2025-11-26"
    }
  ]
}
```

---

### 2.4 Markdown Report Sources

| Directory | Report Type | Count | ID Pattern | Example |
|-----------|-------------|-------|------------|---------|
| `02_TRANSCRIPTIONS/` | Transcripts | 50+ | Video_### | Video_001.md |
| `03_ANALYSIS/Library_Mapping/` | Tool mappings | 15+ | Video_###_Library_Mapping_Report | Video_001_Library_Mapping_Report.md |
| `03_ANALYSIS/Gap_Analysis/` | Gap analyses | 10+ | Video_###_Gap_Analysis | Video_002_Gap_Analysis.md |
| `03_ANALYSIS/Extractions/` | Data extractions | 20+ | Video_###_Extraction_Inventory | Video_002_Extraction_Inventory.md |
| `REPORTS/` | Final reports | 20+ | RSH-{DEPT}-###_Report | RSH-VID-001_Report.md |

---

## 3. ID & Token Rules System

### 3.1 Entity ID Patterns

| Entity Type | Pattern | Format | Example | Description |
|-------------|---------|--------|---------|-------------|
| Research | RSH-{DEPT}-### | Text-Numeric | RSH-VID-001 | Main research identifier |
| Video | Video_### | Text-Numeric | Video_001 | Video processing identifier |
| Search | RSH-SRH-### | Text-Numeric | RSH-SRH-001 | Search queue identifier |
| Influencer | INF-### | Text-Numeric | INF-001 | Influencer tracking ID |
| Channel | YT-CH-### | Text-Numeric | YT-CH-001 | YouTube channel ID |
| Report | RPT-{DEPT}-### | Text-Numeric | RPT-VID-001 | Final report ID |
| Prompt | PMT-### | Text-Numeric | PMT-044 | Prompt identifier |

### 3.2 Department Codes

| Code | Department | Use Case |
|------|------------|----------|
| VID | Video | Video research, SMM, influencer tracking |
| AI | Artificial Intelligence | AI/ML tools, automation research |
| LGN | Learning & Growth | Educational content, knowledge synthesis |
| DEV | Development | Tooling, architecture, technical research |
| HR | Human Resources | HR automation, management research |
| DESIGN | Design | Design tools, workflows |
| SALES | Sales | Sales tools, CRM, strategies |
| SMM | Social Media | SMM tools, content strategies |

### 3.3 Status Values

**Research Status:**
- `planning` - Research scope being defined
- `active` - Research in progress
- `review` - Awaiting review
- `completed` - Research finished
- `archived` - Moved to archive

**Video Processing Status:**
- `queued` - In video queue
- `transcribing` - Transcription in progress
- `analyzing` - Analysis phase
- `completed` - Processing complete
- `failed` - Processing error

**Search Status:**
- `pending` - Not started
- `active` - Search running
- `completed` - Results delivered
- `cancelled` - Search cancelled

### 3.4 File Naming Conventions

**Research Files:**
```
RSH-{DEPT}-###_{Title}.md
Example: RSH-VID-001_Video_Tool_Comparison.md
```

**Reports:**
```
RSH-{DEPT}-###_Report_{Description}.md
Example: RSH-VID-002_Report_Gap_Analysis_Transcription_Tools.md
```

**Data Files:**
```
RSH-{DEPT}-###_Data_{Type}_YYYY-MM-DD.{ext}
Example: RSH-VID-003_Data_Influencer_Metrics_2025-11-26.csv
```

**Video Files:**
```
Video_###.md (Transcripts)
Video_###_{ProcessType}.md (Analysis)
Example: Video_001_Library_Mapping_Report.md
```

---

## 4. Data Quality Assessment

### 4.1 Current State Issues

| Issue | Severity | Impact | Count | Example |
|-------|----------|--------|-------|---------|
| Inconsistent ID formats | HIGH | Query complexity | ~30 | Mix of Video_001 vs RSH-VID-001 |
| Missing metadata | MEDIUM | Searchability | ~50 | Files without department tags |
| Duplicate files | LOW | Storage waste | ~10 | Conflict copies |
| Orphaned references | MEDIUM | Broken links | ~15 | References to archived files |
| No date standardization | MEDIUM | Sorting issues | ALL | Mix of formats |

### 4.2 Data Completeness

| Data Type | Complete | Partial | Missing | Notes |
|-----------|----------|---------|---------|-------|
| Video transcripts | 45 | 5 | 0 | All videos transcribed |
| Library mappings | 15 | 10 | 25 | Phase 7 incomplete |
| Gap analyses | 10 | 5 | 35 | Phase 5 ongoing |
| Influencer data | 20 | 30 | 0 | JSON needs updates |
| Search queue | 40 | 10 | 0 | Recent additions pending |

---

## 5. Data Source Tables (Database Preview)

### 5.1 Core Tables Design

#### Table: `researches`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment ID |
| research_id | VARCHAR(50) | UNIQUE, NOT NULL | RSH-{DEPT}-### |
| title | VARCHAR(255) | NOT NULL | Research title |
| department | VARCHAR(10) | NOT NULL | Department code |
| status | VARCHAR(20) | NOT NULL | Current status |
| created_date | TIMESTAMP | NOT NULL | Creation timestamp |
| updated_date | TIMESTAMP | NULL | Last update |
| researcher_id | VARCHAR(20) | NULL, FK | Employee reference |
| output_path | TEXT | NULL | Report file path |
| metadata | JSONB | NULL | Additional data |

#### Table: `videos`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment ID |
| video_id | VARCHAR(20) | UNIQUE, NOT NULL | Video_### |
| source_url | TEXT | NOT NULL | YouTube/source URL |
| title | VARCHAR(255) | NULL | Video title |
| duration | INTEGER | NULL | Duration in seconds |
| channel_id | VARCHAR(20) | NULL, FK | Channel reference |
| status | VARCHAR(20) | NOT NULL | Processing status |
| phase | INTEGER | NULL | Current phase (1-7) |
| transcript_path | TEXT | NULL | Transcript location |
| created_date | TIMESTAMP | NOT NULL | Queue entry date |
| completed_date | TIMESTAMP | NULL | Completion date |

#### Table: `influencers`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment ID |
| influencer_id | VARCHAR(20) | UNIQUE, NOT NULL | INF-### |
| name | VARCHAR(255) | NOT NULL | Channel/Creator name |
| platform | VARCHAR(50) | NOT NULL | Social platform |
| category | VARCHAR(50) | NULL | Content category |
| subscriber_count | INTEGER | NULL | Follower count |
| engagement_rate | DECIMAL(5,2) | NULL | Engagement % |
| last_updated | TIMESTAMP | NULL | Last data refresh |

#### Table: `search_queue`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment ID |
| search_id | VARCHAR(50) | UNIQUE, NOT NULL | RSH-SRH-### |
| department | VARCHAR(10) | NOT NULL | Target department |
| status | VARCHAR(20) | NOT NULL | Queue status |
| priority | INTEGER | NULL | Priority (1-5) |
| created_date | TIMESTAMP | NOT NULL | Creation time |
| assigned_to | VARCHAR(20) | NULL, FK | Researcher ID |
| query | TEXT | NULL | Search query |
| results_path | TEXT | NULL | Results location |

#### Table: `reports`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | SERIAL | PRIMARY KEY | Auto-increment ID |
| report_id | VARCHAR(50) | UNIQUE, NOT NULL | RPT-{DEPT}-### |
| research_id | VARCHAR(50) | NULL, FK | Related research |
| title | VARCHAR(255) | NOT NULL | Report title |
| report_type | VARCHAR(50) | NULL | Gap Analysis, Library Mapping, etc. |
| file_path | TEXT | NOT NULL | Report file location |
| created_date | TIMESTAMP | NOT NULL | Creation date |
| published_date | TIMESTAMP | NULL | Publication date |

---

## 6. Integration Requirements

### 6.1 Dropbox Sync Strategy

| Requirement | Priority | Implementation | Notes |
|-------------|----------|----------------|-------|
| Bidirectional sync | HIGH | Dropbox API | Keep local/cloud in sync |
| Conflict resolution | HIGH | Last-write-wins + versioning | Handle concurrent edits |
| Selective sync | MEDIUM | Path-based filters | Skip ARCHIVE by default |
| Change detection | HIGH | File system events | Real-time updates |
| Batch operations | MEDIUM | Scheduled jobs | Periodic full sync |

### 6.2 CSV Import Rules

| Rule | Description | Validation |
|------|-------------|------------|
| Header validation | Verify column names | Compare against schema |
| Type checking | Enforce data types | Parse and validate |
| Required fields | Check for NULL values | Reject incomplete rows |
| ID uniqueness | Prevent duplicates | Check against existing records |
| Date parsing | Standardize date formats | Convert to ISO 8601 |
| Encoding | Handle UTF-8 | Validate character encoding |

### 6.3 JSON Schema Validation

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Influencer",
  "type": "object",
  "required": ["id", "name", "platform"],
  "properties": {
    "id": {"type": "string", "pattern": "^INF-[0-9]{3}$"},
    "name": {"type": "string", "minLength": 1},
    "platform": {"type": "string", "enum": ["YouTube", "Instagram", "TikTok"]},
    "category": {"type": "string"},
    "subscriber_count": {"type": "integer", "minimum": 0},
    "engagement_rate": {"type": "number", "minimum": 0, "maximum": 100}
  }
}
```

---

## 7. Data Migration Checklist

### 7.1 Pre-Migration Tasks

- [ ] Audit all CSV files for completeness
- [ ] Validate JSON schema compliance
- [ ] Identify and resolve duplicate IDs
- [ ] Standardize date formats across all files
- [ ] Document all data dependencies
- [ ] Create backup of Dropbox folder
- [ ] Test Dropbox API connectivity
- [ ] Define rollback procedures

### 7.2 Migration Priorities

| Priority | Data Source | Reason | Est. Records |
|----------|-------------|--------|--------------|
| P0 | Video_Queue_Master.csv | Active pipeline dependency | ~50 |
| P0 | Search_Queue_Master.csv | Active searches | ~20 |
| P1 | RESEARCHES_Master_List.csv | Core research tracking | ~100 |
| P1 | Video transcripts (02_TRANSCRIPTIONS/) | High value content | ~50 |
| P2 | Influencer_Database.json | SMM insights | ~30 |
| P2 | Analysis reports (03_ANALYSIS/) | Reference data | ~40 |
| P3 | Archive data (ARCHIVE/) | Historical reference | ~200 |

---

## 8. Success Criteria

### 8.1 Data Quality Metrics

| Metric | Target | Current | Gap |
|--------|--------|---------|-----|
| ID format compliance | 100% | ~70% | 30% |
| Required field completeness | 100% | ~85% | 15% |
| Duplicate records | 0% | ~5% | 5% |
| Broken file references | 0% | ~10% | 10% |
| Date format standardization | 100% | ~60% | 40% |

### 8.2 Phase Completion Criteria

- [ ] All data sources cataloged and documented
- [ ] ID/token rules defined and documented
- [ ] CSV schemas validated
- [ ] JSON schemas created and tested
- [ ] Database table designs reviewed
- [ ] Data quality issues identified
- [ ] Migration priorities established
- [ ] Integration requirements documented

---

## 9. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Dropbox sync conflicts | HIGH | MEDIUM | Implement versioning + conflict UI |
| Data loss during migration | CRITICAL | LOW | Full backup + staged rollout |
| ID collision after migration | HIGH | MEDIUM | Pre-migration ID audit |
| CSV encoding issues | MEDIUM | HIGH | UTF-8 validation in import |
| JSON schema violations | MEDIUM | MEDIUM | Pre-import validation |
| Performance issues with large files | MEDIUM | LOW | Batch processing + pagination |

---

## 10. Next Steps → PHASE 1

**Prerequisites for Phase 1:**
1. Complete data source audit
2. Finalize table schemas
3. Set up Dropbox API credentials
4. Create test database instance
5. Define import/export API contracts

**Phase 1 Focus:**
- Postgres database setup
- ETL pipeline implementation
- CSV/JSON import automation
- Export functionality for dashboards

---

**Document Status:** Draft
**Last Updated:** 2025-11-26
**Next Review:** Before Phase 1 kickoff
**Owner:** RESEARCHES Team
