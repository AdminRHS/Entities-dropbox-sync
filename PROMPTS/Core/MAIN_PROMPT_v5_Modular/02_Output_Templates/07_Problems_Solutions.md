# Template 07: Problems & Solutions

**Purpose:** Document problems discussed and solutions proposed/implemented
**Library Integration:** ⭐⭐ Medium (Actions, Processes, Results)
**Priority:** Include when problems or challenges discussed

---

## Template

```markdown
## Problems & Solutions

**Problems Discussed:** [Number]
**Solutions Proposed:** [Number]
**Solutions Implemented:** [Number]
**Open Issues:** [Number]

### Critical Issues

#### [Problem Title] - [Department]
- **Severity:** [Critical | High | Medium | Low]
- **Status:** [Open | In Progress | Resolved]
- **Impact:** [Who/what is affected]
- **Description:** [What the problem is - 2-3 sentences]
- **Root Cause:** [Why this problem exists]
- **First Identified:** [When was this discovered]
- **Current Workaround:** [Temporary solution if any]
- **Proposed Solution:**
  - [Solution option 1]
  - [Solution option 2 if multiple discussed]
- **Chosen Solution:** [Which solution was selected]
- **Implementation Plan:**
  - Action: [ACT-XXX] - [Action from Responsibilities/Responsibilities/Actions library]
  - Owner: [Who will fix this]
  - Timeline: [When will this be fixed]
  - Resources Needed: [What's required]
- **Success Criteria:** [How to know it's resolved]
- **Related Items:**
  - Process: [PROC-XXX if process-related]
  - Expected Result: [RES-XXX what should happen after fix]

### High Priority Issues

[Same structure as Critical Issues]

### Medium/Low Priority Issues

[Same structure but can be more concise]

### Resolved in Meeting

#### [Problem Title] - [Department]
- **Problem:** [What the issue was]
- **Solution Implemented:** [How it was solved]
- **Outcome:** [Result of the solution]
- **Who Fixed:** [Name]

### Recurring Problems

[Problems that keep coming up; need systematic solution]

### Preventive Measures

[New processes or standards to prevent future problems]

### Lessons Learned

[What the team learned from solving these problems]
```

---

## Recognition Rules

### Identifying Problems

**Direct Problem Statements:**
- "We have a problem with..."
- "The issue is..."
- "I'm stuck on..."
- "This isn't working..."

**Complaint Patterns:**
- "This is taking too long"
- "This keeps breaking"
- "We keep having to redo..."
- "I can't figure out how to..."

**Blocker Identification:**
- "I'm blocked by..."
- "We can't proceed until..."
- "Waiting on..."
- "This is preventing us from..."

**Performance Issues:**
- "This is too slow"
- "Quality isn't good enough"
- "Missing the target"
- "Below standard"

### Identifying Solutions

**Proposed Solutions:**
- "We could..."
- "What if we..."
- "I suggest..."
- "The solution is to..."

**Decision on Solutions:**
- "Let's do..."
- "We'll implement..."
- "Going forward, we'll..."
- "Approved to proceed with..."

**Implementation Plans:**
- "I'll fix this by..."
- "Steps: First X, then Y"
- "Timeline: complete by Friday"

### Problem Severity Assessment

**Critical:** Production down, security breach, client deliverable blocked, revenue impacted
**High:** Significant workflow disruption, quality issues affecting deliverables, timeline at risk
**Medium:** Inefficiency, minor quality issues, frustration but workarounds exist
**Low:** Nice-to-have improvements, minor annoyances, optimization opportunities

---

## Examples

### Example 1: Development Team - Production Bug

