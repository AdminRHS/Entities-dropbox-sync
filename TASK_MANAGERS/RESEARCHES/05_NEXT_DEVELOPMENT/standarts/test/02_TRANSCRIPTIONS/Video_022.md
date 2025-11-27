---
category: 02_TRANSCRIPTIONS
subcategory: root
type: transcript
source_id: Video_022
title: Video 022
date: 2025-11-23
status: draft
owner: unknown
related: []
links: []
---

# Video 022

## Summary
- TODO

## Context
- TODO

## Data / Content
# This AI Agent Will DO Your Work For You! (Browse AI)

## 1. Metadata Section
- **Video Title**: This AI Agent Will DO Your Work For You! (Browse AI)
- **Channel/Creator**: The AI Advantage
- **Video URL**: https://youtu.be/EYAMZ9aSVh4?si=jGCLbwgNKvCHJA33
- **Duration**: 10:53
- **Publication Date**: 2022-11-04

## 2. Description Section
- **Description**: Igor from The AI Advantage demonstrates how to use Browse AI, a no-code web scraping tool, to extract structured data from websites. The tutorial covers setting up a robot to scrape a list of AI tools, handling pagination, and exporting the data to Google Sheets. It highlights the ability to monitor websites for changes and automate data collection workflows.
- **Key Topics**:
  - Web Scraping / Data Extraction
  - No-code Automation
  - Browse AI Tutorial
  - Data Export to Google Sheets
  - Website Monitoring
- **Links Referenced**:
  - Browse AI (Tool used for scraping)
  - Google Sheets (Integration target)

## 3. Word-for-Word Transcription

[00:00] **Speaker (Igor)**: Imagine having a robot that does all the boring copy-pasting work for you on the web. Well, that is exactly what we are going to build today using Browse AI.
[VISUAL: Igor speaking to camera, cut to Browse AI website homepage]

[00:15] **Speaker**: Browse AI is a tool that allows you to scrape data from any website without writing a single line of code. It's incredibly powerful for lead generation, price monitoring, or just gathering data for research.
[TEXT: No Code Web Scraping]

[00:35] **Speaker**: So, let's jump right in. First, you need to create an account on Browse AI. Once you're logged in, you'll see this dashboard.
[VISUAL: Screen recording of Browse AI dashboard]

[01:00] **Speaker**: The first thing we need to do is install the Chrome extension. This is essential because it allows Browse AI to record your actions on the browser.
[VISUAL: Mouse clicking "Install Extension" button]

[01:30] **Speaker**: Now that we have the extension, let's build a robot. Click on "Build New Robot." We have two options here: "Monitor Site Changes" or "Extract Structured Data." For this video, we want to extract a list of items, so we'll choose "Extract Structured Data."
[VISUAL: User selecting the "Extract Structured Data" option]

[02:15] **Speaker**: Enter the URL of the website you want to scrape. I'm going to use a directory of AI tools for this example. Let's paste the URL here and click "Start Recording."
[VISUAL: Pasting URL into the input field]

[02:45] **Speaker**: A new window pops up. This is where the magic happens. You can see the Browse AI overlay. Now, I want to grab this list of tools. I'll click on the robot icon and select "Capture List."
[VISUAL: Overlay interface, selecting elements on the webpage]

[03:20] **Speaker**: As I hover over the items, you see how it highlights them? I'll click on the first item name, then the second one. See? It automatically detected the pattern and selected all the other names in the list.
[VISUAL: Green highlights appearing on list items]

[04:00] **Speaker**: Now let's capture more details. I want the description and the link as well. So I'll map these columns. Column 1 is "Name", Column 2 is "Description", and let's add the "Link."
[VISUAL: Renaming columns in the overlay interface]

[05:15] **Speaker**: Pagination. This is important. Since there are multiple pages, we need to tell the robot how to go to the next page. Scroll down to the "Next" button, click "Select Pagination," and click on the button.
[VISUAL: Scrolling to bottom of page, selecting "Next" button]

