# Template 06: Rules & Best Practices

**Purpose:** Document quality standards, rules, and best practices discussed
**Library Integration:** ⭐⭐⭐ Heavy (Parameters - 10,596+)
**Priority:** Include when standards, quality, or best practices discussed

---

## Template

```markdown
## Rules & Best Practices

**Standards Discussed:** [Number]
**Parameters Referenced:** [Number from Parameters library]
**Departments Affected:** [Which teams]

### Quality Standards

#### [Standard Category] - [Department]
- **Parameter:** [PARAM-XXX] - [Parameter name from Parameters library]
- **Standard:** [What the standard is]
- **Current Value/Target:** [Specific threshold or goal]
- **Context:** [Why this standard was discussed]
- **Application:** [When/how to apply this standard]
- **Enforcement:** [How to ensure compliance]
- **Examples:**
  - ✅ Good: [Example of meeting standard]
  - ❌ Bad: [Example of violating standard]

### Process Standards

#### [Process Name] - [Department]
- **Process ID:** [PROC-XXX from Processes library]
- **Standard:** [What must be followed]
- **Rationale:** [Why this standard exists]
- **Exceptions:** [When standard doesn't apply]
- **Related Parameters:** [PARAM-XXX, PARAM-YYY]

### Data Standards

#### [Data Type] - [Department]
- **Parameter:** [PARAM-XXX] - [Data quality threshold]
- **Standard:** [Required quality level]
- **Measurement:** [How to measure]
- **Consequences:** [What happens if not met]

### Communication Standards

[Standards for team communication, documentation, reporting]

### New Best Practices Established

[New standards or practices agreed upon in meeting]

### Standards Violations/Issues

[Cases where standards were not met; discussion of why]

### Standards Updates

[Changes to existing standards; what changed and why]
```

---

## Recognition Rules

### Identifying Standards Discussions

**Direct Standard Mentions:**
- "Our standard is..."
- "Design quality must be 8/10 minimum"
- "Data accuracy should be >90%"
- "We require test coverage >80%"

**Quality Thresholds:**
- Numeric targets: "95% deliverability," "4 revisions maximum"
- Time limits: "24-hour code review SLA," "respond within 2 hours"
- Performance metrics: "Load time <3 seconds," "conversion rate >5%"

**Process Requirements:**
- "Always do X before Y"
- "Never skip testing"
- "Must use design system components"
- "All PRs require 2 reviewers"

**Best Practice Sharing:**
- "The best way to do X is..."
- "We found that Y works better than Z"
- "Good practice: start with mobile wireframes"

### Matching to Parameters Library

**Total Parameters:** 10,596+ across all departments

**Parameter Organization:**
```
By Department:
- Developers: 124 parameters
- Designers: 48 parameters
- Lead Generators: 78 parameters
- Sales: 52 parameters
- HR: 87 parameters
- Video: 64 parameters
- AI: 95 parameters
```

**Common Parameter Categories:**
1. **Quality Thresholds** (e.g., design_quality_min: 8/10)
2. **Time Limits** (e.g., code_review_sla_hours: 24)
3. **Performance Metrics** (e.g., email_deliverability_min: 95%)
4. **Process Requirements** (e.g., test_coverage_required: 80%)
5. **Data Standards** (e.g., lead_accuracy_target: 92%)

**Reference:** `01_Library_Integration/08_Parameters_Lightweight.md` for overview

---

## Examples

### Example 1: Design Team - Quality Standards

