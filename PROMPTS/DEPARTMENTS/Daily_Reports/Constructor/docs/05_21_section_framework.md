# 21-Section Daily Report Framework

## Overview
This document provides the comprehensive 21-section framework used in the MAIN PROMPT v2 for organizing daily call transcripts into structured reports.

---

## Framework Structure

The 21-section framework provides a consistent structure for extracting and organizing information from call transcripts across all departments.

---

## Section 1: Meeting Metadata

### Purpose
Capture basic information about the meeting/call

### Required Fields
- **Date**: Full date of the meeting
- **Participants**: All identified participants with:
  - Full name (matched to Employee Directory)
  - Employee ID
  - Department
  - Role/Profession
  - Confidence level (High/Medium/Low)
- **Duration**: Length of the call
- **Main Topics**: 3-5 key topics discussed

### Format Example
```markdown
## 1. MEETING METADATA

**Date:** October 24, 2025 (Friday)
**Participants:**
- Artemchuk Nikolay (ID: 37226) - Project manager, Lead generator | AI | Confidence: High
- Shelep Olha (ID: 86641) - UI/UX designer | Design | Confidence: High
**Duration:** 45 minutes
**Main Topics:**
- Project X design review
- Q4 roadmap planning
- Team resource allocation
```

---

## Section 2: Executive Summary

### Purpose
Provide a high-level overview of the entire meeting in 2-4 sentences

### Guidelines
- Summarize key decisions made
- Highlight critical action items
- Note major challenges or blockers
- Mention important client/project updates
- Keep it concise (100-200 words)

### Format Example
```markdown
## 2. EXECUTIVE SUMMARY

The team conducted a comprehensive design review of Project X, approving the final wireframes while identifying three critical UX improvements needed before development. Key decisions were made to allocate two additional designers to the project and extend the timeline by one week to ensure quality. The team also outlined Q4 priorities, focusing on completing three major client projects and launching the new service platform by December 15th.
```

---

## Section 3: Action Items & Tasks

### Purpose
Extract all actionable tasks with full details

### Required Fields Per Task
- **Description**: Action + Object + Context format
- **Owner/Assignee**: Matched to Employee Directory (name, ID, department)
- **Priority**: critical, high, medium, low
- **Timeline**: Due date, estimated duration
- **Dependencies**: Other tasks or resources needed
- **Status**: not_started, in_progress, blocked, completed
- **Related Project**: Matched to Project Directory
- **Success Criteria**: How to know it's complete
- **RACI** (if applicable): Responsible, Accountable, Consulted, Informed

### Format Example
```markdown
## 3. ACTION ITEMS & TASKS

### Create Employee Onboarding System
- **Description:** Develop employee registration/onboarding module within Talents system where new employees can self-register and input required data
- **Owner/Assignee:** Shelep Olha (ID: 86641) - UI/UX designer | Design | Danylenko Liliia (ID: 72754) - Full-Stack Developer | Dev
- **Priority:** High
- **Timeline:** Due: Nov 15, Estimated: 5-7 days
- **Dependencies:** Requirements document, Tango documentation link
- **Status:** Not Started
- **Related Project:** LibDev / Talents Microservice
- **Success Criteria:** System allows self-registration, all required fields captured, data validates correctly
- **RACI:**
  - Responsible: Danylenko Liliia (Dev)
  - Accountable: Artemchuk Nikolay (AI - Project Manager)
  - Consulted: Shelep Olha (Design), Nealova Evgeniya (HR)
  - Informed: All Department Leads
```

---

## Section 4: Projects & Features

### Purpose
Document project-specific discussions and feature development

### Content
- Project updates and progress
- New features discussed or approved
- Feature specifications and requirements
- Project timelines and milestones
- Cross-project dependencies

### Format Example
```markdown
## 4. PROJECTS & FEATURES

### LibDev / Talents Microservice - Phase 2
**Status:** In Development
**Progress:** 60% complete
**Features Discussed:**
- Job Application Intake Module (Ready for QA)
- Resume Parser with AI Integration (In Planning)
- Multi-status System (Blocked - needs architecture review)

**Timeline:**
- Phase 2 completion: Nov 30
- QA cycle: Dec 1-7
- Production deployment: Dec 15

**Stakeholders:** Dev team, HR team, Management
```

