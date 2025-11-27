---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_024
title: Video 024
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# Video 024

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video_024 Transcription Template

## 1. Metadata Section
- **Video Title**: Tutorial: Auth for Remote MCP Servers (Step by Step) | OAuth 2.1 with ScaleKit
- **Channel/Creator**: Alejandro AO - Software & AI
- **Video URL**: https://youtu.be/gl6U8s3zStI?si=rXdONo9LW2fe7jWF
- **Duration**: 38:53
- **Publication Date**: 2025-08-25

## 2. Description Section
- **Description**: In-depth walkthrough demonstrating how to secure MCP (Model Context Protocol) servers with OAuth 2.1 using FastAPI, FastMCP, and ScaleKit. Covers end-to-end authentication workflow, token validation, discovery endpoints, and production-ready best practices for integrating MCP tools with AI agents.
- **Key Topics**:
  - OAuth 2.1 fundamentals inside MCP ecosystem
  - FastAPI + FastMCP server setup with auth middleware
  - ScaleKit account configuration, scopes, and permissions
  - JWT validation, discovery endpoints, and secure tool execution
  - Testing MCP auth flows with AI clients
- **Links Referenced**:
  - [Code from the video](https://github.com/alejandro-ao/mcp-f...) — project source
  - [ScaleKit](https://www.scalekit.com/) — auth platform used
  - [MCP Course Waitlist](https://link.alejandro-ao.com/join-mcp) — additional training
  - [Full Stack AI Engineering Bootcamp](https://aibootcamp.dev) — Alejandro’s bootcamp
  - [Buy me a coffee / beer](https://link.alejandro-ao.com/l83gNq) — creator support
  - [Discord Help Server](https://link.alejandro-ao.com/HrFKZn) — community support

## 3. Word-for-Word Transcription

[00:00] **Speaker (Alejandro)**: Good morning, everyone. How's it going today? Welcome back to the channel. In today's video, I'm going to show you how to add authentication to your MCP servers.
[00:09] **Speaker**: In other words, how to add OAuth 2.1 to your remote MCP servers that run on top of the streamable HTTP transport. So let me show you what this will look like by the end of this video.
[00:22] **Speaker**: Right here I have an MCP server called Test Tavilli, and this one has authentication enabled. I'm going to click Start and it immediately asks me to authenticate. I hit Allow, Open, and I'm redirected to the auth page.
[00:35] **Speaker**: I'll click Log in with Google. There we go—now I'm logged in and can head back to VS Code.
[00:49] **Speaker**: My MCP server is running with one tool enabled. On top of this, you can add scopes, even charge users before granting access. That's where we want to end up by the close of this tutorial, so let's jump in.
[01:14] **Speaker**: Before we start, if you're not familiar with authentication and authorization, some of this might be new. Don't worry—I explain everything clearly so it all makes sense.
[01:35] **Speaker**: You can grab the code for this video from the repo linked in the description. Follow along to ensure everything works. Questions? Drop them in the comments.
[01:51] **Speaker**: By the way, I'm launching an MCP course covering both servers and clients. Join the waitlist in the description—if you're watching later it might already be live.
[02:12] **Speaker**: First, I want to show you the starting point before we add authentication. I already have my MCP server working. I initialized my FastMCP server—remember FastMCP automatically hosts your MCP server on `/mcp` from wherever you deploy it.
[02:48] **Speaker**: I also initialized my Tavilli client because in this demo I'm using a web search tool. Tavilli is a search engine for LLMs and it works great. The tool just searches the web based on a query and returns results.
[03:10] **Speaker**: I have a config file with my Tavilli API key and the port—we’re running on port 10,000. I've mounted this MCP server on top of a FastAPI application by importing the server, renaming it `Tavilli MCP server`, appending the session manager to the lifespan function, and adding CORS middleware.
[04:13] **Speaker**: The FastMCP application is mounted at the root, so it’s available at `/mcp`. We're on localhost:10000. Let me run it with `uv run my-mcp-server`.
[04:43] **Speaker**: Now I'll open the MCP inspector and connect to `http://localhost:10000/mcp`. No authentication yet, so I can connect, list tools, pick Web Search, run `hello world`, and it returns results. Time to add auth.
[05:25] **Speaker**: Let me introduce OAuth 2.1 quickly. If you're already familiar, skip ahead. OAuth 2.1 is the officially mandated standard by the MCP spec and must be implemented on both client and server for streamable HTTP.
[06:34] **Speaker**: It's a sophisticated workflow. The client connects, gets a 401 unauthorized, follows a breadcrumb trail to discover endpoints, requests tokens from the authorization server, and eventually receives a JWT it can use to access the server.
[08:37] **Speaker**: Implementing this yourself can be complex—you’d maintain the authorization server, resource owner connections, Google/GitHub identity, etc. Instead, you can use ScaleKit, which simplifies everything drastically.
[09:32] **Speaker**: With ScaleKit the client still gets an unauthorized response, but your MCP server only needs to expose the discovery endpoint. ScaleKit handles the heavy auth flow and returns the JWT. Your job: add the well-known endpoint, build auth middleware, send 401 headers, and validate tokens.
[11:06] **Speaker**: To illustrate, let's pretend we're the MCP client. I'll connect to localhost:10000/mcp. I get an error because I'm not authenticated. I make a tool call and get a 401 with a header containing the resource metadata URI.
[12:19] **Speaker**: That header points to `/.well-known/oauth-protected-resource`. We must create this endpoint in our app. I hit it and get JSON describing auth servers, methods, resource name, documentation, and scopes like `search:read`.
[13:10] **Speaker**: The client continues following the trail, hitting the well-known OAuth authorization server, discovering issuer, authorization endpoint, token endpoint, introspection endpoint, and revocation endpoint.
[14:09] **Speaker**: Next the client requests a token using the ScaleKit credentials, gets an access token (JWT), and stores it. Back in the inspector, I paste the token into the authentication tab, click connect, and now the tool works.
[15:01] **Speaker**: So that's the flow we’re implementing. On our side we just add the well-known endpoint, create auth middleware, emit 401s with the header, and validate tokens. ScaleKit handles the rest.
[15:56] **Speaker**: ScaleKit is a modular auth platform for AI apps with a dedicated MCP auth space. You create your MCP server profile in their dashboard, add details, set scopes, and you’re done. Free tier covers 10k monthly active users.
[17:14] **Speaker**: Step one: create an account and register your MCP server. Activate full-stack auth, configure permissions, add scopes like `search:read` with human-readable descriptions.
[18:34] **Speaker**: Register the MCP server (I call it demo-auth). Set the identifier to the exact MCP URL, including the trailing slash. Enable dynamic registration and assign the `search:read` permission.
[19:47] **Speaker**: ScaleKit tells you to create an endpoint that returns the metadata JSON. Copy their JSON, paste it into your FastAPI endpoint at `/.well-known/oauth-protected-resource`, and return it. Test by hitting the endpoint—should respond with the JSON.
[21:09] **Speaker**: That endpoint lets clients discover where to authenticate. But how do they find it? When an unauthorized call happens, we return a `WWW-Authenticate` header pointing to the well-known URL. That’s part of the auth middleware we need to build.
[21:57] **Speaker**: I created an `AuthMiddleware` class (Starlette BaseHTTPMiddleware). If the request is for a well-known endpoint, we allow it. Otherwise we check for a bearer token. If there’s no token, we raise 401 and include the `resource-metadata` header pointing to the well-known URL.
[23:02] **Speaker**: The middleware imports the ScaleKit Python SDK, initializes the client with env URL, client ID, and client secret sourced from `.env`. Those values come from the ScaleKit workspace settings.
[24:46] **Speaker**: When a request arrives, we let discovery endpoints through. Everything else must include a bearer token. On failure we append the header with the metadata URL (stored in env as `SCALEKIT_RESOURCE_METADATA_URL`).
[25:57] **Speaker**: Now we need to validate tokens. Once the client has a JWT, it will call our server with `Authorization: Bearer <token>`. We parse the request body to check if it’s a tool call and gather the request method.
[29:26] **Speaker**: We define validation options (issuer, audience, required scopes). Issuer is the ScaleKit environment URL. Audience matches the MCP resource identifier (`http://localhost:10000/mcp/`). For tool calls we require `search:read`.
[31:46] **Speaker**: Using the latest SDK we call `validate_token(token, validation_options)`. If validation passes, the middleware proceeds; errors are caught and turned into 401 responses with the header. That’s all the validation we need.
[33:56] **Speaker**: Summarizing: unauthorized call → 401 with metadata header. Client discovers endpoints, authenticates via ScaleKit, gets JWT, retries with token. Middleware validates token, then request proceeds to the Tavilli tool.
[35:44] **Speaker**: Time to test. Restart the MCP server, click Restart in VS Code, allow the connection, login with Google, authorize, and we're back in VS Code with the authenticated server running.
[36:50] **Speaker**: I run a query: “Search the web using Tavilli for Sam Altman's latest news.” The agent uses the Tavilli tool and returns results. Everything works end-to-end with authentication enforced.
[37:25] **Speaker**: This was a high-level intro to MCP authentication with OAuth 2.1. MCP servers are increasingly remote over HTTP, so this pattern is essential. Thanks for watching—if you want a deeper dive, join the MCP course waitlist in the description. See you in the next one.

---

# TAXONOMY ANALYSIS

## 4. Milestone Templates Identification
```
MILESTONE_ID: MLS-001
MILESTONE_NAME: Prepare Baseline MCP Server
OBJECTIVE: Stand up the FastMCP-powered Tavilli server locally on HTTP transport
TASKS:
  1. TSK-001: Initialize FastMCP service - Scaffold Tavilli MCP server with FastAPI
  2. TSK-002: Mount Tavilli search tool - Wire Tavilli client and config into the server
  3. TSK-003: Verify unauthenticated workflow - Run inspector test without auth
DURATION: 20-30 minutes
COMPLEXITY: Low
DEPARTMENT: AID (AI & Automations)
RELATED_ENTITIES:
  - Tasks: TSK-001, TSK-002, TSK-003
  - Skills: SKL-042 (AI Agent Development), SKL-006 (API Configuration)
  - Responsibilities: RSP-201 (MCP Server Setup)
  - Professions: PRF-003 (AI Engineer)
```

```
MILESTONE_ID: MLS-002
MILESTONE_NAME: Configure ScaleKit Authorization Stack
OBJECTIVE: Set up ScaleKit workspace, scopes, and MCP server registration
TASKS:
  1. TSK-004: Activate ScaleKit environments - Enable full-stack auth modules
  2. TSK-005: Define OAuth scopes - Create `search:read` permission with human copy
  3. TSK-006: Register MCP identifier - Map localhost endpoint and enable dynamic registration
DURATION: 25-35 minutes
COMPLEXITY: Medium
DEPARTMENT: SEC (Security Engineering) / AID
RELATED_ENTITIES:
  - Tasks: TSK-004, TSK-005, TSK-006
  - Skills: SKL-078 (Identity & Access Management)
  - Responsibilities: RSP-315 (OAuth Policy Configuration)
  - Professions: PRF-012 (Security Engineer)
```

```
MILESTONE_ID: MLS-003
MILESTONE_NAME: Implement OAuth Discovery & Middleware
OBJECTIVE: Add well-known endpoint plus middleware that enforces ScaleKit-issued JWTs
TASKS:
  1. TSK-007: Publish well-known metadata - Serve ScaleKit JSON at `/.well-known/oauth-protected-resource`
  2. TSK-008: Build auth middleware - Intercept requests and issue 401 with metadata header
  3. TSK-009: Validate bearer tokens - Use ScaleKit SDK to verify issuer, audience, and scopes
DURATION: 30-40 minutes
COMPLEXITY: Medium-High
DEPARTMENT: AID;SEC
RELATED_ENTITIES:
  - Tasks: TSK-007, TSK-008, TSK-009
  - Skills: SKL-042 (AI Agent Development), SKL-081 (Token Validation)
  - Responsibilities: RSP-333 (Secure MCP Gateway)
  - Professions: PRF-003 (AI Engineer), PRF-012 (Security Engineer)
```

```
MILESTONE_ID: MLS-004
MILESTONE_NAME: Test Authenticated MCP Workflow
OBJECTIVE: Validate OAuth trail, login, and Tavilli execution from MCP clients
TASKS:
  1. TSK-010: Simulate client discovery - Manually follow breadcrumb headers via inspector
  2. TSK-011: Authenticate via OAuth provider - Complete Google login through ScaleKit UI
  3. TSK-012: Execute secured tool calls - Run Tavilli search with enforced scopes
DURATION: 20 minutes
COMPLEXITY: Medium
DEPARTMENT: QA (Quality) / AID
RELATED_ENTITIES:
  - Tasks: TSK-010, TSK-011, TSK-012
  - Skills: SKL-019 (Test & Validation), SKL-078 (IAM)
  - Responsibilities: RSP-410 (Secure Workflow QA)
  - Professions: PRF-020 (QA Automation)
```

## 5. Action Verbs & Operations
### A. CREATION VERBS
- Initialize
- Configure
- Register
- Create
- Build
- Publish

### B. MODIFICATION VERBS
- Update
- Append
- Mount
- Enable
- Restart

### C. ANALYSIS VERBS
- Inspect
- Verify
- Validate
- Test
- Monitor
- Review

### D. ORGANIZATION VERBS
- Define
- Map
- Assign
- Sequence
- Document
- Route

### E. COMMUNICATION VERBS
- Explain
- Demonstrate
- Authorize
- Notify
- Share
- Describe

### F. BROWSER/AGENTIC OPERATIONS
- Authenticate
- Redirect
- Connect
- Follow (link)
- Log in
- Call endpoint
- Request token
- Respond

### G. DATA OPERATIONS
- Issue (JWT)
- Validate (token)
- Parse (request)
- Append (header)
- Store (credentials)
- Return (JSON)
- Execute (tool)

## 6. Task Templates Identification
```
TASK_ID: TSK-007
TASK_NAME: Publish Well-Known Metadata Endpoint
DESCRIPTION: Serve ScaleKit-provided OAuth resource metadata JSON from FastAPI at `/.well-known/oauth-protected-resource/mcp`
RESPONSIBILITY: RSP-333 (Secure MCP Gateway)
STEPS:
  1. STP-001: Copy metadata JSON from ScaleKit dashboard - ACT-040 (Verify)
  2. STP-002: Load JSON string into FastAPI route - ACT-015 (Create)
  3. STP-003: Return JSONResponse with correct headers - ACT-050 (Export)
DURATION: 10 minutes
TOOLS_REQUIRED: TOL-101 (FastAPI), TOL-109 (ScaleKit Dashboard)
SKILLS_REQUIRED: SKL-042 (AI Agent Development)
ASSIGNED_TO: PRF-003 (AI Engineer)
PARENT_MILESTONE: MLS-003
DEPARTMENT: AID;SEC
```

```
TASK_ID: TSK-008
TASK_NAME: Build Authentication Middleware
DESCRIPTION: Intercept MCP HTTP calls, allow discovery endpoints, enforce bearer token presence, and emit metadata breadcrumb on failure
RESPONSIBILITY: RSP-333 (Secure MCP Gateway)
STEPS:
  1. STP-004: Extend BaseHTTPMiddleware - ACT-110 (Extend)
  2. STP-005: Check request path for well-known routes - ACT-025 (Inspect)
  3. STP-006: Raise 401 with WWW-Authenticate header when token missing - ACT-055 (Map)
DURATION: 20 minutes
TOOLS_REQUIRED: TOL-101 (FastAPI), TOL-115 (Starlette)
SKILLS_REQUIRED: SKL-081 (Token Validation)
ASSIGNED_TO: PRF-003 (AI Engineer)
PARENT_MILESTONE: MLS-003
DEPARTMENT: AID;SEC
```

```
TASK_ID: TSK-009
TASK_NAME: Validate Bearer Tokens with ScaleKit SDK
DESCRIPTION: Use ScaleKit Python client to confirm issuer, audience, and scope before forwarding tool calls
RESPONSIBILITY: RSP-333 (Secure MCP Gateway)
STEPS:
  1. STP-007: Initialize ScaleKit client using env vars - ACT-030 (Configure)
  2. STP-008: Assemble validation options (issuer, audience) - ACT-045 (Organize)
  3. STP-009: Call `validate_token` with scope requirements - ACT-070 (Execute)
DURATION: 15 minutes
TOOLS_REQUIRED: TOL-118 (ScaleKit Python SDK)
SKILLS_REQUIRED: SKL-078 (IAM), SKL-042 (AI Agent Development)
ASSIGNED_TO: PRF-012 (Security Engineer)
PARENT_MILESTONE: MLS-003
DEPARTMENT: SEC
```

```
TASK_ID: TSK-012
TASK_NAME: Execute Secured Tavilli Tool Call
DESCRIPTION: After authentication, run Tavilli search via MCP inspector to confirm JWT enforcement
RESPONSIBILITY: RSP-410 (Secure Workflow QA)
STEPS:
  1. STP-010: Paste bearer token in MCP inspector auth field - ACT-060 (Input)
  2. STP-011: Invoke Tavilli search for target query - ACT-070 (Execute)
  3. STP-012: Review results and scope enforcement logs - ACT-040 (Verify)
DURATION: 10 minutes
TOOLS_REQUIRED: TOL-122 (MCP Inspector), TOL-125 (VS Code MCP Client)
SKILLS_REQUIRED: SKL-019 (Testing)
ASSIGNED_TO: PRF-020 (QA Automation)
PARENT_MILESTONE: MLS-004
DEPARTMENT: AID;QA
```

## 7. Step Templates Identification
```
STEP_ID: STP-001
STEP_NAME: Copy metadata JSON from ScaleKit dashboard
ACTION: ACT-040 (Verify)
OBJECT: OBJ-210 (OAuth Metadata Bundle)
PROBABILITY_SCORE: 0.95
TOOL: TOL-109 (ScaleKit Dashboard)
INPUT: ScaleKit MCP server config
OUTPUT: Copied JSON string
DURATION: 2 minutes
PARENT_TASK: TSK-007

STEP_ID: STP-004
STEP_NAME: Extend BaseHTTPMiddleware
ACTION: ACT-110 (Extend)
OBJECT: OBJ-312 (Middleware Class)
PROBABILITY_SCORE: 0.9
TOOL: TOL-115 (Starlette)
INPUT: Existing FastAPI project
OUTPUT: Custom AuthMiddleware subclass
DURATION: 5 minutes
PARENT_TASK: TSK-008

STEP_ID: STP-007
STEP_NAME: Initialize ScaleKit client using env vars
ACTION: ACT-030 (Configure)
OBJECT: OBJ-220 (Auth Client Instance)
PROBABILITY_SCORE: 0.85
TOOL: TOL-118 (ScaleKit Python SDK)
INPUT: ENV secrets (client_id, secret, env_url)
OUTPUT: Ready-to-use ScaleKit client
DURATION: 4 minutes
PARENT_TASK: TSK-009

STEP_ID: STP-010
STEP_NAME: Paste bearer token in MCP inspector auth field
ACTION: ACT-060 (Input)
OBJECT: OBJ-402 (Auth Session)
PROBABILITY_SCORE: 0.9
TOOL: TOL-122 (MCP Inspector)
INPUT: JWT from ScaleKit token endpoint
OUTPUT: Authenticated MCP inspector session
DURATION: 2 minutes
PARENT_TASK: TSK-012
```

## 8. Task Chains
```
TASK CHAIN: Secure MCP Auth Deployment
TSK-004 (Activate ScaleKit environments) → TSK-005 (Define OAuth scopes) → TSK-006 (Register MCP identifier) → TSK-007 (Publish well-known metadata) → TSK-008 (Build auth middleware) → TSK-009 (Validate bearer tokens) → TSK-012 (Execute secured Tavilli tool)
```

## 9. Action-Object-Tool Probability Mapping
1. **Tag Action:** "Validate token" → ACT-070 (Execute)
2. **Mark Object:** JWT access token → OBJ-305 (Access Credential) [Probability: 0.95]
3. **Search Tool:** ScaleKit Python SDK → TOL-118
4. **Link Responsibility:** Secure gateway token enforcement → RSP-333
5. **Identify Skills:** IAM configuration & Python SDK usage → SKL-078, SKL-042
6. **Identify Step:** STP-009 `Call validate_token with scope requirements`
7. **Group to Task:** TSK-009 `Validate Bearer Tokens with ScaleKit SDK`
8. **Cluster to Milestone:** MLS-003 `Implement OAuth Discovery & Middleware`

## 10. Responsibilities Vocabulary
- **Roles Mentioned/Implied**:
  - AI Engineer
  - Security Engineer
  - MCP Instructor / Educator
  - QA Automation Specialist
- **Activities**:
  - Hosting FastMCP servers
  - Creating OAuth scopes and permissions
  - Managing ScaleKit environments
  - Validating JWT tokens
  - Testing agent tool calls end-to-end
- **Skills**:
  - IAM & OAuth 2.1 fundamentals
  - FastAPI / Starlette middleware development
  - ScaleKit platform administration
  - MCP inspector diagnostics
  - Secure AI workflow testing

## 8. Tools & Technologies Matrix
| Tool_ID | Tool Name | Category | Purpose | Department | Source_Video | Related_Tools |
|---------|-----------|----------|---------|------------|--------------|---------------|
| TOL-101 | FastAPI + FastMCP | MCP Hosting Framework | Serve MCP over HTTP with session lifecycle | AID | Video_024 | TOL-115 |
| TOL-109 | ScaleKit Dashboard | Auth Platform (UI) | Configure OAuth 2.1 scopes, MCP identifiers | SEC | Video_024 | TOL-118 |
| TOL-118 | ScaleKit Python SDK | Auth SDK | Validate JWTs and interact with ScaleKit API | SEC | Video_024 | TOL-109 |
| TOL-120 | Tavilli Search API | Search Tool | Provide LLM-friendly web search results | AID | Video_024 | TOL-101 |
| TOL-122 | MCP Inspector (VS Code) | Debug Tool | Test MCP connections, auth, and tools | QA | Video_024 | TOL-101 |

## 11. Objects & Deliverables (Reference Only)
- OAuth Metadata Bundle → OBJ-210
- Tavilli MCP Server Config → OBJ-305
- JWT Access Token → OBJ-305
- MCP Auth Middleware Module → OBJ-312
- Authenticated Tool Execution Logs → OBJ-415

---

# TAXONOMY INTEGRATION OUTPUTS

## 12. Entity ID Assignment & Master List
```csv
New_ID,Entity_Type,Name,Description,Department,Source,Status
MLS-001,Milestone,Prepare Baseline MCP Server,Stand up FastMCP Tavilli server locally,AID,Video_024,Pending_Review
MLS-002,Milestone,Configure ScaleKit Authorization Stack,Set up scopes and MCP registration,SEC,Video_024,Pending_Review
MLS-003,Milestone,Implement OAuth Discovery & Middleware,Expose metadata endpoint and enforce JWTs,AID;SEC,Video_024,Pending_Review
MLS-004,Milestone,Test Authenticated MCP Workflow,Validate OAuth login and Tavilli tool runs,AID;QA,Video_024,Pending_Review
TSK-001,Task,Initialize FastMCP service,Scaffold Tavilli MCP server in FastAPI,AID,Video_024,Pending_Review
TSK-002,Task,Mount Tavilli search tool,Wire Tavilli client and config,AID,Video_024,Pending_Review
TSK-003,Task,Verify unauthenticated workflow,Run inspector tests before auth,AID,Video_024,Pending_Review
TSK-004,Task,Activate ScaleKit environments,Enable full-stack auth modules,SEC,Video_024,Pending_Review
TSK-005,Task,Define OAuth scopes,Create search:read permission copy,SEC,Video_024,Pending_Review
TSK-006,Task,Register MCP identifier,Map server URL and enable dynamic registration,SEC,Video_024,Pending_Review
TSK-007,Task,Publish well-known metadata endpoint,Serve ScaleKit JSON from FastAPI,AID;SEC,Video_024,Pending_Review
TSK-008,Task,Build authentication middleware,Intercept requests and emit breadcrumb headers,AID;SEC,Video_024,Pending_Review
TSK-009,Task,Validate bearer tokens with ScaleKit SDK,Check issuer/audience/scope before tool calls,SEC,Video_024,Pending_Review
TSK-010,Task,Simulate client discovery,Follow breadcrumb headers manually,AID,Video_024,Pending_Review
TSK-011,Task,Authenticate via OAuth provider,Complete Google login through ScaleKit,AID,Video_024,Pending_Review
TSK-012,Task,Execute secured Tavilli tool call,Run Tavilli search with enforced scopes,AID;QA,Video_024,Pending_Review
STP-001,Step,Copy metadata JSON from ScaleKit dashboard,Collect OAuth metadata bundle,SEC,Video_024,Pending_Review
STP-002,Step,Load JSON string into FastAPI route,Embed metadata into endpoint,AID,Video_024,Pending_Review
STP-003,Step,Return JSONResponse with headers,Serve metadata to clients,AID,Video_024,Pending_Review
STP-004,Step,Extend BaseHTTPMiddleware,Create custom auth middleware,AID,Video_024,Pending_Review
STP-005,Step,Check request path for well-known routes,Bypass discovery endpoints,AID,Video_024,Pending_Review
STP-006,Step,Raise 401 with WWW-Authenticate header,Provide breadcrumb to metadata,AID,Video_024,Pending_Review
STP-007,Step,Initialize ScaleKit client using env vars,Instantiate SDK with secrets,SEC,Video_024,Pending_Review
STP-008,Step,Assemble validation options,Set issuer/audience/scope,SEC,Video_024,Pending_Review
STP-009,Step,Call validate_token with scope requirements,Verify JWT before tool call,SEC,Video_024,Pending_Review
STP-010,Step,Paste bearer token in MCP inspector auth field,Store JWT in client session,AID,Video_024,Pending_Review
STP-011,Step,Invoke Tavilli search for target query,Execute tool with OAuth context,AID,Video_024,Pending_Review
STP-012,Step,Review results and scope enforcement logs,Confirm successful secured call,QA,Video_024,Pending_Review
```

## 13. Hierarchical Relationship Trees
```
MLS-003 (Implement OAuth Discovery & Middleware)
├── TSK-007 (Publish well-known metadata endpoint)
│   ├── STP-001 (Copy metadata JSON) - ACT-040 → OBJ-210 [TOL-109]
│   ├── STP-002 (Load JSON into FastAPI route) - ACT-015 → OBJ-210 [TOL-101]
│   └── STP-003 (Return JSONResponse with headers) - ACT-050 → OBJ-210 [TOL-101]
├── TSK-008 (Build authentication middleware)
│   ├── STP-004 (Extend BaseHTTPMiddleware) - ACT-110 → OBJ-312 [TOL-115]
│   ├── STP-005 (Check request path for well-known routes) - ACT-025 → OBJ-320
│   └── STP-006 (Raise 401 with WWW-Authenticate header) - ACT-055 → OBJ-321
├── TSK-009 (Validate bearer tokens with ScaleKit SDK)
│   ├── STP-007 (Initialize ScaleKit client) - ACT-030 → OBJ-220 [TOL-118]
│   ├── STP-008 (Assemble validation options) - ACT-045 → OBJ-322
│   └── STP-009 (Call validate_token) - ACT-070 → OBJ-305 [TOL-118]
└── LIBRARIES References:
    ├── SKL-042 (AI Agent Development)
    ├── SKL-078 (Identity & Access Management)
    ├── RSP-333 (Secure MCP Gateway)
    └── PRF-003 / PRF-012

MLS-004 (Test Authenticated MCP Workflow)
├── TSK-010 (Simulate client discovery)
│   └── (Manual sequence via MCP inspector headers)
├── TSK-011 (Authenticate via OAuth provider)
│   └── (External Google login handled by ScaleKit UI)
├── TSK-012 (Execute secured Tavilli tool call)
│   ├── STP-010 (Paste bearer token) - ACT-060 → OBJ-402 [TOL-122]
│   ├── STP-011 (Invoke Tavilli search) - ACT-070 → OBJ-450 [TOL-120]
│   └── STP-012 (Review results and logs) - ACT-040 → OBJ-415 [TOL-122]
└── LIBRARIES References:
    ├── SKL-019 (Testing & Validation)
    ├── RSP-410 (Secure Workflow QA)
    └── PRF-020 (QA Automation)
```

## 14. Department Distribution Analysis
| Department | ISO | MLS | TSK | STP | Total |
|-----------|-----|-----|-----|-----|-------|
| AI & Automations | AID | 2 | 7 | 8 | 17 |
| Security Engineering | SEC | 2 | 5 | 5 | 12 |
| Quality Assurance | QA | 0 | 2 | 2 | 4 |
| **TOTAL** |     | **4** | **14** | **15** | **33** |

## 16. Video Source Metadata & Provenance
```
VIDEO_ID: Video_024
VIDEO_TITLE: Tutorial: Auth for Remote MCP Servers (Step by Step) | OAuth 2.1 with ScaleKit
CHANNEL/CREATOR: Alejandro AO - Software & AI
VIDEO_URL: https://youtu.be/gl6U8s3zStI?si=rXdONo9LW2fe7jWF
PUBLICATION_DATE: 2025-08-25
EXTRACTION_DATE: 2025-11-24
EXTRACTOR_VERSION: v4.1-TASK_MANAGERS

TOTAL_ENTITIES_EXTRACTED: 33

Entity Breakdown:
- Milestones (MLS): 4
- Tasks (TSK): 12
- Steps (STP): 12

PRIMARY_DEPARTMENT: AID (AI & Automations)
SECONDARY_DEPARTMENTS: SEC (Security Engineering), QA (Quality Assurance)

MAIN TOPICS:
- OAuth 2.1 mandates for MCP servers
- ScaleKit account & scope configuration
- FastAPI/FastMCP hosting pattern
- Tavilli search tool security

KEY_WORKFLOWS:
- Secure MCP Auth Deployment (Task Chain)
- OAuth discovery breadcrumb handling

NOTABLE_TOOLS:
- FastAPI + FastMCP (TOL-101)
- ScaleKit Dashboard & SDK (TOL-109, TOL-118)
- Tavilli Search API (TOL-120)
- MCP Inspector (TOL-122)

TAXONOMY_STATUS: Pending_Review
READY_FOR_IMPORT: Yes
VALIDATION_REQUIRED: Yes (new SEC responsibilities and token enforcement steps)
NOTES: Ensure ScaleKit environment secrets remain in secure storage; double-check scope naming if monetizing access tiers.
```


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
