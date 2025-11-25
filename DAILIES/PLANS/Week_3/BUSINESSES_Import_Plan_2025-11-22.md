# BUSINESSES Entity Import Plan
**Created:** 2025-11-22
**Status:** Pending Approval
**Source:** Dropbox\Nov25\Sales Nov25
**Target:** Dropbox\ENTITIES\BUSINESSES

---

## Executive Summary

This plan defines a 10-phase automated import system for the BUSINESSES entity. Each phase is a standalone Python script that produces output consumed by subsequent phases. All scripts require manual approval before execution.

---

## Phase Overview

| Phase | Script | Purpose | Inputs | Outputs |
|-------|--------|---------|--------|---------|
| 0 | phase0_cleanup.py | Archive existing data & reset | BUSINESSES/* | archive_2025-11-21/* |
| 1 | phase1_schema_definition.py | Define JSON schema & validation rules | Research | schemas/*.json |
| 2 | phase2_data_mapping.py | Map source columns to schema fields | client_list.md | mapping_rules.json |
| 3 | phase3_data_extraction.py | Extract data from all sources | Multiple sources | raw_extracted_data.json |
| 4 | phase4_data_enrichment.py | Enrich with services, budget, urgency | Extracted data + transcripts | enriched_data.json |
| 5 | phase5_categorization.py | Categorize as Client/Prospect/Ex_Client | Enriched data | categorized_entities.json |
| 6 | phase6_id_generation.py | Deduplicate & generate unique IDs | Categorized data | deduplicated_entities.json |
| 7 | phase7_json_generation.py | Generate individual JSON files | Deduplicated data | BUSINESSES/*.json |
| 8 | phase8_validation.py | Validate against schema & quality checks | Generated files | validation_report.md |
| 9 | phase9_documentation.py | Generate docs & reusable prompts | All outputs | USER_GUIDE, PROMPTS |

---

## Data Flow Diagram

```
[Source Data]
     |
     v
+------------------+
| Phase 0: Cleanup |  --> Archive existing files
+------------------+
     |
     v
+------------------------+
| Phase 1: Schema Define |  --> BUSINESSES_SCHEMA.json
+------------------------+
     |
     v
+------------------------+
| Phase 2: Data Mapping  |  --> mapping_rules.json
+------------------------+
     |
     v
+-------------------------+
| Phase 3: Data Extract   |  --> raw_extracted_data.json
+-------------------------+
     |
     v
+-------------------------+
| Phase 4: Data Enrich    |  --> enriched_data.json
+-------------------------+
     |
     v
+---------------------------+
| Phase 5: Categorization   |  --> categorized_entities.json
+---------------------------+
     |
     v
+--------------------------+
| Phase 6: ID Generation   |  --> deduplicated_entities.json
+--------------------------+
     |
     v
+--------------------------+
| Phase 7: JSON Generation |  --> Individual .json files
+--------------------------+
     |
     v
+------------------------+
| Phase 8: Validation    |  --> validation_report.md
+------------------------+
     |
     v
+------------------------+
| Phase 9: Documentation |  --> USER_GUIDE, PROMPTS
+------------------------+
```

---

## Data Sources

### Primary Source
- **client_list.md** - Nov 2025 client records (40+ records, 15 columns)

### Secondary Sources
- **Sales_Oct25/Clients/** - October 2025 client folders (30+ folders)
- **Sales Sep25/** - September 2025 transcripts (19+ files)
- **Sales Aug25/** - August 2025 transcripts (18+ files)
- **Sales Jul25/** - July 2025 transcripts (12+ files)

### Enrichment Sources
- **first call transcripts/** - 15+ call transcriptions with client needs
- **client_deepresearch/** - 8+ deep research files
- **Email templates/** - Pre-call and follow-up templates

---

## Expected Outputs

### Entity Files
- **Estimated Total:** 50-60+ unique entities
- **Clients:** ~5-8 (companies that hired)
- **Prospects:** ~40-50 (active outreach)
- **Ex_Clients:** ~2-5 (former clients)

### Schema & Documentation
- BUSINESSES_SCHEMA.json - Formal JSON schema
- field_definitions.md - Human-readable field docs
- validation_rules.json - Data validation specs

### Reports
- extraction_report.md
- enrichment_report.md
- categorization_report.md
- duplicate_report.md
- validation_report.md
- FINAL_IMPORT_SUMMARY.md

### Quality Metrics
- **Target Completeness:** 95%+
- **Target Accuracy:** 98%+
- **Schema Compliance:** 100%

---

## Execution Instructions

1. Review this plan and the Technical Specification document
2. Approve or request changes
3. Each phase script will be created and shown for approval
4. After approval, script will be executed
5. Review outputs before proceeding to next phase

---

## Key Improvements Over Previous Import

1. **Schema-First Approach** - Define structure before importing
2. **Multi-Source Consolidation** - All months (Jul-Nov) in one import
3. **Deduplication** - Merge records from overlapping sources
4. **Better Enrichment** - Parse transcripts for detailed client needs
5. **Formal Validation** - Schema-based validation with quality metrics
6. **Manual Approval Gates** - Control at each phase

---

## File Locations

**Scripts:** `C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-22_Sales_Import\`
**Output:** `C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES\`
**Reports:** `C:\Users\Dell\Dropbox\ENTITIES\IMPORTS\2025-11-22_Sales_Import\`
**Schemas:** `C:\Users\Dell\Dropbox\ENTITIES\BUSINESSES\schemas\`

---

## Next Step

Review the companion document:
**BUSINESSES_Import_Technical_Spec_2025-11-22.md**

This contains detailed specifications for each phase including:
- Exact field mappings
- Transformation rules
- Categorization logic
- Validation criteria
- Error handling
