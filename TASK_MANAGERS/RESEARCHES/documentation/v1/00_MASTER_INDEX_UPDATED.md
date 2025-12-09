# RESEARCHES 2 - MASTER DOCUMENTATION INDEX

**Last Updated:** 2025-12-08
**Version:** 2.0
**Project Status:** Phase 0 (Planning & Architecture) - 12.5% Complete

---

## 📚 QUICK NAVIGATION

### 🚀 START HERE
1. [12_QUICK_START.md](./12_QUICK_START.md) - Quick start guide for new users
2. [14_DEVELOPMENT_PLAN_COMPLETE.md](./14_DEVELOPMENT_PLAN_COMPLETE.md) - **Full 9-phase development plan** (Russian)
3. [15_FULL_APP_GENERATION_PROMPT.md](./15_FULL_APP_GENERATION_PROMPT.md) - **AI generation prompt** (English)

### 🎨 DESIGN & UI
4. [16_DESIGN_SYSTEM_CSS_VARIABLES.md](./16_DESIGN_SYSTEM_CSS_VARIABLES.md) - Complete CSS variables reference
5. Design System Reference: https://adminrhs.github.io/Design-system/
6. Video Catalog Reference: https://adminrhs.github.io/Video-catalog/

### 📖 SYSTEM DOCUMENTATION
7. [01_FOLDER_STRUCTURE.md](./01_FOLDER_STRUCTURE.md) - Complete folder structure
8. [02_ALL_FILES_INVENTORY.md](./02_ALL_FILES_INVENTORY.md) - Full file inventory
9. [03_SEARCH_QUEUE_COMPLETE.md](./03_SEARCH_QUEUE_COMPLETE.md) - Search Queue module documentation
10. [04_VIDEO_QUEUE_COMPLETE.md](./04_VIDEO_QUEUE_COMPLETE.md) - Video Queue module documentation
11. [05_TRANSCRIPTIONS_COMPLETE.md](./05_TRANSCRIPTIONS_COMPLETE.md) - Transcription workflow
12. [06_ANALYSIS_COMPLETE.md](./06_ANALYSIS_COMPLETE.md) - Analysis process
13. [07_INTEGRATION_COMPLETE.md](./07_INTEGRATION_COMPLETE.md) - Integration workflows
14. [08_SCRIPTS_DETAILED.md](./08_SCRIPTS_DETAILED.md) - Python scripts documentation (21 scripts)
15. [09_PROMPTS_CATALOG.md](./09_PROMPTS_CATALOG.md) - AI prompts library (50+ prompts)
16. [10_DATA_FILES.md](./10_DATA_FILES.md) - Data files documentation
17. [11_REPORTS_ARCHIVE.md](./11_REPORTS_ARCHIVE.md) - Reports documentation

### 🔧 TROUBLESHOOTING
18. [13_TROUBLESHOOTING.md](./13_TROUBLESHOOTING.md) - Common issues and solutions

---

## 📊 PROJECT OVERVIEW

### Core Concept
**RESEARCHES 2** is a comprehensive video content processing system with 7-phase workflow for extracting, analyzing, and integrating educational entities into a taxonomic knowledge base.

### 7-Phase Workflow
1. **🔍 Search Queue** → Create search tasks, find videos
2. **📹 Video Queue** → Manage video queue with priority system
3. **📝 Transcription** → Generate transcripts (YouTube + Whisper)
4. **🔬 Analysis** → Extract entities (AI-powered)
5. **🔎 Gap Analysis** → Identify missing information
6. **🔗 Integration** → Integrate into Dropbox taxonomy
7. **🗺️ Mapping** → Create cross-reference relationships

### Tech Stack

#### Frontend
- **Framework:** React 19+ + TypeScript
- **UI Library:** ShadCN UI + Tailwind CSS v4
- **State:** Zustand
- **Data Fetching:** TanStack Query
- **Tables:** TanStack Table
- **Icons:** Lucide React
- **Charts:** Recharts
- **Animations:** Framer Motion

#### Backend
- **Runtime:** Node.js 20+
- **Framework:** Express.js
- **ORM:** Prisma
- **Database:** PostgreSQL (Neon)
- **Queue:** BullMQ + Redis
- **APIs:** Dropbox API, YouTube Data API v3, OpenAI API

#### Deployment
- **Frontend:** Vercel → Corporate Server
- **Backend:** Railway → Corporate Server
- **Database:** Neon (PostgreSQL)
- **File Storage:** Dropbox

---

## 🗂️ TAXONOMY SYSTEM

### Entity Types (752+ entities)
- **WRF** - Workflows (93 entities)
- **TOL** - Tools (145 entities)
- **OBJ** - Objects (178 entities)
- **ACT** - Actions (98 entities)
- **PRF** - Profiles/Roles (67 entities)
- **SKL** - Skills (124 entities)
- **DPT** - Departments (47 entities)

