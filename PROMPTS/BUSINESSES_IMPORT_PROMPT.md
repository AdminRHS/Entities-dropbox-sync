# Multi-Phase Import Prompt: BUSINESSES Entity

## Overview

This prompt template creates a complete multi-phase import system for importing business/client data from various sources into the BUSINESSES entity structure.

---

## Primary Import Prompt

```
Build me a multi-phase import system for the following entity:

SOURCE: Dropbox\ENTITIES\BUSINESSES
CONTEXT: Dropbox\Nov25\Sales Nov25

Take as Source Context from the Sales Nov25 directory, specifically:
- client_list.md (primary data source with 37+ client records)
- Sales Nov25\Clients\ (call transcripts and supporting documents)
- Sales_Oct25\ archive (additional client folders and documents)

Requirements:
1. Validate source data quality and identify issues
2. Extract all entities and categorize by type (Clients, Prospects, Ex-Clients)
3. Generate unique company IDs (BUS-2025-XXX starting from 001)
4. Transform dates to ISO 8601 format (YYYY-MM-DD)
5. Calculate relationship health scores based on last contact + status
6. Auto-generate tags based on data patterns (status, services, manager, timeline)
7. Enrich with supporting documents where available (transcripts, emails)
8. Create individual JSON files following BUSINESSES schema
9. Generate index files and master catalog with statistics
10. Review ALL archive directories (Oct25, Sep25, Aug25) for additional entities
11. Provide comprehensive documentation and user guides

Please follow a multi-phase approach:
- Phase 1: Validation & Preparation
- Phase 2: Entity Extraction & Categorization
- Phase 3: Data Enrichment (from transcripts)
- Phase 4: JSON File Generation
- Phase 5: Archive Review & Supplementary Import (Oct25, etc.)
- Phase 6: Documentation & Statistics

Create Python scripts for each phase that can be run independently.
```

---

## Source Data Schema

### Expected Fields in client_list.md

| Field | Required | Description |
|-------|----------|-------------|
| Client Company | Yes | Business/organization name |
| CRM Link | Yes | Link to CRM system |
| Transcription Link | Recommended | Reference to call notes |
| Google Doc | Optional | Document reference |
| Dropbox | Recommended | Path to client files |
| Client Name | Yes | Decision maker name |
| Email | Yes | Contact email |
| Status | Yes | Current stage (Sent, Draft, Transcript, etc.) |
| Comments | Recommended | Internal notes about relationship |
| To Do | Optional | Next action items |
| Last Contact Day | Yes | Date of last interaction |
| Date | Recommended | Relationship start date |
| Sales Manager | Yes | Account manager name |
| Approved | Optional | Approval status |
| Email Content | Optional | Email correspondence |

---

## Categorization Rules

### Clients (Active Paying Customers)
**Criteria:**
- Status = "Sent" OR "Active" OR "Client"
- AND Comments contain: "hired", "signed", "paying", "active project"
- OR active_projects array is populated

**Target:**
- Sub-entity: "Client"
- Status: "Active_Client"
- Directory: BUSINESSES/Clients/

### Prospects (Potential Customers)
**Criteria:**
- Status = "Sent" OR "Draft" OR "Transcript" OR "Lead"
- AND No hiring activity
- AND Still in communication

**Target:**
- Sub-entity: "Prospect"
- Status mapping:
  - "Sent" → "Active_Outreach"
  - "Draft" → "Pipeline_Stage_Qualification"
  - "Transcript" → "Pipeline_Stage_Early"
- Directory: BUSINESSES/Prospects/

### Ex-Clients (Former Customers)
**Criteria:**
- Status = "Lost" OR "Inactive" OR "Paused" OR "new year"
- OR Comments contain: "follow up next year", "reengagement"

**Target:**
- Sub-entity: "Ex_Client"
- Status: "Reengagement_Queue"
- Directory: BUSINESSES/Ex_Clients/

---

## Data Transformations

### Date Format
```python
Source: MM/DD/YYYY (e.g., "10/8/2025")
Target: YYYY-MM-DD (e.g., "2025-10-08")
```

### Contact Restructuring
```python
Source:
  Client Name: "John Doe"
  Email: "john@company.com"

Target:
  decision_makers: [
    {
      "name": "John Doe",
      "title": "Unknown",
      "email": "john@company.com"
    }
  ]
```

### ID Generation
```python
Pattern: BUS-YYYY-XXX
Example: BUS-2025-001, BUS-2025-002, ...
Increment: Sequential
```

### Relationship Health
```python
Algorithm:
  days_ago = (today - last_contact_date).days

  if days_ago < 30 and status == "Active":
      return "Strong"
  elif days_ago < 60:
      return "Moderate"
  else:
      return "Weak"
```

### Tag Generation
**Auto-generate from:**
1. Sub-entity type: `active_client`, `active_prospect`, `reengagement`
2. Account manager: `anastasia_portfolio`, `anush_portfolio`
3. Status: `outreach`, `qualification`, `early_stage`
4. Comments keywords: `hired`, `interview`, `follow_up_needed`, `lead_generation`, `design_services`, `ai_automation`
5. Timeline: `needs_followup` (>30 days), `dormant` (>60 days)

