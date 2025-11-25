# Technical Guides & Best Practices
## Remote Helpers AI-First Organization - Week 2-3 (Nov 8-20, 2025)

**Document Version:** 1.0
**Generated:** 2025-11-20
**Total Lines:** ~400

**Source Files:**
- Task Manager.md (Data extraction prompt v2.2)
- Sheets_Cursor.md (Setup guides)
- 171125_Niko.md (Cursor/VS Code usage)
- 191225_Niko.md (Multi-model approach)
- MAIN_PROMPT_v5_Modular (Prompt engineering)

**Related LIBRARIES:**
- **Actions:** Configure, Setup, Install, Document, Create, Update
- **Objects:** Guide, Prompt, Configuration, Template, Documentation
- **Tools:** Cursor, Claude Code, VS Code, Perplexity, AI Studio
- **Processes:** Prompting, Configuration, Documentation, Setup

---

## Executive Summary

Week 2-3 established technical best practices for AI tool usage, prompt engineering, file organization, and multi-model workflows. These guides enable consistent, efficient work across all employees regardless of technical background.

**Core Topics:**
- Prompt engineering methodology
- Multi-model workflow strategy
- File naming conventions
- Tool configuration guides
- UTF-8 and encoding fixes

---

## 1. Prompt Engineering Methodology

### 1.1 Prompt Versioning

**Format:** `v[major].[minor]`

**When to increment:**
- Minor (v3.1 → v3.2): Clarification, small fixes
- Major (v3.2 → v4.0): Structure change, new sections

**Header Template:**
```markdown
# Prompt Name
**Version:** v3.2
**Last Updated:** 2025-11-19
**Purpose:** [Description]

## Changelog
- v3.2: Added section X, fixed Y
- v3.1: Clarified Z
```

### 1.2 Post-Use Improvement

**After every prompt use:**
1. Evaluate output quality
2. Ask AI: "How should I have prompted to get better results?"
3. Document suggestion
4. Update prompt version
5. Save in prompts.md

### 1.3 Prompt Structure

