# TASK_MANAGERS ISO Code Registry

**Version:** 1.1.0
**Generated:** 2025-11-18
**Last Updated:** 2025-11-20
**Entity:** TASK_MANAGERS
**Total Registered Codes:** 10 entity types + 7 departments = 17 codes

---

## Purpose

This registry documents all 3-letter ISO codes used in the TASK_MANAGERS taxonomy system. All codes follow consonant-only naming conventions (no vowels: A, E, I, O, U) for consistency and memorability.

---

## Entity Type ISO Codes

### Meta-Level Category Code

| ISO Code | Full Name | Derivation | Count | ID Range | Description |
|----------|-----------|------------|-------|----------|-------------|
| **TSM** | Task System Meta | **T**_ask **S**_ystem **M**_eta | 8 | TSM-001 to TSM-008 | Meta-level category identifiers for TASK_MANAGERS entity types (organizational layer above templates) |

**Purpose:** TSM codes represent meta-level categories that organize and classify the 8 main TASK_MANAGERS entity types. Each TSM entry acts as a container/category for multiple instances of a specific entity type.

**Usage Pattern:**
```
TSM-001 → Project Templates (category containing 9 PRT instances)
TSM-002 → Milestone Templates (category containing 28 MLT instances)
...etc.
```

---

### Template Entities (with 'T' suffix)

| ISO Code | Full Name | Derivation | Count | ID Range | Description |
|----------|-----------|------------|-------|----------|-------------|
| **PRT** | Project Template | **P**_**R**_oject **T**_emplate | 9 | PRT-001 to PRT-009 | High-level project definitions with milestones and task sequences |
| **MLT** | Milestone Template | **M**_i**L**_estone **T**_emplate | 9 | MLT-001 to MLT-009 | Project phase markers with task collections and deliverables |
| **TST** | Task Template | **T**_a**S**_k **T**_emplate | 71 | TST-001 to TST-071 | Individual task definitions using Action + Object + Tool formula |
| **STT** | Step Template | **ST**_ep **T**_emplate | 379 | STT-001 to STT-379 | Detailed procedural steps within tasks, organized by department |
| **CHT** | Checklist Template | **CH**_ecklist **T**_emplate | 98 | CHT-001 to CHT-098 | Deliverable items and substep verification checklists |

**Naming Rule:** All template entity codes end with 'T' to clearly identify them as templates.

### Non-Template Entities

| ISO Code | Full Name | Derivation | Count | ID Range | Description |
|----------|-----------|------------|-------|----------|-------------|
| **WRF** | Workflow | **W**_o**R**_k**F**_low | 20 | WRF-001 to WRF-020 | Automated process flows (Linear/Parallel types) |
| **GDS** | Guide | **G**_ui**D**_e**S** | 8+ | GDS-001 onwards | Taxonomy and framework documentation guides |
| **PMT** | Prompts (Entity Reference) | **P**_ro**M**_p**T**_s | N/A | See ENTITIES/PROMPTS | Reference to standalone PROMPTS entity (155 prompts) |
| **RSR** | Research | **R**_e**S**_ea**R**_ch | 50+ | RSR-001 onwards | Research reports and video analyses |

---

## Department ISO Codes

| ISO Code | Full Name | Derivation | Description | Active |
|----------|-----------|------------|-------------|--------|
| **AID** | AI Department | **A**rtificial **I**ntelligence **D**_epartment | AI, Automations, Operations, Administration (consolidated 2025-11-17) | ✓ Active |
| **HRM** | Human Resource Management | **H**_uman **R**_esource **M**_anagement | Talent acquisition, recruitment, employee management | ✓ Active |
| **DEV** | Development | **DEV**_elopment | Software development, engineering, MCP infrastructure | ✓ Active |
| **LGN** | Lead Generation | **L**_ead **G**_e**N**_eration | Lead generation, marketing, outreach campaigns | ✓ Active |
| **DGN** | Design | **D**_esi**G**_**N** | Design, creative, branding, portfolio management | ✓ Active |
| **VID** | Video | **VID**_eo | Video production, content creation, social media | ✓ Active |
| **SLS** | Sales | **S**_a**L**_e**S** | Sales, client relations, account management | ✓ Active |

### Deprecated Department Codes (2025-11-17)

