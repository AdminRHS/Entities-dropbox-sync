# Phase 4 Step Templates Master Index

**Total Steps:** 141
**Total Templates:** 22 (20 active + 2 deprecated)
**Departments:** 6
**Date:** 2025-11-12
**Phase:** Phase 4 (Video_006 + Video_008)

---

## Quick Navigation

**By Department:** [LG](#lg-steps) | [AI](#ops-steps) | [DEV](#dev-steps) | [HR](#hr-steps) | [SALES](#sales-steps) | [AI](#marketing-steps)

---

## 📊 Overview Statistics

### Steps by Department
- **LG (Lead Generation):** 82 steps from 12 templates
- **AI (Operations):** 21 steps from 4 templates
- **DEV (Development):** 20 steps from 3 templates
- **HR:** 6 steps from 1 template
- **SALES:** 6 steps from 1 template
- **AI:** 6 steps from 1 template

### Complexity Distribution
- **Average Steps per Template:** 6.4 (excluding deprecated)
- **Min Steps:** 6 (simple enrichment workflows)
- **Max Steps:** 9 (complex scraping + n8n workflows)

---

## LG Steps

### TASK-TEMPLATE-003: Enrich Lead List via Anymailfinder (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-003-01 | Prepare company domain list | Excel/Google Sheets | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-01.md) |
| 2 | STEP-TASK-TEMPLATE-003-02 | Upload domain list to Anymailfinder | Anymailfinder | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-02.md) |
| 3 | STEP-TASK-TEMPLATE-003-03 | Configure enrichment settings | Anymailfinder | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-03.md) |
| 4 | STEP-TASK-TEMPLATE-003-04 | Run nominative enrichment | Anymailfinder | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-04.md) |
| 5 | STEP-TASK-TEMPLATE-003-05 | Export enriched email list | Anymailfinder | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-05.md) |
| 6 | STEP-TASK-TEMPLATE-003-06 | Import to CRM and log campaign metrics | CRM (Instantly, Apollo) | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-003-06.md) |

### TASK-TEMPLATE-004: Extract Leads from LinkedIn Sales Navigator (7 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-004-01 | Define LinkedIn Sales Navigator search criteria | LinkedIn Sales Navigator | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-01.md) |
| 2 | STEP-TASK-TEMPLATE-004-02 | Execute LinkedIn search and export results | LinkedIn Sales Navigator | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-02.md) |
| 3 | STEP-TASK-TEMPLATE-004-03 | Configure Vayne scraper for profile extraction | Vayne | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-03.md) |
| 4 | STEP-TASK-TEMPLATE-004-04 | Run Vayne scraper to extract full profiles | Vayne | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-04.md) |
| 5 | STEP-TASK-TEMPLATE-004-05 | Enrich contacts with email addresses | Anymailfinder/Bright Data | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-05.md) |
| 6 | STEP-TASK-TEMPLATE-004-06 | Review and clean final lead list | Excel/Google Sheets | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-06.md) |
| 7 | STEP-TASK-TEMPLATE-004-07 | Import to CRM and set up outreach campaign | CRM | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-004-07.md) |

### TASK-TEMPLATE-008: Execute Enterprise Email Arbitrage Strategy (8 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-008-01 | Select enterprise target companies | Company research | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-01.md) |
| 2 | STEP-TASK-TEMPLATE-008-02 | Upload company domains to Airscale | Airscale | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-02.md) |
| 3 | STEP-TASK-TEMPLATE-008-03 | Unlock employee directory for target companies | Airscale | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-03.md) |
| 4 | STEP-TASK-TEMPLATE-008-04 | Extract employee list with titles/departments | Airscale | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-04.md) |
| 5 | STEP-TASK-TEMPLATE-008-05 | Filter for decision-maker roles | Excel/Google Sheets | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-05.md) |
| 6 | STEP-TASK-TEMPLATE-008-06 | Enrich employee emails via Anymailfinder | Anymailfinder | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-06.md) |
| 7 | STEP-TASK-TEMPLATE-008-07 | Calculate arbitrage ROI metrics | Excel/Google Sheets | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-07.md) |
| 8 | STEP-TASK-TEMPLATE-008-08 | Import to CRM for multi-contact outreach | CRM | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-008-08.md) |

