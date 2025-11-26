# PHASE 1: POSTGRES IMPORT/EXPORT PIPELINE

**Phase ID:** RSH-ARCH-PHASE-1
**Status:** Planning
**Created:** 2025-11-26
**Dependencies:** PHASE 0 (Data Source Inventory)

---

## 1. Overview

PHASE 1 establishes a robust PostgreSQL-based data infrastructure for the RESEARCHES dashboard. This includes database schema design, ETL (Extract, Transform, Load) pipeline implementation, automated import/export processes, and API integration layers.

**Key Objectives:**
- Design normalized PostgreSQL schema
- Build ETL pipeline for CSV/JSON/Markdown sources
- Create automated sync with Dropbox
- Implement export APIs for dashboard consumption
- Establish data versioning and audit trails

---

## 2. Database Architecture

### 2.1 PostgreSQL Schema Design

#### A. Core Tables

**Database:** `researches_db`
**Schema:** `public`

```sql
-- Researches Table
CREATE TABLE researches (
    id SERIAL PRIMARY KEY,
    research_id VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    department VARCHAR(10) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'planning',
    created_date TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_date TIMESTAMP DEFAULT NOW(),
    researcher_id VARCHAR(20) REFERENCES employees(employee_id),
    output_path TEXT,
    metadata JSONB,
    CONSTRAINT valid_department CHECK (department IN ('VID', 'AI', 'LGN', 'DEV', 'HR', 'DESIGN', 'SALES', 'SMM')),
    CONSTRAINT valid_status CHECK (status IN ('planning', 'active', 'review', 'completed', 'archived'))
);

-- Videos Table
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    video_id VARCHAR(20) UNIQUE NOT NULL,
    source_url TEXT NOT NULL,
    title VARCHAR(255),
    duration INTEGER CHECK (duration > 0),
    channel_id VARCHAR(20) REFERENCES channels(channel_id),
    status VARCHAR(20) NOT NULL DEFAULT 'queued',
    phase INTEGER CHECK (phase BETWEEN 1 AND 7),
    transcript_path TEXT,
    transcript_content TEXT,
    created_date TIMESTAMP NOT NULL DEFAULT NOW(),
    completed_date TIMESTAMP,
    metadata JSONB,
    CONSTRAINT valid_video_status CHECK (status IN ('queued', 'transcribing', 'analyzing', 'completed', 'failed'))
);

-- Channels Table
CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    channel_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    platform VARCHAR(50) NOT NULL DEFAULT 'YouTube',
    url TEXT,
    category VARCHAR(50),
    videos_in_queue INTEGER DEFAULT 0,
    last_scan_date TIMESTAMP,
    metadata JSONB
);

-- Influencers Table
CREATE TABLE influencers (
    id SERIAL PRIMARY KEY,
    influencer_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    subscriber_count INTEGER CHECK (subscriber_count >= 0),
    engagement_rate DECIMAL(5,2) CHECK (engagement_rate BETWEEN 0 AND 100),
    last_updated TIMESTAMP DEFAULT NOW(),
    metadata JSONB
);

-- Search Queue Table
CREATE TABLE search_queue (
    id SERIAL PRIMARY KEY,
    search_id VARCHAR(50) UNIQUE NOT NULL,
    department VARCHAR(10) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    priority INTEGER CHECK (priority BETWEEN 1 AND 5),
    created_date TIMESTAMP NOT NULL DEFAULT NOW(),
    assigned_to VARCHAR(20) REFERENCES employees(employee_id),
    query TEXT,
    results_path TEXT,
    completed_date TIMESTAMP,
    metadata JSONB,
    CONSTRAINT valid_search_status CHECK (status IN ('pending', 'active', 'completed', 'cancelled'))
);

-- Reports Table
CREATE TABLE reports (
    id SERIAL PRIMARY KEY,
    report_id VARCHAR(50) UNIQUE NOT NULL,
    research_id VARCHAR(50) REFERENCES researches(research_id),
    title VARCHAR(255) NOT NULL,
    report_type VARCHAR(50),
    file_path TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT NOW(),
    published_date TIMESTAMP,
    metadata JSONB
);
```

#### B. Relationship Tables

