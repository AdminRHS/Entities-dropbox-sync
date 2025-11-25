# Template 10: Decisions Log

**Purpose:** Document key decisions made during meetings
**Library Integration:** ⭐ Low (primarily standalone decision tracking)
**Priority:** Include when significant decisions are made

---

## Template

```markdown
## Decisions Log

**Decisions Made:** [Number]
**Pending Decisions:** [Number]
**Decision Owners:** [Number of people]
**Impact Level:** [Critical | High | Medium | Low]

### Critical Decisions

#### Decision: [Decision Title]
- **Date:** YYYY-MM-DD
- **Category:** [Strategic | Technical | Process | Budget | Hiring | Product]
- **Decision:** [What was decided - clear, concise statement]
- **Context:** [Why this decision was needed - background]
- **Decision Makers:** [Who made this decision]
- **Input From:** [Who was consulted]
- **Alternatives Considered:**
  1. [Option 1] - [Pros/Cons]
  2. [Option 2] - [Pros/Cons]
  3. [Option 3 - CHOSEN] - [Pros/Cons]
- **Rationale:** [Why this option was chosen]
- **Impact:**
  - **Team:** [How this affects the team]
  - **Timeline:** [Schedule impact]
  - **Budget:** [Cost impact]
  - **Clients:** [Client impact]
- **Implementation:**
  - **Owner:** [Who will execute]
  - **Timeline:** [When this will be implemented]
  - **Dependencies:** [What's needed]
- **Success Criteria:** [How to measure if this was the right decision]
- **Reversibility:** [Can this decision be changed? At what cost?]
- **Review Date:** [When to review if decision is working]

### High Priority Decisions

[Same structure as Critical, can be slightly more concise]

### Medium/Low Priority Decisions

[More concise format for smaller decisions]

### Deferred Decisions

#### Decision: [What needs to be decided]
- **Deferred Until:** [Date or condition]
- **Reason for Deferral:** [Why not decided now]
- **Information Needed:** [What's needed to make decision]
- **Owner:** [Who will bring this back]

### Decision Reversals

#### Reversed: [Previous Decision]
- **Original Decision:** [What was decided before]
- **Original Date:** YYYY-MM-DD
- **Reversal:** [New decision]
- **Reason for Reversal:** [Why we changed our mind]
- **Lessons Learned:** [What we learned from this]

### Decision Impact Matrix

| Decision | Impact Area | Magnitude | Timeline | Owner |
|----------|-------------|-----------|----------|-------|
| [Title] | [Area] | [H/M/L] | [When] | [Who] |

### Stakeholder Communication

[How and when decisions will be communicated to broader team/clients]
```

---

## Recognition Rules

### Identifying Decisions

**Direct Decision Language:**
- "We decided to..."
- "The decision is..."
- "We're going with..."
- "Approved"
- "Let's do..."

**Decision Points:**
- "Should we A or B?" → "[Response]" = Decision
- "What do you think about X?" → "Yes, let's proceed" = Decision
- "I propose we..." → "Agreed" = Decision

**Approval Language:**
- "Approved"
- "Go ahead"
- "Green light"
- "Let's move forward"

**Rejection Language:**
- "No, we won't..."
- "Decided against..."
- "Declined"
- "Not proceeding with..."

### Decision Categories

**Strategic Decisions:**
- Company direction
- Major initiatives
- Market positioning
- Long-term goals

**Technical Decisions:**
- Architecture choices
- Technology stack
- Infrastructure
- Tool selection

**Process Decisions:**
- Workflow changes
- New procedures
- Policy updates
- Standards

**Budget Decisions:**
- Spending approvals
- Resource allocation
- Tool subscriptions
- Hiring budget

**Hiring Decisions:**
- New positions
- Promotions
- Team restructuring
- Contractor hiring

**Product Decisions:**
- Feature priorities
- Roadmap changes
- Product direction
- Client offerings

### Decision Impact Levels

**Critical:**
- Affects entire company
- Major budget impact (>$5K)
- Strategic direction change
- High risk if wrong

**High:**
- Affects multiple teams
- Significant budget ($1K-$5K)
- Important but not strategic
- Moderate risk

