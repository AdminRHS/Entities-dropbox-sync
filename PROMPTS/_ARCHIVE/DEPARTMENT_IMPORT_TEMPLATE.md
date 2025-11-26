# Department-Specific Import Prompt Template

This template provides specialized prompts for importing entity data from different department sources.

---

## Sales Department Import

### Prompt
```
Build me a multi-phase import system for BUSINESSES entity:

SOURCE: Dropbox\Nov25\Sales Nov25\client_list.md
CONTEXT: Dropbox\Nov25\Sales Nov25\
ARCHIVES: Sales_Oct25, Sales_Sep25, Sales_Aug25, Sales_Jul25

Import all client/prospect data including:
- Active clients (hired/paying)
- Prospects in pipeline
- Ex-clients for reengagement

Follow 5-phase approach:
1. Validation (check data quality)
2. Extraction (categorize entities)
3. Enrichment (from call transcripts)
4. Generation (create JSON files)
5. Archive Review (check Oct25, Sep25, etc.)

Requirements:
- Generate BUS-2025-XXX IDs
- Calculate relationship health scores
- Auto-tag by status, services, manager
- Review ALL archive months for additional entities
- Cross-reference to avoid duplicates
```

**Expected Output:**
- 40+ BUSINESSES entities
- Clients, Prospects, Ex_Clients categorized
- Full documentation and statistics

---

## HR Department Import

### Prompt
```
Build me a multi-phase import system for TALENTS entity:

SOURCE: Dropbox\Nov25\HR Nov25\[employee_list or roster file]
CONTEXT: Dropbox\Nov25\HR Nov25\

Import all employee/talent data including:
- Full-time employees
- Part-time contractors
- Candidates in pipeline
- Former employees

Follow 4-phase approach:
1. Validation (check employee records)
2. Extraction (categorize by employment type)
3. Enrichment (from HR documents)
4. Generation (create JSON files)

Requirements:
- Generate TAL-2025-XXX IDs
- Track employment status
- Link to assigned clients (BUSINESSES entity)
- Include skills, certifications, performance data
```

**Expected Output:**
- TALENTS entities
- Employees, Contractors, Candidates, Alumni
- Cross-references to BUSINESSES clients

---

## Content Department Import

### Prompt
```
Build me a multi-phase import system for CONTENT entity:

SOURCE: Dropbox\Nov25\Content Nov25\[content_inventory or asset_list]
CONTEXT: Dropbox\Nov25\Content Nov25\

Import all content assets including:
- Blog posts and articles
- Social media content
- Marketing materials
- Client deliverables

Follow 4-phase approach:
1. Validation (check content metadata)
2. Extraction (categorize by content type)
3. Enrichment (from content files)
4. Generation (create JSON files)

Requirements:
- Generate CON-2025-XXX IDs
- Track content status (draft, published, archived)
- Link to related BUSINESSES clients
- Include performance metrics (views, engagement)
```

**Expected Output:**
- CONTENT entities
- Categorized by type and status
- Performance tracking enabled

---

## Design Department Import

### Prompt
```
Build me a multi-phase import system for DESIGN entity:

SOURCE: Dropbox\Nov25\Design Nov25\[design_projects or portfolio]
CONTEXT: Dropbox\Nov25\Design Nov25\

Import all design projects including:
- Client projects
- Internal projects
- Templates and assets
- Brand materials

Follow 4-phase approach:
1. Validation (check project data)
2. Extraction (categorize by project type)
3. Enrichment (from design files and feedback)
4. Generation (create JSON files)

Requirements:
- Generate DES-2025-XXX IDs
- Track project status and revisions
- Link to BUSINESSES clients
- Include design assets and deliverables
```

**Expected Output:**
- DESIGN entities
- Portfolio of work
- Client linkages

---

## Development Department Import

### Prompt
```
Build me a multi-phase import system for DEVELOPMENT entity:

SOURCE: Dropbox\Nov25\Dev Nov25\[projects_list or repository_index]
CONTEXT: Dropbox\Nov25\Dev Nov25\

Import all development projects including:
- Client development projects
- Internal tools and systems
- Maintenance projects
- R&D initiatives

Follow 4-phase approach:
1. Validation (check project specs)
2. Extraction (categorize by project type)
3. Enrichment (from code repos and docs)
4. Generation (create JSON files)

Requirements:
- Generate DEV-2025-XXX IDs
- Track project status and milestones
- Link to BUSINESSES clients
- Include tech stack and repository links
```

**Expected Output:**
- DEVELOPMENT entities
- Active and completed projects
- Technical documentation

---

## Lead Generation Department Import

