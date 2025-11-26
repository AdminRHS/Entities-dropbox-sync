# MLT-005: Template Creation

**Milestone ID:** MLT-005
**Milestone Name:** Template Creation
**Duration:** 30 minutes
**Part of Workflow:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
**Position:** Milestone 5 of 9

---

## Overview

Create new TST-### task templates for all LIBRARY_ONLY and NEW tasks identified in gap analysis. Expected: 28 LIBRARY_ONLY + 14 NEW = 42 new templates.

---

## What You'll Do

### 1. Create TST-### Templates

**Template Location:**
```
/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/
```

**Also Save Copy To:**
```
/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/04_Task_Templates/
```

### 2. Template ID Assignment

**Next Available IDs:**
- Current: TST-071
- New Range: TST-072 to TST-113 (42 templates)

**ID Assignment by Department:**

| Department | Template Range | Count |
|------------|----------------|-------|
| AI & Automation (AID) | TST-072 to TST-079 | 8 |
| Design (DGN) | TST-080 to TST-089 | 10 |
| Lead Generation (LGN) | TST-090 to TST-104 | 15 |
| Video (VID) | TST-105 to TST-109 | 5 |
| Sales (SLS) | TST-110 to TST-111 | 2 |
| Development (DEV) | TST-112 | 1 |
| HR (HRM) | TST-113 | 1 |

---

## Template Structure (JSON Format)

**File Name:** `TST-{ID}_{TASK_NAME}.json`

**Example:** `TST-072_Export_Contacts_CSV_LinkedIn.json`

```json
{
  "template_id": "TST-072",
  "template_name": "Export_Contacts_CSV_LinkedIn",
  "template_type": "task_template",
  "version": "1.0",
  "created_date": "2025-11-25",
  "status": "active",

  "metadata": {
    "department": "LGN",
    "department_name": "Lead Generation",
    "profession": "PRF-LDG",
    "profession_name": "Lead Generator",
    "category": "lead_enrichment",
    "priority": "high",
    "estimated_duration_minutes": 15
  },

  "task_definition": {
    "name": "Export Contacts to CSV from LinkedIn",
    "description": "Export filtered contact list from LinkedIn Sales Navigator to CSV file for lead database",
    "action": {
      "id": "ACT-067",
      "name": "Export",
      "type": "process_verb"
    },
    "object": {
      "id": "OBJ-LGN-008",
      "name": "Contact List",
      "deliverable_type": "data_file"
    },
    "tool": {
      "id": "TOL-LGN-015",
      "name": "LinkedIn Sales Navigator",
      "category": "lead_generation"
    }
  },

  "skills_required": [
    {
      "skill_id": "SKL-012",
      "skill_name": "export contacts via LinkedIn",
      "proficiency_level": "intermediate"
    }
  },

  "steps": [
    {
      "step_id": "STP-001",
      "step_name": "Apply search filters",
      "description": "Set filters for job title, location, company size in Sales Navigator",
      "estimated_minutes": 3
    },
    {
      "step_id": "STP-002",
      "step_name": "Select contacts",
      "description": "Review results and select all relevant contacts (up to 2,500)",
      "estimated_minutes": 5
    },
    {
      "step_id": "STP-003",
      "step_name": "Export to CSV",
      "description": "Click Export button, select CSV format, download file",
      "estimated_minutes": 2
    },
    {
      "step_id": "STP-004",
      "step_name": "Verify export",
      "description": "Open CSV, verify all required fields present (name, title, company, email)",
      "estimated_minutes": 5
    }
  ],

  "checklist": [
    "Filters applied correctly",
    "Contact count matches expectation",
    "CSV file downloaded successfully",
    "All required fields present in CSV",
    "No duplicate entries",
    "File saved to correct location"
  ],

  "deliverables": [
    {
      "name": "LinkedIn_Contacts_Export.csv",
      "type": "data_file",
      "format": "CSV",
      "location": "/ENTITIES/LIBRARIES/Lead_Generation/Contact_Lists/"
    }
  ],

  "dependencies": {
    "tools_required": ["TOL-LGN-015"],
    "library_objects": ["OBJ-LGN-008"],
    "prerequisite_tasks": [],
    "related_workflows": ["WRF-002"]
  },

  "success_criteria": {
    "quality_checks": [
      "CSV contains minimum 100 contacts",
      "All email fields populated",
      "No formatting errors"
    ],
    "completion_indicator": "CSV file saved and verified"
  },

  "tags": [
    "lead_generation",
    "linkedin",
    "data_export",
    "contact_management"
  ]
}
```

