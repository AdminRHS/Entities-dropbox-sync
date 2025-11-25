# Milestone Templates ISO Code Registry

**Purpose:** Define and document the ISO code system for Milestone Templates
**Generated:** November 18, 2025
**Last Updated:** November 20, 2025
**Version:** 1.1.0
**Meta-Category:** TSM-002 (Task System Meta - Milestone Templates)

---

## ISO Code System Overview

This registry documents the standardized 3-letter ISO code system used for Milestone Templates across the TASK_MANAGERS ecosystem. Milestone Templates are organized under the TSM-002 meta-category.

---

## Entity Type ISO Codes

| ISO Code | Full Name | Description | Range | Count | Template |
|----------|-----------|-------------|-------|-------|----------|
| **MLT** | Milestone Template | Major phases or checkpoints within projects containing multiple tasks | MLT-001 to MLT-009 | 9 | Yes |

### Code Derivation

**MLT** is derived from:
- **M**i**L**estone **T**emplate
- Uses consonants only (M, L from Milestone)
- Ends with **T** to denote Template entity
- Alternative considered: MLS (rejected to maintain template suffix convention)

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

## Milestone Template Usage Examples

### Example 1: Analysis Milestone
```
ISO Code: MLT-001
Legacy ID: Milestone-Template-001
Name: Content Analysis
Department: AID
Category: Analysis
Phase: 3
Tasks: 3 task templates
```

### Example 2: Video Research Milestone
```
ISO Code: MLT-006
Legacy ID: Milestone-Template-006
Name: VIDEO-001 Research Complete
Department: VID
Category: Research
Phase: 1
Tasks: 2 task templates
```

### Example 3: Workflow Migration Milestone
```
ISO Code: MLT-009
Legacy ID: Milestone-Template-009
Name: Behance Project Publishing Workflow
Department: DGN
Category: Workflow Migration
Source: Behance_Project_Publishing_Workflow.yaml
```

---

## Validation Checksum

| Metric | Count |
|--------|-------|
| Total Milestone Templates | 9 |
| AID Department | 5 |
| VID Department | 3 |
| DGN Department | 1 |
| **Grand Total** | **9** |

---

## Hierarchy Position

Milestone Templates (MLT) exist at level 2 in the task management hierarchy:

```
Level 1: Project Template (PRT)
  └─ Level 2: Milestone Template (MLT)
      └─ Level 3: Task Template (TST)
          └─ Level 4: Step Template (STT)
              └─ Level 5: Checklist Template (CHT)
```

### Relationships
- **Parent:** Project Template (PRT) - Each milestone belongs to a project
- **Child:** Task Template (TST) - Each milestone contains multiple tasks
- **Deliverables:** Checklist Template (CHT) - Milestones produce deliverables

---

## Code Derivation Rules

### 1. **Consonant-Only Principle**
- All 3-letter codes use primarily consonants
- **Rationale:** Reduces confusion, creates distinct identifiers

### 2. **Template Suffix Convention**
- All template entities end with **'T'**
- Template Codes: PRT, MLT, TST, STT, CHT

### 3. **Three-Letter Standard**
- All codes exactly 3 letters
- Zero-padded numbering: 001, 010, 100

---

## Reserved Codes for Future Use

- **MLT-010** to **MLT-050**: Reserved for additional project milestones
- **MLT-051** to **MLT-100**: Reserved for specialized workflow milestones

---

**Last Updated:** November 18, 2025
