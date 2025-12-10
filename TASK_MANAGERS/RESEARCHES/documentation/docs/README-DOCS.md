# RESEARCHES 2 - ДОКУМЕНТАЦИЯ

**Создано:** 2025-12-08
**Версия:** 1.0
**Статус:** Production Ready Documentation

---

## 📁 СТРУКТУРА ДОКУМЕНТАЦИИ

```
docs/
├── README-DOCS.md (этот файл)
├── ARCHITECTURE-DECISION-DROPBOX-VS-DATABASE.md    ⭐ АРХИТЕКТУРНОЕ РЕШЕНИЕ
├── SEARCH-VIDEO-QUEUE-FUNCTIONAL-REQUIREMENTS.md   ⭐ ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ
├── RESEARCHES-2-FULL-DEVELOPMENT-PLAN-v1.0-RU.md   ⭐ ГЛАВНЫЙ ПЛАН
├── QUICK-START-GUIDE-RU.md                          ⭐ БЫСТРЫЙ СТАРТ
├── RESEARCHES-2-Development-Plan-Full.md
├── RESEARCHES-2-Development-Plan-Summary.md
├── SEARCH-QUEUE-VIDEO-QUEUE-DETAILED-PLAN.md
├── prompts/
│   └── app/
│       ├── COMPLETE-APP-GENERATION-PROMPT_1.md     ⭐ ГЛАВНЫЙ ПРОМПТ (v3.1 - Dropbox API)
│       └── COMPLETE-APP-GENERATION-PROMPT.md       (v2.0 - Database, архив)
└── steps/
    └── (пошаговые инструкции)
```

---

## 🎯 С ЧЕГО НАЧАТЬ?

### Для быстрого старта:
1. 🏗️ **Архитектура:** [ARCHITECTURE-DECISION-DROPBOX-VS-DATABASE.md](./ARCHITECTURE-DECISION-DROPBOX-VS-DATABASE.md) - **ВАЖНО!**
2. 📖 **Прочитать:** [QUICK-START-GUIDE-RU.md](./QUICK-START-GUIDE-RU.md)
3. 📋 **Изучить:** [RESEARCHES-2-FULL-DEVELOPMENT-PLAN-v1.0-RU.md](./RESEARCHES-2-FULL-DEVELOPMENT-PLAN-v1.0-RU.md)
4. 🎯 **Функционал:** [SEARCH-VIDEO-QUEUE-FUNCTIONAL-REQUIREMENTS.md](./SEARCH-VIDEO-QUEUE-FUNCTIONAL-REQUIREMENTS.md)
5. 🎨 **Генерация приложения:** [prompts/app/COMPLETE-APP-GENERATION-PROMPT_1.md](./prompts/app/COMPLETE-APP-GENERATION-PROMPT_1.md) **(v3.1 - Dropbox API)**

### Для детального понимания:
1. Архитектура системы → FULL-DEVELOPMENT-PLAN раздел "Архитектура"
2. 9 фаз разработки → FULL-DEVELOPMENT-PLAN раздел "План разработки"
3. Дизайн-система → prompts/design-system-analysis.md

---

## 📚 ОСНОВНЫЕ ДОКУМЕНТЫ

### 1. ARCHITECTURE-DECISION-DROPBOX-VS-DATABASE.md ⭐ **ВАЖНО!**
**Назначение:** Анализ и рекомендация по выбору архитектуры
**Разделы:**
- Сравнение Database (PostgreSQL) vs Dropbox API
- Анализ текущей системы (CSV/JSON files)
- Производительность и стоимость
- Сложность разработки и деплоя
- **Рекомендация: Использовать Dropbox API (v3.1)**

**Использовать для:**
- Понимания архитектурного решения
- Выбора между v2.0 (Database) и v3.1 (Dropbox)
- Обоснования технических решений

**Итоговое решение:** ✅ **Использовать v3.1 (Dropbox API)** - дешевле, проще, работает с существующими файлами

### 2. SEARCH-VIDEO-QUEUE-FUNCTIONAL-REQUIREMENTS.md ⭐
**Назначение:** Полный список функционала для Search Queue и Video Queue
**Разделы:**
- Search Queue: 8 разделов функционала (создание задач, поиск, метрики)
- Video Queue: 13 разделов функционала (добавление, приоритизация, статусы)
- Processing Workflow (7 фаз)
- Automation & Intelligence (90% автоматизация)
- Known Issues (ISS-RES-001 to ISS-RES-010)

