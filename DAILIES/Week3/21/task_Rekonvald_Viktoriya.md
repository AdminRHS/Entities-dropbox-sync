# Task Breakdown - November 21, 2025

## Instructions
**What**: Detailed action steps for today
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Fix Discord ID Matching for Employee Statistics

### Steps:

1. **Gather Profile Data**
   - Access profile files from `Finance/November/public/` (shared profiles with Discord usernames)
   - Access profile files from `ENTITIES/TALENTS/Employees/profiles/` (individual employee profiles)
   - Extract Discord IDs and usernames from both sources

2. **Create ID Mapping**
   - Match Discord numeric IDs from voice logs to employee names using profile data
   - Create mapping table/document linking IDs to usernames and employee names
   - Verify mapping accuracy for all employees

3. **Re-run Statistics Calculation**
   - Use the ID mapping to correctly identify employees in Discord voice logs
   - Recalculate attendance statistics for November 18th (and other dates as needed)
   - Verify counts are now accurate

### Resources and Links:
- **Resource 1:** `Finance/November/public/` - Shared employee profiles
- **Resource 2:** `ENTITIES/TALENTS/Employees/profiles/` - Individual employee profiles
- **Resource 3:** `ENTITIES/TALENTS/Employees/Voice Log Discord/attendance_report_2025-11-18.json` - Discord voice logs

### Instructions:
- **Priority:** 🚨 Critical (blocks accurate employee analysis)
- **Time Estimate:** ~1-2 hours
- **Start with:** Gathering profile files from both locations
- **End with:** Accurate Discord statistics with proper ID matching

---

## Task 2: Standardize Employee Folder Structures Across Departments

### Steps:

1. **Analyze Current Structures**
   - Review folder structures for Devs, HR, and LeadGens departments
   - Document inconsistencies (dates vs weeks, different naming conventions)
   - Identify which employees need reorganization

2. **Define Standard Structure**
   - Create standard folder structure template (e.g., Week_X/Day format)
   - Document the standard in a reference file
   - Ensure structure supports automated processing

3. **Reorganize Folders**
   - Use AI assistance to rename/reorganize employee folders consistently
   - Apply standard structure to all departments
   - Verify all employees now follow the same structure

### Resources and Links:
- **Resource 1:** Employee folders in `HR Nov25/` directory
- **Resource 2:** AI tools (Cursor, VS Code + Gemini/AntiGravity) for bulk reorganization

### Instructions:
- **Priority:** 🟡 High (enables automated processing)
- **Time Estimate:** ~2-3 hours
- **Start with:** Analyzing current structures and documenting inconsistencies
- **End with:** All employee folders standardized across departments

---

## Task 3: Complete LeadGen TODO File Distribution

### Steps:

1. **Address Folder Structure Issues**
   - Fix folder structure inconsistencies for LeadGen employees first
   - Ensure all LeadGen folders follow standard Week_X/Day format

2. **Create Remaining TODO Files**
   - Generate TODO.md files for remaining LeadGen employees
   - Include same content as Devs/HR (Anti-Gravity download instructions, documentation reminders)
   - Ensure files are placed in correct employee folders

3. **Verify Distribution**
   - Check that all LeadGen employees now have TODO.md files
   - Verify file content matches standard template

### Resources and Links:
- **Resource 1:** LeadGen employee folders
- **Resource 2:** TODO.md template from Day 19 work

