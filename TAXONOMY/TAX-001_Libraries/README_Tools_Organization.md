# Tools Organization & ID Assignment

**Generated:** 2025-11-19
**Purpose:** Documentation for the tools taxonomy organization, ID assignment, and priority system

---

## Overview

This directory contains the master files for tools organization within the ENTITIES taxonomy. All tools have been analyzed, counted for mentions across the entire ENTITIES system, and assigned priority-based IDs.

---

## Files in This Directory

### 1. Tools_Master_List.csv
**Purpose:** Complete spreadsheet of all tools with IDs, priorities, and mention counts

**Columns:**
- `Tool_ID` - Sequential ID in format TOL-### (001-177)
- `Tool_Name` - Official name of the tool
- `Category` - Tool category (AI Tools, Development Tools, etc.)
- `Mention_Count` - Number of times mentioned across all ENTITIES files
- `Priority` - Priority level based on mention count
- `Departments` - Departments using the tool
- `Filename` - Original JSON filename
- `Source` - Whether from Master Listing or File System

**Usage:** Import into Excel/Google Sheets for analysis and reporting

---

### 2. Tools_Master_Priority.json
**Purpose:** Structured JSON with complete tool data including mention locations

**Structure:**
```json
{
  "metadata": {
    "generated_date": "2025-11-19",
    "total_tools": 177,
    "description": "..."
  },
  "priority_summary": {
    "CRITICAL": 161,
    "HIGH": 5,
    "MEDIUM": 7,
    "LOW": 4,
    "MINIMAL": 0
  },
  "tools": [
    {
      "tool_id": "TOL-###",
      "name": "Tool Name",
      "filename": "filename.json",
      "category": "Category",
      "mention_count": ###,
      "priority": "PRIORITY",
      "departments": "Dept1, Dept2",
      "mentions_by_file": [...]
    }
  ]
}
```

**Usage:** Import into applications, scripts, or cross-referencing systems

---

### 3. Tools_Priority_Analysis_Report.md
**Purpose:** Human-readable markdown report with insights and recommendations

**Contents:**
- Priority distribution summary
- Top 20 most mentioned tools
- Tools grouped by priority level
- Recommendations for next steps

**Usage:** Review, planning, and documentation

---

## Priority System

Tools are assigned priority levels based on mention frequency across all ENTITIES files:

| Priority | Criteria | Count | Action |
|----------|----------|-------|--------|
| **CRITICAL** | 20+ mentions | 161 tools | Must document, highest importance |
| **HIGH** | 10-19 mentions | 5 tools | Important, document soon |
| **MEDIUM** | 5-9 mentions | 7 tools | Moderate importance |
| **LOW** | 1-4 mentions | 4 tools | Lower priority |
| **MINIMAL** | 0 mentions | 0 tools | Consider archiving |

---

## ID Assignment Strategy

### Format: `TOL-###`

- **TOL** = Tool identifier prefix
- **###** = Sequential 3-digit number (001-177)

### Assignment Order:
1. **Priority-based:** Tools sorted by mention count (highest first)
2. **Sequential numbering:** IDs assigned 001-177 in descending priority order
3. **Unique IDs:** Each tool gets exactly one ID

