---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: ASSIGNMENT_GUIDELINES
title: ASSIGNMENT GUIDELINES
date: 2025-11-24
status: archived
owner: unknown
related: []
links: []
---

# ASSIGNMENT GUIDELINES

## Summary
- TODO

## Context
- TODO

## Data / Content
# Research Assignment Guidelines

**Created:** 2025-11-21
**Location:** `ENTITIES/TASK_MANAGERS/RESEARCHES/LOGS/`
**Purpose:** Provide decision framework for manually assigning research tasks to employees

---

## Overview

This document provides a systematic approach to manually assigning research tasks to the right employees based on skills, availability, workload, and research type.

**Core Principle:** Match the right employee to the right research based on skills, capacity, and development opportunities.

---

## Assignment Decision Tree

```
START: New Research Task Identified
    ↓
1. What DEPARTMENT does this research serve?
    → AI, Design, Dev, LG, Video, HR, Sales, SMM
    ↓
2. What RESEARCH TYPE is this?
    → Video Phase 5-7, Tool Research, Workflow Analysis, Gap Analysis, Market Research
    ↓
3. What SKILLS are required?
    → Check DEPARTMENT_GAP_ANALYSIS.md for required skills
    ↓
4. Check ACTIVE_EMPLOYEES_LIST.md:
    ├─ Any "Available" employees with matching department + skills?
    │   ├─ YES → Go to Step 5
    │   └─ NO → Check "Work" status employees with matching skills
    │       ├─ YES → Check workload capacity → Go to Step 5
    │       └─ NO → Consider cross-training opportunity → Go to Step 5
    ↓
5. Check EMPLOYEE_RESEARCH_HISTORY.md:
    ├─ Has employee done similar research before?
    │   ├─ YES → Check quality score
    │   │   ├─ Score 7+ → Good candidate
    │   │   └─ Score <7 → Consider if improvement opportunity
    │   └─ NO → Is this a good learning opportunity?
    ↓
6. Check WEEKLY_RESEARCH_PLAN.md:
    ├─ How many tasks already assigned to this employee this week?
    │   ├─ 0-1 tasks → OK to assign
    │   ├─ 2 tasks → Check total hours (max 8 hours/week for Available)
    │   └─ 3+ tasks → Avoid unless critical and employee requests it
    ↓
7. ASSIGN:
    → Update RESEARCH_ASSIGNMENT_LOG.md
    → Update WEEKLY_RESEARCH_PLAN.md
    → Notify employee (outside this system)
    ↓
END
```

---

## Skill Matching Matrix

### AI Department Research

**Required Skills:** AI Tools, Prompt Engineering, Automation, AI Model Knowledge

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Perederii Vladislav (86246) | ⭐⭐⭐ Perfect | 1st choice | Available, Prompt Engineer |
| Artemchuk Nikolay (37226) | ⭐⭐ Good | 2nd choice | Work status, Project Manager |

**Fallback:** Assign to Development employees (Azar Imranov, Klimenko Yaroslav) for AI coding tools research

---

### Video Department Research

**Required Skills:** Video Editing, Post-production, Transcription, AI Video Tools

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Azanova Darya (80190) | ⭐⭐⭐ Perfect | 1st choice | Available, Video Editor |
| Podolskyi Sviatoslav (299) | ⭐⭐⭐ Perfect | 2nd choice | Work status, Video Editor |

**Fallback:** Assign to Design employees for video-related design research (motion graphics, etc.)

---

### Design Department Research

**Required Skills:** UI/UX, Graphic Design, Illustration, Design Tools, Figma

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Shymkevych Iryna (88357) | ⭐⭐⭐ Perfect | 1st choice | Available, UI/UX Designer |
| Safonova Eleonora (87995) | ⭐⭐⭐ Perfect | 1st choice | Available, UI/UX Designer |
| Skrypkar Vilhelm (333) | ⭐⭐ Good | 3rd choice | Available, Illustrator |

**Fallback:** None needed - 3 available designers

---

### Development Department Research

**Required Skills:** Frontend, Backend, Full Stack, DevOps, Git, VS Code, Testing

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Azar Imranov (88645) | ⭐⭐⭐ Perfect | 1st choice | Available, Full Stack |
| Klimenko Yaroslav (86478) | ⭐⭐⭐ Perfect | 2nd choice | Available, Frontend |
| Artem Skichko (88853) | ⭐⭐⭐ Perfect | 3rd choice | Available, Frontend |
| Kizilova Olha (178) | ⭐⭐ Good | 4th choice | Work status, Backend |
| Danylenko Liliia (72754) | ⭐⭐ Good | 5th choice | Work status, Full Stack |

**Fallback:** None needed - 5 development employees

---

### Lead Generation Department Research

**Required Skills:** Lead Generation, Email Enrichment, Scraping, CRM, LinkedIn, Social Media

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Davlatmamadova Firuza (84059) | ⭐⭐⭐ High | 1st choice | Available |
| Archibong Isaac (86453) | ⭐⭐ Medium | 2nd choice | Available |
| Bindiak Dana (87396) | ⭐⭐ Medium | 3rd choice | Available |
| Shkinder Kseniia (87157) | ⭐⭐ Medium | 4th choice | Work status |

