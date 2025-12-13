# Libraries Service - Comprehensive Documentation

## Quick Navigation

### For AI Agents

**First Time?** Start with this path:
1. [TECH_STACK.md](TECH_STACK.md) - Understand the technologies
2. [DATABASE.md](DATABASE.md) - Learn the data model
3. [API.md](API.md) - Explore the endpoints

**Working on Backend?** See:
- [BACKEND.md](BACKEND.md) - Architecture and patterns
- [API.md](API.md) - Endpoints and integration
- [AUTH.md](AUTH.md) - Authentication flow

**Working on Frontend?** See:
- [FRONTEND.md](FRONTEND.md) - React architecture
- [API.md](API.md) - API integration

**AI Features?** See:
- [MCP.md](MCP.md) - MCP server for AI agents (Claude, ChatGPT)

**Deploying?** See:
- [DEPLOYMENT.md](DEPLOYMENT.md) - Docker and environment

**Need to Develop?** See:
- [DEVELOPMENT.md](DEVELOPMENT.md) - Getting started and common tasks

### Core Documentation Files

| File | Description |
|------|-------------|
| [TECH_STACK.md](TECH_STACK.md) | Technologies, dependencies, architectural decisions |
| [DATABASE.md](DATABASE.md) | Complete database schema, models, relationships |
| [API.md](API.md) | All endpoints, request/response formats, integrations |
| [AUTH.md](AUTH.md) | Authentication flow, permissions, API keys |
| [FRONTEND.md](FRONTEND.md) | React architecture, components, state management |
| [BACKEND.md](BACKEND.md) | Services, controllers, middleware, patterns |
| [MCP.md](MCP.md) | Model Context Protocol server for AI agents |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Docker, environment variables, production |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Getting started, common tasks, workflows |
| [diagrams/](diagrams/) | Visual architecture diagrams |

---

## System Overview

### What is libraries-service?

A full-stack microservice for managing organizational entities, geographic data, and business entities with advanced features:

**Core Capabilities**:
- **Multilingual Terminology System**: 35+ models with translation support
- **MCP Server**: Direct DB access for AI agents via Model Context Protocol
- **External JWT Authentication**: Integration with auth-users-service
- **Event-Driven Architecture**: Publishes entity changes to API Gateway
- **Permission-Based Access Control**: Granular service.resource.action permissions
- **Full-Stack Application**: React frontend with Material-UI

**Key Statistics**:
- **Backend**: 35+ database models, 28 controllers, 37 migrations
- **Frontend**: 25+ pages, 60+ React components
- **MCP Server**: 9 tools for AI agents, multi-language support
- **Architecture**: Microservice with external auth, Redis caching, PostgreSQL

---

## Quick Start

### Development Setup

```bash
# Backend
npm install
cp .env.example .env
# Configure .env file
npm run dev  # Starts on port 3002

# Frontend (separate terminal)
cd client
npm install
npm run dev  # Starts on port 3000
```

### Docker Setup

```bash
# Set NODE_ENV in .env
NODE_ENV=development  # or production

# Start all services
docker-compose up -d

# Services:
# - app: http://localhost:3002
# - postgres: localhost:5432
# - redis: localhost:6379
# - pgadmin: http://localhost:5050 (dev only)
```

### Quick Test

```bash
# Health check
curl http://localhost:3002/health

# API info
curl http://localhost:3002/api/info

# Get departments (requires auth)
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:3002/api/department
```

---

