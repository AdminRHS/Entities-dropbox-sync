# MAIN_PROMPT v6 (DRAFT)
**Version:** 6.0
**Date:** November 15, 2025
**Based On:** Learnings from v5 Modular implementation
**Status:** DRAFT - Proposed improvements for next version

---

## Overview

MAIN_PROMPT v6 builds on the successful v5 Modular architecture, adding intelligent automation, enhanced compression, and advanced recognition patterns. This version focuses on making the system more autonomous, efficient, and user-friendly.

**Key Improvements Over v5:**
- ✅ Auto-assembly system (intelligent module loading)
- ✅ Template recommendation engine (AI suggests relevant templates)
- ✅ Advanced compression framework (adaptive compression levels)
- ✅ Recognition pattern library (formalized trigger detection)
- ✅ Validation automation (quality gates)
- ✅ Department auto-detection (smart library loading)
- ✅ Confidence scoring (rate template relevance)
- ✅ Light mode templates (reduced versions for tight budgets)
- ✅ Progressive disclosure (expand sections on-demand)
- ✅ Template chains (pre-defined workflows)

---

## Architecture

### Hierarchical Module System

```
MAIN_PROMPT_v6/
│
├── Level 1: CORE (Always Load) - 2,000 tokens
│   ├── 01_Meeting_Overview.md
│   ├── 02_Participant_Directory.md
│   ├── 03_Employee_Directory.md (Single source of truth)
│   ├── 04_Project_Directory.md
│   └── 05_AI_Instructions.md (Enhanced with auto-assembly logic)
│
├── Level 2: LIBRARIES (Selective Load) - 1,000-3,100 tokens
│   ├── Common/ (Always Load) - 1,000 tokens
│   │   └── 00_Common_Libraries.md
│   │       ├── Professions (27)
│   │       ├── Core Prompts (5)
│   │       ├── Results Overview
│   │       └── Responsibilities Formula
│   │
│   ├── Department/ (Load 1-2 based on participants) - 1,200-2,100 tokens each
│   │   ├── 01_HR_Libraries.md (87 params)
│   │   ├── 02_AI_Libraries.md (75+ tools FULL)
│   │   ├── 03_Video_Libraries.md
│   │   ├── 04_Sales_Libraries.md (Services 7, Products 39)
│   │   ├── 05_Design_Libraries.md (20 deliverables)
│   │   ├── 06_Dev_Libraries.md (124 params)
│   │   └── 07_LG_Libraries.md (11 employees)
│   │
│   └── Specialized/ (Optional) - 300-500 tokens each
│       ├── 08_Parameters_Lightweight.md (10,596+ summary)
│       ├── 09_Taxonomy_Framework.md (system reference)
│       └── 10_Recognition_Patterns.md (NEW - trigger database)
│
├── Level 3: TEMPLATES (Selective Load) - 3,000-6,000 tokens
│   ├── Essential/ (Always Include) - 600-1,000 tokens
│   │   ├── 01_Meeting_Metadata.md
│   │   ├── 02_Executive_Summary.md
│   │   └── 21_Follow_Up_Items.md
│   │
│   ├── High-Value/ (Usually Include) - 1,500-2,500 tokens
│   │   ├── 03_Action_Items_Tasks.md (⭐⭐⭐)
│   │   ├── 07_Problems_Solutions.md (⭐⭐)
│   │   ├── 10_Decisions_Log.md (⭐)
│   │   ├── 13_Blockers_Dependencies.md (⭐⭐)
│   │   └── 14_Insights_Lessons.md (⭐)
│   │
│   ├── Department-Specific/ (Conditional) - 800-1,200 tokens each
│   │   ├── 16_Employee_Team_Context.md (⭐⭐⭐)
│   │   ├── 17_Lead_Gen_Sales_Context.md (⭐⭐⭐)
│   │   ├── 18_Design_Creative_Context.md (⭐⭐⭐)
│   │   └── 19_Development_Technical_Context.md (⭐⭐⭐)
│   │
│   ├── Contextual/ (Optional) - 1,000-1,500 tokens
│   │   ├── 04_Projects_Features.md (⭐⭐⭐)
│   │   ├── 05_Workflows_Processes.md (⭐⭐⭐)
│   │   ├── 06_Rules_Best_Practices.md (⭐⭐⭐)
│   │   ├── 08_Tools_Resources.md (⭐⭐⭐)
│   │   ├── 09_Technical_Architecture.md (⭐⭐⭐)
│   │   ├── 11_Documentation_Gaps.md (⭐)
│   │   ├── 12_Communication_Announcements.md (⭐)
│   │   ├── 15_Analogies_Frameworks.md (⭐)
│   │   └── 20_Onboarding_Training_Context.md (⭐⭐)
│   │
│   └── Light_Mode/ (NEW - Reduced versions) - 200-400 tokens each
│       ├── 03_Action_Items_LIGHT.md (⭐)
│       ├── 08_Tools_Resources_LIGHT.md (⭐)
│       └── 16_Employee_Team_Context_LIGHT.md (⭐)
│
├── Level 4: PROCESSING RULES (Automated) - 1,000-1,500 tokens
│   ├── 01_Recognition_Patterns.md (Trigger detection)
│   ├── 02_Entity_Extraction.md (Find Actions, Tools, etc.)
│   ├── 03_Validation_Rules.md (Quality gates)
│   ├── 04_Prioritization_Logic.md (Template ranking)
│   ├── 05_Confidence_Scoring.md (NEW - Relevance rating)
│   └── 06_Error_Handling.md (Edge cases)
│
└── Level 5: ASSEMBLY & ORCHESTRATION (Automated)
    ├── 01_Auto_Assembly.py (NEW - Intelligent module loader)
    ├── 02_Template_Recommender.py (NEW - AI template selection)
    ├── 03_Compression_Engine.py (NEW - Adaptive compression)
    ├── 04_Validation_Checker.py (Automated validation)
    └── 05_Output_Generator.py (Formatted output)
```

