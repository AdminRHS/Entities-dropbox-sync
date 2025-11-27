---
category: PROMPTS
subcategory: root
type: prompt
source_id: Universal Research Prompt
title: Universal Research Prompt
date: 2025-11-23
status: draft
owner: unknown
related: []
links: []
---

# Universal Research Prompt

## Summary
- TODO

## Context
- TODO

## Data / Content
# ROLE & OBJECTIVE
Act as a Senior Technical Researcher for "Remote Helpers." Your goal is to find high-value, actionable video tutorials.

# VARIABLES (User Input)
TOPIC = [e.g., AI Tools for HR, New Automation Features]
TIMEFRAME = [e.g., Last 30 days]
TECH_STACK_FILTER = [e.g., Must integrate with Notion or n8n]
EXCLUDE = [e.g., Reaction videos, Podcasts, Marketing fluff, "Top 10" lists]

# SEARCH PROTOCOL
1.  **Date Calculation:** Identify today's date. Calculate the start date based on the {TIMEFRAME}.
2.  **Query Generation:** Generate 5 distinct YouTube search queries for {TOPIC} combined with terms like "tutorial," "workflow," "walkthrough," "guide," and "how-to."
3.  **Filtering:** Exclude YouTube Shorts and videos under 5 minutes.
4.  **Quality Check:** Prioritize content that shows the user's screen/UI over "talking head" videos.

# OUTPUT FORMAT (Markdown Table preferred)
Create a table with the following columns:
| Relevance (0-100) | Video Title & URL | Channel | Duration | Key Workflow/Insight |
|-------------------|-------------------|---------|----------|----------------------|

# DETAILED ANALYSIS
For the Top 3 most relevant videos, provide a deep dive:
**[Video Title]**
* **Direct Value:** One sentence on why this specific video solves a problem.
* **Tech Stack:** List tools used.
* **Implementation Level:** (Beginner/Intermediate/Advanced)
* **Timestamp:** Highlight the specific timestamp where the "meat" of the tutorial begins.

# CONTEXT
I represent "Remote Helpers," a 32-person remote services company. We are transitioning to an AI-first infrastructure.
**Current Strategic Goals:**
1.  **Reduction:** 60-80% admin overhead reduction via AI.
2.  **Automation:** Transitioning from n8n/Make to Natural Language Automation (Opal AI) and Agentic Workflows (Claude MCP).
3.  **Development:** Heavy use of Cursor IDE, Windsurf, and automated documentation.
4.  **Creative:** Adoption of WAN 2.2 and Open Source video generation.

# TASK
Search YouTube for videos published in the **last 45 days** that directly address our Strategic Goals.

# PRIORITY KEYWORDS (Use these to drive search)
* "Claude MCP integration tutorial"
* "Opal AI automation workflow"
* "WAN 2.2 video generation guide"
* "Cursor IDE agentic workflow"
* "Whisper to Claude transcription automation"
* "Discord bot advanced logging python"

# NEGATIVE CONSTRAINTS
* Ignore generic "Intro to AI" videos.
* Ignore videos that do not show actual code, nodes, or configuration screens.
* Ignore "Reaction" videos or "News roundups" without demos.

# SCORING ALGORITHM
Rate every video (0-100) based on:
* +40 pts: Does it solve a specific Remote Helpers Goal?
* +30 pts: Does it use our stack (Claude, Cursor, n8n, Opal)?
* +30 pts: Is it a step-by-step implementation guide?

# OUTPUT
List the top 8-12 videos sorted by Score.
Format:
### [Score] [Title](URL)
**Time:** [Duration] | **Channel:** [Name]
**Why it fits Remote Helpers:** [Specific connection to our goals]
**Actionable Takeaway:** [The specific workflow or script we can copy]

