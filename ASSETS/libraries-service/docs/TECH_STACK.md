# Technology Stack

Complete inventory of all technologies, libraries, versions, and architectural decisions for the libraries-service microservice.

## Table of Contents

1. [Backend Technologies](#backend-technologies)
2. [Frontend Technologies](#frontend-technologies)
3. [Infrastructure](#infrastructure)
4. [Development Tools](#development-tools)
5. [Architectural Decisions](#architectural-decisions)
6. [Dependencies Reference](#dependencies-reference)
7. [Version Compatibility](#version-compatibility)

---

## Backend Technologies

### Core Framework

#### Node.js v16+

**Purpose**: JavaScript runtime for backend

**Why Chosen**:
- Industry standard for JavaScript backend development
- Excellent async/await support for concurrent operations
- Large ecosystem of packages
- Event-driven architecture fits microservice patterns
- Strong community and tooling support

**Key Features Used**:
- Async/await for all I/O operations
- Event emitters for internal events
- Child process for running migrations
- Stream API for file processing
- Built-in crypto for security

**Configuration**:
```javascript
// package.json
"engines": {
  "node": ">=16.0.0",
  "npm": ">=8.0.0"
}
```

#### Express.js v4.18.2

**Purpose**: Web application framework

**Why Chosen**:
- Minimalist and flexible
- Extensive middleware ecosystem
- Well-documented and battle-tested
- Easy to understand and maintain
- Perfect for REST APIs

**Middleware Stack** (in order):
1. `helmet` - Security headers
2. `cors` - Cross-origin resource sharing
3. `compression` - Response compression
4. `morgan` - HTTP request logging
5. `express.json()` - JSON body parser
6. `express-rate-limit` - Rate limiting
7. Custom middleware (auth, permissions, validation)

**Location**: `d:\RH\libraries-service\src\index.js`

**Example Configuration**:
```javascript
const app = express();

// Security
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
    },
  },
  crossOriginEmbedderPolicy: false,
}));

// CORS
app.use(cors({
  origin: function (origin, callback) {
    const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || [];
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  message: 'Too many requests'
});
app.use('/api/', limiter);
```

---

### Database Layer

#### PostgreSQL v12+

**Purpose**: Primary data store

**Why Chosen**:
- **ACID Compliance**: Reliable transactions for critical data
- **JSONB Support**: Flexible storage for AI metadata, configs
- **Advanced Queries**: CTEs, window functions, full-text search
- **Spatial Data**: PostGIS extension for coordinates (cities)
- **Performance**: Excellent query optimization and indexing
- **Mature**: Battle-tested, stable, well-documented

**Features Used**:
- **JSONB Columns**: AI metadata, configurations, event data
- **Full-Text Search**: Term searching with trgm extension
- **Foreign Keys**: Referential integrity
- **Indexes**: B-tree, GIN, unique constraints
- **Triggers**: Automatic timestamp updates
- **Schemas**: Public schema for all tables

**Connection Configuration**:
```javascript
// config/config.js
{
  development: {
    username: process.env.DB_USER || 'postgres',
    password: process.env.DB_PASSWORD || 'postgres',
    database: process.env.DB_NAME || 'libraries_db',
    host: process.env.DB_HOST || 'localhost',
    port: process.env.DB_PORT || 5432,
    dialect: 'postgres',
    logging: process.env.SEQUELIZE_LOGGING === 'true',
    pool: {
      max: 20,
      min: 5,
      acquire: 30000,
      idle: 10000
    }
  }
}
```

**Required Extensions**:
```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;  -- Trigram similarity
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- UUID generation
```

#### Sequelize ORM v6.35.1

**Purpose**: Object-Relational Mapping

**Why Chosen**:
- **Type Safety**: Model definitions with validations
- **Migration Support**: Version-controlled schema changes
- **Association Handling**: Easy relationship management
- **Query Builder**: Chainable, readable queries
- **Transaction Support**: Atomic operations
- **Hooks**: Lifecycle events for business logic

**Patterns Used**:
1. **Model-Based Queries**: Always use models, not raw queries
2. **Eager Loading**: `include` for associations
3. **Transactions**: Wrap multi-step operations
4. **Migrations**: All schema changes via migrations
5. **Hooks**: `beforeCreate`, `afterUpdate` for side effects

**Model Location**: `d:\RH\libraries-service\src\models\`

**Example Model**:
```javascript
// src/models/profession.js
module.exports = (sequelize, DataTypes) => {
  const Profession = sequelize.define('Profession', {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    term_group_id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'term_groups',
        key: 'id'
      }
    },
    department_id: {
      type: DataTypes.INTEGER,
      references: {
        model: 'departments',
        key: 'id'
      }
    },
    full_price: DataTypes.DECIMAL(10, 2),
    part_price: DataTypes.DECIMAL(10, 2),
    min_price: DataTypes.DECIMAL(10, 2),
    currency_id: DataTypes.INTEGER
  }, {
    tableName: 'professions',
    timestamps: true,
    underscored: true
  });

  Profession.associate = (models) => {
    Profession.belongsTo(models.TermGroup, {
      foreignKey: 'term_group_id'
    });
    Profession.belongsTo(models.Department, {
      foreignKey: 'department_id'
    });
    Profession.belongsToMany(models.Tool, {
      through: 'profession_tools',
      foreignKey: 'profession_id',
      otherKey: 'tool_id',
      as: 'tools'
    });
  };

  return Profession;
};
```

#### sequelize-cli v6.6.3

**Purpose**: Migration and seeder management

**Commands**:
```bash
# Run migrations
npx sequelize-cli db:migrate --migrations-path src/migrations

# Rollback last migration
npx sequelize-cli db:migrate:undo --migrations-path src/migrations

# Check status
npx sequelize-cli db:migrate:status --migrations-path src/migrations

# Generate new migration
npx sequelize-cli migration:generate --name add-field-to-table
```

**Configuration**: `.sequelizerc`
```javascript
const path = require('path');

module.exports = {
  'config': path.resolve('config', 'config.js'),
  'models-path': path.resolve('src', 'models'),
  'seeders-path': path.resolve('src', 'seeders'),
  'migrations-path': path.resolve('src', 'migrations')
};
```

---

### Caching & State

#### Redis v5.5.6

**Purpose**: In-memory cache and session store

**Why Chosen**:
- **Performance**: Sub-millisecond response times
- **Data Structures**: Strings, hashes, lists, sets
- **TTL Support**: Automatic expiration
- **Pub/Sub**: Real-time messaging (future use)
- **Persistence**: Optional data persistence

**Use Cases**:
1. **API Key Caching**: Cache validated API keys (TTL: 600s)
2. **Terms Cache**: Cache frequently accessed terms (TTL: 1800s)
3. **Session Data**: User session information
4. **Rate Limiting**: Request counts per IP
5. **MCP Sessions**: Store MCP session tokens and metadata

**Configuration**:
```javascript
// src/utils/redis.js
const redis = require('redis');

const client = redis.createClient({
  url: process.env.REDIS_URL || 'redis://localhost:6379',
  socket: {
    reconnectStrategy: (retries) => {
      if (retries > 10) {
        return new Error('Redis retry limit exceeded');
      }
      return Math.min(retries * 100, 3000);
    }
  }
});

client.on('error', (err) => logger.error('Redis Client Error', err));
client.on('connect', () => logger.info('Redis connected'));
client.on('reconnecting', () => logger.warn('Redis reconnecting'));

await client.connect();

module.exports = client;
```

**Usage Example**:
```javascript
// Cache API key validation
const cacheKey = `api_key:${apiKey}`;
const cached = await redis.get(cacheKey);

if (cached) {
  return JSON.parse(cached);
}

const validation = await validateApiKeyFromGateway(apiKey);
await redis.setEx(cacheKey, 600, JSON.stringify(validation));

return validation;
```

---

### HTTP & Communication

#### Axios v1.9.0

**Purpose**: HTTP client for external service communication

**Why Chosen**:
- Promise-based API
- Request/response interceptors
- Automatic JSON transformation
- Timeout support
- Error handling
- Request cancellation

**Use Cases**:
1. **Auth Service**: JWT token validation
2. **API Gateway**: Event publishing, permission checks
3. **External APIs**: Third-party integrations

**Configuration Examples**:

**Backend (Auth Service Communication)**:
```javascript
// src/middleware/authMiddleware.js
const validateToken = async (token) => {
  const response = await axios.post(
    `${process.env.API_GATEWAY_URL}/auth/validate-token`,
    {},
    {
      headers: { Authorization: `Bearer ${token}` },
      timeout: 5000
    }
  );
  return response.data;
};
```

**Frontend (API Client)**:
```javascript
// client/src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:3002/api',
  timeout: 30000
});

// Request interceptor - add auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  config.headers['X-Client-Domain'] = window.location.origin;
  return config;
});

// Response interceptor - handle 401, refresh token
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Try to refresh token
      const newToken = await authService.refreshToken();
      if (newToken) {
        error.config.headers.Authorization = `Bearer ${newToken}`;
        return axios.request(error.config);
      }
      // Redirect to login
      window.location.href = '/';
    }
    return Promise.reject(error);
  }
);

