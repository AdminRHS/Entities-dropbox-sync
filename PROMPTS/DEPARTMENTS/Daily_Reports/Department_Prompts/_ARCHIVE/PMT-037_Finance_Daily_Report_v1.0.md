# Finance Department - Daily Report Collection Prompt

## Purpose
This prompt is specifically designed for the **Finance Department** to process call transcriptions and generate daily activity reports. It combines the comprehensive call organization framework with Finance-specific context, employee directory, and daily report automation.

---

## Department Context: Finance

### Department Overview
**Mission:** Financial operations, accounting, bookkeeping, budget management
**Team Size:** 2 employees
**Key Responsibilities:**
- Month-end and year-end financial closing
- Invoice management and tracking
- Budget and expense tracking
- Bank reconciliation
- Exchange rate management
- Financial reporting and analytics
- Accounting file management

### Finance Department Employees

**Yelisieieva Daria** - Financial Analyst, Accountant | Ukraine | Status: Work

**Ponomarova Kateryna** - Financial Analyst, Accountant | Ukraine | Status: Work

### Finance-Specific Projects
- **Monthly Financial Closing** - Month-end accounting processes
- **Invoice Management** - Invoice tracking and reconciliation
- **Budget Tracking** - Expense monitoring and budget management
- **Financial Reporting** - Analytics and financial statements
- **Banking Operations** - Bank statement reconciliation
- **Exchange Rate Management** - Currency tracking and updates

### Finance-Specific Tools
- **Communication:** Discord, Gmail, Google Workspace
- **AI Tools:** ChatGPT, Claude (for documentation and analysis)
- **Financial Tools:** Accounting software, Excel/Google Sheets, CRM financial modules
- **Documentation:** Google Drive, Dropbox, accounting files
- **Banking:** Corporate bank accounts, online banking platforms

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
   - Folder organization (`/Finance 2025/Fin Nov25/Reports/{DAY}/`)
   - Metrics and statistics extraction

---

## Finance-Specific Instructions

### Step 1: Read Finance Employee Daily Files
Read daily files from both Finance employees:
- `Dropbox/Finance 2025/Fin Nov25/Yelisieieva Daria/{DAY}/daily.md`
- `Dropbox/Finance 2025/Fin Nov25/Yelisieieva Daria/{DAY}/plans.md`
- `Dropbox/Finance 2025/Fin Nov25/Yelisieieva Daria/{DAY}/task.md`
- `Dropbox/Finance 2025/Fin Nov25/Ponomarova Kateryna/{DAY}/daily.md`
- `Dropbox/Finance 2025/Fin Nov25/Ponomarova Kateryna/{DAY}/plans.md`
- `Dropbox/Finance 2025/Fin Nov25/Ponomarova Kateryna/{DAY}/task.md`

**Note:** If files are empty (0 bytes), note this in the report as "No activity documented"

### Step 2: Process Call Transcripts (if applicable)
When processing Finance-related call transcripts, focus on:

**Finance-Specific Sections to Emphasize:**

#### Section 3: ACTION ITEMS & TASKS
- **Finance-Specific Tasks:**
  - Month-end closing activities
  - Invoice processing and verification
  - Bank reconciliation
  - Exchange rate updates
  - Budget tracking and reporting
  - Financial file updates
  - Expense reconciliation
  - Document collection
  - XML file generation (for Polish accountants)

#### Section 5: KEY TOPICS DISCUSSED
- **Financial Operations:**
  - Accounting processes
  - Invoice management
  - Budget discussions
  - Banking operations
  - Expense tracking
  - Financial reporting
  - Currency management

#### Section 16: EMPLOYEE & TEAM CONTEXT
- **Employee Mentions:** Track all Finance team discussions
- **Cross-Department Coordination:** Document collection from other departments
- **Financial Workflow:** Month-end processes, accounting cycles

### Step 3: Generate Finance Daily Activity Report

**File Location:** `/Finance 2025/Fin Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md`

**Finance-Specific Report Sections:**

1. **Executive Summary**
   - Report period (date)
   - Department: Finance
   - Team size: 2 employees
   - Total transactions processed
   - Total invoices managed
   - Overall financial status
   - Critical financial activities

2. **Activity Timeline**
   - Chronological breakdown of financial activities
   - Employee-specific work (Yelisieieva Daria, Ponomarova Kateryna)
   - Key milestones (month-end closing, reconciliations, reports)

3. **Metrics and Statistics**
   - Invoices processed: [count]
   - Invoices verified: [count]
   - Bank statements reconciled: [count]
   - Exchange rates updated: [count]
   - Expenses tracked: [count]
   - Financial files updated: [count]
   - Documents collected: [count]
   - Outstanding invoices: [count]

4. **Key Deliverables**
   - Month-end closing completion
   - Invoice management updates
   - Bank reconciliation reports
   - Exchange rate updates (CRM, accounting files, bonus analytics)
   - Budget tracking updates
   - Financial file updates
   - XML files generated
   - Accounting reports created

5. **Finance Department Impact Analysis**
   - Impact level (Critical/High/Medium/Low)
   - Financial processes completed
   - Benefits gained (accuracy, efficiency, compliance)
   - Categories affected (Accounting, Invoicing, Banking, Reporting)

