# Phase 2 Context: PROSPECTS Population

**Phase**: 2 of 6
**Agents**: 2 simultaneous
**Priority**: P2-MEDIUM
**Status**: ⏸️ **POSTPONED** - Blocked on CRM data from Kolya/Olya
**Dependencies**: Phase 1C (empty folder analysis) must complete first
**Estimated Complexity**: Medium-High

---

## 🎯 Phase Objectives

1. **Validate prospect schema** against database structure
2. **Update BUSINESSES_Master.json** with new prospect entries
3. **Populate empty prospect folders** (when CRM data arrives)
4. **Integrate department reports** for business context

---

## ⏸️ POSTPONED STATUS

**Reason**: Waiting on CRM data from Kolya/Olya (per user notes: "Get From CRM Data on Daily LeadGen Cards Updates / Delegate to Kolya and Olya")

**Prerequisites to Un-Block**:
1. CRM export data received from Kolya/Olya
2. Phase 1C empty folder analysis completed
3. Decision made on which folders to populate vs delete

**When Un-Blocked**: Execute agents as documented below.

---

## 🤖 Agent Assignments

### Agent 2A: Schema Validation & Department Integration Agent
**Focus**: Validate prospect schema + integrate department reports
**Working Directory**: `BUSINESSES/schemas/` + `REPORTS/2025-11-21/Departments/`
**Output**: Validated schema + department business context mapping

### Agent 2B: Master List Update Agent
**Focus**: Update BUSINESSES_Master.json with validated prospects
**Working Directory**: `BUSINESSES/`
**Output**: Updated master JSON + cross-reference reports

---

## 📋 Agent 2A: Schema Validation & Department Integration

### Problem Statement
Need to ensure prospect data structure aligns with:
1. Database schema (from user notes)
2. Existing populated prospects (33 JSON files)
3. Department report context (for business intelligence)

### Task Instructions

#### Step 1: Validate Existing Prospect Schema
Scan 33 populated prospects in `BUSINESSES/Prospects/` and extract:
- Common field structure
- Required vs optional fields
- Data types and constraints
- Nested object structures (company, contacts, communications)

Compare against database schema:
```sql
prospects (id, name, position_id, status_id, notes, tool_id)
prospect_companies (id, name, website, city_id, country_id, affiliate_id, tool_id, manager_id, created_by, created_at)
prospect_prospect_company (junction)
prospect_company_industries (junction)
prospect_company_sub_industries (junction)
prospect_company_contacts (junction)
prospect_communications (id, prospect_id, prospect_company_id, user_id, account_id, created_at, is_followup, note)
prospect_communication_messages (junction)
```

Output: `Prospect_Schema_Validation_Report.md`

Include:
- Fields present in JSON but not in DB schema (extra fields)
- Fields present in DB schema but not in JSON (missing fields)
- Data type mismatches
- Recommended schema adjustments

#### Step 2: Integrate Department Reports Context
Analyze department reports to extract business context for prospects:

**Source 1**: `REPORTS/2025-11-21/Departments/`
- Scan all department daily reports
- Extract: Companies mentioned, industries discussed, tools used, contacts referenced
- Output: `Department_Business_Context_2025-11-21.csv`

**Source 2**: `REPORTS/2025-11-20/Departments_Processed_TM/`
- Scan processed department reports with task manager integration
- Extract: Prospect-related tasks, industry focus areas, lead generation targets
- Output: `Department_Prospects_Analysis_2025-11-20.csv`

Format:
```csv
Department,Date,Company_Mentioned,Industry,Tool_Used,Contact_Name,Context,Source_Report
LG,2025-11-21,Acme Corp,SaaS,LinkedIn,John Doe,Outreach campaign,LG_Daily_2025-11-21.md
Sales,2025-11-21,Beta Inc,E-commerce,HubSpot,Jane Smith,Demo scheduled,Sales_Daily_2025-11-21.md
```

#### Step 3: Map Industries to Prospects
Cross-reference:
- Department reports industries mentioned
- Existing `BUSINESSES/Industries/` (if exists)
- prospect_company_industries schema

