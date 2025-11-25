# Schema Validation Report

**Report ID:** REP-003
**Generated:** 2025-11-17
**Version:** 1.0
**Project:** PROJ-001 - ENTITIES Analysis
**Milestone:** M02 - Schema & Naming Validation

---

## Executive Summary

This report documents schema validation results across the ENTITIES ecosystem. Out of 1,245 files analyzed, **138 schema violations** were identified across Project, Task, and Step templates. While naming conventions achieved 100% compliance, critical gaps exist in required field coverage.

### Key Findings

- **Total Violations:** 138
- **Critical (Missing Required Fields):** 97 (70.3%)
- **Medium (Missing Recommended Fields):** 41 (29.7%)
- **Files Affected:** 101 unique files
- **Template Types:** Project Templates, Task Templates, Step Templates

---

## Violation Breakdown by Severity

### Critical Violations (97)

Missing required fields that prevent proper template functionality:

| Entity Type | Count | Primary Issue |
|-------------|-------|---------------|
| Step Templates | 59 | Missing `step_template_id` and `step_template_name` |
| Task Templates | 34 | Missing `task_template_id` and `task_template_name` |
| Project Templates | 4 | Missing `project_template_id` and `template_name` |

### Medium Violations (41)

Missing recommended fields that reduce template usability:

| Entity Type | Count | Primary Issue |
|-------------|-------|---------------|
| Task Templates | 34 | Missing `category` field |
| Project Templates | 4 | Missing `milestone_templates` array |
| Task Templates | 3 | Missing `description`, `department` fields |

---

## Detailed Violation Analysis

### Project Templates (8 violations - 4 files)

**Files Affected:**
1. `TEMPLATE-PROJ-DEV-001.json`
2. `TEMPLATE-PROJ-LG-001.json`
3. `TEMPLATE-PROJ-LG-002.json`
4. `TEMPLATE-PROJ-RES-001_Research_to_Taxonomy_Pipeline.json`

**Missing Required Fields (4 critical):**
- `project_template_id` - All 4 files
- `template_name` - All 4 files

**Missing Recommended Fields (4 medium):**
- `milestone_templates` - All 4 files

**Impact:** Projects cannot be instantiated properly without these core identifiers and milestone definitions.

**Remediation Priority:** HIGH

---

### Task Templates (68 violations - 34 files)

**Critical Issues (34 files):**
All task templates are missing:
- `task_template_id`
- `task_template_name`

**Medium Issues:**
- 34 files missing `category` field
- 3 files missing `description`, `department`

**Sample Affected Files:**
- Airscale_Employee_Enrichment.json
- AI_Powered_HTML_Parsing.json
- Anymailfinder_Nominative_Enrichment.json
- Apollo_IO_Full_Stack_DEPRECATED.json
- Automate_Morning_Email_Drafting.json
- Create_Job_Posting_Template.json
- Create_MCP_Connector.json
- All TEMPLATE-TASK-HR-AUTO-* files (6 total)
- All TEMPLATE-TASK-RES-* files (4 total)
- All TEMPLATE-TASK-VIDEO-* files (4 total)

**Field Usage Patterns:**

Most task templates have descriptive filenames but lack the structured JSON fields. Files use varying field names:
- Some use just `"name"` instead of `"task_template_name"`
- Some use just `"id"` instead of `"task_template_id"`
- Category field completely absent in 34 files

**Impact:**
- Tasks cannot be properly indexed or cross-referenced
- Filtering by category impossible
- Automation scripts cannot process templates reliably

**Remediation Priority:** HIGH

---

### Step Templates (62 violations - 62 files)

**Critical Issues:**
All step template violations are for missing:
- `step_template_id`
- `step_template_name`

**Files Affected:**

**Listing Files (9 files):**
- ADMIN/Listing.json
- AI/Listing.json
- DESIGN/Listing.json
- DEV/Listing.json
- HR/Listing.json
- LG/Listing.json
- OPS/Listing.json
- SALES/Listing.json
- VIDEO/Listing.json

**VIDEO Step Templates (53 files):**
All VIDEO step templates from VIDEO-VIDEO-001-01 through VIDEO-VIDEO-004-16 are missing required fields.

**Pattern Analysis:**

Step templates use various naming approaches:
- File naming follows pattern but JSON content lacks standardized fields
- Some templates may be using generic `"id"` and `"name"` fields
- Listing files are not actual templates (false positives)

**Impact:**
- Step templates cannot be validated against parent task references
- Broken cross-references detected in M4 (56 broken refs)
- Documentation consistency compromised

