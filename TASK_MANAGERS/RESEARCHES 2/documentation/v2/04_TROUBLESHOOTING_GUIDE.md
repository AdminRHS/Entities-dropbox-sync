# RESEARCHES 2 - Troubleshooting Guide

**Version:** 2.0
**Generated:** 2025-12-04
**Purpose:** Quick solutions to common problems
**Audience:** All users encountering issues

---

## 📖 Table of Contents

1. [Quick Diagnostic Guide](#quick-diagnostic-guide)
2. [Phase 0: Search Problems](#phase-0-search-problems)
3. [Phase 0→1: Queue Problems](#phase-01-queue-problems)
4. [Phase 1: Transcription Problems](#phase-1-transcription-problems)
5. [Phase 2: Extraction Problems](#phase-2-extraction-problems)
6. [Phase 3: Gap Analysis Problems](#phase-3-gap-analysis-problems)
7. [Phase 4: Integration Problems](#phase-4-integration-problems)
8. [Phase 5: Mapping Problems](#phase-5-mapping-problems)
9. [Script and Automation Problems](#script-and-automation-problems)
10. [Data and File Problems](#data-and-file-problems)
11. [Quality and Validation Problems](#quality-and-validation-problems)
12. [System and Performance Problems](#system-and-performance-problems)

---

## Quick Diagnostic Guide

### Problem Identification Flow

```
Start here → What went wrong?

├─ Can't find files/folders
│  └─ See: Data and File Problems
│
├─ Script failed/error message
│  └─ See: Script and Automation Problems
│
├─ Quality score too low
│  └─ See: Quality and Validation Problems
│
├─ Phase-specific issue
│  ├─ Phase 0: Search Problems
│  ├─ Phase 0→1: Queue Problems
│  ├─ Phase 1: Transcription Problems
│  ├─ Phase 2: Extraction Problems
│  ├─ Phase 3: Gap Analysis Problems
│  ├─ Phase 4: Integration Problems
│  └─ Phase 5: Mapping Problems
│
└─ System slow/crashing
   └─ See: System and Performance Problems
```

### Emergency Quick Fixes

**If completely stuck:**
```bash
# 1. Check if files exist
dir "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2"

# 2. Verify Python working
python --version

# 3. Check recent backups exist
dir 07_ARCHIVE\backups

# 4. Contact team lead with:
#    - What you were doing
#    - Error message (exact text)
#    - RSR/VQ ID involved
#    - What you already tried
```

**If data might be corrupted:**
```bash
# STOP working immediately
# DO NOT save any files
# DO NOT run any scripts
# Contact team lead for backup restoration
```

---

## Phase 0: Search Problems

### Problem: Can't find relevant videos

**Symptoms:**
- Search returns no results
- Results not matching topic
- Videos too old or low quality

**Diagnosis:**
```
Check:
□ Search query too specific?
□ Using right search tool?
□ Date filters too restrictive?
□ Topic actually exists on YouTube?
```

**Solutions:**

**Solution 1: Broaden search query**
```
❌ Too specific: "Claude AI API integration with Next.js 14 using TypeScript 2025"
✅ Better: "Claude AI API tutorial Next.js"
✅ Even better: "Claude AI integration tutorial"
```

**Solution 2: Try different search tools**
```
1. Start with Perplexity AI (best for recent videos)
2. Try ChatGPT with browsing (good for analysis)
3. Fall back to YouTube direct search
4. Use Google as last resort
```

**Solution 3: Adjust date filters**
```
Instead of: "Last 30 days only"
Try: "Last 90 days"
Or: "Last 6 months"
```

**Solution 4: Search related topics**
```
If can't find: "Cursor IDE pair programming"
Try instead: "AI code editor pair programming"
Or: "Cursor IDE tutorial"
Or: "AI coding assistant"
```

### Problem: Videos found but all low quality

**Symptoms:**
- Short videos (< 5 minutes)
- No practical demos
- Poor production quality
- Outdated information

**Solutions:**

**Solution 1: Adjust quality filters**
```
YouTube search filters:
- Duration: > 10 minutes
- Upload date: Last 3 months
- Sort by: View count or Rating
```

**Solution 2: Target specific channels**
```
Find reliable channels in topic area:
1. Check who uploaded best video so far
2. Search their channel for more content
3. Note their channel for future searches
```

**Solution 3: Expand topic scope**
```
If "Figma AI plugins" yields poor results:
Try broader: "Figma plugins" + manual filter for AI
Try related: "Design automation tools"
```

### Problem: Search results all duplicates

**Symptoms:**
- Videos cover same content
- Same channels/creators
- No new information

**Solutions:**

**Solution 1: Check Video Queue first**
```bash
# Search queue for existing videos on topic
findstr /i "keyword" Video_Queue_Master.csv

# If many exist, choose different angle
```

**Solution 2: Search different aspect**
```
If "React hooks" overrepresented:
Try: "React custom hooks patterns"
Or: "React hooks advanced techniques"
Or: "React hooks common mistakes"
```

**Solution 3: Different platform/format**
```
Consider:
- Course platforms (Udemy, Coursera)
- Conference talks
- Live coding streams
- Documentation tutorials
```

---

## Phase 0→1: Queue Problems

### Problem: Video Queue CSV won't open

**Symptoms:**
- Excel says file corrupted
- Can't find Video_Queue_Master.csv
- Permission denied error

**Solutions:**

**Solution 1: Check file location**
```bash
# Verify file exists
dir "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\01_QUEUE_ASSIGNMENTS\Video_Queue_Master.csv"

# If not found, check Dropbox sync status
```

**Solution 2: File might be open elsewhere**
```
1. Close all Excel/CSV programs
2. Check if colleague has file open
3. Wait 2-3 minutes for Dropbox sync
4. Try opening again
```

**Solution 3: Restore from backup**
```bash
# Copy from latest backup
copy "07_ARCHIVE\backups\YYYY-MM-DD\Video_Queue_Master.csv" "01_QUEUE_ASSIGNMENTS\"

# Verify restoration
python scripts/verify_data_integrity.py
```

### Problem: Can't assign video to employee

**Symptoms:**
- Script fails with error
- Employee name not recognized
- Video already assigned

**Solutions:**

**Solution 1: Check employee name spelling**
```bash
# List valid employee names
python scripts/list_employees.py

# Use exact name from list
python scripts/assign_video.py VQ-120 "John Doe"
```

**Solution 2: Video already assigned**
```bash
# Check current assignment
findstr "VQ-120" Video_Queue_Master.csv

# If assigned, reassign instead
python scripts/reassign_video.py VQ-120 "Jane Smith"
```

**Solution 3: Manual assignment**
```
1. Open Video_Queue_Master.csv
2. Find VQ-XXX row
3. Update fields:
   - Assigned_To: "Employee Name"
   - Status: "Assigned"
   - Date_Assigned: YYYY-MM-DD
4. Save file
```

### Problem: Priority score seems wrong

**Symptoms:**
- High-quality video has low priority
- Low-quality video has high priority
- Priority score = 0 or negative

**Solutions:**

**Solution 1: Recalculate priority**
```bash
# Refresh video metadata
python scripts/update_video_metadata.py VQ-120

# Recalculate priority score
python scripts/calculate_priority.py VQ-120

# Check updated score
findstr "VQ-120" Video_Queue_Master.csv
```

**Solution 2: Manual priority override**
```
1. Open Video_Queue_Master.csv
2. Find VQ-XXX row
3. Update Priority_Score: [0-100]
4. Add note: Priority_Override: "Reason for override"
5. Save file
```

**Solution 3: Understand priority algorithm**
```
Priority = (Views×30%) + (Likes×20%) + (Recency×30%) + (Engagement×20%)

Low priority might be correct if:
- Video is old (low recency score)
- Low view count
- Low engagement ratio

This doesn't mean bad video, just lower automatic priority.
```

---

## Phase 1: Transcription Problems

### Problem: AI won't transcribe video

**Symptoms:**
- Upload fails
- "File too large" error
- "Invalid format" error
- Transcription incomplete

**Solutions:**

**Solution 1: File size too large**
```
Check file size:
- Claude AI limit: 30 MB
- ChatGPT limit: 25 MB

If too large:
1. Use YouTube URL instead of file upload
2. Or compress video:
   - Use HandBrake or similar tool
   - Reduce resolution to 720p
   - Use h.264 codec
3. Or split video into parts
```

**Solution 2: Use URL instead of file**
```
Instead of uploading file:
1. Copy YouTube URL
2. Paste into Claude AI:
   "Please transcribe this YouTube video: [URL]"
3. AI will fetch and transcribe
```

**Solution 3: Try different AI platform**
```
If Claude AI fails:
1. Try ChatGPT (requires Plus subscription)
2. Try Google Gemini (different file limits)
3. Try specialized transcription service
```

**Solution 4: Transcription incomplete**
```
If AI stops mid-transcription:
1. Say "Please continue from where you stopped"
2. Copy partial transcription
3. Continue in new chat
4. Merge transcriptions manually
```

### Problem: Transcription has major errors

**Symptoms:**
- Tool names wrong ("Clawed" instead of "Claude")
- Missing sections
- Gibberish text
- Technical terms mangled

**Solutions:**

**Solution 1: Fix common errors manually**
```
Find and replace:
- "Clawed AI" → "Claude AI"
- "cursor idee" → "Cursor IDE"
- "figma" → "Figma"
- "git hub" → "GitHub"
- "J son" → "JSON"
- "react jess" → "React JS"
```

**Solution 2: Re-transcribe problematic sections**
```
1. Identify timestamp of error
2. Watch video section
3. Manually transcribe 1-2 paragraphs
4. Replace AI transcription in that section
```

**Solution 3: Use better audio quality**
```
If video audio poor:
1. Check if video has captions/subtitles
2. Download YouTube auto-captions:
   - Click CC button
   - Open transcript
   - Copy text
3. Clean up and format
```

### Problem: Can't save transcription

**Symptoms:**
- "Permission denied" error
- Folder not found
- File name too long

**Solutions:**

**Solution 1: Folder doesn't exist**
```bash
# Create research folder
mkdir "02_TRANSCRIPTIONS\RSR-XXX"

# Save transcription
copy transcript.txt "02_TRANSCRIPTIONS\RSR-XXX\RSR-XXX_transcript.md"
```

**Solution 2: Permission issue**
```
1. Check if file already open elsewhere
2. Close all programs using file
3. Wait for Dropbox sync to complete
4. Try saving again
```

**Solution 3: File name too long**
```
❌ Too long:
RSR-024_Full_Complete_Transcription_of_Video_About_Claude_AI_API_Integration.md

✅ Standard format:
RSR-024_transcript.md
```

---

## Phase 2: Extraction Problems

### Problem: Not enough entities extracted

**Symptoms:**
- Quality score low
- Warning: "Minimum entity counts not met"
- Gap analysis shows poor coverage

**Solutions:**

**Solution 1: Re-read transcription carefully**
```
Checklist:
□ Read entire transcription again
□ Highlight every tool mentioned
□ Note every workflow described
□ Identify all actions performed
□ Mark professions/roles mentioned
□ List skills demonstrated
□ Note departments/organizations
```

**Solution 2: Extract implied entities**
```
Don't just extract explicitly mentioned:

Video says: "I'm opening VS Code and installing the Claude extension"

Extract:
- Tool: "VS Code"
- Tool: "Claude extension for VS Code"
- Action: "Install editor extension"
- Skill: "IDE configuration"
- Profession: "Developer" (implied user)
```

**Solution 3: Use AI extraction then enhance**
```
1. Run AI extraction prompt
2. Review results
3. Add entities AI missed
4. Enhance descriptions
5. Check minimum counts met:
   - Workflows: ≥ 3
   - Tools: ≥ 5
   - Objects: ≥ 5
   - Actions: ≥ 8
   - Professions: ≥ 2
   - Skills: ≥ 5
   - Departments: ≥ 1
```

### Problem: Entity descriptions too vague

**Symptoms:**
- Quality reviewer requests more detail
- Can't distinguish from similar entities
- Descriptions < 10 words

**Solutions:**

**Solution 1: Enhance descriptions**
```
❌ Vague:
"Claude AI - AI tool"

✅ Detailed:
"Claude AI - Anthropic's large language model with 200K token context window, specialized in coding assistance, document analysis, and technical tasks. Features artifacts for shareable content and multi-modal input capabilities."

Add to descriptions:
- What it does specifically
- Key features or capabilities
- Why/when you'd use it
- How it's different from similar tools
```

**Solution 2: Add context from video**
```
Description template:
"[Entity Name] - [What it is]. [Key feature 1]. [Key feature 2]. [Use case from video]. [Why it matters]."

Example:
"GitHub Actions - CI/CD automation platform. Enables automated testing and deployment workflows. Integrates directly with GitHub repositories. Demonstrated in video for automated React app deployment to production."
```

**Solution 3: Reference specific uses**
```
Instead of generic description:
"Used for web development"

Include specifics from video:
"Used to build responsive landing pages with Tailwind CSS, demonstrated with e-commerce checkout flow implementation"
```

### Problem: Wrong entity type categorization

**Symptoms:**
- Workflow listed as Tool
- Action listed as Skill
- Object listed as Workflow
- Quality reviewer requests recategorization

**Solutions:**

**Solution 1: Review entity type definitions**
```
Quick reference:

Workflow = Multi-step process with clear beginning and end
Tool = Specific software/platform/service
Object = Digital artifact (file, component, output)
Action = Single specific task
Profession = Job role/title
Skill = Competency or capability
Department = Organizational unit
```

**Solution 2: Ask categorization questions**
```
For each entity, ask:

"Is this a process?" → Workflow
"Is this a software/service?" → Tool
"Is this something created?" → Object
"Is this a single task?" → Action
"Is this a job role?" → Profession
"Is this a learned capability?" → Skill
"Is this an org unit?" → Department
```

**Solution 3: Common categorization fixes**
```
Often miscategorized:

"Deploy to production"
❌ Workflow (too simple)
✅ Action (single task)

"Deployment workflow"
✅ Workflow (multi-step process)

"VS Code"
✅ Tool (software)
❌ Object (not a created artifact)

"React component"
✅ Object (created artifact)
❌ Tool (not a service)

"Component development"
❌ Object
✅ Skill (capability)
```

---

## Phase 3: Gap Analysis Problems

### Problem: Gap analysis script fails

**Symptoms:**
- Error: "File not found"
- Error: "Invalid JSON"
- Script crashes
- No output generated

**Solutions:**

**Solution 1: Extraction file missing/incorrect**
```bash
# Check extraction file exists
dir "03_EXTRACTION\RSR-XXX\extracted_entities.md"

# If missing, Phase 2 not complete
# Complete Phase 2 first

# Verify file has content (not empty)
type "03_EXTRACTION\RSR-XXX\extracted_entities.md"
```

**Solution 2: LIBRARIES path incorrect**
```bash
# Verify LIBRARIES exists
dir "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES"

# Check script configuration
python scripts/check_config.py

# Update paths if needed in config.py
```

**Solution 3: Run with verbose logging**
```bash
# Run script with debug output
python scripts/run_gap_analysis.py RSR-XXX --verbose

# Check error log
type scripts\logs\gap_analysis.log

# Share error message with team lead
```

**Solution 4: Manual gap analysis**
```
If script completely fails:
1. Open extracted_entities.md
2. For each entity, manually search LIBRARIES
3. Note which entities not found
4. Create basic gap analysis report
5. Report script issue to team lead
```

### Problem: Gap coverage seems wrong

**Symptoms:**
- Shows 0% gaps but know entities are new
- Shows 100% gaps but entities exist in LIBRARIES
- Match scores don't make sense

**Solutions:**

**Solution 1: LIBRARIES out of date**
```bash
# Update LIBRARIES if using version control
cd LIBRARIES
git pull

# Re-run gap analysis
python scripts/run_gap_analysis.py RSR-XXX --force
```

**Solution 2: Entity names don't match LIBRARIES format**
```
Gap analysis uses fuzzy matching but needs similar names:

Extracted: "Claude Artificial Intelligence"
LIBRARIES has: "Claude AI"
May not match well.

Fix:
1. Standardize entity names in extraction
2. Use common/official names
3. Re-run gap analysis
```

**Solution 3: Check match score thresholds**
```
Gap analysis considers match scores:
- Score > 0.90 = "Already in LIBRARIES"
- Score 0.70-0.90 = "Similar entity exists"
- Score < 0.70 = "New entity (gap)"

If thresholds seem wrong, may need script adjustment.
Report to team lead.
```

### Problem: Can't decide if entity is duplicate

**Symptoms:**
- Match score 0.85 (borderline)
- Entity seems similar but different
- Descriptions don't match well

**Solutions:**

**Solution 1: Side-by-side comparison**
```
1. Open extracted entity description
2. Find matched entity in LIBRARIES
3. Compare:
   □ Are they same thing with different names?
   □ Is one more specific than the other?
   □ Do they have same use cases?
   □ Are key features identical?
```

**Solution 2: Decision tree**
```
If match score > 0.90:
└─ Almost certainly duplicate → Don't integrate

If match score 0.85-0.90:
├─ Same core functionality?
│  ├─ Yes → Duplicate → Don't integrate
│  └─ No → Different → Integrate
└─ Just similarly named?
   └─ Yes → Check functionality → Decide

If match score < 0.85:
└─ Likely different → Integrate
```

**Solution 3: Ask team lead**
```
When in doubt:
1. Document both descriptions
2. Note match score
3. Ask team lead for decision
4. Document decision for future reference
```

---

## Phase 4: Integration Problems

### Problem: JSON syntax error

**Symptoms:**
- Validation script fails
- Error: "Expecting comma"
- Error: "Unexpected token"
- Error: "Invalid JSON"

**Solutions:**

**Solution 1: Use JSON validator**
```
Online JSON validators:
1. Copy JSON content
2. Go to: jsonlint.com
3. Paste and validate
4. Fix errors shown
5. Copy corrected JSON back
```

**Solution 2: Common JSON errors**
```
❌ Missing comma:
{
  "field1": "value1"
  "field2": "value2"
}

✅ Fixed:
{
  "field1": "value1",
  "field2": "value2"
}

❌ Trailing comma:
{
  "field1": "value1",
  "field2": "value2",
}

✅ Fixed (remove last comma):
{
  "field1": "value1",
  "field2": "value2"
}

❌ Unquoted strings:
{
  "name": value
}

✅ Fixed:
{
  "name": "value"
}

❌ Single quotes instead of double:
{
  'name': 'value'
}

✅ Fixed:
{
  "name": "value"
}
```

**Solution 3: Use JSON template**
```
Don't write from scratch:
1. Copy working JSON from previous research
2. Find in: 05_INTEGRATION/RSR-[previous]/
3. Modify field values
4. Keep structure identical
5. Validate before saving
```

### Problem: Duplicate ID error

**Symptoms:**
- Validation error: "ID already exists"
- Integration fails
- LIBRARIES conflicts

**Solutions:**

**Solution 1: Check next available ID**
```bash
# Get next ID in category
python scripts/get_next_id.py TOL-AID

# Output: Next available: TOL-AID-215

# Verify not in use
python scripts/check_id_exists.py TOL-AID-215

# If available, use this ID
```

**Solution 2: Search LIBRARIES for ID**
```bash
# Search for ID across all files
findstr /s /i "TOL-AID-214" "G:\Job\REMS\Dropbox\ENTITIES\LIBRARIES\*"

# If found, ID in use
# Use next sequential ID instead
```

**Solution 3: Fix duplicate**
```
If you already created duplicate:
1. Identify which ID is duplicate
2. Get correct next available ID
3. Update your JSON file with correct ID
4. Update all cross-references
5. Validate again
```

### Problem: Missing required fields

**Symptoms:**
- Validation error: "Required field missing"
- Entity incomplete
- Integration fails

**Solutions:**

**Solution 1: Check required fields list**
```
Required fields by entity type:

Workflow:
- entity_type
- workflow_id
- workflow_name
- description
- metadata.created_date
- metadata.status

Tool:
- entity_type
- tool_id
- tool_name
- description
- metadata.created_date
- metadata.status

[Check entity templates for complete lists]
```

**Solution 2: Use complete template**
```
1. Open: 12_TEMPLATES.md (v1 docs)
2. Find entity type template
3. Copy complete template
4. Fill in all fields
5. Don't delete any required fields
```

**Solution 3: Validation details**
```bash
# Run validation with details
python scripts/validate_integration.py RSR-XXX --verbose

# Output shows exactly which fields missing
# Add missing fields to JSON
# Re-validate
```

### Problem: Invalid cross-reference

**Symptoms:**
- Validation error: "Referenced ID not found"
- Error: "Invalid tool reference"
- Mapping fails

**Solutions:**

**Solution 1: Verify referenced IDs exist**
```bash
# Check if ID exists in LIBRARIES
python scripts/check_id_exists.py TOL-DEV-089

# If doesn't exist:
# - Find correct ID
# - Or remove cross-reference
# - Or integrate that entity first
```

**Solution 2: Search for correct ID**
```bash
# Find entity by name
python scripts/find_entity_id.py "Claude AI"

# Output: TOL-AID-201

# Update cross-reference with correct ID
```

**Solution 3: Remove invalid references temporarily**
```
If can't find correct ID:
1. Remove cross-reference from JSON
2. Add TODO note in metadata
3. Complete integration
4. Fix cross-references later
5. Re-validate after fix
```

---

## Phase 5: Mapping Problems

### Problem: Mapping script fails

**Symptoms:**
- Script crashes
- No output generated
- Error messages

**Solutions:**

**Solution 1: Check integration complete**
```bash
# Verify Phase 4 done
dir "05_INTEGRATION\RSR-XXX\*.json"

# Should see JSON files
# If not, complete Phase 4 first
```

**Solution 2: Verify entities in LIBRARIES**
```bash
# Check entities integrated
python scripts/verify_integration.py RSR-XXX

# Should show: "All entities integrated"
# If not, copy JSON files to LIBRARIES folders
```

**Solution 3: Run with verbose mode**
```bash
# Debug mapping
python scripts/run_mapping.py RSR-XXX --verbose

# Check log
type scripts\logs\mapping.log

# Look for specific error
```

### Problem: Quality score too low (< 0.90)

**Symptoms:**
- Overall score 0.75-0.89
- Specific component scores low
- Review required

**Solutions:**

**Solution 1: Identify low-score component**
```
Check mapping report sections:

Gap Coverage Score: 0.65 ← LOW
Match Accuracy Score: 0.95 ← OK
Integration Quality: 0.88 ← OK
Overall: 0.82 ← TOO LOW

Problem is: Gap Coverage
Solution: Integrate more new entities
```

**Solution 2: Improve specific scores**
```
Low Gap Coverage (< 0.70):
- Review gap analysis again
- Integrate more new entities
- Add entities you skipped

Low Match Accuracy (< 0.85):
- Check for duplicates you integrated
- Remove duplicate entities
- Improve entity matching

Low Integration Quality (< 0.85):
- Fix JSON errors
- Add missing fields
- Improve descriptions
- Fix cross-references

Low Cross-Reference Quality (< 0.85):
- Add more cross-references
- Fix invalid references
- Link related entities
```

**Solution 3: Systematic improvement**
```
1. Read mapping report completely
2. Note all scores < 0.90
3. For each low score:
   a. Identify root cause
   b. Fix underlying issue
   c. Re-run mapping
   d. Verify improvement
4. Repeat until overall ≥ 0.90
```

### Problem: Entities not mapped correctly

**Symptoms:**
- IDs missing in mapping report
- Entities show as unmapped
- Cross-references broken

**Solutions:**

**Solution 1: Verify entities in LIBRARIES**
```bash
# List all entities for this research
python scripts/list_research_entities.py RSR-XXX

# Check each in LIBRARIES
# If missing, copy from 05_INTEGRATION/RSR-XXX/
```

**Solution 2: Re-generate mapping**
```bash
# Clear cache
python scripts/clear_mapping_cache.py RSR-XXX

# Re-run mapping
python scripts/run_mapping.py RSR-XXX --force

# Verify all entities mapped
```

**Solution 3: Manual mapping verification**
```
1. Open entity_mapping_report.md
2. For each extracted entity:
   □ Check if mapped to LIBRARIES ID
   □ Verify ID correct
   □ Check cross-references valid
3. If entity unmapped:
   - Verify JSON file in LIBRARIES
   - Check file naming correct
   - Run mapping again
```

---

## Script and Automation Problems

### Problem: Python script won't run

**Symptoms:**
- "Python not recognized"
- "Module not found"
- "Permission denied"
- Script crashes immediately

**Solutions:**

**Solution 1: Python not installed/configured**
```bash
# Check Python installed
python --version

# Should show: Python 3.x.x
# If not, Python not installed or not in PATH

# Install Python or add to PATH
```

**Solution 2: Wrong directory**
```bash
# Navigate to scripts folder
cd "G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\scripts"

# Run script from this folder
python run_gap_analysis.py RSR-XXX
```

**Solution 3: Missing dependencies**
```bash
# Check if required modules installed
python -c "import pandas, json, pathlib"

# If error, install requirements
pip install -r requirements.txt

# Or install specific module
pip install pandas
```

**Solution 4: Permission denied**
```
1. Close all files/folders
2. Wait for Dropbox sync
3. Run as administrator (if Windows)
4. Try script again
```

### Problem: Script runs but does nothing

**Symptoms:**
- No error message
- No output generated
- Status unchanged
- Files not created

**Solutions:**

**Solution 1: Check script arguments**
```bash
# Verify correct syntax
python script_name.py --help

# Check argument format
# Correct: python run_gap_analysis.py RSR-024
# Wrong: python run_gap_analysis.py 024
# Wrong: python run_gap_analysis.py RSR24
```

**Solution 2: Check input files exist**
```bash
# Script might silently fail if input missing
# Verify required files:
dir "03_EXTRACTION\RSR-XXX\extracted_entities.md"
dir "04_GAP_ANALYSIS\RSR-XXX\"

# If missing, create folders or files first
```

**Solution 3: Check output location**
```bash
# Script might write to different location
# Check all possible output folders:
dir /s /b | findstr "RSR-XXX"

# Look in logs
type scripts\logs\automation.log
```

### Problem: Automation produces wrong results

**Symptoms:**
- Gap analysis shows 0% gaps (but shouldn't)
- Mapping report empty
- Priority scores all zero
- Statistics don't match reality

**Solutions:**

**Solution 1: Update data sources**
```bash
# Ensure LIBRARIES updated
cd LIBRARIES
# Pull latest if using version control

# Clear any caches
python scripts/clear_all_caches.py

# Re-run automation
python scripts/run_gap_analysis.py RSR-XXX --force
```

**Solution 2: Verify input data quality**
```
Check:
□ Extraction file has content (not empty)
□ JSON files valid (no syntax errors)
□ CSV files not corrupted
□ IDs formatted correctly
```

**Solution 3: Manual verification**
```
1. Run automation
2. Get results
3. Manually check sample:
   - Pick 3-5 entities
   - Manually verify results
   - Compare with automation output
4. If differences found:
   - Report to team lead
   - Note exact discrepancies
   - Use manual results until fixed
```

---

## Data and File Problems

### Problem: Can't find research folder

**Symptoms:**
- "Path not found"
- "Directory doesn't exist"
- RSR-XXX folder missing

**Solutions:**

**Solution 1: Search for research ID**
```bash
# Search entire system
dir /s /b | findstr "RSR-XXX"

# Should find folder in one of:
# - 02_TRANSCRIPTIONS\RSR-XXX
# - 03_EXTRACTION\RSR-XXX
# - 04_GAP_ANALYSIS\RSR-XXX
# - 05_INTEGRATION\RSR-XXX
# - 06_MAPPING\RSR-XXX
# - 07_ARCHIVE\RSR-XXX
```

**Solution 2: Check Master List**
```bash
# Find in master registry
findstr "RSR-XXX" RESEARCHES_Master_List.csv

# Check Status column:
# - If "Archived", check 07_ARCHIVE
# - If "In Progress", check phase folders
```

**Solution 3: Folder never created**
```bash
# Create research folders
mkdir "02_TRANSCRIPTIONS\RSR-XXX"
mkdir "03_EXTRACTION\RSR-XXX"
mkdir "04_GAP_ANALYSIS\RSR-XXX"
mkdir "05_INTEGRATION\RSR-XXX"
mkdir "06_MAPPING\RSR-XXX"

# Proceed with work
```

### Problem: CSV file corrupted

**Symptoms:**
- Can't open in Excel
- Weird characters showing
- Missing data
- Structure broken

**Solutions:**

**Solution 1: Restore from backup**
```bash
# List recent backups
dir "07_ARCHIVE\backups" /o-d

# Find latest good backup
# Copy to working location
copy "07_ARCHIVE\backups\YYYY-MM-DD\Video_Queue_Master.csv" "01_QUEUE_ASSIGNMENTS\"

# Verify restoration
python scripts/verify_csv_integrity.py
```

**Solution 2: Open in text editor**
```
If Excel can't open:
1. Open in Notepad++ or VS Code
2. Check encoding (should be UTF-8)
3. Look for obvious corruption:
   - Missing quotes
   - Extra commas
   - Broken lines
4. Fix manually if minor
5. Restore from backup if major
```

**Solution 3: Export from backup**
```
1. Open backup copy in Excel
2. File → Save As
3. Choose: CSV UTF-8
4. Save to working location
5. Verify data intact
```

### Problem: Dropbox sync issues

**Symptoms:**
- "Syncing..." never completes
- Files not updating
- Version conflicts
- "Permission denied" errors

**Solutions:**

**Solution 1: Pause and resume sync**
```
1. Right-click Dropbox icon in system tray
2. Click "Pause syncing"
3. Wait 30 seconds
4. Click "Resume syncing"
5. Wait for completion
```

**Solution 2: Resolve sync conflicts**
```
If see "(Conflicted Copy)" files:
1. Open both versions
2. Compare changes
3. Keep correct version
4. Delete conflicted copy
5. Rename if needed
```

**Solution 3: Check Dropbox space**
```
1. Open Dropbox
2. Check storage quota
3. If full:
   - Delete old files
   - Or upgrade plan
   - Or move archived research off Dropbox
```

---

## Quality and Validation Problems

### Problem: Validation script reports errors

**Symptoms:**
- Multiple validation failures
- "Quality check failed"
- Required fields missing
- Format errors

**Solutions:**

**Solution 1: Fix reported errors systematically**
```bash
# Run validation with details
python scripts/validate_integration.py RSR-XXX --verbose > errors.txt

# Read error file
type errors.txt

# Fix each error:
1. Note error type and file
2. Open file
3. Fix issue
4. Save
5. Re-validate
6. Repeat until clean
```

**Solution 2: Common validation fixes**
```
Error: "Missing required field: description"
Fix: Add description field to JSON

Error: "Invalid ID format: WRF-SEC-1"
Fix: Change to WRF-SEC-001 (3 digits)

Error: "Duplicate ID: TOL-AID-214"
Fix: Use next available ID TOL-AID-215

Error: "Referenced ID not found: SKL-DEV-999"
Fix: Find correct ID or remove reference

Error: "Empty value for required field"
Fix: Add actual value (not empty string)
```

**Solution 3: Use validation checklist**
```
Before running validation:

□ All JSON files have .json extension
□ All IDs use correct format
□ All required fields present
□ All descriptions ≥ 10 words
□ All cross-references valid
□ No duplicate IDs
□ Files saved in UTF-8 encoding
□ No trailing commas in JSON
```

### Problem: Quality score below target

**Symptoms:**
- Overall score < 0.90
- Review comments: "Quality insufficient"
- Multiple component scores low

**Solutions:**

See: [Phase 5: Mapping Problems → Quality score too low](#problem-quality-score-too-low--090)

(Same solutions apply)

---

## System and Performance Problems

### Problem: System very slow

**Symptoms:**
- Scripts take very long
- Files slow to open
- Dropbox syncing slow
- Computer unresponsive

**Solutions:**

**Solution 1: Check system resources**
```
Windows Task Manager:
- Press Ctrl+Shift+Esc
- Check CPU usage (should be < 80%)
- Check Memory (should be < 90%)
- Check Disk (should be < 100%)

If high usage:
- Close unnecessary programs
- Restart computer
- Check for background processes
```

**Solution 2: Optimize Dropbox**
```
1. Pause Dropbox sync during intensive work
2. Only sync folders you need
3. Use selective sync:
   - Right-click Dropbox
   - Preferences → Sync
   - Uncheck folders not needed
```

**Solution 3: Clean up files**
```bash
# Remove temporary files
python scripts/cleanup_temp_files.py

# Archive old research
python scripts/archive_old_research.py

# Compress archived files
python scripts/compress_archives.py
```

### Problem: Running out of disk space

**Symptoms:**
- "Disk full" errors
- Can't save files
- Dropbox sync fails
- Very slow performance

**Solutions:**

**Solution 1: Check space usage**
```bash
# Check folder sizes
dir /s

# Identify large folders:
# - 02_TRANSCRIPTIONS
# - 07_ARCHIVE

# Estimate: 5-10 GB per 100 research items
```

**Solution 2: Archive and compress**
```bash
# Compress old archives
python scripts/compress_old_archives.py

# Move very old archives off Dropbox
# (Keep local or external storage)

# Typical compression: 60-70% size reduction
```

**Solution 3: Clean up non-essential files**
```
Delete:
□ Temporary files in temp folders
□ Old backup copies (keep last 30 days only)
□ Cached data files
□ Log files > 30 days old
□ Downloaded videos after transcription
```

---

## When to Ask for Help

### Escalation Guidelines

**Ask immediately if:**
- Data corruption suspected
- Backup restoration needed
- System-wide errors
- Script errors you can't fix
- Blocked > 30 minutes
- Quality score < 0.80 after attempts to fix

**Ask within 2 hours if:**
- Unclear requirements
- Uncertain about decisions
- Need permission/approval
- Process deviation needed

**Ask by end of day if:**
- Quality concerns
- Process improvement ideas
- Documentation unclear
- Tools not working properly

### How to Ask for Help

**Provide this information:**
```
1. What you're trying to do
   Example: "Processing RSR-024 Phase 4 integration"

2. What went wrong
   Example: "Validation script reports duplicate ID error"

3. Exact error message
   Example: "Error: Duplicate ID TOL-AID-214 already exists in LIBRARIES/Tools/"

4. What you've already tried
   Example: "Checked LIBRARIES, confirmed duplicate. Tried using TOL-AID-215 but still error."

5. Which research/video
   Example: "RSR-024 / VQ-120"

6. Relevant files
   Example: "File: 05_INTEGRATION/RSR-024/tool_claude_ai.json"
```

**Channels:**
- Team lead (direct message)
- Team channel (if affects others)
- Documentation issue (if docs problem)

---

## Prevention Tips

### Prevent Problems Before They Happen

**Daily habits:**
```
□ Save work frequently (every 15-30 min)
□ Update status immediately after each phase
□ Run validation scripts before moving forward
□ Make backup copies of critical work
□ Document unusual situations
□ Ask questions early
```

**Quality habits:**
```
□ Read instructions completely
□ Use templates and checklists
□ Validate before submitting
□ Self-review with fresh eyes
□ Learn from revisions
□ Apply best practices consistently
```

**System habits:**
```
□ Keep Dropbox synced
□ Monitor disk space weekly
□ Clean up temp files regularly
□ Update LIBRARIES periodically
□ Check automation logs daily
□ Report errors immediately
```

---

## Related Documentation

**For workflows:**
- [01_STEP_BY_STEP_WORKFLOWS.md](01_STEP_BY_STEP_WORKFLOWS.md)

**For best practices:**
- [03_BEST_PRACTICES.md](03_BEST_PRACTICES.md)

**For daily operations:**
- [02_DAILY_OPERATIONS.md](02_DAILY_OPERATIONS.md)

**For quick reference:**
- [05_QUICK_REFERENCE.md](05_QUICK_REFERENCE.md)

**For technical details:**
- [../v1/13_TROUBLESHOOTING.md](../v1/13_TROUBLESHOOTING.md)

---

**Last Updated:** 2025-12-04
**Version:** 2.0
**Maintained By:** RESEARCHES 2 Team
