# PROJ-AI-NMP-001: Next Main Prompt Version (v5)

## Project Overview

**Status:** 🟡 Planned
**Progress:** 0% Complete
**Department:** AI
**Priority:** High
**Created:** 2025-11-15
**Target Completion:** 2025-12-15

---

## Quick Links

- **Project Instance:** [project_instance.json](project_instance.json)
- **Meta-Prompt:** [CREATE_MAIN_PROMPT_v5.md](C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Core\CREATE_MAIN_PROMPT_v5.md)
- **Source (v4):** [MAIN_PROMPT_v4.md](C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Core\MAIN_PROMPT_v4.md)
- **Target Output:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\Core\MAIN_PROMPT_v5_Modular\`

---

## Description

Transform MAIN_PROMPT v4 from a monolithic 2,538-line file into a highly maintainable modular system consisting of ~50 individual files across 5 main folders. Each module will be enhanced with detailed integration to all 12 LIBRARIES entities, updated with current statistics, and improved cross-referencing.

---

## Objectives

1. ✅ Create modular architecture with ~50 files across 5 folders
2. ✅ Integrate all 12 LIBRARIES entities with current statistics
3. ✅ Break down 21 output templates into individual files
4. ✅ Update statistics (429 actions, 10,596 parameters, etc.)
5. ✅ Build assembly system for generating monolithic versions
6. ✅ Provide comprehensive logging and progress tracking

---

## Project Structure

```
MAIN_PROMPT_v5_Modular/
├── 00_Core/ (5 files)
│   ├── Purpose, Vision, Company Context
│   ├── Employee Directory (32 employees)
│   └── Project Directory (31+ projects)
│
├── 01_Library_Integration/ (13 files)
│   ├── 12 individual library integration modules
│   └── Taxonomy Framework overview
│
├── 02_Output_Templates/ (22 files)
│   ├── 21 individual section templates
│   └── README with integration guide
│
├── 03_Processing_Rules/ (6 files)
│   ├── Entity recognition patterns
│   └── Cross-reference rules
│
├── 04_Usage/ (7 files)
│   ├── Usage instructions
│   ├── Examples
│   ├── CHANGELOG
│   └── Migration guide (v4 → v5)
│
└── scripts/ (4 files)
    └── Python assembly scripts
