# BUSINESSES Import - Refreshed Strategy & Prompts

**Created:** 2025-11-22
**Version:** 2.0
**Status:** Ready for Execution

---

## Executive Summary

This document consolidates the complete import strategy for the BUSINESSES entity, incorporating all sub-entities, lookup tables, and architectural decisions made during planning.

---

## 1. Complete Data Model Overview

### 1.1 Entity Structure

```
BUSINESSES/
├── Clients/                    # Converted clients
├── Prospects/                  # Pre-conversion pipeline
├── Ex_Clients/                 # Former clients
├── schemas/                    # JSON schemas
│
├── Industries/                 # Lookup tables (root level)
├── SubIndustries/
├── Positions/
├── CompanySizes/
├── LeadStatuses/
├── LeadSources/
├── Countries/
├── ContactTypes/
├── Templates/
│
├── JobRequests/                # Job request lookups (nested)
│   ├── Professions/
│   ├── Rates/
│   ├── Shifts/
│   ├── Tools/
│   ├── Languages/
│   └── LanguageLevels/
│
└── BUSINESSES_Master.json      # Master index
```

### 1.2 Sub-Entity Summary

| # | Sub-Entity | Purpose | Source Tables |
|---|------------|---------|---------------|
| 2.2 | Company | Core company data | companies, company_cities, company_industries |
| 2.3 | POCs | Points of contact | pocs, poc_contacts, poc_types |
| 2.4 | Business Relationship | Lead/Client/Affiliate status | businesses, leads, clients, affiliates |
| 2.5 | Communication History | All interactions | manual + google_calendar |
| 2.6 | Prospect | Pre-conversion contact | prospects, prospect_contacts |
| 2.7 | Prospect Company | Pre-conversion company | prospect_companies, prospect_company_industries |
| 2.8 | Prospect Communications | Prospect interactions | prospect_communications |
| 2.9 | Assigned Users | Team assignments | business_users |
| 2.10 | Lookup Tables | Reference data | 9 root + 6 nested folders |
| 2.11 | Job Requests | Hiring positions | job_requests + 4 pivot tables |
| 2.12 | References | External links | CRM, Dropbox, Calendar |
| 2.13 | Metadata | System tracking | tags, timestamps, quality |
| 2.14 | Templates | Message/email templates | 4 template types |

---

## 2. Data Sources Inventory

### 2.1 Primary Sources

| Source | Location | Records | Data Type |
|--------|----------|---------|-----------|
| client_list.md | Nov25/Sales Nov25/ | 40+ | Structured table |
| Client_JSON_Clusters | Nov25/Niko Nov25/ExportCRMS/ | 100+ | CRM export |

### 2.2 Secondary Sources

| Source | Location | Records | Data Type |
|--------|----------|---------|-----------|
| Sales_Oct25/Clients | Nov25/Sales Nov25/ | 30+ | Client folders |
| Sales Sep25 | Nov25/ | 19+ | Transcripts |
| Sales Aug25 | Nov25/ | 18+ | Transcripts |
| Sales Jul25 | Nov25/ | 12+ | Transcripts |

### 2.3 Enrichment Sources

| Source | Purpose |
|--------|---------|
| first call transcripts | Client needs, interests |
| client_deepresearch | Background research |
| Email templates | Service interests |

---

## 3. Revised Phase Execution Plan

### Phase 0: Cleanup & Archive
**Purpose:** Backup existing data, create fresh structure

