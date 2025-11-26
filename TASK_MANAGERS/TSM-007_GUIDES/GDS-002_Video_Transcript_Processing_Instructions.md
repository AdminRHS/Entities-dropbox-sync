# GDS-002: Video Transcript Processing Instructions

**Version:** 1.0
**Date:** 2025-11-25
**Status:** Active
**Target Users:** Video processing team members (AI, Video departments)
**Reference System:** RESEARCHES 6-Milestone Workflow

---

## Overview

### Purpose

This guide provides step-by-step instructions for processing video transcripts through the complete RESEARCHES workflow, from video search to library integration.

### What You'll Do

1. Assign and track video search tasks (Milestone MLT-010: Search Queue)
2. Prioritize videos for processing (Milestone MLT-011: Video Queue)
3. Transcribe videos with full taxonomy (Milestone MLT-012: Transcriptions)
4. Extract entities and cross-references (Milestone MLT-013: Analysis/Extraction)
5. Perform gap analysis (Milestone MLT-013: Gap Analysis)
6. Create JSON entities and integrate (Milestone MLT-014: Integration)
7. Generate final mapping documentation (Milestone MLT-013: Library Mapping)

### Time Commitment

- **Research & Search:** 2-3 hours/week
- **Per Video Processing:** 50-100 minutes (with v3.2 improvements)
  - Transcription: 40-60 minutes
  - Gap Analysis: 10-20 minutes
  - Integration: 10-20 minutes
- **Weekly Target:** 3-5 videos processed

### Key Benefits

- **90-95% time savings** vs manual processing (pre-v3.2: 4.5-9.5 hours per video)
- Systematic knowledge capture from video sources
- Continuous library growth and enrichment
- Structured taxonomy integration

---

## Quick Start

### Before You Begin

**Required Access:**
- [ ] ENTITIES/TASK_MANAGERS/RESEARCHES/ folder
- [ ] ENTITIES/PROMPTS/ folder
- [ ] ENTITIES/LIBRARIES/ folder
- [ ] Video transcription tools (Google AI Studio, Transcribe AI, or Whisper)

