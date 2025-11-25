# Implementation Guide: Remaining 8 Department Prompts v2.1

**Date:** 2025-11-19
**Purpose:** Guide for completing remaining department prompt updates to v2.1
**Templates Available:** AI (technical), Design (creative), Finance (operational)

---

## Completed Templates (Use These as Reference)

### ✅ PMT-033_AI_Daily_Report.md (Technical/Infrastructure Template)
**Use for:** Dev, Video (with creative adjustments)

**Key Features:**
- Section 6: "Infrastructure and Technical Achievements"
- Focus: System configs, framework enhancements, tool integrations
- Projects: PRT-001, PRT-006, PRT-007, PRT-002
- Tasks: TST-015, TST-055, TST-058, TST-001, TST-018
- Entity Mix: 70% project, 30% operational
- Research: Technical tools, optimization, frameworks
- Improvements: Process automation, technical debt, tool efficiency

### ✅ PMT-035_Design_Daily_Report.md (Creative/Client Template)
**Use for:** Content, SMM

**Key Features:**
- Section 6: "Creative Deliverables and Design Work"
- Focus: Client projects, creative assets, design system
- Projects: DGN-CLIENT-###, PRT-008_VIDEO_Production
- Tasks: TST-012, TST-010, TST-009, TST-007
- Entity Mix: 80%+ project (client deliverables)
- Research: Design trends, creative tools, best practices
- Improvements: Client feedback process, creative workflow, asset management

### ✅ PMT-037_Finance_Daily_Report.md (Operational Template)
**Use for:** Sales, Marketing, LG

**Key Features:**
- Section 6: "Financial Operations and Reporting"
- Focus: Routine operations, accuracy metrics, process efficiency
- Projects: Mostly Operational/Maintenance (80-90%)
- Activities: Month-end closing, processing, reconciliation
- Entity Mix: 90%+ operational
- Research: Automation opportunities, efficiency tools
- Improvements: Process streamlining, accuracy, automation

---

## Remaining 8 Prompts - Implementation Matrix

| Prompt | Template | Section 6 Title | Focus Areas | Entity Mix |
|--------|----------|----------------|-------------|------------|
| **PMT-034** Content | Design | "Content Creation and Publishing" | Blog posts, SEO, editorial calendar, content distribution | 60% project, 40% operational |
| **PMT-036** Dev | AI | "Development and Technical Work" | Feature development, bug fixes, integrations, code reviews | 70% project, 30% operational |
| **PMT-038** HR | Finance + Custom | "Recruitment and HR Operations" | Candidate sourcing, interviews, CV screening, onboarding | 50% project, 50% operational |
| **PMT-039** LG | Finance | "Lead Generation and CRM Operations" | Lead sourcing, qualification, CRM management, pipeline support | 80% operational, 20% project |
| **PMT-040** Marketing | Finance | "Marketing Campaigns and Analytics" | Campaign execution, brand management, market research, analytics | 60% project, 40% operational |
| **PMT-041** Sales | Finance | "Sales Operations and Client Management" | B2B sales, client relationships, deal closure, pipeline management | 70% operational, 30% project |
| **PMT-042** SMM | Design | "Social Media Content and Engagement" | Content creation, engagement, analytics, scheduling | 70% project (campaigns), 30% operational |
| **PMT-043** Video | AI + Design | "Video Production and Creative Work" | Video editing, animation, post-production, asset management | 60% project, 40% operational |

---

## Step-by-Step Implementation (For Each Prompt)

### Step 1: Choose Template
1. Identify department type (technical/creative/operational)
2. Select closest template from 3 completed examples
3. Copy template structure

### Step 2: Update Header
```markdown
# PMT-###: [Department Name] - Daily Report v2.1

**Prompt ID:** PMT-###
**Version:** 2.1
**Department:** [Full Name] ([CODE])
**Category:** Daily Report Generation
**Date:** 2025-11-19
**Status:** Active
```

### Step 3: Update Department Context
```markdown
## Department Context: [Department Name]

### Department Overview
- **Code:** [DEPT CODE]
- **Mission:** [Department mission]
- **Team Size:** [Number] employees
- **Key Responsibilities:**
  - [Responsibility 1]
  - [Responsibility 2]
  - [Responsibility 3]
```

**Update:** Employee list, tools, specific projects/tasks

### Step 4: Update Common Projects Section
```markdown
## [Department]-Specific Projects (TASK_MANAGERS)

### Common Projects
- [List relevant PRT-### projects]
- [Client projects if applicable: DEPT-CLIENT-###]

### Common Tasks
- [List relevant TST-### tasks]

### Activity Patterns
- [Pattern 1] → [Entity mapping guideline]
- [Pattern 2] → [Entity mapping guideline]
```

