# COMPREHENSIVE ANALYSIS: 241125.md
**Date:** 2025-11-24 (November 24)
**Analysis Framework:** MAIN_PROMPT_v6
**Document Type:** Mixed format - Task list + Conversation transcript (Whisper Flow)
**Languages:** Mixed Russian/Ukrainian/English
**Total Length:** 95 lines
**Participants:** CEO (Kolya), Developer (likely Stas or Olya)

---

## EXECUTIVE SUMMARY

This document captures a **critical system architecture discussion** and **weekly task planning session** on November 24, 2025. The conversation reveals the **breaking point** of the current workflow - CEO working nights/weekends to process data manually because token limits prevent automation at scale.

**Central Crisis:**
> "I've exhausted 8 AI accounts working around the clock. I can only work when others sleep. I need a local model that can process 50MB of text documents overnight."

**Key Themes:**
1. **Token Economics at Breaking Point** - All 8 accounts exhausted, blocking all work
2. **Data Processing Overhead** - 3 full cycles to process just Week 3 reports
3. **Video Research System** - Working example of phased automation (contrast to reports)
4. **Talent Profiles Creation** - Finally creating employee profiles with IDs
5. **Jobs/Vacancies Update** - Outdated content blocking sales
6. **Strategic Planning Methodology** - 2-3 day project cycles needed

---

## SECTION 1: IMMEDIATE TASK LIST (TOP OF FILE)

### 1.1 URGENT TASKS IDENTIFIED

**Employee Data Management:**
```markdown
## Task Template: Collect all employees profiles
Take employees folders inside Nov25 folder and Finance
→ Copy them to: ENTITIES/Talents/Employees
```

**Data Structure Fixes:**
```markdown
- Tools Master File CSV [create/update]
- Fix ID inside JSON [format violations]
```

**Access & Infrastructure:**
```markdown
- GitHub Access to Entities [set up]
- Prompts Folder Ecosystem [organize]
```

**Weekly Planning Process:**
```markdown
Last Week Master list of Tasks
→ Combine with listed Plans
→ Split them into Workflows
→ Split Into Departments
→ Assign to Employees in Departments
```

**Folder Organization:**
```markdown
Create Week_4 Folder
* Clean Up PROMPTS folder

<Process Historical notes>
- Use Prompt MAIN_PROMPT_v6.md
```

**Dashboard Requirements:**
```markdown
Dashboards:
    - Tasks By Departments
    - Tasks by Employees

Need: Weekly master list of tasks (maybe with attached steps, workflows
      split by tasks, projects and milestones if exist).
      In listing format without too much metadata for next week's distribution.
```

**Task Tracking System:**
```markdown
Build Tasks Tracking System:
- Split into Phases
- Include Approval receiving

All Tasks Manual Distribution System:
[to be implemented]
```

---

## SECTION 2: THE TOKEN CRISIS

### 2.1 SCALE OF THE PROBLEM

**Current Situation:**
```
CEO's Work Pattern:
  - 8 AI accounts total
  - 3-4 accounts exhausted per day
  - Accounts refresh after 3 hours
  - Works nights/weekends only (when employees aren't using accounts)
  - Circular workflow: Use Account 1-2 hours → wait 3 hours cooldown →
    switch to Account 2 → repeat
```

**Quote:**
> "Циклnly processing data - not practical from token standpoint. Yes, he can
   easily process 1 file, tells you nicely, stuffs in extra info. But for
   regular processes, I never managed to make it work.

   If I take Week 3 reports, I maybe brought only part of Nov 19 to good
   condition, and that's because prompts are too bulky."

**Time Investment:**
> "This task alone - I spent the entire weekend parsing these reports.
   This is not a realistic amount of time and iterations."

---

### 2.2 CONTRAST: VIDEO RESEARCH SYSTEM (WORKING)

**Why Video Research Works:**

CEO describes a **phased, scripted system** that actually functions:

```
ENTITIES/TASK_MANAGERS/researches/
├── Phase 1: Search for videos (compile list of videos to transcribe)
│   ↓ [Script converts to queue]
├── Phase 2: Transcription queue (process videos)
│   ↓ [Script processes transcriptions]
├── Phase 3: Entity extraction
│   ↓ [Google AI Studio exports separately]
└── Phase 4: Import to libraries
    ├── Tools (TOL-###)
    ├── Actions (ACT-###)
    ├── Task Templates (TSK-###)
    ├── Milestones (MLT-###)
    └── Workflows (sequential task chains)
```

**Key Success Factors:**
1. **Phase-based:** Each phase has clear input/output
2. **Scripts between phases:** Data transformation automated
3. **Separate exports:** Tools vs Actions vs Tasks extracted independently
4. **Clear sequencing:** "What? Where? Do what? How? In what order?"

**CEO Quote:**
> "So we made scripts. Google AI Studio already outputs tools for import
   separately: tasks, templates, actions, everything for populating.
   Milestones and chains. Workflows with task sequences."

**Application Created:**
> "Olya will make a dashboard for it. It's inside task manager where there
   are several phases, between these phases are scripts that process and
   transfer data."

---

### 2.3 WHY REPORTS DON'T WORK (YET)

**Problems Identified:**

**1. No Employee Profiles:**
```
Example: Yulia Kucherenko in Lead Generation
Problem: Department not recognized correctly
Reason: No employee/talent profiles exist
Result: Can't assign tasks automatically
```

**CEO Quote:**
> "We need talents urgently. Because of this 'public finance' thing - me and
   Dasha talked this morning - public finance is great where profiles are just
   'available' or 'not available', but we need to develop it further."

**Missing Data:**
- Interview transcriptions
- Video recordings
- Any direction for delegation

**2. Prompts Don't Navigate Properly:**
```
Problem: Prompts in separate /prompts folder
Reality: AI working in /reports or /research folders won't jump up a level
         to find prompts folder
Workaround: Must explicitly point AI to prompts every time
```

**CEO Quote:**
> "Unfortunately, the theory that prompts will be in prompts folder - it didn't
   work. It won't jump from reports folder or research work and jump up a level
   to find prompts folder. Unless you directly point it there! You constantly
   have to point and remind."

