---
category: PROMPTS
subcategory: root
type: prompt
source_id: PMT-045_SMM_Document_Processing
title: PMT-045 SMM Document Processing
date: 2025-11-21
status: draft
owner: unknown
related: []
links: []
---

# PMT-045 SMM Document Processing

## Summary
- TODO

## Context
- TODO

## Data / Content
# SMM Research Document Processing Instructions - Taxonomy Analysis Focus

---

## 🔴 CRITICAL OUTPUT REQUIREMENT 🔴

**MUST OUTPUT COMPLETE STRUCTURED MARKDOWN DOCUMENT**

❌ **DO NOT** output JSON, plain text, or any other format
✅ **REQUIRED FORMAT:** Markdown (.md) with sections below
✅ **FILE EXTENSION:** .md (not .json, .txt)

---

**Purpose**: Process SMM research documents with structured extraction of workflows, action verbs, task chains, and responsibilities vocabulary for taxonomy mapping.

**Version**: 1.0 - Adapted from Video Transcription Methodology
**Date**: 2025-11-13
**Source Adaptation**: Based on Video_Transcription_Custom_Instructions.md

---

## Core Document Processing Requirements

**Output complete structured markdown document** with the following format:

### Technical Requirements
- **Format:** Markdown (.md) only - NOT JSON, NOT plain text
- **Encoding:** UTF-8
- **Special Characters:** If $ or currency symbols cause corruption, write out full words ("five point six million")
- **Quality Check:** Ensure all text is properly formatted and readable

Process the SMM research document with the following structure in markdown format:

### 1. Metadata Section
- **Document Title**: [Extract exact title]
- **Document Type**: [Research/Guide/Strategy/Process]
- **Domain**: SMM/Social Media AI
- **Source**: [If available]
- **Date Created/Updated**: [If available]
- **Author/Team**: [If available]

### 2. Document Summary Section
- **Overview**: [Brief summary of document purpose]
- **Key Topics**: [List main topics covered]
- **Primary Focus Areas**: [Main themes - e.g., Instagram recruiting, content strategy, etc.]
- **Target Audience**: [Who this document is for - e.g., Recruiters, Content Creators, SMM specialists]

### 3. Full Document Content Extraction

Extract and organize content, including:
- **Section Headings**: Preserve document structure
- **Key Concepts**: Highlight important terms and definitions
- **Process Descriptions**: Capture all described workflows and procedures
- **Tools Mentioned**: Note all platforms, apps, and tools referenced
- **Examples**: Include any examples or case studies provided

---

## TAXONOMY EXTRACTION REQUIREMENTS (Critical)

### 4. Workflows Identification

**Identify and extract all workflows/processes mentioned in the document:**

Format each workflow as:
```
WORKFLOW: [Workflow Name]
OBJECTIVE: [What the workflow achieves]
STEPS:
  1. [Action verb] + [object/deliverable]
  2. [Action verb] + [object/deliverable]
  3. [Continue...]
DURATION: [Time estimate if mentioned]
COMPLEXITY: [Low/Medium/High if mentioned]
TOOLS USED: [List all tools/platforms mentioned]
INPUT: [What you start with]
OUTPUT: [What you end with]
PLATFORM: [Primary platform - Instagram, LinkedIn, TikTok, etc.]
```

**Examples from SMM Context:**
```
WORKFLOW: Screen Candidates via Instagram DMs
OBJECTIVE: Engage with candidates responding to Instagram ads by confirming application details and scheduling interviews
STEPS:
  1. Confirm candidate interest in vacancies
  2. Assess language skills for communications
  3. Request candidate profiles via CV or video business card
  4. Schedule interviews for job requests
DURATION: 15-30 minutes per candidate
COMPLEXITY: Medium
TOOLS USED: Instagram DMs, Video recording tools
INPUT: Candidate inquiry from Instagram ad
OUTPUT: Scheduled interview with qualified candidate
PLATFORM: Instagram
```

```
WORKFLOW: Create Platform-Specific Content Strategy
OBJECTIVE: Develop tailored content approach for different social media platforms
STEPS:
  1. Analyze platform demographics and behavior
  2. Define content categories per platform
  3. Establish posting frequency and timing
  4. Create content calendar template
  5. Define success metrics per platform
DURATION: 2-4 hours for initial strategy
COMPLEXITY: High
TOOLS USED: Social media platforms (Instagram, LinkedIn, TikTok), Analytics tools, Content calendar tools
INPUT: Brand identity, target audience data, platform insights
OUTPUT: Platform-specific content strategy document
PLATFORM: Multi-platform
```

