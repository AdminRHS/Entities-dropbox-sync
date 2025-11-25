# ENTITIES Import Prompts - Master Guide

**Last Updated:** 2025-11-21
**Status:** Production Ready

---

## Overview

This directory contains reusable prompt templates for importing data from various sources into the ENTITIES system. All templates follow a proven multi-phase methodology that ensures data quality, completeness, and comprehensive documentation.

---

## Available Prompts

### 1. BUSINESSES Entity Import
**File:** [BUSINESSES_IMPORT_PROMPT.md](BUSINESSES_IMPORT_PROMPT.md)

**Use Case:** Import client/prospect/ex-client data from Sales department

**Source Data:**
- Primary: `Sales Nov25\client_list.md`
- Archives: `Sales_Oct25\`, `Sales_Sep25\`, etc.

**Proven Results:**
- ✅ 40 entities imported
- ✅ 91.9% data quality
- ✅ 100% coverage (all archives reviewed)
- ✅ Complete documentation

**When to Use:**
- New Sales CRM exports
- Quarterly client list updates
- Archive consolidation
- Client database migration

---

### 2. Department-Specific Templates
**File:** [DEPARTMENT_IMPORT_TEMPLATE.md](DEPARTMENT_IMPORT_TEMPLATE.md)

**Departments Covered:**
- 📊 **Sales** - BUSINESSES entities (clients, prospects)
- 👥 **HR** - TALENTS entities (employees, contractors)
- 📝 **Content** - CONTENT entities (articles, assets)
- 🎨 **Design** - DESIGN entities (projects, deliverables)
- 💻 **Development** - DEVELOPMENT entities (code projects)
- 🎯 **Lead Generation** - LEADS entities (campaigns, conversions)
- 💰 **Finance** - FINANCE entities (invoices, revenue)
- 📱 **Social Media** - SMM entities (campaigns, posts)
- 🤖 **AI/Automation** - AI_TOOLS entities (tools, workflows)

**When to Use:**
- Department-specific data imports
- New entity type creation
- Cross-department integration

---

### 3. Multi-Phase Import Template
**File:** [MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md](../IMPORTS/MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md)

**Location:** `ENTITIES\IMPORTS\`

**Use Case:** Generic reusable template for any entity type

**Features:**
- Complete phase-by-phase instructions
- Data transformation standards
- Quality metrics and success criteria
- Common issues and solutions
- Example Python script structures

**When to Use:**
- Creating custom entity imports
- Learning the import methodology
- Troubleshooting existing imports

---

## Quick Start Guide

### For a BUSINESSES Import

1. **Review the source data**
   - Locate client list file (CSV, MD, XLSX, etc.)
   - Identify supporting documents (transcripts, emails)
   - Check archive directories

2. **Use the prompt**
   ```
   Copy the BUSINESSES_IMPORT_PROMPT.md content
   Customize the SOURCE and CONTEXT paths
   Submit to Claude Code
   ```

3. **Run the generated scripts**
   ```bash
   python phase1_validation.py
   python phase2_entity_extraction.py
   python phase3_data_enrichment.py
   python phase4_json_generation.py
   python phase5_supplement_oct25.py  # if archives exist
   ```

4. **Review the output**
   - Check validation reports
   - Verify JSON files created
   - Review statistics dashboard
   - Read final import summary

---

### For Other Departments

1. **Select the appropriate template**
   - Open `DEPARTMENT_IMPORT_TEMPLATE.md`
   - Find your department section

2. **Customize the prompt**
   - Update SOURCE path
   - Adjust entity ID prefix
   - Define department-specific rules

3. **Run the import**
   - Follow multi-phase approach
   - Generate documentation
   - Create cross-references

---

## Import Methodology

All imports follow this proven 5-8 phase approach:

### Core Phases (Always Required)

**Phase 1: Validation & Preparation**
- Validate source data quality
- Identify data issues and gaps
- Create staging environment
- Generate validation report

**Phase 2: Entity Extraction & Categorization**
- Parse source data into structured format
- Categorize entities by type/status
- Generate unique IDs
- Transform dates and formats
- Calculate derived fields

**Phase 3: Data Enrichment**
- Match entities to supporting documents
- Extract additional context
- Build communication history
- Enhance entity records

**Phase 4: JSON File Generation**
- Create directory structure
- Generate individual JSON files
- Create index files per category
- Generate master catalog with statistics

### Optional Phases (As Needed)

**Phase 5: Archive Review**
- Check historical data directories
- Identify additional entities
- Cross-reference to avoid duplicates
- Add supplementary entities

**Phase 6: Relationship Mapping**
- Map cross-entity relationships
- Link to other entity types
- Identify dependencies

**Phase 7: Validation & QA**
- Schema compliance checks
- Data integrity validation
- Cross-reference verification

**Phase 8: Documentation**
- Final import summary
- Statistics dashboard
- User guide
- Reusable templates

---

## File Naming Standards

### Entity Files
```
Pattern: [ENTITY_TYPE]_[SubEntity]_[Name]_[ID].json

