# Tool References - November 20, 2025

**Source:** Daily activity reports from all departments
**Total Tools Referenced:** 15 tools (5 new + 10 existing)
**Date:** 2025-11-21

---

## New Tools to Add

| TOL ID | Tool Name | Category | Departments Using | Usage Count | Description |
|--------|-----------|----------|-------------------|-------------|-------------|
| TOL-221 | Antigravity IDE | Development_Tools | AID, DGN, DEV, SLS | 3 | Google's AI-powered IDE alternative to VS Code with Gemini 3 Pro integration |
| TOL-222 | Google AI Studio | AI_Tools | VID | 1 | Google's AI platform for transcription and analysis |
| TOL-223 | Runway | Design_Tools | DGN | 1 | AI-powered animation and video generation tool |
| TOL-224 | Leonardo AI | AI_Image_Generation | DGN | 1 | AI image generation tool alternative to Midjourney |
| TOL-225 | ChatGPT-5 | AI_Tools | AID, DGN, DEV | 3 | OpenAI's latest language model for text generation and refinement |

---

## Existing Tools Referenced

| TOL ID | Tool Name | Category | Departments Using | Usage Count | Status |
|--------|-----------|----------|-------------------|-------------|--------|
| TOL-081 | Google Cloud Console | Cloud_Platforms | AID, DEV | 2 | EXISTING |
| TOL-045 | Google Sheets | Productivity | AID, FIN | 2 | EXISTING |
| TOL-156 | Midjourney | AI_Image_Generation | DGN | 2 | EXISTING |
| TOL-148 | Perplexity AI | AI_Tools | AID | 1 | EXISTING |
| TOL-092 | Discord | Communication | AID, LGN | 2 | EXISTING |
| TOL-058 | Notion | Productivity | HRM | 1 | EXISTING |
| TOL-119 | n8n | Automation | FIN | 1 | EXISTING |
| TOL-201 | Cursor | Development_Tools | AID | 1 | EXISTING |
| TOL-003 | Gemini 3 Pro | AI_Tools | AID, DGN | 2 | EXISTING |
| TOL-002 | Claude | AI_Tools | AID | 1 | EXISTING |

---

## Detailed Tool Information

### New Tools

#### TOL-221: Antigravity IDE
- **Category:** Development_Tools
- **URL:** https://antigravity.dev (assumed)
- **Pricing:** Free (open beta period)
- **Description:** Google's AI-powered IDE alternative to VS Code with integrated Gemini 3 Pro model access. Provides Claude extension availability and department account login compatibility.
- **Departments Using:** AID (primary), DGN, DEV, SLS
- **Usage Context:**
  - Installation and configuration for Design department (Activity 1 - AI Report)
  - IDE evaluation by Development department
  - Setup planning for Sales department
- **API Integration:** Gemini 3 Pro model API
- **Key Features:**
  - Gemini 3 Pro access (newest, most advanced model)
  - Claude extension support
  - Department account integration
  - VS Code/Cursor compatibility
- **Strategic Value:** High - Free access to Gemini 3 Pro during beta enables AI-powered development without additional costs

#### TOL-222: Google AI Studio
- **Category:** AI_Tools
- **URL:** https://aistudio.google.com
- **Pricing:** Free tier (100MB video limit)
- **Description:** Google's comprehensive AI platform for transcription, Gemini API access, and AI model experimentation
- **Departments Using:** VID (Video Production)
- **Usage Context:** Video transcription workflows
- **API Integration:** Gemini API for transcription
- **Key Features:**
  - High-accuracy transcription
  - Gemini model access
  - Free tier for small videos
- **Strategic Value:** Medium - Enables free transcription for video processing pipeline

#### TOL-223: Runway
- **Category:** Design_Tools / Video_Generation
- **URL:** https://runwayml.com
- **Pricing:** Subscription-based ($15-100/month)
- **Description:** AI-powered animation and video generation tool with advanced video creation capabilities
- **Departments Using:** DGN (Design)
- **Usage Context:** Animation instruction creation and course development
- **Key Features:**
  - AI video generation
  - Animation tools
  - Text-to-video
  - Image-to-video