### ID Standards
- **Videos:** `Video_XXX` (e.g., Video_001)
- **Video Queue:** `VQ-XXX` (e.g., VQ-001)
- **Search Tasks:** `SEARCH-XXX` (e.g., SEARCH-001)
- **Issues:** `ISS-RES-XXX` (e.g., ISS-RES-001)
- **Tasks:** `TASK-XXX` (e.g., TASK-001)
- **Changes:** `CHG-RES-YYYYMMDD-XXX` (e.g., CHG-RES-20251208-001)

---

## 📈 DEVELOPMENT PHASES

### Phase 0: Complete Planning & Architecture (2-3 weeks) ⏳
**Status:** 12.5% Complete (1/8 sub-phases done)

#### Sub-phases:
1. ✅ **0.1: Infrastructure Analysis** - Complete
2. ⏳ **0.2: Architecture Document** (C4 Model) - Pending
3. ⏳ **0.3: Database Schema** (Prisma + ERD) - Pending
4. ⏳ **0.4: API Specification** (OpenAPI/Swagger) - Pending
5. ⏳ **0.5: UI/UX Design** (Figma prototypes) - Pending
6. ⏳ **0.6: Pseudo-Code** for all modules - Pending
7. ⏳ **0.7: AI-generation prompts** - Pending
8. ⏳ **0.8: Tech Stack Setup** (GitHub, Vercel, Neon, Railway) - Pending

**⚠️ CRITICAL:** Development (Phase 1-9) starts ONLY after Phase 0 is 100% complete.

### Phase 1: Foundation & Infrastructure (MVP Week 1-2)
- Project initialization
- Design system implementation
- Database setup (Prisma + Neon)
- Authentication system

### Phase 2: Search Queue Module (Week 3)
- Search task management
- YouTube API integration
- Search results modal
- AI search integration

### Phase 3: Video Queue Module (Week 4-5)
- Video queue dashboard
- Priority calculation system
- Metadata management
- Phase transitions

### Phase 4: Transcription Module (Week 6)
- YouTube transcript API
- Whisper API integration
- Transcript storage
- Quality validation

### Phase 5: Analysis Module (Week 7-8)
- Entity extraction (AI)
- Pattern recognition
- Data validation
- Review interface

### Phase 6: Integration Module (Week 9)
- Dropbox API integration
- File synchronization
- Taxonomy mapping
- Conflict resolution

### Phase 7: Mapping & Cross-References (Week 10)
- Relationship mapping
- Cross-reference system
- Graph visualization
- Network analysis

### Phase 8: Dashboard & Analytics (Week 11)
- Main dashboard
- Statistics & charts
- Performance metrics
- Activity feed

### Phase 9: Testing & Deployment (Week 12)
- Unit tests (80%+ coverage)
- E2E tests
- Performance optimization
- Production deployment

---

## 🎯 KEY METRICS

### Current System Statistics
- **Total Videos Processed:** 100+ videos
- **Entities in Taxonomy:** 752+ entities across 7 types
- **Python Scripts:** 21 automation scripts
- **AI Prompts:** 50+ specialized prompts
- **Documentation Pages:** 300+ pages

### Target Metrics (v1.0)
- **Processing Time:** < 30 min per video (vs 5+ hours manual)
- **Accuracy:** 95%+ entity extraction
- **Automation:** 90%+ workflow automation
- **ROI:** 550+ hours/year saved at 100 videos/year

---

## 🚨 CRITICAL ISSUES

### High Priority
1. **ISS-RES-005** - Phase 2 Manual Bottleneck (450 hrs/year waste)
2. **ISS-RES-001** - Phase Tracker Desync (30% error rate)
3. **ISS-RES-010** - No Unit Tests (high risk)

### Medium Priority
4. **ISS-RES-002** - VQ JSON Parsing Issues
5. **ISS-RES-003** - Daily Report Aggregation
6. **ISS-RES-006** - No Analytics Dashboard

---

## 📂 FOLDER STRUCTURE