export default api;
```

---

### Security

#### Helmet v7.1.0

**Purpose**: Security headers middleware

**Features**:
- Content Security Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security
- X-DNS-Prefetch-Control

**Configuration**:
```javascript
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", process.env.API_GATEWAY_URL],
    },
  },
  crossOriginEmbedderPolicy: false,
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

#### CORS v2.8.5

**Purpose**: Cross-Origin Resource Sharing

**Configuration**:
```javascript
// Dynamic origin validation
const allowedOrigins = [
  'http://localhost:3000',
  'http://localhost:3001',
  process.env.CLIENT_URL,
  ...process.env.ALLOWED_ORIGINS?.split(',') || []
].filter(Boolean);

app.use(cors({
  origin: function (origin, callback) {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      logger.warn(`CORS blocked origin: ${origin}`);
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-API-Key', 'X-Client-Domain']
}));
```

#### express-rate-limit v7.1.5

**Purpose**: Rate limiting to prevent abuse

**Configuration**:
```javascript
const rateLimit = require('express-rate-limit');

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests from this IP',
  standardHeaders: true,
  legacyHeaders: false,
});

// Search rate limit (stricter)
const searchLimiter = rateLimit({
  windowMs: 1 * 60 * 1000, // 1 minute
  max: 50, // 50 searches per minute
  message: 'Too many search requests'
});

app.use('/api/', apiLimiter);
app.use('/api/terms/search', searchLimiter);
app.use('/api/search/', searchLimiter);
```