**Использовать для:**
- Понимания полного функционала системы
- Создания технического задания
- Планирования разработки

### 3. RESEARCHES-2-FULL-DEVELOPMENT-PLAN-v1.0-RU.md ⭐
**Назначение:** Полный план разработки приложения
**Разделы:**
- Обзор проекта
- Подтвержденные требования (от 2025-12-08)
- Технологический стек
- Архитектура системы
- 9 фаз разработки (детально)
- Timeline (25-26 недель)
- Критические файлы
- Риски и митигация

**Использовать для:**
- Планирования всего проекта
- Понимания архитектуры
- Оценки сроков
- Распределения задач

### 2. QUICK-START-GUIDE-RU.md ⭐
**Назначение:** Быстрое руководство по запуску
**Разделы:**
- Что это?
- Подтвержденные требования
- Timeline (6 месяцев)
- С чего начать (пошагово)
- Критические задачи
- Быстрая установка
- API keys
- Типичные проблемы

**Использовать для:**
- Быстрого старта разработки
- Setup environment
- Первых шагов в Phase 0
- Troubleshooting

### 5. prompts/app/COMPLETE-APP-GENERATION-PROMPT_1.md ⭐ **ИСПОЛЬЗУЙТЕ ЭТОТ!**
**Назначение:** Полный промпт для генерации приложения (Backend + Frontend)
**Версия:** 3.1 (Dropbox API - БЕЗ БАЗЫ ДАННЫХ)
**Разделы:**
- Полная дизайн-система (Game Academy Design System v1.0)
- Technology Stack (React 19 + Express.js + Dropbox API)
- Backend: Express.js с Dropbox Service (читает/пишет CSV/JSON)
- Frontend: React + Vite + shadcn/ui + Tailwind v4
- Search Queue Module (полный функционал)
- Video Queue Module (с приоритизацией)
- Priority Calculation Algorithm
- Deployment (Vercel/Railway)

**Использовать для:**
- Генерации полного приложения (Backend + Frontend)
- Понимания архитектуры Dropbox API
- Создания Express.js API endpoints
- Создания React компонентов с дизайн-системой

**ВАЖНО:** Эта версия использует Dropbox API вместо PostgreSQL. Файлы CSV/JSON остаются в Dropbox, backend читает их через Dropbox SDK.

### 4. prompts/design-system-analysis.md
**Назначение:** Детальный анализ дизайн-системы
**Использовать для:**
- Понимания Design System https://adminrhs.github.io/Design-system/
- CSS variables
- Component styling guidelines

---

## 🗺️ КАРТА ДОКУМЕНТОВ ПО ФАЗАМ

### Phase 0: Промпты и планирование (Неделя 1)
📖 Читать:
- QUICK-START-GUIDE-RU.md (раздел "Phase 0")
- FULL-DEVELOPMENT-PLAN раздел "ФАЗА 0"

### Phase 1: Infrastructure (Недели 2-6)
📖 Читать:
- FULL-DEVELOPMENT-PLAN раздел "ФАЗА 1"
- QUICK-START-GUIDE раздел "ШАГ 2"

### Phase 2: Search & Queue (Недели 7-9)
📖 Читать:
- FULL-DEVELOPMENT-PLAN раздел "ФАЗА 2"
- SEARCH-QUEUE-VIDEO-QUEUE-DETAILED-PLAN.md
- FULL-APP-GENERATION-PROMPT раздел "Search Queue Module"

### Phase 3: Video Processing (Недели 10-13)
📖 Читать:
- FULL-DEVELOPMENT-PLAN раздел "ФАЗА 3"
- FULL-APP-GENERATION-PROMPT раздел "Video Queue Module"

### Phase 4-6: Entities, Tracking, Testing (Недели 14-21)
📖 Читать:
- FULL-DEVELOPMENT-PLAN разделы "ФАЗА 4-6"
- QUICK-START-GUIDE раздел "ШАГ 5"

---

## 🎯 КЛЮЧЕВЫЕ КОНЦЕПЦИИ

