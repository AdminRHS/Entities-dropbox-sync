# Template 18: Design & Creative Context

**Purpose:** Track design-specific discussions, creative work, and visual projects
**Library Integration:** ⭐⭐⭐ Heavy (Design tools, processes, deliverables, parameters)
**Priority:** Include when design projects, creative decisions, or visual work discussed

---

## Template

```markdown
## Design & Creative Context

**Projects Discussed:** [Number]
**Design Decisions:** [Number]
**Creative Assets:** [Number]
**Quality Standards:** [Discussed standards]

### Design Projects

#### [Project/Client Name]
- **Project Type:** [UI/UX | Brand Identity | Social Graphics | Web Design | Mobile App]
- **Client:** [Client name]
- **Deliverables:** [What's being created]
- **Designer(s):** [Who's working on this]
- **Timeline:** [Start - End dates]
- **Status:** [In Progress | Review | Completed]
- **Design Approach:** [Strategy, style, methodology]
- **Tools Used:** [TOOL-DESIGN-XXX from Tools library]
- **Quality Target:** [Standard being applied]
- **Next Steps:** [Actions needed]

### Design Standards & Quality

#### [Standard/Guideline]
- **Standard:** [What the standard is]
- **Application:** [When/how to apply]
- **Quality Bar:** [Minimum threshold]
- **Examples:** [Good vs bad examples]

### Creative Decisions

#### [Decision Title]
- **Decision:** [What was decided]
- **Context:** [Why this decision was needed]
- **Options Considered:** [Alternatives]
- **Rationale:** [Why this choice]
- **Impact:** [How this affects work]

### Design System & Components

[Component library, design system updates, style guides]

### Portfolio & Showcasing

[Dribbble, Behance, portfolio work]

### Client Feedback & Revisions

[Client input, revision rounds, approval status]

### Design Process Improvements

[Workflow optimizations, new techniques]
```

---

## Examples