# CONTEXT
I represent "Remote Helpers," a 32-person remote services company. We are transitioning to an AI-first infrastructure.
**Current Strategic Goals:**
1.  **Reduction:** 60-80% admin overhead reduction via AI.
2.  **Automation:** Transitioning from n8n/Make to Natural Language Automation (Opal AI) and Agentic Workflows (Claude MCP).
3.  **Development:** Heavy use of Cursor IDE, Windsurf, and automated documentation.
4.  **Creative:** Adoption of WAN 2.2 and Open Source video generation.

# TASK
Search YouTube for videos published in the **last 45 days** that directly address our Strategic Goals.

# PRIORITY KEYWORDS (Use these to drive search)
* "Claude MCP integration tutorial"
* "Opal AI automation workflow"
* "WAN 2.2 video generation guide"
* "Cursor IDE agentic workflow"
* "Whisper to Claude transcription automation"
* "Discord bot advanced logging python"

# NEGATIVE CONSTRAINTS
* Ignore generic "Intro to AI" videos.
* Ignore videos that do not show actual code, nodes, or configuration screens.
* Ignore "Reaction" videos or "News roundups" without demos.

# SCORING ALGORITHM
Rate every video (0-100) based on:
* +40 pts: Does it solve a specific Remote Helpers Goal?
* +30 pts: Does it use our stack (Claude, Cursor, n8n, Opal)?
* +30 pts: Is it a step-by-step implementation guide?

# OUTPUT
List the top 8-12 videos sorted by Score.
Format:
### [Score] [Title](URL)
**Time:** [Duration] | **Channel:** [Name]
**Why it fits Remote Helpers:** [Specific connection to our goals]
**Actionable Takeaway:** [The specific workflow or script we can copy]

# ROLE
HR Automation Researcher.
**Timeframe:** Last 60 days.

# MISSION
Find practical tutorials on applying AI to HR workflows (Recruitment, Onboarding, Employee Data).

# SEARCH MATRIX (Combine these terms)
* **Tools:** Claude Desktop, ChatGPT Team, NotebookLM, n8n.
* **Tasks:** "CV Screening," "Onboarding Checklist Automation," "Interview Scheduling," "Employee FAQ Bot."

# FILTERING RULES
* **Strictly exclude** theoretical videos on "The Future of Work."
* **Include only** videos that show a screen recording of the process.
* **Compliance Check:** Note if the video mentions GDPR or Data Privacy (Crucial for EU/Ukraine ops).

# OUTPUT
Group results by Category:
1.  **Recruitment Automation**
2.  **Internal Ops & Data**
3.  **Training/Onboarding**

Format: **[Title](URL)** - *[Tool Used]* - *[One-sentence Value Prop]*

# OBJECTIVE
Find technical implementation tutorials for n8n, OpenAI API (v2/Realtime), and Google Workspace Automation.
**Timeframe:** Last 60 days relative to {{CURRENT_DATE}}.

# SEARCH CRITERIA
Search for videos that meet these requirements:
1.  **Complexity:** Intermediate to Advanced (Loops, Error Handling, API integration).
2.  **Resources:** High priority for videos that share **JSON Workflows**, **GitHub Repos**, or **Code Snippets** in the description.
3.  **Topic Focus:**
    * n8n AI Agents (LangChain nodes).
    * OpenAI Realtime API / Structured Outputs.
    * Google Apps Script + Gemini integration.

# EXECUTION STEPS
1.  Search for: "n8n AI agent tutorial json download", "OpenAI realtime api tutorial code", "Google apps script gemini automation".
2.  Filter out videos that only use Zapier or generic no-code tools without logic.

# OUTPUT FORMAT
For each valid result:

## 🔧 [Title](URL)
* **Tech Stack:** [e.g. n8n + Pinecone + OpenAI]
* **Resources Available:** [JSON / GitHub / None]
* **Key Mechanism:** Briefly explain the logic (e.g., "Uses a sub-workflow to handle error loops").
* **Implementation Difficulty:** [1-5]

## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-23 standardization scaffold added
