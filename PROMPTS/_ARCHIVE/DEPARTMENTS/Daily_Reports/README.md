# Daily Reports Prompts

**Category:** Daily Activity Reports  
**Purpose:** Automated daily report generation for all departments  
**Status:** Active

---

## Overview

Daily Reports system automates the collection and generation of comprehensive daily activity reports from all departments into department-specific reports.

---

## Structure

### PROMPT_Daily_Report_Collection.md
**Purpose:** Main collection prompt - orchestrates all department reports  
**Status:** Active  
**Features:**
- Reads all department prompt logs
- Generates department-specific reports

### Constructor/
**Purpose:** Template builder and prompt generator  
**Contains:**
- Template structures
- Variable mappings
- Implementation guides
- Documentation standards

### Department_Prompts/
**Purpose:** Department-specific daily report prompts  
**Prompts:**
- `PROMPT_AI_Daily_Report.md` - AI department reports
- `PROMPT_Content_Daily_Report.md` - Content department reports
- `PROMPT_Design_Daily_Report.md` - Design department reports
- `PROMPT_Dev_Daily_Report.md` - Development department reports
- `PROMPT_Finance_Daily_Report.md` - Finance department reports
- `PROMPT_HR_Daily_Report.md` - HR department reports
- `PROMPT_LG_Daily_Report.md` - Lead Generation reports
- `PROMPT_Marketing_Daily_Report.md` - AI reports
- `PROMPT_Sales_Daily_Report.md` - Sales reports
- `PROMPT_SMM_Daily_Report.md` - Social Media Management reports
- `PROMPT_Video_Daily_Report.md` - Video department reports

---

## Workflow

1. **Read Prompt Logs:** Collect activities from department prompt logs
2. **Generate Reports:** Create department-specific daily reports

---

## Report Structure

Each department report includes:
- Executive Summary
- Activity Timeline
- Metrics and Statistics
- Key Deliverables
- Impact Analysis
- Challenges and Solutions
- Recommendations

---

## Integration

- References MAIN PROMPT v4.md for company context
- Uses department-specific employee directories
- Integrates with LIBRARIES for tools and resources
- Links to TASK_MANAGERS for task tracking

---

**Last Updated:** 2025-11-13



