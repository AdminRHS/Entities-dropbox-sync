---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_19_Taxonomy_Extraction
title: Video 19 Taxonomy Extraction
date: 2025-11-22
status: draft
owner: unknown
related: []
links: []
---

# Video 19 Taxonomy Extraction

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video_19 - Taxonomy Extraction Document

**Video Title:** The Best Freelance and Remote Hiring Websites
**Processing Date:** 2025-11-22
**Extraction Methodology:** v3.2
**Department Relevance:** HR (Primary), LG, Sales, All Departments (Secondary)

---

## 1. WORKFLOWS IDENTIFIED

### Workflow 1: General Freelance Marketplace Hiring (UpWork/Fiverr Model)
- **Name:** HIRE_FREELANCER_MARKETPLACE
- **Description:** Browse marketplace, post job, review bids, select freelancer, manage project, complete payment
- **Department:** HR, All Departments
- **Tools Used:** UpWork, Fiverr
- **Task Templates:** POST_JOB_LISTING, REVIEW_FREELANCER_PROPOSALS, SELECT_FREELANCER, MANAGE_PROJECT_DELIVERY, PROCESS_PAYMENT
- **Complexity:** Low-Medium
- **Duration:** 1-7 days (hiring), project-dependent (delivery)

### Workflow 2: Pre-Vetted Specialist Hiring (MarketerHire/Revelo/Mayple Model)
- **Name:** HIRE_SPECIALIST_CURATED_PLATFORM
- **Description:** Submit requirements brief, receive curated candidates (AI or human-matched), interview shortlist, select specialist, onboard with platform support
- **Department:** HR, Dev, Sales
- **Tools Used:** MarketerHire, Revelo, Mayple
- **Task Templates:** SUBMIT_HIRING_REQUIREMENTS, REVIEW_CURATED_CANDIDATES, CONDUCT_INTERVIEWS, NEGOTIATE_TERMS, ONBOARD_SPECIALIST
- **Complexity:** Medium
- **Duration:** 2-5 days (matching), ongoing (engagement)

### Workflow 3: Design Contest Model (99designs)
- **Name:** RUN_DESIGN_CONTEST
- **Description:** Create contest brief, set prize amount, review submissions from multiple designers, provide feedback, select winner, receive final files
- **Department:** Design, Sales, HR
- **Tools Used:** 99designs
- **Task Templates:** CREATE_CONTEST_BRIEF, SET_CONTEST_PARAMETERS, REVIEW_DESIGN_SUBMISSIONS, PROVIDE_DESIGNER_FEEDBACK, SELECT_WINNING_DESIGN
- **Complexity:** Medium
- **Duration:** 1-2 weeks

### Workflow 4: Offshore RevOps Talent Hiring (CloudTask Model)
- **Name:** HIRE_OFFSHORE_REVOPS_TALENT
- **Description:** Browse video profiles, filter by skills/location, schedule interviews via platform, assess communication fit, hire with centralized payment processing
- **Department:** Sales, LG
- **Tools Used:** CloudTask
- **Task Templates:** FILTER_CANDIDATE_PROFILES, REVIEW_VIDEO_PROFILES, SCHEDULE_PLATFORM_INTERVIEWS, ASSESS_CANDIDATE_FIT, PROCESS_INTERNATIONAL_PAYMENT
- **Complexity:** Low-Medium
- **Duration:** 1-2 weeks

### Workflow 5: Platform Evaluation and Selection
- **Name:** EVALUATE_FREELANCE_PLATFORMS
- **Description:** Identify hiring needs, research platforms, compare features/pricing, pilot test with small projects, evaluate results, select optimal platform
- **Department:** HR
- **Tools Used:** All 7 platforms (evaluation), comparison matrix, pilot projects
- **Task Templates:** IDENTIFY_HIRING_NEEDS, RESEARCH_PLATFORM_OPTIONS, COMPARE_PLATFORM_FEATURES, CONDUCT_PILOT_TESTS, ANALYZE_PILOT_RESULTS, SELECT_PLATFORM
- **Complexity:** Medium-High
- **Duration:** 1-2 months

---

## 2. TASK TEMPLATES EXTRACTED

### HR Department Tasks