---

### File Handling

#### Multer v2.0.2

**Purpose**: Multipart/form-data file upload handling

**Why Chosen**:
- Simple API
- Disk/memory storage options
- File validation
- Size limits
- Filename customization

**Use Cases**:
1. Term group icon uploads
2. Tool logo uploads
3. CSV imports for bulk data
4. Document attachments (future)

**Configuration**:
```javascript
// src/middleware/uploadMiddleware.js
const multer = require('multer');
const path = require('path');
const fs = require('fs').promises;

const storage = multer.diskStorage({
  destination: async (req, file, cb) => {
    const uploadPath = path.join(__dirname, '../../uploads');
    await fs.mkdir(uploadPath, { recursive: true });
    cb(null, uploadPath);
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, `${file.fieldname}-${uniqueSuffix}${path.extname(file.originalname)}`);
  }
});

const fileFilter = (req, file, cb) => {
  const allowedTypes = /jpeg|jpg|png|gif|svg/;
  const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
  const mimetype = allowedTypes.test(file.mimetype);

  if (mimetype && extname) {
    return cb(null, true);
  }
  cb(new Error('Only image files are allowed'));
};

const upload = multer({
  storage: storage,
  fileFilter: fileFilter,
  limits: {
    fileSize: 5 * 1024 * 1024, // 5MB
    files: 1
  }
});

module.exports = { upload };
```

**Usage Example**:
```javascript
// Controller
router.post(
  '/upload-icon',
  authMiddleware,
  upload.single('icon'),
  async (req, res) => {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    const iconUrl = `/uploads/${req.file.filename}`;
    // Save iconUrl to database

    res.json({ success: true, iconUrl });
  }
);
```

---

### Logging

#### Winston v3.17.0

**Purpose**: Application logging

**Why Chosen**:
- Multiple transports (file, console, HTTP)
- Log levels (error, warn, info, debug)
- JSON formatting for production
- Pretty formatting for development
- Log rotation support
- Custom metadata

**Configuration**:
```javascript
// src/utils/logger.js
const winston = require('winston');
const path = require('path');

const logDir = path.join(__dirname, '../../logs');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    winston.format.errors({ stack: true }),
    winston.format.splat(),
    winston.format.json()
  ),
  defaultMeta: { service: 'libraries-service' },
  transports: [
    // Error log
    new winston.transports.File({
      filename: path.join(logDir, 'error.log'),
      level: 'error',
      maxsize: 10485760, // 10MB
      maxFiles: 5
    }),
    // Combined log
    new winston.transports.File({
      filename: path.join(logDir, 'app.log'),
      maxsize: 10485760,
      maxFiles: 5
    })
  ]
});

// Console in development
if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.simple()
    )
  }));
}

// Custom logging methods
logger.api = (method, endpoint, statusCode, duration, meta = {}) => {
  logger.info('API Request', {
    method,
    endpoint,
    statusCode,
    duration: `${duration}ms`,
    ...meta
  });
};

logger.sql = (query, duration) => {
  if (process.env.SHOW_SQL_QUERIES === 'true') {
    logger.debug('SQL Query', { query, duration: `${duration}ms` });
  }
};

logger.security = (event, details) => {
  logger.warn('Security Event', { event, ...details });
};

module.exports = logger;
```

