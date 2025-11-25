# 01_Library_Integration - Department-Based LIBRARIES Integration

**Purpose:** Department-focused integration guides for 12 LIBRARIES entities, optimized for selective loading and reduced prompt weight.

**Files in this folder:** 10 (7 department files + common + parameters + framework)
**Update Frequency:** When LIBRARIES are updated
**Architecture:** Department-based grouping for 40-70% prompt weight reduction

---

## Overview

This folder contains department-focused library integration files instead of individual library files. This approach:

- **Reduces prompt weight** by 40-70% through selective loading
- **Aligns with org structure** - 7 departments at Remote Helpers
- **Enables targeted processing** - Load only relevant libraries per meeting
- **Maintains completeness** - Full library coverage across all files
- **Supports cross-functional** - Can load multiple department files

### Design Philosophy

Instead of loading all 12 libraries (8,000-12,000 lines) for every meeting, we load:
- **Common Libraries** (always) - ~800 lines
- **Department-Specific** (as needed) - ~400-1,500 lines per department
- **Parameters Summary** (lightweight) - ~300-500 lines

**Result:** Typical meeting analysis uses 1,400-2,300 lines instead of 8,000-12,000 lines.

---

## File Structure

### 00_Common_Libraries.md (Always Loaded)
**Size:** 500-800 lines
**Contains:**
- Professions Library (27 professions) - Condensed reference
- Prompts Library - Core system prompts
- Results Library - High-level overview
- Responsibilities Formula (Action + Object = Responsibility)

**Why Common:**
- Every department needs profession/role context
- Results apply cross-functionally
- Prompts are system-level

**Loading:** ALWAYS included in all assemblies

---

### 01_HR_Libraries.md
**Size:** 400-600 lines
**Department:** HR (2 employees - Rekonvald Viktoriia, Nealova Evgeniya)

**Libraries Integrated:**
1. **Professions** (FULL) - 27 professions with details (recruitment focus)
2. **Skills** (subset) - Recruitment, evaluation, candidate assessment skills
3. **Responsibilities** (subset) - HR-related responsibilities
4. **Actions** (subset) - Recruitment actions (interview, evaluate, onboard, hire)
5. **Processes** (subset) - Recruitment workflows, candidate pipelines
6. **Parameters** (recruiter_parameters.json - 87 params)

**Recognition Patterns:**
- Hiring, recruiting, candidates, talent acquisition
- Employee management, onboarding, interviews
- Job descriptions, candidate evaluation
- Recruitment platforms (LinkedIn, job boards)

**Use Cases:**
- HR team meetings about recruitment
- Candidate pipeline discussions
- Employee onboarding planning

---

### 02_AI_Libraries.md
**Size:** 1,000-1,500 lines (Largest - AI team needs comprehensive tool knowledge)
**Department:** AI (3 employees - Zasiadko Matvii, Artemchuk Nikolay, Perederii Vladislav)

**Libraries Integrated:**
1. **Tools** (FULL - 75+ tools) - CRITICAL for AI department
   - 21 AI tools (Claude, ChatGPT, Cursor, Windsurf, etc.)
   - 18 Dev tools (GitHub, Docker, VS Code, etc.)
   - 7 Database tools
   - 3 Cloud platforms
   - Automation tools, MCP connectors
2. **Skills** (AI_Skills.json - full)
3. **Actions** (Data_Operations FULL + AI-related actions)
   - 12 Data_Operations files (scraping, parsing, sanitizing, etc.)
4. **Processes** (AI_Automation_Workflows.json + related)
5. **Objects** (Agentic objects, AI-related objects)
6. **Professions** (AI engineer, automation engineer, prompt engineer)
7. **Parameters** (project_manager_parameters.json - 56 params)

**Recognition Patterns:**
- AI tools (Claude Desktop, Cursor, ChatGPT, Midjourney, etc.)
- Automation, MCP connectors, prompts, workflows
- Scraping, parsing, data processing, API integration
- GitHub, Docker, cloud platforms

**Use Cases:**
- AI team technical discussions
- Automation project planning
- Tool selection and evaluation
- Prompt engineering sessions

---

### 03_Video_Libraries.md
**Size:** 600-800 lines
**Department:** Video (3 employees - Panchenko Diana, Podolskyi Sviatoslav, Azanova Darya)

**Libraries Integrated:**
1. **Actions** (Video_Generation_Actions.json - specialized file)
2. **Objects** (Video_Generation_Objects.json - specialized file)
3. **Tools** (subset) - Video-specific tools
   - HeyGen, Runway, Synthesia, Kling, Sora, Luma AI
   - Adobe Premiere Pro, After Effects, DaVinci Resolve
   - YouTube, Vimeo, TikTok platforms
