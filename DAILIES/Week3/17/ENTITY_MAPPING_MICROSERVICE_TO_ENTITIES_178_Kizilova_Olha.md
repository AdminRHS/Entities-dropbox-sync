# Entity Mapping: Account Management Microservice ↔ ENTITIES Ecosystem

**Document Version:** 1.0
**Created:** 2025-11-18
**Purpose:** Define the complete mapping between PostgreSQL microservice tables and ENTITIES JSON structures

---

## Table of Contents

1. [Overview](#overview)
2. [Core Entity Mappings](#core-entity-mappings)
3. [Foreign Key Bridge Specifications](#foreign-key-bridge-specifications)
4. [Data Flow Diagrams](#data-flow-diagrams)
5. [API Integration Points](#api-integration-points)
6. [Sync Strategy](#sync-strategy)

---

## Overview

The Account Management Microservice uses **PostgreSQL as the source of truth** for transactional data, while the **ENTITIES ecosystem provides taxonomic structure** and cross-entity relationships.

### Architecture Pattern

```
PostgreSQL (Microservice)          ENTITIES (Taxonomy)
       ↓                                  ↓
Source of Truth                  Reference Data
Transactional Data               Structural Definitions
Real-time Operations             Templates & Workflows
```

### Integration Strategy

- **Write Operations:** Always write to PostgreSQL first
- **Read Operations:** Query PostgreSQL, enrich with ENTITIES data
- **Sync Operations:** Daily batch sync from PostgreSQL → ENTITIES JSON files
- **Validation:** Validate against ENTITIES schemas before write

---

## Core Entity Mappings

### 1. Accounts Table → ENTITIES/ACCOUNTS/Accounts/

#### PostgreSQL Schema (accounts table)

```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tool_id INTEGER NOT NULL,
    login VARCHAR(255) NOT NULL,
    profile_link TEXT,
    password TEXT,
    can_verify_others BOOLEAN DEFAULT false,
    status_id INTEGER NOT NULL,
    owner_id VARCHAR(64),
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0,
    connections INTEGER,
    country_id INTEGER,
    is_approved_manager BOOLEAN DEFAULT false,
    created_date DATE
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/accounts_schema.json`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `account_id` | INT → String | Transform: `ACC-{id:03d}` |
| `name` | `name` | VARCHAR → String | Direct mapping |
| `tool_id` | `tool_id` | INT → String | **Bridge to LIBRARIES/Tools** |
| `login` | `login` | VARCHAR → String | Encrypted |
| `profile_link` | `profile_link` | TEXT → String | Direct mapping |
| `password` | `password` | TEXT → String | Encrypted (never sync to JSON) |
| `can_verify_others` | `can_verify_others` | BOOLEAN → Boolean | Direct mapping |
| `status_id` | `status_id` | INT → String | **Bridge to LIBRARIES/Statuses** |
| `owner_id` | `owner_id` | VARCHAR(64) → String | **Bridge to TALENTS/Employees** |
| `metadata` | `usage_metadata.custom_metadata` | JSONB → Object | Direct mapping |
| `notes` | `note` | TEXT → String | Direct mapping |
| `created_at` | `created_at` (internal) | TIMESTAMP → DateTime | PostgreSQL only |
| `updated_at` | `last_updated` | TIMESTAMP → Date | Convert to date |
| `last_used_at` | `last_used_at` | TIMESTAMP → DateTime | Direct mapping |
| `usage_count` | `usage_count` | INT → Integer | Direct mapping |
| `connections` | `connections` | INT → Integer | Direct mapping |
| `country_id` | `country_id` | INT → String | **Bridge to LIBRARIES/Countries** |
| `is_approved_manager` | `is_approved_manager` | BOOLEAN → Boolean | Direct mapping |
| `created_date` | `created_date` | DATE → Date | Direct mapping |

#### Additional ENTITIES Fields (not in PostgreSQL)

| ENTITIES Field | Source | Notes |
|----------------|--------|-------|
| `entity_type` | Constant | Always "ACCOUNTS" |
| `sub_entity` | Constant | Always "Account" |
| `entity_id` | Derived | Business entity reference |
| `account_type` | Derived from `tool_id` | Mapped from tool category |
| `verification_status` | Calculated | Based on verifications table |
| `relationships` | Enriched | Populated from related tables |

---

### 2. Job Accounts Table → ENTITIES/ACCOUNTS/JobSites/

#### PostgreSQL Schema (job_accounts table)

```sql
CREATE TABLE job_accounts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    job_site_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    login VARCHAR(255) NOT NULL,
    password TEXT NOT NULL,
    profile_link TEXT,
    status_id INTEGER NOT NULL,
    owner_id VARCHAR(64),
    available_job_posts INTEGER DEFAULT 0,
    active_job_posts INTEGER DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP,
    usage_count INTEGER DEFAULT 0
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/job_accounts_schema.json`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `job_account_id` | INT → String | Transform: `JOB-ACC-{id:03d}` |
| `name` | `name` | VARCHAR → String | Direct mapping |
| `job_site_id` | `job_site_id` | INT → String | **Bridge to ACCOUNTS/Accounts** (transform: `ACC-{id:03d}`) |
| `login` | `login` | VARCHAR → String | Encrypted |
| `password` | `password` | TEXT → String | Encrypted (never sync to JSON) |
| `profile_link` | `profile_link` | TEXT → String | Direct mapping |
| `status_id` | `status_id` | INT → String | **Bridge to LIBRARIES/Statuses** |
| `owner_id` | `owner_id` | VARCHAR(64) → String | **Bridge to TALENTS/Employees** |
| `available_job_posts` | `available_job_posts` | INT → Integer | Direct mapping |
| `active_job_posts` | `active_job_posts` | INT → Integer | Direct mapping |
| `metadata` | `metadata` | JSONB → Object | Direct mapping |
| `notes` | `notes` | TEXT → String | Direct mapping |
| `created_at` | `created_at` | TIMESTAMP → DateTime | Direct mapping |
| `updated_at` | `updated_at` | TIMESTAMP → DateTime | Direct mapping |
| `last_used_at` | `last_used_at` | TIMESTAMP → DateTime | Direct mapping |
| `usage_count` | `usage_count` | INT → Integer | Direct mapping |

---

### 3. Verifications Table → ENTITIES/ACCOUNTS/Verifications/

#### PostgreSQL Schema (verifications table)

```sql
CREATE TABLE verifications (
    id SERIAL PRIMARY KEY,
    verifiable_type VARCHAR(50) NOT NULL CHECK (verifiable_type IN ('account', 'job_account')),
    verifiable_id INTEGER NOT NULL,
    verification_account_id INTEGER NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/verification_subscription_schema.json#/definitions/verification`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `verification_id` | INT → String | Transform: `VER-{id:05d}` |
| `verifiable_type` | `verifiable_type` | VARCHAR → String | Direct mapping ('account' or 'job_account') |
| `verifiable_id` | `verifiable_id` | INT → String | Transform based on type: `ACC-XXX` or `JOB-ACC-XXX` |
| `verification_account_id` | `verification_account_id` | INT → String | Transform: `ACC-{id:03d}` |
| `created_at` | `created_at` | TIMESTAMP → DateTime | Direct mapping |

---

### 4. Plans Table → ENTITIES/BUSINESSES/Products/

#### PostgreSQL Schema (plans table)

```sql
CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    currency_id INTEGER NOT NULL,
    duration_days INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/verification_subscription_schema.json#/definitions/plan`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `plan_id` | INT → String | Transform: `PLAN-{id:03d}` |
| `name` | `name` | VARCHAR → String | Direct mapping |
| `description` | `description` | TEXT → String | Direct mapping |
| `price` | `price` | DECIMAL → Number | Direct mapping |
| `currency_id` | `currency_id` | INT → String | **Bridge to LIBRARIES/Currencies** |
| `duration_days` | `duration_days` | INT → Integer | Direct mapping |
| `is_active` | `is_active` | BOOLEAN → Boolean | Direct mapping |
| `created_at` | `created_at` | TIMESTAMP → DateTime | Direct mapping |
| `updated_at` | `updated_at` | TIMESTAMP → DateTime | Direct mapping |

---

### 5. Verification Subscriptions Table → ENTITIES/ACCOUNTS/Subscriptions/

#### PostgreSQL Schema (verification_subscriptions table)

```sql
CREATE TABLE verification_subscriptions (
    id SERIAL PRIMARY KEY,
    verification_id INTEGER NOT NULL REFERENCES verifications(id) ON DELETE CASCADE,
    plan_id INTEGER REFERENCES plans(id) ON DELETE SET NULL,
    status_id INTEGER NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    cancelled_at TIMESTAMP,
    auto_renew BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/verification_subscription_schema.json#/definitions/verification_subscription`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `subscription_id` | INT → String | Transform: `SUB-{id:05d}` |
| `verification_id` | `verification_id` | INT → String | Transform: `VER-{id:05d}` |
| `plan_id` | `plan_id` | INT → String | Transform: `PLAN-{id:03d}` (nullable) |
| `status_id` | `status_id` | INT → String | **Bridge to LIBRARIES/Statuses** |
| `started_at` | `started_at` | TIMESTAMP → DateTime | Direct mapping |
| `expires_at` | `expires_at` | TIMESTAMP → DateTime | Direct mapping (nullable) |
| `cancelled_at` | `cancelled_at` | TIMESTAMP → DateTime | Direct mapping (nullable) |
| `auto_renew` | `auto_renew` | BOOLEAN → Boolean | Direct mapping |
| `created_at` | `created_at` | TIMESTAMP → DateTime | Direct mapping |
| `updated_at` | `updated_at` | TIMESTAMP → DateTime | Direct mapping |

---

### 6. Payments Table → ENTITIES/ANALYTICS/Payments/

#### PostgreSQL Schema (verification_subscription_payments table)

```sql
CREATE TABLE verification_subscription_payments (
    id SERIAL PRIMARY KEY,
    subscription_id INTEGER NOT NULL REFERENCES verification_subscriptions(id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    transaction_id VARCHAR(255),
    invoice_number VARCHAR(255),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### ENTITIES JSON Schema

**File:** `ENTITIES/ACCOUNTS/verification_subscription_schema.json#/definitions/subscription_payment`

**Mapping:**

| PostgreSQL Field | ENTITIES Field | Type | Notes |
|------------------|----------------|------|-------|
| `id` | `payment_id` | INT → String | Transform: `PAY-{id:06d}` |
| `subscription_id` | `subscription_id` | INT → String | Transform: `SUB-{id:05d}` |
| `amount` | `amount` | DECIMAL → Number | Direct mapping |
| `currency` | `currency` | VARCHAR → String | Direct mapping (validate against LIBRARIES/Currencies) |
| `payment_date` | `payment_date` | TIMESTAMP → DateTime | Direct mapping |
| `payment_method` | `payment_method` | VARCHAR → String | Direct mapping |
| `payment_status` | `payment_status` | VARCHAR → String | **Validate against LIBRARIES/Statuses** |
| `transaction_id` | `transaction_id` | VARCHAR → String | Direct mapping |
| `invoice_number` | `invoice_number` | VARCHAR → String | Direct mapping |
| `notes` | `notes` | TEXT → String | Direct mapping |
| `created_at` | `created_at` | TIMESTAMP → DateTime | Direct mapping |

---

## Foreign Key Bridge Specifications

### Bridge 1: tool_id → LIBRARIES/Tools

**PostgreSQL:** `accounts.tool_id` (INTEGER)
**ENTITIES:** `LIBRARIES/Tools/{tool_category}/{tool_name}.json`

**Lookup Process:**
1. Query `LIBRARIES/Tools/` to find tool by numeric ID
2. Retrieve tool details: name, category, api_enabled, etc.
3. Populate `relationships.tool` object in account JSON

**Example:**
```json
// PostgreSQL: accounts.tool_id = 15
// ENTITIES Lookup:
{
  "tool_id": "TOOL-015",
  "tool_name": "LinkedIn",
  "tool_category": "Social_Media_Tools",
  "api_enabled": true
}
```

---

### Bridge 2: owner_id → TALENTS/Employees

**PostgreSQL:** `accounts.owner_id` (VARCHAR(64))
**ENTITIES:** `TALENTS/Employees/{employee_id}.json`

**Format:** `EMP-YYYY-XXX` (e.g., `EMP-2025-001`)

**Lookup Process:**
1. Parse employee_id from PostgreSQL owner_id
2. Query `TALENTS/Employees/EMP-{year}-{num}.json`
3. Retrieve employee details: name, department, active status
4. Populate `relationships.owner` object in account JSON

**Example:**
```json
// PostgreSQL: accounts.owner_id = "EMP-2025-042"
// ENTITIES Lookup:
{
  "employee_id": "EMP-2025-042",
  "name": "John Smith",
  "department": "HR",
  "is_active": true
}
```

---

### Bridge 3: status_id → LIBRARIES/Statuses

**PostgreSQL:** `accounts.status_id` (INTEGER or VARCHAR depending on implementation)
**ENTITIES:** `LIBRARIES/Statuses/statuses.json`

**Mapping Table:**

| PostgreSQL status_id | ENTITIES status_id | Name |
|----------------------|-------------------|------|
| 1 or "active" | "active" | Active |
| 2 or "inactive" | "inactive" | Inactive |
| 3 or "suspended" | "suspended" | Suspended |
| 4 or "pending_verification" | "pending_verification" | Pending Verification |
| 5 or "expired" | "expired" | Expired |
| 6 or "archived" | "archived" | Archived |

**Recommendation:** Use VARCHAR in PostgreSQL matching ENTITIES status_id strings for consistency.

---

### Bridge 4: country_id → LIBRARIES/Countries

**PostgreSQL:** `accounts.country_id` (INTEGER or VARCHAR)
**ENTITIES:** `LIBRARIES/Countries/countries.json`

**Mapping:** Use ISO 2-letter country codes

**Recommendation:**
```sql
-- Store as VARCHAR(2) in PostgreSQL using ISO codes
ALTER TABLE accounts ALTER COLUMN country_id TYPE VARCHAR(2);

-- Example values: 'US', 'CA', 'GB', 'DE', 'UA'
```

**Lookup Process:**
1. Query `LIBRARIES/Countries/countries.json`
2. Find country by country_id (ISO 2 code)
3. Retrieve full details: name, currency, phone_code, region

---

### Bridge 5: currency_id → LIBRARIES/Currencies

**PostgreSQL:** `plans.currency_id` (INTEGER or VARCHAR)
**ENTITIES:** `LIBRARIES/Currencies/currencies.json`

**Mapping:** Use ISO 3-letter currency codes

**Recommendation:**
```sql
-- Store as VARCHAR(3) in PostgreSQL using ISO codes
ALTER TABLE plans ALTER COLUMN currency_id TYPE VARCHAR(3);

-- Example values: 'USD', 'EUR', 'GBP', 'CAD'
```

---

## Data Flow Diagrams

### Workflow 1: Create New Account

```
User Input (API Request)
    ↓
Validate against ENTITIES/ACCOUNTS/accounts_schema.json
    ↓
Validate tool_id exists in LIBRARIES/Tools
    ↓
Validate owner_id exists in TALENTS/Employees
    ↓
Validate status_id exists in LIBRARIES/Statuses
    ↓
INSERT INTO PostgreSQL accounts table
    ↓
Generate account_id: ACC-{id:03d}
    ↓
[Optional] Sync to ENTITIES/ACCOUNTS/Accounts/ACC-XXX.json
    ↓
Return enriched response with relationships
```

### Workflow 2: Retrieve Account with Relationships

```
API Request: GET /api/accounts/ACC-001
    ↓
Parse account_id → PostgreSQL id (001 → 1)
    ↓
SELECT FROM accounts WHERE id = 1
    ↓
Enrich with ENTITIES data:
  - tool_id → LIBRARIES/Tools (get tool details)
  - owner_id → TALENTS/Employees (get employee details)
  - status_id → LIBRARIES/Statuses (get status details)
  - country_id → LIBRARIES/Countries (get country details)
    ↓
Query verifications table (get verification accounts)
    ↓
Query user_assignments table (get assigned users)
    ↓
Build relationships object
    ↓
Return enriched JSON response
```

### Workflow 3: Daily Sync PostgreSQL → ENTITIES

```
Cron Job (Daily at 2 AM)
    ↓
SELECT * FROM accounts WHERE updated_at >= yesterday
    ↓
For each account:
  - Transform id → ACC-{id:03d}
  - Enrich with ENTITIES lookups
  - Build relationships
  - Generate JSON file
    ↓
Write to ENTITIES/ACCOUNTS/Accounts/ACC-XXX.json
    ↓
Update sync log in ANALYTICS/Sync_Logs/
    ↓
Send notification if errors
```

---

## API Integration Points

### Microservice API Endpoints

**Base URL:** `https://accounts.anyemp.com/api/v1/`

#### Accounts Endpoints

```
GET    /accounts
       Query params: tool_id, owner_id, status_id, country_id, department
       Returns: Array of enriched account objects

POST   /accounts
       Body: Account data (validated against ENTITIES schema)
       Returns: Created account with generated ID

GET    /accounts/:id
       Params: id (e.g., "ACC-001" or "1")
       Returns: Enriched account with relationships

PUT    /accounts/:id
       Body: Updated account data
       Returns: Updated account

DELETE /accounts/:id
       Returns: Success confirmation
```

#### Enrichment Endpoints

```
GET    /accounts/:id/relationships
       Returns: All related entities (tool, owner, verifications, assignments)

GET    /accounts/:id/verifications
       Returns: Verification accounts for this account

POST   /accounts/:id/verifications
       Body: { verification_account_id, method }
       Returns: Created verification relationship

GET    /accounts/tools/:tool_id
       Returns: All accounts using specific tool

GET    /accounts/owner/:employee_id
       Returns: All accounts owned by specific employee

GET    /accounts/department/:dept_code
       Returns: All accounts in specific department (via owner lookup)
```

### ENTITIES Validation API

**Base URL:** `https://libs.anyemp.com/api/v1/`

```
GET    /tools/:tool_id
       Validate tool exists

GET    /employees/:employee_id
       Validate employee exists (from TALENTS)

GET    /statuses/:type/:status_id
       Validate status exists for given type

GET    /countries/:country_id
       Get country details

GET    /currencies/:currency_id
       Get currency details
```

---

## Sync Strategy

### Real-time Sync (Write Operations)

**When:** Every CREATE, UPDATE, DELETE in PostgreSQL

**Process:**
1. Perform operation in PostgreSQL
2. If successful, trigger webhook/event
3. Event handler enriches data with ENTITIES lookups
4. Write JSON file to ENTITIES/{entity}/{sub_entity}/{id}.json
5. Update `last_synced_at` timestamp

**Implementation:**
```javascript
// PostgreSQL trigger or app-level hook
afterCreate('Account', async (account) => {
  const enrichedAccount = await enrichAccountWithEntities(account);
  await writeToEntities(enrichedAccount, `ACCOUNTS/Accounts/ACC-${account.id.toString().padStart(3, '0')}.json`);
});
```

### Batch Sync (Nightly)

**When:** Daily at 2 AM (configurable)

**Purpose:**
- Catch any missed real-time syncs
- Rebuild all relationships
- Update analytics and reports

**Process:**
```javascript
// Pseudo-code
async function nightly SyncPostgreSQLToEntities() {
  const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000);

  // Sync accounts
  const accounts = await db.accounts.findAll({ where: { updated_at: { gte: yesterday } } });
  for (const account of accounts) {
    const enriched = await enrichAccountWithEntities(account);
    await writeToEntities(enriched, `ACCOUNTS/Accounts/ACC-${formatId(account.id)}.json`);
  }

  // Sync job_accounts
  const jobAccounts = await db.job_accounts.findAll({ where: { updated_at: { gte: yesterday } } });
  for (const jobAccount of jobAccounts) {
    const enriched = await enrichJobAccountWithEntities(jobAccount);
    await writeToEntities(enriched, `ACCOUNTS/JobSites/JOB-ACC-${formatId(jobAccount.id)}.json`);
  }

  // Sync verifications, subscriptions, payments
  // ... similar pattern

  // Log sync results
  await logSyncResults('ANALYTICS/Sync_Logs/', results);
}
```

### Validation-Only Mode (No Sync)

**When:** For high-volume operations or testing

**Process:**
1. Validate against ENTITIES schemas
2. Perform PostgreSQL operation
3. Skip JSON sync (rely on nightly batch)

---

## Summary

### Key Principles

1. **PostgreSQL = Source of Truth** for transactional data
2. **ENTITIES = Reference Data** for taxonomy, templates, workflows
3. **Always validate** against ENTITIES schemas before write
4. **Enrich responses** with ENTITIES lookups for client consumption
5. **Sync strategically** (real-time for critical, batch for analytics)

### ID Transformation Rules

| Entity | PostgreSQL Type | ENTITIES Pattern | Example |
|--------|----------------|------------------|---------|
| Account | INTEGER | `ACC-{id:03d}` | ACC-001 |
| JobAccount | INTEGER | `JOB-ACC-{id:03d}` | JOB-ACC-042 |
| Verification | INTEGER | `VER-{id:05d}` | VER-00123 |
| Plan | INTEGER | `PLAN-{id:03d}` | PLAN-005 |
| Subscription | INTEGER | `SUB-{id:05d}` | SUB-00456 |
| Payment | INTEGER | `PAY-{id:06d}` | PAY-000789 |

### Critical Bridges

- `tool_id` → `LIBRARIES/Tools/`
- `owner_id` → `TALENTS/Employees/`
- `status_id` → `LIBRARIES/Statuses/`
- `country_id` → `LIBRARIES/Countries/`
- `currency_id` → `LIBRARIES/Currencies/`

---

**Next Steps:**
1. Implement ID transformation utilities
2. Build enrichment service layer
3. Set up real-time sync webhooks
4. Configure nightly batch sync cron job
5. Create API endpoint wrappers with automatic enrichment
