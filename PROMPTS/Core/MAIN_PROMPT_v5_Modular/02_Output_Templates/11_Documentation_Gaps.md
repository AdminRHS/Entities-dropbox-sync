# Template 11: Documentation Gaps

**Purpose:** Track missing or outdated documentation identified in meetings
**Library Integration:** ⭐ Low (standalone documentation tracking)
**Priority:** Include when documentation issues are mentioned

---

## Template

```markdown
## Documentation Gaps

**Gaps Identified:** [Number]
**Documentation Updates Needed:** [Number]
**Outdated Docs:** [Number]
**Owners Assigned:** [Number]

### Critical Documentation Gaps

#### [Documentation Title/Topic]
- **Type:** [Process Doc | API Doc | User Guide | Technical Spec | Onboarding | Training]
- **Current State:** [Missing | Outdated | Incomplete]
- **Impact:** [How lack of documentation affects work]
- **Who Needs This:** [Team/role that needs this documentation]
- **Use Case:** [When/why this documentation is needed]
- **Content Needed:**
  - [Section 1]
  - [Section 2]
  - [Section 3]
- **Owner:** [Who will create/update this]
- **Deadline:** [When this is needed]
- **Priority:** [Critical | High | Medium | Low]
- **Related Process:** [PROC-XXX if applicable]

### High Priority Documentation

[Same structure, slightly more concise]

### Medium/Low Priority Documentation

[More concise format]

### Outdated Documentation

#### [Document Name]
- **Location:** [Where the doc lives]
- **Last Updated:** [Date]
- **What's Outdated:** [Specific sections or information]
- **Impact:** [Confusion, incorrect information, etc.]
- **Update Owner:** [Who will update]
- **Deadline:** [When update needed]

### Documentation Requests

[Documentation requested by team members]

### Knowledge Gaps

[Areas where team lacks knowledge; documentation could help]

### Documentation Debt

[Accumulating documentation that needs to be created]
```

---

## Recognition Rules

### Identifying Documentation Gaps

**Direct Mentions:**
- "We don't have documentation for..."
- "The docs are outdated..."
- "Where is the documentation for...?"
- "We need to document..."

**Confusion Indicators:**
- "I didn't know how to..."
- "Where do I find...?"
- "How does X work again?"
- "Can you explain...?" (indicates missing docs)

**Onboarding Issues:**
- "New team member asked where to find..."
- "Training would be easier if we had docs for..."

**Process Gaps:**
- "We keep doing this differently" (need standardization doc)
- "Everyone has their own way of..." (need process doc)

**Technical Gaps:**
- "API endpoints aren't documented"
- "No README for this repo"
- "Setup instructions missing"

---

## Examples

### Example 1: Development Team Documentation Gaps

```markdown
## Documentation Gaps

**Gaps Identified:** 5
**Documentation Updates Needed:** 2
**Outdated Docs:** 2
**Owners Assigned:** 3

### Critical Documentation Gaps

#### API Documentation for v2 Endpoints
- **Type:** API Documentation
- **Current State:** Missing (v2 API being built, no docs yet)
- **Impact:**
  - Frontend developers can't build against new API (blocked)
  - Integration partners can't plan migration from v1 to v2
  - Testing incomplete (QA doesn't know expected responses)
- **Who Needs This:** Frontend developers (internal), integration partners (external), QA team
- **Use Case:**
  - Developers: Understand endpoints, request/response formats, authentication
  - Partners: Plan migration timeline, update integration code
  - QA: Write test cases, validate responses
- **Content Needed:**
  - Endpoint list (all v2 endpoints with URLs, methods)
  - Authentication flow (JWT token usage)
  - Request/response schemas (JSON examples)
  - Error codes and handling
  - Rate limiting rules
  - Migration guide (v1 → v2 differences)
  - Code examples (cURL, JavaScript, Python)
- **Owner:** Olha Kizilova (ID: 178) - Backend Developer (building the API)
- **Deadline:** December 1, 2025 (before frontend integration starts)
- **Priority:** Critical (blocks other teams)
- **Related Process:** PROC-DEV-001 (Feature Development Workflow) - Documentation is step 7

**Implementation Plan:**
- Week 1 (Nov 18-22): Set up Swagger/OpenAPI spec (auto-generate from code)
- Week 2 (Nov 25-29): Write migration guide, add code examples
- Week 3 (Dec 2): Review with frontend team, incorporate feedback
- **Tools:** Swagger UI for interactive docs, hosted at `https://api.remotehelpers.com/docs/v2`