#### TASK-HR-101: POST_JOB_LISTING_MARKETPLACE
- **Description:** Create and post job listing on freelance marketplace with clear requirements, budget, and timeline
- **Department:** HR
- **Tools:** UpWork, Fiverr, 99designs
- **Inputs:** Job requirements, budget, timeline, skill requirements
- **Outputs:** Published job posting, initial applicant pool
- **Complexity:** Low
- **Reusability:** High (any marketplace hiring)
- **Success Criteria:** 5-10 qualified applicants within 48 hours

#### TASK-HR-102: REVIEW_FREELANCER_PROPOSALS
- **Description:** Evaluate freelancer proposals, check portfolios, verify reviews, assess skill fit
- **Department:** HR
- **Tools:** UpWork, Fiverr, Platform rating systems
- **Inputs:** Freelancer proposals, portfolios, ratings, job requirements
- **Outputs:** Shortlist of 3-5 qualified candidates
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** Shortlist includes candidates meeting 80%+ of requirements

#### TASK-HR-103: CONDUCT_FREELANCER_INTERVIEWS
- **Description:** Schedule and conduct interviews with shortlisted freelancers to assess communication, expertise, and cultural fit
- **Department:** HR
- **Tools:** Platform messaging (UpWork, Revelo, MarketerHire), Video conferencing
- **Inputs:** Shortlisted candidates, interview questions, evaluation criteria
- **Outputs:** Interview notes, final candidate selection
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** Clear top candidate identified with 85%+ fit score

#### TASK-HR-104: NEGOTIATE_FREELANCER_TERMS
- **Description:** Negotiate rates, timelines, deliverables, and contract terms with selected freelancer
- **Department:** HR, Department Manager
- **Tools:** Platform messaging, Revelo negotiation support, MarketerHire rate flexibility
- **Inputs:** Initial freelancer quote, budget constraints, project requirements
- **Outputs:** Agreed contract terms, signed agreement
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** Agreement within budget, clear deliverables defined

#### TASK-HR-105: ONBOARD_FREELANCER
- **Description:** Set up freelancer access, share project details, establish communication protocols, define success metrics
- **Department:** HR, Department Manager
- **Tools:** Platform project management (UpWork), Communication tools (Discord, Email)
- **Inputs:** Contract agreement, project brief, access requirements
- **Outputs:** Freelancer ready to start, communication channels established
- **Complexity:** Low-Medium
- **Reusability:** High
- **Success Criteria:** Freelancer starts work within 2-3 days of agreement

#### TASK-HR-106: MANAGE_FREELANCER_PERFORMANCE
- **Description:** Monitor freelancer progress, review deliverables, provide feedback, track time/budget
- **Department:** HR, Department Manager
- **Tools:** UpWork work diary, Platform messaging, Project management tools
- **Inputs:** Project milestones, deliverables, time tracking data
- **Outputs:** Performance reports, feedback to freelancer, course corrections
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** Project on track, 80%+ milestone completion rate

#### TASK-HR-107: EVALUATE_FREELANCER_PLATFORMS
- **Description:** Research and compare freelance platforms based on needs, budget, quality, and use cases
- **Department:** HR
- **Tools:** Platform websites, comparison matrices, pilot test tracking
- **Inputs:** Hiring needs analysis, budget constraints, quality requirements
- **Outputs:** Platform evaluation report, recommendation for primary platforms
- **Complexity:** Medium-High
- **Reusability:** Medium (periodic evaluation)
- **Success Criteria:** 2-3 platforms selected aligned with 90%+ of hiring needs

### Sales/Marketing Tasks

#### TASK-SALES-101: HIRE_SMM_FREELANCER
- **Description:** Hire social media manager or content creator via MarketerHire or Fiverr
- **Department:** Sales
- **Tools:** MarketerHire, Fiverr
- **Inputs:** SMM requirements, budget ($3K-$8K/month or $500-$1.5K/month), content strategy
- **Outputs:** Hired SMM specialist, content calendar established
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** SMM specialist onboarded within 1 week, content plan approved

