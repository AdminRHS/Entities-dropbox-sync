# БЫСТРОЕ РУКОВОДСТВО ПО ЗАПУСКУ RESEARCHES 2

**Дата:** 2025-12-08
**Версия:** 1.0
**Для:** 1 разработчик + AI

---

## 🎯 ЧТО ЭТО?

**RESEARCHES 2** - веб-приложение на React для автоматизированной обработки YouTube видео и интеграции знаний в таксономию ENTITIES.

**Цель v1.0:** MVP с 90% автоматизацией за 25-26 недель (~6 месяцев)

---

## 📋 ПОДТВЕРЖДЕННЫЕ ТРЕБОВАНИЯ

### Платформа
- ✅ React Web App (responsive: 320px-1440px+)
- ✅ Dark/Light mode
- ✅ Design System: https://adminrhs.github.io/Design-system/
- ❌ Desktop/Mobile native apps (не планируется)

### Технологии
- **Frontend:** React 18 + TypeScript + Tailwind CSS + shadcn/ui
- **Backend:** Node.js + Express + PostgreSQL + Redis
- **APIs:** Dropbox API + YouTube API + Claude/OpenAI API
- **Deploy:** Локально (Docker) → AWS позже

### Пользователи
- ✅ Неограниченное количество
- ✅ JWT авторизация
- ✅ Роли: Admin, Researcher, Manager, Viewer
- ❌ Collaboration (не в v1.0)

### Автоматизация
- ✅ 90%+ (сейчас 70%)
- ✅ Phase 2 automation - КРИТИЧНО
- ✅ YouTube API - полная интеграция

---

## 📅 TIMELINE (6 МЕСЯЦЕВ)

| Фаза | Недели | Что делаем |
|------|--------|------------|
| **Phase 0** | 1 | Промпты + планирование |
| **Phase 1** | 5 | Infrastructure (Docker, DB, API) |
| **Phase 2** | 3 | Search Queue + Video Queue |
| **Phase 3** | 4 | Video Processing (7 фаз) |
| **Phase 4** | 3 | Entities Management |
| **Phase 5** | 3 | Progress Tracking + Dashboards |
| **Phase 6** | 2 | Testing + Bug Fixes |
| **Buffer** | 4-5 | Отладка |
| **ИТОГО** | 25-26 | MVP Ready |

---

## 🚀 С ЧЕГО НАЧАТЬ?

### ШАГ 1: Phase 0 - Промпты (Неделя 1)

**Дни 1-2:** Архитектурные диаграммы
- System Architecture
- Component relationships
- Database schema (ER diagram)
- Data flow diagrams

**Дни 2-3:** Database schemas
- SQL CREATE TABLE statements
- Migrations
- Seeds

**День 3:** API endpoints
- Express.js routes
- OpenAPI specs
- Request/Response examples

**Дни 4-5:** Frontend components
- React TypeScript components
- Props, state, methods
- Material-UI/shadcn/ui setup

**Дни 5-7:** Processing workflows
- Phase 1-5 промпты
- AI orchestration
- Dropbox integration

**Результат:** 50+ готовых промптов для AI-assisted разработки

### ШАГ 2: Phase 1 - Infrastructure (Недели 2-6)

**Неделя 1-2:**
```bash
# Setup project
mkdir researches-app && cd researches-app
npx create-nx-workspace@latest --preset=react-express

# Setup Docker
docker-compose up -d postgres redis
```

**Неделя 2-3:**
- PostgreSQL схемы
- Prisma ORM
- JWT authentication
- Core API routes

**Неделя 3-4:**
- Dropbox API integration
- YouTube API integration
- AI service (Claude/OpenAI)

**Неделя 4-5:**
- React frontend setup
- Tailwind CSS + Design System
- shadcn/ui components
- Dark mode toggle

### ШАГ 3: Phase 2 - Search & Queue (Недели 7-9)

**Создать:**
- Search Queue Dashboard
- Video Queue Dashboard
- Priority Calculator (0-100)
- YouTube metadata extraction
- Search Results Modal (ключевой компонент!)

### ШАГ 4: Phase 3 - Video Processing (Недели 10-13)

**Автоматизировать:**
- Phase 1: Transcription (PMT-004)
- Phase 2: Extraction (PMT-007) - **КРИТИЧНО**
- Phase 3: Gap Analysis
- Phase 4: Integration
- Phase 5: Mapping & Reports

### ШАГ 5: Phase 4-6 - Entities, Tracking, Testing (Недели 14-21)

**Завершить:**
- Entities Browser
- Main Dashboard
- Progress Monitoring
- Reports Generator
- Unit tests (80%+ coverage)
- Bug fixes

---

## 🎯 КРИТИЧЕСКИЕ ЗАДАЧИ (MUST-HAVE для v1.0)

### ⚠️ ISS-RES-005: Phase 2 Automation
**Проблема:** Phase 2 не автоматизирован, 30-45 мин ручной работы
**Решение:** Создать `video_extraction_automator.py`
**Эффект:** 30-45 мин → 2-3 мин (90% автоматизация)
**Приоритет:** КРИТИЧНЫЙ