**Medium:**
- Affects one team
- Small budget (<$1K)
- Operational decision
- Low risk

**Low:**
- Individual level
- Minimal budget
- Easily reversible
- Very low risk

---

## Examples

### Example 1: Multi-Department Decisions

```markdown
## Decisions Log

**Decisions Made:** 5
**Pending Decisions:** 1
**Decision Owners:** 4
**Impact Level:** 2 Critical, 2 High, 1 Medium

### Critical Decisions

#### Decision: Extract Authentication to Microservice (Dev)
- **Date:** 2025-11-15
- **Category:** Technical
- **Decision:** Extract authentication functionality from monolithic API to dedicated microservice using Node.js + Redis
- **Context:**
  - Recent production outage (auth bug caused full system downtime)
  - Performance issues (auth queries slowing down main API - 300ms latency)
  - Scalability concern (auth can't scale independently)
  - Security vulnerability (no rate limiting for login attempts)
- **Decision Makers:** Olha Kizilova (Backend Developer/Tech Lead), approved by Anastasiya (Manager)
- **Input From:** Yaroslav Klimenko (Developer), team discussion in sprint planning
- **Alternatives Considered:**
  1. **Keep monolithic auth** - Pros: Simpler, no architecture change. Cons: Doesn't solve performance/scalability/security issues
  2. **Use third-party auth (Auth0, Firebase)** - Pros: No development needed, battle-tested. Cons: Expensive ($500+/month), vendor lock-in
  3. **Build custom microservice (CHOSEN)** - Pros: Decoupled, scalable, secure, cost-effective. Cons: 5 weeks development time, added complexity
- **Rationale:**
  - Option 1 doesn't solve core problems (status quo unacceptable)
  - Option 2 too expensive for current scale (200 users, projected 1,000 in 6 months)
  - Option 3 best long-term: Solves all issues, manageable cost ($135/month infrastructure vs $500+/month SaaS)
- **Impact:**
  - **Team:** Dev team will focus on this for 5 weeks (delays other features)
  - **Timeline:** 5-week implementation (Nov 18 - Dec 20)
  - **Budget:** +$135/month infrastructure (ElastiCache Redis + additional EC2); one-time development cost ~120 hours
  - **Clients:** No direct impact (backend change); improved reliability long-term
- **Implementation:**
  - **Owner:** Olha Kizilova (lead developer)
  - **Timeline:**
    - Week 1: Design API contract
    - Week 2-3: Build microservice
    - Week 4: Integration testing
    - Week 5: Production deployment (gradual rollout)
  - **Dependencies:**
    - AWS ElastiCache Redis setup (Anastasiya to provision)
    - CI/CD pipeline for auth service (Yaroslav to configure)
- **Success Criteria:**
  - Auth latency reduced from 300ms → <50ms (83% improvement)
  - 99.9% uptime for auth service (measured over 30 days post-launch)
  - Zero authentication-related production incidents in first 60 days
  - Load testing: Handle 1,000 concurrent users (10x current load)
- **Reversibility:** Difficult to reverse after 2-3 weeks (once main API refactored). Rollback plan: Keep monolithic auth running in parallel for first 30 days.
- **Review Date:** January 15, 2026 (60 days post-launch)

#### Decision: Hire Additional Lead Generator (LG)
- **Date:** 2025-11-15
- **Category:** Hiring
- **Decision:** Hire 1 additional lead generator (full-time, remote) by end of December
- **Context:**
  - Current LG team: 11 people (at capacity)
  - Client demand increased 40% in Q4 (more lead list projects)
  - Team working overtime (unsustainable)
  - Apollo.io limit issue revealed we're near capacity (6,500 exports/month, upgraded to 10,000)
- **Decision Makers:** Anastasiya (Sales Manager), Hanan Zaheur (LG Team Lead)
- **Input From:** LG team (reported capacity issues)
- **Alternatives Considered:**
  1. **Overtime for existing team** - Pros: No hiring cost/time. Cons: Unsustainable, burnout risk, quality may suffer
  2. **Hire contractor (part-time)** - Pros: Flexible, lower commitment. Cons: Less reliable, training overhead for temporary help
  3. **Hire full-time employee (CHOSEN)** - Pros: Dedicated capacity, team culture, long-term investment. Cons: Higher cost, 4-week recruitment
- **Rationale:**
  - Q4 demand increase appears sustainable (client feedback indicates ongoing need)
  - Team at breaking point (overtime not sustainable)
  - Full-time hire provides stability (contractor would need constant management)
  - ROI calculation: Additional LG can handle 15-20 lists/month × $300 avg = $4,500-$6,000 revenue vs $1,200 salary = Positive ROI
- **Impact:**
  - **Team:** Reduced pressure on existing LG team; mentorship opportunity
  - **Timeline:** Recruitment 2-3 weeks, onboarding 1-2 weeks, productive by mid-January
  - **Budget:** $1,200/month salary + $200 tools/benefits = $1,400/month total cost
  - **Clients:** Faster turnaround on lead lists (5-7 days → 4-5 days)
- **Implementation:**
  - **Owner:** Anastasiya (recruitment lead), Hanan (interviewing + training)
  - **Timeline:**
    - Nov 18-25: Post job ads (Upwork, LinkedIn, internal network)
    - Nov 25-Dec 6: Interview candidates (target 10-15 applications)
    - Dec 6: Make offer
    - Dec 9: Start date (2-week onboarding)
  - **Dependencies:**
    - Job description (Anastasiya to draft by Nov 18)
    - Onboarding materials (Hanan to update LG onboarding docs)
    - Laptop/tools budget (approved)
- **Success Criteria:**
  - Hire completed by December 9
  - New hire productive (delivering 5+ lists/month) by mid-January
  - Team capacity increased by 20% (measured by lists delivered/month)
  - Team overtime reduced by 30%
- **Reversibility:** Can be reversed (probation period: 90 days). If demand drops, can transition to part-time or end contract.
- **Review Date:** February 15, 2026 (after 90-day probation)

### High Priority Decisions

#### Decision: Upgrade Apollo.io Plan (LG)
- **Date:** 2025-11-15
- **Category:** Budget (Tool subscription)
- **Decision:** Upgrade Apollo.io from 5,000 exports/month to 10,000 exports/month ($149/month → $249/month)
- **Context:** Monthly export limit reached mid-month (blocked from delivering client lists)
- **Decision Makers:** Anastasiya (Sales Manager - budget approval)
- **Input From:** Hanan (reported limit issue), LG team (confirmed usage pattern)
- **Alternatives Considered:**
  1. **Keep current plan, use LinkedIn Sales Navigator as backup** - Rejected: Less efficient workflow, inconsistent data quality
  2. **Upgrade to 10,000/month (CHOSEN)** - Approved: Solves immediate problem, room for growth
  3. **Switch to different tool (ZoomInfo)** - Rejected: Too expensive ($15K+/year), not worth migration effort
- **Rationale:** Team uses ~6,500 exports/month (30% over limit); 10,000/month provides 50% buffer for growth
- **Impact:**
  - **Team:** Removes bottleneck; team can work without worrying about limits
  - **Timeline:** Immediate (upgraded during meeting)
  - **Budget:** +$100/month ($1,200/year)
  - **Clients:** No more delays due to tool limits
- **Implementation:**
  - **Owner:** Hanan (processed upgrade during meeting)
  - **Timeline:** Completed immediately
  - **Dependencies:** None
- **Success Criteria:** Team never hits 10,000 limit in next 6 months (indicates sufficient capacity)
- **Reversibility:** Can downgrade if usage decreases (unlikely)
- **Review Date:** May 2026 (6 months; check if still needed)

#### Decision: Implement Mobile-First Design Standard (Design)
- **Date:** 2025-11-15
- **Category:** Process
- **Decision:** All responsive web projects must start with mobile wireframes (375px), then scale up to tablet/desktop
- **Context:**
  - Recent projects had poor mobile UX (desktop designs poorly adapted to mobile)
  - Mobile usage >60% for most clients
  - Design team agreed desktop-first is backwards
- **Decision Makers:** Anastasiia (Design Lead), team consensus
- **Input From:** All designers (discussed pain points with current approach)
- **Alternatives Considered:**
  1. **Continue desktop-first** - Rejected: Leads to poor mobile UX
  2. **Mobile-first for all projects (CHOSEN)** - Approved: Better UX, matches user behavior
  3. **Designer choice (case-by-case)** - Rejected: Inconsistent results
- **Rationale:** Mobile-first ensures better mobile UX (designing for constraints first, then expanding to desktop is easier than reverse)
- **Impact:**
  - **Team:** Workflow change; designers need to adjust mindset (training needed)
  - **Timeline:** Effective immediately (all new projects starting Nov 18+)
  - **Budget:** No cost (process change only)
  - **Clients:** Better mobile UX (higher user satisfaction)
- **Implementation:**
  - **Owner:** Anastasiia (enforce in project reviews)
  - **Timeline:** Immediate for new projects; existing projects can continue with current approach
  - **Dependencies:** Update design process documentation (PROC-DESIGN-001)
- **Success Criteria:**
  - 100% of new projects start with mobile wireframes
  - Client feedback: Improved mobile UX (measured in project retrospectives)
  - Designer feedback: Mobile-first feels natural after 2-3 projects
- **Reversibility:** Easily reversible (just a process change)
- **Review Date:** January 2026 (after 10+ projects completed with new approach)

### Medium/Low Priority Decisions

#### Decision: Reduce Adobe Creative Cloud Licenses (Design)
- **Date:** 2025-11-15
- **Category:** Budget
- **Decision:** Reduce Adobe CC licenses from 10 to 7 (only 7 designers actively use Adobe; 3 are Figma-only)
- **Rationale:** Wasting $165/month on unused licenses
- **Owner:** Olha (design lead) to audit usage and process cancellation
- **Timeline:** End of month
- **Impact:** $1,980/year savings

#### Decision: Post 2 Dribbble Shots Per Week (Design)
- **Date:** 2025-11-15
- **Category:** Process
- **Decision:** Design team will post 2 shots per week on Dribbble (Tuesdays and Thursdays, 2-3 PM)
- **Rationale:** Maintain agency presence, attract talent, showcase work
- **Owner:** Rotating schedule (each designer posts on assigned weeks)
- **Timeline:** Starting this week
- **Impact:** Improved portfolio visibility

### Deferred Decisions

#### Decision: Implement Clearbit for Data Enrichment (LG)
- **Deferred Until:** December 18, 2025 (after 1-month trial)
- **Reason for Deferral:** Need to test data quality improvement before committing
- **Information Needed:**
  - Data accuracy improvement (Apollo-only vs Apollo + Clearbit)
  - Time investment (is enrichment worth the effort?)
  - Client feedback (do clients notice better data quality?)
- **Trial Plan:** Test on 3 client lists in November
- **Owner:** Hanan (LG lead) to review trial results and make recommendation

### Decision Reversals

None in this meeting

### Decision Impact Matrix

| Decision | Impact Area | Magnitude | Timeline | Owner |
|----------|-------------|-----------|----------|-------|
| Auth Microservice | Technical, Security | Critical | 5 weeks | Olha |
| Hire LG | Team Capacity | Critical | 4 weeks | Anastasiya |
| Apollo Upgrade | Tools, Budget | High | Immediate | Hanan |
| Mobile-First Design | Process, Quality | High | Immediate | Anastasiia |
| Adobe License Reduction | Budget | Medium | 2 weeks | Olha |
| Dribbble Posting | AI | Low | Immediate | Design Team |

### Stakeholder Communication

**Auth Microservice Decision:**
- **Audience:** Dev team (full details), broader team (summary)
- **Method:** Dev team meeting (detailed), company Slack announcement (summary)
- **Timing:** This week (Nov 18)
- **Message:** "We're improving authentication reliability and performance with a new architecture. No impact to your work, but this is why dev team will be focused on infrastructure for next 5 weeks."

**New Hire Decision:**
- **Audience:** LG team (first), broader team (announcement)
- **Method:** LG team meeting (discuss mentorship), company announcement when hired
- **Timing:** LG team informed immediately; broader team when candidate accepted offer
- **Message:** "We're growing the LG team to meet increased client demand. Excited to welcome a new team member in December!"

**Apollo Upgrade:**
- **Audience:** LG team (directly affected)
- **Method:** Slack message (immediate)
- **Timing:** Today (completed during meeting)
- **Message:** "Apollo limit increased to 10,000/month. No more mid-month capacity issues!"

**Mobile-First Design:**
- **Audience:** Design team (primary), dev team (aware of new deliverable format)
- **Method:** Design team meeting (detailed), dev team FYI (Slack)
- **Timing:** This week
- **Message:** "All new responsive projects will start with mobile wireframes. This ensures better mobile UX for our clients."
```