**Usage Example**:
```javascript
// Log API requests
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.api(req.method, req.path, res.statusCode, duration, {
      ip: req.ip,
      userAgent: req.get('user-agent')
    });
  });
  next();
});

// Log errors
logger.error('Database connection failed', {
  error: error.message,
  stack: error.stack,
  context: 'startup'
});

// Log security events
logger.security('Invalid API key attempt', {
  apiKey: apiKey.substring(0, 8) + '...',
  ip: req.ip
});
```

---

### Validation

#### express-validator v7.0.1

**Purpose**: Request validation middleware

**Why Chosen**:
- Express-integrated
- Chainable validators
- Custom validators
- Sanitization
- Error formatting

**Configuration**:
```javascript
// src/middleware/validation.js
const { body, query, param, validationResult } = require('express-validator');

// Validation middleware
const validateCreateTermGroup = [
  body('name').trim().notEmpty().withMessage('Name is required'),
  body('main_term_id').isInt().withMessage('Valid main_term_id required'),
  body('status_id').optional().isInt(),
  body('icon').optional().isString(),

  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({
        success: false,
        errors: errors.array()
      });
    }
    next();
  }
];

const validatePagination = [
  query('page').optional().isInt({ min: 1 }).toInt(),
  query('limit').optional().isInt({ min: 1, max: 100 }).toInt(),
  query('sortBy').optional().isString(),
  query('sortOrder').optional().isIn(['ASC', 'DESC']),

  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ success: false, errors: errors.array() });
    }
    next();
  }
];

module.exports = {
  validateCreateTermGroup,
  validatePagination
};
```

**Usage**:
```javascript
router.post('/terms/groups',
  authMiddleware,
  validateCreateTermGroup,
  termsController.createTermGroup
);
```

---

### Utilities

#### uuid v9.0.1

**Purpose**: UUID generation

**Use Cases**:
- Request IDs for tracing
- Unique identifiers
- Session tokens

```javascript
const { v4: uuidv4 } = require('uuid');

// Add request ID
app.use((req, res, next) => {
  req.requestId = uuidv4();
  res.setHeader('X-Request-ID', req.requestId);
  next();
});
```

#### dotenv v16.3.1

**Purpose**: Environment variable management

**Configuration**:
```javascript
// Load at startup
require('dotenv').config();

// Usage
const dbHost = process.env.DB_HOST || 'localhost';
const apiGatewayUrl = process.env.API_GATEWAY_URL;
```

---

## Frontend Technologies

### Core Framework

#### React v19.1.0

**Purpose**: UI library

**Why Chosen**:
- **Component-Based**: Reusable UI components
- **Virtual DOM**: Efficient rendering
- **Hooks**: Modern state management
- **Large Ecosystem**: Rich library support
- **Developer Experience**: Excellent tooling

**Key Features Used**:
- **Hooks**: useState, useEffect, useCallback, useMemo, useContext
- **Context API**: Global state (Auth, Permissions, Theme)
- **Suspense**: Code splitting (future)
- **Error Boundaries**: Error handling (future)