**Examples:**
- **Dev:** PRT-002_MCP_Automation_Stack, TST-001_AI_Powered_HTML_Parsing, feature dev → project tasks, bug fixes → operational
- **Content:** PRT-### (content projects), TST-### (blog writing, SEO), blog posts → project, admin → operational
- **HR:** PRT-003_HR_Automation, TST-039_CV_Screening, recruitment → mix of project and operational

### Step 5: Customize Section 6 Title and Content

**Section 6 Templates by Type:**

**Technical (Dev, Video):**
```markdown
## 6. [DEVELOPMENT/TECHNICAL] AND [SPECIFIC WORK]

### [Category 1]
- [Item with description and impact]

### [Category 2]
- [Item with description and impact]
```

**Creative (Content, SMM):**
```markdown
## 6. [CONTENT/CREATIVE] DELIVERABLES AND [WORK TYPE]

### Client/Campaign Work
- [Deliverable with details]

### Internal Work
- [Deliverable with details]
```

**Operational (Sales, Marketing, LG, HR):**
```markdown
## 6. [DEPARTMENT] OPERATIONS AND [FOCUS AREA]

### [Operation Category 1]
- [Activity with metrics]

### [Operation Category 2]
- [Activity with metrics]

### Process Improvements
- [Improvement with impact]
```

### Step 6: Update Section 7 (Next Day Plans)
**Customize examples:**
- Technical: Code reviews, feature implementation, testing
- Creative: Client feedback reviews, content creation, campaign planning
- Operational: Pipeline management, processing tasks, reporting

### Step 7: Update Section 8 (Research Needed)
**Customize focus:**
- Technical: New frameworks, tools, integration patterns
- Creative: Design trends, content strategies, engagement tactics
- Operational: Automation tools, process optimization, efficiency gains

### Step 8: Update Section 9 (Improvements Needed)
**Customize improvements:**
- Technical: Code quality, deployment automation, testing coverage
- Creative: Creative workflow, asset management, collaboration tools
- Operational: Process streamlining, data accuracy, reporting automation

### Step 9: Update Examples Throughout
- Update all placeholder text with department-specific examples
- Use realistic project names, tasks, and activities
- Ensure entity mappings align with department patterns

### Step 10: Update Footer and Metadata
```markdown
**Status:** Active
**Maintained By:** AI & Automation Department
**Last Updated:** 2025-11-19
```

---

## Department-Specific Guidance

### PMT-034: Content Department

**Template:** Design (creative work focus)

**Section 6:** "Content Creation and Publishing"
```markdown
## 6. CONTENT CREATION AND PUBLISHING

### Blog Posts and Articles
- [Title]: [Word count], [Topic], [Status]
- SEO optimization: [Keywords, meta descriptions]

### Content Calendar Management
- [Content scheduled for week/month]
- Publication schedule: [Details]

### SEO and Analytics
- Keyword research: [Topics]
- Content performance: [Metrics]
- Traffic analysis: [Insights]

### Editorial Work
- Content editing: [Articles reviewed]
- Style guide updates: [Changes]
- Content distribution: [Channels]
```

**Projects:**
- Content campaigns (by topic/theme)
- SEO improvement initiatives
- Editorial calendar projects

**Tasks:**
- Blog post writing, SEO optimization, content editing, social distribution

**Entity Mix:** 60% project (campaigns, initiatives), 40% operational (routine publishing)

---

### PMT-036: Dev Department

**Template:** AI (technical focus)

**Section 6:** "Development and Technical Work"
```markdown
## 6. DEVELOPMENT AND TECHNICAL WORK

### Feature Development
- [Feature name]: [Description, status, impact]
- Code written: [Lines, files]
- Tests added: [Coverage]

### Bug Fixes and Maintenance
- [Bug ID]: [Description, solution, impact]
- Technical debt addressed: [Details]

### Code Reviews and Collaboration
- PRs reviewed: [Count]
- Code quality improvements: [Details]

### System Integration
- [Integration name]: [API, service, status]
- Performance optimization: [Metrics]

### Testing and QA
- Unit tests: [Count, coverage]
- Integration tests: [Scenarios]
- Bug verification: [Issues]
```

**Projects:**
- PRT-002_MCP_Automation_Stack
- PRT-003_HR_Automation (support)
- Feature development projects

**Tasks:**
- TST-001_AI_Powered_HTML_Parsing
- TST-042_Configure_ATS_Integration
- TST-045_Build_CV_Parser_Workflow

**Entity Mix:** 70% project (features, integrations), 30% operational (bugs, maintenance)

---

### PMT-038: HR Department

**Template:** Finance + Custom (recruitment operations)