## Architecture at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│                       CLIENT LAYER                          │
│                                                             │
│  React App (port 3000)                                      │
│  ├── Material-UI Components                                 │
│  ├── React Router (25+ pages)                               │
│  ├── Context API (Auth, Permissions, Theme)                 │
│  └── Axios API Services (27 endpoints)                      │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP + JWT
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    EXPRESS API LAYER                        │
│                                                             │
│  Express Server (port 3002)                                 │
│  ├── Routes (28 controllers)                                │
│  ├── Middleware                                             │
│  │   ├── authMiddleware (JWT validation)                    │
│  │   ├── permissionCheck (RBAC)                             │
│  │   ├── apiKeyAuth (API key validation)                    │
│  │   ├── validation (request validation)                    │
│  │   └── uploadMiddleware (file handling)                   │
│  ├── Services (business logic)                              │
│  └── Models (Sequelize ORM)                                 │
│                                                             │
└───┬───────────────┬───────────────┬─────────────────────────┘
    │               │               │
    ▼               ▼               ▼
┌─────────┐   ┌─────────┐   ┌──────────────┐
│PostgreSQL   │  Redis  │   │ API Gateway  │
│         │   │         │   │              │
│35+ tables   │ Cache   │   │ Auth Service │
│Terms    │   │ API keys│   │ Events       │
│MCP      │   │         │   │ Permissions  │
└─────────┘   └─────────┘   └──────────────┘
```

---

## File Locations Reference

### Backend Structure

| Component | Location |
|-----------|----------|
| **Server Entry** | `src/index.js` |
| **Routes Index** | `src/routes/index.js` |
| **Models** | `src/models/` (35+ files) |
| **Controllers** | `src/controllers/` (28+ files) |
| **Services** | `src/services/` |
| **Middleware** | `src/middleware/` |
| **Migrations** | `src/migrations/` (37 files) |
| **Seeders** | `src/seeders/` |
| **Config** | `config/config.js`, `src/config/` |
| **Utils** | `src/utils/` |

### Frontend Structure

| Component | Location |
|-----------|----------|
| **Entry Point** | `client/src/main.jsx` |
| **App Component** | `client/src/App.jsx` |
| **Pages** | `client/src/pages/` (25+ files) |
| **Components** | `client/src/components/` (60+ files) |
| **Contexts** | `client/src/contexts/` |
| **Services** | `client/src/services/` |
| **Hooks** | `client/src/hooks/` |
| **Themes** | `client/src/themes/` |
| **Config** | `client/src/config/` |

### Configuration Files

| File | Purpose |
|------|---------|
| `.env` | Environment variables (create from .env.example) |
| `docker-compose.yml` | Docker services configuration |
| `package.json` | Backend dependencies |
| `client/package.json` | Frontend dependencies |
| `config/config.js` | Database configuration |
| `.sequelizerc` | Sequelize CLI configuration |

---

## Common Workflows

### Adding New Entity

See [DEVELOPMENT.md#adding-new-entity](DEVELOPMENT.md#adding-new-entity)

**Steps**:
1. Create migration for new table
2. Create Sequelize model
3. Create service with business logic
4. Create controller with HTTP handlers
5. Add routes
6. Create frontend page
7. Create form dialogs
8. Add to navigation

### Database Changes

See [DEVELOPMENT.md#database-migrations](DEVELOPMENT.md#database-migrations)

**Steps**:
1. Generate migration: `npx sequelize-cli migration:generate --name description`
2. Implement `up` and `down` methods
3. Test migration: `npm run migrate` and `npm run migrate:undo`
4. Update model if needed
5. Commit migration file

### API Changes

See [DEVELOPMENT.md#api-modifications](DEVELOPMENT.md#api-modifications)

**Steps**:
1. Update service logic
2. Update controller handler
3. Update route if needed
4. Test with Postman/curl
5. Update frontend API service
6. Update components

### Frontend Features

See [DEVELOPMENT.md#frontend-features](DEVELOPMENT.md#frontend-features)

**Steps**:
1. Create/update page component
2. Add to routing in App.jsx
3. Create/update reusable components
4. Implement both table and card views
5. Add permission checks
6. Update navigation sidebar

---

## Critical Patterns

### 1. Terms System (Multilingual)

**Pattern**: All entities use `TermGroup` → `Terms` → `Languages`

**Why**: Centralized multilingual support, AI-friendly, no schema changes for new languages

**Example**:
```javascript
// Instead of direct text fields:
{ name: "Software Engineer", name_ru: "Программист" }