**Standard Sections:**
1. Context (who you are, what you're doing)
2. Objective (specific goal)
3. Input (data being provided)
4. Output format (structure expected)
5. Constraints (rules, limitations)
6. Examples (sample outputs)

**Example:**
```markdown
## Context
You are processing daily notes for Remote Helpers.

## Objective
Extract all action items and convert to TASK_MANAGERS format.

## Input
- Daily notes in markdown
- Employee name
- Date

## Output
- List of TSK-### entries
- Each with description, assignee, deadline

## Constraints
- Only extract explicit action items
- Ignore hypotheticals
- Link to existing ACT-### when possible

## Example
[Sample input → output]
```

---

## 2. Data Extraction Prompt v2.2

### 2.1 Skills Extraction Formula

**Formula:** `[RESULT] + [OBJECT] + via/using/in + [TOOL]`

**Transformation:**
| Action | Result |
|--------|--------|
| Create | Created |
| Design | Designed |
| Build | Built |
| Analyze | Analyzed |
| Generate | Generated |

### 2.2 Extraction Rules

**Only extract from completed tasks (✅)**

**Include:**
- Object created/modified
- Tool used
- Context (for what purpose)

**Exclude:**
- In-progress tasks
- Failed attempts
- Planned work

### 2.3 Output Format

```yaml
SKILL_ID: SKILL-DEV-023
SKILL_PHRASE: "Created REST API using FastAPI"
COMPONENTS:
  result: Created
  object: REST API
  tool: FastAPI
PROFESSION: Developer
PROFICIENCY: Intermediate
FREQUENCY: 5
FIRST_DEMONSTRATED: 2025-11-08
LAST_DEMONSTRATED: 2025-11-14
```

---

## 3. Multi-Model Workflow

### 3.1 Model Selection Strategy

**For Local Development (Prompts, Code):**
- **Cursor** - Best for code context
- **Claude Code** - Best for file operations
- **VS Code Extensions** - Various AI integrations

**For Research (Web):**
- **Perplexity** - Best for citations, recent info
- **Gemini** - Best for data analytics
- **ChatGPT** - Best for general queries

### 3.2 Token Management

**Problem:** Single model exhausts tokens quickly

**Solution:** Rotate models by task type
- Morning: Cursor for code
- Midday: Perplexity for research
- Evening: Claude Code for documentation

### 3.3 Free Tier Optimization

**Use free tiers strategically:**
- GPT-5.1 Codex (Cursor) - Free for 2 days
- Gemini 3 Pro - Extended free tier
- Claude Code Extension - API-based

**Tip:** Track model releases, switch to free trials

---

## 4. File Organization Standards

### 4.1 Naming Conventions

**Daily Files:** `YYMMDD_[topic].md`
- Example: `191125_meeting_notes.md`

**Task Templates:** `TSK-###_[Name].md`
- Example: `TSK-011_Install_Claude_Skills.md`

**No Spaces:** Use underscores
- Correct: `Data_Extraction_v2.md`
- Incorrect: `Data Extraction v2.md`

### 4.2 Folder Structure Standards

**Every department folder must have:**
1. Logs.md
2. prompts.md
3. readme.md
4. issues.md
5. tools.json
6. task_templates.md

### 4.3 Index Files

**Purpose:** Quick navigation for AI and humans

**Format:**
```markdown
# Actions Index

## High Priority (50+ uses)
- ACT-001: Create [→ ACT-001_Create.md]
- ACT-015: Update [→ ACT-015_Update.md]

## Medium Priority (20-49 uses)
- ACT-023: Analyze [→ ACT-023_Analyze.md]
```

---

## 5. Tool Configuration Guides

### 5.1 Cursor Setup

**Required Extensions:**
- Claude Code
- Markdown Preview
- Git integration

**Configuration:**
1. Install Cursor from cursor.com
2. Add Claude API key
3. Enable Plan Mode
4. Configure .cursorrules

**Model Selection:**
- Use Composer for planning
- Use Chat for quick queries
- Disable Auto mode (unreliable)

### 5.2 VS Code + Claude Code

**Installation:**
1. Install VS Code
2. Extensions → Search "Claude Code"
3. Install and authenticate
4. Configure workspace settings

**Best Practices:**
- Use for file operations
- Keep context window small
- Save prompts in prompts.md

### 5.3 Perplexity Setup

**For Research:**
1. Create account
2. Enable Pro Search (if available)
3. Set citation preferences
4. Connect to workspace

**Prompting Tips:**
- Ask for sources
- Specify date range
- Request structured output

---

## 6. UTF-8 and Encoding Fixes

### 6.1 Common Issues

**Problem:** Russian/Ukrainian text displays as ???

**Cause:** File saved with wrong encoding

**Solution:**
1. Open in VS Code
2. Click encoding in status bar
3. Select "UTF-8"
4. Save file

### 6.2 Prevention

**Always use:**
- UTF-8 encoding
- LF line endings (not CRLF)
- No BOM

**VS Code Settings:**
```json
{
  "files.encoding": "utf8",
  "files.eol": "\n"
}
```

---

## 7. Plan Mode Usage

### 7.1 When to Use Plan Mode

**Use for:**
- Complex multi-step tasks
- Architecture decisions
- Large file changes
- Strategy planning

**Don't use for:**
- Simple queries
- Quick fixes
- File reading

### 7.2 Plan Mode Workflow

1. Activate Plan Mode in Cursor
2. Describe the goal
3. AI creates step-by-step plan
4. Review and approve
5. AI executes each step
6. Verify results

### 7.3 Benefits

- Clear execution path
- Visible progress
- Easier debugging
- Better token management

---

## 8. Email & Communication Logging

### 8.1 Email Workflow

**For client communication:**
1. Send email directly (not through intermediary)
2. Log in CRM
3. Add to client folder
4. Extract action items to TASK_MANAGERS

### 8.2 Discord Best Practices

**Message Guidelines:**
- Clear subject
- Tag relevant people
- Include context
- Link to files

**Channel Usage:**
- #general - Announcements
- #department - Team work
- #project-X - Specific projects

---

## 9. Prompt Library Management

### 9.1 Storage Location

**Central:** `ENTITIES/TASK_MANAGERS/PROMPTS/`

**Categories:**
- Research Prompts
- Video Processing
- Daily Reports
- Data Extraction
- Department-specific

### 9.2 Prompt Metadata

**Each prompt file includes:**
- Purpose
- Version
- Input requirements
- Output format
- Example usage
- Changelog

### 9.3 Sharing Prompts

**To share a prompt:**
1. Copy from your prompts.md
2. Post in relevant Discord channel
3. Tag with use case
4. Add to central PROMPTS folder

---

## 10. Quick Reference Cards

### 10.1 Daily Workflow

1. Morning: Check next-day file, Discord
2. Start CRM timer
3. Work from task list
4. Take screenshots (3x)
5. Document in daily notes
6. End CRM timer
7. Update tomorrow's tasks

### 10.2 Research Workflow

1. Receive topic
2. Create prompt in Cursor
3. Run in Perplexity
4. Format results
5. Store in RESEARCHES
6. Extract to LIBRARIES

### 10.3 File Creation Workflow

1. Use correct naming convention
2. Add to proper folder
3. Include metadata header
4. Link to related files
5. Update index

---

## Cross-References

**Related Export Files:**
- [01_Framework_Implementation.md](01_Framework_Implementation.md) - File structure
- [02_RAG_Systems_Knowledge_Management.md](02_RAG_Systems_Knowledge_Management.md) - Knowledge system
- [04_Automation_Integration.md](04_Automation_Integration.md) - Tool integration

**Source Files:**
- [Task Manager.md](../Task%20Manager.md) - Data extraction
- [Sheets_Cursor.md](../Sheets_Cursor.md) - Tool setup
- [MAIN_PROMPT_v5_Modular](../../W3/MAIN_PROMPT_v5_Modular/)

---

## Metadata

**Extraction Date:** 2025-11-20
**Processing:** MAIN_PROMPT v5.0
**Confidence:** High (90%+)
**Line Count:** ~400

---

**Generated by MAIN_PROMPT v5.0 Export Process**
**Remote Helpers - AI-First Organization**
**November 2025**
