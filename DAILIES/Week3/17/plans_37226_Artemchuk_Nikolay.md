# PLANS - Daily Processing Output

**Date:** 2025-01-27  
**Source:** daily.md  
**Processed with:** MAIN PROMPT v4.md

---

## EXECUTIVE SUMMARY

This call identified critical operational gaps in the Sales department (no pre-call emails, no client research) and systemic issues with employee work environments and file hygiene. A unified methodology was outlined: enforce individual accountability through one-on-one sales meetings, audit and fix work environments (VS Code, Cursor, Dropbox, internet), and introduce intermediate "export/play-out" folders plus scripts so daily outputs can be structured like GitHub commits. The team also discussed synchronizing voice-log bots with CRM attendance, expanding AI platform integrations (Gemini and others), training Design/Video on taxonomy and transcript processing, and improving prompt and task-template architecture. Overall direction: make data reliably structured across departments so AI tools can automate research, processing, and reporting on top.

---

## STRATEGIC INITIATIVES

### 1. Sales Process Improvement

**Problem Identified:**
- Sales team (Силзы) is not sending any emails to clients
- No initial connection emails before calls
- No client research (depressor checks) before scheduled calls
- Missing basic information gathering (name, website, company details)
- Sales processes have been forgotten/neglected in favor of lead generation focus

**Strategic Approach:**
- Conduct individual one-on-one meetings (30 minutes per person)
- Separate meetings for each team member: Лиля (Liliia), Настя (Anastasiya), новая Лера (new Lera)
- Address group responsibility issues ("group responsibility = no responsibility")
- Present and train on research processes that were never shown to the team

**Related Department:** Sales  
**Related Project:** CRM System  
**Priority:** Critical

---

### 2. Work Environment Audit & Setup

**Areas to Review:**
- Internet speed issues
- Software installations and configurations
- Power outages/connectivity problems
- VS Code extensions setup
- Cursor setup and token management
- File synchronization issues (empty files after calls)
- Dropbox folder connections

**Specific Issues:**
- Files not saving properly
- Dropbox not connected (example: Юля Чоботар / Chobotar Yuliia)
- Need point-by-point verification with each person

**Related Department:** All Departments  
**Priority:** High

---

### 3. Framework & Script Development

**Methodology Established:**
- Intermediate folders required between connecting folders
- Example workflow: daily folder → export folder → task template/library
- Structured updates similar to GitHub commits
- Script-based data structuring and processing

**Implementation Plan:**
- Create intermediate "play-out" folders for daily processing
- Develop scripts to extract information from one folder and transfer to another
- Structure data updates similar to GitHub change tracking
- Script processes and structures data automatically

**Related Department:** AI  
**Related Project:** CRM System, Task Management Framework  
**Priority:** High

---

### 4. Data Synchronization & Integration

**Current Integration:**
- Bot checking voice logs syncing with attendance in CRM
- Need to synchronize plans and processing between systems

**Expansion Plans:**
- Connect Gemini platform
- Add more AI platforms gradually
- Small scripts for incremental processing
- Centralized Dropbox location for all synchronized data
- Output flexibility: dashboards, apps, tables, anywhere

**Key Principle:**
- Once data is structured and stored, output is easy
- Focus on data structuring first
- Incremental improvements daily

**Related Department:** AI  
**Related Project:** CRM System, Data Integration  
**Priority:** Medium

---

### 5. Taxonomy Training & Process Documentation

**Request from Вильгельм (Skrypkar Vilhelm):**
- Need training on taxonomy
- Currently only transcribing videos
- Don't know how to distribute/process transcriptions further
- Reference: Process Lab folder in prompts

**Training Scope:**
- Taxonomy structure and organization
- Export processes
- Distribution to task managers
- Task template updates
- Milestone object updates
- Token optimization strategies

**Related Department:** Design (Video/Content)  
**Related Project:** Process Documentation, RAC Knowledge Base  
**Priority:** Medium

---

### 6. Prompt Management & Task Template Structure

**Current State:**
- Prompts moved to Task Manager folder
- Need to modify prompts to reference specific task templates and milestones
- Example: "go to task template 3" or "milestone 8"

**Improvements Needed:**
- Describe logic within folders
- Provide variations/options to people
- Avoid hardcoding departments in task IDs
- Avoid hardcoding projects in milestone IDs
- Use simple milestone IDs for flexibility
- Enable combination of different options

**Example Use Case:**
- Task: "transcribe call"
- Options provided: Wispr Flow, Crega, Transcriber 4 in Google Meet
- Person chooses method, but result is what matters
- Concept of "delivery" introduced (similar to Object Type)

**Related Department:** AI  
**Related Project:** Task Management Framework, Prompt Engineering  
**Priority:** Medium

---

### 7. Account Management & Access Control

**GPT Accounts:**
- Review current GPT account usage
- Consider disabling GPT analysis where appropriate
- Add 3 more Claude accounts

**Account Redistribution:**
- Move to content management
- Archive management (shared on admin, now removed)
- Access to PR department resources
- Email access for Дашиных сотрудниц (Darya's employees)
- Dropbox access setup

**Related Department:** AI, HR  
**Priority:** Low-Medium

---

## CROSS-DEPARTMENT DEPENDENCIES

1. **Sales ↔ AI:** Sales process training requires AI department to present research methodologies
2. **All Departments ↔ IT/Infrastructure:** Work environment setup affects all departments
3. **Design ↔ AI:** Taxonomy training requires AI department expertise
4. **AI ↔ CRM:** Framework development requires CRM integration

---

## KEY METRICS TO TRACK

- Email send rates from Sales team
- Client research completion rate before calls
- File synchronization success rate
- Script processing success rate
- Taxonomy adoption rate in Design department
- Prompt modification and usage rates

---

## NEXT STEPS SUMMARY

1. Schedule individual meetings with Sales team members
2. Conduct work environment audits for all team members
3. Develop intermediate folder structure and scripts
4. Expand AI platform integrations (Gemini + others)
5. Conduct taxonomy training session
6. Refine prompt management structure
7. Review and optimize account access

