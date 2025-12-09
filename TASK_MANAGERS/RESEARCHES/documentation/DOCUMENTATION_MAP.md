# RESEARCHES 2 - DOCUMENTATION MAP

**Created:** 2025-12-08
**Purpose:** Visual map of all documentation and their relationships
**Start Here:** [v1/00_MASTER_INDEX_UPDATED.md](./v1/00_MASTER_INDEX_UPDATED.md)

---

## 🗺️ DOCUMENTATION STRUCTURE

```
RESEARCHES/documentation/
│
├── 📍 START HERE
│   ├── v1/00_MASTER_INDEX_UPDATED.md ← Master index (you are here guide)
│   ├── v1/12_QUICK_START.md          ← Quick start for new users
│   └── PHASE_0_START_GUIDE.md        ← Phase 0 execution roadmap
│
├── 📋 PLANNING & ARCHITECTURE (Phase 0)
│   ├── v1/14_DEVELOPMENT_PLAN_COMPLETE.md     ← 🔴 MAIN: 9-phase plan (RU)
│   ├── DEVELOPMENT_PLAN_SUMMARY.md            ← Executive summary (8KB)
│   ├── v1/15_FULL_APP_GENERATION_PROMPT.md    ← 🔴 MAIN: AI prompt (EN)
│   └── v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md   ← CSS variables reference
│
├── 🎨 DESIGN SYSTEM
│   ├── v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md   ← Complete CSS vars
│   ├── 🌐 https://adminrhs.github.io/Design-system/  ← Official design system
│   └── 🌐 https://adminrhs.github.io/Video-catalog/  ← UI reference
│
├── 📖 SYSTEM DOCUMENTATION
│   ├── v1/01_FOLDER_STRUCTURE.md              ← Folder hierarchy
│   ├── v1/02_ALL_FILES_INVENTORY.md           ← Complete file list
│   ├── v1/03_SEARCH_QUEUE_COMPLETE.md         ← Search Queue module
│   ├── v1/04_VIDEO_QUEUE_COMPLETE.md          ← Video Queue module
│   ├── v1/05_TRANSCRIPTIONS_COMPLETE.md       ← Transcription workflow
│   ├── v1/06_ANALYSIS_COMPLETE.md             ← Analysis process
│   ├── v1/07_INTEGRATION_COMPLETE.md          ← Integration workflows
│   ├── v1/08_SCRIPTS_DETAILED.md              ← Python scripts (21)
│   ├── v1/09_PROMPTS_CATALOG.md               ← AI prompts (50+)
│   ├── v1/10_DATA_FILES.md                    ← Data files
│   └── v1/11_REPORTS_ARCHIVE.md               ← Reports
│
├── 🔧 OPERATIONS
│   ├── v1/13_TROUBLESHOOTING.md               ← Common issues
│   └── v1/README.md                           ← Version 1 overview
│
├── 🧪 ADVANCED DOCUMENTATION
│   ├── v2/                                     ← Advanced topics
│   ├── technical/                              ← Technical specs
│   └── taxonomy/                               ← Entity definitions (752+)
│
├── 📝 PROMPTS & TEMPLATES
│   └── prompts/
│       └── FULL-APP-GENERATION-PROMPT.md      ← Original prompt source
│
└── 🐛 ISSUES & TRACKING
    └── issues/                                 ← Issue documentation
        ├── ISS-RES-001 ← Phase tracker desync
        ├── ISS-RES-005 ← Manual bottleneck (450 hrs/year)
        └── ISS-RES-010 ← No unit tests
```

---

## 🎯 DOCUMENT RELATIONSHIPS

### For New Users → Start Learning Path
```
1. v1/00_MASTER_INDEX_UPDATED.md
   ↓
2. v1/12_QUICK_START.md
   ↓
3. DEVELOPMENT_PLAN_SUMMARY.md (8KB - quick overview)
   ↓
4. v1/14_DEVELOPMENT_PLAN_COMPLETE.md (70KB - full plan)
```

