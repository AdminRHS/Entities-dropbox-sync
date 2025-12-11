# Templates Index - TSM-004 Step Templates

**Created:** 2025-12-11
**Purpose:** Complete index of 178 step templates across 5 departments
**Location:** TASK_MANAGERS/TSM-004_Step_Templates/

---

## Overview

**Total Templates:** 178
**Departments:** 5 (DESIGN, DEV, HR, LG, SALES)
**Format:** Markdown (.md) + JSON listings
**Created:** 2025-11-10

### Template Distribution

```csv
DEPARTMENT,TEMPLATE_COUNT,PERCENTAGE,LISTING_FILE
DESIGN,61,34%,DESIGN/Listing.json
HR,36,20%,HR/Listing.json
DEV,33,19%,DEV/Listing.json
SALES,27,15%,SALES/Listing.json
LG,21,12%,LG/Listing.json
```

---

## Quick Search Guide

### By Action Type

```csv
ACTION,DEPARTMENTS,EXAMPLE_TEMPLATES,COUNT
Create,DESIGN DEV HR,create-logo-concepts design-ui-component-library create-dockerfile,35+
Design,DESIGN,design-scraper-architecture design-admin-calendar-interface,20+
Configure,DEV,configure-mcp configure-environment-variables,10+
Document,ALL,document-spacing-rules document-designer-responses document-deployment,18+
Review,DESIGN HR LG,review-client-landing-page review-employee-status collect-performance-data,15+
Implement,DEV,implement-data-extraction implement-api-endpoints implement-multi-threaded,12+
Test,DEV,test-integration test-docker-build test-scraper-stability,8+
Deploy,DEV,deploy-to-production,5+
Communicate,DESIGN HR,communicate-questions-to-designer send-welcome-email,8+
Identify,DESIGN HR LG,identify-missing-information identify-status-discrepancies,10+
```

### By Task Category

```csv
CATEGORY,DEPARTMENTS,TEMPLATE_RANGE,COUNT
Brand Identity,DESIGN,DESIGN-001-01 to DESIGN-001-08,8
Client Communication,DESIGN,DESIGN-002-01 to DESIGN-010-06,50+
Web Scraping,DEV,DEV-001-01 to DEV-004-06,27
MCP Integration,DEV,DEV-002-01 to DEV-002-06,6
Docker Deployment,DEV,DEV-003-01 to DEV-005-07,21
Employee Onboarding,HR,HR-001-01 to HR-006-06,36
Performance Management,LG,LG-001-01 to LG-003-07,21
CRM & Lead Management,SALES,SALES-001-01 to SALES-004-06,27
```

### By Tool

```csv
TOOL,DEPARTMENTS,TEMPLATE_COUNT,EXAMPLE_USE_CASES
Figma,DESIGN,40+,UI design component-library mockups responsive-designs
Python,DEV,25+,Scraping threading API-endpoints data-processing
Docker,DEV,15+,Containerization deployment configuration monitoring
Selenium,DEV,12+,Web-scraping automation testing
Email / HR system,HR,15+,Employee-communication onboarding feedback
CRM,SALES,20+,Lead-tracking contact-management sales-pipeline
Spreadsheet,LG HR SALES,18+,Data-analysis performance-tracking reporting
Zoom,DESIGN HR,8+,Client-discovery team-meetings presentations
Documentation tools,ALL,25+,Process-documentation guidelines knowledge-base
```

---

## Department Breakdown

### DESIGN Department (61 templates)

**Path:** `TSM-004_Step_Templates/DESIGN/`
**Listing:** `DESIGN/Listing.json`

#### Task Groups

