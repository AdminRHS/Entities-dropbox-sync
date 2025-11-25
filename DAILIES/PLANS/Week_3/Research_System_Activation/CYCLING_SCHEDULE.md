# Research System Cycling Schedule

**Project:** Research System Activation & Cycling Implementation
**Created:** 2025-11-21
**Purpose:** Define the operational rhythm and timing for weekly/monthly research cycles

---

## Overview

The research system operates on a **weekly cycle** with **monthly reviews** and **quarterly planning**. This document defines exactly when each activity happens, who's responsible, and how long it takes.

**Core Principle:** Every Monday triggers a new research cycle through Phase 0 analysis. The cycle completes Friday with quality review and LIBRARIES integration, setting up the next Monday's analysis.

---

## Weekly Cycle (Steady-State Operations)

### Monday - Phase 0 Analysis Day

**Time Block:** 9:00 AM - 10:30 AM (1.5 hours)
**Owner:** Research Manager
**Priority:** CRITICAL - This drives the entire week

#### Schedule

**9:00-9:15 AM: Data Gathering (15 min)**
- Review RESEARCH_COMPLETION_TRACKER for last week's completions
- Check EMPLOYEE_RESEARCH_HISTORY for new quality scores
- Review DEPARTMENT_GAP_ANALYSIS for gaps marked closed
- Scan REPORTS (if using daily report analysis) for emerging needs
- Check employee availability in ACTIVE_EMPLOYEES_LIST

**9:15-10:00 AM: Phase 0 Analysis (45 min)**
- Open Phase_0_Analysis_Prompt.md
- Work through all 7 sections systematically:
  1. Last Week Review (10 min) - What was completed, what gaps closed
  2. Current Department Status (5 min) - Any urgent needs from reports
  3. Gap Identification (10 min) - Review DEPARTMENT_GAP_ANALYSIS priorities
  4. Priority Scoring (10 min) - Score top 10 gaps by urgency + impact
  5. Assignment Recommendations (5 min) - Match gaps to employee skills
  6. Employee Availability Check (3 min) - Verify recommended employees available
  7. Weekly Goals (2 min) - Set 2-4 priorities for the week

**10:00-10:30 AM: Documentation (30 min)**
- Create weekly analysis file: `[Month]_[Year]_Week_[#]_Analysis.md`
- Use Phase_0_Template.md structure
- Include week-over-week comparison if available
- Archive previous week's analysis to ANALYSIS_HISTORY (if new week starts)
- Update WEEKLY_RESEARCH_PLAN with this week's priorities

**Deliverable:** Weekly analysis file created, priorities identified, ready for assignments

---

### Tuesday - Assignment Day 1

**Time Block:** 2:00 PM - 3:00 PM (1 hour)
**Owner:** Research Manager
**Priority:** HIGH - Start week strong with clear assignments

#### Schedule

**2:00-2:30 PM: Assignment Creation (30 min)**
- Review Monday's Phase 0 priorities (top 2-3 items)
- Create assignment entries in RESEARCH_ASSIGNMENT_LOG
- Assign unique IDs: RSH-{DEPT}-### format
- Match priorities to employee skills and availability
- Set realistic deadlines (typically 5-7 days for 1-2 hour tasks)
- Update WEEKLY_RESEARCH_PLAN with assignments

**2:30-3:00 PM: Employee Notification (30 min)**
- Prepare notification for each employee
- Use Employee_Notification_Template.md (after Phase 4) or custom message
- Include: Task description, deadline, resources, estimated time, deliverables
- Send via Discord/Email/preferred channel
- Note notification sent in RESEARCH_ASSIGNMENT_LOG

**Target:** 2-3 assignments made and communicated

---

### Wednesday - Assignment Day 2 (if needed)

**Time Block:** 10:00 AM - 10:30 AM (30 min)
**Owner:** Research Manager
**Priority:** MEDIUM - Additional assignments or follow-ups

#### Schedule

**10:00-10:30 AM: Additional Assignments or Check-ins (30 min)**
- If capacity exists: Assign 1-2 more tasks from Monday's priorities
- If no new assignments: Check in with employees on active tasks
  - "How's [assignment] going? Any questions?"
  - Offer to review work-in-progress
  - Note any blockers or concerns
- Update WEEKLY_RESEARCH_PLAN with status notes

**Flexibility:** This slot is optional - skip if week is fully assigned or use for other research admin tasks

---

### Thursday - Mid-Week Check & Support

**Time Block:** 3:00 PM - 3:30 PM (30 min)
**Owner:** Research Manager
**Priority:** MEDIUM - Keep momentum, prevent stalls

#### Schedule

