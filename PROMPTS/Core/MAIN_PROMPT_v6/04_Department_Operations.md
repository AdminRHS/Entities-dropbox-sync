# 4. DEPARTMENT OPERATIONS

**Version:** 6.1 | **Date:** 2025-11-26 | **Status:** Production
**Part of:** MAIN_PROMPT_v6 Modular System

---

## DEPARTMENT CODES & FOCUS

| Code | Department | Daily | Primary Prompts | Focus Areas |
|------|-----------|-------|-----------------|-------------|
| **AID** | AI & Automation | PMT-033 | PMT-048, 066-069 | Taxonomy, automation, system health, prompt eng |
| **VID** | Video Production | PMT-043 | PMT-004-013, 071 | Transcription, entity extraction, video workflows |
| **HRM** | Human Resources | PMT-038 | PMT-053-057, 047/049 | CV parsing, recruitment automation |
| **DEV** | Development | PMT-036 | PMT-046, 052, 068-069 | Version control, VSCode, API integration |
| **LGN** | Lead Generation | PMT-039 | PMT-044 (Sales research) | Lead scraping, prospecting, outreach |
| **DGN** | Design | PMT-035 | - | UI/UX, graphics, creative assets |
| **MKT** | Marketing | PMT-040 | PMT-034 (Content) | Campaigns, content strategy |
| **SLS** | Sales | PMT-041 | PMT-044 | Pipeline management, research |
| **SMM** | Social Media | PMT-042 | PMT-045 | Content, engagement, community |
| **FIN** | Finance | PMT-037 | - | Reporting, compliance, budgets |

## CROSS-DEPARTMENT PROJECTS

**Research Operations (Cross-Department Project):**

Research is a **cross-department project**, not a standalone department. Multiple departments contribute to and utilize research:

**Research Types:**

- **Video Processing** - Transcription, entity extraction (VID dept leads, PMT-004 to PMT-013)
- **Document Analysis** - PDF parsing, document research (SMM, HRM, SLS depts contribute, PMT-045)
- **Web Research** - Sales research, market research (SLS, LGN depts contribute, PMT-044, PMT-051)
- **Platform Research** - VSCode extensions, AI tools, tutorials (DEV, AID depts contribute, PMT-046, 047, 048, 050, 052)

**Research Workflow (Cross-Department):**

1. **Input**: Various sources (video, documents, web, platforms)
2. **Extract**: TST-### (tasks), STT-### (steps) using task-first approach
3. **Classify**: Group into MLT-### and PRT-### using [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011)
4. **Enrich**: Link to TOL-### (tools) and GDS-### (guides)
5. **Output**: Structured data reusable across departments

**Key Notes:**

- Research projects involve multiple departments working together
- Each department contributes research from their domain expertise
- Research outputs populate data across all departments
- Templates created during research are reusable (many-to-many)

---

## COLLABORATION PATTERNS

**Cross-Department Entities:**

- All depts use shared Tools (TOL-###) and Guides (GDS-###)
- Research extracts → AI validates → Marketing uses
- HR profiles → Sales uses → LG targets
- Dev tools → All depts reference (TOL-###)
- Classification guides → All depts use ([GDS-010](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010), [GDS-011](ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-011))

**Daily Workflow:**

1. Run dept report (PMT-0XX)
2. Extract entity references (TST-###, STT-###, MLT-###, PRT-###)
3. Link to Tools (TOL-###) and Guides (GDS-###)
4. Update master CSVs in `ENTITIES/TASK_MANAGERS/TSM-00X_[Category]/`
5. Archive to ENTITIES/REPORTS/{Dept}/{Date}
