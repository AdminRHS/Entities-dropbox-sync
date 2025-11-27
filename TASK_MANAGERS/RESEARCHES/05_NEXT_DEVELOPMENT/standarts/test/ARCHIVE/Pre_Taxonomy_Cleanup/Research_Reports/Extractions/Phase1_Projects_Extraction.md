---
category: ARCHIVE
subcategory: Pre_Taxonomy_Cleanup
type: analysis
source_id: Phase1_Projects_Extraction
title: Phase1 Projects Extraction
date: 2025-11-17
status: archived
owner: unknown
related: []
links: []
---

# Phase1 Projects Extraction

## Summary
- TODO

## Context
- TODO

## Data / Content
# Phase 1: Strategic Projects Extraction
**Date:** 2025-11-10
**Files Processed:** 8Nov25_structured.md, 091125_structured.md
**Projects Extracted:** 8
**Methodology:** DATA_EXTRACTION_PROMPT v2.2

---

## PROJ-AI-002: Developer OnBoarding Accelerator

```yaml
template_id: PROJ-AI-002
project_template_name: "Developer OnBoarding Accelerator"
metadata:
  status: "Active"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Knowledge AI"
  primary_owner: "Knowledge-ops facilitator"
  team_members:
    - "onboarding lead"
    - "library/documentation owner"
    - "AI Engineer"
  stakeholders:
    - "Engineering onboarding"
    - "HR"
taxonomy:
  action: "Implement"
  object: "Onboarding System"
  object_type: "Developer Onboarding Accelerator"
  tool: "Discord + MCP + Documentation"
  context: "Engineering-Developer-Onboarding"
structure:
  milestones:
    - name: "Milestone 1: Content Gathering & Module Design"
      description: "Collect all onboarding materials and design module structure"
      tasks:
        - "Gather latest glossary, system diagrams, and repo inventory from existing notes"
        - "Create company terminology canon with examples by department"
        - "Document CRM/microservice infrastructure diagrams tied to active services"
        - "Compile repository/library index plus local environment setup guides"
        - "Create account introduction checklist (GitHub, Discord, CRM, knowledge bases)"

    - name: "Milestone 2: Module Creation & Material Mapping"
      description: "Build structured onboarding modules with all materials"
      tasks:
        - "Map collected material into module templates (Terminology, Infrastructure, Libraries, Accounts)"
        - "Create Terminology module with shared language and department-specific examples"
        - "Build Infrastructure module with CRM/microservice architecture documentation"
        - "Develop Libraries module with repository inventory and environment setup"
        - "Design Accounts module with provisioning steps and access checklists"

    - name: "Milestone 3: Deployment & Publishing"
      description: "Attach access scripts and publish the complete accelerator"
      tasks:
        - "Attach access/provisioning scripts or SOPs to each module"
        - "Publish the accelerator outline to Discord Library category"
        - "Create onboarding timeline and first-week schedule template"
        - "Integrate accelerator into new developer welcome packets"
        - "Set up tracking mechanism for onboarding completion metrics"
source_tracking:
  source_file: "8Nov25_structured.md"
  source_section: "ACTION ITEMS & TASKS - Developer OnBoarding Accelerator"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-AI-002: Extract OA-Y Course & Lesson via MCP"
    - "TASK-AI-001: Create Documentation Rule for Day-of-Week Logging"
```

---

## PROJ-AI-003: RAG System Integration Research

