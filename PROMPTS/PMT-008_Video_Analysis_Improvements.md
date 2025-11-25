# Video Transcription Prompt - Analysis & Improvements

**Date:** November 12, 2025
**Prompt Version Analyzed:** v3.0
**Videos Analyzed:** Video_003, Video_004, Video_005, Video_006
**Purpose:** Identify improvements based on real-world transcription results

---

## Executive Summary

After analyzing 4 video transcriptions against the Video_Transcription_Custom_Instructions v3.0 prompt, I've identified several patterns and improvement opportunities:

**Key Findings:**
1. **Format inconsistency** - Videos transcribed in 3 different formats (markdown, JSON, mixed)
2. **Taxonomy extraction quality** - Varies significantly (Video_003 excellent, Video_006 missing)
3. **Character encoding issues** - Video_003 has corrupted text sections (lines 46-207, 352-391)
4. **Browser/Agentic verbs working** - v3.0 addition proving valuable (Video_004 identified need)

---

## Transcription Format Analysis

### Video_003: Kimi K2 Thinking Model (Matthew Berman, 14:31)
**Format:** Markdown with numbered sections
**Quality:** ✅ Excellent taxonomy extraction
**Issues:** ⚠️ Character-by-character corruption in 2 sections

**Structure:**
```markdown
1. Metadata Section (basic fields)
2. Description Section (good detail)
3. Word-for-Word Transcription (timestamps, VISUAL/TEXT tags)
TAXONOMY ANALYSIS (comprehensive)
- Workflows Identified (3 workflows with full structure)
- Action Verbs & Operations (6 categories including new F. category)
- Task Chains
- Responsibilities Vocabulary
- Tools & Technologies Matrix (table format)
- Objects & Deliverables
- Integration Patterns
- Business Concepts & Strategy
- Optimization & Best Practices
```

**Strengths:**
- Complete 6-category action verb extraction (including F. BROWSER/AGENTIC)
- Well-structured workflows with OBJECTIVE, STEPS, DURATION, COMPLEXITY, TOOLS, INPUT, OUTPUT
- Comprehensive tools matrix in table format
- Business strategy insights captured

**Weaknesses:**
- Character encoding corruption: "5.6mworth" appears as individual characters on lines 46-207
- Missing some metadata (video URL, publication date)
- No explicit "markdown document" declaration

---

### Video_004: Perplexity Comet (Matt Wolfe, 38:35)
**Format:** Markdown (well-structured)
**Quality:** ✅ Excellent - Led to v3.0 prompt enhancement
**Issues:** None identified

**Key Discovery:**
This transcription naturally included "F. BROWSER/AGENTIC OPERATIONS" category before it was in the prompt, which led to v3.0 update. Validates the improvement.

---

### Video_005: Agentic Engineering Tech Stack (Cole, 34:24)
**Format:** Markdown (basic)
**Quality:** ⚠️ Basic - Transcription only, no taxonomy analysis yet
**Status:** Phase 1 complete, needs Phases 2-7

**Structure:**
```markdown
### 1. Metadata Section
### 2. Description Section
### 3. Word-for-Word Transcription
(No TAXONOMY ANALYSIS section)
```

**Status:** Awaiting Phase 3+ processing

---

### Video_006: Lead Generation Methods (Nick Saraev, 32:36)
**Format:** ❌ JSON (not markdown)
**Quality:** ⚠️ Transcription only, zero taxonomy extraction
**Issues:** Wrong format entirely

**Structure:**
```json
{
  "metadata": {...},
  "description": {...},
  "transcription": [
    {"timestamp": "00:00", "text": "..."},
    ...
  ]
}
```

**Problems:**
- **Not markdown** - JSON format prevents easy reading/editing
- **No taxonomy analysis** - Missing all taxonomy extraction sections
- **No WORKFLOW structures** - Despite video being 100% about workflows (10 lead gen methods)
- **No action verbs categorization** - Video contains scraping, parsing, enriching, exporting, etc.
- **No tools matrix** - Video mentions 20+ tools (Airscale, Anymailfinder, Apollo, Apify, etc.)

