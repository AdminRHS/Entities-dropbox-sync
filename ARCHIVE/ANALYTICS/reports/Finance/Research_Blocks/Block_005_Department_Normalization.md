# Research Block 005: Department Structure Normalization

**Block ID:** Block_005_Department_Normalization  
**Date:** 2025-11-21  
**Duration:** 2 hours  
**Status:** Complete  
**Researcher:** Finance Operations Team  
**Report ID:** RES-REP-FIN-005 (to be created)

---

## Research Questions

1. What are the department naming variations?
2. How should departments be normalized?
3. How do they align with ENTITIES TAXONOMY?
4. What mapping rules are needed?

---

## Scope

**What This Block Covers:**
- Department naming variations across Finance, ENTITIES, and Nov25
- Normalization strategies and mapping rules
- ENTITIES TAXONOMY ISO code alignment
- Special cases (managers department, Content department)
- Implementation requirements

**What This Block Excludes:**
- Implementation of normalization scripts (future work)
- Historical data migration (future research block)
- Department restructuring (organizational decision)

**Time Boundaries:**
- Start: 2025-11-21 18:00
- End: 2025-11-21 20:00
- Duration: 2 hours

---

## Methodology

**Data Sources:**
- `Finance 2025 - Copy/Fin_Dec25/03_department_structure_analysis_results.yaml` - Department analysis
- `Finance 2025 - Copy/Fin_Dec25/Fields_Data/department_values.yaml` - Department mapping
- `Finance 2025 - Copy/Fin_Dec25/07_employee_integration_schema_results.yaml` - Integration schema
- `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md` - ISO code registry
- `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md` - Task Manager ISO codes

**Research Approach:**
- Analyze department naming variations
- Map Finance/Nov25 departments to ENTITIES ISO codes
- Document normalization rules
- Identify special cases and edge cases
- Assess alignment with ENTITIES TAXONOMY

**Tools Used:**
- Department analysis (YAML files)
- ISO code registry (TAXONOMY documentation)
- Mapping table analysis (department_values.yaml)

---

## Findings

### Key Findings

1. **Department Naming Variations**
   - **Finance:** Lowercase plural (e.g., "designers", "developers", "managers")
   - **ENTITIES:** Title case singular (e.g., "Design", "Dev", "LG")
   - **Nov25:** Folder names with "Nov25" suffix (e.g., "Design Nov25", "Dev Nov25")
   - **ENTITIES ISO Codes:** Consonant-only 3-letter codes (e.g., "DGN", "DEV", "LGN")

2. **Department Counts**
   - **Finance:** 6 unique departments (designers, developers, videographers, managers, marketers, crm)
   - **ENTITIES:** 7 departments (AI, Design, Dev, HR, LG, Sales, Video) - **Missing Finance**
   - **Nov25:** 9 department folders (includes Content and Niko folders)
   - **Unified:** 8 canonical departments (AIA, DGN, DEV, HRM, LGN, SLS, VID, FIN)

3. **ENTITIES TAXONOMY ISO Codes**
   - **Format:** Consonant-only 3-letter codes
   - **Standard:** AIA, DGN, DEV, HRM, LGN, SLS, VID, FIN
   - **Alignment:** All departments should use ISO codes for consistency

4. **Special Cases**
   - **Finance "managers" department:** Includes multiple roles (LG, HR, Sales, Finance, AI) - needs profession-based mapping
   - **Content department:** Exists in Nov25 but not in Finance or ENTITIES - needs decision
   - **Niko Nov25 folder:** Management/admin folder, not a department - should be ignored
   - **21 accounts with empty department:** Need assignment rules

### Department Naming Analysis

**Finance Department Naming:**
- **Format:** Lowercase plural
- **Examples:** "designers", "developers", "videographers", "managers", "marketers", "crm"
- **Variations:** "designers project", "crm" (mapped to developers)
- **Total:** 6 unique department names

**ENTITIES Department Naming:**
- **Format:** Title case singular
- **Examples:** "AI", "Design", "Dev", "HR", "LG", "Sales", "Video"
- **Missing:** "Finance" department (needs to be added)
- **Total:** 7 departments (8 with Finance)

