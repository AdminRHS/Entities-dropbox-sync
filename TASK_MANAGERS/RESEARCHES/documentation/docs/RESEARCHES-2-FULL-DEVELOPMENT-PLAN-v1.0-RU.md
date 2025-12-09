# ПОЛНЫЙ ПЛАН РАЗРАБОТКИ ПРИЛОЖЕНИЯ RESEARCHES 2 v1.0

**Создан:** 2025-12-08
**Версия:** 1.0 (Русская версия)
**Статус:** Утверждено для разработки
**Разработчик:** 1 разработчик + AI assistance

---

## 📋 ОГЛАВЛЕНИЕ

1. [Обзор проекта](#обзор-проекта)
2. [Подтвержденные требования](#подтвержденные-требования)
3. [Технологический стек](#технологический-стек)
4. [Архитектура системы](#архитектура-системы)
5. [План разработки (9 фаз)](#план-разработки)
6. [Timeline и метрики](#timeline-и-метрики)
7. [Критические файлы](#критические-файлы)
8. [Риски и митигация](#риски-и-митигация)

---

## 📊 ОБЗОР ПРОЕКТА

### Что такое RESEARCHES 2?

**RESEARCHES 2** - это production-ready система автоматизированной обработки видео-контента с YouTube и интеграции знаний в таксономическую структуру ENTITIES.

### Текущее состояние
- ✅ 28 видео обработано
- ✅ 500+ entities извлечено
- ✅ 70% автоматизации (потенциал 90%)
- ✅ 14 Python скриптов
- ✅ 50+ промптов
- ✅ 22 видео полностью интегрировано
- ⚠️ 12 критических issues идентифицировано

### Ключевой функционал
- **7-фазный workflow**: Search → Queue → Transcription → Extraction → Gap Analysis → Integration → Mapping → Complete
- **Zero-loss Video Queue**: Накопление до 20 видео с приоритизацией (0-100 баллов)
- **Автоматический gap-анализ**: Сравнение с LIBRARIES, метрики покрытия
- **Bidirectional cross-referencing**: Tool↔Object↔Workflow↔Profession↔Skill
- **Comprehensive taxonomy**: 7 типов entities с автоматической категоризацией

### Цель проекта

Создать **веб-приложение на React** с полноценным backend для управления всем процессом обработки видео, которое:
- Автоматизирует 90%+ операций
- Масштабируется до 100+ видео и неограниченного количества пользователей
- Интегрируется с Dropbox (ENTITIES filesystem) и PostgreSQL
- Предоставляет responsive UI с dark/light mode
- Следует дизайн-системе https://adminrhs.github.io/Design-system/

---

## 🎯 ПОДТВЕРЖДЕННЫЕ ТРЕБОВАНИЯ ПРОЕКТА

### Технические параметры (подтверждено клиентом 2025-12-08)

**Платформа:**
- ✅ React Web Application (responsive)
- ✅ Адаптация под все экраны (desktop, tablet, mobile)
- ❌ Десктопная версия (не планируется)
- ❌ Native мобильное приложение (не планируется)
- ❌ Progressive Web App (пока не планируется)

**Автоматизация:**
- ✅ Максимальная автоматизация (90%+)
- ✅ Phase 2 automation (ISS-RES-005) - КРИТИЧНО
- ✅ YouTube API integration (полная)

**Пользователи:**
- ✅ Неограниченное количество пользователей
- ✅ Система авторизации (JWT)
- ✅ Разделение ролей (Admin, Researcher, Manager, Viewer)
- ❓ Collaborative features (под вопросом, **не включаем в v1.0**)

**Инфраструктура:**
- ✅ Все с нуля (нет существующего backend)
- ✅ **PostgreSQL** - основная БД (metadata, users, progress)
- ✅ **Dropbox API** - интеграция для доступа к ENTITIES
- ✅ Источник истины: Dropbox (файлы), PostgreSQL (metadata + кеш)
- ✅ Локальный сервер сначала → AWS/внешний сервер позже
- ❌ Cloud deployment в v1.0 (только локально)

**Команда:**
- ✅ **1 разработчик** (вы) + AI assistance
- ✅ Полное планирование + промпты перед разработкой
- ✅ Фокус на **Version 1.0** (базовый функционал)

**Интеграция с ENTITIES:**
- ✅ Dropbox API для доступа к файловой структуре
- ✅ ENTITIES структура:
  - `/ENTITIES/LIBRARIES/` - Tools, Workflows, Objects, Actions, Skills, Professions
  - `/ENTITIES/TASK_MANAGERS/` - Project Templates, Milestone Templates, Task Templates, Workflows
  - `/ENTITIES/TAXONOMY/` - Master Lists, ID Systems
  - `/ENTITIES/PROMPTS/` - PMT-XXX prompts
- ✅ JSON entities с Dropbox синхронизация
- ✅ Создание нового backend для orchestration

---

## 🛠 ТЕХНОЛОГИЧЕСКИЙ СТЕК

### Frontend
- **Framework:** React 18 + TypeScript
- **Styling:** Tailwind CSS 3 (с Design System tokens)
- **UI Components:** shadcn/ui (pre-configured)
- **State Management:** Zustand
- **Data Fetching:** React Query (TanStack Query)
- **Routing:** React Router v6
- **Icons:** Lucide React
- **Charts:** Recharts
- **Animations:** Framer Motion

### Backend
- **Runtime:** Node.js 18+
- **Framework:** Express.js 4
- **Database:** PostgreSQL 14+
- **Caching:** Redis 7+
- **ORM:** Prisma или TypeORM

### External APIs
- **Dropbox API** - доступ к ENTITIES filesystem
- **YouTube Data API v3** - метаданные видео
- **YouTube Transcript API** - транскрипты
- **Claude API** - AI обработка (приоритет)
- **OpenAI API** - AI fallback
- **Gemini API** - AI fallback (опционально)

### DevOps
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Testing:** Jest (frontend), Pytest (Python scripts)
- **Version Control:** Git + GitHub

---

## 🏗 АРХИТЕКТУРА СИСТЕМЫ

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React)                        │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ Dashboard │  │ Search    │  │ Video     │              │
│  │           │  │ Queue     │  │ Queue     │              │
│  └───────────┘  └───────────┘  └───────────┘              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ Video     │  │ Entities  │  │ Reports   │              │
│  │ Processing│  │ Browser   │  │           │              │
│  └───────────┘  └───────────┘  └───────────┘              │
└─────────────────────────────────────────────────────────────┘
                           │
                           ↓ REST API
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND (Node.js/Express)                 │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ Auth      │  │ Search    │  │ Video     │              │
│  │ Service   │  │ Service   │  │ Service   │              │
│  └───────────┘  └───────────┘  └───────────┘              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ Dropbox   │  │ YouTube   │  │ AI        │              │
│  │ Service   │  │ Service   │  │ Service   │              │
│  └───────────┘  └───────────┘  └───────────┘              │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         ↓                    ↓                    ↓
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ PostgreSQL   │    │ Redis        │    │ Dropbox      │
│ (metadata)   │    │ (cache)      │    │ (ENTITIES)   │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Data Flow

**Video Processing Flow:**
```
User → Search Queue → Execute Search → YouTube API
                                           ↓
                                    Videos Found
                                           ↓
                                    Video Queue
                                           ↓
                                    Select Video
                                           ↓
                                    Phase 1: Transcription
                                           ↓
                                    Phase 2: Extraction
                                           ↓
                                    Phase 3: Gap Analysis
                                           ↓
                                    Phase 4: Integration
                                           ↓
                                    Phase 5: Mapping
                                           ↓
                                    Complete → Dropbox ENTITIES
```

### Database Schema (PostgreSQL)

**Core Tables:**
1. `users` - Authentication, roles
2. `search_queue` - Search tasks (SEARCH-XXX)
3. `video_queue` - Video queue (VQ-XXX)
4. `video_progress` - Processing progress (Video_XXX)
5. `researches` - Research entities (RSR-XXX)
6. `entities_cache` - Cached ENTITIES from Dropbox

---

## 📅 ПЛАН РАЗРАБОТКИ (9 ФАЗ)

### Адаптированный план для 1 разработчика

**Ключевые изменения:**
1. **Reduced scope до Version 1.0** (Phases 0-6 только)
2. **Simplified architecture** (монолитный backend вместо microservices)
3. **Emphasis on prompts & AI assistance** (детальные промпты для каждого этапа)
4. **Sequential development** (один компонент за раз)
5. **Dropbox-first approach** (Dropbox как source of truth)
6. **No collaboration features** в v1.0
7. **Extended timeline** (21 weeks + 4-5 weeks buffer = 25-26 weeks)

---

## 🚀 ФАЗА 0: ПРОМПТЫ И ДЕТАЛЬНОЕ ПЛАНИРОВАНИЕ

**Длительность:** 1 неделя (7 дней)
**Цель:** Создать полный набор промптов, технических спецификаций и архитектурных диаграмм

### Подфазы

#### 0.1: Архитектурная документация (Days 1-2)
- System Architecture Diagram
- Component Architecture
- Database schema (ER diagram)
- API endpoints map
- Data Flow Diagrams

#### 0.2: Database Schema Prompts (Days 2-3)
- SQL schemas для всех таблиц
- Migration scripts
- Seed data

#### 0.3: API Endpoints Prompts (Day 3)
- Промпты для каждого endpoint
- OpenAPI/Swagger specification
- Request/Response examples

#### 0.4: Frontend Components Prompts (Days 4-5)
- Layout components
- Page components
- Shared components
- Component specifications

#### 0.5: Processing Workflow Prompts (Days 5-7)
- Phase 1-5 промпты
- AI orchestration
- Error handling

#### 0.6: Dropbox Integration Prompts (Day 7)
- Authentication
- File operations
- Sync strategy

#### 0.7: Testing Strategy Prompts (Day 7)
- Unit testing
- Integration testing
- E2E testing

**Outcome:** 50+ детальных промптов готовых к использованию

---

## 🏗 ФАЗА 1: ФУНДАМЕНТ И ИНФРАСТРУКТУРА

**Длительность:** 5 недель
**Цель:** Базовая архитектура, infrastructure, core functionality

### Подфазы

#### 1.1: Project Setup (Week 1, Days 1-5)
- Monorepo структура
- Docker containerization
- PostgreSQL setup
- MongoDB setup (optional)
- Redis setup
- CI/CD pipeline

#### 1.2: Database Schema & Models (Week 1, Days 3-7)
- PostgreSQL tables
- ORM setup (Prisma/TypeORM)
- Migration scripts
- Seed data

#### 1.3: Authentication & Authorization (Week 2, Days 1-3)
- JWT implementation
- Roles: Admin, Researcher, Manager, Viewer
- Password hashing
- Session management

#### 1.4: Core API Development (Week 2-3, Days 1-10)
- Search Queue APIs
- Video Queue APIs
- Video Processing APIs
- Entities APIs

#### 1.5: Dropbox Integration (Week 3-4, Days 1-10)
- OAuth 2.0
- File read/write operations
- Sync strategy
- Error handling

#### 1.6: Frontend Core Setup (Week 4, Days 1-5)
- React app scaffold
- Routing structure
- Shared components
- Authentication flow
- Dark mode setup

---

## 🔍 ФАЗА 2: SEARCH & QUEUE MANAGEMENT

**Длительность:** 3 недели
**Цель:** Phase 0 (Search Queue) и Phase 0→1 (Video Queue)

### Подфазы

#### 2.1: Search Queue UI (Week 5, Days 1-3)
- Search Queue Dashboard
- Create Search Task Modal
- Search Results Modal
- Filters and sorting

#### 2.2: Video Queue UI (Week 5, Days 4-7)
- Video Queue Dashboard
- Add Video Modal
- Batch Add Modal
- Priority visualization

#### 2.3: YouTube Metadata Integration (Week 6, Days 1-3)
- YouTube API integration
- Metadata extraction
- Transcript extraction
- Error handling

#### 2.4: Priority Calculation System (Week 6, Days 3-5)
- Formula implementation
- Configurable weights
- Manual override
- Batch recalculation

#### 2.5: Queue Analytics (Week 6, Days 4-7)
- Metrics dashboard
- Charts
- Export reports

---

## 📹 ФАЗА 3: VIDEO PROCESSING WORKFLOW

**Длительность:** 4 недели
**Цель:** Phase 1-5 processing с автоматизацией

### Подфазы

#### 3.1: Video Detail & Processing UI (Week 7, Days 1-5)
- Video Detail Page
- Phase progress tracker
- Processing Workspace
- Tab-based interface

#### 3.2: Phase 1 - Transcription (Week 7, Days 3-7)
- Transcript loading
- PMT-004 integration
- AI API selector
- Entity extraction preview
- Validation (≥37 entities)

#### 3.3: Phase 2 - Extraction Automation (Week 8, Days 1-5) ⚠️ КРИТИЧНО
**✅ Resolve ISS-RES-005**
- Automated extraction service
- PMT-007 integration
- Entity expansion (37 → 60-70)
- **Time savings: 30-45 min → 2-3 min**

#### 3.4: Phase 3 - Gap Analysis (Week 8, Days 3-7)
- Automated analysis
- NEW/EXISTING/UPDATE classification
- Coverage metrics
- Entity classification table

#### 3.5: Phase 4 - Integration (Week 9, Days 1-5)
- JSON template generator
- Dynamic forms
- Batch processing
- Cross-reference linking
- Validation

#### 3.6: Phase 5 - Mapping & Reports (Week 9, Days 3-7)
- Auto-generate reports
- Visual knowledge graph
- Export as PNG/SVG

---

## 🗂 ФАЗА 4: ENTITIES MANAGEMENT & LIBRARIES

**Длительность:** 3 недели
**Цель:** Comprehensive interface для ENTITIES ecosystem

### Подфазы

#### 4.1: Libraries Browser (Week 10, Days 1-5)
- Libraries Overview
- Entity List View
- Entity Detail View
- Cross-references section

#### 4.2: Cross-Reference Management (Week 10, Days 3-7)
- Validator
- Auto-fix tools
- Cross-Reference Editor
- Visualization

#### 4.3: Entity Templates & Bulk Operations (Week 11, Days 1-3)
- Pre-defined templates
- Bulk import/export
- Duplicate detection

#### 4.4: Entity Analytics (Week 11, Days 2-5)
- Analytics Dashboard
- Charts
- Export reports

---

## 📊 ФАЗА 5: PROGRESS TRACKING & MONITORING

**Длительность:** 3 недели
**Цель:** Comprehensive progress tracking, dashboards, monitoring

### Подфазы

#### 5.1: Progress Tracker Sync (Week 12, Days 1-2) ⚠️ КРИТИЧНО
**✅ Resolve ISS-RES-001**
- Batch update script
- Automated sync
- Verification

#### 5.2: Main Dashboard (Week 12, Days 1-5)
**✅ Resolve ISS-RES-004**
- System Overview
- Current Status
- Phase Distribution
- Entity Growth
- Team Performance
- Recent Activity

#### 5.3: Video Progress Monitoring (Week 12-13, Days 3-7)
- Progress Tracker Page
- Phase progress visualization
- Time tracking
- Bottleneck detection

#### 5.4: Reports Generator (Week 13, Days 1-5)
- Weekly Report
- Monthly Report
- Video Report
- Entity Report
- Custom Report
- Export formats: PDF, Excel, CSV, JSON

---

## ✅ ФАЗА 6: QUALITY ASSURANCE & TESTING

**Длительность:** 2 недели
**Цель:** Comprehensive testing, bug fixes, optimization

### Подфазы

#### 6.1: Unit Testing (Week 14, Days 1-5) ⚠️ КРИТИЧНО
**✅ Resolve ISS-RES-010**
- Backend tests (Jest)
- Python tests (Pytest)
- Frontend tests (Jest + React Testing Library)
- **Target: 80%+ code coverage**

#### 6.2: Integration Testing (Week 14, Days 3-7)
- End-to-end workflow tests
- API integration tests
- Database integration tests

#### 6.3: Performance Testing (Week 15, Days 1-3)
- Load testing
- Stress testing
- Optimization

#### 6.4: User Acceptance Testing (Week 15, Days 2-5)
- UAT scenarios
- Usability testing
- Accessibility audit
- Bug tracking

#### 6.5: Bug Fixes & Refinements (Week 15, Days 3-7)
- Fix P0/P1 bugs
- Fix P2 bugs
- Code refactoring
- Documentation updates

---

## 🚀 ФАЗЫ 7-9: VERSION 2.0 (ПОСЛЕ v1.0 LAUNCH)

**Фаза 7:** Advanced Features & Automation (ML, batch processing, multi-AI)
**Фаза 8:** Collaboration & Workflow Optimization (team features, notifications)
**Фаза 9:** Knowledge Base & Advanced Analytics (semantic search, knowledge graph)

---

## 📈 TIMELINE И МЕТРИКИ

### Timeline Summary

| Phase | Duration | Focus | Key Deliverables |
|-------|----------|-------|------------------|
| **Phase 0** | 1 week | **Prompts & Planning** | Все промпты, детальные ТЗ для AI, architecture diagrams |
| **Phase 1** | 5 weeks | **Infrastructure** | Docker, PostgreSQL, Backend skeleton, Dropbox API |
| **Phase 2** | 3 weeks | **Search/Queue** | Search Queue + Video Queue UI/API |
| **Phase 3** | 4 weeks | **Video Processing** | 7-phase processing workflow (Phase 1-5) |
| **Phase 4** | 3 weeks | **Entities Management** | Libraries browser, cross-references |
| **Phase 5** | 3 weeks | **Progress Tracking** | Dashboards, monitoring, reports |
| **Phase 6** | 2 weeks | **Testing & QA** | Unit tests, bug fixes, optimization |
| **TOTAL v1.0** | **21 weeks** | **MVP Production Ready** | All critical features functional |
| **Buffer** | +4-5 weeks | **Learning curve + debugging** | |
| **REALISTIC TOTAL** | **25-26 weeks** | **~6 месяцев** | |

### Ключевые метрики успеха

**Phase 1-3 (Foundation):**
- ✅ All infrastructure deployed
- ✅ Search Queue functional
- ✅ Video Queue functional (90% automation)
- ✅ Full 7-phase processing workflow functional
- ✅ ISS-RES-005 resolved (Phase 2 automated → 90% total automation)
- ✅ ISS-RES-001 resolved (Progress tracker synced)

**Phase 4-6 (Quality):**
- ✅ Entities management system functional
- ✅ Cross-reference validation working
- ✅ Main Dashboard operational (ISS-RES-004 resolved)
- ✅ 80%+ code coverage
- ✅ <500ms API response times
- ✅ All P0/P1 bugs fixed

**Overall System Metrics:**
- ⏱️ **Processing time:** 2-3 hours → <30 min per video (90% automation)
- 📊 **Automation level:** 70% → 90%
- 🎯 **Quality score:** ≥0.90 per video
- 📈 **Throughput:** 10-20 videos/week (with batch processing)
- 💰 **ROI:** 60-75% time reduction
- ✅ **Success rate:** 95%+ videos successfully integrated

---

## 📁 КРИТИЧЕСКИЕ ФАЙЛЫ ДЛЯ СОЗДАНИЯ

### Backend Files
```
server/
├── src/
│   ├── server.ts
│   ├── config/
│   │   ├── database.ts
│   │   ├── redis.ts
│   │   └── dropbox.ts
│   ├── middleware/
│   │   └── auth.ts
│   ├── routes/
│   │   ├── auth.routes.ts
│   │   ├── search-queue.routes.ts
│   │   ├── video-queue.routes.ts
│   │   ├── videos.routes.ts
│   │   └── entities.routes.ts
│   ├── services/
│   │   ├── auth.service.ts
│   │   ├── search.service.ts
│   │   ├── video.service.ts
│   │   ├── dropbox.service.ts
│   │   ├── youtube.service.ts
│   │   └── ai.service.ts
│   ├── models/
│   │   ├── User.model.ts
│   │   ├── SearchQueue.model.ts
│   │   ├── VideoQueue.model.ts
│   │   └── VideoProgress.model.ts
│   └── utils/
│       ├── logger.ts
│       └── validators.ts
├── migrations/
├── seeds/
└── package.json
```

### Frontend Files
```
client/
├── src/
│   ├── App.tsx
│   ├── routes/
│   │   └── index.tsx
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── SearchQueue.tsx
│   │   ├── VideoQueue.tsx
│   │   ├── VideoDetail.tsx
│   │   └── EntitiesBrowser.tsx
│   ├── components/
│   │   ├── ui/ (shadcn/ui components)
│   │   ├── search-queue/
│   │   ├── video-queue/
│   │   ├── dashboard/
│   │   └── common/
│   ├── services/
│   │   └── api.ts
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useVideos.ts
│   │   └── useEntities.ts
│   ├── store/
│   │   ├── authStore.ts
│   │   └── themeStore.ts
│   └── styles/
│       ├── globals.css
│       └── components.css
└── package.json
```

### Infrastructure Files
```
/
├── docker-compose.yml
├── Dockerfile.frontend
├── Dockerfile.backend
├── .github/
│   └── workflows/
│       └── ci.yml
└── nginx.conf
```

---

## ⚠️ РИСКИ И МИТИГАЦИЯ

### Технические риски

1. **AI API rate limits**
   - **Митигация:** Multi-API support, queueing, retry logic, caching

2. **Data migration issues**
   - **Митигация:** Extensive testing, backup strategy, rollback plan

3. **Performance bottlenecks**
   - **Митигация:** Load testing, optimization, caching, CDN

4. **Security vulnerabilities**
   - **Митигация:** Security audit, penetration testing, regular updates

### Бизнес-риски

1. **User adoption**
   - **Митигация:** User training, documentation, onboarding

2. **Budget overruns**
   - **Митигация:** Phased approach, MVP first, monitor costs

3. **Timeline delays**
   - **Митигация:** Agile methodology, regular sprints, buffer time

---

## ✅ КРИТЕРИИ ГОТОВНОСТИ v1.0

### Дизайн
- ✅ Соответствует референсу: https://adminrhs.github.io/Video-catalog/
- ✅ Dark/Light mode работает корректно
- ✅ Все цвета из Design System используются
- ✅ Smooth transitions (300ms) на всех элементах
- ✅ Responsive на всех устройствах (320px-1440px+)
- ✅ Custom scrollbar styling применен

### Функционал
- ✅ Search Queue: создание, выполнение, результаты
- ✅ Video Queue: добавление, приоритизация, статусы
- ✅ Video Processing: все 7 фаз работают
- ✅ Entities Management: создание, редактирование, cross-references
- ✅ Progress Tracking: real-time мониторинг
- ✅ Reports: генерация и export
- ✅ API integration: все endpoints работают
- ✅ YouTube API: метаданные и транскрипты загружаются
- ✅ Dropbox API: синхронизация ENTITIES

### UX
- ✅ Все hover states работают
- ✅ Loading states показываются
- ✅ Error handling реализован
- ✅ Success notifications показываются
- ✅ Empty states с CTA кнопками
- ✅ Smooth scrolling

### Качество
- ✅ 80%+ code coverage
- ✅ <500ms API response times
- ✅ Zero P0/P1 bugs
- ✅ Security audit passed
- ✅ Performance benchmarks met

---

## 🎯 СЛЕДУЮЩИЕ ШАГИ

1. **Финализировать план** с stakeholders
2. **Создать Phase 0 промпты** (1 неделя)
3. **Setup development environment** (Docker, PostgreSQL, Redis)
4. **Begin Phase 1** (Infrastructure)

---

## 📝 ЗАКЛЮЧЕНИЕ

Этот план обеспечивает:
- ✅ **Comprehensive coverage** всего функционала из документации
- ✅ **Structured 9-phase approach** с 5+ подфазами каждая (v1.0 = Phases 0-6, v2.0 = Phases 7-9)
- ✅ **Clear deliverables** для каждой подфазы
- ✅ **Resolution of critical issues** для v1.0 (ISS-RES-001, ISS-RES-005, ISS-RES-004)
- ✅ **90% automation achievement** (current 70% → target 90%)
- ✅ **Production-ready MVP** at end of Phase 6
- ✅ **Realistic timeline** для 1 разработчика (25-26 weeks с buffer)
- ✅ **Scalable architecture** (handles 100+ videos, multiple users)
- ✅ **AI-assisted development** (детальные промпты для каждого этапа)

Система трансформируется из collection of scripts в полноценный **enterprise-grade knowledge management platform**.

---

**ГОТОВО К РАЗРАБОТКЕ! 🚀**

*Документ создан: 2025-12-08*
*Версия: 1.0*
*Статус: Утверждено*