**This is a MAJOR miss** - Video_006 is perfect for taxonomy extraction (10 detailed workflows, 20+ tools, clear processes) but got JSON-only treatment.

---

## Format Inconsistency Root Cause

**Problem:** Transcribers are using 3 different formats
1. **Markdown with taxonomy** (Video_003, Video_004) ✅
2. **Markdown without taxonomy** (Video_005) ⏳
3. **JSON without taxonomy** (Video_006) ❌

**Root Cause Analysis:**
The v3.0 prompt says:
> "IMPORTANT: Output complete structured markdown document."

But this is **buried in line 12**, not emphasized enough. Transcribers may be:
- Using different AI models with different defaults
- Not reading the full prompt
- Using automated tools that default to JSON
- Following old templates

**Impact:**
- Video_006 lost 60+ taxonomy elements (10 workflows, 20+ tools, 50+ action verbs)
- Inconsistent format makes batch processing difficult
- Manual rework required for Video_006

---

## Character Encoding Issues (Video_003)

**Issue:** Text corruption in 2 sections

**Example 1 (lines 46-207):**
```
"5.6mworth" becomes:
5
.
6
m
w
o
r
t
h
```

**Example 2 (lines 352-391):**
Similar corruption for "$5.6 million" and "$3 million"

**Root Cause:** Likely copy-paste or encoding issue during transcription
**Fix:** Need to re-process these sections or add error handling to prompt

---

## Action Verb Categories - V3.0 Validation

### Categories in Use Across Videos:

**A. CREATION VERBS** ✅
- Video_003: Create, Generate, Build, Develop, Write
- Video_006: Would include: Create, Generate, Build (if extracted)

**B. MODIFICATION VERBS** ✅
- Video_003: Fix, Debug, Update
- Video_006: Would include: Enrich, Update, Sanitize, Trim, Filter

**C. ANALYSIS VERBS** ✅
- Video_003: Analyze, Compare, Evaluate, Test, Reason, Compute, Rank
- Video_006: Would include: Analyze, Compare, Evaluate, Parse, Search

**D. ORGANIZATION VERBS** ✅
- Video_003: Plan, Mark off
- Video_006: Would include: Organize, Structure, Categorize, Prioritize

**E. COMMUNICATION VERBS** ✅
- Video_003: Break down, Show, Report
- Video_006: Would include: Export, Share, Send, Pitch

**F. BROWSER/AGENTIC OPERATIONS** ✅✅ (NEW IN V3.0)
- Video_003: Download, Search, Browse, Execute, Click, Save, Deploy
- Video_004: Takes over, Controls, Opens, Clicks, Navigates, Fills in, Submits
- Video_006: Would include: Scrape, Parse, Extract, Download, Export, Feed

**VALIDATION:** Category F is being used naturally! Success!

**MISSING CATEGORY DISCOVERED:**
Video_006 reveals need for:
**G. DATA OPERATIONS** (Processing, transforming, moving data)
- Scrape, Parse, Extract, Feed, Import, Upload, Enrich, Validate, Deduplicate, Sanitize

This overlaps with F (browser/agentic) but is distinct - it's about data manipulation, not UI control.

---

## Workflow Structure Quality

### Video_003 Workflows: ✅ Excellent

**WORKFLOW 1: Analyze Healthcare Data and Create a Dashboard**
```
OBJECTIVE: To analyze the relationship between population density and healthcare facility accessibility in Ghana and generate an interactive web dashboard.
STEPS: (11 detailed steps)
DURATION: A few minutes.
COMPLEXITY: High.
TOOLS USED: Kimi K2 Thinking, OK Computer (internal environment), Web Browser (tool), Code Interpreter (implied).
INPUT: A 4-step natural language prompt detailing the analysis requirements.
OUTPUT: A fully interactive, multi-section HTML dashboard with maps, charts, executive summary, and downloadable CSV files.
```