```sql
-- Research-Video Relationships
CREATE TABLE research_videos (
    id SERIAL PRIMARY KEY,
    research_id VARCHAR(50) REFERENCES researches(research_id) ON DELETE CASCADE,
    video_id VARCHAR(20) REFERENCES videos(video_id) ON DELETE CASCADE,
    relevance_score DECIMAL(3,2) CHECK (relevance_score BETWEEN 0 AND 1),
    created_date TIMESTAMP DEFAULT NOW(),
    UNIQUE(research_id, video_id)
);

-- Video-Influencer Relationships
CREATE TABLE video_influencers (
    id SERIAL PRIMARY KEY,
    video_id VARCHAR(20) REFERENCES videos(video_id) ON DELETE CASCADE,
    influencer_id VARCHAR(20) REFERENCES influencers(influencer_id) ON DELETE CASCADE,
    created_date TIMESTAMP DEFAULT NOW(),
    UNIQUE(video_id, influencer_id)
);

-- Analysis Results (Gap Analysis, Library Mapping, etc.)
CREATE TABLE analysis_results (
    id SERIAL PRIMARY KEY,
    analysis_id VARCHAR(50) UNIQUE NOT NULL,
    video_id VARCHAR(20) REFERENCES videos(video_id),
    analysis_type VARCHAR(50) NOT NULL,
    file_path TEXT,
    results JSONB,
    created_date TIMESTAMP DEFAULT NOW(),
    CONSTRAINT valid_analysis_type CHECK (analysis_type IN ('gap_analysis', 'library_mapping', 'extraction', 'validation', 'phase_report'))
);
```

#### C. Audit & Version Tables

```sql
-- Change Log Table
CREATE TABLE change_log (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(50) NOT NULL,
    record_id INTEGER NOT NULL,
    operation VARCHAR(10) NOT NULL,
    changed_by VARCHAR(50),
    changed_at TIMESTAMP DEFAULT NOW(),
    old_values JSONB,
    new_values JSONB,
    CONSTRAINT valid_operation CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE'))
);

-- File Sync Log
CREATE TABLE file_sync_log (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    sync_type VARCHAR(20) NOT NULL,
    sync_status VARCHAR(20) NOT NULL,
    file_hash VARCHAR(64),
    synced_at TIMESTAMP DEFAULT NOW(),
    error_message TEXT,
    CONSTRAINT valid_sync_type CHECK (sync_type IN ('import', 'export', 'update')),
    CONSTRAINT valid_sync_status CHECK (sync_status IN ('success', 'failed', 'pending'))
);
```

---

### 2.2 Indexes & Performance

```sql
-- Performance Indexes
CREATE INDEX idx_researches_department ON researches(department);
CREATE INDEX idx_researches_status ON researches(status);
CREATE INDEX idx_researches_created_date ON researches(created_date DESC);
CREATE INDEX idx_videos_status ON videos(status);
CREATE INDEX idx_videos_channel ON videos(channel_id);
CREATE INDEX idx_videos_created_date ON videos(created_date DESC);
CREATE INDEX idx_search_queue_status ON search_queue(status);
CREATE INDEX idx_search_queue_priority ON search_queue(priority DESC);

-- JSONB Indexes (for metadata queries)
CREATE INDEX idx_researches_metadata ON researches USING GIN(metadata);
CREATE INDEX idx_videos_metadata ON videos USING GIN(metadata);
CREATE INDEX idx_analysis_results ON analysis_results USING GIN(results);

-- Full-Text Search Indexes
CREATE INDEX idx_videos_transcript_fts ON videos USING GIN(to_tsvector('english', transcript_content));
CREATE INDEX idx_researches_title_fts ON researches USING GIN(to_tsvector('english', title));
```

---

## 3. ETL Pipeline Architecture

### 3.1 Pipeline Overview

```
┌─────────────────┐
│  DROPBOX FILES  │
│  - CSV          │
│  - JSON         │
│  - Markdown     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   EXTRACTOR     │
│  - File Watch   │
│  - API Fetch    │
│  - Batch Import │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  TRANSFORMER    │
│  - Validate     │
│  - Normalize    │
│  - Enrich       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     LOADER      │
│  - Postgres     │
│  - Upsert       │
│  - Audit Log    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   POSTGRES DB   │
└─────────────────┘
```

### 3.2 ETL Components

#### A. Extractor (Python)

**File:** `scripts/etl/extractor.py`

