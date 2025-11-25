# Research Block 002: Bonus Analytics Architecture

**Block ID:** Block_002_Bonus_Analytics  
**Date:** 2025-11-21  
**Duration:** 2 hours  
**Status:** Complete  
**Researcher:** Finance Operations Team  
**Report ID:** RES-REP-FIN-002 (to be created)

---

## Research Questions

1. How does the bonus analytics dashboard system work?
2. What is the data flow from source to visualization?
3. How can it integrate with ENTITIES ANALYTICS?
4. What transformation rules are needed?

---

## Scope

**What This Block Covers:**
- Bonus analytics dashboard architecture
- Data flow from Excel to CSV to HTML dashboard
- Integration opportunities with ENTITIES ANALYTICS
- Transformation rules and calculation formulas
- Monthly workflow and automation potential

**What This Block Excludes:**
- Implementation of ENTITIES integration (future work)
- Dashboard UI/UX improvements (out of scope)
- Historical data migration (future research block)

**Time Boundaries:**
- Start: 2025-11-21 12:00
- End: 2025-11-21 14:00
- Duration: 2 hours

---

## Methodology

**Data Sources:**
- `Projects Eliseeva/Bonuses/Technical documentation/` - Complete technical documentation
- `Projects Eliseeva/Bonuses/Bonuses Lib 2025.xlsx` - Master Excel data file
- `Projects Eliseeva/Bonuses/Bonuses Analytics 2025 - Total.csv` - Aggregated analytics
- `Projects Eliseeva/Bonuses/Bonuses Analytics 2025 - Finance.csv` - Financial analytics
- `Projects Eliseeva/Bonuses/dashboards/` - Monthly HTML dashboards
- `Finance 2025 - Copy/Fin_Dec25/04_finance_schema_analysis_results.yaml` - Finance schema analysis

**Research Approach:**
- Analyze dashboard architecture and components
- Map data flow from source to visualization
- Identify integration points with ENTITIES ANALYTICS
- Document transformation rules and calculations
- Assess automation opportunities

**Tools Used:**
- Documentation analysis (technical docs, workflow guides)
- Data structure analysis (Excel tabs, CSV formats)
- Architecture mapping (component relationships)

---

## Findings

### Key Findings

1. **Dashboard Architecture**
   - **Data Sources:** Multi-tab Excel file (15+ tabs) → Aggregated CSV files → HTML dashboards
   - **Components:** Dashboard hub (index.html), monthly dashboards, interactive breakdowns
   - **Technology:** HTML5/CSS3/JavaScript, Chart.js 3.9.1, GitHub Pages hosting
   - **Update Frequency:** Monthly (Days 1-10 of new month)

2. **Data Flow Architecture**
   ```
   Department Reports (HR, Sales, Finance, Operations)
       ↓
   Bonuses Lib 2025.xlsx (Master Excel - 15+ tabs)
       ↓
   CSV Export (Bonuses Analytics 2025 - Total.csv, Finance.csv)
       ↓
   Claude Artifacts (Dashboard Generation)
       ↓
   HTML Dashboard (Self-contained, embedded CSS/JS)
       ↓
   GitHub Pages (Public hosting)
   ```

3. **Integration with ENTITIES ANALYTICS**
   - **Current Status:** ⏳ No integration exists
   - **Opportunity:** Map bonus metrics to ENTITIES ANALYTICS financial schema
   - **Target Schema:** `ENTITIES/ANALYTICS/Financial/{period}.json`
   - **Integration Points:** Department financials, project financials, employee financials

4. **Transformation Rules**
   - **Excel → CSV:** Manual export process (automation opportunity)
   - **CSV → Dashboard:** Claude Artifacts generation (semi-automated)
   - **Calculations:** Excel formulas → CSV aggregation → Dashboard visualization
   - **Currency:** Mixed ₴ (UAH) and $ (USD) - normalization needed

### Data Structure Analysis

**Master Excel File Structure:**
- **Tabs:** 15+ functional tabs (HR, HRVideo, Calls, Sales, Fired, Finance, etc.)
- **Fields:** 200+ fields across all tabs
- **Update Frequency:** Monthly (Finance tab: 3x per month)
- **Format:** Excel .xlsx with formulas and calculations

**CSV Analytics Files:**
- **Bonuses Analytics 2025 - Total.csv:** Aggregated monthly metrics
  - HR metrics (hired, started, salaries, costs)
  - Employee turnover (departures, fired, voluntary)
  - Call activities (total calls, leadgen, conversions)
  - Sales performance (companies, revenue, profits)
  - Financial overview (revenue, balance, cash, pending)
  
- **Bonuses Analytics 2025 - Finance.csv:** Financial-specific analytics
  - Revenue tracking
  - Payment receipts
  - Salary accruals and payments
  - Expense tracking
  - Balance calculations
  - Cash position
  - Pending invoices

