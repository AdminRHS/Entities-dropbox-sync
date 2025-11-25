# Sales Department - Daily Report Collection Prompt

## Purpose
This prompt is specifically designed for the **Sales Department** to process call transcriptions and generate daily activity reports. It combines the comprehensive call organization framework with Sales-specific context, employee directory, and daily report automation.

---

## Department Context: Sales

### Department Overview
**Mission:** B2B sales, client relationships, deal closure, pipeline management
**Team Size:** 1 employee
**Key Responsibilities:**
- B2B sales and client acquisition
- Client relationship management
- Sales pipeline management
- Deal closure and negotiation
- CRM management

### Sales Department Employees

**Kovalska Anastasiya** (ID: 45405) - Sales Manager, SMM Manager, Personal Assistant | Ukraine | @anastasia_kovalska | avkovalska23@gmail.com | Status: Work

**Pasichna Anastasiia** (ID: 88105) - Personal Assistant, Financial manager | Ukraine | @aabeeille | anastasiya.pasichnaya@gmail.com | Status: Available
*Note: Also listed as lead generator in some contexts*

### Sales-Specific Projects
- **B2B Lead Generation** - Prospecting and sales pipeline management
- **CRM System** - Customer Relationship Management
- **Client Management** - Client relationship and account management
- **Sales Pipeline** - Deal tracking and closure

### Sales-Specific Tools
- **CRM System** - Template-driven task and project management
- **Communication:** Discord, Gmail, Google Workspace, Notion, LinkedIn
- **AI Tools:** ChatGPT, Claude, Gemini (for sales content and communication)
- **Documentation:** Google Drive, Notion, RAC (Remote AI Context)

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
   - Folder organization (`/Nov25/Sales Nov25/Reports/{DAY}/`)
   - Metrics and statistics extraction

---

## Sales-Specific Instructions

### Step 1: Read Sales Prompt Log
Read the Sales department prompt log file:
- `Dropbox/Nov25/Sales Nov25/Sales prompt log.md`

### Step 2: Process Call Transcripts (if applicable)
When processing Sales-related call transcripts, focus on:

**Sales-Specific Sections to Emphasize:**

#### Section 17: LEAD GENERATION & SALES CONTEXT
- **Sales Process:**
  - Pipeline Stage: Prospecting/Qualification/Proposal/Negotiation/Closed Won/Closed Lost
  - Conversion Metrics: CTR, Conversion Rate, Win Rate
  - Objections: Objection handling strategies
  - Next Steps: Follow-up actions, proposals, demos

- **Client Management:**
  - Client relationships
  - Account management
  - Deal tracking
  - Contract negotiations

#### Section 3: ACTION ITEMS & TASKS
- **Sales-Specific Tasks:**
  - Contact client
  - Send proposal
  - Schedule demo
  - Follow up on deal
  - Update CRM
  - Close deal
  - Process contract

### Step 3: Generate Sales Daily Activity Report

**File Location:** `/Nov25/Sales Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**Sales-Specific Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department: Sales
   - Team size: 1 employee
   - Total client contacts
   - Total deals in pipeline
   - Total deals closed
   - Overall status

2. **Sales Activities**
   - Client contacts made
   - Proposals sent
   - Demos scheduled/conducted
   - Follow-ups completed
   - Meetings conducted
   - Negotiations in progress

3. **Pipeline Management**
   - Deals in pipeline
   - Pipeline stages distribution
   - Deal values
   - Conversion rates
   - Win/loss analysis

4. **Client Management**
   - New clients acquired
   - Existing client interactions
   - Account updates
   - Relationship building activities

5. **CRM Activities**
   - CRM updates
   - Data entry
   - Pipeline updates
   - Contact management
   - Deal tracking

6. **Metrics and Statistics**
   - Client contacts: [count]
   - Proposals sent: [count]
   - Demos conducted: [count]
   - Deals closed: [count]
   - Pipeline value: [amount]
   - Conversion rate: [percentage]
   - Win rate: [percentage]

7. **Key Deliverables**
   - Proposals created
   - Contracts processed
   - Client documentation
   - CRM updates
   - Sales reports

8. **Sales Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Revenue impact
   - Process improvements made
   - Categories affected (Pipeline, Clients, Deals, CRM)

9. **Technical Achievements**
   - CRM improvements
   - Process optimizations
   - Documentation enhancements
   - Tool integrations

10. **Challenges and Solutions**
    - Sales challenges
    - Objection handling
    - Process bottlenecks
    - Solutions implemented

11. **Files Created/Modified Summary**
    - Proposals created
    - Contracts processed
    - Client documentation
    - CRM updates
    - Sales reports

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
**Department:** Sales
**Team Size:** 1
**Report Status:** Complete
---
*End of Report*
```

---

## Sales-Specific Vocabulary

**Sales Terms:**
- BANT (Budget, Authority, Need, Timeline)
- MQL (AI Qualified Lead), SQL (Sales Qualified Lead)
- CAC (Customer Acquisition Cost), CTR (Click-Through Rate), ROI
- Pipeline, Sales Funnel
- Cold Calling/Email, Warm-up, Nurturing, Follow-up
- BDR (Business Development Rep), SDR (Sales Development Rep)
- ICP (Ideal Customer Profile), Buyer Persona, Decision Maker

**Pipeline Terms:**
- Prospecting
- Qualification
- Proposal
- Negotiation
- Closed Won
- Closed Lost

---

## Sales-Specific Project Matching

When processing transcripts, automatically identify Sales-related projects:

**Sales Projects:**
- **B2B Lead Generation** - Prospecting and sales pipeline
- **CRM System** - Customer Relationship Management
- **Client Management** - Client relationship system

---

## Sales-Specific Quality Standards

### Content Requirements
- ✅ All sales activities included
- ✅ All pipeline updates documented
- ✅ All client interactions tracked
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
Process Sales department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read Sales prompt log: Dropbox/Nov25/Sales Nov25/Sales prompt log.md
2. Process any Sales-related call transcripts using MAIN PROMPT v3.md framework
3. Create Reports/{DAY} folder in Sales department
4. Generate detailed Sales activity report following Sales-specific template

Focus on:
- Sales activities (contacts, proposals, demos)
- Pipeline management
- Client management
- CRM updates
- Sales metrics and conversion rates
```

---

## Version History

**v1.0** - November 25, 2025
- Initial Sales-specific prompt creation
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added Sales-specific employees and context
- Customized report template for Sales department

---

*Last Updated: November 25, 2025*
*Department: Sales*