- **Strategic Value:** Medium - Specialized tool for animation projects

#### TOL-224: Leonardo AI
- **Category:** AI_Image_Generation
- **URL:** https://leonardo.ai
- **Pricing:** Freemium (free tier + $10-50/month plans)
- **Description:** AI image generation tool providing an alternative to Midjourney with unique style options
- **Departments Using:** DGN (Design)
- **Usage Context:** Course visual materials creation, image generation
- **Key Features:**
  - AI image generation
  - Style presets
  - Fine-tuned models
  - Free tier available
- **Strategic Value:** Medium - Alternative to Midjourney for design work

#### TOL-225: ChatGPT-5
- **Category:** AI_Tools / LLM_Services
- **URL:** https://chat.openai.com
- **Pricing:** Subscription ($20/month Plus) + API usage-based
- **Description:** OpenAI's latest language model for text generation, character refinement, and complex reasoning tasks
- **Departments Using:** AID, DGN, DEV (Multi-department)
- **Usage Context:**
  - Character design refinement (Design Department)
  - Automation planning (AI Department)
  - Development assistance (Dev Department)
- **API Integration:** OpenAI API
- **Key Features:**
  - Advanced language understanding
  - Character refinement capabilities
  - Multi-modal support
  - API access
- **Strategic Value:** High - Cross-department utility for AI-assisted work

---

## Tool Usage Analysis

### By Category
- **AI_Tools:** 5 tools (3 new + 2 existing)
- **Development_Tools:** 2 tools (1 new + 1 existing)
- **Design_Tools:** 2 tools (1 new + 1 existing)
- **AI_Image_Generation:** 2 tools (1 new + 1 existing)
- **Cloud_Platforms:** 1 tool (existing)
- **Productivity:** 2 tools (existing)
- **Communication:** 1 tool (existing)
- **Automation:** 1 tool (existing)

### By Department
- **AID (AI):** 10 tools referenced
- **DGN (Design):** 8 tools referenced
- **DEV (Development):** 4 tools referenced
- **VID (Video):** 2 tools referenced
- **LGN (Lead Generation):** 1 tool referenced
- **HRM (HR):** 1 tool referenced
- **FIN (Finance):** 2 tools referenced
- **SLS (Sales):** 1 tool referenced

### By Usage Frequency
- **High (3 uses):** Antigravity IDE, ChatGPT-5
- **Medium (2 uses):** Google Cloud, Google Sheets, Midjourney, Gemini 3 Pro, Discord
- **Low (1 use):** Google AI Studio, Runway, Leonardo AI, Perplexity AI, Notion, n8n, Cursor, Claude

---

## Import Actions Required

### Create New Tool JSON Files
1. TOL-221_Antigravity_IDE.json
2. TOL-222_Google_AI_Studio.json
3. TOL-223_Runway.json
4. TOL-224_Leonardo_AI.json
5. TOL-225_ChatGPT_5.json

### Update Libraries_Master_List.csv
- Add 5 new entries with status "Active"
- Assign appropriate categories
- Document pricing and integration details

### Validation Checklist
- [ ] Verify tool names are unique (no duplicates)
- [ ] Confirm official URLs
- [ ] Validate pricing information from official sources
- [ ] Document API integration capabilities
- [ ] Assign appropriate categories
- [ ] Cross-reference with task templates (TST-072, etc.)

---

## Strategic Insights

**Free Tools Adopted:** 2/5 (Antigravity IDE beta, Google AI Studio free tier)
**Subscription Tools:** 3/5 (Runway, Leonardo AI freemium, ChatGPT-5)

**Cost Impact:**
- New subscriptions: ~$30-70/month (if all adopted)
- Free alternatives available: Antigravity (vs Cursor $20/mo), Google AI Studio (vs paid transcription)
- **Net cost optimization opportunity:** $10-30/month savings

**Cross-Department Tools:** 3/5 tools used by multiple departments
- Antigravity IDE: 4 departments
- ChatGPT-5: 3 departments
- Gemini 3 Pro: 2 departments

**ROI Potential:** High - Tools enable automation, faster design workflows, and free AI access during beta periods