---

## Key Innovations in v6

### 1. Auto-Assembly System (NEW)

**Purpose:** Automatically load correct modules based on meeting metadata

**How It Works:**
```
INPUT: Meeting metadata (participants, topics, duration, type)
↓
STEP 1: Detect departments from participants
  - Look up each participant in Employee Directory
  - Extract department(s)
  - Example: Olha (Dev), Hanan (LG), Anastasiia (Design) → Departments: [Dev, LG, Design]
↓
STEP 2: Load core modules (always)
  - 00_Core/ (5 files, ~2,000 tokens)
↓
STEP 3: Load common libraries (always)
  - 00_Common_Libraries.md (~1,000 tokens)
↓
STEP 4: Load department libraries (selective)
  - For each detected department, load corresponding library
  - Dev → 06_Dev_Libraries.md (~1,800 tokens)
  - LG → 07_LG_Libraries.md (~1,600 tokens)
  - Design → 05_Design_Libraries.md (~1,300 tokens)
  - Total: ~4,700 tokens (vs 8,000-12,000 if all loaded)
↓
STEP 5: Analyze meeting topics/content (NEW)
  - Extract keywords, themes, sentiment
  - Identify potential template triggers
  - Example: "decided," "blocker," "action item," "quality standard"
↓
STEP 6: Recommend templates (NEW - see Template Recommender)
  - Score each template by relevance (0-100)
  - Select top 10-15 templates (within token budget)
  - Prioritize: Essential (always) + High-Value (if relevant) + Contextual (if triggered)
↓
STEP 7: Load selected templates
  - Essential: 01, 02, 21 (~1,000 tokens)
  - High-Value: 03, 07, 10, 13, 14 (~2,000 tokens)
  - Contextual: 04, 08, 19 (~1,500 tokens)
  - Total: ~4,500 tokens
↓
STEP 8: Assemble final prompt
  - Core (2,000) + Common (1,000) + Departments (4,700) + Templates (4,500)
  - Total: ~12,200 tokens (context) + Meeting transcript (variable)
  - Leaves ~135,000 tokens for transcript and output
↓
OUTPUT: Optimized prompt ready for AI processing
```

**Benefits:**
- 40-70% smaller prompts vs monolithic approach
- Relevant context only (no noise)
- Automatic (no manual selection)
- Adaptive (adjusts to meeting type)

**Implementation:**
```python
# Auto-Assembly Pseudocode
def assemble_prompt(meeting_metadata, transcript):
    prompt = []

    # Always load core
    prompt += load_core_modules()

    # Always load common libraries
    prompt += load_common_libraries()

    # Detect departments
    departments = detect_departments(meeting_metadata.participants)

    # Load department libraries
    for dept in departments:
        prompt += load_department_library(dept)

    # Analyze content for template triggers
    triggers = analyze_content(transcript)

    # Recommend templates
    templates = recommend_templates(triggers, meeting_metadata)

    # Load templates
    for template in templates:
        prompt += load_template(template)

    # Add processing rules
    prompt += load_processing_rules()

    return assemble(prompt)
```

---

### 2. Template Recommendation Engine (NEW)

**Purpose:** AI suggests most relevant templates based on meeting content

