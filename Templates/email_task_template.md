# Email Template for Task Assignment

**Entity:** Templates
**Purpose:** Standardized email format for assigning tasks
**Created:** 2025-12-08
**Version:** 1.0

---

## Standard Task Email Template

### Subject Line Format
```
[PRIORITY] Task: [Brief Description] - Due [Date]
```

**Examples:**
- `[HIGH] Task: Review cloud pricing proposal - Due Dec 10`
- `[MEDIUM] Task: Update employee handbook - Due Dec 15`
- `[LOW] Task: Schedule Q1 planning meeting - Due Dec 20`

---

## Email Body Template

```markdown
Hi [Name],

I'm assigning you the following task:

## Task: [Task Title]

**Priority:** [High / Medium / Low]
**Due Date:** [YYYY-MM-DD]
**Estimated Time:** [X hours/days]
**Assigned By:** [Your Name]
**Date Assigned:** [YYYY-MM-DD]

### Description
[Clear, concise description of what needs to be done. Include context and background if needed.]

### Deliverables
- [ ] [Specific deliverable 1]
- [ ] [Specific deliverable 2]
- [ ] [Specific deliverable 3]

### Resources
- [Link to relevant document]
- [Link to reference material]
- [Contact person for questions]

### Success Criteria
[How will we know this task is complete and successful?]

### Questions or Blockers?
Please reply to this email or message me on [Monday.com / Slack / etc.] if you:
- Need clarification
- Encounter blockers
- Need additional resources
- Require deadline extension

### Next Steps
1. Acknowledge receipt of this task
2. Review requirements and ask questions
3. Add to your Monday.com board
4. Complete by [due date]
5. Notify me when complete

---

**Monday.com Task Link:** [Link to Monday.com task]
**Project:** [Project name if applicable]
**Related Tasks:** [Links to dependencies]

Best regards,
[Your Name]
[Your Title]
```

---

## Priority Level Guidelines

### HIGH Priority
**Response Time:** Same day acknowledgment
**Due Date:** Typically 1-3 days
**Use When:**
- Critical deadline approaching
- Blocking other work
- Executive request
- Client-facing urgency

**Subject Example:**
`[HIGH] Task: Fix production bug - Due Dec 08 EOD`

### MEDIUM Priority
**Response Time:** Within 1 business day
**Due Date:** Typically 1-2 weeks
**Use When:**
- Important but not urgent
- Standard project work
- Scheduled deliverables
- Team coordination needs

**Subject Example:**
`[MEDIUM] Task: Create training materials - Due Dec 15`

### LOW Priority
**Response Time:** Within 2-3 business days
**Due Date:** Typically 2-4 weeks
**Use When:**
- Nice to have
- Process improvements
- Future planning
- Low-impact tasks

**Subject Example:**
`[LOW] Task: Research new tools - Due Dec 30`

---

## Task Type Variations

### 1. Research Task Template

```markdown
## Research Task: [Topic]

**Priority:** Medium
**Due Date:** [Date]
**Estimated Time:** 4-8 hours

### Research Objective
[What question are we trying to answer?]

### Scope
- [Area 1 to investigate]
- [Area 2 to investigate]
- [Area 3 to investigate]

### Deliverable
Document with:
- Findings summary (1-2 pages)
- Comparison table (if applicable)
- Recommendation with rationale
- Sources cited

### Research Sources
- Industry reports
- Competitor analysis
- User reviews
- Expert interviews
- [Other relevant sources]

### Questions to Answer
1. [Question 1]
2. [Question 2]
3. [Question 3]

**Output Format:** Google Doc or Markdown file
**Save Location:** [Google Drive path or Dropbox path]
```

---

### 2. Build/Create Task Template

```markdown
## Build Task: [What to Build]

**Priority:** High
**Due Date:** [Date]
**Estimated Time:** [X days/weeks]

### What to Build
[Clear description of the end product]

### Requirements
**Must Have:**
- [Requirement 1]
- [Requirement 2]

**Nice to Have:**
- [Optional feature 1]
- [Optional feature 2]

### Technical Specifications
- [Tech stack or tools to use]
- [Performance requirements]
- [Integration needs]

### Acceptance Criteria
- [ ] [Criterion 1 - how to test/verify]
- [ ] [Criterion 2 - how to test/verify]
- [ ] [Criterion 3 - how to test/verify]

### Resources
- Design mockups: [link]
- Similar examples: [link]
- Documentation: [link]

### Testing
Please test the following before submitting:
- [Test case 1]
- [Test case 2]

### Delivery
**Format:** [Code/Document/Design file]
**Location:** [Where to submit]
**Notification:** Tag me when complete
```

---

### 3. Review Task Template

```markdown
## Review Task: [What to Review]

**Priority:** High
**Due Date:** [Date] (Typically 2-3 days)
**Estimated Time:** 1-2 hours

### What to Review
[Link to document/code/design]

### Review Focus
Please evaluate:
- [Aspect 1 - e.g., technical accuracy]
- [Aspect 2 - e.g., completeness]
- [Aspect 3 - e.g., style/formatting]

### Review Criteria
**Technical:**
- [ ] Accuracy of information
- [ ] Completeness
- [ ] Follows standards

**Quality:**
- [ ] Clear and understandable
- [ ] No errors or typos
- [ ] Professional presentation

### Deliverable
Please provide:
- Approval to proceed OR
- List of changes needed
- Comments inline (if document)
- Summary of feedback

### Feedback Format
- Use comment/track changes in document
- Email summary of major points
- Rate overall: Approved / Minor Changes / Major Revision
```

---

