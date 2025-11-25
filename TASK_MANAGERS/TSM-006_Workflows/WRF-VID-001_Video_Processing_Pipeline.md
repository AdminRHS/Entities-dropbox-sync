# WRF-VID-001: Video Processing Pipeline Workflow
## 7-Milestone System for Video Taxonomy Extraction

**Workflow ID**: WRF-VID-001
**Workflow Name**: Video Processing Pipeline
**Department**: VID (Video), AID (AI Integration)
**Category**: Research & Taxonomy Integration
**Created**: 2025-11-23
**Status**: Active

---

## Overview

The Video Processing Pipeline is a systematic 7-milestone workflow for extracting taxonomy elements from video content and integrating them into the ENTITIES ecosystem (LIBRARIES, TASK_MANAGERS, etc.).

**Purpose**: Transform unstructured video content into structured, reusable taxonomy components

**Input**: YouTube video URL
**Output**: Integrated taxonomy entries (Tools, Workflows, Tasks, Actions, Objects)
**Average Duration**: 2-4 hours per video (with automation)
**Complexity**: Medium to High

---

## Workflow Architecture

```
MLT-VID-001: Transcription
    ↓
MLT-VID-002: Naming (Optional)
    ↓
MLT-VID-003: Initial Analysis
    ↓
MLT-VID-004: Objects Extraction
    ↓
MLT-VID-005: Gap Analysis
    ↓
MLT-VID-006: Taxonomy Integration
    ↓
MLT-VID-007: Library Mapping
```

---

## Success Metrics

- **Automation Rate**: 90-95% with optimized prompts
- **Coverage**: 100% of tools, workflows, and actions identified
- **Integration Quality**: 95%+ cross-reference accuracy
- **Time Reduction**: From 15-20 hours (manual) to 2-4 hours (automated)

---

## Milestones

### MLT-VID-001: Transcription

**Objective**: Convert video content into structured markdown with embedded taxonomy

**Duration**: 15-25 minutes
**Complexity**: Low (automated)
**Dependencies**: None
**Output**: `02_TRANSCRIPTIONS/Video_XXX.md`

**Prompt**: PMT-004 (Video Transcription v4.1)
**Prompt Location**: `PROMPTS/PMT-004_Video_Transcription_v4.1.md`

**Deliverables**:
- Full timestamped transcription
- Metadata extraction
- Embedded taxonomy (Milestones, Tasks, Steps)
- Action verb categorization (7 categories A-G)
- Tools matrix
- Objects/deliverables inventory

**Format**: Markdown (NOT JSON)

**Next Milestone**: MLT-VID-002 (if title needs refinement) OR MLT-VID-003 (if title is professional)

---

### MLT-VID-002: Naming (Optional)

**Objective**: Generate professional business-appropriate title

**Duration**: 5 minutes
**Complexity**: Low
**Dependencies**: MLT-VID-001
**Output**: Professional video title

**Prompt**: PMT-005 (Video Naming Alternatives)
**Prompt Location**: `PROMPTS/PMT-005_Video_Naming_Alternatives.md`

**When to Use**:
- Casual or clickbait original titles
- Multiple videos on same topic requiring differentiation
- Corporate documentation needs

**Skip if**: Original title is already professional

**Next Milestone**: MLT-VID-003

---

### MLT-VID-003: Initial Analysis

**Objective**: Extract and structure all taxonomy elements (tools, workflows, actions)

**Duration**: 30-45 minutes
**Complexity**: Medium
**Dependencies**: MLT-VID-001 (or MLT-VID-002)
**Output**: `03_ANALYSIS/Extractions/Video_XXX_Phase3_Analysis.md`

**Prompt**: PMT-006 (Video Analysis)
**Prompt Location**: `PROMPTS/PMT-006_Video_Analysis.md`

