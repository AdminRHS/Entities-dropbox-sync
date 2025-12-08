# PROMPT: Build Placements Library

**Prompt ID:** PMT-BUILD-PLM
**Version:** 1.0
**Created:** 2025-12-08
**Purpose:** Complete prompt for AI to build Placements library entity from scratch
**Target:** Work Agent, System Agent

---

## Context

User requested: "Switch the word locations to the placements. We need a placements library prelibrary prompt to build the library entity of placements, store them all together, and when adding to the nodes, it also should be applicable."

**Goal:** Create complete Placements library (LIB.PLM) with:
- Standardized "placement" terminology (replaces location/path)
- Master catalog of all placements in system
- Integration with reserved words (PLACEMENT as 11th reserved word)
- Alignment with Responsibilities library structure
- Applicable when adding to documentation nodes

---

## Task Overview

Build **ENTITIES/Libraries/Placements/** with complete structure following Responsibilities library pattern.

**Expected Duration:** 2-3 hours
**Files to Create:** 15+ files
**Integration Points:** Reserved words, automation-agent, all documentation

---

## Prerequisites

**Read First:**
1. ENTITIES/Libraries/Responsibilities/README.md - Pattern to follow
2. ENTITIES/Libraries/Responsibilities/ structure - Folder organization reference
3. System/Vocabulary/reserved_words.md - Reserved words list (add PLACEMENT)
4. ENTITIES/Libraries/Placements/README.md - Already created, understand purpose

---

## Step 1: Create Folder Structure (15 min)

**Create these folders:**

```
ENTITIES/Libraries/Placements/
├── Core/
├── By_Type/
├── Integration/
├── Symbols/
└── Templates/
```

**Action:**
```bash
mkdir -p ENTITIES/Libraries/Placements/Core
mkdir -p ENTITIES/Libraries/Placements/By_Type
mkdir -p ENTITIES/Libraries/Placements/Integration
mkdir -p ENTITIES/Libraries/Placements/Symbols
mkdir -p ENTITIES/Libraries/Placements/Templates
```

**Validation:**
- [ ] All 5 folders created
- [ ] README.md already exists (created previously)

---

## Step 2: Create Core Files (30 min)

### File 1: Core/placement_master.json

**Purpose:** Master catalog of all significant placements in system

**Structure:**
```json
{
  "library": "Placements",
  "version": "1.0",
  "created": "2025-12-08",
  "total_placements": 0,
  "placements": [
    {
      "id": "PLM-001",
      "placement": "System/Workflows/SESSION_LIFECYCLE.md",
      "type": "system",
      "category": "Workflows",
      "sys_id": "SYS.60",
      "description": "Main session lifecycle workflow",
      "created": "2025-12-08",
      "status": "active",
      "importance": "critical"
    },
    {
      "id": "PLM-002",
      "placement": "ENTITIES/Libraries/Placements/README.md",
      "type": "entity",
      "entity": "LBS",
      "library": "Placements",
      "description": "Placements library documentation",
      "created": "2025-12-08",
      "status": "active",
      "importance": "high"
    }
  ]
}
```

**Add placements for:**
- All System/ folders (Principles, Agents, Verification, Workflows, Skills, etc.)
- All ENTITIES/ (Libraries, Similar, Video, HR, etc.)
- Key files (SESSION_HANDOFF.md, chat_log.md, etc.)
- Report folders (Reports/Daily/, etc.)
- Workflow documents

**Estimate:** 50-100 placements

---

### File 2: Core/placement_types.json

**Purpose:** Define all placement type categories

**Structure:**
```json
{
  "placement_types": [
    {
      "type": "absolute",
      "description": "Full path from drive root",
      "format": "C:\\Users\\Dell\\Dropbox\\[path]",
      "example": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\Libraries\\Placements\\",
      "use_case": "Scripts, configuration, exact references"
    },
    {
      "type": "relative",
      "description": "Path relative to current location",
      "format": "../[folder]/[file] or ../../[folder]/[file]",
      "example": "../../System/Workflows/SESSION_LIFECYCLE.md",
      "use_case": "Markdown links, portable references"
    },
    {
      "type": "system",
      "description": "Placement within System/ folder",
      "format": "System/[Category]/[file]",
      "example": "System/Principles/strict_principles.md",
      "categories": [
        "Principles",
        "Agents",
        "Verification",
        "Workflows",
        "Skills",
        "Integration",
        "IDs",
        "Libraries",
        "Notifications"
      ]
    },
    {
      "type": "entity",
      "description": "Placement within ENTITIES/ folder",
      "format": "ENTITIES/[EntityName]/[file]",
      "example": "ENTITIES/Video/shooting_instructions.md",
      "entities": [
        "Libraries",
        "Actions",
        "Similar",
        "Scraping",
        "Video",
        "HR",
        "Executives",
        "Mediateka"
      ]
    },
    {
      "type": "task",
      "description": "Task or execution placement",
      "format": "TASKS/TASK-###_Name.md or AI_EXECUTIONS/EXC-###_Name.md",
      "example": "TASKS/TASK-010_Internal_Companies_Ecosystem.md"
    },
    {
      "type": "report",
      "description": "Report placement",
      "format": "Reports/[Category]/[date]_[name].md",
      "example": "Reports/Daily/2025-12-08_session_report.md",
      "categories": [
        "Daily",
        "Processing",
        "Execution",
        "Analytics"
      ]
    },
    {
      "type": "day",
      "description": "Day folder placement",
      "format": "[Month]/[Entity]/Week_##/##/[file]",
      "example": "DEC_25/EXC/Niko_Kar_002/Week_01/07/README.md"
    }
  ]
}
```

---

### File 3: Core/placement_patterns.json

**Purpose:** Common path patterns and templates

**Structure:**
```json
{
  "patterns": [
    {
      "pattern_id": "PTN-001",
      "name": "root_level_file",
      "pattern": "[filename].md",
      "description": "File at project root",
      "examples": [
        "SESSION_HANDOFF.md",
        "README.md"
      ],
      "usage": "Session management, entry points"
    },
    {
      "pattern_id": "PTN-002",
      "name": "entity_structure",
      "pattern": "ENTITIES/[Entity]/[category]/[file]",
      "description": "Standard entity file organization",
      "variables": {
        "Entity": "Video, HR, Libraries, etc.",
        "category": "Templates, Data, Output, etc."
      },
      "examples": [
        "ENTITIES/Video/Templates/shooting_template.md",
        "ENTITIES/Libraries/Placements/Core/placement_master.json"
      ]
    },
    {
      "pattern_id": "PTN-003",
      "name": "system_resource",
      "pattern": "System/[Category]/[file].md",
      "description": "System-level resources",
      "categories": [
        "Principles (SYS.30)",
        "Agents (SYS.40)",
        "Verification (SYS.50)",
        "Workflows (SYS.60)",
        "Skills (SYS.70)"
      ]
    },
    {
      "pattern_id": "PTN-004",
      "name": "library_structure",
      "pattern": "ENTITIES/Libraries/[Library]/[structure]",
      "description": "Library organization pattern",
      "libraries": [
        "Responsibilities",
        "Placements",
        "Icons",
        "Similar"
      ],
      "common_structure": [
        "Core/",
        "By_Type/ or By_Category/",
        "Integration/",
        "README.md"
      ]
    },
    {
      "pattern_id": "PTN-005",
      "name": "daily_work_files",
      "pattern": "[Month]/[Entity]/Week_##/##/##_[type].md",
      "description": "Employee daily files",
      "types": [
        "notes",
        "daily",
        "todo",
        "wspr"
      ],
      "example": "DEC_25/EXC/Niko_Kar_002/Week_01/07/07_notes.md"
    }
  ]
}
```

---

## Step 3: Create By_Type Files (45 min)

**Create one JSON file per placement type:**

### File: By_Type/system_placements.json

**Content:**
```json
{
  "type": "system",
  "description": "All placements within System/ folder",
  "placements": [
    {
      "id": "PLM-SYS-001",
      "placement": "System/Principles/strict_principles.md",
      "sys_id": "SYS.30",
      "description": "Core operating principles"
    },
    {
      "id": "PLM-SYS-002",
      "placement": "System/Agents/agent_architecture.md",
      "sys_id": "SYS.40",
      "description": "Agent system architecture"
    },
    {
      "id": "PLM-SYS-003",
      "placement": "System/Verification/verification_system.md",
      "sys_id": "SYS.50",
      "description": "Verification and transparency system"
    },
    {
      "id": "PLM-SYS-004",
      "placement": "System/Workflows/SESSION_LIFECYCLE.md",
      "sys_id": "SYS.60",
      "description": "Session lifecycle workflow"
    },
    {
      "id": "PLM-SYS-005",
      "placement": "System/Skills/SKL.04_File_Monitor_Notification.md",
      "sys_id": "SYS.70",
      "description": "File monitoring skill specification"
    }
  ]
}
```

**Similarly create:**
- By_Type/entity_placements.json (all ENTITIES/ placements)
- By_Type/task_placements.json (TASKS/ and AI_EXECUTIONS/)
- By_Type/report_placements.json (Reports/ placements)
- By_Type/workflow_placements.json (specific to workflow files)

---

## Step 4: Create Integration Files (30 min)

### File: Integration/placement_mapping.json

**Purpose:** Map old terminology to new "placement" terminology

**Structure:**
```json
{
  "terminology_migration": {
    "old_to_new": {
      "location": "placement",
      "path": "placement",
      "file path": "file placement",
      "folder path": "folder placement",
      "directory": "folder placement",
      "at": "at placement",
      "in": "within placement",
      "stored in": "stored at placement"
    },
    "examples": [
      {
        "before": "The file is located at C:\\Users\\Dell\\Dropbox\\ENTITIES\\Video\\",
        "after": "File placement: ENTITIES/Video/"
      },
      {
        "before": "Path: ../System/Workflows/",
        "after": "Placement reference: ../System/Workflows/"
      },
      {
        "before": "Store in Reports/Daily/ folder",
        "after": "Placement for storage: Reports/Daily/"
      }
    ]
  }
}
```

### File: Integration/cross_references.json

**Purpose:** Map relationships between placements

**Structure:**
```json
{
  "cross_references": [
    {
      "placement": "TASKS/TASK-010_Internal_Companies_Ecosystem.md",
      "references": [
        "CLARIFICATIONS/README.md (Question Q010-A)",
        "System/IDs/entity_ids.md (company IDs)",
        "ENTITIES/ (entity assignments)"
      ],
      "referenced_by": [
        "SESSION_HANDOFF.md (CRITICAL priority)",
        "Reports/Daily/2025-12-08_systems_created_summary.md"
      ]
    }
  ]
}
```

---

## Step 5: Create Symbols Files (15 min)

### File: Symbols/path_symbols.json

**Purpose:** Visual symbols for different path types

**Structure:**
```json
{
  "symbols": {
    "placement_indicator": {
      "symbol": "📍",
      "unicode": "U+1F4CD",
      "usage": "Prefix for placement references",
      "example": "📍 Placement: ENTITIES/Video/"
    },
    "folder_types": {
      "generic_folder": {
        "symbol": "📁",
        "usage": "Generic folder reference"
      },
      "open_folder": {
        "symbol": "📂",
        "usage": "Active work folder"
      },
      "archive_folder": {
        "symbol": "🗂️",
        "usage": "Archived content"
      },
      "templates_folder": {
        "symbol": "📋",
        "usage": "Template storage"
      }
    },
    "file_types": {
      "document": {
        "symbol": "📄",
        "usage": "Markdown files (.md)"
      },
      "data": {
        "symbol": "📊",
        "usage": "Data files (.json, .csv)"
      },
      "script": {
        "symbol": "🐍",
        "usage": "Python scripts (.py)"
      },
      "config": {
        "symbol": "⚙️",
        "usage": "Configuration files"
      }
    },
    "special": {
      "important": {
        "symbol": "⭐",
        "usage": "Important/entrance files"
      },
      "link": {
        "symbol": "🔗",
        "usage": "Link/reference indicator"
      }
    }
  }
}
```

---

## Step 6: Update Reserved Words (15 min)

**File to update:** `System/Vocabulary/reserved_words.md`

**Add PLACEMENT as 11th reserved word:**

```markdown
# Reserved Vocabulary

**Total Reserved Words:** 11
**Status:** Active
**Last Updated:** 2025-12-08

---

## Reserved Words List

1. **RESEARCH** - Investigation, information gathering, analysis
2. **BUILD** - Construction, system building, creation of complex systems
3. **CREATE** - Generation of new items, file creation
4. **PROCESS** - Data transformation, handling, workflow execution
5. **SHARE** - Distribution, communication, sharing information
6. **EXECUTE** - Running scripts, implementation, carrying out tasks
7. **UPGRADE** - Improvement, enhancement, system updates
8. **TEACH** - Education, training, knowledge transfer
9. **REVIEW** - Evaluation, checking, assessment
10. **MARK** - Flagging, noting, highlighting important items
11. **PLACEMENT** ← NEW - Location specification, path references, file positioning

---

## PLACEMENT Reserved Word

**Added:** 2025-12-08
**Purpose:** Standardize all location/path terminology to "placement"

**Usage:**
- PLACEMENT for new entity: ENTITIES/Mediateka/
- PLACEMENT of configuration files: System/Config/
- PLACEMENT reference update in all README files

**Detection:** automation-agent detects PLACEMENT and triggers placement-related tasks
```

---

## Step 7: Create Templates (20 min)

### File: Templates/placement_documentation_template.md

**Purpose:** Template for documenting placements in task/execution files

**Content:**
```markdown
# [Document Name]

## Placements

**Current Placement:** [This file's placement]
**Related Placements:**
- [Related placement 1]
- [Related placement 2]

## Working Placements

**Input Placement:** [Where input files come from]
**Output Placement:** [Where output files go]
**Integration Placement:** [Where integrated into system]

## Folder Structure

📁 [Current folder placement]
├── 📄 [file1].md
├── 📄 [file2].md
├── 📂 [subfolder]/
│   ├── 📄 [file3].md
│   └── 📊 [data].json
└── ⭐ README.md

## Placement References

**Absolute Placement:** C:\\Users\\Dell\\Dropbox\\[path]
**Relative Placement:** ../[path] or ../../[path]
**System Placement:** System/[category]/
**Entity Placement:** ENTITIES/[entity]/
```

---

## Step 8: Integration with automation-agent (20 min)

**Update:** `automation-agent/modules/reserved_word_detector.py`

**Add PLACEMENT detection:**

```python
class ReservedWordDetector:
    def __init__(self):
        self.reserved_words = [
            "RESEARCH", "BUILD", "CREATE", "PROCESS",
            "SHARE", "EXECUTE", "UPGRADE", "TEACH",
            "REVIEW", "MARK", "PLACEMENT"  # Added
        ]

    def detect_placement_action(self, line):
        """Detect PLACEMENT reserved word and extract placement info"""
        pattern = r'PLACEMENT\s+(?:for|of|at|reference)?\s*:?\s*(.+)'
        match = re.search(pattern, line, re.IGNORECASE)

        if match:
            placement_info = match.group(1).strip()
            return {
                "action": "PLACEMENT",
                "placement": placement_info,
                "line": line,
                "type": self.determine_placement_type(placement_info)
            }
        return None

    def determine_placement_type(self, placement):
        """Determine type of placement"""
        if placement.startswith("C:\\"):
            return "absolute"
        elif placement.startswith("../") or placement.startswith("../../"):
            return "relative"
        elif placement.startswith("System/"):
            return "system"
        elif placement.startswith("ENTITIES/"):
            return "entity"
        elif placement.startswith("TASKS/") or placement.startswith("AI_EXECUTIONS/"):
            return "task"
        else:
            return "unknown"
```

---

## Step 9: Documentation Updates (30 min)

**Update these key files to use "placement" terminology:**

### Priority 1: Core Documentation
- [ ] README.md (root) - Replace location/path with placement
- [ ] SESSION_HANDOFF.md - Use placement terminology
- [ ] System/Workflows/SESSION_LIFECYCLE.md - Update references

### Priority 2: Entity Documentation
- [ ] ENTITIES/Libraries/README.md - Terminology update
- [ ] ENTITIES/Video/README.md - Use placements
- [ ] ENTITIES/HR/README.md - Use placements

### Priority 3: Task Templates
- [ ] Create task template with placement section
- [ ] Update existing TASK files as examples

**Pattern to follow:**
- Find: "location", "path", "directory"
- Replace with: "placement", "folder placement", "file placement"
- Add: 📍 symbol where helpful

---

## Step 10: Validation & Testing (15 min)

**Validation checklist:**

- [ ] All folder structure created (Core/, By_Type/, Integration/, Symbols/, Templates/)
- [ ] Core files created (placement_master.json, placement_types.json, placement_patterns.json)
- [ ] By_Type files created (at least 3)
- [ ] Integration files created (mapping, cross_references)
- [ ] Symbols file created (path_symbols.json)
- [ ] Templates created (documentation template)
- [ ] Reserved words updated (PLACEMENT added)
- [ ] automation-agent updated (PLACEMENT detection)
- [ ] Sample documentation updated (at least 3 files)
- [ ] All JSON files valid (no syntax errors)

**Test:**
```bash
# Validate JSON files
python -m json.tool ENTITIES/Libraries/Placements/Core/placement_master.json

# Check placement references work
ls -la ENTITIES/Libraries/Placements/

# Verify folder structure
tree ENTITIES/Libraries/Placements/
```

---

## Deliverables

**Files to Create:** (minimum 15)

1. ✅ ENTITIES/Libraries/Placements/README.md (already created)
2. Core/placement_master.json
3. Core/placement_types.json
4. Core/placement_patterns.json
5. By_Type/system_placements.json
6. By_Type/entity_placements.json
7. By_Type/task_placements.json
8. By_Type/report_placements.json
9. By_Type/workflow_placements.json
10. Integration/placement_mapping.json
11. Integration/cross_references.json
12. Symbols/path_symbols.json
13. Templates/placement_documentation_template.md
14. System/Vocabulary/reserved_words.md (updated)
15. automation-agent/modules/reserved_word_detector.py (updated)

**Plus:** Update 5-10 existing documentation files with placement terminology

---

## Success Criteria

✅ **Complete library structure** - All folders and files created
✅ **Terminology standardized** - "Placement" used consistently
✅ **Reserved word integrated** - PLACEMENT detection working
✅ **Documentation updated** - Key files use new terminology
✅ **Validation passed** - All JSON valid, references work
✅ **Applicable to nodes** - Can add placement info when documenting

---

## Timeline

**Total time:** 2-3 hours

- Step 1: Folder structure (15 min)
- Step 2: Core files (30 min)
- Step 3: By_Type files (45 min)
- Step 4: Integration files (30 min)
- Step 5: Symbols files (15 min)
- Step 6: Reserved words (15 min)
- Step 7: Templates (20 min)
- Step 8: automation-agent (20 min)
- Step 9: Documentation updates (30 min)
- Step 10: Validation (15 min)

**Buffer:** 30 min for issues/refinement

---

## Notes

**Pattern to follow:**
- Look at ENTITIES/Libraries/Responsibilities/ structure
- Mirror the organization (Core/, By_X/, Integration/)
- Use similar JSON format and naming conventions
- Maintain consistency with existing libraries

**When adding to nodes (documentation):**
```markdown
## Placements Section

📍 **Current Placement:** [this file]
📍 **Related Placements:** [list]
📍 **Output Placement:** [where deliverables go]
```

---

**Prompt Created:** 2025-12-08
**Prompt ID:** PMT-BUILD-PLM
**Ready to Execute:** Yes
**Estimated Completion:** 2-3 hours