**3. Tasks Not Standardized:**
```
Result from Week 3 processing:
  - 53 tasks from all departments (surprisingly low)
  - 450 tasks from CEO's notes (mix of themes, need grouping)
  - CEO asked AI to classify by department and find assignees
  - AI copied entire task manager but couldn't match properly
```

**Why Matching Failed:**
> "Because it's not populated, because it's empty. Even transcribed videos
   aren't all shoved into library. System isn't working yet. Otherwise it could
   find common points, connecting points, extract entire action chains."

---

## SECTION 3: WEEK 3 REPORTS PROCESSING

### 3.1 MANUAL PROCESSING RESULTS

**Files Generated:**

**1. Master Consolidated File:**
```
Location: /reports/Week_3/all_tasks_consolidated.csv
Contents: All tasks from all departments
Example departments:
  - Lead Generation
  - Prompt Engineering
  - Training
  - Google Script Expansion
  - World Connection
```

**2. Department-Specific Files:**
```
Example: Lead Generation tasks
Issues found:
  - Yulia Kucherenko (wrong department assignment)
  - Google Map Scraping (assigned to wrong person - was Vlada's)
```

**3. Delegation Map:**
```
Created: Task-to-department-to-employee assignments
Status: Incomplete due to missing employee profiles
Next step: Import responsibilities, match by responsibilities
```

**CEO Observation:**
> "He assigned departments to these tasks: Design, Marketing, Old Workflow
   System... We got a duplicate - Workflow and Milestone duplicate. Well,
   this is task 427 - not enough to just delete workflow, need to tell AI
   'I want to cut workflow from system and migrate data to this.' It goes
   and updates links everywhere - in documentation, in main entity folder,
   in prompt files..."

---

### 3.2 TASK CLASSIFICATION ATTEMPT

**Process:**
```
1. Collected 450 CEO tasks (from notes)
2. Collected 53 departmental tasks (from Week 3)
3. Asked AI: Match to task templates in TASK_MANAGERS
4. Asked AI: Classify by department
5. Asked AI: Suggest assignees

Result: Couldn't match properly because:
  - Task templates incomplete
  - Video transcriptions not fully imported to libraries
  - No employee skill/tool mappings
```

**Quote:**
> "He copied the entire task template [from] task manager, but because it's
   not populated, because it's empty... Even videos that were transcribed
   aren't all shoved into library yet. So system isn't working yet."

---

## SECTION 4: TALENT PROFILES - FINALLY CREATED

### 4.1 PROFILE STRUCTURE

**What's Needed:**
```
Employee Profile Structure:
  - Employee ID (EMP-###)
  - Name
  - Department
  - Skills (SKL-### references)
  - Tools (TOL-### references)
  - Completed tasks (log)
  - Availability status
  - VS Code installed? (yes/no)
  - Dropbox synced? (yes/no)
  - Claude Code setup? (yes/no)
```

**Why It Matters:**
> "ID assignment - like here [example shown] - then writing taxonomy, writing
   README with these IDs, it allows finding similar data at least somehow."

**Example:**
```
Designer: User Interface
Likely objects:
  - Design Layout (OBJ-###)
  - Design [something]

In talents there are skills. I haven't brought them to IDs yet. There's SKL-020
for clothing, for example. Need to re-authenticate, re-write everything.
What tools does a person work with?
```

---

### 4.2 INTEGRATION WITH LIBRARIES

**Connection Points:**
```
Talent Profile → Skills (SKL-###) → Tools (TOL-###)
                                  ↓
                            Task Templates (TSK-###)
                            (can this person do this task?)
```

**Current State:**
> "Unfortunately, integration of IDs and structuring written in all files -
   it only goes through AI and it eats a lot of time and iterations. It goes
   through all files. That's why I'm desperately trying to reduce number of
   files - extract something, archive, reduce quantity so it can move faster
   through this."

**Example Bug Found:**
```
Location: libraries/tools/
Problem: Split into categories
Issue: Categories not documented anywhere
Bug: Should be "tool_id" but shows "date" instead
      (category shoved in here, wrong field)

Action: Need to build Tools Master File CSV
        Then fix IDs inside JSON
```

**Taxonomy Folder Created:**
```
Location: /taxonomy/
Contains: Taxonomy of libraries
Purpose: Lists all IDs for reference
Problem: AI still doesn't have enough tokens to process all tools
         even with taxonomy guide
```

---

### 4.3 VERIFICATION TABLE CONCEPT

**CEO's Vision:**
```
Like Video Verification Table:
  - Video 023 extracted:
    - Tools: 4
    - Workflows: [extracted]
    - Actions: [extracted]

Replace "Video" with "Employee":
  - Employee 042:
    - Dropbox installed: ✓
    - VS Code: ✓
    - Claude Code confirmed: ✓
    - Can assign tasks using: Claude Code, Midjourney, [others]
```

**Enables Smart Assignment:**
> "Then you already know I can give him a task on Claude Code, or Midjourney,
   or whatever else."

---

## SECTION 5: JOBS/VACANCIES CRISIS

### 5.1 OUTDATED CONTENT PROBLEM

**Context:**
```
Old System: Remote Employees website + old CRM
Content: Jobs (vacancy postings)
Composed from: Responsibilities
Status: SEVERELY OUTDATED
```

**CEO Quote:**
> "Jobs - develop and connect to RE [Remote Employees]

   Remember we had 'jobs' concept in old CRM, on the new [system], job
   postings that were assembled from responsibilities and all that?

   So by downloading content from Remote Employees or downloading content
   from new CRM about jobs, you could put the ancestor on Dropbox, develop
   this jobs [system], set up system for populating it from general records,
   filling with new types of responsibilities, etc."

**What Was Scraped from Videos:**
> "What we scraped from videos - fill it back to Remote Employees. Fill
   it in living mode if not each [manual update], but through simple automation
   8n [n8n] or Make, employee profiles will be populated."

---

### 5.2 CURRENT SALES IMPACT

