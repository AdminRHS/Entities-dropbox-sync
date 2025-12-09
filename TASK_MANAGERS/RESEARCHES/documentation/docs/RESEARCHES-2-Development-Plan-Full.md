# План разработки приложения RESEARCHES 2 - Простая версия

**Дата создания:** 2025-12-08
**Статус:** Готов к утверждению
**Версия:** 2.0 (Simplified)

---

## ЭТАП 0: ДОКУМЕНТАЦИЯ И АРХИТЕКТУРА ПРИЛОЖЕНИЯ

### 0.1 Описание системы

**RESEARCHES 2** - это веб-приложение для управления обработкой видеоконтента и интеграции извлеченных знаний в таксономическую систему. Система обрабатывает YouTube видео через 7-фазный workflow, используя Dropbox для хранения файлов и Google Sheets для данных.

### 0.2 Основные модули системы

**Модуль 1: Search Queue**
- Управление поисковыми заданиями
- Назначение задач сотрудникам (SEARCH-XXX)
- Отслеживание найденных видео
- Хранение: Google Sheets

**Модуль 2: Video Queue**
- Приоритизация видео (0-100 баллов)
- Управление очередью
- Метаданные из YouTube API
- Хранение: Google Sheets

**Модуль 3: Transcriptions**
- AI-assisted транскрипция
- Извлечение 37+ сущностей (7 типов)
- Хранение: Dropbox (markdown файлы)

**Модуль 4: Analysis**
- Phase 2: Экстракция (углубленный анализ)
- Phase 3: Gap анализ (сравнение с библиотекой)
- Phase 5: Финальное картирование
- Хранение: Dropbox (markdown отчёты)

**Модуль 5: Integration**
- Создание JSON для сущностей
- Cross-references
- Хранение: Dropbox (JSON файлы)

**Модуль 6: Taxonomy**
- Просмотр всех сущностей
- Поиск и фильтрация
- Визуализация связей
- Источник: Dropbox JSON files

### 0.3 Единая система ID

**Формат ID:** `{PREFIX}-{NUMBER}`

**Префиксы:**
```
SEARCH-XXX    - Поисковые задания (001, 002, ...)
VQ-XXX        - Видео в очереди (001, 002, ...)
VIDEO-XXX     - Обработанные видео (001-028)
WRF-XXX       - Workflows
TOL-XXX       - Tools
OBJ-XXX       - Objects
ACT-XXX       - Actions
PRF-XXX       - Professions
SKL-XXX       - Skills
DPT-XXX       - Departments
```

**Генерация ID:**
- Автоматическая последовательная нумерация
- Сканирование существующих ID в Dropbox/Sheets
- Вычисление следующего доступного номера
- Формат: всегда 3 цифры с ведущими нулями

**Примеры:**
- SEARCH-001, SEARCH-002, ..., SEARCH-042
- VQ-001, VQ-002, ..., VQ-128
- VIDEO-001, VIDEO-002, ..., VIDEO-028
- WRF-001, WRF-412
- TOL-001, TOL-342

### 0.4 Технологический стек

**Frontend:**
- React.js 18+
- Tailwind CSS 3+
- shadcn/ui components
- React Query (data fetching)
- Zustand (state management)
- React Router v6

**Backend:**
- Node.js 18+
- Express.js 4+
- Dropbox API (file storage)
- Google Sheets API (structured data)
- YouTube Data API v3 (metadata)
- OpenAI API / Anthropic Claude API (AI processing)

**Data Storage:**
- **Google Sheets:**
  - Search_Queue_Master (поисковые задания)
  - Video_Queue_Master (очередь видео)
  - Video_Progress_Tracker (прогресс обработки)
  - Integration_Log (лог интеграций)
- **Dropbox:**
  - /02_TRANSCRIPTIONS/ (markdown файлы)
  - /03_ANALYSIS/ (отчёты анализа)
  - /ENTITIES/LIBRARIES/ (JSON файлы сущностей)
  - /PROMPTS/ (prompt templates)

**No Database:** Вся информация хранится в Google Sheets + Dropbox
**No Auth:** Приложение без авторизации (простая версия)

### 0.5 Архитектура приложения

**Frontend Structure:**
```
researches-app/
├── src/
│   ├── components/
│   │   ├── ui/ (shadcn/ui components)
│   │   ├── search-queue/
│   │   ├── video-queue/
│   │   ├── transcriptions/
│   │   ├── analysis/
│   │   ├── integration/
│   │   ├── taxonomy/
│   │   └── dashboard/
│   ├── pages/
│   ├── services/
│   │   ├── api.ts
│   │   ├── dropbox.ts
│   │   ├── sheets.ts
│   │   └── youtube.ts
│   ├── hooks/
│   ├── store/
│   ├── utils/
│   └── App.tsx
├── public/
└── package.json
```

**Backend Structure:**
```
server/
├── src/
│   ├── routes/
│   │   ├── search-queue.js
│   │   ├── video-queue.js
│   │   ├── transcriptions.js
│   │   ├── analysis.js
│   │   ├── integration.js
│   │   ├── taxonomy.js
│   │   └── progress.js
│   ├── services/
│   │   ├── dropbox-service.js
│   │   ├── sheets-service.js
│   │   ├── youtube-service.js
│   │   ├── ai-service.js
│   │   ├── id-generator.js
│   │   └── priority-calculator.js
│   ├── utils/
│   └── app.js
├── config/
│   └── config.js
└── package.json
```

**Data Flow:**
```
Frontend → Express API → Dropbox API / Google Sheets API
                    ↓
              YouTube API (metadata)
              AI API (processing)
```

### 0.6 Workflow процесса

**7-Phase Workflow:**
```
Phase 0: Search Queue
  ↓ (Google Sheets: Search_Queue_Master)
Phase 0→1: Video Queue
  ↓ (Google Sheets: Video_Queue_Master)
Phase 1: Transcription
  ↓ (Dropbox: 02_TRANSCRIPTIONS/Video_XXX.md)
Phase 2: Extraction
  ↓ (Dropbox: 03_ANALYSIS/Extractions/)
Phase 3: Gap Analysis
  ↓ (Dropbox: 03_ANALYSIS/Gap_Analysis/)
Phase 4: Integration
  ↓ (Dropbox: ENTITIES/LIBRARIES/*.json)
Phase 5: Mapping
  ↓ (Dropbox: 03_ANALYSIS/Library_Mapping/)
Complete ✓
  (Google Sheets: Video_Progress_Tracker)
```

### 0.7 Google Sheets структура

**Sheet 1: Search_Queue_Master**
```
Columns:
- search_id (SEARCH-XXX)
- employee
- department
- topic
- search_query
- status (Assigned/Completed)
- date_assigned
- videos_found
- date_completed
- notes
```

**Sheet 2: Video_Queue_Master**
```
Columns:
- vq_id (VQ-XXX)
- youtube_url
- title
- channel
- duration
- views
- upload_date
- topic
- source
- employee
- priority (0-100)
- status (Queued/Selected/In_Progress/Completed)
- date_added
- notes
```

**Sheet 3: Video_Progress_Tracker**
```
Columns:
- video_number (VIDEO-XXX)
- title
- youtube_url
- employee
- status (Phase_0/Phase_1/.../Complete)
- phase_0_date
- phase_1_date
- phase_2_date
- phase_3_date
- phase_4_date
- phase_5_date
- complete_date
- total_days
- notes
```

