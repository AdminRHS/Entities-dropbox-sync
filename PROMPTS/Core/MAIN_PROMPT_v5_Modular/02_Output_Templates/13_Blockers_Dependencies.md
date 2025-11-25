# Template 13: Blockers & Dependencies

**Purpose:** Track blockers, dependencies, and items waiting on others
**Library Integration:** ⭐⭐ Medium (Actions, Processes for context)
**Priority:** Include when blockers or dependencies discussed

---

## Template

```markdown
## Blockers & Dependencies

**Active Blockers:** [Number]
**Dependencies Identified:** [Number]
**Waiting On:** [Number of external items]
**Resolved Blockers:** [Number]

### Critical Blockers

#### [Blocker Title]
- **Blocked Item:** [What is blocked - task, project, decision]
- **Blocked By:** [What/who is blocking]
- **Impact:**
  - **Who:** [Who is affected]
  - **What:** [What can't proceed]
  - **Timeline:** [How much delay this causes]
  - **Severity:** [Critical | High | Medium | Low]
- **First Blocked:** [When did this start]
- **Duration:** [How long has this been blocking]
- **Blocker Owner:** [Who can unblock this]
- **Resolution Plan:**
  - **Action:** [What needs to happen to unblock]
  - **Timeline:** [When will this be unblocked]
  - **Dependencies:** [What else is needed]
- **Workaround:** [Temporary solution if available]
- **Escalation:** [If not resolved by X date, escalate to Y]
- **Related:** [Links to tasks, processes, etc.]

### High Priority Blockers

[Same structure as Critical]

### Medium/Low Priority Blockers

[More concise format]

### Dependencies

#### [Item Name] depends on [Dependency]
- **Dependent Item:** [What needs something else]
- **Depends On:** [What it needs]
- **Dependency Owner:** [Who controls the dependency]
- **Needed By:** [Deadline for dependency]
- **Status:** [Blocker's status]
- **Risk:** [What happens if dependency not met]
- **Mitigation:** [Backup plan]

### Waiting On External

#### Waiting on [External Party/Item]
- **What We're Waiting For:** [Specific item]
- **From:** [External party - client, vendor, partner]
- **Requested:** [When we asked for this]
- **Expected:** [When we expect to receive]
- **Impact If Delayed:** [What happens if we don't get this]
- **Follow-up Plan:** [When/how to follow up]
- **Owner:** [Who is tracking this]

### Cross-Team Dependencies

[Dependencies between internal teams]

### Resolved Blockers

#### [Blocker Title] - RESOLVED
- **What Was Blocked:** [The issue]
- **How Resolved:** [What unblocked it]
- **Resolution Time:** [How long it took]
- **Resolved By:** [Who resolved it]
- **Lessons:** [What we learned]

### Blocker Prevention

[New processes or approaches to prevent future blockers]
```

---

## Recognition Rules

### Identifying Blockers

**Direct Blocker Language:**
- "Blocked by..."
- "Can't proceed until..."
- "Waiting on..."
- "Stuck on..."
- "This is preventing..."

**Dependency Language:**
- "Depends on..."
- "Needs X before..."
- "Requires..."
- "Won't work without..."

**External Waiting:**
- "Waiting for client..."
- "Vendor hasn't delivered..."
- "Need approval from..."
- "Expecting response from..."

**Timeline Impact:**
- "This is delaying..."
- "Can't meet deadline because..."
- "Timeline at risk due to..."

---

## Examples

### Example 1: Development Team Blockers

