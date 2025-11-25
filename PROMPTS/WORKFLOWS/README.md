# Operational Workflows Prompts

**Category:** Business Process Prompts  
**Purpose:** Workflow automation and process management  
**Status:** Active

---

## Overview

Operational Workflows prompts handle business process automation, call organization, and workflow management.

---

## Prompts

### Call_Organizer_v2.md
**Version:** 2.0  
**Purpose:** Call organization framework (legacy)  
**Status:** Deprecated (maintained for reference, see `Archive/Call_Organizer_v2.md`)

### Call_Organizer_v3.md
**Version:** 3.1  
**Purpose:** Enhanced call organization with Remote Helpers employee & project directories  
**Status:** Archived (replaced by v4, see `Archive/Call_Organizer_v3.md`)  
**Features:**
- Embedded employee directory (32 employees)
- Embedded project directory (31+ projects)
- Call transcription processing
- Action item extraction
- Participant identification
- Project matching
- Workflow documentation

### Call_Organizer_v4.md
**Version:** 4.0  
**Purpose:** Entity-centric call organizer aligned with ENTITIES architecture (focus on `TASK_MANAGERS`)  
**Status:** Active  
**Features:**
- Entity-aware metadata (BUSINESSES, JOBS, TALENTS, TASK_MANAGERS, ANALYTICS)
- Task extraction in `Action + Object + Context` format aligned with LIBRARIES
- JSON-ready task and workflow candidates for TASK_MANAGERS
- Workflow pattern detection (Linear/Parallel/Conditional/Iterative/Event-Driven)
- Risks, decisions, metrics, and documentation gaps mapped to entities

### PROMPT_Document_Finished_Project.md
**Version:** 1.0
**Purpose:** Comprehensive completion report creation for finished projects
**Status:** Active
**Features:**
- 12-section completion report template
- Input requirements checklist
- Quality verification standards
- Business value analysis framework
- Lessons learned documentation
- Success metrics verification (Goal vs Actual)
- Cross-references to deliverables
- File naming conventions for reports

---

## Usage

- Use `Call_Organizer_v3.md` for processing call transcriptions and organizing business workflows
- Use `PROMPT_Document_Finished_Project.md` for creating standardized completion reports when project phases or milestones are finished

---

## Integration

- Integrates with MAIN PROMPT v4.md
- Links to LIBRARIES for tools and resources
- Connects to TASK_MANAGERS for task creation

---

**Last Updated:** 2025-11-16