### 5. Action Verbs & Operations

**Extract ALL action verbs and operations mentioned:**

Create categorized lists:

#### A. CREATION VERBS (Making new things)
- Create
- Generate
- Design
- Build
- Develop
- Draft
- Produce
- Craft
- Compose
- Record
- Post
- Publish
- [Add others found]

#### B. MODIFICATION VERBS (Changing existing things)
- Edit
- Refine
- Optimize
- Enhance
- Update
- Revise
- Improve
- Adjust
- Customize
- Reschedule
- Reconfirm
- [Add others found]

#### C. ANALYSIS VERBS (Understanding/Evaluating)
- Analyze
- Review
- Evaluate
- Research
- Assess
- Examine
- Test
- Compare
- Verify
- Screen
- [Add others found]

#### D. ORGANIZATION VERBS (Structuring/Managing)
- Organize
- Structure
- Categorize
- Schedule
- Plan
- Coordinate
- Prioritize
- Arrange
- Confirm
- [Add others found]

#### E. COMMUNICATION VERBS (Sharing/Presenting)
- Present
- Share
- Publish
- Deliver
- Communicate
- Report
- Demonstrate
- Respond
- Engage
- Inquire
- Request
- Follow up
- [Add others found]

#### F. SOCIAL MEDIA OPERATIONS (Platform-Specific Actions)
- Post
- Message
- DM (Direct Message)
- Comment
- Like
- Share
- Repost
- Tag
- Mention
- Story
- Reel
- Go live
- Engage
- Interact
- Monitor
- [Add others found]

**Note**: This category captures action verbs specific to social media platforms, community management, and digital engagement activities.

#### G. DATA OPERATIONS (Processing, Transforming, Moving Data)
- Scrape
- Parse
- Extract
- Import
- Upload
- Download
- Export
- Track
- Measure
- Monitor
- Analyze metrics
- Report
- [Add others found]

**Note**: This category captures verbs related to social media analytics, performance tracking, and data-driven decision making.

#### H. RECRUITMENT-SPECIFIC OPERATIONS (HR/Recruiting Actions)
- Screen
- Interview
- Recruit
- Hire
- Onboard
- Assess
- Qualify
- Source
- Reach out
- Nurture
- Follow up
- Reject
- Accept
- [Add others found]

**Note**: This category captures verbs specific to recruitment workflows conducted via social media platforms.

### 6. Task Chains

**Identify sequential task chains (multi-step processes):**

Format:
```
TASK CHAIN: [Name]
[Step 1] → [Step 2] → [Step 3] → [Output]

Example:
TASK CHAIN: Instagram Candidate Recruitment
Candidate responds to ad → Confirm vacancy interest → Assess language skills → Request CV/video → Schedule interview → Conduct interview
```

```
TASK CHAIN: Multi-Platform Content Distribution
Create content → Adapt for platform specs → Schedule posts → Publish → Monitor engagement → Analyze performance → Optimize strategy
```

### 7. Responsibilities Vocabulary

**Extract all role-related terms and responsibilities:**

#### Professional Roles Mentioned:
- Recruiter
- SMM Specialist
- Content Creator
- Social Media Manager
- Community Manager
- Content Strategist
- [List all mentioned]

#### Responsibilities/Activities:
- "Screening candidates via Instagram DMs"
- "Creating platform-specific content"
- "Managing social media recruitment campaigns"
- "Engaging with community members"
- "Monitoring social media metrics"
- [Extract all responsibility phrases]

#### Skills Mentioned:
- "Social media communication"
- "Candidate screening"
- "Content strategy development"
- "Platform-specific optimization"
- "Community engagement"
- "Analytics interpretation"
- [Extract all skill references]

### 8. Tools & Platforms Matrix

**Create a comprehensive tools matrix:**

| Tool/Platform Name | Category | Purpose | Used For | Mentioned With |
|-------------------|----------|---------|----------|----------------|
| Instagram | Social Media Platform | Communication & Recruitment | Candidate screening, DM communication | Video recording tools |
| LinkedIn | Social Media Platform | Professional networking | B2B content, professional outreach | Articles, long-form content |
| TikTok | Social Media Platform | Short-form video | Viral content, brand awareness | Video editing tools |
| Telegram | Messaging Platform | File sharing | Resume submission, document exchange | Instagram |
| [Continue...] | | | | |

