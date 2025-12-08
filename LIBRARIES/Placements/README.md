# Placements Library (LIB.PLM)

**Library ID:** LIB.PLM
**Entity:** Libraries (LBS)
**Type:** Location/Path References
**Status:** Active
**Created:** 2025-12-08
**Purpose:** Standardized terminology for file locations, paths, and placement references

---

## Purpose

Replaces generic terms like "location" and "path" with standardized **"placement"** terminology across all documentation, ensuring:
- Consistent naming across system
- Clear reference to file/folder locations
- Integration with reserved words (PLACEMENT as reserved word)
- Aligned with Responsibilities library structure

---

## Terminology Standard

### Primary Term: PLACEMENT

**Use "placement" instead of:**
- ❌ location
- ❌ path
- ❌ directory
- ❌ folder path
- ❌ file path

**Correct usage:**
- ✅ placement: `C:\Users\Dell\Dropbox\ENTITIES\`
- ✅ file placement: `System/Skills/SKL.04.md`
- ✅ entity placement: `ENTITIES/Video/`
- ✅ placement reference: `../../TASKS/TASK-001.md`

---

## Reserved Word Integration

**PLACEMENT** = 11th Reserved Word

**Added to reserved vocabulary:**
```
RESEARCH   (investigation, search)
BUILD      (construction, creation)
CREATE     (generation, new item)
PROCESS    (transformation, handling)
SHARE      (distribution, communication)
EXECUTE    (running, implementation)
UPGRADE    (improvement, enhancement)
TEACH      (education, training)
REVIEW     (evaluation, checking)
MARK       (flagging, noting)
PLACEMENT  ← NEW (location, path, reference)
```

**Usage in documentation:**
```markdown
PLACEMENT for new entity: ENTITIES/Mediateka/
PLACEMENT of icon library: System/Libraries/Icons/
```

---

## Folder Structure

```
Placements/
├── README.md (this file)
├── Core/
│   ├── placement_master.json (all placements cataloged)
│   ├── placement_types.json (types of placements)
│   └── placement_patterns.json (common path patterns)
├── By_Type/
│   ├── system_placements.json (System/ paths)
│   ├── entity_placements.json (ENTITIES/ paths)
│   ├── task_placements.json (TASKS/ paths)
│   ├── report_placements.json (Reports/ paths)
│   └── workflow_placements.json (Workflows/ paths)
├── Integration/
│   ├── placement_mapping.json (maps old terms to PLACEMENT)
│   └── cross_references.json (placement relationships)
└── Symbols/
    ├── path_symbols.json (visual symbols for paths)
    └── placement_icons.json (icons for different placement types)
```

---

## Placement Types

### 1. Absolute Placements
**Definition:** Full path from drive root

**Format:** `C:\Users\Dell\Dropbox\[folder]\[subfolder]\[file]`

**Examples:**
```json
{
  "type": "absolute",
  "placement": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\Libraries\\Placements\\README.md",
  "description": "This file"
}
```

**When to use:** In scripts, configuration files, exact references

---

### 2. Relative Placements
**Definition:** Path relative to current location

**Format:** `../[folder]/[file]` or `../../[folder]/[file]`

**Examples:**
```json
{
  "type": "relative",
  "placement": "../../System/Skills/SKL.04.md",
  "from": "ENTITIES/Libraries/Placements/README.md",
  "description": "From Placements README to SKL.04"
}
```

**When to use:** In markdown links, documentation, portability

---

### 3. System Placements
**Definition:** Placements within System/ folder

**Format:** `System/[Category]/[file]`

**Categories:**
- `System/Principles/` - Core principles
- `System/Agents/` - Agent architecture
- `System/Verification/` - Verification system
- `System/Workflows/` - Workflow documents
- `System/Skills/` - Skill specifications
- `System/Integration/` - Integration documents
- `System/IDs/` - ID registries
- `System/Libraries/` - Shared libraries
- `System/Notifications/` - Notification queue

**Examples:**
```json
{
  "type": "system",
  "placement": "System/Workflows/SESSION_LIFECYCLE.md",
  "category": "Workflows",
  "description": "Session lifecycle workflow"
}
```

---

### 4. Entity Placements
**Definition:** Placements within ENTITIES/ folder

**Format:** `ENTITIES/[EntityName]/[subfolder]/[file]`

**Entity Names:**
- Libraries (LBS)
- Actions (ACT)
- Similar (SIM)
- Scraping (SCR)
- Video (VID)
- HR (Human Resources)
- Executives (EXC)
- Mediateka (planned)

**Examples:**
```json
{
  "type": "entity",
  "placement": "ENTITIES/Video/shooting_instructions.md",
  "entity": "VID",
  "description": "Video production workflow"
}
```

---

### 5. Task Placements
**Definition:** Placements for tasks and executions

**Format:**
- Tasks: `TASKS/TASK-###_Name.md`
- Executions: `AI_EXECUTIONS/EXC-###_Name.md`

