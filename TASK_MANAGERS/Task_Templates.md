# Task Templates Documentation
**Version:** 1.0  
**Last Updated:** November 25, 2025  
**Total Templates:** 2

---

## 📋 Overview

This document contains complete details for all Task Templates in the TASK_MANAGERS entity. Each template includes full specifications, steps, checklists, responsibilities, and cross-references.

**Quick Reference:** See [Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md) for ID and name index.

---

## TASK-TEMPLATE-001: Create Job Posting

**ID:** `TASK-TEMPLATE-001`  
**File:** `Task_Templates/Task-Template-007.json`  
**Status:** Active  
**Version:** 1.0  
**Created:** 2025-11-01  
**Last Updated:** 2025-11-01

### Basic Information

- **Task Name:** Create Job Posting for [Position]
- **Action:** Create
- **Object:** Job Posting
- **Context:** for [Position]
- **Department:** HR
- **Profession:** HR Manager
- **Estimated Duration:** 2 hours
- **Status:** Template

### Description

Create a new job posting for a specific position using standardized template and requirements.

### Responsibilities

**Primary Responsible:**
- HR Manager - Creates and manages the job posting process

**Accountable:**
- Hiring Manager - Approves final job posting

**Consulted:**
- Department Lead - Provides position requirements and expectations
- Finance Team - Validates compensation ranges

**Informed:**
- Recruitment Team - Notified when posting goes live
- Company Leadership - Aware of new position openings

### Dependencies

- Job template selected
- Position requirements defined
- Hiring manager assigned

### Tools Required

- Notion
- Google Docs
- CRM

### Success Criteria

- Job posting published on 3+ platforms
- All required fields completed
- Approved by hiring manager
- Posted to company website and LinkedIn

### Steps

1. **Select job template**
   - Tool: Notion
   - Responsibility: HR Manager
   - Placement: Notion - Job Templates
   - Duration: 5 minutes
   - Dependencies: None
   - Success Criteria: Template selected and opened

2. **Fill in position details**
   - Tool: Notion
   - Responsibility: HR Manager
   - Placement: Notion - Job Posting draft
   - Duration: 30 minutes
   - Dependencies: Step 1
   - Success Criteria: Title, description, and basic details completed

3. **Define skills and requirements**
   - Tool: Notion
   - Responsibility: HR Manager
   - Placement: Notion - Job Posting draft
   - Duration: 30 minutes
   - Dependencies: Step 2
   - Success Criteria: All required skills and experience levels specified

4. **Set compensation and benefits**
   - Tool: Notion
   - Responsibility: HR Manager
   - Placement: Notion - Job Posting draft
   - Duration: 15 minutes
   - Dependencies: Step 3
   - Success Criteria: Compensation range and benefits clearly stated

5. **Review and get approval**
   - Tool: Notion, Email
   - Responsibility: HR Manager
   - Placement: Notion - Job Posting draft, Email to hiring manager
   - Duration: 20 minutes
   - Dependencies: Step 4
   - Success Criteria: Approval received from hiring manager

6. **Publish to platforms**
   - Tool: Job Boards, Company Website, LinkedIn
   - Responsibility: HR Manager
   - Placement: Multiple platforms
   - Duration: 20 minutes
   - Dependencies: Step 5
   - Success Criteria: Posted to at least 3 platforms

### Checklist

- [ ] Job title clear and accurate
  - Guide: No generic titles, specific role
  - Required: Yes

- [ ] Required skills listed with proficiency levels
  - Guide: Minimum 5 skills, specify Junior/Mid/Senior
  - Required: Yes

- [ ] Compensation range included
  - Guide: Market rate research completed
  - Required: Yes

- [ ] Location and remote options specified
  - Guide: Clear work arrangement
  - Required: Yes

- [ ] Application deadline set
  - Guide: Reasonable timeframe, typically 2-4 weeks
  - Required: Yes

- [ ] Posted to correct platforms
  - Guide: At least 3 job boards, company website, LinkedIn
  - Required: Yes

### Tags

hr, recruitment, job_posting, template

### Cross-References

