# Tool Collection and Matching Prompt (Updated 2025-11-10)

## Objective
Collect, validate, and match all tools mentioned across the taxonomy framework. Identify new tools, validate recently discovered tools (253 tools added 2025-11-10), and enrich existing tool entries with usage context from multiple sources.

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
**Path:** `C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\TASK_MANAGERS`

**Structure:**
```
TASK_MANAGERS/
├── Task_Templates/          # 55 Task Templates
│   ├── AI/
│   │   ├── AI-001.md       # Simplified ID format (was TASK-AI-001.md)
│   │   ├── AI-006.md
│   │   └── ...
│   └── [10 departments: AI, AI, DESIGN, DEV, HR, LG, AI, SALES, VIDEO]
│
├── Step_Templates/          # 335+ Step Templates
│   ├── AI/
│   │   ├── AI-006-03_extract-company-adaptations.md  # ID + slug format
│   │   └── ...
│   └── [10 departments]
│
├── tool_mapping.json        # Maps tool names → Tool IDs
└── discovered_tools.json    # 253 tools found from task analysis
```

**File Types:**
- **Task Templates:** `.md` files with YAML frontmatter
- **Step Templates:** `.md` files with metadata tables
- **Mappings:** `.json` files

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

**File Types:**
- All `.md` files (markdown)
- Unstructured/semi-structured format

**Tool Reference Patterns:**
- Explicit tool names: "using ChatGPT", "with Figma"
- Platform mentions: "on Dropbox", "via Discord"
- Tool categories: "Design Tools", "Automation platform"
- Implicit references: "created in CRM", "exported from analytics"

**Purpose:**
- Historical tool discovery
- Cross-validation of current tools
- Finding missed tools from earlier operations

### Target: LIBRARIES\Tools (Tool Library)
**Path:** `C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\LIBRARIES\Tools`

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

4. **Enrich tool entries:**
   - Add actual_remote_helpers_usage data
   - Fill in departments_using
   - Add specific use_cases from tasks
   - Update status from "discovered_needs_review" to "active"
   - Add documentation_url if found
   - Fill vendor information

5. **Identify issues:**
   - Tools that should be merged (duplicates/variations)
   - Tools miscategorized
   - Tools with insufficient information
   - Generic tool names needing clarification

### Phase 2: Scan RestructuredData for Additional Tools

**Goal:** Find tools mentioned in historical data not yet in library

**Steps:**
1. **Scan all .md files in RestructuredData**
   - Extract tool mentions using patterns (see below)
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
   - Create tool entry with available information
   - Mark status as "discovered_needs_review"

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
   - Create entries for new tools

4. **Update tool usage statistics:**
   - Count how many tasks use each tool
   - Count how many steps use each tool
   - Identify most-used tools
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

**Pattern 4: Platform references**
- Capitalized platform names: Dropbox, Figma, GitHub
- Domain references: .ai, .io platforms

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

### Section 1: Validation Results (253 Tools)
```markdown
## Tool Validation Results

### Tools Validated and Enriched

#### [Tool Name] - TOOL-XXX-###
- **Status:** ✅ Validated → Active
- **Category:** [Category]
- **Mentions Found:** [Count] times in TASK_MANAGERS
- **Used In:**
  - Tasks: [AI-006, HR-001, ...]
  - Steps: [AI-006-03, HR-001-02, ...]
- **Departments Using:** [AI, HR, Design, ...]
- **Use Cases Added:**
  - "Extract company adaptations from documentation" (AI-006-03)
  - "Onboard new developer documentation" (HR-001-05)
- **Enrichments Made:**
  - ✓ Added actual_remote_helpers_usage
  - ✓ Updated departments_using
  - ✓ Added 3 use cases
  - ✓ Updated status to "active"
- **Recommendation:** Tool entry complete

#### [Tool Name] - TOOL-XXX-###
- **Status:** ⚠️ Needs Merge
- **Issue:** Duplicate of TOOL-XXX-###
- **Recommendation:** Merge with [other tool] and update references
```

### Section 2: Matched Tools (From RestructuredData)
```markdown
## Tools Found in RestructuredData

### Exact Matches

#### [Tool Name]
- **Status:** ✅ Already in Library
- **Tool ID:** TOOL-XXX-###
- **Mentions:** [Count] times in historical data
- **Source Files:**
  - 091125_structured.md (3 mentions)
  - Department_Operations_Nov06_2025.md (2 mentions)
- **Context Examples:**
  - "Using [Tool] for prompt compression" (091125_structured.md:45)
  - "Exported from [Tool] to library" (Department_Operations_Nov06_2025.md:102)
- **Enrichment Opportunity:**
  - Add historical use cases from Oct-Nov operations
  - Update workflows based on meeting notes
```