**Examples:**
```json
{
  "type": "task",
  "placement": "TASKS/TASK-010_Internal_Companies_Ecosystem.md",
  "id": "TASK-010",
  "description": "Company ecosystem project"
}
```

---

### 6. Report Placements
**Definition:** Placements within Reports/ folder

**Format:** `Reports/[Category]/[date]_[name].md`

**Categories:**
- Daily/ - Session reports
- Processing/ - Line tracking
- Execution/ - Systems built
- Analytics/ - Metrics

**Examples:**
```json
{
  "type": "report",
  "placement": "Reports/Daily/2025-12-08_session_report.md",
  "category": "Daily",
  "date": "2025-12-08",
  "description": "Day 08 session report"
}
```

---

### 7. Week/Day Placements
**Definition:** Placements for day folders

**Format:** `[Month]/[Entity]/Week_##/##/[file]`

**Examples:**
```json
{
  "type": "day",
  "placement": "DEC_25/EXC/Niko_Kar_002/Week_01/07/README.md",
  "month": "DEC_25",
  "entity": "EXC",
  "employee": "Niko_Kar_002",
  "week": "01",
  "day": "07",
  "description": "Day 07 entrance document"
}
```

---

## Placement Patterns

### Pattern 1: Root-Level Files
**Pattern:** `[filename].md` (at project root)

**Common files:**
- SESSION_HANDOFF.md
- README.md
- .gitignore

**Usage:**
```json
{
  "pattern": "root_level",
  "placement": "SESSION_HANDOFF.md",
  "type": "session_management"
}
```

---

### Pattern 2: Entity Structure
**Pattern:** `ENTITIES/[Entity]/[category]/[file]`

**Categories vary by entity:**
- README.md (every entity)
- Templates/ (where applicable)
- Data/ (where applicable)
- Output/ (where applicable)

**Usage:**
```json
{
  "pattern": "entity_structure",
  "placement": "ENTITIES/Video/Templates/shooting_template.md",
  "entity": "VID",
  "category": "Templates"
}
```

---

### Pattern 3: System Resources
**Pattern:** `System/[Category]/[file].md`

**Standardized categories:**
- Principles/ (SYS.30)
- Agents/ (SYS.40)
- Verification/ (SYS.50)
- Workflows/ (SYS.60)
- Skills/ (SYS.70)

**Usage:**
```json
{
  "pattern": "system_resource",
  "placement": "System/Principles/strict_principles.md",
  "sys_id": "SYS.30",
  "category": "Principles"
}
```

---

### Pattern 4: Library Organization
**Pattern:** `ENTITIES/Libraries/[Library]/[structure]`

**Libraries:**
- Responsibilities/ (Actions, Objects, Parameters)
- Placements/ (this library)
- Icons/ (planned)
- Similar/ (normalization)

**Usage:**
```json
{
  "pattern": "library_organization",
  "placement": "ENTITIES/Libraries/Placements/Core/placement_master.json",
  "library": "Placements",
  "category": "Core"
}
```

---

## Symbols & Icons