**Sheet 4: Integration_Log**
```
Columns:
- log_id
- video_number
- entity_type
- entity_id
- action (CREATE/UPDATE)
- file_path
- timestamp
- status
- notes
```

### 0.8 Dropbox структура

**Директории:**
```
/ENTITIES/TASK_MANAGERS/RESEARCHES 2/
├── 00_SEARCH_QUEUE/
│   └── (metadata, не используется в веб-версии)
├── 01_VIDEO_QUEUE/
│   └── (metadata, не используется в веб-версии)
├── 02_TRANSCRIPTIONS/
│   ├── Video_001.md
│   ├── Video_002.md
│   └── ...
├── 03_ANALYSIS/
│   ├── Extractions/
│   ├── Gap_Analysis/
│   └── Library_Mapping/
├── 04_INTEGRATION/
│   └── (metadata)
├── PROMPTS/
│   ├── PMT-004_Video_Transcription_v4.1.md
│   ├── PMT-007_Objects_Library_Extraction.md
│   └── PMT-009_*.md
└── documentation/

/ENTITIES/LIBRARIES/
├── TOOLS/
│   └── TOL-XXX.json
├── WORKFLOWS/
│   └── WRF-XXX.json
├── OBJECTS/
│   └── OBJ-XXX.json
├── ACTIONS/
│   └── ACT-XXX.json
├── PROFESSIONS/
│   └── PRF-XXX.json
├── SKILLS/
│   └── SKL-XXX.json
└── DEPARTMENTS/
    └── DPT-XXX.json
```

### 0.9 Ключевые функции

**Search Queue:**
- Создание новой задачи (SEARCH-XXX)
- Просмотр всех задач
- Завершение задачи с результатами
- Статистика по сотрудникам

**Video Queue:**
- Добавление видео (full/simple mode)
- Автоматическое получение метаданных (YouTube API)
- Расчёт приоритета (алгоритм)
- Обновление статуса
- Сортировка и фильтрация
- Dashboard с визуализацией

**Transcriptions:**
- AI-assisted транскрипция (PMT-004)
- Редактор markdown с preview
- Извлечение 37+ сущностей
- Валидация (минимум 37)
- Сохранение в Dropbox

**Analysis:**
- Phase 2: Автоматическая экстракция (PMT-007)
- Phase 3: Gap analysis (сравнение с LIBRARIES)
- Phase 5: Генерация финального отчёта
- Визуализация результатов

**Integration:**
- Создание JSON для NEW entities
- Обновление EXISTING entities
- Валидация JSON schemas
- Запись в Integration_Log

**Taxonomy:**
- Просмотр всех сущностей
- Поиск по типу/названию
- Детальная информация
- Визуализация связей (graph view)

---

## ЭТАП 1: ПОДГОТОВКА И ИНФРАСТРУКТУРА

### 1.1 Настройка окружения разработки

**Backend (Node.js + Express):**
```bash
# Инициализация проекта
mkdir researches-app && cd researches-app
mkdir server && cd server
npm init -y

# Установка зависимостей
npm install express cors dotenv
npm install googleapis dropbox-v2-api axios
npm install --save-dev nodemon
```

**Frontend (React + Tailwind + shadcn/ui):**
```bash
# Создание React app
npx create-react-app client
cd client

# Установка Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Установка shadcn/ui
npx shadcn-ui@latest init

# Установка дополнительных библиотек
npm install react-query zustand react-router-dom axios
```

**Время:** 1-2 часа

### 1.2 Структура проекта

**Полная структура:**
```
researches-app/
├── server/                          # Backend (Node.js + Express)
│   ├── src/
│   │   ├── routes/
│   │   │   ├── search-queue.js
│   │   │   ├── video-queue.js
│   │   │   ├── transcriptions.js
│   │   │   ├── analysis.js
│   │   │   ├── integration.js
│   │   │   ├── taxonomy.js
│   │   │   └── progress.js
│   │   ├── services/
│   │   │   ├── dropbox-service.js    # Dropbox API integration
│   │   │   ├── sheets-service.js     # Google Sheets API
│   │   │   ├── youtube-service.js    # YouTube Data API v3
│   │   │   ├── ai-service.js         # OpenAI/Claude API
│   │   │   ├── id-generator.js       # Unified ID generator
│   │   │   └── priority-calculator.js
│   │   ├── utils/
│   │   │   ├── logger.js
│   │   │   ├── validators.js
│   │   │   └── helpers.js
│   │   └── app.js
│   ├── config/
│   │   ├── config.js
│   │   ├── dropbox.js
│   │   ├── sheets.js
│   │   └── apis.js
│   ├── .env
│   ├── .gitignore
│   └── package.json
│
├── client/                          # Frontend (React + Tailwind)
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/                  # shadcn/ui components
│   │   │   ├── search-queue/
│   │   │   ├── video-queue/
│   │   │   ├── transcriptions/
│   │   │   ├── analysis/
│   │   │   ├── integration/
│   │   │   ├── taxonomy/
│   │   │   └── dashboard/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── SearchQueue.tsx
│   │   │   ├── VideoQueue.tsx
│   │   │   ├── Transcriptions.tsx
│   │   │   ├── Analysis.tsx
│   │   │   ├── Integration.tsx
│   │   │   └── Taxonomy.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── search-queue-api.ts
│   │   │   ├── video-queue-api.ts
│   │   │   ├── transcription-api.ts
│   │   │   ├── analysis-api.ts
│   │   │   ├── integration-api.ts
│   │   │   └── taxonomy-api.ts
│   │   ├── hooks/
│   │   │   ├── useSearchQueue.ts
│   │   │   ├── useVideoQueue.ts
│   │   │   └── useTaxonomy.ts
│   │   ├── store/
│   │   │   └── store.ts             # Zustand store
│   │   ├── utils/
│   │   │   ├── helpers.ts
│   │   │   └── constants.ts
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── tailwind.config.js
│   ├── components.json              # shadcn/ui config
│   └── package.json
│
├── .gitignore
└── README.md
```

**Время:** 2-3 часа

### 1.3 API Credentials Setup

**Необходимые API keys:**

**1. Dropbox API:**
- Создать Dropbox App: https://www.dropbox.com/developers/apps
- Получить Access Token
- Настроить разрешения (files.content.read, files.content.write)

**2. Google Sheets API:**
- Создать проект в Google Cloud Console
- Включить Google Sheets API
- Создать Service Account
- Получить credentials.json

**3. YouTube Data API v3:**
- Google Cloud Console → Enable YouTube Data API v3
- Получить API Key

**4. OpenAI API (опционально):**
- Получить API key: https://platform.openai.com/

**5. Anthropic Claude API (опционально):**
- Получить API key: https://www.anthropic.com/

**Файл .env:**
```bash
# Server configuration
PORT=5000
NODE_ENV=development

# Dropbox
DROPBOX_ACCESS_TOKEN=your_dropbox_token

# Google Sheets
GOOGLE_SHEETS_CREDENTIALS_PATH=./config/google-credentials.json
SPREADSHEET_ID=your_spreadsheet_id

# YouTube
YOUTUBE_API_KEY=your_youtube_api_key

# AI APIs
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key

# Frontend URL
CLIENT_URL=http://localhost:3000
```

**Время:** 2-3 часа

### 1.4 Базовая конфигурация сервера