---

### Example 2: Single-Department Focus (Hiring Decision)

```markdown
## Decisions Log

**Decisions Made:** 1
**Pending Decisions:** 0
**Decision Owners:** 1
**Impact Level:** Critical

### Critical Decisions

#### Decision: Hire Senior Frontend Developer (Dev)
- **Date:** 2025-11-15
- **Category:** Hiring
- **Decision:** Hire 1 Senior Frontend Developer (React specialist) by end of January 2026
- **Context:**
  - Current dev team: 2 backend developers (Olha, Yaroslav), 1 full-stack (Liliia)
  - Recent projects require advanced React skills (complex state management, performance optimization)
  - Liliia is junior-level frontend (capable but needs mentorship for complex work)
  - Client A project: Needs senior-level React expertise (interactive dashboard with real-time updates, 10K+ data points)
  - Team is bottlenecked on frontend work (Yaroslav helps but backend is his strength)
- **Decision Makers:** Anastasiya (Manager), Olha (Tech Lead)
- **Input From:** Dev team (reported frontend capacity issue); Client A (confirmed project complexity)
- **Alternatives Considered:**
  1. **Upskill Liliia (training/mentorship)** - Pros: No hiring cost, develop internal talent. Cons: Takes 6-9 months, Client A project needs expertise now
  2. **Hire contractor for Client A project** - Pros: Temporary, lower commitment, immediate help. Cons: Expensive ($50-80/hour), knowledge doesn't stay in team
  3. **Hire senior full-time (CHOSEN)** - Pros: Long-term investment, mentors Liliia, builds frontend capability. Cons: Higher salary ($2,500-3,000/month), recruitment time
  4. **Delay Client A project** - Rejected: Client expects delivery in Q1; delay damages relationship
- **Rationale:**
  - Client A project is high-value ($25K contract, potential for ongoing work)
  - Contractor would cost $15K+ for this project alone (3 months × $5K/month avg); senior hire is $7,500-9,000 (more economical if we have ongoing frontend work)
  - Team skill gap is strategic issue (not just one project); need to build frontend expertise
  - Liliia would benefit from senior mentorship (invest in team growth)
  - Market analysis: Hiring market is good (many qualified candidates available)
- **Impact:**
  - **Team:** Strengthens frontend capability; Liliia gets mentorship; team can take on more complex frontend projects
  - **Timeline:** Recruitment 4-6 weeks (competitive market for senior roles), start date target: early January
  - **Budget:** $2,500-3,000/month salary + $300 tools/benefits = ~$2,800-3,300/month total cost (~$34K-40K/year)
  - **Clients:** Can deliver Client A project on time (Q1); can take on similar complex projects in future
- **Implementation:**
  - **Owner:** Anastasiya (recruitment lead), Olha (technical interviews + onboarding)
  - **Timeline:**
    - Nov 18-25: Write job description (Olha + Anastasiya)
    - Nov 25: Post to LinkedIn, Upwork, React Jobs, AngelList, Remote OK
    - Dec 2-20: Review applications (target 20-30 candidates), conduct interviews
      - Screen: Olha reviews portfolios, rejects weak candidates
      - Technical interview: Live coding challenge (2 hours, React + TypeScript)
      - Culture fit: Anastasiya interview (team values, communication)
    - Dec 23: Make offer to top candidate
    - Jan 6: Start date (2-week onboarding, pair with Liliia on Client A project)
  - **Dependencies:**
    - Job description approved (Anastasiya + Olha collaboration)
    - Budget approved (already confirmed: $3,000/month max)
    - Onboarding plan (Olha to create: 2-week ramp-up plan)
    - Client A project timeline (must align: new hire starts → 1 week onboarding → 10 weeks development → Q1 delivery)
- **Success Criteria:**
  - **Recruitment Success:**
    - Hire completed by December 31 (target: Jan 6 start date)
    - Candidate has 5+ years React experience, portfolio with 3+ complex projects
    - Strong technical skills (validated in coding challenge)
    - Culture fit (team feedback positive)
  - **Performance Success (measured at 90 days):**
    - Client A project delivered on time, high quality (client satisfaction >4/5)
    - New hire mentoring Liliia (Liliia reports skill improvement)
    - Team velocity increased by 30% on frontend work (measured by story points)
    - New hire retention (still with team at 90 days, plans to stay long-term)
- **Reversibility:**
  - Probation period: 90 days (can end contract if not working out)
  - If Client A project is only complex frontend work: Could transition to part-time or contractor after project (but team believes ongoing need exists)
  - Downside of reversal: Lost recruitment time, team disruption, Liliia misses mentorship opportunity
- **Review Date:**
  - **30 days (Feb 6):** Check-in on onboarding, early performance, Client A project progress
  - **90 days (April 6):** Full performance review, decision to continue employment, evaluate if frontend capability gap is solved

**Risk Mitigation:**
- **Risk 1: Can't find qualified candidate in timeline**
  - Mitigation: Cast wide net (5 job boards), leverage network (ask for referrals), consider remote candidates globally (not just local)
  - Backup plan: Hire contractor for Client A project if can't find full-time by Dec 31
- **Risk 2: New hire doesn't perform as expected**
  - Mitigation: Rigorous interview process (technical challenge reveals real skills), 90-day probation
  - Backup plan: End contract during probation, hire replacement
- **Risk 3: Budget overrun (salary higher than expected)**
  - Mitigation: Set max budget upfront ($3,000/month firm cap), decline candidates who require more
  - Backup plan: If all candidates require >$3,000, re-evaluate (hire mid-level instead of senior, or delay hire)

**Job Description Key Points (Draft):**
- **Title:** Senior Frontend Developer (React Specialist)
- **Location:** Remote (global)
- **Salary:** $2,500-3,000/month (negotiable based on experience)
- **Requirements:**
  - 5+ years professional React experience
  - Expert in: React Hooks, Context API, Redux (or similar state management)
  - Strong TypeScript skills
  - Performance optimization experience (handling large datasets, real-time updates)
  - Testing: Jest, React Testing Library
  - Bonus: GraphQL, WebSocket, data visualization (D3.js, Chart.js)
- **Responsibilities:**
  - Lead frontend development on Client A project (interactive dashboard)
  - Mentor junior developer (Liliia)
  - Establish frontend best practices, code review standards
  - Collaborate with backend team on API design
- **Culture Fit:**
  - Remote-first team (async communication, self-directed)
  - Startup environment (wear multiple hats, move fast)
  - Mentorship mindset (we value teaching and learning)
```

