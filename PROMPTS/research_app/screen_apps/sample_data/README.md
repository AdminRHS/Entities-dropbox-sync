# Sample Data Library

This directory contains sample data files for testing import/export features in the Research Management System.

---

## 📁 File Inventory

### Import Templates

#### 1. **video_import_template.csv** (10 rows)
CSV template for bulk video import with sample data.

**Columns:**
- `video_url` - YouTube video URL (required)
- `video_title` - Video title (required, min 3 chars)
- `channel_name` - YouTube channel name (optional)
- `duration_minutes` - Video duration (optional, 1-999)
- `priority` - Priority level: low, medium, high (default: medium)
- `department` - Department code: DEV, SMM, VID, AID, DGN, MKT (required)
- `assigned_to` - Email address of assignee (optional)
- `notes` - Additional notes (optional)

**Use Case:** Bulk import videos into the video queue table
**Screen:** 11_bulk_video_import (if created)
**Test:** Upload via drag & drop or file picker

---

#### 2. **video_import_sample.json** (5 records)
JSON template for bulk video import with structured sample data.

**Structure:**
```json
[
  {
    "video_url": "string (URL)",
    "video_title": "string",
    "channel_name": "string",
    "duration_minutes": number,
    "priority": "low|medium|high",
    "department": "DEV|SMM|VID|AID|DGN|MKT",
    "assigned_to": "string (email)",
    "notes": "string"
  }
]
```

**Use Case:** Programmatic import or API testing
**Screen:** 11_bulk_video_import (if created)
**Test:** JSON parsing and validation

---

### Transcription Files

#### 3. **sample_transcription.txt** (Plain Text Format)
Full video transcription with timestamps in plain text format.

**Format:**
- Timestamp headers: `00:00:00 - Section Title`
- Content paragraphs below each timestamp
- Total duration: 15 minutes

**Use Case:** Upload transcription for Phase 1 processing
**Screen:** 05_upload_transcription_screen
**Size:** ~3.8 KB
**Test:** Drag & drop, file validation, preview display

---

#### 4. **sample_transcription.srt** (SubRip Format)
Transcription in SubRip subtitle format (.srt).

**Format:**
```
1
00:00:00,000 --> 00:00:15,000
Subtitle text here

2
00:00:15,000 --> 00:00:30,000
Next subtitle text
```

**Use Case:** Import from subtitle files, video platforms
**Screen:** 05_upload_transcription_screen
**Size:** ~2.6 KB
**Test:** SRT parsing, timestamp extraction

---

#### 5. **sample_transcription.vtt** (WebVTT Format)
Transcription in WebVTT subtitle format (.vtt).

**Format:**
```
WEBVTT

00:00:00.000 --> 00:00:15.000
Subtitle text here

00:00:15.000 --> 00:00:30.000
Next subtitle text
```

**Use Case:** Web video subtitles, HTML5 video
**Screen:** 05_upload_transcription_screen
**Size:** ~2.5 KB
**Test:** VTT parsing, browser compatibility

---

### Export Examples

#### 6. **exported_entities_tools.json** (5 tools)
Sample export of extracted tool entities from Phase 2.

**Entities:**
- Claude Desktop (NEW)
- n8n (EXISTING)
- MCP Server Protocol (NEW)
- Supabase (EXISTING)
- ChatGPT API (UPDATE)

**Fields:**
- `entity_type`: "TOOL"
- `classification`: NEW/EXISTING/UPDATE
- `category`: AI, AUTOMATION, DATABASE
- `confidence_score`: 0-1
- `metadata`: Pricing, platform, website, etc.

**Use Case:** Export entity extraction results
**Screen:** 06_entity_extraction_viewer
**Test:** JSON export download, data integrity

---

#### 7. **exported_entities_workflows.json** (4 workflows)
Sample export of extracted workflow entities from Phase 2.

**Workflows:**
- MCP Server Setup Process (8 steps, 15 min)
- n8n Automation Workflow Creation (12 steps, 30 min)
- Supabase Row Level Security Setup (10 steps, 45 min)
- Figma to React Component Conversion (7 steps, 25 min)

**Fields:**
- `entity_type`: "WORKFLOW"
- `steps_count`: Number of steps
- `estimated_time_minutes`: Duration
- `difficulty`: Easy/Medium/Hard
- `prerequisites`: Array of requirements
- `outputs`: Expected results

