# Architecture Overview

**Updated:** 2025-12-09
**Version:** 2.0 - Separated Backend & Frontend

---

## 🏗️ ARCHITECTURE

### Separated Applications

Приложение состоит из **двух независимых** приложений:

```
research-management/
├── frontend/          # React 19 + Vite + TypeScript
│   ├── Port: 3000
│   ├── Build: Vite
│   └── Deploy: Vercel/Netlify
│
└── backend/           # Node.js + Express.js + TypeScript
    ├── Port: 5000
    ├── Database: PostgreSQL (Supabase/Neon)
    └── Deploy: Railway/Render/Heroku
```

---

## 🎨 FRONTEND (React)

### Stack

- **Framework:** React 19
- **Language:** TypeScript 5.0+
- **Build Tool:** Vite
- **Styling:** Tailwind CSS v4
- **State:** Zustand
- **Data Fetching:** TanStack Query (React Query)
- **Forms:** React Hook Form + Zod
- **HTTP Client:** Axios

### Structure

```bash
frontend/
├── src/
│   ├── components/
│   │   ├── search-queue/
│   │   ├── video-queue/
│   │   └── shared/
│   ├── stores/             # Zustand stores
│   ├── contexts/           # Theme, Auth contexts
│   ├── lib/                # Utils, types
│   ├── design-system/      # design-system.json
│   └── styles/
├── public/
├── package.json
├── vite.config.ts
├── tailwind.config.ts
└── tsconfig.json
```

### API Communication

```typescript
// Frontend вызывает Backend API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

// Example: Fetch search tasks
const response = await axios.get(`${API_BASE_URL}/search-queue`);
```

---

## 🖥️ BACKEND (Express.js)

### Stack

- **Runtime:** Node.js 20+
- **Framework:** Express.js 4.18+
- **Language:** TypeScript 5.0+
- **Database:** PostgreSQL 15+
- **ORM:** Prisma
- **Validation:** Zod
- **Auth:** JWT (jsonwebtoken)
- **CORS:** cors middleware

### Structure

```bash
backend/
├── src/
│   ├── server.ts           # Express app
│   ├── routes/
│   │   ├── search-queue.ts
│   │   ├── video-queue.ts
│   │   └── index.ts
│   ├── controllers/        # Business logic
│   ├── services/           # External APIs (OpenAI, YouTube, Dropbox)
│   ├── middleware/         # Validation, error handling
│   ├── lib/
│   │   └── prisma.ts
│   └── types/
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── package.json
├── tsconfig.json
└── .env
```

### API Endpoints

**Base URL:** `http://localhost:5000/api`

#### Search Queue

- `GET    /api/search-queue` - Get all tasks
- `POST   /api/search-queue` - Create task
- `PATCH  /api/search-queue/:id` - Update task
- `DELETE /api/search-queue/:id` - Delete task
- `POST   /api/search-queue/execute` - Execute search with OpenAI

#### Video Queue

- `GET    /api/video-queue` - Get all videos
- `POST   /api/video-queue` - Add video
- `PATCH  /api/video-queue/:id` - Update video
- `DELETE /api/video-queue/:id` - Delete video
- `GET    /api/video-queue/export` - Export to CSV

#### YouTube

- `GET    /api/youtube/metadata?videoId=xxx` - Get video metadata

---

## 🔄 DATA FLOW

```
┌─────────────┐         HTTP/REST         ┌─────────────┐
│             │    ──────────────────→    │             │
│   FRONTEND  │                            │   BACKEND   │
│  (React)    │    ←──────────────────    │  (Express)  │
│  Port 3000  │         JSON Data         │  Port 5000  │
└─────────────┘                            └─────────────┘
                                                  │
                                                  │ Prisma ORM
                                                  ↓
                                           ┌─────────────┐
                                           │ PostgreSQL  │
                                           │  Database   │
                                           └─────────────┘
```

### Request Example

```typescript
// FRONTEND (React Component)
import { useSearchQueueStore } from '@/stores/searchQueueStore';

function SearchQueueDashboard() {
  const { tasks, fetchTasks, createTask } = useSearchQueueStore();

  useEffect(() => {
    fetchTasks(); // Calls Backend API
  }, []);
}

// FRONTEND (Zustand Store)
export const useSearchQueueStore = create((set) => ({
  fetchTasks: async () => {
    const response = await axios.get(`${API_URL}/search-queue`);
    set({ tasks: response.data });
  }
}));

// BACKEND (Express Route)
router.get('/', async (req, res) => {
  const tasks = await prisma.searchTask.findMany();
  res.json(tasks);
});
```