#### Onboarding Guide for New Developers
- **Type:** Onboarding Documentation
- **Current State:** Incomplete (has setup instructions, missing workflow/culture/resources)
- **Impact:**
  - New developers take 2-3 weeks to ramp up (could be 1 week with better docs)
  - Repeated questions asked to senior devs (time drain)
  - Inconsistent understanding of processes (everyone learns differently)
- **Who Needs This:** New developer hires, contractors, interns
- **Use Case:** First day → Week 1 onboarding (read docs, follow setup, understand workflow)
- **Content Needed:**
  - **Existing (good):** Development environment setup (git, docker, IDE)
  - **Missing:**
    - Team structure (who does what, who to ask for help)
    - Workflow overview (how we work: sprint planning, standups, code reviews)
    - Coding standards (linting, formatting, naming conventions)
    - Git workflow (branching strategy, commit message format, PR process)
    - Testing requirements (coverage, test types, how to run tests)
    - Deployment process (staging, production, rollback)
    - Communication norms (Slack channels, meeting schedule, async vs sync)
    - Resources (where to find designs, API docs, project specs)
    - First week checklist (complete these tasks to validate setup)
- **Owner:** Yaroslav Klimenko (ID: 86478) - Has been with team longest, good writer
- **Deadline:** December 15, 2025 (before next developer hire in January)
- **Priority:** Critical (hiring senior frontend dev in January; need this ready)
- **Related Process:** PROC-HR-ONBOARD-001 (Onboarding workflow)

**Implementation Plan:**
- Week 1 (Nov 18-22): Draft outline, identify existing resources to link
- Week 2 (Nov 25-29): Write missing sections (workflow, standards, etc.)
- Week 3 (Dec 2-6): Review with team (get feedback from Olha, Liliia)
- Week 4 (Dec 9-13): Finalize, add to team wiki
- **Format:** Notion page (team wiki), linked from README

### High Priority Documentation

