# Tool Collection and Matching Prompt (Updated 2025-11-11)

## Objective
Collect, validate, and match all tools mentioned across the taxonomy framework. Produce **actionable decisions** with clear execution steps, risk assessment, and specific tool IDs - not just findings.

This prompt generates output similar to CLEANUP_PROPOSAL.md format: clear decisions, risk-assessed actions, and execution checklists ready for immediate implementation.

---

## Current State (As of 2025-11-10)

### Tool Library Overview
**Total Tools:** 254 tools across 15 categories

| Category | Count | ID Range | Status |
|----------|-------|----------|--------|
| Automation_Tools | 95 | TOOL-AUTO-002 to TOOL-AUTO-191 | Many need review |
| Documentation_Tools | 37 | TOOL-DOC-003 to TOOL-DOC-076 | Many need review |
| Development_Tools | 31 | TOOL-DEV-003 to TOOL-DEV-064 | Some need review |
| AI_Tools | 15 | TOOL-AI-009 to TOOL-AI-038 | Some need review |
| Communication_Tools | 17 | TOOL-COMM-002 to TOOL-COMM-035 | Some need review |
| Design_Tools | 8 | TOOL-DESIGN-007 to TOOL-DESIGN-022 | Few need review |
| Analytics_Tools | 11 | TOOL-ANALYTICS-001 to TOOL-ANALYTICS-022 | Some need review |
| Collaboration_Tools | 9 | TOOL-COLLAB-002 to TOOL-COLLAB-009 | Few need review |
| Testing_Tools | 11 | TOOL-TEST-001 to TOOL-TEST-011 | Some need review |
| Video_Tools | 7 | TOOL-VIDEO-001 to TOOL-VIDEO-014 | Few need review |
| Data_Tools | 5 | TOOL-DATA-001 to TOOL-DATA-005 | Few need review |
| File_Management | 5 | TOOL-FILE-001 to TOOL-FILE-005 | Few need review |
| Cloud_Services | 2 | TOOL-CLOUD-001 to TOOL-CLOUD-002 | Few entries |
| Presentation_Tools | 1 | TOOL-PRES-001 | Single entry |

### Recent Addition (2025-11-10)
**253 tools** were discovered from TASK_MANAGERS analysis with:
- Status: `"discovered_needs_review"`
- Discovery source: `"task_step_analysis"`
- Discovery date: `"2025-11-10"`

**Priority:** Validate and enrich these 253 tools

---

## Source Directories

### Primary Source: TASK_MANAGERS (Current/Structured)
**Path:** `C:\Users\Dell\Dropbox\Nov25\Entities\TASK_MANAGERS`

**Structure:**
```
TASK_MANAGERS/
├── Task_Templates/          # 55 task templates
│   ├── AI/
│   │   ├── AI-001.md       # Simplified ID format (was TASK-AI-001.md)
│   │   ├── AI-006.md
│   │   └── ...
│   └── [10 departments: ADMIN, AI, DESIGN, DEV, HR, LG, OPS, SALES, VIDEO]
│
├── Step_Templates/          # 335+ step templates
│   ├── AI/
│   │   ├── AI-006-03_extract-company-adaptations.md  # ID + slug format
│   │   └── ...
│   └── [10 departments]
│
├── tool_mapping.json        # Maps tool names → Tool IDs
└── discovered_tools.json    # 253 tools found from task analysis
```

**Tool Reference Patterns:**

**In Task Templates (YAML):**
```yaml
taxonomy:
  tool: "Gemini + Google Drive"  # Free-text tool reference
key_tools:
  - "Claude"
  - "ChatGPT"
  - "Documentation tools"
```

**In Step Template Metadata:**
```markdown
| Tool | Documentation |
| Tool ID | TBD - Documentation |
```

**In tool_mapping.json:**
```json
{
  "Gemini + Google Drive": {
    "tool_id": "TOOL-AI-027",
    "category": "AI_Tools",
    "file_path": "C:\\...\\AI_Tools\\Tool_Name.json"
  }
}
```

### Secondary Source: RestructuredData (Historical/Archival)
**Path:** `C:\Users\Dell\Dropbox\Nov25\Taxonomy\RestructuredData`

**Contents:**
- Daily structured summaries (05-10 Nov 2025)
- Department operations reports
- Project deliverables and milestones
- Historical meeting notes and task logs
- October 2025 comprehensive review

**Tool Reference Patterns:**
- Explicit tool names: "using ChatGPT", "with Figma"
- Platform mentions: "on Dropbox", "via Discord"
- Tool categories: "Design Tools", "Automation platform"
- Implicit references: "created in CRM", "exported from analytics"

### Target: LIBRARIES\Tools (Tool Library)
**Path:** `C:\Users\Dell\Dropbox\Nov25\Entities\LIBRARIES\Tools`

**Structure:** Tools organized in 15 category subdirectories

