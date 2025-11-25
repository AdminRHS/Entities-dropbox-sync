# BUSINESSES Import - Task Manager

**Created:** 2025-11-22
**Entity:** BUSINESSES
**Source:** Nov25/Sales Nov25 + CRM Export
**Target:** ENTITIES/BUSINESSES/
**Approach:** Manual Processing with Guided Steps

---

## Overview

This task manager provides step-by-step guidance for manually importing BUSINESSES data. Each phase includes clear tasks, checklists, and quality checks. Work at your own pace and mark tasks complete as you go.

---

## Current Status

- ✅ **Phase 0:** Cleanup & Archive - COMPLETED
- ✅ **Phase 1:** Schema Definition - COMPLETED
- ✅ **Phase 2:** Lookup Tables - COMPLETED (285 files)
- ✅ **Phase 3:** Field Mapping - COMPLETED (11 transformation functions)
- ✅ **Phase 4:** Data Extraction - COMPLETED (1000 records)
- ⏸️ **Phase 5:** Manual Entity Creation - IN PROGRESS
- ⏳ **Phase 6-10:** Pending

---

## Phase 5: Manual Entity Creation (CURRENT)

### Objective
Manually create BUSINESSES entities from the extracted CRM data, ensuring quality and accuracy for each record.

### Before You Start

**Review These Files:**
1. `ENTITIES/IMPORTS/2025-11-22_Sales_Import/raw_extracted_data.json` - Full dataset (1000 records)
2. `ENTITIES/IMPORTS/2025-11-22_Sales_Import/raw_extracted_data_sample.json` - Sample (10 records)
3. `ENTITIES/PLANS/BUSINESSES_Import_Technical_Spec_2025-11-22.md` - Schema reference
4. `ENTITIES/IMPORTS/2025-11-22_Sales_Import/mapping_rules.json` - Field mappings

**Lookup Tables Reference:**
- Industries: `BUSINESSES/Industries/Industries_INDEX.json` (117 industries)
- SubIndustries: `BUSINESSES/SubIndustries/SubIndustries_INDEX.json` (55 sub-industries)
- CompanySizes: `BUSINESSES/CompanySizes/CompanySizes_INDEX.json` (18 sizes)
- LeadStatuses: `BUSINESSES/LeadStatuses/LeadStatuses_INDEX.json` (7 statuses)
- Countries: `BUSINESSES/Countries/Countries_INDEX.json` (36 countries)

---

### Task 5.1: Review Sample Data

**Goal:** Understand the data structure before creating entities.

**Steps:**

1. [ ] Open `raw_extracted_data_sample.json` in your editor
2. [ ] Review first 3 records to understand structure:
   - Company name (`company_name`)
   - Contact name (`name`)
   - Industry (`lead_company_industry`)
   - Company size (`lead_company_size`)
   - Lead status (`lead_status`)
   - Email/contact info (`email`, `pocs`)
3. [ ] Note any data quality issues or missing fields
4. [ ] Open extraction report: `phase4_extraction_report.md`
5. [ ] Review coverage statistics (100% companies, 70.9% emails, etc.)

**Questions to Consider:**
- Are company names clean and consistent?
- Do all records have industry information?
- What percentage have contact information?

**Completion Criteria:**
- ✓ Understand CRM data structure
- ✓ Identified key fields for entity creation
- ✓ Noted any data quality concerns

---

### Task 5.2: Create Processing Tracker

**Goal:** Track which records have been processed to avoid duplicates.

**Steps:**

