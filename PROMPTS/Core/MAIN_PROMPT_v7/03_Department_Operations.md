# 3. DEPARTMENT OPERATIONS

**Version:** 7.0 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v7 System

---

## DEPARTMENTS (10)

| Code | Department | Daily Report | Focus Areas |
|------|-----------|--------------|-------------|
| **AID** | AI & Automation | PMT-033 | Taxonomy, automation, system health, prompt engineering |
| **VID** | Video Production | PMT-043 | Transcription, entity extraction, video workflows |
| **HRM** | Human Resources | PMT-038 | CV parsing, recruitment automation |
| **DEV** | Development | PMT-036 | Version control, VSCode, API integration |
| **LGN** | Lead Generation | PMT-039 | Lead scraping, prospecting, outreach |
| **DGN** | Design | PMT-035 | UI/UX, graphics, creative assets |
| **MKT** | Marketing | PMT-040 | Campaigns, content strategy |
| **SLS** | Sales | PMT-041 | Pipeline management, research |
| **SMM** | Social Media | PMT-042 | Content, engagement, community |
| **FIN** | Finance | PMT-037 | Reporting, compliance, budgets |

---

## CROSS-DEPARTMENT PROJECTS

**Research Operations:**

Research is a **cross-department project**, not a standalone department. Multiple departments contribute:

| Research Type | Leading/Contributing Depts | Prompts |
|---------------|---------------------------|---------|
| **Video Processing** | VID (leads) | PMT-004 to PMT-013 |
| **Document Analysis** | SMM, HRM, SLS | PMT-045 |
| **Web Research** | SLS, LGN | PMT-044, PMT-051 |
| **Platform Research** | DEV, AID | PMT-046 to PMT-052 |

**Research Workflow:**
1. Input: Video, document, web page, platform data
2. Extract: TST-### (tasks), STT-### (steps) using task-first approach
3. Classify: Group into MLT-### and PRT-### using [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)
4. Enrich: Link to TOL-### (tools) and GDS-### (guides)
5. Output: Structured data reusable across departments

---

## COLLABORATION PATTERNS

**Shared Resources:**
- All depts use Tools (TOL-###) and Guides (GDS-###)
- Research outputs → AI validates → Marketing uses
- HR profiles → Sales uses → LG targets
- Dev tools → All depts reference
- Classification guides → All depts use ([GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010), [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011))

**Daily Workflow:**
1. Run dept report (PMT-033 to PMT-043)
2. Extract entities (TST-###, STT-###, MLT-###, PRT-###)
3. Link to TOL-### and GDS-###
4. Update master CSVs in `ENTITIES/TASK_MANAGERS/TSM-00X_[Category]/`
5. Archive to `ENTITIES/REPORTS/{Dept}/{Date}`
