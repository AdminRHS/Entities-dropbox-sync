# API Integration Specification
## Account Management Microservice ↔ ENTITIES Ecosystem

**Document Version:** 1.0
**Created:** 2025-11-18
**Last Updated:** 2025-11-18
**Status:** Draft

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [API Endpoints](#api-endpoints)
4. [Authentication & Authorization](#authentication--authorization)
5. [Request/Response Formats](#requestresponse-formats)
6. [Error Handling](#error-handling)
7. [Rate Limiting](#rate-limiting)
8. [Webhooks & Events](#webhooks--events)
9. [Integration Examples](#integration-examples)
10. [Testing Strategy](#testing-strategy)

---

## Overview

### Purpose
This document specifies the complete API integration between the Account Management PostgreSQL microservice and the ENTITIES JSON-based taxonomy ecosystem.

### Base URLs

**Production:**
- Microservice API: `https://accounts.anyemp.com/api/v1/`
- ENTITIES API: `https://libs.anyemp.com/api/v1/`

**Development:**
- Microservice API: `http://localhost:3000/api/v1/`
- ENTITIES API: `http://localhost:3001/api/v1/`

### API Versioning
- Version format: `/api/v1/`, `/api/v2/`
- Backward compatibility maintained for 12 months
- Deprecation notices sent 6 months in advance

---

## Architecture

### Service Communication Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                         Client Layer                         │
│              (React Frontend, Mobile App, CLI)               │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ├─── GET/POST/PUT/DELETE requests
                       │
          ┌────────────▼────────────────┐
          │   API Gateway (Optional)     │
          │   - Rate limiting            │
          │   - Authentication           │
          │   - Request routing          │
          └────────────┬─────────────────┘
                       │
                       ├─────────────────┐
                       │                 │
        ┌──────────────▼──────────┐   ┌─▼─────────────────────┐
        │  Account Microservice    │   │   ENTITIES API        │
        │  (Node.js + PostgreSQL)  │   │   (JSON Files + API)  │
        │                          │   │                       │
        │  ┌────────────────────┐  │   │  ┌─────────────────┐ │
        │  │ Accounts Service   │  │   │  │ Tools Library   │ │
        │  │ JobAccounts Service│  │   │  │ Employees       │ │
        │  │ Verifications      │◄─┼───┼──│ Statuses        │ │
        │  │ Subscriptions      │  │   │  │ Countries       │ │
        │  │ Payments           │  │   │  │ Currencies      │ │
        │  └────────────────────┘  │   │  └─────────────────┘ │
        │                          │   │                       │
        │  ┌────────────────────┐  │   │  ┌─────────────────┐ │
        │  │ PostgreSQL DB      │  │   │  │ File System     │ │
        │  │ - accounts         │  │   │  │ - LIBRARIES/    │ │
        │  │ - job_accounts     │  │   │  │ - TALENTS/      │ │
        │  │ - verifications    │  │   │  │ - ACCOUNTS/     │ │
        │  │ - subscriptions    │  │   │  │ - BUSINESSES/   │ │
        │  │ - payments         │  │   │  └─────────────────┘ │
        │  └────────────────────┘  │   └───────────────────────┘
        └─────────────────────────┘
                       │
                       ├─── Sync Service
                       │
          ┌────────────▼────────────────┐
          │   Background Jobs            │
          │   - Nightly sync             │
          │   - Expiration alerts        │
          │   - Security audits          │
          │   - Auto-renewals            │
          └──────────────────────────────┘
```

### Data Flow Patterns

**Pattern 1: Create with Validation**
```
Client → POST /api/accounts
  │
  ├─→ Validate against accounts_schema.json
  ├─→ Query ENTITIES API for tool_id validation
  ├─→ Query ENTITIES API for owner_id validation
  ├─→ Insert into PostgreSQL
  ├─→ Trigger sync to ENTITIES JSON
  └─→ Return enriched response
```

**Pattern 2: Read with Enrichment**
```
Client → GET /api/accounts/:id
  │
  ├─→ Query PostgreSQL for account
  ├─→ Query ENTITIES API for tool details
  ├─→ Query ENTITIES API for owner details
  ├─→ Query ENTITIES API for status details
  ├─→ Build relationships object
  └─→ Return enriched response
```

**Pattern 3: Batch Sync (Nightly)**
```
Cron Job (2 AM) → Sync Service
  │
  ├─→ Query PostgreSQL for updated records
  ├─→ For each record:
  │     ├─→ Enrich with ENTITIES data
  │     └─→ Write to ENTITIES JSON files
  └─→ Log sync results to ANALYTICS
```

---

## API Endpoints

### Accounts Endpoints

#### 1. List Accounts

**Endpoint:** `GET /api/accounts`

**Description:** Retrieve a paginated list of accounts with optional filtering

**Query Parameters:**
| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `page` | integer | No | Page number (default: 1) | `1` |
| `limit` | integer | No | Results per page (default: 20, max: 100) | `20` |
| `tool_id` | string | No | Filter by tool | `TOOL-015` |
| `owner_id` | string | No | Filter by owner | `EMP-2025-042` |
| `status_id` | string | No | Filter by status | `active` |
| `department` | string | No | Filter by owner department | `HR` |
| `account_type` | string | No | Filter by account type | `social_media` |
| `can_verify_others` | boolean | No | Filter verification-capable accounts | `true` |
| `search` | string | No | Search in name and login | `linkedin` |
| `sort_by` | string | No | Sort field | `created_at` |
| `sort_order` | string | No | Sort direction (asc/desc) | `desc` |

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "accounts": [
      {
        "account_id": "ACC-001",
        "name": "LinkedIn - HR Recruiter",
        "tool": {
          "tool_id": "TOOL-015",
          "name": "LinkedIn",
          "category": "Social_Media_Tools"
        },
        "owner": {
          "employee_id": "EMP-2025-042",
          "name": "John Smith",
          "department": "HR"
        },
        "status": {
          "status_id": "active",
          "name": "Active"
        },
        "verification_status": "verified",
        "created_at": "2025-01-15T10:00:00Z",
        "last_used_at": "2025-11-17T14:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total_results": 45,
      "total_pages": 3
    }
  },
  "meta": {
    "request_id": "req_abc123",
    "timestamp": "2025-11-18T10:00:00Z"
  }
}
```

---

#### 2. Get Account by ID

**Endpoint:** `GET /api/accounts/:id`

**Description:** Retrieve detailed account information with full relationships

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Account ID (ACC-XXX format or numeric ID) |

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "account_id": "ACC-001",
    "name": "LinkedIn - HR Recruiter",
    "login": "hr@company.com",
    "profile_link": "https://linkedin.com/in/company-hr",
    "account_type": "social_media",
    "can_verify_others": false,
    "usage_count": 145,
    "connections": 500,
    "tool": {
      "tool_id": "TOOL-015",
      "name": "LinkedIn",
      "category": "Social_Media_Tools",
      "api_enabled": true
    },
    "owner": {
      "employee_id": "EMP-2025-042",
      "name": "John Smith",
      "department": "HR",
      "email": "john.smith@company.com"
    },
    "status": {
      "status_id": "active",
      "name": "Active",
      "allows_operations": true
    },
    "country": {
      "country_id": "US",
      "name": "United States",
      "currency": "USD"
    },
    "verification_status": "verified",
    "verification_accounts": [
      {
        "verification_id": "VER-00123",
        "verification_account_id": "ACC-005",
        "verification_account_name": "Gmail - Company Email",
        "verification_method": "email",
        "verified_at": "2025-01-15T11:00:00Z"
      }
    ],
    "assigned_users": [
      {
        "employee_id": "EMP-2025-042",
        "name": "John Smith",
        "role": "owner",
        "permissions": ["read", "write", "manage_users"]
      }
    ],
    "security_metadata": {
      "two_factor_enabled": true,
      "password_last_changed": "2025-08-15",
      "backup_codes_stored": true
    },
    "created_at": "2025-01-15T10:00:00Z",
    "updated_at": "2025-11-15T09:30:00Z",
    "last_used_at": "2025-11-17T14:30:00Z"
  },
  "meta": {
    "request_id": "req_abc124",
    "timestamp": "2025-11-18T10:00:00Z"
  }
}
```

**Error Responses:**
- `404 Not Found` - Account does not exist
- `403 Forbidden` - User lacks permission to view account

---

#### 3. Create Account

**Endpoint:** `POST /api/accounts`

**Description:** Create a new account with validation against ENTITIES schemas

**Request Body:**
```json
{
  "name": "LinkedIn - Senior Recruiter",
  "tool_id": "TOOL-015",
  "login": "recruiter@company.com",
  "password": "SecureP@ssw0rd123!",
  "owner_id": "EMP-2025-055",
  "account_type": "social_media",
  "status_id": "pending_verification",
  "verification_required": true,
  "country_id": "US",
  "metadata": {
    "profile_url": "https://linkedin.com/in/recruiter",
    "industry": "Technology"
  },
  "security_metadata": {
    "two_factor_enabled": true,
    "recovery_email": "backup@company.com"
  }
}
```

**Response:** `201 Created`
```json
{
  "success": true,
  "data": {
    "account_id": "ACC-046",
    "name": "LinkedIn - Senior Recruiter",
    "tool": {...},
    "owner": {...},
    "status": {...},
    "verification_status": "not_verified",
    "created_at": "2025-11-18T10:05:00Z"
  },
  "meta": {
    "request_id": "req_abc125",
    "timestamp": "2025-11-18T10:05:00Z",
    "next_steps": [
      "Account created successfully",
      "Verification required - trigger verification workflow",
      "Account synced to ENTITIES/ACCOUNTS/Accounts/ACC-046.json"
    ]
  }
}
```

**Validation Errors:** `400 Bad Request`
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Account validation failed",
    "details": [
      {
        "field": "owner_id",
        "error": "Employee EMP-2025-999 does not exist in TALENTS/Employees"
      },
      {
        "field": "password",
        "error": "Password does not meet complexity requirements"
      }
    ]
  },
  "meta": {
    "request_id": "req_abc126",
    "timestamp": "2025-11-18T10:06:00Z"
  }
}
```

---

#### 4. Update Account

**Endpoint:** `PUT /api/accounts/:id`

**Description:** Update account information (partial updates supported with PATCH)

**Request Body:**
```json
{
  "name": "LinkedIn - HR Manager (Updated)",
  "status_id": "active",
  "connections": 650,
  "metadata": {
    "premium": true,
    "premium_expires": "2026-01-15"
  }
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "account_id": "ACC-001",
    "updated_fields": ["name", "status_id", "connections", "metadata"],
    "updated_at": "2025-11-18T10:10:00Z"
  }
}
```

---

#### 5. Delete Account

**Endpoint:** `DELETE /api/accounts/:id`

**Description:** Delete or archive account (soft delete by default)

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `hard_delete` | boolean | No | Permanently delete (default: false) |

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "account_id": "ACC-001",
    "action": "archived",
    "archived_at": "2025-11-18T10:15:00Z"
  }
}
```

---

### Verification Endpoints

#### 6. List Verification-Capable Accounts

**Endpoint:** `GET /api/accounts/verifiers`

**Description:** Get accounts that can verify others (can_verify_others=true)

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tool_type` | string | No | Filter by tool (e.g., 'gmail', 'phone') |
| `available` | boolean | No | Only available (status=active) |

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "verification_accounts": [
      {
        "account_id": "ACC-005",
        "name": "Gmail - Company Email",
        "tool_name": "Gmail",
        "can_verify": true,
        "verification_methods": ["email"],
        "verified_accounts_count": 12
      },
      {
        "account_id": "ACC-008",
        "name": "Phone - Operations",
        "tool_name": "Phone",
        "can_verify": true,
        "verification_methods": ["sms", "phone_call"],
        "verified_accounts_count": 8
      }
    ]
  }
}
```

---

#### 7. Create Verification

**Endpoint:** `POST /api/accounts/:id/verifications`

**Description:** Create verification relationship between accounts

**Request Body:**
```json
{
  "verification_account_id": "ACC-005",
  "verification_method": "email"
}
```

**Response:** `201 Created`
```json
{
  "success": true,
  "data": {
    "verification_id": "VER-00789",
    "verifiable_account_id": "ACC-046",
    "verification_account_id": "ACC-005",
    "verification_method": "email",
    "verification_status": "pending",
    "created_at": "2025-11-18T10:20:00Z",
    "next_steps": [
      "Verification code sent to verification account",
      "Enter code to complete verification"
    ]
  }
}
```

---

### Subscription Endpoints

#### 8. List Subscriptions for Verification

**Endpoint:** `GET /api/verifications/:verification_id/subscriptions`

**Description:** Get all subscriptions for a verification relationship

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "subscriptions": [
      {
        "subscription_id": "SUB-00123",
        "plan": {
          "plan_id": "PLAN-005",
          "name": "Monthly Verification",
          "price": 49.99,
          "currency": "USD"
        },
        "status": "active",
        "started_at": "2025-10-18T10:00:00Z",
        "expires_at": "2025-11-18T10:00:00Z",
        "auto_renew": false,
        "renewal_count": 3
      }
    ]
  }
}
```

---

#### 9. Create Subscription

**Endpoint:** `POST /api/verifications/:verification_id/subscriptions`

**Description:** Create a new subscription for verification

**Request Body:**
```json
{
  "plan_id": "PLAN-005",
  "auto_renew": true,
  "payment_method": "card_ending_4242"
}
```

**Response:** `201 Created`
```json
{
  "success": true,
  "data": {
    "subscription_id": "SUB-00456",
    "verification_id": "VER-00789",
    "plan_id": "PLAN-005",
    "status": "active",
    "started_at": "2025-11-18T10:25:00Z",
    "expires_at": "2025-12-18T10:25:00Z",
    "auto_renew": true
  }
}
```

---

#### 10. Get Expiring Subscriptions

**Endpoint:** `GET /api/subscriptions/expiring-soon`

**Description:** Get subscriptions expiring within specified timeframe

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `days` | integer | No | Days ahead to check (default: 30) |
| `department` | string | No | Filter by department |

**Response:** `200 OK`
```json
{
  "success": true,
  "data": {
    "urgent": 3,
    "warning": 5,
    "notice": 8,
    "subscriptions": [...]
  }
}
```

---

## Authentication & Authorization

### Authentication Methods

#### 1. API Key Authentication
```http
GET /api/accounts
Authorization: Bearer {api_key}
```

#### 2. JWT Token Authentication
```http
GET /api/accounts
Authorization: Bearer {jwt_token}
```

#### 3. OAuth 2.0 (for third-party integrations)
```http
GET /api/accounts
Authorization: Bearer {oauth_access_token}
```

### Authorization Levels

| Role | Permissions | Description |
|------|-------------|-------------|
| **Admin** | All operations | Full system access |
| **Manager** | Read, Create, Update | Department-level management |
| **User** | Read, Update (own) | Individual account management |
| **Viewer** | Read only | Read-only access |

### Permission Scopes

```json
{
  "scopes": [
    "account:read",
    "account:write",
    "account:delete",
    "verification:create",
    "subscription:manage",
    "payment:process",
    "audit:view"
  ]
}
```

---

## Request/Response Formats

### Standard Response Format

**Success Response:**
```json
{
  "success": true,
  "data": {...},
  "meta": {
    "request_id": "req_unique_id",
    "timestamp": "ISO 8601 timestamp",
    "version": "1.0"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": []
  },
  "meta": {
    "request_id": "req_unique_id",
    "timestamp": "ISO 8601 timestamp"
  }
}
```

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error, malformed request |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | Resource conflict (e.g., duplicate) |
| 422 | Unprocessable Entity | Validation failed |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 503 | Service Unavailable | Temporary unavailability |

### Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Input validation failed |
| `NOT_FOUND` | Resource not found |
| `PERMISSION_DENIED` | Insufficient permissions |
| `DUPLICATE_RESOURCE` | Resource already exists |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `ENTITIES_API_UNAVAILABLE` | ENTITIES API unreachable |
| `PAYMENT_FAILED` | Payment processing failed |

---

## Rate Limiting

### Limits

| Tier | Requests/minute | Requests/hour |
|------|----------------|---------------|
| Free | 60 | 1,000 |
| Standard | 300 | 10,000 |
| Premium | 1,000 | 50,000 |

### Rate Limit Headers

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 995
X-RateLimit-Reset: 1700305200
```

---

## Webhooks & Events

### Event Types

| Event | Trigger |
|-------|---------|
| `account.created` | New account created |
| `account.updated` | Account information updated |
| `account.deleted` | Account deleted/archived |
| `verification.completed` | Account verification successful |
| `subscription.created` | New subscription created |
| `subscription.renewed` | Subscription renewed |
| `subscription.expiring` | Subscription expiring soon (7 days) |
| `subscription.expired` | Subscription expired |
| `payment.completed` | Payment successful |
| `payment.failed` | Payment failed |

### Webhook Payload Format

```json
{
  "event_id": "evt_abc123",
  "event_type": "account.created",
  "timestamp": "2025-11-18T10:30:00Z",
  "data": {
    "account_id": "ACC-046",
    "name": "LinkedIn - Senior Recruiter",
    "owner_id": "EMP-2025-055"
  }
}
```

---

## Integration Examples

### Example 1: Create Account with Full Workflow

```javascript
// Step 1: Validate with ENTITIES
const toolValidation = await fetch('https://libs.anyemp.com/api/v1/tools/TOOL-015');
const ownerValidation = await fetch('https://libs.anyemp.com/api/v1/employees/EMP-2025-055');

// Step 2: Create account
const accountResponse = await fetch('https://accounts.anyemp.com/api/v1/accounts', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer {api_key}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'LinkedIn - Senior Recruiter',
    tool_id: 'TOOL-015',
    login: 'recruiter@company.com',
    password: 'SecureP@ssw0rd123!',
    owner_id: 'EMP-2025-055',
    account_type: 'social_media',
    status_id: 'pending_verification',
    verification_required: true
  })
});