**server/src/app.js:**
```javascript
const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();

const app = express();

// Middleware
app.use(cors({ origin: process.env.CLIENT_URL }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/search-queue', require('./routes/search-queue'));
app.use('/api/video-queue', require('./routes/video-queue'));
app.use('/api/transcriptions', require('./routes/transcriptions'));
app.use('/api/analysis', require('./routes/analysis'));
app.use('/api/integration', require('./routes/integration'));
app.use('/api/taxonomy', require('./routes/taxonomy'));
app.use('/api/progress', require('./routes/progress'));

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK' });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: err.message });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Время:** 1 час

**Итого Этап 1:** 6-9 часов

---

## ЭТАП 2: CORE SERVICES (Dropbox, Google Sheets, ID Generator)

### 2.1 ID Generator Service

**server/src/services/id-generator.js:**
```javascript
/**
 * Единая система генерации ID
 * Формат: {PREFIX}-{NUMBER}
 * Примеры: SEARCH-001, VQ-042, VIDEO-015, WRF-412
 */
class IDGenerator {
  constructor(sheetsService, dropboxService) {
    this.sheets = sheetsService;
    this.dropbox = dropboxService;
  }

  // Генерация SEARCH-XXX (из Google Sheets)
  async generateSearchID() {
    const existing = await this.sheets.getAllSearchIDs();
    return this._getNextID('SEARCH', existing);
  }

  // Генерация VQ-XXX (из Google Sheets)
  async generateVQID() {
    const existing = await this.sheets.getAllVQIDs();
    return this._getNextID('VQ', existing);
  }

  // Генерация VIDEO-XXX (сканирование Dropbox)
  async generateVideoID() {
    const files = await this.dropbox.listFiles('/02_TRANSCRIPTIONS/');
    const existing = files
      .filter(f => f.name.match(/Video_(\d+)\.md/))
      .map(f => parseInt(f.name.match(/Video_(\d+)\.md/)[1]));
    return this._getNextID('VIDEO', existing);
  }

  // Генерация entity IDs (WRF, TOL, OBJ, etc.)
  async generateEntityID(type) {
    const path = `/ENTITIES/LIBRARIES/${type.toUpperCase()}S/`;
    const files = await this.dropbox.listFiles(path);
    const prefix = this._getEntityPrefix(type);
    const existing = files
      .filter(f => f.name.match(new RegExp(`${prefix}-(\\d+)\\.json`)))
      .map(f => parseInt(f.name.match(new RegExp(`${prefix}-(\\d+)\\.json`))[1]));
    return this._getNextID(prefix, existing);
  }

  _getNextID(prefix, existingNumbers) {
    const maxNum = existingNumbers.length > 0
      ? Math.max(...existingNumbers)
      : 0;
    const nextNum = (maxNum + 1).toString().padStart(3, '0');
    return `${prefix}-${nextNum}`;
  }

  _getEntityPrefix(type) {
    const prefixes = {
      workflow: 'WRF',
      tool: 'TOL',
      object: 'OBJ',
      action: 'ACT',
      profession: 'PRF',
      skill: 'SKL',
      department: 'DPT'
    };
    return prefixes[type.toLowerCase()];
  }
}

module.exports = IDGenerator;
```

**Время:** 3-4 часа

### 2.2 Google Sheets Service

**server/src/services/sheets-service.js:**
```javascript
const { google } = require('googleapis');

class SheetsService {
  constructor() {
    this.auth = new google.auth.GoogleAuth({
      keyFile: process.env.GOOGLE_SHEETS_CREDENTIALS_PATH,
      scopes: ['https://www.googleapis.com/auth/spreadsheets']
    });
    this.sheets = google.sheets({ version: 'v4', auth: this.auth });
    this.spreadsheetId = process.env.SPREADSHEET_ID;
  }

  // Search Queue operations
  async getSearchQueue() {
    const range = 'Search_Queue_Master!A2:J';
    const response = await this.sheets.spreadsheets.values.get({
      spreadsheetId: this.spreadsheetId,
      range
    });
    return this._parseSearchQueue(response.data.values);
  }

  async addSearchTask(task) {
    const range = 'Search_Queue_Master!A:J';
    const values = [[
      task.search_id,
      task.employee,
      task.department,
      task.topic,
      task.search_query || '',
      task.status || 'Assigned',
      new Date().toISOString(),
      0,
      '',
      task.notes || ''
    ]];

    await this.sheets.spreadsheets.values.append({
      spreadsheetId: this.spreadsheetId,
      range,
      valueInputOption: 'USER_ENTERED',
      resource: { values }
    });
  }

  async updateSearchTask(searchId, updates) {
    // Find row, update values
    // Implementation...
  }

  // Video Queue operations
  async getVideoQueue() {
    const range = 'Video_Queue_Master!A2:N';
    const response = await this.sheets.spreadsheets.values.get({
      spreadsheetId: this.spreadsheetId,
      range
    });
    return this._parseVideoQueue(response.data.values);
  }

  async addVideoToQueue(video) {
    const range = 'Video_Queue_Master!A:N';
    const values = [[
      video.vq_id,
      video.youtube_url,
      video.title,
      video.channel,
      video.duration,
      video.views || 0,
      video.upload_date || '',
      video.topic,
      video.source,
      video.employee,
      video.priority || 50,
      video.status || 'Queued',
      new Date().toISOString(),
      video.notes || ''
    ]];

    await this.sheets.spreadsheets.values.append({
      spreadsheetId: this.spreadsheetId,
      range,
      valueInputOption: 'USER_ENTERED',
      resource: { values }
    });
  }

  // Video Progress Tracker operations
  async getVideoProgress() {
    const range = 'Video_Progress_Tracker!A2:N';
    // Implementation...
  }

  async updateVideoProgress(videoNumber, phaseData) {
    // Implementation...
  }

  // Helper methods
  _parseSearchQueue(rows) {
    return rows.map(row => ({
      search_id: row[0],
      employee: row[1],
      department: row[2],
      topic: row[3],
      search_query: row[4],
      status: row[5],
      date_assigned: row[6],
      videos_found: parseInt(row[7]) || 0,
      date_completed: row[8],
      notes: row[9]
    }));
  }

  _parseVideoQueue(rows) {
    return rows.map(row => ({
      vq_id: row[0],
      youtube_url: row[1],
      title: row[2],
      channel: row[3],
      duration: row[4],
      views: parseInt(row[5]) || 0,
      upload_date: row[6],
      topic: row[7],
      source: row[8],
      employee: row[9],
      priority: parseInt(row[10]) || 50,
      status: row[11],
      date_added: row[12],
      notes: row[13]
    }));
  }

  async getAllSearchIDs() {
    const data = await this.getSearchQueue();
    return data.map(item =>
      parseInt(item.search_id.split('-')[1])
    );
  }

  async getAllVQIDs() {
    const data = await this.getVideoQueue();
    return data.map(item =>
      parseInt(item.vq_id.split('-')[1])
    );
  }
}

module.exports = SheetsService;
```

**Время:** 4-5 часов

### 2.3 Dropbox Service

**server/src/services/dropbox-service.js:**
```javascript
const Dropbox = require('dropbox-v2-api');

class DropboxService {
  constructor() {
    this.dbx = Dropbox({
      auth: process.env.DROPBOX_ACCESS_TOKEN
    });
    this.basePath = '/ENTITIES/TASK_MANAGERS/RESEARCHES 2';
  }