**Integration Points:**
- **Finance CSV:** Employee data → Bonus calculations
- **ENTITIES TALENTS:** Employee profiles → Bonus attribution
- **ENTITIES ANALYTICS:** Financial metrics → Analytics storage
- **Finance RH Dashboard:** Related financial dashboard system

**Transformation Needs:**
- **Excel Export:** Manual process → Automation needed
- **Currency Normalization:** Mixed ₴/$ → Standardize to USD with local tracking
- **Date Formats:** Excel dates → ISO YYYY-MM-DD format
- **Department Mapping:** Excel department names → ENTITIES ISO codes
- **Employee ID Mapping:** Excel numeric IDs → ENTITIES EMP-YYYY-XXX format

### Architecture Analysis

**Current Architecture:**
- **Component 1:** Master Excel File (Bonuses Lib 2025.xlsx)
  - Source of truth for all operational data
  - Contains formulas and calculations
  - Updated monthly by departments
  
- **Component 2:** CSV Export Files
  - Aggregated analytics (Total.csv, Finance.csv)
  - Manual export process
  - Used for dashboard generation
  
- **Component 3:** Dashboard Generation (Claude Artifacts)
  - Semi-automated process using AI
  - Uses previous month's dashboard as template
  - Generates self-contained HTML files
  
- **Component 4:** Dashboard Hub (index.html)
  - Central navigation interface
  - Links to all monthly dashboards
  - Hosted on GitHub Pages
  
- **Component 5:** Monthly Dashboards (HTML files)
  - Self-contained HTML with embedded CSS/JS
  - Interactive charts using Chart.js
  - Month-over-month comparisons

**Integration Opportunities:**
- **Opportunity 1:** Auto-export Excel to CSV
  - Current: Manual export process
  - Opportunity: Python script to automate CSV generation
  - Benefit: Reduce manual work, ensure consistency
  
- **Opportunity 2:** Integrate with ENTITIES ANALYTICS
  - Current: No integration
  - Opportunity: Map bonus metrics to ENTITIES financial schema
  - Benefit: Unified analytics, cross-system reporting
  
- **Opportunity 3:** Link bonus data to employee profiles
  - Current: Bonus data separate from employee profiles
  - Opportunity: Link bonuses to ENTITIES TALENTS employee records
  - Benefit: Complete employee financial picture
  
- **Opportunity 4:** Automate dashboard generation
  - Current: Semi-automated via Claude Artifacts
  - Opportunity: Full automation with Python/JavaScript
  - Benefit: Faster dashboard creation, reduced errors

**Gaps Identified:**
- **Gap 1:** No automated Excel → CSV export
  - Manual process prone to errors
  - Opportunity: Python script with openpyxl library
  
- **Gap 2:** No integration with ENTITIES ANALYTICS
  - Bonus metrics isolated from ENTITIES system
  - Opportunity: Map to ENTITIES financial schema
  
- **Gap 3:** Currency normalization needed
  - Mixed ₴ and $ throughout system
  - Opportunity: Standardize to USD with conversion tracking
  
- **Gap 4:** Employee ID format mismatch
  - Excel uses numeric IDs, ENTITIES uses EMP-YYYY-XXX
  - Opportunity: ID mapping table for integration

---

## Data Flow Analysis

### Phase 1: Data Collection (Days 1-3)
```
Department Reports
    ↓
Manual Entry into Excel Tabs
    ↓
Excel Formula Calculations
    ↓
Data Validation
```

### Phase 2: Data Export (Days 4-7)
```
Bonuses Lib 2025.xlsx
    ↓ (Manual Export)
Bonuses Analytics 2025 - Total.csv
Bonuses Analytics 2025 - Finance.csv
    ↓
Data Verification
```

### Phase 3: Dashboard Generation (Days 7-10)
```
CSV Files + Previous Dashboard Template
    ↓ (Claude Artifacts)
HTML Dashboard Generation
    ↓
Quality Check
    ↓
GitHub Pages Deployment
```

### Proposed Integration Flow
```
Bonuses Lib 2025.xlsx
    ↓ (Automated Export Script)
CSV Files
    ↓ (Transformation Script)
ENTITIES ANALYTICS/Financial/{period}.json
    ↓
ENTITIES ANALYTICS Dashboard
```

---

## Integration Mapping

### Bonus Metrics → ENTITIES ANALYTICS Schema