Examples:
- BUSINESSES_Client_Acme_Corp_BUS-2025-001.json
- TALENTS_Employee_John_Doe_TAL-2025-042.json
- CONTENT_BlogPost_AI_Guide_CON-2025-015.json
```

### Index Files
```
Pattern: [SubEntity]_INDEX.json

Examples:
- Clients_INDEX.json
- Employees_INDEX.json
- BlogPosts_INDEX.json
```

### Master Catalogs
```
Pattern: [ENTITY_TYPE]_Master.json

Examples:
- BUSINESSES_Master.json
- TALENTS_Master.json
- CONTENT_Master.json
```

---

## ID Prefixes by Entity Type

| Entity Type | Prefix | Example | Department |
|-------------|--------|---------|------------|
| BUSINESSES | BUS-YYYY-XXX | BUS-2025-001 | Sales |
| TALENTS | TAL-YYYY-XXX | TAL-2025-042 | HR |
| CONTENT | CON-YYYY-XXX | CON-2025-015 | Content |
| DESIGN | DES-YYYY-XXX | DES-2025-008 | Design |
| DEVELOPMENT | DEV-YYYY-XXX | DEV-2025-023 | Dev |
| LEADS | LED-YYYY-XXX | LED-2025-101 | Lead Gen |
| FINANCE | FIN-YYYY-XXX | FIN-2025-500 | Finance |
| SMM | SMM-YYYY-XXX | SMM-2025-050 | Social Media |
| AI_TOOLS | AIT-YYYY-XXX | AIT-2025-012 | AI/Auto |
| PRODUCTS | PRO-YYYY-XXX | PRO-2025-025 | Multiple |
| SERVICES | SVC-YYYY-XXX | SVC-2025-018 | Multiple |

---

## Directory Structure Standard

```
ENTITIES/
├── [ENTITY_TYPE]/
│   ├── [SubEntity_1]/
│   │   ├── [SubEntity_1]_INDEX.json
│   │   └── [ENTITY]_[SubEntity]_[Name]_[ID].json (multiple)
│   ├── [SubEntity_2]/
│   │   ├── [SubEntity_2]_INDEX.json
│   │   └── [ENTITY]_[SubEntity]_[Name]_[ID].json (multiple)
│   └── [ENTITY_TYPE]_Master.json
│
├── IMPORTS/
│   └── YYYY-MM-DD_[SourceName]/
│       ├── phase1_validation.py
│       ├── phase2_entity_extraction.py
│       ├── phase3_data_enrichment.py
│       ├── phase4_json_generation.py
│       ├── validation_report.md
│       ├── categorization_report.md
│       ├── enrichment_report.md
│       ├── FINAL_IMPORT_SUMMARY.md
│       └── STATISTICS_DASHBOARD.md
│
└── PROMPTS/
    ├── README_PROMPTS.md (this file)
    ├── BUSINESSES_IMPORT_PROMPT.md
    ├── DEPARTMENT_IMPORT_TEMPLATE.md
    └── MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md
