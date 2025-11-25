# Template 12: Communication & Announcements

**Purpose:** Track communications, announcements, and information sharing discussed
**Library Integration:** ⭐ Low (standalone communication tracking)
**Priority:** Include when team communications or announcements discussed

---

## Template

```markdown
## Communication & Announcements

**Announcements to Make:** [Number]
**Communication Plans:** [Number]
**Updates to Share:** [Number]

### Team Announcements

#### [Announcement Title]
- **Type:** [Company Update | Team Change | Process Change | New Policy | Achievement | Event]
- **Audience:** [Who needs to know]
- **Message:** [What to communicate - draft the actual message]
- **Purpose:** [Why this announcement matters]
- **Timing:** [When to announce]
- **Channel:** [Slack | Email | Meeting | All-Hands | 1-on-1]
- **Sender:** [Who will make the announcement]
- **Follow-up:** [Any follow-up actions needed]

### Client Communications

#### [Client Communication]
- **Client:** [Client name or project]
- **Purpose:** [Why we're communicating]
- **Message:** [What to say]
- **Timing:** [When to send]
- **Method:** [Email | Call | Video meeting]
- **Sender:** [Who will communicate]
- **Approval Needed:** [Yes/No, from whom]

### External Communications

[Partner updates, public announcements, social media]

### Internal Updates

#### [Department/Team Update]
- **From:** [Who is sharing update]
- **To:** [Which team(s)]
- **Update:** [What's the news]
- **Impact:** [How this affects recipients]
- **Action Required:** [What recipients should do, if anything]

### Sensitive Communications

[Communications requiring discretion or careful handling]

### Communication Templates Created

[Any new email templates, message templates, or communication scripts created]

### Communication Delays/Holds

[Communications that should wait or be timed carefully]
```

---

## Recognition Rules

### Identifying Communication Needs

**Direct Mentions:**
- "We should announce..."
- "Let the team know..."
- "Send an email about..."
- "Post in Slack..."

**Sharing Information:**
- "Everyone should know that..."
- "Make sure to communicate..."
- "Update the team on..."
- "Inform the client..."

**Timing Discussions:**
- "When should we tell them?"
- "Don't mention this yet..."
- "Wait until X before announcing..."

**Channel Discussions:**
- "Email vs Slack?"
- "Should we have a meeting?"
- "All-hands announcement or team meeting?"

---

## Examples

### Example 1: Company-Wide Announcements