**Required Knowledge:**
- [ ] Understanding of entity taxonomy (MLT-###, TST-###, TOL-###, etc.)
- [ ] Familiarity with video transcript formats
- [ ] Basic gap analysis methodology
- [ ] JSON file creation

**Key Files:**
- **Workflow Overview:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/README.md`
- **Complete Workflow:** `/ENTITIES/PROMPTS/PMT-012_Transcript_Processing_Workflow.md`
- **Transcription Prompt:** `/ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md`
- **Gap Analysis Examples:** `/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Gap_Analysis/`

---

## Complete 6-Milestone Workflow

### Milestone MLT-010: Search Queue (2-3 hours/week)

#### Goal
Assign video search tasks based on strategic priorities and weekly reports

#### Location
`/ENTITIES/TASK_MANAGERS/RESEARCHES/00_SEARCH_QUEUE/`

#### Process

**1. Identify Research Needs**

From:
- Daily reports and strategic priorities
- Department requests
- Library gaps identified in previous processing
- Current project challenges

**2. Create Search Assignment**

Use script:
```bash
python 00_SEARCH_QUEUE/scripts/assign_search.py "Employee Name" "Department" "Search Topic"
```

Example:
```bash
python assign_search.py "Nikolay Artemchuk" "AI" "Claude MCP OAuth tutorials"
```

**3. Track in Search Queue Master**

File: `00_SEARCH_QUEUE/Search_Queue_Master.csv`

**4. Employee Executes Search**

- Use Perplexity AI (recommended) or YouTube
- Search criteria: Published in last 30-60 days, 10-40 minutes length
- Focus on practical tutorials, not news/hype

**5. Complete Search**

Use script:
```bash
python 00_SEARCH_QUEUE/scripts/complete_search.py SEARCH-001 15
```

Where `15` is the number of videos found.

#### Output
- Search assignments tracked
- Videos identified for queue

---

### Milestone MLT-011: Video Queue (30 minutes/week)

#### Goal
Accumulate and prioritize videos before processing

#### Location
`/ENTITIES/TASK_MANAGERS/RESEARCHES/01_VIDEO_QUEUE/`

#### Process

**1. Add Video to Queue**

Use script:
```bash
python 01_VIDEO_QUEUE/scripts/add_video_to_queue.py \
    "https://youtube.com/watch?v=VIDEO_ID" \
    "Your Name" \
    "Research Topic" \
    "Perplexity"
```

**2. Calculate Priority**

Videos are scored 0-100:
- **Strategic Alignment:** 0-40 points
- **Tool/Tech Relevance:** 0-30 points
- **Actionable Value:** 0-30 points

Use script:
```bash
python 01_VIDEO_QUEUE/scripts/calculate_priority.py VQ-001
```

**3. Select for Processing**

- Minimum score: 70/100
- Priority: Select videos scoring 80+
- Target: 3-5 videos per week

**4. Update Status**

```bash
python 01_VIDEO_QUEUE/scripts/update_queue_status.py update VQ-001 Selected
```

#### Files
- `Video_Queue_Master.csv` - Main queue with metadata
- `Video_Queue_Dashboard.html` - Visual queue manager

#### Output
- Prioritized video list
- Top 3-5 videos selected for transcription

---

### Milestone MLT-012: Transcriptions (40-60 minutes/video)

#### Goal
Convert video to structured markdown with full taxonomy analysis

#### Location
`/ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/`

#### Tools
- **Google AI Studio** (recommended for smaller videos)
- **Transcribe AI** (for larger videos)
- **Whisper** (alternative, local processing)

#### Process

**1. Load Transcription Prompt**

Open: `/ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md`

This contains v3.2 custom instructions with 14 taxonomy sections.

**2. Upload Video to Transcription Tool**

- Google AI Studio: Upload video directly
- Transcribe AI: Provide video URL
- Whisper: Download video first, then process

**3. Apply PMT-004 Instructions**

Paste the custom instructions from PMT-004 into the transcription tool.

**4. Generate Transcription**

The tool will create a structured markdown document with:

**Core Sections (1-3):**
- Section 1: Metadata (title, URL, duration, date)
- Section 2: Description (key topics, links)
- Section 3: Word-for-word transcription (timestamps every 30-60 sec)

**Taxonomy Sections (4-14):**
- Section 4: Workflows Identification
- Section 4B: Task Templates Extraction (ACTION_OBJECT_CONTEXT)
- Section 4C: Step Templates Extraction (ACTION_OBJECT_SPECIFIC_DETAIL)
- Section 4D: Project Templates (if applicable)
- Section 5: Action Verbs (Categories A-G)
- Section 6: Task Chains (sequential flows with →)
- Section 7B: Skills Extraction ("action via tool" format)
- Section 8: Tools & Technologies Matrix (TABLE format)
- Section 9: Objects & Deliverables
- Section 10: Integration Patterns
- Section 11: Business Concepts & Strategy
- Section 12: Optimization & Best Practices
- Section 13: Reusability Analysis
- Section 14: Success Metrics & Performance Data

**5. Validate Output**

Quality checks:
- [ ] Output is markdown (.md), NOT JSON
- [ ] All 14 sections present
- [ ] Task Templates follow ACTION_OBJECT_CONTEXT naming
- [ ] Step Templates follow ACTION_OBJECT_SPECIFIC_DETAIL naming
- [ ] Skills follow "action via tool" format
- [ ] Tools matrix in TABLE format
- [ ] Timestamps included

**6. Save Transcription**

Save to: `/ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`

File naming: `Video_[Number]_[Short_Title].md`

Example: `Video_024_Secure_MCP_OAuth_2.1_Implementation.md`

#### Output
- Complete transcription markdown file
- All 14 taxonomy sections populated
- Ready for Phase 3 analysis

---

### Milestone MLT-013: Analysis & Gap Analysis (20-30 minutes/video)

#### Goal
Extract entities, cross-reference, and identify library gaps

#### Locations
- `03_ANALYSIS/Extractions/` - Entity extraction
- `03_ANALYSIS/Gap_Analysis/` - Coverage analysis
- `03_ANALYSIS/Library_Mapping/` - Final mapping

#### Process

**Step 1: Entity Extraction (PMT-007)**

From the transcription file, extract:
- All TOL-### (Tools) mentioned
- All WRF-### (Workflows) identified
- All TST-### (Task Templates) with proper naming
- All STP-### (Step Templates) with proper naming
- All SKL-### (Skills) in proper format
- All OBJ-### (Objects) mentioned
- All ACT-### (Actions) used

Create extraction document.

**Step 2: Gap Analysis (PMT-009 Part 1)**

Create gap analysis document using the format from existing examples.

**Gap Analysis Template:**

```markdown
# Video_XXX – Milestone MLT-015: Gap Analysis
## [Video Title]

**Video**: "[Full Video Title]"
**Phase**: 5 (Gap Analysis – Library Coverage Review)
**Date**: 2025-11-25

---

## 1. Coverage Snapshot

| Entity Group | Total Identified | Already in Libraries? | Gaps / Notes | Priority |
|--------------|-----------------|------------------------|--------------|----------|
| Tools (TOL) | X | Y exist, Z missing | Need... | HIGH/MED/LOW |
| Workflows (WRF) | X | Y exist, Z missing | Need... | HIGH/MED/LOW |
| Milestones / Tasks / Steps | X MLS / Y TSK / Z STP | Y exist, Z missing | Need... | HIGH/MED/LOW |
| Responsibilities (RSP) | X | Y exist, Z missing | Need... | MED |
| Skills (SKL) | X | Y exist, Z missing | Need... | LOW/MED |
| Objects (OBJ) | X | Y exist, Z missing | Need... | MED-HIGH |
| Actions (ACT) | Covered | Already exist | No action | LOW |

---

## 2. Detailed Gaps & Recommendations

### 2.1 Tools Library (LIBRARIES/LBS_003_Tools)

| Tool | Status | Required Actions | Owner | Priority |
|------|--------|------------------|-------|----------|
| Tool_Name (TOL-XXX-YYY) | EXISTS/MISSING | Create/Update entry | Dept | HIGH/MED |

### 2.2 Workflow Library (TASK_MANAGERS)
- **Gap**: Description of what's missing
- **Action**: What needs to be created
- **Notes**: Additional context

### 2.3 Responsibilities / Departments
- Updates needed to existing RSP entries
- New responsibilities to create

### 2.4 Objects Catalog
- Missing objects identified
- Action items

### 2.5 Documentation / Indexes
- Updates needed to master lists

---

## 3. Risks & Impact

| Risk | Impact | Mitigation |
|------|--------|------------|
| Risk 1 | Impact description | How to mitigate |

---

## 4. Next Steps (toward Phase 6)
1. Action item 1
2. Action item 2
3. etc.

---

**Prepared by**: [Your Name]
**Status**: Phase 5 complete – ready for Phase 6 integration
**Date**: 2025-11-25
```

Save to: `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

**Step 3: Cross-Reference Validation**

Verify:
- All tool references point to existing or planned TOL-### entries
- All task/step references use proper naming conventions
- Skills properly link to tasks and tools
- No duplicate IDs proposed

#### Output
- Entity extraction document
- Gap analysis report with coverage snapshot
- Clear action items for Phase 4

---

### Milestone MLT-014: Integration (10-20 minutes/video)

#### Goal
Create JSON entities and integrate into LIBRARIES and TASK_MANAGERS

#### Location
`/ENTITIES/TASK_MANAGERS/RESEARCHES/04_INTEGRATION/`

#### Process (PMT-009 Part 2)

**1. Create Missing Tool Entries**

For each tool marked as MISSING in gap analysis:

Location: `/ENTITIES/LIBRARIES/LBS_003_Tools/[Category]/`

Create JSON file: `Tool_Name.json`

**Tool JSON Schema:**
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOL-CATEGORY-###",
  "name": "Tool Name",
  "vendor": "Vendor Name",
  "category": "Category / Subcategory",
  "purpose": "Primary purpose",
  "description": "Detailed description with video context",
  "skill_level_required": "Beginner|Intermediate|Advanced|Expert",
  "cost_structure": "Pricing model",
  "platform_compatibility": ["Web", "Mobile", "Desktop", "API"],
  "integration_capabilities": ["API", "Zapier", "n8n"],
  "documentation_url": "https://...",
  "actual_remote_helpers_usage": {
    "primary_use": "Main use case from video",
    "users": ["Department"],
    "use_cases": ["Use case 1", "Use case 2"],
    "workflows": ["Workflow from video"]
  },
  "discovery_date": "2025-11-25",
  "discovery_source": "video_transcription",
  "video_source": "Video_XXX",
  "status": "active"
}
```

**2. Create Task Templates**

For each task template identified:

Location: `/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/`

Create JSON file: `TST-XXX_[Task_Name].json`

Follow schema from GDS-001 (Daily Processing guide).

**3. Create Step Templates**

For each step template:

Location: `/ENTITIES/TASK_MANAGERS/TSM-004_Step_Templates/`

Create markdown files with detailed instructions.

**4. Create Skills**

For each skill identified:

Location: `/ENTITIES/TALENTS/Skills/`

Create JSON file: `SKL-XXX_[skill_name].json`

**Skill JSON Schema:**
```json
{
  "entity_type": "TALENTS",
  "sub_entity": "Skill",
  "skill_id": "SKL-###",
  "skill_phrase": "action via tool",
  "difficulty": "Beginner|Intermediate|Advanced|Expert",
  "professions": ["Role 1", "Role 2"],
  "parent_tasks": ["TST-XXX", "TST-YYY"],
  "workflows": ["WRF-XXX"],
  "tools_required": ["TOL-XXX"],
  "time_to_learn": "Duration if mentioned",
  "description": "What skill enables",
  "discovery_source": "Video_XXX",
  "created_date": "2025-11-25"
}
```

**5. Update Mappings**

Update: `/ENTITIES/TASK_MANAGERS/tool_mapping.json`

```json
{
  "Tool Name": {
    "tool_id": "TOL-CATEGORY-###",
    "category": "Category_Name",
    "file_path": "path/to/Tool_Name.json",
    "video_source": "Video_XXX"
  }
}
```

**6. Update Master CSVs**

- Task_Templates_Master_List.csv
- Tools_Master_List.csv (if exists)
- Skills_Master_List.csv (if exists)

#### Output
- New tool JSON files created
- New task template JSON files created
- New step template files created
- New skill JSON files created
- Mappings updated
- Master CSVs updated

---

### Milestone MLT-015: Library Mapping (10 minutes/video)

#### Goal
Generate final mapping documentation

#### Location
`/ENTITIES/TASK_MANAGERS/RESEARCHES/03_ANALYSIS/Library_Mapping/`

#### Process (PMT-009 Part 3)

**Create Mapping Document:**

```markdown
# Video_XXX – Library Mapping Report

