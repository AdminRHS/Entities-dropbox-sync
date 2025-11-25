# SMM Research Documents Library

**Purpose**: Central repository for Social Media Marketing (SMM) research documents and their corresponding taxonomy mapping analysis.

**Location**: `LIBRARIES/Researches/SMM/`

**Last Updated**: 2025-11-13

---

## Overview

This folder contains SMM research documents analyzed for taxonomy extraction. Each document is processed to identify:
- Social media workflows and processes
- Platform-specific operations
- Action verbs and operations (including SMM-specific actions)
- Task chains and sequences
- Communication patterns and templates
- Responsibilities vocabulary (Recruiter, SMM Specialist roles)
- Tools and platforms integration
- Best practices and strategies

The extracted information is then mapped to the existing taxonomy structure in the LIBRARIES folder.

---

## File Structure

### Current Research Documents

| File | Size | Status | Integration Report |
|------|------|--------|-------------------|
| `Communicate with Remote Candidates via Instagram DMs.md` | 5 KB | ✅ Complete (Phases 1-7) | [Document_1_Integration_Report.md](Document_1_Integration_Report.md) |
| `Content Strategy & Categories by Platform.md` | 17 KB | ✅ Complete (Phases 1-7) | [Document_2_Integration_Report.md](Document_2_Integration_Report.md) |
| `Social Media Strategies for Creative Professionals (EU, 2025).md` | 148 KB | ⏸️ Pending | - |
| `README.md` | - | - | This file |

#### Document Processing Status

**Document 1** ("Communicate with Remote Candidates via Instagram DMs")
- **Focus**: Instagram DM recruitment workflows, Telegram file sharing
- **Files Created**: 7 files (Instagram.json, Telegram.json, Recruiter.json, 8 recruitment templates, 2 workflow files)
- **Status**: ✅ Complete
- **Report**: [Document_1_Integration_Report.md](Document_1_Integration_Report.md)

**Document 2** ("Content Strategy & Categories by Platform")
- **Focus**: Multi-platform content strategy, creative professional workflows
- **Files Created**: 35 files (9 platforms, 5 professions, 12 workflows, 22 objects, 15 templates)
- **Status**: ✅ Complete (6 critical platforms pending)
- **Report**: [Document_2_Integration_Report.md](Document_2_Integration_Report.md)
- **Integration Score**: 85%

**Document 3** ("Social Media Strategies for Creative Professionals (EU, 2025)")
- **Focus**: Tactical execution, EU/US market strategies, platform deep-dives
- **Size**: 148 KB (3x larger than Document 2)
- **Status**: ⏸️ Pending
- **Expected Output**: 50+ files (platform variations, market-specific strategies, tactical templates)

### Naming Conventions

**Research Documents**:
- Format: `[Descriptive Title].md`
- Contains: Research content, workflows, processes, strategies
- Formats supported: Markdown

**Analysis Reports** (to be created):
- Format: `[Document Name]_Taxonomy_Analysis.md`
- Contains: Comprehensive taxonomy extraction and mapping
- Includes: Workflows, action verbs, tools, integration patterns

---

## Workflow: From SMM Research Document to Taxonomy

