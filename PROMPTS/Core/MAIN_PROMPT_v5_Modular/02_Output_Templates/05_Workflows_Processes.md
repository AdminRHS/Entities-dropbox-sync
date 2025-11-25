# Template 05: Workflows & Processes

**Purpose:** Document workflows and process discussions
**Library Integration:** ⭐⭐⭐ Heavy (Processes, Results)
**Priority:** Include when workflows or processes discussed

---

## Template

```markdown
## Workflows & Processes

**Processes Discussed:** [Number]
**Process Status Updates:** [Number]

### Active Workflows

#### [Process Name] (ID: PROC-XXX-XXX)
- **Process Type:** [Workflow | Standard Operating Procedure | Checklist | Framework]
- **Department:** [Which department owns this process]
- **Current Status:** [Planning | In Use | Being Updated | Deprecated]
- **Participants:** [Who executes this process]
- **Discussion Points:**
  - [What was discussed about this process]
- **Changes Proposed:** [Any modifications suggested]
- **Expected Results:** [RES-XXX] - [Result name from Results library]
- **Success Metrics:** [How to measure process success]

### Process Improvements

[Improvements or optimizations discussed]

### New Processes Proposed

[New workflows suggested or designed]

### Process Issues/Blockers

[Problems with current processes]
```

---

## Recognition Rules

### Identifying Process Discussions

**Direct Process Mentions:**
- "Following the UI/UX design process"
- "Using our lead gen workflow"
- "According to the development process"

**Process Descriptions:**
- "First we do X, then Y, then Z" (workflow steps)
- "Our standard approach is..." (SOP)
- "The checklist includes..." (procedure)

**Process Status:**
- "The process is working well"
- "We need to update the workflow"
- "This step is inefficient"

### Matching to Processes Library

**Total Processes:** 428
**Source:** Processes_Master.json + Workflow files

**Common Processes:**
- PROC-DESIGN-001: UI/UX Design Process
- PROC-DEV-001: Feature Development Workflow
- PROC-LG-001: B2B Lead List Building
- PROC-RECRUIT-001: Full Recruitment Cycle
- PROC-VID-001: Full Video Production Workflow
- PROC-SALES-001: Sales Pipeline Management

**Reference:** Department library files for process details

### Results Integration

**Every process should have expected results:**
- Design process → High-quality designs delivered
- Development process → Feature deployed successfully
- Lead gen process → Qualified leads delivered
- Recruitment process → Position filled

**Results Library:** 432 results
**Format:** RES-XXX or RESULT-XXX

---

## Examples

### Example 1: Design Team - Process Discussion

