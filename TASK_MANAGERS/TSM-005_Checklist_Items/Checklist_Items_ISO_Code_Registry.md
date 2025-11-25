# Checklist Items ISO Code Registry

**Purpose:** Define and document the ISO code system for Checklist Item templates
**Generated:** November 18, 2025
**Version:** 1.0.0

---

## ISO Code System Overview

This registry documents the standardized 3-letter ISO code system used for Checklist Item templates across the TASK_MANAGERS ecosystem.

---

## Entity Type ISO Codes

| ISO Code | Full Name | Description | Range | Count | Template |
|----------|-----------|-------------|-------|-------|----------|
| **CHT** | Checklist Template | Checklist items serving as deliverables or substeps within projects, milestones, tasks, or steps | CHT-001 to CHT-098 | 98 | Yes |

### Code Derivation

**CHT** is derived from:
- **CH**ecklist **T**emplate
- Uses consonants only (CH from Checklist)
- Ends with **T** to denote Template entity
- Alternative considered: CHK (rejected to maintain template suffix convention)

---

## Department ISO Codes

| Code | Department Name | Description |
|------|-----------------|-------------|
| **AID** | AI Department | AI, Automations, Operations, Administration (consolidated) |
| **HRM** | Human Resource Management | HR operations, recruitment, employee management |
| **DEV** | Development & Engineering | Software development, technical infrastructure |
| **LGN** | Lead Generation & Marketing | Marketing, lead generation, client acquisition |
| **DGN** | Design & Creative | Design, creative work, brand development |
| **VID** | Video Production | Video content creation and production |
| **SLS** | Sales & Client Relations | Sales operations, client management |

---

## Code Derivation Rules

### 1. **Consonant-Only Principle**
- All 3-letter codes use primarily consonants (avoid A, E, I, O, U when possible)
- Exception: AIA (AI Department) requires vowels for clarity
- **Rationale:** Reduces confusion, creates distinct identifiers

**Examples:**
- Checklist → CHT (not CHE or CHL)
- Template → T suffix (not TMP or TEM)

### 2. **Template Suffix Convention**
- All template entities must end with **'T'** as the third character
- Clear visual distinction between templates and operational entities
- Applies to: PRT, MLT, TST, STT, CHT

**Template Codes:** CHT (ends in T)
**Non-Template Codes:** WRF, GDS, PRM, RSR (no T suffix)

### 3. **Three-Letter Standard**
- All ISO codes are exactly 3 letters
- Zero-padded sequential numbering: 001, 010, 100
- Format: `{CODE}-{###}`

**Examples:**
- CHT-001, CHT-042, CHT-098

### 4. **Uppercase Requirement**
- All codes must be uppercase
- Ensures consistency across all systems and documentation

### 5. **Memorable Derivation**
- Codes derived from entity type names for intuitive recall
- Logical connection between name and code

---

## Checklist Template Usage Examples

### Example 1: Deliverable (Project-Level)
```
ISO Code: CHT-044
Legacy ID: CHK-044
Name: n8n workflow: Gmail → Gemini AI → Google Sheets
Department: HRM
Type: Deliverable
Associated Project: Project-Template-003
```

### Example 2: Substep (Step-Level)
```
ISO Code: CHT-024
Legacy ID: CHK-024
Name: Claude Skills enabled in Claude Desktop
Department: DEV
Type: Substep
Associated Step: STEP-TASK-PROJ-DEV-001-001-001
```

### Example 3: Documentation Deliverable
```
ISO Code: CHT-067
Legacy ID: CHK-067
Name: Complete Notion playbook (50+ pages of documentation)
Department: HRM
Type: Deliverable
Associated Project: Project-Template-003
```

---

## Reserved Codes for Future Use

The following CHT codes are reserved for future checklist template expansion:

- **CHT-099** to **CHT-150**: Reserved for additional checklist items
- **CHT-151** to **CHT-200**: Reserved for specialized quality checklists
- **CHT-201** to **CHT-250**: Reserved for compliance and audit checklists

---

## Validation Checksum

| Metric | Count |
|--------|-------|
| Total Checklist Templates | 98 |
| AIA Department | 23 |
| DEV Department | 20 |
| HRM Department | 28 |
| LGN Department | 27 |
| **Grand Total** | **98** |

---

## Migration History

### Phase 1: Legacy to ISO Migration (2025-11-18)

