---
category: PROMPTS
subcategory: root
type: prompt
source_id: PMT-097_YouTube_AI_Models_Deep_Research
title: PMT-097 YouTube AI Models Deep Research
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# PMT-097 YouTube AI Models Deep Research

## Summary
- TODO

## Context
- TODO

## Data / Content
# PMT-097 — YouTube AI Models Deep Research Prompt

**Purpose:** Discover YouTube videos (last 30–60 days) that run deep research on AI models/platforms, comparing capabilities, pricing, deployment options, and providing hands-on tutorials or implementation guidance.  
**Version:** 1.0.0  
**Date:** 2025-11-22  
**Status:** Active  
**Applies To:** AI, Dev, Video, Design departments (multi-model evaluations feed several stacks)  
**Related Prompts:** `PMT-048_YouTube_AI_Tools_Daily.md`, `PMT-093_Design_AI_Video_Discovery.md`, Schema-aligned v2 prompts in `Research_Prompts_Schema_Aligned/`

---

## 1. Mission & Outcomes

**Mission:** Surface the best recent videos that (a) perform deep research or benchmarking on AI models/platforms, (b) compare workflows or pricing, and (c) teach actionable steps (tutorial, build guide, or workflow demo). Each qualifying video should deliver tangible insights Remote Helpers can translate into new workflows, lead-generation tactics, or Upwork-ready service packages.

**What “deep research” means here:**
- Multi-model comparisons (e.g., Claude vs GPT-4o vs Gemini vs Grok vs OpenRouter mixes)
- Platform breakdowns covering latency, pricing, context windows, MCP/agent support, integrations
- Tutorials or implementation guidance (API walk-throughs, demo project builds, RAG/RPA workflows)
- Evidence-backed claims (benchmarks, datasets, metrics, or downloadable assets)

**Deliverables:**
1. Curated list of 6–10 high-scoring videos using the documentation schema below.
2. Highlighted findings per model/platform (strengths, weaknesses, recommended use cases, and how they can support lead-generation funnels or Upwork positioning).
3. Suggested follow-up actions (tool evaluations, workflow prototypes, queue-ready prompts, or lead-gen experiments to run with Design/Sales pods).

---

## 2. Research Parameters

### 2.1 Time & Recency
- **Primary window:** Last 45 days (default filter on YouTube)
- **Extended window:** Up to 60 days if few results; note why older content remains relevant
- **Refresh cadence:** 2× weekly (Mon / Thu) or on-demand before strategic planning sessions

### 2.2 Priority Topics
| Category | Focus Areas |
|----------|-------------|
| **Foundational models** | Claude 3.5/Claude-Code, GPT-4o/4.1 mini, Gemini 1.5 Pro/Flash, Grok 2, MiniMax, DeepSeek |
| **Routing platforms** | OpenRouter, Together API, Fireworks, LlamaEdge |
| **Desktop/agent stacks** | Cursor, Visual Studio + MCP, v0.dev, Bolt.new |
| **Comparison themes** | Latency, context window, structured output, MCP support, RAG quality, pricing tiers, enterprise controls |
| **Tutorial types** | Build a research assistant, automate long-form analysis, compare eval methods, multi-agent orchestration |
| **Go-to-market & lead gen** | Lead magnet builders, Upwork proposal workflows, AI-enhanced onboarding, funnel tracking dashboards |

### 2.3 Preferred Creators / Channels
- Matthew Berman, Matt Wolfe, D-Squared, World of AI, All About AI, Kris DeBruine, Theoretically Media
- Official engineering or product channels (Anthropic, OpenAI, Google, OpenRouter, etc.)
- Credible indie researchers sharing reproducible repos (GitHub links, Colab, JSON assets)

-### 2.4 Lead-Generation Hooks
- Capture whether each video demonstrates:
  - Lead magnet creation flows or demo assets suited for landing pages.
  - Embedded AI guidance inside CRMs, Upwork proposal builders, or outreach dashboards.
  - Metrics or strategies remote teams can reuse for pipeline visibility (conversion %, bid win rates, offer templates).
- Flag departments (Sales, Design, Lead Gen) needing follow-up experiments.

---

## 3. Search Query Recipes

Use Perplexity to generate candidate lists, then jump into YouTube with date filters:

```
"deep research" AI models comparison November 2025
"Claude 3.5 Sonnet vs GPT-4o" benchmark tutorial
"OpenRouter multi-model routing" workflow demo 2025
"Gemini 1.5 Pro API" research assistant tutorial
"Grok 2 vs GPT-4o pricing" video
"Multi-agent MCP workflow" YouTube tutorial 2025
"AI platform stack" evaluation "Remote team"
"RAG benchmark" Claude Gemini comparison October 2025
"AI lead generation dashboard" tutorial 2025
"Upwork proposal system" AI automation "task manager"
"Lead gen funnel" "Claude 3.5" "YouTube tutorial"
```

Combine with modifiers:
- `site:youtube.com "published"` within Perplexity
- Add `intitle:benchmark`, `intitle:tutorial`, or `intitle:"research"`
- Append department names if aiming for functional coverage (`for designers`, `for sales ops`, `for video teams`)

---