**Problem Chain:**
```
Old Responsibilities → Old Skills → Old Tools
         ↓
  Outdated Job Postings
         ↓
   Candidates Don't Apply
         ↓
    No Talent Pool
         ↓
   Can't Fulfill Client Orders
         ↓
     Lost Sales
```

**CEO Quote:**
> "You're trading goods that are expired... Yes, these expired responsibilities
   that existed then - they're not relevant today. Skills that existed then
   like HTML - they're not relevant. Yes, you can cook from spoiled expired
   food, like fast food, sell one-day stuff... But all this, all this is
   crutches. Goods are outdated. Let's be real."

**Old CRM Data Quality:**
```
Export: 3000 clients from old CRM
Created: 3000 separate files (one per client)
Result: Removed from Dropbox sync immediately (too many files for AI)
Problem: 90% of fields completely empty, don't exist
Legacy: Remnants from very first CRM installation
```

**CEO:**
> "Jaw drops at how bad everything is there. Remnants of the very first CRM
   we installed. 90% of fields - they're about nothing. Not even filled.
   They don't exist. But each lead, each million leads drags with it 90%
   of pure garbage."

---

### 5.3 PROPOSED SOLUTION

**2-3 Day Project:**
```
Day 1: Export jobs content from old CRM + Remote Employees
       Structure the data

Day 2: System should populate these jobs automatically from:
       - New transcribed videos
       - Synchronized with our library of tags
       - Updated responsibilities

Day 3: Test automation, launch

Maintenance: Auto-updates from ongoing video processing
```

**Why It Must Be Fast:**
> "2-3 day projects are normal. Let you keep focus and have time frames.
   Not abandon like 'I'll go do this now.' No, for this task the deadline
   is burning. But that other thing can wait."

**Why It's Urgent:**
> "This whole branch doesn't exist right now - vacancies outdated, people
   outdated, etc. You're selling expired product."

---

## SECTION 6: SYSTEM ARCHITECTURE INSIGHTS

### 6.1 WORKING VS. BROKEN PATTERNS

**Pattern 1: Video Research (WORKING)**
```
✓ Clear phases
✓ Scripts between phases
✓ Separate exports per entity type
✓ Sequential processing
✓ Dashboard created
✓ Integrated into task manager

Result: Can process 50+ videos per cycle
```

**Pattern 2: Report Processing (BROKEN)**
```
✗ No clear phases
✗ Manual iteration required
✗ Prompts not co-located
✗ Mixed entity extraction
✗ No employee profiles to assign to
✗ 3 cycles to process Week 3

Result: CEO working nights/weekends, exhausting all accounts
```

**Pattern 3: Task Manager (INCOMPLETE)**
```
⚠ Structure exists
⚠ Some templates filled
⚠ Missing video imports
⚠ No cross-references complete
⚠ Can't auto-match tasks yet

Result: Useful for manual lookup, not ready for automation
```

---

### 6.2 ID SYSTEM CRITICAL PATH

**The ID Assignment Workflow:**
```
1. Create entity (e.g., Tool, Employee, Skill)
2. Assign ID (TOL-039, EMP-042, SKL-020)
3. Update taxonomy file (master list)
4. Write cross-references in related entities
5. Run validation script
6. Update documentation/README with IDs

Enables: Finding connections, automated matching
```

**Token Cost of Re-ID'ing:**
```
One folder (e.g., /tools/) to add IDs:
  - 3-4 complete cycles
  - 1 full AI account exhausted

But manual is impossible:
  - Hundreds of files
  - Dozens of cross-references per file
  - Would take weeks manually vs. hours with AI
```

**CEO Quote:**
> "Just to change one folder's IDs... it eats at least one completely blown
   AI account... But by hand it would take longer. By hand it's impossible
   to do. I'm at a loss, to put it mildly, with the volume of work that
   can't be delegated to anyone."

---

### 6.3 WORKFLOW/MILESTONE DUPLICATE ISSUE

**Problem Discovered:**
```
System has:
  - Workflow (WFL-###) for sequential tasks
  - Milestone (MLT-###) for project phases

Issue: They overlap/duplicate functionality
Decision: Need to remove one, migrate data
```

**CEO Quote:**
> "Old workflow system - we got a duplicate of workflow and milestone.

   Task 427: Not enough to just delete workflow. Need to tell AI 'I want to
   cut workflow from system and migrate data to THIS.' And it goes updating
   links everywhere - in all documentation, in main entity folder, in prompt
   files, etc. It's not that simple."

**Why It Matters:**
- Can't just delete files (breaks all references)
- Must migrate data systematically
- Must update all prompts that reference deleted entity type
- Requires AI to track down all mentions across entire ecosystem

---

## SECTION 7: AI TOOL STRATEGY

### 7.1 ACCOUNTS INVENTORY

**Currently Owned:**
```
1. Cursor (admin account) - paid
2. Cursor (design account - DGN) - recent purchase
3. Cursor (sales account?) - mentioned
4. Claude direct accounts - multiple
5. GPT accounts - "lying around unused"
6. Windurf - tried, limited (mentioned: 11:00 session limit)
7. Whispr Flow - not AI, transcription tool
```

**Recent Purchases:**
```
- DGN (design) account
- Niko account (mentioned buying "on Niko")
- Specific Claude account
```

**Budget Request:**
> "TSK-154: Purchase additional AI tool accounts
   We bought on DGN just now, on Niko we bought, we bought specific Claude.
   We still need more. More instruments are needed."

---

### 7.2 ALTERNATIVE TOOLS RESEARCH

**CEO Quote:**
> "We urgently need alternatives. I already started searching - Copilot,
   something else. Researches on what else exists. Not bad alternative -
   working through GitHub, through G5 and GitHub, through Gimini-GitHub.

   Well, they all have GitHub connection. At least entities - maybe not
   full profiles maybe not, but now..."

**GitHub Integration:**
- All these tools can connect to GitHub
- Can work with Entities repository
- May not have full profiles but enough

**Desired: Local Model**
> "If local models installed, like Llama type or some of latest that came
   out - Gemma, etc. - local Mixtral models, someone else who can think,
   who could read just 50 megabytes of text documents...

   Very simplified, but they should be thinking about this every day. It
   would save them so much energy. But we didn't launch local models, we
   abandoned local computers that could help us."

