# MAIN_PROMPT v5 - Modular Architecture

## Overview

MAIN_PROMPT v5 is the master prompt for AI-assisted call organization, meeting analysis, and taxonomy-driven documentation at Remote Helpers.

**Version:** 5.0
**Last Updated:** 2025-11-15
**Modular Files:** ~50 files across 5 folders
**Total Libraries Integrated:** 12
**Status:** 🚧 In Development

---

## Folder Structure

```
MAIN_PROMPT_v5_Modular/
├── README.md (this file)
│
├── 00_Core/                          # Company context and core data (5 files)
│   ├── 01_Purpose_Vision.md
│   ├── 02_Company_Context.md
│   ├── 03_Employee_Directory.md      # 32 employees
│   ├── 04_Project_Directory.md       # 31+ projects
│   └── 05_AI_Instructions.md
│
├── 01_Library_Integration/           # 12 LIBRARIES entity integrations (13 files)
│   ├── README.md
│   ├── 01_Actions_Library.md         # 429 actions
│   ├── 02_Objects_Library.md         # 36 objects
│   ├── 03_Processes_Library.md       # 428 processes
│   ├── 04_Results_Library.md         # 432 results
│   ├── 05_Skills_Library.md          # 12+ skills
│   ├── 06_Responsibilities_Library.md
│   ├── 07_Products_Library.md        # 39 products
│   ├── 08_Services_Library.md        # 7 categories
│   ├── 09_Parameters_Library.md      # 10,596+ parameters
│   ├── 10_Professions_Library.md     # 12+ professions
│   ├── 11_Tools_Library.md           # 75+ tools
│   ├── 12_Prompts_Library.md
│   └── 13_Taxonomy_Framework.md
│
├── 02_Output_Templates/              # 21 meeting output sections (22 files)
│   ├── README.md
│   ├── 01_Meeting_Metadata.md
│   ├── 02_Executive_Summary.md
│   ├── 03_Action_Items_Tasks.md      # ⭐ Actions, Objects, Skills, Responsibilities
│   ├── 04_Projects_Features.md       # ⭐ Products, Services
│   ├── 05_Workflows_Processes.md     # ⭐ Processes, Results, Steps
│   ├── 06_Rules_Best_Practices.md    # ⭐ Parameters
│   ├── 07_Problems_Solutions.md
│   ├── 08_Tools_Resources.md         # ⭐ Tools
│   ├── 09_Technical_Architecture.md  # ⭐ Tools, Processes
│   ├── 10_Decisions_Log.md
│   ├── 11_Documentation_Gaps.md
│   ├── 12_Communication_Announcements.md
│   ├── 13_Blockers_Dependencies.md   # ⭐ Processes, Results
│   ├── 14_Insights_Lessons.md
│   ├── 15_Analogies_Frameworks.md
│   ├── 16_Employee_Team_Context.md   # ⭐ Professions, Skills, Responsibilities
│   ├── 17_Lead_Gen_Sales_Context.md  # ⭐ Services, Products, Processes
│   ├── 18_Design_Creative_Context.md # ⭐ Objects, Products, Tools
│   ├── 19_Development_Technical_Context.md # ⭐ Tools, Processes, Objects
│   ├── 20_Onboarding_Training_Context.md # ⭐ Skills, Responsibilities, Professions
│   └── 21_Follow_Up_Items.md         # ⭐ Actions, Tasks
│
├── 03_Processing_Rules/              # Entity recognition patterns (6 files)
│   ├── README.md
│   ├── 01_Participant_Identification.md
│   ├── 02_Project_Recognition.md
│   ├── 03_Entity_Recognition.md      # All 12 libraries
│   ├── 04_Language_Handling.md
│   ├── 05_Vocabulary_Recognition.md
│   └── 06_Cross_Reference_Rules.md
│
├── 04_Usage/                         # Documentation and guides (7 files)
│   ├── 01_Usage_Instructions.md
│   ├── 02_Examples.md
│   ├── 03_Tips_Best_Practices.md
│   ├── 04_Advanced_Features.md
│   ├── 05_Maintenance_Guide.md
│   ├── 06_CHANGELOG.md
│   └── 07_Migration_Guide.md         # v4 → v5
│
└── scripts/                          # Assembly scripts (4 files)
    ├── README.md
    ├── assemble_full_prompt.py       # Generate MAIN_PROMPT_v5.md
    ├── assemble_department.py        # Department-specific versions
    └── assemble_lightweight.py       # Minimal version
```

**Legend:** ⭐ = Heavy library integration

---

## Library Statistics (Current as of 2025-11-15)

| Library | Count | Files | Key Use Cases |
|---------|-------|-------|---------------|
| **Actions** | 429 | Actions_Master.json + Data Operations | Action Items, Follow-ups, Task creation |
| **Objects** | 36 | 4 collections | Design deliverables, Documents, Video objects |
| **Processes** | 428 | Processes_Master.json + Workflows | Workflow documentation, Process mapping |
| **Results** | 432 | Results_Master.json | Outcomes, Deliverables, Success metrics |
| **Skills** | 12+ | By department | Team context, Onboarding, Training |
| **Responsibilities** | Multiple | responsibilities.json | Role clarification, Team assignments |
| **Products** | 39 | Products_Master.json | Project features, Product discussions |
| **Services** | 7 categories | Service files | Service offerings, Sales context |
| **Parameters** | 10,596+ | parameters.json | Rules, Best practices, Standards |
| **Professions** | 12+ | Individual files | Employee context, Role identification |
| **Tools** | 75+ | Categorized | Tool mentions, Technical architecture |
| **Prompts** | Multiple | Categories | Prompt references, Workflow automation |

---

## Assembly Instructions

