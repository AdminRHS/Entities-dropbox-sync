# Phase 4: Data Extraction Report

**Executed:** 2025-11-22T21:10:57.691863
**Status:** Completed

## Summary

- **Total Records Extracted:** 1000
- **Source Files:** 100 CRM cluster files
- **Data Source:** CRM Export (Client_JSON_Clusters)

## Data Coverage Analysis

| Field | Records | Coverage |
|-------|---------|----------|
| has_company_name | 1000 | 100.0% |
| has_contact_name | 1000 | 100.0% |
| has_email | 709 | 70.9% |
| has_pocs | 0 | 0.0% |
| has_industry | 1000 | 100.0% |
| has_location | 0 | 0.0% |
| has_lead_status | 999 | 99.9% |
| has_communications | 0 | 0.0% |

## Entity Type Estimates

- **Potential Clients:** 0
- **Potential Prospects:** 1000
- **Has Job Requests:** 0

## Unique Values

- **Unique Companies:** 1000
- **Unique Emails:** 708
- **Unique CRM IDs:** 1000
- **Unique Industries:** 117
- **Unique Countries:** 0
- **Unique Lead Statuses:** 7

## Duplicate Detection

- **Duplicate Company Names:** 0
- **Duplicate Emails:** 1
- **Duplicate CRM IDs:** 0

## Files Generated

- `raw_extracted_data.json` - Full dataset (1000 records)
- `raw_extracted_data_sample.json` - Sample dataset (10 records)
- `processing_registry.json` - Record tracking registry

## Next Step

Proceed to **Phase 5: Metadata Tagging**
