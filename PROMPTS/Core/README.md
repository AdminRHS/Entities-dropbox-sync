# Core Prompts

**Category:** Core System Prompts  
**Purpose:** Main system prompts for call organization and company context  
**Status:** Active

---

## Overview

Core prompts provide the foundational framework for processing calls, organizing information, and maintaining company context across all operations.

---

## Prompts

### MAIN_PROMPT_v2.md
**Version:** 2.0  
**Purpose:** Call organization framework (legacy version)  
**Status:** Deprecated (maintained for reference)

### MAIN_PROMPT_v3.md
**Version:** 3.0  
**Purpose:** Enhanced call organization framework  
**Status:** Active (being phased out)

### MAIN_PROMPT_v4.md
**Version:** 4.0  
**Purpose:** Current main system prompt - Complete call organization framework  
**Status:** Active - Current Version  
**Key Features:**
- Company context (Remote Helpers - AI-First organization)
- Employee Directory (32 employees across departments)
- Project Directory (31+ active projects)
- 21 comprehensive extraction sections
- Intelligent participant and project matching
- Template-driven operations framework

### MAIN_PROMPT_v4_Modular/
**Version:** 4.0 (Modular)  
**Purpose:** Modular version of MAIN PROMPT v4 for easier maintenance  
**Status:** Active  
**Structure:**
- `00_Purpose_and_Company_Context.md` - Company overview
- `01_Employee_Directory.md` - Employee information
- `02_Project_Directory.md` - Project listings
- `03_Instructions_for_AI.md` - Processing instructions
- `04_Section_Templates_1-11.md` - First 11 extraction sections
- `05_Section_Templates_12-21.md` - Remaining extraction sections
- `06_Section_22_Taxonomy_Framework.md` - Taxonomy integration
- `07_Section_23_LIBRARIES_Integration.md` - LIBRARIES integration
- `08_Processing_Guidelines.md` - Processing rules
- `09_Usage_Instructions.md` - Usage guide
- `10_Version_History.md` - Change log

---

## Usage

**Primary Prompt:** Use `MAIN_PROMPT_v4.md` for all call processing  
**Modular Version:** Use `MAIN_PROMPT_v4_Modular/` for component-based processing

---

## Related Prompts

- Daily Reports prompts reference MAIN PROMPT v4
- Video Processing prompts use MAIN PROMPT v4 framework
- All department-specific prompts integrate MAIN PROMPT v4

---

**Last Updated:** 2025-11-13