**Perfect adherence to v3.0 structure!**

### Video_006 Missing Workflows: ❌ Major Loss

Video contains **10 explicit workflows** that should have been extracted:

**WORKFLOW 1: Airscale + Anymailfinder Lead Generation**
```
OBJECTIVE: Generate decision-maker emails from company domains
STEPS:
  1. Search companies in Airscale (location, size, keywords)
  2. Load companies to table
  3. Extract company domains using workflow
  4. Export CSV with domains
  5. Upload to Anymailfinder bulk search
  6. Run decision maker enrichment
  7. Download enriched list with emails
DURATION: 10-15 minutes for 40 records
COMPLEXITY: Medium
TOOLS USED: Airscale, Anymailfinder, Google Sheets
INPUT: Search criteria (location, company size, keywords)
OUTPUT: CSV with company names, domains, decision-maker names, emails, LinkedIn URLs, roles
```

**This pattern repeats 10 times with different tool combinations!**

**Loss:** ~10 workflows, ~20 tools, ~50 action verbs, ~15 integration patterns

---

## Tools Matrix Quality

### Video_003: ✅ Excellent Table Format

```markdown
Tool Name	Category	Purpose	Used For	Mentioned With
Kimi K2 Thinking	Large Language Model	Open-source agentic AI model	Reasoning, tool-use, coding, data analysis	GPT-5, Claude 4.5, DeepSeek R1
DeepSeek R1	Large Language Model	Open-source frontier AI model	Comparison for architecture and performance	Kimi K2 Thinking
...
```

**Perfect!** Table format makes tools matrix highly scannable.

### Video_006: ❌ Missing 20+ Tools

Tools mentioned but not extracted:
1. **Airscale** - Company search platform
2. **Anymailfinder** - Email enrichment service
3. **LinkedIn Sales Navigator** - People search
4. **Vayne** - LinkedIn scraper
5. **Apollo** - Contact database
6. **AmpleLeads** - Apollo scraper
7. **LeadsRapidly** - Apollo scraper
8. **ExportApollo** - Apollo scraper
9. **Apify** - Scraping platform
10. **Google SERP Scraper** - Search results scraper (Apify)
11. **Google Maps Scraper** - Local business scraper (Apify)
12. **Instagram Scraper** - Social media scraper (Apify)
13. **LinkedIn Jobs Scraper** - Job listing scraper (Apify)
14. **n8n** - Workflow automation
15. **Make.com** - Workflow automation
16. **Zapier** - Workflow automation
17. **Bright Data** - Data marketplace
18. **OpenAI GPT-5** - AI model for data extraction
19. **Google Sheets** - Data storage/manipulation
20. **Strudel** - (mentioned in Video_003)

**All lost due to JSON format.**

---

## Recommendations for V3.1

### HIGH PRIORITY

#### 1. **Strengthen Format Requirement** ⭐⭐⭐
**Current (v3.0 line 12):**
> "IMPORTANT: Output complete structured markdown document."

**Proposed (v3.1 - move to top, bold, caps):**
```markdown
# Video Transcription Custom Instructions - Taxonomy Analysis Focus

**CRITICAL OUTPUT REQUIREMENT:**
🔴 **MUST OUTPUT COMPLETE STRUCTURED MARKDOWN DOCUMENT** 🔴
**DO NOT** output JSON, plain text, or any other format.
**REQUIRED FORMAT:** Markdown (.md) with the structure below.

**Purpose**: Transcribe videos with structured extraction...
```

**Rationale:** Video_006's JSON format lost 60+ taxonomy elements. This must be prevented.

---

#### 2. **Add Data Operations Category** ⭐⭐⭐
**Add as new category after F. BROWSER/AGENTIC OPERATIONS:**