**Tool JSON Schema:**
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-CATEGORY-###",
  "name": "Tool Name",
  "vendor": "Vendor Name",
  "category": "Category / Subcategory",
  "purpose": "Primary purpose",
  "description": "Detailed description",
  "skill_level_required": "Beginner|Intermediate|Advanced|Expert",
  "cost_structure": "Pricing model or 'TBD'",
  "platform_compatibility": ["Web", "Mobile", "Desktop", "API"],
  "integration_capabilities": ["API", "Zapier", "n8n"],
  "documentation_url": "https://...",
  "actual_remote_helpers_usage": {
    "primary_use": "Main use case",
    "users": ["Department/Team"],
    "use_cases": ["Use case 1", "Use case 2"],
    "workflows": ["Workflow 1"]
  },
  "strengths": ["Strength 1", "Strength 2"],
  "limitations": ["Limitation 1", "Limitation 2"],
  "departments_using": ["Department 1", "Department 2"],
  "tags": ["tag1", "tag2", "tag3"],
  "discovery_date": "2025-11-10",
  "discovery_source": "task_step_analysis",
  "status": "discovered_needs_review|active|deprecated"
}
```

---

## Decision Framework

### Auto-Validation Criteria
Tools meeting ALL criteria can be automatically validated:
- ✅ Tool ID exists and is unique (no duplicates)
- ✅ Name matches known tool (exact match in usage patterns)
- ✅ Category is appropriate based on purpose
- ✅ Found in 3+ tasks/steps (high confidence usage)
- ✅ No merge candidates (not similar to existing tools)

### Manual Review Required When:
- ⚠️ Tool mentioned 1-2 times only (low confidence)
- ⚠️ Generic tool name ("Documentation", "Text editor")
- ⚠️ Potential duplicate (similar name/vendor)
- ⚠️ Missing vendor information
- ⚠️ Unclear category assignment

### Confidence Scoring
- **High (90-100%):** Exact matches, well-documented usage, no ambiguity → Auto-validate
- **Medium (60-89%):** Some usage found, minor gaps in data → Quick review
- **Low (<60%):** Minimal mentions, unclear purpose → Manual research

---

## Collection & Validation Process

### Phase 1: Validate Recently Discovered Tools (Priority)

**Goal:** Review and enrich the 253 tools with status "discovered_needs_review"

**Steps:**
1. **Load discovered_tools.json**
   - Get list of 253 tool names
   - Note their categories and IDs

2. **Cross-reference with tool_mapping.json**
   - Verify mapping accuracy
   - Check for duplicate entries
   - Identify tools mapped to multiple IDs

3. **Scan TASK_MANAGERS for usage context**
   - Find where each tool is mentioned
   - Extract use cases, departments, workflows
   - Identify which tasks/steps use each tool

4. **Classify tools by confidence:**
   - High confidence (90%+, 3+ mentions) → Auto-validate
   - Medium confidence (60-89%, some data) → Quick review
   - Low confidence (<60%, 1-2 mentions) → Manual research
   - Duplicates detected → Merge candidates
   - Zero usage → Archive candidates

5. **Generate actionable decisions:**
   - List specific tool IDs for each action (VALIDATE, MERGE, REVIEW, ARCHIVE)
   - Provide execution commands for each action
   - Include confidence scores and risk assessment

### Phase 2: Scan RestructuredData for Additional Tools

**Goal:** Find tools mentioned in historical data not yet in library

**Steps:**
1. **Scan all .md files in RestructuredData**
   - Extract tool mentions using patterns (regex, keyword search)
   - Note context and source file

2. **Normalize tool names**
   - Handle variations: "ChatGPT" vs "Chat GPT" vs "OpenAI ChatGPT"
   - Remove version numbers: "Python 3.9" → "Python"
   - Standardize capitalization

3. **Match against existing tools**
   - Check if tool exists in LIBRARIES\Tools
   - Check tool_mapping.json for aliases
   - Determine match confidence (Exact, High, Medium, Low, None)

4. **For unmatched tools:**
   - Categorize appropriately
   - Generate new tool ID
   - Add to CREATE list with suggested details

### Phase 3: Scan Current TASK_MANAGERS for New Tools

**Goal:** Find tools added/mentioned since last discovery run

**Steps:**
1. **Scan Task Templates:**
   - Parse YAML frontmatter
   - Extract `taxonomy.tool` field
   - Extract `key_tools` array
   - Note which tasks use which tools

2. **Scan Step Templates:**
   - Parse metadata tables
   - Extract Tool field
   - Extract Tool ID field (if present)
   - Map steps to tools

3. **Compare with tool_mapping.json:**
   - Find new tool mentions not in mapping
   - Add to CREATE list

4. **Update tool usage statistics:**
   - Count how many tasks use each tool
   - Count how many steps use each tool
   - Identify most-used tools (for priority validation)
   - Find underutilized or deprecated tools

---

## Tool Extraction Patterns

### TASK_MANAGERS Patterns

**Task Template YAML (AI-006.md):**
```yaml
# Pattern 1: Single tool in taxonomy
taxonomy:
  tool: "Gemini + Google Drive"

# Pattern 2: Array of key tools
key_tools:
  - "Claude"
  - "ChatGPT"
  - "Documentation tools"

# Pattern 3: Tool in structure
structure:
  steps:
    - step_id: AI-006-01
      tool: "Gemini"
```

**Step Template Metadata (AI-006-03_slug.md):**
```markdown
| Tool | Documentation |
| Tool ID | TBD - Documentation |
```

**Extraction Strategy:**
- Parse YAML blocks with `yaml.safe_load()`
- Extract from markdown metadata tables
- Look for "Tool:", "tool:", "Tool ID:" patterns
- Handle multi-tool references ("+", "and", "/", ",")

### RestructuredData Patterns

**Pattern 1: Direct mentions**
- "using [Tool]"
- "with [Tool]"
- "via [Tool]"
- "through [Tool]"
- "on [Platform]"
- "in [Software]"

**Pattern 2: Section headers**
- "## Tools Used:"
- "### Technologies:"
- "**Tools:** [list]"

**Pattern 3: Task descriptions**
- "Task: Use [Tool] to..."
- "Created in [Tool]"
- "Exported from [Tool]"

**Regex Patterns:**
```regex
# Direct tool mentions
(?:using|with|via|through|in|on)\s+([A-Z][a-zA-Z0-9\s+]+?)(?:\s|,|\.|$)