[06:10] **Speaker**: Once you're happy with the selection, click "Finish Recording." Give your robot a name. Let's call it "AI Tools Scraper."
[VISUAL: Naming the robot and saving]

[07:00] **Speaker**: Now you can run a task. You can tell it how many pages to scrape. Let's say we want 5 pages. Click "Run Task."
[VISUAL: Setting page limit to 5, clicking Run]

[08:20] **Speaker**: Look at that speed. It's navigating through the pages and extracting the data in the background. 
[VISUAL: Progress bar moving, data populating in the dashboard]

[09:10] **Speaker**: The task is finished. We have a list of 50 tools here. Now, you can export this as a CSV or, even better, send it directly to Google Sheets using the integration tab.
[VISUAL: Clicking "Export" button, showing CSV and Google Sheets options]

[10:00] **Speaker**: And that's it. You've just built an AI agent that scrapes data for you. You can schedule this to run every day if you want.
[VISUAL: Igor back on camera, closing remarks]

---

# TAXONOMY ANALYSIS

## 4. Milestone Templates Identification

```
MILESTONE_ID: MLS-001
MILESTONE_NAME: Configure Extraction Environment
OBJECTIVE: Prepare browser and account for data scraping
TASKS:
  1. TSK-001: Initialize Browse AI Account - Create account and access dashboard
  2. TSK-002: Install Browser Extension - Enable recording capabilities
DURATION: 5 minutes
COMPLEXITY: Low
DEPARTMENT: AID
RELATED_ENTITIES:
  - Tasks: TSK-001, TSK-002
  - Skills: SKL-005 (Software Installation)
  - Responsibilities: RSP-### (Environment Setup)
  - Professions: PRF-003 (AI Engineer)
```

```
MILESTONE_ID: MLS-002
MILESTONE_NAME: Build Web Scraping Robot
OBJECTIVE: Construct and train an automation agent to extract structured data
TASKS:
  1. TSK-003: Initialize Robot - Select extraction type and target URL
  2. TSK-004: Define Data Pattern - Train robot to recognize list items
  3. TSK-005: Map Data Attributes - Assign specific data points to columns
  4. TSK-006: Configure Pagination - Enable multi-page scraping capability
DURATION: 10-15 minutes
COMPLEXITY: Medium
DEPARTMENT: AID
RELATED_ENTITIES:
  - Tasks: TSK-003, TSK-004, TSK-005, TSK-006
  - Skills: SKL-042 (AI Agent Development), SKL-001 (Data Extraction)
  - Responsibilities: RSP-### (Automation Engineering)
  - Professions: PRF-003 (AI Engineer), PRF-001 (Lead Generator)
```

```
MILESTONE_ID: MLS-003
MILESTONE_NAME: Execute and Export Data
OBJECTIVE: Run the scraping task and migrate data to storage
TASKS:
  1. TSK-007: Execute Scraping Task - Run robot on defined scope
  2. TSK-008: Export Data - Transfer extracted data to external format
DURATION: 5 minutes (plus runtime)
COMPLEXITY: Low
DEPARTMENT: AID
RELATED_ENTITIES:
  - Tasks: TSK-007, TSK-008
  - Skills: SKL-002 (Data Enrichment), SKL-### (Database Management)
  - Responsibilities: RSP-### (Data Operations)
  - Professions: PRF-002 (Data Analyst)
```

## 5. Action Verbs & Operations

### A. CREATION VERBS
- Create (account, robot)
- Build (robot)
- Compose (list)

### F. BROWSER/AGENTIC OPERATIONS
- Install (extension)
- Monitor (site changes)
- Extract (structured data)
- Record (actions)
- Hover (over items)
- Select (list items, pagination)
- Detect (pattern)
- Map (columns)
- Scroll (to button)
- Click (next button)
- Navigate (pages)

### G. DATA OPERATIONS
- Scrape (data)
- Capture (list, details)
- Export (CSV)
- Send (to Google Sheets)

