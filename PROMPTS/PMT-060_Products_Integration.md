# Products Integration Prompt (depricated)
## Processing and Integrating Products with AI-First Principles

**Purpose**: Guide for processing raw product lists, optimizing with AI-first tool substitutions, and integrating with taxonomy libraries.

**Version**: 1.0
**Date**: 2025-11-12
**Status**: Active - Production Ready
**AI-First Compliance**: Mandatory for all products

---

## Table of Contents

1. [Overview](#overview)
2. [AI-First Tool Substitution](#ai-first-tool-substitution)
3. [Processing Raw Product Lists](#processing-raw-product-lists)
4. [Optimization Methodology](#optimization-methodology)
5. [Cross-Referencing](#cross-referencing)
6. [Real Examples from 39 Products](#real-examples-from-39-products)
7. [Quality Validation](#quality-validation)

---

## Overview

This prompt guides you through transforming raw product data into structured, AI-first taxonomy entries that integrate with all LIBRARIES entities.

### Input Format

Typical raw product list:
```
Product ID | Product Name | Description | MIN Hours
pdt0001 | Website Audit | Evaluates site's SEO and usability | 10
pdt0002 | Keyword Research | Identifies effective SEO keywords | 8
```

### Output Format

Structured JSON with AI-first focus:
```json
{
  "product_id": "PDT-0001",
  "name": "Website Audit",
  "description": "AI-powered comprehensive evaluation...",
  "ai_tools_used": ["ChatGPT", "SEO.ai", "Surfer SEO"],
  "ai_automation_level": "Semi-automated",
  ...
}
```

---

## AI-First Tool Substitution

### Core Principle

**EVERY tool must be AI-native OR AI-integrated.**

Traditional manual tools are replaced with AI alternatives to maximize:
- ⚡ Efficiency (reduce hours)
- 🎯 Quality (AI-powered analysis)
- 📈 Scalability (serve more clients)
- 💰 Profitability (lower costs, higher margins)

### Substitution Rules

#### Rule 1: Prefer AI-Native Tools

**AI-Native** = Built with AI at the core

**Examples**:
- ✅ ChatGPT, Claude (AI content generation)
- ✅ Midjourney, DALL-E (AI image generation)
- ✅ Runway, Synthesia (AI video generation)
- ✅ Descript (AI transcription, editing)
- ✅ Jasper.ai (AI copywriting)

#### Rule 2: AI-Enhanced Traditional Tools

If a traditional tool exists, use the **AI-enhanced version**:

| Traditional | AI-Enhanced Version |
|------------|-------------------|
| Google Analytics (manual) | Google Analytics + AI insights plugins |
| SEMrush (manual) | SEMrush with AI features enabled |
| Ahrefs (manual) | Ahrefs with AI keyword suggestions |
| Photoshop (manual) | Photoshop with Generative Fill (AI) |
| Premiere Pro (manual) | Premiere Pro with AI auto-reframe |
| Excel (manual) | Excel with Copilot (AI) |

#### Rule 3: AI + Human Hybrid

For complex tasks requiring human expertise:

**Format**: AI Tool (automated task) + Human (strategic task)

**Examples**:
- ChatGPT (generate draft) + Human (strategy, refinement)
- Midjourney (generate concepts) + Human (art direction)
- AI analytics (data processing) + Human (interpretation, insights)

#### Rule 4: No Traditional-Only Tools

**PROHIBITED** (unless no AI alternative exists):
- ❌ Manual spreadsheet analysis (use AI analytics)
- ❌ Manual keyword research (use AI keyword tools)
- ❌ Manual content writing (use AI content generation)
- ❌ Manual video editing (use AI video tools)
- ❌ Manual data entry (use AI automation)

### AI Tool Database Reference

All AI tools MUST exist in `LIBRARIES/Tools/AI_Tools/*.json`

**Check before adding**:
1. Search `AI_Tools/` for the tool
2. If exists: Reference by tool_id (e.g., "TOOL-AI-001")
3. If missing: Create new tool entry first

---

## Processing Raw Product Lists

### Step 1: Parse Input Data

From raw format:
```
pdt0001 | Website Audit | Evaluates site's SEO and usability | 10
```

Extract:
- **Product ID**: pdt0001 → Standardize to `PDT-0001`
- **Product Name**: Website Audit → Validate naming
- **Description**: Evaluates site's SEO... → Expand with AI focus
- **MIN Hours**: 10 → Add MAX hours estimate

### Step 2: Standardize Product ID

**Format**: `PDT-XXXX` (always 4 digits, zero-padded)

**Examples**:
- pdt0001 → PDT-0001 ✅
- pdt0042 → PDT-0042 ✅
- pdt123 → PDT-0123 ✅

### Step 3: Optimize Product Name

**Rules**:
- Capitalize each word (Title Case)
- Be specific and descriptive
- Remove vague terms ("Amazing", "Great")
- Include key benefit if space allows

**Examples**:
- "website audit" → "Website Audit" ✅
- "seo work" → "On-Page SEO Optimization" ✅ (more specific)
- "video stuff" → "Product Demonstration Video" ✅ (clear)

### Step 4: Expand Description (AI-First)

Transform from feature-focused to value-focused with AI emphasis:

**Original**: "Evaluates site's SEO and usability"

**AI-First Version**: "AI-powered comprehensive evaluation of website's SEO performance, technical health, and user experience usability, leveraging automated analysis tools to identify optimization opportunities and provide actionable recommendations"

**Template**:
```
"AI-powered [what it does] using [AI tools], delivering [value/outcome] through [AI capabilities]"
```

### Step 5: Estimate MAX Hours

If only MIN hours provided, estimate MAX hours:

**Formula**: `MAX Hours = MIN Hours × 1.5` (for complex scenarios)

**Examples**:
- MIN: 10 hours → MAX: 15 hours (50% buffer)
- MIN: 20 hours → MAX: 30 hours
- MIN: 8 hours → MAX: 12 hours

**Adjust based on complexity**:
- Simple products: 1.2× multiplier
- Standard products: 1.5× multiplier
- Complex products: 2.0× multiplier

---

## Optimization Methodology

### Phase 1: Identify AI Tools (15-20 min per product)

For each product, determine which AI tools can deliver it.

**Questions to ask**:
1. What tasks does this product involve?
2. Which AI tools can automate or assist those tasks?
3. What AI capabilities are needed (generation, analysis, optimization)?
4. What manual tasks remain (strategy, creativity, client communication)?

**Example: PDT-0001 Website Audit**

**Tasks**:
- Analyze site structure
- Evaluate SEO elements
- Assess technical issues
- Review usability
- Generate recommendations

**AI Tools**:
- ChatGPT/Claude → Automated analysis and recommendation generation
- SEO.ai or Surfer SEO → AI-powered SEO audit
- Google Search Console → Data source
- PageSpeed Insights → Technical analysis with AI recommendations

**AI Capabilities**:
- Automated issue detection
- AI-generated recommendations
- Predictive SEO suggestions
- Automated competitive analysis

**Manual Components**:
- Strategic interpretation
- Client-specific context
- Final review and quality assurance

### Phase 2: Determine AI Automation Level (5 min per product)

Classify how much AI automates:

**Manual** (AI-assisted, 0-30% automation):
- Human does most work
- AI provides suggestions or references
- High human oversight needed
- Example: Brand strategy (AI helps with research, human does strategy)

**Semi-automated** (30-70% automation):
- AI handles major tasks
- Human reviews and refines
- Moderate oversight needed
- Example: Website audit (AI does analysis, human interprets)

**Fully automated** (70-100% automation):
- AI handles end-to-end process
- Human only sets parameters and reviews output
- Minimal oversight needed
- Example: Automated email sequences (AI writes, sends, tracks)

### Phase 3: Map to Taxonomy (10-15 min per product)

Cross-reference with existing libraries:

#### Tools Mapping
```json
"ai_tools_used": [
  "ChatGPT - TOOL-AI-001",
  "Surfer SEO - TOOL-AI-XXX",
  "SEMrush with AI - TOOL-AI-XXX"
]
```

#### Professions Mapping
```json
"professions_required": [
  "SEO Specialist",
  "Web Analyst"
]
```

Check: `LIBRARIES/Professions/*.json`

#### Skills Mapping
```json
"skills_required": [
  "AI-assisted SEO analysis",
  "Technical SEO",
  "Prompt engineering",
  "Data interpretation"
]
```

Check: `TALENTS/Skills/Master/all_skills.json` or `TALENTS/Skills/By_Department/*.json`

#### Objects Mapping
```json
"objects_created": [
  "reports",
  "presentations",
  "action plans"
]
```

Check: `LIBRARIES/Objects/*.json`

#### Workflows Mapping
```json
"workflows_involved": [
  "SEO Audit Workflow - PROC-SEO-001"
]
```

Check: `LIBRARIES/Processes/*.json`

### Phase 4: Calculate Pricing (2-3 min per product)

**Formula**: `Price = Hours × $12.50`

```json
"pricing": {
  "minimum_hours": 10,
  "maximum_hours": 15,
  "base_rate_per_hour": 12.50,
  "estimated_price_min": 125,
  "estimated_price_max": 187.50
}
```

**Note**: AI automation should reduce hours compared to traditional manual delivery.

### Phase 5: Define Deliverables (5 min per product)

List concrete outputs client receives:

```json
"deliverables": [
  "SEO Audit Report (PDF, 15-25 pages)",
  "Technical Issues List (Excel/Google Sheets)",
  "Prioritized Recommendations (Action plan)",
  "Executive Summary Presentation (PowerPoint/Google Slides)"
]
```

**Make specific**: Include format and approximate size/length.

---

## Cross-Referencing

### Products → Tools (Bidirectional)

**In Product JSON**:
```json
"ai_tools_used": [
  "ChatGPT - TOOL-AI-001",
  "Midjourney - TOOL-AI-006"
]
```

**In Tool JSON** (update):
```json
"products_using_this_tool": [
  "Website Audit - PDT-0001",
  "Content Creation - PDT-0017"
]
```

### Products → Objects (Bidirectional)

**In Product JSON**:
```json
"objects_created": [
  "reports",
  "presentations"
]
```

**In Object JSON** (update Objects/Design_Deliverables.json):
```json
{
  "object_name": "presentations",
  "created_by_products": [
    "Website Audit - PDT-0001",
    "Campaign Analysis - PDT-0016"
  ]
}
```

### Products → Professions (Bidirectional)

**In Product JSON**:
```json
"professions_required": [
  "SEO Specialist",
  "Web Analyst"
]
```

**In Profession JSON** (update Professions/SEO_Specialist.json):
```json
{
  "profession": "SEO Specialist",
  "products_delivered": [
    "Website Audit - PDT-0001",
    "Keyword Research - PDT-0002",
    "Technical SEO - PDT-0006"
  ]
}
```

### Products → Skills (Bidirectional)

**In Product JSON**:
```json
"skills_required": [
  "AI-assisted SEO analysis",
  "Technical SEO"
]
```

**In Skill JSON** (update Skills/*.json):
```json
{
  "skill": "AI-assisted SEO analysis",
  "used_in_products": [
    "Website Audit - PDT-0001",
    "On-Page SEO - PDT-0003"
  ]
}
```

---

## Real Examples from 39 Products

### Example 1: PDT-0001 Website Audit

**Raw Input**:
```
pdt0001 | Website Audit | Evaluates site's SEO and usability | 10
```

**Step-by-Step Optimization**:

**Step 1: Standardize ID**
```
pdt0001 → PDT-0001 ✅
```

**Step 2: Expand Description**
```
Original: "Evaluates site's SEO and usability"
AI-First: "AI-powered comprehensive evaluation of website's SEO performance, technical health, and user experience usability, leveraging automated analysis tools to identify optimization opportunities and provide data-driven recommendations"
```

**Step 3: Identify AI Tools**
```json
"ai_tools_used": [
  "ChatGPT/Claude - TOOL-AI-001 (automated analysis and recommendations)",
  "SEO.ai or Surfer SEO (AI-powered SEO audit)",
  "Google Search Console (data source with AI insights)",
  "PageSpeed Insights (technical analysis with AI recommendations)",
  "Screaming Frog (crawling with AI pattern detection)"
]
```

**Step 4: Determine Automation Level**
```json
"ai_automation_level": "Semi-automated",
"ai_capabilities": [
  "Automated site crawling and indexing",
  "AI-powered issue detection (broken links, duplicate content, etc.)",
  "Automated SEO scoring and benchmarking",
  "AI-generated recommendations with priority levels",
  "Predictive impact analysis for suggested changes"
],
"manual_components": [
  "Strategic interpretation of audit findings",
  "Client-specific context and business goals alignment",
  "Custom recommendations based on industry best practices",
  "Final quality assurance and report formatting"
]
```

**Step 5: Map to Taxonomy**
```json
"cross_references": {
  "tools_used": [
    "TOOL-AI-001 (ChatGPT)",
    "TOOL-AI-XXX (SEO.ai or similar)"
  ],
  "professions_required": [
    "SEO Specialist",
    "Web Analyst"
  ],
  "skills_required": [
    "AI-assisted SEO analysis",
    "Technical SEO",
    "Data interpretation",
    "Prompt engineering",
    "SEO reporting"
  ],
  "objects_created": [
    "reports (SEO audit report)",
    "presentations (findings presentation)",
    "action plans (prioritized recommendations)"
  ],
  "workflows_involved": [
    "SEO Audit Workflow - PROC-SEO-001"
  ]
}
```

**Step 6: Calculate Pricing**
```json
"pricing": {
  "minimum_hours": 10,
  "maximum_hours": 15,
  "base_rate_per_hour": 12.50,
  "estimated_price_min": 125,
  "estimated_price_max": 187.50
}
```

**Step 7: Define Deliverables**
```json
"deliverables": [
  "Comprehensive SEO Audit Report (PDF, 20-30 pages with charts and graphs)",
  "Technical Issues Inventory (Excel spreadsheet with severity ratings)",
  "Prioritized Action Plan (Task list with estimated impact and effort)",
  "Executive Summary Presentation (PowerPoint, 10-15 slides)",
  "Competitive Benchmarking Report (comparison with 3-5 competitors)"
]
```

**Final JSON**:
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Product",
  "product_id": "PDT-0001",
  "name": "Website Audit",
  "category": "SEO Services",
  "tier": "Product (Tier 2)",
  "description": "AI-powered comprehensive evaluation of website's SEO performance, technical health, and user experience usability, leveraging automated analysis tools to identify optimization opportunities and provide data-driven recommendations",

  "pricing": {
    "minimum_hours": 10,
    "maximum_hours": 15,
    "base_rate_per_hour": 12.50,
    "estimated_price_min": 125,
    "estimated_price_max": 187.50
  },

  "ai_integration": {
    "ai_tools_used": [
      "ChatGPT/Claude - TOOL-AI-001 (automated analysis and recommendations)",
      "SEO.ai or Surfer SEO (AI-powered SEO audit)",
      "Google Search Console (data source with AI insights)",
      "PageSpeed Insights (technical analysis with AI recommendations)"
    ],
    "ai_automation_level": "Semi-automated",
    "ai_capabilities": [
      "Automated site crawling and indexing",
      "AI-powered issue detection",
      "Automated SEO scoring and benchmarking",
      "AI-generated recommendations with priority levels",
      "Predictive impact analysis"
    ],
    "manual_components": [
      "Strategic interpretation",
      "Client context alignment",
      "Custom industry recommendations",
      "Final QA and formatting"
    ]
  },

  "deliverables": [
    "Comprehensive SEO Audit Report (PDF, 20-30 pages)",
    "Technical Issues Inventory (Excel with severity ratings)",
    "Prioritized Action Plan (task list with impact/effort)",
    "Executive Summary Presentation (PowerPoint, 10-15 slides)",
    "Competitive Benchmarking Report (3-5 competitors)"
  ],

  "cross_references": {
    "tools_used": ["TOOL-AI-001", "TOOL-AI-XXX"],
    "professions_required": ["SEO Specialist", "Web Analyst"],
    "skills_required": ["AI-assisted SEO analysis", "Technical SEO", "Prompt engineering"],
    "objects_created": ["reports", "presentations", "action plans"],
    "workflows_involved": ["PROC-SEO-001"]
  },

  "requirements": {
    "prerequisites": [
      "Website URL and access credentials",
      "Google Analytics access",
      "Google Search Console access",
      "List of primary target keywords (optional)"
    ],
    "complexity": "Medium",
    "typical_duration": "1-2 weeks"
  },

  "related_products": [
    "PDT-0002 (Keyword Research)",
    "PDT-0003 (On-Page SEO)",
    "PDT-0006 (Technical SEO)"
  ],

  "tags": ["seo", "audit", "ai-powered", "analysis", "website-optimization"]
}
```

---

### Example 2: PDT-0010 3D Models

**Raw Input**:
```
pdt0010 | 3d models | Creation of detailed 3D models with photorealistic rendering | 45
```

**AI-First Optimization**:

**Identify AI Tools** (Traditional → AI-First):
- ❌ Traditional: 3ds Max, Maya, Blender (manual modeling)
- ✅ AI-First: Spline AI, Kaedim, NVIDIA Omniverse with AI, Blender with AI plugins

**AI Tools to Use**:
```json
"ai_tools_used": [
  "Spline AI (AI-assisted 3D modeling)",
  "Kaedim (2D image to 3D model AI conversion)",
  "NVIDIA Omniverse with AI tools (collaborative 3D creation)",
  "Blender with AI plugins (AI texture generation, AI lighting)",
  "ChatGPT/Claude (concept ideation and technical guidance)"
]
```

**AI Capabilities**:
```json
"ai_capabilities": [
  "2D to 3D AI conversion (upload image, get 3D model)",
  "AI-assisted UV unwrapping and texturing",
  "AI-powered lighting suggestions",
  "Automated LOD (Level of Detail) generation",
  "AI material recommendations based on object type"
],
"manual_components": [
  "Art direction and concept refinement",
  "Complex topology for animation-ready models",
  "Final detail passes for hero assets",
  "Quality control and client feedback integration"
]
```

**Automation Level**: Semi-automated (AI accelerates modeling, human refines quality)

---

### Example 3: PDT-0013 Blog & SEO Content

**Raw Input**:
```
pdt0013 | Blog & SEO Content | Production of SEO-optimized blog posts | 50
```

**AI-First Optimization**:

**Identify AI Tools** (Traditional → AI-First):
- ❌ Traditional: Manual writing, grammar checkers
- ✅ AI-First: ChatGPT/Claude, Jasper.ai, Surfer SEO, Grammarly AI

**AI Tools to Use**:
```json
"ai_tools_used": [
  "ChatGPT/Claude - TOOL-AI-001 (primary content generation)",
  "Jasper.ai (AI copywriting with templates)",
  "Surfer SEO (AI content optimization and SEO scoring)",
  "Clearscope or MarketMuse (AI content briefs)",
  "Grammarly AI (automated grammar and style)",
  "Hemingway Editor with AI (readability optimization)"
]
```

**AI Capabilities**:
```json
"ai_capabilities": [
  "AI content generation from outlines (5000+ words in minutes)",
  "Automated SEO optimization (keyword density, semantic keywords)",
  "AI-generated meta descriptions and titles",
  "Automated internal linking suggestions",
  "AI tone and style matching to brand voice",
  "Real-time content scoring and improvement suggestions"
],
"manual_components": [
  "Content strategy and topic selection",
  "Brand voice alignment and editing",
  "Fact-checking and accuracy verification",
  "Adding unique insights and examples",
  "Final polish and human touch"
]
```

**Automation Level**: Semi-automated to Fully automated (depending on content complexity)

**Pricing Impact**:
- Traditional manual: 50 hours @ $12.50 = $625
- AI-assisted: 20-30 hours @ $12.50 = $250-$375 (60% reduction)

---

## Quality Validation

### Validation Checklist

Before finalizing a product entry:

#### AI-First Compliance
- [ ] All tools are AI-native OR AI-integrated
- [ ] No traditional-only tools without justification
- [ ] AI automation level accurately reflects capabilities
- [ ] AI capabilities are specific (not vague "uses AI")

#### Data Completeness
- [ ] Product ID follows PDT-XXXX format
- [ ] Name is clear, specific, and professional
- [ ] Description is value-focused with AI emphasis
- [ ] MIN and MAX hours are realistic
- [ ] Pricing calculated correctly ($12.50/hour)
- [ ] Deliverables are concrete and specific

#### Cross-Reference Integrity
- [ ] All AI tools exist in LIBRARIES/Tools/AI_Tools
- [ ] All professions exist in LIBRARIES/Professions
- [ ] All skills exist in TALENTS/Skills
- [ ] All objects exist in LIBRARIES/Objects
- [ ] All workflows exist in LIBRARIES/Processes

#### Quality Standards
- [ ] Description > 100 characters (detailed enough)
- [ ] At least 3 deliverables specified
- [ ] Prerequisites clearly stated
- [ ] Related products identified (upsell opportunities)
- [ ] Tags are relevant and searchable

### Common Issues to Avoid

**❌ Vague AI tool references**:
```json
"ai_tools_used": ["AI tools"] // TOO VAGUE
```

**✅ Specific AI tools**:
```json
"ai_tools_used": [
  "ChatGPT - TOOL-AI-001 (content generation)",
  "Surfer SEO (optimization)"
]
```

**❌ Missing automation level**:
```json
// No ai_automation_level field
```

**✅ Clear automation level**:
```json
"ai_automation_level": "Semi-automated"
```

**❌ Traditional tools without AI**:
```json
"tools_used": ["Microsoft Word", "Excel"] // NO AI
```

**✅ AI-enhanced versions**:
```json
"ai_tools_used": [
  "Microsoft Word with Copilot (AI writing assistance)",
  "Excel with Copilot (AI data analysis)"
]
```

---

## Summary Workflow

### Complete Processing Flow

```
1. Parse raw input → Extract ID, name, description, hours
   ↓
2. Standardize → Format to PDT-XXXX, title case
   ↓
3. Expand description → Add AI-first value proposition
   ↓
4. Identify AI tools → Research and select AI alternatives
   ↓
5. Determine automation → Manual/Semi/Fully automated
   ↓
6. Map to taxonomy → Cross-reference all entities
   ↓
7. Calculate pricing → Apply $12.50/hour formula
   ↓
8. Define deliverables → Specify concrete outputs
   ↓
9. Validate → Check AI-first compliance and completeness
   ↓
10. Save JSON → Create product file in appropriate category
```

**Time per product**: 30-45 minutes (with AI tools to assist)

---

## Related Documentation

- [`README.md`](./README.md) - Products library overview and AI-first principles
- [`../Tools/AI_Tools/`](../Tools/AI_Tools/) - All available AI tools for products
- [`../Objects/`](../Objects/) - Deliverables created by products
- [`../Professions/`](../Professions/) - Roles that deliver products
- [`../Skills/`](../Skills/) - Skills required for products
- [`../Processes/`](../Processes/) - Workflows involved in products

---

**Maintained By**: Taxonomy Team
**Version**: 1.0
**Last Updated**: 2025-11-12
**Status**: Active - Production Ready
**AI-First Enforcement**: Mandatory

---

**End of Products Integration Prompt**