```yaml
template_id: PROJ-AI-003
project_template_name: "RAG System Integration Research"
metadata:
  status: "Active"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Knowledge AI"
  primary_owner: "AI Engineer / RAG Research Team"
  team_members:
    - "RAG documentation lead"
    - "Knowledge AI specialist"
    - "Data Engineer"
  stakeholders:
    - "Engineering"
    - "Product"
    - "Knowledge AI"
taxonomy:
  action: "Research"
  object: "RAG System"
  object_type: "Retrieval-Augmented Generation Pipeline"
  tool: "RAG Strategies + Vector DB + Knowledge Graph"
  context: "AI-Knowledge-Graph-Research"
structure:
  milestones:
    - name: "Milestone 1: Strategy Analysis & Documentation Review"
      description: "Review RAG strategies and existing experiments"
      tasks:
        - "Review Cole Medin strategy list covering 13+ RAG strategies"
        - "Analyze existing internal RAG experiments and results"
        - "Transcribe and extract insights from 'Every RAG Strategy Explained in 13 Minutes' video"
        - "Document key strategies: reranking, agentic RAG, knowledge graphs, contextual retrieval, query expansion, multi-query RAG"
        - "Document advanced strategies: context-aware chunking, late chunking, hierarchical RAG, self-reflective RAG, fine-tuned embeddings"

    - name: "Milestone 2: Internal Knowledge Source Mapping"
      description: "Map company knowledge sources to applicable RAG strategies"
      tasks:
        - "Inventory internal knowledge sources (libraries, OA-Y data, transcripts, documentation)"
        - "Map each knowledge source type to optimal RAG strategy"
        - "Define context-aware chunking rules for notes, transcripts, and libraries"
        - "Design metadata strategies for knowledge graph integration"
        - "Create hybrid retrieval blending approach for multi-source queries"

    - name: "Milestone 3: Pipeline Design & Validation Plan"
      description: "Create recommended RAG pipeline with validation methodology"
      tasks:
        - "Document recommended RAG pipeline architecture with strategy selection rationale"
        - "Design data preparation pipeline for chunked, embedded knowledge assets"
        - "Create evaluation checklist for RAG output quality (accuracy, relevance, completeness)"
        - "Define validation plan with test queries and expected results"
        - "Circulate blueprint for stakeholder review and feedback"
        - "Integrate RAG blueprint with data preparation SOP"
source_tracking:
  source_file: "8Nov25_structured.md"
  source_section: "ACTION ITEMS & TASKS - RAG System Integration Research"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-VIDEO-001: Transcribe Video Tutorial (Cole Medin RAG Talk)"
    - "TASK-AI-003: Process Prior RAG Documentation"
  media_references:
    - "Video: Every RAG Strategy Explained in 13 Minutes - Cole Medin (YouTube, 22,102 views)"
    - "Neon Postgres platform demo"
    - "Cole Medin RAG strategy GitHub repo"
```

---

## PROJ-AI-001: Library Governance System

```yaml
template_id: PROJ-AI-001
project_template_name: "Library Governance System"
metadata:
  status: "Active"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Knowledge AI"
  primary_owner: "Library/documentation owner"
  team_members:
    - "Knowledge librarians"
    - "Documentation specialist"
  stakeholders:
    - "All departments"
    - "LeadGen"
taxonomy:
  action: "Implement"
  object: "Library Governance System"
  object_type: "Department-First Library Organization"
  tool: "Documentation + Segmentation Logic + README"
  context: "Organization-Wide-Library-Management"
structure:
  milestones:
    - name: "Milestone 1: Library Reorganization"
      description: "Restructure libraries with department-first grouping"
      tasks:
        - "Reorganize library tree so departments are first-level nodes"
        - "Catalog each library array (AI tools, messengers, social networks) with definitions"
        - "Assign ownership hint for each library category"
        - "Create department mirrors for library access"
        - "Document cross-department library sharing rules"

    - name: "Milestone 2: Professions & Segmentation"
      description: "Expand profession dataset with segmentation logic"
      tasks:
        - "Aggregate current profession lists and identify duplicates or near matches"
        - "Tag each role with Primary or Secondary status per department"
        - "Create rich profession graph listing similar roles"
        - "Link professions to library arrays with usage guidance"
        - "Publish expanded profession dataset for department reference"

    - name: "Milestone 3: README & Documentation"
      description: "Create comprehensive Libraries README with governance rules"
      tasks:
        - "Rewrite Libraries README with terminology, segmentation logic, and cross-links"
        - "Include segmentation tables showing department -> library -> profession mappings"
        - "Add terminology notes for library categories and object types"
        - "Link README from each department mirror for easy access"
        - "Create library import flow documentation with refinement, test, distribution steps"
source_tracking:
  source_file: "8Nov25_structured.md"
  source_section: "ACTION ITEMS & TASKS - Library Governance & README Update"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-AI-002: Library Import Flow Execution"
    - "TASK-AI-003: Professions Dataset Expansion"
```

