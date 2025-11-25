# Step_Templates ISO Code Registry

## Overview
The code `STT` follows the standard 3-letter consonant-only convention and ends with 'T' as step templates ARE templates for step execution.

## ISO Code Definition

### Primary Code
- **Code**: `STT`
- **Full Name**: Step_Templates
- **Entity Type**: Execution Templates
- **Description**: Detailed step-by-step execution templates for task completion
- **Template Status**: Template (ends with 'T')

### Code Structure
```
STT-XXX
│   └── Sequential 3-digit number (001-252 currently allocated)
└── Step_Templates identifier (ends with T for template)
```

## Department Codes

| Code | Department | Count | Percentage |
|------|------------|-------|------------|
| **DGN** | Design | 61 | 24.2% |
| **VID** | Video | 59 | 23.4% |
| **HRM** | Human Resources | 42 | 16.7% |
| **DEV** | Development | 33 | 13.1% |
| **SLS** | Sales | 27 | 10.7% |
| **LGN** | Lead Generation | 21 | 8.3% |
| **AID** | AI Department | 9 | 3.6% |

## File Format Distribution

### JSON Format (STT-001 to STT-070) - 70 Templates
**Characteristics**:
- Complex steps with full metadata
- Execution details documented
- Tool requirements specified
- Input/output definitions
- Success criteria defined
- Estimated duration included

**Primary Departments**: HRM, VID

### Markdown Format (STT-071 to STT-252) - 182 Templates
**Characteristics**:
- Lightweight, human-readable format
- Basic step structure
- Quick reference documentation
- Simplified execution guidelines

**Primary Departments**: DGN, DEV, SLS, LGN

## ID Allocation

### Current Range
- **Allocated**: STT-001 to STT-252 (252 step templates)
- **Available**: STT-253 to STT-999 (747 IDs remaining)

### Reserved Ranges
- `STT-001 to STT-299`: General step templates (current usage)
- `STT-300 to STT-399`: Reserved for video production expansion
- `STT-400 to STT-499`: Reserved for design workflow expansion
- `STT-500 to STT-599`: Reserved for development workflow expansion
- `STT-600 to STT-999`: Available for future use

## Cross-References

### Integration with Other TASK_MANAGERS
- **Task_Templates (TST)**: Step templates are children of task templates
- **Checklist_Items (CHT)**: Checklists associated with step templates
- **Workflows (WRF)**: Steps execute within workflow contexts
- **GUIDES (GDS)**: Steps reference operational guides

---

**Last Updated**: 2025-11-19
**Version**: 1.0
**Total Step Templates**: 252
