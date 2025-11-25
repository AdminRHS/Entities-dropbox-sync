# Video Processing Milestones - Master Reference
## 7 Milestones for WRF-VID-001 Workflow

**Document Type**: Master Reference / Index
**Workflow**: WRF-VID-001 (Video Processing Pipeline)
**Created**: 2025-11-23
**Purpose**: Lightweight reference linking to detailed prompts

---

## Overview

This master file provides lightweight milestone definitions for the Video Processing Pipeline workflow. Instead of duplicating full prompt content, each milestone links to the authoritative prompt in RESEARCHES/VIDEO_RESEARCHES.

**Design Principle**: Keep TASK_MANAGERS lightweight - link to detailed prompts rather than copying them

---

## Milestone Quick Reference

| ID | Name | Duration | Complexity | Prompt | Link |
|----|------|----------|------------|--------|------|
| MLT-VID-001 | Transcription | 15-25 min | Low | PMT-004 | [View Prompt](#mlt-vid-001-transcription) |
| MLT-VID-002 | Naming (Optional) | 5 min | Low | PMT-005 | [View Prompt](#mlt-vid-002-naming-optional) |
| MLT-VID-003 | Initial Analysis | 30-45 min | Medium | PMT-006 | [View Prompt](#mlt-vid-003-initial-analysis) |
| MLT-VID-004 | Objects Extraction | 20-30 min | Medium | PMT-007 | [View Prompt](#mlt-vid-004-objects-extraction) |
| MLT-VID-005 | Gap Analysis | 30-45 min | Medium-High | PMT-009 Part 1 | [View Prompt](#mlt-vid-005-gap-analysis) |
| MLT-VID-006 | Taxonomy Integration | 45-60 min | High | PMT-009 Part 2 | [View Prompt](#mlt-vid-006-taxonomy-integration) |
| MLT-VID-007 | Library Mapping | 20-30 min | Medium | PMT-009 Part 3 | [View Prompt](#mlt-vid-007-library-mapping) |

---

## MLT-VID-001: Transcription

**Objective**: Convert video to structured markdown with embedded taxonomy

**Input**: YouTube video URL
**Output**: `RESEARCHES/02_TRANSCRIPTIONS/Video_XXX.md`

**Prompt Reference**:
- **ID**: PMT-004
- **Name**: Video Transcription v4.1
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Transcription\PMT-004_Video_Transcription_v4.1.md`

**Key Deliverables**:
- Word-for-word transcription with timestamps
- Embedded Milestones, Tasks, Steps
- 7 action verb categories (A-G)
- Tools matrix, Objects inventory

**Dependencies**: None
**Next Milestone**: MLT-VID-002 (if title casual) OR MLT-VID-003 (if title professional)

---

## MLT-VID-002: Naming (Optional)

**Objective**: Generate professional business-appropriate title

**Input**: Transcription with casual/clickbait title
**Output**: Professional video title

**Prompt Reference**:
- **ID**: PMT-005
- **Name**: Video Naming Alternatives
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Transcription\PMT-005_Video_Naming_Alternatives.md`

**When to Use**: Casual titles, multiple similar videos, corporate docs
**Skip if**: Original title already professional

**Dependencies**: MLT-VID-001
**Next Milestone**: MLT-VID-003

---

## MLT-VID-003: Initial Analysis

**Objective**: Extract tools, workflows, and actions

**Input**: Transcription (Video_XXX.md)
**Output**: `RESEARCHES/03_ANALYSIS/Extractions/Video_XXX_Phase3_Analysis.md`

**Prompt Reference**:
- **ID**: PMT-006
- **Name**: Video Analysis
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Analysis\PMT-006_Video_Analysis.md`

**Key Deliverables**:
- Tools inventory (TOL-###)
- Workflows documentation (WRF-###)
- Action verbs (ACT-###)
- Integration patterns
- Business value propositions

**Dependencies**: MLT-VID-001 (or MLT-VID-002)
**Next Milestone**: MLT-VID-004

---

## MLT-VID-004: Objects Extraction

**Objective**: Identify deliverables, outputs, tangible items

**Input**: Transcription + Phase 3 Analysis
**Output**: `RESEARCHES/03_ANALYSIS/Extractions/Video_XXX_Phase4_Objects.md`

**Prompt Reference**:
- **ID**: PMT-007
- **Name**: Objects Library Extraction
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Analysis\PMT-007_Objects_Library_Extraction.md`

**Key Deliverables**:
- Object inventory with types (OBJ-###)
- Object categories (Data, Technical, Configuration, Platform)
- Object relationship matrix
- Action + Object = Task mapping

**Dependencies**: MLT-VID-003
**Next Milestone**: MLT-VID-005

---

## MLT-VID-005: Gap Analysis

**Objective**: Identify what exists vs. what's missing in LIBRARIES

**Input**: Phase 3 + Phase 4 outputs
**Output**: `RESEARCHES/03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

**Prompt Reference**:
- **ID**: PMT-009 (Part 1)
- **Name**: Taxonomy Integration - Gap Analysis
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Taxonomy_Integration\PMT-009_Taxonomy_Integration.md`

**Key Deliverables**:
- Tools library gaps
- TASK_MANAGERS gaps (milestones, tasks, steps)
- Coverage % (before/after)
- Priority assignments (CRITICAL/HIGH/MEDIUM/LOW)
- ID mapping recommendations

**Dependencies**: MLT-VID-003, MLT-VID-004
**Next Milestone**: MLT-VID-006

---

## MLT-VID-006: Taxonomy Integration

**Objective**: Create JSON files and integrate into LIBRARIES/TASK_MANAGERS

**Input**: Gap Analysis report
**Output**: New JSON files in LIBRARIES and TASK_MANAGERS

**Prompt Reference**:
- **ID**: PMT-009 (Part 2)
- **Name**: Taxonomy Integration - Implementation
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Taxonomy_Integration\PMT-009_Taxonomy_Integration.md`

**Key Actions**:
- Create tool JSONs (TOL-###)
- Create workflow JSONs (WRF-###)
- Create milestone templates (MLT-###)
- Create task templates (TST-###)
- Create object JSONs (OBJ-###)
- Establish cross-references

**Dependencies**: MLT-VID-005
**Next Milestone**: MLT-VID-007

---

## MLT-VID-007: Library Mapping

**Objective**: Document integration results and create mapping report

**Input**: Integration outputs from MLT-VID-006
**Output**: `RESEARCHES/03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md`

**Prompt Reference**:
- **ID**: PMT-009 (Part 3)
- **Name**: Taxonomy Integration - Mapping Report
- **Location**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Taxonomy_Integration\PMT-009_Taxonomy_Integration.md`

**Key Deliverables**:
- Tool → Workflow → Task hierarchy
- Cross-reference integration matrix
- Coverage & gap resolution summary
- Quality metrics (target: >= 95%)
- File locations reference

**Dependencies**: MLT-VID-006
**Next Step**: Update VIDEO_METADATA_TRACKER.md

---

## Prompt Locations Summary

All detailed prompts are stored in:
`C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\Video_Processing\`

```
Video_Processing/
├── Transcription/
│   ├── PMT-004_Video_Transcription_v4.1.md        → MLT-VID-001
│   └── PMT-005_Video_Naming_Alternatives.md       → MLT-VID-002
│
├── Analysis/
│   ├── PMT-006_Video_Analysis.md                  → MLT-VID-003
│   ├── PMT-007_Objects_Library_Extraction.md      → MLT-VID-004
│   ├── PMT-008_Video_Analysis_Improvements.md
│   └── PMT-071_Actions_Library_Extraction.md
│
├── Taxonomy_Integration/
│   └── PMT-009_Taxonomy_Integration.md            → MLT-VID-005, 006, 007
│
└── Workflows/
    ├── PMT-010_Complete_Workflow_Full.md
    ├── PMT-011_Complete_Workflow_Short.md
    ├── PMT-012_Transcript_Processing_Workflow.md
    └── PMT-090_YouTube_Video_Processing.md
```

---

## Usage Instructions

### For New Video Processing

1. **Start with MLT-VID-001**: Use PMT-004 prompt from RESEARCHES
2. **Progress sequentially**: Each milestone depends on previous
3. **Create outputs in VIDEO_RESEARCHES**: Follow folder structure
4. **Link back to this master**: Reference milestone IDs in your outputs
5. **Complete MLT-VID-007**: Final mapping report
6. **Update tracker**: Mark video as complete in VIDEO_METADATA_TRACKER.md

### For Existing Video (Video_022 Example)

- ✅ MLT-VID-001: Complete (`Video_022.md`)
- ⏭️ MLT-VID-002: Skipped (title was professional)
- ✅ MLT-VID-003: Complete (`Video_022_Phase3_Analysis.md`)
- ✅ MLT-VID-004: Complete (`Video_022_Phase4_Objects.md`)
- ✅ MLT-VID-005: Complete (`Video_022_Gap_Analysis.md`)
- ⏳ MLT-VID-006: Pending (integration phase)
- ✅ MLT-VID-007: Complete (`Video_022_Library_Mapping_Report.md`)

---

## Integration Benefits

**Lightweight TASK_MANAGERS**:
- Milestones defined here (metadata only)
- Detailed prompts stay in RESEARCHES (authoritative source)
- No duplication = easier maintenance

**Clear Workflow Structure**:
- 7 milestones with clear dependencies
- Links to actual prompts
- Output locations specified

**Cross-Entity Sync**:
- TASK_MANAGERS: Workflow structure
- RESEARCHES: Detailed prompts and outputs
- TAXONOMY: ID registry and standards
- LIBRARIES: Final integration destination

---

## Related Documents

- **Workflow Definition**: `TASK_MANAGERS/TSM-006_Workflows/WRF-VID-001_Video_Processing_Pipeline.md`
- **Phase System Overview**: `TASK_MANAGERS/RESEARCHES/00_PHASES/Phase_System_Overview.md`
- **Taxonomy Registry**: `TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`
- **Video Tracker**: `TASK_MANAGERS/RESEARCHES/VIDEO_METADATA_TRACKER.md`

---

*Master File Created: 2025-11-23*
*Purpose: Lightweight milestone reference with links to authoritative prompts*
*Design: Keep TASK_MANAGERS light, link to RESEARCHES for details*