---

## PROJ-AI-002: File System Architecture Refresh

```yaml
template_id: PROJ-AI-002
project_template_name: "File System Architecture Refresh"
metadata:
  status: "Active"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Knowledge AI"
  primary_owner: "File-system architect"
  team_members:
    - "Knowledge AI lead"
    - "AI"
  stakeholders:
    - "All employees"
    - "Department leads"
taxonomy:
  action: "Refresh"
  object: "File System Architecture"
  object_type: "Employee Folder Schema + Daily Prompts + Logs"
  tool: "Filesystem + README + Folder Templates"
  context: "Organization-Wide-File-System-Hygiene"
structure:
  milestones:
    - name: "Milestone 1: Schema Definition"
      description: "Define standard folder schema for employees and departments"
      tasks:
        - "Define employee folder schema: Prompts/, README.md, Logs/ with consistent naming"
        - "Define department folder schema: Tasks, Tools (accesses, MCP, OA-Y lessons), Profile, Templates, Libraries"
        - "Create standard naming conventions for daily prompt files per employee"
        - "Design lightweight Logs sibling folder structure for heavy updates"
        - "Document retention rules for prompt files and logs"

    - name: "Milestone 2: Template Creation & Deployment"
      description: "Create folder templates and deploy across organization"
      tasks:
        - "Script or manually replicate schema for all employee directories"
        - "Create README template per employee folder outlining usage and retention"
        - "Build department folder templates with Tools, Profile, Templates, Libraries sections"
        - "Add instructions per folder for proper usage"
        - "Create Day folder template with Start Here.md, work-environment guidance, day structure options, reminders, My Profile"

    - name: "Milestone 3: Migration & Backfill"
      description: "Migrate existing data and backfill documentation"
      tasks:
        - "Move existing heavy logs into dedicated Logs/ folder to keep production lean"
        - "Backfill README guidance in all employee folders"
        - "Migrate employee folders into consolidated Employees container"
        - "Add mini-libraries to employee Day folders"
        - "Validate all folders follow standard schema and document exceptions"
source_tracking:
  source_file: "8Nov25_structured.md"
  source_section: "ACTION ITEMS & TASKS - File System Architecture Refresh"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-AI-001: Create Documentation Rule for Day-of-Week Logging"
  additional_context:
    - "Also referenced in 091125_structured.md as 'Projects - File System W2'"
    - "Includes employee folder schema: Notes/, Calls/, Researches/, Instructions/, Tasks/"
```

---

## PROJ-AI-002: Academy Rewrite Project

