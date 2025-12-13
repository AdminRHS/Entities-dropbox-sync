# API Documentation

Complete API reference for libraries-service microservice.

## Overview

- **Base URL**: `http://localhost:3002/api`
- **Protocol**: HTTP/HTTPS
- **Format**: JSON
- **Authentication**: JWT Bearer Token or API Key
- **Rate Limiting**: 100 requests / 15 minutes (general), 50 requests / minute (search)

## Authentication

### JWT Token (Primary)

**Header**:
```http
Authorization: Bearer <access_token>
```

**Obtaining Token**: Via [auth-users-service](AUTH.md#external-jwt-authentication)

**Token Validation**: Automatic via `authMiddleware`

### API Key (MCP Server)

**Headers**:
```http
X-API-Key: <api_key>
X-API-Token: <api_key>
```

**Usage**: For MCP protocol communications and service-to-service requests

See [AUTH.md](AUTH.md) for detailed authentication flows.

## Standard Response Format

### Success Response

```json
{
  "success": true,
  "data": {
    "rows": [...],
    "count": 100
  },
  "pagination": {
    "total": 100,
    "page": 1,
    "limit": 20,
    "pages": 5
  }
}
```

### Error Response

```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

### HTTP Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `401` - Unauthorized (missing or invalid token)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

## Common Query Parameters

All list endpoints support:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number (1-indexed) |
| `limit` | integer | 20 | Items per page (max: 100) |
| `search` | string | - | Search term (case-insensitive) |
| `sortBy` | string | 'id' | Field to sort by |
| `sortOrder` | string | 'ASC' | Sort direction (ASC/DESC) |

**Example**:
```http
GET /api/profession?page=2&limit=50&search=engineer&sortBy=createdAt&sortOrder=DESC
```

---

## Core Entity Endpoints

All entities follow standard REST pattern with 5 basic operations.

### Departments

**Base Path**: `/api/department`

#### List Departments
```http
GET /api/department?page=1&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "id": 1,
        "term_group_id": 123,
        "TermGroup": {
          "id": 123,
          "name": "Engineering",
          "main_term_id": 456,
          "MainTerm": {
            "id": 456,
            "value": "Engineering",
            "language_id": 1
          },
          "Terms": [
            { "value": "Engineering", "term_type": "main" },
            { "value": "Инженерия", "term_type": "translation", "language_id": 2 }
          ]
        },
        "createdAt": "2025-01-10T12:00:00Z",
        "updatedAt": "2025-01-10T12:00:00Z"
      }
    ],
    "count": 15
  }
}
```

#### Create Department
```http
POST /api/department
Content-Type: application/json

{
  "term_group_id": 123
}
```

**Response**: `201 Created`

#### Get Department by ID
```http
GET /api/department/1
```

#### Update Department
```http
PUT /api/department/1
Content-Type: application/json

{
  "term_group_id": 456
}
```

#### Delete Department
```http
DELETE /api/department/1
```

**Response**: `200 OK` or `204 No Content`

#### Get Department Terms
```http
GET /api/department/terms/all?page=1&limit=20
```

**Permission Required**: `libraries-service.department.list`

---

### Professions

**Base Path**: `/api/profession`

#### Create Profession (with icon upload)
```http
POST /api/profession
Content-Type: multipart/form-data

{
  "term_group_id": 789,
  "department_id": 1,
  "icon": <File>,
  "toolIds": [1, 2, 3]
}
```

**Response**: `201 Created`

#### Update Profession (with icon upload)
```http
PUT /api/profession/5
Content-Type: multipart/form-data

{
  "term_group_id": 789,
  "department_id": 2,
  "icon": <File>,  // optional
  "toolIds": [4, 5]
}
```

#### Get Professions with Terms
```http
GET /api/profession/terms?page=1&limit=20&language_id=1
```

**Response**:
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "id": 5,
        "department_id": 1,
        "icon_path": "/uploads/icons/profession_5.png",
        "TermGroup": {
          "MainTerm": { "value": "Software Engineer" },
          "Terms": [
            { "value": "Software Engineer", "language_id": 1 },
            { "value": "Программист", "language_id": 2 }
          ]
        },
        "Tools": [
          { "id": 1, "name": "JavaScript" },
          { "id": 2, "name": "React" }
        ]
      }
    ],
    "count": 120
  }
}
```

