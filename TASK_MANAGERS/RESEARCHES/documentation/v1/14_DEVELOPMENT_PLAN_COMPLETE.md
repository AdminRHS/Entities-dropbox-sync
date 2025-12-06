# План Разработки Приложения для Системы RESEARCHES 2

## 📋 Краткое Резюме

**Что создаем:** Веб-приложение для автоматизации обработки YouTube видео с таксономической классификацией контента

**Масштаб:**
- 7-фазный workflow (Search → Queue → Transcription → Extraction → Gap Analysis → Integration → Mapping)
- 752+ entities в таксономии (Tools, Workflows, Objects, Skills, Professions)
- 300+ страниц документации
- 21 Python script + 50+ AI промптов

**Tech Stack:** React 19 + ShadCN UI + Node.js (Express) + Prisma + PostgreSQL + Dropbox API

**Команда:** Solo Developer (AI-ассистируемая разработка)

**Методология:**
- ⚠️ **КРИТИЧНО:** Разработка начинается ТОЛЬКО после завершения Фазы 0
- 📝 **Фаза 0 обязательна:** Полное описание + архитектура + проектирование
- 🤖 **AI-генерация кода:** Только ПОСЛЕ полной документации Фазы 0
- ⚡ **Цель:** Максимально быстрая разработка через AI-ассистирование

**Timeline (Solo):**
- **Фаза 0:** 2-3 недели (критическая фаза планирования)
- **MVP:** 2-3 месяца (с AI-генерацией)
- **v1.0:** 4-6 месяцев (с AI-генерацией)

**ROI:** 550+ часов/год экономии при 100 видео/год

**Критические Вызовы:**
1. ISS-RES-005: Phase 2 automation (450 часов/год ROI)
2. ISS-RES-001: VIDEO_PROGRESS_TRACKER desync
3. ISS-RES-010: Unit testing (80%+ coverage needed)

---

## Общий Обзор

### Цель
Создать комплексное веб-приложение для автоматизации 7-фазного процесса обработки видео контента с интеграцией в систему таксономии ENTITIES (752+ сущностей, 421 шаблон задач).

### Текущее Состояние
- **Документация:** 300+ страниц (v1 техническая, v2 workflow, таксономия)
- **Автоматизация:** 70% (цель: 90%+)
- **Критические Issues:** ISS-RES-001 (десинхронизация), ISS-RES-005 (Phase 2 не автоматизирована)
- **Скрипты:** 21 Python скрипт (70% покрытия)
- **Промпты:** 50+ AI промптов (PMT-004, PMT-007, PMT-009)

### Ключевые Файлы для Анализа
- `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\call.md` - Требования менеджмента
- `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\technical\04_ID_System_Standard.md` - Стандарт ID
- `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\v2\01_STEP_BY_STEP_WORKFLOWS.md` - Workflow

---

## ФАЗА 0: ПОДГОТОВКА И АНАЛИЗ СУЩЕСТВУЮЩЕЙ СИСТЕМЫ

### Подфаза 0.1: Анализ Текущей Инфраструктуры (3-5 дней)
**Цель:** Полное понимание существующих систем и интеграций

**Задачи:**
- Анализ 21 Python скрипта (process_video.py, video_gap_analyzer.py, video_json_updater.py)
- Изучение структуры данных CSV (Search_Queue, Video_Queue, VIDEO_PROGRESS_TRACKER)
- Анализ JSON схем (Tools, Objects, Workflows - 25+ полей каждая)
- Документирование Dropbox API интеграции
- Маппинг микросервисов (Talents, Libraries)

**Критические Файлы:**
- `scripts/process_video.py` - Главный оркестратор
- `DATA/Video_Queue_Master.csv` - Очередь видео
- `DATA/RESEARCHES_Master_List.csv` - Реестр исследований
- `LIBRARIES/Tools/AI_Tools/*.json` - Схемы инструментов

**Ожидаемые Результаты:**
- Карта зависимостей между 21 скриптом
- Документация API endpoints (Dropbox, Talents, Libraries)
- Список потенциальных конфликтов и рисков

### Подфаза 0.2: Аудит Таксономии и ID Системы (2-3 дня)
**Цель:** Валидация существующей таксономии и стандартов ID

**Задачи:**
- Проверка 752+ сущностей на соответствие стандарту 04_ID_System_Standard.md
- Аудит 7 типов сущностей (WRF, TOL, OBJ, ACT, PRF, SKL, DPT)
- Валидация двунаправленных cross-references
- Анализ Master Lists (Libraries_Master_List.csv, Taxonomy_Master_List.csv)

**Критические Файлы:**
- `technical/04_ID_System_Standard.md` - Стандарт ID
- `DATA/Libraries_Master_List.csv` - Мастер список библиотек
- `DATA/Taxonomy_Master_List.csv` - Мастер список таксономии

**Ожидаемые Результаты:**
- Отчет о соответствии ID стандартам
- Список сущностей с некорректными ID
- План миграции на новый стандарт (если нужно)

### Подфаза 0.3: Анализ Критических Issues (1-2 дня)
**Цель:** Приоритизация технического долга

**Задачи:**
- Глубокий анализ 5 HIGH priority issues
- Оценка влияния ISS-RES-001 (десинхронизация tracker)
- Оценка ROI для ISS-RES-005 (Phase 2 automation - 450 часов/год)
- Планирование ISS-RES-010 (unit tests - 80%+ покрытия)

**Критические Issues:**
1. **ISS-RES-001** (CRITICAL): VIDEO_PROGRESS_TRACKER десинхронизация
2. **ISS-RES-005** (HIGH): Phase 2 не автоматизирована (30-45 мин/видео)
3. **ISS-RES-004** (HIGH): Отсутствует Progress Dashboard
4. **ISS-RES-010** (HIGH): Отсутствуют unit tests
5. **ISS-RES-008** (MEDIUM): Отсутствует YouTube API интеграция

**Ожидаемые Результаты:**
- Матрица приоритетов (Issue × Impact × Effort)
- Roadmap решения issues
- Список quick wins (быстрые победы)

### Подфаза 0.4: Выбор Tech Stack (2-3 дня)
**Цель:** Определение технологий для разработки

**Требования из call.md:**
- Корпоративные ресурсы only (Neon/Supabase для БД)
- Versioned APIs (v1, v2, v3+)
- Интеграция с Dropbox API
- Микросервисная архитектура
- Reusable widget для селекции/сравнения

**Утвержденный Tech Stack:**

**Frontend:**
- **Framework:** React 19+ с TypeScript
- **Build Tool:** Vite
- **State Management:** Zustand (легче Redux)
- **UI Components:** ShadCN UI (Radix UI + Tailwind CSS)
- **Styling:** Tailwind CSS v4
- **Data Grid:** TanStack Table (React Table v8) для CSV таблиц
- **Charts:** Recharts (для dashboard)
- **Forms:** React Hook Form + Zod (валидация)
- **Routing:** React Router v6

**Backend:**
- **Runtime:** Node.js 20+ (LTS)
- **Framework:** Express.js
- **API Style:** REST (OpenAPI/Swagger documentation)
- **ORM:** Prisma
- **Queue:** BullMQ с Redis (для job processing)
- **Validation:** Zod (unified с frontend)
- **File Uploads:** Multer (если нужно)

**Database:**
- **Primary:** PostgreSQL (через Prisma ORM)
- **Hosting:** Может быть локально сначала, потом Neon или Supabase
- **Cache:** Redis для queue и cache
- **Object Storage:** Dropbox API для CSV/JSON файлов

**AI Integration:**
- **Providers:** OpenAI API, Google Studio AI, Claude API
- **Orchestration:** Собственная wrapper система
- **Prompt Management:** Собственная система (уже есть 50+ prompts в PROMPTS/)

**DevOps:**
- **Testing:**
  - Frontend: Vitest + React Testing Library + Playwright
  - Backend: Jest + Supertest
  - Python: pytest (для существующих scripts)
- **CI/CD:** GitHub Actions (корпоративный GitHub)
- **Deployment:**
  - Frontend: Vercel или корпоративный сервер
  - Backend: Railway, Render, или корпоративный сервер
- **Monitoring:** Sentry (errors) + LogTail (logs)

**Ожидаемые Результаты:**
- Детальный tech stack document
- Proof of concept для критических интеграций
- Оценка стоимости инфраструктуры

### Подфаза 0.5: Архитектура Системы и API Design (3-4 дня)
**Цель:** Проектирование high-level архитектуры

**Компоненты:**

**1. Frontend Applications:**
```
┌─────────────────────────────────────────┐
│   React App (Main Interface)            │
│   ├── Search Queue Module (Phase 0)     │
│   ├── Video Queue Module (Phase 0→1)    │
│   ├── Processing Module (Phases 1-5)    │
│   ├── Taxonomy Editor (7 entity types)  │
│   ├── Dashboard Module (metrics)        │
│   └── Admin Module (issues, tasks)      │
└─────────────────────────────────────────┘
```