6. **Technical Achievements**
   - Accounting system updates
   - Process improvements
   - Formula verification and optimization
   - File organization improvements
   - Documentation enhancements

7. **Financial Operations Summary**
   - **Month-End Closing:** Status and completion percentage
   - **Invoice Management:** Sent, received, verified, outstanding
   - **Bank Reconciliation:** Statements processed, accounts reconciled
   - **Exchange Rate Management:** Rates updated, systems synchronized
   - **Budget Tracking:** Expenses monitored, budget status
   - **Document Management:** Files organized, archives updated

8. **Challenges and Solutions**
   - Missing invoices/documents
   - Reconciliation discrepancies
   - System issues
   - Cross-department coordination challenges
   - Solutions implemented
   - Process improvements

9. **Cross-Department Coordination**
   - Documents requested from departments
   - Financial information shared
   - Coordination with management
   - Support provided to other departments

10. **Files Created/Modified Summary**
    - New accounting files created (with paths)
    - Modified financial files (with descriptions)
    - Bank statements processed
    - Reports generated
    - Documentation updates

11. **Recommendations for Follow-up**
    - Immediate financial actions required
    - Missing documents to collect
    - Reconciliation items to resolve
    - Short-term process improvements
    - Long-term financial system enhancements

12. **Success Indicators**
    - [ ] Month-end closing completed on time
    - [ ] All invoices sent and tracked
    - [ ] Bank reconciliation completed
    - [ ] Exchange rates updated in all systems
    - [ ] Budget tracking current
    - [ ] No outstanding financial issues
    - [ ] All formulas verified and accurate
    - [ ] Financial files organized and updated

13. **Conclusion**
    - Summary of day's financial work
    - Key achievements recap
    - Financial status assessment
    - Overall department status

14. **Data Quality Note**
    - Note if any employee files were empty or had incomplete data
    - Example: "Note: Ponomarova Kateryna's daily files were empty (0 bytes) for this date"

**Report Footer:**
```
---
**Report Generated:** [Date]
**Department:** Finance
**Team Size:** 2
**Report Status:** Complete
---
*End of Report*
```

---

## Finance-Specific Vocabulary

**Accounting Terms:**
- Month-end closing
- Year-end closing
- Financial reconciliation
- Invoice verification
- Price list validation
- Bonus analytics
- Exchange rate updates
- Bank statements
- Expense tracking
- Formula verification

**Banking Terms:**
- Bank reconciliation
- Corporate account
- Statement processing
- Transaction verification
- Payment tracking

**Reporting Terms:**
- Financial analytics
- Budget tracking
- Expense reports
- Accounting files
- XML generation
- Financial statements

**Document Management:**
- Invoice collection
- Document verification
- File organization
- Archive management
- Accounting file structure

---

## Finance-Specific Project Matching

When processing transcripts, automatically identify Finance-related projects:

**Finance Projects:**
- **Monthly Financial Closing** - Month-end accounting processes
- **Invoice Management** - Tracking and verification
- **Budget Tracking** - Expense monitoring
- **Financial Reporting** - Analytics and statements
- **Banking Operations** - Reconciliation and management

---

## Finance-Specific Quality Standards

### Content Requirements
- ✅ All financial transactions documented
- ✅ All invoice activities tracked
- ✅ Bank reconciliation status included
- ✅ Exchange rate updates noted
- ✅ Budget tracking activities recorded
- ✅ Month-end closing progress documented
- ✅ Metrics and statistics calculated
- ✅ Impact analysis provided
- ✅ Data quality issues noted (empty files, missing data)

### Formatting Requirements
- ✅ Markdown format with proper headers
- ✅ Tables for financial statistics and metrics
- ✅ Bullet lists for transactions and achievements
- ✅ Checkboxes for completed financial tasks
- ✅ Consistent section structure
- ✅ Professional financial tone and language

---

## Example Usage

### Command to AI Assistant:

```
Process Finance department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read Finance employee daily files:
   - Yelisieieva Daria: Dropbox/Finance 2025/Fin Nov25/Yelisieieva Daria/{DAY}/daily.md, plans.md, task.md
   - Ponomarova Kateryna: Dropbox/Finance 2025/Fin Nov25/Ponomarova Kateryna/{DAY}/daily.md, plans.md, task.md
2. Process any Finance-related call transcripts using MAIN PROMPT v3.md framework
3. Create Reports/{DAY} folder in Finance department
4. Generate detailed Finance activity report following Finance-specific template

Focus on:
- Month-end closing activities and status
- Invoice management (sent, received, verified, outstanding)
- Bank reconciliation (statements processed, accounts balanced)
- Exchange rate updates (all systems synchronized)
- Budget tracking (expenses monitored, compliance checked)
- Document management (files organized, collected, verified)
- Financial metrics and statistics
- Note any empty files or missing data
```

---

## Version History

**v1.0** - November 5, 2025
- Initial Finance-specific prompt creation
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added Finance-specific employees and context
- Customized report template for Finance department
- Added data quality tracking for empty files

---

*Last Updated: November 5, 2025*
*Department: Finance*
