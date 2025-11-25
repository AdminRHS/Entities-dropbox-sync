# Extracted Task Templates Documentation
**Version:** 1.0
**Last Updated:** November 10, 2025
**Total Templates:** 10
**Source:** RestructuredData Files Extraction
**Extraction Coverage:** 42% (8 of 19 files)

---

## 📋 Overview

This document contains Task Templates extracted from RestructuredData documents following the DATA_EXTRACTION_PROMPT.md guidelines. Each template includes complete taxonomy (Action + Object + Tool + Context), specifications, responsibilities, and cross-references.

**Quick Reference:** See [Extracted_Task_Templates_Checklist-Item-003.md](./Extracted_Task_Templates_Checklist-Item-003.md) for ID and name index.

---

## TASK-LG-001: Create Folder Structure for Employee

**ID:** `TASK-LG-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-05
**Last Updated:** 2025-11-10
**Source:** Projects_Milestones_Tasks_Nov05-07_2025.md (Line 75)

### Basic Information

- **Task Name:** Create Folder Structure for [Employee Name]
- **Action:** Create
- **Object:** Folder Structure
- **Tool:** Filesystem
- **Context:** LG-Department-Onboarding
- **Department:** LG (Legal & Governance)
- **Profession:** AI
- **Estimated Duration:** 30 minutes
- **Priority:** High
- **Status:** Template (Reusable)

### Description

Create standardized folder structure for new employee onboarding in LG Department. This ensures consistent file organization and access permissions for team members.

### Responsibilities

**Primary Responsible:**
- AI - Creates and configures folder structure with proper permissions

**Accountable:**
- Department Lead (LG) - Approves folder structure and access rights

**Consulted:**
- IT Administrator - Provides technical guidance on permissions and access control
- HR - Confirms employee details and start date

**Informed:**
- Employee - Notified when folder is ready with access instructions
- Team Members - Aware of new team member folder location

### Dependencies

- Employee information confirmed (name, role, start date)
- Standard folder template available
- Access permissions defined
- Dropbox/file system access configured

### Tools Required

- Filesystem (Dropbox, OneDrive, or internal file system)
- Permissions management system
- Documentation templates

### Success Criteria

- Folder structure created following organizational standard
- All required subfolders present (Projects, Reports, Personal, Archive)
- Access permissions properly configured
- Employee can access folder on first day
- Documentation templates copied into folder
- Folder location communicated to relevant parties

### Steps

1. **Verify employee details**
   - Tool: HR System, Email
   - Responsibility: AI
   - Placement: HR Database
   - Duration: 5 minutes
   - Dependencies: None
   - Success Criteria: Employee name, role, department confirmed

2. **Navigate to department folder location**
   - Tool: Filesystem
   - Responsibility: AI
   - Placement: /Dropbox/[Department]/Team/
   - Duration: 2 minutes
   - Dependencies: Step 1
   - Success Criteria: Correct department folder opened

3. **Create main employee folder**
   - Tool: Filesystem
   - Responsibility: AI
   - Placement: /Dropbox/[Department]/Team/[Employee_Name]/
   - Duration: 3 minutes
   - Dependencies: Step 2
   - Success Criteria: Main folder created with proper naming convention

4. **Create standard subfolders**
   - Tool: Filesystem
   - Responsibility: AI
   - Placement: Within employee main folder
   - Duration: 10 minutes
   - Dependencies: Step 3
   - Success Criteria: All required subfolders created (01_Projects, 02_Reports, 03_Personal, 04_Archive, 05_Training)

5. **Copy documentation templates**
   - Tool: Filesystem
   - Responsibility: AI
   - Placement: Employee folder subfolders
   - Duration: 5 minutes
   - Dependencies: Step 4
   - Success Criteria: All template files copied successfully

6. **Configure access permissions**
   - Tool: Permission management system
   - Responsibility: AI
   - Placement: Folder properties/settings
   - Duration: 5 minutes
   - Dependencies: Step 5
   - Success Criteria: Employee has read/write access, department has read access

### Checklist

- [ ] Employee information verified with HR
  - Guide: Confirm name spelling, role, department, start date
  - Required: Yes

- [ ] Folder naming follows convention
  - Guide: LastName_FirstName or Employee_Full_Name format
  - Required: Yes

- [ ] All standard subfolders created
  - Guide: Minimum 5 subfolders (Projects, Reports, Personal, Archive, Training)
  - Required: Yes

- [ ] Documentation templates copied
  - Guide: Include relevant templates for employee role
  - Required: Yes

- [ ] Access permissions configured
  - Guide: Employee (read/write), Department (read), AI (full control)
  - Required: Yes

- [ ] Folder location communicated
  - Guide: Send email with folder path and access instructions
  - Required: Yes

### Tags

lg, onboarding, folder_structure, admin, employee_setup, template

### Cross-References

**Related Entities:**
- [../Projects_Checklist-Item-003.md](../Projects_Checklist-Item-003.md) - PROJ-LG-001: LG Team Onboarding Solution
- `../../LIBRARIES/Actions/` - "Create" action definition
- `../../LIBRARIES/Objects/` - "Folder Structure" object definition
- `../../TALENTS/Employees/` - Employee records

---

## TASK-DESIGN-001: Define Brand Guidelines for Client

**ID:** `TASK-DESIGN-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-05
**Last Updated:** 2025-11-10
**Source:** Projects_Milestones_Tasks_Nov05-07_2025.md (Line 147)

### Basic Information

- **Task Name:** Define Brand Guidelines for [Client Name]
- **Action:** Define
- **Object:** Brand Guidelines
- **Tool:** Design Principles
- **Context:** Client-Branding
- **Department:** Design
- **Profession:** Designer
- **Estimated Duration:** 4 hours
- **Priority:** Critical
- **Status:** Template (Reusable)

### Description

Create comprehensive brand guidelines including logo, colors, typography, and spacing rules for client branding projects. Ensures consistent visual identity across all client deliverables.

### Responsibilities

**Primary Responsible:**
- Senior Designer - Creates and documents brand guidelines

**Accountable:**
- Design Lead - Reviews and approves guidelines
- Client Stakeholder - Final approval of brand identity

**Consulted:**
- AI Team - Provides brand positioning input
- Client Team - Shares brand history and preferences

**Informed:**
- Development Team - Notified for implementation reference
- Content Team - Aware of brand standards for content creation

### Dependencies

- Client discovery session completed
- Brand research conducted
- Client preferences documented
- Competitor analysis completed

### Tools Required

- Figma (primary design tool)
- Adobe Illustrator (logo refinement)
- Color palette generators
- Typography pairing tools
- Design system documentation tools

### Success Criteria

- Complete logo design (primary + variations)
- Color palette defined (primary, secondary, accent colors with hex codes)
- Typography system established (headings, body, captions)
- Spacing/grid system documented
- Usage guidelines clear and comprehensive
- Client approval obtained
- Documentation accessible to all teams

### Deliverables

- Logo files (SVG, PNG, PDF in multiple sizes)
- Color palette specification document
- Typography guide with font files
- Spacing rules and grid system documentation
- Brand usage guidelines PDF

### Steps

1. **Conduct client brand discovery session**
   - Tool: Zoom, Miro, Notion
   - Responsibility: Senior Designer
   - Placement: Client folder/discovery notes
   - Duration: 60 minutes
   - Dependencies: None
   - Success Criteria: Client preferences, values, and vision documented

2. **Research competitor branding**
   - Tool: Web research, design inspiration sites
   - Responsibility: Designer
   - Placement: Research document
   - Duration: 45 minutes
   - Dependencies: Step 1
   - Success Criteria: 5-10 competitor brands analyzed for differentiation

3. **Create logo concepts**
   - Tool: Figma, Illustrator
   - Responsibility: Senior Designer
   - Placement: Figma design file
   - Duration: 90 minutes
   - Dependencies: Step 2
   - Success Criteria: 3-5 logo concepts designed