**Extraction Focus**:
- **Tools** (TOOL-{CATEGORY}-###)
- **Workflows** (WRF-###)
- **Action verbs** (ACT-###)
- **Integration patterns**
- **Business concepts**
- **Use cases**

**Deliverables**:
- Complete tools inventory with categories, vendors, features
- Workflow documentation with milestones, tasks, steps
- Action verb categorization across 7 categories
- Integration patterns identified
- Business value propositions
- Timestamps for all references

**Next Milestone**: MLT-VID-004

---

### MLT-VID-004: Objects Extraction

**Objective**: Identify and document all objects (deliverables, outputs, tangible items)

**Duration**: 20-30 minutes
**Complexity**: Medium
**Dependencies**: MLT-VID-003
**Output**: `03_ANALYSIS/Extractions/Video_XXX_Phase4_Objects.md`

**Prompt**: PMT-007 (Objects Library Extraction)
**Prompt Location**: `PROMPTS/PMT-007_Objects_Library_Extraction.md`

**Extraction Focus**:
- **Object types** and variations
- **Object categories** (Data, Technical, Configuration, Platform)
- **Action + Object = Task** relationships
- **Tool-Object relationships**
- **Profession-Object assignments**

**Deliverables**:
- Object inventory with types and categories
- Object relationship matrix
- Object-to-task mapping
- Complexity and time estimates
- Department distribution
- Cross-references with tools and workflows

**Next Milestone**: MLT-VID-005

---

### MLT-VID-005: Gap Analysis

**Objective**: Identify what exists vs. what's missing in LIBRARIES and TASK_MANAGERS

**Duration**: 30-45 minutes
**Complexity**: Medium to High
**Dependencies**: MLT-VID-003, MLT-VID-004
**Output**: `03_ANALYSIS/Gap_Analysis/Video_XXX_Gap_Analysis.md`

**Prompt**: PMT-009 Part 1 (Taxonomy Integration - Gap Analysis)
**Prompt Location**: `PROMPTS/PMT-009_Taxonomy_Integration.md`

**Analysis Focus**:
- Tools library gaps
- TASK_MANAGERS gaps (milestones, tasks, steps)
- Actions library gaps
- Objects library gaps
- ID conflict analysis
- Coverage metrics (before/after)

**Deliverables**:
- Complete gap inventory
- Priority assignments (CRITICAL, HIGH, MEDIUM, LOW)
- Coverage % calculations
- ID mapping recommendations (e.g., MLS-### → MLT-###)
- Recommended file paths for new entities
- Integration complexity assessment

**Next Milestone**: MLT-VID-006

---

### MLT-VID-006: Taxonomy Integration

**Objective**: Create JSON files and integrate findings into LIBRARIES and TASK_MANAGERS

**Duration**: 45-60 minutes
**Complexity**: High
**Dependencies**: MLT-VID-005
**Output**: New JSON files in LIBRARIES and TASK_MANAGERS

**Prompt**: PMT-009 Part 2 (Taxonomy Integration - Implementation)
**Prompt Location**: `PROMPTS/PMT-009_Taxonomy_Integration.md`

**Integration Actions**:
1. Create tool JSON files (LIBRARIES/LBS_003_Tools/)
2. Create workflow JSON files (TASK_MANAGERS/TSM-001_Templates/Workflows/)
3. Create milestone templates (TASK_MANAGERS/TSM-001_Templates/Milestones/)
4. Create task templates (TASK_MANAGERS/TSM-002_Task_Templates/)
5. Create step templates
6. Create object JSON files (LIBRARIES/Responsibilities/Objects/)
7. Verify/create action entries (LIBRARIES/LBS_002_Actions/)
8. Establish all cross-references

**Deliverables**:
- Tool JSON files (TOL-###)
- Workflow JSON files (WRF-###)
- Milestone templates (MLT-###)
- Task templates (TST-###)
- Step templates (STP-###)
- Object JSON files (OBJ-###)
- Updated master lists and registries

**Verification**:
- Cross-references validated
- IDs consistent with ISO code registry
- File paths correct
- JSON structure valid

**Next Milestone**: MLT-VID-007

---

### MLT-VID-007: Library Mapping

**Objective**: Document integration results and create comprehensive mapping report

**Duration**: 20-30 minutes
**Complexity**: Medium
**Dependencies**: MLT-VID-006
**Output**: `03_ANALYSIS/Library_Mapping/Video_XXX_Library_Mapping_Report.md`

**Prompt**: PMT-009 Part 3 (Taxonomy Integration - Mapping Report)
**Prompt Location**: `PROMPTS/PMT-009_Taxonomy_Integration.md`

**Mapping Focus**:
- Tool → Workflow → Task hierarchy
- Tool → Object relationships
- Action → Object → Task relationships
- Department distribution
- Coverage metrics (final)
- Integration verification

**Deliverables**:
- Complete library mapping report
- Cross-reference integration matrix
- Tool-Workflow-Task hierarchy visualization
- Coverage & gap resolution summary
- Quality metrics (processing success %)
- File locations reference
- Business value documentation

**Final Verification**:
- All entities created
- All cross-references established
- Master lists updated
- Quality >= 95%

**Next Step**: Update VIDEO_METADATA_TRACKER.md with completion status

---

## Workflow Summary Table

| Milestone ID | Milestone Name | Duration | Complexity | Prompt | Output Location |
|--------------|----------------|----------|------------|--------|-----------------|
| MLT-VID-001 | Transcription | 15-25 min | Low | PMT-004 | `02_TRANSCRIPTIONS/` |
| MLT-VID-002 | Naming (Optional) | 5 min | Low | PMT-005 | Title update |
| MLT-VID-003 | Initial Analysis | 30-45 min | Medium | PMT-006 | `03_ANALYSIS/Extractions/` |
| MLT-VID-004 | Objects Extraction | 20-30 min | Medium | PMT-007 | `03_ANALYSIS/Extractions/` |
| MLT-VID-005 | Gap Analysis | 30-45 min | Medium-High | PMT-009 Part 1 | `03_ANALYSIS/Gap_Analysis/` |
| MLT-VID-006 | Taxonomy Integration | 45-60 min | High | PMT-009 Part 2 | `LIBRARIES/`, `TASK_MANAGERS/` |
| MLT-VID-007 | Library Mapping | 20-30 min | Medium | PMT-009 Part 3 | `03_ANALYSIS/Library_Mapping/` |

**Total Duration**: 2-4 hours (depending on video complexity and automation level)

---

## Prompt Reference Quick Links

| Prompt ID | Prompt Name | Usage | Location |
|-----------|-------------|-------|----------|
| PMT-004 | Video Transcription v4.1 | MLT-VID-001 | `PROMPTS/` |
| PMT-005 | Video Naming Alternatives | MLT-VID-002 | `PROMPTS/` |
| PMT-006 | Video Analysis | MLT-VID-003 | `PROMPTS/` |
| PMT-007 | Objects Library Extraction | MLT-VID-004 | `PROMPTS/` |
| PMT-009 | Taxonomy Integration (Parts 1-3) | MLT-VID-005, 006, 007 | `PROMPTS/` |

**Additional Prompts** (supporting workflows):
- PMT-008: Video Analysis Improvements
- PMT-071: Actions Library Extraction
- PMT-010: Complete Workflow Full
- PMT-011: Complete Workflow Short
- PMT-012: Transcript Processing Workflow
- PMT-090: YouTube Video Processing

---

## Example: Video_022 Processing Results

**Video**: "This AI Agent Will DO Your Work For You! (Browse AI)"
**Processing Date**: 2025-11-23
**Duration**: 10:53

### Results Summary

| Milestone | Status | Output File | Entities Extracted |
|-----------|--------|-------------|--------------------|
| MLT-VID-001 | ✅ Complete | Video_022.md | Base transcription |
| MLT-VID-002 | ⏭️ Skipped | N/A | Title was professional |
| MLT-VID-003 | ✅ Complete | Video_022_Phase3_Analysis.md | 3 tools, 1 workflow, 27 actions |
| MLT-VID-004 | ✅ Complete | Video_022_Phase4_Objects.md | 8 objects |
| MLT-VID-005 | ✅ Complete | Video_022_Gap_Analysis.md | All gaps identified |
| MLT-VID-006 | ⏳ Pending | N/A | ~42 JSON files to create |
| MLT-VID-007 | ✅ Complete | Video_022_Library_Mapping_Report.md | Complete mapping |

**Entities Identified**:
- **3 Tools**: Browse AI (TOL-AUT-###), Google Sheets (TOL-BIZ-###), Chrome Extension
- **1 Workflow**: Automated Web Scraping Pipeline (WRF-AUT-001)
  - 3 Milestones (MLT-029, MLT-030, MLT-031)
  - 8 Tasks (TST-### × 8)
  - 16 Steps (STP-### × 16)
- **27 Actions**: Across 7 categories (A, B, C, F, G)
- **8 Objects**: Across 4 categories (Data, Technical, Configuration, Platform)

**Coverage Improvement**: 0% → 100% (after MLT-VID-006 integration)
**Processing Quality**: 95%
**Integration Readiness**: 100%

---

## Integration with RESEARCHES Taxonomy

This workflow is stored in:
- **TASK_MANAGERS**: `TSM-006_Workflows/WRF-VID-001_Video_Processing_Pipeline.md` (this file)
- **RESEARCHES**: `00_PHASES/Phase_System_Overview.md` (detailed docs)

**Relationship**:
- TASK_MANAGERS provides the lightweight workflow structure
- RESEARCHES provides detailed prompts and processing outputs
- Both reference the same PMT-### prompts
- Cross-entity integration via TAXONOMY registry

---

## Quality Standards

### Completion Criteria (Per Milestone)

**MLT-VID-001**: Transcription includes all 7 action categories, tools matrix, objects inventory
**MLT-VID-003**: All tools have vendor, category, features, timestamps
**MLT-VID-004**: All objects have category, type, cross-references
**MLT-VID-005**: Gap coverage % calculated, priorities assigned
**MLT-VID-006**: All JSON files created, cross-references validated
**MLT-VID-007**: Integration matrix complete, quality >= 95%

### File Naming Conventions

- Transcriptions: `Video_XXX.md`
- Analysis: `Video_XXX_Phase#_[Name].md`
- Final outputs: `Video_XXX_[Type]_Report.md`

### ID Assignment Rules

- Follow `TAXONOMY/TAX-001_Libraries/Libraries_ISO_Code_Registry.md`
- Use sequential numbering within categories
- Verify no ID conflicts before assignment
- Document all mappings (e.g., video-specific MLS-### → template MLT-###)

---

## Next Steps After Workflow Completion

1. **Update VIDEO_METADATA_TRACKER.md** with completion status
2. **Update Master Lists** in TAXONOMY registries
3. **Verify Cross-References** using validation scripts
4. **Archive Work Files** to appropriate ARCHIVE folders
5. **Update Coverage Metrics** in taxonomy dashboards

---

## Related Workflows

- **WRF-AUT-001**: Automated Web Scraping Pipeline (extracted from Video_022)
- **WRF-###**: Future video-extracted workflows
- **PMT-070**: Daily Reports Processing (different domain)

---

*Workflow Created: 2025-11-23*
*Status: Active - Production Ready*
*Department: VID, AID*
*Entity Location: TASK_MANAGERS/TSM-006_Workflows/*
