# Video Processing Phase System Overview

**Created:** 2025-11-21
**Status:** Active
**Location:** `TASK_MANAGERS/RESEARCHES/00_PHASES/`

---

## Overview

The Video Processing Phase System is a 7-phase workflow for extracting taxonomy elements from video transcriptions and integrating them into the LIBRARIES entity system.

**Total Phases:** 7
**Average Time per Video:** 2-4 hours (reduced from 15-20 hours with v3.2 automation)
**Success Rate:** 90-95% automation with v3.2 prompts

---

## Phase Flow

```
Phase 1: Transcription
    ↓
Phase 2: Naming (Optional)
    ↓
Phase 3: Initial Analysis
    ↓
Phase 4: Objects Extraction
    ↓
Phase 5: Gap Analysis
    ↓
Phase 6: Taxonomy Updates
    ↓
Phase 7: Reporting
```

---

## Quick Reference

| Phase | Name | Prompt | Input | Output | Time |
|-------|------|--------|-------|--------|------|
| 1 | Transcription | PMT-004 | Video URL | Video_XXX.md | 15-25 min |
| 2 | Naming | PMT-005 | Transcription | Professional title | 5 min |
| 3 | Analysis | PMT-006 | Transcription | Structured extraction | 30 min |
| 4 | Objects | PMT-007 | Analysis | Object inventory | 20 min |
| 5 | Gap Analysis | PMT-009 Part 1 | Objects | Gap report | 30 min |
| 6 | Updates | PMT-009 Part 2 | Gap report | Updated entities | 45 min |
| 7 | Reporting | PMT-009 Part 3 | All phases | Mapping report | 20 min |

---

## Phase Descriptions

### Phase 1: Transcription
**Objective:** Convert video content into structured markdown with embedded taxonomy

**Prompt:** `PMT-004_Video_Transcription_v4.1.md`
**Location:** `PROMPTS/Transcription/`

**Outputs:**
- Full timestamped transcription
- Metadata extraction
- Embedded taxonomy (Milestones, Tasks, Steps)
- Action verb categorization (7 categories)
- Tools matrix
- Objects/deliverables inventory

**Format Requirements:**
- MUST be markdown (NOT JSON)
- Include 7 action verb categories (A-G)
- Structured workflows with OBJECTIVE, STEPS, TOOLS

---

### Phase 2: Naming (Optional)
**Objective:** Generate professional business-appropriate title

**Prompt:** `PMT-005_Video_Naming_Alternatives.md`
**Location:** `PROMPTS/Transcription/`

**When to Use:**
- Casual or clickbait titles
- Multiple videos on same topic
- Corporate documentation needs

**Skip if:** Original title is already professional

---

### Phase 3: Initial Analysis
**Objective:** Extract and structure all taxonomy elements

**Prompt:** `PMT-006_Video_Analysis.md`
**Location:** `PROMPTS/Analysis/`

**Extraction Focus:**
- Tools (TOOL-{CATEGORY}-###)
- Workflows (WRF-###)
- Action verbs (ACT-###)
- Processes (PRO-###)
- Professions (PRF-###)
- Integration patterns

**Output:** Structured analysis document

---

### Phase 4: Objects Extraction
**Objective:** Identify deliverables and cross-reference with tools/actions

**Prompt:** `PMT-007_Objects_Library_Extraction.md`
**Location:** `PROMPTS/Analysis/`

**Categories:**
- Design objects (mockups, prototypes)
- Media objects (videos, images)
- Document objects (reports, specs)
- Data objects (datasets, databases)
- Communication objects (emails, messages)

**Output:** Object inventory with bidirectional cross-references

---

### Phase 5: Gap Analysis
**Objective:** Compare extracted elements against existing LIBRARIES

**Prompt:** `PMT-009_Taxonomy_Integration.md` (Part 1)
**Location:** `PROMPTS/Taxonomy_Integration/`

**Process:**
1. Inventory existing LIBRARIES entities
2. Compare with video extractions
3. Identify new elements
4. Identify updates to existing
5. Calculate coverage improvement

**Output:** `Video_XXX_Gap_Analysis.md`

---

### Phase 6: Taxonomy Updates
**Objective:** Create/update LIBRARIES entities and cross-references

**Prompt:** `PMT-009_Taxonomy_Integration.md` (Part 2)
**Location:** `PROMPTS/Taxonomy_Integration/`

**Updates:**
- Tools.json
- Actions_Master.json
- Objects.json
- Processes.json
- Skills.json
- Cross-reference files

**Output:** Updated entity files

---

### Phase 7: Reporting
**Objective:** Document integration results and impact

**Prompt:** `PMT-009_Taxonomy_Integration.md` (Part 3)
**Location:** `PROMPTS/Taxonomy_Integration/`

**Report Sections:**
- Executive summary
- Elements created/updated
- Coverage improvement metrics
- Cross-reference map
- Next steps

**Output:** `Video_XXX_Library_Mapping_Report.md`

---

## Phase Tracking

All videos tracked in:
- `02_TRANSCRIPTIONS/VIDEOS_INDEX.md` - Master catalog
- `01_QUEUE/Video_Queue_Tracker.md` - Processing queue

### Status Indicators
- ✅ Complete
- ⏳ In Progress
- ❌ Blocked
- N/A - Not Applicable

---

## Prompt Versions

### v2.0 (Deprecated)
- Videos 001, 002
- Basic extraction
- JSON output

### v3.0 (Current - Transcription)
- Added F. BROWSER/AGENTIC OPERATIONS category
- Improved workflow structure
- Markdown-only output

### v3.1 (Current - Full Stack)
- Added G. DATA OPERATIONS category
- Enhanced action verb categorization
- Improved object cross-referencing

### v4.1 (Latest - TASK_MANAGERS Integration)
- Integrated Milestones, Tasks, Steps extraction
- Enhanced department tagging
- Improved metadata structure

**Recommendation:** Use PMT-004 v4.1 for all new transcriptions

---

## Quality Standards

### Required Elements
- [ ] Timestamped transcription
- [ ] 7 action verb categories populated
- [ ] Tools matrix complete
- [ ] Workflows structured (OBJECTIVE, STEPS, TOOLS)
- [ ] Cross-references bidirectional
- [ ] Markdown format (NOT JSON)

### Success Criteria
- 90%+ extraction accuracy
- All new tools identified
- Coverage improvement quantified
- Cross-references validated

---

## Related Documentation

- [PMT-004: Video Transcription](../PROMPTS/Transcription/PMT-004_Video_Transcription_v4.1.md)
- [PMT-006: Video Analysis](../PROMPTS/Analysis/PMT-006_Video_Analysis.md)
- [PMT-009: Taxonomy Integration](../PROMPTS/Taxonomy_Integration/PMT-009_Taxonomy_Integration.md)
- [Videos Index](../02_TRANSCRIPTIONS/VIDEOS_INDEX.md)
- [Queue Tracker](../01_QUEUE/Video_Queue_Tracker.md)

---

*Phase System established: 2025-11-12*
*Consolidated into RESEARCHES: 2025-11-21*
