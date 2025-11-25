# LIBRARIES ID and Name Conventions

**Document Type:** Reference Guide  
**Entity:** LIBRARIES  
**Last Updated:** 2025-12-26  
**Purpose:** Document ID formats and naming conventions (including letter case rules) for all LIBRARIES entities

---

## Overview

This document provides a comprehensive reference for ID formats and naming conventions used across all LIBRARIES sub-entities. It covers:
- **ID Format Patterns** - How entity IDs are structured
- **Name Conventions** - Letter case rules for entity names
- **ISO Code Standards** - 3-letter consonant-only codes
- **Department Code Integration** - How department codes are used in IDs

---

## ID Format Patterns

### General ID Structure

**Basic Format:** `{TYPE}-{NUMBER}`  
**Department-Specific Format:** `{TYPE}-{DEPT-CODE}-{NUMBER}`

Where:
- `{TYPE}` = Entity type prefix (uppercase)
- `{DEPT-CODE}` = 3-letter department ISO code (optional, uppercase)
- `{NUMBER}` = Sequential number (zero-padded to 3 digits)

### Entity Type ID Formats

| Entity Type | ID Format | Examples | Notes |
|-------------|-----------|----------|-------|
| **Actions** | `ACTION-XXX` or `ACT-XXX` | `ACTION-001`, `ACT-042` | Two formats coexist |
| **Objects** | `OBJ-XXX` or `OBJ-{DEPT}-XXX` | `OBJ-001`, `OBJ-DEV-001` | Department-specific optional |
| **Tools** | `TOOL-XXX` or `TOOL-{DEPT}-XXX` | `TOOL-AI-029`, `TOOL-DEV-001` | Department-specific common |
| **Skills** | `SKL-XXX` | `SKL-001`, `SKL-063` | Sequential numbering |
| **Responsibilities** | `RESP-XXX` or `RSP-XXX` | `RESP-001`, `RSP-002` | Two formats coexist |
| **Parameters** | `PRM-XXX` or `PRM-{DEPT}-XXX` | `PRM-001`, `PRM-DEV-015` | Department-specific optional |
| **Professions** | No standard ID format | N/A | Uses `profession_name` field instead |
| **Departments** | `DPT-XXX` | `DPT-001`, `DPT-002` | Sequential numbering |

### Department Code Integration

When department codes are included in IDs, they use the 3-letter ISO format:

**Format:** `{TYPE}-{DEPT-CODE}-{NUMBER}`

**Examples:**
- `OBJ-DEV-001` - Development Object #1
- `TOOL-AI-029` - AI Tool #29
- `RSP-AIA-001` - AI Responsibility #1
- `PRM-DEV-015` - Development Parameter #15

**Department ISO Codes:**
- `AIA` - AI & Automation
- `DEV` - Development
- `HRM` - Human Resources
- `LGN` - Lead Generation
- `DGN` - Design
- `VID` - Video Production
- `SLS` - Sales
- `SMM` - Social Media Management
- `FNC` - Finance

---

## Name Conventions (Letter Case Rules)

### Tool Names
**Format:** **Title Case** (Capitalize First Letter of Each Word)

**Examples:**
- ✅ `"GitHub"` (not "github" or "GITHUB")
- ✅ `"Claude"` (not "claude" or "CLAUDE")
- ✅ `"ChatGPT"` (not "chatgpt" or "CHATGPT")
- ✅ `"VS Code"` (not "vs code" or "VS CODE")
- ✅ `"Leonardo AI"` (not "leonardo ai")

**Field:** `tool_name`, `name`

### Profession Names
**Format:** **lowercase** (all lowercase letters)

**Examples:**
- ✅ `"ai engineer"` (not "AI Engineer" or "AI ENGINEER")
- ✅ `"developer"` (not "Developer" or "DEVELOPER")
- ✅ `"lead generator"` (not "Lead Generator")
- ✅ `"automation specialist"` (not "Automation Specialist")

**Field:** `profession_name`

**Note:** Display names may use Title Case, but the canonical `profession_name` field uses lowercase.

### Department Names
**Format:** **Title Case** (Capitalize First Letter of Each Word)

**Examples:**
- ✅ `"AI Engineers"` (not "ai engineers" or "AI ENGINEERS")
- ✅ `"Developers"` (not "developers" or "DEVELOPERS")
- ✅ `"Lead Generators"` (not "lead generators")
- ✅ `"Video Editors"` (not "video editors")

**Fields:** `name`, `full_name`

### Action Names
**Format:** **lowercase** (all lowercase letters)

**Examples:**
- ✅ `"abstract"` (not "Abstract" or "ABSTRACT")
- ✅ `"access"` (not "Access")
- ✅ `"create"` (not "Create")
- ✅ `"generate"` (not "Generate")