```
RESEARCHES/
├── documentation/
│   ├── v1/                      # Main documentation (THIS FOLDER)
│   │   ├── 00_MASTER_INDEX_UPDATED.md  # ← YOU ARE HERE
│   │   ├── 01-13_*.md           # System documentation
│   │   ├── 14_DEVELOPMENT_PLAN_COMPLETE.md
│   │   ├── 15_FULL_APP_GENERATION_PROMPT.md
│   │   └── 16_DESIGN_SYSTEM_CSS_VARIABLES.md
│   ├── v2/                      # Advanced documentation
│   ├── taxonomy/                # Entity definitions
│   ├── technical/               # Technical specs
│   ├── issues/                  # Issue tracking
│   ├── prompts/                 # AI prompts library
│   └── PHASE_0_START_GUIDE.md   # Phase 0 execution guide
│
├── Phase_2_Video_Queue/         # Video queue data
│   ├── Video_Queue_Master.json  # Master queue file
│   └── daily/                   # Daily snapshots
│
├── Phase_1_Search_Queue/        # Search tasks
│   └── searches/                # Search results
│
├── Phase_3_Transcriptions/      # Transcripts
│   └── Video_XXX/               # Per-video folders
│
├── Phase_4_Analysis/            # Analysis results
│   └── Video_XXX/               # Per-video analysis
│
├── Phase_5_Integration/         # Integration data
│
├── Phase_6_Dropbox_Integration/ # Dropbox sync
│
├── scripts/                     # Python automation (21 scripts)
│   ├── search_queue/            # Search automation
│   ├── video_queue/             # Queue management
│   ├── transcription/           # Transcription scripts
│   └── analysis/                # Analysis tools
│
└── tests/                       # Test suites (future)
```

---

## 🔗 EXTERNAL RESOURCES

### Design References
- **Design System:** https://adminrhs.github.io/Design-system/
- **Video Catalog UI:** https://adminrhs.github.io/Video-catalog/

### APIs & Services
- **YouTube Data API v3:** https://developers.google.com/youtube/v3
- **Dropbox API:** https://www.dropbox.com/developers/documentation
- **OpenAI API:** https://platform.openai.com/docs
- **Prisma ORM:** https://www.prisma.io/docs
- **Neon Database:** https://neon.tech/docs

### Development Tools
- **ShadCN UI:** https://ui.shadcn.com/
- **TanStack Query:** https://tanstack.com/query/latest
- **TanStack Table:** https://tanstack.com/table/latest
- **Vercel:** https://vercel.com/docs
- **Railway:** https://docs.railway.app/

---

## 📝 VERSION HISTORY

### v2.0 - 2025-12-08 (Current)
- ✅ Added complete development plan (9 phases, Russian)
- ✅ Added full AI generation prompt (English)
- ✅ Added design system CSS variables reference
- ✅ Updated tech stack (React 19, ShadCN UI, Prisma, Neon)
- ✅ Added Phase 0 detailed guide
- ✅ Added deployment strategy

### v1.0 - 2025-11-XX (Previous)
- Initial documentation system
- 13 core documentation files
- Python scripts documentation
- Prompts catalog
- Basic workflow descriptions

---

## 🎯 NEXT STEPS

### Immediate (This Week)
1. ✅ Complete infrastructure analysis (Phase 0.1) - DONE
2. ⏳ Create C4 architecture diagrams (Phase 0.2)
3. ⏳ Design complete Prisma schema (Phase 0.3)
4. ⏳ Write OpenAPI specification (Phase 0.4)

### Short-term (Next 2 Weeks)
5. ⏳ Create Figma UI/UX prototypes (Phase 0.5)
6. ⏳ Write pseudo-code for all modules (Phase 0.6)
7. ⏳ Prepare AI generation prompts (Phase 0.7)
8. ⏳ Setup GitHub, Vercel, Neon, Railway (Phase 0.8)

### Long-term (After Phase 0 Complete)
9. Start Phase 1: Foundation & Infrastructure
10. Begin AI-assisted code generation
11. Implement Search Queue module
12. Build Video Queue with priority system

---

## 👥 TEAM & APPROACH

### Development Team
- **Solo Developer:** User
- **AI Assistants:** Claude Code, Cursor, v0.dev
- **Approach:** AI-assisted development with human oversight

### Development Methodology
1. **Documentation-First:** Complete all planning before coding
2. **AI-Assisted:** Use AI for code generation and boilerplate
3. **Human Review:** Review all AI-generated code
4. **Iterative:** Build incrementally, test frequently
5. **Quality-Focused:** 80%+ test coverage, strict TypeScript

---

## 📞 SUPPORT & FEEDBACK

### For Questions
- Review [12_QUICK_START.md](./12_QUICK_START.md) first
- Check [13_TROUBLESHOOTING.md](./13_TROUBLESHOOTING.md) for common issues
- Review development plan for implementation details

### For Issues
- Document in `documentation/issues/` folder
- Use format: `ISS-RES-XXX`
- Include reproduction steps and expected behavior

---

## 📄 LICENSE & ATTRIBUTION

**Project:** RESEARCHES 2 - Video Content Processing System
**Created:** 2025
**Design System:** Based on https://adminrhs.github.io/Design-system/
**UI Reference:** Based on https://adminrhs.github.io/Video-catalog/

---

**Last Updated:** 2025-12-08 | **Document Version:** 2.0 | **Project Status:** Phase 0 (12.5%) ⏳
