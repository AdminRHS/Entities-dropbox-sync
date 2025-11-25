# SAMPLE: Guide with Full Metadata Preview

**Purpose:** Example guide showing all proposed database fields in markdown format
**This is a SAMPLE for architecture review**

---

## Guide Metadata (From `guides` table)

```yaml
# Core Identification
id: 10
guide_code: GDS-010
name: Quick Start Guide - PMT-032 v2.1

# Classification
entity_id: null
department_code: AID
category: Tutorial
scope: task_template
priority: critical
status: active

# Version & Description
version: "1.2"
description: |
  Quick start tutorial for daily report submission using PMT-032 v2.1 framework.
  Covers Whisper Flow setup, activity logging, entity mapping, and report submission workflow.
  Essential for all employees.
estimated_read_time_min: 7

# Audit Trail
created_at: 2025-11-22T09:00:00
created_by: 1
updated_at: 2025-11-22T14:00:00
```

---

## Available Formats (From `guide_formats` table)

```yaml
formats:
  - id: 13
    format_id: 1  # Markdown
    format_name: Markdown
    link: TSM-007_GUIDES/GDS-010_Quick_Start_PMT032_v2.1.md
    is_primary: true
    format_version: "1.2"
    file_size_kb: 25
    description: Primary markdown tutorial with step-by-step instructions

  - id: 14
    format_id: 2  # PDF
    format_name: PDF
    link: TSM-007_GUIDES/exports/GDS-010_Quick_Start_v1.0.pdf
    is_primary: false
    format_version: "1.0"
    file_size_kb: 180
    description: Printable PDF version for offline reference

  - id: 15
    format_id: 4  # Video Tutorial
    format_name: Video Tutorial
    link: https://drive.google.com/drive/folders/1ABC123XYZ_VIDEO
    is_primary: false
    format_version: "1.0"
    file_size_kb: 45000
    description: 5-minute video tutorial - ideal for visual learners
```

---

## Version History (From `guide_versions` table)

```yaml
versions:
  - id: 1
    version: "1.0"
    change_type: created
    changes: Initial creation of Quick Start Guide for PMT-032 v2.1
    created_at: 2025-11-22T09:00:00
    created_by: 1

  - id: 2
    version: "1.1"
    change_type: format_added
    changes: Added video tutorial format, clarified Whisper Flow setup section
    created_at: 2025-11-22T10:30:00
    created_by: 1

  - id: 3
    version: "1.2"
    change_type: minor_fix
    changes: Fixed typos in section 3, updated screenshot in step 2
    created_at: 2025-11-22T14:00:00
    created_by: 1
```

---

## Tags (From `guide_tags` table)

```yaml
tags:
  - id: 1
    tag: beginner
    tag_category: skill_level

  - id: 2
    tag: onboarding
    tag_category: task_type

  - id: 3
    tag: daily_workflow
    tag_category: task_type

  - id: 4
    tag: required
    tag_category: priority

  - id: 5
    tag: whisper_flow
    tag_category: tool

  - id: 6
    tag: claude
    tag_category: tool
```

---

## Template Cross-References

### Project Templates (From `guide_project_templates` table)

```yaml
project_templates:
  - id: 1
    project_template_code: PRT-001
    project_name: Daily Report Collection
    relevance: required
    context: Daily Report Collection project - essential for all employees
    display_order: 1
```

### Milestone Templates (From `guide_milestone_templates` table)

```yaml
milestone_templates:
  - id: 1
    milestone_template_code: MLT-001
    milestone_name: Weekly Report Compilation
    relevance: recommended
    context: Weekly report compilation milestone
    display_order: 1

  - id: 2
    milestone_template_code: MLT-002
    milestone_name: Monthly Report Aggregation
    relevance: recommended
    context: Monthly report aggregation milestone
    display_order: 2
```

### Task Templates (From `guide_task_templates` table)

```yaml
task_templates:
  - id: 1
    task_template_code: TST-042
    task_name: Daily Report Submission
    relevance: required
    context: Daily report submission workflow - comprehensive guide
    display_order: 1

  - id: 2
    task_template_code: TST-043
    task_name: Whisper Flow Recording
    relevance: required
    context: Whisper Flow recording setup - essential for transcripts
    display_order: 2

  - id: 3
    task_template_code: TST-044
    task_name: Entity Mapping Validation
    relevance: recommended
    context: Entity mapping validation - ensures correct code assignment
    display_order: 3

  - id: 4
    task_template_code: TST-045
    task_name: Activity Time Tracking
    relevance: recommended
    context: Activity time tracking - best practices for hour estimation
    display_order: 4
```

### Step Templates (From `guide_step_templates` table)

```yaml
step_templates:
  - id: 1
    step_template_code: STP-127
    step_name: Whisper Flow Initialization
    relevance: required
    context: Whisper Flow recording initialization
    display_order: 1

  - id: 2
    step_template_code: STP-128
    step_name: Activity Logging Format
    relevance: required
    context: Activity logging format specification
    display_order: 2

  - id: 3
    step_template_code: STP-129
    step_name: Timestamp Documentation
    relevance: recommended
    context: Timestamp documentation best practices
    display_order: 3

  - id: 4
    step_template_code: STP-130
    step_name: Transcript Embedding
    relevance: recommended
    context: Transcript embedding in daily reports
    display_order: 4
```