4. **Processes** (subset) - Video production workflows
5. **Results** (subset) - Video deliverables and outcomes
6. **Skills** (Video editing, motion design, animation)
7. **Professions** (Video editor, animator, motion designer)

**Recognition Patterns:**
- Video editing, rendering, animation, motion graphics
- Video tools and platforms
- Video deliverables (explainer videos, reels, shorts)
- Effects, transitions, color grading

**Use Cases:**
- Video project planning
- Client video requirements
- Video production workflows
- Platform upload discussions (YouTube, TikTok)

---

### 04_Sales_Libraries.md
**Size:** 700-900 lines
**Department:** Sales (1 employee - Kovalska Anastasiya)

**Libraries Integrated:**
1. **Services** (FULL - 7 categories)
   - Content, Design, LG, AI, SEO, Technical, Video
2. **Products** (FULL - 39 products)
3. **Processes** (subset) - Sales workflows, client management, pipeline
4. **Actions** (subset) - Client communication, presentations, demos, proposals
5. **Parameters** (sales_manager_parameters.json - 95 params)
6. **Professions** (Sales manager, SDR, account executive, customer success)
7. **Tools** (subset) - CRM tools (Apollo.io, Instantly.ai, LinkedIn Sales Navigator)

**Recognition Patterns:**
- Services, products, offerings, pricing
- Sales pipeline, deals, proposals, contracts
- Client communication, demos, presentations
- CRM platforms, outreach tools

**Use Cases:**
- Sales strategy meetings
- Client requirement discussions
- Service/product positioning
- Pricing and proposal planning

---

### 05_Design_Libraries.md
**Size:** 800-1,000 lines
**Department:** Design (9 employees - largest department)

**Libraries Integrated:**
1. **Objects** (Design_Deliverables.json - specialized file)
   - UI/UX deliverables, design system components
2. **Actions** (subset) - Design creation actions
3. **Processes** (Design_System_Workflows.json + related)
4. **Tools** (subset) - Design-specific tools
   - Figma, Adobe Creative Suite (Illustrator, Photoshop, XD)
   - Design AI tools (Midjourney, Leonardo, Stable Diffusion)
   - Portfolio platforms (Dribbble, Behance, ArtStation)
5. **Skills** (SKL-DESIGN-001, SKL-DESIGN-002, SKL-DESIGN-003)
6. **Parameters** (designers_parameters.json - 48 params)
7. **Professions** (UI/UX designer, graphic designer, 3D designer, illustrator, web designer)
8. **Products** (subset) - Design-related products
9. **Services** (Design_Services.json)

**Recognition Patterns:**
- UI/UX, design systems, components, wireframes
- Figma, Adobe tools, design platforms
- Design deliverables (mockups, prototypes, assets)
- Portfolio platforms (Dribbble, Behance)

**Use Cases:**
- Design review meetings
- Client design projects
- Design system discussions
- Portfolio showcase planning

---

### 06_Dev_Libraries.md
**Size:** 1,000-1,500 lines (Heavy on tools like AI department)
**Department:** Dev (3 employees - Klimenko Yaroslav, Kizilova Olha, Danylenko Liliia)

**Libraries Integrated:**
1. **Tools** (FULL - 75+ tools) - CRITICAL for dev team
   - 18 Dev tools (VS Code, GitHub, Docker, npm, etc.)
   - 7 Database tools (PostgreSQL, MongoDB, MySQL, etc.)
   - 3 Cloud platforms (AWS, Google Cloud, Azure)
   - Frameworks, libraries, APIs
2. **Actions** (subset) - Data_Operations + development actions
3. **Processes** (subset) - Development workflows, CI/CD, code review
4. **Objects** (subset) - Technical objects (APIs, databases, repos)
5. **Skills** (DEV_Skills.json + SKL-DESIGN-002 for frontend)
6. **Parameters** (developers_parameters.json - 124 params)
7. **Professions** (Frontend, backend, fullstack developer, QA engineer)
8. **Prompts** (subset) - Technical prompts

**Recognition Patterns:**
- Databases, APIs, deployment, infrastructure
- Frontend, backend, fullstack development
- Docker, GitHub, React, Node.js, Python
- CI/CD, testing, code review

**Use Cases:**
- Development planning meetings
- Technical architecture discussions
- Code review sessions
- Deployment and infrastructure planning

---

### 07_LG_Libraries.md
**Size:** 800-1,200 lines
**Department:** LG (11 employees - second largest)