#### TASK-SALES-102: HIRE_EMAIL_MARKETER
- **Description:** Hire email marketing specialist for campaign creation and automation
- **Department:** Sales
- **Tools:** MarketerHire, UpWork
- **Inputs:** Email marketing goals, budget, current email list, CRM details
- **Outputs:** Hired email marketer, campaign strategy, automation setup
- **Complexity:** Medium
- **Reusability:** High
- **Success Criteria:** First campaign launched within 2 weeks

#### TASK-SALES-103: HIRE_REVOPS_SUPPORT
- **Description:** Hire offshore RevOps talent for CRM management, pipeline reporting, or sales operations
- **Department:** Sales, LG
- **Tools:** CloudTask, UpWork
- **Inputs:** RevOps requirements, budget ($15-$40/hour), time zone preferences
- **Outputs:** Hired RevOps specialist, CRM processes optimized
- **Complexity:** Medium
- **Reusability:** Medium
- **Success Criteria:** RevOps support starts within 2 weeks, CRM reporting improved

### Design Department Tasks

#### TASK-DESIGN-101: RUN_LOGO_DESIGN_CONTEST
- **Description:** Launch design contest on 99designs to generate multiple logo options
- **Department:** Design
- **Tools:** 99designs
- **Inputs:** Brand brief, logo requirements, contest budget ($299-$1,299)
- **Outputs:** 10-20 logo submissions, selected final logo
- **Complexity:** Medium
- **Reusability:** High (per client project)
- **Success Criteria:** 5+ high-quality submissions, client-approved final logo

#### TASK-DESIGN-102: OUTSOURCE_OVERFLOW_DESIGN_WORK
- **Description:** Hire freelance designers for overflow work during peak periods
- **Department:** Design
- **Tools:** 99designs, Fiverr, UpWork
- **Inputs:** Design requirements, urgency, budget, design team capacity
- **Outputs:** Completed design deliverables, client deadlines met
- **Complexity:** Low-Medium
- **Reusability:** High
- **Success Criteria:** Deliverables on time, quality matches in-house standards

### Dev Department Tasks

#### TASK-DEV-101: HIRE_PROJECT_DEVELOPER
- **Description:** Hire additional developers for large projects via Revelo or UpWork
- **Department:** Dev
- **Tools:** Revelo, UpWork
- **Inputs:** Technical requirements, project scope, budget ($30-$70/hour Revelo, $25-$50/hour UpWork), timeline
- **Outputs:** Onboarded developer, development work started
- **Complexity:** Medium-High
- **Reusability:** Medium
- **Success Criteria:** Developer onboarded within 1 week, code quality meets standards

#### TASK-DEV-102: HIRE_SPECIALIZED_DEVELOPER
- **Description:** Hire specialist for niche technologies (blockchain, ML, etc.) not available in-house
- **Department:** Dev
- **Tools:** UpWork, Revelo
- **Inputs:** Specialized skill requirements, project scope, budget ($40-$100/hour)
- **Outputs:** Specialist hired, technical challenge resolved
- **Complexity:** High
- **Reusability:** Low (niche needs)
- **Success Criteria:** Specialist delivers solution within project timeline

### LG Department Tasks

#### TASK-LG-101: OUTSOURCE_LEAD_RESEARCH
- **Description:** Hire freelance lead researchers to build lead lists via UpWork or CloudTask
- **Department:** LG
- **Tools:** UpWork, CloudTask
- **Inputs:** Lead criteria (industry, location, company size), budget, quantity target
- **Outputs:** Curated lead list, contact details, initial qualification
- **Complexity:** Low-Medium
- **Reusability:** High
- **Success Criteria:** Lead list meets quality standards (80%+ valid contacts)

#### TASK-LG-102: EVALUATE_FREELANCE_VS_INHOUSE
- **Description:** Pilot test freelance lead generation vs. in-house team performance and cost
- **Department:** LG, HR
- **Tools:** UpWork, CloudTask, Performance tracking tools
- **Inputs:** In-house LG metrics (cost, appointments, conversion), pilot budget ($1K-$2K)
- **Outputs:** Comparison report, cost-benefit analysis, strategic recommendation
- **Complexity:** High
- **Reusability:** Low (strategic decision)
- **Success Criteria:** Clear data on freelance vs. in-house ROI, decision made

---

## 3. STEP TEMPLATES EXTRACTED

### Marketplace Hiring Steps