### Examples:
- `TOL-001` = LinkedIn (5,148 mentions - #1 most used)
- `TOL-002` = Claude (5,076 mentions - #2 most used)
- `TOL-020` = GLIF (1,060 mentions)
- `TOL-177` = CRM MCP Connector (2 mentions - lowest)

---

## Top 20 Most Used Tools

| Rank | ID | Tool Name | Category | Mentions | Priority |
|------|-----|-----------|----------|----------|----------|
| 1 | TOL-001 | LinkedIn | Social/Business | 5,148 | CRITICAL |
| 2 | TOL-002 | Claude | AI Platform | 5,076 | CRITICAL |
| 3 | TOL-003 | Medium | Publishing | 4,036 | CRITICAL |
| 4 | TOL-004 | Instagram | Social Media | 3,612 | CRITICAL |
| 5 | TOL-005 | Dropbox | File Management | 3,528 | CRITICAL |
| 6 | TOL-006 | YouTube | Video Platform | 2,856 | CRITICAL |
| 7 | TOL-007 | n8n | Automation | 2,816 | CRITICAL |
| 8 | TOL-008 | GitHub | Development | 2,564 | CRITICAL |
| 9 | TOL-009 | Anymailfinder | Data/Lead Gen | 2,048 | CRITICAL |
| 10 | TOL-010 | Apify | Web Scraping | 1,884 | CRITICAL |
| 11 | TOL-011 | Gemini | AI Platform | 1,836 | CRITICAL |
| 12 | TOL-012 | Cursor | AI Dev Tool | 1,560 | CRITICAL |
| 13 | TOL-013 | OpenArt | AI Image Gen | 1,376 | CRITICAL |
| 14 | TOL-014 | React | Development | 1,208 | CRITICAL |
| 15 | TOL-015 | Behance | Design Portfolio | 1,180 | CRITICAL |
| 16 | TOL-016 | Perplexity | AI Search | 1,168 | CRITICAL |
| 17 | TOL-017 | Docker | DevOps | 1,140 | CRITICAL |
| 18 | TOL-018 | TikTok | Social Media | 1,140 | CRITICAL |
| 19 | TOL-019 | Airscale | Data Tools | 1,076 | CRITICAL |
| 20 | TOL-020 | GLIF | AI Workflow | 1,060 | CRITICAL |

---

## Tool Categories

### AI Tools (73 tools)
- AI Platforms (Claude, ChatGPT, Gemini, Perplexity)
- Image Generation (Midjourney, Leonardo, OpenArt, Flux)
- Video Generation (Sora, VAYU, Kling, Seedream)
- AI Development (Cursor, Claude Desktop, v0.dev)
- Workflow Automation (GLIF, MCP Builder)

### Development Tools (40+ tools)
- Web Scraping (Apify, Bright Data)
- Frameworks (React, FastAPI, Streamlit)
- DevOps (Docker, GitHub Actions)
- Cloud (Google Cloud, Azure, Render)
- Databases (Supabase, PostgreSQL, Neo4j)

### Automation Tools (8 tools)
- Workflow (n8n, Make.com, Zapier)
- Lead Gen (AmpleLeads, LeadsRapidly, Vayne)

### Data Tools (5 tools)
- Email Finding (Anymailfinder, Airscale)
- Web Scraping (Bright Data, Apify scrapers)

### Business Tools (5 tools)
- CRM (Apollo.io, LinkedIn Sales Navigator)
- Email (Instantly.ai)

### Social/Publishing Platforms (30+ tools)
- Major platforms (LinkedIn, Instagram, YouTube, TikTok)
- Professional (Behance, Dribbble, GitHub)
- Publishing (Medium, Substack, Dev.to)

---

## File Naming Convention

### Recommended Format:
`TOL-###_Tool_Name.json`

### Examples:
- `TOL-001_LinkedIn.json`
- `TOL-002_Claude.json`
- `TOL-020_GLIF.json`
- `TOL-045_Sora.json`

### Implementation:
Use the provided `rename_tool_files.py` script to batch rename all tool files with proper ID prefixes.

---

## Cross-Reference Integration

All tools should be referenced by ID in:

1. **Objects** (`LIBRARIES/Responsibilities/Objects/`)
   - Link tools used to create objects
   - Format: `"tool_id": "TOL-###"`

2. **Actions** (`LIBRARIES/Responsibilities/Actions/`)
   - Link tools commonly used for actions
   - Format: `"tool_ids": ["TOL-###", "TOL-###"]`

3. **Workflows** (`TASK_MANAGERS/Workflows/`)
   - Link all tools used in workflow steps
   - Format: `"tool_id": "TOL-###"`

4. **Professions** (`LIBRARIES/Professions/`)
   - Link tools used by profession
   - Format: `"tool_id": "TOL-###"`

---

## Maintenance Scripts

### 1. count_tool_mentions.py
**Purpose:** Scan all ENTITIES files and count tool mentions

**Usage:**
```bash
python count_tool_mentions.py
```

**Outputs:**
- `Tools_Master_List.csv`
- `Tools_Master_Priority.json`
- `Tools_Priority_Analysis_Report.md`

**When to Run:**
- After adding new tools
- After major content updates
- Monthly maintenance check

---

### 2. rename_tool_files.py
**Purpose:** Rename tool files with TOL-### prefixes

**Usage:**
```bash
python rename_tool_files.py
```

**Features:**
- Dry run preview
- Confirmation prompt
- Generates rename log

**Outputs:**
- Renamed files in place
- `Tool_File_Rename_Log.md`

---

## Integration with Video Processing Workflow

The taxonomy integration prompt ([PMT-009_Taxonomy_Integration.md](../PROMPTS__Video_Processing__Taxonomy_Integration/PMT-009_Taxonomy_Integration.md)) uses this tool organization for:

1. **Gap Analysis:** Identify tools mentioned in videos but missing from taxonomy
2. **Tool Creation:** Create new tool entries with proper TOL-### IDs
3. **Priority Assignment:** Use mention counts to prioritize documentation
4. **Cross-Referencing:** Link tools to objects, workflows, and professions

---

## Next Steps & Recommendations

### Immediate (Week 1)
1. ✅ Generate Tools Master List with IDs and priorities
2. ✅ Create priority analysis report
3. ⏳ Optionally rename tool files with ID prefixes (use script)
4. ⏳ Update `AI_Tools_Master_Listing.json` with new TOL-### IDs

### Short-term (Month 1)
1. Update all Object files to reference tools by TOL-### IDs
2. Update all Action files to reference tools by TOL-### IDs
3. Update all Workflow files to reference tools by TOL-### IDs
4. Update all Profession files to reference tools by TOL-### IDs
5. Document top 20 CRITICAL tools with detailed JSON entries

### Long-term (Quarter 1)
1. Establish automated monitoring of tool mentions
2. Create tool recommendation engine based on usage patterns
3. Build tool dependency graph
4. Integrate tool taxonomy with skill taxonomy
5. Create tool-to-outcome mapping

---

## Related Documentation

- [Libraries Master List](./Libraries_Master_List.csv) - All LIBRARIES entities
- [Libraries Hierarchy](./Libraries_Hierarchy_Tree.md) - Visual structure
- [PMT-009 Taxonomy Integration](../PROMPTS__Video_Processing__Taxonomy_Integration/PMT-009_Taxonomy_Integration.md) - Video processing workflow
- [Tools Directory](../../LIBRARIES/Tools/) - All tool JSON files

---

## Changelog

### 2025-11-19
- Initial tool analysis completed
- 177 tools analyzed across all ENTITIES
- Priority system established (CRITICAL to MINIMAL)
- Sequential TOL-### IDs assigned (001-177)
- Master CSV, JSON, and Report generated
- Rename scripts created

---

**Maintained By:** Taxonomy Team
**Last Updated:** 2025-11-19
**Status:** Active - Production Ready