| ISO Code | Full Name | Status | Migrated To |
|----------|-----------|--------|-------------|
| ~~OPS~~ | Operations | Deprecated | AID |
| ~~ADM~~ | Administration | Deprecated | AID |

**Consolidation Rationale:** Operations and Administration functions were merged into AI Department (AID) to streamline automation workflows and reduce department fragmentation.

---

## Code Derivation Rules

### 1. Consonant-Only Principle
All ISO codes use **only consonants** (B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z). No vowels (A, E, I, O, U) are allowed except when unavoidable (e.g., AID for AI Department).

**Examples:**
- Project → **PRT** (P_R_oject T_emplate)
- Milestone → **MLT** (M_iL_estone T_emplate)
- Design → **DGN** (D_esiG_N, not DSN)

### 2. Three-Letter Format
All codes are exactly **3 letters** for consistency and easy memorability.

### 3. Uppercase Only
All codes are **UPPERCASE** (e.g., PRT, not prt or Prt).

### 4. Template Suffix 'T'
All **Template** entities end with **'T'** as the third character:
- PRT (Project Template)
- MLT (Milestone Template)
- TST (Task Template)
- STT (Step Template)
- CHT (Checklist Template)

This makes it easy to identify template vs. non-template entities at a glance.

### 5. Memorable & Intuitive
Codes are derived from the entity type name to be easily remembered and understood:
- **WRF** = WoRkFlow
- **GDS** = GuiDeS
- **PRM** = PRoMpt
- **RSR** = ReSeaRch

---

## Reserved Codes for Future Use

| ISO Code | Reserved For | Expected Use |
|----------|-------------|--------------|
| **SCN** | Scenario | Scenario templates for complex multi-project workflows |
| **PHT** | Phase Template | Major phase templates above milestones |
| **SPR** | Sprint | Sprint/iteration templates for agile workflows |
| **GTT** | Gate Template | Quality gate/checkpoint templates |
| **SBT** | Subtask Template | Subtask breakdown templates |

---

## Complete Entity Type Hierarchy

```
TASK_MANAGERS/
│
├── TSM-001 (Project Templates Meta-Category)
│   └── PRT (Project Template Instances: 9)
│       └── Contains multiple...
│           ├── MLT (Milestone Templates)
│           │   └── Contains multiple...
│           │       ├── TST (Task Templates)
│           │       │   └── Contains multiple...
│           │       │       ├── STT (Step Templates)
│           │       │       │   └── Contains multiple...
│           │       │       │       └── CHT (Checklist Templates)
│           │       │       └── CHT (Checklist Templates)
│           │       └── CHT (Checklist Templates)
│           └── CHT (Checklist Templates)
│
├── TSM-002 (Milestone Templates Meta-Category)
│   └── MLT (Milestone Template Instances: 28)
│
├── TSM-003 (Task Templates Meta-Category)
│   └── TST (Task Template Instances: 71)
│
├── TSM-004 (Step Templates Meta-Category)
│   └── STT (Step Template Instances: 379)
│
├── TSM-005 (Checklist Templates Meta-Category)
│   └── CHT (Checklist Template Instances: 98)
│
├── TSM-006 (Workflows Meta-Category)
│   └── WRF (Workflow Instances: 20) - Automated multi-task processes
│
├── TSM-007 (Guides Meta-Category)
│   └── GDS (Guide Instances: 8+) - Documentation and frameworks
│
└── TSM-008 (Research Meta-Category)
    └── RSR (Research Instances: 24+) - Analysis reports and studies
    └── Path: ENTITIES/TASK_MANAGERS/RESEARCHES/
    └── Structure:
        ├── 00_SEARCH_QUEUE/ - Search assignment & tracking
        ├── 01_VIDEO_QUEUE/ - Video accumulation & prioritization
        ├── 02_TRANSCRIPTIONS/ - 23 video transcriptions
        ├── 03_ANALYSIS/ - Extractions, Gap Analysis, Library Mapping
        ├── 04_INTEGRATION/ - Integration tracking
        ├── PROMPTS/ - 26 research prompts
        ├── DATA/ - Research data & metadata
        ├── REPORTS/ - Research reports
        └── ARCHIVE/ - Archived content
```

---

## Usage Examples

### Entity Identification