```markdown
## Rules & Best Practices

**Standards Discussed:** 5
**Parameters Referenced:** 8 (from Design parameters)
**Departments Affected:** Design

### Quality Standards

#### Design Deliverable Quality - Design Department
- **Parameter:** PARAM-DES-001 - `design_quality_min`
- **Standard:** All client-facing designs must meet 8/10 quality threshold
- **Current Value/Target:** 8/10 minimum (scale 1-10)
- **Context:** Client feedback indicated some recent work felt rushed; team agreed to enforce quality gate
- **Application:** Before submitting to client, self-assess design against quality checklist (alignment, typography, spacing, brand consistency, polish)
- **Enforcement:** Peer review before client delivery; if below 8/10, requires revision
- **Examples:**
  - ✅ Good: Landing page with perfect alignment, custom graphics, polished interactions, brand-consistent colors → 9/10
  - ❌ Bad: Social graphics with misaligned text, generic stock photos, inconsistent fonts → 6/10 (requires revision)

#### Client Revision Limit - Design Department
- **Parameter:** PARAM-DES-012 - `client_revisions_max`
- **Standard:** Maximum 3 revision rounds per project phase
- **Current Value/Target:** 3 revisions (industry standard)
- **Context:** Recent project had 7 revision rounds (scope creep); need to set boundary
- **Application:** Communicate to client at project start; after 3 rounds, additional revisions are billed separately
- **Enforcement:** Project manager (or designer if direct client) enforces; documented in contract
- **Examples:**
  - ✅ Good: Round 1 (initial), Round 2 (minor changes), Round 3 (final polish) → Approved
  - ❌ Bad: Round 1, 2, 3, 4, 5, 6, 7 (client keeps changing mind) → Should have stopped at Round 3

#### Design System Usage - Design Department
- **Parameter:** PARAM-DES-025 - `design_system_compliance`
- **Standard:** 100% of new projects must use design system components (no custom components without approval)
- **Current Value/Target:** 100% compliance
- **Context:** Inconsistencies across projects due to designers creating one-off components instead of using library
- **Application:** Start every project by reviewing design system; if needed component doesn't exist, request addition to system
- **Enforcement:** Design lead (Anastasiia) reviews projects during in-progress check-ins
- **Examples:**
  - ✅ Good: Use design system buttons, forms, cards → Consistent across all projects
  - ❌ Bad: Create custom button style for one project → Breaks consistency, creates maintenance burden

### Process Standards

#### Mobile-First Design Approach - Design Department
- **Process ID:** PROC-DESIGN-001 (UI/UX Design Process)
- **Standard:** All responsive web projects must start with mobile wireframes (375px), then scale up to tablet/desktop
- **Rationale:** Mobile usage >60% for most clients; mobile-first ensures better mobile UX (instead of desktop designs poorly adapted to mobile)
- **Exceptions:** Desktop-only applications (e.g., internal admin dashboards)
- **Related Parameters:**
  - PARAM-DES-018 - `mobile_breakpoint_min`: 375px
  - PARAM-DES-019 - `tablet_breakpoint`: 768px
  - PARAM-DES-020 - `desktop_breakpoint`: 1440px
- **Context Discussed:** Team noticed mobile experiences were often afterthoughts; new standard to fix this
- **Examples:**
  - ✅ Good: Wireframe mobile (375px) → Tablet (768px) → Desktop (1440px)
  - ❌ Bad: Design desktop first, then "squeeze" into mobile → Poor mobile UX

#### Design Feedback Turnaround - Design Department
- **Process ID:** PROC-DESIGN-001 (UI/UX Design Process)
- **Standard:** Client feedback requests must have 24-48 hour expected response time (set expectation upfront)
- **Rationale:** Current average is 2-3 days; slows down iteration cycles
- **Exceptions:** Complex projects where client needs internal stakeholder alignment (allow up to 5 business days)
- **Related Parameters:**
  - PARAM-DES-033 - `client_feedback_sla_hours`: 48
  - PARAM-DES-034 - `internal_feedback_sla_hours`: 24
- **Context Discussed:** Projects stall waiting for feedback; need to set expectations
- **Enforcement:** Communicate timeline at project kickoff; send reminder if feedback overdue
- **Examples:**
  - ✅ Good: "Please review by Friday EOD (48 hours)" → Client responds Thursday
  - ❌ Bad: "Let me know when you can review" → Client takes 10 days

### Data Standards

#### Figma File Organization - Design Department
- **Parameter:** PARAM-DES-040 - `figma_file_naming_standard`
- **Standard:** All Figma files must follow naming convention: `[Client Name] - [Project Type] - [Date YYYY-MM]`
- **Measurement:** Audit Figma workspace monthly; non-compliant files flagged
- **Consequences:** Hard to find files, duplicate work, unprofessional client experience
- **Context Discussed:** Current workspace is disorganized; designers use inconsistent naming
- **Examples:**
  - ✅ Good: "Acme Corp - Landing Page - 2025-11"
  - ❌ Bad: "new design final v3 FINAL2"

#### Design Asset Delivery Format - Design Department
- **Parameter:** PARAM-DES-045 - `asset_delivery_formats`
- **Standard:** All client deliverables include: (1) Figma link (view-only), (2) PDF export, (3) PNG/JPG assets (if web), (4) Source files (.fig) at project completion
- **Measurement:** Checklist before delivery
- **Consequences:** Client can't access work or use assets properly
- **Context Discussed:** Recent client couldn't open Figma; had no alternative format
- **Examples:**
  - ✅ Good: Send all 4 formats in organized Google Drive folder
  - ❌ Bad: Send only Figma link (client has no Figma account)

### Communication Standards

**Design Critique Sessions:**
- **Standard:** All designs presented to team before client delivery
- **Format:** 15-minute critique per project (quick feedback, not deep dive)
- **Frequency:** Weekly design sync (Fridays)
- **Purpose:** Catch quality issues, share knowledge, maintain consistency

**Client Presentation Format:**
- **Standard:** All client presentations include: (1) Context/problem, (2) Design solution, (3) Rationale, (4) Next steps
- **Purpose:** Educate client on design decisions (not just show pretty pictures)
- **Related Parameter:** PARAM-DES-050 - `presentation_structure_required`: true

### New Best Practices Established

**Dribbble Portfolio Strategy:**
- **Practice:** Post 2 shots per week (Tuesdays and Thursdays, 2-3 PM optimal engagement)
- **Quality Bar:** Only post work rated 9/10 or higher
- **Content:** Real client work (with permission) or personal projects
- **Purpose:** Maintain agency presence, attract design talent, showcase capabilities
- **Owner:** Rotating weekly (schedule created)

**Design System Update Workflow:**
- **Practice:** Weekly 15-minute sync to review design system updates
- **Notification:** Slack channel post when components updated
- **Version Control:** Major changes get version number (e.g., Design System v2.1)
- **Documentation:** Update component descriptions in Figma
- **Purpose:** Keep team aligned on design system changes

### Standards Violations/Issues

**Issue: Skipping Design System Review**
- **Violation:** Two recent projects used custom components instead of design system
- **Impact:** Inconsistent UI across projects; extra maintenance work
- **Discussion:** Team acknowledged this is inefficient
- **Resolution:** Reaffirmed 100% design system compliance standard (PARAM-DES-025)
- **Prevention:** Anastasiia will review projects at wireframe stage

**Issue: Client Feedback Delays**
- **Violation:** Recent project stalled for 8 days waiting for client feedback (target: 48 hours)
- **Impact:** Project timeline delayed, designer blocked
- **Discussion:** Need to set expectations upfront and send reminders
- **Resolution:** Implement feedback SLA communication at project kickoff

### Standards Updates

**Updated: Design Quality Minimum**
- **Previous:** No formal threshold (subjective)
- **New:** 8/10 minimum for client deliverables (PARAM-DES-001)
- **Reason:** Recent quality inconsistencies; need objective standard
- **Effective:** Immediately (applies to all active projects)

**Updated: Mobile-First Requirement**
- **Previous:** Desktop-first approach (designer preference)
- **New:** Mobile-first mandatory for all responsive projects (PROC-DESIGN-001)
- **Reason:** Mobile usage >60%; better UX when designed mobile-first
- **Effective:** All new projects starting November 18+
```