---

## Creation Priority

### Priority 1: LIBRARY_ONLY Templates (28 templates)

**Faster to create** - All library entities exist

**Top 10 by Demand:**
1. TST-072: Export_Contacts_CSV_LinkedIn (LGN) - 8 requests
2. TST-073: Analyze_Video_Metrics_YouTube (VID) - 5 requests
3. TST-074: Create_Social_Media_Post_Instagram (DGN) - 5 requests
4. TST-075: Update_Project_Status_Notion (AID) - 4 requests
5. TST-076: Generate_Weekly_Report_Google_Sheets (AID) - 4 requests
6. TST-077: Design_Email_Newsletter_Figma (DGN) - 3 requests
7. TST-078: Schedule_Meeting_Calendly (AID) - 3 requests
8. TST-079: Create_Thumbnail_Photoshop (DGN) - 3 requests
9. TST-080: Send_Follow_Up_Email_Gmail (SLS) - 2 requests
10. TST-081: Backup_Files_Dropbox (AID) - 2 requests

### Priority 2: NEW Templates (14 templates)

**Requires library work first** - Create missing entities

**By Library Complexity:**

#### Simple (3 new entities or fewer):
1. TST-090: Generate_Leads_Via_Hunter_IO (LGN)
   - Missing: TOL-LGN-042 (Hunter.io)
2. TST-091: Track_Time_Toggl (AID)
   - Missing: TOL-AIA-081 (Toggl)
3. TST-092: Create_MCP_Connector_VS_Code (DEV)
   - Missing: TOL-DEV-026 (MCP SDK)

#### Complex (4+ new entities):
1. TST-093: Create_3D_Animation_Blender (DGN)
   - Missing: TOL-DGN-045 (Blender), OBJ-DGN-025 (3D Animation), SKL-025
2. TST-094: Automate_HR_Onboarding_Bamboo (HRM)
   - Missing: TOL-HRM-001 (BambooHR), WRF-025 (Onboarding Workflow), SKL-026

---

## Library Entity Creation

For NEW tasks, create missing library entries first:

### Tools (8 new)

**File Location:** `/ENTITIES/LIBRARIES/Tools/`

**Format:** Add to appropriate category file (e.g., `Lead_Generation_Tools.json`)

```json
{
  "tool_id": "TOL-LGN-042",
  "tool_name": "Hunter.io",
  "category": "lead_generation",
  "subcategory": "email_finder",
  "department": "LGN",
  "description": "Email finding and verification tool for B2B lead generation",
  "url": "https://hunter.io",
  "pricing": "freemium",
  "features": [
    "Email finder by domain",
    "Email verifier",
    "Bulk email search",
    "Chrome extension"
  ],
  "integration": ["CRM", "Google Sheets"],
  "learning_curve": "low",
  "status": "active"
}
```

### Objects (3 new)

**File Location:** `/ENTITIES/LIBRARIES/Objects/`

**Example:** `OBJ-DGN-025: 3D Animation`

### Skills (2 new)

**File Location:** `/ENTITIES/LIBRARIES/Skills/`

**Example:** `SKL-025: "create 3D animation via Blender"`

---

## Batch Creation Strategy

### Option 1: Manual (30 min)
- Create templates one by one
- Use existing templates as reference
- Copy/paste and modify

### Option 2: Template Generator Script (Future)
**Script:** `create_template_batch.py`