**Libraries Integrated:**
1. **Actions** (Data_Operations - FULL)
   - 12 Data_Operations files (scraping, parsing, sanitizing, enriching, etc.)
2. **Processes** (Lead_Generation_Workflows.json - full)
3. **Tools** (subset) - LG-specific tools
   - Apollo.io, Instantly.ai, LinkedIn Sales Navigator
   - Bright Data, Apify scrapers, Phantombuster
   - Email finders, contact enrichment tools
4. **Skills** (LG_Skills.json - full)
5. **Parameters** (lead_generator_parameters.json - 78 params)
6. **Services** (Lead_Generation_Services.json)
7. **Professions** (Lead generator, SDR, data analyst)
8. **Objects** (subset) - Contact data, lead lists, scraped data
9. **Results** (subset) - Qualified leads, enriched data, contact databases

**Recognition Patterns:**
- Lead generation, prospecting, outreach, scraping
- Contact enrichment, email finding, data cleaning
- Apollo, LinkedIn, Apify, Bright Data
- B2B platforms, lead databases

**Use Cases:**
- Lead generation campaign planning
- Data scraping project discussions
- Contact enrichment workflows
- Platform strategy (LinkedIn, Apollo)

---

### 08_Parameters_Lightweight.md
**Size:** 300-500 lines (Summary only, not full 61,383-line source)
**Purpose:** Lightweight parameters overview

**Contains:**
- Overview of parameters structure (10,596+ parameters)
- Department breakdown table
  - Managers: 316 parameters (4 professions)
  - Developers: 124 parameters (1 profession)
  - Designers: 48 parameters (1 profession)
  - Marketers: 89 parameters (1 profession)
  - etc.
- Links to profession-specific parameter files
- Top 20 most common parameters across all professions
- How to reference full parameters.json when detailed params needed

**Why Lightweight:**
- Full parameters.json = 61,383 lines (too large for any prompt)
- Already organized by department AND profession in source
- Summary provides context without overwhelming prompt
- Detailed params can be loaded on-demand via reference

**Use Cases:**
- Quick parameter reference
- Understanding parameter structure
- Identifying relevant parameter files for specific professions

---

### 09_Taxonomy_Framework.md
**Size:** 600-800 lines
**Purpose:** System architecture reference

**Contains:**
- Overview of entire 12-library taxonomy system
- How all libraries interconnect
- Master relationship diagram
  - Actions → Processes → Results (lifecycle)
  - Action + Object = Task Template
  - Responsibility = Action + Object
  - Responsibility + Tool = Skill
- System architecture principles
- Cross-reference patterns
- ID format conventions for all 12 libraries
- Integration philosophy

**Why Separate:**
- Reference document, not operational
- Explains system architecture, not used for entity matching
- Loaded when understanding overall system needed
- Educational/onboarding value

---

## Department-to-Library Mapping Matrix

| Library | HR | AI | Video | Sales | Design | Dev | LG | Common |
|---------|----|----|-------|-------|--------|-----|----|----|
| **Actions** | Subset | Full | Subset | Subset | Subset | Subset | Full | Overview |
| **Objects** | - | Subset | Full | - | Full | Subset | Subset | - |
| **Processes** | Subset | Subset | Subset | Full | Full | Full | Full | Overview |
| **Results** | - | - | Subset | - | - | - | Subset | Overview |
| **Skills** | Subset | Full | Subset | Subset | Full | Full | Full | - |
| **Responsibilities** | Full | - | - | - | - | Subset | - | Formula |
| **Products** | - | - | - | Full | Subset | - | - | - |
| **Services** | - | - | - | Full | Full | - | Full | - |
| **Parameters** | 87 | 56 | - | 95 | 48 | 124 | 78 | Summary |
| **Professions** | Full | Subset | Subset | Subset | Full | Subset | Subset | Condensed |
| **Tools** | - | Full | Subset | Subset | Subset | Full | Subset | - |
| **Prompts** | - | Subset | - | - | - | Subset | - | Core |

**Legend:**
- **Full** = Complete library included
- **Subset** = Department-relevant portion only
- **Overview** = High-level summary
- **-** = Not included (minimal relevance)

---

## Loading Strategies

### Strategy 1: Single Department
**Use Case:** Department-specific meeting (e.g., Design team meeting)

**Load:**
- 00_Common_Libraries.md (always)
- 05_Design_Libraries.md (department-specific)
- 08_Parameters_Lightweight.md (summary)

**Total:** ~1,600-2,300 lines

---

### Strategy 2: Cross-Functional
**Use Case:** Multi-department collaboration (e.g., AI + Design meeting)