**Remediation Priority:** MEDIUM (many referenced steps don't exist yet)

---

## Schema Compliance by Template Type

| Template Type | Total Files | With Required Fields | Compliance % |
|---------------|-------------|---------------------|--------------|
| Project Templates | 6 | 2 | 33.3% |
| Milestone Templates | Not analyzed | Not analyzed | - |
| Task Templates | 87 | 53 | 60.9% |
| Step Templates | 71 | 9 | 12.7% |

---

## Required vs Recommended Field Coverage

### Project Templates

**Required Fields:**
- `project_template_id` ❌ 67% missing
- `template_name` ❌ 67% missing
- `milestone_templates` ⚠️ Recommended only

**Recommended Fields:**
- `description` - Not tracked
- `version` - 100% present (M2 versioning analysis)
- `created` - Not tracked
- `last_updated` - Not tracked
- `department` - Not tracked
- `category` - Not tracked

### Task Templates

**Required Fields:**
- `task_template_id` ❌ 39% missing
- `task_template_name` ❌ 39% missing
- `category` ❌ 39% missing
- `department` ⚠️ Partially missing (3 files)

**Recommended Fields:**
- `description` ⚠️ Partially missing (3 files)
- `estimated_hours` - Not tracked
- `step_templates` - Present in many files (cross-references found in M4)
- `dependencies` - Not tracked

### Step Templates

**Required Fields:**
- `step_template_id` ❌ 87% missing
- `step_template_name` ❌ 87% missing

**Recommended Fields:**
- `description` - Not tracked
- `checklist_items` - Not tracked

---

## Root Cause Analysis

### Why So Many Violations?

1. **Inconsistent Field Naming:**
   - Templates use generic `"id"` instead of specific `"{entity}_template_id"`
   - Generic `"name"` instead of `"{entity}_template_name"`

2. **Legacy Templates:**
   - Older templates created before standardization
   - DEPRECATED files still in active folder

3. **Listing Files Treated as Templates:**
   - `Listing.json` files flagged but aren't actual templates
   - Should be excluded from validation or moved to separate folder

4. **Missing Category Taxonomy:**
   - No category field means no systematic organization
   - Department field present but category absent

---

## Remediation Recommendations

### Phase 1: Immediate Fixes (High Priority)

**Week 1-2: Project & Task Templates**

1. **Add Required Fields to Project Templates (4 files)**
   - Add `project_template_id` to all 4 projects
   - Add `template_name` to all 4 projects
   - Estimated effort: 1 hour

2. **Add Required Fields to Task Templates (34 files)**
   - Rename generic `"id"` to `"task_template_id"`
   - Rename generic `"name"` to `"task_template_name"`
   - Add `category` field to all 34 files
   - Estimated effort: 4 hours

### Phase 2: Medium Priority

**Week 3-4: Step Templates**

3. **Add Required Fields to Existing Step Templates**
   - Focus on VIDEO step templates first (53 files)
   - Rename fields to match schema standards
   - Estimated effort: 6 hours

4. **Exclude Listing Files from Validation**
   - Move `Listing.json` files to separate folder or rename
   - Update validation scripts to skip listing files
   - Estimated effort: 1 hour

### Phase 3: Recommended Fields

**Month 2:**

5. **Add Recommended Fields**
   - `description` to all templates
   - `estimated_hours` to task templates
   - `dependencies` where applicable
   - Estimated effort: 8 hours

---

## Validation Standards Reference

### Regex Patterns for Validation

From [REP-006_terminology_standards.json](REP-006_terminology_standards.json):

```regex
# JSON Field Pattern
^[a-z][a-z0-9_]*$

# Entity ID Patterns
step_template_id: ^STEP-[A-Z]+-\d{3}-\d{2}$
task_template_id: ^TASK-TEMPLATE-[A-Z]+-\d{3}$
milestone_template_id: ^MIL-TEMPL-\d{3}$
project_template_id: ^PROJ-TEMPL-\d{3}$
```

### Required Fields by Entity

**Project Templates:**
- project_template_id
- template_name
- milestone_templates (recommended but critical)

**Task Templates:**
- task_template_id
- task_template_name
- category
- department

**Step Templates:**
- step_template_id
- step_template_name

**All Templates (Recommended):**
- description
- version
- created
- last_updated

---

## Automated Validation Script

### Proposed Enhancement

Create `validate_schemas.py` to run on pre-commit:

```python
import json
from pathlib import Path

REQUIRED_FIELDS = {
    'Project_Templates': ['project_template_id', 'template_name'],
    'Milestone_Templates': ['milestone_template_id', 'name'],
    'Task_Templates': ['task_template_id', 'task_template_name', 'category', 'department'],
    'Step_Templates': ['step_template_id', 'step_template_name'],
    'Checklist_Items': ['checklist_item_id', 'item_name', 'status']
}

# Run validation and block commits if violations found
```

---

## Success Metrics

### Targets for Next Audit (Q1 2026)

| Metric | Current | Target |
|--------|---------|--------|
| Critical Violations | 97 | 0 |
| Medium Violations | 41 | <10 |
| Overall Compliance | 72.7% | 100% |
| Project Template Compliance | 33.3% | 100% |
| Task Template Compliance | 60.9% | 100% |
| Step Template Compliance | 12.7% | 95% |

---

## Cross-References

**Related Reports:**
- [REP-001: File Inventory Report](REP-001_File_Inventory_Report.md)
- [REP-002: Naming Convention Audit](REP-002_Naming_Convention_Audit.md)
- [REP-006: Terminology Standards](REP-006_terminology_standards.json)
- [REP-007: Cross-Reference Validation](REP-007_Cross_Reference_Validation.md)

**Data Sources:**
- `schema_violations.json` - Complete violation list
- `field_usage_stats.json` - Field usage patterns
- `milestone_02_summary.json` - M2 overview

---

## Conclusion

Schema validation reveals significant gaps in template standardization, with 97 critical violations requiring immediate attention. The root cause stems from inconsistent field naming and lack of systematic validation during template creation.

**Immediate Action Required:** Fix 4 project templates and 34 task templates to restore core functionality.

**Long-term Solution:** Implement automated pre-commit validation to prevent future violations.

---

*Report generated from Milestone 2 data analysis*
*Next review: After remediation completion*