  // List files in directory
  async listFiles(path) {
    return new Promise((resolve, reject) => {
      this.dbx({
        resource: 'files/list_folder',
        parameters: { path: this.basePath + path }
      }, (err, result) => {
        if (err) reject(err);
        else resolve(result.entries);
      });
    });
  }

  // Read file content
  async readFile(path) {
    return new Promise((resolve, reject) => {
      this.dbx({
        resource: 'files/download',
        parameters: { path: this.basePath + path }
      }, (err, result, response) => {
        if (err) reject(err);
        else resolve(response);
      });
    });
  }

  // Write file content
  async writeFile(path, content) {
    return new Promise((resolve, reject) => {
      this.dbx({
        resource: 'files/upload',
        parameters: {
          path: this.basePath + path,
          mode: 'overwrite'
        },
        readStream: Buffer.from(content)
      }, (err, result) => {
        if (err) reject(err);
        else resolve(result);
      });
    });
  }

  // Read transcription
  async getTranscription(videoNumber) {
    const path = `/02_TRANSCRIPTIONS/Video_${videoNumber.toString().padStart(3, '0')}.md`;
    return await this.readFile(path);
  }

  // Write transcription
  async saveTranscription(videoNumber, content) {
    const path = `/02_TRANSCRIPTIONS/Video_${videoNumber.toString().padStart(3, '0')}.md`;
    return await this.writeFile(path, content);
  }

  // Read entity JSON
  async getEntity(type, id) {
    const path = `/ENTITIES/LIBRARIES/${type.toUpperCase()}S/${id}.json`;
    const content = await this.readFile(path);
    return JSON.parse(content);
  }

  // Write entity JSON
  async saveEntity(type, id, data) {
    const path = `/ENTITIES/LIBRARIES/${type.toUpperCase()}S/${id}.json`;
    const content = JSON.stringify(data, null, 2);
    return await this.writeFile(path, content);
  }

  // List all entities of type
  async listEntities(type) {
    const path = `/ENTITIES/LIBRARIES/${type.toUpperCase()}S/`;
    const files = await this.listFiles(path);
    return files
      .filter(f => f.name.endsWith('.json'))
      .map(f => f.name.replace('.json', ''));
  }

  // Read prompt template
  async getPrompt(promptName) {
    const path = `/PROMPTS/${promptName}.md`;
    return await this.readFile(path);
  }
}

