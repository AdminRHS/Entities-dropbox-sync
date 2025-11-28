# Strapi & Visual Studio Code: Comprehensive Integration Guide

**Research Date:** November 2025
**Status:** Complete

---

## Table of Contents

1. [Project and Code Workflows](#1-project-and-code-workflows)
2. [VS Code Extensions and Tooling](#2-vs-code-extensions-and-tooling)
3. [Editing Strapi Content from VS Code](#3-editing-strapi-content-from-vs-code)
4. [Custom Developer Tooling](#4-custom-developer-tooling)
5. [DX, Performance, and Team Workflows](#5-dx-performance-and-team-workflows)
6. [Limitations, Anti-Patterns, and Common Pitfalls](#6-limitations-anti-patterns-and-common-pitfalls)
7. [Summary: When to Use What](#summary-when-to-use-what)
8. [Sources](#sources)

---

## 1. Project and Code Workflows

### Running and Developing Strapi Projects in VS Code

#### Standard npm/yarn Scripts

Strapi projects use standard Node.js tooling with package.json scripts:

**Common scripts:**
- `npm run develop` - Starts development server with auto-reload
- `npm run build` - Builds the admin panel for production
- `npm run start` - Starts production server
- `strapi ts:generate-types` - Generates TypeScript types from schemas

**Purpose:** Execute Strapi commands without leaving VS Code terminal

**Typical setup:**
1. Open integrated terminal (Ctrl+`)
2. Run `npm run develop` to start development server
3. Access admin panel at http://localhost:1337/admin
4. API endpoints available at http://localhost:1337/api

**When to use:** Daily development workflow, rapid iteration on content types and plugins

#### Debugging Configuration (launch.json)

**Method 1: Launch via npm**

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch via NPM",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run-script", "develop"],
      "port": 9229,
      "skipFiles": ["<node_internals>/**"],
      "console": "integratedTerminal"
    }
  ]
}
```

**Purpose:** Debug Strapi with breakpoints directly in VS Code

**Typical setup:**
1. Add configuration to `.vscode/launch.json`
2. Press F5 to start debugging
3. Set breakpoints in controllers, services, or custom code
4. Use Debug Console to inspect variables

**When to use:** Troubleshooting bugs, understanding code flow, plugin development

**Important caveat:** Strapi develop command runs two processes (admin panel + core server). The debugger may need to attach to port 9230 instead of 9229 for the core server.

**Method 2: Direct node execution with autoAttachChildProcesses**

```json
{
  "name": "STRAPI Debug",
  "type": "node",
  "request": "launch",
  "cwd": "${workspaceRoot}",
  "runtimeExecutable": "node",
  "skipFiles": ["<node_internals>/**"],
  "program": "${workspaceRoot}/node_modules/@strapi/strapi/bin/strapi.js",
  "args": ["develop"],
  "protocol": "inspector",
  "env": {
    "NODE_ENV": "development"
  },
  "autoAttachChildProcesses": true,
  "console": "integratedTerminal"
}
```

**When to use:** When you need to debug both admin and server processes

**When NOT to use:** Simple API development without complex debugging needs

#### Environment Variables Management

**Setup:**

Create `.env` file in project root:

```
DATABASE_PASSWORD=acme
HOST=0.0.0.0
PORT=1337
APP_KEYS="toBeModified1,toBeModified2"
API_TOKEN_SALT=tobemodified
ADMIN_JWT_SECRET=tobemodified
NODE_ENV=development
```

**Accessing variables:**

In configuration files using Strapi's env() utility:

```javascript
module.exports = ({ env }) => ({
  connection: {
    password: env('DATABASE_PASSWORD'),
    port: env.int('DATABASE_PORT', 5432),
  },
});
```

**Best practices:**
- Add `.env` to `.gitignore` (never commit secrets)
- Use `.env.example` for team documentation
- Use environment-specific files: `.env.development`, `.env.production`
- Install "DotENV" VS Code extension for syntax highlighting

**Typical setup:**
1. Create `.env` in project root
2. Add to `.gitignore`
3. Configure variables in `.env`
4. Access via `env()` utility in config files

**When to use:** Managing database credentials, API keys, deployment configurations

**Common pitfall:** Committing `.env` files to version control exposes secrets

### Best Practices for Structuring Strapi Codebase

#### Recommended Directory Structure

```
project-root/
├── .vscode/
│   ├── launch.json        # Debugging configurations
│   ├── settings.json      # Workspace settings
│   └── tasks.json         # Build/test tasks
├── config/
│   ├── database.ts        # Database configuration
│   ├── server.ts          # Server configuration
│   └── admin.ts           # Admin panel configuration
├── src/
│   ├── api/               # Content types, controllers, services
│   ├── admin/             # Admin panel customizations
│   ├── extensions/        # Plugin extensions
│   └── plugins/           # Custom plugins
├── types/                 # Generated TypeScript types
├── .env                   # Environment variables (gitignored)
├── .env.example           # Environment template
├── package.json
└── tsconfig.json
```

**Purpose:** Consistent structure improves navigation, code sharing, and onboarding

**When to use:** All Strapi projects, especially team environments

---

## 2. VS Code Extensions and Tooling

### Official Strapi Extensions

**Finding:** There is NO official Strapi VS Code extension published by Strapi itself as of 2025. Developers rely on general-purpose extensions configured for Strapi workflows.

### Essential Extensions for Strapi Development

#### 1. ESLint

**What it does:** Real-time JavaScript/TypeScript linting, enforces code quality standards

**How it helps Strapi:**
- Catches common errors in controllers and services
- Enforces consistent coding style across team
- Integrates with Strapi's JavaScript/TypeScript codebase

**Setup:**
1. Install: `npm install eslint --save-dev`
2. Install VS Code extension: "ESLint"
3. Create `.eslintrc.json` or use Strapi's default config
4. Configure in VS Code settings:

```json
{
  "eslint.validate": ["javascript", "typescript"]
}
```

**Pros:**
- Prevents bugs before runtime
- Maintains code consistency
- Works with both JS and TS

**Cons:**
- Can be noisy with strict configs
- Requires initial setup and configuration

**When to use:** All Strapi projects

#### 2. Prettier - Code Formatter

**What it does:** Automatic code formatting on save

**How it helps Strapi:**
- Formats JavaScript, TypeScript, JSON config files
- Eliminates formatting debates in teams
- Works with Strapi's JSON schema files

**Setup:**
1. Install: `npm install prettier --save-dev`
2. Install VS Code extension: "Prettier - Code formatter"
3. Create `.prettierrc`:

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100
}
```

4. Configure in VS Code settings:

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true
}
```

**Pros:**
- Zero-config formatting
- Eliminates formatting inconsistencies
- Fast and reliable

**Cons:**
- Opinionated formatting may conflict with preferences
- Can conflict with ESLint if not configured together

**When to use:** All projects, especially with multiple developers

#### 3. Thunder Client (REST API Client)

**What it does:** Lightweight REST API testing directly in VS Code

**How it helps Strapi:**
- Test Strapi REST APIs without leaving editor
- Test authentication, CRUD operations, custom endpoints
- Supports collections and environment variables

**Setup:**
1. Install extension: "Thunder Client"
2. Create collections for Strapi endpoints
3. Set environment variables for base URL, tokens

**Typical workflow:**
1. Open Thunder Client (sidebar icon)
2. Create new request: `GET http://localhost:1337/api/articles`
3. Add authentication header if needed
4. Save to collection for reuse

**Pros:**
- No external app needed (vs Postman)
- Fast, lightweight
- Git-friendly (requests saved as JSON)
- Free for non-commercial use

**Cons:**
- Less features than Postman
- Paid tier required for commercial use (as of Jan 2025)

**Alternative:** REST Client extension (completely free, request files in workspace)

**When to use:** API development, testing custom endpoints, debugging authentication

**When NOT to use:** Complex API workflows requiring advanced Postman features (mocking, comprehensive team collaboration)

#### 4. GitLens

**What it does:** Supercharges Git capabilities in VS Code

**How it helps Strapi:**
- See who changed content-type schemas
- Understand history of configuration changes
- Review changes before committing

**Setup:**
1. Install extension: "GitLens"
2. Works immediately with Git repos

**When to use:** Team projects, understanding code history

#### 5. npm IntelliSense

**What it does:** Autocompletes npm module imports

**How it helps Strapi:**
- Autocomplete Strapi package imports: `@strapi/strapi`, `@strapi/plugin-*`
- Faster coding with import suggestions

**Setup:**
1. Install extension: "npm Intellisense"
2. Works automatically

**When to use:** All Node.js/Strapi projects

#### 6. JavaScript (ES6) Code Snippets

**What it does:** Provides code snippets for modern JavaScript

**How it helps Strapi:**
- Quickly scaffold controllers, services, routes
- Arrow functions, async/await patterns common in Strapi

**Setup:**
1. Install extension: "JavaScript (ES6) code snippets"

**When to use:** Rapidly writing Strapi backend code

#### 7. Database Management Extensions

**SQLTools**

**What it does:** Universal database client for VS Code

**How it helps Strapi:**
- Connect to PostgreSQL, MySQL, SQLite directly from editor
- Run queries, browse tables, view Strapi's database schema
- Supports multiple connection profiles

**Setup:**
1. Install: "SQLTools"
2. Install driver extension: "SQLTools PostgreSQL/MySQL/SQLite"
3. Create connection profile in VS Code settings
4. Connect to Strapi database

**Pros:**
- Multi-database support
- Query history
- IntelliSense for SQL

**Cons:**
- Requires separate driver extensions

**When to use:** Debugging database issues, exploring schema, running manual queries

**Microsoft PostgreSQL Extension**

**What it does:** Official PostgreSQL IDE for VS Code (public preview 2025)

**Features:**
- Context-aware IntelliSense
- GitHub Copilot '@pgsql' agent integration
- Connection manager
- Query execution and formatting

**Setup:**
1. Install: "PostgreSQL" (by Microsoft)
2. Connect to PostgreSQL database
3. Execute queries with IntelliSense

**When to use:** Strapi projects using PostgreSQL

#### 8. TypeScript Extensions

**TypeScript Importer**

**What it does:** Automatically finds and adds TypeScript imports

**How it helps Strapi:**
- Auto-import Strapi types from generated schemas
- Faster TypeScript development

**Setup:**
1. Install: "TypeScript Importer"
2. Works with generated types from `strapi ts:generate-types`

**When to use:** TypeScript Strapi projects

**VS Code Built-in TypeScript Support**

VS Code has excellent TypeScript support out-of-the-box:
- Real-time type checking
- IntelliSense for Strapi types
- Refactoring tools
- Go-to-definition for content types

**Setup for Strapi:**

Enable source maps in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "sourceMap": true
  }
}
```

Run type generation:

```bash
npm run strapi ts:generate-types
```

**When to use:** All TypeScript Strapi projects

#### 9. Jest Test Runner

**Jest Extension (by Orta)**

**What it does:** Full Jest integration with VS Code testing framework

**How it helps Strapi:**
- Run Strapi unit and integration tests
- Inline error reporting
- Code coverage visualization
- Automatic test discovery and running

**Setup:**
1. Install Jest: `npm install jest @types/jest --save-dev`
2. Install extension: "Jest"
3. Configure `jest.config.js`
4. Extension auto-detects Jest

**Features:**
- Run tests from sidebar
- Inline red underlines where tests fail
- Toggle code coverage via command palette
- Debug tests with breakpoints

**When to use:** Testing Strapi APIs, services, controllers

**Alternative:** "Jest Runner" extension for running individual tests via CodeLens

#### 10. Docker & Dev Containers

**Dev Containers Extension**

**What it does:** Develop inside Docker containers

**How it helps Strapi:**
- Consistent development environment across team
- Run Strapi + database in containers
- Avoids "works on my machine" issues

**Setup:**
1. Install: "Dev Containers"
2. Create `.devcontainer/devcontainer.json`
3. Configure with Strapi + database containers
4. Reopen in container

**Typical configuration:**

```json
{
  "name": "Strapi Development",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "strapi",
  "workspaceFolder": "/app",
  "extensions": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode"],
  "forwardPorts": [1337, 5432]
}
```

**When to use:**
- Teams needing identical environments
- Projects with complex dependencies
- Avoid local Node.js/database version conflicts

**When NOT to use:**
- Simple local development
- Resource-constrained machines

---

## 3. Editing Strapi Content from VS Code

### Approaches to Pulling Strapi Content into VS Code

#### Method 1: REST/GraphQL API + Custom Scripts

**Approach:** Write scripts to fetch content via Strapi APIs and save as local JSON files

**Example workflow:**

```javascript
// scripts/fetch-content.js
const fetch = require('node-fetch');
const fs = require('fs');

async function fetchArticles() {
  const response = await fetch('http://localhost:1337/api/articles');
  const data = await response.json();
  fs.writeFileSync('content/articles.json', JSON.stringify(data, null, 2));
}

fetchArticles();
```

**Run from VS Code terminal:**

```bash
node scripts/fetch-content.js
```

**Pros:**
- Simple to implement
- Works with any content type
- Can version content in Git

**Cons:**
- Manual sync required
- No real-time updates
- Need custom scripts for each content type

**When to use:** One-time exports, backup content, seeding test environments

**When NOT to use:** Continuous content editing by non-technical users

#### Method 2: Strapi Import/Export Plugin

**What it is:** Official and third-party plugins for bulk import/export

**Official CLI Commands:**

```bash
# Export all content
strapi export

# Import content
strapi import
```

**Features:**
- Exports content, files, config, schemas
- Encrypted and compressed tar.gz.enc format
- Options: `--only`, `--exclude`, `--no-encrypt`, `--no-compress`

**Third-party plugin: strapi-plugin-import-export-entries**

**What it does:**
- Import/export CSV and JSON
- Manual field mapping
- Import as draft or published
- Upload media from URLs
- Export without IDs/timestamps

**Setup:**
1. Install: `npm install strapi-plugin-import-export-entries`
2. Rebuild admin: `npm run build`
3. Access in Content Manager

**Pros:**
- Official support
- Handles relationships and files
- Good for migrations

**Cons:**
- Deletes all existing data on import (destructive)
- Source and target schemas must match
- Doesn't export admin users or API tokens

**When to use:**
- Environment migrations (dev → staging → production)
- Backups and restores
- Bulk content seeding

**When NOT to use:**
- Partial content updates
- Real-time content editing

#### Method 3: Database Direct Access (Not Recommended)

**Approach:** Connect to Strapi's database directly, query/edit records

**Tools:** SQLTools, PostgreSQL extension

**Pros:**
- Direct access to all data
- Powerful query capabilities

**Cons:**
- DANGEROUS: Bypasses Strapi's validation and lifecycle hooks
- Can corrupt data
- Breaks relationships
- No audit trail

**When to use:** Emergency database repairs by experienced DBAs only

**When NOT to use:** Regular content editing (use Strapi Admin UI or APIs instead)

### Workflows: Editing Content in VS Code vs Strapi Admin UI

#### Scenario 1: Developers Editing Content as Code

**Workflow:**
1. Export content to JSON via API or plugin
2. Edit JSON files in VS Code
3. Import back to Strapi
4. Commit JSON to Git for versioning

**Pros:**
- Content versioned in Git
- Developers comfortable with code
- Batch updates via scripts
- Merge conflicts solvable with Git tools

**Cons:**
- No WYSIWYG preview
- Complex for non-technical users
- Risk of malformed JSON
- Relationships hard to manage (IDs not human-readable)

**When to use:**
- Technical documentation
- Configuration-as-code
- Seed data for testing
- Migration scripts

**When NOT to use:**
- Marketing content with rich media
- Non-technical content editors
- Real-time collaboration

#### Scenario 2: Marketers Editing via Admin UI (Recommended)

**Workflow:**
1. Content editors use Strapi Admin UI
2. WYSIWYG editor for rich content
3. Media library for images/videos
4. Preview before publishing
5. Draft/Publish workflow

**Pros:**
- User-friendly interface
- Rich text editing (markdown, blocks, or custom WYSIWYG)
- Visual media management
- Role-based access control
- Audit logs

**Cons:**
- Content not directly in Git
- Requires Strapi instance access

**When to use:**
- Content marketing
- Blog posts, articles
- Non-technical users
- Real-time publishing

**Trade-offs Summary:**

| Factor | VS Code Editing | Admin UI Editing |
|--------|----------------|------------------|
| **Learning curve** | Requires technical skills | User-friendly |
| **Version control** | Git-native | Requires export/import |
| **Rich media** | Difficult | Built-in media library |
| **Collaboration** | Git merge conflicts | Real-time, role-based |
| **Preview** | None (JSON) | WYSIWYG |
| **Validation** | Manual | Automatic |
| **Best for** | Developers, config, seeds | Marketers, content creators |

---

## 4. Custom Developer Tooling

### Strapi CLI Commands

**Core commands for VS Code terminal:**

```bash
# Type generation
strapi ts:generate-types          # Generate TypeScript types
strapi ts:generate-types --debug  # Detailed output
strapi ts:generate-types -o types # Custom output directory

# Content generation
strapi generate                   # Interactive CLI wizard
strapi generate api article       # Generate API
strapi generate controller user   # Generate controller
strapi generate service product   # Generate service
strapi generate migration add_field  # Generate migration

# Development
strapi develop                    # Start development server
strapi build                      # Build admin panel
strapi start                      # Production server

# Data management
strapi export                     # Export data
strapi import                     # Import data
```

**Purpose:** Scaffold APIs, generate types, manage content

**When to use:** Initial setup, adding content types, keeping TypeScript in sync

### Example: Type Generation Workflow

**Setup automated type generation:**

Add to `package.json`:

```json
{
  "scripts": {
    "develop": "strapi develop",
    "types": "strapi ts:generate-types",
    "dev": "npm run types && npm run develop"
  }
}
```

**VS Code Tasks Integration:**

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Generate Strapi Types",
      "type": "shell",
      "command": "npm run types",
      "problemMatcher": []
    },
    {
      "label": "Build Strapi",
      "type": "shell",
      "command": "npm run build",
      "problemMatcher": []
    }
  ]
}
```

**Run tasks:** Terminal → Run Task → Select task

**Purpose:** Quick access to common commands without typing

**When to use:** Frequent type generation, builds, custom scripts

### Content Seeding Scripts

**Example: Seed development data**

Create `scripts/seed.js`:

```javascript
const strapi = require('@strapi/strapi');

async function seed() {
  const app = await strapi({ distDir: './dist' }).load();

  await strapi.query('api::article.article').create({
    data: {
      title: 'Hello World',
      content: 'This is a test article',
      publishedAt: new Date(),
    },
  });

  console.log('Seeded articles');
  await app.destroy();
}

seed();
```

**Run from VS Code terminal:**

```bash
node scripts/seed.js
```

**Purpose:** Populate database with test data for development

**When to use:**
- Fresh development environments
- Automated testing
- Demo data

**When NOT to use:** Production environments

### Migration Scripts

**Strapi's migration system:**

Generate migration:

```bash
strapi generate migration add_featured_flag
```

Creates: `database/migrations/[timestamp].add_featured_flag.js`

Example migration:

```javascript
module.exports = {
  async up(knex) {
    await knex.schema.alterTable('articles', (table) => {
      table.boolean('featured').defaultTo(false);
    });
  },

  async down(knex) {
    await knex.schema.alterTable('articles', (table) => {
      table.dropColumn('featured');
    });
  },
};
```

**Important:** Migrations run automatically on server start (no manual execution)

**When to use:** Database schema changes not handled by Strapi's automatic migrations

### Custom VS Code Tasks for Strapi

**Advanced `.vscode/tasks.json` example:**

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Strapi: Develop",
      "type": "shell",
      "command": "npm run develop",
      "problemMatcher": [],
      "isBackground": true
    },
    {
      "label": "Strapi: Build",
      "type": "shell",
      "command": "npm run build",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Strapi: Generate Types",
      "type": "shell",
      "command": "npm run strapi ts:generate-types",
      "problemMatcher": []
    },
    {
      "label": "Strapi: Seed Database",
      "type": "shell",
      "command": "node scripts/seed.js",
      "problemMatcher": []
    }
  ]
}
```

**Usage:** `Ctrl+Shift+P` → "Tasks: Run Task" → Select task

**Purpose:** Common Strapi operations accessible via command palette

---

## 5. DX, Performance, and Team Workflows

### Recommended VS Code Settings for Strapi Projects

**Workspace settings: `.vscode/settings.json`**

```json
{
  // ESLint
  "eslint.validate": ["javascript", "typescript"],
  "eslint.workingDirectories": ["./"],

  // Prettier
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // TypeScript
  "typescript.preferences.importModuleSpecifier": "relative",
  "typescript.updateImportsOnFileMove.enabled": "always",

  // Files
  "files.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.cache": true,
    "**/build": true
  },

  // Search
  "search.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.cache": true
  },

  // Git
  "git.ignoreLimitWarning": true,

  // Jest
  "jest.autoRun": "off",
  "jest.showCoverageOnLoad": false
}
```

**Purpose:** Consistent environment across team, optimized for Strapi structure

**Key configurations:**
- **Format on save:** Automatic code formatting
- **ESLint validation:** Real-time linting
- **File exclusions:** Hide build artifacts from search/explorer
- **TypeScript imports:** Relative paths for portability

### Code Navigation and Refactoring

**VS Code features for Strapi:**

1. **Go to Definition (F12):** Jump to controller/service definitions
2. **Find All References (Shift+F12):** Find where content types are used
3. **Rename Symbol (F2):** Refactor function/variable names safely
4. **IntelliSense:** Autocomplete for Strapi APIs and types

**TypeScript advantages:**
- Type-safe refactoring across files
- Catch errors before runtime
- Better autocomplete with generated types

**Setup:**
1. Use TypeScript Strapi project
2. Run `strapi ts:generate-types` regularly
3. Enable `sourceMap: true` in tsconfig.json

### Testing Configuration

**Jest setup for Strapi:**

Install dependencies:

```bash
npm install jest @types/jest supertest sqlite3 --save-dev
```

**jest.config.js:**

```javascript
module.exports = {
  testEnvironment: 'node',
  collectCoverageFrom: ['src/**/*.js'],
  coveragePathIgnorePatterns: ['/node_modules/'],
  testMatch: ['**/__tests__/**/*.js', '**/?(*.)+(spec|test).js'],
};
```

**Example test: `tests/article.test.js`:**

```javascript
const request = require('supertest');

it('should return articles', async () => {
  await request(strapi.server.httpServer)
    .get('/api/articles')
    .expect(200)
    .expect('Content-Type', /json/);
});
```

**VS Code integration:**
1. Install Jest extension
2. Tests appear in Testing sidebar
3. Run/debug individual tests
4. View coverage inline

**When to use:**
- API testing
- Unit testing services/controllers
- CI/CD integration

### Git and Team Collaboration

#### Recommended Branching Strategy

**GitHub Flow (recommended by Strapi community):**

1. **Main branch:** Always deployable
2. **Feature branches:** `feature/add-article-api`
3. **Pull requests:** Code review before merge
4. **Deploy:** From main branch

**Workflow:**
1. Create branch: `git checkout -b feature/new-content-type`
2. Develop in VS Code
3. Commit: `git commit -m "Add article content type"`
4. Push: `git push origin feature/new-content-type`
5. Open PR on GitHub
6. Review with team
7. Merge to main
8. Deploy

**Alternative: GitFlow** (for complex projects with release cycles)

**Purpose:** Organized collaboration, code review, safe deployments

#### What to Version Control

**Include in Git:**
- `/src` - Custom code, APIs, plugins
- `/config` - Configuration files
- `/database/migrations` - Migration scripts
- `package.json`, `package-lock.json`
- `.env.example` - Environment variable template
- `README.md`

**Exclude from Git (`.gitignore`):**
- `.env` - Environment variables with secrets
- `node_modules/` - Dependencies
- `dist/`, `build/`, `.cache/` - Build artifacts
- `.tmp/` - Temporary files
- `public/uploads/` - User-uploaded media (use S3/Cloudinary)

**Important:** Strapi writes content types as JSON/JS files, making them Git-friendly

#### Handling Environment Differences

**Problem:** Different databases, URLs, secrets across dev/staging/prod

**Solution:** Environment-specific .env files

**Setup:**

```bash
# Development
.env.development

# Staging
.env.staging

# Production
.env.production
```

**Load with:**

```bash
NODE_ENV=production npm start
```

**Strapi automatically loads:** `./config/env/production/*` when `NODE_ENV=production`

**Best practices:**
- Never commit `.env` files
- Use CI/CD secrets for production credentials
- Document required variables in `.env.example`

### CI/CD Integration

#### GitHub Actions for Strapi

**Example: `.github/workflows/strapi-ci.yml`**

```yaml
name: Strapi CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_PASSWORD: strapi
          POSTGRES_USER: strapi
          POSTGRES_DB: strapi
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
        env:
          DATABASE_CLIENT: postgres
          DATABASE_HOST: localhost
          DATABASE_PORT: 5432
          DATABASE_NAME: strapi
          DATABASE_USERNAME: strapi
          DATABASE_PASSWORD: strapi

      - name: Build
        run: npm run build
```

**Purpose:** Automated testing on every commit/PR

**Key features:**
- Runs tests in isolated environment
- Uses PostgreSQL service container
- Builds admin panel
- Blocks merge if tests fail

**When to use:** All team projects

#### Deployment Automation

**Common deployment targets:**
- **Heroku:** Git-based deployment
- **Vercel/Netlify:** Frontend hosting (with Strapi backend separate)
- **AWS/DigitalOcean:** VPS or container deployments
- **Docker:** Containerized deployments

**Example deployment workflow:**
1. Merge PR to main
2. GitHub Actions runs tests
3. If pass, build Docker image
4. Push to registry
5. Deploy to production

**Environment variable management:**
- Use GitHub Secrets for sensitive data
- Inject into CI/CD pipeline
- Never hardcode in workflows

### Performance Optimization in VS Code Workflow

#### Profiling Strapi Applications

**Tools:**

1. **Chrome DevTools:**
   - Start Strapi with `--inspect` flag
   - Open `chrome://inspect`
   - Profile CPU, memory, network

2. **VS Code Built-in Profiler:**
   - Launch with debugging
   - Use Performance view
   - Analyze slow functions

3. **Node.js Built-in:**
   ```bash
   node --prof ./node_modules/@strapi/strapi/bin/strapi.js develop
   ```

**When to use:** Identifying slow API endpoints, memory leaks

#### Code Optimization Strategies

**Database queries:**
- Add indexes to frequently queried fields
- Use Strapi's populate wisely (don't over-fetch)
- Paginate large collections

**Caching:**
- Install REST Cache plugin
- Cache frequently accessed content
- Use CDN for media (Cloudinary, S3)

**Monitoring in development:**
- Use Chrome DevTools Network tab
- Monitor API response times
- Identify N+1 query problems

**VS Code extensions for performance:**
- **Import Cost:** Shows size of imported packages
- **Bundle Analyzer:** Visualize bundle size (for frontend)

---

## 6. Limitations, Anti-Patterns, and Common Pitfalls

### Editing Content Outside Admin UI

**Limitations:**

1. **No validation:** Direct JSON editing bypasses Strapi's validation rules
2. **Relationships are fragile:** Require numeric IDs, easy to break
3. **No lifecycle hooks:** Custom logic in `beforeCreate`, `afterUpdate` won't run
4. **No media handling:** File uploads can't be managed via JSON
5. **No WYSIWYG preview:** Rich text is markdown or HTML strings
6. **Risk of corruption:** Malformed JSON breaks content

**Anti-patterns:**

1. **Direct database editing:** NEVER modify database directly
   - **Why:** Bypasses all Strapi logic, breaks relationships, corrupts data
   - **Instead:** Use Strapi APIs or Admin UI

2. **Committing `.env` files:** Exposes secrets
   - **Why:** Passwords, API keys in Git history
   - **Instead:** Use `.env.example`, document variables

3. **Editing content in Git for non-developers:** Confusing, error-prone
   - **Why:** Marketers struggle with JSON, IDs, merge conflicts
   - **Instead:** Use Admin UI, export only when necessary

4. **Skipping type generation:** Breaks TypeScript benefits
   - **Why:** Outdated types cause runtime errors
   - **Instead:** Run `strapi ts:generate-types` after schema changes

5. **Not using migrations for schema changes:** Manual database edits
   - **Why:** Changes not versioned, can't roll back
   - **Instead:** Use `strapi generate migration`

### Common Pitfalls

1. **Debugging port confusion:**
   - **Issue:** Strapi develop runs 2 processes (ports 9229 and 9230)
   - **Solution:** Configure debugger for port 9230 for core server

2. **Breakpoints not binding (TypeScript):**
   - **Issue:** Source maps not enabled
   - **Solution:** Add `"sourceMap": true` to tsconfig.json

3. **Import/export destroys data:**
   - **Issue:** `strapi import` deletes all existing data
   - **Solution:** Always backup before importing, test in dev environment

4. **Schema mismatch on import:**
   - **Issue:** Source and target schemas must match exactly
   - **Solution:** Import schemas first, then content

5. **Large node_modules slowing VS Code:**
   - **Issue:** Indexing millions of files
   - **Solution:** Add to `files.exclude` and `search.exclude` in settings

6. **Git merge conflicts in generated types:**
   - **Issue:** Multiple developers generate types simultaneously
   - **Solution:** Regenerate types after merging, don't manually resolve

7. **Jest tests timing out:**
   - **Issue:** Strapi instance takes time to start
   - **Solution:** Increase Jest timeout, use SQLite for tests

---

## Summary: When to Use What

| Task | Recommended Tool/Approach | When NOT to Use |
|------|--------------------------|----------------|
| **Daily development** | VS Code + integrated terminal, `npm run develop` | N/A |
| **Debugging** | VS Code launch.json with port 9230 | Simple console.log debugging |
| **API testing** | Thunder Client or REST Client extension | Complex multi-step workflows (use Postman) |
| **Database management** | SQLTools or PostgreSQL extension | Content editing (use Admin UI) |
| **Type generation** | `strapi ts:generate-types` after schema changes | Manual type writing |
| **Content editing (developers)** | Admin UI or APIs, NOT direct JSON | JSON editing for marketers |
| **Content editing (marketers)** | Strapi Admin UI exclusively | VS Code, Git, JSON |
| **Testing** | Jest + VS Code Jest extension | Manual testing (not scalable) |
| **Version control** | Git with GitHub Flow, exclude .env | Committing secrets, media uploads |
| **CI/CD** | GitHub Actions with automated tests | Manual deployments |
| **Environment management** | .env files, never commit | Hardcoded credentials |
| **Migrations** | `strapi generate migration` | Direct database ALTER statements |
| **Performance profiling** | Chrome DevTools + VS Code debugger | Guessing without data |

---

## Sources

- [13 Essential VS Code Extensions for 2025](https://strapi.io/blog/vs-code-extensions)
- [Debugging strapi in Visual Studio Code - Stack Overflow](https://stackoverflow.com/questions/58145392/debugging-strapi-in-visual-studio-code)
- [Strapi v4 debug breakpoints do not bind in VS Code - Strapi Forum](https://forum.strapi.io/t/strapi-v4-debug-breakpoints-do-not-bind-in-vs-code/21181)
- [TypeScript Integration with Strapi Headless CMS](https://strapi.io/integrations/typescript-cms)
- [TypeScript development | Strapi 5 Documentation](https://docs.strapi.io/cms/typescript/development)
- [Command Line Interface | Strapi 5 Documentation](https://docs.strapi.io/cms/cli)
- [Database migrations | Strapi 5 Documentation](https://docs.strapi.io/cms/database-migrations)
- [Data import | Strapi 5 Documentation](https://docs.strapi.io/cms/data-management/import)
- [Data export | Strapi 5 Documentation](https://docs.strapi.io/cms/data-management/export)
- [Importing, Exporting & Transferring Data with Strapi CLI](https://strapi.io/blog/importing-exporting-and-transferring-data-with-the-strapi-cli)
- [Environment variables | Strapi Documentation](https://docs-v4.strapi.io/dev-docs/configurations/environment)
- [Git and Version Control Best Practices](https://strapi.io/blog/git-and-version-control)
- [Getting Started with Strapi Workflows Using Git!](https://strapi.io/blog/getting-started-with-strapi-workflows-using-git)
- [Thunder Client – An Alternative Way to Test Restful APIs](https://www.freecodecamp.org/news/thunder-client-for-vscode/)
- [Postman vs Thunder Client: API Testing Tools and Alternatives](https://apidog.com/blog/postman-vs-thunder-client/)
- [SQLTools - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
- [PostgreSQL - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-ossdata.vscode-pgsql)
- [Microsoft PostgreSQL Extension Announcement](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)
- [Database configuration | Strapi 5 Documentation](https://docs.strapi.io/cms/configurations/database)
- [How to Connect Strapi to PostgreSQL](https://strapi.io/blog/postgre-sql-and-strapi-setup)
- [Testing | Strapi 5 Documentation](https://docs.strapi.io/cms/testing)
- [Automated Testing for Strapi API With Jest and Supertest](https://strapi.io/blog/automated-testing-for-strapi-api-with-jest-and-supertest)
- [Jest Extension - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest)
- [Better Unit Testing in Visual Studio Code with Jest](https://plainenglish.io/blog/better-unit-testing-in-visual-studio-code-with-jest)
- [Create a Dev Container - VS Code](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
- [How to run a Strapi dev stack using Docker compose](https://strapi.io/blog/how-to-run-a-strapi-dev-stack-with-docker-compose)
- [Docker | Strapi 5 Documentation](https://docs.strapi.io/cms/installation/docker)
- [Admin Panel API | Strapi 5 Documentation](https://docs.strapi.io/cms/plugins-development/admin-panel-api)
- [Developing plugins | Strapi 5 Documentation](https://docs.strapi.io/cms/plugins-development/developing-plugins)
- [GitHub Actions for Strapi CI/CD](https://strapi.io/blog/getting-started-with-strapi-workflows-using-git)
- [Streamlining Your Strapi CMS CI/CD Pipeline](https://medium.com/@asit.panda/streamlining-your-strapi-cms-ci-cd-pipeline-a-guide-to-plugin-setup-25885ef20b15)
- [How to Improve Strapi Performance (2025 Guide)](https://strapi.io/blog/how-to-optimize-strapi-performance)
- [Optimize Performance of Strapi-Powered Websites](https://strapi.io/blog/how-to-optimize-performance-of-strapi-powered-websites-and-applications-techniques-and-best-practices)
- [Improve Your Frontend Experience With Strapi Types And TypeScript](https://strapi.io/blog/improve-your-frontend-experience-with-strapi-types-and-type-script)
- [Strapi & CKEditor: pairing headless CMS with WYSIWYG editor](https://ckeditor.com/blog/strapi-and-ckeditor/)
- [How to change the WYSIWYG in Strapi](https://strapi.io/blog/how-to-change-the-wysiwyg-in-strapi/)

---

**End of Research Document**
