# Day 28 Manual Comparison Workflow

## Purpose
Compare TODO files (what was planned) with actual employee daily.md files (what was done) to identify updates and actual work completed on Day 28 (November 28, 2025).

---

## Main Principles of the Flow

### 1. Two-Source Comparison

**Source A: TODO Files (The Plan)**
- Location: `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\TODO_EXTRACTION\`
- File Pattern: `{Employee}_TODO_Day28_STRUCTURED.md`
- Contains: Planned tasks, estimated hours, priorities
- 16 files total across departments

**Source B: Employee Daily Reports (The Reality)**
- Location: `C:\Users\Dell\Dropbox\Nov25\{Department} Nov25\{Employee}\Week_4\28\`
- File Pattern: `daily.md`, `plans.md`, `task.md`, and all `.md`/`.txt` files
- Contains: Actual work done, time spent, deliverables

### 2. Comparison Methodology

For each of the 16 employees:

#### Step 1: Read the TODO File
- Open: `TODO_EXTRACTION/{Department}/{Employee}_TODO_Day28_STRUCTURED.md`
- Extract: Planned tasks from `## 📋 TASKS FOR DAY 28` section
- Note: Task IDs, priorities, estimated hours

#### Step 2: Read the Daily Report
- Navigate: `Nov25/{Department} Nov25/{Employee}/Week_4/28/`
- Read: `daily.md`, `plans.md`, `task.md`, and any other `.md`/`.txt` files
- Extract: What actually happened, time spent, completed work

#### Step 3: Compare & Identify Updates
- **Completed**: Which planned tasks were finished?
- **In Progress**: Which tasks were started but not completed?
- **Not Started**: Which planned tasks weren't touched?
- **Unplanned**: What work was done that wasn't in the TODO?
- **Time Variance**: Estimated vs actual hours spent

#### Step 4: Document Findings

Create a comparison entry:

```markdown
## Employee: {Name} ({ID})
**Department:** {Dept}

### Planned Tasks (from TODO)
1. [TASK-XXX-001] Task Name - Priority: High, Est: 2h
2. [TASK-XXX-002] Task Name - Priority: Medium, Est: 3h

### Actual Work (from daily.md)
- ✅ [TASK-XXX-001] COMPLETED - Actual: 2.5h
  - Outcome: Delivered XYZ
- 🔄 [TASK-XXX-002] IN PROGRESS - Actual: 1h
  - Status: 50% complete, blocked by ABC
- 🆕 UNPLANNED: Fixed critical bug in production
  - Time: 1.5h

### Summary
- Planned: 2 tasks, 5h estimated
- Completed: 1 task
- Time Spent: 5h actual
- Variance: +0h (on track)
- Unplanned Work: 1 item (1.5h)
```

---

## Workflow Steps

### Phase 1: Preparation (15 min)
1. Open TODO_EXTRACTION folder
2. Open Nov25 folder
3. Create comparison notes document: `Day28_TODO_vs_Actual_Comparison.md`
4. List all 16 employees to process

### Phase 2: Department-by-Department Comparison (3-4 hours)

#### Development Department (2 employees)
- [ ] Skichko Artem (DEV-002)
  - TODO: `TODO_EXTRACTION/Development/Skichko_Artem_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/DEV Nov25/Artem Skichko/Week_4/28/daily.md`
- [ ] Danylenko Liliia (DEV-001)
  - TODO: `TODO_EXTRACTION/Development/Danylenko_Liliia_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/DEV Nov25/Liliia Danylenko/Week_4/28/daily.md`

#### Lead Generation (4 employees)
- [ ] Burda Anna (LGN-001)
  - TODO: `TODO_EXTRACTION/Lead_Generation/Burda_Anna_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/LG Nov25/Anna Burda/Week_4/28/daily.md`
- [ ] Cynthia Aninwezi (LGN-XXX)
  - TODO: `TODO_EXTRACTION/Lead_Generation/Cynthia_Aninwezi_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/LG Nov25/Cynthia Aninwezi/Week_4/28/daily.md`
