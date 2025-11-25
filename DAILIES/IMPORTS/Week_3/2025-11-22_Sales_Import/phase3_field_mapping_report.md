# Phase 3: Field Classification & Mapping Report

**Executed:** 2025-11-22T21:07:56.780789
**Status:** Completed

## Summary

- **Sub-Entities Mapped:** 7
- **Transformation Functions:** 11
- **Unmapped Fields:** 113

## Field Mapping Overview

| Sub-Entity | Fields Mapped | Source Types |
|------------|---------------|---------------|
| company | 9 | company_name, generated, lead_company_city, lead_company_size.id, lead_company_size.title, multiple, not_available, website |
| pocs | 9 | generated, pocs[].email, pocs[].is_primary, pocs[].linkedin_url, pocs[].name, pocs[].notes, pocs[].phone, pocs[].position.id, pocs[].position.title |
| business_relationship | 6 | derived, lead_source.id, lead_source.name, lead_status.id, lead_status.priority, lead_status.type |
| communication_history | 3 | calculated, communications[], communications[].created_at |
| assigned_users | 5 | created_by.id, created_by.name, lead_agent.id, sales_manager, sales_manager_assistant.name |
| references | 3 | calculated, client_id, generated |
| metadata | 7 | calculated, constant, derived, generated, tracking |

## Transformation Functions

### normalize_company_name

**Description:** Clean and normalize company name

**Input:** string

**Output:** string

**Logic:**
- Trim whitespace
- Remove special characters (except spaces, hyphens, apostrophes)
- Title case each word
- Handle common abbreviations (LLC, Inc, Ltd)

**Example:** "ACME Corp. " → "Acme Corp"

### generate_company_id

**Description:** Generate unique company ID

**Input:** none

**Output:** string

**Logic:**
- Format: BUS-YYYY-###
- YYYY = current year (2025)
- ### = sequential 3-digit number
- Check uniqueness in registry

**Example:** → "BUS-2025-001"

### generate_poc_id

**Description:** Generate unique POC ID

**Input:** none

**Output:** string

**Logic:**
- Format: POC-###
- ### = sequential 3-digit number
- Check uniqueness in registry

**Example:** → "POC-001"

### normalize_email

**Description:** Validate and normalize email address

**Input:** string

**Output:** string

**Logic:**
- Convert to lowercase
- Trim whitespace
- Validate format (basic regex)
- Return null if invalid

**Example:** "John.Doe@Example.COM " → "john.doe@example.com"

### clean_url

**Description:** Clean and validate URL

**Input:** string

**Output:** string

**Logic:**
- Trim whitespace
- Add https:// if no protocol
- Remove trailing slashes
- Validate basic URL format

**Example:** "linkedin.com/company/acme" → "https://linkedin.com/company/acme"

### classify_entity_type

**Description:** Classify as Client/Prospect/Ex_Client

**Input:** record object

**Output:** string

**Logic:**
- Check for job_requests → Client
- Check lead_status.type == 'Client' → Client
- Check notes for 'hired' → Client
- Check notes for 'stopped' → Ex_Client
- Default → Prospect

**Example:** record with job_requests → "Client"

### derive_tags

**Description:** Extract tags from record data

**Input:** record object

**Output:** array of strings

**Logic:**
- Scan notes for keywords: 'urgent', 'hired', 'lead gen', 'dev', 'ai'
- Add industry as tag
- Add entity_type as tag
- Add lead_status.type as tag

**Example:** notes: 'urgent dev needs' → ['urgent', 'development', 'active_prospect']

### calculate_quality_score

**Description:** Calculate data completeness score

**Input:** record object

**Output:** integer (0-100)

**Logic:**
- Count total fields in schema
- Count non-null fields in record
- Score = (filled / total) * 100

**Example:** 15/20 fields filled → 75

### extract_locations

**Description:** Extract company locations from city data

**Input:** lead_company_city object

**Output:** array of location objects

**Logic:**
- Map city_id, city_name from lead_company_city
- Map country_id, country_name from city.country
- Set is_primary = true for main location

**Example:** city object → [{city_id: 123, city_name: 'NYC', country_id: 1, is_primary: true}]

### extract_industries

**Description:** Extract industries and sub-industries

**Input:** lead_company_industry, sub_industries array

**Output:** array of industry objects

**Logic:**
- Map industry_id, industry_name from lead_company_industry
- Iterate sub_industries array
- Map sub_industry_id, sub_industry_name for each
- Return combined array

**Example:** industry + 2 sub_industries → [{industry_id: 20, industry_name: 'Finance', sub_industry_id: 114, sub_industry_name: 'Financial Services'}]

### parse_iso_date

**Description:** Parse date to ISO 8601 format

**Input:** string (various formats)

**Output:** string (ISO 8601)

**Logic:**
- Try parsing common formats: YYYY-MM-DD, MM/DD/YYYY, DD.MM.YYYY
- Add T00:00:00Z for dates without time
- Return null if unparseable

**Example:** "2025-11-22" → "2025-11-22T00:00:00Z"


## Unmapped Fields (First 50)

- `company_id`
- `user_id`
- `countries_id`
- `size_id`
- `account_id`
- `industry_id`
- `email_notifications`
- `lead_status_id`
- `type_id`
- `placement_id`
- `verified`
- `lg_manager_id`
- `status_id`
- `image_url`
- `user`
- `user.id`
- `user.name`
- `user.email`
- `user.image_url`
- `project_companies`
- `project_companies[].id`
- `project_companies[].company_id`
- `project_companies[].name`
- `project_companies[].short_name`
- `project_companies[].updated_at`
- `project_companies[].pivot`
- `project_companies[].pivot.client_details_id`
- `project_companies[].pivot.project_id`
- `lead_account`
- `lead_account.id`
- `lead_account.company_id`
- `lead_account.project_company_id`
- `lead_account.name`
- `lead_account.link`
- `lead_account.connections`
- `lead_account.premium`
- `lead_account.linked_login`
- `lead_account.linked_password`
- `lead_account.email_login`
- `lead_account.email_password`
- `lead_account.passport_link`
- `lead_account.created_date`
- `lead_account.agent_id`
- `lead_account.status_id`
- `lead_account.country_id`
- `lead_account.source_id`
- `lead_account.placement_id`
- `lead_account.is_approved_manager`
- `lead_account.created_at`
- `lead_account.updated_at`

## Next Step

Proceed to **Phase 4: Data Extraction**