Generate:
- `Industries_Master_List_Enhanced.csv` (existing industries + new from reports)
- `Sub_Industries_Master_List_Enhanced.csv` (sub-industries)
- Mapping: Which prospects belong to which industries

This supports user note: "Expand Industries (LG Team Leads)" and "populate leads data with new classifications and industries"

#### Step 4: Create Enhanced Schema
Based on validation + department context, create:

**File**: `BUSINESSES/schemas/prospect_schema_v2.json`

Include:
- All DB schema fields
- Additional metadata fields from department reports:
  - `mentioned_in_department_reports` (array of dates)
  - `primary_industry_id`
  - `sub_industry_ids` (array)
  - `last_contact_date`
  - `assigned_department`
  - `lead_source`
  - `priority_score` (calculated from report mentions)
- Validation rules (required fields, data types)
- Example values

#### Step 5: Create Department-Prospect Mapping
Generate cross-reference showing which departments work with which prospects:

**File**: `BUSINESSES/Department_Prospect_Matrix.csv`

Format:
```csv
Prospect_ID,Prospect_Name,Primary_Department,Secondary_Departments,Last_Mentioned_Date,Mention_Count,Industries,Status
PROS-001,Acme Corp,LG,"Sales,Marketing",2025-11-21,5,"SaaS,B2B",Active
PROS-002,Beta Inc,Sales,Design,2025-11-20,2,"E-commerce",Prospect
```

This enables:
- Department dashboards showing their prospects
- Priority scoring based on cross-department interest
- Industry analysis per department

### Input Files
```
BUSINESSES/Prospects/ (33 populated JSON files)
BUSINESSES/schemas/ (if existing schema exists)
BUSINESSES/Industries/ (industry master data)
REPORTS/2025-11-21/Departments/ (latest department reports)
REPORTS/2025-11-20/Departments_Processed_TM/ (processed reports with TM)
LIBRARIES/LBS_006_Departments/ (department definitions)
```

### Output Files
```
BUSINESSES/schemas/
├── prospect_schema_v2.json (enhanced schema)
├── Prospect_Schema_Validation_Report.md
├── Industries_Master_List_Enhanced.csv
└── Sub_Industries_Master_List_Enhanced.csv

BUSINESSES/
└── Department_Prospect_Matrix.csv

REPORTS/2025-11-22/System_Rebuild/
├── Phase_2A_Schema_Validation_Report.md
├── Phase_2A_Department_Business_Context_2025-11-21.csv
├── Phase_2A_Department_Prospects_Analysis_2025-11-20.csv
└── Phase_2A_Industry_Expansion_Recommendations.md
```

### Success Criteria
- [ ] Schema validated against DB structure (all fields mapped)
- [ ] Department reports analyzed for business context (2 date ranges)
- [ ] Industries extracted and enhanced (existing + new from reports)
- [ ] Department-Prospect matrix generated
- [ ] Enhanced schema v2 created with validation rules
- [ ] Priority scoring algorithm documented

### Department Reports Integration Details

**Why This Matters**:
Per user notes - "run analysis that describe our target audience" and "extract and analyse conversations from LG accounts"

Department reports contain:
- Real prospect interactions (from LG, Sales, Marketing)
- Industry patterns (which industries each department focuses on)
- Tool usage (which tools are used with which prospects)
- Contact history (who was contacted, when, outcome)

Integrating this into prospect schema enables:
1. **Automated priority scoring** - Prospects mentioned multiple times rank higher
2. **Department routing** - New prospects auto-assigned to relevant departments
3. **Industry intelligence** - See which industries are hot based on report activity
4. **Lookalike audience building** - Per user note: "build look alike auditory for setting campaigns"

---

## 📋 Agent 2B: Master List Update

### Problem Statement
`BUSINESSES_Master.json` currently has 40 entities. After Phase 1C and Phase 2A, need to update with:
- Validated prospects (from 33 populated + new CRM data)
- Department cross-references
- Industry classifications
- Status tracking

### Task Instructions