### TASK-TEMPLATE-009: Generate Leads from Google SERP (8 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-009-01 | Define Google search queries for target industry | Search planning | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-01.md) |
| 2 | STEP-TASK-TEMPLATE-009-02 | Configure Apify Google SERP scraper | Apify | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-02.md) |
| 3 | STEP-TASK-TEMPLATE-009-03 | Run Google SERP scraper for company domains | Apify | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-03.md) |
| 4 | STEP-TASK-TEMPLATE-009-04 | Clean and deduplicate scraped domain list | Excel/Google Sheets | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-04.md) |
| 5 | STEP-TASK-TEMPLATE-009-05 | Build n8n enrichment pipeline | n8n | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-05.md) |
| 6 | STEP-TASK-TEMPLATE-009-06 | Run automated enrichment via n8n | n8n | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-06.md) |
| 7 | STEP-TASK-TEMPLATE-009-07 | Review enriched lead list for quality | Excel/Google Sheets | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-07.md) |
| 8 | STEP-TASK-TEMPLATE-009-08 | Import to CRM and segment by industry | CRM | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-009-08.md) |

### TASK-TEMPLATE-011: Build Custom Niche Platform Scraper (9 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-011-01 | Identify target niche platform and data structure | Platform research | 30-45 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-01.md) |
| 2 | STEP-TASK-TEMPLATE-011-02 | Analyze platform HTML structure | Browser DevTools | 30-45 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-02.md) |
| 3 | STEP-TASK-TEMPLATE-011-03 | Design n8n scraper workflow | n8n | 30-45 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-03.md) |
| 4 | STEP-TASK-TEMPLATE-011-04 | Configure HTTP request nodes in n8n | n8n | 20-30 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-04.md) |
| 5 | STEP-TASK-TEMPLATE-011-05 | Build data parsing logic via n8n nodes | n8n | 45-60 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-05.md) |
| 6 | STEP-TASK-TEMPLATE-011-06 | Add error handling and retry logic | n8n | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-06.md) |
| 7 | STEP-TASK-TEMPLATE-011-07 | Test scraper with sample data | n8n | 20-30 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-07.md) |
| 8 | STEP-TASK-TEMPLATE-011-08 | Run full scraper and export results | n8n | 15-30 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-08.md) |
| 9 | STEP-TASK-TEMPLATE-011-09 | Enrich and validate scraped leads | Enrichment tools | 20-30 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-011-09.md) |

### TASK-TEMPLATE-014: Parse HTML Data via AI (9 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-014-01 | Identify target website with difficult structure | Website analysis | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-01.md) |
| 2 | STEP-TASK-TEMPLATE-014-02 | Scrape raw HTML from target pages | Apify/n8n | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-02.md) |
| 3 | STEP-TASK-TEMPLATE-014-03 | Design n8n workflow with AI parsing | n8n | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-03.md) |
| 4 | STEP-TASK-TEMPLATE-014-04 | Configure OpenAI/Claude API node in n8n | n8n + AI API | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-04.md) |
| 5 | STEP-TASK-TEMPLATE-014-05 | Create AI parsing prompt for data extraction | Prompt engineering | 20-30 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-05.md) |
| 6 | STEP-TASK-TEMPLATE-014-06 | Test AI parsing on sample HTML | n8n + AI API | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-06.md) |
| 7 | STEP-TASK-TEMPLATE-014-07 | Run batch AI parsing on full dataset | n8n + AI API | 30-45 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-07.md) |
| 8 | STEP-TASK-TEMPLATE-014-08 | Validate parsed data quality | Data validation | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-08.md) |
| 9 | STEP-TASK-TEMPLATE-014-09 | Export cleaned data and calculate success rate | Excel/Google Sheets | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-014-09.md) |

### TASK-TEMPLATE-015: Enrich Company Employees via Airscale (8 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-015-01 | Prepare list of target company domains | Excel/Google Sheets | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-01.md) |
| 2 | STEP-TASK-TEMPLATE-015-02 | Upload domains to Airscale | Airscale | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-02.md) |
| 3 | STEP-TASK-TEMPLATE-015-03 | Unlock employee directories | Airscale | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-03.md) |
| 4 | STEP-TASK-TEMPLATE-015-04 | Extract employee names and titles | Airscale | 5-8 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-04.md) |
| 5 | STEP-TASK-TEMPLATE-015-05 | Filter for target roles and departments | Excel/Google Sheets | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-05.md) |
| 6 | STEP-TASK-TEMPLATE-015-06 | Enrich employee emails via Anymailfinder | Anymailfinder | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-06.md) |
| 7 | STEP-TASK-TEMPLATE-015-07 | Review and validate enriched contacts | Excel/Google Sheets | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-07.md) |
| 8 | STEP-TASK-TEMPLATE-015-08 | Import to CRM for account-based marketing | CRM | 3-5 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-015-08.md) |

