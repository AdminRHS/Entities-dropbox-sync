# MCP Server (Model Context Protocol)

AI agent interface for direct database operations via standardized protocol.

## Overview

- **Protocol**: [Model Context Protocol](https://modelcontextprotocol.io) (Anthropic standard)
- **Purpose**: Allow AI agents (Claude, ChatGPT, etc.) to perform CRUD operations directly
- **Endpoint**: `/mcp`
- **Authentication**: Token-based (separate from main API)
- **Added**: November 12, 2025
- **Multi-language**: Supports UA/RU/EN resource names

## What is MCP?

MCP (Model Context Protocol) is a standardized protocol that allows AI agents to interact with external systems. Instead of making AI generate API calls as text, MCP provides a structured way for AI to:
- List available operations (tools)
- Execute operations with validated schemas
- Get structured responses

## Architecture

```
AI Agent (Claude/ChatGPT)
    ↓ (MCP Protocol)
MCP Server (/mcp endpoint)
    ↓ (Token Auth)
McpService (API wrapper)
    ↓ (HTTP requests)
Main API (CRUD operations)
    ↓
PostgreSQL Database
```

## MCP Tools

### 1. list
List resources with pagination
```javascript
{
  resource: "departments" | "professions" | "languages" | ...,
  page: 1,
  limit: 20,
  search: "optional",
  all: false
}
```

### 2. get
Get single resource by ID
```javascript
{
  resource: "department",
  id: 123
}
```

### 3. create
Create new entity with optional AI metadata
```javascript
{
  resource: "professions",
  payload: {
    mainTerm: {
      value: "Software Engineer",
      language_id: 1,
      term_type_id: 1,
      // AI Metadata (optional)
      ai_generated: true,
      ai_model: "claude-sonnet-4",
      ai_prompt_version: "v1.0",
      ai_validation_status: "approved",
      ai_confidence_score: 0.95
    },
    department_id: 5,
    tool_ids: [1, 2, 3]
  }
}
```

### 4. update
Update existing entity
```javascript
{
  resource: "professions",
  id: "123",
  payload: {
    mainTerm: {
      value: "Updated Name",
      language_id: 1,
      term_type_id: 1,
      ai_generated: true,
      ai_model: "gpt-4o-mini"
    }
  }
}
```

### 5. get_term_types
Get available term types
```javascript
// No parameters
// Returns: [{ id: 1, name: "main" }, { id: 2, name: "similar" }, ...]
```

### 6. create_term
Create individual term
```javascript
{
  term_group_id: 123,
  value: "New Term",
  language_id: 1,
  term_type_id: 1,
  ai_generated: true,
  ai_model: "claude-sonnet-4"
}
```

### 7. update_term
Update individual term
```javascript
{
  id: 456,
  value: "Updated Term",
  ai_model: "gpt-4o-mini"
}
```

### 8. find_responsibility_terms
Find existing responsibilities by action/object
```javascript
{
  language_id: 1,
  action_id: 5,    // optional
  object_id: 10    // optional
}
```

### 9. find_skill_terms
Find existing skills by responsibility/tool
```javascript
{
  language_id: 1,
  responsibility_id: 15,  // optional
  tool_id: 3             // optional
}
```

## AI Metadata Support

MCP automatically supports AI metadata for all term-based entities:

### Available AI Fields
```javascript
{
  ai_generated: boolean,        // Is this AI-generated?
  ai_model: string,             // Model used (required if ai_generated=true)
  ai_prompt_version: string,    // Prompt version
  ai_validation_status: string, // "pending"|"approved"|"rejected"|"needs_review"
  ai_confidence_score: number,  // 0.0 to 1.0
  ai_notes: string,             // Additional notes
  ai_last_human_review: string  // ISO 8601 timestamp
}
```

### Validation Rules
- If `ai_generated: true`, then `ai_model` is **required**
- When creating AI content, **always include** `ai_generated` and `ai_model`
- AI metadata is optional for non-AI-generated content

## Multi-language Resource Names

MCP supports resource names in Ukrainian, Russian, and English:

### Examples
```javascript
// All equivalent:
list({ resource: "departments" })
list({ resource: "департаменти" })
list({ resource: "отделы" })

// All equivalent:
get({ resource: "profession", id: 1 })
get({ resource: "професія", id: 1 })
get({ resource: "профессия", id: 1 })
```

### Supported Resources
- **Departments**: departments, департаменти, відділи, отделы
- **Professions**: professions, професії, профессии
- **Languages**: languages, мови, языки
- **Countries**: countries, країни, страны
- **Cities**: cities, міста, города
- **Industries**: industries, індустрії, индустрии
- **Skills**: skills, навички, навыки, умения
- **Tools**: tools, інструменти, инструменты
- And 15+ more resources...

## Session Management

### Session Lifecycle
1. **Initialize**: First request creates session with unique ID
2. **Active**: Session remains active with API token
3. **Idle Timeout**: Closes after 24 hours of inactivity
4. **Max Lifetime**: Closes after 7 days even if active
5. **Cleanup**: Expired sessions cleaned every hour

### Configuration
```javascript
sessionIdleTimeout: 24 * 60 * 60 * 1000,      // 24 hours
sessionMaxLifetime: 7 * 24 * 60 * 60 * 1000,  // 7 days
cleanupInterval: 3600000,                      // 1 hour
```

## Rate Limiting

### Initialize Requests
- **Limit**: Configurable per window
- **Window**: From config (default varies)
- **Purpose**: Prevent session creation spam

### General Requests
- **Limit**: Configurable per window
- **Window**: From config
- **Purpose**: Prevent API abuse

## Authentication Flow

```
1. AI Agent initiates MCP connection
2. MCP Server requests API token
3. User provides token (via initialize params or separate auth)
4. Token stored in session (sessionTokens map)
5. All subsequent requests use stored token
6. McpService forwards requests with token to main API
7. Main API validates token and processes request
```

## Health Check

```bash
GET /mcp/health

Response:
{
  "status": "ok",
  "service": "libraries-service-mcp",
  "version": "1.0.0",
  "timestamp": "2025-12-12T20:00:00.000Z",
  "metrics": {
    "activeSessions": 5,
    "memoryUsage": {
      "heapUsed": 120,
      "heapTotal": 200,
      "rss": 250
    }
  },
  "uptime": 86400
}
```

## Use Cases

### When to Use MCP

MCP is ideal for:
- **AI Agents** (Claude, ChatGPT, etc.) performing direct database operations
- **Automated workflows** that need to create/update entities programmatically
- **Data migration** scripts that want to preserve AI metadata
- **Bulk operations** with AI-generated content tracking
- **Cross-language operations** (works with UA/RU/EN resource names)

## Usage Examples

### Example 1: Create AI-generated Profession via Claude
```javascript
// Claude calls MCP create tool
{
  resource: "professions",
  payload: {
    mainTerm: {
      value: "DevOps Engineer",
      language_id: 1,  // English
      term_type_id: 1,  // main
      ai_generated: true,
      ai_model: "claude-sonnet-4-5",
      ai_confidence_score: 0.92
    },
    department_id: 3
  }
}

// Result: Profession created with AI metadata
```

### Example 2: List Departments in Ukrainian
```javascript
// Claude calls MCP list tool
{
  resource: "департаменти",
  page: 1,
  limit: 10
}

// Returns: List of departments with pagination
```

### Example 3: Update Term with AI Model Info
```javascript
// ChatGPT calls MCP update_term tool
{
  id: 123,
  value: "Machine Learning Engineer",
  ai_generated: true,
  ai_model: "gpt-4o-mini",
  ai_validation_status: "approved"
}
```

## File Locations

- **Server**: `src/mcp/server.js`
- **Handlers**: `src/mcp/handlers.js`
- **Service**: `src/mcp/services/mcpService.js`
- **Routes**: `src/routes/mcp.js`
- **Config**: `config/config.js` (mcp section)

## Configuration

Located in `config/config.js`:
```javascript
mcp: {
  requestTimeout: 30000,           // 30 seconds
  sessionIdleTimeout: 86400000,    // 24 hours
  sessionMaxLifetime: 604800000,   // 7 days
  cleanupInterval: 3600000,        // 1 hour
  maxRequestSize: 10485760,        // 10 MB
  rateLimit: {
    windowMs: 60000,
    maxRequests: 100,
    maxInitializeRequests: 10
  }
}
```

## Error Handling

MCP uses JSON-RPC 2.0 error format:
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32004,
    "message": "Too many requests"
  },
  "id": null
}
```

### Common Error Codes
- `-32004`: Rate limit exceeded
- `-32005`: Request too large
- Standard HTTP codes for API errors

---

**See Also**: [API.md](API.md), [AUTH.md](AUTH.md), [DATABASE.md](DATABASE.md)