4. **Define color palette**
   - Tool: Figma, color palette generators
   - Responsibility: Designer
   - Placement: Brand guidelines document
   - Duration: 30 minutes
   - Dependencies: Step 3 (logo approved)
   - Success Criteria: Primary (2-3 colors), secondary (2-3 colors), accent (1-2 colors) defined with hex codes

5. **Select typography system**
   - Tool: Google Fonts, Adobe Fonts, font pairing tools
   - Responsibility: Designer
   - Placement: Brand guidelines document
   - Duration: 30 minutes
   - Dependencies: Step 4
   - Success Criteria: Heading font, body font, and usage rules defined

6. **Document spacing and grid rules**
   - Tool: Figma
   - Responsibility: Designer
   - Placement: Brand guidelines document
   - Duration: 30 minutes
   - Dependencies: Step 5
   - Success Criteria: 8pt or 4pt grid system defined, spacing scale documented

7. **Create usage guidelines**
   - Tool: Figma, Google Docs
   - Responsibility: Senior Designer
   - Placement: Brand guidelines PDF
   - Duration: 45 minutes
   - Dependencies: Steps 3-6
   - Success Criteria: Clear dos and don'ts, application examples included

8. **Present to client for approval**
   - Tool: Zoom, Figma presentation mode
   - Responsibility: Design Lead + Senior Designer
   - Placement: Client meeting
   - Duration: 45 minutes
   - Dependencies: Step 7
   - Success Criteria: Client approval obtained, revision notes documented

### Checklist

- [ ] Client discovery completed
  - Guide: Document brand values, target audience, preferences
  - Required: Yes

- [ ] Logo designed and approved
  - Guide: Include primary logo + 2-3 variations (horizontal, vertical, icon)
  - Required: Yes

- [ ] Color palette defined with hex codes
  - Guide: Minimum 6 colors (primary, secondary, accent)
  - Required: Yes

- [ ] Typography system documented
  - Guide: Heading font, body font, font sizes, line heights
  - Required: Yes

- [ ] Spacing rules established
  - Guide: Grid system (4pt or 8pt), padding/margin standards
  - Required: Yes

- [ ] Usage guidelines created
  - Guide: Include dos and don'ts with visual examples
  - Required: Yes

- [ ] Client approval obtained
  - Guide: Formal sign-off on all brand elements
  - Required: Yes

### Tags

design, branding, brand_guidelines, logo, typography, color_palette, client_deliverable, template

### Cross-References

**Related Entities:**
- [../Projects_Checklist-Item-003.md](../Projects_Checklist-Item-003.md) - PROJ-DESIGN-001: RH & GA Design System
- `../../BUSINESSES/Clients/` - Client records
- `../../LIBRARIES/Actions/` - "Define" action definition
- `../../LIBRARIES/Objects/` - "Brand Guidelines" object definition

---

## TASK-DEV-001: Develop Scraper Engine

**ID:** `TASK-DEV-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-06
**Last Updated:** 2025-11-10
**Source:** Projects_Milestones_Tasks_Nov05-07_2025.md (Line 520)

### Basic Information

- **Task Name:** Develop Scraper Engine for [Target Platform]
- **Action:** Develop
- **Object:** Scraper Engine
- **Tool:** Python + Selenium
- **Context:** Lead-Generation-Automation
- **Department:** Dev
- **Profession:** Backend Developer
- **Estimated Duration:** 16 hours (2 days)
- **Priority:** Critical
- **Status:** Template (Reusable)

### Description

Develop multi-threaded web scraper engine with advanced features including proxy rotation, captcha handling, and data extraction for lead generation purposes. Designed for scraping business listings from platforms like Google Maps.

### Responsibilities

**Primary Responsible:**
- Backend Developer - Develops core scraper engine and infrastructure

**Accountable:**
- Dev Team Lead - Reviews code quality and architecture decisions
- Sales Lead - Validates data quality and business requirements

**Consulted:**
- Lead Generation Team - Provides requirements for data fields
- DevOps Engineer - Advises on deployment and scaling

**Informed:**
- Sales Team - Notified when scraper is ready for use
- Data Team - Aware of new data source for analysis

### Dependencies

- Target platform URL structure analyzed
- Required data fields defined
- Proxy service subscription active
- Captcha solving service configured
- Python development environment setup
- Database schema designed

### Tools Required

- **Primary Development:**
  - Python 3.9+
  - Selenium WebDriver
  - BeautifulSoup or lxml

- **Infrastructure:**
  - Proxy rotation service (e.g., ScraperAPI, Bright Data)
  - Captcha solving service (e.g., 2Captcha, Anti-Captcha)
  - PostgreSQL or MongoDB (data storage)

- **Supporting Tools:**
  - Git (version control)
  - Docker (containerization)
  - pytest (testing)

### Success Criteria

- Scraper successfully extracts all required data fields
- Multi-threaded processing handles 50+ concurrent requests
- Proxy rotation prevents IP blocking
- Captcha handling success rate >95%
- Error handling and retry logic functional
- Data quality validation passes
- Performance: 100+ listings extracted per hour
- Code reviewed and approved
- Unit tests achieve >80% coverage
- Documentation complete

### Features

- **Core Capabilities:**
  - Multi-threaded processing
  - Proxy rotation with health checking
  - Captcha detection and solving
  - Intelligent retry logic with exponential backoff
  - Rate limiting and request throttling

- **Data Extraction:**
  - Business name
  - Address
  - Phone number
  - Website
  - Rating
  - Review count
  - Additional custom fields

- **Robustness:**
  - Error logging and monitoring
  - Session management
  - Cookie handling
  - User-agent rotation

### Steps

1. **Analyze target platform structure**
   - Tool: Browser DevTools, Python requests library
   - Responsibility: Backend Developer
   - Placement: Research documentation
   - Duration: 2 hours
   - Dependencies: None
   - Success Criteria: URL patterns, HTML structure, API endpoints (if any) documented

2. **Set up development environment**
   - Tool: Python, virtual environment, Selenium, required libraries
   - Responsibility: Backend Developer
   - Placement: Local development machine
   - Duration: 1 hour
   - Dependencies: Step 1
   - Success Criteria: All dependencies installed, test script runs successfully

3. **Implement basic scraper logic**
   - Tool: Python, Selenium
   - Responsibility: Backend Developer
   - Placement: GitHub repository
   - Duration: 4 hours
   - Dependencies: Step 2
   - Success Criteria: Basic scraper extracts data from single page successfully

4. **Add multi-threading capability**
   - Tool: Python threading or asyncio
   - Responsibility: Backend Developer
   - Placement: Scraper engine module
   - Duration: 3 hours
   - Dependencies: Step 3
   - Success Criteria: Concurrent processing of multiple URLs working

5. **Integrate proxy rotation**
   - Tool: Proxy service API, Python requests
   - Responsibility: Backend Developer
   - Placement: Proxy management module
   - Duration: 2 hours
   - Dependencies: Step 4
   - Success Criteria: Requests distributed across multiple proxies, failed proxies automatically rotated

6. **Implement captcha handling**
   - Tool: Captcha solving service API
   - Responsibility: Backend Developer
   - Placement: Captcha handling module
   - Duration: 2 hours
   - Dependencies: Step 5
   - Success Criteria: Captchas detected and solved automatically with >95% success rate

7. **Add error handling and retry logic**
   - Tool: Python exception handling, logging library
   - Responsibility: Backend Developer
   - Placement: Error handling module
   - Duration: 1 hour
   - Dependencies: Step 6
   - Success Criteria: All errors logged, failed requests retried with exponential backoff

8. **Implement data validation and storage**
   - Tool: PostgreSQL/MongoDB, data validation libraries
   - Responsibility: Backend Developer
   - Placement: Database module
   - Duration: 2 hours
   - Dependencies: Step 7
   - Success Criteria: Extracted data validated and stored in database successfully

9. **Write unit tests and documentation**
   - Tool: pytest, Markdown
   - Responsibility: Backend Developer
   - Placement: Tests folder, README.md
   - Duration: 2 hours
   - Dependencies: Step 8
   - Success Criteria: >80% code coverage, documentation complete with usage examples

10. **Code review and deployment**
    - Tool: GitHub, Docker, production server
    - Responsibility: Backend Developer + Dev Team Lead
    - Placement: Production environment
    - Duration: 1 hour
    - Dependencies: Step 9
    - Success Criteria: Code approved, deployed to production, monitoring active

### Checklist

- [ ] Target platform structure analyzed
  - Guide: Document URL patterns, HTML selectors, rate limits
  - Required: Yes

- [ ] Required data fields defined
  - Guide: List all fields to extract with example values
  - Required: Yes

- [ ] Multi-threading implemented
  - Guide: 10-50 concurrent threads depending on platform limits
  - Required: Yes

- [ ] Proxy rotation configured
  - Guide: Minimum 10 proxies in rotation pool
  - Required: Yes

- [ ] Captcha handling working
  - Guide: >95% success rate on captcha solving
  - Required: Yes

- [ ] Error handling comprehensive
  - Guide: All exceptions caught and logged properly
  - Required: Yes

- [ ] Data validation implemented
  - Guide: Validate required fields, data types, format
  - Required: Yes

- [ ] Unit tests written
  - Guide: >80% code coverage
  - Required: Yes

- [ ] Documentation complete
  - Guide: Setup instructions, usage examples, API reference
  - Required: Yes

- [ ] Code reviewed and approved
  - Guide: At least one senior developer review
  - Required: Yes

### Tags

dev, backend, web_scraping, automation, lead_generation, python, selenium, template

### Cross-References

**Related Entities:**
- [../Projects_Checklist-Item-003.md](../Projects_Checklist-Item-003.md) - PROJ-DEV-002: Google Maps Scraping System
- `../../LIBRARIES/Actions/` - "Develop" action definition
- `../../LIBRARIES/Objects/` - "Scraper Engine" object definition
- `../../LIBRARIES/Tools/` - Python, Selenium tool definitions

---

## TASK-HR-001: Audit Current Systems for Employee Data

**ID:** `TASK-HR-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-05
**Last Updated:** 2025-11-10
**Source:** Projects_Milestones_Tasks_Nov05-07_2025.md (Line 232)