**Legacy Format:** `CHK-###` (Checklist Item)
**New Format:** `CHT-###` (Checklist Template)
**Entities Migrated:** 98

**Rationale for Change:**
1. **Template Suffix Consistency:** CHT ends with 'T' matching PRT, MLT, TST, STT pattern
2. **Hierarchical Clarity:** CHT clearly identifies templates vs instances
3. **Consonant-Only Standard:** Maintains ecosystem-wide naming convention
4. **Backwards Compatibility:** Legacy CHK IDs preserved in migration map

**Migration Completed:** November 18, 2025

---

## Hierarchy Position

Checklist Items (CHT) can exist at multiple levels within the task management hierarchy:

### Level 1: Project/Milestone Deliverables
```
Project (PRT)
  └─ Milestone (MLT)
      └─ Checklist Item (CHT) ← Deliverable
```

### Level 2: Step Substeps
```
Task (TST)
  └─ Step (STT)
      └─ Checklist Item (CHT) ← Substep
```

### Cross-Entity Relationships
- **CHT** can be associated with PRT, MLT, TST, or STT
- Acts as **deliverable** at project/milestone level
- Acts as **substep** at step level
- Flexible association model supports complex workflows

---

## Related Entities

| Entity Type | ISO Code | Relationship |
|-------------|----------|--------------|
| Project Template | PRT | CHT can be project deliverable |
| Milestone Template | MLT | CHT can be milestone deliverable |
| Task Template | TST | CHT can be task deliverable |
| Step Template | STT | CHT can be step substep |
| Workflow | WRF | CHT may reference workflows |
| Guide | GDS | CHT may reference guides |

---

## Naming Convention Format

**File Naming Pattern:**
```
Checklist-Item-{LEGACY_NUM}_{Description}.json

Legacy Example:
Checklist-Item-001_Item_101_to_Item_110.json

Future ISO Pattern:
CHT-{###}_{Description}.json

ISO Example:
CHT-001_Unified_Responsibilities_Ecosystem.json
```

**CSV Listing:**
```
New_ID,Entity_Type,Current_ID,Name,Description,Department,File_Path,Status
CHT-001,Checklist_Template,CHK-001,Unified Responsibilities ecosystem structure,...,AIA,ENTITIES/...,Active
```

---

## Usage Guidelines

### When to Create New CHT Entries

1. **Project Deliverables:** Tangible outputs required for project completion
2. **Milestone Outputs:** Deliverables marking milestone achievement
3. **Task Deliverables:** Specific outputs from task execution
4. **Step Substeps:** Detailed procedural steps within a larger step
5. **Quality Checkpoints:** Validation points ensuring quality standards
6. **Compliance Items:** Regulatory or policy compliance requirements

### CHT Field Requirements

**Required Fields:**
- `checklist_item_id` (e.g., CHT-044)
- `item_name`
- `entity_type` (TASK_MANAGERS)
- `sub_entity` (Checklist_Item)
- `associated_project` (for deliverables)

**Optional Fields:**
- `associated_milestone`
- `associated_task`
- `associated_step` (for substeps)
- `status` (pending, in_progress, completed, blocked)
- `item_type` (deliverable, substep, output, validation, etc.)
- `order` (for substeps)
- `acceptance_criteria`
- `dependencies`

---

## Code Consistency Rules

### ✅ Correct Usage
- `CHT-001` (3 letters, uppercase, hyphen, 3 digits)
- `CHT-042` (zero-padded sequential)
- `CHT-098` (within defined range)

### ❌ Incorrect Usage
- `checklst-1` (not 3 letters, lowercase)
- `CHK-001` (legacy format, use CHT for new entries)
- `CHT-1` (not zero-padded)
- `CHT-999` (exceeds current range without reservation)

---

## Integration with Taxonomy System

Checklist Items are fully integrated with the TASK_MANAGERS Taxonomy system:

1. **Master List:** All CHT entries cataloged in Checklist_Items_Master_List.csv
2. **Migration Map:** Legacy-to-ISO mappings in Checklist_Items_Migration_Map.json
3. **Hierarchy Tree:** Parent-child relationships documented in Checklist_Items_Hierarchy_Tree.md
4. **Department Distribution:** Statistical analysis in Checklist_Items_Department_Distribution.md
5. **ISO Registry:** This document defines all CHT codes and rules

---

**Last Updated:** November 18, 2025
**Next Review:** Q1 2026