1. [ ] Create spreadsheet: `IMPORTS/2025-11-22_Sales_Import/processing_tracker.xlsx`
2. [ ] Add columns:
   - `Sequence` (1-1000)
   - `CRM_ID` (from `client_id`)
   - `Company_Name` (from `company_name`)
   - `Contact_Name` (from `name`)
   - `Status` (Not Started / In Progress / Complete / Skipped)
   - `Generated_ID` (BUS-2025-###)
   - `Entity_Type` (Client / Prospect / Ex_Client)
   - `Notes` (any issues or special handling)
   - `Date_Processed`

3. [ ] Populate first 3 columns from `processing_registry.json`
4. [ ] Set all Status to "Not Started"
5. [ ] Save and keep this file open while processing

**Completion Criteria:**
- ✓ Tracking spreadsheet created
- ✓ All 1000 records listed
- ✓ Ready to track progress

---

### Task 5.3: Setup Entity Templates

**Goal:** Create reusable templates for quick entity creation.

**Steps:**

1. [ ] Create folder: `IMPORTS/2025-11-22_Sales_Import/Templates/`

2. [ ] Create `Template_Prospect.json`:

```json
{
  "company": {
    "id": "BUS-2025-XXX",
    "name": "",
    "logo": null,
    "website": "",
    "size_id": null,
    "size_label": "",
    "year_established": null,
    "note": "",
    "locations": [],
    "industries": []
  },
  "pocs": [],
  "business_relationship": {
    "entity_type": "Prospect",
    "status_id": null,
    "status_type": "",
    "source_id": null,
    "source_name": "",
    "priority": null,
    "relationship_start_date": null
  },
  "communication_history": {
    "total_interactions": 0,
    "last_contact_date": null,
    "interactions": []
  },
  "assigned_users": {
    "sales_manager_id": null,
    "sales_manager_name": "",
    "lead_agent_id": null,
    "created_by_id": null,
    "created_by_name": ""
  },
  "references": {
    "crm_link": "",
    "crm_id": "",
    "dropbox_path": ""
  },
  "metadata": {
    "schema_version": "1.0.0",
    "tags": [],
    "created_at": "",
    "updated_at": "",
    "source_file": "",
    "import_batch": "2025-11-22_Sales_Import",
    "data_quality_score": 0,
    "approved": false
  }
}
```

3. [ ] Create `Field_Mapping_QuickRef.md` with common transformations:

```markdown
# Quick Reference - Field Mappings

## Company
- name: `company_name` (clean, title case)
- website: `website` (add https:// if missing)
- size_id: `lead_company_size.id`
- size_label: `lead_company_size.title`

## Industries
- industry_id: `lead_company_industry.id`
- industry_name: `lead_company_industry.title`
- sub_industry_id: `sub_industries[0].id`
- sub_industry_name: `sub_industries[0].name`

## Business Relationship
- entity_type: Classify based on:
  - Has job_requests → Client
  - Notes contain "hired" → Client
  - Notes contain "stopped" → Ex_Client
  - Default → Prospect
- status_id: `lead_status.id`
- status_type: `lead_status.type`
- source_id: `lead_source.id`
- source_name: `lead_source.name`

## POCs
- name: `pocs[].name` OR `name` (contact name)
- email: `pocs[].email` OR `email`
- position_id: `pocs[].position.id`
- position_title: `pocs[].position.title`

## Assigned Users
- sales_manager_id: `sales_manager`
- sales_manager_name: `sales_manager_assistant.name`
- lead_agent_id: `lead_agent.id`
- created_by_id: `created_by.id`
- created_by_name: `created_by.name`

## References
- crm_id: `client_id`
- crm_link: https://crm-s.com/clients/{client_id}
- dropbox_path: ENTITIES/BUSINESSES/{entity_type}/{company_name}/
```

**Completion Criteria:**
- ✓ Templates created and ready to use
- ✓ Quick reference guide available

---

### Task 5.4: Process First 10 Records (Practice Batch)

**Goal:** Practice the workflow with a small batch before scaling up.

**Steps for Each Record:**

1. [ ] **Select Record** (Start with record #1 from sample)

2. [ ] **Review Source Data**
   - Open raw_extracted_data_sample.json
   - Find record by sequence number
   - Read all fields carefully

3. [ ] **Classify Entity Type**
   - Check for job_requests → Client
   - Check notes for keywords (hired, stopped)
   - Default → Prospect
   - Mark in tracker

4. [ ] **Copy Template**
   - Copy Template_Prospect.json
   - Rename: `TEMP_working_record.json`

5. [ ] **Fill Company Section**
   - id: Generate next ID (BUS-2025-001)
   - name: Copy from company_name (clean if needed)
   - website: Copy from website (add https:// if needed)
   - size_id: Copy from lead_company_size.id
   - size_label: Copy from lead_company_size.title
   - note: Copy from notes/description
   - locations: Look up lead_company_city, map to location object
   - industries: Look up lead_company_industry + sub_industries

6. [ ] **Fill POCs Section**
   - If pocs array exists, map each POC
   - If not, create POC from contact name + email fields
   - Generate POC-### IDs sequentially

7. [ ] **Fill Business Relationship**
   - entity_type: Use classification from step 3
   - status_id: From lead_status.id
   - status_type: From lead_status.type
   - source_id: From lead_source.id
   - source_name: From lead_source.name
   - priority: From lead_status.priority

8. [ ] **Fill Assigned Users**
   - Map from created_by, sales_manager, lead_agent fields

9. [ ] **Fill References**
   - crm_id: From client_id
   - crm_link: https://crm-s.com/clients/{client_id}
   - dropbox_path: ENTITIES/BUSINESSES/{entity_type}/{clean_company_name}/

10. [ ] **Fill Metadata**
    - schema_version: "1.0.0"
    - tags: Derive from industry, status, keywords
    - created_at: Current timestamp (ISO 8601)
    - updated_at: Same as created_at
    - source_file: From _source_file field
    - data_quality_score: Estimate 0-100 based on completeness
    - approved: false

11. [ ] **Quality Check**
    - [ ] All required fields filled (company.id, company.name, metadata)
    - [ ] IDs follow format (BUS-2025-###, POC-###)
    - [ ] Dates in ISO 8601 format
    - [ ] Foreign key IDs exist in lookup tables
    - [ ] No null in required fields

12. [ ] **Save Entity**
    - Determine target folder based on entity_type:
      - Client → `BUSINESSES/Clients/`
      - Prospect → `BUSINESSES/Prospects/`
      - Ex_Client → `BUSINESSES/Ex_Clients/`
    - Create company folder: `{entity_type}/{CompanyName}/`
    - Save as: `{CompanyName}_MASTER.json`

13. [ ] **Update Tracker**
    - Mark Status: "Complete"
    - Record Generated_ID: BUS-2025-001
    - Record Entity_Type
    - Add Date_Processed
    - Note any issues

14. [ ] **Repeat for Records 2-10**

**Completion Criteria:**
- ✓ 10 entities created successfully
- ✓ Files saved in correct folders
- ✓ Tracker updated
- ✓ Comfortable with workflow

**Time Estimate:** 30-45 minutes per record initially (will get faster with practice)

---

### Task 5.5: Review Practice Batch

**Goal:** Verify quality before processing remaining records.

**Steps:**

1. [ ] Review all 10 created entities
2. [ ] Check consistency:
   - [ ] ID sequences correct (BUS-2025-001 through BUS-2025-010)
   - [ ] All in correct folders (Clients/Prospects/Ex_Clients)
   - [ ] Schema compliance (all required fields present)
   - [ ] Date formats consistent (ISO 8601)
3. [ ] Verify against source data (spot check 3 records)
4. [ ] Check lookup table references are valid
5. [ ] Document any issues found
6. [ ] Adjust template/process if needed

**Completion Criteria:**
- ✓ All 10 entities pass quality check
- ✓ Process documented and refined
- ✓ Ready to scale to full dataset

---

### Task 5.6: Batch Processing Strategy

**Goal:** Plan how to process remaining 990 records efficiently.

**Recommended Approach:**

**Option A: Daily Batches (Recommended)**
- Process 20-50 records per day
- Review and quality check each batch
- Total time: 20-50 days at steady pace
- Lower error rate, better quality control

**Option B: Weekly Sprints**
- Dedicate focused time blocks
- Process 100-200 records per sprint
- Total time: 5-10 weeks
- Good for dedicated work sessions

**Option C: Prioritized Processing**
1. [ ] First: All Clients (if any found - currently 0)
2. [ ] Second: High-quality Prospects (those with emails + full info)
3. [ ] Third: Standard Prospects
4. [ ] Last: Low-quality records (missing contact info)

**Batch Processing Checklist:**

Per Batch (20-50 records):
1. [ ] Create working folder: `IMPORTS/batch_YYYY-MM-DD/`
2. [ ] Extract records for this batch from raw_extracted_data.json
3. [ ] Process each record using Task 5.4 workflow
4. [ ] Update tracker after each record
5. [ ] Quality check batch when complete
6. [ ] Move completed files to BUSINESSES folders
7. [ ] Document any issues or patterns
8. [ ] Take break before next batch

**Completion Criteria:**
- ✓ Processing strategy selected
- ✓ Schedule planned
- ✓ Ready to begin full import

---

### Task 5.7: Processing Aids & Tools

**Goal:** Create helper tools to speed up repetitive tasks.

**Suggested Helpers:**

1. [ ] **ID Generator Tracker**
   - Keep running count in `IMPORTS/id_counter.txt`:
     ```
     LAST_BUSINESS_ID: BUS-2025-010
     LAST_POC_ID: POC-025
     LAST_COMM_ID: COMM-000
     ```
   - Update after each entity

2. [ ] **Quick Lookup Sheets**
   - Create `IMPORTS/lookup_quick_reference.xlsx`
   - Tabs for each lookup table with ID/Name columns
   - Quick search for validating foreign keys

3. [ ] **Tag Keywords List**
   - Create `IMPORTS/tag_keywords.md`
   - Common tags to apply based on industry/notes
   - Speeds up metadata tagging

4. [ ] **Quality Checklist Template**
   - Printable checklist for each entity
   - Check off required validations
   - Attach to daily processing log

**Completion Criteria:**
- ✓ Helper tools created
- ✓ Workflow streamlined
- ✓ Efficiency improved

---

## Phase 6: Validation & Quality Assurance

### Objective
Validate all created entities against schema and business rules.

**Start When:** All entities created (Task 5 complete)

### Task 6.1: Schema Validation

**Steps:**

1. [ ] Load schema: `BUSINESSES/schemas/BUSINESSES_SCHEMA.json`
2. [ ] For each entity folder:
   - [ ] Load *_MASTER.json file
   - [ ] Manually verify against schema:
     - [ ] Required fields present
     - [ ] Field types correct
     - [ ] ID formats valid
     - [ ] Dates in ISO 8601
3. [ ] Document validation errors in `IMPORTS/validation_errors.log`
4. [ ] Fix errors and re-validate

**Completion Criteria:**
- ✓ 100% schema compliance
- ✓ All validation errors fixed

---

### Task 6.2: Foreign Key Validation

**Steps:**

1. [ ] Create validation spreadsheet: `IMPORTS/fk_validation.xlsx`
2. [ ] Extract all foreign key references:
   - company.size_id → CompanySizes
   - industries[].industry_id → Industries
   - industries[].sub_industry_id → SubIndustries
   - pocs[].position_id → Positions
   - business_relationship.status_id → LeadStatuses
   - business_relationship.source_id → LeadSources
3. [ ] For each FK, verify ID exists in lookup table INDEX
4. [ ] Mark invalid FKs
5. [ ] Fix by either:
   - Correcting ID if typo
   - Adding missing lookup value
   - Setting to null if truly unavailable

**Completion Criteria:**
- ✓ 100% FK integrity
- ✓ All lookups validated

---

### Task 6.3: Duplicate Detection

**Steps:**

1. [ ] Create spreadsheet: `IMPORTS/duplicate_check.xlsx`
2. [ ] List all company names in column A
3. [ ] Sort alphabetically
4. [ ] Visually scan for duplicates
5. [ ] For each duplicate found:
   - [ ] Compare records side-by-side
   - [ ] Determine which is most complete
   - [ ] Merge data if needed
   - [ ] Archive duplicate
   - [ ] Update tracker

**Completion Criteria:**
- ✓ No duplicate companies
- ✓ All duplicates merged or resolved

---

### Task 6.4: Data Quality Review

**Steps:**

1. [ ] Calculate quality scores:
   - [ ] Count entities with quality_score < 50
   - [ ] Count entities with quality_score 50-75
   - [ ] Count entities with quality_score > 75
2. [ ] Review low-quality entities:
   - [ ] Can missing data be found in CRM?
   - [ ] Can data be enriched from LinkedIn/website?
   - [ ] Should entity be kept or archived?
3. [ ] Document quality improvement actions
4. [ ] Update entities with enriched data

**Completion Criteria:**
- ✓ Quality score distribution documented
- ✓ Improvement plan for low-quality records
- ✓ 85%+ of records have quality_score > 50

---

## Phase 7: Organization & Finalization

### Task 7.1: Create Master Index

**Goal:** Create searchable index of all entities.

**Steps:**

1. [ ] Create `BUSINESSES/BUSINESSES_Master_Index.json`
2. [ ] For each entity, include:
   ```json
   {
     "id": "BUS-2025-001",
     "company_name": "AICO Solutions",
     "entity_type": "Prospect",
     "industry": "Finance",
     "country": "Israel",
     "quality_score": 75,
     "file_path": "BUSINESSES/Prospects/AICO_Solutions/AICO_Solutions_MASTER.json",
     "created_at": "2025-11-22T21:00:00Z"
   }
   ```
3. [ ] Sort by company_name
4. [ ] Save with formatting

**Completion Criteria:**
- ✓ Master index created
- ✓ All entities listed
- ✓ Searchable and well-formatted

---

### Task 7.2: Create Summary Report

**Steps:**

1. [ ] Create `IMPORTS/2025-11-22_Sales_Import/FINAL_IMPORT_REPORT.md`
2. [ ] Include statistics:
   - Total records processed
   - Clients / Prospects / Ex_Clients breakdown
   - Average quality score
   - Top industries represented
   - Countries represented
   - Data coverage percentages
3. [ ] Document challenges encountered
4. [ ] List improvements made
5. [ ] Recommendations for future imports

**Completion Criteria:**
- ✓ Comprehensive report created
- ✓ Lessons learned documented

---

### Task 7.3: Archive Import Process

**Steps:**

1. [ ] Create archive folder: `IMPORTS/2025-11-22_Sales_Import/ARCHIVE/`
2. [ ] Move to archive:
   - [ ] raw_extracted_data.json
   - [ ] All phase reports
   - [ ] Processing tracker
   - [ ] Validation logs
   - [ ] Templates
3. [ ] Keep in IMPORTS root:
   - [ ] FINAL_IMPORT_REPORT.md
   - [ ] Processing summary
4. [ ] Update `IMPORTS/README.md` with this import

**Completion Criteria:**
- ✓ Import process archived
- ✓ Documentation complete
- ✓ System ready for next import

---

## Daily Processing Log Template

Copy this for each processing session:

```markdown
# Processing Log - [DATE]

## Session Info
- Date: YYYY-MM-DD
- Start Time: HH:MM
- End Time: HH:MM
- Records Processed: X

## Records Completed
- BUS-2025-XXX: CompanyName (entity_type)
- BUS-2025-XXX: CompanyName (entity_type)
[...]

## Issues Encountered
- Issue 1: Description and resolution
- Issue 2: Description and resolution

## Quality Notes
- Average quality score: XX
- Records needing follow-up: X

## Next Session
- Start with record #XXX
- Focus area: [Clients/Prospects/specific batch]
```

---

## Quick Reference: File Locations

**Source Data:**
- Raw CRM Data: `IMPORTS/2025-11-22_Sales_Import/raw_extracted_data.json`
- Sample Data: `IMPORTS/2025-11-22_Sales_Import/raw_extracted_data_sample.json`

**Schemas & Rules:**
- Main Schema: `BUSINESSES/schemas/BUSINESSES_SCHEMA.json`
- Validation Rules: `BUSINESSES/schemas/validation_rules.json`
- Field Mappings: `IMPORTS/2025-11-22_Sales_Import/mapping_rules.json`
- Transformation Functions: `IMPORTS/2025-11-22_Sales_Import/transformation_functions.json`

**Lookup Tables:**
- All lookups: `BUSINESSES/[TableName]/[TableName]_INDEX.json`

**Target Folders:**
- Clients: `BUSINESSES/Clients/`
- Prospects: `BUSINESSES/Prospects/`
- Ex_Clients: `BUSINESSES/Ex_Clients/`

**Reports:**
- Phase Reports: `IMPORTS/2025-11-22_Sales_Import/phaseX_*.md`

---

## Support & Questions

**If you encounter:**
- **Schema questions:** Review `PLANS/BUSINESSES_Import_Technical_Spec_2025-11-22.md`
- **Field mapping questions:** Check `IMPORTS/mapping_rules.json`
- **Lookup table questions:** Check INDEX files in lookup folders
- **Quality issues:** Document in processing log, review in QA phase

---

**Last Updated:** 2025-11-22
**Version:** 1.0