### Basic Information

- **Task Name:** Audit Current Systems for Employee Data
- **Action:** Audit
- **Object:** Employee Data Systems
- **Tool:** Analysis Tools
- **Context:** HR-Systems-Integration
- **Department:** HR
- **Profession:** HR AI
- **Estimated Duration:** 8 hours (1 day)
- **Priority:** Critical
- **Status:** Template (Reusable)

### Description

Conduct comprehensive audit of all HR and employee management systems to understand data structures, identify inconsistencies, and prepare for system integration or synchronization projects.

### Responsibilities

**Primary Responsible:**
- HR AI - Conducts audit, documents findings, creates recommendations

**Accountable:**
- HR Director - Reviews findings and approves integration plan

**Consulted:**
- IT Administrator - Provides technical access and system documentation
- Systems Vendor Support - Clarifies data structures and capabilities
- Finance Team - For payroll system integration requirements

**Informed:**
- Department Leads - Aware of audit findings affecting their teams
- Executive Team - Updated on major inconsistencies or risks

### Dependencies

- Access to all HR systems (HRIS, Payroll, Directory, Access Management)
- System administrator credentials or support
- Current employee roster
- Documentation of existing systems

### Tools Required

- **HR Systems:**
  - HRIS (Human Resource Information System)
  - Payroll system
  - Employee directory
  - Access management system

- **Analysis Tools:**
  - Excel/Google Sheets (data comparison)
  - Database query tools (if applicable)
  - Documentation tools (Notion, Confluence)

### Systems to Review

1. **HRIS (Human Resource Information System)**
   - Employee personal information
   - Employment history
   - Job titles and roles
   - Department assignments
   - Manager relationships

2. **Payroll System**
   - Compensation data
   - Payment schedules
   - Tax information
   - Bank account details

3. **Employee Directory**
   - Contact information
   - Organizational structure
   - Reporting relationships
   - Office locations

4. **Access Management System**
   - System access permissions
   - Security roles
   - Active accounts
   - Access logs

### Success Criteria

- All 4+ systems audited completely
- Data fields documented for each system
- Inconsistencies identified and categorized
- Missing data documented
- Synchronization requirements defined
- Audit report completed with recommendations
- Stakeholders informed of findings

### Steps

1. **Gather system access and documentation**
   - Tool: Email, IT support tickets
   - Responsibility: HR AI
   - Placement: HR shared folder
   - Duration: 1 hour
   - Dependencies: None
   - Success Criteria: Access credentials obtained for all systems, vendor documentation collected

2. **Export employee data from HRIS**
   - Tool: HRIS export function
   - Responsibility: HR AI
   - Placement: Secure HR folder
   - Duration: 30 minutes
   - Dependencies: Step 1
   - Success Criteria: Complete employee roster with all available fields exported

3. **Export employee data from Payroll system**
   - Tool: Payroll system export function
   - Responsibility: HR AI
   - Placement: Secure HR folder
   - Duration: 30 minutes
   - Dependencies: Step 1
   - Success Criteria: Employee compensation and payment data exported

4. **Export employee data from Directory**
   - Tool: Directory export function
   - Responsibility: HR AI
   - Placement: Secure HR folder
   - Duration: 30 minutes
   - Dependencies: Step 1
   - Success Criteria: Contact information and org structure exported

5. **Export user access data from Access Management system**
   - Tool: Access Management export function
   - Responsibility: HR AI
   - Placement: Secure HR folder
   - Duration: 30 minutes
   - Dependencies: Step 1
   - Success Criteria: All user accounts and permissions exported

6. **Create master comparison spreadsheet**
   - Tool: Excel/Google Sheets
   - Responsibility: HR AI
   - Placement: HR analysis folder
   - Duration: 1 hour
   - Dependencies: Steps 2-5
   - Success Criteria: All data sources combined in single spreadsheet with employee ID as key

7. **Identify data inconsistencies**
   - Tool: Excel formulas, manual review
   - Responsibility: HR AI
   - Placement: Analysis spreadsheet
   - Duration: 2 hours
   - Dependencies: Step 6
   - Success Criteria: All inconsistencies flagged (name mismatches, missing data, status conflicts)

8. **Categorize and prioritize issues**
   - Tool: Excel, documentation tool
   - Responsibility: HR AI
   - Placement: Findings document
   - Duration: 1 hour
   - Dependencies: Step 7
   - Success Criteria: Issues categorized by severity (Critical, High, Medium, Low)

9. **Document synchronization requirements**
   - Tool: Notion, Google Docs
   - Responsibility: HR AI
   - Placement: Requirements document
   - Duration: 1 hour
   - Dependencies: Step 8
   - Success Criteria: Clear requirements defined for system integration

10. **Create audit report with recommendations**
    - Tool: Google Docs, PowerPoint
    - Responsibility: HR AI
    - Placement: HR reports folder
    - Duration: 1.5 hours
    - Dependencies: Steps 7-9
    - Success Criteria: Comprehensive report with executive summary, findings, and actionable recommendations

### Checklist

- [ ] Access obtained to all HR systems
  - Guide: HRIS, Payroll, Directory, Access Management
  - Required: Yes

- [ ] Data exported from all systems
  - Guide: Complete employee datasets with all available fields
  - Required: Yes

- [ ] Master comparison spreadsheet created
  - Guide: All systems data combined with employee ID as key
  - Required: Yes

