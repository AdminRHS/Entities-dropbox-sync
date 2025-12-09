# RESEARCHES 2 - План разработки (Простая версия)

**Дата:** 2025-12-08
**Версия:** 2.0 (Simplified)
**Статус:** Готов к утверждению

---

## КРАТКАЯ СВОДКА

**Технологии:**
- Frontend: React.js + Tailwind CSS + shadcn/ui
- Backend: Node.js + Express.js
- Storage: Dropbox API + Google Sheets API
- No Database, No Auth, No Rate Limiting

**Единая система ID:** `{PREFIX}-{NUMBER}`
- SEARCH-XXX, VQ-XXX, VIDEO-XXX, WRF-XXX, TOL-XXX, OBJ-XXX, ACT-XXX, PRF-XXX, SKL-XXX, DPT-XXX

**Data Flow:**
```
Frontend (React) → Express API → Google Sheets (data) + Dropbox (files)
```

---

## ЭТАПЫ РАЗРАБОТКИ

### **ЭТАП 0: АРХИТЕКТУРА** (Документация)
- Описание системы и модулей
- Единая система ID
- Google Sheets структура (4 листа)
- Dropbox структура
- **Время:** Документация

---

### **ЭТАП 1: ИНФРАСТРУКТУРА** (6-9 часов)

**1.1 Настройка окружения:**
- Backend: Node.js + Express
- Frontend: React + Tailwind + shadcn/ui
- Установка зависимостей

**1.2 Структура проекта:**
```
researches-app/
├── server/          # Express backend
│   ├── routes/
│   ├── services/
│   └── config/
└── client/          # React frontend
    ├── components/
    ├── pages/
    └── services/
```

**1.3 API Credentials:**
- Dropbox Access Token
- Google Sheets credentials.json
- YouTube API Key
- OpenAI/Claude API Keys (optional)

**1.4 Базовый сервер Express**

---

### **ЭТАП 2: CORE SERVICES** (11-14 часов)

**2.1 ID Generator Service** (3-4 ч)
- Генерация SEARCH-XXX, VQ-XXX, VIDEO-XXX
- Генерация entity IDs (WRF, TOL, OBJ, etc.)
- Сканирование Google Sheets + Dropbox

**2.2 Google Sheets Service** (4-5 ч)
- CRUD для Search_Queue_Master
- CRUD для Video_Queue_Master
- CRUD для Video_Progress_Tracker
- CRUD для Integration_Log

**2.3 Dropbox Service** (4-5 ч)
- Read/Write файлов
- List directories
- Управление transcriptions
- Управление JSON entities

---

### **ЭТАП 3: VIDEO QUEUE** (18-22 часа)

**3.1 Backend** (8-10 ч)
- API endpoints (GET, POST, PUT, DELETE)
- YouTube metadata extraction
- Priority calculator (0-100 баллов)
- Integration с Google Sheets

**3.2 Frontend** (10-12 ч)
- Video Queue Dashboard (shadcn/ui Table)
- Add Video Form
- Priority Badge, Status Badge
- Filters & Sorting
- Stats panel

---

### **ЭТАП 4: TRANSCRIPTIONS** (25-30 часов)

**4.1 Backend** (10-12 ч)
- API endpoints
- AI service (OpenAI/Claude integration)
- Entity extraction (37+ entities)
- Dropbox integration
- Validation

**4.2 Frontend** (15-18 ч)
- Transcription Editor (markdown with preview)
- Entity List (7 types visualization)
- Validation Panel
- AI-assisted processing
- Save to Dropbox

---

### **ЭТАП 5: ANALYSIS** (30-35 часов)

**5.1 Phase 2: Extraction** (8-10 ч)
- Backend: Deep entity extraction
- AI integration (PMT-007 prompt)
- Generate analysis reports

**5.2 Phase 3: Gap Analysis** (10-12 ч)
- Backend: Compare with LIBRARIES
- Categorize: NEW/EXISTING/UPDATE
- Calculate coverage metrics

**5.3 Phase 5: Mapping** (8-10 ч)
- Backend: Generate comprehensive report
- Business value calculation
- Cross-reference map

**5.4 Frontend** (4-6 ч)
- Analysis Dashboard
- Results visualization (charts, tables)
- Export reports

---

### **ЭТАП 6: INTEGRATION** (25-30 часов)

**6.1 Backend** (15-18 ч)
- JSON Creator (templates for 7 entity types)
- JSON Updater
- Schema Validator
- Cross-reference Manager
- Integration Logger

**6.2 Frontend** (10-12 ч)
- JSON Creation Wizard (step-by-step)
- Entity Form
- JSON Preview/Editor
- Validation Panel
- Integration Log view

---

### **ЭТАП 7: TAXONOMY** (20-25 часов)

**7.1 Backend** (8-10 ч)
- List all entities by type
- Search/Filter entities
- Get entity by ID
- Relationship queries

**7.2 Frontend** (12-15 ч)
- Taxonomy Explorer
- Entity Viewer (detailed view)
- Search Panel
- Hierarchy Tree
- Relationship Graph (D3.js/vis.js)

---

### **ЭТАП 8: DASHBOARD & PROGRESS** (20-25 часов)

**8.1 Backend** (8-10 ч)
- Progress Tracker API
- Statistics API
- Reports Generator

**8.2 Frontend** (12-15 ч)
- Main Dashboard
  - Overall stats
  - Phase distribution chart
  - Recent activity feed
  - Employee performance
- Process Monitor
- Progress Timeline
- Reports Panel

---

### **ЭТАП 9: SEARCH QUEUE** (12-15 часов)