```markdown
## Workflows & Processes

**Processes Discussed:** 2
**Process Status Updates:** 1

### Active Workflows

#### UI/UX Design Process (ID: PROC-DESIGN-001)
- **Process Type:** Workflow (6-step process)
- **Department:** Design
- **Current Status:** In Use (with proposed improvements)
- **Participants:** All UI/UX designers (Olha, Anastasiia, Iuliia K.)
- **Discussion Points:**
  - Current process works well but wireframing phase taking too long
  - Client feedback loop needs to be faster (currently 2-3 days)
  - Design system usage should be enforced earlier in process
  - Mobile-first approach not consistently applied
- **Changes Proposed:**
  - Add design system checkpoint before high-fidelity mockups
  - Reduce client feedback turnaround to 24 hours (set expectation)
  - Start all projects with mobile wireframes, then scale up
- **Expected Results:**
  - RESULT-DES-001: High-quality designs delivered
  - RESULT-DES-002: Client satisfaction achieved
  - RESULT-DES-003: On-time delivery
- **Success Metrics:**
  - Design quality: 8/10 minimum
  - Client approval: First or second round
  - Timeline adherence: 90%+

#### Design System Workflows (ID: PROC-DESIGN-003)
- **Process Type:** Standard Operating Procedure
- **Department:** Design
- **Current Status:** Being Updated
- **Participants:** All designers (focus: Anastasiia as maintainer)
- **Discussion Points:**
  - Design system update process needs documentation
  - When to update components vs when to create new ones (unclear)
  - How to notify team of updates (currently ad-hoc)
  - Version control for design system changes
- **Changes Proposed:**
  - Document component update workflow
  - Weekly design system sync (15 min standup)
  - Slack notification channel for updates
  - Version numbering for major changes
- **Expected Results:**
  - RESULT-DES-004: Consistent design across projects
  - RESULT-DES-005: Design system adopted by all
- **Success Metrics:**
  - Component usage: 100% of projects use design system
  - Update notifications: All team members aware within 24 hours

### Process Improvements

**Client Feedback Loop:**
- **Current:** Email feedback, 2-3 day response time
- **Proposed:** Frame.io for faster async feedback, 24-hour target
- **Owner:** Olha to test with next client project
- **Expected Impact:** 50% faster iteration cycles

**Mobile-First Design:**
- **Current:** Desktop designs first, mobile adapted later
- **Proposed:** Start with mobile wireframes (375px), scale up to desktop
- **Owner:** All designers adopt starting next project
- **Expected Impact:** Better mobile experiences, less rework

### New Processes Proposed

**Dribbble Posting Workflow:**
- **Purpose:** Systematize portfolio posting (currently inconsistent)
- **Steps Proposed:**
  1. Select best work from completed projects (quality threshold: 9/10)
  2. Create shot description and tags (Friday)
  3. Post Tuesday/Thursday (optimal engagement times)
  4. Cross-post to Behance (same content)
- **Owner:** Rotating weekly (schedule created)
- **Expected Result:** Consistent portfolio presence, 8 shots/month

### Process Issues/Blockers

**Figma File Organization:**
- **Issue:** No consistent naming or folder structure
- **Impact:** Hard to find files, duplicate work
- **Solution Discussed:** Create file organization standard
- **Next Steps:** Draft standard by next meeting (Owner: Anastasiia)
```

---

### Example 2: Development Team - Process Updates