---

### 7.3 TOKEN ECONOMICS MATH

**Current Bottleneck:**
```
Task: Process Week 3 employee reports
Data size: ~50MB text
Token cost: 8 accounts × 3 cycles = 24 account-exhaustions
Time cost: Entire weekend
Result: Only brought Nov 19 data to "good condition"
```

**If Local Model Existed:**
```
Task: Same processing
Data size: 50MB text (well within local model capacity)
Token cost: $0 (local inference)
Time cost: Run overnight while CEO sleeps
Result: Wake up to processed data + suggestions
```

**CEO Quote:**
> "It's not burning urgently, but... imagine instead of CRM, these 50 megabytes
   are your whole CRM. It shrank because old CRM had 1 gigabyte, markup another
   gigabyte. But the squeeze, the main thing, is 50 megabytes. You want AI
   to help you manage this, right?

   It's about a fundamentally global big decision, not a minute decision like
   'need to connect now.' About the direction where we're moving."

---

## SECTION 8: STRATEGIC PHILOSOPHY

### 8.1 SYSTEM UPGRADE METAPHOR

**Growing Out of Clothes:**
> "The kid walked in sandals and shorts, but he grew up and sandals and
   shorts don't fit him anymore. He looks ridiculous. That's our management
   system, our management model that exists now - it's old small shorts
   with sandals even though he's already 17 years old."

**Old CRM Analogy:**
> "I want to close old CRM. It's useless. Impossible to work with. But now
   with AI, Olya can extract from CRM whatever you want, add, write some
   script for extracting data, clean it, paste back.

   Then you extract it and your jaw drops at how bad everything is there."

---

### 8.2 THE FOCUS PROBLEM

**CEO's Struggle:**
> "One thing at a time. Until you finish polishing it, not abandoning, not
   switching, not running around, not solving closing all holes in the world
   all at once on one knee. But what matters - however long it takes, 1 week,
   2 days, 3 [days]...

   Plan it, create yourself a plan. 'I want to do THIS.' Create multi-level,
   multi-file plan. How will you implement it? Use our task manager structure
   - where's the milestone, where's the steps, where's the tasks?"

**To Developer:**
> "Look at task manager taxonomy and AI will build you files for how you'll
   implement - whether it's video training-interview, video interview, or
   local model processing, or content on RE site that will auto-form from
   Dropbox, from our professions, from libraries, from library populate
   automatically, responsibilities, vacancy descriptions through simple
   automation n8n or Make will populate employee profiles."

---

### 8.3 PROJECT TIME-BOXING

**2-3 Day Cycles:**
```
Day 1: Develop (10% of work)
Day 2 (middle): Check progress (10% verification)
Day 3: Receive work (80% done by others)

Total: 2-3 days maximum per project
```

**Why This Works:**
> "2-3 day projects - normal. Let you keep focus and have time frames. Not
   'abandon' like 'I'll go do this now.' No, for this task the deadline burns.
   But that can wait.

   Because this is a whole branch that doesn't exist right now [vacancies],
   which is outdated, people outdated, etc."

**What Happens Without Time-Boxing:**
> "You took on video streaming, you fixed video streaming and finally it
   works on site. But then you didn't take on the next thing...

   Why does Dropbox work? Because of all this system. Because we developed
   for 2 years all these entities, talents, structure, architecture, task
   managers, how they should be named. And we lift these documents now, give
   to AI and say 'implement this Dropbox for us.'"

---

## SECTION 9: DELEGATION & MENTAL MODELS

### 9.1 THE STRATEGIST GAP

**CEO's Observation (to developer):**
> "You have all the skills - physically you're fine, you're skilled guy, you
   know computers, programs, etc. But there's no backup, this entity of yours
   that would see from behind this whole ecosystem.

   Like in war - the one who sees battlefield coordinates: cavalry go, archers
   go, etc. But strategist - this strategy isn't written in your head. And
   every time it's like you don't understand, all the time you don't see or
   don't recognize it."

**Developer's Response:**
> "I lost following in the middle, heard poorly..."

**CEO:**
> "That's why we need to work now not on task output but on new gymnastics.
   But all this - think about it, work on it. Flashlight, notebook, pen,
   drawing, whatever. Again and again and again, crossing out, tearing out
   pages, drawing new until it clicks for you. All the pieces should work.

   This is your creativity. Super creative dude. And you have such resources
   lying unused. Your internal, this knowledge - maybe. It's very interesting,
   very interesting to see what comes out when you try to take your mental
   resources and throw them not limited by token space and possibility space."

---

### 9.2 WRITING AS THINKING

**CEO's Method:**
> "I showed you literally today how I just wrote in notepad. I asked it on
   weekend like 'summarize my notepad for the day' - my notes for the day.
   What was my surprise when it quickly created from this actions, which it
   immediately started executing.

   It broke into 10 points with 5 sub-points. 'Now let's execute this.' But
   because I wrote while I was doing stuff, some were already done. I told
   it 'in this period we checked, this is already done.' But we get to moment
   where your mental projection, your thoughts can be implemented at same time.

   Then you need to level up your thoughts. What AI doesn't have - it only
   knows what happened. It doesn't know what's next, what will be, what
   specifically suits you. It doesn't know."

**Recommendation:**
> "Try this direction. Seems very interesting to me. Coincidence in this
   unique [situation]. But we don't have enough. We haven't had this for
   long time. We need such big meeting where we sit, discuss, systematize,
   taxonomize.

   But alone one person in field not warrior. You need someone to look from
   outside, discuss, talk through."

---

### 9.3 EMPLOYEE SYNCS (SMENA CONCEPT)

**Current Problem:**
```
Meetings: Chaotic, on-demand
Pattern: "I jumped in on your channel, well we talked about everything"
Result: No preparation, no documentation, no logged progression
```

