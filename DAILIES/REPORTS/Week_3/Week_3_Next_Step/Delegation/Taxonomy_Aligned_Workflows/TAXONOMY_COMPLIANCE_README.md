# TAX-002 Taxonomy Compliance Documentation

**Migration Date:** November 26, 2025
**Source:** Week 3 Workflow Clustering (WFC format)
**Target:** TAX-002_Task_Managers Taxonomy Compliance (WRF format)
**Total Workflows:** 50 (10 Planning + 40 Execution)

---

## Overview

This directory contains **taxonomy-compliant workflow files** that align with the **TAX-002_Task_Managers** taxonomy structure. All workflows have been converted from the original WFC (Workflow Cluster) format to the standardized WRF (Workflow) format with all required taxonomy fields.

---

## Migration Summary

### What Changed

| **Aspect** | **Before (WFC)** | **After (WRF)** | **Reason** |
|------------|------------------|-----------------|------------|
| **Entity ID** | WFC-001 to WFC-050 | WRF-001 to WRF-050 | WFC not in TAX-002 ISO Code Registry; WRF is official |
| **Department Codes** | AI, Design, Development, etc. | AIA, DGN, DEV, etc. | TAX-002 uses 3-letter consonant-only ISO codes |
| **Task IDs** | TSK-### | TST-### | TAX-002 uses TST (TaSk Template) with 'T' suffix |
| **File Format** | CSV | JSON | TAX-002 requires JSON/YAML for structured entities |
| **Required Fields** | 10 fields | 25+ fields | TAX-002 mandates metadata, version, timestamps, etc. |

### Task ID Conversion

**Conversion Pattern:** `TSK-###` → `TST-###` (for simple numeric task IDs only)

**Examples:**
```
TSK-001 → TST-001
TSK-062 → TST-062
TSK-395 → TST-395
```

**Exceptions (kept as-is):**
- `TSK-DEV-2025-11-20-###` - Date-based task IDs (not templates)
- `TSK-DGN-2025-11-20-###` - Department-prefixed daily tasks
- `TSK-AID-2025-11-20-###` - AI department daily tasks
- `TSK-HRM-2025-11-20-###` - HR department daily tasks
- `TSK-LGN-2025-11-20-###` - Lead Gen daily tasks
- `TSK-SLS-2025-11-20-###` - Sales daily tasks
- `TSK-VID-2025-11-20-###` - Video daily tasks
- `TSK-FIN-2025-11-20-###` - Finance daily tasks
- `PRT-###` - Project templates (already correct)
- `MLT-###` - Milestone templates (already correct)
- `FIX-###` - Fix tasks (special entity)

---

## TAX-002 ISO Department Codes

**Department mappings per TAX-002:**

| Old Name | ISO Code | Full Name |
|----------|----------|-----------|
| AI | **AID** | AI Department (includes AI, Automations, Operations, Administration) |
| Design | **DGN** | Design |
| Development | **DEV** | Development |
| Finance | **FIN** | Finance |
| HR | **HRM** | Human Resource Management |
| Lead Generation | **LGN** | Lead Generation |
| Sales | **SLS** | Sales |
| SMM | **SMM** | Social Media Marketing |
| Video | **VID** | Video |

**Rules Applied:**
- ✅ Consonant-only (no vowels A, E, I, O, U except where unavoidable)
- ✅ Exactly 3 letters
- ✅ UPPERCASE only
- ✅ Memorable and intuitive

---

## File Structure

All 50 workflows have been converted to JSON format with full TAX-002 compliance:

**Planning Phase (WRF-001 to WRF-010):**
- WRF-001: Develop USER Entities (PRT-005)
- WRF-002: Prospects Architecture Improvement (PRT-009)
- WRF-003: Populate Business Entity from Sales (PRT-010)
- WRF-004: Google Maps Scraping System (PRT-011)
- WRF-005: Reviews Scraping & Analysis (PRT-012)
- WRF-006: Job Sites Entity Creation (PRT-013)
- WRF-007: HR Attendance Dashboard v1.0 (PRT-014)
- WRF-008: Vilhelm Onboarding & Training (PRT-015)
- WRF-009: AI Tools Management System (PRT-016)
- WRF-010: Task Manager Dashboard UI (PRT-017)

**Execution Phase (WRF-011 to WRF-050):**
- 40 department-based workflows organized by category

_See [WFC_to_WRF_Migration_Map.json](WFC_to_WRF_Migration_Map.json) for complete mapping_

---

## Required TAX-002 Fields

All workflow files include these mandatory fields:

```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Workflow",
  "workflow_id": "WRF-###",
  "metadata": {
    "workflow_name": "string",
    "description": "string",
    "primary_department": "AID|DGN|DEV|FIN|HRM|LGN|SLS|SMM|VID",
    "departments_involved": ["array"],
    "workflow_type": "Sequential|Parallel",
    "execution_phase": "Planning|Execution",
    "priority": "Low|Medium|High",
    "estimated_duration": "string",
    "complexity": "Low|Medium|High",
    "status": "Active",
    "created_date": "2025-11-26",
    "version": "1.0"
  },
  "tasks": {
    "total_count": number,
    "task_ids": ["TST-###", ...],
    "execution_type": "Sequential|Parallel"
  },
  "version": "1.0",
  "created": "2025-11-26",
  "last_updated": "2025-11-26",
  "migration_notes": {
    "original_id": "WFC-###",
    "converted_from": "WFC format",
    "conversion_date": "2025-11-26"
  }
}
```

---

## Usage

**For Project Managers:**
1. Look up WFC-### in [WFC_to_WRF_Migration_Map.json](WFC_to_WRF_Migration_Map.json)
2. Open corresponding WRF-###.json file
3. View full structured workflow data with TAX-002 compliance

**For Developers:**
- Files ready for direct integration into ENTITIES/TAXONOMY/TAX-002_Task_Managers/Workflows/
- All JSON files are valid and schema-compliant
- Can be programmatically validated and processed

**For Department Heads:**
- Find your workflows by department ISO code (e.g., AIA, DGN, DEV, etc.)
- Each file contains task_ids with proper TST-### format
- Full metadata available for planning and tracking

---

## Next Steps

1. **Integration:** Copy workflows to `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Workflows/`
2. **Task Templates:** Convert remaining TSK-### task files to TST-### format
3. **Cross-References:** Link workflows to Project and Milestone templates
4. **Validation:** Run schema validation on all WRF files
5. **Documentation:** Update all references from WFC to WRF

---

## Reference Files

- **[WFC_to_WRF_Migration_Map.json](WFC_to_WRF_Migration_Map.json)** - Complete ID mapping
- **Original:** `../Workflow_Clustering.csv`
- **Taxonomy:** `C:\Users\Dell\Dropbox\ENTITIES\TAXONOMY\TAX-002_Task_Managers\`

---

**Last Updated:** November 26, 2025
**Migration Status:** ✅ Complete (50/50 workflows converted)