### Generate Monolithic Version

To create a single `MAIN_PROMPT_v5.md` file from all modular files:

```bash
cd scripts
python assemble_full_prompt.py
```

**Output:** `../MAIN_PROMPT_v5.md` (in Core folder)

### Generate Department-Specific Version

```bash
cd scripts
python assemble_department.py --dept AI
```

**Options:** AI, Video, Sales, Design, Dev, HR, LG, AI

### Generate Lightweight Version

```bash
cd scripts
python assemble_lightweight.py
```

Creates minimal version without extensive examples.

---

## Quick Start

### For First-Time Users

1. **Read in Order:**
   - Start with `00_Core/` files to understand company context
   - Review `01_Library_Integration/README.md` for taxonomy overview
   - Check `02_Output_Templates/README.md` for output format
   - Review `03_Processing_Rules/README.md` for recognition logic
   - Read `04_Usage/01_Usage_Instructions.md` for workflow

2. **Process a Meeting:**
   - Follow workflow in `04_Usage/01_Usage_Instructions.md`
   - Reference output templates in `02_Output_Templates/`
   - Apply recognition rules from `03_Processing_Rules/`
   - Use library integration guides in `01_Library_Integration/`

3. **Generate Output:**
   - Use templates as structure
   - Match entities using recognition patterns
   - Cross-reference between libraries
   - Validate using checklists in each template

### For v4 Users

- See `04_Usage/07_Migration_Guide.md` for differences
- All v4 functionality is preserved in v5
- New modular structure improves maintainability
- Can generate monolithic version identical to v4 format

---

## Key Improvements in v5

### 1. Modular Architecture
- **Before (v4):** Single 2,538-line file
- **After (v5):** ~50 focused files across 5 folders
- **Benefit:** Easier to maintain, update, and navigate

### 2. Enhanced Library Integration
- **Before (v4):** Basic library mentions
- **After (v5):** 12 dedicated integration modules with:
  - Current statistics from actual library files
  - Detailed recognition patterns
  - Comprehensive examples with real entity IDs
  - Cross-reference mapping

### 3. Granular Templates
- **Before (v4):** 2 large template files (sections 1-11, 12-21)
- **After (v5):** 21 individual template files
- **Benefit:** Update one section without affecting others

### 4. Processing Rules
- **Before (v4):** Embedded in main document
- **After (v5):** Dedicated 6-file module
- **Benefit:** Clear, focused recognition logic

### 5. Assembly System
- **New in v5:** Python scripts to generate variations
- **Benefit:** Modular for maintenance, monolithic for deployment

---

## Maintenance

### Monthly Updates
- **Employee Directory:** Update `00_Core/03_Employee_Directory.md`
- **Verify Count:** Ensure 32 employees current

### Weekly Updates
- **Project Directory:** Update `00_Core/04_Project_Directory.md`
- **Add New Projects:** Follow naming conventions

### Library Statistics Sync
- **When:** Whenever LIBRARIES entities are updated
- **How:** Update relevant file in `01_Library_Integration/`
- **Re-generate:** Run assembly script to update monolithic version

### Quarterly Review
- **Examples:** Update in output templates
- **Statistics:** Verify all library counts
- **Migration Guide:** Update with new patterns

---

## File Count

| Folder | Files | Status |
|--------|-------|--------|
| 00_Core | 5 | 🚧 Pending |
| 01_Library_Integration | 13 | 🚧 Pending |
| 02_Output_Templates | 22 | 🚧 Pending |
| 03_Processing_Rules | 7 | 🚧 Pending |
| 04_Usage | 7 | 🚧 Pending |
| scripts | 4 | 🚧 Pending |
| **Total** | **58** | **🚧 In Development** |

---

## Project Tracking

**Project ID:** PROJ-AI-NMP-001
**Project Location:** `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Projects\PROJ-AI-NMP-001_Next_Main_Prompt_Version\`

**Milestones:**
- ✅ MIL-001: Folder Structure Creation (Complete)
- 🚧 MIL-002: Core Modules
- ⏳ MIL-003: Library Integration Modules
- ⏳ MIL-004: Output Templates
- ⏳ MIL-005: Processing Rules
- ⏳ MIL-006: Usage & Maintenance Docs
- ⏳ MIL-007: Assembly System
- ⏳ MIL-008: Validation & QA

---

## Related Resources

### Source Files
- **MAIN_PROMPT v4:** `../MAIN_PROMPT_v4.md`
- **Meta-Prompt:** `../CREATE_MAIN_PROMPT_v5.md`

### LIBRARIES Location
- **Root:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\`
- **Actions:** `LIBRARIES/Responsibilities/Actions/`
- **Objects:** `LIBRARIES/Responsibilities/Objects/`
- **Processes:** `LIBRARIES/Processes/`
- **Results:** `LIBRARIES/Results/`
- **Skills:** `TALENTS/Skills/` ⚠️ *Migrated to TALENTS (2025-01-16)*
- **Parameters:** `LIBRARIES/Parameters/`
- **Tools:** `LIBRARIES/Tools/`
- And all other libraries...

---

## Notes

- This is a **work in progress** (as of 2025-11-15)
- All statistics will be verified from actual library files during MIL-003
- Both modular and monolithic versions will be maintained
- v4 functionality is 100% preserved in v5

---

## Version History

**Version 5.0** (2025-11-15 - In Development)
- Initial modular architecture created
- Folder structure established
- Enhanced library integration planned
- Assembly system in development

**Version 4.0** (2025-01-27)
- Previous monolithic version
- See `MAIN_PROMPT_v4.md` for details

---

**Maintained By:** AI Department
**Project Manager:** ALX
**Created:** 2025-11-15
**Last Updated:** 2025-11-15
