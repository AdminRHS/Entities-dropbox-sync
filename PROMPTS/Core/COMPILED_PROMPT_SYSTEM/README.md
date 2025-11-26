# COMPILED PROMPT SYSTEM

**Version:** 1.0
**Generated:** 2025-11-26
**Location:** `ENTITIES/PROMPTS/Core/COMPILED_PROMPT_SYSTEM/`

---

## Overview

This is a comprehensive compilation of **all active prompts** across the entire PROMPTS system, organized by category and purpose. This compilation provides a single, unified reference for all prompt-related operations.

### What This Includes

- **155 Active Prompts** from across all departments
- **12 Categories** of prompts (Video, HR, Workflows, etc.)
- **Complete metadata** for each prompt (IDs, departments, file paths)
- **Core folder prompts** including MAIN_PROMPT versions
- **Detailed statistics** and cross-references

### What Was Excluded

- Core folder files (included separately)
- Deprecated prompts (archived separately)
- Draft prompts
- Documentation files (README, INDEX, SUMMARY)
- Template files

---

## File Structure

```
COMPILED_PROMPT_SYSTEM/
├── README.md                    # This file
├── 00_MASTER_INDEX.md          # Master index with all categories
├── 01_FULL_COMPILATION.md      # All prompts in single document
├── 02_STATISTICS.md            # Detailed statistics
├── CORE.md                     # Core system prompts (4 prompts)
├── VIDEO.md                    # Video processing prompts (14 prompts)
├── HR.md                       # Human resources prompts (14 prompts)
├── DAILY_REPORTS.md            # Daily report prompts (27 prompts)
├── TAXONOMY.md                 # Taxonomy & system prompts (40 prompts)
├── WORKFLOWS.md                # Workflow prompts (14 prompts)
├── AUTOMATION.md               # Automation prompts (2 prompts)
├── RESEARCH.md                 # Research prompts (7 prompts)
├── LIBRARIES.md                # Library processing prompts (3 prompts)
├── CREATIVES.md                # Creative & design prompts (7 prompts)
├── UTILITIES.md                # Utility prompts (8 prompts)
└── OTHER.md                    # Uncategorized prompts (15 prompts)
```

---

## Quick Start

### 1. Find a Prompt by Category
Open the relevant category file (e.g., `VIDEO.md` for video processing prompts)

### 2. Browse All Prompts
Open `01_FULL_COMPILATION.md` for complete listing

### 3. Search by ID
Use `00_MASTER_INDEX.md` to locate specific PRM or PMT IDs

### 4. View Statistics
Check `02_STATISTICS.md` for metrics and distributions

---

## Categories Breakdown

| Category | Prompts | Description |
|----------|---------|-------------|
| **Core System** | 4 | Main system prompts (v4, v5, v6) |
| **Taxonomy & System** | 40 | System architecture, data architecture, taxonomy |
| **Daily Reports** | 27 | Department daily reports and collection |
| **Video Processing** | 14 | Video transcription, analysis, naming |
| **Human Resources** | 14 | CV parsing, CRM, interviews, job sites |
| **Workflows** | 14 | Call organizer, project documentation, account management |
| **Utilities** | 8 | Daily updates, entity identification |
| **Creative & Design** | 7 | Brochure design, social media, mascot scenarios |
| **Research** | 7 | YouTube research, department research |
| **Library Processing** | 3 | Tools, products, task manager integration |
| **Automation** | 2 | Weekly planning, script automation |
| **Other** | 15 | Miscellaneous prompts |

---

## Department Coverage

| Department | Prompts | Percentage |
|------------|---------|------------|
| **AID** (AI & Automation) | 116 | 74.8% |
| **HRM** (Human Resources) | 14 | 9.0% |
| **VID** (Video) | 8 | 5.2% |
| **OPS** (Operations) | 5 | 3.2% |
| **LGN** (Lead Generation) | 4 | 2.6% |
| **DGN** (Design) | 3 | 1.9% |
| **SLS** (Sales) | 2 | 1.3% |
| **DEV** (Development) | 2 | 1.3% |
| **MKT** (Marketing) | 1 | 0.6% |

---

## How to Use This System

### For Finding Specific Prompts

1. **By Name**: Search `00_MASTER_INDEX.md`
2. **By Category**: Open the category document
3. **By PMT Number**: Check `02_STATISTICS.md` for PMT range
4. **By Department**: Use department filter in index

### For Understanding the System

1. Read `02_STATISTICS.md` for overview
2. Browse `01_FULL_COMPILATION.md` for complete picture
3. Check category documents for specific areas

### For Integration

1. Reference prompts by PRM ID (e.g., PRM-066)
2. Use file paths for direct access
3. Check Current_ID for legacy PMT references

---

## Key Statistics

- **Total Prompts in System:** 179
- **Active Prompts:** 155 (86.6%)
- **Deprecated Prompts:** 23 (12.8%)
- **Draft Prompts:** 1 (0.6%)
- **PMT-Numbered Prompts:** 92
- **Categories:** 12
- **Departments Served:** 9

---

## Core Prompts Included

This compilation includes the Core folder prompts:

1. **PRM-036**: Main Prompt v4 (Current Production)
2. **PRM-037**: Main Prompt v5 (Modular Architecture)
3. **PRM-039**: Create Main Prompt v5 (Documentation)
4. **PRM-040**: Reverse Prompt Engineering Analysis

---

## ID System

### PRM IDs (New System)
- Range: PRM-001 to PRM-179
- Format: Sequential numbering
- Used for all prompts in master list

### PMT IDs (Legacy System)
- Range: PMT-001 to PMT-092
- Format: Prompt file naming
- Mapped to PRM IDs in Current_ID field

### Legacy IDs (Original System)
- Format: PRM-VT-001, PRM-HR-001, etc.
- Department-specific codes
- Retained in Current_ID for reference

---

## Regeneration

To regenerate this compilation after updates:

```bash
cd C:\Users\Dell\Dropbox\ENTITIES\PROMPTS
python compile_prompt_system.py
```

The script will:
1. Read the latest PROMPTS_Master_List.csv
2. Categorize all active prompts
3. Generate all documentation files
4. Update statistics

---

## Version History

### Version 1.0 (2025-11-26)
- Initial compilation
- 155 active prompts
- 12 categories
- Complete Core folder integration

---

## Related Files

- **Source:** `ENTITIES/PROMPTS/PROMPTS_Master_List.csv`
- **Generator:** `ENTITIES/PROMPTS/compile_prompt_system.py`
- **Core Folder:** `ENTITIES/PROMPTS/Core/`
- **Full System:** `ENTITIES/PROMPTS/`

---

## Notes

- This compilation is **read-only** - do not edit manually
- To add prompts, update the source files and regenerate
- Core folder prompts are included in this compilation
- Deprecated prompts are documented but not included in active compilation
- All file paths are relative to `ENTITIES/`

---

**Last Updated:** 2025-11-26 01:41
**Compiled By:** compile_prompt_system.py v1.0