### Section 3: New Tools Discovered
```markdown
## New Tools Discovered

### From RestructuredData

#### [Tool Name]
- **Status:** ❌ Not in Library
- **Suggested Category:** [Category Name]
- **Mentions:** [Count] times
- **Source Files:**
  - 291025-organized.md (line 156)
  - Projects_Milestones_Tasks_Nov05-07_2025.md (line 89)
- **Context:**
  - "Used [Tool] for video transcription" (291025)
  - "Processed with [Tool] before analysis" (Projects)
- **Available Information:**
  - **Vendor:** [If mentioned]
  - **Purpose:** Video transcription and processing
  - **Departments:** Video, AI
  - **Use Cases:** Transcribe client calls, Process meeting recordings
- **Suggested Tool ID:** TOOL-VIDEO-015
- **Recommended Action:** Create new tool entry

### From TASK_MANAGERS (Post-Mapping)

#### [Tool Name]
- **Status:** ❌ Not in tool_mapping.json
- **Found In:**
  - Task: AI-011.md (key_tools array)
  - Step: AI-011-04_slug.md (metadata)
- **Context:** "Create narration notes for AI generation"
- **Suggested Category:** AI_Tools
- **Suggested Tool ID:** TOOL-AI-039
- **Recommended Action:** Add to library and update mapping
```

### Section 4: Tools Needing Review
```markdown
## Tools Requiring Manual Review

### Merge Candidates

#### [Tool Name A] and [Tool Name B]
- **Tool IDs:** TOOL-XXX-### and TOOL-XXX-###
- **Issue:** Appear to be the same tool or variants
- **Evidence:**
  - Both reference same vendor
  - Similar purpose and description
  - Usage patterns overlap
- **Recommendation:** Merge into single entry, keep most complete data
- **Update Required:** Update all task/step references to winning ID

### Miscategorized Tools

#### [Tool Name] - TOOL-XXX-###
- **Current Category:** [Current]
- **Suggested Category:** [Suggested]
- **Reason:** Tool is primarily used for [purpose], not [current purpose]
- **Impact:** [X] tasks reference this tool
- **Recommendation:** Recategorize and update category ID

### Incomplete Tools (Status: discovered_needs_review)

#### [Tool Name] - TOOL-XXX-###
- **Missing Data:**
  - ✗ No vendor information
  - ✗ No documentation_url
  - ✗ Empty actual_remote_helpers_usage
  - ✗ Generic description
- **Found In:** [X] tasks, [Y] steps
- **Recommendation:** Research tool details, complete entry
```

### Section 5: Statistics & Insights
```markdown
## Summary Statistics

### Overall Counts
- **Total Tools in Library:** 254 → [New Total] (after updates)
- **Tools Validated:** [Number] / 253
- **Tools Enriched:** [Number]
- **New Tools Found:** [Number]
  - From RestructuredData: [Number]
  - From TASK_MANAGERS: [Number]
- **Tools Needing Merge:** [Number]
- **Tools Needing Recategorization:** [Number]

### Category Distribution (Updated)
| Category | Before | After | Change |
|----------|--------|-------|--------|
| AI_Tools | 15 | [New] | +[X] |
| Automation_Tools | 95 | [New] | +[X] |
| Documentation_Tools | 37 | [New] | +[X] |
| [etc...] | ... | ... | ... |

### Tool Usage Frequency (Top 10)
1. **[Tool Name]** - Used in [X] tasks, [Y] steps, [Z] departments
2. **[Tool Name]** - Used in [X] tasks, [Y] steps, [Z] departments
3. [...]

### Department Tool Usage
| Department | Tools Used | Most Used Tool |
|------------|------------|----------------|
| AI | [Count] | [Tool] |
| Design | [Count] | [Tool] |
| Development | [Count] | [Tool] |
| [etc...] | ... | ... |

### Tools by Status
- **Active:** [Count] (fully validated, complete data)
- **Discovered_needs_review:** [Count] (awaiting validation)
- **TBD:** [Count] (minimal data, needs research)
- **Deprecated:** [Count] (no longer in use)
```

### Section 6: Recommendations
```markdown
## Recommendations

### Immediate Actions (Priority 1)
1. **Validate remaining tools with "discovered_needs_review" status**
   - [X] tools still need validation
   - Focus on high-frequency tools first

2. **Merge duplicate tool entries**
   - [X] merge candidates identified
   - Update all task/step references after merge

3. **Complete minimal tool entries**
   - [X] tools have incomplete data
   - Research vendor, documentation, pricing info

### Short-term Actions (Priority 2)
1. **Recategorize miscategorized tools**
   - [X] tools in wrong categories
   - Update tool IDs and references

2. **Add new tools from historical data**
   - [X] new tools found in RestructuredData
   - Create entries with available context

3. **Enrich existing tools with usage data**
   - Add use cases from TASK_MANAGERS
   - Update departments_using fields
   - Add workflow references

### Long-term Improvements (Priority 3)
1. **Tool documentation audit**
   - Find and add missing documentation_urls
   - Verify all links still work
   - Add integration guides

2. **Usage analytics**
   - Track tool adoption over time
   - Identify underutilized tools
   - Find opportunities for tool consolidation

3. **Tool relationships**
   - Document tool dependencies
   - Map integration points
   - Create tool ecosystem diagram

### Process Improvements
1. **Automated tool discovery**
   - Run this collection process monthly
   - Set up alerts for new tool mentions
   - Auto-create "needs review" entries

2. **Tool validation workflow**
   - Establish review schedule
   - Assign tool ownership by category
   - Create validation checklist

3. **Documentation standards**
   - Require documentation_url for all tools
   - Mandate minimum data completeness
   - Establish tool entry quality metrics
```