**How It Works:**
```
INPUT: Meeting transcript + metadata
↓
STEP 1: Extract triggers
  - Keywords: "decided," "blocked," "action," "problem," "standard," etc.
  - Entities: Employee names, tool names, project names
  - Sentiment: Frustration, excitement, uncertainty
  - Structure: Q&A, brainstorming, status update, decision-making
↓
STEP 2: Score templates
  - For each template, calculate relevance score (0-100)
  - Scoring factors:
    * Keyword match (30 points): How many trigger words present?
    * Entity match (25 points): How many relevant entities detected?
    * Sentiment match (15 points): Does sentiment align with template purpose?
    * Context match (20 points): Does meeting structure fit template?
    * Historical usage (10 points): How often used for similar meetings?
↓
STEP 3: Apply constraints
  - Essential templates (01, 02, 21): Always include (mandatory)
  - Token budget: Ensure total tokens < budget
  - Department fit: Prioritize department-specific templates for detected departments
↓
STEP 4: Rank and select
  - Sort templates by score (descending)
  - Select top N templates within token budget
  - Ensure diversity (mix of ⭐, ⭐⭐, ⭐⭐⭐ templates)
↓
OUTPUT: Ranked list of recommended templates with confidence scores
```

**Example:**
```
Meeting: Dev team discussing auth microservice bug

Detected Triggers:
- Keywords: "bug," "fix," "production," "downtime," "decision," "architecture"
- Entities: Olha, Yaroslav, auth microservice, PostgreSQL, Redis
- Sentiment: Urgency (production outage)
- Structure: Problem-solving + decision-making

Template Scores:
1. 07_Problems_Solutions.md - 95% (HIGH - "bug," "production," "downtime")
2. 19_Development_Technical_Context.md - 92% (HIGH - Dev department, technical terms)
3. 10_Decisions_Log.md - 88% (HIGH - "decision," "architecture")
4. 03_Action_Items_Tasks.md - 85% (HIGH - "fix," action-oriented)
5. 09_Technical_Architecture.md - 82% (MEDIUM - "architecture," "microservice")
6. 13_Blockers_Dependencies.md - 78% (MEDIUM - "production," urgency)
7. 08_Tools_Resources.md - 65% (MEDIUM - PostgreSQL, Redis mentioned)
8. 14_Insights_Lessons.md - 60% (LOW - learning opportunity)
9. 21_Follow_Up_Items.md - 100% (MANDATORY - always include)
10. 01_Meeting_Metadata.md - 100% (MANDATORY - always include)
11. 02_Executive_Summary.md - 100% (MANDATORY - always include)

Selected Templates (Top 10 within budget):
✅ 01, 02, 21 (Essential - mandatory)
✅ 03, 07, 10, 13, 19 (High-Value - relevant)
✅ 08, 09 (Contextual - relevant)

Total: 10 templates, ~5,000 tokens
```

**Implementation:**
```python
# Template Recommender Pseudocode
def recommend_templates(triggers, metadata):
    scores = {}

    for template in all_templates:
        # Score based on trigger matching
        keyword_score = match_keywords(triggers.keywords, template.recognition_rules)
        entity_score = match_entities(triggers.entities, template.entity_types)
        sentiment_score = match_sentiment(triggers.sentiment, template.sentiment_indicators)
        context_score = match_context(metadata.structure, template.context_patterns)
        history_score = get_historical_usage(metadata.type, template)

        # Calculate total score (0-100)
        total_score = (
            keyword_score * 0.30 +
            entity_score * 0.25 +
            sentiment_score * 0.15 +
            context_score * 0.20 +
            history_score * 0.10
        )

        scores[template] = total_score

    # Sort by score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Apply constraints (essential, token budget, diversity)
    selected = apply_constraints(ranked, metadata.token_budget)

    return selected
```

---

### 3. Advanced Compression Framework (NEW)

**Purpose:** Adaptively compress content based on prompt budget

**Compression Levels:**

**Level 1: LIGHT (90% compression)**
- Use cases: Tight token budget, quick meetings, summary-only
- Keep: Overview, top 10-20 items, links to full data
- Example: Parameters (61K lines) → Summary (300 lines)

**Level 2: MEDIUM (50% compression)**
- Use cases: Standard meetings, balanced detail
- Keep: Overview, top 50-100 items, key examples
- Example: Tools library (75 tools) → Top 40 tools + summaries

**Level 3: FULL (No compression)**
- Use cases: Deep analysis, complex meetings, full context needed
- Keep: Everything (all 75 tools, all 429 actions, etc.)

