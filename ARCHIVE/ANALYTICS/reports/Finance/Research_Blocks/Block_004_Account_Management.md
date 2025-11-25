# Research Block 004: Account Subscription Management

**Block ID:** Block_004_Account_Management  
**Date:** 2025-11-21  
**Duration:** 2 hours  
**Status:** Complete  
**Researcher:** Finance Operations Team  
**Report ID:** RES-REP-FIN-004 (to be created)

---

## Research Questions

1. How are accounts and subscriptions tracked?
2. What is the subscription lifecycle?
3. How does it integrate with ENTITIES ACCOUNTS?
4. What automation opportunities exist?

---

## Scope

**What This Block Covers:**
- Account and subscription tracking patterns
- Subscription lifecycle management
- Integration with ENTITIES ACCOUNTS schema
- Tool mapping and department assignments
- Shared account handling
- Automation opportunities

**What This Block Excludes:**
- Implementation of automation (future work)
- Password management security (covered separately)
- Account usage analytics (future research block)

**Time Boundaries:**
- Start: 2025-11-21 16:00
- End: 2025-11-21 18:00
- Duration: 2 hours

---

## Methodology

**Data Sources:**
- `Finance 2025 - Copy/Fin Nov25/Public/AI_list.json` - Finance account data (72 accounts)
- `Finance 2025 - Copy/Fin_Dec25/02_account_subscription_mapping_results.yaml` - Account mapping analysis
- `Finance 2025 - Copy/Fin_Dec25/08_account_integration_schema_results.yaml` - Integration schema design
- `ENTITIES/ACCOUNTS/accounts_schema.json` - ENTITIES account schema
- `ENTITIES/LIBRARIES/Tools/` - Tool library for mapping

**Research Approach:**
- Analyze Finance account data structure
- Map accounts to ENTITIES ACCOUNTS schema
- Document subscription lifecycle
- Identify tool mapping patterns
- Assess department assignment patterns
- Document automation opportunities

**Tools Used:**
- JSON data analysis (AI_list.json)
- Schema comparison (Finance vs ENTITIES)
- Tool mapping analysis (35 Finance tools → ENTITIES LIBRARIES)

---

## Findings

### Key Findings

1. **Account Dataset Structure**
   - **Total Accounts:** 72 account records
   - **Unique Tools:** 35 different tools/services
   - **Payment Status:** 45 paid, 25 not paid, 1 free, 1 unknown
   - **Department Coverage:** 8 departments + 21 accounts with empty department field
   - **Shared Accounts:** 10+ shared accounts (admin@rh-s.com, dev@rh-s.com, etc.)

2. **Subscription Lifecycle**
   - **Payment Status Tracking:** Finance tracks paid/not paid/free status
   - **Payment Dates:** Paid date tracked (M/D/YYYY format)
   - **Expiry Dates:** Valid until date tracked (M/D/YYYY format)
   - **Renewal Pattern:** Monthly subscriptions (30-day cycles)
   - **Status Updates:** Manual updates in Finance JSON file

3. **Integration with ENTITIES ACCOUNTS**
   - **Current Status:** ⏳ No integration exists
   - **Tool Mapping:** 28/35 tools exist in ENTITIES LIBRARIES/Tools (80% coverage)
   - **Schema Gaps:** Missing subscription payment tracking, department assignments array
   - **Owner Mapping:** Many shared accounts need special handling

4. **Automation Opportunities**
   - ✅ Tool mapping automation (28/35 tools mapped)
   - ⏳ Subscription expiry alerts (automation needed)
   - ⏳ Payment status sync (automation needed)
   - ⏳ Department assignment normalization (automation needed)
   - ⏳ Account owner mapping (automation needed)

### Data Structure Analysis

**Finance Account Dataset Structure:**
- **Fields:** 8 fields (AI, Acc, col_3, Paid date, valid until, Department, Link, row_number)
- **Records:** 72 account records
- **Format:** JSON array
- **Update Frequency:** Manual updates when subscriptions change

**Account Fields:**
- **AI:** Tool name (e.g., "Cursor Pro", "GPT team")
- **Acc:** Account email/login (may include password)
- **col_3:** Payment status ("paid", "not paid", "free")
- **Paid date:** Payment date (M/D/YYYY format)
- **valid until:** Subscription expiry date (M/D/YYYY format)
- **Department:** Department assignment (can be comma-separated)
- **Link:** Tool/service website URL

