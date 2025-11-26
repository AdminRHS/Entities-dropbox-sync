# YouTube Video Tutorial Search Prompts - Consolidated Collection

**Version:** 1.0  
**Created:** 2025-11-20  
**Purpose:** Comprehensive collection of all YouTube video tutorial search prompts used across the organization  
**Last Updated:** 2025-11-20

---

## 📋 Table of Contents

1. [General Video Research Prompts](#general-video-research-prompts)
2. [Department-Specific Prompts](#department-specific-prompts)
   - [HR Tutorials](#hr-tutorials)
   - [AI Tools Daily Research](#ai-tools-daily-research)
   - [HR Automation](#hr-automation)
   - [Remote Helpers Strategic Research](#remote-helpers-strategic-research)
3. [Technical/Platform-Specific Prompts](#technicalplatform-specific-prompts)
   - [n8n, OpenAI, Google Automation](#n8n-openai-google-automation)
4. [Usage Instructions & Best Practices](#usage-instructions--best-practices)
5. [Quick Reference Guide](#quick-reference-guide)

---

## General Video Research Prompts

### Basic YouTube Video Search Template

**Purpose:** Generic template for finding YouTube tutorial videos  
**Time Frame:** Customizable (typically 7-60 days)  
**Target Platforms:** Perplexity AI, ChatGPT, Claude

```markdown
Find the latest YouTube videos (published in the last [X] days) providing step-by-step tutorials 
and guides on [TOPIC].

**Search Criteria:**
- Published: Last [X] days
- Length: 10-40 minutes preferred
- Quality Focus:
  - Practical tutorials with step-by-step workflows
  - Screen sharing/coding demonstrations
  - Real-world business use cases
  - NOT just hype/news/announcements

**Output Format:**
For each video, provide:
1. Video Title - Full title as published
2. Creator/Channel - Channel name
3. YouTube URL - Direct link
4. Published Date - Exact date (YYYY-MM-DD)
5. Duration - Video length (MM:SS)
6. Key Topics - 3-5 bullet points of main topics covered
7. Relevance Score (0-100 points)
8. Complexity Level - Beginner / Intermediate / Advanced
9. One-Sentence Value - Why this tutorial is valuable

Sort by: Relevance Score (highest first)
```

---

## Department-Specific Prompts

### HR Tutorials

**File Source:** `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-047_YouTube_AI_HR_Tutorials.md`  
**Purpose:** Systematic YouTube research to discover the latest tutorials and guides (last 2 months) focused on AI applications for HR departments  
**Version:** 1.0.0  
**Date:** 2025-01-14

#### Primary Research Prompt

```markdown
I need to find the latest YouTube videos (published in the last 60 days) providing step-by-step tutorials 
and guides on AI applications for HR departments, including automation, workflows, and best practices.

═══════════════════════════════════════════════════════════════════════════════

🔥 CRITICAL PRIORITY TOPICS:

1. AI PLATFORM + HR TUTORIAL COMBINATIONS

**Claude AI for HR:**
- "Claude AI HR tutorial"
- "Claude AI recruitment guide"
- "Claude AI candidate screening tutorial"
- "Claude Desktop HR workflows tutorial"
- "Claude AI job description tutorial"
- "Claude AI onboarding automation guide"
- "Claude MCP HR integration tutorial"

**ChatGPT for HR:**
- "ChatGPT HR tutorial 2025"
- "ChatGPT recruitment automation guide"
- "ChatGPT candidate assessment tutorial"
- "ChatGPT onboarding tutorial"
- "ChatGPT job posting generator tutorial"
- "ChatGPT HR chatbot tutorial"
- "ChatGPT employee training tutorial"

**Gemini AI for HR:**
- "Gemini AI HR tutorial"
- "Google Gemini recruitment guide"
- "Gemini AI employee data analysis tutorial"
- "Gemini HR automation tutorial"

**NotebookLM for HR:**
- "NotebookLM CV analysis tutorial"
- "NotebookLM candidate screening guide"
- "NotebookLM HR documentation tutorial"

**General AI + HR:**
- "AI HR tutorial 2025"
- "AI recruitment guide"
- "AI for HR department tutorial"
- "AI HR automation tutorial"
- "AI tools for HR tutorial"

2. HR PROCESS + AI TUTORIAL COMBINATIONS

**Recruitment & Sourcing:**
- "AI candidate sourcing tutorial"
- "AI CV screening tutorial"
- "AI resume parsing tutorial"
- "AI recruitment automation guide"
- "AI candidate matching tutorial"
- "AI job posting generator tutorial"
- "AI interview scheduling tutorial"

**Onboarding:**
- "AI onboarding automation tutorial"
- "AI employee onboarding guide"
- "AI onboarding workflow tutorial"
- "AI new hire automation tutorial"

**Employee Management:**
- "AI employee data management tutorial"
- "AI HR analytics tutorial"
- "AI performance review tutorial"
- "AI employee engagement tutorial"

**Compliance & Documentation:**
- "AI HR compliance tutorial"
- "AI GDPR HR tutorial"
- "AI HR documentation tutorial"
- "AI employee record management tutorial"

3. AUTOMATION PLATFORM + HR TUTORIAL COMBINATIONS

**n8n for HR:**
- "n8n HR automation tutorial"
- "n8n recruitment workflow tutorial"
- "n8n onboarding automation guide"
- "n8n HR integration tutorial"

**Make/Zapier for HR:**
- "Make.com HR automation tutorial"
- "Zapier HR workflow tutorial"
- "HR automation tutorial Make Zapier"

═══════════════════════════════════════════════════════════════════════════════

📋 SEARCH CRITERIA:

**Published:** Last 60 days (2 months)
**Length:** 10-40 minutes preferred
**Quality Focus:**
  - Practical tutorials with step-by-step workflows
  - Screen sharing/coding demonstrations
  - Real-world business use cases
  - HR-specific content (not generic AI tutorials)
  - English language or accurate subtitles
  - Good audio/video quality (readable screen text)
  - Credible creator (verified channels, known educators)

**Video Content Types to Prioritize:**
1. Complete Tutorial Series ⭐⭐⭐⭐⭐
2. Step-by-Step Walkthroughs ⭐⭐⭐⭐⭐
3. Workflow Demonstration Tutorials ⭐⭐⭐⭐
4. Tool-Specific HR Tutorials ⭐⭐⭐⭐
5. Integration Tutorials ⭐⭐⭐⭐
6. Best Practices & Strategy Guides ⭐⭐⭐
7. Case Study Tutorials ⭐⭐⭐
8. Quick Tips & Short Tutorials ⭐⭐⭐

═══════════════════════════════════════════════════════════════════════════════

📊 OUTPUT FORMAT:

For each tutorial video researched, document using this template:

### [Video Title]

**📺 Channel/Creator**: [Creator Name] ([Subscriber Count if relevant])
**📅 Published Date**: [YYYY-MM-DD]
**⏱️ Duration**: [MM:SS or HH:MM:SS]
**🔗 Link**: [Full YouTube URL]
**📂 Content Type**: [Complete Tutorial | Step-by-Step Guide | Workflow Demo | Tool Deep-Dive | Integration Tutorial | Best Practices | Case Study | Quick Tips]

#### **🎯 Tutorial Focus**
- **Primary Topic**: [Main topic covered]
- **Tutorial Level**: [Beginner | Intermediate | Advanced]
- **HR Process Category**: [Recruitment | Onboarding | Employee Management | Compliance | Analytics | Other]
- **Specific HR Task Addressed**: [HR-001, HR-004, WF-REC-001, etc. if applicable]

#### **🛠️ Tools/Platforms Featured**
- **Primary Tool**: [Main tool demonstrated]
- **Additional Tools**: [Other tools shown]
- **Our Current Stack Match**:
  - ✅ Tools we already use: [List]
  - 🆕 New tools introduced: [List]

#### **📌 Topics & Concepts Covered**
**Main Topics**:
1. [Topic 1 - be specific]
2. [Topic 2]
3. [Topic 3]

**Key Concepts Taught**:
- [Concept 1]
- [Concept 2]

**Techniques Demonstrated**:
- [Technique 1]
- [Technique 2]

#### **💡 Key Learnings & Takeaways**
**What You'll Learn**:
1. [Learning point 1]
2. [Learning point 2]

**Practical Applications**:
- [Application 1: How this applies to our HR processes]
- [Application 2: Specific use case for our team]

#### **⭐ Overall Value Rating**: [1-5 stars]
**Rating Reasoning**: [Why this rating]
**Recommended For**: [Specific use case, team type, or scenario]
```

#### Recommended YouTube Channels for HR Tutorials

- **HR-Specific AI Channels:**
  - AIHR (Analytics in HR)
  - HR Technology Conference
  - Recruiting Brainfood
  - Josh Bersin
  - HR Tech Weekly

- **AI Platform Official Channels:**
  - Anthropic (Claude official)
  - OpenAI (ChatGPT official)
  - Google Workspace
  - Notion (Official)

- **Automation Platform Channels:**
  - n8n (Official Channel)
  - Make (Official - formerly Integromat)
  - Zapier (Official)

---

### AI Tools Daily Research

**File Source:** `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-048_YouTube_AI_Tools_Daily.md`  
**Purpose:** Discover and document the latest AI tools, features, and workflows across multiple departments through systematic YouTube video research  
**Version:** 1.0.0  
**Date:** 2025-01-14

#### Primary Research Prompt

```markdown
I need to find the latest YouTube videos (published in the last 7-30 days) showcasing NEW AI tools 
and NEW features within existing AI platforms, focusing on practical workflows applicable across 
all company departments.

═══════════════════════════════════════════════════════════════════════════════

🎯 RESEARCH OBJECTIVE:

**MISSION**: Conduct daily YouTube research to identify NEW AI tools and NEW features within 
existing AI platforms, focusing on practical workflows applicable across all company departments.

**KEY GOALS**:
1. Discover emerging AI tools not yet in our ecosystem
2. Track new feature releases in established platforms
3. Identify department-specific workflows and use cases
4. Document integration strategies between tools
5. Stay ahead of the AI tools landscape

═══════════════════════════════════════════════════════════════════════════════

🔍 PRIMARY AI PLATFORMS TO MONITOR:

**🤖 Conversational AI:**
- "ChatGPT new features 2025"
- "Claude AI new updates"
- "Gemini AI capabilities"
- "Perplexity AI workflows"
- "Microsoft Copilot tutorials"
- "Anthropic Claude updates"

**🎨 Creative & Design AI:**
- "Midjourney new features"
- "DALL-E 3 workflows"
- "Stable Diffusion tutorials"
- "Adobe Firefly updates"
- "Canva AI features"
- "Runway ML new tools"
- "Leonardo AI tutorials"

**📹 Video & Audio AI:**
- "Sora AI video generation"
- "ElevenLabs new features"
- "Descript AI workflows"
- "Synthesia updates"
- "CapCut AI features"
- "Riverside.fm AI tools"

**📊 Productivity & Automation:**
- "Notion AI workflows"
- "Zapier AI automation"
- "Make.com AI integrations"
- "Airtable AI features"
- "Monday.com AI updates"

**🔧 Developer & Technical AI:**
- "GitHub Copilot new features"
- "Cursor AI tutorials"
- "Replit AI workflows"
- "V0 by Vercel demos"
- "Bolt.new tutorials"

**📈 AI & SEO AI:**
- "Jasper AI updates"
- "Copy.ai workflows"
- "Surfer SEO AI features"
- "Semrush AI tools"
- "HubSpot AI features"

═══════════════════════════════════════════════════════════════════════════════

📺 VIDEO CONTENT TYPES TO PRIORITIZE:

1. **Workflow Demonstrations** ⭐⭐⭐⭐⭐
   - Real-world examples showing complete start-to-finish processes
   - Screen recordings with commentary
   - Step-by-step walkthroughs
   - Before/after comparisons
   - Time-saving metrics

2. **Tutorial Guides** ⭐⭐⭐⭐
   - Actionable how-to content with clear instructions
   - Setup and configuration
   - Feature deep-dives
   - Best practices
   - Common mistakes to avoid

3. **Integration Strategies** ⭐⭐⭐⭐
   - Multi-tool workflows and automation chains
   - Tool-to-tool connections
   - API integrations
   - Zapier/Make.com workflows
   - Tech stack demonstrations

4. **New Feature Announcements** ⭐⭐⭐⭐
   - Official releases and early access previews
   - Platform update videos
   - Beta feature showcases
   - Release note walkthroughs
   - Official channel announcements

5. **Tool Comparisons & Reviews** ⭐⭐⭐
   - Side-by-side analysis and recommendations
   - Feature comparison matrices
   - Use case suitability
   - Pricing analysis
   - Alternatives and recommendations

═══════════════════════════════════════════════════════════════════════════════

📊 OUTPUT FORMAT:

For each video researched, document using this template:

### [Video Title]

**📺 Channel/Creator**: [Creator Name + Subscriber Count if relevant]
**📅 Published Date**: [YYYY-MM-DD]
**⏱️ Duration**: [MM:SS]
**🔗 Link**: [Full YouTube URL]
**📂 Category**: [Tutorial | Workflow Demo | Feature Announcement | Comparison | Use Case]

**🏢 Department Applicability**:
- [ ] AI
- [ ] Design
- [ ] Sales
- [ ] Lead Generation
- [ ] Customer Support
- [ ] HR
- [ ] Project Management
- [ ] Data Analysis
- [ ] Operations
- [ ] Universal (All Departments)

**🛠️ Tools/Platforms Featured**:
- Tool 1 (Primary focus)
- Tool 2 (Secondary/Integration)
- Tool 3 (Mentioned)

**📌 Main Topics Covered**:
1. Topic/feature 1
2. Topic/feature 2
3. Topic/feature 3

**💡 Key Takeaways**:
- Insight 1: [Actionable takeaway]
- Insight 2: [Specific technique or tip]
- Insight 3: [Important limitation or consideration]

**🆕 New Discovery?**:
- [ ] **NEW TOOL** - Not currently in our ecosystem
- [ ] **NEW FEATURE** - Update to existing tool we use
- [ ] Known tool/feature

**⚡ Implementation Difficulty**: [Easy | Medium | Hard]
**🎯 Priority Level**: [High | Medium | Low]
**👥 Best For**: [Specific team/role/use case]

**🔗 Integration Opportunities**:
[How this could connect with our existing tools/workflows]

**📋 Action Items**:
- [ ] Share with [Department/Team]
- [ ] Test tool/feature
- [ ] Create internal documentation
- [ ] Schedule training session
- [ ] Add to tools evaluation list
```

#### Recommended YouTube Channels for AI Tools

- **Multi-Department AI Tools:**
  - AI Foundations
  - Matt Wolfe
  - The AI Advantage
  - AI Andy
  - MattVidPro AI
  - Skill Leap AI
  - AI Tools Official
  - WorldofAI

- **AI & Content:**
  - HubSpot AI
  - Neil Patel
  - Ahrefs
  - Income Stream Surfers

- **Design & Creative:**
  - Flux Academy
  - The Futur
  - DesignCourse
  - CharliMarieTV

- **Business & Productivity:**
  - Keep Productive
  - Francesco D'Alessio
  - Notion
  - Thomas Frank

- **Developer & Technical:**
  - Fireship
  - Theo - t3.gg
  - Web Dev Simplified
  - GitHub

---

### HR Automation

**File Source:** `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-049_YouTube_HR_Automation.md`  
**Purpose:** Comprehensive YouTube research to discover AI automation opportunities for all HR work processes, workflows, and tasks  
**Version:** 1.0.0  
**Date:** 2025-01-14

#### Primary Research Prompt

```markdown
I need to find the latest YouTube videos (published in the last 7-30 days) showcasing AI-powered 
automation solutions for HR processes, including tools, workflows, and integrations that can 
reduce manual work and increase efficiency for small HR teams.

═══════════════════════════════════════════════════════════════════════════════

🎯 RESEARCH MISSION:

**PRIMARY OBJECTIVE**: Discover and document AI-powered automation solutions for HR processes 
by systematically researching YouTube videos showcasing tools, workflows, and integrations that 
can reduce manual work and increase efficiency.

**FOCUS AREAS**:
1. 🔍 Find NEW automation tools not yet in our HR tech stack
2. ✨ Discover NEW features in existing tools (n8n, Make, Zapier, Claude, ChatGPT, Notion)
3. 🔗 Identify integration opportunities between current tools
4. ⚡ Learn workflow automations for repetitive HR tasks
5. 📊 Understand implementation for small teams (2 people)
6. 🌍 Ensure EU/GDPR compliance for Austria/Ukraine operations
7. 📈 Measure time savings and ROI potential

═══════════════════════════════════════════════════════════════════════════════

🔍 PRIMARY SEARCH QUERIES:

**🤖 AI Platform + HR Process Combinations:**

**Claude AI for HR:**
- "Claude AI recruitment automation"
- "Claude AI candidate screening"
- "Claude AI job description generator"
- "Claude Desktop HR workflows"
- "Claude MCP connectors HR"
- "Claude API HR automation"

**ChatGPT for HR:**
- "ChatGPT HR automation workflows"
- "ChatGPT candidate assessment"
- "ChatGPT onboarding automation"
- "ChatGPT job posting generator"
- "ChatGPT HR chatbot"
- "ChatGPT employee training"

**⚙️ Automation Platform + HR Workflows:**

**n8n (Primary Platform):**
- "n8n HR automation workflows 2025"
- "n8n recruitment automation"
- "n8n onboarding workflow"
- "n8n Instagram to CRM automation"
- "n8n Gmail calendar interview scheduling"
- "n8n employee onboarding checklist"
- "n8n ATS integration"
- "n8n job posting automation"
- "n8n candidate tracking workflow"
- "n8n Telegram bot HR"

**Make (Integromat):**
- "Make.com HR automation"
- "Make recruitment workflows"
- "Make onboarding automation"
- "Make Instagram recruitment"
- "Make ATS integration"

**Zapier:**
- "Zapier HR automation 2025"
- "Zapier recruitment workflows"
- "Zapier job posting automation"
- "Zapier onboarding checklist"
- "Zapier candidate tracking"

**🎯 HR Process-Specific Searches:**

**Recruitment & Sourcing:**
- "AI candidate sourcing automation 2025"
- "automated candidate screening tools"
- "CV parsing automation AI"
- "resume screening AI tools"
- "candidate matching AI"
- "recruitment chatbot automation"
- "automated job posting distribution"
- "multi-platform job posting automation"
- "applicant tracking system automation"
- "candidate pipeline automation"

**Interview Management:**
- "automated interview scheduling"
- "AI interview scheduling tools"
- "calendar automation for interviews"
- "video interview automation"
- "interview reminder automation"
- "interview feedback automation"
- "AI interview question generator"

**Onboarding:**
- "employee onboarding automation 2025"
- "automated onboarding checklist"
- "new hire automation workflows"
- "onboarding task automation"
- "employee account provisioning automation"
- "automated welcome email sequences"
- "onboarding document automation"
- "training automation new employees"

**Employee Data Management:**
- "employee database automation"
- "HRIS automation workflows"
- "employee data sync automation"
- "employee folder structure automation"
- "employee status tracking automation"
- "HR data quality automation"

═══════════════════════════════════════════════════════════════════════════════

📺 VIDEO CONTENT PRIORITIZATION:

1. **Workflow Demonstrations** ⭐⭐⭐⭐⭐
   - Real screen recordings showing complete automation workflows
   - Full end-to-end process
   - Before/after time comparisons
   - Actual tool configurations
   - Error handling and troubleshooting
   - Integration setup process

2. **Tool Integration Tutorials** ⭐⭐⭐⭐⭐
   - Step-by-step guides connecting multiple tools
   - API setup, authentication, data mapping
   - Configuration screenshots
   - Code snippets or workflow exports
   - Testing and validation steps

3. **HR Process Automation Case Studies** ⭐⭐⭐⭐
   - Real companies showing their automation implementations
   - Time savings, metrics, ROI
   - Team size context (small teams preferred)
   - Before/after processes
   - Actual time/cost savings data

4. **New Tool Announcements & Features** ⭐⭐⭐⭐
   - Official releases, beta previews, update walkthroughs
   - Feature demonstrations, not just announcements
   - Release notes walkthroughs
   - Migration guides from old methods
   - Pricing and access details

═══════════════════════════════════════════════════════════════════════════════

📊 OUTPUT FORMAT:

For each video researched, document using this comprehensive template:

### [Video Title]

**📺 Channel/Creator**: [Creator Name] ([Subscriber Count if relevant])
**📅 Published Date**: [YYYY-MM-DD]
**⏱️ Duration**: [MM:SS]
**🔗 Link**: [Full YouTube URL]
**📂 Content Type**: [Workflow Demo | Integration Tutorial | Feature Announcement | Case Study | Tool Comparison | Template Showcase]

#### **🏢 HR Process Categories** (Check all that apply)
- [ ] Recruitment & Talent Acquisition
- [ ] Candidate Screening & Interview Management
- [ ] Onboarding & Employee Integration
- [ ] Employee Training & Development
- [ ] Performance Management & Reviews
- [ ] Payroll, Benefits & Compensation
- [ ] Employee Engagement & Retention
- [ ] HR Data Management & Compliance
- [ ] Offboarding & Exit Management
- [ ] HR Analytics & Strategic Planning

#### **🎯 Specific HR Tasks Addressed** (Reference our task IDs if applicable)
- [ ] HR-001: Onboard New Developer
- [ ] HR-003: Implement HR Tool-Calling Automation
- [ ] HR-004: Create Employee Folder Structure
- [ ] HR-005: Review Employee Status Accuracy
- [ ] HR-006: Publish Job Opening
- [ ] WF-REC-001: Communicate with Remote Candidates via Instagram DMs
- [ ] WF-REC-002: Screen Candidates via Instagram DMs
- [ ] TASK-TEMPLATE-001: Create Job Posting
- [ ] Other: [Specify]

#### **🛠️ Tools/Platforms Featured**
**Primary Tool**: [Main tool demonstrated]
**Integration Tools**: [Additional tools shown]
**Our Current Stack Match**:
- ✅ Tools we already use: [List]
- 🆕 New tools to evaluate: [List]

#### **💡 Key Takeaways & Actionable Insights**
**Workflow/Process Shown**:
[Describe the specific workflow demonstrated]

**Implementation Steps**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Time Savings Demonstrated**:
- **Before**: [X hours/minutes]
- **After**: [Y hours/minutes]
- **Savings**: [% or time saved]

**Cost Information**:
- **Free Tier**: [What's included]
- **Paid Tier**: [Pricing mentioned]
- **Total Cost**: [Estimated monthly cost for our team size]

#### **🆕 Discovery Type**
- [ ] **NEW TOOL** - Not currently in our HR tech stack
- [ ] **NEW FEATURE** - Update/capability in existing tool
- [ ] **NEW WORKFLOW** - Novel process/integration approach
- [ ] **NEW TEMPLATE** - Pre-built workflow or template
- [ ] **KNOWN TOOL/PROCESS** - Reinforces existing knowledge

#### **⚡ Implementation Assessment for Our Team**
**Implementation Difficulty**: [Easy | Medium | Hard]
**Time to Implement**: [Estimate: X hours/days]
**Team Capacity Required**: [1 person / 2 people / external help]

#### **🌍 EU/GDPR Compliance**
- [ ] **GDPR Compliant** - Explicitly mentioned
- [ ] **EU-Compatible** - Likely compliant but not stated
- [ ] **Unknown** - Compliance not discussed
- [ ] **US-Only** - Not suitable for EU operations

#### **📊 ROI Potential**
**Time Savings Estimate**:
- **Current Process Time**: [X hours per week/month]
- **Automated Process Time**: [Y hours per week/month]
- **Time Saved**: [Z hours = % reduction]

**Priority Level**: [🔴 High | 🟡 Medium | 🟢 Low]

#### **⭐ Overall Value Rating**: [1-5 stars]
**Rating Reasoning**: [Why this rating]
**Best For**: [Specific use case, team type, or scenario this is most valuable for]
```

---

### Remote Helpers Strategic Research

**File Source:** `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-050_YouTube_Remote_Helpers.md`  
**Purpose:** AI-powered video content discovery aligned with Remote Helpers' November 2025 strategic initiatives  
**Version:** 1.0  
**Created:** November 15, 2025

#### Primary Research Prompt

```markdown
I need to find the latest YouTube videos (published in the last 30-60 days) directly relevant
to Remote Helpers - an AI-first remote services company (32 employees, 7 departments) currently
undergoing major AI transformation initiatives.

═══════════════════════════════════════════════════════════════════════════════

🔥 CRITICAL PRIORITY TOPICS (November 2025 Strategic Initiatives):

1. FILE SYSTEM & WORKFLOW AUTOMATION
   - Meeting transcription workflows (Whisper, Claude, automated task generation)
   - AI-assisted daily workflows reducing administrative overhead by 60-80%
   - VS Code / Cursor IDE automation and extensions
   - Claude Code integration and Claude Desktop applications
   - Automated plan & task generation from transcripts

2. NATURAL LANGUAGE AUTOMATION
   - Opal AI MiniApps (write automation in natural language vs complex workflow builders)
   - Replacing traditional n8n/Make workflows with conversational automation
   - No-code automation tools with AI interfaces

3. OPEN-SOURCE VIDEO GENERATION
   - WAN 2.2 video model (lighting, camera angles, scene composition controls)
   - Runway Gen-3 updates and tutorials
   - AI video generation for marketing and client content
   - Synthesia, HeyGen, Hedra latest features

4. REAL-TIME ANALYTICS & DASHBOARD TRANSFORMATION
   - Shifting from monthly to daily/weekly analytics
   - AI-powered analytics platforms (like Tendency)
   - Data visualization and automated reporting
   - Performance tracking dashboards

5. LEAD GENERATION STRATEGY & OPTIMIZATION
   - Modern lead generation strategies (2025 best practices)
   - AI-powered prospecting and qualification
   - Appointment scheduling optimization
   - Lead conversion analytics and tracking
   - Alternative to data entry-focused LG workflows

═══════════════════════════════════════════════════════════════════════════════

📊 HIGH-PRIORITY TOPICS:

6. AI AGENTS & AGENTIC WORKFLOWS
   - Claude with MCP (Model Context Protocol) integrations
   - Browser automation agents (Perplexity Comet style)
   - Multi-step AI workflows and tool chaining
   - RAG (Retrieval Augmented Generation) systems
   - AI agent frameworks and orchestration

7. DISCORD SERVER AUTOMATION
   - Discord bot development (ProBot, CarlBot alternatives)
   - Advanced logging (voice events, member tracking, server analytics)
   - Discord workflow automation
   - Integration with AI tools

8. PROJECT MANAGEMENT & DOCUMENTATION
   - AI-assisted PM methodologies
   - Automated documentation generation
   - Knowledge base management (like RAC - Remote AI Context)
   - Template-driven operations
   - AI prompt compression techniques

9. BUSINESS PROCESS AUTOMATION
   - CRM automation and workflow optimization
   - Email automation beyond basic campaigns
   - Client onboarding automation
   - Cross-department workflow coordination

10. AI DEVELOPMENT TOOLS & CODING ASSISTANTS
    - Cursor IDE advanced tutorials
    - Windsurf AI coding features
    - Claude Desktop for development
    - AI code generation best practices
    - GitHub integration workflows

═══════════════════════════════════════════════════════════════════════════════

🛠️ TOOLS WE ACTIVELY USE (prioritize these):

**AI & LLMs:**
- Claude (Anthropic), ChatGPT (GPT-4o), Perplexity AI, Gemini, Grok, Minimax
- NotebookLM, Genspark

**Development:**
- Cursor (primary IDE), VS Code, Windsurf, Claude Desktop
- Replit, Google AI Studio, Smithery
- Lovable, v0 (Vercel), DeepSite, Bubble, Runner, OA-Y

**Video Production:**
- Runway (Gen-3), HeyGen, Synthesia, Hedra, Loom
- Maestra (transcription), WAN 2.2 (new focus)

**Design:**
- Leonardo.ai, Midjourney, Gamma (presentations), Manus

**Automation:**
- N8n (current), Make, Zapier
- Opal AI MiniApps (NEW - critical interest)

**Business & Analytics:**
- CRM systems, Discord (ProBot, CarlBot)
- Tendency analytics, Cove AI (sales intelligence)

**Data & Lead Generation:**
- Bright Data, Hunter.io, Instantly.ai, Apollo.io

═══════════════════════════════════════════════════════════════════════════════

👥 PREFERRED CREATORS/CHANNELS:
- Matthew Berman (AI news, model benchmarks)
- Cole (agentic engineering, tech stacks)
- Matt Wolfe (AI tool demos, practical applications)
- Nick Saraev / Leftclick (lead generation at scale)
- Darren Wiener (Claude Code, business automation)
- D-Squared (Claude integrations, no-code)
- Liam Otley (AI automation)
- AI Jason (AI workflows)
- WorldofAI (AI news and tools)

═══════════════════════════════════════════════════════════════════════════════

🎯 SPECIFIC USE CASES TO SEARCH FOR:

- "AI meeting transcription automation workflow 2025"
- "Opal AI MiniApps tutorial"
- "Claude Code business applications"
- "WAN 2.2 video generation tutorial"
- "Cursor IDE automation techniques"
- "Daily analytics dashboard automation"
- "Lead generation strategy 2025 AI powered"
- "Discord bot automation advanced logging"
- "MCP Claude integration tutorial"
- "Natural language workflow automation"
- "AI project management documentation"
- "Real-time sales analytics with AI"
- "Browser automation AI agents"
- "Whisper transcription workflow automation"

═══════════════════════════════════════════════════════════════════════════════

📋 SEARCH CRITERIA:

**Published:** Last 30-60 days (October 15 - December 15, 2025)
**Length:** 10-40 minutes preferred (sweet spot: 15-25 minutes)
**Quality Focus:**
  - Practical tutorials with step-by-step workflows
  - Tool demos with real business applications
  - Case studies with measurable ROI/results
  - NOT just hype/news/announcements

**Technical Depth:**
  - Actionable implementation steps
  - Code examples or workflow screenshots
  - Integration patterns and architecture
  - Real-world use cases

═══════════════════════════════════════════════════════════════════════════════

📊 OUTPUT FORMAT:

For each video (8-12 recommendations), provide:

1. **Video Title** - Full title as published
2. **Creator/Channel** - Channel name
3. **YouTube URL** - Direct link
4. **Published Date** - Exact date (YYYY-MM-DD)
5. **Duration** - Video length (MM:SS)
6. **Key Topics** - 3-5 bullet points of main topics covered
7. **Remote Helpers Relevance Score** (0-100 points):
   - Strategic Alignment (0-40 pts): Matches Nov 2025 initiatives
   - Tool/Tech Relevance (0-30 pts): Uses our tech stack
   - Actionable Value (0-30 pts): Practical implementation steps
8. **Department Relevance** - Which RH departments benefit (AI, Dev, Video, LG, Design, Sales, HR)
9. **Implementation Priority** - Critical/High/Medium/Low
10. **One-Sentence Value** - Why we should watch this

**Sort by:** Relevance Score (highest first)

═══════════════════════════════════════════════════════════════════════════════

💡 CONTEXT FOR BETTER RESULTS:

**Current Challenges We're Solving:**
- Transitioning LG department from data entry to strategic value
- Rolling out file system workflow to all 32 employees
- Moving analytics from monthly to daily/weekly tracking
- Evaluating natural language automation (Opal) vs traditional workflows
- Scaling meeting documentation with AI transcription

**Decision Points:**
- Should we adopt Opal AI MiniApps to replace n8n workflows?
- How to optimize WAN 2.2 for client video production?
- Best practices for daily analytics dashboards with AI
- Modern lead generation strategies beyond data scraping

**Success Metrics:**
- 60-80% administrative overhead reduction
- Daily/weekly analytics instead of monthly
- Increased appointment conversion rates (LG)
- Faster video production cycles

═══════════════════════════════════════════════════════════════════════════════

🚀 BONUS POINTS FOR:
- Videos featuring multiple tools from our stack in integrated workflows
- Real ROI data or performance metrics
- Open-source alternatives to paid tools
- Case studies from similar-sized remote companies
- Comparisons between competing tools (e.g., Opal vs n8n, WAN 2.2 vs Runway)
```

#### Ultra-Concise Version

```markdown
Find latest YouTube videos (last 30-60 days, 10-40 min) about:

🔥 CRITICAL:
- AI meeting transcription automation (Whisper → Claude → tasks)
- Opal AI MiniApps (natural language automation)
- WAN 2.2 video generation tutorials
- Cursor/Windsurf IDE automation
- Daily analytics dashboard automation
- Modern lead generation strategies 2025

⭐ HIGH PRIORITY:
- Claude MCP integrations
- Discord bot advanced automation
- Browser automation agents
- AI project management workflows
- Real-time sales analytics

Creators: Matthew Berman, Cole, Matt Wolfe, Nick Saraev, Darren Wiener, D-Squared

Format per video:
- Title, URL, Date, Length
- Key topics (3-5 bullets)
- Relevance Score (0-100): Strategic (40) + Tech (30) + Actionable (30)
- Department relevance, Priority, One-sentence value

Sort by relevance score.
```

---

## Technical/Platform-Specific Prompts

### n8n, OpenAI, Google Automation

**File Source:** `ENTITIES/PROMPTS/Video_Processing/Research/Video_Search_Prompt_n8n_OpenAI_Google.md`  
**Version:** 1.0  
**Created:** November 21, 2025  
**Purpose:** AI-powered video content discovery for n8n, OpenAI, and Google Automation workflows

#### Primary Research Prompt

```markdown
I need to find the latest YouTube videos (published in the last 30-60 days) providing step-by-step tutorials 
and guides on n8n automation, OpenAI platform, and Google automation solutions.

═══════════════════════════════════════════════════════════════════════════════

🔥 CRITICAL PRIORITY TOPICS:

1. n8n AUTOMATION
   - AI Agents in n8n (LangChain nodes, memory, tools)
   - Advanced workflow patterns (error handling, sub-workflows, loops)
   - Custom node development
   - Integration with vector databases (Pinecone, Qdrant, Supabase)
   - "Human in the loop" workflows

2. OPENAI PLATFORM
   - Assistants API v2 implementation guides
   - Fine-tuning models (GPT-4o, GPT-4o-mini) for specific tasks
   - Realtime API (Voice/Audio) tutorials
   - Structured Outputs and JSON mode best practices
   - Vision API advanced use cases

3. GOOGLE AUTOMATION
   - Google Apps Script for Workspace automation (Sheets, Docs, Gmail)
   - AppSheet AI integration
   - Gemini for Google Workspace workflows
   - Vertex AI Agent Builder tutorials
   - Google Cloud Functions for automation

═══════════════════════════════════════════════════════════════════════════════

🛠️ TOOLS FOCUS:

**Core Platform:**
- n8n (Self-hosted or Cloud)

**AI Models & APIs:**
- OpenAI (GPT-4o, Assistants API, Realtime API)
- Google Gemini (Pro/Flash, Vertex AI)

**Google Ecosystem:**
- Google Sheets, Docs, Gmail, Drive
- Google Apps Script
- Google Cloud Platform (Vertex AI, Cloud Functions)

═══════════════════════════════════════════════════════════════════════════════

🎯 SPECIFIC USE CASES TO SEARCH FOR:

- "n8n AI agent tutorial 2025"
- "OpenAI Assistants API v2 n8n workflow"
- "Google Apps Script automation with Gemini"
- "Build AI chatbot with n8n and OpenAI"
- "Automate Google Sheets with n8n and AI"
- "n8n LangChain tutorial"
- "OpenAI Realtime API n8n integration"
- "Vertex AI Agent Builder guide"
- "n8n custom node development tutorial"
- "Advanced n8n error handling patterns"

═══════════════════════════════════════════════════════════════════════════════

📋 SEARCH CRITERIA:

**Published:** Last 30-60 days
**Length:** 10-40 minutes preferred (sweet spot: 15-25 minutes)
**Quality Focus:**
  - Practical tutorials with step-by-step workflows
  - Screen sharing/coding demonstrations
  - Real-world business use cases
  - NOT just hype/news/announcements

**Technical Depth:**
  - Actionable implementation steps
  - JSON workflow exports or code repositories provided
  - Clear explanation of logic and architecture

═══════════════════════════════════════════════════════════════════════════════

📊 OUTPUT FORMAT:

For each video (8-12 recommendations), provide:

1. **Video Title** - Full title as published
2. **Creator/Channel** - Channel name
3. **YouTube URL** - Direct link
4. **Published Date** - Exact date (YYYY-MM-DD)
5. **Duration** - Video length (MM:SS)
6. **Key Topics** - 3-5 bullet points of main topics covered
7. **Relevance Score** (0-100 points):
   - Topic Alignment (0-40 pts): Matches n8n/OpenAI/Google focus
   - Technical Depth (0-30 pts): Step-by-step vs high level
   - Actionability (0-30 pts): Can be implemented immediately
8. **Primary Tech Stack** - n8n / OpenAI / Google / Hybrid
9. **Complexity Level** - Beginner / Intermediate / Advanced
10. **One-Sentence Value** - Why this specific tutorial is valuable

**Sort by:** Relevance Score (highest first)

═══════════════════════════════════════════════════════════════════════════════

🚀 BONUS POINTS FOR:
- Videos providing downloadable n8n workflow JSONs
- GitHub repositories with code examples
- Complex integrations combining all three (n8n + OpenAI + Google)
- Real-world production use cases (not just "Hello World")
```

#### Ultra-Concise Version

```markdown
Find latest YouTube videos (last 30-60 days, 10-40 min) about:

🔥 TOPICS:
- n8n AI Agents & LangChain nodes
- OpenAI Assistants API v2 & Realtime API
- Google Apps Script & Gemini automation
- Advanced n8n workflows (loops, error handling)

Format per video:
- Title, URL, Date, Length
- Key topics (3-5 bullets)
- Relevance Score (0-100)
- Tech Stack, Complexity, One-sentence value

Sort by relevance score.
```

---

## Usage Instructions & Best Practices

### Method 1: Perplexity AI (Recommended)

1. Go to [Perplexity.ai](https://www.perplexity.ai/)
2. Copy the appropriate **Primary Research Prompt** from above
3. Paste into Perplexity search
4. Review results and extract top videos
5. Score using the relevance system provided

### Method 2: ChatGPT / Claude

1. Open ChatGPT or Claude
2. Copy the **Primary Research Prompt**
3. Paste and submit
4. Request web search if needed
5. Review and validate results

### Method 3: Manual YouTube Search

1. Use the **Specific Use Cases** search queries directly in YouTube
2. Filter by: Upload date (Last month), Duration (10-40 minutes)
3. Check preferred creators' channels first
4. Score videos manually using the relevance system

### Best Practices

**DO:**
- ✅ Focus on practical, actionable content
- ✅ Prioritize workflow demonstrations over theory
- ✅ Document new tools immediately
- ✅ Share discoveries quickly with relevant teams
- ✅ Track trends across multiple videos
- ✅ Test before recommending widely
- ✅ Consider cost and implementation complexity
- ✅ Look for integration opportunities

**DON'T:**
- ❌ Waste time on superficial "top 10 AI tools" lists
- ❌ Ignore pricing and access requirements
- ❌ Recommend tools without department context
- ❌ Overlook privacy and security considerations
- ❌ Duplicate research already completed
- ❌ Skip documentation for "quick finds"
- ❌ Share unverified or untested tools
- ❌ Ignore team feedback on previous recommendations

---

## Quick Reference Guide

### Which Prompt to Use When?

| **Use Case** | **Recommended Prompt** | **Time Frame** |
|--------------|------------------------|----------------|
| General AI tool discovery | AI Tools Daily Research | Last 7-30 days |
| HR-specific tutorials | HR Tutorials | Last 60 days |
| HR automation workflows | HR Automation | Last 7-30 days |
| Company strategic initiatives | Remote Helpers Strategic | Last 30-60 days |
| n8n/OpenAI/Google focus | n8n OpenAI Google Automation | Last 30-60 days |
| Quick search | Ultra-Concise versions | Last 30-60 days |

### Scoring Systems Summary

**HR Tutorials:**
- Educational Value: High/Medium/Low
- Production Quality: High/Medium/Low
- Overall Value Rating: 1-5 stars

**AI Tools Daily:**
- New Discovery: NEW TOOL / NEW FEATURE / Known
- Implementation Difficulty: Easy/Medium/Hard
- Priority Level: High/Medium/Low

**HR Automation:**
- Relevance Score: 0-100 (Topic 40 + Tech 30 + Actionable 30)
- Implementation Difficulty: Easy/Medium/Hard
- ROI Potential: Time savings estimate

**Remote Helpers:**
- Relevance Score: 0-100 (Strategic 40 + Tech 30 + Actionable 30)
- Implementation Priority: Critical/High/Medium/Low
- Department Relevance: AI/Dev/Video/LG/Design/Sales/HR

**n8n/OpenAI/Google:**
- Relevance Score: 0-100 (Topic 40 + Technical 30 + Actionable 30)
- Complexity Level: Beginner/Intermediate/Advanced
- Primary Tech Stack: n8n/OpenAI/Google/Hybrid

---

## File Sources Reference

This consolidated document combines content from:

1. `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-047_YouTube_AI_HR_Tutorials.md`
2. `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-048_YouTube_AI_Tools_Daily.md`
3. `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-049_YouTube_HR_Automation.md`
4. `ENTITIES/PROMPTS/RESEARCH/Research_Prompts/PMT-050_YouTube_Remote_Helpers.md`
5. `ENTITIES/PROMPTS/Video_Processing/Research/Video_Search_Prompt_n8n_OpenAI_Google.md`
6. `ENTITIES/PROMPTS/VIDEO_RESEARCHES_Prompt_Examples.md`

---

## Maintenance & Updates

**Review Frequency:** Monthly  
**Update Triggers:**
- New AI platforms gaining traction
- Departments request specific focus areas
- Search queries becoming less effective
- New video content types emerging
- Team feedback indicates gaps in coverage

**Version History:**
- **v1.0** (2025-11-20): Initial consolidation of all YouTube video tutorial search prompts

---

**Last Updated:** 2025-11-20  
**Maintained By:** AI Department  
**Contact:** For questions or updates to these prompts