**Fallback:** None needed - 9 lead gen employees (8 available)

---

### HR Department Research

**Required Skills:** Recruitment, HR Operations, Talent Management, Performance Management

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Nealova Evgeniya (72889) | ⭐⭐⭐ Perfect | 1st choice | Work status but 1.25 rate (extra capacity) |
| Pasichna Anastasiia (88105) | ⭐⭐ Good | 2nd choice | Work status |
| Rekonvald Viktoriya (83953) | ⭐ Limited | Avoid | Work status 0.5 rate (limited capacity) |

**Fallback:** Assign to AI employees for AI recruitment tool research

---

### Sales Department Research

**Required Skills:** Sales, CRM, Client Relations, Sales Automation, Proposal Writing

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Kovalska Anastasiya (45405) | ⭐⭐⭐ Perfect | 1st choice | Work status |
| Bessarab Valeriia (88972) | ⭐⭐⭐ Perfect | 2nd choice | Work status |

**Fallback:** Assign to Lead Gen employees for CRM/sales tool research

---

### SMM Department Research

**Required Skills:** Social Media Marketing, Content Creation, Analytics, Influencer Marketing

| Employee | Skills Match | Priority | Notes |
|----------|--------------|----------|-------|
| Shymkevych Iryna (88357) | ⭐⭐ Good | 1st choice | Designer with social media potential |
| Lead Gen employees | ⭐ Fair | Fallback | Experience with social media scraping |

**Gap:** No dedicated SMM employees identified
**Solution:** Cross-train Design or Lead Gen employees, or assign based on social media tool experience

---

## Research Type Guidelines

### Video Phase 5-7 (Gap Analysis + Library Mapping)

**Time:** 1-2 hours per video
**Skills Required:** Video knowledge OR AI tools OR department expertise (varies by video content)

**Assignment Logic:**
1. Check video content topic (AI, Design, Development, etc.)
2. Assign to employee from that department if available
3. Otherwise assign to Video department employees (Azanova, Podolskyi)
4. Fallback: AI employees (can handle any video processing)

**Example:**
- Video_006 (Lead Generation) → Davlatmamadova Firuza (Lead Gen) OR Artemchuk Nikolay (AI)
- Video_008 (Claude MCP) → Perederii Vladislav (AI/Prompt Engineer)
- Video_017 (Midjourney) → Shymkevych Iryna (Designer)

---

### Tool Research (2-3 hours)

**Skills Required:** Department-specific + research skills

**Assignment Logic:**
1. Must match department (AI tools → AI employee)
2. Prefer "Available" status
3. Check for prior tool research experience
4. Assign to employee who would USE the tool (practical knowledge)

**Example:**
- Research AI Coding Assistants → Azar Imranov (Developer who would use Cursor/Archon)
- Research Email Enrichment APIs → Davlatmamadova Firuza (Lead Gen who would use the tools)

---

### Workflow Analysis (2-3 hours)

**Skills Required:** Process thinking + department knowledge

**Assignment Logic:**
1. Assign to employee who PERFORMS the workflow
2. Prefer experienced employees (quality over speed)
3. Can be learning opportunity for junior employees

**Example:**
- N8N Workflow Analysis → Artemchuk Nikolay (Project Manager, automation experience)
- Design System Automation → Shymkevych Iryna (UI/UX, design systems)

---

### Gap Analysis (2-3 hours)

**Skills Required:** Strategic thinking + department expertise + LIBRARIES knowledge

**Assignment Logic:**
1. Must be senior/experienced in department
2. Requires understanding of current vs. desired state
3. Prefer employees who have completed research before (knows taxonomy)

**Example:**
- Design Department Gap Analysis → Shymkevych Iryna or Safonova Eleonora (Designers)
- Development Gap Analysis → Azar Imranov (Full Stack, broad perspective)

---

### Market Research (2-4 hours)

**Skills Required:** Research skills + internet research + data synthesis

**Assignment Logic:**
1. Can assign to any employee with good research skills
2. Prefer "Available" status (more time for thorough research)
3. Good for cross-training opportunities

---

## Workload Management

### Maximum Weekly Hours by Status

| Employee Status | Max Research Hours/Week | Reasoning |
|----------------|------------------------|-----------|
| Available (Rate 1.0) | 8 hours | Full availability for projects |
| Work (Rate 1.25) | 6 hours | Extra capacity beyond normal workload |
| Work (Rate 1.0) | 4 hours | Must balance with existing work |
| Work (Rate 0.5) | 0 hours | Limited availability - avoid assignments |

### Task Distribution Guidelines

**Per Employee Per Week:**
- **Ideal:** 1-2 research tasks
- **Maximum:** 3 research tasks (only if employee requests or critical need)
- **Monitor:** If same employee assigned 3 weeks in a row, rotate to others

**Per Department Per Week:**
- **Avoid:** Assigning all tasks to one department
- **Balance:** Spread research across departments when possible
- **Prioritize:** High-priority gaps get resources first