**2. Backend Services:**
```
┌─────────────────────────────────────────┐
│   API Gateway (versioned v1/v2/v3)      │
│   ├── Video Service                     │
│   ├── Taxonomy Service                  │
│   ├── Queue Service                     │
│   ├── AI Processing Service             │
│   ├── Integration Service (Dropbox)     │
│   └── Reporting Service                 │
└─────────────────────────────────────────┘
```

**3. Data Layer:**
```
┌─────────────────────────────────────────┐
│   PostgreSQL (Neon/Supabase)            │
│   ├── videos table                      │
│   ├── entities table (polymorphic)      │
│   ├── queues table                      │
│   ├── cross_references table            │
│   ├── issues table                      │
│   └── tasks table                       │
└─────────────────────────────────────────┘
```

**4. Job Queue:**
```
┌─────────────────────────────────────────┐
│   BullMQ + Redis                         │
│   ├── transcription-jobs                │
│   ├── extraction-jobs (Phase 2)         │
│   ├── gap-analysis-jobs (Phase 3)       │
│   ├── integration-jobs (Phase 4)        │
│   └── mapping-jobs (Phase 5)            │
└─────────────────────────────────────────┘
```

**API Endpoints (v1):**
```
/api/v1/videos
  POST   /search           # Phase 0: Search
  POST   /queue            # Phase 0→1: Add to queue
  GET    /queue            # Get queue
  POST   /:id/transcribe   # Phase 1: PMT-004
  POST   /:id/extract      # Phase 2: PMT-007 (auto)
  POST   /:id/analyze      # Phase 3: Gap analysis
  POST   /:id/integrate    # Phase 4: JSON creation
  GET    /:id/report       # Phase 5: Mapping report

/api/v1/taxonomy
  GET    /entities         # All entities
  POST   /entities         # Create entity
  GET    /entities/:id     # Get entity
  PUT    /entities/:id     # Update entity
  DELETE /entities/:id     # Delete entity
  POST   /entities/:id/link # Create cross-reference

/api/v1/issues
  GET    /                 # List issues
  POST   /                 # Create issue
  PUT    /:id              # Update issue

/api/v1/dashboard
  GET    /stats            # Overview stats
  GET    /queue-status     # Queue dashboard
  GET    /progress         # Progress tracker
```

**Ожидаемые Результаты:**
- Архитектурная диаграмма (C4 model)
- OpenAPI/Swagger спецификация
- Database schema (ERD диаграмма)
- Sequence диаграммы для 7 фаз

---

## ФАЗА 1: БАЗОВАЯ ИНФРАСТРУКТУРА И ФУНДАМЕНТ

### Подфаза 1.1: Database Schema и Migrations (3-4 дня)
**Цель:** Создать базовую структуру данных

**Таблицы:**

**1. videos:**
```sql
CREATE TABLE videos (
  id VARCHAR(20) PRIMARY KEY,        -- Video_XXX
  video_id VARCHAR(50) NOT NULL,     -- YouTube ID
  title VARCHAR(500),
  channel VARCHAR(200),
  duration INTEGER,
  url VARCHAR(500),
  queue_priority NUMERIC(4,2),       -- 0.00-1.00
  current_phase VARCHAR(20),         -- Phase_0, Phase_1, ...
  status VARCHAR(20),                -- pending, processing, completed
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);
```

**2. entities (polymorphic):**
```sql
CREATE TABLE entities (
  id VARCHAR(50) PRIMARY KEY,        -- WRF-XXX, TOL-CAT-XXX, etc.
  entity_type VARCHAR(20) NOT NULL,  -- WRF, TOL, OBJ, ACT, PRF, SKL, DPT
  name VARCHAR(200) NOT NULL,
  category VARCHAR(100),
  data JSONB NOT NULL,               -- Entity-specific fields
  source_video_id VARCHAR(20),       -- FK to videos
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  FOREIGN KEY (source_video_id) REFERENCES videos(id)
);
```

**3. cross_references:**
```sql
CREATE TABLE cross_references (
  id SERIAL PRIMARY KEY,
  from_entity_id VARCHAR(50) NOT NULL,
  to_entity_id VARCHAR(50) NOT NULL,
  reference_type VARCHAR(50),        -- uses_tool, creates_object, requires_skill
  created_at TIMESTAMP,
  FOREIGN KEY (from_entity_id) REFERENCES entities(id),
  FOREIGN KEY (to_entity_id) REFERENCES entities(id),
  UNIQUE(from_entity_id, to_entity_id, reference_type)
);
```

**4. queues:**
```sql
CREATE TABLE queues (
  id VARCHAR(20) PRIMARY KEY,        -- VQ-XXX or SEARCH-XXX
  queue_type VARCHAR(20),            -- search, video
  video_id VARCHAR(20),
  employee_name VARCHAR(100),
  priority NUMERIC(4,2),
  status VARCHAR(20),
  created_at TIMESTAMP,
  FOREIGN KEY (video_id) REFERENCES videos(id)
);
```

**5. issues:**
```sql
CREATE TABLE issues (
  id VARCHAR(20) PRIMARY KEY,        -- ISS-RES-XXX
  title VARCHAR(200),
  description TEXT,
  priority VARCHAR(20),              -- CRITICAL, HIGH, MEDIUM, LOW
  status VARCHAR(20),                -- OPEN, IN_PROGRESS, RESOLVED
  category VARCHAR(50),
  created_at TIMESTAMP,
  resolved_at TIMESTAMP
);
```

**6. tasks:**
```sql
CREATE TABLE tasks (
  id VARCHAR(20) PRIMARY KEY,        -- TASK-XXX
  title VARCHAR(200),
  description TEXT,
  phase VARCHAR(20),
  issue_id VARCHAR(20),
  status VARCHAR(20),
  created_at TIMESTAMP,
  FOREIGN KEY (issue_id) REFERENCES issues(id)
);
```

**Ожидаемые Результаты:**
- Prisma schema
- Migration скрипты
- Seed data для тестирования

### Подфаза 1.2: Backend API Core (4-5 дней)
**Цель:** Базовый REST API

**Структура Backend:**
```
backend/
├── src/
│   ├── services/
│   │   ├── video.service.ts
│   │   ├── taxonomy.service.ts
│   │   ├── queue.service.ts
│   │   └── ai.service.ts
│   ├── routes/
│   │   ├── v1/
│   │   │   ├── videos.routes.ts
│   │   │   ├── taxonomy.routes.ts
│   │   │   └── queue.routes.ts
│   │   └── v2/ (future)
│   ├── middleware/
│   │   ├── auth.middleware.ts
│   │   ├── validation.middleware.ts
│   │   └── error.middleware.ts
│   ├── utils/
│   │   ├── id-generator.ts      # 04_ID_System_Standard.md
│   │   └── dropbox.client.ts
│   └── index.ts
├── prisma/
│   └── schema.prisma
└── tests/
```

**Core Services:**

**1. Video Service:**
- CRUD операции для videos table
- Интеграция с YouTube API (ISS-RES-008)
- Phase transition logic
- Progress tracking

**2. Taxonomy Service:**
- CRUD для 7 типов сущностей
- ID generation (TOL-CAT-XXX format)
- Cross-reference management (bidirectional)
- JSON schema validation

**3. Queue Service:**
- Search queue management
- Video queue with priority scoring
- Dashboard data aggregation

**4. AI Service:**
- Wrapper для OpenAI/Claude APIs
- Prompt management (50+ prompts)
- Response parsing и validation

**Ожидаемые Результаты:**
- Базовый API с 20+ endpoints
- OpenAPI документация
- Integration tests (50%+ покрытия)

### Подфаза 1.3: Frontend Foundation (4-5 дней)
**Цель:** Базовая структура React приложения

**Структура Frontend:**
```
frontend/
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Button.tsx
│   │   │   ├── Table.tsx
│   │   │   ├── Card.tsx
│   │   │   └── ComparisonWidget.tsx  # Reusable widget!
│   │   ├── video/
│   │   │   ├── VideoCard.tsx
│   │   │   └── VideoQueue.tsx
│   │   └── taxonomy/
│   │       ├── EntityForm.tsx
│   │       └── EntityList.tsx
│   ├── pages/
│   │   ├── SearchQueue.tsx
│   │   ├── VideoQueue.tsx
│   │   ├── Processing.tsx
│   │   └── Dashboard.tsx
│   ├── hooks/
│   │   ├── useVideos.ts
│   │   └── useEntities.ts
│   ├── services/
│   │   └── api.service.ts
│   ├── store/
│   │   └── store.ts (Zustand)
│   └── App.tsx
└── tests/
```

**ComparisonWidget Component (из call.md):**
```tsx
<ComparisonWidget
  items={[
    { id: '1', label: 'Option A', data: {...} },
    { id: '2', label: 'Option B', data: {...} }
  ]}
  onSelect={(id) => handleSelection(id)}
  renderItem={(item) => <CustomCard {...item.data} />}
  compareMode="side-by-side" | "overlay" | "table"
/>
```

**Использование:**
- Phase 2: Выбор extracted entities (NEW/EXISTING/UPDATE)
- Phase 3: Gap analysis - выбор лучшего match
- Taxonomy editor: Merge duplicates
- Issue tracker: Приоритизация issues

