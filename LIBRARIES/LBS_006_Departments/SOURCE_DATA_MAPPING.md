# Source Data Mapping for Departments

**Source Location:** `C:\Users\Dell\Dropbox\Overview\`  
**Created:** November 25, 2025  
**Last Updated:** November 25, 2025

---

## 📋 Overview

This document maps the source data files in the `Overview/` folder to the department structure in `ENTITIES/LIBRARIES/LBS_006_Departments/By_Department/`.

---

## 📊 Department Source Files Mapping

| Department Code | Department Name | Source File | Status | Notes |
|----------------|----------------|-------------|--------|-------|
| AI | Artificial Intelligence | `AI_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| DESIGN | Designers | `Design_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| DGN | Designers (alt) | `Design_Department_Deep_Analysis.md` | ✅ Available | Same as DESIGN |
| DEV | Developers | `Dev_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| FIN | Finance | `Finance_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| HR | Human Resources | `HR_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| LG | Lead Generation | `LG_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| SALES | Sales | `Sales_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |
| SMM | Social Media Management | `Nov25/SMM Nov25/README.md` | ✅ Available | Different source location |
| VIDEO | Video Editors | `Video_Department_Deep_Analysis.md` | ✅ Available | Complete analysis |

---

## 📁 Source Files Structure

### Overview Folder Contents

```
Overview/
├── AI_Department_Deep_Analysis.md              ✅
├── AI_Department_Analysis_Process_Log.md       📝 (Process log)
├── Design_Department_Deep_Analysis.md          ✅
├── Design_Department_Analysis_Process_Log.md   📝 (Process log)
├── Dev_Department_Deep_Analysis.md             ✅
├── Dev_Department_Analysis_Process_Log.md       📝 (Process log)
├── Finance_Department_Deep_Analysis.md         ✅
├── HR_Department_Deep_Analysis.md              ✅
├── HR_Department_Analysis_Process_Log.md       📝 (Process log)
├── LG_Department_Deep_Analysis.md              ✅
├── LG_Department_Analysis_Process_Log.md       📝 (Process log)
├── Sales_Department_Deep_Analysis.md           ✅
├── Video_Department_Deep_Analysis.md           ✅
├── Video_Department_Analysis_Process_Log.md     📝 (Process log)
├── Analysis_Summary_and_Key_Findings.md       📊 (Summary)
└── Nov25_ENTITIES_Relationship_Analysis.md     🔗 (Relationships)
```

---

## 📝 Data Extraction Strategy

### For Each Department Deep Analysis File

Each `*_Department_Deep_Analysis.md` file contains structured sections that map to our JSON schema:

#### 1. Overview Section → `overview.json`
- Mission statement
- Department overview
- Key responsibilities
- KPIs and metrics

#### 2. Team Composition Section → `team_composition.json`
- Employee list
- Roles and responsibilities
- Team structure
- Skills and competencies

#### 3. Tools Section → `tools_reference.json`
- Tools used by department
- Map to `LIBRARIES/LBS_003_LBS_003_Tools/` structure
- Tool categories

#### 4. Objects Section → `objects_reference.json`
- Objects/deliverables worked with
- Map to `LIBRARIES/Objects/` structure
- Object types

#### 5. Task Managers Section → `task_managers_reference.json`
- Workflows
- Task templates
- Step templates
- Project templates
- Map to `TASK_MANAGERS/` structure

#### 6. Metrics Section → `metrics.json`
- KPIs
- Performance metrics
- Statistics

#### 7. Projects Section → `projects.json`
- Active projects
- Project status
- Project details

#### 8. Structure Section → `structure.json`
- Folder structure patterns
- File organization
- Naming conventions

#### 9. Integration Section → `integration.json`
- Cross-department dependencies
- Integration points
- Collaboration patterns

---

## 🔄 Extraction Process

### Step 1: Parse Deep Analysis File
- Read the markdown file
- Identify sections using headers
- Extract structured data

### Step 2: Map to JSON Schema
- Transform markdown sections to JSON
- Validate against schema
- Cross-reference with LIBRARIES

### Step 3: Create Reference Files
- Link to existing LIBRARIES structure
- Link to TASK_MANAGERS structure
- Avoid duplication

### Step 4: Validate
- Check JSON validity
- Verify cross-references
- Ensure consistency

---

## 📊 Coverage Status

### Departments with Source Data
- ✅ AI - `AI_Department_Deep_Analysis.md`
- ✅ DESIGN - `Design_Department_Deep_Analysis.md`
- ✅ DEV - `Dev_Department_Deep_Analysis.md`
- ✅ FIN - `Finance_Department_Deep_Analysis.md`
- ✅ HR - `HR_Department_Deep_Analysis.md`
- ✅ LG - `LG_Department_Deep_Analysis.md`
- ✅ SALES - `Sales_Department_Deep_Analysis.md`
- ✅ VIDEO - `Video_Department_Deep_Analysis.md`

### Departments Needing Alternative Sources
- ⚠️ SMM - Using `Nov25/SMM Nov25/README.md` (different format)
- ⚠️ DGN - Can use `Design_Department_Deep_Analysis.md` (same as DESIGN)

**Total Coverage:** 8/10 departments have Deep Analysis files (80%)

---

## 🎯 Next Steps

1. **Create Extraction Script**
   - Parse markdown files
   - Extract structured data
   - Generate JSON files

2. **Start with One Department**
   - Use AI department as pilot
   - Validate extraction process
   - Refine script

3. **Batch Process Remaining**
   - Process all 8 Deep Analysis files
   - Handle SMM separately (different format)
   - Create DGN from DESIGN data

4. **Validate and Cross-Reference**
   - Check all JSON files
   - Verify LIBRARIES references
   - Ensure TASK_MANAGERS links

---

## 📚 Related Documentation

- `ARCHITECTURE_PLAN.md` - Overall architecture
- `DATA_POPULATION_STATUS.md` - Current status
- `Overview/*_Department_Deep_Analysis.md` - Source files
- `Overview/*_Department_Analysis_Process_Log.md` - Process logs

---

**Last Updated:** November 25, 2025  
**Status:** Ready for data extraction