#### STEP-HR-101-01: CREATE_JOB_POSTING
- **Action:** CREATE
- **Object:** JOB_POSTING
- **Detail:** Draft clear job title, requirements, deliverables, budget, timeline
- **Tool:** UpWork, Fiverr (posting interface)
- **Success Criteria:** Job posting includes all required details, clear scope
- **Validation:** Job posting reviewed by hiring manager

#### STEP-HR-101-02: PUBLISH_JOB_TO_MARKETPLACE
- **Action:** PUBLISH
- **Object:** JOB_POSTING
- **Detail:** Post job on selected platform, set visibility and budget parameters
- **Tool:** UpWork, Fiverr
- **Success Criteria:** Job goes live on platform, visible to freelancers
- **Validation:** Confirm job posting appears in search results

#### STEP-HR-102-01: REVIEW_FREELANCER_PORTFOLIO
- **Action:** REVIEW
- **Object:** FREELANCER_PORTFOLIO
- **Detail:** Examine work samples, past projects, client feedback
- **Tool:** UpWork, Fiverr (profile pages)
- **Success Criteria:** Portfolio matches job requirements (80%+ relevance)
- **Validation:** Portfolio includes 3+ relevant work samples

#### STEP-HR-102-02: CHECK_FREELANCER_RATINGS
- **Action:** CHECK
- **Object:** FREELANCER_RATINGS
- **Detail:** Review job success score, client reviews, total earnings, hours worked
- **Tool:** UpWork ratings, Fiverr seller levels
- **Success Criteria:** Freelancer has 4.5+ rating, 90%+ job success score
- **Validation:** Minimum 10 completed jobs with positive reviews

#### STEP-HR-102-03: VERIFY_FREELANCER_SKILLS
- **Action:** VERIFY
- **Object:** FREELANCER_SKILLS
- **Detail:** Confirm freelancer has required technical and soft skills
- **Tool:** Platform skill tests, portfolio review
- **Success Criteria:** Skills match 80%+ of job requirements
- **Validation:** Freelancer passed relevant skill assessments

#### STEP-HR-103-01: SCHEDULE_FREELANCER_INTERVIEW
- **Action:** SCHEDULE
- **Object:** FREELANCER_INTERVIEW
- **Detail:** Use platform messaging to set up video or text interview
- **Tool:** UpWork messaging, Platform video tools
- **Success Criteria:** Interview scheduled within 48 hours of shortlisting
- **Validation:** Confirmed interview time with freelancer

#### STEP-HR-103-02: CONDUCT_INTERVIEW
- **Action:** CONDUCT
- **Object:** INTERVIEW
- **Detail:** Ask questions about experience, approach, communication style, availability
- **Tool:** Video conferencing, Platform messaging
- **Success Criteria:** Clear understanding of freelancer capabilities and fit
- **Validation:** Interview notes documented, fit score assigned

#### STEP-HR-104-01: PROPOSE_CONTRACT_TERMS
- **Action:** PROPOSE
- **Object:** CONTRACT_TERMS
- **Detail:** Send initial contract terms (rate, timeline, deliverables, milestones)
- **Tool:** Platform contract tools (UpWork, Revelo)
- **Success Criteria:** Terms align with budget and project scope
- **Validation:** Terms reviewed by department manager

#### STEP-HR-104-02: NEGOTIATE_RATES
- **Action:** NEGOTIATE
- **Object:** RATES
- **Detail:** Discuss hourly or project rates, adjust based on scope or volume
- **Tool:** Platform messaging, Revelo negotiation support
- **Success Criteria:** Agreement reached within budget constraints
- **Validation:** Final rate confirmed in writing

#### STEP-HR-105-01: GRANT_PROJECT_ACCESS
- **Action:** GRANT
- **Object:** PROJECT_ACCESS
- **Detail:** Provide freelancer with necessary tools, files, credentials
- **Tool:** File sharing, Access management tools
- **Success Criteria:** Freelancer has all required access to start work
- **Validation:** Freelancer confirms access and readiness

#### STEP-HR-105-02: ESTABLISH_COMMUNICATION_PROTOCOL
- **Action:** ESTABLISH
- **Object:** COMMUNICATION_PROTOCOL
- **Detail:** Define check-in frequency, reporting format, primary communication channel
- **Tool:** Discord, Email, Platform messaging
- **Success Criteria:** Clear communication expectations set
- **Validation:** Freelancer acknowledges and agrees to protocol