**Adaptive Compression:**
```python
def compress_content(content, available_tokens):
    # Calculate required tokens for full content
    full_tokens = estimate_tokens(content)

    # If within budget, no compression
    if full_tokens <= available_tokens:
        return content, "FULL"

    # If 2x over budget, use MEDIUM compression
    elif full_tokens <= available_tokens * 2:
        return compress(content, level="MEDIUM"), "MEDIUM"

    # If >2x over budget, use LIGHT compression
    else:
        return compress(content, level="LIGHT"), "LIGHT"
```

**Example:**
```
Scenario: Dev meeting, tight token budget (only 5,000 tokens available for templates)

Without Adaptive Compression:
- Load all templates (15 templates × 500 avg tokens = 7,500 tokens)
- OVER BUDGET by 2,500 tokens → Can't fit

With Adaptive Compression:
- Detect: Need 7,500 tokens, have 5,000 → 50% over budget
- Apply: MEDIUM compression to Heavy templates (⭐⭐⭐)
  * 03_Action_Items_Tasks.md: FULL → MEDIUM (800 → 400 tokens)
  * 08_Tools_Resources.md: FULL → MEDIUM (600 → 300 tokens)
  * 19_Dev_Technical_Context.md: FULL → MEDIUM (1,000 → 500 tokens)
- Result: 7,500 → 5,700 tokens
- Still over by 700 tokens → Compress 2 more templates to LIGHT
- Final: 5,000 tokens (FITS IN BUDGET)
```

---

### 4. Recognition Pattern Library (NEW)

**Purpose:** Formalized database of triggers for template activation

**Pattern Types:**

**1. Keyword Triggers**
```json
{
  "template": "10_Decisions_Log.md",
  "triggers": {
    "direct_keywords": ["decided", "decision", "choose", "selected", "approved", "going with"],
    "implicit_keywords": ["should we", "what if we", "option A vs option B", "alternatives"],
    "negation_keywords": ["decided not to", "rejected", "declined", "not proceeding"]
  },
  "confidence": {
    "high": "Direct keyword + decision maker identified",
    "medium": "Implicit keyword + alternatives discussed",
    "low": "Negation keyword only"
  }
}
```

**2. Entity Triggers**
```json
{
  "template": "08_Tools_Resources.md",
  "triggers": {
    "tool_names": ["Figma", "Apollo.io", "GitHub", "Slack", "Docker", "AWS", "etc."],
    "tool_categories": ["design tool", "development tool", "automation"],
    "tool_actions": ["using", "switching to", "upgrading", "configuring"]
  },
  "confidence": {
    "high": "Tool name + action verb",
    "medium": "Tool name mentioned",
    "low": "Tool category only"
  }
}
```

**3. Sentiment Triggers**
```json
{
  "template": "07_Problems_Solutions.md",
  "triggers": {
    "frustration": ["stuck", "blocked", "not working", "broken", "issue", "problem"],
    "urgency": ["critical", "production", "urgent", "ASAP", "immediately"],
    "resolution": ["fixed", "solved", "resolved", "working now"]
  },
  "confidence": {
    "high": "Frustration + urgency",
    "medium": "Frustration only",
    "low": "Resolution mentioned (problem implied)"
  }
}
```

**4. Structure Triggers**
```json
{
  "template": "13_Blockers_Dependencies.md",
  "triggers": {
    "blocker_structure": "Task A depends on Task B (not yet done)",
    "waiting_structure": "Waiting for [person/thing]",
    "dependency_chain": "Can't do X until Y is complete"
  },
  "confidence": {
    "high": "Explicit blocker + impact stated",
    "medium": "Dependency mentioned",
    "low": "Waiting mentioned (reason unclear)"
  }
}
```

**Implementation:**
```python
# Recognition Pattern Matching
def detect_triggers(transcript):
    triggers = {
        "keywords": [],
        "entities": [],
        "sentiment": [],
        "structure": []
    }

    # Load recognition patterns
    patterns = load_recognition_patterns()

    # Match keywords
    for pattern in patterns:
        for keyword in pattern.keywords:
            if keyword in transcript.lower():
                triggers["keywords"].append({
                    "keyword": keyword,
                    "template": pattern.template,
                    "confidence": calculate_confidence(keyword, pattern)
                })

    # Match entities (names, tools, projects)
    entities = extract_entities(transcript)
    for entity in entities:
        matching_templates = find_templates_for_entity(entity)
        triggers["entities"].append({
            "entity": entity,
            "templates": matching_templates,
            "confidence": "high"  # Entity matches are high-confidence
        })

    # Match sentiment
    sentiment = analyze_sentiment(transcript)
    triggers["sentiment"] = sentiment

    # Match structure
    structure = analyze_structure(transcript)
    triggers["structure"] = structure

    return triggers
```