**Core Components:**
- Layout с navigation
- Reusable Table (AG-Grid)
- Form components (React Hook Form + Zod)
- Loading states и error boundaries

**Ожидаемые Результаты:**
- Работающая React app
- 10+ reusable components
- Интеграция с backend API
- Component tests (Vitest)

### Подфаза 1.4: Dropbox Integration (2-3 дня)
**Цель:** Синхронизация с существующими CSV/JSON файлами

**Задачи:**
- Имплементация Dropbox API client
- CSV parser для 3 главных файлов:
  - Search_Queue_Master.csv
  - Video_Queue_Master.csv
  - VIDEO_PROGRESS_TRACKER.csv
- JSON parser для entities
- Bidirectional sync (Dropbox ↔ Database)

**Критические Файлы:**
- `DATA/Video_Queue_Master.csv` (13 полей)
- `DATA/RESEARCHES_Master_List.csv` (15+ полей)
- `LIBRARIES/Tools/AI_Tools/*.json` (25+ полей)

**Ожидаемые Результаты:**
- Dropbox sync service
- CSV import/export endpoints
- Conflict resolution strategy
- Automated sync scheduler (каждые 5-10 мин)

### Подфаза 1.5: ID System Implementation (2-3 дня)
**Цель:** Имплементация стандарта 04_ID_System_Standard.md

**Задачи:**
- ID generator для всех типов:
  - Video_XXX, VQ-XXX, SEARCH-XXX
  - WRF-XXX, TOL-CAT-XXX, OBJ-CAT-XXX
  - SKL-XXX, PRF-XXX, ACT-CAT-XXX
  - ISS-RES-XXX, TASK-XXX, CHG-RES-YYYYMMDD-XXX
- Regex validation для каждого типа
- Auto-increment logic с zero-padding
- ID conflict detection

**Критический Файл:**
- `technical/04_ID_System_Standard.md` (972 lines)

**Ожидаемые Результаты:**
- ID generator library
- Validation utilities
- Unit tests (100% покрытия)

---

## ФАЗА 2: PHASE 0-1 - SEARCH И VIDEO QUEUE

### Подфаза 2.1: Search Queue Interface (3-4 дня)
**Цель:** Phase 0 - Research assignment система

**Функционал:**
- CRUD для search assignments
- Employee assignment
- Topic management
- Priority tracking
- Status workflow (New → In Progress → Completed)

**UI Components:**
- Search assignment form
- Employee selector
- Topic input с autocomplete
- Priority slider
- Status badges

**Ожидаемые Результаты:**
- Работающая search queue page
- Интеграция с backend API
- Export to CSV

### Подфаза 2.2: Video Queue Core (4-5 дней)
**Цель:** Phase 0→1 - Video accumulation и selection

**Функционал:**
- Add video to queue (manual URL или YouTube API)
- Video metadata extraction (title, channel, duration)
- Priority scoring algorithm (текущая формула из документации)
- Batch selection (до 20 видео)
- Queue visualization

**Priority Algorithm (из Video_Queue_Master.csv):**
```
Priority =
  (Relevance × 0.4) +
  (Authority × 0.3) +
  (Freshness × 0.2) +
  (Completeness × 0.1)
```

**UI Components:**
- Video card с thumbnail
- Priority indicator (color-coded)
- Batch selection checkbox
- Filter и sort controls
- Queue statistics

**Критический Файл:**
- `scripts/add_video_to_queue_simple.py`
- `01_VIDEO_QUEUE/Video_Queue_Dashboard.html`

**Ожидаемые Результаты:**
- Video queue page
- Priority calculator
- Batch selection UI
- Dashboard widgets

### Подфаза 2.3: Video Queue Dashboard (3-4 дня)
**Цель:** Визуализация queue metrics

**Metrics:**
- Total videos in queue
- Videos by priority (High/Medium/Low)
- Videos by employee
- Average priority score
- Time in queue
- Processing rate

**Charts:**
- Priority distribution (pie chart)
- Queue trend (line chart)
- Employee statistics (bar chart)
- Phase distribution (stacked bar)

**Критический Файл:**
- `01_VIDEO_QUEUE/Video_Queue_Dashboard.html` (существующий HTML)

**Ожидаемые Результаты:**
- Interactive dashboard
- Real-time updates
- Export reports (PDF/Excel)

### Подфаза 2.4: YouTube API Integration (2-3 дня)
**Цель:** Решение ISS-RES-008 - Auto-fetch metadata

**Функционал:**
- YouTube Data API v3 integration
- Auto-fetch title, channel, duration, thumbnail
- Video validation (exists, accessible)
- Quota management (10,000 units/day)

**ROI:** 5-10 минут экономии на видео × 100 видео/год = 8-16 часов/год

**Ожидаемые Результаты:**
- YouTube API client
- Metadata auto-fill
- Error handling (private/deleted videos)

### Подфаза 2.5: Queue Automation и Notifications (2-3 дня)
**Цель:** Автоматизация queue management

**Функционал:**
- Auto-priority recalculation (ежедневно)
- Queue capacity warnings (>20 videos)
- Email notifications для employees
- Slack integration (optional)

**Ожидаемые Результаты:**
- Scheduled jobs (cron или BullMQ)
- Notification service
- Email templates

---

## ФАЗА 3: PHASE 1-2 - TRANSCRIPTION И EXTRACTION

### Подфаза 3.1: Phase 1 - Transcription Interface (3-4 дня)
**Цель:** PMT-004 integration для transcription

**Функционал:**
- Trigger transcription (button)
- PMT-004 prompt execution
- Progress indicator
- Transcription editor (markdown)
- Entity pre-categorization (37+ types)

**PMT-004 Output:**
```markdown
# Video_XXX Transcription

## Metadata
- Title: ...
- Channel: ...
- Duration: ...

## Entities Found
### Tools (TOL)
- Tool 1: [Name] - [Description]
- Tool 2: ...

### Objects (OBJ)
- Object 1: ...

### Workflows (WRF)
- Workflow 1: ...

... (37+ entity types)
```

**Критический Файл:**
- `PROMPTS/PMT-004_Transcription.txt`
- `v2/01_STEP_BY_STEP_WORKFLOWS.md` (Phase 1 section)

**Ожидаемые Результаты:**
- Transcription page
- PMT-004 integration
- Markdown editor с preview
- Save to `02_TRANSCRIPTIONS/Video_XXX.md`

### Подфаза 3.2: Phase 2 - Extraction Automation (5-7 дней)
**Цель:** Решение ISS-RES-005 - Автоматизация Phase 2 (КРИТИЧНО)

**Текущее Состояние:**
- Manual process с PMT-007
- 30-45 минут на видео
- 20% automation

**Целевое Состояние:**
- 90%+ automation
- 5-10 минут на видео
- ROI: 450 часов/год при 100 видео/год

**Функционал:**
- Auto-parse transcription markdown
- Entity extraction с AI (PMT-007)
- Entity classification (37+ types)
- Deduplication logic
- Quality validation

**AI Pipeline:**
```
Transcription (MD)
  ↓
PMT-007 (AI Extraction)
  ↓
Entity List (structured JSON)
  ↓
Deduplication
  ↓
Validation
  ↓
Extraction Inventory (MD + JSON)
```

**Критические Файлы:**
- `PROMPTS/PMT-007_Extraction.txt`
- `03_ANALYSIS/Extractions/Video_XXX_Extraction_Inventory.md`

**Ожидаемые Результаты:**
- Extraction automation script
- Entity classifier (ML или rule-based)
- Deduplication algorithm
- Validation rules
- 90%+ automation level

### Подфаза 3.3: Entity Editor Interface (4-5 дней)
**Цель:** Manual review и editing для extracted entities

**Функционал:**
- Table с extracted entities
- Inline editing
- Entity type selector
- Merge/split entities
- Delete duplicates
- Quality score indicator

**UI Components:**
- AG-Grid для entity table
- Entity form modal
- Bulk actions toolbar
- Quality indicators
- **ComparisonWidget для merge duplicates**

**Ожидаемые Результаты:**
- Entity editor page
- CRUD operations
- Bulk editing
- Undo/redo

### Подфаза 3.4: PMT-007 Integration и Testing (3-4 дня)
**Цель:** AI integration для extraction

**Задачи:**
- PMT-007 prompt integration
- Response parsing (structured output)
- Error handling и retries
- Cost tracking (OpenAI API tokens)
- A/B testing (разные prompts)

**Ожидаемые Результаты:**
- PMT-007 service
- Response parser
- Test suite (10+ test cases)
- Cost monitoring

### Подфаза 3.5: Batch Processing для Phase 1-2 (2-3 дня)
**Цель:** Решение ISS-RES-006 - Process multiple videos

**Функционал:**
- Select multiple videos (из queue)
- Batch transcription
- Batch extraction
- Progress tracking (per video)
- Parallel processing (с rate limiting)

**Ожидаемые Результаты:**
- Batch processing UI
- Job queue (BullMQ)
- Progress indicators
- Error recovery

---

