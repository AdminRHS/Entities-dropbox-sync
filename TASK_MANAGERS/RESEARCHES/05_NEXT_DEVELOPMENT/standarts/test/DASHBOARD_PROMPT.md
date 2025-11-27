---
category: ROOT
subcategory: root
type: analysis
source_id: DASHBOARD_PROMPT
title: DASHBOARD PROMPT
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# DASHBOARD PROMPT

## Summary
- TODO

## Context
- TODO

## Data / Content
# Prompt for RESEARCHES Dashboard Generation

**Role:** Senior Full Stack Developer (Node.js/React)
**Task:** Build a web-based dashboard to manage the video research and taxonomy integration workflow (RESEARCHES).

## Context
The "RESEARCHES" system is a workflow for discovering, processing, and integrating video content.
Data is stored in `ENTITIES/TASK_MANAGERS/RESEARCHES` as CSV files and Markdown reports.

## Data Sources
The dashboard must read data from the following files.
**IMPORTANT**: Since different users have different local paths to Dropbox, the root path must be configurable via an Environment Variable (e.g., `DROPBOX_ROOT`).

1.  **Master Research List**: `${DROPBOX_ROOT}/ENTITIES/TASK_MANAGERS/RESEARCHES/RESEARCHES_Master_List.csv`
    *   Columns: `RSR_ID`, `Name`, `Description`, `Department`, `Category`, `File_Path`, `Status`
2.  **Search Queue**: `${DROPBOX_ROOT}/ENTITIES/TASK_MANAGERS/RESEARCHES/00_SEARCH_QUEUE/Search_Queue_Master.csv`
3.  **Video Queue**: `${DROPBOX_ROOT}/ENTITIES/TASK_MANAGERS/RESEARCHES/01_VIDEO_QUEUE/Video_Queue_Master.csv`
    *   Contains video metadata, processing status, and priority.

## Functional Requirements

### 1. Overview Page
*   **KPI Cards**:
    *   Total Active Researches.
    *   Pending Search Tasks (Search Queue count).
    *   Videos Pending Processing (Video Queue count).
    *   Department Distribution (Pie/Doughnut chart).

### 2. Search Queue Tab (00_SEARCH_QUEUE)
*   Data Table displaying active search assignments.
*   Filter by Assignee and Status.
*   Highlight high-priority topics.

### 3. Video Queue Tab (01_VIDEO_QUEUE)
*   Data Table for videos awaiting processing.
*   Status indicators (e.g., Selected, Transcribed, Integration).
*   Sortable by Priority.
*   Clickable YouTube links.

### 4. Researches Status Tab
*   Display data from `RESEARCHES_Master_List.csv`.
*   Show status for each research entity (RSR-XXX).
*   **File Integrity Check**: The backend must verify if the file exists at the location specified in `File_Path` and return a boolean status (Exists/Missing) to the frontend. Display this as a status icon (✅/❌).

## Technical Stack Requirements
*   **Backend**: Node.js (Express or similar lightweight server).
    *   Must handle CSV parsing (use `csv-parser` or `papaparse`).
    *   Must provide API endpoints to serve the parsed data to the frontend.
    *   Must implement the file system check for the "Researches Status" tab.
    *   **Configuration**: Use `dotenv` to manage the `DROPBOX_ROOT` path.
*   **Frontend**: React (preferred) or vanilla HTML/JS.
    *   Use a modern UI library (e.g., Tailwind CSS, Material UI, or Ant Design) for a professional dark-mode look.
    *   Use `recharts` or `chart.js` for visualizations.

## Implementation Steps
1.  **Server Setup**: Create a Node.js server to read the CSV files and serve them as JSON APIs.
2.  **Frontend Setup**: Initialize a React app (or simple HTML page).
3.  **Data Fetching**: Connect frontend to backend APIs.
4.  **UI Construction**: Build the Dashboard layout with Sidebar navigation and the 4 required views.

## Code Skeleton
Please provide the project structure, `package.json` dependencies, `server.js` code for the API, and the main frontend component code.


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
