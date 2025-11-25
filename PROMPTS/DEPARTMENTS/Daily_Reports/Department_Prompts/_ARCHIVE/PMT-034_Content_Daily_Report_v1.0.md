# Content Department - Daily Report Collection Prompt

## Purpose
This prompt is specifically designed for the **Content Department** to process call transcriptions and generate daily activity reports. It combines the comprehensive call organization framework with Content-specific context, employee directory, and daily report automation.

---

## Department Context: CONTENT (Content)

### Department Overview
**Mission:** Content creation, management, and operational workflows
**Team Size:** 3-5 employees
**Key Responsibilities:**
- Create and manage content workflows
- Organize and structure content deliverables
- Coordinate content operations across teams

### Content Department Employees

*Note: Employee list should be populated from MAIN PROMPT v4.md employee directory filtered by department CONTENT*

### Content-Specific Projects

*Note: Projects should be populated from department project listings*

### Content-Specific Tools
**AI Content Creation:**
- C dans - AI-powered video animation and motion graphics
- ElevenLabs - AI text-to-speech and voice cloning
- GLIF - AI workflow automation platform
- Kling - AI-powered video generation
- Nano Banana - AI image generation and manipulation

**Content Management:**
- Various content management and workflow tools (see TOOLS_GUIDE.md)

---

## Base Context Integration

This prompt integrates two core documents:

1. **MAIN PROMPT v4.md** - Complete call organization framework with:
   - Company context (Remote Helpers - AI-First organization)
   - Employee Directory (32 employees across 7 departments)
   - Project Directory (31+ active projects)
   - 21 comprehensive extraction sections
   - Intelligent participant and project matching
   - Template-driven operations framework

2. **PROMPT_Daily_Report_Collection.md** - Daily report automation with:
   - Report template structure (11 sections)
   - Folder organization (`/Nov25/Content Nov25/Reports/{DAY}/`)
   - Metrics and statistics extraction

---

## Content-Specific Instructions

### Step 1: Read Content Prompt Log
Read the Content department prompt log file:
- `Dropbox/Nov25/Content Nov25/Content prompt log.md` (if exists)

**Time Scope:** Focus on this week's activities. When reading employee folders, include the current week's folders (e.g., if reporting on Nov 12, read folders 08, 09, 10, 11, 12), not just the single report day. This allows capturing the full context of ongoing work and multi-day tasks.

**Task Documentation Requirement:** Extract detailed task information from employee daily.md, plans.md, and task.md files. For each task mentioned, include:
- Task name and description
- Specific actions taken
- Outcomes achieved
- Impact or results

Avoid generic confirmations like "6 tasks completed" - instead provide specific summaries of WHAT tasks were accomplished.

### Step 2: Process Call Transcripts (if applicable)
When processing Content-related call transcripts, focus on:

**Content-Specific Sections to Emphasize:**

#### Section 3: ACTION ITEMS & TASKS
- **Content Creation Tasks:** Document all content creation activities
- **Content Management Tasks:** Organization and workflow tasks
- **Content Coordination Tasks:** Cross-team coordination activities

#### Section 8: TOOLS & RESOURCES
- **AI Content Tools:** AI tools used for content creation
- **Content Management Tools:** Tools for organizing and managing content
- **Workflow Tools:** Tools for content workflows

#### Section 18: CREATIVE & CONTENT DELIVERABLES
- **Content Created:** All content deliverables
- **Content Formats:** Types of content produced
- **Content Quality:** Quality metrics and standards

#### Section 11: DOCUMENTATION & KNOWLEDGE GAPS
- **Content Documentation:** Content guidelines and standards
- **Workflow Documentation:** Content workflow processes
- **Tool Documentation:** Content tool usage guides

### Step 3: Generate Content Daily Activity Report

**File Location:** `/Nov25/Content Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**Content-Specific Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department: Content
   - Team size: 3-5 employees
   - Total content tasks
   - Total content deliverables
   - Total workflow improvements
   - Overall status

2. **Content Creation Activities**
   - Content pieces created
   - Content formats produced
   - Content quality metrics
   - AI tool usage

3. **Content Management Activities**
   - Content organization
   - Workflow implementations
   - Content structure improvements
   - Content coordination activities

4. **Workflow Operations**
   - Workflow optimizations
   - Process improvements
   - Tool integrations
   - Automation implementations

5. **Cross-Team Coordination**
   - Collaboration with Design team
   - Collaboration with Video team
   - Collaboration with AI team
   - Content handoffs

6. **Metrics and Statistics**
   - Content pieces created: [count with brief description of each]
   - Workflows implemented: [count with workflow descriptions]
   - Tools utilized: [count with tool names and purposes]
   - Content formats: [count with format types]

   **IMPORTANT:** For each metric, provide specific details rather than just numbers. Example:
   - Instead of: "Content pieces created: 10"
   - Write: "Content pieces created: 10 (5 blog posts for marketing campaign; 3 social media graphics for SMM; 2 video scripts for video team)"

7. **Key Deliverables**
   - Content deliverables created
   - Workflow documentation
   - Tool guides
   - Process improvements

8. **Content Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Process improvements made
   - Content quality improvements
   - Categories affected (Content Creation, Content Management, Workflows, Coordination)

9. **Content Achievements**
   - Content quality improvements
   - Workflow optimizations
   - Tool integrations
   - Process enhancements

10. **Challenges and Solutions**
    - Content creation challenges
    - Workflow issues
    - Tool limitations
    - Solutions implemented

11. **Files Created/Modified Summary**
    - New content files created (with paths)
    - Modified content files (with descriptions)
    - Workflow documentation updates
    - Tool documentation updates

12. **Recommendations for Follow-up**
    - Immediate actions required
    - Short-term improvements
    - Long-term enhancements

13. **Success Indicators**
    - Completed successfully (checkboxes)
    - Quality metrics (checkboxes)
    - Pending items

14. **Conclusion**
    - Summary of day's work
    - Key achievements recap
    - Impact assessment
    - Overall status

**Report Footer:**
```
---
**Report Generated:** [Date]
**Department:** Content
**Team Size:** 3-5
**Report Status:** Complete
---
*End of Report*
```

---

## Content-Specific Vocabulary

**Content Terms:**
- Content creation, Content management, Content workflow
- Content deliverables, Content formats, Content quality
- Content coordination, Content handoff

**Workflow Terms:**
- Workflow optimization, Process improvement
- Tool integration, Automation
- Content structure, Content organization

---

## Content-Specific Quality Standards

### Content Requirements
- ✅ All content creation activities included
- ✅ All content management activities documented
- ✅ All workflow activities tracked
- ✅ All coordination activities recorded
- ✅ Metrics and statistics calculated
- ✅ Impact analysis provided

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for statistics and metrics
- ✅ Bullet lists for achievements
- ✅ Checkboxes for completed items
- ✅ Consistent section structure

---

## Example Usage

### Command to AI Assistant:

```
Process Content department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read Content prompt log: Dropbox/Nov25/Content Nov25/Content prompt log.md (if exists)
2. Process any Content-related call transcripts using MAIN PROMPT v4.md framework
3. Create Reports/{DAY} folder in Content department
4. Generate detailed Content activity report following Content-specific template

Focus on:
- Content creation activities
- Content management workflows
- Tool usage and integration
- Cross-team coordination
```

---

## Version History

**v1.0** - November 13, 2025
- Initial Content-specific prompt creation
- Integrated MAIN PROMPT v4.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added Content-specific context and tools
- Customized report template for Content department

---

*Last Updated: November 13, 2025*
*Department: Content*