**9.1 Backend** (5-6 ч)
- API endpoints для SEARCH operations
- Integration с Google Sheets

**9.2 Frontend** (7-9 ч)
- Search Queue Dashboard
- Assign Search Form
- Complete Search Form
- Stats view

---

### **ЭТАП 10: ТЕСТИРОВАНИЕ & ДЕПЛОЙ** (20-25 часов)

**10.1 Тестирование** (10-12 ч)
- Unit tests (Backend)
- Component tests (Frontend)
- Integration tests
- E2E tests (Playwright/Cypress)

**10.2 Документация** (5-6 ч)
- API documentation
- User guide
- Developer guide

**10.3 Деплой** (5-7 ч)
- Docker setup
- CI/CD (GitHub Actions)
- Production deployment (Vercel/Heroku)

---

## ОБЩАЯ ОЦЕНКА ВРЕМЕНИ

| Этап | Название | Часы |
|------|----------|------|
| 0 | Архитектура | Документация |
| 1 | Инфраструктура | 6-9 |
| 2 | Core Services | 11-14 |
| 3 | Video Queue | 18-22 |
| 4 | Transcriptions | 25-30 |
| 5 | Analysis | 30-35 |
| 6 | Integration | 25-30 |
| 7 | Taxonomy | 20-25 |
| 8 | Dashboard | 20-25 |
| 9 | Search Queue | 12-15 |
| 10 | Тестирование & Деплой | 20-25 |
| **ИТОГО** | | **187-230 часов** |

**Или 24-29 рабочих дней** (при 8 часах/день)

---

## КРИТИЧЕСКИЙ ПУТЬ (MVP)

**Phase 1 (Минимальный функционал):**
1. Этап 1: Инфраструктура ✓
2. Этап 2: Core Services ✓
3. Этап 3: Video Queue
4. Этап 8: Basic Dashboard

**Phase 2 (Основной workflow):**
5. Этап 4: Transcriptions
6. Этап 5: Analysis
7. Этап 6: Integration

**Phase 3 (Дополнительно):**
8. Этап 7: Taxonomy Explorer
9. Этап 9: Search Queue

**Phase 4 (Финализация):**
10. Этап 10: Testing & Deploy

---

## КЛЮЧЕВЫЕ ТЕХНИЧЕСКИЕ РЕШЕНИЯ

### Backend Services (Node.js)

**1. ID Generator**
```javascript
// Unified ID generation
async generateSearchID()  → SEARCH-001
async generateVQID()      → VQ-042
async generateVideoID()   → VIDEO-028
async generateEntityID(type) → WRF-412, TOL-342
```

**2. Google Sheets Service**
```javascript
// CRUD operations for 4 sheets
getSearchQueue()
addSearchTask(task)
getVideoQueue()
addVideoToQueue(video)
getVideoProgress()
updateVideoProgress(videoNum, phase)
```

**3. Dropbox Service**
```javascript
// File operations
listFiles(path)
readFile(path)
writeFile(path, content)
getTranscription(videoNumber)
saveTranscription(videoNumber, content)
getEntity(type, id)
saveEntity(type, id, data)
```

**4. AI Service**
```javascript
// AI integration
processWithOpenAI(prompt, content)
processWithClaude(prompt, content)
extractEntities(transcription)
```

**5. Priority Calculator**
```javascript
// Video priority (0-100)
calculatePriority(video) {
  date_score * 0.30 +
  source_score * 0.25 +
  topic_score * 0.25 +
  engagement * 0.20
}
```

### Frontend Components (React + Tailwind + shadcn/ui)

**Key Components:**
```
<VideoQueueDashboard />
<TranscriptionEditor />
<AnalysisDashboard />
<IntegrationWizard />
<TaxonomyExplorer />
<MainDashboard />
```

**shadcn/ui компоненты:**
- Table (sortable, filterable)
- Form + Input fields
- Card, Badge, Button
- Dialog, Sheet (modals, sidebars)
- Chart components (for dashboards)
- Tabs, Accordion

---

## API ENDPOINTS

### Video Queue
```
GET    /api/video-queue
POST   /api/video-queue
PUT    /api/video-queue/:id
DELETE /api/video-queue/:id
PUT    /api/video-queue/:id/priority
```

### Transcriptions
```
GET    /api/transcriptions
GET    /api/transcriptions/:id
POST   /api/transcriptions
PUT    /api/transcriptions/:id
POST   /api/transcriptions/:id/process
```

### Analysis
```
POST   /api/analysis/:id/extract
POST   /api/analysis/:id/gap
POST   /api/analysis/:id/mapping
GET    /api/analysis/:id/results
```

### Integration
```
POST   /api/integration/:id/create-json
GET    /api/integration/log
POST   /api/integration/validate
```

### Taxonomy
```
GET    /api/taxonomy/entities
GET    /api/taxonomy/entities/:type
GET    /api/taxonomy/entities/:type/:id
POST   /api/taxonomy/search
GET    /api/taxonomy/relationships/:id
```

### Progress
```
GET    /api/progress
GET    /api/progress/:id
PUT    /api/progress/:id
GET    /api/progress/stats
```

### Search Queue
```
GET    /api/search-queue
POST   /api/search-queue
PUT    /api/search-queue/:id/complete
```

---

## СЛЕДУЮЩИЕ ШАГИ

1. ✅ Утвердить план
2. ⬜ Создать репозиторий GitHub
3. ⬜ Настроить окружение разработки (Этап 1)
4. ⬜ Получить API credentials (Dropbox, Google Sheets, YouTube)
5. ⬜ Реализовать Core Services (Этап 2)
6. ⬜ Начать разработку Video Queue (Этап 3)

---

**План готов к выполнению!**