---

### 5. Confidence Scoring (NEW)

**Purpose:** Rate how confident AI is that template is relevant

**Scoring System:**

**HIGH Confidence (80-100%)**
- Multiple strong triggers detected
- Entities clearly match template domain
- Historical usage aligns
- Example: "We decided to hire..." → 95% confidence for Decisions Log

**MEDIUM Confidence (50-79%)**
- Some triggers detected
- Indirect indicators present
- Could be relevant
- Example: "Let's think about..." → 60% confidence for Decisions Log

**LOW Confidence (20-49%)**
- Weak triggers
- Speculative match
- Include only if token budget allows
- Example: "Maybe we should..." → 40% confidence for Decisions Log

**VERY LOW Confidence (<20%)**
- No clear triggers
- Likely not relevant
- Exclude unless user requests
- Example: No decision language → 10% confidence for Decisions Log

**Usage in Output:**
```markdown
## Templates Used (with confidence scores)

✅ 03_Action_Items_Tasks.md - 95% confidence (HIGH)
  - Triggers: "action item" (5×), employee assignments (8×), deadlines (12×)

✅ 07_Problems_Solutions.md - 88% confidence (HIGH)
  - Triggers: "problem" (3×), "solution" (4×), "fix" (7×), frustration sentiment

✅ 10_Decisions_Log.md - 82% confidence (HIGH)
  - Triggers: "decided" (2×), "approved" (1×), alternatives discussed

⚠️ 15_Analogies_Frameworks.md - 45% confidence (LOW)
  - Triggers: "like" (metaphor indicator) mentioned 2× (weak signal)
  - Note: Included due to token budget availability; review may be optional
```

**Benefits:**
- Users know which sections to prioritize
- Can skip low-confidence sections if reviewing quickly
- Helps calibrate AI recommendations over time

---

### 6. Light Mode Templates (NEW)

**Purpose:** Reduced versions of Heavy templates (⭐⭐⭐ → ⭐) for tight budgets

**Example: Action Items (FULL vs LIGHT)**

**FULL Mode (03_Action_Items_Tasks.md - ⭐⭐⭐):**
```markdown
#### 1. Fix Authentication Bug
- **Owner:** Olha Kizilova (ID: 178) - Backend Developer
- **Action:** ACT-DEV-004 - Fix bug
- **Object:** OBJ-DEV-001 - Code
- **Responsibility:** Fix bug + Code = Debug and repair code
- **Required Skill:** SKL-DEV-003 - Backend debugging
- **Deadline:** 2025-11-15, 3:00 PM
- **Priority:** CRITICAL
- **Dependencies:** None
- **Related Process:** PROC-DEV-001
- **Expected Result:** RES-DEV-001
[...500 words of detail...]
```
**Tokens:** ~200

**LIGHT Mode (03_Action_Items_Tasks_LIGHT.md - ⭐):**
```markdown
#### 1. Fix Authentication Bug
- **Owner:** Olha Kizilova
- **What:** Fix auth connection leak
- **Due:** 2025-11-15, 3PM
- **Priority:** CRITICAL
```
**Tokens:** ~30

**Reduction:** 85% smaller (200 → 30 tokens)

**When to Use:**
- Quick status meetings
- Tight token budgets
- Summary-only outputs
- Mobile/email formats (brevity required)

**Available Light Templates:**
- 03_Action_Items_LIGHT.md
- 08_Tools_Resources_LIGHT.md
- 16_Employee_Team_Context_LIGHT.md
- 17_Lead_Gen_Sales_Context_LIGHT.md
- 18_Design_Creative_Context_LIGHT.md
- 19_Development_Technical_Context_LIGHT.md

---

### 7. Progressive Disclosure (NEW)

**Purpose:** Start with high-level summary, expand sections on-demand

**Example:**

**Initial Output (Summary Level):**
```markdown
## Problems & Solutions (Click to Expand)

**Problems Discussed:** 3
**Critical Issues:** 1 (Auth microservice bug - RESOLVED)
**High Priority:** 2 (CI/CD pipeline slow, Code review bottleneck)

[Click to see full details...]
```

**Expanded (Full Details):**
```markdown
## Problems & Solutions

### Critical Issues

#### Authentication API Failure - Dev Department
- **Blocked Item:** Client A dashboard project
- **Blocked By:** Missing senior React expertise
[...full 2,000-word detailed analysis...]
```

