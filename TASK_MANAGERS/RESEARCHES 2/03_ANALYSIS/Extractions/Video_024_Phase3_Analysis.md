# Video_024 – Phase 3: Initial Analysis  
## “Tutorial: Auth for Remote MCP Servers (Step by Step) | OAuth 2.1 with ScaleKit”

**Analysis Date**: 2025-11-24  
**Phase**: 3 (Initial Analysis – Tools & Workflows Extraction)  
**Source**: `Video_024.md` transcription  
**Video URL**: https://youtu.be/gl6U8s3zStI?si=rXdONo9LW2fe7jWF  

---

## Executive Summary

The video demonstrates how to secure a remote MCP (Model Context Protocol) server with OAuth 2.1 using **ScaleKit**, **FastAPI/FastMCP**, and a Tavilli-powered search tool. The walkthrough shows the entire breadcrumb-based discovery workflow, from exposing the `.well-known` endpoint to validating JWTs and testing the authenticated tool chain inside VS Code / MCP Inspector.

**Key Findings**
- **5 primary tools / platforms** highlighted (FastAPI+FastMCP, ScaleKit Dashboard, ScaleKit Python SDK, Tavilli Search API, MCP Inspector).
- **1 end-to-end workflow** with 4 milestones, 12 tasks, and 12 detailed steps (already mapped in `Video_024.md`, replicated here for analysis context).
- **Action verbs** emphasize secure hosting, IAM configuration, middleware enforcement, and QA validation.
- **Primary departments**: AID (AI & Automations) + SEC (Security Engineering) with QA support.

---

## 1. Tools Extraction

### 1.1 FastAPI + FastMCP (Hosting Stack)
- **Vendor**: Open-source (FastAPI by Sebastián Ramírez, FastMCP by Cursor/Anthropic community)
- **Category**: MCP Hosting Framework / API Framework
- **Purpose**: Host MCP servers over HTTP transport with session lifecycle management.
- **Key Features in video**:
  - FastAPI lifespan integration with FastMCP session manager.
  - Mounting MCP server at `/mcp` on port `10000`.
  - Middleware support (CORS + custom auth).
- **Usage**:
  - Baseline server setup (timestamps [02:12]–[04:39]).
  - Running UV command `uv run my-mcp-server`.
- **Departments**: AID primarily; SEC for middleware enforcement.
- **Proposed Tool ID**: `TOL-AID-201`.
- **File Target**: `LIBRARIES/LBS_003_Tools/Automation/FastAPI_FastMCP.json`.

### 1.2 ScaleKit Dashboard
- **Vendor**: ScaleKit
- **Category**: Auth Platform (UI)
- **Purpose**: Manage OAuth 2.1 scopes, permissions, and MCP server registrations.
- **Key Features**:
  - Development + production environments.
  - MCP-specific configuration area.
  - Scope definition (e.g., `search:read`).
  - MCP server identifier & dynamic client registration.
  - `.well-known` metadata generator.
- **Usage**: Timestamps [15:56]–[19:50].
- **Departments**: SEC (IAM) with AID overlap.
- **Proposed Tool ID**: `TOL-SEC-124`.
- **File Target**: `LIBRARIES/LBS_003_Tools/Auth/ScaleKit_Dashboard.json`.

### 1.3 ScaleKit Python SDK
- **Vendor**: ScaleKit
- **Category**: Auth SDK / Python Client
- **Purpose**: Validate tokens (issuer, audience, scopes) and interact with ScaleKit API.
- **Key Features**:
  - `validate_token` helper.
  - Environment URL, client ID, client secret integration.
  - Works with FastAPI middleware.
- **Usage**: Timestamps [22:20]–[33:45].
- **Departments**: SEC, AID.
- **Proposed Tool ID**: `TOL-SEC-125`.
- **File Target**: `LIBRARIES/LBS_003_Tools/Auth/ScaleKit_SDK.json`.

### 1.4 Tavilli Search API
- **Vendor**: Tavilli
- **Category**: AI Search Tool
- **Purpose**: Provide LLM-friendly web search results; acts as MCP tool being protected.
- **Usage**:
  - Tool definition inside FastMCP server ([02:48]–[04:39]).
  - Authenticated call for “Sam Altman latest news” ([36:50]–[37:18]).
- **Departments**: AID (AI Agents), LGN (lead intelligence), OPS (operations intel).
- **Proposed Tool ID**: `TOL-AID-205`.
- **File Target**: `LIBRARIES/LBS_003_Tools/AI_Search/Tavilli.json`.

### 1.5 MCP Inspector / VS Code MCP Client
- **Vendor**: VS Code extensions ecosystem (Cursor / Anthropic)
- **Category**: Debug Tool / Client
- **Purpose**: Test MCP endpoints, follow OAuth breadcrumbs, paste tokens, run tool calls.
- **Usage**:
  - Simulating unauthorized call, capturing 401 metadata ([11:06]–[15:00]).
  - Final QA test with Tavilli search ([35:44]–[37:18]).
- **Departments**: QA, AID.
- **Proposed Tool ID**: `TOL-QA-031`.
- **File Target**: `LIBRARIES/LBS_003_Tools/QA/MCP_Inspector.json`.

