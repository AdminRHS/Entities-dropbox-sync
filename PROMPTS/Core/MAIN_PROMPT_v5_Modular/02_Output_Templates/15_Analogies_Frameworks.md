# Template 15: Analogies & Frameworks

**Purpose:** Capture analogies, mental models, and frameworks used to explain concepts
**Library Integration:** ⭐ Low (standalone knowledge capture)
**Priority:** Include when useful analogies or frameworks are discussed

---

## Template

```markdown
## Analogies & Frameworks

**Analogies Used:** [Number]
**Frameworks Applied:** [Number]
**Mental Models:** [Number]

### Analogies

#### [Analogy Title]
- **Concept Explained:** [What was being explained]
- **Analogy:** [The comparison/metaphor used]
- **How It Helps:** [Why this analogy is useful]
- **Who Used It:** [Person who shared the analogy]
- **Application:** [When to use this analogy again]

### Frameworks

#### [Framework Name]
- **Purpose:** [What this framework helps with]
- **Framework:** [Description of the framework]
- **How to Apply:** [Step-by-step usage]
- **Example:** [Concrete example]
- **When to Use:** [Situations where this applies]

### Mental Models

#### [Mental Model Name]
- **Model:** [The mental model]
- **Concept:** [What it helps understand]
- **Application:** [How to use this model]

### Problem-Solving Approaches

[Specific approaches or methodologies discussed]

### Decision-Making Frameworks

[Frameworks used to make decisions]
```

---

## Examples