**Video**: [Title]
**Date**: 2025-11-25
**Phase**: 6 (Complete)

---

## Entities Created

### Tools
- TOL-XXX-YYY: Tool_Name - Created at [path]
- [List all tools created]

### Task Templates
- TST-XXX: TASK_NAME - Created at [path]
- [List all tasks created]

### Skills
- SKL-XXX: skill_name - Created at [path]
- [List all skills created]

### Objects
- OBJ-XXX: Object_Name - Created at [path]
- [List all objects created]

---

## Integration Points

- tool_mapping.json: Updated with X new tools
- Task_Templates_Master_List.csv: Updated with X new entries
- Skills_Master_List.csv: Updated with X new entries

---

## Coverage Improvement

**Before Video Processing:**
- Tools: X entries
- Tasks: Y entries
- Skills: Z entries

**After Video Processing:**
- Tools: X+A entries (+N%)
- Tasks: Y+B entries (+N%)
- Skills: Z+C entries (+N%)

---

## Next Steps

- [ ] Validate all JSON files created
- [ ] Test task template usage
- [ ] Update RESEARCHES progress tracker
- [ ] Archive to completed videos

---

**Status**: ✅ COMPLETE
**Processing Time**: [Duration]
**Quality**: PASS
```

Save to: `03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping.md`

#### Output
- Complete mapping documentation
- Coverage metrics
- Video processing complete

---

## Workflow Integration with Daily Processing

### When Video Tasks Appear in Daily Processing

If daily processing (GDS-001) identifies video-related tasks:

**Route to RESEARCHES Workflow:**

1. **Identify Video Tasks**
   - Tasks involving video transcription
   - Tasks involving video research
   - Tasks involving library population from videos

2. **Create Search Assignment** (if needed)
   - Use Milestone MLT-010: Search Queue process
   - Assign to appropriate team member

3. **Add to Video Queue**
   - Use Milestone MLT-011: Video Queue process
   - Prioritize and track

4. **Process Through Phases 2-5**
   - Follow this guide (GDS-002)
   - Complete 6-milestone workflow

5. **Report Back to Daily Processing**
   - Note completion in daily processing log
   - Reference created entities (TST-XXX, TOL-XXX, etc.)
   - Update task assignment with new templates available

### Example Integration

**From Daily Processing:**
```
Task extracted: "Process video transcript about Claude MCP OAuth"
Department: AI
Assigned to: Nikolay Artemchuk
```

**Route to Video Workflow:**
```
1. Already have video? → Add to Video Queue (Phase 1)
2. Need to find video? → Create Search Assignment (Phase 0)
3. Process video → Follow Phases 2-5
4. Complete → New templates TST-XXX created, available for future use
```

---

## Quick Reference

### Phase Checklist

```
[ ] Milestone MLT-010: Search Queue - Assign video searches (2-3h/week)
[ ] Milestone MLT-011: Video Queue - Prioritize videos (30min/week)
[ ] Milestone MLT-012: Transcriptions - Transcribe with PMT-004 (40-60min/video)
[ ] Milestone MLT-013: Gap Analysis - Identify library gaps (20-30min/video)
[ ] Milestone MLT-014: Integration - Create JSON entities (10-20min/video)
[ ] Milestone MLT-015: Library Mapping - Final documentation (10min/video)