// Use term_group_id reference:
{
  term_group_id: 123,
  TermGroup: {
    MainTerm: { value: "Software Engineer", language_id: 1 },
    Terms: [
      { value: "Programmer", term_type: "similar", language_id: 1 },
      { value: "Программист", term_type: "translation", language_id: 2 }
    ]
  }
}
```

**Files**: [DATABASE.md#terms-system](DATABASE.md#terms-system)

### 2. Service Layer Pattern

**Pattern**: Controllers → Services → Models

**Why**: Testability, reusability, separation of concerns

**Example**:
```javascript
// Controller (HTTP concerns)
async getProfessions(req, res) {
  const result = await professionService.findAll(req.query);
  res.json({ success: true, data: result });
}

// Service (business logic)
async findAll(options) {
  return await Profession.findAndCountAll({
    include: [{ model: TermGroup, include: [Term] }],
    limit: options.limit,
    offset: (options.page - 1) * options.limit
  });
}
```

**Files**: [BACKEND.md#service-layer](BACKEND.md#service-layer)

### 3. Dual View Support

**Pattern**: All entity lists support Table + Card views

**Why**: User preference, responsive design, information density

**Components**: `DataTable`, `CardView`, `DataViewToggle`

**Files**: [FRONTEND.md#dual-view-pattern](FRONTEND.md#dual-view-pattern)

### 4. Permission-Based Access

**Pattern**: `service.resource.action` format (e.g., `libraries-service.profession.create`)

**Why**: Granular control, centralized permissions, wildcard support

**Example**:
```javascript
// Backend middleware
requirePermission('libraries-service', 'profession', 'create')

// Frontend guard
<PermissionRoute
  service="libraries-service"
  resource="profession"
  action="list"
/>
```

**Files**: [AUTH.md#permission-system](AUTH.md#permission-system)

### 5. Event Publishing

**Pattern**: Publish entity changes to API Gateway Event Hub

**Why**: Microservice communication, audit trail, real-time updates

**Example**:
```javascript
await eventService.publishProfessionCreated(profession);
await eventService.publishProfessionUpdated(profession, changedFields);
await eventService.publishProfessionDeleted(professionId);
```

**Files**: [BACKEND.md#event-system](BACKEND.md#event-system)

---

## Entity Relationships

### Core Entities

```
TermGroup (Multilingual container)
├── MainTerm → Term
├── Terms (translations, synonyms)
└── Used by ALL entities below

Department
├── Has many: Professions
└── Has: TermGroup

Profession
├── Belongs to: Department
├── Has many: Tools
└── Has: TermGroup

Country
├── Has many: Cities
├── Has: Currency
└── Has: TermGroup

Industry
├── Has many: SubIndustries
└── Has: TermGroup

Responsibility = Action + Object
Skill = Responsibility + Tool
```

**Full Diagram**: [DATABASE.md#entity-relationships](DATABASE.md#entity-relationships)

---

## Environment Variables

### Critical Variables

```bash
# Database
DB_NAME=libraries_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379

# External Services
API_GATEWAY_URL=http://localhost:3003/api

# Frontend
CLIENT_URL=http://localhost:3000
VITE_API_URL=http://localhost:3002/api
VITE_API_GATEWAY_URL=http://localhost:3003/api

# Security
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001