```markdown
## Workflows & Processes

**Processes Discussed:** 3
**Process Status Updates:** 2

### Active Workflows

#### Feature Development Workflow (ID: PROC-DEV-001)
- **Process Type:** Workflow (7-step process)
- **Department:** Dev
- **Current Status:** In Use (working well)
- **Participants:** All developers (Yaroslav, Olha, Liliia)
- **Discussion Points:**
  - Process generally working well
  - Code review step sometimes delayed (24-hour target not always met)
  - Testing phase needs more time allocated
  - Deployment to staging occasionally skipped (bad practice)
- **Changes Proposed:**
  - Enforce code review SLA: 24 hours or escalate
  - Add testing time to sprint estimates (+20%)
  - Make staging deployment mandatory (add to PR checklist)
- **Expected Results:**
  - RESULT-DEV-001: Feature deployed successfully
  - RESULT-DEV-002: High code quality maintained
  - RESULT-DEV-003: Low production bug rate
- **Success Metrics:**
  - Code review: <24 hours, 100% reviewed
  - Test coverage: >80%
  - Production bugs: <2 per sprint

#### Code Review Process (ID: PROC-DEV-003)
- **Process Type:** Standard Operating Procedure
- **Department:** Dev
- **Current Status:** In Use (being formalized)
- **Participants:** All developers (peer review)
- **Discussion Points:**
  - Currently informal; need checklist
  - Security vulnerabilities sometimes missed
  - Inconsistent review depth
  - Good practice: Yaroslav's thorough reviews (example to follow)
- **Changes Proposed:**
  - Create code review checklist (8-10 items)
  - Security review section (OWASP top 10)
  - Require 2 reviewers for backend changes
  - Add review completion to sprint metrics
- **Expected Results:**
  - RESULT-DEV-002: High code quality
  - RESULT-DEV-004: Security vulnerabilities prevented
- **Success Metrics:**
  - Review completion: 100% before merge
  - Security issues: 0 in production
  - Review turnaround: <24 hours

#### CI/CD Pipeline (ID: PROC-DEV-004)
- **Process Type:** Automated Workflow
- **Department:** Dev
- **Current Status:** In Use (needs optimization)
- **Participants:** Automated (GitHub Actions), monitored by dev team
- **Discussion Points:**
  - Pipeline sometimes slow (15+ minutes for builds)
  - Test failures occasionally ignored (bad practice)
  - Production deployment process unclear (manual steps)
- **Changes Proposed:**
  - Optimize build process (parallel jobs, caching)
  - Block merge on test failures (enforce)
  - Document production deployment steps
- **Expected Results:**
  - RESULT-DEV-005: Fast, reliable deployments
  - RESULT-DEV-006: Automated quality gates
- **Success Metrics:**
  - Build time: <10 minutes
  - Test pass rate: 100% required for merge
  - Deployment success rate: >95%

### Process Improvements

**Code Review Checklist (Draft):**
1. ✅ Code follows style guide (ESLint passing)
2. ✅ Logic is sound and efficient
3. ✅ No security vulnerabilities (OWASP check)
4. ✅ Tests included and passing (>80% coverage)
5. ✅ Edge cases handled
6. ✅ Documentation updated
7. ✅ No debug code (console.log removed)
8. ✅ Responsive design works (if frontend)

**Next Steps:** Formalize checklist, add to PR template

### New Processes Proposed

**Bug Triage Process:**
- **Purpose:** Standardize bug handling (currently ad-hoc)
- **Steps Proposed:**
  1. Bug reported (GitHub issue)
  2. Triage: Assess severity (Critical/High/Medium/Low)
  3. Assign priority and owner
  4. Fix within SLA (Critical: same day, High: 1-2 days, Medium: 3-5 days, Low: next sprint)
  5. Test fix
  6. Deploy
  7. Verify resolved
- **Owner:** Olha to draft full process
- **Expected Result:** RESULT-DEV-007: Bugs resolved within SLA

### Process Issues/Blockers

**Deployment Documentation:**
- **Issue:** Production deployment steps not documented
- **Impact:** Only Olha knows full process (bus factor)
- **Solution Discussed:** Document step-by-step deployment guide
- **Owner:** Olha to write documentation by next week
```

---

### Example 3: LG Team - Lead Gen Workflows