## ФАЗА 4: PHASE 3-4 - GAP ANALYSIS И INTEGRATION

### Подфаза 4.1: Phase 3 - Gap Analysis Engine (4-5 дней)
**Цель:** Automated gap analysis (уже 100% автоматизирована)

**Функционал:**
- Compare extracted entities vs LIBRARIES master lists
- Classification: NEW, EXISTING, UPDATE
- Match scoring (0.00-1.00)
- Gap coverage calculation
- Recommendations

**Algorithm:**
```
For each extracted entity:
  1. Search in master lists (fuzzy matching)
  2. Calculate match score
  3. Classify:
     - Score > 0.90 → EXISTING
     - Score 0.50-0.90 → UPDATE (potential match)
     - Score < 0.50 → NEW
  4. Generate recommendations
```

**Критический Файл:**
- `scripts/video_gap_analyzer.py`
- `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

**Ожидаемые Результаты:**
- Gap analysis service
- Fuzzy matching algorithm
- Gap report generator
- Visualization (coverage charts)
- **ComparisonWidget для выбора best match**

### Подфаза 4.2: Phase 4 - Integration Service (5-6 дней)
**Цель:** JSON creation и ENTITIES integration

**Функционал:**
- Create JSON files для NEW entities
- Update existing JSON files (UPDATE entities)
- Cross-reference creation (bidirectional)
- Backup before modifications
- Validation after changes

**JSON Creation Pipeline:**
```
Gap Analysis Report
  ↓
For each NEW entity:
  1. Generate ID (TOL-CAT-XXX format)
  2. Create JSON from template
  3. Populate fields
  4. Add cross-references
  5. Validate schema
  6. Save to ENTITIES/
  ↓
Update master lists
  ↓
