# ENTITIES Import Registry

This folder tracks all data imports into the ENTITIES system. Each import has its own subfolder with complete documentation and processing artifacts.

---

## Active Imports

### 2025-11-22_Sales_Import (BUSINESSES)
- **Status:** Phase 5 - Manual Entity Creation (IN PROGRESS)
- **Entity:** BUSINESSES
- **Source:** Nov25/Sales Nov25 + CRM Export (Client_JSON_Clusters)
- **Records:** 1000 CRM records
- **Approach:** Manual processing with guided task manager
- **Started:** 2025-11-22
- **Task Manager:** `TASK_MANAGERS/BUSINESSES_Import_TaskManager.md`
- **Progress:**
  - ✅ Phase 0: Cleanup & Archive
  - ✅ Phase 1: Schema Definition
  - ✅ Phase 2: Lookup Tables (285 files)
  - ✅ Phase 3: Field Mapping
  - ✅ Phase 4: Data Extraction (1000 records)
  - 🔄 Phase 5: Manual Entity Creation (0/1000 complete)
  - ⏳ Phase 6: Validation & QA
  - ⏳ Phase 7: Organization & Finalization

---

## Import Folder Structure

Each import folder contains:

```
YYYY-MM-DD_ImportName/
├── README.md                          # Import overview
├── raw_extracted_data.json            # Source data (read-only)
├── raw_extracted_data_sample.json     # Sample records
├── processing_registry.json           # Record tracking
├── processing_tracker.xlsx            # Manual progress tracking
├── mapping_rules.json                 # Field mappings
├── transformation_functions.json      # Transformation specs
├── validation_rules.json              # Validation criteria
├── phase0_*.md                        # Phase reports
├── phase1_*.md
├── phase2_*.md
├── phase3_*.md
├── phase4_*.md
├── Templates/                         # Entity templates
│   ├── Template_Prospect.json
│   ├── Template_Client.json
│   └── Field_Mapping_QuickRef.md
├── Batches/                           # Daily processing batches
│   ├── batch_2025-11-23/
│   ├── batch_2025-11-24/
│   └── ...
├── Logs/                              # Processing logs
│   ├── log_2025-11-23.md
│   └── ...
├── checkpoints/                       # Rollback checkpoints
│   ├── phase_0/
│   ├── phase_1/
│   └── ...
└── ARCHIVE/                           # Archived after completion
    └── [old processing files]
```

---

## Import Workflow

### 1. Planning Phase
- [ ] Identify data source
- [ ] Define target entity structure
- [ ] Create import folder: `YYYY-MM-DD_EntityName_Import/`
- [ ] Create task manager in `TASK_MANAGERS/`
- [ ] Document schema and field mappings

### 2. Preparation Phase
- [ ] Clean up target entity folders (archive if needed)
- [ ] Create/update lookup tables
- [ ] Define validation rules
- [ ] Extract source data (read-only)
- [ ] Create templates

### 3. Processing Phase
- [ ] Manual or automated entity creation
- [ ] Update processing tracker
- [ ] Daily quality checks
- [ ] Batch processing with checkpoints

### 4. Validation Phase
- [ ] Schema compliance check
- [ ] Foreign key validation
- [ ] Duplicate detection
- [ ] Data quality review

### 5. Finalization Phase
- [ ] Create master index
- [ ] Generate final report
- [ ] Archive import artifacts
- [ ] Update this README

---

## Import Guidelines

### Manual Processing (Recommended for <2000 records)
✅ **Advantages:**
- Higher accuracy and quality control
- Better understanding of data patterns
- Immediate issue identification
- Flexible handling of edge cases
- Learning opportunity

📋 **Best Practices:**
- Process in small batches (20-50 records/day)
- Use templates for consistency
- Track progress in spreadsheet
- Take breaks to maintain quality
- Review each batch before continuing
- Document issues and solutions

### Automated Processing (For >2000 records)
✅ **Advantages:**
- Faster for large datasets
- Consistent transformations
- Repeatable process

⚠️ **Considerations:**
- Requires thorough testing
- Less flexible for exceptions
- Needs quality validation afterward

---

## Quality Standards

All imports must meet:
- ✓ 100% schema compliance
- ✓ 100% foreign key integrity
- ✓ 100% unique IDs
- ✓ 85%+ data completeness
- ✓ ISO 8601 date format
- ✓ 0 duplicate entities

---

## Past Imports

### [Template - Copy for each completed import]

#### YYYY-MM-DD_EntityName_Import
- **Entity:** ENTITY_NAME
- **Source:** Source description
- **Records Processed:** XXX
- **Approach:** Manual/Automated
- **Duration:** X days/weeks
- **Final Quality Score:** XX%
- **Lessons Learned:** Key insights
- **Status:** ✅ COMPLETED on YYYY-MM-DD

---

## Task Manager Location

All import task managers are stored in:
`C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\`

Current task managers:
- `BUSINESSES_Import_TaskManager.md` - BUSINESSES entity import

---

## Support Files

**Global Resources:**
- Entity Plans: `ENTITIES/PLANS/`
- Schemas: `ENTITIES/{ENTITY}/schemas/`
- Lookup Tables: `ENTITIES/{ENTITY}/{LookupTable}/`

**Import-Specific:**
- Each import folder contains its own documentation
- Phase reports document each step
- Processing logs track daily progress

---

**Last Updated:** 2025-11-22
**Active Imports:** 1 (BUSINESSES)
**Completed Imports:** 0