**3:00-3:30 PM: Active Research Support (30 min)**
- Review status of all active assignments
- Identify tasks approaching deadline (next 2-3 days)
- Send reminders if needed: "Reminder: [task] due [date]. Need an extension?"
- Answer any questions from employees
- Update RESEARCH_ASSIGNMENT_LOG with progress notes
- Flag any at-risk tasks for Friday review

**Goal:** No surprises on Friday - know what's coming

---

### Friday - Review & Integration Day

**Time Block:** 1:00 PM - 4:00 PM (3 hours)
**Owner:** Research Manager + Librarian (if separate role)
**Priority:** CRITICAL - Close the loop

#### Schedule

**1:00-2:30 PM: Quality Review (1.5 hours)**
- Review all submissions received this week
- Use QUALITY_REVIEW_PROCESS.md checklist
- For each submission:
  - Completeness check (40 points)
  - Accuracy verification (30 points)
  - Quality assessment (20 points)
  - Actionability evaluation (10 points)
  - Calculate quality score (0-10 scale)
  - Write feedback (if score <7 or if helpful)
- Update RESEARCH_ASSIGNMENT_LOG (status: Completed)
- Update EMPLOYEE_RESEARCH_HISTORY with scores and outcomes
- Update RESEARCH_COMPLETION_TRACKER with new completions

**Time per Review:** 30-45 min for 1-2 hour research task

**2:30-3:45 PM: LIBRARIES Integration (1.25 hours)**
- Extract findings from approved research
- Add new tools to LIBRARIES/Tools/[Department]_Tools/
- Add new workflows to LIBRARIES/Workflows/[Department]_Workflows/
- Catalog new skills to LIBRARIES/Skills/ (if applicable)
- Cross-reference: Include research ID in each library entry
- Update DEPARTMENT_GAP_ANALYSIS: Mark gaps as closed/partially closed
- Verify all findings cataloged (nothing lost)

**Time per Integration:** 30-60 min for 1-2 hour research task

**3:45-4:00 PM: Recognition & Wrap-Up (15 min)**
- Send thank-you messages to all employees who submitted
- Use Completion_Thank_You_Template.txt (after Phase 4) or custom message
- Include: Quality score, specific praise, impact explanation
- Note any follow-up needed for next week
- Quick status update in WEEKLY_RESEARCH_PLAN

**Deliverable:** All submissions reviewed, integrated to LIBRARIES, employees thanked, ready for Monday

---

## Weekly Time Investment Summary

| Day | Activity | Time | Owner |
|-----|----------|------|-------|
| Monday | Phase 0 Analysis | 1.5 hours | Research Manager |
| Tuesday | Assignments | 1 hour | Research Manager |
| Wednesday | Check-ins (optional) | 0.5 hours | Research Manager |
| Thursday | Support | 0.5 hours | Research Manager |
| Friday | Review + Integration | 3 hours | Research Manager + Librarian |
| **TOTAL** | **Weekly Management** | **6.5 hours** | **Research Manager** |

**Employee Time:** 2-4 employees × 1-2 hours = 2-8 hours/week

**Total System Time:** 8.5-14.5 hours/week

---

## Monthly Cycle

### First Monday of Month - Monthly Review

**Time Block:** In addition to regular Phase 0 (add 1 hour)
**Owner:** Research Manager
**Priority:** HIGH - Strategic assessment

#### Schedule

**Additional 1 hour after Phase 0 Analysis:**

**10:30-11:00 AM: Data Aggregation (30 min)**
- Collect all completion data from last month
- Calculate monthly metrics (from SUCCESS_METRICS.md):
  - Total tasks completed
  - Average quality score
  - Employee participation count
  - LIBRARIES additions count
  - Gaps closed count
  - Completion rate
- Identify top performers (by volume and quality)
- Calculate department impact (tasks per department)

**11:00-11:30 AM: Monthly Review Report (30 min)**
- Use Monthly_Review_Report_Template.md (after Phase 4)
- Fill in all metrics
- Write "What Went Well" section (3-5 bullets)
- Write "Challenges Encountered" section (3-5 bullets)
- Write "Next Month Priorities" section (3-5 bullets)
- Save as: `Monthly_Review_[Month]_[Year].md`
- Archive to appropriate folder

**Deliverable:** Monthly review completed, trends identified, next month priorities set

---

### Mid-Month - Archive Cleanup

**Time Block:** 3rd Monday of month, after Phase 0 (add 15 min)
**Owner:** Research Manager
**Priority:** LOW - Housekeeping

#### Schedule

**10:30-10:45 AM: Archive Maintenance (15 min)**
- Review ANALYSIS_HISTORY folder structure
- Ensure previous weeks properly archived
- Verify month folders organized correctly
- Check for any orphaned files
- Clean up if needed

**Optional:** Can skip if archive process is working smoothly week-to-week

---

### Last Friday of Month - Employee List Update

