# Migration Scripts Specification
## Legacy Data → Account Management Microservice → ENTITIES

**Document Version:** 1.0
**Created:** 2025-11-18
**Purpose:** Define data migration strategy from existing files to PostgreSQL and ENTITIES JSON

---

## Table of Contents

1. [Overview](#overview)
2. [Source Data Analysis](#source-data-analysis)
3. [Migration Architecture](#migration-architecture)
4. [Migration Scripts](#migration-scripts)
5. [Data Transformation Rules](#data-transformation-rules)
6. [Validation & Quality Checks](#validation--quality-checks)
7. [Rollback Strategy](#rollback-strategy)
8. [Execution Plan](#execution-plan)

---

## Overview

### Migration Objectives

1. **Migrate existing account data** from JSON/Markdown files to PostgreSQL
2. **Transform data** to match new schema and ENTITIES taxonomy
3. **Preserve relationships** and historical data
4. **Validate data quality** at each step
5. **Sync to ENTITIES** JSON structure post-migration

### Data Sources

| Source File/Directory | Type | Description | Est. Records |
|----------------------|------|-------------|--------------|
| `Job_Account_prod.json` | JSON | Job posting accounts | ~50 |
| `Account_prod.md` | Markdown (JSON inside) | Platform accounts | ~100 |
| `LeadAccount_JSON_Clusters/` | JSON clusters | Lead account data | ~200 |
| Phone numbers in metadata | Nested data | Phone accounts | ~150 |

**Total Estimated Records:** ~500 accounts

---

## Source Data Analysis

### 1. Job_Account_prod.json Structure

**Current Format:**
```json
{
  "job_accounts": [
    {
      "id": 1,
      "name": "Indeed - HR Department",
      "site": "Indeed",
      "login": "hr@company.com",
      "password": "encrypted_password",
      "profile_url": "https://indeed.com/company/profile",
      "status": "active",
      "owner": "John Smith",
      "available_posts": 10,
      "active_posts": 3,
      "created": "2024-01-15"
    }
  ]
}
```

**Mapping to New Schema:**
```javascript
{
  id → job_account_id (transform to JOB-ACC-{id:03d})
  name → name (direct)
  site → job_site_id (lookup in accounts table via tool_id)
  login → login (direct)
  password → password (re-encrypt if needed)
  profile_url → profile_link (direct)
  status → status_id (map to LIBRARIES/Statuses)
  owner → owner_id (lookup in TALENTS/Employees by name)
  available_posts → available_job_posts (direct)
  active_posts → active_job_posts (direct)
  created → created_at (convert to timestamp)
}
```

### 2. Account_prod.md Structure

**Current Format:**
```markdown
# Accounts

## LinkedIn Accounts

```json
{
  "accounts": [
    {
      "id": 15,
      "name": "LinkedIn - HR Recruiter",
      "platform": "LinkedIn",
      "email": "hr@company.com",
      "password": "encrypted",
      "url": "https://linkedin.com/in/hr-recruiter",
      "status": "active",
      "owner": "John Smith",
      "connections": 500,
      "verified_by": "Gmail",
      "last_used": "2025-11-15"
    }
  ]
}
```
```

**Mapping to New Schema:**
```javascript
{
  id → account_id (transform to ACC-{id:03d})
  name → name (direct)
  platform → tool_id (lookup in LIBRARIES/Tools)
  email → login (direct)
  password → password (re-encrypt)
  url → profile_link (direct)
  status → status_id (map to LIBRARIES/Statuses)
  owner → owner_id (lookup in TALENTS/Employees)
  connections → connections (direct)
  verified_by → create verification record in verifications table
  last_used → last_used_at (convert to timestamp)
}
```

### 3. LeadAccount_JSON_Clusters Structure

**Current Format:**
```json
{
  "cluster_id": "lead_linkedin_01",
  "accounts": [
    {
      "account_name": "LinkedIn Lead Account 1",
      "tool": "LinkedIn",
      "login": "lead1@company.com",
      "status": "active",
      "country": "US",
      "can_verify": false,
      "metadata": {
        "industry": "Technology",
        "created_date": "2024-05-10"
      }
    }
  ]
}
```

**Mapping to New Schema:**
```javascript
{
  account_name → name (direct)
  tool → tool_id (lookup in LIBRARIES/Tools)
  login → login (direct)
  status → status_id (map to LIBRARIES/Statuses)
  country → country_id (map to LIBRARIES/Countries ISO codes)
  can_verify → can_verify_others (direct)
  metadata → metadata (JSONB, direct)
}
```

### 4. Phone Numbers in Metadata

**Current Format:**
```json
{
  "account": {
    "name": "LinkedIn - Sales",
    "verification": {
      "phone_numbers": [
        "+1-555-0100",
        "+1-555-0101"
      ]
    }
  }
}
```

**Migration Strategy:**
- Extract phone numbers
- Create separate `account` records for each phone
- Set `tool_id` to "Phone" tool
- Set `can_verify_others=true`
- Link to original account via `verifications` table

---

## Migration Architecture

### Migration Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│                  Phase 1: Extract & Parse                     │
│                                                               │
│  Source Files  →  Parse JSON/MD  →  Normalize Structure      │
│                                                               │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                  Phase 2: Transform & Validate                │
│                                                               │
│  Normalize Data  →  Lookup ENTITIES  →  Validate Schema      │
│                                                               │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                  Phase 3: Load to PostgreSQL                  │
│                                                               │
│  Insert Accounts  →  Create Verifications  →  Link Relations │
│                                                               │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                  Phase 4: Sync to ENTITIES                    │
│                                                               │
│  Enrich Data  →  Generate JSON Files  →  Validate Sync       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## Migration Scripts

### Script 1: migrate_job_accounts.js

**Purpose:** Migrate job posting accounts from `Job_Account_prod.json`

**File:** `scripts/migrations/migrate_job_accounts.js`

```javascript
const fs = require('fs').promises;
const { db } = require('../config/database');
const { lookupEmployee } = require('../services/entitiesApi');
const { encryptPassword } = require('../utils/encryption');

async function migrateJobAccounts() {
  console.log('Starting Job Account Migration...');

  // Step 1: Read source file
  const sourceData = JSON.parse(
    await fs.readFile('./data/Job_Account_prod.json', 'utf-8')
  );

  const results = {
    total: 0,
    success: 0,
    failed: 0,
    errors: []
  };

  // Step 2: Process each job account
  for (const jobAccount of sourceData.job_accounts) {
    results.total++;

    try {
      // Step 2a: Lookup owner in TALENTS
      const owner = await lookupEmployee(jobAccount.owner);
      if (!owner) {
        throw new Error(`Owner not found: ${jobAccount.owner}`);
      }

      // Step 2b: Lookup job site account
      const jobSiteAccount = await db.accounts.findOne({
        where: { name: { [Op.like]: `%${jobAccount.site}%` } }
      });
      if (!jobSiteAccount) {
        throw new Error(`Job site account not found: ${jobAccount.site}`);
      }

      // Step 2c: Map status
      const statusId = mapStatus(jobAccount.status);

      // Step 2d: Re-encrypt password
      const encryptedPassword = await encryptPassword(jobAccount.password);

      // Step 2e: Insert into PostgreSQL
      const newJobAccount = await db.job_accounts.create({
        name: jobAccount.name,
        job_site_id: jobSiteAccount.id,
        login: jobAccount.login,
        password: encryptedPassword,
        profile_link: jobAccount.profile_url,
        status_id: statusId,
        owner_id: owner.employee_id,
        available_job_posts: jobAccount.available_posts || 0,
        active_job_posts: jobAccount.active_posts || 0,
        metadata: {},
        created_at: new Date(jobAccount.created),
        updated_at: new Date()
      });

      // Step 2f: Sync to ENTITIES
      await syncToEntities(newJobAccount, 'job_account');

      console.log(`✓ Migrated: ${jobAccount.name} → JOB-ACC-${newJobAccount.id.toString().padStart(3, '0')}`);
      results.success++;

    } catch (error) {
      console.error(`✗ Failed: ${jobAccount.name}`, error.message);
      results.failed++;
      results.errors.push({
        account: jobAccount.name,
        error: error.message
      });
    }
  }

  // Step 3: Generate report
  console.log('\n=== Migration Summary ===');
  console.log(`Total: ${results.total}`);
  console.log(`Success: ${results.success}`);
  console.log(`Failed: ${results.failed}`);

  if (results.errors.length > 0) {
    await fs.writeFile(
      './logs/migration_job_accounts_errors.json',
      JSON.stringify(results.errors, null, 2)
    );
    console.log('Error log saved to: ./logs/migration_job_accounts_errors.json');
  }

  return results;
}

function mapStatus(oldStatus) {
  const statusMap = {
    'active': 'active',
    'inactive': 'inactive',
    'suspended': 'suspended',
    'pending': 'pending_verification'
  };
  return statusMap[oldStatus.toLowerCase()] || 'inactive';
}

async function syncToEntities(jobAccount, type) {
  // Enrich with ENTITIES data
  const enriched = await enrichJobAccountWithEntities(jobAccount);

  // Write JSON file
  const filePath = `../ENTITIES/ACCOUNTS/JobSites/JOB-ACC-${jobAccount.id.toString().padStart(3, '0')}.json`;
  await fs.writeFile(filePath, JSON.stringify(enriched, null, 2));
}

// Run migration
if (require.main === module) {
  migrateJobAccounts()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('Migration failed:', error);
      process.exit(1);
    });
}

module.exports = { migrateJobAccounts };
```

---

### Script 2: migrate_platform_accounts.js

**Purpose:** Migrate platform accounts from `Account_prod.md`

**File:** `scripts/migrations/migrate_platform_accounts.js`

```javascript
const fs = require('fs').promises;
const { db } = require('../config/database');
const { lookupTool, lookupEmployee } = require('../services/entitiesApi');
const { encryptPassword } = require('../utils/encryption');

async function migratePlatformAccounts() {
  console.log('Starting Platform Account Migration...');

  // Step 1: Read and parse markdown file
  const markdown = await fs.readFile('./data/Account_prod.md', 'utf-8');
  const jsonMatches = markdown.match(/```json\n([\s\S]*?)\n```/g);

  const results = {
    total: 0,
    success: 0,
    failed: 0,
    errors: [],
    verifications_created: 0
  };

  // Step 2: Process each JSON block
  for (const jsonBlock of jsonMatches) {
    const jsonContent = jsonBlock.replace(/```json\n|```/g, '');
    const data = JSON.parse(jsonContent);

    for (const account of data.accounts) {
      results.total++;

      try {
        // Step 2a: Lookup tool
        const tool = await lookupTool(account.platform);
        if (!tool) {
          throw new Error(`Tool not found: ${account.platform}`);
        }

        // Step 2b: Lookup owner
        const owner = await lookupEmployee(account.owner);
        if (!owner) {
          throw new Error(`Owner not found: ${account.owner}`);
        }

        // Step 2c: Determine account type from tool category
        const accountType = determineAccountType(tool.category);

        // Step 2d: Map status
        const statusId = mapStatus(account.status);

        // Step 2e: Re-encrypt password
        const encryptedPassword = await encryptPassword(account.password);

        // Step 2f: Insert into PostgreSQL
        const newAccount = await db.accounts.create({
          name: account.name,
          tool_id: tool.tool_id,
          login: account.email,
          password: encryptedPassword,
          profile_link: account.url,
          status_id: statusId,
          owner_id: owner.employee_id,
          account_type: accountType,
          connections: account.connections || null,
          verification_required: !!account.verified_by,
          last_used_at: account.last_used ? new Date(account.last_used) : null,
          usage_count: account.usage_count || 0,
          created_at: new Date(account.created || Date.now()),
          updated_at: new Date()
        });

        // Step 2g: Create verification if needed
        if (account.verified_by) {
          const verificationAccount = await findVerificationAccount(account.verified_by);
          if (verificationAccount) {
            await db.verifications.create({
              verifiable_type: 'account',
              verifiable_id: newAccount.id,
              verification_account_id: verificationAccount.id,
              created_at: new Date()
            });
            results.verifications_created++;
          }
        }

        // Step 2h: Sync to ENTITIES
        await syncToEntities(newAccount, 'account');

        console.log(`✓ Migrated: ${account.name} → ACC-${newAccount.id.toString().padStart(3, '0')}`);
        results.success++;

      } catch (error) {
        console.error(`✗ Failed: ${account.name}`, error.message);
        results.failed++;
        results.errors.push({
          account: account.name,
          error: error.message
        });
      }
    }
  }

  // Step 3: Generate report
  console.log('\n=== Migration Summary ===');
  console.log(`Total: ${results.total}`);
  console.log(`Success: ${results.success}`);
  console.log(`Failed: ${results.failed}`);
  console.log(`Verifications Created: ${results.verifications_created}`);

  if (results.errors.length > 0) {
    await fs.writeFile(
      './logs/migration_platform_accounts_errors.json',
      JSON.stringify(results.errors, null, 2)
    );
  }

  return results;
}

function determineAccountType(toolCategory) {
  const categoryMap = {
    'Social_Media_Tools': 'social_media',
    'Email_Tools': 'email',
    'CRM_Tools': 'crm',
    'Project_Management_Tools': 'project_management',
    'Communication_Tools': 'communication',
    'Development_Tools': 'development',
    'AI_Tools': 'ai_tool'
  };
  return categoryMap[toolCategory] || 'other';
}

async function findVerificationAccount(verifierName) {
  return await db.accounts.findOne({
    where: {
      name: { [Op.like]: `%${verifierName}%` },
      can_verify_others: true
    }
  });
}

function mapStatus(oldStatus) {
  const statusMap = {
    'active': 'active',
    'inactive': 'inactive',
    'suspended': 'suspended',
    'pending': 'pending_verification',
    'verified': 'active'
  };
  return statusMap[oldStatus.toLowerCase()] || 'inactive';
}

async function syncToEntities(account, type) {
  const enriched = await enrichAccountWithEntities(account);
  const filePath = `../ENTITIES/ACCOUNTS/Accounts/ACC-${account.id.toString().padStart(3, '0')}.json`;
  await fs.writeFile(filePath, JSON.stringify(enriched, null, 2));
}

if (require.main === module) {
  migratePlatformAccounts()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('Migration failed:', error);
      process.exit(1);
    });
}

module.exports = { migratePlatformAccounts };
```

---

### Script 3: migrate_lead_accounts.js

**Purpose:** Migrate lead accounts from `LeadAccount_JSON_Clusters/`

**File:** `scripts/migrations/migrate_lead_accounts.js`

```javascript
const fs = require('fs').promises;
const path = require('path');
const { db } = require('../config/database');
const { lookupTool, lookupCountry } = require('../services/entitiesApi');

async function migrateLeadAccounts() {
  console.log('Starting Lead Account Migration...');

  const clustersDir = './data/LeadAccount_JSON_Clusters';
  const clusterFiles = await fs.readdir(clustersDir);

  const results = {
    total: 0,
    success: 0,
    failed: 0,
    errors: []
  };

  // Process each cluster file
  for (const file of clusterFiles) {
    if (!file.endsWith('.json')) continue;

    const filePath = path.join(clustersDir, file);
    const cluster = JSON.parse(await fs.readFile(filePath, 'utf-8'));

    for (const account of cluster.accounts) {
      results.total++;

      try {
        const tool = await lookupTool(account.tool);
        if (!tool) {
          throw new Error(`Tool not found: ${account.tool}`);
        }

        const countryId = account.country ?
          await lookupCountry(account.country) : null;

        const newAccount = await db.accounts.create({
          name: account.account_name,
          tool_id: tool.tool_id,
          login: account.login,
          password: await encryptPassword('temporary_password'), // Require password reset
          status_id: mapStatus(account.status),
          owner_id: null, // Set later when owner assigned
          account_type: determineAccountType(tool.category),
          country_id: countryId,
          can_verify_others: account.can_verify || false,
          metadata: account.metadata || {},
          created_at: new Date(account.metadata?.created_date || Date.now()),
          updated_at: new Date()
        });

        await syncToEntities(newAccount, 'account');

        console.log(`✓ Migrated: ${account.account_name} → ACC-${newAccount.id.toString().padStart(3, '0')}`);
        results.success++;

      } catch (error) {
        console.error(`✗ Failed: ${account.account_name}`, error.message);
        results.failed++;
        results.errors.push({
          account: account.account_name,
          error: error.message
        });
      }
    }
  }

  console.log('\n=== Migration Summary ===');
  console.log(`Total: ${results.total}`);
  console.log(`Success: ${results.success}`);
  console.log(`Failed: ${results.failed}`);

  return results;
}

if (require.main === module) {
  migrateLeadAccounts()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('Migration failed:', error);
      process.exit(1);
    });
}

module.exports = { migrateLeadAccounts };
```

---

### Script 4: extract_phone_accounts.js

**Purpose:** Extract phone numbers from metadata and create phone accounts

**File:** `scripts/migrations/extract_phone_accounts.js`

```javascript
const { db } = require('../config/database');
const { lookupTool } = require('../services/entitiesApi');

async function extractPhoneAccounts() {
  console.log('Extracting Phone Accounts from Metadata...');

  // Get phone tool
  const phoneTool = await lookupTool('Phone');
  if (!phoneTool) {
    throw new Error('Phone tool not found in LIBRARIES/Tools');
  }

  const results = {
    total: 0,
    success: 0,
    failed: 0,
    errors: []
  };

  // Query all accounts with phone numbers in metadata
  const accountsWithPhones = await db.accounts.findAll({
    where: {
      metadata: {
        [Op.or]: [
          { phone: { [Op.ne]: null } },
          { phone_numbers: { [Op.ne]: null } },
          { verification: { phone_numbers: { [Op.ne]: null } } }
        ]
      }
    }
  });

  for (const account of accountsWithPhones) {
    const phoneNumbers = extractPhoneNumbers(account.metadata);

    for (const phoneNumber of phoneNumbers) {
      results.total++;

      try {
        const phoneAccount = await db.accounts.create({
          name: `Phone - ${phoneNumber}`,
          tool_id: phoneTool.tool_id,
          login: phoneNumber,
          password: null, // Phones don't have passwords
          status_id: 'active',
          owner_id: account.owner_id,
          account_type: 'phone',
          can_verify_others: true,
          metadata: {
            associated_account: account.id,
            phone_type: 'verification'
          },
          created_at: new Date(),
          updated_at: new Date()
        });

        // Create verification link
        await db.verifications.create({
          verifiable_type: 'account',
          verifiable_id: account.id,
          verification_account_id: phoneAccount.id,
          created_at: new Date()
        });

        await syncToEntities(phoneAccount, 'account');

        console.log(`✓ Created phone account: ${phoneNumber} → ACC-${phoneAccount.id.toString().padStart(3, '0')}`);
        results.success++;

      } catch (error) {
        console.error(`✗ Failed: ${phoneNumber}`, error.message);
        results.failed++;
        results.errors.push({
          phone: phoneNumber,
          error: error.message
        });
      }
    }
  }

  console.log('\n=== Extraction Summary ===');
  console.log(`Total Phone Numbers: ${results.total}`);
  console.log(`Success: ${results.success}`);
  console.log(`Failed: ${results.failed}`);

  return results;
}

function extractPhoneNumbers(metadata) {
  const phones = [];

  if (metadata.phone) phones.push(metadata.phone);
  if (metadata.phone_numbers) phones.push(...metadata.phone_numbers);
  if (metadata.verification?.phone_numbers) phones.push(...metadata.verification.phone_numbers);

  return [...new Set(phones)]; // Deduplicate
}

if (require.main === module) {
  extractPhoneAccounts()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('Extraction failed:', error);
      process.exit(1);
    });
}

module.exports = { extractPhoneAccounts };
```

---

### Script 5: migrate_all.js (Master Script)

**Purpose:** Run all migration scripts in sequence

**File:** `scripts/migrations/migrate_all.js`

```javascript
const { migrateJobAccounts } = require('./migrate_job_accounts');
const { migratePlatformAccounts } = require('./migrate_platform_accounts');
const { migrateLeadAccounts } = require('./migrate_lead_accounts');
const { extractPhoneAccounts } = require('./extract_phone_accounts');

async function migrateAll() {
  console.log('═══════════════════════════════════════════════');
  console.log('  ACCOUNT MANAGEMENT MICROSERVICE MIGRATION');
  console.log('═══════════════════════════════════════════════\n');

  const startTime = Date.now();
  const results = {
    job_accounts: null,
    platform_accounts: null,
    lead_accounts: null,
    phone_accounts: null
  };

  try {
    // Step 1: Migrate Job Accounts
    console.log('\n[1/4] Migrating Job Accounts...');
    results.job_accounts = await migrateJobAccounts();

    // Step 2: Migrate Platform Accounts
    console.log('\n[2/4] Migrating Platform Accounts...');
    results.platform_accounts = await migratePlatformAccounts();

    // Step 3: Migrate Lead Accounts
    console.log('\n[3/4] Migrating Lead Accounts...');
    results.lead_accounts = await migrateLeadAccounts();

    // Step 4: Extract Phone Accounts
    console.log('\n[4/4] Extracting Phone Accounts...');
    results.phone_accounts = await extractPhoneAccounts();

    // Final Summary
    const duration = ((Date.now() - startTime) / 1000).toFixed(2);

    console.log('\n═══════════════════════════════════════════════');
    console.log('  MIGRATION COMPLETE');
    console.log('═══════════════════════════════════════════════');
    console.log(`\nDuration: ${duration} seconds\n`);

    console.log('Summary by Type:');
    console.log(`  Job Accounts: ${results.job_accounts.success}/${results.job_accounts.total}`);
    console.log(`  Platform Accounts: ${results.platform_accounts.success}/${results.platform_accounts.total}`);
    console.log(`  Lead Accounts: ${results.lead_accounts.success}/${results.lead_accounts.total}`);
    console.log(`  Phone Accounts: ${results.phone_accounts.success}/${results.phone_accounts.total}`);

    const totalSuccess = Object.values(results).reduce((sum, r) => sum + r.success, 0);
    const totalRecords = Object.values(results).reduce((sum, r) => sum + r.total, 0);

    console.log(`\nTotal: ${totalSuccess}/${totalRecords} records migrated`);
    console.log(`Success Rate: ${((totalSuccess / totalRecords) * 100).toFixed(2)}%`);

  } catch (error) {
    console.error('\n✗ MIGRATION FAILED:', error.message);
    console.error(error.stack);
    process.exit(1);
  }
}

if (require.main === module) {
  migrateAll()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error('Migration failed:', error);
      process.exit(1);
    });
}

module.exports = { migrateAll };
```

---

## Data Transformation Rules

### ID Transformations

| Source | Target PostgreSQL | Target ENTITIES | Example |
|--------|------------------|-----------------|---------|
| Job Account ID (integer) | `id` (SERIAL) | `job_account_id` (string) | 5 → "JOB-ACC-005" |
| Account ID (integer) | `id` (SERIAL) | `account_id` (string) | 42 → "ACC-042" |
| Owner name (string) | `owner_id` (VARCHAR) | `owner_id` (string) | "John Smith" → "EMP-2025-042" |
| Platform name (string) | `tool_id` (INTEGER) | `tool_id` (string) | "LinkedIn" → 15 → "TOOL-015" |

### Status Mappings

| Legacy Status | PostgreSQL status_id | ENTITIES status_id |
|---------------|---------------------|-------------------|
| "active" | "active" | "active" |
| "inactive" | "inactive" | "inactive" |
| "suspended" | "suspended" | "suspended" |
| "pending" | "pending_verification" | "pending_verification" |
| "verified" | "active" | "active" (verification_status="verified") |

### Date/Time Transformations

```javascript
// Legacy: "2024-01-15"
// PostgreSQL: "2024-01-15T00:00:00Z" (TIMESTAMP)
// ENTITIES: "2024-01-15" (Date format)

function transformDate(legacyDate) {
  const postgresTimestamp = new Date(legacyDate).toISOString();
  const entitiesDate = legacyDate; // Keep as-is if already YYYY-MM-DD

  return { postgresTimestamp, entitiesDate };
}
```

---

## Validation & Quality Checks

### Pre-Migration Validation

```javascript
async function validateBeforeMigration() {
  const checks = {
    tools_exist: await checkToolsLibraryExists(),
    employees_exist: await checkEmployeesExist(),
    statuses_defined: await checkStatusesExist(),
    postgresql_ready: await checkPostgreSQLConnection(),
    entities_path_writable: await checkEntitiesPathWritable()
  };

  const failed = Object.entries(checks).filter(([k, v]) => !v);

  if (failed.length > 0) {
    throw new Error(`Pre-migration validation failed: ${failed.map(([k]) => k).join(', ')}`);
  }

  return true;
}
```

### Post-Migration Validation

```javascript
async function validateAfterMigration() {
  const results = {
    record_count_matches: false,
    no_orphaned_records: false,
    all_foreign_keys_valid: false,
    entities_files_created: false
  };

  // Count validation
  const postgresCount = await db.accounts.count() + await db.job_accounts.count();
  const sourceCount = await countSourceRecords();
  results.record_count_matches = postgresCount === sourceCount;

  // Orphaned records check
  const orphanedOwners = await db.accounts.count({
    where: { owner_id: { [Op.notIn]: await getAllEmployeeIds() } }
  });
  results.no_orphaned_records = orphanedOwners === 0;

  // Foreign key validation
  const invalidTools = await db.accounts.count({
    where: { tool_id: { [Op.notIn]: await getAllToolIds() } }
  });
  results.all_foreign_keys_valid = invalidTools === 0;

  // ENTITIES files check
  const entitiesFileCount = await countEntitiesJSONFiles();
  results.entities_files_created = entitiesFileCount === postgresCount;

  return results;
}
```

---

## Rollback Strategy

### Rollback Script

**File:** `scripts/migrations/rollback_migration.js`

```javascript
async function rollbackMigration() {
  console.log('Starting migration rollback...');

  // Step 1: Backup current state
  await backupPostgreSQL();

  // Step 2: Delete migrated records
  await db.verification_subscription_payments.destroy({ truncate: true });
  await db.verification_subscriptions.destroy({ truncate: true });
  await db.verifications.destroy({ truncate: true });
  await db.user_assignments.destroy({ truncate: true });
  await db.job_accounts.destroy({ truncate: true });
  await db.accounts.destroy({ truncate: true });

  // Step 3: Delete ENTITIES JSON files
  await deleteEntitiesJSONFiles();

  // Step 4: Reset auto-increment
  await db.sequelize.query('ALTER SEQUENCE accounts_id_seq RESTART WITH 1');
  await db.sequelize.query('ALTER SEQUENCE job_accounts_id_seq RESTART WITH 1');

  console.log('Rollback complete. Database reset to pre-migration state.');
}
```

---

## Execution Plan

### Phase 1: Preparation (Week 1)

- [x] Set up PostgreSQL database
- [x] Create all tables with migrations
- [x] Validate ENTITIES paths
- [x] Prepare source data files

### Phase 2: Development (Week 2-3)

- [x] Develop migration scripts
- [ ] Test on sample data
- [ ] Validate transformations
- [ ] Create rollback scripts

### Phase 3: Testing (Week 4)

- [ ] Run on staging environment
- [ ] Validate all data
- [ ] Performance testing
- [ ] Fix identified issues

### Phase 4: Production Migration (Week 5)

**Date:** TBD (after testing complete)

**Timeline:**
- 00:00 - Backup production databases
- 00:30 - Run pre-migration validation
- 01:00 - Execute migration (estimated 2 hours)
- 03:00 - Run post-migration validation
- 04:00 - Smoke testing
- 06:00 - Go/No-Go decision

**Success Criteria:**
- ✅ All source records migrated (success rate > 95%)
- ✅ Foreign key constraints valid
- ✅ ENTITIES JSON files created
- ✅ Verification relationships preserved
- ✅ No data loss

---

**End of Document**

For migration support: dev@company.com
Migration coordinator: [Name]
