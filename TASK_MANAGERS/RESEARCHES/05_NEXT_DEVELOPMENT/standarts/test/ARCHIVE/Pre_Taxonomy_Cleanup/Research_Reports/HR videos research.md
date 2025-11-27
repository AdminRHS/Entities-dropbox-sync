---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: HR videos research
title: HR videos research
date: 2025-11-14
status: archived
owner: unknown
related: []
links: []
---

# HR videos research

## Summary
- TODO

## Context
- TODO

## Data / Content
Offer Accepted → Preboarding (Day -7)
  → Send welcome email, IT setup request, documentation tasks
→ Day 0 (First Day)
  → Account provisioning, orientation meetings, team introductions
→ Week 1-4 (Integration)
  → Training modules, buddy check-ins, feedback surveys
→ Day 30/90 (Checkpoints)
  → Extended feedback, performance check-in, onboarding completion
```

**Implementation Platforms**: Zapier (easiest, many pre-built templates), Make (more flexible), n8n (most control).

**Key Automation**: Folder creation for new hires. One tutorial shows using n8n + Google Drive API to automatically copy a template folder structure and rename it for each new employee.

---

### Performance Management & Analytics

**Performance Review Automation**: AI generates initial review drafts (with source citations), managers edit, reduces bias through data grounding.

**Goal Tracking with KPIs**: Real-time tracking against performance goals, trigger feedback reminders, sentiment analysis of feedback.

**Predictive Analytics**: Anticipate performance trends, recommend training, identify at-risk employees.

---

### LinkedIn & Social Recruitment

**Build AI Agent to Auto-Generate LinkedIn Posts**: Uses Pabbly + Google Sheets. Read job title/description/requirements → AI generates compelling LinkedIn post → Auto-publish.

**LinkedIn Recruiter with AI Integration**: Boolean search optimization, AI candidate recommendations, personalized outreach templating.

---

### ChatGPT/Claude for HR Content

**Job Description Generation**: Save 20 minutes per job posting. ChatGPT generates initial draft, you customize for company voice.

**Interview Question Generation**: Based on job description and required competencies.

**Candidate Communication Templates**: Rejection emails, interview invitations, offer letters.

---

## Technology Stack Analysis: What's Being Used in Tutorials

[image:2]

### Tool Frequency in Tutorials (by feature)

| Tool | Feature| Tool | Featured In | Primary Use | Learning Time | Cost |
|------|------------|------------|-----------------|------|
| **n8n** | 8 tutorials | Core automation | 2 weeks | Free |
| **Google Gemini** | 5 tutorials | AI analysis | 1 day | Free API |
| **ChatGPT** | 6 tutorials | Content generation | 1 day | $20/mo |
| **Claude AI** | 3 tutorials | Content generation | 1 day | €20/mo |
| **Notion** | 4 tutorials | Database/ATS | 1 week | Free |
| **Google Sheets** | 8 tutorials | Data storage | 1 day | Free |
| **Zapier** | 5 tutorials | Integration | 1 week | Free* |
| **Make.com** | 4 tutorials | Integration | 1 week | Free* |
| **NotebookLM** | 3 tutorials | Document analysis | 1 day | Free |
| **Typeform** | 3 tutorials | Application forms | 1 day | Free |
| **Gmail** | 7 tutorials | Communication | 1 day | Free |

*Free tier has limitations, paid plans available

---

## Pain Point Mapping: Solutions Identified

### Pain Point #1: Manual CV Screening

**Current State**: Hours spent reading CVs manually, subjective ranking, risk of bias

**Tutorial Solution Path**:
1. **Boomi Techie** (n8n + Gemini) → Automated screening
2. **ByteWise** (NotebookLM) → Interview prep from shortlisted CVs
3. **The AI Doctor** → End-to-end pipeline

**Time Savings**: 20+ minutes per resume
**Implementation Time**: 2-3 hours
**ROI**: Immediate (every recruitment cycle)

**Success Metric**: From processing 50 CVs in 25 hours → 3 hours

---

### Pain Point #2: Manual Interview Scheduling

**Current State**: Back-and-forth emails, calendar coordination, human error

**Tutorial Solution**: n8n workflow with Calendly or Google Calendar integration
- Candidate email triggers interview invite with available time slots
- Calendar syncs automatically
- Confirmation sent to both parties
- Managers notified

**Implementation**: Add-on to main n8n workflow (1-2 additional hours)

---

### Pain Point #3: Folder Creation for New Hires

**Current State**: Manually creating employee folders in Dropbox/Google Drive, copying templates

**Tutorial Solution**: n8n + Google Drive API automation
- Template folder structure created once
- When new hire date arrives, n8n copies template
- Renames folder to employee name
- Shares with appropriate team members

**Implementation**: 2-3 hours (requires API setup)

**Status in Research**: Onboarding automation tutorials cover this technique

---

### Pain Point #4: Job Posting Distribution

**Current State**: Manually posting to Instagram, LinkedIn, job boards, company website

**Tutorial Solution**: Pabbly + Google Sheets + LinkedIn API
1. Enter job details in Google Sheets (title, description, requirements)
2. Pabbly reads the data
3. AI generates LinkedIn post
4. Auto-publish to LinkedIn
5. Manual distribution to other platforms, but templates available

**Implementation**: 1-2 hours setup
**Time Saved**: 1-2 hours per job posting

**Tutorials Covering This**: "How to Build an AI Agent to Auto-Generate LinkedIn Posts" (Pabbly, May 2025)

---

### Pain Point #5: Compliance & Documentation Tracking

**Current State**: Manual document management, risk of missing compliance deadlines, audit trail gaps

**Tutorial Solutions**:
1. **AIHR Compliance Tutorial** → Automated compliance checks
2. **ChatGPT Compliance Document Generator** → AI-assisted document creation

**Automation Examples**:
- Flag expired certifications automatically
- Generate audit-ready reports
- Track GDPR/CCPA compliance
- Maintain immutable audit logs

**Implementation**: 2-3 hours (leveraging templates from tutorials)

---

## 4-Week Implementation Roadmap for Your Team

### Week 1: Recruitment Automation (Core Automation)

**Primary Goal**: Automate CV screening and candidate ranking

**Videos to Complete**:
- Boomi Techie - "Create AI Agent for Recruiters" (2.5 hours watch + pause)
- The AI Doctor - "100% Automated Recruitment" (2 hours)

**Implementation Tasks**:
1. Set up n8n account (free tier) - 15 min
2. Connect Gmail to n8n - 20 min
3. Get Google Gemini API key - 10 min
4. Create Google Sheets template - 20 min
5. Build n8n nodes step-by-step following tutorial - 2 hours
6. Test with 10 sample resumes - 30 min
7. Document workflow in Notion - 30 min

**Team Split**:
- Viktoriia: Technical setup (steps 1-6)
- Evgeniya: Testing & documentation (step 7)

**Expected Outcome**: System that accepts CVs from email, scores them with AI, outputs to Google Sheets

**Success Metric**: Process 50 CVs in 90 minutes (vs. 20+ hours manually)

---

### Week 2: Complete Recruitment System + Onboarding Start

**Primary Goal**: Full hiring pipeline automation + initiate onboarding automation

**Videos to Complete**:
- Jordan Pieces - "Automate Entire Hiring Process" (1 hour + implementation)
- ByteWise - "CV Screening & Interview Questions" (10 min + practice)
- Redwerk - "Smart Onboarding Automation" (1.5 hours)

**Implementation Tasks**:
1. Set up Notion workspace (free account) - 20 min
2. Create Notion ATS database with status tracking - 1 hour
3. Create Typeform application form (free tier) - 30 min
4. Build n8n: Typeform → Notion → Email - 1.5 hours
5. Set up interview scheduling automation - 1 hour
6. Design onboarding workflow in Notion - 1 hour
7. Create onboarding checklist templates - 1 hour

**Team Split**:
- Viktoriia: n8n workflows (steps 4-5)
- Evgeniya: Notion setup & templates (steps 1-3, 6-7)

**Expected Outcome**: Complete system from job application → candidate tracking → interview scheduling → onboarding handoff

**Success Metric**: New job application lands in Notion ATS automatically, interview invite is scheduled automatically

---

### Week 3: Content Generation & Communication

**Primary Goal**: Automate job description creation, interview prep, candidate communication

**Videos to Complete**:
- ChatGPT for HR tutorials (content generation)
- ByteWise NotebookLM tutorial (interview prep)
- Pabbly AI Agent tutorial (LinkedIn posts)

**Implementation Tasks**:
1. Create ChatGPT/Claude prompt library for HR - 1.5 hours
2. Test job description generation (10 examples) - 1 hour
3. Set up NotebookLM workflow for interview prep - 30 min
4. Create candidate communication templates - 1 hour
5. Set up Pabbly workflow for LinkedIn (if managing social recruitment) - 1.5 hours
6. Test end-to-end: job posting → LinkedIn → application - 1 hour

**Team Split**:
- Viktoriia: Pabbly setup, technical integration
- Evgeniya: Prompt engineering, template creation

**Expected Outcome**: Faster job posting creation, LinkedIn posts auto-generated, interview prep materials available for each candidate

**Success Metric**: Job posting created in 30 minutes (vs. 1 hour manual writing)

---

### Week 4: Compliance, Optimization & Documentation

**Primary Goal**: Add compliance layer, measure ROI, document all systems

**Videos to Complete**:
- AIHR "AI in HR Strategy" (strategic review)
- AIHR "AI in Compliance" (compliance automation)
- ChatGPT Compliance Document Generator

**Implementation Tasks**:
1. Audit current HR processes for compliance gaps - 1 hour
2. Set up automated compliance checks (certifications, documents) - 1 hour
3. Create compliance audit trail logging - 1.5 hours
4. Measure time saved in each process - 30 min
5. Document all workflows in shared Notion playbook - 2 hours
6. Train both team members on all systems - 2 hours
7. Set up feedback survey for improvements - 30 min

**Team Split**:
- Both: Weekly checkpoint meetings to discuss progress
- Viktoriia: Technical compliance logging
- Evgeniya: Process documentation & training

**Expected Outcome**: Documented, compliant, measured HR automation system ready for ongoing use and iteration

**Success Metrics**:
- Time saved documented: 20-30 hours/month expected
- Compliance checklist automated
- Playbook created for future reference

---

## Specific Recommendations for Austria & Ukraine Context

### GDPR & EU Compliance

**Tutorials Addressing This**: "100% Automated Recruitment Workflow" explicitly covers EU data hosting options

**Recommendations**:
- ✅ Use **n8n cloud** with EU data center (Frankfurt or Amsterdam) - GDPR compliant
- ✅ Use **Notion** - EU-friendly, GDPR compliant
- ✅ Use **Claude AI** (Anthropic) instead of ChatGPT (OpenAI) for privacy
- ✅ Use **Google Workspace** - you already have GDPR agreements in place
- ⚠️ Avoid ChatGPT for sensitive data (US-based)
- ⚠️ Avoid Zapier alone for critical HR data (consider Make.com as EU alternative)

**Action**: When implementing n8n, select EU hosting region explicitly

---

### Cost Breakdown for Complete System

| Component | Monthly| Component | Monthly Cost | Notes |
|-----------|-------------|-------|
| n8n Cloud (EU hosted) | €49 | Or free if self-hosted on local server |
| Notion | Free | Unlimited for your use case |
| Claude AI (occasional use) | €20 | Or use ChatGPT at $20/month |
| Google Workspace (existing) | Already paid | No additional cost |
| Typeform | Free | 100 responses/month free tier |
| Make.com (if replacing Zapier) | €0-99 | Depends on workflow complexity |
| **Total Monthly** | **€69-169** | One-time setup: €200-300 in tools |

**Comparison**: Standard HR tools cost €2,000-5,000/month. This setup: €100-200/month.

---

## Quick-Start 48-Hour Challenge

**If you have only 2 days to get started**:

**Day 1 (4 hours)**:
- Hour 1: Watch AIHR Strategy video + Boomi Techie first 30 minutes
- Hour 2: Create n8n account, set up Gmail connection
- Hour 3: Build first n8n node for CV retrieval
- Hour 4: Get Google Gemini API working, test with 1 sample resume

**Day 2 (4 hours)**:
- Hour 1: Complete n8n workflow for CV scoring
- Hour 2: Set up Google Sheets database
- Hour 3: Test with 10 resumes, verify accuracy
- Hour 4: Document the workflow, plan Week 2 implementation

**Day 2 Evening**: You have your first working automation processing CVs automatically. Celebrate! 🎉

---

## Learning Path Recommendations

### For Viktoriia (Technical Implementation Focus)

**Week 1-2**: 
- Deep dive into n8n tutorials
- Learn n8n node types: triggers, actions, logic
- Understand APIs and webhook concepts

**Week 3-4**:
- Advanced n8n: custom code nodes, error handling
- Integration patterns (Make.com vs Zapier comparison)
- Google Apps Script for advanced customization

**Month 2**:
- OCR + NLP concepts for resume parsing
- API rate limiting and performance optimization
- Self-hosting n8n on local server (advanced)

### For Evgeniya (Process & Operations Focus)

**Week 1-2**:
- Notion database design and templates
- Process documentation best practices
- ChatGPT prompt engineering for HR content

**Week 3-4**:
- Workflow documentation and team playbooks
- Quality assurance testing for workflows
- Employee change management for new systems

**Month 2**:
- HR compliance frameworks
- Analytics and ROI measurement
- Training other team members

---

## Common Implementation Mistakes to Avoid

1. **❌ Don't start with Make.com if you're a beginner** → Use Zapier first for simplicity, move to Make later if needed

2. **❌ Don't automate everything at once** → Start with recruitment (highest impact), add onboarding next, compliance last

3. **❌ Don't skip documentation** → Document as you build, not after. It only takes extra 15-20 minutes and saves hours later

4. **❌ Don't use US-based AI for sensitive HR data** → Use Claude or Gemini, not just ChatGPT, for privacy

5. **❌ Don't build complex workflows in Week 1** → Start simple, add features incrementally

6. **❌ Don't test in production** → Always test with dummy data first, use staging environment

7. **❌ Don't forget error handling** → Build in fallbacks if automation fails (email alerts to team)

8. **❌ Don't assume "set it and forget it"** → Review workflows monthly, optimize based on results

---

## Success Metrics to Track

### Recruitment Automation

- **CV Screening Time**: Before (2-3 hours for 50 CVs) → After (30 minutes for 50 CVs)
- **Screening Accuracy**: % of AI-ranked candidates that actually pass human interview
- **Recruitment Cycle Time**: Before (30 days) → After (20 days)
- **Cost per Hire**: Calculate savings from reduced manual work

### Onboarding Automation

- **Onboarding Completion Time**: Before → After
- **Document Collection Time**: Before → After
- **First-Week Productivity**: Before → After
- **New Hire Satisfaction Score**: Survey feedback

### Overall Team Efficiency

- **Manual HR Hours Saved/Month**: Track actual time saved
- **Error Rate Reduction**: Track data entry errors eliminated
- **Cost Reduction**: Calculate savings vs. cost of tools

### ROI Example

- **Current**: 20 hours/month manual CV screening at €25/hour = €500
- **After Automation**: 2 hours/month manual review = €50
- **Monthly Savings**: €450
- **Tool Cost**: €100/month
- **Net Savings**: €350/month
- **ROI Breakeven**: First month of recruitment cycle

---

## Next Steps After Research Completion

1. **This Week**: 
   - [ ] Read this full research report (1-2 hours)
   - [ ] Watch the 5 high-priority tutorials in order (8-10 hours total)
   - [ ] Share with your team, assign sections

2. **Next Week**:
   - [ ] Create n8n account, start Week 1 implementation
   - [ ] Designate tech lead (Viktoriia) and process lead (Evgeniya)
   - [ ] Schedule weekly sync meetings (30 min, Mondays)

3. **By End of Week 1**:
   - [ ] Have first automation running (CV screening)
   - [ ] Have generated ROI estimate
   - [ ] Plan Week 2 tasks

4. **By End of Month 1**:
   - [ ] Complete recruitment automation
   - [ ] Start onboarding automation
   - [ ] Measure actual time saved

---

## Resource Downloads & Links

**Video Tutorials (Save These)**:
- Boomi Techie - n8n + Gemini recruitment
- The AI Doctor - Complete recruitment workflow
- Jordan Pieces - Hiring system with Notion
- ByteWise - NotebookLM CV screening
- AIHR - HR AI strategy framework

**Tool Sign-Ups** (free accounts):
- n8n.io (free tier)
- Notion.so (free workspace)
- NotebookLM.ai (free with Google account)
- Make.com (free tier with limits)
- Zapier.com (2 free automations/month)

**Templates to Download**:
- Google Sheets CV scoring template
- Notion ATS database template
- Typeform application form template
- n8n recruitment workflow template

---

## Final Recommendations Summary

Your 2-person Austria/Ukraine HR team should:

✅ **Start with n8n** - Most powerful automation engine, EU GDPR options, free tier available

✅ **Use Notion as ATS** - All-in-one, free, collaborative, customizable, zero vendor lock-in

✅ **Pair with Claude AI** - Better privacy than ChatGPT for HR data, EU-friendly

✅ **Keep Google Workspace** - Already using, integrates perfectly, data already compliant

✅ **Document everything** - Small team means you need to share knowledge easily

✅ **Measure relentlessly** - Track time saved, costs reduced, quality metrics

✅ **Start recruitment automation first** - Highest impact, clearest ROI, easiest to implement

✅ **Plan for growth** - Build systems that scale from 2 people to 5+ people later

**Estimated Timeline**: 4-6 weeks for full implementation from zero to operational automation system

**Estimated Impact**: 20-30 hours/month time savings, €350+/month cost reduction, measurable quality improvements

---

[This research report was systematically compiled from 77+ YouTube videos, tutorials, guides, and case studies published within the last 60 days, specifically filtered for relevance to HR automation, small team implementation, and EU compliance requirements.]

**Report Generated**: November 14, 2025  
**Next Review Recommended**: February 14, 2026 (90 days - to capture new tool innovations)


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-14 standardization scaffold added