**Actions:**
1. Archive existing BUSINESSES/*.json to `archive_2025-11-22/`
2. Create folder structure:
   - Root lookup folders (9)
   - JobRequests nested folders (6)
   - Entity folders (Clients, Prospects, Ex_Clients)
   - schemas folder
3. Generate phase0_report.md

**Output:** Clean folder structure ready for import

---

### Phase 1: Schema Definition
**Purpose:** Create formal JSON schemas with all sub-entities

**Actions:**
1. Generate BUSINESSES_SCHEMA.json with:
   - All 14 sub-entity definitions
   - Required field markers
   - Data type validations
   - FK relationship definitions
2. Add `schema_version: "1.0.0"` to metadata
3. Standardize date format: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`)
4. Generate schema documentation

**Output:**
- `schemas/BUSINESSES_SCHEMA.json`
- `schemas/field_definitions.md`
- `schemas/validation_rules.json`

---

### Phase 2: Lookup Table Population
**Purpose:** Extract and create all reference data

**Actions:**
1. Parse Client_JSON_Clusters for unique values:
   - Industries/SubIndustries
   - CompanySizes
   - LeadStatuses/LeadSources
   - Countries
   - ContactTypes
2. Create Positions from POC data
3. Create JobRequests lookups from job_requests data:
   - Professions, Rates, Shifts
   - Tools, Languages, LanguageLevels
4. Generate INDEX files for each folder
5. Create Templates from existing email templates

**Output:** All lookup folders populated with INDEX files

---

### Phase 3: Field Classification & Mapping
**Purpose:** Map all source fields to target schema

**Actions:**
1. Classify client_list.md columns (15 fields)
2. Map CRM export fields to sub-entities
3. Define transformation functions:
   - `normalize_company_name()`
   - `parse_date()`
   - `extract_services()`
   - `calculate_urgency()`
4. Document unmapped fields

**Output:**
- `mapping_rules.json`
- `transformation_functions.py`
- `field_classification_report.md`

---

### Phase 4: Data Extraction (Read-Only)
**Purpose:** Extract all data without modifying sources

**Actions:**
1. Parse client_list.md → raw records
2. Parse Client_JSON_Clusters → CRM data
3. List Oct25/Clients folders → company names
4. Scan transcripts → communication history
5. Track processed records in registry

**Output:**
- `raw_extracted_data.json`
- `processing_registry.json`
- `extraction_report.md`

---

### Phase 5: Metadata Tagging
**Purpose:** Apply tagging logic to derive metadata

**Tagging Rules:**

| Source Field | Pattern | Tag/Field |
|--------------|---------|-----------|
| Comments | "lg", "lead gen" | services_of_interest: Lead Generation |
| Comments | "dev", "developer" | services_of_interest: Development |
| Comments | "ai", "automation" | services_of_interest: AI/Automation |
| Comments | "hired" | tags: hired, entity_type: Client |
| To Do | "urgent", "asap" | urgency_level: high |
| Status | "Active" | tags: active_prospect |

**Output:**
- `enriched_data.json`
- `tagging_rules_applied.json`

---

### Phase 6: Entity Categorization
**Purpose:** Classify as Client/Prospect/Ex_Client

**Decision Tree:**
```
1. Comments contains "hired" → Client
2. Comments contains "stopped" → Ex_Client
3. Has job_requests → Client (active hiring)
4. Status = "sent" → Prospect (Active_Outreach)
5. Default → Prospect
```

**Output:**
- `categorized_entities.json`
- `categorization_report.md`

---

### Phase 7: ID Generation & Deduplication
**Purpose:** Assign unique IDs, merge duplicates

**ID Formats:**
- Company: `BUS-2025-###`
- POC: `POC-###`
- Prospect: `PROS-###`
- Job Request: `JR-###`
- Communication: `COMM-###`

**Deduplication Logic:**
1. Normalize company names (lowercase, trim, remove punctuation)
2. Match by email address
3. Match by CRM ID
4. Merge records, keep most recent data

**Output:**
- `deduplicated_entities.json`
- `id_registry.json`
- `duplicate_report.md`

---

### Phase 8: JSON Generation
**Purpose:** Create individual entity files

**File Naming:**
```
BUSINESSES_Client_[CompanyName]_[ID].json
BUSINESSES_Prospect_[CompanyName]_[ID].json
BUSINESSES_Ex_Client_[CompanyName]_[ID].json
```

**Actions:**
1. Generate entity JSON files
2. Create category index files
3. Generate BUSINESSES_Master.json
4. Update all INDEX files

**Output:** All entity JSON files in appropriate folders

---

### Phase 9: Validation
**Purpose:** Verify data quality and schema compliance

**Validation Checks:**

| Check | Type | Target |
|-------|------|--------|
| Schema compliance | Structural | 100% |
| Required fields | Completeness | 100% |
| Unique IDs | Integrity | 100% |
| FK references | Referential | 100% |
| Date formats | Format | ISO 8601 |
| Data quality score | Quality | 85%+ |

**Output:**
- `validation_report.md`
- `quality_metrics.json`
- `issues_log.json`

---

### Phase 10: Documentation
**Purpose:** Generate user guides and reusable prompts

**Output:**
- Updated `USER_GUIDE_BUSINESSES.md`
- `BUSINESSES_IMPORT_PROMPT_v2.md`
- `FINAL_IMPORT_SUMMARY.md`

---

## 4. Reusable Import Prompts

### 4.1 Entity Creation Prompt

```markdown
# Create BUSINESSES Entity

## Input Data
- Company Name: [name]
- Contact Name: [name]
- Email: [email]
- Source: [client_list.md / CRM export]

## Required Sub-Entities
1. Company - Fill from source data
2. POCs - Create from contact info
3. Business Relationship - Set entity_type based on status
4. Communication History - Initialize empty, add from transcripts
5. References - Add CRM link, Dropbox path
6. Metadata - Set tags, timestamps, source_file

## Classification
- Check Comments for "hired" → Client
- Check for job_requests → Client
- Default → Prospect

## Output
Generate JSON following BUSINESSES_SCHEMA.json
Save to appropriate subfolder (Clients/Prospects/Ex_Clients)
```

### 4.2 Job Request Creation Prompt

```markdown
# Create Job Request

## Input Data
- Position Name: [name]
- Quantity: [number]
- Required Tools: [list]
- Required Languages: [list with levels]
- Demand Date: [date]

## Required Fields
1. Generate ID: JR-###
2. Link to prospect_id or company_id
3. Set status_id (Open by default)
4. Map tools to JobRequests/Tools/ IDs
5. Map languages to JobRequests/Languages/ with level_ids

## Output
Add to entity's job_requests[] array
```

### 4.3 Lookup Table Population Prompt

```markdown
# Populate Lookup Table

## Table: [Industries/Positions/etc.]

## Steps
1. Extract unique values from source
2. Generate sequential IDs
3. Create individual JSON files
4. Generate INDEX file with all entries

## File Format
{
  "id": [number],
  "name": "[value]",
  "created_at": "[ISO timestamp]",
  "is_active": true
}

## Output
- Individual files: [Table]_[Name]_[ID].json
- Index file: [Table]_INDEX.json
```

### 4.4 Communication History Entry Prompt

```markdown
# Add Communication Entry

## Input Data
- Date: [YYYY-MM-DD]
- Time: [HH:MM]
- Type: [Call/Email/Meeting]
- Source: [manual/google_calendar]
- Summary: [brief description]

## Required Fields
1. Generate ID: COMM-###
2. Set duration_minutes if known
3. Add attendees (email addresses)
4. Extract action_items from notes
5. Set conducted_by (sales manager)

## Calendar Integration (Future)
- event_id: [calendar event ID]
- meeting_link: [Zoom/Meet URL]

## Output
Add to entity's communication_history.interactions[]
Update totals (emails_sent, calls_completed, meetings_held)
```

---

## 5. Quality Metrics & Success Criteria

### 5.1 Quantity Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| Total Entities | 50-60+ | Count of JSON files |
| Clients | 5-8 | Entities with type=Client |
| Prospects | 40-50 | Entities with type=Prospect |
| Ex_Clients | 2-5 | Entities with type=Ex_Client |
| Lookup Tables | 15 folders | Populated with INDEX files |

### 5.2 Quality Targets

| Metric | Target | Validation |
|--------|--------|------------|
| Schema Compliance | 100% | JSON Schema validation |
| Required Fields | 100% | Field presence check |
| ID Uniqueness | 100% | No duplicates in registry |
| FK Integrity | 100% | All references exist |
| Date Format | 100% | ISO 8601 compliance |
| Data Completeness | 85%+ | Non-null field percentage |

### 5.3 Data Quality Score

Calculate per entity:
```
score = (filled_fields / total_fields) * 100

- 90-100: Excellent
- 80-89: Good
- 70-79: Acceptable
- <70: Needs improvement
```

---

## 6. Error Handling Strategy

### 6.1 Principles

1. **Never modify source files** - Read-only access
2. **Log all errors** - Track in issues_log.json
3. **Continue processing** - Don't halt on single errors
4. **Checkpoint after phases** - Enable rollback

### 6.2 Error Categories

| Category | Action | Example |
|----------|--------|---------|
| Missing required field | Log warning, set null | No email address |
| Invalid FK reference | Log error, skip reference | Unknown industry_id |
| Duplicate record | Merge, keep newest | Same company in multiple sources |
| Parse error | Log error, skip record | Malformed markdown row |
| Date format error | Log warning, attempt parse | Non-ISO date |

### 6.3 Rollback Points

| Phase | Backup Location | Restore Action |
|-------|-----------------|----------------|
| Phase 0 | archive_2025-11-22/ | Restore from archive |
| Phase 4 | checkpoints/phase_4/ | Re-extract from sources |
| Phase 7 | checkpoints/phase_7/ | Regenerate JSON files |

---

## 7. Execution Checklist

### Pre-Import
- [ ] Review Technical Specification
- [ ] Review Architecture Review
- [ ] Approve all sub-entity schemas
- [ ] Confirm lookup table structure
- [ ] Verify source file access

### Phase Execution
- [ ] Phase 0: Cleanup complete
- [ ] Phase 1: Schemas generated
- [ ] Phase 2: Lookup tables populated
- [ ] Phase 3: Field mapping complete
- [ ] Phase 4: Data extracted
- [ ] Phase 5: Metadata tagged
- [ ] Phase 6: Entities categorized
- [ ] Phase 7: IDs generated, deduplicated
- [ ] Phase 8: JSON files created
- [ ] Phase 9: Validation passed
- [ ] Phase 10: Documentation generated

### Post-Import
- [ ] Review FINAL_IMPORT_SUMMARY.md
- [ ] Verify quality metrics
- [ ] Address issues in issues_log.json
- [ ] Update USER_GUIDE
- [ ] Plan Google Calendar integration

---

## 8. Next Steps

### Immediate Actions
1. **Approve this strategy document**
2. **Begin Phase 0** - Create cleanup script
3. **Execute phases sequentially** with manual approval

### Future Enhancements
1. Google Calendar integration for communication history
2. Automated CRM sync
3. Data quality dashboard
4. Incremental import capability

---

## Appendix: File Locations

| Item | Path |
|------|------|
| Plans | `ENTITIES/PLANS/` |
| Scripts | `ENTITIES/IMPORTS/2025-11-22_Sales_Import/` |
| Output | `ENTITIES/BUSINESSES/` |
| Schemas | `ENTITIES/BUSINESSES/schemas/` |
| Reports | `ENTITIES/IMPORTS/2025-11-22_Sales_Import/` |

---

**Ready to proceed with Phase 0 upon approval.**