**Proposed: SMENA (Scheduled Shift/Session):**
> "Next on my agenda is 'smena' (shift/session). I tried delegating creation
   of smena to different people but none of them lifted a finger to make smena.

   Smena is when person comes to you - at least an hour, you need at least
   with key employees an hour per week. And you conduct it not chaotically
   like 'I jumped in, we talked about everything,' but purposefully,
   documented, logged on specific date, specific time, which will have
   sequence of development from previous call to next call.

   Not 'jumped in on channels.' When person knows they're coming Wednesday,
   they start preparing for this Wednesday. Unlike moment when you jumped
   in channel - well, let's talk, in middle of task I was doing this and that,
   you such..."

**Structure Needed:**
```
Weekly 1:1 Meetings:
  - Scheduled: Same day/time each week
  - Prepared: Employee knows topic in advance
  - Documented: Logged conversation
  - Sequential: References previous week's discussion
  - Action items: Clear next steps

vs. Current:
  - Random: Whenever someone pops in
  - Unprepared: "What were you working on?"
  - Undocumented: Lost after call ends
  - Disconnected: No reference to previous discussions
```

---

## SECTION 10: DATA CLEANUP PRIORITIES

### 10.1 URGENT CLEANUP TASKS

**1. Tools Master File:**
```
Status: Partially categorized, no master CSV
Issues:
  - Categories not documented
  - IDs wrong format (shows "date" instead of "tool_id")
  - Category field in wrong location

Action: TSK-### Create Tools Master CSV File
        TSK-### Fix IDs inside tools JSON files
```

**2. Taxonomy Integration:**
```
Created: /taxonomy/ folder
Contains: Library taxonomies (all IDs listed)
Problem: Even with taxonomy, AI runs out of tokens processing all tools
Solution: Need scripts + HITL approval, not pure AI processing
```

**3. Workflow vs. Milestone:**
```
Issue: Duplicate functionality
Decision: Remove "workflow" entity type
Process:
  1. Identify all workflow references
  2. Migrate data to milestone structure
  3. Update all prompts mentioning workflow
  4. Update all documentation
  5. Delete workflow files

Note: Can't just delete - must systematically migrate
```

**4. Employee Folders:**
```
Source: Nov25/[EmployeeName]/ and Finance/[EmployeeName]/
Destination: ENTITIES/Talents/Employees/[EmployeeName]/
Content to extract:
  - Interview recordings/transcripts
  - Daily reports
  - Skills used
  - Tools used
  - Completed tasks

Structure needed: Profile with IDs
```

---

### 10.2 PROMPTS FOLDER CLEANUP

**Current Issues:**
```
Problem 1: Prompts scattered
  - Some in /prompts/
  - Some in /entities/*/prompts/
  - Some in department folders (buried deep)

Problem 2: AI can't navigate upward
  - Working in /reports/ won't jump to /prompts/
  - Must explicitly point every time

Problem 3: No co-location
  - Prompts separate from data they process
  - Context lost
```

**Proposed Structure:**
```
Option A: Prompts in each entity folder
  ENTITIES/TASK_MANAGERS/prompts/
  ENTITIES/LIBRARIES/prompts/
  ENTITIES/REPORTS/prompts/

Option B: Central prompts with explicit references
  PROMPTS/
  ├── task-manager-processing.md (references: /entities/task_managers/)
  ├── reports-processing.md (references: /entities/reports/)
  └── libraries-processing.md (references: /entities/libraries/)

CEO Note: Option A preferred - AI stays in working directory
```

---

### 10.3 MASTER FILES STATUS

**Completed:**
- ✓ Tasks Master (TASK_MANAGERS/DATA/tasks_master.csv)
- ✓ Milestones Master (TASK_MANAGERS/DATA/milestones_master.csv)
- ✓ Projects Master (TASK_MANAGERS/DATA/projects_master.csv)
- ✓ Prompts Master (PROMPTS/DATA_FIELDS/PMT_Master_List.csv)

**In Progress:**
- ⚠ Tools Master (categories exist, needs CSV compilation)
- ⚠ Employee/Talent Profiles (just started creating today)
- ⚠ Actions Master (exists but not all videos imported)
- ⚠ Objects Master (exists but not all videos imported)

