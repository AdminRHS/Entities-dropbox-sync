# RESPONSIBILITIES - Integrated Core System

**Entity Type:** RESPONSIBILITIES
**Location:** `LIBRARIES/Responsibilities`
**Purpose:** Atomic units of work composed of Actions, Objects, and Parameters
**Last Updated:** 2025-11-22 (Major Integration Complete)

---

## 📋 Overview

Responsibilities are the **atomic units of work** in the LIBRARIES ecosystem. Each responsibility represents a distinct task or capability that can be performed by a profession using specific tools.

### Formula
```
Responsibility = Action + Object + [Parameters]
```

### Example
```
"extract videos" = extract (Action) + videos (Object) + [format, quality, duration] (Parameters)
```

---

## 🗂️ Directory Structure

```
Responsibilities/
├── Core/                           # Master files & indexes
│   ├── responsibilities_master.json    # 193 core responsibilities
│   ├── phrase_matching_index.json      # 209 phrase patterns
│   ├── action_variants_map.json        # 57 action variants
│   └── object_variants_map.json        # 169 object variants
│
├── Actions/                        # From LBS_001_Actions (429 actions)
│   ├── Master/
│   │   └── actions_master.json         # All 429 actions with metadata
│   ├── By_Domain/                      # Actions grouped by domain
│   ├── Data_Operations/                # Data-specific actions
│   └── Archive/                        # Legacy action files
│
├── Objects/                        # From LBS_002_Objects (50+ objects)
│   ├── object_types.json               # Master object catalog
│   ├── AI_Objects/                     # AI & automation objects
│   ├── Video_Objects/                  # Video production objects
│   ├── Design_Objects/                 # Design deliverables
│   ├── Development_Objects/            # Development artifacts
│   ├── Lead_Generation_Objects/        # LG deliverables
│   └── Marketing_Objects/              # Marketing materials
│
├── Parameters/                     # From LBS_007_Parameters (200+ parameters)
│   ├── organized_by_profession/        # 8 profession-specific files
│   │   ├── graphic_designer_parameters.json (25)
│   │   ├── back_end_developer_parameters.json (30)
│   │   ├── lead_generator_parameters.json (28)
│   │   └── ... (5 more)
│   └── organized_by_department/        # 4 department groups
│       ├── designers_parameters.json
│       ├── developers_parameters.json
│       ├── managers_parameters.json
│       └── marketers_parameters.json
│
├── By_Department/                  # Department-specific responsibilities
│   ├── AI_Responsibilities.json        # 80 AI responsibilities
│   ├── DEV_Responsibilities.json       # 34 dev responsibilities
│   ├── HR_Responsibilities.json        # 6 HR responsibilities
│   └── LG_Responsibilities.json        # 64 LG responsibilities
│
├── Integration/                    # Cross-reference mappings
│   ├── parameter_object_mapping.json   # 7,321 mappings
│   ├── parameter_views_by_profession.json
│   ├── phrase_combinations.json        # Action-object combinations
│   └── unique_combinations.json
│
└── _ARCHIVE/                       # Legacy files
    ├── extracted_pairs_raw.json
    └── task_manager_migration_log.json
```

---

## 🔗 Integration Points

### With TALENTS/Skills
```
Skills = Responsibilities + Tools + Proficiency
```
- Skills reference responsibilities from this catalog
- Example: "developed features in React" (SKL-030) uses "develop" action + "features" object

### With LBS_003_Tools
```
Tools enable specific Actions on Objects
```
- Figma enables "create" + "UI mockups"
- GitHub enables "manage" + "code"
- CRM enables "track" + "leads"

### With LBS_005_Professions
```
Professions perform specific Responsibilities
```
- Frontend Developer: Responsibilities using React, Vue, Angular
- Lead Generator: Responsibilities using LinkedIn, CRM
- Designer: Responsibilities using Figma, Photoshop

### With LBS_006_Departments
```
Departments own specific Objects and Responsibilities
```
- AI Department: 80 responsibilities (41.5%)
- Development: 34 responsibilities (17.6%)
- Lead Generation: 64 responsibilities (33.2%)

---

## 📊 Statistics

### Responsibilities
- **Core:** 193 responsibilities
- **Department-Specific:** 184 responsibilities
- **Total:** 377 responsibilities

### Actions
- **Total:** 429 actions
- **Command Verbs:** 143 (create, update, delete, configure, execute...)
- **Process Verbs:** 143 (analyze, review, transform, monitor...)
- **Result Verbs:** 143 (generate, deliver, report, publish...)

### Objects
- **Total:** 50+ objects across 17 collections
- **AI Objects:** 29 (58% of AI department work)
- **Video Objects:** 23 (46% of video department work)
- **Design Objects:** 24 (48% of design department work)
- **Development Objects:** 12 (24% of dev department work)

### Parameters
- **Total:** 200+ parameters
- **By Profession:** 8 profession files
- **By Department:** 4 department groups
- **Mapped to Objects:** 7,321 mappings (30.9% of possible combinations)

---

## 🎯 Usage Examples

### 1. Finding a Responsibility
```json
{
  "id": "RESP-AI-001",
  "primary_phrase": "extract videos",
  "action_base": "extract",
  "object_base": "videos",
  "departments": "AI",
  "frequency": 6
}
```

