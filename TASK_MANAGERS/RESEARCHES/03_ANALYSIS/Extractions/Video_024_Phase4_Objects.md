# Video_024 – Phase 4: Objects Extraction  
## Secure MCP OAuth 2.1 Workflow – Deliverables & Tangible Outputs

**Video**: “Tutorial: Auth for Remote MCP Servers (Step by Step) | OAuth 2.1 with ScaleKit”  
**Phase**: 4 (Objects Library Extraction)  
**Date**: 2025-11-24  
**Source**: `Video_024.md` transcription + Phase 3 analysis  

---

## 1. Object Inventory (Top-Level)

| Object ID (proposed) | Name | Type | Category | Description / Notes | Produced In |
|----------------------|------|------|----------|---------------------|-------------|
| OBJ-AUT-401 | MCP Server Baseline Config | Configuration | Platform | FastAPI/FastMCP project with Tavilli tool mounted at `/mcp`, port `10000`. | MLS-001 / TSK-001–003 |
| OBJ-AUT-402 | Tavilli API Credential File | Secret / Config | Data | API key + config used by Tavilli search tool. | TSK-002 |
| OBJ-SEC-510 | OAuth Metadata JSON (`.well-known`) | Specification | Security | JSON payload returned from ScaleKit to guide clients (issuer, token endpoint, scopes). | TSK-007 |
| OBJ-SEC-511 | Resource Metadata Header (`WWW-Authenticate`) | Header Spec | Security | HTTP header instructing MCP clients where to fetch metadata. | TSK-008 |
| OBJ-SEC-512 | Auth Middleware Module | Code Module | Security | Custom BaseHTTPMiddleware enforcing bearer token requirements. | TSK-008 |
| OBJ-SEC-513 | Token Validation Log | Log Entry | Security | Validation results (issuer/audience/scope) per request. | TSK-009 |
| OBJ-SEC-514 | ScaleKit IAM Scope Definition (`search:read`) | Policy | Security | Human-readable scope message configured in ScaleKit dashboard. | TSK-005 |
| OBJ-SEC-515 | ScaleKit MCP Registration Record | Record | Security | Identifier + trailing slash mapping for MCP server. | TSK-006 |
| OBJ-SEC-516 | Environment Secrets (.env) | Secret Store | Security | Client ID, client secret, env URL for ScaleKit SDK. | TSK-009 |
| OBJ-QA-220 | OAuth Breadcrumb Trace | Diagnostic Artifact | QA | Step-by-step trace showing 401 → metadata → token retrieval. | TSK-010 |
| OBJ-QA-221 | Authenticated Tavilli Session | Session | QA | Tokenized MCP inspector session connected to Tavilli tool. | TSK-012 |
| OBJ-QA-222 | Tavilli Search Result Packet | Data Output | QA | JSON response for “Sam Altman latest news” under authenticated call. | TSK-012 |

---

## 2. Object Categorization & Attributes

### 2.1 Security / IAM Objects
- **OAuth Metadata JSON (OBJ-SEC-510)**  
  - Fields: issuer, authorization_endpoint, token_endpoint, introspection_endpoint, revocation_endpoint, scopes_supported.  
  - Stored within FastAPI route at `/.well-known/oauth-protected-resource/mcp`.
- **Resource Metadata Header (OBJ-SEC-511)**  
  - Format: `WWW-Authenticate: Bearer realm="oauth", authorization_uri="…" , resourceMetadata="…"`.  
  - Emitted on every unauthorized request.
- **Auth Middleware Module (OBJ-SEC-512)**  
  - Components: Starlette BaseHTTPMiddleware subclass, request path filter, bearer extraction, exception handling.  
  - References ScaleKit client + validation options.
- **Token Validation Log (OBJ-SEC-513)**  
  - Entries: request timestamp, issuer, audience, scopes, decision (allow/deny).  
  - Stored in server logs for audit.
- **ScaleKit IAM Scope Definition (OBJ-SEC-514)**  
  - Scope Key: `search:read`.  
  - Description: “Use Tavilli to search the web.”  
  - Visible on consent screen.
