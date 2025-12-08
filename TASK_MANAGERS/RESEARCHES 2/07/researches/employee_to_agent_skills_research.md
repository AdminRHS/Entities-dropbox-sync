# Employee Skills to Agent Skills - Research & Conversion Framework

**Research ID:** 07-R001
**Created:** 2025-12-07
**Location:** RESEARCHES 2/07/researches/
**Purpose:** Convert 28 employee skills from TALENTS/Skills into Claude Code-style agent skills

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Employee Skills Overview](#employee-skills-overview)
3. [Agent Skills Framework (Claude Code)](#agent-skills-framework-claude-code)
4. [Conversion Methodology](#conversion-methodology)
5. [Conversion Patterns by Category](#conversion-patterns-by-category)
6. [Case Studies](#case-studies)
7. [Implementation Roadmap](#implementation-roadmap)
8. [Quality Standards](#quality-standards)

---

## Executive Summary

### Problem Statement

We have **28 employee skills** documented in JSON format at `C:\Users\Dell\Dropbox\ENTITIES\TALENTS\Skills`, representing capabilities across 6 departments and 13 professions. These skills are currently used for:
- Employee proficiency tracking
- Candidate matching
- Talent showcasing
- Training & development

However, these skills are **not** actionable by AI agents. They exist as data structures, not executable capabilities.

### Opportunity

By converting employee skills into **agent skills** (Claude Code format), we can:
1. **Automate skill execution** - AI can perform tasks using employee skill knowledge
2. **Scale expertise** - Distribute employee capabilities across AI agents
3. **Standardize workflows** - Convert tribal knowledge into reusable patterns
4. **Enable continuous improvement** - Skills evolve through usage and iteration

### Approach

**Convert JSON skill definitions → Claude Code SKILL.md format**

**Example:**
```
Employee Skill (JSON):
{
  "skill_id": "SKL-030",
  "skill_phrase": "developed features in React",
  "difficulty_level": "intermediate",
  "frequency": "daily"
}

↓ Convert to ↓

Agent Skill (SKILL.md):
---
name: react-development
description: Develop React features and components. Use when user requests "develop React feature", "create React component", "build UI in React", or when working with React applications.
---

# React Development

## Overview
Create, modify, and optimize React components and features...

## Scripts
- scripts/create_component.jsx
- scripts/test_component.spec.jsx

## References
- references/react_patterns.md
- references/component_architecture.md

## Assets
- assets/component_template.jsx
```

### Expected Outcomes

1. **28 agent skills** created from employee skills
2. **Skill conversion framework** - reusable templates for future skills
3. **Quality standards** - validation criteria for successful conversions
4. **Priority implementation** - which skills to convert first

---

## Employee Skills Overview

### Source Data

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\TALENTS\Skills`

**Total Skills:** 28 (SKL-001 to SKL-052, non-sequential)

### Current Structure

**Organization:**
- `Master/all_skills.json` - Complete catalog
- `By_Department/` - HR (5), Lead Gen (5), Design (5), Dev (5), Sales (5), Video (3)
- `By_Profession/` - 13 profession-specific files
- `By_Difficulty/` - Beginner (12), Intermediate (11), Advanced (5)
- `By_Tool/` - 20 tool-specific files

**Skill Definition (JSON):**
```json
{
  "skill_id": "SKL-001",
  "skill_phrase": "screened candidates via CRM",
  "components": {
    "result": "screened",
    "action": "screen",
    "object": "candidates",
    "tool": "CRM",
    "tool_category": "Communication"
  },
  "department": "Managers (HR)",
  "professions": ["recruiter", "hr manager"],
  "difficulty_level": "beginner",
  "frequency": "daily",
  "time_estimate_minutes": 30,
  "automation_potential": "high",
  "related_skills": ["SKL-002", "SKL-004"],
  "example_tasks": [
    "Screen 50 candidate profiles in CRM",
    "Filter candidates by job requirements"
  ]
}
```

### Employee Skills Inventory

**By Department:**

**1. HR/Managers (5 skills):**
- SKL-001: screened candidates via CRM
- SKL-002: conducted video interviews via Zoom
- SKL-003: sent job offers via Gmail
- SKL-004: updated candidate status in CRM
- SKL-005: analyzed recruitment data in Google Sheets

**2. Lead Generation (5 skills):**
- SKL-010: sent cold emails via Gmail
- SKL-011: automated email campaigns using n8n
- SKL-012: tracked email responses in CRM
- SKL-013: searched companies on LinkedIn
- SKL-014: scraped contact data using automation tools

**3. Design (5 skills):**
- SKL-020: created UI mockups in Figma
- SKL-021: designed social media posts in Canva
- SKL-022: exported design files from Figma
- SKL-023: generated AI images using Midjourney
- SKL-024: shared design previews via Discord

**4. Developers (5 skills):**
- SKL-030: developed features in React
- SKL-031: created APIs using Node.js
- SKL-032: managed code via GitHub
- SKL-033: debugged applications using DevTools
- SKL-034: deployed applications to production servers

**5. Sales (5 skills):**
- SKL-040: conducted discovery calls via Zoom
- SKL-041: created proposals in Google Docs
- SKL-042: tracked deals in CRM
- SKL-043: sent contracts via DocuSign
- SKL-044: analyzed sales data in Google Sheets

**6. Video (3 skills):**
- SKL-050: edited videos in Adobe Premiere
- SKL-051: added subtitles in Adobe Premiere
- SKL-052: created animations in After Effects

### Key Attributes to Preserve

When converting to agent skills, preserve:
1. **Skill phrase** - becomes skill name and triggers
2. **Components** (action + object + tool) - inform skill structure
3. **Difficulty level** - affects complexity of SKILL.md
4. **Frequency** - indicates importance
5. **Automation potential** - determines script vs. manual guidance
6. **Related skills** - links to other agent skills
7. **Example tasks** - become examples in SKILL.md

---

## Agent Skills Framework (Claude Code)

### What is an Agent Skill?

An **agent skill** is a packaged capability that enables AI to:
- Understand when to use the skill (triggers)
- Execute the skill workflow (instructions)
- Automate repetitive parts (scripts)
- Reference detailed knowledge (references)
- Use templates and boilerplate (assets)

### Claude Code Skill Structure

**Required:**
```
skill-name/
└── SKILL.md
    ├── YAML frontmatter
    │   ├── name: (hyphen-case, <40 chars)
    │   └── description: (what + when/triggers)
    └── Markdown body
        ├── Overview
        ├── Workflow/Instructions
        └── Resources section
```

**Optional:**
```
skill-name/
├── scripts/          # Executable automation
├── references/       # Detailed documentation
└── assets/           # Templates, boilerplate
```

### SKILL.md Template

```yaml
---
name: skill-name
description: [What the skill does] + [When to use - triggers]
---

# Skill Title

## Overview
Brief description of what this skill enables

## [Choose structure]
# Option 1: Workflow-Based (sequential steps)
# Option 2: Task-Based (different operations)
# Option 3: Reference/Guidelines (standards)
# Option 4: Capabilities-Based (features)

## Resources
- scripts/: [List executable scripts]
- references/: [List documentation]
- assets/: [List templates/boilerplate]

## Examples
[Concrete usage examples]
```

### Progressive Disclosure

**Three-level loading:**
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - When triggered (<500 lines)
3. **Bundled resources** - As needed (unlimited)

**Why it matters:**
- Keeps context window efficient
- Loads only what's needed
- Scales to unlimited detail in references/

---

## Conversion Methodology

### Core Conversion Process

**Step 1: Analyze Employee Skill**
```
Input: Employee skill JSON
Extract:
- Skill phrase → Agent skill name + triggers
- Action + Object → Workflow structure
- Tool → Technology focus
- Difficulty → Complexity of instructions
- Automation potential → Scripts vs. guidance
- Example tasks → Concrete examples
```

**Step 2: Map to Agent Skill Structure**
```
Determine:
- Skill name (hyphen-case from skill phrase)
- Description (phrase + triggers)
- Structure type (workflow/task/reference/capability)
- Resources needed (scripts/references/assets)
```

**Step 3: Create SKILL.md**
```
Write:
- Frontmatter (name, description with triggers)
- Overview section
- Main body (workflow/tasks/guidelines)
- Resources section
- Examples section
```

**Step 4: Add Resources (if needed)**
```
Create:
- scripts/ - For automation_potential: high
- references/ - For complex workflows
- assets/ - For templates/boilerplate
```

**Step 5: Package & Register**
```
- Run package_skill.py
- Assign SKL.XX ID
- Register in System/Skills/skills_index.md
```

### Conversion Decision Tree

```
Employee Skill
├─> Automation Potential: high/very high?
│   ├─> YES: Create scripts/ + SKILL.md
│   └─> NO: SKILL.md only (manual guidance)
│
├─> Difficulty: advanced/expert?
│   ├─> YES: Add references/ for detailed docs
│   └─> NO: Keep in SKILL.md body
│
├─> Involves templates/boilerplate?
│   ├─> YES: Add assets/
│   └─> NO: Skip assets/
│
└─> Result: Complete agent skill structure
```

### Attribute Mapping

**Employee Skill → Agent Skill:**

| Employee Skill Attribute | Agent Skill Component | Example |
|--------------------------|----------------------|---------|
| skill_phrase | name (hyphen-case) | "screened candidates via CRM" → `candidate-screening` |
| skill_phrase | description triggers | "screened candidates" → "screen candidates", "filter applicants" |
| action + object | Workflow structure | "screen candidates" → Screening workflow |
| tool | Technology focus | "CRM" → CRM integration guidance |
| difficulty_level | Complexity of instructions | "beginner" → Simple steps, "advanced" → Detailed workflow |
| frequency | Usage priority | "daily" → High priority conversion |
| automation_potential | Scripts needed | "high" → Create automation scripts |
| time_estimate_minutes | Script value proposition | "240 min" → Significant time savings |
| related_skills | Links in SKILL.md | "SKL-031" → Reference react-api-integration skill |
| example_tasks | Examples section | Direct copy with enhancements |

---

## Conversion Patterns by Category

### Pattern 1: HR/Recruiting Skills

**Characteristics:**
- Process-heavy (screening, interviewing, tracking)
- Tool-dependent (CRM, Zoom, Gmail)
- Moderate automation potential
- Daily frequency

**Conversion Template:**
```yaml
---
name: [action]-[object]  # e.g., candidate-screening
description: [Action object] using [tool]. Use when user requests "[action] [object]", "[related phrases]", or when working with [workflow context].
---

# [Skill Title]

## Overview
Perform [action] on [object] using [tool] following [department] best practices.

## Workflow
1. **[Step 1 Name]**
   - [Instruction]
   - [Instruction]

2. **[Step 2 Name]**
   - [Instruction]
   - [Instruction]

## Tool Integration: [Tool Name]
- [How to use tool for this skill]
- [Best practices]

## Examples
[Example tasks from employee skill]

## Resources
- references/[tool]_guide.md - Detailed tool usage
- assets/[template].ext - Template files
```

**Example Conversion:**

**SKL-001: screened candidates via CRM** → **candidate-screening**

```yaml
---
name: candidate-screening
description: Screen and filter candidates in CRM systems. Use when user requests "screen candidates", "filter applicants", "review candidate profiles", or when conducting recruitment activities.
---

# Candidate Screening

## Overview
Efficiently screen candidates in CRM by filtering profiles against job requirements, assessing qualifications, and updating candidate status.

## Workflow
1. **Define Screening Criteria**
   - Review job requirements
   - Identify must-have vs. nice-to-have qualifications
   - Set filters in CRM

2. **Review Candidate Profiles**
   - Open candidate list in CRM
   - Apply filters (skills, experience, location)
   - Review profiles matching criteria

3. **Assess & Categorize**
   - Rate candidates (1-5 scale)
   - Add notes on strengths/concerns
   - Update candidate status (qualified/not qualified/maybe)

4. **Track & Report**
   - Log screening activity
   - Generate screening report
   - Share qualified candidates with hiring manager

## CRM Integration
- Use CRM filters to quickly narrow candidate pool
- Save common filter sets for reuse
- Bulk update candidate statuses
- Export filtered lists for sharing

## Examples
**Example 1:** Screen 50 candidates for Frontend Developer role
- Filter: React experience >2 years, located in US
- Review profiles, assess portfolio links
- Qualify 12 candidates, update CRM status

**Example 2:** Filter candidates by job requirements
- Set filters: degree in CS, Node.js skills, <5 years experience
- Review 30 matches
- Add notes, categorize as junior/mid-level

## Resources
- references/crm_screening_guide.md - Advanced CRM filtering techniques
- references/qualification_assessment.md - How to assess candidate qualifications
- assets/screening_template.csv - Screening scorecard template
```

---

### Pattern 2: Development Skills

**Characteristics:**
- Technical implementation
- Tool-specific (React, Node.js, GitHub)
- Low-to-medium automation potential (code generation varies)
- Daily frequency

**See conversion_examples.md for complete React development example**

---

### Pattern 3: Design Skills

**Characteristics:**
- Creative + technical
- Tool-specific (Figma, Canva, Midjourney)
- Medium automation potential
- Frequent use

**See conversion_templates.md for detailed design skill templates**

---

## Implementation Roadmap

### Phase 1: High-Value Quick Wins (Week 1)

**Priority Skills (automation_potential: high, frequency: daily):**

1. **SKL-032: managed code via GitHub** → `github-management`
2. **SKL-012: tracked email responses in CRM** → `crm-email-tracking`
3. **SKL-042: tracked deals in CRM** → `crm-deal-tracking`

**Effort:** ~2-3 hours per skill | **Total:** ~6-9 hours

---

### Phase 2: Department-Specific Skills (Week 2)

**One skill per major department:**
- HR: SKL-001 (candidate-screening)
- Development: SKL-030 (react-development)
- Design: SKL-020 (ui-mockup-creation-figma)
- Sales: SKL-042 (deal-tracking)
- Lead Gen: SKL-011 (email-campaign-automation)
- Video: SKL-050 (video-editing-premiere)

**Effort:** ~3-4 hours per skill | **Total:** ~18-24 hours

---

### Phase 3: Advanced/Complex Skills (Week 3)

**High Complexity:**
- SKL-011: email-campaign-automation (n8n)
- SKL-031: api-creation-nodejs
- SKL-034: application-deployment
- SKL-050: video-editing-premiere

**Effort:** ~4-6 hours per skill | **Total:** ~16-24 hours

---

### Phase 4: Remaining Skills (Week 4)

**Complete conversion:** 15 remaining skills using established patterns

**Effort:** ~2-3 hours per skill | **Total:** ~30-45 hours

---

### Total Implementation

**Timeline:** 4 weeks
**Total Effort:** ~70-102 hours (1.5-2.5 weeks full-time)
**Deliverables:** 28 agent skills registered in System

---

## Quality Standards

### Validation Criteria

**Every converted agent skill must:**

1. **SKILL.md Structure:**
   - ✓ Valid YAML frontmatter (name, description)
   - ✓ Description includes triggers
   - ✓ Body under 500 lines
   - ✓ Clear structure (workflow/task/reference/capability)
   - ✓ Examples section with concrete examples

2. **Attribute Preservation:**
   - ✓ Original skill phrase reflected in name/triggers
   - ✓ Difficulty level appropriate to instructions complexity
   - ✓ Related skills linked
   - ✓ Example tasks incorporated

3. **Resources (when applicable):**
   - ✓ Scripts tested and working
   - ✓ References properly organized
   - ✓ Assets ready to use
   - ✓ All resources documented in SKILL.md

4. **System Integration:**
   - ✓ Assigned SKL.XX ID
   - ✓ Registered in skills_index.md
   - ✓ Follows System principles (SYS.30)
   - ✓ Packaged successfully (.skill file)

---

## Conclusion

Converting 28 employee skills from JSON definitions to Claude Code agent skills will:

1. **Enable AI execution** of employee expertise
2. **Scale capabilities** across teams and agents
3. **Standardize workflows** with reusable patterns
4. **Preserve institutional knowledge** in executable format

**Next Steps:**
1. Review skill_conversion_templates.md for detailed conversion templates
2. Review employee_skills_inventory.md for complete skill list with priorities
3. Study conversion_examples.md for complete before/after examples
4. Begin Phase 1 implementation

---

**Research Status:** ✅ Complete
**Next:** Create conversion templates and begin implementation
**Created:** 2025-12-07
**Version:** 1.0
**Location:** C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES 2\07\researches\
