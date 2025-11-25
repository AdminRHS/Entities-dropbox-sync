# Template 16: Employee & Team Context

**Purpose:** Track employee-specific context, team dynamics, and personnel information
**Library Integration:** ⭐⭐⭐ Heavy (Employee Directory - 32 employees across 7 departments)
**Priority:** Include when employee assignments, team dynamics, or personnel matters discussed

---

## Template

```markdown
## Employee & Team Context

**Employees Mentioned:** [Number]
**Team Assignments:** [Number]
**Capacity Discussed:** [Yes/No]
**Performance Mentioned:** [Yes/No]

### Employee Assignments

#### [Employee Name] (ID: [Employee ID])
- **Position:** [Current role]
- **Department:** [Department]
- **Assignments Discussed:**
  - [Project/Task 1]
  - [Project/Task 2]
- **Workload:** [Current capacity - overloaded | at capacity | has capacity]
- **Skills Highlighted:** [Skills relevant to discussion]
- **Action Items:** [Tasks assigned]

### Team Capacity

#### [Department] Team
- **Team Size:** [Number of people]
- **Current Capacity:** [Percentage utilization]
- **Constraints:** [Capacity limitations]
- **Hiring Plans:** [If discussed]

### Skills & Expertise

#### [Skill/Expertise Area]
- **Current Team Members:** [Who has this skill]
- **Skill Level:** [Expert | Proficient | Learning]
- **Gaps:** [Skills needed but missing]
- **Development Plans:** [Training or hiring]

### Team Dynamics

[Collaboration patterns, team health, communication]

### Performance & Growth

[Development, achievements, areas for improvement]

### Hiring & Recruitment

[New positions, hiring status, candidate pipeline]

### Onboarding & Training

[New employees, training needs, mentorship]

### Team Structure Changes

[Reorganizations, role changes, promotions]
```

---

## Examples

