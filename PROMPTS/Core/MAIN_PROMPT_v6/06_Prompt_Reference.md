# 6. PROMPT REFERENCE

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## KEY PROMPTS (Quick Reference)

**Daily Operations:**
- **PMT-033 to PMT-043** - Department daily reports (AID, VID, HRM, DEV, LGN, DGN, MKT, SLS, SMM, FIN)
- **PMT-032** - Collection/aggregation of all department reports

**Research (Cross-Department):**
- **PMT-004 to PMT-013** - Video processing (VID leads)
- **PMT-044, PMT-051** - Web/sales research (SLS, LGN)
- **PMT-045** - Document analysis (SMM, HRM, SLS)
- **PMT-046-052** - Platform research (DEV, AID)

**Task Management:**
- **PMT-061** - Project/milestone setup (PRT-###, MLT-###)
- **PMT-062** - Tool & guide matching (TOL-###, GDS-###)

**System:**
- **PMT-029** - System health review
- **PMT-072** - Critical fixes

---

## RUNNING PROJECTS (Examples)

**Active Project Tracking:**

Use [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011) to classify tasks into existing projects:

- **PRT-001 to PRT-009** - Review existing projects before creating new
- Daily tasks → Extract as TST-### → Map to existing PRT-### or create new
- Use task-first approach: TST → MLT → PRT (bottom-up)

**Workflow:**
1. Employee submits daily report in Nov25/ or Finance 2025/
2. Extract TST-### (tasks) and STT-### (steps)
3. Check against existing PRT-001 through PRT-009
4. Link to TOL-### (tools) and GDS-### (guides)
5. Generate department report (PMT-033 to PMT-043)