## 4. Selection & Scoring Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Depth of Research | 30 | Includes benchmarks, metrics, or rigorous analysis beyond marketing claims |
| Actionability | 25 | Offers step-by-step guidance, code, assets, or downloadable frameworks |
| Multi-Model Insight | 20 | Compares at least two models/tools or showcases integrations |
| Recency & Relevance | 15 | Within window, aligns with Remote Helpers priorities |
| Production Quality | 10 | Clear visuals/audio, structured sections, reliable presenter |

**Minimum Score:** 70/100 to enter final list. Videos 60–69 can be included if they fill a coverage gap (note justification).

---

## 5. Documentation Template

Capture each accepted video using this markdown block:

```markdown
### [Video Title]

**Channel / Creator:** [Name + subscriber count if notable]  
**Published:** YYYY-MM-DD (Age: X days)  
**Duration:** HH:MM:SS  
**Link:** https://youtube.com/...
**Category:** [Benchmark | Tutorial | Workflow Build | Pricing Deep-Dive | Hybrid]

**Models / Platforms Covered:** Claude 3.5, GPT-4o, Gemini 1.5 Pro, OpenRouter, etc.  
**Workflow Focus:** Agent orchestration | Research assistant | Design comp generation | etc.  
**Key Findings:**  
1. [Metric or conclusion]  
2. [Implementation insight]  
3. [Limitation or caution]

**Assets / Resources:** GitHub repo, JSON bundle, spreadsheet, evaluation dataset, etc.  
**Remote Helpers Relevance Score (0-100):** Depth (0-35) + Tool fit (0-35) + Actionability (0-30)  
**Recommended Departments:** [AI, Dev, Design, Video, HR, Sales, Ops, Lead Gen]  
**Priority:** Critical / High / Medium / Low  
**Next Actions:**  
- [ ] Test workflow / reproduce benchmark  
- [ ] Add tool notes to LIBRARIES  
- [ ] Queue for transcription / taxonomy extraction  
- [ ] Share with [team/slack channel]
- [ ] Draft lead-gen or Upwork experiment brief
```

Also produce a **Model Comparison Summary** table aggregating the best metrics or insights by model/platform.

---

## 6. Workflow

1. **Prep (10 min)**  
   - Review open gaps from `Video_Queue_Tracker.md` and `Research_ToDo_*.json`.  
   - Lock time window filters (last 45 days).  
   - Load this prompt + schema-aligned instructions if needed.

2. **Discovery (30–40 min)**  
   - Run 5–7 Perplexity queries + 3–4 direct YouTube filtered searches.  
   - Bookmark 12–15 promising videos; note upload dates and creators.  
   - Exclude shallow news recaps or marketing announce videos.

3. **Evaluation (40–60 min)**  
   - Watch top candidates (1.5× speed) capturing metrics, workflows, and downloadable resources.  
   - Score each video using the table above; discard anything <60 unless uniquely valuable.

4. **Documentation (30 min)**  
   - Fill the template per video.  
   - Build comparison summary (table or bullet) highlighting best model/platform per use case.  
   - Flag immediate action items (tool testing, queue addition, taxonomy update).

5. **Handoff (15 min)**  
   - Save findings inside the current week’s research log or department-specific `TASK_MANAGERS/RESEARCHES/sessions/`.  
   - Update `TASK_MANAGERS` or queue entries if new transcription work is needed.  
   - Notify stakeholders via daily/weekly research digest.

_Total session time: ~2.5 hours. Adjust if more videos need deep review._

---

## 7. Output & Filing

- **Primary save location:** `ENTITIES/TASK_MANAGERS/RESEARCHES/AI_Tutorials/Weekly_Searches/YYYY-MM-WXX_AI_Models_Deep_Research.json` (use existing template).  
- **Cross-links:**  
  - Tools → `LIBRARIES/LBS_003_.../Tools/*.json`  
  - Tasks → `TASK_MANAGERS/Task_Templates/*.json` (actionable workflows)  
  - Videos needing transcription → `RESEARCHES/01_QUEUE/Video_Queue_Tracker.md`
  - Lead-generation campaigns → `Sales Nov25/Lead_Gen_Strategy/*.md` or relevant department backlog

Ensure each session references this prompt ID (`PMT-097`) plus any queue IDs spawned from the findings.

---

## 8. Quality Guardrails

- Cite metrics (latency, cost per 1M tokens, context window) when mentioned.  
- Note when creators share downloadable assets (JSON, repos, transcripts) so Phase 1 teams can fast-track transcription.  
- Flag hype vs proof; if claims lack evidence, document the gap.  
- Capture at least one failure/limitation per model to inform risk assessments.  
- Verify links remain accessible (no private/unlisted videos).  
- Keep watchlist of recurring creators; update Influencer DB if new high-signal channels appear.

---

## 9. Next-Step Hooks

- **If >2 videos recommend the same workflow:** start a dedicated task template in `TASK_MANAGERS`.  
- **If comparisons show cost savings or performance gains:** alert Finance/AI Strategy for subscription decisions.  
- **If tutorials include UI/UX insights:** notify Design + Video teams (could trigger separate design-specific prompt).  
- **If any gap remains (e.g., missing designer-focused task-manager builds):** log it directly inside the Video Queue coverage gaps section.

---

*Prompt owner: AI Research Automation Pod (contact: taxonomy@remotehelpers). Keep changelog entries appended below upon future revisions.*  
**Changelog:** v1.0.0 (2025-11-22) – Initial release.




## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