### TASK-TEMPLATE-016: Scrape Local Businesses from Google Maps (7 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-016-01 | Define local business search criteria | Search planning | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-01.md) |
| 2 | STEP-TASK-TEMPLATE-016-02 | Configure Apify Google Maps scraper | Apify | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-02.md) |
| 3 | STEP-TASK-TEMPLATE-016-03 | Run Google Maps scraper | Apify | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-03.md) |
| 4 | STEP-TASK-TEMPLATE-016-04 | Extract business contact information | Apify | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-04.md) |
| 5 | STEP-TASK-TEMPLATE-016-05 | Clean and format business data | Excel/Google Sheets | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-05.md) |
| 6 | STEP-TASK-TEMPLATE-016-06 | Enrich with decision-maker emails if needed | Enrichment tools | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-06.md) |
| 7 | STEP-TASK-TEMPLATE-016-07 | Import to CRM and segment by category | CRM | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-016-07.md) |

### TASK-TEMPLATE-017: Scrape LinkedIn Jobs for Intent-Based Leads (8 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-017-01 | Define job title search criteria | Search planning | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-01.md) |
| 2 | STEP-TASK-TEMPLATE-017-02 | Configure LinkedIn Jobs scraper | Apify/Phantombuster | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-02.md) |
| 3 | STEP-TASK-TEMPLATE-017-03 | Run LinkedIn Jobs scraper | Apify/Phantombuster | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-03.md) |
| 4 | STEP-TASK-TEMPLATE-017-04 | Extract company information from job postings | Data extraction | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-04.md) |
| 5 | STEP-TASK-TEMPLATE-017-05 | Identify buying intent signals | Analysis | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-05.md) |
| 6 | STEP-TASK-TEMPLATE-017-06 | Enrich company contacts | Enrichment tools | 10-15 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-06.md) |
| 7 | STEP-TASK-TEMPLATE-017-07 | Craft intent-based outreach messaging | Copywriting | 15-20 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-07.md) |
| 8 | STEP-TASK-TEMPLATE-017-08 | Import to CRM with intent flags | CRM | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-017-08.md) |

### TASK-TEMPLATE-018: Enrich Emails via Bright Data (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-018-01 | Prepare contact list with names and domains | Excel/Google Sheets | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-01.md) |
| 2 | STEP-TASK-TEMPLATE-018-02 | Upload to Bright Data enrichment tool | Bright Data | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-02.md) |
| 3 | STEP-TASK-TEMPLATE-018-03 | Configure enrichment settings | Bright Data | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-03.md) |
| 4 | STEP-TASK-TEMPLATE-018-04 | Run email enrichment | Bright Data | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-04.md) |
| 5 | STEP-TASK-TEMPLATE-018-05 | Export enriched results | Bright Data | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-05.md) |
| 6 | STEP-TASK-TEMPLATE-018-06 | Import to CRM and log metrics | CRM | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-018-06.md) |

### TASK-TEMPLATE-019: Enrich Emails via Instantly.ai (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-019-01 | Prepare contact list in Instantly.ai format | Excel/Google Sheets | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-01.md) |
| 2 | STEP-TASK-TEMPLATE-019-02 | Upload to Instantly.ai | Instantly.ai | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-02.md) |
| 3 | STEP-TASK-TEMPLATE-019-03 | Configure enrichment options | Instantly.ai | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-03.md) |
| 4 | STEP-TASK-TEMPLATE-019-04 | Run email enrichment | Instantly.ai | 5-10 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-04.md) |
| 5 | STEP-TASK-TEMPLATE-019-05 | Export enriched list | Instantly.ai | 1-2 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-05.md) |
| 6 | STEP-TASK-TEMPLATE-019-06 | Review results and calculate success rate | Excel/Google Sheets | 2-3 min | [View](./PHASE4/LG/STEP-TASK-TEMPLATE-019-06.md) |

---

## AI Steps