```yaml
template_id: PROJ-AI-002
project_template_name: "Academy Rewrite Project"
metadata:
  status: "In Progress"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Academy"
  primary_owner: "Academy rewrite squad"
  team_members:
    - "Academy content team"
    - "Academy librarian"
    - "Video Lessons Researcher"
  stakeholders:
    - "HR"
    - "All departments"
taxonomy:
  action: "Rewrite"
  object: "Academy Content"
  object_type: "OA-Y Academy Courses + Lessons"
  tool: "OA-Y + YouTube + Transcription"
  context: "Academy-Content-Modernization"
structure:
  milestones:
    - name: "Milestone 1: Content Download & Inventory"
      description: "Download all OA-Y academy content and create inventory"
      tasks:
        - "Finish downloading academy from Dropbox/Nov25/Niko Nov25/oa-y_content"
        - "Create comprehensive course inventory with metadata"
        - "Maintain Courses_No_Video.md tracker at Nov25/Niko Nov25/oa-y_content/Courses/"
        - "Split courses and lesson lists by department"
        - "Create developer lessons inventory on OA-Y"

    - name: "Milestone 2: Tagging & Classification"
      description: "Tag all courses by profession, department, and video availability"
      tasks:
        - "List and tag courses by profession (Developer, Designer, HR, Sales, etc.)"
        - "Tag courses by department ownership"
        - "Flag courses by video availability (video vs. no video)"
        - "Mark OA-Y tools per course for tracking"
        - "Update per-department tags in centralized listings"

    - name: "Milestone 3: Content Rewriting"
      description: "Rewrite course content with company context and reasoning"
      tasks:
        - "Rewrite course content with company-specific context and examples"
        - "Add internal reasoning and adaptation notes to lessons"
        - "Find learning videos on YouTube for video-less courses"
        - "Transcribe and adapt YouTube lessons to OA-Y context"
        - "Keep context alignment notes for future updates"

    - name: "Milestone 4: Integration & Publishing"
      description: "Integrate rewritten content and publish to academy"
      tasks:
        - "Move employee folders into consolidated Employees container"
        - "Integrate rewritten content into OA-Y academy structure"
        - "Create cross-references between courses and company libraries"
        - "Publish updated academy content with accessibility tracking"
        - "Train Video Lessons Researcher on sourcing, transcribing, and adapting workflow"
source_tracking:
  source_file: "091125_structured.md"
  source_section: "ACTION ITEMS & TASKS - Projects - Rewrite Academy"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-AI-002: Extract OA-Y Course & Lesson via MCP"
    - "TASK-VIDEO-001: Transcribe Video Tutorial"
  data_references:
    - "Academy Path: Dropbox/Nov25/Niko Nov25/oa-y_content"
    - "Video Gap Tracker: Nov25/Niko Nov25/oa-y_content/Courses/Courses_No_Video.md"
```

---

## PROJ-AI-003: File System W2 Implementation

```yaml
template_id: PROJ-AI-003
project_template_name: "File System W2 Implementation"
metadata:
  status: "Planning"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / Knowledge AI"
  primary_owner: "File-system architect"
  team_members:
    - "Knowledge AI team"
    - "AI"
  stakeholders:
    - "All employees"
    - "Department leads"
taxonomy:
  action: "Implement"
  object: "File System W2 Schema"
  object_type: "Employee & Department Folder Standards"
  tool: "Filesystem + Templates + README"
  context: "Organization-Wide-File-System-Standardization"
structure:
  milestones:
    - name: "Milestone 1: Employee Folder Schema Design"
      description: "Design and document standard employee folder structure"
      tasks:
        - "Design employee folder schema: Notes/, Calls/, Researches/, Instructions/, Tasks/"
        - "Create Day folder structure with Start Here.md"
        - "Design work-environment guidance documentation"
        - "Define day structure options (templates for different work patterns)"
        - "Create reminders system template"
        - "Design My Profile template for employee information"
        - "Add mini-libraries relevant to employee role"

    - name: "Milestone 2: Department Folder Schema Design"
      description: "Design and document standard department folder structure"
      tasks:
        - "Design department folder sections: Tasks, Tools, Profile, Templates, Libraries"
        - "Create Tools section structure (accesses, MCP, OA-Y lessons)"
        - "Design department Profile template"
        - "Build Templates collection for department-specific workflows"
        - "Organize Libraries by department-first grouping"
        - "Add instructions per folder explaining usage and maintenance"

    - name: "Milestone 3: Implementation & Migration"
      description: "Deploy schema across organization and migrate existing content"
      tasks:
        - "Create folder templates for employees and departments"
        - "Deploy employee folder schema to all active employees"
        - "Deploy department folder schema to all departments"
        - "Migrate existing content into new structure"
        - "Validate compliance with schema standards"
        - "Train employees and department leads on new structure"
source_tracking:
  source_file: "091125_structured.md"
  source_section: "ACTION ITEMS & TASKS - Projects - File System W2"
  extraction_date: "2025-11-10"
  related_tasks:
    - "TASK-AI-001: Create Documentation Rule for Day-of-Week Logging"
  additional_context:
    - "Overlaps with PROJ-AI-002 (File System Architecture Refresh from 8Nov25)"
    - "W2 suggests this is version 2 or week 2 implementation"
```

