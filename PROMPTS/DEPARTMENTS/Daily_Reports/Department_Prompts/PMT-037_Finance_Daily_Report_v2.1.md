# PMT-037: Finance Department - Daily Report v2.1

**Prompt ID:** PMT-037
**Version:** 2.1
**Department:** Finance (FNC)
**Category:** Daily Report Generation
**Date:** 2025-11-19
**Status:** Active

---

## Purpose

Generate comprehensive daily activity reports for the **Finance Department** with TASK_MANAGERS entity integration, using token-efficient format and forward planning.

**v2.1 Updates:**
- ✅ TASK_MANAGERS entity integration
- ✅ Token-efficient format: `TST-###_Name`
- ✅ 10-section report schema
- ✅ Entity validation via PMT-070
- ✅ Operational work classification
- ✅ Next day plans, research, improvements

---

## Department Context: Finance

### Department Overview
- **Code:** FNC
- **Mission:** Financial operations, accounting, budgeting, financial reporting
- **Team Size:** 2 employees
- **Key Responsibilities:**
  - Financial operations and accounting
  - Invoice management and tracking
  - Budget and expense tracking
  - Bank reconciliation
  - Financial reporting and analytics

### Finance Department Employees

**Shyiko Viktoriia** (ID: 87598) - Accountant | Ukraine | @viktoriia_shy | shyikoviktoria1@gmail.com | Status: Full Project + Part Time

**[Additional Finance Staff]** - [Role] | [Location] | [Contact] | Status: [Status]

---

## Finance-Specific Projects (TASK_MANAGERS)

### Common Projects
**Note:** Finance work is primarily **Operational/Maintenance** (routine financial operations).

Occasional project work:
- **Automation Projects:** Financial process automation initiatives
- **System Improvements:** Accounting system upgrades or integrations
- **Analysis Projects:** Special financial analysis or reporting projects

### Activity Patterns
- **Month-End Closing:** Operational/Routine (monthly recurring)
- **Invoice Processing:** Operational/Routine (daily/weekly)
- **Bank Reconciliation:** Operational/Routine (daily/weekly)
- **Expense Tracking:** Operational/Routine (ongoing)
- **Financial Reporting:** Operational/Routine (weekly/monthly)
- **Budget Management:** Operational/Routine (monthly/quarterly)
- **System Improvements:** Map to project if significant, or Operational if minor
- **Audit Preparation:** Could be project-specific or Operational

### Entity Mapping Guidance
**Most finance activities are Operational/Maintenance:**
- Focus on operational excellence metrics
- Track routine task completion and accuracy
- Document process improvements even if not project-based
- Map to projects only when part of defined initiative

---

## Finance-Specific Tools

### Accounting Software
- **QuickBooks** - Primary accounting system
- **Xero** - Cloud accounting (if applicable)
- **FreshBooks** - Invoicing and expense tracking

### Banking & Payments
- **Online Banking Platforms** - Bank reconciliation
- **PayPal, Stripe** - Payment processing
- **Wire Transfer Systems** - International payments

### Spreadsheets & Analysis
- **Microsoft Excel** - Financial analysis and reporting
- **Google Sheets** - Collaborative financial tracking
- **Power BI / Tableau** - Financial dashboards (if applicable)

### Communication
- **Gmail, Slack** - Client and vendor communication
- **Google Drive** - Document storage

---

## Data Sources

### Input Files
1. **Finance Prompt Log:** `Dropbox/Nov25/Fin Nov25/Finance prompt log.md` (if exists)
2. **Employee Daily Files:** `Dropbox/Nov25/Fin Nov25/{Employee}/Week_{N}/{DAY}/daily.md`
3. **TASK_MANAGERS CSVs:** (Loaded via PMT-032)

### Output Location
```
Dropbox/Nov25/Fin Nov25/Reports/{DAY}/Daily_Activity_Report_Nov{DAY}_2025.md
```

---

## Report Generation Instructions

### Step 1: Load Entity Data
**Before processing**, ensure TASK_MANAGERS CSV files loaded (handled by PMT-032)

### Step 2: Read Finance Prompt Log
Read: `Dropbox/Nov25/Fin Nov25/Finance prompt log.md` (if exists) or employee daily files

### Step 3: Map Activities to Entities
**For each activity**, invoke PMT-070 entity mapping:

