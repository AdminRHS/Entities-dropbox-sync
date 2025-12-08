# Google Drive Upload Workflow

**Entity:** VID
**Purpose:** Streamline post-shoot asset management
**Last Updated:** 2025-12-08

---

## Overview

This workflow ensures all video footage is:
- Backed up immediately after shooting
- Organized consistently
- Accessible for editing
- Secured with redundancy

---

## Immediate Post-Shoot Workflow

### Step 1: Initial Backup (Within 30 Minutes)

**Action:** Copy raw footage from camera to computer

**Process:**
1. Insert memory card into card reader
2. **DO NOT format card yet**
3. Create temporary folder on desktop: `TEMP_YYYY-MM-DD_project_name`
4. Copy ALL files from card to temp folder
5. Verify file count matches
6. Leave memory card untouched until Google Drive backup complete

**Verification:**
```
Card files: 47 files, 23.4 GB
Temp folder: 47 files, 23.4 GB
✓ Match confirmed
```

---

### Step 2: Google Drive Upload (Within 1 Hour)

**Navigate to:**
`Google Drive > Video Production > Raw Footage/`

**Create Project Folder:**
```
Format: YYYY-MM-DD_project_name_description
Example: 2025-12-08_tutorial_python_basics
```

**Folder Structure:**
```
2025-12-08_tutorial_python_basics/
├── raw/
│   └── (all camera files)
├── audio/
│   └── (separate audio if any)
├── metadata.txt
└── shoot_notes.txt
```

**Upload Process:**
1. Drag `TEMP_YYYY-MM-DD_project_name` → `raw/` folder in Drive
2. Start upload
3. **DO NOT** close browser/app during upload
4. Monitor progress
5. Wait for "Upload complete" confirmation

**Create Metadata File:**
```
metadata.txt content:
---
Shoot Date: YYYY-MM-DD
Project: [Name]
Location: [Address]
Duration: [HH:MM]
Camera: [Model]
Settings: [Brief notes]
Outfit: [Outfit #XXX from catalog]
Weather: [If outdoor]
Issues: [Any problems noted]
Total Files: [Count]
Total Size: [GB]
Uploaded: YYYY-MM-DD HH:MM
Uploaded By: [Name]
---
```

---

### Step 3: Local Backup (Within 2 Hours)

**Purpose:** Redundancy - never rely on single backup

**Backup Location Options:**
1. External hard drive (recommended)
2. Secondary computer
3. NAS (Network Attached Storage)

**Process:**
1. Connect backup drive
2. Navigate to `Video Backups/` folder
3. Create same folder structure:
   `YYYY-MM-DD_project_name_description/`
4. Copy all files from temp folder
5. Verify file count and size match

**Verification Checklist:**
- [ ] Google Drive upload complete (verify in browser)
- [ ] Local backup complete
- [ ] Both match source file count
- [ ] Both match source file size
- [ ] Metadata file created
- [ ] Shoot notes documented

---

### Step 4: Memory Card Management (After Verification)

**ONLY after both backups verified:**

1. Open temp folder on desktop
2. Open Google Drive folder (verify files visible)
3. Open local backup folder (verify files visible)
4. Compare file counts all match
5. **Now safe to format memory card**

**Format Card:**
- In camera (preferred) OR
- In computer (select "quick format")
- Verify card is empty
- Test card with test photo/video
- Card ready for next shoot

**Clean Up:**
- Delete temp folder from desktop
- Empty computer trash/recycle bin
- Note backup completion in content_calendar.md

---

## Organizing Edited Content

### Step 5: Project Editing Folder

**Location:**
`Google Drive > Video Production > Edited/`

**Create Project Folder:**
```
project_name/
├── drafts/
│   ├── v1_draft_2025-12-08.mp4
│   ├── v2_draft_2025-12-09.mp4
│   └── notes.txt
├── final/
│   ├── final_4k.mp4
│   ├── final_1080p.mp4
│   ├── final_mobile.mp4
│   └── thumbnail.jpg
├── project_files/
│   └── (editing software project files)
└── assets/
    ├── music/
    ├── graphics/
    └── b-roll/
```

**Workflow:**
```
Raw Footage
  ↓
Edit in software (save project file frequently)
  ↓
Export draft → drafts/ folder
  ↓
Review, revise
  ↓
Export final → final/ folder
  ↓
Upload to platform
  ↓
Archive project
```

---

## Automated Upload (Future Enhancement)

### Google Drive API Integration

**Goal:** Automate upload on memory card insertion

**Script Concept:**
```python
# Future automation script
import os
import google.auth
from googleapiclient.discovery import build

def auto_upload_video():
    # Detect memory card insertion
    # Copy files to temp
    # Upload to Drive
    # Verify upload
    # Update content_calendar.md
    # Notify user
```

**Status:** Planned for Week 03
**Dependencies:** Google Drive API, Python script, automation-agent integration

---

## Naming Conventions

### File Naming

**Raw Footage:**
- Keep original camera filenames (e.g., MVI_0023.MP4)
- Group in dated folder
- Metadata file explains what they are

