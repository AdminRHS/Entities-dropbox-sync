# 3. WORKFLOW EXECUTION

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## VIDEO PROCESSING

**PMT-004: Video Transcription → TASK_MANAGERS Extraction**

```
Input: Video transcript
Output: JSON with MLT-###, TST-###, STT-### entities

Steps:
1. Load transcript
2. Identify milestones (project phases)
3. Extract tasks per milestone
4. Break tasks into steps
5. Assign sequential IDs
6. Validate against TSM-00X_[Category]/[Entity]_Master_List.csv
7. Reference GDS-010 for workflow structure
8. Save JSON output
```

**Complete Workflow Chain:**
```
PMT-004 (Transcribe) → PMT-006 (Analyze) → PMT-007 (Extract Objects)
→ PMT-009 (Taxonomy Integration) → PMT-032 (Report)
```

## DAILY REPORTS

**Collection:** PMT-032 aggregates all departments

**Department Prompts:**
| Dept | PMT | Use For |
|------|-----|---------|
| AI & Automation | PMT-033 | Taxonomy, automation, system work |
| Design | PMT-035 | Creative assets, UI/UX |
| Dev | PMT-036 | Code, APIs, version control |
| Finance | PMT-037 | Financial reporting |
| HR | PMT-038 | Recruitment, onboarding |
| Lead Gen | PMT-039 | Prospecting, data research |
| Marketing | PMT-040 | Campaigns, content |
| Sales | PMT-041 | Pipeline, deals |
| Social Media | PMT-042 | Engagement, content |
| Video | PMT-043 | Production, editing |

**Daily Ops Workflow:**
```bash
# Run all department reports
for dept in AID DGN DEV FIN HRM LGN MKT SLS SMM VID; do
  execute_prompt "PMT-0XX_${dept}_Daily_Report" >> daily_reports/$(date +%Y-%m-%d)_${dept}.md
done

# Aggregate
execute_prompt "PMT-032" >> daily_reports/$(date +%Y-%m-%d)_COLLECTION.md
```

## RESEARCH INTEGRATION

**Prompts:** PMT-044 to PMT-052

| PMT | Purpose |
|-----|---------|
| PMT-044 | Sales Department Research |
| PMT-045 | SMM Document Processing |
| PMT-046 | VSCode Agent HQ Research |
| PMT-047 | YouTube AI HR Tutorials |
| PMT-048 | YouTube AI Tools Daily |
| PMT-049 | YouTube HR Automation |
| PMT-050 | YouTube Remote Helpers |
| PMT-051 | Department Research Integration |
| PMT-052 | VSCode AI Extensions |

**Workflow:** Research → Extract entities → Match to LIBRARIES → Update taxonomies → Report

## TASK MANAGER OPERATIONS

| Workflow | Prompt | Entities | Validation |
|----------|--------|----------|------------|
| Project Setup | PMT-061 | PRT-###, MLT-### | Check PRT CSV for duplicates |
| Task Breakdown | Manual | TST-###, STT-### | Reusable templates (many-to-many) |
| Tool & Guide Match | PMT-062 | TOL/GDS refs | Match to existing TOL-### and GDS-### |
| Entity Filling | PMT-061 | All types | Complete metadata required |

## HR AUTOMATION

| PMT | Function |
|-----|----------|
| PMT-053 | CV Parser - Extract structured data from resumes |
| PMT-054 | CRM Data Entry - Automate candidate info entry |
| PMT-055 | Communication Templates - Generate outreach emails |
| PMT-056 | Interview Conductor - Guide structured interviews |
| PMT-057 | Job Sites Research - Deep research recruitment platforms |

## SYSTEM MAINTENANCE

| PMT | Function |
|-----|----------|
| PMT-021 to PMT-026 | Ecosystem Analysis (5 milestones) |
| PMT-027 | Data Consistency checks |
| PMT-028 | Folder Reorganization |
| PMT-029 | System Health Review |
| PMT-072 | PROMPTS Critical Fixes |