**Finance-Specific Mapping Guidelines:**
- **Month-end closing tasks** → Operational/Routine
- **Invoice processing** → Operational/Routine
- **Bank reconciliation** → Operational/Routine
- **Expense tracking** → Operational/Routine
- **Financial reports** → Operational/Routine
- **System improvements** → Project if part of initiative, or Operational if minor
- **Process automation** → Map to automation project if exists

**Expected Result:** 80-90% of activities will be Operational/Maintenance

### Step 4: Generate 10-Section Report
Follow REPORT_OUTPUT_SCHEMA_v2.1.md with Finance-specific customization.

---

## 10-Section Report Template

### SECTION 1: EXECUTIVE SUMMARY

```markdown
# Daily Activity Report - Finance Department (FNC)
**Date:** November {DAY}, 2025

## 1. EXECUTIVE SUMMARY

- **Report Date:** 2025-11-{DAY}
- **Department:** Finance (FNC)
- **Team Size:** 2 members
- **Total Activities:** [COUNT]
- **Projects Active:** [COUNT if any] (mostly Operational)
- **Tasks Completed:** [COUNT]
- **Tasks In Progress:** [COUNT]
- **Overall Status:** [On Track/At Risk/Blocked]
- **Key Achievements:**
  - [Financial operation completed accurately]
  - [Process improvement implemented]
  - [Deadline met or efficiency gained]
```

---

### SECTION 2: PROJECT CONTRIBUTIONS

```markdown
## 2. PROJECT CONTRIBUTIONS

### Operational/Maintenance (Primary Focus)
- **Activities:** [COUNT] tasks ([HOURS] hours)
- **Categories:**
  - Month-End Closing: [X hours]
  - Invoice Processing: [X hours]
  - Bank Reconciliation: [X hours]
  - Expense Tracking: [X hours]
  - Financial Reporting: [X hours]
  - Vendor/Client Communications: [X hours]
- **Operational Excellence:** [Achievement or metric]

### [Project Name] (If Applicable)
- **Role:** Lead / Support
- **Status:** Active
- **Progress Today:** [Description]
- **Tasks Completed:** [If any]
- **Timeline:** [Status]
```

**Note:** Finance department focuses on operational excellence rather than project-based work.

---

### SECTION 3: MILESTONE PROGRESS

```markdown
## 3. MILESTONE PROGRESS

### Month-End Closing (November 2025)
- **Progress:** X% → Y% (+Z%)
- **Tasks Completed Today:**
  - Reconciled 47 transactions ✅
  - Processed 15 vendor invoices ✅
  - Validated 3 client payments ✅
- **Tasks In Progress:** Final reconciliation review
- **Blockers:** [None or describe]
- **Timeline:** On track for Nov 30 completion
- **Accuracy:** 100% (0 discrepancies found)

### Quarterly Budget Review (Q4 2025) (If Applicable)
- **Progress:** X% → Y%
- **Tasks Completed Today:** [If any]
- **Timeline:** [Status]
```

**Note:** Milestones are often time-based (month-end, quarter-end) rather than project-based.

---

### SECTION 4: TASK SEQUENCES AND ENTITY MAPPING