**Time Block:** After regular Friday review (add 30 min)
**Owner:** Research Manager
**Priority:** MEDIUM - Maintain accurate availability

#### Schedule

**4:00-4:30 PM: Employee Availability Refresh (30 min)**
- Review ACTIVE_EMPLOYEES_LIST.md
- Check if any "Available" employees now "Busy" (project changes)
- Check if any "Busy" employees now "Available" (projects completed)
- Update employee status based on Finance data or direct knowledge
- Note any new employees who could be researchers
- Update skill tags if employees gained new capabilities

**Deliverable:** Current employee list for next month's assignments

---

## Quarterly Cycle (Future State)

### First Week of Quarter - Strategic Review

**Time Block:** 2-3 hours during first week
**Owner:** Research Manager + Leadership
**Priority:** HIGH - Strategic planning

#### Agenda

**Quarterly Review (1.5 hours):**
- Review all monthly reports from last quarter
- Calculate quarterly metrics
- Analyze trends (quality, participation, gap closure)
- Assess ROI on research investment
- Identify success stories and challenges

**Quarterly Planning (1 hour):**
- Set priorities for next quarter
- Adjust resource allocation if needed
- Plan any system improvements
- Update goals and targets
- Create roadmap for next 3 months

**Deliverable:** Quarterly review report, next quarter roadmap

---

## Special Events & Exceptions

### Phase 0 Falls on Holiday

**Action:** Run Phase 0 on Tuesday instead
**Note:** Adjust entire week schedule by 1 day
**Communication:** Notify employees of shifted deadlines

### Research Manager Unavailable

**Backup Plan:**
- Designate backup Phase 0 runner (train in advance)
- Can skip mid-week check-ins if needed
- Quality review can shift to following Monday if critical
- NEVER skip Phase 0 - this breaks the cycle

### High Volume Week (6+ active tasks)

**Adjustments:**
- Friday review may extend to 4-5 hours
- Consider splitting review across Fri + Mon
- May skip new assignments on Tuesday to catch up
- Prioritize quality over quantity

### Low Activity Week (0-1 completions)

**Adjustments:**
- Friday review only 30-60 minutes
- Use extra time for process improvements
- Review backlog, plan future priorities
- Reach out to employees to build pipeline

---

## Time Optimization Tips

### Save Time on Phase 0 Analysis

- Keep DEPARTMENT_GAP_ANALYSIS.md current (update during Friday integration)
- Use last week's analysis as starting point
- Template saves 10-15 min (after Phase 4)
- Focus on top 5-7 priorities, don't analyze everything

### Save Time on Assignments

- Use templates for notifications (after Phase 4)
- Batch create assignments (not one-by-one)
- Reuse similar task descriptions
- Keep employee skills fresh in mind

### Save Time on Quality Review