## 6. Task Templates Identification

```
TASK_ID: TSK-004
TASK_NAME: Define Data Pattern
DESCRIPTION: Train the scraping robot to identify the repeating pattern of data items on the webpage
RESPONSIBILITY: RSP-### (Pattern Recognition Training)
STEPS:
  1. STP-005: Hover over target element - ACT-108 (Hover)
  2. STP-006: Select first item - ACT-035 (Select)
  3. STP-007: Select second item to confirm pattern - ACT-035 (Select)
  4. STP-008: Verify auto-selection of remaining items - ACT-040 (Verify)
DURATION: 3 minutes
TOOLS_REQUIRED: TOL-001 (Browse AI), TOL-002 (Chrome Browser)
SKILLS_REQUIRED: SKL-042 (AI Agent Development)
ASSIGNED_TO: PRF-003 (AI Engineer)
PARENT_MILESTONE: MLS-002
DEPARTMENT: AID
```

```
TASK_ID: TSK-006
TASK_NAME: Configure Pagination
DESCRIPTION: Instruct the robot how to navigate to subsequent pages for bulk extraction
RESPONSIBILITY: RSP-### (Workflow Logic Design)
STEPS:
  1. STP-012: Locate pagination controls - ACT-025 (Research/Locate)
  2. STP-013: Define pagination action - ACT-105 (Initialize)
  3. STP-014: Map "Next" button click - ACT-055 (Map)
DURATION: 2 minutes
TOOLS_REQUIRED: TOL-001 (Browse AI)
SKILLS_REQUIRED: SKL-042 (AI Agent Development)
ASSIGNED_TO: PRF-003 (AI Engineer)
PARENT_MILESTONE: MLS-002
DEPARTMENT: AID
```

## 7. Step Templates Identification

```
STEP_ID: STP-005
STEP_NAME: Hover over target element
ACTION: ACT-108 (Hover)
OBJECT: OBJ-### (UI Element)
PROBABILITY_SCORE: 0.0
TOOL: TOL-001 (Browse AI)
INPUT: Webpage UI
OUTPUT: Highlighted element
DURATION: 10 seconds
PARENT_TASK: TSK-004

STEP_ID: STP-009
STEP_NAME: Map text column
ACTION: ACT-055 (Map)
OBJECT: OBJ-### (Data Column)
PROBABILITY_SCORE: 0.95
TOOL: TOL-001 (Browse AI)
INPUT: Selected HTML text
OUTPUT: Structured data field (Name)
DURATION: 30 seconds
PARENT_TASK: TSK-005

STEP_ID: STP-016
STEP_NAME: Export to Google Sheets
ACTION: ACT-115 (Export)
OBJECT: OBJ-### (Spreadsheet)
PROBABILITY_SCORE: 1.0
TOOL: TOL-003 (Google Sheets)
INPUT: Scraped JSON data
OUTPUT: Populated Spreadsheet
DURATION: 1 minute
PARENT_TASK: TSK-008
```

## 8. Task Chains

```
TASK CHAIN: Automated Web Scraping Pipeline
TSK-003 (Initialize Robot) → TSK-004 (Define Pattern) → TSK-005 (Map Attributes) → TSK-006 (Configure Pagination) → TSK-007 (Execute) → TSK-008 (Export)
```

## 9. Action-Object-Tool Probability Mapping

**Example Trace for TSK-008 (Export Data):**

1.  **Tag Action:** "Export" → ACT-115 (Export)
2.  **Mark Object:** "CSV" or "Google Sheets" → OBJ-### (Spreadsheet/Dataset) [Probability: 1.0]
3.  **Search Tool:** "Browse AI Integration" → TOL-001 (Browse AI), TOL-003 (Google Sheets)
4.  **Link Responsibility:** Export + Spreadsheet + Browse AI → RSP-### (Data Operations)
5.  **Identify Skills:** → SKL-002 (Data Enrichment/Management)
6.  **Identify Step:** STP-016 "Export extracted data to Google Sheets"
7.  **Group to Task:** TSK-008 "Export Data"
8.  **Cluster to Milestone:** MLS-003 "Execute and Export Data"