**Referenced In:**
- `../INDEX.md` - Listed in master index
- `../Task_Templates_Checklist-Item-003.md` - Index entry
- `../README.md` - Example in entity documentation
- `../../FILES.md` - File structure documentation
- `../../FILE_SYSTEM_MAP.md` - System map reference
- `../../../Guides/CRM_ENTITIES_LLM_TAXONOMY_GUIDE.md` - Task Template structure example
- `../../../Guides/DATA_EXTRACTION_PROMPT.md` - Extraction target
- `../../../AI_CONTEXT_PROMPT.md` - AI context example
- `../../../TAXONOMY_DEEP_DIVE_SUMMARY.md` - System overview
- `../../../Examples/TAXONOMY_IMPLEMENTATION_EXAMPLES.md` - Implementation guide
- `../../Entities/LIBRARIES/Actions/Creative_Actions.json` - Action reference
- `../../Entities/LIBRARIES/README.md` - Library integration example
- `../../Entities/SETTINGS/README.md` - Settings example

**Related Entities:**
- `../../Entities/JOBS/` - Job posting entity
- `../../Entities/TALENTS/` - Employee assignments
- `../../Entities/LIBRARIES/Actions/` - "Create" action definition
- `../../Entities/LIBRARIES/Objects/` - "Job Posting" object definition

---

## TASK-TEMPLATE-002: Send Follow-up Email to Old Clients

**ID:** `TASK-TEMPLATE-002`  
**File:** `Task_Templates/Task-Template-021.json`  
**Status:** Active  
**Version:** 1.0  
**Created:** 2025-11-01  
**Last Updated:** 2025-11-01

### Basic Information

- **Task Name:** Send Follow-up Email to old clients
- **Action:** Send
- **Object:** Follow-up Email
- **Context:** to old clients
- **Department:** Sales
- **Profession:** Sales Manager
- **Estimated Duration:** 4-5 hours for 50 emails
- **Status:** Template

### Description

Send personalized re-engagement emails to former clients (Ex_Clients) as part of old client re-engagement campaign. Target: 50 emails/day minimum.

### Responsibilities

**Primary Responsible:**
- Sales Manager - Executes email campaign and manages client responses

**Accountable:**
- Sales Director - Approves campaign strategy and messaging

**Consulted:**
- CRM Administrator - Provides client data and export support
- AI Assistant (Custom GPT) - Generates personalized email content
- Marketing Team - Reviews messaging alignment with brand

**Informed:**
- Sales Team - Aware of re-engagement efforts
- Customer Success - Notified of reactivated clients
- Finance Team - Tracks ROI metrics

### Dependencies

- CRM export completed
- Deep research completed
- Email templates prepared

### Tools Required

- CRM
- Email Platform (Gmail)
- Custom GPT (Email Generation)
- n8n (Optional automation)

### Success Criteria

- 50 emails sent per day minimum
- All emails personalized with research insights
- All emails logged in CRM
- 5-10% response rate expected
- 1-2% reactivation rate expected

### Expected Results

- **Response Rate:** 5-10%
- **Reactivation Rate:** 1-2%
- **ROI:** <$100 reactivation vs $1,000-3,000 new client acquisition

### Steps

1. **Export old client list from CRM**
   - Tool: CRM export function
   - Responsibility: Sales Manager
   - Placement: Excel/Google Sheets in Sales folder
   - Duration: 10 minutes
   - Dependencies: CRM access permissions
   - Success Criteria: All former clients (Ex_Clients status) exported with contact info

2. **Research current company status and pain points**
   - Tool: GPT/NotebookLM + web search
   - Responsibility: AI Assistant (automated) or Sales Manager
   - Placement: Research Notes document per company
   - Duration: 5-10 minutes per company (automated) or 15-20 minutes (manual)
   - Dependencies: Company website URL, LinkedIn profiles
   - Success Criteria: 2-3 sentence summary of current situation and potential needs

3. **Generate personalized email using research insights**
   - Tool: Custom GPT (email generation assistant)
   - Responsibility: Sales Manager
   - Placement: Email draft in email platform
   - Duration: 2-3 minutes per email (with AI assistance)
   - Dependencies: Research notes complete, email template selected
   - Success Criteria: Email references specific company details, pain points addressed

4. **Send personalized email from corporate account**
   - Tool: Email platform (Gmail)
   - Responsibility: Sales Manager
   - Placement: Sent folder, logged in CRM
   - Duration: 30 seconds per email
   - Dependencies: Email finalized and reviewed
   - Success Criteria: Email sent successfully, logged in CRM with date/status