- [ ] Inconsistencies identified and documented
  - Guide: Name mismatches, missing data, status conflicts, duplicate records
  - Required: Yes

- [ ] Issues categorized by severity
  - Guide: Critical (security risks), High (data integrity), Medium (usability), Low (cosmetic)
  - Required: Yes

- [ ] Synchronization requirements defined
  - Guide: Which fields to sync, sync frequency, master data source
  - Required: Yes

- [ ] Audit report completed
  - Guide: Executive summary, detailed findings, recommendations, timeline
  - Required: Yes

- [ ] Stakeholders informed
  - Guide: HR Director, IT AI, relevant department leads
  - Required: Yes

### Expected Findings

- Name spelling variations across systems
- Missing employee records in some systems
- Outdated department assignments
- Inconsistent job titles
- Missing contact information
- Incorrect manager relationships
- Orphaned access accounts
- Duplicate employee records

### Tags

hr, audit, employee_data, systems_integration, hris, payroll, data_quality, template

### Cross-References

**Related Entities:**
- [../Projects_Checklist-Item-003.md](../Projects_Checklist-Item-003.md) - PROJ-HR-001: Employee Sync Automation
- `../../TALENTS/Employees/` - Employee master data
- `../../LIBRARIES/Actions/` - "Audit" action definition
- `../../LIBRARIES/Objects/` - "Employee Data Systems" object definition

---

## TASK-AI-001: Compress Main Prompt Using Summarization Techniques

