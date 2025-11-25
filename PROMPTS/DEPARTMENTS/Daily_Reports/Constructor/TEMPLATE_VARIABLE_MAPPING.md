# Enhanced Template - Variable Mapping Guide

## Overview
This document provides the complete mapping of variables used in `TEMPLATE_Enhanced_Department_Prompt.md` and how to populate them from the guidance documentation.

---

## Variable Reference Table

| Variable | Source | Description | Example (Design Dept) |
|----------|--------|-------------|----------------------|
| `{DEPARTMENT_NAME}` | Config | Full department name | Design |
| `{DEPARTMENT_MISSION}` | docs/06 | Department mission statement | UI/UX design, graphic design, branding, creative production |
| `{TEAM_SIZE}` | docs/01 | Number of employees | 9 |
| `{TEAM_PERCENTAGE}` | Calculated | Percentage of company | 28.1 |
| `{DEPT_CODE}` | Config | Short department code | DSN or DESIGN |
| `{KEY_RESPONSIBILITIES_LIST}` | docs/06 | Markdown list of responsibilities | See below |
| `{FOCUS_AREAS_COUNT}` | docs/06 | Number of focus areas | 4 |
| `{FOCUS_AREAS_LIST}` | docs/06 | Detailed focus areas with descriptions | See below |
| `{DEPARTMENT_FOLDER}` | Config | Folder name | Design Nov25 |
| `{DAY}` | Runtime | Day of month (2 digits) | 07, 25 |
| `{EMPLOYEE_LIST_WITH_FULL_DETAILS}` | docs/01 | Complete employee list formatted | See below |
| `{PROJECT_LIST_WITH_RESOURCES}` | docs/02 | Projects with resources | See below |
| `{PROJECT_ABBREVIATIONS}` | docs/02 | Quick reference table | See below |
| `{AI_TOOLS_LIST}` | docs/06 + Context | AI tools for department | See below |
| `{TRADITIONAL_TOOLS_LIST}` | docs/06 | Traditional tools | Figma, Adobe Suite, etc. |
| `{COMMUNICATION_TOOLS_LIST}` | Standard | Communication tools | Slack, Discord, Telegram, etc. |
| `{VOCABULARY_CATEGORIES_WITH_TERMS}` | docs/03 | Department vocabulary | See below |
| `{COMMON_OBJECTS_LIST}` | docs/03 + docs/04 | Common objects | banners, headers, icons, etc. |
| `{STANDARD_ACTIONS_WITH_FORMS}` | docs/03 | Actions with 3 forms | create/creating/created |
| `{SECTION_EMPHASIS_DETAILS}` | docs/05 + docs/06 | Which 21-sections to emphasize | Section 18, 8, 3 |
| `{DEPT_SPECIFIC_SECTION}` | docs/06 | Department-specific section number | 18 |
| `{EXTRACTION_FOCUS_POINTS}` | docs/06 | What to focus on extracting | Design reviews, Figma work, etc. |
| `{DEPARTMENT_ACTIVITIES}` | docs/06 | Department activity description | design production activities |
| `{TOOL_CATEGORY}` | docs/06 | Tool category description | AI design |
| `{DELIVERABLE_TYPE}` | docs/06 | Deliverable type description | creative |
| `{ACTIVITY_CATEGORIES_LIST}` | docs/06 | Activity categories | UI/UX Design, Graphic Design, etc. |
| `{KEY_METRICS_WITH_FORMULAS}` | docs/06 | Metrics table | Projects completed, etc. |
| `{KEY_METRICS_DETAILED_DESCRIPTIONS}` | docs/06 | Detailed metric descriptions | See below |
| `{METRIC_FORMULAS}` | docs/06 | Calculation formulas | See below |
| `{PERFORMANCE_TARGETS_TABLE}` | docs/06 | Target values table | See below |
| `{COLLABORATION_PATTERNS}` | docs/06 | Who dept collaborates with | Dev, Video, AI |
| `{COLLABORATION_DETAILS}` | docs/06 | Collaboration details | Design handoff, etc. |
| `{FOCUS_AREAS_BULLET_LIST}` | docs/06 | Simple bullet list | - UI/UX Design |
| `{DATE_TIME}` | Runtime | Current date and time | November 7, 2025 14:30 |

---

## Department Configurations

### Design Department Full Configuration

