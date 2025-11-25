# Multi-Phase Import Prompt Template for BUSINESSES Entity

This document provides reusable prompt templates for importing business data from various sources into the BUSINESSES entity structure.

**Last Updated:** 2025-11-21
**Tested With:** Sales Nov25 dataset (37 entities, 91.9% data quality)

---

## Overview of Multi-Phase Approach

The multi-phase import methodology consists of 4-8 phases depending on dataset complexity:

### Core Phases (Always Required)

**Phase 1: Validation & Preparation**
- Validate source data quality
- Identify data issues
- Create staging environment
- Generate validation report

**Phase 2: Entity Extraction & Categorization**
- Parse source data into structured format
- Categorize entities (Clients, Prospects, Ex-Clients)
- Generate company IDs (BUS-YYYY-XXX)
- Transform dates to ISO format
- Calculate relationship health
- Generate tags

**Phase 3: Data Enrichment**
- Match entities to supporting documents (transcripts, emails)
- Extract additional context
- Enrich entity records
- Build communication history

**Phase 4: JSON File Generation**
- Create BUSINESSES directory structure
- Generate individual JSON files per entity
- Create index files for each sub-entity type
- Generate master catalog with statistics

### Optional Phases (Dataset-Dependent)

**Phase 5: Document Linking**
- Link transcripts and supporting documents
- Create document inventory
- Validate file paths

**Phase 6: Relationship Mapping**
- Map to Products/Services
- Link to Talents/Employees
- Identify cross-sell opportunities

**Phase 7: Validation & QA**
- Deep schema validation
- Cross-reference validation
- Data integrity checks

**Phase 8: Final Documentation**
- Import summary
- User guide
- Statistics dashboard

---

## Prompt Template: Complete Import

Use this prompt to execute a full multi-phase import:

```
Build me a multi-phase import system for the following entity:

SOURCE: [Path to source data file or directory]
TARGET: Dropbox\ENTITIES\BUSINESSES
CONTEXT: [Path to supporting documents or context files]

Requirements:
- Validate source data quality and identify issues
- Extract all entities and categorize by type (Clients, Prospects, Ex-Clients)
- Generate unique company IDs (BUS-YYYY-XXX starting from [number])
- Transform dates to ISO 8601 format (YYYY-MM-DD)
- Calculate relationship health scores
- Auto-generate tags based on data patterns
- Enrich with supporting documents where available
- Create individual JSON files following BUSINESSES schema
- Generate index files and master catalog
- Provide comprehensive documentation

Please follow an 8-phase approach:
1. Validation & Preparation
2. Entity Extraction & Categorization
3. Data Enrichment
4. JSON File Generation
5. Document Linking
6. Relationship Mapping
7. Validation & QA
8. Final Documentation

Create Python scripts for each phase that can be run independently.
```

---

## Prompt Template: Quick Import (Core Phases Only)

For simpler datasets or when time is limited:

```
Build a 4-phase import for the following:

SOURCE: [Path to source data]
TARGET: Dropbox\ENTITIES\BUSINESSES

Execute core phases only:
- Phase 1: Validate source data
- Phase 2: Extract and categorize entities
- Phase 3: Basic enrichment
- Phase 4: Generate JSON files

Skip advanced phases (document linking, relationship mapping).
```

---

## Source Data Requirements

### Minimum Required Fields

For successful import, source data must contain:

| Field | Required | Description |
|-------|----------|-------------|
| Company Name | Yes | Business/organization name |
| Contact Name | Recommended | Decision maker name |
| Contact Email | Recommended | Decision maker email |
| Status | Yes | Current stage (Sent, Draft, Client, etc.) |
| Last Contact | Yes | Date of last interaction |
| Sales Manager | Yes | Account manager name |

### Optional but Valuable Fields

| Field | Value |
|-------|-------|
| CRM Link | Links to external CRM system |
| Notes/Comments | Internal notes about relationship |
| To Do / Next Action | Planned follow-up actions |
| Relationship Start Date | When relationship began |
| Services Discussed | What services they're interested in |
| Transcripts | Call recordings or notes |
| Email Content | Communication history |
| Dropbox Path | Links to supporting documents |