**Implementation:**
```markdown
<!-- Summary Mode -->
<summary>
## Problems & Solutions
**Problems:** 3 | **Critical:** 1 | **Status:** 1 resolved, 2 in progress
</summary>

<!-- Full Details (hidden by default) -->
<details>
<summary>Expand for full details</summary>

[...complete template content...]

</details>
```

**Benefits:**
- Quick scanning (summary view)
- Deep dive available (expand on-demand)
- Reduces initial output size (faster generation)
- Better UX (progressive complexity)

---

### 8. Template Chains (NEW)

**Purpose:** Pre-defined template sequences for common workflows

**Chain Examples:**

**Change Management Chain:**
```
Problem Identified (Template 07)
  ↓
Solution Proposed (Template 07)
  ↓
Decision Made (Template 10)
  ↓
Action Items Created (Template 03)
  ↓
Communication Sent (Template 12)
  ↓
Follow-Up Tracked (Template 21)
```

**Project Launch Chain:**
```
Project Discussed (Template 04)
  ↓
Team Assigned (Template 16)
  ↓
Workflows Defined (Template 05)
  ↓
Tools Selected (Template 08)
  ↓
Architecture Designed (Template 09)
  ↓
Action Items Created (Template 03)
  ↓
Follow-Up Tracked (Template 21)
```

**Quality Improvement Chain:**
```
Quality Issue Identified (Template 07)
  ↓
Standards Discussed (Template 06)
  ↓
Decision Made (Template 10)
  ↓
Training Needed (Template 20)
  ↓
Documentation Created (Template 11)
  ↓
Follow-Up Tracked (Template 21)
```

**Usage:**
```python
# Activate template chain
def activate_chain(chain_name, triggers):
    if chain_name == "change_management":
        # Load templates in sequence
        templates = [
            "07_Problems_Solutions.md",
            "10_Decisions_Log.md",
            "03_Action_Items_Tasks.md",
            "12_Communication_Announcements.md",
            "21_Follow_Up_Items.md"
        ]

        # Ensure continuity (cross-references)
        link_templates(templates)

        return templates
```

**Benefits:**
- Ensures workflow continuity
- Reduces manual template selection
- Captures complete narrative (problem → solution → action → follow-up)
- Improves cross-referencing

---

## Processing Workflow (v6)

### Enhanced 8-Step Process

**STEP 1: Input Validation & Preparation (5 min)**
- Validate meeting transcript format
- Extract metadata (date, participants, duration, type)
- Detect departments from participants → Employee Directory lookup
- Identify meeting language (English, Spanish, etc.)
- **NEW:** Run pre-processing checks (is transcript complete? quality sufficient?)

**STEP 2: Auto-Assembly (2 min)**
- Load Core modules (always)
- Load Common libraries (always)
- Load Department libraries (based on detected departments)
- **NEW:** Check token budget, apply compression if needed

**STEP 3: Content Analysis & Trigger Detection (10 min)**
- **NEW:** Extract triggers (keywords, entities, sentiment, structure)
- **NEW:** Match triggers against Recognition Pattern Library
- **NEW:** Calculate confidence scores for each potential template
- Identify key themes, topics, decisions

**STEP 4: Template Recommendation & Selection (3 min)**
- **NEW:** Run Template Recommender (score all templates 0-100)
- **NEW:** Select top N templates (essential + high-value + contextual)
- **NEW:** Apply constraints (token budget, diversity, department fit)
- Load selected templates

**STEP 5: Entity Extraction & Library Integration (15 min)**
- Extract entities from transcript:
  * **Employees:** Match to Employee Directory → IDs, positions, departments
  * **Actions:** Match to Responsibilities/Responsibilities/Actions library (429 actions) → ACT-XXX IDs
  * **Tools:** Match to Tools library (75+ tools) → TOOL-XXX IDs
  * **Processes:** Match to Processes library (428 processes) → PROC-XXX IDs
  * **Projects:** Match to Project Directory (27+ projects) → Project IDs
  * **Products/Services:** Match to Products (39), Services (7) libraries
  * **Parameters:** Match to Parameters library (10,596+ parameters)
- **NEW:** Apply Responsibility Formula (Action + Object = Responsibility)
- **NEW:** Apply Skill Formula (Responsibility + Tool = Skill)
- Cross-reference entities (e.g., Employee assigned to Action using Tool on Project)

**STEP 6: Template Population & Quality Checks (30 min)**
- Populate each selected template with extracted data
- Apply template-specific rules (recognition patterns, validation logic)
- **NEW:** Run validation checks (Checklist Items, required fields, cross-references)
- **NEW:** Calculate confidence scores for each populated section
- Ensure cross-references valid (all IDs exist in libraries)