```

---

## Success Metrics

### Data Quality Targets

| Metric | Excellent | Good | Acceptable | Poor |
|--------|-----------|------|------------|------|
| Source Data Quality | >95% | 90-95% | 85-90% | <85% |
| Entity Coverage | 100% | 100% | >95% | <95% |
| Schema Compliance | 100% | 100% | 100% | <100% |
| Field Completeness | >90% | 80-90% | 75-80% | <75% |
| Enrichment Rate | >30% | 20-30% | 10-20% | <10% |
| Tag Coverage | 100% | >95% | >90% | <90% |

### BUSINESSES Import Results (Nov 2025)

- Source Data Quality: **91.9%** ✅ Good
- Entity Coverage: **100%** ✅ Excellent
- Schema Compliance: **100%** ✅ Excellent
- Field Completeness: **78.6%** ✅ Acceptable
- Enrichment Rate: **10.8%** ⚠️ Acceptable
- Tag Coverage: **100%** ✅ Excellent

---

## Common Use Cases

### Use Case 1: Monthly Sales Update
**Scenario:** Import new clients from monthly CRM export

**Steps:**
1. Export client list from CRM
2. Save to `Sales Nov25\` or appropriate month
3. Run BUSINESSES import prompt
4. Starting ID: Check BUSINESSES_Master.json for next available
5. Review archives for cross-references
6. Generate supplementary import if needed

**Expected Time:** 2-3 hours (mostly automated)

---

### Use Case 2: Quarterly HR Roster Update
**Scenario:** Import employee changes from quarterly HR review

**Steps:**
1. Get employee roster from HR system
2. Save to `HR Nov25\` or appropriate quarter
3. Customize TALENTS import prompt from template
4. Check for new hires, terminations, status changes
5. Update cross-references to BUSINESSES (client assignments)

**Expected Time:** 3-4 hours

---

### Use Case 3: Annual Data Consolidation
**Scenario:** Consolidate all department data for year-end

**Steps:**
1. For each department, run appropriate import
2. Use department-specific prompts
3. Generate cross-entity relationship mappings
4. Create master analytics dashboard
5. Archive all source data with documentation

**Expected Time:** 1-2 days (for all departments)

---

### Use Case 4: New Entity Type Creation
**Scenario:** Create import for a new entity type (e.g., VENDORS)

**Steps:**
1. Copy MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md
2. Define entity ID prefix (VND-YYYY-XXX)
3. Create JSON schema for new entity
4. Define categorization rules
5. Customize department template
6. Run import following multi-phase approach

**Expected Time:** 4-6 hours (first time), 2-3 hours (subsequent)

---

## Best Practices

### Before Import
- ✅ Back up source data
- ✅ Review existing entities to check next ID
- ✅ Identify all source files and archives
- ✅ Document expected entity count
- ✅ Prepare validation criteria

### During Import
- ✅ Run phases sequentially
- ✅ Review each phase's output before continuing
- ✅ Document any issues or anomalies
- ✅ Validate IDs don't duplicate
- ✅ Cross-reference archive directories

### After Import
- ✅ Verify file counts match expectations
- ✅ Check schema compliance
- ✅ Review statistics dashboard
- ✅ Update master catalog
- ✅ Create backup of imported data
- ✅ Document lessons learned

---

## Troubleshooting

### Issue: Low Data Quality (<85%)
**Solution:**
- Review source data format
- Check for missing required fields
- Identify data entry errors
- Document exceptions in validation report

### Issue: Duplicate Entities
**Solution:**
- Check company_id uniqueness
- Review CRM links for true duplicates
- Use archive cross-reference
- Merge records if truly duplicate

### Issue: Low Enrichment Rate (<10%)
**Solution:**
- Improve transcript matching logic
- Use fuzzy matching for company names
- Manual review of unmatched documents
- Check file path accuracy

### Issue: Missing Cross-References
**Solution:**
- Run relationship mapping phase
- Validate entity IDs exist
- Update index files
- Regenerate master catalog

---

## Support & Resources

### Documentation Hierarchy

1. **This README** - Start here for overview
2. **Department Templates** - For specific imports
3. **Multi-Phase Template** - For deep dive
4. **Import Summaries** - For examples (see IMPORTS/YYYY-MM-DD_*/FINAL_IMPORT_SUMMARY.md)

### Example Imports

**BUSINESSES (Nov 2025):**
- Location: `ENTITIES/IMPORTS/2025-11-21_Sales_Nov25/`
- Files: All Python scripts, reports, summaries
- Result: 40 entities, 53 JSON files, complete documentation

### Getting Help

1. Review relevant prompt template
2. Check FINAL_IMPORT_SUMMARY.md examples
3. Consult MULTI_PHASE_IMPORT_PROMPT_TEMPLATE.md
4. Reference Python scripts from successful imports

---

## Future Enhancements

### Planned Features
- Automated cross-entity relationship detection
- Enhanced enrichment from multiple sources
- Real-time validation during import
- Incremental import support (delta updates)
- API-based imports from external systems

### Template Updates
- Add more department-specific examples
- Include industry-specific variations
- Provide multi-source consolidation templates
- Create migration templates (system-to-system)

---

**README Version:** 1.0
**Last Updated:** 2025-11-21
**Maintained By:** Multi-Phase Import System
**Status:** ✅ Production Ready

---

## Quick Reference

### Essential Commands

**Start a new import:**
```
Use BUSINESSES_IMPORT_PROMPT.md or DEPARTMENT_IMPORT_TEMPLATE.md
Customize SOURCE and CONTEXT paths
Submit to Claude Code
```

**Check next available ID:**
```
Open [ENTITY_TYPE]_Master.json
Review entities_by_id section
Next ID = highest + 1
```

**Run import phases:**
```bash
python phase1_validation.py
python phase2_entity_extraction.py
python phase3_data_enrichment.py
python phase4_json_generation.py
```

**Verify results:**
```
Review: validation_report.md
Review: categorization_report.md
Review: FINAL_IMPORT_SUMMARY.md
Check: STATISTICS_DASHBOARD.md
```

---

**Ready to import? Choose a prompt template and get started!** 🚀