### For Development → AI Generation Path
```
1. PHASE_0_START_GUIDE.md (understand Phase 0 requirements)
   ↓
2. v1/15_FULL_APP_GENERATION_PROMPT.md (AI generation prompt)
   ↓
3. v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md (CSS reference)
   ↓
4. v1/14_DEVELOPMENT_PLAN_COMPLETE.md (implementation details)
   ↓
5. Start Phase 0 sub-phases (0.2 → 0.8)
```

### For Design → UI/UX Path
```
1. v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md (CSS variables)
   ↓
2. 🌐 https://adminrhs.github.io/Design-system/ (official system)
   ↓
3. 🌐 https://adminrhs.github.io/Video-catalog/ (UI reference)
   ↓
4. v1/15_FULL_APP_GENERATION_PROMPT.md (component specs)
```

### For System Understanding → Technical Path
```
1. v1/01_FOLDER_STRUCTURE.md (structure)
   ↓
2. v1/03-07_*.md (module documentation)
   ↓
3. v1/08_SCRIPTS_DETAILED.md (automation scripts)
   ↓
4. v1/09_PROMPTS_CATALOG.md (AI prompts)
   ↓
5. taxonomy/ (entity definitions)
```

---

## 📊 DOCUMENTATION BY PURPOSE

### 🚀 Getting Started
| Document | Size | Purpose | Audience |
|----------|------|---------|----------|
| [00_MASTER_INDEX_UPDATED.md](./v1/00_MASTER_INDEX_UPDATED.md) | ~10KB | Master navigation | Everyone |
| [12_QUICK_START.md](./v1/12_QUICK_START.md) | ~5KB | Quick start guide | New users |
| [DEVELOPMENT_PLAN_SUMMARY.md](./DEVELOPMENT_PLAN_SUMMARY.md) | 8.3KB | Executive summary | Stakeholders |

### 📋 Planning Documents
| Document | Size | Purpose | Audience |
|----------|------|---------|----------|
| [14_DEVELOPMENT_PLAN_COMPLETE.md](./v1/14_DEVELOPMENT_PLAN_COMPLETE.md) | 70KB | Complete plan (RU) | Developers |
| [PHASE_0_START_GUIDE.md](./PHASE_0_START_GUIDE.md) | ~15KB | Phase 0 guide | Developers |
| [15_FULL_APP_GENERATION_PROMPT.md](./v1/15_FULL_APP_GENERATION_PROMPT.md) | ~65KB | AI prompt (EN) | AI tools |

### 🎨 Design Resources
| Document | Size | Purpose | Audience |
|----------|------|---------|----------|
| [16_DESIGN_SYSTEM_CSS_VARIABLES.md](./v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md) | ~25KB | CSS variables | Designers, Devs |
| Design System (external) | Web | Official system | Designers |
| Video Catalog (external) | Web | UI reference | Designers |

### 📖 System Documentation
| Document | Purpose | Key Content |
|----------|---------|-------------|
| [01_FOLDER_STRUCTURE.md](./v1/01_FOLDER_STRUCTURE.md) | Structure | Complete folder tree |
| [02_ALL_FILES_INVENTORY.md](./v1/02_ALL_FILES_INVENTORY.md) | Inventory | All files (300+ pages) |
| [03_SEARCH_QUEUE_COMPLETE.md](./v1/03_SEARCH_QUEUE_COMPLETE.md) | Module docs | Search Queue |
| [04_VIDEO_QUEUE_COMPLETE.md](./v1/04_VIDEO_QUEUE_COMPLETE.md) | Module docs | Video Queue |
| [05_TRANSCRIPTIONS_COMPLETE.md](./v1/05_TRANSCRIPTIONS_COMPLETE.md) | Workflow | Transcription |
| [06_ANALYSIS_COMPLETE.md](./v1/06_ANALYSIS_COMPLETE.md) | Process | Analysis |
| [07_INTEGRATION_COMPLETE.md](./v1/07_INTEGRATION_COMPLETE.md) | Integration | Dropbox sync |
| [08_SCRIPTS_DETAILED.md](./v1/08_SCRIPTS_DETAILED.md) | Automation | 21 Python scripts |
| [09_PROMPTS_CATALOG.md](./v1/09_PROMPTS_CATALOG.md) | AI prompts | 50+ prompts |

