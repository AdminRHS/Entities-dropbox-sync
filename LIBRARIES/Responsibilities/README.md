# Responsibilities Ecosystem

**Version:** 2.0
**Last Updated:** 2025-11-17
**Status:** ✅ Production Ready

A unified system for managing organizational responsibilities, action-object mappings, parameter integrations, and department-specific views.

---

## Overview

The Responsibilities Ecosystem provides a centralized, structured approach to managing:
- **193 Responsibilities** across 8 departments
- **209 Phrase Matching Patterns** for fuzzy lookups
- **57 Action Variants** and **169 Object Variants** for flexible matching
- **7,321 Parameter-Object Mappings** (473 state-based + 6,848 quality-based)
- **8 Department-Specific Views** for role-based access

### Key Features

✅ **Unified Structure** - Single source of truth for all responsibilities
✅ **Fast Lookups** - Indexed phrase matching for quick resolution
✅ **Flexible Matching** - Action and object variant support
✅ **Department Views** - Role-based filtering and access
✅ **Parameter Integration** - Rich parameter-to-object-type mappings
✅ **Automated Validation** - Built-in integrity checking
✅ **Backward Compatible** - Works with existing task/step templates

---

## Quick Start

### Loading Responsibilities

```python
import json

# Load responsibilities master
with open('LIBRARIES/Responsibilities/Core/responsibilities_master.json', 'r', encoding='utf-8') as f:
    responsibilities = json.load(f)

print(f"Loaded {len(responsibilities)} responsibilities")
# Output: Loaded 193 responsibilities
```

### Finding a Responsibility

```python
# Load phrase index
with open('LIBRARIES/Responsibilities/Core/phrase_matching_index.json', 'r', encoding='utf-8') as f:
    phrase_index = json.load(f)

# Find responsibility by action + object
key = "configure+api"
if key in phrase_index:
    resp_id = phrase_index[key]['responsibility_id']
    print(f"Responsibility: {resp_id}")
```

---

## Directory Structure

```
LIBRARIES/Responsibilities/
├── Core/
│   ├── responsibilities_master.json           # 193 responsibilities
│   ├── phrase_matching_index.json             # 209 phrase patterns
│   ├── action_variants_map.json               # 57 action synonyms
│   ├── object_variants_map.json               # 169 object variants
│   └── By_Department/
│       ├── AI_Responsibilities.json           # 80 responsibilities
│       ├── LG_Responsibilities.json           # 64 responsibilities
│       ├── DEV_Responsibilities.json          # 34 responsibilities
│       ├── HR_Responsibilities.json           # 6 responsibilities
│       ├── OPS_Responsibilities.json          # 22 responsibilities
│       ├── MKT_Responsibilities.json          # 8 responsibilities
│       ├── CNT_Responsibilities.json          # 5 responsibilities
│       └── ECM_Responsibilities.json          # 1 responsibility
│
├── Actions/                                   # 27 action definition files
├── Objects/                                   # 13 object definition files
├── Parameters/                                # 15 parameter definition files
│
├── parameter_object_mapping.json              # 7,321 mappings
├── parameter_views_by_profession.json         # Profession-organized views
│
├── migrate_references.py                      # Path migration script
├── validate_ecosystem.py                      # Ecosystem validation script
├── create_parameter_mapping.py                # Parameter mapping generator
│
├── INTEGRATION_COMPLETE_REPORT.md             # Migration report
├── PROMPT_Migrate_Step_Coverage.md            # Step coverage guide
└── README.md                                  # This file
```

---

## Core Concepts

### Responsibilities

A responsibility is a unique action-object combination representing an organizational duty.

**ID Format:** `RESP-{DEPT}-{NUM}`

**Example:**
```json
{
  "id": "RESP-AI-001",
  "primary_phrase": "extract videos",
  "action_base": "extract",
  "object_base": "videos",
  "departments": "AI",
  "is_active": true
}
```

### Phrase Matching

Fast lookup index for action-object pairs.

**Key Format:** `{action}+{object}`

**Example:** `"configure+api"` → `"RESP-DEV-007"`

### Variants

- **Action Variants:** Synonyms for actions (e.g., "configure" → ["setup", "initialize"])
- **Object Variants:** Alternative names for objects (e.g., "database" → ["db", "data store"])

---

## Usage Examples

### Find Responsibility with Variants

```python
def find_responsibility(action, obj, phrase_index, action_variants, object_variants):
    """Find responsibility using phrase matching with variants"""

    # Normalize
    action = action.lower().strip()
    obj = obj.lower().strip()

    # Try exact match
    key = f"{action}+{obj}"
    if key in phrase_index:
        return phrase_index[key]['responsibility_id']

    # Try action variants
    for variant in action_variants.get(action, [action]):
        key = f"{variant}+{obj}"
        if key in phrase_index:
            return phrase_index[key]['responsibility_id']

    return None
```

