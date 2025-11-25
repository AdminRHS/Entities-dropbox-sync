# Shared Resources - Remote Helpers

**Purpose:** Cross-department shared resources
**Created:** 2025-11-13
**Last Updated:** 2025-11-15

---

## Overview

This folder contains resources that are used by **3 or more departments** across the company. These are foundational elements that enable collaboration and consistency.

---

## Contents

### 1. Prompts (`Prompts/`) - **NEW 2025-11-15**

**Purpose:** Centralized AI prompt library for all departments

**Migrated:** 2025-11-15 from `LBS_006_Departments/PROMPTS/`

**Size:** 151 files, ~3.5MB

**Categories:** 9 prompt categories
- **Core/** - Main system prompts (MAIN_PROMPT v4 and v5)
- **Video_Processing/** - 4 prompts for video workflows
- **HR_Operations/** - 4 prompts for HR automation
- **Library_Processing/** - 2 prompts for library maintenance
- **Research/** - Research methodology prompts
- **Daily_Reports/** - Department daily report prompts
- **Operational_Workflows/** - Call organizers
- **Automation/** - Rules and version control
- **Communication/** - Templates and announcements

**Key Files:**
- `Prompts/PROMPTS_INDEX.json` - Master catalog (v1.2, 12 active prompts)
- `Prompts/README.md` - Complete documentation

**Archive:** `Archive/Prompts_Archive/` (~747MB historical content)

**Documentation:** See [Prompts/README.md](Prompts/README.md)

---

### 2. LIBRARIES/ (Common Actions, Objects, Tools)

#### common_actions.json
Actions (verbs) that are used by multiple departments:
- Examples: create, analyze, send, update, review
- These actions form the basis of cross-functional tasks

#### common_objects.json
Objects (nouns) that are manipulated by multiple departments:
- Examples: email, report, document, design, mockup
- These objects represent shared deliverables and artifacts

#### common_tools.json
Tools and software that are used by multiple departments:
- Examples: ChatGPT, Gmail, Google Drive, Notion
- These tools enable company-wide collaboration

---

## Usage

Department-specific libraries inherit from these shared resources. When an action, object, or tool is used by 3+ departments, it's considered "common" and listed here.

### For Departments:
- Use department-specific libraries for day-to-day work
- Refer to shared resources for understanding cross-functional elements
- Propose additions when new common elements emerge

### For System Architects:
- Update shared resources when usage patterns change
- Monitor which elements become common over time
- Ensure consistency across department-specific libraries

---

## Maintenance

- **Update Frequency:** Monthly or when major changes occur
- **Regeneration:** Run consolidation scripts to refresh shared resources
- **Validation:** Ensure shared elements are properly referenced in department libraries

---

**Last Updated:** 2025-11-13