```markdown
## Design & Creative Context

**Projects Discussed:** 2
**Design Decisions:** 3
**Creative Assets:** Dribbble portfolio
**Quality Standards:** 8/10 minimum, 3 revision limit, mobile-first

### Design Projects

#### Client B - E-commerce Website Redesign
- **Project Type:** Web Design (UI/UX, responsive)
- **Client:** Client B (e-commerce company)
- **Deliverables:**
  - Homepage redesign (desktop 1440px, tablet 768px, mobile 375px)
  - Product page template
  - Checkout flow (4 steps)
  - Design system components
- **Designer(s):** Olha (lead), Solomia (supporting)
- **Timeline:** Nov 11 - Dec 6 (4 weeks)
- **Status:** In Progress (Week 2 - wireframes complete, moving to visual design)
- **Design Approach:**
  - **NEW: Mobile-first** (as of Nov 15 decision)
  - Started with mobile wireframes (375px)
  - Now scaling up to tablet and desktop
  - E-commerce best practices (prominent CTAs, trust signals, simplified checkout)
- **Tools Used:**
  - TOOL-DESIGN-001: Figma (primary design tool)
  - TOOL-DESIGN-002: Adobe Photoshop (product image editing)
- **Quality Target:**
  - 8/10 minimum quality standard (self-assessment before client delivery)
  - Maximum 3 revision rounds (communicated to client at kickoff)
- **Client Feedback:**
  - Wireframes approved with minor changes (1 revision round used)
  - 2 revision rounds remaining for visual design
- **Next Steps:**
  - Olha: Complete visual design for mobile (by Nov 22)
  - Olha: Scale to tablet and desktop (by Nov 29)
  - Solomia: Build component library in Figma (reusable elements)
  - Client review scheduled: Dec 2

#### Internal - Design System Documentation
- **Project Type:** Documentation (internal)
- **Client:** Internal (design team resource)
- **Deliverables:**
  - Component catalog (50+ components with screenshots)
  - Usage guidelines (when to use each component)
  - Typography scale, color palette, spacing rules
  - Accessibility guidelines
  - Do's and Don'ts examples
- **Designer(s):** Anastasiia (lead)
- **Timeline:** Nov 18 - Dec 15 (4 weeks)
- **Status:** Starting this week (Week 1)
- **Design Approach:**
  - Document existing design system (built over last 6 months)
  - Prioritize top 20 most-used components first
  - Visual documentation (Figma Community file) + written guidelines (Notion)
- **Tools Used:**
  - TOOL-DESIGN-001: Figma (component library lives here)
  - Notion (written guidelines)
- **Quality Target:** Comprehensive enough that new designers can use design system without asking questions
- **Next Steps:**
  - Anastasiia: Document top 20 components (Week 1-2, Nov 18-29)
  - Anastasiia: Document next 20 components (Week 3, Dec 2-6)
  - Anastasiia: Finalize guidelines and examples (Week 4, Dec 9-13)
  - Team review: Dec 15

### Design Standards & Quality

#### Quality Standard: 8/10 Minimum for Client Deliverables
- **Standard:** All client-facing designs must meet 8/10 quality threshold (self-assessment against checklist)
- **Application:**
  - Before submitting to client, designer self-assesses design
  - Checklist: Alignment (perfect), Typography (consistent), Spacing (clean), Brand consistency (on-brand), Polish (professional)
  - If <8/10, revise before sending to client
  - Peer review available if unsure (ask another designer to review)
- **Quality Bar:** 8/10 minimum (1-10 scale)
- **Examples:**
  - ✅ 9/10: Landing page with perfect alignment, custom graphics, polished interactions, brand-consistent colors
  - ❌ 6/10: Social graphics with misaligned text, generic stock photos, inconsistent fonts (requires revision)
- **Enforcement:** Anastasiia reviews projects at in-progress check-ins (catches issues early)
- **Reason:** Recent quality inconsistencies; client feedback indicated some work felt rushed

#### Revision Limit: Maximum 3 Rounds per Project Phase
- **Standard:** Maximum 3 revision rounds per project phase (communicate to client at kickoff)
- **Application:**
  - At project kickoff, communicate: "We include 3 revision rounds in the project scope"
  - After 3 rounds, additional revisions billed separately (or scope creep addressed)
  - Project manager (or designer if direct client) enforces
- **Quality Bar:** Complete project within 3 rounds (requires clear communication upfront)
- **Examples:**
  - ✅ Round 1 (initial), Round 2 (minor changes), Round 3 (final polish) → Approved
  - ❌ Round 1, 2, 3, 4, 5, 6, 7 (client keeps changing mind) → Should have stopped at Round 3
- **Reason:** Recent project had 7 revision rounds (scope creep, unpaid work)
- **Context:** Industry standard is 2-3 rounds; Remote Helpers aligning with this

#### Mobile-First Design: All Responsive Projects Start with Mobile (375px)
- **Standard:** All responsive web projects must start with mobile wireframes (375px), then scale up to tablet (768px) and desktop (1440px)
- **Application:**
  - Step 1: Design mobile wireframes (375px)
  - Step 2: Scale to tablet (768px) - adapt layout for more space
  - Step 3: Scale to desktop (1440px) - full layout
  - Exception: Desktop-only applications (e.g., internal admin dashboards)
- **Quality Bar:** 100% compliance for all new responsive projects (starting Nov 18)
- **Examples:**
  - ✅ Good: Wireframe mobile (375px) → Tablet (768px) → Desktop (1440px)
  - ❌ Bad: Design desktop first, then "squeeze" into mobile → Poor mobile UX
- **Rationale:** Mobile usage >60% for most clients; mobile-first ensures better mobile UX (instead of desktop designs poorly adapted to mobile)
- **Enforcement:** Anastasiia reviews projects during wireframe stage (ensures mobile-first approach)
- **Effective:** Immediately (all new projects starting Nov 18+)

### Creative Decisions

#### Decision: Mobile-First Design Standard (MAJOR SHIFT)
- **Decision:** All new responsive web projects will be designed mobile-first (375px → 768px → 1440px)
- **Context:** Recent projects had poor mobile UX (desktop designs poorly adapted to mobile); mobile usage >60% for most clients
- **Options Considered:**
  1. Continue desktop-first (rejected - leads to poor mobile UX)
  2. Mobile-first for all projects (CHOSEN - better UX, matches user behavior)
  3. Designer choice (rejected - inconsistent results)
- **Rationale:** Designing for constraints first (mobile) forces prioritization; easier to expand to desktop than to compress desktop to mobile
- **Impact:**
  - **Team:** Workflow change (designers need to adjust mindset)
  - **Clients:** Better mobile UX (higher user satisfaction, better conversion rates)
  - **Timeline:** Minimal impact (design time similar, just different order)
- **Implementation:** Effective immediately (Nov 18+); Anastasiia enforces in project reviews
- **Status:** New standard (team agreed)

#### Decision: Design Quality Minimum 8/10
- **Decision:** Formalize quality standard (8/10 minimum for client deliverables)
- **Context:** Recent quality inconsistencies; some work felt rushed
- **Options Considered:**
  1. No formal threshold (rejected - too subjective)
  2. 8/10 minimum (CHOSEN - objective standard, high but achievable)
  3. 9/10 minimum (rejected - too high, would slow down delivery)
- **Rationale:** Need objective standard to maintain consistency; 8/10 is high quality but realistic for deadlines
- **Impact:** Improved client satisfaction; reduced rework (catch issues before client sees them)
- **Implementation:** Immediate (applies to all active projects)

#### Decision: Reduce Adobe CC Licenses (Cost Optimization)
- **Decision:** Reduce Adobe Creative Cloud licenses from 10 to 7 (cancel 3 unused seats)
- **Context:** Only 7 of 10 designers actively use Adobe (3 are Figma-only); wasting $165/month
- **Options Considered:**
  1. Keep all 10 licenses (rejected - waste of money)
  2. Reduce to 7 licenses (CHOSEN - right-size to actual usage)
  3. Cancel all Adobe, Figma-only (rejected - some designers need Adobe for specific work)
- **Rationale:** Cost savings ($1,980/year) without affecting team capability
- **Impact:** $165/month savings; no negative impact (unused licenses canceled)
- **Implementation:** Olha to audit usage and cancel 3 seats by end of November

### Design System & Components

**Design System Status:**
- **Current:** 50+ components in Figma library (buttons, forms, cards, navigation, etc.)
- **Issue:** Minimal documentation (designers don't know when to use which component)
- **Solution:** Anastasiia creating comprehensive documentation (4-week project, Dec 15 completion)
- **Goal:** 100% design system compliance (no custom components without approval)
- **Enforcement:** Anastasiia reviews projects; flags custom components

**Component Updates:**
- Design system version notifications: Slack channel #design-system (Anastasiia posts when components updated)
- Version control: Major changes get version number (e.g., Design System v2.1)

**Usage Issues Identified:**
- Recent projects used custom components instead of design system (inconsistent UI, maintenance burden)
- Root cause: Designers didn't know design system had the component they needed (documentation gap)
- Solution: Documentation + training (Anastasiia hosting training on Figma Auto Layout advanced techniques)

### Portfolio & Showcasing

#### Dribbble Posting Strategy (Team Portfolio)
- **Goal:** Post 2 shots per week (Tuesdays and Thursdays, 2-3 PM optimal engagement)
- **Quality Bar:** Only post work rated 9/10 or higher (maintain high standard)
- **Content:** Real client work (with permission) or personal projects
- **Purpose:**
  - Maintain agency presence (visibility in design community)
  - Attract design talent (showcase capabilities for recruitment)
  - Client lead generation (potential clients discover Remote Helpers through Dribbble)
- **Schedule:** Rotating weekly (each designer posts on assigned weeks)
- **This Week:** Iuliia posting 2 shots (Client A landing page + Client B social graphics)
- **Tracking:** Track engagement (likes, views, comments) to understand what resonates

**Portfolio Management:**
- Keep Dribbble updated (2 shots/week maintains momentum)
- Link from Remote Helpers website (drive traffic to portfolio)
- Tag work appropriately (increase discoverability)

### Client Feedback & Revisions

#### Client Feedback SLA: 48 Hours
- **Standard:** Request client feedback with 48-hour expected response time (set expectation upfront)
- **Communication:** At project kickoff and in feedback request emails
  - Example: "Please review by Friday EOD (48 hours) to keep project on schedule"
- **Follow-up:** If no response in 48 hours, send reminder; if >72 hours, escalate
- **Rationale:** Projects stall waiting for feedback; proactive SLA reduces delays
- **Implementation:** Add to client communication templates (standardize)

**Recent Client Feedback Issues:**
- Client B: Feedback delayed 8 days (blocked project progress)
- Solution: Implemented 48-hour SLA communication (set expectations upfront)

### Design Process Improvements

**Improvement 1: Mobile-First Workflow**
- **Change:** All responsive projects start with mobile (375px), not desktop
- **Benefit:** Better mobile UX (60%+ of users); easier to expand than compress
- **Implementation:** Immediate (Nov 18+)

**Improvement 2: Design System Documentation**
- **Change:** Create comprehensive design system docs (4-week project)
- **Benefit:** Designers know what components exist; 100% compliance; consistent UI
- **Timeline:** Complete Dec 15

**Improvement 3: Figma File Organization**
- **Change:** Standardize file naming (`[Client Name] - [Project Type] - [Date YYYY-MM]`)
- **Benefit:** Easy to find files; no more wasted time searching
- **Implementation:** Anastasiia drafting standard; team will rename existing files (1-2 hour cleanup)

**Improvement 4: Pre-Delivery Quality Check**
- **Change:** 8/10 quality checklist before client delivery
- **Benefit:** Catch issues before client sees them; improved client satisfaction
- **Implementation:** Immediate

**Improvement 5: Weekly Design Critiques**
- **Change:** 15-minute critique per project (Fridays, weekly design sync)
- **Benefit:** Team feedback improves quality; knowledge sharing; maintain consistency
- **Implementation:** Starting next Friday
```

---

## Validation Checklist

- [ ] **Design projects** documented
- [ ] **Designers** assigned
- [ ] **Tools** referenced from Tools library
- [ ] **Quality standards** specified
- [ ] **Creative decisions** explained
- [ ] **Design system** status tracked
- [ ] **Portfolio** activities noted
- [ ] **Client feedback** processes captured
- [ ] **Process improvements** identified

---

## Related Templates

**Previous:** [17_Lead_Gen_Sales_Context.md](17_Lead_Gen_Sales_Context.md) - LG/Sales
**Next:** [19_Development_Technical_Context.md](19_Development_Technical_Context.md) - Dev specific
**Libraries:** [01_Library_Integration/05_Design_Libraries.md](../../01_Library_Integration/05_Design_Libraries.md) - Design department libraries

---

**Status:** ✅ Template ready for use