### Система обработки видео (7 фаз)
1. **Phase 0:** Search Queue (поиск видео)
2. **Phase 0→1:** Video Queue (накопление и приоритизация)
3. **Phase 1:** Transcription (транскрипция, 37+ entities)
4. **Phase 2:** Extraction (расширение до 60-70 entities) ⚠️ КРИТИЧНО
5. **Phase 3:** Gap Analysis (сравнение с LIBRARIES)
6. **Phase 4:** Integration (создание JSON entities)
7. **Phase 5:** Mapping (финальные отчеты)

### Источники данных
- **Dropbox** - source of truth (ENTITIES filesystem)
- **PostgreSQL** - metadata + progress tracking
- **Redis** - caching
- **YouTube API** - видео metadata + transcripts
- **Claude/OpenAI API** - AI processing

### Автоматизация
- **Сейчас:** 70% (22 видео обработано)
- **Цель v1.0:** 90% (Phase 2 automation)
- **Экономия времени:** 2-3 часа → <30 мин на видео

---

## 📊 МЕТРИКИ ПРОЕКТА

### Текущее состояние
- 28 видео обработано
- 500+ entities извлечено
- 22 видео полностью интегрировано
- 14 Python скриптов
- 50+ промптов
- 12 issues идентифицировано

### Цели v1.0
- ✅ 90%+ автоматизация
- ✅ Web приложение на React
- ✅ PostgreSQL + Dropbox integration
- ✅ JWT авторизация + роли
- ✅ Responsive UI (320px-1440px+)
- ✅ Dark/Light mode
- ✅ 80%+ test coverage

### Timeline
- **Total:** 25-26 недель (~6 месяцев)
- **Phase 0-1:** 6 недель (Infrastructure)
- **Phase 2-3:** 7 недель (Core features)
- **Phase 4-6:** 8 недель (Entities + Testing)
- **Buffer:** 4-5 недель (Отладка)

---

## 🔥 КРИТИЧЕСКИЕ ЗАДАЧИ (MUST-FIX для v1.0)

### ISS-RES-005: Phase 2 Automation ⚠️⚠️⚠️
- **Проблема:** 30-45 мин ручной работы на Phase 2
- **Решение:** Автоматизировать PMT-007
- **Эффект:** 30-45 мин → 2-3 мин (90% автоматизация)
- **Где читать:** FULL-DEVELOPMENT-PLAN раздел "3.3: Phase 2 - Extraction Automation"

### ISS-RES-001: Progress Tracker Sync ⚠️
- **Проблема:** 22 видео показывают неверную фазу
- **Решение:** Batch update script
- **Где читать:** FULL-DEVELOPMENT-PLAN раздел "5.1: Progress Tracker Sync"

### ISS-RES-004: Missing Progress Dashboard ⚠️
- **Проблема:** Нет главного dashboard
- **Решение:** Создать Main Dashboard
- **Где читать:** FULL-DEVELOPMENT-PLAN раздел "5.2: Main Dashboard"

### ISS-RES-010: No Unit Tests ⚠️
- **Проблема:** Нет автотестов
- **Решение:** Jest + Pytest с 80%+ coverage
- **Где читать:** FULL-DEVELOPMENT-PLAN раздел "6.1: Unit Testing"

---

## 🛠️ ТЕХНОЛОГИИ

### Frontend
- React 18 + TypeScript
- Tailwind CSS 3 + shadcn/ui
- Zustand (state)
- React Query (data fetching)
- React Router v6
- Recharts (charts)
- Framer Motion (animations)

### Backend
- Node.js 18+ + Express.js 4
- PostgreSQL 14+ (Prisma ORM)
- Redis 7+ (caching)
- Dropbox SDK
- YouTube Data API v3

### AI & APIs
- Claude API (primary)
- OpenAI API (fallback)
- Gemini API (optional)

### DevOps
- Docker + Docker Compose
- GitHub Actions (CI/CD)
- Jest + Pytest (testing)

---

## 📖 КАК ИСПОЛЬЗОВАТЬ ДОКУМЕНТАЦИЮ

### Сценарий 1: "Я начинаю проект с нуля"
1. Читай **QUICK-START-GUIDE-RU.md** полностью
2. Выполни "Phase 0" из Quick Start
3. Следуй **FULL-DEVELOPMENT-PLAN** по фазам

### Сценарий 2: "Мне нужно создать UI компонент"
1. Открой **prompts/FULL-APP-GENERATION-PROMPT.md**
2. Найди нужный компонент (Search Queue, Video Queue, Dashboard)
3. Используй промпт с AI (Claude/ChatGPT/Cursor)

