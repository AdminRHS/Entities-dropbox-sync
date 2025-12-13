# Architecture Diagrams

This folder contains visual architecture diagrams for the libraries-service microservice.

## System Architecture

```
┌──────────────────┐
│  React Frontend  │  (Port 3000)
│  Material-UI     │
└────────┬─────────┘
         │ HTTP + JWT
         ▼
┌──────────────────┐
│  Express API     │  (Port 3002)
│  + Sequelize     │
└────┬────┬────┬───┘
     │    │    │
     ▼    ▼    ▼
   ┌──┐ ┌──┐ ┌────────┐
   │PG│ │Re│ │Gateway │
   │DB│ │dis│ │ + Auth │
   └──┘ └──┘ └────┬───┘
                   │
                   ▼
              ┌────────┐
              │  AI    │
              │Providers
              └────────┘
```

## Database Schema (Simplified)

```
TermGroup (Central)
├── MainTerm → Term
├── Terms[] (translations, synonyms)
└── Used by ALL entities:
    ├── Department
    ├── Profession
    ├── Country
    ├── City
    ├── Industry
    └── ... (20+ entities)

Department → Profession[]
Profession → Tool[] (M:N)
Country → City[]
Industry → SubIndustry[]

AI System:
AIConfig → AIGeneration[]
AIPrompt → AIGeneration[]
```

## Authentication Flow

```
1. User Login
   ↓
2. Auth Service (JWT)
   ↓
3. Access Token + Refresh Cookie
   ↓
4. Client → libraries-service
   ↓
5. Validate Token (cached 10min)
   ↓
6. Check Permissions
   ↓
7. Process Request
```

## AI Generation Flow

```
1. Select AI Config (provider + model)
   ↓
2. Select Prompt Template
   ↓
3. Provide Input Data
   ↓
4. Call AI Provider API
   ↓
5. Save to AIGeneration
   ↓
6. Validate & Score
   ↓
7. Human Review (optional)
   ↓
8. Apply to Entity
```

## Terms System Pattern

```
Entity (Profession/Department/etc.)
  ├── term_group_id
  └── TermGroup
       ├── name: "Software Engineer"
       ├── MainTerm
       │    └── value: "Software Engineer" (en)
       └── Terms[]
            ├── "Software Engineer" (en, main)
            ├── "Programmer" (en, similar)
            ├── "Программист" (ru, translation)
            └── "Програміст" (uk, translation)
```

## API Request Flow

```
Client Request
  ↓
CORS Check
  ↓
Rate Limiting
  ↓
Auth Middleware (JWT validation)
  ↓
Permission Check (RBAC)
  ↓
Validation Middleware
  ↓
Controller (HTTP)
  ↓
Service (Business Logic)
  ↓
Model (ORM)
  ↓
Database
  ↓
Event Publishing (if entity changed)
  ↓
Response
```

## Technologies Overview

### Backend
- Node.js 16+ + Express.js 4
- PostgreSQL 12+ + Sequelize 6
- Redis 5+ (caching)
- Winston (logging)
- Helmet + CORS (security)

### Frontend
- React 19 + Vite 6
- Material-UI 7
- React Router 7
- Context API (state)
- Axios (HTTP)

### Infrastructure
- Docker + Docker Compose
- PostgreSQL container
- Redis container
- PgAdmin (dev)

---

For detailed architecture information, see the main documentation files in the parent directory.