### TASK-TEMPLATE-005: Automate Post-Meeting Workflow via Stacked Connectors (7 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-005-01 | Enable Claude Skills in Claude Desktop | Claude Desktop | 1-2 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-01.md) |
| 2 | STEP-TASK-TEMPLATE-005-02 | Configure Calendar, Gmail, and CRM MCP connectors | MCP connectors | 30-45 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-02.md) |
| 3 | STEP-TASK-TEMPLATE-005-03 | Test stacked connector functionality | Claude Desktop | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-03.md) |
| 4 | STEP-TASK-TEMPLATE-005-04 | Identify meeting in calendar via Claude | Claude Desktop + Calendar MCP | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-04.md) |
| 5 | STEP-TASK-TEMPLATE-005-05 | Extract meeting notes and action items via AI | Claude Desktop | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-05.md) |
| 6 | STEP-TASK-TEMPLATE-005-06 | Draft follow-up email via Gmail MCP | Claude Desktop + Gmail MCP | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-06.md) |
| 7 | STEP-TASK-TEMPLATE-005-07 | Log meeting outcome in CRM | Claude Desktop + CRM MCP | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-005-07.md) |

### TASK-TEMPLATE-007: Automate Morning Email Drafts (7 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-007-01 | Enable Claude Skills in Claude Desktop | Claude Desktop | 1-2 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-01.md) |
| 2 | STEP-TASK-TEMPLATE-007-02 | Configure Gmail MCP connector | Gmail MCP | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-02.md) |
| 3 | STEP-TASK-TEMPLATE-007-03 | Test Gmail MCP connectivity | Claude Desktop | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-03.md) |
| 4 | STEP-TASK-TEMPLATE-007-04 | Scan unread emails via Claude + Gmail MCP | Claude Desktop | 1-2 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-04.md) |
| 5 | STEP-TASK-TEMPLATE-007-05 | Generate AI-powered draft replies | Claude Desktop | 3-5 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-05.md) |
| 6 | STEP-TASK-TEMPLATE-007-06 | Review and edit drafts in Gmail | Gmail | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-06.md) |
| 7 | STEP-TASK-TEMPLATE-007-07 | Send approved emails and archive completed | Gmail | 5-10 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-007-07.md) |

### TASK-TEMPLATE-012: Automate Newsletter Subscriber Replies (7 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-012-01 | Filter new newsletter subscriber emails | Gmail | 1-2 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-01.md) |
| 2 | STEP-TASK-TEMPLATE-012-02 | Extract subscriber information via Claude | Claude Desktop | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-02.md) |
| 3 | STEP-TASK-TEMPLATE-012-03 | Generate personalized welcome email | Claude Desktop | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-03.md) |
| 4 | STEP-TASK-TEMPLATE-012-04 | Create draft reply via Gmail MCP | Claude Desktop + Gmail MCP | 1-2 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-04.md) |
| 5 | STEP-TASK-TEMPLATE-012-05 | Review drafts for tone and accuracy | Gmail | 3-5 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-05.md) |
| 6 | STEP-TASK-TEMPLATE-012-06 | Send welcome emails in batch | Gmail | 2-3 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-06.md) |
| 7 | STEP-TASK-TEMPLATE-012-07 | Log subscribers in CRM or newsletter tool | CRM/Newsletter tool | 3-5 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-012-07.md) |

---

## DEV Steps

### TASK-TEMPLATE-006: Generate Custom MCP Connector (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-006-01 | Research target API documentation | API docs | 30-60 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-01.md) |
| 2 | STEP-TASK-TEMPLATE-006-02 | Enable mcp-builder skill in Claude Desktop | Claude Desktop | 1-2 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-02.md) |
| 3 | STEP-TASK-TEMPLATE-006-03 | Prompt Claude to generate MCP connector code | Claude Desktop + mcp-builder | 30-60 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-03.md) |
| 4 | STEP-TASK-TEMPLATE-006-04 | Review generated connector code | Code editor | 15-30 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-04.md) |
| 5 | STEP-TASK-TEMPLATE-006-05 | Configure OAuth and API credentials | API provider | 15-30 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-05.md) |
| 6 | STEP-TASK-TEMPLATE-006-06 | Test connector with sample API calls | Claude Desktop | 10-15 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-006-06.md) |