**Entry Point**: `d:\RH\libraries-service\client\src\main.jsx`

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { AuthProvider } from './contexts/AuthContext';
import { PermissionProvider } from './contexts/PermissionContext';
import { ThemeProvider } from './contexts/ThemeContext';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ThemeProvider>
      <AuthProvider>
        <PermissionProvider>
          <App />
        </PermissionProvider>
      </AuthProvider>
    </ThemeProvider>
  </React.StrictMode>
);
```

#### Vite v6.3.5

**Purpose**: Build tool and dev server

**Why Chosen Over Webpack**:
- **Speed**: 10-100x faster than webpack
- **Native ESM**: Uses browser's module system
- **HMR**: Fast hot module replacement (<100ms)
- **Simple Config**: Less configuration needed
- **Optimized Build**: Rollup-based production builds

**Performance Comparison**:
- Dev server start: <1s (vs 10-30s with webpack)
- HMR updates: <100ms (vs 1-5s with webpack)
- Production build: Comparable to webpack

**Configuration**:
```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:3002',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'build',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom', 'react-router-dom'],
          mui: ['@mui/material', '@mui/icons-material']
        }
      }
    }
  }
});
```

---

### UI Framework

#### Material-UI (MUI) v7.1.1

**Purpose**: React component library

**Why Chosen**:
- **Comprehensive**: 100+ components
- **Material Design**: Google's design system
- **Customizable**: Theme system
- **Accessible**: ARIA support
- **Documentation**: Excellent docs
- **TypeScript**: Full type support

**Components Used**:

**Layout**:
- Box, Container, Grid, Stack, Paper

**Navigation**:
- AppBar, Drawer, Tabs, Breadcrumbs, Menu

**Data Display**:
- Table, Card, Chip, Avatar, Tooltip, Typography

**Inputs**:
- TextField, Button, Checkbox, Select, Autocomplete, Switch

**Feedback**:
- Alert, CircularProgress, Snackbar, Skeleton

**Utils**:
- Dialog, Popper, Portal, Collapse

**Theme Configuration**:
```javascript
// client/src/themes/themes.js
import { createTheme } from '@mui/material/styles';

export const lightTheme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
    background: {
      default: '#f5f5f5',
      paper: '#ffffff',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h1: { fontSize: '2.5rem', fontWeight: 500 },
    h2: { fontSize: '2rem', fontWeight: 500 },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
        },
      },
    },
  },
});

export const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
    background: {
      default: '#121212',
      paper: '#1e1e1e',
    },
  },
  // ... other dark theme settings
});
```

---

### Styling

#### Emotion v11.14.0

**Purpose**: CSS-in-JS solution

**Packages**:
- `@emotion/react` - Core library
- `@emotion/styled` - Styled components API

**Why Chosen**:
- Integrated with MUI
- Dynamic styling based on props
- Theme support
- Better performance than styled-components
- Smaller bundle size

**Usage Example**:
```javascript
import { styled } from '@mui/material/styles';

const StyledCard = styled('div')(({ theme, active }) => ({
  padding: theme.spacing(2),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: active
    ? theme.palette.primary.main
    : theme.palette.background.paper,
  transition: theme.transitions.create(['background-color', 'transform']),
  '&:hover': {
    transform: 'scale(1.02)',
  },
}));
```

---

### Icons

#### @mui/icons-material v7.1.1

**Purpose**: Material Design icons

**Features**:
- 2000+ icons
- Tree-shakeable (import only what you use)
- Consistent styling
- Customizable size/color

**Usage**:
```javascript
import {
  Add, Edit, Delete, Search, FilterList,
  Dashboard, People, Work, Settings
} from '@mui/icons-material';

// In component
<Button startIcon={<Add />}>Create New</Button>
<IconButton><Edit /></IconButton>
```

---

### Routing

#### react-router-dom v7.6.2

**Purpose**: Client-side routing

**Why Chosen**:
- Declarative routing
- Nested routes
- Route protection
- Hooks API (useNavigate, useLocation, useParams)
- Lazy loading support

**Route Structure**:
```javascript
// client/src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes */}
        <Route path="/" element={<WikiDashboard />} />
        <Route path="/ai-tools" element={<Wiki />} />
        <Route path="/login" element={<Login />} />
        <Route path="/oauth-callback" element={<OAuthCallback />} />

        {/* Protected routes */}
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />

          <Route element={<PermissionRoute service="libraries-service" resource="department" action="list" />}>
            <Route path="/departments" element={<Departments />} />
          </Route>

          <Route element={<PermissionRoute service="libraries-service" resource="profession" action="list" />}>
            <Route path="/professions" element={<Professions />} />
          </Route>

          {/* ... more protected routes */}
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

---

### State Management

#### React Context API

**Purpose**: Global state management

**Why Chosen Over Redux**:
- Built into React
- Simpler for our use case
- No additional dependencies
- Sufficient for our state needs

**Contexts Implemented**:

**1. AuthContext**
```javascript
// client/src/contexts/AuthContext.jsx
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const login = async (email, password) => { /* ... */ };
  const logout = async () => { /* ... */ };
  const checkAuth = async () => { /* ... */ };

  return (
    <AuthContext.Provider value={{
      user,
      loading,
      error,
      login,
      logout,
      checkAuth,
      isAuthenticated: !!user
    }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
```

