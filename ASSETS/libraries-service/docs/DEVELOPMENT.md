# Development Guide

Getting started and common development tasks.

## Quick Start

### Prerequisites
- Node.js 16+
- PostgreSQL 12+
- Redis 5+
- npm 8+

### Setup
```bash
# Clone repository
git clone <repo-url>
cd libraries-service

# Install backend dependencies
npm install

# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Setup database
npx sequelize-cli db:migrate --migrations-path src/migrations
npm run seed  # Optional: seed data

# Start backend
npm run dev  # Runs on port 3002

# In another terminal, start frontend
cd client
npm install
npm run dev  # Runs on port 3000
```

### Access
- Frontend: http://localhost:3000
- Backend API: http://localhost:3002/api
- Health: http://localhost:3002/health

## Common Tasks

### Adding New Entity

**1. Create Migration**
```bash
npx sequelize-cli migration:generate --name create-entity-name
```

**2. Implement Migration**
```javascript
// src/migrations/XXXXXX-create-entity-name.js
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('entity_names', {
      id: { type: Sequelize.INTEGER, primaryKey: true, autoIncrement: true },
      term_group_id: { type: Sequelize.INTEGER, references: { model: 'term_groups', key: 'id' } },
      createdAt: { type: Sequelize.DATE },
      updatedAt: { type: Sequelize.DATE }
    });
  },
  down: async (queryInterface) => {
    await queryInterface.dropTable('entity_names');
  }
};
```

**3. Create Model**
```javascript
// src/models/entityName.js
module.exports = (sequelize, DataTypes) => {
  const EntityName = sequelize.define('EntityName', {
    id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    term_group_id: { type: DataTypes.INTEGER }
  });

  EntityName.associate = (models) => {
    EntityName.belongsTo(models.TermGroup, { foreignKey: 'term_group_id' });
  };

  return EntityName;
};
```

**4. Create Service**
```javascript
// src/services/entityNameService.js
const { EntityName, TermGroup } = require('../models');

exports.findAll = async (options) => {
  return await EntityName.findAndCountAll({
    include: [{ model: TermGroup, include: ['Terms'] }],
    limit: options.limit,
    offset: (options.page - 1) * options.limit
  });
};

exports.create = async (data) => {
  return await EntityName.create(data);
};

// ... other methods
```

**5. Create Controller**
```javascript
// src/controllers/entityNameController.js
const entityNameService = require('../services/entityNameService');

exports.getAll = async (req, res) => {
  try {
    const result = await entityNameService.findAll(req.query);
    res.json({ success: true, data: result });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};

// ... other methods
```

**6. Create Routes**
```javascript
// src/routes/entityName.js
const router = require('express').Router();
const controller = require('../controllers/entityNameController');
const { authMiddleware } = require('../middleware/authMiddleware');
const { requirePermission } = require('../middleware/permissionCheck');

router.get('/', authMiddleware, controller.getAll);
router.post('/', authMiddleware, requirePermission('libraries-service', 'entity-name', 'create'), controller.create);

module.exports = router;
```

**7. Register Routes**
```javascript
// src/routes/index.js
app.use('/api/entity-name', require('./entityName'));
```

**8. Create Frontend Page**
```jsx
// client/src/pages/EntityNames.jsx
function EntityNames() {
  // Use standard entity page pattern
  // See FRONTEND.md for template
}
```

**9. Add to Navigation**
```jsx
// client/src/components/Sidebar.jsx
{ name: 'Entity Names', path: '/entity-names', icon: <Icon /> }
```

### Database Migrations

**Run Migrations**
```bash
npx sequelize-cli db:migrate --migrations-path src/migrations
```

**Rollback Last Migration**
```bash
npx sequelize-cli db:migrate:undo --migrations-path src/migrations
```

**Check Status**
```bash
npx sequelize-cli db:migrate:status --migrations-path src/migrations
```

### Testing

**Run Tests**
```bash
npm test
npm run test:watch
npm run test:coverage
```

**Write Tests**
```javascript
// src/tests/entity.test.js
const request = require('supertest');
const app = require('../app');

describe('Entity API', () => {
  it('should get all entities', async () => {
    const response = await request(app)
      .get('/api/entity-name')
      .set('Authorization', 'Bearer ' + token)
      .expect(200);

    expect(response.body.success).toBe(true);
  });
});
```

## Troubleshooting

### Database Connection Issues
```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Check connection
psql -h localhost -U postgres -d libraries_db

# Reset database
npx sequelize-cli db:drop
npx sequelize-cli db:create
npx sequelize-cli db:migrate --migrations-path src/migrations
```

### Redis Connection Issues
```bash
# Check Redis is running
docker ps | grep redis

# Test connection
redis-cli ping
```

### Frontend Build Issues
```bash
# Clear node_modules
cd client
rm -rf node_modules
npm install

# Clear Vite cache
rm -rf node_modules/.vite
```

### Port Already in Use
```bash
# Find process using port
lsof -i :3002  # Backend
lsof -i :3000  # Frontend

# Kill process
kill -9 <PID>
```

## Code Style

### Backend
- Use async/await (not promises)
- Service layer for business logic
- Controllers only handle HTTP
- Always use transactions for multi-step operations
- Log errors with context
- Validate input with express-validator

### Frontend
- Functional components with hooks
- Use Context for global state
- Keep components small and focused
- Extract reusable logic to custom hooks
- Follow Material-UI patterns
- Handle loading/error states

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/entity-name

# Make changes
git add .
git commit -m "Add entity name feature"

# Push and create PR
git push origin feature/entity-name
```

## Useful Commands

```bash
# Backend
npm run dev          # Start with nodemon
npm start            # Start production
npm run seed         # Seed database
npm test             # Run tests

# Frontend
cd client
npm run dev          # Start Vite dev server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint

# Docker
docker-compose up -d                    # Start all services
docker-compose logs -f app              # View logs
docker-compose exec postgres psql -U postgres  # Access PostgreSQL
docker-compose exec redis redis-cli     # Access Redis
```

---

**See Also**: [DEPLOYMENT.md](DEPLOYMENT.md), [API.md](API.md), [DATABASE.md](DATABASE.md)