### 4. Video Production Task Template

```markdown
## Video Task: [Video Title]

**Priority:** Medium
**Due Date:** [Date]
**Estimated Time:** [Shoot: X hours, Edit: Y days]

### Video Type
[Tutorial / Personal Brand / Business / Other]

### Shoot Details
**Date:** [YYYY-MM-DD]
**Time:** [HH:MM]
**Location:** [Address or "Home Studio"]
**Outfit:** [Outfit #XXX from clothes_catalog.md]

### Content Requirements
**Topic:** [What the video covers]
**Key Points:**
1. [Point 1]
2. [Point 2]
3. [Point 3]

**Target Length:** [Minutes]
**Target Audience:** [Who is this for?]

### Pre-Production
- [ ] Script/talking points prepared
- [ ] Shot list created
- [ ] Equipment packed
- [ ] Location confirmed
- [ ] Outfit selected

See: [shooting_instructions.md](../Video/shooting_instructions.md)

### Post-Production
- [ ] Footage uploaded (see upload_workflow.md)
- [ ] Editing completed
- [ ] Exports generated (4K, 1080p, mobile)
- [ ] Thumbnail created
- [ ] Upload to platform

### Deliverables
- Final edited video (3 formats)
- Thumbnail image
- Video description/caption
- Upload to [platform]

**Platform:** [YouTube / Instagram / etc.]
**Publish Date:** [YYYY-MM-DD]
```

---

## Automation Integration

### Reserved Word Triggers

When automation-agent detects reserved words in daily files, it auto-generates task emails using these templates:

**RESEARCH** → Research Task Template
**BUILD** → Build/Create Task Template
**CREATE** → Build/Create Task Template
**REVIEW** → Review Task Template
**PROCESS video** → Video Production Task Template

### Auto-Generated Email Flow

```
User writes in 08_daily.md:
"RESEARCH cloud pricing under $1000/month"

↓

Automation-agent detects RESEARCH

↓

Creates task file in Share/
Using Research Task Template

↓

Email sent to assignee
(or Monday.com task created)

↓

Assignee receives structured task
With all necessary context
```

---

## Email Best Practices

### Subject Line
- **Always include priority** [HIGH/MEDIUM/LOW]
- **Keep it under 60 characters**
- **Include due date** for urgency clarity
- **Use keywords** that are searchable

### Body
- **Clear and concise** - respect recipient's time
- **Action-oriented** - what exactly needs to be done
- **Complete context** - enough info to start without back-and-forth
- **Specific deliverables** - checkboxes for clarity
- **Single call-to-action** - what's the next step?

### Timing
- **Send during work hours** - avoid weekend/late night unless urgent
- **Allow adequate time** - don't assign 1-day task at 5pm
- **Consider workload** - check recipient's current tasks
- **Follow up** - if no acknowledgment in 24 hours (high) or 48 hours (medium)

---

## Response Templates

### Acknowledgment Template (For Recipients)

```markdown
Hi [Assigner],

Task received and acknowledged.

**Task:** [Task name]
**Due:** [Date]
**My ETA:** [Your estimated completion date]

**Questions:**
[Any questions or none]

**Status:** Added to my Monday.com board

I'll notify you upon completion or if any blockers arise.

Thanks,
[Your name]
```

### Completion Notification Template

```markdown
Hi [Assigner],

Task completed!

**Task:** [Task name]
**Completed:** [YYYY-MM-DD]
**Deliverable:** [Link to output]

**Summary:**
[Brief summary of what was done]

**Notes:**
[Any notes, learnings, or recommendations]

Ready for your review.

Thanks,
[Your name]
```

---

## Monday.com Integration

### Task Creation from Email

When sending task email:
1. Create corresponding Monday.com task
2. Include Monday.com link in email
3. Attach email to Monday.com task
4. Set deadline in Monday.com
5. Add to appropriate board/project

### Status Sync

**Email Sent** → Monday.com Status: "Assigned"
**Acknowledged** → Monday.com Status: "In Progress"
**Completed** → Monday.com Status: "Complete"
**Blocked** → Monday.com Status: "Stuck"

---

## Template Customization

### For Your Team

Customize these templates by:
1. Copy this file to your department folder
2. Adjust sections to match your workflow
3. Add department-specific fields
4. Update tools/systems referenced
5. Share with team for consistency

### For Specific Projects

Create project-specific variants:
- Add project-specific context
- Include project resources/links
- Adjust deliverable formats
- Modify priority definitions

---

## Usage Examples

### Example 1: High-Priority Research

**Subject:**
`[HIGH] Task: Research AI video interview platforms - Due Dec 09`

**Body:**
[Uses Research Task Template]
- 3 platforms to evaluate
- Comparison table required
- Budget constraint: <$500/month
- Integration needs: Monday.com, Google Drive

### Example 2: Video Production

**Subject:**
`[MEDIUM] Task: Create tutorial video on Python basics - Due Dec 12`

**Body:**
[Uses Video Production Task Template]
- 10-minute tutorial
- Shoot: Dec 10
- Edit: Dec 11-12
- Outfit #001 (professional casual)
- Platform: YouTube

### Example 3: Build Task

**Subject:**
`[HIGH] Task: Build employee onboarding checklist - Due Dec 09`

**Body:**
[Uses Build/Create Task Template]
- 4 phases: Pre-start, Day 1, Week 1, Month 1
- Checkboxes for each item
- Integration with Monday.com
- Template format (reusable)

---

**Template Status:** Active - Ready for use
**Last Updated:** 2025-12-08
**Version:** 1.0
**Next Review:** After 10 uses or 1 month
