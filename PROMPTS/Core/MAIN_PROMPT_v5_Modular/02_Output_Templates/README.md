# 02_Output_Templates - Meeting Output Section Templates

**Purpose:** 21 individual templates for structuring meeting analysis output, each with relevant library integrations.

**Files in this folder:** 22 (21 templates + this README)
**Update Frequency:** As needed when output format changes

---

## Overview

Each output template file provides:
- **Purpose:** What this section captures
- **Integrated Libraries:** Which LIBRARIES entities are used
- **Output Template:** Markdown format with placeholders
- **Recognition Rules:** What to look for in transcripts
- **Examples:** Realistic examples with real entity IDs
- **Validation Checklist:** Quality checks

---

## Templates by Library Integration Level

### Heavily Integrated Templates (⭐⭐⭐)

These templates make extensive use of LIBRARIES entities:

**03_Action_Items_Tasks.md**
- **Libraries:** Actions, Objects, Skills, Responsibilities
- **Purpose:** Document action items with structured task creation

**04_Projects_Features.md**
- **Libraries:** Products, Services
- **Purpose:** Track project discussions and feature mentions

**05_Workflows_Processes.md**
- **Libraries:** Processes, Results, Steps
- **Purpose:** Document workflows and process discussions

**06_Rules_Best_Practices.md**
- **Libraries:** Parameters
- **Purpose:** Capture rules, standards, and best practices

**08_Tools_Resources.md**
- **Libraries:** Tools
- **Purpose:** List tools mentioned or recommended

**09_Technical_Architecture.md**
- **Libraries:** Tools, Processes
- **Purpose:** Document technical architecture discussions

**13_Blockers_Dependencies.md**
- **Libraries:** Processes, Results
- **Purpose:** Track blockers and dependencies

**16_Employee_Team_Context.md**
- **Libraries:** Professions, Skills, Responsibilities
- **Purpose:** Capture team and role discussions

**17_Lead_Gen_Sales_Context.md**
- **Libraries:** Services, Products, Processes (LG-specific)
- **Purpose:** Document lead generation and sales discussions

**18_Design_Creative_Context.md**
- **Libraries:** Objects, Products, Tools (Design-specific)
- **Purpose:** Capture design and creative work

**19_Development_Technical_Context.md**
- **Libraries:** Tools, Processes, Objects (Dev-specific)
- **Purpose:** Document development discussions

**20_Onboarding_Training_Context.md**
- **Libraries:** Skills, Responsibilities, Professions
- **Purpose:** Capture onboarding and training content

**21_Follow_Up_Items.md**
- **Libraries:** Actions, Tasks
- **Purpose:** List follow-up actions and tasks

### Moderately Integrated Templates (⭐⭐)

These templates use libraries minimally or for specific fields:

**01_Meeting_Metadata.md**
- **Libraries:** None (structural data only)
- **Purpose:** Basic meeting information

**02_Executive_Summary.md**
- **Libraries:** Minimal
- **Purpose:** High-level overview

### Lightly Integrated Templates (⭐)

These templates primarily capture free-form content:

- 07_Problems_Solutions.md
- 10_Decisions_Log.md
- 11_Documentation_Gaps.md
- 12_Communication_Announcements.md
- 14_Insights_Lessons.md
- 15_Analogies_Frameworks.md

---

## Complete Template List

| # | Template File | Primary Purpose | Library Integration |
|---|---------------|-----------------|---------------------|
| 01 | Meeting_Metadata.md | Basic info | None |
| 02 | Executive_Summary.md | Overview | Minimal |
| 03 | Action_Items_Tasks.md | Action tracking | ⭐⭐⭐ Heavy |
| 04 | Projects_Features.md | Project discussions | ⭐⭐⭐ Heavy |
| 05 | Workflows_Processes.md | Process documentation | ⭐⭐⭐ Heavy |
| 06 | Rules_Best_Practices.md | Standards capture | ⭐⭐⭐ Heavy |
| 07 | Problems_Solutions.md | Issue tracking | ⭐ Light |
| 08 | Tools_Resources.md | Tool mentions | ⭐⭐⭐ Heavy |
| 09 | Technical_Architecture.md | Architecture | ⭐⭐⭐ Heavy |
| 10 | Decisions_Log.md | Decisions | ⭐ Light |
| 11 | Documentation_Gaps.md | Gaps | ⭐ Light |
| 12 | Communication_Announcements.md | Comms | ⭐ Light |
| 13 | Blockers_Dependencies.md | Blockers | ⭐⭐⭐ Heavy |
| 14 | Insights_Lessons.md | Insights | ⭐ Light |
| 15 | Analogies_Frameworks.md | Frameworks | ⭐ Light |
| 16 | Employee_Team_Context.md | Team context | ⭐⭐⭐ Heavy |
| 17 | Lead_Gen_Sales_Context.md | Sales (LG) | ⭐⭐⭐ Heavy |
| 18 | Design_Creative_Context.md | Design | ⭐⭐⭐ Heavy |
| 19 | Development_Technical_Context.md | Dev | ⭐⭐⭐ Heavy |
| 20 | Onboarding_Training_Context.md | Training | ⭐⭐⭐ Heavy |
| 21 | Follow_Up_Items.md | Follow-ups | ⭐⭐⭐ Heavy |

---

## Usage Workflow

### For Each Meeting:

1. **Start with 01_Meeting_Metadata** - Fill basic info
2. **Create 02_Executive_Summary** - High-level overview
3. **Work through templates 03-21** in order
4. **Skip empty sections** - Only include sections with content
5. **Use recognition rules** - From `../03_Processing_Rules/`
6. **Reference libraries** - From `../01_Library_Integration/`
7. **Validate** - Using checklist in each template

### Template Selection:

**All Meetings:**
- 01 Meeting Metadata (always)
- 02 Executive Summary (always)
- 03 Action Items & Tasks (if action items discussed)

**As Applicable:**
- Use department-specific templates (17-20) for department meetings
- Use technical templates (08-09, 19) for technical discussions
- Use team templates (16, 20) for team/HR discussions
- Use Project Templates (04, 05) for project planning

---

## Output Format Standards

All templates follow these standards:
- **Markdown format** for readability
- **Structured sections** with clear headers
- **Entity IDs** when referencing LIBRARIES entities
- **Confidence levels** for entity matches (High/Medium/Low)
- **Cross-references** between related entities
- **Source attribution** (who said what, when applicable)

---

## Examples Location

Each template file includes:
- At least 1 realistic example
- Examples use real entity IDs from LIBRARIES
- Examples show proper formatting
- Examples demonstrate library integration

---

## Validation

Each template includes a validation checklist to ensure:
- All relevant information captured
- Correct format used
- Entity IDs are valid
- Cross-references are accurate
- Confidence levels assigned appropriately

---

**Status:** 🚧 Pending - Files to be created in MIL-004