### 9. Objects & Deliverables

**List all tangible outputs/deliverables mentioned:**

#### Communication Objects:
- DMs (Direct Messages)
- Comments
- Posts
- Stories
- Reels
- [Add all others]

#### Recruitment Objects:
- CVs/Resumes
- Video business cards
- Job applications
- Interview schedules
- Vacancy descriptions
- [Add all others]

#### Content Objects:
- Social media posts
- Content calendars
- Content strategy documents
- Performance reports
- Analytics dashboards
- [Add all others]

### 10. Integration Patterns

**Document how tools/processes/platforms connect:**

Format:
```
INTEGRATION: [Tool/Platform A] + [Tool/Platform B]
PURPOSE: [Why they're used together]
FLOW: [Tool A output] → [becomes] → [Tool B input]

Example:
INTEGRATION: Instagram + Telegram
PURPOSE: Seamless candidate document collection
FLOW: Initial screening (Instagram DMs) → Request CV → Candidate sends resume (Telegram) → Confirm receipt (Instagram)
```

```
INTEGRATION: Content Calendar + Multi-Platform Publishing
PURPOSE: Coordinated cross-platform content distribution
FLOW: Content strategy → Calendar planning → Platform-specific adaptation → Scheduled publishing → Performance tracking
```

### 11. Business Concepts & Strategy

**Extract business/strategy concepts mentioned:**

- Recruitment funnel strategies (e.g., "Instagram ad → DM screening → Interview")
- Engagement metrics (e.g., "response rate", "conversion rate")
- Content strategies (e.g., "platform-specific optimization", "audience segmentation")
- Success metrics (e.g., "quality of hire", "engagement rate", "reach")
- Strategic approaches (e.g., "multi-platform presence", "authentic engagement")

### 12. Platform-Specific Best Practices

**Document any platform-specific tips, strategies, or best practices:**

Format:
```
PLATFORM: [Platform name]
BEST PRACTICE: [What to do]
REASON: [Why this works]
CONTEXT: [When/where mentioned in document]

Example:
PLATFORM: Instagram
BEST PRACTICE: Use DMs for initial candidate screening before formal interview
REASON: Creates informal, comfortable first contact and allows quick qualification
CONTEXT: Recruiter workflow for remote candidates
```

### 13. Communication Patterns & Templates

**Extract communication templates, scripts, or patterns:**

Format:
```
COMMUNICATION TYPE: [E.g., Initial Contact, Follow-up, Rejection]
CHANNEL: [Platform/Tool]
PURPOSE: [Goal of communication]
TEMPLATE/PATTERN: [Example or structure]
TONE: [Professional/Casual/Friendly]

Example:
COMMUNICATION TYPE: Initial Candidate Contact
CHANNEL: Instagram DM
PURPOSE: Confirm vacancy interest and gather basic information
TEMPLATE: "Hello! Thank you for your interest in [vacancy]. Could you please confirm which specific position you're interested in? Also, what is your proficiency level in [language]?"
TONE: Friendly, Professional
```

---

## FORMATTING STANDARDS

### General Markdown Rules:
- Use `#` headers for major sections
- Use `##` for subsections
- **Bold** important terms
- `Code formatting` for tool/platform names and technical terms
- Bullet points for lists
- Tables for structured data
- > Blockquotes for examples or templates

### Taxonomy-Specific Formatting:
- ACTION VERBS: Always in CAPS when categorizing
- Tool/Platform names: Always capitalized consistently
- Workflows: Always use structured format above
- Task chains: Use → arrows between steps

---

## EXAMPLE OUTPUT STRUCTURE