### Prompt
```
Build me a multi-phase import system for LEADS entity:

SOURCE: Dropbox\Nov25\LG Nov25\[leads_list or campaign_data]
CONTEXT: Dropbox\Nov25\LG Nov25\

Import all lead generation data including:
- Active campaigns
- Lead lists
- Conversion data
- Campaign performance

Follow 4-phase approach:
1. Validation (check lead data quality)
2. Extraction (categorize by campaign and status)
3. Enrichment (from campaign documents)
4. Generation (create JSON files)

Requirements:
- Generate LED-2025-XXX IDs
- Track lead status and conversion
- Link to BUSINESSES prospects/clients
- Include campaign metrics and ROI
```

**Expected Output:**
- LEADS entities
- Campaign performance data
- Conversion tracking

---

## Finance Department Import

### Prompt
```
Build me a multi-phase import system for FINANCE entity:

SOURCE: Dropbox\Nov25\Fin Nov25\[financial_records or invoice_list]
CONTEXT: Dropbox\Nov25\Fin Nov25\

Import all financial data including:
- Invoices and payments
- Revenue records
- Expenses and costs
- Financial forecasts

Follow 4-phase approach:
1. Validation (check financial data accuracy)
2. Extraction (categorize by transaction type)
3. Enrichment (from supporting documents)
4. Generation (create JSON files)

Requirements:
- Generate FIN-2025-XXX IDs
- Track payment status and amounts
- Link to BUSINESSES clients
- Include revenue and profitability metrics
```

**Expected Output:**
- FINANCE entities
- Revenue tracking
- Client profitability analysis

---

## Social Media Marketing Department Import

### Prompt
```
Build me a multi-phase import system for SMM entity:

SOURCE: Dropbox\Nov25\SMM Nov25\[campaign_list or content_calendar]
CONTEXT: Dropbox\Nov25\SMM Nov25\

Import all social media data including:
- Campaign schedules
- Content posts
- Engagement metrics
- Client social accounts

Follow 4-phase approach:
1. Validation (check campaign data)
2. Extraction (categorize by platform and type)
3. Enrichment (from analytics data)
4. Generation (create JSON files)

Requirements:
- Generate SMM-2025-XXX IDs
- Track campaign performance
- Link to BUSINESSES clients
- Include engagement and conversion metrics
```

**Expected Output:**
- SMM entities
- Platform-specific metrics
- Campaign effectiveness tracking

---

## AI/Automation Department Import

### Prompt
```
Build me a multi-phase import system for AI_TOOLS entity:

SOURCE: Dropbox\Nov25\AI Nov25\[tools_inventory or automation_catalog]
CONTEXT: Dropbox\Nov25\AI Nov25\

Import all AI/automation tools and systems including:
- AI assistants and chatbots
- Automation workflows
- Data processing tools
- Internal systems

Follow 4-phase approach:
1. Validation (check tool specifications)
2. Extraction (categorize by tool type)
3. Enrichment (from usage data and documentation)
4. Generation (create JSON files)

Requirements:
- Generate AIT-2025-XXX IDs
- Track tool status and usage
- Link to users (TALENTS) and clients (BUSINESSES)
- Include capabilities and integration points
```

**Expected Output:**
- AI_TOOLS entities
- Capability matrix
- Usage tracking

---

## Cross-Department Linking

After individual department imports, create cross-references:

### Linking Prompt
```
Create relationship mappings between entities:

1. BUSINESSES ↔ TALENTS (client assignments)
2. BUSINESSES ↔ CONTENT (client deliverables)
3. BUSINESSES ↔ DESIGN (client projects)
4. BUSINESSES ↔ DEVELOPMENT (client builds)
5. BUSINESSES ↔ FINANCE (invoices and revenue)
6. LEADS ↔ BUSINESSES (lead conversion tracking)
7. TALENTS ↔ Projects (all entity types)

Generate relationship_map.json with all cross-references.
```

---

## Universal Import Checklist

For ANY department import:

1. ✅ Identify source data file(s)
2. ✅ Validate data quality
3. ✅ Define categorization rules
4. ✅ Generate unique IDs (XXX-2025-###)
5. ✅ Transform data to target schema
6. ✅ Create individual JSON files
7. ✅ Generate index and master catalog
8. ✅ Create comprehensive documentation
9. ✅ Identify cross-entity relationships
10. ✅ Review archive directories

---

## Template Customization

To create a new department import:

1. **Copy this template**
2. **Replace department name** (e.g., "MARKETING", "OPERATIONS")
3. **Define entity ID prefix** (e.g., MKT-2025-XXX, OPS-2025-XXX)
4. **Specify source data location**
5. **Define categorization rules** specific to department
6. **Customize JSON schema** for entity type
7. **Identify cross-references** to other entities
8. **Run the import** following multi-phase approach

---

**Template Version:** 1.0
**Last Updated:** 2025-11-21
**Status:** Ready for use across all departments