| Bonus Metric | ENTITIES Field | Transformation | Status |
|-------------|----------------|----------------|--------|
| Department Salaries | department_financials.department_salaries.total_salary_usd | Sum by department, convert ₴→$ | ⏳ |
| Department Bonuses | department_financials.department_bonuses.total_bonus_usd | Sum by department, convert ₴→$ | ⏳ |
| Project Revenue | project_financials.project_revenue.total_revenue_usd | Map to project ID | ⏳ |
| Employee Bonuses | employee_financials.bonuses.total_bonus_usd | Map to employee ID | ⏳ |
| HR Costs | department_financials.HRM.total_costs_usd | Convert ₴→$ | ⏳ |
| Sales Revenue | project_financials.sales.total_revenue_usd | Direct mapping | ⏳ |

**Note:** Requires ENTITIES ANALYTICS financial schema extension (see Fin_Dec25 analysis)

### Calculation Formulas Mapping

**Excel Formulas → ENTITIES Calculations:**
- **Cost per Employee:** `(HR Salaries + HR Ads) / Started Count` → ENTITIES aggregation
- **Lead Price:** `(LeadGen Salaries + Call Bonuses) / Total Calls` → ENTITIES calculation
- **Profit Project:** `Revenue - USD Employee Salary` → ENTITIES calculation
- **Turnover Rate:** `Departures / Total Employees` → ENTITIES calculation

---

## Recommendations

### Immediate Actions (Next 1-2 Weeks)
- [ ] **Create Excel → CSV export script**
  - Use Python with openpyxl library
  - Automate CSV generation from Excel tabs
  - Validate data during export
  
- [ ] **Document calculation formulas**
  - Extract all Excel formulas
  - Document transformation rules
  - Create formula reference guide
  
- [ ] **Design ENTITIES integration schema**
  - Map bonus metrics to ENTITIES ANALYTICS schema
  - Design transformation rules
  - Create integration specification

### Short-Term Actions (Next 30-90 Days)
- [ ] **Implement ENTITIES ANALYTICS integration**
  - Create transformation script (Excel → ENTITIES)
  - Implement currency normalization (₴ → USD)
  - Map employee IDs (numeric → EMP-YYYY-XXX)
  - Deploy monthly sync process
  
- [ ] **Automate dashboard generation**
  - Create Python script for dashboard generation
  - Use template-based approach
  - Integrate with CSV export script
  
- [ ] **Create bonus → employee profile links**
  - Link bonus data to ENTITIES TALENTS employee records
  - Add bonus history to employee profiles
  - Enable employee-level bonus analytics

### Long-Term Actions (Beyond 3 Months)
- [ ] **Build unified analytics dashboard**
  - Combine bonus analytics with ENTITIES ANALYTICS
  - Create cross-system reporting
  - Enable real-time analytics
  
- [ ] **Implement predictive analytics**
  - Use historical bonus data for forecasting
  - Predict bonus costs
  - Optimize bonus structures

---

## Next Steps

**For Next Research Block:**
- Block 003: Employee Data Integration Patterns
- Will reference bonus data integration with employee profiles

**For Implementation:**
1. Create Excel → CSV export automation script
2. Design ENTITIES ANALYTICS integration schema
3. Implement currency normalization
4. Create employee ID mapping for bonuses
5. Build transformation pipeline

---

## Related Research

**Related Blocks:**
- Block 001: Attendance Dataset Analysis (employee data integration)
- Block 003: Employee Data Integration Patterns (will reference bonus integration)

**Related Reports:**
- `Finance 2025 - Copy/Fin_Dec25/04_finance_schema_analysis_results.yaml` - Finance schema
- `Finance 2025 - Copy/Review/Phase3_Integration_Design/09_financial_analytics_schema.yaml` - Analytics schema

**Related Documentation:**
- `Projects Eliseeva/Bonuses/Technical documentation/` - Complete technical docs
- `Projects Eliseeva/Bonuses/Technical documentation/DATA_STRUCTURE.md` - Data structure
- `Projects Eliseeva/Bonuses/Technical documentation/DASHBOARD_WORKFLOW.md` - Workflow guide

---

## Notes

**Key Insights:**
- Bonus analytics system is well-documented and structured
- Main integration challenge is Excel → CSV automation and ENTITIES mapping
- Currency normalization (₴ → USD) is critical for integration
- Employee ID mapping needed for linking bonuses to employee profiles

**Architecture Strengths:**
- Clear data flow from source to visualization
- Well-documented technical architecture
- Modular design (Excel → CSV → Dashboard)
- Good separation of concerns

**Integration Complexity:**
- **Low Complexity:** CSV export automation, dashboard generation
- **Medium Complexity:** ENTITIES schema mapping, currency normalization
- **High Complexity:** Real-time integration, predictive analytics

**Automation Potential:**
- **High:** Excel → CSV export (straightforward automation)
- **Medium:** Dashboard generation (template-based automation)
- **Low:** Data entry (requires human judgment)

---

**Block Status:** Complete  
**Completion Date:** 2025-11-21  
**Next Review:** After implementation of Excel → CSV automation