```markdown
## Problems & Solutions

**Problems Discussed:** 3
**Solutions Proposed:** 5
**Solutions Implemented:** 1
**Open Issues:** 2

### Critical Issues

#### Authentication API Failure - Dev Department
- **Severity:** Critical (production outage)
- **Status:** In Progress → Resolved
- **Impact:** All users unable to log in (100% user impact); production down since yesterday 3 PM
- **Description:** Users attempting to log in receive "500 Internal Server Error." API endpoint `/auth/login` is failing with database connection timeout. Approximately 200+ users affected based on support tickets.
- **Root Cause:** Database connection pool exhausted due to unclosed connections in recent deployment (bug introduced in v2.3.1 release)
- **First Identified:** Yesterday 3:15 PM (user reports + monitoring alert)
- **Current Workaround:** Restarting API server every 2 hours to clear connection pool (temporary, not sustainable)
- **Proposed Solution:**
  - **Option 1:** Rollback to v2.3.0 (stable version) - Fast but loses new features
  - **Option 2:** Hotfix v2.3.2 (fix connection leak) - Takes 2-4 hours but preserves features
- **Chosen Solution:** Implement hotfix v2.3.2 (Option 2)
  - **Rationale:** New features are important for client demo tomorrow; rollback would require rescheduling demo
- **Implementation Plan:**
  - Action: ACT-DEV-004 - Fix bug (authentication connection leak)
  - Owner: Olha Kizilova (ID: 178) - Backend Developer
  - Timeline: Hotfix deployed within 4 hours (by 3 PM today)
  - Resources Needed: Olha full-time until resolved; Yaroslav available for testing
  - **Steps:**
    1. Reproduce bug locally (completed - confirmed connection leak)
    2. Fix code: Add proper connection closure in auth middleware
    3. Write test to prevent regression
    4. Deploy to staging
    5. Test thoroughly (30 minutes)
    6. Deploy to production
    7. Monitor for 2 hours
- **Success Criteria:**
  - Users can log in successfully
  - No 500 errors in logs
  - Database connection pool stable (<50% usage)
  - Monitor for 24 hours with no issues
- **Related Items:**
  - Process: PROC-DEV-001 (Feature Development Workflow) - Will add "connection leak check" to review checklist
  - Expected Result: RES-DEV-001 (Feature deployed successfully) - This violated the result; need to prevent recurrence

**Update:** ✅ **RESOLVED** (3:00 PM today)
- Hotfix v2.3.2 deployed successfully
- Users can log in; no errors in last 2 hours
- Database connection pool at 35% usage (healthy)
- Monitoring continues

### High Priority Issues

#### Slow CI/CD Pipeline Build Times - Dev Department
- **Severity:** High (productivity impact)
- **Status:** Open
- **Impact:** All developers blocked 15+ minutes per PR; 3-5 PRs/day = 45-75 minutes wasted daily per developer
- **Description:** CI/CD pipeline taking 15-20 minutes to complete (build + tests). Industry standard is <10 minutes. Developers frequently context-switching while waiting, reducing productivity.
- **Root Cause:**
  - No build caching (rebuilds dependencies every time)
  - Tests run sequentially (not parallelized)
  - Docker image built from scratch each time
- **First Identified:** Last month; worsening as codebase grows
- **Current Workaround:** Developers work on multiple branches simultaneously (context switching inefficiency)
- **Proposed Solution:**
  - **Option 1:** Implement build caching (estimate: 30% faster → 10-12 min)
  - **Option 2:** Parallelize test execution (estimate: 40% faster → 9-10 min)
  - **Option 3:** Both caching + parallelization (estimate: 60% faster → 6-8 min)
- **Chosen Solution:** Option 3 (both caching + parallelization)
  - **Rationale:** Maximize impact; worth the extra implementation effort
- **Implementation Plan:**
  - Action: ACT-DEV-009 - Optimize code/process
  - Owner: Olha Kizilova (ID: 178) - Backend Developer
  - Timeline: Implement next week (after hotfix complete); target completion Nov 22
  - Resources Needed: 4-6 hours development time; test across all repos
  - **Steps:**
    1. Research GitHub Actions caching best practices
    2. Implement dependency caching
    3. Configure parallel test execution (split test suite into 4 jobs)
    4. Optimize Docker image (use multi-stage builds)
    5. Test on sample repo
    6. Roll out to all repos
- **Success Criteria:**
  - Build time reduced to <10 minutes (target: 6-8 min)
  - No test failures introduced by parallelization
  - Developer feedback: "Noticeably faster"
- **Related Items:**
  - Process: PROC-DEV-004 (CI/CD Pipeline) - Will update process docs after optimization
  - Expected Result: RES-DEV-005 (Fast, reliable deployments)

#### Code Review Bottleneck - Dev Department
- **Severity:** High (workflow disruption)
- **Status:** Open
- **Impact:** 5 PRs from last sprint exceeded 24-hour review SLA; developers blocked waiting for reviews
- **Description:** Code reviews taking >24 hours (target: <24 hours). Reviewers are overloaded; same people reviewing all PRs. Sprint velocity reduced by ~15% due to blocked work.
- **Root Cause:**
  - Uneven review distribution (Olha reviewing 70% of PRs)
  - No clear reviewer assignment process
  - Reviews not prioritized (treated as "when I have time")
- **First Identified:** Last two sprints (pattern emerging)
- **Current Workaround:** Developers ping reviewers on Slack (reactive, inefficient)
- **Proposed Solution:**
  - **Option 1:** Implement round-robin review assignment (GitHub automation)
  - **Option 2:** Add "Code Review" as sprint task (allocate 2-4 hours/week per developer)
  - **Option 3:** Both round-robin + dedicated review time
- **Chosen Solution:** Option 3 (round-robin + dedicated time)
  - **Rationale:** Process + culture change needed
- **Implementation Plan:**
  - Action: ACT-DEV-008 - Review code (systematize process)
  - Owner: Yaroslav Klimenko (ID: 86478) - Will set up GitHub automation
  - Timeline: Implement this week; monitor for 2 sprints
  - Resources Needed:
    - GitHub Actions configuration (1 hour)
    - Team agreement to dedicate review time (sprint planning)
  - **Steps:**
    1. Configure GitHub to auto-assign reviewers (round-robin)
    2. Add "Code Review" task to sprint (2-4 hours per developer)
    3. Set Slack reminder if PR >18 hours without review (escalation)
    4. Track review metrics (turnaround time, distribution)
- **Success Criteria:**
  - 90% of PRs reviewed within 24 hours
  - Review distribution balanced (no one person >40% of reviews)
  - Developer feedback: "PRs no longer blocking me"
- **Related Items:**
  - Process: PROC-DEV-003 (Code Review Process) - Update with round-robin assignment
  - Expected Result: RES-DEV-002 (High code quality maintained) - Reviews must be thorough AND timely

### Medium/Low Priority Issues

#### Figma File Disorganization - Design Department (Medium)
- **Problem:** Figma workspace has inconsistent file naming; hard to find files
- **Impact:** Designers waste 5-10 minutes daily searching for files; duplicate work created
- **Solution:** Create and enforce file naming standard: `[Client Name] - [Project Type] - [Date YYYY-MM]`
- **Owner:** Anastasiia (ID: 86981) to draft standard by next meeting
- **Timeline:** Implement next week

#### Outdated Documentation - Dev Department (Low)
- **Problem:** API documentation outdated (new endpoints added last week not documented)
- **Impact:** Frontend developers confused; asking backend team repeatedly
- **Solution:** Update docs; add "Documentation updated?" to PR checklist
- **Owner:** Olha (ID: 178) to update docs by Nov 25
- **Timeline:** Next week (low priority)

### Resolved in Meeting

#### Client Feedback Delays - Design Department
- **Problem:** Recent project stalled 8 days waiting for client feedback (target: 48 hours)
- **Solution Implemented:**
  - Set expectation at project kickoff: "Please provide feedback within 48 hours"
  - Send reminder email if feedback overdue at 36 hours
  - Escalate to project manager if >72 hours (discuss timeline impact with client)
- **Outcome:** Team agreed to implement immediately; Olha will test on next client project
- **Who Fixed:** Process change (all designers will adopt)

#### Apollo.io Rate Limit Blocking Lead Lists - LG Department
- **Problem:** Apollo monthly export limit reached mid-month (can't build more client lists)
- **Solution Implemented:** Upgrade Apollo plan from 5,000/month to 10,000/month
- **Outcome:** Approved by Anastasiya (sales manager); upgraded immediately
- **Who Fixed:** Anastasiya processed upgrade; Hanan confirmed access increased
- **Cost:** Additional $100/month (approved from LG budget)

### Recurring Problems

#### Last-Minute Client Changes (Design)
- **Pattern:** Clients frequently request major changes late in project (after 80-90% complete)
- **Impact:** Timeline delays, designer frustration, unpaid rework
- **Discussion:** This is a sales/scoping issue, not design issue
- **Root Cause:** Unclear scope at project start; clients don't fully understand what they're approving
- **Proposed Long-Term Solution:**
  - Sales team: Implement detailed discovery call checklist
  - Design team: More frequent check-ins during project (weekly, not just at milestones)
  - Contract: Define revision rounds clearly (max 3 rounds per phase)
- **Owner:** Anastasiya (sales) + Olha (design lead) to collaborate on solution
- **Timeline:** Draft new process by end of month

#### Production Bugs from Insufficient Testing (Dev)
- **Pattern:** 2-3 production bugs per sprint that could have been caught with better testing
- **Impact:** Hotfixes disrupt sprint work; client trust erosion
- **Discussion:** Test coverage is 60-70% (target: 80%+); staging sometimes skipped due to time pressure
- **Root Cause:** Testing seen as "nice to have" not "must have"; time pressure leads to shortcuts
- **Proposed Long-Term Solution:**
  - Enforce 80% test coverage (CI/CD blocks merge if <80%)
  - Mandatory staging deployment (no direct-to-production)
  - Add 20% buffer to sprint estimates for testing time
- **Owner:** Olha (backend lead) to implement CI/CD enforcement
- **Timeline:** Starting next sprint (Nov 18)
- **Related:** This will prevent issues like the auth bug we just fixed

### Preventive Measures

**New: Connection Leak Prevention (Dev)**
- **Problem Prevented:** Database connection leaks (like auth bug today)
- **Preventive Measure:** Add "Connection leak check" to code review checklist
  - Reviewer must verify: All database connections properly closed (try/finally blocks)
  - Automated test: Run load test in staging (simulate 100+ concurrent connections)
- **Owner:** Add to PROC-DEV-003 (Code Review Process)

**New: Client Feedback SLA Communication (Design)**
- **Problem Prevented:** Client feedback delays blocking projects
- **Preventive Measure:** Set expectation at project kickoff
  - Include in kickoff email: "Please provide feedback within 48 hours to keep project on schedule"
  - Automated reminder at 36 hours
- **Owner:** Add to PROC-DESIGN-001 (UI/UX Design Process)

**New: Round-Robin Code Reviews (Dev)**
- **Problem Prevented:** Review bottlenecks from uneven distribution
- **Preventive Measure:** GitHub auto-assigns reviewers using round-robin algorithm
  - Ensures balanced distribution
  - Reduces key-person dependency (no single reviewer bottleneck)
- **Owner:** Yaroslav to implement this week

### Lessons Learned

**From Auth Bug (Critical Issue):**
- **Lesson 1:** Staging testing is non-negotiable (bug could have been caught in staging load test)
- **Lesson 2:** Monitoring alerts are critical (alert caught issue within 15 minutes)
- **Lesson 3:** Rollback plan is essential (we debated rollback vs hotfix; having clear criteria would save time)
- **Action:** Document rollback criteria (when to rollback vs when to hotfix)

**From Code Review Bottleneck:**
- **Lesson 1:** Process problems need process solutions (not just "try harder")
- **Lesson 2:** Metrics reveal patterns (we didn't realize Olha was reviewing 70% until we looked at data)
- **Lesson 3:** Dedicated time needed (treating reviews as "fit it in" doesn't work)
- **Action:** Systematize review process; track metrics

**From Client Feedback Delays:**
- **Lesson 1:** Set expectations proactively (don't assume client knows turnaround expectations)
- **Lesson 2:** Gentle reminders work (automated email is less awkward than Slack ping)
- **Action:** Build expectation-setting into standard client communication
```