const account = await accountResponse.json();
console.log('Created:', account.data.account_id);

// Step 3: Create verification
const verificationResponse = await fetch(
  `https://accounts.anyemp.com/api/v1/accounts/${account.data.account_id}/verifications`,
  {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer {api_key}',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      verification_account_id: 'ACC-005',
      verification_method: 'email'
    })
  }
);
```

---

## Testing Strategy

### Test Categories

1. **Unit Tests:** Individual endpoint validation
2. **Integration Tests:** Cross-service communication
3. **E2E Tests:** Full workflow testing
4. **Performance Tests:** Load and stress testing
5. **Security Tests:** Auth and authorization testing

### Test Environment

**Base URL:** `https://accounts-staging.anyemp.com/api/v1/`

### Sample Test Cases

```javascript
describe('Account Management API', () => {
  test('Create account with valid data', async () => {
    const response = await createAccount(validAccountData);
    expect(response.status).toBe(201);
    expect(response.data.account_id).toMatch(/^ACC-\d{3}$/);
  });

  test('Reject account with invalid tool_id', async () => {
    const response = await createAccount({...validAccountData, tool_id: 'INVALID'});
    expect(response.status).toBe(400);
    expect(response.error.code).toBe('VALIDATION_ERROR');
  });
});
```

---

**End of Document**

For implementation questions, contact: dev@company.com
For API access requests: api@company.com