**Nov25 Department Naming:**
- **Format:** "{Department} Nov25" folder names
- **Examples:** "AI Nov25", "Design Nov25", "Dev Nov25", "HR Nov25", "LG Nov25", "Sales Nov25", "Video Nov25", "Fin Nov25"
- **Special:** "Content Nov25" (not in Finance/ENTITIES), "Niko Nov25" (management folder)
- **Total:** 9 folders (7 departments + 2 special)

**ENTITIES TAXONOMY ISO Codes:**
- **Format:** Consonant-only 3-letter codes
- **Standard Codes:**
  - **AIA** - AI & Automation
  - **DGN** - Design
  - **DEV** - Development
  - **HRM** - Human Resources
  - **LGN** - Lead Generation
  - **SLS** - Sales
  - **VID** - Video Production
  - **FIN** - Finance (needs to be added)

### Department Mapping Analysis

**Finance → ENTITIES ISO Code Mapping:**

| Finance Department | ENTITIES ISO Code | Transformation | Notes |
|-------------------|-------------------|----------------|-------|
| "designers" | DGN | Lowercase plural → ISO code | Direct mapping |
| "developers" | DEV | Lowercase plural → ISO code | Direct mapping |
| "crm" | DEV | Special case → ISO code | CRM mapped to Dev |
| "videographers" | VID | Lowercase plural → ISO code | Direct mapping |
| "managers" | LGN/HRM/SLS/FIN/AIA | Profession-based mapping | **Special case** |
| "marketers" | SLS | Lowercase plural → ISO code | Marketers → Sales |

**Nov25 → ENTITIES ISO Code Mapping:**

| Nov25 Folder | ENTITIES ISO Code | Transformation | Notes |
|--------------|-------------------|----------------|-------|
| "AI Nov25" | AIA | Remove suffix → ISO code | Direct mapping |
| "Design Nov25" | DGN | Remove suffix → ISO code | Direct mapping |
| "Dev Nov25" | DEV | Remove suffix → ISO code | Direct mapping |
| "HR Nov25" | HRM | Remove suffix → ISO code | Direct mapping |
| "LG Nov25" | LGN | Remove suffix → ISO code | Direct mapping |
| "Sales Nov25" | SLS | Remove suffix → ISO code | Direct mapping |
| "Video Nov25" | VID | Remove suffix → ISO code | Direct mapping |
| "Fin Nov25" | FIN | Remove suffix → ISO code | Direct mapping |
| "Content Nov25" | [TBD] | Decision needed | Not in Finance/ENTITIES |
| "Niko Nov25" | [N/A] | Ignore | Management folder |

### Special Cases Analysis

**Case 1: Finance "managers" Department**
- **Problem:** Finance "managers" department includes multiple roles
- **Employee Count:** 20 employees
- **Breakdown:**
  - Lead generators: 15 → LGN
  - Recruiters: 3 → HRM
  - Sales managers: 2 → SLS
  - Financial managers: 3 → FIN
  - Project managers: 1 → AIA
- **Solution:** Profession-based mapping (check profession field, not department field)
- **Mapping Rules:**
  - Profession "lead generator" → LGN
  - Profession "recruiter" → HRM
  - Profession "sales manager" → SLS
  - Profession "financial manager" → FIN
  - Profession "project manager" → AIA

**Case 2: Content Department**
- **Problem:** "Content Nov25" folder exists but not in Finance or ENTITIES
- **Status:** Documentation only, no active employees
- **Options:**
  - Option A: Add Content department to ENTITIES (CNT code)
  - Option B: Map Content to existing department (e.g., Sales or Video)
  - Option C: Keep as documentation-only folder
- **Recommendation:** Map to Sales (SLS) or create Content department if needed

**Case 3: Niko Nov25 Folder**
- **Problem:** "Niko Nov25" is management/admin folder, not a department
- **Status:** 425 files, no employees
- **Solution:** Ignore for department mapping, treat as management/admin folder

**Case 4: Empty Department Fields**
- **Problem:** 21 accounts have empty department field (29% of accounts)
- **Impact:** Cannot assign accounts to departments
- **Solution:** Auto-assign based on tool usage, owner, or manual assignment

### Normalization Rules