---

## 🚀 DEPLOYMENT

### Frontend Deployment

**Recommended:** Vercel, Netlify, Cloudflare Pages

```bash
# Build
cd frontend
npm run build

# Deploy to Vercel
vercel --prod
```

**Environment Variables:**
```bash
VITE_API_URL=https://api.your-domain.com/api
```

### Backend Deployment

**Recommended:** Railway, Render, Heroku, Fly.io

```bash
# Build
cd backend
npm run build

# Deploy to Railway
railway up
```

**Environment Variables:**
```bash
DATABASE_URL=postgresql://...
OPENAI_API_KEY=sk-...
YOUTUBE_API_KEY=AIza...
DROPBOX_ACCESS_TOKEN=sl....
FRONTEND_URL=https://your-app.vercel.app
PORT=5000
```

---

## 🔐 CORS Configuration

Backend разрешает запросы только от Frontend:

```typescript
// backend/src/server.ts
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  credentials: true,
  methods: ['GET', 'POST', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

---

## 📦 PACKAGE.JSON

### Frontend

```json
{
  "name": "research-frontend",
  "version": "2.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "axios": "^1.6.0",
    "zustand": "^4.4.0",
    "@tanstack/react-query": "^5.0.0",
    "react-hook-form": "^7.48.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "@types/react": "^19.0.0",
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "tailwindcss": "^4.0.0"
  }
}
```

### Backend

```json
{
  "name": "research-backend",
  "version": "2.0.0",
  "scripts": {
    "dev": "ts-node-dev --respawn src/server.ts",
    "build": "tsc",
    "start": "node dist/server.js"
  },
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "helmet": "^7.1.0",
    "morgan": "^1.10.0",
    "dotenv": "^16.3.0",
    "@prisma/client": "^5.7.0",
    "openai": "^4.20.0",
    "googleapis": "^126.0.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.0",
    "@types/cors": "^2.8.0",
    "@types/morgan": "^1.9.0",
    "@types/node": "^20.10.0",
    "typescript": "^5.3.0",
    "ts-node-dev": "^2.0.0",
    "prisma": "^5.7.0"
  }
}
```

---

## 🏃 RUNNING LOCALLY

### Development Mode

```bash
# Terminal 1 - Backend
cd backend
npm install
npx prisma generate
npx prisma migrate dev
npm run dev
# ✅ Backend: http://localhost:5000

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev
# ✅ Frontend: http://localhost:3000
```

### Environment Files

**frontend/.env:**
```bash
VITE_API_URL=http://localhost:5000/api
```

**backend/.env:**
```bash
DATABASE_URL="postgresql://user:password@localhost:5432/research_db"
OPENAI_API_KEY="sk-..."
YOUTUBE_API_KEY="AIza..."
DROPBOX_ACCESS_TOKEN="sl...."
FRONTEND_URL="http://localhost:3000"
PORT=5000
NODE_ENV="development"
```

---

## ✅ ADVANTAGES

### ✅ Разделенная архитектура

1. **Независимое масштабирование** - Backend и Frontend можно масштабировать отдельно
2. **Разные команды** - Команды могут работать параллельно
3. **Технологическая гибкость** - Можно заменить Frontend/Backend независимо
4. **Безопасность** - API Keys хранятся только на Backend
5. **Deployment** - Можно деплоить на разные платформы
6. **Testing** - Легче тестировать отдельно

### ✅ Express.js vs Next.js API Routes

| Feature | Express.js | Next.js API |
|---------|-----------|-------------|
| **Flexibility** | ✅ Полная свобода | ⚠️ Ограничено Next.js |
| **Middleware** | ✅ Богатая экосистема | ⚠️ Ограниченная |
| **Deployment** | ✅ Везде (Railway, Render, Heroku) | ⚠️ Vercel preferred |
| **WebSockets** | ✅ Полная поддержка | ❌ Сложно |
| **Real-time** | ✅ Socket.io, etc. | ⚠️ Ограничено |
| **Scaling** | ✅ Независимое | ⚠️ Вместе с Frontend |

---

## 📚 REFERENCES

- **Complete Prompt:** `COMPLETE-APP-GENERATION-PROMPT.md`
- **Design System:** `design-system.json`
- **Integration Guide:** `DESIGN-SYSTEM-INTEGRATION-GUIDE.md`
- **Functional Spec:** `FUNCTIONAL.md`

---

**Created:** 2025-12-09
**Architecture:** Separated Backend (Express.js) + Frontend (React)
**Status:** ✅ Ready for Implementation