**Field:** `action`

### Object Names
**Format:** **Title Case** (Capitalize First Letter of Each Word)

**Examples:**
- ✅ `"Dashboard Application"` (not "dashboard application")
- ✅ `"GitHub Repository"` (not "github repository")
- ✅ `"Video Script"` (not "video script")
- ✅ `"UI Mockup"` (not "ui mockup")

**Field:** `name`, `object_name`

### Skill Phrases
**Format:** **lowercase** (all lowercase letters)

**Examples:**
- ✅ `"screened candidates via CRM"` (not "Screened Candidates via CRM")
- ✅ `"generated leads via LinkedIn"` (not "Generated Leads via LinkedIn")
- ✅ `"designed UI mockups in Figma"` (not "Designed UI Mockups in Figma")
- ✅ `"developed features in React"` (not "Developed Features in React")

**Field:** `skill_phrase`

### Responsibility Names
**Format:** **lowercase** (all lowercase letters)

**Examples:**
- ✅ `"screen candidates"` (not "Screen Candidates")
- ✅ `"generate leads"` (not "Generate Leads")
- ✅ `"design UI mockups"` (not "Design UI Mockups")
- ✅ `"develop frontend features"` (not "Develop Frontend Features")

**Field:** `responsibility_name`

---

## ISO Code Standards

### Consonant-Only Rule

**CRITICAL:** All ISO codes use **CONSONANTS ONLY** (no vowels: A, E, I, O, U)

**Format:** Exactly 3 uppercase letters, consonants only

**Valid ISO Codes:**
- ✅ `RSP` (Responsibilities)
- ✅ `ACT` (Actions)
- ✅ `OBJ` (Objects)
- ✅ `PRM` (Parameters)
- ✅ `TOL` (Tools)
- ✅ `SKL` (Skills)
- ✅ `PRF` (Professions)
- ✅ `DPT` (Departments)

**Invalid ISO Codes:**
- ❌ `RESP` (contains vowel E)
- ❌ `ACTN` (contains vowel A)
- ❌ `PARAM` (contains vowels A and A)

### Department ISO Codes

| ISO Code | Department Name | Full Name |
|----------|----------------|-----------|
| `AIA` | AI_Tasks | AI & Automation |
| `DEV` | DEV_Tasks | Development |
| `HRM` | HR_Tasks | Human Resources |
| `LGN` | LG_Tasks | Lead Generation |
| `DGN` | Design_Tasks | Design |
| `VID` | Video_Tasks | Video Production |
| `SLS` | Sales_Tasks | Sales |
| `SMM` | SMM_Tasks | Social Media Management |
| `FNC` | Finance_Tasks | Finance & Accounting |

**Note:** All department codes are 3-letter, consonant-only, uppercase.

---

## File Naming Conventions

### JSON Files
**Format:** `{Entity_Type}_{Name}.json` or `{Name}.json`

**Examples:**
- `Actions_Master.json`
- `GitHub.json`
- `AI_Engineer.json`
- `departments.json`
- `responsibilities.json`

**Rules:**
- Use underscores for multi-word names
- PascalCase for entity types: `Actions_Master.json`
- Title Case for specific entities: `Video_Generation_Actions.json`
- lowercase for master files: `departments.json`, `professions.json`

### Directory Structure
**Format:** `LBS_XXX_Name/{Subcategory}/` (root level) or `{Category}/{Subcategory}/` (subfolders)

**Current Structure (Legacy):**
- `LBS_003_LBS_003_Tools/By_Category/AI/`
- `LBS_003_LBS_003_Tools/By_Category/Development/`
- `LBS_004_../TALENTS/Skills/Master/`
- `LBS_004_../TALENTS/Skills/By_Department/`
- `Responsibilities/Actions/`
- `Responsibilities/Objects/`

**Proposed Structure:**
- `LBS_003_LBS_003_Tools/By_Category/AI/`
- `LBS_003_LBS_003_Tools/By_Category/Development/`
- `LBS_004_LBS_004_../TALENTS/Skills/Master/`
- `LBS_004_LBS_004_../TALENTS/Skills/By_Department/`
- `Responsibilities/Actions/Master/`
- `Responsibilities/Objects/By_Domain/`

---

## Field Name Conventions

### Standard Field Names