**Permission Required**: `libraries-service.profession.create/update/delete`

---

### Tools

**Base Path**: `/api/tools`

#### Create Tool (with icon upload)
```http
POST /api/tools
Content-Type: multipart/form-data

{
  "name": "React",
  "link": "https://react.dev",
  "description": "JavaScript library for building user interfaces",
  "toolTypeIds": [1, 2],
  "icon": <File>
}
```

#### Get Tool by ID (from Gateway)
```http
GET /api/libraries/tools/:id?includeTypes=true
```
Uses `gatewayApi` instance for cross-service communication.

**Permission Required**: `libraries-service.tool.create/update`

---

### Actions

**Base Path**: `/api/action`

Actions are verbs used in responsibilities (e.g., "Develop", "Design", "Implement").

#### Create Action
```http
POST /api/action
Content-Type: multipart/form-data

{
  "term_group_id": 100,
  "icon": <File>  // optional
}
```

#### Get All Action Terms
```http
GET /api/action/terms?page=1&limit=50
```

**Permission Required**: `libraries-service.action.create/delete`

---

### Objects

**Base Path**: `/api/object`

Objects are nouns used in responsibilities (e.g., "Web Application", "API", "Database").

#### Create Object
```http
POST /api/object
Content-Type: multipart/form-data

{
  "term_group_id": 200,
  "formatIds": [1, 2],  // Associated file formats
  "icon": <File>  // optional
}
```

**Permission Required**: `libraries-service.object.create/delete`

---

### Responsibilities

**Base Path**: `/api/responsibilities`

Responsibilities are composites of Action + Object (e.g., "Develop Web Application").

#### Create Responsibility
```http
POST /api/responsibilities
Content-Type: application/json

{
  "action_id": 1,
  "object_id": 5,
  "term_group_id": 300
}
```

#### Get Responsibilities with Terms
```http
GET /api/responsibilities/terms?page=1&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "id": 10,
        "action_id": 1,
        "object_id": 5,
        "Action": {
          "TermGroup": { "MainTerm": { "value": "Develop" } }
        },
        "Object": {
          "TermGroup": { "MainTerm": { "value": "Web Application" } }
        },
        "TermGroup": {
          "MainTerm": { "value": "Develop Web Application" }
        }
      }
    ],
    "count": 50
  }
}
```

#### Find Existing Terms by Language
```http
GET /api/responsibilities/find-existing-terms?action_id=1&object_id=5&language_id=1
```

**Permission Required**: `libraries-service.responsibility.create/delete`

---

### Skills

**Base Path**: `/api/skills`

Skills are composites of Responsibility + Tool (e.g., "Develop Web Application using React").

#### Create Skill
```http
POST /api/skills
Content-Type: application/json

{
  "responsibility_id": 10,
  "tool_id": 2,
  "term_group_id": 400
}
```

#### Get Skills with Terms
```http
GET /api/skills/terms?page=1&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "id": 15,
        "responsibility_id": 10,
        "tool_id": 2,
        "Responsibility": {
          "Action": { "TermGroup": { "MainTerm": { "value": "Develop" } } },
          "Object": { "TermGroup": { "MainTerm": { "value": "Web Application" } } }
        },
        "Tool": { "name": "React" },
        "TermGroup": {
          "MainTerm": { "value": "Develop Web Application using React" }
        }
      }
    ],
    "count": 200
  }
}
```

**Permission Required**: `libraries-service.skill.create/delete`

---

### Geographic Entities

#### Countries
**Base Path**: `/api/countries`

```http
GET /api/countries?page=1&limit=50

POST /api/countries
{
  "iso2": "US",
  "iso3": "USA",
  "currency_id": 1,
  "term_group_id": 500
}
```

#### Cities
**Base Path**: `/api/cities`

```http
GET /api/cities?page=1&limit=50&country_id=1

POST /api/cities
{
  "country_id": 1,
  "latitude": "40.7128",
  "longitude": "-74.0060",
  "term_group_id": 600
}
```

#### Industries
**Base Path**: `/api/industries`

```http
GET /api/industries?page=1&limit=20

GET /api/industries/terms?language_id=1
```