**Section 6:** "Recruitment and HR Operations"
```markdown
## 6. RECRUITMENT AND HR OPERATIONS

### Candidate Sourcing
- Candidates sourced: [Count] for [Role]
- Platforms used: [LinkedIn, job boards]
- Sourcing metrics: [Response rate, quality]

### Interview Coordination
- Interviews scheduled: [Count] across [Roles]
- Interviews conducted: [Count] ([First-round/Technical])
- Feedback collected: [Details]

### CV Screening and Processing
- CVs screened: [Count] using [Method/Tool]
- Shortlisted candidates: [Count]
- Screening accuracy: [Percentage if using automation]

### Employee Onboarding
- New hires processed: [Count]
- Onboarding tasks completed: [Checklist items]
- IT equipment coordinated: [Details]

### HR System and Automation
- PRT-003_HR_Automation progress: [Details if applicable]
- CV screening automation testing: [Results]
- Process improvements: [Implemented changes]
```

**Projects:**
- PRT-003_HR_Automation (CV screening, ATS integration)
- Recruitment campaigns (by role/department)

**Tasks:**
- TST-039_Setup_n8n_CV_Screening
- TST-048_Create_Scoring_Algorithm
- TST-053_CV_Parser_Development

**Entity Mix:** 50% project (automation, major campaigns), 50% operational (daily recruitment)

---

### PMT-039: LG (Lead Generation) Department

**Template:** Finance (operational focus)

**Section 6:** "Lead Generation and CRM Operations"
```markdown
## 6. LEAD GENERATION AND CRM OPERATIONS

### Lead Sourcing and Scraping
- Leads sourced: [Count] from [Platforms]
- Data quality: [Validation rate]
- Lead categories: [Breakdown by type]

### Lead Qualification
- Leads qualified: [Count]
- Qualification criteria: [Applied filters]
- Conversion rate: [Percentage]

### CRM Management
- CRM entries created: [Count]
- Data enrichment: [Fields updated]
- Duplicate removal: [Count cleaned]

### Outbound/Inbound Prospecting
- Outreach campaigns: [Count, channels]
- Responses received: [Count, rate]
- Meetings scheduled: [Count]

### Sales Pipeline Support
- Leads handed to Sales: [Count]
- Pipeline stage updates: [Details]
- Follow-up tasks: [Scheduled]
```

**Projects:**
- Lead generation campaigns (by industry/role)
- CRM improvement initiatives

**Tasks:**
- Mostly operational (daily lead gen activities)
- Occasional project tasks for campaigns or system improvements

**Entity Mix:** 80% operational, 20% project (campaigns, CRM improvements)

---

### PMT-040: Marketing Department

**Template:** Finance (operational with campaigns)

**Section 6:** "Marketing Campaigns and Analytics"
```markdown
## 6. MARKETING CAMPAIGNS AND ANALYTICS

### Campaign Execution
- Active campaigns: [Names, status]
- Campaign performance: [Metrics]
- A/B testing: [Results]

### Brand Management
- Brand assets created: [Count, types]
- Brand guidelines updated: [Changes]
- Brand consistency reviews: [Findings]

### Market Research
- Research conducted: [Topics]
- Competitor analysis: [Insights]
- Market trends: [Findings]

### Marketing Analytics
- Campaign ROI: [Metrics]
- Channel performance: [Breakdown]
- Conversion tracking: [Funnel analysis]

### Content Coordination
- Marketing materials: [Created/updated]
- Cross-department collaboration: [With Content, Design, SMM]
```

**Projects:**
- Marketing campaigns (by product/service)
- Brand refresh initiatives

**Tasks:**
- Campaign-specific tasks
- Analytics and reporting tasks

**Entity Mix:** 60% project (campaigns), 40% operational (ongoing marketing)

---

### PMT-041: Sales Department

**Template:** Finance (operational focus)

**Section 6:** "Sales Operations and Client Management"
```markdown
## 6. SALES OPERATIONS AND CLIENT MANAGEMENT

### B2B Sales Activities
- Sales calls: [Count, outcomes]
- Demos scheduled: [Count]
- Proposals sent: [Count, value]

### Client Relationship Management
- Client meetings: [Count, topics]
- Relationship building: [Activities]
- Client satisfaction: [Feedback]

### Deal Closure
- Deals closed: [Count, value]
- Contracts signed: [Count]
- Revenue generated: [Amount]

### Sales Pipeline Management
- Pipeline value: [Total]
- Stage progression: [Movements]
- Forecast updates: [Projections]

### CRM and Reporting
- CRM updates: [Activities logged]
- Sales reports: [Generated for management]
- Performance metrics: [Against targets]
```

**Projects:**
- Major deal pursuits (enterprise clients)
- Sales process improvements

**Tasks:**
- Mostly operational (daily sales activities)
- Occasional project tasks for major deals

**Entity Mix:** 70% operational, 30% project (major deals, process improvements)

---

### PMT-042: SMM (Social Media) Department