```python
"""
Data Extractor for RESEARCHES ETL Pipeline
Handles CSV, JSON, and Markdown file extraction from Dropbox
"""

import csv
import json
import os
from pathlib import Path
from typing import Dict, List, Any
import hashlib

class DataExtractor:
    def __init__(self, dropbox_root: str, config: Dict):
        self.dropbox_root = Path(dropbox_root)
        self.config = config

    def extract_csv(self, file_path: str) -> List[Dict[str, Any]]:
        """Extract data from CSV files"""
        records = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
        return records

    def extract_json(self, file_path: str) -> Dict[str, Any]:
        """Extract data from JSON files"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def extract_markdown(self, file_path: str) -> Dict[str, Any]:
        """Extract metadata and content from Markdown files"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract frontmatter if present
        metadata = self._parse_frontmatter(content)

        return {
            'file_path': str(file_path),
            'content': content,
            'metadata': metadata,
            'file_hash': self._compute_hash(content)
        }

    def _parse_frontmatter(self, content: str) -> Dict[str, Any]:
        """Parse YAML frontmatter from Markdown"""
        # Implementation for YAML parsing
        pass

    def _compute_hash(self, content: str) -> str:
        """Compute SHA-256 hash for change detection"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
```

#### B. Transformer (Python)

**File:** `scripts/etl/transformer.py`

```python
"""
Data Transformer for RESEARCHES ETL Pipeline
Validates, normalizes, and enriches extracted data
"""

from typing import Dict, Any, List
from datetime import datetime
import re

class DataTransformer:
    def __init__(self, config: Dict):
        self.config = config

    def validate_research(self, record: Dict[str, Any]) -> bool:
        """Validate research record against schema"""
        required_fields = ['research_id', 'title', 'department', 'status']

        # Check required fields
        for field in required_fields:
            if field not in record or not record[field]:
                return False

        # Validate ID format
        if not re.match(r'^RSH-[A-Z]+-\d{3}$', record['research_id']):
            return False

        # Validate department
        valid_departments = ['VID', 'AI', 'LGN', 'DEV', 'HR', 'DESIGN', 'SALES', 'SMM']
        if record['department'] not in valid_departments:
            return False

        return True

    def normalize_dates(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize date formats to ISO 8601"""
        date_fields = ['created_date', 'updated_date', 'completed_date']

        for field in date_fields:
            if field in record and record[field]:
                record[field] = self._parse_date(record[field])

        return record

    def enrich_metadata(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Add computed fields and enrichments"""
        # Add processing timestamp
        record['processed_at'] = datetime.utcnow().isoformat()

        # Extract department from research_id if missing
        if 'research_id' in record and 'department' not in record:
            match = re.search(r'RSH-([A-Z]+)-', record['research_id'])
            if match:
                record['department'] = match.group(1)

        return record

    def _parse_date(self, date_str: str) -> str:
        """Parse various date formats to ISO 8601"""
        # Implementation for date parsing
        pass
```

#### C. Loader (Python)

**File:** `scripts/etl/loader.py`

```python
"""
Data Loader for RESEARCHES ETL Pipeline
Loads transformed data into PostgreSQL with upsert logic
"""

import psycopg2
from psycopg2.extras import execute_values
from typing import Dict, Any, List

class DataLoader:
    def __init__(self, db_config: Dict):
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()

    def upsert_researches(self, records: List[Dict[str, Any]]) -> int:
        """Insert or update research records"""
        query = """
            INSERT INTO researches (research_id, title, department, status,
                                   created_date, updated_date, researcher_id,
                                   output_path, metadata)
            VALUES %s
            ON CONFLICT (research_id)
            DO UPDATE SET
                title = EXCLUDED.title,
                department = EXCLUDED.department,
                status = EXCLUDED.status,
                updated_date = EXCLUDED.updated_date,
                researcher_id = EXCLUDED.researcher_id,
                output_path = EXCLUDED.output_path,
                metadata = EXCLUDED.metadata
        """

        values = [
            (r['research_id'], r['title'], r['department'], r['status'],
             r.get('created_date'), r.get('updated_date'), r.get('researcher_id'),
             r.get('output_path'), r.get('metadata'))
            for r in records
        ]

        execute_values(self.cursor, query, values)
        self.conn.commit()
        return len(records)

    def upsert_videos(self, records: List[Dict[str, Any]]) -> int:
        """Insert or update video records"""
        # Similar implementation for videos
        pass

    def log_sync(self, file_path: str, sync_type: str, status: str, error: str = None):
        """Log file sync operation"""
        query = """
            INSERT INTO file_sync_log (file_path, sync_type, sync_status, error_message)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (file_path, sync_type, status, error))
        self.conn.commit()
```