#### Sub-Industries
**Base Path**: `/api/sub-industries`

```http
GET /api/sub-industries?page=1&limit=20&industry_id=1
```

---

### Metadata Entities

#### Statuses
**Base Path**: `/api/status`

Global status values (Active, Inactive, Pending, etc.)

#### Priorities
**Base Path**: `/api/priority`

Priority levels (High, Medium, Low, etc.)

#### Languages
**Base Path**: `/api/language`

```http
GET /api/language?page=1&limit=20

POST /api/language
{
  "iso2": "en",
  "iso3": "eng",
  "term_group_id": 700
}

GET /api/language/terms?page=1&limit=50
```

#### Services
**Base Path**: `/api/services`

Business services definitions.

#### Shifts
**Base Path**: `/api/shifts`

Work shift definitions.

#### Positions
**Base Path**: `/api/positions`

Job position levels (Junior, Senior, Lead, etc.)

```http
GET /api/positions/terms?language_id=1
```

#### Levels
**Base Path**: `/api/levels`

Experience levels (Entry, Mid, Senior, Expert).

```http
GET /api/levels/terms?page=1&limit=20
```

#### Formats
**Base Path**: `/api/formats`

File and content format types.

#### Tool Types
**Base Path**: `/api/tool-type`

Tool categorization (Programming Language, Framework, Database, etc.)

#### Currencies
**Base Path**: `/api/currencies`

Currency definitions (USD, EUR, GBP, etc.)

```http
GET /api/currencies?page=1&limit=50

POST /api/currencies
{
  "code": "USD",
  "symbol": "$",
  "name": "US Dollar"
}
```

#### Rates
**Base Path**: `/api/rates`

Currency exchange rates.

```http
GET /api/rates?page=1&limit=20&from_currency_id=1

POST /api/rates
{
  "from_currency_id": 1,
  "to_currency_id": 2,
  "rate": "1.25"
}
```

---

## Terms System API

### Term Groups

#### List Term Groups
```http
GET /api/terms/groups?page=1&limit=20
```

#### Create Term Group
```http
POST /api/terms/groups
Content-Type: application/json

{
  "name": "Software Engineering",
  "main_term_id": 123,
  "icon": "💻"
}
```

**Response**: `201 Created`

### Terms Search

#### Search Terms
```http
GET /api/terms/search?q=engineer&language_id=1&page=1&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "id": 456,
        "value": "Software Engineer",
        "language_id": 1,
        "term_type_id": 1,
        "term_group_id": 123,
        "ai_generated": false,
        "ai_quality_score": null,
        "Language": { "iso2": "en", "name": "English" },
        "TermType": { "name": "main" }
      }
    ],
    "count": 15
  }
}
```

**Query Parameters**:
- `q` - Search term (required, min 2 chars)
- `language_id` - Filter by language
- `term_type_id` - Filter by term type (main/similar/translation)
- `page` - Page number
- `limit` - Results per page

**Rate Limit**: 50 requests / minute

#### Autocomplete Suggestions
```http
GET /api/terms/autocomplete?q=eng&limit=10
```

**Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": 456,
      "value": "Engineering",
      "language_id": 1,
      "term_group_id": 123
    }
  ]
}
```

### Term Operations

#### Get Professions with Terms
```http
GET /api/terms/professions?language_id=1&page=1&limit=20
```

#### Get Departments with Terms
```http
GET /api/terms/departments?language_id=1&page=1&limit=20
```

#### Get Term Types
```http
GET /api/terms/types
```

**Response**:
```json
{
  "success": true,
  "data": [
    { "id": 1, "name": "main" },
    { "id": 2, "name": "similar" },
    { "id": 3, "name": "translation" }
  ]
}
```

#### Get Term Languages
```http
GET /api/terms/languages
```

#### Get Term Statistics
```http
GET /api/terms/stats
```

**Response**:
```json
{
  "success": true,
  "data": {
    "total_term_groups": 500,
    "total_terms": 2000,
    "terms_by_language": [
      { "language_id": 1, "count": 1200 },
      { "language_id": 2, "count": 800 }
    ],
    "terms_by_type": [
      { "term_type": "main", "count": 500 },
      { "term_type": "translation", "count": 1000 },
      { "term_type": "similar", "count": 500 }
    ]
  }
}
```

#### Get All Terms
```http
GET /api/terms/terms?page=1&limit=100
```

#### Delete Term
```http
DELETE /api/terms/:id
```

**Permission Required**: `libraries-service.term.delete`

---

## AI Generation API

### Generate Profession Data

```http
POST /api/ai/generate/profession
Content-Type: application/json