**DESIGN-001: Brand Identity System (8 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
001-01,Conduct,Conduct client brand discovery session,Zoom Miro Notion
001-02,Research,Research competitor branding,Web-research design-inspiration-sites
001-03,Create,Create logo concepts,Figma Illustrator
001-04,Define,Define color palette,Figma color-palette-generators
001-05,Select,Select typography system,Google-Fonts Adobe-Fonts
001-06,Document,Document spacing and grid rules,Figma
001-07,Create,Create usage guidelines,Figma Google-Docs
001-08,Present,Present to client for approval,Zoom Figma-presentation-mode
```

**DESIGN-002: Client Requirements Clarification (6 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
002-01,Review,Review client landing page,Web-Browser Design-Tools
002-02,Identify,Identify missing information and requirements,Requirements-Analysis
002-03,Formulate,Formulate questions for designer,Question-Documentation
002-04,Communicate,Communicate questions to designer,Discord Email PM-Tool
002-05,Document,Document designer responses,Documentation-System
002-06,Update,Update development plan based on clarifications,Project-Planning
```

**DESIGN-003: Working Hours & Boundaries (6 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
003-01,Identify,Identify boundary violation issue,Issue-Analysis
003-02,Define,Define working hours policy (12:00-16:00),Policy-Documentation
003-03,Communicate,Communicate working hours to client,Client-Communication
003-04,Adjust,Adjust reporting frequency (daily to weekly),Process-Optimization
003-05,Clarify,Clarify reporting expectations and format,Client-Agreement
003-06,Document,Document new communication standards,Documentation-System
```

**DESIGN-004: Employee Status Accuracy (6 steps)**
- Review employee status lists
- Identify status discrepancies
- Document incorrect status examples
- Coordinate with HR
- Update status records
- Establish ongoing process

**DESIGN-005: Design System Creation (6 steps)**
- Define brand identity (personality values voice tone)
- Create visual style specifications
- Design UI component library (10+ categories)
- Document design patterns
- Create accessibility standards (WCAG)
- Document content type requirements

**DESIGN-006: Landing Page Design (6 steps)**
- Create landing page layout
- Design visual elements (hero features CTA)
- Ensure brand consistency
- Create responsive designs (mobile tablet desktop)
- Prepare developer handoff package
- Coordinate development timeline

**DESIGN-007: Calendar Interface Design (6 steps)**
- Design admin calendar interface
- Design regular employee calendar
- Create adaptive designs for screens
- Build reusable design system components
- Conduct client feedback iterations
- Plan for team expansion (2 more UX designers)

**DESIGN-008: Multi-Size Design Variations (6 steps)**
- Complete initial vertical designs
- Identify required size variations
- Adapt designs for multiple sizes
- Test across different dimensions
- Finalize and export all variations
- Negotiate project scope and pricing

**DESIGN-009 & 010: Additional client communication workflows**
- Similar to DESIGN-002 and DESIGN-003 (6 steps each)

**Total DESIGN templates:** 61

---

### DEV Department (33 templates)

**Path:** `TSM-004_Step_Templates/DEV/`
**Listing:** `DEV/Listing.json`

#### Task Groups

**DEV-001: Web Scraper Development (7 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
001-01,Design,Design scraper architecture (single-threaded baseline),Python Selenium
001-02,Implement,Implement data extraction logic for target website,Selenium-WebDriver BeautifulSoup
001-03,Add,Add error handling and retry logic,Python-exception-handling
001-04,Implement,Implement multi-threaded architecture (10-50 threads),Python-threading
001-05,Add,Add proxy rotation for IP management,Proxy-management-service
001-06,Optimize,Optimize performance and resource usage,Profiling-tools
001-07,Test,Test scraper stability and accuracy,QA-testing
```

**DEV-002: MCP Integration (6 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
002-01,Review,Review MCP documentation and API specifications,Documentation
002-02,Install,Install MCP dependencies,Package-manager
002-03,Configure,Configure MCP in Claude Desktop settings,Configuration-file
002-04,Implement,Implement API endpoints,Python MCP-SDK
002-05,Test,Test integration with sample queries,Claude-Desktop
002-06,Troubleshoot,Troubleshoot and debug issues,Debugging-tools
```

**DEV-003: Docker Deployment (7 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
003-01,Create,Create Dockerfile and docker-compose.yml,Docker
003-02,Configure,Configure environment variables and secrets,Docker-secrets
003-03,Test,Test Docker build locally,Docker-CLI
003-04,Set,Set up production hosting infrastructure,Cloud-platform
003-05,Deploy,Deploy to production,Docker-deployment
003-06,Configure,Configure monitoring and health checks,Monitoring-tools
003-07,Document,Document deployment process,DevOps-documentation
```

**DEV-004: Advanced Scraper Features (6 steps)**
- Improve core scraper stability (Reviews button search)
- Implement multi-threaded processing
- Add proxy rotation for IP management
- Expand NLP problem dictionary (dozens of anchors)
- Enhance decision-maker search logic
- Conduct production test cycles

**DEV-005: Production Deployment (7 steps)**
- Evaluate deployment approaches (pm2 vs Docker)
- Create Docker configuration files
- Configure production hosting infrastructure
- Test Docker deployment locally
- Deploy to production (https://honeystone.fv-e.com/)
- Set up monitoring and health checks
- Document deployment process for reusability

**Total DEV templates:** 33

---

### HR Department (36 templates)

**Path:** `TSM-004_Step_Templates/HR/`
**Listing:** `HR/Listing.json`

#### Task Groups

**HR-001: Employee Onboarding (6 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
001-01,Send,Send welcome email and gather required information,Email HR-system
001-02,Create,Create employee folder and documentation,File-system
001-03,Setup,Setup access to systems and tools,IT-provisioning
001-04,Schedule,Schedule orientation and training,Calendar
001-05,Assign,Assign initial tasks and mentor,Task-management
001-06,Follow-up,Follow up on first week progress,Communication-tools
```

**HR-002: Performance Reviews (6 steps)**
- Schedule review meetings
- Collect performance data
- Conduct review session
- Document feedback and goals
- Create development plan
- Schedule follow-up review

**HR-003: Feedback Distribution (6 steps)**
- Prepare individual feedback files
- Review feedback for clarity and actionability
- Distribute feedback to employees
- Add notifications to daily files
- Track delivery confirmations
- Schedule feedback discussion sessions

**HR-004: Employee Registry Management (6 steps)**
- Collect employee information from all sources
- Verify data accuracy and completeness
- Create/update employee registry CSV
- Cross-reference with department rosters
- Validate contact information
- Publish updated registry

**HR-005: Status Tracking (6 steps)**
- Review employee status across all systems
- Identify discrepancies (available vs on projects)
- Document incorrect status examples
- Coordinate with departments for updates
- Update status records
- Establish ongoing accuracy process

**HR-006: Communication Standards (6 steps)**
- Define communication policies
- Create communication templates
- Document escalation procedures
- Train employees on standards
- Monitor compliance
- Update policies based on feedback

**Total HR templates:** 36

---

### LG Department (Legal/Logistics) (21 templates)

**Path:** `TSM-004_Step_Templates/LG/`
**Listing:** `LG/Listing.json`

#### Task Groups

**LG-001: Performance Data Collection (7 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
001-01,Collect,Collect performance data from all sources,Spreadsheet CRM PM-tools
001-02,Normalize,Normalize data formats across sources,Data-processing
001-03,Analyze,Analyze performance metrics,Analytics-tools
001-04,Identify,Identify trends and outliers,Statistical-analysis
001-05,Create,Create performance report,Reporting-tools
001-06,Present,Present findings to management,Presentation-software
001-07,Archive,Archive data for historical tracking,Data-storage
```

**LG-002: Contract Management (7 steps)**
- Review contract requirements
- Draft contract terms
- Coordinate legal review
- Negotiate with client
- Finalize contract
- File and track contract
- Monitor contract compliance

**LG-003: Compliance Tracking (7 steps)**
- Define compliance requirements
- Create compliance checklist
- Audit current practices
- Identify gaps
- Create remediation plan
- Implement changes
- Document compliance status

**Total LG templates:** 21

---

### SALES Department (27 templates)

**Path:** `TSM-004_Step_Templates/SALES/`
**Listing:** `SALES/Listing.json`

#### Task Groups

**SALES-001: CRM Lead Management (7 steps)**
```csv
STEP,ACTION,DESCRIPTION,TOOLS
001-01,Extract,Extract lead visibility data from CRM,CRM-API or-export
001-02,Analyze,Analyze lead distribution and coverage,Analytics-tools
001-03,Identify,Identify gaps in lead visibility,Gap-analysis
001-04,Create,Create lead assignment rules,CRM-configuration
001-05,Update,Update CRM lead ownership,CRM-admin
001-06,Train,Train sales team on new process,Training-materials
001-07,Monitor,Monitor lead response times,CRM-dashboards
```

**SALES-002: Sales Pipeline Optimization (6 steps)**
- Review current pipeline stages
- Analyze conversion rates by stage
- Identify bottlenecks
- Redesign pipeline stages
- Update CRM pipeline configuration
- Train team on new pipeline

**SALES-003: Proposal Creation (7 steps)**
- Gather client requirements
- Create proposal outline
- Develop pricing structure
- Design proposal document
- Review with stakeholders
- Submit proposal to client
- Follow up on proposal status

**SALES-004: Client Follow-up Automation (7 steps)**
- Define follow-up trigger events
- Create follow-up email templates
- Configure CRM automation rules
- Test automation workflows
- Train team on automation
- Monitor automation performance
- Optimize based on results

**Total SALES templates:** 27

---

## Usage Guide

### When to Use Templates

**Before creating any custom task steps:**
1. Search this index for similar actions/tasks
2. Check match score (see calculation below)
3. If match ≥ 80%: Inherit and customize parameters
4. If match 50-79%: Use structure, modify steps
5. If match < 50%: Reference patterns, create custom

### Match Score Calculation

```python
def calculate_template_match(user_task, template):
    """
    Calculate similarity between user task and template
    Returns score 0-100
    """
    from difflib import SequenceMatcher

    # Compare action
    action_sim = SequenceMatcher(None,
        user_task['action'].lower(),
        template['action'].lower()
    ).ratio() * 100

    # Compare description
    desc_sim = SequenceMatcher(None,
        user_task['description'].lower(),
        template['description'].lower()
    ).ratio() * 100

    # Compare tools (Jaccard similarity)
    user_tools = set(user_task.get('tools', '').lower().split())
    template_tools = set(template.get('tools', '').lower().split())

    if user_tools and template_tools:
        tool_sim = len(user_tools & template_tools) / len(user_tools | template_tools) * 100
    else:
        tool_sim = 0

    # Weighted average
    match_score = (action_sim * 0.4) + (desc_sim * 0.4) + (tool_sim * 0.2)

    return round(match_score, 1)
```

### Search Examples

**Example 1: Find templates for "create API endpoint"**

```python
import glob
import json

# Load all DESIGN templates
dept = 'DEV'
with open(f'TSM-004_Step_Templates/{dept}/Listing.json', 'r') as f:
    listing = json.load(f)

# Search for "create" + "api"
matches = []
for step in listing['steps']:
    if 'api' in step['description'].lower() and 'implement' in step['action'].lower():
        matches.append({
            'id': step['id'],
            'description': step['description'],
            'tools': step['tool']
        })

# Result:
# DEV-002-04: Implement API endpoints (Python + MCP SDK)
```

**Example 2: Find templates by department and action**

```python
def find_by_dept_action(department, action_keyword):
    with open(f'TSM-004_Step_Templates/{department}/Listing.json', 'r') as f:
        listing = json.load(f)

    results = [
        step for step in listing['steps']
        if action_keyword.lower() in step['action'].lower()
    ]

    return results

# Find all "Create" actions in DESIGN
create_templates = find_by_dept_action('DESIGN', 'Create')
# Returns: 15+ templates (logo concepts, UI components, layouts, etc.)
```

**Example 3: Find templates by tool**

```python
def find_by_tool(tool_name):
    results = []

    for dept in ['DESIGN', 'DEV', 'HR', 'LG', 'SALES']:
        with open(f'TSM-004_Step_Templates/{dept}/Listing.json', 'r') as f:
            listing = json.load(f)

        for step in listing['steps']:
            if tool_name.lower() in step['tool'].lower():
                results.append({
                    'dept': dept,
                    'id': step['id'],
                    'description': step['description']
                })

    return results

# Find all Figma templates
figma_templates = find_by_tool('Figma')
# Returns: 40+ DESIGN templates
```

---

## Integration with Libraries

### Step 1: Find RESP-ID
Use [Responsibilities library](../LIBRARIES/Responsibilities/) to find RESP-ID

### Step 2: Search for Template
Use this index to find similar templates by:
- Action type
- Description
- Department
- Tools

### Step 3: Calculate Match Score
Use match score calculation to determine inheritance strategy

### Step 4: Inherit or Create
- ≥80%: Inherit template, customize parameters only
- 50-79%: Use template structure, modify steps
- <50%: Create custom, reference similar patterns

---

## Template File Structure

Each template file (.md) contains:

```markdown
# Step Template: {STEP_ID}

**Parent Task:** {TASK_ID}
**Step Number:** {N}
**Action:** {ACTION}
**Tool:** {TOOLS}
**Created:** {DATE}

## Description
{Detailed description of what this step accomplishes}

## Prerequisites
- {List of required conditions before this step}
- {Required inputs/data}

## Execution
{Step-by-step instructions}

## Outputs
- {Expected outputs}
- {Deliverables}

## Validation
- [ ] {Checklist item 1}
- [ ] {Checklist item 2}

## Tools Required
- {Tool 1}: {Usage description}
- {Tool 2}: {Usage description}

## Estimated Duration
{Time estimate}

## Dependencies
{Links to other steps or tasks}
```

---

## Quick Reference Tables

### Top 20 Most Reusable Templates

```csv
RANK,TEMPLATE_ID,ACTION,DESCRIPTION,REUSE_SCORE,DEPT
1,DESIGN-001-03,Create,Create logo concepts,95,DESIGN
2,DEV-003-01,Create,Create Dockerfile and docker-compose.yml,94,DEV
3,HR-001-01,Send,Send welcome email gather information,93,HR
4,DEV-001-03,Add,Add error handling and retry logic,92,DEV
5,DESIGN-005-03,Design,Design UI component library,92,DESIGN
6,HR-002-02,Collect,Collect performance data,91,HR
7,SALES-001-01,Extract,Extract lead visibility data from CRM,90,SALES
8,DEV-002-04,Implement,Implement API endpoints,89,DEV
9,DESIGN-006-01,Create,Create landing page layout,89,DESIGN
10,LG-001-01,Collect,Collect performance data from all sources,88,LG
11,DEV-001-02,Implement,Implement data extraction logic,87,DEV
12,DESIGN-002-02,Identify,Identify missing information,87,DESIGN
13,HR-003-01,Prepare,Prepare individual feedback files,86,HR
14,DEV-003-07,Document,Document deployment process,86,DEV
15,SALES-003-01,Gather,Gather client requirements,85,SALES
16,DESIGN-001-04,Define,Define color palette,85,DESIGN
17,DEV-001-04,Implement,Implement multi-threaded architecture,84,DEV
18,HR-004-03,Create,Create/update employee registry CSV,84,HR
19,LG-002-02,Draft,Draft contract terms,83,LG
20,SALES-002-03,Identify,Identify pipeline bottlenecks,83,SALES
```

### Templates by Estimated Duration

```csv
DURATION,TEMPLATE_COUNT,PERCENTAGE,EXAMPLE_TEMPLATES
< 30min,45,25%,Send-email Install-dependencies Configure-settings
30min-1hr,58,33%,Create-folder-structure Review-document Test-locally
1-2hr,42,24%,Implement-API-endpoint Design-logo-concepts Create-report
2-4hr,23,13%,Build-UI-component-library Implement-multi-threading
4+hr,10,6%,Complete-design-system End-to-end-testing Full-deployment
```

### Templates by Complexity

```csv
COMPLEXITY,TEMPLATE_COUNT,CHARACTERISTICS,EXAMPLE_TEMPLATES
Simple,62,Single-tool One-deliverable Clear-checklist,Send-email Create-folder Review-status
Moderate,78,Multi-tool Multiple-steps Coordination-required,Implement-scraper Configure-deployment Design-landing-page
Complex,38,Multi-department Long-duration Multiple-dependencies,Build-design-system Production-deployment Create-brand-identity
```

---

## Maintenance

### Adding New Templates

1. Create template file in appropriate department folder
2. Add entry to department's Listing.json
3. Update total_items count in listing_metadata
4. Regenerate this index
5. Update integration examples

### Template Versioning

```csv
VERSION,DATE,CHANGES,AFFECTED_TEMPLATES
1.0,2025-11-10,Initial template creation,All (178 templates)
1.1,2025-12-11,Added index and search guide,Documentation only
```

### Quality Metrics

```csv
METRIC,TARGET,CURRENT,STATUS
Template completeness,100%,100%,✅ Complete
Tool specification,100%,100%,✅ Complete
Duration estimates,90%,85%,⚠️ In progress
Validation checklists,100%,100%,✅ Complete
Integration examples,50%,45%,⚠️ In progress
```

---

## Related Documentation

- [Responsibilities Library](../LIBRARIES/Responsibilities/README.md) - RESP-ID assignment
- [Libraries Quick Start](../LIBRARIES/LIBRARIES_QUICK_START.md) - Library integration guide
- [Prompt Template](../../System/PROMPT_TEMPLATE_LIBRARY_INTEGRATED.md) - Integrated prompt template
- [Quick Reference](../../System/QUICK_REFERENCE.md) - Top 10 folders guide
- [Parameters](TSM-003_Parameters/) - 7,321 parameter mappings for output enrichment

---

## Statistics Summary

```csv
METRIC,VALUE
Total Templates,178
Departments,5
Actions (unique),42
Tools (unique),67
Average Steps per Task,6.2
Longest Task,8 steps (DESIGN-001)
Shortest Task,5 steps (multiple)
Most Common Action,Create (35+)
Most Common Tool,Figma (40+)
Most Common Duration,30min-1hr (33%)
```

---

**Use this index when:**
- Creating any new task with multiple steps
- Searching for existing patterns to reuse
- Calculating template match scores
- Understanding department capabilities
- Estimating task durations
- Selecting appropriate tools

**Integration workflow:**
1. Get RESP-ID from Responsibilities library
2. Search this index for similar templates
3. Calculate match score
4. Inherit/modify/reference as appropriate
5. Enrich with Parameters library
6. Execute using integrated prompt template

---

**END TEMPLATES INDEX**