---

### Example 2: Development Team - Code Quality Standards

```markdown
## Rules & Best Practices

**Standards Discussed:** 7
**Parameters Referenced:** 12 (from Dev parameters)
**Departments Affected:** Dev

### Quality Standards

#### Code Test Coverage - Dev Department
- **Parameter:** PARAM-DEV-008 - `test_coverage_min`
- **Standard:** Minimum 80% test coverage required before merging to main branch
- **Current Value/Target:** 80% (industry best practice)
- **Context:** Recent production bugs could have been caught with better tests
- **Application:** Run coverage report before opening PR; if <80%, add more tests
- **Enforcement:** CI/CD pipeline blocks merge if coverage <80% (automated)
- **Examples:**
  - ✅ Good: Feature with 85% test coverage (unit + integration tests) → Merge approved
  - ❌ Bad: Feature with 60% coverage → Blocked until more tests added

#### Code Review Turnaround - Dev Department
- **Parameter:** PARAM-DEV-015 - `code_review_sla_hours`
- **Standard:** All pull requests must be reviewed within 24 hours
- **Current Value/Target:** 24 hours maximum
- **Context:** Recent delays in reviews blocking sprint progress
- **Application:** When PR opened, reviewer assigned; if not reviewed in 24 hours, escalate to tech lead
- **Enforcement:** Daily standup review of pending PRs; GitHub notifications
- **Examples:**
  - ✅ Good: PR opened Monday 2 PM → Reviewed Tuesday 10 AM (20 hours)
  - ❌ Bad: PR opened Monday → Still pending Friday (violates SLA)

#### Security Review Checklist - Dev Department
- **Parameter:** PARAM-DEV-022 - `security_checklist_required`
- **Standard:** All PRs touching authentication, payments, or user data must pass OWASP Top 10 security checklist
- **Current Value/Target:** 100% compliance (critical security requirement)
- **Context:** Recent close call with SQL injection vulnerability in code review
- **Application:** Reviewer checks against OWASP checklist; any issues = immediate reject
- **Enforcement:** Code review checklist includes security section
- **Examples:**
  - ✅ Good: API endpoint with parameterized queries (SQL injection safe) → Approved
  - ❌ Bad: API endpoint with string concatenation for SQL → Rejected immediately

### Process Standards

#### Staging Deployment Requirement - Dev Department
- **Process ID:** PROC-DEV-001 (Feature Development Workflow)
- **Standard:** All features must be deployed to staging and tested before production deployment (no direct-to-production)
- **Rationale:** Production bugs are 10x costlier to fix than staging bugs
- **Exceptions:** Critical hotfixes (with approval from tech lead)
- **Related Parameters:**
  - PARAM-DEV-025 - `staging_required`: true
  - PARAM-DEV-026 - `staging_test_duration_hours`: 24
- **Context Discussed:** Recent production bug could have been caught in staging; team skipped staging due to time pressure
- **Enforcement:** CI/CD pipeline enforces staging before production
- **Examples:**
  - ✅ Good: Deploy to staging → Test 24 hours → Deploy to production
  - ❌ Bad: Merge to main → Deploy directly to production (violates standard)

#### Git Branch Naming Convention - Dev Department
- **Process ID:** PROC-DEV-005 (Git Workflow)
- **Standard:** Branch names must follow format: `[type]/[ticket-id]-[description]`
  - Types: `feature/`, `bugfix/`, `hotfix/`, `refactor/`
  - Example: `feature/RH-123-user-dashboard`
- **Rationale:** Makes git history searchable; links to project management tickets
- **Exceptions:** None (strictly enforced)
- **Related Parameters:**
  - PARAM-DEV-030 - `branch_naming_enforced`: true
- **Context Discussed:** Current branches have inconsistent naming ("olha-branch-2", "fix", "test123")
- **Examples:**
  - ✅ Good: `feature/RH-456-payment-integration`
  - ❌ Bad: `olhas-new-feature` (no type, no ticket ID)

#### Pull Request Template - Dev Department
- **Process ID:** PROC-DEV-003 (Code Review Process)
- **Standard:** All PRs must use PR template with sections: (1) What changed, (2) Why, (3) Testing done, (4) Screenshots (if UI), (5) Checklist
- **Rationale:** Improves review efficiency; ensures nothing forgotten
- **Exceptions:** None (template auto-populates)
- **Related Parameters:**
  - PARAM-DEV-035 - `pr_template_required`: true
  - PARAM-DEV-036 - `pr_min_reviewers`: 2 (for backend changes)
- **Context Discussed:** Recent PRs lacked context; reviewers had to guess what changed
- **Examples:**
  - ✅ Good: PR with all sections filled, checklist completed → Easy to review
  - ❌ Bad: PR with title only, no description → Reviewer wastes time investigating

### Data Standards

#### API Response Format - Dev Department
- **Parameter:** PARAM-DEV-040 - `api_response_format`
- **Standard:** All API responses must follow JSON format: `{ success: boolean, data: {}, error: null | string }`
- **Measurement:** API tests validate response structure
- **Consequences:** Frontend breaks if format inconsistent
- **Context Discussed:** Current APIs have inconsistent response formats
- **Examples:**
  - ✅ Good: `{ "success": true, "data": { "user": {...} }, "error": null }`
  - ❌ Bad: `{ "user": {...} }` (missing success/error fields)

#### Environment Variables Security - Dev Department
- **Parameter:** PARAM-DEV-045 - `env_file_in_gitignore`
- **Standard:** Never commit `.env` files to git; use `.env.example` for template
- **Measurement:** Git pre-commit hook blocks `.env` commits
- **Consequences:** Security breach if API keys exposed in git history
- **Context Discussed:** Reminder after near-miss (developer almost committed `.env`)
- **Examples:**
  - ✅ Good: `.env` in `.gitignore`; `.env.example` committed (with dummy values)
  - ❌ Bad: `.env` committed with real API keys → Security vulnerability

### Communication Standards

**Daily Standups:**
- **Standard:** 15 minutes max; 3 questions: (1) What did you do yesterday? (2) What will you do today? (3) Any blockers?
- **Time:** 10:00 AM EET (daily)
- **Format:** Slack async or video call (team preference)
- **Related Parameter:** PARAM-DEV-050 - `standup_duration_minutes`: 15

**Documentation Updates:**
- **Standard:** All new features must include documentation updates (README, API docs, or wiki)
- **Enforcement:** PR checklist includes "Documentation updated?"
- **Purpose:** Prevent documentation debt

### New Best Practices Established

**Code Review Checklist (8-Item Standard):**
1. ✅ Code follows style guide (ESLint passing)
2. ✅ Logic is sound and efficient
3. ✅ No security vulnerabilities (OWASP check)
4. ✅ Tests included and passing (>80% coverage)
5. ✅ Edge cases handled
6. ✅ Documentation updated
7. ✅ No debug code (console.log removed)
8. ✅ Responsive design works (if frontend)

**Purpose:** Standardize review quality; new reviewers know what to check

**CI/CD Pipeline Optimization:**
- **Practice:** Use parallel jobs and caching to reduce build time from 15+ minutes to <10 minutes
- **Owner:** Olha to implement
- **Target:** <10 minutes for full pipeline (build + tests)
- **Related Parameter:** PARAM-DEV-055 - `ci_build_time_target_minutes`: 10

### Standards Violations/Issues

**Issue: Test Failures Ignored**
- **Violation:** Two recent merges had failing tests (developers merged anyway)
- **Impact:** Broken main branch; blocked other developers
- **Discussion:** Team agreed this is unacceptable
- **Resolution:** CI/CD pipeline now blocks merge on test failures (automated enforcement)
- **Related Parameter:** PARAM-DEV-008 - `block_merge_on_test_fail`: true

**Issue: Code Review Delays**
- **Violation:** 5 PRs from last sprint exceeded 24-hour review SLA
- **Impact:** Sprint velocity reduced; developers blocked
- **Discussion:** Reviewers overloaded; need to rotate review assignments
- **Resolution:** Implement round-robin review assignment; escalate if >24 hours

### Standards Updates

**Updated: Test Coverage Minimum**
- **Previous:** 70% coverage recommended (not enforced)
- **New:** 80% coverage required (enforced by CI/CD)
- **Reason:** Production bugs from untested code
- **Effective:** Starting next sprint (Nov 18)
- **Parameter:** PARAM-DEV-008 - `test_coverage_min`: 80 (was 70)

**Updated: PR Reviewers Required**
- **Previous:** 1 reviewer for all PRs
- **New:** 2 reviewers required for backend changes (1 reviewer for frontend)
- **Reason:** Backend changes are higher risk (database, APIs)
- **Effective:** Immediately
- **Parameter:** PARAM-DEV-036 - `pr_min_reviewers`: 2 (for backend), 1 (for frontend)
```

