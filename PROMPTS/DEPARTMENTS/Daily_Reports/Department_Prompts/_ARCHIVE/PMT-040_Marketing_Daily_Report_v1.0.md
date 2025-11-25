# AI Department - Daily Report Collection Prompt

## Purpose
This prompt is specifically designed for the **AI Department** to process call transcriptions and generate daily activity reports. It combines the comprehensive call organization framework with AI-specific context, employee directory, and daily report automation.

---

## Department Context: AI

### Department Overview
**Mission:** AI campaigns, brand management, content marketing
**Team Size:** 3-5 employees
**Key Responsibilities:**
- Plan and execute marketing campaigns
- Manage brand messaging and positioning
- Create marketing content and materials
- Analyze marketing performance metrics

### AI Department Employees

*Note: Employee list should be populated from MAIN PROMPT v4.md employee directory filtered by department AI*

### AI-Specific Projects

*Note: Projects should be populated from department project listings*

### AI-Specific Tools
**AI & Content Tools:**
- C dans - AI-powered video animation and motion graphics
- ChatGPT (OpenAI) - Content generation, message creation
- Claude - Advanced AI assistant for analysis and automation
- Claude Desktop App - Local desktop application for Claude AI
- Claude Projects - Organize AI workflows

**AI Platforms:**
- Various marketing platforms and analytics tools (see TOOLS_GUIDE.md)

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
   - Folder organization (`/Nov25/AI Nov25/Reports/{DAY}/`)
   - Metrics and statistics extraction

---

## AI-Specific Instructions

### Step 1: Read AI Prompt Log
Read the AI department prompt log file:
- `Dropbox/Nov25/AI Nov25/AI prompt log.md` (if exists)

**Time Scope:** Focus on this week's activities. When reading employee folders, include the current week's folders (e.g., if reporting on Nov 12, read folders 08, 09, 10, 11, 12), not just the single report day. This allows capturing the full context of ongoing work and multi-day tasks.

**Task Documentation Requirement:** Extract detailed task information from employee daily.md, plans.md, and task.md files. For each task mentioned, include:
- Task name and description
- Specific actions taken
- Outcomes achieved
- Impact or results

Avoid generic confirmations like "6 tasks completed" - instead provide specific summaries of WHAT tasks were accomplished.

### Step 2: Process Call Transcripts (if applicable)
When processing AI-related call transcripts, focus on:

**AI-Specific Sections to Emphasize:**

#### Section 3: ACTION ITEMS & TASKS
- **Campaign Tasks:** AI campaign planning and execution
- **Content Tasks:** AI content creation
- **Analytics Tasks:** Performance analysis and reporting
- **Brand Tasks:** Brand management activities

#### Section 8: TOOLS & RESOURCES
- **AI Tools:** AI platforms and tools
- **AI Tools:** AI tools for content and analysis
- **Analytics Tools:** Performance tracking tools

#### Section 17: METRICS & PERFORMANCE INDICATORS
- **Campaign Metrics:** Campaign performance data
- **Engagement Metrics:** Audience engagement metrics
- **Conversion Metrics:** Conversion and ROI data
- **Brand Metrics:** Brand awareness and perception

#### Section 18: CREATIVE & CONTENT DELIVERABLES
- **AI Content:** All marketing materials created
- **Campaign Assets:** Campaign-specific content
- **Brand Assets:** Brand-related materials

### Step 3: Generate AI Daily Activity Report

**File Location:** `/Nov25/AI Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**AI-Specific Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department: AI
   - Team size: 3-5 employees
   - Total campaigns active
   - Total content pieces created
   - Total performance analyses
   - Overall status

2. **Campaign Activities**
   - Campaigns planned
   - Campaigns executed
   - Campaign performance
   - Campaign optimizations

3. **Content Creation**
   - AI content created
   - Content formats produced
   - Content distribution
   - Content performance

4. **Brand Management**
   - Brand messaging activities
   - Brand positioning work
   - Brand consistency checks
   - Brand asset management

5. **Performance Analysis**
   - Campaign performance analysis
   - Engagement metrics review
   - Conversion analysis
   - ROI calculations

6. **Cross-Department Collaboration**
   - Collaboration with Design team
   - Collaboration with Content
   - Collaboration with Sales team
   - Collaboration with SMM team

7. **Metrics and Statistics**
   - Campaigns active: [count with campaign names and status]
   - Content pieces created: [count with content types and purposes]
   - Performance analyses completed: [count with analysis types]
   - Tools utilized: [count with tool names and purposes]

   **IMPORTANT:** For each metric, provide specific details rather than just numbers. Example:
   - Instead of: "Campaigns active: 3"
   - Write: "Campaigns active: 3 (Q4 Product Launch - in execution phase, 45% completion; Holiday Promotion - planning phase; Brand Awareness Campaign - performance review phase)"

8. **Key Deliverables**
   - Campaign plans and materials
   - AI content created
   - Performance reports
   - Brand guidelines updates

9. **AI Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Campaign performance improvements
   - Brand awareness gains
   - Categories affected (Campaigns, Content, Brand, Analytics)

10. **AI Achievements**
    - Campaign successes
    - Content quality improvements
    - Brand positioning enhancements
    - Performance optimizations

11. **Challenges and Solutions**
    - Campaign challenges
    - Content creation issues
    - Performance problems
    - Solutions implemented

12. **Files Created/Modified Summary**
    - New marketing files created (with paths)
    - Modified marketing files (with descriptions)
    - Campaign documentation updates
    - Brand asset updates

13. **Recommendations for Follow-up**
    - Immediate actions required
    - Short-term improvements
    - Long-term enhancements

14. **Success Indicators**
    - Completed successfully (checkboxes)
    - Quality metrics (checkboxes)
    - Pending items

15. **Conclusion**
    - Summary of day's work
    - Key achievements recap
    - Impact assessment
    - Overall status

**Report Footer:**
```
---
**Report Generated:** [Date]
**Department:** AI
**Team Size:** 3-5
**Report Status:** Complete
---
*End of Report*
```

---

## AI-Specific Vocabulary

**AI Terms:**
- Campaign, Brand, Positioning, Messaging
- Engagement, Conversion, ROI, Performance
- Content marketing, Brand management
- AI analytics, Performance metrics

**Campaign Terms:**
- Campaign planning, Campaign execution
- Campaign optimization, Campaign performance
- Audience targeting, Channel selection

---

## AI-Specific Quality Standards

### Content Requirements
- ✅ All campaign activities included
- ✅ All content creation activities documented
- ✅ All brand activities tracked
- ✅ All performance analyses recorded
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
Process AI department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read AI prompt log: Dropbox/Nov25/AI Nov25/AI prompt log.md (if exists)
2. Process any AI-related call transcripts using MAIN PROMPT v4.md framework
3. Create Reports/{DAY} folder in AI department
4. Generate detailed AI activity report following AI-specific template

Focus on:
- Campaign planning and execution
- AI content creation
- Brand management activities
- Performance analysis and metrics
```

---

## Version History

**v1.0** - November 13, 2025
- Initial AI-specific prompt creation
- Integrated MAIN PROMPT v4.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added AI-specific context and tools
- Customized report template for AI department

---

*Last Updated: November 13, 2025*
*Department: AI*

