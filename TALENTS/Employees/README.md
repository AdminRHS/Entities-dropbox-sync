# Employees Sub-Entity

**Parent Entity:** TALENTS
**Entity Code:** EMP
**Total Profiles:** 65 (52 active, 13 former)
**Last Updated:** 2025-11-28

## Overview

The Employees sub-entity contains all employee profiles organized by unique Employee IDs (EMP-XXXXX format).

## Navigation

**Start Here:** [INDEX.md](INDEX.md) - Comprehensive employee lookup with 5 different views

## File Structure

- **Profiles/** - Active employees (52)
- **Left/** - Former employees (13)
- **ORPHANED/** - Profiles needing ID assignment
- **INDEX.md** - Main navigation hub
- **Employee_Profile_Schema.md** - Template for new profiles
- **MIGRATION_MAP.json** - Migration history

## File Naming

All employee profiles use the format: `EMP-{5-digit}.md`

Examples:
- `EMP-00299.md` (ID: 299)
- `EMP-87995.md` (ID: 87995)
- `EMP-88105.md` (ID: 88105)

## Finding Employees

Use [INDEX.md](INDEX.md) with these lookup methods:
1. **By Employee ID** - Direct lookup (EMP-XXXXX)
2. **By Name** - Alphabetical listing
3. **By Department** - Filter by department
4. **By Profession** - Filter by job role
5. **By Status** - Filter by employment status

## Profile Fields

Each employee profile contains:
- ID, Name, Age, Country
- Status, Department, Profession, Rate
- Contact Info (Email, Discord, Phone, Telegram)
- Skills, Tools, Summary
- Start Date, Nov25 Folder

## Automation

Profiles are automatically synced daily from:
- **Finance Public** - Core employment data
- **Nov25 Folders** - Detailed work data

Manual sync: `python3 automations/employee-profile-manager/sync_profiles.py`

## Related Files

- **Taxonomy:** [ENTITIES/TAXONOMY/TAX-003_Talents/](../../TAXONOMY/TAX-003_Talents/)
- **Automation:** `automations/employee-profile-manager/`
- **Finance Public:** Source of truth for core data

---

*Navigate using [INDEX.md](INDEX.md) for the best experience*