- **ScaleKit MCP Registration Record (OBJ-SEC-515)**  
  - Includes MCP identifier (https://localhost:10000/mcp/), trailing slash requirement, dynamic registration flag.  
  - Maintained inside ScaleKit dashboard.
- **Environment Secrets (.env) (OBJ-SEC-516)**  
  - Keys: `SCALEKIT_CLIENT_ID`, `SCALEKIT_CLIENT_SECRET`, `SCALEKIT_ENV_URL`, `SCALEKIT_RESOURCE_METADATA_URL`.  
  - Lives in server `.env` with secure storage.

### 2.2 Platform / Configuration Objects
- **MCP Server Baseline Config (OBJ-AUT-401)**  
  - Files: `main.py`, FastMCP session manager wiring, CORS middleware.  
  - Defines port 10000, root mount `/mcp`.
- **Tavilli API Credential File (OBJ-AUT-402)**  
  - Typically `.toml` or `.env` entry storing Tavilli key + query parameters.  
  - Used by `web_search` tool.

### 2.3 QA / Diagnostic Objects
- **OAuth Breadcrumb Trace (OBJ-QA-220)**  
  - Sequence: unauthorized tool call → metadata header → metadata JSON → OAuth discovery doc → token request.  
  - Captured manually in MCP Inspector demonstration.
- **Authenticated Tavilli Session (OBJ-QA-221)**  
  - VS Code / MCP Inspector session containing pasted JWT.  
  - Valid until token expiry.
- **Tavilli Search Result Packet (OBJ-QA-222)**  
  - Data structure: query string, results list, metadata.  
  - Confirms tool runs only after successful auth.

---

## 3. Action → Object Relationships

| Action (ACT-###) | Description | Object(s) Produced |
|------------------|-------------|--------------------|
| ACT-015 (Create) | Build FastAPI/ScaleKit routes | OBJ-AUT-401, OBJ-SEC-510 |
| ACT-025 (Inspect) | Check request paths / scopes | OBJ-SEC-513 |
| ACT-030 (Configure) | Initialize ScaleKit client | OBJ-SEC-516 |
| ACT-040 (Verify) | Copy metadata, review logs | OBJ-SEC-510, OBJ-QA-220 |
| ACT-050 (Export) | Return JSON response | OBJ-SEC-510 |
| ACT-055 (Map) | Set headers, map scopes | OBJ-SEC-511, OBJ-SEC-514 |
| ACT-060 (Input) | Paste JWT in inspector | OBJ-QA-221 |
| ACT-070 (Execute) | Run `validate_token`, run Tavilli search | OBJ-SEC-513, OBJ-QA-222 |
| ACT-110 (Extend) | Build middleware subclass | OBJ-SEC-512 |

---

## 4. Tool ↔ Object ↔ Responsibility Matrix

| Tool | Objects Produced / Managed | Responsibilities (RSP) |
|------|---------------------------|-------------------------|
| FastAPI + FastMCP (TOL-101) | OBJ-AUT-401, OBJ-SEC-510 | RSP-201 MCP Setup |
| ScaleKit Dashboard (TOL-109) | OBJ-SEC-514, OBJ-SEC-515 | RSP-315 OAuth Policy Config |
| ScaleKit Python SDK (TOL-118) | OBJ-SEC-512, OBJ-SEC-513, OBJ-SEC-516 | RSP-333 Secure MCP Gateway |
| Tavilli Search API (TOL-120) | OBJ-AUT-402, OBJ-QA-222 | RSP-205 AI Research Ops |
| MCP Inspector (TOL-122) | OBJ-QA-220, OBJ-QA-221 | RSP-410 Secure Workflow QA |

---

## 5. Object Lifecycle Highlights

1. **Configuration Stage (MLS-001)**  
   - Create MCP server baseline (OBJ-AUT-401).  
   - Store Tavilli credentials (OBJ-AUT-402).
2. **ScaleKit Setup (MLS-002)**  
   - Define scopes/policies (OBJ-SEC-514).  
   - Register MCP + metadata (OBJ-SEC-515, OBJ-SEC-510).
3. **Middleware Enforcement (MLS-003)**  
   - Build header + middleware artifacts (OBJ-SEC-511, OBJ-SEC-512).  
   - Manage secrets + validation logs (OBJ-SEC-516, OBJ-SEC-513).
4. **Testing & QA (MLS-004)**  
   - Generate breadcrumb trace (OBJ-QA-220).  
   - Maintain authenticated session (OBJ-QA-221) and final Tavilli output (OBJ-QA-222).

---

## 6. Gaps / Next Actions

- **Object IDs**: need confirmation against `LIBRARIES/Responsibilities/Objects` registry before finalizing (OBJ-SEC series may require new entries).  
- **Secret Handling**: highlight requirement for secure storage (e.g., Vault) when integrating into production systems.  
- **Logging Strategy**: consider structured logging for OBJ-SEC-513 to enable compliance.  
- **Session Token Lifecycles**: document expiry/refresh logic for OBJ-QA-221 if building automated QA.

---

**Prepared by**: GPT-5.1 Codex (Cursor Agent)  
**Status**: Phase 4 complete – ready for Phase 5 Gap Analysis.  
**Date**: 2025-11-24