- [ ] Shkinder Kseniia (LGN-XXX)
  - TODO: `TODO_EXTRACTION/Lead_Generation/Shkinder_Kseniia_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/LG Nov25/Kseniia Shkinder/Week_4/28/daily.md`
- [ ] Davlatmamadova Firuza (LGN-XXX)
  - TODO: `TODO_EXTRACTION/Lead_Generation/Davlatmamadova_Firuza_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/LG Nov25/Firuza Davlatmamadova/Week_4/28/daily.md`

#### Finance (1 employee)
- [ ] Ponomarova Kateryna (FIN-001)
  - TODO: `TODO_EXTRACTION/Finance/Ponomarova_Kateryna_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Finance Nov25/Kateryna Ponomarova/Week_4/28/daily.md`

#### Design (1 employee)
- [ ] Shtepa Yuliia (DGN-001)
  - TODO: `TODO_EXTRACTION/Design/Shtepa_Yuliia_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Design Nov25/Yuliia Shtepa/Week_4/28/daily.md`

#### Executive (1 employee)
- [ ] Dembovsky Stas (EXE-001)
  - TODO: `TODO_EXTRACTION/Executive/Dembovsky_Stas_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Executive Nov25/Stas Dembovsky/Week_4/28/daily.md`

#### HR (2 employees)
- [ ] Pasichna Anastasiia (HR-XXX)
  - TODO: `TODO_EXTRACTION/HR/Pasichna_Anastasiia_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/HR Nov25/Anastasiia Pasichna/Week_4/28/daily.md`
- [ ] Rekonvald Viktoriya (HR-XXX)
  - TODO: `TODO_EXTRACTION/HR/Rekonvald_Viktoriya_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/HR Nov25/Viktoriya Rekonvald/Week_4/28/daily.md`

#### Human Resources (1 employee)
- [ ] Nealova Evgeniya (HRM-001)
  - TODO: `TODO_EXTRACTION/Human_Resources/Nealova_Evgeniya_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/HR Nov25/Evgeniya Nealova/Week_4/28/daily.md`

#### Sales (1 employee)
- [ ] Kovalska Anastasiya (SLS-001)
  - TODO: `TODO_EXTRACTION/Sales/Kovalska_Anastasiya_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Sales Nov25/Anastasiya Kovalska/Week_4/28/daily.md`

#### Video Production (2 employees)
- [ ] Podolskyi Sviatoslav (VID-001)
  - TODO: `TODO_EXTRACTION/Video_Production/Podolskyi_Sviatoslav_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Video Nov25/Sviatoslav Podolskyi/Week_4/28/daily.md`
- [ ] Azanova Darya (VID-002)
  - TODO: `TODO_EXTRACTION/Video_Production/Azanova_Darya_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/Video Nov25/Darya Azanova/Week_4/28/daily.md`

#### AI Automation (1 employee)
- [ ] Artemchuk Nikolay (AID-001)
  - TODO: `TODO_EXTRACTION/AI_Automation/Artemchuk_Nikolay_TODO_Day28_STRUCTURED.md`
  - Daily: `Nov25/AI Nov25/Nikolay Artemchuk/Week_4/28/daily.md`

### Phase 3: Aggregate Findings (30 min)
1. Count: How many tasks were completed vs planned?
2. Calculate: Total time estimated vs actual
3. Identify: Common patterns (tasks always taking longer, unplanned work)
4. Note: Blockers and issues mentioned

---

## Key Questions to Answer

### For Each Employee:
1. **Did they complete their planned tasks?**
   - Yes/No/Partially for each task
2. **Were there unplanned tasks?**
   - What unexpected work came up?
3. **Time accuracy:**
   - Were estimates accurate?
4. **Blockers:**
   - What prevented task completion?
5. **Deliverables:**
   - What concrete outputs were created?

### Aggregate Analysis:
1. **Completion Rate:** % of planned tasks completed
2. **Time Variance:** Avg difference between estimated and actual hours
3. **Unplanned Work:** % of time spent on unplanned items
4. **Department Patterns:** Which departments had most variance?
5. **Common Blockers:** Recurring issues across employees

---