- Use checklist template (after Phase 4)
- Spot-check accuracy (don't verify every line)
- Accept "good enough" (score 6+ acceptable)
- Request revisions only if critical gaps

### Save Time on LIBRARIES Integration

- Integrate immediately after review (context fresh)
- Use consistent naming conventions
- Cross-reference research ID in batch (not one-by-one)
- Accept simple entries (can enrich later)

**Goal:** Reduce weekly time from 6.5 hours to 5 hours by Month 3

---

## Automation Opportunities (Future)

### Week 1-2 (Manual Process)
- All steps manual as described above
- Focus on learning the rhythm
- Identify pain points

### Month 2-3 (Template Automation)
- Notification templates save 20 min/week
- Review checklists save 15 min/week
- Report templates save 20 min/month

### Month 4-6 (Potential Automation)
- Automated reminders for approaching deadlines
- Auto-populate Phase 0 data sections
- Dashboard for quick metric viewing
- Integration scripts for LIBRARIES entries

### Month 7+ (Full Optimization)
- Consider research assignment automation
- Employee skill matching algorithms
- Trend analysis and reporting automation
- Integration with TASK_MANAGERS for complex projects

---

## Rhythm Examples

### Example Week 1 (November Week 3 - First Cycle)

**Monday, Nov 18:**
- 9:00 AM: Phase 0 analysis (first time, may take 2 hours learning)
- Create November_2025_Week_3_Analysis.md
- Identify: Video_006 and Video_008 as priorities

**Tuesday, Nov 19:**
- 2:00 PM: Create RSH-VID-001 and RSH-VID-002
- Notify Davlatmamadova Firuza and Perederii Vladislav
- Deadline: Nov 26 (7 days)

**Wednesday, Nov 20:**
- 10:00 AM: No additional assignments (only 2 employees available)
- Light check-in, prepare support materials

**Thursday, Nov 21:**
- 3:00 PM: Check in with both employees
- Answer questions, offer midpoint review

**Friday, Nov 22:**
- No completions yet (tasks just assigned)
- Use time for workflow documentation (Phase 1 Step 3)
- System status update

**Next Week:** Tasks due Tuesday Nov 26, review/integration Wednesday-Friday

---

### Example Week 2 (November Week 4 - First Completions)

**Monday, Nov 25:**
- 9:00 AM: Phase 0 (still no completions to review, normal)
- Light priority refresh, prepare for incoming completions

**Tuesday, Nov 26:**
- Receive RSH-VID-001 and RSH-VID-002 submissions
- Acknowledge receipt
- No new assignments (focus on review)

**Wednesday, Nov 27:**
- Quality review of both submissions (2-3 hours)
- Calculate scores, provide feedback

**Thursday, Nov 28:**
- LIBRARIES integration (2-3 hours)
- Add tools and workflows from research

**Friday, Nov 29:**
- Complete integration
- Send thank-you messages
- Update all tracking logs
- System now has first completion data!

---

### Example Week 3 (December Week 1 - Cycling Proven)

**Monday, Dec 2:**
- 9:00 AM: Phase 0 analysis (SECOND TIME - now with data!)
- Archive November_2025_Week_3_Analysis.md → ANALYSIS_HISTORY/2025_November/
- Create December_2025_Week_1_Analysis.md
- Include Last Week Review with real completions
- Include Week-over-Week Comparison
- Identify new priorities based on gaps closed

**Tuesday, Dec 3:**
- 2:00 PM: Assign RSH-VID-003 and RSH-VID-004
- Notify Perederii Vladislav (repeat) and Artem Skichko (new)
- Cycle continues!

**Rest of week:** Normal rhythm established

---

## Calendar Integration

### Recommended Calendar Blocks

**Recurring Events:**
- **Monday 9:00-10:30 AM:** "Phase 0 Research Analysis" (weekly, critical)
- **Tuesday 2:00-3:00 PM:** "Research Assignments" (weekly)
- **Thursday 3:00-3:30 PM:** "Research Check-ins" (weekly)
- **Friday 1:00-4:00 PM:** "Research Review & Integration" (weekly, critical)
- **First Monday of Month 10:30-11:30 AM:** "Monthly Research Review" (monthly)

**Protection:**
- Mark Phase 0 and Friday Review as "Do Not Schedule Over"
- Other blocks can flex if needed
- Minimum: Protect Monday Phase 0 and Friday afternoon

---

## Communication Rhythm

### Employee Communication

**Tuesday:** "Here's your research assignment for the week"
**Thursday:** "How's it going? Need any help?"
**Next Tuesday (deadline day):** "Reminder: Due today" (if not submitted)
**Friday (after review):** "Thanks for your submission! Score: [X]/10"

### Leadership Communication

**Monthly:** Monthly review report
**Quarterly:** Strategic review and planning session
**Ad-hoc:** Major milestones (system activation, first 10 completions, backlog cleared)

### Team Communication

**Weekly:** Update in team channel with highlights ("3 research tasks completed this week, 5 new tools added to LIBRARIES")
**Monthly:** Top performers recognition
**Quarterly:** Impact stories and case studies

---

## Flexibility & Adaptation

### When to Adjust the Schedule

**Indicators Schedule Needs Adjustment:**
- Consistently running over time blocks (30+ min)
- Consistently under-utilizing time blocks
- Employee feedback about timing
- Completion patterns different than expected
- Seasonal workload changes

**How to Adjust:**
1. Track actual time for 2-3 weeks
2. Identify consistent variances
3. Adjust time blocks ±30 min
4. Test new schedule for 2 weeks
5. Iterate until rhythm feels natural

**Acceptable Variations:**
- Phase 0: 1-2 hours (depends on complexity)
- Assignments: 0.5-1.5 hours (depends on count)
- Review: 2-4 hours (depends on submissions)
- Integration: 1-3 hours (depends on findings)

**Goal:** Find YOUR sustainable rhythm, not force-fit this schedule

---

## Success Indicators

**Good Rhythm Established When:**
- ✅ Phase 0 runs every Monday without fail
- ✅ Time blocks feel accurate (±15 min)
- ✅ Employees know when to expect assignments/feedback
- ✅ Reviews happen within 48 hours
- ✅ LIBRARIES integration within 7 days
- ✅ No tasks falling through cracks
- ✅ Manager time investment sustainable (5-7 hours/week)
- ✅ System feels like habit, not burden

---

## Document Control

**Version:** 1.0
**Created:** 2025-11-21
**Last Updated:** 2025-11-21
**Next Review:** 2025-12-22 (after Phase 4 complete)
**Owned By:** Research Manager

---

*This schedule provides the operational rhythm for a self-sustaining research system. Adapt timing to your actual needs, but maintain the Monday→Friday weekly cycle.*
