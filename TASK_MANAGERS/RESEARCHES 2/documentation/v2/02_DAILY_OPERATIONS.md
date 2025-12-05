# RESEARCHES 2 - Daily Operations Guide

**Version:** 2.0
**Generated:** 2025-12-04
**Purpose:** Day-to-day operational procedures and checklists
**Audience:** All team members performing daily tasks

---

## 📖 Table of Contents

1. [Daily Startup Checklist](#daily-startup-checklist)
2. [Morning Operations](#morning-operations)
3. [Queue Management](#queue-management)
4. [Video Processing Operations](#video-processing-operations)
5. [Quality Control Checks](#quality-control-checks)
6. [End-of-Day Procedures](#end-of-day-procedures)
7. [Weekly Operations](#weekly-operations)
8. [Monthly Operations](#monthly-operations)
9. [Role-Specific Daily Tasks](#role-specific-daily-tasks)
10. [Monitoring & Alerts](#monitoring--alerts)

---

## Daily Startup Checklist

**Time:** 10-15 minutes
**When:** Start of each workday
**Who:** All team members

### ✅ Morning Checklist (5 minutes)

```
□ Check your assigned tasks in Video_Queue_Master.csv
□ Review any overnight automation results
□ Check for new search assignments in Search_Queue_Master.csv
□ Open required tools (VS Code, Excel, AI platforms)
□ Check system notifications or team messages
□ Review yesterday's completed work for any follow-ups
```

### ✅ System Health Check (5 minutes)

```bash
# Check if all CSV files are accessible
□ Open: RESEARCHES_Master_List.csv
□ Open: Video_Queue_Master.csv
□ Open: Search_Queue_Master.csv

# Verify recent backups exist
□ Check: 07_ARCHIVE/backups/ folder has today's date
□ Verify: Last backup completed successfully

# Check automation logs
□ Review: scripts/logs/automation.log for errors
□ Check: Any failed script runs from previous day
```

### ✅ Priority Tasks Identification (5 minutes)

**Questions to answer:**
- What's my primary task for today?
- Are there any urgent/blocked items?
- What's the expected completion time?
- Do I need help or resources?

**Update your status:**
```csv
# In Video_Queue_Master.csv, update your tasks:
Status: "In Progress" (if starting today)
```

---

## Morning Operations

**Time:** 30-45 minutes
**When:** 9:00-10:00 AM
**Who:** Team leads and coordinators

### Task 1: Review Video Queue Status (15 minutes)

**Open:** `01_QUEUE_ASSIGNMENTS/Video_Queue_Master.csv`

**Check each status category:**

```csv
Status = "Assigned" → Verify employee notified
Status = "In Progress" → Check if progress made yesterday
Status = "Blocked" → Identify blockers, assign help
Status = "Review" → Schedule review time
Status = "Completed" → Move to archive planning
```

**Priority sorting:**
1. **Urgent (Priority 80-100):** Review immediately
2. **High (Priority 60-79):** Check progress
3. **Medium (Priority 40-59):** Monitor status
4. **Low (Priority 0-39):** No immediate action needed

**Action items:**
```bash
# Generate priority report
python scripts/generate_priority_report.py

# Output: reports/daily_priority_YYYY-MM-DD.txt
```

### Task 2: Check Search Queue (10 minutes)

**Open:** `00_SEARCH_QUEUE/Search_Queue_Master.csv`

**Review each entry:**
```csv
Status = "Assigned" → Check if employee started
Status = "In Progress" → Verify videos being found
Status = "Completed" → Move videos to Video Queue
```

**If searches completed:**
```bash
# Process completed searches into Video Queue
python scripts/process_search_results.py SEARCH-XXX
```

### Task 3: Archive Completed Work (10 minutes)

**Check for completed research:**
```bash
# List research ready for archival
python scripts/list_completed_research.py

# Archive completed items
python scripts/archive_research.py RSR-XXX
```

**Verification:**
```
□ Research moved to 07_ARCHIVE/RSR-XXX/
□ Master list updated with completion date
□ All reports generated and saved
□ Quality metrics recorded
```

### Task 4: Update Team Dashboard (10 minutes)

**Generate daily status:**
```bash
python scripts/generate_daily_status.py
```

**Share with team:**
- Videos in queue: X
- Videos in progress: Y
- Videos completed this week: Z
- Current bottlenecks: [List]
- Priority tasks: [Top 5]

---

## Queue Management

**Time:** Ongoing throughout day
**Who:** Team leads and project managers

### Video Queue Assignment Process

#### Step 1: Review New Videos (10 minutes)

**When:** New videos added to queue

**Process:**
```bash
# Check new videos
grep "Not Started" Video_Queue_Master.csv

# For each new video:
1. Review video metadata (title, channel, duration)
2. Assess complexity (1-5 scale)
3. Calculate priority score
4. Assign to appropriate team member
```

**Assignment criteria:**
- Employee expertise matches topic
- Employee current workload < 3 videos
- Video complexity matches employee level
- Department needs alignment

#### Step 2: Assign Video (5 minutes per video)

**Manual assignment:**
```csv
# Update Video_Queue_Master.csv:
VQ_ID: VQ-120
Assigned_To: "John Doe"
Status: "Assigned"
Date_Assigned: 2025-12-04
Priority_Score: 75
Expected_Completion: 2025-12-06
```

**Automated assignment:**
```bash
python scripts/auto_assign_video.py VQ-120 "John Doe"
```

#### Step 3: Monitor Progress (Daily)

**Check video status:**
```bash
# Videos in progress > 3 days
python scripts/check_overdue_videos.py

# Videos with no recent updates
python scripts/check_stale_videos.py
```

**Follow-up actions:**
- Contact employee if > 3 days in progress
- Offer help if blocked
- Reassign if necessary

### Queue Cleanup Operations

**Daily cleanup (5 minutes):**
```bash
# Remove duplicates
python scripts/remove_duplicates.py

# Archive completed items
python scripts/archive_completed.py

# Update statistics
python scripts/update_queue_stats.py
```

---

## Video Processing Operations

**Time:** 4-6 hours per video
**Who:** Assigned team members

### Phase 1: Transcription (30-60 minutes)

**Daily workflow:**

```bash
# Step 1: Download video (if needed)
# Use: yt-dlp or browser download

# Step 2: Transcribe with Claude AI
# Open: https://claude.ai
# Upload: video file or paste YouTube URL
# Prompt: [Use Phase 1 prompt from 08_PROMPTS_REFERENCE.md]

# Step 3: Save transcription
# Location: 02_TRANSCRIPTIONS/RSR-XXX/
# Filename: RSR-XXX_transcript.md
```

**Quality check:**
```
□ Transcription complete and readable
□ Timestamps included (if applicable)
□ Speaker identification correct
□ No major errors or gaps
□ File saved with correct naming convention
```

**Update status:**
```csv
Video_Queue_Master.csv:
Status: "In Progress - Phase 1 Complete"
Date_Phase1_Complete: 2025-12-04
```

### Phase 2: Extraction (2-3 hours)

**Daily workflow:**

```bash
# Step 1: Read transcription
# Open: 02_TRANSCRIPTIONS/RSR-XXX/RSR-XXX_transcript.md

# Step 2: Extract entities using AI
# Platform: Claude AI or ChatGPT
# Prompt: [Use Phase 2 prompt from 08_PROMPTS_REFERENCE.md]

# Step 3: Manual review and cleanup
# Review each extracted entity
# Verify accuracy and completeness
# Add missing entities
# Remove false positives

# Step 4: Save extracted entities
# Location: 03_EXTRACTION/RSR-XXX/
# Filename: extracted_entities.md
```

**Quality check:**
```
□ All 7 entity types extracted (Workflows, Tools, Objects, Actions, Professions, Skills, Departments)
□ Entities have clear descriptions
□ No duplicates within entity types
□ Entities categorized correctly
□ File formatted properly
```

**Update status:**
```csv
Video_Queue_Master.csv:
Status: "In Progress - Phase 2 Complete"
Date_Phase2_Complete: 2025-12-04
```

### Phase 3: Gap Analysis (15-30 minutes)

**Daily workflow:**

```bash
# Step 1: Run gap analysis script
cd scripts
python run_gap_analysis.py RSR-XXX

# Output: 04_GAP_ANALYSIS/RSR-XXX/gap_analysis_report.md

# Step 2: Review report
# Open: gap_analysis_report.md
# Check: Gap coverage percentages
# Note: Entity types with high gap coverage (>60%)
```

**Quality check:**
```
□ Gap analysis report generated successfully
□ All 7 entity types analyzed
□ Gap coverage percentages calculated
□ Matching scores reasonable (0.00-1.00)
□ New entities properly identified
```

**Update status:**
```csv
Video_Queue_Master.csv:
Status: "In Progress - Phase 3 Complete"
Date_Phase3_Complete: 2025-12-04
```

### Phase 4: Integration (1-2 hours)

**Daily workflow:**

```bash
# Step 1: Create JSON files for new entities
# Location: 05_INTEGRATION/RSR-XXX/
# Create JSON files based on gap analysis

# Step 2: Manual review
# Verify JSON structure correct
# Check all required fields present
# Validate ID formats

# Step 3: Integrate into LIBRARIES
# Copy approved JSON files to LIBRARIES folders
# Update existing entities if needed

# Step 4: Run validation
python scripts/validate_integration.py RSR-XXX
```

**Quality check:**
```
□ All new entities have JSON files
□ JSON structure valid (no syntax errors)
□ ID formats correct (e.g., WRF-XXX-NNN)
□ Required fields populated
□ No duplicate IDs in LIBRARIES
□ Validation script passes
```

**Update status:**
```csv
Video_Queue_Master.csv:
Status: "In Progress - Phase 4 Complete"
Date_Phase4_Complete: 2025-12-04
```

### Phase 5: Mapping (15-30 minutes)

**Daily workflow:**

```bash
# Step 1: Run mapping script
python scripts/run_mapping.py RSR-XXX

# Output: 06_MAPPING/RSR-XXX/entity_mapping_report.md

# Step 2: Review mapping report
# Check: All entities mapped correctly
# Verify: Cross-references valid
# Note: Overall quality score
```

**Quality check:**
```
□ Mapping report generated successfully
□ All entities have LIBRARIES IDs assigned
□ Cross-references valid
□ Quality score ≥ 0.90 (target)
□ No unmapped entities
```

**Update status:**
```csv
Video_Queue_Master.csv:
Status: "Review"
Date_Phase5_Complete: 2025-12-04
Overall_Quality_Score: 0.92
```

---

## Quality Control Checks

**Time:** 30 minutes daily
**Who:** Quality reviewers and team leads

### Daily Quality Review Process

#### Morning Quality Check (15 minutes)

**Check completed phases from yesterday:**

```bash
# List items ready for review
python scripts/list_review_items.py

# For each item in "Review" status:
1. Open all phase files
2. Check quality metrics
3. Verify completeness
4. Approve or request revisions
```

**Quality criteria:**

**Phase 1 (Transcription):**
```
□ Complete transcript
□ Readable formatting
□ Timestamps if applicable
□ No major gaps
```

**Phase 2 (Extraction):**
```
□ All 7 entity types present
□ Minimum entity counts met:
  - Workflows: ≥3
  - Tools: ≥5
  - Objects: ≥5
  - Actions: ≥8
  - Professions: ≥2
  - Skills: ≥5
  - Departments: ≥1
□ Entities have descriptions
□ No obvious duplicates
```

**Phase 3 (Gap Analysis):**
```
□ Report generated successfully
□ Gap coverage calculated
□ Match scores present (0.00-1.00)
□ High-value gaps identified
```

**Phase 4 (Integration):**
```
□ JSON files created for new entities
□ Valid JSON structure
□ Correct ID formats
□ Required fields populated
□ Validation passes
```

**Phase 5 (Mapping):**
```
□ Mapping report complete
□ All entities mapped
□ Quality score ≥ 0.90
□ Cross-references valid
```

#### Afternoon Quality Check (15 minutes)

**Review in-progress work:**

```bash
# Check work in progress
python scripts/check_wip_quality.py

# For each in-progress item:
1. Verify last update time (should be < 24 hours)
2. Check completion percentage
3. Identify any blockers
4. Offer assistance if needed
```

**Update quality metrics:**
```bash
# Generate quality dashboard
python scripts/generate_quality_dashboard.py

# Metrics tracked:
- Average quality score (target: ≥0.90)
- Phase completion rates
- Average processing time per video
- Error rates by phase
- Team member performance
```

---

## End-of-Day Procedures

**Time:** 15-20 minutes
**When:** End of workday
**Who:** All team members

### Individual End-of-Day Tasks (10 minutes)

**Personal checklist:**
```
□ Update status of all assigned videos in queue
□ Save all work in correct folders
□ Commit any in-progress work with notes
□ Update task completion percentage
□ Note any blockers or issues
□ Plan tomorrow's priorities
□ Close all sensitive documents
□ Log time spent on each task
```

**Status update template:**
```csv
Video_Queue_Master.csv updates:

VQ-120:
- Status: "In Progress - Phase 2 50%"
- Notes: "Extraction 50% complete, continuing tomorrow"
- Blocker: "None"
- Expected_Completion: 2025-12-05

VQ-121:
- Status: "In Progress - Phase 3 Complete"
- Notes: "Gap analysis done, ready to start integration"
- Blocker: "Need approval for 3 new workflow entities"
- Expected_Completion: 2025-12-06
```

### Team Lead End-of-Day Tasks (10 minutes)

**Daily summary:**
```bash
# Generate end-of-day report
python scripts/generate_eod_report.py

# Report includes:
- Videos processed today: X
- Phases completed: Y
- Quality score average: Z
- Blockers to address: [List]
- Tomorrow's priorities: [List]
```

**Backup check:**
```bash
# Verify daily backup completed
python scripts/verify_backup.py

# If backup failed, run manual backup:
python scripts/manual_backup.py
```

**Prepare tomorrow's assignments:**
```bash
# Review queue for tomorrow
python scripts/prepare_tomorrow.py

# Assign any urgent new videos
# Send notifications to team members
```

---

## Weekly Operations

**Time:** 2-3 hours
**When:** Every Friday or Monday
**Who:** Team leads and managers

### Weekly Planning Session (1 hour)

**Review week's performance:**
```bash
# Generate weekly report
python scripts/generate_weekly_report.py

# Metrics reviewed:
- Videos processed this week
- Average quality score
- Completion rate vs. target
- Bottlenecks identified
- Team member performance
```

**Plan next week:**
```
□ Review search queue priorities
□ Assign high-priority videos
□ Identify training needs
□ Schedule team meetings
□ Set weekly goals
```

### Weekly Maintenance (1 hour)

**System cleanup:**
```bash
# Archive all completed research from this week
python scripts/weekly_archive.py

# Clean up temporary files
python scripts/cleanup_temp_files.py

# Update all statistics
python scripts/update_all_stats.py

# Verify data integrity
python scripts/verify_data_integrity.py
```

**Quality review:**
```bash
# Review all completed research from week
python scripts/weekly_quality_review.py

# Check for patterns in errors
# Identify improvement opportunities
# Update best practices documentation
```

### Weekly Reporting (1 hour)

**Generate reports for stakeholders:**
```bash
# Management summary
python scripts/generate_management_report.py

# Team performance report
python scripts/generate_team_report.py

# Quality metrics report
python scripts/generate_quality_report.py
```

**Report contents:**
- Week's highlights
- Videos processed (by department)
- New entities added to LIBRARIES
- Quality metrics trends
- Next week's priorities
- Issues and resolutions

---

## Monthly Operations

**Time:** 4-6 hours
**When:** Last Friday of each month
**Who:** Team leads and managers

### Monthly Review (2 hours)

**Performance analysis:**
```bash
# Generate monthly statistics
python scripts/generate_monthly_stats.py

# Metrics tracked:
- Total videos processed
- Quality score trends
- Processing time trends
- Entity growth in LIBRARIES
- Department coverage
- Team productivity
```

**Quality audit:**
```bash
# Random sample quality check
python scripts/monthly_quality_audit.py

# Review 10-15 random completed research items
# Verify quality standards maintained
# Identify systematic issues
```

### Monthly Maintenance (2 hours)

**System optimization:**
```bash
# Optimize CSV files (remove old entries)
python scripts/optimize_csv_files.py

# Clean up archive (compress old files)
python scripts/compress_archives.py

# Update documentation
# Review and update prompts
# Optimize automation scripts
```

**Backup strategy:**
```bash
# Create monthly full backup
python scripts/monthly_backup.py

# Verify backup integrity
python scripts/verify_monthly_backup.py

# Move old backups to long-term storage
```

### Monthly Planning (2 hours)

**Strategic planning:**
```
□ Review department needs
□ Plan next month's research topics
□ Assign search priorities
□ Update team goals
□ Schedule training sessions
□ Review and update processes
```

**Documentation updates:**
```
□ Update this operations guide if needed
□ Update prompts based on learnings
□ Add new troubleshooting solutions
□ Update best practices
□ Review automation opportunities
```

---

## Role-Specific Daily Tasks

### Research Analysts

**Daily focus:** Process assigned videos through all phases

**Typical day:**
```
09:00-09:30  Check assignments, prioritize tasks
09:30-11:00  Phase 1: Transcription (1-2 videos)
11:00-13:00  Phase 2: Extraction (1 video)
13:00-14:00  Lunch / Break
14:00-15:30  Phase 4: Integration work
15:30-16:30  Phase 5: Review mappings, quality checks
16:30-17:00  Update statuses, plan tomorrow
```

**Daily checklist:**
```
□ Process at least 1 video through Phase 1
□ Complete extraction for 1 video
□ Review and integrate entities from gap analysis
□ Update all video statuses
□ Note any blockers or questions
□ Maintain quality score ≥ 0.90
```

### Team Leads

**Daily focus:** Queue management, quality control, team support

**Typical day:**
```
09:00-10:00  Morning operations (queue review, assignments)
10:00-11:00  Quality control reviews
11:00-12:00  Team support (unblock issues, answer questions)
12:00-13:00  Strategic work (planning, improvements)
13:00-14:00  Lunch / Break
14:00-15:00  Process videos (lead by example)
15:00-16:00  Afternoon quality checks
16:00-17:00  End-of-day procedures, reporting
```

**Daily checklist:**
```
□ Review and update video queue
□ Complete quality reviews for "Review" status items
□ Unblock any team members with issues
□ Assign new videos to team
□ Monitor automation scripts
□ Generate daily status report
□ Update stakeholders on progress
```

### Quality Reviewers

**Daily focus:** Quality assurance, validation, feedback

**Typical day:**
```
09:00-10:00  Morning quality checks
10:00-12:00  Detailed review of completed research
12:00-13:00  Provide feedback to team members
13:00-14:00  Lunch / Break
14:00-15:30  Review in-progress work for quality
15:30-16:30  Update quality metrics and reports
16:30-17:00  Plan tomorrow's review priorities
```

**Daily checklist:**
```
□ Review all items in "Review" status
□ Approve or request revisions
□ Maintain approval rate > 80%
□ Provide constructive feedback
□ Update quality dashboard
□ Identify quality trends
□ Suggest process improvements
```

---

## Monitoring & Alerts

### System Health Monitoring

**Check every 2 hours:**
```bash
# Quick health check
python scripts/health_check.py

# Monitors:
- CSV file accessibility
- Automation script status
- Disk space availability
- Backup status
- Error logs
```

**Alert thresholds:**
- ⚠️ Warning: Quality score < 0.85 for any research
- ⚠️ Warning: Video in progress > 5 days
- 🚨 Critical: Automation script failed
- 🚨 Critical: Backup failed
- 🚨 Critical: Data corruption detected

### Performance Monitoring

**Track daily:**
```bash
# Performance metrics
python scripts/track_performance.py

# Metrics:
- Videos processed per day (target: 2-3)
- Average processing time (target: 4-6 hours)
- Quality score average (target: ≥0.90)
- Automation success rate (target: ≥95%)
```

**Weekly trends:**
```bash
# Generate trend report
python scripts/analyze_trends.py

# Identifies:
- Processing time trends (improving/worsening)
- Quality score trends
- Bottleneck phases
- Team productivity trends
```

### Manual Monitoring Checklist

**Check daily:**
```
□ All automation scripts completed successfully
□ No videos stuck in same status > 3 days
□ Quality scores meeting targets
□ No data integrity issues
□ Backups completing daily
□ Team members not blocked
```

**Check weekly:**
```
□ Archive growing appropriately
□ LIBRARIES entities increasing
□ No duplicate IDs in system
□ Documentation up to date
□ Prompts still effective
□ Scripts performing well
```

---

## Quick Command Reference

**Most-used daily commands:**

```bash
# Morning startup
python scripts/generate_daily_status.py
python scripts/check_overdue_videos.py

# Video processing
python scripts/run_gap_analysis.py RSR-XXX
python scripts/validate_integration.py RSR-XXX
python scripts/run_mapping.py RSR-XXX

# Quality checks
python scripts/list_review_items.py
python scripts/check_wip_quality.py

# End of day
python scripts/generate_eod_report.py
python scripts/verify_backup.py

# Weekly operations
python scripts/generate_weekly_report.py
python scripts/weekly_archive.py
python scripts/weekly_quality_review.py
```

---

## Emergency Procedures

### If Automation Scripts Fail

```bash
# Step 1: Check error logs
cat scripts/logs/automation.log | tail -50

# Step 2: Identify failed script
# Find last error message

# Step 3: Run manual workaround
# See 04_TROUBLESHOOTING_GUIDE.md for specific solutions

# Step 4: Notify team lead
# Document issue for follow-up
```

### If Data Corruption Detected

```bash
# Step 1: STOP all work immediately
# Do not make any changes

# Step 2: Restore from backup
python scripts/restore_from_backup.py YYYY-MM-DD

# Step 3: Verify restoration
python scripts/verify_data_integrity.py

# Step 4: Resume work only after verification
```

### If Quality Scores Drop Below 0.80

```bash
# Step 1: Identify affected research
python scripts/find_low_quality.py

# Step 2: Review and identify root cause
# Check: Which phase has issues?
# Check: Is it systematic or isolated?

# Step 3: Rework affected items
# Assign for revision

# Step 4: Update processes to prevent recurrence
```

---

## Tips for Efficiency

### Time-Saving Shortcuts

**Use templates:**
- Copy previous research folders as starting point
- Use prompt templates from 08_PROMPTS_REFERENCE.md
- Reuse JSON structures from similar entities

**Automation:**
- Let scripts handle repetitive tasks
- Schedule automation during lunch/breaks
- Review automated results rather than doing manually

**Batch processing:**
- Transcribe multiple videos in one session
- Extract entities from 2-3 videos consecutively
- Review multiple quality checks together

### Productivity Tips

**Focus blocks:**
- Morning: Deep work (extraction, integration)
- Afternoon: Reviews and quality checks
- Avoid switching between phases too frequently

**Quality first:**
- Better to complete 1 video well than 3 poorly
- Take time to verify each phase
- Don't skip quality checks to save time

**Communication:**
- Update status immediately when blocked
- Ask questions early, don't waste time stuck
- Share learnings with team

---

## Related Documentation

**For step-by-step workflows:**
- [01_STEP_BY_STEP_WORKFLOWS.md](01_STEP_BY_STEP_WORKFLOWS.md) - Detailed phase workflows

**For troubleshooting:**
- [04_TROUBLESHOOTING_GUIDE.md](04_TROUBLESHOOTING_GUIDE.md) - Quick solutions

**For quick reference:**
- [05_QUICK_REFERENCE.md](05_QUICK_REFERENCE.md) - Command cheatsheets

**For best practices:**
- [03_BEST_PRACTICES.md](03_BEST_PRACTICES.md) - Optimization tips

**For technical details:**
- [../v1/README.md](../v1/README.md) - Complete technical reference

---

**Last Updated:** 2025-12-04
**Version:** 2.0
**Maintained By:** RESEARCHES 2 Team