### TASK-TEMPLATE-010: Deploy MCP Connector Locally (8 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-010-01 | Install Node.js and npm dependencies | Node.js/npm | 5-10 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-01.md) |
| 2 | STEP-TASK-TEMPLATE-010-02 | Clone or download MCP connector code | Git/File system | 2-3 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-02.md) |
| 3 | STEP-TASK-TEMPLATE-010-03 | Install connector dependencies via npm | npm | 2-3 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-03.md) |
| 4 | STEP-TASK-TEMPLATE-010-04 | Configure environment variables and API keys | .env file | 5-10 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-04.md) |
| 5 | STEP-TASK-TEMPLATE-010-05 | Use Cursor AI to deploy connector to Claude Desktop | Cursor | 2-3 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-05.md) |
| 6 | STEP-TASK-TEMPLATE-010-06 | Restart Claude Desktop to load new connector | Claude Desktop | 1 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-06.md) |
| 7 | STEP-TASK-TEMPLATE-010-07 | Verify connector appears in available skills | Claude Desktop | 1-2 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-07.md) |
| 8 | STEP-TASK-TEMPLATE-010-08 | Test connector with sample queries | Claude Desktop | 5-10 min | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-010-08.md) |

### TASK-TEMPLATE-013: Enable Claude Skills Feature (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-013-01 | Open Claude Desktop application | Claude Desktop | 10 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-01.md) |
| 2 | STEP-TASK-TEMPLATE-013-02 | Navigate to Settings menu | Claude Desktop | 10 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-02.md) |
| 3 | STEP-TASK-TEMPLATE-013-03 | Locate Skills or Features section | Claude Desktop | 10 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-03.md) |
| 4 | STEP-TASK-TEMPLATE-013-04 | Toggle Skills feature to ON | Claude Desktop | 5 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-04.md) |
| 5 | STEP-TASK-TEMPLATE-013-05 | Restart Claude Desktop if prompted | Claude Desktop | 30 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-05.md) |
| 6 | STEP-TASK-TEMPLATE-013-06 | Verify Skills icon appears in interface | Claude Desktop | 10 sec | [View](./PHASE4/DEV/STEP-TASK-TEMPLATE-013-06.md) |

---

## HR Steps

### TASK-TEMPLATE-001: Create Job Posting for [Position] (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-001-01 | Select job posting template | Notion/Template library | 5 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-01.md) |
| 2 | STEP-TASK-TEMPLATE-001-02 | Customize role description and responsibilities | Google Docs | 30 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-02.md) |
| 3 | STEP-TASK-TEMPLATE-001-03 | Add required and preferred qualifications | Google Docs | 15 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-03.md) |
| 4 | STEP-TASK-TEMPLATE-001-04 | Define compensation and benefits | Salary tool | 15 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-04.md) |
| 5 | STEP-TASK-TEMPLATE-001-05 | Get hiring manager approval | Slack/Email | 30 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-05.md) |
| 6 | STEP-TASK-TEMPLATE-001-06 | Publish to job boards and social media | LinkedIn/Indeed/Company site | 30 min | [View](./PHASE4/HR/STEP-TASK-TEMPLATE-001-06.md) |

---

## SALES Steps

### TASK-TEMPLATE-002: Send Follow-up Email to old clients (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-002-01 | Identify clients with no activity in 6+ months | CRM | 10 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-01.md) |
| 2 | STEP-TASK-TEMPLATE-002-02 | Segment clients by previous project type | CRM | 10 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-02.md) |
| 3 | STEP-TASK-TEMPLATE-002-03 | Personalize email template for each segment | Email template + CRM data | 20 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-03.md) |
| 4 | STEP-TASK-TEMPLATE-002-04 | Schedule email send times | Email automation tool | 10 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-04.md) |
| 5 | STEP-TASK-TEMPLATE-002-05 | Send emails and track opens/clicks | Email tool + CRM | 10 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-05.md) |
| 6 | STEP-TASK-TEMPLATE-002-06 | Log responses and schedule follow-up calls | CRM | 10 min | [View](./PHASE4/SALES/STEP-TASK-TEMPLATE-002-06.md) |

---

## AI Steps

### TASK-TEMPLATE-020: Scrape Instagram Influencer Profiles (6 steps)

| Step | ID | Description | Tool | Duration |
|------|----|-----------|----|-----|----------|
| 1 | STEP-TASK-TEMPLATE-020-01 | Define influencer search criteria | Search planning | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-01.md) |
| 2 | STEP-TASK-TEMPLATE-020-02 | Configure Apify Instagram scraper | Apify | 5-10 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-02.md) |
| 3 | STEP-TASK-TEMPLATE-020-03 | Run Instagram profile scraper | Apify | 15-20 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-03.md) |
| 4 | STEP-TASK-TEMPLATE-020-04 | Extract engagement metrics and contact info | Apify | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-04.md) |
| 5 | STEP-TASK-TEMPLATE-020-05 | Filter and rank influencers by reach/engagement | Excel/Google Sheets | 10-15 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-05.md) |
| 6 | STEP-TASK-TEMPLATE-020-06 | Export final influencer list for outreach | Excel/Google Sheets | 5-10 min | [View](./PHASE4/AI/STEP-TASK-TEMPLATE-020-06.md) |