---

## Section 5: Workflows & Processes

### Purpose
Capture process discussions, improvements, and new workflows

### Content
- Current workflows being discussed or modified
- Process improvements or optimizations
- New procedures being established
- Workflow automation opportunities
- Integration points between systems

### Format Example
```markdown
## 5. WORKFLOWS & PROCESSES

### Job Application Intake Process - Improvements
**Current State:** Manual data entry from multiple formats
**Proposed Changes:**
1. Implement automatic resume parser (PDF, DOCX, RTF, images)
2. Add clipboard/buffer parser for Excel data import
3. Auto-populate applicant fields from parsed data

**Benefits:**
- 70% reduction in data entry time
- Improved data accuracy
- Faster candidate processing

**Implementation Timeline:** 3-4 weeks
```

---

## Section 6: Rules & Best Practices

### Purpose
Document standards, guidelines, and best practices established or reinforced

### Content
- Coding standards
- Design guidelines
- Communication protocols
- Quality standards
- Company policies
- Industry best practices adopted

### Format Example
```markdown
## 6. RULES & BEST PRACTICES

### QA Issue Tracking Standard
**Rule:** All QA issues must be logged in structured Excel with following columns:
- Page/Module
- Screenshot
- Critical Level (Critical/High/Medium/Low)
- Issue Description
- Comments/Notes

**Rationale:** Ensures consistent tracking and prioritization
**Applies To:** All microservice QA processes
**Effective Date:** Immediate
```

---

## Section 7: Problems & Solutions

### Purpose
Document challenges encountered and solutions proposed or implemented

### Content
- Technical problems
- Process bottlenecks
- Resource constraints
- Client issues
- Solutions proposed
- Workarounds implemented

### Format Example
```markdown
## 7. PROBLEMS & SOLUTIONS

### Problem: Status Updates Don't Refresh Automatically
**Description:** When changing status in job application system, page requires full refresh to display update
**Impact:** User experience issue, time waste, potential confusion
**Root Cause:** No auto-refresh mechanism implemented
**Proposed Solution:** Implement auto-refresh or partial page updates using AJAX
**Priority:** Critical
**Owner:** Klimenko Yaroslav (ID: 86478) - Frontend Developer | Dev
**Timeline:** 2-3 days
```

---

## Section 8: Tools & Resources

### Purpose
Document tools, technologies, and resources discussed

### Content
- Tools being used or evaluated
- Technology stack decisions
- Resource requirements (human, technical, financial)
- Tool integrations
- Licenses or subscriptions needed

### Format Example
```markdown
## 8. TOOLS & RESOURCES

### AI-Powered Resume Parser
**Tool Type:** AI Integration
**Purpose:** Automatically extract data from resumes in multiple formats
**Formats Supported:** PDF, DOCX, RTF, Images
**Integration:** LibDev Talents Microservice
**Decision:** Approved for implementation
**Owner:** Dev team
**Timeline:** Research phase - 1 week, Implementation - 2-3 weeks
```

---

## Section 9: Technical Architecture

### Purpose
Document technical decisions, architecture discussions, and system design

### Content
- Architecture decisions
- Database schema changes
- API design
- System integrations
- Performance considerations
- Security requirements
- Scalability plans

### Format Example
```markdown
## 9. TECHNICAL ARCHITECTURE

### Multi-Status System Architecture
**Component:** Job Application Status Management
**Current Architecture:** Single status per entity
**Proposed Architecture:** Multi-select status with tags
**Reasoning:** Different entities need unique status options
**Technical Approach:**
- Add status tags table
- Implement many-to-many relationship
- Create status filter UI component
**Impact:** Database schema change required
**Migration Plan:** Backfill existing statuses to new system
```

---

## Section 10: Decisions Log

### Purpose
Record all decisions made during the meeting

### Content
- What was decided
- Who made the decision
- Reasoning/context
- Alternatives considered
- Impact assessment