---

### 3.3 ETL Orchestration

**File:** `scripts/etl/pipeline.py`

```python
"""
ETL Pipeline Orchestrator
Coordinates extraction, transformation, and loading
"""

from extractor import DataExtractor
from transformer import DataTransformer
from loader import DataLoader
import logging

class ETLPipeline:
    def __init__(self, config: Dict):
        self.config = config
        self.extractor = DataExtractor(config['dropbox_root'], config)
        self.transformer = DataTransformer(config)
        self.loader = DataLoader(config['database'])
        self.logger = logging.getLogger(__name__)

    def run_full_import(self):
        """Run full import of all data sources"""
        self.logger.info("Starting full ETL import")

        # Import CSVs
        self._import_csv_sources()

        # Import JSONs
        self._import_json_sources()

        # Import Markdown files
        self._import_markdown_sources()

        self.logger.info("Full ETL import completed")

    def run_incremental_sync(self):
        """Run incremental sync for changed files"""
        self.logger.info("Starting incremental sync")

        # Detect changed files
        changed_files = self._detect_changes()

        # Process only changed files
        for file_path in changed_files:
            self._process_file(file_path)

        self.logger.info(f"Incremental sync completed: {len(changed_files)} files processed")

    def _import_csv_sources(self):
        """Import all CSV data sources"""
        csv_sources = [
            ('DATA/00_SEARCH_QUEUE/Search_Queue_Master.csv', 'search_queue'),
            ('DATA/01_VIDEO_QUEUE/Video_Queue_Master.csv', 'videos'),
            ('DATA/RESEARCHES_Master_List.csv', 'researches')
        ]

        for file_path, table_name in csv_sources:
            try:
                records = self.extractor.extract_csv(file_path)
                transformed = [self.transformer.normalize_dates(r) for r in records]

                if table_name == 'researches':
                    self.loader.upsert_researches(transformed)
                elif table_name == 'videos':
                    self.loader.upsert_videos(transformed)

                self.loader.log_sync(file_path, 'import', 'success')
            except Exception as e:
                self.logger.error(f"Error importing {file_path}: {e}")
                self.loader.log_sync(file_path, 'import', 'failed', str(e))
```

---

## 4. Data Import Scripts

### 4.1 CSV Import Configuration

**File:** `config/import_config.yaml`

```yaml
database:
  host: localhost
  port: 5432
  database: researches_db
  user: researches_user
  password: ${DB_PASSWORD}

dropbox:
  root: "C:/Users/Dell/Dropbox/ENTITIES/TASK_MANAGERS/RESEARCHES/"
  api_key: ${DROPBOX_API_KEY}
  sync_interval: 300  # seconds

csv_sources:
  - path: "DATA/00_SEARCH_QUEUE/Search_Queue_Master.csv"
    table: search_queue
    id_column: search_id
    encoding: utf-8

  - path: "DATA/01_VIDEO_QUEUE/Video_Queue_Master.csv"
    table: videos
    id_column: video_id
    encoding: utf-8

  - path: "DATA/RESEARCHES_Master_List.csv"
    table: researches
    id_column: research_id
    encoding: utf-8

json_sources:
  - path: "DATA/ARCHIVE/04_INFLUENCER_DATA/Influencer_Database.json"
    table: influencers
    id_path: "$.influencers[*].id"

  - path: "DATA/ARCHIVE/04_INFLUENCER_DATA/YouTube_Channels.json"
    table: channels
    id_path: "$.channels[*].channel_id"

markdown_sources:
  - path: "02_TRANSCRIPTIONS/"
    pattern: "Video_*.md"
    table: videos
    content_field: transcript_content

  - path: "03_ANALYSIS/Library_Mapping/"
    pattern: "Video_*_Library_Mapping_Report.md"
    table: analysis_results
    analysis_type: library_mapping
```

---

### 4.2 Batch Import Scripts

**File:** `scripts/import/batch_import.sh`

