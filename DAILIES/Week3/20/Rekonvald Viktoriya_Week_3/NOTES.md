## Notes – Week 3 / Day 20

Use this file as a flexible space to write down anything relevant while you are working on Day 20.  
It can include ideas, questions, meeting notes, reminders, or short summaries of what you just did.

## Quick Notes

Write short bullet points here during work so you do not lose important thoughts or context.

- **Focus reminder**: Keep main priority on employee analysis and task generation, avoid getting distracted by tool exploration
- **Resource tracking**: Monitor which AI tools are being used (Cursor, VS Code + Gemini/AntiGravity, Perplexity) and their resource usage
- **Data sources**: Discord logs, CRM exports, attendance records, daily reports in Dropbox
- **Delivery channels**: Discord (minimum) + Email (preferred) for sending TODO files to employees

## Meeting or Conversation Notes

If you have any discussions (online or offline) that impact today's work, summarize them here in complete sentences.  
Include who was involved, what was decided, and any follow-up actions.

- **From Day 19 call with Niko**: Need to return employees' tasks for tomorrow via at least 2 channels (Discord minimum, email preferred). Can use Discord server NITN8 or direct messages. For email, need to extract tokens from Dropbox (Secret Key, creation tokens). Goal is to get employee analysis without direct conversation.

## Ideas and Questions

Use this section for ideas that are not yet tasks, or questions you want to ask later.  
You can later convert important items from here into tasks in `TASK.md`.

- **Question**: How to best structure TODO.md files for employees? Should they include activity summary, specific tasks, priorities, reminders?
- **Idea**: Create template system for TODO generation that can be reused across different days
- **Question**: What's the best way to match Discord IDs when profiles don't have Discord IDs listed?
- **Idea**: Build automated pipeline that combines all data sources and generates reports automatically
- **Question**: Should we standardize employee folder structures across all departments for easier processing?

## Technical Notes

- **Action Normalization pipeline**: Processes daily reports in stages - first finds verbs, then matches objects, then forms actions
- **Discord ID matching**: Need to use profile files from ENTITIES/TALENTS/Employees/profiles or Finance/November/public
- **Tools being used**: Cursor, VS Code + Gemini/AntiGravity extension, Perplexity for API/field questions
- **Data locations**: 
  - Discord logs: ENTITIES/TALENTS/Employees/Voice Log Discord/
  - CRM exports: ENTITIES/TALENTS/Employees/crm_export_attendance/
  - Attendance: ENTITIES/REPORTS/
  - Daily reports: ENTITIES/DAILIES/18/

## Issues Found

- **Discord statistics calculation**: Currently showing incorrect counts because IDs don't match usernames properly
- **Profile data**: Some employees don't have Discord IDs in their profile files
- **Folder structure inconsistency**: Different departments organize employee folders differently (some by dates, some by weeks)

## Follow-up from Day 19

- Added Antigravity to tools library (ENTITIES/LIBRARIES/LBS_003_Tools/AI_Tools/Antigravity.json)
- Created onboarding tasks in ENTITIES/TASKS/Tasks/ based on onboarding instructions
- Need to integrate courses and lessons into Task Templates
- Need to standardize taxonomy across all entities