```markdown
#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Scrape
- Parse
- Extract
- Feed
- Import
- Upload
- Download
- Export
- Enrich
- Validate
- Verify
- Deduplicate
- Sanitize
- Trim
- Filter
- Transform
- Convert
- Merge
- Split
- [Add others found]

**Note**: This category captures verbs related to data acquisition, processing, and transformation. Distinct from F (browser/agentic) which focuses on UI control, this focuses on data manipulation and ETL operations.
```

**Rationale:** Video_006 has 10 workflows entirely about data scraping/enrichment. Current categories don't capture this well.

---

#### 3. **Add Format Validation Checklist** ⭐⭐
**Add to VALIDATION CHECKLIST section:**

```markdown
## FORMAT VALIDATION (CRITICAL)

Before submitting transcription, verify:
- [ ] **Output is markdown (.md)** - NOT JSON, NOT plain text
- [ ] **Document starts with # heading** - Proper markdown structure
- [ ] **All 3 main sections present:**
  - [ ] 1. Metadata Section
  - [ ] 2. Description Section
  - [ ] 3. Word-for-Word Transcription
- [ ] **TAXONOMY ANALYSIS section included** - This is NOT optional
- [ ] **All action verbs categorized into A-G categories**
- [ ] **Tools matrix in table format** (not JSON, not list)
- [ ] **Workflows use structured format** (OBJECTIVE, STEPS, DURATION, etc.)
```

---

#### 4. **Add Character Encoding Note** ⭐
**Add to Core Requirements:**

```markdown
### Technical Requirements
- **Encoding:** Use UTF-8 encoding
- **Special Characters:** If $ or currency symbols cause issues, write out ("five point six million" instead of risking corruption)
- **Quality Check:** If text appears character-by-character (e.g., "h e l l o"), re-process that section
```

---

### MEDIUM PRIORITY

#### 5. **Enhance Workflow Examples** ⭐⭐
**Add a data workflow example to complement existing examples:**

```markdown
```
WORKFLOW: Multi-Source Lead Enrichment Pipeline
OBJECTIVE: Generate enriched lead lists from multiple data sources with email validation
STEPS:
  1. Scrapes company data from Airscale (location, size, keywords)
  2. Extracts company domains using automated workflow
  3. Exports to CSV format
  4. Imports CSV to Anymailfinder bulk search
  5. Enriches with nominative email patterns (firstname@domain, etc.)
  6. Validates email deliverability
  7. Downloads enriched list with verified contacts
DURATION: 10-15 minutes for 40 records, scalable to thousands
COMPLEXITY: Medium
TOOLS USED: Airscale, Anymailfinder, Google Sheets, CSV processors
INPUT: Search criteria (industry, geography, company size)
OUTPUT: CSV with company data + verified decision-maker emails
```
```

**Rationale:** Current examples (thumbnail creation, browser automation) don't cover data pipeline workflows. Video_006 is entirely data workflows.

---

#### 6. **Clarify Tools Matrix Table Format** ⭐⭐
**Add explicit table formatting instructions:**

```markdown
### 8. Tools & Technologies Matrix

**IMPORTANT:** Use markdown table format, NOT JSON, NOT bulleted list.

**Required Table Format:**
```
| Tool Name | Category | Purpose | Used For | Mentioned With |
|-----------|----------|---------|----------|----------------|
| [Tool 1] | [Type] | [Primary purpose] | [Specific use in video] | [Related tools] |
```

**Example:**
| Tool Name | Category | Purpose | Used For | Mentioned With |
|-----------|----------|---------|----------|----------------|
| Anymailfinder | Email Enrichment | Find & verify emails | Nominative email enrichment from domains | Airscale, LinkedIn Sales Navigator |
| Airscale | Company Search | Find companies by criteria | Generate company lists with domains | Anymailfinder, Google Sheets |
```

---

### LOW PRIORITY

#### 7. **Add Integration Patterns Template** ⭐
**Standardize integration pattern documentation:**