```markdown
## Workflows & Processes

**Processes Discussed:** 3
**Process Status Updates:** 2

### Active Workflows

#### B2B Lead List Building (ID: PROC-LG-001)
- **Process Type:** Workflow (7-step process, 5-7 days)
- **Department:** LG
- **Current Status:** In Use (highly optimized)
- **Participants:** All lead generators
- **Discussion Points:**
  - Process working very well (96% deliverability achieved)
  - Data quality improved from 88% to 92% last quarter
  - Enrichment step is bottleneck (slowest part)
  - Apollo.io + Hunter.io combination effective
- **Changes Proposed:**
  - Increase enrichment rate target: 60% → 65%
  - Add Clearbit for company data enrichment (test)
  - Automate duplicate removal (currently manual - 2 hours/list)
- **Expected Results:**
  - RESULT-LG-001: Lead list delivered (500-1000 qualified leads)
  - RESULT-LG-005: Data quality certified (>90% accuracy)
- **Success Metrics:**
  - Data accuracy: >92% (new target)
  - Email deliverability: >95%
  - Delivery time: 5-7 days (maintain)

#### Email Outreach Campaign (ID: PROC-LG-003)
- **Process Type:** Workflow (5-step process, 2-4 weeks)
- **Department:** LG
- **Current Status:** In Use (recently optimized)
- **Participants:** Lead generators + content manager (Nataliia)
- **Discussion Points:**
  - October campaign success (35% open, 4.2% reply)
  - Personalization increased response by 40% (key learning)
  - Warm-up phase critical for new email accounts
  - A/B testing subject lines improved opens by 12%
- **Changes Proposed:**
  - Mandatory personalization: Name + Company minimum
  - Extend warm-up period: 2 weeks → 3 weeks for new accounts
  - A/B test every campaign (2-3 subject line variants)
- **Expected Results:**
  - RESULT-LG-003: Meetings booked (1-2% of list)
  - RESULT-LG-004: High response rate (>5%)
- **Success Metrics:**
  - Deliverability: >95%
  - Open rate: 30-40%
  - Reply rate: 3-5% (target: >5% with new changes)

#### LinkedIn Lead Generation Campaign (ID: PROC-LG-002)
- **Process Type:** Workflow (ongoing, monthly)
- **Department:** LG
- **Current Status:** Planning → Launch Next Week
- **Participants:** Hanan (list building), Nataliia (copy), Plamena (execution)
- **Discussion Points:**
  - First time running this process at scale
  - Based on successful small tests (20-30% acceptance rate)
  - Need to document process for future campaigns
  - LinkedIn ToS considerations (no aggressive automation)
- **Changes Proposed:**
  - Document full process after first campaign completes
  - Stay within LinkedIn limits (20-30 connections/day)
  - Personalize connection requests (not generic)
- **Expected Results:**
  - RESULT-LG-006: Campaign success (KPIs met)
  - RESULT-LG-003: Meetings booked (5-10 per month)
- **Success Metrics:**
  - Connection acceptance: 30-40%
  - Response rate: 10-15%
  - Meetings booked: 5-10/month

### Process Improvements

**Data Quality Automation:**
- **Current:** Manual duplicate removal (Excel, 2 hours per list)
- **Proposed:** Python script to auto-remove duplicates + normalize data
- **Owner:** Isaac (has prompt engineering skills, can automate)
- **Expected Impact:** Save 2 hours per list, reduce errors

**Campaign Copy Process:**
- **Current:** Nataliia writes all copy (bottleneck)
- **Proposed:** Template library + AI assistance for personalization
- **Owner:** Nataliia to create template library
- **Expected Impact:** 50% faster copy creation, consistent quality

### New Processes Proposed

**Lead Scoring Process:**
- **Purpose:** Prioritize highest-quality leads (not all leads equal)
- **Steps Proposed:**
  1. Apply scoring criteria (company size, industry, title, engagement)
  2. Score 1-10 scale
  3. Segment: Hot (8-10), Warm (5-7), Cold (1-4)
  4. Prioritize outreach to Hot leads
- **Owner:** Plamena to draft scoring criteria
- **Expected Result:** Higher meeting booking rate (prioritize best leads)

### Process Issues/Blockers

**Apollo.io Rate Limits:**
- **Issue:** Monthly export limit reached mid-month
- **Impact:** Cannot build more lists until next month
- **Solution Discussed:** Upgrade Apollo plan or supplement with LinkedIn Sales Navigator
- **Decision:** Upgrade Apollo to higher tier (approved by Anastasiya)
```

---

## Validation Checklist

- [ ] **All processes mentioned** captured
- [ ] **Process IDs** match Processes library
- [ ] **Process type** identified (Workflow/SOP/Checklist/Framework)
- [ ] **Department ownership** clear
- [ ] **Current status** accurate
- [ ] **Participants** listed
- [ ] **Discussion points** summarized
- [ ] **Changes proposed** documented
- [ ] **Expected results** linked to Results library (RES-XXX)
- [ ] **Success metrics** defined
- [ ] **Process improvements** captured
- [ ] **New processes** documented if proposed
- [ ] **Issues/blockers** noted

---

## Related Templates

**Previous:** [04_Projects_Features.md](04_Projects_Features.md) - Project context
**Next:** [06_Rules_Best_Practices.md](06_Rules_Best_Practices.md) - Standards
**Libraries:** Department library files for process details
**Reference:** [../03_Processing_Rules/](../03_Processing_Rules/) - Recognition rules

---

**Status:** ✅ Template ready for use