Weekly Total: 3-5 videos = 3-5 hours
```

### Key File Paths

```
Workflow Base:
/ENTITIES/TASK_MANAGERS/RESEARCHES/

Phases:
00_SEARCH_QUEUE/ - Search assignments
01_VIDEO_QUEUE/ - Video prioritization
02_TRANSCRIPTIONS/ - Transcribed videos
03_ANALYSIS/
  ├── Extractions/ - Entity extraction
  ├── Gap_Analysis/ - Coverage analysis
  └── Library_Mapping/ - Final mapping
04_INTEGRATION/ - Integration tracking

Key Prompts:
/ENTITIES/PROMPTS/PMT-004_Video_Transcription_v4.1.md
/ENTITIES/PROMPTS/PMT-012_Transcript_Processing_Workflow.md

Output Locations:
/ENTITIES/LIBRARIES/LBS_003_Tools/ - New tools
/ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/ - New task templates
/ENTITIES/TALENTS/Skills/ - New skills
```

### Naming Conventions

```
Task Templates: ACTION_OBJECT_CONTEXT (all caps, underscores)
  Example: IMPLEMENT_OAUTH_FOR_MCP_SERVER

Step Templates: ACTION_OBJECT_SPECIFIC_DETAIL (all caps, underscores)
  Example: CONFIGURE_SCALEKIT_DASHBOARD_SETTINGS