```markdown
**DEPARTMENT_NAME**: Design
**DEPARTMENT_MISSION**: UI/UX design, graphic design, 3D design, branding, and creative production for internal and client projects
**TEAM_SIZE**: 9
**TEAM_PERCENTAGE**: 28.1
**DEPT_CODE**: DESIGN
**DEPARTMENT_FOLDER**: Design Nov25

**KEY_RESPONSIBILITIES_LIST**:
- UI/UX design for web and mobile applications
- Graphic design and brand identity development
- Illustration and custom artwork creation
- Design system development and maintenance
- Client project design execution
- Figma component library management
- Collaboration with development teams on implementation
- AI design tool integration and experimentation

**FOCUS_AREAS_COUNT**: 4

**FOCUS_AREAS_LIST**:
1. **UI/UX Design**
   - User interface design for web and mobile applications
   - Wireframing and prototyping
   - User flow and journey mapping
   - Usability testing and iteration
   - Responsive design implementation

2. **Graphic Design & Branding**
   - Logo design and brand identity systems
   - AI materials (banners, headers, social media graphics)
   - Illustrations and custom iconography
   - Brand books and style guide creation
   - Print and digital asset production

3. **Project Execution**
   - Client project management and delivery
   - Design reviews and stakeholder presentations
   - Asset organization in Google Drive and Figma
   - Collaboration with Dev team on design handoff
   - DGN (Design Studio) platform projects

4. **AI Design Tools**
   - Midjourney for AI image generation
   - Leonardo.ai for creative assets
   - Gamma AI for presentation design
   - Figma AI plugins integration
   - Process optimization through AI automation
```

### All 7 Departments Quick Reference

#### HR Department
- **Team Size**: 2 (6.25%)
- **Mission**: Recruitment, onboarding, employee management, HR operations
- **Focus Areas**: Recruitment Activities, Onboarding & Training, Employee Management, Documentation & Systems
- **Section Emphasis**: 20, 16, 3
- **Key Objects**: candidates, interviews, contracts, employees, onboarding

#### AI Department
- **Team Size**: 3 (9.4%)
- **Mission**: Prompt engineering, AI integration, automation, RAC management, project coordination
- **Focus Areas**: Prompt Engineering, AI Integration & Automation, RAC Management, Project Management
- **Section Emphasis**: 8, 9, 11, 3
- **Key Objects**: prompts, templates, agents, workflows, automation, documentation

#### Video Department
- **Team Size**: 3 (9.4%)
- **Mission**: Video editing, motion graphics, AI video tools, creative content production
- **Focus Areas**: Video Production, Content Creation, AI Video Tools, Project Collaboration
- **Section Emphasis**: 18, 8, 3
- **Key Objects**: audios, footage, effects, graphics, videos, animations, voiceover

#### Sales Department
- **Team Size**: 1 (3.1%)
- **Mission**: Client management, pipeline management, proposals, SMM support
- **Focus Areas**: Client Management, Pipeline Management, Communication & Outreach, SMM & AI Support
- **Section Emphasis**: 17, 3
- **Key Objects**: calls, leads, clients, communications, proposals, reports

#### Design Department
- **Team Size**: 9 (28.1%)
- **Mission**: UI/UX design, graphic design, branding, creative production
- **Focus Areas**: UI/UX Design, Graphic Design & Branding, Project Execution, AI Design Tools
- **Section Emphasis**: 18, 8, 3
- **Key Objects**: logos, illustrations, mockups, wireframes, components, brandbooks

#### Dev Department
- **Team Size**: 3 (9.4%)
- **Mission**: Frontend/backend development, system architecture, microservices, DevOps
- **Focus Areas**: Frontend Development, Backend Development, System Development, DevOps & Deployment
- **Section Emphasis**: 19, 9, 3
- **Key Objects**: apis, databases, microservices, components, endpoints, deployments

#### LG Department
- **Team Size**: 11 (34.4%)
- **Mission**: Lead generation, prospecting, qualification, outreach, analytics
- **Focus Areas**: Prospecting & Sourcing, Lead Qualification, Outreach & Engagement, Performance & Analytics
- **Section Emphasis**: 16, 17, 3
- **Key Objects**: leads, accounts, messages, emails, connections, companies, databases

---

## Employee List Format

### Design Department Employees (from docs/01)

