# Changelog

## 2025-11-26
- Added Phase 0 data listings plan with actionable steps and code snippets (`ARCHITECTURE_PLAN/DATA_LISTINGS.md`).
- Implemented CSV normalizer script for researches/video/search queues with reporting to Architecture README (`DATA/scripts/normalize_csv_phase0.py`).
- Updated normalizer to write outputs into `DEV/05_NEXT_DEVELOPMENT/_normalized` and log inventory runs in Architecture README.
- Added JSON normalizer (`DEV/05_NEXT_DEVELOPMENT/scripts/normalize_json_phase0.py`) for tool_mapping/discovered_tools with conflict logging and structured outputs.
- Redirected normalization reports to `DEV/05_NEXT_DEVELOPMENT/reports/{csv_normalization_report,json_normalization_report}.md` and initialized report files.
- Added Markdown inventory script (`DEV/05_NEXT_DEVELOPMENT/scripts/md_inventory.py`) to produce `md_listing.{csv,json}` and log to `reports/md_inventory_report.md`.
- Generated initial Markdown listings (`md_listing.csv`, `md_listing.json`) from DATA/** for Phase 0 ETL inputs.
- Added aggregation script (`DEV/05_NEXT_DEVELOPMENT/scripts/aggregate_data_listings.py`) and generated combined vitrines:
  - `ARCHITECTURE_PLAN/data_listing_structured.json` (CSV/JSON sources)
  - `ARCHITECTURE_PLAN/data_listing_markdown.json` (Markdown corpus)
- Added full inventory runner (`DEV/05_NEXT_DEVELOPMENT/scripts/run_inventory.py`) that chains normalization + aggregation, writes `ARCHITECTURE_PLAN/reports/inventory_run.md`, and appends summary to README.
- Added Phase 0 ID/status rules reference (`DATA/id_and_status_rules.md`) and linked from PHASE_0.MD.
- Added test checklist and artifacts under `DEV/05_NEXT_DEVELOPMENT/test`:
  - `PHASE0_TO_TABLES_CHECKLIST.md` (step-by-step Phase0→tables)
  - `schema.sql` (DDL for PostgreSQL target tables)
  - `load_to_db.py` (psycopg2 loader for test vitrines)
  - Test copies of vitrines (`test/data_listing_structured.json`, `test/data_listing_markdown.json`)