**STEP 7: Output Generation & Formatting (15 min)**
- Assemble final output (combine all templates)
- Format markdown (headers, tables, lists, checkboxes)
- Add metadata (templates used, confidence scores, token usage)
- **NEW:** Generate summary view + detailed view (progressive disclosure)
- **NEW:** Highlight high-confidence sections, flag low-confidence sections

**STEP 8: Validation & Quality Assurance (10 min)**
- **NEW:** Run automated validation checks (Quality Gates)
- Verify all action items have owners and deadlines
- Ensure all blockers have resolution plans
- Check all decisions have rationale and implementation plans
- Validate all cross-references (no broken links)
- **NEW:** Generate validation report (pass/fail for each quality gate)
- Final review and adjustments

**Total Processing Time:** ~90 minutes (automated, most steps are AI-driven)

---

## Quality Gates (v6)

### Gate 1: Input Validation
```
✅ Meeting transcript present and complete?
✅ Metadata extracted (date, participants, duration)?
✅ Departments detected (at least 1)?
✅ Transcript language identified?
✅ Transcript quality sufficient (not truncated, readable)?

IF ALL ✅ → Proceed to Gate 2
IF ANY ❌ → Flag issues, request user input
```

### Gate 2: Assembly Validation
```
✅ Core modules loaded?
✅ Common libraries loaded?
✅ Department libraries loaded (at least 1)?
✅ Templates selected (at least 3 essential)?
✅ Token budget sufficient (not exceeded)?
✅ No duplicate content loaded?

IF ALL ✅ → Proceed to Gate 3
IF ANY ❌ → Apply compression or reduce templates
```

### Gate 3: Processing Validation
```
✅ Triggers detected (at least 5)?
✅ Entities extracted (employees, actions, tools)?
✅ Cross-references created?
✅ Library IDs validated (all IDs exist)?
✅ Confidence scores calculated?

IF ALL ✅ → Proceed to Gate 4
IF ANY ❌ → Flag low-quality sections, reduce confidence scores
```

### Gate 4: Output Validation
```
✅ All selected templates populated?
✅ Validation checklists passed (>80% items checked)?
✅ Action items have owners and deadlines?
✅ Decisions have rationale and implementation plans?
✅ Blockers have resolution plans?
✅ Follow-up items tracked?
✅ Cross-references valid (no broken links)?
✅ Quality thresholds met (confidence >50% avg)?

IF ALL ✅ → Output approved, deliver to user
IF ANY ❌ → Generate validation report, highlight issues
```

---

## Token Budget Management (v6)

### Budget Allocation (200,000 total tokens)

```
TOTAL BUDGET: 200,000 tokens

ALLOCATION:
├── Core Modules: 2,000 tokens (1% - FIXED)
├── Common Libraries: 1,000 tokens (0.5% - FIXED)
├── Department Libraries: 1,200-4,700 tokens (0.6-2.4% - VARIABLE)
│   └── Load 1-3 departments based on participants
├── Templates: 3,000-8,000 tokens (1.5-4% - VARIABLE)
│   └── Load 10-15 templates based on relevance
├── Processing Rules: 1,000-1,500 tokens (0.5-0.75% - FIXED)
├── Meeting Transcript: 100,000-140,000 tokens (50-70% - VARIABLE)
│   └── Main input content
├── Output Generation: 5,000-15,000 tokens (2.5-7.5% - RESERVED)
│   └── AI response generation
└── Buffer: 20,000-40,000 tokens (10-20% - SAFETY MARGIN)
    └── Unexpected complexity, edge cases

CONTEXT USAGE: ~110,000-150,000 tokens (55-75%)
OUTPUT RESERVED: ~5,000-15,000 tokens (2.5-7.5%)
BUFFER: ~20,000-40,000 tokens (10-20%)
```

### Adaptive Budget Management

**Scenario 1: Simple HR Meeting (Low Complexity)**
```
Participants: 3 (all HR department)
Duration: 30 minutes
Transcript: ~5,000 words = ~7,000 tokens

Budget Allocation:
- Core: 2,000
- Common: 1,000
- HR Library: 1,200
- Templates (8 selected): 3,000
- Processing: 1,000
- Transcript: 7,000
- TOTAL CONTEXT: 15,200 tokens (7.6% of budget)
- Output Reserve: 10,000 tokens
- Buffer: 174,800 tokens (plenty of room)

Compression: NONE needed (well within budget)
```