---

## Quality Considerations

### First-Time Researcher

**If employee has never done research before:**
- ✅ Start with simple tool research (2 hours)
- ✅ Provide extra guidance and examples
- ✅ Plan for review/revision time
- ❌ Avoid complex gap analysis or workflows as first task

### Proven High-Quality Researcher (Score 8+)

**If employee has track record of excellent research:**
- ✅ Assign complex/critical research
- ✅ Trust with minimal oversight
- ✅ Can assign multiple tasks if they have capacity
- ✅ Consider for training/mentoring others

### Inconsistent Quality (Score 5-7)

**If employee has mixed quality scores:**
- ⚠️ Assign medium-complexity tasks
- ⚠️ Provide clear requirements and examples
- ⚠️ Plan for quality review before completion
- ⚠️ Consider pairing with high-quality researcher

### Low Quality (Score <5)

**If employee consistently produces low-quality research:**
- ❌ Avoid critical research assignments
- ✅ Assign only with mentorship/training plan
- ✅ Provide detailed template and examples
- ✅ Review work in progress (not just final)

---

## Special Scenarios

### Scenario 1: No Perfect Match Available

**Problem:** Research requires skills but no employee with those exact skills is available

**Solution:**
1. Identify closest skill match (e.g., Frontend developer for Full Stack research)
2. Check if research could be learning opportunity
3. Provide extra resources (tutorials, examples)
4. Allow extra time for learning curve

**Example:** SMM research but no SMM employee → Assign to Designer with social media interest + provide SMM tool tutorials

---

### Scenario 2: All Available Employees Fully Loaded

**Problem:** All "Available" status employees at max capacity, "Work" status employees can't take more

**Solution:**
1. Re-prioritize research tasks (defer low priority)
2. Check if any in-progress tasks can be completed first
3. Consider extending deadlines
4. Review if any "Work" status employees have capacity exceptions

---

### Scenario 3: Critical Research, Employee Doesn't Want It

**Problem:** Best-match employee declines or unavailable

**Solution:**
1. Find second-best match from skills matrix
2. Check if task can be split (2 employees collaborate)
3. Consider if research can be deferred
4. Last resort: Assign to willing employee + provide significant support

---

### Scenario 4: Employee Requests Specific Research

**Problem:** Employee interested in research outside their department

**Solution:**
1. ✅ Allow if: (a) Employee has capacity, (b) Research not time-critical, (c) Skills transferable
2. ✅ Good for: Cross-training, skill development, employee engagement
3. ⚠️ Provide extra time and resources
4. ⚠️ Monitor quality closely (first time in new area)

**Example:** Developer wants to research AI video tools → Allow as learning opportunity if not urgent

---

## Assignment Checklist

Before assigning research, verify:

- [ ] **Skills Match:** Employee has required skills (or close enough with support)
- [ ] **Availability:** Employee status is "Available" OR "Work" with confirmed capacity
- [ ] **Workload:** Employee not exceeding max hours/week for their status
- [ ] **History:** Checked past research quality if employee has history
- [ ] **Priority:** Research priority matches employee availability (High priority → Available status preferred)
- [ ] **Timeline:** Deadline realistic given employee's other commitments
- [ ] **Support:** Employee has resources needed (prompts, examples, tools access)

After assigning:

- [ ] **Log Update:** Updated RESEARCH_ASSIGNMENT_LOG.md with assignment details
- [ ] **Plan Update:** Updated WEEKLY_RESEARCH_PLAN.md with task and employee
- [ ] **Notification:** Employee notified (outside this system)
- [ ] **Calendar:** Due date and check-in dates set

---

## Monthly Review Process

**Every Month (1st Monday):**

1. **Review Completion Rates:**
   - Which employees consistently complete on time?
   - Which employees need deadline adjustments?

2. **Review Quality Scores:**
   - Identify top performers (recognize/reward)
   - Identify quality issues (training/support)

3. **Review Workload Distribution:**
   - Any employees over/under utilized?
   - Any departments neglected?

4. **Update Employee Skills:**
   - Have employees gained new research skills?
   - Update ACTIVE_EMPLOYEES_LIST.md with new capabilities

5. **Adjust Guidelines:**
   - Any patterns requiring guideline updates?
   - Any new research types requiring new matching rules?

---

## Related Documentation

- [Active Employees List](ACTIVE_EMPLOYEES_LIST.md) - Who's available and their skills
- [Department Gap Analysis](DEPARTMENT_GAP_ANALYSIS.md) - What research is needed
- [Employee Research History](EMPLOYEE_RESEARCH_HISTORY.md) - Past performance
- [Research Assignment Log](RESEARCH_ASSIGNMENT_LOG.md) - All active assignments
- [Weekly Research Plan](WEEKLY_RESEARCH_PLAN.md) - This week's priorities
- [How to Assign Research](HOW_TO_ASSIGN_RESEARCH.md) - Step-by-step walkthrough

---

*Created: 2025-11-21*
*Last Updated: 2025-11-21*
*Next Review: 2025-12-01*


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