module.exports = DropboxService;
```

**Время:** 4-5 часов

**Итого Этап 2:** 11-14 часов

---

## ОСТАЛЬНЫЕ ЭТАПЫ (КРАТКОЕ ОПИСАНИЕ)

Полное описание всех этапов см. в файле: **nested-floating-naur-summary.md**

### **ЭТАП 3: VIDEO QUEUE** (18-22 часа)
- Backend API + Priority Calculator
- Frontend Dashboard с shadcn/ui
- YouTube metadata integration
- Google Sheets storage

### **ЭТАП 4: TRANSCRIPTIONS** (25-30 часов)
- AI-assisted transcription (PMT-004)
- Entity extraction (37+)
- Markdown editor + preview
- Dropbox integration

### **ЭТАП 5: ANALYSIS** (30-35 часов)
- Phase 2: Extraction (PMT-007)
- Phase 3: Gap Analysis
- Phase 5: Mapping & Reporting
- Frontend visualization

### **ЭТАП 6: INTEGRATION** (25-30 часов)
- JSON Creator для 7 entity types
- Validation & Cross-references
- Integration Wizard (step-by-step)
- Dropbox JSON management

### **ЭТАП 7: TAXONOMY** (20-25 часов)
- Entity Explorer
- Search & Filter
- Relationship Graph (D3.js)
- Hierarchy Tree

### **ЭТАП 8: DASHBOARD & PROGRESS** (20-25 часов)
- Main Dashboard с метриками
- Progress Tracker
- Reports Generator
- Real-time updates

### **ЭТАП 9: SEARCH QUEUE** (12-15 часов)
- Search task management
- Google Sheets integration
- Frontend Dashboard

### **ЭТАП 10: TESTING & DEPLOY** (20-25 часов)
- Unit + Integration tests
- Documentation
- CI/CD + Production deploy

---

## ИТОГОВАЯ СВОДКА

**Общее время разработки:** 187-230 часов (24-29 рабочих дней при 8 ч/день)

**Технологический стек:**
- **Frontend:** React.js + Tailwind CSS + shadcn/ui
- **Backend:** Node.js + Express.js
- **Storage:** Dropbox API + Google Sheets API
- **APIs:** YouTube Data API v3, OpenAI/Claude API
- **No Database, No Auth, No Rate Limiting**

**Единая система ID:**
- Формат: `{PREFIX}-{NUMBER}`
- Примеры: SEARCH-001, VQ-042, VIDEO-028, WRF-412, TOL-342
- Автоматическая генерация с scan Dropbox + Google Sheets

**Data Storage:**
- **Google Sheets (4 листа):**
  - Search_Queue_Master
  - Video_Queue_Master
  - Video_Progress_Tracker
  - Integration_Log
- **Dropbox:**
  - /02_TRANSCRIPTIONS/ (markdown)
  - /03_ANALYSIS/ (reports)
  - /ENTITIES/LIBRARIES/ (JSON files)
  - /PROMPTS/ (templates)

**Критический путь (MVP):**
1. Инфраструктура (Этап 1)
2. Core Services (Этап 2)
3. Video Queue (Этап 3)
4. Transcriptions (Этап 4)
5. Analysis (Этап 5)
6. Integration (Этап 6)
7. Dashboard (Этап 8)

**Дополнительно:**
- Taxonomy Explorer (Этап 7)
- Search Queue (Этап 9)
- Testing & Deploy (Этап 10)

---

## СЛЕДУЮЩИЕ ШАГИ

1. ✅ Утвердить план с командой
2. ⬜ Создать GitHub репозиторий
3. ⬜ Получить API credentials:
   - Dropbox Access Token
   - Google Sheets credentials.json
   - YouTube API Key
   - OpenAI/Claude API Keys
4. ⬜ Начать Этап 1 (Инфраструктура)
5. ⬜ Реализовать Этап 2 (Core Services)

---

**План готов к выполнению!**

Для детального описания каждого этапа с кодом см. файл: **nested-floating-naur-summary.md**

**Время:** 12-15 часов

### 3.2 Frontend для Video Queue

**Компоненты:**
- VideoQueueDashboard (интерактивная таблица с сортировкой)
- AddVideoForm (форма добавления)
- VideoCard (карточка видео с деталями)
- PriorityBadge (визуализация приоритета)
- StatusBadge (визуализация статуса)
- VideoQueueStats (статистика очереди)

**Функционал:**
- Просмотр очереди с фильтрами (статус, приоритет, дата)
- Сортировка по любому полю
- Добавление видео (full/simple mode)
- Пересчёт приоритета (single/batch)
- Обновление статусов
- Экспорт в CSV/JSON/Markdown

**Интерактивный Dashboard:**
- Drag & drop для изменения порядка
- Inline editing для notes
- Bulk actions (выбрать несколько → изменить статус)
- Visual priority indicators (цветовые индикаторы)

**Файлы:**
- `frontend/src/components/VideoQueue/Dashboard.tsx`
- `frontend/src/components/VideoQueue/AddVideoForm.tsx`
- `frontend/src/components/VideoQueue/VideoCard.tsx`
- `frontend/src/components/VideoQueue/PriorityBadge.tsx`
- `frontend/src/components/VideoQueue/StatusBadge.tsx`
- `frontend/src/components/VideoQueue/Stats.tsx`
- `frontend/src/services/videoQueueApi.ts`

**Время:** 15-18 часов

### 3.3 Интеграция скриптов

**Адаптировать:**
- `add_video_to_queue.py` → API
- `add_video_to_queue_simple.py` → API
- `calculate_priority.py` → Service
- `update_queue_status.py` → API
- `export_queue.py` → API
- `video_queue_manager.py` → Web UI

**Время:** 6-8 часов

**Итого Этап 3:** 33-41 часов

---

## ЭТАП 4: TRANSCRIPTIONS MODULE

### 4.1 Backend для Transcriptions

**API endpoints:**
```
POST   /api/transcriptions/start          # Начать транскрипцию
GET    /api/transcriptions/{video_number} # Получить транскрипцию
PUT    /api/transcriptions/{video_number} # Обновить транскрипцию
POST   /api/transcriptions/validate       # Валидация (37+ entities)
GET    /api/transcriptions/                # Список всех транскрипций
```

**Services:**
- `TranscriptionService` - бизнес-логика
- `AIAssistant` - интеграция с AI (OpenAI/Claude API)
- `EntityExtractor` - извлечение 37+ сущностей
- `EntityValidator` - валидация сущностей
- `MarkdownGenerator` - генерация Video_XXX.md

**Entity extraction (7 типов):**
```python
ENTITY_TYPES = {
    "workflows": "WRF-###",
    "tools": "TOL-###",
    "objects": "OBJ-###",
    "actions": "ACT-###",  # 7 categories A-G
    "professions": "PRF-###",
    "skills": "SKL-###",
    "departments": "DPT-###"
}
```

**Validation rules:**
- Минимум 37 сущностей
- Все 7 типов представлены
- Каждая сущность имеет:
  - Уникальный ID
  - Название
  - Описание
  - Категория

**Файлы:**
- `backend/api/routes/transcriptions.py`
- `backend/models/transcription.py`
- `backend/services/transcription_service.py`
- `backend/services/ai_assistant.py`
- `backend/services/entity_extractor.py`
- `backend/services/entity_validator.py`
- `backend/services/markdown_generator.py`
- `backend/schemas/transcription_schema.py`

**Время:** 15-20 часов

### 4.2 Frontend для Transcriptions

**Компоненты:**
- TranscriptionEditor (редактор транскрипции)
- EntityList (список извлечённых сущностей)
- EntityCard (карточка сущности)
- ValidationPanel (панель валидации)
- TranscriptionStats (статистика по видео)
- PromptTemplate (шаблоны PMT-004)

**Функционал:**
- AI-assisted транскрипция (интеграция с OpenAI/Claude)
- Редактор markdown с preview
- Real-time валидация (37+ entities)
- Цветовая индикация типов сущностей
- Drag & drop для организации сущностей
- Экспорт в markdown

**AI Integration:**
- Выбор AI модели (GPT-4, Claude 3)
- Применение PMT-004 prompt
- Автоматическая экстракция сущностей
- Проверка качества

**Файлы:**
- `frontend/src/components/Transcriptions/Editor.tsx`
- `frontend/src/components/Transcriptions/EntityList.tsx`
- `frontend/src/components/Transcriptions/EntityCard.tsx`
- `frontend/src/components/Transcriptions/ValidationPanel.tsx`
- `frontend/src/components/Transcriptions/Stats.tsx`
- `frontend/src/components/Transcriptions/PromptTemplate.tsx`
- `frontend/src/services/transcriptionApi.ts`
- `frontend/src/services/aiApi.ts`

**Время:** 18-22 часов

### 4.3 AI Prompt Integration

**Реализовать PMT-004 prompt:**
- Загрузить prompt из `PROMPTS/PMT-004_Video_Transcription_v4.1.md`
- Интеграция с OpenAI API / Claude API
- Обработка ответов
- Парсинг извлечённых сущностей

**Файлы:**
- `backend/prompts/pmt_004.py`
- `backend/services/prompt_engine.py`

**Время:** 6-8 часов

**Итого Этап 4:** 39-50 часов

---

## ЭТАП 5: ANALYSIS MODULE

### 5.1 Phase 2: Extraction (Backend)

**API endpoints:**
```
POST   /api/analysis/extract/{video_number}  # Запустить экстракцию
GET    /api/analysis/extract/{video_number}  # Получить результаты
```

**Services:**
- `ExtractionService` - глубокая экстракция
- `CrossReferenceBuilder` - построение связей
- `ObjectRelationshipAnalyzer` - анализ отношений

**Extraction logic:**
- Читает Video_XXX.md
- Применяет PMT-007 prompt
- Расширяет сущности (37 → 60-70)
- Создаёт двунаправленные cross-references
- Генерирует Phase3_Analysis.md + Phase4_Objects.md

**Файлы:**
- `backend/api/routes/analysis.py`
- `backend/services/extraction_service.py`
- `backend/services/cross_reference_builder.py`
- `backend/services/object_relationship_analyzer.py`
- `backend/prompts/pmt_007.py`

**Время:** 10-12 часов

### 5.2 Phase 3: Gap Analysis (Backend)

**API endpoints:**
```
POST   /api/analysis/gap/{video_number}     # Запустить gap analysis
GET    /api/analysis/gap/{video_number}     # Получить результаты
```

**Services:**
- `GapAnalysisService` - анализ пробелов
- `LibraryComparator` - сравнение с LIBRARIES
- `CoverageCalculator` - расчёт покрытия

**Gap analysis logic:**
```python
# 1. Сравнить с LIBRARIES/TOOLS/
# 2. Сравнить с LIBRARIES/WORKFLOWS/
# 3. Сравнить с LIBRARIES/OBJECTS/
# 4. Категоризовать:
#    → NEW: не в библиотеке
#    → EXISTING: уже в библиотеке
#    → UPDATE: в библиотеке, но нужно обновить
# 5. Рассчитать метрики покрытия
# 6. Сгенерировать Video_XXX_Gap_Analysis.md
```

**Comparison methods:**
- Exact match (по ID)
- Fuzzy name match (>85% similarity)
- Semantic match (>75% similarity)
- Attribute overlap (>70%)

**Файлы:**
- `backend/services/gap_analysis_service.py`
- `backend/services/library_comparator.py`
- `backend/services/coverage_calculator.py`
- Адаптация `video_gap_analyzer.py`

**Время:** 12-15 часов

### 5.3 Phase 5: Mapping (Backend)

**API endpoints:**
```
POST   /api/analysis/mapping/{video_number}  # Запустить mapping
GET    /api/analysis/mapping/{video_number}  # Получить отчёт
```

**Services:**
- `MappingService` - финальное картирование
- `ReportGenerator` - генерация отчётов
- `BusinessValueCalculator` - расчёт бизнес-ценности

**Mapping report structure:**
```markdown
# Executive Summary
# Integration Status
# Library Locations
# Business Value Analysis
# Cross-Reference Map
# Quality Metrics
# Recommendations
```

**Файлы:**
- `backend/services/mapping_service.py`
- `backend/services/report_generator.py`
- `backend/services/business_value_calculator.py`
- Адаптация `video_integration_reporter.py`

**Время:** 10-12 часов

### 5.4 Frontend для Analysis

**Компоненты:**
- AnalysisDashboard (обзор всех фаз)
- ExtractionPanel (Phase 2 результаты)
- GapAnalysisPanel (Phase 3 результаты)
- MappingPanel (Phase 5 отчёт)
- EntityComparison (сравнение сущностей)
- CoverageChart (визуализация покрытия)

**Функционал:**
- Запуск анализа для видео
- Просмотр результатов по фазам
- Интерактивная визуализация:
  - Pie chart (NEW/EXISTING/UPDATE)
  - Bar chart (покрытие до/после)
  - Network graph (cross-references)
- Экспорт отчётов

**Файлы:**
- `frontend/src/components/Analysis/Dashboard.tsx`
- `frontend/src/components/Analysis/ExtractionPanel.tsx`
- `frontend/src/components/Analysis/GapAnalysisPanel.tsx`
- `frontend/src/components/Analysis/MappingPanel.tsx`
- `frontend/src/components/Analysis/EntityComparison.tsx`
- `frontend/src/components/Analysis/CoverageChart.tsx`
- `frontend/src/services/analysisApi.ts`

**Время:** 15-18 часов

**Итого Этап 5:** 47-57 часов

---

## ЭТАП 6: INTEGRATION MODULE

### 6.1 Backend для Integration

**API endpoints:**
```
POST   /api/integration/create-json/{video_number}  # Создать JSON файлы
PUT    /api/integration/update-json/{entity_id}     # Обновить JSON
POST   /api/integration/validate                    # Валидация схем
GET    /api/integration/log                         # Лог интеграций
POST   /api/integration/rollback/{integration_id}   # Откат изменений
```

**Services:**
- `IntegrationService` - основная логика
- `JSONCreator` - создание JSON из templates
- `JSONUpdater` - обновление existing JSON
- `SchemaValidator` - валидация схем
- `BackupManager` - управление бэкапами
- `CrossReferenceUpdater` - обновление связей

**JSON Creation workflow:**
```python
# Для каждой NEW сущности:
1. Определить тип (Tool/Workflow/Object/etc.)
2. Загрузить соответствующий template
3. Заполнить поля (name, description, category, etc.)
4. Назначить уникальный ID (TOL-XXX, WRF-XXX, etc.)
5. Добавить bidirectional cross-references
6. Валидировать JSON schema
7. Создать backup
8. Сохранить в LIBRARIES/
9. Записать в integration_log
```

**JSON Templates:**
```json
// Tool template
{
  "entity_id": "",
  "name": "",
  "type": "Tool",
  "category": "",
  "features": [],
  "creates_objects": [],
  "used_in_workflows": [],
  "requires_skills": [],
  "metadata": {
    "source_video": "",
    "date_added": "",
    "version": "1.0"
  }
}