**Load:**
- 00_Common_Libraries.md (always)
- 02_AI_Libraries.md
- 05_Design_Libraries.md
- 08_Parameters_Lightweight.md

**Total:** ~2,300-3,800 lines

---

### Strategy 3: Full/Comprehensive
**Use Case:** All-hands meeting, comprehensive analysis

**Load:**
- All 10 files

**Total:** ~6,000-8,000 lines (still better than old approach with detailed params)

---

### Strategy 4: Lightweight Reference
**Use Case:** Quick analysis, simple meeting

**Load:**
- 00_Common_Libraries.md
- 08_Parameters_Lightweight.md
- 09_Taxonomy_Framework.md (optional)

**Total:** ~1,400-2,100 lines

---

## Prompt Weight Comparison

### Old Approach (13 library files)
| Meeting Type | Files Loaded | Estimated Lines |
|--------------|--------------|-----------------|
| HR Meeting | All 13 files | 8,000-12,000 |
| AI Meeting | All 13 files | 8,000-12,000 |
| Design Meeting | All 13 files | 8,000-12,000 |
| Cross-Functional | All 13 files | 8,000-12,000 |

**Issue:** No selective loading, all libraries loaded regardless of relevance

---

### New Approach (10 department files)
| Meeting Type | Files Loaded | Estimated Lines | Reduction |
|--------------|--------------|-----------------|-----------|
| HR Meeting | Common + HR + Params | 1,200-1,700 | 70-85% |
| AI Meeting | Common + AI + Params | 2,100-2,800 | 60-75% |
| Design Meeting | Common + Design + Params | 1,600-2,300 | 70-80% |
| Cross-Functional | Common + 2 Depts + Params | 2,300-3,800 | 50-70% |

**Benefit:** Selective loading reduces prompt weight by 50-85% depending on meeting type

---

## Update and Maintenance

### When to Update Library Integration Files

**Monthly:**
- Verify employee counts match department sizes
- Check if new departments added

**When LIBRARIES Updated:**
1. Identify which library changed (e.g., Tools library)
2. Determine affected department files (Tools = AI + Dev + Design + LG + Video)
3. Update relevant department files
4. Update statistics in affected files
5. Re-run assembly scripts

**Update Matrix:**
| Library Updated | Files to Update |
|-----------------|-----------------|
| Actions | Common (overview) + all dept files with Actions subsets |
| Objects | Video, Design, Dev, LG files |
| Processes | Common (overview) + all dept files |
| Results | Common (overview) + relevant dept files |
| Skills | All dept files (dept-specific skill files) |
| Responsibilities | HR, Common files |
| Products | Sales, Design files |
| Services | Sales, LG files |
| Parameters | Parameters_Lightweight + verify dept param counts |
| Professions | Common (condensed) + HR (full) + all depts (subsets) |
| Tools | AI (full), Dev (full), Design, Video, LG, Sales subsets |
| Prompts | Common + AI + Dev files |

---

## Cross-References

### To Core Files
- **00_Core/02_Company_Context.md** - Department structure (7 departments)
- **00_Core/03_Employee_Directory.md** - Department team sizes
- **00_Core/04_Project_Directory.md** - Project-to-department mapping

### To Output Templates
- **02_Output_Templates/** - Which templates use which libraries
- Integration levels documented in output template files

### To Processing Rules
- **03_Processing_Rules/** - How to apply library recognition patterns

### To Assembly Scripts
- **scripts/assemble_department.py** - Department-specific assembly logic
- **scripts/README.md** - Loading strategies documented

---

## Statistics Verification

**Baseline (2025-11-15):**
- Actions: 429
- Objects: 36
- Processes: 428
- Results: 432
- Skills: 12+
- Products: 39
- Services: 7 categories
- Parameters: 10,596+ (61,383 source lines)
- Professions: 27
- Tools: 75+

**Next Verification:** During MIL-003 file creation (verify against actual library files)
**Final Verification:** MIL-008 (before project completion)

---

## Benefits Summary

### 1. Prompt Weight Reduction
- 40-85% reduction depending on meeting type
- Selective loading only relevant libraries

### 2. Organizational Alignment
- Files match 7-department structure
- Department teams see only relevant content

### 3. Maintainability
- 10 files vs 13 files
- Logical grouping by department
- Clear update matrix

### 4. Flexibility
- Can load single department
- Can load multiple departments (cross-functional)
- Can load all (comprehensive)

### 5. Scalability
- New library? Assign to relevant department(s)
- New department? Add new department file
- Growing libraries? Already segmented

---

**Status:** 🚧 In Progress - Creating 10 department-focused library integration files in MIL-003