### Pre-Vetted Specialist Hiring Steps

#### STEP-HR-201-01: SUBMIT_REQUIREMENTS_BRIEF
- **Action:** SUBMIT
- **Object:** REQUIREMENTS_BRIEF
- **Detail:** Complete detailed brief with hiring needs, budget, timeline, success metrics
- **Tool:** MarketerHire, Mayple, Revelo (platform forms)
- **Success Criteria:** Brief includes all required information
- **Validation:** Platform confirms brief received and processing

#### STEP-HR-201-02: REVIEW_CURATED_SHORTLIST
- **Action:** REVIEW
- **Object:** CURATED_SHORTLIST
- **Detail:** Examine AI-matched or hand-picked candidates (within 48 hours to 5 days)
- **Tool:** MarketerHire, Mayple, Revelo (candidate profiles)
- **Success Criteria:** Shortlist includes 3-5 candidates matching 80%+ requirements
- **Validation:** Platform provides candidate matching rationale

#### STEP-HR-201-03: INTERVIEW_SHORTLISTED_CANDIDATES
- **Action:** INTERVIEW
- **Object:** SHORTLISTED_CANDIDATES
- **Detail:** Schedule and conduct interviews via platform
- **Tool:** Platform interview scheduling, Video conferencing
- **Success Criteria:** All shortlisted candidates interviewed within 1 week
- **Validation:** Interview scores documented for comparison

#### STEP-HR-201-04: SELECT_SPECIALIST
- **Action:** SELECT
- **Object:** SPECIALIST
- **Detail:** Choose best-fit candidate based on interview performance and requirements match
- **Tool:** Decision matrix, Platform selection interface
- **Success Criteria:** Selected candidate meets 90%+ requirements
- **Validation:** Selection confirmed with platform and candidate

### Design Contest Steps

#### STEP-DESIGN-301-01: CREATE_CONTEST_BRIEF
- **Action:** CREATE
- **Object:** CONTEST_BRIEF
- **Detail:** Write detailed design brief with brand guidelines, target audience, preferences, examples
- **Tool:** 99designs contest creation tool
- **Success Criteria:** Brief provides clear direction to designers
- **Validation:** Brief reviewed by creative director

#### STEP-DESIGN-301-02: SET_CONTEST_PARAMETERS
- **Action:** SET
- **Object:** CONTEST_PARAMETERS
- **Detail:** Define contest prize ($299-$1,299), timeline (1-2 weeks), number of finalists
- **Tool:** 99designs platform
- **Success Criteria:** Parameters align with budget and timeline
- **Validation:** Contest launched successfully

#### STEP-DESIGN-301-03: REVIEW_DESIGN_SUBMISSIONS
- **Action:** REVIEW
- **Object:** DESIGN_SUBMISSIONS
- **Detail:** Evaluate submissions from multiple designers, rate and provide feedback
- **Tool:** 99designs review interface
- **Success Criteria:** 10+ submissions received, 3-5 meet requirements
- **Validation:** Feedback provided to designers for revisions

#### STEP-DESIGN-301-04: SELECT_WINNING_DESIGN
- **Action:** SELECT
- **Object:** WINNING_DESIGN
- **Detail:** Choose final design, award prize, receive final files
- **Tool:** 99designs selection interface
- **Success Criteria:** Winning design meets 90%+ of brief requirements
- **Validation:** Final files received in required formats

### RevOps Hiring Steps

#### STEP-SALES-401-01: FILTER_VIDEO_PROFILES
- **Action:** FILTER
- **Object:** VIDEO_PROFILES
- **Detail:** Search and filter 500+ video profiles by skills, experience, location
- **Tool:** CloudTask platform search
- **Success Criteria:** 10-15 profiles match requirements
- **Validation:** Shortlisted profiles meet skill criteria

#### STEP-SALES-401-02: REVIEW_VIDEO_PROFILES
- **Action:** REVIEW
- **Object:** VIDEO_PROFILES
- **Detail:** Watch candidate videos to assess communication, personality, expertise
- **Tool:** CloudTask video player
- **Success Criteria:** 3-5 candidates show strong communication and fit
- **Validation:** Video review notes documented

