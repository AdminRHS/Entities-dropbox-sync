# HR Operations Prompts

**Entity Type:** LIBRARIES
**Sub-Entity:** Prompts
**Category:** HR_Operations
**Purpose:** AI instruction prompts for HR recruitment workflow automation
**Created:** 2025-11-14
**Version:** 1.0

---

## Overview

This directory contains AI instruction prompts specifically designed for the HR department's recruitment workflow at Remote Employees company. These prompts guide AI assistants through standardized processes for:

- **Candidate Communication:** Professional messaging templates and pre-screening
- **Resume Processing:** AI-powered parsing and CRM data entry
- **Interview Management:** Conducting interviews, evaluations, and post-interview processes
- **Contract & Onboarding:** Regular contract processing and employee onboarding

---

## Prompts in This Directory

### 1. CV_Parser_v1.md
**Prompt ID:** PRM-HR-001
**Purpose:** Extract 21 fields from candidate resumes in TSV format
**Complexity:** Medium
**Use When:** Processing new candidate resumes for CRM entry

**Key Features:**
- Extracts 21 standardized fields in exact order
- Outputs TSV (tab-separated values) for Google Sheets
- Strict formatting rules for consistency
- Department/Profession matching against allowed list

**Input:** Candidate resume (PDF/text)
**Output:** Single-line TSV string

**Cross-References:**
- Objects: Resume, TSV_Data, Candidate_Card
- Actions: Parse, Extract
- Tools: ChatGPT, Gemini, Claude
- Task Templates: TASK-TEMPLATE-HR-006

---

### 2. Communication_Templates_Prompt.md
**Prompt ID:** PRM-HR-002
**Purpose:** Guide professional candidate communication with standardized templates
**Complexity:** Medium
**Use When:** Communicating with candidates at any stage of recruitment

**Key Features:**
- Initial contact templates (English)
- Company introduction templates
- 6 rejection scenarios
- 4 special situation handlers
- 5 mandatory pre-screening questions
- Ideal candidate profile criteria

**Input:** Communication scenario and candidate context
**Output:** Professional message following brand guidelines

**Cross-References:**
- Objects: Email, Initial_Contact_Message, Rejection_Letter, Company_Introduction
- Actions: Send, Respond, Pre-Screen, Reject, Invite
- Task Templates: TASK-TEMPLATE-HR-002, TASK-TEMPLATE-HR-003, TASK-TEMPLATE-HR-016

---

### 3. CRM_Data_Entry_Prompt.md
**Prompt ID:** PRM-HR-003
**Purpose:** Guide 3-step process for parsing resumes and entering data into CRM
**Complexity:** High
**Use When:** Adding new candidates to CRM system

**Key Features:**
- Step 1: AI-powered resume parsing with CV Parser prompt
- Step 2: Google Sheets buffer workflow
- Step 3: Browser extension auto-fill guidance
- AI Status meanings and actions
- CRM Status definitions
- Video/test upload procedures
- Google Drive naming conventions

**Input:** Candidate resume and contact information
**Output:** Complete CRM entry with all required fields

**Cross-References:**
- Objects: Resume, TSV_Data, Candidate_Card, Video_Interview, CRM_Entry
- Actions: Parse, Extract, Upload, Add, Record, Update, Check
- Tools: ChatGPT, Gemini, Google_Sheets, Browser_Extension, CRM, Google_Drive
- Task Templates: TASK-TEMPLATE-HR-006, TASK-TEMPLATE-HR-007, TASK-TEMPLATE-HR-008

---

### 4. Interview_Conductor_Prompt.md
**Prompt ID:** PRM-HR-004
**Purpose:** Guide interview process, contracts, and onboarding
**Complexity:** High
**Use When:** Conducting interviews, processing contracts, onboarding new employees

**Key Features:**
- 5-phase interview structure with scripts
- Team Lead opening, closing, and question scripts
- 4 evaluation criteria (technical, communication, motivation, culture fit)
- Post-interview message templates (approval/rejection)
- Regular contract 9-step process
- Onboarding workflow (before/during first day)
- Discord ID addition
- CRM status updates

**Input:** Interview stage and candidate information
**Output:** Structured interview guidance or post-interview communications

**Cross-References:**
- Objects: Interview_Invitation, Regular_Contract, Employee_Card, Onboarding_SMS, Approval_Message, Rejection_Letter
- Actions: Conduct, Evaluate, Send, Sign, Onboard, Add, Update
- Tools: Google_Meet, Zoho_Sign, Google_Sheets, Google_Drive, Discord, CRM
- Task Templates: TASK-TEMPLATE-HR-012, TASK-TEMPLATE-HR-013, TASK-TEMPLATE-HR-015

---

## Workflow Integration

### Complete Recruitment Workflow (16 Stages):

**Stages 1-5: Search & Pre-Screening**
- Uses: Communication_Templates_Prompt.md
- Tasks: Initial contact, pre-screening questions, company introduction

**Stages 6-9: Resume Processing & CRM Entry**
- Uses: CV_Parser_v1.md, CRM_Data_Entry_Prompt.md
- Tasks: AI parsing, CRM data entry, video/test upload

**Stages 10-12: Interview Planning & Execution**
- Uses: Interview_Conductor_Prompt.md
- Tasks: Schedule interview, conduct interview, evaluate candidates

**Stages 13-16: Contracts & Onboarding**
- Uses: Interview_Conductor_Prompt.md
- Tasks: Send contract, collect documents, onboard employee

---

## Usage Guidelines

### For AI Assistants:

