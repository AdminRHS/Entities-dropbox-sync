# HR Department - Daily Report Collection Prompt

## Purpose
This prompt is specifically designed for the **HR Department** to process call transcriptions and generate daily activity reports. It combines the comprehensive call organization framework with HR-specific context, employee directory, and daily report automation.

---

## Department Context: HR (Human Resources)

### Department Overview
**Mission:** Recruitment, onboarding, employee management, talent acquisition
**Team Size:** 2 employees
**Key Responsibilities:**
- Recruitment and talent acquisition
- Employee onboarding and training
- CV processing and candidate evaluation
- Interview coordination
- Employee management and HR operations

### HR Department Employees

**Rekonvald Viktoriia** (ID: 83953) - Recruiter, Lead generator | Austria | @kkktouse | viktoriiarekonvald@gmail.com | Status: Work

**Nealova Evgeniya** (ID: 72889) - Recruiter | Ukraine | @ievgeniia_nealova | zp4058203@gmail.com | Status: Work | Rate: 1.25

### HR-Specific Projects
- **Recruitment Platform** - Talent acquisition and onboarding system
- **Onboarding Programs** - Day 1: Beginner, First Week: Foundation, Advanced training
- **CV Processing** - Candidate evaluation and screening
- **Interview Management** - Coordination and documentation
- **Employee Directory** - Management and updates

### HR-Specific Tools
- **Communication:** Discord, Gmail, Google Workspace, Notion
- **AI Tools:** ChatGPT, Claude, Gemini, NotebookLM (for CV analysis and candidate screening)
- **Documentation:** Google Drive, Notion, RAC (Remote AI Context)
- **CRM:** Template-driven task and project management

---

## Base Context Integration

This prompt integrates two core documents:

1. **MAIN PROMPT v3.md** - Complete call organization framework with:
   - Company context (Remote Helpers - AI-First organization)
   - Employee Directory (32 employees across 7 departments)
   - Project Directory (31+ active projects)
   - 21 comprehensive extraction sections
   - Intelligent participant and project matching
   - Template-driven operations framework

2. **PROMPT_Daily_Report_Collection.md** - Daily report automation with:
   - Report template structure (11 sections)
   - Folder organization (`/Nov25/HR/Reports/{DAY}/`)
   - Metrics and statistics extraction

---

## HR-Specific Instructions

### Step 1: Read HR Prompt Log
Read the HR department prompt log file:
- `Dropbox/Nov25/HR Nov25/HR prompt log.md`

### Step 2: Process Call Transcripts (if applicable)
When processing HR-related call transcripts, focus on:

**HR-Specific Sections to Emphasize:**

#### Section 20: ONBOARDING & TRAINING CONTEXT
- **Onboarding Program Level:** Day 1: Beginner/First Week: Foundation/Advanced
- **Training Topics:**
  - Beginner: Basic AI concepts, account setups, tool introduction
  - Foundation: Software basics, web concepts, communication protocols
  - Advanced: AI automation workflows, specialized tools
- **Tools Setup:** Cursor, Windsurf, Claude Desktop, Wispr Flow, Docker, VS Code, Discord
- **Documentation Needs:** Glossaries, tutorials, SOPs
- **Video Tutorials:** 5-7 second tutorial videos using AI tools
- **Language Considerations:** Simplified language for non-native English speakers, multilingual support
- **Memory Techniques:** Repetition-based learning, spaced repetition
- **Progress Tracking:** Google Tasks integration, webhook triggers, milestones

#### Section 16: EMPLOYEE & TEAM CONTEXT
- **Employee Mentions:** Track all employee discussions
- **CV Processing:** Candidate evaluation and screening activities
- **Interview Coordination:** Interview scheduling and documentation
- **Onboarding Activities:** New employee setup and training
- **Performance Reviews:** Employee evaluation discussions

#### Section 3: ACTION ITEMS & TASKS
- **HR-Specific Tasks:**
  - Create job posting
  - Process CV
  - Schedule interview
  - Onboard new employee
  - Update employee directory
  - Create training material
  - Process candidate application

### Step 3: Generate HR Daily Activity Report