---

## Validation Checklist

- [ ] **All decisions** clearly stated
- [ ] **Decision dates** recorded
- [ ] **Categories** assigned (Strategic, Technical, Process, Budget, Hiring, Product)
- [ ] **Decision makers** identified
- [ ] **Context** provided (why decision needed)
- [ ] **Alternatives** considered and documented
- [ ] **Rationale** explained (why chosen option is best)
- [ ] **Impact** assessed (team, timeline, budget, clients)
- [ ] **Implementation plan** detailed (owner, timeline, dependencies)
- [ ] **Success criteria** defined (measurable outcomes)
- [ ] **Reversibility** noted (can it be changed?)
- [ ] **Review date** set (when to evaluate if decision worked)
- [ ] **Deferred decisions** tracked
- [ ] **Stakeholder communication** planned
- [ ] **Decision matrix** completed (if multiple decisions)

---

## Related Templates

**Previous:** [09_Technical_Architecture.md](09_Technical_Architecture.md) - Architecture decisions
**Next:** [11_Documentation_Gaps.md](11_Documentation_Gaps.md) - Documentation needs
**Related:** [03_Action_Items_Tasks.md](03_Action_Items_Tasks.md) - Actions resulting from decisions
**Reference:** All decisions should have clear owners and implementation plans

---

**Status:** ✅ Template ready for use