### 2. Decomposing into Components
```
Responsibility: "extract videos"
  ↓
Action: "extract" (from Actions/Master/actions_master.json)
  → ACTION-084: extract
  → Forms: extracting (process), extracted (result)
  ↓
Object: "videos" (from Objects/Video_Objects/)
  → Type: Video Deliverables
  → Variants: video files, video content, footage
  ↓
Parameters: (from Integration/parameter_object_mapping.json)
  → format: mp4, mov, avi
  → quality: 1080p, 4K, 8K
  → duration: short-form, long-form
```

### 3. Building a Skill
```
Skill: "extracted video testimonials using Adobe Premiere"
  ↓
Responsibility: "extract videos" (RESP-AI-001)
+ Tool: Adobe Premiere (LBS_003_Tools/Video_Editing/)
+ Parameter: object_type = "testimonials"
= Skill (SKL-XXX)
```

---

## 🔍 Lookup Mechanisms

### 1. Phrase Matching
Use `phrase_matching_index.json` for fuzzy matching:
```
Input: "pull out videos"
→ Matches: "extract videos" (RESP-AI-001)
```

### 2. Action Variants
Use `action_variants_map.json` for synonyms:
```
"create" → ["make", "build", "generate", "produce"]
"analyze" → ["examine", "review", "inspect", "evaluate"]
```

### 3. Object Variants
Use `object_variants_map.json` for alternatives:
```
"videos" → ["video files", "footage", "clips", "recordings"]
"leads" → ["prospects", "contacts", "opportunities"]
```

### 4. Parameter-Object Mapping
Use `Integration/parameter_object_mapping.json`:
```
Object: "UI mockups"
→ Parameters:
  - style: minimalist, modern, corporate
  - fidelity: low-fi, high-fi, wireframe
  - platform: web, mobile, desktop
```

---

## 🚀 Migration History

### 2025-11-22: Major Integration
**What Changed:**
- ✅ LBS_001_Actions → Responsibilities/Actions/
- ✅ LBS_002_Objects → Responsibilities/Objects/
- ✅ LBS_007_Parameters → Responsibilities/Parameters/
- ✅ _ARCHIVE/By_Department → By_Department/ (promoted)
- ✅ Integration files → Integration/ (organized)

**Why:**
- **Conceptual alignment:** Responsibilities = Actions + Objects + Parameters
- **Single source of truth:** All components in one place
- **Cleaner architecture:** Responsibilities as the foundational layer
- **Better discoverability:** Hierarchical structure matches mental model

**Impact:**
- 40 files updated with new paths
- 137 path references corrected
- Validation scripts updated
- Documentation consolidated

### 2025-11-17: Responsibilities Ecosystem Consolidation
- Unified action/object/parameter architecture
- Created phrase matching system
- Built cross-reference mappings

---

## 📚 Related Documentation

### In This Directory
- [INTEGRATION_COMPLETE_REPORT.md](./INTEGRATION_COMPLETE_REPORT.md) - Original consolidation report
- [README.md](./README.md) - Original responsibilities documentation

### In LIBRARIES/Taxonomy
- [Libraries_Hierarchy_Tree.md](../Taxonomy/Libraries_Hierarchy_Tree.md) - Full hierarchy
- [Libraries_Master_List.csv](../Taxonomy/Libraries_Master_List.csv) - Entity registry
- [Libraries_ISO_Code_Registry.md](../Taxonomy/Libraries_ISO_Code_Registry.md) - ISO codes

### External References
- [TALENTS/Skills/README.md](../../TALENTS/Skills/README.md) - Skills catalog
- [LBS_003_Tools/README.md](../LBS_003_Tools/README.md) - Tools catalog
- [LBS_005_Professions/README.md](../LBS_005_Professions/README.md) - Professions

---

## 🛠️ Validation & Quality

### Validation Scripts
- `validate_ecosystem.py` - Check integrity of all components
- `create_parameter_mapping.py` - Generate/update parameter-object mappings

### Validation Reports
- `ecosystem_validation_report.json` - Latest validation status
- `responsibility_usage_report.json` - Usage analytics

### Quality Metrics
- ✅ 193 core responsibilities validated
- ✅ 429 actions with full metadata
- ✅ 7,321 parameter-object mappings
- ✅ 209 phrase patterns for fuzzy matching
- ✅ Cross-reference integrity: 100%

---

## 🎓 Best Practices

### 1. When to Use Responsibilities
- Building task templates
- Defining job requirements
- Creating skill assessments
- Automating workflow generation

### 2. When to Use Actions
- Standardizing verb usage
- Building command interfaces
- Creating action logs/audit trails

### 3. When to Use Objects
- Defining deliverables
- Cataloging work products
- Specifying inputs/outputs

### 4. When to Use Parameters
- Adding specificity to tasks
- Creating filters/search criteria
- Building configuration templates

---

## 📞 Integration Support

### For Questions About:
- **Responsibilities structure:** See this README
- **Actions catalog:** See `Actions/Master/README.md`
- **Objects taxonomy:** See `Objects/README.md`
- **Parameters system:** See `Parameters/README.md`
- **Overall LIBRARIES:** See `../README.md`

### For Updates/Changes:
1. Update master files in respective folders
2. Run validation scripts
3. Update integration mappings
4. Regenerate reports
5. Update documentation

---

**Document Status:** Active
**Maintained By:** LIBRARIES Taxonomy Team
**Last Validated:** 2025-11-22
**Next Review:** As needed (track via `ecosystem_validation_report.json`)