Additional supporting platforms (not captured as standalone tools but referenced):
- **Google OAuth / Google Login** – identity provider leveraged through ScaleKit.
- **VS Code** – IDE environment.
- **Chrome Browser** – used implicitly for login + ScaleKit UI.

---

## 2. Workflow Extraction

### Workflow: Secure MCP OAuth 2.1 Implementation
- **Workflow ID (proposed)**: `WRF-SEC-014`
- **Objective**: Protect a remote MCP server using OAuth 2.1 standard, ensuring only authenticated clients can execute tools.
- **Input**: Running FastMCP server, Tavilli tool, ScaleKit account.
- **Output**: Authenticated MCP workflow with validated JWT and successful tool execution.
- **Duration**: ~60–90 minutes (setup + testing).
- **Complexity**: Medium-High (IAM + backend integration).
- **Departments**: SEC + AID (primary), QA (validation).
- **Business Value**:
  - Enables secure monetization or scope-based control of MCP tools.
  - Aligns with MCP spec requirement for OAuth 2.1 on HTTP transport.
  - Reduces risk of unauthorized access to remote tools.
- **Timestamps**: Entire video [00:00]–[38:53].

#### Milestones Recap (mapped to video-specific MLS IDs)
1. **MLS-001 – Prepare Baseline MCP Server**  
   - Tasks: initialize FastMCP service, mount Tavilli tool, verify unauth workflow.  
   - Tools: FastAPI/FastMCP, Tavilli.  
2. **MLS-002 – Configure ScaleKit Authorization Stack**  
   - Tasks: activate environments, define scopes, register MCP identifier.  
   - Tools: ScaleKit Dashboard.  
3. **MLS-003 – Implement OAuth Discovery & Middleware**  
   - Tasks: publish well-known endpoint, build middleware, validate JWTs.  
   - Tools: FastAPI, ScaleKit SDK.  
4. **MLS-004 – Test Authenticated MCP Workflow**  
   - Tasks: simulate client discovery, authenticate via Google, execute Tavilli tool.  
   - Tools: MCP Inspector, Tavilli.

These milestones already align with the taxonomy entries authored inside `Video_024.md` (Milestones/Tasks/Steps) and will flow into Phase 4–7 outputs.

---

## 3. Action Verbs & Operations (Phase 3 Snapshot)

| Category | Representative Verbs (from video) |
|----------|-----------------------------------|
| **A – Creation** | initialize, configure, publish, build, register |
| **B – Modification** | update, append, mount, enable, restart |
| **C – Analysis** | inspect, verify, validate, review |
| **D – Organization** | define, map, assign, sequence, document |
| **E – Communication** | explain, authorize, notify, demonstrate |
| **F – Browser/Agentic** | authenticate, redirect, connect, follow, log in, request, respond |
| **G – Data** | issue JWT, validate token, parse request, store credentials, execute tool |

Total unique verbs captured during Phase 3: **34** (rolled into the master action inventory in `Video_024.md`).

---

## 4. Integration Opportunities & Notes

- **Tool Library Updates**:  
  - Add/expand entries for FastAPI+FastMCP, ScaleKit Dashboard, ScaleKit SDK, Tavilli, MCP Inspector (if not already in `LBS_003_Tools`).  
  - Cross-link to relevant responsibilities (RSP-333 Secure MCP Gateway, RSP-410 Secure Workflow QA).

- **Workflow Library**:  
  - Create `WRF-SEC-014_Secure_MCP_OAuth_Workflow.json` referencing MLS/TSK/STP extracted here.  
  - Highlight dependencies on ScaleKit + FastAPI.

- **Responsibilities / Skills**:  
  - Ensure IAM-related skills (SKL-078) and Secure Gateway responsibilities exist / updated with OAuth 2.1 details.  
  - Potential new responsibility: “RSP-418 ScaleKit IAM Administration.”

- **Master Lists**:  
  - Update `VIDEOS_INDEX.md` Phase tracker (Phase 1 complete; Phase 3 in progress).  
  - After Phase 4–7, propagate IDs into taxonomy registries.

---

## 5. Next Steps (toward Phases 4–7)

1. **Phase 4 – Objects Extraction** (`PMT-007`):  
   - Document deliverables such as OAuth metadata bundle, auth middleware module, JWT access logs, Tavilli auth session, etc.

2. **Phase 5 – Gap Analysis** (`PMT-009 Part 1`):  
   - Check if ScaleKit tools exist in libraries. Identify missing responsibilities/skills for IAM & secure MCP hosting.

3. **Phase 6 – Integration** (`PMT-009 Part 2`):  
   - Add new JSON entities (Tools, Workflows, Milestones, Tasks, Steps) and update cross-references.

4. **Phase 7 – Library Mapping Report** (`PMT-009 Part 3`):  
   - Summarize the secure-auth workflow, coverage metrics, and readiness for deployment.

---

**Prepared by**: GPT-5.1 Codex (Cursor Agent)  
**Date**: 2025-11-24  
**Status**: Phase 3 complete – ready to proceed to Phase 4.