**Use Case:** Export workflow extraction results
**Screen:** 06_entity_extraction_viewer
**Test:** JSON export download, workflow analysis

---

## 🧪 Testing Scenarios

### Scenario 1: Bulk Video Import
1. Navigate to bulk import screen
2. Download CSV template
3. Upload `video_import_template.csv`
4. Verify 10 rows parsed correctly
5. Check validation (all should pass)
6. Import to database
7. Verify in video queue table

### Scenario 2: Transcription Upload
1. Navigate to upload transcription screen
2. Select video from dropdown
3. Test each format:
   - Drag `sample_transcription.txt` → Should show preview
   - Upload `sample_transcription.srt` → Should parse timestamps
   - Upload `sample_transcription.vtt` → Should validate format
4. Verify file size < 10MB
5. Submit and check database update

### Scenario 3: Entity Export
1. Navigate to entity extraction viewer
2. View extracted tools
3. Click "Export JSON"
4. Compare downloaded file with `exported_entities_tools.json`
5. Repeat for workflows
6. Verify JSON structure matches schema

### Scenario 4: Error Handling
1. Create invalid CSV (wrong column names)
2. Upload oversized file (> 10MB)
3. Upload unsupported format (.doc)
4. Upload malformed JSON
5. Verify error messages display correctly

---

## 📊 Data Validation Rules

### Video Import
- **video_url**: Valid URL format, starts with https://
- **video_title**: Min 3 characters, max 255
- **duration_minutes**: Integer 1-999
- **priority**: Must be low/medium/high
- **department**: Must be DEV/SMM/VID/AID/DGN/MKT
- **assigned_to**: Valid email format

### Transcription Files
- **File types**: .txt, .srt, .vtt only
- **Max size**: 10 MB
- **Encoding**: UTF-8
- **SRT format**: Must have sequence numbers and timestamps
- **VTT format**: Must start with "WEBVTT"

### Entity Exports
- **Classification**: NEW/EXISTING/UPDATE only
- **Confidence score**: Decimal 0.0-1.0
- **Entity IDs**: Format XXX-###-### (e.g., TOOL-AI-224)
- **Timestamps**: ISO 8601 format

---

## 🔄 File Format Conversions

### CSV to JSON
```bash
# Use Papa Parse (already in dependencies)
import Papa from 'papaparse';
Papa.parse(csvFile, { header: true });
```

### SRT to Plain Text
```javascript
// Remove timestamps and sequence numbers
const text = srtContent
  .replace(/^\d+\s*$/gm, '')
  .replace(/\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}/g, '');
```

### JSON to CSV
```javascript
// Use Papa Parse unparse
import Papa from 'papaparse';
const csv = Papa.unparse(jsonData);
```

---

## 📝 Adding New Sample Data

When adding new sample files:

1. **Follow naming convention**: `{type}_{description}.{ext}`
2. **Keep file sizes small**: < 5 MB for samples
3. **Include metadata**: Add entry to this README
4. **Use realistic data**: Based on actual use cases
5. **Validate format**: Ensure parseable by target screen
6. **Document fields**: List all columns/properties
7. **Include edge cases**: Valid, invalid, boundary examples

---

## 🎯 Quick Reference

| File | Format | Size | Use Case | Screen |
|------|--------|------|----------|---------|
| video_import_template.csv | CSV | 1 KB | Bulk import | 11_bulk_video_import |
| video_import_sample.json | JSON | 0.8 KB | API import | 11_bulk_video_import |
| sample_transcription.txt | TXT | 3.8 KB | Upload text | 05_upload_transcription |
| sample_transcription.srt | SRT | 2.6 KB | Upload subtitles | 05_upload_transcription |
| sample_transcription.vtt | VTT | 2.5 KB | Upload WebVTT | 05_upload_transcription |
| exported_entities_tools.json | JSON | 2.2 KB | Export entities | 06_entity_extraction_viewer |
| exported_entities_workflows.json | JSON | 2.0 KB | Export workflows | 06_entity_extraction_viewer |

---

**Created:** 2025-11-28
**Purpose:** Sample data library for development and testing
**Maintained by:** Research Management System Team