Skills: "action via tool" (lowercase, natural language)
  Example: "implement oauth 2.1 via scalekit"

Tool IDs: TOL-[CATEGORY]-###
  Example: TOL-SEC-124 (ScaleKit Dashboard)

Video Files: Video_XXX_[Short_Title].md
  Example: Video_024_Secure_MCP_OAuth.md
```

### Scripts Available

```
Search Queue:
- assign_search.py - Assign new search task
- complete_search.py - Mark search complete

Video Queue:
- add_video_to_queue.py - Add video to queue
- update_queue_status.py - Update video status
- calculate_priority.py - Calculate priority score
- export_queue.py - Export queue data

Progress Tracking:
- update_progress.py - Update video progress
- generate_reports.py - Generate weekly reports
```

---

## Success Metrics

### Per Video
- **Processing Time:** 50-100 minutes (target)
- **Transcription Completeness:** 100% (all 14 sections)
- **Gap Coverage:** Identify all missing entities
- **Integration Success:** All entities created and mapped

### Weekly
- **Videos Processed:** 3-5
- **Library Growth:** 10-25 new entities (tasks, tools, skills)
- **Time Efficiency:** 90-95% improvement vs manual
- **Quality:** All taxonomy sections complete

### Monthly
- **Total Videos:** 12-20
- **New Templates:** 40-100 task templates
- **Tool Library Growth:** 20-50 new tools
- **Coverage Improvement:** Track % increase in library completeness

---

## Troubleshooting

### Problem: Transcription Tool Fails

**Solutions:**
1. Try alternative tool (Google AI Studio → Transcribe AI → Whisper)
2. Split long video into segments
3. Download video and process locally with Whisper

### Problem: Unclear Taxonomy from Video

**Solutions:**
1. Re-watch relevant video sections
2. Use timestamps to locate specific mentions
3. Consult with domain expert
4. When uncertain, mark as "Review needed" in gap analysis

### Problem: Too Many New Entities

**Solutions:**
1. Prioritize HIGH priority gaps first
2. Create tools before tasks (tasks reference tools)
3. Batch similar entities together
4. Schedule integration across multiple days if needed

### Problem: Duplicate Entities

**Solutions:**
1. Always check existing libraries first
2. Use search in master CSVs
3. Compare naming conventions carefully
4. When in doubt, use existing entity ID

---

**End of Guide**

---

**Document Maintained By:** AI & Automation Team
**Last Updated:** 2025-11-25
**Status:** Active - Production Ready
**Next Review:** 2025-12-25 (1 month)
**Related Guide:** GDS-001 (Daily Task Processing)