#### Step 1: Analyze Current BUSINESSES_Master.json
Extract current structure:
- Entity count (currently 40)
- Entity types included (Clients, Prospects, Ex_Clients, etc.)
- Field structure
- ID numbering scheme

Output: `Current_Master_JSON_Analysis.md`

#### Step 2: Cross-Reference with Phase 1C Results
Import results from Phase 1C (empty folder analysis):
- Folders marked KEEP (to be populated)
- Folders marked DELETE (to be removed)
- Cross-reference with existing master JSON

Generate delta report:
- Entities to ADD (new from CRM data when received)
- Entities to UPDATE (existing 33 prospects with enhanced schema)
- Entities to REMOVE (folders marked DELETE)

Output: `Master_JSON_Delta_Report.csv`

#### Step 3: Cross-Reference with MASTER_ACTIVITY_LISTING
Integrate data from `REPORTS/2025-11-21/MASTER_ACTIVITY_LISTING_2025-11-21.csv`:
- Extract any business/company mentions
- Cross-reference with prospects
- Identify prospects that appeared in activities but not in master JSON

This supports user note: "Can Be Used as ToDo Initial List to build"

Output: `Activity_Listing_Business_Extraction.csv`

Format:
```csv
Activity_Date,Activity_Type,Company_Name,In_Prospects,In_Clients,In_Master_JSON,Action_Required
2025-11-21,Call,Acme Corp,Yes,No,Yes,No action
2025-11-21,Meeting,Gamma Ltd,No,No,No,ADD to prospects
```

#### Step 4: Generate Updated BUSINESSES_Master.json
Create new version incorporating:
- Validated schema from Agent 2A
- Phase 1C keep/delete decisions
- Activity listing business entities
- Department-Prospect matrix references

**Structure**:
```json
{
  "meta": {
    "version": "2.0",
    "last_updated": "2025-11-22",
    "entity_count": "[NEW_COUNT]",
    "changes_from_v1": {
      "added": "[COUNT]",
      "updated": "[COUNT]",
      "removed": "[COUNT]"
    }
  },
  "entities": [
    {
      "entity_id": "BUS-001",
      "entity_type": "Prospect",
      "name": "Acme Corp",
      "prospect_id": "PROS-001",
      "schema_version": "v2",
      "primary_department": "LG",
      "industries": ["SaaS", "B2B"],
      "status": "Active",
      "priority_score": 85,
      "last_activity_date": "2025-11-21",
      "file_path": "BUSINESSES/Prospects/Acme_Corp/Acme_Corp.json"
    },
    ...
  ]
}
```

Save as: `BUSINESSES/BUSINESSES_Master_v2.json`

Keep backup: `BUSINESSES/BUSINESSES_Master_v1_backup.json`

#### Step 5: Generate Cross-Reference Reports
Create validation reports:

**Report 1**: `Master_JSON_Coverage_Report.csv`
- Shows which BUSINESSES folders are in master JSON vs not
- Identifies orphaned folders
- Flags missing JSON files

**Report 2**: `Department_Coverage_by_Business.csv`
- Shows which departments work with which businesses
- Identifies businesses with no department assignment
- Recommends department routing for new prospects

**Report 3**: `Industry_Distribution_Report.csv`
- Count of prospects per industry
- Department breakdown per industry
- Gap analysis: underrepresented industries

This supports user note: "Expand Industries (LG Team Leads)" - shows which industries need expansion

### Input Files
```
BUSINESSES/BUSINESSES_Master.json (v1 - 40 entities)
REPORTS/2025-11-22/System_Rebuild/Phase_1C_Empty_Folders_Recommendation_Report.md
BUSINESSES/schemas/prospect_schema_v2.json (from Agent 2A)
BUSINESSES/Department_Prospect_Matrix.csv (from Agent 2A)
REPORTS/2025-11-21/MASTER_ACTIVITY_LISTING_2025-11-21.csv
```