### Сценарий 3: "Мне нужно понять архитектуру"
1. Читай **FULL-DEVELOPMENT-PLAN** раздел "Архитектура системы"
2. Изучи диаграммы
3. Посмотри "Data Flow"

### Сценарий 4: "У меня проблема с setup"
1. Читай **QUICK-START-GUIDE** раздел "Типичные проблемы"
2. Проверь API keys в `.env`
3. Посмотри Docker logs

### Сценарий 5: "Мне нужно оценить сроки"
1. Читай **FULL-DEVELOPMENT-PLAN** раздел "TIMELINE SUMMARY"
2. Изучи каждую фазу
3. Добавь 20-25% buffer

---

## 🔗 ПОЛЕЗНЫЕ ССЫЛКИ

### Референсы
- **Design System:** https://adminrhs.github.io/Design-system/
- **Video Catalog:** https://adminrhs.github.io/Video-catalog/

### Внутренние файлы
- **План в Claude:** `C:\Users\User\.claude\plans\temporal-riding-wilkes.md`
- **Документация:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\documentation\`

### Существующая система
- **Python скрипты:** `G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\`
- **Промпты:** `G:\Job\REMS\Dropbox\ENTITIES\PROMPTS\`
- **ENTITIES:** `G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\`

---

## ✅ ЧЕКЛИСТ ГОТОВНОСТИ К РАЗРАБОТКЕ

Перед началом Phase 1, убедитесь:

**Планирование:**
- [ ] Прочитан QUICK-START-GUIDE-RU.md
- [ ] Прочитан FULL-DEVELOPMENT-PLAN-v1.0-RU.md
- [ ] Понята архитектура системы
- [ ] Понят timeline (25-26 недель)

**Environment:**
- [ ] Node.js 18+ установлен
- [ ] Python 3.10+ установлен
- [ ] Docker установлен и работает
- [ ] PostgreSQL доступен (через Docker)
- [ ] Redis доступен (через Docker)

**API Keys:**
- [ ] Dropbox API token получен
- [ ] YouTube API key получен
- [ ] Claude API key получен
- [ ] OpenAI API key получен (optional)

**Документация:**
- [ ] Все документы скачаны локально
- [ ] Phase 0 промпты подготовлены
- [ ] FULL-APP-GENERATION-PROMPT.md доступен

**Готовность:**
- [ ] Phase 0 (неделя 1) запланирована
- [ ] Git репозиторий создан
- [ ] Рабочее окружение настроено

---

## 📞 ПОМОЩЬ И ПОДДЕРЖКА

**Проблемы с документацией:**
- Проверьте README-DOCS.md (этот файл)
- Найдите нужный раздел выше
- Следуйте "Сценариям использования"

**Технические проблемы:**
- См. QUICK-START-GUIDE раздел "Типичные проблемы"
- Проверьте Docker logs
- Проверьте .env файлы

**Вопросы по плану:**
- См. FULL-DEVELOPMENT-PLAN конкретную фазу
- Изучите подфазы детально
- Следуйте Timeline Summary

---

## 🎯 СЛЕДУЮЩИЕ ШАГИ

1. ✅ Вы прочитали этот README
2. ⏳ Читайте **QUICK-START-GUIDE-RU.md**
3. ⏳ Изучите **FULL-DEVELOPMENT-PLAN-v1.0-RU.md**
4. ⏳ Начните **Phase 0: Промпты и планирование**
5. ⏳ Выполните checklist готовности выше

---

**ГОТОВО К ИСПОЛЬЗОВАНИЮ! 📚**

*Документация создана: 2025-12-08*
*Версия: 1.0*
*Статус: Production Ready*

---

## 📝 ИСТОРИЯ ИЗМЕНЕНИЙ

### v1.0 (2025-12-08)
- ✅ Создан FULL-DEVELOPMENT-PLAN-v1.0-RU.md
- ✅ Создан QUICK-START-GUIDE-RU.md
- ✅ Создан README-DOCS.md (этот файл)
- ✅ Подтверждены требования с клиентом
- ✅ Timeline: 25-26 недель для 1 разработчика
- ✅ Критические issues идентифицированы (ISS-RES-001, 004, 005, 010)