---

## Execution Workflow

### Step-by-Step Process

**1. Prepare Environment**
```bash
# Load existing data
- Load LIBRARIES/Tools/*.json (all 254 tools)
- Load tool_mapping.json
- Load discovered_tools.json (253 tools)
```

**2. Phase 1: Validate Recently Discovered Tools**
```bash
# For each of 253 tools with status "discovered_needs_review":
FOR each tool in discovered_tools.json:
  - Find tool JSON file in LIBRARIES/Tools
  - Search TASK_MANAGERS for usage (grep tool name in all .md files)
  - Extract: tasks using it, steps using it, departments, use cases
  - Update tool JSON with findings
  - Change status to "active" if validated
  - Flag for merge if duplicate detected
  - Flag for recategorization if miscategorized
```

**3. Phase 2: Scan RestructuredData**
```bash
# Scan historical data
FOR each .md file in RestructuredData:
  - Read file content
  - Apply extraction patterns (regex, keyword search)
  - Collect tool mentions with context and line numbers
  - Normalize tool names
  - Match against existing tools (check tool_mapping.json)
  - Record matched/unmatched tools
```

**4. Phase 3: Scan TASK_MANAGERS**
```bash
# Scan current structured data
FOR each task in Task_Templates/*/*.md:
  - Parse YAML frontmatter
  - Extract tool references from taxonomy, key_tools
  - Compare with tool_mapping.json
  - Identify new tools not in mapping

FOR each step in Step_Templates/*/*.md:
  - Parse metadata table
  - Extract Tool and Tool ID fields
  - Cross-reference with tool_mapping.json
  - Flag mismatches
```

**5. Generate Report**
```bash
# Compile all findings
- Section 1: Validation results (253 tools)
- Section 2: Matched tools (RestructuredData)
- Section 3: New tools discovered
- Section 4: Tools needing review
- Section 5: Statistics and insights
- Section 6: Recommendations

# Save report
- Output to: LIBRARIES/Tools/TOOL_COLLECTION_REPORT_[DATE].md
```

**6. Optional: Create/Update Tool Entries**
```bash
# For each new tool discovered:
- Generate tool ID (next in category sequence)
- Create JSON file with available data
- Mark unknown fields as "TBD"
- Set status to "discovered_needs_review"
- Add to tool_mapping.json

# For validated tools:
- Update JSON with enriched data
- Change status from "discovered_needs_review" to "active"
- Save updated file
```

---

## Output File Locations

### Primary Output
**Report:** `C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\LIBRARIES\Tools\TOOL_COLLECTION_REPORT_2025-11-10.md`

### Supporting Files
**Validation Log:** `Tools/tool_validation_log_2025-11-10.json`
- Records all validation actions
- Tracks changes to tool entries
- Notes merge candidates and recategorizations

**Updated Mappings:** `TASK_MANAGERS/tool_mapping_updated_2025-11-10.json`
- Updated tool_mapping.json with new tools
- Includes merge redirects
- Documents ID changes

**New Tools Batch:** `Tools/new_tools_batch_2025-11-10.json`
- JSON array of all new tool entries created
- Ready for review and import

---

## Quality Checklist

### Before Running
- [ ] Verify all source directories exist
- [ ] Backup current tool_mapping.json
- [ ] Backup LIBRARIES/Tools directory
- [ ] Check Python dependencies (yaml, json, pathlib)

### During Execution
- [ ] Monitor for duplicate detection
- [ ] Watch for parse errors in YAML/JSON
- [ ] Track progress through all departments
- [ ] Log all unmatched tools

### After Completion
- [ ] Review merge candidates manually
- [ ] Verify tool ID assignments are sequential
- [ ] Check no tool IDs are duplicated
- [ ] Validate JSON syntax of all new/updated files
- [ ] Test tool_mapping.json loads correctly

### Validation Criteria
**Tool Entry Completeness:**
- ✓ Tool ID assigned (no duplicates)
- ✓ Name and vendor filled
- ✓ Category appropriate
- ✓ Purpose and description clear
- ✓ At least one department or use case
- ✓ Status set (active/discovered_needs_review/deprecated)

**Acceptable "TBD" Fields:**
- cost_structure (if free/open source)
- documentation_url (for internal/custom tools)
- integration_capabilities (for standalone tools)
- skill_level_required (can infer from usage)

**Required Fields (Cannot be "TBD"):**
- tool_id
- name
- category
- purpose/description
- status

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

### Maintenance
- Review "discovered_needs_review" status monthly
- Merge duplicates as identified
- Deprecate unused tools after 6 months of no usage
- Update tool_mapping.json whenever tools are merged or IDs change

---

*Last Updated: 2025-11-10*
*Next Scheduled Run: 2025-11-17 (weekly validation)*
