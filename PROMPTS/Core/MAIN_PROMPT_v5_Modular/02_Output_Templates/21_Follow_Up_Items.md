# Template 21: Follow-Up Items

**Purpose:** Track all follow-up items, pending actions, and next steps from the meeting
**Library Integration:** ⭐⭐⭐ Heavy (Actions, comprehensive summary of all action items)
**Priority:** ALWAYS INCLUDE (every meeting has follow-ups)

---

## Template

```markdown
## Follow-Up Items

**Total Follow-Ups:** [Number]
**Owners:** [Number of people with actions]
**Due This Week:** [Number]
**Due Next Week:** [Number]
**Overdue:** [Number]

### Immediate Actions (Next 1-3 Days)

#### [Action Item]
- **Action:** [ACT-XXX] - [Action name from Responsibilities/Responsibilities/Actions library]
- **Description:** [What needs to be done]
- **Owner:** [Name] (ID: [Employee ID])
- **Due:** [Specific date]
- **Priority:** [Critical | High | Medium | Low]
- **Dependencies:** [What's needed to complete this]
- **Related:** [Link to task, project, decision]

### This Week (Next 7 Days)

[Same structure as Immediate Actions]

### Next Week (8-14 Days)

[Same structure]

### This Month

[Same structure, can be more concise]

### Pending on External

[Items waiting on clients, vendors, approvals]

### Recurring Follow-Ups

[Ongoing commitments, weekly/monthly tasks]

### Meeting Schedule

[Next meetings scheduled, recurring check-ins]

### Communication Follow-Ups

[Announcements to send, emails to write, stakeholders to inform]

### Blocked Follow-Ups

[Actions that can't proceed until blocker resolved]

---

## Summary by Owner

### [Owner Name] (ID: [Employee ID])
- [ ] Action 1 (Due: [Date])
- [ ] Action 2 (Due: [Date])
- [ ] Action 3 (Due: [Date])

[Repeat for each owner]

---

## Critical Path Items

[Items that block other work if not completed]

---

## Follow-Up from Previous Meeting

[Items carried over from previous discussions]
```

---

## Examples