---

### Example 2: LG Team - Campaign Performance Issues

```markdown
## Problems & Solutions

**Problems Discussed:** 2
**Solutions Proposed:** 4
**Solutions Implemented:** 1
**Open Issues:** 1

### High Priority Issues

#### Low Email Open Rates (Previous Campaign) - LG Department
- **Severity:** High (campaign performance)
- **Status:** Resolved (learnings applied to future campaigns)
- **Impact:** September campaign: 18% open rate (target: 30-40%); low open rate = low reply rate = few meetings booked
- **Description:** September email campaign significantly underperformed (18% open vs 30-40% target). Only 1.2% reply rate (target: 3-5%). Client disappointed with results; questioned LG team's capabilities.
- **Root Cause (Identified through analysis):**
  - Subject lines were generic ("Introduction," "Quick question")
  - No A/B testing (sent same subject to all 1,000 contacts)
  - List quality issues (some emails not verified, 8% bounced)
  - Sent during low-engagement time (Friday afternoon)
- **First Identified:** September 30 (campaign results review)
- **Current Workaround:** N/A (campaign complete; learning for future)
- **Proposed Solution:**
  - **Option 1:** Improve subject lines (use curiosity, personalization, specificity)
  - **Option 2:** Implement A/B testing (test 2-3 subject line variants)
  - **Option 3:** Improve list quality (better email verification)
  - **Option 4:** Optimize send timing (Tuesday-Thursday, 10 AM-2 PM)
  - **Option 5:** ALL OF THE ABOVE (comprehensive improvement)
- **Chosen Solution:** Option 5 (implement all improvements)
  - **Rationale:** Multiple issues identified; need comprehensive fix
- **Implementation Plan (October Campaign):**
  - Action: ACT-LG-CONTENT-001 - Write outreach copy (improved subject lines)
  - Owner: Nataliia (ID: 88054) - Content Manager
  - Timeline: Implemented in October campaign (completed)
  - **Changes Made:**
    1. ✅ Subject line overhaul: Specific, curiosity-driven, personalized
       - Example: "{{Company}}'s hiring plan for Q4?" (vs generic "Quick question")
    2. ✅ A/B testing: 3 subject line variants tested
    3. ✅ List quality: Used Hunter.io for email verification (reduced bounce rate 8% → 4%)
    4. ✅ Send timing: Tuesday & Thursday, 11 AM EST
    5. ✅ Personalization: Added {{FirstName}} and {{Company}} to all emails
- **Success Criteria:**
  - Open rate >30%
  - Reply rate >3%
  - Bounce rate <5%
- **RESULTS (October Campaign):**
  - ✅ **35% open rate** (up from 18% - 94% improvement!)
  - ✅ **4.2% reply rate** (up from 1.2% - 250% improvement!)
  - ✅ **4% bounce rate** (down from 8%)
  - ✅ **12 meetings booked** (vs 3 in September)
- **Related Items:**
  - Process: PROC-LG-003 (Email Outreach Campaign) - Updated with new best practices
  - Expected Result: RES-LG-003 (Meetings booked) - Achieved 4x improvement

**Key Learnings Applied Going Forward:**
- Personalization increased response by 40% (data from A/B test)
- Subject lines are critical (3 variants tested; best performed 22% better than worst)
- List quality > list size (better to have 800 verified emails than 1,000 unverified)
- Send timing matters (Tuesday 11 AM had 12% higher opens than Friday 3 PM)

### Medium/Low Priority Issues

#### Manual Data Cleaning Time-Consuming - LG Department (Medium)
- **Problem:** Removing duplicates and normalizing data takes 2 hours per list (manual Excel work)
- **Impact:** Bottleneck in workflow; human error (sometimes duplicates missed)
- **Root Cause:** No automation; manual copy-paste and find-replace in Excel
- **Solution:** Build Python script to auto-remove duplicates + normalize data
- **Owner:** Isaac (ID: 86453) - Has prompt engineering skills; can build automation
- **Timeline:** Build script by end of month; deploy in workflow
- **Expected Impact:** Reduce 2 hours → 15 minutes (88% time savings)
- **Status:** Open (Isaac to start next week)

### Resolved in Meeting

#### Apollo.io Export Limit Reached - LG Department
- **Problem:** Monthly export limit reached mid-month (can't build more lists until next month)
- **Solution Implemented:** Upgrade Apollo plan (5,000 → 10,000 exports/month)
- **Outcome:** Immediate upgrade; team can now build remaining client lists
- **Who Fixed:** Anastasiya approved budget; Hanan processed upgrade
- **Cost:** +$100/month (approved)

### Recurring Problems

None identified

### Preventive Measures

**New: Email Campaign Quality Checklist (LG)**
- **Problem Prevented:** Low-performing campaigns (like September)
- **Preventive Measure:** Pre-launch checklist for all campaigns:
  - [ ] Subject lines A/B tested (minimum 2 variants)
  - [ ] Emails verified (Hunter.io or NeverBounce)
  - [ ] Personalization tokens included ({{FirstName}}, {{Company}})
  - [ ] Send time optimized (Tue-Thu, 10 AM-2 PM)
  - [ ] Bounce rate from test send <5%
- **Owner:** Add to PROC-LG-003 (Email Outreach Campaign)

### Lessons Learned

**From September Campaign Failure:**
- **Lesson 1:** Personalization is not optional (40% impact on response rate)
- **Lesson 2:** A/B test everything (subject lines, send times, CTAs)
- **Lesson 3:** List quality > list quantity (verified 800 > unverified 1,000)
- **Lesson 4:** Learn from failures fast (September failed; October succeeded by applying learnings immediately)
- **Action:** Codify October improvements as standard process
```

