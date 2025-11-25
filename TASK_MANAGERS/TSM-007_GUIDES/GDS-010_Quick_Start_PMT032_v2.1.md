# GDS-010: Quick Start Guide - PMT-032 v2.1

**Version:** 1.0
**Created:** 2025-11-22
**Department:** AI Department (AID)
**Category:** Tutorial
**Estimated Read Time:** 7 minutes
**Priority:** Critical - Required for all employees

---

## Overview

This quick start guide will get you up and running with the PMT-032 v2.1 Daily Report Collection framework. You'll learn how to:

- Set up Whisper Flow for activity recording
- Structure your daily log file
- Map activities to entity codes (TST/MLT/PRT)
- Submit your daily report

**Who needs this guide:** All employees submitting daily reports

**Related Templates:**
- PRT-001: Daily Report Collection
- TST-042: Daily Report Submission
- TST-043: Whisper Flow Recording

---

## Table of Contents

1. [Before You Start](#before-you-start)
2. [Step 1: Set Up Whisper Flow](#step-1-set-up-whisper-flow)
3. [Step 2: Create Your Daily Log File](#step-2-create-your-daily-log-file)
4. [Step 3: Record Your Activities](#step-3-record-your-activities)
5. [Step 4: Map Entity Codes](#step-4-map-entity-codes)
6. [Step 5: Submit Your Report](#step-5-submit-your-report)
7. [Troubleshooting](#troubleshooting)
8. [Quick Reference](#quick-reference)

---

## Before You Start

### What You'll Need

- ✅ Whisper Flow installed and configured
- ✅ Access to your daily log file: `ENTITIES/DAILIES/[DD]/daily_[YourName].md`
- ✅ Claude or Gemini for assistance (optional but recommended)
- ✅ Headphones for clear audio recording

### Estimated Time
- **First time:** 15-20 minutes
- **Once familiar:** 5-10 minutes per day

---

## Step 1: Set Up Whisper Flow

### 1.1 Install Whisper Flow

**Windows:**
```bash
# Download from internal tools repository
# Run installer
whisper-flow-setup.exe
```

**Configuration:**
1. Select your microphone/headset
2. Set recording quality: "High"
3. Enable auto-transcription
4. Set output format: "Text"

### 1.2 Test Your Recording

Before starting your workday:

1. Open Whisper Flow
2. Click "Start Recording"
3. Speak for 10 seconds: "Testing Whisper Flow. This is [Your Name] on [Date]."
4. Click "Stop Recording"
5. Verify transcription appears correctly

**✅ Success criteria:** You can read your transcribed text clearly

**❌ Common issues:**
- No audio detected → Check microphone permissions
- Garbled text → Adjust microphone volume, speak closer to mic
- No transcription → Verify auto-transcription is enabled

---

## Step 2: Create Your Daily Log File

### 2.1 File Location

Your daily log is stored in:
```
ENTITIES/DAILIES/[DD]/daily_[FirstName]_[LastName].md
```

**Example:**
```
ENTITIES/DAILIES/22/daily_John_Smith.md
```

### 2.2 Daily Log Template

Your file should follow this structure:

```markdown
# Daily Log - [DD.MM.YYYY]

## Instructions
**What**: Record of all your activities throughout the day
**Include**:
- Time stamps for each activity
- What you worked on
- Whisper Flow transcripts from all meetings/calls
- Outcomes and results

---

## Activities

### [HH:MM - HH:MM] - [Activity Name]
**What I worked on:**
- [Description of work]
- [Key tasks completed]

**Whisper Flow Transcript:**
[Paste your narration here]

**Outcomes:**
- [Result 1]
- [Result 2]

---

## Notes
-

## Reminder
- Whisper Flow ON during all activities
- Update this file throughout the day
- Include all meeting transcripts
```

### 2.3 Create Your File (First Time)

1. Navigate to `ENTITIES/DAILIES/[today's date]/`
2. Copy the template above
3. Save as `daily_[YourFirstName]_[YourLastName].md`
4. Fill in today's date

---

## Step 3: Record Your Activities

### 3.1 When to Record

**Start Whisper Flow:**
- ✅ Beginning of each work activity
- ✅ Before meetings or calls
- ✅ When starting a new task
- ✅ During focused work sessions

**Stop Whisper Flow:**
- When taking a break
- When switching to personal time
- At end of workday

### 3.2 What to Say in Your Recording

**Good narration includes:**

```
"I'm working on [task name]. This is for [project/milestone].
I started by [first action]. Then I [second action].
I encountered [any issues]. I resolved it by [solution].
The outcome was [result]. This took approximately [X] hours."
```

**Example:**
```
"I'm working on creating video course covers for the Gemini course.
This is for the Content Creation project. I started by adjusting
the images to the correct sizes using Firefly. Then I attempted
to create animations using Runway, but it was taking too long.
I discussed this with my team lead Yulia in the daily meeting,
and we decided to postpone the animation task. The outcome was
that I completed the static covers and moved to the test task
for redesigning the home page. This took about 4 hours."
```

### 3.3 Transcribe and Add to Your Daily Log

1. Stop Whisper Flow recording
2. Copy the transcription
3. Open your daily log file
4. Paste into the **Whisper Flow Transcript** section
5. Add the time range (e.g., "9:00 - 13:00")
6. Add activity name

---

## Step 4: Map Entity Codes

### 4.1 Understanding Entity Types

Every activity should be mapped to an entity code:

| Code Pattern | Type | Example | When to Use |
|--------------|------|---------|-------------|
| **PRT-###** | Project | PRT-001: Daily Report Collection | Large initiatives, multi-week efforts |
| **MLT-###** | Milestone | MLT-005: Task Validation | Major checkpoints within projects |
| **TST-###** | Task | TST-042: Daily Report Submission | Specific tasks, daily activities |
| **STP-###** | Step | STP-127: Whisper Flow Initialization | Granular sub-tasks |

**Most common for daily logs:** TST-### (Task codes)

### 4.2 Finding the Right Code

**Method 1: Ask Claude/Gemini**
```
"What is the task code for daily report submission?"
→ TST-042
```

**Method 2: Browse Task Templates**
1. Open `ENTITIES/TASK_MANAGERS/TSM-003/`
2. Search for task name
3. Code is in filename: `TST-042_Daily_Report_Submission.md`

**Method 3: Check Common Codes**

**Frequent Task Codes:**
- TST-042: Daily Report Submission
- TST-043: Whisper Flow Recording
- TST-044: Entity Mapping Validation
- TST-101: Social Media Post Creation
- TST-018: Entity Classification

### 4.3 Adding Entity Codes to Your Log

In your activity description, reference the entity code:

```markdown
### [9:00 - 13:00] - Course Images & Daily Meeting

**Entity:** TST-XXX (Image Creation Task)

**What I worked on:**
- Adjusted course images to correct sizes using Firefly
- Attempted animations for modules using Runway
- Attended Daily meeting with Team Lead
```

**Note:** Don't worry about getting it perfect! The AI Department will help validate codes during report processing.

---

## Step 5: Submit Your Report

### 5.1 End-of-Day Checklist

Before submitting, verify:

- ✅ All activities have time stamps
- ✅ All Whisper Flow transcripts are included
- ✅ Outcomes are documented for each activity
- ✅ Entity codes are noted (or marked for validation)
- ✅ Total hours approximately add up to your work time

### 5.2 Submission Process

**Automatic submission:** Your daily log file is automatically picked up from the `ENTITIES/DAILIES/[DD]/` folder.

**What happens next:**
1. AI Department processes all daily logs
2. Entity codes are validated
3. Department report is generated
4. You receive feedback if any issues

**Timeline:** Reports processed next business day

### 5.3 Review Your Department Report

The next day, check:
```
ENTITIES/REPORTS/[YYYY-MM-DD]/Departments/[YourDepartment]_Department_Report_[YYYY-MM-DD].md
```

**What to look for:**
- Your activities are listed correctly
- Hours are accurate
- Entity mappings are validated
- Any feedback or corrections

---

## Troubleshooting

### Issue: Whisper Flow not recording

**Symptoms:** No audio captured, transcription empty

**Solutions:**
1. Check microphone permissions in Windows settings
2. Restart Whisper Flow application
3. Try a different audio input device
4. Verify microphone is not muted

---

### Issue: Can't find the right entity code

**Symptoms:** Unsure which TST/MLT/PRT code to use

**Solutions:**
1. Use placeholder: `TST-TBD (Task name)`
2. Describe the work clearly in your log
3. AI Department will help assign correct code
4. Refer to GDS-011 (Entity Mapping Tutorial) for detailed guidance

---

### Issue: Forgot to record an activity

**Symptoms:** Realized at end of day you forgot Whisper Flow

**Solutions:**
1. Write a manual description of the activity
2. Estimate time spent
3. Note in brackets: `[Manual entry - Whisper Flow not recorded]`
4. Try to recall key details and outcomes

**Example:**
```markdown
### [14:00 - 16:00] - Client meeting preparation

[Manual entry - Whisper Flow not recorded]

**What I worked on:**
- Prepared slides for client presentation
- Reviewed project status
- Compiled questions for client

**Outcomes:**
- Presentation deck ready
- Agenda finalized
```

---

### Issue: Activity took longer than expected

**Symptoms:** Time tracking seems inaccurate

**Solutions:**
1. Be honest about actual time spent
2. Include context: `"Took longer due to [reason]"`
3. Note blockers or challenges encountered
4. This helps improve future estimates

---

## Quick Reference

### Daily Workflow

```
1. Morning:
   ✓ Open your daily log file
   ✓ Start Whisper Flow for first activity

2. Throughout day:
   ✓ Record each activity with Whisper Flow
   ✓ Transcribe and add to log after each activity
   ✓ Note time ranges and outcomes

3. End of day:
   ✓ Review all activities are logged
   ✓ Save your daily log file
   ✓ Automatic submission happens overnight

4. Next day:
   ✓ Check department report for your entries
   ✓ Review any feedback
```

### Essential Shortcuts

| Action | Shortcut | Notes |
|--------|----------|-------|
| Start Whisper Flow | `Ctrl+Shift+W` | If enabled in settings |
| Stop Whisper Flow | `Ctrl+Shift+S` | If enabled in settings |
| Open daily log | Navigate to `DAILIES/[DD]/` | Or use your editor's recent files |

### Key File Paths

```
Your daily log:
ENTITIES/DAILIES/[DD]/daily_[FirstName]_[LastName].md

Your department report:
ENTITIES/REPORTS/[YYYY-MM-DD]/Departments/[Dept]_Department_Report_[YYYY-MM-DD].md

Task templates (for entity codes):
ENTITIES/TASK_MANAGERS/TSM-003/TST-XXX_[TaskName].md
```

### Common Entity Codes

```
TST-042  Daily Report Submission
TST-043  Whisper Flow Recording
TST-044  Entity Mapping Validation
TST-045  Activity Time Tracking
TST-101  Social Media Post Creation
TST-102  Content Template Application

→ Full list in TASK_MANAGERS/TSM-003/
```

---

## Next Steps

### After Your First Report

Once you've submitted your first daily report:

1. **Read GDS-011** (Entity Mapping Tutorial) - Learn entity codes in depth
2. **Review your department report** - See how your work is aggregated
3. **Ask questions** - Reach out to AI Department for help
4. **Iterate and improve** - Your daily logs will get faster with practice

### Additional Resources

- **GDS-011:** Entity Mapping Tutorial - Deep dive into TST/MLT/PRT codes
- **GDS-012:** Template Cross-Reference Guide - Understanding template relationships
- **PMT-032 Full Documentation:** Complete framework specification
- **TSM-007_GUIDES:** All available guides and tutorials

---

## Support

### Getting Help

**For technical issues:**
- AI Department: [Contact info]
- IT Support: [Contact info]

**For process questions:**
- Your Department Lead
- AI Department (entity mapping, report processing)

**For this guide:**
- Questions or feedback: Submit to AI Department
- Suggest improvements: Create issue in documentation repo

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-22 | Initial creation | AI Department |

---

## Metadata

**Guide Code:** GDS-010
**ISO Code:** GDS (GuiDeS)
**Scope:** task_template
**Status:** Active
**Tags:** #beginner #onboarding #daily_workflow #required #whisper_flow #claude

**Related Templates:**
- PRT-001: Daily Report Collection [Required]
- MLT-001: Weekly Report Compilation [Recommended]
- MLT-002: Monthly Report Aggregation [Recommended]
- TST-042: Daily Report Submission [Required]
- TST-043: Whisper Flow Recording [Required]
- TST-044: Entity Mapping Validation [Recommended]
- TST-045: Activity Time Tracking [Recommended]

**Available Formats:**
- 📄 Markdown (Primary) - This file
- 📑 PDF - [To be generated]
- 🎥 Video Tutorial (5 min) - [To be created]

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md`
**Maintained By:** AI Department
**Last Updated:** 2025-11-22
**Status:** Active