---

### Example 3: LG Team - Data Quality Standards

```markdown
## Rules & Best Practices

**Standards Discussed:** 6
**Parameters Referenced:** 10 (from LG parameters)
**Departments Affected:** LG

### Quality Standards

#### Lead Data Accuracy - LG Department
- **Parameter:** PARAM-LG-001 - `lead_accuracy_target`
- **Standard:** Minimum 92% data accuracy for all lead lists (up from 90%)
- **Current Value/Target:** 92% (industry-leading)
- **Context:** Recent client feedback; competitor lists had 95% accuracy; we need to match or exceed
- **Application:** Verify data using 3-step process: (1) Apollo.io enrichment, (2) Hunter.io email verification, (3) Manual spot-check 10% sample
- **Enforcement:** QA check before delivery; if <92%, rework required
- **Examples:**
  - ✅ Good: 1,000 leads → 920+ accurate (92%) → Deliver
  - ❌ Bad: 1,000 leads → 880 accurate (88%) → Rework required

#### Email Deliverability Rate - LG Department
- **Parameter:** PARAM-LG-005 - `email_deliverability_min`
- **Standard:** Minimum 95% email deliverability for all campaigns
- **Current Value/Target:** 95% (critical for campaign success)
- **Context:** October campaign achieved 96% deliverability (excellent); maintain this standard
- **Application:** Use Hunter.io or NeverBounce to verify emails before campaign; remove invalid/risky emails
- **Enforcement:** Test send to small batch (50-100 contacts) first; monitor bounce rate
- **Examples:**
  - ✅ Good: 1,000 emails sent → 960+ delivered (96%) → Exceeds standard
  - ❌ Bad: 1,000 emails sent → 920 delivered (92%) → Below standard (investigate)

#### Duplicate Removal - LG Department
- **Parameter:** PARAM-LG-010 - `duplicate_rate_max`
- **Standard:** Maximum 3% duplicates in final lead list (down from 8%)
- **Current Value/Target:** <3% duplicates
- **Context:** Recent list had 8% duplicates (unacceptable); need automated solution
- **Application:** Use Python script to auto-remove duplicates (email + domain matching)
- **Enforcement:** QA check counts duplicates before delivery
- **Examples:**
  - ✅ Good: 1,000 leads → 15 duplicates (1.5%) → Meets standard
  - ❌ Bad: 1,000 leads → 80 duplicates (8%) → Violates standard (rework)

### Process Standards

#### B2B Lead List Building Workflow - LG Department
- **Process ID:** PROC-LG-001 (7-step process, 5-7 days)
- **Standard:** All lead lists must follow 7-step workflow:
  1. ICP definition (client interview)
  2. Target list building (Apollo.io, LinkedIn Sales Navigator)
  3. Data scraping (automated tools)
  4. Data enrichment (email, phone, company data)
  5. Data cleaning (duplicates, invalid data removed)
  6. QA check (10% manual verification)
  7. Delivery (CSV + CRM import)
- **Rationale:** Proven process; 96% deliverability, 92% accuracy achieved
- **Exceptions:** Rush orders (3-day timeline) skip step 6 (QA reduced to spot-check)
- **Related Parameters:**
  - PARAM-LG-001 - `lead_accuracy_target`: 92%
  - PARAM-LG-005 - `email_deliverability_min`: 95%
  - PARAM-LG-015 - `lead_list_delivery_days`: 5-7
- **Context Discussed:** Process working very well; enforce consistency
- **Examples:**
  - ✅ Good: Follow all 7 steps → High-quality list delivered
  - ❌ Bad: Skip enrichment step (step 4) → Low-quality list, client dissatisfied

#### Campaign Warm-Up Period - LG Department
- **Process ID:** PROC-LG-003 (Email Outreach Campaign)
- **Standard:** All new email accounts must undergo 3-week warm-up period before full campaigns (increased from 2 weeks)
- **Rationale:** Prevents spam flagging; builds sender reputation
- **Exceptions:** Pre-warmed accounts (purchased from reputable vendor)
- **Related Parameters:**
  - PARAM-LG-020 - `email_warmup_weeks`: 3
  - PARAM-LG-021 - `warmup_daily_volume_start`: 10 emails/day
  - PARAM-LG-022 - `warmup_daily_volume_end`: 100 emails/day
- **Context Discussed:** Recent account got flagged after 2-week warmup; extend to 3 weeks for safety
- **Examples:**
  - ✅ Good: Week 1 (10/day) → Week 2 (30/day) → Week 3 (50/day) → Week 4 (100/day) → Full campaign
  - ❌ Bad: Start sending 500 emails/day immediately → Account flagged as spam

### Data Standards

#### Lead List File Format - LG Department
- **Parameter:** PARAM-LG-025 - `lead_list_format`
- **Standard:** All lead lists delivered in CSV format with columns: First Name, Last Name, Email, Company, Title, LinkedIn URL, Phone (if available), Industry, Company Size
- **Measurement:** Automated script validates column headers
- **Consequences:** Client can't import to CRM if format wrong
- **Context Discussed:** Recent client couldn't import list (missing columns)
- **Examples:**
  - ✅ Good: CSV with all 9 required columns (even if some fields empty)
  - ❌ Bad: CSV with only Name, Email (missing Company, Title, etc.)

#### LinkedIn Connection Request Limits - LG Department
- **Parameter:** PARAM-LG-030 - `linkedin_connection_daily_max`
- **Standard:** Maximum 20-30 LinkedIn connection requests per day (stay within LinkedIn ToS)
- **Measurement:** Phantombuster automation set to 25/day max
- **Consequences:** Account suspension if exceed limits
- **Context Discussed:** LinkedIn ToS considerations; conservative limits to avoid flagging
- **Examples:**
  - ✅ Good: Send 25 connection requests/day → Safe
  - ❌ Bad: Send 100 connection requests/day → Account at risk

### Communication Standards

**Campaign Copy Personalization:**
- **Standard:** All email/LinkedIn campaigns must include minimum 2 personalization tokens: {{FirstName}} + {{Company}}
- **Purpose:** Increased response by 40% (October campaign data)
- **Related Parameter:** PARAM-LG-035 - `personalization_tokens_min`: 2
- **Examples:**
  - ✅ Good: "Hi {{FirstName}}, I noticed {{Company}} is hiring for..."
  - ❌ Bad: "Hello, I wanted to reach out..." (generic, no personalization)

**A/B Testing Requirement:**
- **Standard:** All campaigns must A/B test 2-3 subject line variants
- **Purpose:** Improved open rates by 12% (October campaign)
- **Related Parameter:** PARAM-LG-040 - `ab_test_variants_min`: 2

### New Best Practices Established

**Lead Scoring Process (NEW):**
- **Purpose:** Prioritize highest-quality leads (not all leads equal)
- **Steps:**
  1. Apply scoring criteria: Company size (1-3 pts), Industry (1-2 pts), Title (1-3 pts), Engagement (1-2 pts)
  2. Score on 1-10 scale
  3. Segment: Hot (8-10), Warm (5-7), Cold (1-4)
  4. Prioritize outreach to Hot leads
- **Owner:** Plamena to draft full scoring criteria
- **Expected Result:** Higher meeting booking rate (focus on best leads)

**Data Quality Automation (NEW):**
- **Practice:** Use Python script to auto-remove duplicates and normalize data (save 2 hours per list)
- **Owner:** Isaac to build script (has prompt engineering skills)
- **Target:** Reduce manual data cleaning from 2 hours → 15 minutes
- **Related Parameter:** PARAM-LG-010 - `duplicate_rate_max`: 3%

**Campaign Copy Template Library (NEW):**
- **Practice:** Build template library for common campaign types (SaaS outreach, E-commerce, Agency, etc.)
- **Purpose:** Reduce copy creation time by 50%; maintain quality
- **Owner:** Nataliia to create library (10-15 templates)
- **Application:** Start with template, personalize for specific client

### Standards Violations/Issues

**Issue: Apollo.io Rate Limits Reached**
- **Violation:** Monthly export limit reached mid-month (can't build more lists)
- **Impact:** Blocked from delivering client lists
- **Discussion:** Need higher Apollo plan or supplement with LinkedIn Sales Navigator
- **Resolution:** Upgrade Apollo to higher tier (approved by Anastasiya)
- **Related Parameter:** PARAM-LG-045 - `apollo_monthly_export_limit`: 5,000 (will increase to 10,000)

**Issue: Duplicate Rate Too High**
- **Violation:** Recent list had 8% duplicates (target: <3%)
- **Impact:** Unprofessional delivery; client flagged issue
- **Discussion:** Manual duplicate removal insufficient; need automation
- **Resolution:** Isaac to build Python script for automated duplicate removal

### Standards Updates

**Updated: Lead Data Accuracy Target**
- **Previous:** 90% accuracy
- **New:** 92% accuracy
- **Reason:** Competitive pressure (competitors at 95%); client feedback
- **Effective:** All new lists starting this week
- **Parameter:** PARAM-LG-001 - `lead_accuracy_target`: 92 (was 90)

**Updated: Email Warm-Up Period**
- **Previous:** 2 weeks warm-up
- **New:** 3 weeks warm-up
- **Reason:** Recent account flagged after 2-week warmup
- **Effective:** All new email accounts
- **Parameter:** PARAM-LG-020 - `email_warmup_weeks`: 3 (was 2)

**Updated: Duplicate Rate Maximum**
- **Previous:** No formal limit (8% observed)
- **New:** Maximum 3% duplicates
- **Reason:** Quality standard; client expectations
- **Effective:** All lists starting next week (after automation script deployed)
- **Parameter:** PARAM-LG-010 - `duplicate_rate_max`: 3 (new standard)
```