```markdown
## 4. TASK SEQUENCES AND ENTITY MAPPING

### Activity 1: Month-end transaction reconciliation
- **Entity:** Operational/Maintenance
- **Category:** Financial Operations - Month-End Closing
- **Time:** 2.5 hours
- **Status:** Completed ✅
- **Priority:** High
- **Objective:** Reconcile all November transactions for accuracy
- **Actions Taken:**
  - Reviewed 47 transactions from bank statements
  - Matched transactions to accounting entries
  - Investigated 2 discrepancies (resolved)
  - Updated reconciliation report
- **Results:**
  - ✅ 47 transactions reconciled (100% accuracy)
  - ✅ 2 discrepancies identified and resolved
  - ✅ Reconciliation report updated
  - ✅ 0 outstanding issues
- **Impact:** Month-end closing 40% complete, on track for Nov 30

### Activity 2: Vendor invoice processing
- **Entity:** Operational/Maintenance
- **Category:** Financial Operations - Accounts Payable
- **Time:** 1.5 hours
- **Status:** Completed ✅
- **Priority:** High
- **Objective:** Process 15 vendor invoices for payment
- **Actions Taken:**
  - Received and verified 15 invoices
  - Matched invoices to purchase orders
  - Entered invoices into accounting system
  - Scheduled payments for Nov 22
- **Results:**
  - ✅ 15 invoices processed
  - ✅ 100% matched to POs
  - ✅ Payments scheduled
  - ✅ Vendors notified of payment dates
- **Impact:** Maintained vendor payment timeline, 0 late payments

### Activity 3: Bank reconciliation
- **Entity:** Operational/Maintenance
- **Category:** Financial Operations - Bank Reconciliation
- **Time:** 1 hour
- **Status:** Completed ✅
- **Priority:** High
- **Objective:** Daily bank reconciliation for checking account
- **Actions Taken:**
  - Downloaded bank transactions for Nov 19
  - Matched 23 transactions to accounting entries
  - Investigated 1 unmatched transaction (resolved)
  - Updated cash flow forecast
- **Results:**
  - ✅ 23 transactions reconciled
  - ✅ 1 unmatched transaction identified (transfer in transit)
  - ✅ 0 discrepancies
  - ✅ Cash flow forecast updated
- **Impact:** Real-time financial accuracy maintained

### Activity 4: Weekly expense report
- **Entity:** Operational/Maintenance
- **Category:** Financial Reporting
- **Time:** 0.5 hours
- **Status:** Completed ✅
- **Priority:** Medium
- **Objective:** Generate weekly expense report for management
- **Actions Taken:**
  - Compiled expense data from Nov 13-19
  - Categorized expenses by department
  - Created summary report with graphs
  - Sent report to management
- **Results:**
  - ✅ Weekly report completed
  - ✅ All departments included
  - ✅ Sent to management on schedule
- **Impact:** Management visibility into spending patterns
```

---

### SECTION 5: CROSS-DEPARTMENT COORDINATION

```markdown
## 5. CROSS-DEPARTMENT COORDINATION

### Expense Approval (Multiple Departments)
- **Departments:** All departments (expense submissions)
- **Our Role:** Expense validation and payment processing
- **Today's Activity:**
  - Processed 12 expense reimbursements
  - Validated receipts and approvals
  - Scheduled payments for Nov 22
- **Status:** All expenses processed, payments scheduled

### Vendor Payment Inquiry (From DEV)
- **From Department:** DEV (Development)
- **Request:** Status of vendor payment for software license
- **Response:** Payment scheduled for Nov 22, vendor notified
- **Status:** Resolved ✅

### Budget Variance Report (Outgoing to Management)
- **To:** Management Team
- **Deliverable:** Week 3 November budget vs. actual report
- **Context:** Weekly financial snapshot
- **Status:** Delivered on schedule
- **Key Findings:** [Summary of variances if significant]
```

**Note:** Finance coordinates with all departments on expenses, invoices, and budgets.

---

### SECTION 6: FINANCIAL OPERATIONS AND REPORTING

```markdown
## 6. FINANCIAL OPERATIONS AND REPORTING

### Month-End Closing Operations (November 2025)
- **Progress:** 40% complete (on track for Nov 30)
- **Completed Today:**
  - Reconciled 47 transactions (100% accuracy)
  - Processed 15 vendor invoices
  - Validated 3 client payments
  - Updated accounts receivable aging report
- **Remaining Tasks:**
  - Final bank reconciliation (Nov 29-30)
  - Month-end journal entries
  - Financial statements preparation
  - Management report generation

### Accounts Payable
- **Invoices Processed:** 15 (total value: $12,450)
- **Payments Scheduled:** Nov 22 payment run ($12,450)
- **Outstanding Invoices:** 3 (awaiting approval)
- **Vendor Communications:** 4 vendors notified of payment schedule

### Accounts Receivable
- **Client Payments Received:** 3 (total: $18,200)
- **Outstanding Invoices:** 8 (total: $34,500)
- **Payment Reminders Sent:** 5 (for overdue accounts)
- **Aging Report:** Updated for management review

### Bank Reconciliation
- **Accounts Reconciled:** 2 (Checking, Savings)
- **Transactions Matched:** 23
- **Discrepancies Found:** 0
- **Outstanding Items:** 1 (transfer in transit, resolved)
- **Cash Balance:** Accurate and current

### Financial Reporting
- **Weekly Expense Report:** Completed and sent to management
- **Budget vs. Actual Tracking:** Updated for Nov W3
- **Department Expense Breakdown:** Generated for all 10 departments
- **Cash Flow Forecast:** Updated with current data

### Process Improvements
- **Expense Reimbursement:** Reduced processing time from 24h to 8h (new checklist)
- **Invoice Matching:** Improved PO matching accuracy to 100%
```

---

### SECTION 7: NEXT DAY PLANS

