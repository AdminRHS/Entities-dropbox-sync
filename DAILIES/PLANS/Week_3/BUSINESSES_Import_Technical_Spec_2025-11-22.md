# BUSINESSES Import - Technical Specification
**Created:** 2025-11-22
**Version:** 1.0
**Approach:** Read-only source, classify fields, verify tagging logic, future Google Calendar integration

---

## Table of Contents
1. [Core Principles](#1-core-principles)
2. [Sub-Entity Schemas](#2-sub-entity-schemas)
3. [Field Classification System](#3-field-classification-system)
4. [Future Integration: Google Calendar](#4-future-integration-google-calendar)
5. [Data Flow & Dependencies](#5-data-flow--dependencies)
6. [Phase 0: Cleanup](#6-phase-0-cleanup)
7. [Phase 1: Schema Definition](#7-phase-1-schema-definition)
8. [Phase 2: Field Classification & Mapping](#8-phase-2-field-classification--mapping)
9. [Phase 3: Data Extraction (Read-Only)](#9-phase-3-data-extraction-read-only)
10. [Phase 4: Metadata Tagging Logic](#10-phase-4-metadata-tagging-logic)
11. [Phase 5: Entity Categorization](#11-phase-5-entity-categorization)
12. [Phase 6: ID Generation & Tracking](#12-phase-6-id-generation--tracking)
13. [Phase 7: JSON Generation](#13-phase-7-json-generation)
14. [Phase 8: Validation](#14-phase-8-validation)
15. [Phase 9: Documentation](#15-phase-9-documentation)
16. [Success Criteria](#16-success-criteria)
17. [Error Handling](#17-error-handling)

---

## 1. Core Principles

### 1.1 Read-Only Source Access
- **NEVER modify files in Nov25/Sales Nov25/**
- **NEVER modify files in Nov25/Sales_Oct25/**
- All source files are read-only inputs
- Track what has been processed via registry files

### 1.2 Tracking System
Maintain a registry of processed records:
```json
{
  "processed_records": [
    {
      "source_file": "client_list.md",
      "source_row": 5,
      "company_name": "TIAL",
      "processed_date": "2025-11-22",
      "output_id": "BUS-2025-001"
    }
  ]
}
```

### 1.3 Field-First Approach
Before extracting data:
1. Classify all source fields into logical groups
2. Define which fields map to which metadata
3. Verify tagging logic for each field chunk
4. Only then extract and transform

### 1.4 Future-Ready Design
Schema designed to accommodate:
- Google Calendar integration for call metadata
- Additional CRM data sources
- External API enrichment

---

## 2. Sub-Entity Schemas

### 2.1 Overview
Schemas aligned with existing database structure, adapted for JSON/Markdown file architecture.

**Database Tables → JSON Sub-Entities Mapping:**

**Company/Client Data:**
- `companies` → `company`
- `company_cities` → `company.locations[]`
- `company_industries` → `company.industries[]`
- `pocs` + `poc_contacts` → `pocs[]`
- `leads` / `clients` / `affiliates` → `business_relationship`
- `business_users` → `assigned_users`

**Prospect Data (Pre-conversion):**
- `prospects` → `prospect`
- `prospect_companies` → `prospect_company`
- `prospect_contacts` → `prospect.contacts[]`
- `prospect_communications` → `prospect_communications[]`
- `prospect_company_industries` → `prospect_company.industries[]`

**Lookup Tables (Separate Folders):**

- `industries` → `BUSINESSES/Industries/`
- `sub_industries` → `BUSINESSES/SubIndustries/`
- `positions` → `BUSINESSES/Positions/`
- `company_sizes` → `BUSINESSES/CompanySizes/`
- `lead_statuses` → `BUSINESSES/LeadStatuses/`
- `lead_sources` → `BUSINESSES/LeadSources/`
- `countries` → `BUSINESSES/Countries/`
- `contact_types` → `BUSINESSES/ContactTypes/`
- `templates` → `BUSINESSES/Templates/`
- `job_requests` → `job_requests[]` (sub-entity within BUSINESSES)

### 2.2 Company Sub-Entity
Maps to: `companies`, `company_cities`, `company_industries`

```json
{
  "company": {
    "id": "BUS-2025-001",
    "name": "TIAL (The Institutional Architecture Lab)",
    "logo": null,
    "website": "https://tial.org",
    "size_id": 3,
    "size_label": "50-100",
    "year_established": 2018,
    "note": "AI research and consulting firm focused on institutional innovation",
    "tool_id": null,
    "prospect_company_id": null,
    "locations": [
      {
        "city_id": 123,
        "city_name": "New York",
        "country_id": 1,
        "country_name": "USA",
        "is_primary": true
      }
    ],
    "industries": [
      {
        "industry_id": 5,
        "industry_name": "Technology",
        "sub_industry_id": 12,
        "sub_industry_name": "AI/ML"
      }
    ]
  }
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | companies.id | Unique ID (BUS-YYYY-###) |
| name | string | companies.name | Company name (VARCHAR 255) |
| logo | string | companies.logo | Logo URL (VARCHAR 255) |
| website | string | companies.website | Website URL (VARCHAR 255) |
| size_id | integer | companies.size_id | FK to sizes lookup |
| size_label | string | - | Denormalized size name |
| year_established | integer | companies.year_established | YEAR |
| note | string | companies.note | Notes (VARCHAR 3000) |
| tool_id | integer | companies.tool_id | FK to tools |
| prospect_company_id | integer | companies.prospect_company_id | Parent prospect |
| locations | array | company_cities | City/country list |
| industries | array | company_industries | Industry/sub-industry list |

### 2.3 POCs Sub-Entity (Points of Contact)
Maps to: `pocs`, `poc_contacts`, `poc_types`, `company_pocs`

```json
{
  "pocs": [
    {
      "id": "POC-001",
      "name": "Sir Geoff Mulgan",
      "position_id": 1,
      "position_name": "CEO",
      "status_id": 1,
      "status_name": "Active",
      "availability": "active",
      "poc_types": [
        {
          "poc_type_id": 1,
          "poc_type_name": "Decision Maker"
        },
        {
          "poc_type_id": 3,
          "poc_type_name": "Technical Contact"
        }
      ],
      "contacts": [
        {
          "contact_id": 101,
          "contact_type": "email",
          "contact_value": "gjmulgan@gmail.com",
          "is_primary": true
        },
        {
          "contact_id": 102,
          "contact_type": "phone",
          "contact_value": "+1-555-123-4567",
          "is_primary": false
        },
        {
          "contact_id": 103,
          "contact_type": "linkedin",
          "contact_value": "linkedin.com/in/geoffmulgan",
          "is_primary": false
        }
      ]
    }
  ]
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | pocs.id | POC ID |
| name | string | pocs.name | Full name (VARCHAR 100) |
| position_id | integer | pocs.position_id | FK to positions |
| position_name | string | - | Denormalized position |
| status_id | integer | pocs.status_id | FK to statuses |
| status_name | string | - | Denormalized status |
| availability | enum | pocs.availability | active/inactive |
| poc_types | array | poc_poc_type | Type classifications |
| contacts | array | poc_contacts | Contact methods |

### 2.4 Business Relationship Sub-Entity
Maps to: `businesses`, `leads`, `clients`, `affiliates`

```json
{
  "business_relationship": {
    "business_id": "BIZ-001",
    "entity_id": 1,
    "entity_type": "lead",
    "created_by": 5,
    "created_at": "2025-09-19T10:00:00Z",
    "lead_info": {
      "lead_id": "LEAD-001",
      "status": "qualified",
      "source": "referral"
    },
    "client_info": null,
    "affiliate_info": null
  }
}
```

**For Clients:**
```json
{
  "business_relationship": {
    "business_id": "BIZ-002",
    "entity_id": 2,
    "entity_type": "client",
    "created_by": 5,
    "created_at": "2025-10-01T10:00:00Z",
    "lead_info": null,
    "client_info": {
      "client_id": "CLI-001",
      "contract_start": "2025-10-01",
      "contract_end": null,
      "lifetime_value": 15000,
      "monthly_revenue": 2500
    },
    "affiliate_info": null
  }
}
```

**For Affiliates:**
```json
{
  "business_relationship": {
    "business_id": "BIZ-003",
    "entity_id": 3,
    "entity_type": "affiliate",
    "created_by": 5,
    "created_at": "2025-11-01T10:00:00Z",
    "lead_info": null,
    "client_info": null,
    "affiliate_info": {
      "affiliate_id": "AFF-001",
      "promo_code_id": 10,
      "promo_code": "TIAL2025",
      "affiliate_model_id": 2,
      "affiliate_model": "revenue_share",
      "commission": 15,
      "referred_prospects": [],
      "referred_companies": []
    }
  }
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| business_id | string | businesses.id | Business record ID |
| entity_id | integer | businesses.entity_id | Entity type FK |
| entity_type | string | - | lead/client/affiliate |
| created_by | integer | businesses.created_by | User who created |
| created_at | string | businesses.created_at | Timestamp |
| lead_info | object | leads.* | Lead-specific data |
| client_info | object | clients.* | Client-specific data |
| affiliate_info | object | affiliates.* | Affiliate-specific data |

### 2.5 Communication History Sub-Entity
All meetings, calls, and emails with the company.

```json
{
  "communication_history": {
    "total_interactions": 5,
    "first_contact": "2025-09-19",
    "last_contact": "2025-10-08",
    "interactions": [
      {
        "id": "COMM-001",
        "date": "2025-10-08",
        "time": "14:00",
        "type": "Call",
        "source": "google_calendar",
        "event_id": "calendar_abc123",
        "summary": "Follow-up call - discussed AI project",
        "duration_minutes": 30,
        "attendees": [
          "sales@company.com",
          "gjmulgan@gmail.com"
        ],
        "meeting_link": "https://meet.google.com/xxx",
        "notes": "Discussed requirements for AI automation project. Client interested in starting Q1.",
        "outcome": "Scheduled proposal presentation",
        "action_items": [
          "Send proposal by Friday",
          "Share case studies"
        ],
        "conducted_by": "Kovalska_Anastasiya"
      },
      {
        "id": "COMM-002",
        "date": "2025-09-19",
        "time": "13:49",
        "type": "Call",
        "source": "manual",
        "event_id": null,
        "summary": "Initial discovery call",
        "duration_minutes": 45,
        "attendees": [
          "sales@company.com",
          "gjmulgan@gmail.com"
        ],
        "meeting_link": null,
        "notes": "First contact. Client found us through referral.",
        "outcome": "Qualified as prospect",
        "action_items": [
          "Send company overview",
          "Schedule follow-up"
        ],
        "conducted_by": "Kovalska_Anastasiya"
      }
    ],
    "emails_sent": 3,
    "calls_completed": 2,
    "meetings_held": 0
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_interactions | number | Yes | Count of all interactions |
| first_contact | string | Yes | First contact date |
| last_contact | string | Yes | Most recent contact |
| interactions | array | Yes | List of all interactions |
| interactions[].id | string | Yes | Unique interaction ID |
| interactions[].date | string | Yes | YYYY-MM-DD |
| interactions[].time | string | No | HH:MM |
| interactions[].type | string | Yes | Call/Email/Meeting |
| interactions[].source | string | Yes | manual/google_calendar |
| interactions[].event_id | string | No | Calendar event ID |
| interactions[].summary | string | Yes | Brief description |
| interactions[].duration_minutes | number | No | Length of interaction |
| interactions[].attendees | array | No | Email addresses |
| interactions[].meeting_link | string | No | Video call URL |
| interactions[].notes | string | No | Detailed notes |
| interactions[].outcome | string | No | Result of interaction |
| interactions[].action_items | array | No | Follow-up tasks |
| interactions[].conducted_by | string | No | Sales manager |
| emails_sent | number | Yes | Total emails |
| calls_completed | number | Yes | Total calls |
| meetings_held | number | Yes | Total meetings |

### 2.6 Prospect Sub-Entity
Maps to: `prospects`, `prospect_contacts`

```json
{
  "prospect": {
    "id": "PROS-001",
    "name": "Sir Geoff Mulgan",
    "position_id": 1,
    "position_name": "CEO",
    "status_id": 2,
    "status_name": "Qualified",
    "notes": "Initial discovery call completed. Interested in AI automation.",
    "tool_id": null,
    "contacts": [
      {
        "contact_id": 101,
        "contact_type": "email",
        "contact_value": "gjmulgan@gmail.com",
        "is_primary": true
      }
    ]
  }
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | prospects.id | Prospect ID |
| name | string | prospects.name | Name (VARCHAR 100) |
| position_id | integer | prospects.position_id | FK to positions |
| status_id | integer | prospects.status_id | FK to statuses |
| notes | string | prospects.notes | Notes (VARCHAR 500) |
| tool_id | integer | prospects.tool_id | FK to tools |
| contacts | array | prospect_contacts | Contact methods |

### 2.7 Prospect Company Sub-Entity
Maps to: `prospect_companies`, `prospect_company_industries`, `prospect_company_sub_industries`

```json
{
  "prospect_company": {
    "id": "PCOMP-001",
    "name": "TIAL",
    "website": "https://tial.org",
    "city_id": 123,
    "city_name": "New York",
    "country_id": 1,
    "country_name": "USA",
    "affiliate_id": null,
    "tool_id": null,
    "manager_id": 5,
    "manager_name": "Kovalska_Anastasiya",
    "created_by": 5,
    "created_at": "2025-09-19T10:00:00Z",
    "industries": [
      {
        "industry_id": 5,
        "industry_name": "Technology"
      }
    ],
    "sub_industries": [
      {
        "sub_industry_id": 12,
        "sub_industry_name": "AI/ML"
      }
    ],
    "prospects": ["PROS-001"],
    "contacts": [
      {
        "contact_id": 101,
        "contact_type": "email",
        "contact_value": "info@tial.org"
      }
    ]
  }
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | prospect_companies.id | Company ID |
| name | string | prospect_companies.name | Name (VARCHAR 100) |
| website | string | prospect_companies.website | Website (VARCHAR 255) |
| city_id | integer | prospect_companies.city_id | FK to cities |
| country_id | integer | prospect_companies.country_id | FK to countries |
| affiliate_id | integer | prospect_companies.affiliate_id | FK to affiliates |
| manager_id | integer | prospect_companies.manager_id | FK to users |
| created_by | integer | prospect_companies.created_by | Creator user |
| created_at | string | prospect_companies.created_at | Datetime |
| industries | array | prospect_company_industries | Industry FKs |
| sub_industries | array | prospect_company_sub_industries | Sub-industry FKs |

### 2.8 Prospect Communications Sub-Entity
Maps to: `prospect_communications`, `prospect_communication_messages`

```json
{
  "prospect_communications": [
    {
      "id": "PCOMM-001",
      "prospect_id": "PROS-001",
      "prospect_company_id": "PCOMP-001",
      "user_id": 5,
      "user_name": "Kovalska_Anastasiya",
      "account_id": 1,
      "created_at": "2025-09-19T13:49:00Z",
      "is_followup": false,
      "note": "Initial discovery call. Client interested in AI automation services.",
      "messages": [
        {
          "message_id": 1,
          "message_type": "email",
          "message_content": "Follow-up email sent"
        }
      ]
    }
  ]
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | prospect_communications.id | Communication ID |
| prospect_id | string | prospect_communications.prospect_id | FK to prospects |
| prospect_company_id | string | prospect_communications.prospect_company_id | FK to prospect_companies |
| user_id | integer | prospect_communications.user_id | FK to users |
| account_id | integer | prospect_communications.account_id | FK to accounts |
| created_at | string | prospect_communications.created_at | Datetime |
| is_followup | boolean | prospect_communications.is_followup | Is follow-up? |
| note | string | prospect_communications.note | Note (VARCHAR 500) |
| messages | array | prospect_communication_messages | Message FKs |

### 2.9 Assigned Users Sub-Entity
Maps to: `business_users`, `companies`

```json
{
  "assigned_users": {
    "lead_generator_id": 12,
    "lead_generator_name": "John Smith",
    "sales_assistant_id": 8,
    "sales_assistant_name": "Maria Garcia",
    "sales_manager_id": 5,
    "sales_manager_name": "Kovalska_Anastasiya",
    "business_users": [
      {
        "user_id": 5,
        "user_name": "Kovalska_Anastasiya",
        "role": "sales_manager"
      }
    ]
  }
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| lead_generator_id | integer | companies.lead_generator_id | LG user FK |
| sales_assistant_id | integer | companies.sales_assistant_id | SA user FK |
| sales_manager_id | integer | companies.sales_manager_id | SM user FK |
| business_users | array | business_users | All assigned users |

---

## 2.10 Lookup Table Folders

### Industries Folder
**Location:** `BUSINESSES/Industries/`

```json
{
  "id": 20,
  "company_id": 1,
  "group_id": 20,
  "status_id": 1,
  "title": "Finance",
  "created_at": "2020-09-04T08:45:50.000000Z",
  "updated_at": "2020-09-04T08:45:50.000000Z"
}
```

**Files:** `Industry_Finance_20.json`, `Industries_INDEX.json`

### SubIndustries Folder
**Location:** `BUSINESSES/SubIndustries/`

```json
{
  "id": 114,
  "company_id": 1,
  "name": "Financial Services",
  "industry_id": 20,
  "created_at": "2024-12-16T09:34:38.000000Z",
  "updated_at": "2024-12-16T09:34:38.000000Z"
}
```

**Files:** `SubIndustry_Financial_Services_114.json`, `SubIndustries_INDEX.json`

### Positions Folder
**Location:** `BUSINESSES/Positions/`

```json
{
  "id": 1,
  "name": "CEO",
  "level": "C-Suite",
  "is_decision_maker": true,
  "is_active": true
}
```

**Files:** `Position_CEO_1.json`, `Positions_INDEX.json`

### CompanySizes Folder
**Location:** `BUSINESSES/CompanySizes/`

```json
{
  "id": 1,
  "company_id": 1,
  "title": "2...10",
  "created_at": "2020-09-04T08:45:50.000000Z",
  "updated_at": "2020-09-04T08:45:50.000000Z"
}
```

**Files:** `CompanySize_2_10_1.json`, `CompanySizes_INDEX.json`

### LeadStatuses Folder
**Location:** `BUSINESSES/LeadStatuses/`

```json
{
  "id": 20,
  "company_id": 1,
  "type": "Call",
  "priority": 8,
  "default": false,
  "label_color": "#ff0000"
}
```

**Files:** `LeadStatus_Call_20.json`, `LeadStatuses_INDEX.json`

### LeadSources Folder
**Location:** `BUSINESSES/LeadSources/`

```json
{
  "id": 76,
  "company_id": 1,
  "name": "LinkedIn Extension",
  "category_id": 3,
  "created_at": "2024-01-17T13:26:23.000000Z",
  "updated_at": "2024-03-04T08:24:11.000000Z"
}
```

**Files:** `LeadSource_LinkedIn_Extension_76.json`, `LeadSources_INDEX.json`

### Countries Folder
**Location:** `BUSINESSES/Countries/`

```json
{
  "id": 272,
  "name": "United Kingdom",
  "iso": "GB",
  "iso3": null,
  "iso_numeric": 0,
  "phonecode": 0
}
```

**Files:** `Country_United_Kingdom_272.json`, `Countries_INDEX.json`

### ContactTypes Folder
**Location:** `BUSINESSES/ContactTypes/`

```json
{
  "id": 1,
  "name": "LinkedIn Company",
  "icon": "linkedin",
  "is_active": true
}
```

**Files:** `ContactType_LinkedIn_1.json`, `ContactTypes_INDEX.json`

### Templates Folder
**Location:** `BUSINESSES/Templates/`

#### Message Template
```json
{
  "id": "TPL-MSG-001",
  "type": "message",
  "name": "LinkedIn Initial Outreach",
  "platform": "linkedin",
  "content": "Hi {{poc_name}}, I noticed your work at {{company_name}}...",
  "variables": ["{{poc_name}}", "{{company_name}}", "{{industry}}"],
  "use_case": "initial_outreach",
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-11-22T10:00:00Z",
  "is_active": true
}
```

#### Email Template
```json
{
  "id": "TPL-EMAIL-001",
  "type": "email",
  "name": "Follow-up Email After Call",
  "subject": "Great speaking with you, {{poc_name}}!",
  "body": "Hi {{poc_name}},\n\nThank you for taking the time to speak with me today about {{company_name}}'s needs...",
  "variables": ["{{poc_name}}", "{{company_name}}", "{{discussed_services}}"],
  "use_case": "post_call_followup",
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-11-22T10:00:00Z",
  "is_active": true
}
```

#### Call Summary Template
```json
{
  "id": "TPL-CALL-001",
  "type": "call_summary",
  "name": "Discovery Call Summary",
  "sections": [
    {
      "name": "attendees",
      "label": "Attendees",
      "required": true
    },
    {
      "name": "agenda",
      "label": "Agenda Items",
      "required": true
    },
    {
      "name": "key_points",
      "label": "Key Discussion Points",
      "required": true
    },
    {
      "name": "client_needs",
      "label": "Client Needs Identified",
      "required": false
    },
    {
      "name": "action_items",
      "label": "Action Items",
      "required": true
    },
    {
      "name": "next_steps",
      "label": "Next Steps",
      "required": true
    }
  ],
  "use_case": "discovery_call",
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-11-22T10:00:00Z",
  "is_active": true
}
```

#### First Call Event Template
```json
{
  "id": "TPL-EVENT-001",
  "type": "first_call_event",
  "name": "First Discovery Call Event",
  "duration_default": 30,
  "title_template": "Discovery Call - {{company_name}}",
  "description_template": "First call with {{poc_name}} from {{company_name}}\n\nAgenda:\n- Introduction\n- Understanding needs\n- Our services overview\n- Q&A\n- Next steps",
  "variables": ["{{company_name}}", "{{poc_name}}", "{{poc_email}}"],
  "attendees_required": ["sales_manager", "poc"],
  "reminder_minutes": [10, 1440],
  "meeting_link_type": "google_meet",
  "use_case": "first_call_scheduling",
  "created_at": "2025-01-15T10:00:00Z",
  "updated_at": "2025-11-22T10:00:00Z",
  "is_active": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| id | string | Template ID (TPL-TYPE-###) |
| type | string | message/email/call_summary/first_call_event |
| name | string | Human-readable template name |
| variables | array | Placeholder variables for substitution |
| use_case | string | When to use this template |
| is_active | boolean | Template availability status |

**Files:** `Template_LinkedIn_Initial_MSG001.json`, `Template_Followup_Email_EMAIL001.json`, `Templates_INDEX.json`

---

### 2.11 Job Requests Sub-Entity
Maps to: `job_requests`, `job_request_tool`, `job_request_language`, `job_request_object_action`, `job_request_job_template`

```json
{
  "job_requests": [
    {
      "id": "JR-001",
      "name": "Senior Python Developer",
      "entity_id": 1,
      "inner_client_id": 2,
      "profession_id": 15,
      "profession_name": "Python Developer",
      "status_id": 1,
      "status_name": "Open",
      "quantity": 2,
      "manager_id": 5,
      "manager_name": "Kovalska_Anastasiya",
      "rate_id": 3,
      "rate_name": "Senior",
      "shift_id": 1,
      "shift_name": "Full-time",
      "created_by": 5,
      "created_at": "2025-11-01T10:00:00Z",
      "demand_date": "2025-12-01",
      "close_date": null,
      "sum_jas": 0,
      "note": "Client needs experienced Python developer for AI automation project. Must have experience with ML frameworks.",
      "prospect_id": "PROS-001",
      "tools": [
        {
          "tool_id": 10,
          "tool_name": "Python"
        },
        {
          "tool_id": 15,
          "tool_name": "TensorFlow"
        }
      ],
      "languages": [
        {
          "language_id": 1,
          "language_name": "English",
          "level_id": 4,
          "level_name": "Fluent"
        }
      ],
      "object_actions": [
        {
          "object_action_id": 101
        }
      ],
      "job_templates": [
        {
          "job_template_id": 5,
          "job_template_name": "Developer Position"
        }
      ]
    }
  ]
}
```

| Field | Type | DB Column | Description |
|-------|------|-----------|-------------|
| id | string | job_requests.id | Job request ID (JR-###) |
| name | string | job_requests.name | Position name (VARCHAR 255) |
| entity_id | integer | job_requests.entity_id | Entity type FK |
| inner_client_id | integer | job_requests.inner_client_id | Internal client FK |
| profession_id | integer | job_requests.profession_id | FK to professions |
| profession_name | string | - | Denormalized profession |
| status_id | integer | job_requests.status_id | FK to statuses |
| status_name | string | - | Denormalized status |
| quantity | integer | job_requests.quantity | Number of positions |
| manager_id | integer | job_requests.manager_id | FK to users |
| manager_name | string | - | Denormalized manager name |
| rate_id | integer | job_requests.rate_id | FK to rates |
| rate_name | string | - | Denormalized rate level |
| shift_id | integer | job_requests.shift_id | FK to shifts |
| shift_name | string | - | Denormalized shift type |
| created_by | integer | job_requests.created_by | Creator user FK |
| created_at | string | job_requests.created_at | Timestamp (ISO 8601) |
| demand_date | string | job_requests.demand_date | Required start date |
| close_date | string | job_requests.close_date | Position filled date |
| sum_jas | integer | job_requests.sum_jas | Sum of job applications |
| note | string | job_requests.note | Notes (VARCHAR 2000) |
| prospect_id | string | job_requests.prospect_id | FK to prospects |
| tools | array | job_request_tool | Required tools/technologies |
| languages | array | job_request_language | Required languages |
| object_actions | array | job_request_object_action | Related actions |
| job_templates | array | job_request_job_template | Applied job templates |

**Lookup Tables Required:**
- Professions → `BUSINESSES/JobRequests/Professions/`
- Rates → `BUSINESSES/JobRequests/Rates/`
- Shifts → `BUSINESSES/JobRequests/Shifts/`
- Tools → `BUSINESSES/JobRequests/Tools/`
- Languages → `BUSINESSES/JobRequests/Languages/`
- LanguageLevels → `BUSINESSES/JobRequests/LanguageLevels/`

---

### 2.12 References Sub-Entity
Links to external systems and documents.

```json
{
  "references": {
    "crm_link": "https://crm-s.com/member/leads/1139621",
    "crm_id": "1139621",
    "dropbox_path": "/Dropbox/Clients/TIAL",
    "google_doc": "Email for Sir Geoff",
    "transcription_links": [
      "TIAL - 2025/09/19 13:49 EEST - Notes by Gemini"
    ],
    "contract_link": null,
    "proposal_link": null,
    "calendar_id": "primary"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| crm_link | string | No | Full CRM URL |
| crm_id | string | No | CRM record ID |
| dropbox_path | string | No | Dropbox folder |
| google_doc | string | No | Google Doc reference |
| transcription_links | array | No | Call transcripts |
| contract_link | string | No | Signed contract |
| proposal_link | string | No | Sent proposal |
| calendar_id | string | No | Google Calendar ID |

### 2.8 Metadata Sub-Entity
System tracking and tagging.

```json
{
  "metadata": {
    "tags": [
      "active_client",
      "hired",
      "ai_automation",
      "anastasia_portfolio",
      "high_value"
    ],
    "created_at": "2025-11-22T10:00:00Z",
    "updated_at": "2025-11-22T15:30:00Z",
    "source_file": "client_list.md",
    "source_row": 5,
    "import_batch": "2025-11-22_Sales_Import",
    "last_synced_calendar": "2025-11-22T10:00:00Z",
    "data_quality_score": 95,
    "approved": "TRUE"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| tags | array | Yes | Searchable tags |
| created_at | string | Yes | Creation timestamp |
| updated_at | string | Yes | Last update |
| source_file | string | Yes | Import source |
| source_row | number | No | Row in source file |
| import_batch | string | Yes | Import batch ID |
| last_synced_calendar | string | No | Calendar sync time |
| data_quality_score | number | No | 0-100 quality score |
| approved | string | Yes | Approval status |

### 2.9 Complete Entity Example

```json
{
  "company_details": {
    "company_id": "BUS-2025-001",
    "company_name": "TIAL (The Institutional Architecture Lab)",
    "website": "https://tial.org",
    "industry": "AI",
    "sub_industry": "Research & Development",
    "country": "USA",
    "city": "New York",
    "company_size": "50-100",
    "founded_year": 2018,
    "description": "AI research and consulting firm"
  },
  "interests": {
    "services_of_interest": ["Lead Generation", "AI/Automation"],
    "specific_needs": ["Need Python developer for AI project"],
    "budget_info": {
      "budget_mentioned": true,
      "estimated_value": 5000,
      "currency": "USD",
      "payment_terms": "monthly"
    },
    "urgency_level": "high",
    "timeline": "Q1 2025",
    "decision_criteria": ["Technical expertise"]
  },
  "contact_details": {
    "primary_contact": {
      "name": "Sir Geoff Mulgan",
      "title": "CEO",
      "email": "gjmulgan@gmail.com",
      "phone": null,
      "linkedin": null
    },
    "additional_contacts": [],
    "preferred_contact_method": "email",
    "best_time_to_contact": null
  },
  "communication_history": {
    "total_interactions": 2,
    "first_contact": "2025-09-19",
    "last_contact": "2025-10-08",
    "interactions": [],
    "emails_sent": 1,
    "calls_completed": 2,
    "meetings_held": 0
  },
  "relationship_status": {
    "entity_type": "Client",
    "status": "Active_Client",
    "pipeline_stage": "Won_Closed",
    "relationship_health": "Strong",
    "relationship_start": "2025-09-19",
    "account_manager": "Kovalska_Anastasiya",
    "lifetime_value": 0,
    "current_monthly_revenue": 0,
    "next_action": "Follow up next week",
    "next_action_date": null,
    "risk_level": null,
    "satisfaction_score": null
  },
  "references": {
    "crm_link": "https://crm-s.com/member/leads/1139621",
    "crm_id": "1139621",
    "dropbox_path": "/Dropbox/Clients/TIAL",
    "google_doc": "Email for Sir Geoff",
    "transcription_links": ["TIAL - 2025/09/19 13:49 EEST - Notes by Gemini"],
    "contract_link": null,
    "proposal_link": null,
    "calendar_id": null
  },
  "metadata": {
    "tags": ["active_client", "hired", "ai_automation", "anastasia_portfolio"],
    "created_at": "2025-11-22T10:00:00Z",
    "updated_at": "2025-11-22T10:00:00Z",
    "source_file": "client_list.md",
    "source_row": 5,
    "import_batch": "2025-11-22_Sales_Import",
    "last_synced_calendar": null,
    "data_quality_score": 85,
    "approved": "TRUE"
  }
}
```

---

## 3. Field Classification System

### 2.1 Source Fields (client_list.md)
15 columns to classify:

| Field | Classification | Used For |
|-------|---------------|----------|
| Client Company | Identity | Primary key, company lookup |
| CRM Link | Reference | External system link |
| Transcription Link | Reference | Supporting document |
| Google Doc | Reference | Supporting document |
| Dropbox | Reference | File location |
| Client Name | Contact | Decision maker info |
| Email | Contact | Communication |
| Status | Lifecycle | Entity categorization |
| Comments | Metadata Source | Tags, interests, budget, urgency |
| To Do | Metadata Source | Next actions, urgency |
| Last Contact Day | Relationship | Health score, recency |
| Date | Relationship | Relationship start |
| Sales Manager | Assignment | Account manager |
| Approved | Workflow | Approval status |
| Email Content | Communication | Template, interests |

### 2.2 Field Chunks

#### Chunk 1: Identity Fields
Purpose: Uniquely identify the company
```
- Client Company → company_name
- CRM Link → crm_link (for cross-reference)
```

#### Chunk 2: Contact Fields
Purpose: Store decision maker information
```
- Client Name → decision_makers[0].name
- Email → decision_makers[0].email
```

#### Chunk 3: Reference Fields
Purpose: Link to external documents
```
- CRM Link → crm_link
- Transcription Link → transcription_link
- Google Doc → google_doc
- Dropbox → dropbox_path
```

#### Chunk 4: Lifecycle Fields
Purpose: Determine entity category and status
```
- Status → status (normalized)
- Comments → used for categorization logic
```

#### Chunk 5: Relationship Fields
Purpose: Track relationship health and timeline
```
- Last Contact Day → last_contact
- Date → relationship_start
- Sales Manager → account_manager
```

#### Chunk 6: Metadata Source Fields
Purpose: Extract tags, interests, budget, urgency
```
- Comments → multiple derived fields
- To Do → next_action, urgency_level
- Email Content → services_of_interest, budget_info
```

#### Chunk 7: Workflow Fields
Purpose: Track processing status
```
- Approved → approved
```

### 2.3 Derived Metadata from Field Chunks

From **Comments** field, extract:
- `services_of_interest[]` - via keyword matching
- `budget_info{}` - via budget keyword detection
- `tags[]` - auto-generated from content
- `sub_entity` - categorization indicator

From **To Do** field, extract:
- `next_action` - direct mapping
- `urgency_level` - via urgency keyword detection
- `next_actions[]` - structured action items

From **Email Content** field, extract:
- `services_of_interest[]` - additional service mentions
- `budget_info{}` - budget discussions
- `communication_history[]` - email as history entry

From **Last Contact Day** + **Status**, calculate:
- `relationship_health` - Strong/Moderate/Weak
- `last_contact_details{}` - days_ago, recency

---

## 3. Future Integration: Google Calendar

### 3.1 Purpose
Enrich entity data with call metadata from Google Calendar events.

### 3.2 Calendar Data Points to Capture

| Field | Description | Maps To |
|-------|-------------|---------|
| Event Title | Call subject | communication_history[].summary |
| Event Date/Time | When call occurred | communication_history[].date |
| Duration | Call length | communication_history[].duration_minutes |
| Attendees | Who was on call | decision_makers[], attendees |
| Description | Call notes/agenda | communication_history[].notes |
| Meeting Link | Zoom/Meet URL | communication_history[].meeting_link |
| Recurrence | Regular meetings | meeting_frequency |
| Location | In-person/Remote | communication_history[].type |

### 3.3 Schema Fields for Calendar Integration

#### New Fields to Add
```json
{
  "calendar_data": {
    "last_synced": "2025-11-22T10:00:00Z",
    "calendar_id": "primary",
    "total_events": 5
  },
  "communication_history": [
    {
      "date": "2025-11-20",
      "time": "14:00",
      "type": "Call",
      "source": "google_calendar",
      "event_id": "abc123",
      "summary": "Discovery Call - TIAL",
      "duration_minutes": 30,
      "attendees": [
        "sales@company.com",
        "client@tial.com"
      ],
      "meeting_link": "https://meet.google.com/xxx",
      "notes": "Discussed lead generation needs",
      "outcome": "Scheduled follow-up"
    }
  ],
  "meeting_frequency": "weekly",
  "next_scheduled_call": "2025-11-25T14:00:00Z",
  "total_calls": 5,
  "average_call_duration": 35
}
```

### 3.4 Matching Logic
Match calendar events to companies by:
1. Company name in event title
2. Contact email in attendees
3. CRM link in event description
4. Manual mapping in config

```python
def match_event_to_company(event, companies):
    """Match calendar event to company entity"""

    # Match by title
    title = event['summary'].lower()
    for company in companies:
        if company['company_name'].lower() in title:
            return company['company_id']

    # Match by attendee email
    attendees = [a['email'] for a in event.get('attendees', [])]
    for company in companies:
        for dm in company.get('decision_makers', []):
            if dm.get('email') in attendees:
                return company['company_id']

    return None
```

### 3.5 Implementation Phases

#### Phase A: Schema Preparation (Current)
- Add calendar-related fields to schema
- Design communication_history structure
- Plan data flow

#### Phase B: Calendar API Setup (Future)
- Google Calendar API authentication
- Service account or OAuth setup
- Permission scopes

#### Phase C: Event Extraction (Future)
- Query calendar for events
- Filter by date range
- Extract relevant fields

#### Phase D: Entity Enrichment (Future)
- Match events to companies
- Update communication_history
- Calculate meeting metrics

### 3.6 Placeholder Fields in Current Import
Include these fields now (empty) for future population:
- `calendar_data: null`
- `meeting_frequency: null`
- `next_scheduled_call: null`
- `total_calls: 0`
- `average_call_duration: null`

---

## 4. Data Flow & Dependencies

### 4.1 Dependency Chain
```
Phase 0: Cleanup (archive existing BUSINESSES data)
    ↓
Phase 1: Schema Definition (define target structure)
    ↓
Phase 2: Field Classification (classify source → target)
    ↓
Phase 3: Data Extraction (read-only from sources)
    ↓
Phase 4: Metadata Tagging (apply tagging logic)
    ↓
Phase 5: Categorization (assign Client/Prospect/Ex_Client)
    ↓
Phase 6: ID Generation (deduplicate, assign IDs)
    ↓
Phase 7: JSON Generation (create files)
    ↓
Phase 8: Validation (verify quality)
    ↓
Phase 9: Documentation (generate docs)
```

### 4.2 Processing Registry
Track all processed records:
```
IMPORTS/2025-11-22_Sales_Import/processing_registry.json
```

---

## 5. Phase 0: Cleanup

### 5.1 Purpose
Archive existing BUSINESSES entity data to start fresh.

### 5.2 What to Archive
Move to `IMPORTS/2025-11-22_Sales_Import/archive_previous/`:
- `BUSINESSES/Clients/*.json`
- `BUSINESSES/Prospects/*.json`
- `BUSINESSES/Ex_Clients/*.json`
- `BUSINESSES/BUSINESSES_Master.json`
- `BUSINESSES/*_INDEX.json`

### 5.3 What to Keep (Do NOT Archive)
- `BUSINESSES/Products/` - Product library
- `BUSINESSES/Services/` - Service definitions
- `BUSINESSES/README.md` - Documentation
- `BUSINESSES/USER_GUIDE_BUSINESSES.md` - User guide
- `BUSINESSES/schemas/` - Schema files (to be created)

### 5.4 Output
- `archive_previous/` - Backed up files
- `phase0_cleanup_report.md`

---

## 6. Phase 1: Schema Definition

### 6.1 Purpose
Define the formal JSON schema structure with calendar integration support.

### 6.2 Complete Schema Field Groups

#### Group 1: Core Identity (Required)
| Field | Type | Description |
|-------|------|-------------|
| entity_type | string | Always "BUSINESSES" |
| sub_entity | string | Client / Prospect / Ex_Client |
| company_id | string | BUS-YYYY-### format |
| company_name | string | Company name |

#### Group 2: Contact Information
| Field | Type | Description |
|-------|------|-------------|
| decision_makers | array | Contact persons |
| decision_makers[].name | string | Full name |
| decision_makers[].title | string | Job title |
| decision_makers[].email | string | Email address |
| decision_makers[].phone | string | Phone number |

#### Group 3: Company Profile
| Field | Type | Description |
|-------|------|-------------|
| industry | string | Business sector |
| company_size | string | Employee range |
| location | string | Geographic location |
| website | string | Company website |

#### Group 4: Relationship Data
| Field | Type | Description |
|-------|------|-------------|
| status | string | Pipeline status |
| relationship_start | string | First contact date |
| last_contact | string | Most recent contact |
| relationship_health | string | Strong/Moderate/Weak |
| account_manager | string | Assigned manager |

#### Group 5: Financial Information
| Field | Type | Description |
|-------|------|-------------|
| lifetime_value | number | Total revenue |
| current_monthly_revenue | number | Monthly revenue |
| budget_info | object | Budget details |

#### Group 6: Service Interests
| Field | Type | Description |
|-------|------|-------------|
| services_of_interest | array | Services they want |
| active_projects | array | Current projects |
| urgency_level | string | high/medium/normal/low |

#### Group 7: Communication (Calendar-Ready)
| Field | Type | Description |
|-------|------|-------------|
| communication_history | array | Contact history (manual + calendar) |
| communication_history[].date | string | YYYY-MM-DD |
| communication_history[].time | string | HH:MM (from calendar) |
| communication_history[].type | string | Call/Email/Meeting |
| communication_history[].source | string | manual/google_calendar |
| communication_history[].event_id | string | Calendar event ID |
| communication_history[].summary | string | Brief description |
| communication_history[].duration_minutes | number | Call length |
| communication_history[].attendees | array | Email addresses |
| communication_history[].meeting_link | string | Zoom/Meet URL |
| communication_history[].notes | string | Discussion notes |
| communication_history[].outcome | string | Result of interaction |
| notes | string | Internal notes |
| email_content | string | Last email sent |
| next_action | string | Next step |
| next_actions | array | Structured actions |

#### Group 8: Calendar Metadata (Future)
| Field | Type | Description |
|-------|------|-------------|
| calendar_data | object | Calendar sync info |
| calendar_data.last_synced | string | Last sync timestamp |
| calendar_data.calendar_id | string | Google calendar ID |
| calendar_data.total_events | number | Events found |
| meeting_frequency | string | weekly/biweekly/monthly/adhoc |
| next_scheduled_call | string | ISO datetime |
| total_calls | number | Total calls count |
| average_call_duration | number | Minutes |

#### Group 9: References
| Field | Type | Description |
|-------|------|-------------|
| crm_link | string | CRM URL |
| dropbox_path | string | Dropbox path |
| google_doc | string | Google Doc ref |
| transcription_link | string | Transcript ref |

#### Group 10: Metadata
| Field | Type | Description |
|-------|------|-------------|
| tags | array | Searchable tags |
| created_at | string | Creation timestamp |
| updated_at | string | Update timestamp |
| source_file | string | Import source |
| approved | string | Approval status |

### 6.3 Output Files
- `BUSINESSES/schemas/BUSINESSES_SCHEMA.json`
- `BUSINESSES/schemas/field_groups.md`
- `BUSINESSES/schemas/calendar_integration.md`

---

## 7. Phase 2: Field Classification & Mapping

### 7.1 Purpose
Classify source fields and define mapping rules.

### 7.2 Mapping Table

| Source Column | Target Field(s) | Transform | Validation |
|---------------|-----------------|-----------|------------|
| Client Company | company_name | trim, normalize | Required, non-empty |
| Client Name | decision_makers[0].name | split name | Optional |
| Email | decision_makers[0].email | lowercase | Email format |
| Status | status | normalize_status() | Enum value |
| Comments | notes, tags, services_of_interest, budget_info | multiple | None |
| To Do | next_action, urgency_level | parse_todo() | None |
| Last Contact Day | last_contact | parse_date() | Date format |
| Date | relationship_start | parse_date() | Date format |
| Sales Manager | account_manager | normalize_name() | None |
| Approved | approved | uppercase | TRUE/FALSE |
| Email Content | email_content, services_of_interest | extract | None |
| CRM Link | crm_link | none | URL format |
| Transcription Link | transcription_link | none | None |
| Google Doc | google_doc | none | None |
| Dropbox | dropbox_path | none | None |

### 7.3 Output Files
- `mapping_rules.json`
- `transformation_functions.md`
- `field_classification_report.md`

---

## 8. Phase 3: Data Extraction (Read-Only)

### 8.1 Purpose
Extract data from sources WITHOUT modifying them.

### 8.2 Sources to Read

#### Primary: client_list.md
- Location: `Nov25/Sales Nov25/client_list.md`
- Action: Parse markdown table, extract all rows
- Track: Record source_file and row number

#### Secondary: Oct25 Client Folders
- Location: `Nov25/Sales Nov25/Sales_Oct25/Clients/*/`
- Action: List folders, extract company names
- Track: Which folders have been processed

#### Tertiary: Call Transcripts
- Location: `Nov25/Sales Nov25/pre call templates/.../first call transcripts/`
- Action: Match transcript to company by name

### 8.3 Output Files
- `raw_extracted_data.json`
- `processing_registry.json`
- `extraction_report.md`

---

## 9. Phase 4: Metadata Tagging Logic

### 9.1 Purpose
Apply tagging rules to derive metadata from source fields.

### 9.2 Service Interest Tags

| Pattern | Tag | Service |
|---------|-----|---------|
| "lg", "lead gen" | lead_generation | Lead Generation |
| "design", "graphic" | design_services | Design |
| "developer", "dev" | development | Development |
| "ai", "automation" | ai_automation | AI/Automation |
| "content", "copy" | content_services | Content |
| "seo" | seo_services | SEO |
| "smm", "social" | social_media | Social Media |
| "video", "youtube" | video_services | Video |
| "va", "virtual" | virtual_assistant | Virtual Assistant |
| "marketing", "ads" | marketing_services | Marketing |

### 9.3 Status Tags

| Condition | Tag |
|-----------|-----|
| status = Active_Client | active_client |
| status = Active_Outreach | active_prospect |
| comments contains "hired" | hired |
| comments contains "interview" | interview_stage |

### 9.4 Output Files
- `enriched_data.json`
- `tagging_rules_applied.json`
- `metadata_report.md`

---

## 10. Phase 5: Entity Categorization

### 10.1 Decision Tree

```
Comments contains "hired"? → Client
Comments contains "stopped"? → Ex_Client
Status = "sent"? → Prospect (Active_Outreach)
Default → Prospect
```

### 10.2 Output Files
- `categorized_entities.json`
- `categorization_decisions.json`
- `categorization_report.md`

---

## 11. Phase 6: ID Generation & Tracking

### 11.1 ID Format
`BUS-2025-###`

### 11.2 Deduplication
Normalize company names, merge duplicate records.

### 11.3 Output Files
- `deduplicated_entities.json`
- `id_registry.json`
- `duplicate_report.md`

---

## 12. Phase 7: JSON Generation

### 12.1 File Naming
`BUSINESSES_[Type]_[CompanyName]_[ID].json`

### 12.2 Directory Structure
```
BUSINESSES/
├── Clients/
├── Prospects/
├── Ex_Clients/
└── BUSINESSES_Master.json
```

### 12.3 Output Files
- Individual entity JSON files
- Category index files
- `BUSINESSES_Master.json`
- `generation_report.md`

---

## 13. Phase 8: Validation

### 13.1 Checks
- Schema compliance
- Required fields
- Data types
- ID uniqueness

### 13.2 Output Files
- `validation_report.md`
- `quality_metrics.json`
- `issues_log.json`

---

## 14. Phase 9: Documentation

### 14.1 Output Files
- Updated `USER_GUIDE_BUSINESSES.md`
- `ENTITIES/PROMPTS/BUSINESSES_IMPORT_PROMPT_v2.md`
- `FINAL_IMPORT_SUMMARY.md`

---

## 15. Success Criteria

### 15.1 Quantity
- Total entities: 50+
- Clients: 5+
- Prospects: 40+

### 15.2 Quality
- Schema compliance: 100%
- Required fields: 100%
- Completeness: 85%+

---

## 16. Error Handling

### 16.1 Principles
- Log all errors
- Continue processing where possible
- Track failures in issues log
- Never modify source files

---

*End of Technical Specification*