---

## Validation Checklist

- [ ] **All problems mentioned** are captured
- [ ] **Severity assessed** (Critical, High, Medium, Low)
- [ ] **Status indicated** (Open, In Progress, Resolved)
- [ ] **Impact described** (who/what affected)
- [ ] **Root cause identified** (why problem exists)
- [ ] **Solutions proposed** documented
- [ ] **Chosen solution** clearly stated
- [ ] **Implementation plan** detailed (action, owner, timeline)
- [ ] **Success criteria** defined
- [ ] **Actions linked** to Responsibilities/Responsibilities/Actions library (ACT-XXX)
- [ ] **Processes referenced** if relevant (PROC-XXX)
- [ ] **Expected results** noted (RES-XXX)
- [ ] **Resolved items** captured
- [ ] **Recurring problems** identified
- [ ] **Preventive measures** documented
- [ ] **Lessons learned** extracted

---

## Related Templates

**Previous:** [06_Rules_Best_Practices.md](06_Rules_Best_Practices.md) - Standards
**Next:** [08_Tools_Resources.md](08_Tools_Resources.md) - Tool discussions
**Related:** [13_Blockers_Dependencies.md](13_Blockers_Dependencies.md) - Blocking issues
**Libraries:** Actions, Processes, Results for linking

---

**Status:** ✅ Template ready for use
