# Фаза 0 - Руководство по Началу Детального Проектирования

**Дата начала:** 2025-12-05
**Срок выполнения:** 2-3 недели
**Статус:** 🔴 НЕ НАЧАТО

⚠️ **КРИТИЧНО:** Разработка кода начинается ТОЛЬКО после 100% завершения Фазы 0!

---

## 🎯 Цель Фазы 0

Создать **полную техническую документацию** и **проектную документацию**, которая позволит AI-инструментам (Claude Code, Cursor, v0.dev) генерировать качественный код.

**Принцип:** "Measure twice, cut once" - тщательное планирование экономит месяцы разработки.

---

## 📋 Checklist Фазы 0 (5 Подфаз)

### Подфаза 0.1: Анализ Текущей Инфраструктуры ✅
**Статус:** Завершено (анализ 300+ страниц документации выполнен)

**Результаты:**
- ✅ Карта зависимостей между 21 Python скриптом
- ✅ Понимание 7-фазного workflow
- ✅ Анализ 752+ entities в таксономии
- ✅ Изучение 50+ AI промптов

### Подфаза 0.2: Architecture Document (C4 Model)
**Срок:** 3-4 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Level 1 - System Context Diagram**
  - Показать систему RESEARCHES 2 и ее взаимодействие с внешними системами
  - Актеры: Solo Developer, YouTube API, Dropbox API, OpenAI API, Neon DB

- [ ] **Level 2 - Container Diagram**
  - React Frontend (Vercel)
  - Express Backend (Railway)
  - PostgreSQL (Neon)
  - Redis (Upstash)
  - Job Queue (BullMQ)

- [ ] **Level 3 - Component Diagram**
  - Frontend: Pages, Components, Hooks, Services, Store
  - Backend: Routes, Services, Middleware, Utils

- [ ] **Level 4 - Code Diagram** (опционально для критических компонентов)
  - ComparisonWidget component
  - Gap Analysis algorithm
  - Cross-reference bidirectional sync

**Инструменты:**
- Diagrams.net (draw.io)
- Mermaid (для markdown-диаграм)
- Excalidraw (для быстрых скетчей)

**Сохранить в:**
- `documentation/architecture/01_C4_MODEL.md`
- `documentation/architecture/diagrams/` (PNG/SVG файлы)

---

### Подфаза 0.3: Database Schema (Prisma + ERD)
**Срок:** 2-3 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Создать Prisma Schema**
  ```prisma
  // schema.prisma
  generator client {
    provider = "prisma-client-js"
  }

  datasource db {
    provider = "postgresql"
    url      = env("DATABASE_URL")
  }

  model Video {
    id            String   @id // Video_XXX
    videoId       String   @unique
    title         String?
    channel       String?
    duration      Int?
    url           String
    queuePriority Decimal?
    currentPhase  String
    status        String
    createdAt     DateTime @default(now())
    updatedAt     DateTime @updatedAt

    entities      Entity[]
    queues        Queue[]
  }

  model Entity {
    id             String   @id
    entityType     String   // WRF, TOL, OBJ, ACT, PRF, SKL, DPT
    name           String
    category       String?
    data           Json
    sourceVideoId  String?
    createdAt      DateTime @default(now())
    updatedAt      DateTime @updatedAt

    video          Video?   @relation(fields: [sourceVideoId], references: [id])

    fromReferences CrossReference[] @relation("fromEntity")
    toReferences   CrossReference[] @relation("toEntity")
  }

  model CrossReference {
    id             Int      @id @default(autoincrement())
    fromEntityId   String
    toEntityId     String
    referenceType  String
    createdAt      DateTime @default(now())

    fromEntity     Entity   @relation("fromEntity", fields: [fromEntityId], references: [id])
    toEntity       Entity   @relation("toEntity", fields: [toEntityId], references: [id])

    @@unique([fromEntityId, toEntityId, referenceType])
  }

  // ... остальные модели (Queue, Issue, Task)
  ```

- [ ] **Создать ERD диаграмму**
  - Использовать dbdiagram.io или Prisma Studio
  - Показать все relationships (1:M, M:M)
  - Указать indexes

- [ ] **Написать Initial Migration**
  ```bash
  npx prisma migrate dev --name init
  ```

