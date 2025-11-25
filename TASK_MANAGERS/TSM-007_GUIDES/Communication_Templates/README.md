# Communication Templates

## Overview

This directory contains reusable communication and content templates used across workflows in the TASK_MANAGERS system. These templates provide standardized text scaffolds, messaging frameworks, and content structures for various communication channels and platforms.

## Purpose

Communication templates serve as **content guidelines** that define **WHAT to say** in various contexts, complementing:
- **Task Templates** (define HOW to execute work)
- **Step Templates** (define detailed sub-steps of tasks)
- **Workflows** (orchestrate tasks and steps, referencing both)

## Directory Contents

### Current Templates

| File | Template Count | Purpose | ID Range |
|------|----------------|---------|----------|
| `SMM_Communication_Templates.json` | 15 | Social media posts, captions, threads, comments | TMPL-SMM-001 to TMPL-SMM-015 |

### Template Categories

**SMM Communication Templates** cover:
- Instagram (Carousel Captions, Reel Captions)
- Twitter/X (Thread Openers, Quick Tips)
- LinkedIn (Thought Leadership, Articles)
- YouTube (Video Descriptions)
- Short-form Video (TikTok, Reels, Shorts)
- Behance (Project Descriptions)
- Medium (Article Openings)
- Facebook (Group Welcome, Value Posts)
- Pinterest (Pin Descriptions)
- Cross-platform (Teasers, Comment Responses)

## Template Structure

Each communication template follows this schema:

```json
{
  "template_id": "TMPL-XXX-###",
  "template_type": "Category/Purpose",
  "full_name": "Descriptive Full Name",
  "channel": "Platform(s)",
  "purpose": "What this template accomplishes",
  "tone": "Communication style (e.g., Professional, Casual)",
  "template_text": "Actual template with [variables]",
  "variables": ["[List]", "[Of]", "[Variables]"],
  "context": "When to use this template",
  "used_in_workflows": ["WF-XXX-###"],
  "workflow_context": {
    "WF-XXX-###": "Which step uses this template"
  },
  "best_practices": [
    "Guidelines for effective use"
  ]
}
```

## Relationship to Workflows

Communication templates are **referenced by workflows** in TASK_MANAGERS/Workflows/:

**Example:**
- Workflow: `Instagram_Content_Strategy_Workflow.yaml` (WF-SMM-003)
- Step 1: "Create Educational Carousels"
- Uses: Template TMPL-SMM-001 (Instagram Carousel Caption)

The workflow defines the **process** (create carousel), the template provides the **content structure** (caption format).

## Template ID Conventions

### Naming Pattern
`TMPL-[CATEGORY]-[###]`

### Categories
- **SMM**: Social Media Marketing templates (001-099)
- **REC**: Recruitment communication templates (100-199)
- **MKT**: Marketing communication templates (200-299)
- **VID**: Video content templates (300-399)
- **EMAIL**: Email templates (400-499)
- **SALES**: Sales communication templates (500-599)

*Note: ID ranges allow for future expansion within each category*

## Usage Guidelines

### For Template Users
1. **Find the right template**: Browse by platform or content type
2. **Replace variables**: Substitute all `[bracketed]` placeholders
3. **Customize tone**: Adapt template to your brand voice
4. **Follow best practices**: Each template includes platform-specific tips
5. **Test and iterate**: A/B test variations for optimization

### For Template Creators
1. **Use consistent schema**: Follow the structure above
2. **Provide clear variables**: Make placeholders obvious with `[brackets]`
3. **Include context**: Explain when and how to use the template
4. **Add workflow references**: Link to workflows that use the template
5. **Document best practices**: Share platform-specific insights

## Platform-Specific Notes

### Instagram
- Focus on **saves** (5x algorithm weight)
- Use 3-5 niche hashtags (not 30)
- Visual storytelling is key

### Twitter/X
- Be concise (280 character limit)
- Use threads for depth (number them: 1/7, 2/7)
- Engage within 30 minutes

### LinkedIn
- Lead with business value and ROI
- Professional tone with data backing
- Post Tuesday-Thursday 8-10am or 5-6pm EST

### YouTube
- SEO-first descriptions (200+ words)
- Detailed timestamps for navigation
- Front-load keywords

### TikTok/Reels/Shorts
- Hook in first 3 seconds (CRITICAL)
- Always include captions (many watch without sound)
- Trending sounds boost algorithm

### Facebook Groups
- Native video preferred over links
- Community-focused language
- Respond within 4 hours

### Medium
- Long-form depth (2000-5000 words)
- Story-driven narratives
- Comprehensive guides

### Pinterest
- SEO keywords essential
- Evergreen content focus
- Vertical images (1000×1500px)

## Integration with Other TASK_MANAGERS Components

```
Workflows (YAML)
    ↓ references
Task Templates (JSON)
    ↓ references
Step Templates (JSON)
    ↓ uses
Communication Templates (JSON) ← YOU ARE HERE
```

**Example Flow:**
1. **Workflow**: `WF-SMM-003` (Instagram Content Strategy)
2. **Task**: Create educational carousel
3. **Steps**: Design slides, write caption, post
4. **Communication Template**: TMPL-SMM-001 (provides caption structure)

## Future Expansion

Planned template categories:
- Email templates (customer support, marketing, transactional)
- Sales communication templates (outreach, follow-up, proposals)
- Video script templates (intros, outros, CTAs)
- Community management templates (moderation, announcements)
- Client communication templates (project updates, invoices)

## Cross-References

### Related Directories
- `../Workflows/` - Workflow definitions that use these templates
- `../Task_Templates/` - Operational Task Templates
- `../Step_Templates/` - Detailed step definitions
- `../../LIBRARIES/Actions/` - Action taxonomy
- `../../LIBRARIES/Objects/` - Content objects created using templates

### Documentation
- See `Taxonomy_Analysis_and_Updates_Prompt.md` for taxonomy integration methodology
- See workflow YAML files for template usage in context

## Metadata

- **Entity Type**: TASK_MANAGERS
- **Sub-Entity**: Communication_Template
- **Format**: JSON
- **Total Templates**: 15 (as of 2025-11-13)
- **Last Updated**: 2025-11-13

---

**Note**: Communication templates are **operational content tools**, not reference library items. They actively support workflow execution by providing standardized, proven content structures for various communication scenarios.