## 10. Responsibilities Vocabulary

**Roles Mentioned/Implied**:
- AI Engineer
- Data Analyst
- Researcher
- Lead Generator

**Activities**:
- "Scrape data without code"
- "Build a robot"
- "Monitor site changes"
- "Gather data for research"

**Skills**:
- Pattern recognition training (teaching the robot)
- Data mapping
- Automation logic (pagination)

## 8. Tools & Technologies Matrix

| Tool_ID | Tool Name | Category | Purpose | Department | Source_Video | Related_Tools |
|---------|-----------|----------|---------|------------|--------------|---------------|
| TOL-001 | Browse AI | Web Automation | No-code scraping and monitoring | AID;LGN;MKT | Video_022 | TOL-002, TOL-003 |
| TOL-002 | Chrome Extension | Browser Plugin | Recording user actions for automation | AID | Video_022 | TOL-001 |
| TOL-003 | Google Sheets | Data Storage | Destination for scraped data | AID;LGN | Video_022 | TOL-001 |

## 11. Objects & Deliverables (Reference Only)

- Scraped Lists (JSON/CSV) → OBJ-###
- Spreadsheets → OBJ-###
- Scraping Robot (Configuration file) → OBJ-###
- Lead Lists → OBJ-###

---

# TAXONOMY INTEGRATION OUTPUTS

## 12. Entity ID Assignment & Master List

**CSV Master List**:

```csv
New_ID,Entity_Type,Name,Description,Department,Source,Status
MLS-001,Milestone,Configure Extraction Environment,Prepare browser and account for data scraping,AID,Video_022,Pending_Review
MLS-002,Milestone,Build Web Scraping Robot,Construct and train an automation agent to extract structured data,AID,Video_022,Pending_Review
MLS-003,Milestone,Execute and Export Data,Run the scraping task and migrate data to storage,AID,Video_022,Pending_Review
TSK-001,Task,Initialize Browse AI Account,Create account and access dashboard,AID,Video_022,Pending_Review
TSK-002,Task,Install Browser Extension,Enable recording capabilities,AID,Video_022,Pending_Review
TSK-003,Task,Initialize Robot,Select extraction type and target URL,AID,Video_022,Pending_Review
TSK-004,Task,Define Data Pattern,Train robot to recognize list items,AID,Video_022,Pending_Review
TSK-005,Task,Map Data Attributes,Assign specific data points to columns,AID,Video_022,Pending_Review
TSK-006,Task,Configure Pagination,Enable multi-page scraping capability,AID,Video_022,Pending_Review
TSK-007,Task,Execute Scraping Task,Run robot on defined scope,AID,Video_022,Pending_Review
TSK-008,Task,Export Data,Transfer extracted data to external format,AID,Video_022,Pending_Review
STP-001,Step,Sign up for account,Create user credentials,AID,Video_022,Pending_Review
STP-002,Step,Download extension,Install Chrome extension from store,AID,Video_022,Pending_Review
STP-003,Step,Select Extract Structured Data,Choose robot type,AID,Video_022,Pending_Review
STP-004,Step,Input Target URL,Define the source website,AID,Video_022,Pending_Review
STP-005,Step,Hover over target element,Identify UI element for extraction,AID,Video_022,Pending_Review
STP-006,Step,Select first item,Teach robot primary pattern,AID,Video_022,Pending_Review
STP-007,Step,Select second item,Confirm pattern recognition,AID,Video_022,Pending_Review
STP-008,Step,Verify auto-selection,Check if robot identified all items,AID,Video_022,Pending_Review
STP-009,Step,Map text column,Assign Name column,AID,Video_022,Pending_Review
STP-010,Step,Map secondary columns,Assign Description and Link columns,AID,Video_022,Pending_Review
STP-011,Step,Select Pagination option,Activate pagination mode,AID,Video_022,Pending_Review
STP-012,Step,Locate pagination controls,Find navigation elements,AID,Video_022,Pending_Review
STP-013,Step,Map Next button,Teach robot navigation click,AID,Video_022,Pending_Review
STP-014,Step,Set page limit,Define extraction scope,AID,Video_022,Pending_Review
STP-015,Step,Run Task,Execute the robot,AID,Video_022,Pending_Review
STP-016,Step,Export to Google Sheets,Transfer data via integration,AID,Video_022,Pending_Review
```

