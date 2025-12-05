# 10_DATA_FILES.md

**CSV & JSON Data File Formats**
**Location:** Multiple directories (00_SEARCH_QUEUE/, 01_VIDEO_QUEUE/, etc.)
**Last Updated:** 2025-12-04
**Status:** ✅ Production Ready

---

## Table of Contents

1. [Overview](#overview)
2. [CSV Files](#csv-files)
3. [JSON Files](#json-files)
4. [Data Standards](#data-standards)
5. [Field Definitions](#field-definitions)
6. [Example Data](#example-data)
7. [Import/Export](#importexport)
8. [Validation](#validation)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Overview

The RESEARCHES 2 system uses **CSV files** for queue management and tracking, and **JSON files** for entity storage in LIBRARIES. This document details all data file formats, schemas, and standards.

### Key Statistics

- **3 Primary CSV Files** (Search Queue, Video Queue, Master List)
- **7 JSON Entity Types** (Workflows, Tools, Objects, Actions, Skills, Professions, Departments)
- **21 CSV Fields** in Video Queue (most comprehensive)
- **10 CSV Fields** in Search Queue (simplest)
- **Encoding:** UTF-8 (all files)
- **Line Endings:** CRLF (Windows) or LF (Unix/Mac)

### Quick Facts

- **CSV Delimiter:** Comma (,)
- **CSV Quote Character:** Double quote (")
- **CSV Encoding:** UTF-8
- **JSON Encoding:** UTF-8
- **JSON Indentation:** 2 spaces
- **Date Format:** YYYY-MM-DD
- **Time Format:** HH:MM:SS
- **ID Formats:** PREFIX-NNN (e.g., VQ-001, SEARCH-001)

---

## CSV Files

### CSV File 1: Search_Queue_Master.csv

**Location:** `00_SEARCH_QUEUE/Search_Queue_Master.csv`

**Purpose:** Track video search assignments (Phase 0)

**Schema:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Search_ID** | String | Yes | Unique ID (SEARCH-001, SEARCH-002...) | SEARCH-001 |
| **Employee** | String | Yes | Employee name | Niko Kar |
| **Department** | String | Yes | Department code (3 letters) | DEV |
| **Topic** | String | Yes | Research topic | Claude AI tutorials |
| **Search_Query** | String | No | Optional search query | claude tutorial |
| **Status** | Enum | Yes | Assigned, In Progress, Completed | Assigned |
| **Videos_Found** | Integer | Yes | Number of videos found (default 0) | 20 |
| **Date_Assigned** | Date | Yes | Date assigned (YYYY-MM-DD) | 2025-12-04 |
| **Date_Completed** | Date | No | Date completed (YYYY-MM-DD) | 2025-12-05 |
| **Notes** | String | No | Free text notes | Focus on 2024-2025 |

**Status Values:**
- `Assigned` - Task assigned, not started
- `In Progress` - Employee working on search
- `Completed` - Search finished, videos added to queue

**Total Fields:** 10

**Example Row:**
```csv
SEARCH-001,John Doe,DEV,Claude AI tutorials,claude tutorial,Assigned,0,2025-12-04,,Focus on 2024-2025
```

**File Size:** Small (~1-5 KB for 10-50 entries)

---

### CSV File 2: Video_Queue_Master.csv

**Location:** `01_VIDEO_QUEUE/Video_Queue_Master.csv`

**Purpose:** Track videos in queue for transcription (Phase 0→1)

**Schema:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Queue_ID** | String | Yes | Unique ID (VQ-001, VQ-002...) | VQ-001 |
| **Video_ID** | String | Yes | YouTube video ID (11 chars) | dQw4w9WgXcQ |
| **Video_Title** | String | Yes | Video title | Google AI Studio Tutorial |
| **Channel_Name** | String | Yes | YouTube channel name | AI for Grownups |
| **Channel_URL** | String | No | Channel URL | [To be extracted] |
| **Video_URL** | String | Yes | Full YouTube URL | https://youtube.com/watch?v=dQw4w9WgXcQ |
| **Views** | Integer | Yes | View count (default 0) | 1500000 |
| **Likes** | Integer | Yes | Like count (default 0) | 45000 |
| **Comments** | Integer | Yes | Comment count (default 0) | 2300 |
| **Publish_Date** | Date | Yes | Publication date (YYYY-MM-DD) | 2025-10-15 |
| **Duration** | Time | Yes | Video duration (HH:MM:SS) | 00:10:32 |
| **Added_By** | String | Yes | Employee who added video | Niko Kar |
| **Added_Date** | Date | Yes | Date added (YYYY-MM-DD) | 2025-11-24 |
| **Status** | Enum | Yes | Pending, Selected, Parsing, Parsed, Rejected | Pending |
| **Selected_By** | String | No | Employee who selected for parsing | |
| **Selected_Date** | Date | No | Date selected (YYYY-MM-DD) | |
| **Parsed_Date** | Date | No | Date parsing completed (YYYY-MM-DD) | |
| **Topic_Category** | String | Yes | Research topic | AI Tools Overview |
| **Research_Source** | String | Yes | Tool used (Perplexity, Gemini, etc.) | Perplexity |
| **Priority_Score** | Float | Yes | Priority score (0-100) | 75.5 |
| **Notes** | String | No | Free text notes | Comprehensive overview |

**Status Values:**
- `Pending` - Newly added, awaiting review
- `Selected` - Marked for parsing
- `Parsing` - Currently being parsed
- `Parsed` - Parsing complete
- `Rejected` - Not relevant

**Total Fields:** 21

**Example Row:**
```csv
VQ-001,dQw4w9WgXcQ,Google AI Studio Full Walkthrough,AI for Grownups,[To be extracted],https://youtube.com/watch?v=dQw4w9WgXcQ,1500000,45000,2300,2025-10-15,00:10:32,Niko Kar,2025-11-24,Pending,,,,AI Tools Overview,Perplexity,75.5,Comprehensive overview
```

**File Size:** Medium (~10-50 KB for 50-200 entries)

---

### CSV File 3: RESEARCHES_Master_List.csv

**Location:** `RESEARCHES_Master_List.csv`

**Purpose:** Master registry of all research entities (videos, reports, etc.)

**Schema:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **RSR_ID** | String | Yes | Unique research ID (RSR-001, RSR-002...) | RSR-024 |
| **Name** | String | Yes | Research name/title | Video Research 023 - Google AI Studio |
| **Description** | String | Yes | Brief description | Full walkthrough and tutorial |
| **Department** | String | Yes | Primary department (3 letters) | VID |
| **Category** | String | Yes | Research category | Video_Transcription |
| **File_Path** | String | Yes | Relative path to file | ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_023.md |
| **Status** | Enum | Yes | Active, Archived, Deprecated | Active |

**Category Values:**
- `Video_Transcription` - Transcribed videos
- `Research_Report` - Written research reports
- `SMM` - Social media research
- `Meta-Category` - Meta-level categories

**Status Values:**
- `Active` - Current and in use
- `Archived` - Old but kept for reference
- `Deprecated` - No longer relevant

**Total Fields:** 7

**Example Row:**
```csv
RSR-024,"Video Research 023 - Google AI Studio","Full walkthrough and tutorial for Google AI Studio","VID","Video_Transcription","ENTITIES/TASK_MANAGERS/RESEARCHES/02_TRANSCRIPTIONS/Video_023.md","Active"
```

**File Size:** Medium (~5-20 KB for 20-100 entries)

---

## JSON Files

### JSON Entity Types

The system uses JSON files to store entities in LIBRARIES. All JSON files follow consistent structure:

**7 Entity Types:**
1. **Workflows** (WRF-XXX-NNN) - Business process workflows
2. **Tools** (TOL-XXX-NNN) - Software tools and platforms
3. **Objects** (OBJ-XXX-NNN) - Tangible outputs/deliverables
4. **Actions** (ACT-NNN) - Action verbs
5. **Skills** (SKL-NNN) - Individual skills
6. **Professions** (PRF-NNN) - Job roles
7. **Departments** (DEP-XXX) - Organizational units

---

### JSON Schema: Tool Entity

**Location:** `LIBRARIES/LBS_003_Tools/[Category]/TOL-XXX-NNN_Tool_Name.json`

**Purpose:** Document software tools and platforms

**Schema:**
```json
{
  "entity_type": "tool",                    // Required: "tool"
  "tool_id": "TOL-XXX-NNN",                 // Required: Unique ID
  "tool_name": "Tool Name",                 // Required: Display name
  "category": "Category",                   // Required: AI_Tools, Automation, Auth, etc.
  "vendor": "Company Name",                 // Required: Vendor or "Open-source"
  "description": "Brief description",       // Required: 1-2 sentences

  "key_features": [                         // Optional: Array of strings
    "Feature 1",
    "Feature 2"
  ],

  "use_cases": [                            // Optional: Array of strings
    "Use case 1",
    "Use case 2"
  ],

  "pricing": {                              // Optional: Object
    "model": "Freemium",                    // Free, Freemium, Subscription, Enterprise
    "tiers": "Free tier available"
  },

  "integration": {                          // Optional: Object
    "api_available": true,                  // Boolean
    "platforms": ["Web", "Desktop"],        // Array of strings
    "integrates_with": ["TOL-XXX-001"]      // Array of tool IDs
  },

  "used_in_workflows": ["WRF-XXX-001"],     // Optional: Array of workflow IDs
  "used_in_tasks": ["TSK-001"],             // Optional: Array of task IDs
  "related_actions": ["ACT-001"],           // Optional: Array of action IDs
  "produces_objects": ["OBJ-XXX-001"],      // Optional: Array of object IDs

  "source_videos": [                        // Optional: Array of objects
    {
      "video_id": "Video_023",
      "video_title": "Video Title",
      "mentions": 12,
      "timestamps": ["00:15:56"]
    }
  ],

  "departments": ["AID", "SEC"],            // Optional: Array of department codes
  "skills_required": ["SKL-001"],           // Optional: Array of skill IDs

  "documentation": {                        // Optional: Object
    "vendor_site": "https://...",
    "api_docs": "https://...",
    "tutorials": ["https://..."]
  },

  "metadata": {                             // Required: Object
    "created_date": "YYYY-MM-DD",           // Required: Creation date
    "last_updated": "YYYY-MM-DD",           // Required: Last update date
    "created_by": "AI Department",          // Optional: Creator
    "status": "active"                      // Required: active, deprecated
  }
}
```

**Field Types:**
- String: "text"
- Integer: 123
- Float: 75.5
- Boolean: true, false
- Array: ["item1", "item2"]
- Object: {"key": "value"}
- Enum: Specific allowed values only

**Required Fields:** 8 (entity_type, tool_id, tool_name, category, vendor, description, metadata.created_date, metadata.last_updated, metadata.status)

**File Size:** Small-Medium (~1-5 KB per file)

---

### JSON Schema: Workflow Entity

**Location:** `TASK_MANAGERS/TSM-001_Templates/Workflows/WRF-XXX-NNN_Workflow_Name.json`

**Purpose:** Document business process workflows

**Schema:**
```json
{
  "entity_type": "workflow",                // Required
  "workflow_id": "WRF-XXX-NNN",             // Required: Unique ID
  "workflow_name": "Workflow Name",         // Required: Display name
  "version": "1.0",                         // Required: Version number

  "description": "Clear objective",         // Required: Purpose
  "category": "Automation",                 // Required: Category
  "complexity": "Medium",                   // Required: Low, Medium, High
  "estimated_duration": "30 minutes",       // Required: Time estimate

  "departments": ["AID", "SEC"],            // Required: Array of department codes
  "primary_department": "AID",              // Required: Main department

  "milestones": [                           // Required: Array of objects
    {
      "milestone_id": "MLS-001",
      "milestone_name": "Milestone Name",
      "objective": "Objective",
      "tasks": ["TSK-001", "TSK-002"],
      "department": "AID",
      "duration": "10 min"
    }
  ],

  "tools_required": ["TOL-XXX-001"],        // Optional: Array of tool IDs
  "skills_required": ["SKL-001"],           // Optional: Array of skill IDs
  "responsibilities": ["RSP-333"],          // Optional: Array of responsibility IDs

  "prerequisites": [                        // Optional: Array of strings
    "Prerequisite 1"
  ],

  "deliverables": [                         // Optional: Array of strings
    "Deliverable 1"
  ],

  "kpis": [                                 // Optional: Array of objects
    {
      "metric": "Success Rate",
      "target": "95%",
      "measurement": "Automated tests"
    }
  ],

  "business_value": "Why it matters",       // Optional: String

  "source_videos": [                        // Optional: Array of objects
    {
      "video_id": "Video_024",
      "video_title": "Video Title",
      "workflow_demo": true
    }
  ],

  "metadata": {                             // Required: Object
    "created_date": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "status": "active",
    "version_history": []
  }
}
```

**Required Fields:** 10 (entity_type, workflow_id, workflow_name, version, description, category, complexity, estimated_duration, departments, primary_department, milestones, metadata)

**File Size:** Medium (~3-10 KB per file)

---

### JSON Schema: Object Entity

**Location:** `LIBRARIES/LBS_004_Objects/OBJ-XXX-NNN.json`

**Purpose:** Document tangible outputs/deliverables

**Schema:**
```json
{
  "entity_type": "object",                  // Required
  "object_id": "OBJ-XXX-NNN",               // Required: Unique ID
  "object_name": "Object Name",             // Required: Display name
  "type": "Configuration",                  // Required: Type
  "category": "Security",                   // Required: Category

  "description": "What it is",              // Required: Description

  "attributes": {                           // Optional: Object
    "format": "JSON",
    "storage_location": "Path",
    "persistence": "Permanent",
    "sensitivity": "Confidential"
  },

  "produced_by": {                          // Optional: Object
    "action": "ACT-015",
    "task": "TSK-007",
    "milestone": "MLS-003",
    "tool": "TOL-SEC-124"
  },

  "consumed_by": {                          // Optional: Object
    "tasks": ["TSK-009"],
    "tools": ["TOL-QA-031"],
    "workflows": ["WRF-SEC-014"]
  },

  "fields": [                               // Optional: Array of objects
    {
      "field_name": "Field Name",
      "type": "string",
      "required": true,
      "description": "Purpose"
    }
  ],

  "example": {                              // Optional: Object (example data)
    "field_name": "example_value"
  },

  "related_objects": ["OBJ-SEC-511"],       // Optional: Array of object IDs
  "department": "SEC",                      // Optional: Department code

  "metadata": {                             // Required: Object
    "created_date": "YYYY-MM-DD",
    "last_updated": "YYYY-MM-DD",
    "status": "active"
  }
}
```

**Type Values:**
- `Configuration` - Config files
- `Secret` - Credentials, API keys
- `Data` - Data files, datasets
- `Log` - Log files
- `Report` - Report documents
- `Specification` - API specs, schemas

**Required Fields:** 6 (entity_type, object_id, object_name, type, category, description, metadata)

**File Size:** Small-Medium (~1-5 KB per file)

---

## Data Standards

### ID Formats

**Pattern:** `PREFIX-CATEGORY-NUMBER` or `PREFIX-NUMBER`

**Examples:**
- Workflows: `WRF-SEC-014`, `WRF-AUT-001`
- Tools: `TOL-AID-201`, `TOL-SEC-124`
- Objects: `OBJ-SEC-510`, `OBJ-AUT-401`
- Actions: `ACT-001`, `ACT-070`
- Skills: `SKL-042`, `SKL-078`
- Professions: `PRF-001`, `PRF-025`
- Video Queue: `VQ-001`, `VQ-002`
- Search Queue: `SEARCH-001`, `SEARCH-002`
- Research: `RSR-001`, `RSR-024`

**ID Rules:**
- Must be unique across all entities of same type
- Sequential numbering (001, 002, 003...)
- Category codes are 3 letters (SEC, AUT, AID, etc.)
- No spaces or special characters (except hyphen)

---

### Date/Time Formats

**Date Format:** `YYYY-MM-DD` (ISO 8601)
- Examples: `2025-12-04`, `2025-11-24`
- Always 4-digit year, 2-digit month, 2-digit day
- Zero-padded (01, not 1)

**Time Format:** `HH:MM:SS` (24-hour)
- Examples: `00:10:32`, `01:23:45`
- Always 2-digit hour, minute, second
- Zero-padded (00:05:30, not 0:5:30)

**DateTime Format:** `YYYY-MM-DDTHH:MM:SS` (ISO 8601)
- Example: `2025-12-04T14:30:00`
- Used in JSON metadata timestamps

---

### Encoding Standards

**CSV Files:**
- **Encoding:** UTF-8 (no BOM)
- **Line Endings:** CRLF (Windows) or LF (Unix/Mac)
- **Delimiter:** Comma (,)
- **Quote Character:** Double quote (")
- **Escape Character:** Double quote ("") for quotes inside quotes
- **Header Row:** Always present (first row)

**JSON Files:**
- **Encoding:** UTF-8 (no BOM)
- **Line Endings:** LF (Unix/Mac preferred)
- **Indentation:** 2 spaces (no tabs)
- **Quote Character:** Double quote (")
- **Null Values:** Use `null`, not empty string ""
- **Trailing Commas:** Not allowed (JSON spec)

---

### Naming Conventions

**CSV Files:**
- Format: `Entity_Name_Master.csv`
- Examples: `Search_Queue_Master.csv`, `Video_Queue_Master.csv`
- Use underscores for spaces
- Capitalize first letter of each word
- Always end with `.csv`

**JSON Files:**
- Format: `PREFIX-XXX-NNN_Entity_Name.json`
- Examples: `TOL-SEC-124_ScaleKit_Dashboard.json`, `WRF-AUT-001_Web_Scraping.json`
- Use underscores for spaces in entity name
- Match entity ID exactly
- Always end with `.json`

**Field Names:**
- **CSV:** Use underscores, capitalize first letter (e.g., `Queue_ID`, `Video_Title`)
- **JSON:** Use snake_case, lowercase (e.g., `tool_id`, `video_title`)

---

## Field Definitions

### Common CSV Fields

**ID Fields:**
- `Queue_ID`, `Search_ID`, `RSR_ID` - Unique identifier
- Format: PREFIX-NNN (e.g., VQ-001, SEARCH-001)
- Sequential numbering
- Never null/empty

**Person Fields:**
- `Employee`, `Added_By`, `Selected_By`, `Created_By` - Person name
- Format: "First Last" (e.g., "Niko Kar", "Maria Designer")
- Use full names, not usernames
- Consistent capitalization

**Date Fields:**
- `Date_Assigned`, `Date_Completed`, `Added_Date`, `Selected_Date`, `Parsed_Date`
- Format: YYYY-MM-DD
- Can be empty (null) if not yet applicable
- Never use placeholder dates (1900-01-01, 0000-00-00)

**Status Fields:**
- `Status` - Current state
- Enum values (predefined list)
- Never freeform text
- Examples: "Pending", "Completed", "Active"

**Text Fields:**
- `Topic`, `Description`, `Notes`, `Video_Title`
- Free text (any characters)
- Use double quotes if contains commas
- No length limit (within reason, <10,000 chars)

**Numeric Fields:**
- `Views`, `Likes`, `Comments`, `Videos_Found` - Integer
- `Priority_Score` - Float (0-100)
- Never negative
- Use 0 for unknown/empty

---

### Common JSON Fields

**Entity Type Fields:**
```json
"entity_type": "tool"           // Required: tool, workflow, object, etc.
"[entity]_id": "PREFIX-XXX-NNN" // Required: Unique ID
"[entity]_name": "Name"         // Required: Display name
```

**Metadata Fields:**
```json
"metadata": {
  "created_date": "YYYY-MM-DD",     // Required: Creation date
  "last_updated": "YYYY-MM-DD",     // Required: Last update
  "created_by": "Department",       // Optional: Creator
  "status": "active",               // Required: active, deprecated
  "version": "1.0",                 // Optional: Version number
  "version_history": []             // Optional: Array of changes
}
```

**Reference Fields:**
```json
"used_in_workflows": ["WRF-XXX-001"]    // Array of workflow IDs
"used_in_tasks": ["TSK-001"]            // Array of task IDs
"tools_required": ["TOL-XXX-001"]       // Array of tool IDs
"related_actions": ["ACT-001"]          // Array of action IDs
"produces_objects": ["OBJ-XXX-001"]     // Array of object IDs
```

**Source Fields:**
```json
"source_videos": [
  {
    "video_id": "Video_023",
    "video_title": "Title",
    "mentions": 12,
    "timestamps": ["00:15:56", "00:20:30"]
  }
]
```

---

## Example Data

### Example: Search_Queue_Master.csv

```csv
Search_ID,Employee,Department,Topic,Search_Query,Status,Videos_Found,Date_Assigned,Date_Completed,Notes
SEARCH-001,John Doe,DEV,Claude AI tutorials,claude tutorial,Completed,20,2025-12-04,2025-12-05,Focus on 2024-2025
SEARCH-002,Maria Designer,DES,UI Design Trends 2025,ui design 2025,In Progress,15,2025-12-04,,Perplexity search
SEARCH-003,Niko Kar,AID,AI Automation Tools,ai automation,Assigned,0,2025-12-04,,Focus on no-code tools
```

---

### Example: Video_Queue_Master.csv

```csv
Queue_ID,Video_ID,Video_Title,Channel_Name,Channel_URL,Video_URL,Views,Likes,Comments,Publish_Date,Duration,Added_By,Added_Date,Status,Selected_By,Selected_Date,Parsed_Date,Topic_Category,Research_Source,Priority_Score,Notes
VQ-001,dQw4w9WgXcQ,Google AI Studio Full Walkthrough,AI for Grownups,[To be extracted],https://youtube.com/watch?v=dQw4w9WgXcQ,1500000,45000,2300,2025-10-15,00:10:32,Niko Kar,2025-11-24,Pending,,,,AI Tools Overview,Perplexity,75.5,Comprehensive overview of features
VQ-003,xYz789GhI12,UI Design Trends for 2025,Design Masters,[To be extracted],https://youtube.com/watch?v=xYz789GhI12,2500000,98000,4500,2025-11-20,00:12:45,Niko Kar,2025-11-24,Selected,Niko Kar,2025-11-24,,UI Design Trends,Perplexity,92.8,Comprehensive overview of upcoming trends
VQ-005,mNo234OpQ56,Social Media Marketing Strategies,Marketing Pro,[To be extracted],https://youtube.com/watch?v=mNo234OpQ56,320000,8500,650,2025-11-15,00:07:55,SMM Manager,2025-11-24,Parsed,SMM Manager,2025-11-23,2025-11-24,Social Media Marketing,YouTube,68.7,Effective strategies for campaigns
```

---

### Example: Tool JSON (TOL-SEC-124_ScaleKit_Dashboard.json)

```json
{
  "entity_type": "tool",
  "tool_id": "TOL-SEC-124",
  "tool_name": "ScaleKit Dashboard",
  "category": "Auth",
  "vendor": "ScaleKit",
  "description": "Web-based dashboard for managing OAuth 2.1 scopes, permissions, and MCP server registrations",

  "key_features": [
    "Development + production environments",
    "MCP-specific configuration area",
    "Scope definition (e.g., search:read)",
    "Dynamic client registration",
    ".well-known metadata generator"
  ],

  "use_cases": [
    "Secure remote MCP servers with OAuth 2.1",
    "Manage IAM scopes for AI agents",
    "Configure breadcrumb-based auth flows"
  ],

  "pricing": {
    "model": "Freemium",
    "tiers": "Free tier available, paid plans for production"
  },

  "integration": {
    "api_available": true,
    "platforms": ["Web"],
    "integrates_with": ["TOL-SEC-125", "TOL-AID-201"]
  },

  "used_in_workflows": ["WRF-SEC-014"],
  "used_in_tasks": ["TSK-004", "TSK-005", "TSK-006"],
  "related_actions": ["ACT-030", "ACT-055"],
  "produces_objects": ["OBJ-SEC-514", "OBJ-SEC-515"],

  "source_videos": [
    {
      "video_id": "Video_024",
      "video_title": "OAuth for Remote MCP Servers",
      "mentions": 12,
      "timestamps": ["00:15:56", "00:17:20", "00:19:50"]
    }
  ],

  "departments": ["SEC", "AID"],
  "skills_required": ["SKL-078"],

  "documentation": {
    "vendor_site": "https://scalekit.com",
    "api_docs": "https://docs.scalekit.com",
    "tutorials": []
  },

  "metadata": {
    "created_date": "2025-12-04",
    "last_updated": "2025-12-04",
    "created_by": "AI Department",
    "status": "active"
  }
}
```

---

### Example: Workflow JSON (WRF-SEC-014_Secure_MCP_OAuth.json)

```json
{
  "entity_type": "workflow",
  "workflow_id": "WRF-SEC-014",
  "workflow_name": "Secure MCP OAuth 2.1 Implementation",
  "version": "1.0",

  "description": "Protect a remote MCP server using OAuth 2.1 standard, ensuring only authenticated clients can execute tools",
  "category": "Security",
  "complexity": "Medium-High",
  "estimated_duration": "60-90 minutes",

  "departments": ["SEC", "AID", "QA"],
  "primary_department": "SEC",

  "milestones": [
    {
      "milestone_id": "MLS-001",
      "milestone_name": "Prepare Baseline MCP Server",
      "objective": "Stand up FastMCP-powered Tavilli server locally on HTTP transport",
      "tasks": ["TSK-001", "TSK-002", "TSK-003"],
      "department": "AID",
      "duration": "15 min"
    },
    {
      "milestone_id": "MLS-002",
      "milestone_name": "Configure ScaleKit Authorization",
      "objective": "Set up ScaleKit environments, scopes, and MCP registration",
      "tasks": ["TSK-004", "TSK-005", "TSK-006"],
      "department": "SEC",
      "duration": "20 min"
    },
    {
      "milestone_id": "MLS-003",
      "milestone_name": "Implement OAuth Discovery & Middleware",
      "objective": "Publish well-known endpoint and build token validation middleware",
      "tasks": ["TSK-007", "TSK-008", "TSK-009"],
      "department": "SEC",
      "duration": "25 min"
    },
    {
      "milestone_id": "MLS-004",
      "milestone_name": "Test Authenticated Workflow",
      "objective": "Verify OAuth breadcrumb discovery and authenticated tool execution",
      "tasks": ["TSK-010", "TSK-011", "TSK-012"],
      "department": "QA",
      "duration": "20 min"
    }
  ],

  "tools_required": [
    "TOL-AID-201",
    "TOL-SEC-124",
    "TOL-SEC-125",
    "TOL-AID-205",
    "TOL-QA-031"
  ],

  "skills_required": ["SKL-042", "SKL-078", "SKL-019"],
  "responsibilities": ["RSP-333", "RSP-418", "RSP-410"],

  "prerequisites": [
    "ScaleKit account with development environment",
    "Tavilli API key",
    "FastMCP server installed",
    "Python 3.8+ environment"
  ],

  "deliverables": [
    "Authenticated MCP server with OAuth 2.1",
    "Validated breadcrumb discovery flow",
    "Successful authenticated tool call"
  ],

  "kpis": [
    {
      "metric": "Auth Success Rate",
      "target": "100%",
      "measurement": "Automated test suite"
    },
    {
      "metric": "Tool Availability",
      "target": "99.9%",
      "measurement": "Uptime monitoring"
    }
  ],

  "business_value": "Enables secure monetization of MCP tools, ensures compliance with OAuth 2.1 standard, reduces unauthorized access risk",

  "source_videos": [
    {
      "video_id": "Video_024",
      "video_title": "OAuth for Remote MCP Servers (Step by Step)",
      "workflow_demo": true
    }
  ],

  "metadata": {
    "created_date": "2025-12-04",
    "last_updated": "2025-12-04",
    "status": "active",
    "version_history": []
  }
}
```

---

## Import/Export

### CSV Import

**Python (pandas):**
```python
import pandas as pd

# Read CSV
df = pd.read_csv('Video_Queue_Master.csv', encoding='utf-8')

# Access data
for index, row in df.iterrows():
    queue_id = row['Queue_ID']
    status = row['Status']
    print(f"{queue_id}: {status}")
```

**Python (csv module):**
```python
import csv

# Read CSV
with open('Video_Queue_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        queue_id = row['Queue_ID']
        status = row['Status']
        print(f"{queue_id}: {status}")
```

---

### CSV Export

**Python (pandas):**
```python
import pandas as pd

# Create DataFrame
data = {
    'Queue_ID': ['VQ-001', 'VQ-002'],
    'Status': ['Pending', 'Selected'],
    'Priority_Score': [75.5, 92.8]
}
df = pd.DataFrame(data)

# Write CSV
df.to_csv('output.csv', index=False, encoding='utf-8')
```

**Python (csv module):**
```python
import csv

# Data
rows = [
    {'Queue_ID': 'VQ-001', 'Status': 'Pending', 'Priority_Score': 75.5},
    {'Queue_ID': 'VQ-002', 'Status': 'Selected', 'Priority_Score': 92.8}
]

# Write CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Queue_ID', 'Status', 'Priority_Score']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

---

### JSON Import

**Python:**
```python
import json

# Read JSON
with open('TOL-SEC-124_ScaleKit_Dashboard.json', 'r', encoding='utf-8') as f:
    tool = json.load(f)

# Access data
tool_id = tool['tool_id']
tool_name = tool['tool_name']
features = tool['key_features']
print(f"{tool_id}: {tool_name}")
print(f"Features: {len(features)}")
```

---

### JSON Export

**Python:**
```python
import json

# Data
tool = {
    "entity_type": "tool",
    "tool_id": "TOL-SEC-124",
    "tool_name": "ScaleKit Dashboard",
    "category": "Auth",
    "metadata": {
        "created_date": "2025-12-04",
        "status": "active"
    }
}

# Write JSON
with open('TOL-SEC-124.json', 'w', encoding='utf-8') as f:
    json.dump(tool, f, indent=2, ensure_ascii=False)
```

---

## Validation

### CSV Validation

**Check CSV Structure:**
```python
import csv

def validate_csv(filepath, required_fields):
    """Validate CSV has all required fields"""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        missing = set(required_fields) - set(header)
        if missing:
            print(f"Missing fields: {missing}")
            return False

        print(f"✓ All required fields present")
        return True

# Usage
required = ['Queue_ID', 'Status', 'Priority_Score']
validate_csv('Video_Queue_Master.csv', required)
```

**Check ID Format:**
```python
import re

def validate_queue_id(queue_id):
    """Validate Queue_ID format: VQ-NNN"""
    pattern = r'^VQ-\d{3}$'
    if re.match(pattern, queue_id):
        print(f"✓ {queue_id} valid")
        return True
    else:
        print(f"✗ {queue_id} invalid (expected VQ-NNN)")
        return False

# Usage
validate_queue_id('VQ-001')  # ✓ Valid
validate_queue_id('VQ-1')    # ✗ Invalid
```

**Check Date Format:**
```python
from datetime import datetime

def validate_date(date_str):
    """Validate date format: YYYY-MM-DD"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        print(f"✓ {date_str} valid")
        return True
    except ValueError:
        print(f"✗ {date_str} invalid (expected YYYY-MM-DD)")
        return False

# Usage
validate_date('2025-12-04')  # ✓ Valid
validate_date('12/04/2025')  # ✗ Invalid
```

---

### JSON Validation

**Check JSON Syntax:**
```python
import json

def validate_json_syntax(filepath):
    """Validate JSON syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"✓ {filepath} is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ {filepath} has JSON error: {e}")
        return False

# Usage
validate_json_syntax('TOL-SEC-124.json')
```

**Check Required Fields:**
```python
import json

def validate_json_fields(filepath, required_fields):
    """Validate JSON has all required fields"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    missing = set(required_fields) - set(data.keys())
    if missing:
        print(f"✗ Missing fields: {missing}")
        return False

    print(f"✓ All required fields present")
    return True

# Usage
required = ['entity_type', 'tool_id', 'tool_name', 'metadata']
validate_json_fields('TOL-SEC-124.json', required)
```

**Check ID Format:**
```python
import re
import json

def validate_tool_id(filepath):
    """Validate Tool ID format: TOL-XXX-NNN"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tool_id = data.get('tool_id', '')
    pattern = r'^TOL-[A-Z]{3}-\d{3}$'

    if re.match(pattern, tool_id):
        print(f"✓ {tool_id} valid")
        return True
    else:
        print(f"✗ {tool_id} invalid (expected TOL-XXX-NNN)")
        return False

# Usage
validate_tool_id('TOL-SEC-124.json')
```

---

## Best Practices

### CSV Best Practices

**Do:**
✅ Always include header row
✅ Use UTF-8 encoding
✅ Quote fields with commas, newlines, or quotes
✅ Use consistent date format (YYYY-MM-DD)
✅ Keep field names simple (no special characters)
✅ Use 0 for unknown numeric values (not empty)
✅ Validate data before writing

**Don't:**
❌ Use tabs as delimiters (use commas)
❌ Mix date formats (MM/DD/YYYY and YYYY-MM-DD)
❌ Leave required fields empty
❌ Use line breaks within fields (unless quoted)
❌ Use non-ASCII characters in field names
❌ Use inconsistent capitalization

---

### JSON Best Practices

**Do:**
✅ Use 2-space indentation
✅ Use double quotes (not single quotes)
✅ Use `null` for missing values (not empty string)
✅ Keep object keys consistent (snake_case)
✅ Validate JSON syntax before saving
✅ Include metadata fields (created_date, status)
✅ Use arrays for multiple values (not comma-separated strings)

**Don't:**
❌ Use trailing commas (invalid JSON)
❌ Use comments (not supported in JSON)
❌ Use single quotes for strings
❌ Leave required fields as `null`
❌ Use inconsistent field names (tool_id vs toolId)
❌ Create deeply nested structures (>5 levels)

---

## Troubleshooting

### Problem 1: CSV Won't Open in Excel

**Symptom:** CSV opens but shows garbled characters or wrong encoding

**Solution:**
```bash
# Convert to UTF-8 with BOM for Excel compatibility
# In Python:
import pandas as pd
df = pd.read_csv('file.csv', encoding='utf-8')
df.to_csv('file_excel.csv', index=False, encoding='utf-8-sig')

# Or use Excel import wizard:
# 1. Open Excel
# 2. Data → From Text/CSV
# 3. Select file
# 4. Choose UTF-8 encoding
# 5. Import
```

---

### Problem 2: JSON Syntax Error

**Symptom:**
```
JSONDecodeError: Expecting ',' delimiter: line 42 column 5
```

**Cause:** Trailing comma, missing comma, or unquoted key

**Solution:**
```bash
# Use JSON formatter to find error
cat file.json | python -m json.tool

# Or use online JSON validator: https://jsonlint.com

# Common fixes:
# 1. Remove trailing comma: {"key": "value",} → {"key": "value"}
# 2. Add missing comma: {"key1": "value1" "key2": "value2"} → {"key1": "value1", "key2": "value2"}
# 3. Quote keys: {key: "value"} → {"key": "value"}
```

---

### Problem 3: CSV Field Mismatch

**Symptom:** Script expects field "Queue_ID" but CSV has "QueueID"

**Solution:**
```python
# Check actual field names
import csv
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)

# Either:
# 1. Fix CSV header to match expected names
# 2. Or update script to use actual names
```

---

### Problem 4: Duplicate IDs

**Symptom:** Two rows with same Queue_ID or tool_id

**Solution:**
```python
# Check for duplicates
import pandas as pd
df = pd.read_csv('Video_Queue_Master.csv')
duplicates = df[df.duplicated('Queue_ID', keep=False)]
print(duplicates)

# Fix: Update duplicate IDs to next available
# Use video_id_scanner.py to get next ID
```

---

## Related Documentation

- **[03_SEARCH_QUEUE_COMPLETE.md](03_SEARCH_QUEUE_COMPLETE.md)** - Search Queue CSV usage
- **[04_VIDEO_QUEUE_COMPLETE.md](04_VIDEO_QUEUE_COMPLETE.md)** - Video Queue CSV usage
- **[07_INTEGRATION_COMPLETE.md](07_INTEGRATION_COMPLETE.md)** - JSON entity creation
- **[08_SCRIPTS_DETAILED.md](08_SCRIPTS_DETAILED.md)** - Scripts that read/write these files
- **[13_TROUBLESHOOTING.md](13_TROUBLESHOOTING.md)** - Additional troubleshooting

---

## Version History

- **v1.0** (2025-12-04): Initial documentation
  - 3 CSV file schemas documented
  - 3 JSON entity schemas documented
  - Data standards defined
  - Validation examples added
  - Import/export code samples
  - Best practices compiled
  - 4 troubleshooting scenarios

---

**Created:** 2025-12-04
**Last Updated:** 2025-12-04
**Status:** ✅ Complete
**Maintainer:** AI Department