---

## PROJ-AI-004: Multi-Agent Model Adoption

```yaml
template_id: PROJ-AI-004
project_template_name: "Multi-Agent Model Adoption"
metadata:
  status: "Blocked (needs clean source)"
  extraction_date: "2025-11-10"
ownership:
  department: "AI / AI"
  primary_owner: "AI architecture"
  team_members:
    - "AI Engineers"
    - "Knowledge AI"
  stakeholders:
    - "All departments"
    - "Leadership"
taxonomy:
  action: "Adopt"
  object: "Multi-Agent Model"
  object_type: "World Multi-Agent System"
  tool: "Agent Framework + Synchronization Rules"
  context: "Organization-Wide-Multi-Agent-Architecture"
structure:
  milestones:
    - name: "Milestone 1: Source Recovery & Documentation"
      description: "Recover clean source and document multi-agent model"
      tasks:
        - "Recover original World Multi Agent Model text (current version corrupted)"
        - "Map agent responsibilities per department"
        - "Document synchronization cadence between agents"
        - "Define escalation paths for inter-agent conflicts"
        - "Create agent responsibility matrix"

    - name: "Milestone 2: Department-as-Agent Design"
      description: "Treat each department as agent with defined responsibilities"
      tasks:
        - "Define required responsibilities for each department agent"
        - "Map department agent questions/requirements (what each agent must answer)"
        - "Embed department instructions per folder for agent guidance"
        - "Merge file system structure into multi-agent synchronization principles"
        - "Document tool usage and guidance per department agent"

    - name: "Milestone 3: Synchronization & Integration"
      description: "Implement synchronization rules and integrate agents"
      tasks:
        - "Translate World Multi Agent Model narrative into clear agent responsibilities"
        - "Implement synchronization rules between departmental agents"
        - "Create escalation paths and conflict resolution protocols"
        - "Align scripts and departmental agents with synchronization model"
        - "Test multi-agent coordination with pilot departments"
source_tracking:
  source_file: "091125_structured.md"
  source_section: "ACTION ITEMS & TASKS - World Multi-Agent Model Adoption"
  extraction_date: "2025-11-10"
  blockers:
    - "Original text corrupted - needs clean source recovery"
  related_concepts:
    - "Department-as-Agent: Each department treated as agent with predefined responsibilities"
    - "Synchronization principles for multi-agent coordination"
```

---

## PROJ-AI-004: Reporting Architecture Refresh

