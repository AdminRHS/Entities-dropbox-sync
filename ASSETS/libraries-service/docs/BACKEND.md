# Backend Architecture

Complete guide to backend architecture and patterns.

## Overview

**Architecture**: Service Layer Pattern
**Framework**: Express.js
**ORM**: Sequelize
**Database**: PostgreSQL
**Cache**: Redis

## Directory Structure

```
src/
├── index.js              # Server entry point
├── routes/
│   ├── index.js          # Main router
│   └── *.js              # Entity routes
├── controllers/          # HTTP request handlers (28 files)
├── services/             # Business logic
│   ├── termsService.js
│   ├── aiService.js
│   ├── eventService.js
│   └── EventPublisherService.js
├── models/               # Sequelize models (35 files)
├── middleware/
│   ├── authMiddleware.js
│   ├── permissionCheck.js
│   ├── apiKeyAuth.js
│   ├── validation.js
│   └── uploadMiddleware.js
├── migrations/           # Database migrations (37 files)
├── seeders/              # Seed data
└── utils/
    ├── logger.js
    ├── redis.js
    └── termsUtils.js
```

## Service Layer Pattern

### Architecture
```
Client Request
    ↓
Controller (HTTP concerns)
    ↓
Service (Business logic)
    ↓
Model (Data access)
    ↓
Database
```

### Controller Example
```javascript
// src/controllers/professionController.js
exports.create = async (req, res) => {
  try {
    const profession = await professionService.create(req.body, req.user);
    res.status(201).json({ success: true, data: profession });
  } catch (error) {
    logger.error('Create profession failed', error);
    res.status(500).json({ success: false, error: error.message });
  }
};
```

### Service Example
```javascript
// src/services/professionService.js
exports.create = async (data, user) => {
  const transaction = await sequelize.transaction();
  try {
    // Business logic
    const termGroup = await createTermGroup(data.terms, transaction);
    const profession = await Profession.create({
      ...data,
      term_group_id: termGroup.id
    }, { transaction });

    // Publish event
    await eventService.publishProfessionCreated(profession);

    await transaction.commit();
    return profession;
  } catch (error) {
    await transaction.rollback();
    throw error;
  }
};
```

## Key Services

### 1. Terms Service
**Location**: `src/services/termsService.js`

**Purpose**: Manage multilingual terminology system

**Key Methods**:
- `createTermGroup(data)` - Create term group with terms
- `searchTerms(query, filters)` - Search across languages
- `addTermToGroup(groupId, termData)` - Add translation/synonym
- `getTermGroupWithAllTerms(id)` - Get full term data

### 2. Event Service
**Location**: `src/services/eventService.js`

**Purpose**: Publish entity change events

**Methods**: For each entity type:
- `publish{Entity}Created(entity)`
- `publish{Entity}Updated(entity, changedFields)`
- `publish{Entity}Deleted(entityId)`

**Event Format**:
```javascript
{
  sourceService: 'libraries-service',
  eventType: 'profession.created',
  eventData: { profession, timestamp, user }
}
```

## Middleware Stack

### Request Flow
```
1. Morgan (HTTP logging)
2. Helmet (Security headers)
3. CORS
4. Compression
5. express.json()
6. Rate Limiting
7. Auth Middleware
8. Permission Middleware
9. Validation Middleware
10. Controller
```

### Custom Middleware

**authMiddleware**: JWT validation
**permissionCheck**: RBAC
**apiKeyAuth**: API key validation
**validation**: Request validation (express-validator)
**uploadMiddleware**: File upload (Multer)

## Event Publishing

### Flow
```
Entity Change (Create/Update/Delete)
    ↓
Event Service
    ↓
API Gateway Event Hub
    ↓
Other Microservices (Subscribers)
```

### Example
```javascript
// After creating profession
await eventService.publishProfessionCreated(profession);

// Event published to API Gateway
POST /event-hub/publish
{
  sourceService: 'libraries-service',
  eventType: 'profession.created',
  eventData: {
    profession: { id, department_id, term_group_id },
    timestamp: '2025-01-12T10:00:00Z'
  }
}
```

## Logging

### Winston Configuration
**Location**: `src/utils/logger.js`

**Log Levels**: error, warn, info, http, debug

**Transports**:
- File: `logs/app.log`, `logs/error.log`
- Console: Development only

**Custom Methods**:
- `logger.api(method, endpoint, statusCode, duration)`
- `logger.sql(query, duration)`
- `logger.security(event, details)`
- `logger.performance(operation, duration)`

### Usage
```javascript
logger.info('Profession created', { professionId, userId });
logger.error('Database error', { error, context });
logger.api('POST', '/api/profession', 201, 150);
```

## Error Handling

### Global Error Handler
```javascript
app.use((err, req, res, next) => {
  logger.error('Error:', err);

  if (err.name === 'ValidationError') {
    return res.status(400).json({ success: false, error: err.message });
  }

  res.status(500).json({
    success: false,
    error: NODE_ENV === 'production' ? 'Internal server error' : err.message
  });
});
```

### Service Error Pattern
```javascript
try {
  // Business logic
} catch (error) {
  logger.error('Service error', { error, context });
  throw new Error(`Operation failed: ${error.message}`);
}
```

## File Upload

### Multer Configuration
**Location**: `src/middleware/uploadMiddleware.js`

**Storage**: `uploads/` directory
**File Types**: Images (jpeg, jpg, png, gif, svg)
**Size Limit**: 5MB
**Files**: 1 per request

**Usage**:
```javascript
router.post(
  '/upload-icon',
  authMiddleware,
  upload.single('icon'),
  async (req, res) => {
    const iconUrl = `/uploads/${req.file.filename}`;
    res.json({ success: true, iconUrl });
  }
);
```

## Caching Strategy

### Redis Usage
1. **API Key Validation**: 10 min TTL
2. **AI Configs**: 1 hour TTL
3. **Terms Cache**: 30 min TTL
4. **Session Data**: User-defined

**Example**:
```javascript
const cacheKey = `api_key:${apiKey}`;
const cached = await redis.get(cacheKey);

if (cached) return JSON.parse(cached);

const validation = await validateApiKey(apiKey);
await redis.setEx(cacheKey, 600, JSON.stringify(validation));
```

## File Locations

- **Entry**: `src/index.js`
- **Routes**: `src/routes/index.js`
- **Controllers**: `src/controllers/*.js`
- **Services**: `src/services/*.js`
- **Middleware**: `src/middleware/*.js`
- **Models**: `src/models/*.js`

---

**See Also**: [API.md](API.md), [AUTH.md](AUTH.md), [DATABASE.md](DATABASE.md)