- [ ] **Создать Seed Data**
  ```typescript
  // prisma/seed.ts
  import { PrismaClient } from '@prisma/client'

  const prisma = new PrismaClient()

  async function main() {
    // Create test video
    await prisma.video.create({
      data: {
        id: 'Video_001',
        videoId: 'dQw4w9WgXcQ',
        title: 'Test Video',
        // ...
      }
    })
  }
  ```

**Сохранить в:**
- `backend/prisma/schema.prisma`
- `documentation/database/ERD.png`
- `documentation/database/DATABASE_DESIGN.md`

---

### Подфаза 0.4: API Specification (OpenAPI/Swagger)
**Срок:** 3-4 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Создать OpenAPI 3.0 спецификацию**
  ```yaml
  openapi: 3.0.0
  info:
    title: RESEARCHES 2 API
    version: 1.0.0
    description: API для автоматизации обработки видео

  servers:
    - url: http://localhost:3000/api/v1
      description: Development
    - url: https://api.researches2.com/api/v1
      description: Production

  paths:
    /videos:
      get:
        summary: Get all videos
        tags: [Videos]
        parameters:
          - name: phase
            in: query
            schema:
              type: string
          - name: status
            in: query
            schema:
              type: string
        responses:
          200:
            description: Success
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    data:
                      type: array
                      items:
                        $ref: '#/components/schemas/Video'

      post:
        summary: Create video
        tags: [Videos]
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateVideoDto'
        responses:
          201:
            description: Created

  components:
    schemas:
      Video:
        type: object
        properties:
          id:
            type: string
            example: Video_001
          videoId:
            type: string
          title:
            type: string
          # ...
  ```

- [ ] **Документировать все 20+ endpoints**
  - `/api/v1/videos` (7 endpoints)
  - `/api/v1/taxonomy` (6 endpoints)
  - `/api/v1/queue` (4 endpoints)
  - `/api/v1/dashboard` (3 endpoints)
  - `/api/v1/issues` (3 endpoints)

- [ ] **Добавить примеры Request/Response**
- [ ] **Описать Error codes**
- [ ] **Добавить Authentication схему**

**Инструменты:**
- Swagger Editor (editor.swagger.io)
- Stoplight Studio

**Сохранить в:**
- `backend/openapi.yaml`
- `documentation/api/API_SPECIFICATION.md`

---

### Подфаза 0.5: UI/UX Design (Figma Prototypes)
**Срок:** 4-5 дней
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Создать Design System**
  - Colors (primary, secondary, accent)
  - Typography (headings, body, code)
  - Spacing (4px, 8px, 16px, 24px, 32px)
  - Components library (из ShadCN UI)

- [ ] **Спроектировать основные страницы:**

  **1. Dashboard Page**
  - Overview stats (total videos, automation level)
  - Phase distribution chart
  - Employee stats
  - Tool stats
  - Quality metrics

  **2. Video Queue Page**
  - Video cards с thumbnails
  - Priority indicators (color-coded)
  - Batch selection checkboxes
  - Filters (phase, status, employee)
  - Queue statistics sidebar

  **3. Video Processing Page**
  - Stepper (7 phases)
  - Phase-specific content area
  - Action buttons (Start Transcription, etc.)
  - Progress indicators
  - Entity preview table

  **4. Taxonomy Editor Page**
  - Entity list (TanStack Table)
  - Entity type tabs (WRF, TOL, OBJ, etc.)
  - Entity form modal
  - ComparisonWidget для merge
  - Cross-reference graph viewer

  **5. Search Queue Page**
  - Search assignment form
  - Employee selector
  - Topic autocomplete
  - Priority slider
  - Status workflow

- [ ] **Создать Reusable Components**
  - **ComparisonWidget** (критический компонент!)
    - Side-by-side view
    - Overlay view
    - Table view
    - Selection controls
  - EntityCard
  - VideoCard
  - StatWidget
  - PriorityBadge
  - PhaseIndicator

**Инструменты:**
- Figma (основной инструмент)
- ShadCN UI docs (для референса компонентов)
- v0.dev (для быстрого прототипирования)

**Сохранить в:**
- Figma project: "RESEARCHES 2 UI/UX"
- Export в `documentation/ui-ux/figma-exports/`
- `documentation/ui-ux/UI_UX_DESIGN.md`

---