---

## 🔄 WORKFLOW DOCUMENTATION MAP

### Phase 0: Planning (Current Phase)
```
📄 PHASE_0_START_GUIDE.md
├── Sub-phase 0.1: Infrastructure Analysis ✅
├── Sub-phase 0.2: Architecture (C4 Model) ⏳
├── Sub-phase 0.3: Database Schema (Prisma) ⏳
├── Sub-phase 0.4: API Spec (OpenAPI) ⏳
├── Sub-phase 0.5: UI/UX Design (Figma) ⏳
├── Sub-phase 0.6: Pseudo-Code ⏳
├── Sub-phase 0.7: AI Prompts ⏳
└── Sub-phase 0.8: Tech Stack Setup ⏳

References:
→ v1/14_DEVELOPMENT_PLAN_COMPLETE.md (detailed plan)
→ v1/15_FULL_APP_GENERATION_PROMPT.md (AI prompt)
→ v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md (design system)
```

### Phase 1: Foundation
```
📄 v1/14_DEVELOPMENT_PLAN_COMPLETE.md (Section: Фаза 1)
├── Project setup
├── Design system
├── Database (Prisma + Neon)
└── Authentication

References:
→ v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md (CSS vars)
→ Phase_0_Start_Guide.md → 0.3 (Prisma schema)
```

### Phase 2: Search Queue
```
📄 v1/03_SEARCH_QUEUE_COMPLETE.md (current docs)
📄 v1/14_DEVELOPMENT_PLAN_COMPLETE.md (Section: Фаза 2)

References:
→ v1/15_FULL_APP_GENERATION_PROMPT.md (UI components)
→ v1/09_PROMPTS_CATALOG.md (search prompts)
```

### Phase 3: Video Queue
```
📄 v1/04_VIDEO_QUEUE_COMPLETE.md (current docs)
📄 v1/14_DEVELOPMENT_PLAN_COMPLETE.md (Section: Фаза 3)

References:
→ v1/15_FULL_APP_GENERATION_PROMPT.md (priority system)
→ Phase_2_Video_Queue/Video_Queue_Master.json (data)
```

### Phases 4-9
```
📄 v1/14_DEVELOPMENT_PLAN_COMPLETE.md (Sections: Фазы 4-9)

Phase 4: Transcription → v1/05_TRANSCRIPTIONS_COMPLETE.md
Phase 5: Analysis → v1/06_ANALYSIS_COMPLETE.md
Phase 6: Integration → v1/07_INTEGRATION_COMPLETE.md
Phase 7: Mapping → (to be documented)
Phase 8: Dashboard → (to be documented)
Phase 9: Testing → (to be documented)
```

---

## 🎯 USE CASE SCENARIOS

### Scenario 1: "I want to understand the project"
```
Start → v1/00_MASTER_INDEX_UPDATED.md
     → DEVELOPMENT_PLAN_SUMMARY.md (quick overview)
     → v1/12_QUICK_START.md
     → v1/03-07_*.md (deep dive into modules)
```

### Scenario 2: "I want to start development"
```
Start → PHASE_0_START_GUIDE.md
     → v1/14_DEVELOPMENT_PLAN_COMPLETE.md
     → Complete Phase 0 (8 sub-phases)
     → v1/15_FULL_APP_GENERATION_PROMPT.md (for AI generation)
     → Begin Phase 1
```

### Scenario 3: "I need design specifications"
```
Start → v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md
     → https://adminrhs.github.io/Design-system/
     → https://adminrhs.github.io/Video-catalog/
     → v1/15_FULL_APP_GENERATION_PROMPT.md (component specs)
```