---

## Validation Checklist

- [ ] **All standards mentioned** are captured
- [ ] **Parameters matched** to Parameters library (PARAM-XXX)
- [ ] **Specific thresholds** documented (numbers, percentages, time limits)
- [ ] **Context provided** for why standard exists
- [ ] **Application instructions** clear (how to apply standard)
- [ ] **Enforcement mechanism** noted (automated, manual review, checklist)
- [ ] **Examples included** (good vs bad)
- [ ] **Process standards linked** to Processes library (PROC-XXX)
- [ ] **Data standards** have measurement approach
- [ ] **New best practices** documented
- [ ] **Standards violations** captured (if discussed)
- [ ] **Standards updates** noted with before/after values
- [ ] **Departments identified** for each standard
- [ ] **Cross-references** to library files accurate

---

## Common Parameter Patterns

### Design Parameters (48 total)
- Quality thresholds (design_quality_min, client_satisfaction_min)
- Time limits (feedback_turnaround_hours, revision_deadline_days)
- Process requirements (design_system_required, mobile_first_required)
- File standards (figma_naming_convention, asset_delivery_formats)

### Development Parameters (124 total)
- Code quality (test_coverage_min, code_review_sla_hours)
- Security (security_checklist_required, owasp_check_enabled)
- Performance (build_time_target_minutes, api_response_time_ms)
- Process (staging_required, branch_naming_enforced)

### LG Parameters (78 total)
- Data quality (lead_accuracy_target, email_deliverability_min)
- Volume limits (linkedin_connection_daily_max, apollo_monthly_export_limit)
- Campaign metrics (open_rate_target, reply_rate_target)
- Process (warmup_weeks, personalization_tokens_min)

### Sales Parameters (52 total)
- Response times (proposal_turnaround_days, client_response_sla_hours)
- Pricing (discount_max_percent, payment_terms_days)
- Process (discovery_call_required, contract_review_required)

### Video Parameters (64 total)
- Quality (video_resolution_min, audio_quality_db)
- Timing (editing_turnaround_days, revision_rounds_max)
- Formats (export_formats_required, platform_specs)

---

## Related Templates

**Previous:** [05_Workflows_Processes.md](05_Workflows_Processes.md) - Process documentation
**Next:** [07_Problems_Solutions.md](07_Problems_Solutions.md) - Problem solving
**Libraries:** [../01_Library_Integration/08_Parameters_Lightweight.md](../01_Library_Integration/08_Parameters_Lightweight.md) - All parameters
**Reference:** [../03_Processing_Rules/](../03_Processing_Rules/) - Recognition rules

---

**Status:** ✅ Template ready for use
