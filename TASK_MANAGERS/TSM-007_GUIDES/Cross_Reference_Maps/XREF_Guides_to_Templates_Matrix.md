# Cross-Reference Matrix: Guides to Templates

**Purpose:** Visual matrix showing which guides apply to which templates across the hierarchy
**Last Updated:** 2025-11-22

---

## Matrix Overview

This matrix shows the cross-reference relationships between guides (GDS-###) and templates across all four levels of the TASK_MANAGERS hierarchy:
- **PRT-###:** Project Templates (TSM-001)
- **MLT-###:** Milestone Templates (TSM-002)
- **TST-###:** Task Templates (TSM-003)
- **STP-###:** Step Templates (TSM-004)

**Legend:**
- `R` = Required
- `r` = Recommended
- `o` = Optional
- `-` = Not linked

---

## Project Templates Cross-Reference (TSM-001)

| Guide Code | Guide Name | PRT-001 | PRT-002 | PRT-003 | PRT-004 | PRT-005 |
|------------|------------|---------|---------|---------|---------|---------|
| GDS-001 | CRM Taxonomy | - | - | - | - | - |
| GDS-002 | Data Extraction | - | - | - | - | - |
| GDS-003 | Designer Integration | - | - | - | - | - |
| GDS-004 | Framework README | - | - | - | R | - |
| GDS-005 | Implementation Checklists | - | - | - | - | - |
| GDS-006 | Knowledge Library | - | - | - | - | - |
| GDS-007 | Tool Usage Proposals | - | - | - | - | - |
| GDS-008 | Taxonomy README | - | - | - | - | - |
| GDS-009 | SMM Communication | - | - | - | - | R |
| GDS-010 | Quick Start PMT-032 | R | - | - | - | - |
| GDS-011 | Entity Mapping | r | - | - | - | - |
| GDS-012 | Template Cross-Ref | - | r | o | - | - |

**Projects:**
- **PRT-001:** Daily Report Collection
- **PRT-002:** Content Creation Pipeline
- **PRT-003:** Template Management
- **PRT-004:** System Architecture
- **PRT-005:** Social Media Management

---

## Milestone Templates Cross-Reference (TSM-002)

| Guide Code | Guide Name | MLT-001 | MLT-002 | MLT-005 | MLT-007 | MLT-008 |
|------------|------------|---------|---------|---------|---------|---------|
| GDS-010 | Quick Start PMT-032 | r | r | - | - | - |
| GDS-011 | Entity Mapping | - | - | R | r | - |
| GDS-012 | Template Cross-Ref | - | - | - | - | o |

**Milestones:**
- **MLT-001:** Weekly Report Compilation
- **MLT-002:** Monthly Report Aggregation
- **MLT-005:** Task Validation
- **MLT-007:** Quality Assurance
- **MLT-008:** Template Review & Approval

---

## Task Templates Cross-Reference (TSM-003)

| Guide Code | Guide Name | TST-001 | TST-015 | TST-018 | TST-019 | TST-023 | TST-042 | TST-043 | TST-044 | TST-045 | TST-067 | TST-089 | TST-101 | TST-102 | TST-103 |
|------------|------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| GDS-001 | CRM Taxonomy | - | - | R | r | - | - | - | - | - | - | - | - | - | - |
| GDS-009 | SMM Comm | - | - | - | - | - | - | - | - | - | - | - | R | R | r |
| GDS-010 | Quick Start | - | - | - | - | - | R | R | r | r | - | - | - | - | - |
| GDS-011 | Entity Map | - | - | R | - | - | r | - | R | - | r | r | - | - | - |
| GDS-012 | Template XRef | o | o | - | - | r | - | - | - | - | - | - | - | - | - |

**Tasks:**
- **TST-001:** Template Creation Workflow
- **TST-015:** Template Documentation Standards
- **TST-018:** Entity Classification
- **TST-019:** Entity Relationship Mapping
- **TST-023:** Cross-Reference Validation
- **TST-042:** Daily Report Submission
- **TST-043:** Whisper Flow Recording
- **TST-044:** Entity Mapping Validation
- **TST-045:** Activity Time Tracking
- **TST-067:** Task-to-Milestone Linking
- **TST-089:** Template Hierarchy Navigation
- **TST-101:** Social Media Post Creation
- **TST-102:** Content Template Application
- **TST-103:** Multi-Channel Posting

---

## Step Templates Cross-Reference (TSM-004)

| Guide Code | Guide Name | STP-089 | STP-090 | STP-091 | STP-092 | STP-127 | STP-128 | STP-129 | STP-130 | STP-150 | STP-151 |
|------------|------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| GDS-010 | Quick Start | - | - | - | - | R | R | r | r | - | - |
| GDS-011 | Entity Map | R | R | r | r | - | - | - | - | - | - |
| GDS-012 | Template XRef | - | - | - | - | - | - | - | - | o | o |

**Steps:**
- **STP-089:** Entity ID Assignment
- **STP-090:** Entity Validation Rules
- **STP-091:** Hierarchy Navigation
- **STP-092:** Cross-Reference Verification
- **STP-127:** Whisper Flow Initialization
- **STP-128:** Activity Logging Format
- **STP-129:** Timestamp Documentation
- **STP-130:** Transcript Embedding
- **STP-150:** Template Metadata Documentation
- **STP-151:** Cross-Reference Creation

---

## Summary Statistics

### Guide Coverage

| Guide Code | Total Template Links | PRT | MLT | TST | STP |
|------------|---------------------|-----|-----|-----|-----|
| GDS-010 | 10 | 1 | 2 | 4 | 4 |
| GDS-011 | 11 | 1 | 2 | 5 | 4 |
| GDS-012 | 7 | 2 | 1 | 3 | 2 |
| GDS-001 | 2 | 0 | 0 | 2 | 0 |
| GDS-009 | 4 | 1 | 0 | 3 | 0 |
| GDS-004 | 1 | 1 | 0 | 0 | 0 |

### Template Coverage

| Template Level | Templates Linked | Total Templates | Coverage % |
|----------------|------------------|-----------------|------------|
| Project (PRT) | 5 | 9+ | ~56% |
| Milestone (MLT) | 5 | 21+ | ~24% |
| Task (TST) | 14 | 58+ | ~24% |
| Step (STP) | 10 | 141+ | ~7% |

---

## Hierarchy Propagation Examples

### Example 1: GDS-010 Hierarchy Chain

```
PRT-001 (Daily Report Collection) [Required]
  ├── MLT-001 (Weekly Report Compilation) [Recommended]
  ├── MLT-002 (Monthly Report Aggregation) [Recommended]
  │
  └── TST-042 (Daily Report Submission) [Required]
      ├── STP-127 (Whisper Flow Init) [Required]
      ├── STP-128 (Activity Logging) [Required]
      ├── STP-129 (Timestamp Doc) [Recommended]
      └── STP-130 (Transcript Embed) [Recommended]
```

**Result:** Guide GDS-010 is linked at ALL 4 hierarchy levels, providing comprehensive coverage for the entire daily report collection process.

### Example 2: GDS-011 Hierarchy Chain

```
PRT-001 (Daily Report Collection) [Recommended]
  └── MLT-005 (Task Validation) [Required]
      ├── TST-042 (Daily Report Submission) [Recommended]
      ├── TST-044 (Entity Mapping Validation) [Required]
      ├── TST-018 (Entity Classification) [Required]
      ├── TST-067 (Task-Milestone Linking) [Recommended]
      └── TST-089 (Hierarchy Navigation) [Recommended]
          ├── STP-089 (Entity ID Assignment) [Required]
          ├── STP-090 (Entity Validation) [Required]
          ├── STP-091 (Hierarchy Nav) [Recommended]
          └── STP-092 (XRef Verification) [Recommended]
```

**Result:** Guide GDS-011 provides deep coverage of entity mapping across task and step levels, with milestone and project context.

---

## Usage Scenarios

### Scenario 1: New Employee Onboarding
**User needs:** Learn daily reporting process

**Recommended guides:**
1. GDS-010 (Quick Start PMT-032) - **Required** for PRT-001, TST-042
2. GDS-011 (Entity Mapping) - **Recommended** for PRT-001, **Required** for MLT-005

**Template path:** PRT-001 → MLT-001 → TST-042 → STP-127, STP-128

---

### Scenario 2: Working on Task TST-044 (Entity Mapping Validation)
**System shows:**
- GDS-011 (Required) - "Entity mapping validation process"
- GDS-010 (Recommended) - "Entity mapping validation"

**User selects:** GDS-011 for detailed tutorial

---

### Scenario 3: Creating Social Media Content
**User needs:** Use communication templates

**Recommended guides:**
1. GDS-009 (SMM Communication Templates) - **Required** for PRT-005, TST-101, TST-102

**Template path:** PRT-005 → TST-101 → [steps]

---

## Gap Analysis

### Templates Without Guides (High-Priority)

**Task Templates needing guides:**
- TST-005, TST-010, TST-025, TST-030, TST-035, TST-040, TST-050, TST-055, TST-060 (Development tasks)
- TST-070, TST-075, TST-080 (Video production tasks)
- TST-085, TST-090, TST-095 (Finance/HR tasks)

**Recommendation:** Create department-specific guides for DEV, VID, FNC, HRM

### Over-Linked Templates
- None currently; all linkages are appropriate

---

## Maintenance Notes

**Update this matrix when:**
- New guides are created (add row)
- New templates are created (add column)
- Cross-references are added/removed (update cell)
- Relevance levels change (update R/r/o designation)

**Review frequency:** Monthly, or when major template changes occur

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/Cross_Reference_Maps/XREF_Guides_to_Templates_Matrix.md`
**Related Files:**
- [XREF_Template_Hierarchy_Integration.md](./XREF_Template_Hierarchy_Integration.md)
- [XREF_Department_Guide_Coverage.md](./XREF_Department_Guide_Coverage.md)
- [Database_Architecture_Preview/SCHEMA_OVERVIEW.md](../Database_Architecture_Preview/SCHEMA_OVERVIEW.md)

**Last Updated:** 2025-11-22