```markdown
# Document Title: Screen Candidates via Instagram DMs

## Metadata
**Document Type**: Research/Process Documentation
**Domain**: SMM - Social Media AI (Recruitment)
**Date**: 2025-11-13
**Target Audience**: Recruiters, HR Specialists

## Document Summary
**Overview**: This document outlines the process for screening job candidates through Instagram DMs, from initial contact to interview scheduling.

**Key Topics**:
- Candidate screening
- Instagram DM communication
- Language assessment
- Interview scheduling

**Primary Focus Areas**: Social media recruitment, remote hiring, Instagram marketing

---
# FULL DOCUMENT CONTENT

[Complete extracted content with preserved structure...]

---
# TAXONOMY ANALYSIS

## Workflows Identified

### WORKFLOW 1: Screen Candidates via Instagram DMs
**OBJECTIVE**: Engage with candidates responding to Instagram ads
**STEPS**:
  1. Confirm candidate interest in vacancies
  2. Assess language skills for communications
  3. Request candidate profiles via CV or video
  4. Schedule interviews for job requests
**DURATION**: 15-30 minutes per candidate
**COMPLEXITY**: Medium
**TOOLS**: Instagram, Telegram
**INPUT**: Candidate inquiry
**OUTPUT**: Scheduled interview
**PLATFORM**: Instagram

[Continue for all workflows...]

## Action Verbs Extracted

### Creation Verbs
- Create (mentioned 5 times)
- Post (mentioned 8 times)
- Design (mentioned 3 times)
[Continue...]

### Communication Verbs
- Engage (mentioned 12 times)
- Respond (mentioned 7 times)
- Follow up (mentioned 9 times)
[Continue...]

### Recruitment-Specific Operations
- Screen (mentioned 15 times)
- Interview (mentioned 10 times)
- Assess (mentioned 8 times)
[Continue...]

## Task Chains

1. Ad response → Confirm interest → Assess language → Request CV → Schedule interview
2. Create content → Optimize for platform → Schedule post → Engage with comments
[Continue...]

## Responsibilities Vocabulary

**Roles**: Recruiter, SMM Specialist, Community Manager
**Activities**:
- "screening candidates via Instagram DMs"
- "assessing language proficiency"
- "scheduling virtual interviews"
- "managing candidate communications"

**Skills**:
- Social media communication
- Candidate qualification
- Multi-platform management
- Language assessment

## Tools & Platforms Matrix

| Tool/Platform | Category | Purpose | Evidence |
|--------------|----------|---------|----------|
| Instagram | Social Media | Candidate screening, DM communication | Throughout document |
| Telegram | Messaging | File sharing, CV submission | Step 6 |
| Video tools | Media creation | Video business cards | Step 3 |

## Objects & Deliverables

- Instagram DMs (text communication)
- CVs/Resumes (PDF/DOC)
- Video business cards (MP4)
- Interview schedules (calendar entries)
- Vacancy descriptions (text/docs)
[Continue...]

## Integration Patterns

**Pattern 1**: Instagram + Telegram
- Purpose: Comprehensive candidate communication
- Flow: Screening (Instagram) → Document collection (Telegram) → Confirmation (Instagram)

[Continue...]

## Business Concepts

- **Recruitment Funnel**: Ad → DM → Screen → Interview
- **Multi-channel Communication**: Instagram for conversation, Telegram for files
- **Remote Hiring Process**: Virtual screening and interviewing

## Platform-Specific Best Practices

1. **Instagram DMs**: Use conversational tone for candidate comfort
2. **Response Time**: Quick replies improve candidate engagement
3. **Multi-step Screening**: Gradual qualification through conversation
[Continue...]

## Communication Patterns

**Type 1**: Initial Contact Template
- Channel: Instagram DM
- Purpose: Confirm vacancy interest
- Template: "Hello! Thank you for your interest in [vacancy]..."
- Tone: Friendly, Professional

[Continue...]

---

## Key Takeaways for Taxonomy

**New Tools to Add**: [List]
**New Workflows**: [List]
**New Actions**: [List]
**New Responsibilities**: [List]
**Integration Opportunities**: [List]
**Platform-Specific Patterns**: [List]
```

---

## CRITICAL INSTRUCTIONS

1. **Never miss action verbs** - They map directly to taxonomy actions
2. **Capture exact workflow steps** - Essential for process documentation
3. **Note all tool/platform combinations** - Shows integration patterns
4. **Extract responsibility phrases** - Maps to profession taxonomy
5. **Document time estimates** - Helps with workflow planning
6. **Preserve business context** - Shows value and ROI
7. **Platform specificity** - Note which social media platform for each workflow
8. **Communication patterns** - Template extraction is critical for SMM processes

## VALIDATION CHECKLIST

### FORMAT VALIDATION (CRITICAL - Check First!)
- [ ] **Output is markdown (.md)** - NOT JSON, NOT plain text
- [ ] **Document starts with # heading** - Proper markdown structure
- [ ] **File would save as .md extension** - Confirm format
- [ ] **No JSON curly braces `{}` at document start** - Must be markdown

### SECTION COMPLETENESS
- [ ] **All 3 main sections present:**
  - [ ] 1. Metadata Section
  - [ ] 2. Document Summary Section
  - [ ] 3. Full Document Content Extraction
