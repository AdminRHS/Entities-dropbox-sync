# Project Templates ISO Code Registry

**Purpose:** Define and document the ISO code system for Project Templates
**Generated:** November 18, 2025
**Last Updated:** November 20, 2025
**Version:** 1.1.0
**Meta-Category:** TSM-001 (Task System Meta - Project Templates)

---

## ISO Code System Overview

This registry documents the standardized 3-letter ISO code system used for Project Templates across the TASK_MANAGERS ecosystem. Project Templates are organized under the TSM-001 meta-category.

---

## Entity Type ISO Codes

| ISO Code | Full Name | Description | Range | Count | Template |
|----------|-----------|-------------|-------|-------|----------|
| **PRT** | Project Template | Strategic project templates representing complete initiatives with milestones and tasks | PRT-001 to PRT-008 | 8 | Yes |

### Code Derivation

**PRT** is derived from:
- **PR**oject **T**emplate
- Uses consonants only (P, R from Project)
- Ends with **T** to denote Template entity
- Alternative considered: PRJ (rejected to maintain template suffix convention)

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

## Project Template Usage Examples

### Example 1: AI Research Project
```
ISO Code: PRT-001
Legacy ID: Project-Template-001
Name: AI Tutorial Research to Taxonomy Integration
Department: AID
Type: Recurring Research Workflow
Duration: 4-6 hours per cycle
Milestones: 3
Tasks: 10
```

### Example 2: Development Project
```
ISO Code: PRT-002
Legacy ID: Project-Template-002
Name: Complete MCP Automation Stack Setup
Department: DEV
Type: Development Project
Milestones: 4
Tasks: 5+
```

### Example 3: HR Automation Project
```
ISO Code: PRT-003
Legacy ID: Project-Template-003
Name: Complete HR Automation Implementation
Department: HRM
Type: Automation Implementation
Duration: 4 weeks
Milestones: 4
```

---

## Validation Checksum

| Metric | Count |
|--------|-------|
| Total Project Templates | 8 |
| AID Department | 3 |
| LGN Department | 2 |
| DEV Department | 1 |
| HRM Department | 1 |
| VID Department | 1 |
| **Grand Total** | **8** |

---

## Hierarchy Position

Project Templates (PRT) exist at level 1 (top level) in the task management hierarchy, organized under TSM-001 meta-category:

```
Level 0: TSM-001 (Project Templates Meta-Category) ← META LEVEL
  └─ Level 1: Project Template (PRT) ← TOP LEVEL (9 instances)
      └─ Level 2: Milestone Template (MLT)
          └─ Level 3: Task Template (TST)
              └─ Level 4: Step Template (STT)
                  └─ Level 5: Checklist Template (CHT)
```

### Relationships
- **Meta-Parent:** TSM-001 (Project Templates Meta-Category)
- **Parent:** None - Projects are the top-level entity type
- **Child:** Milestone Template (MLT) - Each project contains multiple milestones
- **Deliverables:** Through milestones and their checklist items

---

## Reserved Codes for Future Use

- **PRT-009** to **PRT-020**: Reserved for additional projects
- **PRT-021** to **PRT-050**: Reserved for specialized project types

---

## TSM-001 Meta-Category

**Meta-Category ID:** TSM-001
**Category Name:** Project Templates
**Organizes:** PRT (Project Template instances)
**Instance Count:** 9
**ID Range:** PRT-001 to PRT-009
**Department:** ALL
**Description:** Meta-level category organizing all Project Template entities in the TASK_MANAGERS system.

---

**Last Updated:** November 20, 2025