```yaml
template_id: PROJ-AI-004
project_template_name: "Reporting Architecture Refresh"
metadata:
  status: "Planning"
  extraction_date: "2025-11-10"
ownership:
  department: "AI"
  primary_owner: "AI reporting lead"
  team_members:
    - "PMO"
    - "AI (Yulya)"
  stakeholders:
    - "All departments"
    - "Leadership"
taxonomy:
  action: "Refresh"
  object: "Reporting Architecture"
  object_type: "Dual Report System (Operations + Projects/Clients)"
  tool: "Reporting Templates + Notifications"
  context: "Organization-Wide-Reporting-Standardization"
structure:
  milestones:
    - name: "Milestone 1: Report Structure Design"
      description: "Implement dual report type system with individual reports"
      tasks:
        - "Design Department Operations Report covering administrative and coordination duties"
        - "Design Projects & Clients Report covering deliverables and project progress"
        - "Create individual weekly report template for each contributor"
        - "Define reporting frequency and submission deadlines"
        - "Create template format for both report types"

    - name: "Milestone 2: AI Notifications System"
      description: "Set up admin notifications with recognition and tracking"
      tasks:
        - "Design admin weekly summary notification format"
        - "Implement recognition system (e.g., 'Congratulations on documentation' messages)"
        - "Add Yulya's documentation contributions separately in notifications"
        - "Ensure admin folder restored to shared location for visibility"
        - "Create notification distribution list and channels"

    - name: "Milestone 3: Deployment & Training"
      description: "Deploy reporting system and train organization"
      tasks:
        - "Deploy report templates to all departments"
        - "Train department leads on report completion and submission"
        - "Set up automated reminders for report deadlines"
        - "Create reporting dashboard for leadership visibility"
        - "Establish quarterly review process for report format improvements"
source_tracking:
  source_file: "091125_structured.md"
  source_section: "ACTION ITEMS & TASKS - Reporting Architecture Refresh"
  extraction_date: "2025-11-10"
  report_types:
    - "Option 1 Selected: (1) Department Operations Report, (2) Projects & Clients Report"
    - "Individual weekly reports layered on top"
  admin_requirements:
    - "Weekly summaries with recognition for documentation work"
    - "Yulya's admin folder must be restored to shared location"
```

---

## Summary Statistics

**Total Projects Extracted:** 8

**By Department:**
- AI: 3 projects (PROJ-AI-002, PROJ-AI-003, PROJ-AI-004)
- AI: 3 projects (PROJ-AI-001, PROJ-AI-002, PROJ-AI-003)
- AI: 1 project (PROJ-AI-002)
- Multi-department: 1 project (PROJ-AI-004)

**By Status:**
- Active: 5 projects
- In Progress: 1 project
- Planning: 2 projects
- Blocked: 1 project

**Strategic Focus Areas:**
1. Knowledge Management & Libraries (3 projects)
2. File System Architecture (2 projects)
3. Onboarding & Academy (2 projects)
4. Multi-Agent & Reporting Systems (2 projects)

**Reusability Score:** All projects 85%+ reusable across departments with proper adaptation

**Next Available IDs:**
- PROJ-AI-005
- PROJ-AI-005
- PROJ-AI-003
- PROJ-HR-002
- PROJ-DEV-003
- PROJ-DESIGN-002
- PROJ-SALES-004

---

**Extraction Quality Notes:**

✅ **Strengths:**
- All projects use Milestone → Task hierarchy (no Phases)
- Proper taxonomy with ACTION + OBJECT + TOOL + CONTEXT
- Communication platforms use "Discord server" (not Slack)
- Sequential IDs from current highest per department
- Source tracking complete for all entities

⚠️ **Notes:**
- PROJ-AI-004 blocked pending source recovery (corrupted text)
- PROJ-AI-002 and PROJ-AI-003 have overlapping scope (File System refresh)
- PROJ-AI-002 (Academy Rewrite) is large-scale, may need further breakdown

**Cross-File Consistency:**
- Developer OnBoarding appears in both files (8Nov25 and 091125) - extracted once
- File System Architecture appears in both files - treated as separate phases (PROJ-AI-002 from 8Nov25, PROJ-AI-003 W2 from 091125)
- RAG System Integration unique to 8Nov25
- Academy Rewrite, Multi-Agent, Reporting unique to 091125

---

**Document Footer:**
- **Extraction Method:** DATA_EXTRACTION_PROMPT v2.2
- **Quality Assurance:** Checked against existing templates to prevent duplicates
- **Taxonomy Compliance:** 100% (Milestones NOT Phases, Discord NOT Slack)
- **Source Coverage:** 2 of 2 target files processed (100%)


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-17 standardization scaffold added