**Rule 1: Finance → ENTITIES ISO Code**
```
Function: normalize_department_finance_to_iso
Input: Finance department name (lowercase plural)
Output: ENTITIES ISO code (3-letter consonant)

Mapping:
- "designers" → "DGN"
- "developers" → "DEV"
- "crm" → "DEV"
- "videographers" → "VID"
- "marketers" → "SLS"
- "managers" → [profession-based mapping]
```

**Rule 2: Nov25 → ENTITIES ISO Code**
```
Function: normalize_department_nov25_to_iso
Input: Nov25 folder name ("{Department} Nov25")
Output: ENTITIES ISO code (3-letter consonant)

Mapping:
- Remove " Nov25" suffix
- Map canonical name to ISO code
- Handle special cases (Content, Niko)
```

**Rule 3: Profession-Based Mapping (Managers)**
```
Function: map_managers_by_profession
Input: Department="managers", Profession field
Output: ENTITIES ISO code

Mapping:
- Profession="lead generator" → "LGN"
- Profession="recruiter" → "HRM"
- Profession="sales manager" → "SLS"
- Profession="financial manager" → "FIN"
- Profession="project manager" → "AIA"
- Default: "LGN" (if profession unknown)
```

**Rule 4: ENTITIES Name → ISO Code**
```
Function: map_entities_name_to_iso
Input: ENTITIES department name (title case singular)
Output: ENTITIES ISO code (3-letter consonant)

Mapping:
- "AI" → "AIA"
- "Design" → "DGN"
- "Dev" → "DEV"
- "HR" → "HRM"
- "LG" → "LGN"
- "Sales" → "SLS"
- "Video" → "VID"
- "Finance" → "FIN" (when added)
```

### Unified Department Structure

**Canonical Departments (8 total):**
1. **AIA** - AI & Automation
2. **DGN** - Design
3. **DEV** - Development
4. **HRM** - Human Resources
5. **LGN** - Lead Generation
6. **SLS** - Sales
7. **VID** - Video Production
8. **FIN** - Finance (needs to be added to ENTITIES)

**Department Statistics:**
- **Finance Employees:** 6 departments (managers needs profession-based breakdown)
- **ENTITIES:** 7 departments (missing Finance)
- **Nov25:** 7 active departments + 2 special folders
- **Unified:** 8 canonical departments

---

## Integration Mapping

### Department Normalization Table

| Source System | Source Value | Unified ISO Code | Transformation Function | Priority |
|--------------|--------------|------------------|-------------------------|----------|
| Finance CSV | "designers" | DGN | normalize_department | High |
| Finance CSV | "developers" | DEV | normalize_department | High |
| Finance CSV | "crm" | DEV | normalize_department | High |
| Finance CSV | "videographers" | VID | normalize_department | High |
| Finance CSV | "marketers" | SLS | normalize_department | High |
| Finance CSV | "managers" | LGN/HRM/SLS/FIN/AIA | map_managers_by_profession | High |
| Finance Accounts | "AI" | AIA | normalize_department | Medium |
| Finance Accounts | "financial_manager" | FIN | normalize_department | Medium |
| Nov25 | "AI Nov25" | AIA | extract_from_folder_name | High |
| Nov25 | "Design Nov25" | DGN | extract_from_folder_name | High |
| Nov25 | "Dev Nov25" | DEV | extract_from_folder_name | High |
| Nov25 | "HR Nov25" | HRM | extract_from_folder_name | High |
| Nov25 | "LG Nov25" | LGN | extract_from_folder_name | High |
| Nov25 | "Sales Nov25" | SLS | extract_from_folder_name | High |
| Nov25 | "Video Nov25" | VID | extract_from_folder_name | High |
| Nov25 | "Fin Nov25" | FIN | extract_from_folder_name | High |
| Nov25 | "Content Nov25" | [TBD] | [Decision needed] | Low |
| ENTITIES | "AI" | AIA | map_entities_name_to_iso | High |
| ENTITIES | "Design" | DGN | map_entities_name_to_iso | High |
| ENTITIES | "Dev" | DEV | map_entities_name_to_iso | High |
| ENTITIES | "HR" | HRM | map_entities_name_to_iso | High |
| ENTITIES | "LG" | LGN | map_entities_name_to_iso | High |
| ENTITIES | "Sales" | SLS | map_entities_name_to_iso | High |
| ENTITIES | "Video" | VID | map_entities_name_to_iso | High |
| ENTITIES | "Finance" | FIN | map_entities_name_to_iso | High (when added) |