```markdown
## 7. NEXT DAY PLANS

### Scheduled Activities (Nov {DAY+1}, 2025)

#### High Priority
1. **Continue Month-End Closing Operations**
   - **Category:** Month-End Closing
   - **Objective:** Process additional transactions, continue reconciliation
   - **Time Estimate:** 3 hours
   - **Expected Outcome:** Month-end closing 60% complete

2. **Process Client Invoices**
   - **Category:** Accounts Receivable
   - **Objective:** Generate and send 8 client invoices
   - **Time Estimate:** 2 hours
   - **Expected Outcome:** All November invoices sent (total: $42,500)

3. **Bank Reconciliation**
   - **Category:** Daily Operations
   - **Objective:** Reconcile Nov 20 banking transactions
   - **Time Estimate:** 1 hour
   - **Expected Outcome:** 0 discrepancies, cash flow current

#### Medium Priority
4. **Vendor Payment Run**
   - **Category:** Accounts Payable
   - **Objective:** Execute scheduled payments from yesterday
   - **Time Estimate:** 0.5 hours
   - **Expected Outcome:** $12,450 paid to 15 vendors

5. **Update Budget Tracker**
   - **Category:** Budget Management
   - **Objective:** Update November budget vs. actual for all departments
   - **Time Estimate:** 1 hour
   - **Expected Outcome:** Current budget status for month-end

#### Meetings & Coordination
- Finance team sync (9:00 AM, 15 min)
- Management budget review (2:00 PM, 30 min - if scheduled)

### Total Planned Time: 7.5 hours
```

---

### SECTION 8: RESEARCH NEEDED

```markdown
## 8. RESEARCH NEEDED

### High Priority Research

#### 1. Automated Invoice Processing Solutions
- **Context:** Manual invoice processing takes 15-20 hours/month
- **Research Questions:**
  - What invoice automation tools integrate with QuickBooks?
  - Can OCR reduce manual data entry time?
  - What's ROI for invoice automation software?
- **Resources Needed:**
  - Vendor demos (3-4 solutions)
  - Cost-benefit analysis
  - Integration requirements documentation
- **Timeline:** Research by Nov 27, recommendations by Dec 1
- **Owner:** Shyiko Viktoriia
- **Expected Impact:** 40-50% reduction in invoice processing time

#### 2. Financial Dashboard Tools
- **Context:** Manual reporting consumes 10% of time, need real-time visibility
- **Research Questions:**
  - Which dashboard tools work with QuickBooks?
  - Can we automate weekly/monthly reports?
  - What metrics should be on real-time dashboard?
- **Resources Needed:**
  - Power BI vs. Tableau comparison
  - QuickBooks API capabilities
  - Management dashboard preferences
- **Timeline:** Research by Dec 3, prototype by Dec 10
- **Owner:** Finance + AID collaboration
- **Expected Impact:** 10% time savings, better management visibility

### Medium Priority Research

#### 3. Expense Reimbursement Workflow Automation
- **Context:** Manual expense processing has 24-48h delay
- **Research Questions:**
  - What expense management tools integrate with accounting?
  - Can approval workflow be automated?
  - Mobile app for receipt capture?
- **Resources Needed:**
  - Expensify, Receipt Bank, Zoho Expense evaluation
  - Employee feedback on current process pain points
- **Timeline:** Research by Dec 5
- **Owner:** Finance + HR collaboration
- **Expected Impact:** 50% faster reimbursement processing
```

---

### SECTION 9: IMPROVEMENTS NEEDED