#### STEP-SALES-401-03: SCHEDULE_INTERVIEWS_VIA_PLATFORM
- **Action:** SCHEDULE
- **Object:** INTERVIEWS
- **Detail:** Use CloudTask platform to schedule interviews with shortlisted candidates
- **Tool:** CloudTask interview scheduler
- **Success Criteria:** Interviews scheduled within 1 week
- **Validation:** Candidates confirm interview times

---

## 4. SKILLS IDENTIFIED

### skill: freelancer vetting
- **Definition:** Ability to evaluate freelancer profiles, portfolios, ratings, and proposals to identify quality candidates
- **Tools Used:** UpWork, Fiverr, 99designs (rating systems, portfolios)
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** REVIEW_FREELANCER_PROPOSALS, CHECK_FREELANCER_RATINGS, VERIFY_FREELANCER_SKILLS
- **Departments:** HR, All Department Managers

### skill: remote hiring
- **Definition:** Capability to hire, onboard, and manage remote freelancers or contractors across platforms
- **Tools Used:** UpWork, Fiverr, Revelo, MarketerHire, Mayple, CloudTask, 99designs
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** HIRE_FREELANCER_MARKETPLACE, HIRE_SPECIALIST_CURATED_PLATFORM, ONBOARD_FREELANCER
- **Departments:** HR, All Department Managers

### skill: platform evaluation
- **Definition:** Skill in researching, comparing, and selecting optimal platforms for specific needs
- **Tools Used:** Platform comparison matrices, Pilot test tracking
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** EVALUATE_FREELANCE_PLATFORMS, COMPARE_PLATFORM_FEATURES
- **Departments:** HR, Department Managers

### skill: contract negotiation
- **Definition:** Ability to negotiate rates, timelines, deliverables, and contract terms with freelancers
- **Tools Used:** Platform messaging, Revelo negotiation support
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** NEGOTIATE_FREELANCER_TERMS, PROPOSE_CONTRACT_TERMS
- **Departments:** HR, Department Managers

### skill: freelancer performance management
- **Definition:** Capability to monitor freelancer progress, provide feedback, and ensure deliverable quality
- **Tools Used:** UpWork work diary, Platform messaging, Project management tools
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** MANAGE_FREELANCER_PERFORMANCE, REVIEW_DESIGN_SUBMISSIONS
- **Departments:** HR, All Department Managers

### skill: offshore team management
- **Definition:** Ability to manage offshore/international freelancers, navigate time zones, and handle international payments
- **Tools Used:** CloudTask, Revelo, UpWork (international features)
- **Proficiency Levels:** Intermediate → Advanced
- **Linked Tasks:** HIRE_OFFSHORE_REVOPS_TALENT, PROCESS_INTERNATIONAL_PAYMENT
- **Departments:** HR, Sales, LG

### skill: design brief writing
- **Definition:** Skill in creating clear, comprehensive design briefs for contests or freelance projects
- **Tools Used:** 99designs, Written communication tools
- **Proficiency Levels:** Beginner → Intermediate → Advanced
- **Linked Tasks:** CREATE_CONTEST_BRIEF, CREATE_JOB_POSTING
- **Departments:** Design, Sales, HR

---

## 5. TOOLS IDENTIFIED (7 Freelance Platforms)

### Tool 1: UpWork
- **Vendor:** UpWork Inc.
- **Category:** Freelance Marketplace / General
- **Purpose:** Hire freelancers across all categories (marketing, development, design, writing, data science)
- **Key Features:** Millions of freelancers, detailed profiles, work management tools, payment protection, 5% client fee
- **Pricing:** 5% transaction fee for clients
- **Target Use Case:** Diverse hiring needs, budget-conscious, short and long-term contracts
- **Departments:** HR, All Departments
- **Status:** NEW (to be added to LIBRARIES)