**2. PermissionContext**
```javascript
// client/src/contexts/PermissionContext.jsx
const PermissionContext = createContext();

export const PermissionProvider = ({ children }) => {
  const { user } = useAuth();
  const [permissions, setPermissions] = useState([]);

  const hasPermission = (service, resource, action) => {
    return permissions.some(p =>
      p.service === service &&
      p.resource === resource &&
      p.action === action
    );
  };

  const hasServiceAccess = (service) => {
    return permissions.some(p => p.service === service);
  };

  return (
    <PermissionContext.Provider value={{
      permissions,
      hasPermission,
      hasServiceAccess
    }}>
      {children}
    </PermissionContext.Provider>
  );
};
```

**3. ThemeContext**
```javascript
// client/src/contexts/ThemeContext.jsx
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [mode, setMode] = useState(
    localStorage.getItem('theme') || 'light'
  );

  const toggleTheme = () => {
    const newMode = mode === 'light' ? 'dark' : 'light';
    setMode(newMode);
    localStorage.setItem('theme', newMode);
  };

  const theme = mode === 'light' ? lightTheme : darkTheme;

  return (
    <ThemeContext.Provider value={{ mode, toggleTheme }}>
      <MuiThemeProvider theme={theme}>
        {children}
      </MuiThemeProvider>
    </ThemeContext.Provider>
  );
};
```

---

### Additional Libraries

#### react-color v2.19.3

**Purpose**: Color picker component

**Use Cases**:
- Department color selection
- Status color selection
- Priority color selection

**Usage**:
```javascript
import { ChromePicker } from 'react-color';

const [color, setColor] = useState('#1976d2');

<ChromePicker
  color={color}
  onChange={(color) => setColor(color.hex)}
/>
```

---

## Infrastructure

### Containerization

#### Docker

**Purpose**: Application containerization

**Why Chosen**:
- **Consistency**: Same environment everywhere
- **Isolation**: Separate service dependencies
- **Portability**: Run anywhere Docker runs
- **Resource Efficiency**: Lightweight vs VMs

**Dockerfile**:
```dockerfile
# Multi-stage build
FROM node:16-alpine AS builder

WORKDIR /app

# Backend dependencies
COPY package*.json ./
RUN npm ci --only=production

# Frontend build
COPY client/package*.json ./client/
WORKDIR /app/client
RUN npm ci
COPY client ./
RUN npm run build

# Production image
FROM node:16-alpine

WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/client/dist ./client/dist
COPY . .

EXPOSE 3002

CMD ["node", "src/index.js"]
```

#### Docker Compose v3.8

**Purpose**: Multi-container orchestration

**Services Defined**:

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3002:3002"
    environment:
      - NODE_ENV=${NODE_ENV}
      - DB_HOST=postgres
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    networks:
      - app-network

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: libraries_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - postgres
    networks:
      - app-network
    profiles:
      - development

volumes:
  postgres-data:
  redis-data:

networks:
  app-network:
    driver: bridge
```

**Commands**:
```bash
# Start all services
docker-compose up -d

# Start with development profile (includes pgadmin)
docker-compose --profile development up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down

# Rebuild and start
docker-compose up -d --build

# Clean everything
docker-compose down -v  # Removes volumes too
```

---

## Development Tools

### Backend Development

#### nodemon v3.0.1

**Purpose**: Auto-reload on file changes

**Configuration**:
```json
// package.json
{
  "nodemonConfig": {
    "watch": ["src"],
    "ext": "js,json",
    "ignore": ["src/tests/", "node_modules/"],
    "exec": "node src/index.js",
    "env": {
      "NODE_ENV": "development"
    }
  },
  "scripts": {
    "dev": "nodemon src/index.js"
  }
}
```

---

### Testing

#### Jest v29.7.0

**Purpose**: Testing framework

**Configuration**:
```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'node',
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/tests/**',
    '!src/migrations/**',
    '!src/seeders/**'
  ],
  testMatch: ['**/tests/**/*.test.js'],
  setupFilesAfterEnv: ['<rootDir>/src/tests/setup.js']
};
```

#### Supertest v6.3.3

**Purpose**: HTTP assertion library

**Usage**:
```javascript
const request = require('supertest');
const app = require('../app');