```markdown
## Employee & Team Context

**Employees Mentioned:** 8
**Team Assignments:** 5
**Capacity Discussed:** Yes
**Performance Mentioned:** Yes

### Employee Assignments

#### Olha Kizilova (ID: 178)
- **Position:** Backend Developer
- **Department:** Dev
- **Assignments Discussed:**
  - **Project 1:** Auth microservice development (lead developer, 5-week project)
  - **Project 2:** CI/CD pipeline optimization (1-week task, parallel to auth work)
  - **Project 3:** API documentation for v2 (2-week task, critical blocker)
- **Workload:** Fully allocated (100% capacity for next 5 weeks on auth project)
- **Skills Highlighted:**
  - Backend architecture (leading auth microservice design)
  - Node.js/TypeScript expert
  - Infrastructure (Docker, Redis, AWS experience)
- **Action Items:**
  1. Lead auth microservice development (5 weeks, Nov 18 - Dec 20)
  2. Create API documentation by Dec 1 (critical for frontend team)
  3. Optimize CI/CD pipeline by Nov 22 (high priority)
- **Note:** Olha is the technical lead; critical path for multiple projects

#### Yaroslav Klimenko (ID: 86478)
- **Position:** Developer (Full-stack)
- **Department:** Dev
- **Assignments Discussed:**
  - **Project 1:** Auth microservice (supporting Olha, weeks 2-3)
  - **Project 2:** GitHub Actions round-robin PR assignment (1-week setup)
  - **Project 3:** Developer onboarding documentation (2-week writing project)
- **Workload:** At capacity (80-90% utilized; has some flexibility)
- **Skills Highlighted:**
  - Full-stack (React + Node.js)
  - Process documentation (good writer, longest tenure on team)
  - GitHub Actions expertise
- **Action Items:**
  1. Configure GitHub round-robin PR reviews this week
  2. Write developer onboarding guide by Dec 15
  3. Support Olha on auth microservice (weeks 2-3)

#### Liliia (ID: [Not mentioned])
- **Position:** Junior Full-Stack Developer
- **Department:** Dev
- **Assignments Discussed:**
  - Will pair with new senior frontend hire on Client A project (starting Jan 6)
  - Mentorship opportunity (learn advanced React from senior hire)
- **Workload:** Normal capacity (can't lead Client A project alone due to complexity)
- **Skills Highlighted:**
  - React (proficient, but junior-level)
  - Eager to learn (good mentee)
- **Skill Gap:** Advanced React (real-time data, performance optimization for 10K+ data points)
- **Growth Plan:** Pair with senior hire on Client A project (6-month mentorship opportunity)

#### Anastasiya (ID: [Sales Manager])
- **Position:** Sales Manager (Manager role mentioned)
- **Department:** Sales/Management
- **Assignments Discussed:**
  - Approve budgets (Apollo upgrade, Redis infrastructure, hiring)
  - Lead recruitment (LG hire, senior frontend developer)
  - Client relationship management (Client A project)
- **Skills Highlighted:**
  - Budget management
  - Recruitment
  - Client relations
- **Action Items:**
  1. Approve hiring budgets (LG: $1,400/month, Dev: $3,000/month)
  2. Lead senior frontend developer recruitment (4-week process)
  3. Provision AWS ElastiCache Redis (infrastructure setup)

#### Hanan Zaheur (ID: 87984)
- **Position:** Lead Generator, Personal Assistant (LG Team Lead)
- **Department:** LG
- **Assignments Discussed:**
  - Process Apollo.io upgrade (completed during meeting)
  - Lead LG team hiring process (interview + train new hire)
  - Monitor Apollo usage monthly (prevent future limit issues)
- **Workload:** At capacity (leading team + individual contributor)
- **Skills Highlighted:**
  - LG tools expertise (Apollo, Hunter, LinkedIn Sales Navigator)
  - Team leadership
  - Process management
- **Action Items:**
  1. Monitor Apollo usage monthly (alert at 70% capacity)
  2. Interview candidates for new LG hire (December)
  3. Train new hire (onboarding lead, starting Dec 9)

#### Nataliia Rybak (ID: 88054)
- **Position:** Lead Generator, Content Manager
- **Department:** LG
- **Assignments Discussed:**
  - Build campaign copy template library (10-15 templates)
  - Apply October campaign learnings to future campaigns
- **Workload:** Normal capacity
- **Skills Highlighted:**
  - Copywriting (email campaigns, content creation)
  - Campaign performance analysis
- **Action Items:**
  1. Create campaign copy template library by end of November
  2. Document optimal subject line formulas (from October A/B tests)

#### Anastasiia (ID: 86981)
- **Position:** Design Lead
- **Department:** Design
- **Assignments Discussed:**
  - Create design system documentation (critical priority, 4-week project)
  - Draft Figma file organization standard
  - Enforce mobile-first design standard (review projects)
- **Workload:** At capacity (leading team + individual work)
- **Skills Highlighted:**
  - Design leadership
  - Design systems
  - Process creation
- **Action Items:**
  1. Create design system documentation by Dec 15
  2. Finalize Figma organization standard by Nov 22
  3. Review all projects for mobile-first compliance

#### Plamena Peneva (ID: 86297)
- **Position:** Lead Generator
- **Department:** LG
- **Assignments Discussed:**
  - Draft lead scoring criteria (new process)
  - Set up Phantombuster automation for Q4 LinkedIn campaign
- **Workload:** Normal capacity
- **Skills Highlighted:**
  - Automation (Phantombuster expert)
  - Process development (lead scoring)
- **Action Items:**
  1. Draft lead scoring criteria by next week
  2. Configure Phantombuster workflows by Nov 18 (Q4 campaign)

### Team Capacity

#### Dev Team
- **Team Size:** 3 developers (Olha, Yaroslav, Liliia)
- **Current Capacity:** 100% allocated for next 5 weeks (auth microservice project)
- **Constraints:**
  - No bandwidth for new features until late December
  - Frontend expertise gap (need senior React developer)
- **Hiring Plans:**
  - Hire senior frontend developer (start date: Jan 6, 2026)
  - Budget: $2,500-3,000/month
  - Timeline: 4-week recruitment + 2-week onboarding

#### LG Team
- **Team Size:** 11 lead generators (at capacity)
- **Current Capacity:** 100% utilized (demand increased 40% in Q4)
- **Constraints:**
  - Team working overtime (unsustainable)
  - Can't take on more projects without adding headcount
- **Hiring Plans:**
  - Hire 1 additional lead generator (full-time)
  - Start date: Dec 9, 2025
  - Budget: $1,200/month salary + $200 tools = $1,400/month total

#### Design Team
- **Team Size:** 9 designers
- **Current Capacity:** 80-90% utilized (healthy)
- **Constraints:**
  - Some designers overloaded (Anastasiia leading + individual work)
  - 3 unused Adobe licenses (inefficiency)
- **Hiring Plans:** None (capacity adequate)
- **Optimization:** Reduce Adobe licenses from 10 to 7 (save $165/month)

### Skills & Expertise

#### Advanced React (Performance Optimization, Real-Time Data)
- **Current Team Members:** None at expert level
  - Liliia: Proficient (junior-level React)
  - Yaroslav: Proficient (full-stack, but not React specialist)
- **Skill Level:** Learning (team can build basic React apps, not complex dashboards)
- **Gaps:** Cannot handle Client A project (10K+ data points, real-time updates, complex state management)
- **Development Plans:**
  - **Hiring:** Senior frontend developer (React specialist) starting Jan 6
  - **Training:** Liliia will pair with senior hire (6-month mentorship)
  - **Timeline:** Team will have expert-level React capability by mid-2026

#### Email Campaign Optimization (Data-Driven LG)
- **Current Team Members:**
  - Hanan: Expert (team lead, process development)
  - Nataliia: Proficient (content, A/B testing)
  - Plamena: Proficient (automation)
- **Skill Level:** Strong (October campaign: 35% open rate, 4.2% reply rate - industry-leading)
- **Gaps:** None (team performing well)
- **Development Plans:** Codify knowledge (create template library, document best practices)

### Team Dynamics

**Dev Team: High Collaboration, Heavy Load**
- **Observation:** Dev team is small (3 people) but highly collaborative
  - Olha leads technical decisions; Yaroslav and Liliia implement
  - Code reviews are thorough (high quality), but sometimes slow (bottleneck)
- **Challenge:** Overloaded for next 5 weeks (auth microservice takes full attention)
- **Mitigation:** Implemented round-robin PR reviews (balance load); hiring senior developer (expand capacity)

**LG Team: High Performers, Need Capacity**
- **Observation:** LG team delivered 40% more projects in Q4 (vs Q3)
  - October campaign performance excellent (4.2% reply rate, 12 meetings booked)
  - Team working overtime to meet demand
- **Challenge:** Unsustainable pace (burnout risk)
- **Mitigation:** Hiring additional LG team member (relieve pressure)

**Design Team: Transitioning to New Standards**
- **Observation:** Design team adopting new processes (mobile-first, design system documentation)
  - Some resistance to change expected (designer habits)
  - Anastasiia leading transition (strong leadership)
- **Challenge:** Ensure consistency (all designers follow new mobile-first standard)
- **Mitigation:** Anastasiia reviews projects in progress (enforce standards)

### Performance & Growth

**High Performers Highlighted:**
- **Olha (Dev):** Technical leadership on auth microservice (taking ownership of complex project)
- **Hanan (LG):** October campaign performance (94% improvement over September; data-driven iteration)
- **Nataliia (LG):** Copywriting excellence (subject lines, personalization drove campaign success)

**Growth Opportunities:**
- **Liliia (Dev):** Mentorship from senior hire (advance from junior to mid-level React skills within 6 months)
- **LG Team (New Hire):** Onboarding opportunity for existing team (leadership development for Hanan)

**Areas for Improvement:**
- **Dev Team:** CI/CD pipeline optimization needed (15-20 min builds slowing team down)
- **Design Team:** File organization discipline (Figma workspace messy; new standard will help)

### Hiring & Recruitment

#### Position 1: Senior Frontend Developer (React Specialist)
- **Department:** Dev
- **Reporting To:** Anastasiya (Manager), working closely with Olha (Tech Lead)
- **Status:** Recruitment starting this week (Nov 18)
- **Timeline:**
  - Nov 18-25: Post job ads (LinkedIn, Upwork, React Jobs, AngelList, Remote OK)
  - Nov 25-Dec 20: Interview candidates (target 10-15 qualified applicants)
  - Dec 23: Make offer
  - Jan 6: Start date
- **Requirements:**
  - 5+ years professional React experience
  - Expert: React Hooks, Context API, Redux, TypeScript
  - Performance optimization (handling large datasets, real-time updates)
  - Testing: Jest, React Testing Library
  - Bonus: GraphQL, WebSocket, data visualization (D3.js, Chart.js)
- **Salary Range:** $2,500-3,000/month (negotiable based on experience)
- **Reason for Hire:** Client A project requires advanced React skills (team can't deliver with current skillset)
- **Owner:** Anastasiya (recruitment), Olha (technical interviews)

#### Position 2: Lead Generator (Full-Time)
- **Department:** LG
- **Reporting To:** Hanan Zaheur (LG Team Lead), managed by Anastasiya
- **Status:** Recruitment starting this week (Nov 18)
- **Timeline:**
  - Nov 18-25: Post job ads (Upwork, LinkedIn, internal network)
  - Nov 25-Dec 6: Interview candidates (target 10-15 applicants)
  - Dec 6: Make offer
  - Dec 9: Start date (2-week onboarding)
- **Requirements:**
  - Experience with B2B lead generation
  - Familiarity with Apollo.io, Hunter.io, LinkedIn Sales Navigator (or willingness to learn)
  - Data quality focus (attention to detail)
  - English proficiency (client communication)
- **Salary Range:** $1,200/month + $200 tools/benefits = $1,400/month total
- **Reason for Hire:** Q4 demand increased 40%; team at capacity (working overtime)
- **Owner:** Anastasiya (recruitment), Hanan (interviewing + training)

### Onboarding & Training

**Onboarding Plan: Senior Frontend Developer (Jan 6 start)**
- **Week 1:** Environment setup, codebase walkthrough, meet team
- **Week 2:** Pair programming with Liliia (start small tasks), attend sprint planning
- **Week 3:** Lead first feature (with support), Client A project planning
- **Mentor:** Olha (technical), Liliia (peer buddy)
- **Documentation Needed:** Developer onboarding guide (Yaroslav creating by Dec 15)

**Onboarding Plan: New LG Team Member (Dec 9 start)**
- **Week 1:** Tools training (Apollo, Hunter, LinkedIn Sales Navigator, Phantombuster)
- **Week 2:** Shadow Hanan on lead list project (learn 7-step process)
- **Week 3-4:** Complete first lead list independently (with review)
- **Mentor:** Hanan (primary), Nataliia (copywriting support)
- **Documentation:** LG onboarding materials (Hanan to update)

**Training Needs Identified:**
- **Dev Team:** Docker best practices (Liliia requested, Olha to create guide or host session)
- **Design Team:** Figma Auto Layout advanced techniques (Anastasiia to host 1-hour training for junior designers)
- **LG Team:** LinkedIn Sales Navigator advanced filters (Hanan to complete online course)

### Team Structure Changes

**No Immediate Changes**
- Dev, LG, and Design teams maintain current structure
- Two new hires expand team size (but don't change reporting structure)

**Future Consideration:**
- If dev team grows to 6-8 people, may need to split into sub-teams (frontend team, backend team)
- Not immediate (revisit in 6 months)
```

---

## Validation Checklist

- [ ] **Employee IDs** matched to Employee Directory
- [ ] **Assignments** clearly documented
- [ ] **Workload** assessed accurately
- [ ] **Skills** highlighted appropriately
- [ ] **Action items** assigned to individuals
- [ ] **Team capacity** evaluated
- [ ] **Hiring plans** detailed
- [ ] **Performance** mentioned constructively
- [ ] **Growth opportunities** identified
- [ ] **Team dynamics** observed
- [ ] **Onboarding plans** specified

---

## Related Templates

**Previous:** [15_Analogies_Frameworks.md](15_Analogies_Frameworks.md) - Frameworks
**Next:** [17_Lead_Gen_Sales_Context.md](17_Lead_Gen_Sales_Context.md) - LG/Sales specific
**Reference:** [00_Core/03_Employee_Directory.md](../../00_Core/03_Employee_Directory.md) - Employee source of truth

---

**Status:** ✅ Template ready for use