```

---

## Phases & Milestones

### Phase 1: Setup & Infrastructure (3 days)
- [MIL-001](Milestones/MIL-001_Folder_Structure_Creation.json) - Folder Structure Creation
- [MIL-002](Milestones/MIL-002_Core_Modules.json) - Core Modules Complete

### Phase 2: Library Integration (7 days)
- [MIL-003](Milestones/MIL-003_Library_Integration_Modules.json) - Library Integration Modules Complete

### Phase 3: Template Creation (10 days)
- [MIL-004](Milestones/MIL-004_Output_Templates.json) - Output Templates Complete
- [MIL-005](Milestones/MIL-005_Processing_Rules.json) - Processing Rules Complete

### Phase 4: Documentation & Assembly (5 days)
- [MIL-006](Milestones/MIL-006_Usage_Maintenance.json) - Usage & Maintenance Docs Complete
- [MIL-007](Milestones/MIL-007_Assembly_System.json) - Assembly System Complete

### Phase 5: Validation & QA (5 days)
- [MIL-008](Milestones/MIL-008_Validation_QA.json) - Validation & QA Complete

---

## Current Status Dashboard

### Overall Progress

| Phase | Milestones | Status | Progress |
|-------|-----------|--------|----------|
| Phase 1: Setup & Infrastructure | 2 | 🟡 Planned | 0% |
| Phase 2: Library Integration | 1 | 🟡 Planned | 0% |
| Phase 3: Template Creation | 2 | 🟡 Planned | 0% |
| Phase 4: Documentation & Assembly | 2 | 🟡 Planned | 0% |
| Phase 5: Validation & QA | 1 | 🟡 Planned | 0% |

### Milestone Status

| ID | Milestone | Target Date | Status | Progress |
|----|-----------|-------------|--------|----------|
| MIL-001 | Folder Structure Creation | 2025-11-17 | 🟡 Planned | 0% |
| MIL-002 | Core Modules | 2025-11-18 | 🟡 Planned | 0% |
| MIL-003 | Library Integration | 2025-11-25 | 🟡 Planned | 0% |
| MIL-004 | Output Templates | 2025-12-04 | 🟡 Planned | 0% |
| MIL-005 | Processing Rules | 2025-12-06 | 🟡 Planned | 0% |
| MIL-006 | Usage & Maintenance | 2025-12-09 | 🟡 Planned | 0% |
| MIL-007 | Assembly System | 2025-12-11 | 🟡 Planned | 0% |
| MIL-008 | Validation & QA | 2025-12-15 | 🟡 Planned | 0% |

### Task Summary

- **Total Tasks:** 40 (mapped to 40-iteration workflow)
- **Completed:** 0
- **In Progress:** 0
- **Pending:** 40

---

## Deliverables

| ID | Deliverable | Milestone | Files | Status |
|----|-------------|-----------|-------|--------|
| DEL-001 | Modular Folder Structure | MIL-001 | 5 folders + READMEs | Pending |
| DEL-002 | Core Modules | MIL-002 | 5 files | Pending |
| DEL-003 | Library Integration Modules | MIL-003 | 13 files | Pending |
| DEL-004 | Output Templates | MIL-004 | 22 files | Pending |
| DEL-005 | Processing Rules | MIL-005 | 6 files | Pending |
| DEL-006 | Usage & Maintenance Docs | MIL-006 | 7 files | Pending |
| DEL-007 | Assembly System | MIL-007 | 4 scripts | Pending |
| DEL-008 | MAIN_PROMPT_v5.md | MIL-008 | 1 file | Pending |

---

## Key Statistics to Integrate

### LIBRARIES Entity Counts (as of 2025-11-15)

| Library | Count | Files |
|---------|-------|-------|
| Actions | 429 actions | Actions_Master.json + 12 Data Operations files |
| Objects | 36 objects | 4 collections |
| Processes | 428 processes | Processes_Master.json + Workflows |
| Results | 432 results | Results_Master.json |
| Skills | 12+ skills | By department (AI, DEV, LG, OPS) |
| Responsibilities | Multiple | responsibilities.json |
| Products | 39 products | Products_Master.json + Index |
| Services | 7 categories | Content, Design, LG, Marketing, SEO, Tech, Video |
| Parameters | 10,596+ | Organized by dept & profession |
| Professions | 12+ | Individual profession files |
| Tools | 75+ tools | 21 AI, 18 Dev, 7 DB, etc. |
| Prompts | Multiple | Core, Daily Reports, Video, Library, etc. |

---

## Success Criteria

### Quantitative
- [ ] ~50 files created across 5 folders
- [ ] All 12 libraries integrated with current statistics
- [ ] 21 individual output templates created
- [ ] 100% of v4 functionality preserved
- [ ] Assembly scripts generate valid markdown

### Qualitative
- [ ] Modular structure improves maintainability
- [ ] Documentation is comprehensive and clear
- [ ] Examples are realistic and helpful
- [ ] Migration from v4 is straightforward

---

## Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Library statistics change during development | Medium | High | Final statistics update in validation phase |
| Template structure changes from v4 | Low | Low | Follow v4 structure closely, only enhance |
| Assembly scripts may not work cross-platform | Medium | Medium | Test on Windows, provide alternatives |

---

## Dependencies

- ✅ Access to all LIBRARIES entity files
- ✅ MAIN_PROMPT_v4.md as source
- ⏳ Python environment for assembly scripts (to be verified)

---

## Stakeholders

- **Project Owner:** ALX
- **Project Manager:** AI Department
- **Primary Assignee:** Claude (AI Assistant)
- **Reviewers:** ALX, AI Team
- **Stakeholders:** All Departments

---

## Logs & Documentation

### Progress Logs
- [Setup Log](Logs/00_Setup_Log.md) - Initial configuration and decisions
- [Progress Log](Logs/01_Progress_Log.md) - Daily/weekly progress tracking
- [Issues Log](Logs/02_Issues_Log.md) - Problems and resolutions
- [Decisions Log](Logs/03_Decisions_Log.md) - Architecture/design decisions
- [Statistics Log](Logs/04_Statistics_Log.md) - Library statistics updates
- [Completion Report](Logs/05_Completion_Report.md) - Final summary

---

## Related Resources

### TASK_MANAGERS Links
- **Project Templates:** `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Project_Templates\`
- **Task Templates:** `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Task_Templates\`
- **Step Templates:** `C:\Users\Dell\Dropbox\Entities\TASK_MANAGERS\Step_Templates\`

### LIBRARIES Links
- **Actions:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Actions\`
- **Objects:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Objects\`
- **Processes:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Processes\`
- **Results:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Results\`
- **Skills:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Skills\`
- **Parameters:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Parameters\`
- **Tools:** `C:\Users\Dell\Dropbox\Entities\LIBRARIES\Tools\`
- **Prompts:** `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\DEPARTMENTS\_SHARED\Prompts\`

---

## Notes

- This project follows the 40-iteration workflow defined in CREATE_MAIN_PROMPT_v5.md
- Focus on accuracy of library statistics extracted from actual files
- All examples should use real entity IDs from LIBRARIES
- Maintain compatibility with v4 while improving structure
- Both modular and monolithic versions will be maintained

---

## Version History

**Version 1.0** - 2025-11-15
- Initial project setup
- Project instance created
- Milestone structure defined
- Logging system configured

---

**Last Updated:** 2025-11-15
**Next Review:** 2025-11-17 (After MIL-001 completion)
