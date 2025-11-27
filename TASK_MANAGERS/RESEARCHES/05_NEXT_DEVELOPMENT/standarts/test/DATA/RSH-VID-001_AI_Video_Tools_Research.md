---
category: DATA
subcategory: root
type: analysis
source_id: RSH-VID-001_AI_Video_Tools_Research
title: RSH-VID-001 AI Video Tools Research
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# RSH-VID-001 AI Video Tools Research

## Summary
- TODO

## Context
- TODO

## Data / Content
# RSH-VID-001: AI Video Tools Research

**Entity:** RESEARCHES / VIDEO_RESEARCHES
**ID:** RSH-VID-001
**Department(s):** Video (VID); AI Department (AID)
**Status:** Pending
**Owner:** AI Researcher / Video Production Specialist
**Created:** 2025-11-20
**Last Updated:** 2025-11-20

---

## Objective

Design and execute a structured research program to complete and maintain taxonomy-aligned documentation for key AI video tools (Hedra, HeyGen, Synthesia, RunwayML, Vozo AI, Hailo), using the existing video discovery and extraction pipelines.

The research should:
- Close all known documentation gaps for these tools in `ENTITIES/LIBRARIES/Tools/`.
- Produce a comparison and decision-support layer for subscriptions and renewals.
- Establish a repeatable pattern for future AI video tools research under `VIDEO_RESEARCHES`.

---

## Scope

- **Primary focus:**
  - Video generation and video production tools with strong relevance to Remote Helpers workflows.
- **Tools in scope (initial batch):**
  - Hedra, HeyGen, Synthesia, RunwayML, Vozo AI, Hailo.
- **Departments:**
  - **Video (VID):** production workflows, video content output.
  - **AI Department (AID):** research methodology, pipeline automation.
- **Out of scope (for this first iteration):**
  - Non-video-first tools (general LLM platforms, pure audio/voice tools).
  - Deep implementation of billing/finance beyond high-level subscription recommendations.

---

## Background & Context

This research corresponds to the **“AI Video Tools research (Pending)”** entry in:
- `ENTITIES/REPORTS/Taxonomy/RESEARCHES_Department_Distribution.md` (Video – 1 pending entity).

It operationalizes the existing task template:
- `ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/TST-045_Research_AI_Video_Tools.json`

and builds on the methodology defined in:
- `ENTITIES/REPORTS/Videos/Video_Discovery_Pipeline.md`

These inputs together define:
- Discovery, evaluation, and pipeline mechanics for AI video-related content.
- A concrete task workflow for filling all missing fields in 6 tool JSONs.
- Strategic alignment with initiatives like **Open-Source Video Generation (WAN 2.2)** and **Video Production Optimization**.

---

## Sources

- **Task Template:**
  - `TSM-003_Task_Templates/TST-045_Research_AI_Video_Tools.json`  
    - Defines steps, success criteria, dependencies, ROI metrics.

- **Pipeline & Methodology:**
  - `REPORTS/Videos/Video_Discovery_Pipeline.md`  
    - Discovery and scoring system for candidate videos.  
    - Transcription and extraction workflow (v3.2 prompt).  
    - Integration and update requirements for taxonomy.

- **Existing Video Analyses:**
  - `REPORTS/Videos/Video_001.md` … `Video_016.md` (where relevant).  
  - `REPORTS/Videos/VIDEOS_INDEX.md`.

- **Libraries:**
  - `LIBRARIES/Tools/*.json` (Hedra, HeyGen, Synthesia, RunwayML, Vozo AI, Hailo).

---

## Research Questions

1. **Coverage & Completeness**  
   - Which fields and dimensions are currently missing across the 6 AI video tools?  
   - How do those gaps map to decisions the Video and AI departments need to make?

2. **Comparative Positioning**  
   - How do Hedra, HeyGen, Synthesia, RunwayML, Vozo AI, and Hailo compare on:  
     - Features, workflows, integration options, pricing, and quality.  
   - Where does WAN 2.2 (open-source) fit versus commercial tools?

3. **Strategic Fit & Subscription Decisions**  
   - Which tools should be renewed, paused, or newly adopted?  
   - What are the expected ROI and productivity gains for each tool?

4. **Workflow & Taxonomy Impact**  
   - Which new actions, objects, and workflows must be added to LIBRARIES?  
   - How should future AI video tool research be standardized under `VIDEO_RESEARCHES`?

---

## Methodology

This research follows the process encoded in **TST-045** and the **Video Discovery Pipeline**:

1. **Requirements & Gap Review**  
   - Load `Research_ToDo_2025-11-W47_AI_Video_Tools.json` and existing tool JSONs.  
   - Enumerate all missing fields and TBD sections per tool.

2. **Video Discovery & Evaluation**  
   - Use the Video Discovery Pipeline to identify and score 8–12 relevant videos.  
   - Prioritize those with the strongest taxonomy value and strategic fit.

3. **Deep Dive & Note Taking**  
   - Watch top-scored videos (3–5 per tool) and capture structured notes:  
     - Capabilities, workflows, pricing, integration patterns, limitations.

4. **Supplementary Web Research**  
   - Fill remaining gaps through official docs, product pages, and trusted write-ups.

5. **Comparison Matrix Creation**  
   - Build a matrix (spreadsheet / markdown) comparing 6 tools across ≥10 dimensions.

6. **Tool JSON Updates**  
   - Update each tool JSON file to remove all TBD values and empty arrays.  
   - Validate JSON syntax and cross-entity references.

7. **Integration Workflows & Recommendations**  
   - Document integration workflows between tools and the Remote Helpers stack.  
   - Produce clear recommendations for renewals/adoptions (Vozo AI, Hailo, Synthesia, etc.).

8. **Summary & Indexing**  
   - Produce a concise summary report for stakeholders.  
   - Register this research under `TASK_MANAGERS/RESEARCHES/INDEXES/` and update any relevant distributions.

---

## Planned Outputs

1. **Updated Tool JSON Files**  
   - 6 complete tool definitions with no TBDs and fully populated arrays.

2. **Comparison & Decision Layer**  
   - One comparison matrix file (spreadsheet or markdown).  
   - Clear adoption/renewal decisions per tool with rationale.

3. **Workflow & Integration Notes**  
   - Documented integration workflows referencing Video Discovery and extraction processes.

4. **Index & Taxonomy Updates**  
   - Entries in `TASK_MANAGERS/RESEARCHES/INDEXES/VIDEO_RESEARCHES_Index.md` (to be created).  
   - Updates to any existing coverage gap or department distribution documents.

---

## Links to Related Entities

- **TASK_MANAGERS:**
  - `TSM-003_Task_Templates/TST-045_Research_AI_Video_Tools.json` (template driving execution).  
  - Future: one or more concrete tasks instantiated from this template.

- **LIBRARIES:**
  - `LIBRARIES/Tools/` entries for all 6 tools.  
  - Any related Actions/Objects in Responsibilities libraries.

- **REPORTS:**
  - `REPORTS/Videos/Video_Discovery_Pipeline.md`  
  - `REPORTS/Videos/Video_XXX.md` series where these tools are discussed.

---

## Status & Next Steps

- **Current Status:** Pending (research not yet executed; this file defines the container and methodology).

- **Immediate Next Steps:**
  1. Confirm ownership (assign specific AI researcher / video specialist).  
  2. Instantiate a concrete TASK_MANAGERS task from `TST-045` referencing `RSH-VID-001`.  
  3. Run the Video Discovery Pipeline for the 6 tools and populate an initial candidate video list.

- **Planned Review Date:** 2025-11-27  
  (First status check and partial results expected.)


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