### Format Example
```markdown
## 10. DECISIONS LOG

**Decision #1:** Implement AI Resume Parser
- **Made By:** Artemchuk Nikolay (Project Manager)
- **Context:** Manual data entry too time-consuming
- **Alternatives Considered:** Manual process optimization, third-party service
- **Chosen Approach:** Build custom AI parser integrated with system
- **Reasoning:** Better control, customization, long-term cost savings
- **Impact:** 3-4 week development time, improved efficiency afterward

**Decision #2:** Extend Project Timeline by 1 Week
- **Made By:** Management team
- **Context:** Quality issues identified in QA
- **Impact:** Launch date moves to Nov 30
- **Reasoning:** Quality over speed
```

---

## Section 11: Documentation & Knowledge Gaps

### Purpose
Identify documentation needs and knowledge gaps

### Content
- Missing documentation
- Documentation to be created or updated
- Knowledge transfer needs
- Training requirements
- FAQ additions

### Format Example
```markdown
## 11. DOCUMENTATION & KNOWLEDGE GAPS

### Missing Documentation
1. **Employee Onboarding System Requirements**
   - Status: Needs to be written
   - Owner: Shelep Olha (Design)
   - Referenced: Tango documentation link needed
   - Due: Before development starts

2. **Resume Parser API Documentation**
   - Status: To be created
   - Owner: Dev team
   - Format: API specification with examples
   - Due: During implementation

### Knowledge Transfer Needs
- New QA tracking process training for all team members
- LibDev system overview for HR team
```

---

## Section 12: Communication & Announcements

### Purpose
Capture important communications and announcements

### Content
- Team announcements
- Company updates
- Client communications
- Schedule changes
- Event announcements

### Format Example
```markdown
## 12. COMMUNICATION & ANNOUNCEMENTS

### Client Call with TipCan Solutions
- **When:** Held during this meeting
- **Client Contact:** Alan
- **Project:** Freelance platform improvements
- **Key Points:**
  - Notification system implementation requested
  - Web generation training needed
  - Follow-up scheduled for next week

### Team Announcement
- New QA tracking system goes live immediately
- All team members to use standardized Excel format
- Training session scheduled for tomorrow
```

---

## Section 13: Blockers & Dependencies

### Purpose
Identify what's blocking progress and dependencies between tasks

### Content
- Current blockers
- Task dependencies
- Resource dependencies
- External dependencies
- Proposed resolutions

### Format Example
```markdown
## 13. BLOCKERS & DEPENDENCIES

### Blocker: Employee Onboarding Development Waiting on Requirements
- **Blocked Task:** Create New Employee Onboarding System
- **Blocking Item:** Requirements document not yet written
- **Impact:** Development cannot start
- **Dependency Owner:** Shelep Olha (Design)
- **Resolution:** Priority task to write requirements this week
- **Estimated Unblock Date:** Nov 10

### Dependency: Multi-Status System Depends on Architecture Review
- **Task:** Add Multi-status System for Applications
- **Depends On:** Architecture review and approval
- **Dependency Owner:** Technical Lead
- **Timeline Impact:** 3-5 day delay
- **Mitigation:** Parallel work on other tasks
```

---

## Section 14: Key Insights & Lessons

### Purpose
Capture learning, insights, and observations

### Content
- What worked well
- What didn't work
- Lessons learned
- Process improvements identified
- Team observations

### Format Example
```markdown
## 14. KEY INSIGHTS & LESSONS

### Insight: Structured QA Tracking Prevents Issue Loss
**Observation:** Previous QA findings were lost or forgotten due to ad-hoc tracking
**Lesson:** Structured Excel format ensures all issues are captured and tracked
**Application:** Implement for all QA processes going forward

### Lesson: AI Integration Provides Significant Time Savings
**Context:** Manual resume data entry extremely time-consuming
**Learning:** AI parser can reduce work by 70% while improving accuracy
**Future Application:** Look for other manual processes that could benefit from AI
```

---

## Section 15: Analogies & Frameworks

### Purpose
Document conceptual models, analogies, and frameworks discussed

### Content
- Analogies used to explain concepts
- Mental models
- Framework references
- Methodologies discussed