**Integration Points:**
- **ENTITIES ACCOUNTS:** Account schema exists, needs subscription extension
- **ENTITIES LIBRARIES/Tools:** Tool mapping (28/35 tools verified)
- **ENTITIES TALENTS:** Owner mapping (email → employee_id)
- **Finance Employee Data:** Department mapping

**Transformation Needs:**
- **Account ID Generation:** Finance has no account_id → Generate ACC-XXX from email
- **Password Parsing:** Extract and encrypt passwords from Acc field
- **Payment Status Normalization:** Map Finance status to ENTITIES enum
- **Date Format Normalization:** M/D/YYYY → YYYY-MM-DD
- **Department Parsing:** Parse comma-separated departments to array
- **Tool Name Mapping:** Map Finance tool names to ENTITIES tool_id

### Architecture Analysis

**Current Architecture:**
- **Component 1:** Finance AI_list.json (source of truth for subscriptions)
  - Manual updates when subscriptions change
  - Tracks payment status and expiry dates
  - Department assignments (some multi-department)
  
- **Component 2:** ENTITIES ACCOUNTS Schema
  - Account structure exists
  - Missing subscription payment tracking
  - Missing department assignments array
  - Has tool_id reference to LIBRARIES/Tools
  
- **Component 3:** ENTITIES LIBRARIES/Tools
  - 28/35 Finance tools exist
  - 7 video generation tools need verification
  - Tool mapping table exists

**Integration Opportunities:**
- **Opportunity 1:** Auto-sync subscription status
  - Current: Manual updates in Finance JSON
  - Opportunity: Monthly sync Finance → ENTITIES
  - Benefit: Real-time subscription tracking
  
- **Opportunity 2:** Subscription expiry alerts
  - Current: No automated alerts
  - Opportunity: Alert 7 days before expiry
  - Benefit: Prevent service interruptions
  
- **Opportunity 3:** Department assignment normalization
  - Current: 21 accounts have empty department field
  - Opportunity: Auto-assign based on tool usage or owner
  - Benefit: Better account organization
  
- **Opportunity 4:** Shared account owner mapping
  - Current: Shared accounts (admin@rh-s.com) don't map to specific employee
  - Opportunity: Map to department head or create shared account group
  - Benefit: Clear ownership and responsibility

**Gaps Identified:**
- **Gap 1:** No subscription payment tracking in ENTITIES
  - Finance tracks payment_status, paid_date, expiry_date
  - ENTITIES has subscription_type and expiry_date but not payment tracking
  - Opportunity: Implement EXT-ACCOUNTS-001 subscription extension
  
- **Gap 2:** No multi-department support in ENTITIES
  - Finance allows comma-separated departments
  - ENTITIES has single department assignment
  - Opportunity: Implement EXT-ACCOUNTS-002 department assignments array
  
- **Gap 3:** Tool mapping incomplete
  - 7 video generation tools need verification
  - Some tools may need creation in ENTITIES LIBRARIES
  - Opportunity: Complete tool mapping and create missing tools
  
- **Gap 4:** Account owner mapping unclear
  - Many shared accounts don't map to specific employee
  - Owner assignment rules needed
  - Opportunity: Create owner mapping rules for shared accounts

### Subscription Lifecycle Analysis

**Current Lifecycle:**
```
Account Creation
    ↓
Subscription Purchase/Renewal
    ↓
Payment Status Update (paid/not paid)
    ↓
Paid Date Recorded
    ↓
Expiry Date Set (30 days from paid date)
    ↓
[Manual Monitoring]
    ↓
Expiry Alert (if manual check)
    ↓
Renewal or Expiration
```

**Proposed Automated Lifecycle:**
```
Account Creation (Finance JSON)
    ↓ [Auto-sync]
ENTITIES ACCOUNTS Created
    ↓
Subscription Purchase/Renewal
    ↓ [Auto-sync]
Payment Status Updated in ENTITIES
    ↓
Expiry Alert (7 days before)
    ↓
Renewal Reminder
    ↓ [Auto-sync]
Status Updated After Renewal
```

### Tool Mapping Analysis

**Tool Mapping Status:**
- **High Confidence Mappings:** 28 tools (80%)
  - Cursor Pro → Cursor.json
  - Claude Ai → Claude.json
  - GPT team → ChatGPT.json
  - Gemini → Gemini.json
  - Midjourney → Midjourney.json
  - Perplexity → Perplexity.json
  - And 22 more...
  