{
  "title": "Senior Backend Developer",
  "industry": "technology",
  "level": "senior",
  "department": "Engineering",
  "language": "en"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "description": "A senior backend developer responsible for...",
    "skills": ["Node.js", "PostgreSQL", "Docker"],
    "responsibilities": ["Design scalable APIs", "Mentor junior developers"],
    "requirements": "5+ years of experience",
    "salary_range": "$100,000 - $150,000"
  },
  "metadata": {
    "generationId": "abc123",
    "provider": "openai",
    "model": "gpt-4",
    "tokensUsed": 1500,
    "cost": 0.045,
    "duration_ms": 2300
  }
}
```

### Generate Department Data

```http
POST /api/ai/generate/department
Content-Type: application/json

{
  "name": "Product Management",
  "company_size": "mid",
  "industry": "technology"
}
```

### Generate Terms

```http
POST /api/ai/generate/terms
Content-Type: application/json

{
  "term": "Software Engineer",
  "source_language": "en",
  "target_languages": ["ru", "es", "de"],
  "context": "IT industry job title"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "translations": {
      "ru": "Программист",
      "es": "Ingeniero de Software",
      "de": "Software-Ingenieur"
    },
    "similar_terms": ["Developer", "Programmer", "Coder"]
  },
  "metadata": {
    "generationId": "xyz789",
    "qualityScore": 0.95
  }
}
```

### Batch Generation

```http
POST /api/ai/generate/batch
Content-Type: application/json

{
  "requests": [
    { "type": "profession", "data": { "title": "DevOps Engineer" } },
    { "type": "profession", "data": { "title": "QA Engineer" } }
  ],
  "options": {
    "parallel": true,
    "maxConcurrent": 3
  }
}
```

### Apply Generated Content

```http
POST /api/ai/apply/:generation_id
Content-Type: application/json

{
  "approved": true,
  "modifications": {
    "description": "Updated description..."
  }
}
```

### List Generations

```http
GET /api/ai/generations?page=1&limit=20&status=completed
```

**Query Parameters**:
- `status` - Filter by status (pending/completed/failed)
- `provider` - Filter by AI provider
- `entity_type` - Filter by entity type (profession/department/term)

### AI Prompts Management

```http
GET /api/ai/prompts?category=profession
POST /api/ai/prompts
PUT /api/ai/prompts/:id
DELETE /api/ai/prompts/:id
```

### AI Configurations

```http
GET /api/ai/configs
POST /api/ai/configs
PUT /api/ai/configs/:id
```

### AI Statistics

```http
GET /api/ai/stats
```

**Response**:
```json
{
  "success": true,
  "data": {
    "total_generations": 1500,
    "total_tokens_used": 500000,
    "total_cost": 15.75,
    "avg_quality_score": 0.92,
    "by_provider": {
      "openai": 800,
      "anthropic": 500,
      "google": 200
    }
  }
}
```

### AI Dashboard

```http
GET /api/ai/dashboard
```

**Permission Required**: `libraries-service.ai.generate`

---

## MCP (Model Context Protocol) API

### MCP Server Endpoint

```http
POST /mcp
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response** (SSE Stream):
```
data: {"jsonrpc":"2.0","id":1,"result":{"tools":[...]}}
```

See [MCP.md](MCP.md) for detailed MCP protocol documentation.

### MCP Health Check

```http
GET /mcp/health
```

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2025-01-12T10:00:00Z",
  "tools_count": 9
}
```

---

## System Endpoints

### Health Check

```http
GET /health
```

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2025-01-12T10:00:00Z",
  "uptime": 86400
}
```

### Detailed Health Check