#### CI/CD Pipeline Troubleshooting Guide
- **Type:** Technical Documentation
- **Current State:** Missing
- **Impact:** When pipeline fails, developers waste 30-60 minutes debugging (common issues not documented)
- **Who Needs This:** All developers (especially junior devs like Liliia)
- **Content Needed:**
  - Common failure scenarios (test failures, linting errors, build errors, deployment errors)
  - How to diagnose (where to check logs, what errors mean)
  - How to fix (step-by-step solutions)
  - When to escalate (if can't fix in 15 minutes, ask senior dev)
- **Owner:** Olha (has most CI/CD experience)
- **Deadline:** End of November
- **Priority:** High (saves significant debugging time)

#### Database Migration Best Practices
- **Type:** Technical Documentation
- **Current State:** Missing
- **Impact:**
  - Recent migration caused data loss (developer didn't know to back up first)
  - Inconsistent migration process (everyone does it differently)
- **Who Needs This:** Backend developers (Olha, Yaroslav)
- **Content Needed:**
  - When to create migration (schema changes, data changes)
  - How to write safe migrations (transactions, rollback plan)
  - Testing migrations (test on staging first)
  - Deployment process (run migration before deploying code)
  - Rollback procedure (if migration fails)
- **Owner:** Olha
- **Deadline:** November 22 (before next migration)
- **Priority:** High (prevents data loss)

### Medium/Low Priority Documentation

#### Code Review Checklist (Medium)
- **Type:** Process Documentation
- **Current State:** Informal (reviewers use mental checklist)
- **Impact:** Inconsistent code review quality
- **Owner:** Olha to document standard 8-item checklist
- **Deadline:** End of November

#### Environment Variables Reference (Low)
- **Type:** Technical Documentation
- **Current State:** Missing (developers refer to `.env.example` but no explanation of what each variable does)
- **Owner:** Yaroslav
- **Deadline:** Mid-December

### Outdated Documentation

#### Main API README
- **Location:** `backend/README.md` (GitHub repo)
- **Last Updated:** March 2024 (8 months ago)
- **What's Outdated:**
  - Endpoints list (missing 5 new endpoints added in last 6 months)
  - Authentication section (now uses JWT, README says session cookies)
  - Setup instructions (Docker setup changed in July)
  - Contributors list (missing Liliia, who joined in May)
- **Impact:**
  - New developers follow wrong setup (waste time debugging)
  - External partners see incorrect API info
- **Update Owner:** Olha
- **Deadline:** November 25 (quick update, 1 hour)

#### Deployment Guide
- **Location:** Confluence wiki page
- **Last Updated:** January 2024 (10 months ago)
- **What's Outdated:**
  - Deployment process changed (now use GitHub Actions, guide says manual deploy)
  - Server IP addresses changed (migrated to new AWS instances in June)
  - Environment variables (3 new variables added, not in guide)
- **Impact:** Deployment failures if following outdated guide
- **Update Owner:** Yaroslav
- **Deadline:** November 29

### Documentation Requests

**Request 1: Docker Best Practices (from Liliia)**
- **Requester:** Liliia (junior dev)
- **Need:** How to write efficient Dockerfiles, use multi-stage builds, optimize image size
- **Context:** Working on optimizing CI/CD pipeline; needs to learn Docker best practices
- **Owner:** Olha to write guide or link to external resources
- **Timeline:** End of November

**Request 2: React Performance Patterns (from Yaroslav)**
- **Requester:** Yaroslav (full-stack dev, wants to improve React skills)
- **Need:** Performance optimization techniques (memoization, lazy loading, code splitting)
- **Context:** Preparing for Client A project (complex React dashboard)
- **Owner:** Can wait until senior frontend dev hired (they can create this doc)
- **Timeline:** January (after new hire starts)

### Knowledge Gaps

**Gap 1: Team doesn't understand new auth architecture**
- **Issue:** Auth microservice is complex; team needs to understand how it works (not just use it)
- **Impact:** Can't debug issues, can't contribute to auth service development
- **Solution:** Architecture documentation + knowledge-sharing session
- **Owner:** Olha to create architecture diagram + host 1-hour session
- **Timeline:** Mid-December (after auth service deployed)

**Gap 2: QA testing process unclear**
- **Issue:** No formal QA process; developers test their own work (inconsistent quality)
- **Impact:** Bugs reach production
- **Solution:** Define QA process (what to test, when, who, how)
- **Owner:** Anastasiya + Olha to define process, document it
- **Timeline:** December

### Documentation Debt

**Total Debt:** 7 critical docs missing, 2 outdated docs, 5 improvement opportunities

**High-Debt Areas:**
1. **API Documentation:** Critical gap (v2 API undocumented)
2. **Onboarding:** Incomplete (slows down new hires)
3. **Troubleshooting Guides:** Missing (wastes developer time)
4. **Process Documentation:** Informal (inconsistent execution)

**Action Plan:**
- Prioritize API docs (Dec 1 deadline - hard blocker)
- Onboarding docs (Dec 15 deadline - have hire in January)
- Troubleshooting guides (November - quick wins, high impact)
- Update outdated docs (November - low effort, prevents confusion)

**Documentation Champions:**
- Olha: Technical lead (API docs, architecture, troubleshooting)
- Yaroslav: Process expert (onboarding, deployment, workflows)
- Liliia: Fresh perspective (can identify gaps new devs face)
```

---

### Example 2: Design Team Documentation Gaps

```markdown
## Documentation Gaps

**Gaps Identified:** 3
**Documentation Updates Needed:** 1
**Outdated Docs:** 1
**Owners Assigned:** 2

### Critical Documentation Gaps

#### Design System Component Library Documentation
- **Type:** Technical Specification + User Guide
- **Current State:** Incomplete (components exist in Figma, minimal documentation)
- **Impact:**
  - Designers don't know when to use which component (inconsistent usage)
  - New designers can't learn design system (steep learning curve)
  - Developers receive designs with custom components (should use design system)
- **Who Needs This:** All designers (9 people), developers (handoff clarity)
- **Use Case:**
  - Start new project → Review design system docs → Use correct components
  - Design review → Check if design system used correctly
  - Developer handoff → Developer knows which components to build
- **Content Needed:**
  - Component catalog (all 50+ components with screenshots)
  - Usage guidelines (when to use each component)
  - Variants (different states: default, hover, active, disabled)
  - Spacing rules (margins, padding, layout grid)
  - Typography scale (font sizes, line heights, weights)
  - Color palette (primary, secondary, neutrals, semantic colors)
  - Accessibility guidelines (color contrast, keyboard navigation)
  - Do's and Don'ts (examples of good and bad usage)
  - Version history (track design system changes)
- **Owner:** Anastasiia (ID: 86981) - Design Lead
- **Deadline:** December 15, 2025
- **Priority:** Critical (prevents design inconsistencies)
- **Related Process:** PROC-DESIGN-001 (UI/UX Design Process)

**Implementation Plan:**
- Week 1: Document top 20 components (buttons, forms, cards - most used)
- Week 2: Document next 20 components
- Week 3: Document remaining components + guidelines
- Week 4: Team review, finalize
- **Format:** Figma Community file (searchable, visual) + Notion page (written guidelines)

### High Priority Documentation

#### Figma File Organization Standard
- **Type:** Process Documentation
- **Current State:** Draft created (this meeting), not finalized
- **Impact:** Figma workspace is disorganized (hard to find files)
- **Owner:** Anastasiia (created draft, needs team review)
- **Deadline:** November 22 (next team meeting for approval)
- **Priority:** High

#### Client Handoff Checklist
- **Type:** Process Documentation
- **Current State:** Missing (informal process)
- **Impact:** Inconsistent client deliverables (some designers send 4 formats, others send 2)
- **Content Needed:**
  - What to deliver (Figma link, PDF, PNG/JPG assets, source files)
  - File naming conventions
  - Folder structure (organized Google Drive folder)
  - Delivery email template
- **Owner:** Olha (ID: 86641) - Senior Designer
- **Deadline:** End of November
- **Priority:** High

### Outdated Documentation

#### Design Process Workflow
- **Location:** Team wiki (Notion)
- **Last Updated:** 6 months ago
- **What's Outdated:**
  - Says "desktop-first design" (now mobile-first as of this meeting)
  - Missing new steps (design system review, peer critique)
  - Client feedback SLA not documented (now 48 hours)
- **Update Owner:** Anastasiia
- **Deadline:** November 25 (reflect new mobile-first decision)
```

---

## Validation Checklist

- [ ] **All documentation gaps** mentioned are captured
- [ ] **Type** of documentation identified
- [ ] **Current state** assessed (Missing, Outdated, Incomplete)
- [ ] **Impact** of gap described
- [ ] **Who needs** this documentation
- [ ] **Content needed** outlined
- [ ] **Owner** assigned
- [ ] **Deadline** set
- [ ] **Priority** assessed
- [ ] **Outdated docs** tracked with update plans
- [ ] **Documentation requests** noted
- [ ] **Knowledge gaps** identified
- [ ] **Documentation debt** summarized

---

## Related Templates

**Previous:** [10_Decisions_Log.md](10_Decisions_Log.md) - Decisions may create documentation needs
**Next:** [12_Communication_Announcements.md](12_Communication_Announcements.md) - Communications
**Related:** [03_Action_Items_Tasks.md](03_Action_Items_Tasks.md) - Documentation tasks

---

**Status:** ✅ Template ready for use