```bash
#!/bin/bash
# Batch Import Script for RESEARCHES Database

set -e

echo "=== RESEARCHES Database Import ==="
echo "Started: $(date)"

# Set environment
export DB_HOST=${DB_HOST:-localhost}
export DB_NAME=${DB_NAME:-researches_db}

# Run imports in order of dependencies
echo "1. Importing channels..."
python scripts/import/import_channels.py

echo "2. Importing influencers..."
python scripts/import/import_influencers.py

echo "3. Importing videos..."
python scripts/import/import_videos.py

echo "4. Importing researches..."
python scripts/import/import_researches.py

echo "5. Importing search queue..."
python scripts/import/import_search_queue.py

echo "6. Importing analysis results..."
python scripts/import/import_analysis.py

echo "7. Building relationships..."
python scripts/import/build_relationships.py

echo "Completed: $(date)"
echo "=== Import Summary ==="
psql -h $DB_HOST -d $DB_NAME -c "
SELECT
    'researches' as table, COUNT(*) as records FROM researches
UNION ALL
SELECT 'videos', COUNT(*) FROM videos
UNION ALL
SELECT 'channels', COUNT(*) FROM channels
UNION ALL
SELECT 'influencers', COUNT(*) FROM influencers
UNION ALL
SELECT 'search_queue', COUNT(*) FROM search_queue
UNION ALL
SELECT 'analysis_results', COUNT(*) FROM analysis_results;
"
```

---

## 5. Export APIs

### 5.1 REST API Design

**Base URL:** `http://localhost:8000/api/v1`

#### A. Research Endpoints

```
GET    /researches                 # List all researches (paginated)
GET    /researches/{id}             # Get research by ID
POST   /researches                  # Create new research
PUT    /researches/{id}             # Update research
DELETE /researches/{id}             # Delete research
GET    /researches/{id}/videos      # Get related videos
GET    /researches/department/{dept} # Filter by department
```

#### B. Video Endpoints

```
GET    /videos                      # List all videos (paginated)
GET    /videos/{id}                 # Get video by ID
GET    /videos/{id}/transcript      # Get transcript content
GET    /videos/{id}/analysis        # Get analysis results
GET    /videos/status/{status}      # Filter by status
GET    /videos/channel/{channel_id} # Filter by channel
```

#### C. Dashboard Endpoints

```
GET    /dashboard/stats             # Overview statistics
GET    /dashboard/recent            # Recent activity
GET    /dashboard/queue             # Current queue status
GET    /dashboard/analytics         # Analytics data
```

### 5.2 API Implementation (FastAPI)

**File:** `api/main.py`

```python
"""
FastAPI Application for RESEARCHES Dashboard
"""

from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import psycopg2
from pydantic import BaseModel

app = FastAPI(title="RESEARCHES API", version="1.0.0")

# Pydantic Models
class Research(BaseModel):
    research_id: str
    title: str
    department: str
    status: str
    created_date: str
    researcher_id: Optional[str]
    output_path: Optional[str]

class Video(BaseModel):
    video_id: str
    source_url: str
    title: Optional[str]
    status: str
    phase: Optional[int]
    transcript_path: Optional[str]

# Database connection
def get_db():
    return psycopg2.connect(
        host="localhost",
        database="researches_db",
        user="researches_user",
        password="password"
    )

# Research Endpoints
@app.get("/api/v1/researches", response_model=List[Research])
async def list_researches(
    department: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = Query(50, le=100),
    offset: int = 0
):
    """List researches with optional filters"""
    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM researches WHERE 1=1"
    params = []

    if department:
        query += " AND department = %s"
        params.append(department)

    if status:
        query += " AND status = %s"
        params.append(status)

    query += " ORDER BY created_date DESC LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results

@app.get("/api/v1/dashboard/stats")
async def get_dashboard_stats():
    """Get overview statistics for dashboard"""
    conn = get_db()
    cursor = conn.cursor()

    stats = {}

    # Total researches by status
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM researches
        GROUP BY status
    """)
    stats['researches_by_status'] = dict(cursor.fetchall())

    # Total videos by status
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM videos
        GROUP BY status
    """)
    stats['videos_by_status'] = dict(cursor.fetchall())

    # Recent activity
    cursor.execute("""
        SELECT COUNT(*)
        FROM researches
        WHERE created_date > NOW() - INTERVAL '7 days'
    """)
    stats['researches_last_7_days'] = cursor.fetchone()[0]

    conn.close()
    return stats
```

---

### 5.3 Export Scripts for CSV/JSON