### Tool 2: Fiverr
- **Vendor:** Fiverr International Ltd.
- **Category:** Freelance Marketplace / Service Marketplace
- **Purpose:** Affordable freelance services starting at $5 across 200+ categories
- **Key Features:** Low starting prices, seller rating system (New → Top Rated), Fiverr Pro for vetted talent, fast delivery
- **Pricing:** 5.5% transaction fee + small order fee (<$75)
- **Target Use Case:** Quick tasks, small budgets ($5-$500), one-off projects
- **Departments:** Design, Video, AI, Sales, HR
- **Status:** NEW (to be added to LIBRARIES)

### Tool 3: Revelo
- **Vendor:** Revelo Inc.
- **Category:** Specialized Talent Platform / Software Development
- **Purpose:** Hire pre-vetted, English-speaking remote software developers from Latin America
- **Key Features:** 300K+ vetted developers, 3-5 day matching, same U.S. time zone, end-to-end support (payroll, benefits, taxes), 14-day guarantee
- **Pricing:** Custom quotes (estimated $30-$70/hour)
- **Target Use Case:** Long-term developer hires, dedicated development team, same time zone required
- **Departments:** Dev, AI
- **Status:** NEW (to be added to LIBRARIES)

### Tool 4: MarketerHire
- **Vendor:** MarketerHire Inc.
- **Category:** Specialized Talent Platform / Marketing
- **Purpose:** Connect businesses with pre-vetted top-tier marketing talent
- **Key Features:** Rigorous vetting, 48-hour matching, $80-$160/hour specialists, no upfront fees, $1.5K/month minimum
- **Pricing:** $80-$160/hour (freelancer-set), $1,500/month soft commitment
- **Target Use Case:** High-quality marketing expertise, SMM, email, SEO, paid ads
- **Departments:** Sales, Marketing (if exists)
- **Status:** NEW (to be added to LIBRARIES)

### Tool 5: Mayple
- **Vendor:** Mayple Ltd.
- **Category:** Specialized Talent Platform / Marketing (AI-Powered)
- **Purpose:** AI-powered matching with expert marketers for medium/large businesses
- **Key Features:** 600+ vetted marketers, AI matching, dedicated account manager, 3-month minimum, live campaign monitoring
- **Pricing:** Premium (estimated $5K-$15K+/month)
- **Target Use Case:** Long-term marketing strategy, established budgets, agency-like service
- **Departments:** Sales, Marketing (if scaling)
- **Status:** NEW (to be added to LIBRARIES)

### Tool 6: 99designs
- **Vendor:** 99designs (Vistaprint company)
- **Category:** Specialized Marketplace / Design
- **Purpose:** Design-focused marketplace specializing in logos, branding, book covers, websites
- **Key Features:** 90+ design categories, design contests, curated designer matching, money-back guarantee
- **Pricing:** Project-based ($100-$5,000+), contests ($299-$1,299)
- **Target Use Case:** Creative projects, logo contests, branding, design overflow work
- **Departments:** Design, Sales, HR
- **Status:** NEW (to be added to LIBRARIES)

### Tool 7: CloudTask
- **Vendor:** CloudTask Inc.
- **Category:** Specialized Talent Platform / RevOps
- **Purpose:** Hire offshore remote talent for revenue operations roles
- **Key Features:** 500+ video profiles, RevOps specialization, centralized search/interview/payment, international hiring simplified
- **Pricing:** Variable (estimated $15-$40/hour)
- **Target Use Case:** RevOps support (sales ops, marketing ops, customer success ops), offshore talent
- **Departments:** Sales, LG
- **Status:** NEW (to be added to LIBRARIES)

---

## 6. OBJECTS IDENTIFIED

### Primary Objects
- **freelancer** - Individual contractor offering services on platforms
- **job_posting** - Published hiring request on marketplace
- **proposal** - Freelancer application/bid for job
- **portfolio** - Collection of freelancer work samples
- **rating** - Freelancer performance score/reviews
- **contract** - Agreement between client and freelancer
- **deliverable** - Work output from freelancer
- **payment** - Compensation for completed work
- **contest** - Design competition with prize
- **brief** - Detailed project/hiring requirements document
- **shortlist** - Curated list of top candidates
- **video_profile** - Video introduction of candidate (CloudTask)
- **specialist** - Pre-vetted expert in specific domain

### Supporting Objects
- **platform** - Freelance marketplace or hiring service
- **requirements** - Job/project specifications
- **timeline** - Project schedule
- **budget** - Financial allocation for hiring
- **milestone** - Project checkpoint
- **feedback** - Performance review or design critique
- **revision** - Updated/corrected deliverable

