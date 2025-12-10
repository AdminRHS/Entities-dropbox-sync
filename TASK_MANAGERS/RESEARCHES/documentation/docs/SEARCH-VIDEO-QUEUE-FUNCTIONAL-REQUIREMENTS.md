# SEARCH QUEUE & VIDEO QUEUE - ПОЛНЫЙ СПИСОК ФУНКЦИОНАЛА

**Версия:** 2.0
**Дата:** 2025-12-09
**Статус:** ✅ Production-ready (28+ видео обработано)

**Источники анализа:**
- ✅ documentation/v1 - Версия 1 требования
- ✅ documentation/v2 - Версия 2 обновления
- ✅ documentation/technical - Технические спецификации
- ✅ documentation/taxonomy - Классификация сущностей
- ✅ documentation/issues - Известные проблемы и gaps

---

## СОДЕРЖАНИЕ

1. [Search Queue - Полный функционал](#search-queue)
2. [Video Queue - Полный функционал](#video-queue)
3. [Processing Workflow (7 фаз)](#processing-workflow)
4. [Automation & Intelligence](#automation)
5. [Integration Requirements](#integration)
6. [Known Issues & Gaps](#issues)
7. [Summary Table](#summary)

---

<a name="search-queue"></a>
## 📊 SEARCH QUEUE - ПОЛНЫЙ СПИСОК ФУНКЦИОНАЛА

### 1. Создание и управление поисковыми задачами

#### 1.1 Создание задачи
- ✅ Создание новой поисковой задачи с уникальным ID (SEARCH-001, SEARCH-002...)
- ✅ Назначение задачи сотруднику (Employee field)
- ✅ Указание департамента (DEV, DGN, AID, HR, Sales, VID, SMM, MKT, FIN)
- ✅ Определение темы исследования (Topic field)
- ✅ Опциональное добавление поискового запроса (Search_Query field)
- ✅ Опциональные заметки/инструкции для сотрудника (Notes field)
- ✅ Автоматическая установка статуса "Assigned"
- ✅ Автоматическая запись даты назначения (Date_Assigned)

#### 1.2 Валидация темы
- ✅ Проверка специфичности темы (target: 5-20 результатов)
- ✅ Поддержка тем на основе gap analysis
- ✅ Поддержка запросов от департаментов
- ✅ Поддержка трендовых/новостных тем
- ✅ Поддержка стратегических приоритетов
- ✅ Best practices: проверка уровней специфичности (Broad → Narrow)

### 2. Выполнение поиска

#### 2.1 Отслеживание прогресса
- ✅ Статусная система: **Assigned → In Progress → Completed**
- ✅ Возможность отметить **"On Hold"** или **"Cancelled"**
- ✅ Отслеживание текущего этапа поиска
- ✅ Поддержка нескольких активных поисков одновременно

#### 2.2 Многоплатформенный поиск
- ✅ **YouTube Direct Search** (с фильтрами: дата, длительность, сортировка)
- ✅ **Perplexity AI** (natural language queries)
- ✅ **Google Advanced Search** (site:youtube.com + операторы)
- ✅ **ChatGPT** с браузингом
- ✅ **Google AI Overviews**

#### 2.3 Стратегия поиска

**YouTube Filters:**
- ✅ Upload date (последние 30/60/90 дней)
- ✅ Duration (предпочтительно 10-30 минут)
- ✅ Sort by relevance/upload date
- ✅ Channel credibility verification (10K+ subscribers)
- ✅ View count threshold
- ✅ Engagement metrics (likes/views > 2%, comments)

**Perplexity AI:**
- ✅ Natural language queries
- ✅ AI-curated results from multiple sources
- ✅ Multi-source aggregation
- ✅ Quality filtering

**Google Advanced Operators:**
- ✅ `site:youtube.com` - только YouTube
- ✅ Boolean: `OR`, `AND`, `NOT`
- ✅ Date range: `after:YYYY-MM-DD`
- ✅ Exact phrase: `"Claude Sonnet 4.5"`
- ✅ Exclusion: `-outdated -old`

### 3. Завершение поиска

#### 3.1 Отчетность
- ✅ Отметка поиска как завершенного
- ✅ Запись общего количества найденных видео (Videos_Found)
- ✅ Добавление заметок о результатах (Notes)
- ✅ Документирование эффективности поиска
- ✅ Поддержка нулевых результатов с рекомендациями
- ✅ Запись даты завершения (Date_Completed)

#### 3.2 Передача в Video Queue
- ✅ Ссылка на исходный SEARCH-XXX при добавлении видео
- ✅ Связывание найденных видео с задачей поиска
- ✅ Отслеживание метрики videos-per-search
- ✅ Поддержка batch добавления видео после завершения

### 4. Интеграция с промптами

#### 4.1 Используемые промпты
- ✅ **PMT-048:** YouTube AI Tools Daily
- ✅ **PMT-089:** YouTube AI Tutorials Research
- ✅ **PMT-093:** Design AI Video Discovery
- ✅ **PMT-098:** OpenAI Automation Examples
- ✅ **PMT-044 to PMT-052:** Department-specific prompts

### 5. Критерии качества

#### 5.1 Видео для добавления ✅
- Высокое производственное качество
- Trusted source/channel (10K+ подписчиков)
- Практический/actionable контент
- Недавнее (< 60 дней preferred)
- Хорошие engagement метрики (like/view ratio > 2%)
- Релевантность теме

#### 5.2 Видео для пропуска ❌
- Низкое качество производства
- Неизвестный/ненадежный источник
- Только теория, без практики
- Устаревшее (если не evergreen)
- Низкий/нулевой engagement
- Off-topic контент

### 6. Метрики и KPI

#### 6.1 Целевые показатели
| Метрика | Целевое значение |
|---------|------------------|
| Searches assigned per week | 3-5 |
| Completion rate | >80% |
| Videos per search | 5-15 (качественные) |
| Queue addition rate | 10-25 видео/неделю |
| Search-to-process rate | 15-20% |
| Average time per search | 55-75 минут |

#### 6.2 Отслеживаемые метрики
- ✅ Количество назначенных поисков
- ✅ Количество завершенных поисков
- ✅ Средняя длительность поиска
- ✅ Видео на поиск (среднее)
- ✅ Процент успешности
- ✅ Эффективность по департаментам

### 7. Data Model

#### 7.1 Search_Queue_Master.csv структура

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Search_ID | String | SEARCH-001, SEARCH-002... | Уникальный идентификатор |
| Employee | String | Name | Назначенный сотрудник |
| Department | Enum | DEV, DGN, AID, HR, Sales, VID, SMM, MKT, FIN | Департамент |
| Topic | String | Text | Тема исследования |
| Search_Query | String (optional) | Text | Поисковый запрос |
| Status | Enum | Assigned, In Progress, Completed, On Hold, Cancelled | Статус задачи |
| Videos_Found | Integer | 0-N | Количество найденных видео |
| Date_Assigned | Date | YYYY-MM-DD | Дата назначения |
| Date_Completed | Date (nullable) | YYYY-MM-DD | Дата завершения |
| Notes | Text (nullable) | Free text | Заметки и комментарии |

### 8. Best Practices

#### 8.1 Создание задач
- ✅ Четкие, специфичные темы (не "AI tools", а "Claude Sonnet 4.5 features")
- ✅ Стратегический timing (после анонсов, gap analysis, quarterly planning)
- ✅ Точный scope (ожидание 5-20 результатов)
- ✅ Regular reviews (daily assigned, weekly completion, monthly effectiveness)

#### 8.2 Документирование
- ✅ Детальные completion notes
- ✅ Отслеживание efficiency
- ✅ Отслеживание quality
- ✅ Coverage analysis
- ✅ Effectiveness metrics

---

<a name="video-queue"></a>
## 🎬 VIDEO QUEUE - ПОЛНЫЙ СПИСОК ФУНКЦИОНАЛА

### 1. Добавление видео в очередь

#### 1.1 Ручное добавление
- ✅ Добавление по YouTube URL (множество форматов):
  - `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - `https://www.youtube.com/embed/VIDEO_ID`
  - `https://m.youtube.com/watch?v=VIDEO_ID`
- ✅ Автоматическая генерация Queue_ID (VQ-001, VQ-002...)
- ✅ Автоматическое извлечение Video_ID (11 символов)
- ✅ Запись сотрудника, добавившего видео (Added_By)
- ✅ Установка research topic/category
- ✅ Указание research source (Perplexity, Gemini, GPT, DeepSeek, YouTube)
- ✅ Опциональные заметки о релевантности (Notes)
- ✅ Автоматическая установка статуса "Pending"
- ✅ Автоматическое определение дубликатов
- ✅ Batch addition support (быстрое добавление нескольких видео)

#### 1.2 Автоматическое извлечение метаданных
- ✅ Извлечение YouTube video ID из URL
- ✅ Автоустановка Queue status = "Pending"
- ✅ Автогенерация Queue_ID
- ✅ Определение дубликатов (предотвращение повторного добавления)
- ✅ Автосоздание CSV если не существует
- ✅ Без зависимости от pandas (pure Python опция)

#### 1.3 YouTube API Integration (⏳ ISS-RES-008 - ТРЕБУЕТСЯ)
**Приоритет:** HIGH
**Экономия времени:** 5-10 минут на видео

**Автоматическое получение:**
- ⏳ Title (название видео)
- ⏳ Channel name (название канала)
- ⏳ Duration (длительность)
- ⏳ Upload date (дата публикации)
- ⏳ View count (количество просмотров)
- ⏳ Like count (количество лайков)
- ⏳ Video description (описание)
- ⏳ Thumbnail URL (ссылка на превью)
- ⏳ Captions availability (наличие субтитров)

### 2. Система приоритизации (0-100)

#### 2.1 Алгоритм расчета приоритета

```
Priority Score = (Views Score × 30%) + (Likes Score × 20%) +
                 (Recency Score × 30%) + (Engagement Score × 20%)
```

#### 2.2 Factor 1: Views Score (30% вес)

**Формула:** `min(30, (views / 1,000,000) × 30)`

| Views | Score |
|-------|-------|
| 1M+ | 30 баллов |
| 500K | 15 баллов |
| 100K | 3 балла |

#### 2.3 Factor 2: Likes Score (20% вес)

**Формула:** `min(20, (likes / 50,000) × 20)`

| Likes | Score |
|-------|-------|
| 50K+ | 20 баллов |
| 25K | 10 баллов |
| 10K | 4 балла |

#### 2.4 Factor 3: Recency Score (30% вес)

**Формула:** `max(0, 30 × (1 - Days Since Publish / 365))`

| Days Old | Score |
|----------|-------|
| 0 дней | 30 баллов |
| 90 дней | 22.6 баллов |
| 180 дней | 15.2 баллов |
| 365 дней | 0 баллов |

#### 2.5 Factor 4: Engagement Score (20% вес)

**Формула:** `min(20, (Engagement Rate × 100) × 20)`

| Engagement Rate | Score |
|-----------------|-------|
| 1%+ | 20 баллов |
| 0.5% | 10 баллов |
| 0.1% | 2 балла |

#### 2.6 Priority Levels (5-tier system)

| Level | Range | Stars | Color | Action |
|-------|-------|-------|-------|--------|
| **Critical** | 80-100 | ⭐⭐⭐⭐⭐ | #DC2626 (Red) | Обработать немедленно |
| **High** | 60-79 | ⭐⭐⭐⭐ | #EA580C (Orange) | Обработать в течение 2 дней |
| **Medium** | 40-59 | ⭐⭐⭐ | #F59E0B (Yellow) | Обработать в течение 1 недели |
| **Low** | 20-39 | ⭐⭐ | #84CC16 (Light Green) | Review quarterly |
| **Very Low** | 0-19 | ⭐ | #22C55E (Green) | Рассмотреть отклонение |

#### 2.7 ML-Based Prioritization (⏳ ISS-RES-009 - ПЛАНИРУЕТСЯ)

**Улучшение через machine learning:**
- ⏳ Title keywords (AI, trending topics)
- ⏳ Channel authority/credibility
- ⏳ Historical usefulness (какие видео создали ценные entities)
- ⏳ Department-specific needs (gaps in taxonomy)
- ⏳ Topic relevance to strategic priorities
- ⏳ **Ожидаемое улучшение:** 15-20% точности

### 3. Управление очередью и статусами

#### 3.1 Пятиступенчатая система статусов

```
Pending → Selected → Parsing → Parsed
   ↓
Rejected
```

**Статус 1: Pending (Ожидает review)**
- Новое добавление
- Сотрудник просматривает и выбирает или отклоняет
- Накопление до 20 видео перед batch review

**Статус 2: Selected (Выбрано для обработки)**
- Отмечено сотрудником для обработки
- Приоритет одобрен
- Ожидает начала транскрипции (Phase 1)

**Статус 3: Parsing (В процессе транскрипции)**
- В Phase 1 processing
- Ожидание завершения транскрипции

**Статус 4: Parsed (Транскрипция завершена)**
- Transcript сохранен в `02_TRANSCRIPTIONS/Video_XXX.md`
- Готов к Phase 2 (Extraction)
- Переход к анализу

**Статус 5: Rejected (Отклонено)**
- Не релевантно для текущих исследований
- Исключено из обработки
- Остается в очереди для справки

#### 3.2 Управление накоплением
- ✅ Накопление до 20 видео перед review
- ✅ Предотвращение потери результатов исследований
- ✅ Эффективная batch обработка
- ✅ **100% retention** (vs 95% loss в ручном процессе)
- ✅ Persistent queue между сессиями

#### 3.3 Философия Manual Approval (2 точки)

**Approval Point 1: Video Selection**
- **Когда:** После накопления 10-20 видео
- **Кто:** Researcher/employee
- **Решение:** Какие видео обработать vs отклонить
- **Процесс:** Dashboard → filter → review → select → reject
- **Автоматизация:** Направляет с priority scores, не решает

**Approval Point 2: Final Review**
- **Когда:** После Phase 1 (transcription) завершения
- **Кто:** Employee или team lead
- **Решение:** Принять качество транскрипта, перейти к Phase 2
- **Процесс:** Review files → verify 37+ entities → check accuracy
- **Автоматизация:** Предоставляет transcript, не судит релевантность

### 4. Отображение и фильтрация очереди

#### 4.1 Dashboard Display
- ✅ Video cards с thumbnail preview
- ✅ Channel информация
- ✅ View/like counts
- ✅ Priority score с цветовой кодировкой
- ✅ Publication date
- ✅ Topic category badge
- ✅ Source badge
- ✅ Status indicator

#### 4.2 Фильтры
- ✅ Filter by topic (тема исследования)
- ✅ Filter by status (Pending/Selected/Parsing/Parsed/Rejected)
- ✅ Filter by source (Perplexity/Gemini/GPT/YouTube)
- ✅ Filter by employee (кто добавил)
- ✅ Filter by department
- ✅ Filter by priority level (High/Medium/Low)

#### 4.3 Сортировка
- ✅ Sort by priority score (по убыванию)
- ✅ Sort by date added (новые сначала)
- ✅ Sort by views (по убыванию)
- ✅ Sort by likes (по убыванию)
- ✅ Sort by duration (по возрастанию/убыванию)
- ✅ Sort by upload date (свежие сначала)

#### 4.4 Поиск
- ✅ Search by title
- ✅ Search by channel name
- ✅ Search by topic
- ✅ Search by Queue_ID (VQ-XXX)

### 5. Batch обработка

#### 5.1 Множественный выбор
- ✅ Select multiple videos (обычно 5-10)
- ✅ Checkboxes для выбора
- ✅ Select all / Deselect all
- ✅ Select by priority threshold

#### 5.2 Batch операции (⏳ ISS-RES-006 - ТРЕБУЕТСЯ)

**Команды:**
- ⏳ `--batch Video_024 Video_025 Video_026` - Указать список
- ⏳ `--batch-range Video_024 Video_030` - Диапазон
- ⏳ `--batch-all-pending` - Все pending видео
- ⏳ `--batch-top 10` - Топ 10 по приоритету
- ⏳ Auto-approval mode для unattended processing

**Функции:**
- ⏳ Process all selected videos together
- ⏳ Batch status updates
- ⏳ Parallel processing с rate limiting
- ⏳ Progress tracking по видео
- ⏳ Export selected videos

#### 5.3 Статистика очереди
- ✅ Total videos in queue count
- ✅ Videos by priority (High/Medium/Low) - pie chart
- ✅ Videos by status - distribution
- ✅ Videos by employee - bar chart
- ✅ Videos by topic - breakdown
- ✅ Videos by source - distribution
- ✅ Priority distribution percentages
- ✅ Average priority score
- ✅ Time in queue metrics
- ✅ Processing rate metrics

### 6. Dashboard и визуализация

#### 6.1 Video_Queue_Dashboard.html (✅ СУЩЕСТВУЕТ)
- ✅ Rich visualization
- ✅ Interactive charts (pie, bar)
- ✅ Sortable/filterable table
- ✅ Responsive design
- ✅ Real-time updates (при обновлении CSV)

#### 6.2 Progress Dashboard (⏳ ISS-RES-004 - ТРЕБУЕТСЯ)

**Progress_Dashboard.html должен показывать:**
- ⏳ Total videos processed
- ⏳ Videos by phase (bar chart)
- ⏳ Completion rate percentage
- ⏳ Average processing time
- ⏳ Recent activity (last 5 videos)
- ⏳ Bottleneck identification (phases > 7 days)

### 7. Data Model

#### 7.1 Video_Queue_Master.csv (21 полей)

| # | Field | Type | Example | Description |
|---|-------|------|---------|-------------|
| 1 | Queue_ID | String | VQ-001 | Уникальный идентификатор очереди |
| 2 | Video_ID | String (11 char) | dQw4w9WgXcQ | YouTube video ID |
| 3 | Video_Title | String | "Claude API Tutorial" | Название видео |
| 4 | Channel_Name | String | "AI Academy" | Название канала |
| 5 | Channel_URL | String | youtube.com/c/... | URL канала |
| 6 | Video_URL | String | youtube.com/watch?v=... | Полный URL видео |
| 7 | Views | Integer | 250000 | Количество просмотров |
| 8 | Likes | Integer | 12000 | Количество лайков |
| 9 | Comments | Integer | 450 | Количество комментариев |
| 10 | Publish_Date | Date | 2025-11-15 | Дата публикации |
| 11 | Duration | String | 00:25:33 | Длительность (HH:MM:SS) |
| 12 | Added_By | String | "John Doe" | Кто добавил |
| 13 | Added_Date | Date | 2025-12-04 | Дата добавления |
| 14 | Status | Enum | Pending | Текущий статус |
| 15 | Selected_By | String | "Jane Smith" | Кто выбрал |
| 16 | Selected_Date | Date | 2025-12-05 | Дата выбора |
| 17 | Parsed_Date | Date | 2025-12-06 | Дата парсинга |
| 18 | Topic_Category | String | "AI Integration" | Категория темы |
| 19 | Research_Source | Enum | Perplexity | Источник |
| 20 | Priority_Score | Float | 75.5 | Оценка приоритета (0-100) |
| 21 | Notes | Text | "High priority" | Заметки |

### 8. Скрипты и команды

#### 8.1 Существующие скрипты (✅ РАБОТАЮТ)
- ✅ `add_video_to_queue_simple.py` - Добавление с auto-metadata
- ✅ `add_video_to_queue.py` - Advanced extraction (pandas-based)
- ✅ `update_queue_status.py` - Обновление статуса
  - Commands: `update`, `summary`, `list`
- ✅ `export_queue.py` - Export в CSV/JSON/Markdown
- ✅ `calculate_priority.py` - Тестирование алгоритма приоритетов
- ✅ `video_queue_manager.py` - Interactive CLI (JSON-based)

#### 8.2 Требуемые скрипты (⏳ ПЛАНИРУЮТСЯ)
- ⏳ `youtube_api.py` - YouTube API integration (ISS-RES-008)
- ⏳ `video_extraction_automator.py` - Phase 2 automation (ISS-RES-005)
- ⏳ Batch processing flags для `process_video.py` (ISS-RES-006)

### 9. Интеграция с другими фазами

#### 9.1 Интеграция с Search Queue (Phase 0)
- ✅ Input: Видео из SEARCH-XXX задач
- ✅ Запись source SEARCH-XXX при добавлении
- ✅ Отслеживание каких поисков произвели видео
- ✅ Агрегация видео по search topic

#### 9.2 Интеграция с Transcriptions (Phase 1)
- ✅ Input: Видео со Status="Selected"
- ✅ Output: Selected videos (VQ-XXX) готовы для транскрипции
- ✅ Queue_ID referenced в transcription files
- ✅ Status updated на "Parsing" во время транскрипции
- ✅ Status updated на "Parsed" после завершения

#### 9.3 Интеграция с Deep Research Tasks
- ✅ Auto-add все найденные видео в очередь
- ✅ Не требуется немедленный выбор
- ✅ Сотрудник продолжает исследование без прерывания
- ✅ Review queue когда удобно (10-20 видео накоплено)

#### 9.4 Интеграция с REPORTS/Videos Directory
- ✅ Сохранение metadata в `REPORTS/Videos/Metadata/`
- ✅ Routing transcriptions в `REPORTS/Videos/Transcripts/`
- ✅ Архивирование analysis reports в `REPORTS/Videos/Analysis/`

#### 9.5 Интеграция с Daily Reports
- ✅ Включение queue statistics в employee daily reports
- ✅ Отслеживание videos added per day
- ✅ Показ queue status metrics

### 10. Метрики и KPI

#### 10.1 Queue Statistics
| Статус | Описание |
|--------|----------|
| Total videos in queue | Всего в очереди |
| Pending videos | Ожидают review |
| Selected videos | Одобрены для обработки |
| Parsing videos | В процессе |
| Parsed videos | Завершены |
| Rejected videos | Отклонены |

#### 10.2 Priority Distribution (Target)
| Уровень | Range | Target % |
|---------|-------|----------|
| High priority | 70-100 | 30-40% |
| Medium priority | 40-69 | 40-50% |
| Low priority | 0-39 | 10-20% |

#### 10.3 Processing Metrics
- ✅ Videos added per day/week
- ✅ Average time in queue
- ✅ Videos selected per batch (target 5-10)
- ✅ Completion rate
- ✅ Rejection rate
- ✅ Processing time per video (Phase 1-5)

#### 10.4 Efficiency Gains (vs Manual Process)

| Метрика | Manual | Automated | Gain |
|---------|--------|-----------|------|
| Video selection time | 10-15 min | 2-3 min | 80% ↓ |
| Videos retained | 5% | 100% | 95% ↑ |
| Batch size | 1 video | 20 videos | 20x ↑ |
| Queue visibility | None | Full dashboard | ∞ ↑ |
| Priority ranking | Manual guess | Objective 0-100 | Consistency ↑ |

### 11. Troubleshooting и Error Handling

#### 11.1 Обработка ошибок

| Ошибка | Решение |
|--------|---------|
| Queue CSV Not Found | → Auto-create |
| Dashboard Not Loading | → Verify CSV format |
| Priority Score is 0 | → Check missing metadata |
| Video Already in Queue | → Return existing Queue_ID |
| Can't Extract Video ID | → Validate URL format |
| Status Update Not Saving | → Close CSV editors |
| Export Fails | → Create exports/ directory |

#### 11.2 Data Integrity (⏳ ISS-RES-001 - КРИТИЧНО)

**Проблема:**
- VIDEO_PROGRESS_TRACKER.csv desynchronization
- Все 22 видео показывают "Phase_1", но реальный статус "Complete"

**Решение:**
- ⏳ HIGH priority fix needed
- ⏳ Automated sync between tracking system and actual state

### 12. User Experience Features

#### 12.1 Quick Actions
- ✅ Select for parsing (checkbox)
- ✅ Reject video (button)
- ✅ Add notes (text field)
- ✅ View full details (expand card)
- ✅ Copy URL (clipboard button)
- ✅ Open in YouTube (external link)
- ✅ Update status dropdown
- ✅ Manual priority override

#### 12.2 Batch Operations UI
- ✅ Select multiple videos (checkboxes)
- ✅ Bulk status update (dropdown + apply)
- ✅ Bulk export (button)
- ✅ Bulk delete/mark rejected (button)
- ✅ Clear all selections (button)
- ✅ Select all visible (button)
- ✅ Select by priority range (slider)

---

<a name="processing-workflow"></a>
## 🔄 PROCESSING WORKFLOW (7 PHASES)

### Phase 0: Search Queue
**Duration:** 55-75 минут
**Automation:** 80%

- ✅ Discover videos via search tasks
- ✅ Track search assignments
- ✅ Monitor search completion
- ✅ Transfer videos to queue

### Phase 0→1: Video Queue
**Duration:** 2-3 минуты (review), 5-10 минут (batch)
**Automation:** 90%

- ✅ Accumulate discovered videos
- ✅ Calculate priority scores
- ✅ Select for processing
- ✅ Batch management

### Phase 1: TRANSCRIPTION
**Duration:** 1-2 hours
**Automation:** Manual с AI (Claude/ChatGPT)
**Prompt:** PMT-004 (Video Transcription v4.1)

- ✅ Full video transcription
- ✅ Extract 37+ pre-categorized entities
- ✅ Metadata capture
- ✅ **Output:** `Video_XXX.md` (400-500 lines)

### Phase 2: EXTRACTION
**Duration:** 30-45 min (⏳ could be 5-10 min with automation)
**Automation:** 10% (⏳ ISS-RES-005 - критичный gap)
**Prompt:** PMT-007 (Objects Library Extraction)

- ✅ Deep entity extraction
- ✅ Expand 37 → 60-70 entities
- ✅ Create cross-reference matrix
- ✅ **Output:** `Phase3_Analysis.md` + `Phase4_Objects.md`
- ⏳ **Automation potential:** 90% (could reduce to 5-10 min)

### Phase 3: GAP ANALYSIS
**Duration:** 2-3 min automated / 20-30 min manual
**Automation:** 95%
**Prompt:** PMT-009 Part 1

- ✅ Compare vs. LIBRARIES
- ✅ Categorize: NEW/EXISTING/UPDATE
- ✅ Calculate coverage improvement
- ✅ **Output:** `Gap_Analysis.md` with 20-30 NEW entities

### Phase 4: INTEGRATION
**Duration:** 45-60 min / 5-10 min automated
**Automation:** 40% semi-automated
**Prompt:** PMT-009 Part 2

- ✅ Create JSON files for NEW entities
- ✅ Assign unique IDs (TOL-###, WRF-###, etc.)
- ✅ Validate schema
- ✅ Copy to LIBRARIES/
- ✅ **Output:** 20-30 JSON files

### Phase 5: MAPPING
**Duration:** 30-45 min / 2-3 min automated
**Automation:** 95%
**Prompt:** PMT-009 Part 3

- ✅ Generate comprehensive report
- ✅ Document coverage improvement
- ✅ Business value analysis
- ✅ Quality metrics
- ✅ **Output:** `Library_Mapping_Report.md`

### Phase 6: COMPLETE
**Duration:** 5-10 минут
**Automation:** 100%

- ✅ Archive completed research
- ✅ Update registries
- ✅ Log integration
- ✅ Mark as COMPLETE

---

<a name="automation"></a>
## 🔧 AUTOMATION & INTELLIGENCE

### Уровень автоматизации по фазам

| Phase | Automation | Duration | Gap/Opportunity |
|-------|------------|----------|-----------------|
| **Phase 0** (Search) | 80% | 55-75 min | Search execution manual |
| **Phase 0→1** (Queue) | 90% | 2-3 min | YouTube API missing (ISS-RES-008) |
| **Phase 1** (Transcription) | Manual с AI | 1-2 hours | Working with Claude/ChatGPT |
| **Phase 2** (Extraction) | 10% | 30-45 min | ⏳ **КРИТИЧНЫЙ GAP** (ISS-RES-005) |
| **Phase 3** (Gap Analysis) | 95% | 2-3 min | Fully automated |
| **Phase 4** (Integration) | 40% | 5-10 min | Semi-automated |
| **Phase 5** (Mapping) | 95% | 2-3 min | Fully automated |
| **Overall** | **70%** | **2-3 hours** | Target: 90%+ |

### Интеллектуальная приоритизация

**Текущая система:**
- ✅ Multi-factor scoring (views, likes, recency, engagement)
- ✅ Dynamic recalculation (weekly)
- ✅ Manual override capability
- ✅ 4 фактора с весами (30%, 20%, 30%, 20%)

**Планируемая система (ISS-RES-009):**
- ⏳ ML-based модель
- ⏳ Дополнительные факторы:
  - Title keywords
  - Channel authority
  - Historical usefulness
  - Department gaps
  - Strategic priorities
- ⏳ Ожидаемое улучшение: 15-20%

### Batch Processing

**Текущая способность:**
- ✅ Queue до 20 видео
- ✅ Select 3-5 для обработки
- ✅ Manual batch review

**Планируемое (ISS-RES-006):**
- ⏳ Parallel Phase 1 transcription
- ⏳ Batch Phase 2 extraction
- ⏳ Wait queues с rate limiting
- ⏳ Auto-approval mode

---

<a name="integration"></a>
## 🔌 INTEGRATION REQUIREMENTS

### YouTube Data API v3 (⏳ ISS-RES-008)

**Status:** Required, not implemented
**Priority:** HIGH
**Impact:** 5-10 min saved per video

**Fields to fetch:**
- Title, Channel, Duration, Upload date
- Views, Likes, Comments
- Description, Thumbnail URL
- Captions availability

**Implementation:**
```python
youtube_api.get_video_metadata(url) → {
  "title": "...",
  "channel": "...",
  "views": 250000,
  "likes": 12000,
  "duration": "PT25M33S",  # ISO 8601
  "upload_date": "2025-11-15",
  "thumbnail": "https://...",
  "description": "..."
}
```

### OpenAI/Claude API

**Status:** Currently used manually
**Used in:** Phase 1 (Transcription), Phase 2 (Extraction)

**Prompts:**
- PMT-004: Video Transcription v4.1
- PMT-007: Objects Library Extraction
- PMT-009: Taxonomy Integration (Parts 1-3)

**Automation opportunity:**
- ⏳ Phase 2 extraction (ISS-RES-005) - критичный gap

### Dropbox API

**Status:** File storage and sync
**Integration points:**
- Video_Queue_Master.csv sync
- Transcription files backup
- JSON files sync to LIBRARIES
- Reports export

---

<a name="issues"></a>
## 📋 KNOWN ISSUES & GAPS

### CRITICAL (HIGH Priority)

#### ISS-RES-001: VIDEO_PROGRESS_TRACKER Desynchronization
**Проблема:** Все 22 видео показывают "Phase_1", реально "Complete"
**Impact:** Data integrity критична
**Решение:** Automated sync needed

#### ISS-RES-005: Non-Automated Phase 2 (Extraction)
**Проблема:** 30-45 min/video MANUAL
**Impact:** Largest automation gap
**Решение:** `video_extraction_automator.py` needed
**Potential:** 90% automation (reduce to 5-10 min)

#### ISS-RES-008: Missing YouTube API Integration
**Проблема:** 5-10 min/video wasted на manual metadata entry
**Impact:** Time waste + errors
**Решение:** `youtube_api.py` implementation

### MEDIUM Priority

#### ISS-RES-004: Missing Progress Dashboard
**Проблема:** No Progress_Dashboard.html
**Impact:** Limited visibility
**Решение:** Real-time metrics visualization + bottleneck identification

#### ISS-RES-006: Missing Batch Processing
**Проблема:** No `--batch` flags for `process_video.py`
**Impact:** Sequential processing only
**Решение:** Auto-approval mode + parallel processing

#### ISS-RES-009: ML-Based Prioritization
**Проблема:** Simple formula vs ML model
**Impact:** Could be 15-20% more accurate
**Решение:** ML model с feature engineering

### LOW Priority

#### ISS-RES-002: Missing Video_015
**Проблема:** Gap in sequential numbering
**Решение:** Document/fill/accept gaps

#### ISS-RES-003: Conflicting Files
**Проблема:** PMT-051 _CONFLICT version
**Решение:** Resolution needed

#### ISS-RES-007: JSON Formatting
**Проблема:** No automated pretty-printing
**Решение:** Better git diffs

#### ISS-RES-010: Missing Automated Tests
**Проблема:** No unit tests for 16 Python scripts
**Решение:** pytest suite (60-90% coverage)

---

<a name="summary"></a>
## 📊 SUMMARY TABLE

| Feature | Search Queue | Video Queue |
|---------|--------------|-------------|
| **Create/Add** | Search assignment (SEARCH-XXX) | Video to queue (VQ-XXX) |
| **Unique ID Format** | SEARCH-001, SEARCH-002... | VQ-001, VQ-002... |
| **Status Workflow** | Assigned→In Progress→Completed | Pending→Selected→Parsing→Parsed/Rejected |
| **Key Data Fields** | Employee, Department, Topic, Query, Videos Found | Title, Channel, Views, Likes, Priority Score |
| **Primary Metrics** | Completion rate, Videos per search | Priority distribution, Processing rate |
| **Batch Operations** | Individual search assignments | Up to 20 videos batch processing |
| **Manual Approval** | Assignment creation, search execution | Video selection, final transcript review |
| **Integration Points** | Gap analysis, department requests | Transcription queue, daily reports |
| **Quality Standards** | Topic specificity, search strategy | Production value, engagement, recency |
| **Automation Level** | 80% | 90% |
| **Dashboard** | Simple list/tracking | Rich visualization, charts, filters |

---

## 🎯 IMPLEMENTATION PRIORITIES

### Quick Wins (< 1 неделя)
1. **ISS-RES-001:** Fix VIDEO_PROGRESS_TRACKER (2-3 hours)
2. **ISS-RES-006:** Add --batch processing (1 день)
3. **ISS-RES-007:** JSON formatting validation (2-3 hours)

### High-Impact Automation (1-2 недели)
1. **ISS-RES-005:** Phase 2 extraction automator (25-35 min saved per video)
2. **ISS-RES-008:** YouTube API integration (5-10 min saved per video)
3. **Together:** 100-200 hours saved annually across 100 videos

### Medium-Term Enhancements (2-4 недели)
1. **ISS-RES-004:** Progress Dashboard
2. **ISS-RES-009:** ML-based prioritization
3. **ISS-RES-010:** Automated tests

### Total Estimated Effort: 7-9 weeks
- HIGH priority: 4-5 weeks
- MEDIUM priority: 2-3 weeks
- LOW priority: 1 week

---

## 📈 SUCCESS METRICS

### Current State (28 videos processed)
- ✅ Processing time: 2-3 hours per video
- ✅ Entities extracted: 42-45 per video
- ✅ Quality score: 0.92-0.95
- ✅ Automation level: 70%
- ✅ Success rate: 95%+

### Target State (100+ videos)
- 🎯 Processing time: 1-2 hours per video (50% reduction)
- 🎯 Entities extracted: 50-60 per video
- 🎯 Quality score: 0.95+
- 🎯 Automation level: 90%+
- 🎯 Success rate: 98%+
- 🎯 Time savings: 700-1000 hours/year

---

**Дата создания:** 2025-12-09
**Версия:** 2.0
**Статус:** ✅ Ready for Implementation
**Следующий шаг:** Use this list for technical specs and roadmap development