```markdown
## 9. IMPROVEMENTS NEEDED

### Process Improvements

#### 1. Invoice Approval Workflow
- **Current Issue:** Invoice approvals delayed 2-3 days, missing signatures
- **Proposed Improvement:**
  - Implement automated approval reminders
  - Create approval deadline policy (48h)
  - Add approval tracking dashboard
- **Priority:** High
- **Effort:** Medium (3 hours setup + policy communication)
- **Expected Benefit:** 50% faster approvals, zero missed deadlines
- **Owner:** Finance + Management
- **Implementation:** Policy by Nov 25, tracking by Nov 30

#### 2. Month-End Closing Checklist
- **Current Issue:** Month-end tasks sometimes missed or delayed
- **Proposed Improvement:**
  - Create comprehensive month-end checklist
  - Add task dependencies and deadlines
  - Implement progress tracking
- **Priority:** High
- **Effort:** Low (2 hours to create checklist)
- **Expected Benefit:** Zero missed tasks, predictable closing timeline
- **Owner:** Shyiko Viktoriia
- **Implementation:** Checklist by Nov 23 (for Nov month-end)

### Technical Improvements

#### 3. Bank Feed Automation
- **Current Issue:** Manual bank transaction downloads take 30 min/week
- **Proposed Improvement:**
  - Enable automatic bank feeds in QuickBooks
  - Set up transaction categorization rules
  - Implement daily auto-sync
- **Priority:** Medium
- **Effort:** Medium (4 hours setup + testing)
- **Expected Benefit:** 2 hours/month time savings, faster reconciliation
- **Owner:** Finance + IT support
- **Implementation:** Setup by Nov 28

#### 4. Vendor Payment Scheduling System
- **Current Issue:** Manual payment scheduling, risk of missing payment dates
- **Proposed Improvement:**
  - Create automated payment schedule based on terms
  - Add payment reminder notifications
  - Implement early payment discount tracking
- **Priority:** Medium
- **Effort:** Medium (3 hours)
- **Expected Benefit:** Zero late payments, capture more early payment discounts
- **Owner:** Shyiko Viktoriia
- **Implementation:** System by Dec 2

### Documentation Improvements

#### 5. Financial Process Documentation
- **Current Issue:** Processes exist in one person's knowledge only
- **Proposed Improvement:**
  - Document all monthly/quarterly/annual processes
  - Create step-by-step guides with screenshots
  - Build knowledge base for cross-training
- **Priority:** High
- **Effort:** High (12 hours total)
- **Expected Benefit:** Business continuity, easier onboarding, backup coverage
- **Owner:** Finance team
- **Implementation:** Start Nov 24, complete by Dec 15 (1 hour/day)
```

---

### SECTION 10: METRICS AND DELIVERABLES

```markdown
## 10. METRICS AND DELIVERABLES

### Time Allocation
| Category | Hours | Percentage |
|----------|-------|------------|
| Month-End Operations | 2.5 | 42% |
| Invoice Processing | 1.5 | 25% |
| Bank Reconciliation | 1.0 | 17% |
| Reporting | 0.5 | 8% |
| Communications | 0.5 | 8% |
| **Total** | **6.0** | **100%** |

### Task Distribution by Category
| Category | Count | Hours |
|----------|-------|-------|
| Accounts Payable | 2 | 1.5 |
| Accounts Receivable | 1 | 0.3 |
| Bank Reconciliation | 1 | 1.0 |
| Month-End Closing | 3 | 2.5 |
| Reporting | 1 | 0.5 |
| Communications | 2 | 0.2 |

### Operational Metrics
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Transactions Reconciled | 47 | 45+ | ✅ Above Target |
| Reconciliation Accuracy | 100% | 100% | ✅ Met |
| Invoices Processed | 15 | 12+ | ✅ Above Target |
| Invoice Processing Time | 6 min/invoice | <10 min | ✅ Excellent |
| Bank Discrepancies | 0 | 0 | ✅ Perfect |
| Payment Delays | 0 | 0 | ✅ Perfect |

### Financial Activity Summary
| Activity | Count | Total Value |
|----------|-------|-------------|
| Vendor Invoices Processed | 15 | $12,450 |
| Client Payments Received | 3 | $18,200 |
| Expense Reimbursements | 12 | $3,240 |
| Payments Scheduled | 15 | $12,450 |

### Files Created/Modified

#### New Files (3)
1. `Reports/Week_3/Weekly_Expense_Report_Nov13-19.pdf`
2. `Reports/Week_3/Department_Expense_Breakdown_Nov.xlsx`
3. `Month_End/Nov_Reconciliation_Progress.xlsx`

#### Modified Files (4)
1. `Accounting/Transaction_Log_Nov2025.xlsx` (47 transactions added)
2. `Accounts_Payable/Vendor_Invoice_Tracker.xlsx` (15 invoices processed)
3. `Accounts_Receivable/AR_Aging_Report.xlsx` (Updated with 3 payments)
4. `Budget/Budget_vs_Actual_Nov2025.xlsx` (Week 3 updated)

### Key Deliverables Status
- ✅ Month-End Closing (40% complete, on track)
- ✅ All vendor invoices processed on time
- ✅ Bank reconciliation (100% accurate)
- ✅ Weekly expense report (delivered to management)
- ✅ Zero payment delays
- ✅ Zero reconciliation discrepancies

### Challenges Encountered

#### Challenge 1: Transaction Discrepancy Investigation
- **Problem:** 2 transactions didn't match bank statement initially
- **Solution:** Investigated transaction history, found timing difference (one posted next day)
- **Result:** Both transactions reconciled correctly, 0 actual discrepancies
- **Status:** Resolved ✅

#### Challenge 2: Vendor Invoice Missing PO Number
- **Problem:** 1 vendor invoice lacked PO number for matching
- **Solution:** Contacted procurement, obtained PO number, verified delivery
- **Result:** Invoice matched and processed correctly
- **Status:** Resolved ✅
```