---

## Recommendations

### Immediate Actions (Next 1-2 Weeks)
- [ ] **Add Finance department to ENTITIES**
  - Add "Finance" to ENTITIES department enum
  - Add "FIN" ISO code to ENTITIES TAXONOMY
  - Update department documentation
  
- [ ] **Create department normalization mapping table**
  - Document all Finance → ISO code mappings
  - Document Nov25 → ISO code mappings
  - Document profession-based mapping for managers
  
- [ ] **Decide on Content department**
  - Option A: Add Content department (CNT code)
  - Option B: Map Content to Sales (SLS)
  - Option C: Keep as documentation-only
  - Document decision

### Short-Term Actions (Next 30-90 Days)
- [ ] **Implement department normalization functions**
  - Create `normalize_department_finance_to_iso` function
  - Create `normalize_department_nov25_to_iso` function
  - Create `map_managers_by_profession` function
  - Create `map_entities_name_to_iso` function
  
- [ ] **Update all systems to use ISO codes**
  - Update Finance CSV to include ISO codes
  - Update ENTITIES to use ISO codes consistently
  - Update Nov25 folder references to ISO codes
  
- [ ] **Assign departments to empty fields**
  - Assign departments to 21 accounts with empty department field
  - Use tool usage, owner, or manual assignment
  - Document assignment rules

### Long-Term Actions (Beyond 3 Months)
- [ ] **Standardize department naming across all systems**
  - Migrate Finance to use ISO codes
  - Migrate Nov25 to use ISO codes
  - Update all references and documentation
  
- [ ] **Create department management dashboard**
  - Visualize department distribution
  - Track department changes over time
  - Monitor department assignments

---

## Next Steps

**For Implementation:**
1. Add Finance department to ENTITIES
2. Create department normalization mapping table
3. Implement normalization functions
4. Update all systems to use ISO codes
5. Assign departments to empty fields

**For Future Research:**
- Department restructuring analysis (if needed)
- Historical department migration (if needed)

---

## Related Research

**Related Blocks:**
- Block 003: Employee Data Integration Patterns (department mapping)
- Block 004: Account Subscription Management (department assignments)

**Related Reports:**
- `Finance 2025 - Copy/Fin_Dec25/03_department_structure_analysis_results.yaml` - Department analysis
- `Finance 2025 - Copy/Fin_Dec25/Fields_Data/department_values.yaml` - Department mapping

**Related Documentation:**
- `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md` - ISO code registry
- `ENTITIES/TAXONOMY/TAX-002_Task_Managers/Taxonomy_ISO_Code_Registry.md` - Task Manager ISO codes

---

## Notes

**Key Insights:**
- Department naming varies significantly across systems
- ENTITIES TAXONOMY ISO codes provide canonical standard
- Finance "managers" department requires profession-based mapping
- Content department needs organizational decision

**Normalization Complexity:**
- **Low Complexity:** Direct mappings (designers → DGN, developers → DEV)
- **Medium Complexity:** Special cases (crm → DEV, marketers → SLS)
- **High Complexity:** Profession-based mapping (managers department)

**Implementation Priority:**
1. **Critical:** Add Finance department to ENTITIES (blocks integration)
2. **High:** Create department normalization functions (enables integration)
3. **High:** Profession-based mapping for managers (ensures accuracy)
4. **Medium:** Assign departments to empty fields (improves data quality)
5. **Low:** Standardize naming across systems (operational excellence)

**Risk Factors:**
- **Data Quality Risk:** 21 accounts with empty department field
- **Mapping Accuracy Risk:** Managers department needs profession-based mapping
- **Consistency Risk:** Multiple naming conventions cause confusion
- **Integration Risk:** Missing Finance department blocks integration

---

**Block Status:** Complete  
**Completion Date:** 2025-11-21  
**Next Review:** After Finance department added to ENTITIES