**File Location:** `/Nov25/HR Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**HR-Specific Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department: HR
   - Team size: 2 employees
   - Total recruitment activities
   - Total onboarding activities
   - CVs processed count
   - Interviews conducted count
   - Overall status

2. **Recruitment Activities**
   - Job postings created
   - CVs received and processed
   - Candidate screening activities
   - Interview scheduling and coordination
   - Candidate evaluation results

3. **Onboarding Activities**
   - New employees onboarded
   - Training programs conducted
   - Documentation created/updated
   - Tool setup activities
   - Progress tracking updates

4. **Employee Management**
   - Employee directory updates
   - Status changes
   - Performance review activities
   - HR documentation updates

5. **Metrics and Statistics**
   - CVs processed: [count]
   - Interviews scheduled: [count]
   - Interviews conducted: [count]
   - New hires: [count]
   - Onboarding completions: [count]
   - Average time to hire: [days]
   - Onboarding completion rate: [percentage]

6. **Key Deliverables**
   - Job postings created
   - CV processing reports
   - Interview documentation
   - Onboarding materials
   - Training guides
   - Employee directory updates

7. **HR Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Process improvements made
   - Benefits gained
   - Categories affected (Recruitment, Onboarding, Training, Management)

8. **Technical Achievements**
   - Documentation enhancements
   - Process improvements
   - Tool integrations
   - Template creation/updates

9. **Challenges and Solutions**
   - Recruitment challenges
   - Onboarding bottlenecks
   - Process improvements
   - Solutions implemented

10. **Files Created/Modified Summary**
    - New files created (with paths)
    - Modified files (with descriptions)
    - CV files processed
    - Documentation updates

11. **Recommendations for Follow-up**
    - Immediate actions required
    - Short-term improvements
    - Long-term enhancements

12. **Success Indicators**
    - Completed successfully (checkboxes)
    - Quality metrics (checkboxes)
    - Pending items

13. **Conclusion**
    - Summary of day's work
    - Key achievements recap
    - Impact assessment
    - Overall status

**Report Footer:**
```
---
**Report Generated:** [Date]
**Department:** HR
**Team Size:** 2
**Report Status:** Complete
---
*End of Report*
```

---

## HR-Specific Vocabulary

**Recruitment Terms:**
- CV/Resume processing
- Candidate screening
- Job posting
- Interview scheduling
- Candidate evaluation
- Offer letter
- Onboarding checklist

**Onboarding Terms:**
- Day 1 onboarding
- Foundation training
- Advanced training
- Tool setup
- Account creation
- Documentation review
- Progress tracking

**Employee Management Terms:**
- Employee directory
- Status updates
- Performance review
- HR documentation
- Employee profile

---

## HR-Specific Project Matching

When processing transcripts, automatically identify HR-related projects:

**HR Projects:**
- **Recruitment Platform** - Talent acquisition system
- **Onboarding Programs** - Training and onboarding workflows
- **Employee Directory** - Employee management system
- **CV Processing** - Candidate evaluation system

---

## HR-Specific Quality Standards

### Content Requirements
- ✅ All recruitment activities included
- ✅ All onboarding activities documented
- ✅ CV processing activities tracked
- ✅ Interview activities recorded
- ✅ Employee management updates noted
- ✅ Metrics and statistics calculated
- ✅ Impact analysis provided

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for statistics and metrics
- ✅ Bullet lists for achievements
- ✅ Checkboxes for completed items
- ✅ Consistent section structure
- ✅ Professional tone and language

---

## Example Usage

### Command to AI Assistant:

```
Process HR department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read HR prompt log: Dropbox/Nov25/HR Nov25/HR prompt log.md
2. Process any HR-related call transcripts using MAIN PROMPT v3.md framework
3. Create Reports/{DAY} folder in HR department
4. Generate detailed HR activity report following HR-specific template

Focus on:
- Recruitment activities (CVs, interviews, job postings)
- Onboarding activities (training, documentation, tool setup)
- Employee management (directory updates, status changes)
- HR-specific metrics and statistics
```

---

## Version History

**v1.0** - November 25, 2025
- Initial HR-specific prompt creation
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added HR-specific employees and context
- Customized report template for HR department

---

*Last Updated: November 25, 2025*
*Department: HR (Human Resources)*