- **Medium Confidence Mappings:** 0 tools
  - All mapped tools have high confidence
  
- **Low Confidence/Unknown:** 7 tools (20%)
  - Runway (may be in Video Generation folder)
  - invideo AI (needs verification)
  - Hedra (needs verification)
  - Vozo AI (needs verification)
  - HeyGen (needs verification)
  - hailuoai.video/Hailo (needs verification)
  - Google cloud (AI) (may map to Google AI Studio)

**Tool Categories:**
- **AI Tools:** 20+ tools (majority)
- **Automation Tools:** Make.com, N8n
- **Video Generation:** 7 tools (need verification)
- **File Management:** Dropbox
- **Cloud Platforms:** Supabase, Huggingface, Google Cloud

### Department Assignment Analysis

**Department Distribution:**
- **AI:** 3 accounts
- **developers:** 6 accounts
- **financial_manager:** 6 accounts
- **designers:** 10 accounts
- **lead_generator:** 5 accounts
- **sales_manager:** 3 accounts
- **recruiter:** 5 accounts
- **videographers:** 5 accounts
- **multiple_departments:** 4 accounts (comma-separated)
- **empty_department:** 21 accounts (29% of total)

**Multi-Department Accounts:**
- 4 accounts have multiple departments (comma-separated)
- Example: "lead generator,sales manager,recruiter,developers,AI,financial manager,designers,videographers"
- Need array support in ENTITIES schema

**Department Normalization:**
- Finance uses lowercase plural (e.g., "designers", "developers")
- ENTITIES uses ISO codes (e.g., "DGN", "DEV")
- Mapping needed: Finance names → ENTITIES ISO codes

### Shared Account Analysis

**Shared Accounts Identified:**
- **admin@rh-s.com:** Multiple tools (Cursor Pro, GPT, etc.)
- **dev@rh-s.com:** Development tools
- **niko@rh-s.com:** Management tools
- **dd@rh-s.com:** Design tools
- And 6+ more shared accounts

**Owner Mapping Challenges:**
- Shared accounts don't map to specific employee
- Need owner assignment rules:
  - Option 1: Map to department head
  - Option 2: Create shared account group
  - Option 3: Assign to primary user

**Owner Mapping Rules:**
- **admin@rh-s.com:** Map to Finance department head or IT admin
- **dev@rh-s.com:** Map to Development department head
- **niko@rh-s.com:** Map to management/leadership
- **Department-specific:** Map to department head

---

## Integration Mapping

### Finance → ENTITIES ACCOUNTS Mapping

| Finance Field | ENTITIES Field | Transformation | Status |
|--------------|----------------|----------------|--------|
| AI (tool name) | tool_id | Map tool name → ENTITIES tool_id | ⏳ |
| Acc (email) | login | Parse email from Acc field | ⏳ |
| Acc (password) | password | Parse and encrypt password | ⏳ |
| col_3 (status) | subscription.payment_status | Normalize payment status | ⏳ |
| Paid date | subscription.paid_date | Convert M/D/YYYY → YYYY-MM-DD | ⏳ |
| valid until | subscription.expiry_date | Convert M/D/YYYY → YYYY-MM-DD | ⏳ |
| Department | department_assignments | Parse comma-separated → array | ⏳ |
| Link | document_link | Direct mapping | ⏳ |
| [Generated] | account_id | Generate ACC-XXX from email | ⏳ |
| [Mapped] | owner_id | Map email → employee_id | ⏳ |

**Note:** Requires EXT-ACCOUNTS-001 (Subscription) and EXT-ACCOUNTS-002 (Department Assignments)

### Subscription Status Mapping

| Finance Status | ENTITIES Status | Transformation | Notes |
|---------------|-----------------|----------------|-------|
| "paid" | "paid" | Direct mapping | 45 accounts |
| "not paid" | "not_paid" | Direct mapping | 25 accounts |
| "free" | "free" | Direct mapping | 1 account |
| "" (empty) | "not_paid" | Default mapping | 1 account |

### Department Mapping