# Section-based extraction
(?:Tools?|Technologies?):\s*(.+?)(?:\n\n|\n##)

# Tool + action
(?:created|built|designed|developed|exported|generated)\s+(?:in|with|using)\s+([A-Z][a-zA-Z0-9\s]+)
```

---

## Tool Normalization Rules

### Handle Variations
```
"ChatGPT" = "Chat GPT" = "OpenAI ChatGPT" = "GPT"
"n8n" = "N8N" = "n8n workflow automation"
"Figma" = "Figma Design" = "Figma UI/UX"
"Google Drive" = "GDrive" = "Google Drive Storage"
"Dropbox" = "Dropbox Storage" = "Dropbox File Management"
```

### Version Handling
```
"Python 3.9" → "Python" (remove version unless critical)
"Node.js 18" → "Node.js"
"ChatGPT-4" → "ChatGPT" (model versions in description, not name)
```

### Multi-Tool References
```
"Claude + ChatGPT" → Split into ["Claude", "ChatGPT"]
"Email / Slack" → Split into ["Email", "Slack"]
"Text editor, Claude" → Split into ["Text editor", "Claude"]
```

### Generic Terms
```
"CRM" → Check context for specific CRM (HubSpot, Salesforce, etc.)
"Email" → Note as generic, may map to specific client (Gmail, Outlook)
"Text editor" → Check for specific editor (VS Code, Notepad++, etc.)
"Documentation tool" → Check context (Notion, Markdown, Google Docs)
```

---

## Tool Categorization Guide

### Category Decision Tree

**Is it AI-powered?** → AI_Tools
- LLMs: ChatGPT, Claude, Gemini
- AI services: Midjourney, ElevenLabs
- NLP tools: Text analysis, sentiment analysis

**Does it automate workflows?** → Automation_Tools
- n8n, Zapier, Make
- Scripting frameworks
- CI/CD pipelines

**Is it for communication?** → Communication_Tools
- Email clients: Gmail, Outlook
- CRM systems: HubSpot, Salesforce
- Messaging: Slack, Discord

**Is it for team collaboration?** → Collaboration_Tools
- Project management: Asana, Trello, Monday
- Wikis: Notion, Confluence
- Real-time collaboration: Google Docs

**Is it for design/graphics?** → Design_Tools
- Figma, Sketch, Adobe XD
- Photoshop, Illustrator
- Prototyping tools

**Is it for coding/development?** → Development_Tools
- IDEs: VS Code, PyCharm
- Version control: Git, GitHub
- Package managers: npm, pip

**Is it for documentation?** → Documentation_Tools
- Markdown editors
- Documentation generators: Sphinx, Docusaurus
- Note-taking: Obsidian, Roam

**Is it for file storage?** → File_Management
- Dropbox, Google Drive, OneDrive
- Cloud storage services

**Is it for analytics/reporting?** → Analytics_Tools
- Dashboard tools
- Business intelligence
- Metrics platforms

**Is it for data processing?** → Data_Tools
- Data transformation
- ETL tools
- Database tools

**Is it for testing?** → Testing_Tools
- Test frameworks
- QA platforms
- Validation tools

**Is it for video/audio?** → Video_Tools
- Video editing: Adobe Premiere, DaVinci Resolve
- Audio production
- Transcription services

**Is it a cloud platform?** → Cloud_Services
- AWS, Google Cloud, Azure
- Cloud infrastructure

**Is it for presentations?** → Presentation_Tools
- PowerPoint, Google Slides, Keynote
- Presentation platforms

---

## Tool ID Generation

### Format
`TOOL-[CATEGORY]-###`

### Category Abbreviations (ACTUAL)
Based on existing tools:
- AI_Tools → **AI** (e.g., TOOL-AI-027)
- Analytics_Tools → **ANALYTICS** (e.g., TOOL-ANALYTICS-022)
- Automation_Tools → **AUTO** (e.g., TOOL-AUTO-191)
- Cloud_Services → **CLOUD** (e.g., TOOL-CLOUD-002)
- Collaboration_Tools → **COLLAB** (e.g., TOOL-COLLAB-009)
- Communication_Tools → **COMM** (e.g., TOOL-COMM-035)
- Data_Tools → **DATA** (e.g., TOOL-DATA-005)
- Design_Tools → **DESIGN** (e.g., TOOL-DESIGN-022)
- Development_Tools → **DEV** (e.g., TOOL-DEV-064)
- Documentation_Tools → **DOC** (e.g., TOOL-DOC-076)
- File_Management → **FILE** (e.g., TOOL-FILE-005)
- Presentation_Tools → **PRES** (e.g., TOOL-PRES-001)
- Testing_Tools → **TEST** (e.g., TOOL-TEST-011)
- Video_Tools → **VIDEO** (e.g., TOOL-VIDEO-014)

### Next Available IDs (as of 2025-11-10)
- TOOL-AI-039 (next available)
- TOOL-ANALYTICS-023
- TOOL-AUTO-192
- TOOL-CLOUD-003
- TOOL-COLLAB-010
- TOOL-COMM-036
- TOOL-DATA-006
- TOOL-DESIGN-023
- TOOL-DEV-065
- TOOL-DOC-077
- TOOL-FILE-006
- TOOL-PRES-002
- TOOL-TEST-012
- TOOL-VIDEO-015

---

## Output Format

### ✅ Final Decisions Summary

Provide clear, actionable decisions upfront:

```markdown
## ✅ Final Decisions Summary

### A) Tools Ready for Auto-Validation → **VALIDATE** ([Count] tools)
- Tools with high confidence (90%+) and complete data
- **Action:** Update status to "active", enrich with usage data
- **Tool IDs:** TOOL-AI-027, TOOL-AUTO-045, TOOL-DOC-033, [list all IDs]

### B) Tools Requiring Merge → **MERGE** ([Count] pairs)
- Duplicate/variant tools identified
- **Action:** Merge entries, update all references to winning ID
- **Pairs:**
  - TOOL-AI-012 + TOOL-AI-028 → Keep TOOL-AI-012
  - TOOL-DOC-015 + TOOL-DOC-047 → Keep TOOL-DOC-015
  [list all pairs]

### C) Tools Needing Manual Review → **REVIEW** ([Count] tools)
- Low confidence, incomplete data, or generic names
- **Action:** Research and complete manually
- **Tool IDs:** TOOL-AUTO-089, TOOL-DEV-042, [list all IDs]

### D) New Tools Discovered → **CREATE** ([Count] tools)
- Found in RestructuredData or TASK_MANAGERS, not in library
- **Action:** Create new tool entries with available data
- **Suggested IDs:** TOOL-VIDEO-015 (Descript), TOOL-AI-039 (Perplexity), [list all]

### E) Tools to Archive → **ARCHIVE** ([Count] tools)
- No usage found, likely deprecated or test entries
- **Action:** Move to Archive/Deprecated_Tools_[DATE]/
- **Tool IDs:** TOOL-TEST-007, TOOL-DATA-003, [list all IDs]
```

---

### 📋 Executive Summary

```markdown
## 📋 Executive Summary

This report provides actionable decisions for tool library validation:
- **Validate and enrich** high-confidence tools automatically
- **Merge** duplicate tool entries
- **Complete** tools with missing data through manual review
- **Create** new tool entries for discovered tools
- **Archive** deprecated or unused tools

**Total Tools Analyzed:** 254 existing + [X] discovered = [Total]
**Tools Ready for Auto-Validation:** [Count] tools
**Tools Requiring Merge:** [Count] pairs ([Total] tools affected)
**Tools Needing Manual Review:** [Count] tools
**New Tools to Create:** [Count] tools
**Tools to Archive:** [Count] tools
```

---

### 🎯 Proposed Actions

Structure output as numbered actions, not passive findings:

```markdown
## 🎯 Proposed Actions

### Action 1: Auto-Validate High-Confidence Tools

**Decision:** ✅ **VALIDATE** - Update [Count] tools from "discovered_needs_review" to "active"

**Tools Included:**

#### TOOL-AI-027 (Claude)
- **Confidence:** 95% (High)
- **Mentions Found:** 15 tasks, 32 steps
- **Departments:** AI, HR, Design, Content Ops
- **Use Cases:**
  - "Extract company adaptations from documentation" (AI-006-03)
  - "Generate project requirements" (AI-001-02)
  - "Create content guidelines" (-003-05)
- **Enrichments to Apply:**
  - Update actual_remote_helpers_usage with 3 primary use cases
  - Add departments_using: ["AI", "HR", "Design", ""]
  - Set status to "active"
  - Add documentation_url: https://claude.ai/docs
- **Automated Action:** Include in enrichment script

#### TOOL-AUTO-045 (n8n)
- **Confidence:** 92% (High)
- **Mentions Found:** 8 tasks, 12 steps
- **Departments:** Automation, AI, Operations
- **Use Cases:**
  - "Automate data extraction workflows" (AUTO-001-03)
  - "Schedule report generation" (OPS-005-02)
- **Enrichments to Apply:**
  - Update actual_remote_helpers_usage
  - Add departments_using: ["Automation", "AI", "Operations"]
  - Set status to "active"
- **Automated Action:** Include in enrichment script

[Continue for all high-confidence tools - list each specific tool ID with details]

**Execution Command:**
```bash
python enrich_validated_tools.py --tool-ids TOOL-AI-027,TOOL-AUTO-045,[complete list]
```

---

### Action 2: Merge Duplicate Tool Entries

**Decision:** ✅ **MERGE** - Consolidate [Count] tool pairs

**Merge Candidates:**

#### Merge 1: TOOL-AI-012 + TOOL-AI-028 → Keep TOOL-AI-012
- **Tool A:** TOOL-AI-012 (ChatGPT)
- **Tool B:** TOOL-AI-028 (OpenAI ChatGPT)
- **Evidence:**
  - Same vendor (OpenAI)
  - Identical purpose (LLM for text generation)
  - Usage patterns overlap (both used in AI tasks)
- **Winning ID:** TOOL-AI-012 (more complete data, earlier ID)
- **Actions Required:**
  1. Copy missing data from TOOL-AI-028 to TOOL-AI-012
  2. Update all references in task/step files: TOOL-AI-028 → TOOL-AI-012
  3. Update tool_mapping.json: "OpenAI ChatGPT" → TOOL-AI-012
  4. Archive TOOL-AI-028.json to Archive/Merged_Tools_[DATE]/
- **Impact:** 5 tasks, 8 steps reference TOOL-AI-028

#### Merge 2: TOOL-DOC-015 + TOOL-DOC-047 → Keep TOOL-DOC-015
- **Tool A:** TOOL-DOC-015 (Markdown)
- **Tool B:** TOOL-DOC-047 (Markdown Editor)
- **Evidence:**
  - Both reference markdown editing
  - Similar use cases (documentation, notes)
- **Winning ID:** TOOL-DOC-015 (earlier ID, more references)
- **Actions Required:**
  1. Merge use cases from both tools into TOOL-DOC-015
  2. Update references: TOOL-DOC-047 → TOOL-DOC-015
  3. Archive TOOL-DOC-047.json
- **Impact:** 3 tasks, 6 steps reference TOOL-DOC-047

[Continue for all merge pairs - list each specific pair with details]

**Execution Commands:**
```bash
# Step 1: Merge tool data
python merge_tools.py --merge-pairs "TOOL-AI-012:TOOL-AI-028,TOOL-DOC-015:TOOL-DOC-047"

# Step 2: Update all references in task/step files
python update_tool_references.py --replacements "TOOL-AI-028:TOOL-AI-012,TOOL-DOC-047:TOOL-DOC-015"

# Step 3: Archive merged tools
mkdir -p Archive/Merged_Tools_[DATE]/
mv TOOL-AI-028.json Archive/Merged_Tools_[DATE]/
mv TOOL-DOC-047.json Archive/Merged_Tools_[DATE]/
```

---

### Action 3: Manual Review for Incomplete Tools

**Decision:** ⚠️ **REVIEW** - Research and complete [Count] tools with low confidence or missing data

**Tools Requiring Review:**

#### TOOL-AUTO-089 (Generic "Automation Tool")
- **Confidence:** 45% (Low)
- **Issue:** Generic name, no vendor specified
- **Mentions:** 2 steps only
- **Missing Data:**
  - ✗ Vendor: "TBD"
  - ✗ Specific tool name unclear
  - ✗ Documentation URL missing
- **Context Found:**
  - "Use automation tool for data sync" (OPS-002-03)
  - "Configure automation for scheduling" (ADMIN-001-05)
- **Research Needed:**
  - Check step context files to identify specific tool (Zapier? n8n? Custom script?)
  - Find vendor and documentation
  - Determine if should merge with existing automation tool
- **Assigned To:** [Tool Category Owner - Automation]
- **Priority:** Medium (low usage, but could be duplicate)

#### TOOL-DEV-042 (Text Editor)
- **Confidence:** 38% (Low)
- **Issue:** Generic name, could be VS Code, Notepad++, Sublime, etc.
- **Mentions:** 1 task
- **Missing Data:**
  - ✗ Specific editor not identified
  - ✗ Vendor unknown
- **Context Found:**
  - "Edit configuration files with text editor" (DEV-005-02)
- **Research Needed:**
  - Check department standards documentation (likely VS Code)
  - Verify if should map to existing TOOL-DEV-001 (VS Code)
  - Consider merging or deleting if redundant
- **Assigned To:** [Tool Category Owner - Development]
- **Priority:** Low (single mention, likely redundant)

[Continue for all tools needing review - list each specific tool ID with details]

**Manual Review Checklist:**
- [ ] Research tool vendor and specific name from context
- [ ] Find documentation URL
- [ ] Verify tool purpose and category assignment
- [ ] Check for merge candidates (compare with existing tools)
- [ ] Complete tool JSON with accurate data
- [ ] Update status to "active" when complete

---

### Action 4: Create New Tool Entries

**Decision:** ✅ **CREATE** - Add [Count] newly discovered tools to library

**New Tools from RestructuredData:**

#### Descript (Video/Audio Editing)
- **Status:** ❌ Not in Library
- **Suggested Category:** Video_Tools
- **Suggested Tool ID:** TOOL-VIDEO-015
- **Mentions:** 4 times in historical data
- **Source Files:**
  - 291025-organized.md (line 156): "Used Descript for video transcription"
  - Projects_Milestones_Tasks_Nov05-07_2025.md (line 89): "Edited in Descript"
  - Department_Operations_Nov06_2025.md (line 234): "Transcribed with Descript"
- **Available Information:**
  - **Vendor:** Descript, Inc.
  - **Purpose:** Video/audio editing and transcription with text-based interface
  - **Departments:** Video, AI
  - **Use Cases:**
    - Transcribe client calls automatically
    - Edit video content using text-based editor
    - Generate captions automatically
  - **Platform:** Web, Desktop (Mac/Windows)
- **Action:** Create TOOL-VIDEO-015.json with "active" status
- **Data Completeness:** 85% (can create full entry)

#### Perplexity (AI Research)
- **Status:** ❌ Not in Library
- **Suggested Category:** AI_Tools
- **Suggested Tool ID:** TOOL-AI-039
- **Mentions:** 3 times in TASK_MANAGERS
- **Source Files:**
  - AI-011.md (key_tools array)
  - AI-011-04_research-topic-background.md (metadata)
  - AI-015-02_fact-checking.md (metadata)
- **Available Information:**
  - **Vendor:** Perplexity AI
  - **Purpose:** AI-powered research and question answering with citations
  - **Departments:** AI, Research, Content Ops
  - **Use Cases:**
    - Research topic background for content creation
    - Fact-checking and source verification
    - Find recent information with citations
  - **Platform:** Web, Mobile (iOS/Android)
- **Action:** Create TOOL-AI-039.json with "active" status
- **Data Completeness:** 80% (can create full entry)

[Continue for all new tools - list each specific tool with full details]

**Execution Command:**
```bash
python create_new_tools.py --tools "Descript:TOOL-VIDEO-015,Perplexity:TOOL-AI-039,[complete list]" --status active
```

---

### Action 5: Archive Deprecated Tools

**Decision:** 📦 **ARCHIVE** - Move [Count] unused tools to archive

**Tools with Zero Usage:**

#### TOOL-TEST-007 (Test Tool Alpha)
- **Status:** Zero mentions found in TASK_MANAGERS or RestructuredData
- **Discovery Date:** 2025-11-10 (recent discovery, but no usage)
- **Current Data:** Minimal entry, appears to be test/placeholder
- **Reason:** Likely test entry created during tool discovery, never actually used
- **Action:** Move to Archive/Deprecated_Tools_[DATE]/
- **Risk:** Low (no references to break)

#### TOOL-DATA-003 (Legacy Data Processor)
- **Status:** Zero mentions in TASK_MANAGERS
- **Last Mentioned:** RestructuredData Oct 2025 (1 mention, marked "no longer using")
- **Current Data:** Marked as deprecated in old reports
- **Reason:** Deprecated, replaced by newer data processing tools
- **Action:** Move to Archive/Deprecated_Tools_[DATE]/
- **Risk:** Low (explicitly marked as deprecated)

[Continue for all tools to archive - list each specific tool ID with details]

**Execution Command:**
```bash
# Create archive directory
mkdir -p Archive/Deprecated_Tools_[DATE]/

# Move deprecated tools
mv TOOL-TEST-007.json Archive/Deprecated_Tools_[DATE]/
mv TOOL-DATA-003.json Archive/Deprecated_Tools_[DATE]/
[list all]

# Update tool_mapping.json to remove archived tool references
python update_tool_mapping.py --remove-tools TOOL-TEST-007,TOOL-DATA-003,[list all]
```
```

---

### 📊 Summary Statistics

```markdown
## 📊 Summary Statistics

### Decision Breakdown
| Decision | Count | Percentage | Risk Level |
|----------|-------|------------|------------|
| Auto-Validate | [X] | [X%] | Low |
| Merge | [X] pairs ([Y] tools) | [X%] | Medium |
| Manual Review | [X] | [X%] | Medium |
| Create New | [X] | [X%] | Low |
| Archive | [X] | [X%] | Low |
| **Total** | **[Total]** | **100%** | - |

### Category Distribution (After Actions)
| Category | Before | After | Change |
|----------|--------|-------|--------|
| AI_Tools | 15 | [New] | +[X] |
| Automation_Tools | 95 | [New] | +[X] |
| Documentation_Tools | 37 | [New] | +[X] |
| Video_Tools | 7 | [New] | +[X] |
| [All categories] | ... | ... | ... |

### Tool Usage Frequency (Top 15)
1. **TOOL-AI-027 (Claude)** - 15 tasks, 32 steps, 4 departments
2. **TOOL-AUTO-045 (n8n)** - 8 tasks, 12 steps, 3 departments
3. **TOOL-DOC-033 (Notion)** - 6 tasks, 10 steps, 8 departments
[Continue list to 15 most-used tools]

### Department Tool Coverage
| Department | Tools Used | Most Used Tool | Least Used Category |
|------------|------------|----------------|---------------------|
| AI | [Count] | Claude (TOOL-AI-027) | [Category] |
| Design | [Count] | Figma (TOOL-DESIGN-XXX) | [Category] |
| [All departments] | ... | ... | ... |

### Tools by Status (After Actions)
- **Active:** [Count] (validated, complete data, in use)
- **Discovered_needs_review:** [Count] (awaiting manual review)
- **Archived:** [Count] (deprecated/unused, moved to archive)
- **Total:** [Count]
```

---

### 🚨 Risk Assessment

```markdown
## 🚨 Risk Assessment

### Low Risk Actions (Execute Immediately)
**Auto-validate high-confidence tools** (Action 1)
- **Risk:** Minimal - Tools have 90%+ confidence, 3+ mentions, clear usage
- **Impact:** Positive - Improves library completeness, no breaking changes
- **Mitigation:** Automated validation criteria ensure quality

**Create new tool entries** (Action 4)
- **Risk:** Low - Tools clearly identified and not duplicates
- **Impact:** Positive - Expands tool coverage, fills gaps
- **Mitigation:** New IDs assigned sequentially, no conflicts

**Archive zero-usage tools** (Action 5)
- **Risk:** Low - No usage found anywhere, can restore if needed
- **Impact:** Positive - Reduces clutter, improves navigation
- **Mitigation:** Archive preserves data, reversible action

### Medium Risk Actions (Execute with Verification)
**Merge duplicate tools** (Action 2)
- **Risk:** Medium - Must update all task/step references correctly
- **Impact:** High - Consolidates library, but requires reference updates
- **Potential Issues:**
  - Broken references if update script fails
  - Data loss if merge logic incorrect
- **Mitigation:**
  - Verify merge pairs manually before execution
  - Test reference update script on sample files
  - Verify no broken references after execution

**Manual review tools** (Action 3)
- **Risk:** Medium - Requires human judgment and research
- **Impact:** Variable - Depends on tool importance and usage
- **Potential Issues:**
  - Incorrect categorization if research inadequate
  - Missed merge opportunities
  - Incomplete data if research rushed
- **Mitigation:**
  - Assign to category experts
  - Provide detailed review checklist
  - Set quality standards for completion

### High Risk Actions
- None identified (all actions are low-medium risk)

### Overall Risk Assessment: **LOW-MEDIUM**
- Majority of actions (60-70%) are low risk and automated
- Medium risk actions have clear mitigation strategies
- No high-risk actions requiring special approval
```

---

### ✅ Execution Checklist

```markdown
## ✅ Execution Checklist

### Phase 1: Preparation

- [ ] Verify Python dependencies installed (yaml, json, pathlib, re)
- [ ] Create archive directories:
  - [ ] `mkdir -p Archive/Deprecated_Tools_[DATE]/`
  - [ ] `mkdir -p Archive/Merged_Tools_[DATE]/`
- [ ] Load baseline data:
  - [ ] Load all 254 existing tools from LIBRARIES/LBS_003_LBS_003_Tools/
  - [ ] Load tool_mapping.json
  - [ ] Load discovered_tools.json

### Phase 2: Execute Low-Risk Actions (Can Run in Parallel)

**Action 1: Auto-Validation**
- [ ] Execute: `python enrich_validated_tools.py --tool-ids [LIST from Action 1]`
- [ ] Verify [X] tools updated to "active" status
- [ ] Verify actual_remote_helpers_usage populated with use cases
- [ ] Verify departments_using arrays updated

**Action 4: Create New Tools**
- [ ] Execute: `python create_new_tools.py --tools [LIST from Action 4] --status active`
- [ ] Verify [X] new tool JSON files created
- [ ] Verify tool IDs are sequential (no gaps or duplicates)
- [ ] Verify all required fields populated

**Action 5: Archive Deprecated Tools**
- [ ] Execute archive commands from Action 5
- [ ] Verify [X] unused tools moved to Archive/Deprecated_Tools_[DATE]/
- [ ] Verify files no longer in main LBS_003_Tools/ directories
- [ ] Update tool_mapping.json to remove archived tool references

### Phase 3: Execute Medium-Risk Actions (Sequential, with Verification)

**Action 2: Merge Duplicates**
- [ ] Review merge pairs in Action 2 manually (verify logic correct)
- [ ] Execute: `python merge_tools.py --merge-pairs [LIST from Action 2]`
- [ ] Verify merged data complete (no data loss)
- [ ] Execute: `python update_tool_references.py --replacements [LIST from Action 2]`
- [ ] Verify ALL references updated in task/step files:
  - [ ] Grep for old tool IDs (should find zero results)
  - [ ] Spot-check 5-10 updated files manually
- [ ] Move merged tools to Archive/Merged_Tools_[DATE]/
- [ ] Update tool_mapping.json

**Action 3: Assign Manual Reviews**
- [ ] Create review tickets/tasks for [X] tools with low confidence
- [ ] Assign each tool to appropriate category owner:
  - [ ] AI Tools: [Owner Name]
  - [ ] Automation Tools: [Owner Name]
  - [ ] [All categories with reviews needed]
- [ ] Provide review checklist and context for each tool
- [ ] Set deadline for completion
- [ ] Set up tracking mechanism (spreadsheet, project management tool)

### Phase 4: Post-Execution Validation

**Integrity Checks**
- [ ] Verify no duplicate tool IDs exist:
  - [ ] Run: `python check_duplicate_ids.py`
- [ ] Verify all tool JSON files have valid syntax:
  - [ ] Run: `python validate_json_syntax.py`
- [ ] Verify tool_mapping.json loads correctly (no syntax errors)
- [ ] Verify no broken references in task/step files:
  - [ ] Run: `python check_tool_references.py`
  - [ ] All references should resolve to existing tool IDs

**Statistics Generation**
- [ ] Generate updated tool count by category
- [ ] Generate tool usage statistics (top 15 most-used)
- [ ] Generate department tool coverage report
- [ ] Compare before/after statistics

### Phase 5: Documentation

- [ ] Update tool count in this prompt file (line 14-27)
- [ ] Update "Next Available IDs" section (after new tools created)
- [ ] Create TOOL_VALIDATION_LOG_[DATE].md with:
  - [ ] List of all actions executed
  - [ ] Before/after statistics
  - [ ] List of merged tools and new IDs
  - [ ] List of archived tools
- [ ] Update Archive/README.md to document:
  - [ ] Merge decisions and rationale
  - [ ] Deprecated tools and reasons
- [ ] Update next scheduled run date (line 883)

### Phase 6: Manual Review Tracking (Ongoing)

- [ ] Week 1: Check progress on manual reviews
- [ ] Week 2: Follow up on incomplete reviews
- [ ] Week 3: Complete remaining reviews
- [ ] Week 4: Final validation of manually reviewed tools
```

---

### 📝 Detailed Analysis Tables

```markdown
## 📝 Detailed Analysis Tables

### Table 1: Tools Ready for Auto-Validation

| Tool ID | Tool Name | Confidence | Tasks | Steps | Departments | Decision | Risk |
|---------|-----------|------------|-------|-------|-------------|----------|------|
| TOOL-AI-027 | Claude | 95% | 15 | 32 | AI, HR, Design, Content | VALIDATE | Low |
| TOOL-AUTO-045 | n8n | 92% | 8 | 12 | Auto, AI, Ops | VALIDATE | Low |
| TOOL-DOC-033 | Notion | 88% | 6 | 10 | All depts | VALIDATE | Low |
[List ALL tools with 90%+ confidence - include every specific tool ID]

**Total:** [X] tools ready for auto-validation
**Combined Impact:** [X] tasks, [Y] steps use these tools

---

### Table 2: Tools Requiring Merge

| Merge ID | Tool A | Tool B | Winner | Reason | Tasks | Steps | Risk |
|----------|--------|--------|--------|--------|-------|-------|------|
| MERGE-01 | TOOL-AI-012 (ChatGPT) | TOOL-AI-028 (OpenAI ChatGPT) | TOOL-AI-012 | Same tool | 5 | 8 | Medium |
| MERGE-02 | TOOL-DOC-015 (Markdown) | TOOL-DOC-047 (Markdown Editor) | TOOL-DOC-015 | Same purpose | 3 | 6 | Medium |
[List ALL merge pairs - include every specific pair]

**Total:** [X] merge pairs ([Y] tools will be archived)
**Total Impact:** [X] tasks, [Y] steps need reference updates

---

### Table 3: Tools Needing Manual Review

| Tool ID | Tool Name | Confidence | Issue | Missing Data | Priority | Risk |
|---------|-----------|------------|-------|--------------|----------|------|
| TOOL-AUTO-089 | Automation Tool | 45% | Generic name | Vendor, specific tool | Medium | Medium |
| TOOL-DEV-042 | Text Editor | 38% | Generic, ambiguous | Specific editor | Low | Medium |
[List ALL tools needing review - include every specific tool ID]

**Total:** [X] tools need manual review
**Priority Breakdown:** High: [X], Medium: [Y], Low: [Z]

---

### Table 4: New Tools to Create

| Suggested ID | Tool Name | Category | Mentions | Source | Departments | Completeness | Risk |
|--------------|-----------|----------|----------|--------|-------------|--------------|------|
| TOOL-VIDEO-015 | Descript | Video_Tools | 4 | RestructuredData | Video, AI | 85% | Low |
| TOOL-AI-039 | Perplexity | AI_Tools | 3 | TASK_MANAGERS | AI, Research | 80% | Low |
[List ALL new tools - include every specific tool]

**Total:** [X] new tools to create
**Source Breakdown:** RestructuredData: [X], TASK_MANAGERS: [Y]

---

### Table 5: Tools to Archive

| Tool ID | Tool Name | Reason | Last Used | Mentions | Risk |
|---------|-----------|--------|-----------|----------|------|
| TOOL-TEST-007 | Test Tool Alpha | Never used | N/A | 0 | Low |
| TOOL-DATA-003 | Legacy Data Processor | Deprecated | Oct 2025 | 0 current | Low |
[List ALL tools to archive - include every specific tool ID]

**Total:** [X] tools to archive
**Archive Reason Breakdown:** Never used: [X], Deprecated: [Y], Test entries: [Z]
```

---

## Output File Locations

### Primary Output
**Report:** `C:\Users\Dell\Dropbox\Nov25\Entities\LIBRARIES\Tools\TOOL_COLLECTION_REPORT_[DATE].md`

### Supporting Files
**Validation Log:** `LBS_003_Tools/TOOL_VALIDATION_LOG_[DATE].md`
- Records all validation actions taken
- Tracks changes to tool entries
- Documents merge decisions
- Lists archived tools

**Updated Mappings:** `TASK_MANAGERS/tool_mapping_updated_[DATE].json`
- Updated tool_mapping.json with new tools
- Includes merge redirects (old ID → new ID)
- Documents ID changes

**Archive Documentation:** `Archive/README.md`
- Documents all archived tools
- Explains merge decisions
- Lists deprecated tools with reasons

---

## Quality Standards

### Tool Entry Completeness Levels

**Level 1: Minimum (Acceptable for "discovered_needs_review")**
- ✓ Tool ID assigned (unique, sequential)
- ✓ Name (specific tool name, not generic)
- ✓ Category (appropriate category assigned)
- ✓ Purpose (1-2 sentence description)
- ✓ Status set

**Level 2: Standard (Required for "active")**
- All Level 1 fields, plus:
- ✓ Vendor identified
- ✓ At least one department or use case
- ✓ Platform compatibility noted
- ✓ actual_remote_helpers_usage has at least one use case

**Level 3: Complete (Goal for all active tools)**
- All Level 2 fields, plus:
- ✓ Documentation URL
- ✓ Multiple use cases with context
- ✓ Departments_using list complete
- ✓ Integration capabilities documented
- ✓ Cost structure noted
- ✓ Strengths and limitations identified

### Acceptable "TBD" Fields
These fields can remain "TBD" for active tools:
- cost_structure (if free/open source, note as "Free")
- documentation_url (for internal/custom tools only)
- integration_capabilities (for standalone tools with no integrations)
- skill_level_required (can infer from usage if not explicitly known)

### Required Fields (Cannot be "TBD" for active tools)
- tool_id
- name
- vendor (must identify or mark "Unknown" with research note)
- category
- purpose/description
- status
- At least ONE of: departments_using, actual_remote_helpers_usage.use_cases

---

## Notes

### Important Context
- **253 tools** were added 2025-11-10 from TASK_MANAGERS analysis
- Priority is validating these tools, not just finding new ones
- tool_mapping.json is the source of truth for task→tool associations
- TASK_MANAGERS now uses simplified IDs: AI-006, not TASK-AI-006
- Step files use format: AI-006-03_slug.md

### Update Frequency
- Run validation: Weekly
- Run full collection: Monthly
- Audit tool entries: Quarterly
- Review "discovered_needs_review" status: Weekly

### Maintenance Tasks
- Review "discovered_needs_review" status weekly
- Merge duplicates as identified
- Deprecate unused tools after 6 months of no usage
- Update tool_mapping.json whenever tools are merged or IDs change
- Regenerate statistics monthly

---

*Last Updated: 2025-11-11*
*Next Scheduled Run: 2025-11-18 (weekly validation)*
