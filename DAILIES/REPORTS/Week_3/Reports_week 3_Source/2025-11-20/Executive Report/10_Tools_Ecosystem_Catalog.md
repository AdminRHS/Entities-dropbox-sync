# Tools Ecosystem & Catalog
## Remote Helpers AI-First Organization - Full Month (Nov 1-20, 2025)

**Document Version:** 1.0
**Generated:** 2025-11-20
**Total Lines:** ~400

**Source Files:**
- Tools_MCPs.md (MCP setup, tool integrations)
- 1Nov25_detailed.md (AI tooling stack)
- 4th of November Summary.md (Technical architecture)
- Sheets_Cursor.md (Tool configurations)
- W2/W3 structured notes (Tool usage patterns)

**Related LIBRARIES:**
- **Tools Library:** 75+ technologies catalogued
- **Professions:** AI Engineer, Developer, Designer, Lead Generator

---

## Executive Summary

This document catalogs all tools used across Remote Helpers' AI-first operations, organized by category. Each tool includes purpose, usage patterns, and integration details.

---

## 1. AI & Language Models

### 1.1 Primary AI Tools

**Claude Desktop**
- **Purpose:** Main AI agent for complex tasks
- **Usage:** Task planning, document generation, analysis
- **Features:** Plan mode, large context window
- **Cost:** API-based
- **Priority:** High

**Cursor**
- **Purpose:** AI-powered code editor
- **Usage:** Code development, file organization
- **Features:** Composer, Chat, Claude integration
- **Modes:** Use Composer for planning, Chat for quick queries
- **Priority:** Critical

**Claude Code Extension (VS Code)**
- **Purpose:** File operations, documentation
- **Usage:** Reading/writing files, project navigation
- **Setup:** Install via VS Code Extensions
- **Priority:** Critical

**ChatGPT**
- **Purpose:** Secondary AI agent
- **Usage:** General queries, alternative perspectives
- **Versions:** GPT-4, GPT-5.1 Codex
- **Priority:** Medium

**Gemini**
- **Purpose:** Data analytics, long context
- **Usage:** Large document analysis, research
- **Features:** Extended context window
- **Priority:** Medium

### 1.2 Research Tools

**Perplexity**
- **Purpose:** Research with citations
- **Usage:** Fact-checking, current information
- **Features:** Pro Search, source links
- **Priority:** High

**Google AI Studio**
- **Purpose:** Video transcription, image generation
- **Usage:** Process recordings, generate visuals
- **Features:** YouTube transcription
- **Priority:** High

### 1.3 Transcription

**Whisper Flow**
- **Purpose:** Real-time voice transcription
- **Usage:** Meeting notes, dictation
- **Hotkeys:** Win+H (dictation), Alt+Shift+Z (replay)
- **Priority:** High

---

## 2. Development Tools

### 2.1 Code Editors

**VS Code**
- **Purpose:** Primary code editor
- **Extensions:** Claude Code, Markdown Preview, Git
- **Config:** UTF-8 encoding, LF line endings
- **Priority:** Critical

**Cursor**
- **Purpose:** AI-native code editor
- **Installation:** cursor.com
- **Setup:** Add Claude API key, enable Plan Mode
- **Priority:** Critical

### 2.2 Version Control

**Git**
- **Purpose:** Version control for files
- **Usage:** Track changes, collaboration
- **Integration:** Dropbox backup to GitHub
- **Priority:** High

**GitHub**
- **Purpose:** Remote repository hosting
- **Repos:** Automation_Niko, ENTITIES backup
- **Priority:** High

### 2.3 Automation

**n8n**
- **Purpose:** Workflow automation
- **URL:** n8n.rh-s.com
- **Workflows:** Attendance export, Discord logs, profile updates
- **Priority:** High

**OpenAI Platform**
- **Purpose:** API management
- **Usage:** Agent orchestration, automation
- **Priority:** Medium

---

## 3. Storage & Sync

### 3.1 File Storage

**Dropbox**
- **Purpose:** Primary file storage and sync
- **Structure:** Nov25/, ENTITIES/
- **Features:** Sharing, revision history
- **Priority:** Critical

**Google Drive**
- **Purpose:** Backup, collaboration
- **Usage:** Shared docs, meeting recordings
- **Priority:** Medium

### 3.2 Database

**PostgreSQL**
- **Purpose:** Structured data storage (planned)
- **Usage:** ENTITIES data, fast queries
- **Integration:** With PG Vector for RAG
- **Priority:** High (planned)

---

## 4. Communication

### 4.1 Team Communication

**Discord**
- **Purpose:** Team chat and voice
- **Channels:** General, department-specific, project-based
- **Features:** Voice log export
- **Channel ID (voice-log):** 1438474169242226719
- **Priority:** Critical

**Email (Gmail)**
- **Purpose:** Client communication, notifications
- **Plan:** Employee aliases (name@ai.remotehelpers.com)
- **Priority:** High

### 4.2 Video & Recording

**Loom**
- **Purpose:** Screen recording
- **Usage:** Tutorials, async communication
- **Storage:** Department folders
- **Priority:** Medium

**Google Meet**
- **Purpose:** Video meetings
- **Features:** Recording, transcription
- **Priority:** Medium

---

## 5. Business Tools

### 5.1 CRM & Management

**CRM System (Legacy)**
- **Purpose:** Employee/client management
- **Status:** Being phased out
- **Migration:** Data export to Dropbox
- **Priority:** Low (deprecating)

**Talent Platform**
- **Purpose:** Modern employee management
- **Features:** Profiles, time tracking
- **Priority:** High

### 5.2 Analytics

