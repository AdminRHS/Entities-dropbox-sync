# TALENTS Entity

**Entity Type:** TALENTS
**Sub-Entities:** Employees, Skills, Candidates, Templates, Job Applications
**Taxonomy Code:** TAX-003
**Last Updated:** 2025-11-28

## Overview

The TALENTS entity manages all human capital resources for the organization, including employee profiles, skills inventories, candidate pipelines, and employment templates.

## Structure

```
TALENTS/
├── README.md (this file)
├── INDEX.md (top-level talent index)
├── employees.json (master employee registry)
│
├── Employees/ (primary sub-entity)
│   ├── INDEX.md (employee navigation hub)
│   ├── README.md
│   ├── Employee_Profile_Schema.md
│   ├── Profiles/ (active employees: 52)
│   ├── Left/ (former employees: 13)
│   ├── ORPHANED/ (profiles needing review)
│   └── MIGRATION_MAP.json
│
├── Skills/ (skills inventory)
├── Candidates_JSON_Clusters/ (candidate data)
├── Templates/ (employment templates)
└── JobApplications/ (application tracking)
```

## Quick Links

- **Employee INDEX:** [Employees/INDEX.md](Employees/INDEX.md)
- **Taxonomy:** [TAX-003_Talents/](../TAXONOMY/TAX-003_Talents/)
- **Automation:** automations/employee-profile-manager/

## Statistics

- **Total Employees:** 65 (52 active, 13 former)
- **Departments:** 6+ (Design, LG, Dev, Video, AI, Finance)
- **Professions:** 15+ (lead generator, ui/ux designer, developer, etc.)

---

*Part of the ENTITIES ecosystem*