## Output Format

### Individual Comparison (per employee)

```markdown
## {Employee_Name} ({Employee_ID}) - {Department}

### TODO File Analysis
- **Source:** TODO_EXTRACTION/{Dept}/{Name}_TODO_Day28_STRUCTURED.md
- **Tasks Identified:** 3
- **Total Estimated Hours:** 6.5h
- **Projects:** PROJ-DEV-005, PROJ-DEV-001

### Daily Report Analysis
- **Source:** Nov25/{Dept} Nov25/{Name}/Week_4/28/daily.md
- **Files Found:** daily.md, plans.md
- **Work Logged:** Yes/No
- **Time Tracked:** Yes/No

### Task-by-Task Comparison

#### Planned Task 1: [TASK-DEV-010] Video Player Polish & Testing
- **Status in TODO:** 🆕 New
- **Priority:** Medium
- **Estimated:** 2h
- **Actual Status:** ✅ Completed
- **Actual Time:** 2.5h
- **Outcome:** All browsers tested, 3 bugs fixed
- **Variance:** +0.5h

#### Planned Task 2: [TASK-DEV-011] Additional Features
- **Status in TODO:** 🆕 New (Optional)
- **Priority:** Low
- **Estimated:** 3h
- **Actual Status:** ⏸️ Not Started
- **Reason:** Prioritized bug fixes instead

#### Unplanned Work
- **Emergency Fix:** Production bug in video player
- **Time:** 2h
- **Priority:** Critical
- **Outcome:** Hotfix deployed

### Summary
- ✅ **Completed:** 1/2 planned tasks (50%)
- 🔄 **In Progress:** 0
- ❌ **Not Started:** 1
- 🆕 **Unplanned:** 1 item
- ⏱️ **Time:** 6.5h estimated → 4.5h actual (1 task + unplanned)
- **Notes:** Unplanned critical work took priority
```

### Aggregate Summary

```markdown
# Day 28 TODO vs Actual - Aggregate Report

## Overall Statistics
- **Employees Analyzed:** 16
- **Total Planned Tasks:** 64
- **Tasks Completed:** 42 (65.6%)
- **Tasks In Progress:** 12 (18.8%)
- **Tasks Not Started:** 10 (15.6%)
- **Unplanned Work Items:** 18

## Time Analysis
- **Total Estimated Hours:** 140h
- **Total Actual Hours:** 152h
- **Variance:** +12h (+8.6%)
- **Hours on Unplanned:** 22h (14.5% of total)

## By Department

| Dept | Tasks | Completed | % | Time Var |
|------|-------|-----------|---|----------|
| DEV | 6 | 4 | 66% | +2h |
| LGN | 16 | 12 | 75% | +3h |
| FIN | 8 | 8 | 100% | -1h |
| DGN | 4 | 3 | 75% | +1h |
| ... | ... | ... | ... | ... |

## Common Patterns
1. **Underestimated Tasks:** Video editing (avg +1.5h)
2. **Overestimated Tasks:** Email responses (avg -0.5h)
3. **Frequent Blockers:** API access delays (3 employees)
4. **Unplanned Categories:** Bug fixes (40%), urgent requests (35%), meetings (25%)

## Recommendations
1. Add 20% buffer to video editing estimates
2. Track unplanned work for better future planning
3. Address API access process (blocking 3 employees)
```

---

## Success Criteria

- [ ] All 16 employee comparisons completed
- [ ] Each comparison shows: planned vs actual, time variance, unplanned work
- [ ] Aggregate statistics calculated
- [ ] Patterns and insights documented
- [ ] Recommendations provided for future planning

---

## Timeline

- **Preparation:** 15 minutes
- **Per Employee Comparison:** 10-15 minutes × 16 = 2.5-4 hours
- **Aggregate Analysis:** 30 minutes
- **Total:** 3-4.5 hours

---

## Notes

- Some employees may not have Day 28 daily.md files (day off, no work logged)
- TODO files are structured predictions, daily files are freeform reality
- Focus on identifying what actually happened vs what was planned
- Document gaps in logging/tracking for process improvement