### Подфаза 0.6: Pseudo-Code для Всех Модулей
**Срок:** 3-4 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Frontend Components Pseudo-Code**
  ```typescript
  // ComparisonWidget.tsx pseudo-code
  interface ComparisonWidgetProps {
    items: Array<{id: string, label: string, data: any}>
    onSelect: (id: string) => void
    renderItem: (item: any) => ReactNode
    compareMode: 'side-by-side' | 'overlay' | 'table'
  }

  function ComparisonWidget(props) {
    // State
    const [selectedId, setSelectedId] = useState(null)
    const [viewMode, setViewMode] = useState(props.compareMode)

    // Handlers
    const handleSelect = (id) => {
      setSelectedId(id)
      props.onSelect(id)
    }

    // Render
    return (
      <div className="comparison-widget">
        <ViewModeToggle />
        {viewMode === 'side-by-side' && <SideBySideView />}
        {viewMode === 'overlay' && <OverlayView />}
        {viewMode === 'table' && <TableView />}
        <SelectionControls />
      </div>
    )
  }
  ```

- [ ] **Backend Services Pseudo-Code**
  ```typescript
  // video.service.ts pseudo-code
  class VideoService {
    // Phase 0→1: Add to queue
    async addToQueue(videoUrl: string) {
      // 1. Fetch YouTube metadata
      const metadata = await youtubeApi.getVideoInfo(videoUrl)

      // 2. Calculate priority
      const priority = this.calculatePriority(metadata)

      // 3. Generate ID
      const videoId = await this.generateVideoId()

      // 4. Create in database
      const video = await prisma.video.create({
        data: { id: videoId, ...metadata, priority }
      })

      // 5. Sync to Dropbox
      await dropboxService.syncVideoQueue()

      return video
    }

    // Phase 1: Transcription
    async transcribe(videoId: string) {
      // 1. Load video
      const video = await prisma.video.findUnique({where: {id: videoId}})

      // 2. Load PMT-004 prompt
      const prompt = await promptService.load('PMT-004')

      // 3. Call AI
      const transcript = await aiService.call(prompt, {videoUrl: video.url})

      // 4. Parse entities
      const entities = await this.parseTranscript(transcript)

      // 5. Save markdown
      await fs.writeFile(`02_TRANSCRIPTIONS/${videoId}.md`, transcript)

      // 6. Update video phase
      await prisma.video.update({
        where: {id: videoId},
        data: {currentPhase: 'Phase_1', status: 'transcribed'}
      })

      return {transcript, entities}
    }

    // ... остальные методы для Phase 2-5
  }
  ```

- [ ] **Критические Алгоритмы**
  - Gap Analysis (fuzzy matching)
  - Cross-reference bidirectional sync
  - Priority calculation
  - Entity deduplication
  - Quality score calculation

**Сохранить в:**
- `documentation/pseudo-code/FRONTEND_PSEUDO_CODE.md`
- `documentation/pseudo-code/BACKEND_PSEUDO_CODE.md`
- `documentation/pseudo-code/ALGORITHMS_PSEUDO_CODE.md`

---

### Подфаза 0.7: AI-генерация Промптов
**Срок:** 2-3 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Создать промпты для Claude Code**
  ```markdown
  # Prompt: Generate Video Service

  ## Context
  You are generating a backend service for the RESEARCHES 2 application.

  ## Requirements
  - Tech Stack: Node.js 20+, Express.js, Prisma, TypeScript
  - Database: PostgreSQL (Neon)
  - Must implement 7-phase video processing workflow

  ## Architecture
  [Attach: C4 diagrams, Database ERD, API spec]

  ## Pseudo-Code
  [Attach: video.service pseudo-code]

  ## Task
  Generate complete video.service.ts with:
  1. All CRUD operations
  2. Phase transition logic
  3. YouTube API integration
  4. Dropbox sync integration
  5. Error handling
  6. TypeScript types
  7. JSDoc comments

  ## Output Format
  - Single file: backend/src/services/video.service.ts
  - Follow Prisma best practices
  - Use async/await
  - Include error handling
  ```

- [ ] **Промпты для v0.dev (UI components)**
  ```markdown
  # Prompt: Generate ComparisonWidget Component

  ## Context
  React 19+ component using ShadCN UI and Tailwind CSS v4

  ## Requirements
  - Props: items[], onSelect, renderItem, compareMode
  - Three view modes: side-by-side, overlay, table
  - TypeScript
  - Responsive design
  - Accessibility (ARIA labels)

  ## Design
  [Attach: Figma screenshot]

  ## Task
  Generate ComparisonWidget.tsx with all three view modes
  ```

- [ ] **Промпты для Cursor (features)**
- [ ] **Промпты для полных модулей**