5. **Monitor inbox for responses and categorize**
   - Tool: Email + CRM
   - Responsibility: Sales Manager
   - Placement: CRM pipeline, response tracking spreadsheet
   - Duration: 2-5 minutes per response
   - Dependencies: Email sent, monitoring system active
   - Success Criteria: All responses categorized (positive/negative/neutral), next steps assigned

6. **Send follow-up email if no response after 5-7 days**
   - Tool: Email automation (n8n) or manual
   - Responsibility: System (automated) or Sales Manager (manual)
   - Placement: Automated trigger or calendar reminder
   - Duration: Automated or 2-3 minutes manual
   - Dependencies: No response received within timeframe
   - Success Criteria: Follow-up sent, CRM updated with next follow-up date

### Checklist

- [ ] Email personalized with company-specific details
  - Guide: Reference recent company news, changes, or pain points
  - Required: Yes

- [ ] Email sent from corporate account only
  - Guide: Never use personal email for client communication
  - Required: Yes

- [ ] Email logged in CRM
  - Guide: Same day logging required, memory fades fast
  - Required: Yes

- [ ] Follow-up cadence scheduled
  - Guide: 5-7 day follow-up if no response
  - Required: Yes

- [ ] Minimum 50 emails sent
  - Guide: Daily minimum target
  - Required: Yes

### Tags

sales, re-engagement, email, old_clients, campaign

### Cross-References

**Referenced In:**
- `../INDEX.md` - Listed in master index
- `../Task_Templates_Checklist-Item-003.md` - Index entry
- `../README.md` - Example in entity documentation
- `../Workflows/Old_Client_Reengagement_Workflow.yaml` - Used in workflow WF-LIN-001
- `../../FILES.md` - File structure documentation
- `../../FILE_SYSTEM_MAP.md` - System map reference
- `../../Documentation/Tool_Usage_Organizational_Proposals.md` - Workflow reference
- `../../../Guides/DATA_EXTRACTION_PROMPT.md` - Extraction target
- `../../../Skills_Collection/skills_library.json` - Skills reference

**Related Entities:**
- `../../Entities/BUSINESSES/` - Old client re-engagement strategy
- `../../Entities/TALENTS/` - Sales Manager assignment
- `../../Entities/LIBRARIES/Actions/` - "Send" action definition
- `../../Entities/LIBRARIES/Objects/` - "Follow-up Email" object definition
- `../../Entities/LIBRARIES/Tools/Automation_Tools/n8n.json` - Automation tool
- `../Workflows/` - Related workflow definitions

**Related Workflows:**
- `WF-LIN-001` - Old Client Re-Engagement Campaign (uses this template)

---

## 📝 Adding New Templates

When creating a new Task Template:

1. **Assign ID:** Use format `TASK-TEMPLATE-[NEXT_NUMBER]` (sequential)
2. **Create JSON file** in `Task_Templates/` folder
3. **Add to Task_Templates.md** - Full details section
4. **Add to Task_Templates_Checklist-Item-003.md** - ID and name only
5. **Update INDEX.md** - Add to ID reference table
6. **Add cross-references** - Document where template is referenced
7. **Define responsibilities** - RACI model (Responsible, Accountable, Consulted, Informed)

### Required Fields for New Templates

- `template_id` - Unique ID (required)
- `task_name` - ACTION + OBJECT + CONTEXT format (required)
- `action` - From LIBRARIES/Actions (required)
- `object` - From LIBRARIES/Objects (required)
- `context` - Additional details (required)
- `description` - What the task accomplishes (required)
- `department` - Department name (required)
- `profession` - Role that performs this (required)
- `priority` - Critical/High/Medium/Low (required)
- `estimated_duration` - Time estimate (required)
- `status` - Template/Active/Deprecated (required)
- `responsibilities` - RACI model (required)
- `dependencies` - Prerequisites (required)
- `tools_required` - Tools needed (required)
- `success_criteria` - Completion metrics (required)
- `steps` - Step-by-step process (required)
- `checklist` - Quality assurance items (required)
- `tags` - Searchable tags (required)

---

**Last Updated:** November 25, 2025  
**Maintained By:** Framework Architecture Team