// Workflow template
{
  "entity_id": "",
  "name": "",
  "type": "Workflow",
  "description": "",
  "steps": [],
  "complexity": "",
  "uses_tools": [],
  "creates_objects": [],
  "required_skills": [],
  "metadata": {}
}
```

**Файлы:**
- `backend/api/routes/integration.py`
- `backend/models/integration_log.py`
- `backend/services/integration_service.py`
- `backend/services/json_creator.py`
- `backend/services/json_updater.py`
- `backend/services/schema_validator.py`
- `backend/services/backup_manager.py`
- `backend/services/cross_reference_updater.py`
- `backend/templates/json/` (все шаблоны)
- Адаптация `video_json_updater.py`

**Время:** 18-22 часов

### 6.2 Frontend для Integration

**Компоненты:**
- IntegrationDashboard (обзор интеграций)
- JSONCreationWizard (мастер создания JSON)
- EntityForm (форма редактирования сущности)
- CrossReferenceEditor (редактор связей)
- ValidationPanel (панель валидации)
- IntegrationLog (лог операций)
- BackupManager (управление бэкапами)

**Функционал:**
- **Interactive mode:** Пошаговое создание JSON
  - Step 1: Выбрать сущности для создания
  - Step 2: Заполнить основные поля
  - Step 3: Добавить cross-references
  - Step 4: Валидация
  - Step 5: Подтверждение и создание
- **Auto mode:** Автоматическое создание всех NEW entities
- Редактирование JSON в визуальном редакторе
- Preview JSON перед сохранением
- Валидация схем в real-time
- Просмотр и восстановление бэкапов
- History всех изменений

**JSON Editor:**
- Split view: форма + JSON preview
- Syntax highlighting
- Auto-completion
- Schema validation hints

**Файлы:**
- `frontend/src/components/Integration/Dashboard.tsx`
- `frontend/src/components/Integration/JSONCreationWizard.tsx`
- `frontend/src/components/Integration/EntityForm.tsx`
- `frontend/src/components/Integration/CrossReferenceEditor.tsx`
- `frontend/src/components/Integration/ValidationPanel.tsx`
- `frontend/src/components/Integration/IntegrationLog.tsx`
- `frontend/src/components/Integration/BackupManager.tsx`
- `frontend/src/services/integrationApi.ts`

**Время:** 20-25 часов

**Итого Этап 6:** 38-47 часов

---

## ЭТАП 7: TAXONOMY SYSTEM

### 7.1 Backend для Taxonomy

**API endpoints:**
```
GET    /api/taxonomy/entities             # Все сущности
GET    /api/taxonomy/entities/{type}      # Сущности по типу
GET    /api/taxonomy/entities/{id}        # Сущность по ID
POST   /api/taxonomy/search               # Поиск сущностей
GET    /api/taxonomy/relationships/{id}   # Связи сущности
GET    /api/taxonomy/hierarchy            # Иерархия taxonomy
GET    /api/taxonomy/stats                # Статистика
```

**Services:**
- `TaxonomyService` - управление taxonomy
- `EntityManager` - CRUD операции
- `RelationshipManager` - управление связями
- `SearchEngine` - полнотекстовый поиск
- `HierarchyBuilder` - построение иерархии

**Taxonomy structure:**
```
TAX-001: LIBRARIES (Knowledge Base)
  ├── LBS-001: Actions (429 verbs)
  ├── LBS-002: Objects (110+)
  ├── LBS-003: Tools (164+)
  ├── LBS-004: Skills (29+)
  ├── LBS-005: Professions (25+)
  ├── LBS-006: Departments (9)
  └── LBS-007: Responsibilities (193)

TAX-002: TASK_MANAGERS (Workflow Templates)
  ├── Projects (PRT)
  ├── Milestones (MLT)
  ├── Tasks (TST)
  ├── Workflows (WRF)
  └── Prompts (PMT)

