# Phase 0 Weekly Analysis - Step-by-Step Prompt

**Purpose:** Guide Research Manager through weekly Phase 0 analysis
**Frequency:** Every Monday, 1-1.5 hours
**Output:** Weekly analysis file identifying research priorities

---

## Before You Begin

**Time Required:** 1-1.5 hours
**Best Time:** Monday 9:00-10:30 AM
**Prerequisites:**
- [ ] Coffee/tea ready (you'll be thinking strategically)
- [ ] Previous week's completions reviewed
- [ ] No interruptions for next 90 minutes

**Files to Have Open:**
1. `DEPARTMENT_GAP_ANALYSIS.md` (gap inventory)
2. `RESEARCH_COMPLETION_TRACKER.md` (last week's completions)
3. `EMPLOYEE_RESEARCH_HISTORY.md` (quality scores)
4. `ACTIVE_EMPLOYEES_LIST.md` (availability)
5. `WEEKLY_RESEARCH_PLAN.md` (current priorities)
6. `Phase_0_Template.md` (for creating new analysis)

---

## Section 1: Last Week Review (10 minutes)

**Skip this section if:** This is your first Phase 0 analysis (no previous data)

### 1.1: Check Completions

**Open:** `RESEARCH_COMPLETION_TRACKER.md`

**Questions to Answer:**
1. How many research tasks were completed last week?
2. Which assignment IDs were completed? (e.g., RSH-VID-001, RSH-AI-003)
3. What departments benefited from the research?

**Document in your analysis:**
```markdown
## Last Week Review

### Completed Research ✅
| Assignment ID | Task | Completed By | Quality Score | Outcome |
|---------------|------|--------------|---------------|---------|
| RSH-VID-001 | Video_006 Gap Analysis | [Name] | [Score]/10 | [Brief outcome] |
| RSH-AI-003 | Gemini 2.0 Research | [Name] | [Score]/10 | [Brief outcome] |
```

### 1.2: Check Quality Scores

**Open:** `EMPLOYEE_RESEARCH_HISTORY.md`

**Questions to Answer:**
1. What was the average quality score for completed tasks?
2. Were there any exceptional performances (9-10/10)?
3. Were there any issues requiring attention (<6/10)?

**Document:**
- Average score: X.X/10
- High performers: [Names]
- Areas for improvement: [Notes if any]

### 1.3: Check Gap Closure

**Open:** `DEPARTMENT_GAP_ANALYSIS.md`

**Look for gaps marked:**
- Status changed to "Closed" or "Partially Closed"
- Addressed By: RSH-XXX-### (research assignment IDs)

**Questions to Answer:**
1. Which gaps were closed or partially closed?
2. What impact did this research have? (tools added, workflows documented)
3. What remains to fully close the gap?

**Document:**
```markdown
### Gaps Closed ✅
- **GAP-ID:** [Description]
  - Status: Partially Closed (or Fully Closed)
  - Addressed By: RSH-XXX-###
  - Tools Added: [List]
  - Workflows Added: [List]
  - Remaining: [What's still needed, if partially closed]
```

### 1.4: Check LIBRARIES Growth

**Quick check (not deep dive):**
- Scan `LIBRARIES/Tools/` - any new entries last week?
- Scan `LIBRARIES/Workflows/` - any new entries?
- Count approximate additions: X tools, Y workflows

**Document:**
```markdown
### New Discoveries ✅
- **Tools:** X new tools added to LIBRARIES
- **Workflows:** Y new workflows documented
- **Impact:** [Which departments now have better resources]
```

---

## Section 2: Current Department Status (5 minutes)

**Open:** `REPORTS/` (optional - if using daily report analysis)

**Questions to Answer:**
1. Are there any urgent/emerging needs from department reports?
2. Any recurring challenges mentioned multiple times?
3. Any new tools/technologies mentioned worth researching?

**If NOT using daily reports:**
- Skip this section, or
- Note general department priorities you're aware of (project launches, new initiatives)

**Document:**
```markdown
## Current Department Status

### Emerging Needs
- **AI Department:** [Any urgent needs or skip]
- **Design Department:** [Any urgent needs or skip]
- **Development:** [Any urgent needs or skip]
- **Lead Gen:** [Any urgent needs or skip]
- **Video:** [Any urgent needs or skip]
- **HR:** [Any urgent needs or skip]
- **Sales:** [Any urgent needs or skip]
- **SMM:** [Any urgent needs or skip]

### Notes
- [Any cross-department trends]
- [Any blockers to be aware of]
```

---

## Section 3: Gap Identification (10 minutes)

**Open:** `DEPARTMENT_GAP_ANALYSIS.md`

**Review top priorities:**
- Scan all departments
- Focus on "High" priority gaps
- Consider "Medium" if capacity exists

**Questions to Answer:**
1. Which gaps are most urgent? (business impact + time sensitivity)
2. Which gaps are most impactful? (benefit many employees or critical workflows)
3. Which gaps are easiest to close? (quick wins, 1-2 hour tasks)
4. Which gaps have available employees to research? (skill match)

**Document:**
```markdown
## Gap Identification

### Top Priority Gaps (this week)
1. **[GAP-ID]:** [Description]
   - Department: [Dept]
   - Impact: [High/Medium/Low]
   - Urgency: [High/Medium/Low]
   - Estimated Research: [X hours]
   - Skills Needed: [List]

2. **[GAP-ID]:** [Description]
   - [Same format]

3. **[GAP-ID]:** [Description]
   - [Same format]

[Continue for 5-7 top gaps]
```

**Pro Tip:** Don't analyze ALL 24 gaps - focus on top 5-7. You can't assign everything this week anyway.

---

## Section 4: Priority Scoring (10 minutes)

**Now score your top gaps using this formula:**

**Priority Score = (Urgency × 3) + (Impact × 2)**

**Urgency (1-10):**
- 10 = Needed THIS WEEK (blocking work)
- 7-9 = Needed soon (next 2-3 weeks)
- 4-6 = Important but can wait
- 1-3 = Nice to have

**Impact (1-10):**
- 10 = Affects 10+ employees or critical business function
- 7-9 = Affects 5-9 employees or important function
- 4-6 = Affects 2-4 employees or useful enhancement
- 1-3 = Affects 1 employee or minor improvement

**Document:**
```markdown
## Priority Scoring

| Gap ID | Description | Urgency | Impact | Priority Score | Rank |
|--------|-------------|---------|--------|----------------|------|
| LGN-GAP-001 | Email Enrichment | 8 | 9 | (8×3)+(9×2) = 42 | 1 |
| AI-GAP-002 | MCP Connectors | 7 | 8 | (7×3)+(8×2) = 37 | 2 |
| DGN-GAP-001 | AI Design Tools | 6 | 9 | (6×3)+(9×2) = 36 | 3 |
| DEV-GAP-001 | AI Coding Tools | 5 | 7 | (5×3)+(7×2) = 29 | 4 |
| [Continue...] | | | | | |
```

**Sort by Priority Score (highest first)**

**Select top 2-4 for this week's assignments** based on:
- Priority score (highest wins)
- Employee availability (must have skilled employee available)
- Workload balance (don't overload one department)

---

## Section 5: Assignment Recommendations (5 minutes)

**For each top 2-4 priority gaps:**

**Create specific assignment recommendation:**

**Open:** `ACTIVE_EMPLOYEES_LIST.md`

**Match:**
- Gap skills needed → Employee skills
- Research complexity → Employee experience level
- Time estimate → Employee availability

**Document:**
```markdown
## Assignment Recommendations

### Recommendation 1: RSH-XXX-###
- **Task:** [Specific research task from gap]
- **Gap Addressed:** [GAP-ID]
- **Recommended Employee:** [Name (ID)]
- **Department:** [Dept]
- **Skills Match:** [How employee's skills match this research]
- **Estimated Time:** [X hours]
- **Suggested Deadline:** [Date - typically 5-7 days from Tuesday assignment]
- **Priority:** High/Medium/Low
- **Rationale:** [Why this employee + why this task this week]

### Recommendation 2: RSH-XXX-###
[Same format]

### Recommendation 3: RSH-XXX-###
[Same format]

### Recommendation 4: RSH-XXX-###
[Same format - optional if capacity exists]
```

**Pro Tip:**
- Start with 2-3 assignments/week if system is new
- Scale to 4-6/week once process is smooth
- Don't over-assign - better to complete 2 well than rush 5 poorly

---

## Section 6: Employee Availability Check (3 minutes)

**For each recommended employee:**

**Verify in `ACTIVE_EMPLOYEES_LIST.md`:**
- [ ] Status: "Available" (preferred) or "Work" (check capacity)
- [ ] Rate: 1.0 (full time) or 0.5 (half time - limited capacity)
- [ ] Skills: Match confirmed
- [ ] Recent research history: Not overloaded (check `EMPLOYEE_RESEARCH_HISTORY.md`)

**Document:**
```markdown
## Employee Availability Verification

| Employee | Status | Rate | Current Workload | Available for Research |
|----------|--------|------|------------------|----------------------|
| [Name 1] | Available | 1.0 | 0 active research | ✅ Yes - High capacity |
| [Name 2] | Work | 1.0 | 1 active research | ⚠️ Yes - if <2 hours |
| [Name 3] | Available | 0.5 | 0 active research | ⚠️ Yes - <1 hour task |
| [Name 4] | Available | 1.0 | 2 active research | ❌ No - overloaded |
```

**Adjust assignments if:**
- Preferred employee unavailable → substitute with backup
- Employee overloaded → defer to next week or assign to someone else
- No available employees → defer assignments to next week

---

## Section 7: Weekly Goals (2 minutes)

**Set clear, achievable goals for this week:**

**Questions:**
1. How many assignments will you make? (2-4 realistic)
2. What gaps will be addressed?
3. What departments will benefit?
4. What's the success criteria for the week?

**Document:**
```markdown
## Weekly Goals (Current Week)

### Research Assignments
- **Goal:** Assign [#] research tasks by Tuesday
- **Focus:** [Primary department or gap type]
- **Expected Completions:** [#] tasks due by end of week (from previous assignments)

### Gap Closure Targets
- Close or partially close [#] gaps
- Priority: [Which gaps]

### Department Focus
- **Primary:** [Dept] - [# tasks]
- **Secondary:** [Dept] - [# tasks]

### Success Criteria
- [ ] [#] assignments made and employees notified by Tuesday
- [ ] [#] completions reviewed and integrated to LIBRARIES by Friday
- [ ] Week-over-week progress visible (gaps closed, LIBRARIES grew)
- [ ] All employees feel supported and clear on expectations
```

---

## Post-Analysis Actions (10 minutes)

**After completing all 7 sections:**

### 1. Create Weekly Analysis File

**Save your analysis as:**
`[Month]_[Year]_Week_[#]_Analysis.md`

**Example:**
- `November_2025_Week_3_Analysis.md` (Nov 18-24)
- `December_2025_Week_1_Analysis.md` (Dec 2-8)

**Use `Phase_0_Template.md` as structure**

### 2. Archive Previous Week (if applicable)

**If starting a new week:**
```bash
# Create month folder if doesn't exist
mkdir ANALYSIS_HISTORY/2025_November/

# Move previous week's file
mv November_2025_Week_3_Analysis.md ANALYSIS_HISTORY/2025_November/Week_3_Analysis.md
```

### 3. Update WEEKLY_RESEARCH_PLAN.md

**Copy your weekly goals and assignment recommendations into:**
`WEEKLY_RESEARCH_PLAN.md`

**Update:**
- Current week dates
- High priority tasks (your assignments)
- Department focus

### 4. Prepare for Tuesday Assignments

**Monday afternoon or Tuesday morning:**
- Create assignment entries in `RESEARCH_ASSIGNMENT_LOG.md`
- Draft employee notification messages
- Set up reminders for Thursday check-ins

---

## Quality Checklist

**Before finishing Phase 0, verify:**

- [ ] All 7 sections completed (no major gaps)
- [ ] Last Week Review populated (or marked N/A if first cycle)
- [ ] At least 5 gaps reviewed and scored
- [ ] 2-4 specific assignment recommendations made
- [ ] Employee skills verified and matched
- [ ] Employee availability confirmed
- [ ] Weekly goals realistic and measurable
- [ ] Week-over-week comparison included (if previous data exists)
- [ ] File saved with correct naming convention
- [ ] Previous week archived (if applicable)
- [ ] WEEKLY_RESEARCH_PLAN updated

**If all checked:** Phase 0 complete! ✅

**If any unchecked:** Go back and complete that section before proceeding to assignments.

---

## Time Tracking

**Target times for each section:**
- Section 1 (Last Week Review): 10 min
- Section 2 (Department Status): 5 min
- Section 3 (Gap Identification): 10 min
- Section 4 (Priority Scoring): 10 min
- Section 5 (Assignment Recommendations): 5 min
- Section 6 (Availability Check): 3 min
- Section 7 (Weekly Goals): 2 min
- Post-Analysis Actions: 10 min
- **Total: ~55 minutes**

**Add 15-30 min for:**
- First time running Phase 0 (learning curve)
- Reviewing detailed completion data
- Complex prioritization decisions
- Creating comprehensive documentation

**Optimization Goal:** After 3-4 cycles, complete in 45-60 minutes

---

## Troubleshooting

### "I don't have any completions to review yet"

**Week 1-2:** Normal - system just starting
**Solution:** Skip Section 1 or write "N/A - first cycle"
**Focus:** Sections 3-5 (gap identification and assignments)

---

### "Too many priorities, can't choose"

**Problem:** Analysis paralysis with 24 gaps
**Solution:**
1. Only review top 7-10 gaps maximum
2. Use priority scoring formula strictly
3. Take top 3-4 by score
4. Don't overthink - good enough decisions are fine
5. You'll refine next week based on outcomes

---

### "No available employees for my top priorities"

**Problem:** Skill mismatch or workload issues
**Solution:**
1. Check "Work" status employees - may have 1-2 hour capacity
2. Consider easier research for available employees (skill stretch = learning opportunity)
3. Defer high-priority gaps to next week
4. Recruit new researchers (update `ACTIVE_EMPLOYEES_LIST.md`)

---

### "I'm taking 2+ hours on Phase 0"

**Problem:** Spending too much time on analysis
**Solution:**
1. Set timer for each section - move on when time's up
2. Use "good enough" not "perfect" - you'll iterate weekly
3. Skip optional sections (Section 2 if not using daily reports)
4. Don't review ALL gaps - focus on top priorities
5. Template saves time - use it!
6. Gets faster with practice - give it 3-4 cycles

---

### "Analysis feels like busywork"

**Problem:** Not seeing value in weekly analysis
**Check:**
1. Are you making 2-4 assignments based on analysis? (If no, analysis not actionable)
2. Are assignments completing? (If no, may be assigning wrong priorities)
3. Is LIBRARIES growing? (If no, research not integrating)
4. Are gaps closing? (If no, research not addressing gaps)

**If analysis drives action and results, it's valuable. If not, adjust process.**

---

## Quick Reference Card

**Phase 0 in 10 Steps:**
1. ☑️ Check last week's completions
2. ☑️ Check quality scores
3. ☑️ Check gaps closed
4. ☑️ Review top 5-7 gaps
5. ☑️ Score gaps (Urgency×3 + Impact×2)
6. ☑️ Recommend 2-4 assignments
7. ☑️ Match employees to tasks
8. ☑️ Verify availability
9. ☑️ Set weekly goals
10. ☑️ Create analysis file + update tracking

**Time:** 45-90 minutes
**Output:** Weekly analysis file with 2-4 assignment recommendations
**Next:** Tuesday assignments based on recommendations

---

**You're ready! Start with Section 1 and work through systematically. Good luck!** 🚀

**Next File:** [Phase_0_Template.md](Phase_0_Template.md) - Use this as your analysis structure