**File:** `scripts/export/export_dashboard_data.py`

```python
"""
Export data from Postgres to CSV/JSON for dashboard consumption
"""

import psycopg2
import csv
import json
from datetime import datetime

class DashboardExporter:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)

    def export_to_csv(self, query: str, output_path: str):
        """Export query results to CSV"""
        cursor = self.conn.cursor()
        cursor.execute(query)

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([desc[0] for desc in cursor.description])
            writer.writerows(cursor.fetchall())

    def export_to_json(self, query: str, output_path: str):
        """Export query results to JSON"""
        cursor = self.conn.cursor()
        cursor.execute(query)

        columns = [desc[0] for desc in cursor.description]
        results = []

        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=str)

    def export_dashboard_datasets(self, output_dir: str):
        """Export all dashboard datasets"""

        # Export researches overview
        self.export_to_json(
            "SELECT * FROM researches ORDER BY created_date DESC LIMIT 100",
            f"{output_dir}/researches_latest.json"
        )

        # Export video queue
        self.export_to_csv(
            "SELECT * FROM videos WHERE status != 'completed' ORDER BY created_date",
            f"{output_dir}/video_queue.csv"
        )

        # Export statistics
        stats_query = """
            SELECT
                department,
                COUNT(*) as total_researches,
                SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as active,
                SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed
            FROM researches
            GROUP BY department
        """
        self.export_to_json(stats_query, f"{output_dir}/stats_by_department.json")
```

---

## 6. Integration with Dropbox

### 6.1 Dropbox API Setup

**File:** `scripts/dropbox/dropbox_sync.py`

```python
"""
Dropbox Integration for RESEARCHES
Bidirectional sync between local DB and Dropbox files
"""

import dropbox
from dropbox.files import WriteMode
import os

class DropboxSync:
    def __init__(self, access_token: str):
        self.dbx = dropbox.Dropbox(access_token)
        self.base_path = "/ENTITIES/TASK_MANAGERS/RESEARCHES"

    def download_file(self, dropbox_path: str, local_path: str):
        """Download file from Dropbox"""
        metadata, response = self.dbx.files_download(dropbox_path)

        with open(local_path, 'wb') as f:
            f.write(response.content)

        return metadata

    def upload_file(self, local_path: str, dropbox_path: str):
        """Upload file to Dropbox"""
        with open(local_path, 'rb') as f:
            self.dbx.files_upload(
                f.read(),
                dropbox_path,
                mode=WriteMode.overwrite
            )

    def sync_folder(self, folder_path: str):
        """Sync entire folder from Dropbox"""
        result = self.dbx.files_list_folder(f"{self.base_path}/{folder_path}")

        for entry in result.entries:
            if isinstance(entry, dropbox.files.FileMetadata):
                self.download_file(entry.path_display, f"./local/{entry.name}")
```

---

## 7. Deployment & Operations

### 7.1 Database Setup Script

**File:** `scripts/setup/init_database.sh`

```bash
#!/bin/bash
# Initialize RESEARCHES PostgreSQL Database

# Create database
psql -U postgres -c "CREATE DATABASE researches_db;"

# Create user
psql -U postgres -c "CREATE USER researches_user WITH PASSWORD 'secure_password';"

# Grant privileges
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE researches_db TO researches_user;"

# Run schema migrations
psql -U researches_user -d researches_db -f migrations/001_create_tables.sql
psql -U researches_user -d researches_db -f migrations/002_create_indexes.sql
psql -U researches_user -d researches_db -f migrations/003_create_triggers.sql

echo "Database initialized successfully"
```

### 7.2 Scheduled Jobs (Cron)

**File:** `config/crontab`

```bash
# RESEARCHES ETL Scheduled Jobs

# Incremental sync every 5 minutes
*/5 * * * * cd /app && python scripts/etl/pipeline.py --mode incremental

# Full sync daily at 2 AM
0 2 * * * cd /app && python scripts/etl/pipeline.py --mode full

# Export dashboard data hourly
0 * * * * cd /app && python scripts/export/export_dashboard_data.py

# Cleanup old logs weekly
0 3 * * 0 cd /app && python scripts/maintenance/cleanup_logs.py
```

---

## 8. Testing Strategy

### 8.1 Test Coverage