# Features
NODE_ENV=development
PORT=3002
```

**Full List**: [DEPLOYMENT.md#environment-variables](DEPLOYMENT.md#environment-variables)

---

## API Endpoints Overview

### Entity Management (CRUD)

| Resource | Endpoint | Description |
|----------|----------|-------------|
| Departments | `/api/department` | Department management |
| Professions | `/api/profession` | Profession management |
| Tools | `/api/tools` | Tool management |
| Countries | `/api/countries` | Country data |
| Cities | `/api/cities` | City data |
| Industries | `/api/industries` | Industry data |
| Actions | `/api/action` | Action verbs |
| Objects | `/api/object` | Object nouns |
| Responsibilities | `/api/responsibilities` | Responsibilities |
| Skills | `/api/skills` | Skills |
| Languages | `/api/language` | Languages |
| Statuses | `/api/status` | Statuses |
| Priorities | `/api/priority` | Priorities |

### Terms System

| Endpoint | Description |
|----------|-------------|
| `/api/terms/groups` | Term group management |
| `/api/terms/search` | Search terms |
| `/api/terms/autocomplete` | Term suggestions |
| `/api/terms/professions` | Profession terms |
| `/api/terms/departments` | Department terms |

### MCP Server

| Endpoint | Description |
|----------|-------------|
| `/mcp` | MCP protocol endpoint |
| `/mcp/health` | MCP health check |

### System

| Endpoint | Description |
|----------|-------------|
| `/health` | Health check |
| `/api/info` | API information |
| `/api/stats/comprehensive` | System statistics |

**Full API Docs**: [API.md](API.md)

---

## Technology Stack Summary

### Backend
- **Runtime**: Node.js 16+
- **Framework**: Express.js 4.18.2
- **Database**: PostgreSQL 12+ with Sequelize ORM 6.35.1
- **Cache**: Redis 5.5.6
- **Logging**: Winston 3.17.0
- **Security**: Helmet, CORS, express-rate-limit
- **File Upload**: Multer 2.0.2

### Frontend
- **Framework**: React 19.1.0
- **Build Tool**: Vite 6.3.5
- **UI Library**: Material-UI 7.1.1
- **Routing**: React Router 7.6.2
- **Styling**: Emotion (CSS-in-JS)
- **HTTP**: Axios 1.9.0

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **CI/CD**: Bitbucket Pipelines

**Full Tech Stack**: [TECH_STACK.md](TECH_STACK.md)

---

## Database Statistics

- **DBMS**: PostgreSQL 12+
- **ORM**: Sequelize 6.35.1
- **Total Models**: 35
- **Total Migrations**: 37
- **Junction Tables**: 5 (many-to-many relationships)
- **Key Features**: JSONB columns, full-text search, multilingual support, AI metadata

**Full Schema**: [DATABASE.md](DATABASE.md)

---

## Getting Help

### Documentation Structure

Each documentation file is designed to be:
- **Scannable**: Clear headings, tables, lists
- **Complete**: All essential information
- **Practical**: Code examples, file paths, patterns
- **Cross-referenced**: Links between related topics

### Quick References

- **API Examples**: [API.md#examples](API.md#examples)
- **Common Queries**: [DATABASE.md#common-queries](DATABASE.md#common-queries)
- **Troubleshooting**: [DEVELOPMENT.md#troubleshooting](DEVELOPMENT.md#troubleshooting)
- **Best Practices**: Each file has a "Best Practices" section

### Project Guidelines

See [CLAUDE.md](../CLAUDE.md) in project root for Claude Code specific guidance.

---

## Contributing

### Before Making Changes

1. Read relevant documentation files
2. Understand existing patterns
3. Check [DEVELOPMENT.md](DEVELOPMENT.md) for workflows
4. Follow architectural decisions in [TECH_STACK.md](TECH_STACK.md)

### Code Standards

- Follow existing service layer pattern
- Use Terms system for all new entities
- Implement permission checks
- Add both table and card views for frontend
- Write migrations for database changes
- Publish events for entity changes
- Add logging for important operations

---

## Documentation Maintenance

This documentation should be updated when:
- New entities are added
- API endpoints change
- Authentication/authorization changes
- New AI providers are added
- Deployment process changes
- Major architectural decisions are made

Each file has a "Last Updated" section at the bottom.

---

**Last Updated**: 2025-01-12
**Documentation Version**: 1.0
**Project Version**: See package.json