**Edited Files:**
```
Format: projectname_version_resolution_date.ext

Examples:
tutorial_python_final_4k_2025-12-10.mp4
tutorial_python_draft_1080p_2025-12-08.mp4
relax_warsaw_vlog_final_mobile_2025-12-15.mp4
```

**Project Folders:**
```
Format: YYYY-MM-DD_category_description

Examples:
2025-12-08_tutorial_python_basics
2025-12-10_relax-warsaw_weekend_vlog
2025-12-15_business_company_update
```

---

## Storage Quota Management

### Google Drive Space

**Monitor:**
- Check storage usage weekly
- Plan cleanup before hitting limits
- Archive old projects

**Free Up Space:**
1. Export old projects to external drive
2. Delete from Drive (keep local backup)
3. Compress old projects (zip)
4. Remove duplicate exports

**Upgrade Decision Points:**
- 80% full: Start archiving old content
- 90% full: Consider upgrade or aggressive cleanup
- If regular production: Budget for paid storage

---

## Backup Schedule

### Short-Term (Active Projects)
- **Immediate:** Raw footage (as described above)
- **Daily:** Save editing project files
- **Per milestone:** Export draft to Drive

### Mid-Term (Recent Projects)
- **Weekly:** Verify all backups still accessible
- **Monthly:** Archive completed projects

### Long-Term (Archive)
- **Quarterly:** Export to external drive
- **Yearly:** Review and clean up old projects
- **Permanent:** Keep raw footage of important projects

---

## Verification Procedures

### Upload Verification Checklist

**After Every Upload:**
- [ ] File count matches source
- [ ] File size matches source (within a few KB)
- [ ] Files can be opened/played in Drive
- [ ] Folder structure correct
- [ ] Metadata file included
- [ ] Content calendar updated
- [ ] Editing task created

**Monthly Backup Audit:**
- [ ] Random sample of 3 projects
- [ ] Open files to verify not corrupted
- [ ] Check Drive + local backup both exist
- [ ] Verify metadata accurate
- [ ] Test download/restore process

---

## Troubleshooting

### Upload Fails / Interrupts

**Problem:** Upload stops mid-way

**Solutions:**
1. Check internet connection
2. Check Drive storage quota
3. Restart upload from Drive app (resumes automatically)
4. If repeated failures: Upload in smaller batches

### Files Corrupted

**Problem:** File won't play after upload

**Solutions:**
1. Re-upload from original card (if not formatted)
2. Try different player/codec
3. Upload via Drive desktop app instead of browser
4. Check file wasn't corrupted at recording

### Out of Storage Space

**Problem:** Drive quota exceeded

**Solutions:**
1. Archive old projects (see Storage Management)
2. Delete duplicate exports
3. Compress/remove draft versions
4. Upgrade Drive storage plan
5. Use local storage for raw footage archives

---

## Integration with Automation Agent

### Detection Workflow

```
User completes shoot
  ↓
Memory card inserted
  ↓
Automation detects: new video files
  ↓
Copies to temp folder
  ↓
Creates Drive folder (dated/named)
  ↓
Uploads to Drive
  ↓
Verifies upload complete
  ↓
Creates local backup
  ↓
Updates content_calendar.md
  ↓
Creates editing task in Share/
  ↓
Notifies user: "Upload complete, safe to format card"
```

**Manual Override:** Always available
**Status:** Designed, implementation Week 03

---

## Content Calendar Integration

### Auto-Update Template

```markdown
## Project: [Name]

**Shoot Date:** YYYY-MM-DD
**Status:** Footage uploaded ✓
**Drive Location:** Video Production/Raw Footage/YYYY-MM-DD_project_name/
**Local Backup:** ✓ Verified
**Editing Status:** Pending
**Editing Task:** Created in Share/tasks_Niko_Kar_002_YYYY-MM-DD.md
**Deadline:** [TBD]
**Platform:** [YouTube/Instagram/etc.]
**Notes:** [Any shoot notes]
```

---

## Quick Reference Checklist

### Immediate Post-Shoot (Print This)

**☐ Phase 1: Initial Copy (30 min)**
- Insert card → computer
- Create TEMP folder on desktop
- Copy ALL files
- Verify file count match
- Leave card in reader

**☐ Phase 2: Google Drive (1 hour)**
- Create dated folder in Drive
- Upload from TEMP folder
- Create metadata.txt
- Wait for "Upload complete"
- Open Drive, verify files visible

**☐ Phase 3: Local Backup (2 hours)**
- Connect backup drive
- Create same folder structure
- Copy from TEMP folder
- Verify file count match

**☐ Phase 4: Verification**
- Drive: files open/play ✓
- Local: files open/play ✓
- Counts match: Card = TEMP = Drive = Local ✓

**☐ Phase 5: Cleanup**
- Format memory card (in camera)
- Delete TEMP folder
- Empty trash
- Update content_calendar.md
- Create editing task

**☐ Done!**
- Footage safe
- Card ready for next shoot
- Editing can begin

---

**Workflow Version:** 1.0
**Last Updated:** 2025-12-08
**Tested:** Pending first production use
**Feedback:** Update after first 3 uploads