1. **Select the appropriate prompt** based on current workflow stage
2. **Follow prompt instructions precisely** for consistency
3. **Cross-reference with related prompts** when needed
4. **Update CRM fields** at every stage
5. **Maintain professional tone** throughout

### For HR Managers:

1. **Familiarize yourself with all 4 prompts** to understand AI capabilities
2. **Verify AI outputs** before sending to candidates
3. **Customize templates** with candidate-specific details
4. **Track progress** using CRM statuses
5. **Report issues** for prompt improvements

---

## Quality Standards

### All HR prompts must ensure:

- **Professional tone** - No emojis in rejections, maximum 1 in positive messages
- **Clear next steps** - Every communication states what happens next
- **Data accuracy** - All CRM fields filled correctly
- **Consistency** - Same format and structure across all candidates
- **Timeliness** - Last Contact Date updated with every interaction

---

## Links & Resources

### Internal Links:
- **CRM System:** https://crm-s.com/member/dashboard
- **Google Sheets Buffer:** https://docs.google.com/spreadsheets/d/1xRN6ZyKFft-D2-GvZrbIw2C75Bc6xAjZo-d7htws-WQ/
- **Google Drive (Candidates):** https://drive.google.com/drive/folders/1GF-hJ4tCK15an4Pb66DC_UayZRDRPSwT
- **Google Drive (Contracts):** https://drive.google.com/drive/folders/1BHKtEe2GIKJ5ZV0h46J7vbdVtLbg-yq_
- **Contracts Table:** https://docs.google.com/spreadsheets/d/1yYUD9nfHXdRfBkKUIrq_0v0hyJbKO8WpsUBPxkCYsZA/
- **Employee Card:** http://blog.remotemployees.com/welcome/map-for-employee/
- **Company Blog:** https://blog.remotemployees.com/

### External Links:
- **English Test:** http://form-timer.com/start/7b6c524b
- **AI Interview Bot:** https://chat.openai.com/g/g-6900e0ed490c81919a7c6911ebde4b65-remotemployees-ai-recruiter
- **Video Guide:** https://doc.clickup.com/90151865022/d/h/2kyqgjny-635/1cd76da591cbec6
- **Discord Server:** https://discord.gg/bc5FVRmJ6K

---

## Cross-References

### LIBRARIES Entities:

**Actions:**
- Send, Respond, Pre-Screen, Reject, Invite, Parse, Extract, Upload, Add, Record, Update, Check, Conduct, Evaluate, Sign, Onboard

**Objects:**
- Resume, Email, Initial_Contact_Message, Rejection_Letter, Company_Introduction, TSV_Data, Candidate_Card, Video_Interview, CRM_Entry, Interview_Invitation, Regular_Contract, Employee_Card, Onboarding_SMS, Approval_Message

**Tools:**
- ChatGPT, Gemini, Claude, Google_Sheets, Browser_Extension, CRM, Google_Drive, Google_Meet, Zoho_Sign, Discord, Telegram, Viber, Work.ua, Djinni, Robota.ua, English_Test, AI_Interview_Bot

**Processes:**
- Candidate_Search_and_Screening, CRM_Data_Entry_Workflow, Interview_Planning_and_Execution, Contract_Signing_and_Onboarding, Daily_Weekly_HR_Routine

**Professions:**
- HR_Manager, Recruiter, Team_Lead

---

### TASK_MANAGERS Entities:

**Task Templates:**
- TASK-TEMPLATE-HR-002: Send Initial Contact Message
- TASK-TEMPLATE-HR-003: Pre-Screen Candidate
- TASK-TEMPLATE-HR-006: Parse Resume Using AI
- TASK-TEMPLATE-HR-007: Add Candidate to CRM
- TASK-TEMPLATE-HR-008: Upload Video and Test
- TASK-TEMPLATE-HR-012: Conduct Group Interview
- TASK-TEMPLATE-HR-013: Send Regular Contract
- TASK-TEMPLATE-HR-015: Onboard New Employee
- TASK-TEMPLATE-HR-016: Send Rejection

**Project Templates:**
- TEMPLATE-PROJ-HR-001: Complete Recruitment Cycle

**Workflows:**
- Recruitment_Complete_Workflow.yaml
- Daily_HR_Routine_Workflow.yaml
- Weekly_HR_Tasks_Workflow.yaml

---

## Version History

### Version 1.0 (2025-11-14)
- Initial creation of HR_Operations prompts directory
- Added 4 core prompts (PRM-HR-001 through PRM-HR-004)
- Integrated with existing HR instruction documents
- Created cross-references to LIBRARIES and TASK_MANAGERS
- Documented complete recruitment workflow integration

---

## Maintenance

**Review Frequency:** Quarterly or when HR processes change
**Last Review:** 2025-11-14
**Next Review:** 2026-02-14

**Update Triggers:**
- HR process changes
- New communication templates needed
- CRM system updates
- Contract process changes
- User feedback and improvement suggestions

---

## Support

**For Questions:**
- HR Team Lead
- Taxonomy Team
- Technical Support

**For Improvements:**
- Submit feedback through HR Team Lead
- Document issues in prompt files
- Suggest template additions

---

**Related Documentation:**
- ../PROMPTS_INDEX.json - Master prompts catalog
- ../README.md - Prompts library overview
- ../../Actions/README.md - Responsibilities/Responsibilities/Actions library
- ../../Objects/README.md - Responsibilities/Responsibilities/Objects library
- ../../../TASK_MANAGERS/Task_Templates/README.md - Task Templates guide