```markdown
**Shelep Olha** (ID: 86641) - UI/UX designer | Ukraine | @olyashelep | shelep.olya@gmail.com | Status: Project

**Bogun Polina** (ID: 87537) - UI/UX designer | Austria | @polinabogun | pollybogun@gmail.com | Status: Part Project + Part Time

**Kucherenko Iuliia** (ID: 228) - Graphic Designer, Web Designer | Ukraine | viligosh17@gmail.com | Status: Full Project + Part Time | Rate: 1.5

**Chobotar Yuliia** (ID: 87826) - UI/UX designer, Graphic Designer | Ukraine | @Lulu_ly | chobotar.ly@gmail.com | Status: Available

**Vereteno Marta** (ID: 626) - Graphic designer | Moldova | sd.designsmart@gmail.com | Status: Part Project + Part Project

**Safonova Elleonora** (ID: 87995) - UI/UX designer | Germany/Ukraine | @eleonora_lee | ellesafonova@gmail.com | Status: Available

**Skrypkar Vilhelm** (ID: 333) - Illustrator, Graphic Designer | Ukraine | @bull_will | ntwilson666@gmail.com | Status: Available

**Hlushko Mariia** (ID: 88626) - Illustrator, Graphic Designer, Project manager | Ukraine | @white_book_wizard | mariiahlushko9@gmail.com | Status: Project

**Shymkevych Iryna** (ID: 88357) - UI/UX designer | Ukraine | @lamperry | shymkevychiryna@gmail.com | Status: Available
```

---

## Project List Format

### Design Department Projects (from docs/02)

```markdown
**DGN (Design Studio)** - Design services platform
- **Keywords**: Design Studio, DGN, design services
- **Resources**: Logo, Old Files, Google Drive, Figma
- **Abbreviation**: DGN

**MDL EU** - European market version
- **Keywords**: MDL, European market, EU version
- **Resources**: Figma designs (old and new versions)
- **Abbreviation**: MDL

**MDL UA** - Ukrainian market version
- **Keywords**: MDL, Ukrainian market, UA version
- **Resources**: Google Drive folder, Figma designs
- **Abbreviation**: MDL

**RH / Remote Helpers** - Main company platform
- **Keywords**: Remote Helpers, RH, Rhelpers
- **Resources**: Google Drive, Figma work files, approved SMM posts
- **Abbreviation**: RH

**Portfolio of Projects** - Company portfolio showcase
- **Keywords**: portfolio, projects showcase, Портфоліо проектів
- **Resources**: Figma
- **Abbreviation**: Portfolio

**Service Platform Branding** - All service platforms (trn-s, smm-s, d-vs, fv-e, fv-a, of-w, etc.)
- **Keywords**: Translation, SMM, Development, Video, Assistant, Offline services
- **Resources**: Logos, SMM content, Figma designs
```

---

## Section Emphasis Details

### Design Department (from docs/06)

**Primary Sections**: 18, 8, 3

```markdown
#### Section 18: DESIGN & CREATIVE CONTEXT
**Focus**: Design-specific activities and deliverables
- Design project updates and progress
- Figma file organization and components
- Client feedback and design iterations
- UI/UX research and testing results
- Design system updates
- Brand guideline development
- Asset creation and management
- Cross-team design collaboration

**Extract**: All design deliverables, Figma links, client feedback, design decisions, iteration cycles, tool usage, creative process notes

#### Section 8: TOOLS & RESOURCES
**Focus**: AI design tools and integrations
- Midjourney AI image generation usage
- Leonardo.ai creative asset production
- Gamma AI presentation creation
- Figma AI plugin integration
- New tool evaluations and experiments
- Tool workflow optimizations
- License and subscription needs
- Training and onboarding for new tools

**Extract**: All AI tool usage, time savings, quality improvements, new capabilities, integration opportunities

#### Section 3: ACTION ITEMS & TASKS
**Focus**: Design tasks with complete metadata
- All design tasks using ACTION + OBJECT + CONTEXT format
- Owner matched to Employee Directory (with ID and department)
- Priority, status, complexity assignments
- RACI matrix for accountability
- Related projects matched to Project Directory
- Dependencies and blockers identified
- Success criteria defined

**Extract**: All actionable items with full task framework compliance
```

---

## Metrics & KPIs

### Design Department Metrics (from docs/06)

```markdown
**KEY_METRICS_WITH_FORMULAS**:

| Metric | Formula | Target | Purpose |
|--------|---------|--------|---------|
| Projects Completed | Count of completed design projects | 5-7/week | Productivity |
| Revision Rounds | Avg iterations per project | ≤3 | Efficiency |
| Client Satisfaction | Survey score (1-5) | ≥4.5 | Quality |
| Figma Component Library Growth | New components added | +10/month | System Development |
| Design-to-Dev Handoff Quality | Issues found in dev / total designs | <5% | Collaboration |
| AI Tool Time Savings | Hours saved vs traditional methods | 30% | Innovation |
| Design System Usage | Components reused / total designs | >70% | Consistency |

**METRIC_FORMULAS**:
- **Efficiency Rate** = Completed Projects / Total Hours Worked
- **Quality Score** = (Client Satisfaction × 40%) + (Revision Rate × 30%) + (Handoff Quality × 30%)
- **AI Adoption Rate** = Design Tasks Using AI / Total Design Tasks × 100%
- **Component Reusability** = Reused Components / Total Components Used × 100%

**PERFORMANCE_TARGETS_TABLE**:

| KPI | Minimum | Target | Excellent |
|-----|---------|--------|-----------|
| Projects/Week | 3 | 5-7 | 10+ |
| Client Satisfaction | 4.0 | 4.5 | 5.0 |
| Revision Rounds | ≤4 | ≤3 | ≤2 |
| AI Time Savings | 15% | 30% | 50% |
| Handoff Issues | <10% | <5% | <2% |
```

