# Deployment Guide

Deployment and configuration guide.

## Docker Setup

### Services
```yaml
services:
  app:        # Node.js + Express + React build
  postgres:   # PostgreSQL 15-alpine
  redis:      # Redis 7-alpine
  pgadmin:    # PgAdmin (dev only)
```

### Commands
```bash
# Start all services
docker-compose up -d

# Development mode (with pgadmin)
NODE_ENV=development docker-compose --profile development up -d

# Production mode
NODE_ENV=production docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down

# Clean (with volumes)
docker-compose down -v
```

## Environment Variables

### Required Variables
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

# Application
NODE_ENV=development
PORT=3002
```

### Optional Variables
```bash
# Logging
LOG_LEVEL=info
SHOW_SQL_QUERIES=false

# Performance
RATE_LIMIT_MAX_REQUESTS=100
COMPRESSION_ENABLED=true

# Cache
CACHE_TTL=3600
TERMS_CACHE_TTL=1800
```

## Production Deployment

### 1. Build
```bash
# Install dependencies
npm install

# Build frontend
cd client
npm install
npm run build

# Frontend build output: client/dist/
```

### 2. Database
```bash
# Run migrations
npx sequelize-cli db:migrate --migrations-path src/migrations

# Seed data (optional)
npm run seed
```

### 3. Start Application
```bash
# Production mode
NODE_ENV=production npm start

# Or with PM2
pm2 start src/index.js --name libraries-service
```

### 4. Health Check
```bash
curl http://localhost:3002/health
```

## Monitoring

### Health Endpoints
- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health with DB/Redis status

### Logs
- **Location**: `logs/app.log`, `logs/error.log`
- **Rotation**: Max 10MB, 5 files
- **Format**: JSON (production), Pretty (development)

### Metrics
- Uptime
- Memory usage
- Database connections
- Redis connections
- API response times

## Backup Strategy

### Database Backup
```bash
# Full backup
pg_dump -h localhost -U postgres -d libraries_db -F c -b -v -f backup.dump

# Restore
pg_restore -h localhost -U postgres -d libraries_db_new backup.dump
```

### File Backup
- `/uploads/` directory
- Environment files (`.env`)
- Logs

## Scaling

### Horizontal Scaling
- Multiple app instances behind load balancer
- Shared PostgreSQL database
- Shared Redis cache

### Vertical Scaling
- Increase container resources
- Adjust connection pool sizes
- Optimize database indexes

## Security Checklist

- [ ] Change default database password
- [ ] Set secure `ALLOWED_ORIGINS`
- [ ] Use HTTPS in production
- [ ] Enable Helmet security headers
- [ ] Configure rate limiting
- [ ] Set up firewall rules
- [ ] Regular security updates
- [ ] Backup encryption

---

**See Also**: [DEVELOPMENT.md](DEVELOPMENT.md), [TECH_STACK.md](TECH_STACK.md)