---

## 7. REMOTE HELPERS STRATEGIC INSIGHTS

### Critical Decision Point: LG Department
- **Current Model:** 11 in-house employees, $5,000/month cost, declining appointments
- **Alternative Model:** Freelance platforms (UpWork, CloudTask)
- **Estimated Freelance Cost:** $2,000-$3,500/month (variable)
- **Potential Savings:** $1,500-$3,000/month ($18K-$36K annually)
- **Recommendation:** Pilot test freelance model for 2-3 months before decision

### Platform Recommendations by Department

**HR (Primary):**
- **Primary Platform:** UpWork (versatile, budget-friendly, all categories)
- **Secondary Platform:** Fiverr (quick tasks, low budget)
- **Use Case:** Recruitment support, HR automation, job posting copywriting

**Sales:**
- **Primary Platform:** MarketerHire (pre-vetted marketing specialists)
- **Secondary Platform:** Fiverr (content creation, quick SMM tasks)
- **Use Case:** Part-time SMM manager, email marketer, content creator

**Design:**
- **Primary Platform:** 99designs (design contests, overflow work)
- **Secondary Platform:** Fiverr (quick graphics, thumbnails)
- **Use Case:** Logo contests, branding projects, peak period overflow

**Dev:**
- **Primary Platform:** Revelo (pre-vetted developers, same time zone)
- **Secondary Platform:** UpWork (project-based developers)
- **Use Case:** Large project scaling, specialized technical skills

**LG:**
- **Primary Platform:** UpWork (lead researchers, data specialists)
- **Secondary Platform:** CloudTask (RevOps support)
- **Use Case:** Outsourced lead research, alternative to in-house team

**Video:**
- **Primary Platform:** Fiverr (voice-over, video editing)
- **Secondary Platform:** UpWork (additional editors during peak)
- **Use Case:** Voice-over recordings, graphic design support, overflow editing

**AI:**
- **Primary Platform:** UpWork (prompt engineers, AI/ML developers)
- **Use Case:** Specialized AI projects, AI tool research

### Implementation Roadmap
1. **Phase 1 (Week 1-2):** Platform evaluation, create accounts, identify pilot projects
2. **Phase 2 (Week 3-6):** Pilot test UpWork and Fiverr with small projects ($100-$300)
3. **Phase 3 (Month 2-3):** Evaluate pilot results, create SOPs, train team
4. **Phase 4 (Month 3-6):** Strategic decisions (LG department, platform standardization, budget allocation)

---

## 8. GAP ANALYSIS PREVIEW

### Tools Not in Current LIBRARIES
- All 7 platforms are NEW (UpWork, Fiverr, Revelo, MarketerHire, Mayple, 99designs, CloudTask)
- Need to add to LBS_003_Tools with proper categorization

### Missing Integration Points
- Integration between freelance platforms and Remote Helpers' project management tools
- Automated tracking of freelancer costs across departments
- Centralized freelancer performance database

### Process Gaps
- No formal SOP for freelance hiring
- No vetting checklist for freelancers
- No approval workflow for freelance budgets
- No standardized freelancer onboarding process

### Knowledge Gaps
- Team unfamiliarity with freelance platforms (training needed)
- No documented best practices for platform selection
- Limited experience with offshore team management

---

## 9. NEXT STEPS

1. ✅ **Taxonomy Extraction Complete** - This document
2. ⏭️ **Validate Extracted Data** - Review naming conventions, ensure v3.2 compliance
3. ⏭️ **Create Tool Entries** - Add 7 platforms to LBS_003_Tools
4. ⏭️ **Update Mappings** - Link tools to task templates, skills, departments
5. ⏭️ **Generate Full Gap Analysis** - Detailed report with action items

---

**Extraction Completed:** 2025-11-22
**Extracted By:** Claude Sonnet 4.5
**Methodology Version:** v3.2
**Total Tools Identified:** 7 (all new)
**Total Task Templates:** 15
**Total Step Templates:** 20
**Total Skills:** 7
**Total Workflows:** 5

---

**Document Status:** READY FOR VALIDATION


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-22 standardization scaffold added