```http
GET /health/detailed
```

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2025-01-12T10:00:00Z",
  "uptime": 86400,
  "database": "connected",
  "redis": "connected",
  "memory": {
    "heapUsed": 120,
    "heapTotal": 200,
    "external": 15
  }
}
```

### API Information

```http
GET /api/info
```

**Response**:
```json
{
  "name": "Libraries Service API",
  "version": "2.0.0",
  "description": "API для управления библиотеками с поддержкой системы терминов и ИИ",
  "features": [
    "Управление департаментами и профессиями",
    "Система терминов с поддержкой переводов",
    "AI-генерация контента"
  ],
  "endpoints": {
    "legacy": {...},
    "terms": {...},
    "ai": {...}
  }
}
```

### Comprehensive Statistics

```http
GET /api/stats/comprehensive
```

**Response**:
```json
{
  "success": true,
  "data": {
    "system": {
      "uptime": 86400,
      "memory": {...},
      "version": "2.0.0"
    },
    "terms": {
      "total_term_groups": 500,
      "total_terms": 2000
    },
    "ai": {
      "total_generations": 1500,
      "total_tokens_used": 500000,
      "total_cost": "15.75"
    }
  }
}
```

### Global Search

```http
GET /api/search/global?q=engineer&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": {
    "terms": [...],
    "professions": [...],
    "total": {
      "terms": 10,
      "professions": 5
    }
  }
}
```

### API Compatibility Check

```http
GET /api/compatibility
```

**Response**:
```json
{
  "success": true,
  "data": {
    "legacy_api": "supported",
    "terms_api": "active",
    "ai_api": "active",
    "migration_status": "available",
    "breaking_changes": [],
    "deprecated_endpoints": [],
    "new_features": [
      "Terms management system",
      "Multi-language support",
      "AI-powered content generation"
    ]
  }
}
```

---

## Error Codes

### Common Errors

| Code | Message | HTTP Status |
|------|---------|-------------|
| `AUTH_TOKEN_INVALID` | Invalid or expired token | 401 |
| `AUTH_TOKEN_MISSING` | Authorization header missing | 401 |
| `PERMISSION_DENIED` | Insufficient permissions | 403 |
| `VALIDATION_ERROR` | Request validation failed | 400 |
| `NOT_FOUND` | Resource not found | 404 |
| `RATE_LIMIT_EXCEEDED` | Too many requests | 429 |
| `DB_CONNECTION_ERROR` | Database connection failed | 500 |
| `REDIS_CONNECTION_ERROR` | Redis connection failed | 500 |

### Error Response Example

```json
{
  "success": false,
  "error": "Validation failed",
  "code": "VALIDATION_ERROR",
  "details": {
    "field": "term_group_id",
    "message": "term_group_id is required"
  }
}
```

---

## Rate Limiting

### Limits by Endpoint Type

| Endpoint Type | Limit | Window |
|---------------|-------|--------|
| General API | 100 requests | 15 minutes |
| Search (`/terms/search`) | 50 requests | 1 minute |
| Autocomplete | 50 requests | 1 minute |
| AI Generation | 20 requests | 1 hour |
| MCP Protocol | 100 requests | 15 minutes |

### Rate Limit Headers

**Response Headers**:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1673548800
```

### Exceeding Rate Limit

**Response**: `429 Too Many Requests`
```json
{
  "success": false,
  "error": "Rate limit exceeded. Try again in 15 minutes.",
  "code": "RATE_LIMIT_EXCEEDED",
  "retryAfter": 900
}
```

---

## Best Practices

1. **Use Pagination**: Always specify `page` and `limit` for list endpoints
2. **Handle Errors**: Check `success` field in all responses
3. **Cache Responses**: Cache static data (languages, term types, etc.)
4. **Retry Logic**: Implement exponential backoff for failed requests
5. **Rate Limit Awareness**: Monitor `X-RateLimit-*` headers
6. **Token Refresh**: Implement automatic token refresh on 401 errors
7. **Permissions**: Request only necessary permissions
8. **Search Optimization**: Use `autocomplete` for real-time suggestions instead of full search

---

**See Also**:
- [AUTH.md](AUTH.md) - Authentication and permissions
- [BACKEND.md](BACKEND.md) - Backend architecture
- [MCP.md](MCP.md) - MCP protocol details
- [FRONTEND.md](FRONTEND.md) - Frontend API integration

**Last Updated**: 2025-01-12