TAX-003: TALENTS (Employee/Skill Classification)
```

**Файлы:**
- `backend/api/routes/taxonomy.py`
- `backend/models/entity.py`
- `backend/models/relationship.py`
- `backend/services/taxonomy_service.py`
- `backend/services/entity_manager.py`
- `backend/services/relationship_manager.py`
- `backend/services/search_engine.py`
- `backend/services/hierarchy_builder.py`

**Время:** 15-18 часов

### 7.2 Frontend для Taxonomy

**Компоненты:**
- TaxonomyExplorer (навигация по taxonomy)
- EntityViewer (просмотр сущности)
- RelationshipGraph (граф связей)
- SearchPanel (поиск сущностей)
- HierarchyTree (древовидная структура)
- StatsPanel (статистика taxonomy)

**Функционал:**
- Интерактивная навигация по taxonomy
- Визуализация связей (network graph с D3.js)
- Полнотекстовый поиск
- Фильтрация по типам
- Drill-down в детали
- Экспорт структуры

**Visualizations:**
- Network graph для cross-references
- Tree view для иерархии
- Sankey diagram для flows
- Heatmap для покрытия

**Файлы:**
- `frontend/src/components/Taxonomy/Explorer.tsx`
- `frontend/src/components/Taxonomy/EntityViewer.tsx`
- `frontend/src/components/Taxonomy/RelationshipGraph.tsx`
- `frontend/src/components/Taxonomy/SearchPanel.tsx`
- `frontend/src/components/Taxonomy/HierarchyTree.tsx`
- `frontend/src/components/Taxonomy/StatsPanel.tsx`
- `frontend/src/services/taxonomyApi.ts`

**Время:** 18-22 часов

**Итого Этап 7:** 33-40 часов

---

## ЭТАП 8: ORCHESTRATION & MONITORING

### 8.1 Process Orchestrator

**Backend:**
- `ProcessOrchestrator` - управление полным workflow
- Task queue (Celery + RabbitMQ)
- Background jobs
- Error handling и retry logic

**API endpoints:**
```
POST   /api/process/start/{video_number}    # Запустить полный процесс
POST   /api/process/start-phase/{video_number}/{phase}  # Запустить фазу
GET    /api/process/status/{video_number}   # Статус обработки
POST   /api/process/pause/{video_number}    # Пауза
POST   /api/process/resume/{video_number}   # Возобновить
POST   /api/process/cancel/{video_number}   # Отменить
```

**Process flow:**
```python
def process_video_full(video_number):
    # Phase 1: Transcription (manual/AI-assisted)
    transcription = transcribe_video(video_number)
    validate_entities(transcription, min_count=37)

    # Phase 2: Extraction
    extraction = extract_entities(video_number)

    # Phase 3: Gap Analysis (automated)
    gap_analysis = analyze_gaps(video_number)

    # Phase 4: Integration (semi-automated)
    integration = create_json_files(gap_analysis)

    # Phase 5: Mapping (automated)
    mapping = generate_mapping_report(video_number)

    # Complete
    mark_complete(video_number)

    return status
```

**Файлы:**
- `backend/services/process_orchestrator.py`
- `backend/tasks/celery_tasks.py`
- `backend/services/error_handler.py`
- Адаптация `process_video.py`

**Время:** 12-15 часов

### 8.2 Progress Tracking

**Backend:**
- `ProgressTracker` - отслеживание прогресса
- Real-time updates через WebSocket
- Phase transitions
- Metrics calculation

**API endpoints:**
```
GET    /api/progress/video/{video_number}   # Прогресс видео
GET    /api/progress/all                    # Прогресс всех видео
GET    /api/progress/stats                  # Статистика
GET    /api/progress/timeline/{video_number} # Timeline обработки
POST   /api/progress/update/{video_number}  # Обновить прогресс
```

**WebSocket events:**
```javascript
// Real-time updates
ws.on('video:phase-started', { video_number, phase })
ws.on('video:phase-completed', { video_number, phase, duration })
ws.on('video:progress', { video_number, percentage })
ws.on('video:error', { video_number, error })
```

**Файлы:**
- `backend/services/progress_tracker.py`
- `backend/websocket/progress_handler.py`
- Адаптация `update_video_progress.py`

**Время:** 10-12 часов

### 8.3 Reporting & Analytics

**Backend:**
- `ReportGenerator` - генерация отчётов
- `AnalyticsEngine` - аналитика
- Scheduled reports

**API endpoints:**
```
POST   /api/reports/generate/{type}         # Генерация отчёта
GET    /api/reports/list                    # Список отчётов
GET    /api/reports/download/{id}           # Скачать отчёт
GET    /api/analytics/summary               # Сводка
GET    /api/analytics/trends                # Тренды
GET    /api/analytics/performance           # Производительность
```

**Report types:**
- Summary report (общая сводка)
- Weekly report (недельный отчёт)
- Monthly report (месячный отчёт)
- Detailed report (детальный по видео)
- Compliance report (соответствие PMT prompts)

**Файлы:**
- `backend/services/report_generator.py`
- `backend/services/analytics_engine.py`
- Адаптация `generate_progress_report.py`

**Время:** 10-12 часов

### 8.4 Frontend Dashboard & Monitoring

**Компоненты:**
- MainDashboard (главный dashboard)
- ProcessMonitor (мониторинг процессов)
- ProgressTimeline (timeline обработки)
- MetricsPanel (метрики системы)
- ReportsPanel (отчёты)
- NotificationsPanel (уведомления)

**Главный Dashboard:**
- Real-time статистика:
  - Всего видео обработано
  - Видео в процессе
  - Средняя скорость обработки
  - Экономия времени
  - Извлечено сущностей
  - Покрытие библиотеки
- Activity feed (последние действия)
- Phase distribution (pie chart)
- Processing timeline (gantt chart)
- Employee performance (bar chart)

**Process Monitor:**
- Список активных процессов
- Progress bars для каждой фазы
- Real-time logs
- Actions (pause/resume/cancel)

**Файлы:**
- `frontend/src/components/Dashboard/Main.tsx`
- `frontend/src/components/Dashboard/ProcessMonitor.tsx`
- `frontend/src/components/Dashboard/ProgressTimeline.tsx`
- `frontend/src/components/Dashboard/MetricsPanel.tsx`
- `frontend/src/components/Dashboard/ReportsPanel.tsx`
- `frontend/src/components/Dashboard/NotificationsPanel.tsx`
- `frontend/src/services/dashboardApi.ts`
- `frontend/src/websocket/progressClient.ts`

**Время:** 18-22 часов

**Итого Этап 8:** 50-61 часов

---

## ЭТАП 9: ТЕСТИРОВАНИЕ, ОПТИМИЗАЦИЯ, ДЕПЛОЙ

### 9.1 Автоматизированное тестирование

**Backend tests:**
- Unit tests (pytest)
- Integration tests
- API tests (FastAPI TestClient)
- Database tests

**Тестовое покрытие:**
- Models: 90%+
- Services: 85%+
- API routes: 90%+
- Overall: 85%+

**Test files:**
```
tests/
├── unit/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
├── integration/
│   ├── test_api.py
│   ├── test_workflow.py
│   └── test_database.py
├── e2e/
│   └── test_full_process.py
└── fixtures/
    └── sample_data.py