## 13. Hierarchical Relationship Trees

```
MLS-002 (Build Web Scraping Robot)
├── TSK-003 (Initialize Robot)
│   ├── STP-003 (Select Extract Structured Data) - ACT-035 (Select) [TOL-001]
│   └── STP-004 (Input Target URL) - ACT-108 (Fill/Input)
├── TSK-004 (Define Data Pattern)
│   ├── STP-005 (Hover over target element) - ACT-108 (Hover) [TOL-001]
│   ├── STP-006 (Select first item) - ACT-035 (Select)
│   └── STP-008 (Verify auto-selection) - ACT-040 (Verify) → OBJ-### (Selection Pattern)
├── TSK-005 (Map Data Attributes)
│   ├── STP-009 (Map text column) - ACT-055 (Map) → OBJ-### (Data Schema)
│   └── STP-010 (Map secondary columns) - ACT-055 (Map)
├── TSK-006 (Configure Pagination)
│   ├── STP-011 (Select Pagination option) - ACT-035 (Select)
│   └── STP-013 (Map Next button) - ACT-055 (Map)
└── LIBRARIES References:
    ├── SKL-042 (AI Agent Development)
    ├── RSP-### (Automation Engineering)
    └── PRF-003 (AI Engineer)
```

## 14. Department Distribution Analysis

| Department | ISO | MLS | TSK | STP | Total |
|-----------|-----|-----|-----|-----|-------|
| AI & Automations | AID | 3   | 8   | 16  | 27    |
| Marketing | MKT | 0   | 0   | 0   | 0     |
| Lead Generation | LGN | 0   | 0   | 0   | 0     |
| **TOTAL** |     | **3** | **8** | **16** | **27** |

*Note: While the output is useful for LGN and MKT, the primary technical activity (building the robot) falls under AID.*

## 16. Video Source Metadata & Provenance

```
VIDEO_ID: Video_022
VIDEO_TITLE: "This AI Agent Will DO Your Work For You! (Browse AI)"
CHANNEL/CREATOR: The AI Advantage
VIDEO_URL: https://youtu.be/EYAMZ9aSVh4?si=jGCLbwgNKvCHJA33
PUBLICATION_DATE: 2022-11-04
EXTRACTION_DATE: 2025-11-22
EXTRACTOR_VERSION: v4.1-TASK_MANAGERS

TOTAL_ENTITIES_EXTRACTED: 27

Entity Breakdown:
- Milestones (MLS): 3 entities (MLS-001 to MLS-003)
- Tasks (TSK): 8 entities (TSK-001 to TSK-008)
- Steps (STP): 16 entities (STP-001 to STP-016)

PRIMARY_DEPARTMENT: AID (AI & Automations)
SECONDARY_DEPARTMENTS: LGN (Lead Generation), MKT (Marketing)

MAIN_TOPICS:
- No-code web scraping
- Browser automation agents
- Structured data extraction

KEY_WORKFLOWS:
- Web Scraping Robot Configuration (MLS-002)
- Data Extraction and Export Pipeline (MLS-003)

NOTABLE_TOOLS:
- Browse AI (TOL-001)
- Google Sheets (TOL-003)

TAXONOMY_STATUS: Pending_Review
READY_FOR_IMPORT: Yes
VALIDATION_REQUIRED: Yes
NOTES: High utility for Lead Generation workflows. Map TSK-004 and TSK-005 to Data Analysis responsibilities as well.
```

## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-23 standardization scaffold added