### Supported Source Formats

- ✅ Markdown tables (.md)
- ✅ CSV files (.csv)
- ✅ Excel spreadsheets (.xlsx)
- ✅ JSON files (.json)
- ✅ Plain text with structure
- ⚠️ PDF exports (may require preprocessing)

---

## Categorization Rules

### Clients (Active Paying Customers)

**Criteria:**
- Status = "Sent" OR "Active" OR "Client"
- AND Comments contain: "hired", "signed", "paying", "active project"
- OR active_projects array is populated

**Target Status:** `Active_Client`
**Target Directory:** `BUSINESSES/Clients/`

### Prospects (Potential Customers)

**Criteria:**
- Status = "Sent" OR "Draft" OR "Transcript" OR "Lead"
- AND No hiring activity
- AND Still in communication

**Target Status:**
- "Sent" → `Active_Outreach`
- "Draft" → `Pipeline_Stage_Qualification`
- "Transcript" → `Pipeline_Stage_Early`

**Target Directory:** `BUSINESSES/Prospects/`

### Ex-Clients (Former Customers)

**Criteria:**
- Status = "Lost" OR "Inactive" OR "Paused"
- OR Comments contain: "follow up next year", "reengagement", "closed"

**Target Status:** `Reengagement_Queue`
**Target Directory:** `BUSINESSES/Ex_Clients/`

---

## Data Transformation Standards

### Date Format Conversion

```
Source Format: MM/DD/YYYY (e.g., "10/8/2025")
Target Format: YYYY-MM-DD (e.g., "2025-10-08")
```

**Python Implementation:**
```python
from datetime import datetime
dt = datetime.strptime(date_str, "%m/%d/%Y")
iso_date = dt.strftime("%Y-%m-%d")
```

### Contact Restructuring

```
Source:
- Client Name: "John Doe"
- Email: "john@company.com"

Target:
"decision_makers": [
  {
    "name": "John Doe",
    "title": "Unknown",
    "email": "john@company.com"
  }
]
```

### ID Generation

```
Pattern: BUS-YYYY-XXX
Starting: Check existing max ID in BUSINESSES_Master.json
Increment: Sequential (001, 002, 003, ...)

Example:
- First import: BUS-2025-001
- Second import: BUS-2025-038 (if 37 already exist)
```

### Relationship Health Calculation

```python
def calculate_health(last_contact_date, status):
    days_ago = (today - last_contact_date).days

    if days_ago < 30 and status == "Active":
        return "Strong"
    elif days_ago < 60:
        return "Moderate"
    else:
        return "Weak"
```

### Tag Generation Rules

**Auto-Generate Tags From:**

1. **Sub-Entity Type:**
   - Client → `active_client`
   - Prospect → `active_prospect`
   - Ex-Client → `reengagement`

2. **Account Manager:**
   - "Anastasia" → `anastasia_portfolio`
   - "Anush" → `anush_portfolio`

3. **Status:**
   - Active_Outreach → `outreach`
   - Pipeline_Stage_* → `qualification` or `early_stage`

4. **Comments Keywords:**
   - "hired" → `hired`
   - "interview" → `interview`
   - "follow up" → `follow_up_needed`
   - "lg" OR "lead gen" → `lead_generation`
   - "design" → `design_services`
   - "smm" → `social_media`
   - "ai" OR "automation" → `ai_automation`
   - "developer" → `development`

5. **Time-Based:**
   - Last contact > 30 days → `needs_followup`
   - Last contact > 60 days → `dormant`

---

## JSON Schema Template

