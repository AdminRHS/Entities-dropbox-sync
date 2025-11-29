# TALENTS ISO Code Registry

**Last Updated:** 2025-11-28

## Overview

The TALENTS entity uses standardized ISO-style codes for consistent identification across the system.

## Employee Type Codes

| ISO Code | Entity Type | Description | Count |
|----------|-------------|-------------|-------|
| **EMP** | Employees | All employee profiles (active and former) | 65 |

## Status Codes

| Status | Code | Count | Description |
|--------|------|-------|-------------|
| Work | EMP-WRK | 11 | Currently working employees |
| Available | EMP-AVL | 20 | Available for assignments |
| Project | EMP-PRJ | 22 | Project-based employees |
| Part Project + Part Time | EMP-PPT | 2 | Mixed engagement |
| Part Project + Part Project | EMP-PPP | 1 | Multiple projects |
| Full Project + Part Time | EMP-FPT | 1 | Full project + part time |
| Pending | EMP-PND | 2 | Pending onboarding |
| Left | EMP-LFT | 2 | Departed employees |
| Fired | EMP-FRD | 4 | Terminated employees |

## Department Distribution

Uses LIBRARIES department codes:

| Department | Code | Count | Description |
|------------|------|-------|-------------|
| Design | DGN | 0 | Design department |
| Lead Generation | LGN | 0 | Lead generation & sales |
| Development | DEV | 0 | Software development |
| Video | VID | 0 | Video production |
| AI | AIA | 0 | AI & automation |
| Marketing | MKT | 0 | Marketing department |
| Finance | FIN | 0 | Finance & accounting |
| Executive | EXE | 0 | Executive team |

## File Naming Convention

- **Format:** `EMP-{5-digit}.md`
- **Examples:**
  - `EMP-00299.md` (ID: 299)
  - `EMP-87995.md` (ID: 87995)
  - `EMP-88105.md` (ID: 88105)

## Integration with Other Taxonomies

- **Professions:** Links to `TAX-001_Libraries/LBS_005_Professions/`
- **Tools:** Links to `TAX-001_Libraries/LBS_003_Tools/`
- **Task Managers:** Links to `TAX-002_Task_Managers/`

## See Also

- [Talents Master List](Talents_Master_List.csv) - Complete employee registry
- [Talents Hierarchy Tree](Talents_Hierarchy_Tree.md) - Organizational hierarchy
- [Talents Department Distribution](Talents_Department_Distribution.md) - Statistics by department
