# Actions Library (Rebuilt)

This directory is auto-generated from `../actions.json`.
Each record merges the base verb with its continuous process form and past-result form so teams can map responsibilities, processes, and results without ambiguity.

File inventory:
- `Actions_Master.json` – canonical list of actions with process/result variations, departments, and professions sourced from the original spreadsheet.
- `Data_Operations/` – **NEW** subdirectory containing individual action files for specialized data operations (scraping, parsing, enrichment workflows)

## Data Operations Actions (2025-11-12)

A new category of 12 actions has been added to support lead generation and data processing workflows identified in Video_006 analysis:

**Location:** `Data_Operations/`

**Actions:**
- scrape, parse, feed, sanitize, split, combine, lookup, flatten, obfuscate, bill, consume, arbitrage

**Index File:** `Data_Operations/Data_Operations_Actions_Index.json` - Contains metadata and references to all 12 individual action files

**Structure:** Each action has its own JSON file with enhanced metadata:
- Typical use cases
- Common objects/tools
- Related actions
- Workflow examples
- Success metrics

**Integration:** These actions extend the existing actions.json with specialized terminology from Video_006 lead generation workflows. They are maintained as individual files for easier management and can be merged into the main actions file if needed.

To regenerate: run the helper script (see repository instructions) that reads `actions.json`, normalizes spacing/case, and rewrites the master file.***