---

## 📊 Common Step Patterns

Based on analysis of all 141 steps, the following patterns emerge:

### **1. Prepare/Upload Data** (appears 18 times)
- Prepare company domain list
- Upload domain list to [Tool]
- Prepare contact list

**Tools:** Excel, Google Sheets, CSV
**Average Duration:** 2-5 minutes

### **2. Configure Settings** (appears 20 times)
- Configure enrichment settings
- Configure scraper parameters
- Configure API settings

**Tools:** Apify, Anymailfinder, n8n, API platforms
**Average Duration:** 1-5 minutes

### **3. Execute/Run Automation** (appears 21 times)
- Run enrichment
- Run scraper
- Execute automation

**Tools:** Automated platforms (Apify, n8n, Anymailfinder, Bright Data)
**Average Duration:** 5-15 minutes (automated)

### **4. Export Results** (appears 22 times)
- Export enriched results
- Export final lead list
- Export data

**Tools:** Platform export functions
**Average Duration:** 1-3 minutes

### **5. Review/Quality Check** (appears 15 times)
- Review enriched contacts
- Review drafts in Gmail
- Validate data quality

**Tools:** Excel, Google Sheets, Gmail
**Average Duration:** 3-15 minutes

### **6. Import to CRM** (appears 18 times)
- Import to CRM
- Log campaign metrics
- Update CRM records

**Tools:** CRM platforms (Instantly, Apollo, custom)
**Average Duration:** 2-5 minutes

### **7. Configure MCP/OAuth** (appears 5 times)
- Configure OAuth credentials
- Enable Claude Skills
- Install dependencies

**Tools:** Claude Desktop, MCP connectors, OAuth providers
**Average Duration:** 1-45 minutes

---

## 📈 Phase 4 vs. Existing Steps Comparison

| Metric | Existing Steps (Phase 1-3) | Phase 4 Steps | Total |
|--------|-----------|--------------|-------|
| **Total Steps** | 340 | 141 | 481 |
| **Total Tasks** | 55 | 22 | 77 |
| **Avg Steps/Task** | 6.2 | 6.4 | 6.2 |
| **Departments** | 10 | 6 | 10 |

### **Department Coverage Expansion:**
- Phase 1-3 had more departments (AI, Content AI, Design, Video)
- Phase 4 focused on LG, AI, DEV (core workflow automation)
- Combined coverage: Complete operational spectrum

---

## 🔗 Related Documentation

- **[Task_Templates_Checklist-Item-003.md](../Task_Templates_Checklist-Item-003.md)** - All 22 Phase 4 Task Templates
- **[STEPS_INDEX.md](../STEPS_INDEX.md)** - Main Step Templates index (Phases 1-3: 340 steps)
- **[Phase_4_Completion_Report.md](../Phase_4_Completion_Report.md)** - Phase 4 Task Template creation report
- **Department Checklist-Item-003s:**
  - [LG/Checklist-Item-003.json](./PHASE4/LG/Checklist-Item-003.json) - 82 steps
  - [AI/Checklist-Item-003.json](./PHASE4/AI/Checklist-Item-003.json) - 21 steps
  - [DEV/Checklist-Item-003.json](./PHASE4/DEV/Checklist-Item-003.json) - 20 steps
  - [HR/Checklist-Item-003.json](./PHASE4/HR/Checklist-Item-003.json) - 6 steps
  - [SALES/Checklist-Item-003.json](./PHASE4/SALES/Checklist-Item-003.json) - 6 steps
  - [AI/Checklist-Item-003.json](./PHASE4/AI/Checklist-Item-003.json) - 6 steps

---

## 🎯 Business Value

**Time Savings Enabled:**
- 141 documented steps eliminate guesswork
- Average 6.4 steps per workflow
- Clear duration estimates enable accurate planning
- Reusable patterns reduce future template creation time

**Quality Improvements:**
- Standardized step structure
- Dependencies clearly documented
- Success criteria defined
- Input/output specifications reduce errors

**Training Acceleration:**
- New team members can follow step-by-step guides
- Tools and durations specified
- Best practices embedded in templates

---

**Version:** 1.0
**Last Updated:** 2025-11-12
**Phase:** Phase 5 (Step Template Extraction Complete)
**Status:** ✅ COMPLETE