```python
# Pseudo-code
gap_analysis = load('Gap_Analysis_2025-11-25.md')
template_base = load('TST-001_Template_Base.json')

for task in gap_analysis.library_only:
    new_template = template_base.copy()
    new_template['template_id'] = next_id()
    new_template['template_name'] = task.name
    new_template['action'] = task.action
    new_template['object'] = task.object
    new_template['tool'] = task.tool
    save(f'TST-{new_id}_{task.name}.json', new_template)
```

**Time Savings:** 30 min → 5 min (25 min saved)

---

## Taxonomy Integration

### Update Master Lists

After creating templates, update:

**1. Task Templates Master List:**
```
/ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv
```

Add 42 new rows:
```csv
New_ID,Entity_Type,Current_ID,Name,Description,Department,File_Path,Status
TST-072,Task Template,TST-072,Export_Contacts_CSV_LinkedIn,Export contact list from LinkedIn to CSV,LGN,TSM-003_Task_Templates/TST-072_Export_Contacts_CSV_LinkedIn.json,active
TST-073,Task Template,TST-073,Analyze_Video_Metrics_YouTube,Analyze video performance in YouTube Analytics,VID,TSM-003_Task_Templates/TST-073_Analyze_Video_Metrics_YouTube.json,active
...
```

**2. Libraries Master List (for NEW entities):**
```
/ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv
```

Add tool/object/skill entries.

---

## Checklist

- [ ] Review Gap_Analysis_2025-11-25.md
- [ ] Identify 28 LIBRARY_ONLY tasks
- [ ] Identify 14 NEW tasks
- [ ] Assign TST IDs (TST-072 to TST-113)
- [ ] Create missing library entities for NEW tasks (8 tools, 3 objects, 2 skills)
- [ ] Create 28 LIBRARY_ONLY templates
- [ ] Create 14 NEW templates
- [ ] Save all templates to TSM-003_Task_Templates/
- [ ] Save copies to 04_Task_Templates/
- [ ] Update TAX-002 Taxonomy Master List
- [ ] Update TAX-001 Libraries Master List (for NEW entities)
- [ ] Verify all templates have complete JSON structure
- [ ] Update processing log with template creation metrics

---

## Expected Outcomes

✅ **Templates Created**
- **Count:** 42 new TST-### templates (TST-072 to TST-113)
- **Location:** `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/`
- **Copy:** `/ENTITIES/DAILIES/Daily_Processing/2025-11-25_Collection/04_Task_Templates/`

✅ **Library Expanded**
- **New Tools:** 8 (TOL-LGN-042, TOL-DGN-045, etc.)
- **New Objects:** 3 (OBJ-DGN-025, etc.)
- **New Skills:** 2 (SKL-025, SKL-026)

✅ **Ready for MLT-006**
- All tasks now have TST-### templates
- Templates available for assignment algorithm
- Taxonomy updated with new entities

---

## Metrics to Track

Update `06_Processing_Log.md`:

```markdown
## MLT-005: Template Creation Metrics

| Metric | Count |
|--------|-------|
| LIBRARY_ONLY Templates Created | 28 |
| NEW Templates Created | 14 |
| Total Templates Created | 42 |
| New Tools Added | 8 |
| New Objects Added | 3 |
| New Skills Added | 2 |
| Template ID Range | TST-072 to TST-113 |
```

---

## Next Milestone

**→ [MLT-006: Task Assignment Planning](MLT-006_Task_Assignment_Planning.md)** - Assign 87 tasks to employees using multi-factor algorithm (45 minutes)

---

## Related Documentation

- **Main Guide:** [GDS-001 Daily Task Processing Instructions](../../Daily_Processing/Daily_Processing_Workflow/Guides/GDS-001_Daily_Task_Processing_Instructions.md)
- **Task Templates:** [TSM-003 Task Templates](../../../TASK_MANAGERS/TSM-003_Task_Templates/)
- **Template Example:** [TST-001](../../../TASK_MANAGERS/TSM-003_Task_Templates/TST-001_Example.json)
- **Taxonomy Master List:** [TAX-002 Taxonomy Master List](../../../TAXONOMY/TAX-002_Task_Managers/Taxonomy_Master_List.csv)

---

**Created:** 2025-11-25
**Version:** 1.0
**Status:** Active