**Missing:**
- ✗ Steps Master (STP-###) - no master file created yet
- ✗ Workflows Master (WFL-###) - may be eliminated (duplicate of milestones)
- ✗ Skills Master (SKL-###) - mentioned but not systematized
- ✗ Responsibilities Master (RSP-###) - critical for jobs system

---

## SECTION 11: DASHBOARD DEVELOPMENT

### 11.1 ATTEMPTED DASHBOARD (BY OLYA)

**Olya's Experience:**
> "She ran into a problem. I didn't even try. She tried to make dashboard
   with tasks. See? But she said because system is very chaotic, there's
   no chance at all yet for proper data against this ecosystem."

**Why It Failed:**
- Data not standardized
- No master files complete
- No employee profiles to query
- Tasks not properly ID'd and cross-referenced
- Department assignments inconsistent

**What She Built Anyway:**
> "She can make a dashboard for it [video research]. She just pointed it at
   folder and said 'build this.' It built for me. Looks good, these with
   scope counts, but data is chaotic, unordered, so it can't display data
   you want."

---

### 11.2 REQUIRED DASHBOARDS

**From Task List (Top of File):**
```
Dashboards Needed:
  1. Tasks By Departments
     - Show all tasks assigned to each department
     - Filter by status (pending/in-progress/completed)
     - Show assignees

  2. Tasks by Employees
     - Show all tasks per employee
     - Show employee capabilities (tools, skills)
     - Show workload/availability
```

**Data Requirements:**
```
For Department Dashboard:
  - Tasks with department field populated
  - Employees with department field populated
  - Task status tracking

For Employee Dashboard:
  - Employee profiles (with IDs)
  - Skills mapping (EMP → SKL)
  - Tools mapping (EMP → TOL)
  - Task completion history
  - Current assignments
```

**Blocking Issues:**
1. Employee profiles incomplete (just started today)
2. Task assignments not systematized
3. Skills/tools not mapped to employees
4. Historical data not structured

---

## SECTION 12: WEEKLY PLANNING PROCESS

### 12.1 DESIRED WORKFLOW

**From Task List:**
```
Process:
  1. Take "Last Week Master list of Tasks"
  2. Combine with "listed Plans"
  3. Split them into Workflows
  4. Split Into Departments
  5. Assign to Employees in Departments
```

**Output Format:**
> "I need weekly master list of tasks, maybe with attached steps, workflows
   split by tasks, projects and milestones if exist. I need to collect them
   in listing format without too much metadata for next week's task distribution."

**Key Requirement:** Lightweight format, not heavy metadata

---

### 12.2 CURRENT PROBLEMS

**Week 3 Example:**
```
Input:
  - 450 CEO tasks (from various notes)
  - 53 departmental tasks (from employee reports)

Process: Manual classification using AI
  - Match to task templates (failed - templates incomplete)
  - Assign to departments (partially successful)
  - Assign to employees (failed - no profiles)

Output:
  - Delegation map (incomplete)
  - Consolidated CSV (created but unassignable)
```

**Quote:**
> "It made me a map for delegation. Assigned departments: Design, Marketing,
   Old Workflow System... I tell it 'you're talking nonsense, let's start
   over. Maybe import to responsibilities and determine by responsibilities
   at least.' See, it stuck 'Design' department everywhere."

---

### 12.3 MISSING COMPONENTS

**To Make Weekly Planning Work:**

**1. Employee Profiles (just started):**
- Who works in which department?
- What tools do they know?
- What skills do they have?
- Are they available?

**2. Task Templates (incomplete):**
- What are standard tasks?
- What tools/skills required per task?
- How long does each take?
- What's the process?

**3. Historical Data (not structured):**
- What tasks were completed last week?
- Who did them?
- How long did they take?
- Any blockers?

**4. Capacity Planning (doesn't exist):**
- How many hours per employee per week?
- Current workload?
- Can they take more tasks?

---

## SECTION 13: TECHNOLOGY STACK OBSERVATIONS

### 13.1 TOOLS MENTIONED

**AI Tools:**
- Cursor (primary, multiple accounts)
- Claude (direct API, multiple accounts)
- GPT (accounts "lying around" unused)
- Windsurf (tested, limited)
- Copilot (researching)
- G5 (extension for token economy)
- Google AI Studio (for video transcription exports)

**Development Tools:**
- VS Code (with extensions)
- GitHub (repositories for Entities)
- Dropbox (current file storage/sync)
- Local Docker (mentioned for PostgreSQL testing)

**Automation:**
- n8n (mentioned for automation)
- Make (mentioned for automation)
- Scripts (Python, mentioned between phases)

**Transcription:**
- Whispr Flow (not AI, just transcription)

---

### 13.2 INFRASTRUCTURE GAPS

**Missing:**
```
1. Local AI Model
   - Would process 50MB text overnight
   - No token limits
   - Can "think" longer without asking "what's next?"

2. Database
   - Currently: CSV/JSON files in Dropbox
   - Planned: PostgreSQL or vector DB
   - Blocking: Dashboard development

3. Unified Dev Environment
   - Developers don't have standardized setups
   - Each using different tools/accounts
   - No shared workflow
```

---

## SECTION 14: FINANCIAL CONTEXT

### 14.1 BUSINESS MODEL CHALLENGES

**Revenue Pattern:**
> "Positive balance is so small it's not even felt. If it refills, it refills
   a month or two later, understand? Until you earn those specific $5000,
   when will they pay? 97% of payments arrive month or... No, month...
   90% arrives month later, right? While who when will pay, but still..."

**Canadian Business Model Comparison:**
> "I looked at Canada. In Canada with same massage therapists, they can cover
   couple thousand bucks. But for that I need premises to be good. When I
   worked in basement, people came once but maximum twice. Doesn't look nice,
   tasty, somewhere there in basement on fifth turn left. Don't want to go,
   no desire.

   Good premises - that's $3000. Out of this $3000... Well, if so good
   premises, if squeeze a bit, $2000. At least in terms of 3 months I'd take
   maximum 3... 3 for 3 months is $9-10k. Plus need to live somehow, need
   advertising, total $11-12k startup capital right away.

   What kind of iPhone am I buying for $2000 when I have rent and startup?
   In short, don't feel like financially recuperating spirit a bit."

**Remote Work Value Prop:**
> "Parents have separate office, separate warehouse currently. But they have
   opportunity appearing - supermarket type where warehouse and shop are same
   face. You walk into expo center... There's for comparison our Nova Poshta
   or some electronic chain where small shop and corner, then you must go to
   warehouse and wait in queue to receive your goods. Some shop, some store,
   even cable you buy, you must go with slip to warehouse and they issue this
   cable, understand?

   But shop where they give you right away - less logistics, less expenses,
   more free clients, more sales, less queues.

   Same thing with us. World is hinting to us by all hints: enough of this
   with department-type handoff - this person assigned, then passed to another,
   another interviews them, then interview, then... This very complex process.
   If simplified, it just like in stores helped us cut logistics costs and
   seriously increase sales."

---

### 14.2 PROPOSED SOLUTION: LIVE VIDEO CHAT

**Concept:**
> "For this, video chat, live employees. Hire employees like Bookernike -
   you sit times a day, stream on site or 2 hours a day. And on each employee
   time when you can catch them online, you can immediately interview them
   using AI, controlling what words exchanges there, whatever it may be.

   Plus task system where right away you can buy specific task and your tasks
   drip drip drip per day and distribute to employees. Well, can play around
   with a lot."

**Why It Works:**
- No handoffs (candidate → employee → interview → decision = too slow)
- Instant interaction (see employee online → talk immediately)
- AI-assisted (control quality, suggest responses)
- Task-based purchasing (buy specific deliverable)

---

## SECTION 15: KEY QUOTES & PHILOSOPHY

### 15.1 ON SYSTEM BUILDING

**The Renovation Metaphor:**
> "This step [Dropbox] is huge, that's for sure. But it's still renovation.
   It looks like renovation. Look at building - it's under renovation. When
   it's under renovation, it doesn't bring money. But renovation should happen
   on multiple fronts.

   You took on video streaming, you fixed video streaming, finally it works
   on site. But you didn't take on the next thing...

   Why does Dropbox work? Because all this system... Because we developed for
   2 years all these entities, talents, structure, architecture, task managers
   how they should be named. And we lift these documents now, give to AI and
   say 'implement this Dropbox for us.'

   You don't need developers anymore, no web interface, no back, no front.
   You don't need to climb on server and enter fields by hand like it always
   was. Lead gens in old CRM currently - they write to AI 'fill me client
   card.' No, they go click on field, think through 15 fields they fill by
   hand."

---

### 15.2 ON FOCUS & COMPLETION

**One Thing at a Time:**
> "One thing. Until you finish polishing it, not abandoning, not switching,
   not running around, not solving closing all holes in world all at once
   on one knee. But what matters - however long it takes, 1 week, 2 days,
   3 [days].

   Plan it. Create yourself plan. 'I want to do THIS.' Create multi-level
   multi-file plan. How will you implement it?"

**Why Short Cycles Matter:**
> "2-3 day projects are normal. Let you keep focus and have time frames.
   Not 'I'll abandon' like 'I'll go do this now.' No, for this task deadline
   burns. But that can wait.

   Because this is whole branch that doesn't exist right now [jobs/vacancies]
   - which is outdated, people outdated, etc. You need branch working. Right?
   This whole branch doesn't exist currently about vacancy updated, people
   updated. Well, so, trading expired goods."

---

### 15.3 ON AI LIMITATIONS

**What AI Doesn't Know:**
> "Now we're getting to moment where your mental projection, your thoughts
   can be implemented same time. Then you need to level up your thoughts.

   What AI doesn't have - it only knows what happened. It doesn't know what's
   next, what will be, what specifically suits you. It doesn't know.

   ...but implementation became much faster. So I'm asking you, try this
   direction. Seems very interesting to me."

---

### 15.4 ON DELEGATION & TEAM

**The Strategist Role:**
> "You have all skills - physically fine, skilled guy, know computers, programs,
   etc. But there's no backup, this entity of yours that would see from behind
   this whole ecosystem.

   Like in war - one who sees battlefield coordinates: cavalry go, archers go,
   etc. But strategist - this strategy isn't written in your head. And every
   time it's like you don't understand, all time you don't see or don't
   recognize it."

**Need for Collaboration:**
> "Alone, one person in field not warrior. You need someone to look from
   outside, discuss, talk through.

   But that's not their function. You need to understand your firmware currently
   is old. Expiration date passed on this product. Can't sell it anymore. Need
   to change it and turn on imagination. You have imagination without roads."

**When Teaching Employees:**
> "When I start explaining these plans to employees, they get lost in confusion.
   Not enough additional strategist. You have all chances but... You need to
   understand that..."

---

## SECTION 16: ACTION ITEMS EXTRACTED

### IMMEDIATE (WEEK 4 - Nov 25-29)

**Data Structure:**
- [ ] Create Week_4 folder structure
- [ ] Clean up PROMPTS folder (consolidate locations)
- [ ] Process historical notes using MAIN_PROMPT_v6.md
- [ ] Create Tools Master File CSV
- [ ] Fix IDs inside JSON files (tools)

**Employee Profiles:**
- [ ] Collect employee folders from Nov25/ and Finance/
- [ ] Copy to ENTITIES/Talents/Employees/
- [ ] Extract: interviews, skills, tools, dailies
- [ ] Assign employee IDs (EMP-###)
- [ ] Map skills (EMP → SKL-###)
- [ ] Map tools (EMP → TOL-###)

**GitHub Access:**
- [ ] Set up GitHub access to Entities repository
- [ ] Create prompts folder ecosystem (organize)

**Task Distribution:**
- [ ] Take Week 3 Master List of Tasks
- [ ] Combine with planned tasks
- [ ] Split into workflows
- [ ] Split by departments
- [ ] Assign to employees (once profiles ready)

---

### SHORT-TERM (2-3 DAY PROJECTS)

**Project 1: Jobs/Vacancies Update**
```
Day 1: Export jobs content from old CRM + Remote Employees
       Download, structure data

Day 2: Build auto-population system:
       - Sync with video transcriptions
       - Connect to responsibilities library
       - Set up n8n/Make automation

Day 3: Test, deploy to Remote Employees site
```

**Project 2: Dashboard Development (After Profiles)**
```
Day 1: Design dashboard schema
       - Tasks by Departments view
       - Tasks by Employees view

Day 2: Build dashboard (Olya can do with AI once data clean)
       Point at clean data folders

Day 3: Test, deploy, train users
```

**Project 3: Workflow → Milestone Migration**
```
Day 1: Identify all workflow references
       Map workflow → milestone equivalents

Day 2: Migrate data
       Update prompts
       Update documentation

Day 3: Delete workflow files
       Run validation
```

---

### MEDIUM-TERM (1-2 WEEKS)

**System Improvements:**
- [ ] Research local AI model options (Llama, Gemma, Mixtral)
- [ ] Set up local model on developer computer (overnight processing)
- [ ] Research additional AI tool alternatives (Copilot, GitHub integrations)
- [ ] Purchase additional AI tool accounts (TSK-154)

**Data Consolidation:**
- [ ] Complete all master files (Tools, Skills, Responsibilities, Steps)
- [ ] Add cross-references to all entities (EMP→SKL→TOL→TSK)
- [ ] Run taxonomy validation across all entities
- [ ] Archive old/outdated files from Week 3 and earlier

**Process Automation:**
- [ ] Set up weekly planning automation (based on video research model)
- [ ] Create scripts for phase transitions
- [ ] Implement HITL approval checkpoints
- [ ] Build employee capacity tracking

---

### STRATEGIC (ONGOING)

**Cultural Shifts:**
- [ ] Implement SMENA (scheduled 1:1 meetings) with key employees
  - Weekly, same day/time
  - Prepared agenda
  - Documented outcomes
  - Sequential progression

- [ ] Shift from chaotic to scheduled communication
- [ ] Document all major decisions (not just execute)
- [ ] Build feedback loops (learn from completed projects)

**System Evolution:**
- [ ] Continue 2-3 day project cycles (maintain focus)
- [ ] Build component by component (not all at once)
- [ ] Test each component before integrating
- [ ] Migrate from old systems progressively (not big bang)

---

## SECTION 17: RISKS & CHALLENGES

### 17.1 TECHNICAL RISKS

**Token Exhaustion:**
- **Risk:** CEO exhausting all 8 accounts doing data cleanup alone
- **Impact:** No accounts available for anyone else, work stops
- **Mitigation:** Local model urgently needed OR delegate cleanup with tight supervision

**Data Quality Cascade:**
- **Risk:** Incomplete master files → can't auto-assign tasks → can't delegate → CEO bottleneck
- **Impact:** System can't scale, remains manual
- **Mitigation:** Prioritize master files completion before building on top

**Prompt Navigation:**
- **Risk:** AI can't find prompts when working in subdirectories
- **Impact:** Must manually point to prompts every time, slows work
- **Mitigation:** Co-locate prompts with data OR use explicit paths in all prompts

---

### 17.2 ORGANIZATIONAL RISKS

**Strategist Gap:**
- **Risk:** Developer lacks system-level vision, works tactically only
- **Impact:** Builds wrong things, abandons projects mid-stream
- **Mitigation:** SMENA meetings, written strategy documents, CEO collaboration

**Focus Fragmentation:**
- **Risk:** Jumping between projects without finishing
- **Impact:** Nothing reaches production, always "in renovation"
- **Mitigation:** 2-3 day project cycles, strict time-boxing

**Communication Chaos:**
- **Risk:** Random pop-in meetings, no preparation, no documentation
- **Impact:** Decisions forgotten, context lost, repeat discussions
- **Mitigation:** SMENA system, documented meetings, logged decisions

---

### 17.3 BUSINESS RISKS

**Outdated Content:**
- **Risk:** Job postings and employee profiles reflect 2+ years old skills/tools
- **Impact:** Can't attract clients or candidates, lost sales
- **Urgency:** HIGH - actively losing business now
- **Mitigation:** Jobs/vacancies 2-3 day project (immediate)

**Scalability Ceiling:**
- **Risk:** Current manual process can't scale past 20-25 employees
- **Impact:** Can't grow without exponentially more management overhead
- **Timeline:** Will hit ceiling within 3-6 months at current growth
- **Mitigation:** Automation infrastructure must be ready before hitting ceiling

---

## SECTION 18: SUCCESS METRICS

### 18.1 WEEK 4 GOALS

**By End of Week:**
- ✓ Week 4 folder structure created
- ✓ Employee profiles: 10+ employees with IDs and skills mapped
- ✓ Tools Master CSV completed
- ✓ Week 3 consolidated tasks assigned to departments (even if not to individuals yet)
- ✓ Prompts folder cleaned up and organized

---

### 18.2 MONTH-END GOALS (Nov 30)

**Data Quality:**
- All master files exist and validated
- 80%+ of entities have proper IDs
- Cross-references validated by scripts

**Automation:**
- At least 1 phased workflow automated (following video research model)
- Dashboard operational (even if basic)
- Local model researched with recommendation

**Organizational:**
- SMENA meetings scheduled with 3-5 key employees
- Weekly planning process documented
- 2-3 day project cycles established

---

### 18.3 DECEMBER TARGETS

**System Maturity:**
- CEO not working nights/weekends to process data
- Employees can query dashboards for their tasks
- Weekly planning takes <4 hours (not entire weekend)
- Task assignment 80% automated

**Business Impact:**
- Jobs/vacancies content updated on Remote Employees
- Client can see current employee skills/tools
- Sales cycle shortened (no multi-person handoff delays)
- Employee utilization visible

---

## TERMINOLOGY & ABBREVIATIONS

**Russian/Ukrainian Terms:**
- **Smena (Смена)** = Shift/Session (scheduled 1:1 meeting)
- **Делик (Delik)** = Daily (daily report)
- **Одшник (Odzhnik)** = ID number
- **Таланты (Talanty)** = Talents (employee profiles)
- **Папка (Papka)** = Folder
- **Файл (Fail)** = File

**Entity Abbreviations:**
- **EMP** = Employee (not standard in MAIN_PROMPT_v6, newly proposed)
- **SKL** = Skill
- **TOL** = Tool
- **TSK/TST** = Task template
- **RSP** = Responsibility
- **WFL** = Workflow (may be eliminated)
- **MLT** = Milestone

**Technology:**
- **G5** = VS Code extension for token management
- **n8n** = Automation platform (like Zapier)
- **Make** = Automation platform (formerly Integromat)

---

## FINAL SUMMARY

This document reveals a **critical inflection point**: the CEO has hit the scalability wall. Working nights and weekends, exhausting 8 AI accounts just to process Week 3 employee reports demonstrates the current system cannot scale.

**The Core Problem:** Manual data processing with token-limited AI tools.

**The Vision:** Phased, scripted automation (like video research system) applied to all workflows.

**The Blocker:** Missing foundational data (employee profiles, complete master files, standardized IDs).

**The Path Forward:**
1. **This Week:** Create employee profiles, complete master files
2. **Next Week:** Build dashboards, start phased automation
3. **This Month:** Deploy local model, implement SMENA meetings
4. **By Year-End:** CEO freed from data processing, system scales to 50+ employees

**Key Insight:**
> "Until you finish one thing, don't start another. 2-3 days per project. Keep focus. Have time frames. The deadline burns."

The conversation also reveals **deep wisdom** about mental models, strategy, and the difference between tactical execution and strategic thinking. The developer is technically skilled but lacks the "battlefield view" - the ability to see how all pieces connect into a coherent system.

**Metaphor of the Day:**
> "The kid grew out of his sandals and shorts, but we're still trying to make them fit. Our management system is 17-year-old shorts on an adult. Time to upgrade."

---

**Document Analysis Date:** 2025-11-25
**Framework:** MAIN_PROMPT_v6 Entity Taxonomy
**Confidence:** High (transcript quality varied but key points clear)
**Next Review:** After Week 4 completion (Nov 29, 2025)