### Path Symbol: 📍
**Use for placement references in documentation**

**Example:**
```markdown
📍 Placement: ENTITIES/Libraries/Placements/README.md
📍 System Placement: System/Workflows/SESSION_LIFECYCLE.md
```

---

### Type Symbols

**Folder Types:**
- 📁 Generic folder
- 📂 Open folder (active work)
- 🗂️ Archive folder
- 📋 Templates folder

**File Types:**
- 📄 Document (.md)
- 📊 Data (.json, .csv)
- 🐍 Script (.py)
- ⚙️ Config (.yaml, .json)

**Special:**
- ⭐ Important/entrance file
- 🔗 Link/reference
- 📍 Placement indicator

---

## Integration with Responsibilities

### Relationship

**Responsibilities = Actions + Objects + Parameters**
```
Action: "Create"
Object: "Icon Library"
Parameters: tone=professional, audience=developers

↓ Results in ↓

PLACEMENT: ENTITIES/Libraries/Icons/icon_catalog.md
```

**Placements = Where things go**
```
Responsibility: Create employee manual
↓ Specifies ↓
PLACEMENT: ENTITIES/HR/Manuals/employee_handbook.md
```

---

### Combined Usage

**In task documentation:**
```markdown
**Responsibility:** CREATE icon library (Action + Object)
**Parameters:** visual=true, categorized=true
**PLACEMENT:** ENTITIES/Libraries/Icons/

**Implementation:**
1. CREATE Core/icon_master.json at PLACEMENT
2. CREATE By_Category/ subfolders at PLACEMENT
3. CREATE README.md at PLACEMENT
```

---

## Terminology Migration

### Old → New Mapping

| Old Term | New Term | Example |
|----------|----------|---------|
| location | placement | File placement: TASKS/TASK-001.md |
| path | placement | Placement reference: ../System/ |
| directory | folder placement | Folder placement: ENTITIES/ |
| file path | file placement | File placement: README.md |
| folder path | folder placement | Folder placement: Week_01/07/ |
| at | at placement | At placement: System/Workflows/ |
| in | within placement | Within placement: ENTITIES/Video/ |
| stored in | stored at placement | Stored at placement: Reports/Daily/ |

---

### Examples in Context

**Before:**
```markdown
The file is located at C:\Users\Dell\Dropbox\ENTITIES\Video\
Path: ../System/Workflows/
Store in Reports/Daily/ folder
```

**After:**
```markdown
File placement: ENTITIES/Video/
Placement reference: ../System/Workflows/
Placement for storage: Reports/Daily/
```

---

## Usage in Documentation

### In Task Files

**Standard format:**
```markdown
# TASK-XXX: [Name]

**Placement:** TASKS/TASK-XXX_Name.md
**Entity Placement:** ENTITIES/[Entity]/ (if applicable)
**Output Placement:** [Where deliverables go]

## Deliverables

**File Placement:** ENTITIES/[Entity]/[file].md
**Folder Placement:** ENTITIES/[Entity]/[subfolder]/
```

---

### In Execution Files

**Standard format:**
```markdown
# EXC-XXX: [Name]

**Placement:** AI_EXECUTIONS/EXC-XXX_Name.md
**Working Placement:** [Where work happens]
**Output Placement:** [Where results go]

## Output

**Files Created:**
- Placement: [file1.md]
- Placement: [file2.py]

**Integration Placement:** [Where integrated]
```

---

### In README Files

**Standard format:**
```markdown
# [Folder Name] - README

**Placement:** [Current file placement]
**Parent Placement:** [Parent folder]
**Related Placements:**
- [Related folder 1]
- [Related folder 2]

## Structure

📁 Current Placement
├── 📄 file1.md
├── 📄 file2.md
└── 📂 subfolder/
    └── 📄 file3.md
```

---

## Reserved Word Usage

### PLACEMENT as Action Verb

**In task lists:**
```markdown
- PLACEMENT for new entity at ENTITIES/Mediateka/
- PLACEMENT of configuration files at System/Config/
- PLACEMENT reference update in all README files
```