**ID:** `TASK-AI-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-04
**Last Updated:** 2025-11-10
**Source:** 4th of November Summary.md (Line 30)

### Basic Information

- **Task Name:** Compress Main Prompt Using Summarization Techniques
- **Action:** Compress
- **Object:** Main Prompt
- **Tool:** Claude + ChatGPT
- **Context:** Prompt-Optimization
- **Department:** AI
- **Profession:** AI Engineer
- **Estimated Duration:** 2 days
- **Priority:** High
- **Status:** Template (Reusable)

### Description

Optimize large AI prompts by compressing them using advanced summarization techniques while maintaining semantic richness and functionality. Reduces token usage and improves processing efficiency.

### Responsibilities

**Primary Responsible:**
- AI Engineer - Performs compression, tests output quality, iterates

**Accountable:**
- AI Team Lead - Reviews compressed prompts for quality and effectiveness

**Consulted:**
- Department Leads - Validate that compressed prompts meet their use cases
- Prompt Users - Provide feedback on compressed prompt performance

**Informed:**
- Development Team - Notified of new prompt versions for integration
- Operations Team - Aware of token usage improvements

### Dependencies

- Original prompt documented and versioned
- Use cases and requirements clearly defined
- Access to AI models (Claude, ChatGPT)
- Test dataset for validation
- Performance benchmarks established

### Tools Required

- **AI Models:**
  - Claude (Anthropic) - for summarization and compression
  - ChatGPT (OpenAI) - for alternative compression approaches

- **Development Tools:**
  - Cursor or VS Code - for prompt editing
  - Git - for version control
  - Markdown editor - for documentation

- **Testing Tools:**
  - Test case suite
  - Performance monitoring tools
  - Token counting utilities

### Success Criteria

- Token count reduced by 30-50%
- Semantic meaning preserved (95%+ similarity)
- Output quality maintained (tested against validation set)
- Compression techniques documented
- Before/after comparison documented
- All use cases still supported
- Performance improvements quantified
- New prompt version deployed

### Compression Methodologies

1. **Semantic Compression:**
   - Remove redundant explanations
   - Consolidate similar instructions
   - Use more concise phrasing

2. **Structural Optimization:**
   - Eliminate unnecessary examples
   - Combine related sections
   - Use bullet points instead of paragraphs

3. **Information Density:**
   - Replace verbose descriptions with precise terminology
   - Use abbreviations for repeated concepts
   - Remove filler words and phrases

4. **Hierarchical Summarization:**
   - Summarize sections independently
   - Preserve critical instructions
   - Maintain logical flow

### Steps

1. **Analyze original prompt structure**
   - Tool: Text editor, Claude
   - Responsibility: AI Engineer
   - Placement: Analysis document
   - Duration: 2 hours
   - Dependencies: None
   - Success Criteria: Prompt sections identified, token count baseline established, redundancies noted

2. **Define compression requirements**
   - Tool: Documentation tool
   - Responsibility: AI Engineer
   - Placement: Requirements document
   - Duration: 1 hour
   - Dependencies: Step 1
   - Success Criteria: Target token reduction defined, critical elements identified, quality metrics established

3. **Create test validation set**
   - Tool: Test case documentation
   - Responsibility: AI Engineer
   - Placement: Test suite folder
   - Duration: 2 hours
   - Dependencies: Step 2
   - Success Criteria: 10-20 test cases covering all prompt use cases

4. **Run baseline performance tests**
   - Tool: AI model API, testing framework
   - Responsibility: AI Engineer
   - Placement: Test results folder
   - Duration: 1 hour
   - Dependencies: Step 3
   - Success Criteria: Baseline quality scores and performance metrics recorded

5. **Apply semantic compression (Round 1)**
   - Tool: Claude, manual editing
   - Responsibility: AI Engineer
   - Placement: Prompt versions folder
   - Duration: 4 hours
   - Dependencies: Step 4
   - Success Criteria: First compressed version created, 15-20% token reduction achieved

6. **Test compressed version (Round 1)**
   - Tool: Test validation set
   - Responsibility: AI Engineer
   - Placement: Test results folder
   - Duration: 2 hours
   - Dependencies: Step 5
   - Success Criteria: Quality metrics compared to baseline, issues documented

7. **Apply structural optimization (Round 2)**
   - Tool: Claude, ChatGPT, manual editing
   - Responsibility: AI Engineer
   - Placement: Prompt versions folder
   - Duration: 4 hours
   - Dependencies: Step 6
   - Success Criteria: Second compressed version created, 30-50% total token reduction achieved

8. **Test compressed version (Round 2)**
   - Tool: Test validation set
   - Responsibility: AI Engineer
   - Placement: Test results folder
   - Duration: 2 hours
   - Dependencies: Step 7
   - Success Criteria: Quality maintained at 95%+ of baseline, edge cases validated

9. **Document compression techniques**
   - Tool: Markdown, documentation tool
   - Responsibility: AI Engineer
   - Placement: Documentation folder
   - Duration: 1.5 hours
   - Dependencies: Step 8
   - Success Criteria: Before/after comparison, techniques used, performance improvements documented

10. **Review and deploy new prompt version**
    - Tool: Git, deployment system
    - Responsibility: AI Engineer + AI Team Lead
    - Placement: Production environment
    - Duration: 1 hour
    - Dependencies: Step 9
    - Success Criteria: Compressed prompt reviewed, approved, deployed, monitored

### Checklist

- [ ] Original prompt analyzed
  - Guide: Token count, section breakdown, redundancy analysis
  - Required: Yes

- [ ] Compression targets defined
  - Guide: 30-50% token reduction while maintaining 95%+ quality
  - Required: Yes

- [ ] Test validation set created
  - Guide: 10-20 diverse test cases covering all use cases
  - Required: Yes

- [ ] Baseline performance measured
  - Guide: Quality scores, token count, latency recorded
  - Required: Yes

- [ ] Semantic compression applied
  - Guide: Remove redundancy, consolidate instructions
  - Required: Yes

- [ ] Structural optimization applied
  - Guide: Reorganize sections, use concise formatting
  - Required: Yes

- [ ] Compressed version tested
  - Guide: All test cases pass, quality maintained
  - Required: Yes

- [ ] Compression techniques documented
  - Guide: Before/after examples, methods used, results quantified
  - Required: Yes

- [ ] New version reviewed and approved
  - Guide: AI Team Lead sign-off obtained
  - Required: Yes

### Performance Metrics

**Measure These:**
- Token count (before/after)
- Semantic similarity score
- Output quality score
- Test case pass rate
- Processing latency
- Cost savings (tokens × price per token)

**Example Target:**
- Original: 5000 tokens → Compressed: 2500 tokens (50% reduction)
- Semantic similarity: 97%
- Test pass rate: 100%
- Cost savings: ~50% per API call

### Tags

ai, prompt_engineering, optimization, compression, summarization, token_reduction, template

### Cross-References

**Related Entities:**
- [../Projects_Checklist-Item-003.md](../Projects_Checklist-Item-003.md) - PROJ-AI-001: AI-Powered Prompt System Development
- `../../LIBRARIES/Actions/` - "Compress" action definition
- `../../LIBRARIES/Objects/` - "Main Prompt" object definition
- `../../LIBRARIES/Tools/` - Claude, ChatGPT tool definitions

---

## TASK-SALES-001: Conduct Deep Research on Modern Sales Methodologies

**ID:** `TASK-SALES-001`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-04
**Last Updated:** 2025-11-10
**Source:** 4th of November Summary.md (Line 183)

### Basic Information

- **Task Name:** Conduct Deep Research on Modern Sales Methodologies
- **Action:** Research
- **Object:** Sales Methodologies
- **Tool:** Perplexity + ChatGPT + Claude
- **Context:** AI-Era-Sales
- **Department:** Sales
- **Profession:** Sales Manager
- **Estimated Duration:** 1 week
- **Priority:** High
- **Status:** Template (Reusable)

### Description

Conduct comprehensive research on modern sales methodologies adapted for the AI era, including consultative selling, solution selling, SPIN selling, Challenger Sale, and AI-augmented sales techniques.

### Responsibilities

**Primary Responsible:**
- Sales Manager - Conducts research, synthesizes findings, creates recommendations

**Accountable:**
- Sales Director - Reviews research findings and approves new methodologies

**Consulted:**
- AI Team - Provides insights on AI tool capabilities for sales
- Top Performers - Share practical experience with current methods
- Industry Experts - External consultants or thought leaders

**Informed:**
- Sales Team - Receives research findings and training recommendations
- Leadership Team - Updated on sales strategy evolution

### Dependencies

- Access to research tools (Perplexity, ChatGPT, Claude)
- Current sales process documentation
- Sales performance data for baseline
- Time allocated for research activities

### Tools Required

- **Research Platforms:**
  - Perplexity - AI-powered research with sources
  - ChatGPT - Analysis and synthesis
  - Claude - Long-form research and summarization

- **Documentation:**
  - Notion - Research repository
  - Google Docs - Report writing
  - Miro - Methodology mapping

- **Data Sources:**
  - Sales books and publications
  - Industry reports (Gartner, Forrester)
  - YouTube/podcasts (sales thought leaders)
  - LinkedIn Learning courses

### Success Criteria

- 5+ modern sales methodologies researched in depth
- AI-augmented sales techniques identified and documented
- Best practices for B2B/B2C documented separately
- Competitive analysis of methodologies completed
- Implementation recommendations created
- Research report completed (20-30 pages)
- Presentation to sales team delivered
- Training plan proposed

### Research Topics

1. **Core Methodologies:**
   - Consultative Selling
   - Solution Selling
   - SPIN Selling (Situation, Problem, Implication, Need-payoff)
   - Challenger Sale
   - MEDDIC (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion)
   - Sandler Selling System

2. **AI-Era Adaptations:**
   - AI-powered lead qualification
   - Automated personalization at scale
   - Predictive analytics for sales forecasting
   - AI-assisted objection handling
   - Chatbot pre-qualification
   - AI-generated email campaigns

3. **Supporting Topics:**
   - Sales psychology and neuroscience
   - Buyer journey mapping
   - Value proposition development
   - Negotiation techniques
   - Relationship building in digital age

### Steps

1. **Define research scope and objectives**
   - Tool: Notion, documentation tool
   - Responsibility: Sales Manager
   - Placement: Research project folder
   - Duration: 2 hours
   - Dependencies: None
   - Success Criteria: Research questions defined, success criteria established, timeline created

2. **Research consultative and solution selling**
   - Tool: Perplexity, books, articles
   - Responsibility: Sales Manager
   - Placement: Research notes
   - Duration: 1 day
   - Dependencies: Step 1
   - Success Criteria: Core principles, processes, pros/cons documented

3. **Research SPIN and Challenger methodologies**
   - Tool: Perplexity, books, courses
   - Responsibility: Sales Manager
   - Placement: Research notes
   - Duration: 1 day
   - Dependencies: Step 1
   - Success Criteria: Questioning frameworks, techniques, case studies documented

4. **Research AI-augmented sales techniques**
   - Tool: Perplexity, ChatGPT, Claude, industry reports
   - Responsibility: Sales Manager
   - Placement: Research notes
   - Duration: 1 day
   - Dependencies: Step 1
   - Success Criteria: AI tools, use cases, ROI data, implementation examples documented

5. **Analyze current sales process**
   - Tool: Process documentation, CRM data
   - Responsibility: Sales Manager
   - Placement: Analysis document
   - Duration: 4 hours
   - Dependencies: Steps 2-4
   - Success Criteria: Current process mapped, gaps identified, improvement opportunities noted

6. **Compare methodologies for fit**
   - Tool: Comparison matrix, Miro
   - Responsibility: Sales Manager
   - Placement: Comparison document
   - Duration: 4 hours
   - Dependencies: Steps 2-5
   - Success Criteria: Methodologies scored against criteria (complexity, training required, fit with product, scalability)

7. **Interview top sales performers**
   - Tool: Zoom, note-taking
   - Responsibility: Sales Manager
   - Placement: Interview notes
   - Duration: 4 hours (4 interviews × 1 hour)
   - Dependencies: Step 5
   - Success Criteria: Practical insights captured, current methodology gaps identified

8. **Synthesize findings and create recommendations**
   - Tool: ChatGPT, Claude, Google Docs
   - Responsibility: Sales Manager
   - Placement: Recommendations document
   - Duration: 1 day
   - Dependencies: Steps 2-7
   - Success Criteria: Top 2-3 methodologies recommended with rationale, implementation roadmap created

9. **Create comprehensive research report**
   - Tool: Google Docs, Notion
   - Responsibility: Sales Manager
   - Placement: Final reports folder
   - Duration: 1 day
   - Dependencies: Step 8
   - Success Criteria: 20-30 page report with executive summary, methodology overviews, recommendations, training plan

10. **Present findings to stakeholders**
    - Tool: PowerPoint, Zoom
    - Responsibility: Sales Manager
    - Placement: Stakeholder meeting
    - Duration: 1 hour
    - Dependencies: Step 9
    - Success Criteria: Presentation delivered, feedback collected, next steps agreed upon

### Checklist

- [ ] Research objectives defined
  - Guide: What questions to answer, what decisions to inform
  - Required: Yes

- [ ] 5+ methodologies researched
  - Guide: Core principles, process, tools, pros/cons for each
  - Required: Yes

- [ ] AI-augmented techniques documented
  - Guide: Specific AI tools, use cases, ROI data
  - Required: Yes

- [ ] Current sales process analyzed
  - Guide: Process map, performance data, gaps identified
  - Required: Yes

- [ ] Methodology comparison completed
  - Guide: Scoring matrix with weighted criteria
  - Required: Yes

- [ ] Top performers interviewed
  - Guide: 3-5 interviews capturing practical insights
  - Required: Yes

- [ ] Recommendations created
  - Guide: Top 2-3 methodologies with implementation roadmap
  - Required: Yes

- [ ] Research report completed
  - Guide: 20-30 pages, executive summary, detailed findings
  - Required: Yes

- [ ] Presentation delivered
  - Guide: Stakeholder meeting, feedback collected
  - Required: Yes

### Deliverables

- Research notes and annotated bibliography
- Methodology comparison matrix
- Interview summaries
- Comprehensive research report (20-30 pages)
- Executive summary (2 pages)
- Presentation deck
- Proposed training plan
- Implementation roadmap

### Tags

sales, research, methodology, consultative_selling, ai_sales, strategy, training, template

### Cross-References

**Related Entities:**
- `../../LIBRARIES/Actions/` - "Research" action definition
- `../../LIBRARIES/Objects/` - "Sales Methodologies" object definition
- `../../LIBRARIES/Tools/` - Perplexity, ChatGPT, Claude tool definitions
- `../../BUSINESSES/Sales_Process/` - Current sales process documentation

---

## TASK-SALES-002: Restructure Sales Client Folders

**ID:** `TASK-SALES-002`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-05
**Last Updated:** 2025-11-10
**Source:** 05Nov25_structured.md (Line 25)

### Basic Information

- **Task Name:** Restructure Sales Client Folders
- **Action:** Organize
- **Object:** Client Folders
- **Tool:** Dropbox + CRM
- **Context:** Client-History-Management
- **Department:** Sales
- **Profession:** Sales Manager
- **Estimated Duration:** 1 week
- **Priority:** Critical
- **Status:** Template (Reusable)

### Description

Build structured client-correspondence folders so managers can retrieve full client histories within seconds. Enables quick context retrieval for sales calls, follow-ups, and client relationship management.

### Responsibilities

**Primary Responsible:**
- Sales Manager - Executes folder restructuring, implements naming conventions

**Accountable:**
- Sales Director - Approves folder structure and ensures team adoption

**Consulted:**
- Operations Team - Provides guidance on file organization standards
- IT AI - Assists with bulk operations and permissions
- CRM Administrator - Ensures folder structure aligns with CRM records

**Informed:**
- Sales Team - Trained on new folder structure and usage
- Customer Success - Aware of new client history access method

### Dependencies

- Access to Sales Dropbox folder
- List of all current and past clients
- Legacy folder structure documented
- Naming convention defined
- Backup of existing folders completed

### Tools Required

- **Primary:**
  - Dropbox (file storage and organization)
  - CRM (client data reference)

- **Supporting:**
  - Excel/Google Sheets (client list and mapping)
  - Bulk renaming tools (if needed)
  - Automation scripts (optional, for large-scale operations)

### Success Criteria

- All client folders follow standardized naming convention
- Folder structure consistent across all clients
- Any manager can access complete client history in <10 seconds
- All correspondence organized chronologically
- Missing client folders created
- Old/redundant files archived
- Team trained on new structure
- Adoption rate >90% within 2 weeks

### Folder Structure Template

```
Sales/
├── Active_Clients/
│   ├── [ClientID]_[ClientName]_[Status]/
│   │   ├── 01_Correspondence/
│   │   │   ├── Emails/
│   │   │   ├── Call_Notes/
│   │   │   └── Meeting_Minutes/
│   │   ├── 02_Proposals/
│   │   ├── 03_Contracts/
│   │   ├── 04_Invoices/
│   │   ├── 05_Deliverables/
│   │   └── 06_Archive/
│   └── ...
├── Past_Clients/
│   └── [Same structure as Active_Clients]
└── Prospects/
    └── [Same structure as Active_Clients]