---

## Target JSON Schema

```json
{
  "entity_type": "BUSINESSES",
  "sub_entity": "Client|Prospect|Ex_Client",
  "company_id": "BUS-2025-XXX",
  "company_name": "Company Name",
  "status": "Active_Client|Active_Outreach|Pipeline_Stage_*|Reengagement_Queue",

  "industry": "AI|Technology|Finance|Healthcare|etc",
  "company_size": "Unknown",
  "location": "Unknown",

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

  "active_projects": ["Project_1", "Project_2"],
  "relationship_health": "Strong|Moderate|Weak|Unknown",
  "tags": ["tag1", "tag2", "tag3"],

  "crm_link": "https://...",
  "transcription_link": "Reference",
  "google_doc": "Reference",
  "dropbox_path": "/path/to/files",

  "last_contact": "YYYY-MM-DD",
  "next_action": "Next steps",

  "communication_history": [
    {
      "date": "YYYY-MM-DD",
      "type": "call_transcript|email|meeting",
      "summary": "Summary",
      "file_path": "/path/to/file"
    }
  ],

  "notes": "Internal notes",
  "email_content": "Email text",
  "approved": "TRUE|FALSE",

  "metadata": {
    "created_date": "YYYY-MM-DD HH:MM:SS",
    "import_source": "Sales_Nov25",
    "import_date": "YYYY-MM-DD",
    "file_name": "filename.json",
    "last_updated": "YYYY-MM-DD HH:MM:SS"
  }
}
```

---

## File Naming Convention

```
Individual Entity Files:
  BUSINESSES_[SubEntity]_[CompanyName]_[CompanyID].json

Examples:
  BUSINESSES_Client_Acme_Corporation_BUS-2025-001.json
  BUSINESSES_Prospect_Tech_Startup_BUS-2025-042.json
  BUSINESSES_Ex_Client_Global_Services_BUS-2025-015.json

Index Files:
  Clients/Clients_INDEX.json
  Prospects/Prospects_INDEX.json
  Ex_Clients/Ex_Clients_INDEX.json

Master Catalog:
  BUSINESSES_Master.json
```

---

## Directory Structure

```
BUSINESSES/
├── Clients/
│   ├── Clients_INDEX.json
│   └── BUSINESSES_Client_*.json
├── Prospects/
│   ├── Prospects_INDEX.json
│   └── BUSINESSES_Prospect_*.json
├── Ex_Clients/
│   ├── Ex_Clients_INDEX.json
│   └── BUSINESSES_Ex_Client_*.json
├── Companies/ (reserved)
└── BUSINESSES_Master.json
```

---

## Required Deliverables

### Python Scripts
1. `phase1_validation.py` - Validate source data
2. `phase2_entity_extraction.py` - Extract and categorize
3. `phase3_data_enrichment.py` - Enrich from transcripts
4. `phase4_json_generation.py` - Generate JSON files
5. `phase5_supplement_oct25.py` - Add missing entities from archives

### Reports
1. `validation_report.md` - Data quality analysis
2. `categorization_report.md` - Entity breakdown
3. `enrichment_report.md` - Enrichment results
4. `phase4_generation_report.md` - File generation summary
5. `phase5_supplementary_report.md` - Archive review results
6. `SALES_OCT25_ANALYSIS.md` - Archive analysis
7. `FINAL_IMPORT_SUMMARY.md` - Complete summary
8. `STATISTICS_DASHBOARD.md` - Analytics and KPIs
9. `COMPLETE_IMPORT_SUMMARY.md` - Final comprehensive summary

### User Documentation
1. `USER_GUIDE_BUSINESSES.md` - Complete usage guide
2. `MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md` - Reusable template

---

## Quality Targets

| Metric | Target |
|--------|--------|
| Source Data Quality | >90% |
| Entity Coverage | 100% |
| Schema Compliance | 100% |
| Field Completeness | >75% |
| Tag Coverage | 100% |
| Documentation | Complete |

---

## Success Criteria

- ✅ All entities from all sources imported (no data loss)
- ✅ All JSON files valid and schema-compliant
- ✅ All archives reviewed (Oct25, Sep25, Aug25, Jul25)
- ✅ Index files and master catalog generated
- ✅ Comprehensive documentation provided
- ✅ User guide for navigation created
- ✅ Reusable template for future imports

---

## Archive Review Checklist

When reviewing archives (Sales_Oct25, Sales_Sep25, etc.):

1. **List all client folders** in archive
2. **Cross-reference** with main import entities
3. **Identify new clients** not in main list
4. **Extract supporting documents** (transcripts, emails)
5. **Create supplementary entities** for new clients
6. **Enrich existing entities** with archive documents
7. **Update master catalog** with new totals
8. **Document findings** in analysis report

---

## Example Usage

```
User: "Build me a multi-phase import prompt for the BUSINESSES entity
       from Dropbox\Nov25\Sales Nov25"