### Instructions:
- **Priority:** 🟡 High (complete previous day's work)
- **Time Estimate:** ~1 hour
- **Start with:** Fixing folder structures for LeadGen employees
- **End with:** All LeadGen employees have TODO.md files

---

## Task 4: Set Up Automated Delivery System for TODO Files

### Steps:

1. **Extract Tokens from Dropbox**
   - Locate Secret Key in Dropbox
   - Extract creation tokens needed for email/Discord automation
   - Store tokens securely (do not share with third parties)

2. **Configure Discord Delivery**
   - Set up Discord bot/script for sending messages
   - Configure server NITN8 or direct message functionality
   - Create message template with TODO file link/path

3. **Configure Email Delivery**
   - Set up email sending script using extracted tokens
   - Create email template with TODO file information
   - Test email delivery to ensure it works

4. **Test Both Channels**
   - Send test messages via Discord
   - Send test emails
   - Verify employees receive notifications correctly

### Resources and Links:
- **Resource 1:** Dropbox (Secret Key, creation tokens)
- **Resource 2:** Discord server NITN8
- **Resource 3:** Corporate email accounts

### Instructions:
- **Priority:** 🟡 High (enables automated task distribution)
- **Time Estimate:** ~2-3 hours
- **Start with:** Extracting tokens from Dropbox securely
- **End with:** Both Discord and Email channels working for automated delivery

---

## Task 5: Standardize Taxonomy Across All Entities

### Steps:

1. **Identify Inconsistencies**
   - Review all entities for naming inconsistencies
   - Document examples (e.g., "mls" vs "miles to miles to")
   - Create list of all inconsistencies found

2. **Create Unified Taxonomy Document**
   - Define standard naming conventions
   - Map old names to new standard names
   - Document taxonomy hierarchy and structure

3. **Update All References**
   - Update all entity files to use standard taxonomy
   - Update all references in documentation
   - Verify consistency across entire system

### Resources and Links:
- **Resource 1:** All entity folders in `ENTITIES/`
- **Resource 2:** Existing taxonomy files

### Instructions:
- **Priority:** 🟢 Medium (improves system consistency)
- **Time Estimate:** ~2-3 hours
- **Start with:** Reviewing entities and identifying inconsistencies
- **End with:** Unified taxonomy applied across all entities

---

## Task 6: Integrate Courses and Lessons into Task Templates

### Steps:

1. **Determine Course Storage Location**
   - Review existing course/lesson structure
   - Decide where courses should be stored (document in entities)
   - Ensure location supports cross-referencing with tasks

2. **Document Course Storage**
   - Create documentation for course storage location
   - Update FILES.md or similar documentation files
   - Ensure all folders in entities are properly documented

3. **Integrate into Task Templates**
   - Update Task Templates to include course/lesson references
   - Ensure tasks can cross-reference courses and lessons
   - Test integration with existing onboarding tasks

### Resources and Links:
- **Resource 1:** `ENTITIES/TASKS/Tasks/` - Existing task structure
- **Resource 2:** `ENTITIES/ASSETS/oa-y/Courses` and `oa-y/Lessons` - Course/lesson locations
- **Resource 3:** Task Manager system

### Instructions:
- **Priority:** 🟢 Medium (enhances task system)
- **Time Estimate:** ~1-2 hours
- **Start with:** Determining course storage location
- **End with:** Courses and lessons integrated into Task Templates

---

## Task 7: Improve Action Normalization Pipeline Accuracy

### Steps:

1. **Review Current Pipeline**
   - Understand how Action Normalization works (finds verbs → matches objects → forms actions)
   - Identify accuracy issues and edge cases
   - Document current limitations

2. **Test and Validate**
   - Run pipeline on sample daily reports
   - Compare output with manual review
   - Identify specific areas needing improvement

3. **Enhance Pipeline**
   - Improve verb-object matching accuracy
   - Better handling of edge cases and different report formats
   - Add validation steps to catch errors

### Resources and Links:
- **Resource 1:** Action Normalization pipeline code
- **Resource 2:** Sample daily reports in `ENTITIES/DAILIES/`
- **Resource 3:** Existing analyzers (Talents, Employees, Attendance Analyzer)

### Instructions:
- **Priority:** 🟢 Medium (improves analysis quality)
- **Time Estimate:** ~2-3 hours
- **Start with:** Reviewing current pipeline and testing on samples
- **End with:** More accurate Action Normalization pipeline

---

## Task 8: Reorganize Daily Folders Structure

### Steps:

1. **Analyze Current Structure**
   - Review how daily files are currently organized
   - Identify issues with mixing plans and tasks
   - Document desired separation

2. **Create New Structure**
   - Separate plans and tasks into different folders
   - Ensure structure supports easier processing
   - Document new structure

3. **Reorganize Existing Files**
   - Move existing daily files to new structure
   - Update any references to old structure
   - Verify reorganization is complete

### Resources and Links:
- **Resource 1:** `ENTITIES/DAILIES/` - Current daily files structure
- **Resource 2:** Daily files from previous days (18, 19, 20)

### Instructions:
- **Priority:** 🟢 Medium (improves file organization)
- **Time Estimate:** ~1 hour
- **Start with:** Analyzing current structure and planning new structure
- **End with:** Daily folders reorganized with separated plans and tasks

---

## Task 9: Continue HR Research Topics for TASK_MANAGERS

### Steps:

1. **Review Existing Research**
   - Check which videos/topics have been processed
   - Identify gaps in HR automation research
   - Create list of topics still needing research

2. **Process New Videos/Topics**
   - Use Perplexity Deep Research for new HR automation videos
   - Process transcripts through Video Processing prompts
   - Extract tools, workflows, and actions

3. **Integrate into Task Manager**
   - Add new topics to Task Manager system
   - Create tasks, subtasks, and phases based on research
   - Cross-reference with existing content

### Resources and Links:
- **Resource 1:** `ENTITIES/TASK_MANAGERS/RESEARCHES/Videos/` - Video library
- **Resource 2:** `ENTITIES/TASK_MANAGERS/PROMPTS/` - Research prompts
- **Resource 3:** Perplexity Deep Research tool

### Instructions:
- **Priority:** 🟢 Medium (ongoing research work)
- **Time Estimate:** ~2-3 hours
- **Start with:** Reviewing existing research and identifying gaps
- **End with:** New HR research topics integrated into Task Manager

---

## Task 10: Process Video_016 Findings Integration

### Steps:

1. **Review Video_016 Processing Results**
   - Check what was extracted from Video_016 (tools, workflows, actions)
   - Review taxonomy and workflow information
   - Identify what needs to be integrated

2. **Integrate into Task Manager**
   - Add Video_016 findings to Task Manager entities
   - Create task templates based on extracted information
   - Update libraries with new tools/workflows found

3. **Update Documentation**
   - Document Video_016 findings in appropriate files
   - Update FILES.md or similar documentation
   - Ensure findings are accessible for future reference

### Resources and Links:
- **Resource 1:** `ENTITIES/TASK_MANAGERS/RESEARCHES/Videos/Video_016.md`
- **Resource 2:** Task Manager system
- **Resource 3:** Notes from Day 17 about Video_016 processing

### Instructions:
- **Priority:** 🟢 Medium (complete previous research work)
- **Time Estimate:** ~1-2 hours
- **Start with:** Reviewing Video_016 processing results
- **End with:** Video_016 findings integrated into Task Manager

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
- Track progress on each task
- Update CRM systematically
- Maintain communication standards
- Keep focus on main priorities - avoid getting distracted by tool exploration
- Track which AI tools are being used (Cursor, VS Code + Gemini/AntiGravity, Perplexity) for efficiency