**Scenario 2: Complex Multi-Department Meeting (High Complexity)**
```
Participants: 12 (Dev, Design, LG, Sales)
Duration: 2 hours
Transcript: ~30,000 words = ~40,000 tokens

Budget Allocation:
- Core: 2,000
- Common: 1,000
- Dept Libraries (4 depts): 5,200
- Templates (15 selected): 6,000
- Processing: 1,500
- Transcript: 40,000
- TOTAL CONTEXT: 55,700 tokens (27.9% of budget)
- Output Reserve: 15,000 tokens
- Buffer: 129,300 tokens (comfortable)

Compression: LIGHT on 2-3 Heavy templates (saves ~1,500 tokens)
```

**Scenario 3: Very Long Meeting (Edge Case)**
```
Participants: 8 (Dev, Design)
Duration: 4 hours
Transcript: ~80,000 words = ~110,000 tokens

Budget Allocation:
- Core: 2,000
- Common: 1,000
- Dept Libraries (2 depts): 3,100
- Templates (12 selected): 5,000
- Processing: 1,200
- Transcript: 110,000
- TOTAL CONTEXT: 122,300 tokens (61.2% of budget)
- Output Reserve: 15,000 tokens
- Buffer: 62,700 tokens (tight but manageable)

Compression: MEDIUM on Heavy templates (saves ~3,000 tokens)
Consider: Summarize transcript (reduce 110K → 80K) if needed
```

**Scenario 4: Budget Exceeded (Failure Case)**
```
Transcript: 150,000 tokens (too large)

Options:
1. Chunk transcript (split into 2 meetings, process separately)
2. Aggressive compression (LIGHT mode on all templates)
3. Summarize transcript (AI pre-processing to reduce to 80K tokens)
4. Selective template loading (only essential + 3-5 contextual)

Recommended: Option 3 (summarize) + Option 2 (LIGHT templates)
Result: 80K transcript + 8K context = 88K total (within budget)
```

---

## Implementation Roadmap

### Phase 1: Foundation (Complete in v5)
- ✅ Modular architecture (Core, Libraries, Templates)
- ✅ Department-based organization
- ✅ 21 comprehensive templates
- ✅ Validation checklists
- ✅ Cross-referencing

### Phase 2: Automation (v6 - Priority)
- [ ] Auto-assembly system (intelligent module loading)
- [ ] Template recommendation engine (AI selection)
- [ ] Recognition pattern library (formalized triggers)
- [ ] Confidence scoring (relevance rating)
- [ ] Validation automation (quality gates)

### Phase 3: Compression & Optimization (v6 - Priority)
- [ ] Adaptive compression framework (3 levels)
- [ ] Light mode templates (reduced versions)
- [ ] Token budget optimizer (dynamic allocation)
- [ ] Performance monitoring (track token usage)

### Phase 4: Intelligence (v6 - Secondary)
- [ ] Template chains (workflow sequences)
- [ ] Progressive disclosure (expand on-demand)
- [ ] Learning system (improve over time)
- [ ] Anomaly detection (flag unusual meetings)

### Phase 5: Integration (Future - v7)
- [ ] Slack integration (auto-process meeting transcripts)
- [ ] ClickUp integration (create tasks from action items)
- [ ] Notion integration (export to knowledge base)
- [ ] API endpoints (external system access)
- [ ] Multi-language support (Spanish, French, etc.)

---

## Success Metrics

### v6 Goals:

**Efficiency:**
- ✅ 50-80% prompt weight reduction (vs monolithic)
- ✅ <10 seconds assembly time (auto-assembly)
- ✅ <90 minutes total processing time (end-to-end)

**Accuracy:**
- ✅ 95%+ template recommendation accuracy
- ✅ 90%+ entity extraction accuracy
- ✅ 85%+ cross-reference validity

**Quality:**
- ✅ 100% validation checklist completion
- ✅ 80%+ confidence score average
- ✅ 100% quality gates passed

**Usability:**
- ✅ Zero manual template selection (fully automated)
- ✅ Progressive disclosure (summary + details)
- ✅ Clear confidence scores (users know what to trust)

---

## Conclusion

MAIN_PROMPT v6 builds on v5's successful modular foundation by adding:
- **Intelligence** - Auto-assembly, template recommendation, pattern recognition
- **Efficiency** - Adaptive compression, light modes, token optimization
- **Quality** - Confidence scoring, validation automation, quality gates
- **Usability** - Progressive disclosure, template chains, clear metrics

The system becomes more autonomous, efficient, and user-friendly while maintaining the comprehensive coverage and high-quality output established in v5.

**Next Steps:**
1. Implement Phase 2 (Automation) - Priority items
2. Test with realistic meeting scenarios
3. Refine recognition patterns based on testing
4. Iterate and improve

**Status:** DRAFT - Ready for review and implementation planning
