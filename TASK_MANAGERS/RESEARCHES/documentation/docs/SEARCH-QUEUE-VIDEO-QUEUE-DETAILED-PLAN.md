# ДЕТАЛЬНЫЙ ПЛАН: SEARCH QUEUE & VIDEO QUEUE МОДУЛИ

**Дата создания:** 2025-12-08
**Версия:** 1.0
**Статус:** Готов к разработке

---

## ОГЛАВЛЕНИЕ

1. [Обзор системы](#обзор-системы)
2. [Модуль 1: Search Queue](#модуль-1-search-queue)
3. [Модуль 2: Video Queue](#модуль-2-video-queue)
4. [Промпты для модулей](#промпты-для-модулей)
5. [UI/UX Дизайн](#uiux-дизайн)
6. [Интеграция с локальными файлами](#интеграция-с-локальными-файлами)
7. [Технические детали](#технические-детали)

---

## ОБЗОР СИСТЕМЫ

### Workflow между модулями

```
┌─────────────────┐
│  SEARCH QUEUE   │ ← Создание задачи поиска
│  (Модуль 1)     │
└────────┬────────┘
         │
         │ Выполнение промпта поиска
         │ (PMT-093, research prompts)
         ▼
┌─────────────────┐
│  Найденные видео│ ← Модальное окно с результатами
└────────┬────────┘
         │
         │ Пользователь выбирает видео
         ▼
┌─────────────────┐
│  VIDEO QUEUE    │ ← Добавление видео в очередь
│  (Модуль 2)     │
└─────────────────┘
```

### Хранение данных

**Двойное хранение:**
- **Google Sheets** - primary storage (real-time sync)
- **Локальный файл Dropbox** - secondary storage (backup + offline)

**Синхронизация:**
- Каждая операция записывается в Google Sheets
- Асинхронно дублируется в локальный файл
- При запуске приложения - сканирование обоих источников
- Конфликты разрешаются в пользу Google Sheets (source of truth)

---

## МОДУЛЬ 1: SEARCH QUEUE

### 1.1 Функционал

**Основные возможности:**
1. Создание новой задачи поиска (SEARCH-XXX)
2. Назначение задачи сотруднику
3. Выбор department и topic
4. Выполнение промпта поиска
5. Просмотр результатов в модальном окне
6. Добавление найденных видео в Video Queue
7. Завершение задачи с отчётом

### 1.2 UI/UX Компоненты

#### Главная страница Search Queue

```
┌────────────────────────────────────────────────────────┐
│                    SEARCH QUEUE                        │
│  [+ New Search Task]                    [Filter ▼]     │
├────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │ SEARCH-001 | AI Tools Research                   │ │
│  │ Employee: John Doe    Department: AI             │ │
│  │ Status: Assigned      Date: 2025-12-08           │ │
│  │ [Execute Search] [View Details] [Complete]       │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
│  ┌──────────────────────────────────────────────────┐ │
│  │ SEARCH-002 | Design Tool Updates                 │ │
│  │ Employee: Jane Smith  Department: Design         │ │
│  │ Status: In Progress   Date: 2025-12-07           │ │
│  │ [Execute Search] [View Details] [Complete]       │ │
│  └──────────────────────────────────────────────────┘ │
│                                                         │
└────────────────────────────────────────────────────────┘
```

#### Модальное окно создания задачи

```
┌─────────────────────────────────────────────────────┐
│  Create New Search Task                     [X]     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Employee:  [Dropdown: Select Employee ▼]          │
│                                                      │
│  Department: [Dropdown: AI/Design/Dev/etc ▼]       │
│                                                      │
│  Topic:      [Input: e.g., AI Tools, Design...]    │
│                                                      │
│  Search Type: [Dropdown ▼]                          │
│    • Daily AI Tools (PMT-048)                       │
│    • Weekly Tutorials (PMT-089)                     │
│    • Design Tools (PMT-093)                         │
│    • Custom Search                                  │
│                                                      │
│  Custom Query: [Textarea - if Custom selected]     │
│                                                      │
│  Notes: [Textarea]                                  │
│                                                      │
│  [Cancel]                    [Create & Execute]     │
└─────────────────────────────────────────────────────┘
```

#### Модальное окно результатов поиска

```
┌──────────────────────────────────────────────────────────┐
│  Search Results - SEARCH-001              [X]            │
├──────────────────────────────────────────────────────────┤
│  Found 12 videos                                         │
│  [Select All] [Deselect All]                            │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ☑ ┌────────────────────────────────────────────────┐  │
│    │ 🎬 Claude AI Complete Guide                    │  │
│    │ Channel: AI Academy | 18:42 | 125K views      │  │
│    │ https://youtube.com/watch?v=xxxxx              │  │
│    │ Priority: ⭐⭐⭐⭐⭐ (95)                          │  │
│    └────────────────────────────────────────────────┘  │
│                                                          │
│  ☑ ┌────────────────────────────────────────────────┐  │
│    │ 🎬 Building AI Agents from Scratch             │  │
│    │ Channel: Code Masters | 22:15 | 89K views     │  │
│    │ https://youtube.com/watch?v=yyyyy              │  │
│    │ Priority: ⭐⭐⭐⭐ (82)                            │  │
│    └────────────────────────────────────────────────┘  │
│                                                          │
│  ☐ ┌────────────────────────────────────────────────┐  │
│    │ 🎬 AI Tool Review: Top 10 Tools 2025          │  │
│    │ Channel: Tech Reviews | 15:30 | 45K views     │  │
│    │ https://youtube.com/watch?v=zzzzz              │  │
│    │ Priority: ⭐⭐⭐ (68)                              │  │
│    └────────────────────────────────────────────────┘  │
│                                                          │
│  [... 9 more videos ...]                                │
│                                                          │
│  [Cancel]  [Add Selected to Video Queue (2)]           │
└──────────────────────────────────────────────────────────┘
```

### 1.3 Backend API

#### Endpoints

```javascript
// GET /api/search-queue
// Получить все задачи поиска
Response: {
  tasks: [
    {
      search_id: "SEARCH-001",
      employee: "John Doe",
      department: "AI",
      topic: "AI Tools Research",
      search_query: "Build AI Agent Social Strategy",
      status: "Assigned", // Assigned/In_Progress/Completed
      date_assigned: "2025-12-08T10:00:00Z",
      videos_found: 0,
      date_completed: null,
      notes: ""
    }
  ]
}

// POST /api/search-queue/create
// Создать новую задачу
Request: {
  employee: "John Doe",
  department: "AI",
  topic: "AI Tools Research",
  search_type: "PMT-093", // или "custom"
  custom_query?: "...",
  notes?: ""
}
Response: {
  search_id: "SEARCH-042",
  status: "created"
}

// POST /api/search-queue/:search_id/execute
// Выполнить поиск видео
Request: {
  search_id: "SEARCH-001"
}
Response: {
  search_id: "SEARCH-001",
  videos_found: [
    {
      youtube_url: "https://youtube.com/watch?v=xxxxx",
      title: "Claude AI Complete Guide",
      channel: "AI Academy",
      duration: "18:42",
      views: 125000,
      upload_date: "2025-11-28",
      thumbnail: "https://...",
      priority: 95, // автоматически рассчитанный
      description: "..."
    }
  ]
}

// POST /api/search-queue/:search_id/add-to-video-queue
// Добавить выбранные видео в Video Queue
Request: {
  search_id: "SEARCH-001",
  video_urls: [
    "https://youtube.com/watch?v=xxxxx",
    "https://youtube.com/watch?v=yyyyy"
  ]
}
Response: {
  added: 2,
  vq_ids: ["VQ-128", "VQ-129"]
}

// PUT /api/search-queue/:search_id/complete
// Завершить задачу поиска
Request: {
  search_id: "SEARCH-001",
  videos_found: 12,
  videos_added: 2,
  notes: "Found good tutorials"
}
Response: {
  status: "completed"
}
```

### 1.4 Промпты для Search Queue

#### PMT-093: YouTube Search Bookmarklet

**Назначение:** Быстрый поиск видео по теме через bookmarklet

**Использование в Search Queue:**
- Когда пользователь создаёт задачу с типом "AI Agent Social Strategy"
- Автоматически формируется YouTube search query
- Открывается в новой вкладке или встраивается в iframe

**Интеграция:**
```javascript
// При выборе PMT-093 в Search Type
const executeSearch = (searchType) => {
  if (searchType === 'PMT-093') {
    const searchUrl = 'https://www.youtube.com/results?search_query=Build+AI+Agent+Social+Strategy&sp=EgIYAg%253D%253D';
    window.open(searchUrl, '_blank');
    // ИЛИ
    showIframeModal(searchUrl);
  }
}
```

#### Research Prompts (из документации)

**PMT-048: YouTube AI Tools Daily**
- Фокус: Новые AI инструменты
- Частота: Ежедневно
- Результат: 10-15 видео
- Длительность: 10-25 минут
- Подписчики: 10K+

**PMT-089: YouTube AI Tutorials Research**
- Фокус: Комплексные туториалы
- Частота: Еженедельно
- Результат: 15-20 видео
- Длительность: 20-40 минут
- Уровень: Beginner to Intermediate

**PMT-093: Design AI Video Discovery**
- Фокус: AI дизайн инструменты
- Частота: Еженедельно
- Результат: 10-15 видео
- Инструменты: Figma AI, Midjourney, Adobe Firefly

**PMT-098: OpenAI Automation Examples**
- Фокус: AI автоматизация
- Частота: Еженедельно
- Результат: 10-15 видео
- Кейсы: API automation, Make.com, Zapier

### 1.5 Интеграция с AI для поиска

**Вариант 1: YouTube API**
```javascript
// server/src/services/youtube-search-service.js
class YouTubeSearchService {
  async searchVideos(query, filters = {}) {
    const params = {
      part: 'snippet',
      q: query,
      type: 'video',
      maxResults: filters.maxResults || 25,
      videoDuration: filters.duration || 'medium', // medium = 4-20 min
      order: 'relevance',
      relevanceLanguage: 'en'
    };

    const response = await youtube.search.list(params);

    // Получить детали видео (views, duration)
    const videoIds = response.data.items.map(item => item.id.videoId);
    const details = await youtube.videos.list({
      part: 'statistics,contentDetails',
      id: videoIds.join(',')
    });

    // Совместить данные
    return mergeVideoData(response.data.items, details.data.items);
  }
}
```

**Вариант 2: AI-assisted поиск (Perplexity/ChatGPT)**
```javascript
// server/src/services/ai-search-service.js
class AISearchService {
  async searchWithAI(topic, department) {
    const prompt = `
Find 15-20 high-quality YouTube tutorial videos about "${topic}"
for ${department} department.

Requirements:
- Videos from last 60 days
- Duration: 15-30 minutes
- Tutorial format (not news)
- English language
- High production quality
- Channels with 10K+ subscribers

For each video provide:
- Title
- YouTube URL
- Channel name
- Duration
- View count
- Upload date
- Brief description

Format as JSON array.
    `;

    const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [{ role: "user", content: prompt }]
    });

    return JSON.parse(response.choices[0].message.content);
  }
}
```

### 1.6 Локальное хранилище

**Файл:** `E:\Jobs\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\00_SEARCH_QUEUE\search_queue_local.json`

```json
{
  "last_sync": "2025-12-08T15:30:00Z",
  "tasks": [
    {
      "search_id": "SEARCH-001",
      "employee": "John Doe",
      "department": "AI",
      "topic": "AI Tools Research",
      "search_query": "Build AI Agent Social Strategy",
      "status": "Assigned",
      "date_assigned": "2025-12-08T10:00:00Z",
      "videos_found": 0,
      "videos_added_to_queue": 0,
      "date_completed": null,
      "notes": "",
      "created_at": "2025-12-08T10:00:00Z",
      "updated_at": "2025-12-08T10:00:00Z"
    }
  ]
}
```

**Синхронизация:**
```javascript
// server/src/services/search-queue-sync-service.js
class SearchQueueSyncService {
  async syncAll() {
    // 1. Загрузить из Google Sheets
    const sheetsData = await this.sheetsService.getSearchQueue();

    // 2. Загрузить из локального файла
    const localData = await this.dropboxService.readFile(
      '/00_SEARCH_QUEUE/search_queue_local.json'
    );

    // 3. Сравнить и разрешить конфликты
    const merged = this.mergeData(sheetsData, JSON.parse(localData));

    // 4. Обновить оба источника
    await this.sheetsService.updateSearchQueue(merged);
    await this.dropboxService.writeFile(
      '/00_SEARCH_QUEUE/search_queue_local.json',
      JSON.stringify(merged, null, 2)
    );

    return merged;
  }

  mergeData(sheets, local) {
    // Google Sheets = source of truth
    // Если конфликт - использовать данные из Sheets
    const merged = [...sheets];

    // Добавить элементы из local, которых нет в sheets
    local.tasks.forEach(localTask => {
      if (!merged.find(t => t.search_id === localTask.search_id)) {
        merged.push(localTask);
      }
    });

    return merged;
  }
}
```

---

## МОДУЛЬ 2: VIDEO QUEUE

### 2.1 Функционал

**Основные возможности:**
1. Просмотр очереди видео (сортировка, фильтрация)
2. Добавление видео:
   - **Ручное добавление** (пользователь вводит URL)
   - **Из Search Queue** (через модальное окно)
3. Автоматическое получение метаданных (YouTube API)
4. Расчёт приоритета (0-100 баллов)
5. Обновление статуса (Queued/Selected/In_Progress/Completed)
6. Dashboard с визуализацией
7. Экспорт в различных форматах

### 2.2 UI/UX Компоненты

#### Главная страница Video Queue

```
┌──────────────────────────────────────────────────────────────┐
│                      VIDEO QUEUE                             │
│  [+ Add Video Manually]  [Add from Search ▼]  [Export ▼]    │
│  [Filter: Status ▼] [Sort by: Priority ▼]                   │
├──────────────────────────────────────────────────────────────┤
│  📊 Stats: 128 Total | 15 Queued | 3 In Progress | 28 Done │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ VQ-128                           Priority: ⭐⭐⭐⭐⭐ (95)│  │
│  │ 🎬 Claude AI Complete Guide                          │  │
│  │ 📺 AI Academy | ⏱ 18:42 | 👁 125K views             │  │
│  │ 📅 2025-11-28 | Topic: AI Tools | Employee: John    │  │
│  │ Status: [Queued ▼] [View] [Move to Phase 1] [Edit]  │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ VQ-127                           Priority: ⭐⭐⭐⭐ (82) │  │
│  │ 🎬 Building AI Agents from Scratch                   │  │
│  │ 📺 Code Masters | ⏱ 22:15 | 👁 89K views            │  │
│  │ 📅 2025-11-27 | Topic: Development | Employee: Jane │  │
│  │ Status: [In_Progress ▼] [View] [Continue] [Edit]    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  [Load More...]                                             │
└──────────────────────────────────────────────────────────────┘
```

#### Модальное окно ручного добавления

```
┌────────────────────────────────────────────────────┐
│  Add Video Manually                       [X]      │
├────────────────────────────────────────────────────┤
│                                                     │
│  YouTube URL: *                                    │
│  [Input: https://youtube.com/watch?v=xxxxx]       │
│  [Fetch Metadata]                                  │
│                                                     │
│  ─────────────────────────────────────────────    │
│  Auto-filled from YouTube:                         │
│                                                     │
│  Title: Claude AI Complete Guide                   │
│  Channel: AI Academy                               │
│  Duration: 18:42                                   │
│  Views: 125,000                                    │
│  Upload Date: 2025-11-28                           │
│  ─────────────────────────────────────────────    │
│                                                     │
│  Topic: [Input: AI Tools]                          │
│  Employee: [Dropdown: Select ▼]                    │
│  Source: [Input: Daily Search]                     │
│  Priority: 95 (auto-calculated)                    │
│  Notes: [Textarea]                                 │
│                                                     │
│  [Cancel]                      [Add to Queue]      │
└────────────────────────────────────────────────────┘
```

#### Dashboard с метриками

```
┌──────────────────────────────────────────────────────────┐
│              VIDEO QUEUE DASHBOARD                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │   128    │ │    15    │ │    3     │ │   28     │  │
│  │  Total   │ │  Queued  │ │In Progress│ │ Complete │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Priority Distribution (Pie Chart)               │  │
│  │  ⭐⭐⭐⭐⭐ (80-100): 15 videos  (12%)              │  │
│  │  ⭐⭐⭐⭐ (60-79):   45 videos  (35%)              │  │
│  │  ⭐⭐⭐ (40-59):    50 videos  (39%)              │  │
│  │  ⭐⭐ (20-39):      15 videos  (12%)              │  │
│  │  ⭐ (0-19):         3 videos   (2%)               │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Videos by Department (Bar Chart)                │  │
│  │  AI:          42 ████████████                    │  │
│  │  Design:      28 ████████                        │  │
│  │  Development: 35 ██████████                      │  │
│  │  Video:       15 ████                            │  │
│  │  SMM:          8 ██                              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Recent Activity (Timeline)                      │  │
│  │  • VQ-128 added - 5 min ago                      │  │
│  │  • VQ-127 moved to In Progress - 15 min ago     │  │
│  │  • VQ-126 completed - 1 hour ago                 │  │
│  └──────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### 2.3 Backend API

#### Endpoints

```javascript
// GET /api/video-queue
// Получить все видео в очереди
Query params: ?status=Queued&sort=priority&order=desc&limit=50
Response: {
  videos: [
    {
      vq_id: "VQ-128",
      youtube_url: "https://youtube.com/watch?v=xxxxx",
      title: "Claude AI Complete Guide",
      channel: "AI Academy",
      duration: "18:42",
      views: 125000,
      upload_date: "2025-11-28",
      topic: "AI Tools",
      source: "Daily Search",
      employee: "John Doe",
      priority: 95,
      status: "Queued",
      date_added: "2025-12-08T14:00:00Z",
      notes: "",
      thumbnail: "https://..."
    }
  ],
  total: 128,
  stats: {
    total: 128,
    queued: 15,
    in_progress: 3,
    completed: 28
  }
}

// POST /api/video-queue/add
// Добавить видео вручную
Request: {
  youtube_url: "https://youtube.com/watch?v=xxxxx",
  employee: "John Doe",
  topic: "AI Tools",
  source: "Manual",
  notes?: ""
}
Response: {
  vq_id: "VQ-129",
  priority: 95,
  metadata: {
    title: "...",
    channel: "...",
    duration: "...",
    views: 125000,
    upload_date: "2025-11-28"
  }
}

// POST /api/video-queue/add-batch
// Добавить несколько видео (из Search Queue)
Request: {
  videos: [
    {
      youtube_url: "https://youtube.com/watch?v=xxxxx",
      employee: "John Doe",
      topic: "AI Tools",
      source: "SEARCH-001"
    }
  ]
}
Response: {
  added: 2,
  vq_ids: ["VQ-128", "VQ-129"]
}

// GET /api/video-queue/:vq_id/metadata
// Получить метаданные видео из YouTube
Response: {
  title: "Claude AI Complete Guide",
  channel: "AI Academy",
  duration: "18:42",
  views: 125000,
  upload_date: "2025-11-28",
  description: "...",
  thumbnail: "https://...",
  tags: ["AI", "Claude", "Tutorial"]
}

// PUT /api/video-queue/:vq_id/priority
// Пересчитать приоритет
Response: {
  vq_id: "VQ-128",
  old_priority: 85,
  new_priority: 95
}

// PUT /api/video-queue/:vq_id/status
// Обновить статус
Request: {
  status: "In_Progress"
}
Response: {
  vq_id: "VQ-128",
  status: "In_Progress"
}

// POST /api/video-queue/:vq_id/move-to-phase-1
// Переместить видео в Phase 1 (Transcription)
Response: {
  vq_id: "VQ-128",
  video_number: "VIDEO-029",
  status: "Moved to Phase 1"
}

// GET /api/video-queue/dashboard
// Получить данные для dashboard
Response: {
  stats: {
    total: 128,
    queued: 15,
    in_progress: 3,
    completed: 28
  },
  priority_distribution: {
    "80-100": 15,
    "60-79": 45,
    "40-59": 50,
    "20-39": 15,
    "0-19": 3
  },
  by_department: {
    "AI": 42,
    "Design": 28,
    "Development": 35,
    "Video": 15,
    "SMM": 8
  },
  recent_activity: [
    {
      vq_id: "VQ-128",
      action: "added",
      timestamp: "2025-12-08T15:25:00Z"
    }
  ]
}
```

### 2.4 Priority Calculator

**Алгоритм расчёта приоритета (0-100 баллов):**

```javascript
// server/src/services/priority-calculator.js
class PriorityCalculator {
  calculatePriority(video) {
    let score = 0;

    // 1. Views (0-25 points)
    const viewsScore = this.calculateViewsScore(video.views);
    score += viewsScore;

    // 2. Recency (0-25 points)
    const recencyScore = this.calculateRecencyScore(video.upload_date);
    score += recencyScore;

    // 3. Duration (0-20 points)
    const durationScore = this.calculateDurationScore(video.duration);
    score += durationScore;

    // 4. Channel Quality (0-15 points)
    const channelScore = this.calculateChannelScore(video.channel);
    score += channelScore;

    // 5. Topic Relevance (0-15 points)
    const topicScore = this.calculateTopicScore(video.topic, video.title);
    score += topicScore;

    return Math.round(score);
  }

  calculateViewsScore(views) {
    // 0-10K = 0-5 points
    // 10K-50K = 5-10 points
    // 50K-100K = 10-15 points
    // 100K-500K = 15-20 points
    // 500K+ = 20-25 points
    if (views < 10000) return (views / 10000) * 5;
    if (views < 50000) return 5 + ((views - 10000) / 40000) * 5;
    if (views < 100000) return 10 + ((views - 50000) / 50000) * 5;
    if (views < 500000) return 15 + ((views - 100000) / 400000) * 5;
    return 25;
  }

  calculateRecencyScore(uploadDate) {
    const daysAgo = Math.floor((Date.now() - new Date(uploadDate)) / (1000 * 60 * 60 * 24));

    // 0-7 days = 25 points
    // 8-14 days = 20 points
    // 15-30 days = 15 points
    // 31-60 days = 10 points
    // 61-90 days = 5 points
    // 90+ days = 0 points
    if (daysAgo <= 7) return 25;
    if (daysAgo <= 14) return 20;
    if (daysAgo <= 30) return 15;
    if (daysAgo <= 60) return 10;
    if (daysAgo <= 90) return 5;
    return 0;
  }

  calculateDurationScore(duration) {
    const minutes = this.parseDuration(duration);

    // 10-20 min = 20 points (ideal)
    // 20-30 min = 15 points
    // 30-40 min = 10 points
    // 5-10 min = 10 points
    // <5 min or >40 min = 5 points
    if (minutes >= 10 && minutes <= 20) return 20;
    if (minutes > 20 && minutes <= 30) return 15;
    if (minutes > 30 && minutes <= 40) return 10;
    if (minutes >= 5 && minutes < 10) return 10;
    return 5;
  }

  calculateChannelScore(channel) {
    // Здесь можно добавить whitelist известных качественных каналов
    // Или анализировать подписчиков через YouTube API
    // Пока упрощённая версия
    return 10; // базовый балл
  }

  calculateTopicScore(topic, title) {
    // Анализ релевантности топика в заголовке
    const topicWords = topic.toLowerCase().split(' ');
    const titleLower = title.toLowerCase();

    let matches = 0;
    topicWords.forEach(word => {
      if (titleLower.includes(word)) matches++;
    });

    return (matches / topicWords.length) * 15;
  }

  parseDuration(duration) {
    // "18:42" -> 18.7 minutes
    const parts = duration.split(':');
    if (parts.length === 2) {
      return parseInt(parts[0]) + parseInt(parts[1]) / 60;
    }
    // "1:18:42" -> 78.7 minutes
    if (parts.length === 3) {
      return parseInt(parts[0]) * 60 + parseInt(parts[1]) + parseInt(parts[2]) / 60;
    }
    return 0;
  }
}
```

### 2.5 YouTube Metadata Service

```javascript
// server/src/services/youtube-service.js
const { google } = require('googleapis');

class YouTubeService {
  constructor() {
    this.youtube = google.youtube({
      version: 'v3',
      auth: process.env.YOUTUBE_API_KEY
    });
  }

  async getVideoMetadata(videoUrl) {
    // Извлечь video ID из URL
    const videoId = this.extractVideoId(videoUrl);

    // Получить метаданные
    const response = await this.youtube.videos.list({
      part: 'snippet,statistics,contentDetails',
      id: videoId
    });

    if (response.data.items.length === 0) {
      throw new Error('Video not found');
    }

    const video = response.data.items[0];

    return {
      title: video.snippet.title,
      channel: video.snippet.channelTitle,
      description: video.snippet.description,
      upload_date: video.snippet.publishedAt,
      duration: this.formatDuration(video.contentDetails.duration),
      views: parseInt(video.statistics.viewCount),
      likes: parseInt(video.statistics.likeCount),
      thumbnail: video.snippet.thumbnails.high.url,
      tags: video.snippet.tags || []
    };
  }

  extractVideoId(url) {
    // https://youtube.com/watch?v=xxxxx -> xxxxx
    // https://youtu.be/xxxxx -> xxxxx
    const regex = /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&]+)/;
    const match = url.match(regex);
    return match ? match[1] : null;
  }

  formatDuration(isoDuration) {
    // PT18M42S -> 18:42
    // PT1H18M42S -> 1:18:42
    const match = isoDuration.match(/PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/);
    const hours = match[1] || 0;
    const minutes = match[2] || 0;
    const seconds = match[3] || 0;

    if (hours > 0) {
      return `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  }
}
```

### 2.6 Локальное хранилище

**Файл:** `E:\Jobs\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\01_VIDEO_QUEUE\video_queue_local.json`

```json
{
  "last_sync": "2025-12-08T15:45:00Z",
  "videos": [
    {
      "vq_id": "VQ-128",
      "youtube_url": "https://youtube.com/watch?v=xxxxx",
      "title": "Claude AI Complete Guide",
      "channel": "AI Academy",
      "duration": "18:42",
      "views": 125000,
      "upload_date": "2025-11-28",
      "topic": "AI Tools",
      "source": "SEARCH-001",
      "employee": "John Doe",
      "priority": 95,
      "status": "Queued",
      "date_added": "2025-12-08T14:00:00Z",
      "notes": "",
      "thumbnail": "https://...",
      "created_at": "2025-12-08T14:00:00Z",
      "updated_at": "2025-12-08T14:00:00Z"
    }
  ]
}
```

---

## ПРОМПТЫ ДЛЯ МОДУЛЕЙ

### Категории промптов

#### 1. Для Search Queue (Phase 0)

**PMT-093: YouTube Search Bookmarklet**
- **Файл:** `E:\Jobs\REMS\Dropbox\ENTITIES\PROMPTS\PMT-093_YouTube_Search_Bookmarklet.md`
- **Назначение:** Быстрый поиск "AI Agent Social Strategy"
- **Применение:** При создании search task типа "AI Social Agents"
- **Результат:** Открывает YouTube с фильтром >20 минут

**Research Prompts (из документации v2/08_PROMPTS_REFERENCE.md):**

1. **PMT-048: YouTube AI Tools Daily**
   - Ежедневный поиск новых AI инструментов
   - Фокус: Launches, updates, tutorials
   - Длительность видео: 10-25 минут
   - Каналы: 10K+ подписчиков
   - Результат: 10-15 видео

2. **PMT-089: YouTube AI Tutorials Research**
   - Еженедельный поиск туториалов
   - Фокус: Complete guides, step-by-step, projects
   - Длительность: 20-40 минут
   - Уровень: Beginner to Intermediate
   - Результат: 15-20 видео

3. **PMT-093: Design AI Video Discovery**
   - Еженедельный поиск дизайн-инструментов
   - Фокус: Figma AI, Midjourney, Adobe Firefly
   - Аудитория: UI/UX Designers
   - Результат: 10-15 видео

4. **PMT-098: OpenAI Automation Examples**
   - Еженедельный поиск автоматизации
   - Фокус: API workflows, Make.com, Zapier
   - Кейсы: Customer support, content generation
   - Результат: 10-15 видео

**Department-Specific Research Prompts:**
- PMT-044: HR Department Research (monthly)
- PMT-045: Sales Department Research (monthly)
- PMT-046: SMM Department Research (monthly)
- PMT-047: Design Department Research (weekly)
- PMT-048: Development Department Research (weekly)
- PMT-049: Marketing Department Research (monthly)
- PMT-050: Operations Department Research (monthly)
- PMT-051: Finance Department Research (quarterly)
- PMT-052: Legal Department Research (quarterly)

#### 2. Для Video Queue (Phase 0→1)

**PMT-090: YouTube Video Processing**
- **Файл:** `E:\Jobs\REMS\Dropbox\ENTITIES\PROMPTS\PMT-090_YouTube_Video_Processing.md`
- **Назначение:** Обработка видео с custom instructions
- **Платформа:** AI Studio (Google Gemini)
- **Применение:** При переходе video из queue в Phase 1

**PMT-004: Video Transcription v4.1**
- **Файл:** `E:\Jobs\REMS\Dropbox\ENTITIES\PROMPTS\PMT-004_Video_Transcription_v4.1.md`
- **Назначение:** AI-assisted транскрипция с экстракцией 37+ сущностей
- **Применение:** Phase 1 (Transcription)
- **Результат:** `Video_XXX.md` с полной транскрипцией

### Интеграция промптов в UI

#### Search Type Dropdown

```javascript
const searchTypes = [
  {
    id: 'PMT-048',
    name: 'Daily AI Tools',
    description: 'New AI tool launches and updates',
    frequency: 'Daily',
    expectedResults: '10-15 videos',
    prompt: require('./prompts/PMT-048_YouTube_AI_Tools_Daily.md')
  },
  {
    id: 'PMT-089',
    name: 'Weekly Tutorials',
    description: 'Comprehensive AI tutorial series',
    frequency: 'Weekly',
    expectedResults: '15-20 videos',
    prompt: require('./prompts/PMT-089_YouTube_AI_Tutorials_Research.md')
  },
  {
    id: 'PMT-093',
    name: 'Design AI Tools',
    description: 'AI design tool videos (Figma, Midjourney)',
    frequency: 'Weekly',
    expectedResults: '10-15 videos',
    prompt: require('./prompts/PMT-093_Design_AI_Video_Discovery.md')
  },
  {
    id: 'PMT-098',
    name: 'Automation Examples',
    description: 'AI automation workflows',
    frequency: 'Weekly',
    expectedResults: '10-15 videos',
    prompt: require('./prompts/PMT-098_OpenAI_Automation_Examples.md')
  },
  {
    id: 'CUSTOM',
    name: 'Custom Search',
    description: 'Enter your own search query',
    frequency: 'On-demand',
    expectedResults: 'Variable',
    prompt: null
  }
];
```

#### Execute Search Flow

```javascript
const executeSearch = async (searchTask) => {
  const { search_type, custom_query } = searchTask;

  if (search_type === 'CUSTOM') {
    // Выполнить custom query
    return await youtubeSearchService.searchVideos(custom_query);
  }

  // Загрузить prompt для выбранного типа
  const promptConfig = searchTypes.find(t => t.id === search_type);

  // Вариант 1: YouTube API поиск
  const videos = await youtubeSearchService.searchVideos(
    promptConfig.searchQuery,
    promptConfig.filters
  );

  // Вариант 2: AI-assisted поиск
  // const videos = await aiSearchService.searchWithAI(
  //   promptConfig.description,
  //   searchTask.department
  // );

  // Рассчитать приоритет для каждого видео
  videos.forEach(video => {
    video.priority = priorityCalculator.calculatePriority(video);
  });

  // Сортировать по приоритету
  videos.sort((a, b) => b.priority - a.priority);

  return videos;
};
```

---

## UI/UX ДИЗАЙН

### Дизайн-система

**Цветовая схема (на основе shadcn/ui):**
```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;

  --primary: 221.2 83.2% 53.3%;
  --primary-foreground: 210 40% 98%;

  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;

  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;

  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;

  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 221.2 83.2% 53.3%;
}
```

**Компоненты shadcn/ui для использования:**
- `Card` - карточки видео, search tasks
- `Button` - все кнопки
- `Badge` - статусы, приоритеты
- `Dialog` - модальные окна
- `Select` - dropdown меню
- `Input` - поля ввода
- `Textarea` - многострочные поля
- `Table` - таблицы (опционально)
- `Tabs` - переключение между модулями
- `Progress` - индикаторы прогресса

### Priority Badge Component

```tsx
// src/components/ui/PriorityBadge.tsx
import { Badge } from '@/components/ui/badge';

interface PriorityBadgeProps {
  priority: number;
}

export const PriorityBadge: React.FC<PriorityBadgeProps> = ({ priority }) => {
  const getStars = (priority: number) => {
    if (priority >= 80) return '⭐⭐⭐⭐⭐';
    if (priority >= 60) return '⭐⭐⭐⭐';
    if (priority >= 40) return '⭐⭐⭐';
    if (priority >= 20) return '⭐⭐';
    return '⭐';
  };

  const getVariant = (priority: number) => {
    if (priority >= 80) return 'destructive'; // red/urgent
    if (priority >= 60) return 'default'; // blue
    if (priority >= 40) return 'secondary'; // gray
    return 'outline';
  };

  return (
    <Badge variant={getVariant(priority)}>
      {getStars(priority)} ({priority})
    </Badge>
  );
};
```

### Status Badge Component

```tsx
// src/components/ui/StatusBadge.tsx
import { Badge } from '@/components/ui/badge';

interface StatusBadgeProps {
  status: 'Assigned' | 'In_Progress' | 'Completed' | 'Queued' | 'Selected';
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status }) => {
  const getVariant = (status: string) => {
    switch (status) {
      case 'Completed': return 'success'; // green
      case 'In_Progress': return 'warning'; // yellow
      case 'Assigned':
      case 'Queued': return 'secondary'; // gray
      case 'Selected': return 'default'; // blue
      default: return 'outline';
    }
  };

  return (
    <Badge variant={getVariant(status)}>
      {status}
    </Badge>
  );
};
```

### Responsive Design

**Breakpoints:**
```css
/* Mobile */
@media (max-width: 640px) {
  /* Stack cards vertically */
}

/* Tablet */
@media (min-width: 641px) and (max-width: 1024px) {
  /* 2 columns */
}

/* Desktop */
@media (min-width: 1025px) {
  /* 3+ columns, full dashboard */
}
```

---

## ИНТЕГРАЦИЯ С ЛОКАЛЬНЫМИ ФАЙЛАМИ

### Структура файлов

```
E:\Jobs\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\
├── 00_SEARCH_QUEUE/
│   ├── search_queue_local.json         ← Backup search tasks
│   └── README.md
├── 01_VIDEO_QUEUE/
│   ├── video_queue_local.json          ← Backup video queue
│   └── README.md
└── documentation/
```

### Sync Service

```javascript
// server/src/services/dropbox-sync-service.js
class DropboxSyncService {
  constructor(dropboxService, sheetsService) {
    this.dropbox = dropboxService;
    this.sheets = sheetsService;
    this.basePath = '/ENTITIES/TASK_MANAGERS/RESEARCHES';
  }

  async syncSearchQueue() {
    try {
      // 1. Получить данные из Google Sheets
      const sheetsData = await this.sheets.getSearchQueue();

      // 2. Получить данные из локального файла
      const localPath = `${this.basePath}/00_SEARCH_QUEUE/search_queue_local.json`;
      let localData = { tasks: [] };
      try {
        const content = await this.dropbox.readFile(localPath);
        localData = JSON.parse(content);
      } catch (err) {
        console.log('Local file not found, creating new');
      }

      // 3. Merge данных (Sheets = source of truth)
      const merged = this.mergeSearchQueueData(sheetsData, localData.tasks);

      // 4. Обновить локальный файл
      const updatedLocal = {
        last_sync: new Date().toISOString(),
        tasks: merged
      };
      await this.dropbox.writeFile(localPath, JSON.stringify(updatedLocal, null, 2));

      // 5. Обновить Sheets (если были новые задачи в local)
      const newTasks = merged.filter(t =>
        !sheetsData.find(s => s.search_id === t.search_id)
      );
      if (newTasks.length > 0) {
        for (const task of newTasks) {
          await this.sheets.addSearchTask(task);
        }
      }

      return merged;
    } catch (error) {
      console.error('Sync error:', error);
      throw error;
    }
  }

  async syncVideoQueue() {
    // Аналогично syncSearchQueue()
  }

  mergeSearchQueueData(sheetsData, localData) {
    const merged = [...sheetsData];

    // Добавить задачи из local, которых нет в sheets
    localData.forEach(localTask => {
      if (!merged.find(t => t.search_id === localTask.search_id)) {
        merged.push(localTask);
      } else {
        // Обновить timestamps если local новее
        const existing = merged.find(t => t.search_id === localTask.search_id);
        if (new Date(localTask.updated_at) > new Date(existing.updated_at)) {
          Object.assign(existing, localTask);
        }
      }
    });

    return merged;
  }

  // Автоматическая синхронизация каждые 5 минут
  startAutoSync() {
    setInterval(async () => {
      await this.syncSearchQueue();
      await this.syncVideoQueue();
      console.log('Auto-sync completed:', new Date().toISOString());
    }, 5 * 60 * 1000); // 5 minutes
  }
}
```

### Сканирование при запуске

```javascript
// server/src/app.js
const startServer = async () => {
  // 1. Инициализация сервисов
  const dropboxService = new DropboxService();
  const sheetsService = new SheetsService();
  const syncService = new DropboxSyncService(dropboxService, sheetsService);

  // 2. Первичная синхронизация
  console.log('Starting initial sync...');
  await syncService.syncSearchQueue();
  await syncService.syncVideoQueue();
  console.log('Initial sync completed');

  // 3. Запуск автоматической синхронизации
  syncService.startAutoSync();

  // 4. Запуск сервера
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
};

startServer();
```

---

## ТЕХНИЧЕСКИЕ ДЕТАЛИ

### Технологический стек

**Frontend:**
- React 18 + TypeScript
- Tailwind CSS 3
- shadcn/ui components
- React Query (data fetching, caching)
- Zustand (state management)
- React Router v6

**Backend:**
- Node.js 18+ + Express 4
- Google Sheets API
- Dropbox API
- YouTube Data API v3
- OpenAI/Claude API (optional для AI search)

### Файловая структура

```
researches-app/
├── client/                          # Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/                  # shadcn/ui
│   │   │   ├── search-queue/
│   │   │   │   ├── SearchQueueDashboard.tsx
│   │   │   │   ├── CreateSearchTaskModal.tsx
│   │   │   │   ├── SearchResultsModal.tsx
│   │   │   │   └── SearchTaskCard.tsx
│   │   │   ├── video-queue/
│   │   │   │   ├── VideoQueueDashboard.tsx
│   │   │   │   ├── AddVideoModal.tsx
│   │   │   │   ├── VideoCard.tsx
│   │   │   │   ├── PriorityBadge.tsx
│   │   │   │   ├── StatusBadge.tsx
│   │   │   │   └── VideoQueueStats.tsx
│   │   │   └── common/
│   │   │       ├── Navigation.tsx
│   │   │       └── Layout.tsx
│   │   ├── pages/
│   │   │   ├── SearchQueuePage.tsx
│   │   │   ├── VideoQueuePage.tsx
│   │   │   └── DashboardPage.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── searchQueueApi.ts
│   │   │   └── videoQueueApi.ts
│   │   ├── hooks/
│   │   │   ├── useSearchQueue.ts
│   │   │   └── useVideoQueue.ts
│   │   ├── store/
│   │   │   └── store.ts
│   │   └── App.tsx
│   └── package.json
│
├── server/                          # Backend
│   ├── src/
│   │   ├── routes/
│   │   │   ├── search-queue.js
│   │   │   └── video-queue.js
│   │   ├── services/
│   │   │   ├── dropbox-service.js
│   │   │   ├── sheets-service.js
│   │   │   ├── youtube-service.js
│   │   │   ├── priority-calculator.js
│   │   │   ├── dropbox-sync-service.js
│   │   │   ├── id-generator.js
│   │   │   └── ai-search-service.js (optional)
│   │   ├── utils/
│   │   │   ├── logger.js
│   │   │   └── validators.js
│   │   └── app.js
│   ├── config/
│   │   └── config.js
│   ├── .env
│   └── package.json
│
└── README.md
```

### API Credentials

**Необходимые ключи:**
1. **Dropbox Access Token**
   - Создать Dropbox App: https://www.dropbox.com/developers/apps
   - Full Dropbox access
   - Generate access token

2. **Google Sheets API**
   - Google Cloud Console
   - Enable Google Sheets API
   - Create Service Account
   - Download credentials.json

3. **YouTube Data API v3**
   - Google Cloud Console
   - Enable YouTube Data API v3
   - Create API Key

4. **OpenAI API (optional)**
   - https://platform.openai.com/

**.env файл:**
```bash
# Server
PORT=5000
NODE_ENV=development

# Dropbox
DROPBOX_ACCESS_TOKEN=your_dropbox_token

# Google Sheets
GOOGLE_SHEETS_CREDENTIALS_PATH=./config/google-credentials.json
SPREADSHEET_ID=your_spreadsheet_id

# YouTube
YOUTUBE_API_KEY=your_youtube_api_key

# AI (optional)
OPENAI_API_KEY=your_openai_key

# Frontend URL
CLIENT_URL=http://localhost:3000
```

### Оценка времени разработки

**Search Queue Module:**
- Backend API: 8-10 часов
- Frontend UI: 10-12 часов
- Промпт интеграция: 4-5 часов
- Тестирование: 5-6 часов
- **Итого: 27-33 часа**

**Video Queue Module:**
- Backend API: 10-12 часов
- Priority Calculator: 4-5 часов
- YouTube Service: 4-5 часов
- Frontend UI: 12-15 часов
- Dashboard: 6-8 часов
- Тестирование: 6-8 часов
- **Итого: 42-53 часа**

**Интеграция и синхронизация:**
- Dropbox Sync Service: 6-8 часов
- Локальное хранилище: 4-5 часов
- Google Sheets интеграция: 6-8 часов
- **Итого: 16-21 час**

**ОБЩЕЕ ВРЕМЯ: 85-107 часов (11-14 рабочих дней)**

---

## СЛЕДУЮЩИЕ ШАГИ

### Этап 1: Подготовка (1-2 дня)
1. ✅ Создать GitHub репозиторий
2. ✅ Получить все API credentials
3. ✅ Настроить Google Sheets (4 листа)
4. ✅ Инициализировать проекты (client + server)
5. ✅ Установить зависимости

### Этап 2: Backend (3-4 дня)
1. ✅ Реализовать core services
   - DropboxService
   - SheetsService
   - YouTubeService
   - IDGenerator
2. ✅ Реализовать Search Queue API
3. ✅ Реализовать Video Queue API
4. ✅ Реализовать Priority Calculator
5. ✅ Реализовать Sync Service
6. ✅ Тестирование API

### Этап 3: Frontend (4-5 дней)
1. ✅ Настроить React + Tailwind + shadcn/ui
2. ✅ Реализовать Search Queue UI
   - Dashboard
   - Create Task Modal
   - Search Results Modal
3. ✅ Реализовать Video Queue UI
   - Dashboard
   - Add Video Modal
   - Video Cards
   - Stats Dashboard
4. ✅ Интеграция с API
5. ✅ Тестирование UI

### Этап 4: Интеграция (2-3 дня)
1. ✅ Настроить промпты
2. ✅ Интегрировать поиск видео
3. ✅ Интегрировать локальные файлы
4. ✅ End-to-end тестирование
5. ✅ Bug fixing
6. ✅ Documentation

---

## ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ (FUTURE ENHANCEMENTS)

### Phase 2 Enhancements
- Bulk operations (массовое добавление, обновление)
- Advanced filters (по дате, каналу, длительности)
- Saved searches (сохранённые поисковые запросы)
- Email notifications (уведомления о новых видео)
- Analytics dashboard (детальная аналитика)
- Export to multiple formats (CSV, JSON, Markdown, PDF)
- Calendar view (календарное представление)
- Kanban board (drag & drop между статусами)

### AI Enhancements
- AI-powered video summarization
- Automatic tagging
- Content similarity detection
- Duplicate detection
- Smart recommendations

### Collaboration Features
- Comments on tasks/videos
- Assignments history
- Activity log
- Team performance metrics

---

**Конец детального плана**

*Дата создания: 2025-12-08*
*Автор: Claude (Anthropic)*
*Статус: Ready for Development ✅*