- [ ] **TAXONOMY ANALYSIS section included** - This is NOT optional
- [ ] **All required taxonomy subsections present:**
  - [ ] Workflows Identified
  - [ ] Action Verbs & Operations (A-H categories)
  - [ ] Task Chains
  - [ ] Responsibilities Vocabulary
  - [ ] Tools & Platforms Matrix
  - [ ] Objects & Deliverables
  - [ ] Integration Patterns
  - [ ] Business Concepts & Strategy
  - [ ] Platform-Specific Best Practices
  - [ ] Communication Patterns & Templates

### CONTENT QUALITY
- [ ] All workflows have structured format (OBJECTIVE, STEPS, DURATION, PLATFORM, etc.)
- [ ] Action verbs categorized into 8 categories (A-H, including SMM-specific)
- [ ] Tools/platforms matrix in TABLE format (not JSON, not bulleted list)
- [ ] Task chains show clear flow with arrows (→)
- [ ] Responsibilities vocabulary extracted
- [ ] Integration patterns documented
- [ ] Communication patterns/templates extracted
- [ ] Platform-specific context preserved
- [ ] Business value captured

---

## Taxonomy Mapping Guide

### How Extracted Data Maps to Taxonomy:

| Extracted Element | Maps To Taxonomy | File Location |
|-------------------|------------------|---------------|
| **Workflows** | SMM_Processes.json | LIBRARIES/Processes/ |
| **Action Verbs** | Social_Media_Actions.json | LIBRARIES/Actions/ |
| **Platforms** | Individual platform JSON files | LIBRARIES/Tools/Social_Media_Platforms/ |
| **Responsibilities** | Profession files (Recruiter, SMM Specialist) | LIBRARIES/Professions/ |
| **Deliverables** | Social_Media_Deliverables.json | LIBRARIES/Objects/ |
| **Skills** | Skills taxonomy | LIBRARIES/Skills/ |
| **Communication Patterns** | Communication_Templates.json | LIBRARIES/Templates/ |

### Priority for Taxonomy Updates:

1. **High Priority**: New platforms, workflows, action verbs, communication patterns
2. **Medium Priority**: Integration patterns, best practices, templates
3. **Low Priority**: Business concepts (for context only)

---

## Usage Notes

### For AI Document Processing:
- Use this prompt as system instructions
- Process research documents through this structure
- Output complete structured markdown

### For Manual Processing:
- Follow structure systematically
- Use provided templates for each section
- Don't skip taxonomy extraction sections

### For Quality Assurance:
- Verify all workflows have platform context
- Ensure action verbs are properly categorized (including SMM-specific H category)
- Confirm tools/platforms are correctly identified
- Check that communication patterns are extracted with templates

---

## SMM-Specific Considerations

### Platform Context
Always note which social media platform is primary for each:
- Workflow
- Best practice
- Communication pattern
- Tool integration

### Multi-Platform Scenarios
When content spans multiple platforms:
- Document platform-specific adaptations
- Note cross-platform workflows
- Identify platform strengths/use cases

### Communication Tone & Templates
SMM heavily relies on communication patterns:
- Extract message templates
- Note tone guidelines
- Document response frameworks
- Capture follow-up sequences

### Metrics & Performance
Social media is data-driven:
- Note mentioned KPIs
- Document success metrics
- Extract performance indicators
- Identify optimization opportunities

---

## Version History

**v1.0** (2025-11-13)
- **CREATED:** Initial adaptation from Video Transcription methodology
- **ADDED:** H. RECRUITMENT-SPECIFIC OPERATIONS action verb category
- **ADDED:** F. SOCIAL MEDIA OPERATIONS action verb category
- **ADDED:** Section 13: Communication Patterns & Templates
- **ADDED:** Section 12: Platform-Specific Best Practices
- **ENHANCED:** Tools matrix to become Tools & Platforms Matrix
- **ENHANCED:** Integration patterns for social media context
- **ENHANCED:** SMM-specific considerations section
- **SOURCE:** Adapted from Video_Transcription_Custom_Instructions.md v3.1
- **USE CASE:** Processing SMM research documents in LIBRARIES/Researches/SMM/

---

**Maintained By**: Taxonomy Team
**Last Updated**: 2025-11-13
**Status**: Active - Production Ready
**Version**: 1.0
**Adapted From**: Video Transcription methodology for SMM research document processing


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-21 standardization scaffold added