```markdown
### 9. Integration Patterns

**PATTERN [N]: [Name]**
- **PURPOSE:** [What this combination achieves]
- **FLOW:** [Tool 1] → [Tool 2] → [Tool 3] → [Output]
- **USE CASE:** [When to use this pattern]
- **TOOLS:** [List of tools in integration]
- **EXAMPLE:** [Specific example from video]
```

---

## Proposed V3.1 Changelog

**Version 3.1** (Proposed - November 12, 2025)
- **CRITICAL:** Strengthened markdown format requirement (moved to top, emphasized)
- **ADDED:** G. DATA OPERATIONS action verb category (scraping, parsing, enrichment)
- **ADDED:** Format validation checklist (prevent JSON/non-markdown outputs)
- **ADDED:** Character encoding guidance (prevent corruption issues)
- **ADDED:** Data workflow example (lead enrichment pipeline)
- **ENHANCED:** Tools matrix formatting instructions (table format required)
- **ENHANCED:** Integration patterns template (standardized structure)
- Based on analysis of Video_003, 004, 005, 006 real-world results

---

## Video-Specific Recommendations

### Video_003 (Kimi K2 Thinking) - Reprocess Section
**Action:** Fix character encoding corruption
**Priority:** Medium
**Sections to fix:** Lines 46-207, 352-391
**Method:** Re-transcribe those specific sections or manually edit

### Video_005 (Agentic Tech Stack) - Continue Processing
**Action:** Run Phases 3-7 (Analysis through Integration)
**Priority:** High - Contains 40+ tools for Tools library
**Expected output:**
- 15-20 workflows
- 40+ tools (Postgres, Redis, LangChain, LangGraph, etc.)
- Major Tools library expansion

### Video_006 (Lead Generation) - URGENT Reprocess
**Action:** Re-transcribe using v3.1 prompt in markdown format
**Priority:** CRITICAL
**Expected recovery:**
- 10 workflows (each lead gen method)
- 20+ tools
- 50+ action verbs
- 15 integration patterns
**Value:** This is a goldmine for taxonomy - systematic documentation of data workflows

---

## Success Metrics for V3.1

**Format Compliance:**
- Target: 100% of transcriptions in markdown format
- Current: ~50% (2/4 videos in proper format)

**Taxonomy Completeness:**
- Target: All videos have TAXONOMY ANALYSIS section
- Current: 50% (2/4 videos have taxonomy)

**Action Verb Coverage:**
- Target: 7 categories (A-G) used where applicable
- Current: 6 categories, G needed for data ops

**Tools Extraction:**
- Target: 90%+ of mentioned tools captured in matrix
- Current: Variable (Video_003: 100%, Video_006: 0%)

---

## Implementation Plan

**Phase 1: Update Prompt to v3.1** (20 minutes)
1. Move format requirement to top with strong emphasis
2. Add G. DATA OPERATIONS category
3. Add format validation checklist
4. Add character encoding guidance
5. Add data workflow example
6. Enhance tools matrix instructions
7. Update version history

**Phase 2: Reprocess Video_006** (60 minutes)
1. Use v3.1 prompt
2. Ensure markdown output
3. Extract all 10 workflows
4. Create tools matrix (20+ tools)
5. Categorize action verbs (7 categories)
6. Document integration patterns

**Phase 3: Process Video_005 Phases 3-7** (90 minutes)
1. Use v3.1 prompt for consistency
2. Extract tech stack workflows
3. Create comprehensive tools matrix (40+ tools)
4. Update Tools library with discoveries

**Phase 4: Fix Video_003 Encoding** (15 minutes)
1. Manually edit corrupted sections
2. Restore proper text for currency mentions

---

**Report Completed:** November 12, 2025
**Recommendation:** Proceed with v3.1 update immediately
**Priority:** CRITICAL - Prevent future data loss like Video_006
**Estimated Impact:** 5x improvement in taxonomy extraction quality and consistency