---

## Vocabulary & Terminology

### Design Department (from docs/03)

```markdown
**VOCABULARY_CATEGORIES_WITH_TERMS**:

**Figma-Specific Terms:**
- **Frames**: Container elements in Figma
- **Components**: Reusable design elements
- **Variants**: Component variations
- **Auto Layout**: Responsive component behavior
- **Text Blocks**: Text styling elements
- **UI Kits**: Pre-built design component sets
- **Prototyping**: Interactive design mockups

**UI/UX Terms:**
- **Wireframe**: Low-fidelity layout sketch
- **Prototype**: Interactive design mockup
- **User Journey Map**: Visualization of user experience over time
- **User Flow**: Path users take through interface
- **Empathy Map**: Tool for understanding user perspectives
- **Information Architecture**: Structure of information in interface

**Design Process Terms:**
- **Design Review**: Stakeholder feedback session
- **Iteration**: Design refinement cycle
- **Design Handoff**: Transfer from design to development
- **Component Library**: Reusable design system
- **Brand Guidelines**: Brand identity standards
- **Asset Management**: Organization of design files

**COMMON_OBJECTS_LIST**:
banners, headers, icons, illustrations, infographics, logos, presentations, brandbooks, fonts, business cards, thumbnails, mockups, email templates, characters, portraits, wireframes, prototypes, user flows, components, layouts

**STANDARD_ACTIONS_WITH_FORMS**:
- **create** / creating / created
- **design** / designing / designed
- **update** / updating / updated
- **review** / reviewing / reviewed
- **iterate** / iterating / iterated
- **prototype** / prototyping / prototyped
- **export** / exporting / exported
- **organize** / organizing / organized
```

---

## Collaboration Patterns

### Design Department (from docs/06)

```markdown
**COLLABORATION_PATTERNS**:
- **Design + Dev**: Design handoff, component implementation, design QA
- **Design + AI**: Brand materials, campaign assets, social media graphics
- **Design + Video**: Motion graphics coordination, video thumbnails, visual consistency
- **Design + Sales**: Client presentations, proposal designs, demo materials
- **Design + All Departments**: Service platform branding, internal tool UI/UX

**COLLABORATION_DETAILS**:
**Design → Dev Handoff Process:**
1. Design completion in Figma
2. Component specifications documented
3. Assets exported and organized
4. Handoff meeting scheduled
5. Dev questions addressed
6. Implementation QA by designer
7. Final approval and sign-off

**Design → AI Support:**
- Brand consistency across all channels
- Template creation for marketing campaigns
- Social media graphic production
- Event and presentation materials
- Brand guideline maintenance

**Cross-Platform Consistency:**
- Design system ensures consistency across all service platforms (DGN, trn-s, smm-s, d-vs, fv-e, fv-a, of-w)
- Component library shared across projects
- Brand guidelines applied universally
```

---

## Usage Instructions

### To Generate Enhanced Prompt for Any Department:

1. **Load Template**: Open `TEMPLATE_Enhanced_Department_Prompt.md`

2. **Select Department**: Choose from HR, AI, Video, Sales, Design, Dev, or LG

3. **Populate Variables**: Replace all `{VARIABLE}` placeholders using this mapping guide

4. **Employee List**: Copy relevant employees from docs/01

5. **Project List**: Copy relevant projects from docs/02

6. **Vocabulary**: Copy department-specific terms from docs/03

7. **Metrics**: Copy department KPIs from docs/06

8. **Section Emphasis**: Use department configuration from docs/06

9. **Validate**: Check all variables replaced, formatting consistent

10. **Save**: Save as `PROMPT_{DEPARTMENT}_Daily_Report_Enhanced.md`

### Automated Variable Replacement (Future Enhancement)

For automated generation, create a script that:
1. Reads department configuration from docs/06
2. Fetches employees from docs/01 filtered by department
3. Fetches projects from docs/02 filtered by department
4. Builds vocabulary from docs/03 filtered by department
5. Constructs metrics from docs/06 for department
6. Replaces all template variables
7. Validates completeness
8. Outputs enhanced prompt file

---

*Last Updated: November 7, 2025*
*Template Version: 2.0*