### ⚠️ ISS-RES-001: Progress Tracker Sync
**Проблема:** 22 видео показывают "Phase_1", но на самом деле "Complete"
**Решение:** Batch update script
**Эффект:** Корректное отслеживание прогресса
**Приоритет:** ВЫСОКИЙ

### ⚠️ ISS-RES-004: Missing Progress Dashboard
**Проблема:** Нет главного dashboard (есть только queue dashboard)
**Решение:** Создать Main Dashboard с real-time метриками
**Эффект:** Видимость всей системы
**Приоритет:** ВЫСОКИЙ

### ⚠️ ISS-RES-010: No Unit Tests
**Проблема:** Нет автотестов для 16 скриптов
**Решение:** Создать tests/ с pytest + Jest
**Эффект:** Защита от регрессий
**Приоритет:** ВЫСОКИЙ

---

## 📦 БЫСТРАЯ УСТАНОВКА

### Prerequisites
```bash
# Check versions
node --version   # v18+
npm --version
docker --version
git --version
python --version # 3.10+
```

### Setup Backend
```bash
cd server
npm install
cp .env.example .env
# Edit .env with your API keys
npm run db:migrate
npm run db:seed
npm run dev
```

### Setup Frontend
```bash
cd client
npm install
cp .env.example .env
npm run dev
```

### Open Browser
```
http://localhost:3000
```

---

## 🔑 НЕОБХОДИМЫЕ API KEYS

Создайте `.env` файлы:

**Backend `.env`:**
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/researches2
REDIS_URL=redis://localhost:6379

# Dropbox
DROPBOX_ACCESS_TOKEN=your_dropbox_token

# YouTube
YOUTUBE_API_KEY=your_youtube_key

# AI
CLAUDE_API_KEY=your_claude_key
OPENAI_API_KEY=your_openai_key

# Auth
JWT_SECRET=your_secret_key
```

**Frontend `.env`:**
```env
VITE_API_URL=http://localhost:3001/api
```

---

## 📚 ДОКУМЕНТАЦИЯ

### Основные документы
1. **RESEARCHES-2-FULL-DEVELOPMENT-PLAN-v1.0-RU.md** - Полный план (этот документ)
2. **FULL-APP-GENERATION-PROMPT.md** - Промпт для генерации UI
3. **design-system-analysis.md** - Анализ дизайн-системы

### Референсы
- **Design System:** https://adminrhs.github.io/Design-system/
- **Video Catalog:** https://adminrhs.github.io/Video-catalog/
- **Plan файл:** `C:\Users\User\.claude\plans\temporal-riding-wilkes.md`

---

## 🎨 ДИЗАЙН БЫСТРЫЙ СТАРТ

### Цвета (из Design System)
```css
/* Light Theme */
--bg-default: #f7fafc;
--bg-paper: #ffffff;
--text-primary: #2d3748;
--color-primary: #2563EB;

/* Dark Theme */
--bg-default: #1a202c;
--bg-paper: #1f2937;
--text-primary: #f7fafc;
--color-primary: #3B82F6;

/* Module Colors */
--color-search: #6D28D9;    /* Designers Purple */
--color-video: #147857;     /* Developers Green */
--color-transcription: #2563EB; /* Primary Blue */
```

### Типографика
```css
--font-primary: 'Roboto', sans-serif;
--text-h1: 3rem;      /* 48px */
--text-b1: 1rem;      /* 16px */
--text-caption: 0.75rem; /* 12px */
```

### Отступы
```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
```

---

## ✅ КРИТЕРИИ ГОТОВНОСТИ v1.0

**Функционал:**
- ✅ Search Queue работает
- ✅ Video Queue с приоритетами
- ✅ 7-фазная обработка видео
- ✅ Entities management
- ✅ Progress dashboard
- ✅ Reports generator

**Качество:**
- ✅ 80%+ test coverage
- ✅ <500ms API response
- ✅ Responsive 320px-1440px+
- ✅ Dark/Light mode
- ✅ Zero P0/P1 bugs

**Автоматизация:**
- ✅ 90%+ автоматизация
- ✅ Phase 2 автоматизирован
- ✅ YouTube API интегрирован

---

## 🚨 ТИПИЧНЫЕ ПРОБЛЕМЫ

### "Docker не запускается"
```bash
# Check Docker daemon
docker ps
# If error, restart Docker Desktop
```

### "PostgreSQL connection failed"
```bash
# Check if running
docker ps | grep postgres
# Check connection string in .env
```

### "YouTube API quota exceeded"
```
Solution: Use caching (Redis) + implement rate limiting
```

### "Dropbox API 429 (rate limit)"
```
Solution: Exponential backoff retry logic implemented
```

---

## 📞 ПОМОЩЬ

**GitHub Issues:** [создать issue]
**План файл:** `C:\Users\User\.claude\plans\temporal-riding-wilkes.md`
**Документация:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\documentation\`

---

## 🎯 СЛЕДУЮЩИЕ ДЕЙСТВИЯ

1. ✅ Прочитать этот гайд
2. ⏳ Создать Phase 0 промпты (Неделя 1)
3. ⏳ Setup Docker + PostgreSQL
4. ⏳ Begin Phase 1 Infrastructure
5. ⏳ Follow 25-week plan

---

**ГОТОВ К СТАРТУ! 🚀**

*Последнее обновление: 2025-12-08*