---

## Report Footer

```markdown
---

## Report Metadata

**Report Generated:** November {DAY}, 2025 18:00
**Department:** Finance (FNC)
**Team Size:** 2
**Report Version:** v2.1
**Schema Version:** 10-Section Format
**Entity Integration:** Enabled ✅ (Operational Focus)
**Report Status:** Complete

---

## Summary Statistics

- **Total Activities:** 8 (100% operational)
- **Total Time:** 6.0 hours
- **Operational Excellence:** 100% accuracy across all activities
- **Transactions Processed:** 47 reconciled, 15 invoices
- **Financial Accuracy:** 0 discrepancies
- **Deliverables Created:** 3 reports
- **Next Day Plans:** 5 activities (7.5 hours planned)
- **Research Items:** 3 (2 high priority - automation focus)
- **Improvements Identified:** 5 (3 high priority - workflow efficiency)

---

*End of Daily Activity Report*

**Next Report:** November {DAY+1}, 2025
**Prepared By:** AI Assistant via PMT-032 v2.1
**Entity Mapping:** PMT-070 v2.1

---
```

---

## Finance-Specific Vocabulary

### Financial Terms
- **Reconciliation:** Matching transactions to accounting records
- **Accounts Payable (AP):** Money owed to vendors
- **Accounts Receivable (AR):** Money owed by clients
- **General Ledger (GL):** Complete accounting record
- **Journal Entry:** Accounting transaction record
- **Chart of Accounts:** Organized list of all accounts

### Operations Terms
- **Month-End Closing:** Final accounting for the month
- **Aging Report:** Receivables/payables by age
- **Cash Flow:** Money in and out
- **Budget vs. Actual:** Planned vs. real spending
- **PO (Purchase Order):** Authorization to purchase

### Metrics
- **Accuracy:** Percentage of error-free transactions
- **Processing Time:** Time to complete task
- **Discrepancy Rate:** Percentage of unmatched items
- **Days Outstanding:** How long invoice unpaid

---

## Finance-Specific Quality Standards

### Content Requirements
- ✅ All 10 sections populated
- ✅ Operational excellence metrics included
- ✅ Financial accuracy documented (discrepancies, errors)
- ✅ Transaction volumes and values tracked
- ✅ Month-end/quarter-end progress noted
- ✅ Process improvements documented
- ✅ Mostly Operational/Maintenance entity classification

### Operational Excellence Focus
- ✅ Accuracy percentages (target: 100%)
- ✅ Processing time efficiency
- ✅ Zero discrepancies goal
- ✅ On-time completion tracking
- ✅ Process improvement initiatives

### Formatting Requirements
- ✅ Financial values formatted consistently ($X,XXX)
- ✅ Transaction counts clearly stated
- ✅ Accuracy metrics prominent
- ✅ Operational categories organized

---

## Example Command

```
Generate Finance department daily activity report for November 19, 2025.

Use PMT-037 v2.1:

1. Read Finance prompt log or employee daily files
2. Map activities (expect 80-90% Operational/Maintenance)
3. Focus on:
   - Month-end closing operations
   - Invoice and payment processing
   - Bank reconciliation accuracy
   - Financial reporting
   - Operational excellence metrics
4. Include next day plans (month-end tasks)
5. Research automation opportunities
6. Save to: Dropbox/Nov25/Fin Nov25/Reports/19/Daily_Activity_Report_Nov19_2025.md
```

---

## Version History

**v2.1** (2025-11-19)
- ✅ Added TASK_MANAGERS entity integration (Operational focus)
- ✅ Implemented 10-section schema
- ✅ Enhanced operational excellence tracking
- ✅ Added automation research focus
- ✅ Added financial accuracy metrics

**v1.0** (2025-11-05)
- Initial Finance-specific prompt

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Last Updated:** 2025-11-19

---

*End of Prompt*