### Scenario 4: "I want to use AI for code generation"
```
Start → v1/15_FULL_APP_GENERATION_PROMPT.md (main prompt)
     → v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md (CSS reference)
     → v1/14_DEVELOPMENT_PLAN_COMPLETE.md (detailed specs)
     → PHASE_0_START_GUIDE.md → 0.6 (pseudo-code)
     → Generate code with Claude Code / Cursor / v0.dev
```

### Scenario 5: "I have an issue"
```
Start → v1/13_TROUBLESHOOTING.md
     → Check issues/ folder
     → Review relevant module documentation (v1/03-07_*.md)
```

---

## 📈 DOCUMENTATION STATUS

### ✅ Complete (100%)
- Master index
- Quick start guide
- Complete development plan (Russian)
- AI generation prompt (English)
- Design system CSS variables
- All module documentation (Phase 1-7)
- Scripts documentation (21 scripts)
- Prompts catalog (50+ prompts)

### ⏳ In Progress
- Phase 0 execution (12.5% - 1/8 sub-phases done)
- Architecture diagrams (Phase 0.2)
- Database schema (Phase 0.3)
- API specification (Phase 0.4)

### 📝 Planned
- Figma UI/UX prototypes (Phase 0.5)
- Pseudo-code documentation (Phase 0.6)
- AI generation prompts library (Phase 0.7)
- Tech stack setup guide (Phase 0.8)

---

## 🔗 EXTERNAL LINKS

### Design Resources
- **Design System:** https://adminrhs.github.io/Design-system/
- **Video Catalog:** https://adminrhs.github.io/Video-catalog/

### Tech Stack Documentation
- **React 19:** https://react.dev/
- **ShadCN UI:** https://ui.shadcn.com/
- **Tailwind CSS v4:** https://tailwindcss.com/
- **TanStack Query:** https://tanstack.com/query/latest
- **TanStack Table:** https://tanstack.com/table/latest
- **Prisma ORM:** https://www.prisma.io/docs
- **Neon PostgreSQL:** https://neon.tech/docs

### APIs
- **YouTube Data API v3:** https://developers.google.com/youtube/v3
- **Dropbox API:** https://www.dropbox.com/developers/documentation
- **OpenAI API:** https://platform.openai.com/docs

### Deployment
- **Vercel:** https://vercel.com/docs
- **Railway:** https://docs.railway.app/

---

## 📞 QUICK REFERENCE

### Key Documents (Top 5)
1. **[00_MASTER_INDEX_UPDATED.md](./v1/00_MASTER_INDEX_UPDATED.md)** - Start here
2. **[14_DEVELOPMENT_PLAN_COMPLETE.md](./v1/14_DEVELOPMENT_PLAN_COMPLETE.md)** - Full plan (70KB)
3. **[15_FULL_APP_GENERATION_PROMPT.md](./v1/15_FULL_APP_GENERATION_PROMPT.md)** - AI prompt (65KB)
4. **[PHASE_0_START_GUIDE.md](./PHASE_0_START_GUIDE.md)** - Phase 0 guide
5. **[16_DESIGN_SYSTEM_CSS_VARIABLES.md](./v1/16_DESIGN_SYSTEM_CSS_VARIABLES.md)** - CSS vars

### Quick Stats
- **Total Documentation:** 300+ pages
- **Main Planning Docs:** 3 files (~150KB)
- **Module Documentation:** 11 files
- **Python Scripts:** 21 documented
- **AI Prompts:** 50+ cataloged
- **Entities in Taxonomy:** 752+

---

## 🎯 NEXT STEPS

1. Review [PHASE_0_START_GUIDE.md](./PHASE_0_START_GUIDE.md)
2. Complete Phase 0.2: Architecture Document (C4 Model)
3. Complete Phase 0.3: Database Schema (Prisma + ERD)
4. Complete Phase 0.4: API Specification (OpenAPI/Swagger)
5. Continue with remaining Phase 0 sub-phases

---

**Document Version:** 1.0 | **Last Updated:** 2025-12-08 | **Status:** Complete ✅

**Note:** This is a living document. Update as new documentation is created or structure changes.
