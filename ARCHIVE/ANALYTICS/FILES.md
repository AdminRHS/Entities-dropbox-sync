# ANALYTICS – Files Overview

**Purpose:** Summarize the key files and folders in the `ANALYTICS` entity, with a focus on reports, scripts, and project-level analytics infrastructure.  
**Last Updated:** 2025-11-17

---

## Core Documentation

- `README.md` – Entity-level documentation describing purpose, sub-entities, usage patterns, and migration history.
- `INDEX.md` – High-level index and visual structure of the `ANALYTICS` entity.
- `REPORTS/PARSE_AND_REORGANIZE_PLAN.md` – Plan for restructuring analytics reports, scripts, and data.

---

## Analytics Infrastructure

- `Projects/` – Project instances and execution tracking (e.g., `PROJ-001_ENTITIES_Analysis`).
- `Milestones/` – Central milestone tracking JSON files (MIL-001–MIL-00X).
- `Tasks/` – Task execution instances.
- `Steps/` – Step execution instances.
- `REPORTS/System_Analysis/` – Existing system analysis reports and data files by milestone.

---

## Scripts

- `cleanup_duplicate_milestones.py` – Utility script for cleaning up duplicate milestone records.
- `move_milestones_to_central.py` – Script to consolidate milestone files into the central `Milestones/` folder.
- `REPORTS/System_Analysis/milestone_01_inventory.py` – Data inventory analysis script for Milestone 01.
- `REPORTS/System_Analysis/milestone_02_schema_naming.py` – Schema naming analysis script for Milestone 02.
- `REPORTS/System_Analysis/milestone_03_terminology.py` – Terminology and content analysis script for Milestone 03.
- `REPORTS/System_Analysis/milestone_04_relationships.py` – Relationship validation script for Milestone 04.

---

## Attendance Report Extractor

- `EMPLOYEES_Attendance_Remote_Helpers_Extractor.py` – Fetches yesterday’s Remote Helpers attendance from the CRM-S API and writes a daily CSV report to the `ANALYTICS` folder.
- `tests/test_attendance_extractor.py` – Pytest suite covering happy path, empty-data edge case, and HTTP failure scenarios for the attendance extractor.
- **Output Pattern:** `ANALYTICS_Employees_Attendance_Remote_Helpers_YYYY_MM_DD.csv` saved under `C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS`.

---

## Maintenance Notes

- Update this `FILES.md` whenever new analytics scripts, report generators, or project-level tools are added.
- Keep each file under 500 lines; split large modules into smaller, focused components when needed.
- Ensure new utilities include clear Google-style docstrings and are covered by Pytest tests under `ANALYTICS/tests/`.