### Phase 1: Document Processing
1. **Input**: SMM research document (markdown)
2. **Process**: Extract workflows, tools, communication patterns
3. **Instructions**: See [`../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md)
4. **Output**: `[Document Name]_Taxonomy_Analysis.md` with structured extraction

### Phase 2: Initial Analysis
1. **Input**: Research document
2. **Process**: Extract workflows, platforms, actions, responsibilities, communication patterns
3. **Methodology**: Follow SMM Research Document Processing Instructions
4. **Output**: Structured extraction of taxonomy elements

### Phase 3: Platform & Tool Mapping
1. **Input**: Extracted platforms and tools
2. **Process**: Identify social media platforms, messaging tools, analytics tools
3. **Output**: Complete platform/tool inventory with use cases

### Phase 4: Communication Patterns Extraction
1. **Input**: Document content
2. **Process**: Extract message templates, communication workflows, tone guidelines
3. **Output**: Communication pattern library with templates

### Phase 5: Library Mapping and Gap Analysis
1. **Input**: Extracted taxonomy elements
2. **Process**: Map to existing LIBRARIES structure, identify gaps
3. **Compare**: Calculate coverage metrics (before/after percentages)
4. **Output**: Gap analysis with prioritized items to create/update

### Phase 6: Taxonomy Updates
1. **Input**: Gap analysis and extracted elements
2. **Process**: Create/update JSON files across all taxonomy libraries
3. **Locations**:
   - Platforms → `../../Tools/Social_Media_Platforms/*.json`
   - Objects → `../../Objects/*.json` (Social_Media_Deliverables)
   - Workflows → `../../Processes/SMM_Processes.json`
   - Actions → `../../Actions/Social_Media_Actions.json`
   - Professions → `../../Professions/Recruiter.json`, `../../Professions/SMM_Specialist.json`
   - Communication Templates → `../../Templates/Communication_Templates.json`
4. **Output**: Updated taxonomy library entries with bidirectional cross-references

### Phase 7: Comprehensive Reporting
1. **Input**: All completed taxonomy updates
2. **Process**: Generate comprehensive analysis report
3. **Output**: `[Document Name]_Taxonomy_Analysis.md` with:
   - Coverage metrics
   - Gap analysis results
   - Files created/modified
   - Business value and insights
   - Platform-specific patterns
   - Communication templates extracted

---

## Document Processing Instructions

### Complete Processing Guide

**Primary Prompt**: [`../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md)

**Key Features**:
- Adapted from Video Transcription methodology (v3.1)
- SMM-specific action verb categories
- Platform-specific context preservation
- Communication pattern extraction
- Template identification
- Multi-platform workflow support

**Version**: 1.0 (2025-11-13)

---

## Taxonomy Extraction Focus Areas

### 1. Social Media Platforms & Tools

**What to extract**:
- Platform names (Instagram, LinkedIn, TikTok, etc.)
- Messaging tools (Telegram, WhatsApp, etc.)
- Analytics tools
- Content creation tools
- Scheduling/management tools

**Example from "Communicate with Remote Candidates via Instagram DMs"**:
- Instagram (Primary platform for DM communication)
- Telegram (File sharing, CV submission)
- Video recording tools (Video business cards)

### 2. SMM Workflows

**What to extract**:
- Workflow name and objective
- Sequential steps (action verb + object)
- Duration estimates
- Platform specificity
- Tools/platforms used
- Input and output formats

**Example**:
```
WORKFLOW: Screen Candidates via Instagram DMs
OBJECTIVE: Engage with candidates responding to Instagram ads
STEPS:
  1. Confirm candidate interest in vacancies
  2. Assess language skills for communications
  3. Request candidate profiles via CV or video
  4. Schedule interviews for job requests
DURATION: 15-30 minutes per candidate
COMPLEXITY: Medium
PLATFORM: Instagram
TOOLS: Instagram DMs, Telegram, Video tools
INPUT: Candidate inquiry from ad
OUTPUT: Scheduled interview with qualified candidate
```

### 3. Action Verbs (SMM-Specific)

**Categories** (8 total, includes SMM-specific):
- **A. Creation**: Create, Post, Design, Produce
- **B. Modification**: Edit, Optimize, Reschedule
- **C. Analysis**: Analyze, Assess, Screen, Review
- **D. Organization**: Schedule, Plan, Coordinate, Confirm
- **E. Communication**: Engage, Respond, Follow up, Inquire
- **F. Social Media Operations**: Post, DM, Comment, Like, Share, Tag, Story, Reel
- **G. Data Operations**: Track, Monitor, Analyze metrics, Report
- **H. Recruitment-Specific Operations**: Screen, Interview, Recruit, Source, Onboard

### 4. Task Chains

**Format**: `[Step 1] → [Step 2] → [Step 3] → [Output]`

**Example from Instagram Recruitment**:
```
Candidate responds to ad → Confirm vacancy interest → Assess language skills → Request CV/video → Schedule interview → Conduct interview
```

**Example from Content Strategy**:
```
Create content → Adapt for platform specs → Schedule posts → Publish → Monitor engagement → Analyze performance → Optimize strategy
```

### 5. Communication Patterns & Templates

**What to extract**:
- Message templates
- Communication sequences
- Tone guidelines
- Response frameworks
- Follow-up patterns

**Example**:
```
COMMUNICATION TYPE: Initial Candidate Contact
CHANNEL: Instagram DM
PURPOSE: Confirm vacancy interest
TEMPLATE: "Hello! Thank you for your interest in [vacancy]. Could you please confirm which specific position you're interested in?"
TONE: Friendly, Professional
```

### 6. Responsibilities Vocabulary

**What to extract**:
- Role names (Recruiter, SMM Specialist, Content Creator, Community Manager)
- Activity phrases ("screening candidates via DMs", "engaging with community")
- Skill mentions ("social media communication", "content strategy")

### 7. Platform-Specific Patterns

**What to document**:
- Platform strengths and use cases
- Platform-specific workflows
- Best practices per platform
- Platform limitations
- Cross-platform strategies

**Example**:
```
PLATFORM: Instagram
BEST PRACTICE: Use DMs for initial candidate screening
REASON: Creates informal, comfortable first contact
USE CASE: Remote recruitment, candidate engagement
```

### 8. Integration Patterns

**What to document**:
- Platform combinations
- Tool integrations
- Multi-channel workflows
- Data flow between platforms

**Example**:
```
INTEGRATION: Instagram + Telegram
PURPOSE: Comprehensive candidate communication
FLOW: Screening (Instagram DMs) → Document collection (Telegram) → Confirmation (Instagram)
REASON: Instagram for conversation, Telegram for reliable file sharing
```

---

## Coverage Metrics

Track how well document analysis populates the taxonomy:

### Current Status:
- **Documents Processed**: 3 (pending analysis)
- **Platforms Identified**: Instagram, LinkedIn, TikTok, Telegram (preliminary)
- **Workflows Documented**: TBD after analysis
- **Action Verbs Cataloged**: TBD after analysis
- **Communication Templates**: TBD after analysis

---

## Quality Standards

### Document Processing Quality
- [ ] Complete metadata captured (title, type, focus area)
- [ ] All workflows identified with platform context
- [ ] Platform-specific operations noted
- [ ] Communication patterns extracted with templates
- [ ] Tools and platforms listed with use cases
- [ ] Integration patterns documented

### Taxonomy Extraction Quality
- [ ] All mentioned platforms/tools identified
- [ ] Workflows have structured format (objective, steps, duration, platform, tools, I/O)
- [ ] Action verbs categorized into 8 groups (including SMM-specific F, H)
- [ ] Task chains show clear sequential flow
- [ ] Responsibilities vocabulary extracted
- [ ] Communication templates captured with channel, purpose, tone
- [ ] Platform-specific best practices documented

### Mapping Quality
- [ ] Each platform has corresponding JSON file in taxonomy
- [ ] Workflows mapped to SMM_Processes library
- [ ] Action verbs added to Social_Media_Actions library
- [ ] Communication templates added to Templates library
- [ ] Gap analysis completed and documented
- [ ] Coverage metrics calculated
- [ ] Platform-specific patterns preserved

---

## Best Practices

### For Document Processing
1. Use [`SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md) as system prompt
2. Preserve platform context for all workflows
3. Extract all communication patterns and templates
4. Note tone and channel for each communication type
5. Document multi-platform strategies clearly

### For Analysis
1. Follow the structured extraction format
2. Categorize action verbs consistently (including SMM-specific categories)
3. Identify platform specificity for each workflow
4. Extract communication templates with full context
5. Note integration patterns between platforms
6. Document best practices with reasoning

### For Library Mapping
1. Check existing taxonomy before creating duplicates
2. Follow JSON structure standards for platform/tool files
3. Link related entries (platforms ↔ workflows ↔ professions ↔ templates)
4. Preserve communication templates in dedicated library
5. Document all changes in analysis report

---

## Related Documentation

### Taxonomy Categories
Primary mapping targets in LIBRARIES structure:
- **Platforms/Tools** → `../../Tools/Social_Media_Platforms/*.json`
- **Objects** → `../../Objects/Social_Media_Deliverables.json`
- **Workflows** → `../../Processes/SMM_Processes.json`
- **Actions** → `../../Actions/Social_Media_Actions.json`
- **Professions** → `../../Professions/*.json` (Recruiter, SMM_Specialist, etc.)
- **Communication Templates** → `../../Templates/Communication_Templates.json`
- **Skills** → `../../Skills/*.json`
- **Responsibilities** → `../../Responsibilities/*.json`

### Processing Instructions
- **SMM Document Processing**: [`../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md)
- **Original Video Transcription**: [`../../PROMPTS/Video_Transcription/Video_Transcription_Custom_Instructions.md`](../../PROMPTS/Video_Transcription/Video_Transcription_Custom_Instructions.md)

---

## Examples

### Example 1: Platform Extraction

**Mentioned in document**: "Use Instagram DMs for initial screening, then request CV via Telegram"

**Extraction**:
1. **Platform 1**: Instagram
   - Category: Social Media Platform
   - Use Case: Direct messaging, candidate screening
   - Strengths: Casual communication, visual profile

2. **Platform 2**: Telegram
   - Category: Messaging Platform
   - Use Case: File sharing, CV submission
   - Strengths: Reliable file transfer, privacy

**Integration Pattern**:
- Instagram (screening) → Telegram (documents) → Instagram (confirmation)

### Example 2: Workflow Extraction

**Mentioned in document**: "Confirm interest, assess language skills, request CV, schedule interview"

**Extracted Workflow**:
```
WORKFLOW: Screen Candidates via Instagram DMs
OBJECTIVE: Qualify candidates responding to recruitment ads
STEPS:
  1. Confirm candidate interest in vacancies
  2. Assess language skills for communications
  3. Request candidate profiles via CV or video business card
  4. Schedule interviews for job requests
DURATION: 15-30 minutes per candidate
COMPLEXITY: Medium
PLATFORM: Instagram (primary)
TOOLS: Instagram DMs, Telegram (CV sharing)
INPUT: Candidate inquiry from Instagram ad
OUTPUT: Qualified candidate with scheduled interview
```

### Example 3: Communication Template Extraction

**Mentioned in document**: "Begin by confirming the specific vacancy the candidate is interested in"

**Extracted Template**:
```
COMMUNICATION TYPE: Initial Contact - Vacancy Confirmation
CHANNEL: Instagram DM
PURPOSE: Confirm vacancy interest and provide role overview
TEMPLATE: "Hello! Thank you for your interest in [vacancy name]. Could you please confirm which specific position you're interested in? I'd be happy to provide more details about the role."
TONE: Friendly, Professional, Welcoming
FOLLOW-UP: If confirmed → proceed to language assessment
```

---

## Version History

**v1.0** (2025-11-13)
- Initial README creation
- Defined file structure and naming conventions
- Documented workflow from research document to taxonomy
- Established quality standards and best practices
- Created SMM-specific processing instructions
- Adapted from Video Transcriptions methodology

---

## Contributing

### Adding New Research Documents

1. **Add document**: Place in this folder with descriptive name
2. **Process document**: Use SMM Research Document Processing Instructions
3. **Create analysis**: `[Document Name]_Taxonomy_Analysis.md`
4. **Extract taxonomy elements**: Workflows, platforms, actions, templates
5. **Update taxonomy**: Create/update JSON files for gaps
6. **Update this README**: Add file to Current Research Documents table

### Processing Existing Documents

For the current 3 documents awaiting analysis:
1. Process each using [`SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md)
2. Create `[Document Name]_Taxonomy_Analysis.md` for each
3. Extract all taxonomy elements
4. Perform gap analysis
5. Update taxonomy libraries
6. Update coverage metrics in this README

---

## Maintenance

### Regular Tasks
- [ ] Process new research documents as they're added
- [ ] Update coverage metrics after each analysis
- [ ] Consolidate duplicate platform/tool entries
- [ ] Ensure cross-references between platforms, workflows, and templates are accurate
- [ ] Review and update communication templates library

### Quality Checks
- [ ] Verify all platform JSON files have correct category paths
- [ ] Check for broken links in documentation
- [ ] Validate workflow step sequences make sense
- [ ] Ensure action verb categorization includes SMM-specific categories (F, H)
- [ ] Confirm communication templates have channel, purpose, tone, and context
- [ ] Verify platform-specific best practices are documented

---

## Quick Reference

### Current Documents to Process

1. **Communicate with Remote Candidates via Instagram DMs.md**
   - Focus: Recruitment workflows via Instagram
   - Primary Platform: Instagram
   - Key Elements: DM communication, screening steps, interview scheduling

2. **Content Strategy & Categories by Platform.md**
   - Focus: Platform-specific content strategies
   - Primary Platforms: Multi-platform (likely Instagram, LinkedIn, TikTok, etc.)
   - Key Elements: Content categories, platform optimization, strategy frameworks

3. **Social Media Strategies for Creative Professionals (EU, 2025).md**
   - Focus: SMM strategies for creative industry
   - Region: European Union
   - Key Elements: Industry-specific strategies, creative sector workflows

### Processing Priority

**High Priority**:
1. Extract workflows and platform-specific operations
2. Identify communication patterns and templates
3. Map action verbs to SMM-specific categories

**Medium Priority**:
1. Document integration patterns
2. Extract best practices
3. Identify cross-platform strategies

**Low Priority**:
1. Business context (for understanding only)
2. Regional considerations (unless critical to workflow)

---

## Support & Questions

### Documentation Resources
- **Processing Instructions**: [`../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md`](../../PROMPTS/SMM_Research/SMM_Research_Document_Processing_Instructions.md)
- **Taxonomy Structure**: [`../../README.md`](../../README.md) - LIBRARIES overview (if exists)
- **Video Transcription Reference**: [`../../Transcribations/README.md`](../../Transcribations/README.md) - Similar methodology

### Contact
- **Maintained By**: Taxonomy Team
- **Status**: Active - Ready for document processing
- **Last Review**: 2025-11-13

---

**End of README**
