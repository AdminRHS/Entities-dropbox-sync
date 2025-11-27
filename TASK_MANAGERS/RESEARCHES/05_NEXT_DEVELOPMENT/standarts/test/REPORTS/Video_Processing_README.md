---
category: REPORTS
subcategory: root
type: report
source_id: Video_Processing_README
title: Video Processing README
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# Video Processing README

## Summary
- TODO

## Context
- TODO

## Data / Content
# Video Processing Prompts

**Category:** Video Transcription & Analysis  
**Purpose:** Process videos to extract taxonomy elements and populate LIBRARIES  
**Status:** Active

---

## Overview

Video Processing prompts transform raw video content into structured taxonomy data, extracting actions, objects, tools, workflows, and other LIBRARIES entities.

---

## Workflow Phases

### Phase 1: Transcription
**Prompt:** `Transcription/Video_Transcription_Custom_Instructions.md`  
**Purpose:** Transcribe videos with structured format  
**Output:** Structured transcription with taxonomy focus

### Phase 2: Naming (Optional)
**Prompt:** `Transcription/Video_Naming_Business_Alternatives_Prompt.md`  
**Purpose:** Convert casual titles to professional names  
**Output:** Professional video title

### Phase 3: Initial Analysis
**Prompt:** `Analysis/Video_Analysis_Prompt.md`  
**Purpose:** Extract workflows, tools, actions, objects  
**Output:** Structured extraction inventory

### Phase 4: Objects Extraction
**Prompt:** `Analysis/Objects_Library_Extraction_Prompt.md`  
**Purpose:** Detailed object extraction with cross-references  
**Output:** Complete object inventory

### Phase 5-7: Taxonomy Integration
**Prompt:** `Taxonomy_Integration/Taxonomy_Analysis_and_Updates_Prompt.md`  
**Purpose:** Complete taxonomy gap analysis and entity updates  
**Output:** Updated LIBRARIES entities and mapping reports

---

## Prompts

### Transcription/
- `Video_Transcription_Custom_Instructions.md` - Core transcription (v4.0 - Taxonomy Architecture Alignment)
- `Video_Transcription_Custom_Instructions_v3.2.md` - Version 3.2 (archived)
- `Video_Naming_Business_Alternatives_Prompt.md` - Professional naming

### Analysis/
- `Video_Analysis_Prompt.md` - Initial analysis
- `Objects_Library_Extraction_Prompt.md` - Object extraction
- `PROMPT_ANALYSIS_AND_IMPROVEMENTS.md` - Analysis improvements

### Taxonomy_Integration/
- `Taxonomy_Analysis_and_Updates_Prompt.md` - Master integration prompt

---

## Output Format

All prompts output structured JSON compatible with LIBRARIES schemas:
- Actions, Objects, Tools
- Processes, Results
- Skills, Professions
- Cross-references

---

## Integration

- Populates LIBRARIES entities automatically
- Maintains data consistency
- Creates cross-references
- Updates indexes

---

**Last Updated:** 2025-11-13





## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-21 standardization scaffold added