```markdown
## Communication & Announcements

**Announcements to Make:** 4
**Communication Plans:** 2
**Updates to Share:** 3

### Team Announcements

#### New Hire Announcement - LG Team
- **Type:** Team Change
- **Audience:** All Remote Helpers employees (company-wide)
- **Message:**
  ```
  Exciting news! 🎉

  We're growing the Lead Generation team! We'll be welcoming a new Lead Generator to the team in early December.

  **Why:** Our LG team has done amazing work in Q4, and client demand for lead generation services has increased by 40%. To maintain our high-quality service and reduce pressure on our current team, we're adding another team member.

  **Timeline:** Job posting goes live this week, interviews throughout late November, start date target: December 9.

  **What this means for you:**
  - LG Team: Anastasiya and Hanan will share more details in your team meeting
  - Sales Team: We'll have more capacity for lead gen projects starting mid-December
  - Everyone else: Help us find great candidates! If you know someone who'd be a good fit, please refer them.

  Questions? Ask Anastasiya or Hanan.

  Let's keep growing! 🚀
  ```
- **Purpose:**
  - Transparency (team knows we're hiring)
  - Recruitment help (employee referrals)
  - Manage expectations (LG capacity increases in December)
- **Timing:** This week (November 18, Monday morning to maximize visibility)
- **Channel:** Slack #general channel + company-wide email
- **Sender:** Anastasiya (Sales Manager)
- **Follow-up:** Post job link when live (encourage shares)

#### Auth Microservice Project - Dev Team Focus
- **Type:** Company Update (explains why dev team is focused on infrastructure)
- **Audience:** All employees (especially those with dev requests)
- **Message:**
  ```
  Quick update from the Dev team 👨‍💻

  **What:** For the next 5 weeks, our dev team will be focused on a major infrastructure project: extracting authentication to a separate microservice.

  **Why:** After last week's production issue (authentication bug), we're improving our system architecture to make authentication more reliable, faster, and secure.

  **What this means:**
  - **Better reliability:** Auth issues won't bring down the whole system
  - **Better performance:** Login and API calls will be faster (targeting 83% improvement)
  - **Better security:** Advanced security features like rate limiting for login attempts

  **What this means for you:**
  - New feature requests will be delayed by 5 weeks (we'll queue them for late December)
  - Urgent bugs will still be addressed (we're not ignoring critical issues)
  - No impact on your day-to-day work (this is backend infrastructure)

  **Timeline:** Nov 18 - Dec 20 (5 weeks)

  The team is excited to make Remote Helpers more reliable! Questions? Ask Olha or Yaroslav.
  ```
- **Purpose:**
  - Set expectations (dev team capacity is limited for 5 weeks)
  - Explain why (not arbitrary, solving real problem)
  - Reduce frustration (people understand delays are temporary and for good reason)
- **Timing:** This week (November 18, after dev team finalizes plan)
- **Channel:** Slack #general + #dev-updates channels
- **Sender:** Olha (Tech Lead) or Anastasiya (Manager)
- **Follow-up:** Weekly progress updates in #dev-updates channel

#### Mobile-First Design Standard - Design Team Process Change
- **Type:** Process Change
- **Audience:** Design team (primary), Dev team (secondary - aware of new deliverable format), Sales team (FYI - affects project timelines slightly)
- **Message (Design Team):**
  ```
  Design Team Update 🎨

  **New Standard: Mobile-First Design (effective immediately)**

  Starting today (Nov 18), all responsive web design projects will start with mobile wireframes, then scale up to tablet and desktop.

  **Why the change:**
  - Mobile usage is >60% for most of our clients
  - Recent projects had poor mobile UX when we designed desktop-first
  - Designing for constraints first (mobile) leads to better UX at all sizes

  **How this works:**
  1. Start with mobile wireframes (375px width)
  2. Expand to tablet (768px)
  3. Expand to desktop (1440px)

  **Exception:** Desktop-only applications (e.g., admin dashboards) can start with desktop.

  **Questions?** Ask Anastasiia. She can share examples and walk through the approach.

  This will lead to better work for our clients! 📱💻
  ```
- **Message (Dev Team - FYI):**
  ```
  FYI from Design Team: All new responsive projects will be designed mobile-first (starting with 375px mobile, then scaling up). You'll see mobile wireframes earlier in the process. Questions? Ask Anastasiia.
  ```
- **Purpose:**
  - Align team on new process (everyone follows same approach)
  - Explain rationale (not arbitrary change)
  - Set expectation (effective immediately)
- **Timing:** This week (November 18, Monday - start of week)
- **Channel:** Slack #design-team (detailed), #dev-team (FYI), #general (brief mention)
- **Sender:** Anastasiia (Design Lead)
- **Follow-up:** Review in January (after 10+ projects completed with new approach)

#### Apollo.io Upgrade - LG Team Capacity Restored
- **Type:** Team Update (good news - bottleneck removed)
- **Audience:** LG team (primary), Sales team (secondary - can commit to more LG projects)
- **Message (LG Team):**
  ```
  LG Team - Bottleneck Removed! 🎉

  Good news: We've upgraded Apollo.io from 5,000 to 10,000 exports/month (effective immediately).

  **What this means:**
  - No more mid-month capacity issues
  - We can handle the increased client demand comfortably
  - 50% buffer for growth (we use ~6,500/month, now have 10,000)

  The upgrade is already active - Hanan confirmed access. Build those lists! 📊

  Cost: +$100/month (approved by Anastasiya).
  ```
- **Message (Sales Team):**
  ```
  Sales Team Update: LG team capacity increased (Apollo upgraded to 10,000 exports/month). We can take on more lead gen projects - the mid-month bottleneck is resolved! 💪
  ```
- **Purpose:**
  - Celebrate quick problem solving (bottleneck identified and fixed same day)
  - Unblock team (they can work without worrying about limits)
  - Inform sales (can commit to more projects)
- **Timing:** Immediately (problem solved, announce ASAP)
- **Channel:** Slack #lg-team (detailed), #sales-team (brief update)
- **Sender:** Hanan (LG Team Lead) or Anastasiya
- **Follow-up:** None needed (immediate fix)

### Client Communications

#### Client A - Project Timeline Update
- **Client:** Client A (interactive dashboard project)
- **Purpose:** Set expectations for project start (waiting for senior frontend hire)
- **Message:**
  ```
  Subject: Client A Dashboard Project - Timeline Update

  Hi [Client Name],

  Quick update on your interactive dashboard project:

  **Start Date:** Early January 2026 (we're bringing on a senior React specialist to lead this project)

  **Why:** Your dashboard requires advanced React expertise (real-time data updates, handling 10K+ data points, complex interactions). To deliver the quality you expect, we're hiring a senior frontend developer with specific experience in this type of project.

  **Timeline:**
  - December: Hire senior developer (recruitment in progress)
  - January 6: Developer starts, project kickoff
  - January 6-13: Planning and architecture (1 week)
  - January 13 - March 24: Development (10 weeks)
  - Late March: Delivery (Q1 as promised)

  **What's next:**
  - We'll keep you updated on hiring progress
  - In the meantime, we'll finalize requirements so we hit the ground running in January

  This investment in bringing on the right expertise will ensure your dashboard is performant, scalable, and exactly what you need.

  Questions? Let's schedule a call to discuss.

  Best regards,
  [Sender Name]
  ```
- **Timing:** This week (November 18-20, after hire decision confirmed)
- **Method:** Email (formal, documented)
- **Sender:** Anastasiya (project manager/sales)
- **Approval Needed:** Yes, from Olha (tech lead - confirm timeline is realistic)

### Internal Updates

#### Dev Team → Design Team: New API Response Format
- **From:** Olha (Backend Developer)
- **To:** Design Team (affects how they design error states, loading states)
- **Update:**
  ```
  Design Team heads-up:

  We're standardizing API response format (affects how you design error messages and loading states).

  **New Format:**
  - Success response: `{ success: true, data: {...}, error: null }`
  - Error response: `{ success: false, data: null, error: { code: "ERROR_CODE", message: "User-friendly message" } }`

  **What this means for you:**
  When designing error states, use `error.message` (we'll provide user-friendly messages from backend).

  Example: If user enters wrong password, backend returns:
  `{ success: false, data: null, error: { code: "INVALID_CREDENTIALS", message: "Email or password is incorrect" } }`

  Your designs should display: "Email or password is incorrect"

  Questions? Ping me in Slack.
  ```
- **Impact:** Designers know how to design error states (use backend error messages, not hardcode)
- **Action Required:** Designers update error state designs in current/future projects

#### LG Team → Sales Team: New Lead Scoring Process
- **From:** Plamena (LG Team)
- **To:** Sales Team
- **Update:**
  ```
  Sales Team Update:

  We're implementing lead scoring for all lead lists (prioritizes highest-quality leads).

  **What this means:**
  - Lead lists will now include "Score" column (1-10 scale)
  - Hot Leads (8-10): Highest priority (best company size, title, industry match)
  - Warm Leads (5-7): Medium priority
  - Cold Leads (1-4): Lower priority

  **What you should do:**
  Focus outreach on Hot leads first (higher meeting booking rate).

  This should improve your conversion rates! 📈

  Plamena is drafting the full scoring criteria - will share next week.
  ```
- **Impact:** Sales team can prioritize outreach (work smarter)
- **Action Required:** Sales team adjusts outreach strategy (focus on high-score leads)

### Sensitive Communications

#### Developer Performance Issue (Private Communication)
- **Type:** 1-on-1 Performance Discussion
- **Audience:** [Specific developer] (not team-wide announcement)
- **Context:** Recent code quality issues; need private conversation
- **Message:** [Not documented here - private HR matter]
- **Timing:** This week (private 1-on-1 with Anastasiya)
- **Channel:** Private video call (not Slack, not email - verbal only)
- **Sender:** Anastasiya (Manager)
- **Follow-up:** Performance improvement plan (documented privately)
- **Note:** This is NOT a public announcement; handled discreetly with individual

### Communication Templates Created

#### Client Feedback Request Email Template
- **Purpose:** Standardize how we request feedback from clients (ensure 48-hour SLA communicated)
- **Template:**
  ```
  Subject: [Project Name] - Designs Ready for Your Feedback

  Hi [Client Name],

  Great progress on [Project Name]! Your [deliverable type - e.g., landing page wireframes] are ready for review.

  **Review Link:** [Figma link or PDF attachment]

  **What we need:**
  - Your feedback on design direction, layout, content
  - Any changes or adjustments you'd like

  **Timeline:**
  To keep the project on schedule, please provide feedback within 48 hours (by [specific date, time]).

  If you need more time, no problem - just let us know and we can adjust the timeline.

  **How to provide feedback:**
  - Reply to this email with your thoughts
  - [OR: Leave comments directly in Figma]
  - [OR: Schedule a quick call to discuss]

  Looking forward to your feedback!

  Best regards,
  [Designer Name]
  ```
- **Created By:** Olha (Design)
- **Use Case:** All design projects (sends after completing design milestone)
- **Benefit:** Sets 48-hour expectation (reduces delays), professional communication

### Communication Delays/Holds

#### Senior Frontend Hire Announcement - WAIT UNTIL OFFER ACCEPTED
- **Communication:** Announce new senior frontend developer hire
- **Hold Until:** Candidate accepts offer (don't announce before offer accepted)
- **Reason:** Premature announcement could backfire if candidate declines
- **Planned Timing:** After offer accepted (target: late December)
- **Channel:** Slack #general + company email
- **Draft Message:** (Prepared, ready to send once offer accepted)
  ```
  Exciting news! 🎉

  We're welcoming [Name] to the Remote Helpers dev team as our Senior Frontend Developer!

  [Name] brings 5+ years of React expertise and will be leading our Client A dashboard project starting in January.

  Welcome to the team, [Name]! 👏
  ```
```

---

## Validation Checklist

- [ ] **All announcements** identified
- [ ] **Audiences** clearly defined
- [ ] **Messages** drafted (actual content, not just description)
- [ ] **Timing** specified
- [ ] **Channels** selected
- [ ] **Senders** assigned
- [ ] **Purpose** explained
- [ ] **Follow-up actions** noted
- [ ] **Client communications** handled professionally
- [ ] **Sensitive communications** kept private
- [ ] **Communication templates** captured
- [ ] **Delays/holds** tracked appropriately

---

## Related Templates

**Previous:** [11_Documentation_Gaps.md](11_Documentation_Gaps.md) - Documentation needs
**Next:** [13_Blockers_Dependencies.md](13_Blockers_Dependencies.md) - Blocking issues
**Related:** [10_Decisions_Log.md](10_Decisions_Log.md) - Decisions often need communication

---

**Status:** ✅ Template ready for use