```markdown
## Blockers & Dependencies

**Active Blockers:** 3
**Dependencies Identified:** 4
**Waiting On:** 2 external items
**Resolved Blockers:** 1

### Critical Blockers

#### Frontend Development Blocked - No Senior React Developer
- **Blocked Item:** Client A dashboard project (high-value $25K contract)
- **Blocked By:** Missing senior React expertise on team (need to hire)
- **Impact:**
  - **Who:** Frontend development (Liliia can't handle complexity alone), Client A (waiting for project start)
  - **What:** Can't start Client A project (requires advanced React skills - real-time data, 10K+ data points, complex state management)
  - **Timeline:** Project delayed until hire complete (estimated 6 weeks: 4 weeks recruitment + 2 weeks onboarding)
  - **Severity:** Critical (client expects Q1 delivery; delay risk)
- **First Blocked:** November 15, 2025 (when project scoped and team realized skill gap)
- **Duration:** 0 days (just identified)
- **Blocker Owner:** Anastasiya (recruitment lead)
- **Resolution Plan:**
  - **Action:** Hire senior frontend developer (React specialist)
  - **Timeline:**
    - Nov 18-25: Post job ads, source candidates
    - Nov 25-Dec 20: Interview candidates (target 10-15 applications)
    - Dec 23: Make offer
    - Jan 6: Start date (2-week onboarding)
    - Jan 13: Unblocked (new hire productive, can start project)
  - **Dependencies:**
    - Job description approved (Anastasiya + Olha)
    - Budget approved ($3,000/month max - already confirmed)
    - Qualified candidates apply (market risk)
- **Workaround:** None (can't start complex React project without expertise; Liliia is junior, Yaroslav is backend-focused)
- **Escalation:** If can't find candidate by Dec 31 → Hire contractor for Client A project only (expensive backup plan)
- **Related:** Decision logged in [10_Decisions_Log.md]; Action item for Anastasiya (recruitment)

### High Priority Blockers

#### API Documentation Blocking Frontend Integration
- **Blocked Item:** Frontend development for v2 API integration
- **Blocked By:** API documentation missing (v2 endpoints not documented)
- **Impact:**
  - **Who:** Frontend developers (can't build against undocumented API)
  - **What:** Frontend integration work blocked (can't start until we know endpoint contracts)
  - **Timeline:** 2-week delay (frontend integration planned to start Dec 1; will slip to Dec 15 if docs not ready)
  - **Severity:** High (blocks planned work)
- **First Blocked:** November 15 (when frontend team asked for API docs)
- **Duration:** 0 days (just identified)
- **Blocker Owner:** Olha (backend developer building v2 API)
- **Resolution Plan:**
  - **Action:** Olha to create API documentation (Swagger/OpenAPI spec)
  - **Timeline:** Complete by December 1 (2 weeks)
  - **Dependencies:** v2 API development complete (mostly done, finalizing last 2 endpoints)
- **Workaround:** None (frontend can't proceed without knowing API contract)
- **Escalation:** Not needed (Olha committed to Dec 1 deadline; high confidence)
- **Related:** Documentation gap logged in [11_Documentation_Gaps.md]; Critical priority

#### CI/CD Pipeline Slow - Blocking Developer Productivity
- **Blocked Item:** Developer workflow efficiency (not a hard blocker, but significant productivity drain)
- **Blocked By:** Slow CI/CD pipeline (15-20 minutes per build)
- **Impact:**
  - **Who:** All developers (8 people × 3-5 PRs/day = 24-40 builds/day)
  - **What:** Developers wait 15-20 minutes per build (context switching, productivity loss)
  - **Timeline:** Cumulative: 6-13 hours/day of total developer waiting time (across team)
  - **Severity:** High (productivity impact, though not a hard blocker)
- **First Blocked:** Ongoing issue (worsening as codebase grows)
- **Duration:** ~3 months (pipeline used to be 8-10 min; now 15-20 min)
- **Blocker Owner:** Olha (will optimize CI/CD)
- **Resolution Plan:**
  - **Action:** Optimize CI/CD pipeline (caching, parallel tests, Docker optimization)
  - **Timeline:** Complete by November 22 (1 week)
  - **Dependencies:** None (Olha has capacity this week)
  - **Expected Impact:** Reduce 15-20 min → 6-8 min (60-70% improvement)
- **Workaround:** Developers work on multiple branches simultaneously (inefficient, increases context switching)
- **Escalation:** Not needed
- **Related:** Problem documented in [07_Problems_Solutions.md]; High priority fix

### Medium/Low Priority Blockers

#### Design Handoff Delayed - Waiting for Client Feedback (Medium)
- **Blocked Item:** Final design delivery to developer
- **Blocked By:** Client hasn't provided feedback (requested 5 days ago, 48-hour SLA)
- **Impact:** Designer can't finalize design; developer waiting to start build
- **Blocker Owner:** Client (external)
- **Resolution Plan:** Send reminder email today; escalate to client stakeholder if no response in 24 hours
- **Timeline:** Expected resolution: 1-2 days

### Dependencies

#### Auth Service Deployment depends on Redis Infrastructure
- **Dependent Item:** Auth microservice deployment (production launch)
- **Depends On:** AWS ElastiCache Redis cluster provisioned and configured
- **Dependency Owner:** Anastasiya (has AWS access to provision infrastructure)
- **Needed By:** December 9 (auth service ready for staging deployment Week 4)
- **Status:** Not started (need to provision Redis cluster)
- **Risk:** If Redis not ready by Dec 9, auth service deployment delayed by 1 week
- **Mitigation:** Provision Redis early (Week 1: Nov 18-22) to avoid last-minute issues
- **Plan:**
  - Nov 18: Anastasiya provisions ElastiCache cluster (1-2 hours)
  - Nov 19: Olha configures auth service to connect to Redis (test connection)
  - Week 2-3: Auth service development continues (using Redis)
  - Dec 9: Ready for staging deployment

#### Frontend Integration depends on API Documentation
- **Dependent Item:** Frontend v2 API integration development
- **Depends On:** API documentation complete (Swagger spec, migration guide)
- **Dependency Owner:** Olha (creating docs)
- **Needed By:** December 1 (frontend integration starts)
- **Status:** In progress (Olha committed to Dec 1 deadline)
- **Risk:** If docs delayed, frontend integration delayed (pushes production deployment)
- **Mitigation:** Olha prioritizing docs (Week 2-3 focus); high confidence in Dec 1 delivery

#### New Frontend Hire depends on Candidate Acceptance
- **Dependent Item:** Client A project start
- **Depends On:** Senior frontend developer hire (candidate accepts offer)
- **Dependency Owner:** Anastasiya (recruitment) + Candidate decision
- **Needed By:** January 6 (project start date)
- **Status:** Recruitment in progress (job posting going live this week)
- **Risk:** If can't hire by Jan 6, Client A project delayed (client expects Q1 delivery)
- **Mitigation:**
  - Cast wide net (5 job boards, leverage network)
  - Competitive offer ($2,500-3,000/month)
  - Fast recruitment process (minimize candidate drop-off)
  - Backup plan: Hire contractor if can't find full-time by Dec 31

#### Mobile-First Designs depend on Team Training
- **Dependent Item:** All designers successfully using mobile-first approach
- **Depends On:** Team familiarity with mobile-first methodology (some designers never designed mobile-first)
- **Dependency Owner:** Anastasiia (will provide training/examples)
- **Needed By:** Immediately (new standard effective Nov 18)
- **Status:** Training planned (Anastasiia will share examples, answer questions)
- **Risk:** Low (designers are skilled; this is workflow change, not new skill)
- **Mitigation:** Anastasiia available for questions; will review first mobile-first projects

### Waiting On External

#### Waiting on Client A - Requirements Finalization
- **What We're Waiting For:** Final requirements document (dashboard features, data sources, user roles)
- **From:** Client A (external client)
- **Requested:** November 10 (sent requirements gathering questionnaire)
- **Expected:** November 20 (client said "by end of next week")
- **Impact If Delayed:** Can't finalize project plan or architecture (requirements needed before development)
- **Follow-up Plan:**
  - Nov 20: If not received, send reminder email
  - Nov 22: If still not received, schedule call with client stakeholder
  - Nov 25: If still not received, escalate (flag risk to project timeline)
- **Owner:** Anastasiya (client relationship owner)
- **Note:** Not a hard blocker yet (hire is happening in parallel; by Jan 6 start date, requirements will likely be ready)

#### Waiting on Apollo.io - Account Upgrade Confirmation
- **What We're Waiting For:** Email confirmation that Apollo.io upgrade is complete (5K → 10K exports/month)
- **From:** Apollo.io (vendor)
- **Requested:** During meeting (Nov 15, Hanan upgraded plan via website)
- **Expected:** Within 24 hours (automatic, should be instant)
- **Impact If Delayed:** LG team can't confirm new limit until confirmation received (but Hanan reports access already increased)
- **Follow-up Plan:** Hanan to check Apollo dashboard; if limit not increased by Nov 16, contact Apollo support
- **Owner:** Hanan
- **Update:** RESOLVED (Hanan confirmed upgrade during meeting; access confirmed)

### Cross-Team Dependencies

#### Design Team → Dev Team: Figma Designs Ready Before Sprint Start
- **Dependency:** Dev team depends on designs being finalized before sprint starts (can't build without designs)
- **Current Process:** Designs sometimes not ready; developers wait or work on other tasks
- **Impact:** Sprint planning disrupted; velocity reduced
- **Proposed Solution:** Design and dev sprint planning aligned (design sprint finishes 3 days before dev sprint starts)
- **Owner:** Anastasiia (design) + Olha (dev) to align sprint schedules
- **Timeline:** Implement starting next sprint (Dec 2)

#### LG Team → Sales Team: Lead Lists Ready Before Outreach Campaign
- **Dependency:** Sales team depends on LG team delivering lead lists on time (can't run campaigns without lists)
- **Current Process:** Works well (LG team delivers 5-7 day turnaround; sales plans accordingly)
- **Note:** No current blocker (dependency managed well)

### Resolved Blockers

#### Apollo.io Export Limit - RESOLVED
- **What Was Blocked:** LG team couldn't build more lead lists (monthly export limit reached mid-month)
- **How Resolved:** Upgraded Apollo plan (5,000 → 10,000 exports/month); immediate access
- **Resolution Time:** <1 hour (identified in meeting, upgraded immediately, confirmed during meeting)
- **Resolved By:** Anastasiya (approved budget), Hanan (processed upgrade)
- **Lessons:**
  - **Lesson 1:** Proactive monitoring would have prevented mid-month crisis (LG team should track Apollo usage weekly)
  - **Lesson 2:** Upgrade process is fast (good vendor responsiveness)
  - **Action:** Hanan to track Apollo usage monthly; notify team at 70% capacity (7,000 exports used)

### Blocker Prevention

**New Process: Weekly Blocker Review in Standups**
- **Purpose:** Identify blockers early (before they become critical)
- **Implementation:** Each team's weekly standup includes "Blockers?" question
- **Owner:** Team leads (Anastasiia for design, Olha for dev, Hanan for LG)
- **Timeline:** Starting next week

**New Process: Dependency Mapping in Sprint Planning**
- **Purpose:** Identify dependencies during sprint planning (not mid-sprint)
- **Implementation:** Dev team sprint planning includes "Dependencies?" checklist
  - Does this work depend on other teams?
  - Does this work depend on external parties?
  - Does this work depend on infrastructure?
- **Owner:** Olha (dev lead)
- **Timeline:** Starting next sprint (Dec 2)

**New Metric: Time-to-Unblock**
- **Purpose:** Track how long blockers remain unresolved (measure improvement)
- **Metric:** Average days from blocker identified → blocker resolved
- **Target:** <3 days for high-priority blockers
- **Owner:** Anastasiya (tracks across all teams)
- **Timeline:** Start tracking December
```

---

## Validation Checklist

- [ ] **All blockers** identified and documented
- [ ] **Severity** assessed for each blocker
- [ ] **Impact** clearly described (who, what, timeline)
- [ ] **Blocker owners** assigned
- [ ] **Resolution plans** detailed
- [ ] **Workarounds** noted if available
- [ ] **Escalation plans** defined
- [ ] **Dependencies** mapped
- [ ] **External waiting items** tracked
- [ ] **Cross-team dependencies** identified
- [ ] **Resolved blockers** documented with lessons
- [ ] **Prevention measures** proposed
- [ ] **Timelines** realistic and tracked

---

## Related Templates

**Previous:** [12_Communication_Announcements.md](12_Communication_Announcements.md) - Communications
**Next:** [14_Insights_Lessons.md](14_Insights_Lessons.md) - Learning insights
**Related:** [07_Problems_Solutions.md](07_Problems_Solutions.md) - Problems often cause blockers

---

**Status:** ✅ Template ready for use