### Format Example
```markdown
## 15. ANALOGIES & FRAMEWORKS

### Framework: RACI Matrix for Task Accountability
**Applied To:** Major project tasks
**Purpose:** Clear accountability and communication
**Key Principle:** Only one person Accountable, multiple can be Responsible
**Usage:** Apply to all tasks in action items section

### Analogy: Resume Parser as "Smart OCR"
**Concept:** Parser is like OCR but understands context and structure
**Purpose:** Help non-technical team understand capability
**Extension:** Can handle multiple formats, not just images
```

---

## Section 16-20: Department-Specific Sections

### Purpose
Capture department-specific information that doesn't fit standard sections

### Section 16: Lead Generation Specifics
- Lead sources and channels
- Prospecting activities
- Lead quality metrics
- Conversion data
- Pipeline updates
- Account status changes

### Section 17: Sales Specifics
- Deal pipeline status
- Client negotiations
- Proposals and quotes
- Revenue forecasts
- Win/loss analysis
- Client relationship updates

### Section 18: Design Specifics
- Design reviews and feedback
- Creative direction
- Design tool updates
- Brand guidelines
- Asset creation
- Design system updates

### Section 19: Development Specifics
- Code reviews
- Sprint planning
- Technical debt
- Deployment schedules
- Bug reports
- Performance optimization

### Section 20: HR Specifics
- Recruitment updates
- Candidate pipeline
- Interview schedules
- Onboarding activities
- Employee events
- Policy updates

### Format Example (Lead Generation)
```markdown
## 16. LEAD GENERATION SPECIFICS

### Lead Sources Performance
- **LinkedIn**: 45 new leads this week (+12% vs last week)
- **Google Search**: 23 new leads (-5% vs last week)
- **Referrals**: 8 new leads (stable)

### Account Status Updates
- 3 accounts moved from "in work" to "sold"
- 2 accounts flagged as "problematic" - require attention
- 5 new accounts created and initialized

### Next Week Focus
- Target industries: Healthcare, Education
- Geographic focus: UK, Germany
- Promotion: 10-hour free trial offering
```

---

## Section 21: Follow-up Items

### Purpose
Identify items requiring follow-up in future meetings

### Content
- Topics to revisit
- Pending decisions
- Scheduled follow-ups
- Future discussions needed
- Long-term planning items

### Format Example
```markdown
## 21. FOLLOW-UP ITEMS

### Next Meeting (Nov 12)
- Review QA Excel implementation and feedback
- Discuss resume parser research findings
- Approve employee onboarding requirements document
- TipCan Solutions follow-up call results

### Future Discussions (Within 2 Weeks)
- Q4 resource allocation final decisions
- LibDev Phase 3 planning kickoff
- Year-end review preparation

### Pending Decisions
- Multi-status architecture approach (Waiting on technical review)
- Budget approval for AI tools subscription
- Q4 hiring needs assessment
```

---

## Integration Guidelines

### When to Use This Framework

1. **Full 21-Section Format**: Use for comprehensive weekly or monthly call summaries
2. **Abbreviated Format**: Use essential sections (1-3, 10, 21) for quick daily updates
3. **Department Focus**: Emphasize relevant department-specific sections (16-20)

### Section Selection by Call Type

#### Project Planning Calls
Focus on: 1-4, 10, 13, 21

#### Technical Review Calls
Focus on: 1, 7, 9, 10, 19, 21

#### QA/Testing Calls
Focus on: 1, 3, 6, 7, 10, 21

#### Client Calls
Focus on: 1, 2, 3, 10, 12, 17, 21

#### Department Meetings
Focus on: 1, 2, 3, 11, 12, relevant dept section (16-20), 21

### Quality Standards

- All sections should be completed when applicable (may have "No items" if nothing to report)
- Employee names must be matched to Employee Directory
- Project names must be matched to Project Directory
- Tasks must use Action + Object + Context format
- Decisions must include reasoning and impact
- Follow-ups must have clear owners and timelines

---

## Prompt Integration

To integrate this framework into department-specific prompts:

1. **Reference the framework** in the Purpose section
2. **List applicable sections** in Department Instructions
3. **Provide section templates** for each section used
4. **Include examples** relevant to the department
5. **Define quality criteria** for each section
6. **Specify department focus** (which sections are most critical)

---

*Last Updated: November 7, 2025*
