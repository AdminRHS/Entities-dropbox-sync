# Task Templates ISO Code Registry

**Purpose:** Define and document the ISO code system for Task Templates
**Generated:** November 18, 2025
**Last Updated:** November 20, 2025
**Version:** 1.1.0
**Meta-Category:** TSM-003 (Task System Meta - Task Templates)

---

## ISO Code System Overview

This registry documents the standardized 3-letter ISO code system used for Task Templates across the TASK_MANAGERS ecosystem. Task Templates are organized under the TSM-003 meta-category.

---

## Entity Type ISO Codes

| ISO Code | Full Name | Description | Range | Count | Template |
|----------|-----------|-------------|-------|-------|----------|
| **TST** | Task Template | Specific deliverables within milestones containing multiple procedural steps | TST-001 to TST-100 | 68 | Yes |

### Code Derivation

**TST** is derived from:
- **T**a**S**k **T**emplate
- Uses consonants only (T, S from Task)
- Ends with **T** to denote Template entity
- Alternative considered: TSK (rejected to maintain template suffix convention)

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

## Validation Checksum

| Metric | Count |
|--------|-------|
| Total Task Templates | 68 |
| Active Templates | 66 |
| Deprecated Templates | 2 |
| AID Department | 28 |
| LGN Department | 13 |
| VID Department | 10 |
| DEV Department | 9 |
| HRM Department | 6 |
| SLS Department | 1 |
| DGN Department | 1 |

---

## Hierarchy Position

Task Templates (TST) exist at level 3 in the task management hierarchy:

```
Level 1: Project Template (PRT)
  └─ Level 2: Milestone Template (MLT)
      └─ Level 3: Task Template (TST) ← THIS LEVEL
          └─ Level 4: Step Template (STT)
              └─ Level 5: Checklist Template (CHT)
```

### Relationships
- **Parent:** Milestone Template (MLT) - Each task belongs to a milestone
- **Child:** Step Template (STT) - Each task contains multiple steps
- **Deliverables:** Checklist Template (CHT) - Tasks may produce deliverables

---

## Task Categories

### Lead Generation (13 TST)
TST-002, TST-003, TST-006, TST-009, TST-012, TST-013, TST-014, TST-015, TST-016, TST-017, TST-018

### System Analysis (16 TST)
TST-023 to TST-038

### Video Production (10 TST)
TST-045, TST-049 to TST-058

### Development (9 TST)
TST-005, TST-008, TST-010, TST-011, TST-022, TST-047, TST-059 to TST-061

### HR Automation (6 TST)
TST-007, TST-039 to TST-044

### AI Automation (7 TST)
TST-001, TST-019, TST-020, TST-064 to TST-067

---

## Reserved Codes for Future Use

- **TST-068** to **TST-099**: Reserved for additional tasks
- **TST-101** to **TST-200**: Reserved for specialized workflow tasks

---

**Last Updated:** November 18, 2025
