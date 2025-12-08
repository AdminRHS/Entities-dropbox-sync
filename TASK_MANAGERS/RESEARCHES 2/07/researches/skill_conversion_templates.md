# Skill Conversion Templates - Employee to Agent Skills

**Research ID:** 07-R002
**Created:** 2025-12-07
**Location:** RESEARCHES 2/07/researches/
**Purpose:** Reusable templates for converting employee skills into Claude Code agent skills
**Related:** [employee_to_agent_skills_research.md](employee_to_agent_skills_research.md)

---

## Table of Contents

1. [Template Usage Guide](#template-usage-guide)
2. [Template 1: HR/Recruiting Skills](#template-1-hrrecruiting-skills)
3. [Template 2: Development Skills](#template-2-development-skills)
4. [Template 3: Design Skills](#template-3-design-skills)
5. [Template 4: Sales Skills](#template-4-sales-skills)
6. [Template 5: Lead Generation Skills](#template-5-lead-generation-skills)
7. [Template 6: Video/Creative Skills](#template-6-videocreative-skills)
8. [Resource Planning Templates](#resource-planning-templates)
9. [SKILL.md Structure Patterns](#skillmd-structure-patterns)

---

## Template Usage Guide

### How to Use These Templates

**Step 1: Select Template**
- Match employee skill department/type to template category
- HR skill → Use Template 1
- Development skill → Use Template 2
- Design skill → Use Template 3
- Sales skill → Use Template 4
- Lead Gen skill → Use Template 5
- Video skill → Use Template 6

**Step 2: Fill in Placeholders**
- All placeholders are in `[BRACKETS]`
- Replace with values from employee skill JSON
- Examples provided for each field

**Step 3: Customize Resources**
- Determine if scripts/ needed (check automation_potential)
- Determine if references/ needed (check difficulty_level)
- Determine if assets/ needed (check for templates/boilerplate)

**Step 4: Validate**
- Use conversion checklist at end of each template
- Ensure all required fields completed
- Test scripts if included

---

## Template 1: HR/Recruiting Skills

**Use for:** SKL-001 to SKL-005 (HR department skills)

**Characteristics:**
- Process-heavy workflows
- Tool-dependent (CRM, Zoom, Gmail)
- Moderate automation potential
- High frequency (daily/weekly)

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] via [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[what is being acted upon]",
    "tool": "[software/platform used]"
  },
  "department": "Managers (HR)",
  "professions": ["[profession1]", "[profession2]"],
  "difficulty_level": "[beginner/intermediate/advanced]",
  "frequency": "[daily/weekly/monthly]",
  "automation_potential": "[low/medium/high]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example task 1]",
    "[Example task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [object]-[action]
# Example: candidate-screening, interview-conducting, offer-sending

description: [Action] [object] using [tool]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when [context/workflow description].
# Example: Screen and filter candidates in CRM systems. Use when user requests "screen candidates", "filter applicants", "review candidate profiles", or when conducting recruitment activities.
---
```

**SKILL.md Body Structure:**

```markdown
# [Skill Title - Capitalize Each Word]

## Overview
[1-2 sentences describing what this skill enables]
Perform [action] on [object] using [tool] following [department] best practices.

## Workflow

### Step 1: [Preparation/Setup Phase]
- [Instruction 1]
- [Instruction 2]
- [Instruction 3]

### Step 2: [Execution Phase]
- [Instruction 1]
- [Instruction 2]
- [Instruction 3]

### Step 3: [Review/Quality Check Phase]
- [Instruction 1]
- [Instruction 2]

### Step 4: [Completion/Documentation Phase]
- [Instruction 1]
- [Instruction 2]

## Tool Integration: [Tool Name]

**Key Features:**
- [Feature 1 that supports this workflow]
- [Feature 2 that supports this workflow]
- [Feature 3 that supports this workflow]

**Best Practices:**
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

**Common Filters/Views:**
- [Filter/view 1 - when to use]
- [Filter/view 2 - when to use]

## Quality Standards

**Success Criteria:**
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

**Common Pitfalls:**
- [Pitfall 1 - how to avoid]
- [Pitfall 2 - how to avoid]

## Examples

**Example 1:** [Brief scenario from example_tasks]
- [Step 1 - what was done]
- [Step 2 - what was done]
- [Outcome]

**Example 2:** [Brief scenario from example_tasks]
- [Step 1 - what was done]
- [Step 2 - what was done]
- [Outcome]

## Resources
[Include if automation_potential: medium/high OR difficulty_level: advanced]

- `references/[tool_name]_guide.md` - Detailed tool usage and advanced features
- `references/[workflow]_checklist.md` - Complete workflow checklist
- `assets/[template].ext` - Template files for common outputs

[Include if automation_potential: high]
- `scripts/automate_[action].py` - Automation script for [specific task]
```

### Resource Planning for HR Skills

**scripts/ (Create if automation_potential: high)**
```
scripts/
├── automate_[action].py     # Main automation script
├── validate_[object].py     # Validation/quality check
└── report_[metric].py       # Reporting/analytics
```

**Example scripts:**
- `automate_candidate_screening.py` - Auto-filter candidates by criteria
- `validate_candidate_data.py` - Check for missing required fields
- `report_screening_metrics.py` - Generate screening summary

**references/ (Create if difficulty_level: intermediate/advanced)**
```
references/
├── [tool]_guide.md          # Tool-specific advanced usage
├── [workflow]_checklist.md  # Complete workflow steps
└── [domain]_best_practices.md  # Industry best practices
```

**Example references:**
- `crm_guide.md` - Advanced CRM filtering, bulk operations, integrations
- `screening_checklist.md` - Complete candidate screening workflow
- `recruitment_best_practices.md` - HR industry standards

**assets/ (Create if skill involves templates/forms)**
```
assets/
├── [template]_template.ext  # Reusable template
└── [form]_form.ext         # Standard form
```

**Example assets:**
- `screening_scorecard.csv` - Candidate evaluation template
- `interview_questions.docx` - Standard interview questions
- `offer_letter_template.docx` - Job offer template

### Conversion Checklist - HR Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [object]-[action])
- [ ] Description includes WHAT + WHEN (triggers)
- [ ] Workflow broken into 3-5 clear phases
- [ ] Tool integration section explains HOW to use tool
- [ ] Quality standards defined
- [ ] Examples drawn from example_tasks
- [ ] Related skills noted (if any)
- [ ] Resources planned based on automation_potential
- [ ] Scripts created and TESTED (if applicable)
- [ ] References written (if applicable)
- [ ] Assets added (if applicable)
- [ ] SKILL.md under 500 lines

---

## Template 2: Development Skills

**Use for:** SKL-030 to SKL-034 (Developer department skills)

**Characteristics:**
- Technical implementation focus
- Tool-specific (React, Node.js, GitHub, DevTools)
- Variable automation potential (code generation varies)
- Daily frequency
- Requires code examples and best practices

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] in/using [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[technical artifact]",
    "tool": "[technology/framework]"
  },
  "department": "Developers",
  "professions": ["[developer type]"],
  "difficulty_level": "[intermediate/advanced]",
  "frequency": "daily",
  "automation_potential": "[low/medium/high]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example implementation task 1]",
    "[Example implementation task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [technology]-[artifact-type]
# Example: react-development, nodejs-api-creation, github-management

description: [Action] [technical artifact] using [technology]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when working with [technology context].
# Example: Develop React features and components. Use when user requests "develop React feature", "create React component", "build UI in React", or when working with React applications.
---
```

**SKILL.md Body Structure:**

```markdown
# [Technology] [Artifact Type]

## Overview
[1-2 sentences describing technical capability]
Create, modify, and optimize [technical artifact] using [technology] following modern development best practices.

## Quick Start

**Basic [artifact] creation:**
\`\`\`[language]
[Minimal working example - 5-10 lines]
\`\`\`

**When to use this skill:**
- [Use case 1]
- [Use case 2]
- [Use case 3]

## Core Workflows

### Workflow 1: Creating New [Artifact]

**Steps:**
1. **[Planning step]**
   \`\`\`[language]
   [Code example]
   \`\`\`

2. **[Implementation step]**
   \`\`\`[language]
   [Code example]
   \`\`\`

3. **[Testing step]**
   \`\`\`[language]
   [Code example]
   \`\`\`

4. **[Integration step]**
   \`\`\`[language]
   [Code example]
   \`\`\`

### Workflow 2: Modifying Existing [Artifact]

**Steps:**
1. **[Analysis step]**
   - [What to check]
   - [What to identify]

2. **[Modification step]**
   \`\`\`[language]
   [Code example]
   \`\`\`

3. **[Verification step]**
   - [What to test]
   - [What to validate]

### Workflow 3: Debugging [Artifact]

**Common Issues:**
- **Issue 1:** [Description]
  - Solution: [How to fix]
  \`\`\`[language]
  [Code fix example]
  \`\`\`

- **Issue 2:** [Description]
  - Solution: [How to fix]

## Best Practices

### Code Quality
- [Best practice 1 with code example]
- [Best practice 2 with code example]
- [Best practice 3 with code example]

### Performance
- [Performance tip 1]
- [Performance tip 2]

### Security
- [Security consideration 1]
- [Security consideration 2]

## [Technology] Patterns

### Pattern 1: [Pattern Name]
**When to use:** [Context]

\`\`\`[language]
[Pattern code example]
\`\`\`

**Benefits:**
- [Benefit 1]
- [Benefit 2]

### Pattern 2: [Pattern Name]
**When to use:** [Context]

\`\`\`[language]
[Pattern code example]
\`\`\`

## Testing

**Unit Testing:**
\`\`\`[language]
[Test example]
\`\`\`

**Integration Testing:**
\`\`\`[language]
[Test example]
\`\`\`

## Examples

**Example 1:** [Real-world scenario from example_tasks]

**Implementation:**
\`\`\`[language]
[Complete code example]
\`\`\`

**Explanation:**
- [What this does]
- [Why this approach]

**Example 2:** [Real-world scenario from example_tasks]

**Implementation:**
\`\`\`[language]
[Complete code example]
\`\`\`

## Resources

[Include for advanced/complex skills]
- `references/[technology]_patterns.md` - Comprehensive pattern library
- `references/[technology]_api_reference.md` - API documentation
- `references/best_practices.md` - Industry standards and conventions

[Include for high automation potential]
- `scripts/create_[artifact].js` - Scaffold new [artifact]
- `scripts/test_[artifact].js` - Automated testing

[Include if templates exist]
- `assets/[artifact]_template.[ext]` - Boilerplate template
- `assets/[config]_config.[ext]` - Standard configuration
```

### Resource Planning for Development Skills

**scripts/ (Create if automation_potential: medium/high)**
```
scripts/
├── create_[artifact].[ext]      # Scaffolding/generation
├── test_[artifact].[ext]        # Automated testing
├── validate_[artifact].[ext]    # Linting/validation
└── deploy_[artifact].[ext]      # Deployment automation
```

**Example scripts:**
- `create_component.jsx` - React component scaffolding
- `test_component.spec.jsx` - Component test template
- `validate_api.js` - API endpoint validation
- `deploy_app.sh` - Production deployment

**references/ (Create for all development skills - technical detail needed)**
```
references/
├── [technology]_patterns.md         # Design patterns
├── [technology]_api_reference.md    # API documentation
├── best_practices.md                # Coding standards
├── troubleshooting.md               # Common issues & fixes
└── [technology]_ecosystem.md        # Related tools/libraries
```

**Example references:**
- `react_patterns.md` - React patterns (hooks, context, composition)
- `react_api_reference.md` - React API reference
- `component_architecture.md` - Component design principles
- `troubleshooting.md` - Common React errors and solutions

**assets/ (Create if boilerplate/templates exist)**
```
assets/
├── [artifact]_template.[ext]    # Code template
├── [config].[ext]               # Configuration file
└── [structure]/                 # Directory structure template
```

**Example assets:**
- `component_template.jsx` - React component boilerplate
- `test_template.spec.jsx` - Jest test boilerplate
- `tsconfig.json` - TypeScript configuration
- `hello-world/` - Minimal working example project

### Conversion Checklist - Development Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [technology]-[artifact-type])
- [ ] Description includes technology + triggers
- [ ] Quick Start section with minimal example
- [ ] Core workflows identified (create, modify, debug)
- [ ] Code examples in each workflow step
- [ ] Best practices documented (quality, performance, security)
- [ ] Technology-specific patterns included
- [ ] Testing examples provided
- [ ] Real-world examples from example_tasks
- [ ] References created (patterns, API, best practices)
- [ ] Scripts created for scaffolding/testing (if applicable)
- [ ] Assets added (templates, configs, boilerplate)
- [ ] All code examples tested and working
- [ ] SKILL.md under 500 lines (split to references if needed)

---

## Template 3: Design Skills

**Use for:** SKL-020 to SKL-024 (Design department skills)

**Characteristics:**
- Creative + technical blend
- Tool-specific (Figma, Canva, Midjourney)
- Medium automation potential
- Frequent use
- Output-focused (files, assets, deliverables)

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] in [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[design artifact]",
    "tool": "[design tool]"
  },
  "department": "Design",
  "professions": ["[designer type]"],
  "difficulty_level": "[beginner/intermediate/advanced]",
  "frequency": "[daily/weekly]",
  "automation_potential": "[medium/high]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example design task 1]",
    "[Example design task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [artifact]-[action]-[tool]
# Example: ui-mockup-creation-figma, social-media-design-canva, ai-image-generation

description: [Action] [artifact] using [tool]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when [design context].
# Example: Create UI mockups and wireframes in Figma. Use when user requests "create mockup", "design UI", "wireframe interface", or when prototyping applications.
---
```

**SKILL.md Body Structure:**

```markdown
# [Tool] [Artifact] [Action]

## Overview
[1-2 sentences describing design capability]
Create professional [artifact] using [tool] following design system principles and best practices.

## Quick Start

**Basic workflow:**
1. [Step 1 - setup]
2. [Step 2 - create]
3. [Step 3 - refine]
4. [Step 4 - export/share]

**Typical use cases:**
- [Use case 1]
- [Use case 2]
- [Use case 3]

## Design Process

### Phase 1: Planning & Setup

**Before starting in [tool]:**
- [Planning activity 1]
- [Planning activity 2]
- [Planning activity 3]

**[Tool] setup:**
- [Setup step 1]
- [Setup step 2]
- [Setup step 3]

### Phase 2: Creation

**Creating [artifact] in [tool]:**

1. **[Creation step 1 - e.g., Layout]**
   - [Instruction 1]
   - [Instruction 2]
   - **[Tool] features to use:**
     - [Feature 1]
     - [Feature 2]

2. **[Creation step 2 - e.g., Styling]**
   - [Instruction 1]
   - [Instruction 2]
   - **[Tool] features to use:**
     - [Feature 1]
     - [Feature 2]

3. **[Creation step 3 - e.g., Details]**
   - [Instruction 1]
   - [Instruction 2]

### Phase 3: Refinement

**Quality checks:**
- [ ] [Check 1 - e.g., Alignment]
- [ ] [Check 2 - e.g., Consistency]
- [ ] [Check 3 - e.g., Accessibility]
- [ ] [Check 4 - e.g., Responsiveness]

**Iteration:**
- [Refinement technique 1]
- [Refinement technique 2]

### Phase 4: Export & Delivery

**Export settings ([tool]-specific):**
- **For [use case 1]:** [Settings]
- **For [use case 2]:** [Settings]
- **For [use case 3]:** [Settings]

**Delivery checklist:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

## [Tool] Features & Techniques

### Feature 1: [Feature Name]
**What it does:** [Description]
**When to use:** [Context]
**How to use:**
- [Step 1]
- [Step 2]

### Feature 2: [Feature Name]
**What it does:** [Description]
**When to use:** [Context]
**How to use:**
- [Step 1]
- [Step 2]

### Feature 3: [Feature Name]
**What it does:** [Description]
**When to use:** [Context]
**How to use:**
- [Step 1]
- [Step 2]

## Design Best Practices

### Visual Design
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

### User Experience
- [UX principle 1]
- [UX principle 2]
- [UX principle 3]

### Accessibility
- [Accessibility guideline 1]
- [Accessibility guideline 2]

### Brand Consistency
- [Brand guideline 1]
- [Brand guideline 2]

## Common Patterns

### Pattern 1: [Pattern Name]
**Use for:** [Context]
**Implementation:**
- [Step 1]
- [Step 2]
**Example:** [Brief example]

### Pattern 2: [Pattern Name]
**Use for:** [Context]
**Implementation:**
- [Step 1]
- [Step 2]

## Examples

**Example 1:** [Scenario from example_tasks]

**Approach:**
1. [What was created]
2. [How it was structured]
3. [Key design decisions]

**Output:** [Description of final deliverable]

**Example 2:** [Scenario from example_tasks]

**Approach:**
1. [What was created]
2. [How it was structured]
3. [Key design decisions]

## Collaboration & Handoff

**Sharing with stakeholders:**
- [How to share preview]
- [How to gather feedback]
- [How to iterate]

**Developer handoff:**
- [What to include]
- [How to export assets]
- [How to document specs]

## Resources

[Include for advanced features]
- `references/[tool]_advanced_guide.md` - Advanced features and techniques
- `references/design_system.md` - Design system and component library
- `references/[artifact]_best_practices.md` - Industry best practices

[Include if automation possible]
- `scripts/export_[artifact].py` - Automated export with proper settings
- `scripts/optimize_[asset].py` - Asset optimization

[Include for all design skills]
- `assets/[artifact]_template.[ext]` - Starter template
- `assets/design_system/` - Colors, typography, components
- `assets/examples/` - Reference examples
```

### Resource Planning for Design Skills

**scripts/ (Create if automation_potential: high - exports, optimizations)**
```
scripts/
├── export_[artifact].py         # Automated export
├── optimize_[asset].py          # Image/file optimization
├── convert_[format].py          # Format conversion
└── batch_process.py             # Batch operations
```

**Example scripts:**
- `export_figma_assets.py` - Export all assets from Figma with naming convention
- `optimize_images.py` - Compress images for web
- `convert_svg_to_png.py` - Convert SVG exports to PNG at various sizes

**references/ (Create for all design skills - standards and guides needed)**
```
references/
├── [tool]_guide.md              # Comprehensive tool guide
├── design_system.md             # Design system documentation
├── [artifact]_best_practices.md # Artifact-specific best practices
├── accessibility_guidelines.md  # WCAG compliance
└── brand_guidelines.md          # Brand standards
```

**Example references:**
- `figma_guide.md` - Figma features, shortcuts, plugins, auto-layout
- `design_system.md` - Color palette, typography, spacing, components
- `ui_mockup_best_practices.md` - UI design principles
- `accessibility_guidelines.md` - Color contrast, font sizes, focus states

**assets/ (CRITICAL for design skills - templates and examples)**
```
assets/
├── templates/
│   ├── [artifact]_template.[ext]    # Starter template
│   └── [variant]_template.[ext]     # Template variations
├── design_system/
│   ├── colors.png                   # Color palette
│   ├── typography.png               # Typography scale
│   └── components/                  # Component library
├── examples/
│   ├── example_1.[ext]              # Reference example
│   └── example_2.[ext]              # Reference example
└── resources/
    ├── icons/                       # Icon library
    └── images/                      # Stock images/placeholders
```

**Example assets:**
- `templates/ui_mockup_template.fig` - Figma template with artboards
- `design_system/colors.png` - Brand color palette
- `design_system/components/` - Button, input, card components
- `examples/dashboard_mockup.fig` - Example dashboard design
- `resources/icons/` - Icon set for UI elements

### Conversion Checklist - Design Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [artifact]-[action]-[tool])
- [ ] Description includes artifact + tool + triggers
- [ ] Quick Start with basic workflow
- [ ] Design process broken into phases (Planning, Creation, Refinement, Export)
- [ ] Tool-specific features documented
- [ ] Design best practices included (visual, UX, accessibility, brand)
- [ ] Common patterns identified
- [ ] Examples from example_tasks
- [ ] Collaboration/handoff section added
- [ ] Export settings documented
- [ ] References created (tool guide, design system, best practices)
- [ ] Scripts created for automation (if applicable)
- [ ] Assets added (CRITICAL - templates, design system, examples)
- [ ] Templates tested in actual tool
- [ ] SKILL.md under 500 lines

---

## Template 4: Sales Skills

**Use for:** SKL-040 to SKL-044 (Sales department skills)

**Characteristics:**
- Communication and process-focused
- Tool mix (Zoom, Google Docs, CRM, DocuSign)
- Medium automation potential
- Deal-focused workflows
- Documentation-heavy

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] via/in [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[sales artifact]",
    "tool": "[tool used]"
  },
  "department": "Sales",
  "professions": ["[sales role]"],
  "difficulty_level": "[beginner/intermediate/advanced]",
  "frequency": "[daily/weekly]",
  "automation_potential": "[low/medium/high]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example sales task 1]",
    "[Example sales task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [object]-[action]
# Example: discovery-call-conducting, proposal-creation, deal-tracking

description: [Action] [object] using [tool]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when [sales context].
# Example: Conduct discovery calls and sales meetings via Zoom. Use when user requests "conduct discovery call", "run sales meeting", "qualify prospect", or when engaging with potential customers.
---
```

**SKILL.md Body Structure:**

```markdown
# [Activity] [Process/Artifact]

## Overview
[1-2 sentences describing sales capability]
Execute [sales activity] using [tool] following sales methodology and best practices.

## When to Use

**This skill supports:**
- [Sales stage 1]
- [Sales stage 2]
- [Sales stage 3]

**Ideal for:**
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

## Preparation

### Pre-[Activity] Checklist
- [ ] [Preparation item 1]
- [ ] [Preparation item 2]
- [ ] [Preparation item 3]
- [ ] [Preparation item 4]

### Research & Context
**Information to gather:**
- [Info type 1]
- [Info type 2]
- [Info type 3]

**Where to find it:**
- [Source 1 - e.g., CRM]
- [Source 2 - e.g., LinkedIn]
- [Source 3 - e.g., Company website]

## Execution Workflow

### Stage 1: [Opening/Introduction]

**Objectives:**
- [Objective 1]
- [Objective 2]

**Key activities:**
1. [Activity 1]
   - [Detail 1]
   - [Detail 2]

2. [Activity 2]
   - [Detail 1]
   - [Detail 2]

**Script/Framework:**
```
[Example opening script or framework]
```

### Stage 2: [Discovery/Main Activity]

**Objectives:**
- [Objective 1]
- [Objective 2]
- [Objective 3]

**Key questions to ask:**
1. [Question 1 - What it reveals]
2. [Question 2 - What it reveals]
3. [Question 3 - What it reveals]
4. [Question 4 - What it reveals]

**Active listening:**
- [Listening technique 1]
- [Listening technique 2]
- [What to note]

**Handling objections:**
- **Objection 1:** [How to address]
- **Objection 2:** [How to address]
- **Objection 3:** [How to address]

### Stage 3: [Presentation/Solution]

**Structure:**
1. [Element 1]
2. [Element 2]
3. [Element 3]

**Key messages:**
- [Message 1]
- [Message 2]
- [Message 3]

### Stage 4: [Closing/Next Steps]

**Clear next steps:**
- [Next step option 1]
- [Next step option 2]
- [Next step option 3]

**Commitment to gain:**
- [Commitment 1]
- [Commitment 2]

## Documentation

### During [Activity]
**What to capture:**
- [Data point 1]
- [Data point 2]
- [Data point 3]

**Where to log:**
- [System 1 - What to log]
- [System 2 - What to log]

### Post-[Activity]
**Immediate actions:**
1. [Action 1 - Timeline]
2. [Action 2 - Timeline]
3. [Action 3 - Timeline]

**CRM updates:**
- [ ] [Field 1]
- [ ] [Field 2]
- [ ] [Field 3]
- [ ] [Field 4]

## [Tool] Best Practices

### Setup & Configuration
- [Setting 1]
- [Setting 2]
- [Setting 3]

### During Use
- [Tip 1]
- [Tip 2]
- [Tip 3]

### Common Issues
- **Issue 1:** [Solution]
- **Issue 2:** [Solution]

## Success Metrics

**Key performance indicators:**
- [KPI 1 - Target]
- [KPI 2 - Target]
- [KPI 3 - Target]

**Quality indicators:**
- [Quality measure 1]
- [Quality measure 2]

## Examples

**Example 1:** [Scenario from example_tasks]

**Situation:** [Context]

**Approach:**
1. [What was done]
2. [What was done]
3. [What was done]

**Outcome:** [Result achieved]

**Example 2:** [Scenario from example_tasks]

**Situation:** [Context]

**Approach:**
1. [What was done]
2. [What was done]

**Outcome:** [Result achieved]

## Resources

[Include for methodology/frameworks]
- `references/[methodology]_framework.md` - Sales methodology details
- `references/[activity]_playbook.md` - Complete playbook with scripts
- `references/objection_handling.md` - Common objections and responses

[Include if templates exist]
- `assets/[document]_template.docx` - Document template
- `assets/[presentation]_template.pptx` - Presentation template
- `assets/[checklist].md` - Activity checklist

[Include if high automation potential]
- `scripts/create_[document].py` - Auto-generate from CRM data
- `scripts/update_crm.py` - Batch CRM updates
```

### Resource Planning for Sales Skills

**scripts/ (Create if automation_potential: medium/high)**
```
scripts/
├── create_[document].py         # Document generation
├── update_crm.py                # CRM automation
├── schedule_[activity].py       # Scheduling automation
└── generate_report.py           # Reporting
```

**Example scripts:**
- `create_proposal.py` - Generate proposal from CRM data + template
- `update_deal_stage.py` - Update CRM deal stage after activity
- `schedule_followup.py` - Auto-schedule follow-up based on outcome
- `generate_call_summary.py` - Create call summary from notes

**references/ (Create for methodology and playbooks)**
```
references/
├── [methodology]_framework.md   # Sales methodology
├── [activity]_playbook.md       # Complete activity playbook
├── objection_handling.md        # Objection responses
├── qualification_criteria.md    # Lead/opportunity qualification
└── [tool]_guide.md             # Tool usage guide
```

**Example references:**
- `discovery_framework.md` - SPIN, MEDDIC, or other methodology
- `discovery_call_playbook.md` - Complete scripts, questions, frameworks
- `objection_handling.md` - 20+ common objections with responses
- `zoom_guide.md` - Zoom setup, features, troubleshooting

**assets/ (Create for all sales skills - templates critical)**
```
assets/
├── templates/
│   ├── [document]_template.docx     # Document template
│   ├── [presentation]_template.pptx # Presentation template
│   └── [email]_template.txt         # Email template
├── checklists/
│   └── [activity]_checklist.md      # Activity checklist
└── scripts/
    └── [script].md                  # Call/meeting scripts
```

**Example assets:**
- `templates/proposal_template.docx` - Proposal template with placeholders
- `templates/discovery_deck.pptx` - Discovery call presentation
- `templates/followup_email.txt` - Post-call email template
- `checklists/discovery_call_checklist.md` - Pre/during/post-call checklist
- `scripts/discovery_call_script.md` - Opening, questions, closing scripts

### Conversion Checklist - Sales Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [object]-[action])
- [ ] Description includes activity + tool + triggers
- [ ] "When to Use" section defines sales context
- [ ] Preparation checklist included
- [ ] Execution workflow broken into stages
- [ ] Scripts/frameworks provided for key stages
- [ ] Objection handling addressed (if applicable)
- [ ] Documentation section (during + post)
- [ ] CRM update checklist included
- [ ] Tool best practices documented
- [ ] Success metrics defined
- [ ] Examples from example_tasks
- [ ] References created (methodology, playbook, objections)
- [ ] Assets created (templates, checklists, scripts)
- [ ] All templates tested and working
- [ ] SKILL.md under 500 lines

---

## Template 5: Lead Generation Skills

**Use for:** SKL-010 to SKL-014 (Lead Gen department skills)

**Characteristics:**
- Outbound focus
- High-volume activities
- Automation-heavy (n8n, scraping tools)
- Tool mix (Gmail, CRM, LinkedIn, automation platforms)
- Data-driven

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] using/via [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[lead gen artifact]",
    "tool": "[tool/platform]"
  },
  "department": "Lead Generation",
  "professions": ["[lead gen role]"],
  "difficulty_level": "[beginner/intermediate/advanced]",
  "frequency": "[daily/weekly]",
  "automation_potential": "[medium/high/very high]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example lead gen task 1]",
    "[Example lead gen task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [object]-[action]
# Example: email-campaign-automation, contact-data-scraping, company-research

description: [Action] [object] using [tool]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when [lead gen context].
# Example: Automate email campaigns and sequences using n8n. Use when user requests "automate email campaign", "create email sequence", "set up drip campaign", or when scaling outbound outreach.
---
```

**SKILL.md Body Structure:**

```markdown
# [Activity] [Automation/Process]

## Overview
[1-2 sentences describing lead gen capability]
[Action] [object] using [tool] to generate qualified leads at scale.

## Use Cases

**This skill enables:**
- [Use case 1]
- [Use case 2]
- [Use case 3]

**Typical campaigns:**
- [Campaign type 1]
- [Campaign type 2]
- [Campaign type 3]

## Setup & Configuration

### Prerequisites
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]
- [ ] [Requirement 4]

### [Tool] Setup

**Initial configuration:**
1. [Setup step 1]
   - [Detail 1]
   - [Detail 2]

2. [Setup step 2]
   - [Detail 1]
   - [Detail 2]

3. [Setup step 3]
   - [Detail 1]
   - [Detail 2]

**Connecting integrations:**
- [Integration 1 - How to connect]
- [Integration 2 - How to connect]
- [Integration 3 - How to connect]

## Core Workflows

### Workflow 1: [Primary Activity - e.g., Campaign Creation]

**Planning:**
1. [Planning step 1]
2. [Planning step 2]
3. [Planning step 3]

**Implementation in [tool]:**

**Step 1: [Component 1 - e.g., Audience]**
- [Instruction 1]
- [Instruction 2]
- **Settings:**
  - [Setting 1]
  - [Setting 2]

**Step 2: [Component 2 - e.g., Content]**
- [Instruction 1]
- [Instruction 2]
- **Best practices:**
  - [Best practice 1]
  - [Best practice 2]

**Step 3: [Component 3 - e.g., Automation]**
- [Instruction 1]
- [Instruction 2]

[If n8n or automation tool, include workflow diagram or structure]
```
Workflow structure:
[Trigger] → [Action 1] → [Condition] → [Action 2] → [Action 3]
```

**Step 4: [Component 4 - e.g., Testing]**
- [Test 1]
- [Test 2]
- [Test 3]

**Step 5: [Component 5 - e.g., Launch]**
- [Launch step 1]
- [Launch step 2]

### Workflow 2: [Secondary Activity - e.g., Tracking & Optimization]

**Monitoring:**
- [Metric 1 - Where to track]
- [Metric 2 - Where to track]
- [Metric 3 - Where to track]

**Optimization triggers:**
- **If [condition]:** [Action to take]
- **If [condition]:** [Action to take]
- **If [condition]:** [Action to take]

**A/B testing:**
- [Variable to test 1]
- [Variable to test 2]
- [How to implement test]

## Data Management

### Data Sources
**Where to get leads:**
- [Source 1 - How to access]
- [Source 2 - How to access]
- [Source 3 - How to access]

**Data quality:**
- [Quality check 1]
- [Quality check 2]
- [Quality check 3]

### CRM Integration
**Syncing to CRM:**
1. [Sync step 1]
2. [Sync step 2]
3. [Sync step 3]

**Field mapping:**
- [Source field] → [CRM field]
- [Source field] → [CRM field]
- [Source field] → [CRM field]

**Tracking responses:**
- [How to track response 1]
- [How to track response 2]

## Compliance & Best Practices

### Legal Compliance
- [ ] [Compliance requirement 1 - e.g., CAN-SPAM]
- [ ] [Compliance requirement 2 - e.g., GDPR]
- [ ] [Compliance requirement 3 - e.g., Unsubscribe]

### Deliverability Best Practices
- [Practice 1]
- [Practice 2]
- [Practice 3]

### Quality Standards
- [Standard 1]
- [Standard 2]
- [Standard 3]

## Performance Metrics

**Key metrics to track:**
- **[Metric 1]:** [Target/benchmark]
- **[Metric 2]:** [Target/benchmark]
- **[Metric 3]:** [Target/benchmark]
- **[Metric 4]:** [Target/benchmark]

**Reporting:**
- [How often to report]
- [What to include]
- [Where to log]

## Troubleshooting

**Common issues:**
- **Issue 1:** [Symptom] → [Solution]
- **Issue 2:** [Symptom] → [Solution]
- **Issue 3:** [Symptom] → [Solution]

## Examples

**Example 1:** [Scenario from example_tasks]

**Setup:**
- [Tool/platform used]
- [Audience targeted]
- [Campaign structure]

**Implementation:**
1. [What was configured]
2. [What was automated]
3. [How it was tracked]

**Results:**
- [Metric 1 result]
- [Metric 2 result]

**Example 2:** [Scenario from example_tasks]

**Setup:**
- [Context]

**Implementation:**
1. [Step 1]
2. [Step 2]

**Results:**
- [Outcome]

## Resources

[Include for automation workflows]
- `scripts/[workflow].json` - [Tool] workflow template
- `scripts/sync_to_crm.py` - CRM sync automation
- `scripts/validate_data.py` - Data validation

[Include for all lead gen skills]
- `references/[tool]_guide.md` - Complete tool documentation
- `references/compliance_guide.md` - Legal requirements and best practices
- `references/copywriting_guide.md` - Email/message copywriting

[Include templates]
- `assets/[campaign]_template.json` - Campaign template
- `assets/email_templates/` - Email copy templates
- `assets/tracking_dashboard.csv` - Metrics tracking template
```

### Resource Planning for Lead Gen Skills

**scripts/ (CRITICAL for lead gen - high automation potential)**
```
scripts/
├── [workflow].json              # n8n/automation workflow
├── sync_to_crm.py              # CRM integration
├── validate_data.py            # Data quality checks
├── scrape_[source].py          # Data collection
└── generate_report.py          # Performance reporting
```

**Example scripts:**
- `email_campaign_workflow.json` - n8n workflow for email campaigns
- `sync_responses_to_crm.py` - Sync email responses to CRM
- `validate_email_list.py` - Check email validity, remove duplicates
- `scrape_linkedin_companies.py` - Collect company data from LinkedIn
- `generate_campaign_report.py` - Weekly campaign performance report

**references/ (Essential for compliance and best practices)**
```
references/
├── [tool]_guide.md             # Complete platform documentation
├── compliance_guide.md         # CAN-SPAM, GDPR, legal requirements
├── copywriting_guide.md        # Email/message writing best practices
├── deliverability_guide.md     # Email deliverability optimization
└── data_sources.md             # Where to find leads
```

**Example references:**
- `n8n_guide.md` - n8n workflows, nodes, integrations, troubleshooting
- `compliance_guide.md` - CAN-SPAM Act, GDPR, unsubscribe requirements
- `email_copywriting_guide.md` - Subject lines, body copy, CTAs
- `deliverability_guide.md` - SPF/DKIM/DMARC, sender reputation, warmup

**assets/ (Templates for campaigns and tracking)**
```
assets/
├── workflows/
│   └── [campaign]_workflow.json     # Automation workflow template
├── email_templates/
│   ├── cold_email_template_1.txt    # Email template
│   ├── followup_template_1.txt      # Follow-up template
│   └── [sequence]_sequence/         # Email sequence
├── data/
│   └── sample_lead_list.csv         # Example lead list format
└── tracking/
    └── campaign_tracker.csv         # Metrics tracking spreadsheet
```

**Example assets:**
- `workflows/cold_email_campaign.json` - n8n cold email campaign
- `email_templates/saas_cold_email.txt` - SaaS cold email template
- `email_templates/followup_sequence/` - 5-email follow-up sequence
- `data/sample_lead_list.csv` - Properly formatted lead list
- `tracking/campaign_tracker.csv` - Campaign metrics tracker

### Conversion Checklist - Lead Gen Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [object]-[action])
- [ ] Description includes automation + triggers
- [ ] Use cases clearly defined
- [ ] Setup & configuration section complete
- [ ] Tool-specific setup documented
- [ ] Core workflows detailed (creation + optimization)
- [ ] Automation workflow structure documented (if applicable)
- [ ] Data management section (sources + CRM integration)
- [ ] Compliance requirements included (CAN-SPAM, GDPR)
- [ ] Performance metrics defined
- [ ] Troubleshooting section added
- [ ] Examples from example_tasks
- [ ] Scripts created (workflows, sync, validation) - CRITICAL
- [ ] References created (tool guide, compliance, copywriting)
- [ ] Assets added (workflow templates, email templates, tracking)
- [ ] All scripts/workflows tested
- [ ] SKILL.md under 500 lines

---

## Template 6: Video/Creative Skills

**Use for:** SKL-050 to SKL-052 (Video department skills)

**Characteristics:**
- Creative + technical
- Tool-specific (Adobe Premiere, After Effects)
- Advanced complexity
- Medium automation potential (export automation, batch processing)
- Output file-focused

### Employee Skill Input Format

```json
{
  "skill_id": "[SKL-XXX]",
  "skill_phrase": "[action] [object] in [tool]",
  "components": {
    "result": "[result verb]",
    "action": "[action verb]",
    "object": "[video artifact]",
    "tool": "[Adobe tool]"
  },
  "department": "Video",
  "professions": ["[video role]"],
  "difficulty_level": "[intermediate/advanced]",
  "frequency": "[weekly/monthly]",
  "automation_potential": "[low/medium]",
  "related_skills": ["SKL-XXX", "SKL-XXX"],
  "example_tasks": [
    "[Example video task 1]",
    "[Example video task 2]"
  ]
}
```

### Agent Skill Output Template

**SKILL.md Frontmatter:**

```yaml
---
name: [artifact]-[action]-[tool]
# Example: video-editing-premiere, subtitle-creation, animation-creation-after-effects

description: [Action] [artifact] using [tool]. Use when user requests "[trigger phrase 1]", "[trigger phrase 2]", "[trigger phrase 3]", or when [video production context].
# Example: Edit videos in Adobe Premiere Pro. Use when user requests "edit video", "cut footage", "color grade", "add transitions", or when producing video content.
---
```

**SKILL.md Body Structure:**

```markdown
# [Tool] [Activity]

## Overview
[1-2 sentences describing video capability]
[Action] professional [artifact] using [tool] following industry-standard workflows and techniques.

## Prerequisites

**Required:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Recommended:**
- [Recommendation 1]
- [Recommendation 2]

**Project setup:**
- [Setup requirement 1]
- [Setup requirement 2]

## Workflow Overview

**Typical process:**
1. [Phase 1 - e.g., Import & Organize]
2. [Phase 2 - e.g., Rough Cut]
3. [Phase 3 - e.g., Fine Cut]
4. [Phase 4 - e.g., Effects & Color]
5. [Phase 5 - e.g., Audio]
6. [Phase 6 - e.g., Export]

**Timeline estimate:** [Time range based on complexity]

## Phase 1: [Import & Organization]

### Importing Media

**[Tool] import process:**
1. [Import step 1]
   - [Detail 1]
   - [Detail 2]

2. [Import step 2]
   - [Detail 1]
   - [Detail 2]

**Supported formats:**
- [Format 1]
- [Format 2]
- [Format 3]

### Project Organization

**Folder structure:**
```
Project Name/
├── [Folder 1]
├── [Folder 2]
├── [Folder 3]
└── [Folder 4]
```

**Naming conventions:**
- [Convention 1]
- [Convention 2]
- [Convention 3]

**Best practices:**
- [Practice 1]
- [Practice 2]

## Phase 2: [Primary Editing Phase]

### [Editing Technique 1]

**What it does:** [Description]

**When to use:** [Context]

**How to do it in [tool]:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Keyboard shortcuts:**
- `[Shortcut 1]` - [Action]
- `[Shortcut 2]` - [Action]
- `[Shortcut 3]` - [Action]

### [Editing Technique 2]

**What it does:** [Description]

**When to use:** [Context]

**How to do it:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

### [Editing Technique 3]

**What it does:** [Description]

**How to do it:**
1. [Step 1]
2. [Step 2]

## Phase 3: [Effects/Enhancement Phase]

### [Effect Category 1 - e.g., Transitions]

**Common transitions:**
- **[Transition 1]:** [When to use] - [How to apply]
- **[Transition 2]:** [When to use] - [How to apply]
- **[Transition 3]:** [When to use] - [How to apply]

**Best practices:**
- [Practice 1]
- [Practice 2]

### [Effect Category 2 - e.g., Color Correction]

**Basic color correction workflow:**
1. [Step 1 - e.g., Exposure]
   - [How to adjust]
   - [What to look for]

2. [Step 2 - e.g., White Balance]
   - [How to adjust]
   - [What to look for]

3. [Step 3 - e.g., Saturation]
   - [How to adjust]

**[Tool] color tools:**
- [Tool 1] - [What it does]
- [Tool 2] - [What it does]
- [Tool 3] - [What it does]

### [Effect Category 3 - e.g., Text/Graphics]

**Adding text in [tool]:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Text best practices:**
- [Practice 1]
- [Practice 2]
- [Practice 3]

## Phase 4: [Audio Phase]

### Audio Editing

**Basic audio workflow:**
1. [Step 1 - e.g., Sync]
2. [Step 2 - e.g., Levels]
3. [Step 3 - e.g., Noise Reduction]
4. [Step 4 - e.g., Music]

**Audio effects:**
- [Effect 1] - [When to use]
- [Effect 2] - [When to use]
- [Effect 3] - [When to use]

### Audio Best Practices
- [Practice 1]
- [Practice 2]
- [Practice 3]

## Phase 5: [Export]

### Export Settings

**For [Use Case 1 - e.g., YouTube]:**
- **Format:** [Format]
- **Codec:** [Codec]
- **Resolution:** [Resolution]
- **Bitrate:** [Bitrate]
- **Other settings:** [Settings]

**For [Use Case 2 - e.g., Social Media]:**
- **Format:** [Format]
- **Codec:** [Codec]
- **Resolution:** [Resolution]
- **Bitrate:** [Bitrate]
- **Other settings:** [Settings]

**For [Use Case 3 - e.g., Archive]:**
- **Format:** [Format]
- **Codec:** [Codec]
- **Resolution:** [Resolution]
- **Bitrate:** [Bitrate]

### Export Workflow

1. [Export step 1]
2. [Export step 2]
3. [Export step 3]
4. [Export step 4]

**Quality check after export:**
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

## Advanced Techniques

### Technique 1: [Advanced Feature]
**Use case:** [When you need this]

**Implementation:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Technique 2: [Advanced Feature]
**Use case:** [When you need this]

**Implementation:**
1. [Step 1]
2. [Step 2]

## Performance Optimization

**For smooth playback:**
- [Tip 1]
- [Tip 2]
- [Tip 3]

**For faster rendering:**
- [Tip 1]
- [Tip 2]

## Common Issues & Solutions

**Issue 1:** [Problem description]
- **Cause:** [Why it happens]
- **Solution:** [How to fix]

**Issue 2:** [Problem description]
- **Cause:** [Why it happens]
- **Solution:** [How to fix]

**Issue 3:** [Problem description]
- **Solution:** [How to fix]

## Examples

**Example 1:** [Scenario from example_tasks]

**Project specs:**
- [Spec 1]
- [Spec 2]
- [Spec 3]

**Workflow:**
1. [What was done in phase 1]
2. [What was done in phase 2]
3. [What was done in phase 3]

**Techniques used:**
- [Technique 1]
- [Technique 2]

**Output:** [Final deliverable description]

**Example 2:** [Scenario from example_tasks]

**Approach:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Outcome:** [Result]

## Resources

[Include for advanced techniques]
- `references/[tool]_advanced_guide.md` - Advanced features and workflows
- `references/[technique]_guide.md` - Specific technique deep-dive
- `references/keyboard_shortcuts.md` - Complete shortcut reference

[Include for automation]
- `scripts/batch_export.py` - Batch export with preset settings
- `scripts/organize_project.py` - Auto-organize project files

[Include for all video skills]
- `assets/project_templates/` - [Tool] project templates
- `assets/presets/` - Export presets, effect presets
- `assets/resources/` - Music, sound effects, graphics
```

### Resource Planning for Video Skills

**scripts/ (Create if automation possible - exports, batch processing)**
```
scripts/
├── batch_export.py              # Batch export automation
├── organize_project.py          # Project organization
├── convert_media.py             # Format conversion
└── generate_proxy.py            # Proxy file generation
```

**Example scripts:**
- `batch_export_premiere.py` - Export multiple sequences with presets
- `organize_premiere_project.py` - Auto-organize bins and media
- `convert_to_h264.py` - Batch convert footage to editing codec
- `generate_proxy_files.py` - Create proxy files for 4K footage

**references/ (Essential for video skills - complex tool documentation)**
```
references/
├── [tool]_guide.md              # Comprehensive tool guide
├── [technique]_guide.md         # Specific technique documentation
├── keyboard_shortcuts.md        # Complete shortcut reference
├── codec_guide.md               # Codec and format guide
└── best_practices.md            # Industry best practices
```

**Example references:**
- `premiere_guide.md` - Premiere Pro features, panels, workflows
- `color_grading_guide.md` - Color correction and grading techniques
- `keyboard_shortcuts.md` - All Premiere shortcuts categorized
- `codec_guide.md` - When to use H.264, ProRes, DNxHD, etc.
- `video_best_practices.md` - Frame rates, resolutions, aspect ratios

**assets/ (CRITICAL for video skills - templates and presets)**
```
assets/
├── project_templates/
│   ├── [project]_template.prproj    # Premiere project template
│   └── [project]_template.aep       # After Effects project template
├── presets/
│   ├── export_presets/              # Export presets
│   ├── effect_presets/              # Effect presets
│   └── text_presets/                # Text/title presets
├── resources/
│   ├── music/                       # Royalty-free music
│   ├── sound_effects/               # Sound effects library
│   ├── graphics/                    # Lower thirds, bugs, graphics
│   └── transitions/                 # Custom transitions
└── examples/
    └── example_project/             # Complete example project
```

**Example assets:**
- `project_templates/youtube_video_template.prproj` - YouTube video template
- `presets/export_presets/youtube_1080p.epr` - YouTube export preset
- `presets/effect_presets/color_grade_cinematic.prfpset` - Color grade preset
- `presets/text_presets/lower_third.mogrt` - Lower third graphic template
- `resources/music/background_music.mp3` - Background music tracks
- `resources/graphics/lower_thirds/` - Lower third templates
- `examples/example_project/` - Complete project showing techniques

### Conversion Checklist - Video Skills

- [ ] Employee skill JSON analyzed
- [ ] Skill name created (format: [artifact]-[action]-[tool])
- [ ] Description includes artifact + tool + triggers
- [ ] Prerequisites documented (software, hardware, project setup)
- [ ] Workflow overview with phase breakdown
- [ ] Each phase detailed with steps
- [ ] Tool-specific features documented
- [ ] Keyboard shortcuts included
- [ ] Export settings for multiple use cases
- [ ] Advanced techniques section
- [ ] Performance optimization tips
- [ ] Troubleshooting section
- [ ] Examples from example_tasks
- [ ] References created (tool guide, techniques, shortcuts, codecs)
- [ ] Scripts created for automation (if applicable)
- [ ] Assets added (CRITICAL - templates, presets, resources, examples)
- [ ] All templates/presets tested in actual tool
- [ ] SKILL.md under 500 lines

---

## Resource Planning Templates

### Decision Matrix: What Resources to Create

**Use this matrix to decide which resources to create for each skill:**

| Criteria | Create scripts/ | Create references/ | Create assets/ |
|----------|----------------|-------------------|----------------|
| automation_potential: high/very high | ✅ YES | Maybe | Maybe |
| automation_potential: medium | Maybe | ✅ YES | Maybe |
| automation_potential: low | ❌ NO | ✅ YES | Maybe |
| difficulty_level: advanced/expert | Maybe | ✅ YES | Maybe |
| difficulty_level: intermediate | Maybe | Maybe | Maybe |
| difficulty_level: beginner | Maybe | Maybe if complex | Maybe |
| Involves templates/forms | Maybe | Maybe | ✅ YES |
| Involves code generation | ✅ YES | ✅ YES | ✅ YES |
| Involves design output | Maybe | ✅ YES | ✅ YES |
| Involves document creation | ✅ if automated | ✅ YES | ✅ YES |
| Tool has complex features | Maybe | ✅ YES | Maybe |
| Requires compliance knowledge | Maybe | ✅ YES | ✅ YES (checklists) |

### Resource Content Templates

**scripts/ README.md Template:**
```markdown
# Scripts for [Skill Name]

## Available Scripts

### [script1.py]
**Purpose:** [What it does]
**Usage:** `python [script1.py] [arguments]`
**Parameters:**
- `[param1]` - [Description]
- `[param2]` - [Description]
**Example:** `python [script1.py] example_value`

### [script2.py]
**Purpose:** [What it does]
**Usage:** `python [script2.py] [arguments]`
**Example:** `python [script2.py] example_value`

## Requirements
[List dependencies]
```

**references/ Index Template:**
```markdown
# References for [Skill Name]

## Quick Navigation

### [Reference Category 1]
- [reference1.md](reference1.md) - [Brief description]
- [reference2.md](reference2.md) - [Brief description]

### [Reference Category 2]
- [reference3.md](reference3.md) - [Brief description]

## How to Use These References

[Guidance on when to reference each document]
```

**assets/ README Template:**
```markdown
# Assets for [Skill Name]

## Templates
- `[template1.ext]` - [What it's for]
- `[template2.ext]` - [What it's for]

## Resources
- `[resource1]/` - [What's inside]
- `[resource2]/` - [What's inside]

## Usage
[How to use these assets]
```

---

## SKILL.md Structure Patterns

### Pattern 1: Workflow-Based (Sequential Process)

**Best for:** HR skills, Sales skills, Video skills

**Structure:**
```markdown
---
name: skill-name
description: [What + When]
---

# Skill Title

## Overview
[Brief description]

## Workflow

### Phase 1: [Name]
[Steps]

### Phase 2: [Name]
[Steps]

### Phase 3: [Name]
[Steps]

## Tool Integration
[How to use tool]

## Examples
[Real examples]

## Resources
[List resources]
```

### Pattern 2: Task-Based (Tool Collection)

**Best for:** Development skills, Design skills

**Structure:**
```markdown
---
name: skill-name
description: [What + When]
---

# Skill Title

## Overview
[Brief description]

## Quick Start
[Minimal example]

## Task 1: [Task Name]
[How to do task 1]

## Task 2: [Task Name]
[How to do task 2]

## Task 3: [Task Name]
[How to do task 3]

## Best Practices
[Guidelines]

## Examples
[Real examples]

## Resources
[List resources]
```

### Pattern 3: Reference/Guidelines (Standards)

**Best for:** Compliance-heavy skills, Standards documentation

**Structure:**
```markdown
---
name: skill-name
description: [What + When]
---

# Skill Title

## Overview
[Brief description]

## Guidelines

### Guideline Category 1
[Rules and standards]

### Guideline Category 2
[Rules and standards]

## Specifications
[Detailed specs]

## Examples
[Application examples]

## Resources
[List resources]
```

### Pattern 4: Capabilities-Based (Integrated System)

**Best for:** Complex automation skills, Platform skills

**Structure:**
```markdown
---
name: skill-name
description: [What + When]
---

# Skill Title

## Overview
[Brief description]

## Core Capabilities

### Capability 1: [Name]
[What it does]
[How to use it]

### Capability 2: [Name]
[What it does]
[How to use it]

### Capability 3: [Name]
[What it does]
[How to use it]

## Integration
[How capabilities work together]

## Examples
[Real examples]

## Resources
[List resources]
```

---

## Conversion Quality Checklist

**Use this checklist for EVERY skill conversion:**

### Frontmatter Validation
- [ ] `name:` field present and follows [object]-[action] format
- [ ] `name:` is hyphen-case, under 40 characters
- [ ] `description:` field present
- [ ] `description:` includes WHAT the skill does
- [ ] `description:` includes WHEN to use it (3+ trigger phrases)
- [ ] `description:` mentions tool/technology used
- [ ] YAML frontmatter is valid (no syntax errors)

### Content Validation
- [ ] Overview section exists (1-2 sentences)
- [ ] Main body follows appropriate pattern (workflow/task/reference/capability)
- [ ] Clear structure with logical flow
- [ ] Examples section with concrete examples from employee skill
- [ ] Resources section referencing bundled resources (if any)
- [ ] SKILL.md is under 500 lines
- [ ] If over 500 lines, content split to references/

### Attribute Preservation
- [ ] Original skill_phrase reflected in name and triggers
- [ ] Action and object from employee skill preserved
- [ ] Tool mentioned and integration explained
- [ ] Difficulty level appropriate to instructions complexity
- [ ] Related skills noted (if applicable)
- [ ] Example tasks incorporated

### Resource Validation
- [ ] scripts/ created if automation_potential: high
- [ ] All scripts tested and working
- [ ] Scripts documented with usage examples
- [ ] references/ created if difficulty: advanced OR detail needed
- [ ] References organized logically
- [ ] References include table of contents if >100 lines
- [ ] assets/ created if templates/boilerplate needed
- [ ] All assets tested and ready to use

### System Integration
- [ ] Ready to assign SKL.XX ID
- [ ] Can be registered in skills_index.md
- [ ] Follows System principles
- [ ] Can be packaged with package_skill.py

---

**Created:** 2025-12-07
**Status:** Complete
**Usage:** Use these templates to convert each of the 28 employee skills
**Next:** See [employee_skills_inventory.md](employee_skills_inventory.md) for prioritized list of skills to convert

