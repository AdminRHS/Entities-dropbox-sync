# Taxonomy Quick Start Guide

**Read this first for a fast overview, then refer to `taxonomy_complete_guide.md` for full details.**

---

## What is Taxonomy?

Taxonomy is your organization's **universal classification system** that:
- Assigns unique IDs to everything (tools, objects, actions, workflows, etc.)
- Creates relationships between entities
- Enables AI automation through consistent structure
- Extracts knowledge from videos and documents

---

## Quick Facts

- **2 main taxonomies:** LIBRARIES (what you work with) and TASK_MANAGERS (how you work)
- **752+ entities** classified and cross-referenced
- **421 task templates** aligned with taxonomy
- **Video-to-taxonomy pipeline** extracts knowledge from videos automatically
- **40+ prompts** for taxonomy analysis and updates

---

## Key Locations

| What You Need | Where To Find It |
|---------------|------------------|
| **Central Hub** | `ENTITIES/TAXONOMY/README.md` |
| **Tools** | `ENTITIES/LIBRARIES/Tools/AI_Tools/` |
| **Objects** | `ENTITIES/LIBRARIES/Responsibilities/Objects/` |
| **Workflows** | `ENTITIES/TASK_MANAGERS/Workflows/` |
| **Video Prompts** | `ENTITIES/PROMPTS/PMT-004_*.md` |
| **Master Lists** | `ENTITIES/TAXONOMY/TAX-001_Libraries/` |
| **Full Guide** | `ENTITIES/TASK_MANAGERS/RESEARCHES 2/documentation/taxonomy_complete_guide.md` |

---

## ISO Codes Cheat Sheet

**LIBRARIES (Content):**
- **RSP** = Responsibilities (193)
- **ACT** = Actions (429 verbs)
- **OBJ** = Objects (50+ deliverables)
- **TOL** = Tools (200+)
- **SKL** = Skills (28+)
- **PRF** = Professions (17)

**TASK_MANAGERS (Workflows):**
- **PRT** = Project Templates (9)
- **MLT** = Milestone Templates (9)
- **TST** = Task Templates (71)
- **WRF** = Workflows (20)
- **PMT** = Prompts (100+)
- **RSR** = Research (50+)

**Departments:**
- **AIA/AID** = AI & Automation
- **DEV** = Development
- **DGN** = Design
- **VID** = Video
- **HRM** = HR
- **LGN** = Lead Generation
- **SLS** = Sales

---

## How To Use Video Taxonomy

### Fast Method (2-4 hours per video):

1. **Transcribe Video** using PMT-004
   - Location: `ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md`
   - Save to: `02_TRANSCRIPTIONS/Video_XXX.md`

2. **Full Integration** using PMT-009
   - Location: `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`
   - This prompt does everything: analysis, gap detection, JSON creation, cross-referencing
   - Save extractions to appropriate folders

3. **Generate Report**
   - Create: `03_ANALYSIS/Video_XXX_Library_Mapping_Report.md`
   - Document all changes

### What Gets Extracted:

- **Tools** → JSON files in `ENTITIES/LIBRARIES/Tools/AI_Tools/`
- **Objects** → Entries in `ENTITIES/LIBRARIES/Responsibilities/Objects/*.json`
- **Workflows** → JSON files in `ENTITIES/TASK_MANAGERS/Workflows/`
- **Professions** → JSON files in `ENTITIES/LIBRARIES/Professions/`
- **Skills** → Entries in `ENTITIES/LIBRARIES/Skills/Master/all_skills.json`
- **Actions** → Updated in `ENTITIES/LIBRARIES/Responsibilities/Actions/Actions_Master.json`

---

## How To Add A New Tool

Quick steps:

1. **Check if exists:**
   ```bash
   cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"
   ls *.json | grep -i "tool_name"
   ```

2. **Assign ID:**
   - Open: `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_Master_List.csv`
   - Find last TOL-### ID
   - Use next number (e.g., TOL-046)

3. **Create JSON file:**
   - Use template from full guide (Appendix B)
   - Save as: `Tool_Name.json`

4. **Update master list:**
   - Add row to `Libraries_Master_List.csv`

5. **Cross-reference:**
   - Link to objects it creates
   - Link to professions that use it
   - Link to workflows it's part of

**Full details:** See "How to Update Taxonomy → Scenario 1" in `taxonomy_complete_guide.md`

---

## Key Scripts

### taxonomy_lookup.js

**Location:** `Design Nov25/Safonova Eleonora/.../scripts/taxonomy_lookup.js`

**What it does:** Looks up tool data and converts to app format

**Usage:**
```javascript
const { getToolData } = require('./taxonomy_lookup.js');

const toolData = getToolData('GLIF', {
  borderColor: '#28a745',
  department: ['Developers']
}, 'G:\\Job\\REMS\\Dropbox');
```

---

## Essential Prompts

| Prompt | Purpose | Time |
|--------|---------|------|
| **PMT-004** | Transcribe video | 30-60 min |
| **PMT-009** | Full taxonomy integration | 2-4 hours |
| **PMT-006** | Quick video analysis | 30 min |

All prompts in: `ENTITIES/PROMPTS/`

---

## Common Tasks

### Find a Tool
```bash
cd "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\Tools\AI_Tools"
ls *.json | grep -i "tool_name"
```

### Find Last ID
```bash
grep "^TOL-" Libraries_Master_List.csv | tail -1
```

### Validate JSON
```bash
jq . file.json
```

### Search for Reference
```bash
grep -r "TOL-045" .
```

---

## Best Practices

**DO:**
- ✅ Always assign sequential IDs
- ✅ Create bidirectional cross-references
- ✅ Update master lists immediately
- ✅ Validate JSON before saving
- ✅ Document all changes in reports

**DON'T:**
- ❌ Skip ID numbers
- ❌ Create one-way links only
- ❌ Delay master list updates
- ❌ Save invalid JSON
- ❌ Forget to cross-reference

---

## Need Help?

**For detailed information, see:**
- **Full Guide:** `taxonomy_complete_guide.md` (~100 pages, comprehensive)
- **Central Hub:** `ENTITIES/TAXONOMY/README.md`
- **Video Workflow:** `ENTITIES/TAXONOMY/TAX-003_Video_Processing/PMT-009_Taxonomy_Integration.md`
- **ISO Codes:** `ENTITIES/TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`

**Specific questions?**
- How taxonomy works → Full Guide: "What is Taxonomy" section
- How to generate → Full Guide: "How to Generate Taxonomy" section
- How to update → Full Guide: "How to Update Taxonomy" section
- Scripts reference → Full Guide: "Taxonomy Scripts and Tools" section
- Prompts library → Full Guide: "Prompts Library" section
- What's captured → Full Guide: "Information Captured by Taxonomy" section
- Troubleshooting → Full Guide: "Troubleshooting" section

---

**Created:** 2025-12-04
**Location:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\TAXONOMY_QUICK_START.md`
**Related:** `taxonomy_complete_guide.md` (full documentation)