```

**Файлы:**
- `tests/` (вся структура тестов)
- `pytest.ini`
- `.coveragerc`

**Время:** 20-25 часов

### 9.2 Frontend тестирование

**Frontend tests:**
- Component tests (Jest + React Testing Library)
- Integration tests
- E2E tests (Playwright/Cypress)

**Файлы:**
- `frontend/src/__tests__/` (все тесты)
- `jest.config.js`
- `playwright.config.ts`

**Время:** 15-18 часов

### 9.3 Оптимизация производительности

**Backend optimization:**
- Database query optimization (indexes, eager loading)
- API response caching (Redis)
- Background job optimization
- Connection pooling

**Frontend optimization:**
- Code splitting
- Lazy loading
- Image optimization
- Bundle size reduction

**Время:** 12-15 часов

### 9.4 Документация

**Создать документацию:**
- API documentation (OpenAPI/Swagger)
- User guide
- Developer guide
- Deployment guide
- Architecture overview

**Файлы:**
- `docs/api.md`
- `docs/user-guide.md`
- `docs/developer-guide.md`
- `docs/deployment.md`
- `docs/architecture.md`

**Время:** 15-18 часов

### 9.5 CI/CD Pipeline

**Настроить:**
- GitHub Actions / GitLab CI
- Automated tests on push
- Linting и code quality checks
- Docker build
- Deployment to staging
- Deployment to production

**Файлы:**
- `.github/workflows/ci.yml`
- `.github/workflows/deploy.yml`
- `Dockerfile`
- `docker-compose.yml`

**Время:** 8-10 часов

### 9.6 Deployment

**Production setup:**
- Server configuration (AWS/GCP/Azure)
- Database setup (PostgreSQL)
- Redis setup
- RabbitMQ setup
- Nginx configuration
- SSL certificates
- Monitoring (Prometheus + Grafana)
- Logging (ELK stack)

**Файлы:**
- `deploy/nginx.conf`
- `deploy/docker-compose.prod.yml`
- `deploy/prometheus.yml`
- `deploy/grafana-dashboard.json`

**Время:** 15-20 часов

**Итого Этап 9:** 85-106 часов

---

## СВОДКА ПО ЭТАПАМ

| Этап | Название | Часы (мин-макс) | Задачи |
|------|----------|-----------------|--------|
| **0** | Документация и архитектура | - | Описание системы |
| **1** | Подготовка и инфраструктура | 7-11 | Окружение, БД, конфигурация |
| **2** | Search Queue Module | 22-27 | Backend, Frontend, Scripts |
| **3** | Video Queue Module | 33-41 | Backend, Frontend, Scripts |
| **4** | Transcriptions Module | 39-50 | Backend, Frontend, AI Integration |
| **5** | Analysis Module | 47-57 | Phases 2,3,5 - Backend, Frontend |
| **6** | Integration Module | 38-47 | JSON Creation, Validation |
| **7** | Taxonomy System | 33-40 | Taxonomy Explorer, Visualizations |
| **8** | Orchestration & Monitoring | 50-61 | Orchestrator, Dashboard, Reports |
| **9** | Тестирование, Оптимизация, Деплой | 85-106 | Tests, CI/CD, Production |

**ИТОГО:** 354-440 часов (45-55 рабочих дней при 8ч/день)

---

## ПРИОРИТЕТЫ РАЗРАБОТКИ

### Критический путь (MVP):
1. **Этап 1:** Инфраструктура ✓
2. **Этап 3:** Video Queue (основной workflow начинается здесь)
3. **Этап 4:** Transcriptions (ключевая фаза)
4. **Этап 5:** Analysis (автоматизация 3 фаз)
5. **Этап 6:** Integration (финализация workflow)
6. **Этап 8:** Orchestration (связывание всех модулей)

### Второстепенные модули:
7. **Этап 2:** Search Queue (можно отложить)
8. **Этап 7:** Taxonomy (можно реализовать постепенно)

### Финализация:
9. **Этап 9:** Тестирование и деплой

---

## ТЕХНОЛОГИЧЕСКИЙ СТЕК

### Backend:
- **Framework:** FastAPI (Python 3.8+)
- **Database:** PostgreSQL 14+
- **Cache:** Redis 7+
- **Queue:** RabbitMQ + Celery
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **AI:** OpenAI API, Anthropic Claude API
- **Metadata:** yt-dlp

### Frontend:
- **Framework:** React 18 + TypeScript
- **State Management:** Redux Toolkit
- **UI Library:** Material-UI (MUI) или Ant Design
- **Charts:** Recharts / D3.js
- **Forms:** React Hook Form + Zod
- **API Client:** Axios / React Query
- **WebSocket:** Socket.io-client

### DevOps:
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus + Grafana
- **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana)
- **Web Server:** Nginx
- **Cloud:** AWS/GCP/Azure (по выбору)

---

## КЛЮЧЕВЫЕ ФАЙЛЫ ДЛЯ РЕАЛИЗАЦИИ

### Backend критические файлы:
```
backend/
├── api/
│   ├── routes/
│   │   ├── search_queue.py
│   │   ├── video_queue.py
│   │   ├── transcriptions.py
│   │   ├── analysis.py
│   │   ├── integration.py
│   │   ├── taxonomy.py
│   │   ├── process.py
│   │   └── progress.py
│   └── main.py
├── models/
│   ├── search_queue.py
│   ├── video_queue.py
│   ├── transcription.py
│   ├── entity.py
│   ├── integration_log.py
│   └── video_progress.py
├── services/
│   ├── search_queue_service.py
│   ├── video_queue_service.py
│   ├── priority_calculator.py
│   ├── transcription_service.py
│   ├── ai_assistant.py
│   ├── entity_extractor.py
│   ├── extraction_service.py
│   ├── gap_analysis_service.py
│   ├── mapping_service.py
│   ├── integration_service.py
│   ├── json_creator.py
│   ├── taxonomy_service.py
│   ├── process_orchestrator.py
│   └── progress_tracker.py
└── database.py
```

### Frontend критические файлы:
```
frontend/src/
├── components/
│   ├── Dashboard/Main.tsx
│   ├── SearchQueue/Dashboard.tsx
│   ├── VideoQueue/Dashboard.tsx
│   ├── Transcriptions/Editor.tsx
│   ├── Analysis/Dashboard.tsx
│   ├── Integration/Dashboard.tsx
│   ├── Taxonomy/Explorer.tsx
│   └── Progress/Monitor.tsx
├── services/
│   ├── api.ts
│   ├── searchQueueApi.ts
│   ├── videoQueueApi.ts
│   ├── transcriptionApi.ts
│   ├── analysisApi.ts
│   ├── integrationApi.ts
│   ├── taxonomyApi.ts
│   └── progressApi.ts
└── App.tsx
```

---

## КРИТЕРИИ ЗАВЕРШЕНИЯ ЭТАПОВ

### Этап считается завершённым когда:

**Backend:**
- ✓ Все API endpoints реализованы
- ✓ Тесты написаны и проходят (>85% coverage)
- ✓ Swagger документация сгенерирована
- ✓ Все services работают корректно
- ✓ Database migrations готовы

**Frontend:**
- ✓ Все компоненты реализованы
- ✓ UI/UX соответствует макетам
- ✓ Тесты написаны и проходят
- ✓ Интеграция с API работает
- ✓ Error handling реализован

**Integration:**
- ✓ Frontend ↔ Backend интеграция работает
- ✓ WebSocket real-time обновления работают
- ✓ End-to-end тесты проходят
- ✓ Performance requirements выполнены

---

## СЛЕДУЮЩИЕ ШАГИ

1. **Утвердить план** с заинтересованными сторонами
2. **Начать Этап 1** (Инфраструктура)
3. **Настроить репозиторий** и CI/CD
4. **Создать task board** (Jira/GitHub Projects)
5. **Разбить этапы на спринты** (2-недельные спринты)
6. **Назначить команду разработки**
7. **Начать разработку**

---

**План готов к выполнению!**