```json
{
  "entity_type": "BUSINESSES",
  "sub_entity": "Client|Prospect|Ex_Client",
  "company_id": "BUS-2025-XXX",
  "company_name": "Company Name Here",
  "status": "Active_Client|Active_Outreach|Pipeline_Stage_*|Reengagement_Queue",

  "industry": "AI|Technology|Finance|Healthcare|etc",
  "company_size": "1-10|11-50|51-200|201-500|500+|Unknown",
  "location": "Country/Region or Unknown",

  "relationship_start": "YYYY-MM-DD",
  "lifetime_value": 0,
  "current_monthly_revenue": 0,

  "account_manager": "Manager_Name",
  "decision_makers": [
    {
      "name": "Contact Name",
      "title": "Job Title",
      "email": "email@company.com"
    }
  ],

  "active_projects": ["Project_Name_1", "Project_Name_2"],
  "relationship_health": "Strong|Moderate|Weak|Unknown",

  "tags": ["tag1", "tag2", "tag3"],

  "crm_link": "https://...",
  "transcription_link": "Reference to transcript",
  "google_doc": "Google Doc reference",
  "dropbox_path": "/path/to/files",

  "last_contact": "YYYY-MM-DD",
  "next_action": "Next steps or to-do items",

  "communication_history": [
    {
      "date": "YYYY-MM-DD",
      "type": "call_transcript|email|meeting",
      "summary": "Brief summary of communication",
      "file_path": "/path/to/document"
    }
  ],

  "notes": "Internal notes and comments",
  "email_content": "Email correspondence if available",
  "approved": "TRUE|FALSE|Unknown",

  "metadata": {
    "created_date": "YYYY-MM-DD HH:MM:SS",
    "import_source": "Source_Name",
    "import_date": "YYYY-MM-DD",
    "file_name": "filename.json",
    "last_updated": "YYYY-MM-DD HH:MM:SS"
  }
}
```

---

## File Naming Convention

### Individual Entity Files

```
Pattern: BUSINESSES_[SubEntity]_[CompanyName]_[CompanyID].json

Examples:
- BUSINESSES_Client_Acme_Corporation_BUS-2025-001.json
- BUSINESSES_Prospect_Tech_Startup_Inc_BUS-2025-042.json
- BUSINESSES_Ex_Client_Global_Services_BUS-2025-015.json

Rules:
- Remove special characters from company name
- Replace spaces with underscores
- Limit company name to 50 characters
- Always include company_id at end
```

### Index Files

```
Clients/Clients_INDEX.json
Prospects/Prospects_INDEX.json
Ex_Clients/Ex_Clients_INDEX.json
```

### Master Catalog

```
BUSINESSES_Master.json
```

---

## Directory Structure

```
BUSINESSES/
├── Clients/
│   ├── Clients_INDEX.json
│   └── BUSINESSES_Client_*.json (multiple files)
├── Prospects/
│   ├── Prospects_INDEX.json
│   └── BUSINESSES_Prospect_*.json (multiple files)
├── Ex_Clients/
│   ├── Ex_Clients_INDEX.json
│   └── BUSINESSES_Ex_Client_*.json (multiple files)
├── Companies/ (reserved for future use)
└── BUSINESSES_Master.json
```

---

## Import Documentation Template

Every import should generate these files in `ENTITIES/IMPORTS/YYYY-MM-DD_SourceName/`:

### Required Files

1. **validation_report.md** - Phase 1 results
2. **categorization_report.md** - Phase 2 results
3. **enrichment_report.md** - Phase 3 results (if applicable)
4. **phase4_generation_report.md** - Phase 4 results
5. **FINAL_IMPORT_SUMMARY.md** - Complete summary
6. **STATISTICS_DASHBOARD.md** - Analytics and metrics

### Optional Files

7. **document_inventory.md** - Phase 5 results
8. **relationship_mapping.md** - Phase 6 results
9. **validation_results.md** - Phase 7 results

### Source Data Copies

- **source_data_raw.csv** - Original data export
- **entities_extracted.json** - Structured entities
- **entities_enriched.json** - Enriched entities (if applicable)

---

## Quality Metrics

### Target Quality Scores

| Metric | Target | Acceptable | Poor |
|--------|--------|------------|------|
| Source Data Quality | >95% | 85-95% | <85% |
| Field Completeness | >90% | 75-90% | <75% |
| Enrichment Rate | >30% | 15-30% | <15% |
| Tag Coverage | 100% | >95% | <95% |
| Schema Compliance | 100% | 100% | <100% |

### Success Criteria

✅ **Import Successful If:**
- All entities migrated (100%)
- All JSON files valid and conform to schema
- All required fields populated (or documented as missing)
- Index files and master catalog generated
- Comprehensive documentation created