---

## Tool References (From `guide_tools` table)

```yaml
tools:
  - id: 1
    tool_id: 5
    tool_name: Whisper Flow
    usage_context: Whisper Flow for recording activity transcripts
    is_primary_tool: true

  - id: 2
    tool_id: 1
    tool_name: Claude
    usage_context: Claude for processing daily reports
    is_primary_tool: false

  - id: 3
    tool_id: 2
    tool_name: Gemini
    usage_context: Gemini for alternative report generation
    is_primary_tool: false
```

---

## Summary Statistics

```yaml
statistics:
  total_formats: 3
  total_versions: 3
  total_tags: 6
  total_template_links: 11
    project_links: 1
    milestone_links: 2
    task_links: 4
    step_links: 4
  total_tool_links: 3

  hierarchical_coverage:
    - "Covers all 4 levels of template hierarchy"
    - "Comprehensive daily reporting workflow"
    - "Beginner-friendly with multiple formats"
```

---

## User-Facing Presentation

### How This Would Appear in System

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📘 GDS-010: Quick Start Guide - PMT-032 v2.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱ 7 min read  |  🎯 Beginner  |  🔴 Required  |  📦 v1.2

Quick start tutorial for daily report submission using PMT-032 v2.1
framework. Covers Whisper Flow setup, activity logging, entity mapping,
and report submission workflow. Essential for all employees.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Available Formats
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📄 Markdown (Primary)         [View]
     Step-by-step instructions, 25 KB

  📑 PDF                         [Download]
     Printable offline version, 180 KB

  🎥 Video Tutorial (5 min)     [Watch]
     Visual walkthrough, ideal for beginners

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 Related Templates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📂 Projects (1)
  • PRT-001: Daily Report Collection [Required]

📋 Milestones (2)
  • MLT-001: Weekly Report Compilation [Recommended]
  • MLT-002: Monthly Report Aggregation [Recommended]

✓ Tasks (4)
  • TST-042: Daily Report Submission [Required]
  • TST-043: Whisper Flow Recording [Required]
  • TST-044: Entity Mapping Validation [Recommended]
  • TST-045: Activity Time Tracking [Recommended]

→ Steps (4)
  • STP-127: Whisper Flow Initialization [Required]
  • STP-128: Activity Logging Format [Required]
  • STP-129: Timestamp Documentation [Recommended]
  • STP-130: Transcript Embedding [Recommended]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 Tools Covered
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🎙 Whisper Flow (Primary) - Recording activity transcripts
  🤖 Claude - Processing daily reports
  💎 Gemini - Alternative report generation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏷 Tags
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Skill: beginner  |  Type: onboarding, daily_workflow  |  Required

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📜 Version History
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  v1.2 (2025-11-22) - Fixed typos, updated screenshots
  v1.1 (2025-11-22) - Added video format, clarified setup
  v1.0 (2025-11-22) - Initial creation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Database Query Preview

### SQL Query to Retrieve This Guide

```sql
-- Get guide with all relationships
SELECT
  g.*,
  GROUP_CONCAT(DISTINCT gf.link) as formats,
  GROUP_CONCAT(DISTINCT gt.tag) as tags,
  COUNT(DISTINCT gtask.task_template_code) as task_count,
  COUNT(DISTINCT gstep.step_template_code) as step_count
FROM guides g
LEFT JOIN guide_formats gf ON g.id = gf.guide_id
LEFT JOIN guide_tags gt ON g.id = gt.guide_id
LEFT JOIN guide_task_templates gtask ON g.id = gtask.guide_id
LEFT JOIN guide_step_templates gstep ON g.id = gstep.guide_id
WHERE g.guide_code = 'GDS-010'
GROUP BY g.id;
```

### Result Preview

```
id: 10
guide_code: GDS-010
name: Quick Start Guide - PMT-032 v2.1
formats: TSM-007_GUIDES/GDS-010..., exports/GDS-010..., https://drive...
tags: beginner,onboarding,daily_workflow,required,whisper_flow,claude
task_count: 4
step_count: 4
```

---

## Benefits of This Metadata Structure

### 1. **Discoverability**
- Users can find guides by tag, tool, template, or department
- Full-text search on name and description

### 2. **Flexibility**
- Multiple formats cater to different learning styles
- Tags enable creative categorization
- Template links at all hierarchy levels

### 3. **Maintainability**
- Version history tracks all changes
- Clear audit trail with timestamps and authors
- Rollback capability if needed

### 4. **Scalability**
- Handles growth from 12 to 100+ guides
- Template links don't duplicate guide content
- Foreign key relationships maintain data integrity

### 5. **User Experience**
- Clear relevance indicators (required/recommended/optional)
- Context-specific descriptions for each template
- Multiple format options based on preference

---

**File Location:** `ENTITIES/TASK_MANAGERS/TSM-007_GUIDES/SAMPLE_Guide_Full_Metadata.md`
**Purpose:** Architecture preview - demonstrates all database fields in markdown format
**Status:** Sample for review

**Last Updated:** 2025-11-22