### Get Department Responsibilities

```python
# Load AI department responsibilities
with open('Core/By_Department/AI_Responsibilities.json', 'r', encoding='utf-8') as f:
    ai_resp = json.load(f)

print(f"AI has {len(ai_resp)} responsibilities")
```

### Get Parameters for Object

```python
# Load parameter views
with open('parameter_views_by_profession.json', 'r', encoding='utf-8') as f:
    param_views = json.load(f)

# Get parameters for HR/Recruiter candidates
prof = param_views['professions']['HR/Recruiter']
params = prof['objects'].get('candidates', [])
print(f"Found {len(params)} parameters")
```

---

## Department Views

| Department | Code | Count | File |
|------------|------|-------|------|
| AI | AI | 80 | `AI_Responsibilities.json` |
| Lead Generation | LG | 64 | `LG_Responsibilities.json` |
| Development | DEV | 34 | `DEV_Responsibilities.json` |
| Operations | OPS | 22 | `OPS_Responsibilities.json` |
| Marketing | MKT | 8 | `MKT_Responsibilities.json` |
| Human Resources | HR | 6 | `HR_Responsibilities.json` |
| Content | CNT | 5 | `CNT_Responsibilities.json` |
| E-commerce | ECM | 1 | `ECM_Responsibilities.json` |

---

## Parameter Integration

### State-Based Parameters (473 mappings)

Metrics for objects in lifecycle states (new, in work, sold, banned, free).

**Example:**
```json
{
  "parameter": "conversion rate",
  "parameter_type": "new",
  "object": "accounts",
  "profession": "Lead Generator"
}
```

### Quality-Based Parameters (6,848 mappings)

Intrinsic quality metrics (accuracy, clarity, engagement, completeness).

**Example:**
```json
{
  "parameter": "accuracy",
  "object": "blueprints",
  "profession": "3d designer"
}
```

---

## Validation & Scripts

### Validate Ecosystem

```bash
python validate_ecosystem.py
```

**Output:**
- Directory structure checks
- File count validation
- JSON parsing verification
- Department view validation

### Migrate Paths

```bash
python migrate_references.py
```

Scans task/step templates for outdated path references.

### Generate Parameter Mappings

```bash
python create_parameter_mapping.py
```

Creates parameter_object_mapping.json from Parameters and Objects.

---

## Statistics

### Coverage Metrics

| Metric | Value |
|--------|-------|
| Total Responsibilities | 193 |
| Phrase Patterns | 209 |
| Action Variants | 57 |
| Object Variants | 169 |
| Parameter Mappings | 7,321 |
| Mapping Coverage | 69.1% |
| Departments | 8 |
| Professions | 7 |

### Department Distribution

```
AI  (41.5%): ████████████████████████████████████████ 80
LG  (33.2%): █████████████████████████████░░░░░░░░░░ 64
DEV (17.6%): ████████████████░░░░░░░░░░░░░░░░░░░░░░░ 34
OPS (11.4%): ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 22
MKT  (4.1%): ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  8
HR   (3.1%): ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  6
CNT  (2.6%): ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  5
ECM  (0.5%): █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  1
```

---

## Troubleshooting

### JSON Parse Error

**Error:** `JSONDecodeError: Unexpected UTF-8 BOM`

**Solution:**
```python
with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
```

### Responsibility Not Found

1. Check spelling and normalization
2. Try action/object variants
3. Verify responsibility exists in master list

### File Not Found

Use absolute paths from ENTITIES directory:
```python
from pathlib import Path

ENTITIES_DIR = Path(__file__).resolve().parent.parent.parent
RESP_DIR = ENTITIES_DIR / "LIBRARIES" / "Responsibilities"
```

---

## Related Documentation

- [INTEGRATION_COMPLETE_REPORT.md](INTEGRATION_COMPLETE_REPORT.md) - Full migration details
- [PROMPT_Migrate_Step_Coverage.md](PROMPT_Migrate_Step_Coverage.md) - Step coverage guide

---

## Version History

### v2.0 (2025-11-17) - Current
- ✅ Unified Actions, Objects, Parameters into single ecosystem
- ✅ Created 8 department-specific views
- ✅ Generated 7,321 parameter-object mappings
- ✅ Built automation scripts
- ✅ 100% validation pass rate

### v1.0 (Previous)
- Separate libraries
- No department views
- No parameter integration

---

**Status:** ✅ Production Ready
**Next Milestone:** Step Coverage Migration (83.3% → 95%+)