### Output Files
```
BUSINESSES/
├── BUSINESSES_Master_v2.json (NEW)
├── BUSINESSES_Master_v1_backup.json (BACKUP)
└── Master_JSON_Changelog.md

REPORTS/2025-11-22/System_Rebuild/
├── Phase_2B_Current_Master_JSON_Analysis.md
├── Phase_2B_Master_JSON_Delta_Report.csv
├── Phase_2B_Activity_Listing_Business_Extraction.csv
├── Phase_2B_Master_JSON_Coverage_Report.csv
├── Phase_2B_Department_Coverage_by_Business.csv
└── Phase_2B_Industry_Distribution_Report.csv
```

### Success Criteria
- [ ] Current master JSON analyzed (40 entities documented)
- [ ] Delta report shows exact changes (add/update/remove counts)
- [ ] Activity listing mined for business entities
- [ ] Updated master JSON v2 created with enhanced schema
- [ ] All cross-reference reports generated
- [ ] Industry distribution shows expansion opportunities
- [ ] Department routing recommendations complete

---

## 🔗 Cross-Agent Dependencies

### Agent 2A → Agent 2B (Sequential)
**Dependency**: Agent 2B needs Agent 2A's outputs
- Agent 2A creates `prospect_schema_v2.json`
- Agent 2B uses this schema to update master JSON
- **Execution Order**: 2A completes FIRST, then 2B starts

---

## 📊 Phase 2 Validation Checklist

After both agents complete, manually review:

### Agent 2A Outputs
- [ ] Review `Prospect_Schema_Validation_Report.md` - verify schema completeness
- [ ] Check `Department_Business_Context_2025-11-21.csv` - validate extractions
- [ ] Review `Department_Prospects_Analysis_2025-11-20.csv` - confirm task manager integration
- [ ] Verify `Industries_Master_List_Enhanced.csv` - approve new industries
- [ ] Check `Department_Prospect_Matrix.csv` - validate department assignments
- [ ] Review `prospect_schema_v2.json` - approve as canonical schema
- [ ] Approve enhanced schema OR request modifications

### Agent 2B Outputs
- [ ] Review `Master_JSON_Delta_Report.csv` - verify add/update/remove counts
- [ ] Check `Activity_Listing_Business_Extraction.csv` - validate new entities found
- [ ] Review `BUSINESSES_Master_v2.json` - spot-check 10 random entities
- [ ] Verify `Master_JSON_Coverage_Report.csv` - check for orphaned folders
- [ ] Review `Department_Coverage_by_Business.csv` - validate department routing
- [ ] Check `Industry_Distribution_Report.csv` - identify expansion opportunities
- [ ] Approve master JSON v2 OR request adjustments

---

## 🚦 Phase 2 Exit Criteria

Before proceeding to next phase:

**MUST COMPLETE:**
- [ ] ⏸️ **UNBLOCKED** - CRM data received from Kolya/Olya
- [ ] Phase 1C completed (empty folder analysis)
- [ ] Both agents completed successfully
- [ ] Both validation checklists reviewed
- [ ] All reports saved to `REPORTS/2025-11-22/System_Rebuild/`
- [ ] Manual decisions made on:
  - [ ] Approve enhanced schema v2
  - [ ] Approve master JSON v2
  - [ ] Approve industry expansion list

**METRICS UPDATED:**
- [ ] BUSINESSES_Master.json entities: 40 → [NEW COUNT]
- [ ] Prospects with JSON: 33 → [NEW COUNT]
- [ ] Industries cataloged: [OLD COUNT] → [NEW COUNT]
- [ ] Department-Prospect mappings: 0 → [NEW COUNT]

**READY FOR NEXT PHASE:**
- [ ] BUSINESSES_Master_v2.json is canonical source
- [ ] prospect_schema_v2.json is canonical schema
- [ ] Industries expanded per LG Team Leads needs
- [ ] Department routing established

---

## 🔑 Key File Paths Reference