```

### Naming Convention

**Format:** `[ClientID]_[Date]_[ShortName]_[DeptISO]`

**Examples:**
- `CL-001_20251105_Acme_SALES`
- `CL-027_20241215_TechStartup_SALES`

**Rules:**
- ClientID: CL-XXX (3 digits)
- Date: YYYYMMDD format
- ShortName: 1-3 words, no spaces (use underscores)
- DeptISO: Department code (SALES, HR, DEV, etc.)

### Steps

1. **Document current folder structure**
   - Tool: Dropbox, Excel
   - Responsibility: Sales Manager
   - Placement: Documentation folder
   - Duration: 4 hours
   - Dependencies: None
   - Success Criteria: Current structure mapped, all client folders listed, issues documented

2. **Define new folder taxonomy**
   - Tool: Documentation tool, Miro
   - Responsibility: Sales Manager + Operations
   - Placement: Standards documentation
   - Duration: 2 hours
   - Dependencies: Step 1
   - Success Criteria: Folder structure template created, naming convention defined, approved by stakeholders

3. **Create client ID mapping**
   - Tool: Excel/Google Sheets, CRM
   - Responsibility: Sales Manager
   - Placement: Reference spreadsheet
   - Duration: 3 hours
   - Dependencies: Step 2
   - Success Criteria: All clients assigned unique IDs, mapping spreadsheet created

4. **Backup existing folders**
   - Tool: Dropbox backup feature
   - Responsibility: Sales Manager + IT AI
   - Placement: Backup location
   - Duration: 1 hour
   - Dependencies: None (parallel to Steps 1-3)
   - Success Criteria: Complete backup verified, restore tested

5. **Create new folder structure template**
   - Tool: Dropbox
   - Responsibility: Sales Manager
   - Placement: Sales root folder
   - Duration: 2 hours
   - Dependencies: Steps 2-3
   - Success Criteria: Active_Clients, Past_Clients, Prospects folders created with subfolder templates

6. **Migrate active client folders (Phase 1)**
   - Tool: Dropbox, manual or bulk operations
   - Responsibility: Sales Manager
   - Placement: Active_Clients folder
   - Duration: 2 days
   - Dependencies: Steps 3-5
   - Success Criteria: 50+ active client folders migrated, files organized into subfolders

7. **Migrate past client folders (Phase 2)**
   - Tool: Dropbox, bulk operations
   - Responsibility: Sales Manager
   - Placement: Past_Clients folder
   - Duration: 1 day
   - Dependencies: Step 6
   - Success Criteria: Past client folders migrated and archived properly

8. **Apply consistent naming convention**
   - Tool: Bulk renaming tool or manual
   - Responsibility: Sales Manager
   - Placement: All client folders
   - Duration: 1 day
   - Dependencies: Steps 6-7
   - Success Criteria: All folders renamed following [ClientID]_[Date]_[ShortName]_[DeptISO] format

9. **Update CRM with folder links**
   - Tool: CRM
   - Responsibility: Sales Manager
   - Placement: CRM client records
   - Duration: 4 hours
   - Dependencies: Step 8
   - Success Criteria: Folder links added to all active client CRM records

10. **Create documentation and train team**
    - Tool: Notion, Zoom
    - Responsibility: Sales Manager
    - Placement: Team knowledge base
    - Duration: 4 hours
    - Dependencies: Steps 6-9
    - Success Criteria: How-to guide created, team training session conducted, Q&A completed

11. **Monitor adoption and provide support**
    - Tool: Usage analytics, team feedback
    - Responsibility: Sales Manager
    - Placement: Ongoing
    - Duration: 2 weeks
    - Dependencies: Step 10
    - Success Criteria: 90%+ team adoption, support tickets resolved, feedback incorporated

### Checklist

- [ ] Current folder structure documented
  - Guide: Map existing structure, list all client folders, identify issues
  - Required: Yes

- [ ] New folder taxonomy defined
  - Guide: Structure template and naming convention approved
  - Required: Yes

- [ ] Client IDs assigned
  - Guide: All clients have unique IDs in mapping spreadsheet
  - Required: Yes

- [ ] Backup completed
  - Guide: Full backup of existing folders verified
  - Required: Yes

- [ ] Active clients migrated
  - Guide: All active client folders restructured
  - Required: Yes

- [ ] Past clients migrated
  - Guide: All past client folders archived properly
  - Required: Yes

- [ ] Naming convention applied
  - Guide: 100% of folders follow standard format
  - Required: Yes

- [ ] CRM updated
  - Guide: Folder links added to active client records
  - Required: Yes

- [ ] Team trained
  - Guide: Training session conducted, documentation provided
  - Required: Yes

- [ ] Adoption monitored
  - Guide: 90%+ team using new structure within 2 weeks
  - Required: Yes

### Tags

sales, file_organization, client_management, folder_structure, crm, operations, template

### Cross-References

**Related Entities:**
- `../../BUSINESSES/Clients/` - Client master data
- `../../LIBRARIES/Actions/` - "Organize" action definition
- `../../LIBRARIES/Objects/` - "Client Folders" object definition
- `../../SETTINGS/File_Naming_Standards/` - Organization-wide naming conventions

---

## TASK-HR-002: Deploy Instagram DM Recruiting Templates

**ID:** `TASK-HR-002`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-05
**Last Updated:** 2025-11-10
**Source:** 05Nov25_structured.md (Line 102)

### Basic Information

- **Task Name:** Deploy Instagram DM Recruiting Templates
- **Action:** Implement
- **Object:** Recruiting Templates
- **Tool:** Instagram + Telegram
- **Context:** Instagram-Candidate-Communication
- **Department:** HR
- **Profession:** Recruiter
- **Estimated Duration:** 3 days
- **Priority:** High
- **Status:** Template (Reusable)

### Description

Roll out new recruiter Task Templates for communicating with remote candidates via Instagram DMs and Telegram. Standardizes messaging for vacancy confirmation, language assessment, interview scheduling, and follow-ups.

### Responsibilities

**Primary Responsible:**
- Recruiter - Uses templates for candidate communication, provides feedback

**Accountable:**
- HR Manager - Reviews templates for effectiveness, approves rollout

**Consulted:**
- Top Recruiters - Share best practices for Instagram recruiting
- Legal/Compliance - Reviews messaging for compliance
- AI Team - Reviews messaging for brand consistency

**Informed:**
- HR Team - Aware of new templates and usage guidelines
- Hiring Managers - Informed about improved candidate experience

### Dependencies

- Instagram DM recruiting process documented
- Candidate communication workflow defined
- Template approval process established
- Recruiter training scheduled

### Tools Required

- **Primary Communication:**
  - Instagram Direct Messages
  - Telegram

- **Supporting:**
  - Template management tool (Notion, Google Docs)
  - Text expander tool (optional, for efficiency)
  - CRM or ATS (for logging communications)

### Success Criteria

- 5+ message templates created covering all recruiting stages
- Templates tested with 10+ candidates
- Response rates measured and improved
- Templates approved by HR Manager
- All recruiters trained on usage
- Usage compliance >90%
- Candidate satisfaction improved
- Time-to-respond reduced by 30%

### Template Categories

1. **Vacancy Interest Confirmation**
   - Reconfirm interest after delays/travel
   - Verify role details
   - Set expectations

2. **Language & Communication Assessment**
   - Ask about proficiency levels
   - Understand communication preferences
   - Set language expectations

3. **Interview Scheduling**
   - Offer time slots
   - Confirm final time
   - Handle rescheduling
   - Send pre-interview instructions

4. **Application Materials Collection**
   - Request resume/portfolio
   - Specify format requirements
   - Set submission deadline

5. **Follow-up & Status Updates**
   - Thank candidates for applications
   - Provide process timeline updates
   - Notify of decisions (positive/negative)

### Steps

1. **Research best practices for Instagram recruiting**
   - Tool: Online research, recruiter communities
   - Responsibility: HR Manager
   - Placement: Research notes
   - Duration: 3 hours
   - Dependencies: None
   - Success Criteria: Best practices documented, tone guidelines defined

2. **Draft message templates for all 5 categories**
   - Tool: Google Docs, Notion
   - Responsibility: HR Manager + Senior Recruiter
   - Placement: Templates folder
   - Duration: 1 day
   - Dependencies: Step 1
   - Success Criteria: 5+ templates drafted with variables for personalization

3. **Review templates for compliance and brand**
   - Tool: Review process
   - Responsibility: Legal, AI, HR Manager
   - Placement: Review feedback document
   - Duration: 4 hours
   - Dependencies: Step 2
   - Success Criteria: All templates approved or feedback provided for revision

4. **Revise templates based on feedback**
   - Tool: Google Docs
   - Responsibility: HR Manager
   - Placement: Templates folder
   - Duration: 2 hours
   - Dependencies: Step 3
   - Success Criteria: All feedback incorporated, final approval obtained

5. **Create template usage guide**
   - Tool: Notion, Google Docs
   - Responsibility: HR Manager
   - Placement: Recruiter knowledge base
   - Duration: 3 hours
   - Dependencies: Step 4
   - Success Criteria: Guide includes when to use each template, personalization tips, examples

6. **Set up templates in tools**
   - Tool: Text expander, template management system
   - Responsibility: HR Manager
   - Placement: Recruiter tools
   - Duration: 2 hours
   - Dependencies: Step 4
   - Success Criteria: Templates easily accessible for quick use

7. **Train recruiters on template usage**
   - Tool: Zoom, training materials
   - Responsibility: HR Manager
   - Placement: Training session
   - Duration: 2 hours
   - Dependencies: Steps 5-6
   - Success Criteria: All recruiters trained, Q&A completed, role-play exercises conducted

8. **Pilot templates with 10-15 candidates**
   - Tool: Instagram, Telegram
   - Responsibility: Recruiters
   - Placement: Live recruiting
   - Duration: 1 week
   - Dependencies: Step 7
   - Success Criteria: Templates used in real scenarios, feedback collected

9. **Analyze pilot results and refine**
   - Tool: Response rate data, feedback survey
   - Responsibility: HR Manager
   - Placement: Analysis document
   - Duration: 3 hours
   - Dependencies: Step 8
   - Success Criteria: Response rates measured, feedback analyzed, templates refined

10. **Full rollout and ongoing monitoring**
    - Tool: Usage tracking, feedback collection
    - Responsibility: HR Manager
    - Placement: Ongoing
    - Duration: Ongoing
    - Dependencies: Step 9
    - Success Criteria: 90%+ recruiter usage, metrics tracked monthly, continuous improvement

### Checklist

- [ ] Best practices researched
  - Guide: Instagram recruiting dos and don'ts, tone guidelines
  - Required: Yes

- [ ] 5+ templates created
  - Guide: Cover all recruiting stages with personalization variables
  - Required: Yes

- [ ] Compliance and brand review completed
  - Guide: Legal and marketing approval obtained
  - Required: Yes

- [ ] Usage guide created
  - Guide: When to use, how to personalize, examples included
  - Required: Yes

- [ ] Templates set up in tools
  - Guide: Easily accessible for recruiters (text expander, shortcuts)
  - Required: Yes

- [ ] Recruiters trained
  - Guide: All recruiters completed training, Q&A conducted
  - Required: Yes

- [ ] Pilot completed
  - Guide: 10-15 candidates engaged using templates
  - Required: Yes

- [ ] Results analyzed
  - Guide: Response rates, feedback, refinements documented
  - Required: Yes

- [ ] Full rollout executed
  - Guide: All recruiters using templates, compliance >90%
  - Required: Yes

### Sample Template Structure

**Template: Vacancy Interest Confirmation**
```
Hi [Candidate_Name]! 👋