**Template:** Design (creative content focus)

**Section 6:** "Social Media Content and Engagement"
```markdown
## 6. SOCIAL MEDIA CONTENT AND ENGAGEMENT

### Content Creation
- Posts created: [Count by platform]
- Graphics designed: [Count, types]
- Video content: [Count, duration]
- Content themes: [Topics covered]

### Engagement Management
- Comments responded to: [Count]
- Messages handled: [Count]
- Community interaction: [Activities]

### Social Media Analytics
- Follower growth: [Change, platform breakdown]
- Engagement rate: [Metrics]
- Top performing posts: [Highlights]
- Campaign performance: [Results]

### Content Scheduling
- Posts scheduled: [Count for next week]
- Content calendar: [Updated for month]
- Platform optimization: [Timing, format]

### Campaign Support
- Campaign posts: [Created for active campaigns]
- Influencer coordination: [Activities]
- Paid social: [Ad performance]
```

**Projects:**
- Social media campaigns (by theme/product)
- Content series projects

**Tasks:**
- Content creation tasks
- Engagement management tasks

**Entity Mix:** 70% project (campaigns, content series), 30% operational (daily engagement)

---

### PMT-043: Video Department

**Template:** AI + Design (technical + creative mix)

**Section 6:** "Video Production and Creative Work"
```markdown
## 6. VIDEO PRODUCTION AND CREATIVE WORK

### Video Editing and Production
- Videos edited: [Count, duration]
- Projects completed: [Titles]
- Editing techniques: [Applied effects, transitions]

### Animation and Motion Design
- Animations created: [Count, type]
- Motion graphics: [Count, purpose]
- Visual effects: [Applied to projects]

### Video Post-Production
- Color grading: [Videos processed]
- Audio mixing: [Tracks balanced]
- Final exports: [Formats, quality]

### Video Asset Management
- Raw footage organized: [GB, hours]
- Project files archived: [Count]
- Asset library updated: [New additions]

### Creative Collaboration
- Thumbnails requested from Design: [Status]
- Script collaboration with Content: [Projects]
- Brand compliance: [Checks performed]
```

**Projects:**
- PRT-008_VIDEO_Production
- Video series projects (by topic/client)

**Tasks:**
- TST-### (video editing, animation)
- TST-007_Create_Video_Thumbnails (coordination with Design)

**Entity Mix:** 60% project (video series, client work), 40% operational (routine editing)

---

## Quality Checklist (For Each Prompt)

Before finalizing, verify:

### Content
- [ ] All 10 sections present
- [ ] Department context accurate (employees, tools, projects)
- [ ] Section 6 customized for department type
- [ ] Entity mappings realistic for department
- [ ] Next day plans relevant to department work
- [ ] Research topics align with department needs
- [ ] Improvements address department pain points

### Entity Integration
- [ ] Common projects listed (PRT-###)
- [ ] Common tasks listed (TST-###)
- [ ] Activity patterns documented
- [ ] Entity mix percentage realistic
- [ ] Token-efficient format used: `TST-###_Name`
- [ ] No department letters in entity names

### Formatting
- [ ] Header complete with prompt ID, version, date
- [ ] Markdown formatting consistent
- [ ] Code blocks for examples
- [ ] Tables for metrics
- [ ] Bullet lists for achievements

### Examples
- [ ] All placeholder text replaced
- [ ] Realistic project names
- [ ] Department-appropriate tasks
- [ ] Accurate time estimates
- [ ] Relevant tools and metrics

---

## Archive Old Version (After Completion)

```bash
# For each prompt, after creating v2.1:
move "PMT-###_[Dept]_Daily_Report.md" "_ARCHIVE/PMT-###_[Dept]_Daily_Report_v1.0.md"
move "PMT-###_[Dept]_Daily_Report_v2.1.md" "PMT-###_[Dept]_Daily_Report.md"
```

---

## Time Estimates

**Per Prompt:**
- Copy template: 2 min
- Update header/context: 5 min
- Customize projects/tasks: 5 min
- Update Section 6: 5 min
- Update Sections 7-9: 5 min
- Review and validate: 3 min
- **Total:** ~25 min per prompt

**8 Remaining Prompts:** 25 min × 8 = **3.3 hours**

---

## Testing Recommendation

After completing all prompts:

1. **Generate test report** for one department using PMT-032 v2.1
2. **Verify entity mapping** works correctly with PMT-070 v2.1
3. **Check all 10 sections** populate correctly
4. **Validate format** matches REPORT_OUTPUT_SCHEMA_v2.1.md
5. **Review output** for quality and completeness

---

**Implementation Guide Created:** 2025-11-19
**For:** Remaining 8 department prompts (PMT-034, 036, 038, 039, 040, 041, 042, 043)
**Status:** Ready for implementation

---

*End of Guide*