### Agent 2A Paths
```
INPUT:
BUSINESSES/Prospects/ (33 populated JSON files)
BUSINESSES/schemas/
BUSINESSES/Industries/
REPORTS/2025-11-21/Departments/
REPORTS/2025-11-20/Departments_Processed_TM/
LIBRARIES/LBS_006_Departments/

OUTPUT:
BUSINESSES/schemas/prospect_schema_v2.json
BUSINESSES/schemas/Prospect_Schema_Validation_Report.md
BUSINESSES/schemas/Industries_Master_List_Enhanced.csv
BUSINESSES/schemas/Sub_Industries_Master_List_Enhanced.csv
BUSINESSES/Department_Prospect_Matrix.csv
REPORTS/2025-11-22/System_Rebuild/Phase_2A_*.{csv,md}
```

### Agent 2B Paths
```
INPUT:
BUSINESSES/BUSINESSES_Master.json (v1)
REPORTS/2025-11-22/System_Rebuild/Phase_1C_Empty_Folders_Recommendation_Report.md
BUSINESSES/schemas/prospect_schema_v2.json (from Agent 2A)
BUSINESSES/Department_Prospect_Matrix.csv (from Agent 2A)
REPORTS/2025-11-21/MASTER_ACTIVITY_LISTING_2025-11-21.csv

OUTPUT:
BUSINESSES/BUSINESSES_Master_v2.json
BUSINESSES/BUSINESSES_Master_v1_backup.json
BUSINESSES/Master_JSON_Changelog.md
REPORTS/2025-11-22/System_Rebuild/Phase_2B_*.{csv,md}
```

---

## 📝 Prompts Reference

**Prospect Data Extraction Prompts**:
- `PROMPTS/DATA_FIELDS/Prospect_Field_Extraction.md` (if exists)
- `PROMPTS/DEPARTMENTS/Sales/CRM_Data_Processing.md` (if exists)

**Industry Classification Prompts**:
- `PROMPTS/SYSTEM/Taxonomy_Integration/Industry_Classification.md` (if exists)

**Department Reports Analysis Prompts**:
- `PROMPTS/DEPARTMENTS/Daily_Reports/` (10 department templates)
- Use to understand report structure when extracting business context

---

## 🎯 Success Metrics

| Metric | Before Phase 2 | After Phase 2 | Target |
|--------|----------------|---------------|--------|
| BUSINESSES_Master.json entities | 40 | [NEW] | ⬆️ Increased |
| Prospects with JSON | 33 | [NEW] | ⬆️ Populated |
| Empty prospect folders | 298 | [NEW] | ⬇️ Reduced |
| Industries cataloged | [OLD] | [NEW] | ⬆️ Expanded |
| Department-Prospect mappings | 0 | [NEW] | ✅ Created |
| Schema version | v1 (implicit) | v2 (explicit) | ✅ Validated |

---

## 🔄 Rollback Plan

If Phase 2 causes issues:

### Agent 2A Rollback
1. Delete `prospect_schema_v2.json`
2. Continue using implicit schema from 33 populated prospects
3. Department reports analysis saved, not rolled back

### Agent 2B Rollback
1. Restore `BUSINESSES_Master_v1_backup.json` to `BUSINESSES_Master.json`
2. Delete `BUSINESSES_Master_v2.json`
3. Review `Master_JSON_Changelog.md` to understand what was reverted

---

## 💡 Notes for Future Population

When CRM data arrives from Kolya/Olya:

1. **Use templates from Phase 1C**:
   - `BUSINESSES/Prospects/Prospect_Template_v2.json`
   - `BUSINESSES/Prospects/Prospect_Import_Template.csv`
   - `BUSINESSES/Prospects/Prospect_Field_Mapping.md`

2. **Follow schema from Phase 2A**:
   - `BUSINESSES/schemas/prospect_schema_v2.json`

3. **Update master JSON via Phase 2B process**:
   - Add new entities to `BUSINESSES_Master_v2.json`
   - Regenerate cross-reference reports

4. **Reference department reports**:
   - Check if CRM prospects are mentioned in `REPORTS/2025-11-21/Departments/`
   - Auto-assign departments based on mentions

---

**END OF PHASE 2 CONTEXT**

**Current Status**: ⏸️ **POSTPONED** - Execute when CRM data arrives

**Next Steps**:
1. Keep this context document ready
2. When CRM data received, execute Agent 2A then 2B
3. Review validation checklists
4. Update BUSINESSES_Master.json to v2