Create backup
```

**Критические Файлы:**
- `scripts/video_json_updater.py`
- `LIBRARIES/Tools/AI_Tools/*.json` (templates)
- `v2/07_TAXONOMY_BUILDING.md`

**Ожидаемые Результаты:**
- Integration service
- JSON templates (7 entity types)
- Schema validator
- Backup system

### Подфаза 4.3: Cross-Reference Management (4-5 дней)
**Цель:** Bidirectional linking (required by taxonomy)

**Функционал:**
- Create cross-references between entities
- Bidirectional sync (if A links to B, B links to A)
- Cross-reference types:
  - Tool → creates → Object
  - Workflow → uses → Tool
  - Profession → requires → Skill
  - Workflow → requires → Action
- Validation (check both directions)

**Cross-Reference Table:**
```
| From Entity | Relation      | To Entity |
|-------------|---------------|-----------|
| TOL-AI-045  | creates       | OBJ-VIS-043 |
| OBJ-VIS-043 | created_by    | TOL-AI-045 |
| WRF-002     | uses_tool     | TOL-AI-045 |
| TOL-AI-045  | used_in       | WRF-002 |
```

**Ожидаемые Результаты:**
- Cross-reference service
- Bidirectional sync
- Validation rules
- Visual graph (network diagram)

### Подфаза 4.4: Master List Sync (3-4 дня)
**Цель:** Sync с CSV master lists

**Функционал:**
- Auto-update Libraries_Master_List.csv
- Auto-update Taxonomy_Master_List.csv
- Auto-update RESEARCHES_Master_List.csv
- Conflict detection
- Manual conflict resolution UI

**Критические Файлы:**
- `DATA/Libraries_Master_List.csv` (752+ entities)
- `DATA/Taxonomy_Master_List.csv` (421 task templates)
- `DATA/RESEARCHES_Master_List.csv`

**Ожидаемые Результаты:**
- Master list sync service
- Conflict resolver
- Audit log
- Rollback capability

### Подфаза 4.5: Backup и Version Control (2-3 дня)
**Цель:** Safe modifications с rollback

**Функционал:**
- Auto-backup before every JSON modification
- Version history для entities
- Rollback UI (restore previous version)
- Change tracking (audit log)

**Backup Strategy:**
```
ENTITIES/
├── LIBRARIES/
│   └── Tools/
│       └── AI_Tools/
│           ├── TOL-AI-045.json
│           └── .backups/
│               ├── TOL-AI-045_20251205_143022.json
│               └── TOL-AI-045_20251204_095511.json
```

**Ожидаемые Результаты:**
- Backup service
- Version history UI
- Rollback functionality
- Storage cleanup (keep 10 versions)

---

## ФАЗА 5: PHASE 5-6 - MAPPING И ARCHIVE

### Подфаза 5.1: Phase 5 - Mapping Reporter (3-4 дня)
**Цель:** Library mapping отчеты (уже автоматизирована)

**Функционал:**
- Generate Library Mapping Report
- List all created/updated entities
- Validate cross-references
- Calculate quality scores
- Export to PDF/Excel

**Quality Metrics:**
- **Gap Coverage:** % entity types filled (target: 80%+)
- **Match Score:** Average match quality (target: 0.90+)
- **Validation Score:** Data completeness (target: 0.95+)
- **Overall Quality:** Combined score (target: 0.90+)

**Критический Файл:**
- `scripts/video_integration_reporter.py`
- `03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md`

**Ожидаемые Результаты:**
- Mapping report generator
- Quality calculator
- PDF export
- Email notifications

### Подфаза 5.2: Validation Rules Engine (3-4 дня)
**Цель:** Automated validation для entities

**Validation Rules:**
1. **Required Fields:** Все обязательные поля заполнены
2. **ID Format:** Соответствует стандарту 04_ID_System_Standard.md
3. **Cross-References:** Bidirectional links exist
4. **JSON Schema:** Valid according to schema
5. **Unique IDs:** No duplicates
6. **URL Validity:** URLs accessible (optional)
7. **Category Validity:** Category exists in taxonomy

**Ожидаемые Результаты:**
- Validation engine
- 20+ validation rules
- Validation report
- Auto-fix suggestions

### Подфаза 5.3: Quality Score Dashboard (3-4 дня)
**Цель:** Визуализация качества обработки

**Metrics:**
- Quality scores per video
- Quality trends (over time)
- Entity type coverage
- Cross-reference completeness
- Validation pass rate

**Charts:**
- Quality trend line chart
- Coverage radar chart
- Validation pie chart
- Entity type distribution

**Ожидаемые Результаты:**
- Quality dashboard
- Interactive charts
- Drill-down capability
- Export reports

### Подфаза 5.4: Phase 6 - Archive System (2-3 дня)
**Цель:** Completed research archival

**Функционал:**
- Mark video as completed
- Move files to archive
- Create archive report
- Update VIDEO_PROGRESS_TRACKER
- Cleanup temp files

**Archive Structure:**
```
RESEARCHES 2/
└── 05_ARCHIVE/
    └── Video_XXX/
        ├── Video_XXX.md (transcription)
        ├── Video_XXX_Extraction_Inventory.md
        ├── Video_XXX_Gap_Analysis.md
        ├── Video_XXX_Library_Mapping_Report.md
        └── created_entities/
            ├── TOL-AI-045.json
            └── OBJ-VIS-043.json
```

**Ожидаемые Результаты:**
- Archive service
- Archive browser UI
- Search archived videos
- Restore capability

### Подфаза 5.5: Reports Archive (2-3 дня)
**Цель:** 25+ reports per video management

**Reports (из документации):**
- Phase reports (7 reports)
- Quality reports (5 reports)
- Entity reports (10+ reports)
- Statistics reports (5 reports)

**Функционал:**
- Auto-generate all reports
- Archive reports
- Search reports
- Export reports (PDF/Excel/JSON)

**Ожидаемые Результаты:**
- Report generator
- Report templates (25+)
- Report browser
- Scheduled reporting

---

## ФАЗА 6: DASHBOARD И MONITORING

### Подфаза 6.1: Progress Dashboard (5-6 дней)
**Цель:** Решение ISS-RES-004 - Real-time visibility

**Функционал:**
- Overview statistics
- Videos by phase (7 phases)
- Processing timeline
- Employee statistics
- Tool statistics
- Real-time updates (WebSocket)

**Dashboard Sections:**
1. **Overview:**
   - Total videos (28+)
   - Completed (XX)
   - In progress (XX)
   - Automation level (70% → 90%)

2. **Phase Distribution:**
   - Phase 0: XX videos
   - Phase 1: XX videos
   - Phase 2: XX videos
   - ... (stacked bar chart)

3. **Employee Stats:**
   - Videos per employee
   - Average processing time
   - Quality scores

4. **Tool Stats:**
   - Most used tools
   - Tools by category
   - New tools added

5. **Quality Metrics:**
   - Average quality score
   - Gap coverage
   - Validation pass rate

**Критический Issue:** ISS-RES-004 (HIGH priority)

**Ожидаемые Результаты:**
- Interactive dashboard
- Real-time updates
- Responsive design
- Export capabilities

### Подфаза 6.2: VIDEO_PROGRESS_TRACKER Sync (3-4 дня)
**Цель:** Решение ISS-RES-001 (CRITICAL) - Desync fix

**Проблема:**
- VIDEO_PROGRESS_TRACKER.csv desynchronized
- Phase status не соответствует реальности
- Manual updates нужны

**Решение:**
- Auto-update tracker after phase transitions
- Batch sync script
- Conflict detection
- Manual override UI

**Критический Issue:** ISS-RES-001 (CRITICAL priority)

**Ожидаемые Результаты:**
- Sync service
- Batch update script
- Conflict resolver
- Audit log

### Подфаза 6.3: Real-Time Notifications (3-4 дня)
**Цель:** Real-time updates для пользователей

**Функционал:**
- WebSocket connection
- Push notifications (browser)
- Email notifications
- Slack integration (optional)

**Events:**
- Video added to queue
- Phase completed
- Extraction finished (Phase 2)
- Quality score below threshold
- Error occurred

**Ожидаемые Результаты:**
- WebSocket server
- Notification service
- Email templates
- Browser push API

### Подфаза 6.4: Monitoring и Logging (2-3 дня)
**Цель:** System health monitoring

**Функционал:**
- Application logs (LogTail или similar)
- Error tracking (Sentry)
- Performance monitoring (response times)
- API usage tracking
- Database query analytics

**Metrics:**
- API latency (p50, p95, p99)
- Error rate
- Queue depth
- Processing throughput
- Database connections

**Ожидаемые Результаты:**
- Logging infrastructure
- Error tracking
- Performance dashboard
- Alerts (Slack/Email)

### Подфаза 6.5: Admin Panel (3-4 дня)
**Цель:** System administration UI

**Функционал:**
- User management
- System settings
- Job queue management
- Database browser
- Script execution UI (21 Python scripts)
- Backup/restore

**Ожидаемые Результаты:**
- Admin panel
- Role-based access
- Audit log
- System health page

---

## ФАЗА 7: TAXONOMY EDITOR И MANAGEMENT

### Подфаза 7.1: Entity CRUD Interface (4-5 дней)
**Цель:** Full taxonomy management

**Функционал для 7 типов сущностей:**
1. **Workflows (WRF-XXX)**
2. **Tools (TOL-CAT-XXX)**
3. **Objects (OBJ-CAT-XXX)**
4. **Actions (ACT-CAT-XXX)**
5. **Professions (PRF-XXX)**
6. **Skills (SKL-XXX)**
7. **Departments (DPT-XXX)**

**UI Components:**
- Entity list (AG-Grid с filters)
- Entity form (dynamic based on type)
- Entity preview
- Duplicate detector
- Bulk operations
- **ComparisonWidget для merge**

**Критический Файл:**
- `v2/07_TAXONOMY_BUILDING.md`
- `taxonomy/03_WORKING_EXAMPLES.md`

**Ожидаемые Результаты:**
- 7 entity editors
- Reusable form components
- Validation для каждого типа
- Entity templates

### Подфаза 7.2: Cross-Reference Editor (3-4 дня)
**Цель:** Visual cross-reference management

**Функционал:**
- Network graph visualization
- Drag-and-drop linking
- Bidirectional sync
- Link validation
- Bulk link operations

**Visualization:**
- Force-directed graph (D3.js или vis.js)
- Entity nodes (color by type)
- Relationship edges (labeled)
- Zoom/pan/filter controls

**Ожидаемые Результаты:**
- Graph editor
- Link manager
- Visual validation
- Export graph (SVG/PNG)

### Подфаза 7.3: Category Management (2-3 дня)
**Цель:** Category system для Tools/Objects/Actions

**Categories (из документации):**
- **Tools:** AI, Design, Video, Photo, Audio, 3D, Dev, etc.
- **Objects:** Visual, Text, Data, Interactive, etc.
- **Actions:** Create, Edit, Analyze, etc.

**Функционал:**
- CRUD для categories
- Category hierarchy
- Category templates
- Auto-categorization (ML или rules)

**Ожидаемые Результаты:**
- Category manager
- Hierarchy editor
- Auto-categorization
- Category statistics

### Подфаза 7.4: Master List Management (3-4 дня)
**Цель:** UI для master lists

**Master Lists:**
1. Libraries_Master_List.csv (752+ entities)
2. Taxonomy_Master_List.csv (421 task templates)
3. RESEARCHES_Master_List.csv

**Функционал:**
- View/edit master lists
- Import/export CSV
- Bulk operations
- Duplicate detection
- Merge entities

**Ожидаемые Результаты:**
- Master list editor
- CSV import/export
- Duplicate resolver
- Merge wizard

### Подфаза 7.5: Taxonomy Statistics (2-3 дня)
**Цель:** Taxonomy analytics

**Statistics:**
- Total entities (752+)
- Entities by type
- Entities by category
- Cross-reference density
- Growth over time (new entities per month)
- Top entities (most referenced)

**Charts:**
- Entity type distribution
- Category breakdown
- Growth trend
- Network metrics (centrality, clustering)

**Ожидаемые Результаты:**
- Statistics dashboard
- Interactive charts
- Export reports
- Trend analysis

---

## ФАЗА 8: ISSUES, TASKS И CHANGE MANAGEMENT

### Подфаза 8.1: Issue Tracking System (4-5 дней)
**Цель:** ISS-RES-XXX management

**Функционал:**
- CRUD для issues
- Priority/status workflow
- Category management
- Issue templates
- Linked tasks
- Linked changes

**Issue Fields (из 06_Issues_Registry.md):**
- ID (ISS-RES-XXX)
- Title
- Description
- Priority (CRITICAL, HIGH, MEDIUM, LOW)
- Status (OPEN, IN_PROGRESS, RESOLVED, CLOSED)
- Category
- Estimated Effort
- Actual Effort
- Assignee
- Created/Resolved dates

**Критический Файл:**
- `issues/06_Issues_Registry.md` (12 issues documented)

**Ожидаемые Результаты:**
- Issue tracker
- Issue board (Kanban)
- Issue templates
- Effort tracking
- **ComparisonWidget для приоритизации**

### Подфаза 8.2: Task Management (3-4 дня)
**Цель:** TASK-XXX management

**Функционал:**
- CRUD для tasks
- Phase assignment
- Issue linking
- Task templates
- Dependency tracking
- Gantt chart (optional)

**Task Fields:**
- ID (TASK-XXX)
- Title
- Description
- Phase (PHS-RES-001 to PHS-RES-009)
- Issue ID
- Status
- Priority
- Estimated/Actual effort

**Ожидаемые Результаты:**
- Task manager
- Task board
- Dependency graph
- Progress tracking

### Подфаза 8.3: Change Log System (3-4 дня)
**Цель:** CHG-RES-YYYYMMDD-XXX tracking (из call.md)

**Функционал:**
- Auto-generate change entries
- Link to issues/tasks
- Category (FEATURE, BUGFIX, IMPROVEMENT, DOCS, REFACTOR, DEPRECATED)
- Version tracking
- Export changelog (markdown)

**Change Entry Format:**
```markdown
## CHG-RES-20251205-001
**Date:** 2025-12-05
**Category:** FEATURE
**Title:** Phase 2 Automation Implementation
**Description:** Automated extraction process using PMT-007
**Related Issues:** ISS-RES-005
**Related Tasks:** TASK-007, TASK-008, TASK-009
**Impact:** ROI 450 hours/year saved
```

**Критический Файл:**
- `technical/04_ID_System_Standard.md` (Change log section)

**Ожидаемые Результаты:**
- Changelog manager
- Auto-generation
- Markdown export
- Version tagging

### Подфаза 8.4: Traceability Matrix (2-3 дня)
**Цель:** Bidirectional traceability Issue ↔ Task ↔ Change

**Функционал:**
- Traceability viewer
- Impact analysis (if change X, what issues/tasks affected?)
- Coverage matrix (all issues have tasks?)
- Audit trail

**Matrix View:**
```
| Issue ID    | Tasks             | Changes             | Status   |
|-------------|-------------------|---------------------|----------|
| ISS-RES-005 | TASK-007,008,009  | CHG-20251205-001    | RESOLVED |
| ISS-RES-001 | TASK-003,004      | CHG-20251203-002    | OPEN     |
```

**Ожидаемые Результаты:**
- Traceability matrix
- Impact analyzer
- Coverage report
- Audit log

### Подфаза 8.5: Roadmap Viewer (2-3 дня)
**Цель:** Visual development roadmap

**Функционал:**
- Timeline view (v1.0, v2.0, v3.0)
- Phase breakdown (9 phases)
- Task dependencies
- Milestone tracking
- Progress indicators

**Roadmap Phases (из call.md):**
- **v1.0 (Phases 1-3):** Stabilization, Automation, Monitoring
- **v2.0 (Phases 4-6):** QA, AI/ML, Multi-Source
- **v3.0 (Phases 7-9):** Collaboration, Analytics, Knowledge Base

**Ожидаемые Результаты:**
- Roadmap timeline
- Milestone tracker
- Phase visualizer
- Export (PDF/PNG)

---

## ФАЗА 9: TESTING, OPTIMIZATION И DEPLOYMENT

### Подфаза 9.1: Unit Testing (5-7 дней)
**Цель:** Решение ISS-RES-010 - 80%+ test coverage

**Testing Strategy:**

**Backend Tests (Jest + Supertest):**
- Services (video, taxonomy, queue, ai)
- API routes (v1 endpoints)
- Database operations (Prisma)
- ID generation/validation
- Cross-reference logic
- Gap analysis algorithm
- Integration logic

**Frontend Tests (Vitest + React Testing Library):**
- Components (20+ components)
- Hooks (useVideos, useEntities)
- Pages (5+ pages)
- Forms (validation logic)
- State management (Zustand)

**Python Script Tests (pytest):**
- 21 Python scripts
- process_video.py
- video_gap_analyzer.py
- video_json_updater.py
- video_integration_reporter.py

**Target Coverage:**
- Backend: 80%+
- Frontend: 70%+
- Python scripts: 80%+
- Overall: 75%+

**Критический Issue:** ISS-RES-010 (HIGH priority)

**Ожидаемые Результаты:**
- 200+ unit tests
- Test coverage reports
- CI integration
- Test documentation

### Подфаза 9.2: Integration Testing (4-5 дней)
**Цель:** End-to-end testing для 7 фаз

**Test Scenarios:**
1. **Search → Queue → Transcription**
2. **Transcription → Extraction → Gap Analysis**
3. **Gap Analysis → Integration → Mapping**
4. **Full pipeline (Phase 0 → Phase 5)**
5. **Batch processing**
6. **Dropbox sync**
7. **AI integration (PMT-004, PMT-007)**

**Tools:**
- Playwright (E2E)
- Supertest (API testing)
- Mock APIs (Dropbox, YouTube, OpenAI)

**Ожидаемые Результаты:**
- 20+ integration tests
- E2E test suite
- Test fixtures
- Test documentation

### Подфаза 9.3: Performance Optimization (3-4 дня)
**Цель:** Optimize для 100+ videos

**Optimization Areas:**

**Backend:**
- Database indexing (on IDs, status, phase)
- Query optimization (N+1 problem)
- Caching (Redis для frequent queries)
- API pagination (для large lists)
- Batch operations (bulk inserts/updates)

**Frontend:**
- Code splitting (React.lazy)
- Memoization (React.memo, useMemo)
- Virtual scrolling (AG-Grid)
- Image lazy loading
- Bundle optimization (Vite)

**Database:**
- Index creation (videos.status, entities.entity_type)
- Query explain/analyze
- Connection pooling
- Read replicas (future)

**Target Metrics:**
- API latency: <200ms (p95)
- Page load: <2s (p95)
- Database queries: <50ms (p95)
- Frontend bundle: <500KB (gzipped)

**Ожидаемые Результаты:**
- Performance report
- Optimized queries
- Caching strategy
- Bundle reduction

### Подфаза 9.4: Security и Compliance (3-4 дня)
**Цель:** Security best practices

**Security Measures:**

**Authentication:**
- JWT или session-based auth
- Role-based access control (RBAC)
- Employee roles (Researcher, Manager, Admin)

**API Security:**
- Rate limiting (100 requests/min)
- CORS configuration
- Input validation (Zod schemas)
- SQL injection prevention (Prisma ORM)
- XSS prevention (sanitize HTML)

**Data Security:**
- Encryption at rest (database)
- Encryption in transit (HTTPS)
- API key management (environment variables)
- Sensitive data masking (logs)

**Compliance:**
- Audit logs (who, what, when)
- Data retention policies
- Backup/restore procedures
- GDPR compliance (if applicable)

**Ожидаемые Результаты:**
- Security audit report
- Authentication system
- RBAC implementation
- Compliance checklist

### Подфаза 9.5: Deployment и CI/CD (4-5 дней)
**Цель:** Production deployment

**Infrastructure:**

**Frontend:**
- Hosting: Vercel или корпоративный сервер
- CDN: Cloudflare
- Domain: custom domain
- SSL: Let's Encrypt

**Backend:**
- Hosting: Railway, Render, или корпоративный сервер
- Database: Neon или Supabase (PostgreSQL)
- Redis: Upstash или Redis Cloud
- Object Storage: Dropbox API

**CI/CD Pipeline (GitHub Actions):**
```yaml
.github/workflows/
├── test.yml         # Run tests on PR
├── lint.yml         # Lint code
├── deploy-prod.yml  # Deploy to production
└── deploy-dev.yml   # Deploy to development
```

**Stages:**
1. **Lint:** ESLint, Prettier
2. **Test:** Unit + Integration tests
3. **Build:** Frontend + Backend
4. **Deploy:** Vercel + Railway
5. **Smoke Tests:** Basic health checks

**Environment Variables:**
```
# Database
DATABASE_URL=postgresql://...
REDIS_URL=redis://...

# APIs
DROPBOX_ACCESS_TOKEN=...
OPENAI_API_KEY=...
YOUTUBE_API_KEY=...

# Auth
JWT_SECRET=...

# Monitoring
SENTRY_DSN=...
LOGTAIL_TOKEN=...
```

**Ожидаемые Результаты:**
- Production deployment
- CI/CD pipeline
- Environment setup
- Deployment documentation

### Подфаза 9.6: Documentation и Training (3-4 дня)
**Цель:** User и developer documentation

**Documentation:**

**User Documentation:**
- User guide (с screenshots)
- Video tutorials (3-5 videos)
- FAQ
- Troubleshooting guide

**Developer Documentation:**
- API documentation (OpenAPI/Swagger)
- Architecture diagrams (C4 model)
- Database schema (ERD)
- Code contribution guide
- Setup instructions

**Training Materials:**
- Onboarding checklist
- Role-specific guides (Researcher, Manager, Admin)
- Best practices
- Common workflows

**Ожидаемые Результаты:**
- User manual (50+ pages)
- API docs (Swagger UI)
- Video tutorials (3-5)
- Developer guide

---

## ОЦЕНКА УСИЛИЙ И TIMELINE

### По Фазам

| Фаза | Название | Подфазы | Дней | Недель |
|------|----------|---------|------|--------|
| 0 | Подготовка и Анализ | 5 | 14-22 | 3-4 |
| 1 | Базовая Инфраструктура | 5 | 17-23 | 3-5 |
| 2 | Search и Video Queue | 5 | 14-19 | 3-4 |
| 3 | Transcription и Extraction | 5 | 17-24 | 3-5 |
| 4 | Gap Analysis и Integration | 5 | 18-24 | 4-5 |
| 5 | Mapping и Archive | 5 | 15-21 | 3-4 |
| 6 | Dashboard и Monitoring | 5 | 16-21 | 3-4 |
| 7 | Taxonomy Editor | 5 | 14-19 | 3-4 |
| 8 | Issues и Change Management | 5 | 19-26 | 4-5 |
| 9 | Testing и Deployment | 6 | 25-34 | 5-7 |

**Общая Оценка:**
- **Дней:** 169-233 рабочих дней
- **Недель:** 34-47 недели
- **Месяцев:** 8-11 месяцев (при 5-дневной неделе)

### По Приоритетам

**MVP (Minimum Viable Product) - 4-5 месяцев:**
- Фаза 0: Подготовка
- Фаза 1: Инфраструктура
- Фаза 2: Queue система
- Фаза 3: Phase 1-2 (с automation)
- Фаза 6: Базовый dashboard

**v1.0 (Full System) - 7-8 месяцев:**
- MVP +
- Фаза 4: Phase 3-4
- Фаза 5: Phase 5-6
- Фаза 7: Taxonomy editor
- Фаза 9: Testing и deployment

**v2.0 (Optimized) - 10-11 месяцев:**
- v1.0 +
- Фаза 8: Issue tracking
- Performance optimization
- Advanced features

### Оценка для Solo Developer с AI-ассистированием

**КРИТИЧНО:** Фаза 0 должна быть завершена на 100% перед началом разработки!

**Фаза 0 - Планирование и Проектирование (2-3 недели):**
- Полное описание всех модулей
- Архитектурная документация (C4 model)
- Database schema (ERD с Prisma)
- API specification (OpenAPI/Swagger)
- Pseudo-code для всех компонентов
- UI/UX дизайн (Figma прототипы)
- Промпты для AI-генерации кода

**MVP (2-3 месяца с AI-генерацией):**
- Фаза 1: Инфраструктура (2 недели)
- Фаза 2: Queue система (2 недели)
- Фаза 3: Phase 1-2 с automation (3 недели)
- Фаза 6: Базовый dashboard (1 неделя)
- Тестирование и фиксы (2 недели)

**v1.0 (4-6 месяцев с AI-генерацией):**
- MVP + Фаза 4: Phase 3-4 (3 недели)
- Фаза 5: Phase 5-6 (2 недели)
- Фаза 7: Taxonomy editor (3 недели)
- Фаза 9: Testing и deployment (2 недели)

**v2.0 (7-9 месяцев с AI-генерацией):**
- v1.0 + Фаза 8: Issue tracking (2 недели)
- Performance optimization (1 неделя)
- Advanced features (3 недели)

**Ключ к успеху:**
- ✅ Тщательное планирование в Фазе 0
- ✅ Использование AI (Claude Code, Cursor, v0.dev) для генерации кода
- ✅ Копирование готовых компонентов (ShadCN UI)
- ✅ Максимальная автоматизация тестирования
- ✅ Фокус на MVP функциональности сначала

---

## КЛЮЧЕВЫЕ РИСКИ И МИТИГАЦИЯ

### Технические Риски

**1. Phase 2 Automation (ISS-RES-005) - ВЫСОКИЙ**
- **Риск:** Сложность AI extraction, низкая точность
- **Митигация:**
  - A/B testing разных prompts
  - Human-in-the-loop для валидации
  - Incremental automation (50% → 70% → 90%)
  - Fallback к manual process

**2. VIDEO_PROGRESS_TRACKER Sync (ISS-RES-001) - СРЕДНИЙ**
- **Риск:** Data corruption при sync
- **Митигация:**
  - Backups before sync
  - Dry-run mode
  - Manual conflict resolution UI
  - Rollback capability

**3. Dropbox API Rate Limits - СРЕДНИЙ**
- **Риск:** API quota exceeded
- **Митигация:**
  - Rate limiting (15 requests/min)
  - Queue для sync operations
  - Local caching
  - Exponential backoff

**4. AI API Costs - СРЕДНИЙ**
- **Риск:** High costs для 100+ videos
- **Митигация:**
  - Cost tracking per video
  - Budget alerts
  - Prompt optimization (shorter prompts)
  - Caching AI responses

**5. Database Scalability - НИЗКИЙ**
- **Риск:** Performance degradation at 500+ videos
- **Митигация:**
  - Database indexing
  - Query optimization
  - Read replicas (future)
  - Archival strategy

### Организационные Риски

**1. Требования могут измениться - ВЫСОКИЙ**
- **Митигация:**
  - Agile methodology (2-week sprints)
  - Regular stakeholder demos
  - Flexible architecture
  - Feature flags

**2. Недостаточное тестирование - СРЕДНИЙ**
- **Митигация:**
  - Test-driven development (TDD)
  - 80%+ coverage requirement
  - Automated CI/CD
  - QA engineer вовлечение

**3. Недостаточная документация - СРЕДНИЙ**
- **Митигация:**
  - Documentation-first approach
  - Code comments (JSDoc, docstrings)
  - API documentation (Swagger)
  - User guides с screenshots

---

## КРИТЕРИИ УСПЕХА

### Технические KPI

**Automation Level:**
- ✅ Phase 0→1: 50%+ (текущий: 30%)
- ✅ Phase 2: 90%+ (текущий: 20%) - **Критично**
- ✅ Overall: 90%+ (текущий: 70%)

**Quality Metrics:**
- ✅ Gap Coverage: 80%+
- ✅ Match Score: 0.90+
- ✅ Validation Score: 0.95+
- ✅ Overall Quality: 0.90+

**Performance:**
- ✅ API Latency: <200ms (p95)
- ✅ Page Load: <2s (p95)
- ✅ Database Queries: <50ms (p95)

**Testing:**
- ✅ Backend Coverage: 80%+
- ✅ Frontend Coverage: 70%+
- ✅ Integration Tests: 20+ scenarios

**Issues Resolved:**
- ✅ ISS-RES-001: VIDEO_PROGRESS_TRACKER sync
- ✅ ISS-RES-004: Progress Dashboard
- ✅ ISS-RES-005: Phase 2 automation (450 часов/год ROI)
- ✅ ISS-RES-010: Unit tests (80%+ coverage)

### Business KPI

**ROI:**
- ✅ Phase 2 automation: 450 часов/год saved
- ✅ YouTube API: 8-16 часов/год saved
- ✅ Batch processing: 100+ часов/год saved
- ✅ Total: 550+ часов/год saved

**User Adoption:**
- ✅ 5+ active users
- ✅ 100+ videos processed
- ✅ 90%+ user satisfaction

**System Reliability:**
- ✅ 99%+ uptime
- ✅ <1% error rate
- ✅ <24h bug fix time (critical)

---

## ДОПОЛНИТЕЛЬНЫЙ ФУНКЦИОНАЛ ИЗ CALL.MD

### Reusable Widget для Выбора/Сравнения
**Требование из call.md:** Создать переиспользуемый элемент для выбора вариантов

**Функционал:**
- Компонент для сравнения и выбора (например, "какой вариант более подходящий")
- Использование на множестве страниц:
  - Phase 2: Выбор extracted entities (NEW/EXISTING/UPDATE)
  - Phase 3: Gap analysis - выбор лучшего match
  - Taxonomy editor: Merge duplicates
  - Issue tracker: Приоритизация issues

**Компонент Structure:**
```tsx
<ComparisonWidget
  items={[
    { id: '1', label: 'Option A', data: {...} },
    { id: '2', label: 'Option B', data: {...} }
  ]}
  onSelect={(id) => handleSelection(id)}
  renderItem={(item) => <CustomCard {...item.data} />}
  compareMode="side-by-side" | "overlay" | "table"
/>
```

**Место разработки:** Фаза 1.3 - Frontend Foundation

---

## МЕТОДОЛОГИЯ РАЗРАБОТКИ (ИЗ CALL.MD)

### Документо-ориентированный Подход

**Принципы:**
1. **Documentation-First** - создавать документацию ДО начала разработки
2. **Планирование на 2 шага вперед** - AI работает быстрее человека
3. **Мультифазовый подход** - разбить на 9 фаз с подфазами
4. **Claude Code style** - полный контекст, примеры, структурированные промпты

**Структура документации (из call.md):**
```
documentation/
  ├── system/              # Системная документация
  ├── plans/               # Планы разработки
  ├── prompts/             # AI промпты (50+)
  ├── examples/            # Рабочие примеры
  ├── changelog/           # История изменений
  ├── v1/                  # Техническая референция (14 файлов)
  ├── v2/                  # Workflow guides (9 файлов)
  └── taxonomy/            # Таксономия (5 файлов)
```

### Работа с Корпоративными Ресурсами

**Требования (из call.md):**
- ✅ Корпоративный GitHub (не персональный)
- ✅ Корпоративная email
- ✅ Отдельный Chrome профиль для проекта
- ✅ Neon или Supabase (корпоративная БД)
- ✅ Корпоративные API keys (Dropbox, OpenAI, etc.)

**Инструменты:**
- **Primary:** VS Code + Claude Code (для ответственных задач)
- **Secondary:** Cursor IDE
- **Light tasks:** Gemini 30 (не критичные задачи)
- **Multitasking:** Запуск AI на 2-4 браузерах одновременно

### Журналирование Работы

**Daily Files (из call.md):**
- User inputs (1A, 2B, 3C...)
- AI responses и промпты
- Plans и decisions
- Issues и blockers

**Example Daily File:**
```markdown
# 2025-12-05 Daily Log

## 1A: User Request
Проанализировать документацию RESEARCHES 2

## 1B: Claude Response
Создан план с 9 фаз...

## 2A: User Feedback
...

## Issues
- ISS-RES-005: Phase 2 automation (HIGH)
```

---

## ВЕРСИОННОСТЬ API (ИЗ CALL.MD)

### API Version Roadmap

**Version 1 (MVP) - Простая:**
- Базовый CRUD для videos/entities
- Dropbox sync
- AI transcription (PMT-004)
- Queue management
- Dashboard (базовый)

**Version 2 (Интеграции):**
- Microservices integration (Talents, Libraries)
- Advanced queue algorithm
- Phase 2 automation (PMT-007)
- Progress Dashboard
- Batch processing

**Version 3+ (Scale):**
- ML prioritization
- Multi-source (YouTube, Perplexity, Twitter, Reddit)
- Real-time collaboration
- Advanced analytics
- GraphQL API

**API Versioning Strategy:**
```
/api/v1/videos
/api/v2/videos
/api/v3/videos

Headers:
  Accept: application/vnd.research.v2+json
```

---

## PSEUDO-CODE ДЛЯ КАЖДОЙ ВЕРСИИ (ИЗ CALL.MD)

### Version 1 Pseudo-Code

```pseudo
// Phase 0→1: Add video to queue
FUNCTION addVideoToQueue(videoUrl):
  video = fetchYouTubeMetadata(videoUrl)
  priority = calculatePriority(video)
  videoId = generateVideoId()  // Video_XXX

  INSERT INTO videos (id, url, title, priority, phase)
  VALUES (videoId, videoUrl, video.title, priority, 'Phase_0')

  INSERT INTO queues (id, video_id, status)
  VALUES (generateQueueId(), videoId, 'pending')

  syncToDropbox('Video_Queue_Master.csv')

  RETURN videoId

// Phase 1: Transcription
FUNCTION transcribeVideo(videoId):
  video = SELECT * FROM videos WHERE id = videoId

  prompt = loadPrompt('PMT-004')
  transcript = callAI(prompt, video.url)

  entities = parseTranscript(transcript)  // 37+ types

  saveMarkdown(transcript, `02_TRANSCRIPTIONS/${videoId}.md`)

  UPDATE videos SET phase = 'Phase_1', status = 'transcribed'
  WHERE id = videoId

  RETURN entities

// Phase 2: Extraction
FUNCTION extractEntities(videoId):
  transcriptPath = `02_TRANSCRIPTIONS/${videoId}.md`
  transcript = readFile(transcriptPath)

  prompt = loadPrompt('PMT-007')
  extraction = callAI(prompt, transcript)

  entities = parseExtraction(extraction)
  deduplicatedEntities = deduplicateEntities(entities)

  saveMarkdown(entities, `03_ANALYSIS/Extractions/${videoId}_Extraction_Inventory.md`)

  UPDATE videos SET phase = 'Phase_2' WHERE id = videoId

  RETURN deduplicatedEntities

// Phase 3: Gap Analysis
FUNCTION analyzeGaps(videoId):
  extraction = readExtractionInventory(videoId)
  masterLists = loadMasterLists(['Libraries', 'Taxonomy'])

  gaps = []
  FOR EACH entity IN extraction:
    matches = fuzzySearch(entity, masterLists)
    bestMatch = matches[0]

    classification = IF bestMatch.score > 0.90 THEN 'EXISTING'
                     ELSE IF bestMatch.score > 0.50 THEN 'UPDATE'
                     ELSE 'NEW'

    gaps.APPEND({
      entity: entity,
      classification: classification,
      bestMatch: bestMatch
    })

  saveMarkdown(gaps, `03_ANALYSIS/Gap_Analysis/${videoId}_Gap_Analysis.md`)

  UPDATE videos SET phase = 'Phase_3' WHERE id = videoId

  RETURN gaps

// Phase 4: Integration
FUNCTION integrateEntities(videoId):
  gaps = readGapAnalysis(videoId)

  FOR EACH gap IN gaps WHERE gap.classification == 'NEW':
    entityId = generateEntityId(gap.entity.type)  // TOL-CAT-XXX

    json = createJSONFromTemplate(gap.entity)
    json.id = entityId
    json.source_video = videoId

    addCrossReferences(json, gaps)

    backup(json.path)
    saveJSON(json, `ENTITIES/${json.path}`)

    updateMasterList(entityId, json)

  UPDATE videos SET phase = 'Phase_4' WHERE id = videoId

  RETURN createdEntities

// Phase 5: Mapping
FUNCTION generateMappingReport(videoId):
  createdEntities = getCreatedEntities(videoId)

  report = {
    videoId: videoId,
    totalEntities: createdEntities.length,
    byType: countByType(createdEntities),
    qualityScore: calculateQualityScore(createdEntities),
    crossReferences: validateCrossReferences(createdEntities)
  }

  saveMarkdown(report, `03_ANALYSIS/Library_Mapping/${videoId}_Library_Mapping_Report.md`)

  UPDATE videos SET phase = 'Phase_5', status = 'completed' WHERE id = videoId

  RETURN report
```

### Version 2 Pseudo-Code (с интеграциями)

```pseudo
// Microservices Integration
FUNCTION getEmployeeData(employeeId):
  response = callMicroservice('Talents', `/api/v1/employees/${employeeId}`)
  RETURN response.data

FUNCTION getToolData(toolId):
  response = callMicroservice('Libraries', `/api/v1/tools/${toolId}`)
  RETURN response.data

// Batch Processing
FUNCTION processBatch(videoIds[]):
  jobs = []

  FOR EACH videoId IN videoIds:
    job = createJob('transcription', videoId)
    jobs.APPEND(job)

  ENQUEUE jobs TO 'transcription-queue'

  RETURN jobIds

// Progress Dashboard (real-time)
FUNCTION getProgressDashboard():
  stats = {
    totalVideos: COUNT(*) FROM videos,
    byPhase: COUNT(*) FROM videos GROUP BY phase,
    byEmployee: JOIN videos WITH queues GROUP BY employee_name,
    byTool: COUNT entities WHERE entity_type = 'TOL' GROUP BY category,
    automation: calculateAutomationLevel()
  }

  broadcastWebSocket('dashboard-update', stats)

  RETURN stats
```

### Version 3+ Pseudo-Code (ML и Scale)

```pseudo
// ML Prioritization
FUNCTION mlPrioritize(videos[]):
  features = extractFeatures(videos)  // duration, channel, category, etc.

  predictions = mlModel.predict(features)

  FOR EACH video, prediction IN zip(videos, predictions):
    video.priority = prediction.priority
    video.estimatedValue = prediction.value

    UPDATE videos SET priority = video.priority WHERE id = video.id

  RETURN sortedVideos

// Multi-Source Integration
FUNCTION searchMultiSource(query):
  results = []

  // Parallel search
  youtubeResults = searchYouTube(query)
  perplexityResults = searchPerplexity(query)
  twitterResults = searchTwitter(query)

  results = deduplicate(youtubeResults + perplexityResults + twitterResults)

  RETURN results
```

---

## CHANGELOG СИСТЕМА (ИЗ CALL.MD)

### Changelog Требования

**Формат (CHG-RES-YYYYMMDD-XXX):**
- Дата-based ID
- Категория (FEATURE, BUGFIX, IMPROVEMENT, DOCS)
- Связь с Issue и Task
- Описание изменений

**Integration Points:**
- Auto-generate change entry после deployment
- Link к PR/commit
- Отображение в dashboard
- Export changelog.md для Release Notes

**Место разработки:** Фаза 8.3

---

## СЛЕДУЮЩИЕ ШАГИ

### Фаза 0 Action Items

1. **✅ Review этого плана с руководством**
2. **Задать вопросы по неясным моментам**
3. **Утвердить tech stack**
4. **Создать pseudo-code для всех фаз**
5. **Сформировать команду разработки**

### Утвержденные Решения и Открытые Вопросы

**✅ УТВЕРЖДЕНО:**
1. **Tech Stack:**
   - ✅ React 19+ для frontend
   - ✅ Express.js для backend
   - ✅ Prisma для ORM
   - ✅ PostgreSQL для БД
   - ✅ Dropbox API для file sync

**✅ УТОЧНЕНИЯ ПОЛУЧЕНЫ:**

2. **UI Library:**
   - ✅ **ShadCN UI** (современная библиотека на базе Radix UI + Tailwind CSS)
   - Преимущества: Копируемые компоненты, полный контроль, TypeScript-first

3. **Deployment:**
   - ✅ **Первоначально:** Vercel (frontend) + Railway/Render (backend)
   - ✅ **В будущем:** Миграция на корпоративный сервер
   - Стратегия: Быстрый старт на Vercel, потом плавная миграция

4. **Database Hosting:**
   - ✅ **Neon** (PostgreSQL) - скорее всего
   - Преимущества: Serverless PostgreSQL, легкая интеграция с Prisma, бесплатный tier

5. **Team:**
   - ✅ **Solo Developer:** Только вы один на данный момент
   - QA: Самостоятельное тестирование + автоматизация
   - Product Owner: Вы же

6. **Timeline:**
   - ✅ **Принцип:** Чем быстрее, тем лучше
   - ✅ **КРИТИЧНО:** Разработка НЕ НАЧИНАЕТСЯ до полного завершения Фазы 0
   - ✅ **Фаза 0 обязательна:** Полное описание + планирование + проектирование
   - ✅ **Подход:** AI-генерация кода только ПОСЛЕ завершения Фазы 0

7. **Budget:**
   - Инфраструктура: Neon Free tier + Vercel Hobby (бесплатно для старта)
   - AI API: OpenAI/Claude (~$50-100/мес)
   - Upstash Redis Free tier для queue

### Deliverables Фазы 0

- [ ] Architecture document (C4 model)
- [ ] Database schema (ERD)
- [ ] API specification (OpenAPI)
- [ ] Tech stack document
- [ ] Risk analysis document
- [ ] Pseudo-code для 9 фаз
- [ ] Промпты для каждой фазы
- [ ] Timeline и resource plan

---

**Автор плана:** Claude Code Agent
**Дата:** 2025-12-05
**Версия:** 4.0 (RU) - ФИНАЛЬНАЯ С УТОЧНЕНИЯМИ
**Статус:** READY FOR PHASE 0 EXECUTION

**Источники:**
- `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\` (300+ pages)
- `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\call.md`
- Анализ существующей системы (21 script, 50+ prompts, 752+ entities)

---

## 🎯 СЛЕДУЮЩИЙ ШАГ: СОХРАНЕНИЕ ДОКУМЕНТАЦИИ

**После утверждения этого плана, необходимо:**

1. **Сохранить этот полный план** в:
   - `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\v1\14_DEVELOPMENT_PLAN_COMPLETE.md`

2. **Создать краткое executive summary** в:
   - `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\documentation\DEVELOPMENT_PLAN_SUMMARY.md`

3. **Начать Фазу 0 - Детальное Проектирование:**
   - Создать Architecture document (C4 model)
   - Спроектировать Database schema (ERD с Prisma)
   - Написать API specification (OpenAPI/Swagger)
   - Создать UI/UX дизайн (Figma прототипы)
   - Подготовить промпты для AI-генерации кода

**Важно:** Разработка кода начнется ТОЛЬКО после полного завершения Фазы 0!