```markdown
## Analogies & Frameworks

**Analogies Used:** 2
**Frameworks Applied:** 2
**Mental Models:** 1

### Analogies

#### Microservices Architecture = Specialized Teams (Not One Person Doing Everything)
- **Concept Explained:** Why extract authentication to separate microservice (instead of keeping monolithic)
- **Analogy:** "It's like having specialized teams instead of one person doing everything. Right now, our main API is like a generalist doing authentication, data processing, business logic, everything. It's overwhelmed. Extracting auth to a microservice is like hiring a specialist who only does authentication—they do it better, faster, and if they're sick, the rest of the team keeps working."
- **How It Helps:**
  - Non-technical stakeholders understand why microservices matter
  - Illustrates benefits: specialization, fault isolation, scalability
  - Relatable (everyone understands specialist vs generalist)
- **Who Used It:** Olha (explaining technical decision to team)
- **Application:** Use when explaining microservices to non-technical audience

#### Mobile-First Design = Building for Constraints First (Like Designing Tiny House Before Mansion)
- **Concept Explained:** Why mobile-first design approach is better than desktop-first
- **Analogy:** "Designing mobile-first is like designing a tiny house first, then expanding to a mansion. When you design for constraints (small screen), you're forced to prioritize what's essential. Then expanding to desktop is easy (more space for nice-to-haves). But if you design the mansion first, squeezing it into a tiny house is painful—you lose important features."
- **How It Helps:**
  - Designers understand the philosophy (not just following rules)
  - Illustrates why constraints help (force prioritization)
  - Makes sense of why desktop-first often fails on mobile
- **Who Used It:** Anastasiia (explaining mobile-first to design team)
- **Application:** Use when teaching mobile-first approach

### Frameworks

#### Pre-Flight Checklist Framework (Campaign Quality Assurance)
- **Purpose:** Ensure campaign quality before launch (prevent avoidable failures)
- **Framework:** 7-item pre-launch checklist (borrowed from aviation pre-flight checks)
  1. ✅ Emails verified (<5% bounce rate)
  2. ✅ Subject lines A/B tested (minimum 2 variants)
  3. ✅ Personalization tokens included
  4. ✅ Send time optimized (Tue-Thu, 10 AM-2 PM)
  5. ✅ Test send completed
  6. ✅ Unsubscribe link included
  7. ✅ Campaign tracking set up
- **How to Apply:**
  - Before launching any email campaign, complete checklist
  - Don't skip items (each item prevents specific failure mode)
  - Mark each item complete before proceeding
- **Example:** October campaign used checklist → 94% improvement over September (no checklist)
- **When to Use:** Every email campaign, without exception
- **Origin:** Inspired by airline pre-flight checklists (prevent catastrophic failures through systematic checks)

#### 80/20 Rule for Lead Prioritization (Pareto Principle)
- **Purpose:** Focus effort on highest-value leads (maximize meeting booking rate)
- **Framework:** Pareto Principle (80% of results come from 20% of effort)
  - **Application to Leads:**
    - Score all leads (1-10 scale)
    - Hot Leads (8-10) = Top 20% → Drive 80% of meetings booked
    - Focus outreach time on Hot Leads (personalized, multi-touch)
    - Warm/Cold Leads get templated, automated outreach
- **How to Apply:**
  1. Score leads using criteria (company size, title, industry, engagement)
  2. Segment: Hot (8-10), Warm (5-7), Cold (1-4)
  3. Allocate effort: 60% time on Hot, 30% on Warm, 10% on Cold
  4. Measure: Track meeting booking rate by segment (validate 80/20 hypothesis)
- **Example:** October campaign data validated this:
  - Hot Leads: 12% meeting booking rate (3 of 25) → 3 meetings from 15% of list
  - Warm Leads: 4% meeting booking rate (2 of 50)
  - Cold Leads: 1% meeting booking rate (0 of 100)
  - Result: 75% of meetings came from top 25% of list (close to 80/20)
- **When to Use:** Every lead generation campaign (prioritize before outreach)

### Mental Models

#### "Fail Fast, Learn Fast" (Iterative Improvement)
- **Model:** Rapid experimentation with quick feedback loops
- **Concept:** Don't aim for perfection on first try; ship quickly, measure, iterate
- **Application:**
  - September campaign failed fast (1 week to see poor results)
  - Analyzed failures immediately (didn't wait, didn't repeat)
  - Applied learnings to October (comprehensive improvements)
  - Result: 250% improvement in reply rate (Sept → Oct)
- **When to Use:**
  - Campaigns (don't overthink, test quickly)
  - Product development (MVP → iterate)
  - Process changes (try, measure, adjust)
- **Anti-pattern:** Perfectionism (spend 3 months perfecting, never ship, never learn)

### Problem-Solving Approaches

**Five Whys (Root Cause Analysis)**
- Used to analyze September campaign failure:
  - **Problem:** Low open rates (18%)
  - **Why 1:** Subject lines weren't compelling → Why?
  - **Why 2:** Used generic subject lines ("Quick question") → Why?
  - **Why 3:** Didn't test subject lines (guessed what would work) → Why?
  - **Why 4:** No A/B testing process in place → Why?
  - **Why 5 (Root Cause):** No campaign quality framework (shipped campaigns without validation)
  - **Solution:** Implement pre-flight checklist (prevents shipping untested campaigns)

### Decision-Making Frameworks

**ROI-Based Prioritization (Effort vs Impact Matrix)**
- Used to decide between hiring full-time vs contractor for LG team:
  - **X-axis:** Effort (time, cost, complexity)
  - **Y-axis:** Impact (revenue, team capacity, quality)
  - **Quadrants:**
    - High Impact, Low Effort = DO FIRST (quick wins)
    - High Impact, High Effort = STRATEGIC (invest here - full-time hire falls here)
    - Low Impact, Low Effort = DO IF TIME (low priority)
    - Low Impact, High Effort = AVOID (waste of resources)
  - **Analysis:**
    - Full-time hire: High effort ($34K/year, 4-week recruitment), High impact (long-term capacity, team culture)
    - Contractor: Medium effort ($5K+/month, faster hire), Medium impact (temporary capacity, no long-term benefit)
    - Result: Chose full-time hire (strategic investment, better ROI long-term)
```

---

## Validation Checklist

- [ ] **Analogies** captured with context
- [ ] **Frameworks** documented with application steps
- [ ] **Mental models** explained clearly
- [ ] **Examples** provided for each
- [ ] **When to use** specified
- [ ] **Who used** the analogy/framework noted
- [ ] **Problem-solving approaches** detailed
- [ ] **Decision frameworks** applied correctly

---

## Related Templates

**Previous:** [14_Insights_Lessons.md](14_Insights_Lessons.md) - Insights
**Next:** [16_Employee_Team_Context.md](16_Employee_Team_Context.md) - Team context
**Related:** All templates can reference frameworks/analogies

---

**Status:** ✅ Template ready for use