| Field Name | Format | Example Values |
|------------|--------|----------------|
| `entity_type` | Uppercase | `"LIBRARIES"` |
| `sub_entity` | Title Case | `"Tool"`, `"Profession"`, `"Object"` |
| `tool_id` | ID Format | `"TOOL-AI-029"` |
| `tool_name` | Title Case | `"GitHub"`, `"Claude"` |
| `profession_name` | lowercase | `"ai engineer"`, `"developer"` |
| `skill_id` | ID Format | `"SKL-001"` |
| `skill_phrase` | lowercase | `"screened candidates via CRM"` |
| `object_id` | ID Format | `"OBJ-DEV-001"` |
| `name` | Title Case | `"Dashboard Application"` |
| `action_id` | ID Format | `"ACTION-001"` |
| `action` | lowercase | `"create"`, `"generate"` |
| `department_id` | ID Format | `"DPT-001"` |
| `code` | Uppercase | `"AIA"`, `"DEV"`, `"HRM"` |

---

## Examples by Entity Type

### Tools
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-AI-029",
  "tool_name": "Claude",
  "name": "Claude"
}
```

**Key Points:**
- `tool_id`: Department-specific format (`TOOL-AI-029`)
- `tool_name`: Title Case (`"Claude"`)

### Professions
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_name": "ai engineer",
  "department": "developers"
}
```

**Key Points:**
- `profession_name`: lowercase (`"ai engineer"`)
- No standard ID format (uses name as identifier)

### Skills
```json
{
  "skill_id": "SKL-001",
  "skill_phrase": "screened candidates via CRM",
  "components": {
    "result": "screened",
    "action": "screen",
    "object": "candidates",
    "tool": "CRM"
  }
}
```

**Key Points:**
- `skill_id`: Sequential format (`SKL-001`)
- `skill_phrase`: lowercase (`"screened candidates via CRM"`)

### Objects
```json
{
  "object_id": "OBJ-DEV-001",
  "name": "Dashboard Application",
  "category": "Development"
}
```

**Key Points:**
- `object_id`: Department-specific format (`OBJ-DEV-001`)
- `name`: Title Case (`"Dashboard Application"`)

### Actions
```json
{
  "action_id": "ACTION-001",
  "action": "abstract",
  "forms": {
    "processes": ["abstracting"],
    "results": ["abstracted"]
  }
}
```

**Key Points:**
- `action_id`: Sequential format (`ACTION-001`)
- `action`: lowercase (`"abstract"`)

### Departments
```json
{
  "department_id": "DPT-001",
  "code": "AIA",
  "name": "AI Engineers",
  "full_name": "AI & Automations Department"
}
```

**Key Points:**
- `department_id`: Sequential format (`DPT-001`)
- `code`: Uppercase consonant-only (`"AIA"`)
- `name`: Title Case (`"AI Engineers"`)

---

## Validation Rules

### ID Format Validation

1. **Length:** Entity type prefix + hyphen + 3 digits (or + department code + hyphen + 3 digits)
2. **Characters:** Uppercase letters and hyphens only
3. **Numbers:** Zero-padded to 3 digits (001, 002, 010, 100)
4. **Uniqueness:** Each ID must be unique within its entity type

### Name Format Validation

1. **Tool Names:** Title Case - First letter of each word capitalized
2. **Profession Names:** lowercase - All letters lowercase
3. **Department Names:** Title Case - First letter of each word capitalized
4. **Action Names:** lowercase - All letters lowercase
5. **Object Names:** Title Case - First letter of each word capitalized
6. **Skill Phrases:** lowercase - All letters lowercase
7. **Responsibility Names:** lowercase - All letters lowercase

### ISO Code Validation

1. **Length:** Exactly 3 characters
2. **Characters:** Uppercase letters only
3. **Consonants Only:** No vowels (A, E, I, O, U)
4. **Uniqueness:** Each code must be unique within its category

---

## Common Patterns Summary

### ID Patterns
- **Simple:** `{TYPE}-{NUMBER}` → `ACTION-001`, `SKL-001`
- **Department-Specific:** `{TYPE}-{DEPT}-{NUMBER}` → `TOOL-AI-029`, `OBJ-DEV-001`

### Name Patterns
- **Title Case:** Tools, Objects, Departments → `"GitHub"`, `"Dashboard Application"`, `"AI Engineers"`
- **lowercase:** Professions, Actions, Skills, Responsibilities → `"ai engineer"`, `"create"`, `"screened candidates via CRM"`

### ISO Code Patterns
- **3-letter, uppercase, consonants only** → `AIA`, `DEV`, `HRM`, `LGN`, `DGN`, `VID`, `SLS`, `SMM`, `FNC`

---

## Related Documents

- [Libraries_ISO_Code_Registry.md](./Taxonomy/Libraries_ISO_Code_Registry.md) - Complete ISO code registry
- [Libraries_Master_List.csv](./Taxonomy/Libraries_Master_List.csv) - Master entity catalog
- [README.md](./README.md) - LIBRARIES entity documentation

---

**Document Status:** Active  
**Maintenance Schedule:** Update when new entity types or conventions are added  
**Owner:** LIBRARIES Taxonomy Team