**Сохранить в:**
- `documentation/ai-prompts/CLAUDE_CODE_PROMPTS.md`
- `documentation/ai-prompts/V0_DEV_PROMPTS.md`
- `documentation/ai-prompts/CURSOR_PROMPTS.md`

---

### Подфаза 0.8: Tech Stack Setup
**Срок:** 2-3 дня
**Статус:** ⏳ К ВЫПОЛНЕНИЮ

**Задачи:**
- [ ] **Создать GitHub Repository (корпоративный)**
  ```bash
  # Repository structure
  researches-2-app/
  ├── frontend/
  │   ├── src/
  │   ├── package.json
  │   └── vite.config.ts
  ├── backend/
  │   ├── src/
  │   ├── prisma/
  │   ├── package.json
  │   └── tsconfig.json
  ├── docs/
  └── README.md
  ```

- [ ] **Setup Vercel Project**
  - Link GitHub repo
  - Configure environment variables
  - Setup preview deployments

- [ ] **Setup Railway Project**
  - Link GitHub repo
  - Provision PostgreSQL (или link Neon)
  - Provision Redis
  - Configure environment variables

- [ ] **Setup Neon Database**
  - Create project
  - Get connection string
  - Setup prisma connection

- [ ] **Setup Upstash Redis**
  - Create database
  - Get connection string
  - Configure BullMQ

- [ ] **Configure Environment Variables**
  ```env
  # .env.example
  # Database
  DATABASE_URL="postgresql://..."
  REDIS_URL="redis://..."

  # APIs
  DROPBOX_ACCESS_TOKEN="..."
  OPENAI_API_KEY="..."
  YOUTUBE_API_KEY="..."

  # Auth
  JWT_SECRET="..."

  # App
  NODE_ENV="development"
  PORT=3000
  ```

**Сохранить в:**
- GitHub repo: `your-org/researches-2-app`
- `documentation/setup/INFRASTRUCTURE_SETUP.md`

---

## 📊 Deliverables Summary

После завершения Фазы 0 у вас будет:

### Документация (7 документов)
- ✅ Architecture (C4 model) - `documentation/architecture/`
- ✅ Database Design (ERD + Prisma) - `documentation/database/`
- ✅ API Specification (OpenAPI) - `backend/openapi.yaml`
- ✅ UI/UX Design (Figma) - `documentation/ui-ux/`
- ✅ Pseudo-Code (Frontend + Backend) - `documentation/pseudo-code/`
- ✅ AI Prompts - `documentation/ai-prompts/`
- ✅ Infrastructure Setup - `documentation/setup/`

### Готовность к разработке
- ✅ GitHub repo с правильной структурой
- ✅ Vercel project (frontend hosting)
- ✅ Railway project (backend hosting)
- ✅ Neon database (PostgreSQL)
- ✅ Upstash Redis (queue)
- ✅ Environment variables настроены

### AI-Ready
- ✅ Промпты готовы для Claude Code
- ✅ Промпты готовы для v0.dev
- ✅ Промпты готовы для Cursor
- ✅ Pseudo-code для всех компонентов

---

## 🚀 Переход к Фазе 1 (Разработка)

**Критерии готовности:**
- [ ] Все deliverables Фазы 0 завершены
- [ ] Документация проверена и утверждена
- [ ] Infrastructure настроена и протестирована
- [ ] AI промпты подготовлены
- [ ] Команда готова к разработке

**После завершения Фазы 0:**
1. ✅ Review всей документации
2. ✅ Получить финальное утверждение
3. 🚀 **НАЧАТЬ AI-ГЕНЕРАЦИЮ КОДА** (Фаза 1)

---

## 💡 Советы для Фазы 0

**Для Solo Developer:**
1. **Не спешите** - качественная Фаза 0 экономит месяцы разработки
2. **Используйте AI** для генерации диаграм и документации
3. **Проверяйте дважды** - ошибки в архитектуре дорого исправлять потом
4. **Делайте итерации** - показывайте прогресс руководству каждые 2-3 дня
5. **Документируйте решения** - почему выбрали именно так

**Инструменты, которые помогут:**
- Claude Code - для генерации документации
- Cursor - для генерации кода примеров
- v0.dev - для прототипирования UI
- Figma - для дизайна
- dbdiagram.io - для ERD
- Swagger Editor - для API spec

---

**Дата создания:** 2025-12-05
**Автор:** Claude Code Agent
**Статус:** 📘 READY FOR EXECUTION
