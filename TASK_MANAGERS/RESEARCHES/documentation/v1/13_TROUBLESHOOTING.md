# 13_TROUBLESHOOTING.md

**Common Issues & Solutions**
**Location:** `documentation/v1/`
**Last Updated:** 2025-12-04
**Status:** ✅ Production Ready

---

## Table of Contents

1. [Overview](#overview)
2. [Phase 0: Search Queue Issues](#phase-0-search-queue-issues)
3. [Phase 0→1: Video Queue Issues](#phase-01-video-queue-issues)
4. [Phase 1: Transcription Issues](#phase-1-transcription-issues)
5. [Phase 2-3-5: Analysis Issues](#phase-2-3-5-analysis-issues)
6. [Phase 4: Integration Issues](#phase-4-integration-issues)
7. [Script Execution Issues](#script-execution-issues)
8. [Data File Issues](#data-file-issues)
9. [Report Generation Issues](#report-generation-issues)
10. [General System Issues](#general-system-issues)

---

## Overview

This document consolidates troubleshooting guidance from all documentation files into one comprehensive reference. Issues are organized by phase and category for quick lookup.

### Quick Diagnostic Questions

**Before troubleshooting, ask:**
1. Which phase are you in? (0, 0→1, 1, 2, 3, 4, 5)
2. What were you trying to do?
3. What command did you run? (exact command)
4. What error message did you get? (exact text)
5. What files are involved? (paths)

### Common Error Patterns

**File Not Found Errors:**
- Check file paths (absolute vs relative)
- Verify file exists: `ls path/to/file`
- Check current directory: `pwd`

**Permission Errors:**
- Check file permissions: `ls -la path/to/file`
- Run with appropriate permissions
- Check directory write access

**CSV/JSON Errors:**
- Validate syntax (commas, quotes, brackets)
- Check encoding (UTF-8)
- Verify field names match expected

**Script Errors:**
- Check Python version: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Run with debug flag: `--debug` or `--verbose`

---

## Phase 0: Search Queue Issues

### Problem 1: Search_Queue_Master.csv Not Found

**Symptom:**
```bash
python 00_SEARCH_QUEUE/scripts/assign_search.py Employee DEV "Topic"
FileNotFoundError: Search_Queue_Master.csv not found
```

**Cause:** CSV file doesn't exist yet

**Solution:**
```bash
# CSV is auto-created on first run
# Run script once to create it:
python 00_SEARCH_QUEUE/scripts/assign_search.py "John Doe" DEV "Claude AI tutorials" "claude tutorial" "Focus on 2024-2025"

# Verify created:
ls 00_SEARCH_QUEUE/Search_Queue_Master.csv

# Output should show:
# Search_Queue_Master.csv
```

**Prevention:** First script run auto-creates CSV with headers

---

### Problem 2: Search Status Not Updating

**Symptom:** Status remains "Assigned" after completion

**Cause:** Forgot to run complete_search.py

**Solution:**
```bash
# Complete the search assignment
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 20

# This updates:
# - Status: "Assigned" → "Completed"
# - Videos_Found: 0 → 20
# - Date_Completed: (current date)

# Verify update:
cat 00_SEARCH_QUEUE/Search_Queue_Master.csv | grep SEARCH-001
```

**Prevention:** Always run complete_search.py when search is done

---

### Problem 3: Duplicate Search_ID

**Symptom:**
```
Error: SEARCH-001 already exists
```

**Cause:** Trying to create duplicate ID

**Solution:**
```bash
# Check existing IDs
cat 00_SEARCH_QUEUE/Search_Queue_Master.csv

# Script auto-generates next ID
# If manual creation, use next available number:
# SEARCH-001, SEARCH-002, SEARCH-003, etc.

# Let script handle ID generation (recommended)
```

**Prevention:** Use scripts (auto-generate IDs), don't create manually

---

## Phase 0→1: Video Queue Issues

### Problem 4: Queue CSV Not Found

**Symptom:**
```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py "URL" "Name" "Topic" "Source"
FileNotFoundError: Video_Queue_Master.csv not found
```

**Cause:** CSV doesn't exist

**Solution:**
```bash
# Run script once to auto-create CSV
python 01_VIDEO_QUEUE/scripts/add_video_to_queue_simple.py \
    "https://youtube.com/watch?v=dQw4w9WgXcQ" \
    "Niko Kar" \
    "AI Tools" \
    "Perplexity" \
    "Test video"

# Verify created:
ls 01_VIDEO_QUEUE/Video_Queue_Master.csv
```

**Prevention:** First run auto-creates CSV

---

### Problem 5: Priority Score is 0

**Symptom:** All videos show `Priority_Score: 0.0`

**Cause:** Missing metadata (views, likes, publish_date)

**Solution:**
```bash
# Manually update CSV with metadata:
# 1. Open Video_Queue_Master.csv in editor
# 2. Find row with Queue_ID
# 3. Update Views, Likes, Publish_Date columns
# 4. Save CSV

# Example row:
# VQ-001,dQw4w9WgXcQ,...,1500000,45000,2300,2025-10-15,...

# Re-calculate priority:
python 01_VIDEO_QUEUE/scripts/calculate_priority.py 1500000 45000 2025-10-15

# Output will show calculated score (e.g., 75.5)
# Manually update Priority_Score column in CSV
```

**Prevention:** Add metadata when adding video (use full script, not simple)

---

### Problem 6: Can't Extract Video ID

**Symptom:**
```
❌ Error: Could not extract video ID from URL: [url]
```

**Cause:** Unsupported URL format

**Solution:**
```bash
# Use standard YouTube URL format:
# ✅ Correct: https://www.youtube.com/watch?v=VIDEO_ID
# ✅ Correct: https://youtu.be/VIDEO_ID
# ❌ Incorrect: https://youtube.com/c/CHANNEL/videos

# Copy URL from browser address bar when watching video
# Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ
#                                          ^^^^^^^^^^^
#                                          Video ID (11 chars)

# Retry with correct URL
```

**Prevention:** Always use video URL (not channel URL)

---

### Problem 7: Dashboard Not Loading

**Symptom:** Video_Queue_Dashboard.html opens but blank/no videos

**Solutions:**

**A) File Location**
```bash
# Ensure dashboard in same directory as CSV
ls 01_VIDEO_QUEUE/
# Should show both:
#   Video_Queue_Master.csv
#   Video_Queue_Dashboard.html
```

**B) Serve via Web Server**
```bash
cd 01_VIDEO_QUEUE
python -m http.server 8000

# Open browser: http://localhost:8000/Video_Queue_Dashboard.html
```

**C) Check CSV Format**
```bash
# Verify CSV has data
cat 01_VIDEO_QUEUE/Video_Queue_Master.csv

# Should show header + data rows
```

**Prevention:** Keep dashboard in same folder as CSV

---

## Phase 1: Transcription Issues

### Problem 8: Video File Too Large for AI

**Symptom:** AI transcript tool fails with "file too large" error

**Cause:** Video > 100MB or > 40 minutes

**Solution:**
```bash
# Use TurboScribe for large videos (instead of Google AI Studio)
# TurboScribe handles up to 10 hours

# Or split video into segments:
# 1. Use video editing tool to split
# 2. Transcribe each segment separately
# 3. Combine transcripts manually
```

**Prevention:** Check video duration/size before transcription

---

### Problem 9: Transcription Quality Poor

**Symptom:** Transcript has many [inaudible], missing words

**Cause:** Poor audio quality, heavy accent, background noise

**Solution:**
```bash
# Try different transcription tool:
# 1. Google AI Studio (good for clear audio)
# 2. TurboScribe (good for long videos)
# 3. Whisper API (good for accents)

# Manual correction:
# 1. Watch video while reading transcript
# 2. Fix obvious errors
# 3. Mark unclear sections: [unclear: approximate words]

# Quality check:
# - Must be understandable
# - Entity extraction must be possible (≥37 entities)
```

**Prevention:** Choose high-quality audio videos for transcription

---

### Problem 10: Entity Count < 37

**Symptom:** Transcription complete but only 25 entities extracted

**Cause:** Video not comprehensive enough, or extraction incomplete

**Solution:**
```bash
# Re-extract entities more carefully:
# 1. Re-read transcript looking for:
#    - Tools mentioned (even briefly)
#    - Workflow steps described
#    - Objects created/used
#    - Actions performed (verbs)
#    - Skills demonstrated
# 2. Update entity counts

# If still < 37:
# - Video may not be suitable (too simple)
# - Consider rejecting video (mark as low priority)
# - Or accept with note: "Limited entity video"

# Quality levels:
# Minimum: 37 entities (required)
# Good: 50+ entities
# Excellent: 70+ entities
```

**Prevention:** Select comprehensive tutorial videos (not quick tips)

---

## Phase 2-3-5: Analysis Issues

### Problem 11: Gap Analyzer Script Fails

**Symptom:**
```bash
python scripts/video_gap_analyzer.py Video_024
FileNotFoundError: Video_024.md not found
```

**Cause:** Phase 1 transcription not complete

**Solution:**
```bash
# Verify transcription exists
ls 02_TRANSCRIPTIONS/Video_024.md

# If missing, complete Phase 1 first:
# 1. Transcribe video
# 2. Extract entities (≥37)
# 3. Save as Video_024.md

# Then retry gap analysis:
python scripts/video_gap_analyzer.py Video_024
```

**Prevention:** Complete Phase 1 before Phase 3

---

### Problem 12: Missing Extraction Files

**Symptom:**
```
No Phase 3 analysis file found for Video_024
```

**Cause:** Phase 2 extraction not completed

**Solution:**
```bash
# Complete Phase 2 extraction:
# 1. Create Video_024_Phase3_Analysis.md (Tools & Workflows)
# 2. Create Video_024_Phase4_Objects.md (Objects inventory)

# See templates in:
# 06_ANALYSIS_COMPLETE.md (Phase 2 section)

# Then retry gap analyzer or mapping reporter
```

**Prevention:** Follow phase sequence (1→2→3→4→5)

---

### Problem 13: Low Quality Score

**Symptom:**
```
Quality score: 0.62 (below minimum 0.75)
```

**Cause:** Incomplete entity relationships

**Diagnosis:**
```bash
# Run validation check
python scripts/analyze_video_phases.py Video_024 --validate

# Common issues:
# - Actions without objects (orphaned actions)
# - Tools not mapped to tasks (unused tools)
# - Orphaned milestones (no workflow parent)
```

**Solution:**
```bash
# Fix relationships:
# 1. Map all actions to objects
# 2. Link all tools to tasks
# 3. Ensure milestone→task→step hierarchy

# Update files:
# - Video_024_Phase4_Objects.md (add Action→Object links)
# - Video_024_Phase3_Analysis.md (add Tool→Task links)

# Re-run integration reporter:
python scripts/video_integration_reporter.py Video_024

# Verify quality score ≥0.75
```

**Prevention:** Complete all relationships during extraction

---

### Problem 14: Integration Reporter Empty

**Symptom:**
```
Integration report generated but shows 0 entities
```

**Cause:** Can't find transcription or analysis files

**Solution:**
```bash
# Verify all required files exist:
ls 02_TRANSCRIPTIONS/Video_024.md
ls 03_ANALYSIS/Extractions/Video_024_Phase3_Analysis.md
ls 03_ANALYSIS/Extractions/Video_024_Phase4_Objects.md
ls 03_ANALYSIS/Gap_Analysis/Video_024_Gap_Analysis.md

# If any missing, complete that phase first
# Then re-run integration reporter:
python scripts/video_integration_reporter.py Video_024
```

**Prevention:** Check prerequisites before running reporter

---

## Phase 4: Integration Issues

### Problem 15: video_json_updater.py Fails

**Symptom:**
```bash
python scripts/video_json_updater.py Video_024
FileNotFoundError: Gap analysis not found
```

**Cause:** Phase 3 not complete

**Solution:**
```bash
# Verify gap analysis exists
ls 03_ANALYSIS/Gap_Analysis/Video_024_Gap_Analysis.md

# If missing, run gap analyzer:
python scripts/video_gap_analyzer.py Video_024

# Then retry integration:
python scripts/video_json_updater.py Video_024
```

**Prevention:** Complete Phase 3 before Phase 4

---

### Problem 16: JSON Syntax Error

**Symptom:**
```bash
python -m json.tool TOL-SEC-124.json
Expecting ',' delimiter: line 42 column 5
```

**Cause:** Invalid JSON (missing comma, trailing comma, unquoted key)

**Solution:**
```bash
# Common JSON errors:
# 1. Trailing comma: {"key": "value",} → {"key": "value"}
# 2. Missing comma: {"key1": "value1" "key2": "value2"} → {"key1": "value1", "key2": "value2"}
# 3. Unquoted keys: {key: "value"} → {"key": "value"}
# 4. Single quotes: {'key': 'value'} → {"key": "value"}

# Fix manually or use JSON formatter:
cat TOL-SEC-124.json | jq '.' > temp.json
mv temp.json TOL-SEC-124.json

# Verify valid:
python -m json.tool TOL-SEC-124.json > /dev/null
echo "✓ Valid JSON"
```

**Prevention:** Use JSON editor with syntax highlighting

---

### Problem 17: Broken Cross-Reference

**Symptom:**
```bash
python scripts/verify_manual_integration.py Video_024
❌ TSK-005 → TOL-SEC-999 (TOL-SEC-999 doesn't exist)
```

**Cause:** Referenced entity doesn't exist (typo or wrong ID)

**Solution:**
```bash
# Find correct ID:
grep -r "ScaleKit" LIBRARIES/LBS_003_Tools/Auth/

# Should show: TOL-SEC-124 (not TOL-SEC-999)

# Fix reference in TSK-005.json:
# Change "TOL-SEC-999" to "TOL-SEC-124"

# Re-run verification:
python scripts/verify_manual_integration.py Video_024
```

**Prevention:** Use gap analyzer's recommended IDs (not manual guessing)

---

### Problem 18: Duplicate ID

**Symptom:**
```bash
python scripts/check_duplicate_ids.py
❌ Duplicate ID: TOL-SEC-124
  - LIBRARIES/LBS_003_Tools/Auth/TOL-SEC-124_ScaleKit_Dashboard.json
  - LIBRARIES/LBS_003_Tools/Auth/TOL-SEC-124_ScaleKit_SDK.json
```

**Cause:** Two files with same ID (copy-paste error)

**Solution:**
```bash
# Get next available ID:
python scripts/video_id_scanner.py --category tools

# Next available: TOL-SEC-125

# Rename second file:
mv LIBRARIES/LBS_003_Tools/Auth/TOL-SEC-124_ScaleKit_SDK.json \
   LIBRARIES/LBS_003_Tools/Auth/TOL-SEC-125_ScaleKit_SDK.json

# Update ID inside file:
# Open TOL-SEC-125_ScaleKit_SDK.json
# Change "tool_id": "TOL-SEC-124" to "TOL-SEC-125"

# Re-run check:
python scripts/check_duplicate_ids.py
```

**Prevention:** Use script-generated IDs (don't copy-paste)

---

### Problem 19: Backup Restore Needed

**Symptom:** Incorrect integration, need to rollback

**Solution:**
```bash
# List backups:
ls -la LIBRARIES/Archive/Backups/

# Identify correct backup date:
# Example: 2025-12-04 (before incorrect integration)

# Restore specific files:
cp LIBRARIES/Archive/Backups/2025-12-04/LBS_003_Tools/Auth/*.json \
   LIBRARIES/LBS_003_Tools/Auth/

# Or restore entire directory:
rm -rf LIBRARIES/LBS_003_Tools/Auth
cp -r LIBRARIES/Archive/Backups/2025-12-04/LBS_003_Tools/Auth \
      LIBRARIES/LBS_003_Tools/

# Verify restore:
ls LIBRARIES/LBS_003_Tools/Auth/

# Re-run integration correctly:
python scripts/video_json_updater.py Video_024
```

**Prevention:** Always verify dry-run before live integration

---

## Script Execution Issues

### Problem 20: Python Version Mismatch

**Symptom:**
```bash
python scripts/video_gap_analyzer.py Video_024
SyntaxError: invalid syntax (f-string)
```

**Cause:** Python version too old (< 3.6)

**Solution:**
```bash
# Check Python version:
python --version

# Should be: Python 3.8+ (recommended)
# Minimum: Python 3.6

# If too old, upgrade:
# Windows: Download from python.org
# Mac: brew install python3
# Linux: sudo apt-get install python3.8

# Use python3 explicitly:
python3 scripts/video_gap_analyzer.py Video_024
```

**Prevention:** Use Python 3.8+ for all scripts

---

### Problem 21: Missing Dependencies

**Symptom:**
```bash
python scripts/video_gap_analyzer.py Video_024
ModuleNotFoundError: No module named 'pandas'
```

**Cause:** Required Python packages not installed

**Solution:**
```bash
# Install required packages:
pip install pandas
pip install pathlib
pip install datetime

# Or install from requirements file (if exists):
pip install -r requirements.txt

# Verify installation:
python -c "import pandas; print(pandas.__version__)"
```

**Prevention:** Install dependencies before first script run

---

### Problem 22: Script Permission Denied

**Symptom:**
```bash
python scripts/video_gap_analyzer.py Video_024
PermissionError: [Errno 13] Permission denied
```

**Cause:** No write permission to output directory

**Solution:**
```bash
# Check permissions:
ls -la 03_ANALYSIS/Gap_Analysis/

# Fix permissions:
chmod u+w 03_ANALYSIS/Gap_Analysis/

# Or run with sudo (Linux/Mac):
sudo python scripts/video_gap_analyzer.py Video_024

# Windows: Run terminal as Administrator
```

**Prevention:** Ensure write permissions to output directories

---

### Problem 23: Script Hangs/Freezes

**Symptom:** Script runs but never completes, no output

**Cause:** Infinite loop, network timeout, or large dataset

**Solution:**
```bash
# Kill script: Ctrl+C

# Run with debug output:
python scripts/video_gap_analyzer.py Video_024 --debug

# Or with timeout:
timeout 300 python scripts/video_gap_analyzer.py Video_024
# (kills after 300 seconds / 5 minutes)

# Check for:
# - Network issues (if fetching data)
# - Large CSV files (slow processing)
# - Infinite loops (bug in script)
```

**Prevention:** Run with --debug for visibility

---

## Data File Issues

### Problem 24: CSV Won't Open in Excel

**Symptom:** CSV opens with garbled characters or wrong encoding

**Solution:**
```bash
# Convert to UTF-8 with BOM for Excel:
# Python:
import pandas as pd
df = pd.read_csv('file.csv', encoding='utf-8')
df.to_csv('file_excel.csv', index=False, encoding='utf-8-sig')

# Or use Excel import wizard:
# 1. Open Excel
# 2. Data → From Text/CSV
# 3. Select file
# 4. Choose UTF-8 encoding
# 5. Import
```

**Prevention:** Use UTF-8 encoding for all CSV files

---

### Problem 25: CSV Field Mismatch

**Symptom:** Script expects "Queue_ID" but CSV has "QueueID"

**Solution:**
```bash
# Check actual field names:
head -n 1 Video_Queue_Master.csv

# Either:
# 1. Fix CSV header to match expected names
# 2. Or update script to use actual names

# Expected field names:
# Search Queue: Search_ID, Employee, Department, Topic, Status
# Video Queue: Queue_ID, Video_ID, Video_Title, Status, Priority_Score
```

**Prevention:** Use script-generated CSVs (correct headers)

---

### Problem 26: Duplicate IDs in CSV

**Symptom:** Two rows with same Queue_ID or Search_ID

**Solution:**
```bash
# Find duplicates:
import pandas as pd
df = pd.read_csv('Video_Queue_Master.csv')
duplicates = df[df.duplicated('Queue_ID', keep=False)]
print(duplicates)

# Fix: Update duplicate IDs to next available
# Use video_id_scanner.py to get next ID:
python scripts/video_id_scanner.py --category queue

# Update CSV with unique IDs
```

**Prevention:** Use scripts (auto-generate unique IDs)

---

## Report Generation Issues

### Problem 27: Report Not Generated

**Symptom:**
```bash
python scripts/video_gap_analyzer.py Video_024
# No output file created
```

**Cause:** Script error or missing prerequisites

**Solution:**
```bash
# Run with debug:
python scripts/video_gap_analyzer.py Video_024 --debug

# Check prerequisites:
ls 02_TRANSCRIPTIONS/Video_024.md
ls LIBRARIES/LBS_003_Tools/

# Common issues:
# 1. Transcription missing (Phase 1 incomplete)
# 2. LIBRARIES path incorrect (check config.py)
# 3. Write permissions (check directory access)

# Run with verbose output:
python scripts/video_gap_analyzer.py Video_024 --verbose
```

**Prevention:** Verify prerequisites before running

---

### Problem 28: Report Metrics Incorrect

**Symptom:** Quality score shows 0.50 but should be higher

**Cause:** Missing cross-references or broken links

**Solution:**
```bash
# Re-run with validation:
python scripts/video_integration_reporter.py Video_024 --validate

# Check for broken references:
python scripts/verify_manual_integration.py Video_024

# Common issues:
# 1. Tools not linked to tasks
# 2. Actions not linked to objects
# 3. Workflow missing milestone references

# Fix broken links then re-generate report
```

**Prevention:** Complete all cross-references before reporting

---

### Problem 29: Progress Report Empty

**Symptom:**
```bash
python scripts/generate_progress_report.py
# Output: "No data available"
```

**Cause:** VIDEO_PROGRESS_TRACKER.csv missing

**Solution:**
```bash
# Check if tracker exists:
ls VIDEO_PROGRESS_TRACKER.csv

# Create tracker from transcriptions:
python scripts/update_video_progress.py --init

# Or manually create:
echo "Video_Number,Title,Status,Current_Phase,Employee" > VIDEO_PROGRESS_TRACKER.csv

# Then re-run:
python scripts/generate_progress_report.py
```

**Prevention:** Initialize progress tracker at project start

---

## General System Issues

### Problem 30: Path Not Found

**Symptom:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'RESEARCHES 2/scripts/...'
```

**Cause:** Wrong working directory or incorrect path

**Solution:**
```bash
# Check current directory:
pwd

# Should be in: .../ENTITIES/TASK_MANAGERS/RESEARCHES 2/

# If not, navigate to correct directory:
cd "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2"

# Or use absolute paths in commands:
python "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\scripts\video_gap_analyzer.py" Video_024

# Update config.py with correct base path if needed
```

**Prevention:** Always run scripts from RESEARCHES 2 root directory

---

### Problem 31: Config.py Path Issues

**Symptom:** Scripts can't find LIBRARIES or TRANSCRIPTIONS

**Cause:** Incorrect paths in config.py

**Solution:**
```bash
# Open config.py
# Check BASE_PATH:
BASE_PATH = Path(r"C:\Users\Dell\Dropbox\ENTITIES")

# Update to your actual Dropbox path:
# Windows: C:\Users\YourName\Dropbox\ENTITIES
# Mac: /Users/YourName/Dropbox/ENTITIES
# Linux: /home/YourName/Dropbox/ENTITIES

# Save and retry script
```

**Prevention:** Configure paths correctly at setup

---

### Problem 32: Large File Performance

**Symptom:** Scripts very slow with large CSV files (10,000+ rows)

**Solution:**
```bash
# Optimize CSV processing:
# 1. Use pandas (faster than csv module)
# 2. Read only needed columns
# 3. Use chunking for very large files

# Example:
import pandas as pd
df = pd.read_csv('large_file.csv', usecols=['Queue_ID', 'Status'])

# Or process in chunks:
for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    process(chunk)

# Archive old data:
# Move completed videos to archive CSV
```

**Prevention:** Archive old data periodically (quarterly)

---

### Problem 33: Disk Space Full

**Symptom:**
```
OSError: [Errno 28] No space left on device
```

**Cause:** Disk full from large video files or backups

**Solution:**
```bash
# Check disk space:
df -h

# Find large files:
du -h --max-depth=1 | sort -hr | head -20

# Clean up:
# 1. Delete old backups (>30 days)
rm -rf LIBRARIES/Archive/Backups/2025-10-*

# 2. Delete downloaded videos (keep transcriptions)
rm 02_TRANSCRIPTIONS/*.mp4

# 3. Archive old reports (compress)
tar -czf reports_2025-11.tar.gz 03_ANALYSIS/
rm -rf 03_ANALYSIS/2025-11/
```

**Prevention:**
- Delete video files after transcription
- Archive old backups monthly
- Compress old reports

---

### Problem 34: Git Merge Conflicts

**Symptom:** Git merge conflicts in CSV or JSON files

**Solution:**
```bash
# Check conflict files:
git status

# For CSV files:
# 1. Accept one version (ours or theirs)
git checkout --ours Video_Queue_Master.csv
# or
git checkout --theirs Video_Queue_Master.csv

# 2. Manually merge unique rows if needed

# For JSON files:
# 1. Use JSON merge tool
# 2. Or manually resolve conflicts
# 3. Validate JSON syntax after merge:
python -m json.tool file.json > /dev/null

# Complete merge:
git add resolved_files
git commit -m "Resolved merge conflicts"
```

**Prevention:**
- Coordinate changes (avoid concurrent edits)
- Use branches for major changes
- Pull before pushing

---

## Quick Reference: Common Commands

### Diagnostic Commands
```bash
# Check file exists
ls path/to/file

# Check current directory
pwd

# Check Python version
python --version

# Check disk space
df -h

# Check file permissions
ls -la path/to/file

# Validate JSON
python -m json.tool file.json

# Check CSV headers
head -n 1 file.csv
```

### Fix Commands
```bash
# Change permissions
chmod u+w path/to/file

# Create directory
mkdir -p path/to/directory

# Copy file
cp source.csv backup.csv

# Remove file
rm file.txt

# Navigate directory
cd path/to/directory

# Install Python package
pip install package_name
```

### Script Commands
```bash
# Run with debug
python script.py --debug

# Run with verbose
python script.py --verbose

# Run with timeout
timeout 300 python script.py

# Check script syntax
python -m py_compile script.py
```

---

## Getting Help

### Documentation References

**Phase-Specific:**
- Phase 0: [03_SEARCH_QUEUE_COMPLETE.md](03_SEARCH_QUEUE_COMPLETE.md#troubleshooting)
- Phase 0→1: [04_VIDEO_QUEUE_COMPLETE.md](04_VIDEO_QUEUE_COMPLETE.md#troubleshooting)
- Phase 1: [05_TRANSCRIPTIONS_COMPLETE.md](05_TRANSCRIPTIONS_COMPLETE.md#troubleshooting)
- Phase 2-3-5: [06_ANALYSIS_COMPLETE.md](06_ANALYSIS_COMPLETE.md#troubleshooting)
- Phase 4: [07_INTEGRATION_COMPLETE.md](07_INTEGRATION_COMPLETE.md#troubleshooting)

**Topic-Specific:**
- Scripts: [08_SCRIPTS_DETAILED.md](08_SCRIPTS_DETAILED.md)
- Data Files: [10_DATA_FILES.md](10_DATA_FILES.md#troubleshooting)
- Reports: [11_REPORTS_ARCHIVE.md](11_REPORTS_ARCHIVE.md#troubleshooting)

**Overview:**
- Master Index: [00_MASTER_INDEX.md](00_MASTER_INDEX.md)
- Quick Start: [12_QUICK_START.md](12_QUICK_START.md)

---

### Support Channels

**Internal Support:**
1. Check this documentation first
2. Review phase-specific troubleshooting
3. Search existing issues in documentation
4. Ask team members

**External Resources:**
- Python documentation: https://docs.python.org
- Pandas documentation: https://pandas.pydata.org/docs/
- JSON validator: https://jsonlint.com
- CSV validator: https://csvlint.io

---

## Version History

- **v1.0** (2025-12-04): Initial troubleshooting guide
  - 34 common problems documented
  - Organized by phase and category
  - Quick reference commands added
  - Support channels listed

---

**Created:** 2025-12-04
**Last Updated:** 2025-12-04
**Status:** ✅ Complete
**Maintainer:** AI Department
**Problems Documented:** 34