```markdown
## Follow-Up Items

**Total Follow-Ups:** 32
**Owners:** 8 people with actions
**Due This Week:** 15 actions
**Due Next Week:** 10 actions
**Overdue:** 0

### Immediate Actions (Next 1-3 Days)

#### Provision AWS ElastiCache Redis Cluster
- **Action:** ACT-DEV-INFRA-001 - Set up infrastructure
- **Description:** Provision AWS ElastiCache Redis cluster for auth microservice (staging + production)
- **Owner:** Anastasiya (Sales Manager - has AWS access)
- **Due:** November 18, 2025 (Monday - start of Week 1)
- **Priority:** Critical (blocks auth microservice development)
- **Dependencies:** AWS account access, budget approved ($135/month - already confirmed)
- **Configuration:**
  - Staging: t3.micro, 1GB, single node, $15/month
  - Production: t3.small, 4GB, 3-node cluster, $120/month
- **Related:** Auth microservice project (Template 09, Technical Architecture)

#### Apollo.io Usage Monitoring Setup
- **Action:** ACT-LG-AI-002 - Monitor tool usage
- **Description:** Set up monthly Apollo.io usage tracking (alert at 70% capacity - 7,000/10,000 exports)
- **Owner:** Hanan Zaheur (ID: 87984) - LG Team Lead
- **Due:** November 18, 2025 (Monday)
- **Priority:** Medium (prevents future mid-month capacity issues)
- **Dependencies:** None (simple spreadsheet tracking or calendar reminder)
- **Related:** Apollo upgrade decision (Template 10, Decisions Log)

#### Post Job Ads for Senior Frontend Developer
- **Action:** ACT-HR-RECRUIT-001 - Post job listings
- **Description:** Post senior frontend developer job ads on 5 platforms (LinkedIn, Upwork, React Jobs, AngelList, Remote OK)
- **Owner:** Anastasiya (Sales Manager - recruitment lead)
- **Due:** November 18-25, 2025 (this week)
- **Priority:** Critical (4-week recruitment timeline, need to start immediately)
- **Dependencies:**
  - Job description finalized (Olha + Anastasiya collaboration - complete by Nov 18)
  - Budget approved ($3,000/month max - already confirmed)
- **Related:** Senior frontend hire decision (Template 10, Decisions Log)

#### Post Job Ads for Lead Generator
- **Action:** ACT-HR-RECRUIT-001 - Post job listings
- **Description:** Post lead generator job ads (Upwork, LinkedIn, internal network)
- **Owner:** Anastasiya (recruitment lead)
- **Due:** November 18-25, 2025 (this week)
- **Priority:** High (target Dec 9 start date)
- **Dependencies:** Job description drafted
- **Related:** LG hire decision (Template 10, Decisions Log)

#### Configure GitHub Round-Robin PR Review Assignment
- **Action:** ACT-DEV-CONFIG-001 - Configure automation
- **Description:** Set up GitHub Actions to auto-assign PR reviewers using round-robin algorithm (balance review load)
- **Owner:** Yaroslav Klimenko (ID: 86478) - Developer
- **Due:** November 22, 2025 (Friday - end of week)
- **Priority:** High (reduces code review bottleneck)
- **Dependencies:** None (Yaroslav has capacity this week)
- **Related:** Code review bottleneck (Template 07, Problems & Solutions)

### This Week (Next 7 Days)

#### Implement CI/CD Pipeline Optimizations
- **Action:** ACT-DEV-OPTIMIZE-001 - Optimize code/infrastructure
- **Description:** Optimize GitHub Actions CI/CD pipeline (caching, parallel tests, Docker multi-stage builds) to reduce build time from 15-20 min → 6-8 min
- **Owner:** Olha Kizilova (ID: 178) - Backend Developer
- **Due:** November 22, 2025 (Friday)
- **Priority:** High (saves 6-13 hours/day of developer waiting time)
- **Dependencies:** None (Olha has capacity this week)
- **Steps:**
  1. Implement dependency caching (npm/yarn, pip)
  2. Configure parallel test execution (4 jobs)
  3. Optimize Dockerfiles (multi-stage builds)
  4. Test on sample repo, roll out to all repos
- **Related:** CI/CD blocker (Template 13, Blockers & Dependencies)

#### Design Auth Microservice API Contract
- **Action:** ACT-DEV-DESIGN-001 - Design system architecture
- **Description:** Design API contract for auth microservice (endpoints, request/response schemas, authentication flow)
- **Owner:** Olha Kizilova (ID: 178)
- **Due:** November 22, 2025 (end of Week 1)
- **Priority:** Critical (blocks Week 2-3 development)
- **Dependencies:** Redis provisioned (Anastasiya, Nov 18)
- **Related:** Auth microservice project (Template 09, Technical Architecture)

#### Configure Auth Service CI/CD Pipeline
- **Action:** ACT-DEV-CONFIG-002 - Set up CI/CD
- **Description:** Configure GitHub Actions workflow for auth microservice (testing, build, deploy)
- **Owner:** Yaroslav Klimenko (ID: 86478)
- **Due:** November 22, 2025 (end of Week 1)
- **Priority:** Critical (needed for Week 2 development)
- **Dependencies:** None
- **Related:** Auth microservice infrastructure (Template 09, Technical Architecture)

#### Draft Figma File Organization Standard
- **Action:** ACT-DESIGN-DOC-001 - Create documentation
- **Description:** Finalize Figma file organization standard (naming convention, folder structure)
- **Owner:** Anastasiia (ID: 86981) - Design Lead
- **Due:** November 22, 2025 (Friday - team review next meeting)
- **Priority:** High (reduces time wasted searching for files)
- **Dependencies:** Draft created (in progress)
- **Related:** Figma organization issue (Template 18, Design Context)

#### Finalize Senior Frontend Developer Job Description
- **Action:** ACT-HR-RECRUIT-002 - Create job description
- **Description:** Finalize job description for senior frontend developer (Olha technical requirements + Anastasiya company/role description)
- **Owner:** Olha (technical requirements) + Anastasiya (company description)
- **Due:** November 18, 2025 (Monday - before posting job ads)
- **Priority:** Critical (blocks recruitment)
- **Dependencies:** None (quick collaboration)
- **Related:** Senior hire decision (Template 10, Decisions Log)

#### Send Client A Timeline Update Email
- **Action:** ACT-SALES-COMM-001 - Communicate with client
- **Description:** Email Client A with project timeline update (start date: Jan 6, explain senior hire needed)
- **Owner:** Anastasiya (client relationship owner)
- **Due:** November 20, 2025 (Wednesday)
- **Priority:** High (manage client expectations)
- **Dependencies:** Olga confirms timeline is realistic
- **Related:** Client A project (Template 17, LG & Sales Context)

#### Audit Adobe CC License Usage
- **Action:** ACT-DESIGN-AI-001 - Audit tool usage
- **Description:** Audit who uses Adobe Creative Cloud in last 30 days; cancel 3 unused seats (save $165/month)
- **Owner:** Olha (ID: 86641) - Senior Designer
- **Due:** November 30, 2025 (end of month)
- **Priority:** Medium (cost optimization)
- **Dependencies:** None
- **Related:** Adobe license decision (Template 18, Design Context)

#### Create Code Review Checklist
- **Action:** ACT-DEV-DOC-002 - Create documentation
- **Description:** Document 8-item code review checklist (style, logic, security, tests, edge cases, docs, debug code, responsive)
- **Owner:** Olha Kizilova (ID: 178)
- **Due:** November 22, 2025 (Friday)
- **Priority:** High (standardizes code review quality)
- **Dependencies:** None
- **Related:** Code quality standards (Template 19, Dev Context)

#### Host Docker Best Practices Training
- **Action:** ACT-DEV-TRAIN-001 - Conduct training
- **Description:** Host 30-minute training session on Docker best practices for Liliia (multi-stage builds, optimization)
- **Owner:** Olha (trainer)
- **Due:** November 22, 2025 (any day this week)
- **Priority:** Medium (skill development)
- **Dependencies:** None
- **Related:** Training needs (Template 20, Onboarding & Training)

#### Complete LinkedIn Sales Navigator Course
- **Action:** ACT-LG-TRAIN-001 - Complete training
- **Description:** Complete LinkedIn Sales Navigator online course (2 hours, advanced filters)
- **Owner:** Hanan Zaheur (ID: 87984)
- **Due:** November 22, 2025 (end of week)
- **Priority:** Medium (skill improvement for Q4 campaign)
- **Dependencies:** None (self-paced course)
- **Related:** Training needs (Template 20, Onboarding & Training)

#### Build Q4 LinkedIn Campaign Target List
- **Action:** ACT-LG-LISTBUILD-001 - Build lead list
- **Description:** Build 1,000-contact target list for Q4 LinkedIn campaign using Sales Navigator filters
- **Owner:** Hanan Zaheur (ID: 87984)
- **Due:** November 22, 2025 (Friday)
- **Priority:** High (Q4 campaign starts next week)
- **Dependencies:** Sales Navigator course completed (improves targeting)
- **Related:** Q4 LinkedIn campaign (Template 17, LG & Sales Context)

#### Configure Phantombuster Workflows for Q4 Campaign
- **Action:** ACT-LG-AUTO-001 - Configure automation
- **Description:** Set up Phantombuster workflows for Q4 LinkedIn campaign (20 connections/day, 3-5 message sequence)
- **Owner:** Plamena Peneva (ID: 86297)
- **Due:** November 22, 2025 (Friday)
- **Priority:** High (Q4 campaign starts next week)
- **Dependencies:** Target list from Hanan (Nov 22)
- **Related:** Q4 LinkedIn campaign (Template 17, LG & Sales Context)

### Next Week (8-14 Days)

#### Update README with API Changes
- **Action:** ACT-DEV-DOC-003 - Update documentation
- **Description:** Update main API README (5 new endpoints, JWT authentication, Docker setup, contributors list)
- **Owner:** Olha Kizilova (ID: 178)
- **Due:** November 25, 2025 (Monday next week)
- **Priority:** Medium (outdated docs causing confusion)
- **Dependencies:** None (1-hour task)
- **Related:** Outdated documentation (Template 11, Documentation Gaps)

#### Update Deployment Guide
- **Action:** ACT-DEV-DOC-004 - Update documentation
- **Description:** Update deployment guide (GitHub Actions process, new server IPs, environment variables)
- **Owner:** Yaroslav Klimenko (ID: 86478)
- **Due:** November 29, 2025 (Friday next week)
- **Priority:** Medium (outdated docs)
- **Dependencies:** None
- **Related:** Outdated documentation (Template 11, Documentation Gaps)

#### Build Auth Microservice (Weeks 2-3)
- **Action:** ACT-DEV-BUILD-001 - Develop feature
- **Description:** Build auth microservice (login, logout, refresh, verify endpoints; JWT + Redis integration)
- **Owner:** Olha Kizilova (ID: 178) - lead; Yaroslav Klimenko (ID: 86478) - support
- **Due:** December 6, 2025 (end of Week 3)
- **Priority:** Critical (5-week project timeline)
- **Dependencies:** API contract designed (Week 1), Redis provisioned (Week 1)
- **Related:** Auth microservice project (Template 09, Technical Architecture)

#### Create Campaign Copy Template Library
- **Action:** ACT-LG-DOC-001 - Create documentation
- **Description:** Build campaign copy template library (10-15 proven subject line formulas, 5 email body templates, 3 CTA styles)
- **Owner:** Nataliia Rybak (ID: 88054) - Content Manager
- **Due:** November 30, 2025 (end of month)
- **Priority:** Medium (reduces campaign creation time by 50%)
- **Dependencies:** None
- **Related:** Best practices (Template 14, Insights & Lessons)

#### Draft Lead Scoring Criteria
- **Action:** ACT-LG-PROCESS-001 - Create process
- **Description:** Draft lead scoring criteria (1-10 scale based on company size, title, industry, engagement)
- **Owner:** Plamena Peneva (ID: 86297)
- **Due:** November 22, 2025 (next week)
- **Priority:** High (improves campaign targeting)
- **Dependencies:** None
- **Related:** Lead scoring insights (Template 17, LG & Sales Context)

#### Host Figma Auto Layout Training
- **Action:** ACT-DESIGN-TRAIN-001 - Conduct training
- **Description:** Host 1-hour Figma Auto Layout training for junior designers (Solomia, Daria)
- **Owner:** Anastasiia (ID: 86981) - Design Lead
- **Due:** November 22, 2025 (Friday next week)
- **Priority:** Medium (skill development)
- **Dependencies:** None
- **Related:** Training needs (Template 20, Onboarding & Training)

### This Month

#### Create API Documentation for v2
- **Action:** ACT-DEV-DOC-005 - Create documentation
- **Description:** Create comprehensive API documentation for v2 (Swagger/OpenAPI spec, migration guide, code examples)
- **Owner:** Olha Kizilova (ID: 178)
- **Due:** December 1, 2025
- **Priority:** Critical (blocks frontend integration)
- **Dependencies:** v2 API development mostly complete
- **Related:** Documentation gap (Template 11, Documentation Gaps)

#### Create Developer Onboarding Guide
- **Action:** ACT-DEV-DOC-006 - Create documentation
- **Description:** Write comprehensive developer onboarding guide (team structure, workflow, coding standards, git process, testing, deployment, communication, resources, first week checklist)
- **Owner:** Yaroslav Klimenko (ID: 86478)
- **Due:** December 15, 2025
- **Priority:** Critical (senior hire starts Jan 6 - need this ready)
- **Dependencies:** None
- **Related:** Onboarding plan (Template 20, Onboarding & Training)

#### Update LG Onboarding Materials
- **Action:** ACT-LG-DOC-002 - Update documentation
- **Description:** Update LG onboarding materials (tools setup, 7-step process, quality standards, campaign best practices, client communication templates)
- **Owner:** Hanan Zaheur (ID: 87984)
- **Due:** December 1, 2025
- **Priority:** Critical (new hire starts Dec 9 - need this ready)
- **Dependencies:** None
- **Related:** Onboarding plan (Template 20, Onboarding & Training)

#### Create Design System Documentation
- **Action:** ACT-DESIGN-DOC-002 - Create documentation
- **Description:** Create comprehensive design system documentation (component catalog, usage guidelines, typography, colors, spacing, accessibility, do's and don'ts)
- **Owner:** Anastasiia (ID: 86981)
- **Due:** December 15, 2025
- **Priority:** Critical (prevents design inconsistencies)
- **Dependencies:** None (4-week project)
- **Related:** Design system gap (Template 18, Design Context)

#### Interview Candidates for Senior Frontend Developer
- **Action:** ACT-HR-RECRUIT-003 - Interview candidates
- **Description:** Review applications, conduct technical interviews (live coding challenges), culture fit interviews for senior frontend role
- **Owner:** Anastasiya (recruitment lead), Olha (technical interviews)
- **Due:** November 25 - December 20, 2025 (4 weeks)
- **Priority:** Critical (need to make offer by Dec 23)
- **Dependencies:** Job ads posted (Nov 18-25), applications received
- **Related:** Senior hire decision (Template 10, Decisions Log)

#### Interview Candidates for Lead Generator
- **Action:** ACT-HR-RECRUIT-004 - Interview candidates
- **Description:** Review applications, conduct interviews for LG position
- **Owner:** Anastasiya (recruitment lead), Hanan (LG team interviews)
- **Due:** November 25 - December 6, 2025 (2 weeks)
- **Priority:** High (need to make offer by Dec 6 for Dec 9 start)
- **Dependencies:** Job ads posted (Nov 18-25), applications received
- **Related:** LG hire decision (Template 10, Decisions Log)

### Pending on External

#### Waiting on Client A - Requirements Finalization
- **Action:** Client A to provide final requirements document
- **Owner (Internal):** Anastasiya (following up)
- **Expected:** November 20, 2025
- **Follow-up Plan:**
  - Nov 20: If not received, send reminder email
  - Nov 22: If still not received, schedule call
  - Nov 25: If still not received, escalate (flag timeline risk)
- **Impact:** Can't finalize project plan without requirements
- **Related:** Client A project (Template 17, LG & Sales Context)

### Recurring Follow-Ups

#### Weekly LG Team Check-In
- **Frequency:** Weekly (Mondays, 10 AM)
- **Participants:** LG team (11 members + new hire starting Dec 9)
- **Purpose:** Review active campaigns, discuss blockers, share learnings
- **Owner:** Hanan (team lead)

#### Weekly Dev Team Standup
- **Frequency:** Daily (async in Slack or video call, 15 min)
- **Participants:** Dev team (Olha, Yaroslav, Liliia, new hire starting Jan 6)
- **Purpose:** 3 questions (What did you do yesterday? What will you do today? Any blockers?)
- **Owner:** Olha (tech lead)

#### Weekly Design Team Sync
- **Frequency:** Weekly (Fridays)
- **Participants:** Design team (9 designers)
- **Purpose:** Design critiques (15 min per project), share updates, discuss standards
- **Owner:** Anastasiia (design lead)

#### Monthly Campaign Retrospective (LG Team)
- **Frequency:** Monthly (first Monday of month)
- **Participants:** LG team
- **Purpose:** Review all campaigns from previous month, share learnings, update best practices
- **Owner:** Hanan (team lead)

### Meeting Schedule

#### Next All-Hands Meeting
- **Date:** November 22, 2025 (Friday, 3 PM)
- **Purpose:** Company-wide updates (hiring announcements, auth microservice explanation, Q4 progress)
- **Participants:** All Remote Helpers employees
- **Agenda:**
  - New hire announcements (LG, Dev)
  - Auth microservice project update (Olha)
  - Q4 achievements (Anastasiya)
  - Q&A

#### Senior Frontend Developer - Final Interview
- **Date:** TBD (mid-December after candidates narrowed)
- **Purpose:** Final interview with top candidate (offer decision)
- **Participants:** Anastasiya, Olha, candidate

#### Client A - Requirements Review Call
- **Date:** November 25, 2025 (tentative - depends on requirements received)
- **Purpose:** Review finalized requirements, Q&A, confirm timeline
- **Participants:** Anastasiya, Olha, Client A stakeholders

### Communication Follow-Ups

#### Announce New Hires (Company-Wide)
- **What:** Slack #general + company email announcing LG and Dev hires
- **When:** When candidates accept offers (LG: ~Dec 6, Dev: ~Dec 23)
- **Owner:** Anastasiya
- **Related:** Communication plan (Template 12, Communication & Announcements)

#### Auth Microservice Project Update (Team Announcement)
- **What:** Explain auth microservice project to company (why dev team focused on infrastructure for 5 weeks)
- **When:** November 18, 2025 (Monday)
- **Owner:** Olha or Anastasiya
- **Related:** Communication plan (Template 12, Communication & Announcements)

#### Mobile-First Design Standard (Design Team + Dev Team)
- **What:** Announce new mobile-first design standard to design team (detailed) and dev team (FYI)
- **When:** November 18, 2025 (Monday)
- **Owner:** Anastasiia
- **Related:** Communication plan (Template 12, Communication & Announcements)

### Blocked Follow-Ups

#### Frontend Integration (Blocked Until API Docs Complete)
- **Action:** Start frontend v2 API integration
- **Owner:** Frontend team (when senior hire starts)
- **Blocked By:** API documentation missing (Olha creating by Dec 1)
- **Can Proceed:** December 1, 2025 (when docs ready)
- **Related:** Blocker (Template 13, Blockers & Dependencies)

#### Client A Development (Blocked Until Hire Complete)
- **Action:** Start Client A dashboard development
- **Owner:** Senior frontend developer (new hire)
- **Blocked By:** Need to hire senior frontend developer
- **Can Proceed:** January 13, 2026 (after hire starts Jan 6 + 1 week onboarding)
- **Related:** Blocker (Template 13, Blockers & Dependencies)

---

## Summary by Owner

### Olha Kizilova (ID: 178) - 10 Actions
- [ ] Design auth microservice API contract (Due: Nov 22) - **CRITICAL**
- [ ] Implement CI/CD pipeline optimizations (Due: Nov 22) - **HIGH**
- [ ] Build auth microservice (Due: Dec 6, Weeks 2-3) - **CRITICAL**
- [ ] Create API documentation for v2 (Due: Dec 1) - **CRITICAL**
- [ ] Create code review checklist (Due: Nov 22) - **HIGH**
- [ ] Host Docker best practices training (Due: Nov 22) - **MEDIUM**
- [ ] Update main API README (Due: Nov 25) - **MEDIUM**
- [ ] Technical interviews for senior frontend hire (Nov 25 - Dec 20) - **CRITICAL**
- [ ] Finalize senior frontend job description (Due: Nov 18) - **CRITICAL**
- [ ] Confirm Client A timeline is realistic (Due: Nov 18) - **HIGH**

### Anastasiya (Sales Manager) - 7 Actions
- [ ] Provision AWS ElastiCache Redis (Due: Nov 18) - **CRITICAL**
- [ ] Post senior frontend developer job ads (Due: Nov 18-25) - **CRITICAL**
- [ ] Post lead generator job ads (Due: Nov 18-25) - **HIGH**
- [ ] Finalize senior frontend job description (Due: Nov 18) - **CRITICAL**
- [ ] Send Client A timeline update email (Due: Nov 20) - **HIGH**
- [ ] Interview candidates (senior frontend: Nov 25-Dec 20, LG: Nov 25-Dec 6) - **CRITICAL**
- [ ] Announce new hires (when offers accepted) - **MEDIUM**

### Yaroslav Klimenko (ID: 86478) - 4 Actions
- [ ] Configure GitHub round-robin PR review assignment (Due: Nov 22) - **HIGH**
- [ ] Configure auth service CI/CD pipeline (Due: Nov 22) - **CRITICAL**
- [ ] Update deployment guide (Due: Nov 29) - **MEDIUM**
- [ ] Create developer onboarding guide (Due: Dec 15) - **CRITICAL**

### Hanan Zaheur (ID: 87984) - 5 Actions
- [ ] Set up Apollo.io usage monitoring (Due: Nov 18) - **MEDIUM**
- [ ] Complete LinkedIn Sales Navigator course (Due: Nov 22) - **MEDIUM**
- [ ] Build Q4 LinkedIn campaign target list (Due: Nov 22) - **HIGH**
- [ ] Update LG onboarding materials (Due: Dec 1) - **CRITICAL**
- [ ] Interview LG candidates (Nov 25-Dec 6) - **HIGH**

### Anastasiia (ID: 86981 - Design Lead) - 4 Actions
- [ ] Draft Figma file organization standard (Due: Nov 22) - **HIGH**
- [ ] Create design system documentation (Due: Dec 15) - **CRITICAL**
- [ ] Host Figma Auto Layout training (Due: Nov 22) - **MEDIUM**
- [ ] Announce mobile-first design standard (Due: Nov 18) - **MEDIUM**

### Nataliia Rybak (ID: 88054) - 1 Action
- [ ] Create campaign copy template library (Due: Nov 30) - **MEDIUM**

### Plamena Peneva (ID: 86297) - 2 Actions
- [ ] Configure Phantombuster workflows for Q4 campaign (Due: Nov 22) - **HIGH**
- [ ] Draft lead scoring criteria (Due: Nov 22) - **HIGH**

### Olha (ID: 86641 - Senior Designer) - 1 Action
- [ ] Audit Adobe CC license usage and cancel 3 seats (Due: Nov 30) - **MEDIUM**

---

## Critical Path Items

**These items block other work if not completed on time:**

1. **Provision Redis** (Anastasiya, Nov 18) → Blocks auth microservice development
2. **Design auth API contract** (Olha, Nov 22) → Blocks Week 2-3 development
3. **Post job ads** (Anastasiya, Nov 18-25) → Blocks hiring timeline (critical for Client A project)
4. **API v2 documentation** (Olha, Dec 1) → Blocks frontend integration
5. **Developer onboarding guide** (Yaroslav, Dec 15) → Blocks senior hire onboarding (Jan 6)
6. **LG onboarding materials** (Hanan, Dec 1) → Blocks new LG hire onboarding (Dec 9)
7. **Design system documentation** (Anastasiia, Dec 15) → Blocks design consistency improvements

---

## Follow-Up from Previous Meeting

**No previous meeting context provided** (this is a standalone meeting summary)

If this were a continuation:
- Review action items from previous meeting
- Mark completed items
- Escalate overdue items
- Carry over pending items
```

---

## Validation Checklist

- [ ] **All action items** from meeting captured
- [ ] **Owners** assigned with Employee IDs
- [ ] **Due dates** specified
- [ ] **Priorities** assessed
- [ ] **Dependencies** noted
- [ ] **Actions** linked to Responsibilities/Responsibilities/Actions library (ACT-XXX)
- [ ] **Summary by owner** complete
- [ ] **Critical path** identified
- [ ] **Blocked items** tracked
- [ ] **External dependencies** noted
- [ ] **Recurring items** documented
- [ ] **Meetings** scheduled

---

## Related Templates

**Previous:** [20_Onboarding_Training_Context.md](20_Onboarding_Training_Context.md) - Training
**First:** [01_Meeting_Metadata.md](01_Meeting_Metadata.md) - Meeting basics
**Core:** [03_Action_Items_Tasks.md](03_Action_Items_Tasks.md) - Detailed action items
**Reference:** All templates contribute to follow-up items

---

**Status:** ✅ Template ready for use
**Note:** This is the FINAL template (21 of 21) - Template suite complete!