```
PRT-001 = Project Template #001 (AI Tutorial Research)
MLT-005 = Milestone Template #005 (Synthesis Recommendations)
TST-042 = Task Template #042 (Onboard New Employee)
STT-156 = Step Template #156 (Specific procedure step)
CHT-071 = Checklist Template #071 (Verification item)
WRF-002 = Workflow #002 (Lead Enrichment Automation)
GDS-003 = Guide #003 (Designer Integration Summary)
PRM-004 = Prompt #004 (VS Code Agent Research)
RSR-009 = Research #009 (Video Analysis 008)
RSR-024 = Research #024 (Video Analysis 023 - Google AI Studio)
```

### Department-Entity Relationships

```
AID + TST-046 = AI Department owns Task Template 046 (Automate Version Control)
HRM + TST-007 = HR Management owns Task Template 007 (Create Job Posting)
DEV + TST-008 = Development owns Task Template 008 (Create MCP Connector)
LGN + TST-001 = Lead Generation owns Task Template 001 (AI-Powered HTML Parsing)
DGN + TST-068 = Design owns Task Template 068 (Publish Behance Project)
VID + TST-045 = Video owns Task Template 045 (Research Video Tools)
SLS + TST-021 = Sales owns Task Template 021 (Old Client Re-Engagement)
```

---

## Validation Checksum

| Entity Type | ISO Code | Count | ID Range | Status |
|-------------|----------|-------|----------|--------|
| **Meta-Level Categories** | **TSM** | **8** | **TSM-001 to TSM-008** | **✓ Valid** |
| Project Templates | PRT | 9 | PRT-001 to PRT-009 | ✓ Valid |
| Milestone Templates | MLT | 28 | MLT-001 to MLT-028 | ✓ Valid |
| Task Templates | TST | 71 | TST-001 to TST-071 | ✓ Valid |
| Step Templates | STT | 379 | STT-001 to STT-379 | ✓ Valid |
| Checklist Templates | CHT | 98 | CHT-001 to CHT-098 | ✓ Valid |
| Workflows | WRF | 20 | WRF-001 to WRF-020 | ✓ Valid |
| Guides | GDS | 8+ | GDS-001 onwards | ✓ Valid |
| Prompts | PRM | 100+ | PRM-001 onwards | ✓ Valid |
| Researches | RSR | 24+ | RSR-001 to RSR-024+ | ✓ Valid |
| **TOTAL** | **10 types** | **752+** | - | **✓ Valid** |

---

## Migration History

### 2025-11-17: Department Consolidation
- **OPS** (Operations) → **AID** (AI Department)
- **ADM** (Administration) → **AID** (AI Department)
- All OPS and ADM entities reassigned to AID

### 2025-11-18: Taxonomy Standardization
- Implemented consonant-only 3-letter ISO codes
- Added 'T' suffix for all Template entities
- Created hierarchical ID system
- Established department code registry

### 2025-11-20: Meta-Level TSM Implementation
- Added **TSM** (Task System Meta) code for meta-level category organization
- Created 8 TSM entries (TSM-001 to TSM-008) for entity type categories
- Enhanced hierarchy to show TSM → ISO code → template instance relationships
- Total system now includes 10 ISO code types (1 meta + 9 entity types)

---

## Cross-References

**Related Documentation:**
- [Taxonomy_Master_List.csv](Taxonomy_Master_List.csv) - Complete entity catalog
- [Taxonomy_Hierarchy_Tree.md](Taxonomy_Hierarchy_Tree.md) - Parent-child relationships
- [Taxonomy_Department_Distribution.md](Taxonomy_Department_Distribution.md) - Department breakdowns
- [Taxonomy_Migration_Map.json](Taxonomy_Migration_Map.json) - ID migration mappings

---

## Notes

1. **Scalability:** Current system supports up to 999 entities per type (001-999)
2. **Uniqueness:** All ISO-### combinations are globally unique across TASK_MANAGERS
3. **Consistency:** Template suffix 'T' consistently applied to all template entity types
4. **Future-Proof:** Reserved codes available for new entity types as system grows
5. **Human-Readable:** Codes designed to be memorable and intuitive for daily use
6. **Department-Agnostic:** Entity type codes work independently of department assignments

---

**End of ISO Code Registry**