describe('GET /api/department', () => {
  it('should return departments', async () => {
    const response = await request(app)
      .get('/api/department')
      .set('Authorization', `Bearer ${token}`)
      .expect(200);

    expect(response.body.success).toBe(true);
    expect(Array.isArray(response.body.data)).toBe(true);
  });
});
```

---

### Linting

#### ESLint v9.25.0

**Purpose**: Code linting and formatting

**Configuration**:
```javascript
// .eslintrc.js
module.exports = {
  env: {
    node: true,
    es2021: true,
    jest: true
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended'
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  rules: {
    'no-unused-vars': 'warn',
    'no-console': 'off'
  }
};
```

---

## Architectural Decisions

### 1. Microservice Architecture

**Decision**: Standalone service with external auth integration

**Rationale**:
- **Separation of Concerns**: Authentication handled by dedicated service
- **Scalability**: Scale libraries-service independently
- **Deployment Flexibility**: Can deploy separately
- **Technology Freedom**: Can use different tech for different services

**Trade-offs**:
- Network latency for auth calls (mitigated with caching)
- Complexity in distributed tracing
- Need for event-driven synchronization

**Implementation**:
- External JWT validation via API Gateway
- Event publishing for entity changes
- Redis caching for auth responses

---

### 2. Terms System for Multilingual Support

**Decision**: TermGroup → Terms → Languages pattern

**Rationale**:
- **Centralized Management**: Single source of truth
- **Flexibility**: Add languages without schema changes
- **AI-Ready**: Centralized location for AI-generated content
- **Relationships**: Link synonyms, similar terms
- **Consistency**: Same pattern across all entities

**Trade-offs**:
- Complexity: More joins in queries
- Performance: Requires eager loading
- Learning curve: New developers need to understand pattern

**Implementation**:
```javascript
// Without Terms:
{ name: "Software Engineer", name_ru: "Программист" }

// With Terms:
{
  term_group_id: 123,
  TermGroup: {
    MainTerm: { value: "Software Engineer", language_id: 1 },
    Terms: [
      { value: "Programmer", term_type: "similar" },
      { value: "Программист", term_type: "translation", language_id: 2 }
    ]
  }
}
```

**Benefits Realized**:
- Added Russian, Ukrainian translations easily
- AI can generate translations automatically
- Consistent pattern across 20+ entity types
- No schema changes when adding languages

---

### 3. Service Layer Pattern

**Decision**: Controllers → Services → Models

**Rationale**:
- **Testability**: Test business logic without HTTP
- **Reusability**: Services callable from multiple controllers
- **Separation**: HTTP concerns vs business logic
- **Transaction Management**: Services handle DB transactions

**Trade-offs**:
- More files to maintain
- Slight overhead in simple CRUD operations
- Need discipline to maintain pattern

**Example**:
```javascript
// Controller (HTTP)
exports.createProfession = async (req, res) => {
  try {
    const profession = await professionService.create(req.body, req.user);
    res.status(201).json({ success: true, data: profession });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};

// Service (Business Logic)
exports.create = async (data, user) => {
  const transaction = await sequelize.transaction();
  try {
    // 1. Create term group
    const termGroup = await createTermGroup(data.terms, transaction);

    // 2. Create profession
    const profession = await Profession.create({
      ...data,
      term_group_id: termGroup.id
    }, { transaction });

    // 3. Publish event
    await eventService.publishProfessionCreated(profession);

    await transaction.commit();
    return profession;
  } catch (error) {
    await transaction.rollback();
    throw error;
  }
};
```

---

### 4. Dual View Mode (Table + Card)

**Decision**: All entity lists support both views

**Rationale**:
- **User Preference**: Different users prefer different formats
- **Responsive**: Cards better on mobile
- **Information Density**: Tables for detail, cards for browsing
- **Consistency**: Same UX across all pages

**Implementation**:
- `DataTable` component for table view
- `CardView` component for card view
- `DataViewToggle` to switch
- `useResponsiveView` hook for persistence
- Auto-switch to cards on mobile

**Trade-offs**:
- Need to maintain two views per entity
- More code per page
- Slight performance overhead

**Benefits**:
- Users love the flexibility
- Mobile experience is excellent
- Visual browsing with cards is popular
- Consistent UX across app

---

### 5. External Auth Service

**Decision**: JWT validation via external auth-users-service

**Rationale**:
- **Centralized Users**: Single user database across services
- **Consistent Permissions**: Unified RBAC system
- **Session Management**: Dedicated service handles it
- **Security**: Auth service can implement stricter security
- **SSO Support**: Easier to implement single sign-on

**Trade-offs**:
- Network dependency on auth service
- Latency for every authenticated request
- Need caching strategy (implemented with Redis)

**Flow**:
```
1. Client → Libraries Service (with JWT)
2. Libraries Service → Auth Service (validate token)
3. Auth Service → Libraries Service (user data + permissions)
4. Libraries Service → Client (response)

Cache: Redis stores valid tokens for 10 minutes
```

**Mitigation of Trade-offs**:
- Redis caching reduces auth calls by 95%
- Fallback to service-to-service tokens
- Graceful degradation if auth service down

---

### 7. Event-Driven Architecture

**Decision**: Publish entity changes to API Gateway Event Hub

**Rationale**:
- **Microservice Communication**: Other services notified
- **Audit Trail**: All changes tracked
- **Real-time Updates**: WebSocket broadcasts (future)
- **Decoupling**: Services don't need direct communication
- **Analytics**: Can analyze event stream

**Implementation**:
```javascript
// After creating profession
await eventService.publishProfessionCreated(profession);

// Event structure
{
  sourceService: 'libraries-service',
  eventType: 'profession.created',
  eventData: {
    profession: { id, term_group_id, department_id },
    timestamp: '2025-01-12T10:30:00Z',
    user: 'user@example.com'
  }
}
```

**Event Types**:
- `entity.created`
- `entity.updated` (includes changedFields)
- `entity.deleted`

**Subscribers** (Other Services):
- Auth Service: Track entity creators
- Analytics Service: Usage statistics
- Notification Service: Real-time alerts
- Audit Service: Compliance logging

---

### 8. Vite Instead of Webpack

**Decision**: Use Vite for frontend build tool

**Rationale**:
- **Speed**: 10-100x faster in development
- **Native ESM**: Uses browser's module system
- **HMR**: Fast hot module replacement
- **Simple Config**: Less configuration
- **Modern**: Built for modern browsers

**Performance Comparison**:
| Metric | Vite | Webpack |
|--------|------|---------|
| Dev server start | <1s | 10-30s |
| HMR update | <100ms | 1-5s |
| Production build | ~30s | ~30s |

**Trade-offs**:
- Newer, less mature than webpack
- Some plugins not available
- Different mental model

**Benefits Realized**:
- Developers love fast HMR
- Onboarding is faster
- Build times acceptable
- Config is simple

---

## Dependencies Reference

### Backend Dependencies

```json
{
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.21.1",
    "axios": "^1.9.0",
    "compression": "^1.7.4",
    "cors": "^2.8.5",
    "csv-parser": "^3.0.0",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "express-rate-limit": "^7.1.5",
    "express-validator": "^7.0.1",
    "fast-csv": "^4.3.6",
    "helmet": "^7.1.0",
    "morgan": "^1.10.0",
    "multer": "^2.0.2",
    "pg": "^8.16.0",
    "pg-hstore": "^2.3.4",
    "redis": "^5.5.6",
    "sequelize": "^6.35.1",
    "uuid": "^9.0.1",
    "winston": "^3.17.0"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "nodemon": "^3.0.1",
    "sequelize-cli": "^6.6.3",
    "supertest": "^6.3.3"
  }
}
```

### Frontend Dependencies

```json
{
  "dependencies": {
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.0",
    "@mui/icons-material": "^7.1.1",
    "@mui/material": "^7.1.1",
    "axios": "^1.9.0",
    "react": "^19.1.0",
    "react-color": "^2.19.3",
    "react-dom": "^19.1.0",
    "react-router-dom": "^7.6.2"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.4",
    "eslint": "^9.25.0",
    "eslint-plugin-react": "^7.37.2",
    "eslint-plugin-react-hooks": "^5.1.0",
    "eslint-plugin-react-refresh": "^0.4.16",
    "vite": "^6.3.5"
  }
}
```

---

## Version Compatibility

### Minimum Versions

| Package | Min Version | Max Tested | Notes |
|---------|-------------|------------|-------|
| Node.js | 16.0.0 | 20.x | LTS versions recommended |
| PostgreSQL | 12.0 | 16.x | JSONB and trgm required |
| Redis | 5.0 | 7.x | Pub/sub support needed |
| React | 19.0.0 | 19.1.0 | Latest stable |
| Docker | 20.10.0 | 24.x | Compose v3.8+ |

### Breaking Changes to Watch

**Node.js**:
- v16 → v18: Fetch API added
- v18 → v20: New --watch flag

**PostgreSQL**:
- v12 → v13: pg_trgm improvements
- v14 → v15: Performance improvements

**React**:
- v18 → v19: Concurrent features stable

### Upgrade Path

**Backend**:
1. Update Node.js (LTS versions only)
2. Update PostgreSQL (test migrations)
3. Update Sequelize (check breaking changes)
4. Update Express and middleware

**Frontend**:
1. Update React and React-DOM together
2. Update MUI (check migration guides)
3. Update Vite
4. Update other dependencies

---

**Last Updated**: 2025-01-12
**Documentation Version**: 1.0