Hope you're doing well! We wanted to check in about the [Job_Title] position we discussed [Time_Frame] ago.

Are you still interested in learning more about this role? We'd love to continue the conversation!

Just to recap:
• Position: [Job_Title]
• Type: [Full-time/Part-time/Contract]
• Location: [Remote/Office/Hybrid]

Let me know if you'd like to move forward! 😊

Best,
[Recruiter_Name]
[Company]
```

### Tags

hr, recruiting, templates, instagram, telegram, candidate_communication, remote_recruiting, template

### Cross-References

**Related Entities:**
- `../../TALENTS/Candidates/` - Candidate records
- `../../JOBS/Open_Positions/` - Job postings
- `../../LIBRARIES/Actions/` - "Implement" action definition
- `../../LIBRARIES/Objects/` - "Recruiting Templates" object definition

---

## TASK-SALES-003: Inventory and Relaunch Social Accounts

**ID:** `TASK-SALES-003`
**Status:** Active
**Version:** 1.0
**Created:** 2025-11-06
**Last Updated:** 2025-11-10
**Source:** 061125_structured.md (Line 29)

### Basic Information

- **Task Name:** Inventory and Relaunch Social Accounts
- **Action:** Audit
- **Object:** Social Accounts
- **Tool:** Main Prompt v2
- **Context:** Social-Media-Relaunch
- **Department:** Sales
- **Profession:** SMM Manager
- **Estimated Duration:** 1 day
- **Priority:** High
- **Status:** Template (Reusable)

### Description

Use AI tools (Main Prompt v2) to scan department folders and list current Instagram/social accounts to identify dormant accounts and reopen advertising campaigns.

### Responsibilities

**Primary Responsible:**
- SMM Manager - Conducts audit, creates account inventory, plans relaunch

**Accountable:**
- Sales Director - Approves relaunch strategy and budget allocation

**Consulted:**
- Department Leads - Provide access to department folders, confirm account ownership
- AI Team - Advises on relaunch best practices
- Finance Team - Approves ad budget allocation

**Informed:**
- Sales Team - Aware of relaunched accounts and campaigns
- Content Team - Notified for content support

### Dependencies

- Access to shared Dropbox/Google Drive
- Main Prompt v2 configured
- Social media account credentials
- Ad account access
- Budget approved for ad campaigns

### Tools Required

- **Audit Tools:**
  - Main Prompt v2 (AI file scanning)
  - File search tools
  - Excel/Google Sheets (account inventory)

- **Social Media Platforms:**
  - Instagram
  - Facebook Business Manager
  - TikTok (if applicable)
  - LinkedIn (if applicable)

- **Ad Management:**
  - Meta Ads Manager
  - TikTok Ads Manager

### Success Criteria

- All social accounts identified and inventoried
- Account status determined (active, dormant, suspended)
- Dormant accounts accessed and reactivated
- Ad accounts reconnected
- Relaunch strategy created for each account
- At least 3 accounts relaunched with ads running
- Performance baseline established for tracking

### Steps

1. **Configure Main Prompt v2 for file scanning**
   - Tool: Main Prompt v2, AI tool
   - Responsibility: SMM Manager
   - Placement: AI tool configuration
   - Duration: 30 minutes
   - Dependencies: None
   - Success Criteria: Main Prompt v2 configured to scan for social media references (account names, usernames, links)

2. **Scan department folders for social accounts**
   - Tool: Main Prompt v2
   - Responsibility: SMM Manager
   - Placement: Department shared folders
   - Duration: 2 hours
   - Dependencies: Step 1
   - Success Criteria: All Instagram, Facebook, TikTok, LinkedIn accounts found and listed

3. **Create account inventory spreadsheet**
   - Tool: Excel/Google Sheets
   - Responsibility: SMM Manager
   - Placement: Social media folder
   - Duration: 1 hour
   - Dependencies: Step 2
   - Success Criteria: Spreadsheet includes: Account name, Platform, Username, Followers, Last post date, Status, Owner, Access

4. **Verify account access**
   - Tool: Social media platforms
   - Responsibility: SMM Manager
   - Placement: Login testing
   - Duration: 2 hours
   - Dependencies: Step 3
   - Success Criteria: Access status confirmed for all accounts (accessible, locked, credentials missing)

5. **Recover access to locked accounts**
   - Tool: Platform recovery tools, admin access
   - Responsibility: SMM Manager + IT AI
   - Placement: Account recovery process
   - Duration: 3 hours
   - Dependencies: Step 4
   - Success Criteria: Access recovered or recovery plan created for locked accounts

6. **Assess account health and performance**
   - Tool: Platform analytics
   - Responsibility: SMM Manager
   - Placement: Analysis document
   - Duration: 2 hours
   - Dependencies: Step 5
   - Success Criteria: Follower count, engagement rate, last activity documented for each account

7. **Prioritize accounts for relaunch**
   - Tool: Scoring matrix
   - Responsibility: SMM Manager
   - Placement: Prioritization document
   - Duration: 1 hour
   - Dependencies: Step 6
   - Success Criteria: Accounts ranked by potential (follower base, past performance, niche relevance)

8. **Reconnect ad accounts**
   - Tool: Meta Ads Manager, TikTok Ads Manager
   - Responsibility: SMM Manager
   - Placement: Ad platforms
   - Duration: 2 hours
   - Dependencies: Steps 5-7
   - Success Criteria: Ad accounts linked to social accounts, payment methods verified

9. **Create relaunch content strategy**
   - Tool: Content planning tool, AI tools
   - Responsibility: SMM Manager
   - Placement: Content calendar
   - Duration: 3 hours
   - Dependencies: Step 7
   - Success Criteria: Content themes, posting frequency, ad creatives planned for top 3-5 accounts

10. **Launch ad campaigns**
    - Tool: Meta Ads Manager, TikTok Ads Manager
    - Responsibility: SMM Manager
    - Placement: Ad platforms
    - Duration: 2 hours
    - Dependencies: Steps 8-9
    - Success Criteria: Ads launched for at least 3 accounts, budgets allocated, performance tracking enabled

### Checklist

- [ ] Main Prompt v2 configured for scanning
  - Guide: Set up to detect social media references in files
  - Required: Yes

- [ ] Department folders scanned
  - Guide: Search Dropbox, Google Drive, shared folders
  - Required: Yes

- [ ] Account inventory created
  - Guide: Spreadsheet with all accounts and key details
  - Required: Yes

- [ ] Account access verified
  - Guide: Test login for all accounts, document status
  - Required: Yes

- [ ] Locked accounts recovered
  - Guide: Regain access or create recovery plan
  - Required: Yes

- [ ] Account health assessed
  - Guide: Follower count, engagement, last activity documented
  - Required: Yes

- [ ] Accounts prioritized
  - Guide: Ranked by potential for relaunch success
  - Required: Yes

- [ ] Ad accounts reconnected
  - Guide: Ad platforms linked, payment methods verified
  - Required: Yes

- [ ] Content strategy created
  - Guide: Content plan for top 3-5 accounts
  - Required: Yes

- [ ] Ad campaigns launched
  - Guide: At least 3 accounts running ads
  - Required: Yes

### Account Inventory Template

| Account Name | Platform | Username | Followers | Last Post | Status | Owner | Access | Priority | Notes |
|--------------|----------|----------|-----------|-----------|--------|-------|--------|----------|-------|
| Example_Co | Instagram | @example_co | 5.2K | 2024-08-15 | Dormant | Sales Team | Yes | High | Good engagement historically |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Tags

sales, social_media, instagram, audit, relaunch, smm, advertising, account_management, template

### Cross-References

**Related Entities:**
- `../../BUSINESSES/Marketing_Campaigns/` - Campaign records
- `../../LIBRARIES/Actions/` - "Audit" action definition
- `../../LIBRARIES/Objects/` - "Social Accounts" object definition
- `../../SETTINGS/Social_Media_Guidelines/` - Organization social media policies

---

**Document Footer:**

**Last Updated:** November 10, 2025
**Maintained By:** Taxonomy Framework Team
**Version:** 1.0
**Source:** Data Extraction from RestructuredData Files
**Extraction Coverage:** 42% (8 of 19 files processed)

**Note:** Additional Task Templates will be added as remaining RestructuredData files (11 files) are processed. Current extraction represents high-priority tasks from November 4-10, 2025 period.