---

## Common Issues & Solutions

### Issue: Missing Required Fields

**Problem:** Source data lacks required fields (e.g., last_contact, sales_manager)

**Solution:**
- Document missing fields in validation report
- Use fallback values: "Unknown", empty string, or null
- Flag entities for manual review
- Add to data quality issues list

### Issue: Date Format Inconsistencies

**Problem:** Multiple date formats in source data

**Solution:**
```python
def parse_flexible_date(date_str):
    formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except:
            continue
    return None  # Could not parse
```

### Issue: Duplicate Company Names

**Problem:** Same company appears multiple times

**Solution:**
- Check company_id uniqueness
- Review CRM links to identify true duplicates
- Merge records if truly duplicate
- Keep separate if different divisions/projects

### Issue: Low Enrichment Rate

**Problem:** Few entities match to supporting documents

**Solution:**
- Use fuzzy matching for company names
- Check multiple variations (abbreviations, full names)
- Manual review of unmatched transcripts
- Document enrichment opportunities for manual processing

---

## Example Python Script Structure

### Phase 1 Script Template

```python
import csv, json, re
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_FILE = Path(r"path/to/source.csv")
OUTPUT_DIR = Path(r"ENTITIES/IMPORTS/YYYY-MM-DD_Source")

def validate_data(records):
    issues = []
    # Validation logic here
    return issues

def main():
    print("PHASE 1: VALIDATION")
    # Load source data
    # Validate each record
    # Generate report
    # Export results

if __name__ == "__main__":
    main()
```

### Phase 2 Script Template

```python
def categorize_entity(record):
    # Categorization logic
    return sub_entity, status

def generate_company_id(index):
    return f"BUS-{datetime.now().year}-{index:03d}"

def create_entity(record, index):
    entity = {
        "entity_type": "BUSINESSES",
        "company_id": generate_company_id(index),
        # ... more fields
    }
    return entity

def main():
    print("PHASE 2: ENTITY EXTRACTION")
    # Parse source data
    # Categorize each record
    # Generate company IDs
    # Transform data
    # Export entities
```

### Phase 4 Script Template

```python
def create_json_file(entity):
    subdir = map_subdir(entity['sub_entity'])
    filename = generate_filename(entity)
    filepath = BUSINESSES_DIR / subdir / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(entity, f, indent=2)

    return filepath

def create_master_catalog(entities):
    catalog = {
        "entity_type": "BUSINESSES",
        "total_entities": len(entities),
        # ... statistics
    }
    # Generate catalog
    # Save to file
```

---

## Post-Import Checklist

After completing an import, verify:

- [ ] All source records accounted for
- [ ] All JSON files created and valid
- [ ] Index files generated for all sub-entities
- [ ] Master catalog created with statistics
- [ ] All documentation files generated
- [ ] No duplicate company_ids
- [ ] All required fields populated (or documented as missing)
- [ ] Tags applied to all entities
- [ ] Relationship health calculated where possible
- [ ] Source data backed up in import directory
- [ ] User guide updated if needed
- [ ] Import summary reviewed and approved

---

## Future Import Notes

### Next Starting ID

After Sales Nov25 import (37 entities):
- **Next ID:** BUS-2025-038

Check `BUSINESSES_Master.json` → `entities_by_id` for highest current ID.

### Lessons Learned from Sales Nov25

**What Worked Well:**
- ✅ Multi-phase approach provided good structure
- ✅ Automated scripts reduced manual work
- ✅ Comprehensive documentation was valuable
- ✅ Tag auto-generation was effective

**What Could Be Improved:**
- 🔄 Enhance transcript matching (was only 10.8%)
- 🔄 Add fuzzy matching for company names
- 🔄 Automate industry classification
- 🔄 Better handling of missing dates

---

**Template Version:** 1.0
**Created:** 2025-11-21
**Based On:** Sales Nov25 import success

**For questions or updates to this template, refer to:**
`ENTITIES/IMPORTS/2025-11-21_Sales_Nov25/FINAL_IMPORT_SUMMARY.md`