**Detection by automation-agent:**
```python
reserved_words = [
    "RESEARCH", "BUILD", "CREATE", "PROCESS",
    "SHARE", "EXECUTE", "UPGRADE", "TEACH",
    "REVIEW", "MARK", "PLACEMENT"  # New
]

if "PLACEMENT" in line:
    # Detect placement action
    create_task_for_file_placement()
```

---

## Placement Validation

### Validation Rules

**1. Format Consistency:**
- Windows paths use backslash: `C:\Users\Dell\`
- Markdown links use forward slash: `ENTITIES/Video/`
- Relative paths use `../` or `../../`

**2. Existence Check:**
```python
import os

def validate_placement(placement):
    """Verify placement exists"""
    if os.path.exists(placement):
        return True
    else:
        return False
```

**3. Reference Integrity:**
- All placement references should be valid
- No broken links to non-existent placements
- Relative paths resolve correctly

---

## Master Catalog

**File:** `Core/placement_master.json`

**Structure:**
```json
{
  "placements": [
    {
      "id": "PLM-001",
      "placement": "System/Workflows/SESSION_LIFECYCLE.md",
      "type": "system",
      "category": "Workflows",
      "description": "Session lifecycle workflow",
      "created": "2025-12-08",
      "status": "active"
    },
    {
      "id": "PLM-002",
      "placement": "ENTITIES/Libraries/Placements/README.md",
      "type": "entity",
      "entity": "LBS",
      "library": "Placements",
      "description": "Placements library documentation",
      "created": "2025-12-08",
      "status": "active"
    }
  ],
  "total_placements": 2,
  "last_updated": "2025-12-08"
}
```

---

## Quick Reference

### Standard Terminology

✅ **Use:** placement, file placement, folder placement, placement reference
❌ **Avoid:** location, path, directory, file path

### In Documentation

**Pattern:** `📍 Placement: [path]`

**Example:**
```markdown
📍 Placement: ENTITIES/Libraries/Placements/README.md
📍 Related Placement: System/Workflows/
```

### In Code

**Python:**
```python
placement = "C:\\Users\\Dell\\Dropbox\\ENTITIES\\Video\\"
file_placement = os.path.join(placement, "README.md")
```

**Markdown:**
```markdown
[Link to file](../System/Workflows/SESSION_LIFECYCLE.md)
```

---

## Integration Checklist

### When Creating New Documents

- [ ] Use "placement" terminology consistently
- [ ] Include 📍 symbol for placement references
- [ ] Follow placement patterns (absolute, relative, system, entity, etc.)
- [ ] Validate placement exists
- [ ] Update placement_master.json if significant new placement

### When Updating Existing Documents

- [ ] Replace "location" with "placement"
- [ ] Replace "path" with "placement" or "placement reference"
- [ ] Replace "directory" with "folder placement"
- [ ] Add 📍 symbols where helpful
- [ ] Verify all placement references still valid

---

## Related Libraries

**Responsibilities Library:**
- Placement: ENTITIES/Libraries/Responsibilities/
- Purpose: Actions, Objects, Parameters
- Relationship: Placements specify WHERE Responsibilities happen

**Icons Library (Planned):**
- Placement: ENTITIES/Libraries/Icons/ (when built)
- Purpose: Visual symbols, emojis, icons
- Relationship: Provides symbols for placement types

**Similar Library:**
- Placement: ENTITIES/Similar/
- Purpose: Normalization, variant mappings
- Relationship: Can normalize placement terminology variants

---

## Status

**Created:** 2025-12-08
**Version:** 1.0
**Status:** Active
**Next Steps:**
1. Create Core/placement_master.json
2. Create By_Type/ category files
3. Update existing documentation to use "placement" terminology
4. Add PLACEMENT to reserved words system
5. Update automation-agent to detect PLACEMENT

---

**Library ID:** LIB.PLM
**Entity:** Libraries (LBS)
**Maintained By:** System updates, manual curation
**Last Updated:** 2025-12-08
