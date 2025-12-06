# RESEARCHES 2 - Quick Reference

**Version:** 2.0
**Generated:** 2025-12-04
**Purpose:** Fast lookup for commands, formats, and key information
**Audience:** All users needing quick answers

---

## 📖 Table of Contents

1. [System Overview](#system-overview)
2. [ID Formats Quick Reference](#id-formats-quick-reference)
3. [Command Cheat Sheet](#command-cheat-sheet)
4. [File Locations](#file-locations)
5. [CSV Schema Quick Reference](#csv-schema-quick-reference)
6. [JSON Templates Quick Access](#json-templates-quick-access)
7. [Entity Type Decision Tree](#entity-type-decision-tree)
8. [Quality Targets](#quality-targets)
9. [Status Values](#status-values)
10. [Priority Calculations](#priority-calculations)
11. [Time Estimates](#time-estimates)
12. [Keyboard Shortcuts & Aliases](#keyboard-shortcuts--aliases)

---

## System Overview

### 7-Phase Pipeline

```
Phase 0: Search Queue
    ↓ manual selection
Phase 0→1: Video Queue (TSM-008)
    ↓ automated + manual
Phase 1: Transcription (RSR-XXX)
    ↓ automated
Phase 2: Extraction → extracted_entities.md
    ↓ manual
Phase 3: Gap Analysis → gap_analysis_report.md
    ↓ automated
Phase 4: Integration → JSON in LIBRARIES
    ↓ manual + automated
Phase 5: Mapping → entity_mapping_report.md
    ↓ automated
Phase 6: Archive & Documentation
```

### System Statistics

| Metric | Value |
|--------|-------|
| Total Scripts | 21 Python scripts |
| Total Prompts | 48 AI prompts |
| Automation Level | 70% overall |
| Processing Time | 4-6 hours per video |
| Quality Target | ≥ 0.90 score |
| Entity Types | 7 types |
| CSV Files | 3 master files |

---

## ID Formats Quick Reference

### Entity ID Formats

| Entity Type | Format | Example | Notes |
|-------------|--------|---------|-------|
| Workflow | `WRF-{CAT}-{NNN}` | WRF-SEC-014 | Multi-step process |
| Tool | `TOL-{CAT}-{NNN}` | TOL-AID-201 | Software/platform |
| Object | `OBJ-{CAT}-{NNN}` | OBJ-MED-100 | Digital artifact |
| Action | `ACT-{CAT}-{NNN}` | ACT-DSG-050 | Single task |
| Profession | `PRF-{CAT}-{NNN}` | PRF-ENG-001 | Job role |
| Skill | `SKL-{CAT}-{NNN}` | SKL-TEC-025 | Competency |
| Department | `DPT-{CAT}-{NNN}` | DPT-HRM-001 | Org unit |

### Research & Queue IDs

| Type | Format | Example | Range |
|------|--------|---------|-------|
| Research | `RSR-{NNN}` | RSR-024 | 001-999 |
| Video Queue | `VQ-{NNN}` | VQ-120 | 001-999 |
| Search | `SEARCH-{NNN}` | SEARCH-042 | 001-999 |

### Category Codes (3-letter)

**Common categories:**
```
AID = AI/ML Tools
DEV = Development
DSG = Design
MKT = Marketing
SEC = Security
HRM = Human Resources
FIN = Finance
OPS = Operations
MGT = Management
EDU = Education
```

**ID Rules:**
- PREFIX: 3 letters (uppercase)
- CATEGORY: 3 letters (uppercase)
- NUMBER: 3 digits (001-999, sequential)
- Separator: Hyphen (-)

**Examples:**
```
✅ Correct: WRF-DEV-045
✅ Correct: TOL-AID-201
❌ Wrong: wrf-dev-45
❌ Wrong: WRF_DEV_045
❌ Wrong: WRF-DEV-45
```

---

## Command Cheat Sheet

### Daily Commands

**Morning startup:**
```bash
python scripts/generate_daily_status.py
python scripts/check_overdue_videos.py
python scripts/list_review_items.py
```

**Video processing:**
```bash
# Phase 3: Gap Analysis
python scripts/run_gap_analysis.py RSR-XXX

# Phase 4: Validation
python scripts/validate_integration.py RSR-XXX

# Phase 5: Mapping
python scripts/run_mapping.py RSR-XXX
```

**Queue management:**
```bash
# Assign video
python scripts/assign_video.py VQ-XXX "Employee Name"

# Update priority
python scripts/calculate_priority.py VQ-XXX

# Check assignments
python scripts/list_assignments.py "Employee Name"
```

**Quality checks:**
```bash
# Validate extraction
python scripts/validate_extraction.py RSR-XXX

# Check integration
python scripts/verify_integration.py RSR-XXX

# Verify LIBRARIES integrity
python scripts/verify_libraries_integrity.py
```

**End of day:**
```bash
python scripts/generate_eod_report.py
python scripts/verify_backup.py
```

### ID Management

```bash
# Get next available ID
python scripts/get_next_id.py TOL-AID

# Check if ID exists
python scripts/check_id_exists.py TOL-AID-215

# Find entity by name
python scripts/find_entity_id.py "Claude AI"

# List all IDs in category
python scripts/list_category_ids.py TOL-AID
```

### Data Management

```bash
# Archive completed research
python scripts/archive_research.py RSR-XXX

# Backup current state
python scripts/manual_backup.py

# Restore from backup
python scripts/restore_from_backup.py YYYY-MM-DD

# Verify data integrity
python scripts/verify_data_integrity.py
```

### Reporting

```bash
# Daily status
python scripts/generate_daily_status.py

# Weekly report
python scripts/generate_weekly_report.py

# Quality dashboard
python scripts/generate_quality_dashboard.py

# Team performance
python scripts/generate_team_report.py
```

---

## File Locations

### System Root
```
G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\
```

### Key Folders

```
RESEARCHES 2/
├── 00_SEARCH_QUEUE/
│   └── Search_Queue_Master.csv
│
├── 01_QUEUE_ASSIGNMENTS/
│   └── Video_Queue_Master.csv
│
├── 02_TRANSCRIPTIONS/
│   └── RSR-XXX/
│       └── RSR-XXX_transcript.md
│
├── 03_EXTRACTION/
│   └── RSR-XXX/
│       └── extracted_entities.md
│
├── 04_GAP_ANALYSIS/
│   └── RSR-XXX/
│       └── gap_analysis_report.md
│
├── 05_INTEGRATION/
│   └── RSR-XXX/
│       └── *.json (entity files)
│
├── 06_MAPPING/
│   └── RSR-XXX/
│       └── entity_mapping_report.md
│
├── 07_ARCHIVE/
│   ├── RSR-XXX/ (completed research)
│   └── backups/ (daily backups)
│
├── scripts/
│   ├── *.py (21 automation scripts)
│   └── logs/ (script logs)
│
├── prompts/
│   └── *.txt (48 AI prompts)
│
└── documentation/
    ├── v1/ (file-by-file reference)
    └── v2/ (workflow guides)
```

### LIBRARIES Structure

```
LIBRARIES/
├── Workflows/
│   └── WRF-{CAT}-{NNN}.json
├── Tools/
│   └── TOL-{CAT}-{NNN}.json
├── Objects/
│   └── OBJ-{CAT}-{NNN}.json
├── Actions/
│   └── ACT-{CAT}-{NNN}.json
├── Professions/
│   └── PRF-{CAT}-{NNN}.json
├── Skills/
│   └── SKL-{CAT}-{NNN}.json
└── Departments/
    └── DPT-{CAT}-{NNN}.json
```

---

## CSV Schema Quick Reference

### Search_Queue_Master.csv

| Field | Type | Values | Example |
|-------|------|--------|---------|
| Search_ID | String | SEARCH-NNN | SEARCH-001 |
| Employee | String | Full name | John Doe |
| Department | String | 3-letter code | DEV |
| Topic | String | Free text | Claude AI tutorials |
| Status | Enum | Assigned, In Progress, Completed | Assigned |
| Date_Assigned | Date | YYYY-MM-DD | 2025-12-04 |
| Videos_Found | Integer | Count | 12 |
| Date_Completed | Date | YYYY-MM-DD | 2025-12-05 |

### Video_Queue_Master.csv (21 fields)

| Field | Type | Example |
|-------|------|---------|
| VQ_ID | String | VQ-120 |
| Video_URL | URL | https://youtube.com/watch?v=... |
| Video_Title | String | Claude AI Tutorial |
| Channel_Name | String | AI Tutorials Pro |
| Duration_Seconds | Integer | 1250 |
| Upload_Date | Date | 2025-11-15 |
| Views | Integer | 250000 |
| Likes | Integer | 12000 |
| Priority_Score | Float | 75.5 |
| Department | String | DEV |
| Topic | String | AI Integration |
| Assigned_To | String | John Doe |
| Status | Enum | Assigned / In Progress / Review / Completed / Blocked |
| Date_Assigned | Date | 2025-12-04 |
| Date_Completed | Date | 2025-12-06 |
| Research_ID | String | RSR-024 |
| Quality_Score | Float | 0.92 |
| Complexity | Integer | 1-5 |
| Notes | String | Free text |
| Blocker | String | Issue description |
| Expected_Completion | Date | 2025-12-06 |

### RESEARCHES_Master_List.csv

| Field | Type | Example |
|-------|------|---------|
| Research_ID | String | RSR-024 |
| VQ_ID | String | VQ-120 |
| Video_Title | String | Claude AI Tutorial |
| Employee | String | John Doe |
| Department | String | DEV |
| Status | Enum | In Progress / Completed / Archived |
| Date_Started | Date | 2025-12-04 |
| Date_Completed | Date | 2025-12-06 |
| Quality_Score | Float | 0.92 |

---

## JSON Templates Quick Access

### Workflow Template

```json
{
  "entity_type": "workflow",
  "workflow_id": "WRF-XXX-NNN",
  "workflow_name": "[Name]",
  "category": "[Category]",
  "description": "[Detailed description]",
  "steps": [
    "Step 1: [Action]",
    "Step 2: [Action]"
  ],
  "tools_used": ["TOL-XXX-NNN"],
  "skills_required": ["SKL-XXX-NNN"],
  "target_professions": ["PRF-XXX-NNN"],
  "outputs": ["OBJ-XXX-NNN"],
  "metadata": {
    "created_date": "YYYY-MM-DD",
    "source": "RSR-XXX",
    "status": "active",
    "difficulty": "beginner|intermediate|advanced"
  }
}
```

### Tool Template

```json
{
  "entity_type": "tool",
  "tool_id": "TOL-XXX-NNN",
  "tool_name": "[Name]",
  "category": "[Category]",
  "vendor": "[Company]",
  "description": "[Detailed description]",
  "use_cases": [
    "[Use case 1]",
    "[Use case 2]"
  ],
  "key_features": [
    "[Feature 1]",
    "[Feature 2]"
  ],
  "pricing": "Free|Freemium|Paid",
  "platform": "Web|Desktop|Mobile|All",
  "integrations": ["TOL-YYY-NNN"],
  "required_skills": ["SKL-XXX-NNN"],
  "metadata": {
    "created_date": "YYYY-MM-DD",
    "source": "RSR-XXX",
    "status": "active",
    "website": "[URL]"
  }
}
```

### Object Template

```json
{
  "entity_type": "object",
  "object_id": "OBJ-XXX-NNN",
  "object_name": "[Name]",
  "category": "[Category]",
  "description": "[Detailed description]",
  "object_type": "File|Component|Artifact|Document|Output",
  "created_by": ["PRF-XXX-NNN"],
  "using_tools": ["TOL-XXX-NNN"],
  "part_of_workflow": ["WRF-XXX-NNN"],
  "metadata": {
    "created_date": "YYYY-MM-DD",
    "source": "RSR-XXX",
    "status": "active"
  }
}
```

### Minimal Required Fields

**All entities must have:**
```json
{
  "entity_type": "[type]",
  "[type]_id": "XXX-YYY-NNN",
  "[type]_name": "[Name]",
  "description": "[At least 10 words]",
  "metadata": {
    "created_date": "YYYY-MM-DD",
    "status": "active"
  }
}
```

---

## Entity Type Decision Tree

```
Is it a process with multiple steps?
├─ Yes → WORKFLOW
└─ No ↓

Is it software/platform/service?
├─ Yes → TOOL
└─ No ↓

Is it a digital artifact you create?
├─ Yes → OBJECT
└─ No ↓

Is it a single specific task?
├─ Yes → ACTION
└─ No ↓

Is it a job role/title?
├─ Yes → PROFESSION
└─ No ↓

Is it a learned capability?
├─ Yes → SKILL
└─ No ↓

Is it an organizational unit?
├─ Yes → DEPARTMENT
└─ No → Check definitions again
```

### Quick Type Checks

| If it... | Then it's... |
|----------|--------------|
| Has beginning, steps, and end | Workflow |
| You can install/subscribe to | Tool |
| You create/edit/deliver | Object |
| Is one verb + object | Action |
| Is on a business card | Profession |
| Can be learned and measured | Skill |
| Has multiple roles reporting to it | Department |

---

## Quality Targets

### Overall Targets

| Metric | Target | Acceptable | Poor |
|--------|--------|------------|------|
| Overall Quality Score | ≥ 0.90 | 0.85-0.89 | < 0.85 |
| Gap Coverage | 40-60% | 20-80% | < 20% or > 80% |
| Match Accuracy | ≥ 0.90 | 0.85-0.89 | < 0.85 |
| Integration Quality | ≥ 0.90 | 0.85-0.89 | < 0.85 |
| Processing Time | 4-6 hours | 3-7 hours | < 3 or > 7 hours |

### Entity Minimums per Video

| Entity Type | Minimum | Target | Excellent |
|-------------|---------|--------|-----------|
| Workflows | 3 | 5-8 | > 10 |
| Tools | 5 | 8-12 | > 15 |
| Objects | 5 | 8-12 | > 15 |
| Actions | 8 | 12-20 | > 25 |
| Professions | 2 | 3-5 | > 7 |
| Skills | 5 | 8-15 | > 20 |
| Departments | 1 | 2-4 | > 5 |

### Description Quality

| Quality | Description Length | Detail Level |
|---------|-------------------|--------------|
| Minimum | ≥ 10 words | Basic what it is |
| Target | 20-30 words | What, why, how |
| Excellent | 40-60 words | What, why, how, features, context |

---

## Status Values

### Video Queue Status

| Status | Meaning | Next Action |
|--------|---------|-------------|
| Not Started | Added to queue | Assign to employee |
| Assigned | Employee notified | Employee starts work |
| In Progress | Work in progress | Continue phases |
| Review | Awaiting quality review | QA team reviews |
| Completed | Approved and done | Archive |
| Blocked | Issue preventing progress | Resolve blocker |

### Research Status

| Status | Meaning | Location |
|--------|---------|----------|
| In Progress | Active work | Phase folders |
| Completed | All phases done | 06_MAPPING |
| Archived | In archive | 07_ARCHIVE |

### Entity Status

| Status | Meaning | Use When |
|--------|---------|----------|
| active | Currently valid | Default |
| deprecated | Old version exists | Tool superseded |
| inactive | No longer used | Discontinued |

---

## Priority Calculations

### Priority Score Formula

```
Priority Score = (V × 30%) + (L × 20%) + (R × 30%) + (E × 20%)

Where:
V = Views Score = min(30, (views / 1,000,000) × 30)
L = Likes Score = min(20, (likes / 50,000) × 20)
R = Recency Score = 30 × (1 - days_since_publish / 365)
E = Engagement Score = min(20, (likes/views × 100) × 20)
```

### Priority Ranges

| Score | Priority | Action |
|-------|----------|--------|
| 80-100 | Urgent | Process immediately |
| 60-79 | High | Process within 2 days |
| 40-59 | Medium | Process within 1 week |
| 0-39 | Low | Process when capacity available |

### Example Calculation

```
Video Stats:
- Views: 250,000
- Likes: 12,000
- Days old: 30
- Engagement: 4.8% (12,000/250,000)

Calculations:
V = min(30, (250,000 / 1,000,000) × 30) = min(30, 7.5) = 7.5
L = min(20, (12,000 / 50,000) × 20) = min(20, 4.8) = 4.8
R = 30 × (1 - 30/365) = 30 × 0.918 = 27.5
E = min(20, (4.8 × 100) × 20) = min(20, 96) = 20

Priority = 7.5 + 4.8 + 27.5 + 20 = 59.8 (Medium-High)
```

---

## Time Estimates

### Phase Time Estimates

| Phase | Activity | Quick | Typical | Complex |
|-------|----------|-------|---------|---------|
| 0 | Search | 30 min | 60 min | 90 min |
| 0→1 | Queue add | 5 min | 10 min | 15 min |
| 1 | Transcription | 30 min | 45 min | 90 min |
| 2 | Extraction | 90 min | 120 min | 180 min |
| 3 | Gap Analysis | 15 min | 20 min | 30 min |
| 4 | Integration | 45 min | 75 min | 120 min |
| 5 | Mapping | 15 min | 20 min | 30 min |
| | **Total** | **3.5 hrs** | **5 hrs** | **8 hrs** |

### Daily Output Expectations

| Role | Videos/Day | Phases/Day |
|------|------------|------------|
| Junior Analyst | 0.5-1 | 2-3 phases |
| Mid-level Analyst | 1-1.5 | 3-4 phases |
| Senior Analyst | 1.5-2 | 4-6 phases |
| Team Lead | 0.5-1 | 2-3 phases + management |

### Weekly Output

| Metric | Target | Stretch |
|--------|--------|---------|
| Videos processed | 8-12 | 15+ |
| New entities added | 80-120 | 150+ |
| Quality score average | ≥ 0.90 | ≥ 0.95 |

---

## Keyboard Shortcuts & Aliases

### Bash Aliases (Setup)

**Create aliases file:**
```bash
# Create: ~/.bashrc or ~/.bash_aliases

alias gap="python scripts/run_gap_analysis.py"
alias validate="python scripts/validate_integration.py"
alias map="python scripts/run_mapping.py"
alias nextid="python scripts/get_next_id.py"
alias checkid="python scripts/check_id_exists.py"
alias findid="python scripts/find_entity_id.py"
alias status="python scripts/generate_daily_status.py"
alias backup="python scripts/manual_backup.py"
```

**Usage:**
```bash
gap RSR-024
validate RSR-024
map RSR-024
nextid TOL-AID
checkid TOL-AID-215
findid "Claude AI"
status
backup
```

### Windows Batch Shortcuts

**Create: shortcuts.bat**
```batch
@echo off
set SCRIPTS=G:\Job\REMS\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\scripts

python %SCRIPTS%\%*
```

**Usage:**
```batch
shortcuts run_gap_analysis.py RSR-024
shortcuts validate_integration.py RSR-024
```

### VS Code Snippets

**JSON snippet:**
```json
"workflow-template": {
  "prefix": "wrf",
  "body": [
    "{",
    "  \"entity_type\": \"workflow\",",
    "  \"workflow_id\": \"WRF-${1:CAT}-${2:NNN}\",",
    "  \"workflow_name\": \"${3:Name}\",",
    "  \"category\": \"${4:Category}\",",
    "  \"description\": \"${5:Description}\",",
    "  \"metadata\": {",
    "    \"created_date\": \"${CURRENT_YEAR}-${CURRENT_MONTH}-${CURRENT_DATE}\",",
    "    \"source\": \"RSR-${6:XXX}\",",
    "    \"status\": \"active\"",
    "  }",
    "}"
  ]
}
```

---

## Common Command Patterns

### Video Processing Pattern

```bash
# Complete video workflow
python scripts/run_gap_analysis.py RSR-024
python scripts/validate_integration.py RSR-024
python scripts/run_mapping.py RSR-024
```

### Quality Check Pattern

```bash
# Full quality verification
python scripts/validate_extraction.py RSR-024
python scripts/validate_integration.py RSR-024
python scripts/verify_integration.py RSR-024
python scripts/verify_libraries_integrity.py
```

### Daily Operations Pattern

```bash
# Morning routine
python scripts/generate_daily_status.py
python scripts/check_overdue_videos.py
python scripts/list_review_items.py

# End of day
python scripts/generate_eod_report.py
python scripts/verify_backup.py
```

---

## Regex Patterns

### Searching CSVs

**Find specific research:**
```bash
findstr "RSR-024" RESEARCHES_Master_List.csv
```

**Find by employee:**
```bash
findstr "John Doe" Video_Queue_Master.csv
```

**Find by status:**
```bash
findstr "In Progress" Video_Queue_Master.csv
```

### Searching LIBRARIES

**Find entity by ID:**
```bash
findstr /s /i "WRF-SEC-014" LIBRARIES\*
```

**Find entity by name:**
```bash
findstr /s /i "Claude AI" LIBRARIES\*.json
```

---

## Emergency Reference

### Critical Issues

**Data corruption:**
```bash
# STOP all work
# Contact team lead
# DO NOT save anything
# Restore from backup:
python scripts/restore_from_backup.py YYYY-MM-DD
```

**Validation failing:**
```bash
# Get detailed errors
python scripts/validate_integration.py RSR-XXX --verbose > errors.txt
type errors.txt
# Fix each error systematically
```

**Quality score < 0.80:**
```bash
# Find low-scoring research
python scripts/find_low_quality.py
# Review and rework identified items
```

### Quick Fixes

**CSV won't open:**
1. Check if open elsewhere
2. Wait for Dropbox sync
3. Restore from backup

**Script won't run:**
1. Check Python installed: `python --version`
2. Check in correct folder
3. Check file paths exist

**Can't find file:**
1. Search: `dir /s /b | findstr "filename"`
2. Check RESEARCHES_Master_List.csv
3. Check 07_ARCHIVE

---

## Resource Links

### Internal Documentation

- **v2 Workflows:** [01_STEP_BY_STEP_WORKFLOWS.md](01_STEP_BY_STEP_WORKFLOWS.md)
- **v2 Operations:** [02_DAILY_OPERATIONS.md](02_DAILY_OPERATIONS.md)
- **v2 Best Practices:** [03_BEST_PRACTICES.md](03_BEST_PRACTICES.md)
- **v2 Troubleshooting:** [04_TROUBLESHOOTING_GUIDE.md](04_TROUBLESHOOTING_GUIDE.md)
- **v1 Technical Docs:** [../v1/README.md](../v1/README.md)

### AI Platforms

- **Claude AI:** https://claude.ai
- **ChatGPT:** https://chat.openai.com
- **Perplexity:** https://perplexity.ai
- **Google Gemini:** https://gemini.google.com

### Tools

- **JSON Validator:** https://jsonlint.com
- **CSV Editor:** Excel, LibreOffice, VS Code
- **Text Editor:** VS Code, Notepad++
- **Python:** https://python.org

---

## Quick Tips

### Speed Tips

✅ **DO:**
- Use templates (saves 10-15 min per entity)
- Batch similar tasks (saves 30-45 min per day)
- Let automation handle repetitive work
- Use keyboard shortcuts
- Keep reference files open

❌ **DON'T:**
- Switch between videos unnecessarily
- Manually do what scripts can do
- Skip validation to save time
- Work without breaks
- Create from scratch when templates exist

### Quality Tips

✅ **DO:**
- Read transcription completely
- Use two-pass extraction (AI + manual)
- Validate before moving forward
- Self-review with fresh eyes
- Ask questions early

❌ **DON'T:**
- Skip quality checks
- Accept AI output without review
- Guess at categorization
- Ignore low quality scores
- Wait until blocked to ask help

### Organization Tips

✅ **DO:**
- Update status immediately
- Name files consistently
- Document blockers as they occur
- Keep workspace organized
- Track your patterns

❌ **DON'T:**
- Delay status updates
- Use random naming
- Forget to document issues
- Clutter workspace
- Ignore your metrics

---

## Print-Ready Checklists

### Daily Checklist

```
Morning (10 min):
□ Check assigned videos
□ Review overnight automation
□ Check new search assignments
□ Open required tools
□ Review yesterday's work
□ Plan today's priorities

During Work:
□ Update status after each phase
□ Save work every 15-30 min
□ Run validation scripts
□ Document blockers immediately
□ Take breaks every 90 min

End of Day (15 min):
□ Update all video statuses
□ Save all work
□ Update task completion %
□ Note any blockers
□ Plan tomorrow
□ Close sensitive documents
□ Log time spent
```

### Phase Completion Checklist

```
Phase 1 - Transcription:
□ Transcription complete
□ Timestamps included
□ Major errors fixed
□ File saved correctly
□ Status updated

Phase 2 - Extraction:
□ All 7 entity types present
□ Minimum counts met
□ Descriptions clear (≥ 10 words)
□ No obvious duplicates
□ Proper categorization
□ File saved correctly
□ Status updated

Phase 3 - Gap Analysis:
□ Script ran successfully
□ Report generated
□ Gap coverage reviewed
□ High matches checked
□ Decisions documented
□ Status updated

Phase 4 - Integration:
□ JSON files created
□ Valid JSON syntax
□ Correct ID formats
□ Required fields filled
□ Cross-references valid
□ Validation passed
□ Files copied to LIBRARIES
□ Status updated

Phase 5 - Mapping:
□ Script ran successfully
□ Report generated
□ Quality score ≥ 0.90
□ All entities mapped
□ Status updated to "Review"
```

---

**Last Updated:** 2025-12-04
**Version:** 2.0
**Maintained By:** RESEARCHES 2 Team

---

**💡 Pro Tip:** Bookmark this page for instant access to commands, formats, and quick answers!