| Component | Test Type | Coverage Target |
|-----------|-----------|-----------------|
| ETL Pipeline | Unit + Integration | 80%+ |
| Database Schema | Schema validation | 100% |
| API Endpoints | Integration | 90%+ |
| Dropbox Sync | Integration | 70%+ |
| Data Validation | Unit | 95%+ |

### 8.2 Test Scenarios

**File:** `tests/test_etl_pipeline.py`

```python
import pytest
from scripts.etl.pipeline import ETLPipeline

def test_csv_import():
    """Test CSV import functionality"""
    pipeline = ETLPipeline(test_config)
    records = pipeline.extractor.extract_csv('test_data/sample.csv')

    assert len(records) > 0
    assert 'research_id' in records[0]

def test_data_validation():
    """Test data validation rules"""
    transformer = DataTransformer(test_config)

    valid_record = {
        'research_id': 'RSH-VID-001',
        'title': 'Test Research',
        'department': 'VID',
        'status': 'active'
    }

    assert transformer.validate_research(valid_record) == True

def test_upsert_logic():
    """Test upsert prevents duplicates"""
    loader = DataLoader(test_db_config)

    record = {'research_id': 'RSH-VID-TEST', 'title': 'Test'}
    loader.upsert_researches([record])

    # Insert again - should update, not create duplicate
    record['title'] = 'Updated Test'
    loader.upsert_researches([record])

    # Verify only one record exists
    count = loader.cursor.execute("SELECT COUNT(*) FROM researches WHERE research_id = 'RSH-VID-TEST'")
    assert count == 1
```

---

## 9. Performance Benchmarks

### 9.1 Target Metrics

| Operation | Target | Measurement |
|-----------|--------|-------------|
| CSV import (1000 rows) | < 5 seconds | Execution time |
| API response (list 50 items) | < 200ms | Response time |
| Full text search | < 500ms | Query time |
| Incremental sync | < 10 seconds | Sync cycle |
| Export to JSON (1000 records) | < 3 seconds | File write time |

### 9.2 Optimization Strategies

- Use bulk inserts with `execute_values()`
- Implement connection pooling
- Add appropriate indexes for common queries
- Use JSONB for flexible metadata storage
- Implement query result caching
- Batch file operations

---

## 10. Monitoring & Logging

### 10.1 Log Structure

**File:** `logs/etl_pipeline.log`

```
[2025-11-26 10:30:00] INFO - Starting incremental sync
[2025-11-26 10:30:01] INFO - Detected 5 changed files
[2025-11-26 10:30:01] INFO - Processing: DATA/Video_Queue_Master.csv
[2025-11-26 10:30:02] INFO - Imported 45 video records
[2025-11-26 10:30:02] SUCCESS - Incremental sync completed in 2.3s
```

### 10.2 Monitoring Dashboard

**Metrics to Track:**
- Import success rate
- Failed sync attempts
- Database query performance
- API response times
- Storage usage
- Record counts by table

---

## 11. Success Criteria

### 11.1 Phase Completion Checklist

- [ ] PostgreSQL database schema created and tested
- [ ] ETL pipeline scripts implemented and tested
- [ ] CSV/JSON import working for all sources
- [ ] Markdown file parsing implemented
- [ ] Export APIs functional
- [ ] Dropbox sync configured
- [ ] Scheduled jobs set up
- [ ] Test coverage > 80%
- [ ] Performance benchmarks met
- [ ] Documentation complete

---

## 12. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Data corruption during import | CRITICAL | LOW | Transactions + backups + validation |
| API performance degradation | HIGH | MEDIUM | Caching + pagination + indexes |
| Dropbox API rate limits | MEDIUM | MEDIUM | Implement exponential backoff |
| Schema migration conflicts | HIGH | LOW | Version control + rollback scripts |
| Concurrent write conflicts | MEDIUM | HIGH | Use database locks + conflict resolution |

---

## 13. Next Steps → PHASE 2

**Prerequisites for Phase 2:**
1. Complete database implementation
2. Validate ETL pipeline with production data
3. Performance test with realistic data volumes
4. Set up monitoring infrastructure

**Phase 2 Focus:**
- Graph database for relationship mapping
- Vector database for semantic search
- Transcript embeddings for similarity search
- Advanced query capabilities

---

**Document Status:** Draft
**Last Updated:** 2025-11-26
**Next Review:** After Phase 1 implementation
**Owner:** RESEARCHES Development Team