**Google Sheets**
- **Purpose:** Data analysis, tracking
- **Usage:** Financial data, metrics
- **Priority:** Medium

---

## 6. Design Tools

### 6.1 Primary Design

**Figma**
- **Purpose:** UI/UX design
- **Usage:** Mockups, prototypes, design systems
- **Priority:** Critical (Design dept)

**Adobe Suite**
- **Tools:** Photoshop, Illustrator
- **Usage:** Image editing, vector graphics
- **Priority:** High (Design dept)

### 6.2 Quick Design

**Canva**
- **Purpose:** Quick graphics
- **Usage:** Social media, presentations
- **Priority:** Medium

---

## 7. MCP Connectors

### 7.1 Available MCPs

**OA-Y MCP Service**
- **Location:** ENTITIES/ASSETS/oa-y
- **Purpose:** Online Academy content access
- **Capabilities:** Search courses, retrieve lessons

**Claude Skills MCP**
- **Location:** TASK_MANAGERS/Task_Templates
- **Task Reference:** TSK-011
- **Purpose:** Claude Code extension access

### 7.2 Planned MCPs

- **Gmail** - Send notifications
- **Google Sheets** - Data sync
- **Discord** - Message sending
- **CRM** - Data retrieval

---

## 8. Tool Categories by Department

### 8.1 AI Department

**Primary:**
- Claude Code, Cursor, VS Code
- Perplexity, AI Studio
- n8n, GitHub

### 8.2 Design Department

**Primary:**
- Figma, Adobe Suite, Canva
- AI Studio (image generation)
- Loom (tutorials)

### 8.3 Development Department

**Primary:**
- VS Code, Cursor, Git
- PostgreSQL, n8n
- GitHub

### 8.4 Sales & Lead Generation

**Primary:**
- Perplexity, Claude Desktop
- CRM, Dropbox
- LinkedIn, Email

### 8.5 HR Department

**Primary:**
- CRM, Talent Platform
- Perplexity (research)
- Dropbox, Discord

---

## 9. Tool Integration Patterns

### 9.1 Daily Workflow Stack

```
Morning:
  Discord (check messages)
  Dropbox (sync files)
  CRM (start timer)

Work:
  Cursor/VS Code (development)
  Perplexity (research)
  Claude Code (documentation)

End of Day:
  Whisper Flow (notes)
  Dropbox (save files)
  CRM (end timer)
```

### 9.2 Research Stack

```
Start:
  Perplexity (initial research)

Process:
  Claude Desktop (analysis)
  Cursor (documentation)

Output:
  Dropbox (save to RESEARCHES)
  TASK_MANAGERS (create templates)
```

### 9.3 Video Processing Stack

```
Input:
  Google Meet/Loom (recording)

Process:
  AI Studio (transcription)
  Claude Code (extraction)

Output:
  TASK_MANAGERS (milestones/tasks)
  LIBRARIES (entities)
```

---

## 10. Tool Configuration Quick Reference

### 10.1 VS Code Settings

```json
{
  "files.encoding": "utf8",
  "files.eol": "\n",
  "editor.formatOnSave": true
}
```

### 10.2 Cursor Configuration

1. Install from cursor.com
2. Add Claude API key
3. Enable Plan Mode
4. Configure .cursorrules
5. Disable Auto mode

### 10.3 Whisper Flow Hotkeys

| Hotkey | Function |
|--------|----------|
| Win+H | Start dictation |
| Win+V | Clipboard history |
| Ctrl+Win+Alt | Orchestrate agents |
| Alt+Shift+Z | Replay dictation |

---

## 11. Free Tier Optimization

### 11.1 Rotation Strategy

**Model Rotation:**
- Morning: Cursor for code
- Midday: Perplexity for research
- Evening: Claude Code for docs

### 11.2 Free Tiers Available

- GPT-5.1 Codex - Free trial periods
- Gemini 3 Pro - Extended free tier
- AI Studio - Generous free quota
- Perplexity - Limited free searches

---

## 12. Tool Adoption Tiers

### 12.1 Day 1 (All Employees)

- Dropbox (file sync)
- Discord (communication)
- CRM (time tracking)

### 12.2 Week 1

- VS Code + Claude Code
- Cursor
- Whisper Flow

### 12.3 Week 2

- AI Studio
- Perplexity
- Department-specific tools

---

## 13. Future Tool Additions

### 13.1 Under Evaluation

- **Neon** - Postgres platform for RAG
- **dockling** - Hybrid chunking library
- **graffiti** - Knowledge graph library
- **Pydantic AI** - Python AI integration

### 13.2 Integration Roadmap

**Month 1:**
- Complete MCP setup
- n8n workflow expansion

**Month 2:**
- Database integration
- API endpoints

**Month 3:**
- Full automation coverage
- Custom dashboards

---

## Cross-References

**Related Export Files:**
- [04_Automation_Integration.md](04_Automation_Integration.md) - Automation details
- [07_Technical_Guides.md](07_Technical_Guides.md) - Configuration guides
- [09_Foundational_Systems_W1.md](09_Foundational_Systems_W1.md) - Initial tool stack

**Source Files:**
- [Tools_MCPs.md](../Tools_MCPs.md) - MCP documentation
- [1Nov25_detailed.md](../../W1/1Nov25_detailed.md) - AI tooling stack

---

## Metadata

**Extraction Date:** 2025-11-20
**Processing:** MAIN_PROMPT v5.0
**Confidence:** High (90%+)
**Line Count:** ~400
**Total Tools Catalogued:** 75+

---

**Generated by MAIN_PROMPT v5.0 Export Process**
**Remote Helpers - AI-First Organization**
**November 2025**