| Finance Department | ENTITIES ISO Code | Transformation | Notes |
|-------------------|-------------------|----------------|-------|
| "AI" | "AIA" | Direct mapping | AI & Automation |
| "developers" | "DEV" | Direct mapping | Development |
| "financial_manager" | "FIN" | Direct mapping | Finance |
| "designers" | "DGN" | Direct mapping | Design |
| "lead_generator" | "LGN" | Direct mapping | Lead Generation |
| "sales_manager" | "SLS" | Direct mapping | Sales |
| "recruiter" | "HRM" | Direct mapping | Human Resources |
| "videographers" | "VID" | Direct mapping | Video Production |

---

## Recommendations

### Immediate Actions (Next 1-2 Weeks)
- [ ] **Complete tool mapping verification**
  - Verify 7 video generation tools in ENTITIES
  - Create missing tools in ENTITIES LIBRARIES if needed
  - Update tool mapping table
  
- [ ] **Create account owner mapping rules**
  - Document shared account owner assignment rules
  - Map shared accounts to department heads
  - Create owner mapping table
  
- [ ] **Design department assignment normalization**
  - Create Finance → ENTITIES department mapping table
  - Handle multi-department accounts (comma-separated parsing)
  - Assign departments to 21 empty department accounts

### Short-Term Actions (Next 30-90 Days)
- [ ] **Implement ENTITIES schema extensions**
  - Deploy EXT-ACCOUNTS-001 (Subscription Payment Tracking)
  - Deploy EXT-ACCOUNTS-002 (Department Assignments Array)
  - Update ENTITIES ACCOUNTS schema
  
- [ ] **Create Finance → ENTITIES sync script**
  - Implement account ID generation
  - Implement password parsing and encryption
  - Implement subscription status sync
  - Implement department assignment parsing
  - Create sync logs
  
- [ ] **Implement subscription expiry alerts**
  - Create alert system (7 days before expiry)
  - Email notifications for expiring subscriptions
  - Dashboard for subscription status overview

### Long-Term Actions (Beyond 3 Months)
- [ ] **Automate subscription lifecycle**
  - Auto-sync payment status updates
  - Auto-update expiry dates after renewal
  - Auto-assign departments based on usage
  - Create subscription analytics dashboard
  
- [ ] **Build account usage tracking**
  - Track account usage by employee
  - Track account usage by department
  - Optimize account allocation
  - Identify unused accounts

---

## Next Steps

**For Next Research Block:**
- Block 005: Department Structure Normalization
- Will reference account department assignments

**For Implementation:**
1. Complete tool mapping verification
2. Create account owner mapping rules
3. Implement ENTITIES schema extensions
4. Create Finance → ENTITIES sync script
5. Implement subscription expiry alerts
6. Deploy automation

---

## Related Research

**Related Blocks:**
- Block 003: Employee Data Integration Patterns (owner mapping)
- Block 005: Department Structure Normalization (department mapping)

**Related Reports:**
- `Finance 2025 - Copy/Fin_Dec25/02_account_subscription_mapping_results.yaml` - Account mapping
- `Finance 2025 - Copy/Fin_Dec25/08_account_integration_schema_results.yaml` - Integration schema

**Related Documentation:**
- `Finance 2025 - Copy/Fin Nov25/Public/AI_list.json` - Finance account data
- `ENTITIES/ACCOUNTS/accounts_schema.json` - ENTITIES account schema
- `ENTITIES/LIBRARIES/Tools/` - Tool library

---

## Notes

**Key Insights:**
- Account data is well-structured and ready for integration
- Tool mapping is 80% complete (28/35 tools)
- Subscription lifecycle is clear but manual
- Department assignments need normalization (21 empty, 4 multi-department)

**Integration Complexity:**
- **Low Complexity:** Tool mapping (mostly complete), department mapping (clear rules)
- **Medium Complexity:** Account ID generation, password parsing, subscription sync
- **High Complexity:** Shared account owner mapping, multi-department parsing

**Automation Potential:**
- **High:** Subscription status sync, expiry alerts
- **Medium:** Department assignment normalization, owner mapping
- **Low:** Account creation (requires human judgment)

**Risk Factors:**
- **Security Risk:** Password handling must be encrypted
- **Data Quality Risk:** 21 accounts with empty department field
- **Sync Failure Risk:** Need error handling for sync failures
- **Expiry Risk:** Manual monitoring risks service interruptions

---

**Block Status:** Complete  
**Completion Date:** 2025-11-21  
**Next Review:** After schema extensions implementation

